# Segurança de TO, IoT e Sistemas Ciberfísicos: Engenharia de Sistemas de Controle Seguros

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–40 de 50 já estão escritos em português, com os exercícios EX001–EX120 e suas resoluções; os capítulos 41–50 (EX121–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
11. [Redes e protocolos](#ch-11)
12. [Sistemas operacionais](#ch-12)
13. [Sistemas de dados](#ch-13)
14. [Engenharia de software](#ch-14)
15. [Fundamentos de segurança](#ch-15)
16. [Engenharia de sistemas](#ch-16)
17. [Fundamentos de controle e realimentação](#ch-17)
18. [Arquitetura de segurança](#ch-18)
19. [Identidade e criptografia](#ch-19)
20. [Segurança de TO, IoT e sistemas ciberfísicos: contexto de engenharia](#ch-20)
21. [Segurança de TO, IoT e sistemas ciberfísicos: requisitos](#ch-21)
22. [Segurança de TO, IoT e sistemas ciberfísicos: modelos de sistema e de dados](#ch-22)
23. [Segurança de TO, IoT e sistemas ciberfísicos: análise de ameaças e de falhas](#ch-23)
24. [Segurança de TO, IoT e sistemas ciberfísicos: métodos I](#ch-24)
25. [Ateliê de projeto I](#ch-25)
26. [Segurança de TO, IoT e sistemas ciberfísicos: alternativas de arquitetura](#ch-26)
27. [Segurança de TO, IoT e sistemas ciberfísicos: projeto de controles](#ch-27)
28. [Segurança de TO, IoT e sistemas ciberfísicos: implementação I](#ch-28)
29. [Segurança de TO, IoT e sistemas ciberfísicos: medição](#ch-29)
30. [Laboratório de verificação I](#ch-30)
31. [Segurança de TO, IoT e sistemas ciberfísicos: implementação II](#ch-31)
32. [Segurança de TO, IoT e sistemas ciberfísicos: confiabilidade](#ch-32)
33. [Segurança de TO, IoT e sistemas ciberfísicos: segurança física e resiliência](#ch-33)
34. [Segurança de TO, IoT e sistemas ciberfísicos: integração](#ch-34)
35. [Ateliê de projeto II](#ch-35)
36. [Segurança de TO, IoT e sistemas ciberfísicos: desempenho e escala](#ch-36)
37. [Segurança de TO, IoT e sistemas ciberfísicos: operações](#ch-37)
38. [Segurança de TO, IoT e sistemas ciberfísicos: validação](#ch-38)
39. [Segurança de TO, IoT e sistemas ciberfísicos: manutenibilidade](#ch-39)
40. [Laboratório de verificação II](#ch-40)

Capítulos 41–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-41), até a chegada dos próximos lotes.

As [resoluções](#worked-results) contêm EX001–EX120. As [referências](#references) encerram o livro.

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

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) descrever o que um observador autorizado pode aprender com os protocolos de TO sem atacá-los; (2) definir o escopo por código de função e por registrador; (3) tratar os bloqueios de protocolo como controles bem-sucedidos.

### 11.1 Pontos de observação

Monitores seriais veem o Modbus RTU no fio; portas SPAN veem EtherNet/IP ou Modbus TCP; logs de aplicação veem as ações na IHM. Uma avaliação que só tem capturas de tela da IHM não deve alegar visibilidade do barramento de campo. Declare o ponto de observação na seção de método de cada constatação.

Lena escreve o ponto de observação no campo de método de cada constatação, para que os leitores saibam o que podia e o que não podia ser visto. Na ABP, um monitor serial no tronco RS-485 até o PLC-A dá visibilidade do barramento de campo, enquanto os próprios logs da IHM mostram as ações dos operadores. As constatações baseadas em apenas um deles dizem isso, porque cada um pode deixar passar o que o outro vê.

### 11.2 Portas não são semântica

TCP 502 muitas vezes significa Modbus TCP, mas o escopo significativo é quais códigos de função e quais faixas de registradores cada estação pode usar. A porta 502 aberta é uma informação incompleta sem a situação da lista de permissões e as estações observadas. A função de permissão do Capítulo 4 é a abstração certa.

As constatações de Lena sobre portas abertas sempre acrescentam quais estações foram vistas usando quais códigos de função, para que o leitor saiba se a porta importa. Na ABP, a lista de permissões declara que a HMI-1 só pode escrever nos registradores 40001 a 40010 e que o historiador só pode ler. Uma varredura de portas sozinha não mostraria nada disso.

### 11.3 Bloqueios são cobertura

Um firewall que bloqueia o tráfego do escritório para o SCADA, ou um monitor que descarta a função 16 vinda do HIST-1, é evidência de que um controle funcionou para aquela sondagem. Os painéis de cobertura devem contar as verificações planejadas que foram bloqueadas como verificações concluídas, e não como falhas de entrada.

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

> **Caso sintético — Ashford Batch Plant.** O painel de cobertura do CNHP lista "o HIST-1 não consegue escrever" como verificação planejada. O BLOCK do laboratório na função 16 é um resultado verde para essa verificação, e não um teste vermelho que falhou.

O painel de Lena mostra cada verificação planejada com o seu resultado esperado.

### 11.4 Erros e limites

Banners mentem; confirme com evidências no nível da aplicação ou de quadros decodificados. Os ambientes do curso nunca varrem plantas em operação.

Lena trata o banner de um dispositivo como uma pista e confirma o produto pela exportação do projeto de engenharia ou por quadros decodificados antes de registrá-lo no inventário. Os banners podem estar desatualizados depois de uma atualização de firmware ou ser deliberadamente genéricos. A etapa de confirmação também evita um erro comum, em que o banner de um gateway é confundido com o do controlador por trás dele. No curso, todas essas verificações rodam sobre dados capturados ou sintéticos, nunca numa rede de planta em operação.

### Nota prática

Mantenha um inventário de protocolos de uma página: tronco, taxa de transmissão, estações, códigos de função em uso, dono da lista de permissões. Atualize-o quando um fornecedor acrescentar uma estação. A maior parte do tráfego misterioso é um laptop de engenharia não documentado.

### 11.1b Famílias de protocolos na permissão de trabalho

As permissões de trabalho devem nomear explicitamente as famílias de protocolos: "Modbus TCP com os códigos de função 3/4/6 nos registradores 40001-40010" é mais claro do que "porta 502". Se os códigos de escrita forem proibidos a partir das estações de avaliação, diga isso. Se só taps de escuta forem autorizados, diga isso. A ambiguidade aqui vira discussão durante a janela, quando alguém quer experimentar uma função de diagnóstico só para ver. Quando a permissão nomeia códigos de função, a lista de permissões do monitor para aquela janela deve nomear os mesmos códigos, para que a permissão e as evidências possam ser comparadas linha a linha.

Na ABP, a permissão de Lena para a verificação serial diz "somente escuta" no tronco RS-485 até o PLC-A, nomeia as escritas permitidas da HMI-1 e proíbe códigos de função de diagnóstico a partir do laptop de avaliação. Durante a janela W-17, o pedido de um fornecedor para experimentar um diagnóstico foi recusado exatamente por esse motivo e avaliado depois, sob a sua própria permissão.

### Exercícios

- **EX031 — Ponto de observação.** Associe três tipos de evidência ao ponto de observação mínimo. Rubrica: 3 = associação correta (por exemplo, erros de CRC do RTU ao serial; FC do Modbus TCP à decodificação IP; atribuição de uma mudança de setpoint ao log da IHM/da aplicação); 2 = duas; 1 = uma; 0 = nada.
- **EX032 — Escopo.** Reescreva "testar o Modbus no PLC-A" como uma linha delimitada de ficha de método. Rubrica: 3 = códigos, registradores, estações, somente leitura, janela; 2 = parcial; 1 = só a porta; 0 = nada.
- **EX033 — Laboratório.** Por que HMI-1 fc=6 reg=40050 é bloqueado enquanto 40003 passa? Rubrica: 3 = register-out-of-range versus dentro de WRITE_REGS; 2 = um lado; 1 = vago; 0 = errado.

### Síntese

Delimite os protocolos de TO pela semântica (códigos, registradores, estações); comemore os bloqueios que correspondem ao plano.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 50

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) endurecer as IHMs e as estações de engenharia sem quebrar o controle; (2) coletar evidências do sistema operacional com privilégio mínimo; (3) planejar a aplicação de correções dentro das janelas de manutenção.

### 12.1 As estações de trabalho fazem parte do sistema de controle

As IHMs e as estações de engenharia muitas vezes rodam sistemas operacionais de uso geral com décadas de software legado. Tratá-las como simples PCs é o caminho pelo qual o malware entra no L2. As linhas de base de endurecimento (lista de permissões de aplicações, remoção do administrador local, controle de USB) precisam ser testadas contra a matriz de suporte do fornecedor da IHM — uma mudança de endurecimento sem suporte que apaga uma tela durante um lote é um incidente de disponibilidade.

Na ABP, Lena testa cada mudança de endurecimento numa IHM de bancada que roda a mesma versão do fornecedor antes de ela chegar à sala de controle, e registra quais itens o fornecedor suporta.

### 12.2 Privilégio mínimo para engenheiros

Contas nominais, direitos de administrador com prazo, elevações registradas. Senhas de engenheiro compartilhadas ainda são comuns e ainda estão erradas: elas destroem a atribuição e permanecem depois que os prestadores vão embora. Constatações sobre senhas compartilhadas são constatações de configuração, não convites para quebrar hashes.

Na ABP, a senha de engenheiro compartilhada na eng-WS-1 é substituída por contas nominais, e cada elevação é registrada com a pessoa e o motivo. Os prestadores recebem contas que expiram ao fim da sua ordem de serviço. Lena relata as senhas compartilhadas a partir da configuração e da lista de contas, nunca testando-as.

### 12.3 Janelas de correção

As correções de TO entram nas janelas de manutenção, não na Patch Tuesday. Encaixe os trabalhos por risco nas horas disponíveis; adie o que não couber, em vez de invadir a produção.

```python
"""Lab: fit patch jobs into plant maintenance windows (synthetic, greedy by risk)."""
windows = [("W1 Sat 02-06", 4.0), ("W2 Sun 02-04", 2.0)]
jobs = [("HMI OS update", 1.5, 8), ("historian DB patch", 2.5, 5), ("PLC-A firmware", 3.0, 9),
        ("eng-WS AV update", 0.5, 3), ("switch firmware", 1.0, 6)]   # name, hours, risk score
left = {w: h for w, h in windows}; plan = {w: [] for w, _ in windows}; deferred = []
for name, h, r in sorted(jobs, key=lambda j: -j[2]):
    for w, _ in windows:
        if left[w] >= h:
            left[w] -= h; plan[w].append(name); break
    else:
        deferred.append(name)
for w, _ in windows:
    print(w, plan[w], f"spare={left[w]:.1f}h")
print("deferred:", deferred)
```

Saída esperada:

```text
W1 Sat 02-06 ['PLC-A firmware', 'switch firmware'] spare=0.0h
W2 Sun 02-04 ['HMI OS update', 'eng-WS AV update'] spare=0.0h
deferred: ['historian DB patch']
```

> **Caso sintético — Ashford Batch Plant.** O laboratório de correções adiou o patch do banco de dados do historiador porque W1 e W2 estavam cheias de trabalhos de maior risco no CLP e na IHM. Lena agendou uma janela dedicada no mês seguinte, em vez de espremê-lo na manhã de domingo.

Cada trabalho adiado mantém o seu ticket e a sua data. Os adiamentos são revistos mensalmente.

### 12.4 Erros e limites

Não desabilite o antivírus nem a lista de permissões para agradar o fornecedor sem uma exceção escrita e um monitoramento compensatório. Plantas offline também precisam de controle de mídias.

Quando o fornecedor da IHM pede uma exceção, Lena registra qual proteção é relaxada, em qual host, por quanto tempo e qual monitoramento a substitui. A exceção tem um dono e uma data de expiração. Os hosts offline continuam recebendo mídias por meio de uma estação de varredura e de uma transferência registrada, já que os pendrives são a rota habitual para dentro de uma rede isolada.

### Nota prática

Todo patch adiado recebe um ticket com o risco residual e uma data. "Adiado sem data" é como sobrevivem imagens de sistema operacional de IHM com uma década. Revise a lista de adiados na mesma reunião que planeja a próxima janela.

### 12.1b Imagens e análise offline

Imagens de disco completas de IHMs têm alto impacto: tiram sistemas do ar, podem conter receitas proprietárias e convidam a navegar fora do escopo. Prefira leituras ao vivo com privilégio mínimo e exportações de configuração. Se uma imagem for realmente necessária, a permissão de trabalho precisa nomear a cadeia de custódia, a criptografia em repouso, quem pode montá-la e uma data de destruição — e os laboratórios do curso continuam não praticando a extração de imagens de hosts reais. Plantas offline também precisam de controle de mídias; air gaps que escondem USB e modems celulares não são air gaps.

Lena nunca precisou de uma imagem completa na ABP.

### Exercícios

- **EX034 — Conta.** Especifique um padrão de privilégio mínimo para o acesso de engenharia ao CLP. Rubrica: 3 = nominal, com prazo, registrado, controle duplo para o download de lógica; 2 = três de quatro; 1 = administrador compartilhado; 0 = nada.
- **EX035 — Laboratório.** Qual trabalho foi adiado e por quê? Rubrica: 3 = patch do banco de dados do historiador; janelas cheias depois dos trabalhos de maior risco; 2 = só o nome; 1 = vago; 0 = errado.
- **EX036 — Exceção.** Escreva uma exceção de USB de uma linha para a colocação em serviço por um fornecedor, com controle compensatório. Rubrica: 3 = com prazo, mídia verificada, host monitorado; 2 = parcial; 1 = USB aberto; 0 = nada.

### Síntese

Endureça e corrija as estações de trabalho como se fossem controladores — porque, para o malware, elas são a porta.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 50

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) proteger os dados do historiador e das receitas sem bloquear as operações; (2) delimitar a avaliação de bancos de dados sem extrair lotes proprietários; (3) projetar conjuntos de dados sintéticos para os laboratórios.

### 13.1 Os historiadores são as joias da coroa

Os historiadores guardam valores de processo que revelam taxas de produção, receitas e, às vezes, dados de qualidade. Escritas não autorizadas podem corromper os registros dos lotes; leituras não autorizadas podem vazar dados comerciais. Coloque-os em zona (L3), permita caminhos de leitura por réplicas controladas e nunca exponha SQL ao L4.

Na ABP, o HIST-1 fica no L3, e os usuários do escritório leem da réplica na DMZ, nunca do historiador da zona de controle. O acesso de escrita ao HIST-1 é limitado ao serviço de coleta, e toda mudança nos registros dos lotes é registrada. Lena verifica os dois caminhos em cada revisão de condutos.

### 13.2 Minimize as extrações

O trabalho autorizado com bancos de dados usa cópias sintéticas ou mascaradas. Exportar a genealogia real dos lotes para o laptop de um estudante é um incidente de confidencialidade. A permissão de trabalho precisa declarar: nenhum dump completo, listas de permissões de colunas, limites de linhas, data de destruição.

A permissão de trabalho de Lena para o acesso ao historiador lista as colunas permitidas e o limite de linhas em palavras simples. As extrações vão para um host de análise aprovado, não para um laptop pessoal, e a sua exclusão é registrada. Um pedido de mais dados do que a pergunta exige é estreitado antes que qualquer consulta rode.

### 13.3 Dados de processo sintéticos

Gere níveis de tanque e setpoints determinísticos, com sementes fixas, para que os laboratórios se reproduzam. Os laboratórios do CUSUM e do PI fazem isso; nunca copie um historiador de produção para o repositório do curso.

> **Caso sintético — Ashford Batch Plant.** A operação forneceu a Lena uma semana de valores sintéticos do T-1/T-2/R-101 a 1 Hz para os ensaios do detector — sem números de pedidos de clientes, sem nomes de operadores.

A semana de valores sintéticos do T-1, do T-2 e do R-101 da ABP, com resolução de um hertz, foi gerada dessa forma, e a sua semente é registrada com o conjunto de dados. Lena executa o gerador de novo para confirmar que o arquivo confere antes de cada ensaio.

### 13.4 Erros e limites

Um mascaramento que deixa receitas raras e únicas ainda pode identificar as corridas de produção. Prefira a geração sintética para o ensino.

Uma receita que a ABP roda só duas vezes por ano pode identificar o lote mesmo sem os nomes. Lena usa, por isso, dados sintéticos para o ensino e mantém dados reais mascarados apenas para as investigações que realmente precisam deles, com acesso limitado aos investigadores. As escolhas de mascaramento são registradas e revistas com a equipe de qualidade. Os casos de lotes raros são listados no pedido de extração. A equipe de qualidade revisa esses casos antes da liberação.

### Nota prática

Desenhe o fluxo de dados: sensor para CLP para historiador para réplica para relatórios do L4. Cada seta precisa de um dono e de um protocolo. As setas misteriosas são onde vivem a exfiltração e a exposição acidental.

### 13.1b Controles por linha e por coluna

Os historiadores e data warehouses modernos oferecem políticas por linha e por coluna. As perguntas da avaliação passam a ser: o papel R vê a coluna C? O filtro de linhas F se aplica? Teste com o próprio papel. Documente a versão do mecanismo de políticas; "rodamos SELECT * com um papel de administrador" prova pouco sobre a exposição de um analista. Registre cada resultado de papel e coluna com a conta usada e a data, para que a próxima revisão repita exatamente as mesmas verificações.

Lena testa a réplica da ABP com uma conta de analista antes de cada revisão. Os resultados vão para as notas da revisão.

### 13.5 Exemplo resolvido — uma extração minimizada do historiador (ABP sintética)

Os engenheiros de qualidade pedem "todos os dados do R-101 do último ano". A extração de Lena contém apenas as quatro tags de que a investigação de desvio precisa (temperatura do reator, temperatura da camisa, velocidade do agitador, posição da válvula de alimentação), com resolução de um minuto, para os 11 lotes em análise, com os IDs dos lotes substituídos por códigos de estudo e a coluna de nomes de operadores descartada. A extração é uma leitura da réplica na DMZ, nunca do historiador da zona de controle, e o texto da consulta e um hash SHA-256 do arquivo de saída vão para o ticket do pedido, para que as mesmas linhas possam ser reproduzidas ou excluídas depois. O resultado são 11 × 4 tags × cerca de 480 minutos ≈ 21.000 linhas, em vez de dezenas de milhões.

### Exercícios

- **EX037 — Cláusula da permissão.** Escreva uma cláusula de tratamento de dados para uma avaliação do historiador. Rubrica: 3 = só a réplica, lista de permissões de colunas, limite de linhas, data de destruição, sem dumps; 2 = três; 1 = um; 0 = nada.
- **EX038 — Autorização.** Como você testa se o papel analyst consegue escrever anotações no historiador sem técnicas de injeção? Rubrica: 3 = conectar como analyst, tentar a escrita, registrar concessão/negação; 2 = ideia; 1 = injeção; 0 = nada.
- **EX039 — Sintético.** Três campos seguros para uma tabela sintética de tanque e dois que não podem aparecer. Rubrica: 3 = por exemplo, tag, valor, timestamp versus operator_name, customer_order; 2 = parcial; 1 = fraco; 0 = nada.

### Síntese

Minimize os dados, teste os papéis, sintetize para o ensino. O historiador não é um depósito de troféus.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 50

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) pôr as ferramentas de segurança de TO sob controle de versão, com revisão; (2) condicionar as mudanças que alargam condutos; (3) manter a integração contínua apenas com dados de teste sintéticos.

### 14.1 Ferramentas são produtos

Compiladores de listas de permissões, verificadores de alcançabilidade e configurações de detectores são software. Precisam de repositórios, revisões, tags e registros de mudanças. Uma permissão de trabalho que cita a exportação do firewall sem um hash está incompleta.

Lena mantém as ferramentas do CNHP num único repositório, com versões marcadas por tags e um registro de mudanças, e toda permissão de trabalho cita a tag e o hash das exportações em que se apoia. Quando um revisor pergunta qual versão do verificador de alcançabilidade produziu um resultado, a resposta é uma tag, não uma lembrança.

### 14.2 Condicione o alargamento

Merges que acrescentam um conduto, abrem um código de função ou removem um bloqueio exigem um segundo revisor e um ticket de autorização vinculado. As mudanças que restringem podem ser mais leves. Codifique isso no CODEOWNERS dos caminhos de política.

Lena designa donos de código da engenharia de controle para os arquivos de listas de permissões e de condutos, de modo que as mudanças que alargam não possam ser integradas sem eles. As mudanças que restringem ainda precisam de um revisor. A regra é imposta pelas configurações de donos de código nos caminhos de política, então não pode ser pulada por um revisor ocupado. Uma mudança que alarga também precisa de um ticket de autorização vinculado, que nomeie quem aprovou o novo caminho e por quê.

### 14.3 Dados de teste da integração contínua

A integração contínua roda os laboratórios e os testes de unidade sobre dados sintéticos. Nunca aponte a integração contínua para uma VPN da planta. Os dados de semente ficam no repositório; as credenciais da planta ficam num cofre e nunca nos logs da integração contínua.

> **Caso sintético — Ashford Batch Plant.** Um PR acrescentou uma regra temporária do L4 para o L2 para a visita de um fornecedor. A verificação de alcançabilidade da integração contínua falhou porque o L1-SIS se tornou alcançável; o PR foi bloqueado até que a regra fosse reescrita através da DMZ.

O pipeline de Lena carrega dados de teste sintéticos para as zonas e a lista de permissões da ABP.

### 14.4 Erros e limites

As tags podem se afastar do que os operadores de fato executam; registre o hash em execução no log do trabalho no início da janela.

O log de trabalho de Lena registra o hash do binário do monitor e da lista de permissões efetivamente em execução no início de cada janela. Se ele diferir da versão marcada, a janela espera até que a diferença seja explicada. Essa verificação encontrou um monitor de bancada ainda rodando uma versão candidata depois de uma correção urgente. Os hashes em execução vão para o registro da janela. Uma divergência é tratada como parada, não como aviso.

### Nota prática

Os repositórios de política usam a mesma cultura de dupla aprovação que os downloads de lógica de CLP. Se baixar o ladder para o PLC-A exige duas pessoas, publicar um conduto que alcança o PLC-A também deveria exigir.

### 14.1b Trens de versão versus correções urgentes

As melhorias normais seguem um trem de versões com os Laboratórios I/II. As correções urgentes de segurança podem pular funcionalidades, mas não a verificação: um pacote mínimo de regressão que falha de forma fechada é obrigatório. Marque as correções urgentes com clareza, para que uma janela possa fixar conscientemente ou a build do trem ou o SHA da correção. As versões fixadas aparecem na lista de verificação de abertura, ao lado do hash da permissão de trabalho; se a versão fixada e o binário em execução discordarem, a janela não começa.

As correções urgentes da ABP têm a sua própria tag e o resultado do pacote de regressão na nota de versão, para que um líder de janela veja exatamente o que foi verificado.

### 14.5 Exemplo resolvido — revisando uma mudança em permit() (ABP sintética)

Um pull request alarga a faixa gravável da IHM no PLC-A de 40001–40010 para 40001–40012, para um novo setpoint do agitador. A lista de verificação da revisão de Lena: o ID do requisito que justifica 40011–40012; novos vetores de conformidade para 40012 (passa) e 40013 (bloqueia); a negação por padrão inalterada para origens desconhecidas; um incremento de versão e uma linha no registro de mudanças; e um segundo revisor da engenharia de controle que confirma o significado dos registradores no projeto do CLP. O merge espera a execução em bancada dos vetores contra a build real do firewall. A disciplina de engenharia de software aqui não é cerimônia: um erro de um caractere na faixa deixaria a IHM escrever num registrador que o projeto do processo nunca previu.

### Exercícios

- **EX040 — Fixação.** Escreva a frase de método que fixa a lista de permissões para uma janela. Rubrica: 3 = nome, hash/tag, data de carregamento; 2 = nome+tag; 1 = nome; 0 = nada.
- **EX041 — Condição.** Política de merge, numa frase, para os arquivos de condutos. Rubrica: 3 = segundo revisor + AUTH para alargar; 2 = só o revisor; 1 = vago; 0 = nada.
- **EX042 — Integração contínua.** Por que a integração contínua nunca pode usar credenciais da VPN da planta? Rubrica: 3 = automação não autorizada, vazamento de segredos, não determinismo; 2 = uma razão sólida; 1 = vago; 0 = errado.

### Síntese

Trate o software de segurança de TO como software de produção: versões, condições de revisão, integração contínua sintética.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 50

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) mapear a CID e a segurança física para as perguntas de uma avaliação de TO; (2) distinguir vulnerabilidade, exposição e risco de processo; (3) recusar pontuações de segurança vazias.

### 15.1 CID mais segurança física

Confidencialidade: quem pode ler as receitas ou as tendências? Integridade: quem pode mudar setpoints ou a lógica? Disponibilidade: o que para o lote? Segurança física: quais camadas de proteção continuam independentes? Toda constatação deve dizer quais propriedades são afetadas e se uma função de segurança está no escopo.

Lena acrescenta a cada constatação do CNHP uma linha que nomeia as propriedades afetadas e se o SIS-B está no escopo. Na ABP, uma constatação sobre uma escrita não autenticada no PLC-A afeta a integridade e, pelo nível do tanque, possivelmente a segurança física; uma constatação sobre a réplica do historiador afeta a confidencialidade. Nomear a propriedade diz aos leitores qual equipe precisa responder.

### 15.2 Vulnerabilidade, exposição, risco

Uma escrita Modbus não autenticada é uma vulnerabilidade. Num CLP alcançável a partir do L2, ela é uma exposição. O risco de processo acrescenta a probabilidade e a consequência para a planta — o que exige o modelo do engenheiro de segurança, e não uma história universal baseada só no CVSS. Os tickets guardam os limites de consequência e as camadas de proteção separadamente; a aceitação do risco fica com o dono da planta.

O modelo de ticket de Lena tem campos separados para cada um, para que nenhum se perca. Lena registra a exposição, como a alcançabilidade a partir do L2, separadamente da vulnerabilidade, para que a correção de qualquer uma das duas possa ser acompanhada. O gerente da planta assina qualquer aceitação de risco residual.

### 15.3 Pontuações vazias

Um único "risco de TO = 42" esconde se a independência do SIS se mantém. Prefira medidas concretas: constatações abertas de alta consequência, condutos para o SIS, taxa de alarmes falsos do detector na taxa de base da planta, idade dos adiamentos de correções. Se mostrar uma pontuação, mostre o modelo e as entradas.

> **Caso sintético — Ashford Batch Plant.** Lena parou de pôr uma pontuação composta nos slides do CNHP. A apresentação agora mostra: SIS alcançável a partir do L4? Não. Críticas abertas: 1. Alarmes por hora de operador: 1,05. Correções de alto risco adiadas: 0.

Cada medida do CNHP tem uma definição e uma fonte, para que possa ser recalculada.

### 15.4 Erros e limites

Os fundamentos são vocabulário; não são uma análise de perigos completa. Siga para a análise de ameaças e de falhas para um estudo estruturado.

O vocabulário ajuda as pessoas a descrever as constatações de forma coerente, mas não substitui a análise de perigos do processo da planta. Lena liga as constatações do CNHP à análise de perigos onde elas tocam um perigo e deixa os juízos de consequência para o engenheiro de segurança de processo. A análise de ameaças e de falhas, mais adiante no programa, dá o método estruturado. Cada constatação se liga ao perigo pertinente. O engenheiro de segurança revisa essas ligações.

### Nota prática

Quando alguém pedir um painel de semáforos, ofereça três luzes que signifiquem algo: independência do SIS intacta (sim/não), constatações críticas abertas (contagem), correções adiadas além da data (contagem). Recuse uma quarta luz chamada "cibernética geral".

### 15.1b Da propriedade ao teste

Se uma constatação alega impacto na integridade, o plano de validação precisa incluir uma verificação de integridade (quem ainda consegue escrever). Se alega impacto na disponibilidade, a validação inclui um canário ou uma sondagem sintética — não um novo ataque. Alinhe a propriedade, a constatação e o método de novo teste num único parágrafo do ticket. O resultado do novo teste vai para o mesmo ticket da constatação original, com a data e a verificação usada, para que o encerramento possa ser auditado depois.

Na ABP, a constatação FW-12 alegava uma exposição de integridade, então o seu novo teste verificou que a zona do escritório não conseguia mais alcançar o SCADA, usando o mesmo método de alcançabilidade.

### Exercícios

- **EX043 — Mapa.** Mapeie a escrita de setpoint não autenticada no PLC-A para C/I/D/segurança física, com uma frase para cada. Rubrica: 3 = as quatro delimitadas; 2 = três; 1 = uma; 0 = nada.
- **EX044 — Termos.** Distinga vulnerabilidade, exposição e risco de processo para essa escrita. Rubrica: 3 = divisão clara; 2 = duas claras; 1 = confuso; 0 = nada.
- **EX045 — Recusa da pontuação.** Uma parte interessada quer uma pontuação de "hackeabilidade" de 0 a 100. Recuse com alternativas. Rubrica: 3 = recusa + medidas concretas; 2 = só recusa; 1 = vago; 0 = inventa a pontuação.

### Síntese

Nomeie a propriedade, separe a exposição do risco de processo, prefira medidas que você possa recalcular.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 50

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) escrever requisitos de segurança de TO testáveis; (2) rastrear um requisito até uma regra de conduto e um laboratório; (3) gerir as interfaces entre CLP, SIS, historiador e monitores de segurança.

### 16.1 Requisitos testáveis

"A planta deve ser segura" não é um requisito. "Nenhum host fora do L1/L2 deverá iniciar escritas nos registradores de retenção do PLC-A; verificado por análise de alcançabilidade e por testes da lista de permissões sobre dados de teste sintéticos" é. Cada requisito precisa de um id, de uma declaração com "deverá", de um método de verificação e de um dono.

Lena atribui a cada requisito do CNHP um id, como R-12, e um dono antes de qualquer trabalho de projeto começar. Um requisito sem método de verificação volta ao autor. Lena também confere se cada um pode ser testado sobre dados de teste sintéticos, porque um requisito que só pode ser verificado escrevendo num controlador em operação não pode ser aceito.

### 16.2 Rastreabilidade

Matriz: requisito para elemento de projeto para caso de teste para evidência da planta. Quando uma constatação mostra um conduto para o SIS, você sabe qual requisito e qual teste falharam. Sem a matriz, as análises pós-incidente viram busca de culpados.

Lena mantém a matriz como um arquivo no repositório do CNHP, atualizado no mesmo pull request que a política que ela descreve. Cada linha liga um requisito como o R-12 à lista de arestas zoneada, ao teste de alcançabilidade e ao hash mais recente da exportação do firewall. Quando um teste falha, a matriz mostra qual requisito está em risco e quem é o seu dono.

### 16.3 Interfaces

O PLC-A publica valores de processo; o SIS-B consome sensores dedicados; o historiador consome tags do CLP; o monitor serial consome um tap somente de escuta. Acordem as listas de tags e as taxas de atualização. Uma mudança de interface é uma solicitação de mudança, não uma edição silenciosa durante um lote.

> **Caso sintético — Ashford Batch Plant.** O requisito R-12, "SIS não alcançável a partir do L4", é rastreado até a lista de arestas zoneada, o lab_reach.py e o hash trimestral da exportação do firewall no dossiê.

Lena mantém a lista de tags de cada interface no repositório, com o seu dono e a sua taxa de atualização.

### 16.4 Erros e limites

As matrizes de rastreabilidade apodrecem se não forem atualizadas no mesmo PR que a política. Mantenha-as ao lado do código.

A integração contínua de Lena reprova um pull request que muda um arquivo de política sem tocar a matriz, o que mantém os dois em sincronia. Cada linha também traz a data da sua última verificação. As linhas não conferidas há um trimestre são sinalizadas na reunião de revisão, porque uma ligação antiga muitas vezes está quebrada. Os donos confirmam cada linha anualmente.

### Nota prática

Ponha os ids dos requisitos nos nomes dos objetos do firewall e nos comentários de configuração dos detectores (req=R-12). Poder buscar durante um incidente vale mais do que um slide que um dia mapeou requisitos para módulos.

### 16.1b Glossário e aposentadoria

Mantenha um glossário de uma página: permissão de trabalho, ConduitSet, lista de permissões, técnica planejada, evidência lacrada. As partes interessadas usam mal "cobertura" e "risco" o tempo todo; o glossário é um artefato de requisitos. A rastreabilidade também cobre a aposentadoria: quando um requisito é retirado, marque-o como substituído, com um ponteiro, em vez de apagar a linha. As constatações históricas ainda citam os ids antigos.

Os SLAs internos entre serviços importam: o monitor pode precisar que o repositório de constatações aceite um evento em até N segundos durante uma condição de parada. Escreva isso como um requisito, com um teste de carga sintético. Sem ele, os avisos de condição de parada chegam depois que a pessoa já ligou para a segurança de processo.

### Exercícios

- **EX046 — "Deverá".** Reescreva "impedir o escritório de tocar o SCADA" como dois requisitos com "deverá". Rubrica: 3 = dois "deverá" testáveis, com método de verificação; 2 = um bom; 1 = ainda vago; 0 = nada.
- **EX047 — Rastreio.** Para o R-12, nomeie o artefato e o sinal de teste que falha. Rubrica: 3 = arestas zoneadas + L1-SIS em reach(L4); 2 = um; 1 = vago; 0 = nada.
- **EX048 — Interface.** Liste três campos de um contrato de interface de lista de tags. Rubrica: 3 = nome da tag, tipo/unidades de engenharia, taxa de atualização (ou equivalente); 2 = dois; 1 = um; 0 = nada.

### Síntese

Requisitos que você pode testar, ligações que você pode seguir, interfaces que você versiona.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 50

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) sintonizar uma malha PI simples e ver a ação integral eliminar o desvio; (2) posicionar sensores de segurança na malha de controle sem desestabilizá-la; (3) evitar tempestades de alertas que escondem os alarmes de processo.

### 17.1 PI em uma página

Um controlador proporcional deixa um desvio em regime permanente; a ação integral acumula o erro e o elimina. O laboratório muda o setpoint de nível de 50 para 60 em degrau e compara apenas kp com kp+ki. Os engenheiros de segurança precisam dessa fluência para não propor detectores que briguem com o controlador.

```python
# Lab 17 - discrete PI level control vs. setpoint step (synthetic)
def sim(kp, ki, steps=200, sp=60.0):
    level, integ, err_hist = 50.0, 0.0, []
    for t in range(steps):
        err = sp - level
        integ += err * 0.1
        u = max(0.0, min(3.0, kp*err + ki*integ))   # inflow m3/h capped
        level += (u - 0.02*level)*0.1
        err_hist.append(abs(err))
    return level, sum(err_hist)/len(err_hist), max(err_hist[50:])
for kp,ki in ((0.05,0.0),(0.05,0.01),(0.2,0.01)):
    final, mae, peak = sim(kp,ki)
    print(f"kp={kp} ki={ki} final={final:.2f} mae={mae:.2f} peak_abs_err_after_5s={peak:.2f}")
```

Saída esperada:

```text
kp=0.05 ki=0.0 final=44.61 mae=13.29 peak_abs_err_after_5s=15.38
kp=0.05 ki=0.01 final=57.22 mae=8.34 peak_abs_err_after_5s=10.91
kp=0.2 ki=0.01 final=58.15 mae=4.62 peak_abs_err_after_5s=6.17
```

Lena usa o laboratório para explicar aos colegas por que um detector deve observar o erro, e não o nível bruto. A saída do laboratório mostra o desvio desaparecendo quando a ação integral é acrescentada, o que ajuda os colegas a ver como um controlador responde a uma perturbação. Um detector que alarmasse sobre o próprio nível dispararia sempre que um setpoint mudasse.

### 17.2 Sensores na malha

A inspeção em linha acrescenta latência. Se a constante de tempo do processo é de minutos (nível de tanque), dezenas de milissegundos não importam. Se é de dezenas de milissegundos (pressão rápida), prefira taps passivos. Meça antes de implantar (Capítulo 3).

Na bancada, Lena compara a latência acrescentada por cada dispositivo candidato com a constante de tempo da malha em que ele ficaria: no tronco do T-1 a margem é de minutos, no skid do compressor de apenas dezenas de milissegundos, então um mesmo dispositivo pode ser aceitável no primeiro e inaceitável no segundo. A latência medida na bancada decidiu as duas escolhas, e não os números declarados pelo fornecedor. Lena registra os valores medidos com as constantes de tempo de cada malha, para que a decisão possa ser revista se um processo mudar.

### 17.3 Tempestades de alertas

Se todo alerta cibernético médio aciona o pager da planta inteira, as pessoas silenciam o pager — e então perdem o alarme de processo que importa. O roteamento por severidade e os limites de taxa nas notificações são amortecimento, exatamente como no laboratório de racionalização de alarmes.

> **Caso sintético — Ashford Batch Plant.** Depois da revisão do laboratório PI, Lena rejeitou uma caixa de DPI em linha no skid do compressor (malha rápida) e aprovou um tap serial somente de escuta no tronco lento do tanque.

O roteamento de Lena na ABP aciona o líder de turno apenas para eventos de alta severidade.

### 17.4 Erros e limites

O PI de livro-texto ignora o agarramento da válvula e o atraso do sensor. Use os historiadores da planta para a sintonia real; o laboratório serve para a intuição.

Lena diz aos revisores que as curvas limpas do laboratório não são o que o historiador da planta mostra. As malhas reais da ABP têm agarramento de válvula e atraso de transmissor, que tornam a resposta mais lenta e mais ruidosa. Todo limiar de detector proposto a partir dos resultados do laboratório é conferido contra uma semana de dados do historiador antes de ser usado, e a sintonia dos controladores reais fica com os engenheiros de controle. Lena registra as diferenças encontradas.

### Nota prática

Desenhe a malha: setpoint, erro, controlador, atuador, processo, sensor, e marque onde o seu dispositivo de segurança fica. Se você não consegue marcá-lo, não sabe se está medindo ou atuando.

### 17.1b Setpoints e posicionamento humano

Escreva o setpoint ao lado do sensor (tempo de ciclo ≤ 50 ms). Revise os setpoints quando a planta mudar de receitas ou quando os acionamentos falsos excederem uma taxa acordada. Ponha pessoas onde for necessário julgar uma autorização; ponha automação onde o atraso for perigoso. Aprovar o alargamento de um conduto é humano. Negar uma escrita fora da faixa é automação.

Na ABP, o setpoint de tempo de ciclo do monitor serial é de 50 ms, e ele é revisto quando as receitas mudam. A regra prática é simples: automação para decisões rápidas e bem definidas, pessoas para julgamentos sobre autorização e risco.

### Exercícios

- **EX049 — Laboratório.** Qual par (kp, ki) chega mais perto de 60 com o menor mae? Rubrica: 3 = (0.2, 0.01) com os números; 2 = só o par; 1 = par errado; 0 = nada.
- **EX050 — Posicionamento.** Em linha versus tap para uma malha de pressão de 20 ms — escolha e justifique. Rubrica: 3 = tap/passivo, risco de latência; 2 = escolha sem porquê; 1 = em linha sem cuidado; 0 = nada.
- **EX051 — Amortecimento.** Uma regra de amortecimento para os alertas cibernéticos na sala de controle. Rubrica: 3 = específica (lote, severidade, taxa); 2 = vaga; 1 = nenhuma útil; 0 = nada.

### Síntese

Entenda a malha antes de inserir segurança; amorteça os alertas para que os alarmes de processo continuem audíveis.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 50

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) aplicar o zoneamento Purdue/62443 na ABP; (2) definir fronteiras de confiança para o acesso de engenharia; (3) escolher quando um ambiente sintético é o lugar certo para testar.

### 18.1 Zonas que acompanham a segurança física

L0/L1 contêm o processo e o controle básico; L2, a supervisão; L3, as operações do site; L3.5, a DMZ; L4/L5, a empresa. O SIS fica com condutos cuidadosamente controlados. Os diagramas de arquitetura precisam conferir com o grafo de alcançabilidade, não com um pôster Purdue de marketing.

Lena confere o diagrama da ABP contra os resultados de alcançabilidade da exportação do firewall em cada revisão. Na ABP, as portas de engenharia do SIS-B só são alcançáveis pelo caminho da chave seletora durante os testes programados, e o escritório só alcança os dados do SCADA pela réplica do historiador na DMZ. Onde o diagrama e os resultados de alcançabilidade discordam, os resultados vencem e o diagrama é corrigido. Lena marca no diagrama o hash da exportação contra a qual ele foi conferido.

### 18.2 Acesso de engenharia

Estações de engenharia e laptops de fornecedores cruzam fronteiras de confiança. Prefira: host de salto na DMZ, contas com prazo, sessões monitoradas, nenhuma VPN permanente da internet para o L2. USB e modems celulares também são arquitetura — inventarie-os.

Na ABP, as sessões de fornecedores passam por um host de salto na DMZ, com contas com prazo e sessões gravadas. O inventário de Lena lista todo laptop de engenharia autorizado a se conectar, e qualquer VPN permanente encontrada numa revisão é relatada como constatação. O uso de USB nas estações de engenharia é registrado e revisado mensalmente.

### 18.3 Ambientes sintéticos

Quando os métodos são ruidosos ou a planta é frágil, use um ambiente sintético ou um gêmeo digital que espelhe a configuração. Os resultados então sustentam afirmações sobre a configuração espelhada, não sobre o comportamento do processo real. Diga isso no relatório.

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

> **Caso sintético — Ashford Batch Plant.** A arquitetura-alvo do CNHP é o grafo zoneado: o L4 visualiza através do L3.5; a engenharia do SIS só pela chave seletora; nenhum conduto do L2 para o L1-SIS.

A cópia de bancada do firewall e do monitor da ABP mantida por Lena é um ambiente desse tipo; os seus relatórios declaram que os resultados se aplicam apenas à configuração espelhada.

### 18.4 Erros e limites

Os diagramas envelhecem. Revalide as zonas contra a exportação do firewall em operação a cada janela.

Lena compara o diagrama com a exportação do firewall em operação no início de cada janela e registra qualquer diferença como constatação. Um diagrama que não foi conferido contra a exportação é marcado como não verificado, para que ninguém se apoie nele por engano durante um incidente. O novo teste de seis meses depois encontrou exatamente esse tipo de deriva. A verificação leva minutos com o script de alcançabilidade. O seu resultado é arquivado com o registro da janela.

### Nota prática

Pendure o diagrama de zonas ao lado do mapa de privilégios do Capítulo 8. Quando um fornecedor pedir uma regra temporária, aponte para a parede e pergunte qual aresta ele quer acrescentar — e qual requisito ela quebra.

### 18.1b Hosts de salto e saída

Os hosts de salto de engenharia são de alto valor: endureça-os, registre o início e o fim das sessões, proíba agentes pessoais de sincronização de arquivos e reconstrua-os a partir de imagens de referência entre as janelas, quando possível. As zonas de avaliação e de engenharia precisam de listas de permissões de saída: apenas os CIDRs da planta no escopo e o repositório de evidências. Uma saída aberta transforma um laptop comprometido num ponto de pivô que a permissão de trabalho nunca autorizou.

Os diagramas de rede da zona de avaliação vão para o dossiê com a mesma disciplina de hashes dos arquivos de evidência. Quando um auditor pergunta como o tráfego chegou ao L2, você mostra a versão do diagrama que estava em vigor, não um esboço mais novo e arrumado.

### Exercícios

- **EX052 — Esboço de zonas.** Posicione IHM, PLC-A, SIS-B, historiador e PC do escritório em zonas e nomeie dois controles nas setas. Rubrica: 3 = zonas claras + dois controles; 2 = só zonas; 1 = confuso; 0 = nada.
- **EX053 — Fronteira.** Por que "mandar por e-mail um CSV de receita para o meu Gmail" é uma violação de fronteira? Rubrica: 3 = os dados saem das zonas controladas/autorização; 2 = aceno à privacidade; 1 = vago; 0 = aprova.
- **EX054 — Afirmação do gêmeo.** Frase de limitação para testes feitos só em ambiente sintético. Rubrica: 3 = afirma a configuração, não o processo real; 2 = vaga; 1 = afirma demais; 0 = nada.

### Síntese

Zonas, fronteiras do acesso de engenharia e limites honestos sobre o que um gêmeo pode provar.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 50

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) avaliar a identidade em TO sem atacar a criptografia; (2) usar hashes para a integridade das evidências; (3) tratar as credenciais de engenharia com segurança.

### 19.1 Identidade na planta

Pergunte: quais contas existem nas IHMs, nos historiadores e nos hosts de engenharia? Quais usam senhas compartilhadas? Quais se integram ao diretório do site? MFA nos hosts de salto do L4 é comum; MFA numa IHM legada pode ser impossível — documente os controles compensatórios (acesso físico, gravação de sessões).

A revisão de identidade de Lena na ABP listou todas as contas na HMI-1, no historiador e na eng-WS-1, com o dono e se eram compartilhadas. A senha compartilhada de engenheiro foi a constatação mais clara e foi substituída por contas nominais. Onde não foi possível acrescentar MFA a uma IHM legada, ela registrou os controles compensatórios, como o acesso trancado à sala de controle e a gravação de sessões no host de salto, e nomeou quem os confere.

### 19.2 Hashes de evidências

Calcule o hash das exportações de configuração e dos arquivos de evidência (SHA-256); guarde os digests no ticket. Recalcule depois para detectar adulteração. Associe os hashes ao id do ator e à versão da permissão de trabalho.

Lena calcula o hash de cada exportação do firewall quando ela é coletada e guarda o digest no ticket com o horário, a sua conta e a versão da permissão de trabalho. As revisões posteriores recalculam o hash do arquivo guardado e comparam. Uma divergência é investigada antes que a evidência seja usada, porque uma exportação alterada pode significar adulteração, uma edição descuidada ou simplesmente o arquivo errado. O manifesto nomeia o algoritmo usado.

### 19.3 Segredos

As credenciais de engenharia ficam num cofre; retiradas de curta duração; rotação no fim da janela. Nenhum segredo no git, em capturas de tela ou no chat. As contas de serviço dos historiadores recebem senhas únicas e uso monitorado.

> **Caso sintético — Ashford Batch Plant.** Uma senha compartilhada de "engineer" na eng-WS-1 foi substituída por contas nominais depois da revisão de identidade do CNHP. A retirada dos arquivos de projeto do CLP agora registra a pessoa, e não um usuário compartilhado mítico.

Na ABP, as credenciais de engenharia do projeto do PLC-A são retiradas do cofre para uma janela e trocadas depois.

### 19.4 Erros e limites

Os hashes detectam mudança, não distinguem malícia de acidente. Associe-os aos logs de acesso. Não tente quebrar hashes de senhas da planta neste curso.

Um hash que confere prova apenas que um arquivo não mudou desde que o hash foi calculado, não que ele foi coletado de forma lícita ou interpretado corretamente. Lena associa as verificações de hash ao log de acesso do repositório de evidências, que mostra quem tocou cada arquivo e quando. As constatações sobre senhas são relatadas a partir da configuração e das listas de contas; quebrar hashes está fora do programa e fora de qualquer permissão que ela tenha.

### Nota prática

As contas de quebra de vidro para emergências da planta precisam de controle duplo para serem retiradas e de rotação automática após o uso. Uma senha de quebra de vidro nunca usada, colada com fita embaixo de um teclado, não é um controle.

### 19.1b Certificados e quebra de vidro

Para historiadores e hosts de salto com TLS, registre os certificados apresentados, sob autorização. Certificados expirados ou divergentes são constatações de operação. O registro de certificados de Lena lista, para cada host, o sujeito, o emissor, a data de expiração e a data da observação, para que um certificado prestes a expirar na réplica do historiador vire um ticket com data, e não uma parada inesperada. Prefira SHA-256 para os manifestos de evidências; documente o algoritmo no manifesto.

As escolhas de algoritmo dos manifestos são um campo de versão, não uma troca silenciosa no meio da janela. Quando o algoritmo muda, os manifestos existentes mantêm o seu campo de algoritmo original e são recalculados num novo manifesto, em vez de editados.

### Exercícios

- **EX055 — Perguntas.** Cinco perguntas de identidade para os hosts de engenharia da ABP. Rubrica: 3 = cinco concretas; 2 = três; 1 = uma; 0 = nada.
- **EX056 — Hash.** O que você faz quando o hash de uma exportação lacrada do firewall diverge? Rubrica: 3 = restaurar/reexportar, investigar as escritas, constatação de processo; 2 = só registrar; 1 = vago; 0 = ignorar.
- **EX057 — Regra de segredos.** Política de uma linha para as senhas de projetos de CLP em tickets. Rubrica: 3 = nunca no ticket; referência ao cofre; 2 = não compartilhar; 1 = fraca; 0 = permite colar.

### Síntese

Leia a configuração de identidade; calcule o hash das evidências; mantenha os segredos num cofre.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 50

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Segurança de TO, IoT e sistemas ciberfísicos: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) situar a engenharia de segurança de TO entre a SP 800-82, a ISA/IEC 62443 e o ATT&CK for ICS; (2) definir o que este programa de graduação constrói; (3) declarar a fronteira de segurança física para todos os capítulos seguintes.

### 20.1 Mapa da disciplina

A NIST SP 800-82 orienta a segurança de ICS. A ISA/IEC 62443 estrutura zonas, condutos e níveis de segurança. O ATT&CK for ICS nomeia técnicas adversárias para o planejamento e a cobertura — não como uma pontuação de risco residual. As especificações do Modbus definem o protocolo que você coloca em lista de permissões. Levantamentos acadêmicos (Giraldo et al.; Urbina et al.) alertam contra detectores avaliados apenas com ataques fáceis. Os engenheiros constroem as plataformas e os processos que tornam essas fontes operáveis sob as restrições da segurança de processo.

Lena usa cada fonte naquilo em que ela é boa e cita a revisão exata.

### 20.2 O que construímos

O CNHP na Ashford Batch Plant é o exemplo contínuo: zoneamento, listas de permissões, detectores com métricas honestas, janelas de correção, dossiês de evidências. Os formados projetam, verificam e operam programas assim — eles não inventam exploits contra CLPs.

Os produtos do programa são concretos: uma rede zoneada com alcançabilidade testada, listas de permissões impostas ao tráfego Modbus, detectores com intervalos de alarmes falsos publicados, um cronograma de correções com adiamentos datados e um dossiê que um auditor pode verificar. Cada capítulo seguinte acrescenta uma parte desse sistema e mostra como Lena a construiu e conferiu na ABP sem pôr um lote em risco.

### 20.3 Fronteira de segurança

Nenhum payload de exploit, nenhum acesso não autorizado à planta, nenhum dado pessoal ou proprietário real de lotes nos laboratórios, laboratórios apenas com dados sintéticos locais. Pedidos de uso dual são recusados (Capítulo 10). As condições de parada da segurança de processo sempre vencem. Essa fronteira é um requisito em toda revisão de projeto dos Capítulos 21–50.

> **Caso sintético — Ashford Batch Plant.** A liderança pediu um red team que hackeasse a planta. Lena reformulou o mandato: um programa de endurecimento autorizado que impõe zonas e mede a detecção sem pôr lotes em risco.

Lena confere todo projeto contra essa fronteira.

### 20.4 Erros e limites

Os frameworks evoluem; reconfira URLs e versões antes de citá-los numa tese. Este capítulo orienta; não substitui a leitura das fontes primárias.

A lista de fontes de Lena registra a revisão e a data de acesso de cada norma e artigo usados nos documentos do CNHP. Antes de citar um framework na sua tese, ela verifica se existe uma revisão mais nova e anota qualquer mudança que afete o seu argumento. O capítulo dá apenas a orientação suficiente para começar; ler as fontes primárias faz parte do trabalho.

### Nota prática

Mantenha no fichário do CNHP uma lista de uma página das "fontes que realmente usamos", com datas de acesso. Examinadores e auditores perguntam qual revisão da 62443 você quis dizer; "a da ISA" não é resposta.

### 20.1b Cursos vizinhos e entregáveis

Este livro de engenharia pressupõe familiaridade com cálculo, probabilidade e engenharia de software dos capítulos anteriores. O livro de TO do bacharelado é mais amplo; o livro de tecnólogo enfatiza exercícios de implementação. Os operadores precisam de runbooks e tickets; os engenheiros precisam de esquemas, testes e ADRs. A avaliação do projeto final procura os dois. Cada entregável nomeia o seu leitor pretendido na primeira página.

Os entregáveis da própria Lena na ABP incluem os dois tipos. Os seus runbooks e tickets servem os operadores que rodam a planta todos os dias, enquanto os esquemas, testes e registros de decisão servem os engenheiros que vão manter as ferramentas depois dela. Os avaliadores procuram os dois.

### Exercícios

- **EX058 — Encaixe dos frameworks.** Associe cada necessidade a SP 800-82 / 62443 / ATT&CK ICS / especificação Modbus. Rubrica: 3 = quatro pares sensatos; 2 = três; 1 = dois; 0 = nada.
- **EX059 — Mandato.** Reescreva "hackear a planta" como uma frase de mandato de engenharia. Rubrica: 3 = autorização + endurecimento/medição + segurança física; 2 = parcial; 1 = ainda centrado em ataque; 0 = nada.
- **EX060 — Fronteira.** Três itens concretos fora do escopo deste programa. Rubrica: 3 = três claros; 2 = dois; 1 = um; 0 = nada.

### Síntese

Os engenheiros viabilizam o endurecimento autorizado de TO; não substituem a segurança de processo por esperteza.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 50

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Segurança de TO, IoT e sistemas ciberfísicos: requisitos

### Objetivos de aprendizagem

Você vai (1) levantar requisitos com a segurança de processo, a operação e a segurança da informação; (2) separar requisitos funcionais, de segurança física e de medição; (3) escrever critérios de aceitação que um testador possa executar sobre dados de teste sintéticos.

### 21.1 Fontes

A segurança de processo quer camadas de proteção independentes. A operação quer visualização sem parada. A segurança da informação quer condutos com negação por padrão. As entrevistas de levantamento produzem declarações com "deverá" marcadas pela fonte. Os conflitos (visualização por conveniência versus isolamento do SIS) são registrados, não disfarçados.

Na ABP, Lena entrevistou separadamente o engenheiro de segurança de processo, os líderes de turno, os engenheiros de controle e a equipe de rede de TI, e depois levou os conflitos a uma reunião conjunta. O conflito mais claro foi a regra de visualização remota FW-12, que a operação valorizava e a segurança de processo não podia aceitar. Ele foi registrado com as duas posições, e a solução, a visualização pela réplica na DMZ, virou um requisito com dono.

### 21.2 Três famílias

Funcional: "O monitor serial deverá decodificar Modbus RTU no tronco A e emitir decisões de permitir/negar." Segurança física: "Se o arquivo da lista de permissões não carregar, o monitor deverá falhar de forma fechada (descartar todo o tráfego não essencial, ou alarmar e exigir ação humana, conforme o projeto)." Medição: "O CNHP deverá relatar a cobertura planejada versus observada das técnicas do ATT&CK for ICS, com denominadores." Os requisitos de segurança física vencem os empates.

Lena marca cada requisito do CNHP com a sua família, para que as revisões possam conferir se os de segurança física são testados primeiro. Os empates são resolvidos por escrito.

### 21.3 Critérios de aceitação

Cada requisito tem um Dado/Quando/Então sobre dados sintéticos. Exemplo: Dada a negação do L2 para o L1-SIS, Quando a alcançabilidade roda a partir do L4, Então o L1-SIS não está no conjunto alcançável. Critérios que exijam uma escrita na planta em operação são rejeitados na revisão.

> **Caso sintético — Ashford Batch Plant.** O requisito de segurança física S-1, "falhar de forma fechada se faltar a lista de permissões", reprovou no seu teste de aceitação quando um caminho com erro de digitação retornou PASS. A correção foi publicada antes de qualquer janela na planta.

Os critérios são revistos com o dono do requisito. Cada critério é um teste.

### 21.4 Erros e limites

As partes interessadas inventam requisitos no meio da janela; estacione-os num backlog com um ticket AUTH, não altere às pressas monitores de produção durante um lote.

Quando alguém pede uma nova regra no monitor durante um lote, Lena a registra no backlog com um ticket de autorização e a avalia depois da janela. Mudar um monitor de produção no meio de um lote arrisca uma parada ou um defeito de falha aberta que ninguém testou. O item do backlog nomeia quem pediu, por que e quando será revisto, para que o pedido não se perca e quem o levantou veja que foi tratado.

### Nota prática

Os testes de aceitação levam o nome dos ids dos requisitos e reprovam a integração contínua quando pulados. Requisitos Must órfãos são testados ou formalmente adiados, com um dono executivo.

### 21.1b MoSCoW sob segurança física

A priorização Must/Should/Could ainda põe todos os requisitos de segurança física em Must. Um Could que enfraquece um Must (negação opcional de códigos de escrita) é reclassificado ou rejeitado. Gerentes de produto não derrotam no voto a falha fechada. Os campos de log também levam o id do requisito (req=S-1), para que um evento de negação possa ser rastreado até o requisito que ele impõe.

Na ABP, o S-1 e o R-12 são ambos itens Must, e nenhuma decisão de produto pode rebaixá-los. Um pedido para tornar opcionais, por conveniência, as negações de códigos de escrita foi rejeitado com base nisso, e a rejeição é registrada com o requisito que teria enfraquecido.

### Exercícios

- **EX061 — Levantamento.** Escreva um requisito funcional e um de segurança física com "deverá" a partir de "o escritório não pode alcançar o SIS". Rubrica: 3 = ambos testáveis; 2 = um; 1 = vago; 0 = nada.
- **EX062 — Aceitação.** Dado/Quando/Então para a falha fechada com a lista de permissões ausente. Rubrica: 3 = completo, com negação/alarme esperados; 2 = parcial; 1 = ideia; 0 = nada.
- **EX063 — Conflito.** Visualização do L4 para o L2 por conveniência versus zoneamento — registre o conflito e a regra escolhida. Rubrica: 3 = conflito nomeado + regra com a segurança primeiro, via DMZ; 2 = só a regra; 1 = escolhe a conveniência; 0 = nada.

### Síntese

Os requisitos vêm das pessoas, se dividem em famílias e são entregues com testes de aceitação sobre dados de teste sintéticos.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue estudando — capítulo 21 de 50

[← Capítulo 20](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Segurança de TO, IoT e sistemas ciberfísicos: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) desenhar um modelo de entidades para ativos, zonas, condutos e constatações; (2) escolher chaves e cardinalidades; (3) manter o conteúdo de exploits fora do modelo.

### 22.1 Entidades

Plant 1—* Unit; Unit 1—* Asset; Zone 1—* Asset; Conduit *—* Zone (de/para); Finding *—* EvidenceObject (por hash); TechniqueTag *—* Finding. Erros de cardinalidade (vários conjuntos de condutos ativos sem um ponteiro de versão) fazem os auditores perguntarem quais regras estavam em vigor.

O modelo de Lena dá a cada ConduitSet uma versão e registra qual versão estava em vigor em cada momento, para que um auditor veja as regras que valiam num dado dia. Cada Finding se liga à sua evidência por hash, e as tags de técnica se ligam às constatações apenas depois de revisadas.

### 22.2 Chaves

Os ids das constatações são UUID. A evidência é endereçada pelo conteúdo, via SHA-256. O ConduitSet tem (plant_id, version_int). Nunca use o título como chave das constatações — os títulos mudam.

O esquema de Lena usa essas chaves em todo o CNHP. Uma constatação sobre a FW-12 manteve o seu identificador quando o título foi reescrito depois da revisão, e o seu histórico ficou intacto. Uma evidência com o hash como chave não pode ser trocada em silêncio, já que um arquivo diferente teria uma chave diferente. O número de versão do ConduitSet aumenta a cada mudança publicada e nunca reutiliza um valor antigo.

### 22.3 Atributos proibidos

Nenhum atributo para payload, shellcode ou ataque passo a passo. O EvidenceObject guarda os bytes num bucket lacrado; o modelo guarda apenas o hash, o tipo de mídia e a classe de retenção.

> **Caso sintético — Ashford Batch Plant.** Um esquema inicial tinha notas em texto livre; as pessoas colavam senhas de engenharia. Lena o substituiu por campos estruturados mais um hash de evidência, e um linter rejeita textos com cara de senha nos títulos.

O linter de Lena impõe a lista. Ele roda em todo registro criado ou importado, inclusive nas importações em massa de scanners, e rejeita textos com cara de senha nos títulos. Os registros rejeitados retornam um erro que explica qual campo foi recusado.

### 22.4 Erros e limites

Modelos que tornam toda técnica do ATT&CK for ICS um campo obrigatório geram tags lixo. Mantenha as tags de técnica opcionais e revisadas.

Na ABP, as tags de técnica são acrescentadas por um analista depois que a constatação é escrita, e uma segunda pessoa as revisa. Uma constatação sem técnica adequada fica sem tag, em vez de ser forçada para a mais próxima. Isso mantém os números de cobertura honestos, porque uma tag lixo contaria como cobertura observada de uma técnica que ninguém testou de fato. As tags são revistas quando a versão do ATT&CK for ICS muda.

### Nota prática

Faça exclusão lógica das constatações, com ator e motivo; expurgo definitivo apenas por rotinas de retenção que emitam eventos de auditoria. Um DELETE FROM findings silencioso é um presente para o repúdio.

### 22.1b Limites de anexos e tempo

Os objetos de evidência precisam de limites de tamanho e de listas de permissões de tipos de mídia. Uploads sem limite viram ataques de disponibilidade e tentam a despejar dados proprietários em massa. Toda entidade mutável precisa de created_at, created_by e, para mudanças de estado, updated_at/updated_by ou um evento somente de acréscimo. Prefira UTC com deslocamentos explícitos nas exportações.

As exportações declaram o seu fuso horário uma vez no cabeçalho do arquivo, além de em cada timestamp. Clientes de API que emitem DELETE em laço durante uma nova tentativa defeituosa têm as credenciais revogadas depois de um limite.

### 22.5 Exemplo resolvido — modelando uma constatação sem vazar a planta (ABP sintética)

O modelo de dados de Lena para as constatações do CNHP tem as entidades Asset, Zone, Conduit, Finding e Evidence. Uma Finding referencia um Asset por chave, nunca embute o seu endereço IP nem credenciais, e guarda a evidência como um hash mais um ponteiro para o repositório controlado de evidências. A lista de atributos proibidos (senhas, payloads completos de pacotes, valores de receitas) é imposta por uma verificação de esquema que rejeita qualquer registro que contenha esses campos. Quando uma constatação sobre a porta Modbus aberta do PLC-A é exportada para a gerência, ela diz "Asset PLC-A, Conduit L2→L1, ATT&CK for ICS T0869 Standard Application Layer Protocol, severidade alta" — o suficiente para agir, não o suficiente para atacar.

### Exercícios

- **EX064 — Cardinalidade.** Por que o ConduitSet é versionado em vez de editado no lugar? Rubrica: 3 = auditoria do que estava autorizado e quando; 2 = versionamento vago; 1 = boa prática; 0 = nada.
- **EX065 — Chave.** Por que endereçar a evidência pelo conteúdo? Rubrica: 3 = integridade + deduplicação + evidência de adulteração; 2 = uma razão; 1 = vago; 0 = nada.
- **EX066 — Proibido.** Validação que impede senhas no título. Rubrica: 3 = heurística/linter + processo; 2 = um; 1 = vago; 0 = nada.

### Síntese

Modele ativos, zonas, versões, constatações e hashes — não ataques.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue estudando — capítulo 22 de 50

[← Capítulo 21](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Segurança de TO, IoT e sistemas ciberfísicos: análise de ameaças e de falhas

### Objetivos de aprendizagem

Você vai (1) enumerar as falhas do próprio programa de segurança de TO; (2) usar uma passada leve de STRIDE sobre as ferramentas; (3) alimentar os requisitos com os resultados sem construir módulos de exploit.

### 23.1 O programa pode falhar de forma perigosa

Listas de permissões que falham abertas, verificação de alcançabilidade pulada na integração contínua, detectores com tempestades silenciosas de alarmes falsos, adiamentos de correções sem data — isso ameaça a segurança de processo e a honestidade, não só a confidencialidade de uma ferramenta.

Lena lista essas falhas primeiro na análise de ameaças do CNHP, porque elas poderiam ferir a planta pelas mesmas ferramentas feitas para protegê-la. Um monitor que falha aberto deixaria escritas não autorizadas chegarem ao PLC-A enquanto todos acreditavam que estavam bloqueadas. Uma verificação de alcançabilidade pulada na integração contínua deixaria um novo conduto para o SIS-B ser integrado sem ser visto. Cada falha recebe um requisito e um teste.

### 23.2 STRIDE sobre as ferramentas do CNHP

Falsificação (spoofing): conta de engenharia falsa. Adulteração: editar a exportação do firewall depois do lacre. Repúdio: nenhum ator nos eventos de negação. Divulgação de informação: réplica do historiador legível por todos. Negação de serviço: um scanner inunda um tronco. Elevação: uma única pessoa consegue publicar um conduto para o SIS. Cada linha recebe um requisito de mitigação.

Lena roda a análise em cada ferramenta do CNHP e registra as linhas no backlog com donos. Para a ABP, as linhas mais graves foram o monitor falhando aberto e uma única pessoa publicando um conduto para o SIS-B; elas viraram o requisito S-1 e a condição de dupla aprovação nas mudanças de condutos. Cada linha é revista de novo quando a sua mitigação é entregue.

### 23.3 As ameaças à planta ficam na análise de perigos

As ameaças ao processo pertencem à análise de perigos do processo da planta e ao HAZOP informado por cibersegurança, não a funcionalidades de uma ferramenta de estudante. Não construa exploração automatizada para satisfazer uma linha do STRIDE.

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

> **Caso sintético — Ashford Batch Plant.** A linha do STRIDE "falha aberta" virou o requisito de segurança física S-1. A linha "publicação solitária de conduto" virou a condição de dupla aprovação.

Lena repassa as ameaças à planta ao engenheiro de segurança de processo para a análise de perigos. Ela fornece fatos sobre as ferramentas e a rede, como quais zonas alcançam o PLC-A, e o engenheiro julga as consequências para o processo. Nada nas ferramentas do CNHP simula um ataque ao processo.

### 23.4 Erros e limites

O STRIDE é um estímulo, não uma prova. Revise-o ao acrescentar uma nova fronteira de confiança (por exemplo, um historiador SaaS de um fornecedor).

Lena repete a análise sempre que o CNHP acrescenta uma fronteira de confiança, como um novo caminho de acesso remoto para um fornecedor ou uma mudança no destino dos alertas. As linhas das revisões anteriores são mantidas, para que a equipe veja quais ameaças foram acrescentadas, quais mitigações foram construídas e quais continuam abertas. Uma tabela STRIDE nunca prova que uma ferramenta é segura; os testes e as revisões é que fazem isso.

### Nota prática

Inclua no modelo o comprometimento do host de salto: credenciais de curta duração, listas de permissões de saída, revogação rápida. Se a resposta for apenas confiar no host de salto, a análise está incompleta.

### 23.1b Abuso versus mau uso e backlog

Casos de abuso são ações intencionais de um adversário contra as ferramentas do CNHP. Casos de mau uso são operadores honestos cometendo erros perigosos (colar um CIDR que inclui um parceiro). Projete controles para os dois. As linhas do STRIDE viram issues com ligações para os requisitos. As linhas de mau uso costumam virar regras de validação; as de abuso costumam virar controles de acesso.

Alimentar o backlog significa que cada linha do STRIDE tem um dono e um prazo. Na ABP, o caso de mau uso de um engenheiro colando o CIDR de um parceiro no arquivo de condutos virou uma regra de validação que rejeita faixas fora do plano de endereçamento da planta.

Os dois tipos alimentam o backlog.

### Exercícios

- **EX067 — Falha aberta.** Um teste que prove a falha fechada. Rubrica: 3 = remover a política, esperar negação+alerta; 2 = ideia; 1 = vago; 0 = nada.
- **EX068 — STRIDE.** Mitigação do repúdio nos eventos de negação. Rubrica: 3 = ator autenticado + log imutável; 2 = só logging; 1 = vago; 0 = nada.
- **EX069 — Fronteira.** Por que o STRIDE do programa não justifica um módulo de exploit? Rubrica: 3 = objetivo diferente/fronteira de segurança; 2 = parcial; 1 = justifica; 0 = nada.

### Síntese

Analise como o seu programa pode ferir a planta ou mentir; mitigue isso primeiro.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue estudando — capítulo 23 de 50

[← Capítulo 22](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Segurança de TO, IoT e sistemas ciberfísicos: métodos I

### Objetivos de aprendizagem

Você vai (1) encadear permissão de trabalho, descoberta, validação e relato; (2) escolher métodos que correspondam à autorização e ao risco de processo; (3) definir quando um método está concluído sem escrever num CLP.

### 24.1 Sequência

Primeiro a permissão de trabalho. A descoberta enumera ativos e condutos pelos métodos acordados. A validação confirma problemas de configuração com o menor privilégio. O relato entrega as constatações e os hashes das evidências. Pular a permissão é como acontecem os testes não autorizados.

Na ABP, toda atividade do CNHP começa com uma permissão de trabalho assinada que nomeia unidades, métodos, janelas e condições de parada. A descoberta usa captura passiva e exportações de projetos de engenharia; a validação usa revisão de configuração e testes de bancada. As constatações são relatadas com os hashes das evidências, e nada passa para a etapa seguinte até que a anterior tenha produzido os seus artefatos.

### 24.2 Fichas de método

Cada ficha: nome, propósito, privilégio, ruidoso?, impacto no processo, condições de parada, artefatos. A revisão de configuração autenticada é uma ficha; um exploit de CLP armado não está no baralho deste programa.

Lena mantém as fichas de método da ABP no repositório, ao lado do modelo de permissão de trabalho. Uma permissão só pode listar métodos que tenham ficha, e cada ficha declara se o método é ruidoso e que impacto no processo ele poderia ter. Os revisores conferem as condições de parada da ficha contra a permissão, para que um método não possa ser usado sob condições mais fracas do que as que a sua ficha exige.

### 24.3 Concluído significa artefatos

Um método está concluído quando existem o CSV de inventário, os hashes de configuração, os rascunhos de constatações e as atualizações de cobertura — não quando alguém se sente terminado.

> **Caso sintético — Ashford Batch Plant.** A ficha do método de verificação da lista de permissões serial exige modo somente de escuta, parada por tempo de ciclo em 50 ms e uma tabela de decisões no estilo do laboratório como artefato.

O checklist de Lena para cada método lista os artefatos exigidos. Para a verificação da lista de permissões serial na ABP, isso significa a tabela de decisões, o hash da captura, eventuais rascunhos de constatações e o painel de cobertura atualizado. Um método com artefatos faltando é reaberto, não encerrado com uma nota prometendo-os para depois. Lena confere a lista no fim de cada janela.

### 24.4 Erros e limites

Copiar a lista de métodos de outra pessoa sem a autorização correspondente é 62443 de culto à carga.

Uma lista de métodos copiada de outra planta ou de um guia publicado pode pressupor autorizações, equipamentos ou tolerâncias de processo que a ABP não tem. Lena adapta cada método à permissão da própria ABP, escreve uma ficha para ele e faz a ficha ser revisada pela engenharia de controle antes do uso. Um método emprestado sem essa revisão é tratado como não autorizado, por mais respeitável que seja a fonte, e fica fora da permissão até ser revisado.

### Nota prática

Congele os métodos durante uma janela do mesmo modo que congela os condutos: métodos novos precisam do caminho AUTH, e não de um "já que estávamos aqui, também tentamos".

### 24.1b Silenciosos versus ruidosos e dependências

Os métodos silenciosos (decodificação somente de escuta, exportação de configuração) cabem em mais janelas. Os métodos ruidosos precisam de limites de taxa mais apertados e, muitas vezes, de horários fora do pico. Codifique as dependências entre métodos no plano, para que as revisões não sejam agendadas contra uma lista de ativos vazia. O plano de Lena lista, para cada método, os métodos anteriores de cujos artefatos ele precisa.

Fichas de método sem o campo "ruidoso" são o motivo de as janelas de lote da manhã ficarem congestionadas. Os métodos ruidosos são reservados contra o cronograma de lotes com uma semana de antecedência, para que o líder de turno saiba quando esperar tráfego extra.

Lena agenda os métodos silenciosos primeiro.

### Nota de campo — o congelamento de métodos na prática

Durante a janela W-17 da ABP, um fornecedor pediu para testar uma função de diagnóstico extra no meio do turno. Lena estacionou o pedido no backlog de planejamento do trabalho seguinte e manteve a ficha de método congelada. O lote terminou sem tráfego inexplicado, e o diagnóstico foi avaliado no mês seguinte, sob uma nova permissão de trabalho com as suas próprias condições de parada.

### Exercícios

- **EX070 — Ficha.** Escreva uma ficha de método para a decodificação Modbus somente de escuta. Rubrica: 3 = todos os campos preenchidos com segurança; 2 = falta um; 1 = inclui escritas/exploits; 0 = nada.
- **EX071 — Sequência.** O que há de errado na descoberta antes de uma permissão de trabalho assinada? Rubrica: 3 = teste não autorizado; 2 = processo vago; 1 = ordem ruim; 0 = nada.
- **EX072 — Concluído.** Liste quatro artefatos que encerram um método de revisão de zoneamento. Rubrica: 3 = quatro concretos; 2 = dois; 1 = um; 0 = nada.

### Síntese

Os métodos são autorizados, têm ficha e estão concluídos quando os artefatos existem.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue estudando — capítulo 24 de 50

[← Capítulo 23](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) esboçar o pipeline de permitir/negar do monitor serial da ABP; (2) justificar os trade-offs numa breve revisão de projeto; (3) produzir um registro de decisão de uma página.

### 25.1 Problema do ateliê

Projeto: quadro de entrada para decodificação para carga do ConduitSet/lista de permissões para avaliação de permit() para emissão de evento para encaminhar ou descartar. Opções: política embutida no código versus arquivo de dados assinado; alertas síncronos versus assíncronos nas negações.

A equipe de ateliê de Lena na ABP esboça o caminho inteiro numa página e marca onde um quadro é negado se a política estiver ausente. As duas escolhas debatidas foram se a lista de permissões fica no código ou num arquivo de dados assinado, e se os alertas de negação são enviados de forma síncrona ou enfileirados. Cada opção é escrita com as suas consequências antes que alguém defenda uma delas.

### 25.2 Trade-offs

A política como dados assinados permite publicar atualizações sem reimplantar o firmware, mas exige verificação de assinatura e falha fechada em assinaturas ruins. Os alertas assíncronos escalam, mas podem chegar fora de ordem; para as negações no caminho do SIS, prefira o alerta síncrono.

A equipe de Lena concorda que uma assinatura ruim precisa parar todo o tráfego não essencial, exatamente como o requisito S-1 exige para uma política ausente. Os alertas síncronos ficam para as negações de códigos de escrita e para os caminhos ligados ao SIS, onde o atraso importa; as negações rotineiras de leitura são enfileiradas. A equipe também registra o que acontece se a chave de assinatura for perdida: o monitor mantém a última lista válida e alarma, e nenhuma atualização sem assinatura é aceita.

### 25.3 Registro de decisão

Uma página: contexto, opções, decisão, consequências, data, donos. Guarde ao lado do código.

> **Caso sintético — Ashford Batch Plant.** O ateliê escolheu listas de permissões em JSON assinado, caminho síncrono para as negações que tocam códigos de escrita e lote assíncrono para as leituras rotineiras. O ADR-004 registra isso.

O ADR-004 registra nesse formato a decisão do ateliê sobre as listas de permissões em JSON assinado, com Lena e o líder da engenharia de controle como donos. Ele fica no repositório ao lado do código da política, para que qualquer pessoa que mude o carregador possa ler por que ele funciona do jeito que funciona.

### 25.4 Erros e limites

Ateliês que pulam os requisitos de segurança física produzem diagramas bonitos que falham abertos.

O ateliê de Lena se recusa a revisar um projeto até que ele mostre onde o monitor nega o tráfego quando a lista de permissões está ausente ou a sua assinatura falha. Os projetos que não conseguem responder voltam antes de qualquer discussão de layout ou ferramentas. Os cartões de restrição deixam os requisitos de segurança física visíveis na mesa desde o primeiro minuto, para que não sejam esquecidos no entusiasmo por uma arquitetura engenhosa. Os projetos rejeitados também são registrados.

### Nota prática

Os facilitadores pausam a sala com: Onde negamos se a política estiver ausente? Se ninguém souber responder, a arquitetura não está pronta.

### 25.1b Cartões de restrição e galeria

Entregue a cada equipe do ateliê cartões de restrição: residência dos dados, operação por dois engenheiros, falha fechada, nada de pontuações vazias, independência do SIS. Projetos que violam um cartão são rejeitados antes do debate estético. Os ateliês terminam com uma galeria: as equipes expõem os rascunhos de ADR, e as outras tentam achar um caminho de falha aberta em cinco minutos.

Um esboço de ateliê precisa nomear por escrito as fronteiras de confiança, os repositórios de dados e o caminho de falha fechada. Dez minutos rotulando valem mais do que uma hora de layout estético. Os caminhos de falha aberta encontrados na galeria são escritos no ADR antes de ele ser aceito.

### Nota de campo — rotular antes do layout

As equipes de ateliê que passaram os primeiros vinte minutos nomeando os pontos de negação e as fronteiras de confiança produziram ADRs que sobreviveram à revisão. As equipes que começaram pelas paletas de cores redescobriram caminhos de falha aberta durante a galeria. O CNHP agora exige um caminho de falha fechada rotulado na fotografia do quadro branco anexada a todo ADR.

### Exercícios

- **EX073 — Opções.** Duas opções de entrega da política e um risco de cada. Rubrica: 3 = duas + riscos; 2 = opções; 1 = uma; 0 = nada.
- **EX074 — ADR.** Linha de decisão para os alertas síncronos de negação em códigos de escrita. Rubrica: 3 = decisão clara + porquê; 2 = só a decisão; 1 = vago; 0 = nada.
- **EX075 — Revisão.** Três perguntas que um revisor precisa fazer. Rubrica: 3 = falha fechada, autenticação da política, orçamento de latência; 2 = duas; 1 = uma; 0 = nada.

### Síntese

O trabalho de ateliê termina numa decisão registrada, não numa impressão.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue estudando — capítulo 25 de 50

[← Capítulo 24](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Segurança de TO, IoT e sistemas ciberfísicos: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar monitores locais com analytics em nuvem para dados de TO; (2) avaliá-los frente às restrições de residência dos dados e de segurança de processo; (3) escolher uma alternativa rejeitando as outras de forma explícita.

### 26.1 Alternativas

A: monitores seriais/IP locais com detectores locais. B: coleta local com analytics no historiador do site. C: SaaS de analytics em nuvem recebendo valores de processo. Cada uma atende a restrições diferentes.

Lena descreve cada opção para a ABP com a mesma estrutura: para onde vão os dados de processo, quem a opera, como ela falha e quanto custa. A opção C enviaria valores de processo para fora do site, o que levanta de imediato questões de residência dos dados e de confidencialidade das receitas. As opções A e B mantêm os dados no site, mas diferem na rapidez com que conseguem impor decisões no caminho de escrita.

### 26.2 Critérios

Independência da segurança de processo, residência dos dados, comportamento de falha fechada, operabilidade pela equipe do site, custo. Dê mais peso à segurança física e à residência do que à novidade.

Lena acorda os pesos com o engenheiro de segurança de processo e com o gerente da planta antes de pontuar. A independência da segurança física e a residência dos dados têm o maior peso, porque uma falha ali não pode ser desfeita por correções posteriores. Cada opção é pontuada com evidências, e as opções que reprovam num critério de segurança física são rejeitadas, quaisquer que sejam as suas outras notas. Os pesos são publicados na análise, para que os revisores possam contestá-los.

### 26.3 Decisão

A ABP rejeitou a C porque as tendências próximas às receitas não podem sair do site sem uma exceção no nível do conselho. Escolheu a A para a imposição no caminho de escrita, com a B para a pesquisa de detecção de prazo mais longo sobre réplicas.

> **Caso sintético — Ashford Batch Plant.** Uma demonstração da C por um fornecedor parecia caprichada; o jurídico e a segurança de processo bloquearam o upload irrestrito. O ADR-011 registra a rejeição.

O ADR-011 registra essa decisão. As razões são curtas: a opção A impõe as decisões localmente no caminho de escrita e pode ser operada pelos engenheiros do site; a opção B acrescenta pesquisa de detecção, mas exige competências que o turno da noite não tem, então fica para o trabalho diurno sobre réplicas. A opção C continua rejeitada até que as regras de residência mudem, que é o seu gatilho de revisão registrado.

### 26.4 Erros e limites

Uma análise de alternativas que ignora as cláusulas de dados da permissão de trabalho é teatro.

Na ABP, as cláusulas de dados da permissão proíbem que valores de processo saiam do site sem uma exceção no nível do conselho, então a opção C reprovou antes de qualquer comparação técnica. Lena registra essa restrição no topo da análise, para que os leitores vejam por que a C foi rejeitada sem ler a pontuação. Uma análise que tivesse dado nota alta à C ignorando a permissão teria desperdiçado o tempo do conselho e poderia ter pressionado alguém a conceder uma exceção.

### Nota prática

Documente as competências que cada alternativa exige. Um pipeline em nuvem que ninguém no site consegue operar falha aberto socialmente, mesmo que falhe fechado tecnicamente.

### 26.1b Custo, competências e gatilhos de revisão

Inclua o custo anual aproximado e as competências que cada alternativa exige. Uma opção que precisa de seis pessoas em tempo integral para operar com falha fechada não é gratuita. Termine a análise de alternativas com uma decisão, as opções rejeitadas com as razões e um gatilho de revisão (reabrir se a lei de residência mudar).

Os custos de troca importam: um monólito que já exporta listas de permissões assinadas pode crescer para serviços; um contrato de SaaS com exceções de residência é mais difícil de desfazer no meio de um incidente. Prefira opções que mantenham uma saída de emergência offline para negar/permitir.

O ADR-011 declara o seu gatilho de revisão.

### Nota de campo — pressupostos de competência

O caminho de analytics da opção B pressupunha um engenheiro do site que entendesse a ordenação de eventos. A ABP não tinha essa pessoa à noite. Até que as contratações chegassem, Lena manteve a imposição no caminho de escrita na opção A e limitou a B à pesquisa diurna sobre réplicas. Uma arquitetura que pressupõe competências indisponíveis falha aberta socialmente.

### Exercícios

- **EX076 — Critério.** Acrescente um critério para os dados do SIS e pontue A/B/C. Rubrica: 3 = critério sensato + notas; 2 = critério; 1 = vago; 0 = nada.
- **EX077 — Rejeitar a C.** Frase de rejeição com razão de residência/segurança física. Rubrica: 3 = clara; 2 = parcial; 1 = só custo; 0 = aceita a C.
- **EX078 — Contingência.** Quando a A puramente local é o ambiente de execução certo? Rubrica: 3 = queda da WAN / exercício de isolamento; 2 = vago; 1 = sempre; 0 = nunca.

### Síntese

Escolha a arquitetura frente a restrições ponderadas; registre as opções rejeitadas.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue estudando — capítulo 26 de 50

[← Capítulo 25](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Segurança de TO, IoT e sistemas ciberfísicos: projeto de controles

### Objetivos de aprendizagem

Você vai (1) projetar controles preventivos, detectivos e corretivos para o CNHP; (2) ligar os controles aos requisitos; (3) evitar controles que exijam competências de exploit para serem operados.

### 27.1 Três tipos

Preventivo: lista de permissões antes do encaminhamento. Detectivo: alerta sobre códigos de escrita negados. Corretivo: desativar automaticamente uma conta de engenharia comprometida no fim da janela. Cada um corresponde a um id de requisito.

Na ABP, a lista de permissões no monitor serial é preventiva, o alerta quando a HMI-1 tenta escrever fora de 40001 a 40010 é detectivo, e a desativação das contas temporárias de engenharia no fim de cada janela é corretiva. Lena registra o id do requisito ao lado de cada controle, para que um revisor veja qual requisito falha se o controle for removido ou enfraquecido.

### 27.2 Competência do operador

Os controles precisam ser operáveis por engenheiros que seguem runbooks — não só por especialistas em exploits. Um controle que exige shellcode sob medida para ser verificado é o controle errado para este programa.

Lena escreve uma entrada de runbook para cada controle do CNHP, descrevendo como verificá-lo com ferramentas comuns, como reproduzir um quadro sintético na bancada e ler o log de decisões. Se um controle só pode ser verificado por alguém escrevendo código de exploit, ela o substitui por um que possa ser conferido com segurança pelos próprios engenheiros do site no trabalho de rotina.

### 27.3 Compensação

Se um CLP legado não consegue impor listas de permissões, acrescente monitoramento detectivo e uma aprovação humana mais rígida para o acesso de engenharia. Documente a compensação na permissão de trabalho.

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

> **Caso sintético — Ashford Batch Plant.** Escritas fora de 40001-40010 são negadas — uma barreira preventiva com um evento detectivo quando alguém tenta.

Na ABP, a compensação é escrita na permissão de trabalho com um dono e uma data de revisão, para que seja conferida, e não presumida. Para um CLP legado que não consegue impor uma lista de permissões, Lena combina monitoramento detectivo no seu tronco com aprovação por duas pessoas para o acesso de engenharia.

### 27.4 Erros e limites

Pilhas de controles compensatórios sem dono viram alertas ignorados.

O registro de controles de Lena lista cada controle compensatório da ABP com o seu dono, os seus alertas e a data do último teste. Um controle encontrado sem dono recebe um antes da janela seguinte, ou é retirado do registro e o seu requisito é marcado como não atendido. Controles que ninguém observa são contados como ausentes, porque os seus alertas serão ignorados quando finalmente dispararem. A titularidade é revista em cada dia de saúde.

### Nota prática

Programe um dia trimestral de saúde dos controles: quebre cada controle preventivo num laboratório sintético e confirme que os controles detectivos disparam. Controles não testados são desejos.

### 27.1b Titularidade e detecção da quebra de vidro

Todo controle tem um dono que recebe os seus alertas e uma data de revisão. Registre quando um operador usa a quebra de vidro para pular a dupla aprovação. Uma quebra de vidro sem detecção é só um controle único escondido. A revisão semanal dos eventos de quebra de vidro faz parte do projeto do controle, e cada revisão nomeia quem usou a quebra de vidro e o motivo informado.

A entrada de cada controle no registro também declara como ele falha: se uma lista de permissões quebrada bloqueia ou deixa passar o tráfego decide qual alerta detectivo precisa disparar primeiro e quem é acionado quando ele dispara.

### Nota de campo — dia de saúde dos controles

No dia de saúde de março, a equipe apagou a lista de permissões de um monitor de bancada e confirmou que o alerta detectivo disparou em 12 segundos. O caminho preventivo negou as escritas imediatamente. Um controle compensatório de um CLP legado não tinha dono; recebeu um antes da janela seguinte.

### Exercícios

- **EX079 — Mapa.** Um controle preventivo e um detectivo contra a adulteração de evidências. Rubrica: 3 = os dois; 2 = um; 1 = vago; 0 = nada.
- **EX080 — Operável.** Por que "verificar explorando de novo" é um controle ruim? Rubrica: 3 = uso dual + instável + competência errada; 2 = uma razão; 1 = vago; 0 = defende.
- **EX081 — Laboratório.** Qual regra bloqueia HIST-1 fc=16? Rubrica: 3 = fc-not-allowed; 2 = negação vaga; 1 = errada; 0 = nada.

### Síntese

Os controles são preventivos/detectivos/corretivos, têm dono e são operáveis sem exploits.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue estudando — capítulo 27 de 50

[← Capítulo 26](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Segurança de TO, IoT e sistemas ciberfísicos: implementação I

### Objetivos de aprendizagem

Você vai (1) implementar permit() com códigos de motivo explícitos; (2) acrescentar testes para cada cláusula; (3) registrar logs sem armazenar segredos.

### 28.1 Forma da implementação

Função pura: entradas origem, código de função, registrador e AllowListVersion, saída (allow: bool, reason: str). Nenhuma E/S de rede dentro do predicado. Isso mantém os testes rápidos e livres de contato com a planta.

A função permit de Lena na ABP segue exatamente essa forma: recebe os campos do quadro decodificado e a versão da lista de permissões e devolve uma decisão com um motivo. A carga da lista de permissões e a escrita dos logs acontecem fora da função, então os seus testes rodam em milissegundos sobre dados sintéticos e nunca arriscam contato com a planta.

### 28.2 Testes por cláusula

Um arquivo de teste por cláusula: permissão da estação, código de função, faixa de registradores, política indisponível. Apenas dados de teste sintéticos. Mutação: quebre uma cláusula e veja o teste falhar.

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

Lena mantém um arquivo de teste por cláusula para a função permit da ABP, com os dados de teste nomeados pelo requisito que conferem. Os testes de mutação confirmaram que cada arquivo falha quando a sua cláusula é quebrada: apagar a verificação da faixa de registradores, por exemplo, fez os testes de fora da faixa falharem na hora. Uma cláusula cujos testes sobrevivem a uma mutação é tratada como não testada.

### 28.3 Logging

Registre a decisão, o motivo, a versão da política e o ator. Não registre senhas nem payloads completos de quadros que possam conter dados proprietários de receitas. Redija o que for necessário.

> **Caso sintético — Ashford Batch Plant.** A implementação I entregou códigos de motivo que a interface de linha do tempo mostra — os operadores finalmente viram por que uma escrita foi bloqueada às 03:12.

Os logs de Lena mostram qual versão da política tomou cada decisão. Os payloads dos quadros ficam de fora porque podem conter valores de receitas. Lena confere uma amostra dos logs depois de cada versão, para confirmar que nada sensível escapou.

### 28.4 Erros e limites

Motivos em texto livre derivam; use um enum compartilhado com o painel de cobertura.

A implementação de Lena usa uma lista compartilhada de códigos de motivo, como register-out-of-range e policy-unavailable, publicada como documento versionado. O painel de cobertura e a visão de linha do tempo leem a mesma lista, então um código novo não pode aparecer nos logs sem ser entendido nos outros lugares. Os consumidores que veem um código desconhecido o tratam como negação e geram um alerta para o dono da ferramenta. O documento é revisto a cada mudança do predicado.

### Nota prática

Faça fuzzing do predicado com estações, códigos e UTF-8 quebrado aleatórios. Ele precisa negar (DENY) ou dar erro de forma fechada, nunca permitir (ALLOW) numa falha de parsing.

### 28.1b Catálogo de motivos e fuzzing

O catálogo lista, para cada código de motivo, a cláusula que o emite e o teste que o fixa: fc-not-allowed, register-out-of-range, policy-unavailable, station-unknown. As entradas de fuzzing que um dia encontraram um defeito entram numa lista de regressão reproduzida em cada versão, com a semente que as produziu.

As listas de verificação da revisão de código para mudanças no predicado incluem: nova cláusula, novos testes, documentação dos códigos de motivo, caso de fuzzing, falha fechada em erro de parsing. Revisores que pulam a lista estão fazendo revisão social, não revisão de segurança.

A lista de verificação de Lena é anexada a toda revisão do predicado.

### Nota de campo — achados do fuzzing

Um harness de fuzzing de cinco minutos lançou um nome de estação em UTF-8 que antes fazia o decodificador cair numa exceção não tratada — que o chamador tratava como ALLOW. A correção passou a retornar DENY parse-error, e o harness agora roda na integração contínua a cada mudança do predicado.

### 28.5 Exemplo resolvido — um teste de cláusula que pegou um defeito real (ABP sintética)

Cada cláusula da função permit tem o seu próprio teste: origem permitida, código de função permitido, registrador na faixa, negação por padrão. O harness de fuzzing de Lena então alimenta 10.000 triplas aleatórias (origem, função, registrador), tiradas de um gerador com semente, e afirma que todo PASS satisfaz todas as cláusulas. Na primeira execução, ele descobriu que o código de função 23 (leitura/escrita de múltiplos registradores) passava para a HMI-1, porque a implementação verificava apenas a metade de leitura do pedido. A correção rejeita o 23 a menos que ele esteja listado explicitamente, um teste de cláusula agora o fixa, e a nota do incidente registra qual semente reproduziu a falha, para que qualquer pessoa possa rodá-la de novo.

### Exercícios

- **EX082 — Assinatura.** Assinatura de tipos de permit e por que AllowListVersion é um argumento. Rubrica: 3 = assinatura + razão da fixação da versão; 2 = assinatura; 1 = vago; 0 = nada.
- **EX083 — Mutação.** Qual teste falha se a faixa de registradores for ignorada? Rubrica: 3 = 40050 espera BLOCK; 2 = vago; 1 = errado; 0 = nada.
- **EX084 — Redação.** Dois campos de log a redigir. Rubrica: 3 = por exemplo, senhas, payloads completos com receitas; 2 = um; 1 = vago; 0 = nada.

### Síntese

Predicado puro, testes por cláusula, logs seguros.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue estudando — capítulo 28 de 50

[← Capítulo 27](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Segurança de TO, IoT e sistemas ciberfísicos: medição

### Objetivos de aprendizagem

Você vai (1) definir a cobertura com um denominador; (2) separar as métricas de atividade das métricas de resultado; (3) avaliar detectores por classe de ataque e com intervalos (lições de Urbina/Giraldo).

### 29.1 A cobertura precisa de um plano

A cobertura do ATT&CK for ICS é o observado intersectado com o planejado sobre o planejado, não o observado sobre todas as técnicas. Sem um plano, a cobertura é vaidade.

Na ABP, Lena escreve o plano das técnicas a testar antes de cada avaliação, e o painel de cobertura conta apenas essas. As técnicas observadas fora do plano são relatadas à parte. O número de 31 das 44 técnicas planejadas observadas significa algo porque as 44 foram escolhidas antecipadamente e o guia de planejamento é publicado com o painel. O plano é fixado antes dos testes.

### 29.2 Atividade versus resultado

Atividade: quadros decodificados, ferramentas executadas. Resultado: remediações verificadas, alcançabilidade do SIS ainda falsa, taxa de alarmes falsos na taxa de base da planta. Conduza pelos resultados.

O relatório mensal do CNHP feito por Lena começa pelos resultados: remediações verificadas por novo teste, se o SIS-B continua inalcançável a partir do L4 e a taxa de alarmes falsos do detector na taxa de base da ABP. As contagens de atividade, como quadros decodificados, aparecem apenas num apêndice de capacidade. Conduzir pela atividade premiaria rodar mais ferramentas, e não corrigir mais problemas. Os resultados são o que o gerente da planta financia.

### 29.3 Honestidade dos detectores

Relate os intervalos de alarmes falsos, o atraso de detecção e a classe de ataque. Um detector de banda que perde ataques furtivos sobre o resíduo não equivale a um CUSUM que os pega — o laboratório torna isso visível.

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

> **Caso sintético — Ashford Batch Plant.** O CNHP relata a cobertura das técnicas planejadas e os alarmes falsos/atraso dos detectores por classe — não um único "percentual seguro".

O relatório piloto de Lena para a ABP lista os resultados por classe de ataque. Cada classe tem o seu próprio intervalo de alarmes falsos e o seu atraso médio, para que um leitor veja que o CUSUM pegou os ataques furtivos sobre o resíduo que o detector de banda perdeu.

### 29.4 Erros e limites

Denominadores tirados de outra planta invalidam a métrica. Ataques sintéticos não são o adversário.

Lena nunca toma emprestado um denominador do plano de outro site, porque as técnicas, os ativos e os processos da ABP são diferentes. Se for necessária uma comparação com outra planta, os dois sites precisam usar as mesmas regras de planejamento, e o relatório diz isso. Ela também declara em cada relatório que os ataques sintéticos representam classes escolhidas, não o comportamento de um adversário real, para que os leitores não superestimem os números de detecção. As duas ressalvas aparecem em todo relatório.

### Nota prática

Ponha a fórmula e o id da planta na legenda de todo widget do painel. Um widget sem fórmula é decoração e deve ser removido na revisão.

### 29.1b Amostragem e comparações entre coortes

Se você amostrar 50 de 500 ativos, diga isso e não escale as constatações como se tivesse visitado os 500. Comparar a cobertura entre janelas exige as mesmas regras de planejamento. Publique o guia de planejamento ao lado do painel de cobertura, para que 71% em março signifique o mesmo tipo de denominador que 71% em setembro.

A seleção da amostra é registrada com a sua semente ou regra, para que os mesmos ativos possam ser revisitados no novo teste. Prefira métricas que subestimam o sucesso, como contar uma correção apenas depois do novo teste.

O guia de planejamento da ABP é publicado ao lado do painel.

### Nota de campo — linhas de metodologia nos gráficos

Quando o CNHP mudou as regras de planejamento em junho, os gráficos no estilo Pulse ganharam uma linha vertical rotulada methodology_id=2026-06. A liderança parou de comparar os 80% de maio com os 70% de julho como se tivessem o mesmo denominador. A honestidade na legenda do gráfico evitou uma falsa narrativa de declínio.

### Exercícios

- **EX085 — Fórmula.** Escreva a fórmula da cobertura e explique um denominador ruim. Rubrica: 3 = denominador planejado + exemplo do mau uso de todo o ICS; 2 = fórmula; 1 = vaidade; 0 = nada.
- **EX086 — Laboratório.** Compare banda e CUSUM na classe A numa frase. Rubrica: 3 = o CUSUM detecta, a banda não, alarmes falsos 0 nos dois na amostra; 2 = parcial; 1 = errado; 0 = nada.
- **EX087 — Subestimar.** Um desenho que subestima o sucesso. Rubrica: 3 = exigir novo teste antes de encerrar; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Planeje o denominador; meça os resultados; avalie os detectores por classe, com intervalos.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue estudando — capítulo 29 de 50

[← Capítulo 28](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) executar um plano de verificação contra o monitor e o zoneamento da ABP; (2) registrar aprovação/reprovação com os hashes das evidências; (3) parar o laboratório se um teste de segurança física falhar.

### 30.1 Plano

Testes: permitir as leituras no escopo; negar códigos de função ruins; negar escritas fora da faixa; falha fechada com política ausente; alcançabilidade do SIS a partir do L4 é falsa; tempo de ciclo dentro do orçamento com o tap. Cada linha: id, preparação, ação, esperado, caminho da evidência.

Na ABP, cada linha do plano nomeia o requisito que confere, como o S-1 para a linha da política ausente e o R-12 para a linha da alcançabilidade. A linha do tempo de ciclo usa a cópia de bancada do tronco até o PLC-A com o tap instalado, conferindo se o tempo fica bem abaixo da parada em 50 ms. As linhas são escritas antes de o laboratório rodar.

### 30.2 Execução

Use apenas hosts sintéticos e bancadas. Capture o stdout e os hashes de configuração. Qualquer falha de segurança física (falha aberta ou SIS alcançável) para o laboratório e abre um bloqueio — nada de continuar para juntar dados.

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

O laboratório de Lena na ABP roda no ambiente de bancada, com hosts e dados de teste sintéticos. Quando a linha da política ausente reprovou uma vez, o laboratório parou e um bloqueio foi aberto contra o S-1; nenhuma outra linha rodou até a correção, porque continuar teria produzido resultados sobre um monitor já sabidamente inseguro.

### 30.3 Relatório

Relatório de laboratório de uma página: versões do ambiente, tabela de resultados, bloqueios abertos, assinatura. Anexe os hashes.

> **Caso sintético — Ashford Batch Plant.** O Laboratório I reprovou uma vez na linha da política ausente; a versão foi suspensa até que o S-1 fosse corrigido.

O relatório de Lena de cada execução do Laboratório I lista as versões das ferramentas, o hash do conjunto de dados de teste, o resultado de cada linha e eventuais bloqueios abertos, e é assinado pelo executor independente. Os hashes dos logs e das exportações são anexados, para que um revisor possa confirmar que a evidência confere com o que foi executado. Um relatório sem hashes não é evidência.

### 30.4 Erros e limites

Laboratórios em bancadas compartilhadas colidem; reserve o ambiente sintético.

Lena reserva o ambiente de bancada da ABP para cada execução de laboratório no calendário compartilhado, com a versão sob teste na reserva. Duas equipes uma vez rodaram builds diferentes na mesma bancada em horários sobrepostos, e os seus logs ficaram impossíveis de separar. Desde então, uma execução sem reserva não conta como evidência de versão, e a bancada é restaurada para um estado conhecido antes de cada execução reservada. Reservar leva minutos.

### Nota prática

O Laboratório I é executado por alguém que não implementou a mudança sob teste. A aprovação registrada precisa de um checklist verde independente.

### 30.1b Dados de teste de referência e inventário

Mantenha um diretório lacrado de dados de teste sintéticos com decisões esperadas conhecidas. As execuções do laboratório precisam conferir o hash do conjunto de dados de teste antes de contarem como evidência de versão. Fotografe ou exporte o inventário do ambiente de laboratório para o relatório. "Passou na minha máquina" sem inventário não é evidência transferível.

As mudanças nos dados de teste são revisadas como código: uma nova decisão esperada precisa nomear o requisito de onde vem. Os logs dos resultados do laboratório são evidência; guarde-os com a tag da versão.

O conjunto de dados de teste de Lena é lacrado e tem hash.

### Nota de campo — verde independente

O implementador de uma correção urgente se ofereceu para rodar o Laboratório I para ganhar tempo. O revisor recusou, rodou pessoalmente as linhas de segurança física e encontrou um caminho que ainda permitia (ALLOW) quando o arquivo de política era um diretório, e não um arquivo. Executores independentes pegam os pressupostos que os autores deixam de ver.

### 30.5 Exemplo resolvido — lendo um resultado de laboratório com honestidade (ABP sintética)

O Laboratório I reproduz um dia gravado de tráfego da ABP mais 40 tentativas de escrita injetadas, passando pela função permit e pela lógica de alarmes. Resultados: 40 de 40 escritas injetadas bloqueadas; 2 escritas legítimas de engenharia bloqueadas porque a estação de engenharia faltava na lista de permissões durante o comissionamento; 0 alarmes suprimidos. Lena relata os dois bloqueios falsos como um defeito de projeto, não como ruído — numa planta em operação, eles teriam impedido uma mudança de receita programada — e acrescenta um conjunto de vetores para o modo de comissionamento. O relatório do laboratório declara o que não foi testado: desempenho sob carga, enlaces seriais e o SIS-B, que está fora do escopo por projeto.

### Exercícios

- **EX088 — Linha.** Escreva a linha de laboratório da falha fechada. Rubrica: 3 = linha completa; 2 = parcial; 1 = vago; 0 = nada.
- **EX089 — Parada.** O que acontece se o SIS for alcançável a partir do L4? Rubrica: 3 = parar, bloqueio, nenhum uso na planta; 2 = só uma nota; 1 = continuar; 0 = nada.
- **EX090 — Evidência.** Três hashes a anexar. Rubrica: 3 = política, binário/versão, log de resultados; 2 = dois; 1 = um; 0 = nada.

### Síntese

Verifique a segurança física primeiro; pare na falha aberta ou na exposição do SIS; calcule o hash de tudo.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue estudando — capítulo 30 de 50

[← Capítulo 29](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Segurança de TO, IoT e sistemas ciberfísicos: implementação II

### Objetivos de aprendizagem

Você vai (1) acrescentar upserts idempotentes de constatações; (2) impor validação de esquema na escrita; (3) versionar as respostas das APIs das ferramentas do CNHP.

### 31.1 Upsert

PUT /findings/{id} com o corpo completo; o mesmo id duas vezes gera uma linha. As impressões digitais de deduplicação propõem ids; pessoas confirmam as fusões entre causas-raiz diferentes.

Na ABP, os ids das constatações vêm do cliente na criação e são reutilizados em cada nova tentativa, então uma falha de rede no meio do pedido não pode criar uma duplicata. As impressões digitais sugerem quando duas constatações podem ser o mesmo problema, mas uma pessoa confirma qualquer fusão, porque duas constatações no PLC-A podem compartilhar um registrador e ainda ter causas diferentes. As fusões são registradas com os motivos.

### 31.2 Validar na escrita

Rejeite campos desconhecidos e nomes proibidos; force a severidade por um enum. Os erros de validação retornam códigos legíveis por máquina.

O repositório de constatações de Lena na ABP rejeita qualquer registro com um campo desconhecido ou um nome proibido, como payload ou password, e retorna um código dizendo qual campo falhou. A severidade aceita apenas os valores acordados. O mesmo validador roda para as criações interativas e para as importações em massa, então nenhum caminho de entrada é mais confiável do que outro e toda rejeição é relatada no mesmo formato. Os erros são documentados com exemplos.

### 31.3 Versionamento da API

Prefixo /v1/; apenas mudanças aditivas dentro da v1. Mudanças incompatíveis exigem /v2/ e uma nota de migração.

> **Caso sintético — Ashford Batch Plant.** Um cliente móvel enviou risk_score; o validador o rejeitou — as pontuações vazias ficam de fora (Capítulo 15).

A API de Lena para a ABP continua na v1 até agora. Lena publica a regra das mudanças aditivas na documentação da API, e a integração contínua compara cada novo esquema com a última versão para pegar campos removidos ou renomeados. Se algum dia uma mudança incompatível se tornar necessária, a v1 continuará rodando ao lado da v2 por um período anunciado, para que os clientes móveis e as importações de scanners possam migrar sem falhar no meio de uma janela.

### 31.4 Erros e limites

As chaves de idempotência não podem ser derivadas apenas do relógio.

Uma chave de idempotência construída a partir da hora atual muda entre as tentativas, então cada nova tentativa parece um pedido novo e cria uma duplicata. Os clientes de Lena geram a chave uma vez por operação lógica, guardam-na com o pedido pendente e a reutilizam até que o servidor confirme o sucesso. A regra é documentada com a API, e as bibliotecas cliente a impõem, para que desenvolvedores individuais não possam reintroduzir o atalho baseado no tempo. As revisões conferem essa regra explicitamente.

### Nota prática

A importação em massa de scanners precisa passar pela mesma validação de esquema que a criação interativa, incluindo as verificações de campos proibidos.

### 31.1b Atualizações parciais e concorrência

Um PATCH que permite mudar a severidade sem referências de evidência convida a rebaixamentos silenciosos. Prefira o PUT completo do corpo validado, ou um PATCH restrito que não possa limpar os hashes das evidências nem mudar o status para encerrado sem um ponteiro de novo teste. Use ETags para que dois responsáveis pela remediação não sobrescrevam um ao outro.

Uma mudança de status para encerrado só é aceita quando o mesmo pedido traz um ponteiro de novo teste. Exclusões em massa são proibidas sem controle duplo. Documente a semântica do upsert no OpenAPI, para que os clientes móveis não inventem ids de nova tentativa.

ETags são obrigatórias em toda atualização de constatação.

### Nota de campo — incidente de importação em massa

Um caminho de importação de scanner pulava as verificações de campos proibidos porque era considerado confiável. O campo de notas de alguém continha uma senha. Depois da limpeza e da troca da senha, a importação em massa foi religada pelo mesmo validador da criação interativa. A importação "confiável" é como os payloads entram em repositórios lacrados.

Clientes que omitem o id da constatação na criação recebem 400 com um link para a documentação do upsert, para que as novas tentativas não inventem duplicatas por acidente.

### 31.5 Exemplo resolvido — upsert idempotente de registros de ativos (ABP sintética)

Duas fontes de inventário relatam o PLC-A: a exportação do projeto de engenharia e a descoberta passiva na rede. O upsert de Lena usa como chave (site, etiqueta do ativo), e não o endereço IP, porque o IP muda quando um controlador é substituído. Cada escrita traz a fonte e um horário de observação; uma observação posterior só atualiza a versão de firmware se a sua fonte for a autoridade para esse campo (a exportação do projeto vence para o firmware; a descoberta vence para "visto pela última vez"). Reproduzir a mesma importação duas vezes não produz mudança — é o teste que prova a idempotência. Sem essas regras, uma importação em massa certa vez sobrescreveu o campo de firmware do PLC-A com "unknown" e o escondeu de uma verificação de avisos de segurança.

### Exercícios

- **EX091 — Upsert.** Por que um POST sem id é arriscado para as novas tentativas? Rubrica: 3 = duplicatas na nova tentativa; 2 = vago; 1 = errado; 0 = nada.
- **EX092 — Rejeitar.** Corpo JSON que precisa receber 400. Rubrica: 3 = contém payload/password/risk_score; 2 = fraco; 1 = corpo válido; 0 = nada.
- **EX093 — Versão.** Renomear reason_code para reason é uma mudança segura na v1? Rubrica: 3 = não, incompatível, vai para a v2; 2 = hesitante; 1 = sim; 0 = nada.

### Síntese

Escritas idempotentes, esquema estrito, versões explícitas.

<!-- cyberabc:chapter-navigation:start ch-31 -->
### Continue estudando — capítulo 31 de 50

[← Capítulo 30](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Segurança de TO, IoT e sistemas ciberfísicos: confiabilidade

### Objetivos de aprendizagem

Você vai (1) definir metas de disponibilidade para as ferramentas de segurança de TO; (2) usar novas tentativas com orçamentos que respeitem o tempo de ciclo; (3) degradar com segurança quando uma dependência falha.

### 32.1 Metas

Caminho de permitir/negar durante as janelas: alta disponibilidade. Painéis de cobertura: melhor esforço. Declare a meta; não insinue cinco noves sem um orçamento.

Na ABP, o caminho de negação do monitor serial precisa funcionar durante toda janela, enquanto o painel de cobertura pode ficar indisponível por uma hora sem dano. Lena escreve as duas metas com o orçamento por trás de cada uma, para que ninguém presuma que o painel precisa do mesmo cuidado que a imposição, nem que a imposição tolera as indisponibilidades do painel. As metas são revistas todo ano.

### 32.2 Novas tentativas

As novas tentativas ajudam nos uploads instáveis de evidências, mas precisam de um prazo para que o orçamento do tronco continue valendo. Limite o total de tentativas.

O enviador de evidências de Lena na ABP tenta de novo com atrasos crescentes e desiste depois de um número fixo de tentativas ou de um prazo, o que vier primeiro. Os uploads que falham ficam enfileirados em disco e são relatados, então nada se perde. As novas tentativas nunca rodam no tronco até o PLC-A, onde poderiam tomar o lugar do tráfego de controle e quebrar o orçamento do ciclo. Os limites são escritos na permissão.

### 32.3 Degradação segura

Se o repositório de constatações cair, continue negando/permitindo localmente e enfileire os rascunhos em disco — nunca falhe aberto nas verificações de política.

> **Caso sintético — Ashford Batch Plant.** Durante uma indisponibilidade do repositório de constatações, a fila do laptop de Lena guardou os rascunhos; o monitor serial continuou negando as escritas fora da faixa.

Lena testa esse modo degradado no Laboratório II, na bancada. Durante uma indisponibilidade real do repositório de constatações, os rascunhos ficaram enfileirados no laptop de Lena e o monitor serial continuou negando as escritas fora da faixa. Depois de cada indisponibilidade, Lena confirma que todo rascunho enfileirado chegou ao repositório, comparando as contagens com o log da fila.

### 32.4 Erros e limites

Novas tentativas contra um tronco com limite de taxa podem parecer inundações; coordene os orçamentos com a permissão de trabalho.

A permissão de trabalho de Lena na ABP declara a taxa máxima de pedidos para qualquer tráfego de avaliação em cada tronco, incluindo as novas tentativas. Se as novas tentativas fossem ultrapassá-la, a ferramenta espera. Ela coordena com a equipe de monitoramento do site antes de uma janela, para que uma rajada de novas tentativas não seja confundida com um ataque e não dispare uma resposta a incidentes desnecessária. As taxas são definidas com os engenheiros de controle. Elas são revistas anualmente.

### Nota prática

Quando a fila de rascunhos passar de um limite, pare de iniciar novos métodos de descoberta e acione o líder. Varreduras não registradas enquanto as constatações não podem ser gravadas criam risco.

### 32.1b Orçamentos de erro e verificações de saúde

Defina os orçamentos de erro do caminho de negação separadamente dos orçamentos de melhor esforço da interface. Verifique a saúde do armazenamento de políticas e do destino dos eventos no início da janela. Começar uma janela às cegas e descobrir um destino quebrado no meio de uma varredura é uma falha de operação que este capítulo pretende evitar. Uma verificação de saúde que falha atrasa o início da janela; as verificações nunca são encurtadas para ganhar tempo.

Experimentos de caos rodam apenas em ambientes sintéticos, nunca durante a janela assinada de um cliente. Registre os ids dos experimentos separadamente dos ids das janelas, para que as métricas não se misturem. Publique os dois orçamentos de erro, o do caminho de negação e o da interface.

### Nota de campo — contrapressão da fila

Quando a fila de rascunhos chegou a 50 durante uma indisponibilidade do repositório, a descoberta no estilo Track parou automaticamente e acionou Lena. A negação/permissão continuou. O limite de 50 foi escolhido para que a fila guarde uma noite inteira de rascunhos com folga.

### 32.5 Exemplo resolvido — degradando com segurança quando o coletor falha (ABP sintética)

O coletor de monitoramento do CNHP fica numa porta espelhada. Se ele falhar, nada no processo deve mudar: o projeto mantém o coletor fora de todo caminho de controle. As metas de confiabilidade de Lena dizem respeito às evidências, não à produção: 99,5 % de disponibilidade de captura por mês e alertas para perdas acima de 0,1 %. As novas tentativas até o repositório central usam recuo exponencial com um teto, para que uma indisponibilidade do repositório não inunde o enlace da DMZ compartilhado com a réplica do historiador. Quando a fila enche, o coletor descarta os pacotes brutos mais antigos, mas mantém os registros de resumo, e gera um alerta de "visibilidade degradada" para que os analistas saibam que a ausência de alertas significa menos.

### Exercícios

- **EX094 — Meta.** Frase de disponibilidade para o caminho de negação. Rubrica: 3 = meta por janela + medida; 2 = "alta" vago; 1 = piada dos cinco noves; 0 = nada.
- **EX095 — Degradar.** O que nunca pode degradar para ALLOW? Rubrica: 3 = decisões de política/lista de permissões; 2 = parcial; 1 = interface; 0 = errado.
- **EX096 — Fila.** Regra de contrapressão quando a fila de rascunhos está longa. Rubrica: 3 = parar a nova descoberta + acionar; 2 = parcial; 1 = ignorar; 0 = nada.

### Síntese

Negações confiáveis, novas tentativas com orçamento, degradação fechada.

<!-- cyberabc:chapter-navigation:start ch-32 -->
### Continue estudando — capítulo 32 de 50

[← Capítulo 31](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Segurança de TO, IoT e sistemas ciberfísicos: segurança física e resiliência

### Objetivos de aprendizagem

Você vai (1) escrever as condições de parada como verificações executáveis; (2) planejar a reversão de mudanças nas ferramentas no meio da janela; (3) conduzir um exercício de mesa sobre uma falha da lista de negação ou do tempo de ciclo.

### 33.1 Paradas executáveis

As condições de parada são código: canário de tempo de ciclo, feed de alarmes de processo, arquivo de kill switch do cliente, entrada de falha do SIS. Pessoas também mandam parar; o software não pode discordar de uma parada humana.

Na ABP, a lógica de parada do monitor serial lê o canário de tempo de ciclo, o feed de alarmes de processo, um arquivo de kill switch e a entrada de falha do SIS-B. Qualquer um deles para imediatamente a atividade de avaliação. Uma ordem humana de parada sempre vence, e o software não tem nenhuma configuração que possa anulá-la ou adiá-la até que um trabalho em execução termine.

### 33.2 Reversão

Fixe as versões; mantenha assinado o binário anterior do monitor. Se um novo build avaliar mal as listas de permissões, reverta em minutos.

Lena mantém o build assinado anterior do monitor na bancada e no kit da janela, para que a reversão seja um comando testado, não uma recompilação. A reversão foi ensaiada antes da primeira janela na planta e é repetida depois de cada versão importante. Uma reversão restaura tanto o binário quanto a versão da lista de permissões que rodava com ele. A reversão restaura o estado anterior em minutos. Os dois são fixados.

### 33.3 Exercício de mesa

Percorra um cenário: o tempo de ciclo passa de 50 ms às 02:40; quem é chamado; o que é dito; quando a retomada é permitida. Atualize o runbook onde o exercício empacou.

> **Caso sintético — Ashford Batch Plant.** O exercício de mesa descobriu que o caminho do arquivo de kill switch não estava documentado; o runbook v1.4 corrigiu isso antes da janela seguinte.

Os exercícios de mesa da ABP acontecem a cada período, com a presença do líder de turno, e toda lacuna que eles expõem é fechada por uma nova versão do runbook antes da janela seguinte. Cada cenário nomeia quem é chamado, o que lhe é dito e quem pode autorizar a retomada do trabalho.

### 33.4 Erros e limites

Teatro de resiliência é um fichário que ninguém abre. Faça um exercício por período.

Os exercícios de resiliência de Lena na ABP acontecem uma vez por período, usam o runbook real e incluem pelo menos uma parada e uma reversão. Cada exercício produz pelo menos uma edição do runbook ou um motivo registrado de por que nenhuma foi necessária. Um fichário que não é aberto desde a última auditoria é tratado como não testado, por mais completo que pareça na prateleira. Os resultados dos exercícios são arquivados com a versão do runbook. As lacunas recebem donos.

### Nota prática

Escreva antecipadamente os modelos de SMS/e-mail para parada, retomada e reversão. Sob estresse, as pessoas omitem a versão da permissão de trabalho ou o horário do próximo ponto de verificação.

### 33.1b Contatos secundários e autoridade de retomada

Condições de parada que acionam uma única pessoa falham quando essa pessoa está offline. Mantenha contatos primário e secundário, com passagem confirmada. Quem pode retomar depois de uma parada? Nomeie o papel na permissão de trabalho. O monitor deve exigir um token de retomada ligado a esse papel e à AllowListVersion.

Depois de toda parada real, faça uma avaliação a quente de cinco minutos e registre pelo menos uma edição do runbook. As notas dessa avaliação registram o gatilho, o tempo até a parada e o tempo até a retomada, para que os exercícios possam ser comparados com as paradas reais.

### Nota de campo — token de retomada

Depois de uma parada, a retomada exigiu um token emitido para o papel do contato de segurança de processo e ligado à AllowListVersion v1.4.2. Um interruptor booleano no host de salto foi removido da interface. Retomar sem autoridade é como as condições de parada se tornam opcionais.

### 33.5 Exemplo resolvido — uma parada executável durante o comissionamento (ABP sintética)

Durante a troca do firewall no conduto L3–L2, a condição de parada diz: "Se a IHM perder os valores do PLC-A por mais de 10 segundos, ou se ocorrer qualquer desarme do SIS-B, reverter para o conjunto de regras anterior." A reversão é um único comando preparado com antecedência e testado duas vezes no dia anterior, e o líder de turno detém a autoridade para acioná-lo; o engenheiro não discute. A retomada exige um token escrito do líder de turno depois que a causa for entendida. Separadamente, Lena confirma que o desarme por nível alto do SIS-B no R-101 é cabeado e não é afetado pela mudança, coerente com a expectativa da IEC 61511 de que a função de segurança permaneça independente.

### Exercícios

- **EX097 — Kill switch.** Projete um kill switch humano atendido em ≤30 s. Rubrica: 3 = mecanismo + sondagem + falha fechada; 2 = ideia; 1 = vago; 0 = nada.
- **EX098 — Reversão.** Três precondições para reverter no meio da janela. Rubrica: 3 = binário anterior, fixação da política, notificar a segurança de processo; 2 = duas; 1 = uma; 0 = nada.
- **EX099 — Injeção.** Uma injeção para o exercício de mesa. Rubrica: 3 = específica; 2 = vaga; 1 = nenhuma; 0 = insegura.

### Síntese

Paradas que você consegue executar, reversões que você consegue fazer, exercícios de mesa que atualizam os runbooks.

<!-- cyberabc:chapter-navigation:start ch-33 -->
### Continue estudando — capítulo 33 de 50

[← Capítulo 32](#ch-32) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Segurança de TO, IoT e sistemas ciberfísicos: integração

### Objetivos de aprendizagem

Você vai (1) integrar os eventos do monitor ao repositório de constatações; (2) definir consumidores idempotentes; (3) testar contratos com dados de teste.

### 34.1 Contrato de eventos

Eventos de negação/permissão: versão do esquema, ids, timestamps em UTC, origem, fc, registrador, motivo, versão da política. Os consumidores ignoram campos desconhecidos; os produtores permanecem aditivos.

O contrato de eventos de Lena na ABP é versionado e publicado com dados de teste para cada código de motivo. Cada evento traz tanto o horário em que aconteceu quanto o horário em que foi recebido, além da fonte do relógio. Os produtores podem acrescentar campos, mas nunca removê-los ou renomeá-los dentro de uma versão, para que os consumidores mais antigos continuem funcionando. Os dados de teste ficam no repositório. As mudanças são revisadas.

### 34.2 Consumidores idempotentes

O repositório de constatações registra os eventos processados pelo event_id. Reproduzir o log não pode criar constatações duplicadas.

Lena testa a reprodução na bancada passando o log de eventos de um dia inteiro duas vezes pelo consumidor e conferindo que a contagem de constatações não muda. O teste pegou um defeito em que os eventos eram identificados pelo timestamp em vez do event_id, o que duplicou três tickets durante uma tempestade de reprodução antes que a correção chegasse. Os testes de reprodução rodam na integração contínua. As falhas bloqueiam o merge. O teste roda toda noite.

### 34.3 Testes de contrato

JSON de dados de teste para cada código de motivo; os testes do consumidor afirmam os campos do ticket resultante. Rodam na integração contínua sobre dados de teste sintéticos.

> **Caso sintético — Ashford Batch Plant.** Uma tempestade de reprodução duplicou três tickets até que a idempotência por event_id fosse implantada.

Os testes de contrato de Lena rodam em todo pull request e de forma agendada. Eles usam um dado de teste para cada código de motivo e afirmam os campos do ticket que o consumidor deve criar, como ativo, técnica e severidade. Uma execução agendada contra o ambiente de homologação pega mudanças do produtor mesmo quando não há nenhum pull request aberto, então a deriva é encontrada antes de uma janela, e não durante uma.

### 34.4 Erros e limites

A defasagem de relógio confunde as linhas do tempo; prefira o horário do evento mais o horário de recebimento.

A visão de linha do tempo de Lena na ABP mostra o horário do evento e o horário de recebimento lado a lado, para que um leitor veja quando o relógio de um dispositivo está errado. O Laboratório II depois injetou uma defasagem de 90 segundos no PLC-A e descobriu que dois eventos ficavam fora de ordem no dossiê até que uma correção de deslocamento fosse aplicada. As fontes de relógio são registradas em cada evento exatamente por esse motivo. Lena mantém os relógios sincronizados onde possível. A deriva gera alarme.

### Nota prática

Eventos envenenados (timestamps no futuro, versões de política desconhecidas) vão para uma fila de mensagens mortas com um alerta — não para as constatações e não para /dev/null.

### 34.1b Mensagens mortas e exercícios de esquema

Cada evento enviado à fila de mensagens mortas guarda o erro de validação que o rejeitou. Os operadores reproduzem depois de corrigir o produtor. Pratique acrescentar um campo opcional de ponta a ponta numa simulação: produtor, consumidor, dado de teste, documentação. Equipes que só evoluem esquemas em emergências inventam atalhos incompatíveis.

Uma execução agendada que falha abre um ticket para a equipe do produtor, não para a do consumidor. A idade das mensagens mortas é um gráfico de SLO ao lado da latência do caminho de negação.

A ABP faz um exercício de esquema a cada período. Os resultados dos exercícios são registrados com as versões do produtor e do consumidor envolvidas.

### Nota de campo — quarentena de eventos envenenados

Um defeito num produtor emitiu eventos com timestamps em 2099. A quarentena de mensagens mortas os pegou; nenhuma constatação foi criada contra hosts aleatórios. Descartes invisíveis teriam sido piores — ao menos a quarentena aciona alguém.

Inclua um canário do consumidor que reprove a implantação se os eventos envenenados não forem postos em quarentena em até um minuto na homologação.

Cada exercício termina com o novo campo visível num ticket de homologação e com a duração do exercício registrada, para que o próximo exercício possa ser comparado com ele.

### 34.5 Exemplo resolvido — integrando os alertas ao sistema de manutenção (ABP sintética)

Os alertas do CNHP fluem para o sistema de gestão da manutenção da ABP, para que um alerta de "download de programa para o PLC-A" possa ser casado com uma ordem de serviço aberta. O contrato de eventos traz um ID de evento, a etiqueta do ativo, a técnica do ATT&CK for ICS (T0843 Program Download), o horário com a fonte do relógio e o hash da evidência. O consumidor é idempotente no ID do evento, então um alerta reproduzido não cria duas ordens de serviço. Os testes de contrato rodam na integração contínua com dados de teste dos dois lados; um evento sem o campo de técnica é enviado para uma fila de mensagens mortas e revisado diariamente, em vez de descartado. Um download sem ordem de serviço correspondente é escalado ao líder de turno em até cinco minutos.

### Exercícios

- **EX100 — Campo.** Por que incluir policy_version em todo evento? Rubrica: 3 = auditar quais regras se aplicaram; 2 = vago; 1 = errado; 0 = nada.
- **EX101 — Reprodução.** Como o event_id impede constatações duplicadas? Rubrica: 3 = upsert/ignorar duplicatas; 2 = vago; 1 = errado; 0 = nada.
- **EX102 — Dado de teste.** Dois dados de teste exigidos antes de um novo código de motivo. Rubrica: 3 = exemplo do produtor + ticket esperado do consumidor; 2 = um; 1 = vago; 0 = nada.

### Síntese

Contratos, consumidores idempotentes, testes com dados de teste.

<!-- cyberabc:chapter-navigation:start ch-34 -->
### Continue estudando — capítulo 34 de 50

[← Capítulo 33](#ch-33) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 35 →](#ch-35)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) redesenhar a interface de cobertura do CNHP segundo os princípios de subestimação; (2) defender o projeto numa revisão; (3) produzir textos de interface que recusem pontuações vazias.

### 35.1 Problema

As partes interessadas querem uma grande porcentagem verde. Projete uma interface que mostre planejado/observado/não visto e recuse uma pontuação única de segurança.

Na ABP, o gerente da planta primeiro pediu uma porcentagem que mostrasse se o CNHP estava funcionando. A equipe de Lena explicou que qualquer número único misturaria técnicas observadas, deriva dos condutos e alcançabilidade do SIS-B, que precisam de donos diferentes e de orçamentos diferentes. A tela resultante dá a cada medida a sua própria linha, com o denominador visível, e as técnicas planejadas mas não vistas são listadas por id, para que o gerente possa perguntar quais importam antes de aprovar a fase seguinte.

### 35.2 Texto

71% das técnicas de ICS planejadas observadas — não é uma pontuação de risco residual. Botão: exportar o denominador. Mostre "SIS alcançável?" como um sim/não separado.

A equipe de Lena testou essa redação com o gerente da planta e dois líderes de turno antes da publicação. Um líder de turno leu um rascunho inicial que dizia apenas setenta e um por cento e presumiu que a planta estava setenta e um por cento segura, que é exatamente a leitura errada que a ressalva evita. O botão de exportação produz a lista das 44 técnicas planejadas, cada uma marcada como observada ou não vista, e a linha do SIS-B nunca mostra uma porcentagem, porque a alcançabilidade é verdadeira ou falsa no dia da verificação.

### 35.3 Revisão

Os revisores tentam forçar um selo de risco vermelho/amarelo/verde; o ateliê precisa manter a posição com as regras do capítulo de medição.

> **Caso sintético — Ashford Batch Plant.** O Ateliê II eliminou o selo; o painel lista as técnicas planejadas não vistas por id e a alcançabilidade do SIS separadamente.

Os críticos no ateliê argumentaram que os executivos não leriam uma lista. A equipe de Lena respondeu com a decisão real do gerente: quais condutos financiar e fechar em seguida, o que uma cor não consegue expressar. O selo removido também não tinha regra definida para ficar amarelo, então dois revisores já tinham discordado sobre a sua cor com os mesmos dados. Substituí-lo por itens nomeados encerrou a discussão e deu um dono a cada item.

### 35.4 Erros e limites

Padrões obscuros ("só para os executivos") reintroduzem as pontuações vazias — rejeite-os no CODEOWNERS da interface.

Na ABP, um pedido posterior solicitou uma visão de resumo só para executivos, com um único mostrador colorido. A equipe de Lena a recusou durante a revisão de código, citando a decisão do ateliê e as regras de medição, e ofereceu em seu lugar uma exportação de uma página com os mesmos três números e os seus denominadores. Exigir que um dono de código aprove toda mudança na interface do painel significa que essa discussão é resolvida por um revisor nomeado que conhece o histórico, e não reaberta em silêncio por quem quer que edite a tela em seguida.

### Nota prática

Tarefa de pesquisa com usuários: explique este número a um gerente de planta sem dizer "estamos seguros". Se os usuários não conseguirem, o texto falhou.

### 35.1b Acessibilidade e verdade da exportação

As métricas que subestimam ainda precisam ser legíveis: fonte grande para a fração, linguagem simples para a ressalva, acesso por teclado à exportação do denominador. Se a interface e a exportação em CSV discordarem, a exportação vence para o relatório. Construa as exportações primeiro; trate a interface como uma visão.

As exportações narrativas geradas pela mesma consulta da interface são coladas nos relatórios sem a ambiguidade das capturas de tela. Esconder a ressalva numa dica de ferramenta reintroduz o problema da pontuação vazia para quem não passa o mouse por cima.

Lena confere cada versão contra a exportação.

### Nota de campo — a tarefa de explicar ao diretor financeiro

Na pesquisa com usuários, três gerentes explicaram a fração de cobertura como "o quanto estamos seguros". Depois de mudanças no texto que proibiram essa leitura e destacaram a alcançabilidade do SIS separadamente, a mesma tarefa produziu explicações sobre as verificações planejadas e as constatações abertas.

Toda exportação traz na primeira linha a versão da consulta e o horário em que rodou.

### 35.5 Exemplo resolvido — a crítica do ateliê (ABP sintética)

O enunciado do Ateliê II: um gerente de planta precisa decidir, a partir de uma única tela, se aprova a fase seguinte do CNHP. A equipe de Lena mostra três números com denominadores — 31 das 44 técnicas planejadas do ATT&CK for ICS observadas nos testes, 6 dos 9 condutos conferindo com o projeto de zonas, SIS-B alcançável a partir de qualquer zona roteada: não — mais uma lista curta de constatações altas abertas. Os críticos defenderam um selo de risco único; a equipe respondeu que a decisão do gerente depende de quais condutos continuam abertos, e não de uma média. O projeto aceito põe a lista de condutos abertos em primeiro lugar, porque é o item que o gerente de fato pode financiar.

### Exercícios

- **EX103 — Texto.** Subtítulo sob o número de cobertura. Rubrica: 3 = nega a leitura como risco residual; 2 = ressalva fraca; 1 = nenhuma; 0 = insinua segurança.
- **EX104 — Selo.** Uma frase recusando um selo RAG. Rubrica: 3 = clara + alternativa; 2 = só recusa; 1 = aceita; 0 = nada.
- **EX105 — Exportação.** Colunas da exportação do denominador. Rubrica: 3 = id da técnica, planejada, observada, notas; 2 = parcial; 1 = só a %; 0 = nada.

### Síntese

Uma interface que ensina a métrica, não um semáforo de impressões.

<!-- cyberabc:chapter-navigation:start ch-35 -->
### Continue estudando — capítulo 35 de 50

[← Capítulo 34](#ch-34) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 36 →](#ch-36)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-36"></a>

## Capítulo 36 — Segurança de TO, IoT e sistemas ciberfísicos: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) dimensionar os monitores dentro dos orçamentos de tempo de ciclo; (2) aplicar o raciocínio de token bucket ao tráfego de avaliação; (3) medir o impacto na planta com um canário.

### 36.1 O tempo de ciclo é cidadão de primeira classe

Metas de vazão que ignoram o orçamento de ciclo do CLP são defeitos. Dimensione os pipelines de decodificação para que o tempo de fio mais decodificação fique dentro do orçamento medido no Capítulo 3.

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

Na ABP, o tronco RS-485 até o PLC-A roda um ciclo de polling de 21 ms dentro de um ciclo de controle de 100 ms, e a condição de parada dispara se o tempo de ciclo chegar a 50 ms. Lena dimensiona o monitor para que o tap, a decodificação e o logging não acrescentem nada ao tempo de fio, porque o tap é passivo e o decodificador roda no seu próprio host. Os testes de carga na bancada reproduzem um dia inteiro de tráfego capturado em velocidade dupla, para confirmar que o decodificador nunca fica atrás do tronco.

### 36.2 Tráfego de avaliação

Quando métodos ativos são autorizados, limite a sua taxa para que não possam esfomear o tráfego de controle. Prefira métodos somente de escuta; quando precisar fazer polling, compartilhe um orçamento global entre os scanners.

Durante as janelas de avaliação do CNHP na ABP, apenas uma ferramenta ativa pode fazer polling no tronco por vez, e a sua taxa de pedidos é escrita na permissão antes de ela começar. A descoberta passiva a partir do tap cobre a maior parte do inventário, então o polling ativo fica limitado aos poucos dispositivos que não falam por conta própria. Cada ferramenta informa a sua taxa ao orçamento compartilhado, e o líder da janela pode pausar todos os métodos ativos com um único interruptor se o tempo de ciclo subir.

### 36.3 Canários

Um pedido canário sintético ou uma sondagem de tempo de ciclo a cada minuto acompanha a saúde; as condições de parada disparam no limiar (Capítulo 33).

> **Caso sintético — Ashford Batch Plant.** Com ciclos de 21 ms no tronco RS-485, Lena deixou folga abaixo de 50 ms para que um pico de decodificação não disparasse a parada.

O canário na ABP lê um registrador de status inofensivo do PLC-A a cada minuto e registra o tempo de resposta ao lado do tempo de ciclo do tronco. Se qualquer um dos dois se aproximar do seu limiar, o líder da janela é acionado antes de a condição de parada ser atingida, o que dá tempo para pausar o trabalho ativo com calma, em vez de reagir a uma parada automática.

### 36.4 Erros e limites

Scanners distribuídos precisam de um orçamento global coordenado, ou multiplicam o limite por N.

Na ABP, dois scanners certa vez rodaram de hosts diferentes, cada um dentro da sua própria taxa, e juntos excederam o orçamento do tronco. Lena moveu o orçamento para um único coordenador que concede tokens a todos os scanners, para que o total fique dentro da permissão não importa quantas ferramentas estejam rodando. Um scanner que não consegue alcançar o coordenador não pode enviar nada, o que mantém a falha segura, em vez de deixar cada ferramenta recorrer ao seu próprio limite.

### Nota prática

Publique uma nota sobre a economia dos limites de taxa: o custo de esperar versus o custo da interrupção de um lote. A maioria dos argumentos para aumentar os limites se dissolve quando o custo da interrupção é escrito.

### 36.1b Justiça e aquecimento

Quando vários métodos compartilham um orçamento, um enumerador ruidoso pode esfomear uma revisão de configuração silenciosa. Pondere ou separe os orçamentos por classe de método. Aumente o tráfego gradualmente no início da janela e esvazie-o antes da parada definitiva. Esvaziar significa nenhum pedido novo nos últimos dez minutos, para que as respostas em trânsito cheguem antes da parada.

Documente quem pode aumentar um limite de taxa e qual tipo de ticket AUTH é exigido. Um limite aumentado expira no fim da janela, a menos que seja renovado por um novo ticket.

Lena impõe os dois orçamentos no coordenador.

### Nota de campo — cronograma de aquecimento

O agendador agora aumenta os pollings de avaliação ao longo de cinco minutos no início da janela. Partidas instantâneas em taxa máxima tinham disparado alarmes de vibração sem relação num skid vizinho. O aquecimento é uma cortesia com o processo e com as pessoas que são donas dele.

### 36.5 Exemplo resolvido — medindo a carga do monitoramento no PLC-A (ABP sintética)

Um coletor de saúde de ativos proposto leria 120 registradores de retenção do PLC-A a cada segundo. No controlador de bancada, Lena mede o tempo de varredura com e sem o coletor: 18 ms de base, 23 ms com o polling, contra um watchdog de 50 ms. O aumento é aceitável na bancada, mas ela ainda limita o coletor a 120 registradores a cada 5 segundos em produção, acrescenta um canário numa linha antes da implantação em toda a planta e alarma se o tempo de varredura passar de 30 ms. O tráfego de avaliação recebe o mesmo tratamento: toda ferramenta de teste precisa declarar a sua taxa de pedidos, e a permissão define um máximo.

### Exercícios

- **EX106 — Laboratório.** Bytes e tempo por ciclo a 115200 — relate os dois. Rubrica: 3 = 244 bytes, 21,2 ms; 2 = um; 1 = errado; 0 = nada.
- **EX107 — Folga.** Se o orçamento é de 50 ms e o ciclo é de 21 ms, que folga resta e por que mantê-la? Rubrica: 3 = ~29 ms para picos/novas tentativas; 2 = só o número; 1 = usar tudo; 0 = nada.
- **EX108 — Global.** Por que três coletores não coordenados quebram uma permissão de 2 req/s? Rubrica: 3 = 3× a taxa; 2 = vago; 1 = nega; 0 = nada.

### Síntese

Orçamento primeiro, escala depois, canário sempre.

<!-- cyberabc:chapter-navigation:start ch-36 -->
### Continue estudando — capítulo 36 de 50

[← Capítulo 35](#ch-35) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 37 →](#ch-37)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-37"></a>

## Capítulo 37 — Segurança de TO, IoT e sistemas ciberfísicos: operações

### Objetivos de aprendizagem

Você vai (1) escrever o runbook de uma janela; (2) fazer a passagem de turno; (3) conduzir o encerramento, incluindo a desativação de contas e o lacre das evidências.

### 37.1 Conteúdo do runbook

Contatos, ponteiro para a permissão de trabalho, versões das ferramentas, condições de parada, árvore de escalonamento, caminhos das evidências. Mantenha-o curto o bastante para ser usado sob estresse.

O runbook da ABP feito por Lena cabe em quatro páginas impressas. Ele nomeia o líder da janela e o engenheiro de controle, aponta para a permissão de trabalho e lista as versões permitidas de cada ferramenta. As condições de parada, incluindo o tempo de ciclo em 50 ms, estão na primeira página, seguidas pela árvore de escalonamento e pela localização da pasta de evidências. O runbook v1.4 acrescentou o caminho do arquivo de kill switch depois que o exercício de mesa descobriu que ele faltava, e toda mudança desde então é registrada no histórico de versões.

### 37.2 Passagem de turno

Log do turno: constatações abertas, últimos ids de eventos, aprovações pendentes, estado do kill switch, alarmes de processo durante a janela. Passagem verbal mais o log.

Na ABP, o líder que sai lê o log do turno em voz alta para o líder que entra, e os dois o rubricam. O log lista as constatações abertas com os donos, os últimos ids de eventos registrados pelo monitor, eventuais aprovações ainda pendentes, se o kill switch está armado e os alarmes de processo gerados durante a janela. Falar os itens em voz alta pega entradas que uma pessoa achava óbvias e a outra nunca tinha visto, como uma regra temporária aguardando remoção.

### 37.3 Encerramento

Desativar contas temporárias, trocar segredos, lacrar evidências, exportar métricas, agendar a retrospectiva. Um checklist vence a memória.

```python
"""Lab: fit patch jobs into plant maintenance windows (synthetic, greedy by risk)."""
windows = [("W1 Sat 02-06", 4.0), ("W2 Sun 02-04", 2.0)]
jobs = [("HMI OS update", 1.5, 8), ("historian DB patch", 2.5, 5), ("PLC-A firmware", 3.0, 9),
        ("eng-WS AV update", 0.5, 3), ("switch firmware", 1.0, 6)]   # name, hours, risk score
left = {w: h for w, h in windows}; plan = {w: [] for w, _ in windows}; deferred = []
for name, h, r in sorted(jobs, key=lambda j: -j[2]):
    for w, _ in windows:
        if left[w] >= h:
            left[w] -= h; plan[w].append(name); break
    else:
        deferred.append(name)
for w, _ in windows:
    print(w, plan[w], f"spare={left[w]:.1f}h")
print("deferred:", deferred)
```

Saída esperada:

```text
W1 Sat 02-06 ['PLC-A firmware', 'switch firmware'] spare=0.0h
W2 Sun 02-04 ['HMI OS update', 'eng-WS AV update'] spare=0.0h
deferred: ['historian DB patch']
```

> **Caso sintético — Ashford Batch Plant.** O encerramento pegou a correção adiada do historiador ainda sem data — escalada antes da retrospectiva.

O checklist de encerramento de Lena é executado por duas pessoas, e o seu resultado é guardado com um hash. Uma correção do historiador tinha sido adiada durante a janela sem data, então o checklist a sinalizou, e a correção recebeu um dono e uma data antes da reunião de retrospectiva.

### 37.4 Erros e limites

Runbooks em wikis que ninguém consegue acessar da sala de controle falham; mantenha uma cópia offline.

Na ABP, a sala de controle perdeu o acesso de rede à wiki durante uma janela, e o líder precisava da árvore de escalonamento imediatamente. Desde então, o runbook mais recente é impresso e guardado numa pasta ao lado da HMI-1, e uma cópia fica na estação de engenharia para uso offline. Cada cópia impressa traz o seu número de versão, e o checklist de encerramento confirma que a cópia em papel confere com a versão atual, para que um procedimento antigo não seja seguido por engano durante um incidente.

### Nota prática

O plantão das ferramentas do CNHP não é licença para alargar condutos. Os acionamentos tratam da segurança das ferramentas e da imposição da permissão; os incidentes de processo seguem pelo caminho de resposta a incidentes e de segurança de processo da planta.

### 37.1b Calendário e kits sobressalentes

As janelas ficam num calendário compartilhado, com a versão da permissão de trabalho na descrição. A sobreposição acidental de dois métodos ruidosos no mesmo tronco é uma falha de operação. Os kits de operação incluem imagens sobressalentes do host de salto, cartões de contato impressos e cópias offline da permissão para quando o SSO estiver fora do ar.

O encerramento não é marcado como concluído até que os dois signatários do checklist sejam registrados pelo nome. A passagem de turno inclui ler em voz alta, para o líder que entra, as últimas dez negações do monitor.

Lena confere o calendário em cada passagem de turno. As sobreposições são registradas como constatações.

### Nota de campo — kit offline

O SSO falhou durante uma janela de domingo. A cópia offline do runbook e os cartões de contato impressos permitiram que a equipe parasse de forma limpa e notificasse a segurança de processo. Desde então, o kit é conferido em todo encerramento.

As métricas de operação incluem os acionamentos por janela e o tempo médio para reconhecer as paradas; métricas de vaidade, como hosts tocados, ficam fora do painel de operações.

### 37.5 Exemplo resolvido — uma passagem de turno com conteúdo de segurança (ABP sintética)

A folha de passagem de turno da ABP ganha três linhas: alertas abertos do CNHP e quem é dono deles; qualquer sessão remota de fornecedor habilitada ou agendada; e qualquer regra temporária ou desvio em vigor, com o horário de expiração. Em 14 de março, o turno da noite registrou uma regra temporária de firewall para um diagnóstico de fornecedor, expirando às 06:00; o turno do dia conferiu às 06:15, encontrou-a ainda presente e a removeu com a concordância do engenheiro. Sem a linha na passagem de turno, a regra teria se tornado um conduto permanente. O encerramento de cada ordem de serviço de segurança exige o ponteiro da evidência e a confirmação de que as mudanças temporárias foram revertidas.

### Exercícios

- **EX109 — Checklist.** Seis passos de encerramento. Rubrica: 3 = seis sensatos; 2 = quatro; 1 = dois; 0 = nada.
- **EX110 — Passagem de turno.** Três campos que o log do turno precisa incluir. Rubrica: 3 = constatações/eventos/aprovações (ou equivalente); 2 = dois; 1 = um; 0 = nada.
- **EX111 — Laboratório.** Qual trabalho foi adiado e o que o encerramento precisa registrar? Rubrica: 3 = correção do historiador + risco residual + data da próxima janela; 2 = só o nome; 1 = vago; 0 = errado.

### Síntese

Opere com runbooks, passagens de turno e um encerramento implacável.

<!-- cyberabc:chapter-navigation:start ch-37 -->
### Continue estudando — capítulo 37 de 50

[← Capítulo 36](#ch-36) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 38 →](#ch-38)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-38"></a>

## Capítulo 38 — Segurança de TO, IoT e sistemas ciberfísicos: validação

### Objetivos de aprendizagem

Você vai (1) validar correções com novos testes; (2) evitar validações que reintroduzam risco de processo; (3) registrar resultados negativos.

### 38.1 Projeto do novo teste

Mesmo ponto de observação, menor privilégio, mesmo padrão de evidência. Para a correção de uma lista de permissões: confirme na bancada que a escrita é negada; não dispare escritas contra o CLP em operação.

Quando a lista de permissões do HIST-1 foi apertada na ABP, Lena refez o teste a partir do mesmo host de salto e da mesma conta usados na constatação original. Ela reproduziu uma escrita de função 16 na cópia de bancada do PLC-A e confirmou que o monitor a negou com o código de motivo esperado. A verificação ao vivo foi somente de leitura: ela comparou a versão da lista de permissões implantada com a versão da bancada, em vez de enviar escritas em direção a equipamentos de produção.

### 38.2 Resultados negativos

"Ainda aberto" é um resultado de validação válido. Os repositórios de constatações precisam aceitá-lo sem forçar o encerramento.

Na ABP, o novo teste das senhas de engenharia compartilhadas descobriu que elas ainda estavam em uso em duas estações, então a constatação ficou aberta, com a nova evidência anexada. O repositório de constatações de Lena permite que um novo teste registre "ainda aberto" com uma data e um motivo, e o dono recebe um novo prazo. Forçar todo novo teste a encerrar uma constatação estimularia os revisores a marcar correções como concluídas quando elas foram aplicadas só em parte.

### 38.3 Nenhum método novo

A validação usa o método que encontrou o problema, ou uma verificação mais fraca, somente de leitura — não é uma oportunidade de experimentar novos ataques.

> **Caso sintético — Ashford Batch Plant.** Novo teste da regra do L4 para o L2: a alcançabilidade agora exclui o L1-SIS; ticket encerrado com o hash da exportação. Uma constatação separada sobre senhas de engenharia compartilhadas continuou aberta.

O plano de validação de Lena nomeia o método original no ticket antes de o novo teste começar. Quando um revisor sugeriu experimentar uma nova ferramenta de fuzzing durante a validação, ela a registrou como proposta para a avaliação seguinte.

### 38.4 Erros e limites

Ambiente diferente (bancada versus planta) significa que você validou a bancada.

Na ABP, a correção da lista de permissões de Lena foi validada primeiro na cópia de bancada do PLC-A, e o ticket dizia isso. Uma verificação separada, somente de leitura, confirmou que o monitor de produção rodava a mesma versão da lista de permissões, e só então a constatação foi marcada como corrigida em produção. Os relatórios mantêm os dois resultados separados, porque uma aprovação na bancada não pode mostrar que a configuração da planta confere com a da bancada, e algumas diferenças, como revisões de firmware, mudariam o resultado.

### Nota prática

Os novos testes automatizados são verificações em lista de permissões com timeouts rígidos. Eles nunca incluem credential stuffing nem novas tentativas de exploit.

### 38.1b Evidência da validação e arbitragem

Os tickets de validação se ligam à constatação original, ao método usado, ao timestamp e ao hash da nova evidência. Um "parece bom para mim" sem esses campos não encerra uma crítica. As disputas escalam para um árbitro nomeado, que compara os hashes das evidências — ele não ataca de novo.

Quando muitas constatações semelhantes compartilham uma causa-raiz, refaça o teste numa amostra mais os ativos originalmente relatados, e diga isso. As decisões do árbitro são finais para a janela e só podem ser contestadas na retrospectiva.

Os tickets de Lena trazem os quatro campos.

### Nota de campo — novo teste por amostra

Vinte IHMs compartilhavam uma entrada faltando na lista de permissões. A validação refez o teste em cinco mais as duas originalmente relatadas, documentou a amostra e deixou a constatação aberta até que o trabalho na frota terminasse. Declarar as vinte encerradas depois de duas verificações teria sido uma mentira de medição.

### 38.5 Exemplo resolvido — novo teste de validação do projeto de zoneamento (ABP sintética)

Seis meses depois da implantação, Lena roda de novo a verificação de alcançabilidade do Capítulo 2 contra a exportação do firewall em operação e a lista de condutos da descoberta passiva. A exportação confere com o projeto em 8 dos 9 condutos; o nono mostra uma regra L4→L3 não documentada, acrescentada durante uma atualização do ERP. O relatório de validação registra a constatação negativa com evidências, atribui-a ao dono da rede e não introduz nenhum método de teste novo no meio da validação, para que os resultados continuem comparáveis com a linha de base do comissionamento. A zona do SIS-B continua inalcançável nos dois conjuntos de dados, o que é relatado como confirmado, e não presumido.

### Exercícios

- **EX112 — Novo teste.** Passos para validar com segurança uma regra do L4 para o L2 removida. Rubrica: 3 = exportação+alcançabilidade, esperar nenhum caminho, evidência, nenhuma escrita ao vivo; 2 = parcial; 1 = ataque ao vivo; 0 = nada.
- **EX113 — Negativo.** Por que "ainda aberto" precisa poder ser registrado? Rubrica: 3 = honestidade/métricas; 2 = vago; 1 = sempre encerrar; 0 = nada.
- **EX114 — Ambiente.** Limitação quando o novo teste foi feito só na bancada. Rubrica: 3 = clara; 2 = vaga; 1 = afirma a planta; 0 = nada.

### Síntese

Valide de forma estreita; guarde os negativos; não alargue os métodos.

<!-- cyberabc:chapter-navigation:start ch-38 -->
### Continue estudando — capítulo 38 de 50

[← Capítulo 37](#ch-37) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 39 →](#ch-39)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-39"></a>

## Capítulo 39 — Segurança de TO, IoT e sistemas ciberfísicos: manutenibilidade

### Objetivos de aprendizagem

Você vai (1) reservar orçamento para atualizações de políticas e de dependências; (2) manter os adaptadores finos; (3) documentar a titularidade, incluindo a cobertura de férias.

### 39.1 Rotatividade

As técnicas do ATT&CK for ICS, os firmwares dos CLPs e as matrizes de suporte das IHMs dos fornecedores mudam. Reserve tempo de calendário para as atualizações; fixe as versões e acompanhe os avisos de segurança.

Na ABP, Lena mantém uma página de dependências que lista a versão do ATT&CK for ICS usada pelo mapeador, as revisões de firmware do PLC-A e do SIS-B e as versões suportadas pelo fornecedor da IHM. Uma assinatura dos avisos dos fornecedores alimenta uma revisão semanal, e cada versão fixada tem uma data de revisão. Quando a lista de técnicas muda, o plano de cobertura é reconstruído a partir da nova versão antes da avaliação seguinte, para que as 44 técnicas planejadas nunca se refiram em silêncio a um catálogo desatualizado.

### 39.2 Adaptadores finos

Isole os SDKs de terceiros atrás de interfaces, para que as atualizações não reescrevam o núcleo do repositório de constatações.

A equipe de Lena aprendeu isso com o adaptador de alarmes por raspagem de tela, que quebrava a cada atualização da IHM e tocava código muito além do seu propósito. O CNHP agora coloca toda biblioteca de fornecedor atrás de uma pequena interface de que a equipe é dona, com testes de contrato que usam saídas gravadas do fornecedor. Quando um fornecedor muda a sua biblioteca, só o adaptador e os seus testes mudam; a função permit, o repositório de constatações e o código do dossiê ficam intocados, e as notas de versão podem dizer exatamente qual parte mudou.

### 39.3 Titularidade

Todo serviço tem uma equipe dona nomeada e um substituto. O CODEOWNERS impõe a revisão. A falta de cobertura de férias bloqueia a versão.

> **Caso sintético — Ashford Batch Plant.** O mapeador do ATT&CK for ICS é um adaptador; atualizar a lista de técnicas é um PR de dados, não uma reescrita.

Na ABP, a página de cada serviço do CNHP nomeia um dono e um substituto como pessoas, não como um alias de equipe. Antes de uma versão, as páginas são conferidas contra o calendário de férias, e uma versão sem cobertura durante a janela seguinte fica retida até que alguém seja treinado.

### 39.4 Erros e limites

Ferramentas órfãs apodrecem em museus de falha aberta.

O adaptador de alarmes por raspagem de tela da ABP é o exemplo que Lena usa: um engenheiro o entendia, ele precisou de onze correções em um ano e falhava em silêncio sempre que a IHM mudava. Uma ferramenta sem dono deixa de receber correções e, quando quebra, ninguém percebe se ela está falhando fechada ou aberta. A regra de Lena é que uma ferramenta sem dono e sem substituto seja adotada por uma pessoa nomeada em até um mês ou aposentada com uma data de exclusão publicada.

### Nota prática

Escreva uma nota de fator ônibus: quem pode publicar versões, quem entende a permit(), quem pode restaurar o repositório lacrado. Se a resposta for uma única pessoa, agende treinamento cruzado antes da próxima temporada.

### 39.1b Planos de descontinuação e de exclusão

Anuncie as descontinuações da API com datas; mantenha períodos de execução dupla. A manutenibilidade inclui saber como aposentar uma ferramenta: exportar os dossiês, revogar as credenciais, arquivar o código. Reserve no calendário um mês anual de atualização de dependências, para que as fixações por CVE não esperem por uma emergência.

As sessões de treinamento cruzado usam os mesmos dados de teste sintéticos do Laboratório I, para que um substituto pratique com as entradas pelas quais a versão será julgada e possa rodar o laboratório sozinho depois.

Lena aplica esse plano a toda ferramenta do CNHP, inclusive ao adaptador substituído. A sua aposentadoria foi anunciada com antecedência.

### Nota de campo — bloqueio por férias

Uma versão foi bloqueada porque a única pessoa que entendia a permit() estava de férias sem um substituto treinado. O treinamento cruzado com os dados de teste do Laboratório I, na semana seguinte, liberou o bloqueio. A manutenibilidade é, sobretudo, sobre as pessoas poderem tirar férias.

Os códigos de motivo descontinuados continuam legíveis pelos consumidores por uma versão completa depois que os produtores deixam de emiti-los.

A data de exclusão é anunciada na página do serviço com pelo menos uma versão de antecedência.

### 39.5 Exemplo resolvido — removendo um adaptador frágil (ABP sintética)

O CNHP tinha um adaptador sob medida que lia a exportação de alarmes do fornecedor da IHM por raspagem de tela. Cada atualização da IHM o quebrava, e só um engenheiro o entendia. A revisão de manutenibilidade de Lena mede a rotatividade (11 correções em um ano), a titularidade (uma pessoa) e o raio de impacto (estatísticas de alarmes de toda a planta). Ela o substitui pela interface de alarmes OPC UA suportada pelo fornecedor, mantém o adaptador somente de leitura por uma versão como contingência, publica uma data de exclusão e escreve o runbook para que um segundo engenheiro possa operar o novo caminho. Menos peças sob medida significam menos falhas silenciosas nas evidências de segurança.

### Exercícios

- **EX115 — Fixação.** Como você fixa o monitor para uma janela e ainda permite correções de segurança? Rubrica: 3 = fixação de versão + mini Laboratório I para a correção urgente; 2 = parcial; 1 = sempre a mais recente; 0 = nada.
- **EX116 — Adaptador.** Um método numa interface StoragePort. Rubrica: 3 = por exemplo, put_evidence(hash,bytes); 2 = vago; 1 = chamada concreta do SDK; 0 = nada.
- **EX117 — Dono.** Linha de titularidade do monitor serial. Rubrica: 3 = equipe + substituto + contato; 2 = equipe; 1 = "o time"; 0 = nada.

### Síntese

Fixações, adaptadores e donos nomeados mantêm as ferramentas vivas com segurança.

<!-- cyberabc:chapter-navigation:start ch-39 -->
### Continue estudando — capítulo 39 de 50

[← Capítulo 38](#ch-38) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 40 →](#ch-40)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem

Você vai (1) verificar o fluxo de ponta a ponta, do quadro ao ticket e à cobertura; (2) injetar falhas; (3) assinar uma versão candidata.

### 40.1 Ponta a ponta

Quadro sintético para decisão do monitor para evento para ticket de constatação para atualização da cobertura. Registre os hashes em cada salto.

No Laboratório II da ABP, Lena reproduz um quadro sintético na bancada e o acompanha por cada etapa: a decisão da função permit com o seu código de motivo, o alerta, a ordem de serviço no sistema de manutenção, o ticket da constatação e a atualização da cobertura. Um hash é registrado em cada salto, para que o dossiê possa provar que o ticket descreve o mesmo evento que o monitor viu. Uma cadeia que não pode ser rastreada salto a salto não conta como aprovada, mesmo quando o resultado final parece certo.

### 40.2 Falhas

Derrube o repositório de constatações no meio do fluxo; confirme que o monitor continua negando e que os rascunhos são enfileirados. Corrompa um arquivo de evidência; confirme o alerta de divergência de hash. Alimente uma lista de arestas plana (insegura); confirme que a alcançabilidade reprova a verificação do SIS.

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

As falhas do Laboratório II de Lena incluem também a perda de energia do coletor, que gerou o alerta de visibilidade degradada em 40 segundos, e 90 segundos de defasagem de relógio na cópia de bancada do PLC-A. Cada falha é injetada separadamente e depois em pares, porque uma falha inofensiva sozinha pode corromper evidências quando combinada com outra.

### 40.3 Aprovação

Checklist da versão candidata assinado pelo implementador e pelo revisor; as linhas de segurança física precisam estar verdes.

> **Caso sintético — Ashford Batch Plant.** O Laboratório II descobriu que a cobertura era atualizada antes da criação do ticket numa nova tentativa — a ordem foi corrigida com um outbox.

Na ABP, a aprovação do Laboratório II lista cada linha com o seu resultado e todo defeito aberto com um dono, como a ordenação errada de eventos causada pela defasagem de relógio. A correção de ordenação de Lena garante que o ticket seja gravado antes que o painel de cobertura seja atualizado, para que uma nova tentativa não possa contar uma constatação que nunca foi registrada.

### 40.4 Erros e limites

Um teste de ponta a ponta sem injeção de falhas só prova o caminho feliz.

A primeira execução de ponta a ponta de Lena na ABP passou em todas as linhas, mas o Laboratório II com falhas injetadas descobriu que a defasagem de relógio desordenava dois eventos no dossiê e que uma nova tentativa atualizava a cobertura antes de o ticket existir. Nenhum dos dois defeitos apareceria numa execução limpa, porque ambos dependem de falhas de tempo que só ocorrem quando algo quebra. A aprovação do Laboratório II exige, por isso, que cada script de falha tenha rodado e que o seu resultado esteja registrado, e uma execução sem falhas é relatada como teste de fumaça.

### Nota prática

Pacote de dados de teste maliciosos: hashes errados, eventos reordenados, timestamps no futuro, grafo plano alegando ser zoneado. Passar só nos dados de teste felizes é um laboratório incompleto.

### 40.1b Observabilidade e paridade

O Laboratório II ativa logs de depuração temporariamente, mas lacra uma cópia redigida. Deixar a depuração ligada nos builds da janela pode vazar segredos. O ambiente do laboratório espelha as versões das ferramentas de produção e as chaves de assinatura das políticas (chaves de teste). Um Laboratório II instável é um bloqueio, não um ritual de tentar de novo até ficar verde.

Um script de falha que não consegue rodar é registrado como linha reprovada, não pulado. Os scripts de injeção de falhas ficam na pasta do laboratório e são fixados por SHA no relatório. As lacunas de paridade de ambiente explicam as surpresas de "verde no laboratório, vermelho na janela".

A aprovação de Lena procura lacunas de paridade.

### Nota de campo — pacote malicioso

O pacote malicioso do Laboratório II incluía um grafo plano rotulado como zoneado. A verificação de alcançabilidade falhou de forma fechada e bloqueou a versão. Laboratórios só de caminho feliz publicam mentiras.

Lacre os logs do Laboratório II com a mesma ferramenta de manifesto que o dossiê usa, para que os estudantes pratiquem um único fluxo de hashes.

Testes instáveis são postos em quarentena e corrigidos; publicar com um "às vezes falha fechado" é publicar falha aberta.

### 40.5 Exemplo resolvido — injeção de falhas de ponta a ponta (ABP sintética)

O Laboratório II exercita a cadeia completa na bancada: tráfego reproduzido → função permit → alerta → ordem de serviço no sistema de manutenção → dossiê. Falhas injetadas: perda de energia do coletor, defasagem de relógio de 90 segundos no PLC-A, um evento malformado e um acúmulo na fila de mensagens mortas. Resultados: a perda de energia gerou "visibilidade degradada" em 40 s; a defasagem de relógio foi detectada pela verificação da fonte de tempo, mas desordenou dois eventos no dossiê até que a correção de deslocamento fosse aplicada; o evento malformado chegou à fila de mensagens mortas; o acúmulo foi esvaziado em 7 minutos. A aprovação lista a desordenação como um defeito aberto, com dono.

### Exercícios

- **EX118 — Ordenação.** Por que criar o ticket antes de a contagem de cobertura aumentar? Rubrica: 3 = a cobertura precisa refletir constatações registradas; 2 = vago; 1 = qualquer ordem; 0 = nada.
- **EX119 — Falha.** Comportamento esperado do monitor quando o repositório de constatações está fora do ar. Rubrica: 3 = continua avaliando/negando; enfileira rascunhos; 2 = parcial; 1 = falha aberta; 0 = nada.
- **EX120 — Aprovação.** Duas assinaturas exigidas — de quem? Rubrica: 3 = implementador + revisor independente; 2 = uma; 1 = só o gerente; 0 = nada.

### Síntese

Ponta a ponta com falhas; segurança física verde; duas assinaturas.

<!-- cyberabc:chapter-navigation:start ch-40 -->
### Continue estudando — capítulo 40 de 50

[← Capítulo 39](#ch-39) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 41 (inglês) →](../../en/book/MANUSCRIPT.md#ch-41)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX150. A Ashford Batch Plant, Lena Okafor, o CNHP e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação. Esta edição parcial traz as resoluções de EX001–EX120; as de EX121–EX150 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

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

**EX031.** Exemplo: CRC/enquadramento serial exige um monitor serial no tronco; o código de função do Modbus TCP exige captura/decodificação IP no conduto; saber qual operador mudou um setpoint exige um log de auditoria da IHM ou da aplicação. Outras trincas corretas são aceitas.

**EX032.** Decodificação somente leitura do Modbus TCP até o PLC-A a partir da HMI-1/do HIST-1; apenas os códigos de função 3/4/6; registradores 40001-40010; nenhuma escrita a partir da estação de avaliação; janela sábado 02:00-04:00, com o contato de segurança de processo de plantão.

**EX033.** WRITE_REGS permite à HMI-1 fc=6 apenas para registradores em range(40001, 40011). 40003 está dentro (PASS); 40050 está fora (BLOCK register-out-of-range).

**EX034.** Contas nominais de engenheiro; direitos de administrador por meio de associação a um grupo retirada com prazo; todos os downloads de lógica registrados; uma segunda pessoa aprova os downloads para o SIS e para o CLP de produção fora de uma janela.

**EX035.** O patch do banco de dados do historiador (2,5 h, risco 5) foi adiado — a W1 levou o firmware do PLC-A e o firmware do switch; a W2 levou o SO da IHM e o antivírus da eng-WS; não sobraram horas.

**EX036.** USB de fornecedor permitido apenas na eng-WS-2, 14 de março, 09:00-12:00, mídia verificada num quiosque isolado, sessão gravada em vídeo; porta desabilitada depois.

**EX037.** Usar apenas a réplica do L3. SELECT limitado a tag, valor e timestamp. LIMIT 10000. Sem dumps. Arquivos destruídos em até 24 h, com confirmação no ticket.

**EX038.** Obter as credenciais de analista emitidas para o teste; conectar; tentar um UPDATE/INSERT numa tabela de anotações de setpoints; registrar sucesso ou permissão negada. Nenhum payload elaborado.

**EX039.** Seguros: tag_id, value, quality_code, timestamp. Proibidos: operator_name, customer_order_id, recipe_secret_key.

**EX040.** Lista de permissões Modbus abp-modbus-v1.4.2 (SHA do git c0ffee1), carregada em 14 de março às 02:05 a partir do bucket de versões assinadas.

**EX041.** Todo PR que alarga condutos (aresta ou código acrescentado, ou bloqueio removido) precisa de um ticket AUTH vinculado e de um segundo dono de código; restringir exige um dono.

**EX042.** Uma integração contínua com credenciais da VPN da planta tocaria sistemas fora de uma janela autorizada por uma pessoa, poderia vazar segredos nos logs e faria as builds dependerem das redes da planta. Os dados de teste sintéticos mantêm a integração contínua segura e repetível.

**EX043.** Confidencialidade: pouco impacto direto (escritas de setpoint não são leituras). Integridade: mudança não autorizada do setpoint de nível do T-1. Disponibilidade: o lote pode ser abortado ou intertravado. Segurança física: o nível muito alto do SIS-B continua independente se os condutos se mantiverem — declare isso explicitamente.

**EX044.** Vulnerabilidade: escrita Modbus não autenticada. Exposição: gravável a partir da rede de IHMs do L2. Risco de processo: o julgamento do dono da planta sobre a probabilidade e a consequência de um transbordamento, dado o SIS-B — aceito ou remediado por ele.

**EX045.** Não publicamos uma pontuação única de "hackeabilidade". Aqui estão: alcançabilidade do SIS (não), críticas abertas (1), alarmes por hora de operador (1,05), correções de alto risco adiadas (0).

**EX046.** "Nenhum host do L4 deverá ter um conduto permitido até os servidores SCADA do L2; verificar por alcançabilidade em cada exportação do firewall." "Toda visualização de dados de processo a partir do L4 deverá usar a réplica do historiador no L3.5; verificar pela ausência de regras diretas do L4 para o L2 e por testes das ACLs da réplica."

**EX047.** Artefato: a lista de arestas zoneada, sem L2 para L1-SIS e sem L4 para L2. Sinal: o lab_reach relata writes_to_SIS=True ou o L1-SIS no alcance a partir do L4.

**EX048.** Nome/id da tag, tipo de dado e unidades de engenharia, taxa de atualização ou de exceção, significado do código de qualidade, dono — quaisquer três com significado claro.

**EX049.** kp=0.2 ki=0.01: final≈58,15, mae≈4,62, o melhor dos três. O P puro (ki=0) deixa um desvio maior (final≈44,61).

**EX050.** Prefira um tap passivo ou espelhamento; a DPI em linha arrisca acrescentar uma latência comparável à escala de tempo da malha. Meça primeiro numa cópia de bancada.

**EX051.** Acionar imediatamente para eventos cibernéticos relevantes para a segurança física; agrupar os eventos médios num resumo do turno; suprimir duplicatas da mesma impressão digital por 24 h.

**EX052.** PC do escritório no L4; historiador no L3; IHM no L2; PLC-A no L1; SIS-B no L1-segurança. Controles: salto pela DMZ para a visualização a partir do L4; nenhuma aresta do L2 para o SIS; lista de permissões no Modbus — qualquer esboço coerente com dois controles.

**EX053.** Os dados da receita saem do caminho controlado de TO/TI para uma conta pessoal não autorizada, quebrando a confidencialidade e a retenção.

**EX054.** Os testes usaram um ambiente sintético que espelha a configuração da ABP; os resultados sustentam afirmações sobre essa configuração sob a permissão de trabalho, não sobre o comportamento do processo real nem sobre dados de produção.

**EX055.** Contas nominais ou compartilhadas? Locais ou do diretório? Membros do grupo de administradores? Última troca de senha? Procedimento de quebra de vidro? Gravação de sessões nos hosts de salto?

**EX056.** Reexportar do dispositivo ou restaurar a cópia lacrada; reverificar os hashes; verificar quem escreveu depois do horário do lacre; abrir uma constatação de processo sobre edições não controladas.

**EX057.** Os segredos da planta e de engenharia nunca são colados em tickets, no chat ou no git; os tickets guardam apenas um id de referência do cofre e o horário da última rotação.

**EX058.** Exemplo: orientação de segurança de ICS para a SP 800-82; zonas/condutos/SL para a 62443; vocabulário de técnicas para o ATT&CK ICS; detalhes dos códigos de função para o Modbus Application Protocol.

**EX059.** Projetar e operar um programa autorizado de endurecimento da rede de controle que imponha zonas e listas de permissões, meça a detecção com honestidade e nunca ponha em risco a segurança de processo nem exceda a permissão de trabalho assinada.

**EX060.** Exploits funcionais para CLPs; varredura de plantas em operação sem permissão de trabalho; exportação da genealogia proprietária de lotes para os laboratórios; desativação do SIS para facilitar um teste.

**EX061.** Funcional: "Nenhuma exportação do firewall deverá conter um caminho do L4 para o L1-SIS; verificar pela alcançabilidade na integração contínua." Segurança física: "Se a política não puder ser carregada, o ponto de imposição deverá negar novas sessões e alarmar em até 30 s."

**EX062.** Dado o caminho da lista de permissões configurado, mas o arquivo ausente; Quando houver qualquer chamada a permit(); Então o resultado é DENY com o motivo policy-unavailable e um alerta dispara; nenhum quadro de escrita é encaminhado.

**EX063.** Conflito: os operadores querem visualização direta do L4 para o L2; a segurança física e a da informação não querem nenhuma aresta do L4 para o L2. Regra escolhida: visualização apenas pela réplica do historiador no L3.5; regra direta proibida; quebra de vidro documentada à parte.

**EX064.** Edições no lugar apagam quais condutos estavam em vigor no momento t; o versionamento permite que uma constatação aponte para o conjunto de regras autorizado quando a observação foi feita.

**EX065.** Recalcular o hash detecta mudanças; arquivos idênticos se fundem; os tickets referenciam bytes imutáveis.

**EX066.** Rejeitar títulos que casem com padrões de atribuição de senha ou com segredos de alta entropia; os revisores ainda conferem; apenas referências ao cofre nos metadados da evidência.

**EX067.** Implantar com o caminho da lista de permissões apontando para uma montagem vazia; chamar permit(); esperar DENY policy-unavailable e um alerta; nenhum quadro encaminhado.

**EX068.** Todo evento de negação guarda o id do ator autenticado e a versão da política; o armazenamento é somente de acréscimo; exclusões exigem quebra de vidro com controle duplo.

**EX069.** O STRIDE do programa protege a integridade da avaliação e a segurança de processo; módulos de exploit aumentam o dano de uso dual e violam a fronteira do curso — não são mitigações.

**EX070.** Nome: decodificação Modbus somente de escuta. Propósito: verificar as decisões da lista de permissões. Privilégio: acesso ao tap, sem injeção. Ruidoso: baixo. Impacto: apenas latência. Parada: tempo de ciclo >50 ms ou alarme de processo. Artefatos: tabela de decisões, hash de configuração, log de tempo de ciclo.

**EX071.** Ações sem uma permissão de trabalho assinada não são autorizadas; é uma falha legal, ética e de segurança de processo, qualquer que seja a intenção.

**EX072.** Hash do diagrama de zonas atualizado; relatório de alcançabilidade; hash da exportação do firewall; rascunhos de constatações ou um explícito "nenhuma encontrada", com nota de cobertura.

**EX073.** Arquivo JSON assinado: risco = os operadores esquecerem de assinar ou de verificar. Política embutida no código: risco = reimplantações a cada mudança da lista de permissões, deriva entre dispositivos.

**EX074.** As decisões de negação em códigos de função de escrita alertam de forma síncrona antes do encaminhamento, para que as condições de parada cumpram a meta do sensor; as leituras permitidas podem ser enfileiradas de forma assíncrona.

**EX075.** Ele falha de forma fechada? Quem pode publicar a política? Qual é a latência acrescentada no tronco mais lento?

**EX076.** Critério: o estado do SIS nunca sai do L1 sem a chave seletora. A alta, se os monitores ficarem locais; B média, se a réplica excluir o SIS; C baixa, se os uploads incluírem tags de segurança física.

**EX077.** Opção C rejeitada: dados de processo e próximos às receitas sairiam da fronteira de residência do site exigida pela política da ABP e pela cláusula de dados da permissão de trabalho.

**EX078.** Quando a WAN do site cai ou o caminho para a nuvem está fora da permissão — rodar apenas as listas de permissões e os detectores locais, com registro manual das constatações.

**EX079.** Preventivo: bucket lacrado somente de acréscimo, com IAM de escrita única. Detectivo: rotina agendada que recalcula os hashes e alerta em caso de divergência.

**EX080.** Exige competência de uso dual, não é determinístico e pode ferir o processo; prefira reler a configuração ou testar a lista de permissões.

**EX081.** (HIST-1, 16) não está em ALLOW, então BLOCK fc-not-allowed — os historiadores não podem escrever múltiplos registradores.

**EX082.** permit(source, fc, register, allow_list: AllowListVersion) -> (bool, Reason). A AllowListVersion fixa quais regras foram avaliadas, para a auditoria.

**EX083.** O teste que afirma BLOCK register-out-of-range para HMI-1 fc=6 reg=40050.

**EX084.** Segredos de autenticação; quadros brutos que embutem parâmetros proprietários de receitas; identificadores pessoais de operadores, se não forem necessários para a decisão.

**EX085.** cobertura = |observadas ∩ planejadas| / |planejadas|. Usar todas as técnicas do ATT&CK for ICS como denominador faz a cobertura parecer minúscula ou estimula um planejamento lixo — planeje as técnicas pertinentes ao trabalho.

**EX086.** Na classe A, o CUSUM detecta 60/60 com atraso de ~25 amostras; a banda detecta 0/60; os dois mostram 0/60 alarmes falsos neste conjunto de sementes.

**EX087.** O status fica aberto até que um ticket de novo teste passe; o encerramento automático com base na promessa do fornecedor é proibido.

**EX088.** ID V-04; preparação: montagem vazia da lista de permissões; ação: permit(qualquer escrita); esperado: DENY policy-unavailable + alerta; evidência: hash do log.

**EX089.** Interromper o laboratório, abrir um bloqueio, revogar a aprovação da janela na planta até a correção e um novo laboratório aprovado.

**EX090.** Hash do arquivo da lista de permissões/política, hash do build/versão do monitor, hash do log de resultados.

**EX091.** Uma nova tentativa de rede pode criar duas constatações com ids de servidor diferentes; os clientes devem fazer PUT com ids conhecidos.

**EX092.** {"title":"x","payload":"..."} ou {"password":"..."} ou {"risk_score":42} — qualquer campo proibido/desconhecido segundo a política.

**EX093.** Não — renomear quebra os clientes; mantenha reason_code na v1 ou publique a /v2/.

**EX094.** Durante as janelas assinadas, sucesso do caminho de negação ≥ 99,5%, medido por sondagens sintéticas a cada minuto; as indisponibilidades acionam o líder.

**EX095.** A avaliação do escopo e da lista de permissões — precisa falhar de forma fechada, nunca ALLOW na incerteza.

**EX096.** Parar de iniciar novos métodos de descoberta; acionar o líder; manter a negação/permissão funcionando; esvaziar a fila antes de retomar a descoberta.

**EX097.** Criar o arquivo /var/lib/otmon/STOP via SSH/SSO; o monitor o consulta a cada 10 s; se ele existir ou estiver ilegível, negar as escritas e alertar.

**EX098.** Binário assinado anterior disponível; AllowListVersion inalterada ou reverificada; contato de segurança de processo notificado da reversão.

**EX099.** Às 02:40, o tempo de ciclo no tronco A marca 62 ms durante três minutos; o líder está numa área barulhenta, com rádio instável.

**EX100.** Para que os revisores saibam qual AllowListVersion autorizou a decisão quando o evento disparou.

**EX101.** O consumidor guarda os event_ids processados; as duplicatas são ignoradas ou recebem upsert sem novos tickets.

**EX102.** Um JSON de evento de exemplo para o novo motivo e os campos esperados do ticket no repositório de constatações depois do consumo.

**EX103.** Fração das técnicas planejadas do ATT&CK for ICS observadas nesta janela — não é uma pontuação de risco residual nem de conformidade.

**EX104.** Não publicamos selos de risco vermelho/âmbar/verde; use a alcançabilidade do SIS, as críticas abertas e as contagens de SLA/adiamento de correções.

**EX105.** technique_id, nome, planejada (S/N), observada (S/N), first_seen_utc, notas.

**EX106.** bytes por ciclo=244; tempo por ciclo≈21,2 ms a 115200, com 10 bits/byte.

**EX107.** Cerca de 29 ms de folga absorvem picos de decodificação e novas tentativas; gastá-la toda não deixa margem para que a condição de parada tenha sentido.

**EX108.** Cada um pode enviar 2/s → ~6/s no agregado, o triplo da permissão — é preciso um limitador compartilhado.

**EX109.** Desativar as contas temporárias; trocar os segredos do cofre; lacrar os hashes das evidências; exportar as métricas de cobertura/alcançabilidade do SIS; confirmar o kill switch liberado; agendar a retrospectiva; notificar a segurança de processo do horário de término.

**EX110.** Ids e status das constatações abertas; último event_id processado; pedidos de aprovação pendentes; estado do kill switch — quaisquer três ou mais.

**EX111.** A correção do banco de dados do historiador foi adiada; o encerramento precisa registrar o risco residual e a data da próxima janela agendada (não adiada para sempre).

**EX112.** Exportar as regras atuais do firewall; rodar a alcançabilidade a partir do L4; esperar que o L2/L1-SIS não sejam alcançáveis indevidamente; guardar os hashes; não enviar tráfego para a planta para prová-lo.

**EX113.** Do contrário, as métricas mentem e os painéis ficam verdes enquanto o risco permanece.

**EX114.** O novo teste confirmou apenas a configuração da bancada/do gêmeo; o ambiente de execução da planta ficou fora do escopo da validação.

**EX115.** Fixar a versão exata para a janela; correções de emergência precisam de um mini laboratório de verificação (Capítulo 30) antes da troca.

**EX116.** put_evidence(key: Hash, body: bytes) -> None / get_evidence(key) -> bytes.

**EX117.** Dono: equipe CNHP Platform (primária: Lena Okafor); substituto: engenheiro de TO de plantão; contato: #cnhp-monitors.

**EX118.** Do contrário, a cobertura alega técnicas observadas sem um registro durável de constatação — a métrica mente sob falha parcial.

**EX119.** Continua permitindo/negando a partir da política local; enfileira os rascunhos; alerta sobre o crescimento da fila; nunca ALLOW em erros de política.

**EX120.** O implementador da mudança e um segundo engenheiro que não escreveu o código.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; os frameworks mudam, então verifique de novo.

- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series overview. <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS. <https://attack.mitre.org/matrices/ics/>
- Modbus Application Protocol V1.1b3. <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
