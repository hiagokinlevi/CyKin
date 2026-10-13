# Operações de Segurança e Blue Team: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 130, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–32 de 50 já estão escritos em português, com os exercícios EX001–EX096 e suas resoluções com rubricas de 0 a 3 e 6 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 33–50 (EX097–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de engenharia que vão projetar, construir, verificar e operar sistemas de monitoramento de segurança e os processos de SOC em torno deles.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite ético e legal: monitore e responda apenas em sistemas que você está autorizado a defender; nada de código de exploração, *payloads*, procedimentos de ataque ou instruções para escapar da detecção. As detecções são ensinadas do lado do defensor, com telemetria sintética. Todas as evidências, pessoas e organizações são **sintéticas**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia em ordem: os capítulos de fundamentos aplicam matemática, computação e prática de engenharia às operações de segurança, e os capítulos de especialidade acompanham um único estágio num SOC, de um incidente de tomada de contas no portal do cliente até um projeto final validado que fecha uma lacuna de monitoramento nos depósitos. Execute cada laboratório onde ele aparece, tente os três exercícios antes das resoluções e pontue-se com as rubricas.

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Amara Osei** | Estudante de engenharia em estágio | Inventada |
| **Paolo Ricci** | Engenheiro de detecção e mentor | Inventado |
| **Kingsbridge Engineering University** | Universidade fictícia | Inventada |
| **Lindqvist Freight** | Empresa fictícia de logística que abriga o SOC | Inventada |

### Fontes principais

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) e [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker e Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) |

Capítulos 33–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-33), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) modelar uma fila de alertas com taxas de variação; (2) ler uma derivada como "quão rápido o acúmulo cresce"; (3) ligar modelos contínuos a dados horários; (4) explicar por que dimensionar a equipe de um SOC é um problema de taxas.

### 1.1 Por que cálculo num SOC

As operações de segurança lidam com fluxos: alertas chegam, analistas os resolvem, e o acúmulo é o que sobra. O cálculo é a linguagem da variação. Se A(t) é a taxa de chegada e C(t) a taxa de resolução, o acúmulo B(t) varia segundo dB/dt = A(t) − C(t). Quando as chegadas excedem a capacidade, o acúmulo sobe; quando a capacidade excede as chegadas, ele cai. A mesma equação descreve uma banheira enchendo com o ralo meio aberto. Para quem lidera um SOC, seu valor está em separar duas perguntas que as pessoas costumam misturar: quantos alertas chegaram hoje, e quão rápido eles chegaram em comparação com a velocidade com que a equipe consegue trabalhar. Um dia com total modesto ainda pode sobrecarregar um turno se a maioria dos alertas chegar em duas horas.

### 1.2 O caso do curso

**Amara Osei**, estudante de engenharia na fictícia **Kingsbridge Engineering University**, entra em estágio no centro de operações de segurança da fictícia **Lindqvist Freight**. Seu mentor é o engenheiro de detecção **Paolo Ricci**. No primeiro dia, o portal do cliente sofre uma rajada de logins malsucedidos, e a fila de alertas cresce mais rápido do que os dois analistas do turno conseguem resolver. A rajada é um padrão comum em páginas públicas de login: muitas tentativas falhas contra muitos nomes de usuário, muitas vezes a partir de uma pequena faixa de endereços. A primeira tarefa de Amara não é decidir se houve um ataque, mas entender por que a fila cresceu, o que leva diretamente às taxas. O mesmo incidente volta ao longo do livro, e cada capítulo o examina com uma ferramenta diferente.

### 1.3 Do contínuo ao discreto

Dados reais chegam em contagens horárias, não em curvas suaves. A derivada vira uma diferença: a variação do acúmulo por hora é igual às chegadas daquela hora menos os alertas tratados. A integral — o acúmulo total — vira uma soma acumulada. Em símbolos, B[n] = B[n−1] + A[n] − C[n], com a regra de que o acúmulo não pode ficar abaixo de zero, já que um analista ocioso não consegue resolver alertas que ainda não existem. O passo horário é uma escolha; contagens por minuto mostrariam mais detalhe, mas também mais ruído. Amara monta a soma acumulada primeiro numa planilha, uma linha por hora, para que cada passo possa ser conferido à mão.

### Laboratório — fila como taxa

```python
"""Alert queue as a rate problem: backlog change = arrivals - handled, per hour (synthetic)."""
arrivals = [40, 55, 70, 90, 85, 60, 45, 30]   # alerts per hour, 08:00-16:00
capacity = 60                                  # alerts the shift can triage per hour
backlog = 0
peak = 0
for h, a in enumerate(arrivals):
    handled = min(capacity, backlog + a)
    rate = a - handled
    backlog += rate
    peak = max(peak, backlog)
    print(f"{8+h:02d}:00 arrivals={a:3} handled={handled:3} d(backlog)/dt={rate:+4} backlog={backlog:3}")
print("peak backlog", peak, "| backlog at 16:00", backlog)
```

Execute com `python3 lab_queue.py`. Saída verificada:

```text
08:00 arrivals= 40 handled= 40 d(backlog)/dt=  +0 backlog=  0
09:00 arrivals= 55 handled= 55 d(backlog)/dt=  +0 backlog=  0
10:00 arrivals= 70 handled= 60 d(backlog)/dt= +10 backlog= 10
11:00 arrivals= 90 handled= 60 d(backlog)/dt= +30 backlog= 40
12:00 arrivals= 85 handled= 60 d(backlog)/dt= +25 backlog= 65
13:00 arrivals= 60 handled= 60 d(backlog)/dt=  +0 backlog= 65
14:00 arrivals= 45 handled= 60 d(backlog)/dt= -15 backlog= 50
15:00 arrivals= 30 handled= 60 d(backlog)/dt= -30 backlog= 20
peak backlog 65 | backlog at 16:00 20
```

### 1.4 Lendo o resultado

Com capacidade de 60 alertas por hora, o acúmulo fica em zero até as 10:00, depois cresce +10, +30 e +25 por hora e atinge o pico de 65 alertas às 13:00. Só começa a cair às 14:00 e ainda é 20 às 16:00. O pico acompanha a área entre a curva de chegadas e a linha de capacidade, não a pior hora isolada. A surpresa para Amara é que o acúmulo continua subindo depois que a pior hora passou. Enquanto as chegadas excedem sessenta, a fila cresce, ainda que mais devagar. Ela só cai quando as chegadas ficam abaixo da capacidade, e mesmo assim apenas no tamanho dessa diferença a cada hora. É por isso que a fila se arrastou pela tarde, embora a rajada em si tivesse terminado no começo da tarde.

### 1.5 Significado para a engenharia

Acrescentar um analista às 10:00 elevaria a capacidade acima da taxa máxima de chegada e manteria o acúmulo perto de zero. São as taxas, e não os totais diários, que dizem quando é preciso ajuda. O mesmo modelo responde também a outras perguntas: quanto tempo um acúmulo de 65 leva para ser zerado com uma dada capacidade ociosa, ou com que antecedência a ajuda precisa chegar para manter o pico abaixo de uma meta. Paolo lembra que analistas reais não resolvem alertas a uma taxa fixa, já que alertas difíceis levam mais tempo, por isso o modelo dá uma estimativa de planejamento, não uma previsão precisa.

### Exemplo resolvido

Paolo pergunta a Amara quanto tempo espera um alerta que chega às 12:00. Ela raciocina que ele entra numa fila de 40 alertas com capacidade de 60 por hora, então espera cerca de 40 minutos até que um analista chegue a ele — tempo suficiente para fazer diferença num ataque de credenciais em andamento.

> **Caso sintético.** A Lindqvist Freight, a Kingsbridge University, Amara e Paolo são inventados; as contagens vêm do script do laboratório.

### Erros e limites

O modelo supõe que todo alerta leva o mesmo tempo e que os analistas nunca fazem pausas; o tempo real de triagem varia muito, então trate os resultados como primeiras estimativas.

### Exercícios

- **EX001 — Equação do acúmulo.** Escreva a equação da variação do acúmulo e explique cada termo. *Rubrica:* 3 = dB/dt = A − C, com chegadas e resolução explicadas; 2 = equação sem significado; 1 = só palavras; 0 = nada.
- **EX002 — Momento do pico.** Quando e por que o acúmulo atinge o pico no laboratório? *Rubrica:* 3 = 13:00, com 65; as chegadas excedem a capacidade das 10:00 às 12:00 e se igualam a ela às 13:00; 2 = só o valor do pico; 1 = horário errado; 0 = nada.
- **EX003 — Tempo de espera.** Estime a espera de um alerta que chega às 12:00. *Rubrica:* 3 = cerca de 40 minutos, a partir de 40 na fila a 60/h; 2 = método sem número; 1 = palpite; 0 = nada.

### Síntese

As filas de alertas seguem taxas; tratar chegadas e capacidade como funções do tempo mostra quando os acúmulos se formam e quanta capacidade extra os elimina.

### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) usar conjuntos e relações para descrever usuários, hosts e alertas; (2) aplicar lógica a condições de detecção; (3) contar combinações para regras de correlação; (4) raciocinar sobre grafos de logons.

### 2.1 Conjuntos na detecção

Uma detecção muitas vezes faz perguntas de conjuntos. Quais usuários falharam no login a partir da rede N? Quais deles tiveram sucesso depois? Se F é o conjunto de nomes de usuário com falhas e S o conjunto com sucessos a partir da mesma rede, F ∩ S são as contas que podem ter sido adivinhadas corretamente. A notação de conjuntos transforma um palpite vago numa consulta precisa. A interseção não prova comprometimento; um cliente que digitou a senha errada duas vezes e depois acertou também cai em F ∩ S. O que ela faz é encolher a lista, de todos os que falharam para os poucos que merecem um olhar mais atento, que é o que uma etapa de triagem deve fazer.

### 2.2 Lógica

Condições de regras são fórmulas lógicas. "O processo é PowerShell E o pai é um aplicativo do Office" é uma conjunção; acrescentar OU amplia uma regra; acrescentar NÃO a estreita. Escrever as condições em lógica deixa seu escopo explícito e testável, e é assim que o formato Sigma expressa a lógica de detecção. Erros de lógica produzem erros reais: escrever OU onde se queria E pode transformar uma regra precisa numa que dispara em todo documento do Office. Tabelas-verdade ajudam a conferir regras pequenas, listando cada combinação de condições e o resultado esperado. As regras Sigma usam seleções nomeadas unidas numa linha de condição, o que mantém a lógica legível mesmo quando cada seleção tem muitos campos.

### 2.3 Relações e grafos

Um logon do usuário u no host h é um par (u, h). Juntos, os pares formam um grafo bipartido. Uma conta que de repente se conecta a muitos hosts novos aparece como um nó cujo grau salta. Grau, aqui, significa o número de hosts distintos que uma conta toca numa janela de tempo. Uma conta do suporte técnico pode normalmente se conectar a dezenas, enquanto um auxiliar de folha de pagamento se conecta a dois ou três, de modo que o salto importa em relação ao histórico de cada conta. Os grafos também mostram caminhos, como uma conta que chega a um servidor por um host intermediário, coisa que listas de pares escondem.

### 2.4 Contagem

Regras de correlação combinam eventos. Com 7 tipos de evento, uma regra sobre quaisquer 3 tipos em ordem tem 7 × 6 × 5 = 210 possibilidades. A contagem mostra por que a correlação exaustiva explode e por que as regras precisam ser escolhidas a partir do conhecimento de ameaças, como as técnicas do MITRE ATT&CK. Se a ordem não importa, a contagem cai para a combinação de 7 escolhe 3, que é 35, mas acrescentar janelas de tempo e condições de campo multiplica de novo as possibilidades. Nenhuma equipe consegue escrever e testar centenas de correlações, então o conhecimento de ameaças estreita a busca às sequências que os atacantes de fato usam. O ATT&CK oferece essa base ao descrever técnicas observadas em intrusões reais.

### 2.5 Uso no caso

Durante a rajada no portal, Amara lista F (nomes de usuário com falhas a partir de 203.0.113.0/24) e S (nomes de usuário com sucesso a partir da mesma rede). Um nome, u5, está nos dois: uma conta de cliente candidata a comprometida. A faixa de endereços 203.0.113.0/24 é reservada para documentação, o que convém a um caso sintético. Amara escreve os dois conjuntos de forma explícita, o que permite a Paolo conferir o raciocínio dela linha a linha. O próximo passo não é bloquear u5 de imediato, mas verificar os detalhes do sucesso, como horário, dispositivo e o que a sessão fez, antes de decidir a ação.

### 2.6 Precisão da linguagem

A matemática discreta obriga a uma linguagem exata: "muitos" vira "mais de 5 nomes de usuário distintos em 10 minutos". Essa precisão torna as regras revisáveis. Revisável significa que outro analista pode ler a regra e concordar, ou discordar, sobre o que ela deveria pegar. "Muitos" convida a discussões; "mais de cinco em dez minutos" convida a um teste. A versão precisa também pode ser ajustada com evidências, contando com que frequência usuários legítimos ultrapassam cinco falhas em dez minutos e ajustando o limiar com dados, e não com opinião. Todo limiar deve trazer suas unidades.

### Exemplo resolvido

Amara escreve a condição da regra assim: count(distinct username where result = fail and source in N, 10 min) > 5 AND exists(username in that set where result = ok). Paolo observa que a segunda cláusula transforma um alerta ruidoso de *spray* num alerta mais certeiro de "possível comprometimento".

> **Caso sintético.** Os nomes de usuário e as redes são sintéticos.

### Erros e limites

A lógica de conjuntos é exata, mas os dados não são: logs ausentes tornam os conjuntos incompletos, então resultados vazios não provam ausência.

### Exercícios

- **EX004 — Interseção.** Por que F ∩ S importa no caso do portal? *Rubrica:* 3 = contas que falharam e depois tiveram sucesso a partir da mesma rede: possíveis credenciais adivinhadas; 2 = parcial; 1 = só a definição de conjunto; 0 = nada.
- **EX005 — Contagem de correlações.** Quantas sequências ordenadas de 3 tipos saem de 7 tipos de evento, e o que isso implica? *Rubrica:* 3 = 210; a correlação exaustiva explode, escolha pelo conhecimento de ameaças; 2 = só o número; 1 = número errado; 0 = nada.
- **EX006 — Regra mais certeira.** O que a segunda cláusula da regra de Amara acrescenta? *Rubrica:* 3 = transforma o alerta de *spray* em alerta de possível comprometimento ao exigir um sucesso; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Conjuntos, lógica, grafos e contagem dão significado exato às regras de detecção e mostram por que a escolha das regras deve ser guiada pelo conhecimento de ameaças.

### Continue estudando — capítulo 02 de 50

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar limites físicos ao projeto de sensores e de armazenamento; (2) raciocinar sobre sinal, ruído e amostragem na telemetria; (3) estimar energia e calor para a infraestrutura do SOC; (4) reconhecer modos de falha física.

### 3.1 Sinais e ruído

A física descreve medições como sinal mais ruído. A telemetria é parecida: a atividade real de ataque é o sinal, a atividade normal é o ruído. Um sensor que amostra raramente demais perde sinais curtos, assim como um osciloscópio lento perde pulsos rápidos. A razão entre os dois decide quão fácil é a detecção. Um ataque ruidoso contra uma rede silenciosa se destaca; um ataque discreto escondido em tráfego normal intenso, não. Os defensores podem melhorar essa razão coletando campos que separam os dois, como a filiação de processos, em vez de simplesmente coletar mais dados, que acrescentam ruído tão depressa quanto sinal.

### 3.2 Amostragem

Se um sensor de rede exporta resumos de fluxo a cada 5 minutos, uma rajada de 20 segundos aparece diluída num único registro. Amostragem mais rápida resolve rajadas, mas multiplica o volume de dados. A engenharia escolhe uma taxa que resolva os sinais de interesse a um custo aceitável. A diluição é um efeito de média: a intensidade da rajada espalhada por cinco minutos parece uma alta leve, e não um pico. Uma regra ajustada com dados por minuto deixaria de vê-la. Amara compara os logs web por requisição do portal com os resumos de fluxo de cinco minutos do mesmo período e vê com clareza o ritmo da rajada num deles, enquanto o outro guarda apenas um único registro grande.

### 3.3 Energia e calor

Um cluster de SIEM consome energia elétrica e a transforma em calor. Dobrar a ingestão pode exigir mais servidores, mais refrigeração e mais espaço em *rack*. A capacidade física limita quanta telemetria um SOC consegue guardar. O consumo de energia de cada servidor vira quase todo calor, que a refrigeração precisa remover, de modo que os orçamentos de energia e de refrigeração crescem juntos. Uma sala de dados com refrigeração fixa pode chegar ao limite antes que acabe o orçamento para servidores. Planejar o crescimento da ingestão envolve, portanto, a equipe de instalações, e não só a equipe do SIEM, e a retenção longa pode sair mais barata em armazenamento de arquivo mais lento e mais frio.

### 3.4 Falhas físicas

Discos se desgastam, fontes de alimentação falham, fibras são cortadas. A infraestrutura de monitoramento precisa de redundância; um único coletor com falha pode silenciar os logs de um site inteiro. Um coletor silencioso é pior do que um ruidoso, porque a ausência de logs pode parecer ausência de ataques. Por isso os SOCs monitoram o monitoramento: cada fonte tem um volume esperado, e uma queda brusca gera seu próprio alerta. Coletores redundantes, fontes duplas e caminhos de rede separados reduzem a chance de que uma única falha deixe um site inteiro às cegas.

### 3.5 Tempo e relógios

Os relógios derivam porque os osciladores são dispositivos físicos. O NTP os mantém próximos, mas uma deriva de segundos pode reordenar eventos entre hosts. O NIST SP 800-92 enfatiza a sincronização de tempo na gestão de logs. A ordem importa nas investigações: o login veio antes do acesso ao arquivo ou depois? O Network Time Protocol ajusta cada relógio em relação a servidores de referência, normalmente mantendo a deriva em milissegundos numa rede saudável. Os logs devem registrar horários em UTC, com o fuso declarado, para que eventos de regiões diferentes possam ser comparados sem erros de conversão.

### 3.6 Ligação com o caso

Os logs do portal da Lindqvist vêm de três servidores web. O relógio de um deles está 4 segundos adiantado, de modo que as falhas registradas ali aparecem um pouco depois de terem acontecido. Quatro segundos parecem triviais, mas durante uma rajada de várias tentativas por segundo eles reordenam eventos entre servidores. Um sucesso em outro servidor poderia parecer ter acontecido antes das falhas que o precederam. Amara anota o desvio em sua análise e o corrige em vez de editar os logs, e a equipe de operações conserta a sincronização de tempo do servidor.

### Segurança eletromagnética e física

O acesso físico a armários de rede permite que alguém acrescente um *tap* ou desconecte um sensor. Sensores, coletores e seu cabeamento fazem parte do ambiente monitorado e precisam de fechaduras e alarmes contra violação.

### Exemplo resolvido

Amara compara os resumos de fluxo de 5 minutos do portal com os logs web por requisição. Os fluxos mostram um único registro grande para 203.0.113.0/24 às 10:05; os logs web mostram, dentro dele, 600 tentativas espalhadas por 40 segundos. Ela anota que os dados de fluxo detectaram a rajada, mas não conseguiram mostrar seu ritmo.

> **Caso sintético.** Os servidores e os números são inventados.

### Erros e limites

Analogias físicas ajudam a intuição, mas o ruído da telemetria não é aleatório no sentido físico; ele segue padrões do negócio.

### Exercícios

- **EX007 — Efeito da amostragem.** O que acontece com uma rajada de 20 segundos em resumos de fluxo de 5 minutos? *Rubrica:* 3 = diluída num único registro; o ritmo se perde; 2 = parcial; 1 = vago; 0 = nada.
- **EX008 — Deriva do relógio.** Por que um erro de relógio de 4 segundos importa? *Rubrica:* 3 = reordena eventos entre hosts; é preciso sincronizar o tempo (SP 800-92); 2 = parcial; 1 = não importa; 0 = nada.
- **EX009 — Capacidade física.** Como a física limita a retenção de telemetria? *Rubrica:* 3 = energia, refrigeração, espaço e disco limitam servidores e armazenamento; 2 = um fator; 1 = vago; 0 = nada.

### Síntese

Os limites físicos de amostragem, relógios e infraestrutura determinam que telemetria um SOC consegue coletar e em qual pode confiar.

### Continue estudando — capítulo 03 de 50

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas pequenos que leem e resumem registros de log; (2) usar variáveis, laços, condições e funções; (3) testar um programa com entradas conhecidas; (4) manter o código legível para revisores.

### 4.1 Programas como procedimentos precisos

Um programa é um procedimento que o computador segue à risca. Num SOC, programas pequenos contam, filtram e resumem registros mais rápido e de forma mais consistente do que pessoas. Por serem exatos, os erros neles também se repetem exatamente, por isso precisam ser testados. Uma pessoa contando logins malsucedidos a olho pode deixar passar algumas linhas ou contar uma duas vezes, e cada contagem sairia um pouco diferente. Um programa dá a mesma resposta todas as vezes, o que é tranquilizador quando ele está certo e perigoso quando está errado. É por isso que os scripts do SOC são revisados e testados como qualquer outro artefato de engenharia antes que os analistas confiem em sua saída.

### 4.2 Construções básicas

Variáveis guardam valores, como uma contagem. Laços visitam cada registro. Condições escolhem o que contar. Funções empacotam uma etapa, como "extrair a rede /24 de um endereço", para que possa ser reutilizada e testada isoladamente. O primeiro script de Amara usa as quatro: um dicionário de contagens indexado por rede, um laço sobre as linhas de log, uma condição que seleciona os logins malsucedidos e uma função que devolve o prefixo /24. Manter a etapa do prefixo em sua própria função permite testá-la com endereços capciosos, como os que ficam na borda de uma faixa, sem rodar o script inteiro.

### 4.3 Lendo registros

Os logs chegam como linhas de texto ou como registros estruturados. Um programa divide cada linha em campos, converte tipos (texto em números ou horários) e trata linhas malformadas sem travar, registrando quantas foram puladas. Logs reais contêm linhas truncadas, codificações inesperadas e campos em formatos estranhos. Um script que trava na primeira linha ruim não dá resposta alguma; um que ignora as linhas ruins em silêncio pode dar uma resposta errada. Contar as linhas puladas e informá-las junto com os resultados permite ao leitor julgar se os dados estavam limpos o bastante para merecer confiança.

### 4.4 Testando com entradas conhecidas

Antes de rodar sobre logs reais, Amara alimenta sua função com cinco linhas feitas à mão cuja resposta correta ela já conhece. Se a saída diferir, o código está errado, não os dados. Suas cinco linhas incluem uma falha comum, um sucesso, uma linha malformada, um endereço na fronteira de uma faixa /24 e uma linha com horário de outro fuso. Cada uma testa um erro possível. Quando a primeira execução conta a linha malformada como falha, ela corrige o analisador e roda de novo antes de tocar em dados reais.

### 4.5 Legibilidade

Funções curtas, nomes claros e comentários sobre a intenção ajudam Paolo a revisar o código dela. Código que só o autor entende é um risco nas operações. Num SOC, os scripts muitas vezes são executados às 3 da manhã, durante um incidente, por alguém que não é o autor. Uma função chamada `failed_logins_by_network` se explica sozinha; uma chamada `proc2`, não. Os comentários devem dizer por que uma etapa existe, por exemplo que uma fonte de logs grava a hora local, em vez de repetir o que o código faz.

### 4.6 Biblioteca padrão primeiro

A biblioteca padrão do Python lê CSV, JSON e datas. Usá-la evita instalar pacotes não revisados nas máquinas do SOC. Cada pacote instalado é código de fora da organização rodando em máquinas que veem dados sensíveis. Cada um exige revisão, atualizações e confiança em seus mantenedores. Para contar, filtrar e analisar formatos comuns, a biblioteca padrão basta, e as máquinas do SOC ficam mais simples de proteger e de reconstruir. Ferramentas maiores são acrescentadas de forma deliberada quando surge uma necessidade real. Paolo mantém uma lista curta de pacotes aprovados, cada um com um responsável nomeado que acompanha suas atualizações.

### Controle de versão

Amara mantém seus scripts no repositório de controle de versão da equipe. Cada mudança tem uma mensagem explicando o porquê, e Paolo revisa as mudanças antes que rodem sobre dados de produção. O histórico permite à equipe ver qual versão produziu um dado resultado.

### Exemplo resolvido

A primeira função de Amara devolve a rede /24 de um endereço IPv4. Seus casos de teste incluem "203.0.113.14" → "203.0.113.0/24" e um "203.0.113" malformado, que deve devolver None em vez de travar. Um teste falha de início porque ela esqueceu o caso malformado; ela o corrige antes de usar a função nos logs do portal.

> **Caso sintético.** O código e os dados são sintéticos.

### Erros e limites

Testes aprovados mostram que o código trata os casos em que você pensou, não todos os casos; acrescente testes quando novas entradas surpreenderem você.

### Exercícios

- **EX010 — Linhas malformadas.** Como um programa de logs deve tratar linhas malformadas? *Rubrica:* 3 = pular sem travar e contar as linhas puladas; 2 = só pular; 1 = travar; 0 = nada.
- **EX011 — Teste com entradas conhecidas.** Por que testar primeiro com linhas feitas à mão? *Rubrica:* 3 = a resposta correta é conhecida, então as diferenças revelam erros no código; 2 = parcial; 1 = nenhum motivo; 0 = nada.
- **EX012 — Biblioteca padrão.** Por que preferir a biblioteca padrão nas máquinas do SOC? *Rubrica:* 3 = evita pacotes de terceiros não revisados; já está disponível; 2 = parcial; 1 = velocidade; 0 = nada.

### Síntese

Programas pequenos, testados e legíveis tornam a análise de logs consistente; sua exatidão só é uma força quando são verificados.

### Continue estudando — capítulo 04 de 50

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever notas técnicas, chamados e documentos de projeto claros; (2) adaptar a comunicação a analistas, gestores e clientes; (3) apresentar dados com honestidade em tabelas e gráficos; (4) usar linguagem precisa para a incerteza.

### 5.1 Públicos

Analistas precisam de campos e horários exatos; gestores precisam de impacto e decisões; clientes precisam saber o que aconteceu e o que fazer. Um incidente produz vários documentos, cada um escrito para seu leitor. Escrever um único documento para os três falha com todos eles: os analistas perdem detalhes, os gestores se afogam neles, os clientes recebem jargão. Amara começa cada texto perguntando o que o leitor precisa fazer depois de lê-lo. Essa pergunta decide o que incluir, dos nomes de campo para o analista a uma única decisão recomendada para o gestor.

### 5.2 Chamados

Um bom chamado de SOC declara o que foi observado, quando (com fuso horário), em quais ativos, o que foi feito e o que ainda é desconhecido. Knerler, Parker e Zimmerman (2022) enfatizam a comunicação clara como uma estratégia de SOC por si só. Declarar o que é desconhecido é a parte mais pulada, mas é ela que diz ao próximo turno onde procurar. Um horário sem fuso obriga o leitor a adivinhar, e um palpite errado pode reordenar a história. Os ativos devem ser nomeados pelos identificadores usados no inventário de ativos, para que outras equipes os encontrem sem precisar perguntar.

### 5.3 Documentos de projeto

Mudanças de engenharia, como uma nova detecção, precisam de um documento de projeto curto: problema, proposta, alternativas, riscos, plano de testes e reversão. Escrever as alternativas obriga o autor a mostrar por que a proposta supera outras opções, e não apenas que ela funciona. Um plano de testes declara como se vai mostrar que a detecção dispara no comportamento-alvo e fica em silêncio na atividade normal. A reversão explica como remover a mudança depressa se ela inundar a fila depois da implantação. Paolo revisa cada documento antes de a regra entrar em produção.

### 5.4 Gráficos honestos

Os gráficos devem começar os eixos de contagens no zero, rotular unidades e fusos horários e evitar suavizar picos que importam. Um eixo de contagem que começa em 900 pode fazer uma alta de 950 para 1.000 parecer uma duplicação. Fusos horários sem rótulo podem deslocar um pico para o turno errado. Suavizar com uma média móvel longa deixa as linhas de tendência arrumadas, mas pode apagar justamente a rajada que um gráfico de incidente deveria mostrar, por isso as contagens brutas devem aparecer ao lado de qualquer linha suavizada. As legendas declaram a fonte dos dados.

### 5.5 Palavras para a incerteza

"Confirmado", "provável" e "possível" devem ser usados de forma consistente. A equipe de Amara os define num guia de estilo para que os leitores saibam quão seguro o autor está. Sem significados acordados, o "provável" de um autor é o "possível" de outro, e um gestor pode agir com base numa afirmação mais forte do que a evidência sustenta. O guia de estilo liga cada palavra à evidência esperada: "confirmado" exige evidência direta, como uma entrada de log; "provável" exige vários indicadores consistentes; e "possível" marca uma pista ainda não verificada. O guia cabe numa página.

### 5.6 Caso

Depois da rajada no portal, Amara escreve três peças: o chamado para os analistas, um resumo para o gestor e um rascunho de aviso ao cliente dono da conta u5, revisados por Paolo e pela equipe de comunicação. O chamado lista as contagens de falhas, a rede, o horário do login bem-sucedido de u5 e as ações da sessão, com os horários em UTC. O resumo para o gestor dá o impacto em duas frases e declara o que já foi feito e a mudança agora proposta. O aviso ao cliente explica em palavras simples que foi vista uma atividade de acesso incomum e o que o cliente deve fazer.

### Revisão antes do envio

Tudo o que sai do SOC é revisado por uma segunda pessoa: uma confere os fatos contra o chamado, a outra confere o tom e a clareza. Nos avisos a clientes, a equipe de comunicação aprova a redação final, porque um aviso enganoso pode fazer mais mal do que o próprio incidente. Amara guarda as versões revisadas junto com o chamado.

### Exemplo resolvido

O resumo de Amara para o gestor: "Na segunda-feira, das 10:05 às 10:06 UTC, cerca de 600 tentativas de login a partir de uma rede miraram contas do portal do cliente. Uma conta de cliente foi acessada com sucesso e foi bloqueada; o cliente foi contatado. Nenhum sistema de funcionários foi afetado. Propõe-se uma mudança no limite de taxa."

> **Caso sintético.** O incidente e os textos são inventados.

### Erros e limites

Escrita clara não conserta fatos errados; confira os números contra as fontes antes de enviar.

### Exercícios

- **EX013 — Campos do chamado.** Liste cinco coisas que um bom chamado de SOC declara. *Rubrica:* 3 = o observado, horário com fuso, ativos, ações, desconhecidos; 2 = três; 1 = uma; 0 = nada.
- **EX014 — Palavras de incerteza.** Por que definir "confirmado", "provável" e "possível" num guia de estilo? *Rubrica:* 3 = o significado consistente permite aos leitores saber o grau de certeza; 2 = parcial; 1 = só estilo; 0 = nada.
- **EX015 — Resumo para o gestor.** O que o resumo de Amara inclui e o que deixa de fora? *Rubrica:* 3 = horário, escala, impacto, ações, proposta; deixa de fora o detalhe técnico bruto; 2 = parcial; 1 = cópia do chamado; 0 = nada.

### Síntese

Comunique para cada leitor, com incerteza precisa e gráficos honestos; a clareza faz parte da engenharia de SOC.

### Continue estudando — capítulo 05 de 50

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar integrais para totalizar quantidades ao longo do tempo; (2) aplicar crescimento e decaimento exponenciais a volumes de logs e à retenção; (3) usar aproximações por séries no planejamento de capacidade; (4) ligar modelos contínuos aos custos de armazenamento.

### 6.1 Integrais como totais

O armazenamento necessário para os logs é a integral da taxa de ingestão ao longo do período de retenção. Se um SIEM ingere r(t) gigabytes por dia, o armazenamento depois de T dias é a área sob r(t) de 0 a T. Quando a taxa é constante, a área é só um retângulo: taxa vezes dias. A ingestão real sobe nos dias úteis, cai nos fins de semana e salta durante incidentes, de modo que a área tem uma borda superior irregular. Somar os números diários dos próprios relatórios de volume do SIEM dá a área diretamente, e comparar essa soma com a estimativa do retângulo mostra quanto o modelo simples deixa escapar.

### 6.2 Crescimento exponencial

Se o volume de logs cresce 3% ao mês, o volume depois de n meses é V₀·1,03ⁿ. Depois de dois anos, ele quase dobra. Planos de capacidade que supõem volume constante falham. A duplicação vem de 1,03²⁴ ≈ 2,03. Um atalho útil é a regra dos 70: dividir 70 pela taxa percentual de crescimento dá o tempo aproximado de duplicação, aqui cerca de 23 meses. Um crescimento assim vem da conexão de novos sistemas, de logs mais verbosos depois de incidentes e da expansão do negócio, por isso tende a continuar, a menos que alguém corte fontes de forma deliberada. Amara traça as duas projeções.

### 6.3 Decaimento

O valor dos logs antigos decai: a maioria das investigações usa dados recentes. Um modelo simples trata a chance de precisar dos logs de um dia como decaindo exponencialmente com a idade, o que orienta o armazenamento em camadas — quente, morna, fria. Sob esse modelo, se a chance de precisar de um dado dia cai pela metade a cada mês, logs de três meses são necessários com um oitavo da frequência dos recentes. Isso sugere armazenamento rápido e caro para os dados recentes e armazenamento mais lento e barato depois. O modelo é uma simplificação: algumas investigações, como casos lentos de ameaça interna, voltam muito atrás, e é por isso que a camada fria é mantida pesquisável em vez de descartada.

### 6.4 Aproximações

Para taxas de crescimento pequenas, (1 + g)ⁿ ≈ 1 + ng em períodos curtos, uma verificação rápida para planilhas. A 3% ao longo de três meses, a estimativa linear dá 9% contra 9,27% exatos, perto o bastante para uma checagem de sanidade. Ao longo de dois anos, ela dá 72% contra 103% exatos, muito errado. O valor da aproximação está em pegar rapidamente erros grosseiros de planilha, como uma vírgula decimal fora do lugar, e não em substituir o cálculo exato no planejamento. Amara a usa para conferir sua planilha de armazenamento: uma alta mensal de 3% ao longo de um trimestre deve acrescentar cerca de 9% à ingestão, e uma célula mostrando 90% apontaria direto para uma vírgula decimal fora do lugar.

### 6.5 Caso

O SIEM da Lindqvist ingere 120 GB por dia e mantém 90 dias na camada quente. Paolo pergunta a Amara se a camada quente atual, de 12 TB, vai durar um ano caso o volume cresça 3% ao mês. A pergunta tem duas partes: quanto armazenamento quente a taxa de hoje exige, e como essa necessidade muda à medida que a ingestão cresce ao longo do ano. Amara a monta como uma taxa multiplicada pela janela de retenção, primeiro com a taxa de hoje e depois com a taxa daqui a um ano. Ela observa que a camada quente guarda uma janela móvel, então o que importa é a taxa de ingestão no momento, e não o total coletado durante o ano.

### 6.6 Regras de retenção

A retenção também é definida por política e por lei; o NIST SP 800-92 recomenda definir a retenção por tipo de log. A matemática informa o custo; a política decide os mínimos. Um tipo de log necessário para auditorias regulatórias pode precisar ser guardado por anos, mesmo que as investigações raramente o toquem; logs de depuração de um sistema de teste podem ser guardados por dias. O SOC propõe a retenção com base no valor investigativo, as equipes jurídica e de conformidade definem os mínimos, e o custo de armazenamento determina em que camada cada tipo fica em cada fase de sua vida.

### Taxas de variação do custo

A derivada do custo de armazenamento em relação aos dias de retenção é o custo diário de ingestão. Ver o custo como uma taxa ajuda os gestores a comparar guardar mais dez dias de logs com outros usos do orçamento. Amara apresenta o custo total e o custo marginal de cada tipo de log, para que as decisões possam ser tomadas fonte por fonte, e não todas de uma vez.

### Exemplo resolvido

Amara calcula a necessidade quente de hoje: 120 GB × 90 = 10,8 TB. Em 12 meses, a ingestão será de 120 × 1,03¹² ≈ 171 GB/dia, então 90 dias exigem cerca de 15,4 TB, acima dos 12 TB. Ela recomenda mover os logs de *firewall* com mais de 30 dias para a camada morna.

> **Caso sintético.** Os volumes e as camadas são inventados.

### Erros e limites

O crescimento raramente segue uma curva suave; novas fontes de logs acrescentam degraus. Revise os planos a cada trimestre.

### Exercícios

- **EX016 — Integral do armazenamento.** Expresse o armazenamento como uma integral e calcule a necessidade quente de hoje. *Rubrica:* 3 = área sob a ingestão ao longo da retenção; 10,8 TB; 2 = uma parte; 1 = errado; 0 = nada.
- **EX017 — Efeito do crescimento.** Que armazenamento quente será necessário em 12 meses com crescimento de 3% ao mês? *Rubrica:* 3 = cerca de 171 GB/dia, 15,4 TB, acima de 12 TB; 2 = parcial; 1 = suposição de volume constante; 0 = nada.
- **EX018 — Política versus matemática.** O que decide a retenção mínima, e o que a matemática decide? *Rubrica:* 3 = política/lei definem o mínimo; a matemática informa custo e camadas; 2 = parcial; 1 = a matemática decide tudo; 0 = nada.

### Síntese

Integrais e modelos de crescimento transformam taxas de ingestão em planos de armazenamento, dentro dos limites de retenção definidos pela política.

### Continue estudando — capítulo 06 de 50

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) aplicar a regra de Bayes à precisão dos alertas; (2) distinguir a taxa de falsos positivos da precisão; (3) resumir dados com medianas e percentis; (4) reconhecer efeitos da taxa-base.

### 7.1 Probabilidade condicional

Duas perguntas são fáceis de confundir. "Se um ataque acontece, qual a probabilidade de um alerta?" é a taxa de verdadeiros positivos. "Se um alerta dispara, qual a probabilidade de um ataque?" é a precisão. A regra de Bayes liga as duas por meio da taxa-base. Confundi-las leva a decisões ruins. Um fornecedor pode anunciar que seu detector pega 99% dos ataques, que é a taxa de verdadeiros positivos, enquanto os analistas vivem outra coisa: a maioria dos alertas que abrem acaba sendo benigna. A regra de Bayes mostra como as duas coisas podem ser verdadeiras ao mesmo tempo, porque a precisão depende fortemente de quão raros são os ataques entre os eventos avaliados.

### 7.2 Taxas-base

Axelsson (2000) mostrou que, quando os ataques são raros entre os eventos, mesmo um bom detector produz principalmente alarmes falsos. A precisão cai à medida que a prevalência cai. O argumento de Axelsson aplicou isso aos sistemas de detecção de intrusão numa época em que os fornecedores se concentravam nas taxas de detecção. Suponha que apenas um evento em dez mil seja malicioso; mesmo uma taxa de falsos positivos de um em mil produz dez alarmes falsos para cada verdadeiro. A lição prática é que as taxas de falsos positivos precisam ser extremamente baixas, ou os alertas precisam ser filtrados mais antes de chegar às pessoas.

### Laboratório — Bayes para uma regra

```python
"""Bayes' rule for one detection rule at Lindqvist Freight (synthetic figures)."""
p_attack = 0.002          # share of evaluated logon bursts that are credential stuffing
tpr, fpr = 0.90, 0.01
p_alert = tpr * p_attack + fpr * (1 - p_attack)
ppv = tpr * p_attack / p_alert
print(f"P(alert)={p_alert:.5f}  P(attack|alert)={ppv:.3f}")
print(f"per 100,000 bursts: true alerts={tpr*p_attack*1e5:.0f} false alerts={fpr*(1-p_attack)*1e5:.0f}")
```

Execute com `python3 lab_bayes.py`. Saída verificada:

```text
P(alert)=0.01178  P(attack|alert)=0.153
per 100,000 bursts: true alerts=180 false alerts=998
```

### 7.3 Lendo o resultado

Com 0,2% das rajadas de logon sendo *credential stuffing*, uma taxa de verdadeiros positivos de 90% e uma taxa de falsos positivos de 1%, a precisão é 0,153: cerca de um alerta em sete é real. A cada 100.000 rajadas, esperam-se 180 alertas verdadeiros e 998 falsos. Ver as contagens deixa o ponto evidente: 998 alarmes falsos contra 180 reais. Reduzir a taxa de falsos positivos à metade, para 0,5%, cortaria os alarmes falsos para 499 e elevaria a precisão para cerca de 0,27, então melhorar a especificidade compensa mais do que melhorar a detecção aqui. Amara confere a aritmética montando a tabela completa de ataques e não ataques antes de confiar no resultado da fórmula.

### 7.4 Resumos

Os tempos de triagem são assimétricos: a maioria é rápida, alguns levam horas. Medianas e percentis 90 os descrevem melhor do que médias. Algumas investigações longas podem puxar a média muito acima do que um alerta típico leva, dando uma imagem enganosa do trabalho diário. A mediana diz quanto custa um alerta típico; o percentil 90 mostra quanto duram os lentos, o que importa para dimensionar a equipe. Amara relata os dois, com o número de alertas da amostra, para que os leitores vejam quão sólidos são os números.

### 7.5 Usando a estatística

Amara usa esses números para argumentar que a regra de rajada precisa de uma segunda condição (um sucesso dentro da rajada) para elevar a precisão antes de acionar analistas à noite. Exigir um sucesso dentro da rajada muda a taxa-base: rajadas com sucesso formam um grupo muito menor e mais suspeito, de modo que uma fração muito maior dos alertas que disparam sobre elas é real. A contrapartida é que ataques que falham por completo deixam de acionar alguém à noite. Amara propõe registrá-los numa fila de revisão diurna para que ainda sejam vistos.

### Intervalos para taxas

Uma taxa observada de falsos positivos de 1% em 2.000 rajadas benignas tem incerteza: a taxa verdadeira pode ser um pouco maior ou menor. Amara relata as taxas com intervalos de 95% e anota o tamanho da amostra, para que os leitores não tratem 1% como exato. Quando as amostras são pequenas, ela o diz e evita decisões que dependam de diferenças finas entre regras. Paolo pede que toda proposta de regra inclua a amostra em que suas taxas foram medidas.

### Exemplo resolvido

Paolo pergunta: "Se reduzirmos a taxa de falsos positivos à metade, o que acontece?" Amara refaz o cálculo com 0,5%: a precisão sobe para cerca de 0,27. Reduzir os falsos positivos à metade quase dobra a fração de alertas reais, o que é mais útil do que elevar a sensibilidade de 90% para 95%.

> **Caso sintético.** As taxas vêm do script do laboratório; o caso de 0,5% é o recálculo dela.

### Erros e limites

Taxas estimadas a partir de amostras pequenas são incertas; relate intervalos quando possível.

### Exercícios

- **EX019 — Duas perguntas.** Distinga taxa de verdadeiros positivos de precisão. *Rubrica:* 3 = P(alerta dado ataque) vs P(ataque dado alerta); 2 = parcial; 1 = são a mesma coisa; 0 = nada.
- **EX020 — Precisão do laboratório.** Que precisão o laboratório dá, e o que ela significa? *Rubrica:* 3 = 0,153; cerca de 1 em 7 alertas é real; 180 vs 998; 2 = só o número; 1 = errado; 0 = nada.
- **EX021 — Qual alavanca.** Por que reduzir a taxa de falsos positivos à metade vale mais do que elevar a sensibilidade aqui? *Rubrica:* 3 = taxa-base baixa: os FP dominam; a precisão sobe para cerca de 0,27; 2 = parcial; 1 = a sensibilidade é melhor; 0 = nada.

### Síntese

A regra de Bayes e as taxas-base explicam por que a precisão, e não apenas a taxa de detecção, decide se uma regra é útil.

### Continue estudando — capítulo 07 de 50

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) explicar como CPU, memória, armazenamento e E/S moldam a telemetria; (2) relacionar processos e privilégio aos eventos de *endpoint*; (3) raciocinar sobre os custos de desempenho dos sensores; (4) identificar fontes arquiteturais de evidência.

### 8.1 Componentes

Um computador executa instruções numa CPU, mantém os dados de trabalho na memória, guarda arquivos em discos e fala com o mundo por dispositivos de entrada/saída. Cada componente pode ser observado: uso de CPU, regiões de memória, gravações de arquivos e pacotes de rede. Cada ponto de observação responde a uma pergunta diferente. A criação de processos mostra o que rodou; a inspeção da memória pode revelar código que nunca tocou o disco; as gravações de arquivos mostram o que foi alterado ou deixado; os pacotes de rede mostram para onde os dados foram. Nenhuma visão isolada vê tudo, e é por isso que os SOCs combinam dados de *endpoint*, de rede e de logs em vez de depender de uma única fonte.

### 8.2 Níveis de privilégio

Os processadores separam o código privilegiado do *kernel* dos programas de usuário. Agentes de detecção de *endpoint* muitas vezes rodam em parte no *kernel* para ver com confiabilidade a criação de processos e a atividade de arquivos, o que é poderoso, mas significa que defeitos no agente podem derrubar máquinas. O código no *kernel* consegue ver e interceptar atividades que os programas de usuário não conseguem, inclusive tentativas de adulterar o próprio agente. O mesmo poder significa que um componente de *kernel* defeituoso pode parar a máquina inteira, por isso as atualizações do agente são distribuídas em etapas, com grupos de teste primeiro. Os engenheiros pesam a visibilidade ganha contra o risco de estabilidade nos servidores críticos.

### 8.3 Processos e *threads*

Um processo é um programa em execução com memória própria; *threads* são caminhos de execução dentro dele. A telemetria de *endpoint* registra a criação de processos, o processo pai e a linha de comando, que as detecções usam intensamente. As relações pai–filho contam uma história: um processo de servidor web que inicia um *shell* de comandos é incomum e merece atenção, enquanto a área de trabalho de um usuário que inicia um navegador não é. Detecções que combinam pai, filho e argumentos da linha de comando são muito mais precisas do que as que olham apenas o nome de um processo.

### 8.4 *Caches* e desempenho

Os sensores consomem ciclos de CPU e memória. Um agente que inspeciona cada gravação de arquivo pode deixar lento um servidor ocupado. Os engenheiros equilibram visibilidade e desempenho, testando em máquinas representativas. Inspecionar cada gravação de arquivo significa interceptá-la, examiná-la e deixá-la seguir, o que acrescenta latência a discos ocupados. Os agentes muitas vezes excluem caminhos conhecidos de alto volume, como arquivos de banco de dados, para reduzir o custo, mas cada exclusão é um ponto cego que atacantes poderiam usar. Os engenheiros testam os agentes sob carga realista e documentam cada exclusão com seu motivo.

### 8.5 Caminhos de armazenamento

Os logs passam de *buffers* na memória para o disco e para a rede. Uma queda pode perder eventos em *buffer*. Conhecer o caminho explica lacunas depois de reinicializações. A maioria dos sistemas de log guarda os eventos em *buffer* na memória e os grava em lotes, por eficiência. Uma perda súbita de energia ou uma queda descarta o que estava no *buffer*. Os encaminhadores podem armazenar em *buffer* de novo antes de enviar pela rede. Saber onde ficam os *buffers* ajuda o analista a explicar por que os últimos segundos antes de uma queda estão faltando, em vez de suspeitar de apagamento. Encaminhadores com filas apoiadas em disco perdem menos.

### 8.6 *Firmware*

Abaixo do sistema operacional fica o *firmware*. Mudanças nele raramente são visíveis para a telemetria normal, por isso verificações de integridade e atualizações do fornecedor importam. O *firmware* roda antes de o sistema operacional iniciar e pode influenciar tudo o que vem depois, o que torna as mudanças nele especialmente graves. Os agentes de *endpoint* comuns começam tarde demais para observar boa parte dele. Os defensores contam com a inicialização medida, com a verificação de assinaturas do fornecedor nas atualizações e com a comparação das versões de *firmware* com valores esperados em toda a frota. Diferenças inesperadas de versão entre servidores idênticos são investigadas, não descartadas.

### 8.7 Caso

Os servidores do portal da Lindqvist rodam um agente de *endpoint*. Durante a rajada, a CPU de um servidor chega a 95%, principalmente por causa do serviço web, não do agente; Amara verifica antes de culpar o sensor. Culpar o agente teria sido um palpite fácil, já que os sensores costumam ser suspeitos quando os servidores ficam lentos. Amara confere os números de CPU por processo e vê o serviço web consumindo a maior parte enquanto responde à enxurrada de tentativas de login. A fatia do agente continua pequena. A constatação aponta para a limitação de taxa no portal, e não para o ajuste do sensor.

### Exemplo resolvido

Paolo pergunta por que o servidor do portal perdeu 30 segundos de eventos do agente às 10:06. Amara lê o log de saúde do agente: o *buffer* de eventos encheu enquanto o enlace de rede estava saturado pela rajada, e os eventos mais antigos foram descartados. Ela propõe um *buffer* maior e um alerta de saúde quando houver descartes.

> **Caso sintético.** Os servidores e os logs são inventados.

### Erros e limites

O conhecimento de arquitetura explica onde os dados podem se perder, mas cada produto se comporta de um jeito; leia a documentação do fornecedor.

### Exercícios

- **EX022 — Agentes no *kernel*.** Por que muitos agentes de *endpoint* rodam em parte no *kernel*, e qual é o risco? *Rubrica:* 3 = visibilidade confiável de eventos de processos/arquivos; defeitos podem derrubar sistemas; 2 = um lado; 1 = vago; 0 = nada.
- **EX023 — Eventos perdidos.** Explique a perda de 30 segundos de eventos às 10:06. *Rubrica:* 3 = o *buffer* encheu durante a saturação da rede; eventos mais antigos foram descartados; 2 = parcial; 1 = palpite de defeito no agente; 0 = nada.
- **EX024 — Troca de desempenho.** Como os engenheiros decidem quanto um sensor pode inspecionar? *Rubrica:* 3 = equilibrar visibilidade vs CPU/memória; testar em máquinas representativas; 2 = parcial; 1 = sempre o máximo; 0 = nada.

### Síntese

A arquitetura explica que telemetria existe, quanto ela custa e onde pode se perder.

### Continue estudando — capítulo 08 de 50

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar programas maiores em módulos; (2) usar estruturas de dados para buscas eficientes; (3) tratar erros e casos-limite de forma deliberada; (4) escrever testes unitários para a lógica de detecção.

### 9.1 De scripts a programas

À medida que as ferramentas de Amara crescem, ela separa a análise sintática, a lógica e a saída em módulos. Cada um pode ser testado e substituído sem mexer nos outros. Um único script longo mistura responsabilidades: mudar o formato de saída arrisca quebrar o analisador. Módulos com fronteiras claras permitem a Amara trocar o analisador por um novo formato de log enquanto a lógica de contagem permanece intocada e testada. A estrutura também permite a Paolo revisar um módulo de cada vez, o que mantém as revisões curtas e focadas. Cada módulo tem seus próprios testes, e um pequeno programa principal os une.

### 9.2 Estruturas de dados

Dicionários dão buscas rápidas — por exemplo, mapear um nome de usuário à sua contagem de falhas. Conjuntos respondem rapidamente a perguntas de pertinência. Escolher a estrutura certa transforma minutos em segundos em logs grandes. Procurar um nome de usuário numa lista significa percorrer cada entrada até aparecer uma correspondência; com um milhão de entradas, isso fica lento quando se repete para cada linha de log. Um dicionário salta para a entrada quase diretamente. Os conjuntos fazem o mesmo para perguntas do tipo "já vi isto antes?", que a lógica de detecção faz o tempo todo, como saber se um endereço já está numa lista de observação.

### 9.3 Erros

Os programas encontram campos ausentes, codificações estranhas e linhas enormes. O tratamento deliberado — capturar erros específicos, contá-los e continuar — mantém as análises completas e honestas. Capturar todos os erros com um único tratador amplo esconde defeitos reais, como um nome de variável digitado errado. Capturar erros específicos, como um valor que não pode ser lido como horário, trata os problemas esperados e deixa os inesperados aparecerem. A contagem de erros tratados vai para a saída, para que os leitores saibam quantos registros foram deixados de lado. O silêncio é pior.

### 9.4 Testes unitários

O módulo unittest do Python permite a Amara escrever testes como "cinco falhas para usuários distintos numa rede devem disparar; quatro não". Os testes rodam automaticamente antes de cada mudança ser incorporada. Um par de testes, um de cada lado do limiar, fixa exatamente onde o comportamento da regra muda. Rodar os testes automaticamente antes da incorporação faz com que uma mudança posterior que desloque o limiar por acidente falhe de imediato, em vez de ser descoberta quando um ataque real passar despercebido. Os testes também servem de documentação do que a regra deve fazer.

### 9.5 Casos-limite

Valores de fronteira (exatamente o limiar), entrada vazia e eventos duplicados são onde o código de detecção costuma quebrar. Os testes miram neles primeiro. Uma regra que dispara com "mais de cinco" e uma que dispara com "cinco ou mais" diferem apenas em exatamente cinco, e é aí que os defeitos se escondem. Testes com entrada vazia verificam se o código não relata nada em vez de travar. Eventos duplicados, comuns quando um encaminhador de logs tenta de novo, verificam se a mesma falha não é contada duas vezes. Amara lista esses casos antes de escrever a regra, e não depois que aparece um defeito.

### 9.6 Desempenho

Para um dia de logs do portal (2 milhões de linhas), ler linha a linha usa pouca memória; carregar tudo numa lista pode esgotá-la. Dois milhões de linhas de algumas centenas de bytes cada podem ocupar muito mais memória quando cada linha vira um objeto Python separado. Ler uma linha de cada vez e atualizar contadores mantém o uso de memória estável. Amara mede as duas abordagens num dia de amostra e registra o pico de memória de cada uma, o que justifica o desenho em fluxo na revisão.

### 9.7 Revisões

Paolo revisa o código quanto à correção e à clareza; um segundo par de olhos pega deslizes de lógica que os testes deixaram passar. Os testes verificam aquilo que o autor pensou em testar; um revisor pergunta pelo que não foi considerado. Paolo percebe que o código de Amara trata os nomes de usuário diferenciando maiúsculas de minúsculas, enquanto o portal não faz isso, de modo que "U5" e "u5" eram contados separadamente. Acrescenta-se um teste para esse caso, e as notas de revisão viram uma lista de verificação para futuros códigos de detecção. As revisões são registradas com o nome do revisor, para que leitores posteriores saibam que alguém conferiu o código antes de ele entrar em produção.

### Registro de log dentro das ferramentas

As ferramentas de Amara registram as próprias ações: arquivo de entrada, seu *hash*, registros lidos, registros pulados e saída gravada. Quando um resultado é questionado semanas depois, o log da ferramenta mostra exatamente o que ela processou. Esse autorregistro custa algumas linhas de código e poupa horas de dúvida.

### Exemplo resolvido

O teste de Amara para "exatamente 5 falhas" falha: o código dela usa "> 5", enquanto o documento de projeto diz "pelo menos 5". Ela pergunta a Paolo qual é a intenção; eles escolhem "≥ 5", atualizam juntos o documento de projeto e o código e mantêm o teste.

> **Caso sintético.** Os testes e os dados são sintéticos.

### Erros e limites

Os testes codificam o entendimento do momento em que foram escritos; se a ameaça mudar, eles podem impor uma lógica desatualizada.

### Exercícios

- **EX025 — Escolha da estrutura de dados.** Que estrutura serve para contar falhas por usuário, e por quê? *Rubrica:* 3 = dicionário: atualizações rápidas por chave; 2 = parcial; 1 = lista; 0 = nada.
- **EX026 — Defeito de fronteira.** O que o teste de "exatamente 5" revelou, e como foi corrigido? *Rubrica:* 3 = o código usava > 5 e o projeto, ≥ 5; projeto, código e teste foram alinhados; 2 = parcial; 1 = ignorado; 0 = nada.
- **EX027 — Leitura em fluxo.** Por que ler logs grandes linha a linha? *Rubrica:* 3 = baixo uso de memória; evita esgotá-la; 2 = parcial; 1 = sempre mais rápido; 0 = nada.

### Síntese

Código estruturado, estruturas de dados adequadas e testes de casos-limite tornam confiável a lógica de detecção.

### Continue estudando — capítulo 09 de 50

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética da engenharia às operações de segurança; (2) equilibrar monitoramento e privacidade; (3) lidar com conflitos entre rapidez e segurança; (4) relatar preocupações de forma responsável.

### 10.1 Deveres

Os engenheiros têm deveres para com o público, os empregadores e os colegas. Num SOC, o monitoramento protege as pessoas, mas também as observa. A prática ética significa coletar o que a finalidade exige, e nada mais. O dever para com o público inclui os clientes cujas contas são protegidas e cujos dados passam por sistemas monitorados. O dever para com o empregador significa fazer um trabalho competente e honesto. O dever para com os colegas significa não monitorá-los além do que a política permite. Coletar apenas o que a finalidade exige limita o dano caso os dados de monitoramento sejam algum dia mal usados ou vazados.

### 10.2 Privacidade e monitoramento

Funcionários e clientes têm interesses de privacidade. A política de monitoramento da Lindqvist informa aos funcionários o que é monitorado e por quê; o acesso do SOC ao conteúdo (como o corpo de e-mails) exige aprovação por caso. Informar aos funcionários o que é monitorado é ao mesmo tempo justo e prático: quem conhece as regras tem menos chance de se sentir traído quando o monitoramento revela um problema. Metadados, como quem mandou e-mail a quem e quando, são menos invasivos do que o conteúdo. Exigir aprovação por caso antes de ler o conteúdo mantém o passo mais invasivo ligado a uma necessidade específica e justificada.

### 10.3 Segurança das ações

As ações de resposta podem prejudicar as operações: bloquear uma rede poderia interromper as atualizações de rota dos caminhões de entrega. Os engenheiros consideram os efeitos colaterais e usam *playbooks* aprovados. Os caminhões da Lindqvist dependem de acesso à rede para atualizações de rota e de entrega, então cortar um segmento de rede durante uma resposta poderia deixar motoristas sem orientação ou atrasar remessas. Os *playbooks* listam as dependências conhecidas de cada ação e quem precisa ser avisado antes que ela seja tomada. Onde o risco é alto, tenta-se uma ação mais estreita, como bloquear um único endereço, antes de uma ampla.

### 10.4 Honestidade

Os relatórios não devem esconder falhas, como uma detecção perdida, mesmo quando constrangedoras. Escondê-las impede o aprendizado. Uma detecção perdida é informação: mostra uma lacuna nos dados, na lógica ou no processo. Relatá-la permite à equipe fechar a lacuna e aos gestores julgar o risco com precisão. Ocultá-la deixa a lacuna aberta e corrói a confiança quando ela vem à tona mais tarde, o que costuma acontecer durante a revisão do incidente seguinte. Na Lindqvist, as detecções perdidas aparecem no relatório mensal com o que foi mudado depois, para que a mesma lacuna seja fechada de forma visível, e não esquecida em silêncio.

### 10.5 Conflitos

Quando um gestor pede o monitoramento de um funcionário sem um pedido de investigação, Amara recusa e remete à política e ao processo de RH. Monitorar um único funcionário sem um pedido formal poderia servir a uma disputa pessoal em vez de a uma necessidade de segurança e pode violar a legislação trabalhista ou a política de monitoramento. Amara não julga os motivos do gestor; ela explica o processo e indica o RH, que pode abrir uma investigação se houver motivo. Ela registra o pedido e sua resposta.

### 10.6 Levantando preocupações

Se uma prática parece insegura ou ilegal, os engenheiros a levantam pelos canais definidos, documentando os fatos. Os canais definidos incluem o gestor direto, o líder de segurança, a equipe de conformidade e, quando estes falham, qualquer canal de denúncia que a organização ofereça. Documentar fatos em vez de opiniões mantém a preocupação específica e verificável. Levantá-la cedo, antes que ocorra dano, dá à organização a chance de corrigir a prática discretamente. Amara descobre onde está publicada a política de denúncias da Lindqvist já na primeira semana. A retaliação contra alguém que levanta uma preocupação de boa-fé é, ela própria, uma violação da maioria dos códigos e de muitas leis.

### 10.7 Códigos profissionais

Entidades de engenharia e de computação publicam códigos que enfatizam o bem público, a competência e a honestidade; Amara lê o código de sua universidade durante a integração. Os códigos são curtos e gerais, então orientam o julgamento em vez de substituí-lo. Amara anota três pontos relevantes para seu estágio: agir dentro de sua competência, ser honesta quanto a resultados e limites e pôr a segurança pública à frente da conveniência. Ela volta a eles quando o pedido de monitoramento em seu estágio põe esses princípios à prova. As entidades de classe podem punir membros que os violam, o que dá peso aos códigos.

### Consentimento e transparência

O aviso de privacidade do portal informa aos clientes que a atividade de login é registrada por segurança. A transparência não substitui a minimização, mas permite que as pessoas entendam o monitoramento e reclamem se ele for mal usado. O SOC revisa o aviso com a equipe jurídica todo ano, para que ele corresponda à prática real.

### Exemplo resolvido

Durante o incidente do portal, um colega sugere bloquear permanentemente toda a faixa 203.0.113.0/24. Amara observa que a faixa pertence a um provedor de nuvem também usado por um parceiro logístico. Paolo concorda com um bloqueio temporário, com monitoramento e uma revisão após 24 horas, documentado no chamado.

> **Caso sintético.** A situação e as pessoas são inventadas.

### Erros e limites

A ética orienta o julgamento, mas não dá respostas automáticas; discuta os casos difíceis com os supervisores.

### Exercícios

- **EX028 — Coleta mínima.** O que significa "coletar o que a finalidade exige" num SOC? *Rubrica:* 3 = monitorar para uma finalidade definida, sem conteúdo extra sem aprovação; 2 = parcial; 1 = coletar tudo; 0 = nada.
- **EX029 — Recusando um pedido.** Por que Amara recusou monitorar um funcionário? *Rubrica:* 3 = não havia pedido de investigação; remeteu à política e ao RH; 2 = parcial; 1 = atendeu; 0 = nada.
- **EX030 — Bloqueio da faixa.** Por que o bloqueio permanente foi rejeitado? *Rubrica:* 3 = faixa compartilhada com um parceiro; em vez disso, bloqueio temporário com revisão; 2 = parcial; 1 = bloqueou; 0 = nada.

### Síntese

A engenharia ética de SOC limita o monitoramento à sua finalidade, pesa os efeitos colaterais das ações e relata com honestidade.

### Continue estudando — capítulo 10 de 50

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar endereçamento, portas e protocolos comuns; (2) ler telemetria de rede, como fluxos e logs web; (3) agregar a atividade por rede; (4) reconhecer os limites da atribuição baseada em IP.

### 11.1 Camadas

As redes movem dados em camadas: enlaces físicos, endereçamento e roteamento IP, transporte TCP ou UDP e aplicações como o HTTPS. Existe telemetria em cada camada: estatísticas de enlace, registros de fluxo e logs de aplicação. Cada camada responde a perguntas diferentes. As estatísticas de enlace mostram se um cabo ou porta está saturado; os registros de fluxo mostram quem falou com quem, por quanto tempo e quantos bytes trafegaram; os logs de aplicação mostram o que foi pedido e o que voltou. Durante a rajada no portal, os fluxos revelam o volume vindo de uma rede, mas só os logs do servidor web mostram quais nomes de usuário foram tentados.

### 11.2 Endereços e redes

Os endereços IPv4 são agrupados em redes por prefixo. Uma rede /24 compartilha os três primeiros octetos. O tráfego de ataque vindo de um provedor de hospedagem muitas vezes se espalha por muitos endereços em poucas redes, então agregar por rede revela rajadas que as contagens por endereço escondem. Contar por endereço pode fazer um ataque distribuído parecer inofensivo: cinquenta endereços com duas tentativas cada nunca acionam um limiar de cinco por endereço. Agrupar por /24 os reúne numa única rede com cem tentativas. A escolha do comprimento do prefixo é uma troca, já que um prefixo mais largo pega atividades mais espalhadas, mas também junta clientes sem relação entre si atrás do mesmo provedor.

### Laboratório — falhas por rede

```python
"""Count failed portal logins by source /24 network and by distinct usernames (synthetic)."""
from collections import defaultdict
log = [("203.0.113.10","u1","fail"),("203.0.113.11","u2","fail"),("203.0.113.12","u3","fail"),
       ("203.0.113.13","u4","fail"),("203.0.113.14","u5","ok"),("198.51.100.20","u6","fail"),
       ("198.51.100.20","u6","fail"),("198.51.100.20","u6","ok"),("203.0.113.15","u7","fail"),
       ("203.0.113.16","u8","fail")]
fails = defaultdict(int); users = defaultdict(set)
for ip, user, res in log:
    net = ".".join(ip.split(".")[:3]) + ".0/24"
    users[net].add(user)
    if res == "fail": fails[net] += 1
for net in sorted(fails):
    print(f"{net:17} failures={fails[net]} distinct_users={len(users[net])}")
```

Execute com `python3 lab_failed.py`. Saída verificada:

```text
198.51.100.0/24   failures=2 distinct_users=1
203.0.113.0/24    failures=6 distinct_users=7
```

### 11.3 Lendo o resultado

A rede 203.0.113.0/24 produziu 6 falhas, uma contra cada um de seis nomes de usuário, e tocou 7 nomes de usuário distintos ao todo quando se conta o sucesso de u5 — muitas contas, poucas tentativas cada, o padrão do *credential stuffing*. A 198.51.100.0/24 mostra 2 falhas e um sucesso para um único usuário: um cliente digitando a senha errada. O padrão importa mais do que os totais. Muitos nomes de usuário com uma tentativa cada sugerem alguém percorrendo uma lista de credenciais vazadas, na esperança de que alguns clientes tenham reutilizado senhas. Um único nome de usuário com algumas falhas e depois um sucesso parece uma pessoa comum que esqueceu qual senha usou. Uma regra que só contasse falhas trataria as duas redes da mesma forma e perderia essa distinção.

### 11.4 Visibilidade do HTTPS

O tráfego web cifrado esconde o conteúdo dos sensores de rede; os próprios logs do servidor web mostram caminhos, códigos de status e nomes de usuário. Escolher onde observar é uma decisão de engenharia. Quebrar a cifragem na rede para inspecionar o conteúdo é possível com *proxies* de interceptação, mas acrescenta risco, custo e preocupações de privacidade. No portal, o servidor já vê as requisições decifradas, então seus logs são o lugar natural para observar os logins. Os sensores de rede ainda ajudam com volume e tempo, enquanto os logs do servidor fornecem o significado de cada requisição.

### 11.5 Limites da atribuição

Um endereço identifica um ponto de conexão, não uma pessoa. *Proxies* compartilhados, faixas de nuvem e reutilização de endereços tornam imprecisos o bloqueio e a atribuição. Muitos clientes podem compartilhar um endereço atrás do *gateway* de uma operadora de telefonia móvel, então bloqueá-lo pode impedir o acesso de usuários inocentes. Os atacantes alugam servidores na nuvem e os abandonam em poucas horas, de modo que um endereço hostil ontem pode pertencer a outra pessoa amanhã. Por isso, os relatórios do SOC descrevem os endereços como fontes de atividade, em vez de nomear quem estava por trás deles. Os bloqueios de endereços recebem datas de expiração.

### 11.6 Conhecimento de protocolo

Saber que o login usa POST para /login e devolve 401 em caso de falha permite a Amara escrever uma análise sintática precisa. Sem esse conhecimento, um analisador poderia contar como tentativa toda requisição à página de login, inclusive de pessoas que apenas carregam o formulário. Conhecer o método, o caminho e os códigos de status permite a Amara contar apenas as credenciais enviadas e separar falhas de sucessos. Ela confirma os detalhes com os desenvolvedores do portal em vez de adivinhá-los a partir de uma amostra, já que um redirecionamento depois do login poderia esconder o resultado real.

### DNS e tempo

Os logs de DNS mostram quais nomes os hosts consultam, muitas vezes revelando contatos antes que as conexões aconteçam. Os dispositivos de rede precisam compartilhar um horário sincronizado para que fluxos, DNS e logs web se alinhem; sem isso, a correlação entre camadas vira adivinhação.

### Exemplo resolvido

Amara nota que um endereço, 203.0.113.14, produziu o sucesso de u5. Ela confere o log web: a mesma sessão depois requisitou /account/address, com uma alteração às 10:07. Ela acrescenta isso ao chamado como uma possível ação de tomada de conta.

> **Caso sintético.** Os endereços usam faixas de documentação; os eventos são sintéticos.

### Erros e limites

Agregar por /24 pode juntar usuários sem relação entre si de grandes provedores; confirme com outros sinais.

### Exercícios

- **EX031 — Agregação por rede.** Por que agregar falhas por rede /24? *Rubrica:* 3 = rajadas espalhadas por muitos endereços aparecem juntas; 2 = parcial; 1 = nenhum motivo; 0 = nada.
- **EX032 — Padrão de *stuffing*.** Que rede mostra *credential stuffing*, e por quê? *Rubrica:* 3 = 203.0.113.0/24: muitos usuários, poucas tentativas cada; 2 = só a rede; 1 = errado; 0 = nada.
- **EX033 — Ação seguinte.** O que a sessão bem-sucedida fez em seguida? *Rubrica:* 3 = requisitou alteração de endereço às 10:07; possível tomada de conta; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

A telemetria de rede ganha significado com a agregação e o conhecimento de protocolo, dentro dos limites da atribuição por IP.

### Continue estudando — capítulo 11 de 50

[← Capítulo 10 (rascunho)](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 (rascunho) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) explicar como os sistemas operacionais gerenciam processos, arquivos, usuários e logs; (2) localizar os principais eventos de segurança no Windows e no Linux; (3) relacionar as configurações de auditoria do SO à cobertura de detecção; (4) reconhecer como a configuração muda a telemetria.

### 12.1 O que um SO faz

O sistema operacional escalona processos, gerencia a memória, controla o acesso a arquivos e dispositivos e autentica usuários. Cada uma dessas funções pode produzir eventos de segurança se a auditoria estiver ativada. A auditoria transforma essas funções de bastidor em registros: um processo iniciando, um arquivo aberto, um usuário entrando. A maioria dos sistemas vem com apenas parte disso ativada, porque a auditoria completa produz grandes volumes e algum custo de desempenho. Escolher quais funções auditar é, portanto, uma decisão de projeto ligada às detecções que o SOC pretende executar.

### 12.2 Eventos do Windows

O Windows registra logons, criação de processos, instalação de serviços e mudanças de política em seus logs de eventos quando a política de auditoria os ativa. A criação de processos com linha de comando, por exemplo, precisa ser ligada de forma deliberada; sem ela, muitas detecções de *endpoint* não têm com o que casar. Uma instalação padrão pode registrar que um processo iniciou, mas não a linha de comando que recebeu, que é onde fica boa parte do detalhe útil. A Política de Grupo permite aos administradores ativar a auditoria de forma consistente em muitas máquinas. Amara verifica uma amostra de servidores do portal e descobre que a configuração de linha de comando não está aplicada de maneira uniforme, uma lacuna que sua tabela de cobertura depois atribui a um modelo de *build* mais antigo.

### 12.3 Logs do Linux

Os sistemas Linux registram a autenticação nos logs do sistema, e o subsistema de auditoria pode registrar acesso a arquivos e execução de programas conforme regras. Como no Windows, a cobertura depende da configuração. As mensagens de autenticação vão para arquivos como o log de autenticação do sistema ou para o *journal* do systemd, conforme a distribuição. O subsistema de auditoria usa regras que nomeiam o que observar, por exemplo a execução de qualquer programa por uma conta de serviço web. Cada regra acrescenta volume, então as regras são escritas para riscos específicos, em vez de registrar tudo o que o sistema faz.

### 12.4 Usuários e privilégio

Os sistemas operacionais separam usuários comuns de administradores. Eventos que mudam privilégio — acrescentar um usuário a um grupo de administradores, por exemplo — são sinais de alto valor para a detecção. Atacantes que conseguem um ponto de apoio geralmente querem mais direitos, então mudanças de pertencimento a grupos costumam aparecer cedo numa intrusão. Essas mudanças também são raras na operação normal, o que as torna boas candidatas à detecção, com poucos falsos positivos. Mudanças legítimas ainda acontecem, por isso os alertas são conferidos contra o registro da gestão de mudanças em busca de um pedido aprovado. As remoções de grupos privilegiados também são registradas.

### 12.5 Serviços e tarefas agendadas

Programas podem ser configurados para iniciar automaticamente. Novos serviços e tarefas agendadas são mecanismos comuns de persistência descritos no MITRE ATT&CK, por isso vale a pena registrar sua criação. A persistência permite que o programa de um atacante sobreviva a uma reinicialização ou ao *logout* de um usuário. Softwares legítimos também instalam serviços, sobretudo durante atualizações, então um alerta bruto a cada novo serviço seria ruidoso. As detecções estreitam o foco, por exemplo a serviços que rodam a partir de pastas graváveis pelo usuário ou a tarefas criadas por processos pais incomuns, e os analistas comparam com as implantações de software conhecidas.

### 12.6 Configuração como cobertura

A cobertura de detecção só é tão boa quanto a configuração de auditoria. Amara monta uma tabela que lista cada regra de detecção e a configuração do SO de que ela depende, e depois verifica se as configurações estão implantadas por política em todas as classes de servidor. A tabela revela lacunas que só os testes das regras não pegariam: uma regra pode passar nos testes em laboratório e mesmo assim nunca disparar em produção, porque o evento de que precisa não é gerado ali. A verificação de Amara descobre que uma classe de servidor registra a criação de processos sem a linha de comando. Corrigir a política restaura de uma vez a cobertura de várias regras, e a tabela é conferida de novo após cada mudança de *build*.

### 12.7 Tamanho e rotação dos logs

Os logs de eventos têm tamanho máximo; quando cheios, os eventos antigos são sobrescritos. Encaminhar os logs ao SIEM sem demora evita a perda. Num servidor ocupado, um log de eventos pequeno pode dar a volta em horas, de modo que a evidência de um ataque pela manhã pode ter sumido à tarde. Os atacantes às vezes geram ruído de propósito para empurrar as entradas mais antigas para fora. Encaminhar os eventos ao SIEM em segundos mantém uma cópia fora do host, e alertas sobre lacunas no encaminhamento mostram quando um servidor para de enviar. As configurações de tamanho dos logs fazem parte do padrão de *build*.

### Exemplo resolvido

A tabela de Amara revela que os servidores web do portal não têm registro da linha de comando na criação de processos porque foram construídos a partir de um modelo mais antigo. Três regras de detecção, portanto, nunca poderiam disparar nesses servidores. Paolo abre uma mudança para atualizar o modelo e verifica depois com um processo de teste inofensivo.

> **Caso sintético.** Os servidores, os modelos e as regras são inventados.

### Erros e limites

Ativar mais auditoria aumenta o volume e o custo; ative o que as detecções e as investigações precisam.

### Exercícios

- **EX034 — Dependência da cobertura.** Por que uma regra de detecção pode nunca disparar em alguns servidores? *Rubrica:* 3 = a configuração de auditoria exigida (por exemplo, registro da linha de comando) não está ativada; 2 = parcial; 1 = defeito na regra; 0 = nada.
- **EX035 — Eventos de privilégio.** Por que as mudanças de pertencimento a grupos são sinais de alto valor? *Rubrica:* 3 = mudam o privilégio; atacantes buscam direitos de administrador; 2 = parcial; 1 = ruído; 0 = nada.
- **EX036 — Correção do modelo.** Como a lacuna dos servidores web foi corrigida e verificada? *Rubrica:* 3 = modelo de *build* atualizado; um processo de teste inofensivo confirmou o registro; 2 = parcial; 1 = ignorada; 0 = nada.

### Síntese

Os sistemas operacionais só produzem eventos de segurança ricos quando configurados para isso; mapear as regras às configurações revela pontos cegos.

### Continue estudando — capítulo 12 de 50

[← Capítulo 11 (rascunho)](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 (rascunho) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) modelar dados de segurança em tabelas e documentos; (2) escrever consultas que juntam e agregam eventos; (3) projetar esquemas com campos consistentes; (4) raciocinar sobre indexação e custo de consultas.

### 13.1 Dados de segurança como dados

Um SIEM é um sistema de dados: ingere registros, armazena-os, indexa campos e responde a consultas. Um bom projeto de dados torna as detecções mais rápidas e mais precisas. Tratar o SIEM como sistema de dados traz ideias de bancos de dados: esquemas, índices, planos de consulta e capacidade. Uma tabela mal projetada pode fazer uma pergunta simples levar minutos, o que importa quando um analista está no meio de um incidente. Amara aprende a ler as estatísticas das consultas, como quantos registros foram varridos para responder a cada busca. As buscas lentas são então reescritas ou indexadas.

### 13.2 Esquemas

Se uma fonte chama o campo de usuário de "user", outra de "username" e uma terceira de "acct", toda consulta precisa lembrar os três. Normalizar os campos num esquema comum na ingestão — um único nome para usuário, endereço de origem, host, ação e resultado — simplifica as regras e reduz erros. Normalizar na ingestão significa converter os campos de cada fonte uma única vez, quando os dados chegam, em vez de em cada consulta que os lê. Os valores pedem o mesmo cuidado: uma fonte pode escrever "FAIL", outra "failure", outra um código numérico. O mapeamento de cada fonte é documentado e testado, porque um erro ali quebra em silêncio todas as regras que dependem do campo.

### 13.3 Junções

Muitas perguntas juntam dados: "em que hosts a conta que fez login a partir de 203.0.113.14 tocou em seguida?" junta logs web com logs internos de autenticação por nome de usuário e horário. Juntar apenas pelo nome de usuário pode enganar se dois sistemas grafarem os nomes de forma diferente ou se o mesmo nome pertencer a um cliente e a um funcionário. O horário acrescenta uma segunda chave, limitando as correspondências a eventos próximos no tempo. As junções costumam ser custosas, por isso os engenheiros filtram cada lado primeiro, por exemplo para o único endereço suspeito, antes de combiná-los.

### 13.4 Agregação

Contar, agrupar e janelar (por exemplo, a cada 10 minutos) são o núcleo das detecções por limiar. Uma detecção por limiar pega eventos brutos, agrupa-os por uma chave, como a rede de origem, conta-os dentro de uma janela de tempo e compara a contagem com um limite. Janelas fixas podem dividir uma rajada numa fronteira, de modo que nenhuma das metades ultrapasse o limiar. Janelas deslizantes evitam isso a um custo computacional maior, uma troca que Amara testa com os dados do portal. Ela registra quantas rajadas cada tipo de janela encontra no mesmo dia de dados.

### 13.5 Índices e custo

Campos indexados são rápidos de pesquisar; buscas de texto completo sem índice são lentas e caras. Os engenheiros indexam os campos que as detecções e os analistas mais usam, como usuário, host e endereço de origem. Um índice funciona como o índice de um livro: aponta direto para os registros que contêm um dado valor, em vez de ler todas as páginas. Cada índice ocupa armazenamento e deixa a ingestão um pouco mais lenta. Escolher os campos indexados a partir das consultas que os analistas de fato executam, em vez de indexar tudo, mantém sob controle tanto a velocidade de busca quanto o custo de armazenamento.

### 13.6 Qualidade dos dados

Valores ausentes, tipos errados e duplicatas distorcem os resultados. Verificações de qualidade na ingestão os pegam cedo. Um campo de horário lido no fuso errado pode deslocar eventos em horas e quebrar correlações; eventos duplicados podem dobrar contagens e acionar limiares falsamente. As verificações de ingestão contam, por fonte, os registros que falham na validação e alertam quando a taxa salta, o que muitas vezes sinaliza uma mudança de formato depois de uma atualização de software no sistema emissor. Cada fonte tem um responsável, que é avisado quando sua taxa de rejeição sobe, para que a correção aconteça no emissor, e não por meio de contornos em cada consulta.

### 13.7 Retenção por tabela

Tabelas diferentes podem precisar de retenções diferentes: logs de autenticação guardados por mais tempo que logs verbosos de depuração. Os registros de autenticação ajudam a reconstruir o mau uso de contas meses depois, por isso merecem retenção longa. A saída verbosa de depuração raramente é útil além de alguns dias e custa muito para guardar. Definir a retenção por tabela, com os motivos registrados, permite ao SOC gastar armazenamento onde as investigações realmente precisam, cumprindo os mínimos legais. A tabela de retenção é revisada todo ano com a equipe jurídica, e qualquer mudança é registrada com o motivo e quem a aprovou.

### Janelas de tempo

A agregação em janelas exige cuidado nas fronteiras: uma rajada que vai das 10:09 às 10:11 pode se dividir entre duas janelas de 10 minutos e não atingir o limiar em nenhuma delas.

### Exemplo resolvido

Amara descobre que os logs do portal guardam o carimbo de tempo como texto em hora local, enquanto os logs internos usam UTC. Sua junção não devolve nada porque os horários nunca coincidem. Ela acrescenta uma etapa de análise que converte os horários do portal para UTC na ingestão, roda a junção de novo e descobre que a sessão de u5 não tocou nenhum sistema interno.

> **Caso sintético.** As tabelas e os campos são inventados.

### Erros e limites

A normalização pode perder detalhes da fonte; guarde o registro bruto original ao lado dos campos normalizados.

### Exercícios

- **EX037 — Normalização de campos.** Por que normalizar os nomes de campo na ingestão? *Rubrica:* 3 = um nome por conceito simplifica as consultas e reduz erros; 2 = parcial; 1 = estilo; 0 = nada.
- **EX038 — Junção que falhou.** Por que a junção de Amara não devolveu nada, e como foi corrigida? *Rubrica:* 3 = texto em hora local vs UTC; converter na ingestão; 2 = parcial; 1 = palpite de consulta errada; 0 = nada.
- **EX039 — Escolha da indexação.** Que campos devem ser indexados primeiro? *Rubrica:* 3 = os mais usados por detecções e analistas: usuário, host, endereço de origem; 2 = parcial; 1 = todos; 0 = nada.

### Síntese

Trate os dados de segurança como um sistema de dados projetado: esquemas consistentes, junções cuidadosas, índices sensatos e verificações de qualidade.

### Continue estudando — capítulo 13 de 50

[← Capítulo 12 (rascunho)](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 (rascunho) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) aplicar práticas de requisitos, projeto, testes e liberação ao conteúdo de detecção; (2) usar controle de versão e revisão de código para regras; (3) planejar implantação e reversão; (4) gerenciar a dívida técnica num SOC.

### 14.1 Detecção como código

Regras de detecção são software. Escrevê-las como arquivos de texto num formato padrão, como o Sigma, guardá-las em controle de versão e revisar as mudanças traz a disciplina da engenharia de software para o SOC. O controle de versão registra quem mudou uma regra, quando e por quê, o que responde a perguntas depois de um incidente, como se uma detecção estava ativa naquele momento. Um formato padrão como o Sigma também torna as regras portáveis entre produtos de SIEM e permite às equipes compartilhar e revisar regras com ferramentas comuns de software, em vez de um console de fornecedor.

### 14.2 Requisitos

Cada regra começa com um requisito: que comportamento, em quais ativos, com que taxa aceitável de falsos positivos e com que resposta. Os requisitos remetem a ameaças, muitas vezes expressas como técnicas do ATT&CK. Escrever o requisito antes da regra mantém o trabalho apontado para um risco real. Declarar de antemão uma taxa aceitável de falsos positivos dá ao teste uma nota de aprovação. Nomear a resposta diz ao autor da regra quanto detalhe um alerta precisa carregar: um alerta que aciona o bloqueio de uma conta precisa de evidência mais forte do que um que só alimenta uma revisão diária.

### 14.3 Testes

As regras são testadas contra dados benignos gravados (para medir falsos positivos) e contra eventos de teste seguros (para confirmar que disparam). Os testes rodam automaticamente quando uma mudança é proposta. Os dados benignos gravados podem ser uma semana de logs normais do portal; os eventos de teste seguros são registros sintéticos feitos para parecer o comportamento-alvo, sem nenhum ataque real. Uma regra que dispara na rajada sintética e fica em silêncio na semana normal é aprovada. Rodar os dois automaticamente a cada mudança pega regressões antes da implantação.

### 14.4 Revisão

Um segundo engenheiro revisa a lógica, o desempenho e a documentação. A revisão pega condições amplas demais antes que inundem os analistas. O desempenho é fácil de esquecer: uma regra que procura uma *substring* em todos os registros pode funcionar com dados de teste, mas sobrecarregar o SIEM em produção. O revisor também verifica se a documentação diz a um analista o que fazer quando a regra dispara. Paolo usa uma lista de verificação curta, para que as revisões sejam consistentes entre revisores e regras. Os comentários da revisão e as respostas do autor ficam anexados à mudança no controle de versão.

### 14.5 Liberação e reversão

Novas regras são implantadas primeiro em modo "só monitoramento", que registra as correspondências sem alertar. Depois de uma semana de resultados aceitáveis, passam a alertar. Se surgirem problemas, a versão anterior é restaurada a partir do controle de versão. O modo de monitoramento mostra com que frequência uma regra dispararia em dados reais sem aumentar a fila dos analistas. Resultados aceitáveis significam que a taxa de correspondência e a precisão atendem ao requisito. Como todas as versões ficam no controle de versão, a reversão é rápida e deixa registro, ao contrário de editar uma regra no próprio console, sem histórico.

### 14.6 Dívida técnica

Regras antigas e não testadas se acumulam. Paolo agenda uma revisão trimestral para aposentar regras que já não correspondem a nenhum ativo ou ameaça. Uma regra escrita para um servidor desativado há dois anos ainda consome processamento e pode confundir analistas novos. Regras cujos testes já não passam, ou que nem têm testes, carregam um risco oculto. A revisão trimestral lista cada regra com sua última correspondência, o estado dos testes e o responsável, e as regras aposentadas são mantidas no histórico de versões, em vez de simplesmente apagadas.

### 14.7 Documentação

Cada regra traz descrição, autor, referências, gatilhos benignos conhecidos e orientação de resposta. Os gatilhos benignos conhecidos poupam tempo aos analistas: se uma tarefa de *backup* aciona uma regra com regularidade, a documentação diz isso e como reconhecê-la. As referências ligam a regra à ameaça que ela trata. A orientação de resposta dá os primeiros passos, para que um analista mais novo aja corretamente à noite sem esperar o autor da regra. Uma regra sem algum desses campos falha nas verificações automáticas e não pode ser incorporada, de modo que a documentação nunca fica para depois e cai no esquecimento.

### Responsabilidade

Toda regra tem um responsável nomeado que responde a perguntas e revisa seu desempenho.

### Exemplo resolvido

Amara escreve sua regra de *stuffing* no portal como um arquivo no estilo Sigma, com um vínculo ao requisito, dois casos de teste e orientação de resposta. No modo só monitoramento, ela corresponde quatro vezes numa semana: duas rajadas reais e dois testes de carga da equipe web. Ela acrescenta uma exceção ligada ao *user agent* assinado da ferramenta de teste de carga e a uma verificação de calendário e então promove a regra.

> **Caso sintético.** A regra e a semana são inventadas.

### Erros e limites

A sobrecarga de processo pode atrasar detecções urgentes; mantenha um caminho de emergência com revisão posterior.

### Exercícios

- **EX040 — Modo só monitoramento.** O que é a implantação em só monitoramento, e por que usá-la? *Rubrica:* 3 = registra correspondências sem alertar para medir o ruído primeiro; 2 = parcial; 1 = nunca alertar; 0 = nada.
- **EX041 — Exceção para teste de carga.** Como foram tratadas as correspondências dos testes de carga? *Rubrica:* 3 = exceção ligada ao *user agent* assinado e a uma verificação de calendário; 2 = parcial; 1 = regra apagada; 0 = nada.
- **EX042 — Documentação da regra.** Liste quatro coisas que o documento de cada regra contém. *Rubrica:* 3 = descrição, autor, referências, gatilhos benignos, orientação de resposta (quatro); 2 = três; 1 = uma; 0 = nada.

### Síntese

A detecção como código aplica requisitos, testes, revisão e liberação em etapas para manter as regras confiáveis.

### Continue estudando — capítulo 14 de 50

[← Capítulo 13 (rascunho)](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 (rascunho) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) explicar confidencialidade, integridade e disponibilidade; (2) relacionar ameaças, vulnerabilidades e controles; (3) situar as operações de segurança nas funções do NIST CSF 2.0; (4) distinguir prevenção de detecção e resposta.

### 15.1 As três propriedades

A confidencialidade mantém a informação longe de pessoas não autorizadas; a integridade a mantém exata e inalterada; a disponibilidade mantém os sistemas utilizáveis. O incidente do portal tocou as três: dados de clientes podiam ser vistos, endereços foram alterados e o serviço de login ficou lento. Pensar nas três mantém a resposta equilibrada. Uma equipe focada apenas na confidencialidade poderia não perceber que os endereços de entrega dos clientes podiam ter sido alterados, um problema de integridade capaz de desviar encomendas. A disponibilidade também sofreu, já que clientes legítimos enfrentaram logins lentos durante a rajada. As notas de incidente de Amara registram o efeito sobre cada propriedade separadamente.

### 15.2 Ameaças, vulnerabilidades, controles

Uma ameaça é uma possível causa de dano; uma vulnerabilidade é uma fraqueza que ela pode explorar; um controle reduz o risco. Senhas de clientes reutilizadas são a vulnerabilidade que o *credential stuffing* explora; limitação de taxa e autenticação multifator são controles. Separar os três esclarece o que cada correção faz. A Lindqvist não consegue impedir criminosos de comprar listas de senhas vazadas, a ameaça, nem consegue obrigar os clientes a parar de reutilizar senhas, a vulnerabilidade. Ela pode acrescentar controles que tornem as senhas reutilizadas menos úteis, como desacelerar tentativas repetidas e pedir um segundo fator.

### 15.3 Funções do CSF 2.0

O NIST Cybersecurity Framework 2.0 organiza os resultados em Govern, Identify, Protect, Detect, Respond e Recover. Um SOC entrega principalmente Detect e Respond, mas depende de Identify (conhecimento dos ativos) e alimenta Govern com informação de risco. Sem Identify, o SOC não saberia de quais sistemas o portal depende nem quem é responsável por eles. Alimentar Govern significa transformar as lições dos incidentes em informação de risco que os líderes usam para decidir, como financiar MFA para os clientes. Mapear o trabalho do SOC às funções também mostra onde a equipe depende de outros para entregar os próprios resultados.

### 15.4 Prevenção e detecção

Nenhuma prevenção é perfeita. A detecção encontra o que a prevenção deixou passar, e a resposta limita o dano. Um programa equilibrado investe nas três. Gastar tudo em prevenção deixa a organização às cegas quando um controle falha; gastar tudo em detecção deixa passar ataques evitáveis e inunda os analistas. A resposta transforma detecção em dano reduzido, então uma detecção sem ninguém capaz de agir sobre ela acrescenta pouco. Os orçamentos são defendidos com incidentes como a rajada no portal, que precisou das três. Cada função tem suas próprias medidas.

### 15.5 Defesa em profundidade

Várias camadas — limites de taxa, detecção de *bots*, MFA, monitoramento de alterações de conta — fazem com que uma única falha não leve ao comprometimento completo. Cada camada pega uma parte do que escapa da anterior. Os limites de taxa desaceleram as tentativas, a detecção de *bots* bloqueia clientes automatizados, o MFA impede que uma senha correta baste, e o monitoramento de alterações de conta identifica mau uso depois do login. As camadas devem falhar de forma independente, para que uma única configuração errada não possa desativar várias de uma vez. Amara lista quais camadas do portal existiam durante a rajada e quais faltavam.

### 15.6 Menor privilégio

As contas recebem apenas os direitos de que precisam, limitando o dano quando uma delas é mal usada. Na Lindqvist, a conta de banco de dados do portal pode ler e atualizar registros de clientes, mas não pode apagar tabelas nem ler dados de funcionários. Se um atacante controlasse o portal, o dano ficaria limitado ao que essa conta permite. Os analistas do SOC seguem a mesma regra: recebem acesso de leitura aos logs, enquanto ações de resposta, como bloqueios de conta, exigem permissões separadas. Os direitos são revisados a cada trimestre e removidos quando os papéis mudam.

### 15.7 Mapeamento do caso

Amara mapeia o incidente do portal: a vulnerabilidade (reutilização de senhas pelos clientes), o controle ausente (nenhuma opção de MFA para clientes), a detecção (sua regra de rajada) e a resposta (bloqueio da conta, aviso). O mapeamento mostra onde o esforço teria mais efeito. A detecção e a resposta funcionaram, mas ambas agiram depois que uma conta de cliente já havia sido acessada. Acrescentar uma opção de MFA trataria a lacuna antes que o login tenha sucesso. Amara apresenta o mapa a Paolo como uma tabela de uma página, que depois vira insumo para a discussão de risco da equipe de segurança com a direção.

### O risco como organizador

O risco combina quão provável é o dano e quão grave ele seria. A Lindqvist classifica o portal do cliente como alto porque ele guarda endereços e cronogramas de entrega, então seu monitoramento tem prioridade sobre sistemas internos de teste.

### Exemplo resolvido

Paolo pergunta a Amara em que função do CSF se enquadra uma nova opção de MFA para clientes. Ela responde Protect e observa que monitorar as taxas de adesão ao MFA e as falhas de segundo fator acrescentaria um resultado de Detect.

> **Caso sintético.** O mapeamento e os controles são inventados.

### Erros e limites

Os *frameworks* organizam o raciocínio, mas não definem prioridades; a avaliação de risco define.

### Exercícios

- **EX043 — CID no caso.** Mostre como o incidente tocou a confidencialidade, a integridade e a disponibilidade. *Rubrica:* 3 = dados visíveis, endereço alterado, serviço lento; 2 = duas; 1 = uma; 0 = nada.
- **EX044 — Vulnerabilidade e controle.** Nomeie a vulnerabilidade e dois controles contra *credential stuffing*. *Rubrica:* 3 = reutilização de senhas; limitação de taxa e MFA; 2 = um controle; 1 = vago; 0 = nada.
- **EX045 — Posição no CSF.** Que funções do CSF um SOC entrega principalmente, e de quais depende? *Rubrica:* 3 = Detect e Respond; depende de Identify, informa Govern; 2 = parcial; 1 = uma; 0 = nada.

### Síntese

Os fundamentos de segurança enquadram o trabalho do SOC: propriedades a proteger, riscos a reduzir e funções a entregar.

### Continue estudando — capítulo 15 de 50

[← Capítulo 14 (rascunho)](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 (rascunho) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) ver o SOC como um sistema de pessoas, processos e tecnologia; (2) definir interfaces e requisitos entre componentes; (3) gerenciar trocas com critérios explícitos; (4) planejar o ciclo de vida, da concepção à aposentadoria.

### 16.1 O SOC como sistema

Um SOC combina pessoas (analistas, engenheiros), processos (triagem, escalonamento) e tecnologia (sensores, SIEM, gestão de casos). Zimmerman (2014) argumentou que muitos SOCs investem demais em ferramentas e de menos em pessoas e processos; o pensamento sistêmico os mantém em equilíbrio. Um novo SIEM comprado sem analistas treinados para usá-lo, ou sem um processo de triagem para receber seus alertas, acrescenta custo, mas pouca proteção. O pensamento sistêmico pergunta como uma mudança numa parte afeta as outras: uma nova detecção acrescenta alertas, o que acrescenta carga aos analistas, o que pode exigir uma mudança de processo. Amara aprende a fazer essa cadeia de perguntas antes de propor qualquer ferramenta.

### 16.2 Interfaces

Cada componente troca alguma coisa: os sensores enviam eventos ao SIEM, o SIEM envia alertas ao sistema de casos, os analistas enviam escalonamentos aos responsáveis pela resposta a incidentes. Cada interface precisa de formato, prazo e responsável definidos. A maioria das falhas entre equipes acontece em interfaces que ninguém possui. Se o SIEM muda o formato de seus alertas e ninguém avisa o administrador do sistema de casos, os alertas podem chegar com campos faltando, ou nem chegar. Registrar formato, prazo e responsável de cada interface transforma uma suposição num acordo que pode ser conferido e dá a alguém o dever de notar quando ele se rompe.

### 16.3 Desdobramento dos requisitos

Necessidades de alto nível ("detectar a tomada de conta em até 15 minutos") se desdobram em requisitos de componentes: logs do portal entregues em até 2 minutos, latência da regra abaixo de 5 minutos, reconhecimento pelo analista em até 8 minutos. As partes se somam: dois minutos de entrega, cinco da regra e oito de reconhecimento dão exatamente quinze, o que não deixa folga. Se a entrega dos logs escorregar para quatro minutos, a meta inteira falha, mesmo com a regra e os analistas dentro do prazo. Paolo sugere apertar os orçamentos dos componentes para que o total deixe uma margem, e monitorar cada um separadamente.

### 16.4 Trocas

Mais dados melhoram a visibilidade, mas custam armazenamento e atenção dos analistas. Os engenheiros de sistemas declaram critérios (tempo de detecção, custo, carga dos analistas) e comparam as opções com eles. Declarar os critérios antes de comparar as opções impede que as pessoas escolham a opção de que já gostavam e depois procurem motivos. Os pesos tornam as prioridades explícitas: se o tempo de detecção é o que mais importa, uma opção mais cara que o reduz à metade pode vencer. Amara monta uma pequena tabela para o acréscimo de sensores de rede nos depósitos, pontuando cada opção nos critérios acordados, com a evidência por trás de cada nota.

### 16.5 Ciclo de vida

Os componentes são planejados, construídos, operados, mantidos e aposentados. Aposentar um sensor antigo exige um substituto primeiro, ou a cobertura desaparece em silêncio. A aposentadoria é a fase mais negligenciada. Um sensor desligado durante uma renovação de *hardware* pode deixar uma lacuna que ninguém nota até que um incidente precise de seus dados. Planejar a aposentadoria significa verificar quais regras dependem do componente, confirmar que o substituto produz dados equivalentes e rodar os dois em paralelo por um curto período antes de desligar o antigo. Os responsáveis aprovam cada aposentadoria.

### 16.6 Verificação

Cada requisito tem um teste: um evento sintético cronometrado verifica se a meta de 15 minutos é cumprida de ponta a ponta. O evento sintético é injetado no portal, como se viesse de uma rajada real de logins, e os carimbos de tempo são registrados em cada etapa: chegada do log, disparo da regra, criação do alerta e reconhecimento pelo analista. Comparar os tempos das etapas com os orçamentos dos componentes mostra exatamente onde ocorre o atraso. O teste roda regularmente, e não uma única vez, porque o desempenho deriva à medida que os volumes e a equipe mudam. Metas não cumpridas abrem um chamado.

### 16.7 Caso

Amara desenha o SOC da Lindqvist como um diagrama de blocos e rotula cada interface com formato, latência e responsável. Desenhar o diagrama revela duas interfaces sem responsável nomeado: a alimentação vinda do balanceador de carga e o elo entre o sistema de casos e o serviço de acionamento do plantão. Ele também mostra que os logs do portal passam por um coletor intermediário que ninguém havia listado. Cada lacuna vira uma tarefa, e o diagrama é guardado com os documentos de arquitetura do SOC. Paolo o revisa com ela.

### Modos de falha do sistema

As falhas no nível do sistema muitas vezes ficam nas interfaces: uma mudança de formato a montante quebra em silêncio a análise a jusante. Amara acrescenta um alerta de erro de análise em cada interface.

### Exemplo resolvido

O teste cronometrado dela injeta uma rajada sintética e inofensiva de logins no portal às 14:00:00. O SIEM a recebe às 14:01:40, a regra dispara às 14:05:10 e um analista reconhece às 14:11:30 — 11,5 minutos de ponta a ponta, dentro do requisito de 15 minutos. A etapa mais lenta é o reconhecimento pelo analista.

> **Caso sintético.** O projeto do SOC e o teste são inventados.

### Erros e limites

Testes de ponta a ponta em horários tranquilos podem subestimar os atrasos em períodos movimentados; repita-os sob carga.

### Exercícios

- **EX046 — Equilíbrio.** Contra que desequilíbrio Zimmerman (2014) alertou? *Rubrica:* 3 = investir demais em ferramentas vs pessoas e processos; 2 = parcial; 1 = vago; 0 = nada.
- **EX047 — Desdobramento do requisito.** Desdobre "detectar em até 15 minutos" em requisitos de componentes. *Rubrica:* 3 = entrega dos logs, latência da regra, reconhecimento, com os tempos; 2 = dois; 1 = um; 0 = nada.
- **EX048 — Teste cronometrado.** O que o teste de ponta a ponta mostrou? *Rubrica:* 3 = 11,5 min no total; dentro da meta; reconhecimento mais lento; 2 = parcial; 1 = errado; 0 = nada.

### Síntese

A engenharia de sistemas liga as pessoas, os processos e a tecnologia do SOC por meio de interfaces, requisitos e testes definidos.

### Continue estudando — capítulo 16 de 50

[← Capítulo 15 (rascunho)](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 (rascunho) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) explicar os laços de realimentação nas operações de segurança; (2) modelar o ajuste fino como um sistema de controle; (3) reconhecer oscilação e instabilidade nos limiares de alerta; (4) projetar uma realimentação estável, com medição.

### 17.1 Laços de realimentação

Um laço de realimentação mede uma saída e ajusta uma entrada para atingir uma meta. Um termostato mede a temperatura e liga ou desliga o aquecimento. Num SOC, os analistas medem a qualidade dos alertas e ajustam as regras. Um laço tem quatro partes: uma meta, uma medição, uma comparação e um ajuste. Se faltar qualquer parte, o laço não funciona. Muitos SOCs têm o ajuste, já que os engenheiros de fato ajustam regras, mas não têm uma meta clara nem uma medição confiável, e o ajuste vira uma reação à reclamação mais barulhenta daquela semana.

### 17.2 O ajuste fino como controle

Suponha que a meta seja menos de 20 alertas falsos por dia vindos de uma regra. Se a contagem medida for maior, o limiar sobe; se ataques reais forem perdidos, ele desce. Isso é um laço de controle em que o engenheiro é o controlador. O laço tem duas pressões opostas: os alertas falsos empurram o limiar para cima, os ataques perdidos o empurram para baixo. Um bom controlador equilibra as duas, em vez de reagir apenas à mais visível. Os analistas veem os alertas falsos todos os dias, enquanto as perdas podem ficar escondidas, então os engenheiros precisam procurar as perdas de forma deliberada, ou o limiar vai derivar para cima com o tempo.

### 17.3 Oscilação

Se os ajustes forem grandes ou rápidos demais, o sistema passa do ponto: o limiar salta para cima, perde um ataque, salta para baixo, inunda os analistas. Passos pequenos e medidos, com tempo para observar os efeitos, evitam a oscilação. Um termostato que ligasse e desligasse o aquecimento por completo à menor mudança faria um cômodo oscilar entre quente e frio demais. O ajuste de regras se comporta do mesmo modo. Mudar um limiar de cinco para seis e depois observar por quinze dias dá evidência clara do efeito. Mudar de cinco para quinze e voltar dentro de uma semana não diz nada a ninguém.

### 17.4 Atraso

A realimentação nos SOCs é lenta: o efeito de uma mudança sobre os ataques perdidos pode levar semanas para ser conhecido. Atrasos longos tornam perigoso o ajuste agressivo. Um ataque perdido pode vir à tona só quando um cliente reclama ou quando uma investigação posterior encontra sinais anteriores. Se um engenheiro eleva um limiar hoje, o custo dessa mudança pode só aparecer em um mês. Sinais mais rápidos, como eventos de teste injetados que deveriam ser pegos, encurtam o laço ao mostrar de imediato se uma mudança abriu uma lacuna.

### 17.5 Realimentação positiva

Alguns laços amplificam: uma fila sobrecarregada faz os analistas fecharem alertas mais depressa e com menos cuidado, o que esconde perdas, o que leva a mais comprometimentos silenciosos. Reconhecer esses laços permite aos gestores rompê-los. O laço se alimenta sozinho: mais comprometimentos silenciosos levam a mais incidentes depois, que acrescentam mais trabalho, que aumenta a pressão para fechar alertas rapidamente. Rompê-lo pode significar desativar temporariamente regras de baixo valor para dar tempo aos analistas, ou acrescentar pessoal. Gestores que acompanham apenas o tamanho da fila podem vê-la encolher e acreditar que as coisas melhoraram, enquanto a qualidade cai.

### 17.6 Medição

A realimentação só é tão boa quanto sua medição. Amostras rotuladas de alertas fechados e eventos de teste seguros periódicos fornecem sinais sobre as perdas. Amostras rotuladas significam revisar uma seleção aleatória de alertas fechados e verificar se a decisão de fechamento estava certa. Isso mostra com que frequência os fechamentos como benignos estavam, na verdade, errados. Eventos de teste seguros, injetados sem aviso, mostram se a cadeia completa, do sensor ao analista, ainda funciona. Ambos dão ao laço dados sobre as perdas, que as contagens comuns de alertas não conseguem revelar. Ambos alimentam a revisão mensal.

### 17.7 Caso

O limiar da regra do portal de Amara começa em 5 falhas a cada 10 minutos; Paolo pede que ela planeje o laço de ajuste. O plano de Amara nomeia a meta, no máximo um número definido de alertas falsos por dia, sem nenhuma rajada de teste perdida; as medições, contagens diárias e rajadas injetadas semanalmente; o tamanho do passo, uma falha de cada vez; e a espera, duas semanas entre mudanças. Paolo o aprova com um acréscimo: toda mudança e seu resultado devem ser escritos no histórico da regra. Amara começa o laço na segunda-feira seguinte.

### Exemplo resolvido

Amara propõe: medir semanalmente os alertas falsos e a detecção dos eventos de teste; mudar o limiar no máximo um passo a cada quinze dias; nunca elevá-lo se algum evento de teste tiver sido perdido. Depois de quatro semanas, a regra se estabiliza em 6 falhas, com 8 alertas falsos por dia e todos os eventos de teste pegos.

> **Caso sintético.** Os limiares e as contagens são inventados.

### Erros e limites

Tratar o ajuste como controle é um modelo; os atacantes se adaptam de propósito, ao contrário do calor num cômodo.

### Exercícios

- **EX049 — Causa da oscilação.** O que causa a oscilação do limiar, e como ela é evitada? *Rubrica:* 3 = mudanças grandes/rápidas; passos pequenos com tempo de observação; 2 = parcial; 1 = vago; 0 = nada.
- **EX050 — Laço nocivo.** Descreva um laço de realimentação positiva num SOC. *Rubrica:* 3 = sobrecarga → fechamentos apressados → ataques perdidos → mais comprometimento; 2 = parcial; 1 = vago; 0 = nada.
- **EX051 — Plano de ajuste.** Declare as regras de ajuste de Amara e o resultado. *Rubrica:* 3 = ≤ 1 passo a cada quinze dias; nada de elevar se um teste foi perdido; estabilizou em 6, 8 falsos/dia, todos os testes pegos; 2 = parcial; 1 = só o resultado; 0 = nada.

### Síntese

Trate o ajuste fino como um laço de realimentação lento: meça com cuidado, ajuste com delicadeza e fique atento aos laços que amplificam.

### Continue estudando — capítulo 17 de 50

[← Capítulo 16 (rascunho)](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 (rascunho) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever a arquitetura de segurança como o posicionamento estruturado de controles; (2) projetar zonas de rede e fronteiras de confiança; (3) posicionar sensores onde eles veem a atividade mais relevante; (4) avaliar a arquitetura em relação às ameaças.

### 18.1 O que significa arquitetura

A arquitetura de segurança decide onde ficam os controles e como os componentes confiam uns nos outros. É a estrutura que faz os controles individuais trabalharem juntos, em vez de formarem uma pilha de produtos. Produtos comprados separadamente podem se sobrepor em algumas áreas e deixar lacunas em outras. A arquitetura parte dos sistemas e dados a proteger, decide de que controles cada um precisa e então escolhe produtos para cumprir esses papéis. Ela também define como as partes confiam umas nas outras, como quais sistemas podem enviar logs ao SIEM e como provam quem são.

### 18.2 Zonas e fronteiras

A Lindqvist separa o portal voltado para a internet, os sistemas internos de negócio, as redes dos depósitos que operam os leitores portáteis e os próprios sistemas do SOC. Cada fronteira tem regras sobre o que pode atravessá-la. As fronteiras são onde o monitoramento é mais informativo, porque o tráfego legítimo que as atravessa é limitado e conhecido. Dentro de uma zona, muitos sistemas conversam livremente e o tráfego é difícil de julgar. Numa fronteira, só fluxos específicos devem passar: o portal pode chamar o sistema de pedidos numa porta, os depósitos podem enviar dados de leitura a um servidor. Qualquer outra coisa que atravesse é suspeita por definição, o que dá ao monitoramento uma linha de base clara para comparação.

### 18.3 Posicionamento de sensores

Os sensores devem ficar onde veem a atividade relevante com pouco ruído: na camada web, para o portal; nos controladores de domínio, para a autenticação; na fronteira entre as redes de negócio e dos depósitos. Pôr um único sensor grande na borda da internet vê muito tráfego, mas pouco contexto. Um sensor de borda vê cada pacote vindo da internet, a maior parte dele ruído de varredura, sem saber a que conta de cliente uma requisição se referia. Um sensor na camada web vê a requisição decifrada e o nome de usuário. Posicionar sensores onde o significado está disponível, e não onde o volume é maior, dá aos analistas eventos em menor número e mais ricos para trabalhar.

### 18.4 Protegendo o SOC

O SIEM e o sistema de casos são alvos valiosos: mostram o que os defensores conseguem ver. Ficam em sua própria zona, com contas de administrador separadas e autenticação multifator. Um atacante que controle o SIEM pode ver quais alertas existem, descobrir quais ações estão sendo detectadas ou apagar evidências. Contas de administrador separadas fazem com que uma conta de funcionário comprometida na zona de negócio não consiga alcançar os sistemas do SOC. O SOC também monitora os próprios sistemas, com alertas sobre mudanças de configuração e sobre logins vindos de fora da zona do SOC.

### 18.5 Mapeamento às ameaças

Os arquitetos conferem cada técnica importante do ATT&CK contra a arquitetura: que controle a previne, que sensor a veria e que equipe responderia. As lacunas viram itens do *backlog*. O D3FEND ajuda a nomear a técnica defensiva que cada controle oferece. O exercício produz uma tabela: cada técnica numa linha, com colunas para prevenção, detecção e responsável pela resposta. As células vazias são lacunas. Nem toda lacuna precisa ser fechada; algumas técnicas são improváveis contra a Lindqvist, e a discussão de risco decide as prioridades. Os nomes do D3FEND, como *credential hardening*, facilitam comparar controles entre produtos.

### 18.6 Simplicidade

Arquiteturas complexas escondem lacunas. Menos fronteiras, e bem compreendidas, são mais fáceis de monitorar. Cada fronteira extra precisa de suas próprias regras, sensores e manutenção, e as exceções se acumulam com o tempo até que ninguém lembre por que um fluxo é permitido. Fundir zonas que servem ao mesmo propósito pode tornar o monitoramento mais claro. Amara observa que a Lindqvist tem três projetos de rede de depósito ligeiramente diferentes, o que multiplica o trabalho de definir o tráfego normal de cada um. Ela propõe um projeto padrão de depósito, implantado à medida que o equipamento de cada local for substituído, para que a linha de base só precise ser definida uma vez.

### 18.7 Caso

Amara revisa onde os logs do portal são produzidos e descobre que o balanceador de carga, que vê os endereços reais dos clientes, não estava encaminhando seus logs; os servidores web viam apenas o endereço do balanceador em algumas requisições. Como o balanceador substituía os endereços dos clientes pelo seu próprio em algumas requisições, os logs dos servidores web mostravam muitas tentativas vindas de um único endereço interno. Agregar por rede então agrupava clientes sem relação entre si e escondia as fontes reais. Encaminhar os logs do balanceador, e configurá-lo para repassar o endereço original num cabeçalho, corrige tanto os dados quanto a precisão da regra.

### Exemplo resolvido

Antes que essa mudança entre em produção, Paolo só a aprova depois de verificar que o cabeçalho não pode ser forjado de fora: o balanceador sobrescreve qualquer cabeçalho que um cliente envie, então o endereço registrado é confiável.

> **Caso sintético.** A arquitetura e as zonas são inventadas.

### Erros e limites

Os diagramas de arquitetura se afastam da realidade; verifique com o tráfego e a configuração, não apenas com os desenhos.

### Exercícios

- **EX052 — Monitoramento de fronteiras.** Por que o monitoramento é mais informativo nas fronteiras de confiança? *Rubrica:* 3 = o tráfego legítimo que atravessa é limitado e conhecido; 2 = parcial; 1 = vago; 0 = nada.
- **EX053 — Lacuna do balanceador de carga.** Que lacuna Amara encontrou, e como foi fechada com segurança? *Rubrica:* 3 = logs do balanceador não encaminhados; cabeçalho do cliente acrescentado, o balanceador sobrescreve o cabeçalho enviado pelo cliente; 2 = parcial; 1 = ignorada; 0 = nada.
- **EX054 — Proteção do SOC.** Como os próprios sistemas do SOC são protegidos? *Rubrica:* 3 = zona própria, contas de administrador separadas, MFA; 2 = duas; 1 = uma; 0 = nada.

### Síntese

Uma boa arquitetura posiciona controles e sensores nas fronteiras, protege o próprio SOC e é conferida em relação às ameaças.

### Continue estudando — capítulo 18 de 50

[← Capítulo 17 (rascunho)](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 (rascunho) →](#ch-19)

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) explicar autenticação, autorização e métodos multifator; (2) relacionar eventos de identidade à detecção; (3) descrever *hashing*, cifragem e assinaturas nas ferramentas do SOC; (4) reconhecer ataques baseados em identidade do ponto de vista do defensor.

### 19.1 A identidade como novo perímetro

Muitos ataques hoje usam credenciais válidas em vez de explorações técnicas. Os logs de autenticação — sucessos, falhas, desafios de MFA, emissão de *tokens* — estão, por isso, entre os dados mais valiosos de um SOC. Com serviços em nuvem e trabalho remoto, não há uma única borda de rede que todo acesso atravesse. São as credenciais que concedem acesso, por isso os atacantes as compram, adivinham ou roubam. Os logs dos sistemas de identidade mostram quem tentou entrar, de onde, com que resultado e qual segundo fator foi usado, o que os torna centrais para identificar o mau uso.

### 19.2 Autenticação e autorização

A autenticação prova quem um usuário é; a autorização decide o que ele pode fazer. O portal autentica os clientes por senha; os funcionários da Lindqvist usam *single sign-on* com MFA. Os logs de autorização mostram o acesso a funções sensíveis, como alterar um endereço de entrega. Uma senha correta satisfaz a autenticação, mas o portal ainda decide se aquele cliente pode ver um determinado pedido. Os logs de cada etapa respondem a perguntas diferentes: os de autenticação mostram quem entrou, os de autorização mostram o que tentaram fazer. Um atacante que entra com sucesso muitas vezes aparece depois nos logs de autorização por meio de ações incomuns.

### 19.3 Sinais de MFA

O MFA reduz o sucesso do *credential stuffing*. Seus logs acrescentam sinais: pedidos de MFA repetidamente negados pelo usuário podem indicar que alguém tem a senha; uma troca súbita do dispositivo de MFA merece verificação. Pedidos negados sugerem que a senha é conhecida por outra pessoa, já que o usuário real está recusando um acesso que não iniciou. Pedidos repetidos enviados em sequência rápida podem ser uma tentativa de vencer o usuário pelo cansaço até que ele aprove um. Um novo dispositivo de MFA registrado logo depois de um acesso vindo de um lugar desconhecido merece revisão imediata.

### 19.4 *Hashing*

Um *hash* criptográfico dá uma impressão digital de tamanho fixo dos dados. Os SOCs usam *hashes* para identificar arquivos e verificar se a evidência exportada não foi alterada. As senhas devem ser armazenadas com funções de *hash* de senha lentas e com *salt*, para que bancos de dados roubados resistam à quebra. Um *hash* de arquivo permite aos analistas procurar o mesmo arquivo em muitas máquinas sem mover o próprio arquivo. A evidência exportada que recebe um *hash* na exportação pode ser conferida depois por qualquer pessoa. O *hashing* de senhas é diferente: funções projetadas para ser lentas e com *salt* tornam cada palpite caro, de modo que um banco de dados roubado não pode ser conferido rapidamente contra bilhões de palpites.

### 19.5 Cifragem e assinaturas

A cifragem protege a confidencialidade em trânsito (TLS) e em repouso. As assinaturas digitais provam origem e integridade: software assinado, lotes de logs assinados. Ferramentas de teste de carga assinadas, como no capítulo 14, permitem às regras fazer exceções confiáveis. A cifragem em trânsito impede que alguém na rede leia os logins; a cifragem em repouso protege os dados armazenados se um disco for roubado. As assinaturas respondem a outra pergunta: isto veio de quem diz ter vindo, sem alterações? Uma regra pode excluir com segurança os testes de carga de uma ferramenta cuja assinatura é verificada e, ainda assim, alertar sobre uma cópia não assinada que usa o mesmo nome.

### 19.6 Ataques de identidade vistos pelo defensor

*Credential stuffing*, *password spraying* e roubo de *tokens* deixam rastros nos logs de identidade. O trabalho do defensor é coletar esses logs e conhecer os padrões normais, não reproduzir os ataques. O *credential stuffing* testa pares vazados de nome de usuário e senha em muitas contas; o *password spraying* testa algumas senhas comuns contra muitas contas; o roubo de *tokens* reutiliza um *token* de sessão sem precisar da senha. Cada padrão parece diferente nos logs, e as detecções são construídas a partir dessas visões defensivas, com dados sintéticos, e não a partir de tentativas reais.

### 19.7 Caso

Depois do incidente, a Lindqvist oferece MFA opcional aos clientes e alerta sobre alterações de endereço logo após um login vindo de uma rede nova. O MFA opcional protege os clientes que o escolhem; o alerta de alteração de endereço protege todos, porque uma mudança do endereço de entrega muitas vezes é o que um atacante quer depois de entrar numa conta. O alerta combina dois sinais, uma rede nova e uma alteração sensível, embora sua primeira semana mostre com que frequência clientes honestos que se mudam também correspondem aos dois. A equipe de segurança planeja revisar a adesão ao MFA depois de seis meses. Os clientes são informados de como ativá-lo.

### Exemplo resolvido

Amara projeta uma regra: "alteração de endereço até 10 minutos depois de um login bem-sucedido a partir de uma rede não vista para aquele cliente em 90 dias". No modo só monitoramento, ela dispara 12 vezes numa semana; 11 são clientes que se mudaram e entraram a partir da rede da nova casa. Ela acrescenta, para essas alterações, uma etapa de confirmação por e-mail ao cliente em vez de um alerta ao analista, mantendo o alerta apenas quando a confirmação falha.

> **Caso sintético.** As regras e as contagens são inventadas.

### Erros e limites

Os logs de identidade de provedores externos podem chegar atrasados ou sem alguns campos; confira os tempos de entrega.

### Exercícios

- **EX055 — Por que logs de identidade.** Por que os logs de autenticação estão entre os dados mais valiosos do SOC? *Rubrica:* 3 = os ataques muitas vezes usam credenciais válidas; os logs mostram seu uso; 2 = parcial; 1 = vago; 0 = nada.
- **EX056 — Sinais de MFA.** Dê dois sinais de detecção relacionados ao MFA. *Rubrica:* 3 = pedidos negados repetidamente; novo dispositivo de MFA; 2 = um; 1 = vago; 0 = nada.
- **EX057 — Projeto da confirmação.** Como Amara reduziu o ruído da regra de alteração de endereço? *Rubrica:* 3 = confirmação por e-mail ao cliente; alerta só quando a confirmação falha; 2 = parcial; 1 = regra apagada; 0 = nada.

### Síntese

Os eventos de identidade e as ferramentas criptográficas são material central do SOC; projete as detecções em torno de como os usuários legítimos se comportam.

### Continue estudando — capítulo 19 de 50

[← Capítulo 18 (rascunho)](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 (rascunho) →](#ch-20)

<a id="ch-20"></a>

## Capítulo 20 — Operações de segurança e blue team: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) descrever a missão e os serviços do SOC em termos de engenharia; (2) relacionar as funções do SOC ao risco da organização; (3) identificar partes interessadas e restrições; (4) enquadrar os problemas de engenharia de SOC para o restante do curso.

### 20.1 Missão primeiro

Knerler, Parker e Zimmerman (2022) começam com "saiba o que você está protegendo e por quê". A Lindqvist protege dados de clientes, operações de entrega e fluxos de pagamento. As escolhas de engenharia decorrem dessa missão, e não dos recursos das ferramentas. Começar pelas ferramentas leva a coletar tudo o que a ferramenta suporta. Começar pela missão leva a perguntar que dano importaria mais: dados de clientes roubados, entregas paradas ou pagamentos desviados. Essas respostas decidem quais sistemas precisam da melhor cobertura e quais alertas merecem acionar alguém à noite, de modo que o esforço de engenharia segue o impacto no negócio.

### 20.2 Serviços do SOC

O SOC da Lindqvist oferece monitoramento e triagem, coordenação da resposta a incidentes, engenharia de detecção, recebimento de vulnerabilidades e consumo de inteligência de ameaças. Cada serviço tem clientes dentro da empresa e saídas mensuráveis. Tratar cada um como serviço esclarece a quem ele atende e como medi-lo. O monitoramento atende à empresa inteira e é medido pelos tempos de detecção e de resposta; a engenharia de detecção atende aos analistas e é medida pela qualidade das regras; o recebimento de vulnerabilidades atende às equipes de TI e é medido pela rapidez com que os relatos chegam aos responsáveis. Serviços pouco claros tendem a escorregar para trabalho não planejado.

### 20.3 Restrições

Orçamento, tamanho da equipe, regulação e sistemas legados restringem o projeto. Os leitores dos depósitos rodam software antigo que não comporta agentes, então o monitoramento de rede precisa cobri-los. As restrições são insumos do projeto, não desculpas. O software antigo dos leitores, que não consegue rodar um agente, exclui a telemetria de *endpoint*, então o projeto passa a observar o tráfego dos leitores na rede do depósito. O orçamento pode limitar os sensores, primeiro, aos depósitos mais movimentados. A regulação pode exigir que certos logs sejam guardados por períodos definidos. Cada restrição é registrada por escrito, para que leitores posteriores entendam o projeto.

### 20.4 Partes interessadas

O CISO define as prioridades; as operações de TI são donas dos sistemas; as equipes jurídica e de privacidade definem limites; as unidades de negócio sentem o impacto das ações de resposta. Os engenheiros de SOC precisam trabalhar com todos eles. As operações de TI podem resistir a um sensor que possa deixar seus sistemas lentos; a equipe jurídica pode limitar o conteúdo que pode ser coletado; as unidades de negócio podem se opor ao bloqueio de uma conta no horário de pico das entregas. Engenheiros que os envolvem cedo ouvem essas preocupações enquanto o projeto ainda é flexível. Amara mantém uma lista de partes interessadas com o que mais importa para cada grupo.

### 20.5 Problemas de engenharia pela frente

O curso acompanha quatro problemas na Lindqvist: detectar a tomada de contas no portal; monitorar as redes dos depósitos sem agentes; manter o SIEM dentro da capacidade; e provar, por meio da verificação, que o SOC funciona. Cada problema recorre a habilidades diferentes: a tomada de contas, a dados de identidade e estatística; o monitoramento dos depósitos, a redes e arquitetura; a capacidade do SIEM, a sistemas de dados e matemática; e a verificação, a testes e medição. Acompanhar a mesma empresa nos quatro permite ao curso mostrar como decisões numa área, como as camadas de armazenamento, restringem as opções em outra.

### 20.6 Maturidade

O SOC-CMM (van Os, 2016) avalia negócio, pessoas, processos, tecnologia e serviços. A autoavaliação da Lindqvist mostra tecnologia forte, mas documentação de processos fraca, o que orienta as prioridades. Um modelo de maturidade oferece um modo estruturado de ver forças e fraquezas no SOC inteiro. Tecnologia forte com documentação de processos fraca significa que as ferramentas funcionam, mas os resultados dependem de qual analista está no turno. A autoavaliação sugere escrever *playbooks* antes de comprar mais ferramentas e dá uma linha de base para repetir depois e mostrar o progresso. A avaliação é repetida a cada ano, pelo mesmo método.

### 20.7 Medidas de sucesso

O sucesso não é "nenhum incidente", e sim detecção mais rápida, decisões melhores e menos dano. Um ano tranquilo pode significar que nada aconteceu, ou que nada foi detectado; os dois parecem iguais numa contagem de incidentes. Medidas melhores incluem o tempo entre a primeira evidência e a detecção, o tempo até a contenção e com que frequência as decisões de resposta foram depois julgadas corretas. O SOC da Lindqvist relata essas medidas mensalmente, junto com notas honestas sobre qualquer detecção perdida. Cada medida tem uma meta declarada, e as tendências ao longo de vários meses importam mais do que o número de um único mês, que pode oscilar com um único incidente grande.

### Financiamento do SOC

O orçamento do SOC compete com outros trabalhos de TI. Engenheiros que conseguem mostrar como uma mudança reduz o risco ou o tempo dos analistas obtêm apoio com mais facilidade do que os que pedem ferramentas.

### Exemplo resolvido

Amara escreve um resumo de contexto de uma página: missão, serviços, restrições, partes interessadas e os quatro problemas de engenharia. Paolo acrescenta uma restrição que ela deixou passar — o SOC tem apenas dois analistas no turno da noite —, o que molda todas as decisões de alerta.

> **Caso sintético.** O SOC da Lindqvist e sua avaliação são inventados.

### Erros e limites

O contexto muda com o negócio; revise o resumo quando a empresa mudar.

### Exercícios

- **EX058 — Vínculo com a missão.** Como a missão orienta as escolhas de engenharia? *Rubrica:* 3 = o que é protegido define as prioridades, não os recursos das ferramentas; 2 = parcial; 1 = vago; 0 = nada.
- **EX059 — Restrição dos depósitos.** Por que os leitores dos depósitos precisam ser monitorados pela rede? *Rubrica:* 3 = o software antigo não comporta agentes; 2 = parcial; 1 = nenhum motivo; 0 = nada.
- **EX060 — Turno da noite.** Por que importa o turno da noite com dois analistas? *Rubrica:* 3 = limita o volume de alertas que eles conseguem tratar; molda os alertas; 2 = parcial; 1 = irrelevante; 0 = nada.

### Síntese

A engenharia de SOC parte da missão, dos serviços, das restrições e das partes interessadas; o restante do curso resolve problemas dentro desses limites.

### Continue estudando — capítulo 20 de 50

[← Capítulo 19 (rascunho)](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 (rascunho) →](#ch-21)

<a id="ch-21"></a>

## Capítulo 21 — Operações de segurança e blue team: requisitos

### Objetivos de aprendizagem

Você vai (1) levantar requisitos de SOC junto às partes interessadas e a partir das ameaças; (2) escrever requisitos funcionais e não funcionais mensuráveis; (3) rastrear requisitos até ameaças e testes; (4) priorizar requisitos sob restrições.

### 21.1 Fontes de requisitos

Os requisitos vêm da missão, das ameaças, das regulações, dos incidentes e das dores dos analistas. O incidente do portal produziu o requisito "detectar provável tomada de conta no portal do cliente em até 15 minutos". Cada fonte puxa numa direção. As ameaças sugerem o que os atacantes vão tentar; as regulações definem mínimos, como a retenção; os incidentes expõem lacunas que de fato machucaram; as dores dos analistas revelam onde o trabalho é desperdiçado com regras ruidosas ou falta de contexto. Coletar de todas elas evita um conjunto de requisitos que reflita apenas a voz mais alta, e a fonte de cada um é registrada ao lado dele.

### 21.2 Requisitos funcionais

Dizem o que o sistema faz: ingerir os logs do balanceador de carga; correlacionar falhas e sucessos por rede; gerar um alerta com o ID do cliente, a rede de origem e as ações subsequentes. Cada enunciado é formulado como algo que o sistema precisa fazer, para que um testador possa conferi-lo diretamente: alimentar logs do balanceador e ver se são ingeridos; criar uma rajada de falhas seguida de um sucesso e ver se a correlação dispara; abrir o alerta e ver se ele traz os três campos nomeados. Verbos vagos como "suportar" ou "tratar" são evitados.

### 21.3 Requisitos não funcionais

Dizem quão bem: latência abaixo de 5 minutos do evento ao alerta; disponibilidade de 99,5% para o *pipeline*; no máximo 10 alertas falsos por dia para o turno da noite; dados retidos por 90 dias na camada quente. Essas qualidades são muitas vezes onde os sistemas decepcionam, porque são fáceis de esquecer durante o projeto. Uma regra logicamente perfeita, mas que alerta vinte minutos atrasada, perde a meta. Uma meta de disponibilidade de 99,5% admite cerca de 44 horas de indisponibilidade do *pipeline* por ano, que Amara compara com as janelas de manutenção já planejadas, para conferir se o número é realista.

### 21.4 Redação mensurável

"Rápido" e "preciso" não podem ser testados. Cada requisito declara um número, uma condição e um método de medição. Por exemplo, "rápido" vira "95% dos alertas criados em até 5 minutos após o evento que os aciona, medidos do horário do evento ao horário do alerta ao longo de um mês civil". O método importa tanto quanto o número: medir a partir do horário de ingestão, e não do horário do evento, esconderia atrasos na entrega dos logs e faria o *pipeline* parecer melhor do que é. Amara reescreve todos os requisitos nessa forma e pede a Paolo que tente escrever um teste para cada um; o que ele não conseguir testar volta para ser reescrito.

### 21.5 Rastreabilidade

Uma tabela liga cada requisito à sua fonte (ameaça, regulação, incidente), ao elemento de projeto que o atende e ao teste que o verifica. Os IDs de técnicas do ATT&CK dão uma referência comum para as fontes de ameaça. A tabela funciona nos dois sentidos. Lendo para a frente, a partir de uma ameaça, vê-se se algo a trata; lendo para trás, a partir de um teste, vê-se por que ele existe. Uma regulação alterada é rastreada do mesmo modo, de sua linha até os requisitos e testes que a citam. Usar IDs de técnicas permite à equipe de segurança e aos relatórios externos se referirem à mesma ameaça sem ambiguidade.

### 21.6 Priorização

Com equipe limitada, Amara e Paolo classificam os requisitos como obrigatório, desejável ou opcional, guiados pelo risco e pelo custo. Um obrigatório é algo sem o qual o sistema falha em seu propósito, como detectar a tomada de conta; um desejável acrescenta valor real, mas pode esperar, como enriquecer os alertas com o nível do cliente; um opcional é bom de ter. Classificar abertamente permite aos gestores ver o que não será entregue neste trimestre, em vez de descobrirem isso mais tarde, quando o tempo acabar. Os obrigatórios são financiados primeiro; os opcionais esperam capacidade ociosa.

### 21.7 Controle de mudanças

Os requisitos mudam; cada mudança é registrada com motivo e aprovação, e os testes afetados são atualizados. Sem isso, os requisitos se deslocam em silêncio por meio de conversas, e os testes acabam verificando algo com que ninguém concordou. Registrar o motivo mantém as mudanças honestas: baixar o limite de alertas falsos porque os analistas reclamaram é diferente de baixá-lo porque o turno da noite foi reduzido. Atualizar os testes junto mantém a verificação alinhada com o que agora se espera do sistema. Paolo aprova cada mudança, e o requisito mantém seu histórico, para que resultados de testes anteriores ainda possam ser interpretados em relação à versão vigente na época.

### Critérios de aceitação

Cada requisito tem critérios de aceitação acordados antes da construção: que resultado em qual teste conta como aprovado. Acordá-los cedo evita discussões posteriores sobre se o trabalho está pronto e dá aos analistas uma promessa clara do que a nova detecção vai entregar.

### Exemplo resolvido

O requisito R-07 de Amara diz: "O *pipeline* deve gerar um alerta de possível tomada de conta em até 15 minutos após um login bem-sucedido no portal que se siga a pelo menos 6 falhas para usuários distintos a partir da mesma /24 em 10 minutos; verificado mensalmente por um evento sintético cronometrado." Paolo o aprova como obrigatório.

> **Caso sintético.** Os requisitos são inventados.

### Erros e limites

Requisitos demais se tornam ingerenciáveis; concentre-se nos ligados a riscos reais.

### Exercícios

- **EX061 — Funcional versus não funcional.** Dê um requisito funcional e um não funcional do caso. *Rubrica:* 3 = por exemplo, correlacionar falhas/sucessos; latência abaixo de 5 minutos; 2 = um; 1 = confuso; 0 = nada.
- **EX062 — Redação mensurável.** Reescreva "os alertas precisam ser rápidos" como um requisito mensurável. *Rubrica:* 3 = número, condição, medição; 2 = parcial; 1 = inalterado; 0 = nada.
- **EX063 — Tabela de rastreabilidade.** Que colunas tem a tabela de rastreabilidade? *Rubrica:* 3 = requisito, fonte, elemento de projeto, teste; 2 = três; 1 = uma; 0 = nada.

### Síntese

Requisitos mensuráveis, rastreáveis e priorizados transformam incidentes e ameaças em trabalho de engenharia.

### Continue estudando — capítulo 21 de 50

[← Capítulo 20 (rascunho)](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 (rascunho) →](#ch-22)

<a id="ch-22"></a>

## Capítulo 22 — Operações de segurança e blue team: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) modelar o *pipeline* do SOC como etapas e repositórios de dados; (2) definir o modelo de dados de eventos; (3) modelar entidades como usuários, hosts e clientes; (4) usar modelos para encontrar lacunas.

### 22.1 Modelo do *pipeline*

O *pipeline* da Lindqvist tem etapas: coleta (agentes, syslog, APIs de nuvem), transporte, análise e normalização, enriquecimento (dados de ativos e de identidade), armazenamento, detecção, alerta e gestão de casos. Cada etapa pode falhar, atrasar ou distorcer os dados. Pensar em etapas ajuda a localizar problemas. Um alerta ausente pode significar que o evento nunca foi coletado, foi descartado no transporte, falhou na análise, não tinha o enriquecimento de que a regra precisava, expirou no armazenamento ou nunca casou com a regra. Cada etapa recebe suas próprias medidas de saúde, para que um analista possa seguir um evento pelo *pipeline* e descobrir onde ele desapareceu.

### 22.2 Modelo de eventos

Todo evento normalizado traz horário (UTC), fonte, host, usuário, ação, resultado e uma referência ao registro bruto. Um modelo compartilhado permite que uma regra funcione em várias fontes. Manter uma referência ao registro bruto importa porque a normalização pode perder detalhes ou introduzir erros; um analista pode precisar da linha original para conferir o que a fonte de fato disse. Registrar o horário em UTC evita confusão entre fontes em fusos diferentes. Como todas as fontes se mapeiam para os mesmos campos, uma regra sobre logins malsucedidos funciona no portal, na VPN e no acesso dos funcionários.

### 22.3 Modelo de entidades

As entidades persistem entre eventos: um cliente, um funcionário, um host, uma rede. As tabelas de entidades guardam atributos como criticidade, responsável e locais habituais, usados no enriquecimento. Os eventos são momentos; as entidades lhes dão contexto. Um alerta sobre um host significa mais quando também mostra que o host é um servidor de pagamentos de responsabilidade do financeiro. Os locais habituais de um cliente ajudam a julgar se um login vindo de um país novo é incomum. As tabelas de entidades precisam de atualização, já que dados desatualizados enganam os analistas tanto quanto dados ausentes.

### 22.4 Relações

Clientes possuem contas; funcionários usam hosts; hosts ficam em zonas. Modelar as relações permite aos analistas perguntar automaticamente "em que zona está este host?". Sem relações modeladas, um analista precisa procurar cada vínculo manualmente em sistemas diferentes, o que é lento durante um incidente. Com elas, um alerta pode mostrar automaticamente que o host pertence a uma zona de depósito e que seu usuário habitual está de licença. As relações também permitem às regras raciocinar entre entidades, por exemplo sinalizando um funcionário que usa um host fora de sua própria zona.

### 22.5 Lacunas a partir dos modelos

Percorrendo o modelo etapa por etapa, Amara confere cada fonte: ela é coletada, analisada, enriquecida e coberta por detecções? As redes dos depósitos são coletadas, mas não enriquecidas, porque o inventário de ativos não tem os dispositivos dos depósitos. O percurso é sistemático: para cada fonte, quatro perguntas de sim ou não. A falta de enriquecimento dos dispositivos dos depósitos significa que os alertas sobre eles trazem apenas um endereço, sem responsável, local ou função, de modo que os analistas precisam investigar do zero. A correção fica a montante: acrescentar os dispositivos dos depósitos ao inventário de ativos, o que ajuda as operações de TI tanto quanto o SOC.

### 22.6 Responsável pelo modelo

O modelo de dados pertence à equipe de engenharia de detecção; as mudanças são versionadas como as regras. Um responsável decide quais campos existem e o que significam, e revisa as mudanças propostas. O versionamento permite às regras declarar que versão do modelo esperam, para que a renomeação de um campo não as quebre em silêncio. Sem um responsável, engenheiros diferentes acrescentam campos com significados sobrepostos, e com o tempo o modelo compartilhado se fragmenta em dialetos de cada fonte. O responsável publica um registro de mudanças, e os autores de regras o leem antes de cada liberação. Campos descontinuados continuam disponíveis por uma liberação, para que as regras possam migrar sem lacuna de cobertura.

### 22.7 Modelos e pessoas

Os modelos também incluem quem age em cada etapa: que equipe corrige erros de análise, quem mantém as tabelas de enriquecimento. Um diagrama de *pipeline* que mostra apenas sistemas esconde o trabalho humano que o mantém funcionando. Nomear a equipe responsável pelas falhas dos analisadores faz com que os alertas sobre análise quebrada cheguem a alguém capaz de agir. Nomear o responsável pelas tabelas de enriquecimento faz com que as entradas desatualizadas tenham alguém que responda por elas. Amara acrescenta um responsável a cada etapa do diagrama do *pipeline*. Cada responsável também tem um substituto nomeado, para que uma falha de analisador durante as férias ainda chegue a alguém capaz de corrigi-la.

### Atualidade do enriquecimento

As tabelas de enriquecimento precisam estar em dia. Um host transferido do financeiro para os depósitos e ainda marcado como "financeiro" engana os analistas. Amara acrescenta uma data de atualização a cada tabela.

### Exemplo resolvido

A matriz de cobertura de Amara lista 14 fontes contra 6 etapas. Duas células estão vazias para as redes dos depósitos (enriquecimento, detecção) e uma para o balanceador de carga do portal (detecção, recém-coletado). Ela transforma cada célula vazia num item do *backlog* com um responsável.

> **Caso sintético.** As fontes e a matriz são inventadas.

### Erros e limites

Os modelos simplificam; uma fonte marcada como "coletada" ainda pode ter lacunas no tempo ou nos campos.

### Exercícios

- **EX064 — Etapas do *pipeline*.** Liste as etapas do *pipeline* em ordem. *Rubrica:* 3 = coleta, transporte, análise/normalização, enriquecimento, armazenamento, detecção, alerta, caso; 2 = a maioria em ordem; 1 = poucas; 0 = nada.
- **EX065 — Lacuna dos depósitos.** Por que as redes dos depósitos não eram enriquecidas? *Rubrica:* 3 = o inventário de ativos não tinha os dispositivos dos depósitos; 2 = parcial; 1 = nenhum motivo; 0 = nada.
- **EX066 — Uso da matriz.** Como Amara usou a matriz de cobertura? *Rubrica:* 3 = as células vazias viraram itens do *backlog* com responsável; 2 = parcial; 1 = arquivou-a; 0 = nada.

### Síntese

Os modelos de *pipeline*, de eventos e de entidades expõem onde os dados faltam, não são enriquecidos ou não são detectados.

### Continue estudando — capítulo 22 de 50

[← Capítulo 21 (rascunho)](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 (rascunho) →](#ch-23)

<a id="ch-23"></a>

## Capítulo 23 — Operações de segurança e blue team: análise de ameaças e falhas

### Objetivos de aprendizagem

Você vai (1) analisar as ameaças relevantes para a organização com o ATT&CK; (2) analisar os modos de falha do sistema de monitoramento; (3) combinar as visões de ameaças e de falhas em prioridades; (4) documentar as análises para revisão.

### 23.1 Análise de ameaças

A análise de ameaças da Lindqvist pergunta que adversários miram empresas de logística e que técnicas usam. Relatórios públicos e os grupos do ATT&CK mostram abuso de credenciais, *phishing* contra funcionários, *ransomware* e fraude por meio de contas de clientes. Começar pelos adversários que miram o setor mantém a análise ancorada no que de fato acontece a empresas semelhantes. Para uma empresa de logística, a fraude de entregas e o desvio de pagamentos são tão relevantes quanto o roubo de dados. Os grupos do ATT&CK documentam técnicas vistas em campanhas reais, o que transforma uma preocupação genérica com *ransomware* em comportamentos específicos que o SOC pode procurar.

### 23.2 Cobertura de técnicas

Para cada técnica relevante, a equipe registra as fontes de dados necessárias, as detecções existentes e a confiança. Os mapas de cobertura mostram forças (abuso de credenciais no portal) e lacunas (movimento lateral nas redes dos depósitos). A confiança registra quão segura a equipe está de que uma detecção funcionaria, com base em testes, e não em sua mera existência. Uma regra escrita, mas nunca testada, recebe confiança baixa. O mapa de cobertura torna as prioridades visíveis para gestores que não sabem ler regras: forte numa área, fraco em outra, com a evidência por trás de cada classificação.

### 23.3 Análise de falhas

O próprio sistema de monitoramento falha: fontes silenciam, analisadores quebram depois de atualizações, tabelas de enriquecimento ficam desatualizadas, regras são desativadas e esquecidas. Uma tabela de modos de falha e efeitos lista cada falha, seu efeito sobre a detecção, como ela seria notada e sua probabilidade. O formato vem da análise de segurança da engenharia, onde é usado para máquinas e instalações. Aplicado ao monitoramento, cada linha pergunta: se esta parte falhar, que detecções param de funcionar, com que rapidez saberíamos e quão provável é? Um analisador que quebra depois de uma atualização é provável e pode passar dias despercebido, então fica no topo da lista.

### 23.4 Falhas silenciosas

As piores falhas são as silenciosas: uma fonte para de enviar e nada alerta. Elas recebem uma detecção própria, tratada no capítulo 47. O silêncio é perigoso porque a ausência de alertas parece igual à ausência de ataques. Uma fonte que normalmente envia dez mil eventos por hora e de repente não envia nenhum deveria, ela mesma, disparar um alarme. Volumes esperados por fonte, com alertas para quedas grandes, transformam o silêncio num sinal visível. Algumas fontes são naturalmente silenciosas à noite, então os limiares comparam cada hora com a mesma hora das semanas anteriores, e não com uma média diária fixa.

### 23.5 Combinando as visões

A prioridade é mais alta onde uma técnica importante depende de um componente frágil — por exemplo, a detecção de tomada de conta dependendo de uma única alimentação de logs do balanceador de carga. A análise de ameaças mostra o que importa; a análise de falhas mostra o que é frágil. A interseção das duas é onde uma única falha deixaria o SOC cego para uma técnica importante. A alimentação do balanceador de carga é um exemplo claro: se ela parar, a detecção de tomada de conta se degrada. A resposta é uma segunda alimentação ou um monitoramento cerrado da existente. Amara marca essas interseções em vermelho no mapa de cobertura.

### 23.6 Revisão

As análises são revisadas pelos analistas, pelas operações de TI e pelo gabinete do CISO, e retomadas depois de incidentes ou de grandes mudanças. Os analistas sabem em quais detecções se confia na prática; as operações de TI sabem quais componentes são frágeis; o gabinete do CISO conhece as prioridades do negócio. Cada visão corrige as outras. Retomar a análise depois de incidentes a mantém atual, já que um incidente muitas vezes revela uma técnica ou um modo de falha que a revisão original deixou passar. Cada revisão produz uma versão datada, com uma lista curta de mudanças e de quem as pediu, para que leitores posteriores vejam como a visão da equipe sobre ameaças e falhas evoluiu com o tempo.

### 23.7 Evitando vieses

As equipes dão peso demais aos incidentes recentes. Usar o ATT&CK como lista de verificação ajuda a considerar técnicas que ainda não atingiram a Lindqvist. Depois do incidente do portal, a atenção se concentra no abuso de credenciais, e é tentador gastar todo o esforço ali. Uma lista de verificação obriga a equipe a olhar de forma sistemática para outras técnicas, como o mau uso de ferramentas de gerenciamento remoto nos depósitos, que ainda não causaram problemas. A dor recente é um sinal útil, mas um guia completo ruim. Cada técnica deixada de fora é marcada com um motivo curto.

### Ameaças internas e de fraude

Nem toda ameaça é externa. Funcionários com acesso a contas de clientes poderiam fazer mau uso dele, e fraudadores podem usar recursos legítimos do portal. Essas ameaças dependem mais de logs de negócio, como alterações de endereço e reembolsos, do que de telemetria técnica.

### Exemplo resolvido

Entrada da tabela de falhas de Amara: "A alimentação de logs do balanceador de carga para → nenhum alerta de tomada de conta → notado só por acaso → probabilidade média (a alimentação quebrou duas vezes no ano passado) → prioridade alta. Ação: monitoramento de *heartbeat* e um segundo caminho de alimentação."

> **Caso sintético.** As análises são inventadas.

### Erros e limites

Os relatórios de ameaças descrevem a experiência de outros; adapte-os ao seu ambiente.

### Exercícios

- **EX067 — Registro de cobertura.** O que é registrado para cada técnica relevante? *Rubrica:* 3 = fontes de dados, detecções, confiança; 2 = dois; 1 = um; 0 = nada.
- **EX068 — Falha silenciosa.** Por que as falhas silenciosas são as piores? *Rubrica:* 3 = nada alerta, então a detecção desaparece sem ser notada; 2 = parcial; 1 = vago; 0 = nada.
- **EX069 — Prioridade combinada.** Por que a alimentação do balanceador de carga foi classificada como alta? *Rubrica:* 3 = uma detecção importante depende de uma única alimentação frágil; 2 = parcial; 1 = aleatório; 0 = nada.

### Síntese

Combine a cobertura de ameaças com a análise de falhas do sistema de monitoramento para definir as prioridades.

### Continue estudando — capítulo 23 de 50

[← Capítulo 22 (rascunho)](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 (rascunho) →](#ch-24)

<a id="ch-24"></a>

## Capítulo 24 — Operações de segurança e blue team: métodos I

### Objetivos de aprendizagem

Você vai (1) projetar detecções por limiar e por correlação; (2) avaliar regras contra janelas rotuladas; (3) comparar variantes de regras por verdadeiros e falsos positivos; (4) escolher variantes pelo propósito operacional.

### 24.1 Regras por limiar

Uma regra por limiar dispara quando uma contagem numa janela ultrapassa um limite: pelo menos 5 usuários distintos falhando a partir de uma /24 em 10 minutos. Contar usuários distintos, em vez do total de falhas, mira o padrão de *stuffing*: muitas contas, poucas tentativas cada. Um único cliente falhando dez vezes não acionaria a regra, o que é intencional. A janela e o limite são parâmetros a ajustar, e a documentação da regra registra os valores escolhidos e a evidência que levou a eles. Cinco em dez minutos é o ponto de partida.

### 24.2 Regras de correlação

Uma regra de correlação exige várias condições, possivelmente de fontes diferentes: falhas seguidas de um sucesso, ou um sucesso seguido de uma alteração de endereço. A correlação acrescenta significado ao juntar passos que são fracos isoladamente. Falhas acontecem o tempo todo; um sucesso isolado é normal; falhas seguidas de um sucesso a partir da mesma rede sugerem uma senha adivinhada. Uma alteração de endereço depois de um login vindo de uma rede nova é mais suspeita do que qualquer dos dois eventos separadamente. Essas regras precisam de fontes com horários alinhados e campos compartilhados. Os desvios de relógio entre as fontes precisam ser pequenos.

### Laboratório — comparando variantes de regras

```python
"""Evaluate a Sigma-style burst rule over synthetic 10-minute windows with labels."""
windows = [  # (window, distinct users failed, any success, label)
    ("09:50", 2, True, "benign"), ("10:00", 7, True, "attack"), ("10:10", 6, False, "attack"),
    ("10:20", 1, False, "benign"), ("11:00", 9, False, "benign"),   # load test
    ("13:30", 5, True, "attack"), ("14:00", 3, True, "benign"), ("15:00", 6, False, "benign")]
def rule(users, success, threshold): return users >= threshold and success
for t in (5, 6):
    tp = sum(rule(u, s, t) and l == "attack" for _, u, s, l in windows)
    fp = sum(rule(u, s, t) and l == "benign" for _, u, s, l in windows)
    fn = sum(not rule(u, s, t) and l == "attack" for _, u, s, l in windows)
    print(f"threshold={t} with-success: TP={tp} FP={fp} FN={fn}")
tp = sum(u >= 5 and l == "attack" for _, u, s, l in windows); fp = sum(u >= 5 and l == "benign" for _, u, s, l in windows)
print(f"threshold=5 no success clause: TP={tp} FP={fp} FN={3-tp}")
```

Execute com `python3 lab_rule.py`. Saída verificada:

```text
threshold=5 with-success: TP=2 FP=0 FN=1
threshold=6 with-success: TP=1 FP=0 FN=2
threshold=5 no success clause: TP=3 FP=2 FN=0
```

### 24.3 Lendo o resultado

Com a cláusula de sucesso e limiar 5, a regra pega 2 de 3 janelas de ataque, sem alertas falsos; com limiar 6, pega apenas 1. Sem a cláusula de sucesso, o limiar 5 pega as 3 janelas de ataque, mas acrescenta 2 alertas falsos — o teste de carga das 11:00 e uma janela das 15:00. Os números mostram a troca com clareza. Exigir um sucesso torna a regra precisa, mas custa uma janela de ataque, uma tentativa que nunca teve sucesso. Retirar a cláusula pega todas as tentativas, mas acrescenta ruído, inclusive um teste de carga que uma exceção para ferramenta assinada poderia remover. Elevar o limiar para seis perde mais uma janela real sem remover nenhum alerta falso, já que não havia nenhum.

### 24.4 O propósito decide

A variante sem sucesso detecta tentativas; a variante com sucesso detecta comprometimento provável. A Lindqvist usa as duas: as tentativas vão para uma fila diurna de ajuste dos limites de taxa; o comprometimento provável aciona o turno da noite. Nenhuma variante é simplesmente melhor; cada uma responde a uma pergunta diferente. As tentativas importam para ajustar as defesas, como os limites de taxa, e podem esperar o dia. O comprometimento provável exige ação em minutos, então justifica acordar alguém. Dividir a regra por propósito dá a cada uma a urgência certa, em vez de forçar um único limiar de meio-termo para as duas necessidades.

### 24.5 Rótulos

A avaliação precisa de janelas rotuladas. Os rótulos vêm de incidentes investigados, de testes autorizados e da revisão de amostras pelos analistas. Cada fonte de rótulos tem fraquezas. Os incidentes investigados são confiáveis, mas poucos; os testes autorizados são limpos, mas podem não se parecer com ataques reais; as revisões dos analistas são abundantes, mas podem estar erradas. Registrar de onde veio cada rótulo permite aos avaliadores ponderá-los e verificar se os resultados dependem demais de um tipo de rótulo. Ao lado de cada uma de suas oito janelas, Amara escreve qual fonte forneceu o rótulo e quem o confirmou, para que um revisor possa contestar qualquer rótulo isolado.

### 24.6 Amostras pequenas

Oito janelas apenas ilustram o método; uma avaliação real usa semanas de dados. Com oito janelas, uma única janela mal rotulada muda os resultados drasticamente. Semanas de dados dão centenas de janelas, o suficiente para estimar taxas com confiança útil e para ver a variação entre dias úteis e fins de semana. O conjunto pequeno continua valioso para o ensino e para testes unitários, em que cada janela pode ser conferida à mão. Amara declara o tamanho da amostra ao lado de cada número que relata, para que ninguém confunda o exemplo didático com um desempenho medido da regra em produção.

### Nomes e severidade das regras

Cada variante recebe um nome claro e uma severidade. "Tentativas de *stuffing* no portal" é baixa e vai para a fila; "Possível tomada de conta no portal" é alta e aciona o plantão. Os nomes dizem aos analistas o que esperar antes de abrirem o alerta, o que acelera a triagem e reduz a confusão entre regras parecidas.

### Exemplo resolvido

Amara apresenta os resultados a Paolo como uma tabela de variantes, com uma recomendação: acionar o plantão com "limiar 5 com sucesso" e enviar "limiar 5 sem sucesso" para a revisão diurna. A janela de ataque das 10:10 que foi perdida não teve sucesso, então a regra de acionamento corretamente ficou em silêncio — o atacante ainda não tinha entrado. Isso traz o limiar de acionamento de volta dos 6 em que o laço de ajuste anterior se estabilizou para 5. Aquele laço ajustava a regra só de falhas, em que elevar o limiar era a única forma de cortar alertas falsos. Uma vez acrescentada a cláusula de sucesso, ela remove os alertas falsos por si só: nas janelas do laboratório, o limiar 5 com sucesso não tem alertas falsos e pega duas janelas de ataque, enquanto o 6 pega apenas uma. Manter o 6 perderia detecção sem ganhar nada, então o limiar do R-07 é alterado para 5 por meio do controle de mudanças.

> **Caso sintético.** As janelas e os rótulos vêm do script do laboratório.

### Erros e limites

Os próprios rótulos podem estar errados; revise os contestados.

### Exercícios

- **EX070 — Resultados das variantes.** Informe VP, FP e FN das três variantes. *Rubrica:* 3 = 5+sucesso 2/0/1; 6+sucesso 1/0/2; 5 sem sucesso 3/2/0; 2 = duas; 1 = uma; 0 = nada.
- **EX071 — Dois propósitos.** Por que manter uma variante com sucesso e outra sem sucesso? *Rubrica:* 3 = tentativas vs comprometimento provável; filas diferentes; 2 = parcial; 1 = escolher uma; 0 = nada.
- **EX072 — A janela perdida.** Por que perder a janela das 10:10 é aceitável para a regra de acionamento? *Rubrica:* 3 = ainda sem sucesso: não há comprometimento para acionar; 2 = parcial; 1 = não é aceitável; 0 = nada.

### Síntese

Projete variantes de regras para propósitos distintos e escolha-as por resultados medidos em dados rotulados.

### Continue estudando — capítulo 24 de 50

[← Capítulo 23 (rascunho)](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 (rascunho) →](#ch-25)

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) trabalhar em equipe num problema aberto de projeto de SOC; (2) gerar e comparar projetos alternativos; (3) apresentar um projeto com sua justificativa; (4) responder à crítica num ambiente de ateliê.

### 25.1 O problema do ateliê

As equipes projetam o monitoramento das redes dos depósitos da Lindqvist, onde os leitores portáteis e as estações de trabalho antigas não conseguem rodar agentes. O projeto precisa detectar conexões incomuns dos depósitos para os sistemas de negócio. Conexões incomuns podem incluir um leitor conversando com um servidor do financeiro, ou uma estação de trabalho de depósito alcançando sistemas que nunca usou antes. Sem agentes, o projeto precisa se apoiar na observação da rede. As equipes também precisam considerar que os depósitos diferem em tamanho e conectividade, de modo que um único projeto precisa funcionar num pequeno depósito rural e num grande centro de distribuição.

### 25.2 Gerando alternativas

A equipe de Amara lista três opções: monitoramento de fluxos na fronteira entre depósitos e negócio; um sensor de detecção de rede com análise de protocolos; e o aperto das regras de *firewall*, com registro das conexões negadas. Listar várias opções antes de avaliar qualquer uma impede que a primeira ideia vire a única. As três diferem em natureza: uma observa fluxos, uma inspeciona conteúdo, uma restringe o tráfego e registra as recusas. Cada uma tem custos e pontos cegos diferentes, que a comparação por critérios vai evidenciar, e uma solução híbrida pode surgir quando as peças forem compreendidas.

### 25.3 Critérios

Eles comparam as opções em visibilidade, custo, carga operacional, privacidade e modos de falha, usando uma tabela ponderada. A visibilidade pergunta o que cada opção consegue ver; o custo inclui *hardware*, licenças e tempo da equipe; a carga operacional pergunta quem a mantém; a privacidade considera se o conteúdo do tráfego dos funcionários é coletado; os modos de falha perguntam o que acontece quando ela quebra. Os pesos são acordados antes da pontuação, e cada nota cita uma evidência, como uma folha de dados do fornecedor ou uma medição. A privacidade tem peso alto porque os funcionários dos depósitos usam a mesma rede para mensagens pessoais nos intervalos, e a política de monitoramento da empresa limita a coleta de conteúdo.

### 25.4 Crítica no ateliê

Cada equipe apresenta por dez minutos; colegas e professores contestam as suposições. O ateliê valoriza o raciocínio claro mais do que *slides* bem acabados. A crítica mira o projeto, não as pessoas. Contestações típicas são "o que acontece se o sensor falhar?" ou "como vocês vão saber que as regras funcionam?". *Slides* com diagramas impressionantes, mas sem raciocínio, recebem notas baixas. Os professores anotam fraquezas recorrentes entre as equipes e as tratam na aula seguinte. O retorno é escrito em cartões e entregue a cada equipe depois de sua vez, para que os comentários não se percam e os alunos mais calados também possam contribuir.

### 25.5 Iteração

Depois da crítica, as equipes revisam. A equipe de Amara descobre que o *firewall* da fronteira já registra os fluxos permitidos e negados; combinar os logs do *firewall* com um pequeno número de regras de permissão sai mais barato do que um novo sensor. A descoberta veio de perguntar à equipe de TI dos depósitos durante a crítica, o que mostra o valor de envolver quem conhece os sistemas existentes. Usar os logs que o *firewall* já produz custa quase nada em *hardware*. Regras de permissão estritas reduzem o tráfego normal a uma lista curta, de modo que qualquer fluxo negado ou inesperado se destaca com clareza nos logs.

### 25.6 Documentação

O projeto final inclui um diagrama, os fluxos de dados, os requisitos atendidos, os riscos e um plano de testes. O diagrama mostra de onde vêm os logs e para onde vão; os fluxos de dados dão formatos e volumes; os requisitos atendidos remetem ao enunciado; os riscos dizem o que pode dar errado; o plano de testes mostra como o projeto será comprovado. Um revisor que não assistiu à apresentação deve entender o projeto só pelo documento. A equipe de Amara limita o documento a seis páginas. Os apêndices guardam os detalhes.

### 25.7 Trabalho em equipe

Os papéis se revezam: apresentador, relator, crítico. Todos explicam todas as partes. Revezar os papéis impede que um membro confiante apresente tudo enquanto os outros ficam calados. O relator registra decisões e críticas; o crítico procura fraquezas antes que pessoas de fora o façam. Exigir que todos expliquem todas as partes significa que os professores podem questionar qualquer membro, o que revela se o entendimento é compartilhado ou está nas mãos de uma única pessoa. No fim, cada membro escreve uma nota curta sobre o que contribuiu e o que aprendeu com outro membro, que os professores leem junto com o projeto da equipe.

### Privacidade no projeto

Os dispositivos dos depósitos são usados por motoristas e funcionários do armazém. O projeto registra apenas metadados das conexões, não o conteúdo, e os guarda por 30 dias, o que o responsável pela privacidade revisa e aprova. As equipes incluem essas revisões no plano, em vez de acrescentá-las no fim.

### Exemplo resolvido

O projeto final da equipe: restringir o tráfego entre depósitos e negócio a cinco serviços necessários, registrar todas as tentativas negadas, alertar quando um dispositivo de depósito tentar um destino novo mais de três vezes numa hora e revisar semanalmente. Custo estimado: apenas tempo de configuração. Risco principal: falha da alimentação de logs do *firewall*, coberta por monitoramento de *heartbeat*.

> **Caso sintético.** O ateliê e os projetos são inventados.

### Erros e limites

Os projetos do ateliê não foram testados; o laboratório do capítulo 30 os verifica.

### Exercícios

- **EX073 — Três opções.** Liste as três opções de monitoramento dos depósitos consideradas. *Rubrica:* 3 = monitoramento de fluxos, sensor de rede, aperto do *firewall* com registro; 2 = duas; 1 = uma; 0 = nada.
- **EX074 — Resultado da crítica.** O que a crítica mudou no projeto? *Rubrica:* 3 = uso dos logs existentes do *firewall*; mais barato que um sensor novo; 2 = parcial; 1 = vago; 0 = nada.
- **EX075 — Projeto final.** Resuma o projeto final e seu risco principal. *Rubrica:* 3 = 5 serviços permitidos, negações registradas, alerta para destinos novos repetidos, revisão semanal; risco de falha da alimentação; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Os ateliês ensinam projeto por meio de alternativas, critérios e crítica; o bom projeto mais barato muitas vezes reaproveita o que já existe.

### Continue estudando — capítulo 25 de 50

[← Capítulo 24 (rascunho)](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 (rascunho) →](#ch-26)

<a id="ch-26"></a>

## Capítulo 26 — Operações de segurança e blue team: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar modelos de arquitetura de SOC, como centralizado, distribuído e híbrido; (2) avaliar opções de SIEM, de *data lake* e de serviço gerenciado; (3) pesar decisões de construir ou comprar; (4) documentar as decisões de arquitetura com seus motivos.

### 26.1 Modelos de SOC

Zimmerman (2014) e Knerler, Parker e Zimmerman (2022) descrevem estruturas de SOC que vão de pequenas equipes centralizadas a modelos em níveis, distribuídos e federados. A Lindqvist, com uma sede e quarenta depósitos, mantém um pequeno SOC central, com a equipe de TI dos depósitos como contatos locais. A estrutura acompanha o tamanho e a dispersão. Um modelo em níveis com muitos especialistas convém a uma organização grande; um modelo federado convém a uma com unidades de negócio independentes. Os quarenta depósitos da Lindqvist são numerosos demais para a equipe central visitá-los, mas pequenos demais para terem os próprios analistas, então os contatos de TI dos depósitos atuam como olhos e mãos no local quando necessário.

### 26.2 Opções de plataforma de dados

Um SIEM tradicional indexa eventos para busca rápida e regras embutidas. Uma abordagem de *data lake* armazena barato e consulta com flexibilidade, mas exige mais engenharia. Muitos SOCs combinam os dois: SIEM quente para dados recentes e de alto valor e um *lake* para dados volumosos e de longo prazo. A indexação de um SIEM torna as buscas rápidas, mas custa armazenamento e licenças cobradas por volume. Um *lake* guarda dados brutos com baixo custo, mas busca mais devagar e exige engenheiros para construir consultas e *pipelines*. Combinar os dois põe os dados onde seu uso justifica o custo: logs de autenticação recentes no SIEM, meses de logs de *firewall* no *lake*.

### 26.3 Serviços gerenciados

Um provedor de detecção gerenciada pode vigiar à noite e trazer um conhecimento de ameaças mais amplo, mas conhece menos o contexto local e exige acordos de escalonamento claros. A Lindqvist considera usar um para a cobertura noturna. A cobertura noturna por um provedor pode sair mais barata do que um turno da noite interno completo. Os riscos são o provedor escalonar demais ou de menos, ou não ter contexto para julgar os alertas. Acordos claros declaram quais alertas o provedor trata, o que ele pode fazer por conta própria e com que rapidez precisa chamar o engenheiro de plantão da Lindqvist.

### 26.4 Construir ou comprar

Construir dá controle e aderência; comprar dá rapidez e suporte. Os engenheiros estimam o custo total ao longo de vários anos, incluindo o tempo da equipe, e não apenas o preço da licença. Uma ferramenta construída se encaixa exatamente, mas precisa de pessoas para mantê-la depois que seus autores seguem adiante. Uma ferramenta comprada vem com atualizações e suporte, mas pode obrigar os processos a se ajustarem ao seu desenho. Comparar os custos em cinco anos, incluindo as horas da equipe para integração e manutenção, muitas vezes muda o quadro em relação ao preço da licença sozinho. A comparação da Lindqvist para seu sistema de casos mostra que uma licença mais barata custaria mais em trabalho de integração em dois anos, o que decide a escolha.

### 26.5 Registros de decisão

Cada escolha importante é escrita como um registro de decisão de arquitetura: contexto, opções, decisão, consequências. Futuros engenheiros conseguem ver por que as coisas são como são. Os registros são curtos, muitas vezes de uma página, e escritos no momento da decisão. As consequências incluem benefícios e custos, como a dependência de um formato do fornecedor. Quando uma equipe posterior se perguntar por que o *lake* usa um formato específico, o registro explica o raciocínio e as opções rejeitadas, poupando-a de repetir a análise. A Lindqvist os guarda junto do código.

### 26.6 Reversibilidade

Prefira escolhas que possam ser desfeitas. Manter os logs brutos num formato aberto torna possível trocar de plataforma mais tarde. Algumas escolhas são difíceis de reverter: dados guardados apenas num formato proprietário podem exigir uma conversão cara para serem movidos. Manter os logs brutos em formatos abertos, como linhas JSON, ao lado da cópia da própria plataforma preserva as opções. Escolhas reversíveis permitem a uma equipe andar mais depressa, já que um erro pode ser corrigido sem um grande projeto. Os termos do contrato também contam: um prazo inicial curto com um fornecedor é mais fácil de deixar do que um compromisso de cinco anos assinado em troca de desconto.

### 26.7 Caso

Com o armazenamento crescendo (capítulo 6), a Lindqvist precisa decidir se expande o SIEM ou acrescenta um *lake* para os logs de *firewall* e de DNS. Expandir o SIEM mantém tudo num só lugar, mas custa mais à medida que o volume cresce. Acrescentar um *lake* para os logs de *firewall* e de DNS, que são volumosos, mas pesquisados com menos frequência, mantém o SIEM para os dados de alto valor. Amara prepara a comparação com estimativas de custo em cinco anos e o efeito sobre a velocidade de investigação para cada tipo de log. A decisão vai ao CISO com uma recomendação e é registrada como registro de decisão.

### Exemplo resolvido

O registro de decisão de Amara recomenda manter os dados do portal, de identidade e de *endpoint* no SIEM por 90 dias e enviar os logs de *firewall* e de DNS para um *lake* depois de 14 dias, com buscas no *lake* para as investigações. Consequência anotada: as consultas ao *lake* levam minutos, não segundos, então os *playbooks* de caça precisam levar isso em conta.

> **Caso sintético.** As opções e as decisões são inventadas.

### Erros e limites

As alegações dos fornecedores sobre escala e custo precisam ser testadas com seus próprios dados.

### Exercícios

- **EX076 — Plataforma híbrida.** Explique a abordagem híbrida de SIEM mais *lake*. *Rubrica:* 3 = SIEM quente para dados recentes de alto valor, *lake* para volume/longo prazo; 2 = parcial; 1 = só um; 0 = nada.
- **EX077 — Cobertura noturna gerenciada.** Cite um benefício e um risco de um provedor gerenciado para as noites. *Rubrica:* 3 = cobertura e conhecimento mais amplo vs menos contexto local, acordos de escalonamento; 2 = um lado; 1 = vago; 0 = nada.
- **EX078 — Registro de decisão.** Que seções compõem um registro de decisão de arquitetura? *Rubrica:* 3 = contexto, opções, decisão, consequências; 2 = três; 1 = uma; 0 = nada.

### Síntese

Compare estruturas de SOC e plataformas de dados pelo custo total, pela aderência e pela reversibilidade, e registre por que as decisões foram tomadas.

### Continue estudando — capítulo 26 de 50

[← Capítulo 25 (rascunho)](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 (rascunho) →](#ch-27)

<a id="ch-27"></a>

## Capítulo 27 — Operações de segurança e blue team: projeto de controles

### Objetivos de aprendizagem

Você vai (1) projetar controles de detecção e de resposta com gatilhos e ações definidos; (2) especificar *playbooks* para alertas comuns; (3) projetar salvaguardas contra ações automatizadas nocivas; (4) mapear os controles às técnicas do D3FEND.

### 27.1 Controles de detecção e de resposta

Um controle de detecção encontra a atividade; um controle de resposta age sobre ela. Para a tomada de conta no portal, a detecção é a regra de possível tomada de conta; a resposta é bloquear a conta, invalidar as sessões e contatar o cliente. Cada um precisa do outro. Uma detecção sem resposta planejada deixa os analistas inseguros sobre o que fazer às 3 da manhã, enquanto uma resposta sem detecção confiável ou nunca é acionada ou é acionada nas contas erradas. Projetá-los juntos permite a Amara casar a força da evidência com a força da ação: uma tomada de conta provável justifica invalidar as sessões, enquanto uma mera tentativa não justifica deixar o cliente sem acesso.

### 27.2 *Playbooks*

Um *playbook* lista os passos que um analista segue para um tipo de alerta: verificar, delimitar, conter, notificar, registrar. Ele nomeia os dados a conferir e os pontos de decisão. O NIST SP 800-61r3 situa essas atividades de resposta no ciclo mais amplo de gestão de riscos. Os pontos de decisão são onde o *playbook* pede ao analista que julgue, em vez de seguir: o sucesso veio do dispositivo habitual do cliente? O endereço já foi alterado? Nomear os dados a conferir em cada ponto impede os analistas de pularem evidências sob pressão. O *playbook* também diz quando parar e escalonar, para que os analistas conheçam os limites de sua própria autoridade durante um incidente.

### 27.3 Ações automatizadas

Alguns passos podem ser automatizados: invalidar uma sessão é rápido e de baixo risco. Outros, como bloquear uma faixa de rede, podem prejudicar usuários legítimos e exigem uma decisão humana. Invalidar uma sessão força um novo login; se o cliente for legítimo, ele simplesmente entra de novo, então uma decisão errada custa pouco. Bloquear uma faixa de rede poderia cortar uma operadora móvel que atende milhares de clientes, então uma decisão errada custa muito. Amara classifica cada ação candidata pelo custo de errar e automatiza apenas aquelas em que um erro é barato e fácil de reverter.

### 27.4 Salvaguardas

A automação precisa de limites: número máximo de ações por hora, exclusões para contas críticas e alertas automáticos se os limites forem atingidos. Uma automação descontrolada pode deixar milhares de clientes sem acesso. Um defeito numa regra ou uma enxurrada de eventos de teste sintéticos poderia acionar a automação milhares de vezes em minutos. Um teto de ações por hora transforma um possível desastre num problema contido. Contas críticas, como as usadas pelos sistemas dos depósitos, ficam excluídas porque bloqueá-las pararia as entregas. Atingir um limite pausa a automação e aciona um engenheiro, que decide se ela continua.

### 27.5 Mapeamento ao D3FEND

O D3FEND nomeia técnicas defensivas como a limiarização de eventos de autenticação e o bloqueio de contas. Mapear os controles a ele esclarece o que cada controle de fato faz e ajuda a encontrar lacunas. Os nomes de produtos e os termos de *marketing* variam, o que dificulta saber se duas ferramentas se sobrepõem ou deixam lacunas. O D3FEND oferece um vocabulário comum que descreve o que um controle faz com a atividade do adversário. Mapear os controles do portal da Lindqvist mostra que a limiarização e o bloqueio de contas estão presentes, enquanto nada ainda analisa o comportamento da sessão depois do login, o que sugere onde investir em seguida.

### 27.6 Testando os controles

Cada controle é testado com eventos sintéticos seguros, e os *playbooks* de resposta são ensaiados em exercícios. Os eventos sintéticos verificam se a detecção dispara e se a automação age dentro de seus limites. Os exercícios verificam as partes humanas: o analista encontra o *playbook*, o atendimento ao cliente sabe o que dizer a um cliente bloqueado, o contato de escalonamento atende? Os exercícios muitas vezes revelam pequenos problemas, como um número de telefone desatualizado, que nenhum teste técnico pegaria. As constatações de cada exercício são registradas com um responsável e uma data para a correção.

### 27.7 Caso

Amara projeta o *playbook* de possível tomada de conta com Paolo e com a gerente de atendimento ao cliente. Envolver o atendimento ao cliente cedo importa porque é ele que vai falar com os clientes cujas contas foram bloqueadas. A gerente pede um roteiro curto explicando por que o acesso foi redefinido e como recuperá-lo, e um campo no alerta mostrando se o cliente já foi contatado. Os dois pedidos entram no *playbook* antes de ele ser testado. O *playbook* pronto é ensaiado uma vez com um alerta sintético antes da entrada em produção, com a gerente de atendimento fazendo o papel do cliente.

### Experiência do cliente

Os controles de resposta tocam os clientes. A mensagem de suspensão no portal explica que a conta está pausada por segurança e dá o número do suporte, para que os clientes legítimos não fiquem confusos.

### Exemplo resolvido

O *playbook* automatiza a invalidação de sessões e uma suspensão temporária da conta, com teto de 20 contas por hora; acima disso, a automação pausa e aciona o engenheiro de plantão. Um analista confirma em até 30 minutos, contata o cliente pelo telefone cadastrado e registra o resultado.

> **Caso sintético.** O *playbook* é inventado.

### Erros e limites

Os *playbooks* envelhecem à medida que os sistemas mudam; revise-os após cada uso.

### Exercícios

- **EX079 — Detecção versus resposta.** Dê um controle de detecção e um de resposta para a tomada de conta no portal. *Rubrica:* 3 = regra de possível tomada de conta; bloquear a conta/invalidar sessões; 2 = um; 1 = confuso; 0 = nada.
- **EX080 — Salvaguarda da automação.** Que salvaguarda limita a suspensão automatizada? *Rubrica:* 3 = teto de 20 contas/hora; pausar e acionar acima dele; 2 = parcial; 1 = vago; 0 = nada.
- **EX081 — Decisão humana.** Por que o bloqueio de faixas de rede deve exigir uma pessoa? *Rubrica:* 3 = pode prejudicar usuários legítimos; exige julgamento; 2 = parcial; 1 = velocidade; 0 = nada.

### Síntese

Projete os controles como detecção mais resposta, automatize os passos de baixo risco com limites e mapeie os controles a técnicas defensivas nomeadas.

### Continue estudando — capítulo 27 de 50

[← Capítulo 26 (rascunho)](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 (rascunho) →](#ch-28)

<a id="ch-28"></a>

## Capítulo 28 — Operações de segurança e blue team: implementação I

### Objetivos de aprendizagem

Você vai (1) implementar uma detecção e as mudanças correspondentes no *pipeline*; (2) usar ambientes em etapas; (3) gerenciar a configuração como código; (4) registrar a evidência da implementação.

### 28.1 Do projeto à construção

A implementação transforma o R-07 e o *playbook* em peças funcionando: o encaminhamento dos logs do balanceador de carga, as atualizações do analisador, a regra, o roteamento dos alertas e a automação. R-07 é o identificador do requisito de detecção de possível tomada de conta, e manter esse rótulo ao longo da implementação permite que cada componente remeta ao motivo de sua existência. Construir as peças na ordem das dependências importa: a regra não pode ser testada até que o analisador produza os campos de que ela precisa, e o roteamento não pode ser conferido até que a regra crie alertas. Amara elabora um plano de construção curto com essa ordem.

### 28.2 Ambientes

As mudanças vão primeiro para um SIEM de teste com dados sintéticos reproduzidos, depois para a produção em modo só monitoramento e depois para o alerta. Cada etapa tem critérios de entrada e de saída. Os critérios de entrada dizem o que precisa ser verdade antes de uma mudança entrar numa etapa, como passar nos testes unitários. Os critérios de saída dizem o que precisa ser mostrado antes de ela sair, como uma semana em modo só monitoramento com alertas falsos abaixo do limite. Pular etapas poupa dias, mas arrisca descobrir problemas em produção, onde eles afetam analistas e clientes.

### 28.3 Configuração como código

As configurações dos analisadores, as regras e o roteamento ficam no controle de versão e são implantados por um *pipeline*, e não editados à mão em consoles. Isso torna as mudanças revisáveis e reversíveis. Edições manuais num console não deixam registro claro de quem mudou o quê e por quê, e são fáceis de fazer por engano. Um *pipeline* aplica a mesma configuração revisada todas as vezes. Se uma mudança causar problemas, reverter o *commit* e reimplantar restaura o estado anterior em minutos, com um registro completo do que aconteceu.

### 28.4 Atualizações do analisador

Os logs do balanceador de carga usam um formato novo. Amara escreve um analisador, testa-o com 1.000 linhas de amostra e verifica se cada campo se mapeia para o modelo de eventos. As mil linhas incluem requisições normais, falhas, caracteres incomuns em nomes de usuário e algumas linhas malformadas. Amara conta quantas linhas são analisadas por completo, quantas em parte e quantas falham, e confere uma amostra à mão contra o texto bruto. Campos como o endereço do cliente precisam se mapear para o campo de origem do modelo de eventos, ou a regra vai agrupar os valores errados.

### 28.5 Gestão de mudanças

As mudanças em produção seguem o processo de mudanças da Lindqvist: um chamado, uma revisão, uma janela e um plano de reversão. O chamado descreve a mudança e seu propósito; a revisão confere o risco; a janela escolhe um horário em que os problemas afetem o menor número de pessoas; a reversão diz exatamente como desfazê-la. As mudanças de detecção às vezes são tratadas como de baixo risco, mas uma mudança de analisador pode quebrar muitas regras de uma vez, por isso elas seguem o mesmo processo das outras mudanças em produção. O primeiro chamado de Amara é revisado por Paolo e pelo administrador do SIEM.

### 28.6 Evidência

Os registros da implementação incluem *commits*, resultados de testes, chamados de mudança e capturas de tela dos resultados em modo só monitoramento. Auditores e futuros engenheiros os usam. Meses depois, alguém pode perguntar quando a regra entrou em produção e se foi testada. Os *commits* respondem o que mudou; os resultados de testes, se funcionou; os chamados, quem aprovou; os resultados em modo só monitoramento, como ela se comportou com dados reais antes de alertar. Manter tudo isso junto poupa tempo em auditorias e em revisões de incidentes. Amara liga os quatro a partir da linha do requisito na tabela de rastreabilidade, para que a trilha comece no R-07.

### 28.7 Trabalho em par

Amara trabalha em par com um analista durante a configuração do roteamento, para que os alertas caiam onde os analistas esperam. Os engenheiros pensam em termos de regras e filas; os analistas, em termos de turnos e cargas de trabalho. O analista aponta que os alertas roteados para uma fila geral seriam perdidos à noite, quando só a fila do plantão é observada. O trabalho em par pega esse tipo de descompasso antes da implantação e dá ao analista um senso de responsabilidade pelos novos alertas. Eles terminam com um alerta de teste que o analista abre na tela do plantão.

### Ensaio da reversão

Antes da mudança em produção, Amara ensaia a reversão no SIEM de teste: implanta o novo analisador, depois restaura a versão anterior a partir do controle de versão e verifica se a análise volta ao comportamento antigo. Uma reversão nunca praticada é uma esperança, não um plano. O ensaio leva dez minutos e é registrado no chamado de mudança.

### Exemplo resolvido

Durante a etapa de teste, 12 de 1.000 linhas de amostra falham na análise: contêm um campo extra acrescentado por uma atualização do balanceador. Amara amplia o analisador, acrescenta as 12 linhas como casos de teste e roda de novo: as 1.000 são analisadas sem erros. Só então ela pede a mudança em produção.

> **Caso sintético.** As linhas e as contagens são inventadas.

### Erros e limites

Os dados de teste podem não incluir todas as variantes de produção; monitore os erros de análise depois da liberação.

### Exercícios

- **EX082 — Etapas.** Descreva as três etapas da implementação. *Rubrica:* 3 = SIEM de teste com reprodução, produção em só monitoramento, alerta; 2 = duas; 1 = uma; 0 = nada.
- **EX083 — Falhas de análise.** O que causou as 12 falhas de análise, e como foram tratadas? *Rubrica:* 3 = campo extra de uma atualização do balanceador; analisador ampliado, linhas acrescentadas como testes; 2 = parcial; 1 = ignoradas; 0 = nada.
- **EX084 — Configuração como código.** Por que implantar a configuração a partir do controle de versão? *Rubrica:* 3 = revisável, reversível, consistente; 2 = parcial; 1 = estilo; 0 = nada.

### Síntese

Implemente por meio de ambientes em etapas, configuração sob controle de versão e evidência registrada.

### Continue estudando — capítulo 28 de 50

[← Capítulo 27 (rascunho)](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 (rascunho) →](#ch-29)

<a id="ch-29"></a>

## Capítulo 29 — Operações de segurança e blue team: medição

### Objetivos de aprendizagem

Você vai (1) definir métricas de SOC ligadas a objetivos; (2) calcular resumos robustos dos tempos de resposta; (3) evitar métricas que distorcem o comportamento; (4) apresentar as medições com contexto.

### 29.1 Por que medir

Knerler, Parker e Zimmerman (2022) tratam a medição como uma estratégia: "meça o desempenho para melhorar o desempenho". As métricas mostram se as mudanças ajudam e para onde o esforço deve ir. Sem medição, um SOC não consegue saber se uma nova regra reduziu o dano ou só acrescentou ruído, nem se uma mudança na equipe ajudou. As medidas também sustentam conversas honestas com a direção sobre o que a equipe consegue entregar. O objetivo é a melhoria, não julgar indivíduos, o que afeta como as métricas são escolhidas e compartilhadas. A Lindqvist começa com um punhado de medidas e só acrescenta outras quando há uma pergunta clara a responder.

### 29.2 Escolhendo métricas

Boas métricas de SOC se ligam a objetivos: tempo da detecção ao reconhecimento, fração de incidentes detectados internamente em vez de relatados por clientes, cobertura das técnicas prioritárias e taxas de alertas falsos por regra. Cada métrica deve responder a uma pergunta que alguém de fato faz. O tempo até o reconhecimento diz ao CISO com que rapidez o SOC reage; a detecção interna versus a relatada por clientes mostra se o monitoramento encontra os problemas primeiro; a cobertura de técnicas mostra a amplitude; as taxas de alertas falsos por regra mostram onde é preciso ajustar. Coletar métricas que ninguém usa desperdiça esforço e polui os relatórios.

### Laboratório — resumos dos tempos de resposta

```python
"""Median and 90th percentile of detection-to-acknowledgement minutes (synthetic)."""
import statistics
minutes = [3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 11, 12, 14, 18, 41]
q = statistics.quantiles(minutes, n=10, method="inclusive")
print(f"n={len(minutes)} mean={statistics.mean(minutes):.1f} median={statistics.median(minutes)} p90={q[8]:.1f}")
```

Execute com `python3 lab_latency.py`. Saída verificada:

```text
n=15 mean=10.2 median=7 p90=16.4
```

### 29.3 Lendo o resultado

Quinze tempos de reconhecimento dão uma média de 10,2 minutos, mas uma mediana de 7 e um percentil 90 de 16,4. Um único caso de 41 minutos puxa a média para cima. A mediana descreve o caso típico; o percentil 90, a cauda lenta que importa para o requisito de 15 minutos. Relatar só a média sugeriria que a equipe costuma levar dez minutos, quando a maioria dos reconhecimentos acontece em cerca de sete. Relatar só a mediana esconderia que um décimo dos casos leva mais de dezesseis minutos, além do requisito. Amara examina o caso de 41 minutos separadamente e descobre que ele chegou durante uma passagem de turno, o que aponta para uma correção de processo.

### 29.4 Métricas que distorcem

Kokulu et al. (2019) constataram que desalinhamentos de métricas são comuns nos SOCs. Recompensar o fechamento rápido pode produzir fechamento descuidado. Combine as métricas de velocidade com verificações de qualidade, como amostras revisadas de alertas fechados. Quando um número vira meta, as pessoas encontram formas de movê-lo que não refletem melhoria real. Se os analistas são julgados por alertas fechados por hora, fechamentos rápidos sem investigação se tornam racionais. Usar várias métricas juntas torna qualquer uma delas mais difícil de manipular. A amostra de alertas fechados é sorteada a cada semana, para que os analistas não consigam prever quais fechamentos serão revisados.

### 29.5 Contexto

Uma métrica sem contexto engana: o tempo de reconhecimento subiu no mês passado porque a equipe noturna diminuiu, e não porque os analistas ficaram mais lentos. Os relatórios incluem essas explicações. Um gráfico mostrando reconhecimentos mais lentos poderia levar os gestores a culpar os analistas ou exigir horas extras. Com a explicação de que a equipe noturna caiu de dois para um, a conversa passa para as decisões de pessoal. Amara acrescenta ao relatório mensal uma coluna curta de observações para eventos como mudanças de equipe, incidentes e novas regras. Os relatórios comparam cada mês com o mesmo mês do ano anterior quando há padrões sazonais.

### 29.6 Qualidade dos dados

As métricas dependem dos carimbos de tempo do sistema de casos; analistas que reconhecem tarde na ferramenta, mas agem cedo, tornam os dados errados. Treinamento e ferramentas corrigem isso. Se os analistas começam a investigar a partir de uma notificação por e-mail e só clicam em reconhecer depois, o sistema de casos registra um tempo mais lento do que o real. A métrica então engana no sentido oposto. Tornar o reconhecimento automático quando o analista abre o alerta, e treinar a equipe sobre por que os carimbos de tempo importam, alinha os dados com o que de fato aconteceu. Amara confere uma amostra de casos contra os logs de *chat*.

### Métricas de cobertura

A cobertura das técnicas prioritárias do ATT&CK é medida como a fração que tem pelo menos uma detecção testada. Detecções não testadas não contam, porque uma regra que nunca disparou num evento de teste seguro pode não funcionar. A Lindqvist relata essa fração a cada trimestre, com a lista de lacunas anexada, para que o número não possa esconder quais técnicas faltam.

### Exemplo resolvido

Amara relata: "Mediana de reconhecimento de 7 minutos, percentil 90 de 16,4 contra uma meta de 15 minutos. O caso mais lento (41 minutos) ocorreu durante uma passagem de turno; propomos sobrepor as passagens de turno em 15 minutos."

> **Caso sintético.** Os tempos vêm do script do laboratório.

### Erros e limites

Quinze valores são poucos; percentis de amostras pequenas são instáveis.

### Exercícios

- **EX085 — Resumos do laboratório.** Informe a média, a mediana e o percentil 90. *Rubrica:* 3 = 10,2, 7, 16,4; 2 = dois; 1 = um; 0 = nada.
- **EX086 — Por que a mediana.** Por que descrever o reconhecimento com mediana e percentil, e não com a média? *Rubrica:* 3 = assimétrico; o valor atípico puxa a média; a cauda importa para a meta; 2 = parcial; 1 = a média serve; 0 = nada.
- **EX087 — Proteção contra distorção.** Como evitar que uma métrica de velocidade cause fechamentos descuidados? *Rubrica:* 3 = combiná-la com verificações de qualidade por revisão de alertas fechados; 2 = parcial; 1 = eliminar métricas; 0 = nada.

### Síntese

Meça o que se liga aos objetivos, resuma de forma robusta, proteja-se contra a distorção e sempre relate o contexto.

### Continue estudando — capítulo 29 de 50

[← Capítulo 28 (rascunho)](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 (rascunho) →](#ch-30)

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) verificar a lógica de detecção com testes unitários automatizados; (2) verificar o comportamento do *pipeline* com eventos sintéticos seguros; (3) registrar a evidência de verificação; (4) distinguir verificação de validação.

### 30.1 Verificação versus validação

A verificação pergunta "construímos certo?" — a regra se comporta como especificado? A validação pergunta "construímos a coisa certa?" — ela ajuda a detectar ameaças reais em operação? Este laboratório se concentra na verificação. Uma regra pode passar em todos os testes de verificação e ainda assim ser inútil, se mirar um comportamento que os atacantes não usam ou se os ataques reais forem diferentes dos dados de teste. A validação responde a essa pergunta mais tarde, com evidência operacional. Manter as duas separadas impede que uma equipe afirme que uma regra "funciona" quando só mostrou que ela corresponde à sua especificação.

### 30.2 O laboratório

O laboratório é um SIEM de teste isolado da produção, com logs sintéticos reproduzidos. Não se usam dados reais de clientes nem ferramentas de ataque; os eventos de teste são registros de log fabricados que se parecem com o comportamento que a regra mira. O isolamento impede que os eventos de teste cheguem aos analistas de produção e desperdicem seu tempo. Os logs sintéticos reproduzidos dão volume e variedade realistas sem expor dados de clientes. Os registros fabricados permitem ao testador controlar exatamente quais condições estão presentes, e é assim que os casos de fronteira são testados com precisão. O laboratório é reconstruído a partir da configuração, para que seu estado seja conhecido antes de cada execução.

### Laboratório — testes unitários da regra de rajada

```python
"""Unit tests for a detection function, run with the standard library (synthetic cases)."""
import io, unittest
def burst(users_failed, any_success, threshold=5):
    return users_failed >= threshold and any_success
class T(unittest.TestCase):
    def test_fires_at_threshold(self): self.assertTrue(burst(5, True))
    def test_quiet_below(self): self.assertFalse(burst(4, True))
    def test_needs_success(self): self.assertFalse(burst(9, False))
    def test_zero(self): self.assertFalse(burst(0, False))
if __name__ == "__main__":
    r = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(unittest.defaultTestLoader.loadTestsFromTestCase(T))
    print("tests run", r.testsRun, "failures", len(r.failures))
```

Execute com `python3 lab_unittest.py`. Saída verificada:

```text
tests run 4 failures 0
```

### 30.3 Lendo o resultado

Quatro testes rodam e nenhum falha: a regra dispara com exatamente 5 usuários distintos falhando e um sucesso, fica em silêncio com 4, fica em silêncio sem um sucesso mesmo com 9 usuários e fica em silêncio sem atividade. Esses testes codificam a fronteira e a cláusula de sucesso decididas nos capítulos 9 e 24. Cada teste confere um aspecto do comportamento. Disparar com cinco e ficar em silêncio com quatro fixa o limiar com exatidão; ficar em silêncio com nove sem um sucesso mostra que a cláusula de sucesso é de fato exigida; ficar em silêncio sem atividade mostra que a regra não dispara por engano em janelas vazias. Juntos, os quatro testes aprovados descrevem o comportamento pretendido da regra.

### 30.4 Testes do *pipeline*

Os testes unitários conferem a lógica; os testes do *pipeline* conferem se um registro sintético que entra no coletor produz um alerta no sistema de casos com os campos corretos. Amara injeta três registros e confere cada campo do alerta resultante. Uma regra pode estar correta enquanto o *pipeline* em volta dela quebra: um campo renomeado pelo analisador, uma regra de roteamento que envia os alertas para a fila errada ou um erro de conversão de horário. Conferir cada campo do alerta final, como o ID do cliente, a rede de origem e as ações subsequentes, confirma que a cadeia inteira funciona, e não só a lógica da regra.

### 30.5 Evidência

O registro do laboratório lista o teste, a versão, a entrada, os resultados esperado e obtido, a data e o testador. Registrar a versão da regra liga cada resultado a uma configuração exata, para que uma mudança posterior possa ser comparada. Os resultados esperado e obtido lado a lado tornam as falhas evidentes. O nome do testador e a data mostram quem responde pelo teste. Esses registros passam a fazer parte da evidência de que a regra foi verificada antes de entrar em produção. Os testes que falharam continuam no registro depois de corrigidos, ao lado da nova execução, para que o histórico mostre o que deu errado e como foi corrigido.

### 30.6 Repetibilidade

Os testes rodam automaticamente a cada mudança de regra, de modo que a verificação é contínua, e não pontual. As regras mudam com frequência por ajustes, atualizações de analisadores e renomeações de campos. Um teste rodado só uma vez, na criação, não diz nada sobre a regra seis meses depois. Rodar a bateria a cada mudança pega regressões de imediato, e um teste que falha bloqueia a implantação até que alguém corrija a regra ou justifique a mudança do teste. A bateria leva menos de dois minutos, então os engenheiros a rodam localmente antes de propor uma mudança, e o *pipeline* compartilhado a roda de novo antes da incorporação.

### Higiene dos dados de teste

Os registros de teste sintéticos trazem um campo marcador, para que nunca se misturem com alertas ou métricas reais.

### Exemplo resolvido

O teste do *pipeline* revela que o alerta não traz o ID do cliente: o modelo de roteamento fazia referência a um nome de campo antigo. Amara corrige o modelo, roda de novo e registra tanto a falha quanto a correção. Só os testes unitários jamais teriam encontrado isso.

> **Caso sintético.** Os testes e os registros são sintéticos.

### Erros e limites

Passar na verificação não mostra que a regra pega atacantes reais; isso é validação, tratada no capítulo 38.

### Exercícios

- **EX088 — V e V.** Distinga verificação de validação. *Rubrica:* 3 = construir certo vs construir a coisa certa; especificação vs eficácia real; 2 = parcial; 1 = são iguais; 0 = nada.
- **EX089 — Quatro testes.** O que os quatro testes unitários conferem? *Rubrica:* 3 = fronteira do limiar 5/4, cláusula de sucesso, entrada vazia; 2 = três; 1 = um; 0 = nada.
- **EX090 — Constatação do *pipeline*.** O que o teste do *pipeline* pegou que os testes unitários não conseguiam? *Rubrica:* 3 = ID do cliente ausente por causa do nome de campo no modelo; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Verifique a lógica com testes unitários e o *pipeline* inteiro com eventos sintéticos seguros, registrando cada resultado.

### Continue estudando — capítulo 30 de 50

[← Capítulo 29 (rascunho)](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 (rascunho) →](#ch-31)

<a id="ch-31"></a>

## Capítulo 31 — Operações de segurança e blue team: implementação II

### Objetivos de aprendizagem

Você vai (1) implementar o monitoramento das redes dos depósitos a partir do projeto do ateliê; (2) integrar os logs do *firewall* e a política de lista de permissões; (3) implementar o enriquecimento dos ativos dos depósitos; (4) gerenciar a implantação em muitos locais.

### 31.1 Do ateliê à produção

O projeto dos depósitos do capítulo 25 agora se torna real: restringir o tráfego entre depósitos e negócio a cinco serviços, registrar as negações e alertar sobre tentativas repetidas a destinos novos. Cinco serviços cobrem o que os depósitos legitimamente precisam dos sistemas de negócio, como atualizações de entrega e consultas de estoque. Todo o resto é negado e registrado. Alertar sobre tentativas repetidas a destinos novos filtra erros pontuais e ainda pega um dispositivo que tenta com insistência alcançar sistemas que não deveria, que é o comportamento que o projeto pretendia revelar.

### 31.2 Enriquecimento dos ativos

A detecção precisa saber quais endereços são de depósitos. Amara trabalha com a TI para acrescentar as sub-redes e os tipos de dispositivo dos depósitos ao inventário de ativos e, depois, às tabelas de enriquecimento. Sem enriquecimento, um log de negação mostra apenas um endereço, e um analista precisa procurar a que depósito e dispositivo ele pertence. Com as sub-redes e os tipos de dispositivo dos depósitos no inventário, os alertas chegam mostrando de imediato "leitor portátil, Depósito 14". O trabalho no inventário também ajuda as operações de TI, que antes não tinham uma lista completa dos dispositivos dos depósitos.

### 31.3 Implantação em fases

Quarenta depósitos não podem mudar de uma vez. Três depósitos-piloto vão primeiro; os problemas encontrados ali são corrigidos antes que os demais sigam em grupos de dez. Os três depósitos-piloto são escolhidos para cobrir tamanhos e equipamentos diferentes, de modo que problemas que afetam só alguns tipos de depósito tendam a aparecer. Grupos de dez depois disso mantêm administrável o número de depósitos afetados por qualquer problema novo. Cada grupo só começa depois que o anterior rodou sem problemas por um período definido. As lições são registradas depois de cada grupo.

### 31.4 Constatações do piloto

No piloto, uma impressora de etiquetas num depósito precisa alcançar um servidor de impressão que não está na lista de permissões. O *firewall* a bloqueia, a impressão para e o depósito liga para a TI. A equipe acrescenta o serviço de impressão, documenta o porquê e confere os outros depósitos em busca das mesmas impressoras antes do grupo seguinte. O problema da impressora mostra por que a lista de permissões precisa de contribuições de quem conhece as operações dos depósitos, e não só dos diagramas de rede. Conferir os outros depósitos antes do grupo seguinte evita a mesma interrupção em outros lugares. Documentar por que o serviço de impressão foi acrescentado mantém a lista de permissões compreensível, para que futuros revisores não o removam como uma exceção sem explicação.

### 31.5 Coordenação

Os gerentes dos depósitos recebem um aviso antes das mudanças, um número de contato e uma promessa de reversão. Os gerentes dos depósitos tocam locais movimentados, onde uma interrupção sem explicação pode atrasar entregas. Um aviso antecipado lhes permite planejar em torno da mudança; um número de contato lhes dá alguém para quem ligar; uma promessa de reversão os tranquiliza de que um problema será revertido rapidamente, em vez de debatido. Uma boa coordenação facilita as implantações seguintes, porque a confiança foi construída. Depois, pergunta-se aos gerentes como a mudança correu. Suas respostas moldam o aviso seguinte.

### 31.6 Monitorando a implantação

Um painel mostra as negações por depósito por hora; um pico depois de uma mudança sinaliza um serviço legítimo esquecido. Antes de uma mudança, as negações num depósito ficam perto de zero, porque o tráfego não era restrito. Uma alta brusca logo depois da mudança costuma significar que um serviço legítimo foi esquecido, como no caso da impressora. Acompanhar o painel durante cada janela de implantação permite à equipe reagir em minutos, em vez de esperar reclamações dos funcionários do depósito. Um pico fora de uma janela de implantação é tratado, em vez disso, como um possível evento de segurança.

### 31.7 Encerramento

Depois de todos os depósitos, a equipe revisa as taxas de negação e o volume de alertas em relação às estimativas do projeto. Comparar os resultados reais com as estimativas confere se as premissas do projeto se sustentaram. Se as negações forem muito maiores do que o esperado, a lista de permissões ainda pode estar sem alguns serviços; se os alertas forem muito maiores, os limiares podem precisar de ajuste. A revisão é registrada por escrito e ligada ao documento de projeto, fechando o ciclo do ateliê à operação. Paolo a lê antes de o projeto ser encerrado, e os números finais passam a ser a linha de base do monitoramento rotineiro do tráfego dos depósitos dali em diante.

### Documentando as exceções

Todo serviço permitido tem um responsável e um motivo no arquivo de política.

### Exemplo resolvido

Depois da implantação, as negações dos depósitos ficam em média em 40 por dia somando todos os locais, a maioria de dispositivos tentando de novo um servidor de atualização antigo. O alerta de destino novo dispara duas vezes na primeira semana; nas duas, é o *laptop* de um prestador de serviço conectado à rede de um depósito. O segundo leva a TI a impor o controle de acesso à rede para dispositivos visitantes.

> **Caso sintético.** Os depósitos, os dispositivos e as contagens são inventados.

### Erros e limites

Restringir o tráfego pode quebrar dependências desconhecidas; os pilotos reduzem esse risco, mas não o eliminam.

### Exercícios

- **EX091 — Implantação em fases.** Por que fazer o piloto primeiro em três depósitos? *Rubrica:* 3 = encontrar problemas como a dependência da impressora antes de um impacto mais amplo; 2 = parcial; 1 = velocidade; 0 = nada.
- **EX092 — Problema da impressora.** Como o problema da impressora foi tratado? *Rubrica:* 3 = serviço de impressão acrescentado, documentado, outros depósitos conferidos antes do grupo seguinte; 2 = parcial; 1 = restrição removida; 0 = nada.
- **EX093 — Alerta do prestador.** O que os alertas de destino novo revelaram, e o que veio depois? *Rubrica:* 3 = *laptop* de um prestador na rede do depósito; controle de acesso à rede imposto; 2 = parcial; 1 = alarmes falsos; 0 = nada.

### Síntese

Implemente mudanças em todos os locais com enriquecimento, pilotos, coordenação e monitoramento dos efeitos colaterais.

### Continue estudando — capítulo 31 de 50

[← Capítulo 30 (rascunho)](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 (rascunho) →](#ch-32)

<a id="ch-32"></a>

## Capítulo 32 — Operações de segurança e blue team: confiabilidade

### Objetivos de aprendizagem

Você vai (1) definir metas de confiabilidade para o *pipeline* de monitoramento; (2) identificar pontos únicos de falha; (3) projetar redundância e degradação controlada; (4) medir a disponibilidade e a completude dos dados.

### 32.1 Metas de confiabilidade

O *pipeline* tem como meta 99,5% de disponibilidade e 99,9% de completude das fontes prioritárias. A completude — a fração dos eventos esperados que chega — importa tanto quanto o tempo no ar, porque um *pipeline* funcionando com dados faltando ainda deixa o SOC às cegas. O tempo no ar sozinho engana: um *pipeline* pode estar rodando enquanto descarta em silêncio uma parte dos eventos. A completude mede o que de fato chega. Para fontes prioritárias, como os logs de autenticação, 99,9% significa no máximo um evento perdido em mil, o que mantém baixa a chance de perder o evento-chave de um ataque e ainda é alcançável com uma engenharia razoável.

### 32.2 Pontos únicos de falha

O *pipeline* da Lindqvist tem um coletor por local e uma única alimentação de logs do balanceador de carga. Se qualquer um falhar, uma fonte inteira desaparece. Um coletor por local significa que um defeito de *hardware* ali silencia todas as fontes daquele local até ser consertado. A alimentação única do balanceador de carga significa que a detecção de tomada de conta depende de um único caminho. Listar esses pontos é o primeiro passo; decidir quais eliminar depende do custo e das detecções que cada um sustenta. Amara lista os dois na análise de falhas, com as detecções que cada um sustenta, o que mostra que a alimentação carrega a detecção mais importante.

### 32.3 Redundância

Dois coletores por local, em modo ativo-passivo, e um segundo caminho de alimentação para os logs do balanceador eliminam os principais pontos únicos. A redundância custa dinheiro, então vai primeiro para onde o valor de detecção é maior. Ativo-passivo significa que um coletor trabalha enquanto o outro espera, assumindo se o primeiro falhar. Isso é mais simples do que dividir a carga entre os dois e evita eventos duplicados. Começar pelos locais e alimentações que sustentam as detecções mais importantes dá a maior proteção por unidade de orçamento, e as fontes de menor valor vêm depois, se o orçamento permitir.

### 32.4 Degradação controlada

Quando o SIEM está sobrecarregado, o *pipeline* deve descartar primeiro os logs de depuração de baixo valor, e não os logs de autenticação. Filas de prioridade implementam isso. Quando falta capacidade, algo precisa ser perdido; a pergunta é o quê. Os logs de depuração raramente são necessários para a detecção, enquanto os de autenticação são centrais. As filas de prioridade permitem ao *pipeline* descartar primeiro os eventos de baixa prioridade sob pressão. O descarte é registrado, para que o SOC saiba quais dados faltam naquele período. As prioridades são definidas por fonte na configuração do *pipeline* e revisadas quando novas fontes entram.

### 32.5 Medindo a completude

Comparar os eventos contados nas fontes com os eventos armazenados no SIEM mostra a perda. Um relatório diário de reconciliação lista as fontes abaixo de 99,9%. As fontes podem informar quantos eventos enviaram, e o SIEM sabe quantos armazenou; a diferença é a perda no caminho. Onde as fontes não conseguem informar contagens, os coletores podem contar o que receberam. O relatório diário lista a razão de cada fonte, e qualquer uma abaixo da meta é investigada pelo responsável pela fonte. O relatório vai aos responsáveis pelas fontes toda manhã e é resumido semanalmente para Paolo.

### 32.6 Orçamentos de erro

Se a disponibilidade cair abaixo da meta, os novos recursos ficam em pausa e o trabalho de confiabilidade tem prioridade até que o orçamento se recupere. Uma meta de 99,5% deixa 0,5% do tempo como margem para indisponibilidade. Isso dá uma regra clara e acordada de antemão para equilibrar trabalho novo e estabilidade, em vez de uma nova discussão cada vez que algo quebra. O orçamento é reiniciado a cada trimestre; com 99,5%, a margem é de cerca de onze horas por trimestre. Os gerentes de produto e os líderes do SOC acordam essa regra de antemão, para que pausar o trabalho em recursos quando o orçamento se esgota seja rotina, e não uma disputa.

### 32.7 Caso

Na primeira semana de reconciliação, os servidores web do portal mostram 99,95% de completude; o *firewall* dos depósitos mostra 97,8%, por causa de um caminho de syslog sobre UDP que descarta pacotes sob carga. O syslog sobre UDP envia mensagens sem confirmação, então os pacotes descartados sob carga simplesmente se perdem. Uma perda de 2,2% significa que cerca de uma negação em quarenta e cinco nunca chega ao SIEM. Mudar o *firewall* dos depósitos para TCP ou para um agente de encaminhamento com confirmação e *buffer* resolveria o problema, e o relatório de reconciliação vai mostrar se a completude sobe acima da meta.

### Monitorando os monitores

Coletores, analisadores e o próprio SIEM informam métricas de saúde — profundidade das filas, erros de análise, atraso de ingestão — a um sistema de monitoramento separado. Se o SIEM não está saudável, não se pode confiar nele para alertar sobre a própria falha, então os alertas de saúde seguem por um caminho independente até o engenheiro de plantão.

### Exemplo resolvido

Amara passa o *firewall* dos depósitos para o encaminhamento de logs sobre TCP, com um *buffer* local. A completude sobe para 99,96%. Ela acrescenta a mudança ao registro de confiabilidade e mantém o relatório de reconciliação rodando diariamente.

> **Caso sintético.** Os números são inventados.

### Erros e limites

As verificações de completude dependem de contagens exatas nas fontes, que alguns dispositivos não fornecem.

### Exercícios

- **EX094 — Completude.** Por que a completude é tão importante quanto a disponibilidade? *Rubrica:* 3 = o *pipeline* pode rodar com dados faltando e ainda deixar o SOC às cegas; 2 = parcial; 1 = menos importante; 0 = nada.
- **EX095 — Ordem de degradação.** Sob sobrecarga, que logs devem ser descartados primeiro? *Rubrica:* 3 = depuração de baixo valor antes de autenticação; filas de prioridade; 2 = parcial; 1 = aleatório; 0 = nada.
- **EX096 — Correção do *firewall*.** O que causou os 97,8% de completude, e o que os corrigiu? *Rubrica:* 3 = descartes do syslog sobre UDP; encaminhamento TCP com *buffer*; 99,96%; 2 = parcial; 1 = ignorado; 0 = nada.

### Síntese

Um monitoramento confiável precisa de metas tanto para o tempo no ar quanto para a completude, de redundância onde o valor é maior e de degradação controlada.

### Continue estudando — capítulo 32 de 50

[← Capítulo 31 (rascunho)](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 (rascunho) →](#ch-33)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX096 (as de EX097–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Amara Osei, Paolo Ricci, a Kingsbridge Engineering University, a Lindqvist Freight e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O acúmulo varia segundo dB/dt = A(t) − C(t): chegadas por hora menos alertas resolvidos por hora.

**EX002.** Atinge o pico de 65 alertas às 13:00, porque as chegadas ficaram acima da capacidade de 60 das 10:00 às 12:00 e só se igualaram a ela às 13:00.

**EX003.** Cerca de 40 minutos: há 40 alertas à frente dele, e o turno resolve 60 por hora.

**EX004.** Contém as contas que falharam e depois tiveram sucesso a partir da rede atacante, as mais propensas a terem sido adivinhadas corretamente.

**EX005.** 7 × 6 × 5 = 210, portanto as regras não conseguem cobrir todas as combinações e precisam ser escolhidas com base no conhecimento de ameaças.

**EX006.** Exige pelo menos um sucesso no mesmo conjunto, transformando um alerta genérico de *spraying* num alerta específico de possível comprometimento.

**EX007.** É dobrada num único registro de 5 minutos, de modo que a rajada fica visível, mas seu ritmo e sua forma se perdem.

**EX008.** Pode colocar os eventos daquele servidor na ordem errada em relação aos de outros, e é por isso que as orientações de gestão de logs enfatizam a sincronização de tempo.

**EX009.** Mais dados exigem mais servidores, energia, refrigeração e espaço de armazenamento, todos fisicamente limitados e caros.

**EX010.** Deve pulá-las com segurança e registrar quantas foram puladas, para que a perda de dados fique visível.

**EX011.** Como a resposta correta é conhecida de antemão, qualquer diferença revela um defeito no código, e não algo nos dados.

**EX012.** Evita instalar pacotes de terceiros não revisados em máquinas sensíveis e já está disponível em qualquer lugar onde o Python esteja.

**EX013.** O que foi observado, quando (com fuso horário), quais ativos, o que foi feito e o que continua desconhecido.

**EX014.** Para que todo leitor entenda o mesmo grau de certeza a partir da mesma palavra.

**EX015.** Dá horário, escala, impacto, ações tomadas e uma mudança proposta, sem o detalhe campo a campo de que os analistas precisam.

**EX016.** O armazenamento é a integral da taxa de ingestão ao longo da janela de retenção; hoje, 120 GB × 90 dias = 10,8 TB.

**EX017.** Cerca de 15,4 TB, já que a ingestão diária chega a aproximadamente 171 GB, o que excede a camada de 12 TB.

**EX018.** A política e a lei definem a retenção mínima; a matemática estima o custo e orienta as camadas dentro desses limites.

**EX019.** A taxa de verdadeiros positivos é a chance de um alerta quando um ataque acontece; a precisão é a chance de um alerta ser um ataque real.

**EX020.** 0,153, ou seja, cerca de um alerta em sete é real: aproximadamente 180 verdadeiros contra 998 falsos a cada 100.000 rajadas.

**EX021.** Porque os alarmes falsos dominam com essa taxa-base baixa, reduzi-los à metade eleva a precisão para cerca de 0,27, muito mais do que um pequeno ganho de sensibilidade.

**EX022.** Componentes no *kernel* veem com confiabilidade a atividade de processos e arquivos, mas um defeito ali pode derrubar a máquina inteira.

**EX023.** O *buffer* do agente encheu enquanto o enlace estava saturado pela rajada, então os eventos mais antigos foram descartados.

**EX024.** Equilibram a visibilidade contra o custo de CPU e memória e testam as configurações em máquinas parecidas com as de produção.

**EX025.** Um dicionário, porque cada nome de usuário aponta diretamente para sua contagem, com buscas e atualizações rápidas.

**EX026.** O código usava "maior que", enquanto o projeto queria "pelo menos"; os dois foram alinhados em ≥ 5 e o teste foi mantido.

**EX027.** Mantém pequeno o uso de memória, enquanto carregar milhões de linhas de uma vez pode esgotá-la.

**EX028.** Monitorar apenas o que a finalidade de segurança exige e acessar conteúdo, como o corpo de e-mails, somente com aprovação por caso.

**EX029.** Não havia investigação autorizada, então ela remeteu o gestor à política e ao processo de RH.

**EX030.** A faixa também atendia um parceiro logístico, então um bloqueio temporário com revisão em 24 horas evitou interromper tráfego legítimo.

**EX031.** Os atacantes espalham as tentativas por muitos endereços nas mesmas redes, então agrupar revela rajadas que as contagens por endereço escondem.

**EX032.** 203.0.113.0/24, porque suas seis falhas atingiram seis nomes de usuário diferentes, uma tentativa cada, e sete nomes de usuário aparecem ali ao todo.

**EX033.** Requisitou uma alteração de endereço às 10:07, o que sugere que a conta foi tomada.

**EX034.** Porque a configuração de auditoria de que a regra depende, como o registro da linha de comando dos processos, não está ativada ali.

**EX035.** Concedem mais privilégio, que é o que os atacantes buscam, então as mudanças merecem atenção.

**EX036.** O modelo do servidor foi atualizado por meio de uma mudança, e um processo de teste inofensivo confirmou que as linhas de comando passaram a ser registradas.

**EX037.** Para que toda regra e toda consulta usem um único nome para cada conceito, em vez de lembrar as variantes de cada fonte.

**EX038.** O portal guardava texto em hora local, enquanto os logs internos usavam UTC; converter os horários do portal na ingestão consertou a junção.

**EX039.** Os campos que as detecções e os analistas mais consultam, como usuário, host e endereço de origem.

**EX040.** A regra registra as correspondências sem alertar, para que seu ruído possa ser medido antes de os analistas serem acionados.

**EX041.** Com uma exceção estreita, que usa o *user agent* assinado da ferramenta de carga e uma verificação de calendário.

**EX042.** Uma descrição, o autor, referências, gatilhos benignos conhecidos e orientação de resposta.

**EX043.** Dados de clientes podiam ser vistos, um endereço foi alterado e o serviço de login ficou lento sob a rajada.

**EX044.** Clientes que reutilizam senhas; a limitação de taxa e a autenticação multifator reduzem o risco.

**EX045.** Entrega principalmente Detect e Respond, apoiando-se em Identify para o conhecimento dos ativos e informando Govern.

**EX046.** Gastar muito em ferramentas e negligenciar pessoas e processos.

**EX047.** Logs do portal entregues em até 2 minutos, latência da regra abaixo de 5 minutos e reconhecimento pelo analista em até 8 minutos.

**EX048.** A rajada foi reconhecida 11,5 minutos depois da injeção, dentro da meta, e o reconhecimento pelo analista foi a etapa mais lenta.

**EX049.** Ajustes grandes ou rápidos demais passam do ponto; passos pequenos, com tempo para observar os efeitos, evitam isso.

**EX050.** Uma fila sobrecarregada leva os analistas a fechar alertas às pressas, o que esconde perdas e permite mais comprometimento, acrescentando ainda mais carga.

**EX051.** No máximo um passo de limiar a cada quinze dias e nenhuma elevação depois de qualquer evento de teste perdido; a regra se estabilizou em 6 falhas, com 8 alertas falsos por dia e todos os eventos de teste pegos.

**EX052.** Porque o tráfego legítimo que atravessa uma fronteira é limitado e bem conhecido, as travessias incomuns se destacam.

**EX053.** Os logs do balanceador de carga não eram encaminhados; foram acrescentados, e os logs web agora registram um cabeçalho com o endereço do cliente que o balanceador sobrescreve, para que os clientes não possam forjá-lo.

**EX054.** Ficam numa zona separada, com contas de administrador dedicadas e protegidas por autenticação multifator.

**EX055.** Porque muitos ataques usam credenciais roubadas, mas válidas, que só os logs de identidade revelam.

**EX056.** Pedidos de MFA repetidos que o usuário nega e uma troca inesperada do dispositivo de MFA registrado.

**EX057.** Acrescentou uma confirmação por e-mail ao cliente e manteve um alerta ao analista apenas quando a confirmação falhava.

**EX058.** As prioridades de engenharia seguem o que a empresa precisa proteger — dados de clientes, entregas, pagamentos —, e não o que as ferramentas conseguem fazer.

**EX059.** Seu software antigo não consegue rodar agentes de *endpoint*, então o monitoramento de rede é a única opção.

**EX060.** Com apenas dois analistas à noite, cada alerta encaminhado a eles precisa valer o tempo limitado que têm.

**EX061.** Funcional: correlacionar falhas e sucessos por rede; não funcional: latência do alerta abaixo de 5 minutos.

**EX062.** "Os alertas devem ser gerados em até 5 minutos após o evento que os aciona, medidos por eventos sintéticos cronometrados mensais."

**EX063.** O requisito, sua fonte, o elemento de projeto que o atende e o teste que o verifica.

**EX064.** Coleta, transporte, análise e normalização, enriquecimento, armazenamento, detecção, alerta e gestão de casos.

**EX065.** O inventário de ativos não continha os dispositivos dos depósitos, então não havia com o que enriquecer.

**EX066.** Cada célula vazia virou um item do *backlog* com um responsável nomeado.

**EX067.** As fontes de dados de que precisa, as detecções existentes e a confiança nelas.

**EX068.** Porque nada as sinaliza, a cobertura de detecção desaparece sem que ninguém perceba.

**EX069.** A detecção de tomada de conta depende dessa única alimentação, que já quebrou antes.

**EX070.** Limiar 5 com sucesso: 2, 0, 1; limiar 6 com sucesso: 1, 0, 2; limiar 5 sem sucesso: 3, 2, 0.

**EX071.** Uma detecta tentativas, para o trabalho diurno de ajuste; a outra detecta comprometimento provável e aciona o turno da noite.

**EX072.** O ataque das 10:10 não tinha tido sucesso, então não havia comprometimento para acionar o plantão; a regra de tentativas ainda o registra.

**EX073.** Monitoramento de fluxos na fronteira, um sensor de detecção de rede e regras de *firewall* mais estritas com registro das conexões negadas.

**EX074.** Descobriram que o *firewall* da fronteira já registrava os fluxos, então os logs do *firewall* com regras de permissão superaram a compra de um sensor.

**EX075.** Permitir cinco serviços, registrar as negações, alertar quando um dispositivo de depósito tentar um destino novo mais de três vezes numa hora, revisar semanalmente; o risco principal é a falha da alimentação de logs.

**EX076.** Os dados recentes de alto valor ficam no SIEM para busca rápida, enquanto os dados volumosos e mais antigos vão para um *lake* mais barato.

**EX077.** Acrescenta cobertura noturna e um conhecimento de ameaças mais amplo, mas conhece menos o contexto local e depende de acordos de escalonamento claros.

**EX078.** Contexto, opções consideradas, a decisão e suas consequências.

**EX079.** Detecção: a regra de possível tomada de conta; resposta: bloquear a conta e invalidar suas sessões.

**EX080.** Um teto de 20 contas por hora, acima do qual a automação pausa e aciona o engenheiro de plantão.

**EX081.** Porque bloquear uma faixa pode cortar clientes ou parceiros legítimos, o que exige julgamento humano.

**EX082.** Um SIEM de teste com dados sintéticos reproduzidos, depois a produção em modo só monitoramento e depois o alerta completo.

**EX083.** Um campo extra vindo de uma atualização do balanceador; o analisador foi ampliado e as linhas foram mantidas como casos de teste.

**EX084.** Torna cada mudança revisável, reversível e consistente entre os ambientes.

**EX085.** Média de 10,2 minutos, mediana de 7 minutos, percentil 90 de 16,4 minutos.

**EX086.** Os tempos são assimétricos; um caso longo infla a média, enquanto a mediana mostra o caso típico e o percentil 90, a cauda que ameaça a meta.

**EX087.** Combiná-la com medidas de qualidade, como a revisão regular de uma amostra de alertas fechados.

**EX088.** A verificação confere se a regra corresponde à sua especificação; a validação confere se ela de fato ajuda a detectar ameaças reais em operação.

**EX089.** Que a regra dispara com 5 usuários e um sucesso, fica em silêncio com 4, exige um sucesso mesmo com 9 usuários e fica em silêncio sem atividade.

**EX090.** O alerta não trazia o ID do cliente porque o modelo de roteamento usava um nome de campo antigo.

**EX091.** Para descobrir problemas, como a dependência da impressora, antes que afetem os quarenta depósitos.

**EX092.** O serviço de impressão foi permitido com um motivo documentado, e os outros depósitos foram conferidos em busca das mesmas impressoras antes do grupo seguinte.

**EX093.** O *laptop* de um prestador numa rede de depósito; a TI então impôs o controle de acesso à rede para dispositivos visitantes.

**EX094.** Porque um *pipeline* pode estar no ar enquanto perde eventos em silêncio, deixando o SOC às cegas.

**EX095.** Os logs de depuração de baixo valor devem ser descartados antes dos de autenticação e de outros logs prioritários, usando filas de prioridade.

**EX096.** O syslog sobre UDP descartava pacotes sob carga; mudar para o encaminhamento TCP com um *buffer* local elevou a completude para 99,96%.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
