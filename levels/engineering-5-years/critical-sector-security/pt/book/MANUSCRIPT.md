# Infraestrutura Crítica e Segurança Setorial: Engenharia de Sistemas Seguros e Resilientes

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado (curso 138 de 207 na [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–26 de 50 já estão escritos em português, com os exercícios EX001–EX052 e suas resoluções; os capítulos 27–50 (EX053–EX100) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
6. [Cálculo II](#ch-06)
7. [Probabilidade e estatística](#ch-07)
8. [Arquitetura de computadores](#ch-08)
9. [Programação II](#ch-09)
10. [Ética e segurança em engenharia](#ch-10)
11. [Redes e protocolos](#ch-11)
12. [Sistemas operacionais](#ch-12)
13. [Sistemas de dados](#ch-13)
14. [Engenharia de software](#ch-14)
15. [Fundamentos de segurança](#ch-15)
16. [Engenharia de sistemas](#ch-16)
17. [Fundamentos de controle e realimentação](#ch-17)
18. [Arquitetura de segurança](#ch-18)
19. [Identidade e criptografia](#ch-19)
20. [Infraestrutura crítica e segurança setorial: contexto de engenharia](#ch-20)
21. [Infraestrutura crítica e segurança setorial: requisitos](#ch-21)
22. [Infraestrutura crítica e segurança setorial: modelos de sistema e de dados](#ch-22)
23. [Infraestrutura crítica e segurança setorial: análise de ameaças e de falhas](#ch-23)
24. [Infraestrutura crítica e segurança setorial: métodos I](#ch-24)
25. [Ateliê de projeto I](#ch-25)
26. [Infraestrutura crítica e segurança setorial: alternativas de arquitetura](#ch-26)

Capítulos 27–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-27), até a chegada dos próximos lotes.

As [resoluções](#worked-results) contêm EX001–EX052. Um [glossário](#glossary) e as [referências](#references) fecham o livro.


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

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) escrever uma equação diferencial ordinária (EDO) de primeira ordem para um estoque com vazão de entrada e de saída; (2) resolver analiticamente EDOs lineares de primeira ordem, incluindo a aproximação exponencial ao equilíbrio e sua constante de tempo; (3) resolver EDOs numericamente e controlar o erro devido ao tamanho do passo; e (4) usar séries e sensibilidade (derivadas parciais) para ver qual parâmetro mais importa para uma margem de resiliência. Ele estende o Capítulo 1 e prepara o Capítulo 17 (controle).

### 6.1 Estoques com realimentação viram equações diferenciais

O reservatório do Capítulo 1 tinha uma vazão de saída conhecida e nenhuma vazão de entrada. Estoques reais têm fluxos que dependem do próprio estoque. A água que sai de um tanque aberto por um orifício depende da carga hidráulica acima dele; o cloro residual decai a uma taxa proporcional à sua concentração; a tensão nos terminais de uma bateria cai com seu estado de carga. Quando a taxa depende da quantidade, obtém-se uma equação como $dx/dt = f(x, t)$. O caso importante mais simples é o linear: $dx/dt = -kx + u$, com constante $k > 0$ e entrada $u$.

### 6.2 A solução linear de primeira ordem e a constante de tempo

Com $u$ constante, a solução é $x(t) = x_\infty + (x_0 - x_\infty)e^{-kt}$, em que $x_\infty = u/k$ é o equilíbrio. A **constante de tempo** $\tau = 1/k$ é o tempo para fechar cerca de 63% da diferença; após $3\tau$, cerca de 95% está fechado, e após $5\tau$, cerca de 99%. Os engenheiros usam $\tau$ para raciocinar sobre a rapidez com que um sistema responde a uma mudança — e a rapidez com que responde a um ataque. Exemplo: o cloro livre num tanque de armazenamento decai com uma constante de primeira ordem; se $k = 0.05$ por hora, $\tau = 20$ h. Se a dosagem parar (por falha ou por comando malicioso), o residual cai pela metade em $\ln 2/k \approx 13.9$ h. Essa é a janela em que um operador precisa perceber e agir antes que o residual caia abaixo do mínimo regulatório.

### 6.3 Solução numérica e erro

Na prática, a maioria das EDOs é não linear ou movida por entradas medidas, então você as resolve numericamente. O método de Euler explícito, $x_{n+1} = x_n + h f(x_n, t_n)$, tem erro global proporcional ao passo $h$; reduzir $h$ à metade reduz o erro aproximadamente à metade. O método de Heun e o método clássico de Runge–Kutta de quarta ordem reduzem o erro muito mais depressa para o mesmo $h$. Faça sempre uma **verificação de convergência do passo**: se reduzir $h$ à metade muda a resposta que lhe interessa em mais do que sua tolerância, o passo é grande demais. Em sistemas rígidos (stiff) — com alguns componentes muito mais rápidos do que outros —, os métodos explícitos podem se tornar instáveis, a menos que $h$ seja muito pequeno; Euler aplicado a $dx/dt = -kx$ é instável para $h > 2/k$.

### 6.4 Sensibilidade: qual suposição importa?

Uma margem de projeto depende de vários parâmetros: nível inicial, demanda, taxa de vazamento, capacidade das bombas. A derivada parcial da margem em relação a cada parâmetro, multiplicada pela faixa plausível desse parâmetro, mostra qual incerteza domina. Para a autonomia $T = V/q$ com demanda constante, $\partial T/\partial V = 1/q$ e $\partial T/\partial q = -V/q^2$; um erro de 10% na demanda move $T$ aproximadamente tanto quanto um erro de 10% no volume utilizável, mas no sentido oposto. As séries de Taylor dão a mesma percepção para modelos não lineares: perto de um ponto nominal, $f(x + \Delta) \approx f(x) + f'(x)\Delta$.

### 6.5 Exemplo resolvido: perda da dosagem de cloro (sintético)

O residual na saída de Hollin Hill, na LRWA, é mantido em 0,8 mg/L; o mínimo operacional sintético é de 0,2 mg/L. Com a dosagem parada e decaimento de primeira ordem $k = 0.05$ h⁻¹, o residual atinge 0,2 mg/L quando $0.8e^{-0.05t} = 0.2$, isto é, $t = \ln 4 / 0.05 \approx 27.7$ h. Se o tempo quente elevar $k$ para 0,08 h⁻¹, a janela encolhe para 17,3 h. A equipe de projeto escreve o requisito R9: *a perda da dosagem deverá gerar alarme em até 15 minutos, independentemente dos próprios relatórios de estado do controlador de dosagem* — porque um controlador comprometido poderia informar operação normal. A EDO se transformou num requisito de tempo de detecção com margem.

### 6.6 Atividade prática

Modifique o Laboratório 1 para incluir uma vazão de entrada constante de 120 m³/h vinda de uma única bomba sobrevivente e um vazamento de primeira ordem de $0.01V$ m³/h. Integre pelo método de Euler com três tamanhos de passo e encontre analiticamente o nível de equilíbrio fazendo $dV/dt = 0$, com a demanda substituída por sua média. Informe o nível de equilíbrio e compare-o com a capacidade e com o piso do reservatório. Com uma bomba a 120 metros cúbicos por hora contra uma demanda média de 150, o estoque precisa continuar caindo, a menos que o vazamento compense a diferença, então verifique se sua resposta analítica é fisicamente possível antes de confiar nela. Depois confirme que as execuções de Euler convergem à medida que o passo diminui. O objetivo do exercício é a combinação: uma verificação analítica, um resultado numérico e um teste de convergência que concordam entre si.

### 6.7 Erros comuns e limites

- Usar decaimento exponencial quando o processo não é de primeira ordem.
- Informar uma solução numérica sem verificação do passo.
- Ignorar que os parâmetros (taxas de decaimento, demanda) variam com a temperatura e a estação do ano.
- Analisar a sensibilidade um parâmetro de cada vez quando os parâmetros interagem; para interações fortes, use métodos globais ([Saltelli et al., 2008](https://doi.org/10.1002/9780470725184)).

No exemplo do cloro, uma equipe que usasse o ano inteiro a constante de decaimento de tempo frio acreditaria ter 27,7 horas quando o verão deixa cerca de 17. O alarme de 15 minutos de R9 foi escolhido com essa faixa sazonal em mente, e é por isso que o requisito não depende da constante exata.

### Exercícios — capítulo 6

**EX011 — Da constante de tempo ao requisito.** *Objetivo:* transformar dinâmica num requisito de tempo de detecção. *Entradas:* §6.5. *Passos:* (1) calcule a janela com $k = 0.12$ h⁻¹; (2) se os operadores precisam de 4 h para restabelecer a dosagem manualmente, calcule o último instante aceitável para o alarme; (3) escreva o requisito. *Evidência esperada:* números e requisito. *Rubrica:* 3 = janela e margem corretas e um requisito verificável independente do controlador; 2 = um deslize; 1 = apenas números; 0 = nada.

**EX012 — Estabilidade de Euler.** *Objetivo:* ver a instabilidade numérica. *Entradas:* $dx/dt = -kx$, $k = 0.5$, $x_0 = 1$. *Passos:* calcule cinco passos de Euler com $h = 1$, $h = 3$ e $h = 5$ e compare com a solução exata. *Evidência esperada:* tabela e explicação. *Rubrica:* 3 = valores corretos e a instabilidade para $h > 2/k$ explicada; 2 = valores certos, explicação fraca; 1 = apenas um tamanho de passo; 0 = nada.

### Síntese do capítulo

Quando um fluxo depende do estoque, escreva uma EDO. Sistemas lineares de primeira ordem se aproximam do equilíbrio exponencialmente, com constante de tempo $\tau$; esse número se torna um requisito de detecção e resposta. Resolva numericamente com verificações de convergência e atenção à estabilidade. Use a sensibilidade para descobrir qual suposição domina uma margem e projete uma detecção que não dependa do componente sob suspeita.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 50

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) aplicar a regra de Bayes a alarmes e explicar o problema da taxa-base; (2) calcular a disponibilidade de caminhos redundantes com e sem falha de causa comum; (3) modelar eventos raros com a distribuição de Poisson; e (4) resumir dados com uma incerteza honesta, incluindo quando desconfiar de uma amostra pequena. Ele se apoia nos capítulos 1–6 e prepara os capítulos 23 (análise de falhas), 29 (medição) e 32 (confiabilidade).

### 7.1 Probabilidade como modelo de incerteza

Uma probabilidade é um número entre 0 e 1 associado a um evento sob um modelo. Os engenheiros usam três leituras: frequência de longo prazo (falhas de bombas por ano numa frota), grau de crença (a estimativa de um especialista sobre a capacidade de um adversário) e margem de projeto (uma meta como 99,9% de disponibilidade). Deixe explícito qual delas você quer dizer; misturá-las é o modo como os registros de riscos viram ficção. As regras centrais: $P(A \cup B) = P(A) + P(B) - P(A\cap B)$; $P(A \cap B) = P(A)P(B\mid A)$; independência significa $P(B\mid A) = P(B)$.

### 7.2 A regra de Bayes e o problema da taxa-base

$P(H\mid E) = P(E\mid H)P(H)/P(E)$. Aplique-a a um alarme de intrusão: suponha que ataques ocorram em 0,1% das janelas de uma hora, que o detector dispare em 95% dos ataques (taxa de verdadeiros positivos) e em 1% das janelas benignas (taxa de falsos positivos). A probabilidade de que um alarme signifique um ataque é de apenas cerca de 8,7%. A maioria dos alarmes é falsa mesmo para um detector "99% preciso", porque as janelas benignas superam de longe os ataques. É por isso que os operadores aprendem a ignorar alarmes — e por isso que o projeto de alarmes precisa informar a taxa esperada de alarmes e o **valor preditivo positivo**, e não apenas a acurácia. [Sommer and Paxson (2010)](https://doi.org/10.1109/SP.2010.25) discutem esse e outros obstáculos relacionados à detecção de anomalias em redes operacionais.

### 7.3 Redundância e causa comum

Se um caminho de comunicação está disponível com probabilidade $a$ e os caminhos falham de forma independente, $n$ caminhos dão $1-(1-a)^n$. A independência é a suposição que falha na prática: caminhos que compartilham um alimentador de energia, um fornecedor, uma configuração ou uma vulnerabilidade explorável falham juntos. O **modelo do fator beta** atribui uma fração $\beta$ da indisponibilidade de cada unidade a causas comuns que derrubam todas as unidades de uma vez. Com $a = 0.98$ e $\beta = 0.05$, dois caminhos têm indisponibilidade ≈ 0,00136 em vez de 0,0004: a causa comum domina. Em segurança, uma vulnerabilidade de software idêntica nos dois caminhos é uma causa comum com $\beta$ próximo de 1 diante de um adversário que a conhece.

### 7.4 Eventos raros: o modelo de Poisson

Se os eventos chegam de forma independente a uma taxa média $\lambda$ por ano, o número de eventos num ano segue uma Poisson: $P(N=k) = e^{-\lambda}\lambda^k/k!$. Com $\lambda = 0.5$ faltas longas de energia da rede por ano, $P(N \ge 1) \approx 0.39$. O modelo de Poisson supõe taxa constante e independência; tempestades, campanhas de ataques e envelhecimento violam ambas, então trate-o como uma primeira aproximação. Para a LRWA, uma falta longa de energia da rede, de mais de quatro horas, é o evento que testa R5 e a reserva do hospital ao mesmo tempo. Se as faltas se agrupam em tempestades, o valor de Poisson subestima a chance de duas faltas num intervalo de dias, então a equipe do TMRP o confere contra os registros de interrupções da distribuidora antes de usá-lo na árvore de falhas.

### 7.5 Descrever dados com honestidade

Informe um valor central com a dispersão (mediana e intervalo interquartil para dados assimétricos, como durações de interrupções), o tamanho da amostra e o modo como os dados foram coletados. Um intervalo de confiança descreve a incerteza amostral sob um modelo; ele não diz nada sobre viés naquilo que foi registrado. Amostras pequenas de eventos raros são especialmente traiçoeiras: zero falhas em 3 anos de operação não significa risco zero. A "regra de três" dá um limite superior aproximado de 95% de $3/n$ para uma taxa quando 0 eventos são observados em $n$ tentativas ou unidades de tempo.

### 7.6 Exemplo resolvido: a LRWA deve acionar o engenheiro de sobreaviso? (sintético)

O TMRP propõe um detector de anomalias de rede no centro de controle com as taxas da §7.2. Avaliado em janelas de uma hora, ele acionaria o sobreaviso cerca de 0,26 vez por dia — aproximadamente uma vez a cada quatro dias — e cerca de 91% dos acionamentos seriam falsos. A equipe decide: acionar apenas quando o alarme de rede coincidir com uma anomalia de processo (mudança inesperada de setpoint ou desequilíbrio de vazão) e encaminhar os alarmes de rede isolados para uma fila de revisão no dia útil seguinte. A decisão é justificada pela taxa-base, e seu custo — resposta mais lenta a um ataque furtivo apenas de rede — é registrado no registro de riscos.

### 7.7 Atividade prática: Laboratório 4

```python
# Lab 4 - base rates, redundancy and rare events (synthetic numbers, offline)
import math
prior, tpr, fpr = 0.001, 0.95, 0.01
ppv = tpr * prior / (tpr * prior + fpr * (1 - prior))
print(f"P(attack | alarm) = {ppv:.3f}")
alarms_per_day = 24 * (tpr * prior + fpr * (1 - prior))
print(f"expected alarms per day (hourly windows) = {alarms_per_day:.3f}")
a = 0.98
for n in (1, 2, 3): print(f"{n} independent paths at {a}: availability {1 - (1 - a) ** n:.6f}")
beta = 0.05   # beta-factor common-cause share of unavailability
q = 1 - a
print(f"2 paths with beta={beta}: unavailability {(1 - beta) ** 2 * q ** 2 + beta * q:.6f}")
lam = 0.5
print(f"P(>=1 grid outage >4 h per year | lambda={lam}) = {1 - math.exp(-lam):.3f}")
print(f"P(>=2) = {1 - math.exp(-lam) * (1 + lam):.4f}")
```

Saída esperada:

```text
P(attack | alarm) = 0.087
expected alarms per day (hourly windows) = 0.263
1 independent paths at 0.98: availability 0.980000
2 independent paths at 0.98: availability 0.999600
3 independent paths at 0.98: availability 0.999992
2 paths with beta=0.05: unavailability 0.001361
P(>=1 grid outage >4 h per year | lambda=0.5) = 0.393
P(>=2) = 0.0902
```

As duas primeiras linhas repetem o resultado da taxa-base do exemplo resolvido: menos de um alarme em dez seria um ataque real, e o detector acionaria o sobreaviso cerca de uma vez a cada quatro dias. As linhas de redundância mostram com que rapidez caminhos independentes melhoram a disponibilidade, e a linha do fator beta mostra como uma causa comum de cinco por cento elimina a maior parte desse ganho. As linhas de Poisson dão a chance de pelo menos uma, e de pelo menos duas, faltas longas de energia da rede num ano, à taxa suposta pela LRWA.

### 7.8 Erros comuns e limites

- Informar a acurácia de um detector sem a taxa-base e o valor preditivo.
- Multiplicar disponibilidades como se fossem independentes quando os caminhos compartilham causas.
- Usar Poisson para eventos agrupados.
- Tratar zero falhas observadas como probabilidade zero.
- Estimativas pontuais sem tamanho de amostra e método de coleta.

Cada erro tem um exemplo na LRWA. Acionar o engenheiro de sobreaviso a cada alarme de rede ignora a taxa-base. Tratar os dois caminhos LTE como independentes ignora seu alimentador compartilhado. Usar Poisson para as faltas causadas por tempestades esconde o agrupamento, e três anos tranquilos na PS4 não provam que as bombas não podem falhar juntas.

### Exercícios — capítulo 7

**EX013 — Sensibilidade à taxa-base.** *Objetivo:* ver como o valor preditivo depende da prevalência. *Entradas:* Laboratório 4. *Passos:* calcule o VPP para as probabilidades a priori 0,0001, 0,001 e 0,01 com o mesmo detector, e para a priori 0,001 com FPR 0,001. *Evidência esperada:* quatro valores e uma recomendação sobre qual parâmetro melhorar. *Rubrica:* 3 = valores corretos e a percepção de que reduzir a FPR importa mais em baixa prevalência; 2 = valores certos; 1 = um valor; 0 = nada.

**EX014 — Causa comum na telemetria.** *Objetivo:* quantificar a diversidade. *Entradas:* dois caminhos LTE de operadoras diferentes ($a = 0.98$ cada). *Passos:* calcule a indisponibilidade para $\beta$ = 0, 0,05 e 0,2; nomeie duas causas comuns reais que esses caminhos ainda poderiam compartilhar. *Evidência esperada:* três números e duas causas. *Rubrica:* 3 = números corretos e causas compartilhadas plausíveis (energia da instalação, torre ou backhaul compartilhados, mesmo firmware de modem); 2 = causas genéricas; 1 = um número; 0 = nada.

### Síntese do capítulo

Probabilidade é um modelo; diga de que tipo. A regra de Bayes torna as taxas-base decisivas para os alarmes; a redundância só funciona na medida em que as falhas são independentes, e as causas comuns — incluindo vulnerabilidades compartilhadas — geralmente dominam. O modelo de Poisson é um ponto de partida para eventos raros. Descreva os dados com dispersão, tamanho da amostra e método de coleta, e nunca trate a ausência de falhas observadas como prova de segurança.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 50

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) descrever como um processador, a hierarquia de memória e a E/S interagem, e por que isso importa para o controle em tempo real; (2) explicar a arquitetura de controladores lógicos programáveis (PLCs), RTUs e controladores embarcados; (3) relacionar recursos de hardware — níveis de privilégio, proteção de memória, inicialização segura, raízes de confiança em hardware — a garantias de segurança; e (4) explicar como otimizações de desempenho, como caches e execução especulativa, criam vulnerabilidades. Ele se apoia no Capítulo 3 e prepara o Capítulo 12 (sistemas operacionais).

### 8.1 O modelo de máquina

Um processador busca instruções na memória, decodifica-as e executa-as, e lê e escreve dados em registradores e na memória. A memória é uma hierarquia — registradores, caches, memória principal, armazenamento —, cada nível maior e mais lento. Os dispositivos de E/S se conectam por barramentos e interrupções; uma interrupção suspende a execução normal para que o processador atenda a um dispositivo. O **determinismo** — saber o tempo de pior caso que uma operação leva — importa mais no controle do que a velocidade média: uma rotina de proteção de bomba que normalmente leva 1 ms, mas às vezes 50 ms por causa de uma tempestade de faltas de cache ou da coleta de lixo, pode perder seu prazo.

### 8.2 PLCs, RTUs e controladores embarcados

Um PLC executa um **ciclo de varredura**: lê as entradas, executa o programa do usuário, escreve as saídas, realiza comunicações e diagnósticos, e repete — muitas vezes a cada 10–100 ms. Seu programa é escrito em linguagens padronizadas pela IEC 61131-3 (lógica ladder, diagramas de blocos funcionais, texto estruturado). Uma RTU é projetada para instalações remotas: coleta medições, aplica lógica simples e se comunica por enlaces de longa distância, tolerando conectividade intermitente. Ambos têm vida longa: um equipamento instalado hoje pode funcionar por quinze a vinte e cinco anos, então os recursos de segurança que você escolher agora ainda precisarão ser aceitáveis na década de 2040. Muitos controladores legados aceitam mudanças de programa de qualquer pessoa que consiga alcançá-los pela rede; o Stuxnet explorou o caminho de uma estação de engenharia até a lógica do PLC, como analisado por [Langner (2011)](https://doi.org/10.1109/MSP.2011.67).

### 8.3 Suporte de hardware à segurança

- Os **níveis de privilégio** separam o código do kernel do código de usuário; uma falha no código de usuário não consegue sobrescrever diretamente o kernel.
- As **unidades de proteção de memória** (MPU) e as **unidades de gerenciamento de memória** (MMU) impõem qual código pode acessar qual memória; a MPU é comum em microcontroladores que não têm uma MMU completa.
- A marcação **execute-never** impede que regiões de dados sejam executadas.
- A **inicialização segura** (secure boot) verifica uma assinatura criptográfica em cada estágio do firmware antes de executá-lo, ancorada numa raiz de confiança imutável (código em ROM ou chaves gravadas em fusíveis). Ela protege contra a modificação persistente do firmware, não contra uma imagem corretamente assinada, mas vulnerável.
- Os **módulos de plataforma confiável** (TPMs) e os elementos seguros armazenam chaves de modo que o software não consiga lê-las.

### 8.4 Quando a velocidade cria vazamento

Caches e execução especulativa tornam os processadores rápidos ao fazer suposições e manter estado, e esse estado pode vazar. [Kocher et al. (2019)](https://doi.org/10.1109/SP.2019.00002) mostraram que a execução especulativa pode ser direcionada para ler memória através de fronteiras de proteção (Spectre). [Kim et al. (2014)](https://doi.org/10.1109/ISCA.2014.6853210) mostraram que acessos repetidos à DRAM podem inverter bits em linhas adjacentes (Rowhammer). Isso importa mais onde código não confiável compartilha o hardware com código confiável — servidores virtualizados do centro de controle, nuvem compartilhada — e menos num PLC de propósito único. A lição de engenharia: o hardware faz parte da superfície de ataque, e um isolamento que depende de hardware compartilhado precisa ser justificado.

### 8.5 Exemplo resolvido: escolhendo uma plataforma de RTU (sintético)

O TMRP compara duas RTUs candidatas. *RTU-A:* madura, determinística, sem inicialização segura, atualizações de firmware sem assinatura, mudanças de programa autenticadas apenas por uma senha compartilhada. *RTU-B:* inicialização segura com firmware assinado pelo fornecedor, autenticação baseada em papéis para mudanças de programa, armazenamento de chaves em hardware, mas uma resposta de pior caso 200 ms mais lenta a requisições de comunicação e um produto novo, com histórico limitado em campo. A equipe pontua as duas contra os requisitos: R1 (telemetria autenticada) precisa de armazenamento de chaves — o que favorece a B; R7 (alarme em até 60 s) é atendido por ambas, já que 200 ms são desprezíveis; a manutenibilidade ao longo de 20 anos favorece um fornecedor com um ciclo de vida de desenvolvimento seguro publicado. O registro de decisão escolhe a B para as novas instalações e um gateway para as instalações legadas com RTU-A, com um piloto para coletar dados de confiabilidade em campo antes da implantação em toda a frota.

### 8.6 Atividade prática

Para uma família de microcontroladores ou de PLCs de sua escolha, leia o manual público de segurança do fornecedor (ou uma folha de dados) e preencha uma tabela: separação de privilégios, proteção de memória, inicialização segura, atualizações assinadas, armazenamento de chaves, programação autenticada. Marque cada item como "sim / não / configurável / desconhecido", com a citação da fonte. Use apenas documentos públicos. Registre o título, a versão e a data do documento para cada entrada, porque os recursos de segurança mudam entre versões de firmware. Onde o manual for omisso, marque o recurso como desconhecido em vez de adivinhar, e liste a pergunta que você faria ao fornecedor. A tabela é a mesma comparação que a equipe do TMRP fez entre a RTU-A e a RTU-B, e mostra rapidamente se um produto consegue suportar telemetria autenticada e armazenamento de chaves sem um gateway.

### 8.7 Erros comuns e limites

- Igualar "rápido" a "determinístico".
- Supor que a inicialização segura impede a exploração de firmware assinado.
- Ignorar a vida útil de 20 anos ao escolher recursos criptográficos e de atualização.
- Tratar como absoluto o isolamento de hardware em servidores compartilhados.
- Tratar o marketing do fornecedor como evidência; peça documentação e teste.

A comparação das RTUs mostra esses erros na prática. A RTU-A é determinística, mas não consegue proteger chaves, então a velocidade sozinha não a torna adequada. A inicialização segura da RTU-B não impede uma mudança de lógica maliciosa, mas legitimamente assinada, e é por isso que o acesso de programação baseado em papéis aparece ao lado dela. Ambas ainda precisam ter suporte na década de 2040, e o piloto existe porque as alegações do fornecedor não são evidência de campo.

### Exercícios — capítulo 8

**EX015 — Orçamento do ciclo de varredura.** *Objetivo:* raciocinar sobre determinismo. *Entradas:* varredura de PLC de 20 ms nominais e 45 ms no pior caso; um requisito de proteção da bomba de desarmar em até 100 ms após um sinal de sucção baixa, que passa por filtragem (debounce) em duas varreduras consecutivas. *Passos:* calcule a latência de desarme de pior caso (entrada amostrada logo após uma leitura, duas varreduras para confirmar, escrita da saída). *Evidência esperada:* cálculo e conclusão. *Rubrica:* 3 = pior caso correto, incluindo o atraso de amostragem, e julgamento contra os 100 ms; 2 = atraso de amostragem omitido; 1 = apenas a varredura nominal; 0 = nada.

**EX016 — O que a inicialização segura compra.** *Objetivo:* delimitar um controle com precisão. *Entradas:* a RTU-B da §8.5. *Passos:* liste dois ataques que a inicialização segura impede, dois que ela não impede e o controle complementar para cada um destes últimos. *Evidência esperada:* tabela. *Rubrica:* 3 = escopo exato (impede firmware persistente não assinado; não impede explorações em tempo de execução nem mudanças maliciosas de lógica pela programação legítima), controles correspondentes; 2 = um erro; 1 = genérico; 0 = nada.

### Síntese do capítulo

A arquitetura determina tanto a temporização quanto a confiança. O controle precisa de desempenho de pior caso, não de média. PLCs e RTUs são máquinas de vida longa, baseadas em varreduras, cujos recursos de segurança ainda precisarão ser adequados daqui a décadas. Os mecanismos de hardware — privilégio, proteção de memória, inicialização segura, armazenamento de chaves — dão garantias específicas e limitadas; os recursos de desempenho podem vazar através de fronteiras. Diga exatamente contra o que cada mecanismo protege.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 50

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) estruturar um programa em módulos com interfaces e invariantes claros; (2) implementar máquinas de estados simples para a lógica de protocolos e de equipamentos; (3) escrever testes unitários, incluindo testes de limites e de falhas, e medir o que eles cobrem; e (4) tratar erros, tempo e concorrência de forma deliberada. Ele se apoia no Capítulo 4 e prepara o Capítulo 14 (engenharia de software) e o Capítulo 30 (verificação).

### 9.1 Módulos, interfaces e invariantes

[Parnas (1972)](https://doi.org/10.1145/361598.361623) defendeu que um sistema deve ser decomposto de modo que cada módulo esconda uma decisão de projeto com probabilidade de mudar. Em software de infraestrutura, as mudanças prováveis incluem o protocolo de campo, o historiador e o esquema de autenticação. Esconda cada uma atrás de uma interface: uma `TelemetrySource` que entrega leituras validadas, qualquer que seja o protocolo. Cada módulo deve declarar seus **invariantes** — propriedades sempre verdadeiras sobre seu estado —, por exemplo, "o último contador aceito para cada estação nunca diminui". Escreva os invariantes como asserções nos testes e, onde for barato, como verificações em tempo de execução que falham de modo seguro.

### 9.2 Máquinas de estados

Equipamentos e protocolos têm modos: uma bomba está *parada*, *partindo*, *em funcionamento*, *parando* ou *desarmada*; uma sessão está *não autenticada*, *autenticada* ou *encerrada*. Uma máquina de estados finitos lista os estados, os eventos que causam transições, as guardas das transições e as ações. Escreva-a como uma tabela e implemente-a a partir da tabela, rejeitando qualquer evento não listado para o estado atual. As transições não listadas são onde vivem tanto os bugs quanto os ataques: um comando "stop" chegando durante a *partida*, ou um "write setpoint" chegando antes da autenticação. O controlador de bombas da LRWA, no exemplo resolvido abaixo, é construído exatamente assim, para que seus testes possam enumerar todos os pares.

### 9.3 Testes

Um teste unitário verifica um comportamento de uma unidade. Bons conjuntos de testes incluem: casos típicos; **limites** (mínimo, máximo, logo dentro, logo fora); entradas inválidas; e testes de **regressão** que reproduzem bugs passados. A cobertura mede quais instruções ou ramos os testes executaram; ela diz o que *não* foi testado, não que o código testado está correto. O módulo `unittest` do Python, na biblioteca padrão, basta para este livro. No controlador de bombas da LRWA, os testes de limite incluem o tempo-limite de partida de 30 segundos exatamente em 30 segundos e logo acima disso, e os testes de regressão reproduzem cada bug de transição encontrado no comissionamento, para que uma falha corrigida não possa voltar discretamente numa versão posterior.

### 9.4 Erros, tempo e concorrência

Decida como cada erro é tratado: rejeitado com um motivo, repetido com um limite ou escalado. Nunca engula exceções em silêncio em código de controle ou de segurança. O tempo é uma fonte recorrente de falhas: use relógios monotônicos para intervalos e a hora de relógio sincronizada (com sua fonte registrada) para os logs; trate os saltos de relógio. A concorrência — threads, tarefas assíncronas, múltiplos clientes — cria condições de corrida: dois operadores emitindo setpoints conflitantes, ou uma verificação e uma ação separadas por uma janela em que o estado muda (time-of-check to time-of-use). Prefira um único dono para cada parte do estado, com mensagens para alterá-la.

### 9.5 Exemplo resolvido: uma máquina de estados de bomba (sintético)

O controlador de bombas da LRWA aceita `start`, `stop`, `trip` e `reset`. A tabela: *parada* + `start` (guarda: permissão verdadeira) → *partindo*; *partindo* + `run_confirmed` → *em funcionamento*; *partindo* + tempo-limite de 30 s → *desarmada*; *em funcionamento* + `stop` → *parando*; qualquer estado + `trip` → *desarmada*; *desarmada* + `reset` (guarda: operador local) → *parada*. A guarda do `reset` importa: exigir uma ação local após um desarme significa que um atacante remoto que provoque um desarme não consegue religar imediatamente a bomba dentro da mesma falha. Os testes cobrem cada transição listada e afirmam que todo par não listado (por exemplo, *desarmada* + `start`) é rejeitado e registrado em log.

### 9.6 Atividade prática

Implemente a tabela da §9.5 em cerca de 40 linhas de Python, com um dicionário indexado por `(state, event)`. Escreva casos de `unittest` para todas as transições listadas e um laço que afirme que todo par `(state, event)` não listado levanta um erro. Conte os pares não listados. Seu laço deve imprimir o número de pares não listados e confirmar que cada um levanta um erro e escreve uma linha de log. Depois acrescente um teste mostrando que um reset remoto após um desarme é recusado, porque a guarda exige um operador local. Esse teste protege a propriedade com que o exemplo resolvido mais se importa: um atacante que desarma uma bomba remotamente não consegue religá-la diretamente dentro da mesma falha. Mantenha a tabela e os testes num único arquivo, para que um revisor possa compará-los.

### 9.7 Erros comuns e limites

- Implementar a lógica de estados com flags espalhadas em vez de uma tabela explícita.
- Ramos padrão que aceitam eventos desconhecidos.
- Usar a hora de relógio para tempos-limite.
- Testes que só exercitam o caminho feliz; igualar cobertura a correção.
- Tratamento silencioso de exceções.

Cada erro derrota uma propriedade da máquina de estados da bomba. Flags espalhadas tornam impossível listar todas as transições. Um ramo padrão deixaria passar um comando de partida com a bomba desarmada. Um tempo-limite baseado na hora de relógio poderia disparar cedo demais, ou nunca, após um salto de relógio, e uma exceção engolida no caminho do reset deixaria a bomba num modo desconhecido.

### Exercícios — capítulo 9

**EX017 — Conte e teste as transições não listadas.** *Objetivo:* raciocinar sobre completude. *Entradas:* §9.5 (estados: stopped, starting, running, stopping, tripped; eventos: start, stop, trip, reset, run_confirmed, timeout, stop_confirmed — acrescente *stopping* + `stop_confirmed` → *stopped*). *Passos:* conte o total de pares, os pares listados e os não listados; dê três pares não listados cuja rejeição tenha uma justificativa de segurança operacional ou de segurança da informação. *Evidência esperada:* contagens e justificativa. *Rubrica:* 3 = contagens corretas e justificativas significativas; 2 = erro de contagem; 1 = sem justificativa; 0 = nada.

**EX018 — Invariante contra repetição.** *Objetivo:* expressar e testar um invariante. *Entradas:* o `Receiver` do Laboratório 8. *Passos:* escreva o invariante sobre `last`, um teste unitário que envie os contadores 1, 2, 2, 1, 5 e afirme os resultados de aceitação/rejeição e o estado final, e diga um modo de falha do invariante após um reinício do receptor. *Evidência esperada:* código do teste e afirmação. *Rubrica:* 3 = resultados esperados corretos (aceita, aceita, rejeita, rejeita, aceita), problema do reinício identificado (estado perdido → repetições aceitas, a menos que seja persistido ou que as chaves sejam trocadas); 2 = reinício não percebido; 1 = sem teste; 0 = nada.

### Síntese do capítulo

Decomponha em torno das decisões com probabilidade de mudar e declare invariantes. Torne os modos explícitos como máquinas de estados e rejeite tudo o que não estiver listado. Teste limites e falhas, leia a cobertura como um mapa do que não foi testado, trate os erros de forma deliberada, use o relógio certo e dê a cada parte do estado compartilhado um único dono.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 50

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança em engenharia

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) aplicar códigos de ética profissional a decisões de segurança de infraestrutura; (2) explicar a relação entre segurança operacional (safety) e segurança da informação (security) e onde elas entram em conflito; (3) reconhecer os limites legais e de autorização para testes e pesquisas; e (4) tomar e documentar uma decisão ética sob incerteza, incluindo quando escalar. Ele se apoia no Capítulo 5 e enquadra todos os capítulos seguintes, em particular os de testes (capítulos 30 e 40) e de prática (Capítulo 43).

### 10.1 Os deveres de um engenheiro

Os códigos profissionais convergem para uma hierarquia: colocar acima de tudo a segurança, a saúde e o bem-estar do público; agir dentro da própria competência; ser honesto e objetivo; evitar conflitos de interesse; proteger informações confidenciais. O [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics) faz da segurança pública o primeiro cânone fundamental; o [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) pede aos profissionais de computação que evitem danos e sejam honestos sobre as capacidades e os limites dos sistemas. Em infraestrutura crítica, o público é concreto: pacientes em diálise, domicílios sem água, pessoas esperando uma ambulância. O dever não é cumprido seguindo instruções se o resultado for um dano público previsível.

### 10.2 Segurança operacional e segurança da informação juntas

A **segurança operacional** (safety) protege as pessoas e o meio ambiente de danos causados pelo sistema; a **segurança da informação** (security) protege o sistema contra o uso indevido deliberado. Em tecnologia operacional, as duas interagem. Um controle de segurança da informação pode criar um perigo para a segurança operacional — o bloqueio automático de uma conta num console de operador durante uma emergência, ou uma correção que reinicia um controlador durante a execução de um processo. Um mecanismo de segurança operacional pode ser um alvo de segurança da informação: o malware TRITON/TRISIS mirou controladores de sistemas instrumentados de segurança, como descrito no [relatório de análise do malware HatMan da CISA](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). A boa prática trata ambas numa única análise de perigos (Capítulo 33) e dá às funções de segurança operacional independência em relação às redes e aos sistemas que elas protegem.

### 10.3 Autorização e lei

Testar um sistema que você não possui, ou que não tem permissão escrita para testar, pode ser crime, quaisquer que sejam suas intenções, e em infraestrutura pode pôr pessoas em perigo. A autorização precisa ser escrita, específica (sistemas, horários, métodos), dada por alguém com legitimidade para concedê-la, e incluir condições de interrupção. Pesquisas que envolvem pessoas ou dados operacionais precisam de revisão ética e de acordos sobre os dados. Vulnerabilidades que você encontre por acaso devem ir ao dono do ativo de forma privada ou por meio de um programa de divulgação coordenada, como o [programa de CVD da CISA](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program). Os laboratórios deste livro são sintéticos exatamente por essas razões.

### 10.4 Decidir sob incerteza

Um procedimento prático de decisão ética: (1) declare a decisão e quem é afetado; (2) identifique os deveres e os fatos que pesam sobre eles; (3) liste as opções, incluindo escalar e recusar; (4) avalie as consequências para as partes interessadas mais vulneráveis; (5) escolha, documente o raciocínio e as divergências e marque um ponto de revisão. Os engenheiros raramente enfrentam dilemas limpos; com mais frequência, o problema é a pressão para aprovar algo que ainda não se mostrou funcional. "Não verificado" é uma resposta honesta e suficiente. No exemplo resolvido a seguir, o engenheiro de verificação do TMRP usa exatamente esses cinco passos.

### 10.5 Exemplo resolvido: a aprovação no prazo final (sintético)

O prazo de comissionamento do TMRP é sexta-feira. O teste T3 (limites de setpoint) falhou: o controlador da PS4 aceita um setpoint fora da faixa segura quando enviado como valor NaN. O fornecedor propõe comissionar com uma nota para corrigir na próxima versão. Como engenheiro de verificação, você aplica o procedimento: as pessoas afetadas incluem os pacientes do hospital, se a PS4 se comportar de forma imprevisível; seu dever é para com a segurança pública e o relato honesto; as opções são (a) assinar, (b) recusar, (c) comissionar com um controle compensatório — escritas remotas de setpoint desabilitadas no gateway, operação apenas local para a PS4 — e uma correção datada. Você recomenda (c), registra T3 como reprovado, não dispensado, e exige um novo teste antes que as escritas remotas sejam habilitadas. A decisão é documentada e assinada pelo gerente de operações, que é o dono do risco operacional.

### 10.6 Atividade prática

Escreva um modelo de autorização de uma página para um teste de um sistema sintético: escopo, métodos excluídos, janela de tempo, condições de interrupção, contatos, tratamento de dados e aprovação. Preencha o modelo para um teste de bancada do gateway de telemetria da LRWA, e não para uma estação em operação. Diga quem pode assiná-lo, liste os métodos excluídos, como qualquer tráfego dirigido a RTUs reais, e dê condições de interrupção que um testador consiga reconhecer sem interpretação. Inclua um contato que possa interromper o teste a qualquer momento e uma regra sobre o que acontece depois com os dados capturados. Um modelo que permitisse a alguém testar a PS4 durante um período de alta demanda falhou em seu propósito.

### 10.7 Erros comuns e limites

- Tratar a ética como uma lista de verificação de conformidade, em vez de raciocinar sobre danos.
- "Permissão verbal" para testes.
- Controles de segurança da informação projetados sem considerar a segurança operacional em emergências.
- Aprovar o que não foi verificado porque um cronograma exige.
- Divulgar publicamente fraquezas de infraestrutura sem coordenação.

A aprovação no prazo final do exemplo resolvido mostra vários desses erros de uma vez: pressão para comissionar, um fornecedor oferecendo uma promessa verbal de corrigir depois e um teste reprovado que poderia facilmente ter sido marcado como dispensado. O engenheiro evitou cada um deles ao registrar a falha e acordar por escrito um controle compensatório.

### Exercícios — capítulo 10

**EX019 — Conflito entre segurança operacional e segurança da informação.** *Objetivo:* resolver um controle que põe as operações em perigo. *Entradas:* proposta de bloquear as contas da IHM dos operadores após cinco logins malsucedidos. *Passos:* analise o perigo, proponha uma alternativa que preserve a intenção de segurança e diga como você a verificaria. *Evidência esperada:* análise de meia página. *Rubrica:* 3 = perigo claro (bloqueio durante uma emergência), alternativa que mantém a responsabilização e resiste a tentativas de adivinhação (por exemplo, limitação de taxa com alertas, liberação por presença física, contas de turno com registro em log), verificação declarada; 2 = alternativa fraca; 1 = apenas o perigo; 0 = nada.

**EX020 — Achado incidental.** *Objetivo:* agir dentro da autorização. *Entradas:* ao estudar, para um trabalho do curso, documentos de compras de uma concessionária pública, você nota numa captura de tela uma página de gerenciamento de um controlador de bombas exposta à internet, com o fornecedor e o modelo visíveis. *Passos:* diga o que você não deve fazer, o que deve fazer e para quem, e o que seu trabalho pode dizer. *Evidência esperada:* 150 palavras. *Rubrica:* 3 = nenhum acesso ou sondagem, notificação privada ao dono ou via CVD, trabalho anonimizado; 2 = um passo ausente; 1 = sugere "verificar se é real"; 0 = nada.

### Síntese do capítulo

A segurança pública vem primeiro, relatada com honestidade. A segurança operacional e a segurança da informação precisam ser analisadas juntas, porque cada uma pode derrotar a outra. Teste apenas com autorização escrita e específica; relate os achados incidentais de forma privada. Decida sob incerteza com um procedimento documentado e trate "não verificado" como uma resposta que você tem o direito — e a obrigação — de dar.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 50

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) explicar o modelo em camadas e os papéis de Ethernet, IP, TCP, UDP e dos protocolos de aplicação; (2) descrever protocolos industriais (Modbus/TCP, DNP3, IEC 60870-5-104, OPC UA) e quais propriedades de segurança cada um oferece ou não oferece; (3) montar um orçamento de latência para a telemetria; e (4) expressar a segmentação como zonas e condutos e conferir os fluxos observados contra ela. Ele se apoia nos capítulos 3 e 4 e prepara os capítulos 18 (arquitetura de segurança) e 26 (alternativas de arquitetura).

### 11.1 As camadas e o que elas prometem

As redes são construídas em camadas: física e de enlace (quadros Ethernet num segmento), de rede (pacotes IP roteados entre segmentos), de transporte (o TCP, com fluxos de bytes confiáveis e ordenados; o UDP, com datagramas sem garantia de entrega — o TCP é especificado na [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)) e de aplicação (o protocolo que carrega o significado). Cada camada promete algo limitado. O TCP garante ordem e retransmissão, não autenticidade. O IP roteia, mas endereços de origem podem ser forjados em muitas redes. As propriedades de segurança precisam ser acrescentadas deliberadamente, em geral com TLS ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), IPsec ou autenticação na camada de aplicação.

### 11.2 Protocolos industriais

Os protocolos industriais clássicos foram projetados para redes seriais fechadas. O **Modbus/TCP** (porta 502) transporta códigos de função, como leitura e escrita de registradores, sem autenticação; qualquer um que alcance a porta 502 pode emitir escritas. O **DNP3** é amplamente usado em água e eletricidade; sua extensão Secure Authentication acrescenta autenticação por desafio e resposta para comandos críticos, mas não está implantada universalmente. O **IEC 60870-5-104** é comum nos sistemas elétricos europeus, com extensões de segurança definidas na IEC 62351. O **OPC UA** foi projetado com modos de segurança que oferecem assinatura e cifração, mas eles precisam ser configurados — "None" é uma política válida. A lição é consistente: capacidade do protocolo não é implantação. Verifique o que está configurado.

### 11.3 Latência, jitter e varredura cíclica (polling)

A telemetria costuma ser consultada ciclicamente: o mestre SCADA interroga cada RTU por vez. A latência de ponta a ponta, de um evento físico até a tela de um operador, é a soma da atualização do sensor, da varredura da RTU, da ida e volta no enlace, da espera pela consulta do mestre, do processamento e da atualização da tela. O **jitter** é a variação da latência. Escreva um orçamento, meça cada elemento e compare o total com o requisito; o Capítulo 36 acrescenta as filas. O orçamento da LRWA no Laboratório 5 soma a varredura da RTU, a ida e volta na LTE, a espera pela consulta e a atualização da tela para chegar a um segundo, contra um requisito de 1,5 segundo, mas a espera pela consulta é o elemento que mais varia, e o EX022 mostra como ela domina o pior caso.

### 11.4 Zonas, condutos e listas de permissões

A segmentação divide uma rede em **zonas** com requisitos de segurança semelhantes e controla os **condutos** entre elas. Esse vocabulário vem da [série ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards). Uma política de conduto é uma **lista de permissões** (allowlist): zona de origem, zona de destino, protocolo e porta específicos, e todo o resto negado. Verificar não é ler a configuração do firewall; é conferir os fluxos observados contra a política pretendida, porque as configurações derivam e caminhos não documentados (o modem de acesso remoto de um fornecedor, um laptop com duas interfaces de rede) contornam os firewalls. A revisão de fluxos da LRWA, abaixo, mostra por quê.

### 11.5 Exemplo resolvido: revisão de fluxos da LRWA (sintético)

A LRWA define as zonas: *enterprise* (corporativa), *dmz*, *control* (servidores SCADA), *field* (RTUs) e *eng* (estações de engenharia). Os condutos pretendidos estão listados no Laboratório 5. Uma semana de registros de fluxo mostra três violações: um host corporativo falando Modbus diretamente com uma RTU de campo (um script de relatório esquecido que contorna a DMZ), uma estação de engenharia abrindo SSH diretamente para uma RTU em vez de passar pelo jump host da zona de controle, e um servidor SCADA fazendo consultas DNS a um resolvedor público. Cada uma é uma constatação com um dono: remover o script e servir seus dados a partir do historiador da DMZ; encaminhar o acesso de engenharia pelo jump host; apontar o DNS do SCADA para um resolvedor interno, ou para nenhum.

### 11.6 Atividade prática: Laboratório 5

```python
# Lab 5 - check observed flows against a zone-conduit allowlist (synthetic, offline)
RULES = [  # (src_zone, dst_zone, protocol, port)
    ("control", "field", "tcp", 502), ("control", "dmz", "tcp", 443), ("dmz", "enterprise", "tcp", 443),
    ("eng", "control", "tcp", 22), ("field", "control", "udp", 20000)]
ZONE = {"10.1.0.": "control", "10.2.0.": "field", "10.3.0.": "dmz", "10.4.0.": "enterprise", "10.5.0.": "eng"}
def zone(ip): return next((z for p, z in ZONE.items() if ip.startswith(p)), "unknown")
FLOWS = [("10.1.0.5", "10.2.0.31", "tcp", 502), ("10.4.0.77", "10.2.0.31", "tcp", 502),
         ("10.2.0.31", "10.1.0.5", "udp", 20000), ("10.3.0.9", "10.4.0.20", "tcp", 443),
         ("10.5.0.12", "10.2.0.33", "tcp", 22), ("10.1.0.5", "8.8.8.8", "udp", 53),
         ("10.1.0.6", "10.3.0.9", "tcp", 443)]
for s, d, p, port in FLOWS:
    ok = (zone(s), zone(d), p, port) in RULES
    print(f"{s:>10} {zone(s):>10} -> {d:<10} {zone(d):<10} {p}/{port:<5} {'allowed' if ok else 'VIOLATION'}")
budget = {"rtu_scan": 120, "lte_rtt": 180, "scada_poll_wait": 500, "operator_view": 200}
print("end-to-end latency budget ms:", sum(budget.values()), "vs requirement 1500")
```

Saída esperada:

```text
  10.1.0.5    control -> 10.2.0.31  field      tcp/502   allowed
 10.4.0.77 enterprise -> 10.2.0.31  field      tcp/502   VIOLATION
 10.2.0.31      field -> 10.1.0.5   control    udp/20000 allowed
  10.3.0.9        dmz -> 10.4.0.20  enterprise tcp/443   allowed
 10.5.0.12        eng -> 10.2.0.33  field      tcp/22    VIOLATION
  10.1.0.5    control -> 8.8.8.8    unknown    udp/53    VIOLATION
  10.1.0.6    control -> 10.3.0.9   dmz        tcp/443   allowed
end-to-end latency budget ms: 1000 vs requirement 1500
```

Três dos sete fluxos são violações, e cada uma corresponde a uma constatação do exemplo resolvido: o script de relatório corporativo falando Modbus com uma RTU de campo, a estação de engenharia abrindo SSH diretamente para uma RTU em vez de passar pelo jump host, e um servidor SCADA consultando um resolvedor DNS público. A linha do orçamento de latência mostra um total de um segundo contra o requisito de 1,5 segundo, mas esse valor usa valores típicos, então trate-o como ponto de partida para a análise de pior caso do EX022, e não como evidência de que R7 foi atendido.

### 11.7 Erros comuns e limites

- Igualar a cifração numa camada à proteção de ponta a ponta.
- Supor que a segurança opcional de um protocolo industrial está habilitada.
- Verificar a segmentação apenas lendo configurações.
- Orçamentos de latência com médias em vez de piores casos.
- Listas de permissões por host em vez de por função, que se tornam impossíveis de manter.

A revisão de fluxos da LRWA ilustra diretamente o terceiro erro: a configuração do firewall parecia correta, mas uma semana de registros de fluxo mostrou três violações. Ler as configurações não teria encontrado nenhuma delas. Listas de permissões escritas por host também teriam exigido edições constantes à medida que as RTUs fossem acrescentadas.

### Exercícios — capítulo 11

**EX021 — Estenda a verificação da política.** *Objetivo:* encontrar violações por função. *Entradas:* Laboratório 5. *Passos:* (1) acrescente um fluxo de `10.2.0.31` para `10.4.0.77` em TCP/445; (2) acrescente uma regra para que a estação de engenharia só alcance as RTUs por um jump host na zona de controle, e modele os dois saltos; (3) execute de novo e relate. *Evidência esperada:* mudanças no código e saída. *Rubrica:* 3 = nova violação detectada, modelo de dois saltos correto, nenhuma regra enfraquece a proteção do campo; 2 = um problema; 1 = não executado; 0 = nada.

**EX022 — Latência contra o requisito.** *Objetivo:* orçar a latência de pior caso. *Entradas:* varredura da RTU de 120 ms, ida e volta na LTE de 180 ms típicos / 900 ms no percentil 99, espera pela consulta de até um ciclo completo de 1,3 s (Laboratório 13), atualização da tela do operador de 200 ms; requisito: 95% dos alarmes na tela em até 1,5 s e todos em até 5 s. *Passos:* calcule os totais típico e de pior caso; julgue as duas cláusulas; proponha uma mudança de projeto. *Evidência esperada:* tabela. *Rubrica:* 3 = somas corretas, espera pela consulta reconhecida como dominante, mudança proposta (relato por exceção ou alarmes não solicitados); 2 = uma soma errada; 1 = apenas o típico; 0 = nada.

### Síntese do capítulo

Cada camada de rede promete algo estreito; a autenticidade precisa ser acrescentada. Os protocolos industriais variam em capacidade de segurança, e capacidade não é configuração. Orce a latência com piores casos. Expresse a segmentação como zonas e condutos com listas de permissões e verifique-a contra os fluxos observados, e não contra as configurações pretendidas.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 50

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) explicar processos, threads, escalonamento, gerenciamento de memória e sistemas de arquivos; (2) distinguir sistemas operacionais de propósito geral e de tempo real e escolher entre eles; (3) aplicar os mecanismos de segurança do sistema operacional — contas, permissões, isolamento, registro em log, aplicação de correções — aos servidores do centro de controle e às estações de engenharia; e (4) planejar a aplicação de correções e o endurecimento sob as restrições de disponibilidade da tecnologia operacional. Ele se apoia no Capítulo 8 e prepara os capítulos 18 e 39.

### 12.1 O que um sistema operacional faz

Um sistema operacional multiplexa o hardware entre os programas e oferece abstrações: **processos** (espaços de endereçamento isolados), **threads** (execução concorrente dentro de um processo), **memória virtual**, **arquivos** e **dispositivos**. O kernel executa com privilégios; as aplicações pedem serviços por meio de chamadas de sistema. O escalonador decide qual thread executa; sua política determina a latência. Na LRWA, os servidores SCADA e as estações de engenharia executam sistemas operacionais de propósito geral, enquanto a lógica de proteção das bombas executa nas RTUs e nos PLCs de cada estação. Saber qual código executa onde diz quais máquinas precisam de garantias de tempo real e quais precisam de endurecimento, aplicação de correções e registro em log do tipo descrito abaixo.

### 12.2 Sistemas operacionais de tempo real

Um sistema operacional de **tempo real** garante resposta limitada: as tarefas com prazos são escalonadas de modo que, se a análise disser que elas cabem, elas cumprem seus prazos. O escalonamento por prioridade fixa com atribuição de prioridades rate-monotonic é uma abordagem clássica; a análise de Liu e Layland dá um limite suficiente de utilização para tarefas periódicas sob essa política. Os sistemas operacionais de propósito geral (Windows, Linux de desktop) otimizam a vazão e a equidade; sua latência de pior caso não é limitada sem configuração especial. Regra: as funções de proteção executam em controladores de tempo real; as funções de supervisão (IHM, historiador) podem executar em sistemas de propósito geral.

### 12.3 Mecanismos de segurança do sistema operacional

- **Privilégio mínimo:** os serviços executam sob contas dedicadas, apenas com os direitos necessários; nada de contas de administrador compartilhadas. [Saltzer and Schroeder (1975)](https://doi.org/10.1109/PROC.1975.9939) apresentaram o privilégio mínimo, os padrões à prova de falhas, a mediação completa e a economia de mecanismo como princípios de projeto que continuam válidos.
- **Controle de acesso:** permissões de arquivos e de objetos; controle de acesso obrigatório onde estiver disponível.
- **Lista de permissões de aplicações:** apenas executáveis aprovados executam — prático em hosts de TO de propósito único, cujo software raramente muda.
- **Registro em log:** autenticação, uso de privilégios, mudanças de serviços e criação de processos, encaminhados para fora do host.
- **Endurecimento:** remover serviços não usados, fechar portas não usadas, desabilitar a execução automática de mídias removíveis.
- **Aplicação de correções:** aplicar as atualizações de segurança, testadas e agendadas.

### 12.4 Aplicação de correções sob restrições de disponibilidade

Sistemas de TO muitas vezes não podem ser reiniciados à vontade, e os fornecedores podem suportar apenas níveis específicos de correções. A aplicação de correções é, portanto, baseada em risco: avalie a explorabilidade de cada vulnerabilidade na sua arquitetura (o serviço vulnerável é alcançável?), sua consequência e o risco para a disponibilidade de aplicá-la; depois corrija, mitigue (bloqueie a porta, desabilite o recurso) ou aceite com uma data de revisão. Mantenha um sistema de teste que espelhe a produção para validar as correções. O [guia de TO do NIST (SP 800-82 Rev. 3)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) discute esses compromissos.

### 12.5 Exemplo resolvido: endurecendo os servidores SCADA (sintético)

Os dois servidores SCADA da LRWA executam um sistema operacional de propósito geral. A linha de base do TMRP: contas de serviço dedicadas; os operadores entram com contas nominais; administrador local desabilitado, exceto uma conta de emergência (break-glass) cuja senha fica lacrada e cujo uso gera alarme; lista de permissões habilitada após um período de aprendizado de duas semanas num ambiente de teste; armazenamento USB bloqueado; logs encaminhados ao coletor da DMZ; uma janela mensal de correções alternando entre os servidores, para que um deles esteja sempre em funcionamento. O risco residual — o fornecedor certifica as correções 30 dias após o lançamento — é mitigado por regras de rede que expõem ao campo e à DMZ apenas as portas da aplicação SCADA.

### 12.6 Atividade prática

Numa máquina virtual Linux que seja sua, liste os serviços em escuta (`ss -tulpn`), as contas locais com shell de login e os serviços habilitados. Escreva uma nota de endurecimento: quais serviços você desabilitaria num host historiador de propósito único e por quê. Não execute isso contra nenhum sistema que não seja seu. Registre a saída com a data e o nome da máquina e, para cada serviço que você desabilitaria, anote o que quebraria se você estivesse errado. Um host historiador na LRWA precisaria de seu serviço de banco de dados e do encaminhamento de logs, mas raramente de um servidor de e-mail ou de um serviço de compartilhamento de arquivos. Compare sua lista com as medidas de endurecimento do exemplo do SCADA e explique qualquer diferença. O exercício treina o hábito de perguntar por que cada serviço está em execução antes de decidir se ele deveria estar.

### 12.7 Erros comuns e limites

- Executar a lógica de proteção num sistema operacional de propósito geral.
- Contas compartilhadas, que destroem a responsabilização.
- Aplicar correções pelo calendário sem avaliar a explorabilidade — ou nunca aplicá-las porque "a TO é especial".
- Logs mantidos apenas no host que um atacante controla.
- Lista de permissões ligada em produção sem um período de aprendizado.

O endurecimento do SCADA da LRWA evita cada um desses erros: contas nominais substituem as compartilhadas, os logs saem do host, a lista de permissões veio após duas semanas de aprendizado num ambiente de teste, e a janela mensal de correções alterna entre os dois servidores. O risco residual está registrado.

### Exercícios — capítulo 12

**EX023 — Verificação rate-monotonic.** *Objetivo:* testar a escalonabilidade com o limite de Liu–Layland. *Entradas:* três tarefas periódicas numa RTU: (C=2 ms, T=10 ms), (C=4 ms, T=40 ms), (C=10 ms, T=100 ms). *Passos:* calcule a utilização; calcule o limite $n(2^{1/n}-1)$ para $n = 3$; conclua. *Evidência esperada:* números e conclusão. *Rubrica:* 3 = U = 0,40, limite ≈ 0,780, escalonável pelo teste suficiente, com a ressalva de que ultrapassar o limite não provaria a não escalonabilidade; 2 = ressalva ausente; 1 = erro aritmético; 0 = nada.

**EX024 — Decisão de correção.** *Objetivo:* tomar uma decisão de correção baseada em risco. *Entradas:* uma vulnerabilidade de execução remota de código no serviço de compartilhamento de arquivos do sistema operacional; o serviço está habilitado no historiador, mas bloqueado pelo firewall da zona de controle para todas as zonas exceto a de engenharia; a certificação da correção pelo fornecedor está a 30 dias. *Passos:* recomende corrigir / mitigar / aceitar, com controles provisórios e uma data de revisão. *Evidência esperada:* nota de decisão. *Rubrica:* 3 = mitigação agora (desabilitar o serviço ou restringir mais), correção após a certificação, monitoramento, data; 2 = sem controle provisório; 1 = "corrigir imediatamente", ignorando o suporte do fornecedor, ou "aceitar" sem raciocínio; 0 = nada.

### Síntese do capítulo

O sistema operacional determina tanto a temporização quanto a linha de base de segurança. Coloque os prazos em plataformas de tempo real. Aplique privilégio mínimo, lista de permissões, endurecimento e registro em log fora do host. Aplique correções com base no risco avaliado, com procedimentos testados e controles compensatórios quando ainda não puder corrigir, e mantenha um ambiente espelho para tornar isso possível.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 50

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) projetar modelos de dados relacionais e de séries temporais para dados operacionais; (2) explicar transações, consistência e replicação; (3) proteger a integridade dos dados com restrições, proveniência e cadeias de hashes, e dizer exatamente o que cada um detecta; e (4) planejar fluxos de dados entre os sistemas de controle e a análise de dados corporativa sem abrir um caminho para dentro do controle. Ele se apoia nos capítulos 9 e 11 e prepara os capítulos 22 (modelos de dados) e 29 (medição).

### 13.1 Modelos para dados operacionais

[Codd (1970)](https://doi.org/10.1145/362384.362685) introduziu o modelo relacional: dados como relações (tabelas) com chaves, manipulados por operações de conjuntos. Cadastros de ativos, ordens de serviço e contas de usuários se encaixam bem nele. Os dados de processo — milhares de tags amostradas a cada segundo — costumam ir para um **historiador**, um repositório de séries temporais otimizado para acréscimos e consultas por intervalo, muitas vezes com uma compressão que descarta mudanças menores do que uma banda morta. Saiba o que seu historiador descarta: a análise forense pode precisar de valores que ele nunca armazenou. O historiador da LRWA armazena o nível de Hollin Hill com compressão por banda morta, então as mudanças menores do que a banda morta nunca são guardadas.

### 13.2 Transações, consistência e replicação

Uma **transação** agrupa operações de modo que todas aconteçam ou nenhuma aconteça (atomicidade), deixando os dados válidos (consistência), sem interferência de transações concorrentes (isolamento) e sobrevivendo a quedas (durabilidade). A replicação copia os dados para a disponibilidade; quando as réplicas podem discordar, os sistemas escolhem entre consistência e disponibilidade durante uma partição da rede. Para as operações: um alarme reconhecido por um operador não pode reaparecer como não reconhecido após a troca para o servidor reserva (failover); uma mudança de setpoint não pode ser aplicada duas vezes. No par SCADA da LRWA, o failover é o momento em que essas propriedades são testadas: os testes de integração devem confirmar que os alarmes reconhecidos e os setpoints aplicados sobrevivem à troca exatamente uma vez.

### 13.3 Integridade: o que cada mecanismo detecta

- As **restrições** (tipos, faixas, chaves estrangeiras) rejeitam valores impossíveis na entrada.
- Os campos de **proveniência** (origem, hora da coleta, transformação) permitem rastrear um número até sua origem.
- As **somas de verificação** (checksums) detectam corrupção acidental.
- As **cadeias de hashes** ligam cada registro ao anterior, de modo que editar qualquer registro muda todos os hashes posteriores. Elas detectam modificações *se* você tiver uma cópia confiável de um hash posterior (uma **âncora**) guardada em algum lugar que o atacante não consiga alterar. Elas não detectam o truncamento do final, a menos que a âncora inclua a contagem de registros, e não provam que os dados originais eram verdadeiros.
- As **assinaturas digitais** ou os MACs sobre registros ou âncoras os vinculam a quem detém a chave.

### 13.4 Tirar os dados sem deixar os ataques entrarem

As equipes corporativas querem os dados de controle para relatórios e análises. O padrão seguro é empurrar os dados para fora — da zona de controle para uma réplica do historiador na DMZ — e deixar os usuários corporativos consultarem a réplica, nunca o historiador de controle. Onde a consequência de um comprometimento da zona de controle é grave, gateways unidirecionais (diodos de dados) impõem fisicamente o fluxo apenas para fora. A violação do Laboratório 5 — um script corporativo consultando diretamente uma RTU — é o antipadrão. Na LRWA, a réplica do historiador na DMZ atende às equipes de finanças e de ativos, e o script corporativo esquecido, encontrado na revisão de fluxos, está sendo aposentado em favor dela.

### 13.5 Exemplo resolvido: protegendo a linha do tempo do incidente (sintético)

Após uma queda inexplicada do nível do reservatório em 4 de março, no registro sintético, a LRWA precisa preservar o extrato do historiador para a investigação. O Laboratório 6 encadeia por hashes seis leituras diárias e guarda o hash da cabeça no chamado do incidente (a âncora). A edição do valor de 4 de março é detectada no índice 3 e em todos os registros posteriores. A exclusão do último registro não é detectada comparando apenas as cabeças se o atacante também substituir a cabeça armazenada — e é por isso que a âncora vai para um sistema fora do alcance do atacante, junto com a contagem de registros.

### 13.6 Atividade prática: Laboratório 6

```python
# Lab 6 - a hash-chained historian extract detects edits, not deletions at the tail (offline)
import hashlib, json
recs = [{"t": f"2026-03-0{d} 06:00", "tag": "HOLLIN_LVL", "v": v} for d, v in zip(range(1, 7), [78.1, 77.4, 79.0, 41.2, 76.5, 77.9])]
def chain(rs):
    prev, out = "0" * 64, []
    for r in rs:
        h = hashlib.sha256((prev + json.dumps(r, sort_keys=True)).encode()).hexdigest()
        out.append(h); prev = h
    return out
anchor = chain(recs)
print("head:", anchor[-1][:16])
tampered = [dict(r) for r in recs]; tampered[3]["v"] = 74.0
bad = [i for i, (a, b) in enumerate(zip(anchor, chain(tampered))) if a != b]
print("first mismatch at index:", bad[0], "mismatches:", len(bad))
print("truncated head matches stored index 4:", chain(recs[:5])[-1] == anchor[4])
```

Saída esperada:

```text
head: a8407870e41914c1
first mismatch at index: 3 mismatches: 3
truncated head matches stored index 4: True
```

O hash da cabeça é o que a LRWA guarda no chamado do incidente. Editar a leitura de 4 de março para esconder a queda muda o hash no índice três e em todos os registros posteriores, então a edição é detectada onde quer que ocorra. A última linha mostra a fraqueza: uma cadeia construída a partir dos cinco primeiros registros coincide com o hash armazenado no índice quatro, então um atacante que exclua o registro final e substitua a cabeça armazenada passaria despercebido. O EX025 fecha essa lacuna acrescentando a contagem de registros à âncora.

### 13.7 Erros comuns e limites

- Tratar os dados do historiador como completos quando a compressão ou as bandas mortas descartam detalhes.
- Cadeias de hashes sem uma âncora armazenada de forma independente.
- Acreditar que os mecanismos de integridade provam a verdade; eles provam a não modificação desde a ancoragem.
- Conexões bidirecionais de "relatório" para dentro da zona de controle.
- Perder as informações de fuso horário e de fonte do relógio.

A investigação de 4 de março depende de evitar cada um desses erros, das lacunas de compressão a um fuso horário ausente. Um historiador que descarta pequenas mudanças pode ter descartado justamente os valores que mostrariam com que rapidez o nível caiu, uma âncora mantida no servidor do historiador poderia ser reescrita pelo mesmo administrador, e carimbos de tempo sem fuso tornam impossível alinhar a queda com o registro do operador.

### Exercícios — capítulo 13

**EX025 — Truncamento do final.** *Objetivo:* fechar a lacuna de truncamento. *Entradas:* Laboratório 6. *Passos:* (1) mostre que `chain(recs[:5])` coincide com o hash armazenado no índice 4; (2) modifique a âncora para incluir a contagem de registros e mostre que o truncamento é detectado; (3) diga onde a âncora deve ser guardada na LRWA e por quê. *Evidência esperada:* código e saída. *Rubrica:* 3 = demonstração e correção certas, âncora guardada fora do alcance dos administradores do controle e do historiador; 2 = correção incompleta; 1 = não executado; 0 = nada.

**EX026 — Projeto de fluxo de dados.** *Objetivo:* projetar com segurança o acesso para análises. *Entradas:* a equipe de finanças quer dados horários de energia das bombas; a equipe de ativos quer dados de pressão ao vivo para um painel. *Passos:* desenhe (em texto) os fluxos, as zonas e o sentido; diga qual componente impõe o sentido e o que acontece se a réplica da DMZ for comprometida. *Evidência esperada:* descrição dos fluxos e análise das consequências. *Rubrica:* 3 = empurrar para a DMZ, nada entrando no controle, consequência limitada à confidencialidade/integridade dos dados da réplica; 2 = sentido não imposto; 1 = consulta direta ao historiador de controle; 0 = nada.

### Síntese do capítulo

Modele os dados operacionais deliberadamente, saiba o que seu historiador descarta e use transações e replicação com o failover em mente. Cada mecanismo de integridade detecta algo específico: as restrições rejeitam o impossível, as cadeias de hashes detectam edições em relação a uma âncora armazenada de forma independente, as assinaturas vinculam a quem detém a chave — nenhum deles prova a verdade. Mova os dados para fora, para uma DMZ, e nunca deixe que os relatórios se tornem um caminho para dentro do controle.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 50

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) aplicar um ciclo de vida de desenvolvimento seguro de software ao software de infraestrutura; (2) gerenciar requisitos, revisões de projeto, revisão de código e inspeções; (3) gerenciar dependências e a cadeia de suprimentos de software com SBOMs e proveniência; e (4) planejar versões e atualizações para software embarcado e de TO de vida longa. Ele se apoia nos capítulos 5 e 9 e prepara os capítulos 28, 31 e 39.

### 14.1 Por que o processo importa

[Brooks (1987)](https://doi.org/10.1109/MC.1987.1663532) defendeu que as dificuldades essenciais do software — complexidade, conformidade, mutabilidade, invisibilidade — não admitem um avanço único e decisivo. O processo não as remove; ele torna os erros visíveis cedo, quando corrigi-los é barato, e deixa evidências de que o trabalho foi feito. Em infraestrutura crítica, a evidência faz parte do produto: reguladores, seguradoras e donos de ativos vão pedi-la. No gateway do TMRP, essa evidência inclui a revisão do modelo de ameaças, os resultados dos testes e a compilação assinada, que vão todos para o dossiê.

### 14.2 Um ciclo de vida de desenvolvimento seguro

O [NIST Secure Software Development Framework (SP 800-218)](https://csrc.nist.gov/pubs/sp/800/218/final) agrupa as práticas em preparar a organização, proteger o software, produzir software bem protegido e responder a vulnerabilidades. Concretamente: requisitos de segurança e modelos de ameaças com cada funcionalidade; padrões de codificação segura; revisão por pares; análise estática automatizada e testes na integração contínua; sistemas de compilação protegidos; recebimento e divulgação de vulnerabilidades; e correções com avisos claros. Os princípios de [Secure by Design da CISA](https://www.cisa.gov/securebydesign) acrescentam que os fabricantes devem assumir a responsabilidade pelos resultados de segurança dos clientes — padrões seguros, nenhuma senha padrão, linguagens com segurança de memória onde for viável.

### 14.3 Revisões e inspeções

[Fagan (1976)](https://doi.org/10.1147/sj.153.0182) descreveu inspeções formais de projeto e de código, com papéis e listas de verificação definidos, relatando que elas encontravam defeitos mais cedo e de forma mais barata do que os testes. A revisão de código moderna é mais leve, mas mantém os princípios: uma segunda pessoa competente lê cada mudança, com uma lista de verificação que inclui validação de entradas, autenticação, tratamento de erros e registro em log. Métricas de complexidade, como a complexidade ciclomática de McCabe ([McCabe, 1976](https://doi.org/10.1109/TSE.1976.233837)), sinalizam funções difíceis de testar. Na LRWA, cada mudança no código do gateway é lida por um segundo engenheiro com uma lista de verificação.

### 14.4 Dependências e a cadeia de suprimentos

A maior parte do software é montada a partir de componentes de terceiros. Uma **lista de materiais de software (SBOM)** os relaciona para que, quando uma vulnerabilidade for anunciada, você saiba se é afetado ([recursos de SBOM da CISA](https://www.cisa.gov/sbom)). A **proveniência** — evidência verificável de como e a partir de quê um artefato foi construído — protege contra compilações adulteradas; o [framework SLSA](https://slsa.dev/) define níveis de integridade da compilação, e as [compilações reprodutíveis](https://reproducible-builds.org/) permitem que partes independentes confirmem que um binário corresponde ao seu código-fonte.

### 14.5 Versões para sistemas de vida longa

O software de TO pode ser mantido por vinte anos. Planeje: atualizações assinadas; reversão (rollback); implantação em etapas (bancada de teste, uma instalação, frota); janelas de compatibilidade; datas de fim de suporte publicadas com antecedência; e um processo de atualização que funcione quando uma instalação só é alcançável de forma intermitente. Um mecanismo de atualização é ele próprio uma superfície de ataque e precisa ser autenticado. No TMRP, o plano é concreto: o gateway passa da bancada para a PS2 e depois para a PS1, uma imagem de reversão é mantida em cada etapa, e as atualizações precisam chegar a estações que só são alcançáveis de forma intermitente pela LTE. Como os gateways estão registrados como dívida técnica com horizonte de três anos, a data de fim de suporte é publicada desde o início.

### 14.6 Exemplo resolvido: o projeto do gateway de telemetria (sintético)

O TMRP precisa construir um pequeno gateway que acrescente autenticação HMAC para as RTUs legadas da PS1 e da PS2. O plano: requisitos R1, R2 e R7 rastreados até os testes; um modelo de ameaças revisado por um segundo engenheiro; apenas a biblioteca padrão do Python, evitando dependências de terceiros; análise estática e testes unitários na integração contínua; compilações num executor dedicado, com artefatos assinados e um SBOM (trivialmente curto aqui); implantação numa bancada, depois na PS2, depois na PS1; e uma imagem de reversão mantida. Cada etapa deixa um registro no dossiê de evidências (Capítulo 48).

### 14.7 Atividade prática

Escreva um plano de uma página, mapeado ao SSDF, para uma pequena ferramenta que você tenha escrito: para cada um dos quatro grupos de práticas, liste duas práticas concretas e a evidência que cada uma produz. Escolha algo real que você tenha escrito, como o seu interpretador do Laboratório 3, para que as práticas sejam concretas. Para cada prática, nomeie a evidência que ela deixa: um registro de revisão, um relatório de teste, uma compilação assinada ou um modelo de aviso. Se uma prática não deixar nenhuma evidência, mude-a ou admita que ela é apenas uma intenção. Compare seu plano com o plano do gateway do TMRP e anote uma prática que você acrescentaria.

### 14.8 Erros comuns e limites

- Documentos de processo sem as práticas que eles descrevem.
- Revisão de código sem lista de verificação ou sem autoridade para bloquear.
- Dependências baixadas no momento da compilação sem fixação de versão nem proveniência.
- Mecanismos de atualização sem autenticação ou reversão.
- Nenhuma data de fim de suporte publicada.

O plano do gateway do TMRP foi escrito para evitar cada um desses erros. Ele usa apenas a biblioteca padrão, então não há dependências sem versão fixada; as revisões seguem uma lista de verificação; as compilações são assinadas, com um SBOM; a implantação mantém uma imagem de reversão; e os gateways têm um horizonte publicado de três anos.

### Exercícios — capítulo 14

**EX027 — Lista de verificação de revisão.** *Objetivo:* criar uma lista de verificação de revisão para código de infraestrutura. *Entradas:* o código dos laboratórios 3 e 8. *Passos:* escreva uma lista de verificação de dez itens e aplique-a aos dois laboratórios, registrando uma constatação para cada um. *Evidência esperada:* lista de verificação e duas constatações. *Rubrica:* 3 = lista específica (validação de entradas, comparação em tempo constante, tratamento de chaves, caminhos de erro, registro em log, limites) e constatações reais; 2 = lista genérica; 1 = sem constatações; 0 = nada.

**EX028 — Simulação de resposta com SBOM.** *Objetivo:* usar um SBOM numa resposta a vulnerabilidade. *Entradas:* um SBOM sintético que lista `libmodbus 3.1.6`, `openssl 3.0.8`, `zlib 1.2.13` para o firmware da RTU-B, e um aviso sobre um deles. *Passos:* descreva os passos de triagem, do aviso à decisão, incluindo como você determina a explorabilidade na sua implantação. *Evidência esperada:* procedimento. *Rubrica:* 3 = correspondência, análise de alcançabilidade, contato com o fornecedor, controle compensatório, comunicação; 2 = sem alcançabilidade; 1 = "atualizar tudo"; 0 = nada.

### Síntese do capítulo

O processo torna os erros visíveis cedo e deixa evidências. Use um framework reconhecido de desenvolvimento seguro, revise com listas de verificação, meça a complexidade e trate as dependências e as compilações como parte da sua superfície de ataque, com SBOMs e proveniência. Projete versões e atualizações para décadas, com autenticação, implantação em etapas e reversão.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 50

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) definir confidencialidade, integridade e disponibilidade e explicar por que sua prioridade é diferente em infraestrutura; (2) descrever ameaças, vulnerabilidades, risco e controles e relacioná-los numa avaliação de riscos; (3) aplicar princípios de projeto da literatura de segurança; e (4) mapear os controles de um sistema a um framework reconhecido. Ele integra os capítulos 1–14 e prepara os capítulos de arquitetura de segurança e de identidade (18–19) e os capítulos setoriais (do 20 em diante).

### 15.1 As propriedades

A **confidencialidade** limita quem pode ler a informação; a **integridade** garante que a informação e os sistemas não sejam alterados sem autorização; a **disponibilidade** garante acesso oportuno e confiável. Na TI corporativa, a confidencialidade costuma vir na frente. Em infraestrutura, o processo físico vem em primeiro lugar: integridade e disponibilidade do controle, depois a segurança operacional, depois a confidencialidade — embora a confidencialidade dos projetos de rede e das credenciais proteja as demais. [Avizienis et al. (2004)](https://doi.org/10.1109/TDSC.2004.2) colocam a segurança ao lado da confiabilidade, da segurança operacional e da manutenibilidade como atributos da dependabilidade; sua taxonomia de faltas, erros e falhas é usada ao longo de todo este livro.

### 15.2 Ameaça, vulnerabilidade, risco

Uma **ameaça** é uma causa potencial de dano (um ator com capacidade e intenção, ou um perigo natural); uma **vulnerabilidade** é uma fraqueza que uma ameaça pode explorar; o **risco** combina probabilidade e consequência. O [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) descreve a avaliação de riscos como a identificação de fontes e eventos de ameaça, vulnerabilidades, probabilidade e impacto. Em infraestrutura, comece pela consequência: quais são as piores coisas que poderiam acontecer ao serviço e às pessoas? O método [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/), do Idaho National Laboratory, começa assim, perguntando qual perda ou uso indevido de funções seria inaceitável e trabalhando de trás para a frente até o que um adversário precisaria.

### 15.3 Controles e princípios

Os controles são preventivos, detectivos, corretivos ou compensatórios, e técnicos, procedimentais ou físicos. Princípios de projeto de [Saltzer and Schroeder (1975)](https://doi.org/10.1109/PROC.1975.9939): economia de mecanismo, padrões à prova de falhas, mediação completa, projeto aberto, separação de privilégios, privilégio mínimo, mínimo mecanismo comum e aceitabilidade psicológica. Acrescente a **defesa em profundidade** (camadas cujas falhas são independentes) e a **presunção de violação** (assume breach: projetar de modo que o comprometimento de uma camada seja detectado e contido). No projeto do TMRP, o modo manual local com uma chave seletora física é um exemplo de separação de privilégios, e o analisador de cloro independente é uma camada de detecção fora dos sistemas que ele observa.

### 15.4 Frameworks

Os frameworks dão estrutura e um vocabulário comum. O [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) organiza os resultados em Govern, Identify, Protect, Detect, Respond e Recover. O catálogo [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) lista controles; a [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) especifica requisitos para sistemas e componentes de automação industrial, com níveis de segurança; o [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf), do Reino Unido, é baseado em resultados para serviços essenciais. Um framework é uma lista de verificação de resultados, não uma evidência de que um projeto os alcança.

### 15.5 Exemplo resolvido: a primeira tabela de riscos do TMRP (sintético)

| Consequência | Evento de ameaça | Vulnerabilidade | Controle existente | Controle proposto |
|---|---|---|---|---|
| Hospital perde o abastecimento por > 4 h | Comandos de parada forjados para a PS3/PS4 | Modbus sem autenticação sobre LTE | Cifração da operadora | Telemetria autenticada (R1/R2), modo manual local |
| Níveis de cloro inseguros | Setpoint de dosagem manipulado | Nenhum limite de setpoint no controlador | Observação do operador | Limites no lado do controlador (R3), alarme do analisador independente (R9) |
| Perda de visibilidade | Queda da telemetria durante a falta de energia da rede | Bateria do armário com 6 h no fim da vida útil | Nenhum | Bateria de 24 h (R5) |
| Recuperação lenta | Ransomware nos servidores SCADA | Backups on-line, no mesmo domínio | Backups noturnos | Backups off-line, restauração testada (R6) |

Cada linha nomeia primeiro uma consequência em termos de serviço. A tabela é uma hipótese a ser refinada nos capítulos 23 e 27.

### 15.6 Atividade prática

Mapeie cada controle proposto na §15.5 a uma função do CSF 2.0 e a uma família de controles do SP 800-53, citando os documentos. Para cada linha da tabela de riscos do TMRP, escolha a função do CSF que melhor descreve o propósito principal do controle proposto e anote onde um controle serve a duas. A telemetria autenticada é principalmente protetiva, o alarme do analisador independente é principalmente detectivo, e os backups off-line testados apoiam a recuperação. Cite os documentos dos frameworks com suas versões. Depois escreva uma frase para cada linha explicando o que o mapeamento não lhe diz, porque um mapeamento correto ainda não é evidência de que o controle funciona na LRWA.

### 15.7 Erros comuns e limites

- Copiar as prioridades corporativas para a TO.
- Registros de riscos que listam vulnerabilidades sem consequências.
- Camadas de "defesa em profundidade" que compartilham um único ponto de falha.
- Tratar o mapeamento a um framework como prova de segurança.
- Notas de probabilidade sem base declarada.

A primeira tabela de riscos do TMRP evita esses erros ao nomear primeiro cada consequência em termos de serviço, de modo que toda vulnerabilidade fique ligada a um dano, e ao tratar suas probabilidades como hipóteses a refinar nos capítulos seguintes. Suas camadas são conferidas quanto a dependências compartilhadas antes de serem chamadas de independentes.

### Exercícios — capítulo 15

**EX029 — Auditoria de princípios.** *Objetivo:* aplicar princípios de projeto. *Entradas:* o Laboratório 8 e a máquina de estados da bomba da §9.5. *Passos:* para cada um, identifique dois princípios de Saltzer–Schroeder aplicados e um violado ou não tratado, e proponha uma correção. *Evidência esperada:* tabela. *Rubrica:* 3 = princípios atribuídos corretamente, com uma lacuna crível (por exemplo, a chave fixada no código do Laboratório 8 viola a separação/o privilégio mínimo; o projeto aberto é respeitado pelo HMAC); 2 = uma atribuição errada; 1 = apenas nomes; 0 = nada.

**EX030 — Cenário a partir da consequência.** *Objetivo:* começar pela consequência. *Entradas:* o serviço da LRWA. *Passos:* identifique duas consequências inaceitáveis e, para cada uma, as funções que um adversário precisaria usar indevidamente e o controle de engenharia mais barato que tornaria a consequência fisicamente impossível ou limitada. *Evidência esperada:* meia página. *Rubrica:* 3 = consequências em termos de serviço, funções específicas, pelo menos um limite físico projetado (por exemplo, alívio mecânico de sobrepressão, limite por fiação dedicada na bomba de cloro); 2 = todos os controles digitais; 1 = genérico; 0 = nada.

### Síntese do capítulo

A segurança de infraestrutura protege um serviço físico: a integridade e a disponibilidade do controle e a segurança operacional vêm na frente. Comece pela consequência, depois as ameaças e as vulnerabilidades, depois os controles. Aplique princípios de projeto duradouros, empilhe defesas cujas falhas sejam independentes, presuma a violação e use os frameworks como listas de verificação estruturadas — não como evidência.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 50

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) aplicar o ciclo de vida da engenharia de sistemas — concepção, requisitos, arquitetura, projeto, integração, verificação, validação, operação, desativação — a um programa de segurança; (2) decompor as necessidades das partes interessadas em requisitos de sistema e de subsistema com rastreabilidade; (3) gerenciar interfaces e configuração; e (4) integrar a engenharia de segurança à engenharia de sistemas, em vez de acoplá-la depois. Ele se apoia nos capítulos 5 e 14 e enquadra toda a segunda metade do livro.

### 16.1 O ciclo de vida e o V

A engenharia de sistemas gerencia a complexidade passando das necessidades aos requisitos, à arquitetura e aos componentes, e depois subindo de volta pela integração e pela verificação. O **modelo em V** emparelha cada nível de decomposição, à esquerda, com um nível de verificação, à direita: necessidades das partes interessadas com validação, requisitos de sistema com verificação do sistema, projeto de subsistemas com testes de integração, componentes com testes unitários. O [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) descreve esse ciclo de vida e suas revisões técnicas. O desenvolvimento iterativo não abole o V; ele executa Vs menores com mais frequência.

### 16.2 Necessidades, requisitos, rastreabilidade

As necessidades das partes interessadas são o que as pessoas precisam que o sistema alcance, na linguagem delas: "o hospital não pode ficar sem água por mais de quatro horas". Os requisitos de sistema traduzem as necessidades em afirmações verificáveis sobre o sistema (Capítulo 5). A **rastreabilidade** liga cada requisito, para cima, a uma necessidade e, para baixo, a elementos de projeto e à verificação. Um requisito sem pai é excesso de enfeite ou uma necessidade oculta; uma necessidade sem requisito é uma lacuna; um requisito sem verificação é uma afirmação sem sustentação (Capítulo 38 e Laboratório 14).

### 16.3 Interfaces e configuração

A maioria das falhas de sistemas acontece nas interfaces — entre subsistemas, organizações ou pessoas. Um **documento de controle de interface** (ICD) especifica dados, temporização, protocolos, energia, conexões físicas e responsabilidades de cada lado. A **gestão de configuração** identifica cada item (hardware, versões de firmware, parâmetros, documentos), controla as mudanças por meio de revisão e mantém registros, para que o sistema como construído seja conhecido. Em segurança, uma configuração desconhecida é uma superfície de ataque desconhecida. Os três documentos de controle de interface do TMRP cobrem RTU para gateway, gateway para SCADA e SCADA para DMZ. Cada um nomeia um dono de cada lado.

### 16.4 A segurança como disciplina da engenharia de sistemas

O [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) enquadra a engenharia de segurança de sistemas como atividades de segurança embutidas nos processos técnicos da engenharia de sistemas: necessidades de proteção das partes interessadas, requisitos de segurança, projeto arquitetural para a segurança, verificação das afirmações de segurança, e operação e descarte seguros. Seu volume companheiro, o [SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1), trata da ciber-resiliência: antecipar, resistir, recuperar-se e adaptar-se a condições adversas, incluindo ataques. O TMRP segue essa abordagem: N2 é uma necessidade de proteção decomposta em R1 e R2, e cada um tem uma verificação planejada.

### 16.5 Exemplo resolvido: o TMRP como sistema (sintético)

As necessidades de nível mais alto do TMRP: N1 manter o hospital abastecido (interrupção ≤ 4 h em cenários plausíveis); N2 detectar e conter o uso indevido do controle remoto; N3 recuperar a operação remota em até um dia útil; N4 manter a visibilidade do operador durante faltas de energia da rede. Elas se decompõem nos requisitos R1–R9 apresentados até aqui (telemetria autenticada, rejeição de repetições, limites de setpoint, modo manual local, autonomia de 24 h do armário, restauração em até 8 h, alarmes em até 60 s, integridade dos logs, alarme de dosagem independente). A equipe escreve documentos de controle de interface para RTU–gateway, gateway–SCADA e SCADA–DMZ, e coloca todas as versões de firmware e os arquivos de configuração das RTUs sob controle de mudanças. Cada requisito agora tem uma necessidade-pai e um método de verificação planejado.

### 16.6 Atividade prática

Desenhe uma matriz de rastreabilidade N1–N4 × R1–R9 e marque o(s) pai(s) de cada requisito. Identifique qualquer necessidade com cobertura fraca. Use uma grade simples com as necessidades nas colunas e os requisitos nas linhas, e marque o pai ou os pais de cada requisito. Alguns requisitos servem a mais de uma necessidade: R5 apoia a visibilidade durante faltas de energia da rede, e R1 apoia tanto a contenção quanto o abastecimento do hospital. Quando terminar, conte os requisitos sob cada necessidade. Uma necessidade sustentada por um único requisito merece um segundo olhar, porque um único teste reprovado a deixaria sem sustentação no dossiê.

### 16.7 Erros comuns e limites

- Requisitos escritos depois do projeto para justificá-lo.
- Interfaces sem dono.
- Configuração conhecida apenas pelo engenheiro de comissionamento.
- Requisitos de segurança num documento separado, nunca rastreados nem verificados.
- Tratar o modelo em V como uma desculpa em cascata para adiar os testes.

No TMRP, cada um desses erros tem uma contramedida: os requisitos são rastreados até N1–N4, cada interface tem um dono, e o firmware e a configuração das RTUs estão sob controle de mudanças. A verificação é planejada para cada requisito antes do início do projeto, então o V não é usado como motivo para adiar os testes.

### Exercícios — capítulo 16

**EX031 — Rastreie e encontre lacunas.** *Objetivo:* construir e analisar uma matriz de rastreabilidade. *Entradas:* §16.5. *Passos:* atribua cada um de R1–R9 à(s) sua(s) necessidade(s)-pai; identifique qual necessidade depende do menor número de requisitos e proponha um requisito adicional. *Evidência esperada:* matriz e proposta. *Rubrica:* 3 = mapeamento defensável, necessidade mais fraca identificada, com um novo requisito verificável; 2 = erros de mapeamento; 1 = sem proposta; 0 = nada.

**EX032 — Controle de interface.** *Objetivo:* especificar uma interface por completo. *Entradas:* a interface gateway–SCADA. *Passos:* liste pelo menos oito atributos da interface, com valores de exemplo (itens de dados, codificação, taxa, latência, autenticação, tratamento de erros, fonte de tempo, propriedade, processo de mudança). *Evidência esperada:* tabela. *Rubrica:* 3 = completa e coerente com os laboratórios 8 e 13; 2 = faltam atributos de segurança ou de propriedade; 1 = apenas dados; 0 = nada.

### Síntese do capítulo

A engenharia de sistemas vai das necessidades a sistemas verificados e validados por meio de requisitos rastreáveis, interfaces gerenciadas e configuração controlada. A segurança pertence a esses processos: as necessidades de proteção se tornam requisitos, os requisitos se tornam arquitetura e projeto, e toda afirmação de segurança precisa de evidência de verificação.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 50

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) descrever o controle em malha aberta e em malha fechada, setpoints, erro e limites dos atuadores; (2) explicar o controle proporcional-integral (PI) e a saturação do integrador (wind-up); (3) analisar como dados falsos de sensores — uma injeção de dados falsos — levam um controlador correto a um estado inseguro; e (4) projetar uma detecção baseada em resíduos usando medições físicas independentes e declarar seus pontos cegos. Ele se apoia no Capítulo 6 e prepara os capítulos 27 e 33.

### 17.1 Realimentação

Um controlador em **malha fechada** mede uma variável de processo, compara-a com um setpoint e ajusta um atuador para reduzir o erro. A realimentação torna os sistemas robustos a perturbações e a erros de modelo — e os faz confiar totalmente em seus sensores. O livro [*Feedback Systems*, de Åström e Murray](https://fbswiki.org/wiki/index.php/Main_Page), disponível gratuitamente on-line, é o texto de referência deste capítulo. Em Hollin Hill, o controlador PI ajusta a vazão de entrada da PS3 para manter o nível do reservatório no setpoint. Ele só vê o reservatório pelo transmissor de nível, então o que esse transmissor informar é, para o controlador, a verdade. O restante deste capítulo acompanha a consequência dessa confiança.

### 17.2 Controle PI

Um controlador proporcional define a saída do atuador como $u = K_p e$; ele deixa um erro em regime permanente quando uma perturbação constante precisa ser equilibrada. Acrescentar um termo integral, $u = K_p e + K_i\int e\,dt$, elimina o erro em regime permanente, porque a integral continua crescendo até o erro ser zero. Os atuadores saturam — uma bomba não consegue entregar mais do que sua vazão máxima — e, enquanto saturado, a integral continua crescendo (**wind-up**), causando sobressinal quando o atuador sai da saturação. O anti-wind-up interrompe a integração durante a saturação.

### 17.3 Dados falsos e o controlador crédulo

Se um atacante soma um viés $b$ à medição de nível, o controlador regula o nível *medido* no setpoint, de modo que o nível *real* se estabiliza no setpoint menos $b$. O controlador funciona perfeitamente; o processo, não. Esse é o núcleo dos ataques conscientes do processo: o Stuxnet, como analisado por [Langner (2011)](https://doi.org/10.1109/MSP.2011.67), manipulou as velocidades das centrífugas enquanto reproduzia para os operadores valores de aparência normal. As defesas não podem depender do mesmo fluxo de sensores que o atacante controla. Em Hollin Hill, um transmissor de nível com viés baixaria o nível real enquanto a tela do operador mostrasse o setpoint, então a defesa precisa vir de uma medição independente.

### 17.4 Detecção baseada em resíduos

Um **resíduo** é a diferença entre o que uma medição diz e o que um modelo independente prevê. Para um reservatório, o balanço de massa prevê a variação de nível a partir das vazões de entrada e de saída medidas de forma independente: $\Delta h = (q_{in} - q_{out})\Delta t / A$. Dois detectores: um **resíduo de passo** compara a variação do nível medido com a variação prevista num passo; um **resíduo cumulativo** compara o nível medido com o nível integrado a partir das vazões desde a última calibração confiável. O detector de passo pega um viés abrupto, mas não uma deriva lenta; o detector cumulativo pega a deriva, mas acumula o erro dos medidores, então precisa de recalibração periódica e de um limiar acima da deriva normal dos medidores. Um atacante que também controle os medidores de vazão derrota ambos — a independência dos caminhos de medição é o verdadeiro controle.

### 17.5 Exemplo resolvido: ataque ao nível de Hollin Hill (sintético)

O Laboratório 7 simula o controle PI de Hollin Hill (área em planta de 1.000 m², setpoint de 3,0 m, vazão de saída de 300 m³/h, bomba de entrada de 0–600 m³/h) por 48 h. Um viés em degrau de +1,5 m às 10 h leva o nível real para 1,5 m; os dois detectores alarmam em 10,0 h. Um viés de +0,04 m — pequeno o bastante para parecer erro do sensor — só é pego pelo detector cumulativo. Uma rampa lenta de 0,05 m/h escapa inteiramente do detector de passo; o detector cumulativo alarma em 10,6 h, quando o viés é de cerca de 0,03 m. Sem detecção, a rampa deixa o nível real em 1,1 m após 48 h.

### 17.6 Atividade prática: Laboratório 7

```python
# Lab 7 - PI level control under sensor-bias attacks, and two residual detectors (synthetic, offline)
def run(attack=None, hours=48, dt=0.1):
    A = 1000.0                         # m2 reservoir plan area: level h (m), volume A*h (m3)
    h, integ, sp, kp, ki = 3.0, 7.5, 3.0, 400.0, 40.0   # integ preloaded so u = 300 at start
    est = h                            # mass-balance estimate from independently metered flows
    prev_meas, step_t, cum_t, hmin = h, None, None, h
    for k in range(int(hours / dt)):
        t = k * dt
        b = attack(t) if attack else 0.0
        meas = h + b
        err = sp - meas
        u = kp * err + ki * integ
        q_in = min(max(u, 0.0), 600.0)              # pump limits 0..600 m3/h
        if 0.0 < u < 600.0: integ += err * dt         # anti-windup
        q_out = 300.0
        if k > 0 and step_t is None and abs((meas - prev_meas) - (est - est_prev)) > 0.05: step_t = round(t, 1)
        if cum_t is None and abs(meas - est) > 0.03: cum_t = round(t, 1)
        prev_meas, est_prev = meas, est
        h += (q_in - q_out) / A * dt; est += (q_in - q_out) / A * dt
        hmin = min(hmin, h)
    return round(h, 2), round(hmin, 2), step_t, cum_t
print("columns: true final level m, true min level m, step-detector alarm h, cumulative-detector alarm h")
print("no attack        ", run())
print("step bias +1.5 m ", run(lambda t: 1.5 if t >= 10 else 0.0))
print("step bias +0.04 m", run(lambda t: 0.04 if t >= 10 else 0.0))
print("ramp 0.05 m/h    ", run(lambda t: 0.05 * (t - 10) if t >= 10 else 0.0))
```

Saída esperada:

```text
columns: true final level m, true min level m, step-detector alarm h, cumulative-detector alarm h
no attack         (3.0, 3.0, None, None)
step bias +1.5 m  (1.5, 1.4, 10.0, 10.0)
step bias +0.04 m (2.96, 2.95, None, 10.0)
ramp 0.05 m/h     (1.1, 1.1, None, 10.6)
```

Leia as quatro linhas à luz do exemplo resolvido. Sem ataque, o nível fica em três metros e nenhum detector dispara. O viés em degrau grande é pego pelos dois detectores ao mesmo tempo, e o nível real se estabiliza um metro e meio abaixo. O degrau pequeno e a rampa lenta são onde os detectores diferem: só o detector cumulativo os vê, e a rampa, se deixada em paz, arrasta o nível real para cerca de um metro. Lembre-se de que os medidores de vazão do laboratório são perfeitos, então os tempos reais de detecção seriam mais tardios.

### 17.7 Erros comuns e limites

- Igualar "o controlador funcionou" a "o processo está seguro".
- Detecção que usa o mesmo caminho de dados da malha de controle.
- Limiares definidos sem medir o ruído e a deriva normais.
- Ignorar o wind-up e a saturação no raciocínio de segurança operacional.
- Resultados de simulação apresentados como comportamento da planta; o Laboratório 7 é um modelo simplificado, com medidores de vazão perfeitos.

Para Hollin Hill, o EX034 mostra claramente o problema da dependência: o sensor de nível e o medidor de vazão de entrada estão ambos ligados à RTU3, então comprometer uma única RTU derrota os dois lados do resíduo.

### Exercícios — capítulo 17

**EX033 — Compromisso do limiar.** *Objetivo:* ajustar um detector. *Entradas:* Laboratório 7. *Passos:* (1) acrescente ruído gaussiano com desvio-padrão de 0,01 m ao nível medido (semente 17) e conte os falsos alarmes do detector cumulativo no caso sem ataque com os limiares 0,03 e 0,05; (2) informe o tempo de detecção da rampa nos dois limiares; (3) recomende um limiar. *Evidência esperada:* tabela e recomendação. *Rubrica:* 3 = experimento implementado corretamente, compromisso explicado, recomendação ligada ao tempo de resposta; 2 = apenas um limiar; 1 = não executado; 0 = nada.

**EX034 — Argumento de independência.** *Objetivo:* argumentar a independência da detecção. *Entradas:* a arquitetura da LRWA: sensor de nível e medidor de vazão de entrada ambos ligados à RTU3; medidor de vazão de saída na PS4, na RTU4. *Passos:* identifique quais posições do atacante derrotam o detector de resíduos e proponha uma mudança de arquitetura que melhore a independência. *Evidência esperada:* meia página. *Rubrica:* 3 = comprometer a RTU3 derrota nível e vazão de entrada, a mudança propõe um caminho separado (por exemplo, transmissor de nível independente para um registrador separado ou conferência física da régua); 2 = parcial; 1 = genérico; 0 = nada.

### Síntese do capítulo

A realimentação torna os sistemas robustos e crédulos. Um sensor com viés leva um controlador correto a um estado físico incorreto. Detecte com resíduos construídos a partir de física independente, use testes de passo e cumulativos para ataques abruptos e lentos, defina os limiares a partir do ruído medido e lembre-se de que a independência dos caminhos de medição — e não a engenhosidade do algoritmo — é o que derrota um atacante capaz.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 50

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) descrever arquiteturas de referência para a tecnologia operacional, incluindo modelos em camadas e DMZs; (2) aplicar os princípios de confiança zero onde eles cabem na TO e explicar onde não cabem; (3) projetar arquiteturas de acesso remoto, registro em log e monitoramento; e (4) avaliar uma arquitetura pela consequência, e não apenas pela contagem de controles. Ele se apoia nos capítulos 11, 12 e 15 e prepara os capítulos 26 e 27.

### 18.1 Arquiteturas de TO em camadas

As arquiteturas de TO costumam ser descritas em níveis: processo físico (nível 0), sensores e atuadores com controle básico (1), controle supervisório (2), operações da instalação (3), uma zona desmilitarizada e o nível corporativo (4–5). O modelo, que descende da arquitetura de referência de Purdue e aparece no [guia de TO do NIST](https://csrc.nist.gov/pubs/sp/800/82/r3/final), é uma ferramenta para posicionar ativos e condutos, não uma lei. Os sistemas modernos borram os níveis: sensores conectados à nuvem, serviços remotos de fornecedores e dispositivos de campo com enlaces celulares diretos. Na LRWA, os servidores SCADA ficam na zona de controle, as RTUs na zona de campo e a réplica do historiador na DMZ.

### 18.2 A DMZ e a intermediação de dados

A DMZ de TO fica entre as redes de controle e corporativa. Nenhum tráfego direto a atravessa: os sistemas corporativos falam com serviços da DMZ (réplica do historiador, servidor de correções, gateway de acesso remoto), que falam com os sistemas de controle. Um teste útil: se qualquer host corporativo for comprometido, ele consegue enviar um pacote que chegue a um controlador? Se sim, a DMZ é decorativa. Na LRWA, a revisão de fluxos aplicou esse teste e reprovou: um script de relatório corporativo alcançava diretamente uma RTU de campo. Mover esses dados para a réplica do historiador na DMZ é o modo como a LRWA torna sua DMZ real, e não decorativa, e o teste é repetido depois que cada novo conduto é acrescentado.

### 18.3 Confiança zero na TO

A confiança zero, como descrita no [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final), remove a confiança implícita baseada na localização na rede; todo acesso é autenticado, autorizado e avaliado por sessão. Na TO, o princípio é valioso para o acesso humano e de engenharia — identidades nominais, autenticação forte, privilégio sob demanda (just-in-time), gravação de sessões — e para dispositivos novos que o suportem. Ele se encaixa mal onde controladores legados não conseguem autenticar de forma alguma e onde as malhas de controle não toleram um ponto de decisão de política no seu caminho. A resposta de engenharia é aplicar a confiança zero nas fronteiras em que for possível (acesso de engenharia, intermediação de dados, gateways) e usar segmentação e monitoramento em torno do que não consegue autenticar.

### 18.4 Acesso remoto

O acesso remoto de fornecedores e da equipe é um dos principais caminhos de entrada na TO. Projete-o assim: um gateway de acesso na DMZ; autenticação multifator; contas nominais; acesso aprovado por sessão; conexões a um jump host, nunca diretamente aos controladores; gravação das sessões; e expiração automática. O [incidente na estação de tratamento de água de Oldsmar](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a) foi inicialmente atribuído a acesso remoto não autorizado por meio de software de compartilhamento de área de trabalho; declarações posteriores, relatadas pela [WUSF Public Media (2023)](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021), indicaram que provavelmente foi erro de um funcionário. De um modo ou de outro, o caso ilustra por que o compartilhamento de área de trabalho sem controle nas estações dos operadores é uma fraqueza de arquitetura, e por que os relatos iniciais de incidentes devem ser tomados como provisórios.

### 18.5 Arquitetura de monitoramento

O monitoramento de segurança de rede na TO costuma ser passivo: cópias do tráfego, vindas de portas espelhadas dos switches ou de taps, alimentam sensores que entendem protocolos industriais e estabelecem uma linha de base do comportamento normal. Os logs de servidores, firewalls e gateways vão para um coletor na DMZ ou numa zona de segurança dedicada. O monitoramento não pode criar novos caminhos para dentro do controle: os sensores recebem apenas cópias, e as interfaces de gerenciamento ficam numa rede separada. Na LRWA, os taps passivos ficam no switch da zona de controle e no head-end da LTE, e suas interfaces de gerenciamento são mantidas fora da rede monitorada.

### 18.6 Exemplo resolvido: a arquitetura-alvo do TMRP (sintético)

O alvo da LRWA: corporativo — firewall — DMZ (réplica do historiador, gateway de acesso remoto com MFA, preparação de correções, coletor de logs) — firewall — zona de controle (par SCADA, jump host de engenharia) — conduto de campo sobre LTE privada com autenticação na camada de aplicação (gateways para as RTUs legadas) — RTUs e painéis de controle locais com modo manual. Os taps de monitoramento passivo ficam no switch da zona de controle e no head-end da LTE. A arquitetura é avaliada pelas consequências: comandos forjados exigem comprometer uma chave de gateway de campo ou os servidores SCADA; o comprometimento do corporativo rende os dados da réplica do historiador, mas nenhum caminho de pacotes até os dispositivos de campo; a perda da LTE deixa as instalações em modo automático local ou manual, com baterias de telemetria de 24 h.

### 18.7 Atividade prática

Desenhe a arquitetura-alvo em texto ou num diagrama simples e anote em cada conduto as entradas da lista de permissões do Laboratório 5. Depois aplique o teste da DMZ da §18.2. Marque cada conduto com seu sentido e seu protocolo, e mostre onde ficam os taps passivos. Para cada entrada da lista de permissões, pergunte qual zona inicia a conexão e se o teste da DMZ ainda passa caso essa zona seja comprometida. Depois acrescente o caminho de engenharia pelo jump host e verifique que nenhuma regra deixa uma estação de engenharia alcançar diretamente uma RTU de campo, que foi uma das três violações de fluxo da LRWA. Um diagrama que esconde o sentido não consegue mostrar se a DMZ realmente funciona.

### 18.8 Erros comuns e limites

- DMZs com regras diretas "temporárias".
- Confiança zero alegada para sistemas que não conseguem autenticar.
- Acesso remoto que contorna o gateway (modems de fornecedores, ferramentas de compartilhamento de área de trabalho).
- Sensores de monitoramento com interfaces de gerenciamento na rede monitorada.
- Arquiteturas julgadas pelo número de controles, e não pelas consequências evitadas.

Na LRWA, o terceiro e o primeiro erros são os mais prováveis: um fornecedor querendo acesso rápido à RTU-B para diagnósticos, e uma regra direta temporária acrescentada durante uma interrupção. A arquitetura-alvo responde aos dois com o gateway de acesso da DMZ e o controle de mudanças em cada conduto.

### Exercícios — capítulo 18

**EX035 — Teste da DMZ.** *Objetivo:* testar um projeto de DMZ. *Entradas:* uma regra proposta que permite ao servidor de ERP corporativo escrever o estado das ordens de serviço diretamente no banco de dados do SCADA por TCP/1433. *Passos:* aplique o teste da DMZ; proponha um projeto alternativo que atenda à necessidade do negócio. *Evidência esperada:* análise e projeto. *Rubrica:* 3 = regra rejeitada com o motivo, a alternativa intermedeia os dados pela DMZ, com o lado do controle buscando os dados ou com uma exportação unidirecional; 2 = a alternativa ainda é de entrada; 1 = aceita a regra; 0 = nada.

**EX036 — Arquitetura de acesso remoto.** *Objetivo:* projetar o acesso de fornecedores. *Entradas:* o fornecedor da RTU-B precisa de acesso trimestral para diagnósticos. *Passos:* especifique o caminho de acesso, a autenticação, a aprovação, o monitoramento e a expiração; liste as evidências que mostrariam que o projeto funciona. *Evidência esperada:* especificação e lista de evidências. *Rubrica:* 3 = gateway, MFA, aprovação por sessão, jump host, gravação, expiração, e evidências (logs, teste do caminho direto negado); 2 = sem evidências; 1 = VPN direta para o controle; 0 = nada.

### Síntese do capítulo

Use modelos em camadas para posicionar ativos e condutos, torne a DMZ real não permitindo nenhuma travessia direta, aplique a confiança zero onde os sistemas conseguem autenticar e a segmentação onde não conseguem, faça todo acesso remoto passar por um gateway controlado, monitore de forma passiva sem criar caminhos e julgue a arquitetura pelas consequências que ela torna difíceis de causar.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 50

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) explicar a criptografia simétrica e a de chave pública, hashes e MACs, e escolher entre eles; (2) projetar a autenticação de mensagens com proteção contra repetição para uma telemetria com recursos limitados; (3) planejar a gestão de chaves — geração, distribuição, armazenamento, rotação, revogação — para uma frota de campo; e (4) projetar identidade e autenticação para pessoas e dispositivos. Ele se apoia nos capítulos 4, 13 e 18 e prepara os capítulos 27–28.

### 19.1 Primitivas

- As **funções de hash** (SHA-256, [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)) mapeiam dados para um resumo de tamanho fixo; encontrar colisões ou pré-imagens deve ser inviável. Um hash sozinho não autentica nada.
- A **cifração simétrica** (AES, [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)) usa uma única chave compartilhada para a confidencialidade.
- Os **códigos de autenticação de mensagem** (HMAC, [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final); [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104)) permitem a quem detém uma chave compartilhada verificar que uma mensagem não foi alterada e veio de alguém que detém a chave.
- A **criptografia de chave pública**, introduzida por [Diffie and Hellman (1976)](https://doi.org/10.1109/TIT.1976.1055638) e realizada para assinaturas por [Rivest, Shamir and Adleman (1978)](https://doi.org/10.1145/359340.359342), usa pares de chaves: qualquer um pode verificar uma assinatura com a chave pública; só quem detém a chave privada pode assinar.
- A **cifração autenticada** (por exemplo, AES-GCM) fornece confidencialidade e integridade juntas.

Nunca projete suas próprias primitivas ou protocolos quando um padrão servir; o TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)) é o padrão para enlaces IP que conseguem executá-lo.

### 19.2 Autenticando a telemetria

Para um enlace com recursos limitados, um projeto comum é: carga útil mais um contador monotônico (ou um carimbo de tempo), um MAC sobre ambos, o receptor verifica o MAC em tempo constante e depois verifica se o contador é maior do que o último valor aceito. O contador derrota a repetição; um carimbo de tempo com uma janela de atualidade derrota ataques de atraso, mas exige relógios sincronizados. Truncar o HMAC-SHA256 para 128 bits é comum por causa da largura de banda, com uma margem contra falsificação correspondentemente reduzida, mas ainda muito grande. Persista o último contador ou troque as chaves no reinício, ou um reinício reabre a repetição (EX018).

### 19.3 Gestão de chaves

As chaves são onde a criptografia encontra as operações. Decida: quem gera as chaves e onde (de preferência em hardware, nunca à mão); como elas chegam aos dispositivos (provisionamento de fábrica, cadastro seguro); onde ficam armazenadas (elementos seguros, não arquivos de configuração); como são trocadas (de forma agendada e após suspeita de comprometimento); como são revogadas; e quem pode acessá-las. Uma chave por par de dispositivos limita o raio de impacto: comprometer uma RTU não deve permitir que um atacante se passe por outra. Uma única chave para toda a frota é uma causa comum com $\beta \approx 1$ (Capítulo 7).

### 19.4 Identidade para pessoas e dispositivos

As pessoas precisam de contas nominais, autenticação forte (multifator resistente a phishing onde for possível — veja o [NIST SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)), papéis mapeados a tarefas e remoção imediata quando saem. Os dispositivos também precisam de identidades — certificados ou chaves provisionadas — para que um gateway saiba com qual RTU está falando. Credenciais compartilhadas ou padrão são a falha de identidade mais comum na TO. No TMRP, os operadores usam contas nominais com autenticação forte nos servidores SCADA, e cada RTU tem sua própria chave, de modo que o gateway sabe qual estação enviou cada mensagem.

### 19.5 Exemplo resolvido: o formato de mensagem do TMRP (sintético)

O ADR-007 escolheu HMAC com contadores. O quadro do Laboratório 8 leva um contador de 8 bytes, um ID de estação de 2 bytes, um nível de 2 bytes e um HMAC-SHA256 truncado de 16 bytes: 28 bytes, dos quais 22 são sobrecarga em relação a uma carga útil de 6 bytes sem autenticação. As chaves por estação são geradas no elemento seguro do gateway no cadastro e armazenadas no repositório de chaves da RTU; o lado do SCADA as mantém num módulo de segurança de hardware (HSM). As chaves são trocadas anualmente e imediatamente diante de suspeita de comprometimento; o contador é persistido em memória não volátil a cada incremento de 1.000, com um salto à frente no reinício, de modo que a repetição de mensagens antigas continua impossível.

### 19.6 Atividade prática: Laboratório 8

```python
# Lab 8 - authenticated telemetry with a counter: tamper and replay are rejected (synthetic key, offline)
import hmac, hashlib, struct
KEY = bytes.fromhex("00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff")  # demo key only
def seal(ctr, station, level_cm):
    body = struct.pack(">QHH", ctr, station, level_cm)
    return body + hmac.new(KEY, body, hashlib.sha256).digest()[:16]
class Receiver:
    def __init__(self): self.last = {}
    def accept(self, msg):
        body, tag = msg[:12], msg[12:]
        if not hmac.compare_digest(tag, hmac.new(KEY, body, hashlib.sha256).digest()[:16]): return "reject: tag"
        ctr, st, lvl = struct.unpack(">QHH", body)
        if ctr <= self.last.get(st, -1): return "reject: replay"
        self.last[st] = ctr; return f"ok st={st} ctr={ctr} level={lvl}cm"
r = Receiver(); m1, m2 = seal(1, 3, 312), seal(2, 3, 309)
forged = m2[:10] + struct.pack(">H", 150) + m2[12:]
for name, m in [("m1", m1), ("m2", m2), ("replay m1", m1), ("forged", forged)]: print(f"{name:10}", r.accept(m))
print("frame bytes:", len(m1), "overhead vs 6-byte payload:", len(m1) - 6)
```

Saída esperada:

```text
m1         ok st=3 ctr=1 level=312cm
m2         ok st=3 ctr=2 level=309cm
replay m1  reject: replay
forged     reject: tag
frame bytes: 28 overhead vs 6-byte payload: 22
```

A chave do laboratório é um valor de demonstração publicado; chaves reais nunca devem aparecer no código-fonte.

As duas primeiras mensagens da estação três são aceitas, com contadores crescentes. A repetição da primeira mensagem é recusada porque seu contador não é maior do que o último valor aceito, e a mensagem forjada, com o nível alterado de 309 para 150 centímetros, reprova na verificação da etiqueta. A última linha confirma o tamanho de quadro usado no ADR-007: vinte e oito bytes, vinte e dois deles de sobrecarga. O laboratório mantém o estado apenas na memória, e é por isso que o EX018 pergunta o que acontece após um reinício.

### 19.7 Erros comuns e limites

- Hashes ou CRCs usados como se fossem MACs.
- Comparação de etiquetas que não é em tempo constante.
- Proteção contra repetição perdida no reinício.
- Chaves compartilhadas por toda a frota; chaves em arquivos de configuração ou no código-fonte.
- Senhas padrão e contas compartilhadas.
- Escolhas criptográficas sem um plano para a vida útil do sistema (agilidade de algoritmos).

O projeto do TMRP responde a cada item: as etiquetas são comparadas em tempo constante, os contadores persistem entre reinícios, as chaves são por estação, em hardware seguro, e o formato de mensagem ganha um identificador de suíte para futuras mudanças de algoritmo. Cada escolha tem um teste.

### Exercícios — capítulo 19

**EX037 — Persistência do contador.** *Objetivo:* projetar uma proteção contra repetição segura diante de reinícios. *Entradas:* §19.5 (persistir a cada 1.000 incrementos). *Passos:* explique por que a RTU precisa saltar à frente no reinício e em quanto, no mínimo; diga o que o receptor precisa persistir. *Evidência esperada:* explicação. *Rubrica:* 3 = salto ≥ 1.000 além do último valor persistido, para que nenhum contador seja reutilizado, receptor persiste o último aceito por estação ou troca as chaves; 2 = apenas um dos lados; 1 = vago; 0 = nada.

**EX038 — Raio de impacto.** *Objetivo:* comparar projetos de chaves. *Entradas:* 42 estações de campo; opção A, uma chave para a frota; opção B, uma chave por estação. *Passos:* compare a consequência de extrair uma chave de uma RTU roubada, o esforço de rotação após esse roubo e o armazenamento necessário no SCADA. *Evidência esperada:* tabela e recomendação. *Rubrica:* 3 = A permite ao ladrão forjar qualquer estação e força a rotação em toda a frota; B confina a falsificação a uma estação, com uma rotação; armazenamento trivial; recomendação B; 2 = falta uma dimensão; 1 = recomendação sem raciocínio; 0 = nada.

### Síntese do capítulo

Escolha primitivas padrão para a propriedade de que você precisa: hashes para impressões digitais, MACs ou assinaturas para autenticidade, cifração autenticada para confidencialidade com integridade. Acrescente atualidade para derrotar a repetição e mantenha-a entre reinícios. A gestão de chaves é o sistema de verdade: chaves por dispositivo em hardware, rotação e revogação. Dê a pessoas e dispositivos identidades distintas e fortemente autenticadas.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 50

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Infraestrutura crítica e segurança setorial: contexto de engenharia

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) descrever como a infraestrutura crítica é definida e organizada em setores, e o panorama regulatório dentro do qual os engenheiros trabalham; (2) caracterizar os setores por seus processos físicos, unidades de consequência e tecnologia; (3) descrever as interdependências entre setores; e (4) aprender com incidentes documentados no nível que suas fontes públicas sustentam. É a ponte entre os fundamentos (capítulos 1–19) e os capítulos da área (21–50).

### 20.1 O que torna uma infraestrutura "crítica"

Os governos designam como críticos os ativos, sistemas e redes cuja incapacitação prejudicaria gravemente a segurança, a economia, a saúde pública ou a segurança das pessoas. Os Estados Unidos identificam dezesseis [setores de infraestrutura crítica](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors) e, mais recentemente, um conjunto de [National Critical Functions](https://www.cisa.gov/national-critical-functions-set) que atravessam as organizações. A [Diretiva NIS2 (2022/2555)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) da União Europeia estabelece obrigações de cibersegurança para entidades essenciais e importantes, e a [Diretiva CER (2022/2557)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) trata da resiliência das entidades críticas de forma mais ampla. As regras setoriais acrescentam detalhes: as [normas NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) para os sistemas elétricos de grande porte da América do Norte, os [requisitos de avaliação de riscos do America's Water Infrastructure Act de 2018](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans) para os sistemas comunitários de água dos EUA, o [DORA (2022/2554)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) para as finanças da UE e as [HHS Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). Essas regras mudam; cite a versão e a data e verifique de novo.

### 20.2 Setores como sistemas de engenharia

Cada setor tem um processo físico ou de serviço, uma **unidade de consequência** e uma tecnologia característica.

| Setor | Processo | Unidade de consequência | Tecnologia típica |
|---|---|---|---|
| Água | Tratar e distribuir água | Pessoas sem água segura × horas | PLCs/RTUs, SCADA, dosagem, telemetria |
| Eletricidade | Gerar, transmitir, distribuir | MW ou consumidores interrompidos × horas | Relés de proteção, EMS/DMS, automação de subestações |
| Saúde | Diagnosticar e tratar | Atendimento atrasado, desvios de pacientes, danos | Prontuário eletrônico, dispositivos médicos, sistemas prediais |
| Transporte | Mover pessoas e mercadorias | Viagens interrompidas, incidentes de segurança | Sinalização, controle de tráfego, bilhetagem |
| Finanças | Compensar e liquidar | Transações falhas ou atrasadas | Sistemas de pagamento, infraestruturas do mercado financeiro |
| Comunicações | Transportar voz e dados | Assinantes afetados × horas | Redes de núcleo, acesso por rádio, sincronismo |

A tabela é uma simplificação para orientação de engenharia; cada linha é uma carreira.

### 20.3 Interdependência

[Rinaldi, Peerenboom and Kelly (2001)](https://doi.org/10.1109/37.969131) classificam as interdependências como físicas, cibernéticas, geográficas e lógicas. A água precisa de eletricidade para o bombeamento; a recomposição da eletricidade precisa de comunicações; os hospitais precisam de água, energia e comunicações; quase tudo precisa de hora precisa. A interdependência transforma falhas locais em regionais e fornecedores compartilhados em causas comuns. A atualização defeituosa da CrowdStrike, em julho de 2024, que a Microsoft estimou ter afetado cerca de 8,5 milhões de dispositivos Windows ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)), não foi um ataque, mas interrompeu de uma só vez companhias aéreas, hospitais e outros serviços por meio de uma dependência de software compartilhada.

### 20.4 Aprender com incidentes documentados

Os relatórios públicos de incidentes são valiosos e parciais. Use-os no nível de suas fontes. O [incidente da Colonial Pipeline](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years), em 2021, envolveu ransomware na TI de negócios; a empresa paralisou as operações do oleoduto por precaução — um lembrete de que a dependência das operações em relação a sistemas de TI (faturamento, programação) pode interromper o serviço físico sem nenhum comprometimento da TO. O [ataque de 2015 à rede elétrica ucraniana](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01) usou acesso remoto para operar disjuntores e danificou as capacidades de recuperação. O surto do [WannaCry em 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) interrompeu serviços do NHS na Inglaterra. Cada um tem detalhes documentados e questões em aberto; onde os relatos iniciais foram revistos, como em Oldsmar, cite ambos.

### 20.5 Exemplo resolvido: situando a LRWA no contexto (sintético)

A LRWA é uma concessionária de água que tem um hospital entre seus clientes críticos. Sua unidade de consequência são pessoas-hora sem água segura, ponderadas para usuários vulneráveis; a reservação própria do St Brenna's dá cerca de quatro horas de folga. Suas interdependências: eletricidade (bombeamento, tratamento), comunicações (telemetria LTE), fornecimento de produtos químicos (cloro) e tempo (correlação de logs). Supõe-se que seu contexto regulatório inclua um dever de avaliação de riscos e resiliência semelhante ao do AWIA. O escopo do TMRP é definido por esses elementos: o programa não é "proteger o SCADA", e sim "manter a água segura chegando às pessoas sob condições adversas plausíveis, incluindo ataques".

### 20.6 Atividade prática

Escolha um setor que não seja o de água. Apenas a partir de fontes públicas, construa a linha dele na §20.2 com mais detalhes: três unidades de consequência, três tecnologias típicas, duas regulações principais com versão e data, e um incidente documentado com sua fonte. Mantenha o perfil no nível de suas fontes. Para cada regulação, dê a versão, a data em que você a consultou e as entidades que ela abrange. Para o incidente, diga apenas o que o relatório citado diz e anote qualquer revisão posterior, como no caso de Oldsmar. Depois compare a unidade de consequência do seu setor com as pessoas-hora sem água segura da LRWA e anote uma interdependência que seu setor compartilha com a água, como eletricidade, comunicações ou tempo.

### 20.7 Erros comuns e limites

- Tratar a "infraestrutura crítica" como uma categoria de tecnologia, e não como uma categoria de consequência.
- Regulações citadas sem versão ou data.
- Narrativas de incidentes repetidas além do que as fontes sustentam.
- Ignorar as dependências de TI das operações físicas.
- Pensar num único setor num mundo interdependente.

O próprio contexto da LRWA mostra por que isso importa. Sua condição de crítica vem do St Brenna's e de seus outros clientes, não da tecnologia que ela opera. Suas operações dependem de eletricidade, LTE, fornecimento de cloro e hora precisa, então analisar a água isoladamente deixaria passar a dependência oculta do alimentador encontrada antes. Qualquer dever regulatório em que ela se apoie precisa ser citado com versão e data.

### Exercícios — capítulo 20

**EX039 — Perfil setorial.** *Objetivo:* traçar o perfil de um setor a partir de fontes públicas. *Entradas:* §20.6. *Passos:* produza o perfil com citações. *Evidência esperada:* uma página. *Rubrica:* 3 = exato, citado, unidades de consequência mensuráveis, incidente descrito dentro de suas fontes; 2 = uma afirmação sem citação; 1 = genérico; 0 = nada.

**EX040 — Dependência compartilhada.** *Objetivo:* raciocinar sobre causas comuns entre setores. *Entradas:* a interrupção da CrowdStrike de julho de 2024, como descrita pela Microsoft. *Passos:* explique em 200 palavras por que uma atualização de software não maliciosa produziu uma interrupção em vários setores, qual propriedade de engenharia ela revela e uma prática de projeto que limita eventos assim. *Evidência esperada:* texto. *Rubrica:* 3 = dependência compartilhada/causa comum, componente privilegiado com atualização automática, implantação em etapas ou diversidade como prática, afirmações dentro das fontes; 2 = prática genérica; 1 = chama de ataque; 0 = nada.

### Síntese do capítulo

A infraestrutura crítica é definida pela consequência. Os setores diferem em processo, unidades de consequência e tecnologia, mas compartilham a interdependência de energia, comunicações, tempo e fornecedores comuns. Trabalhe dentro das regulações por versão e data, aprenda com os incidentes apenas até onde suas fontes vão e defina todo programa de segurança pelo serviço e pelas pessoas que ele protege.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 50

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Infraestrutura crítica e segurança setorial: requisitos

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) levantar requisitos de segurança e de resiliência a partir de consequências, partes interessadas, regulações e informações sobre ameaças; (2) escrever requisitos baseados em desempenho para a operação degradada, a recuperação e a segurança operacional, e não apenas para a proteção; (3) derivar requisitos de componentes a partir dos requisitos de sistema usando níveis de segurança; e (4) negociar explicitamente os conflitos entre requisitos. Ele aplica os capítulos 5 e 16 ao setor e prepara o Capítulo 22.

### 21.1 Fontes de requisitos

Os requisitos de segurança de infraestrutura vêm de cinco fontes, e um bom conjunto é rastreável a todas elas: **consequências** (o que nunca pode acontecer, e o que precisa ser restabelecido e com que rapidez); **partes interessadas** (operadores, clientes como hospitais, serviços de emergência, reguladores); **regulações e normas** (por exemplo, as avaliações de riscos do AWIA, o NERC CIP, as medidas de gestão de riscos da NIS2); **informações sobre ameaças** (capacidades de adversários documentadas em fontes como o [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) e os avisos da CISA); e **restrições** (equipamentos legados, orçamento, equipe, certificação de segurança operacional).

### 21.2 Requisitos para a operação degradada

Um sistema que está ou "seguro" ou "comprometido" está mal especificado. Escreva requisitos para os estados intermediários: *Durante a perda da rede de telemetria, cada estação de bombeamento deverá continuar em controle automático local, dentro de seus limites configurados, por pelo menos 72 h.* *Durante a suspeita de comprometimento dos servidores SCADA, os operadores deverão conseguir operar a PS3 e a PS4 em modo manual local, com procedimentos documentados e equipe, em até 1 h após a decisão.* *Após um incidente, a operação remota deverá ser restabelecida em até 8 h após a decisão de restabelecer, a partir de backups off-line verificados.* São esses os requisitos que mantêm as pessoas abastecidas.

### 21.3 Níveis de segurança e requisitos de componentes

A IEC 62443-3-3 e a IEC 62443-4-2 expressam requisitos de sistema e de componentes em relação a **níveis de segurança** (SL 1–4), que refletem a capacidade do adversário a que se deve resistir, desde a violação casual ou acidental até o ataque sofisticado e com muitos recursos ([visão geral da série ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). A avaliação de riscos para o projeto (IEC 62443-3-2, [página do catálogo](https://webstore.iec.ch/en/publication/30727)) divide o sistema em zonas e condutos e atribui um nível-alvo a cada um. Um nível-alvo se torna então requisitos concretos de componentes — por exemplo, autenticação de todos os usuários humanos, ou proteção da integridade das comunicações. O texto da norma não é de acesso livre; cite cláusulas apenas de uma cópia que você tenha obtido legalmente.

### 21.4 Conflitos e negociação

Os requisitos entram em conflito: acesso rápido do operador versus autenticação forte; correções frequentes versus disponibilidade; registro detalhado em log versus armazenamento em instalações remotas; suporte do fornecedor versus isolamento da rede. Não resolva conflitos em silêncio no projeto. Registre cada um, suas opções e a decisão com seu dono — geralmente a pessoa que é dona do risco operacional. O primeiro conflito registrado no TMRP é entre o modo manual local de R4 e a autenticação de R1, resolvido com uma chave seletora, um alarme e um log local. O dono é a área de operações, que assume o risco de um acesso manual mais lento.

### 21.5 Exemplo resolvido: conjunto de requisitos v1.0 do TMRP (sintético)

| ID | Requisito | Fonte | Verificação |
|---|---|---|---|
| R1 | A telemetria e os comandos entre o campo e o SCADA deverão levar um MAC sobre o conteúdo e o contador; verificações reprovadas deverão ser rejeitadas e alarmadas. | Consequência (comandos forjados), ADR-007 | Teste (T1, T2) |
| R2 | Mensagens repetidas deverão ser rejeitadas, inclusive após o reinício de qualquer das pontas. | Ameaça (repetição) | Teste (T2) |
| R3 | Os controladores deverão rejeitar setpoints fora dos limites físicos configurados ou que excedam o passo configurado, incluindo valores não finitos. | Consequência (operação insegura) | Teste (T3) |
| R4 | Cada estação deverá suportar a operação manual local independente do SCADA e da rede. | Operação degradada | Demonstração |
| R5 | A telemetria de campo deverá operar ≥ 24 h com bateria na capacidade de fim de vida útil. | Parte interessada (visibilidade) | Análise + teste (T4) |
| R6 | A operação remota deverá poder ser restabelecida em até 8 h a partir de backups off-line. | Recuperação | Ensaio (T7, Capítulo 47) |
| R7 | Os alarmes prioritários deverão chegar às telas dos operadores em até 60 s para 99% dos eventos. | Operações | Teste (T5) |
| R8 | Os logs de segurança deverão ter a integridade protegida com âncoras fora da zona de controle. | Investigação | Teste (T6) |
| R9 | A perda da dosagem de cloro deverá gerar alarme em até 15 min por um caminho independente do controlador de dosagem. | Consequência (água insegura) | Teste |

Conflito registrado: o modo manual local de R4 cria um caminho que contorna a autenticação de R1. Resolução: o modo manual exige uma chave seletora física no painel, é alarmado no SCADA e é registrado localmente.

### 21.6 Atividade prática

Escolha um estado degradado ainda não coberto (por exemplo, a perda do fornecedor de cloro por 7 dias) e escreva um requisito, sua fonte e o método de verificação. Escreva o requisito na mesma forma da tabela do TMRP: um identificador, uma única afirmação verificável, sua fonte e um método de verificação. Uma perda de sete dias no fornecimento de cloro, por exemplo, poderia levar a um estoque mínimo de produto químico na instalação, com uma inspeção, e a um procedimento para um fornecedor alternativo, testado por exercício. Verifique se seu requisito não entra em conflito com um existente e, se entrar, registre o conflito e quem deve decidi-lo.

### 21.7 Erros comuns e limites

- Requisitos apenas para a proteção, nenhum para a degradação e a recuperação.
- Níveis de segurança atribuídos sem uma avaliação de riscos documentada.
- Citar cláusulas de normas sem acesso ao texto.
- Conflitos resolvidos em silêncio por quem escreve o projeto.
- Requisitos que não podem ser verificados com os meios do programa.

O conjunto do TMRP evita o primeiro erro ao incluir R4, R5 e R6 para a operação degradada e a recuperação, e evita o quarto ao registrar abertamente o conflito do modo manual local. Todo requisito do conjunto pode ser verificado com a bancada, o ensaio ou a demonstração do próprio programa.

### Exercícios — capítulo 21

**EX041 — Requisitos de estado degradado.** *Objetivo:* especificar o comportamento sob estresse. *Entradas:* LRWA, cenário "servidores SCADA cifrados por ransomware". *Passos:* escreva três requisitos cobrindo a continuidade do serviço, a detecção/contenção e a restauração, cada um com fonte e verificação. *Evidência esperada:* tabela. *Rubrica:* 3 = mensuráveis, cobrem as três fases, verificação realista; 2 = falta uma fase; 1 = apenas proteção; 0 = nada.

**EX042 — Registro de conflito.** *Objetivo:* documentar um conflito. *Entradas:* os operadores querem que a IHM fique conectada o turno inteiro; um novo requisito exige nova autenticação após 15 min de inatividade. *Passos:* escreva um registro de conflito com opções, resolução recomendada e dono. *Evidência esperada:* registro. *Rubrica:* 3 = as opções incluem controles compensatórios (controle de acesso físico à sala de controle, bloqueio apenas de visualização com nova autenticação rápida para ações de controle), dono nomeado pelo papel; 2 = sem dono; 1 = escolhe um lado sem opções; 0 = nada.

### Síntese do capítulo

Derive os requisitos das consequências, das partes interessadas, das regulações, das ameaças e das restrições. Especifique a operação degradada e a recuperação com o mesmo cuidado que a proteção. Traduza os níveis de segurança-alvo em requisitos concretos de componentes por meio de uma avaliação de riscos documentada e registre cada conflito com opções, decisão e dono.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue estudando — capítulo 21 de 50

[← Capítulo 20](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Infraestrutura crítica e segurança setorial: modelos de sistema e de dados

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) construir um inventário de ativos e um modelo de sistema que sustentem a análise de segurança; (2) modelar dependências funcionais, fluxos de dados e fronteiras de confiança; (3) representar estados degradados, e não apenas ligado/desligado; e (4) manter o modelo atualizado e protegido como informação sensível. Ele se apoia nos capítulos 2, 13 e 21 e prepara o Capítulo 23 (análise de ameaças e de falhas).

### 22.1 O inventário primeiro

Você não consegue proteger o que não conhece. Um inventário de ativos de TO registra, para cada dispositivo: identidade, localização, função, zona, endereços de rede, versões de hardware e de firmware, relações de comunicação, dono, criticidade e situação do suporte. Construa-o a partir de várias fontes e concilie-as: documentos de projeto, monitoramento passivo da rede, exportações de configuração e vistorias em campo. Cada fonte deixa coisas de fora — os documentos derivam, o monitoramento passivo não vê dispositivos silenciosos, as vistorias não veem os virtuais. Na LRWA, o inventário cobre as 42 estações de campo, o par SCADA e os gateways, construído a partir de documentos de projeto, do monitoramento passivo no switch de controle e no head-end da LTE, e de visitas às instalações.

### 22.2 Três visões de um sistema

- **Visão funcional:** o que o sistema faz — funções como "manter o nível do reservatório", "desinfetar", "dar visibilidade ao operador" — e quais funções dependem de quais (o grafo do Laboratório 2).
- **Visão física/de rede:** onde estão os ativos e como se conectam — zonas, condutos, enlaces.
- **Visão de fluxo de dados:** quais dados vão para onde, em que sentido, com que proteção, atravessando quais **fronteiras de confiança**. Os diagramas de fluxo de dados com fronteiras de confiança são a entrada da modelagem de ameaças (Capítulo 23).

Mantenha as visões ligadas: toda função mapeia para os ativos que a implementam; todo fluxo mapeia para um conduto.

### 22.3 Estados degradados

Grafos de ligado/desligado são úteis (Capítulo 2), mas insuficientes. Uma estação de bombeamento pode estar em *automático remoto*, *automático local*, *manual local*, *degradada* (uma bomba de duas) ou *fora de serviço*; o reservatório pode estar *normal*, *baixo* ou *abaixo do piso*. Um **modelo de estados** para cada função crítica, com transições causadas por falhas, ataques e ações dos operadores, permite perguntar: a partir da operação normal, que sequência de eventos chega a um estado inaceitável, e qual controle a interrompe? A PS4 é a primeira candidata óbvia na LRWA, porque alimenta o hospital diretamente.

### 22.4 O modelo como informação sensível

Um modelo de sistema preciso é um mapa para um adversário. Armazene-o com controle de acesso, versione-o e publique apenas abstrações. Trate as exportações para fornecedores e consultores sob acordos. Mantenha um **registro de mudanças do modelo** ligado à gestão de configuração (Capítulo 16), para que o modelo continue atualizado; um modelo desatualizado há um ano é um passivo apresentado como ativo. O modelo da LRWA, incluindo o grafo de dependências e as listas de permissões das zonas, é mantido com controle de acesso e versionado a cada mudança de configuração.

### 22.5 Exemplo resolvido: modelo funcional de Hollin Hill (sintético)

A função F1, "abastecer o St Brenna's", é satisfeita se o caminho A (PS4 direto) ou o caminho B (reservatório de Hollin Hill alimentado pela PS3) estiver disponível, *e* o tanque próprio do hospital cobrir a lacuna durante a comutação. O caminho A precisa da PS4, de sua energia (alimentador F2 ou gerador) e de seu controle (o automático local basta). O caminho B precisa do reservatório acima do piso e da PS3 com energia do alimentador F1. A telemetria não é necessária para o abastecimento — o controle automático local mantém as bombas funcionando —, mas é necessária para a *visibilidade* (F3) e para a *intervenção* remota. Essa percepção muda as prioridades: a propriedade de segurança mais importante para F1 é que ninguém consiga comandar remotamente as bombas para um estado inseguro, enquanto a perda da telemetria é um problema de visibilidade com uma folga de 72 h em automático local (R-local). A árvore de falhas do Capítulo 23 formaliza exatamente essa estrutura E/OU.

### 22.6 Atividade prática

Estenda o Laboratório 2 para que cada nó tenha um tipo de dependência E ou OU, e implemente uma função de disponibilidade que avalie se `hospital_supply` funciona dado um conjunto de nós em falha. Teste com as falhas `{grid_f1}`, `{ps4}` e `{ps4, grid_f1}`. Modele o abastecimento do hospital como um OU de seus dois caminhos, com a energia da PS4 como um OU do alimentador F2 e do gerador. Deixe a telemetria fora da função de abastecimento, como argumenta o exemplo resolvido, mas mantenha-a numa função de visibilidade separada, para que sua perda continue aparecendo. Depois confira seus três resultados com o EX043: o abastecimento deve sobreviver à perda do alimentador F1 ou à perda da PS4, e falhar apenas quando ambos forem perdidos.

### 22.7 Erros comuns e limites

- Inventário a partir de uma única fonte.
- Diagramas sem fronteiras de confiança ou sentido dos dados.
- Modelos de ligado/desligado onde os modos degradados decidem os resultados.
- Modelos que nunca são atualizados, ou que são compartilhados livremente.
- Tratar a perda da telemetria e o uso indevido do controle como a mesma consequência.

O modelo de Hollin Hill mostra claramente o último erro: tratar a perda da telemetria como perda do abastecimento mandaria o orçamento do TMRP para a redundância das comunicações, quando a propriedade que de fato protege o hospital é que as bombas não possam ser comandadas remotamente para um estado inseguro.

### Exercícios — capítulo 22

**EX043 — Avaliação E/OU.** *Objetivo:* implementar e usar um modelo de dependências misto. *Entradas:* §22.6. *Passos:* implemente, execute os três testes, relate os resultados. *Evidência esperada:* código e saída. *Rubrica:* 3 = semântica correta; `{grid_f1}` → o abastecimento sobrevive via PS4, se a PS4 funcionar em automático local (sem precisar da LTE); `{ps4}` → sobrevive via reservatório; `{ps4, grid_f1}` → falha; 2 = telemetria exigida indevidamente para o abastecimento; 1 = não executado; 0 = nada.

**EX044 — Modelo de estados.** *Objetivo:* modelar estados degradados. *Entradas:* os modos da PS4 na §22.3. *Passos:* desenhe um modelo de estados com pelo menos cinco estados e os eventos (falha, ataque, ação do operador) entre eles; identifique um caminho de *automático remoto* até *fora de serviço* que um atacante remoto poderia conduzir, e o controle que o interrompe. *Evidência esperada:* tabela de estados e análise. *Rubrica:* 3 = estados e eventos coerentes, caminho de ataque realista, o controle o interrompe (por exemplo, o reset do desarme exige ação local); 2 = apenas estados; 1 = apenas ligado/desligado; 0 = nada.

### Síntese do capítulo

Construa o inventário a partir de várias fontes conciliadas, modele o sistema nas visões funcional, física e de fluxo de dados, com fronteiras de confiança, represente explicitamente os modos degradados e mantenha o modelo atualizado e protegido. Bons modelos separam a visibilidade do controle e mostram qual propriedade realmente protege o serviço.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue estudando — capítulo 22 de 50

[← Capítulo 21](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Infraestrutura crítica e segurança setorial: análise de ameaças e de falhas

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) fazer a modelagem de ameaças sobre diagramas de fluxo de dados com STRIDE e ATT&CK for ICS; (2) construir árvores de falhas e calcular os conjuntos de corte mínimos e as probabilidades do evento de topo; (3) combinar a análise de falhas e a de ataques — árvores de ataque, bow-ties e cenários orientados por consequências; e (4) declarar as suposições e os limites de cada método. Ele usa os capítulos 7 e 22 e prepara os capítulos 24, 27 e 33.

### 23.1 Modelagem de ameaças

A modelagem de ameaças pergunta, de forma sistemática, o que pode dar errado em cada elemento e em cada fronteira de confiança de um modelo de sistema. O **STRIDE** — falsificação de identidade (spoofing), adulteração (tampering), repúdio, divulgação de informações, negação de serviço, elevação de privilégios — é um mnemônico para categorias de ameaças aplicado a cada fluxo de dados, processo e repositório. O [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) cataloga táticas e técnicas de adversários observadas contra sistemas industriais, do acesso inicial ao impacto (por exemplo, manipulação do controle ou perda de visão). Use o STRIDE para gerar ameaças candidatas elemento por elemento e o ATT&CK para conferir o realismo e a completude contra o comportamento observado.

### 23.2 Árvores de falhas

Uma árvore de falhas decompõe um evento de topo indesejado em combinações de eventos básicos usando portas E e OU. Um **conjunto de corte mínimo** é um menor conjunto de eventos básicos cuja ocorrência conjunta causa o evento de topo; a lista dos conjuntos de corte mínimos é a lógica de falha do sistema em sua forma mais simples. Conjuntos de corte de um único evento são pontos únicos de falha. Com probabilidades independentes dos eventos básicos, a probabilidade do evento de topo é calculada exatamente por enumeração para árvores pequenas, ou aproximadamente somando as probabilidades dos conjuntos de corte (a **aproximação de eventos raros**, um limite superior quando as probabilidades são pequenas).

### 23.3 Árvores de ataque e bow-ties

Uma árvore de ataque aplica a mesma estrutura E/OU ao objetivo de um adversário; as folhas são ações do atacante com atributos como custo, habilidade ou detectabilidade, em vez de probabilidades. Atribuir probabilidades a ataques deliberados é questionável — os adversários se adaptam —, então as árvores de ataque costumam ser usadas para encontrar o caminho mais barato ou menos detectável e, depois, para posicionar controles nele. Um **bow-tie** junta as causas (à esquerda), o evento central e as consequências (à direita), mostrando as barreiras preventivas antes do evento e as barreiras mitigadoras depois dele; ele se comunica bem com operadores e gestores.

### 23.4 Combinando falhas e ataques

Os eventos de infraestrutura misturam causas acidentais e deliberadas: um atacante pode esperar por uma tempestade, ou uma falha pode mascarar uma intrusão. Métodos orientados por consequências, como o [CCE do INL](https://inl.gov/national-security/cce/), partem da consequência inaceitável e perguntam quais combinações de falhas e ações de adversários chegam a ela. Uma abordagem prática: construa a árvore de falhas para a consequência; marque quais eventos básicos um adversário poderia causar deliberadamente; recalcule com esses eventos definidos como "ocorridos" para ver o que resta como proteção. O que restar é sua verdadeira defesa contra um adversário capaz.

### 23.5 Exemplo resolvido: perda do abastecimento do hospital (sintético)

Evento de topo: o St Brenna's perde o abastecimento por mais de 4 h num ano. Seguindo o modelo do Capítulo 22: o caminho A (PS4) se perde se a PS4 falhar, ou se o alimentador F2 *e* o gerador da PS4 falharem ambos; o caminho B se perde se o reservatório estiver indisponível, se a PS3 falhar ou se o alimentador F1 falhar; e o evento exige os dois caminhos perdidos *e* o tanque do hospital falhando em cobrir a lacuna (TANK). O Laboratório 9 enumera a árvore com probabilidades anuais sintéticas. Há seis conjuntos de corte mínimos, todos de ordem três ou quatro, porque TANK aparece em todos eles. O maior contribuinte é {G1, PS4, TANK}. A probabilidade exata é de 9,10 × 10⁻⁵ por ano; a aproximação de eventos raros dá 9,36 × 10⁻⁵.

Agora a visão adversarial: se um atacante consegue parar remotamente a PS3 e a PS4 (sem R1), as duas passam a "ocorridas" e o evento de topo se reduz apenas a TANK — probabilidade de 0,03. A autenticação dos comandos remotos faz o sistema passar de um problema de duas de três falhas independentes para um problema de ponto único de falha. Essa comparação é o argumento mais claro a favor de R1 em todo o dossiê.

### 23.6 Atividade prática: Laboratório 9

```python
# Lab 9 - fault tree: minimal cut sets and top-event probability (synthetic annual probabilities, offline)
from itertools import product
P = {"G1": 0.10, "G2": 0.08, "GEN": 0.05, "PS4": 0.02, "PS3": 0.02, "RES": 0.01, "TANK": 0.03}
# Top: hospital loses supply > 4 h = (feed A lost AND feed B lost)
# feed A (PS4 direct) lost = PS4 OR (G2 AND GEN);  feed B (reservoir) lost = RES OR PS3 OR G1
# hospital on-site tank TANK failing (empty/contaminated) is needed too: top = A AND B AND TANK
def top(s): A = s["PS4"] or (s["G2"] and s["GEN"]); B = s["RES"] or s["PS3"] or s["G1"]; return A and B and s["TANK"]
names = list(P); exact = 0.0; cuts = []
for bits in product([0, 1], repeat=len(names)):
    s = dict(zip(names, bits)); pr = 1.0
    for n in names: pr *= P[n] if s[n] else 1 - P[n]
    if top(s):
        exact += pr
        on = frozenset(n for n in names if s[n])
        cuts.append(on)
mcs = sorted({c for c in cuts if not any(o < c for o in cuts)}, key=lambda c: (len(c), sorted(c)))
for c in mcs:
    pr = 1.0
    for n in c: pr *= P[n]
    print(sorted(c), f"{pr:.2e}")
rare = sum(eval("*".join(str(P[n]) for n in c)) for c in mcs)
print(f"rare-event approx {rare:.3e}  exact {exact:.3e}")
```

Saída esperada:

```text
['G1', 'PS4', 'TANK'] 6.00e-05
['PS3', 'PS4', 'TANK'] 1.20e-05
['PS4', 'RES', 'TANK'] 6.00e-06
['G1', 'G2', 'GEN', 'TANK'] 1.20e-05
['G2', 'GEN', 'PS3', 'TANK'] 2.40e-06
['G2', 'GEN', 'RES', 'TANK'] 1.20e-06
rare-event approx 9.360e-05  exact 9.101e-05
```

Os seis conjuntos de corte contêm TANK, então a reservação própria do hospital aparece em todos os caminhos até o evento de topo. O maior contribuinte isolado combina o alimentador F1, a PS4 e o tanque. Os dois valores de probabilidade diferem ligeiramente porque a aproximação de eventos raros conta duas vezes os conjuntos de corte que se sobrepõem, então dá um pequeno limite superior para o valor exato. A leitura adversarial do exemplo resolvido vem de definir a PS3 e a PS4 como falha certa e executar de novo, o que o EX045 pede que você mesmo faça.

### 23.7 Erros comuns e limites

- Árvores de falhas com eventos básicos dependentes tratados como independentes (energia comum, software comum).
- Probabilidades de ataques deliberados apresentadas como frequências.
- Modelos de ameaças sem fronteiras de confiança.
- Listas STRIDE nunca conferidas contra o comportamento observado de adversários.
- Tratar a aproximação de eventos raros como exata quando as probabilidades são grandes.

O próprio Laboratório 9 supõe independência, então uma falha de software compartilhada nas RTUs das duas estações tornaria seus números otimistas. Suas probabilidades de falha da PS3 e da PS4 são frequências de falhas aleatórias, então não dizem nada sobre quão provável é que um atacante pare as duas estações, e é por isso que o caso adversarial é tratado por condicionamento, e não pelo acréscimo de uma probabilidade de ataque.

### Exercícios — capítulo 23

**EX045 — Árvore condicionada ao adversário.** *Objetivo:* quantificar o que a autenticação compra. *Entradas:* Laboratório 9. *Passos:* (1) defina a PS3 e a PS4 com probabilidade 1 (o atacante consegue pará-las remotamente) e calcule a probabilidade do evento de topo; (2) em vez disso, defina G1 e G2 como 1 (o atacante consegue cortar os dois alimentadores) e recalcule; (3) interprete ambos. *Evidência esperada:* números e uma interpretação de 150 palavras. *Rubrica:* 3 = números corretos (0,03; e, com G1=G2=1, topo = P(TANK)·P(PS4 ou GEN) — calcule), interpretação ligada aos controles (R1; independência do gerador e o tanque); 2 = um número errado; 1 = não executado; 0 = nada.

**EX046 — STRIDE num fluxo.** *Objetivo:* modelar as ameaças de um fluxo de dados. *Entradas:* o fluxo gateway–SCADA (quadros do Laboratório 8 sobre o conduto LTE). *Passos:* aplique cada categoria do STRIDE, nomeie uma técnica do ATT&CK for ICS onde couber e declare o controle existente ou proposto. *Evidência esperada:* tabela de seis linhas. *Rubrica:* 3 = as seis categorias significativas e controles correspondentes (por exemplo, falsificação de identidade → MAC; negação de serviço → retorno ao automático local); 2 = uma categoria vazia; 1 = apenas a lista; 0 = nada.

### Síntese do capítulo

Os modelos de ameaças geram o que poderia dar errado em cada fronteira de confiança; o ATT&CK os mantém realistas. As árvores de falhas e os conjuntos de corte mínimos mostram a lógica de falha e os pontos únicos de falha; as árvores de ataque e os bow-ties mostram os caminhos dos adversários e as barreiras. Combine-os condicionando ao que um adversário consegue causar: o que restar é a defesa que realmente importa.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue estudando — capítulo 23 de 50

[← Capítulo 22](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Infraestrutura crítica e segurança setorial: métodos I

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) selecionar métodos de análise adequados a uma questão de projeto — avaliação de riscos, STPA, simulação, experimento em bancada de testes, exercício de mesa; (2) conduzir uma avaliação de riscos estruturada e documentá-la de forma reprodutível; (3) planejar um estudo de simulação com verificação e validação explícitas; e (4) escolher evidências proporcionais à decisão. Ele se apoia nos capítulos 15, 21 e 23 e prepara o ateliê de projeto (Capítulo 25).

### 24.1 Associar o método à questão

| Questão | Método | Evidência típica |
|---|---|---|
| Quais cenários importam mais? | Avaliação de riscos (SP 800-30, IEC 62443-3-2) | Tabela de cenários, justificativa |
| Quais ações de controle são inseguras? | STPA ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)) | Ações de controle inseguras, cenários de perda |
| Como o processo responde? | Simulação (laboratórios 1 e 7) | Modelo, registro de V&V, execuções |
| O controle funciona na prática? | Experimento em bancada de testes | Plano de teste, resultados, logs |
| As pessoas conseguem executar o plano? | Exercício de mesa ou funcional | Relatório pós-ação |
| O projeto é sólido? | Revisão independente (Capítulo 45) | Constatações da revisão e respostas |

Os projetos de engenharia usam vários; um erro comum é usar um método para responder à questão de outro — por exemplo, um exercício de mesa "mostrando" que um tempo de restauração é alcançável.

### 24.2 Avaliação de riscos estruturada

Uma avaliação reprodutível documenta: escopo e suposições; versão do modelo de sistema; fontes de ameaça e suas capacidades supostas; cenários (evento de ameaça → vulnerabilidade → consequência); controles existentes; escalas de probabilidade e de consequência com definições; classificações com justificativa; e controles recomendados. As escalas precisam ser definidas nos termos da organização (pessoas-hora sem água, não "alto"). Classificações sem justificativa são opiniões; com justificativa, podem ser contestadas e melhoradas. As escalas do TMRP usam pessoas-hora sem água no hospital e nos demais clientes, então as classificações significam a mesma coisa para operadores e gestores.

### 24.3 Simulação com verificação e validação

A **verificação** pergunta se o modelo está implementado corretamente (o código faz o que o modelo diz?); a **validação** pergunta se o modelo representa a realidade bem o bastante para seu propósito. [Sargent (2013)](https://doi.org/10.1057/jos.2012.20) descreve técnicas: comparação com resultados analíticos (o Euler do Laboratório 1 versus a solução exata), testes em condições extremas, comparação com dados históricos, validade aparente junto aos operadores e análise de sensibilidade. Declare o uso pretendido do modelo; um modelo válido para estimar a autonomia pode ser inválido para a análise de transientes de pressão. No TMRP, o modelo de autonomia é validado contra uma interrupção planejada histórica antes de ser usado no cenário combinado de falta de energia da rede e perda de telemetria.

### 24.4 Exercícios com pessoas

Os exercícios de mesa conduzem uma equipe por um cenário para testar planos, papéis e decisões; os exercícios funcionais executam algumas ações de verdade. Projete-os com objetivos, injeções, observadores e um relatório pós-ação que registre as lacunas sem atribuir culpa. Eles mostram se as pessoas sabem o que fazer e onde os planos são ambíguos; não medem o desempenho dos equipamentos. O exercício funcional noturno do TMRP, do modo manual local na PS3 e na PS4, é o exemplo: ele usa a equipe noturna real, registra o tempo gasto para estabelecer a operação manual e relata as lacunas que encontra, mas não consegue mostrar se as bombas ou os gateways atendem aos seus próprios requisitos.

### 24.5 Exemplo resolvido: escolhendo os métodos para o TMRP (sintético)

O TMRP tem quatro questões em aberto: (1) quais cenários merecem financiamento — avaliação de riscos com escalas de consequência em pessoas-hora; (2) se os operadores conseguem passar a PS3/PS4 para manual local em até 1 h — um exercício funcional à noite, com a equipe real; (3) se o gateway rejeita quadros forjados e repetidos — testes T1–T2 em bancada; (4) se o reservatório dura o suficiente durante uma falta combinada de energia da rede e de telemetria — uma simulação no estilo do Laboratório 1, validada contra uma interrupção planejada histórica. O plano nomeia a evidência de cada método e seu limite, para que ninguém cite depois o exercício de mesa como prova de R6.

### 24.6 Atividade prática

Conduza com dois colegas um exercício de mesa de 45 minutos sobre o cenário "servidores SCADA cifrados às 02:00", usando o conjunto de requisitos do TMRP. Registre decisões, horários e lacunas num relatório pós-ação. Atribua os papéis antes de começar: o operador noturno, o gerente de plantão e um facilitador que faz as injeções. Use os requisitos do TMRP como régua, especialmente a operação manual local em até uma hora e a restauração da operação remota em até oito. Registre cada decisão com seu horário e quem a tomou. O relatório pós-ação deve listar o que o plano não cobriu, sem apontar ninguém como causa, e deve declarar que um exercício de mesa não consegue mostrar se a restauração em oito horas é alcançável.

### 24.7 Erros comuns e limites

- Um método esticado para responder a todas as questões.
- Escalas de probabilidade e de consequência não definidas.
- Simulação apresentada sem V&V ou sem uso pretendido.
- Relatórios de exercícios que culpam indivíduos ou registram apenas os sucessos.
- Evidência desproporcional à decisão (pouca demais para o que é crítico para a segurança, demais para o trivial).

O plano de métodos do TMRP se protege contra o primeiro erro ao nomear o limite de cada método, de modo que um exercício de mesa nunca seja citado como prova de que R6 foi atendido. Suas escalas de probabilidade e de consequência são definidas em pessoas-hora, e a simulação de autonomia declara seu uso pretendido.

### Exercícios — capítulo 24

**EX047 — Associação de métodos.** *Objetivo:* selecionar métodos. *Entradas:* quatro questões: (a) setpoints forjados na PS4 causariam sobrepressão? (b) o detector de anomalias do fornecedor encontra inundações de escritas Modbus? (c) o gerente de plantão consegue autorizar o modo manual local à noite? (d) qual é a classificação anual de risco de oito cenários? *Passos:* escolha um método para cada uma, sua evidência e seu principal limite. *Evidência esperada:* tabela. *Rubrica:* 3 = (a) simulação/análise hidráulica mais STPA, (b) experimento em bancada, (c) exercício, (d) avaliação de riscos, com limites honestos; 2 = uma associação errada; 1 = um método para todas; 0 = nada.

**EX048 — Valide um modelo.** *Objetivo:* planejar a V&V. *Entradas:* o modelo do Laboratório 1. *Passos:* proponha três verificações e três validações, incluindo uma com dados históricos, e declare o uso pretendido do modelo e um uso para o qual ele é inválido. *Evidência esperada:* lista. *Rubrica:* 3 = verificação e validação distintas, comparação histórica especificada, uso inválido identificado (por exemplo, transientes de pressão, qualidade da água); 2 = V e V misturadas; 1 = vago; 0 = nada.

### Síntese do capítulo

Associe cada questão a um método capaz de respondê-la e conheça o limite de cada método. Torne as avaliações de riscos reprodutíveis, com escalas definidas e justificativas; verifique e valide as simulações para um propósito declarado; use os exercícios para testar pessoas e planos, não equipamentos; e dimensione a evidência de acordo com a decisão que ela sustenta.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue estudando — capítulo 24 de 50

[← Capítulo 23](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) conduzir um ateliê de projeto estruturado, do briefing ao conceito revisado; (2) gerar e comparar alternativas de conceito contra critérios ponderados; (3) apresentar um conceito, com suas suposições, riscos e plano de verificação, a uma banca de revisão crítica; e (4) responder de forma construtiva às constatações da revisão. Ele integra os capítulos 16–24 no primeiro artefato de projeto completo e prepara o Capítulo 26.

### 25.1 O que é um ateliê

Um ateliê de projeto é um exercício de projeto iterativo e criticado. As equipes recebem um briefing, produzem conceitos, apresentam-nos a revisores que contestam as suposições e revisam. Seu valor está na crítica: os projetos melhoram mais depressa quando alguém competente tenta quebrá-los cedo. Neste curso, cada ateliê produz um **dossiê de conceito**: enunciado do problema, trecho dos requisitos, alternativas, avaliação, conceito selecionado, registro de riscos, plano de verificação e questões em aberto. No TMRP, o dossiê do Ateliê I cobre a operação remota das seis estações de bombeamento e da estação de Fenwick.

### 25.2 O briefing

**Briefing do Ateliê I (sintético):** a LRWA precisa proteger a operação remota da PS1–PS6 e da estação de Fenwick. Restrições: orçamento de 250 mil (Laboratório 16); a PS1 e a PS2 têm unidades RTU-A legadas que não podem ser substituídas por três anos; a LTE privada é o único enlace econômico; uma sala de controle, com equipe 24/7 e um único operador à noite; o hospital precisa de interrupção ≤ 4 h. Entregar: de dois a quatro conceitos, avaliação, seleção e plano de verificação.

A restrição da equipe noturna é a que mais molda os conceitos, porque qualquer projeto que exija que alguém dirija até uma estação para cada mudança deixa um único operador incapaz de dar conta de seis instalações.

### 25.3 Gerando alternativas

Gere conceitos que difiram em princípio, não em detalhe: (A) LTE cifrada pela operadora, apenas com firewall central; (B) túneis IPsec a partir das RTUs novas, gateways para as legadas; (C) autenticação na camada de aplicação com gateways e forte autonomia local; (D) nenhum controle remoto — apenas monitoramento, com operadores despachados para cada mudança. Incluir um extremo (D) esclarece quanto vale o controle remoto. Os quatro conceitos diferem quanto a onde a autenticação acontece e se o controle remoto existe. A nota muito baixa do conceito D em operabilidade, na avaliação, mostra por que vale a pena incluir um extremo.

### 25.4 Avaliação ponderada

Defina os critérios a partir dos requisitos e das restrições, atribua os pesos antes de pontuar, pontue cada conceito com evidências e teste se a classificação sobrevive a mudanças plausíveis dos pesos (sensibilidade). Uma soma ponderada é uma conversa estruturada, não um oráculo.

| Critério (peso) | A | B | C | D |
|---|---:|---:|---:|---:|
| Impede comandos forjados, R1 (0,30) | 1 | 4 | 4 | 5 |
| Serviço durante a perda da rede, R4 (0,20) | 2 | 3 | 5 | 5 |
| Operabilidade com um operador noturno (0,20) | 5 | 4 | 4 | 1 |
| Custo dentro de 250 mil (0,15) | 5 | 2 | 4 | 4 |
| Compatibilidade com o legado (0,15) | 5 | 3 | 4 | 5 |
| **Nota ponderada** | **3,20** | **3,35** | **4,20** | **4,05** |

D fica perto de C porque é muito seguro, mas sua nota de operabilidade reflete que um operador noturno não consegue dirigir até seis instalações; na prática, ele não atende à necessidade do hospital. O desafio da banca à equipe é mostrar que a liderança de C sobrevive se a operabilidade tiver peso 0,10 e R1, peso 0,40 (EX049).

### 25.5 Apresentar e responder à revisão

Apresente: o problema em uma frase, as restrições, as alternativas, a avaliação, a seleção, os riscos e o que você não verificou. Os revisores vão atacar as suposições; registre cada constatação, responda (aceitar, rejeitar com motivo, adiar com dono) e revise. Uma equipe defensiva não aprende nada; uma equipe que aceita todo comentário não tem projeto. As constatações da banca no EX050 são típicas do TMRP: o gateway como ponto único de falha, o modo manual local contornando a autenticação e a falta dos custos de pessoal da gestão de chaves. Cada uma precisa de uma resposta registrada, com dono. A segunda pode ser respondida com evidências que já existem, porque a chave seletora, o alarme e o log local foram registrados quando o conflito entre R4 e R1 foi resolvido.

### 25.6 Atividade prática

Produza o dossiê de conceito para o briefing do Ateliê I em no máximo oito páginas e faça uma revisão de 20 minutos com dois colegas atuando como banca. Limite-se a oito páginas para que a banca consiga lê-lo antes da revisão. Apresente os quatro conceitos na tabela ponderada, mostre a verificação de sensibilidade e declare o que não foi verificado. Peça a cada colega que ataque uma suposição, como a estimativa de custo ou a nota de operabilidade noturna. Registre as constatações num registro de respostas com aceitar, rejeitar ou adiar e um dono, como pede o EX050, e revise o conceito antes de entregar o dossiê.

### 25.7 Erros comuns e limites

- Alternativas que são variações de uma única ideia.
- Pesos escolhidos depois da pontuação.
- Notas sem evidências.
- Nenhuma verificação de sensibilidade.
- Tratar a revisão como uma prova a ser superada, e não como informação.

O Ateliê I se protege contra esses erros: seus quatro conceitos diferem em princípio, seus pesos foram fixados antes da pontuação, e o EX049 testa se a liderança do conceito C sobrevive a outros pesos. O desafio da banca ao conceito D, que pontua bem em segurança mas falha na operabilidade noturna, é o tipo de constatação que uma revisão deve produzir. Toda nota cita evidências.

### Exercícios — capítulo 25

**EX049 — Sensibilidade aos pesos.** *Objetivo:* testar a robustez de uma seleção. *Entradas:* a tabela da §25.4. *Passos:* recalcule com os pesos (R1 0,40, perda da rede 0,20, operabilidade 0,10, custo 0,15, legado 0,15) e com (R1 0,20, perda da rede 0,20, operabilidade 0,30, custo 0,15, legado 0,15). *Evidência esperada:* notas e conclusão. *Rubrica:* 3 = aritmética correta e uma conclusão honesta sobre quando D ultrapassa C e o que isso implica; 2 = um erro aritmético; 1 = um cenário; 0 = nada.

**EX050 — Registro de respostas à revisão.** *Objetivo:* responder à crítica. *Entradas:* três constatações da banca: "o gateway é um ponto único de falha"; "o modo manual local contorna a autenticação"; "a estimativa de custo ignora o pessoal da gestão de chaves". *Passos:* escreva uma entrada no registro de respostas para cada uma (aceitar/rejeitar/adiar, motivo, mudança, dono). *Evidência esperada:* registro. *Rubrica:* 3 = respostas substantivas, com mudanças de projeto onde forem justificadas (por exemplo, gateways duplos ou falha para o automático local; chave seletora e alarme; acrescentar uma linha de custo operacional); 2 = uma resposta desdenhosa; 1 = aceita tudo sem mudanças; 0 = nada.

### Síntese do capítulo

Um ateliê transforma conhecimento num projeto sob crítica. Gere alternativas genuinamente diferentes, incluindo extremos; pondere os critérios antes de pontuar e teste a sensibilidade; apresente abertamente as suposições e as afirmações não verificadas; e trate as constatações da revisão como informação de projeto, com respostas registradas.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue estudando — capítulo 25 de 50

[← Capítulo 24](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Infraestrutura crítica e segurança setorial: alternativas de arquitetura

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) comparar padrões de arquitetura para sistemas críticos — controle centralizado versus distribuído, esquemas de redundância, diversidade, fluxos unidirecionais, autonomia local; (2) analisar o comportamento de cada padrão diante de falhas e ataques; (3) quantificar os compromissos usando os modelos de disponibilidade, latência e custo dos capítulos anteriores; e (4) documentar as decisões de arquitetura com suas consequências. Ele desenvolve o conceito selecionado no Ateliê I e prepara o Capítulo 27.

### 26.1 Controle centralizado e distribuído

O controle centralizado (um SCADA dirigindo dispositivos de campo simples) dá aos operadores uma visão única e facilita a coordenação, mas concentra tanto as falhas quanto os ataques. O controle distribuído (controladores de campo capazes, que funcionam localmente e aceitam alvos de supervisão) degrada com elegância quando o centro ou a rede se perdem, ao custo de mais dispositivos para proteger e configurar. A maioria dos projetos resilientes é hierárquica: o controle local mantém a operação segura de forma autônoma; o centro otimiza e coordena. A escolha do TMRP, a hierárquica C2, mantém o controle automático local em todas as estações.

### 26.2 Padrões de redundância

- **Reserva quente (hot standby):** uma segunda unidade funcionando e pronta para assumir automaticamente (pares de servidores SCADA).
- **Reserva fria (cold standby):** uma reserva que precisa ser ligada ou instalada (RTUs reservas na prateleira).
- **N+1:** uma unidade a mais do que o necessário (três bombas onde duas atendem à demanda).
- **Votação k-de-n:** usada em sistemas de segurança operacional (sensores 2-de-3) para tolerar uma entrada defeituosa ou falsificada.

Cada padrão precisa ser julgado diante das causas comuns (Capítulo 7): dois servidores idênticos com software idêntico são redundantes contra falhas de hardware, não contra malware.

### 26.3 Diversidade

A diversidade — tecnologias, fornecedores, caminhos ou equipes diferentes — reduz as causas comuns. Ela custa mais, aumenta as habilidades necessárias e pode acrescentar superfície de ataque. Use-a onde uma causa comum seria inaceitável: um segundo caminho de comunicação por outra operadora e com outra energia; um desarme de segurança por fiação dedicada, independente do software; uma régua manual que um operador consiga ler quando toda a eletrônica está sob suspeita. Na LRWA, o argumento a favor da diversidade é mais claro no caminho da telemetria, onde uma segunda operadora com energia separada eliminaria a dependência compartilhada do alimentador F1, e em Hollin Hill, onde uma régua de nível manual dá aos operadores uma leitura em que podem confiar quando toda a eletrônica está sob suspeita.

### 26.4 Fluxos unidirecionais e autonomia local

Os gateways unidirecionais impõem fisicamente o fluxo de dados apenas para fora; eles eliminam toda uma classe de ataques de entrada no lado protegido, mas também eliminam o controle remoto por esse caminho. A autonomia local — a capacidade de uma instalação de funcionar com segurança sem o centro — é um padrão de resiliência que também limita a consequência dos ataques: um centro comprometido pode atrapalhar a otimização, mas não deve conseguir levar uma instalação para fora dos limites seguros se esses limites forem impostos localmente (R3). A opção C3 do TMRP leva isso ao limite para o monitoramento.

### 26.5 Exemplo resolvido: três arquiteturas do TMRP comparadas (sintético)

| Propriedade | C1: central + IPsec | C2: hierárquica + autenticação na camada de aplicação (escolha do Ateliê I) | C3: hierárquica + diodo para o monitoramento, controle apenas local |
|---|---|---|---|
| Comando remoto forjado | Exige a chave do túnel ou o comprometimento do SCADA | Exige a chave da estação ou o comprometimento do SCADA | Impossível remotamente |
| Centro comprometido | Pode comandar qualquer instalação dentro dos limites da RTU | Pode comandar qualquer instalação dentro dos limites impostos localmente | Não consegue comandar |
| Perda da rede | As instalações mantêm o último estado | As instalações funcionam em automático local por 72 h | As instalações funcionam em automático local |
| Operabilidade | Alta | Alta | Baixa à noite (despacho necessário) |
| Indisponibilidade das comunicações, duas operadoras, β = 0,05 | 0,00136 | 0,00136 | n/a para o controle |
| Custo | Médio | Médio | Capital baixo, pessoal alto |

A tabela torna explícito o risco residual de C2: um centro SCADA comprometido ainda consegue emitir comandos autenticados dentro dos limites locais. Esse risco residual é aceito com base no monitoramento, na aprovação por duas pessoas para mudanças de setpoint em lote e em limites locais que mantêm o processo seguro.

### 26.6 Atividade prática

Escreva um ADR escolhendo entre C2 e C3 especificamente para a PS4 (a alimentação do hospital), considerando que os setpoints da PS4 mudam raramente. Parta da tabela de comparação e do que torna a PS4 especial: ela alimenta diretamente o St Brenna's e seus setpoints mudam raramente. Pese a segurança de eliminar as escritas remotas de setpoint contra o custo de enviar um técnico para cada mudança, especialmente à noite, com um único operador de plantão. Diga o que o faria rever a decisão, como mudanças de setpoint mais frequentes. A defesa do Capítulo 50 mais tarde se refere a um ADR com exatamente essa opção de controle apenas local para a PS4.

### 26.7 Erros comuns e limites

- Redundância sem diversidade, alegada como resiliência contra ataques.
- Diversidade em toda parte, sobrecarregando a capacidade de manutenção.
- Centralização por conveniência sem limites seguros locais.
- Ignorar o custo operacional de arquiteturas que eliminam o controle remoto.
- Comparações de arquitetura sem números onde há números disponíveis.

A tabela do TMRP evita o último erro ao colocar números onde eles existem, como a indisponibilidade das comunicações com um fator de causa comum, e ao declarar com clareza o custo de pessoal de C3. Ela também aceita abertamente o risco residual de C2, em vez de alegar que sua redundância protege contra ataques.

### Exercícios — capítulo 26

**EX051 — Votação contra falsificação.** *Objetivo:* analisar a votação 2-de-3. *Entradas:* três transmissores de nível em Hollin Hill; seleção pela mediana. *Passos:* explique o que um transmissor falsificado consegue e não consegue fazer; o que um atacante que controle a RTU comum que lê os três consegue fazer; e como restabelecer a independência. *Evidência esperada:* meia página. *Rubrica:* 3 = a mediana tolera uma entrada falsificada, a RTU comum derrota a votação, independência por E/S ou controlador separados; 2 = ponto da RTU comum não percebido; 1 = genérico; 0 = nada.

**EX052 — Decisão de arquitetura da PS4.** *Objetivo:* escrever um registro de decisão. *Entradas:* §26.6. *Passos:* escreva o ADR com contexto, opções, decisão, consequências e condições de revisão. *Evidência esperada:* ADR. *Rubrica:* 3 = decisão justificada pela criticidade da PS4 e pelas mudanças raras de setpoint (C3 ou C2 com escritas de setpoint apenas locais, defendida), consequências incluindo o custo operacional, gatilhos de revisão; 2 = consequências fracas; 1 = sem opções; 0 = nada.

### Síntese do capítulo

Escolha a arquitetura pelo modo como ela falha e pelo modo como pode ser atacada. O controle hierárquico com limites seguros locais combina operabilidade com degradação elegante. A redundância protege contra falhas independentes, a diversidade contra causas comuns; os fluxos unidirecionais eliminam os caminhos de ataque de entrada junto com o controle remoto. Quantifique onde puder e documente o risco residual que você aceita.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue estudando — capítulo 26 de 50

[← Capítulo 25](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 (inglês) →](../../en/book/MANUSCRIPT.md#ch-27)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável. Os resultados numéricos foram produzidos executando os laboratórios e os scripts curtos descritos, com Python 3 e as sementes indicadas; seus últimos dígitos podem diferir se você mudar a ordem dos sorteios aleatórios. Nos exercícios de projeto, a rubrica do capítulo importa mais do que coincidir com a redação abaixo. Lowmarsh Regional Water Authority, St Brenna's Hospital, o TMRP e todos os números são sintéticos. Esta edição parcial traz as resoluções de EX001–EX052; as de EX053–EX100 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

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

### Capítulo 6

**EX011.** Com $k = 0.12$ h⁻¹: janela = ln 4 / 0,12 ≈ 11,6 h. Com 4 h para o restabelecimento manual, o alarme precisa chegar em até ≈ 7,6 h; com uma margem de segurança, especifique muito menos. Requisito: "A perda da dosagem de cloro deverá ser alarmada na sala de controle em até 30 min, detectada por um analisador e um registrador independentes do controlador de dosagem." 30 min deixam uma margem grande sob o pior caso de decaimento em tempo quente.

**EX012.** Exata: 0,6065; 0,3679; 0,2231; 0,1353; 0,0821 em t = 1…5. Euler com h = 1: 0,5; 0,25; 0,125; 0,0625; 0,0312 (estável, subestima). h = 3 (fator −0,5): −0,5; 0,25; −0,125; 0,0625; −0,0312 — oscila de sinal, fisicamente sem sentido, embora decaia. h = 5 (fator −1,5): −1,5; 2,25; −3,375; 5,06; −7,59 — instável. Euler explícito aplicado a $x' = -kx$ multiplica por $(1 - kh)$ a cada passo; $|1 - kh| > 1$ quando $h > 2/k = 4$.

### Capítulo 7

**EX013.** VPP: 0,009 (a priori 0,0001), 0,087 (0,001), 0,490 (0,01); com a priori 0,001 e FPR 0,001: 0,487. Reduzir dez vezes a taxa de falsos positivos melhora o valor preditivo aproximadamente tanto quanto um aumento de dez vezes na prevalência; com taxas-base baixas, a FPR é o parâmetro que vale a pena melhorar.

**EX014.** Indisponibilidade: β = 0 → 0,0004; β = 0,05 → 0,00136; β = 0,2 → 0,00426. Causas compartilhadas: energia e bateria da instalação; mastro de antena ou armário; mesmo modelo e firmware de modem; backhaul compartilhado ou acordos de roaming entre operadoras; mesma plataforma de provisionamento de SIM.

### Capítulo 8

**EX015.** Pior caso: o sinal de sucção baixa aparece logo após uma leitura das entradas, então só é visto na varredura seguinte (até 45 ms depois); a confirmação exige uma segunda varredura consecutiva (45 ms); a saída é escrita no fim dessa varredura. Pior caso ≈ 45 + 45 + 45 = 135 ms (mais o atraso do módulo de saída), o que viola os 100 ms. Correção: reduzir a varredura de pior caso, fazer a filtragem com um temporizador numa tarefa mais rápida ou usar um desarme por fiação dedicada.

**EX016.** A inicialização segura impede: (1) a instalação persistente de firmware não assinado ou modificado; (2) a inicialização de uma imagem rebaixada, se a proteção contra rollback for aplicada. Ela não impede: (1) a exploração, em tempo de execução, de uma vulnerabilidade em firmware assinado → aplicação de correções, validação de entradas, restrição de rede; (2) mudanças de lógica maliciosas, mas legítimas, pela interface de engenharia → programação autenticada e baseada em papéis, com detecção de mudanças e registro em log.

### Capítulo 9

**EX017.** 5 estados × 7 eventos = 35 pares. Listados: stopped+start, starting+run_confirmed, starting+timeout, running+stop, stopping+stop_confirmed, tripped+reset (6), mais `trip` a partir dos 5 estados (5) = 11. Não listados: 24. Exemplos com justificativa: tripped+start (religar dentro da falha — deve exigir reset local); stopped+run_confirmed (uma confirmação espúria ou forjada não pode criar a crença de "em funcionamento"); running+reset (o reset não pode limpar um desarme inexistente e mascarar o estado).

**EX018.** Invariante: para cada estação, `last[st]` nunca diminui e é igual ao maior contador aceito. Sequência 1, 2, 2, 1, 5 → aceita, aceita, rejeita (repetição), rejeita (repetição), aceita; estado final `last[3] == 5`. Após um reinício do receptor, `last` fica vazio, então mensagens já vistas voltam a ser aceitas, a menos que o receptor persista `last` ou que as chaves sejam trocadas no reinício.

### Capítulo 10

**EX019.** Perigo: um operador bloqueado durante uma emergência não consegue agir; um atacante pode bloquear os operadores deliberadamente (negação de serviço). Alternativa: nenhum bloqueio nas IHMs da sala de controle; em vez disso, atraso progressivo após falhas, alertas para falhas repetidas, contas nominais com autenticação forte, controle de acesso físico à sala de controle e uma liberação de emergência com presença física e registro em log. Verifique por teste (tentativas malsucedidas produzem atrasos e alertas, nunca bloqueio) e por exercício (o operador consegue entrar sob estresse).

**EX020.** Não visite, não sonde e não tente entrar na página, e não compartilhe a captura de tela. Notifique a concessionária de forma privada pelo seu contato de segurança publicado ou, se não houver, por um programa de divulgação coordenada como o da CISA, relatando apenas o que você observou e onde. O trabalho do curso pode descrever o padrão ("interfaces de gerenciamento expostas em documentos de compras") sem nomear a concessionária, o fornecedor, o modelo ou o local.

### Capítulo 11

**EX021.** O novo fluxo field → enterprise em TCP/445 é uma VIOLATION. Modele o jump host: acrescente a regra ("control", "field", "tcp", 22); então eng `10.5.0.12` → jump host `10.1.0.20` em TCP/22 é permitido; jump host → RTU `10.2.0.33` em TCP/22 é permitido; o acesso direto eng → RTU em TCP/22 continua sendo uma VIOLATION. Nenhuma regra dá à zona de engenharia acesso direto ao campo.

**EX022.** Típico: 120 + 180 + até 1.300 + 200 ≈ 1,8 s se um evento acabou de perder sua consulta (≈ 1,15 s em média, com espera de meio ciclo). Pior caso: 120 + 900 + 1.300 + 200 ≈ 2,5 s. A cláusula de 95% em até 1,5 s está em risco porque a espera pela consulta domina; a cláusula de 5 s é atendida. Mudança: relato por exceção (respostas não solicitadas) para os alarmes, para que não esperem pela consulta.

### Capítulo 12

**EX023.** U = 2/10 + 4/40 + 10/100 = 0,40. Limite para n = 3: 3(2^{1/3} − 1) ≈ 0,780. U ≤ limite, então o conjunto é escalonável sob prioridades rate-monotonic. O teste é suficiente, não necessário: um conjunto que ultrapasse o limite ainda poderia ser escalonável (uma análise exata do tempo de resposta decidiria).

**EX024.** Mitigar agora: desabilitar o serviço de compartilhamento de arquivos no historiador, se não for necessário, ou restringi-lo a um único host de engenharia nomeado; monitorar tentativas de conexão; aplicar a correção após a certificação do fornecedor, na janela de manutenção seguinte; data de revisão na certificação + 14 dias. Aceitar sem nenhuma ação ignora o caminho alcançável a partir da zona de engenharia.

### Capítulo 13

**EX025.** `chain(recs[:5])[-1] == anchor[4]` → True: um atacante que exclua o último registro e substitua a cabeça armazenada por `anchor[4]` passa despercebido. Incluir a contagem — âncora = H(cabeça ‖ n) — torna o truncamento detectável (verificado: a âncora truncada é diferente). Guarde a âncora no sistema de chamados de incidentes e num arquivo de gravação única fora da zona de controle e fora dos privilégios dos administradores do historiador.

**EX026.** O historiador de controle empurra os dados horários de energia e os valores de pressão ao vivo para uma réplica na DMZ (apenas para fora, imposto por firewall ou por um gateway unidirecional); finanças e o painel consultam a réplica. Nenhuma conexão de entrada na zona de controle. Se a réplica for comprometida, os atacantes podem ler ou falsificar os dados de relatório e os painéis — um problema de integridade e confidencialidade dos dados —, mas não ganham nenhum caminho para dentro do controle.

### Capítulo 14

**EX027.** Lista de verificação: comprimento da entrada verificado antes da indexação; integridade verificada antes do uso; comparação de segredos em tempo constante; nenhum segredo no código-fonte; caminhos de erro que rejeitam; exceções não engolidas; limites para laços e tamanhos; registro das rejeições em log sem segredos; ordem de bytes explícita; testes para cada caminho de rejeição. Constatações: Laboratório 3 — quadros truncados informam "crc" em vez de formato (clareza do diagnóstico); Laboratório 8 — chave fixada no código-fonte (aceitável apenas como demonstração rotulada).

**EX028.** Faça a correspondência do aviso com as entradas e versões do SBOM; confirme se a função ou o recurso vulnerável está presente e alcançável na configuração da RTU-B (por exemplo, o servidor TLS está habilitado? o interpretador vulnerável da biblioteca é usado?); peça ao fornecedor uma avaliação e um firmware corrigido; aplique controles compensatórios (restringir o conduto, desabilitar o recurso); comunique às operações; agende a atualização por meio da implantação em etapas; registre a decisão.

### Capítulo 15

**EX029.** Laboratório 8: aplica o projeto aberto (a segurança repousa na chave, não no segredo do algoritmo) e a mediação completa (toda mensagem é verificada); viola o privilégio mínimo/a separação no sentido de que a chave de demonstração está no código-fonte e é compartilhada entre as estações — correção: chaves por estação vindas de armazenamento protegido. Máquina de estados (§9.5): aplica padrões à prova de falhas (eventos não listados são rejeitados) e a separação de privilégios (o reset precisa de um operador local); não tratado: a economia de mecanismo, se for implementada com flags espalhadas — correção: implementação guiada por tabela.

**EX030.** Consequência 1: hospital sem água por > 4 h — funções usadas indevidamente: partida/parada das bombas na PS3/PS4, posições de válvulas; limite projetado: reservação própria do hospital mais uma lógica local de religamento automático que um comando remoto não consegue desabilitar. Consequência 2: superdosagem de cloro — funções: setpoint de dosagem e velocidade da bomba; limite projetado: bomba dosadora fisicamente dimensionada para que o curso máximo na vazão máxima não consiga ultrapassar uma concentração nociva, mais um desarme por fiação dedicada para residual alto.

### Capítulo 16

**EX031.** Um mapeamento: N1 ← R3, R4, R5 (em parte), R9; N2 ← R1, R2, R3, R7, R8; N3 ← R6, R8; N4 ← R5, R7. N3 depende do menor número. Proposta: "R10 — Backups off-line das configurações do SCADA e dos controladores deverão ser feitos semanalmente, guardados fora dos domínios de controle e corporativo, e ter a restauração testada trimestralmente."

**EX032.** Itens de dados (ID da estação, contador, nível, pressão, alarmes); codificação (binária, big-endian, quadro de 28 bytes mais o ID da suíte); taxa (1 a cada 10 s por estação, mais alarmes por exceção); latência (≤ 1 s no gateway); autenticação (HMAC-SHA256-128, chave por estação); tratamento de erros (rejeitar e registrar em log; alarme após 3 rejeições em 10 min; alarme de estação inativa em 60 s); fonte de tempo (NTP interno por um conduto da lista de permissões; carimbos de tempo em UTC); propriedade (gateway: engenharia do TMRP; lado do SCADA: operações); processo de mudança (revisão do ICD sob controle de configuração, com aprovação dos dois donos).

### Capítulo 17

**EX033.** Semente 17, ruído σ = 0,01 m, 48 h: limiar de 0,03 m → 2 episódios de falso alarme sem ataque (≈ 1 por dia), primeiro alarme na rampa de 0,05 m/h em 10,7 h; limiar de 0,05 m → 0 episódios de falso alarme, primeiro alarme da rampa em 10,9 h. Recomendação: 0,05 m — o atraso de detecção de 0,2 h é pequeno diante de horas de autonomia, enquanto falsos alarmes diários ensinariam os operadores a ignorar o detector. Confira de novo com dados reais de ruído.

**EX034.** Comprometer a RTU3 permite ao atacante falsificar tanto o nível quanto a vazão de entrada, de modo que o balanço de massa pode ser tornado coerente e o resíduo fica pequeno; comprometer apenas a RTU4 falsifica a vazão de saída e é detectável. Melhoria: um transmissor de nível independente ligado a um registrador separado (controlador e caminho de comunicação diferentes), ou uma leitura física regular da régua comparada com o SCADA.

### Capítulo 18

**EX035.** A regra reprova no teste da DMZ: um servidor de ERP comprometido poderia enviar pacotes diretamente ao banco de dados do SCADA. Alternativa: o ERP escreve o estado das ordens de serviço num serviço da DMZ; um processo da zona de controle busca as atualizações (ou as recebe por um intermediário com validação estreita), validando formato e conteúdo; nenhuma conexão de entrada do corporativo para o controle.

**EX036.** Caminho: fornecedor → gateway de acesso da DMZ (MFA, contas nominais do fornecedor) → sessão aprovada a cada pedido pelo gerente de plantão → jump host na zona de controle → apenas a interface de diagnóstico da RTU-B; sessão gravada; o acesso expira no fim da janela aprovada; conta do fornecedor desabilitada entre as sessões. Evidências: logs do gateway e do jump host, sessões gravadas, um teste mostrando que a conexão direta do fornecedor às RTUs é bloqueada e uma revisão trimestral das contas.

### Capítulo 19

**EX037.** Se a RTU persiste seu contador a cada 1.000 incrementos e reinicia, o último valor persistido pode estar até 999 atrás do último valor usado. Para evitar reutilizar um contador (o que o receptor rejeitaria, ou que poderia permitir repetição após um reinício do receptor), a RTU salta à frente pelo menos 1.000 além do valor persistido. O receptor precisa persistir o último contador aceito por estação, ou os dois lados trocam as chaves após o reinício.

**EX038.** A (chave da frota): uma RTU roubada permite ao ladrão forjar mensagens para todas as 42 estações; a recuperação exige trocar as chaves de todas as estações. B (chaves por estação): a falsificação fica confinada à estação roubada; uma chave é revogada e substituída. Armazenar 42 chaves num HSM é trivial para o SCADA. Recomendação: B.

### Capítulo 20

**EX039.** Avaliado pela rubrica; por exemplo, distribuição de eletricidade: unidades de consequência — consumidores interrompidos × horas, MW não supridos, clientes críticos afetados; tecnologias — relés de proteção, sistemas de gerenciamento da distribuição, RTUs de subestações; regulações — normas NERC CIP (cite versão e data) e NIS2 (2022/2555) para operadores da UE; incidente — Ucrânia 2015, descrito a partir do IR-ALERT-H-16-056-01 da CISA.

**EX040.** Modelo: um único produto de segurança com acesso privilegiado ao kernel estava instalado em muitas organizações de setores diferentes e era atualizado automaticamente; uma atualização de conteúdo defeituosa derrubou hosts Windows simultaneamente, e a Microsoft estimou que cerca de 8,5 milhões de dispositivos foram afetados. A propriedade é uma causa comum por meio de uma dependência compartilhada, privilegiada e atualizada automaticamente. Prática: implantações de atualizações em etapas (canário) — pelos fornecedores e, onde possível, controladas pelos clientes para sistemas críticos — mais procedimentos de recuperação que não dependam dos hosts afetados. Não foi um ataque.

### Capítulo 21

**EX041.** Continuidade do serviço: "Na perda do SCADA, a PS3 e a PS4 deverão continuar em controle automático local, e os operadores deverão conseguir operá-las localmente em até 1 h (exercício)." Contenção: "Diante da suspeita de comprometimento do SCADA, os caminhos de comando remoto para todas as estações deverão ser desabilitados a partir dos gateways em até 15 min após a decisão (teste)." Restauração: "A operação remota deverá ser restabelecida a partir de backups off-line verificados em até 8 h após a decisão de restabelecer (ensaio)."

**EX042.** Conflito: acesso contínuo do operador vs nova autenticação a cada 15 min. Opções: (a) manter a nova autenticação; (b) nenhuma nova autenticação; (c) a tela apenas de visualização permanece ativa; as ações de controle exigem uma nova autenticação rápida (aproximação do crachá ou PIN) após 15 min de inatividade, com a sala de controle sob controle de acesso físico. Recomendação: (c). Dono: gerente de operações (dono do risco), com o líder de segurança.

### Capítulo 22

**EX043.** Com a PS4 precisando apenas de `grid_f2` em modo automático local (sem LTE para o abastecimento) e o abastecimento como OU: `{grid_f1}` → o abastecimento funciona (via PS4); `{ps4}` → funciona (via reservatório); `{ps4, grid_f1}` → falha. Um modelo que faça o abastecimento depender da telemetria falha indevidamente no primeiro caso.

**EX044.** Estados: automático remoto, automático local, manual local, degradado (uma bomba), desarmado, fora de serviço. Caminho de ataque: comandos de parada forjados e partidas/paradas repetidas (automático remoto → desarmado pela proteção do motor de partida) → se o reset do desarme for remoto, o atacante mantém a estação desarmada → fora de serviço. Controle: o reset do desarme exige ação local; comandos autenticados; limite de taxa para os comandos de partida.

### Capítulo 23

**EX045.** PS3 = PS4 = 1: topo = P(TANK) = 0,03. G1 = G2 = 1: caminho B perdido; caminho A perdido se a PS4 ou o GEN falhar: 1 − 0,98 × 0,95 = 0,069; topo = 0,03 × 0,069 = 0,00207. Interpretação: a autenticação dos comandos remotos remove o caminho mais barato do adversário (o topo cai de 0,03 para 9,1 × 10⁻⁵); se um adversário consegue cortar os dois alimentadores, o gerador e o tanque do hospital se tornam as barreiras decisivas — mantenha-os e teste-os.

**EX046.** Falsificação de identidade — quadros forjados (ATT&CK for ICS: Spoof Reporting Message) → MAC por estação. Adulteração — valores modificados em trânsito → MAC. Repúdio — disputas sobre comandos → logs assinados ou com MAC, com âncoras. Divulgação de informações — telemetria lida na rede da operadora → cifração da operadora mais cifração opcional da carga útil. Negação de serviço — interferência ou inundação (Denial of Service; Block Reporting Message) → retorno ao automático local, alarme de estação inativa, limites de taxa. Elevação de privilégios — comprometimento do gateway para emitir comandos → endurecimento do gateway, filtragem de códigos de função, limites locais.

### Capítulo 24

**EX047.** (a) Simulação hidráulica mais STPA do caminho do setpoint — limite: fidelidade do modelo para transientes. (b) Experimento em bancada com inundações rotuladas — limite: o tráfego de laboratório difere do da instalação. (c) Exercício funcional noturno — limite: uma única ocasião, efeito do observador. (d) Avaliação de riscos estruturada com escalas definidas — limite: estimativas, não medições.

**EX048.** Verificação: comparar o Euler com a integral exata (Laboratório 1); testes unitários de `demand` e `drawn`; casos extremos (demanda zero → autonomia infinita; demanda constante → V/q). Validação: comparar a queda de nível prevista com dados do historiador de uma parada planejada das bombas; validade aparente da curva de demanda junto aos operadores; sensibilidade à amplitude da demanda. Uso pretendido: estimativa de autonomia para planejamento. Inválido para transientes de pressão, qualidade da água e hidráulica da rede.

### Capítulo 25

**EX049.** Pesos (0,40, 0,20, 0,10, 0,15, 0,15): A 2,80, B 3,35, C 4,20, D 4,45 — D ultrapassa C. Pesos (0,20, 0,20, 0,30, 0,15, 0,15): A 3,60, B 3,35, C 4,20, D 3,65. A liderança de C depende de a operabilidade ter peso real; se os decisores valorizarem a prevenção de comandos forjados muito acima da operabilidade, D vence no papel — mas D não atende à necessidade do hospital, na prática, à noite, o que sugere que a operabilidade é mais bem expressa como uma restrição do que como um peso.

**EX050.** Ponto único de falha no gateway: aceitar — a falha do gateway precisa levar ao automático local, com alarme; acrescentar um gateway reserva frio por região. Contorno pelo modo manual: aceitar — chave seletora no painel, alarme no SCADA na mudança de modo, log local. Pessoal da gestão de chaves: aceitar — acrescentar 0,2 ETI de custo operacional e a manutenção do HSM ao caso de negócio; dono: gerente do TMRP.

### Capítulo 26

**EX051.** A mediana de três tolera um transmissor falsificado ou com defeito. Um atacante que controle a RTU que lê os três consegue falsificar os três de forma coerente, derrotando a votação. Restabeleça a independência ligando os transmissores a módulos de E/S ou controladores separados, com comunicações separadas, de modo que nenhum comprometimento isolado controle duas das três entradas.

**EX052.** ADR-modelo: contexto — a PS4 é a alimentação direta do hospital, os setpoints mudam cerca de uma vez por mês; opções — C2 (remoto dentro dos limites) ou C3/variante de C2 (escritas de setpoint apenas locais, monitoramento remoto); decisão — escritas de setpoint apenas locais na PS4, partida/parada remota mantida com autenticação; consequências — visita mensal à instalação para mudanças de setpoint, procedimentos de resposta local mais rápidos, risco residual D1 na PS4 reduzido a partida/parada; rever se a frequência de mudanças de setpoint aumentar ou se o quadro de pessoal mudar.

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
