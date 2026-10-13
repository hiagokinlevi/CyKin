# Operações de Segurança e Blue Team: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 130, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 50 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 9–50 (EX025–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Amara Osei, Paolo Ricci, a Kingsbridge Engineering University, a Lindqvist Freight e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
