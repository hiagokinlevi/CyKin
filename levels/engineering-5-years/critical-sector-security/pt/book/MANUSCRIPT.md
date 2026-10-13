# Infraestrutura Crítica e Segurança Setorial: Engenharia de Sistemas Seguros e Resilientes

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado (curso 138 de 207 na [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–5 de 50 já estão escritos em português, com os exercícios EX001–EX010 e suas resoluções; os capítulos 6–50 (EX011–EX100) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: futuros projetistas de sistemas de segurança para serviços críticos — água, eletricidade, saúde, transporte, finanças e comunicações. Conhecimento de entrada: matemática e física do ensino médio; o livro constrói cálculo, probabilidade, programação, redes e engenharia de sistemas a partir do Capítulo 1.
- Relação com os demais livros desta área: o [livro de mestrado](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) ensina a projetar, pilotar e defender um estudo empírico com revisão ética; o [livro de doutorado](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) exige uma contribuição original e validada de forma independente para o conhecimento. **Este livro de engenharia trata de construir coisas**: derivar requisitos a partir de consequências, escolher arquiteturas, implementar e verificar controles, medir confiabilidade e desempenho, ensaiar a recuperação e defender um sistema projetado com evidências. Seu capítulo de pesquisa (42) existe para resolver decisões de projeto, não para publicar.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de propriedade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: este curso é um projeto educacional independente. Não é um diploma de engenharia credenciado, não concede habilitação profissional e não concede autorização para acessar, varrer, testar ou modificar nenhuma infraestrutura real. Toda organização, instalação, dispositivo, endereço, pessoa e número de um exemplo resolvido é **sintético**, salvo quando uma frase cita explicitamente uma fonte pública. Nada aqui é um procedimento operacional para uma concessionária, um hospital ou um operador reais, e nada é aconselhamento jurídico.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão do livro](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os cinquenta capítulos acompanham os dez semestres do plano. Os **capítulos 1–10** constroem os fundamentos matemáticos, físicos, computacionais e profissionais, cada um aplicado a um problema de infraestrutura desde a primeira página. Os **capítulos 11–19** cobrem redes, sistemas operacionais, dados, engenharia de software, fundamentos de segurança, engenharia de sistemas, controle, arquitetura de segurança, e identidade e criptografia. O **Capítulo 20** estabelece o contexto setorial. Os **capítulos 21–42** são o núcleo da área: requisitos, modelos, análise de ameaças e de falhas, métodos, arquiteturas, controles, implementação, medição, confiabilidade, segurança operacional e resiliência, integração, desempenho, operações, validação, manutenibilidade, otimização e pesquisa aplicada, com dois ateliês de projeto (25, 35) e dois laboratórios de verificação (30, 40). Os **capítulos 43–50** são a prática e a sequência do projeto final: estágio, projeto final, revisão independente, ensaio de falha e recuperação, dossiê de evidências, trabalho de conclusão e defesa.

Todo capítulo tem objetivos de aprendizagem, seções didáticas com definições, um exemplo resolvido, uma atividade prática, erros comuns e limites, dois exercícios e uma síntese. Dezessete capítulos incorporam um laboratório offline escrito para a biblioteca padrão do Python 3; as saídas impressas foram produzidas executando o código. Escreva sua resposta antes de abrir as [resoluções](#worked-results).

Mantenha quatro rótulos nas suas anotações de engenharia: **requisito** (o que deve ser verdadeiro, de forma verificável), **decisão de projeto** (o que foi escolhido, por quê e o que a mudaria), **evidência** (teste, análise, ensaio ou revisão que sustenta uma afirmação, com sua versão) e **risco residual** (o que resta e quem é seu dono). A falha mais comum no nível de engenharia não é um cálculo errado; é uma afirmação que nenhuma evidência sustenta, ou um risco residual que ninguém assume.

### O caso de projeto sintético usado neste livro

O livro acompanha um único programa inventado, dos primeiros princípios até a defesa final.

| Elemento sintético | Papel | Limite |
|---|---|---|
| **Lowmarsh Regional Water Authority (LRWA)** — estação de tratamento de água de Fenwick, estações de bombeamento PS1–PS6, o reservatório de distribuição de Hollin Hill, de 4.000 m³, uma sala de controle e servidores SCADA, telemetria por LTE privada, 42 estações de campo | O sistema que está sendo projetado | Concessionária inventada; nenhuma instalação, rede ou equipe real |
| **St Brenna's Hospital** | Cliente crítico abastecido por Hollin Hill (via PS3) e diretamente pela PS4; cerca de 4 h de reservação própria | Inventado |
| **Telemetry Modernisation and Resilience Programme (TMRP)** | O programa de projeto; necessidades N1–N4 e requisitos R1–R9 (capítulos 16 e 21) | Inventado |
| Alimentadores da rede elétrica F1 e F2, a operadora de LTE, fornecedores de RTU (RTU-A legada, RTU-B nova) | Dependências e fornecedores | Inventados; nenhum produto real é descrito |
| Todos os endereços (10.x.x.x), chaves, probabilidades, custos e saídas de laboratório | Dados didáticos | Sintéticos; a chave de demonstração do Laboratório 8 é pública e nunca deve ser usada |

### Política de fontes

Toda afirmação factual sobre uma lei, uma norma, um incidente ou um estudo publicado tem link para uma fonte consultada em outubro de 2026. Leis e normas mudam: verifique de novo versões e datas antes de se apoiar nelas. Conhecimento padrão de engenharia (a lei de Ohm, a lei de Little, a definição de derivada) é apresentado sem citação ou com uma referência clássica. Incidentes são descritos apenas no nível de suas fontes públicas citadas, e, quando um relato inicial foi revisto (Oldsmar), ambos são citados. Normas pagas (IEC 62443, IEC 61508) são citadas por suas páginas públicas de catálogo ou de visão geral; não cite cláusulas que você não leu.

## Sumário

1. [Cálculo I](#ch-01)
2. [Matemática discreta](#ch-02)
3. [Física para computação](#ch-03)
4. [Programação I](#ch-04)
5. [Comunicação em engenharia](#ch-05)

Capítulos 6–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-06), até a chegada dos próximos lotes.

As [resoluções](#worked-results) contêm EX001–EX010. Um [glossário](#glossary) e as [referências](#references) fecham o livro.


<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) ler uma taxa de variação como a grandeza física que um operador acompanha — metros cúbicos por hora saindo de um reservatório, megawatts subindo num alimentador; (2) calcular uma derivada e uma integral definida para as curvas suaves de demanda usadas no planejamento de infraestrutura; (3) resolver problemas do tipo "quanto tempo até…" integrando uma taxa e encontrando o instante em que a quantidade acumulada atinge um limite; e (4) explicar por que o atalho da taxa média pode superestimar o tempo de autonomia. O capítulo inicia o caso de projeto do livro e prepara o Capítulo 6, em que o mesmo reservatório se torna uma equação diferencial com vazão de entrada e controle.

### 1.1 Por que um engenheiro de infraestrutura precisa de cálculo

Serviços críticos são estoques e fluxos. Um reservatório é um estoque de água tratada; bombas e consumidores são fluxos. Um banco de baterias é um estoque de energia; a carga é um fluxo. O tanque de combustível de um hospital, o empacotamento de uma linha de gás, uma fila de mensagens de telemetria não processadas: cada um é uma quantidade que varia a uma taxa. As perguntas de segurança e de resiliência são quase sempre perguntas sobre essas quantidades sob estresse. *Se as bombas param porque sua rede de controle caiu, quantas horas de abastecimento restam?* *Se um atacante consegue manter uma válvula aberta, com que rapidez o nível sobe?* A resposta nunca é um único número tirado de uma folha de dados; é a integral de uma taxa ao longo do tempo, comparada com um limite que importa para as pessoas.

A derivada $dV/dt$ é a taxa instantânea com que uma quantidade $V$ varia. Se $V(t)$ é o volume de um reservatório em metros cúbicos e $t$ está em horas, $dV/dt$ está em m³/h. A integral definida $\int_a^b q(t)\,dt$ de um fluxo $q$ é a quantidade total movimentada entre os instantes $a$ e $b$. O **teorema fundamental do cálculo** liga as duas: se $V' = -q$, então $V(b) - V(a) = -\int_a^b q(t)\,dt$. Todo cálculo de autonomia neste livro é essa frase aplicada a um estoque real.

### 1.2 Derivadas que você vai usar

Você precisa de um pequeno conjunto de ferramentas: a derivada de um polinômio ($d/dt\, t^n = n t^{n-1}$), da exponencial ($d/dt\, e^{kt} = k e^{kt}$), do seno e do cosseno ($d/dt \sin(\omega t) = \omega\cos(\omega t)$), as regras do produto e da cadeia, e a ideia de ponto estacionário, em que $f'(t) = 0$. A demanda diária de uma rede de água costuma ser aproximada por uma média mais uma senoide com período de 24 horas. Se $d(t) = 150 + 60\sin(2\pi t/24)$ m³/h, então $d'(t) = 60\cdot(2\pi/24)\cos(2\pi t/24) \approx 15.7\cos(2\pi t/24)$ m³/h², de modo que a demanda sobe mais depressa — cerca de 15,7 m³/h a cada hora — quando o cosseno vale 1. Essa inclinação importa para um controlador de bombas: se as bombas só conseguem acelerar a 10 m³/h², elas ficarão atrás da demanda no seu trecho mais íngreme.

### 1.3 Integrais e quantidades acumuladas

A antiderivada da demanda acima é $D(t) = 150t - \frac{60\cdot 24}{2\pi}\cos(2\pi t/24) + C$. A água retirada do instante 0 até $T$ é $D(T) - D(0) = 150T - \frac{1440}{2\pi}(\cos(2\pi T/24) - 1)$. Observe o que a senoide faz: ao longo de um dia inteiro ela se cancela, então o total diário é simplesmente $150 \times 24 = 3600$ m³; mas ao longo de parte de um dia ela não se cancela, e *quando* a interrupção começa muda quanto tempo o estoque dura. Para responder "quando o reservatório atinge seu nível mínimo seguro?", iguale o volume retirado ao volume utilizável e resolva para $T$. A maioria dessas equações não tem solução em forma fechada, então os engenheiros as resolvem numericamente. A **bissecção** divide ao meio um intervalo que sabidamente contém a resposta até que ele fique pequeno o bastante; é lenta, mas não pode falhar se a função for contínua e o intervalo inicial contiver a raiz.

### 1.4 Exemplo resolvido: autonomia de Hollin Hill (sintético)

**Este caso é sintético.** O livro acompanha a inventada **Lowmarsh Regional Water Authority (LRWA)**, que opera a estação de tratamento de água de Fenwick, seis estações de bombeamento (PS1–PS6) e o reservatório de distribuição de Hollin Hill, de 4.000 m³, que abastece, entre outros clientes, o St Brenna's Hospital. A LRWA está iniciando um **Telemetry Modernisation and Resilience Programme (TMRP)**, um programa de modernização e resiliência da telemetria; você faz parte da equipe de engenharia. Suponha que uma falha na rede de telemetria pare as bombas que alimentam Hollin Hill às 06:00 (t = 0), quando o reservatório contém 3.400 m³ (85%). A política de operação trata 20% (800 m³) como o piso abaixo do qual a pressão e as reservas para combate a incêndio ficam em risco. A demanda é a $d(t)$ acima, com t = 0 às 06:00. O volume utilizável é de 2.600 m³. Um planejador que divide pela demanda média obtém 2.600/150 = 17,3 horas. Integrar a curva real dá cerca de **14,6 horas**, porque a interrupção começa quando a demanda sobe para o pico da manhã e do meio-dia. A diferença de 2,7 horas não é arredondamento; é a diferença entre despachar a tempo uma equipe com gerador e não despachar.

### 1.5 Atividade prática: Laboratório 1

Execute o laboratório com a biblioteca padrão do Python 3. Ele encontra o instante exato por bissecção, compara a integração passo a passo pelo método de Euler explícito com três tamanhos de passo e imprime a estimativa pela taxa média.

```python
# Lab 1 - how long does Hollin Hill reservoir last after the pumps stop? (synthetic, offline)
import math
V0, VMIN = 3400.0, 800.0          # m3: start at 85% of 4000, alarm floor at 20%
def demand(t):                     # m3/h, t in hours after the pumps stop (t=0 is 06:00)
    return 150.0 + 60.0 * math.sin(2 * math.pi * t / 24)
def drawn(t):                      # exact integral of demand from 0 to t
    return 150.0 * t - (60.0 * 24 / (2 * math.pi)) * (math.cos(2 * math.pi * t / 24) - 1)
lo, hi = 0.0, 48.0
for _ in range(60):                # bisection on drawn(t) = V0 - VMIN
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if drawn(mid) < V0 - VMIN else (lo, mid)
print(f"exact time to 20%: {lo:.2f} h")
for dt in (1.0, 0.1, 0.01):        # forward Euler
    v, t = V0, 0.0
    while v > VMIN:
        v -= demand(t) * dt; t += dt
    print(f"Euler dt={dt:<5} reaches 20% at {t:.2f} h")
print(f"constant-average model (150 m3/h): {(V0 - VMIN) / 150:.2f} h")
print(f"dV/dt at t=6 h: {-demand(6):.1f} m3/h")
```

Saída esperada:

```text
exact time to 20%: 14.62 h
Euler dt=1.0   reaches 20% at 15.00 h
Euler dt=0.1   reaches 20% at 14.70 h
Euler dt=0.01  reaches 20% at 14.63 h
constant-average model (150 m3/h): 17.33 h
dV/dt at t=6 h: -210.0 m3/h
```

O método de Euler com passo de uma hora superestima o tempo em cerca de 0,4 h; com 0,01 h ele concorda com a resposta exata até a segunda casa decimal. A derivada em t = 6 h é −210 m³/h: o esvaziamento mais rápido da janela.

Antes de confiar no laboratório, verifique se seus números concordam com o exemplo resolvido: o instante exato deve coincidir com a autonomia integrada de Hollin Hill, e a linha da taxa média deve reproduzir a estimativa mais longa do planejador. Se você mudar o horário de início, mantenha o piso em 800 metros cúbicos para que a comparação continue justa. Um resultado que só aparece com um tamanho de passo é uma propriedade do método, não do reservatório.

### 1.6 Erros comuns e limites

- Usar uma taxa média para um fluxo variável no tempo ao longo de menos de um ciclo completo.
- Misturar unidades (litros por segundo contra metros cúbicos por hora: 1 L/s = 3,6 m³/h).
- Ignorar que o volume "utilizável" exclui o volume morto e as reservas.
- Confiar num método numérico sem compará-lo com um passo menor ou com um caso exato.
- Tratar o modelo de demanda como fato. Uma senoide é uma aproximação de planejamento; a demanda real tem efeitos de dia da semana, de clima e de eventos, e a demanda durante uma emergência pode cair (avisos de economia) ou subir (pessoas armazenando água).

### Exercícios — capítulo 1

**EX001 — Inclinação de pico.** *Objetivo:* usar uma derivada para comparar a demanda com os limites dos equipamentos. *Entradas:* $d(t)$ da §1.2; bombas que conseguem acelerar no máximo 12 m³/h por hora. *Passos:* (1) encontre $d'(t)$; (2) encontre seu máximo e o horário em que ocorre, se t = 0 é 06:00; (3) decida se as bombas conseguem acompanhar a demanda em todos os instantes. *Evidência esperada:* a dedução e uma conclusão de engenharia em uma frase. *Rubrica:* 3 = derivada, máximo e horário corretos, e conclusão que liga a inclinação ao limite de aceleração; 2 = um deslize; 1 = apenas a derivada; 0 = nada.

**EX002 — Autonomia com outro horário de início.** *Objetivo:* mostrar que o horário de início importa. *Entradas:* Laboratório 1. *Passos:* altere a demanda para que a interrupção comece às 18:00 (substitua `sin(2πt/24)` por `sin(2π(t+12)/24)`), execute de novo e compare com o resultado das 06:00 e com a estimativa pela taxa média. *Evidência esperada:* três números e uma recomendação de 100 palavras sobre qual valor um plano de emergência deve citar. *Rubrica:* 3 = números corretos e recomendação de planejar pelo pior horário de início plausível, com o motivo; 2 = números certos, recomendação fraca; 1 = não executado; 0 = nada.

### Síntese do capítulo

Infraestrutura é feita de estoques e fluxos. Uma derivada é uma taxa que você pode comparar com o que os equipamentos conseguem fazer; uma integral é uma quantidade que você pode comparar com um limite que protege pessoas. O tempo de autonomia é uma integral resolvida para seu limite superior, geralmente de forma numérica, e depende de quando a perturbação começa. Confira os resultados numéricos contra uma solução exata ou mais fina, mantenha as unidades explícitas e nunca deixe uma média ocupar o lugar de uma curva quando é a curva que a interrupção vai encontrar.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) escrever condições de intertravamento e de permissão como expressões booleanas e verificá-las exaustivamente com uma tabela-verdade; (2) modelar dependências de infraestrutura como um grafo dirigido e calcular o que falha quando um nó falha; (3) usar conjuntos, relações e contagem para limitar quantos estados um sistema de controle pode assumir; e (4) dizer com precisão quando uma verificação exaustiva é viável e quando não é. O capítulo se apoia na visão de estoques e fluxos do Capítulo 1 e prepara o Capítulo 4, em que você vai implementar esses modelos em código.

### 2.1 A lógica é a linguagem das permissões

Sistemas de controle estão cheios de regras da forma "a bomba só pode funcionar se…". Escreva-as como expressões booleanas. Seja $H$ = nível acima do limite alto, $S$ = pressão de sucção baixa, $P$ = permissão remota presente, $M$ = modo manual local selecionado. Uma regra típica é $\text{RUN} = \neg H \wedge \neg S \wedge (P \vee M)$. Duas regras são equivalentes se concordam em todas as entradas; as leis de De Morgan ($\neg(A\wedge B) = \neg A \vee \neg B$) permitem reescrever condições de desarme como permissões. Com quatro entradas há $2^4 = 16$ estados, e uma tabela-verdade verifica cada um deles. A engenharia de segurança acrescenta uma pergunta que a engenharia de segurança operacional já faz: *em que entrada um atacante pode influir?* Se $P$ chega por uma rede, então $P \vee M$ significa que uma permissão forjada basta para ligar a bomba sempre que $H$ e $S$ forem falsos. Isso pode ser aceitável — os desarmes físicos continuam valendo — ou não, se funcionar naquele momento causar um transiente de pressão.

### 2.2 Grafos modelam dependência

Um **grafo dirigido** $G = (V, E)$ tem nós e setas. Desenhe uma seta de $a$ para $b$ quando $a$ precisa de $b$ para funcionar. O conjunto do que é afetado quando $b$ falha é tudo o que consegue chegar a $b$ seguindo as setas — seus **ancestrais** nessa orientação. A busca em largura calcula esse conjunto em tempo proporcional ao número de arestas. [Rinaldi, Peerenboom and Kelly (2001)](https://doi.org/10.1109/37.969131) distinguem interdependências físicas, cibernéticas, geográficas e lógicas entre infraestruturas; um grafo de dependências é o modelo mais simples capaz de conter as quatro, desde que você rotule cada aresta com seu tipo.

Vocabulário de grafos que você vai usar: **caminho**, **ciclo** (um laço de dependência — por exemplo, a rede de telemetria precisa da energia da rede elétrica, e a recomposição feita pelo operador da rede elétrica precisa da telemetria), **grau de entrada** e **grau de saída**, **vértice de corte** (um nó cuja remoção desconecta o grafo) e **componente fortemente conexa**. Um vértice de corte num grafo de abastecimento é um ponto único de falha.

### 2.3 Contagem, espaços de estados e seus limites

Um sistema com $n$ entradas binárias tem $2^n$ estados de entrada; com 30 entradas, são mais de um bilhão. Acrescente memória interna (temporizadores, travas) e o espaço de estados cresce mais depressa. A verificação exaustiva é excelente para pequenos intertravamentos e impossível para plantas inteiras; para estas, você usa estrutura (decomposição, invariantes) e amostragem (Capítulo 30). O **princípio da casa dos pombos** dá limites rápidos de segurança: um contador de mensagens de 16 bits dá a volta após 65.536 mensagens, então, a uma mensagem por segundo, ele se repete em cerca de 18 horas, e a partir daí uma verificação contra repetição baseada apenas nesse contador falha.

### 2.4 Exemplo resolvido: dependências de Lowmarsh (sintético)

Os engenheiros da LRWA listam aquilo de que depende o abastecimento do St Brenna's Hospital: o reservatório de Hollin Hill e a alimentação direta pela PS4; Hollin Hill depende da PS3; cada estação de bombeamento precisa da energia da rede elétrica e de sua RTU; as duas RTUs se comunicam por uma rede LTE privada que, por sua vez, é alimentada pelo alimentador F1 da rede elétrica. O Laboratório 2 codifica isso e calcula o conjunto de impacto de cada falha. Perder o alimentador F1 derruba a rede LTE além da PS3 — e assim a telemetria "redundante" da PS4, que está no alimentador F2, também se perde. O projeto com dois alimentadores parecia diverso no desenho elétrico; o grafo mostra uma dependência comum pelas comunicações.

### 2.5 Atividade prática: Laboratório 2

```python
# Lab 2 - dependency closure and an interlock truth table (synthetic Lowmarsh assets, offline)
from collections import deque
from itertools import product
DEPENDS = {  # asset: assets it needs in order to work
    "hospital_supply": ["hollin_res", "ps4"],
    "hollin_res": ["ps3"], "ps4": ["grid_f2", "rtu4"], "ps3": ["grid_f1", "rtu3"],
    "rtu3": ["lte"], "rtu4": ["lte"], "lte": ["grid_f1"], "fenwick_wtw": ["grid_f1", "chlorine"],
    "ps3_feed": ["fenwick_wtw"],
}
def impacted(failed):
    users = {}
    for a, ds in DEPENDS.items():
        for d in ds: users.setdefault(d, []).append(a)
    seen, q = {failed}, deque([failed])
    while q:
        n = q.popleft()
        for u in users.get(n, []):
            if u not in seen: seen.add(u); q.append(u)
    return sorted(seen - {failed})
for f in ("grid_f1", "lte", "grid_f2", "chlorine"):
    print(f"{f:9} -> {impacted(f)}")
# Pump P3 may run iff level below high AND suction not low AND (remote permit OR local manual)
rows = [(h, s, p, m, (not h) and (not s) and (p or m)) for h, s, p, m in product([0, 1], repeat=4)]
print("states allowing run:", sum(r[4] for r in rows), "of", len(rows))
```

Saída esperada:

```text
grid_f1   -> ['fenwick_wtw', 'hollin_res', 'hospital_supply', 'lte', 'ps3', 'ps3_feed', 'ps4', 'rtu3', 'rtu4']
lte       -> ['hollin_res', 'hospital_supply', 'ps3', 'ps4', 'rtu3', 'rtu4']
grid_f2   -> ['hospital_supply', 'ps4']
chlorine  -> ['fenwick_wtw', 'ps3_feed']
states allowing run: 3 of 16
```

Apenas 3 dos 16 estados de entrada permitem que a bomba funcione: aqueles com $H = S = 0$ e pelo menos um entre $P, M$.

Leia devagar a lista de impacto do alimentador F1. Ela contém a rede LTE, as duas RTUs e a PS4, embora a própria PS4 seja alimentada pelo alimentador F2, porque a RTU da PS4 só chega à sala de controle pela LTE. Essa é a dependência comum oculta que o exemplo resolvido descreve. O resultado da tabela-verdade é igualmente concreto: três de dezesseis estados permitem que a bomba funcione, e todos eles exigem que as entradas de nível alto e de sucção baixa sejam falsas, então uma permissão remota forjada sozinha nunca consegue ligar a bomba numa condição de desarme.

### 2.6 Erros comuns e limites

- Desenhar setas em direções misturadas ("alimenta" versus "depende de") num mesmo grafo.
- Tratar dois caminhos como redundantes sem verificar nós compartilhados mais adiante.
- Testar um intertravamento apenas com casos "típicos", quando a tabela é pequena o bastante para testar todos.
- Esquecer que um grafo modela *se* algo funciona, e não *quão bem*: modos degradados precisam de pesos ou de estados (Capítulo 22).
- Escolher tamanhos de contadores e de identificadores sem contar quanto tempo falta até darem a volta.

Na LRWA esses erros têm consequências diretas: um grafo que mistura direções de setas informaria que perder a PS4 prejudica o alimentador F2, e uma revisão que parasse no desenho elétrico teria deixado passar completamente a dependência compartilhada da LTE.

### Exercícios — capítulo 2

**EX003 — Reescrita do intertravamento.** *Objetivo:* manipular expressões booleanas e raciocinar sobre entradas que chegam pela rede. *Entradas:* RUN na §2.1. *Passos:* (1) escreva a condição de desarme $\neg\text{RUN}$ na forma de soma de produtos usando as leis de De Morgan; (2) liste os estados em que uma permissão remota forjada muda o resultado; (3) proponha uma mudança que mantenha a operação remota, mas exija uma segunda condição independente. *Evidência esperada:* expressões, lista e proposta. *Rubrica:* 3 = álgebra correta, exatamente os estados certos, proposta independente do mesmo caminho de rede; 2 = um deslize; 1 = apenas a álgebra; 0 = nada.

**EX004 — Verificação de diversidade.** *Objetivo:* encontrar dependências comuns ocultas. *Entradas:* Laboratório 2. *Passos:* (1) acrescente um enlace por satélite com bateria, `sat`, usado apenas pela RTU4, sem dependência da rede elétrica; (2) execute de novo e informe o impacto de `grid_f1`; (3) diga se o abastecimento do hospital agora sobrevive à perda de F1 e o que o grafo ainda não lhe diz. *Evidência esperada:* dicionário modificado, saída, duas frases. *Rubrica:* 3 = modelagem correta (a RTU4 depender de lte *ou* de sat exige observar que este grafo simples só modela dependências do tipo E), conclusão honesta sobre esse limite; 2 = saída correta, limite não percebido; 1 = não executado; 0 = nada.

### Síntese do capítulo

Escreva regras como lógica e dependências como grafos, e depois deixe o computador verificá-las. Pequenos intertravamentos podem e devem ser verificados exaustivamente; sistemas inteiros não podem, e a contagem lhe diz isso. Procure nós compartilhados por trás de caminhos aparentemente diversos, rotule as arestas com seu tipo e pergunte, para cada entrada, quais delas chegam por uma rede que um adversário pode alcançar.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 50

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) usar a lei de Ohm, potência e energia para dimensionar fontes de reserva para equipamentos de controle e de comunicação; (2) explicar propagação de sinais, ruído e atenuação o suficiente para ler um balanço de enlace; (3) relacionar calor, temperatura e vida útil de componentes com a confiabilidade de armários de campo; e (4) identificar canais laterais físicos e efeitos eletromagnéticos que importam para a segurança. Ele se apoia nos capítulos 1–2 e prepara o Capítulo 8 (arquitetura de computadores) e o Capítulo 11 (redes).

### 3.1 Eletricidade para o engenheiro de sistemas

A tensão $V$ (volts) impulsiona a corrente $I$ (ampères) através da resistência $R$ (ohms): $V = IR$. A potência é $P = VI$ watts; a energia é a potência integrada no tempo, $E = \int P\,dt$, geralmente expressa em watts-hora. Uma RTU de campo que consome 0,5 A a 24 V usa 12 W; com um modem LTE de 6 W e um pequeno switch Ethernet de 8 W, a carga do armário é de 26 W. Uma bateria de 24 V e 40 Ah armazena nominalmente 960 Wh; a energia utilizável é menor, porque as baterias não devem ser totalmente descarregadas e a capacidade cai com a idade e com o frio. Com uma fração utilizável de 0,6 e eficiência de conversão de 85%, o armário funciona por $960 \times 0.6 \times 0.85 / 26 \approx 18.8$ horas. Esse número é um **requisito de segurança**, não um detalhe de manutenção: se uma falta de energia faz parte de um ataque, uma telemetria que morre após duas horas cega o operador exatamente quando ele precisa dela. O **ataque à rede elétrica ucraniana de dezembro de 2015** incluiu a desativação de nobreaks em centros de controle, segundo o [caso de uso de defesa do E-ISAC e do SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and) e o [alerta IR-ALERT-H-16-056-01 da CISA](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01).

### 3.2 Sinais, ruído e enlaces

Os sinais percorrem o cobre a uma fração significativa da velocidade da luz e a fibra a cerca de dois terços dela, então 100 km de fibra acrescentam cerca de 0,5 ms em um sentido — pouco em comparação com os atrasos de protocolo e de filas (Capítulo 36). Enlaces de rádio perdem potência com a distância e com obstáculos; os engenheiros expressam ganhos e perdas em decibéis (dB), em que +3 dB é cerca do dobro da potência e +10 dB, dez vezes. Um balanço de enlace soma a potência do transmissor e os ganhos das antenas e subtrai as perdas de percurso e de cabo; o que sobra acima da sensibilidade do receptor é a **margem de desvanecimento**. [Shannon (1948)](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x) mostrou que a capacidade de um canal depende da largura de banda e da relação sinal-ruído, $C = B\log_2(1 + S/N)$. A consequência para a segurança: um interferidor (jammer) não precisa quebrar nenhuma criptografia; basta reduzir $S/N$ abaixo do que o enlace precisa. A disponibilidade da telemetria por rádio é uma propriedade física antes de ser uma propriedade criptográfica.

### 3.3 Calor e vida útil

Componentes eletrônicos falham mais depressa quando estão quentes. Uma regra prática de engenharia muito usada, derivada da relação de Arrhenius, é que muitos mecanismos de falha dobram aproximadamente de taxa a cada 10 °C de aumento; trate-a como uma heurística a ser substituída pelos dados do fabricante. Um armário vedado à beira da estrada, sob o sol do verão, pode ficar muito mais quente do que o ar. Implicações de projeto: reduza a carga nominal, ventile ou resfrie, e monitore a temperatura do armário — uma subida repentina também pode indicar uma porta deixada aberta.

Nos armários de beira de estrada da LRWA, o sensor de temperatura deve reportar ao SCADA junto com a tensão da bateria, para que uma tendência de alta fique visível antes que os componentes envelheçam precocemente.

### 3.4 Física e segurança

Efeitos físicos vazam informação e permitem falhas. O consumo de energia e as emanações eletromagnéticas podem revelar chaves criptográficas (canais laterais); falhas provocadas de tensão ou de clock (glitches) podem fazer um processador pular instruções; linhas de DRAM perturbadas por acessos repetidos podem inverter bits nas vizinhas, como demonstraram [Kim et al. (2014)](https://doi.org/10.1109/ISCA.2014.6853210). Em infraestrutura, o acesso físico a armários de campo costuma ser mais fácil do que o acesso pela rede, então esses ataques não são exóticos. Chaves de violação, gabinetes vedados e chaves criptográficas guardadas fora do dispositivo são os controles físicos.

Na LRWA, o armário de cada estação de bombeamento abriga a RTU e, depois do TMRP, seu repositório de chaves.

### 3.5 Exemplo resolvido: autonomia do armário da PS4 (sintético)

O requisito R5 do TMRP da LRWA diz que a telemetria de campo deve sobreviver a uma falta de energia de 24 horas na rede elétrica. O armário planejado da PS4 consome 26 W. A energia utilizável necessária, com 85% de eficiência, é $26 \times 24 / 0.85 \approx 734$ Wh; com fração utilizável de 0,6, a capacidade nominal deve ser de pelo menos $734/0.6 \approx 1{,}224$ Wh, ou cerca de 51 Ah a 24 V. Os engenheiros arredondam para um banco padrão de 65 Ah para levar em conta o envelhecimento (a capacidade costuma ser especificada até o fim da vida útil em 80%: $65 \times 0.8 = 52$ Ah, que ainda atende ao requisito). Um projeto que só atendesse a R5 com a bateria nova falharia no terceiro ano.

### 3.6 Atividade prática

Sem código: monte uma planilha ou um script de dez linhas que calcule a autonomia da bateria a partir da carga (W), da capacidade nominal (Wh), da fração utilizável, da eficiência e do fator de capacidade no fim da vida útil. Reproduza a §3.5 e depois acrescente um aquecedor de armário de 15 W que funciona sempre que a temperatura externa está abaixo de 0 °C, e recalcule. Use a carga de 26 W do armário, a eficiência de 85%, a fração utilizável de 0,6 e o fator de fim de vida útil de 80% do exemplo resolvido, para que seu primeiro resultado reproduza a escolha de 65 Ah. Depois acrescente o aquecedor e veja quanto o requisito cresce. Escreva a resposta como uma verificação de requisito, não como um número isolado: diga se o banco ainda atende às 24 horas de R5 no fim da vida útil em tempo frio e o que você mudaria se não atender. Mantenha as unidades visíveis em todas as colunas.

### 3.7 Erros comuns e limites

- Dimensionar pela capacidade de placa da bateria, em vez da capacidade utilizável no fim da vida útil e no frio.
- Esquecer que o caminho de comunicação (estações rádio base celulares, repetidores de fibra) tem sua própria dependência de energia, fora do seu controle.
- Tratar a proteção criptográfica como proteção da disponibilidade.
- Usar regras práticas (dobrar a cada 10 °C) como previsões precisas.

Cada um desses erros faria R5 parecer atendido no papel enquanto falha na prática. Dimensionar para uma bateria nova é o mais comum, porque o déficit só aparece no terceiro ano. Esquecer a dependência de energia da operadora importa na LRWA porque a rede LTE compartilha o alimentador F1 com a PS3. Tratar a cifração como proteção da disponibilidade é o mal-entendido que o EX006 pede que você corrija, e uma regra prática usada como previsão dá um número de aparência precisa sem nenhuma base real por trás.

### Exercícios — capítulo 3

**EX005 — Autonomia com aquecedor.** *Objetivo:* dimensionar o armazenamento de energia com uma carga condicional. *Entradas:* §§3.5–3.6. *Passos:* calcule a capacidade nominal necessária no fim da vida útil se o aquecedor de 15 W funcionar 10 das 24 horas. *Evidência esperada:* cálculo com unidades. *Rubrica:* 3 = energia, eficiência, fração utilizável e fator de fim de vida útil aplicados corretamente; 2 = um fator ausente; 1 = unidades erradas; 0 = nada.

**EX006 — Interferência versus cifração.** *Objetivo:* separar confidencialidade e integridade de disponibilidade. *Entradas:* um comentário de revisão de projeto: "A telemetria LTE é cifrada, então os ataques por rádio estão mitigados". *Passos:* escreva uma resposta de 150 palavras que explique o que a cifração mitiga e o que não mitiga e proponha dois controles físicos ou de arquitetura. *Evidência esperada:* resposta. *Rubrica:* 3 = raciocínio sobre interferência e S/N, controles que tratam da disponibilidade (caminho diverso, autonomia local, detecção de perda de enlace); 2 = controles genéricos; 1 = equívoco mantido; 0 = nada.

### Síntese do capítulo

Energia, sinal e calor são onde o cibernético encontra o físico. Dimensione a energia de reserva para as condições de fim de vida útil e para a interrupção completa que o modelo de ameaças inclui; trate a disponibilidade do rádio como uma questão de relação sinal-ruído, não de criptografia; projete os armários para o calor; e lembre-se de que o acesso físico abre canais laterais e ataques por injeção de falhas que nenhum firewall vê.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 50

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) escrever programas Python pequenos e corretos com funções, laços, condicionais, bytes e dicionários; (2) implementar um algoritmo publicado — o CRC-16 do Modbus RTU — e testá-lo contra um vetor conhecido; (3) interpretar entradas binárias não confiáveis de forma defensiva, rejeitando em vez de consertar dados malformados; e (4) explicar por que o código de interpretação (parsing) é crítico para a segurança em infraestrutura. Ele transforma em código a lógica do Capítulo 2 e prepara o Capítulo 9.

### 4.1 Programas como descrições precisas

Um programa é a descrição de uma computação, precisa o bastante para uma máquina. Software de infraestrutura precisa ser preciso sobre três coisas que os iniciantes confundem: **tipos** (um byte não é um caractere; um registrador inteiro não é um número de ponto flutuante), **limites** (o que acontece no primeiro e no último elemento, no zero, no máximo) e **falha** (o que o programa faz com uma entrada que não esperava). Este livro usa Python porque sua biblioteca padrão cobre bytes, hashing e simulação sem instalação. Seu tipo `bytes` é imutável e indexável por inteiros; `int.from_bytes(b, "big")` converte com uma ordem de bytes explícita.

### 4.2 Implementando o checksum de um protocolo

O Modbus é um protocolo industrial de longa vida; sua forma serial (RTU) termina cada quadro com uma verificação de redundância cíclica de 16 bits, enviada com o byte menos significativo primeiro, conforme definido nas [especificações do protocolo de aplicação Modbus e da linha serial publicadas pela Modbus Organization](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf). Um CRC detecta corrupção acidental — ruído numa linha serial — com alta probabilidade. Ele **não** é um mecanismo de segurança: qualquer pessoa pode calcular um CRC válido para um quadro forjado. Aprenda a diferença cedo: integridade contra a natureza versus integridade contra um adversário (Capítulo 19).

O CRC padrão do Modbus começa em 0xFFFF, faz XOR de cada byte nos bits menos significativos e desloca para a direita oito vezes, fazendo XOR com 0xA001 quando o bit deslocado para fora é 1. Um vetor de teste amplamente publicado é a requisição `01 03 00 00 00 0A` (unidade 1, ler 10 registradores holding a partir do endereço 0), cujos bytes de CRC são `C5 CD`. Testar contra um vetor antes de usar sua função é inegociável.

### 4.3 Interpretação defensiva

Um interpretador (parser) que lê dados de um dispositivo de campo, de uma rede ou de um arquivo é a fronteira entre o mundo externo e as suposições do seu programa. Regras: verifique o comprimento antes de indexar; verifique a integridade (CRC) antes de confiar em qualquer campo; confira cada campo contra o que você pediu (unidade, função, contagem de bytes); confira os valores contra os limites físicos; diante de qualquer falha, **rejeite e informe** — não adivinhe. As listas da OWASP e da CWE de fraquezas comuns ([CWE Top 25](https://cwe.mitre.org/top25/)) são dominadas por erros de tratamento de entrada: leituras e escritas fora dos limites, validação inadequada de entrada, estouro de inteiros.

### 4.4 Exemplo resolvido: lendo o nível de Hollin Hill (sintético)

A RTU da LRWA na PS3 devolve dois registradores: o nível do reservatório em centímetros e a pressão de saída em kPa. O Laboratório 3 monta o quadro de requisição e depois interpreta cinco respostas: uma boa, uma com um único bit invertido, uma exceção Modbus, um valor fora da faixa física do tanque (65535 cm — um registrador não inicializado) e um quadro truncado. Cada caso ruim é rejeitado com um motivo sobre o qual um operador ou um analista de logs consegue agir.

Cada motivo de rejeição é escrito para apontar uma causa: uma falha de CRC sugere ruído na linha, uma exceção aponta para o estado da própria RTU, e uma falha de faixa sugere um defeito ou um registrador não inicializado que a manutenção deve investigar.

### 4.5 Atividade prática: Laboratório 3

```python
# Lab 3 - Modbus RTU CRC-16 and a defensive response parser (offline)
def crc16(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return crc
def frame(body: bytes) -> bytes:
    c = crc16(body); return body + bytes([c & 0xFF, c >> 8])   # low byte first
req = frame(bytes.fromhex("01030000000A"))
print("request:", req.hex(" "))
def parse(resp: bytes, unit=1, count=2, lo=0, hi=4000):
    if len(resp) < 5: return "reject: short"
    if crc16(resp[:-2]) != resp[-2] | resp[-1] << 8: return "reject: crc"
    if resp[0] != unit: return "reject: unit"
    if resp[1] & 0x80: return f"reject: exception {resp[2]}"
    if resp[1] != 3 or resp[2] != 2 * count or len(resp) != 5 + 2 * count: return "reject: shape"
    vals = [int.from_bytes(resp[3 + 2*i:5 + 2*i], "big") for i in range(count)]
    if any(not lo <= v <= hi for v in vals): return f"reject: range {vals}"
    return f"ok {vals}"
good = frame(bytes.fromhex("010304") + (3150).to_bytes(2, "big") + (212).to_bytes(2, "big"))
tests = {"good": good, "bitflip": good[:4] + bytes([good[4] ^ 1]) + good[5:],
         "exception": frame(bytes.fromhex("018302")), "outrange": frame(bytes.fromhex("010304FFFF00D4")),
         "truncated": good[:6]}
for k, v in tests.items(): print(f"{k:9} {parse(v)}")
```

Saída esperada:

```text
request: 01 03 00 00 00 0a c5 cd
good      ok [3150, 212]
bitflip   reject: crc
exception reject: exception 2
outrange  reject: range [65535, 212]
truncated reject: crc
```

O quadro truncado é rejeitado pela verificação de CRC porque seus dois últimos bytes não são um CRC; um interpretador que verificasse o formato primeiro daria um motivo mais claro. As duas ordens são seguras; a propriedade importante é que nada seja aceito com base em evidência parcial.

Observe que a resposta boa é decodificada como um nível de 3.150 cm e uma pressão de 212 kPa, ambos dentro dos limites físicos configurados no interpretador. O caso fora da faixa mostra por que consertar é perigoso: limitar 65.535 ao máximo de 4.000 cm informaria um reservatório cheio quando o registrador nunca tinha sido escrito. Rejeitá-lo com o valor bruto no motivo dá à equipe de manutenção a pista de que precisa, e dá a um investigador a evidência de que o valor não era simplesmente ruído na linha.

### 4.6 Erros comuns e limites

- Erros de ordem de bytes (os registradores Modbus são big-endian; o CRC é transmitido com o byte menos significativo primeiro).
- Indexar antes de verificar o comprimento; confiar num campo de comprimento dentro da mensagem.
- Tratar um CRC como autenticação.
- "Consertar" uma entrada ruim (limitar 65535 a 4000) em vez de rejeitá-la, o que esconde falhas e ataques.
- Escrever testes apenas para o caminho feliz.

Cada item tem um teste correspondente no Laboratório 3 ou no EX008. Um interpretador que passa nesses testes, mas nunca foi conferido contra um quadro truncado ou malformado, só foi testado no caminho feliz, e a primeira linha serial ruidosa numa estação de bombeamento vai mostrar o que ele faz com uma entrada que não esperava. Escreva primeiro os testes de falha, porque são eles que importam quando algo dá errado em campo.

### Exercícios — capítulo 4

**EX007 — CRC à mão e por código.** *Objetivo:* verificar uma implementação. *Entradas:* Laboratório 3. *Passos:* (1) calcule com a função o CRC de `01 06 00 01 00 03` (escrever um registrador); (2) inverta um bit nos dados e mostre que o CRC muda; (3) explique em duas frases por que um atacante na linha serial não é impedido pelo CRC. *Evidência esperada:* valores hexadecimais e explicação. *Rubrica:* 3 = CRC correto (confira na resolução), demonstração, afirmação de segurança correta; 2 = um item ausente; 1 = código não executado; 0 = nada.

**EX008 — Endurecimento do interpretador.** *Objetivo:* melhorar o relato de erros sem enfraquecer as verificações. *Entradas:* `parse()`. *Passos:* reordene as verificações para que um quadro truncado informe "short" ou "shape" antes do CRC, acrescente uma verificação que rejeite uma resposta cujo identificador de unidade seja 0 (broadcast) e acrescente dois casos de teste. *Evidência esperada:* diff do código e saídas. *Rubrica:* 3 = todas as rejeições originais preservadas, novas verificações corretas, testes incluídos; 2 = uma rejeição perdida; 1 = sem testes; 0 = nada.

### Síntese do capítulo

Escreva código explícito sobre tipos, limites e falhas. Implemente algoritmos publicados contra vetores de teste publicados. Trate todo interpretador como uma fronteira de segurança: comprimento, integridade, formato e, por fim, significado físico, e rejeite com um motivo em vez de adivinhar. Mantenha separadas, na sua cabeça, a detecção de erros acidentais (CRC) e a integridade contra adversários (MACs e assinaturas).

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 50

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) escrever um requisito que possa ser verificado; (2) produzir uma nota de projeto de uma página, um registro de decisão e um relatório de teste que outro engenheiro consiga conferir; (3) apresentar risco e incerteza a operadores, gestores e reguladores sem exagerá-los nem escondê-los; e (4) tratar de forma adequada, em documentos, detalhes sensíveis de infraestrutura. Ele se apoia nos capítulos 1–4, cujos números você agora precisa comunicar, e prepara os ateliês de projeto (capítulos 25 e 35).

### 5.1 Escrever para decisões

Documentos de engenharia existem para que alguém possa tomar ou conferir uma decisão. Comece pela decisão e por sua base; deixe as deduções para depois. Uma boa nota de projeto responde, nesta ordem: o que está sendo decidido, as opções consideradas, a recomendação, as evidências e as suposições por trás dela, o que mudaria a recomendação e quem precisa aprová-la. Os **registros de decisão de arquitetura** (ADRs) — notas curtas, datadas e numeradas que registram uma decisão, seu contexto e suas consequências — mantêm visíveis os motivos de um projeto anos depois, quando a equipe original já seguiu adiante.

### 5.2 Requisitos que podem ser verificados

Um requisito é uma afirmação que o sistema precisa satisfazer, escrita de modo que um teste, uma análise, uma inspeção ou uma demonstração possa mostrar se ele a satisfaz. O [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) recomenda requisitos necessários, inequívocos, verificáveis, viáveis e rastreáveis. Compare: "A telemetria deverá ser segura" (não verificável) com "Cada mensagem de telemetria de uma RTU de campo para o centro de controle deverá levar um código de autenticação de mensagem sobre seu conteúdo e um contador monotônico; o receptor deverá rejeitar as mensagens que falharem em qualquer das verificações e gerar um alarme em até 60 s" (verificável por teste). Use "deverá" para requisitos, mantenha um requisito por frase e dê a cada um deles um identificador.

### 5.3 Números, incerteza e figuras

Informe os números com unidades, o método que os produziu e sua incerteza ou suas suposições: "autonomia de 14,6 h (modelo de demanda integrada, início às 06:00, nível inicial de 85%; 17,3 h se for assumida a demanda média)". Prefira tabelas para valores exatos, gráficos de linha para séries temporais, e nunca um gráfico sem eixos rotulados e unidades. Evite a falsa precisão: uma autonomia de bateria calculada a partir de cargas estimadas é de "cerca de 19 h", não de "18,83 h". Faça figuras legíveis em tons de cinza e por pessoas com deficiência na visão de cores.

Na LRWA, o valor de autonomia no dossiê do TMRP traz seu horário de início e seu nível inicial, para que ninguém o cite para um cenário diferente.

### 5.4 Comunicar risco a leitores diferentes

Operadores precisam saber o que fazer e quando; gestores precisam de consequência, custo e opções; reguladores precisam de evidências de conformidade e de raciocínio. A mesma constatação — "setpoints remotos são aceitos sem autenticação" — torna-se, para um operador, "até a correção, confirme por telefone com a sala de controle qualquer mudança inesperada de setpoint"; para um gestor, "um comando forjado poderia ligar ou desligar bombas; custo da correção 120 mil, três meses"; para um regulador, uma lacuna de controle mapeada com um plano datado. Nenhuma dessas versões pode contradizer outra.

### 5.5 Informação sensível

Documentos de infraestrutura costumam conter endereços de rede, modelos de dispositivos, vulnerabilidades e limites de capacidade. Classifique os documentos por sensibilidade, compartilhe-os com base na necessidade de saber e retire detalhes das versões destinadas a públicos amplos. Relatórios públicos e trabalhos de estudantes devem descrever os sistemas no nível do [NIST Guide to OT Security (SP 800-82 Rev. 3)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — padrões de arquitetura —, e não as fraquezas específicas de um operador identificado. Neste livro todo número da LRWA é sintético, mas pratique o hábito mesmo assim: classifique as notas de projeto para uso interno, mantenha endereços de rede fora dos slides e produza uma versão reduzida para públicos de fora da equipe de engenharia.

### 5.6 Exemplo resolvido: um registro de decisão do TMRP (sintético)

> **ADR-007 — Autenticar a telemetria de campo na camada de aplicação.** *Data:* 2026-03-04. *Situação:* aceito. *Contexto:* o tráfego RTU–SCADA atravessa uma rede LTE privada operada por terceiros; a cifração da LTE termina na operadora. *Opções:* (a) confiar na cifração da operadora; (b) túneis IPsec por RTU; (c) HMAC na camada de aplicação com contadores. *Decisão:* (c), com (b) onde as RTUs o suportarem. *Consequências:* +22 bytes por mensagem (Laboratório 8); gestão de chaves necessária (Capítulo 19); as RTUs legadas da PS1 e da PS2 precisam de um gateway. *Rever se:* o contrato com a operadora mudar ou o firmware das RTUs ganhar protocolos seguros nativos.

### 5.7 Atividade prática

Reescreva em forma verificável três requisitos vagos de um briefing sintético ("o sistema deverá ser resiliente", "os alarmes deverão ser oportunos", "os logs deverão ser protegidos"), cada um com um método de verificação. Para cada reescrita, nomeie a evidência que mostraria que o requisito foi atendido: um teste com critério de aprovação, uma análise com suposições declaradas, uma inspeção ou uma demonstração. Use o contexto da LRWA onde ajudar. Um sistema resiliente pode virar uma autonomia declarada durante uma falta de energia da rede elétrica, alarmes oportunos podem virar uma meta de latência para uma parcela declarada dos eventos, e logs protegidos podem virar proteção de integridade com âncoras guardadas fora da zona de controle, como R8 exigirá mais adiante. Mantenha cada afirmação com um único requisito.

### 5.8 Erros comuns e limites

- Enterrar a recomendação; escrever uma cronologia em vez de um argumento.
- Requisitos contendo "e/ou", "conforme apropriado", "amigável", "seguro".
- Números sem unidades, método ou incerteza.
- Histórias diferentes para públicos diferentes.
- Compartilhar detalhes sensíveis em excesso, ou compartilhar tão pouco que os revisores não conseguem conferir o trabalho.

A maioria desses erros aparece primeiro nos conjuntos de requisitos. Um requisito que contém seguro não pode ser testado, então ele será discretamente abandonado ou declarado atendido sem evidência. Histórias diferentes para públicos diferentes são igualmente danosas: se a nota ao operador, o resumo ao gestor e a declaração ao regulador do EX010 discordarem sobre a bateria da PS4, quem ler duas delas não confiará em nenhuma.

### Exercícios — capítulo 5

**EX009 — Torne verificável.** *Objetivo:* escrever requisitos testáveis. *Entradas:* os três requisitos vagos da §5.7. *Passos:* reescreva cada um como uma ou mais afirmações com "deverá", com um identificador e um método de verificação (teste, análise, inspeção, demonstração). *Evidência esperada:* tabela. *Rubrica:* 3 = cada um mensurável, único, viável, com um método adequado; 2 = um ainda vago; 1 = apenas troca de palavras; 0 = nada.

**EX010 — Três públicos.** *Objetivo:* comunicar uma constatação de forma consistente. *Entradas:* "A bateria da telemetria da PS4 dura 6 h no fim da vida útil; o requisito R5 é de 24 h". *Passos:* escreva uma nota de duas frases ao operador, um resumo de 100 palavras ao gestor, com opções, e uma declaração de lacuna dirigida ao regulador. *Evidência esperada:* três textos. *Rubrica:* 3 = fatos consistentes, ações adequadas a cada público, sem excesso de detalhes sensíveis; 2 = uma inconsistência; 1 = o mesmo texto três vezes; 0 = nada.

### Síntese do capítulo

Escreva para viabilizar decisões: a recomendação primeiro, as evidências e suposições em seguida, as condições de mudança por último. Torne todo requisito verificável e rastreável; informe números com unidades, métodos e incerteza; adapte a mensagem, não os fatos, ao leitor; e trate os detalhes de infraestrutura como informação sensível, com um público definido.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 50

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (inglês) →](../../en/book/MANUSCRIPT.md#ch-06)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável. Os resultados numéricos foram produzidos executando os laboratórios e os scripts curtos descritos, com Python 3 e as sementes indicadas; seus últimos dígitos podem diferir se você mudar a ordem dos sorteios aleatórios. Nos exercícios de projeto, a rubrica do capítulo importa mais do que coincidir com a redação abaixo. Lowmarsh Regional Water Authority, St Brenna's Hospital, o TMRP e todos os números são sintéticos. Esta edição parcial traz as resoluções de EX001–EX010; as de EX011–EX100 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

### Capítulo 1

**EX001.** $d'(t) = 60\cdot\frac{2\pi}{24}\cos(2\pi t/24) \approx 15.71\cos(2\pi t/24)$ m³/h². Máximo de 15,71 m³/h² em $t = 0$ (06:00) e de novo a cada 24 h. Como 15,71 > 12, as bombas não conseguem acompanhar a demanda em todos os instantes: $d'(t) > 12$ quando $|t| < 2.68$ h, isto é, aproximadamente das 03:20 às 08:40 todos os dias. A reservação precisa cobrir o déficit durante a subida da manhã, o que é uma das razões pelas quais os reservatórios existem.

**EX002.** Interrupção às 06:00: 14,62 h. Interrupção às 18:00: 18,62 h. Estimativa pela demanda média: 17,33 h. O plano de emergência deve citar o pior horário de início plausível (≈ 14,6 h, ou menos se um nível inicial mais baixo for plausível), porque o plano precisa funcionar seja quando for que a interrupção comece; o valor da demanda média não é nem o pior caso nem o caso típico.

### Capítulo 2

**EX003.** $\neg\text{RUN} = H \vee S \vee (\neg P \wedge \neg M)$. Uma permissão forjada só muda o resultado nos estados com $H = 0$, $S = 0$, $M = 0$ (em que RUN seria falso de outro modo): um estado em 16. Uma proposta: exigir, para a partida remota, tanto $P$ quanto uma segunda condição que não percorra o mesmo caminho de rede — por exemplo, uma chave seletora local de "remoto habilitado" $K$: $\text{RUN} = \neg H \wedge \neg S \wedge ((P \wedge K) \vee M)$. A chave seletora é acionada pela equipe da instalação para a operação remota planejada.

**EX004.** Com a RTU4 passando a usar apenas `sat` (e `sat` sem depender de nada), a perda de `grid_f1` afeta `fenwick_wtw, hollin_res, hospital_supply, lte, ps3, ps3_feed, rtu3` — `ps4` e `rtu4` sobrevivem. Mas o grafo do laboratório ainda marca `hospital_supply` como afetado, porque suas arestas são dependências do tipo E: o abastecimento "precisa" tanto do reservatório quanto da PS4. A lógica real é OU (qualquer um dos caminhos basta), o que este grafo simples não consegue expressar — o Capítulo 22 acrescenta tipos E/OU. Uma modelagem melhor da tarefa (a RTU4 precisa da LTE *ou* do satélite) também exige semântica de OU. Resposta honesta: o hospital provavelmente sobrevive à perda de F1 via PS4, mas este modelo não consegue mostrar isso.

### Capítulo 3

**EX005.** Energia diária: 26 W × 24 h + 15 W × 10 h = 774 Wh na carga. Divida pela eficiência de 0,85, pela fração utilizável de 0,6 e pelo fator de fim de vida útil de 0,8: 774 / (0,85 × 0,6 × 0,8) ≈ 1.897 Wh nominais, ≈ 79 Ah a 24 V. É necessário um banco padrão de 80 Ah ou maior; o banco de 65 Ah da §3.5 deixa de atender a R5 no inverno.

**EX006.** Resposta-modelo: "A cifração da LTE protege a confidencialidade e, dependendo da configuração, a integridade do tráfego no trecho de rádio; ela não faz nada pela disponibilidade. Um interferidor ou uma queda da operadora reduz a relação sinal-ruído abaixo do que o enlace precisa, e nenhuma chave impede isso. A cifração também termina na operadora, então não autentica nossas RTUs perante nosso SCADA de ponta a ponta. Para a disponibilidade: (1) projetar as instalações para funcionar em modo automático local por 72 h sem telemetria e alarmar a perda de enlace no SCADA em até 60 s; (2) prover um caminho diverso (segunda operadora, com torres e energia diferentes, ou satélite) para as instalações mais críticas; (3) monitorar a qualidade do enlace para distinguir interferência de queda."

### Capítulo 4

**EX007.** `01 06 00 01 00 03` → bytes de CRC `98 0B` (quadro `01 06 00 01 00 03 98 0b`). Trocar o último byte de dados para `02` dá `59 CB`. Um atacante na linha serial calcula o CRC de um quadro forjado exatamente como o mestre legítimo, porque o algoritmo não tem segredo; o CRC só detecta corrupção acidental.

**EX008.** Mova `len(resp) < 5` e uma verificação de comprimento total (`len(resp) == 5 + 2*count` para respostas normais, 5 para exceções) para antes do CRC; depois o CRC; depois `if resp[0] == 0: return "reject: broadcast"` e a verificação de unidade; depois função/contagem de bytes; depois a faixa. Testes: quadro truncado → "reject: shape"; quadro com unidade 0 e CRC válido → "reject: broadcast". Todos os casos originais mantêm uma rejeição. (Requisições de broadcast não recebem resposta no Modbus; uma resposta da unidade 0 é malformada.)

### Capítulo 5

**EX009.** Exemplo: "R10 — O sistema deverá manter o abastecimento de água tratada ao St Brenna's dentro da pressão contratual durante a perda de qualquer estação de bombeamento isolada por pelo menos 24 h (análise + ensaio)." "R7 — Os alarmes prioritários deverão ser exibidos nas telas dos operadores em até 60 s após o evento em campo para 99% dos eventos, numa medição de 30 dias (teste)." "R8 — Os logs de segurança deverão ser encaminhados para fora do host em até 5 min e protegidos em integridade com âncoras diárias guardadas fora da zona de controle; a modificação de qualquer registro armazenado deverá ser detectável (teste)."

**EX010.** Operador: "A telemetria da PS4 pode apagar após cerca de 6 h sem energia da rede. Se a telemetria da PS4 for perdida durante uma falta de energia, despache o técnico de plantão para ler os manômetros locais na marca de 4 h." Gestor: "A bateria da telemetria da PS4 dura cerca de 6 h no fim da vida útil, contra um requisito de 24 h (R5). Durante uma interrupção longa perderíamos a visibilidade — não o abastecimento — na alimentação do hospital. Opções: substituir por um banco de 80 Ah (≈ custo de uma visita à instalação mais o equipamento, duas semanas) ou acrescentar uma entrada para gerador pequeno; provisoriamente: regra de despacho do técnico." Regulador: "Lacuna: R5 (24 h de autonomia da telemetria) não atendido na PS4 (6 h medidas no fim da vida útil). Procedimento compensatório em vigor desde [data]; correção até [data]."

<a id="glossary"></a>

## Glossário

- **Lista de permissões (allowlist)** — política que permite apenas fluxos, programas ou valores listados; todo o resto é negado.
- **Âncora** — cópia confiável da cabeça de uma cadeia de hashes (com a contagem de registros) guardada fora do alcance do atacante.
- **Caso de garantia (assurance case)** — argumento estruturado de que um sistema atende a uma afirmação, ligando subafirmações a evidências, com ressalvas e refutadores.
- **Disponibilidade** — fração do tempo em que um sistema é capaz de desempenhar sua função; MTBF/(MTBF + MTTR) para uma unidade reparável simples.
- **Taxa-base** — prevalência do evento de interesse; decisiva para o valor preditivo de um alarme.
- **Fator beta** — fração da indisponibilidade de uma unidade atribuída a causas comuns que derrubam juntas as unidades redundantes.
- **Conduto (conduit)** — caminho de comunicação controlado entre zonas (vocabulário da IEC 62443).
- **Caminho crítico** — a cadeia mais longa de tarefas dependentes; define o tempo mínimo de conclusão.
- **Refutador (defeater)** — condição sob a qual a conclusão de um argumento não se sustentaria.
- **DMZ** — zona intermediária pela qual todo o tráfego entre as redes de controle e corporativa é intermediado.
- **Injeção de falhas** — introdução deliberada de falhas para testar o tratamento de erros.
- **HMAC** — código de autenticação de mensagem com chave, construído a partir de uma função de hash (FIPS 198-1).
- **Autonomia local** — capacidade de uma instalação de continuar operando com segurança sem o centro ou a rede.
- **Conjunto de corte mínimo** — menor conjunto de eventos básicos cuja ocorrência conjunta causa o evento de topo de uma árvore de falhas.
- **PLC / RTU** — controlador lógico programável (controle local por ciclos de varredura) / unidade terminal remota (coleta de dados e controle remotos por enlaces longos).
- **Precisão / revocação (precision / recall)** — parcela dos alarmes que são reais / parcela dos eventos reais que geram alarme.
- **Teste baseado em propriedades** — teste que verifica uma propriedade declarada em muitas entradas geradas, incluindo valores especiais.
- **Resíduo** — diferença entre uma medição e a previsão de um modelo independente.
- **Risco residual** — risco que permanece após os controles; precisa ter um dono.
- **Inicialização segura (secure boot)** — verificação das assinaturas do firmware a partir de uma raiz de confiança imutável antes da execução.
- **STPA** — System-Theoretic Process Analysis; encontra ações de controle inseguras e seus cenários causais.
- **Constante de tempo** — em sistemas de primeira ordem, o tempo para fechar cerca de 63% da diferença até o equilíbrio.
- **Rastreabilidade** — ligações das necessidades aos requisitos, ao projeto, aos testes e aos resultados.
- **Ação de controle insegura** — ação de controle que, num contexto específico, leva a um perigo.
- **Validação / verificação** — o sistema certo para a necessidade / o sistema construído conforme sua especificação.
- **Zona** — agrupamento de ativos com requisitos de segurança comuns.

<a id="references"></a>

## Referências

Leis, normas, orientações e páginas de incidentes mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas. A lista é idêntica à da edição em inglês; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional.

**Políticas, leis, normas e frameworks**

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [ICS Advisories](https://www.cisa.gov/news-events/ics-advisories).
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- International Electrotechnical Commission. [IEC 62443-3-2:2020 — Security risk assessment for system design (catalogue page)](https://webstore.iec.ch/en/publication/30727).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- MITRE. [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/).
- Modbus Organization. [Modbus Application Protocol Specification](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf).
- NASA. [NASA Systems Engineering Handbook (SP-2016-6105 Rev. 2)](https://www.nasa.gov/reference/systems-engineering-handbook/).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final). September 2012.
- National Institute of Standards and Technology. [SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025.
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final). September 2023.
- National Institute of Standards and Technology. [SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final). November 2022.
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST, December 2021.
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). August 2020.
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final). February 2022.
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final); [FIPS 197, Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final); [FIPS 198-1, The Keyed-Hash Message Authentication Code (HMAC)](https://csrc.nist.gov/pubs/fips/198-1/final).
- National Institute of Standards and Technology. [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). 13 August 2024.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- Open Source Security Foundation. [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/).
- Reproducible Builds project. [Reproducible Builds](https://reproducible-builds.org/).
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, August 2018.
- Eddy, W. (ed.). [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293). IETF, August 2022.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, February 1997.
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).

**Ética profissional**

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics). 2018.
- National Society of Professional Engineers. [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics).

**Incidentes e evidências setoriais**

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Cybersecurity and Infrastructure Security Agency. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). 2019.
- E-ISAC and SANS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). March 2016 (archived copy).
- Langner, R. [Stuxnet: Dissecting a Cyberwarfare Weapon](https://doi.org/10.1109/MSP.2011.67). *IEEE Security & Privacy*, 9(3), 49–51, 2011.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems*, 21(6), 11–25, 2001.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Computação, segurança e dependabilidade**

- Avizienis, A., Laprie, J.-C., Randell, B., and Landwehr, C. [Basic Concepts and Taxonomy of Dependable and Secure Computing](https://doi.org/10.1109/TDSC.2004.2). *IEEE Transactions on Dependable and Secure Computing*, 1(1), 11–33, 2004.
- Brooks, F. P. [No Silver Bullet: Essence and Accidents of Software Engineering](https://doi.org/10.1109/MC.1987.1663532). *Computer*, 20(4), 10–19, 1987.
- Codd, E. F. [A Relational Model of Data for Large Shared Data Banks](https://doi.org/10.1145/362384.362685). *Communications of the ACM*, 13(6), 377–387, 1970.
- Diffie, W., and Hellman, M. [New Directions in Cryptography](https://doi.org/10.1109/TIT.1976.1055638). *IEEE Transactions on Information Theory*, 22(6), 644–654, 1976.
- Fagan, M. E. [Design and Code Inspections to Reduce Errors in Program Development](https://doi.org/10.1147/sj.153.0182). *IBM Systems Journal*, 15(3), 182–211, 1976.
- Kim, Y., Daly, R., Kim, J., et al. [Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors](https://doi.org/10.1109/ISCA.2014.6853210). *ISCA*, 2014.
- Kocher, P., Horn, J., Fogh, A., et al. [Spectre Attacks: Exploiting Speculative Execution](https://doi.org/10.1109/SP.2019.00002). *IEEE Symposium on Security and Privacy*, 2019.
- Liu, C. L., and Layland, J. W. [Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment](https://doi.org/10.1145/321738.321743). *Journal of the ACM*, 20(1), 46–61, 1973.
- McCabe, T. J. [A Complexity Measure](https://doi.org/10.1109/TSE.1976.233837). *IEEE Transactions on Software Engineering*, SE-2(4), 308–320, 1976.
- Parnas, D. L. [On the Criteria to Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623). *Communications of the ACM*, 15(12), 1053–1058, 1972.
- Rivest, R. L., Shamir, A., and Adleman, L. [A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://doi.org/10.1145/359340.359342). *Communications of the ACM*, 21(2), 120–126, 1978.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.
- Shannon, C. E. [A Mathematical Theory of Communication](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). *Bell System Technical Journal*, 27(3), 379–423, 1948.

**Controle, segurança operacional, confiabilidade e resiliência**

- Åström, K. J., and Murray, R. M. [Feedback Systems: An Introduction for Scientists and Engineers](https://fbswiki.org/wiki/index.php/Main_Page). Princeton University Press; free online edition.
- Bruneau, M., Chang, S. E., Eguchi, R. T., et al. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra*, 19(4), 733–752, 2003.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis*, 29(4), 498–501, 2009.
- Leveson, N. [A New Accident Model for Engineering Safer Systems](https://doi.org/10.1016/S0925-7535(03)00047-X). *Safety Science*, 42(4), 237–270, 2004.
- Little, J. D. C. [A Proof for the Queuing Formula: L = λW](https://doi.org/10.1287/opre.9.3.383). *Operations Research*, 9(3), 383–387, 1961.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320(7237), 768–770, 2000.
- Saltelli, A., Ratto, M., Andres, T., et al. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.

**Avaliação, pesquisa e argumentação**

- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security Symposium*, 2022.
- Goh, J., Adepu, S., Junejo, K. N., and Mathur, A. [A Dataset to Support Research in the Design of Secure Water Treatment Systems](https://doi.org/10.1007/978-3-319-71368-7_8). *Critical Information Infrastructures Security (CRITIS 2016)*, LNCS 10242, 88–99, 2017.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology*, 9(10), e1003285, 2013.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation*, 7(1), 12–24, 2013.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Taormina, R., Galelli, S., Tippenhauer, N. O., et al. [Battle of the Attack Detection Algorithms: Disclosing Cyber Attacks on Water Distribution Networks](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969). *Journal of Water Resources Planning and Management*, 144(8), 2018.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
