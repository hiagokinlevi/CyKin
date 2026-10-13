# Infraestrutura Crítica e Segurança Setorial: Engenharia de Sistemas Seguros e Resilientes

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado (curso 138 de 207 na [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–50 de 50 têm texto didático escrito; os exercícios EX001–EX100 (dois por capítulo) têm resoluções correspondentes; dezessete laboratórios offline estão incorporados com suas saídas verificadas. Revisão independente por especialistas, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto. A meta do plano, de três exercícios por capítulo, ainda não foi atingida. Cobertura de capítulos em rascunho não é um livro concluído.
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
27. [Infraestrutura crítica e segurança setorial: projeto de controles](#ch-27)
28. [Infraestrutura crítica e segurança setorial: implementação I](#ch-28)
29. [Infraestrutura crítica e segurança setorial: medição](#ch-29)
30. [Laboratório de verificação I](#ch-30)
31. [Infraestrutura crítica e segurança setorial: implementação II](#ch-31)
32. [Infraestrutura crítica e segurança setorial: confiabilidade](#ch-32)
33. [Infraestrutura crítica e segurança setorial: segurança operacional e resiliência](#ch-33)
34. [Infraestrutura crítica e segurança setorial: integração](#ch-34)
35. [Ateliê de projeto II](#ch-35)
36. [Infraestrutura crítica e segurança setorial: desempenho e escala](#ch-36)
37. [Infraestrutura crítica e segurança setorial: operações](#ch-37)
38. [Infraestrutura crítica e segurança setorial: validação](#ch-38)
39. [Infraestrutura crítica e segurança setorial: manutenibilidade](#ch-39)
40. [Laboratório de verificação II](#ch-40)
41. [Infraestrutura crítica e segurança setorial: otimização de sistemas](#ch-41)
42. [Infraestrutura crítica e segurança setorial: pesquisa aplicada](#ch-42)
43. [Prática na indústria ou no serviço público](#ch-43)
44. [Projeto final de engenharia I](#ch-44)
45. [Revisão independente de projeto](#ch-45)
46. [Projeto final de engenharia II](#ch-46)
47. [Ensaio de falha e recuperação](#ch-47)
48. [Dossiê de evidências](#ch-48)
49. [Trabalho de conclusão de curso de engenharia](#ch-49)
50. [Defesa final](#ch-50)

As [resoluções](#worked-results) contêm EX001–EX100. Um [glossário](#glossary) e as [referências](#references) fecham o livro.


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

O método de Euler com passo de uma hora superestima o tempo em cerca de 0,4 h; com 0,01 h ele fica a 0,01 h da resposta exata. A derivada em t = 6 h é −210 m³/h: o esvaziamento mais rápido da janela.

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

[← Capítulo 25](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Infraestrutura crítica e segurança setorial: projeto de controles

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) projetar controles que tratam de cenários específicos com desempenho definido; (2) combinar controles preventivos, detectivos e de recuperação numa defesa em profundidade cujas camadas falham de forma independente; (3) dar preferência a limites projetados, baseados na física, para as piores consequências; e (4) especificar cada controle de modo que ele possa ser verificado. Ele aplica os capítulos 15, 23 e 26 e prepara os capítulos 28 e 30.

### 27.1 Do cenário ao controle

Cada cenário do Capítulo 23 recebe controles em três pontos: **prevenir** o evento de ameaça, **detectá-lo** se a prevenção falhar, e **limitar e recuperar-se** das consequências. Exemplo — comandos de parada forjados para a PS3 e a PS4: prevenir com comandos autenticados (R1); detectar com alarmes para anomalias de comando e mudanças de estado inesperadas; limitar com a lógica local de religamento automático e o tanque do hospital; recuperar com os procedimentos manuais locais (R4). Cada um desses controles precisa então ser especificado e verificado, como mostra o restante do capítulo, antes que o cenário da parada forjada possa ser considerado coberto no dossiê.

### 27.2 Limites projetados primeiro

Para as piores consequências, os controles mais robustos não dependem de software algum: válvulas de alívio de pressão, batentes mecânicos, intertravamentos por fiação dedicada, bombas dosadoras de produtos químicos fisicamente dimensionadas para que não consigam superdosar no curso máximo. A engenharia informada pela cibersegurança (veja o [CCE do INL](https://inl.gov/national-security/cce/)) enfatiza esses controles porque eles se mantêm mesmo que todos os sistemas digitais sejam comprometidos. Eles não conseguem cobrir tudo — uma válvula de alívio mecânica não impede que uma bomba seja desligada —, mas limitam os piores casos. Para a bomba dosadora da LRWA, o limite de curso dimensionado pelos engenheiros de processo é um controle desse tipo.

### 27.3 Camadas independentes

A defesa em profundidade só funciona se as camadas falharem de forma independente. Liste as dependências de cada camada: se a autenticação, o monitoramento e o registro em log dependem todos dos servidores SCADA, um único comprometimento derrota os três. Coloque pelo menos uma camada de detecção fora dos sistemas que ela observa (monitoramento passivo da rede, um analisador independente) e mantenha os materiais de recuperação (backups off-line, procedimentos, chaves reservas) fora do alcance da ameaça da qual se está recuperando. O TMRP aplica isso colocando o alarme do analisador de cloro num registrador separado e mantendo os backups off-line longe dos servidores SCADA que eles restaurariam.

### 27.4 Especificando os controles

Uma especificação de controle declara: o(s) cenário(s) de que ele trata; sua função; o desempenho (detecção em até X, taxa de rejeição, tempo de restauração); as dependências; o modo de falha (à prova de falhas ou operacional em falha, e o que isso significa aqui); o dono; e o método de verificação. Sem desempenho e verificação, um controle é uma intenção. A especificação dos limites de setpoint no exemplo resolvido abaixo mostra todos os elementos: o cenário, os limites e o limite de passo, a regra de alarme, as dependências, a manutenção do último setpoint válido como modo de falha e o teste T3 como verificação. Seu dono é a equipe de engenharia de controle que configura o controlador de dosagem.

### 27.5 Exemplo resolvido: limites de setpoint (sintético)

Cenário: um setpoint forjado ou errôneo leva a bomba dosadora de cloro a superdosar. Controles: (1) **projetado** — curso da bomba dosadora limitado fisicamente, de modo que a dose máxima na vazão máxima fique abaixo de uma concentração nociva (dimensionado pelos engenheiros de processo); (2) **preventivo** — limites e limites de passo no lado do controlador (R3), implementados no controlador, não na IHM, para que um SCADA comprometido não consiga contorná-los; (3) **detectivo** — alarme do analisador de cloro independente (R9) num registrador separado; (4) **recuperação** — procedimento para isolar a linha de dosagem e lavá-la. Especificação de (2): rejeitar setpoints fora de 0,5–5,5 mg/L ou que mudem mais de 0,5 mg/L por comando, rejeitar valores não finitos, registrar em log toda rejeição, alarmar após três rejeições em 10 minutos; à prova de falhas = manter o último setpoint válido; verificado pelo teste T3, incluindo testes baseados em propriedades (Laboratório 11).

### 27.6 Atividade prática

Escreva especificações completas para dois controles do cenário de parada forjada da §27.1, incluindo desempenho, dependências, modo de falha e verificação. Escolha um controle preventivo, como os comandos autenticados, e um controle de recuperação, como a operação manual local na PS3 e na PS4. Para cada um, declare o desempenho que ele precisa alcançar, do que depende e o que acontece quando falha. A autenticação deve falhar fechada para os comandos; a operação manual local precisa funcionar sem o SCADA e sem a rede. Nomeie um dono pelo papel e um método de verificação, e depois verifique se os dois controles compartilham alguma dependência que permitiria a um único evento derrotar ambos.

### 27.7 Erros comuns e limites

- Controles sem critérios de desempenho.
- Limites impostos na IHM, e não no controlador.
- "Camadas" que compartilham dependências.
- Nenhum limite projetado para a pior consequência quando um é viável.
- Materiais de recuperação alcançáveis pelo mesmo atacante.

O exemplo da dosagem evita cada um: os limites ficam no controlador, o alarme do analisador usa um registrador separado, o limite de curso é projetado, e cada elemento tem uma meta de desempenho. Os limites também mantêm o último setpoint válido quando um comando é rejeitado, de modo que o modo de falha está declarado, e cada rejeição é registrada em log para a regra de alarme.

### Exercícios — capítulo 27

**EX053 — Auditoria de dependências das camadas.** *Objetivo:* verificar a independência. *Entradas:* os quatro controles da §27.5 e sua implementação: limites do controlador no PLC de dosagem; analisador num registrador separado; registro em log via SCADA. *Passos:* liste as dependências de cada camada; identifique qualquer dependência compartilhada; proponha uma mudança. *Evidência esperada:* tabela e mudança. *Rubrica:* 3 = dependência compartilhada encontrada (registro e alarme das rejeições via SCADA), mudança proposta (log local mais caminho de alarme independente); 2 = sem mudança; 1 = apenas a lista; 0 = nada.

**EX054 — O significado de à prova de falhas.** *Objetivo:* definir modos de falha no contexto. *Entradas:* o gateway de telemetria autenticada na PS4. *Passos:* para a falha do gateway, defina o que significa à prova de falhas para (a) os comandos, (b) a telemetria, (c) o controle local, e justifique. *Evidência esperada:* três definições. *Rubrica:* 3 = os comandos falham fechados (rejeitados), a telemetria falha de forma visível (alarme no SCADA), o controle local continua automaticamente; 2 = uma mal definida; 1 = "à prova de falhas = desligar"; 0 = nada.

### Síntese do capítulo

Projete controles por cenário, nos pontos de prevenção, detecção e recuperação. Coloque limites físicos projetados nas piores consequências, imponha os limites onde o atacante não consiga contorná-los, torne as camadas independentes e especifique, para cada controle, desempenho, dependências, modo de falha, dono e verificação.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue estudando — capítulo 27 de 50

[← Capítulo 26](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Infraestrutura crítica e segurança setorial: implementação I

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) implementar um controle de segurança como código funcional com testes, a partir da especificação; (2) aplicar práticas de codificação segura para o tratamento de entradas, a criptografia e o tratamento de erros; (3) construir uma bancada de testes que exercite o controle off-line; e (4) registrar evidências de implementação que remetam aos requisitos. Ele implementa as especificações do Capítulo 27 e prepara o Capítulo 29.

### 28.1 Da especificação ao código

Parta da especificação do controle (Capítulo 27): cada "deverá" se torna pelo menos um teste antes do código ou junto com ele. Mantenha a implementação pequena e sem dependências onde for possível — o gateway deste livro usa apenas a biblioteca padrão do Python. Estruture-a como recomenda o Capítulo 9: um interpretador (Capítulo 4), um verificador (Capítulo 19), um repositório de estado (contadores contra repetição) e uma interface de saída, cada um testado separadamente. O gateway do TMRP segue essa estrutura, e é por isso que seu bug de NaN pôde ser encontrado e corrigido apenas no validador.

### 28.2 Codificação segura para os caminhos de controle

- Valide a entrada antes de usá-la: comprimento, MAC, contador, formato, faixa física (laboratórios 3 e 8).
- Compare segredos em tempo constante (`hmac.compare_digest`).
- Carregue as chaves de um armazenamento protegido, nunca do código-fonte ou de arquivos legíveis por todos.
- Trate toda exceção no caminho de verificação como uma rejeição; nunca aceite por padrão.
- Limite o uso de recursos: tamanho máximo de mensagem, comprimento máximo de fila, limites de taxa por origem.
- Registre as rejeições em log com contexto suficiente para investigar, sem registrar segredos.

Essas regras vêm diretamente dos laboratórios 3, 8 e 11. Cada uma tem um teste no conjunto de testes do gateway.

### 28.3 A bancada de testes

Uma bancada de testes reproduz off-line o ambiente do controle: RTUs simuladas que enviam mensagens válidas, malformadas, forjadas, repetidas e atrasadas; um SCADA simulado que recebe a saída do gateway; e um relógio que você controla. O Laboratório 15 (Capítulo 40) é uma versão compacta. As bancadas permitem testar modos de falha que seriam inseguros ou impossíveis de provocar num sistema em operação. A bancada do TMRP inclui RTUs simuladas da PS2 e da PS4, um receptor SCADA simulado e um relógio controlável, para que reinícios, atrasos e repetições possam ser produzidos sob demanda. O mesmo arcabouço carrega depois a campanha de injeção de falhas com sementes, e é por isso que investir nele cedo poupa tempo quando começa a verificação do projeto final.

### 28.4 Evidências

Registre para cada implementação: as versões do requisito e da especificação implementadas; a revisão do código-fonte; os resultados dos testes, com as versões das ferramentas; as limitações conhecidas; e a aprovação do revisor. Isso passa a fazer parte do dossiê de evidências (Capítulo 48). Para o validador de setpoint do TMRP, o registro mostra a versão da especificação, os commits da v1 e da v2, os resultados do T3 para cada uma, a limitação conhecida de que a v1 aceitava NaN e o revisor que fez a pergunta sobre o NaN. Sem esse registro, a constatação posterior do dossiê sobre a situação do T3 teria sido impossível de resolver, porque ninguém conseguiria mostrar qual versão tinha sido aprovada. Registrar as evidências enquanto o trabalho é feito custa minutos; reconstruí-las depois custa dias.

### 28.5 Exemplo resolvido: validador de setpoint v1 (sintético)

A equipe do TMRP implementa R3 a partir da especificação da §27.5. A versão 1 verifica `new < lo`, `new > hi` e o limite de passo, e passa nos testes de exemplo: dentro da faixa, aceito; acima e abaixo da faixa, rejeitado; passo grande demais, rejeitado. A revisão de código pergunta: e o NaN? Na aritmética IEEE 754, toda comparação ordenada com NaN é falsa, então `nan < lo` e `nan > hi` são ambas falsas e `abs(nan - old) > max_step` é falsa — a v1 aceita NaN. A versão 2 rejeita explicitamente valores não finitos e expressa a região segura de forma positiva (`lo <= new <= hi`), o que é falso para NaN. Os testes baseados em propriedades do Capítulo 30 confirmam a diferença de forma sistemática (Laboratório 11). Essa é a reprovação do teste T3 no cenário de aprovação do Capítulo 10.

### 28.6 Atividade prática

Implemente um gateway mínimo que combine a saída do interpretador do Laboratório 3 com a selagem do Laboratório 8, de modo que uma leitura Modbus validada se torne um quadro autenticado. Escreva testes para cada caminho de rejeição. Mantenha as duas partes separadas por interfaces claras: o interpretador devolve uma leitura validada ou um motivo de rejeição, e apenas uma leitura validada é selada. Teste cada caminho de rejeição do Laboratório 3 e confirme que nada chega à função de selagem. Depois verifique se o quadro selado passa no receptor do Laboratório 8 e se uma cópia adulterada é recusada. Guarde a chave fora do arquivo-fonte, mesmo neste exercício, para que o hábito já esteja estabelecido antes que apareçam chaves reais.

### 28.7 Erros comuns e limites

- Código escrito antes que a especificação esteja clara.
- Comportamento de aceitar por padrão diante de exceções.
- Verificações negativas (`if x > hi: reject`) que deixam passar o NaN; prefira verificações positivas da região segura.
- Chaves no código-fonte.
- Evidências reconstruídas depois do fato.

A primeira versão do validador de setpoint mostra o terceiro erro, e o dossiê do TMRP existe para impedir o último. Sua aceitação do NaN veio das verificações negativas, e a correção foi declarar a região segura de forma positiva. As chaves no código da bancada do TMRP são carregadas de um arquivo protegido, nunca escritas no código-fonte, e toda exceção no caminho de verificação termina numa rejeição registrada em log.

### Exercícios — capítulo 28

**EX055 — O NaN e seus amigos.** *Objetivo:* encontrar aceitações inseguras. *Entradas:* `validate_v1` no Laboratório 11. *Passos:* avalie à mão a v1 e a v2 para `new` = NaN, +∞, −∞, 5.5 e 5.50001 com `old` = 5.2, e explique cada resultado. *Evidência esperada:* tabela. *Rubrica:* 3 = entre os valores especiais, a v1 só aceita NaN (∞ rejeitado por `> hi`, −∞ por `< lo`), 5.5 aceito pelas duas (limite inclusivo), 5.50001 rejeitado; a v2 rejeita todos os não finitos; explicações corretas; 2 = um erro; 1 = sem explicações; 0 = nada.

**EX056 — Registro das rejeições em log.** *Objetivo:* projetar logs úteis. *Entradas:* o gateway. *Passos:* defina um registro de log para cada tipo de rejeição (etiqueta, repetição, inatividade, formato, faixa), com os campos, e explique um campo que você exclui deliberadamente. *Evidência esperada:* esquema. *Rubrica:* 3 = os campos permitem a investigação (fonte de tempo, estação, contador, motivo, ID do gateway, hash da mensagem), exclui material de chaves e a carga útil completa onde for sensível; 2 = falta a fonte de tempo ou a estação; 1 = texto livre; 0 = nada.

### Síntese do capítulo

Implemente os controles a partir de especificações, com testes para cada "deverá". Codifique o caminho de controle de forma defensiva: valide por completo, compare em tempo constante, proteja as chaves, rejeite diante de qualquer erro, limite os recursos, registre em log de forma útil. Prefira verificações positivas da região segura. Teste numa bancada capaz de produzir as falhas que você não consegue provocar em operação e registre as evidências à medida que avança.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue estudando — capítulo 28 de 50

[← Capítulo 27](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Infraestrutura crítica e segurança setorial: medição

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) definir métricas de segurança e resiliência que apoiem decisões; (2) calcular métricas de detecção — precisão, revocação, F1, taxa de alarmes falsos, tempo até a detecção — a partir de testes rotulados; (3) medir a resiliência como o desempenho do serviço ao longo do tempo durante uma perturbação; e (4) evitar métricas que recompensam o comportamento errado. Ele se apoia nos capítulos 7 e 28 e prepara os capítulos 30, 38 e 40.

### 29.1 O que medir

Uma métrica é útil se muda uma decisão. Há três famílias: **desempenho dos controles** (o controle faz o que foi especificado: taxas de rejeição, tempos de detecção); **exposição** (quanta superfície de ataque ou vulnerabilidade existe: condutos não autenticados, vulnerabilidades alcançáveis sem patch, contas compartilhadas); e **resiliência do serviço** (como o serviço se degrada e se recupera). Use a abordagem objetivo–pergunta–métrica: declare o objetivo, a pergunta que mostraria o progresso e só então a métrica. Para o TMRP, a latência de alarme de R7 mede o desempenho dos controles, a contagem de condutos não autenticados mede a exposição e a fração da demanda atendida durante o ensaio de recuperação mede a resiliência.

### 29.2 Métricas de detecção

A partir de um conjunto de teste rotulado: verdadeiros positivos (VP), falsos positivos (FP), falsos negativos (FN), verdadeiros negativos (VN). **Precisão** = VP/(VP+FP): dos alarmes, quantos eram reais. **Revocação** = VP/(VP+FN): dos eventos reais, quantos foram encontrados. **F1** é a média harmônica das duas. Informe a precisão e a revocação junto com a taxa-base do conjunto de teste; a precisão num conjunto de teste com 50% de ataques diz pouco sobre uma operação com 0,1% (Capítulo 7). O **tempo até a detecção** é uma distribuição; informe a mediana e os piores casos, não apenas a média. [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) listam armadilhas comuns na avaliação de sistemas de segurança baseados em aprendizado de máquina, incluindo taxas-base irreais e contaminação de dados (data snooping); [Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) mostram como a avaliação com ajuste de pontos pode inflar as pontuações da detecção de anomalias em séries temporais.

### 29.3 A resiliência como desempenho ao longo do tempo

Trace o desempenho do serviço $Q(t)$ — para a LRWA, a fração da demanda atendida — durante uma perturbação. [Bruneau et al. (2003)](https://doi.org/10.1193/1.1623497) propuseram medir a perda de resiliência como a área entre o desempenho pleno e $Q(t)$, da perturbação até a recuperação. A curva mostra a robustez (quanto o desempenho cai), a rapidez (com que velocidade ele se recupera) e a perda total. Os requisitos de engenharia se projetam sobre ela: R4 mantém a queda rasa; R6 encurta a recuperação. O ensaio de recuperação do TMRP fornece uma curva real, já que o abastecimento ficou em modo local enquanto a operação remota era restaurada.

### 29.4 Métricas que enganam

Contar ataques bloqueados recompensa firewalls ruidosos; contar patches aplicados ignora quais deles importavam; o tempo médio até a detecção esconde o único evento detectado depois de três semanas. Quando uma métrica se torna uma meta, as pessoas otimizam a métrica. Prefira métricas ligadas às consequências e verificadas por teste. O teste de aceitação do detector do TMRP evita isso informando as falhas de detecção e a detecção mais lenta, e não apenas uma média. Os dois eventos de reconhecimento não detectados permanecem no relatório, porque são o resultado que muda o quanto a LRWA pode confiar no detector.

### 29.5 Exemplo resolvido: teste de aceitação de um detector de anomalias (sintético)

O teste de aceitação do TMRP para um detector de anomalias de rede usa 14 eventos rotulados de uma semana de teste na bancada (Laboratório 10): 7 maliciosos (inundações de escrita, códigos de função não autorizados, uma nova conexão de engenharia) e 7 benignos (manutenção, backup de firmware, um failover). Resultados: precisão 0,625, revocação 0,714, F1 0,667; tempo até a detecção dos eventos detectados de 2 a 30 minutos, mediana 7. Os dois ataques não detectados eram ambos reconhecimentos lentos e de baixo volume. A decisão de aceitação: implantar para a detecção de ataques de alto volume, não confiar nele para o reconhecimento, e registrar que a taxa-base de 50% do conjunto de teste torna a precisão operacional muito menor.

### 29.6 Atividade prática: Laboratório 10

```python
# Lab 10 - detection metrics and time-to-detect from a labelled synthetic test week (offline)
# (event_id, truly_malicious, alerted, minutes_from_start_to_alert or None)
EV = [(1,1,1,4),(2,1,1,11),(3,1,0,None),(4,0,1,None),(5,0,0,None),(6,1,1,2),(7,0,1,None),
      (8,0,0,None),(9,1,1,30),(10,0,0,None),(11,0,0,None),(12,1,0,None),(13,0,1,None),(14,1,1,7)]
tp = sum(1 for e in EV if e[1] and e[2]); fp = sum(1 for e in EV if not e[1] and e[2])
fn = sum(1 for e in EV if e[1] and not e[2]); tn = sum(1 for e in EV if not e[1] and not e[2])
prec, rec = tp / (tp + fp), tp / (tp + fn)
print(f"TP={tp} FP={fp} FN={fn} TN={tn} precision={prec:.3f} recall={rec:.3f} F1={2*prec*rec/(prec+rec):.3f}")
ttd = sorted(e[3] for e in EV if e[1] and e[2])
print("time to detect (min):", ttd, "mean", round(sum(ttd)/len(ttd), 1), "median", ttd[len(ttd)//2])
```

Saída esperada:

```text
TP=5 FP=3 FN=2 TN=4 precision=0.625 recall=0.714 F1=0.667
time to detect (min): [2, 4, 7, 11, 30] mean 10.8 median 7
```

As contagens coincidem com o exemplo resolvido: cinco ataques detectados, três eventos benignos alarmados, dois ataques não detectados e quatro eventos benignos deixados em silêncio. Os dois ataques não detectados eram reconhecimentos lentos e de baixo volume, que o detector não enxerga. Os tempos de detecção mostram por que a mediana importa: um evento levou trinta minutos, enquanto a maioria foi encontrada em menos de dez. Como metade dos eventos de teste era maliciosa, a precisão aqui é muito maior do que a LRWA veria em operação, como mostra o EX057.

### 29.7 Erros comuns e limites

- Métricas que ninguém usa para uma decisão.
- Precisão de conjuntos de teste balanceados informada como se fosse operacional.
- Tempo médio até a detecção sem distribuição nem falhas de detecção.
- Resiliência informada apenas como disponibilidade (uptime).
- Métricas que se tornam metas.

O teste de aceitação do TMRP informa as falhas de detecção e a detecção mais lenta, e sua precisão é declarada com a taxa-base de cinquenta por cento do conjunto de teste, para que ninguém a confunda com a precisão operacional. A resiliência é mostrada como a fração da demanda atendida ao longo do tempo, e não como disponibilidade. Cada métrica nele informa a decisão de implantação.

### Exercícios — capítulo 29

**EX057 — Precisão operacional.** *Objetivo:* traduzir as métricas de teste para a operação. *Entradas:* revocação de 0,714 do Laboratório 10 e taxa de FP no teste de 3/7; taxa-base operacional de 1 evento malicioso a cada 1.000 eventos. *Passos:* calcule a precisão operacional e os alarmes falsos esperados a cada 1.000 eventos; interprete. *Evidência esperada:* números e interpretação. *Rubrica:* 3 = cálculo correto (precisão ≈ 0,0017; ≈ 428 alarmes falsos a cada 1.000 eventos), interpretação de que a estimativa de FP a partir de 7 eventos benignos é incerta demais e de que o detector é inutilizável sem uma TFP muito menor; 2 = números certos; 1 = fórmula errada; 0 = nada.

**EX058 — Curva de resiliência.** *Objetivo:* calcular a perda de resiliência. *Entradas:* $Q(t)$ sintético: 100% até t = 0; 60% de 0 a 4 h; recuperação linear até 100% de 4 h a 12 h. *Passos:* calcule a área de perda em %·h; recalcule se o modo manual local (R4) mantiver $Q$ em 85% de 0 a 4 h. *Evidência esperada:* dois números e uma frase. *Rubrica:* 3 = 160+160 = 320 %·h e 60+60 = 120 %·h, com interpretação clara; 2 = um erro; 1 = apenas o método; 0 = nada.

### Síntese do capítulo

Meça o que muda decisões: o desempenho dos controles, a exposição e a resiliência do serviço. Informe a precisão e a revocação com as taxas-base, e as distribuições do tempo até a detecção incluindo as falhas de detecção. Represente a resiliência como desempenho ao longo do tempo. Desconfie de métricas que podem ser manipuladas ou que escondem o pior caso.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue estudando — capítulo 29 de 50

[← Capítulo 28](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) planejar e executar uma campanha de verificação de controles de segurança com critérios definidos de aprovação e reprovação; (2) usar testes baseados em exemplos, de limites, negativos e baseados em propriedades; (3) registrar os resultados para que outro engenheiro possa reproduzi-los; e (4) tratar testes reprovados com honestidade, incluindo o novo teste depois das correções. Ele verifica a implementação do Capítulo 28 e prepara o Capítulo 38 (validação) e o Capítulo 40 (Laboratório de verificação II).

### 30.1 A verificação como campanha

A verificação responde: a implementação atende à sua especificação? Um plano de campanha lista, para cada requisito, os casos de teste, o ambiente, as entradas, o procedimento, o resultado esperado, o critério de aprovação e quem o executa. Os testes são escritos antes da execução e não são alterados para fazer os resultados passarem. Os resultados incluem detalhes do ambiente (versões de software, sementes, configuração) para que o teste possa ser repetido. O plano de campanha do TMRP lista T1 a T7 contra R1 a R8, com critérios de aprovação fixados antes da execução de qualquer teste; R9 ainda não tem teste atribuído, o que o mapa de evidências expõe depois. Cada teste nomeia seu ambiente e quem o executa.

### 30.2 Tipos de teste

- **Testes de exemplo** verificam o comportamento típico.
- **Testes de limites** verificam as bordas: exatamente nos limites, logo dentro, logo fora.
- **Testes negativos** verificam que entradas inválidas são rejeitadas: malformadas, forjadas, repetidas, fora da faixa.
- **Testes baseados em propriedades** declaram uma propriedade que precisa valer para todas as entradas ("nenhum setpoint inseguro é jamais aceito") e a verificam em muitas entradas geradas, incluindo valores especiais. Eles encontram casos que ninguém pensou em escrever.
- **Testes de injeção de falhas** (Capítulo 40) perturbam o ambiente: descartam, atrasam ou corrompem mensagens; reiniciam componentes.

Os testes de exemplo mostram a presença do comportamento correto nos casos escolhidos; os testes baseados em propriedades e de injeção de falhas buscam de forma mais ampla a ausência de comportamento incorreto. Nenhum deles prova a correção para todas as entradas, exceto em domínios finitos pequenos (Capítulo 2).

### 30.3 Reprodutibilidade

Defina a semente de todo gerador aleatório e imprima-a; registre as versões das ferramentas e bibliotecas; guarde as entradas de teste; armazene os resultados com a revisão do código-fonte. Um teste reprovado que não pode ser reproduzido não pode ser corrigido nem verificado de novo. O registro do T3 do TMRP segue essa regra: ele informa a semente, o número de casos gerados e a versão do Python, para que qualquer pessoa possa executar de novo o teste baseado em propriedades e ver as mesmas trinta e uma aceitações de NaN na v1 e nenhuma na v2. Sem a semente, um revisor só poderia aceitar o resultado na confiança. O mesmo registro armazena a revisão do código-fonte de cada versão do validador.

### 30.4 Testes reprovados

Um teste reprovado é informação. Registre-o como reprovado, com evidências; analise a causa raiz; corrija; execute de novo o teste reprovado e o conjunto de regressão; registre o novo teste. Nunca rotule de novo uma reprovação como "não aplicável" porque o prazo está próximo (Capítulo 10). Se uma reprovação for aceita temporariamente, ela precisa de um controle compensatório, um dono e uma data. O T3 é o modelo: reprovado na v1, corrigido na v2, testado de novo e registrado. A reprovação da v1 nunca foi rotulada de novo, e o controle compensatório da PS4 tinha um dono e uma data.

### 30.5 Exemplo resolvido: T3, limites de setpoint (sintético)

O teste T3 verifica R3. Os testes de exemplo na v1 (dentro da faixa, acima, abaixo, passo grande) são aprovados. O teste baseado em propriedades gera 2.000 casos com a semente 30, um em cada dez sorteado entre valores especiais (NaN, ±∞, limites exatos). A v1 aceita 31 valores inseguros — todos NaN. A v2 não aceita nenhum. O T3 é registrado como **reprovado na v1**, com causa raiz "comparações negativas são falsas para NaN", corrigido na v2, testado de novo e **aprovado na v2**, com a semente e a versão do Python registradas. Os dois resultados permanecem no registro. O resultado do novo teste é depois lançado na matriz de rastreabilidade.

### 30.6 Atividade prática: Laboratório 11

```python
# Lab 11 - property-based testing of a setpoint validator finds what example tests missed (offline)
import random, math
def validate_v1(new, old, lo=0.5, hi=5.5, max_step=0.5):
    if new < lo: return False
    if new > hi: return False
    if abs(new - old) > max_step: return False
    return True
def validate_v2(new, old, lo=0.5, hi=5.5, max_step=0.5):
    if not (isinstance(new, float) and math.isfinite(new)): return False
    return lo <= new <= hi and abs(new - old) <= max_step
examples = [(3.0, 3.2), (6.0, 5.8), (0.2, 0.6), (4.0, 3.0)]
print("example tests v1:", [validate_v1(n, o) for n, o in examples])
rng = random.Random(30)
specials = [float("nan"), float("inf"), -float("inf"), 5.5, 0.5]
def prop(f, trials=2000):
    fails = []
    for i in range(trials):
        old = rng.uniform(0.5, 5.5)
        new = rng.choice(specials) if i % 10 == 0 else rng.uniform(-1, 7)
        ok = f(new, old)
        safe = math.isfinite(new) and 0.5 <= new <= 5.5 and abs(new - old) <= 0.5
        if ok and not safe: fails.append(new)
    return fails
f1 = prop(validate_v1); f2 = prop(validate_v2)
print("v1 unsafe acceptances:", len(f1), "first:", f1[:1])
print("v2 unsafe acceptances:", len(f2))
```

Saída esperada:

```text
example tests v1: [True, False, False, False]
v1 unsafe acceptances: 31 first: [nan]
v2 unsafe acceptances: 0
```

Os testes de exemplo dão as mesmas respostas para os dois validadores, então não conseguem distinguir a v1 da v2. É a execução baseada em propriedades que os separa: a v1 aceita trinta e um valores inseguros, todos NaN, enquanto a v2 não aceita nenhum. A semente trinta torna a execução repetível. Observe que o gerador sorteia valores especiais apenas uma vez em cada dez; sem isso, o NaN quase nunca apareceria e o bug ficaria escondido por mais casos aleatórios que fossem tentados. Registre a semente junto com o resultado.

### 30.7 Erros comuns e limites

- Testes escritos depois de ver os resultados.
- Apenas testes de exemplo.
- Testes aleatórios sem semente; resultados sem versões.
- Reprovações rotuladas de novo em vez de corrigidas.
- Alegar que testes baseados em propriedades provam a correção.

O registro do T3 do TMRP evita cada um desses erros. Sua propriedade foi escrita antes da execução, seu gerador tem semente, a reprovação na v1 permaneceu registrada como reprovação, e o relatório alega apenas que nenhum valor inseguro foi encontrado entre os casos gerados, e não que a v2 está correta para todas as entradas. A semente e a versão ficam armazenadas com o resultado.

### Exercícios — capítulo 30

**EX059 — Conte as reprovações.** *Objetivo:* raciocinar sobre testes gerados. *Entradas:* Laboratório 11. *Passos:* (1) explique por que todas as 31 aceitações inseguras são NaN; (2) estime quantos casos NaN o gerador produziu (um em cada dez casos é um valor especial, escolhido uniformemente entre cinco) e compare com 31; (3) explique por que nem todo caso NaN é uma aceitação insegura na v1 — ou mostre que todo NaN é aceito. *Evidência esperada:* raciocínio e números. *Rubrica:* 3 = ≈ 200 casos especiais × 1/5 ≈ 40 NaN esperados, 31 observados, compatível com a variação aleatória, e todo NaN é aceito pela v1, então 31 é a contagem de NaN; 2 = parcial; 1 = sem números; 0 = nada.

**EX060 — Plano de verificação para R2.** *Objetivo:* planejar testes para a rejeição de repetições. *Entradas:* R2 e Laboratório 8. *Passos:* escreva um plano de teste com pelo menos seis casos (incluindo o reinício de cada lado, o estouro ou o máximo do contador, a entrega fora de ordem), resultados esperados e critérios de aprovação. *Evidência esperada:* tabela. *Rubrica:* 3 = os casos cobrem o reinício e a ordenação, resultados esperados coerentes com o projeto da §19.5, critérios inequívocos; 2 = reinício ausente; 1 = apenas o caminho feliz; 0 = nada.

### Síntese do capítulo

A verificação é uma campanha planejada, com critérios fixados com antecedência. Combine testes de exemplo, de limites, negativos, baseados em propriedades e de injeção de falhas; torne cada execução reprodutível; e trate as reprovações como informação a ser corrigida e verificada de novo, nunca rotulada de novo.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue estudando — capítulo 30 de 50

[← Capítulo 29](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Infraestrutura crítica e segurança setorial: implementação II

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) implantar controles em ambientes operacionais por meio de uma implantação em etapas com reversão; (2) gerenciar chaves, configuração e segredos em produção; (3) integrar equipamentos legados por meio de gateways e controles compensatórios; e (4) comissionar um controle com testes de aceitação e passagem aos operadores. Ele leva a implementação de bancada do Capítulo 28 para o campo e prepara os capítulos 32 a 34.

### 31.1 Implantação em etapas

A implantação em campo segue etapas, cada uma com critérios de entrada e saída: bancada (todos os testes aprovados); local piloto de baixa consequência; um local de alta consequência, com monitoramento extra e um plano de reversão; frota. Cada etapa tem uma **reversão** — a capacidade de voltar rapidamente ao estado anterior conhecido como bom — testada antes de ser necessária. Programe as mudanças fora dos picos de demanda e com os operadores informados; no setor de água, evite mudanças durante períodos de alta demanda ou quando o armazenamento estiver baixo. As etapas do TMRP são a bancada, a PS2 como piloto de baixa consequência, a PS4 como primeiro local de alta consequência e depois a frota.

### 31.2 Gestão de chaves e segredos em produção

Na bancada, as chaves são arquivos; em produção, são ciclos de vida. Gere as chaves em módulos de segurança de hardware ou nos elementos seguros dos dispositivos; cadastre os dispositivos numa cerimônia auditável (duas pessoas, registrada em log); armazene o inventário de qual chave pertence a qual dispositivo e sua data de rotação; faça a rotação; e revogue prontamente quando um dispositivo for perdido ou desativado. Os segredos das contas de serviço vão para um cofre com registro de acessos, e não para scripts. Um inventário de chaves é, ele próprio, sensível. No TMRP, as chaves são geradas no elemento seguro do gateway no cadastro.

### 31.3 Integração de legados

Dispositivos legados que não conseguem se autenticar são encapsulados: um gateway colocado fisicamente ao lado (no mesmo gabinete) acrescenta autenticação do lado da rede e fala o protocolo legado num enlace curto e fisicamente protegido. O gateway passa a fazer parte da fronteira de segurança do dispositivo, então precisa de seu próprio endurecimento, monitoramento e caminho de atualização. Controles compensatórios cobrem o que o gateway não consegue: alarmes de violação do gabinete, registro local em log e restrições sobre quais códigos de função passam. Na PS2, o gateway fica no gabinete da RTU, num enlace serial de 30 cm, e deixa passar apenas dois códigos de função.

### 31.4 Comissionamento e passagem aos operadores

O comissionamento verifica o sistema instalado em seu ambiente real: os testes de aceitação em campo repetem no local os principais testes de bancada (a autenticação rejeita quadros forjados; a repetição é rejeitada; o failover para o modo automático local funciona; os alarmes chegam à sala de controle em até 60 s). A passagem dá aos operadores procedimentos, treinamento, contatos e as limitações conhecidas. Até que os operadores consigam operar e recuperar o sistema, o controle não está em serviço. Na PS2, a aceitação em campo também encontrou a deriva do relógio do gateway, que foi corrigida e testada de novo antes da passagem. Os operadores foram treinados primeiro.

### 31.5 Exemplo resolvido: piloto da PS2 (sintético)

O local piloto do TMRP é a PS2 — RTU-A legada, baixa consequência. Critérios de entrada: T1, T2, T3 (v2) e T5 aprovados na bancada; imagem de reversão pronta; operadores informados. O gateway é instalado no gabinete da RTU; o enlace serial tem 30 cm dentro do gabinete trancado; o gateway deixa passar apenas os códigos de função 3 (leitura) e 6 (escrita de um único registrador) para a faixa de registradores configurada. Aceitação em campo: quadros forjados e repetidos rejeitados e alarmados; retirar a antena LTE resulta em operação automática local e num alarme de perda de comunicação em até 60 s; recolocar a antena retoma a telemetria com os contadores continuando. Uma constatação: o relógio do gateway derivou 40 s em 48 h porque o NTP não era alcançável pelo novo conduto; corrigido acrescentando uma fonte de tempo interna à lista de permissões do conduto. Critérios de saída atendidos após o novo teste; a PS4 é a próxima.

### 31.6 Atividade prática

Escreva o plano de etapas para a implantação do TMRP na frota, com critérios de entrada e saída e reversão para cada etapa, e uma nota de passagem de duas páginas para os operadores do gateway. Use o piloto da PS2 como modelo para os critérios de entrada e saída e depois estenda o plano à PS4 e às demais estações. Para cada etapa, diga como a reversão é feita e quem decide usá-la. Na nota de passagem, informe aos operadores os alarmes que o gateway gera, o que cada um significa, como passar para a operação manual local e a quem chamar. Liste com franqueza as limitações conhecidas, como a dependência de uma fonte de tempo interna aprendida na PS2.

### 31.7 Erros comuns e limites

- Implantação "big bang", sem piloto nem reversão.
- Planos de reversão nunca testados.
- Cadastro de chaves por uma única pessoa, sem registros.
- Gateways tratados como transparentes, e não como dispositivos críticos para a segurança.
- Comissionamento sem os operadores; passagem sem as limitações conhecidas.

O piloto da PS2 do TMRP evitou esses erros: tinha uma imagem de reversão, os operadores foram informados antes da instalação, e a constatação da deriva do relógio foi tratada como uma correção de interface e testada de novo antes do início da PS4. O cadastro de chaves segue a cerimônia de duas pessoas, registrada em log, descrita acima, e o gateway foi tratado como um dispositivo crítico para a segurança, com seu próprio endurecimento e caminho de atualização.

### Exercícios — capítulo 31

**EX061 — Critérios de reversão.** *Objetivo:* definir quando reverter. *Entradas:* implantação na PS4. *Passos:* defina três gatilhos de reversão mensuráveis, quem decide e o tempo máximo para concluir a reversão. *Evidência esperada:* lista. *Rubrica:* 3 = gatilhos mensuráveis (p. ex., perda de telemetria > 5 min não explicada pela perda do enlace, qualquer mensagem aceita que falhe na auditoria, latência de alarme > 60 s para alarmes prioritários), dono da decisão nomeado pelo papel, tempo de reversão coerente com a reserva do hospital; 2 = gatilhos vagos; 1 = sem dono; 0 = nada.

**EX062 — O gateway como fronteira.** *Objetivo:* proteger um encapsulador de legado. *Entradas:* o gateway da PS2. *Passos:* liste seis controles de que o próprio gateway precisa e o risco residual se um atacante obtiver acesso físico ao gabinete. *Evidência esperada:* lista e declaração do residual. *Rubrica:* 3 = endurecimento, atualizações assinadas, proteção das chaves, filtragem de códigos de função, detecção de violação, registro em log; residual honesto (um atacante físico pode contornar pelo enlace serial); 2 = residual ausente; 1 = genérico; 0 = nada.

### Síntese do capítulo

Implante em etapas, com critérios de entrada e saída e reversão testada. Gerencie chaves e segredos como ciclos de vida, com cerimônias auditáveis. Encapsule dispositivos legados com gateways que sejam, eles próprios, tratados como críticos para a segurança, mais controles físicos compensatórios. Um controle só está em serviço depois da aceitação em campo e da passagem aos operadores.

<!-- cyberabc:chapter-navigation:start ch-31 -->
### Continue estudando — capítulo 31 de 50

[← Capítulo 30](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Infraestrutura crítica e segurança setorial: confiabilidade

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) usar medidas de confiabilidade — taxa de falhas, MTBF, MTTR, disponibilidade; (2) calcular a disponibilidade de sistemas em série, em paralelo e redundantes reparáveis com modelos de Markov; (3) mostrar como a capacidade de reparo e as causas comuns mudam os benefícios da redundância; e (4) ligar a engenharia de confiabilidade à segurança, em que as falhas podem ser induzidas. Ele se apoia no Capítulo 7 e prepara os capítulos 33 e 41.

### 32.1 Medidas

Para um componente com taxa de falhas constante $\lambda$ (falhas por hora), o tempo médio entre falhas é $1/\lambda$. Com tempo médio de reparo $1/\mu$, a disponibilidade em regime permanente é $A = \mu/(\lambda+\mu) = \text{MTBF}/(\text{MTBF}+\text{MTTR})$. Taxas de falhas constantes servem para o período de vida útil dos eletrônicos; as falhas do início da vida e as de desgaste precisam de outras distribuições (Weibull). Componentes em **série** (todos necessários) têm taxas que se somam: $\lambda_s = \sum\lambda_i$. Componentes em **paralelo** (basta qualquer um) só falham juntos. Na PS4, a taxa de falhas de cada bomba, de uma a cada duas mil horas, e seu tempo de reparo de 24 horas dão a disponibilidade de uma bomba usada no Laboratório 12.

### 32.2 Redundância reparável

As fórmulas simples para sistemas em paralelo pressupõem unidades independentes, cada uma reparada de forma independente. Locais reais muitas vezes têm uma única equipe de reparo, então, quando as duas unidades estão paradas, uma espera. Uma cadeia de Markov de tempo contínuo modela isso: estados 0, 1 e 2 unidades com falha; transições à taxa $2\lambda$ de 0 para 1, $\lambda$ de 1 para 2, e $\mu$ de volta a partir de 1 e de 2, com uma equipe. Resolver as equações de equilíbrio dá as probabilidades em regime permanente; a indisponibilidade é a probabilidade do estado 2. A PS4 tem exatamente essa restrição: duas bombas, uma equipe de reparo. O modelo de Markov do Laboratório 12 captura a espera.

### 32.3 Falhas induzidas

Os modelos de confiabilidade pressupõem que as falhas chegam aleatoriamente. Um adversário escolhe quando. Se um atacante consegue desativar uma bomba remotamente e esperar que a outra falhe — ou desativar as duas —, os números de Markov deixam de descrever o risco. A engenharia de confiabilidade continua importando para a segurança: ela informa a **linha de base** que o atacante precisa superar, a **capacidade de reparo** que determina a velocidade de recuperação e os estoques de reserva que tornam real a reserva fria. Os requisitos de segurança visam então fazer com que falhas induzidas exijam comprometimentos independentes (o condicionamento do Capítulo 23).

### 32.4 Exemplo resolvido: bombas principal/reserva da PS4 (sintético)

Cada bomba da PS4 tem taxa de falhas de 1 a cada 2.000 h e tempo médio de reparo de 24 h, com uma equipe. O Laboratório 12 dá uma disponibilidade de uma bomba de 0.98814 (cerca de 104 h paradas por ano). O par 1-de-2 com uma equipe tem disponibilidade de 0.999719 — as duas bombas paradas cerca de 148 minutos por ano. A fórmula ingênua $1-(1-A)^2$ dá 0.999859, metade da indisponibilidade real, porque ignora que a segunda falha pode ocorrer enquanto a única equipe está ocupada. Para a cadeia de controle do conjunto de bombas — bomba, partida e RTU em série, com MTBFs de 2.000, 5.000 e 10.000 h —, o MTBF da série é de 1.250 h: a cadeia é menos confiável do que seu elemento mais fraco.

### 32.5 Atividade prática: Laboratório 12

```python
# Lab 12 - availability of a duplicated pump set with repair (two-state units, one repair crew; offline)
lam, mu = 1 / 2000, 1 / 24     # failures per hour per pump, repairs per hour
A1 = mu / (lam + mu)
# states: 0 = both up, 1 = one down, 2 = both down; one crew repairs one pump at a time
# balance: p1 = (2 lam / mu) p0 ; p2 = (lam / mu) p1
p0 = 1 / (1 + 2 * lam / mu + 2 * (lam / mu) ** 2)
p1 = 2 * lam / mu * p0; p2 = lam / mu * p1
print(f"single pump availability {A1:.6f}  downtime h/yr {8760*(1-A1):.1f}")
print(f"1oo2 availability {1-p2:.8f}  P(both down) {p2:.2e}  downtime min/yr {8760*60*p2:.2f}")
print(f"naive independent 1-(1-A1)^2 = {1-(1-A1)**2:.8f}")
mtbf_series = 1 / (1/2000 + 1/5000 + 1/10000)
print(f"series MTBF pump+starter+RTU: {mtbf_series:.0f} h")
```

Saída esperada:

```text
single pump availability 0.988142  downtime h/yr 103.9
1oo2 availability 0.99971883  P(both down) 2.81e-04  downtime min/yr 147.78
naive independent 1-(1-A1)^2 = 0.99985939
series MTBF pump+starter+RTU: 1250 h
```

Uma bomba fica parada cerca de 104 horas por ano. O par com uma equipe fica parado ao mesmo tempo por cerca de 148 minutos por ano, aproximadamente o dobro do que sugere a fórmula ingênua, porque a segunda falha pode chegar enquanto a equipe ainda está reparando a primeira. O valor da série mostra a fraqueza da cadeia de controle: bomba, partida e RTU juntas têm um tempo médio entre falhas de 1.250 horas, menor do que o de qualquer uma delas sozinha. É a capacidade de reparo, e não a qualidade das bombas, que produz a diferença.

### 32.6 Erros comuns e limites

- Fórmulas de reparo independente com uma única equipe.
- Taxas de falhas constantes para equipamentos envelhecidos.
- Ignorar causas comuns (painel de partida compartilhado, energia compartilhada).
- Números de confiabilidade apresentados como proteção contra ataques deliberados.
- Valores de MTBF de fornecedores usados sem conhecer suas condições de teste.

Para a PS4, o primeiro erro reduz à metade o tempo de parada previsto, e o terceiro ignora que as duas bombas compartilham um painel de partida e um alimentador. Os valores de MTBF do fornecedor para a RTU devem ser conferidos com os próprios registros de manutenção da LRWA antes de entrarem no dossiê, e nenhum desses números diz nada sobre um atacante que pare as duas bombas deliberadamente.

### Exercícios — capítulo 32

**EX063 — Duas equipes.** *Objetivo:* modelar a capacidade de reparo. *Entradas:* Laboratório 12. *Passos:* modifique o modelo de Markov para duas equipes independentes (taxa de reparo $2\mu$ a partir do estado 2) e calcule a indisponibilidade; compare com uma equipe e com a fórmula ingênua. *Evidência esperada:* números e conclusão. *Rubrica:* 3 = o resultado com duas equipes coincide com a fórmula ingênua independente (explique por quê), uma equipe aproximadamente o dobro; 2 = números certos, sem explicação; 1 = não executado; 0 = nada.

**EX064 — Decisão sobre reservas.** *Objetivo:* ligar a confiabilidade à logística. *Entradas:* o tempo de reparo de 24 h pressupõe uma bomba reserva em estoque; sem reserva, o reparo leva 21 dias (504 h). *Passos:* calcule a indisponibilidade 1oo2 com uma equipe e MTTR de 504 h, e recomende se convém manter uma reserva. *Evidência esperada:* número e recomendação. *Rubrica:* 3 = cálculo correto (use a fórmula do laboratório com μ = 1/504), recomendação ligada à consequência para o hospital; 2 = número certo; 1 = taxa errada; 0 = nada.

### Síntese do capítulo

A confiabilidade é medida com taxas de falhas, tempos de reparo e disponibilidade; cadeias em série são mais fracas do que seu elo mais fraco; a redundância reparável depende da capacidade de reparo, que as fórmulas simples ignoram. Os adversários induzem falhas no cronograma deles, então a confiabilidade fornece a linha de base e a capacidade de recuperação, enquanto a segurança precisa fazer com que falhas induzidas exijam comprometimentos independentes.

<!-- cyberabc:chapter-navigation:start ch-32 -->
### Continue estudando — capítulo 32 de 50

[← Capítulo 31](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Infraestrutura crítica e segurança setorial: segurança operacional e resiliência

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) aplicar a Análise de Processos Teórica de Sistemas (STPA) a uma estrutura de controle, incluindo causas relacionadas à segurança da informação; (2) descrever os sistemas instrumentados de segurança e por que eles precisam de independência; (3) definir e projetar a resiliência — antecipar, resistir, recuperar-se, adaptar-se; e (4) integrar segurança operacional, segurança da informação e resiliência numa única análise. Ele se apoia nos capítulos 10, 17, 23 e 32 e prepara os capítulos 34 e 47.

### 33.1 STPA

[Leveson (2004)](https://doi.org/10.1016/S0925-7535(03)00047-X) propôs o STAMP, um modelo de acidentes que trata a segurança operacional como um problema de controle: os acidentes surgem quando as restrições sobre o comportamento do sistema não são impostas. A STPA, o método de análise construído sobre ele, procede assim: (1) definir perdas e perigos; (2) modelar a estrutura de controle — controladores, ações de controle, realimentação; (3) identificar **ações de controle inseguras** (UCAs) de quatro tipos: não fornecida quando necessária, fornecida quando insegura, fornecida cedo/tarde demais ou na ordem errada, interrompida cedo demais ou aplicada por tempo demais; (4) identificar cenários de perda — por que cada UCA poderia ocorrer, incluindo realimentação falha, modelos de processo falhos e, para a segurança da informação (STPA-Sec), a ação de um adversário. A força da STPA é encontrar perigos que surgem de interações em que nenhum componente falhou — exatamente a situação de um ataque de dados falsos.

### 33.2 Sistemas instrumentados de segurança e independência

Um sistema instrumentado de segurança (SIS) leva um processo a um estado seguro quando uma condição perigosa é detectada, de forma independente do sistema básico de controle do processo. As normas de segurança funcional (IEC 61508 e suas derivadas setoriais) atribuem níveis de integridade de segurança. Independência significa sensores, lógica e elementos finais separados e, em termos modernos, redes e acesso de engenharia separados, porque uma estação de engenharia comprometida que consiga reprogramar tanto a lógica de controle quanto a de segurança elimina a independência. O TRITON visou diretamente controladores de SIS ([relatório HatMan da CISA](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)).

### 33.3 Resiliência

A [NIST SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1) estrutura a ciber-resiliência em torno dos objetivos de antecipar, resistir, recuperar-se e adaptar-se, com técnicas como diversidade, segmentação, redundância, não persistência e resposta adaptativa. [Haimes (2009)](https://doi.org/10.1111/j.1539-6924.2009.01216.x) argumenta que a resiliência precisa ser definida em relação a ameaças e estados do sistema específicos. Projetar a resiliência significa: projetar modos degradados (Capítulo 22), manter capacidade e reservas (armazenamento, baterias, peças de reposição), tornar a recuperação rápida e praticada (Capítulo 47) e aprender depois dos eventos. Para a LRWA, o tanque do hospital, as baterias dos gabinetes e as 72 horas de operação automática local são reservas; o ensaio de recuperação é a prática.

### 33.4 Exemplo resolvido: STPA no controle de nível de Hollin Hill (sintético)

Perda L1: hospital sem água; L2: transbordamento do reservatório e inundação. Perigos: H1 nível abaixo do mínimo enquanto a demanda continua; H2 nível acima do transbordamento. Estrutura de controle: operador do SCADA → controlador PI (velocidade da bomba da PS3) → bomba → reservatório; realimentação pelo transmissor de nível. UCAs: UCA1 "o controlador reduz a vazão de entrada quando o nível está baixo" (fornecida quando insegura → H1); UCA2 "o operador não intervém quando o nível cai" (não fornecida → H1); UCA3 "o controlador aumenta a vazão de entrada quando o nível está alto" (→ H2). Cenário para a UCA1: o modelo de processo do controlador acredita que o nível está alto porque a realimentação de nível foi falsificada (Laboratório 7). Cenário para a UCA2: a tela do operador mostra o mesmo nível falsificado. Restrições: medição de nível independente com alarme (EX034); desligamento da bomba por nível alto, com fiação dedicada, para H2; alarme de nível baixo ao operador a partir da medição independente. A STPA chegou ao mesmo controle que o detector de resíduos, mas partindo do perigo, e não do ataque.

### 33.5 Atividade prática

Estenda a §33.4 com a malha de dosagem: perdas, perigos, estrutura de controle, pelo menos quatro UCAs (uma de cada tipo) e um cenário de perda para cada, um deles adversarial. Comece com perdas como danos aos consumidores por superdosagem ou subdosagem, e perigos como o cloro residual fora de seus limites. Desenhe a estrutura de controle: o operador, o controlador de dosagem, a bomba dosadora e o analisador que realimenta o residual. Use os limites no lado do controlador e o alarme do analisador independente dos controles de dosagem do TMRP ao derivar as restrições, e faça do seu cenário adversarial um em que a realimentação do controlador é falsificada.

### 33.6 Erros comuns e limites

- Análise de perigos que ignora adversários, ou análise de segurança da informação que ignora perigos.
- "Independência" do SIS com estação de engenharia ou rede compartilhada.
- Resiliência definida como "uptime".
- STPA reduzida a uma checklist sem estrutura de controle.

O EX066 mostra o segundo erro em Fenwick, onde o sistema de desligamento por vazamento de gás cloro compartilha a estação de engenharia e o switch de rede com os controladores de processo. A análise de Hollin Hill do TMRP evita o primeiro erro incluindo a realimentação de nível falsificada como cenário de perda ao lado das falhas aleatórias, e trata a resiliência como serviço entregue ao longo do tempo, e não como uptime dos servidores.

### Exercícios — capítulo 33

**EX065 — Tabela de UCAs.** *Objetivo:* identificar ações de controle inseguras. *Entradas:* §33.5. *Passos:* produza a tabela de UCAs com os quatro tipos e os cenários. *Evidência esperada:* tabela. *Rubrica:* 3 = quatro tipos corretamente aplicados, cenários incluem realimentação falha e ação de adversário, restrições derivadas; 2 = tipos confundidos; 1 = lista de falhas, e não de ações de controle; 0 = nada.

**EX066 — Auditoria de independência.** *Objetivo:* testar a independência do SIS. *Entradas:* o sistema de desligamento por vazamento de gás cloro de Fenwick compartilha a estação de engenharia e o switch de rede com os controladores de processo. *Passos:* identifique as violações de independência e proponha uma arquitetura que restaure a independência, com os riscos residuais. *Evidência esperada:* meia página. *Rubrica:* 3 = estação e switch compartilhados identificados, acesso de engenharia separado com chave física ou estação separada, rede separada ou fiação dedicada, residual declarado; 2 = uma violação não percebida; 1 = genérico; 0 = nada.

### Síntese do capítulo

A STPA trata as perdas como falhas de controle e encontra ações de controle inseguras que surgem de interações, incluindo as adversariais. Os sistemas instrumentados de segurança precisam ser independentes em sensores, lógica, redes e acesso de engenharia. A resiliência — antecipar, resistir, recuperar-se, adaptar-se — precisa ser definida diante de ameaças específicas e projetada por meio de modos degradados, reservas e recuperação praticada.

<!-- cyberabc:chapter-navigation:start ch-33 -->
### Continue estudando — capítulo 33 de 50

[← Capítulo 32](#ch-32) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Infraestrutura crítica e segurança setorial: integração

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) planejar a integração de sistemas de forma incremental, com testes de interface; (2) integrar os controles de segurança às operações — alarmes, procedimentos, monitoramento e resposta a incidentes; (3) gerenciar interfaces organizacionais com fornecedores, operadoras e outras concessionárias; e (4) reconhecer comportamentos emergentes que só aparecem quando os componentes se combinam. Ele vem depois dos capítulos 31 a 33 e prepara o Ateliê de projeto II (Capítulo 35).

### 34.1 Integração incremental

Integre em pequenos incrementos, com testes de interface a cada passo: gateway com RTU; gateway com SCADA; SCADA com a réplica do historiador; sensores de monitoramento com o coletor de logs. Cada passo usa o documento de controle de interface (Capítulo 16) como sua especificação de teste. Quando um teste de integração falha, a especificação da interface diz qual lado está errado — ou revela que a especificação era ambígua. A ordem do TMRP segue os documentos de controle de interface: primeiro o gateway com a RTU na PS2, depois o gateway com o SCADA, depois a réplica na DMZ.

### 34.2 Comportamento emergente

Combinar componentes corretos pode produzir sistemas incorretos. Exemplos: um gateway de autenticação que armazena mensagens durante a perda do enlace e depois libera uma rajada na reconexão, inundando o poller do SCADA; o failover do par SCADA que zera os contadores contra repetição; um detector de anomalias que sinaliza cada retransmissão do gateway como um ataque. Os testes de integração precisam incluir cenários do sistema inteiro — perda e recuperação do enlace, failover, modo de manutenção —, e não apenas a conformidade das interfaces. O TMRP encontrou o primeiro exemplo nos testes de integração, como descreve o exemplo resolvido abaixo. Cada um precisa de um teste de cenário.

### 34.3 Integração com as operações

Um controle não está integrado até que as operações consigam usá-lo: alarmes com significado, prioridade e procedimentos de resposta claros; painéis que mostram o estado de segurança ao lado do estado do processo; playbooks que ligam os alarmes de segurança às decisões operacionais (passar para o manual local? chamar o gerente de plantão?); e treinamento. A prática de gestão de alarmes — racionalizar os alarmes para que cada um exija uma ação do operador — importa porque inundações de alarmes sem sentido escondem os reais. Na LRWA, o playbook para uma mudança inesperada de setpoint é o modo como os alarmes do gateway chegam às decisões operacionais. Cada novo alarme é racionalizado antes da liberação.

### 34.4 Interfaces organizacionais

A segurança da infraestrutura depende de organizações que você não controla: a operadora LTE, o fornecedor das RTUs, o integrador, a distribuidora de eletricidade, as concessionárias vizinhas para ajuda mútua. Torne as interfaces explícitas em contratos e acordos: deveres de notificação de incidentes e vulnerabilidades, condições de acesso, tempos de resposta do suporte e exercícios conjuntos. Um incidente na operadora também é um incidente seu. Para a LRWA, a operadora LTE é o exemplo mais claro, já que todo o conduto de campo do TMRP passa pela rede dela. O contrato deve fixar tempos de notificação e exercícios conjuntos com termos mensuráveis.

### 34.5 Exemplo resolvido: a rajada de reconexão (sintético)

Durante os testes de integração, a equipe desconecta a central LTE por 30 minutos. Na reconexão, cada um dos 42 gateways libera de uma vez 180 leituras armazenadas. O front-end do SCADA, dimensionado para o regime permanente, enfileira a rajada; os alarmes prioritários atrasam mais de dois minutos, violando R7. O modelo de filas do Laboratório 13 explica por quê: uma utilização acima de 0,9 faz o atraso explodir. Correção: os gateways encaminham imediatamente apenas o valor mais recente e quaisquer alarmes, e depois preenchem o histórico a uma taxa limitada no historiador, e não no poller do SCADA. A correção é registrada como uma mudança de interface (revisão do ICD) e um teste de regressão.

### 34.6 Atividade prática

Projete um teste de integração que combine o failover do SCADA com a proteção contra repetição, declarando o comportamento esperado, as observações e o critério de aprovação. Descreva a sequência: um servidor SCADA faz failover para seu parceiro enquanto os gateways continuam enviando mensagens autenticadas. O comportamento esperado é que o lado receptor continue rejeitando repetições depois do failover, o que significa que o último contador aceito de cada estação precisa ser compartilhado ou persistido. Observe se alguma mensagem antiga é aceita e se os alarmes ainda chegam em até 60 segundos. O critério de aprovação é zero repetições aceitas e nenhuma lacuna na entrega de alarmes.

### 34.7 Erros comuns e limites

- Integração "big bang" no final.
- Apenas testes de interface, sem cenários do sistema inteiro.
- Alarmes de segurança sem procedimentos operacionais.
- Contratos omissos sobre notificação de incidentes e divulgação de vulnerabilidades.
- Tratar problemas emergentes como bug de um único componente, e não como questão de interface.

A rajada de reconexão mostra o segundo e o último erros: cada componente passou em seus testes de interface, mas juntos atrasaram os alarmes, e a correção foi uma mudança de interface, e não um bug isolado. A integração na LRWA avança uma interface por vez. Cada passo tem seu próprio teste de interface.

### Exercícios — capítulo 34

**EX067 — Aritmética da rajada.** *Objetivo:* quantificar a rajada de reconexão. *Entradas:* 42 gateways × 180 leituras liberadas em 10 s; o front-end do SCADA processa 50 mensagens/s. *Passos:* calcule o tempo para escoar a rajada supondo que ela chegue toda de uma vez; calcule quanto espera um alarme prioritário no fim da fila; compare com R7. *Evidência esperada:* números. *Rubrica:* 3 = 7.560 mensagens / 50 por s = 151,2 s, viola os 60 s, explica a fila com prioridade ou a correção do valor mais recente; 2 = aritmética certa, sem correção; 1 = aritmética errada; 0 = nada.

**EX068 — Acordo com a operadora.** *Objetivo:* especificar uma interface organizacional. *Entradas:* o contrato da operadora LTE. *Passos:* liste seis cláusulas relevantes para a segurança, com termos mensuráveis. *Evidência esperada:* lista. *Rubrica:* 3 = tempo de notificação de incidentes, divulgação de vulnerabilidades, notificação de manutenção, prioridades de restauração, registro de acessos, exercício conjunto, com números; 2 = sem números; 1 = genérico; 0 = nada.

### Síntese do capítulo

Integre de forma incremental, com testes de interface e cenários do sistema inteiro, porque o comportamento emergente só aparece na combinação. Integre os controles às operações por meio de alarmes com significado, playbooks e treinamento. Torne as interfaces organizacionais explícitas e mensuráveis; sua segurança depende de organizações que você não controla.

<!-- cyberabc:chapter-navigation:start ch-34 -->
### Continue estudando — capítulo 34 de 50

[← Capítulo 33](#ch-33) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 35 →](#ch-35)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) levar um projeto do conceito ao projeto detalhado, com justificativa quantitativa; (2) integrar as análises de confiabilidade, segurança operacional, segurança da informação, desempenho e custo num único argumento; (3) construir um argumento de garantia estruturado que ligue alegações a evidências; e (4) defender decisões de projeto detalhado sob revisão. Ele integra os capítulos 26 a 34 e prepara os capítulos 36 a 40.

### 35.1 Do conceito ao projeto detalhado

O Ateliê I selecionou um conceito. O Ateliê II o detalha: componentes, configurações, interfaces, procedimentos e verificação específicos. Todos os números dos capítulos anteriores voltam: tempos de autonomia (capítulos 1 e 6), dimensionamento das baterias (Capítulo 3), taxas-base (Capítulo 7), latência (Capítulo 11), árvore de falhas (Capítulo 23), métricas de detecção (Capítulo 29), disponibilidade (Capítulo 32), filas (prévia do Capítulo 36). Um projeto detalhado é coerente quando esses números são consistentes entre si e com os requisitos. Para o TMRP, o dimensionamento das baterias, as 72 horas de operação automática local, a reserva de quatro horas do hospital e o tempo de recuperação precisam contar a mesma história; o EX069 mostra o que acontece quando um deles não conta.

### 35.2 Argumentos de garantia

Um **caso de garantia** é um argumento estruturado de que um sistema atende a uma alegação, apoiado em evidências. Ele tem uma alegação de topo ("o TMRP mantém o hospital abastecido em cenários críveis, incluindo a falsificação de comandos remotos"), subalegações (cada requisito atendido; riscos residuais aceitáveis), argumentos (por que as subalegações apoiam a alegação) e evidências (resultados de testes, análises, revisões). O modelo de argumentação de Toulmin — alegação, dados, garantia, respaldo, qualificador, refutação ([Toulmin, 1958/2003](https://doi.org/10.1017/CBO9780511840005)) — é uma lente útil: que evidência apoia a alegação, por que ela é pertinente e o que a derrotaria. **Derrotadores** explícitos ("a menos que o centro SCADA esteja comprometido") mantêm o argumento honesto.

### 35.3 Enunciado do Ateliê II (sintético)

Produza o projeto detalhado da fase 1 do TMRP (PS2, PS3, PS4 e Hollin Hill): lista de componentes com seus recursos de segurança; listas de permissões de zonas e condutos; procedimento de gestão de chaves; procedimentos de manual local e de failover; racionalização dos novos alarmes de segurança; plano de verificação; e um caso de garantia para a alegação de topo, com pelo menos quatro subalegações e derrotadores identificados. O enunciado cobre os quatro ativos que mais importam para St Brenna's: a PS2 como piloto comprovado, a PS3 e Hollin Hill como o caminho do reservatório e a PS4 como a alimentação direta. As demais estações e a estação de tratamento de Fenwick vêm em fases posteriores, então o caso de garantia da fase 1 precisa dizer claramente que ainda não as cobre.

### 35.4 Exemplo resolvido: um ramo do caso de garantia (sintético)

*Subalegação C2:* comandos remotos forjados não podem causar a perda do abastecimento do hospital. *Argumento:* os comandos exigem um MAC válido por estação (R1) e um contador novo (R2); mesmo comandos aceitos não conseguem levar o processo além dos limites locais (R3); a perda dos dois caminhos de abastecimento exige, além disso, que o tanque do hospital falhe (árvore de falhas). *Evidências:* T1 e T2 aprovados (bancada e aceitação em campo na PS2); T3 aprovado na v2; análise de condicionamento do Laboratório 9; revisão independente da gestão de chaves. *Derrotadores:* (D1) servidores SCADA comprometidos — os comandos são autênticos; mitigado pelos limites locais e pela aprovação por duas pessoas de mudanças em massa, residual aceito pela diretora de operações; (D2) chave de uma estação extraída de uma RTU roubada — confinado a uma estação, detecção pelo alarme de violação, procedimento de rotação. *Qualificador:* a alegação vale para os cenários do registro de riscos v1.2; não para um ataque físico às duas estações de bombeamento.

### 35.5 Atividade prática

Escreva o caso de garantia completo para o enunciado do Ateliê II e apresente-o a uma banca instruída a encontrar derrotadores. Dê à banca o enunciado, sua lista de componentes e o caso de garantia, e peça que encontrem o que derrotaria cada subalegação. Registre todo derrotador encontrado, quer você já o tivesse listado ou não, e escreva uma resposta: evidência que o trate, uma mudança de projeto ou uma aceitação explícita com um dono. Derrotadores como um centro SCADA comprometido ou a chave de uma RTU roubada são esperados; o trabalho da banca é encontrar os que você deixou passar, como o uso indevido do modo manual local.

### 35.6 Erros comuns e limites

- Números inconsistentes entre as análises.
- Casos de garantia com alegações e sem evidências, ou com evidências e sem argumento.
- Derrotadores omitidos para que o caso pareça mais forte.
- Projeto detalhado que muda os requisitos em silêncio.

O EX069 é um exemplo do primeiro erro dentro do próprio TMRP: R6 pede oito horas, mas o ensaio de recuperação mediu doze. Um caso que alegasse R6 citando o ensaio seria inconsistente, então o caso registra R6 como não atendido e explica por que a alegação sobre o hospital ainda pode se sustentar graças à operação automática local.

### Exercícios — capítulo 35

**EX069 — Verificação de consistência.** *Objetivo:* encontrar inconsistências entre as análises. *Entradas:* autonomia das baterias da PS4 de 24 h (R5); reserva do hospital de 4 h; R6 restaurar a operação remota em 8 h; o ensaio do Capítulo 47 mostra 12 h. *Passos:* identifique quais alegações conflitam e o que o conflito significa para o caso de garantia. *Evidência esperada:* análise. *Rubrica:* 3 = identifica que R6 não é atendido (12 > 8), que o abastecimento não depende da operação remota (automático local), de modo que a alegação sobre o hospital ainda pode se sustentar, e que o caso precisa registrar R6 como reprovado, com plano; 2 = parcial; 1 = não percebe R6; 0 = nada.

**EX070 — Encontre um derrotador.** *Objetivo:* contestar um argumento. *Entradas:* a subalegação C2 da §35.4. *Passos:* proponha mais dois derrotadores não listados e a evidência ou mudança de projeto que trataria cada um. *Evidência esperada:* dois derrotadores com respostas. *Rubrica:* 3 = derrotadores críveis (p. ex., uso indevido do modo manual local por um insider; caminho de atualização do firmware do gateway comprometido; falha na persistência do contador) com respostas específicas; 2 = um fraco; 1 = repete os listados; 0 = nada.

### Síntese do capítulo

O projeto detalhado faz com que todos os números anteriores se encontrem. Um caso de garantia liga a alegação de topo às evidências por meio de argumentos explícitos, com qualificadores e derrotadores declarados abertamente. A consistência entre as análises e a honestidade sobre os derrotadores são o que torna um projeto detalhado defensável.

<!-- cyberabc:chapter-navigation:start ch-35 -->
### Continue estudando — capítulo 35 de 50

[← Capítulo 34](#ch-34) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 36 →](#ch-36)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-36"></a>

## Capítulo 36 — Infraestrutura crítica e segurança setorial: desempenho e escala

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) modelar vazão, latência e utilização com a teoria das filas e a lei de Little; (2) estimar o custo de desempenho dos controles de segurança; (3) dimensionar sistemas para condições de pico e degradadas, incluindo a carga induzida por ataques; e (4) projetar para a escala — frotas de milhares de dispositivos — na gestão de chaves, no monitoramento e nas atualizações. Ele se apoia nos capítulos 11, 19 e 34 e prepara o Capítulo 41.

### 36.1 Filas por toda parte

As mensagens esperam em filas nos gateways, nos servidores e nos enlaces. A [lei de Little](https://doi.org/10.1287/opre.9.3.383), $L = \lambda W$, relaciona o número médio no sistema $L$, a taxa de chegada $\lambda$ e o tempo médio no sistema $W$, sob condições muito gerais. Para o modelo simples M/M/1 (chegadas aleatórias, serviço exponencial, um servidor com taxa de serviço $\mu$), a utilização é $\rho = \lambda/\mu$ e $W = 1/(\mu - \lambda)$. O atraso cresce sem limite quando $\rho \to 1$: com 80% de utilização, a mensagem média passa cinco tempos de serviço no sistema; com 96%, vinte e cinco. Dimensione para que a utilização de pico fique bem abaixo de 1 — em geral abaixo de 0,7 nos caminhos críticos para a latência.

### 36.2 O custo da segurança

Todo controle custa algo: bytes (os 22 bytes de sobrecarga do Laboratório 8), CPU (cálculo do MAC, handshakes TLS), latência (decisões de política, inspeção) e tempo dos operadores (nova autenticação, aprovações). Meça-os na bancada. Os custos costumam ser pequenos em relação às idas e voltas da rede, mas importam em enlaces restritos (rádio de baixa largura de banda), em dispositivos restritos (microcontroladores pequenos) e em escala. Para o TMRP, os custos medidos incluem os vinte e dois bytes extras por quadro, o cálculo do MAC de cada mensagem no verificador do lado do SCADA e o tempo dos operadores na aprovação por duas pessoas de mudanças de setpoint em massa. Nenhum é grande, mas é o limite de vazão do verificador que o exemplo resolvido precisa dimensionar.

### 36.3 Carga de pico, degradada e de ataque

Dimensione para a pior carga crível: inundações de alarmes em tempestades, rajadas de reconexão após quedas (Capítulo 34), recuperação do atraso após failover e inundações deliberadas. Um atacante que consiga enviar tráfego a um gateway pode empurrar a utilização para perto de 1 e atrasar alarmes legítimos; as defesas incluem limites de taxa por origem, filas com prioridade para os alarmes, rejeição precoce do tráfego não autenticado (faça primeiro a verificação barata) e margens de capacidade. Para o TMRP, a rajada de reconexão encontrada nos testes de integração é o exemplo mais claro, e a fila com prioridade para alarmes no verificador é a defesa escolhida no exemplo resolvido.

### 36.4 Escala

Na escala de frota, os processos manuais falham. O cadastro, a rotação e a revogação de chaves precisam ser automatizados, com auditoria; o monitoramento precisa agregar e priorizar; as atualizações precisam ser feitas em etapas e ser observáveis; o inventário precisa ser conciliado continuamente. Um procedimento que leva 30 minutos por dispositivo consome três semanas de trabalho da equipe para mil dispositivos. A LRWA tem hoje apenas 42 estações de campo, mas o mesmo projeto pode depois ser usado numa frota muito maior, então o TMRP automatiza desde o início os registros de cadastro e rotação de chaves, em vez de depender de uma planilha mantida por um único engenheiro.

### 36.5 Exemplo resolvido: dimensionamento do gateway (sintético)

O verificador do lado do SCADA consegue processar 50 mensagens/s. Em regime permanente, as 42 estações da LRWA geram cerca de 20 mensagens/s ($\rho = 0.4$, $W \approx 33$ ms). Durante uma tempestade, os alarmes elevam as chegadas a 40/s ($\rho = 0.8$, $W = 100$ ms, cerca de 4 mensagens no sistema). Com 48/s, $W = 500$ ms e há em média 24 mensagens no sistema. A varredura sequencial de 42 estações, com 180 ms de ida e volta mais o tempo dos registradores, leva 7,8 s por ciclo; seis canais paralelos a reduzem a 1,3 s. Decisões: capacidade do verificador dobrada para 100 mensagens/s, por folga; fila com prioridade para os alarmes; relato por exceção para os alarmes, em vez de esperar pela varredura.

### 36.6 Atividade prática: Laboratório 13

```python
# Lab 13 - is the telemetry gateway fast enough? M/M/1 and a polling cycle (synthetic, offline)
mu = 50.0                                    # messages/s the gateway can verify and forward
for lam in (20.0, 40.0, 45.0, 48.0):
    rho = lam / mu; W = 1 / (mu - lam); L = lam * W
    print(f"lambda={lam:>4} rho={rho:.2f} W={W*1000:6.1f} ms L={L:5.1f} msgs")
stations, regs_per_poll, rtt_ms, per_reg_ms = 42, 3, 180, 2
cycle = stations * (rtt_ms + regs_per_poll * per_reg_ms)
print(f"sequential polling cycle: {cycle/1000:.2f} s; with 6 parallel channels: {cycle/6/1000:.2f} s")
```

Saída esperada:

```text
lambda=20.0 rho=0.40 W=  33.3 ms L=  0.7 msgs
lambda=40.0 rho=0.80 W= 100.0 ms L=  4.0 msgs
lambda=45.0 rho=0.90 W= 200.0 ms L=  9.0 msgs
lambda=48.0 rho=0.96 W= 500.0 ms L= 24.0 msgs
sequential polling cycle: 7.81 s; with 6 parallel channels: 1.30 s
```

As quatro primeiras linhas mostram o atraso crescendo bruscamente à medida que as chegadas se aproximam da capacidade do verificador, de cinquenta mensagens por segundo: com vinte mensagens por segundo, a mensagem média espera cerca de um terço de décimo de segundo, enquanto com quarenta e oito espera meio segundo e há duas dúzias de mensagens no sistema. As linhas da varredura mostram por que a LRWA usa seis canais paralelos: um ciclo sequencial de quase oito segundos deixaria os alarmes esperando muito antes de chegarem ao verificador.

### 36.7 Erros comuns e limites

- Dimensionar para a carga média.
- Ignorar que o atraso explode perto da utilização plena.
- Supor que os custos de segurança são desprezíveis sem medi-los no dispositivo-alvo.
- Procedimentos manuais que não escalam.
- M/M/1 usado onde as chegadas são em rajadas ou o serviço é determinístico; trate-o como uma primeira aproximação.

O dimensionamento do TMRP evita os dois primeiros erros dimensionando para a carga de tempestade e mantendo o verificador dobrado bem abaixo da utilização plena, e trata os resultados de filas como uma primeira aproximação a ser conferida com as medições de bancada.

### Exercícios — capítulo 36

**EX071 — Dobrar a capacidade.** *Objetivo:* quantificar a folga. *Entradas:* Laboratório 13 com $\mu = 100$. *Passos:* calcule $\rho$, $W$ e $L$ a 20, 40 e 48 mensagens/s; compare com $\mu = 50$. *Evidência esperada:* tabela. *Rubrica:* 3 = valores corretos (p. ex., a 48/s: ρ = 0,48, W ≈ 19,2 ms, L ≈ 0,92) e conclusão; 2 = um erro; 1 = uma única taxa; 0 = nada.

**EX072 — Defesa contra inundações.** *Objetivo:* projetar contra a carga de ataque. *Entradas:* um atacante na rede LTE consegue enviar 1.000 quadros forjados/s ao verificador. *Passos:* proponha três defesas em ordem de custo e explique como cada uma protege a latência dos alarmes. *Evidência esperada:* lista. *Rubrica:* 3 = filtragem no nível da rede por origem/túnel, verificações prévias baratas antes do MAC, limites de taxa por origem e filas com prioridade, com raciocínio sobre onde a carga é descartada; 2 = uma defesa; 1 = apenas "acrescentar capacidade"; 0 = nada.

### Síntese do capítulo

As filas governam a latência; a lei de Little e os modelos de filas simples mostram que o atraso explode à medida que a utilização se aproxima de um. Meça os custos dos controles de segurança, dimensione para a carga de pico, degradada e de ataque, com prioridade para os alarmes, e automatize desde o início os processos na escala de frota.

<!-- cyberabc:chapter-navigation:start ch-36 -->
### Continue estudando — capítulo 36 de 50

[← Capítulo 35](#ch-35) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 37 →](#ch-37)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-37"></a>

## Capítulo 37 — Infraestrutura crítica e segurança setorial: operações

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) projetar as operações de segurança para TO — monitoramento, triagem, escalonamento, coordenação com as operações do processo; (2) escrever procedimentos operacionais e playbooks que os operadores consigam executar sob estresse; (3) gerenciar mudanças, acessos e vulnerabilidades nas operações diárias; e (4) aprender com incidentes e quase acidentes sem atribuir culpa. Ele se apoia nos capítulos 18, 29 e 34 e prepara os capítulos 38 e 47.

### 37.1 Operações de segurança em TO

O monitoramento de segurança de TO observa o tráfego de rede, os logs e os dados do processo em busca de sinais de uso indevido. A triagem em TO difere da de TI: a primeira pergunta não é "isto é malicioso?", mas "o processo está seguro?". Os caminhos de escalonamento, portanto, vão até a sala de controle e o gerente de operações de plantão, além da equipe de segurança. Muitas concessionárias não têm uma equipe de segurança 24/7; a sala de controle tem pessoal 24/7 e precisa conseguir agir sobre os alarmes de segurança com playbooks claros, escalonando para especialistas de segurança de sobreaviso.

### 37.2 Playbooks

Um playbook é um procedimento curto e testado para uma situação específica: gatilho, ações imediatas de segurança operacional, informações a coletar, decisões e quem as toma, comunicações e retorno à normalidade. Escreva para um operador cansado às 03:00: passos numerados, pontos de decisão claros, números de telefone, nada de jargão. Teste cada playbook em exercícios e atualize-o depois de cada uso. Orientações de tratamento de incidentes como a [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) fornecem a estrutura geral; os playbooks de TO acrescentam passos de segurança do processo. O playbook da LRWA para uma mudança inesperada de setpoint é escrito segundo esse padrão.

### 37.3 Gestão de mudanças, acessos e vulnerabilidades

As operações diárias mantêm o sistema no estado projetado: gestão de mudanças (nenhuma mudança de configuração sem aprovação e registro); gestão de acessos (admissões, transferências, desligamentos; sessões de fornecedores aprovadas a cada uso); gestão de vulnerabilidades (acompanhar alertas como os [ICS advisories da CISA](https://www.cisa.gov/news-events/ics-advisories), avaliar a aplicabilidade, planejar a correção, Capítulo 12). A deriva — mudanças não documentadas que se acumulam — é o modo mais comum de um sistema bem projetado se tornar inseguro. Na LRWA, o script de relatório corporativo esquecido, encontrado na revisão de fluxos, é um exemplo de deriva, e o controle de mudanças em cada conduto é o modo como o TMRP impede que esses caminhos reapareçam.

### 37.4 Aprender sem culpa

Incidentes e quase acidentes são evidências sobre o sistema. [Reason (2000)](https://doi.org/10.1136/bmj.320.7237.768) contrastou a abordagem da pessoa (culpar indivíduos) com a abordagem do sistema (defesas, barreiras e condições latentes), argumentando que a segunda é mais eficaz. As revisões pós-ação perguntam o que aconteceu, por que aquilo fazia sentido para as pessoas envolvidas no momento, quais defesas funcionaram ou falharam e o que vai mudar. A culpa suprime o relato, e quase acidentes não relatados são lições perdidas. Na LRWA, o técnico que conectou um laptop à rede da PS3 no EX074 é tratado desse modo: a revisão pergunta por que o jump host parecia lento demais e o que tornou o atalho possível.

### 37.5 Exemplo resolvido: playbook "mudança inesperada de setpoint" (sintético)

*Gatilho:* o SCADA mostra uma mudança de setpoint em qualquer estação que não corresponde a uma ação de operador nos últimos 5 minutos, ou um gateway registra falhas repetidas de MAC. *Ações imediatas de segurança operacional:* (1) confira os valores do processo da estação com as medições independentes; (2) se estiverem fora da faixa normal, restaure localmente o setpoint anterior ou passe para o manual local por meio do técnico de plantão; (3) não desligue a telemetria remota. *Coletar:* estação, horário, valores antigo/novo, trecho do log do gateway, log do operador. *Decidir:* o gerente de plantão decide se desativa as escritas remotas em toda a frota (chave de configuração dos gateways). *Comunicar:* segurança de sobreaviso em até 30 minutos; contato com o hospital se a PS3/PS4 forem afetadas. *Retorno à normalidade:* as escritas remotas só são reativadas depois que a segurança de sobreaviso concordar.

### 37.6 Atividade prática

Execute o playbook num exercício de mesa com uma sequência roteirizada de injeções (primeiro uma única mudança de setpoint, depois falhas de MAC numa segunda estação, depois um telefonema do hospital sobre pressão baixa). Registre os tempos de decisão e as ambiguidades e revise o playbook. Execute as injeções em ordem e anote o horário de cada decisão. Observe em especial se a equipe mantém a telemetria remota funcionando, como o playbook exige, e se o gerente de plantão decide sobre a desativação das escritas remotas em toda a frota antes que chegue o telefonema do hospital. Registre cada ponto em que alguém perguntou o que o playbook queria dizer. Depois do exercício, reescreva esses passos e agende uma segunda execução para conferir as revisões.

### 37.7 Erros comuns e limites

- Alarmes de segurança encaminhados a uma equipe que não está de serviço quando eles disparam.
- Playbooks escritos para especialistas, nunca testados.
- Gestão de mudanças contornada "temporariamente".
- Revisões pós-ação que terminam com "erro do operador".

O projeto do playbook da LRWA responde a esses erros: os alarmes de segurança chegam à sala de controle, que tem pessoal a todo momento, e a segurança de sobreaviso é chamada em até 30 minutos. O playbook é testado em exercícios de mesa, e o controle de mudanças não tem exceções temporárias. As revisões pós-ação na LRWA buscam condições latentes, como um jump host lento, em vez de terminar com erro do operador.

### Exercícios — capítulo 37

**EX073 — Revisão do playbook.** *Objetivo:* melhorar um playbook. *Entradas:* §37.5. *Passos:* identifique três fraquezas (p. ex., limiares ambíguos, contatos ausentes, padrão inseguro) e reescreva os passos afetados. *Evidência esperada:* passos revisados. *Rubrica:* 3 = fraquezas substantivas corrigidas com passos executáveis; 2 = mudanças cosméticas; 1 = apenas crítica; 0 = nada.

**EX074 — Revisão de quase acidente.** *Objetivo:* conduzir uma revisão sem culpa. *Entradas:* um técnico conectou um laptop à rede de controle da PS3 para baixar logs, contornando o jump host; o laptop não tinha sido verificado. Nenhum incidente se seguiu. *Passos:* escreva uma revisão de uma página: o que aconteceu, por que fazia sentido, defesas que falharam, mudanças no sistema. *Evidência esperada:* revisão. *Rubrica:* 3 = explica a racionalidade local (jump host lento, prazo), identifica condições latentes (sem segurança de porta, sem caminho fácil para os logs), propõe mudanças no sistema; 2 = alguma culpa; 1 = "treinar de novo o técnico"; 0 = nada.

### Síntese do capítulo

As operações de segurança de TO começam pela segurança do processo e encaminham o escalonamento pela sala de controle. Os playbooks precisam ser curtos, testados e executáveis sob estresse. A gestão diária de mudanças, acessos e vulnerabilidades mantém o sistema como projetado, e o aprendizado sem culpa com incidentes e quase acidentes melhora as defesas.

<!-- cyberabc:chapter-navigation:start ch-37 -->
### Continue estudando — capítulo 37 de 50

[← Capítulo 36](#ch-36) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 38 →](#ch-38)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-38"></a>

## Capítulo 38 — Infraestrutura crítica e segurança setorial: validação

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) distinguir a validação (o sistema certo para a necessidade) da verificação (o sistema construído segundo sua especificação); (2) validar com as partes interessadas por meio de demonstrações, ensaios operacionais e exercícios; (3) usar a rastreabilidade para mostrar quais necessidades estão apoiadas em evidências e quais não estão; e (4) relatar os resultados da validação com honestidade, incluindo os resultados parciais. Ele se apoia nos capítulos 16, 24 e 30 e prepara os capítulos 40 e 48.

### 38.1 Verificação não é validação

Um sistema pode passar em todos os testes contra sua especificação e ainda assim falhar com seus usuários, se a especificação estava errada ou incompleta. A validação pergunta se o sistema atende às necessidades das partes interessadas no ambiente pretendido: os operadores conseguem de fato operar o modo manual local à noite? O hospital de fato recebe água dentro de sua reserva quando a PS4 é perdida? As evidências de validação vêm do uso realista: ensaios operacionais, demonstrações com as partes interessadas, exercícios e os primeiros dados de operação. Para o TMRP, o exercício noturno do modo manual local é a atividade de validação que responde à primeira pergunta.

### 38.2 A rastreabilidade como mapa de evidências

Rastreie as necessidades até os requisitos, os testes e os resultados. Depois faça três perguntas: quais requisitos não têm teste (alegações não testadas)? Quais testes falharam ou não foram executados (alegações sem apoio)? Quais necessidades dependem apenas de requisitos ainda não verificados (necessidades não validadas)? O Laboratório 14 calcula isso para o dossiê do TMRP. Para o TMRP, as perguntas são concretas. R4 não tem teste porque sua demonstração nunca foi agendada. R9, o alarme de dosagem independente, não tem teste algum: a tabela de requisitos indica um teste como seu método de verificação, mas nenhum teste jamais foi escrito para ele. O único teste registrado de R3 é o reprovado na v1, e o teste de R8 não foi executado. N1 depende de R4, então não pode ser alegada como validada até que o exercício noturno aconteça. O Laboratório 14 imprime essas lacunas diretamente.

### 38.3 Validação com as partes interessadas

Envolva as pessoas a quem o sistema serve. Os operadores validam os procedimentos e as telas; a equipe de manutenção valida a reparabilidade e as peças de reposição; o hospital valida que os arranjos de abastecimento atendem às suas necessidades; os reguladores validam o raciocínio de conformidade. Registre as constatações deles como registraria as constatações de uma revisão, com respostas. Para o TMRP, os operadores validam o procedimento manual local e os novos alarmes de segurança, a equipe de manutenção confere que os gateways podem ser substituídos a partir das reservas, e o hospital confirma que os arranjos de abastecimento e sua reserva de quatro horas atendem às suas necessidades. As constatações deles vão para o mesmo registro de respostas das constatações da revisão de projeto.

### 38.4 Relatar resultados parciais

Relate a situação da validação por necessidade: validada, parcialmente validada (com o que falta), não validada. Não arredonde para cima. "N1 parcialmente validada: o ensaio de perda da PS4 atendeu à reserva de 4 h; a perda combinada da PS4 e do alimentador F1 da rede elétrica ainda não foi ensaiada." O mapa de evidências do TMRP torna isso concreto: N1 depende de R4, que ainda não foi demonstrado, então N1 é relatada como não validada até que o exercício noturno aconteça, mesmo que a maioria de seus outros requisitos tenha passado nos testes. A situação é atualizada depois do exercício.

### 38.5 Exemplo resolvido: mapa de evidências do TMRP (sintético)

O Laboratório 14 mostra: R4 (operação manual local) não tem teste — foi planejado como demonstração e nunca agendado; R3 tem um teste reprovado (na v1; o novo teste na v2 ainda não foi lançado na matriz); o teste T6 de R8 não foi executado. R9 (alarme de dosagem independente) também não tem teste: seu método de verificação é "Teste", mas nenhum identificador de teste foi jamais atribuído, então a evidência para ele é uma intenção de projeto, e não um resultado. Verificados: 5 de 9 requisitos (55,6%). Consequência para a validação: N1 (abastecimento do hospital) depende de R4, então N1 não pode ser alegada como validada; o exercício noturno do manual local é agendado como a atividade de validação. A matriz também expõe uma lacuna administrativa — o novo teste do T3 na v2 precisa ser registrado —, exatamente o tipo de inconsistência que examinadores e auditores encontram.

### 38.6 Atividade prática: Laboratório 14

```python
# Lab 14 - requirements traceability: what is claimed but not shown? (synthetic TMRP dossier, offline)
REQS = ["R1 auth telemetry", "R2 replay reject", "R3 setpoint bounds", "R4 local manual", "R5 24h hold-up",
        "R6 restore 8h", "R7 alarm 60s", "R8 log integrity", "R9 dosing alarm"]
TESTS = {"T1": ["R1"], "T2": ["R1", "R2"], "T3": ["R3"], "T4": ["R5"], "T5": ["R7"], "T6": ["R8"], "T7": ["R6"]}
RESULT = {"T1": "pass", "T2": "pass", "T3": "fail", "T4": "pass", "T5": "pass", "T6": "not run", "T7": "pass"}
ids = [r.split()[0] for r in REQS]
cov = {r: [t for t, rs in TESTS.items() if r in rs] for r in ids}
verified = [r for r in ids if cov[r] and all(RESULT[t] == "pass" for t in cov[r])]
print("untested:", [r for r in ids if not cov[r]])
print("tested but not passing:", [r for r in ids if cov[r] and r not in verified])
print(f"verified {len(verified)}/{len(ids)} = {100*len(verified)/len(ids):.1f}%")
```

Saída esperada:

```text
untested: ['R4', 'R9']
tested but not passing: ['R3', 'R8']
verified 5/9 = 55.6%
```

A saída mostra que R4 e R9 não têm teste, que R3 e R8 estão testados mas não aprovados, e que cinco de nove requisitos estão verificados. A situação de R3 está desatualizada, e não realmente reprovada: o novo teste na v2 foi aprovado, mas ninguém o lançou na matriz, exatamente a lacuna administrativa de que o exemplo resolvido adverte. O EX075 atualiza o mapa. R9 é a lição mais difícil: o alarme de dosagem aparece no conjunto de requisitos, na tabela de riscos e nos controles de dosagem, então parece coberto, mas nenhum teste jamais lhe foi atribuído. Uma versão anterior desta matriz deixava R9 inteiramente fora da lista, o que elevava a fração verificada de cinco de nove para cinco de oito sem nenhuma evidência nova. Uma matriz precisa listar todo requisito definido, porque um requisito que ela omite não pode ser relatado como não testado.

### 38.7 Erros comuns e limites

- Chamar de "validação" um conjunto de testes aprovado.
- Partes interessadas consultadas apenas no início.
- Arredondar a validação parcial para "validada".
- Mapas de evidências não atualizados depois de novos testes.

O próprio mapa do TMRP mostra o último erro: o novo teste do T3 na v2 foi aprovado, mas a matriz nunca foi atualizada. Partes interessadas como os operadores e o hospital são envolvidas o tempo todo, e não apenas quando os requisitos foram escritos, e o mapa de evidências é atualizado toda vez que um novo teste ou uma demonstração produz um resultado, de modo que a situação de validação relatada nunca se adianta às evidências.

### Exercícios — capítulo 38

**EX075 — Atualize o mapa.** *Objetivo:* manter a rastreabilidade. *Entradas:* Laboratório 14. *Passos:* (1) acrescente o T3b (novo teste na v2) cobrindo R3 com resultado "pass" e remova a ligação do T3 com R3 como superada; (2) acrescente a demonstração T8 cobrindo R4 com resultado "pass"; (3) execute o T6 com resultado "pass"; recalcule. *Evidência esperada:* código e saída. *Rubrica:* 3 = oito de nove verificados (88,9%), R9 ainda listado como não testado porque não existe teste do alarme de dosagem, com uma nota de que verificação ≠ validação; 2 = uma mudança não feita; 1 = não executado; 0 = nada.

**EX076 — Plano de validação para N1.** *Objetivo:* planejar a validação com as partes interessadas. *Entradas:* N1 "o hospital não pode ficar sem água por > 4 h". *Passos:* proponha duas atividades de validação com as partes interessadas, condições realistas, observações e critérios de sucesso. *Evidência esperada:* plano. *Rubrica:* 3 = atividades realistas (exercício noturno do manual local com o efetivo real; isolamento planejado da PS4 com monitoramento pelo hospital), critérios ligados à reserva de 4 h, partes interessadas nomeadas pelo papel; 2 = critérios vagos; 1 = testes rebatizados de validação; 0 = nada.

### Síntese do capítulo

A verificação pergunta se o sistema foi construído direito; a validação pergunta se ele é o sistema certo. Use a rastreabilidade como mapa de evidências para encontrar alegações não testadas, sem apoio e não validadas, valide com as pessoas a quem o sistema serve em condições realistas e relate os resultados parciais como parciais.

<!-- cyberabc:chapter-navigation:start ch-38 -->
### Continue estudando — capítulo 38 de 50

[← Capítulo 37](#ch-37) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 39 →](#ch-39)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-39"></a>

## Capítulo 39 — Infraestrutura crítica e segurança setorial: manutenibilidade

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) projetar para a manutenibilidade ao longo de ciclos de vida longos — atualizações, peças de reposição, competências, documentação; (2) gerenciar a dívida técnica e a obsolescência em TO; (3) planejar a agilidade criptográfica e a transição para a criptografia pós-quântica; e (4) planejar a desativação com segurança. Ele se apoia nos capítulos 8, 14 e 31 e prepara os capítulos 41 e 44.

### 39.1 Ciclos de vida longos

Os ativos de infraestrutura duram décadas; o software e as ameaças mudam em meses. Manutenibilidade significa que o sistema pode ser mantido seguro e funcional por toda a sua vida: componentes substituíveis sem novo projeto; atualizações possíveis sem longas interrupções; documentação em dia; competências disponíveis. Escolhas de projeto que prejudicam a manutenibilidade incluem protocolos proprietários com um único fornecedor, código personalizado não documentado e hardware sem caminho de atualização. Para o TMRP, as RTUs instaladas agora talvez ainda funcionem nos anos 2040, então o projeto do gateway, o formato das mensagens e a gestão de chaves precisam ser manuteníveis ao longo desse período.

### 39.2 Dívida técnica e obsolescência

A dívida técnica é o custo futuro dos atalhos tomados agora: uma configuração fixa no código, um teste pulado, um gateway construído "temporariamente" para RTUs legadas. Registre os itens de dívida com dono, custo de correção e risco de deixá-los. A gestão da obsolescência acompanha as datas de fim de venda e de fim de suporte de cada componente e planeja a substituição antes que o suporte termine, mantendo reservas onde a substituição é lenta. Os gateways do TMRP para as unidades legadas RTU-A da PS1 e da PS2 estão registrados como dívida com horizonte de três anos. As reservas são compradas antes do fim de venda.

### 39.3 Agilidade criptográfica

Os algoritmos se enfraquecem e as normas mudam. A agilidade criptográfica é a capacidade de mudar algoritmos e tamanhos de chave sem projetar o sistema de novo: identificadores de algoritmo nos formatos de mensagem, caminhos de atualização de firmware e uma gestão de chaves capaz de provisionar novos tipos de chave. O NIST publicou suas primeiras normas de criptografia pós-quântica (FIPS 203, 204 e 205) em agosto de 2024 ([anúncio do NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)); equipamentos de infraestrutura comprados agora talvez ainda estejam operando quando adversários com capacidade quântica forem plausíveis, então os mecanismos de chave pública em dispositivos de vida longa precisam de um caminho de migração. MACs simétricos como o HMAC-SHA256 são muito menos afetados; a troca de chaves e as assinaturas são onde a migração importa.

### 39.4 Desativação segura

Dispositivos aposentados contêm chaves, configurações e detalhes da rede. Passos da desativação: revogar chaves e certificados; remover contas; apagar ou destruir o armazenamento conforme a política; atualizar o inventário, os modelos e as listas de permissões; e remover as regras de firewall que serviam ao dispositivo. Regras obsoletas de dispositivos desativados são um caminho clássico para atacantes que colocam um novo dispositivo num endereço antigo. A revisão de manutenibilidade do TMRP constatou que não existia procedimento de desativação, então um foi escrito e ligado à gestão de mudanças. Ele será usado pela primeira vez quando a RTU-A legada da PS2 e seu gateway forem substituídos, como descreve o EX078.

### 39.5 Exemplo resolvido: revisão de manutenibilidade do TMRP (sintético)

A revisão constata: (1) os gateways da PS1/PS2 são dívida técnica com horizonte de três anos — registrados com plano de substituição; (2) o formato de mensagem do Laboratório 8 não tem identificador de algoritmo — alterado para incluir um ID de suíte de um byte (versão 1 = HMAC-SHA256-128) antes da implantação na frota, ao custo de um byte por mensagem; (3) a assinatura do firmware da RTU-B usa um esquema de assinatura clássico — pedido ao fornecedor um roteiro de migração pós-quântica como condição contratual; (4) não há modems LTE de reserva e o modelo chega ao fim de venda no ano que vem — comprar reservas agora, planejar a substituição; (5) procedimento de desativação ausente — escrito e ligado à gestão de mudanças.

### 39.6 Atividade prática

Monte um registro de obsolescência para os componentes do TMRP (RTUs, gateways, modems, servidores SCADA, sistema operacional, HSM) com datas presumidas, situação do suporte, reservas mantidas e plano de substituição. Inclua todos os componentes que a revisão do TMRP menciona: a RTU-A e a RTU-B, os gateways, os modems LTE, os servidores SCADA e seu sistema operacional, e o módulo de segurança de hardware. Para cada um, registre as datas presumidas de fim de venda e de fim de suporte, as reservas mantidas e o plano de substituição. Sinalize qualquer componente cujo suporte termine antes da substituição planejada, como a revisão constatou para os modems LTE. Mantenha o registro sob controle de mudanças para que ele continue atualizado.

### 39.7 Erros comuns e limites

- Projetos que exigem o fornecedor original para sempre.
- Dívida técnica não registrada.
- Formatos de mensagem sem versionamento nem identificadores de algoritmo.
- Dispositivos desativados que deixam chaves e regras de firewall para trás.

A revisão do TMRP encontrou o terceiro erro no quadro do Laboratório 8 e o corrigiu com um identificador de suíte de um byte antes da implantação na frota. Ela também registrou os gateways legados como dívida e escreveu o procedimento de desativação que faltava. Os modems LTE de reserva são comprados antes do fim de venda do modelo. O novo procedimento revoga as chaves e remove as regras de firewall obsoletas.

### Exercícios — capítulo 39

**EX077 — Adaptação para agilidade.** *Objetivo:* acrescentar agilidade criptográfica. *Entradas:* formato de quadro do Laboratório 8. *Passos:* acrescente um ID de suíte de um byte e uma política do receptor que aceite apenas as suítes configuradas; mostre como a suíte 2 (um MAC diferente) poderia ser introduzida durante um período de transição e como a suíte 1 seria aposentada. *Evidência esperada:* projeto e esboço curto de código. *Rubrica:* 3 = ID de suíte autenticado (dentro do MAC), política de suítes permitidas por estação, prevenção de rebaixamento, passo de aposentadoria; 2 = ID de suíte não autenticado; 1 = apenas descrição; 0 = nada.

**EX078 — Checklist de desativação.** *Objetivo:* aposentar um dispositivo com segurança. *Entradas:* a RTU-A legada da PS2 e o gateway sendo substituídos pela RTU-B. *Passos:* escreva uma checklist de pelo menos oito passos, com a evidência de cada um. *Evidência esperada:* checklist. *Rubrica:* 3 = chaves revogadas, contas removidas, armazenamento apagado, inventário/modelo/lista de permissões atualizados, regras de firewall removidas, linhas de base do monitoramento atualizadas, destinação das reservas, aprovação formal; 2 = faltam regras ou chaves; 1 = genérico; 0 = nada.

### Síntese do capítulo

Projete para décadas: componentes substituíveis, software atualizável, documentação em dia, competências disponíveis. Registre a dívida técnica, gerencie a obsolescência antes do fim do suporte, incorpore a agilidade criptográfica aos formatos e aos caminhos de atualização, com um plano de migração pós-quântica, e desative de modo que nada — chaves, contas, regras — sobreviva ao dispositivo.

<!-- cyberabc:chapter-navigation:start ch-39 -->
### Continue estudando — capítulo 39 de 50

[← Capítulo 38](#ch-38) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 40 →](#ch-40)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) projetar e executar uma campanha de injeção de falhas com semente contra um controle de segurança; (2) classificar os resultados e calcular as taxas de detecção por classe de falha; (3) encontrar lacunas entre o que um controle detecta e o que um requisito exige; e (4) relatar uma campanha de forma reprodutível. Ele estende o Capítulo 30 às falhas ambientais e aos ataques e prepara o projeto final (capítulos 44 a 47).

### 40.1 Injeção de falhas

A injeção de falhas introduz deliberadamente falhas — mensagens corrompidas, descartadas, atrasadas, repetidas ou reordenadas; reinícios de processos; saltos de relógio; esgotamento de recursos — para observar como um sistema se comporta. Ela testa o tratamento de erros que os testes comuns raramente alcançam. Uma campanha especifica o modelo de falhas (quais falhas, a que taxas), o sistema sob teste, o oráculo (qual é o comportamento correto para cada falha) e as medições. Para o TMRP, a campanha do receptor neste capítulo injeta corrupção, repetição, atraso e descarte. Cada falha tem um oráculo. Os resultados são contados por classe.

### 40.2 Oráculos e classificação

Para cada falha injetada, defina o resultado esperado: corrompida → rejeitada como corrompida; repetida → rejeitada como repetição; atrasada além da janela de atualidade → rejeitada como inativa; descartada → detectada como lacuna (ou não, se o projeto não detecta lacunas). Classifique os resultados observados contra os esperados. Uma falha que produz "ok" quando deveria ter sido rejeitada é uma **falha silenciosa** — a classe mais importante a encontrar. Para o receptor do TMRP, a classe dos descartes é aquela em que o oráculo expôs uma lacuna: o projeto não tinha resultado esperado para uma mensagem perdida, porque ninguém tinha perguntado o que deveria acontecer.

### 40.3 Sementes, taxas e cobertura

Defina a semente do gerador de falhas, registre-a e relate as contagens por classe de falha. Escolha taxas que produzam eventos suficientes de cada classe para serem significativos; uma campanha de 500 mensagens com 5% por classe de falha dá cerca de 25 eventos de cada — o bastante para encontrar falhas sistemáticas, não o bastante para estimar com precisão as raras. Estenda a campanha para as classes que preocupam especialmente. A campanha do TMRP usa a semente quarenta, quinhentas mensagens e cinco por cento por classe de falha, de modo que cada classe produz eventos suficientes para mostrar o comportamento sistemático. O projeto final estende a campanha a dez mil mensagens em sete classes de falha, incluindo reinício e reordenação.

### 40.4 Exemplo resolvido: campanha do receptor de telemetria (sintético)

O Laboratório 15 envia 500 mensagens com a semente 40; cada uma tem 80% de chance de não ter falha e 5% de cada: corrupção, repetição de uma mensagem válida anterior, atraso de 120 s (janela de atualidade de 60 s) e descarte. Resultados: toda mensagem corrompida foi rejeitada como corrompida; toda repetição, como repetição; toda mensagem atrasada, como inativa; nenhuma falha produziu um "ok" silencioso. Mas **os descartes são invisíveis para o receptor**: 21 mensagens foram perdidas e o receptor não gerou nada. A verificação de contador do receptor rejeita contadores antigos, mas não alarma diante de lacunas. O requisito R7 (alarmes em até 60 s) implica que a perda dos dados de uma estação precisa, ela própria, ser visível. Mudança de projeto: alarmar quando nenhuma mensagem válida chegar de uma estação por 60 s, e registrar em log as lacunas de contador. A campanha é executada de novo depois da mudança, com a mesma semente.

### 40.5 Atividade prática: Laboratório 15

```python
# Lab 15 - fault-injection campaign against the telemetry receiver (synthetic, seeded, offline)
import random, hmac, hashlib, struct
KEY = b"k" * 32
def seal(c, lvl, ts):
    b = struct.pack(">QHI", c, lvl, ts); return b + hmac.new(KEY, b, hashlib.sha256).digest()[:16]
def receive(m, state, now, max_age=60):
    b, tag = m[:14], m[14:]
    if len(m) != 30 or not hmac.compare_digest(tag, hmac.new(KEY, b, hashlib.sha256).digest()[:16]): return "corrupt"
    c, lvl, ts = struct.unpack(">QHI", b)
    if c <= state["last"]: return "replay"
    if now - ts > max_age: return "stale"
    state["last"] = c; return "ok"
rng = random.Random(40); state = {"last": 0}; tally = {}; sent = []
for i in range(1, 501):
    now = 10 * i; m = seal(i, 300, now); fault = rng.choices(["none", "corrupt", "replay", "delay", "drop"], [80, 5, 5, 5, 5])[0]
    if fault == "corrupt": m = m[:5] + bytes([m[5] ^ 0x10]) + m[6:]
    if fault == "replay" and sent: m = rng.choice(sent)
    if fault == "drop": tally[("drop", "lost")] = tally.get(("drop", "lost"), 0) + 1; continue
    arrive = now + (120 if fault == "delay" else 1)
    out = receive(m, state, arrive)
    tally[(fault, out)] = tally.get((fault, out), 0) + 1
    if fault == "none": sent.append(m)
for k in sorted(tally): print(k, tally[k])
```

Saída esperada:

```text
('corrupt', 'corrupt') 14
('delay', 'stale') 22
('drop', 'lost') 21
('none', 'ok') 419
('replay', 'replay') 24
```

Toda mensagem corrompida, repetida e atrasada terminou na classe que seu oráculo previa, e nenhuma falha produziu uma aceitação silenciosa. As mensagens descartadas são a constatação: vinte e uma se perderam e o receptor não gerou nada, porque as verificações de contador só rejeitam mensagens antigas. Esse resultado levou ao alarme de estação inativa, que dispara quando nenhuma mensagem válida chega de uma estação por sessenta segundos, e à constatação de revisão F2. A campanha é então executada de novo com a mesma semente para confirmar a mudança.

### 40.6 Erros comuns e limites

- Modelos de falhas limitados ao que o projetista esperava.
- Sem oráculo, de modo que os resultados não podem ser julgados.
- Campanhas sem semente.
- Tratar "nenhuma falha silenciosa observada" como prova.
- Não executar a campanha de novo depois das correções.

A primeira campanha do TMRP mostrou o primeiro erro: os descartes eram silenciosos porque os projetistas nunca listaram a perda de dados como uma falha que o receptor deveria perceber. Executar de novo depois de acrescentar o alarme de estação inativa é o modo como a correção é confirmada. Sua semente é registrada, de modo que a nova execução é comparável. A classe dos descartes agora é mantida em todas as execuções.

### Exercícios — capítulo 40

**EX079 — Detecção de lacunas.** *Objetivo:* fechar a lacuna dos descartes. *Entradas:* Laboratório 15. *Passos:* acrescente a detecção de lacunas (um salto de contador maior que 1 registra `gap`) e execute de novo com a mesma semente; relate quantos eventos de lacuna são registrados e por que o número pode diferir do número de descartes. *Evidência esperada:* código e saída. *Rubrica:* 3 = implementado corretamente; explica que descartes consecutivos produzem um único evento de lacuna e que repetições e mensagens rejeitadas também afetam a continuidade do contador; 2 = implementado, sem explicação; 1 = não executado; 0 = nada.

**EX080 — Estenda o modelo de falhas.** *Objetivo:* acrescentar falhas. *Entradas:* Laboratório 15. *Passos:* acrescente duas classes de falha — reordenação (trocar duas mensagens consecutivas) e reinício do receptor (zerar `state`) —, defina os oráculos, execute e relate as falhas silenciosas. *Evidência esperada:* código, oráculos e resultados. *Rubrica:* 3 = a reordenação faz a mensagem anterior ser rejeitada como repetição (aceitável ou não — argumentado), o reinício permite repetições (falha silenciosa), a menos que o estado seja persistido; 2 = uma classe; 1 = sem oráculo; 0 = nada.

### Síntese do capítulo

A injeção de falhas exercita o tratamento de erros que os testes comuns deixam passar. Defina com antecedência o modelo de falhas e o oráculo, use sementes e conte, classifique os resultados e cace as falhas silenciosas. O Laboratório 15 mostra o resultado típico: o controle rejeita o que foi projetado para rejeitar e é cego para o que ninguém listou — aqui, a perda de dados.

<!-- cyberabc:chapter-navigation:start ch-40 -->
### Continue estudando — capítulo 40 de 50

[← Capítulo 39](#ch-39) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 41 →](#ch-41)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-41"></a>

## Capítulo 41 — Infraestrutura crítica e segurança setorial: otimização de sistemas

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) formular o investimento em segurança como um problema de otimização, com objetivos e restrições; (2) resolver problemas pequenos de forma exata e entender por que heurísticas gulosas podem falhar; (3) tratar múltiplos objetivos e a incerteza com análise de Pareto e de sensibilidade; e (4) apresentar os resultados da otimização como apoio à decisão, e não como decisões. Ele se apoia nos capítulos 25, 32 e 36 e prepara o projeto final.

### 41.1 Formulando o problema

Escolha um conjunto de controles $S$ que maximize o benefício $\sum_{c\in S} b_c$ sujeito ao custo $\sum_{c\in S} k_c \le B$. Esse é o problema da mochila 0/1. Os benefícios podem ser a redução da perda anual esperada, a redução de pessoas-hora sem água ou a redução da probabilidade do evento de topo. Problemas reais acrescentam restrições (dependências entre controles, limites de pessoal, fases) e interações (dois controles que tratam do mesmo cenário não somam benefícios). Para a fase 1 do TMRP, os benefícios do Laboratório 16 são estimativas sintéticas da redução da perda anual esperada.

### 41.2 Soluções exatas e heurísticas

Com um punhado de candidatos, enumere todos os subconjuntos ($2^n$). A programação dinâmica resolve problemas da mochila de forma exata, em tempo proporcional a $n \times B$ para custos inteiros. A heurística **gulosa** — escolher pela razão benefício/custo até gastar o orçamento — é rápida e intuitiva, mas pode deixar orçamento sem uso ou perder combinações melhores. Para problemas maiores, os solucionadores de programação inteira são o padrão. O Laboratório 16 mostra a falha da heurística gulosa nos sete candidatos do TMRP. A gulosa deixou orçamento sem uso e perdeu as RTUs de reserva, uma lacuna que a busca exaustiva encontrou de imediato.

### 41.3 Múltiplos objetivos e incerteza

Os investimentos em segurança equilibram custo, redução de risco, operabilidade e outros bens. Uma solução é **ótima de Pareto** se nenhuma outra solução é melhor num objetivo sem ser pior em outro; apresente o conjunto de Pareto, e não uma única resposta ponderada. Os benefícios são estimativas incertas; teste se o conjunto ótimo muda quando os benefícios variam dentro de faixas plausíveis. Escolhas robustas — as que são boas em vários cenários — muitas vezes são preferíveis a escolhas ótimas apenas sob estimativas pontuais. Para o TMRP, a verificação de robustez do EX082 varia cada benefício em vinte por cento e constata que três das catorze execuções mudam o ótimo, de modo que a última parte da carteira é um quase empate.

### 41.4 Interações

Os benefícios raramente são aditivos. A telemetria autenticada e o monitoramento da rede reduzem ambos o risco de comandos forjados; depois que a autenticação está implantada, o benefício adicional do monitoramento para esse cenário é menor. Modele as interações calculando o benefício a partir do modelo de cenários (p. ex., a árvore de falhas) para cada conjunto candidato, em vez de somar números por controle. No Laboratório 16 os benefícios são simplesmente somados, o que é uma simplificação: a telemetria autenticada e o sensor de detecção na rede reduzem ambos o risco de comandos forjados, então seu valor combinado é menor do que a soma. Um modelo melhor recalcula o benefício a partir da árvore de falhas para cada conjunto candidato.

### 41.5 Exemplo resolvido: portfólio da fase 1 do TMRP (sintético)

Sete controles candidatos com custos e benefícios sintéticos, orçamento de 250 mil (Laboratório 16). A gulosa pela razão escolhe os backups off-line, o modo manual local, a telemetria autenticada e o endurecimento da estação de engenharia: custo de 215 mil, benefício de 480 mil. A busca exaustiva encontra um conjunto melhor — telemetria autenticada, modo manual local, backups off-line e RTUs de reserva — com custo de 250 mil e benefício de 530 mil. A gulosa escolheu cedo o barato endurecimento da estação de trabalho e depois não teve como pagar as RTUs de reserva. A equipe apresenta os dois, observa que as estimativas de benefício têm grande incerteza e mostra que, quando cada benefício varia ±20% individualmente, a telemetria autenticada e o modo manual local permanecem em todos os ótimos, enquanto três execuções substituem os backups off-line e as RTUs de reserva pelo gerador de reserva (EX082) — uma verificação de robustez, e não uma prova.

### 41.6 Atividade prática: Laboratório 16

```python
# Lab 16 - choose controls under a budget: exhaustive search beats greedy here (synthetic, offline)
from itertools import combinations
C = {  # control: (cost k$, expected annual loss reduction k$)
    "auth_telemetry": (120, 260), "backup_gen_PS4": (90, 150), "local_manual_mode": (40, 110),
    "offline_backups": (30, 70), "eng_ws_hardening": (25, 40), "ndr_sensor": (100, 120), "spare_rtus": (60, 90)}
B = 250
best = max((s for r in range(len(C)+1) for s in combinations(C, r) if sum(C[c][0] for c in s) <= B),
           key=lambda s: sum(C[c][1] for c in s))
print("optimal:", sorted(best), "cost", sum(C[c][0] for c in best), "benefit", sum(C[c][1] for c in best))
g, spent = [], 0
for c in sorted(C, key=lambda c: C[c][1] / C[c][0], reverse=True):
    if spent + C[c][0] <= B: g.append(c); spent += C[c][0]
print("greedy :", sorted(g), "cost", spent, "benefit", sum(C[c][1] for c in g))
```

Saída esperada:

```text
optimal: ['auth_telemetry', 'local_manual_mode', 'offline_backups', 'spare_rtus'] cost 250 benefit 530
greedy : ['auth_telemetry', 'eng_ws_hardening', 'local_manual_mode', 'offline_backups'] cost 215 benefit 480
```

O ótimo exaustivo gasta todo o orçamento em telemetria autenticada, modo manual local, backups off-line e RTUs de reserva. A gulosa escolhe cedo o endurecimento da estação de trabalho por causa de sua boa razão, deixando dinheiro de menos para as RTUs de reserva e terminando com menos benefício e algum orçamento sem uso. Com sete candidatos, a busca exaustiva é instantânea, então não há razão para aceitar a resposta gulosa; com centenas de candidatos, um solucionador de programação inteira substituiria ambas. Registre os dois resultados. Observe o orçamento sem uso.

### 41.7 Erros comuns e limites

- Somar os benefícios de controles que interagem.
- Apresentar um único ótimo, sem sensibilidade.
- Heurísticas gulosas usadas sem conferi-las com soluções exatas em instâncias pequenas.
- Resultados de otimização apresentados como decisões, e não como insumos para decisões.
- Números de benefício sem base declarada.

O portfólio do TMRP evita o terceiro erro conferindo a gulosa com a busca exaustiva e apresenta os dois resultados, com a verificação de robustez, ao dono da decisão. Cada valor de benefício é rotulado como estimativa sintética, e o resultado é oferecido como apoio à decisão. As interações são registradas.

### Exercícios — capítulo 41

**EX081 — Varredura de orçamento.** *Objetivo:* ver como o ótimo muda com o orçamento. *Entradas:* Laboratório 16. *Passos:* calcule o conjunto ótimo e o benefício para orçamentos de 150, 200, 250, 300 e 350 mil; trace ou tabule o benefício marginal a cada 50 mil adicionais. *Evidência esperada:* tabela. *Rubrica:* 3 = ótimos corretos (execute o código), benefício marginal decrescente observado e interpretado; 2 = um erro; 1 = um único orçamento; 0 = nada.

**EX082 — Robustez.** *Objetivo:* testar a sensibilidade do ótimo. *Entradas:* Laboratório 16. *Passos:* para cada controle, multiplique seu benefício por 0,8 e por 1,2 (os demais inalterados), recalcule o ótimo e relate qualquer mudança. *Evidência esperada:* tabela das 14 execuções. *Rubrica:* 3 = resultados corretos e conclusão sobre a robustez; 2 = parcial; 1 = não executado; 0 = nada.

### Síntese do capítulo

Formule as escolhas de investimento como otimização, com objetivos e restrições explícitos; resolva problemas pequenos de forma exata e desconfie dos atalhos gulosos; modele as interações em vez de somar benefícios; apresente conjuntos de Pareto e a sensibilidade; e ofereça o resultado como apoio estruturado a uma decisão humana.

<!-- cyberabc:chapter-navigation:start ch-41 -->
### Continue estudando — capítulo 41 de 50

[← Capítulo 40](#ch-40) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 42 →](#ch-42)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-42"></a>

## Capítulo 42 — Infraestrutura crítica e segurança setorial: pesquisa aplicada

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) formular uma pergunta de engenharia que exige novas evidências; (2) projetar um pequeno estudo aplicado — experimento em testbed, estudo de simulação ou medição em campo — com controles e reprodutibilidade; (3) usar conjuntos de dados e testbeds públicos de forma responsável; e (4) relatar os resultados com seus limites. Ele é a contrapartida, na engenharia, dos livros de pesquisa de mestrado e doutorado e prepara o projeto final e o trabalho de conclusão (capítulos 44 a 49).

### 42.1 Pesquisa de engenharia versus pesquisa acadêmica

A pesquisa aplicada deste curso responde a uma pergunta de projeto para um sistema específico, com evidências boas o bastante para uma decisão de engenharia. Ela difere do [livro de mestrado](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md), que ensina a projetar e defender um único estudo empírico com revisão ética, e do [livro de doutorado](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md), que pede uma contribuição original ao conhecimento, validada de forma independente. Um estudo de engenharia tem sucesso se muda ou confirma uma decisão de projeto com evidências que um revisor consiga conferir.

### 42.2 Projetando um pequeno estudo

Declare a pergunta e a decisão que ela informa; defina a medição (Capítulo 29); escolha um desenho — comparação de alternativas num testbed, varredura de parâmetros em simulação ou medição de um sistema existente; fixe a análise antes da execução; controle os fatores de confusão (mesma carga, mesmo hardware, mesmas sementes); repita as execuções para medir a variabilidade; e registre tudo para permitir a reprodução ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)). O estudo do detector do TMRP segue esse padrão, com sua regra de análise fixada antes de qualquer execução. Suas sementes são registradas.

### 42.3 Conjuntos de dados e testbeds públicos

Conjuntos de dados e testbeds públicos de segurança industrial permitem experimentos sem tocar na infraestrutura real. O conjunto de dados do testbed Secure Water Treatment (SWaT), descrito por [Goh et al. (2017)](https://doi.org/10.1007/978-3-319-71368-7_8), e a competição BATADAL sobre redes de distribuição de água, relatada por [Taormina et al. (2018)](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969), são amplamente usados. Conheça seus limites: os testbeds são menores e mais limpos do que as plantas reais, os conjuntos de ataques são escolhidos pelos pesquisadores, e o desempenho em benchmarks não se transfere automaticamente. Leia sobre as armadilhas de avaliação antes de alegar resultados ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp); [Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 42.4 Ética e autorização

A pesquisa aplicada em sistemas reais exige a autorização por escrito do proprietário e, quando há pessoas ou dados pessoais envolvidos, revisão ética (Capítulo 10). Resultados que revelam fraquezas de sistemas específicos vão para o proprietário, e não para uma conferência. Para o TMRP, o estudo do detector usa simulação e os dados do próprio historiador da LRWA, sob a autoridade do programa. Qualquer constatação sobre o produto de um fornecedor iria para esse fornecedor, de forma privada, antes que qualquer coisa fosse escrita para um público mais amplo, e nenhuma estação real é usada como objeto experimental.

### 42.5 Exemplo resolvido: vale a pena implantar o detector cumulativo? (sintético)

Pergunta: o TMRP deve implantar em Hollin Hill o detector cumulativo de balanço de massa do Capítulo 17? Decisão informada: implantar, com qual limiar e qual intervalo de recalibração. Desenho do estudo: varredura em simulação sobre os níveis de ruído (0,005–0,02 m), a deriva dos medidores de vazão (0–1%) e os limiares (0,02–0,08 m), 100 execuções com semente por célula, medindo os alarmes falsos por mês e o tempo de detecção para ataques em rampa de 0,01–0,1 m/h. Análise fixada com antecedência: escolher o limiar com menos de um alarme falso por mês no nível de ruído medido e relatar o tempo de detecção nesse limiar. Validação: comparar o ruído simulado com duas semanas de dados do historiador. Limites: modelo de tanque com mistura perfeita; um atacante que controle os medidores de vazão está fora do escopo.

### 42.6 Atividade prática

Implemente uma versão reduzida da §42.5 usando o Laboratório 7: três limiares × três níveis de ruído × 20 sementes; relate os alarmes falsos e os tempos de detecção da rampa numa tabela com a variabilidade. Fixe sua regra de análise antes da execução: por exemplo, escolha o menor limiar sem alarmes falsos nas execuções sem ataque em cada nível de ruído. Defina a semente de cada execução e registre as sementes. Relate o número de alarmes falsos e o tempo de detecção da rampa para cada célula, com sua dispersão entre as sementes, e não apenas a média. Depois declare um limite do estudo reduzido, como medidores de vazão perfeitos, e a direção em que ele enviesa seus resultados.

### 42.7 Erros comuns e limites

- Estudos sem uma decisão que informem.
- Análise escolhida depois de ver os resultados.
- Execuções únicas relatadas como resultados.
- Desempenho em benchmarks alegado como transferível para plantas reais.
- Fraquezas de sistemas reais publicadas sem coordenação.

O estudo do detector cumulativo no exemplo resolvido evita cada um desses erros: ele informa uma decisão de implantação, fixa sua regra de análise com antecedência, usa cem execuções por célula, valida seu modelo de ruído contra duas semanas de dados do historiador da LRWA e declara que um atacante que controle os medidores de vazão está fora do escopo.

### Exercícios — capítulo 42

**EX083 — Protocolo do estudo.** *Objetivo:* escrever um protocolo pré-especificado. *Entradas:* §42.5. *Passos:* escreva um protocolo de uma página: pergunta, decisão, desenho, medições, regra de análise, validação, limites. *Evidência esperada:* protocolo. *Rubrica:* 3 = completo, regra de análise fixada com antecedência, validação contra dados reais de ruído, limites honestos; 2 = análise vaga; 1 = sem decisão; 0 = nada.

**EX084 — Limites dos conjuntos de dados.** *Objetivo:* avaliar a transferência a partir de um testbed. *Entradas:* um fornecedor alega 99% de detecção num conjunto de dados público de um testbed de água. *Passos:* liste cinco perguntas que você faria antes de aceitar isso para a LRWA. *Evidência esperada:* lista. *Rubrica:* 3 = taxa-base e taxa de alarmes falsos em operação, realismo do conjunto de ataques, protocolo de avaliação (ajuste de pontos, vazamento de dados), escala/diferença da planta, adaptação a adversários; 2 = três boas perguntas; 1 = genérico; 0 = nada.

### Síntese do capítulo

A pesquisa de engenharia responde a uma pergunta de projeto com evidências conferíveis. Pré-especifique o estudo, controle os fatores de confusão, repita as execuções, use os testbeds públicos dentro de seus limites, obtenha autorização para qualquer coisa real e relate os resultados com suas fronteiras.

<!-- cyberabc:chapter-navigation:start ch-42 -->
### Continue estudando — capítulo 42 de 50

[← Capítulo 41](#ch-41) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 43 →](#ch-43)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-43"></a>

## Capítulo 43 — Prática na indústria ou no serviço público

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) planejar e concluir um estágio de prática supervisionada num operador, fornecedor, integrador, regulador ou órgão público; (2) trabalhar dentro das regras de autorização, confidencialidade e segurança do estágio; (3) manter um diário de prática reflexiva que ligue o trabalho observado aos métodos do curso; e (4) produzir um relatório de estágio útil para a organização anfitriã e seguro para compartilhar. Ele aplica o curso inteiro à prática real e prepara o projeto final.

### 43.1 O propósito da prática

A prática expõe as restrições que os livros didáticos suavizam: ciclos de compras, pessoal, equipamentos legados, prazos regulatórios, acordos sindicais, orçamentos e a distância entre o procedimento e a prática. Engenheiros que já viram uma sala de controle à noite projetam de modo diferente dos que não viram. O caso do TMRP neste livro é sintético; um estágio é onde você vê o quanto as restrições de uma concessionária real diferem dele. Observe como as decisões são de fato tomadas, quem é dono do risco operacional e quanto tempo leva uma mudança simples, porque essas observações vão moldar o modo como você define o escopo do seu projeto final.

### 43.2 Acordo de estágio

Antes de começar, acorde por escrito: o supervisor na organização anfitriã e o supervisor acadêmico; o escopo do trabalho; os sistemas que você pode acessar e como; a confidencialidade e o tratamento dos dados; a integração de segurança; o que você pode publicar no seu relatório; e como as constatações incidentais são tratadas. Você trabalha sob a autoridade e as políticas da organização anfitriã; seu curso não lhe dá autoridade para testar ou acessar coisa alguma. A organização anfitriã do exemplo resolvido aprovou o texto do relatório final antes que ele saísse da organização. Acordar a regra de publicação com antecedência evitou qualquer discussão sobre o que o relatório poderia incluir.

### 43.3 Diário de prática reflexiva

Mantenha um diário semanal com quatro entradas: **observação** (o que você viu, sem julgamento), **conexão** (a que método de qual capítulo ela se relaciona), **diferença** (onde a prática divergiu do método, e por que isso fazia sentido localmente) e **pergunta** (o que você investigaria). A reflexão transforma a experiência em julgamento transferível. Não registre detalhes sensíveis no diário; registre padrões. No exemplo resolvido abaixo, a observação do estudante sobre as versões de firmware segue exatamente esse padrão e não contém nomes de dispositivos. As entradas semanais mantêm o hábito.

### 43.4 Trabalho comum no estágio

Tarefas típicas para um estudante de engenharia: atualizar um inventário de ativos e conciliá-lo com os dados da rede (Capítulo 22); redigir ou revisar um playbook (Capítulo 37); apoiar uma avaliação de riscos (Capítulo 24); preparar um procedimento de teste para um comissionamento (Capítulo 31); avaliar alertas contra o inventário (Capítulo 12). Cada uma produz uma entrega para a organização anfitriã e um artefato de aprendizagem sanitizado para o curso. O estudante do exemplo resolvido fez a primeira tarefa, conciliando um registro de ativos com os dados de monitoramento. A entrega do estudante à organização anfitriã foi uma mudança no formulário de ordem de serviço.

### 43.5 Exemplo resolvido: um relatório de estágio sanitizado (sintético)

Um estudante estagiando numa distribuidora regional de eletricidade (sintética) escreve uma seção do relatório: "Observação: as versões de firmware das RTUs das subestações no registro de ativos diferiam das observadas no monitoramento passivo em 18% de uma amostra de 60 dispositivos. Conexão: a conciliação de múltiplas fontes de inventário do Capítulo 22. Diferença: o registro é atualizado nas visitas anuais de manutenção, enquanto as mudanças de firmware ocorrem durante reparos não programados; a equipe de campo não tinha um modo simples de relatar as mudanças. Recomendação (aceita pela organização anfitriã): acrescentar um campo de firmware ao formulário de ordem de serviço de reparo e uma conciliação trimestral com os dados de monitoramento." Não aparecem nomes, endereços nem localizações de dispositivos; a organização anfitriã aprovou o texto.

### 43.6 Atividade prática

Redija um acordo de estágio para um estágio hipotético de quatro meses numa concessionária de água, cobrindo todos os itens da §43.2. Use uma concessionária de água como a LRWA como modelo mental, mas mantenha o acordo geral o bastante para que uma organização anfitriã real possa assiná-lo. Nomeie os dois supervisores pelo papel, liste os sistemas que você pode ver e como, e declare com clareza que você não pode testar nem varrer coisa alguma. Diga como as constatações incidentais são relatadas e quem aprova seu relatório antes que ele saia da organização anfitriã. Acrescente uma data para a integração de segurança e os dados que você pode levar consigo, que em geral devem ser nenhum.

### 43.7 Erros comuns e limites

- Começar sem um escopo e um acordo de tratamento de dados por escrito.
- Tratar o acesso do estágio como permissão para explorar.
- Diários contendo detalhes sensíveis.
- Relatórios que criticam a organização anfitriã sem entender as restrições locais.

O exemplo resolvido evita cada um desses erros: seu escopo foi acordado, seu diário registrou padrões, e não detalhes de dispositivos, e sua recomendação levou em conta por que o registro ficava atrás dos reparos. Sua crítica ao registro foi formulada em torno de uma lacuna de processo, e não da equipe de campo, e a organização anfitriã aceitou a recomendação porque ela se encaixava no modo como os reparos eram de fato feitos.

### Exercícios — capítulo 43

**EX085 — Acordo de estágio.** *Objetivo:* definir as fronteiras do estágio. *Entradas:* §43.6. *Passos:* escreva o acordo. *Evidência esperada:* uma a duas páginas. *Rubrica:* 3 = todos os itens da §43.2, proibição explícita de testes fora do escopo, caminho para as constatações incidentais, aprovação da publicação; 2 = um ausente; 1 = genérico; 0 = nada.

**EX086 — Entrada reflexiva.** *Objetivo:* refletir de forma útil. *Entradas:* uma observação: "os operadores mantinham um caderno de papel com as mudanças de setpoint ao lado do log do SCADA". *Passos:* escreva uma entrada de diário em quatro partes. *Evidência esperada:* entrada. *Rubrica:* 3 = observação neutra, ligação com os capítulos 13/37, racionalidade local (confiança, quedas, passagem de turno), pergunta investigativa; 2 = julgadora; 1 = apenas a observação; 0 = nada.

### Síntese do capítulo

A prática ensina as restrições que moldam os projetos reais. Trabalhe dentro de um acordo por escrito e da autoridade da organização anfitriã, registre observações, conexões, diferenças e perguntas sem detalhes sensíveis, e entregue valor à organização anfitriã numa forma segura para compartilhar.

<!-- cyberabc:chapter-navigation:start ch-43 -->
### Continue estudando — capítulo 43 de 50

[← Capítulo 42](#ch-42) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 44 →](#ch-44)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-44"></a>

## Capítulo 44 — Projeto final de engenharia I

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) definir um projeto final com patrocinador, escopo, requisitos e critérios de aceitação; (2) planejá-lo com cronograma, registro de riscos e plano de verificação; (3) montar um ambiente de engenharia reprodutível; e (4) ser aprovado numa revisão preliminar de projeto. O projeto final integra o curso num único sistema construído e verificado e continua pelos capítulos 45 a 50.

### 44.1 O que é um projeto final

Um projeto final é um projeto de engenharia substancial no qual o estudante projeta, constrói e verifica um sistema que atende a requisitos reais ou realistas sob restrições. Neste curso, o projeto final precisa: tratar de uma necessidade de segurança ou resiliência de infraestrutura crítica; incluir um artefato funcional (software, configuração, testbed ou protótipo); incluir análises (ameaças/falhas, desempenho, confiabilidade); e ser verificado contra requisitos declarados. O projeto final continua o caso do TMRP, a menos que seu supervisor aprove outro caso sintético ou autorizado. O exemplo resolvido abaixo segue o TMRP: telemetria autenticada segura diante de reinícios para as RTUs legadas da PS1 e da PS2.

### 44.2 Definição do escopo

Um bom escopo de projeto final é estreito o bastante para ser concluído e profundo o bastante para exigir engenharia de verdade. Exemplos: um gateway de telemetria autenticada com verificação por injeção de falhas; um detector baseado em resíduos com um estudo de simulação validado; uma ferramenta de orquestração da recuperação com um ensaio de restauração medido; uma ferramenta de verificação da segmentação com um modelo de política. Escreva um escopo de uma página: necessidade, partes interessadas, entregas, itens fora do escopo, restrições e critérios de aceitação. O escopo do projeto final do TMRP no exemplo resolvido abaixo cabe numa página e deixa de fora o hardware real das RTUs e a rede da operadora.

### 44.3 Planejamento

Planeje com uma estrutura analítica do trabalho, um cronograma com marcos (revisão preliminar de projeto, revisão crítica de projeto, verificação concluída, rascunho do trabalho de conclusão, defesa), um registro de riscos (técnicos, de cronograma, de acesso, de competências) e um plano de verificação que rastreie os requisitos até os testes. Mantenha um diário semanal e atualize o registro de riscos mensalmente. Para o projeto final do TMRP, o cronograma de doze semanas coloca a revisão preliminar de projeto nas primeiras semanas e a revisão independente antes da verificação. Seu registro de riscos inclui a chance de a segurança diante de reinícios se mostrar mais difícil do que o esperado, o que, como mostra depois o resumo da verificação, foi o que aconteceu quando o receptor aceitou repetições após um reinício.

### 44.4 Ambiente

Monte controle de versões, um rastreador de tarefas, um build reprodutível (dependências fixadas ou apenas a biblioteca padrão), testes automatizados e um diretório de resultados em que cada resultado seja armazenado com o commit, as sementes e o ambiente que o produziram. Para o projeto final do TMRP, o gateway usa apenas a biblioteca padrão do Python, então não há dependências a fixar, e cada resultado de campanha é armazenado com sua semente e seu commit. É essa disciplina que permite ao dossiê posterior listar um hash e uma versão para cada resultado.

### 44.5 Exemplo resolvido: escopo do projeto final (sintético)

*Título:* Telemetria autenticada segura diante de reinícios para RTUs legadas. *Necessidade:* N2/N3 do TMRP. *Entregas:* software do gateway (biblioteca padrão do Python), arcabouço de bancada, campanha de injeção de falhas, procedimento de rotação de chaves, trabalho de conclusão. *Fora do escopo:* hardware real das RTUs; rede da operadora. *Restrições:* 12 semanas; dados sintéticos. *Aceitação:* R1, R2 (incluindo reinícios) e R7 verificados na bancada; zero falhas silenciosas numa campanha com semente de 10.000 mensagens em sete classes de falha; rotação de chaves sem perda de telemetria demonstrada. Cada critério de aceitação corresponde a um requisito ou a uma demonstração, para que a revisão crítica de projeto possa conferi-los um a um.

### 44.6 Atividade prática

Escreva o escopo e o plano do seu projeto final e realize uma revisão preliminar de projeto com seu supervisor e um colega. Baseie seu escopo no modelo de uma página: necessidade, partes interessadas, entregas, itens fora do escopo, restrições e critérios de aceitação. Depois prepare um plano curto, com marcos e um registro de riscos. Na revisão, peça ao supervisor e ao colega que contestem sobretudo os critérios de aceitação, porque um critério que não pode ser testado vai causar problemas na revisão crítica de projeto. Registre as constatações deles e suas respostas.

### 44.7 Erros comuns e limites

- Escopos amplos demais ("proteger a concessionária").
- Nenhum critério de aceitação.
- Verificação planejada por último.
- Ambientes não reprodutíveis.

O rascunho de escopo do EX087 mostra os dois primeiros erros: proteger concessionárias de água com um sistema de IA não tem fronteira nem critérios de aceitação. O escopo do projeto final do TMRP os evita nomeando um gateway, três requisitos e uma campanha medida. Seu plano de verificação foi escrito junto com o escopo, e seu ambiente usa apenas a biblioteca padrão, com execuções com semente, de modo que cada resultado pode ser reproduzido. Seus marcos têm datas.

### Exercícios — capítulo 44

**EX087 — Crítica de escopo.** *Objetivo:* estreitar um escopo. *Entradas:* rascunho de escopo "Construir um sistema de IA para proteger concessionárias de água contra ciberataques". *Passos:* liste quatro problemas e reescreva o escopo em uma página. *Evidência esperada:* crítica e reescrita. *Rubrica:* 3 = problemas (sem limites, sem requisitos, sem dados, sem aceitação) e uma reescrita viável e verificável; 2 = reescrita vaga; 1 = apenas a crítica; 0 = nada.

**EX088 — Registro de riscos.** *Objetivo:* planejar para os riscos do projeto. *Entradas:* §44.5. *Passos:* escreva cinco riscos do projeto com probabilidade, impacto, mitigação e gatilho. *Evidência esperada:* tabela. *Rubrica:* 3 = riscos realistas (aumento descontrolado do escopo, projeto da segurança diante de reinícios mais difícil do que o esperado, fidelidade da bancada, tempo, disponibilidade do supervisor) com gatilhos concretos; 2 = sem gatilhos; 1 = genérico; 0 = nada.

### Síntese do capítulo

Um projeto final é um sistema com escopo definido, construído e verificado. Defina a necessidade, as entregas, as restrições e os critérios de aceitação; planeje marcos, riscos e verificação desde o início; e torne o ambiente reprodutível para que cada resultado possa ser rastreado e executado de novo.

<!-- cyberabc:chapter-navigation:start ch-44 -->
### Continue estudando — capítulo 44 de 50

[← Capítulo 43](#ch-43) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 45 →](#ch-45)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-45"></a>

## Capítulo 45 — Revisão independente de projeto

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) conduzir uma revisão técnica independente do projeto de outra equipe usando critérios estruturados; (2) escrever constatações específicas, evidenciadas e acionáveis; (3) classificar as constatações por gravidade e recomendar encaminhamentos; e (4) receber uma revisão do seu próprio projeto e respondê-la. Ele aplica o rigor ao estilo de Fagan (Capítulo 14) a projetos inteiros e prepara o Projeto final II.

### 45.1 Independência e propósito

Um revisor independente não trabalhou no projeto e não se reporta a seus autores. A independência pega erros que os autores não conseguem ver — pressupostos compartilhados, pontos cegos, verificação otimista. O propósito é melhorar o projeto e a decisão sobre ele, e não marcar pontos. Para o TMRP, o revisor do dossiê do projeto final é alguém que não trabalhou no gateway e não se reporta a seus autores. Essa independência é a razão pela qual o revisor percebeu que o caso de garantia citava o T3 como aprovado enquanto a matriz ainda o registrava como reprovado, uma inconsistência pela qual os autores tinham passado muitas vezes sem notar.

### 45.2 Critérios de revisão

Revise contra: os requisitos (completos, verificáveis, rastreados); a arquitetura (orientada pelas consequências, comportamento diante de falhas e ataques analisado); os controles (especificados com desempenho, camadas independentes); as análises (pressupostos declarados, números consistentes); a verificação (o plano cobre os requisitos, reprovações tratadas com honestidade); as operações (procedimentos, treinamento, recuperação); a manutenibilidade; e o caso de garantia (alegações apoiadas, derrotadores declarados). Cada critério corresponde a um capítulo deste livro: requisitos ao Capítulo 21, arquitetura ao Capítulo 26, controles ao Capítulo 27, verificação aos capítulos 30 e 40, operações ao Capítulo 37 e o caso de garantia ao Capítulo 35. Os revisores do dossiê do TMRP usaram essa lista como checklist.

### 45.3 Escrevendo as constatações

Uma constatação declara: o que foi observado (com uma referência ao documento ou à evidência), por que importa (consequência), o critério em que falha e uma recomendação. Gravidade: **crítica** (a alegação não pode ser apoiada, ou há risco à segurança operacional), **maior** (lacuna significativa que exige mudança antes da aprovação), **menor** (melhoria), **observação** (nenhuma mudança exigida). Evite constatações vagas ("a segurança parece fraca") e o projeto pelo revisor (prescrever sua solução favorita quando várias serviriam). As constatações do TMRP no exemplo resolvido abaixo seguem essa forma. A F4, sobre a fração da bateria, é menor porque a alegação sobrevive com uma fonte acrescentada.

### 45.4 Respondendo à revisão

Os autores respondem a cada constatação: aceitar (com mudança), rejeitar (com raciocínio e evidências) ou adiar (com dono e data). O revisor confere as respostas e encerra ou escalona as constatações. Divergências que não podem ser resolvidas vão para o dono da decisão, com as duas posições registradas. Para o TMRP, os autores aceitaram a F2 e acrescentaram o alarme de estação inativa, e aceitaram a F3 relatando R6 como não atendido e orçando opções no ADR-015. Cada resposta nomeou um dono, e o revisor conferiu a campanha executada de novo antes de encerrar a F2.

### 45.5 Exemplo resolvido: constatações sobre o dossiê do TMRP (sintético)

- **F1 (crítica):** a subalegação C2 do caso de garantia cita o T3 como aprovado, mas a matriz de rastreabilidade (Laboratório 14) registra o T3 como reprovado, e o novo teste na v2 não está registrado. *Recomendação:* registrar as evidências do novo teste ou rebaixar a alegação.
- **F2 (maior):** o receptor não alarma diante de dados ausentes (descartes silenciosos no Laboratório 15); R7 não pode ser alegado para eventos de perda de dados. *Recomendação:* acrescentar o alarme de estação inativa e executar de novo a campanha.
- **F3 (maior):** o ensaio de restauração (Capítulo 47) mostra 12 h contra as 8 h de R6; o dossiê declara R6 como atendido. *Recomendação:* relatar R6 como não atendido e apresentar opções.
- **F4 (menor):** o dimensionamento das baterias usa uma fração utilizável de 0,6 sem fonte; cite os dados do fabricante das baterias.
- **F5 (observação):** a avaliação ponderada dos conceitos (§25.4) é sensível ao peso da operabilidade; a decisão continua defensável.

### 45.6 Atividade prática

Troque dossiês de projeto final com outro estudante, revise segundo os critérios da §45.2 e escreva pelo menos seis constatações com gravidades. Escolha um revisor que não tenha ajudado no seu projeto. Para cada constatação, inclua a observação com sua referência, a consequência, o critério em que falha e uma recomendação. Use os quatro níveis de gravidade com honestidade. Depois troquem de papéis e responda às constatações sobre seu próprio dossiê com aceitar, rejeitar ou adiar, dando evidências para cada rejeição. Guarde os dois registros no seu dossiê. Atenha-se às evidências.

### 45.7 Erros comuns e limites

- Revisões feitas por pessoas que ajudaram no projeto.
- Constatações vagas ou sem evidências.
- Inflação ou deflação da gravidade.
- Autores que rejeitam constatações sem evidências.

A revisão do TMRP evitou esses erros: o revisor era independente, cada constatação citava um documento, as gravidades correspondiam às consequências, e as respostas dos autores eram apoiadas em evidências e conferidas antes do encerramento. A F5 foi mantida como observação, sem ser inflada. A F1 foi classificada como crítica porque a alegação não podia ser apoiada tal como escrita, e não porque o erro fosse constrangedor, e os autores não rejeitaram nenhuma constatação sem evidências que apoiassem a rejeição.

### Exercícios — capítulo 45

**EX089 — Reescreva constatações fracas.** *Objetivo:* escrever constatações acionáveis. *Entradas:* "a gestão de chaves não está ótima"; "os testes parecem incompletos"; "eu usaria OPC UA no lugar". *Passos:* reescreva cada uma como uma constatação adequada ou explique por que deveria ser retirada. *Evidência esperada:* três reescritas. *Rubrica:* 3 = observação específica, consequência, critério, recomendação; a terceira retirada ou reformulada como preocupação baseada em requisitos; 2 = uma vaga; 1 = mera troca de palavras; 0 = nada.

**EX090 — Responda à F2 e à F3.** *Objetivo:* responder à revisão. *Entradas:* §45.5. *Passos:* escreva as respostas dos autores à F2 e à F3, com encaminhamentos, mudanças, donos e datas. *Evidência esperada:* duas respostas. *Rubrica:* 3 = F2 aceita com mudança de projeto e novo teste, F3 aceita com relato honesto e opções (paralelizar a recuperação, imagens pré-construídas, revisar o requisito com acordo das partes interessadas); 2 = defensiva; 1 = rejeita; 0 = nada.

### Síntese do capítulo

A revisão independente encontra o que os autores não conseguem ver. Revise contra critérios explícitos, escreva constatações específicas, evidenciadas e acionáveis, com gravidades honestas, e responda a cada constatação com aceitar, rejeitar ou adiar — registrado e conferido.

<!-- cyberabc:chapter-navigation:start ch-45 -->
### Continue estudando — capítulo 45 de 50

[← Capítulo 44](#ch-44) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 46 →](#ch-46)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-46"></a>

## Capítulo 46 — Projeto final de engenharia II

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) concluir a implementação do artefato do projeto final; (2) executar o plano de verificação completo e registrar os resultados; (3) encerrar as constatações da revisão; e (4) ser aprovado numa revisão crítica de projeto com evidências. Ele continua o Capítulo 44 depois da revisão independente e prepara o ensaio de falha e recuperação (Capítulo 47).

### 46.1 Concluindo a construção

Congele o escopo: novas funcionalidades agora ameaçam a verificação. Encerre primeiro as constatações da revisão que exigem mudanças de projeto. Mantenha o ramo principal sempre aprovado em seus testes; marque com uma tag a versão que entra na verificação final. Para o projeto final do TMRP, o escopo foi congelado depois da revisão independente. O alarme de estação inativa da F2 foi a mudança de projeto feita antes que a versão marcada entrasse na verificação final; todas as ideias posteriores foram para uma lista de trabalhos futuros. A correção do reinício veio depois, como uma correção encontrada pela própria verificação, que é o único tipo de mudança permitido depois do congelamento. O ramo principal permaneceu verde.

### 46.2 Executando a verificação

Execute o plano de verificação completo contra a versão marcada: testes unitários, de integração, baseados em propriedades e de injeção de falhas (capítulos 30 e 40). Registre cada resultado com a versão, a semente e o ambiente. Para qualquer reprovação: registre, analise, corrija, execute de novo, registre de novo. Não sobrescreva os resultados anteriores; o histórico é evidência. Para o projeto final do TMRP, a falha do receptor em rejeitar repetições depois de um reinício foi registrada, corrigida com a persistência do último contador por estação e testada de novo, com os dois resultados mantidos. A versão marcada foi a testada. Sua semente foi registrada.

### 46.3 Revisão crítica de projeto

Na revisão crítica de projeto, a banca confere: requisitos atendidos, com evidências; constatações da revisão encerradas ou encaminhadas; riscos residuais declarados e com dono; operações e manutenção preparadas; e prontidão para o ensaio. Leve a matriz de rastreabilidade, os resultados da verificação, o registro de constatações e o caso de garantia. Para o TMRP, a banca viu o resumo da verificação abaixo. Ele inclui a falha no reinício e sua correção, o alarme de estação inativa acrescentado depois da F2 e a demonstração da rotação de chaves. Com a F1 a F3 encerradas ou encaminhadas e R6 relatado com honestidade, a banca pôde tomar uma decisão explícita de prontidão para o ensaio, em vez de uma suposição.

### 46.4 Exemplo resolvido: resumo da verificação do projeto final (sintético)

| Requisito | Testes | Resultado | Notas |
|---|---|---|---|
| R1 | T1, T2, campanha (classe corrupção) | Aprovado | 0 falhas silenciosas em 10.000 mensagens |
| R2 | T2, testes de reinício (dos dois lados), campanha (repetição, reordenação, reinício) | Aprovado após correção | O reinício do receptor inicialmente aceitava repetições; corrigido com a persistência do último contador por estação; testado de novo |
| R7 | T5, teste do alarme de estação inativa | Aprovado após correção | Detecção de descartes acrescentada depois da F2 |
| Rotação de chaves | Demonstração | Aprovado | Janela de sobreposição de 10 min com as duas chaves aceitas, depois a chave antiga revogada |

A falha no reinício foi encontrada pelo modelo de falhas estendido do EX080 — um retorno direto do investimento no laboratório de verificação.

### 46.5 Atividade prática

Execute seu plano de verificação completo e produza a tabela-resumo com links para os resultados brutos. Para cada requisito, informe os testes, o resultado e qualquer correção, como no resumo do TMRP. Mantenha os resultados reprovados com suas datas e as correções que se seguiram, e ligue cada linha aos arquivos de resultados brutos, com suas sementes e versões. Se um teste não foi executado, diga isso na tabela em vez de deixá-la em branco. A tabela deve permitir a um revisor rastrear qualquer alegação até um arquivo num único passo.

### 46.6 Erros comuns e limites

- Acrescentar funcionalidades durante a verificação.
- Sobrescrever resultados reprovados com aprovações posteriores.
- Entrar na revisão crítica de projeto com constatações críticas em aberto.

O projeto final do TMRP evitou esses erros congelando o escopo depois da revisão, mantendo a falha no reinício no registro ao lado de sua aprovação posterior e encerrando a F1 a F3 antes da revisão crítica de projeto. Os resultados reprovados permaneceram no registro com as correções que se seguiram, para que os revisores pudessem ver como cada aprovação foi conquistada. Nenhuma funcionalidade foi acrescentada durante a verificação. As constatações em aberto foram encerradas primeiro.

### Exercícios — capítulo 46

**EX091 — Projeto da rotação.** *Objetivo:* projetar a rotação de chaves sem perdas. *Entradas:* §46.4. *Passos:* descreva passo a passo o protocolo de rotação, incluindo como o receptor sabe qual chave tentar, a janela de sobreposição, o tratamento de falhas e a revogação. *Evidência esperada:* procedimento. *Rubrica:* 3 = ID da chave no cabeçalho autenticado, receptor aceita as duas chaves durante a janela, os contadores continuam, reversão se a nova chave falhar, chave antiga revogada e destruída; 2 = sem ID da chave; 1 = "trocar a chave"; 0 = nada.

**EX092 — Decisão de prontidão.** *Objetivo:* julgar a prontidão. *Entradas:* todos os requisitos aprovados, exceto uma constatação menor sobre a documentação e uma constatação maior em aberto de que o limiar do alarme de estação inativa (60 s) produz dois alarmes falsos por dia durante o congestionamento da LTE. *Passos:* recomende prosseguir / prosseguir com condições / não prosseguir com o ensaio, com o raciocínio. *Evidência esperada:* recomendação. *Rubrica:* 3 = prosseguir com condições (estudo de ajuste do limiar durante o ensaio, operadores informados), raciocínio sobre a consequência dos alarmes falsos versus uma perda de dados não detectada; 2 = sem condições; 1 = sem raciocínio; 0 = nada.

### Síntese do capítulo

Congele o escopo, encerre as constatações, verifique por completo a versão marcada e mantenha o histórico de reprovações como evidência. Entre na revisão crítica de projeto com rastreabilidade, resultados, constatações e o caso de garantia, e saia dela com uma decisão explícita de prontidão.

<!-- cyberabc:chapter-navigation:start ch-46 -->
### Continue estudando — capítulo 46 de 50

[← Capítulo 45](#ch-45) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 47 →](#ch-47)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-47"></a>

## Capítulo 47 — Ensaio de falha e recuperação

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) projetar um ensaio controlado de falha e recuperação, com fronteiras de segurança; (2) calcular caminhos críticos e comparar os tempos de recuperação planejados e medidos; (3) observar e registrar o desempenho humano e técnico durante o ensaio; e (4) transformar os resultados do ensaio em situação dos requisitos e mudanças de projeto. Ele valida os requisitos de recuperação (R6) e prepara o dossiê de evidências (Capítulo 48).

### 47.1 Por que ensaiar a recuperação

Uma capacidade de recuperação que não foi exercitada é uma esperança. Backups que não foram restaurados podem estar incompletos; procedimentos que não foram seguidos podem estar errados; tempos que não foram medidos são palpites. A [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) trata do planejamento de contingência, incluindo testes, treinamento e exercícios. O próprio ensaio do TMRP mostrou por quê: a meta de restauração de oito horas de R6 parecia razoável até que o caminho crítico fosse medido. Medi-lo era o objetivo.

### 47.2 Projetando o ensaio

Defina o cenário (p. ex., servidores SCADA declarados comprometidos às 02:00), os objetivos (restaurar a operação remota a partir dos backups off-line; manter o abastecimento em modo local o tempo todo), as fronteiras de segurança (ensaio no ambiente de teste ou numa janela planejada com a operação local guarnecida; critérios de interrupção), os observadores e as medições (horário de cada tarefa, desvios do procedimento, decisões). O ensaio do TMRP usou o cenário de servidores SCADA declarados comprometidos, com o abastecimento mantido em modo local o tempo todo. Os observadores registraram o tempo de cada tarefa e todo desvio do procedimento.

### 47.3 Caminho crítico

As tarefas de recuperação têm durações e dependências. O **caminho crítico** é a cadeia mais longa de tarefas dependentes; ele define o tempo mínimo de recuperação. As tarefas fora do caminho crítico têm **folga**. Encurtar a recuperação significa encurtar as tarefas do caminho crítico ou quebrar dependências — e não acelerar tarefas que têm folga. No ensaio do TMRP, a troca de chaves das RTUs tinha seis horas de folga. Acelerá-la não teria mudado nada. Apenas a geração de imagens, a reconstrução e a restauração da configuração definiram o resultado de doze horas, e é por isso que toda opção para atender a R6 visa uma dessas três tarefas, como imagens de reserva pré-construídas ou a geração de imagens em hardware de reserva.

### 47.4 Exemplo resolvido: ensaio de recuperação do TMRP (sintético)

O plano do ensaio (Laboratório 17): isolar (1 h); estabelecer a operação manual (1 h); geração de imagens forenses dos servidores SCADA (3 h); reconstruir o SCADA a partir de mídia off-line (4 h); restaurar a configuração (2 h); trocar as chaves das RTUs (3 h, em paralelo); verificar os setpoints (1 h); retomar o controle remoto (1 h). O caminho crítico passa pela geração de imagens forenses, pela reconstrução e pela restauração da configuração: o controle remoto volta em 12 h, contra as 8 h de R6. A troca de chaves tem 6 h de folga — acelerá-la não leva a nada. Opções para atender às 8 h: imagens de SCADA de reserva pré-construídas (reconstrução de 4 h → 1 h); geração de imagens em paralelo com a reconstrução, em hardware de reserva (remove 3 h do caminho); ou acordo com as partes interessadas para que R6 seja de 12 h, porque o abastecimento é mantido em modo local o tempo todo. O ensaio também mediu que a operação manual foi estabelecida em 50 minutos, atendendo ao requisito de 1 h.

### 47.5 Atividade prática: Laboratório 17

```python
# Lab 17 - recovery critical path versus the restoration target (synthetic TMRP trial plan, offline)
T = {  # task: (hours, prerequisites)
    "isolate": (1, []), "manual_ops": (1, ["isolate"]), "forensic_image": (3, ["isolate"]),
    "rebuild_scada": (4, ["forensic_image"]), "restore_config": (2, ["rebuild_scada"]),
    "rekey_rtus": (3, ["isolate"]), "verify_setpoints": (1, ["restore_config", "rekey_rtus"]),
    "resume_remote": (1, ["verify_setpoints"])}
ef, prev = {}, {}
def finish(t):
    if t not in ef:
        d, ps = T[t]; start = max((finish(p) for p in ps), default=0)
        prev[t] = max(ps, key=finish) if ps else None; ef[t] = start + d
    return ef[t]
end = finish("resume_remote"); path, n = [], "resume_remote"
while n: path.append(n); n = prev[n]
print("restore remote control at", end, "h; critical path:", " -> ".join(reversed(path)))
print("slack of rekey_rtus:", finish("restore_config") - finish("rekey_rtus"), "h; target 8 h met:", end <= 8)
```

Saída esperada:

```text
restore remote control at 12 h; critical path: isolate -> forensic_image -> rebuild_scada -> restore_config -> verify_setpoints -> resume_remote
slack of rekey_rtus: 6 h; target 8 h met: False
```

A saída confirma o exemplo resolvido: o controle remoto volta depois de doze horas porque a geração de imagens, a reconstrução e a restauração da configuração correm em série, e a troca de chaves termina seis horas antes de ser necessária. Mude o plano como pede o EX093 e observe o caminho crítico passar para outra cadeia. O laboratório não inclui a operação manual no caminho até o controle remoto, porque ela corre em paralelo; o ensaio a mediu separadamente, em cinquenta minutos, contra o requisito de uma hora. Guarde as duas saídas.

### 47.6 Erros comuns e limites

- Recuperação testada apenas no papel.
- Ensaios sem critérios de interrupção nem pessoal de segurança.
- Melhorar tarefas que têm folga.
- Resultados de ensaio relatados como aprovações quando o requisito não foi atendido.
- Preservação forense pulada para ganhar tempo, sem uma decisão.

O ensaio do TMRP evitou o quarto erro relatando R6 como não atendido em doze horas, e manteve a geração de imagens forenses em vez de pulá-la sem uma decisão. Os critérios de interrupção e o pessoal local foram definidos antes do início do ensaio, e as opções para atender a R6 visam apenas tarefas do caminho crítico.

### Exercícios — capítulo 47

**EX093 — Encurte o caminho.** *Objetivo:* usar o caminho crítico. *Entradas:* Laboratório 17. *Passos:* (1) faça `rebuild_scada` depender apenas de `isolate` (hardware de reserva, geração de imagens em paralelo) e recalcule; (2) além disso, reduza `rebuild_scada` a 1 h (imagem de reserva) e recalcule; relate o novo caminho crítico a cada vez. *Evidência esperada:* saídas. *Rubrica:* 3 = resultados corretos (execute o código) e a observação de que o caminho crítico passa para outra cadeia; 2 = números certos, caminho não discutido; 1 = não executado; 0 = nada.

**EX094 — Forense versus velocidade.** *Objetivo:* fazer uma escolha documentada. *Entradas:* pular a geração de imagens forenses encurta a recuperação. *Passos:* escreva uma nota de decisão para a diretora de operações: opções, consequências para a investigação, aspectos legais/regulatórios e a prevenção futura, recomendação. *Evidência esperada:* uma página. *Rubrica:* 3 = geração de imagens em paralelo em hardware de reserva como preferida, riscos de perder evidências explicados, dono da decisão; 2 = recomenda pular sem consequências; 1 = vago; 0 = nada.

### Síntese do capítulo

A recuperação precisa ser ensaiada para merecer confiança. Projete ensaios com fronteiras de segurança e medições, encontre o caminho crítico, melhore apenas o que está nele e relate a situação do requisito que o ensaio de fato mostra — depois mude o projeto ou o requisito com as partes interessadas.

<!-- cyberabc:chapter-navigation:start ch-47 -->
### Continue estudando — capítulo 47 de 50

[← Capítulo 46](#ch-46) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 48 →](#ch-48)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-48"></a>

## Capítulo 48 — Dossiê de evidências

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) montar um dossiê de evidências de engenharia que apoie as alegações do projeto final; (2) organizar as evidências por alegação, com proveniência; (3) proteger as evidências sensíveis mantendo-as revisáveis; e (4) conferir a consistência do dossiê antes da entrega. Ele reúne os capítulos 44 a 47 e prepara o trabalho de conclusão de engenharia.

### 48.1 O que é o dossiê

O dossiê de evidências é a coleção de artefatos que apoia o caso de garantia: requisitos e rastreabilidade; documentos de projeto e registros de decisão; análises (modelos de ameaças, árvores de falhas, desempenho, confiabilidade); registros de implementação (revisão do código-fonte, SBOM, proveniência do build); resultados de verificação e validação; constatações de revisão e respostas; relatórios de ensaios; documentos operacionais; e o registro de riscos residuais com os donos. Organize-o por alegação, e não por data: um revisor deve conseguir partir de uma alegação e encontrar sua evidência em dois cliques. Para o TMRP, as alegações do dossiê são C1 a C4.

### 48.2 Proveniência

Toda evidência declara o que é, quem a produziu, quando, a partir de qual versão do sistema e com quais ferramentas. Os números do trabalho de conclusão precisam ser rastreáveis até um arquivo de resultados (compare com a verificação de proveniência do livro de mestrado, no seu Capítulo 7). Use hashes de conteúdo para os arquivos de resultados e registre-os num índice, como a cadeia de hashes do Capítulo 13 faz para os logs. Para o TMRP, cada entrada do índice do dossiê traz uma versão, como a versão do gateway ou a data do ensaio, e os primeiros caracteres de seu hash.

### 48.3 Sensibilidade

Dossiês sobre infraestrutura contêm detalhes sensíveis. Mantenha uma versão completa e restrita para os revisores autorizados e uma versão com supressões para públicos mais amplos, e registre o que foi suprimido e por quê. Em trabalhos acadêmicos com casos sintéticos, a sensibilidade é menor — mas pratique a disciplina. Para o TMRP, a versão restrita incluiria as configurações dos gateways e os procedimentos de gestão de chaves, enquanto a versão com supressões descreve a arquitetura no nível de zonas e condutos. O registro de supressões lista cada item removido e o motivo, de modo que um revisor da versão com supressões sabe o que foi retido e pode pedir acesso pelo caminho adequado.

### 48.4 Verificação de consistência

Antes da entrega: toda alegação tem evidência; todo número do trabalho de conclusão coincide com sua fonte; as situações concordam entre os documentos (nada de "aprovado" num e "reprovado" noutro — a constatação F1 do Capítulo 45); os riscos residuais têm donos; e todas as constatações de revisão estão encerradas ou encaminhadas. O dossiê do TMRP falhou nessa verificação uma vez, quando C2 citava o T3 como aprovado enquanto a matriz ainda o mostrava como reprovado. A correção foi registrar o novo teste na v2 como T3b e atualizar todos os documentos que se referiam a ele, de modo que o índice agora mostra a mesma situação em toda parte.

### 48.5 Exemplo resolvido: trecho do índice do dossiê (sintético)

| Alegação | Evidência | Versão | Hash (12 primeiros) | Situação |
|---|---|---|---|---|
| C1 R1 atendido | Resultados de T1/T2; campanha de 10 mil mensagens | gw v1.3.0 | 3f9a1c0b7e22 | Aprovado |
| C2 comandos forjados não podem causar perda de abastecimento | Condicionamento do Laboratório 9; T3b; revisão da gestão de chaves | reg. de riscos v1.2 | 8b01d4e6aa90 | Apoiada, com os derrotadores D1, D2 |
| C3 R6 restauração ≤ 8 h | Relatório do ensaio de recuperação | ensaio 2026-09-14 | c47e2b19f5d3 | **Não atendido (12 h)**; opções no ADR-015 |
| C4 R5 bateria de 24 h | Análise de dimensionamento; teste de descarga T4 | gab. v2 | 51d7a0e8c4f6 | Aprovado |

(Os hashes são marcadores ilustrativos para o caso sintético.)

### 48.6 Atividade prática

Monte o índice do seu dossiê com hashes de conteúdo reais dos seus arquivos de resultados (`hashlib.sha256`) e execute a verificação de consistência da §48.4. Use o script do EX095 para calcular os hashes e guarde o índice sob controle de versões, para que seu histórico faça parte das evidências. Depois execute a verificação de consistência contra o rascunho do seu trabalho de conclusão. Todo número do rascunho deve aparecer num arquivo de resultados listado no índice, e toda situação deve coincidir. Corrija qualquer divergência primeiro no documento de origem e depois gere o índice de novo.

### 48.7 Erros comuns e limites

- Dossiês organizados por data ou autor, e não por alegação.
- Números do trabalho de conclusão sem arquivo de origem.
- Situações inconsistentes entre documentos.
- Supressões sem registro.

O índice do TMRP evita o primeiro erro organizando as evidências por alegação, e seu registro de C3 como não atendido impede que o terceiro apareça. Um registro de supressões acompanha a versão compartilhada. Todo número do trabalho de conclusão é rastreável até um arquivo de resultados listado no índice, e a versão compartilhada traz um registro do que foi suprimido e por quê.

### Exercícios — capítulo 48

**EX095 — Script de índice.** *Objetivo:* automatizar a proveniência. *Entradas:* uma pasta de resultados. *Passos:* escreva um script com a biblioteca padrão que percorra a pasta, calcule o SHA-256 de cada arquivo e escreva um índice CSV com caminho, tamanho, hash e horário de modificação; explique por que o horário de modificação é uma evidência fraca. *Evidência esperada:* script e explicação. *Rubrica:* 3 = script funcional, explicação (o mtime é facilmente alterado; hash mais commit no controle de versões é mais forte); 2 = sem explicação; 1 = não funciona; 0 = nada.

**EX096 — Auditoria de consistência.** *Objetivo:* pegar inconsistências. *Entradas:* o trecho da §48.5 e uma frase do resumo, "Todos os requisitos foram verificados e o sistema restaura a operação remota em até 8 horas". *Passos:* identifique a inconsistência e reescreva a frase. *Evidência esperada:* reescrita. *Rubrica:* 3 = identifica a contradição com C3, reescrita precisa e ainda positiva onde justificado; 2 = reescrita vaga; 1 = não a percebe; 0 = nada.

### Síntese do capítulo

O dossiê é o corpo de evidências, organizado por alegação e com proveniência rastreada, por trás do caso de garantia. Mantenha versões restrita e com supressões, com um registro das supressões, e confira a consistência de cada alegação, número e situação antes que qualquer outra pessoa o faça.

<!-- cyberabc:chapter-navigation:start ch-48 -->
### Continue estudando — capítulo 48 de 50

[← Capítulo 47](#ch-47) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 49 →](#ch-49)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-49"></a>

## Capítulo 49 — Trabalho de conclusão de curso de engenharia

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) estruturar um trabalho de conclusão de engenharia em torno de um problema de projeto, uma solução e as evidências; (2) escrever resultados e limitações que fiquem dentro das evidências; (3) apresentar resultados quantitativos com incerteza e proveniência; e (4) preparar um trabalho de conclusão que um examinador consiga verificar. Ele transforma o dossiê num documento e prepara a defesa.

### 49.1 O trabalho de conclusão de engenharia

Um trabalho de conclusão de engenharia argumenta que um sistema projetado atende a uma necessidade sob restrições, apoiado em evidências de verificação e validação. Ele não é uma dissertação de pesquisa (o [livro de mestrado](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) trata disso) e não precisa alegar uma contribuição original ao conhecimento (o [livro de doutorado](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md)). Sua originalidade, se houver, está no projeto e na qualidade de suas evidências. Para o TMRP, o trabalho de conclusão argumenta que o gateway seguro diante de reinícios atende a R1, R2 e R7 na bancada e relata R6 como não atendido.

### 49.2 Estrutura

1. **Introdução:** necessidade, partes interessadas, consequência, escopo.
2. **Fundamentação:** contexto setorial, normas pertinentes e projetos anteriores, com fontes.
3. **Requisitos:** requisitos derivados, com fontes e métodos de verificação.
4. **Projeto:** alternativas, seleção, arquitetura, controles, com registros de decisão.
5. **Análise:** análise de ameaças e falhas, desempenho, confiabilidade.
6. **Implementação:** o que foi construído, como, com quais ferramentas.
7. **Verificação e validação:** métodos, resultados, reprovações e correções.
8. **Discussão:** situação dos requisitos, riscos residuais, limitações, o que você faria de outro modo.
9. **Conclusão:** o que foi alcançado e o que falta.
Apêndices: matriz de rastreabilidade, índice do dossiê, código dos laboratórios.

O trabalho de conclusão do TMRP segue essa estrutura.

### 49.3 Resultados e limitações

Relate a situação dos requisitos com honestidade: atendido, atendido após correção, não atendido, não verificado. Para cada limitação, diga quais alegações ela afeta e em que direção: "a bancada usa relógios perfeitos; a deriva real dos relógios aumentaria as rejeições de mensagens inativas, então a taxa de falsas inatividades relatada é um limite inferior". Uma limitação sem direção é enfeite. O parágrafo de discussão do TMRP no exemplo resolvido abaixo dá uma limitação desse tipo: a bancada usou uma rede sintética, então o limiar de sessenta segundos da estação inativa precisa ser ajustado de novo em campo, onde o congestionamento da LTE pode aumentar os alarmes falsos. Essa frase nomeia a alegação afetada e a direção provável.

### 49.4 Escrever bem

Abra cada capítulo com seu ponto principal. Use figuras com eixos rotulados e unidades; tabelas para valores exatos. Mantenha os números rastreáveis até o dossiê. Escreva em linguagem técnica simples, defina os termos no primeiro uso e use um glossário. Para o TMRP, a tabela de situação dos requisitos aparece cedo na discussão, e cada número nela é rastreável até uma entrada do índice do dossiê, com seu hash. Cada capítulo abre com seu ponto principal, e termos como alarme de estação inativa são definidos no primeiro uso e no glossário, de modo que um examinador consiga ler qualquer capítulo sem caçar definições.

### 49.5 Exemplo resolvido: parágrafo de discussão (sintético)

> O gateway atendeu a R1 e R2 na bancada, incluindo reinícios de qualquer das extremidades, depois que o receptor foi alterado para persistir seu último contador aceito (Seção 7.3). R7 foi atendido para os alarmes prioritários e, depois da constatação de revisão F2, para a perda de dados. R6 não foi atendido: o ensaio de recuperação restaurou a operação remota em 12 h contra um requisito de 8 h, porque a geração de imagens forenses e a reconstrução ficam em série no caminho crítico. O abastecimento do hospital foi mantido em modo local durante todo o ensaio, então a consequência da insuficiência é a redução da visibilidade e da capacidade de intervenção, e não a perda do abastecimento. Duas opções de projeto que atenderiam às 8 h estão orçadas no ADR-015. Todos os resultados vêm de uma bancada sintética; o desempenho em campo, em particular a latência da LTE sob congestionamento, pode ser diferente, e o limiar de 60 s da estação inativa precisa ser ajustado de novo em campo.

### 49.6 Atividade prática

Escreva o capítulo de discussão do seu trabalho de conclusão, com uma tabela de situação dos requisitos e limitações com direção. Use o parágrafo de discussão do TMRP como modelo. Comece com uma tabela que dê a situação de cada requisito como atendido, atendido após correção, não atendido ou não verificado. Depois escreva um parágrafo por resultado significativo, incluindo qualquer requisito que você não atendeu, e termine com suas limitações, cada uma nomeando a alegação que afeta e a direção do viés provável. Confira cada número contra o índice do seu dossiê antes da entrega.

### 49.7 Erros comuns e limites

- Trabalhos de conclusão organizados como diários.
- Situação dos requisitos arredondada para cima.
- Limitações sem direção nem alegações afetadas.
- Números que não coincidem com o dossiê.

O trabalho de conclusão do TMRP evita cada um desses erros: é organizado pelo argumento, relata R6 como não atendido, dá limitações com direção e tira seus números do índice do dossiê. Sua tabela de situação dos requisitos é conferida contra o dossiê antes da entrega, então nada é arredondado para cima. Suas limitações nomeiam a bancada sintética e o ensaio de recuperação único, e dizem em que direção cada uma poderia enviesar os resultados.

### Exercícios — capítulo 49

**EX097 — Limitações com direção.** *Objetivo:* escrever limitações úteis. *Entradas:* três limitações: modelo de ruído sintético; bancada sem LTE real; um único ensaio de recuperação. *Passos:* para cada uma, declare a alegação afetada e a direção do viés provável. *Evidência esperada:* três frases. *Rubrica:* 3 = cada uma tem alegação e direção (p. ex., um único ensaio não dá estimativa de variabilidade — as 12 h podem ser otimistas ou pessimistas; a latência real da LTE aumentaria as rejeições por inatividade e a latência dos alarmes); 2 = falta uma direção; 1 = apenas a lista; 0 = nada.

**EX098 — Resumo.** *Objetivo:* resumir com precisão. *Entradas:* §49.5. *Passos:* escreva um resumo estruturado de 150 palavras (necessidade, projeto, métodos, resultados, limitações). *Evidência esperada:* resumo. *Rubrica:* 3 = preciso, incluindo R6 não atendido, limite da bancada sintética declarado; 2 = um exagero; 1 = vago; 0 = nada.

### Síntese do capítulo

Um trabalho de conclusão de engenharia argumenta da necessidade ao projeto e às evidências. Estruture-o para um examinador, relate a situação dos requisitos como ela é, dê a cada limitação uma alegação afetada e uma direção, e mantenha cada número rastreável até o dossiê.

<!-- cyberabc:chapter-navigation:start ch-49 -->
### Continue estudando — capítulo 49 de 50

[← Capítulo 48](#ch-48) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 50 →](#ch-50)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-50"></a>

## Capítulo 50 — Defesa final

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo você será capaz de (1) preparar a apresentação técnica de defesa de um projeto final e de um trabalho de conclusão; (2) antecipar as perguntas dos examinadores por família e preparar respostas baseadas em evidências; (3) lidar com honestidade com as perguntas que você não consegue responder; e (4) planejar as correções e a passagem depois da defesa. Ele encerra o curso.

### 50.1 O que os examinadores testam

Os examinadores conferem se o candidato entende a necessidade e as restrições; tomou decisões de projeto defensáveis; verificou as alegações com competência; conhece os limites das evidências; e consegue raciocinar sobre mudanças ("e se o requisito fosse de 2 h?"). Eles leem o trabalho de conclusão com atenção e sondam as inconsistências. Na defesa do TMRP, os examinadores provavelmente vão sondar a insuficiência de R6 e o risco residual aceito D1. Eles podem perguntar o que mudaria se a reserva do hospital fosse de duas horas em vez de quatro, e o candidato deve raciocinar a partir da árvore de falhas e do modo automático local, em vez de chutar.

### 50.2 A apresentação

Vinte minutos: necessidade e consequência (2 min); requisitos (2); alternativas e seleção (3); arquitetura e principais controles (4); resultados de verificação e validação, com reprovações e correções (5); situação dos requisitos e riscos residuais (2); limitações e próximos passos (2). Uma mensagem por slide. Mostre a tabela de situação dos requisitos; os examinadores respeitam um "não atendido" dito com clareza. Para o TMRP, a tabela de situação dos requisitos mostraria R1, R2 e R7 como atendidos após correções e R6 como não atendido em doze horas, com as opções do ADR-015. Esse slide prepara a banca para as perguntas do exemplo resolvido, e declarar a insuficiência antes que um examinador a encontre conquista mais confiança do que qualquer resultado polido.

### 50.3 Famílias de perguntas

- **Necessidade:** por que isto importa, para quem, como você sabe?
- **Projeto:** por que esta e não aquela alternativa; o que mudaria sua escolha?
- **Análise:** de onde vem este número; e se este pressuposto estiver errado?
- **Verificação:** como você sabe que o teste testa o requisito; o que seus testes deixaram passar?
- **Limites:** o que você não pode alegar; o que uma implantação em campo revelaria?
- **Ética e segurança:** o que poderia dar errado para as pessoas; quem é dono do risco residual?

Prepare duas respostas por família, com referências ao dossiê.

### 50.4 Respostas honestas

Quando você não sabe: diga isso, diga como descobriria e — se puder — raciocine em voz alta rumo a uma resposta, deixando claro que é raciocínio. Não invente números. Quando um examinador encontra um erro: reconheça-o, avalie seu impacto sobre as alegações e proponha uma correção. No exemplo resolvido, o candidato faz isso quando perguntado sobre o risco residual D1: declara quem o aceitou, as evidências que o limitam e a alternativa que o eliminaria, sem fingir que o risco é desprezível. Nenhum número é inventado.

### 50.5 Depois da defesa

As correções são listadas numa tabela: pedido do examinador, mudança feita, localização. Passe o artefato e o dossiê ao patrocinador, com as limitações conhecidas e as necessidades de manutenção. Em projetos reais, encaminhe quaisquer constatações de segurança pelos processos do proprietário. Para o TMRP, a passagem vai para a diretora de operações da LRWA, com o dossiê, o item em aberto sobre R6 e a nota de que o limiar da estação inativa precisa ser ajustado de novo em campo. Qualquer constatação de segurança sobre equipamentos reais passaria pelos próprios processos da LRWA, e não pelo trabalho de conclusão.

### 50.6 Exemplo resolvido: respondendo a uma pergunta difícil (sintético)

*Examinador:* "Seu caso de garantia aceita o risco residual D1 — um centro SCADA comprometido emitindo comandos autênticos. Por que isso é aceitável para o abastecimento de um hospital?" *Candidato:* "Ele foi aceito pela diretora de operações, e não por mim, e o caso declara por quê: os limites locais (R3) mantêm qualquer setpoint aceito dentro de limites seguros, então o pior que um centro comprometido pode fazer na PS4 é parar as bombas, e a árvore de falhas mostra que perder o abastecimento exige então que o caminho do reservatório e o tanque do hospital também falhem. Se os examinadores considerarem isso insuficiente, a alternativa do ADR-012 — escritas de setpoint apenas locais na PS4 — elimina o controle remoto naquele local, a um custo de pessoal estimado em um acionamento por mês. Eu não alegaria que D1 é desprezível; alego que ele é limitado e tem dono."

### 50.7 Atividade prática

Realize uma defesa simulada com dois colegas atuando como examinadores, usando as famílias de perguntas; registre as perguntas que você não conseguiu responder e prepare as respostas. Peça aos examinadores que usem todas as famílias de perguntas e que sondem pelo menos um número do seu trabalho de conclusão. Registre cada pergunta que você não conseguiu responder e depois rastreie a resposta até o seu dossiê. Para o TMRP, as perguntas mais difíceis tratam da insuficiência de R6 e do risco residual D1; prepare essas respostas até conseguir dá-las de forma breve, com as evidências nomeadas e sem alegar mais do que o dossiê apoia.

### 50.8 Erros comuns e limites

- Apresentações que escondem as reprovações.
- Respostas defensivas a constatações de erro.
- Números inventados sob pressão.
- Nenhum plano de correções.

O candidato do TMRP evita esses erros mostrando a insuficiência de R6 num slide, reconhecendo os erros com clareza, recusando-se a inventar números e mantendo uma tabela de correções pronta para os pedidos dos examinadores. Reprovações como a repetição após o reinício são apresentadas como constatações que a verificação pegou, com a correção e o novo teste, que é exatamente o que os examinadores querem ver. Uma tabela de correções está pronta. Cada alegação fica dentro do dossiê.

### Exercícios — capítulo 50

**EX099 — Banco de perguntas.** *Objetivo:* antecipar o exame. *Entradas:* seu trabalho de conclusão ou o caso do TMRP. *Passos:* escreva doze perguntas (duas por família) e respostas curtas baseadas em evidências, com referências ao dossiê. *Evidência esperada:* banco. *Rubrica:* 3 = perguntas difíceis e específicas, com respostas honestas que incluem os limites; 2 = perguntas brandas; 1 = respostas sem evidências; 0 = nada.

**EX100 — Tabela de correções.** *Objetivo:* planejar as correções. *Entradas:* pedidos dos examinadores: (1) relatar a variabilidade do tempo de recuperação; (2) justificar a fração utilizável de 0,6 da bateria; (3) remover a alegação de que o detector "impede" ataques. *Passos:* escreva uma tabela de correções com a mudança, a localização e como cada uma é evidenciada. *Evidência esperada:* tabela. *Rubrica:* 3 = (1) reconhece o ensaio único e acrescenta um plano ou execuções simuladas repetidas, (2) acrescenta a fonte do fabricante ou uma análise de sensibilidade, (3) reformulação para "detecta"; 2 = uma fraca; 1 = sem localizações; 0 = nada.

### Síntese do capítulo

A defesa testa a compreensão, o julgamento e a honestidade sobre os limites. Apresente com clareza a necessidade, o projeto, as evidências e a situação; prepare-se por família de perguntas, com referências ao dossiê; responda o que você sabe, raciocine de forma transparente sobre o que não sabe e transforme as constatações dos examinadores numa tabela de correções precisa e numa passagem responsável.

<!-- cyberabc:chapter-navigation:start ch-50 -->
### Continue estudando — capítulo 50 de 50

[← Capítulo 49](#ch-49) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável. Os resultados numéricos foram produzidos executando os laboratórios e os scripts curtos descritos, com Python 3 e as sementes indicadas; seus últimos dígitos podem diferir se você mudar a ordem dos sorteios aleatórios. Nos exercícios de projeto, a rubrica do capítulo importa mais do que coincidir com a redação abaixo. Lowmarsh Regional Water Authority, St Brenna's Hospital, o TMRP e todos os números são sintéticos.

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

**EX031.** Um mapeamento: N1 ← R3, R4, R5 (em parte), R9; N2 ← R1, R2, R3, R7, R8; N3 ← R6, R8; N4 ← R5, R7. N3 e N4 empatam com o menor número (dois cada); a proposta reforça N3: "R10 — Backups off-line das configurações do SCADA e dos controladores deverão ser feitos semanalmente, guardados fora dos domínios de controle e corporativo, e ter a restauração testada trimestralmente."

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

### Capítulo 27

**EX053.** Limite projetado: nenhuma (mecânico). Limites do controlador: PLC de dosagem. Alarme do analisador: registrador separado e suas comunicações. Registro e alarme das rejeições: via SCADA — compartilhados com o sistema que poderia estar comprometido. Mudança: log local não volátil de rejeições no PLC e um caminho de alarme independente (do registrador do analisador até a sala de controle por uma rota separada).

**EX054.** Os comandos falham fechados: se o gateway falhar, nenhum comando passa. A telemetria falha de forma visível: o SCADA gera um alarme de estação inativa em até 60 s. O controle local continua automaticamente, dentro dos limites impostos localmente. Desligar a estação transformaria a falha de um componente de segurança numa falha de abastecimento.

### Capítulo 28

**EX055.** Com `old` = 5.2: v1 — NaN aceito (todas as comparações falsas); +∞ rejeitado (`> hi`); −∞ rejeitado (`< lo`); 5.5 aceito (|5,5 − 5,2| = 0,3 ≤ 0,5, limite inclusivo); 5.50001 rejeitado (`> hi`). A v2 rejeita NaN e ±∞ via `isfinite`, aceita 5.5 e rejeita 5.50001.

**EX056.** Campos: carimbo de tempo em UTC e fonte de tempo; ID do gateway; ID da estação; código do motivo (etiqueta, repetição, inatividade, formato, faixa); valor do contador (se interpretável); último contador aceito; SHA-256 do quadro recebido; endereço de origem. Exclua o material de chaves e a carga útil completa dos comandos onde ela poderia revelar setpoints sensíveis a quem lê os logs; o hash do quadro permite a correlação sem divulgação.

### Capítulo 29

**EX057.** Revocação 5/7 ≈ 0,714; TFP no teste 3/7 ≈ 0,429. A cada 1.000 eventos com um malicioso: VP esperados ≈ 0,714, FP ≈ 428. Precisão operacional ≈ 0,0017. Interpretação: a estimativa da TFP a partir de 7 eventos benignos é extremamente incerta, mas mesmo uma melhoria de uma ordem de grandeza deixa o detector inutilizável para acionar plantonistas; ele precisa de uma TFP muito menor, medida sobre muito mais dados benignos.

**EX058.** Base: 40% × 4 h = 160 %·h, mais o triângulo de recuperação 0,5 × 8 × 40 = 160 → 320 %·h. Com o manual local a 85%: 15 × 4 = 60, mais 0,5 × 8 × 15 = 60 → 120 %·h. Neste caso sintético, R4 reduz a perda de resiliência em cerca de 62%.

### Capítulo 30

**EX059.** O NaN dá falso em qualquer comparação, então as verificações negativas da v1 nunca o rejeitam, enquanto ±∞ falham em `> hi` ou `< lo`. Cerca de 2.000/10 = 200 casos de valores especiais, um quinto deles NaN → cerca de 40 esperados; 31 observados (o gerador sorteou 31 casos NaN com a semente 30), bem dentro da variação aleatória (desvio-padrão binomial ≈ 5,7). Todo caso NaN é uma aceitação insegura pela v1, então as 31 reprovações são exatamente os casos NaN.

**EX060.** Casos: (1) contadores 1, 2, 3 → todos aceitos; (2) repetir o 2 → rejeitado; (3) contador menor → rejeitado; (4) reinício do receptor e depois repetição de uma mensagem antiga → rejeitada (exige estado persistido ou rotação de chaves); (5) reinício do emissor → retoma em persistido + 1.000, aceito; contadores antigos rejeitados; (6) entrega fora de ordem (3 antes de 2) → 3 aceito, 2 rejeitado e registrado em log (comportamento documentado); (7) contador no máximo 2⁶⁴ − 1 → rotação de chaves exigida antes do estouro; testar que o emissor se recusa a dar a volta. Critérios de aprovação: resultados exatos de aceitação/rejeição e entradas de log.

### Capítulo 31

**EX061.** Gatilhos: telemetria da PS4 ausente por > 5 min enquanto o enlace está ativo; qualquer quadro aceito que falhe na auditoria posterior; latência de alarme prioritário > 60 s em dois eventos numa hora; mudança inesperada do estado de uma bomba. Dono da decisão: gerente de operações de plantão. Reversão concluída em até 1 h (bem dentro da reserva de 4 h do hospital), com a PS4 em modo automático local o tempo todo.

**EX062.** Controles: endurecimento do sistema operacional e dos serviços; atualizações de firmware assinadas; chave num elemento seguro; filtragem de códigos de função e de faixa de registradores; chave de violação do gabinete alarmada no SCADA; registro em log local e encaminhado; portas não usadas desativadas; trancas físicas. Residual: um atacante com acesso físico ao gabinete aberto pode se conectar ao enlace serial legado e comandar a RTU diretamente; a detecção de violação reduz o tempo de permanência, mas não o impede.

### Capítulo 32

**EX063.** Com duas equipes, a transição do estado 2 de volta ao estado 1 tem taxa 2μ, então $p_2 = p_0 \cdot 2r \cdot r/2 = p_0 r^2$ com $r = \lambda/\mu$. Indisponibilidade ≈ 1,41 × 10⁻⁴, igual à fórmula ingênua independente — porque o reparo independente é exatamente o que essa fórmula pressupõe. Uma equipe: 2,81 × 10⁻⁴, cerca do dobro.

**EX064.** Com MTTR de 504 h e uma equipe: indisponibilidade ≈ 0,078 (cerca de 28 dias por ano com as duas bombas paradas), contra 2,8 × 10⁻⁴ com uma reserva. Mantenha uma bomba reserva: o custo é irrisório diante de semanas de abastecimento do hospital por um único caminho.

### Capítulo 33

**EX065.** Linhas-modelo para a malha de dosagem (perdas: água insegura; danos por superdosagem): não fornecida — o controlador não aumenta a dose quando a demanda sobe (realimentação de vazão falha); fornecida quando insegura — o controlador aumenta a dose quando o residual já está alto (leitura do analisador falsificada por um atacante); momento errado — aumento de dose aplicado depois que a vazão caiu (atraso na realimentação); por tempo demais — a dosagem continua depois que a vazão para (sinal de vazão travado). Restrições: monitoramento independente do residual, dose intertravada com a vazão, limite físico de curso.

**EX066.** Violações: estação de engenharia compartilhada (um único comprometimento pode reprogramar tanto a lógica de controle quanto a de segurança) e switch compartilhado (caminho de rede e falha comum). Arquitetura: estação de engenharia dedicada ao SIS mantida off-line, alterações no programa do SIS habilitadas apenas com uma chave física, SIS numa rede separada ou com fiação dedicada a seus sensores e elementos finais, exportação de dados somente leitura para o sistema de controle. Residual: um insider com a chave física, comprometimento do firmware do SIS na cadeia de suprimentos.

### Capítulo 34

**EX067.** 42 × 180 = 7.560 mensagens; a 50 por segundo, 151,2 s para escoar; um alarme prioritário no fim espera cerca de 151 s, violando R7 (60 s). Correção: fila com prioridade para os alarmes e encaminhamento do valor mais recente, com preenchimento do histórico no historiador a taxa limitada.

**EX068.** Cláusulas: notificação de incidentes à LRWA em até 1 h após a detecção; divulgação de vulnerabilidades que afetem a rede privada em até 72 h; manutenção planejada notificada com 10 dias úteis de antecedência; prioridade de restauração para os locais da LRWA, com meta de 4 h; logs de acesso ao APN da LRWA fornecidos mensalmente; exercício conjunto anual.

### Capítulo 35

**EX069.** R6 (8 h) conflita com o resultado do ensaio (12 h): R6 não é atendido. O abastecimento do hospital não depende da operação remota (modo automático local, 72 h), então a alegação N1 ainda pode se sustentar; o caso de garantia precisa registrar R6 como reprovado, com um plano de correção ou uma revisão acordada com as partes interessadas. A bateria de 24 h e a reserva de 4 h são consistentes.

**EX070.** D3: uso indevido do modo manual local na PS4 por um insider — resposta: regra de duas pessoas para o modo manual fora dos horários de manutenção, alarme e CFTV no painel. D4: comprometimento do caminho de atualização do firmware do gateway — resposta: atualizações assinadas com chaves num HSM, implantação em etapas, monitoramento do comportamento do gateway. D5: a persistência do contador falha após a perda de energia — resposta: teste de reinício (EX060) e rotação de chaves em reinício não limpo.

### Capítulo 36

**EX071.** μ = 100/s: λ = 20 → ρ = 0,20, W = 12,5 ms, L = 0,25; λ = 40 → ρ = 0,40, W ≈ 16,7 ms, L ≈ 0,67; λ = 48 → ρ = 0,48, W ≈ 19,2 ms, L ≈ 0,92. Comparado com μ = 50 (33,3, 100 e 500 ms), dobrar a capacidade elimina a explosão do atraso em tempestades.

**EX072.** (1) Filtragem no nível da rede: apenas as extremidades dos túneis dos gateways podem alcançar o verificador — descarta a maior parte do tráfego forjado antes de qualquer computação. (2) Verificações prévias baratas (comprimento, ID de estação conhecido, contador plausivelmente à frente do último aceito) antes de calcular o MAC. (3) Limites de taxa por origem e uma fila com prioridade estrita para os alarmes verificados, de modo que as inundações sejam descartadas na prioridade mais baixa. Apenas acrescentar capacidade perde para um atacante que consegue escalar o tráfego.

### Capítulo 37

**EX073.** Fraquezas: "não corresponde a uma ação de operador" é ambíguo — defina como nenhum comando de operador registrado para aquela estação e parâmetro nos 5 min anteriores; sem dados de contato — acrescente os números do gerente de plantão e da segurança de sobreaviso; restaurar setpoints remotamente poderia usar o caminho comprometido — especifique a restauração local pelo técnico de plantão se houver falhas de MAC no gateway.

**EX074.** O que aconteceu: o técnico conectou um laptop à rede da PS3 para baixar logs. Por que fazia sentido: a rota pelo jump host é lenta e exige um chamado; os logs eram necessários para uma ligação com o fornecedor naquela tarde. Defesas que falharam: sem segurança de porta no switch; sem caminho aprovado simples para os logs; o procedimento pressupunha o jump host sempre disponível. Mudanças: fornecer um coletor de logs na DMZ para que os técnicos não precisem se conectar; habilitar a segurança de porta; disponibilizar um conjunto de laptops de manutenção verificados; simplificar o acesso pelo jump host para a obtenção de logs somente leitura.

### Capítulo 38

**EX075.** Com o T3b aprovado para R3, o T8 aprovado para R4 e o T6 aprovado para R8: untested ['R9'], tested but not passing [], verified 8/9 (88.9%). R9 permanece não verificado até que um teste do alarme de dosagem independente (por exemplo, parar a dosagem na bancada e cronometrar o alarme no registrador separado contra 15 min) seja escrito e aprovado. A verificação está completa para os outros oito requisitos; a validação de N1 ainda precisa das atividades com as partes interessadas do EX076.

**EX076.** (1) Exercício noturno: a equipe de operações passa a PS3 e a PS4 para o manual local com o efetivo noturno real; observar o tempo e os erros; sucesso: operação manual em até 1 h e pressão de abastecimento mantida. (2) Isolamento planejado da PS4 em período de baixa demanda, com o gerente de instalações do hospital monitorando o armazenamento e a pressão no local; sucesso: abastecimento mantido pelo reservatório, com o armazenamento nunca abaixo do nível que dá 4 h de reserva. Partes interessadas: gerente de operações, instalações do hospital, engenharia do TMRP.

### Capítulo 39

**EX077.** Quadro: ID de suíte (1 byte) ‖ contador ‖ estação ‖ valor ‖ etiqueta, com o MAC calculado também sobre o ID de suíte (para que não possa ser alterado). O receptor mantém as suítes permitidas por estação, p. ex., {1} → {1, 2} durante a transição → {2}. Prevenção de rebaixamento: depois que uma estação tiver enviado a suíte 2, rejeitar dela a suíte 1. Aposentadoria: remover a suíte 1 de todos os conjuntos permitidos depois que todas as estações tiverem migrado e revogar as chaves da suíte 1.

**EX078.** Revogar a chave da estação e removê-la do HSM; remover as contas do gateway; apagar (ou destruir) o armazenamento do gateway e da RTU; atualizar o inventário, o modelo do sistema e o dossiê; remover as entradas da lista de permissões e as regras de firewall dos endereços antigos; atualizar as linhas de base do monitoramento; dar destinação às reservas ou colocá-las em quarentena; registrar a aprovação formal de operações e de segurança.

### Capítulo 40

**EX079.** A detecção de lacunas registra 67 eventos de lacuna, cobrindo 81 contadores ausentes, com a semente 40. Os números diferem dos 21 descartes porque toda mensagem não aceita — corrompidas (14), atrasadas e inativas (22), descartadas (21) e os espaços em que um quadro antigo foi repetido no lugar do atual (24) — deixa seu contador sem uso; 14 + 22 + 21 + 24 = 81. Contadores ausentes consecutivos produzem um único evento de lacuna, então há menos eventos do que contadores ausentes.

**EX080.** Com as classes de reordenação e reinício (5% cada, semente 40): as mensagens reordenadas que chegam depois de sua sucessora são rejeitadas como repetições (17) — aceitável se documentado, já que dados antigos são descartados e o valor mais novo já está guardado, mas registre em log. Os reinícios do receptor não produzem nenhum erro visível (26 aceitas normalmente), e esse é o perigo: depois de um reinício, qualquer repetição que chegue antes da próxima mensagem nova seria aceita. A campanha, por acaso, não mostra nenhum caso assim; um teste determinístico (reinício e depois repetição) o expõe — uma falha silenciosa, a menos que o receptor persista o estado.

### Capítulo 41

**EX081.** 150 mil: telemetria autenticada + backups off-line → 330; 200 mil: + manual local → 440 (custo 190); 250 mil: + RTUs de reserva → 530; 300 mil: telemetria autenticada, gerador de reserva, manual local, backups off-line → 590 (custo 280); 350 mil: + RTUs de reserva → 680 (custo 340). Benefício marginal a cada 50 mil adicionais: 110, 90, 60, 90 — em geral decrescente, mas irregular porque os controles são indivisíveis.

**EX082.** Das 14 execuções, três mudam o ótimo para {telemetria autenticada, gerador de reserva da PS4, manual local} (custo 250, benefício 520 nos valores de base): benefício do gerador de reserva × 1,2, backups off-line × 0,8 ou RTUs de reserva × 0,8. Todas as outras execuções mantêm o conjunto de base. Conclusão: a telemetria autenticada e o modo manual local são escolhas robustas; os últimos 90 mil do orçamento são um quase empate entre {backups off-line + RTUs de reserva} e o gerador de reserva, então essa parte da decisão deve se apoiar em estimativas melhores ou em critérios não monetários.

### Capítulo 42

**EX083.** O protocolo inclui: pergunta (o detector cumulativo com limiar θ produz < 1 alarme falso por mês no ruído medido e detecta rampas de 0,05 m/h em até 2 h?); decisão (implantar e definir θ e o intervalo de recalibração); desenho (varredura em simulação, 100 sementes por célula); medições; regra de análise fixada com antecedência; validação contra duas semanas de ruído do historiador; limites (mistura perfeita, medidores de vazão honestos, tanque único).

**EX084.** Que taxa de alarmes falsos por dia veríamos na nossa taxa de eventos? Quais ataques estavam no conjunto de teste e quem os escolheu? A avaliação usou ajuste de pontos ou foi livre de vazamento (divisão treino/teste por tempo)? Quão semelhante à nossa planta é o testbed em escala e ruído? Como o desempenho se sustenta contra um atacante adaptativo que conhece o detector?

### Capítulo 43

**EX085.** Avaliado pela rubrica; o acordo precisa nomear os supervisores, o escopo, o método de acesso, a confidencialidade, a integração de segurança, a aprovação da publicação, o caminho para as constatações incidentais e uma declaração explícita de que o estudante não testará nem explorará sistemas fora das tarefas acordadas.

**EX086.** Observação: os operadores registram as mudanças de setpoint num caderno de papel, além de no SCADA. Conexão: Capítulo 13 (proveniência) e Capítulo 37 (operações). Diferença: a prática duplica o log eletrônico; localmente racional, porque o caderno sobrevive às quedas do SCADA, apoia a passagem de turno e é confiável. Pergunta: os dois registros alguma vez divergem, e o caderno poderia servir como verificação independente de integridade?

### Capítulo 44

**EX087.** Problemas: escopo sem limites ("concessionárias de água"), nenhum requisito nem critério de aceitação, nenhuma fonte de dados, tecnologia escolhida antes do problema. Reescrita: p. ex., "Um detector baseado em resíduos para dados de nível falsos num único reservatório sintético: requisitos, estudo de simulação com ruído com semente, critérios de aceitação < 1 alarme falso/mês e detecção de rampas de 0,05 m/h em até 2 h, 12 semanas, apenas dados sintéticos."

**EX088.** Aumento descontrolado do escopo (probabilidade média, impacto alto; mitigação: congelamento do escopo na CDR; gatilho: novos pedidos de funcionalidades depois da semana 6); segurança diante de reinícios mais difícil do que o planejado (M/A; prova de conceito na semana 2; gatilho: projeto não estável até a semana 4); fidelidade da bancada insuficiente (M/M; revisão com o supervisor; gatilho: constatação de um revisor); tempo (A/A; semana de folga; gatilho: atraso de um marco > 1 semana); disponibilidade do supervisor (B/M; revisões agendadas; gatilho: revisão perdida).

### Capítulo 45

**EX089.** (1) "As chaves das 42 estações são geradas no laptop de um engenheiro (procedimento de GC §3.2); o comprometimento desse laptop expõe a frota; falha na intenção de R1; recomenda-se a geração no HSM ou no elemento seguro do gateway." (2) "O comportamento do receptor diante de reinícios não é coberto por nenhum teste (plano de verificação, tabela 4); R2 exige a rejeição de repetições após o reinício; recomendam-se testes conforme o EX060." (3) Retirar como preferência de projeto, ou reformular: "o projeto não declara por que o protocolo escolhido atende a R1 e R7; acrescentar a justificativa."

**EX090.** F2: aceita — alarme de estação inativa em 60 s e registro de lacunas de contador acrescentados; campanha executada de novo com a semente 40; dono: líder do gateway; data: duas semanas. F3: aceita — dossiê corrigido para "R6 não atendido (12 h)"; opções orçadas: geração paralela de imagens em hardware de reserva (9 h), mais imagem de SCADA de reserva (6 h); revisão pelas partes interessadas para decidir entre mudança de projeto e requisito revisado; dono: gerente do TMRP; data: próxima reunião do comitê diretor.

### Capítulo 46

**EX091.** Gere a nova chave no HSM; distribua-a ao gateway com o ID de chave k+1; por 10 minutos o receptor aceita quadros marcados com qualquer dos dois IDs de chave (o ID da chave fica dentro do cabeçalho autenticado); o emissor passa para k+1 e os contadores continuam; se os quadros com k+1 falharem, reverta para k; depois da janela, o receptor rejeita k, e k é destruída nos dois lugares; registre cada passo em log.

**EX092.** Prosseguir com condições: iniciar o ensaio com o limiar de 60 s, monitorado por um engenheiro; coletar dados sobre os alarmes falsos de inatividade durante o congestionamento; ajustar o limiar (p. ex., 90 s para estações não críticas) até uma data declarada; informar aos operadores que alarmes de inatividade durante o congestionamento são esperados. A consequência de não detectar uma perda real de dados supera dois alarmes falsos por dia por um período limitado.

### Capítulo 47

**EX093.** (1) Com a reconstrução dependendo apenas do isolamento: controle remoto em 9 h; caminho crítico isolar → reconstruir → restaurar a configuração → verificar → retomar; a geração de imagens sai do caminho. (2) Com uma reconstrução de 1 h a partir de uma imagem de reserva: 6 h; a cadeia da reconstrução e a cadeia da troca de chaves (isolar → trocar chaves → verificar → retomar) empatam agora em 6 h, então a troca de chaves passou a ser crítica e ganhos adicionais exigem encurtá-la também.

**EX094.** Opções: (a) pular a geração de imagens (mais rápida; evidências perdidas; a causa raiz e a persistência do atacante podem passar despercebidas; possíveis consequências regulatórias ou legais); (b) gerar as imagens primeiro (mais lenta); (c) gerar as imagens em paralelo usando hardware de reserva e reconstruir em hardware limpo (quase a mais rápida; evidências preservadas). Recomendação: (c), com uma decisão pré-aprovada de que a diretora de operações pode autorizar (a) apenas se o abastecimento estiver em risco. Dono: diretora de operações.

### Capítulo 48

**EX095.** Script: percorra a pasta com `os.walk`; para cada arquivo, leia em blocos para o `hashlib.sha256`; escreva `path, size, sha256, mtime` com `csv.writer`. O horário de modificação é uma evidência fraca porque é facilmente alterado e não está vinculado ao conteúdo; um hash de conteúdo registrado no controle de versões (ID do commit e tag assinada) é muito mais forte.

**EX096.** Inconsistência: C3 mostra R6 não atendido (12 h). Reescrita: "Todos os requisitos, exceto a meta de restauração de 8 horas, foram verificados; um ensaio de recuperação restaurou a operação remota em 12 horas enquanto o abastecimento continuava em modo local, e são apresentadas duas opções de projeto para atender à meta."

### Capítulo 49

**EX097.** Modelo de ruído sintético → afeta as alegações de alarmes falsos e de tempo de detecção do detector; o ruído real provavelmente não é gaussiano e tem deriva, então os alarmes falsos provavelmente estão subestimados. Bancada sem LTE real → afeta as alegações de latência e de rejeição por inatividade; a latência e o jitter reais aumentariam as rejeições por inatividade e a latência dos alarmes. Um único ensaio de recuperação → afeta a situação de R6; sem estimativa de variabilidade, as 12 h podem ser otimistas ou pessimistas.

**EX098.** Exemplo: "Necessidade: RTUs legadas numa concessionária de água aceitam comandos não autenticados pela LTE, pondo em risco o abastecimento de um hospital. Projeto: um gateway que acrescenta autenticação HMAC por estação, com contadores seguros diante de reinícios, retorno ao modo automático local e alarmes de estação inativa. Métodos: verificação em bancada, campanhas de injeção de falhas com semente e um ensaio de recuperação em sistemas sintéticos. Resultados: os requisitos de autenticação e de repetição foram atendidos, incluindo reinícios após uma correção; os alarmes atenderam aos 60 s; a restauração remota levou 12 h contra uma meta de 8 h, enquanto o abastecimento continuava localmente. Limitações: bancada sintética sem LTE real; um único ensaio de recuperação."

### Capítulo 50

**EX099.** Avaliado pela rubrica. Perguntas fortes incluem: "O que acontece se o HSM falhar?"; "Por que 60 s?"; "O que seu modelo de falhas não incluiu?"; "Quem é dono de D1?"; "O que mudaria se a reserva do hospital fosse de 1 h?"; as respostas citam itens do dossiê e declaram os limites.

**EX100.** (1) Acrescentar a declaração de que um único ensaio não dá estimativa de variabilidade; acrescentar 100 execuções simuladas de recuperação com semente, com faixas de duração das tarefas, e relatar a mediana e o percentil 90; Seção 7.4 e Apêndice C. (2) Citar a recomendação de profundidade de descarga do fabricante da bateria ou acrescentar uma tabela de sensibilidade para 0,5–0,8; Seção 5.2. (3) Substituir "impede" por "detecta" e acrescentar o contexto do tempo de detecção; resumo e Seção 8.1.

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
