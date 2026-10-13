# Segurança de TO, IoT e Sistemas Ciberfísicos: Engenharia de Sistemas de Controle Seguros

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções; os capítulos 11–50 (EX031–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: futuros engenheiros que vão projetar, implementar e verificar a segurança de sistemas de controle industrial, de TO e de sistemas ciberfísicos.
- Relação com os livros vizinhos: o livro de engenharia de infraestrutura crítica enfatiza os setores; o livro de mestrado de TO enfatiza o desenho de estudos empíricos. **Este livro trata de construir a segurança de sistemas de controle**.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é um diploma credenciado nem uma habilitação profissional. Não concede autorização para acessar plantas reais. Todas as plantas, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–19 constroem os fundamentos, aplicados à TO desde a primeira página. O Capítulo 20 estabelece o contexto de TO. Os capítulos 21–42 formam o núcleo da área, com ateliês de projeto (25, 35) e laboratórios de verificação (30, 40). Os capítulos 43–50 são de prática e de projeto final. Mantenha os rótulos: **requisito**, **decisão de projeto**, **evidência**, **risco residual**.

### Caso de projeto sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Ashford Batch Plant (ABP)** — reator R-101, tanques de alimentação T-1/T-2, PLC-A, SIS-B, SCADA, historiador | Sistema em projeto | Inventado |
| **Control Network Hardening Programme (CNHP)** | O programa de engenharia | Inventado |
| **Lena Okafor** | Engenheira do CNHP | Inventada |

### Fontes centrais

- NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); Modbus [Application Protocol V1.1b3](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf); Giraldo et al. [CSUR 2018](https://doi.org/10.1145/3203245); Urbina et al. [CCS 2016](https://doi.org/10.1145/2976749.2978388).

## Sumário

1. [Cálculo I](#ch-01)
2. [Matemática discreta](#ch-02)
3. [Física para computação](#ch-03)
4. [Programação I](#ch-04)
5. [Comunicação em engenharia](#ch-05)
6. [Cálculo II](#ch-06)
7. [Probabilidade e estatística](#ch-07)
8. [Arquitetura de computadores](#ch-08)
9. [Programação II](#ch-09)
10. [Ética e segurança na engenharia](#ch-10)

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

As [resoluções](#worked-results) contêm EX001–EX030. As [referências](#references) encerram o livro.

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) modelar o nível de um tanque como a integral da vazão líquida; (2) usar esse modelo para calcular quanto tempo os operadores têm depois que uma bomba para; (3) explicar por que esse tempo é uma grandeza de segurança, e não apenas de processo.

### 1.1 O nível é vazão acumulada

O tanque de alimentação T-1 da Ashford Batch Plant (ABP) contém V(t) metros cúbicos. Se a bomba de reposição para em t = 0 e o reator continua puxando q(t) m³/h, então V(t) = V₀ − ∫₀ᵗ q(s) ds. O nível cai exatamente tão rápido quanto a vazão de saída, e o tempo até ele chegar ao volume mínimo seguro retido V_min é o t* que resolve ∫₀^t* q(s) ds = V₀ − V_min. Quando q é constante, isso é (V₀ − V_min)/q; quando q varia, você integra.

### 1.2 Por que um engenheiro de segurança se importa

Um atacante que consegue parar uma bomba ou falsificar uma leitura de nível altera essa integral. O tempo de autonomia é a janela em que os operadores ou um sistema de segurança precisam perceber e agir. Se o T-1 contém 12 m³, o mínimo é 2 m³ e o reator puxa cerca de 1,8 m³/h, os operadores têm aproximadamente 5,5 horas. Esse número vai direto para o requisito de detecção: um alarme que dispara depois de seis horas não detecta nada de útil. O cálculo transforma "detectar rápido" em "detectar dentro de 5,5 horas, com margem".

Lena escreve o número no requisito junto com a forma como ele foi calculado.

### 1.3 Consumo variável

O consumo da ABP oscila com a receita do lote: q(t) = 1,8 + 0,4 sen(2πt/6). A sua integral tem forma fechada, e o laboratório resolve t* por bissecção. A resposta, 5,53 h, fica perto da estimativa pela taxa média, de 5,56 h, porque a oscilação se compensa ao longo de um ciclo completo de seis horas; com uma janela mais curta ou uma receita assimétrica, as duas divergiriam, e a escolha conservadora é o tempo menor.

```python
# Lab 1 - tank hold-up after feed pump stop (Ashford Batch Plant, synthetic)
import math
V0, VMIN = 12.0, 2.0   # m3 in feed tank T-1
def outflow(t):         # m3/h to reactor; t hours after stop of makeup
    return 1.8 + 0.4*math.sin(2*math.pi*t/6)
def drawn(t):
    return 1.8*t - (0.4*6/(2*math.pi))*(math.cos(2*math.pi*t/6)-1)
lo,hi=0.0,24.0
for _ in range(50):
    mid=(lo+hi)/2
    lo,hi=(mid,hi) if drawn(mid)<V0-VMIN else (lo,mid)
print(f"time to min level: {lo:.2f} h")
print(f"average-rate estimate: {(V0-VMIN)/1.8:.2f} h")
```

Saída esperada:

```text
time to min level: 5.53 h
average-rate estimate: 5.56 h
```

> **Caso sintético — Ashford Batch Plant.** Lena Okafor, engenheira do Control Network Hardening Programme (CNHP), usou o cálculo da autonomia para argumentar que um alarme de nível baixo no T-1 precisa ser independente do PLC-A, porque um CLP comprometido poderia suprimir tanto o estado da bomba quanto o alarme dentro da janela de 5,5 horas.

### 1.4 Erros e limites

Os modelos pressupõem que o sensor de nível é honesto; o Capítulo 29 trata da falsificação de sensores. Misturar m³/h com minutos é o deslize mais comum. Escolha sempre a raiz conservadora quando a incerteza for grande.

Uma leitura de nível falsificada é o caso que este modelo não consegue tratar: se o transmissor relata um tanque cheio enquanto o T-1 se esvazia, a integral está correta, mas ninguém está olhando para ela. É por isso que Lena combina o cálculo da autonomia com uma chave de nível independente. Confira as unidades em cada passo, escreva o tempo em horas com o consumo pressuposto ao lado e repita o cálculo sempre que a receita mudar a demanda do reator.

### Exercícios

- **EX001 — Consumo constante.** O T-2 contém 9 m³, mínimo de 1,5 m³, consumo constante de 1,25 m³/h. Tempo até o mínimo? Rubrica: 3 = 6,0 h com o desenvolvimento; 2 = método certo, deslize aritmético; 1 = só a fórmula; 0 = nada.
- **EX002 — Requisito.** Transforme a sua resposta do EX001 num requisito de detecção com margem. Rubrica: 3 = limite de tempo com margem declarada e independência do CLP que controla; 2 = só o limite de tempo; 1 = "rápido", vago; 0 = nada.
- **EX003 — Leitura do laboratório.** Por que as respostas da bissecção e da taxa média ficam tão próximas aqui, e quando não ficariam? Rubrica: 3 = um ciclo completo do seno tem média 1,8; uma janela assimétrica ou curta diverge; 2 = uma metade; 1 = vago; 0 = errado.

### Síntese

O tempo de autonomia é ao mesmo tempo uma integral e um orçamento de segurança: ele limita o quão tarde a detecção pode chegar.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) representar uma rede de TO como um grafo direcionado; (2) calcular a alcançabilidade entre os níveis Purdue; (3) provar que remover uma aresta não pode acrescentar um caminho.

### 2.1 Grafos de condutos

No vocabulário da ISA/IEC 62443, zonas são grupos de ativos com requisitos de segurança comuns, e condutos são os caminhos de comunicação permitidos entre elas. Um grafo direcionado modela isso exatamente: os nós são as zonas (L4 escritório, L3.5 DMZ, L3 historiador, L2 SCADA, L1 CLP, L1 SIS, L0 E/S) e uma aresta a→b significa que a pode iniciar tráfego para b. Perguntar "a rede do escritório consegue escrever no sistema de segurança?" vira "o L1-SIS é alcançável a partir do L4?".

Lena monta o grafo da ABP a partir da exportação do firewall, e não do diagrama de rede, porque a exportação é o que é de fato aplicado.

### 2.2 Alcançabilidade

A busca em profundidade calcula o conjunto de nós alcançáveis a partir de um nó inicial em tempo proporcional ao número de nós mais arestas. A alcançabilidade é transitiva: se L4→L3, L3→L2 e L2→L1-SIS, então o L4 alcança o SIS mesmo sem nenhuma regra direta. As revisões de firewall que conferem as regras uma a uma deixam passar exatamente essa composição, e é por isso que os engenheiros calculam o fecho em vez de ler listas de regras.

Lena executa a busca a partir de cada zona, não só do escritório, e guarda o resultado como uma tabela que a próxima revisão pode comparar.

### 2.3 Prova de monotonicidade

Alegação: apagar uma aresta nunca aumenta um conjunto alcançável. Prova: qualquer caminho no grafo menor usa apenas arestas que também existem no grafo maior, então todo nó alcançável depois da remoção já era alcançável antes. Daí decorre a regra prática: remoções de regras podem ser aprovadas rapidamente; acréscimos de regras exigem análise, porque podem criar novos caminhos transitivos.

```python
# Lab 23 - reachability count on a synthetic Purdue-layered OT network
# Nodes: L5-ERP, L4-Office, L3.5-DMZ, L3-Hist, L2-SCADA, L1-PLC, L1-SIS, L0-IO
edges_flat=[("L5","L4"),("L4","L3"),("L3","L2"),("L2","L1-PLC"),("L2","L1-SIS"),("L1-PLC","L0"),("L1-SIS","L0"),("L4","L2")]
edges_zoned=[("L5","L4"),("L4","L3.5"),("L3.5","L3"),("L3","L2"),("L2","L1-PLC"),("L1-SIS","L0"),("L1-PLC","L0")]  # SIS not reachable from SCADA
def reach(edges, start):
    g={}; 
    for a,b in edges: g.setdefault(a,[]).append(b)
    seen=set(); stack=[start]
    while stack:
        n=stack.pop()
        if n in seen: continue
        seen.add(n); stack.extend(g.get(n,[]))
    return seen
for name,e in (("flat",edges_flat),("zoned",edges_zoned)):
    r=reach(e,"L4")
    print(f"{name}: L4 reaches {sorted(r)} count={len(r)} writes_to_SIS={'L1-SIS' in r}")
```

Saída esperada:

```text
flat: L4 reaches ['L0', 'L1-PLC', 'L1-SIS', 'L2', 'L3', 'L4'] count=6 writes_to_SIS=True
zoned: L4 reaches ['L0', 'L1-PLC', 'L2', 'L3', 'L3.5', 'L4'] count=6 writes_to_SIS=False
```

> **Caso sintético — Ashford Batch Plant.** A rede original da ABP tinha uma regra de conveniência L4→L2 para a visualização remota da IHM. O laboratório de alcançabilidade mostra que, no desenho plano, a zona do escritório alcança o L1-SIS; no desenho zoneado, com uma DMZ e sem conduto SCADA→SIS, não alcança.

### 2.4 Erros e limites

Os grafos modelam a iniciação permitida, não o tráfego real nem as vulnerabilidades. Protocolos bidirecionais e ferramentas de acesso remoto podem criar arestas reversas ocultas; inventarie-as explicitamente.

Lena acrescenta uma ferramenta de acesso remoto usada por um fornecedor como uma aresta explícita de fora da planta para o L2, já que as suas sessões são iniciadas para fora, mas carregam comandos para dentro. Sem essa aresta, o grafo mostraria o escritório isolado do SCADA enquanto uma sessão de suporte ainda poderia alcançá-lo. Cada uma dessas arestas é listada com o seu dono e o registro que a justifica, e o grafo é reconstruído depois de qualquer mudança nas ferramentas de acesso remoto ou nos contratos com fornecedores.

### Exercícios

- **EX004 — Fecho.** Arestas: A→B, B→C, C→D, B→E. Liste todos os nós alcançáveis a partir de A. Rubrica: 3 = {A,B,C,D,E}; 2 = falta um; 1 = só os diretos; 0 = nada.
- **EX005 — Uso da prova.** Explique em duas frases por que acrescentar L3→L1-SIS exige mais revisão do que remover L4→L2. Rubrica: 3 = o acréscimo pode criar novos caminhos transitivos, a remoção não (monotonicidade); 2 = só intuição; 1 = vago; 0 = errado.
- **EX006 — Laboratório.** Qual aresta isolada do desenho plano dá ao L4 o seu caminho até o L1-SIS? Rubrica: 3 = L2→L1-SIS (com L4→L2 ou L4→L3→L2 a montante); 2 = nomeia só L4→L2; 1 = vago; 0 = errado.

### Síntese

Zonas e condutos são um grafo; é a alcançabilidade, e não a leitura regra por regra, que responde quem pode tocar o sistema de segurança.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 50

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) calcular a temporização de enlaces seriais para a consulta (polling) de barramentos de campo; (2) relacionar a velocidade do processo físico com os tempos de ciclo de controle exigidos; (3) reconhecer que os sinais físicos podem ser manipulados fora da rede.

### 3.1 Bits num fio

Boa parte da comunicação nas plantas ainda corre sobre RS-485 serial, a taxas como 115.200 bit/s. Com um bit de início, oito bits de dados e um bit de parada, cada byte custa dez tempos de bit. Uma resposta Modbus RTU de 40 bytes leva, portanto, 40 × 10 / 115.200 ≈ 3,5 ms no fio, antes do processamento no dispositivo. Somar todas as consultas de um ciclo diz se o cronograma cabe no orçamento de ciclo do controlador.

```python
"""Lab: does a polling schedule fit the PLC scan/communication budget? (synthetic)"""
link_bps = 115200; bits_per_byte = 10           # RS-485 serial, 8N1 + start bit
polls = [("T-1 level", 8), ("T-2 level", 8), ("R-101 block", 40), ("pump status", 8), ("historian sweep", 120)]
overhead = 12                                    # bytes of request+framing per poll (assumed)
total = sum(n + overhead for _, n in polls)
t = total * bits_per_byte / link_bps
print(f"bytes per cycle={total} time per cycle={t*1000:.1f} ms")
for target in (100, 50):
    print(f"cycle budget {target} ms -> {'fits' if t*1000 <= target else 'OVERRUN'}")
```

Saída esperada:

```text
bytes per cycle=244 time per cycle=21.2 ms
cycle budget 100 ms -> fits
cycle budget 50 ms -> fits
```

Lena faz essa soma para o tronco até o PLC-A antes de aprovar qualquer dispositivo de monitoramento nele, e o resultado é o valor de 21 ms que ela usa depois ao longo de todo o programa.

### 3.2 Constantes de tempo do processo

Uma malha de nível num tanque de 12 m³ varia ao longo de minutos; uma malha de pressão num compressor varia em dezenas de milissegundos. A velocidade de controle e de detecção exigida decorre da física. Um monitoramento de segurança que acrescenta 200 ms de latência é inofensivo no tanque e perigoso no compressor. Pergunte sempre qual é a constante de tempo do processo antes de inserir dispositivos de inspeção em linha.

Na ABP, os tanques de alimentação e o nível do reator são malhas lentas, enquanto um skid de compressor próximo é rápido. Lena lista as malhas de cada tronco com as suas constantes de tempo antes de escolher onde um monitor pode ficar.

### 3.3 Manipulação da camada física

Os sensores medem física: uma malha de 4–20 mA, a tensão de um termopar, um pulso de um medidor de vazão. Um adversário ou uma falha pode alterar esses sinais sem tocar em nenhum pacote de rede — injetando corrente, aquecendo uma sonda ou fazendo um medidor vibrar. O monitoramento de rede não consegue ver isso; as verificações de plausibilidade física (Capítulo 29) e os invólucros com evidência de violação conseguem.

> **Caso sintético — Ashford Batch Plant.** O orçamento de consulta de Lena para o tronco RS-485 até o PLC-A chegou a 21 ms por ciclo, folgadamente dentro do ciclo de 100 ms. Isso deixou espaço para um monitor serial em linha, que ela só aprovou depois de medir a latência acrescentada numa cópia de bancada.

### 3.4 Erros e limites

Os cálculos de temporização ignoram o tempo de resposta dos dispositivos e as retransmissões; meça numa bancada antes de se comprometer. Não teste injeção de sinal em malhas ativas.

A cópia de bancada de Lena do tronco RS-485 até o PLC-A é onde o orçamento de consulta e a latência acrescentada pelo monitor serial foram medidos, e é o único lugar em que o trabalho do curso toca a temporização serial. Qualquer experimento de injeção de sinal, mesmo um pequeno viés numa malha de 4–20 mA, pertence a uma bancada com um transmissor sobressalente, nunca à malha ativa do T-1. Registre os resultados de bancada com o equipamento usado, porque um transmissor ou um cabo diferente pode mudar os números.

### 3.5 Exemplo resolvido — níveis de sinal e o orçamento de tempo (ABP sintética)

O transmissor de nível do T-1 envia um sinal de 4–20 mA por 180 m de par trançado até o PLC-A. Um viés de 0,2 mA injetado num armário de distribuição desloca a leitura em 0,2/16 = 1,25 % da faixa, o que, para a faixa calibrada de 9 m³ do transmissor, é cerca de 0,11 m³ — pequeno o bastante para se esconder no ruído normal. A constante de tempo do tanque (faixa sobre a vazão típica de entrada, 9/1,25 ≈ 7,2 h) diz a Lena por quanto tempo esse viés pode agir antes que o cálculo de autonomia do Capítulo 1 esteja errado por uma margem de segurança inteira. Ela especifica, portanto, uma segunda chave de nível independente no T-1, ligada ao SIS-B, e uma comparação periódica entre o transmissor e a chave, porque um ataque na camada física a uma malha não consegue então derrotar as duas em silêncio.

### Exercícios

- **EX007 — Tempo no fio.** Quanto tempo leva um quadro de 120 bytes a 19.200 bit/s, com 10 bits por byte? Rubrica: 3 = 62,5 ms com o desenvolvimento; 2 = deslize; 1 = método; 0 = nada.
- **EX008 — Orçamento.** Usando os 244 bytes por ciclo do laboratório, qual é a taxa mais lenta que ainda cabe num orçamento de 50 ms? Rubrica: 3 = 48.800 bit/s (portanto, 57.600 padrão) com o desenvolvimento; 2 = número sem a taxa padrão; 1 = método; 0 = nada.
- **EX009 — Física.** Dê duas manipulações da camada física que um IDS de rede não consegue detectar e um controle compensatório para cada uma. Rubrica: 3 = duas manipulações mais os controles; 2 = duas sem controles; 1 = uma; 0 = nada.

### Síntese

A física define o orçamento de tempo do controle e de qualquer dispositivo de segurança que você ponha na malha.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 50

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever funções pequenas e puras que decidem se uma mensagem de TO é permitida; (2) representar endereços industriais com tipos exatos; (3) testar com tráfego decodificado sintético, nunca com tráfego real da planta.

### 4.1 Decisões como funções

Uma lista de permissões (allow-list) para Modbus é uma função `permit(source, function_code, register) -> (bool, reason)`. Torná-la pura — entradas entram, decisão sai, sem configuração oculta — permite testá-la num laptop com registros sintéticos. A string de motivo importa: "register-out-of-range" diz a um revisor que a IHM tentou escrever fora do bloco de setpoints, o que é uma história diferente de uma estação desconhecida usando uma função de diagnóstico.

Lena mantém as strings de motivo curtas e fixas, para que os logs possam ser contados por motivo.

### 4.2 Tipos exatos

Armazene os códigos de função como inteiros, as faixas de registradores como objetos `range` e as identidades das estações como strings fixas vindas de um inventário. Um bug frequente trata a notação 4xxxx de "holding register" como string e casa por prefixo, de modo que 400500 parece 40050. Converta os endereços uma única vez, no momento da análise, em inteiros com deslocamentos documentados.

Lena escreve uma única função de conversão para os endereços de registradores e a testa nas duas pontas da faixa gravável da IHM, 40001 e 40010, e um passo fora de cada uma. Os nomes das estações vêm do inventário, então um erro de digitação na lista de permissões falha numa consulta, em vez de criar em silêncio uma nova estação que não casa com nada.

### 4.3 Testes em quadros decodificados sintéticos

O laboratório abaixo nunca abre um socket; ele verifica tuplas já decodificadas. Isso é deliberado. O código do curso não pode enviar tráfego Modbus a nenhum dispositivo. Escreva um teste por regra, mais os registradores de fronteira 40001 e 40010.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Saída esperada:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

Os testes são agrupados por regra, para que uma falha aponte direto para a cláusula que quebrou. O teste de escrita do historiador, que pegou a função 16, é mantido como caso permanente. A tabela de testes de Lena lista cada tupla, a decisão esperada e a string de motivo, e um revisor pode lê-la sem executar nada. Novas estações ou registradores acrescentados à lista de permissões chegam com as suas próprias linhas no mesmo pull request.

### 4.3b Registrando o que a função decidiu

Toda decisão deve ser registrada com a origem, o código de função, o registrador, a decisão, o motivo e a versão do arquivo da lista de permissões. Quando um operador pergunta por que uma escrita da IHM foi bloqueada às 03:12, o log responde numa linha. Sem o campo de versão, ninguém consegue dizer se o bloqueio veio da lista de ontem ou da de hoje.

> **Caso sintético — Ashford Batch Plant.** A primeira lista de permissões de Lena deixava o HIST-1 usar a função 16 (escrever múltiplos registradores) porque ele "só lê". A tabela de testes pegou isso: o historiador não tem nada que escrever, então a função 16 foi removida e o teste agora espera BLOCK.

### 4.4 Erros e limites

Uma lista de permissões num monitor só é tão boa quanto o decodificador. Quadros malformados precisam ser contados e alarmados, não descartados em silêncio. Os dispositivos reais de aplicação precisam de validação do fornecedor antes da implantação.

O monitor de Lena conta os quadros malformados por minuto e gera um alarme se a contagem subir, porque uma rajada repentina pode significar um dispositivo falhando ou um bug no decodificador. Tratar esses quadros como permitidos transformaria cada lacuna do decodificador numa porta aberta. O monitor deste curso apenas observa; qualquer dispositivo que de fato bloqueie tráfego na ABP é um produto de fornecedor validado antes na bancada.

### Exercícios

- **EX010 — Regra.** Escreva a regra de permissão (em palavras ou em código) para "o HIST-1 pode ler registradores de entrada e de retenção, nada mais". Rubrica: 3 = só fc 3 e 4, todo o resto BLOCK com motivo; 2 = falta um motivo; 1 = vago; 0 = inclui escritas.
- **EX011 — Fronteira.** Quais valores de registrador testam as bordas da faixa de escrita da IHM no laboratório, e o que se espera para 40011? Rubrica: 3 = 40001 e 40010 PASS, 40011 BLOCK; 2 = uma borda; 1 = vago; 0 = errado.
- **EX012 — Laboratório.** Por que ENG-WS fc=8 é bloqueado, e por que esse é o padrão correto? Rubrica: 3 = não há entrada (ENG-WS, 8); diagnóstico/negar por padrão; 2 = primeira metade; 1 = vago; 0 = errado.

### Síntese

Funções de permissão puras, tipadas e testadas são a menor unidade confiável de software de segurança de TO.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 50

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever constatações de segurança de TO sobre as quais operadores e engenheiros de segurança de processo possam agir; (2) separar observação, consequência e recomendação; (3) evitar linguagem alarmista ou sem limites.

### 5.1 Três públicos

Um operador da sala de controle precisa saber o que observar. Um engenheiro de segurança de processo precisa saber se uma função de segurança é afetada. Um gerente precisa de custo e de tempo de parada. Uma constatação pode servir aos três se declarar: o ativo e a zona; o que foi observado e como; a consequência plausível para o processo; o estado da camada de segurança; a correção e a janela de manutenção necessária.

Lena escreve cada constatação uma vez, nessa ordem, para que cada leitor encontre rapidamente a sua parte. Uma constatação à qual falte qualquer uma dessas partes volta ao autor antes da revisão.

### 5.2 Consequências delimitadas

"Um atacante poderia explodir a planta" não é verdadeiro nem útil. Uma declaração delimitada diz: "Uma estação no L2 consegue escrever registradores de setpoint no PLC-A sem autenticação. Uma mudança do setpoint de nível do T-1 poderia fazer o tanque transbordar em cerca de 40 minutos; o trip independente de nível muito alto no SIS-B pararia a bomba de alimentação antes do transbordamento." Isso nomeia o caminho, o tempo e a camada de proteção que continua de pé.

Lena confere cada declaração delimitada com o engenheiro de segurança de processo antes do envio, já que os minutos até o transbordamento e o trip que segura vêm da análise de segurança, não da equipe de segurança cibernética.

### 5.3 Estrutura de um relatório curto

Resumo (três frases); escopo e método; constatações ordenadas por consequência; risco residual, com as camadas de proteção nomeadas; apêndice com referências às evidências. Diagramas de zonas valem mais do que páginas de tabelas de regras.

Os relatórios de Lena para o CNHP cabem em duas páginas mais o apêndice. O resumo nomeia a constatação mais grave e diz se alguma função de segurança é afetada. Cada constatação cita a sua evidência pelo hash e declara a janela de manutenção necessária para a correção, para que os planejadores possam agendá-la. Um diagrama de zonas com o conduto afetado destacado costuma explicar a constatação mais rápido do que o texto.

### 5.3b Palavras a evitar e palavras a usar

Evite "trivial", "catastrófico" e "totalmente comprometido": nenhuma dessas pode ser verificada. Use grandezas medidas — minutos até o transbordamento, número de zonas alcançáveis, camadas de proteção intactas — e nomeie a evidência. Um engenheiro de segurança confia muito mais numa constatação que diz "o SIS-B continua independente" do que numa que diz "tudo está em risco".

> **Caso sintético — Ashford Batch Plant.** O primeiro rascunho de Lena de uma constatação dizia que a rede SCADA era "totalmente insegura". A versão revisada: "A regra de visualização remota L4→L2 permite que hosts do escritório alcancem os servidores SCADA (regra FW-12, observada na exportação de configuração de 3 de março). Recomenda-se a remoção; a visualização passa a ser feita pela réplica do historiador na DMZ. Tempo de parada: nenhum."

### 5.4 Erros e limites

Nunca inclua procedimentos de ataque funcionais nos relatórios; faça referência ao repositório de evidências. Não alegue uma consequência de segurança sem a revisão do engenheiro de segurança.

Evidências como as exportações de configuração ficam no repositório lacrado, e o relatório as cita pelo hash, de modo que qualquer pessoa com acesso possa verificá-las sem que o relatório carregue detalhes sensíveis. Lena envia toda constatação que mencione o SIS-B ou um trip ao engenheiro de segurança de processo para revisão antes da liberação e registra no relatório o nome do revisor. Uma consequência que o engenheiro não confirmou é escrita como pergunta, não como alegação.

### Exercícios

- **EX013 — Reescrita.** Reescreva "o CLP pode ser hackeado" como uma frase de constatação delimitada para o PLC-A. Rubrica: 3 = caminho, zona, observação, limite da consequência, camada de proteção; 2 = falta um; 1 = ainda vago; 0 = inalterado.
- **EX014 — Público.** Para a constatação FW-12, escreva uma frase para cada um: operador, engenheiro de segurança e gerente. Rubrica: 3 = três frases sob medida; 2 = duas; 1 = uma; 0 = nada.
- **EX015 — Risco residual.** Depois da remoção da FW-12, declare um risco residual com honestidade. Rubrica: 3 = caminho remanescente específico (por exemplo, estação de engenharia, acesso remoto de fornecedor) e o seu controle; 2 = genérico; 1 = "nenhum"; 0 = nada.

### Síntese

Boas constatações de TO são delimitadas, nomeiam as camadas de proteção e dão a cada público o que ele precisa para decidir.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 50

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar séries para raciocinar sobre retransmissões repetidas nas comunicações da planta; (2) aplicar um modelo diferencial simples ao acúmulo de alarmes; (3) decidir quando um modelo contínuo é bom o bastante para uma discussão de manutenção.

### 6.1 Retransmissões geométricas num barramento de campo

Se cada requisição Modbus tem sucesso com probabilidade p = 0,9, de forma independente (sintético, para um tronco ruidoso), a chance de ter sucesso em até k tentativas é 1 − (1 − p)^k. Com k = 3, isso dá 0,999. As retransmissões aumentam a confiabilidade, mas multiplicam o tráfego: o número esperado de tentativas até o sucesso é 1/p ≈ 1,11, então um ciclo de 1.000 consultas espera cerca de 1.110 quadros. O orçamento de comunicações (Capítulo 3) precisa contar as retransmissões, não só as consultas lógicas.

Lena inclui as retransmissões quando confere o tronco RS-485 até o PLC-A, já que um período ruidoso pode aumentar o tráfego em um décimo ou mais.

### 6.2 O acúmulo de alarmes como equação de taxas

Seja B(t) o número de alarmes abertos. Os alarmes chegam à taxa a e são reconhecidos à taxa c quando há equipe. Então B′ ≈ a − c. Se a = 3,3/h (a taxa anterior à racionalização, do laboratório de alarmes) e dois operadores juntos eliminam 2,0/h, o acúmulo cresce. Depois da racionalização para 1,05/h, a mesma equipe dá conta. O modelo é grosseiro — ignora a prioridade —, mas torna quantitativas a dotação de pessoal e a racionalização.

```python
"""Lab: alarm load per operator hour before and after rationalisation (synthetic counts)."""
before = {"T-1 high": 140, "T-2 high": 95, "R-101 temp": 30, "pump trip": 6, "comm loss PLC-A": 210, "door open": 75}
remove = {"comm loss PLC-A": 200, "door open": 70, "T-1 high": 110}   # chattering/duplicate alarms removed
hours = 24 * 7
tb = sum(before.values()); ta = tb - sum(remove.values())
print(f"week alarms before={tb} after={ta}")
print(f"per operator-hour before={tb/hours:.2f} after={ta/hours:.2f}")
top = max(before, key=before.get)
print(f"worst source before: {top} ({before[top]/tb:.0%} of load)")
```

Saída esperada:

```text
week alarms before=556 after=176
per operator-hour before=3.31 after=1.05
worst source before: comm loss PLC-A (38% of load)
```

Lena usa o modelo para defender a racionalização antes de pedir pessoal. Os números deixaram o argumento claro.

### 6.3 Quando o contínuo basta

As discussões de manutenção muitas vezes precisam de uma ordem de grandeza: "200 alarmes oscilantes de perda de comunicação por semana vão sobrecarregar um operador?" Sim: só isso já dá cerca de 1,2/h. Reserve a análise exata para as malhas que afetam a temporização de segurança.

> **Caso sintético — Ashford Batch Plant.** O laboratório de alarmes reduziu a carga semanal de 556 para 176, removendo fontes oscilantes conhecidas. Lena usou B′ para mostrar que um operador noturno daria conta depois da mudança, o que destravou a proposta do CNHP, parada em "primeiro precisamos de mais pessoal".

### 6.4 Erros e limites

A independência das retransmissões falha quando o tronco está sistematicamente fora do ar. Os modelos de acúmulo ignoram os alarmes críticos para a segurança, que precisam interromper; trate-os à parte.

Quando o tronco até o PLC-A está fora do ar, todas as retransmissões falham juntas, então a fórmula geométrica superestima muito a confiabilidade; Lena trata uma queda do tronco como um caso separado, com o seu próprio alarme. Da mesma forma, um nível muito alto no T-1 ou um trip do SIS-B precisa chegar ao operador imediatamente, seja qual for o acúmulo de alarmes de rotina. O modelo de taxas serve para planejar a dotação de pessoal e a racionalização, não para decidir quais alarmes podem esperar.

### Nota prática

Mantenha um gráfico semanal de a e de c ao lado do registro de racionalização de alarmes. Quando a sobe depois de uma mudança de firmware, você sabe que deve procurar uma nova fonte oscilante antes de culpar os operadores.

### Exercícios

- **EX016 — Retransmissões.** Com p = 0,85 e 500 consultas, quantos quadros se esperam? Rubrica: 3 ≈ 588 com o desenvolvimento; 2 = deslize; 1 = fórmula; 0 = nada.
- **EX017 — Acúmulo.** B(0)=40, a=1,0/h, c=1,5/h. Horas até zerar? Rubrica: 3 = 80 h; 2 = método; 1 = qualitativo; 0 = nada.
- **EX018 — Laboratório.** Que fração da carga anterior à mudança era "comm loss PLC-A"? Rubrica: 3 = 38%; 2 = só a contagem; 1 = vago; 0 = errado.

### Síntese

Séries e taxas transformam "tente de novo" e "contrate alguém" em números que cabem numa decisão de comunicações ou de pessoal.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 50

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) relatar taxas de detecção com intervalos; (2) comparar detectores sem alegar demais; (3) recusar classificações que a amostra não sustenta.

### 7.1 Taxas e intervalos

Sessenta ensaios sintéticos com 0 alarmes falsos e 60/60 detecções parecem perfeitos — até você lembrar que um intervalo de Wilson de 95% para 0/60 ainda admite, no longo prazo, uma taxa de alarmes falsos de alguns por cento. Relate o intervalo, não só o ponto. Para 60/60 detecções, o intervalo da taxa de perdas também é estreito, mas não é zero para sempre.

Os relatórios de Lena para o CNHP dão a contagem, o intervalo e a lista de sementes juntos, para que o leitor veja tanto o resultado quanto o quanto ele poderia mudar com mais ensaios.

### 7.2 Comparando detectores

O laboratório do CUSUM de resíduo mostra um detector de faixa deixando passar os ataques da classe A enquanto o CUSUM os capta com atraso médio de ~25 amostras, ambos com 0/60 alarmes falsos neste conjunto de sementes. Isso é evidência de que o CUSUM supera a faixa *nesses ataques sintéticos*, não de que o CUSUM é universalmente melhor. Prefira desenhos pareados sobre os mesmos traços e declare a classe de ataque.

```python
# Lab 27 - residual CUSUM vs band on batch reactor level (synthetic)
import random
def run(seed, atk, det, k=0.8, h=6.0):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(500):
        inflow=1.0+rng.gauss(0,0.05)+(0.08 if atk and t>=250 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=250: lvl=50+rng.gauss(0,0.3)
        if atk=="B" and t>=250: fm=1.0+rng.gauss(0,0.02)
        est+=fm-0.02*est
        hit=abs(lvl-50)>2.0 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-k); hit=s>h
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,None,det) is not None for i in range(60))
    for atk in ("A","B"):
        hits=[a-250 for a in (run(i,atk,det) for i in range(60)) if a is not None and a>=250]
        print(f"{det} class{atk} FA={fa}/60 det={len(hits)}/60 mean_delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Saída esperada:

```text
band classA FA=0/60 det=0/60 mean_delay=nan
band classB FA=0/60 det=0/60 mean_delay=nan
cusum classA FA=0/60 det=60/60 mean_delay=24.8
cusum classB FA=0/60 det=0/60 mean_delay=nan
```

O plano piloto de Lena mantém os mesmos traços para os dois detectores e nomeia a classe de ataque testada, para que a comparação possa ser repetida depois com novas sementes.

### 7.3 Taxas de base na sala de controle

Se os ataques ciberfísicos genuínos são raros, um detector com uma taxa de alarmes falsos de apenas 1% vai dominar a atenção do operador. A regra de Bayes se aplica exatamente como no Capítulo 7 dos cursos de segurança vizinhos: a precisão desaba quando a taxa de base é minúscula. Projete para a taxa de base da planta, não para o conjunto balanceado de um laboratório.

> **Caso sintético — Ashford Batch Plant.** Um fornecedor alegou "99% de detecção, 0% de alarmes falsos" a partir de uma demonstração de 20 execuções. Lena pediu a classe de ataque, a lista de sementes e o intervalo de alarmes falsos; nada disso foi fornecido. O piloto usou, em vez disso, o desenho do laboratório do CUSUM.

### 7.4 Erros e limites

Ataques sintéticos não são o adversário. Os intervalos pressupõem ensaios independentes; sementes correlacionadas os invalidam. Nunca invente um valor-p para uma tabela que você não testou.

Os relatórios do piloto de Lena declaram que os ataques eram sintéticos, listam as sementes e explicam como elas foram geradas. Se duas sementes produzem traços quase idênticos, ela as conta como um único ensaio, porque tratá-las como independentes faria o intervalo parecer mais estreito do que as evidências sustentam. Todo teste estatístico que ela relata é um teste que ela de fato executou, com as entradas guardadas para que um revisor possa executá-lo de novo.

### Nota prática

Publique a lista de sementes e os parâmetros do detector com toda alegação de detecção nos documentos do CNHP. A reprodutibilidade custa menos do que discutir um slide seis meses depois, e é o que Urbina et al. e Giraldo et al. exigem das avaliações.

### Exercícios

- **EX019 — Intervalo.** Declare o que 0/60 alarmes falsos permite alegar a ~95%. Rubrica: 3 = limite superior de ~5–6% (regra de três / Wilson), não "zero para sempre"; 2 = só o limite; 1 = "zero"; 0 = nada.
- **EX020 — Laboratório.** Para o CUSUM na classe A, relate as detecções e o atraso médio. Rubrica: 3 = 60/60 e ~24,8; 2 = um número; 1 = vago; 0 = errado.
- **EX021 — Recusa de classificação.** A faixa e o CUSUM mostram ambos FA=0/60 na classe B (nenhuma detecção). Escreva a frase que se recusa a chamá-los de iguais em qualidade. Rubrica: 3 = cita a falta de poder / a necessidade da classe A ou de um n maior; 2 = cautela vaga; 1 = declara iguais; 0 = nada.

### Síntese

As alegações de detecção precisam de intervalos, da classe de ataque e de honestidade quanto à taxa de base — não de uma única porcentagem.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 50

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) situar o CLP, o SIS e o SCADA num mapa de privilégios e de dependências; (2) explicar por que os sistemas de segurança precisam de hardware independente; (3) projetar uma coleta de evidências que não exija escrever no CLP.

### 8.1 Privilégio na planta

Um CLP executa a malha regulatória básica. Um SIS implementa as funções instrumentadas de segurança e precisa ser capaz de agir quando o CLP está errado ou comprometido. O SCADA e as IHMs são de supervisão: definem setpoints e exibem o estado. Uma arquitetura que deixa o SCADA escrever na lógica do SIS desfaz essa independência — exatamente o que o laboratório de alcançabilidade advertiu.

Na ABP, o PLC-A executa as malhas regulatórias do T-1, do T-2 e do R-101, e o SIS-B guarda os trips. Lena marca esses papéis no seu mapa de privilégios.

### 8.2 A independência é física

Independência não é uma tag de VLAN. Significa controladores separados, sensores separados onde a especificação de requisitos de segurança exigir e condutos que não permitam à rede regulatória alterar a lógica de segurança. A NIST SP 800-82 e a ISA/IEC 62443 tratam os sistemas de segurança como algo que exige um zoneamento cuidadoso; as normas de segurança de processo (IEC 61511) vão além quanto à independência. A arquitetura de segurança cibernética não pode desfazer aquilo que a arquitetura de segurança física pagou.

Lena verifica a independência rastreando fios e condutos, não lendo rótulos no desenho da rede. Os sensores de nível próprios do SIS-B no T-1 são o exemplo mais claro dessa independência.

### 8.3 Evidências sem escrever no CLP

A avaliação autorizada de TO prefere métodos somente leitura: exportações de configuração, dados espelhados do historiador, portas espelhadas, monitores seriais em modo de escuta. Escrever um setpoint de teste num CLP ativo é uma mudança de processo e precisa da mesma autorização que uma mudança de engenharia. Os laboratórios do curso nunca escrevem em dispositivos reais.

> **Caso sintético — Ashford Batch Plant.** O SIS-B é um controlador separado, com os seus próprios sensores para o nível muito alto no T-1. O conjunto de regras do CNHP proíbe qualquer conduto do L2/L3 para as portas de engenharia do SIS, exceto por meio de uma chave física trancada durante os testes programados.

### 8.4 Erros e limites

As alegações de "air gap" muitas vezes escondem USB, laptops de fornecedores e modems celulares. Inventarie esses caminhos fora de banda com o mesmo cuidado que as rotas IP.

O inventário de Lena para a ABP lista cada porta USB das IHMs e das estações de engenharia, cada laptop de fornecedor que se conecta para suporte e cada modem celular instalado para diagnóstico remoto. Cada um recebe um dono e um controle, como o bloqueio de portas ou uma retirada registrada. Uma planta descrita como isolada é conferida com essa lista antes que alguém repita a alegação num relatório, porque um único modem esquecido pode criar um caminho que o grafo de zonas nunca mostra.

### Nota prática

Desenhe o mapa de privilégios numa página: quem pode mudar setpoints, quem pode mudar a lógica, quem pode mudar os setpoints de segurança e por quais portas físicas. Pendure-o na sala de engenharia. As discussões sobre "só uma regra temporária" morrem mais rápido quando o mapa está à vista.

### Exercícios

- **EX022 — Mapa.** Nomeie três ações que exigem privilégio de engenharia do SIS e três que uma IHM normal pode fazer. Rubrica: 3 = seis corretamente divididas; 2 = quatro; 1 = vago; 0 = nada.
- **EX023 — Independência.** Por que a separação por VLAN sozinha é insuficiente para a independência do SIS? Rubrica: 3 = controlador/sensores/caminho de gestão compartilhados ainda podem acoplar; 2 = uma razão; 1 = vago; 0 = alega que a VLAN basta.
- **EX024 — Evidência.** Proponha um caminho de evidência somente leitura para "a IHM consegue escrever o registrador 40050". Rubrica: 3 = exportação de configuração ou porta espelhada monitorada mostrando a capacidade/tentativa de escrita, sem escrita ao vivo; 2 = parcial; 1 = escrita ao vivo; 0 = nada.

### Síntese

Mantenha a lógica de segurança independente no hardware e nos condutos; colete evidências sem se tornar um atuador.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 50

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) projetar um esquema para constatações de TO que proíba receitas de exploração; (2) implementar atualizações idempotentes indexadas por ativo e fraqueza; (3) testar por propriedades as regras de zonas.

### 9.1 Esquema sem payloads

Armazene título, ativo, zona, classe de fraqueza, hash da evidência, limite da consequência, camadas de proteção intactas e situação. Rejeite campos chamados payload, shell ou exploit. A evidência fica num repositório lacrado; o ticket guarda o hash.

O esquema de Lena rejeita o registro inteiro se um campo proibido aparecer, em vez de removê-lo em silêncio, para que quem o enviou aprenda a não fazê-lo. Os limites de consequência e as camadas de proteção intactas são campos separados, o que permite ao engenheiro de segurança filtrar as constatações que tocam o SIS-B. O hash da evidência liga cada ticket à sua prova lacrada sem copiar nada dela para o sistema de tickets.

### 9.2 Upserts idempotentes

Dois scanners que relatam a mesma escrita Modbus aberta no PLC-A precisam virar uma única constatação. Impressão digital = (ativo, classe de fraqueza, registrador ou caminho). Retransmissões e reimportações deixam uma única linha.

Lena testa isso importando duas vezes a mesma saída de scanner e importando os relatos de dois scanners sobre o mesmo problema; os dois casos precisam deixar exatamente uma constatação. A impressão digital usa o registrador ou o caminho, não a redação do próprio scanner, porque duas ferramentas descrevem a mesma fraqueza de maneiras diferentes. Quando as impressões digitais colidem para problemas de fato diferentes, uma pessoa as separa e registra por quê.

### 9.3 Testes de propriedades para zonas

Declare: "para todo host da zona do escritório e todo registrador do SIS, permit é falso". Gere hosts sintéticos e verifique com asserções. Os testes de propriedades pegam o bug em que uma nova sub-rede de escritório foi acrescentada ao inventário, mas não ao lado de negação da lista de permissões.

> **Caso sintético — Ashford Batch Plant.** Depois da constatação FW-12, Lena acrescentou um teste de propriedade: nenhum host do L4 pode ter um caminho de permissão até o L1-SIS. A integração contínua o executa a cada mudança na exportação do firewall.

O teste roda sobre hosts sintéticos tirados do inventário.

### 9.4 Erros e limites

Os esquemas derivam; versione-os. Geradores de propriedades que nunca emitem a nova sub-rede deixam passar o bug que deveriam pegar — inclua as diferenças do inventário como entradas.

Lena alimenta o teste de propriedade com a diferença mais recente do inventário, para que toda nova sub-rede seja testada na execução seguinte. O esquema tem um campo de versão, e os registros mais antigos são migrados com um script registrado, e não editados à mão. Quando um teste é alterado, ela confere se ele ainda falha no bug original, já que uma propriedade que não pode mais falhar não protege nada.

### Nota prática

Quando alguém pedir um host de exceção "só desta vez", exija no esquema um objeto de exceção com prazo, com uma data de expiração e um dono. Exceções sem expiração viram condutos permanentes.

### 9.1b Evolução do esquema sem parada

Quando o esquema de constatações ganha um campo obrigatório, implante uma mudança em duas fases: primeiro aceite e persista o campo como opcional enquanto preenche os registros antigos; depois mude o validador para obrigatório. As janelas em andamento não podem quebrar porque um cliente móvel está uma versão atrás. Publique a versão do esquema nas respostas da API, para que os clientes possam se recusar a escrever quando forem incompatíveis. As importações em massa vindas de scanners precisam passar pelo mesmo caminho de validação que as criações interativas, incluindo a verificação de campos proibidos, ou os payloads vão entrar pela porta lateral confiável da importação.

### Exercícios

- **EX025 — Rejeição.** Escreva uma regra de validação que rejeite campos com cara de payload. Rubrica: 3 = regra + exemplo que falha; 2 = regra; 1 = ideia; 0 = nada.
- **EX026 — Impressão digital.** Por que dois relatos do registrador 40050 do PLC-A se fundem? Rubrica: 3 = mesma impressão digital; 2 = "mesma constatação"; 1 = vago; 0 = errado.
- **EX027 — Propriedade.** Declare uma propriedade depois de acrescentar uma zona DMZ. Rubrica: 3 = por exemplo, o L4 só alcança o L2 via L3.5; 2 = informal; 1 = errado; 0 = nada.

### Síntese

Esquemas, idempotência e propriedades mantêm o ferramental de segurança de TO entediante — no bom sentido.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 50

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) recusar o acesso não autorizado a plantas e os pedidos de duplo uso; (2) aplicar condições de parada que protejam a segurança do processo; (3) documentar o consentimento de modo que uma revisão possa reconstruí-lo.

### 10.1 Autorização não é entusiasmo

Um gerente de planta dizendo "pode ir em frente" num corredor não é uma autorização escrita. O trabalho em TO precisa de um escopo assinado que nomeie as unidades, os métodos, as janelas, as condições de parada e um contato de segurança de processo capaz de parar a planta. Sem esse documento, o engenheiro para. A NIST SP 800-82 e a ISA/IEC 62443 pressupõem atividades autorizadas e planejadas — não improvisação engenhosa.

Lena mantém uma cópia do escopo assinado com cada pacote de trabalho e a confere antes de cada sessão. Se o escopo não cobre um passo planejado, ela para e pede um aditamento, em vez de interpretá-lo com generosidade. O telefone do contato de segurança de processo está na própria permissão de trabalho.

### 10.2 Duplo uso

Este programa ensina zoneamento, monitoramento, medição e relato. Ele não ensina o desenvolvimento de exploits contra CLPs, pilhas de protocolo transformadas em armas nem contornos de sistemas de segurança. Quando um colega pede "só a PoC contra a marca X", a resposta é a descrição da constatação e o canal de divulgação do fornecedor, não um ataque funcional.

As recusas de Lena são educadas e específicas e apontam o que ela pode oferecer no lugar: uma constatação com consequências delimitadas, uma referência ao processo de divulgação do fornecedor e uma mudança de projeto que elimina a exposição. O registro de cada pedido e de cada recusa é guardado com as anotações do projeto.

### 10.3 Condições de parada que protegem o processo

Pare se: disparar um alarme de processo inesperado; a latência ou o tempo de ciclo exceder o orçamento; um sistema de segurança indicar uma falha; o contato de segurança de processo disser para parar. Bloqueios rígidos no software ajudam, mas as pessoas sempre prevalecem. Nunca desabilite uma função de segurança para "fazer o teste funcionar".

> **Caso sintético — Ashford Batch Plant.** Durante um teste de bancada do monitor serial, o tempo de ciclo subiu acima de 50 ms. Lena parou, removeu o dispositivo e testou de novo num tronco sobressalente antes de reservar qualquer janela na planta.

Essas condições são impressas na permissão de trabalho.

### 10.4 Erros e limites

A ética é uma restrição sobre todos os capítulos seguintes. O texto jurídico aqui é orientação, não aconselhamento. Plantas em operação nunca são alvos dos laboratórios do curso.

Todos os capítulos seguintes pressupõem esse limite. O trabalho de Lena na ABP acontece sob um escopo assinado, com condições de parada nomeadas e um contato de segurança de processo; nada no curso é jamais dirigido a uma planta em funcionamento. Quando uma questão toca a lei, como a proteção de dados ou os contratos com fornecedores, ela consulta o assessor jurídico do local, em vez de se apoiar nas anotações do curso, e registra a orientação recebida.

### Nota prática

Imprima as condições de parada na permissão de trabalho pendurada no painel. Sob ruído e pressão de tempo, as pessoas lembram do que conseguem ver. Uma condição de parada enterrada na página 12 de um PDF é uma condição de parada que será esquecida.

### 10.5 Exemplo resolvido — uma permissão que diz não (ABP sintética)

Um prestador pede para executar uma varredura Modbus ativa no PLC-A durante um lote, "para terminar o inventário mais rápido". A revisão da permissão por Lena aplica três testes: a autorização escrita do dono é específica para esse host e essa técnica (não é); existe uma condição de parada que um operador possa acionar (nenhuma foi escrita); e existe uma alternativa passiva (uma captura por porta espelhada mais a exportação do projeto de engenharia dá o mesmo inventário). Ela recusa a varredura ativa, registra o motivo e emite uma permissão apenas para a captura passiva, com o líder do turno nomeado como a pessoa que pode parar o trabalho. A NIST SP 800-82r3 adverte que a varredura ativa pode perturbar os dispositivos de TO, que é a razão de engenharia por trás da razão ética.

### Exercícios

- **EX028 — Recusa.** Recusa em duas frases a um pedido de um exploit funcional de CLP para um trabalho avaliado. Rubrica: 3 = recusa, oferece uma alternativa permitida, cita a segurança; 2 = só recusa; 1 = vago; 0 = fornece o exploit.
- **EX029 — Parada.** Liste quatro condições de parada para uma janela na ABP. Rubrica: 3 = quatro relevantes para o processo; 2 = três; 1 = uma; 0 = nada.
- **EX030 — Campos.** Seis campos que uma permissão de trabalho de TO assinada precisa conter. Rubrica: 3 = unidades, métodos, janela, limites de taxa/impacto, contatos, parada/retomada; 2 = quatro; 1 = dois; 0 = nada.

### Síntese

Permissão escrita, condições de parada que põem o processo em primeiro lugar e o hábito da recusa são engenharia de segurança.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 50

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (inglês) →](../../en/book/MANUSCRIPT.md#ch-11)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX150. A Ashford Batch Plant, Lena Okafor, o CNHP e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação. Esta edição parcial traz as resoluções de EX001–EX030; as de EX031–EX150 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

**EX001.** (9 − 1,5) / 1,25 = 7,5 / 1,25 = 6,0 horas.

**EX002.** "Uma condição de nível baixo no T-2 deve ser alarmada ao operador em até 4 horas após a perda da reposição (6,0 h de autonomia menos 2 h de margem de resposta), por um caminho de alarme independente do CLP que controla a bomba de reposição."

**EX003.** O termo do seno integra quase a zero ao longo de um período completo de 6 horas, então o consumo médio é 1,8 m³/h e 10/1,8 ≈ 5,56 h. Se a janela cobrisse apenas a parte alta do ciclo, ou se a receita pendesse para um consumo alto, o tempo real seria menor do que a estimativa pela taxa média.

**EX004.** A partir de A: B (direto), C e E (via B), D (via C). Conjunto alcançável {A, B, C, D, E}.

**EX005.** Remover uma aresta só pode encolher os conjuntos alcançáveis, então não pode expor nada de novo. Acrescentar L3→L1-SIS pode criar um caminho de todas as zonas que já alcançam o L3 — incluindo o L4 e o L5 — até o sistema de segurança, então exige uma verificação completa de alcançabilidade.

**EX006.** A aresta L2→L1-SIS. O L4 já alcança o L2 (diretamente via L4→L2 e via L3), então esse único conduto SCADA→SIS completa o caminho; o desenho zoneado o omite.

**EX007.** 120 × 10 = 1.200 bits; 1.200 / 19.200 = 0,0625 s = 62,5 ms.

**EX008.** Taxa necessária = 244 × 10 bits / 0,050 s = 48.800 bit/s. A próxima taxa padrão igual ou acima disso é 57.600 bit/s; 38.400 estouraria o orçamento.

**EX009.** (1) Injeção de corrente numa malha de 4–20 mA → sensor redundante com verificação cruzada. (2) Aquecer ou resfriar uma sonda de temperatura → verificação de plausibilidade por modelo físico em relação ao ciclo de trabalho do aquecedor. Invólucros e lacres com evidência de violação também são controles aceitáveis.

**EX010.** permit(src, fc, reg): se src == "HIST-1" e fc em {3, 4} → PASS; se src == "HIST-1" em qualquer outro caso → BLOCK "fc-not-allowed". Nenhum código de escrita (5, 6, 15, 16) é listado.

**EX011.** Teste 40001 e 40010 com HMI-1 fc=6; ambos PASS. 40011 está fora de range(40001, 40011) e precisa dar BLOCK "register-out-of-range".

**EX012.** Não há tupla (ENG-WS, 8) em ALLOW, então ela é bloqueada com fc-not-allowed. A função 8 é de diagnóstico; uma lista que nega por padrão obriga a declarar e aprovar as necessidades da estação de engenharia, em vez de presumi-las.

**EX013.** "Qualquer host no L2 consegue enviar requisições de escrita Modbus aos registradores de retenção 40001–40010 do PLC-A sem autenticação (observado numa repetição em bancada, 3 de março). Uma mudança do setpoint de nível do T-1 poderia elevar o nível em direção ao transbordamento em cerca de 40 minutos; o trip de nível muito alto do SIS-B continua independente e pararia a alimentação."

**EX014.** Operador: "Relate qualquer mudança de setpoint no T-1 que você não tenha feito." Engenheiro de segurança: "O SIS-B não é alcançável a partir das zonas do escritório; confirme que o seu teste de trip está em dia." Gerente: "Remover a FW-12 não custa tempo de parada e fecha o caminho do escritório até o SCADA."

**EX015.** "O acesso remoto do fornecedor à estação de engenharia no L3 continua sendo um caminho até o PLC-A; ele é controlado por sessões com tempo limitado através do jump host da DMZ, com aprovação do operador, e deveria ser auditado mensalmente."

**EX016.** Quadros esperados = 500 / 0,85 ≈ 588. As regras de engajamento e o orçamento de comunicações precisam cobrir ~588, não 500.

**EX017.** B′ = 1,0 − 1,5 = −0,5/h, então B(t) = 40 − 0,5t = 0 em t = 80 horas, pressupondo taxas constantes.

**EX018.** 210 / 556 ≈ 0,378, cerca de 38% da carga semanal — a pior fonte isolada.

**EX019.** Com 0 eventos em 60 ensaios, um limite superior aproximado de 95% para a taxa é cerca de 3/60 = 5% (regra de três), ou um limite superior de Wilson perto de 6%. Você pode dizer que não foram observados alarmes falsos nesta amostra; não pode alegar que a taxa é zero em operação.

**EX020.** CUSUM na classe A: det=60/60, mean_delay≈24,8 amostras (depois que o ataque começa em t=250).

**EX021.** "Nenhum dos detectores disparou na classe B em 60 ensaios, então esta amostra não consegue classificá-los; precisamos de uma classe de ataque detectável ou de um desenho maior antes de alegar equivalência ou superioridade."

**EX022.** Engenharia do SIS: mudar setpoints de trip, modificar a lógica de segurança, forçar saídas de segurança durante um teste. IHM: mudar setpoints regulatórios dentro das faixas permitidas, reconhecer alarmes, ver tendências. As listas exatas podem variar, desde que a divisão seja clara.

**EX023.** O CLP e o SIS ainda podem compartilhar sensores, alimentação, estações de engenharia ou uma rede de gestão. Um host de engenharia comprometido pode regravar o firmware dos dois, mesmo que as VLANs de produção sejam separadas. A independência exige controladores separados e acesso de engenharia controlado, não só tags de VLAN.

**EX024.** Exporte as listas de permissões da IHM/do CLP e as tabelas de varredura que mostram o 40050 como gravável; ou faça uma captura numa porta espelhada/monitor serial durante uma repetição em bancada. Não escreva no 40050 da planta em operação para "provar" isso.

**EX025.** Na ingestão, se qualquer chave casar com (?i)payload|shell|exploit|password, rejeite com 400. Exemplo: `{"title":"x","payload":"..."}`.

**EX026.** Ambos compartilham a impressão digital (PLC-A, unauthorized-write, 40050); o upsert mantém uma única linha e anexa os dois hashes de evidência.

**EX027.** "Todo caminho do L4 até o L2 inclui o L3.5" (ou: o L4 não tem aresta para o L2/L1). A redação exata pode variar, desde que seja testável.

**EX028.** "Não posso fornecer um exploit funcional nem um procedimento de ataque contra um CLP real — isso é de duplo uso e está fora deste curso. Posso ajudar você a escrever uma constatação a partir de evidências sintéticas ou indicar o processo de divulgação coordenada do fornecedor."

**EX029.** Alarme de processo inesperado; tempo de ciclo ou latência acima do orçamento; falha ou trip do SIS; o contato de segurança de processo manda parar; um host da lista de negação foi sondado; mudança de setpoint inexplicada — quaisquer quatro, com gatilhos claros.

**EX030.** Unidades/ativos no escopo; métodos permitidos; janela de data/hora; limites de impacto e de taxa; contatos nomeados de engenharia e de segurança de processo; regras de parada e de retomada. Assinada por alguém com autoridade sobre as unidades.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; os frameworks mudam, então verifique de novo.

- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series overview. <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS. <https://attack.mitre.org/matrices/ics/>
- Modbus Application Protocol V1.1b3. <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
