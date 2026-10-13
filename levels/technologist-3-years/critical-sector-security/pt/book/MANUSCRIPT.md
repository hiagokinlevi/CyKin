# Infraestrutura Crítica e Segurança Setorial: Prática Aplicada para Tecnólogos

- Idioma: português do Brasil (`pt`); curso de tecnólogo, três anos; aproximadamente 2.400 horas de estudo planejado (curso 092 de 207 da [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–30 de 30 têm texto didático escrito, dezessete laboratórios offline, os exercícios EX001–EX090 e as resoluções correspondentes. Revisão independente por especialistas, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: implementadores e administradores de tecnologia — administradores de sistemas e de redes, técnicos de TO e de sistemas prediais, equipes de service desk e de plataforma, analistas de segurança juniores — que já operam computadores profissionalmente e agora precisam **construir, operar e evidenciar** a segurança de um serviço do qual as pessoas dependem. Conhecimento de entrada: fundamentos de computação e introdução a operações de segurança; à vontade na linha de comando; capaz de ler e alterar levemente um script Python curto.
- Como este curso difere dos vizinhos. O [livro de bacharelado](../../../../bachelors-4-years/critical-sector-security/en/book/MANUSCRIPT.md) constrói os fundamentos conceituais da área, disciplina por disciplina. O [livro de engenharia](../../../../engineering-5-years/critical-sector-security/en/book/MANUSCRIPT.md) projeta, modela e verifica sistemas a partir de requisitos. O [livro de pós-graduação](../../../../postgraduate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) ensina especialistas a liderar e justificar decisões em escala de organização. **Este livro de tecnólogo trata de implementação e operação**: pegar um projeto que outra pessoa aprovou, construí-lo corretamente, operá-lo todos os dias, provar com evidências que os seus controles funcionam, descobrir rapidamente quando deixam de funcionar e passá-lo adiante para que o próximo turno possa continuar. Ele explica a teoria apenas até onde um implementador precisa dela para fazer boas escolhas no teclado e na reunião de mudanças.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de titularidade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: este curso é um projeto educacional independente. Não é um programa credenciado, não concede qualificação e não concede nenhuma autorização para acessar, varrer, testar ou alterar qualquer infraestrutura, operador, dispositivo, conjunto de dados ou pessoa reais. Toda organização, local, pessoa, endereço, registro, valor e resultado numérico de um exemplo resolvido ou de um laboratório é **sintético**, a menos que uma frase cite explicitamente uma fonte pública. Os endereços IP vêm de faixas privadas ([RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)) ou de faixas de documentação ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)). Nada neste livro é um procedimento operacional para uma concessionária, um hospital, um operador de transporte ou uma rede elétrica reais, e nada nele é aconselhamento jurídico, clínico ou regulatório.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão de livros](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os trinta capítulos acompanham um tecnólogo ao longo de três anos construindo e operando um único serviço. O resultado do curso é prático: **implementar um serviço de ponta a ponta com controles monitorados** num ambiente de setor crítico, e ser capaz de mostrar — com evidências operacionais, e não com afirmações — que ele funciona.

- **A Etapa 1 (Capítulos 1–5)** revisita computação, redes, programação, dados e letramento em segurança, sempre pela pergunta "o que isto significa para um serviço que não pode parar?"
- **A Etapa 2 (Capítulos 6–10)** cobre sistemas operacionais e virtualização, identidade e acesso, arquitetura, medição e uma orientação sobre os setores críticos.
- **A Etapa 3 (Capítulos 11–15)** os aplica ao serviço: ativos, fluxos de dados, cenários de risco, um primeiro conjunto de métodos e uma construção guiada do componente central.
- **A Etapa 4 (Capítulos 16–20)** trata de operá-lo: métodos de endurecimento e de mudança, ferramental, controles, monitoramento e resolução de problemas.
- **A Etapa 5 (Capítulos 21–25)** integra o serviço com os seus vizinhos, automatiza com segurança, avalia se os controles funcionam, apresenta métodos de pesquisa aplicada e trabalha em equipe.
- **A Etapa 6 (Capítulos 26–30)** passa o serviço para a operação, implanta-o e valida-o, pratica em campo, conclui a construção do trabalho de conclusão e o avalia.

Todo capítulo tem objetivos de aprendizagem, seções didáticas com definições, um exemplo resolvido, uma atividade prática, uma lista de erros comuns e limites, três exercícios numerados e uma síntese. Dezessete capítulos contêm um laboratório em Python. Os laboratórios usam apenas a biblioteca padrão do Python 3 (as saídas deste rascunho foram produzidas com o Python 3.13.5); não precisam de rede, pacotes, privilégios nem dados reais, e toda saída está impressa no texto para que você confira a sua execução. Um laboratório que grava arquivos o faz apenas dentro de um diretório temporário que ele cria e remove. Escreva a sua resposta a cada exercício antes de abrir as [resoluções](#worked-results). Muitos exercícios têm mais de uma resposta defensável: a resolução mostra uma, e a rubrica (0–3) mostra o que um avaliador recompensaria.

Mantenha quatro rótulos em toda nota de trabalho, porque os registros operacionais são lidos depois por pessoas que não estavam lá: **observado** (o que uma ferramenta ou pessoa nomeada registrou, com hora e fonte), **inferido** (o que você conclui e por quê), **feito** (o que você mudou, sob qual registro de mudança) e **em aberto** (o que ainda é desconhecido ou está inacabado, e quem é o responsável). A falha mais comum no nível de tecnólogo não é desconhecer um controle; é um controle que foi instalado uma vez, nunca testado, parou de funcionar em silêncio e continuou sendo relatado como "implantado".

### O ambiente sintético usado neste livro

| Elemento sintético | Papel no livro | Limite |
|---|---|---|
| **Fallowmere** — um distrito de cerca de 60.000 pessoas | Ambiente de todos os exemplos resolvidos. | Lugar inventado. |
| **Fallowmere Shared Technology Services (FSTS)** | Um serviço compartilhado do setor público que opera TI e parte do suporte de TO para três operadores locais. O leitor é um **Tecnólogo de Segurança** na sua equipe de Plataforma e Segurança. | Inventado; nenhuma organização, equipe ou sistema real. |
| **Fallowmere Water** — 14 estações de bombeamento (PS-01 a PS-14), uma estação de tratamento, um local central | O principal cliente do serviço construído neste livro. | Inventado. |
| **Fallowmere Community Hospital** e **Fallowmere Transit** (garagem de ônibus) | Dois outros clientes que compartilham a equipe, as redes e os fornecedores da FSTS. | Inventados. |
| **LANTERN** — o serviço de relay de telemetria | O serviço de ponta a ponta que o leitor implementa: estações → relay autenticado (RLY-01..03) → historiador (HIST-01) → relatórios, com monitoramento pela plataforma de monitoramento de segurança da FSTS (SIEM-01). | Projeto inventado para o ensino; não é uma arquitetura de referência para uma concessionária real. |
| Fornecedores **Kell Instruments**, **Arlen Controls**, **Halden Cloud**, **BayTel** | Fornecedor das RTUs das estações, fornecedor dos CLPs, hospedagem em nuvem, operadora de telecomunicações. | Empresas inventadas; qualquer semelhança com empresas reais é acidental. |
| Pessoas como A. Okafor (operação de Água), B. Lind (líder de Segurança da FSTS), E. Strand (engenheiro de plataforma), e todo endereço, conta, linha de log, valor e horário | Contexto para os exercícios. | Inventados. |

Como os dados são sintéticos, o livro às vezes pode dizer o que um operador real nunca sabe — por exemplo, que uma lacuna na telemetria foi causada por um relógio, e não por um atacante. Use esse privilégio para aprender como as verificações falham, nunca como evidência sobre organizações reais.

### Política de fontes

Toda afirmação factual sobre uma lei, norma, protocolo, incidente público ou orientação publicada remete a uma fonte consultada em outubro de 2026. Normas e orientações mudam: cada uma é citada com a sua versão ou data e precisa ser verificada de novo antes que você se apoie nela, e nada aqui interpreta uma lei para uma organização específica. Onde uma afirmação é vocabulário profissional comum — por exemplo, que uma função de hash mapeia uma entrada de qualquer tamanho para um digest de tamanho fixo —, o texto não inventa uma referência para ela. Uma citação sustenta a afirmação geral ao seu lado, nunca os detalhes sintéticos. Os incidentes públicos são descritos apenas no nível que os seus publicadores divulgaram.

### Regras de segurança para o trabalho prático

1. Pratique apenas nos laboratórios do livro, em equipamentos que são seus ou em sistemas cujo dono lhe deu permissão **escrita e específica**, nomeando os sistemas, a janela de tempo e as ações permitidas (o Capítulo 23 traz um modelo).
2. Nunca conecte um scanner, um laptop de teste ou um "script rápido" a uma rede de controle em produção sem essa permissão e sem o acordo da pessoa responsável pelo processo físico. Em tecnologia operacional, uma leitura pode ser uma ação: alguns dispositivos se comportam mal quando sondados.
3. Se você topar com uma fraqueza num sistema real, pare, anote o que viu e relate-a em particular ao seu dono ou por divulgação coordenada. Não a "confirme".
4. Mantenha segredos fora de notas, tickets e capturas de tela. A chave de laboratório do Capítulo 15 está impressa justamente porque é falsa.

## Sumário

1. [Sistemas computacionais](#ch-01) — recursos, capacidade e falhas num host que precisa continuar funcionando.
2. [Redes e serviços de internet](#ch-02) — zonas, conduítes, serviços e como conferir o que a rede realmente transporta.
3. [Fundamentos de programação](#ch-03) — escrever ferramentas pequenas, corretas e testáveis; validar entradas não confiáveis.
4. [Modelos de dados](#ch-04) — inventários, esquemas e restrições que tornam os dados operacionais confiáveis.
5. [Letramento em segurança](#ch-05) — o vocabulário de ameaças, controles e evidências para um serviço essencial.
6. [Sistemas operacionais e virtualização](#ch-06) — endurecimento, serviços, integridade de arquivos e plataformas virtuais.
7. [Fundamentos de identidade e acesso](#ch-07) — contas, autenticação, privilégios e revisão de acessos.
8. [Fundamentos de arquitetura de segurança](#ch-08) — zonas e conduítes, defesa em profundidade e projeto para a operabilidade.
9. [Evidência e medição](#ch-09) — métricas que dizem a verdade, denominadores e honestidade com amostras pequenas.
10. [Infraestrutura crítica e segurança setorial: orientação](#ch-10) — o que torna um serviço crítico e como os setores diferem.
11. [Infraestrutura crítica e segurança setorial: ativos e contexto](#ch-11) — inventário, responsabilidade, dependências e situação de suporte.
12. [Infraestrutura crítica e segurança setorial: fluxos de dados](#ch-12) — registros de fluxos, classificação, retenção e verificação.
13. [Infraestrutura crítica e segurança setorial: cenários de risco](#ch-13) — escrever cenários e ordená-los pela consequência.
14. [Infraestrutura crítica e segurança setorial: métodos I](#ch-14) — linhas de base, endurecimento e controle de mudanças como métodos diários.
15. [Infraestrutura crítica e segurança setorial: laboratório guiado](#ch-15) — construir o relay autenticado com proteção contra replay.
16. [Infraestrutura crítica e segurança setorial: métodos II](#ch-16) — tratamento de vulnerabilidades e patches, backups e recuperação.
17. [Infraestrutura crítica e segurança setorial: ferramental](#ch-17) — logs, tempo, normalização e construir uma ferramenta em que se possa confiar.
18. [Infraestrutura crítica e segurança setorial: controles](#ch-18) — escolher, implementar e documentar controles com evidências.
19. [Infraestrutura crítica e segurança setorial: monitoramento](#ch-19) — regras de detecção, a ausência como sinal e a qualidade dos alertas.
20. [Infraestrutura crítica e segurança setorial: resolução de problemas](#ch-20) — um método para falhas que podem ou não ser ataques.
21. [Infraestrutura crítica e segurança setorial: integração do serviço](#ch-21) — integrar com operadores, fornecedores, o SOC e os planos de emergência.
22. [Infraestrutura crítica e segurança setorial: automação](#ch-22) — configuração como código, detecção de deriva e automação segura.
23. [Infraestrutura crítica e segurança setorial: avaliação](#ch-23) — testar se os controles funcionam e dizer o quanto você tem certeza.
24. [Métodos de pesquisa aplicada](#ch-24) — responder a uma pergunta operacional com um estudo pequeno e honesto.
25. [Ateliê de projeto em equipe](#ch-25) — trabalhar como equipe de entrega num serviço compartilhado.
26. [Infraestrutura crítica e segurança setorial: passagem para a operação](#ch-26) — runbooks, responsabilidade e uma passagem que sobrevive ao turno da noite.
27. [Implantação e validação](#ch-27) — pré-verificações, canários, rollback e validação pós-implantação.
28. [Prática de campo](#ch-28) — trabalhar com segurança em locais remotos e com a equipe de operação.
29. [Construção do trabalho de conclusão](#ch-29) — o serviço monitorado de ponta a ponta e o seu registro de evidências.
30. [Avaliação do trabalho de conclusão](#ch-30) — revisão de projeto, evidências operacionais e o projeto de integração avaliados.

Apêndices: [Resoluções e notas de avaliação](#worked-results) · [Glossário](#glossary) · [Referências](#references).

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- descrever um host em termos dos quatro recursos que um operador de fato vê se esgotarem — processamento, memória, armazenamento e E/S — e do recurso que as pessoas esquecem, o **tempo**;
- prever quando um recurso vai se esgotar a partir de uma série curta de medições, e dizer quanto confiar na previsão;
- explicar por que um host que sustenta uma função essencial precisa de **folga**, e não apenas de "o suficiente";
- reconhecer as formas comuns pelas quais um host falha em silêncio, e escrever as primeiras verificações que as notariam.

O curso de entrada ensinou como um computador funciona. Este capítulo faz uma pergunta mais estreita, que atravessa o livro inteiro: *o que precisa continuar verdadeiro sobre este computador para que o serviço em cima dele continue funcionando, e como você saberia se deixasse de ser verdadeiro?* O host de retransmissão do LANTERN, RLY-01, é a primeira máquina que você vai conhecer; no Capítulo 29, ele será um de três.

### 1.1 Um host como um conjunto de recursos finitos

Todo serviço que você opera fica sobre um host com recursos finitos. O **processamento** (tempo de CPU) limita quanto trabalho pode ser feito por segundo. A **memória** limita quanto pode ser mantido de uma vez; quando ela acaba, o sistema operacional ou faz swap para o disco (e tudo fica lento) ou encerra processos. O **armazenamento** limita o que pode ser guardado; quando um disco enche, as gravações falham, e muitos programas falham mal — um banco de dados pode parar de aceitar gravações, um daemon de logs pode descartar mensagens em silêncio, um relay pode travar. A **E/S** (vazão de disco e de rede) limita a velocidade com que os dados entram e saem.

O recurso que as pessoas esquecem é o **tempo**: o relógio do host. Um relógio errado não para um serviço, mas faz os seus registros discordarem dos de todos os outros, quebra a validação de certificados e as verificações de janelas de tempo, e torna as investigações enganosas. Os Capítulos 17 e 20 voltam ao tempo em detalhe.

Para um serviço crítico, a pergunta útil sobre cada recurso não é "quanto está sendo usado?", mas "quanto tempo até este recurso parar o serviço, e com quanta antecedência seremos avisados?"

### 1.2 Utilização, saturação e erros

Uma forma prática de inspecionar qualquer recurso é perguntar três coisas sobre ele: a sua **utilização** (quão ocupado está, como fração da capacidade), a sua **saturação** (quanto trabalho está esperando porque ele está ocupado — uma fila de execução, uma fila de disco, pacotes descartados) e os seus **erros** (operações que falharam). Uma CPU a 60 % de utilização sem fila está bem; um disco a 40 % de utilização com uma fila longa não está. A utilização, sozinha, esconde o problema que os usuários sentem, que é a espera.

Disso decorrem dois hábitos. Primeiro, meça num percentil, não numa média: a CPU no percentil 95 ao longo de um dia informa sobre os momentos de pico que importam; a média diária os esconde. Segundo, meça por um período longo o bastante para ver o ritmo do serviço. Os relays de telemetria ficam mais ocupados quando os relatórios rodam e quando as estações enviam dados em lote depois de uma queda da rede; os sistemas hospitalares têm pico nas trocas de turno; os sistemas de transporte, na hora do rush.

### 1.3 A folga e por que "o suficiente" não basta

A **folga** é a capacidade sobressalente entre a carga normal de pico e o ponto em que o serviço se degrada. Um serviço essencial precisa de folga por três motivos: a demanda sobe de forma inesperada (uma tempestade, um evento com múltiplas vítimas, uma interrupção em outro lugar que envia tráfego para você); a própria recuperação consome recursos (as estações que estavam offline enviam o seu acúmulo quando voltam; uma restauração grava intensamente em disco); e as ferramentas de segurança consomem recursos (uma varredura, uma verificação de integridade ou uma atualização do antivírus pode dobrar o uso de CPU por minutos). Um host dimensionado para "apenas o suficiente" num dia normal está dimensionado para falhar no dia em que mais importa.

### 1.4 Prever o esgotamento

Para recursos que crescem de forma constante — o disco preenchido por logs e dados é o caso clássico —, uma reta ajustada às medições diárias recentes dá uma previsão utilizável: o crescimento por dia e os dias até um limiar de alarme e até encher. É uma previsão, não uma promessa. Ela pressupõe que o crescimento continue no ritmo recente. Estará errada se a retenção for alterada, se um processo ruidoso começar a registrar logs em nível de depuração ou se uma interrupção for seguida por uma rajada de acúmulo. Use-a para agendar a ação bem antes do limiar, e execute-a de novo depois de qualquer mudança.

Um cálculo complementar útil é o tamanho em **regime estacionário**: se os dados são mantidos por *R* dias e chegam a *g* GB por dia, o volume retido se estabiliza em cerca de *g × R*. Se esse número exceder o disco, nenhuma "limpeza" vai salvar o host; ou a retenção, ou o volume, ou a capacidade precisa mudar.

### 1.5 Modos de falha silenciosos

Hosts em serviços de longa duração tendem a falhar de um pequeno número de formas silenciosas: um disco ou partição enche; uma tarefa de rotação de logs para e um arquivo cresce sem limite; um certificado expira; o relógio deriva depois que a sua fonte de tempo fica inalcançável; um processo vaza memória e é reiniciado pelo gerenciador do sistema a cada poucos dias, perdendo os dados em trânsito; uma tarefa agendada (backup, relatório) falha e ninguém lê o seu e-mail. Cada um deles pode ser notado com uma verificação que não custa quase nada — se alguém escrever a verificação e alguém ler o seu resultado. O Capítulo 19 transforma essas verificações em monitoramento.

### 1.6 Exemplo resolvido: o disco do RLY-01 (sintético)

E. Strand pergunta se o RLY-01, que armazena em buffer a telemetria das estações e mantém os seus próprios logs por 30 dias, precisa de um disco maior antes do inverno. Você coleta 14 dias de uso de disco (disco de 200 GB) e a CPU diária no percentil 95. O disco cresce cerca de 1,9 GB por dia e está em 120,9 GB. O alarme de operações dispara em 85 % (170 GB). Neste ritmo, o alarme dispara em cerca de 26 dias e o disco enche em cerca de 41 dias. Com retenção de 30 dias, o volume de logs em regime estacionário é de cerca de 57 GB — mas o disco já passou bem disso, o que indica que o crescimento não vem apenas de logs dentro da retenção. Algo está mantendo dados por mais de 30 dias. Essa é uma pergunta de configuração, não de capacidade, e deve ser respondida antes de comprar um disco.

A série de CPU mostra um padrão semanal: os dias 6–7 de cada semana rodam a cerca de 62 %, contra cerca de 42 % nos outros dias. Você pergunta à operação de Água e descobre que os relatórios semanais de conformidade rodam nesses dias. Essa é uma carga normal, mas é a carga para a qual você precisa dimensionar.

### 1.7 Atividade prática: folga de capacidade

Execute o Laboratório 1. Ele ajusta uma reta à série do disco, informa os dias até o alarme e até encher, o volume de logs em regime estacionário com retenção de 30 dias, e compara a CPU nos dias de relatório com a dos outros dias.

**Laboratório 1** (salve como `lab01.py`, execute com `python3 lab01.py`):

```python
# Lab 1 - capacity headroom for the relay host (offline, standard library only)
# Synthetic: Fallowmere relay host RLY-01. Daily samples over 14 days.
disk_total_gb = 200.0
disk_used_gb = [96.0, 97.9, 99.7, 101.8, 103.6, 105.5, 107.6, 109.4, 111.3, 113.2, 115.1, 117.0, 118.8, 120.9]
cpu_p95 = [41, 43, 40, 44, 42, 61, 63, 42, 41, 44, 43, 40, 62, 64]  # percent, 95th percentile per day
alarm_at = 0.85  # operations alarm when disk reaches 85 % full

n = len(disk_used_gb)
xs = list(range(n))
mx, my = sum(xs) / n, sum(disk_used_gb) / n
slope = sum((x - mx) * (y - my) for x, y in zip(xs, disk_used_gb)) / sum((x - mx) ** 2 for x in xs)
print(f"growth: {slope:.2f} GB/day")
for limit, label in ((alarm_at * disk_total_gb, "85% alarm"), (disk_total_gb, "full")):
    days = (limit - disk_used_gb[-1]) / slope
    print(f"days until {label}: {days:.1f}")
# retention: logs kept 30 days; growth comes from logs (synthetic assumption)
print(f"steady-state log volume at 30-day retention: {slope*30:.1f} GB")
weekly = [cpu_p95[i] for i in range(n) if i % 7 in (5, 6)]
weekday = [cpu_p95[i] for i in range(n) if i % 7 not in (5, 6)]
print(f"cpu p95 mean weekday {sum(weekday)/len(weekday):.1f}% vs days 6-7 of each week {sum(weekly)/len(weekly):.1f}%")
```

Saída esperada (Python 3.13.5):

```text
growth: 1.91 GB/day
days until 85% alarm: 25.7
days until full: 41.4
steady-state log volume at 30-day retention: 57.3 GB
cpu p95 mean weekday 42.0% vs days 6-7 of each week 62.5%
```

Registre os quatro números na sua nota de trabalho sob **observado**, depois escreva uma frase **inferida** e um item **em aberto**. Um bom item em aberto nomeia uma pergunta e um responsável: "Por que o RLY-01 retém mais de 30 dias de dados? — E. Strand, até sexta-feira."

### 1.8 Erros comuns e limites

- Relatar a CPU média e concluir que há folga, quando o pico — o momento que importa — está perto da saturação.
- Tratar uma previsão linear como garantia; ela pressupõe que o futuro se pareça com as duas últimas semanas.
- Resolver uma falha de retenção ou de logs comprando capacidade, o que esconde a falha até o novo disco encher.
- Esquecer que a recuperação e as atividades de segurança consomem recursos.
- Definir um alarme num limiar que deixa menos tempo de aviso do que o necessário para adquirir, aprovar e instalar mais capacidade.
- Ignorar o relógio porque "é só o tempo".

Catorze amostras são uma base pequena para qualquer previsão. O valor do método está em transformar uma impressão ("o disco parece estar enchendo") num número com uma premissa explícita, que alguém pode conferir.

### Exercícios — capítulo 1

**EX001 — Prazo de reposição versus tempo de aviso.** *Objetivo:* definir um limiar de alarme a partir do prazo operacional de reposição. *Entradas:* a saída do Laboratório 1; a aquisição e a instalação aprovada de um disco novo levam 21 dias úteis (cerca de 30 dias corridos). *Restrições:* mantenha a mesma taxa de crescimento. *Etapas:* (1) calcule o nível de preenchimento em que você precisa abrir a solicitação para que o disco seja instalado antes de encher, com 7 dias de margem; (2) expresse-o como porcentagem do disco; (3) diga se o alarme de 85 % é adequado. *Evidência esperada:* cálculo e recomendação em duas frases. *Rubrica:* 3 = limiar correto (37 dias × 1,91 GB ≈ 71 GB de espaço livre necessários, ou seja, abrir a solicitação em cerca de 129 GB ou 65 %, que o RLY-01 atinge em cerca de quatro dias) e um julgamento claro de que 85 % é tarde demais para esse prazo; 2 = método certo, deslize aritmético; 1 = limiar escolhido sem o prazo de reposição; 0 = nada.

**EX002 — Explique o crescimento.** *Objetivo:* separar um problema de capacidade de um problema de configuração. *Entradas:* o exemplo resolvido. *Restrições:* não toque em nenhum sistema real; raciocine a partir dos números. *Etapas:* (1) calcule quantos dias de dados, a 1,91 GB/dia, os 120,9 GB atuais representam; (2) dê duas causas de configuração plausíveis; (3) descreva a verificação que distinguiria uma da outra. *Evidência esperada:* nota curta com os rótulos observado / inferido / em aberto. *Rubrica:* 3 = cerca de 63 dias calculados, duas causas específicas (por exemplo, rotação que não apaga, buffer para um upstream offline que não está sendo esvaziado, um segundo fluxo de logs fora da política de retenção) e uma verificação para cada uma; 2 = causas genéricas; 1 = recomenda apenas um disco maior; 0 = nada.

**EX003 — Lista de verificação de falhas silenciosas.** *Objetivo:* transformar modos de falha silenciosos em verificações. *Entradas:* Capítulo 1 ("Modos de falha silenciosos"). *Restrições:* cinco verificações; cada uma deve nomear o que é medido, o limiar e quem lê o resultado. *Etapas:* escreva uma tabela com as colunas: modo de falha, medição, limiar, leitor, ação. *Evidência esperada:* tabela. *Rubrica:* 3 = cinco modos de falha distintos, limiares mensuráveis com tempo de aviso, um leitor nomeado e uma ação para cada um; 2 = uma coluna fraca; 1 = "monitorar o servidor" genérico; 0 = nada.

### Síntese do capítulo

Um host é um conjunto de recursos finitos mais um relógio. Para um serviço essencial, a pergunta sobre cada recurso é quanto tempo falta até ele parar o serviço e com quanta antecedência você será avisado. Meça utilização, saturação e erros em percentis ao longo do ritmo natural do serviço; mantenha folga para os dias ruins, para a recuperação e para o trabalho de segurança; preveja o esgotamento com premissas explícitas; e escreva verificações baratas para as falhas silenciosas que de fato derrubam serviços. Quando os números contrariam as expectativas, como o disco do RLY-01, procure uma causa de configuração antes de comprar capacidade.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 30

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- descrever uma rede em termos de **zonas** (grupos de sistemas com confiança e função semelhantes) e **conduítes** (os caminhos permitidos entre elas);
- ler um registro de fluxo e mapeá-lo para zonas, protocolos e portas;
- comparar o que a rede de fato transporta com o que foi declarado, e classificar cada diferença;
- explicar por que um fluxo declarado que **não** transporta tráfego também é uma constatação.

O Capítulo 1 olhou para um host. Um serviço é feito de muitos hosts conversando entre si. Na infraestrutura crítica, a rede é onde se espera que a maior parte da separação entre sistemas de negócio, sistemas de controle e o mundo externo seja aplicada — e onde ela mais se desgasta, uma regra "temporária" de cada vez.

### 2.1 De endereços a zonas

Um endereço IP diz para onde um pacote vai; não diz para que serve o destino. Por isso, os operadores agrupam os sistemas em **zonas**: no projeto do LANTERN, a zona de *estações* (CLPs e RTUs nas estações de bombeamento), a zona de *relay* (hosts RLY), a zona *corporativa* (sistemas de negócio da FSTS e os usuários de relatórios do historiador) e a *externa* (tudo o que está fora, incluindo os fornecedores). A ideia de zonas e conduítes vem da prática de segurança em automação industrial: a série ISA/IEC 62443 usa exatamente esses termos ([visão geral da ISA](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)), e o guia de TO do NIST recomenda segmentar as redes de controle das redes de negócio ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

Um **conduíte** é um caminho declarado e justificado entre duas zonas: zona de origem, zona de destino, protocolo, porta e finalidade. O LANTERN declara quatro: as estações enviam Modbus/TCP (tcp/502) ao relay; o relay envia HTTPS (tcp/443) ao historiador na zona corporativa; os administradores na zona corporativa alcançam o relay por SSH (tcp/22); e o relay fornece hora (udp/123, NTP) às estações.

### 2.2 Serviços, portas e o que eles implicam

Um número de porta é uma convenção, não uma garantia: a tcp/443 costuma transportar TLS, mas qualquer coisa pode escutar ali. Ainda assim, a convenção diz o que esperar e o que questionar. Protocolos industriais como o Modbus/TCP foram projetados para redes fechadas e não têm autenticação embutida; um dispositivo que aceita escritas Modbus as aceitará de qualquer um que consiga alcançá-lo. É por isso que o caminho importa tanto: *se um laptop corporativo consegue alcançar um CLP na tcp/502, a única coisa entre um erro (ou um atacante) e uma bomba é a ausência de alguém tentando.*

Os serviços de internet — DNS, NTP, HTTPS, SSH — são o encanamento de todo serviço moderno. Cada um tem um modo de falha que importa operacionalmente: a falha do DNS torna os nomes irresolvíveis, embora os hosts estejam bem; a falha do NTP deixa os relógios derivarem; a falha do TLS (um certificado expirado) transforma um serviço que funciona num serviço inalcançável; o SSH exposto à internet atrai tentativas constantes de adivinhar senhas.

### 2.3 Declarado versus observado

Uma base de regras de firewall ou um diagrama de projeto diz o que *deveria* acontecer. Os **registros de fluxo** — resumos de conversas coletados por firewalls, switches ou sensores — dizem o que *de fato* aconteceu. Comparar os dois é uma das tarefas de rotina de maior valor que um tecnólogo pode fazer, e não exige ferramentas de ataque: é ler os seus próprios registros. Cada diferença cai numa de quatro classes:

1. **Observado e declarado** — esperado; ainda assim, confira se os volumes parecem normais.
2. **Observado, mas não declarado** — existe um caminho que ninguém justificou. Ou a declaração está incompleta (atualize-a, com um responsável e uma finalidade), ou a base de regras é permissiva demais (corrija-a).
3. **Declarado, mas não observado** — ou o serviço não está funcionando (uma estação está em silêncio), ou o conduíte declarado está obsoleto e deve ser removido.
4. **Observado para uma zona desconhecida** — um endereço que você não consegue situar; o seu inventário está incompleto.

### 2.4 Exemplo resolvido: os fluxos de uma noite (sintético)

B. Lind lhe entrega uma exportação de fluxos do firewall central referente a uma noite. A maioria dos fluxos corresponde a conduítes. Três não: uma estação de trabalho corporativa, 10.40.3.7, conversou em Modbus diretamente com o CLP da PS-04 (12 conversas); um endereço externo, 192.0.2.44, alcançou o relay por SSH (3 conversas); e o relay fez uma conexão HTTPS para um endereço externo, 192.0.2.80. Uma origem declarada, a RTU da PS-09 em 10.20.0.13, não enviou nada.

Nada disso é prova de ataque. O fluxo corporativo-para-CLP pode ser um engenheiro usando uma ferramenta de configuração a partir da rede errada; o SSH externo pode ser ruído de fundo da internet alcançando uma porta exposta; o HTTPS de saída do relay pode ser uma atualização de pacotes. Cada um ainda é uma constatação, porque cada um é um caminho que o projeto não permite. A estação silenciosa é antes de tudo um problema operacional: a operação de Água pode estar operando a PS-09 às cegas.

### 2.5 Atividade prática: fluxos versus conduítes

Execute o Laboratório 2. Ele atribui cada endereço a uma zona com o módulo `ipaddress`, compara cada fluxo com os conduítes declarados e relata os fluxos declarados com tráfego zero.

**Laboratório 2** (salve como `lab02.py`, execute com `python3 lab02.py`):

```python
# Lab 2 - observed flows versus the declared conduit list (offline, standard library only)
# Synthetic: Fallowmere Water pumping-station network. Addresses are documentation/private ranges.
import ipaddress
zones = {
    "station": ipaddress.ip_network("10.20.0.0/24"),
    "relay":   ipaddress.ip_network("10.30.0.0/28"),
    "corp":    ipaddress.ip_network("10.40.0.0/16"),
    "vendor":  ipaddress.ip_network("192.0.2.0/24"),   # TEST-NET-1, stands in for internet
}
declared = {("station", "relay", "tcp", 502), ("relay", "corp", "tcp", 443),
            ("corp", "relay", "tcp", 22), ("relay", "station", "udp", 123)}
flows = """10.20.0.11,10.30.0.5,tcp,502,1840
10.20.0.12,10.30.0.5,tcp,502,1790
10.30.0.5,10.40.8.20,tcp,443,3600
10.40.3.7,10.30.0.5,tcp,22,4
10.30.0.5,10.20.0.11,udp,123,96
10.40.3.7,10.20.0.11,tcp,502,12
192.0.2.44,10.30.0.5,tcp,22,3
10.30.0.5,192.0.2.80,tcp,443,1
10.20.0.13,10.30.0.5,tcp,502,0"""
def zone(a):
    ip = ipaddress.ip_address(a)
    return next((z for z, net in zones.items() if ip in net), "unknown")
seen = set()
for line in flows.splitlines():
    s, d, p, port, count = line.split(",")
    key = (zone(s), zone(d), p, int(port))
    if int(count) == 0:
        print(f"SILENT  {s:>12} -> {d:<12} {p}/{port}  (declared flow with no traffic)")
        continue
    seen.add(key)
    tag = "OK     " if key in declared else "UNDECL "
    print(f"{tag} {s:>12} -> {d:<12} {p}/{port} {key[0]}->{key[1]} n={count}")
for k in sorted(declared - seen):
    print("NOT SEEN", k)
```

Saída esperada (Python 3.13.5):

```text
OK        10.20.0.11 -> 10.30.0.5    tcp/502 station->relay n=1840
OK        10.20.0.12 -> 10.30.0.5    tcp/502 station->relay n=1790
OK         10.30.0.5 -> 10.40.8.20   tcp/443 relay->corp n=3600
OK         10.40.3.7 -> 10.30.0.5    tcp/22 corp->relay n=4
OK         10.30.0.5 -> 10.20.0.11   udp/123 relay->station n=96
UNDECL     10.40.3.7 -> 10.20.0.11   tcp/502 corp->station n=12
UNDECL    192.0.2.44 -> 10.30.0.5    tcp/22 vendor->relay n=3
UNDECL     10.30.0.5 -> 192.0.2.80   tcp/443 relay->vendor n=1
SILENT    10.20.0.13 -> 10.30.0.5    tcp/502  (declared flow with no traffic)
```

Escreva cada constatação numa linha: o que foi observado, a qual classe pertence, a explicação benigna mais provável, a explicação mais preocupante e a próxima verificação. Não "teste" nenhum caminho você mesmo; pergunte ao responsável.

Aplicadas à exportação da noite, as quatro linhas ficam assim. Corporativo 10.40.3.7 para Modbus da PS-04, 12 conversas: caminho não declarado; benigna, a ferramenta de configuração de um engenheiro na rede errada; preocupante, uma estação de trabalho comprometida alcançando um CLP; próxima verificação, perguntar à engenharia de Água quem usa esse host. Externo 192.0.2.44 para o relay por SSH: exposição; próxima verificação, por que a porta 22 responde a partir de fora. Relay para 192.0.2.80 HTTPS: saída não declarada. PS-09 em silêncio: fluxo declarado com tráfego zero, levado primeiro à operação de Água.

### 2.6 Erros comuns e limites

- Ler uma base de regras e acreditar que ela descreve o tráfego; as regras são intenções, os fluxos são fatos.
- Tratar "não declarado" como "malicioso" — ou como "inofensivo porque é interno".
- Ignorar fluxos declarados silenciosos; uma estação que para de falar é uma interrupção de serviço antes de ser uma questão de segurança.
- Presumir que uma porta identifica uma aplicação.
- Coletar fluxos apenas na borda com a internet, onde os caminhos de maior consequência (corporativo para controle) são invisíveis.

Os registros de fluxo mostram quem conversou com quem, em qual porta, quanto; não mostram conteúdo nem intenção, e podem ser amostrados. São excelentes para conferir a arquitetura e fracos para provar o que foi feito.

### Exercícios — capítulo 2

**EX004 — Classifique e priorize.** *Objetivo:* classificar as diferenças de fluxo e ordenar o acompanhamento. *Entradas:* a saída do Laboratório 2. *Restrições:* quatro constatações; no máximo uma frase de explicação cada. *Etapas:* (1) ponha cada constatação numa classe do Capítulo 2 ("Declarado versus observado"); (2) ordene-as para acompanhamento pela consequência potencial para o serviço de água; (3) nomeie o responsável que você contataria primeiro para cada uma. *Evidência esperada:* tabela. *Rubrica:* 3 = Modbus corporativo→estação em primeiro lugar porque alcança o processo físico, PS-09 silenciosa tratada como prioridade operacional, SSH externo e saída do relay ordenados com sensatez, responsáveis nomeados; 2 = classes certas, ordenação mal justificada; 1 = ordena pelo número de conversas; 0 = nada.

**EX005 — Atualize a declaração.** *Objetivo:* decidir entre mudar o projeto e mudar a rede. *Entradas:* a operação de Água confirma que o HTTPS de saída do relay foi uma atualização do sistema operacional a partir de um espelho do fornecedor; o tráfego corporativo→CLP foi o laptop de um engenheiro. *Restrições:* todo conduíte precisa de origem, destino, protocolo/porta, finalidade e responsável. *Etapas:* (1) decida, para cada um, se acrescenta um conduíte ou remove o caminho; (2) para qualquer conduíte acrescentado, escreva a sua entrada completa; (3) para o acesso do engenheiro, proponha o caminho declarado que deve substituí-lo. *Evidência esperada:* lista de conduítes atualizada e justificativa. *Rubrica:* 3 = caminho de atualização acrescentado de forma estreita (espelho específico, via proxy ou servidor de atualização, responsável nomeado) ou substituído por uma fonte interna de atualizações; acesso de engenharia movido para um caminho de salto declarado e autenticado, e não corporativo→CLP; 2 = entradas sensatas, mas incompletas; 1 = simplesmente permite tudo o que foi observado; 0 = nada.

**EX006 — Estenda o laboratório.** *Objetivo:* tornar a ferramenta de comparação mais útil. *Entradas:* Laboratório 2. *Restrições:* apenas a biblioteca padrão; não altere os dados sintéticos, exceto como indicado. *Etapas:* (1) acrescente um fluxo de 10.50.1.9 para o relay na tcp/443; (2) modifique o script para que endereços fora de todas as zonas sejam relatados como "UNKNOWN ZONE", em vez de casados; (3) mostre a nova saída. *Evidência esperada:* diff do código e saída. *Rubrica:* 3 = endereço desconhecido relatado de forma distinta e a execução o mostra; 2 = funciona, mas a mensagem é pouco clara; 1 = não executado; 0 = nada.

### Síntese do capítulo

Pense na rede como zonas unidas por conduítes declarados, cada um com uma finalidade e um responsável. As regras declaram intenções; os registros de fluxo declaram fatos. Comparar os dois com regularidade — observado e declarado, observado mas não declarado, declarado mas silencioso, desconhecido — é barato, seguro e está entre as coisas mais valiosas que um implementador faz. Na infraestrutura crítica, o caminho não declarado de maior consequência é o que alcança o processo físico.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 30

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- escrever uma pequena ferramenta cujo comportamento diante de entradas ruins é decidido de antemão, e não descoberto em produção;
- validar entradas não confiáveis por **allowlisting** de estrutura, tipo, faixa e ordem;
- separar os desfechos **rejeitar**, **quarentenar** e **aceitar**, e explicar por que um sistema em operação precisa dos três;
- testar uma ferramenta com casos deliberadamente ruins e registrar os resultados como evidência.

Os implementadores em serviços críticos escrevem muito código pequeno: parsers, cola entre sistemas, verificações, geradores de relatórios. A maior parte nunca é revisada. Este capítulo trata de escrever esse código de modo que ele falhe com segurança, porque, no LANTERN, o código que lê as mensagens das estações decide no que o historiador — e, portanto, os operadores — acreditam sobre a rede de água.

### 3.1 Entrada não confiável

**Entrada não confiável** é qualquer dado cujo conteúdo você não controla: mensagens de dispositivos de campo, arquivos de fornecedores, campos digitados por usuários, registros do sistema de outra organização. Mesmo um dispositivo que é seu se torna não confiável quando você lembra que ele pode estar mal configurado, com defeito, ter sido substituído ou estar sendo personificado. A regra é simples: confira a entrada contra o que você espera *antes* de agir sobre ela, e decida de antemão o que acontece quando ela falha na verificação. A orientação do projeto OWASP sobre validação de entradas recomenda o allowlisting (aceitar apenas formas sabidamente boas) em vez do denylisting (bloquear formas sabidamente ruins), validar tanto a sintaxe quanto o significado, e fazê-lo o mais cedo possível ([OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)).

### 3.2 Camadas de validação

Para uma mensagem de telemetria no formato `STATION|TAG|VALUE|UNIX_TIME|SEQ`, a validação tem camadas, e a ordem importa:

1. **Estrutura** — exatamente cinco campos. Um número errado de campos significa que a mensagem não pode ser interpretada de forma alguma.
2. **Identidade e vocabulário** — o identificador da estação corresponde exatamente ao padrão permitido (`PS-` e dois dígitos) e a tag é uma que o sistema conhece. Tags desconhecidas são rejeitadas, e não guardadas "por via das dúvidas".
3. **Tipo** — o valor, o tempo e a sequência são interpretados como números. Valores que são interpretados, mas não são finitos (`nan`, `inf`), são rejeitados; muitas linguagens os interpretam sem reclamar.
4. **Significado físico** — o valor fica dentro do que o processo físico pode produzir (um nível de reservatório entre 0 e 12 metros; cloro entre 0 e 5 mg/L neste projeto sintético). Um valor fora dessa faixa não é necessariamente malicioso — sensores falham —, então ele é **quarentenado** para revisão por uma pessoa, em vez de ser descartado ou guardado em silêncio.
5. **Tempo** — o carimbo de tempo da mensagem está próximo do relógio do receptor. Uma diferença grande significa um problema de relógio ou uma mensagem antiga; quarentene-a.
6. **Ordem** — o número de sequência é maior que o último aceito para aquela estação. Um número repetido ou menor é uma reprodução ou uma reordenação; rejeite-o.

### 3.3 Rejeitar, quarentenar, aceitar

Uma função de validação que só retorna "válido" ou "inválido" força uma má escolha para os dados limítrofes: ou jogar fora uma leitura de que um operador pode precisar, ou guardar uma que pode enganar. Os sistemas em operação precisam de um terceiro desfecho. **Rejeitar** significa que a entrada não pode ser confiada nem interpretada, e é registrada em log e descartada. **Quarentenar** significa que a entrada é interpretável, mas implausível; ela é mantida à parte, sinalizada e revisada. **Aceitar** significa que ela passou em todas as verificações e pode servir de base para ação. Cada desfecho é contado: um aumento súbito de rejeições é, por si só, um sinal de monitoramento (Capítulo 19).

### 3.4 Disciplina do código pequeno

Quatro hábitos tornam as pequenas ferramentas confiáveis. Mantenha **uma função por decisão**, para que ela possa ser testada sozinha. Torne o **estado explícito** — a última sequência vista por estação é passada como argumento, e não escondida numa global. **Falhe fechado** — qualquer caminho que você não previu termina em rejeição, e não em aceitação. E **teste primeiro com casos ruins**: para cada verificação, escreva pelo menos uma entrada que deveria falhar nela, e execute todas depois de cada mudança.

O Laboratório 3 segue os quatro em pequena escala: todas as decisões ficam em uma única função curta, `validate()`, que pode ser testada sozinha. A verificação de sequência recebe como argumento o último número aceito por estação, e é por isso que o 102 repetido pode ser testado sozinho; e a regra de plausibilidade do cloro é uma etapa separada, guiada pela tabela `LIMITS` depois que o valor é convertido, e é por isso que 9,80 mg/L pode ser quarentenado em vez de rejeitado sem mexer no parser.

### 3.5 Exemplo resolvido: o validador de mensagens das estações (sintético)

O Laboratório 3 implementa as seis camadas. Executá-lo sobre onze mensagens sintéticas produz três aceitações, seis rejeições e duas quarentenas. Olhe para os casos que um parser ingênuo erraria: `nan` é interpretado como float e seria guardado; `210.5;DROP` só é pego porque o valor é interpretado como número, em vez de repassado como texto; `PS-7` falha porque o padrão é casado por inteiro; um número de sequência 102 repetido é rejeitado como reprodução, embora a mensagem seja perfeita em todo o resto; e um valor de cloro de 9,80 mg/L é quarentenado, e não rejeitado, porque uma pessoa precisa saber se o analisador da PS-07 falhou.

### 3.6 Atividade prática: validador e casos de teste

**Laboratório 3** (salve como `lab03.py`, execute com `python3 lab03.py`):

```python
# Lab 3 - validating telemetry messages before they reach the historian (offline, standard library only)
# Synthetic message format from Fallowmere pumping stations:  STATION|TAG|VALUE|UNIX_TIME|SEQ
import re
LIMITS = {"LEVEL_M": (0.0, 12.0), "FLOW_LS": (0.0, 450.0), "CL2_MGL": (0.0, 5.0)}
STATION = re.compile(r"PS-\d{2}")
def validate(line, now, last_seq):
    parts = line.strip().split("|")
    if len(parts) != 5:
        return "reject: field count"
    st, tag, val, ts, seq = parts
    if not STATION.fullmatch(st):
        return "reject: station id"
    if tag not in LIMITS:
        return "reject: unknown tag"
    try:
        v, t, q = float(val), int(ts), int(seq)
    except ValueError:
        return "reject: not numeric"
    if v != v or v in (float("inf"), float("-inf")):
        return "reject: not finite"
    lo, hi = LIMITS[tag]
    if not lo <= v <= hi:
        return "quarantine: out of physical range"
    if abs(now - t) > 300:
        return "quarantine: clock skew >300 s"
    if q <= last_seq.get(st, -1):
        return "reject: replay or reorder"
    last_seq[st] = q
    return "accept"
now = 1_790_000_000
msgs = ["PS-04|LEVEL_M|3.42|1789999990|101", "PS-04|LEVEL_M|3.44|1789999995|102",
        "PS-04|LEVEL_M|3.44|1789999995|102", "PS-07|CL2_MGL|0.61|1789999801|55",
        "PS-07|CL2_MGL|9.80|1789999990|56", "PS-07|FLOW_LS|nan|1789999990|57",
        "PS-7|FLOW_LS|120|1789999990|58", "PS-09|PRESS_BAR|2.1|1789999990|9",
        "PS-09|FLOW_LS|210.5|1789990000|10", "PS-09|FLOW_LS|210.5;DROP|1789999990|11",
        "PS-04|LEVEL_M|3.47|1789999999"]
state = {}
counts = {}
for m in msgs:
    r = validate(m, now, state)
    counts[r.split(":")[0]] = counts.get(r.split(":")[0], 0) + 1
    print(f"{m:<38} {r}")
print(counts)
```

Saída esperada (Python 3.13.5):

```text
PS-04|LEVEL_M|3.42|1789999990|101      accept
PS-04|LEVEL_M|3.44|1789999995|102      accept
PS-04|LEVEL_M|3.44|1789999995|102      reject: replay or reorder
PS-07|CL2_MGL|0.61|1789999801|55       accept
PS-07|CL2_MGL|9.80|1789999990|56       quarantine: out of physical range
PS-07|FLOW_LS|nan|1789999990|57        reject: not finite
PS-7|FLOW_LS|120|1789999990|58         reject: station id
PS-09|PRESS_BAR|2.1|1789999990|9       reject: unknown tag
PS-09|FLOW_LS|210.5|1789990000|10      quarantine: clock skew >300 s
PS-09|FLOW_LS|210.5;DROP|1789999990|11 reject: not numeric
PS-04|LEVEL_M|3.47|1789999999          reject: field count
{'accept': 3, 'reject': 6, 'quarantine': 2}
```

Antes de mudar qualquer coisa, anote o que você espera que cada linha imprima. Depois execute. Toda linha em que a sua expectativa estava errada é um ponto em que o seu modelo mental do código estava errado — e esse é o objetivo do exercício.

Três linhas costumam surpreender os leitores: `nan` ser rejeitado em vez de guardado, `PS-7` falhar no padrão de identificador embora pareça inofensivo, e a leitura de cloro de 9,80 mg/L terminar em quarentena em vez de rejeição. Se você previu errado alguma delas, anote por quê; depois acrescente à lista de mensagens um caso ruim seu, como um número de sequência menor que 102 ou um identificador com um espaço no final, e confirme que o validador o rejeita antes de confiar na mudança.

### 3.7 Erros comuns e limites

- Validar com uma denylist ("rejeitar se contiver ponto e vírgula") em vez de uma allowlist do que é aceitável.
- Usar um casamento parcial para identificadores, de modo que `PS-7`, `XPS-04` ou `PS-04-test` passem.
- Esquecer `nan` e o infinito.
- Descartar em silêncio valores fora da faixa, de modo que um sensor com defeito pareça uma estação quieta.
- Atualizar o estado de reprodução antes que todas as outras verificações tenham passado — uma mensagem autenticada, mas malformada ou implausível, pode então bloquear mensagens legítimas que vêm depois (você verá isso no Capítulo 29).
- Escrever testes só para o caminho feliz.

A validação protege o receptor de dados malformados e implausíveis. Ela **não** prova que os dados são autênticos: uma mensagem perfeitamente formatada e plausível ainda pode ser forjada. A autenticação é acrescentada no Capítulo 15.

### Exercícios — capítulo 3

**EX007 — Preveja, depois execute.** *Objetivo:* testar o seu modelo da ordem de validação. *Entradas:* Laboratório 3. *Restrições:* escreva as previsões antes de executar. *Etapas:* (1) acrescente três mensagens: `PS-04|LEVEL_M|inf|1789999999|103`, `PS-04|LEVEL_M|12.0|1789999999|103`, `PS-04|LEVEL_M|-0.0|1789999999|104`; (2) preveja cada desfecho; (3) execute e explique qualquer surpresa. *Evidência esperada:* previsões, saída, explicação. *Rubrica:* 3 = inf rejeitado por não ser finito, 12.0 aceito (limite inclusivo), -0.0 aceito porque −0,0 é igual a 0,0 e a sequência avançou, com um comentário sobre se −0,0 deveria ser normalizado; 2 = desfechos certos, explicação rasa; 1 = não executado; 0 = nada.

**EX008 — Projeto da quarentena.** *Objetivo:* projetar o caminho da quarentena. *Entradas:* Capítulo 3 ("Rejeitar, quarentenar, aceitar") e o caso do cloro da PS-07. *Restrições:* nenhum código é exigido. *Etapas:* (1) diga onde as mensagens quarentenadas são guardadas e por quanto tempo; (2) diga quem as revisa, com que rapidez, e o que dispara o escalonamento para a operação de Água; (3) diga o que a tela do operador deve mostrar enquanto um valor está em quarentena. *Evidência esperada:* projeto de meia página. *Rubrica:* 3 = armazenamento separado com retenção, revisor nomeado e tempo de resposta, regra de escalonamento ligada ao processo físico (por exemplo, duas leituras consecutivas de cloro implausíveis → ligar para a sala de controle), tela mostrando "valor retido — em revisão" em vez do último valor bom como se fosse atual; 2 = falta um elemento; 1 = "um administrador confere"; 0 = nada.

**EX009 — Falhe fechado.** *Objetivo:* encontrar um caminho que falha aberto. *Entradas:* este fragmento: `try: v = float(val) except: pass; if v > hi: return "quarantine"; return "accept"`. *Restrições:* identifique, explique, corrija. *Etapas:* (1) mostre uma entrada para a qual ele retorna accept indevidamente; (2) explique; (3) reescreva-o. *Evidência esperada:* entrada, explicação, código corrigido. *Rubrica:* 3 = mostra que um valor não numérico deixa `v` sem definição ou obsoleto (um `NameError` na primeira mensagem, ou o valor da mensagem anterior reaproveitado depois), aponta a falta do limite inferior e o `except` sem tipo, e reescreve para retornar reject em qualquer falha de interpretação, com os dois limites e uma verificação de finitude; 2 = encontra um problema; 1 = vago; 0 = nada.

### Síntese do capítulo

O código pequeno decide o que os operadores veem. Trate toda mensagem como não confiável, valide-a em camadas — estrutura, identidade, tipo, significado físico, tempo, ordem — e dê aos dados limítrofes um caminho de quarentena, para que as falhas não sejam nem escondidas nem guardadas como verdade. Mantenha as decisões em funções pequenas e testáveis, torne o estado explícito, falhe fechado e teste primeiro os casos ruins. Validação não é autenticação; essa vem depois.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 30

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- modelar registros operacionais — ativos, responsáveis, situação de suporte — como tabelas relacionadas por chaves;
- usar **restrições** para que o banco de dados rejeite registros que não podem ser verdadeiros;
- escrever consultas que respondem a perguntas operacionais ("quais ativos críticos não têm responsável?") em vez de produzir listas;
- explicar por que um valor ausente (`NULL`) é informação e precisa ser tratado de forma deliberada.

Todos os capítulos seguintes dependem de registros: inventários, registros de fluxos de dados, registros de riscos, listas de acesso, logs de evidências. Quando eles vivem em planilhas editadas por muitas pessoas, eles se deterioram — linhas duplicadas, responsáveis em texto livre, "A CONFIRMAR" em campos de data. Este capítulo mostra a modelagem de dados mínima de que um implementador precisa para que os registros operacionais continuem confiáveis.

### 4.1 Entidades, atributos e chaves

Um **modelo de dados** diz que tipos de coisas os registros descrevem (**entidades**: ativo, responsável, contrato de suporte), o que é registrado sobre cada uma (**atributos**: modelo, firmware, local, criticidade) e como elas se relacionam. Cada entidade tem uma **chave primária** — um valor que identifica exatamente um registro, como a etiqueta de um ativo. Uma **chave estrangeira** numa tabela aponta para a chave primária de outra: o `owner_id` de um ativo se refere a uma linha da tabela de responsáveis. Essa única escolha de projeto substitui nomes de responsáveis em texto livre, que derivam ("Water Ops", "water operations", "A. Okafor (saiu)"), por uma referência que ou aponta para um responsável real, ou não aponta.

### 4.2 Restrições: tornar impossíveis os registros impossíveis

Uma **restrição** é uma regra que o banco de dados aplica a cada gravação. `NOT NULL` diz que um valor precisa estar presente; `CHECK (criticality BETWEEN 1 AND 3)` diz que só esses valores são permitidos; uma chave estrangeira diz que a linha referenciada precisa existir (no SQLite, a aplicação das chaves estrangeiras precisa ser ligada em cada conexão, um detalhe que vale conhecer porque surpreende as pessoas). As restrições levam a validação de "alguém deveria conferir" para "o sistema recusa". Elas são a validação de entradas do Capítulo 3 aplicada a registros.

No Laboratório 4, a última consulta é exatamente isso: inserir um ativo com criticidade 7 falha no banco de dados, seja quem for que escreveu o script.

### 4.3 Valores ausentes são constatações

Num inventário, um valor ausente não é um espaço em branco; é uma afirmação de que algo é desconhecido. Um ativo sem responsável é um ativo que ninguém vai corrigir, revisar ou desativar. Um ativo com firmware desconhecido é um cujas vulnerabilidades não podem ser avaliadas. Por isso, as consultas devem procurar *pelos* valores ausentes, e não ignorá-los. O `NULL` do SQL se comporta de modo especial: `owner_id = NULL` nunca é verdadeiro; é preciso escrever `owner_id IS NULL`. Muitos erros silenciosos de relatório vêm de esquecer isso.

O ativo de criticidade 1 sem responsável do Laboratório 4, a RTU da PS-09, só aparece porque a consulta pergunta por ele.

### 4.4 As junções respondem às perguntas reais

As perguntas operacionais costumam abranger várias tabelas. "Quais ativos rodam num modelo cujo suporte do fornecedor terminou?" exige a tabela de ativos unida à tabela de suporte pelo modelo. "Quantos ativos de criticidade 1 cada responsável tem?" exige os ativos unidos aos responsáveis, com uma **junção à esquerda** (left join), para que os ativos sem responsável apareçam como "(none)" em vez de sumirem da contagem. A diferença entre uma junção interna e uma junção à esquerda costuma ser a diferença entre um relatório que esconde um problema e um que o mostra.

### 4.5 Exemplo resolvido: extrato do inventário da FSTS (sintético)

O Laboratório 4 constrói um pequeno inventário num banco SQLite em memória (o módulo `sqlite3` do Python, [documentação](https://docs.python.org/3/library/sqlite3.html)) e faz cinco perguntas. Cada resposta leva a uma ação. A RTU da PS-09 não tem responsável, é de criticidade 1, e o suporte do fornecedor ao seu modelo terminou em 2025-12-31: três motivos para agir, sobre o mesmo ativo, que uma planilha ordenada por local nunca teria reunido. O switch da estação PS-04 tem firmware desconhecido. Dois servidores rodam versões de sistema operacional que estão na própria lista de aposentadoria por política da FSTS. A consulta de criticidade por responsável mostra um ativo de criticidade 1 que não pertence a ninguém. Por fim, uma tentativa de inserir um ativo com criticidade 7 é recusada pela restrição `CHECK`.

### 4.6 Atividade prática: consultas ao inventário

**Laboratório 4** (salve como `lab04.py`, execute com `python3 lab04.py`):

```python
# Lab 4 - an asset inventory as a relational model (offline, standard library only: sqlite3)
# Synthetic: Fallowmere Shared Technology Services inventory extract.
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE owner(id INTEGER PRIMARY KEY, name TEXT NOT NULL, service TEXT NOT NULL);
CREATE TABLE asset(id TEXT PRIMARY KEY, kind TEXT NOT NULL, model TEXT, firmware TEXT,
  site TEXT NOT NULL, owner_id INTEGER REFERENCES owner(id), criticality INTEGER CHECK (criticality BETWEEN 1 AND 3));
CREATE TABLE support(model TEXT PRIMARY KEY, vendor_end TEXT);
INSERT INTO owner VALUES (1,'Water Ops','drinking water'),(2,'Clinical Eng','hospital'),(3,'Depot IT','transit');
INSERT INTO asset VALUES
 ('PS04-PLC','plc','Arlen 300','4.2','PS-04',1,1),('PS07-PLC','plc','Arlen 300','3.9','PS-07',1,1),
 ('PS09-RTU','rtu','Kell R2','1.1','PS-09',NULL,1),('RLY-01','server','generic x86','deb12','Hub',1,1),
 ('HIST-01','server','generic x86','win2016','Hub',1,2),('INF-PUMP-12','infusion','Moro IP5','2.0','Ward 3',2,1),
 ('PACS-GW','server','generic x86','win2012r2','Hospital',2,2),('DEPOT-KIOSK','kiosk','Tella K1','8.1','Depot',3,3),
 ('SW-STN-04','switch','Brack 24',NULL,'PS-04',1,2);
INSERT INTO support VALUES ('Arlen 300','2027-06-30'),('Kell R2','2025-12-31'),('Moro IP5','2029-01-01'),('Tella K1','2026-03-31');
""")
q = {
 "no owner": "SELECT id, site FROM asset WHERE owner_id IS NULL",
 "unknown firmware": "SELECT id, site FROM asset WHERE firmware IS NULL",
 "vendor support ended (as of 2026-10-12)":
   "SELECT a.id, s.vendor_end FROM asset a JOIN support s ON a.model=s.model WHERE s.vendor_end < '2026-10-12'",
 "OS on the service's retire-by-policy list (synthetic)": "SELECT id, firmware FROM asset WHERE firmware IN ('win2012r2','win2016')",
 "criticality-1 assets by owner": """SELECT COALESCE(o.name,'(none)'), COUNT(*) FROM asset a LEFT JOIN owner o
   ON a.owner_id=o.id WHERE a.criticality=1 GROUP BY o.name ORDER BY 2 DESC""",
}
for title, sql in q.items():
    print(f"-- {title}")
    for row in db.execute(sql):
        print("  ", row)
try:
    db.execute("INSERT INTO asset VALUES ('X','plc','m','1','PS-01',1,7)")
except sqlite3.IntegrityError as e:
    print("constraint rejected bad row:", e)
```

Saída esperada (Python 3.13.5):

```text
-- no owner
   ('PS09-RTU', 'PS-09')
-- unknown firmware
   ('SW-STN-04', 'PS-04')
-- vendor support ended (as of 2026-10-12)
   ('PS09-RTU', '2025-12-31')
   ('DEPOT-KIOSK', '2026-03-31')
-- OS on the service's retire-by-policy list (synthetic)
   ('HIST-01', 'win2016')
   ('PACS-GW', 'win2012r2')
-- criticality-1 assets by owner
   ('Water Ops', 3)
   ('Clinical Eng', 1)
   ('(none)', 1)
constraint rejected bad row: CHECK constraint failed: criticality BETWEEN 1 AND 3
```

Leia a saída como uma lista de trabalho, e não como um relatório. A RTU da PS-09 é a primeira linha de trabalho, porque três constatações se encontram num só ativo: sem responsável, criticidade 1 e suporte do fornecedor encerrado em 2025-12-31. O firmware desconhecido do switch da estação PS-04 vira uma pergunta para o engenheiro de Água, e não um palpite. Os dois servidores na lista de aposentadoria por política da FSTS vão para o responsável pela plataforma, com as suas datas de substituição. Por fim, confira a inserção recusada: se a linha de criticidade 7 tivesse sido aceita, a aplicação das chaves estrangeiras e do `CHECK` não estaria ativa naquela conexão, e todas as respostas anteriores mereceriam menos confiança.

### 4.7 Erros comuns e limites

- Campos de texto livre para qualquer coisa que deveria referenciar outro registro (responsáveis, locais, modelos).
- Comparar com `= NULL`, de modo que os valores ausentes sejam excluídos em silêncio.
- Junções internas em relatórios de cobertura, que descartam justamente os registros com vínculos ausentes.
- Guardar datas como texto livre em formatos misturados, de modo que as comparações ordenem errado; guarde em ISO 8601 (`YYYY-MM-DD`), que ordena corretamente como texto.
- Acreditar que o banco de dados é a verdade. Ele é tão bom quanto o processo de descoberta e atualização por trás dele (Capítulo 11).

Um modelo de dados não pode dizer que um ativo existe se ninguém o registrou. Ele pode garantir que o que está registrado seja consistente, e que as lacunas fiquem visíveis.

### Exercícios — capítulo 4

**EX010 — Encontre o ativo escondido.** *Objetivo:* ver uma junção interna esconder um problema. *Entradas:* Laboratório 4. *Restrições:* altere apenas a última consulta. *Etapas:* (1) troque `LEFT JOIN` por `JOIN` na consulta de criticidade por responsável; (2) execute e compare; (3) explique em duas frases qual ativo sumiu e por que isso importa para um relatório de cobertura. *Evidência esperada:* as duas saídas e a explicação. *Rubrica:* 3 = a linha da PS09-RTU some, a contagem total de criticidade 1 cai de 5 para 4, explicação ligada a ativos sem responsável sumindo dos relatórios gerenciais; 2 = observado, explicação fraca; 1 = não executado; 0 = nada.

**EX011 — Acrescente uma restrição e uma tabela.** *Objetivo:* estender o modelo com segurança. *Entradas:* Laboratório 4. *Restrições:* apenas a biblioteca padrão. *Etapas:* (1) acrescente uma tabela `review` (id do ativo, data da revisão, revisor, resultado) com uma chave estrangeira para asset e um `CHECK` de que o resultado é um de `ok`, `issue`, `not-reachable`; (2) habilite as chaves estrangeiras com `PRAGMA foreign_keys = ON`; (3) mostre que inserir uma revisão para um ativo inexistente falha; (4) escreva uma consulta que liste os ativos de criticidade 1 sem revisão nos últimos 90 dias. *Evidência esperada:* código e saída. *Rubrica:* 3 = restrição e chave estrangeira aplicadas, a consulta usa uma junção à esquerda ou `NOT EXISTS` para que os ativos nunca revisados apareçam; 2 = funciona, mas perde os ativos nunca revisados; 1 = só o esquema; 0 = nada.

**EX012 — Da planilha ao modelo.** *Objetivo:* reconhecer falhas de qualidade de dados. *Entradas:* um conjunto sintético de linhas de planilha: `PS-03 PLC | owner: Water Ops | fw: 4.2 | support: Jun 2027`; `PS-03 plc | owner: water operations | fw: ? | support: 30/06/27`; `PS-05 PLC | owner: A. Okafor (left) | fw: 4.1 | support: TBC`. *Restrições:* nenhum código é necessário. *Etapas:* (1) liste todas as falhas de qualidade de dados; (2) diga qual restrição ou escolha de projeto, na orientação do Capítulo 4 sobre chaves, restrições e valores ausentes, impede cada uma. *Evidência esperada:* tabela. *Rubrica:* 3 = ativo duplicado com caixa inconsistente, variantes de responsável em texto livre, uma pessoa em vez de um papel como responsável e alguém que saiu, firmware desconhecido como "?", formatos de data misturados, "TBC" — cada um mapeado para chave primária, chave estrangeira, NOT NULL/desconhecido explícito, datas ISO; 2 = a maioria encontrada; 1 = poucas; 0 = nada.

### Síntese do capítulo

Os registros operacionais só são úteis se continuarem consistentes. Modele-os como entidades com chaves, ligue-os com chaves estrangeiras em vez de texto livre e deixe as restrições recusarem os registros impossíveis. Trate os valores ausentes como constatações, consulte-os explicitamente e use junções à esquerda em qualquer relatório sobre cobertura. Um bom modelo torna as lacunas visíveis; ele não consegue encontrar ativos que ninguém registrou.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 30

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- usar o vocabulário central — ativo, ameaça, vulnerabilidade, exposição, controle, risco, incidente, evidência — com precisão e consistência;
- explicar como as prioridades de segurança num serviço essencial diferem das de um escritório comum: a **disponibilidade e a safety** do serviço físico costumam vir primeiro;
- descrever um controle pelo que ele **previne, detecta ou ajuda a recuperar**, e pela evidência de que ele funciona;
- ler um relatório público de incidente em busca das suas lições sem transformá-lo numa técnica.

Os Capítulos 1–4 trataram de computação. Este capítulo fornece a linguagem comum que você vai usar com operadores, gestores, auditores e fornecedores pelo resto do livro. Palavras imprecisas causam falhas reais: "o CLP é seguro" não significa nada; "o CLP aceita escritas apenas da sub-rede do relay, verificado por uma revisão de fluxos em 3 de outubro" significa alguma coisa.

### 5.1 Termos centrais

- **Ativo**: qualquer coisa de valor para o serviço — um controlador de bomba, um historiador, uma credencial, um conjunto de dados, o conhecimento de uma pessoa.
- **Ameaça**: uma causa potencial de dano — um grupo criminoso, uma mudança descuidada, uma enchente, um fornecedor em dificuldades.
- **Vulnerabilidade**: uma fraqueza que uma ameaça poderia explorar — uma falha sem patch, uma senha compartilhada, um caminho não documentado, um backup não testado.
- **Exposição**: se uma ameaça consegue de fato alcançar a vulnerabilidade. Uma falha sem patch num dispositivo isolado está menos exposta que a mesma falha alcançável a partir da internet.
- **Controle**: uma medida que reduz o risco — técnica (uma regra de firewall), procedimental (uma aprovação de mudança) ou física (um armário trancado).
- **Risco**: a combinação de quão provável é o dano e de quão grave ele seria, para as pessoas que dependem do serviço. O Capítulo 13 torna isso concreto.
- **Incidente**: um evento que de fato prejudica, ou ameaça prejudicar, a confidencialidade, a integridade ou a disponibilidade — ou, na infraestrutura crítica, a safety.
- **Evidência**: um registro que permite a outra pessoa, que não você, conferir uma afirmação.

O Cybersecurity Framework 2.0 do NIST organiza os resultados em Govern, Identify, Protect, Detect, Respond e Recover ([NIST CSWP 29](https://doi.org/10.6028/NIST.CSWP.29)); ele é um mapa útil do território, e não uma lista de verificação para ticar.

### 5.2 Prioridades num serviço essencial

A segurança da TI de escritório costuma ser descrita em termos de confidencialidade, integridade e disponibilidade, com a confidencialidade em primeiro lugar. Numa rede de água, num hospital ou num sistema de transporte, a ordem muda. A primeira preocupação costuma ser que o serviço físico continue e que ninguém se machuque; a integridade dos dados de controle e de medição vem logo atrás (um operador agindo sobre uma leitura falsa pode causar dano); a confidencialidade importa — prontuários de pacientes, dados de clientes, diagramas de rede —, mas raramente vale uma interrupção. O guia de TO do NIST discute como essas prioridades diferem para a tecnologia operacional ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

Isso tem consequências práticas para um implementador. Um controle que pode parar um processo (um bloqueio automático numa estação de operador, uma reinicialização forçada para aplicar um patch) precisa de uma aprovação e de um momento diferentes na TO em relação a um escritório. Um controle que falha "fechado" na TI pode precisar falhar "aberto" num sistema relevante para a safety — e essa escolha precisa ser feita de forma deliberada por pessoas que entendem o processo, e não por padrão na configuração de um fornecedor.

### 5.3 Prevenir, detectar, recuperar

Classificar os controles pela função ajuda a ver lacunas. Os controles **preventivos** impedem que algo aconteça (autenticação, segmentação, allowlists). Os controles **detectivos** notam que está acontecendo (alertas, verificações de integridade, revisões). Os controles **corretivos** ou **de recuperação** restauram o serviço (backups, equipamentos sobressalentes, procedimentos de operação manual). Um serviço protegido apenas por controles preventivos não tem como notar quando eles falham; um com apenas controles detectivos nota o dano sem conseguir pará-lo ou desfazê-lo. Todo risco importante deve ter pelo menos um controle de cada tipo, e todo controle deve ter uma **evidência** declarada que mostre que ele funciona — e não apenas que está configurado.

### 5.4 Ler incidentes públicos

Os relatórios públicos de incidentes são o melhor material didático que a área tem, se lidos corretamente. Leia-os em busca das **premissas que falharam** e das **lições**: no que o operador acreditava que não era verdade? O alerta da CISA sobre o evento de 2021 na estação de tratamento de água de Oldsmar, na Flórida, descreveu software de acesso remoto, senhas compartilhadas e um sistema conectado à internet como condições a corrigir ([CISA AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)); um ex-funcionário municipal disse depois que o evento provavelmente foi erro de um empregado, e não uma intrusão ([WUSF, 13 de abril de 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). Os dois relatos ensinam a mesma lição ao implementador: o acesso remoto a um sistema de controle com credenciais compartilhadas e logs fracos torna impossível saber depois o que aconteceu. Note também a lição sobre evidência — um primeiro relato pode ser revisto.

### 5.5 Exemplo resolvido: reescrever afirmações vagas (sintético)

Um relatório de situação da FSTS diz: "O LANTERN é seguro. Os firewalls estão instalados. Os backups são feitos. O monitoramento está ativo." Reescrito no vocabulário deste capítulo, com evidências:

| Afirmação vaga | Afirmação precisa | Evidência |
|---|---|---|
| "O LANTERN é seguro" | (não é uma afirmação utilizável — remover) | — |
| "Os firewalls estão instalados" | As estações aceitam Modbus apenas da sub-rede do relay (preventivo). | Revisão de fluxos em 3 out.; um caminho corporativo→PS-04 não declarado encontrado e fechado (CHG-121). |
| "Os backups são feitos" | As configurações do relay e do historiador têm backup toda noite; os dados do historiador, toda semana (recuperação). | Último teste de restauração em 28 set.: historiador restaurado em 3 h 10 min, contra uma meta de 4 h. |
| "O monitoramento está ativo" | Rajadas de falhas de login, Modbus corporativo→estação e silêncio de estação geram alertas (detectivo). | Testes das regras em 1 out.: 12/12, 7/10, 8/8 detectados (Capítulo 23). |

### 5.6 Atividade prática: um cartão de controle

Escolha um controle do LANTERN dos Capítulos 2–4 (por exemplo, o validador de mensagens). Escreva um **cartão de controle** de uma página: nome; risco que ele trata; tipo (prevenir / detectar / recuperar); onde está implementado; responsável; como ele poderia falhar; evidência de que funciona; data da última evidência. Você vai estender esses cartões no Capítulo 18.

Para o validador de mensagens, um cartão completo fica assim: risco, mensagens de estação forjadas, reproduzidas ou malformadas chegando ao historiador; tipo, prevenir; implementado no caminho de entrada do relay; responsável, FSTS Platform; poderia falhar se o estado de reprodução se perder numa reinicialização ou se a allowlist ficar atrás de uma estação nova, como a PS-11; evidência, as três aceitações, seis rejeições e duas quarentenas do Laboratório 3, mais as contagens de rejeição do relay; última evidência, a data da execução mais recente.

### 5.7 Erros comuns e limites

- Usar "seguro" como um estado, em vez de descrever proteções específicas e as suas evidências.
- Tratar a confidencialidade como a prioridade máxima num sistema de controle e aceitar o risco de interrupção para protegê-la.
- Contar controles em vez de perguntar o que cada um previne, detecta ou recupera.
- Ler relatórios de incidentes como guias de como fazer, ou repetir um primeiro relato depois que ele foi revisto.
- Chamar todo evento de incidente, o que esgota os respondedores; ou não chamar nada de incidente, o que atrasa a resposta.

Três deles aparecem no relatório de situação deste capítulo antes de ser reescrito. "O LANTERN é seguro" é o primeiro erro. "Os firewalls estão instalados" conta um controle sem dizer que um caminho corporativo→PS-04 não declarado precisou ser fechado sob a CHG-121. "O monitoramento está ativo" escondia que a Regra B detectou apenas 7 de 10 testes.

### Exercícios — capítulo 5

**EX013 — Precisão dos termos.** *Objetivo:* usar o vocabulário corretamente. *Entradas:* a frase "A conta do fornecedor é uma ameaça porque a RTU é um risco sem controle." *Restrições:* reescreva em no máximo três frases. *Etapas:* (1) identifique cada termo mal usado; (2) reescreva corretamente usando ativo, vulnerabilidade, exposição, ameaça e controle. *Evidência esperada:* texto reescrito com uma nota de uma linha por correção. *Rubrica:* 3 = conta do fornecedor identificada como vulnerabilidade ou caminho de exposição (não uma ameaça), RTU como ativo, risco descrito como probabilidade e consequência, um controle ausente concreto nomeado; 2 = quase tudo certo; 1 = mudanças cosméticas; 0 = nada.

**EX014 — Prevenir, detectar, recuperar.** *Objetivo:* ver lacunas de controle pela função. *Entradas:* risco: "uma mudança de configuração no relay faz com que dados das estações sejam descartados". *Restrições:* um controle por função, implementável pela FSTS. *Etapas:* (1) proponha um controle preventivo, um detectivo e um de recuperação; (2) dê, para cada um, uma evidência de que funciona. *Evidência esperada:* tabela de três linhas. *Rubrica:* 3 = por exemplo, aprovação de mudança com revisão por pares (prevenir), alerta de integridade de arquivos e alerta de silêncio de estação (detectar), configuração versionada com rollback testado (recuperar), cada um com evidência testável; 2 = um fraco; 1 = todos preventivos; 0 = nada.

**EX015 — Leitura de relatório de incidente.** *Objetivo:* extrair lições para o implementador de uma fonte pública. *Entradas:* CISA AA21-042A e o artigo da WUSF. *Restrições:* apenas lições; nenhuma técnica de ataque. *Etapas:* (1) liste três condições que o alerta recomendou corrigir; (2) diga o que o relato posterior muda e o que não muda; (3) escreva uma regra de projeto do LANTERN que cada lição apoia. *Evidência esperada:* nota de meia página citando as duas fontes. *Rubrica:* 3 = condições como software de acesso remoto, credenciais compartilhadas e exposição à internet tiradas corretamente do alerta; reconhece que a revisão muda a atribuição, e não o valor das lições de higiene; regras de projeto específicas; 2 = um elemento fraco; 1 = repete o primeiro relato como fato firmado; 0 = nada.

### Síntese do capítulo

Um vocabulário preciso é um controle de segurança: ele torna as afirmações verificáveis. Nos serviços essenciais, a continuidade e a safety do serviço físico costumam vir primeiro, o que muda como os controles são escolhidos, programados e autorizados a falhar. Descreva todo controle pelo que ele previne, detecta ou recupera, e pela evidência de que funciona. Leia os incidentes públicos em busca das premissas que falharam, e acompanhe as revisões.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 30

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- endurecer um servidor removendo o que ele não precisa e restringindo o que ele precisa;
- executar um serviço sob uma conta dedicada e sem privilégios, com apenas os arquivos e as portas de que ele precisa;
- construir e usar uma **linha de base de integridade de arquivos** para detectar mudanças não aprovadas;
- explicar o que a virtualização muda para a segurança — e o que ela não muda.

Os relays e o historiador do LANTERN são servidores comuns. A maioria dos comprometimentos desses servidores, e muitas interrupções, não vêm de falhas exóticas, mas de coisas deixadas neles: um serviço não usado escutando em todas as interfaces, uma opção de depuração, um arquivo gravável por todos, uma conta antiga. Este capítulo trata de manter um servidor pequeno, conhecido e verificável.

### 6.1 Endurecimento como subtração

**Endurecer** (hardening) significa reduzir um sistema ao que a sua função exige e configurar com segurança o que sobra. O guia de segurança de servidores do NIST recomenda remover ou desabilitar serviços, aplicações e protocolos de rede desnecessários, configurar a autenticação e os controles de recursos, e manter o sistema com patches e monitorado ([NIST SP 800-123](https://csrc.nist.gov/pubs/sp/800/123/final)). Para um relay, isso significa: nenhum ambiente de desktop, nenhum compilador, nenhum serviço de compartilhamento de arquivos, SSH escutando apenas na interface de gerenciamento, o processo do relay escutando apenas no seu endereço e porta declarados, e nada escutando em `0.0.0.0` sem um motivo registrado por escrito.

### 6.2 Contas de serviço e menor privilégio

Execute cada serviço com a sua própria conta sem privilégios (`relay`, e não `root`). Dê a essa conta acesso de leitura à sua configuração, acesso de escrita apenas aos seus próprios diretórios de dados e de logs, e nenhum login de shell. Use o gerenciador de serviços do sistema operacional para reiniciá-lo em caso de falha e para aplicar restrições adicionais (por exemplo, uma visão somente leitura da maior parte do sistema de arquivos). Se o processo do relay um dia for comprometido, essas escolhas determinam se o atacante fica com um serviço ou com o host inteiro.

No RLY-01, essa é a definição de serviço cujas permissões mudaram para `0666`.

### 6.3 Os arquivos de configuração são relevantes para a segurança

Num relay, os arquivos mais relevantes para a segurança são a sua configuração (onde ele escuta, para onde encaminha, onde fica a sua chave), a sua allowlist de estações e a sua definição de serviço (com qual conta ele roda, com quais restrições). Uma mudança em qualquer um deles muda a segurança do serviço. As permissões dos arquivos importam tanto quanto o conteúdo: uma definição de serviço que passou a ser gravável por qualquer usuário permite que qualquer usuário local decida o que roda como o serviço.

O RLY-01 mostrou os dois tipos: uma mudança de conteúdo, `debug_listen 0.0.0.0:9000`, e uma mudança de permissão para `0666`.

### 6.4 Linhas de base de integridade de arquivos

Uma **linha de base de integridade de arquivos** registra um hash criptográfico e as permissões de cada arquivo importante num momento sabidamente bom. Os retratos posteriores são comparados com ela; toda diferença ou é explicada por um registro de mudança aprovado, ou é investigada. O SHA-256, especificado na [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final), é uma escolha padrão: qualquer mudança no conteúdo do arquivo muda o seu digest. A própria linha de base precisa ser protegida — guardada fora do host ou assinada —, porque um atacante que consegue mudar um arquivo e a linha de base consegue esconder a mudança.

### 6.5 Virtualização

A virtualização executa vários sistemas operacionais num único host físico por meio de um **hipervisor**. Ela ajuda a operação — snapshots, reconstruções rápidas, convidados separados para funções separadas — e cria coisas novas a proteger. O guia do NIST sobre virtualização completa observa que o hipervisor e as suas interfaces de gerenciamento se tornam alvos de alto valor, e que os convidados num mesmo host compartilham recursos físicos e podem afetar uns aos outros ([NIST SP 800-125](https://csrc.nist.gov/pubs/sp/800/125/final)). Consequências práticas: a rede de gerenciamento do hipervisor é uma zona própria; quem administra o hipervisor administra, na prática, todos os convidados; os snapshots contêm segredos e precisam ser protegidos como backups; e colocar um relay voltado às estações e um servidor de relatórios voltado ao corporativo no mesmo host une duas zonas por meio de hardware compartilhado e de um administrador compartilhado.

### 6.6 Exemplo resolvido: uma linha de base pega um listener de depuração (sintético)

Você faz a linha de base dos três arquivos de configuração do RLY-01. Uma semana depois, a comparação mostra quatro diferenças. A allowlist ganhou `PS-11` sob a mudança aprovada CHG-118 — explicada. A configuração do relay ganhou `debug_listen 0.0.0.0:9000` sem registro de mudança: alguém habilitou uma porta de depuração em todas as interfaces, talvez durante uma resolução de problemas, e a deixou. As permissões da definição de serviço mudaram de `0640` para `0666`: qualquer usuário local agora pode reescrevê-la. Um novo arquivo `helper.sh` apareceu no diretório de units. Três mudanças não aprovadas num host crítico são uma investigação, e não uma arrumação: antes de reverter qualquer coisa, preserve os arquivos atuais e a saída da comparação, e pergunte quem mudou o quê (Capítulo 20).

### 6.7 Atividade prática: linha de base de integridade de arquivos

**Laboratório 6** (salve como `lab06.py`, execute com `python3 lab06.py`):

```python
# Lab 6 - a file-integrity baseline for the relay host's configuration (offline, standard library only)
# Synthetic files are created in a temporary directory; nothing outside it is read or changed.
import hashlib, json, os, tempfile
def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()
def snapshot(root):
    out = {}
    for d, _, files in os.walk(root):
        for name in sorted(files):
            p = os.path.join(d, name)
            st = os.stat(p)
            out[os.path.relpath(p, root)] = {"sha256": digest(p), "mode": oct(st.st_mode & 0o777)}
    return out
with tempfile.TemporaryDirectory() as root:
    files = {"relay.conf": "listen 10.30.0.5:8443\nupstream hist-01:443\nhmac_key_file /etc/relay/key\n",
             "allow.list": "PS-04\nPS-07\nPS-09\n", "units/relay.service": "[Service]\nUser=relay\n"}
    for rel, text in files.items():
        p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f: f.write(text)
        os.chmod(p, 0o640)
    base = snapshot(root)
    print("baseline entries:", len(base), "| relay.conf", base["relay.conf"]["sha256"][:16])
    # simulated changes: one approved (change ticket CHG-118), one not, one permission change, one new file
    with open(os.path.join(root, "allow.list"), "a") as f: f.write("PS-11\n")
    with open(os.path.join(root, "relay.conf"), "a") as f: f.write("debug_listen 0.0.0.0:9000\n")
    os.chmod(os.path.join(root, "units/relay.service"), 0o666)
    with open(os.path.join(root, "units/helper.sh"), "w") as f: f.write("#!/bin/sh\n")
    approved = {"allow.list": "CHG-118"}
    now = snapshot(root)
    for rel in sorted(set(base) | set(now)):
        b, n = base.get(rel), now.get(rel)
        if b == n: continue
        kind = "added" if b is None else "removed" if n is None else "content" if b["sha256"] != n["sha256"] else "mode " + b["mode"] + "->" + n["mode"]
        print(f"{rel:<20} {kind:<16} {'approved ' + approved[rel] if rel in approved else 'UNAPPROVED - investigate'}")
    print("baseline json bytes:", len(json.dumps(base, sort_keys=True)))
```

Saída esperada (Python 3.13.5):

```text
baseline entries: 3 | relay.conf 1defd9289ede0120
allow.list           content          approved CHG-118
relay.conf           content          UNAPPROVED - investigate
units/helper.sh      added            UNAPPROVED - investigate
units/relay.service  mode 0o640->0o666 UNAPPROVED - investigate
baseline json bytes: 342
```

O script cria os seus arquivos num diretório temporário, então você pode executá-lo em qualquer lugar. Note que o digest impresso para `relay.conf` depende apenas do conteúdo do arquivo: se você mudar um caractere do conteúdo sintético no script, o digest muda por completo.

Compare a saída com a semana do RLY-01 descrita acima: quatro diferenças, das quais apenas a entrada `PS-11` da allowlist, sob a CHG-118, tem registro de mudança. Depois faça uma edição sua dentro do script, por exemplo acrescentar uma segunda linha de depuração ou mudar um modo de `0640` para `0644`, execute-o de novo e confirme que a comparação relata exatamente essa diferença e nada mais. Uma linha de base que relata mais ou menos do que você mudou ainda não é confiável o bastante para servir de evidência numa investigação.

### 6.8 Erros comuns e limites

- Endurecer uma vez, na construção, e nunca mais conferir.
- Executar serviços como root "porque foi mais fácil fazer funcionar".
- Manter a linha de base de integridade no mesmo host, gravável pelos mesmos administradores.
- Alertar sobre toda mudança de arquivo num sistema movimentado, de modo que os alertas sejam ignorados; faça a linha de base dos arquivos que importam.
- Tratar um snapshot como backup sem testar a restauração, ou deixar desprotegidos snapshots com chaves dentro.
- Colocar convidados de zonas diferentes num mesmo hipervisor sem registrar que as zonas agora compartilham uma falha e um administrador.

A integridade de arquivos detecta mudanças; ela não diz se a mudança foi maliciosa, e nada diz sobre mudanças em memória ou em arquivos que você não incluiu na linha de base.

### Exercícios — capítulo 6

**EX016 — Revisão de endurecimento.** *Objetivo:* aplicar o endurecimento como subtração. *Entradas:* uma listagem sintética do RLY-02: escutando em `0.0.0.0:22`, `10.30.0.6:8443`, `0.0.0.0:9000`, `0.0.0.0:111`; os pacotes instalados incluem um compilador e um ambiente de desktop; o relay roda como `root`. *Restrições:* apenas proponha mudanças; cada uma precisa de um motivo. *Etapas:* (1) liste todas as mudanças; (2) marque quais precisam de um ticket de mudança e quais podem ser feitas na próxima mudança padrão. *Evidência esperada:* tabela. *Rubrica:* 3 = SSH vinculado à interface de gerenciamento, depuração 9000 removida, porta 111 (RPC) desabilitada, compilador e desktop removidos, relay movido para uma conta sem privilégios com restrições; classificação sensata das mudanças; 2 = a maioria; 1 = genérico; 0 = nada.

**EX017 — Proteja a linha de base.** *Objetivo:* projetar o armazenamento da linha de base. *Entradas:* Laboratório 6. *Restrições:* dois projetos. *Etapas:* (1) descreva guardar a linha de base fora do host, num local de gravação única; (2) descreva assinar a linha de base com uma chave que não fica no relay; (3) compare contra o que cada um protege. *Evidência esperada:* meia página. *Rubrica:* 3 = os dois projetos corretos; observa que um atacante com root no relay consegue mudar arquivos, mas não consegue mudar sem ser detectado uma linha de base fora do host ou assinada; observa que a ferramenta de comparação no próprio host pode ser subvertida, então a comparação também deve rodar de fora; 2 = um projeto; 1 = vago; 0 = nada.

**EX018 — Posicionamento no hipervisor.** *Objetivo:* raciocinar sobre plataformas compartilhadas. *Entradas:* proposta de executar o RLY-01 (voltado às estações), o HIST-01 (voltado ao corporativo) e o gateway clínico do hospital como convidados num único hipervisor da FSTS, para economizar. *Restrições:* não rejeite automaticamente; declare condições. *Etapas:* (1) liste o que as zonas passariam a compartilhar; (2) liste as condições sob as quais você aceitaria; (3) nomeie o risco residual e o seu dono. *Evidência esperada:* uma página. *Rubrica:* 3 = hardware, administradores do hipervisor, rede de gerenciamento e armazenamento compartilhados, e um ponto único de falha atravessando dois setores; condições como zona de gerenciamento separada, grupo de administradores restrito com MFA, redes virtuais separadas sem ponte, folga de capacidade documentada e um plano para a perda do host; risco residual assumido por donos de serviço nomeados; 2 = parcial; 1 = sim/não seco; 0 = nada.

### Síntese do capítulo

Mantenha os servidores pequenos e conhecidos: remova o que a função não precisa, execute os serviços sob contas dedicadas e sem privilégios, vincule os listeners a endereços declarados e trate os arquivos de configuração e as suas permissões como relevantes para a segurança. Faça a linha de base dos arquivos que importam com um hash criptográfico, proteja a linha de base e investigue toda diferença sem explicação. A virtualização simplifica a operação, mas concentra o controle no hipervisor e nos seus administradores; registre quais zonas compartilham um host.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 30

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- distinguir identificação, autenticação e autorização, e dizer qual controle atua em cada etapa;
- escolher a força da autenticação pelo que uma conta pode fazer, e não por quem a detém;
- gerenciar os quatro tipos de conta encontrados em todo serviço crítico — pessoal, privilegiada, de serviço e de fornecedor — e as contas compartilhadas que não deveriam existir;
- conduzir uma **revisão de acessos** que compara as contas com uma lista de pessoal oficial e com uma declaração de necessidade.

Nos relatórios de incidentes do Capítulo 5, o acesso é um fio recorrente: acesso remoto com senhas compartilhadas, contas de fornecedores que nunca foram removidas. Para um implementador, identidade não é um produto; é um conjunto de registros e rotinas que precisam continuar precisos à medida que as pessoas entram, mudam de função e saem.

### 7.1 Identificar, autenticar, autorizar

**Identificação** é alegar uma identidade ("sou b.lind"). **Autenticação** é prová-la — com algo que você sabe (uma senha), tem (uma chave de hardware, um aplicativo autenticador) ou é (uma biometria). **Autorização** é decidir o que essa identidade pode fazer. As diretrizes de identidade digital do NIST descrevem os tipos de autenticador e os níveis de garantia, e recomendam autenticação multifator resistente a phishing para acessos de maior garantia ([NIST SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)). Na prática: todo acesso privilegiado ou remoto a um host do LANTERN exige autenticação multifator (MFA), e o fator deve resistir a phishing onde a plataforma permitir.

### 7.2 Tipos de conta

- **Contas pessoais** pertencem a uma pessoa e são o padrão para todo ser humano.
- **Contas privilegiadas** podem mudar configurações, contas ou parâmetros de segurança. Devem ser separadas da conta do dia a dia da pessoa, exigir MFA e ser poucas.
- **Contas de serviço** são usadas por software (o relay gravando no historiador). Devem ter apenas as permissões de que o software precisa, nenhum login interativo, e credenciais que são rotacionadas e guardadas num lugar protegido — não num script.
- **Contas de fornecedor** dão acesso a uma parte externa. Devem ser **limitadas no tempo**: habilitadas para um trabalho específico, monitoradas enquanto em uso e desabilitadas depois.
- **Contas compartilhadas** ("opsuser") são usadas por várias pessoas. Elas destroem a responsabilização — o log diz que "opsuser" fez — e as suas senhas vazam a cada pessoa que sai. Onde um dispositivo realmente não suporta contas individuais, controle a credencial compartilhada num cofre que registre quem a retirou, e quando.

### 7.3 O processo de entrada, mudança e saída

As contas dão errado nas transições. Quem **entra** recebe acessos copiados de um colega e herda privilégios de que não precisa. Quem **muda** de função mantém os acessos antigos ao ganhar os novos. As contas de quem **sai** continuam habilitadas porque ninguém avisou o dono do sistema. A correção é um processo ligado a uma fonte oficial — a lista de pessoal do RH — e uma **revisão de acessos** periódica que pegue o que o processo deixou passar.

A exportação do Laboratório 7 mostra as três falhas: `c.mendes` é alguém que saiu e cuja conta continuou habilitada depois de 31 de agosto, `d.reyes` mantém administração do historiador de que a Engenharia Clínica não precisa, e `vendor-kell` é um acesso permanente de fornecedor nunca ligado a um ticket.

### 7.4 A revisão de acessos

Uma revisão de acessos compara três coisas: as **contas** que existem num sistema (exportadas dele, e não da memória), a **lista de pessoal**, com as pessoas e a sua situação, e uma declaração de **necessidade** — quais papéis cada equipe exige em cada sistema. As constatações caem em tipos reconhecíveis: órfãs (contas sem pessoa correspondente), pessoas que saíram e continuam habilitadas (pior se usadas depois da saída), papéis injustificados, acesso privilegiado sem MFA, contas dormentes, contas compartilhadas e acesso permanente de fornecedor.

Para o RLY-01 e o HIST-01, a exportação lista nove contas, e a lista de pessoal diz que `f.ito` não corresponde a ninguém.

### 7.5 Exemplo resolvido: revisão trimestral do RLY-01 e do HIST-01 (sintético)

A exportação tem nove contas; o Laboratório 7 encontra nove constatações em cinco delas. Duas exigem ação imediata, e não um ticket no próximo trimestre. `c.mendes` saiu em 31 de agosto e a conta foi **usada em 14 de setembro**: isso é um potencial incidente, e não uma arrumação administrativa — preserve os logs, desabilite a conta e pergunte se outra pessoa usou as credenciais (Capítulo 20). `vendor-kell` é uma conta de administrador permanente no relay, sem MFA, ociosa há 85 dias. As outras constatações são sérias, mas rotineiras: `d.reyes` tem administração no historiador, de que a Engenharia Clínica não precisa, sem MFA, e não faz login há 224 dias; `opsuser` é um administrador compartilhado sem MFA; `f.ito` nem está na lista de pessoal — talvez um terceirizado registrado em outro lugar, talvez uma conta que ninguém consegue explicar.

Note o que o script *não* sinaliza: `svc-relay` não tem MFA, o que é normal para uma conta de serviço, mas o armazenamento e a rotação da sua credencial não são visíveis nesta exportação e precisam ser conferidos à parte.

### 7.6 Atividade prática: revisão de acessos

**Laboratório 7** (salve como `lab07.py`, execute com `python3 lab07.py`):

```python
# Lab 7 - quarterly access review for the relay and historian (offline, standard library only)
# Synthetic account export and HR roster; "today" is 2026-10-12.
from datetime import date
today = date(2026, 10, 12)
roster = {"a.okafor": ("Water Ops", "active"), "b.lind": ("FSTS Security", "active"),
          "c.mendes": ("Water Ops", "left 2026-08-31"), "d.reyes": ("Clinical Eng", "active"),
          "e.strand": ("FSTS Platform", "active")}
accounts = [  # name, system, role, last_login, mfa, kind
    ("a.okafor", "HIST-01", "operator", "2026-10-10", True, "person"),
    ("b.lind", "RLY-01", "admin", "2026-10-11", True, "person"),
    ("c.mendes", "HIST-01", "engineer", "2026-09-14", True, "person"),
    ("d.reyes", "HIST-01", "admin", "2026-03-02", False, "person"),
    ("e.strand", "RLY-01", "admin", "2026-10-01", True, "person"),
    ("opsuser", "HIST-01", "admin", "2026-10-11", False, "shared"),
    ("svc-relay", "HIST-01", "writer", "2026-10-12", False, "service"),
    ("vendor-kell", "RLY-01", "admin", "2026-07-19", False, "vendor"),
    ("f.ito", "RLY-01", "operator", "2026-10-05", True, "person")]
need = {("Water Ops", "HIST-01"): {"operator", "engineer"}, ("FSTS Security", "RLY-01"): {"admin"},
        ("FSTS Platform", "RLY-01"): {"admin"}, ("Clinical Eng", "HIST-01"): set()}
findings = []
for name, sysid, role, last, mfa, kind in accounts:
    idle = (today - date.fromisoformat(last)).days
    if kind == "person":
        if name not in roster: findings.append((name, sysid, "not on HR roster (orphan)"))
        else:
            dept, status = roster[name]
            if status != "active": findings.append((name, sysid, f"leaver ({status}) still enabled; used after leaving" if last > status[5:] else f"leaver ({status})"))
            elif role not in need.get((dept, sysid), set()): findings.append((name, sysid, f"role {role} not justified for {dept}"))
    if kind == "shared": findings.append((name, sysid, "shared account: no individual accountability"))
    if kind == "vendor" and idle > 30: findings.append((name, sysid, f"vendor account standing, idle {idle} d: make time-bound"))
    if role == "admin" and not mfa and kind != "service": findings.append((name, sysid, "privileged without MFA"))
    if idle > 90 and kind == "person": findings.append((name, sysid, f"dormant {idle} d"))
for f in findings: print(f"{f[0]:<12} {f[1]:<8} {f[2]}")
print("accounts:", len(accounts), "findings:", len(findings), "accounts with >=1 finding:", len({f[0] for f in findings}))
```

Saída esperada (Python 3.13.5):

```text
c.mendes     HIST-01  leaver (left 2026-08-31) still enabled; used after leaving
d.reyes      HIST-01  role admin not justified for Clinical Eng
d.reyes      HIST-01  privileged without MFA
d.reyes      HIST-01  dormant 224 d
opsuser      HIST-01  shared account: no individual accountability
opsuser      HIST-01  privileged without MFA
vendor-kell  RLY-01   vendor account standing, idle 85 d: make time-bound
vendor-kell  RLY-01   privileged without MFA
f.ito        RLY-01   not on HR roster (orphan)
accounts: 9 findings: 9 accounts with >=1 finding: 5
```

Ordene as nove constatações pelo que precisa acontecer hoje. `c.mendes`, usada em 14 de setembro depois da saída em 31 de agosto, vai para o processo de incidentes: preserve os logs de autenticação antes de desabilitar a conta. `vendor-kell`, um administrador permanente no relay sem MFA e com 85 dias de ociosidade, é desabilitada e reabilitada apenas mediante ticket. `d.reyes`, `opsuser` e `f.ito` viram tickets com responsáveis. Depois procure o que o script não consegue ver, como a forma de guardar a credencial de `svc-relay` e quando ela foi rotacionada pela última vez.

### 7.7 Erros comuns e limites

- Revisar contas a partir de uma lista que alguém digitou, em vez de uma exportação do sistema.
- Copiar os acessos de um colega para quem entra.
- Tratar como item de arrumação a conta de quem saiu que foi *usada* depois da saída.
- Dar às contas de fornecedor acesso permanente "para ganhar tempo numa emergência"; projete, em vez disso, um processo de habilitação rápido e registrado.
- Exigir MFA para as pessoas, mas deixar os segredos das contas de serviço em scripts em texto claro.
- Remover uma conta compartilhada num dispositivo de controle antes de confirmar como os operadores vão fazer login durante uma emergência.

Uma revisão de acessos mostra o estado das contas num momento. Ela não mostra como as credenciais são usadas, o que exige logs (Capítulo 17), e é tão boa quanto a lista de pessoal e a declaração de necessidade.

### Exercícios — capítulo 7

**EX019 — Priorize as constatações.** *Objetivo:* separar incidentes de arrumação. *Entradas:* a saída do Laboratório 7. *Restrições:* três faixas de prioridade: hoje, esta semana, este trimestre. *Etapas:* (1) ponha cada constatação numa faixa; (2) para cada item de "hoje", escreva as duas primeiras ações, em ordem. *Evidência esperada:* tabela. *Rubrica:* 3 = c.mendes usada depois da saída e o administrador permanente do fornecedor sem MFA em "hoje", com "preservar os logs" antes de "desabilitar" para c.mendes e confirmação com a Kell antes de desabilitar onde a operação depender dela; d.reyes e opsuser nesta semana; f.ito investigada nesta semana; 2 = faixas sensatas, ações na ordem errada; 1 = tudo "hoje"; 0 = nada.

**EX020 — Acesso de fornecedor limitado no tempo.** *Objetivo:* projetar um processo de habilitação de fornecedor. *Entradas:* a Kell Instruments precisa de acesso de administrador ao relay cerca de quatro vezes por ano, às vezes com urgência, à noite. *Restrições:* precisa ser utilizável às 03:00 pelo tecnólogo de plantão; precisa deixar evidência. *Etapas:* (1) descreva solicitação, aprovação, habilitação, monitoramento e desabilitação; (2) declare o tempo máximo para habilitar; (3) diga qual evidência é mantida. *Evidência esperada:* procedimento de no máximo dez etapas. *Rubrica:* 3 = solicitação ligada a um ticket, aprovação do plantão com a operação informada, conta habilitada por uma janela fixa com MFA, sessão gravada ou registrada, expiração automática, revisão no dia útil seguinte; 2 = falta a expiração ou a evidência; 1 = "habilitar quando pedirem"; 0 = nada.

**EX021 — Estenda a revisão.** *Objetivo:* acrescentar uma verificação à ferramenta. *Entradas:* Laboratório 7. *Restrições:* apenas a biblioteca padrão. *Etapas:* (1) acrescente uma verificação que sinalize qualquer pessoa com administração tanto no RLY-01 quanto no HIST-01 (uma concentração de privilégio); (2) acrescente uma conta `b.lind` no `HIST-01` como `admin`, com MFA e a data de hoje como último login; (3) execute e relate a nova constatação. *Evidência esperada:* código e saída. *Rubrica:* 3 = verificação implementada sobre a lista inteira de contas, b.lind sinalizada, nenhum falso alarme; também observa que a nova conta é ela mesma injustificada, porque a FSTS Security não tem necessidade declarada no HIST-01; 2 = funciona sem notar a constatação de necessidade; 1 = não executado; 0 = nada.

### Síntese do capítulo

Identidade é um conjunto de registros e rotinas. Autentique pelo que a conta pode fazer; separe contas pessoais, privilegiadas, de serviço e de fornecedor, e remova as compartilhadas ou controle-as num cofre; ligue as contas ao processo de entrada, mudança e saída; e revise-as com regularidade contra uma exportação, uma lista de pessoal e uma declaração de necessidade. Algumas constatações da revisão — a conta de quem saiu usada depois da saída — são incidentes, e a evidência vem antes da limpeza.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 30

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- ler e desenhar uma arquitetura de **zonas e conduítes** para um serviço, incluindo os caminhos de gerenciamento;
- aplicar a defesa em profundidade e o menor privilégio, para que um controle que falha não seja um serviço que falha;
- projetar para a **operabilidade**: manutenção, acesso de emergência e modos de falha como parte da arquitetura;
- reconhecer os atalhos arquiteturais que desgastam a separação ao longo do tempo.

O Capítulo 2 comparou os fluxos observados com os conduítes declarados. Este capítulo trata da própria declaração: por que o LANTERN tem a forma que tem, e o que um implementador precisa proteger ao construí-lo. Você raramente vai projetar sozinho um sistema crítico inteiro, mas vai tomar dezenas de pequenas decisões que preservam o projeto ou o desfazem em silêncio.

### 8.1 Zonas, conduítes e a direção da confiança

No LANTERN, os dados fluem *para cima*: estações → relay → historiador → relatórios. Os comandos para as estações não passam pelo LANTERN de forma alguma; os operadores controlam as estações a partir do sistema separado da sala de controle. Essa é a propriedade mais importante do projeto. Se o relay for comprometido, um atacante pode falsificar ou bloquear a telemetria — algo sério —, mas não pode comandar uma bomba por meio dele. Toda mudança proposta deve ser conferida contra essa propriedade: "isto cria um caminho para que comandos, ou sistemas corporativos, alcancem a zona das estações?"

A segmentação das redes de controle em relação às redes de negócio, com caminhos controlados e monitorados entre elas, é uma orientação consistente entre as fontes de segurança de TO ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [visão geral da ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Os firewalls implementam isso; a orientação do NIST sobre firewalls recomenda políticas de negação por padrão que permitam apenas o tráfego necessário ([NIST SP 800-41 Rev. 1](https://csrc.nist.gov/pubs/sp/800/41/r1/final)).

### 8.2 Defesa em profundidade e menor privilégio

**Defesa em profundidade** significa vários controles independentes, para que uma falha não leve direto ao dano. Para que uma mensagem de telemetria forjada engane um operador, ela teria de alcançar o relay (segmentação), carregar um código de autenticação válido (Capítulo 15), passar na validação (Capítulo 3) e evitar os alertas de valores implausíveis (Capítulo 19). Cada camada precisa ser *independente*: dois controles que dependem da mesma senha são um controle só.

O **menor privilégio** — dar a cada usuário e processo apenas o acesso de que ele precisa — aparece nos princípios clássicos de projeto de Saltzer e Schroeder ([Saltzer e Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939)), junto com os padrões à prova de falha e a economia de mecanismo. Para um implementador, eles são concretos: a conta de serviço do relay não consegue gravar na sua própria configuração; a conta do historiador que o relay usa consegue inserir telemetria, mas não apagá-la.

### 8.3 Os caminhos de gerenciamento fazem parte da arquitetura

Muitos diagramas mostram o caminho dos dados e omitem o **caminho de gerenciamento**: como administradores, sistemas de backup, agentes de monitoramento e fornecedores alcançam cada host. Os caminhos de gerenciamento costumam transportar o acesso mais poderoso do sistema. No LANTERN, a administração só alcança os relays a partir de um host de salto de gerenciamento na zona corporativa, com MFA; os fornecedores alcançam o host de salto por meio de uma conta limitada no tempo (Capítulo 7); o monitoramento recebe logs enviados *pelos* relays, em vez de fazer login neles.

O RLY-02 do Laboratório 22, alcançando servidores de hora públicos, é um caminho de gerenciamento que ninguém desenhou.

### 8.4 Projetar para a operabilidade

Um projeto seguro que os operadores não conseguem operar será contornado. Pergunte, para cada controle: como ele é mantido? O que acontece às 03:00 quando ele falha? Como um engenheiro obtém acesso de emergência, e como esse acesso é registrado? O que o serviço faz quando o relay está fora — os operadores sabem que a visão do historiador está desatualizada? Projete os **modos degradados** de forma deliberada: as estações do LANTERN armazenam localmente 24 horas de leituras, então uma interrupção do relay perde atualidade, e não dados; a tela do operador mostra a idade de cada valor.

### 8.5 Desgaste: como as arquiteturas se deterioram

As arquiteturas se desgastam por meio de exceções que parecem razoáveis: uma regra de firewall "temporária" para um fornecedor, um laptop com duas interfaces usado para configuração, um servidor de relatórios movido para a zona de controle "para ficar mais rápido", uma conta de administrador compartilhada por conveniência. Cada uma é pequena; juntas, removem a separação. As defesas são rotineiras: conduítes registrados com responsável e data de expiração (Capítulo 2), revisões de fluxos, revisões de regras e a recusa de exceções não documentadas.

Fallowmere mostra cada tipo. A estação de trabalho corporativa conversando em Modbus com a PS-04 é um hábito de duas interfaces; o modem celular que a Kell deixou no CLP da PS-07 é uma exceção de fornecedor esquecida que nenhum registro de fluxo mostra; e o pedido para enviar setpoints recomendados do historiador para a PS-07 teria sido uma exceção de aparência razoável que inverteria a direção da confiança.

### 8.6 Exemplo resolvido: um pedido que atravessa zonas (sintético)

A operação de Água pede que o historiador envie semanalmente um arquivo de "setpoint recomendado" ao CLP da PS-07, para automatizar uma otimização. Conferido contra o Capítulo 8 ("Zonas, conduítes e a direção da confiança"), o pedido quebra a propriedade mais importante: ele cria um caminho da zona corporativa para a zona das estações que transporta informação de *controle*. Você não o recusa de imediato; devolve a questão de projeto ao seu dono, com alternativas: um operador revisa a recomendação no sistema da sala de controle e a aplica ali; ou o arquivo vai para o sistema da sala de controle, que o valida e o prepara para aprovação de um operador. Qualquer uma preserva a direção da confiança. O seu papel é mostrar a consequência e as alternativas, e registrar a decisão.

### 8.7 Atividade prática: desenhe o caminho de gerenciamento

Desenhe as zonas e os conduítes do LANTERN do Capítulo 2 e depois acrescente todos os caminhos de gerenciamento: SSH de administração via host de salto, acesso de fornecedor, backup, monitoramento, hora, atualizações de pacotes. Para cada um, registre origem, destino, protocolo, autenticação e responsável. Marque qualquer caminho que permitiria a uma única credencial alcançar tanto a zona corporativa quanto a das estações.

No LANTERN, o caminho a vigiar é a rota do fornecedor: a conta limitada no tempo da Kell alcança o host de salto, e o host de salto alcança os relays. Se essa mesma conta, ou uma credencial compartilhada `opsuser`, também abrir o compartilhamento de arquivos corporativo, uma única senha roubada atravessa as duas zonas. Marque também o caminho do servidor de hora, já que o RLY-02 do Laboratório 22 foi encontrado usando servidores de hora públicos que nenhum diagrama mostrava.

### 8.8 Erros comuns e limites

- Diagramas que mostram apenas os caminhos de dados.
- Tratar como independentes dois controles que compartilham uma credencial, um administrador ou um fornecedor.
- Permitir um caminho bidirecional porque o protocolo "só lê".
- Projetar apenas para o dia normal, sem modos degradados nem acesso de emergência.
- Aceitar exceções sem responsável nem data de expiração.

A arquitetura limita o que pode acontecer; ela não mostra o que de fato acontece. A verificação precisa de fluxos, logs e testes (Capítulos 2, 19 e 23).

Um exemplo de Fallowmere: os cartões de controle do risco R2 (Capítulo 18) seriam menos independentes do que parecem se o registro das sessões do fornecedor e a conta do fornecedor fossem administrados pelo mesmo login da Kell.

### Exercícios — capítulo 8

**EX022 — Confira a direção da confiança.** *Objetivo:* avaliar pedidos de mudança contra a propriedade-chave do projeto. *Entradas:* três pedidos: (a) o relay busca uma nova allowlist de estações no historiador a cada hora; (b) o SIEM envia um comando de bloqueio automatizado ao firewall das estações quando vê um ataque; (c) o relay encaminha telemetria para a Halden Cloud num teste de análise de dados. *Restrições:* aceite, rejeite ou reprojete cada um, com um parágrafo. *Etapas:* avalie cada um contra as quatro propriedades de projeto do Capítulo 8 (direção da confiança, menor privilégio, caminhos de gerenciamento, operabilidade). *Evidência esperada:* três parágrafos. *Rubrica:* 3 = (a) reprojetar: a configuração deve fluir do controle de versões por meio de uma mudança, e não ser buscada numa zona de menor confiança; (b) reprojetar com cuidado: o bloqueio automatizado num caminho de TO exige acordo com a operação, falha segura e confirmação manual; (c) aceitável apenas como um novo conduíte declarado, com entrada no registro de fluxos de dados (Capítulo 12), contrato e monitoramento; 2 = dois bem argumentados; 1 = respostas secas; 0 = nada.

**EX023 — Independência das camadas.** *Objetivo:* testar a defesa em profundidade. *Entradas:* camadas propostas para proteger o relay: firewall gerenciado por E. Strand; administração do relay por E. Strand; chave HMAC gerada e guardada por E. Strand no relay; regras de monitoramento escritas por E. Strand. *Restrições:* não presuma má intenção. *Etapas:* (1) identifique a dependência comum; (2) diga qual evento único derrota todas as camadas; (3) proponha duas mudanças que restaurem a independência. *Evidência esperada:* meia página. *Rubrica:* 3 = uma única pessoa e um único conjunto de credenciais; o comprometimento ou o erro de uma conta derrota todas; mudanças como papéis de administração separados, chave mantida num armazenamento separado com custodiantes diferentes, regras de monitoramento de responsabilidade da equipe de segurança e revisadas por ela; 2 = parcial; 1 = "acrescentar mais controles"; 0 = nada.

**EX024 — Modo degradado.** *Objetivo:* projetar a operabilidade. *Entradas:* o relay fica fora por quatro horas durante a noite. *Restrições:* considere operadores, dados e alertas. *Etapas:* (1) descreva o que os operadores veem; (2) o que acontece com os dados; (3) quais alertas disparam e quem os recebe; (4) o que acontece quando o relay volta. *Evidência esperada:* uma página. *Rubrica:* 3 = as telas mostram a idade desatualizada, e não valores congelados como se fossem atuais; as estações armazenam em buffer; os alertas de silêncio de estação e de saúde do relay chegam ao plantão; a volta causa um envio do acúmulo que exige folga (Capítulo 1) e não dispara indevidamente as verificações de reprodução; 2 = falta um aspecto; 1 = genérico; 0 = nada.

### Síntese do capítulo

A propriedade arquitetural mais importante do LANTERN é a direção da confiança: os dados fluem para cima, e os comandos nunca descem por ele. Proteja essa propriedade em toda mudança, mantenha as camadas realmente independentes, ponha os caminhos de gerenciamento no diagrama e projete deliberadamente os modos degradados e o acesso de emergência. As arquiteturas se deterioram por meio de exceções; registre cada uma com um responsável e uma data de expiração, e confira-as.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 30

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Evidência e medição

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- escolher uma medida que responda a uma pergunta operacional e declarar o seu **numerador, denominador e período**;
- relatar distribuições com medianas e percentis altos, e dizer o que uma média esconde;
- incluir **o que ainda não aconteceu** (itens em aberto) nas medidas de latência;
- relatar uma taxa de sucesso a partir de um número pequeno de tentativas, com um intervalo honesto.

Todos os capítulos seguintes pedem que você prove algo com evidências: que um controle funciona, que a aplicação de patches é tempestiva, que uma restauração cumpre a sua meta. A medição é como um implementador transforma "está tudo bem" numa afirmação que alguém pode conferir. É também como as organizações se enganam — em geral não mentindo, mas escolhendo um denominador conveniente.

### 9.1 O que uma boa medida declara

Uma medida é útil quando outra pessoa conseguiria recalculá-la. Declare a **pergunta** ("com que rapidez instalamos as correções dos fornecedores nos controladores das estações?"), a **população** (quais ativos, quais correções), o **numerador e o denominador**, o **período**, a **fonte** dos dados e o que é **excluído** e por quê. Uma cifra de conformidade de patches de "96 %" sem denominador pode significar 96 % dos laptops do escritório, o que nada diz sobre as estações de bombeamento.

A mediana agregada de 9 dias do Laboratório 9 falha nesse teste: não informa a população, e o seu denominador exclui em silêncio sete correções em aberto.

### 9.2 Distribuições, e não só médias

As grandezas operacionais — tempo para aplicar o patch, tempo para restaurar, tempo de resposta a alertas — costumam ser assimétricas: a maioria é rápida, algumas são muito lentas, e as lentas são as que importam. A **mediana** descreve o caso típico; o **percentil 90** (p90) descreve os casos ruins; a **média** é puxada pelos valores extremos e não descreve bem nenhum dos dois. Relate a mediana e o p90 juntos, e olhe para o máximo.

No Laboratório 9, a mediana de 95 dias dos controladores das estações, com cinco correções ainda em aberto, é a cifra que a mediana agregada escondia.

### 9.3 Itens em aberto e viés de sobrevivência

Um erro comum nas medidas de latência é calculá-las apenas sobre os itens **concluídos**. Se cinco correções para os controladores das estações foram lançadas, mas não instaladas, elas são as mais lentas de todas — e são invisíveis para uma mediana calculada sobre as correções instaladas. Relate sempre quantos itens ainda estão em aberto e há quanto tempo. A orientação do NIST sobre gestão corporativa de patches trata a aplicação de patches como um processo de resposta a riscos com uma tempestividade mensurável, e recomenda métricas que a reflitam ([NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final)).

Agregar grupos com comportamentos muito diferentes é a armadilha relacionada. Uma única mediana sobre a TI de escritório, os servidores e os controladores das estações é dominada pelo grupo com mais itens — em geral a TI de escritório — e esconde o grupo de maior consequência.

### 9.4 Amostras pequenas precisam de intervalos

Os testes em serviços críticos são caros, então as amostras são pequenas: dez exercícios de restauração, oito alertas de teste injetados. "9 de 10 exercícios cumpriram a meta" é um fato; "a nossa taxa de sucesso de restauração é de 90 %" é uma afirmação exagerada. Um **intervalo de confiança** mostra a faixa de taxas subjacentes compatíveis com os dados. Para proporções de amostras pequenas, o **intervalo de escore de Wilson** se comporta bem ([Wilson, 1927](https://doi.org/10.1080/01621459.1927.10502953)). Para 9 de 10, o intervalo de Wilson de 95 % vai aproximadamente de 0,60 a 0,98: a taxa verdadeira poderia, de forma plausível, ser tão baixa quanto 60 %.

É por isso que a restauração de backup do Laboratório 23, com 9 de 10 exercícios na meta, ainda falha numa regra de afirmação cujo limite inferior precisa chegar a 0,70.

### 9.5 Exemplo resolvido: latência de patches e exercícios de restauração (sintético)

O relatório mensal da FSTS diz "mediana da latência de patches: 9 dias". O Laboratório 9 a recalcula por grupo. TI corporativa: 12 de 12 correções instaladas, mediana de 5,5 dias, p90 de cerca de 9. Relay/historiador: 6 de 8 instaladas, mediana de 18,5 dias, p90 de cerca de 31,5, duas ainda em aberto. CLP/RTU das estações: apenas 3 de 8 instaladas, mediana de 95 dias, cinco ainda em aberto. A mediana agregada de 9 dias está aritmeticamente correta e é operacionalmente enganosa: ela descreve laptops, e omite as sete correções em aberto — cinco delas nos ativos de maior consequência.

Os controladores das estações recebem patches mais devagar por bons motivos: os fornecedores precisam certificar as correções, e a instalação pode exigir uma visita ao local e uma janela de interrupção acordada com a operação (Capítulo 16). A medida não deve punir isso; deve mostrá-lo, para que os controles compensatórios possam ser justificados durante o período de exposição.

### 9.6 Atividade prática: medidas honestas

**Laboratório 9** (salve como `lab09.py`, execute com `python3 lab09.py`):

```python
# Lab 9 - measuring patch latency and a restore drill honestly (offline, standard library only)
# Synthetic: days from vendor fix release to installation, Fallowmere estate, last two quarters.
import math, statistics as st
latency = {"corp IT": [3, 5, 4, 9, 6, 2, 7, 5, 30, 4, 6, 8],
           "relay/historian": [12, 19, 15, 41, 22, 18],
           "station PLC/RTU": [64, 140, 95]}
not_yet = {"corp IT": 0, "relay/historian": 2, "station PLC/RTU": 5}  # fixes released but not installed
def pct(xs, p):
    xs = sorted(xs); k = (len(xs) - 1) * p; f = math.floor(k); c = math.ceil(k)
    return xs[f] + (xs[c] - xs[f]) * (k - f)
for g, xs in latency.items():
    n = len(xs) + not_yet[g]
    print(f"{g:<16} installed {len(xs):>2}/{n:<2} median {st.median(xs):>5.1f} d  p90 {pct(xs, .9):>6.1f} d  mean {st.mean(xs):>5.1f} d")
allx = [x for xs in latency.values() for x in xs]
print(f"pooled (misleading) median {st.median(allx):.1f} d over {len(allx)} installed fixes; {sum(not_yet.values())} still open are invisible to it")
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n; c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
k, n = 9, 10  # restore drills that met the 4-hour target
lo, hi = wilson(k, n)
print(f"restore drills within target: {k}/{n} = {k/n:.0%}, 95% Wilson interval [{lo:.2f}, {hi:.2f}]")
```

Saída esperada (Python 3.13.5):

```text
corp IT          installed 12/12 median   5.5 d  p90    8.9 d  mean   7.4 d
relay/historian  installed  6/8  median  18.5 d  p90   31.5 d  mean  21.2 d
station PLC/RTU  installed  3/8  median  95.0 d  p90  131.0 d  mean  99.7 d
pooled (misleading) median 9.0 d over 21 installed fixes; 7 still open are invisible to it
restore drills within target: 9/10 = 90%, 95% Wilson interval [0.60, 0.98]
```

Escreva a linha de relatório que você enviaria no lugar de "mediana da latência de patches: 9 dias". Ela deve caber em duas frases.

Uma linha de duas frases que passaria: "A TI corporativa instalou 12 de 12 correções, mediana de 5,5 dias; relay e historiador, 6 de 8, mediana de 18,5 dias, duas em aberto. Os controladores das estações instalaram 3 de 8, mediana de 95 dias, com cinco correções em aberto sob controles compensatórios e planos com data." Ela é mais longa que "9 dias", mas o leitor agora consegue ver onde está o risco, e os controladores das estações não estão mais escondidos atrás dos laptops do escritório.

### 9.7 Erros comuns e limites

- Relatar uma porcentagem sem o seu denominador.
- Médias para grandezas assimétricas.
- Calcular a latência apenas sobre os itens fechados.
- Agregar grupos de modo que o grupo grande e de baixa consequência esconda o pequeno e de alta consequência.
- Transformar um pequeno número de tentativas bem-sucedidas numa taxa sem intervalo.
- Mudar a definição de uma medida entre relatórios sem avisar.

As medidas descrevem o que foi registrado. Se os dados de origem estiverem incompletos — correções não registradas, exercícios não anotados —, nenhuma estatística vai consertar isso.

No Laboratório 9, a mediana agregada mostra três desses erros de uma vez: sem denominador, itens em aberto excluídos e grupos agregados.

### Exercícios — capítulo 9

**EX025 — Reescreva a linha do relatório.** *Objetivo:* comunicar uma medida com honestidade. *Entradas:* a saída do Laboratório 9. *Restrições:* no máximo duas frases; inclua os denominadores e os itens em aberto. *Etapas:* escreva-a e depois liste o que você deixou de fora e por quê. *Evidência esperada:* a linha e uma nota. *Rubrica:* 3 = medianas ou p90 por grupo com contagens de instaladas/total, correções em aberto das estações mencionadas explicitamente, nenhuma cifra agregada apresentada como destaque; 2 = quase tudo; 1 = repete a mediana agregada; 0 = nada.

**EX026 — Envelheça os itens em aberto.** *Objetivo:* incluir os itens em aberto na medida. *Entradas:* as cinco correções em aberto das estações foram lançadas há 20, 45, 70, 130 e 200 dias; as duas correções em aberto do relay/historiador, há 10 e 35 dias. *Restrições:* trate a idade de cada correção em aberto como um limite inferior da sua latência. *Etapas:* (1) combine as latências das instaladas com as idades das em aberto para CLP/RTU das estações; (2) calcule uma mediana que seja um limite inferior; (3) explique por que isso é um limite inferior, e não uma estimativa. *Evidência esperada:* cálculo e explicação. *Rubrica:* 3 = valores combinados 20, 45, 64, 70, 95, 130, 140, 200 → limite inferior da mediana de 82,5 dias, corretamente explicado (os itens em aberto só vão envelhecer); 2 = deslize aritmético; 1 = ignora os itens em aberto; 0 = nada.

**EX027 — Quantos exercícios?** *Objetivo:* planejar o tamanho da amostra a partir de um intervalo. *Entradas:* a função de Wilson do Laboratório 9. *Restrições:* presuma que todo exercício tenha sucesso. *Etapas:* (1) encontre o menor número de exercícios consecutivos bem-sucedidos para o qual o limite inferior de Wilson de 95 % seja pelo menos 0,80; (2) diga se isso é viável a um exercício por mês e o que você faria em vez disso. *Evidência esperada:* o número, com a execução que o mostra, e um parágrafo. *Rubrica:* 3 = 16 exercícios (limite inferior ≈ 0,806; 15 dá ≈ 0,796), reconhecidos como 16 meses a um por mês, com alternativas sensatas, como restaurações parciais menores e mais frequentes ou testes de restauração automatizados; 2 = número certo, sem plano; 1 = chutado; 0 = nada.

### Síntese do capítulo

Uma medida é útil quando declara a sua pergunta, população, numerador, denominador, período, fonte e exclusões. Relate medianas com percentis altos para grandezas assimétricas; inclua os itens em aberto; não agregue grupos com consequências diferentes; e acrescente intervalos às taxas de sucesso de amostras pequenas. O objetivo não é um número lisonjeiro, mas um que outra pessoa consiga recalcular e sobre o qual consiga agir.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 30

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Infraestrutura crítica e segurança setorial: orientação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- explicar o que torna um serviço **crítico**: a consequência da sua perda para as pessoas, para outros serviços e para a sociedade;
- descrever como água, saúde, energia, transporte e finanças diferem no que protegem, na rapidez com que o dano chega e em quem os regula;
- identificar as **dependências e interdependências** que transformam uma falha local numa falha regional;
- situar o seu próprio trabalho como implementador dentro das obrigações que um operador carrega.

Os Capítulos 1–9 construíram habilidades gerais. Daqui em diante, o livro as aplica especificamente aos serviços críticos. Este capítulo é de orientação: o formato da área, o bastante para entender por que um tecnólogo da FSTS precisa pensar numa estação de bombeamento, num hospital e numa garagem de ônibus de formas diferentes, mesmo quando os servidores se parecem.

### 10.1 O que torna um serviço crítico

Um serviço é crítico quando a sua interrupção prejudicaria gravemente a saúde, a segurança, a proteção, a atividade econômica ou o funcionamento da sociedade. Os governos formalizam isso de formas diferentes. Os Estados Unidos descrevem **National Critical Functions** — funções tão vitais que a sua interrupção teria um efeito debilitante —, e não apenas listas de setores ([CISA National Critical Functions](https://www.cisa.gov/national-critical-functions-set)). A Diretiva NIS2 da União Europeia estabelece obrigações de gestão de riscos de cibersegurança e de notificação para entidades em setores de alta criticidade ([Diretiva (UE) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)), e a Diretiva CER trata da resiliência física e mais ampla das entidades críticas ([Diretiva (UE) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)). Esses textos mudam; confira a versão atual e como a sua jurisdição a aplica. Este livro não dá aconselhamento jurídico.

Para um implementador, o significado prático é mais simples: **a unidade de dano é pessoas e tempo**, e não apenas registros de dados ou dinheiro. "41.000 pessoas sem informações confiáveis sobre a água por seis horas" é o tipo de afirmação que deve orientar as prioridades.

### 10.2 Como os setores diferem

| Setor (exemplo sintético de Fallowmere) | O que é protegido primeiro | Com que rapidez o dano chega | Tecnologia típica |
|---|---|---|---|
| Água (Fallowmere Water) | Água potável segura, continuidade do fornecimento | De horas a dias; o dano à qualidade pode ser mais rápido | CLPs, RTUs, SCADA, telemetria sobre enlaces de operadora |
| Saúde (Community Hospital) | Segurança do paciente, continuidade do cuidado | Minutos, para alguns sistemas clínicos | Dispositivos médicos, gateways clínicos, prontuários eletrônicos |
| Transporte (Transit depot) | Segurança dos passageiros, continuidade do serviço | De minutos a horas | Sistemas de frota, bilhetagem, TI da garagem |
| Energia (não operada pela FSTS) | Estabilidade da rede, fornecimento | De segundos a horas | Relés de proteção, centros de controle |
| Finanças (não operadas pela FSTS) | Integridade das transações, disponibilidade | Minutos | Sistemas de pagamento, data centers |

As diferenças mudam as escolhas de implementação. Um patch no gateway das bombas de infusão de um hospital exige a aprovação da engenharia clínica; uma mudança de firewall numa estação de bombeamento pode exigir uma visita ao local e uma janela de interrupção; um quiosque da garagem em geral pode ser reconstruído no mesmo dia. Tratar todos com um único processo de mudanças de TI ou atrasa as mudanças seguras, ou apressa as perigosas.

### 10.3 Dependências e interdependências

Os serviços críticos dependem uns dos outros: a água precisa de eletricidade para as bombas e de telecomunicações para a telemetria; os hospitais precisam de água, eletricidade e telecomunicações; todos dependem de um pequeno número de fornecedores. O artigo clássico de Rinaldi e colegas classifica as interdependências como físicas, cibernéticas, geográficas e lógicas ([Rinaldi, Peerenboom e Kelly, 2001](https://doi.org/10.1109/37.969131)). Na FSTS, a interdependência mais importante é organizacional: a mesma equipe pequena, o mesmo host de salto e os mesmos fornecedores atendem aos três operadores. Uma única conta de administrador da FSTS comprometida toca água, saúde e transporte ao mesmo tempo.

### 10.4 As obrigações do operador e a sua parte nelas

Os operadores de serviços essenciais costumam carregar obrigações de gerenciar o risco cibernético, notificar incidentes significativos dentro de prazos definidos, manter planos de continuidade e cooperar com as autoridades. Frameworks como o Cyber Assessment Framework do NCSC do Reino Unido expressam essas obrigações como resultados a alcançar ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)); os Cross-Sector Cybersecurity Performance Goals da CISA oferecem uma linha de base de práticas ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)). Um implementador raramente é dono dessas obrigações, mas produz a maior parte das evidências para elas: listas de ativos, revisões de acessos, logs, resultados de testes, linhas do tempo de incidentes. Se essas evidências estiverem atrasadas ou erradas, o relatório do operador estará atrasado ou errado.

### 10.5 Exemplo resolvido: uma falha, três clientes (sintético)

Às 02:10, um disco do host de salto da FSTS falha. A operação de Água perde a administração remota dos relays, mas mantém a telemetria (os relays continuam rodando). Os engenheiros clínicos do hospital não conseguem alcançar o gateway das bombas de infusão para carregar uma atualização da biblioteca de medicamentos programada para as 06:00. A garagem não consegue enviar uma mudança de horários para os quiosques. A mesma falha tem três consequências diferentes, com três prazos diferentes. O tecnólogo de plantão que reconhece isso liga primeiro para a Engenharia Clínica — porque a atualização das 06:00 tem uma finalidade de segurança do paciente —, embora a Água seja o maior cliente.

### 10.6 Atividade prática: tabela de consequências e prazos

Para cada cliente de Fallowmere, liste três sistemas operados pela FSTS. Para cada sistema, escreva: o que as pessoas perdem se ele parar, com que rapidez essa perda se torna danosa, quem decide sobre a ação de emergência e de qual outro sistema ele depende. Guarde esta tabela; o Capítulo 11 a transforma num inventário com dependências.

Para o Fallowmere Community Hospital, uma linha poderia ser: gateway das bombas de infusão; perda, as atualizações da biblioteca de medicamentos não podem ser carregadas; danosa em horas se uma atualização programada, como a das 06:00, for perdida; a Engenharia Clínica decide; depende do host de salto da FSTS. Essa linha é o motivo pelo qual a falha do host de salto no exemplo resolvido foi escalada ao hospital antes da Água.

### 10.7 Erros comuns e limites

- Tratar todo sistema operado por uma equipe de TI como tendo a mesma consequência.
- Medir o dano apenas em dados ou dinheiro.
- Ignorar pessoas, ferramentas e fornecedores compartilhados como dependências.
- Citar regulamentos de memória; o seu escopo e os seus prazos mudam e diferem entre jurisdições.
- Presumir que o implementador não tem parte nas obrigações do operador.

A falha do host de salto mostra juntos o primeiro e o terceiro erros: um único host compartilhado da FSTS teve três consequências, com três prazos.

Medir o dano apenas em dinheiro teria posto a Água em primeiro lugar naquela noite, por ser o maior cliente, e teria perdido a atualização da biblioteca de medicamentos das 06:00.

### Exercícios — capítulo 10

**EX028 — Consequência em pessoas e tempo.** *Objetivo:* expressar o dano em unidades de serviço. *Entradas:* o cenário do Capítulo 10 ("Exemplo resolvido: uma falha, três clientes"). *Restrições:* apenas números sintéticos; declare as premissas. *Etapas:* para cada cliente, escreva uma frase da forma "N pessoas perdem X por T, o que se torna danoso depois de D porque…". *Evidência esperada:* três frases com premissas. *Rubrica:* 3 = três afirmações específicas, plausíveis e com premissas rotuladas, mostrando prazos diferentes, com o prazo de segurança do paciente do hospital identificado como o mais curto; 2 = uma genérica; 1 = todas em dinheiro; 0 = nada.

**EX029 — Mapa de dependências compartilhadas.** *Objetivo:* encontrar as interdependências criadas por um serviço compartilhado. *Entradas:* a FSTS opera um host de salto, um SIEM, um diretório de identidades e um sistema de backup para os três clientes; a Kell fornece as RTUs de água, a BayTel transporta a telemetria da água e a internet do hospital. *Restrições:* use os quatro tipos de Rinaldi. *Etapas:* (1) classifique cada dependência; (2) nomeie a falha única de efeito mais amplo; (3) proponha uma mudança para reduzi-la. *Evidência esperada:* tabela e parágrafo. *Rubrica:* 3 = sistemas compartilhados da FSTS como cibernéticos/lógicos, BayTel como operadora comum cibernética/física, pessoal como lógico; comprometimento do diretório de identidades ou do host de salto identificado como o mais amplo; uma mudança prática, como níveis privilegiados por cliente ou um segundo caminho de operadora para a telemetria; 2 = classificação fraca; 1 = só a lista; 0 = nada.

**EX030 — As evidências que você deve.** *Objetivo:* ligar o trabalho diário às obrigações do operador. *Entradas:* CISA CPGs ou NCSC CAF (escolha um; cite a versão que você leu). *Restrições:* três resultados ou metas. *Etapas:* para cada um, nomeie a evidência que um tecnólogo da FSTS produz para ele, com que frequência e onde ela é guardada. *Evidência esperada:* tabela com citação. *Rubrica:* 3 = três resultados/metas corretamente citados (por exemplo, inventário de ativos, MFA, coleta de logs), cada um com evidência específica e produzida com regularidade; 2 = evidência vaga; 1 = sem citação; 0 = nada.

### Síntese do capítulo

Um serviço é crítico por causa do que a sua perda faz às pessoas, medido em pessoas e tempo. Os setores diferem no que protegem primeiro e na rapidez com que o dano chega, então a mesma falha técnica exige respostas diferentes. Serviços compartilhados como a FSTS criam interdependências por meio de pessoas, ferramentas e fornecedores. Os operadores carregam as obrigações legais; os implementadores produzem a maior parte das evidências que mostram que elas são cumpridas.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 30

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Infraestrutura crítica e segurança setorial: ativos e contexto

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- construir e manter um inventário de ativos para um serviço misto de TI/TO a partir de várias fontes;
- registrar, para cada ativo, o seu **responsável, função, criticidade, localização, versão de software ou firmware, situação de suporte e dependências**;
- usar métodos de descoberta **passivos**, que são seguros para redes operacionais;
- conciliar fontes que discordam e tratar a discordância como uma constatação.

O Capítulo 4 mostrou como modelar um inventário. Este capítulo trata de preenchê-lo com veracidade. As Cross-Sector Performance Goals da CISA incluem manter um inventário de ativos, inclusive dos ativos de TO ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)); você não consegue proteger, corrigir ou monitorar o que não registrou.

### 11.1 O que registrar e por quê

| Atributo | Por que um implementador precisa dele |
|---|---|
| Identificador e localização | Para encontrá-lo, fisicamente e na rede. |
| Função e criticidade | Para decidir a prioridade na aplicação de patches, no monitoramento e na resposta. |
| Responsável (um papel, não uma pessoa) | Alguém precisa aprovar mudanças e aceitar o risco. |
| Modelo e versão de firmware/software | Para casar alertas e correções dos fornecedores. |
| Situação de suporte do fornecedor | Ativos sem suporte precisam de controles compensatórios e de planos de substituição. |
| Endereços de rede e zona | Para conferir os fluxos (Capítulo 2). |
| Dependências | Para entender o que mais falha junto com ele (Capítulo 10). |
| Última verificação (data, método) | Para que os registros desatualizados fiquem visíveis. |

### 11.2 As fontes e os seus pontos cegos

Nenhuma fonte isolada é completa. Os **registros de compras e contratos** sabem o que foi comprado, mas não para onde foi. Os **registros de gestão de configuração ou de engenharia** conhecem o projeto, mas podem ficar atrás da realidade. A **observação da rede** (tabelas de switches, registros de fluxo, um sensor passivo) vê o que conversa, mas não o que está em silêncio. As **vistorias em campo** veem o que está fisicamente presente, mas são caras e pouco frequentes. Os **portais dos fornecedores** sabem as versões de firmware do que eles suportam. Combine pelo menos duas fontes e registre qual fonte disse o quê.

A PS-09 mostra por quê: só os registros de fluxo sabiam que a estação tinha ficado em silêncio.

### 11.3 Descoberta segura em redes operacionais

A varredura ativa — enviar sondas a todos os endereços — é rotina nas redes de escritório e arriscada nas redes de controle: alguns controladores mais antigos e dispositivos embarcados podem se comportar mal ou reiniciar quando sondados de forma inesperada. O guia de TO do NIST aconselha cautela com a varredura ativa em ambientes de TO e favorece métodos passivos ou trabalho ativo cuidadosamente planejado e coordenado ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Para um implementador, a regra é: na zona das estações, use fontes passivas (registros de fluxo, tabelas de switches, exportações de configuração dos próprios controladores feitas pelos seus engenheiros), a menos que um método ativo tenha sido acordado com a operação, testado num equipamento sobressalente e agendado.

### 11.4 Conciliação

Quando as fontes discordam, a discordância é informação. Um ativo nos registros de compras, mas nunca visto na rede, pode estar num armário — ou conectado em algum lugar inesperado. Um endereço visto nos fluxos, mas ausente de todos os registros, é um dispositivo desconhecido. Uma versão de firmware que difere entre o registro de engenharia e o portal do fornecedor significa que um deles está errado — e, se for o registro de engenharia, uma correção pode ter sido aplicada, ou não, sem documentação. Acompanhe cada discrepância como um ticket com responsável até que ela seja resolvida.

### 11.5 Ativos sem suporte

Os serviços críticos costumam operar equipamentos além do suporte do fornecedor, porque a substituição exige capital, interrupções e nova certificação. O inventário precisa tornar isso visível, com um plano de **controles compensatórios** para cada ativo sem suporte: segmentação mais estreita, allowlists mais rígidas, monitoramento extra, peças sobressalentes e uma data de substituição de responsabilidade de alguém que tenha orçamento.

A RTU Kell R2 da PS-09, sem suporte desde 2025-12-31 e ainda de criticidade 1, é o caso de Fallowmere. O seu plano nomearia a entrada na allowlist do relay e o conduíte como os controles apertados, a Regra C como o monitoramento extra, uma RTU sobressalente mantida pela Água e uma data de substituição de responsabilidade da operação de Água, que detém o orçamento de capital.

### 11.6 Exemplo resolvido: conciliar a PS-09 (sintético)

Três fontes descrevem a estação de bombeamento PS-09. O registro de compras lista uma RTU Kell R2 comprada em 2017. O registro de engenharia lista o firmware 1.1 e o responsável "Water Ops". Os registros de fluxo mostram 10.20.0.13 conversando com o relay até três semanas atrás, e nada desde então (a estação silenciosa do Capítulo 2). O inventário (Capítulo 4) não tem responsável para a PS09-RTU e registra que o suporte do fornecedor terminou em 2025-12-31. Você registra quatro discrepâncias: responsável ausente no inventário, mas presente no registro de engenharia (corrigir o registro, depois de confirmar com a Water Ops); suporte encerrado (exige um plano de controles compensatórios); estação em silêncio (questão operacional, levada à operação de Água no mesmo dia); e firmware não verificado de forma independente (pedir ao engenheiro de Água que exporte a configuração da RTU na próxima visita ao local — Capítulo 28).

### 11.7 Atividade prática: conciliação de três fontes

Usando o inventário do Laboratório 4 e os fluxos do Laboratório 2, liste todo ativo ou endereço que aparece numa fonte, mas não na outra, e todo atributo que difere. Para cada um, escreva a próxima ação e o responsável. Não sonde nenhum dispositivo para resolver uma discrepância; pergunte ao responsável.

Espere que a RTU da PS-09 em 10.20.0.13 apareça nas duas fontes, mas discorde: presente no inventário, silenciosa nos fluxos.

Espere também que os fluxos do Laboratório 2 mostrem endereços que faltam no inventário, como a estação de trabalho corporativa 10.40.3.7; registre o seu responsável como uma pergunta para a engenharia de Água, e não como um palpite.

### 11.8 Erros comuns e limites

- Tratar uma única fonte como o inventário.
- Executar varreduras ativas em redes de controle "só para ter certeza".
- Registrar uma pessoa como responsável, em vez de um papel.
- Registrar o firmware uma vez e nunca mais verificá-lo.
- Listar ativos sem suporte sem controles compensatórios nem um responsável pela substituição.
- Esconder discrepâncias para que o inventário pareça completo.

Um inventário é um modelo da realidade, sempre um pouco desatualizado. A sua qualidade se mede por quão recentemente cada registro foi verificado e pela rapidez com que as discrepâncias são fechadas.

O modem celular da PS-07, encontrado apenas numa visita ao local, é o argumento contra confiar numa só fonte.

### Exercícios — capítulo 11

**EX031 — Concilie.** *Objetivo:* encontrar discrepâncias entre fontes. *Entradas:* o inventário do Laboratório 4 e os fluxos do Laboratório 2. *Restrições:* apenas as zonas de estações, relay e corporativa. *Etapas:* (1) liste os endereços nos fluxos sem registro no inventário (presuma que o inventário mapeia PS04-PLC para 10.20.0.11, PS07-PLC para 10.20.0.12, PS09-RTU para 10.20.0.13, RLY-01 para 10.30.0.5 e HIST-01 para 10.40.8.20); (2) liste os ativos do inventário nessas zonas nunca vistos nos fluxos; (3) dê uma ação e um responsável para cada um. *Evidência esperada:* tabela. *Rubrica:* 3 = 10.40.3.7 (estação de trabalho corporativa, ausente do extrato) identificada como não registrada e como a origem do Modbus não declarado; SW-STN-04 não visto (esperado para um switch — explique); PS09-RTU em silêncio; ações com responsáveis; 2 = parcial; 1 = só a lista; 0 = nada.

**EX032 — Controles compensatórios.** *Objetivo:* planejar para um ativo sem suporte. *Entradas:* PS09-RTU, criticidade 1, suporte do fornecedor encerrado, orçamento de substituição disponível em 14 meses. *Restrições:* controles que a FSTS e a Água conseguem implementar sem correções do fornecedor. *Etapas:* liste quatro controles compensatórios, com evidência para cada um, e o responsável pela substituição. *Evidência esperada:* tabela. *Rubrica:* 3 = conduíte restrito apenas ao relay e verificado, validação no lado do relay e quarentena por faixa, alertas de silêncio de estação e de valor implausível, unidade sobressalente ou procedimento manual testado, backup da configuração; substituição de responsabilidade de um papel da Água, com data; 2 = três; 1 = "monitorá-la"; 0 = nada.

**EX033 — Plano de descoberta.** *Objetivo:* planejar uma descoberta segura. *Entradas:* a operação de Água quer uma lista completa dos dispositivos das 14 estações em três meses. *Restrições:* nenhuma varredura ativa sem acordo; no máximo duas visitas a campo por semana. *Etapas:* (1) liste as fontes passivas a usar primeiro; (2) diga quando um método ativo seria justificado e como você o tornaria seguro; (3) dê um cronograma. *Evidência esperada:* plano de uma página. *Rubrica:* 3 = fontes passivas (fluxos, tabelas de switches, exportações de engenharia, registros de compras) primeiro; método ativo apenas com acordo da operação, testado num sobressalente, com taxa limitada, numa janela, com alguém no local; cronograma realista; 2 = plano sólido, mas vago quanto à segurança; 1 = "varrer a sub-rede"; 0 = nada.

### Síntese do capítulo

Um inventário registra, para cada ativo, o que ele é, onde está, quem é o responsável, o que ele roda, se tem suporte, de que depende e quando isso foi verificado pela última vez. Construa-o a partir de várias fontes, faça a descoberta com segurança nas redes de controle, trate a discordância entre fontes como constatação e dê a todo ativo sem suporte controles compensatórios e um responsável pela substituição.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 30

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Infraestrutura crítica e segurança setorial: fluxos de dados

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- manter um **registro de fluxos de dados** que anota, para cada fluxo, a sua origem, destino, classe de dados, proteção e retenção;
- classificar os dados num serviço crítico: telemetria operacional, configuração, dados pessoais e vinculados a pacientes, logs de segurança;
- verificar o registro contra o que os sistemas de fato enviam e guardam;
- reconhecer quando um fluxo novo precisa de revisão de privacidade, contratual ou de safety antes de começar.

O Capítulo 2 comparou os fluxos de rede com os conduítes declarados. Um conduíte diz que *um caminho é permitido*; um registro de fluxos de dados diz *quais dados viajam por ele, como são protegidos e por quanto tempo são guardados na outra ponta*. Nos serviços compartilhados, a segunda pergunta costuma ser a que põe uma organização em apuros, porque os dados sobrevivem ao motivo pelo qual foram coletados.

### 12.1 O registro

Cada entrada no registro do LANTERN anota: identificador; origem e destino (sistemas, não apenas endereços); **classe de dados**; se o fluxo é cifrado em trânsito; por quanto tempo o destino guarda os dados; a finalidade; o responsável; e, para dados pessoais, a base legal registrada pelo responsável pelos dados. O registro é um documento que as pessoas leem num incidente ("o que saiu do gateway do hospital?") e numa solicitação de privacidade ("para onde vão os dados da bomba deste paciente?").

A DF5 é uma entrada-modelo: gateway clínico para a Halden Cloud, vinculada a pacientes, cifrada, 30 dias registrados.

### 12.2 Classes de dados

Para um implementador, quatro classes cobrem a maior parte de um serviço crítico compartilhado:

- **Telemetria operacional** — leituras e estados (níveis, vazões, cloro). Em geral não é pessoal, mas é crítica para a integridade e às vezes sensível em conjunto (revela como a rede funciona).
- **Dados de configuração e de engenharia** — programas dos controladores, diagramas de rede, setpoints, configuração do relay. Altamente sensíveis: são um mapa para um atacante.
- **Dados pessoais e vinculados a pacientes** — qualquer coisa sobre uma pessoa identificável. No hospital, os logs de eventos das bombas de infusão ligados a uma enfermaria e a um horário podem identificar um paciente. A lei de proteção de dados se aplica; na UE, o GDPR ([Regulamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)) exige, entre outros princípios, que os dados pessoais não sejam guardados por mais tempo do que o necessário para a sua finalidade.
- **Logs de segurança** — autenticação, fluxos, alertas. Muitas vezes contêm dados pessoais (nomes de usuário, endereços) e precisam ser protegidos e retidos de acordo com a política.

O Privacy Framework do NIST oferece uma estrutura para gerenciar o risco de privacidade junto com o risco de cibersegurança ([NIST Privacy Framework](https://www.nist.gov/privacy-framework)).

### 12.3 Verificar o registro

Os registros se deterioram como os inventários. Verifique-os amostrando o que de fato acontece: quais sistemas enviam para quais (fluxos), que classe de dados há nos conteúdos (amostragem de metadados pelo responsável pelos dados, e não lendo prontuários de pacientes), se o transporte é cifrado e por quanto tempo o destino de fato guarda os dados (as suas configurações de retenção e a idade dos seus registros mais antigos). As diferenças caem em tipos conhecidos: fluxos não registrados; fluxos que enviam uma classe diferente da registrada; cifração registrada, mas ausente; retenção mais longa que a registrada.

### 12.4 Fluxos novos precisam de revisão antes de começar

A maioria dos problemas de fluxos de dados começa com um pedido razoável: um fornecedor quer telemetria para diagnóstico remoto; uma equipe de relatórios quer uma cópia dos eventos do gateway clínico. Antes que um fluxo desses comece, a entrada do registro é escrita e revisada — pelo responsável pelos dados, pela segurança (proteção e conduíte) e, quando há dados pessoais envolvidos, pela função de privacidade. Se ele transportar dados de controle ou de configuração, aplica-se a regra de arquitetura do Capítulo 8.

O pedido da Kell por telemetria horária dos relays é o caso de Fallowmere: a entrada precisa ser escrita e revisada antes que a primeira hora seja enviada.

### 12.5 Exemplo resolvido: registro versus realidade (sintético)

O Laboratório 12 compara cinco entradas do registro com sete fluxos observados. Quatro fluxos registrados coincidem. Três diferenças importam:

1. **DF5 — gateway clínico para a Halden Cloud — guarda dados vinculados a pacientes por 400 dias, contra os 30 registrados.** O fluxo está registrado e cifrado, mas a retenção no destino não coincide. Essa é uma questão de privacidade e de contrato; o responsável pelos dados do hospital precisa ser informado, e a configuração de retenção da Halden, conferida contra o contrato.
2. **Um fluxo não registrado do historiador para um sistema de suporte do fornecedor, em texto claro.** Ele transporta telemetria — não pessoal, mas operacionalmente sensível — sem cifração e sem que ninguém o tenha aprovado.
3. **Um fluxo não registrado do gateway clínico para o servidor de relatórios, transportando dados vinculados a pacientes.** Cifrado, mas ninguém o aprovou, e o servidor de relatórios fica na zona corporativa usada pela equipe de água.

O terceiro é o mais grave, apesar de cifrado: dados vinculados a pacientes chegaram a um sistema e a um público sem finalidade registrada. A cifração em trânsito protege o percurso, e não o destino.

### 12.6 Atividade prática: conferência do registro

**Laboratório 12** (salve como `lab12.py`, execute com `python3 lab12.py`):

```python
# Lab 12 - checking a data-flow register against what the service actually sends (offline, standard library only)
# Synthetic: Fallowmere shared services. Each register entry: id, source, destination, data class, encrypted, retention days.
register = [
 ("DF1", "PS-*", "RLY-01", "telemetry", False, 0),
 ("DF2", "RLY-01", "HIST-01", "telemetry", True, 730),
 ("DF3", "HIST-01", "REPORTS", "telemetry-aggregate", True, 365),
 ("DF4", "WARD-PUMPS", "CLIN-GW", "patient-linked", True, 30),
 ("DF5", "CLIN-GW", "HALDEN-CLOUD", "patient-linked", True, 30),
]
observed = [  # source, destination, data class seen by sampling payload metadata, tls?, stored days at destination
 ("PS-04", "RLY-01", "telemetry", False, 0), ("RLY-01", "HIST-01", "telemetry", True, 730),
 ("HIST-01", "REPORTS", "telemetry-aggregate", True, 365), ("WARD-PUMPS", "CLIN-GW", "patient-linked", True, 30),
 ("CLIN-GW", "HALDEN-CLOUD", "patient-linked", True, 400), ("HIST-01", "VENDOR-SUPPORT", "telemetry", False, None),
 ("CLIN-GW", "REPORTS", "patient-linked", True, 365),
]
sensitive = {"patient-linked"}
def match(src, dst):
    for r in register:
        if (r[1] == src or (r[1].endswith("*") and src.startswith(r[1][:-1]))) and r[2] == dst:
            return r
for src, dst, cls, enc, keep in observed:
    r = match(src, dst)
    if r is None:
        sev = "HIGH" if cls in sensitive else "MED"
        print(f"{sev:<4} unregistered flow {src}->{dst} ({cls}, encrypted={enc})")
        continue
    issues = []
    if r[3] != cls: issues.append(f"class {cls} != registered {r[3]}")
    if r[4] and not enc: issues.append("registered encrypted but sent clear")
    if keep is not None and keep > r[5]: issues.append(f"kept {keep} d > registered {r[5]} d")
    print(f"{'OK  ' if not issues else 'HIGH' if cls in sensitive else 'MED '} {r[0]} {src}->{dst} {'; '.join(issues)}")
```

Saída esperada (Python 3.13.5):

```text
OK   DF1 PS-04->RLY-01 
OK   DF2 RLY-01->HIST-01 
OK   DF3 HIST-01->REPORTS 
OK   DF4 WARD-PUMPS->CLIN-GW 
HIGH DF5 CLIN-GW->HALDEN-CLOUD kept 400 d > registered 30 d
MED  unregistered flow HIST-01->VENDOR-SUPPORT (telemetry, encrypted=False)
HIGH unregistered flow CLIN-GW->REPORTS (patient-linked, encrypted=True)
```

A saída reproduz as três diferenças acima. Antes de agir, decida quem recebe cada uma: a retenção de 400 dias da DF5 vai para o responsável pelos dados do hospital e para quem detém o contrato com a Halden; o fluxo em texto claro do historiador para o sistema de suporte do fornecedor vai para o responsável pelos dados da Água e para a FSTS Security; e o fluxo não registrado de dados vinculados a pacientes para o servidor de relatórios vai primeiro para a função de privacidade do hospital, porque um público da zona corporativa pode já ter visto os dados.

### 12.7 Erros comuns e limites

- Registrar caminhos (conduítes), mas não classes de dados e retenção.
- Presumir que "cifrado" significa "aceitável".
- Tratar a telemetria operacional como inofensiva porque não é pessoal.
- Verificar as classes de dados lendo você mesmo os dados pessoais, em vez de pedir ao responsável pelos dados que amostre os metadados.
- Deixar um fluxo de fornecedor ou de relatórios começar antes que a entrada seja revisada.

O registro mostra o que é conhecido; os fluxos que saem por rotas inesperadas (mídias removíveis, o laptop de um fornecedor) precisam de outros controles.

O fluxo não registrado do gateway clínico para o servidor de relatórios é o segundo erro em ação: cifrado, e ainda assim inaceitável.

### Exercícios — capítulo 12

**EX034 — Faça a triagem das diferenças.** *Objetivo:* priorizar as constatações de fluxos de dados. *Entradas:* a saída do Laboratório 12. *Restrições:* uma ação e um responsável por constatação. *Etapas:* (1) ordene as três constatações; (2) dê a primeira ação e o responsável; (3) diga qual precisa ser relatada a alguém fora da FSTS. *Evidência esperada:* tabela. *Rubrica:* 3 = CLIN-GW→REPORTS em primeiro lugar (dados vinculados a pacientes não aprovados num público errado: interromper o fluxo com o acordo do responsável pelos dados do hospital, avaliar), retenção da DF5 em segundo (responsável pelos dados do hospital e contrato com a Halden), texto claro para o suporte do fornecedor em terceiro (interromper ou cifrar, registrar); reconhece que a necessidade de notificação externa é decisão do responsável pelos dados e da função de privacidade; 2 = ordenação defensável, responsáveis vagos; 1 = ordena apenas pela cifração; 0 = nada.

**EX035 — Escreva uma entrada do registro.** *Objetivo:* especificar um fluxo novo antes que ele comece. *Entradas:* a Kell Instruments pede telemetria horária da PS-09 para diagnóstico remoto. *Restrições:* todos os campos do Capítulo 12 ("O registro"); inclua o conduíte e a proteção. *Etapas:* escreva a entrada e liste quem precisa aprová-la. *Evidência esperada:* entrada e aprovadores. *Rubrica:* 3 = origem/destino específicos (exportação do relay ou do historiador, e não a RTU diretamente), classe de dados telemetria operacional, transporte cifrado, campos e frequência mínimos, retenção limitada e contratual, finalidade, responsável, aprovações do responsável pelos dados da Água e da segurança da FSTS, com uma data de expiração; 2 = um campo fraco; 1 = "enviar dados à Kell"; 0 = nada.

**EX036 — Estenda a conferência.** *Objetivo:* acrescentar uma verificação à ferramenta. *Entradas:* Laboratório 12. *Restrições:* apenas a biblioteca padrão. *Etapas:* (1) acrescente uma verificação que sinalize qualquer fluxo de dados `patient-linked` cujo destino não esteja numa lista aprovada `{"CLIN-GW", "HALDEN-CLOUD"}`, mesmo que registrado; (2) registre `("DF6", "CLIN-GW", "REPORTS", "patient-linked", True, 365)` e execute de novo; (3) explique por que o registro, por si só, não deveria tornar esse fluxo aceitável. *Evidência esperada:* código, saída, explicação. *Rubrica:* 3 = fluxo para REPORTS ainda sinalizado depois do registro; explicação de que o registro anota decisões, e um fluxo registrado para um público não aprovado é uma má decisão a revisar, e não um resultado limpo; 2 = o código funciona, explicação rasa; 1 = não executado; 0 = nada.

### Síntese do capítulo

Um registro de fluxos de dados anota quais dados viajam para onde, como são protegidos e por quanto tempo são guardados. Classifique os dados — telemetria, configuração, pessoais e vinculados a pacientes, logs de segurança — e verifique o registro contra o que os sistemas de fato enviam e retêm. A cifração protege o percurso, e não o destino. Os fluxos novos são revisados antes de começar, pelo responsável pelos dados, pela segurança e, quando há dados pessoais envolvidos, pela função de privacidade.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 30

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Infraestrutura crítica e segurança setorial: cenários de risco

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- escrever um **cenário** de risco como uma história específica: causa, caminho, ativo afetado, consequência para as pessoas e controles existentes;
- atribuir faixas de consequência e de probabilidade com motivos declarados, medindo a consequência em pessoas e tempo;
- ordenar os cenários com a **consequência primeiro** quando a safety está envolvida, e explicar por que o produto probabilidade × consequência pode enganar;
- transformar os principais cenários em trabalho de implementação com responsáveis.

A avaliação de riscos pode ser feita em muitas profundidades; o guia do NIST descreve um processo completo para organizações ([NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). Este capítulo ensina a versão do implementador: escrever cenários precisos o bastante para que um tecnólogo consiga construir, testar e monitorar os controles que eles implicam.

### 13.1 Cenários, e não categorias

"Ransomware" é uma categoria. Um cenário é: "Um ransomware entregue por um e-mail de phishing cifra o HIST-01; os dados das estações ainda chegam ao relay, que os armazena em buffer; os operadores perdem as telas de tendências e os relatórios semanais de conformidade até que o historiador seja restaurado." Um bom cenário nomeia a **causa**, o **caminho**, o **ativo afetado**, a **consequência** para as pessoas e para o serviço, e os **controles existentes**. Ele pode então ser testado ("o relay realmente armazena em buffer? por quanto tempo?") e monitorado.

O R2 passa no teste: credencial de fornecedor roubada, acesso remoto do fornecedor, setpoint de dosagem da PS-07, mudança de cloro na água que se bebe.

### 13.2 A consequência primeiro

A consequência descreve o que acontece às pessoas: quantas, por quanto tempo e se alguém poderia ser prejudicado. Uma faixa simples usa pessoas × horas de interrupção, com qualquer efeito crível de safety posto na faixa mais alta, quaisquer que sejam os números. A **probabilidade** é uma faixa de julgamento (de 1 a 5), informada pela exposição, pelas ameaças conhecidas e pelo histórico. Escreva o motivo de cada faixa; uma faixa sem motivo não pode ser contestada.

Muitos registros ordenam pelo produto probabilidade × consequência. O produto é conveniente e perigoso: trata um incômodo frequente e uma catástrofe rara como iguais se os produtos coincidirem, e deixa um problema visto com frequência, mas recuperável, passar à frente de um cenário de safety. Onde a safety é possível, ordene primeiro pela consequência e depois pela probabilidade dentro da faixa; use o produto, se usar, apenas dentro de uma faixa de consequência. Os métodos orientados por consequências desenvolvidos para a infraestrutura crítica adotam a mesma visão: partir dos desfechos que não podem acontecer ([INL CCE](https://inl.gov/national-security/cce/)).

### 13.3 Controles existentes e risco residual

Para cada cenário, registre os controles que já o reduzem e se eles foram testados (Capítulo 23). Um controle não testado é uma esperança, e não deveria baixar muito a faixa. O **risco residual** — o que sobra depois dos controles — precisa de um dono que o tenha aceitado, identificado pelo nome do papel, com uma data de revisão.

Para o R1, o ransomware no historiador, o controle-chave é o armazenamento em buffer dos dados das estações pelo relay enquanto o HIST-01 está fora. Até que esse buffer tenha sido testado parando o historiador de propósito e conferindo quantas horas o relay retém, ele é uma esperança, e a faixa baixa do R1 se apoia nele. O dono do risco residual do R1 seria a operação de Água, porque os relatórios de conformidade são dela.

### 13.4 Dos cenários ao trabalho

O valor do registro está no trabalho que ele produz. Para cada um dos principais cenários, liste as tarefas de implementação que reduziriam a consequência ou a probabilidade, e o monitoramento que o detectaria em andamento. Um registro que não produz tarefas é um documento; um que produz tarefas com responsáveis é um plano.

Para o R3, o enchimento do disco do relay, o trabalho é concreto: descobrir o que mantém os dados do RLY-01 além de 30 dias, definir um alerta de disco antes do alarme de 85 % e testar o comportamento do buffer quando o disco está cheio. Para o R2, são os controles da conta do fornecedor e o alerta fora de banda de cloro que aparecem como cartões de controle no Capítulo 18.

### 13.5 Exemplo resolvido: seis cenários de Fallowmere (sintético)

O Laboratório 13 ordena seis cenários. Dois carregam uma marca de safety — uma credencial de fornecedor roubada usada para mudar o setpoint de dosagem da PS-07 (R2), e uma interrupção do gateway clínico que impede as atualizações da biblioteca de medicamentos das bombas de infusão (R4) — e vão para a faixa de consequência 5. Ordenados com a consequência primeiro, R2 e R4 lideram, seguidos pelo enchimento do disco do relay (R3) e pela interrupção da operadora (R6). Ordenados pelo produto, R3 (16) e R6 (12) passam à frente dos dois cenários de safety (10 cada). A ordenação pelo produto mandaria o esforço do próximo trimestre para a capacidade de disco — útil, mas não onde o dano às pessoas é possível.

Note também o R1, o ransomware no historiador, no fim da lista, com consequência 1. Isso reflete o projeto: a telemetria e o controle continuam sem o historiador. Não é um motivo para ignorar o R1 — os relatórios de conformidade e as investigações dependem do historiador —, mas um motivo para confiar na propriedade de projeto do Capítulo 8, *se* o buffer do relay tiver sido testado.

O R2 merece uma nota. O LANTERN não transporta comandos, então o caminho do R2 não passa pelo LANTERN. Ele passa pelo acesso remoto do fornecedor ao sistema de controle. O registro de riscos de um tecnólogo deve incluir cenários que o serviço *não* causa, mas *precisa detectar ou apoiar*: a telemetria do LANTERN é como os operadores notariam uma mudança inesperada na dosagem.

### 13.6 Atividade prática: ordenação de cenários

**Laboratório 13** (salve como `lab13.py`, execute com `python3 lab13.py`):

```python
# Lab 13 - a small risk-scenario register ranked by consequence first (offline, standard library only)
# Synthetic: Fallowmere scenarios. Likelihood band 1-5 (judgement), consequence in service units.
scenarios = [  # id, scenario, likelihood band, people affected, hours of disruption, safety flag
 ("R1", "Ransomware encrypts historian; station data still reaches relay", 3, 0, 0, False),
 ("R2", "Stolen vendor credential used to change PS-07 dosing setpoint", 2, 41000, 24, True),
 ("R3", "Relay disk fills; telemetry dropped for remote stations", 4, 41000, 6, False),
 ("R4", "Clinical gateway outage stops infusion-pump library updates", 2, 300, 72, True),
 ("R5", "Depot kiosk defaced", 4, 0, 2, False),
 ("R6", "Upstream carrier outage isolates 6 stations", 3, 18000, 8, False),
]
def consequence_band(people, hours, safety):
    ph = people * hours
    band = 1 if ph == 0 else 2 if ph < 10_000 else 3 if ph < 100_000 else 4 if ph < 1_000_000 else 5
    return 5 if safety else band  # any credible safety effect goes to the top band
rows = []
for sid, text, lik, people, hours, safety in scenarios:
    c = consequence_band(people, hours, safety)
    rows.append((c, lik, sid, text, c * lik))
print("ranked by consequence, then likelihood:")
for c, lik, sid, text, prod in sorted(rows, key=lambda r: (-r[0], -r[1])):
    print(f"  {sid} C{c} L{lik} CxL={prod:>2}  {text}")
print("ranked by CxL product only:")
print("  " + " ".join(sid for c, lik, sid, text, prod in sorted(rows, key=lambda r: -r[4])))
```

Saída esperada (Python 3.13.5):

```text
ranked by consequence, then likelihood:
  R2 C5 L2 CxL=10  Stolen vendor credential used to change PS-07 dosing setpoint
  R4 C5 L2 CxL=10  Clinical gateway outage stops infusion-pump library updates
  R3 C4 L4 CxL=16  Relay disk fills; telemetry dropped for remote stations
  R6 C4 L3 CxL=12  Upstream carrier outage isolates 6 stations
  R5 C1 L4 CxL= 4  Depot kiosk defaced
  R1 C1 L3 CxL= 3  Ransomware encrypts historian; station data still reaches relay
ranked by CxL product only:
  R3 R6 R2 R4 R5 R1
```

Execute-o e compare as duas ordenações. Com a consequência primeiro, R2 e R4 lideram porque ambos carregam a marca de safety na faixa 5. Pelo produto, R3 com 16 e R6 com 12 os ultrapassam, e o R1 fica no fim de qualquer forma. Depois mude uma entrada que você considere incerta, como a probabilidade do R2, e veja se isso põe o R2 abaixo do R3. Se a ordenação com a consequência primeiro sobreviver à sua mudança e a ordenação pelo produto não, esse é o argumento a pôr diante de quem distribui o trabalho do próximo trimestre.

### 13.7 Erros comuns e limites

- Escrever categorias em vez de cenários.
- Faixas sem motivos.
- Ordenar pelo produto quando a safety está envolvida.
- Baixar a probabilidade por causa de controles que nunca foram testados.
- Risco residual sem dono.
- Deixar de fora cenários externos ao seu sistema que o seu sistema precisa detectar.

As faixas são julgamentos. O seu valor está em tornar o raciocínio explícito e comparável, e não em medir o risco com precisão.

O Laboratório 13 mostra o terceiro erro: ordenar pelo produto põe a capacidade de disco acima da dosagem de cloro.

Deixar de fora o R2 porque o LANTERN não transporta comandos seria o sexto erro: a telemetria do LANTERN é como os operadores notam uma mudança inesperada na dosagem.

### Exercícios — capítulo 13

**EX037 — Escreva dois cenários.** *Objetivo:* escrever cenários testáveis. *Entradas:* o projeto do LANTERN dos Capítulos 2 e 8. *Restrições:* cada um precisa nomear causa, caminho, ativo, consequência (pessoas e tempo) e controles existentes. *Etapas:* escreva um cenário sobre a operadora BayTel e um sobre o host de salto da FSTS. *Evidência esperada:* dois cenários de 80–120 palavras. *Rubrica:* 3 = específicos, testáveis, consequências em pessoas e tempo, controles nomeados com a situação de teste; 2 = um elemento vago; 1 = categorias; 0 = nada.

**EX038 — Produto versus consequência.** *Objetivo:* explicar uma escolha de ordenação a um gestor. *Entradas:* a saída do Laboratório 13. *Restrições:* 150 palavras; sem jargão. *Etapas:* explique por que R2 e R4 devem ser tratados antes do R3, embora o R3 tenha nota maior pelo produto, e do que o R3 ainda precisa. *Evidência esperada:* parágrafo. *Rubrica:* 3 = argumento claro sobre o possível dano às pessoas, a irrecuperabilidade e a falha do produto em pesar tudo igualmente; reconhece que o R3 ainda precisa de ação de capacidade (Capítulo 1) e é barato de corrigir; 2 = argumento parcial; 1 = apenas "safety primeiro"; 0 = nada.

**EX039 — Do cenário ao trabalho.** *Objetivo:* produzir tarefas de implementação. *Entradas:* R2 (credencial de fornecedor usada para mudar um setpoint de dosagem). *Restrições:* tarefas que a FSTS ou a Água conseguem entregar; cada uma com responsável e evidência de conclusão. *Etapas:* liste três tarefas de prevenção ou redução e duas de detecção. *Evidência esperada:* tabela. *Rubrica:* 3 = por exemplo, acesso de fornecedor limitado no tempo com MFA (Capítulo 7), registro das sessões, limites de setpoint no CLP projetados pela Água, alerta de telemetria para mudança de cloro/dosagem fora de uma janela aprovada, e comparação dos valores de setpoint com uma linha de base aprovada; responsáveis e evidências nomeados; 2 = tarefas genéricas; 1 = menos de três; 0 = nada.

### Síntese do capítulo

Escreva os riscos como cenários específicos — causa, caminho, ativo, consequência e controles —, para que possam ser testados e monitorados. Meça a consequência em pessoas e tempo, ponha os efeitos críveis de safety no topo e ordene com a consequência primeiro; o produto probabilidade × consequência pode deixar incômodos passarem à frente do dano. Dê um dono ao risco residual, inclua os cenários que o seu serviço precisa detectar e transforme o registro em tarefas.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 30

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Infraestrutura crítica e segurança setorial: métodos I

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- escrever uma **linha de base de configuração** para uma classe de host e mantê-la sob controle de versões;
- conduzir um **controle de mudanças** proporcional: mudanças padrão, normais e de emergência;
- planejar uma mudança num ambiente operacional, com verificações prévias, uma janela, um rollback e uma etapa de verificação;
- ligar toda mudança a evidências de que ela foi feita como aprovada.

Os Capítulos 1–13 descreveram sistemas, dados e riscos. Este capítulo e o Capítulo 16 tratam de *métodos*: as rotinas que um tecnólogo executa toda semana. Métodos I cobre linhas de base e mudanças, porque quase todos os outros controles dependem de saber como um sistema deveria ser e de controlar como ele muda.

### 14.1 Linhas de base de configuração

Uma **linha de base** é a configuração aprovada para uma classe de sistema: pacotes instalados e as suas versões, serviços habilitados e os seus endereços de escuta, contas e grupos, permissões de arquivos, configurações de logs e de hora, e parâmetros de segurança. O guia do NIST sobre gestão de configuração focada em segurança descreve como estabelecer linhas de base, controlar as mudanças nelas e monitorar desvios ([NIST SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final)). Escreva a linha de base como um arquivo sob controle de versões, e não como um documento na pasta de alguém: o Capítulo 22 a usa para detectar a deriva automaticamente.

### 14.2 Um controle de mudanças que as pessoas vão usar

O controle de mudanças existe para impedir que mudanças não revisadas causem interrupções ou enfraqueçam a segurança. Processos pesados demais são contornados; é assim que surgem listeners de depuração e scripts auxiliares sem explicação (Capítulo 6). Um esquema proporcional tem três tipos de mudança:

- **Mudanças padrão** — pré-aprovadas, de baixo risco, repetíveis (acrescentar uma estação à allowlist a partir de uma solicitação aprovada). Seguem um procedimento escrito e são registradas.
- **Mudanças normais** — revisadas e aprovadas antes da implementação, com um plano e um rollback.
- **Mudanças de emergência** — feitas rapidamente para restaurar o serviço ou conter um incidente, aprovadas por uma autoridade de plantão nomeada e revisadas depois.

Na TO, a aprovação de qualquer mudança que possa afetar o processo físico inclui o responsável pela operação, e não apenas a TI.

### 14.3 Planejar uma mudança num ambiente operacional

Um plano de mudança do LANTERN declara: o que vai mudar e por quê; os sistemas e clientes afetados; as verificações prévias (backups feitos, rollback preparado, operação informada); a **janela** (acordada com a operação — não durante o pico de demanda da manhã nem durante uma execução programada de relatórios); a implementação passo a passo; a **verificação** (como você vai saber que funcionou — verificações específicas, e não "testar o serviço"); os critérios e as etapas do **rollback**; e para quem ligar. O Capítulo 27 estende isso para implantações com canários.

Mover o listener SSH do RLY-02 é um caso típico: o rollback não pode depender do SSH.

### 14.4 Evidências da mudança

Depois de uma mudança, três coisas devem concordar: o registro da mudança (o que foi aprovado), a linha de base sob controle de versões (o que agora deveria ser verdade) e o próprio sistema (o que é verdade, verificado pela verificação de integridade do Capítulo 6 e pela verificação de deriva do Capítulo 22). Quando discordam, ou a mudança não foi feita como aprovada, ou o registro está errado. As duas coisas são constatações.

Depois da CHG-118, as três concordavam para `allow.list` e discordavam para o listener de depuração.

Para o listener de depuração não havia registro de mudança algum, então a própria discordância foi a constatação, e ela levou à investigação do Capítulo 6.

### 14.5 Exemplo resolvido: acrescentar a PS-11 (sintético)

A operação de Água comissiona uma nova estação, a PS-11. Acrescentá-la ao LANTERN é uma mudança padrão com um procedimento escrito: (1) receber a solicitação de comissionamento com o ID da estação, o endereço e o responsável; (2) confirmar que o conduíte já cobre a sub-rede da estação; (3) acrescentar `PS-11` à allowlist sob controle de versões, com revisão de um segundo tecnólogo; (4) implantar a allowlist nos relays; (5) verificar: as primeiras mensagens da PS-11 aparecem como `accept` no log do relay; a verificação de integridade mostra que `allow.list` mudou sob a CHG-118 e nada mais; (6) atualizar o inventário e o registro de fluxos de dados. No laboratório do Capítulo 6, essa foi a única diferença *aprovada*. As outras três diferenças não tinham registro de mudança — e foi assim que o método as revelou.

### 14.6 Atividade prática: escreva um plano de mudança normal

Escreva um plano de mudança completo para: "Mover o listener SSH do RLY-02 de todas as interfaces apenas para a interface de gerenciamento." Inclua todos os elementos do Capítulo 14 ("Planejar uma mudança num ambiente operacional"). Preste atenção ao risco de se trancar do lado de fora: como você vai alcançar o host se a mudança falhar?

Para a mudança do RLY-02, um plano seguro mantém uma segunda forma de entrar: acesso ao console pelo hipervisor, ou uma sessão aberta na interface de gerenciamento, testada antes que o listener seja movido. A verificação é específica: o SSH responde no endereço de gerenciamento, não responde no endereço voltado às estações, e a verificação de deriva mostra que só a linha pretendida mudou. Escolha a janela com a operação de Água, evitando o pico de demanda da manhã e as execuções semanais de relatórios nos dias 6 e 7.

### 14.7 Erros comuns e limites

- Linhas de base mantidas como documentos que ninguém compara com os sistemas.
- Processos de mudança tão pesados que as pessoas os contornam.
- Janelas de mudança escolhidas pela conveniência da TI, e não da operação.
- "Verificar se o serviço funciona" como etapa de verificação.
- Planos de rollback que nunca foram testados.
- Mudanças de emergência nunca revisadas depois, que assim se tornam permanentes.

O controle de mudanças controla as mudanças *autorizadas*. Ele não detecta mudanças não autorizadas; esse é o trabalho das verificações de integridade e de deriva.

A fusão do NTP no Capítulo 25 é o quarto erro na prática: o seu critério de aceitação dizia apenas "atualizar os servidores NTP".

### Exercícios — capítulo 14

**EX040 — Classifique as mudanças.** *Objetivo:* aplicar um controle de mudanças proporcional. *Entradas:* (a) acrescentar uma estação à allowlist; (b) atualizar o software do relay para uma nova versão menor; (c) desabilitar uma conta de fornecedor comprometida às 02:00; (d) mudar a retenção do historiador de 730 para 365 dias; (e) rotacionar a chave HMAC do relay. *Restrições:* padrão, normal ou de emergência para cada uma, com um motivo. *Etapas:* classifique e diga quem aprova. *Evidência esperada:* tabela. *Rubrica:* 3 = (a) padrão, (b) normal, (c) de emergência, com aprovação do plantão e revisão, (d) normal, com aprovação do responsável pelos dados, porque afeta registros e obrigações, (e) normal (ou padrão, quando existir um procedimento testado), coordenada com as estações; aprovadores sensatos; 2 = uma mal classificada; 1 = todas normais; 0 = nada.

**EX041 — Etapas de verificação.** *Objetivo:* escrever uma verificação específica. *Entradas:* a mudança "o relay encaminha ao HIST-01 por TLS 1.3 em vez de TLS 1.2". *Restrições:* pelo menos quatro verificações; cada uma observável. *Etapas:* liste as verificações e a evidência que cada uma produz. *Evidência esperada:* lista. *Rubrica:* 3 = por exemplo, o log de conexões mostra TLS 1.3 negociado, o historiador recebe leituras de todas as estações dentro da latência normal, nenhum aumento de erros ou rejeições no relay, a validação de certificados continua aplicada, a verificação de integridade mostra que só o arquivo aprovado mudou; 2 = três; 1 = "testar"; 0 = nada.

**EX042 — Revise uma mudança de emergência.** *Objetivo:* fechar o ciclo de uma mudança de emergência. *Entradas:* durante uma interrupção às 03:00, um engenheiro abriu a tcp/22 da zona corporativa diretamente para todos os relays, "temporariamente". *Restrições:* revisão pós-mudança em até um dia útil. *Etapas:* (1) liste as perguntas que a revisão faz; (2) decida o que acontece com a regra; (3) diga qual mudança de processo impede uma repetição. *Evidência esperada:* nota de revisão. *Rubrica:* 3 = pergunta por que a rota pelo host de salto falhou, quem aprovou, o que foi acessado durante a janela (logs), remove ou estreita a regra com um registro de mudança, corrige a resiliência do host de salto ou o projeto do acesso de emergência; 2 = regra removida, mas sem causa raiz; 1 = regra mantida; 0 = nada.

### Síntese do capítulo

Escreva as configurações aprovadas como linhas de base sob controle de versões. Conduza o controle de mudanças de forma proporcional — padrão, normal e de emergência —, com a operação aprovando as mudanças que podem afetar o processo físico. Planeje as mudanças com verificações prévias, uma janela acordada, uma verificação específica e um rollback testado. Depois de toda mudança, o registro, a linha de base e o sistema devem concordar; quando não concordam, você tem uma constatação.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 30

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Infraestrutura crítica e segurança setorial: laboratório guiado

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- explicar o que um **código de autenticação de mensagem** (MAC) prova e o que ele não prova;
- implementar a selagem e a verificação com HMAC-SHA-256, com comparação em tempo constante;
- acrescentar **atualidade** (janela de tempo) e **ordem** (números de sequência) para derrotar a reprodução;
- testar a construção com mensagens deliberadamente ruins e registrar os resultados como evidência.

Esta é a primeira construção guiada do componente central do LANTERN. O validador do Capítulo 3 confere se as mensagens são bem formadas e plausíveis; ele não consegue dizer se uma mensagem realmente veio de uma estação. Aqui você acrescenta a autenticação. O projeto é deliberadamente simples, para que cada linha possa ser entendida; um projeto de produção acrescentaria gestão de chaves e segurança de transporte (veja "O que esta construção não faz", abaixo).

### 15.1 Integridade e autenticidade

Um **hash** como o SHA-256 detecta mudanças acidentais, mas qualquer um pode calculá-lo, então um atacante que muda uma mensagem também pode recalcular o seu hash. Um **MAC** é calculado com uma chave secreta; apenas quem detém a chave consegue produzir um MAC válido. O HMAC, definido na [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104), constrói um MAC a partir de uma função de hash. Se uma mensagem carrega um HMAC válido sob a chave de uma estação, o receptor sabe que ela foi produzida por quem detém a chave e não foi alterada em trânsito.

Um MAC **não** fornece confidencialidade (a mensagem continua legível), não prova que o *sensor* da estação está certo e não impede que um atacante reenvie uma mensagem capturada antes — uma **reprodução**.

### 15.2 Forma canônica

Um MAC é calculado sobre bytes. Se o remetente e o receptor serializarem a mesma mensagem de formas diferentes — ordem de chaves diferente, espaçamento diferente —, a verificação falha. As mensagens do LANTERN são serializadas como JSON com chaves ordenadas e sem espaços, e o MAC é calculado exatamente sobre esses bytes. Defina sempre a forma canônica de modo explícito.

Um relay que reserializa o JSON interpretado antes de conferir o MAC pode aceitar bytes que a estação nunca assinou.

O Laboratório 15 serializa com chaves ordenadas e sem espaços dos dois lados, de modo que o gateway da estação e o relay calculam o MAC sobre bytes idênticos; uma atualização de firmware do gateway que mudasse o espaçamento apareceria de imediato como uma rajada de falhas de MAC daquela estação.

### 15.3 Comparação em tempo constante

Comparar o MAC recebido com o esperado usando uma comparação comum de strings pode vazar, pelo tempo, quantos caracteres iniciais coincidiram. O `hmac.compare_digest` do Python compara num tempo independente de onde as entradas diferem ([documentação do hmac do Python](https://docs.python.org/3/library/hmac.html)). Use-o em toda comparação de MAC.

O Laboratório 15 e o Laboratório 29 usam ambos `hmac.compare_digest`, nunca `==`, e o relay que rejeitou 40 de 40 testes de falha de MAC no Capítulo 23 precisa fazer o mesmo.

Uma comparação comum permitiria que um atacante na rede da estação descobrisse, um caractere de cada vez, um MAC válido para uma leitura de cloro forjada.

### 15.4 Atualidade e ordem

Duas verificações baratas derrotam a reprodução. Uma **janela de tempo** rejeita as mensagens cujo carimbo de tempo esteja a mais de um número definido de segundos do relógio do receptor (aqui, 120 s); ela depende de os dois relógios estarem certos (Capítulo 17). Um **número de sequência** por estação, que cresce a cada mensagem, permite ao receptor rejeitar qualquer mensagem cujo número não seja maior que o último aceito. Os dois valores ficam dentro do corpo autenticado pelo MAC, então um atacante não consegue alterá-los sem invalidar o MAC.

O erro de relógio de 422 segundos da PS-09 mostra o custo: as suas mensagens genuínas falhariam na janela de 120 s.

### 15.5 Construção guiada

O laboratório abaixo implementa `seal` (o lado da estação) e `Relay.receive` (o lado do relay) e executa sete testes: duas mensagens boas, uma reprodução, um valor adulterado, uma mensagem selada com a chave errada, uma mensagem velha e uma mensagem truncada.

**Laboratório 15** (salve como `lab15.py`, execute com `python3 lab15.py`):

```python
# Lab 15 - guided build: an authenticated telemetry relay message with replay protection (offline, stdlib only)
# Synthetic key and messages. A real deployment keeps the key in a protected store, never in source code.
import hmac, hashlib, json
KEY = bytes.fromhex("6c616e7465726e2d6c61622d6b65792d6e6f742d7265616c2d30303031")  # "lantern-lab-key-not-real-0001"
WINDOW = 120  # seconds
def seal(station, tag, value, ts, seq, key=KEY):
    body = json.dumps({"st": station, "tag": tag, "v": value, "ts": ts, "seq": seq}, sort_keys=True, separators=(",", ":"))
    mac = hmac.new(key, body.encode(), hashlib.sha256).hexdigest()
    return body + "." + mac
class Relay:
    def __init__(self, key): self.key, self.last = key, {}
    def receive(self, wire, now):
        try:
            body, mac = wire.rsplit(".", 1)
        except ValueError:
            return "reject: malformed"
        good = hmac.new(self.key, body.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(good, mac):
            return "reject: bad MAC"
        m = json.loads(body)
        if abs(now - m["ts"]) > WINDOW:
            return "reject: outside time window"
        if m["seq"] <= self.last.get(m["st"], -1):
            return "reject: replay"
        self.last[m["st"]] = m["seq"]
        return f"accept {m['st']} {m['tag']}={m['v']}"
r = Relay(KEY)
now = 1_790_000_000
a = seal("PS-04", "LEVEL_M", 3.42, now - 5, 1)
b = seal("PS-04", "LEVEL_M", 3.44, now - 1, 2)
tampered = a.replace('"v":3.42', '"v":9.42')
forged = seal("PS-04", "LEVEL_M", 1.00, now, 3, key=b"guessed-key")
old = seal("PS-07", "CL2_MGL", 0.6, now - 900, 1)
tests = [("first", a), ("second", b), ("replay of first", a), ("tampered value", tampered),
         ("wrong key", forged), ("stale", old), ("truncated", a[:20])]
for name, wire in tests:
    print(f"{name:<16} {r.receive(wire, now)}")
print("MAC length (hex chars):", len(a.rsplit('.', 1)[1]))
```

Saída esperada (Python 3.13.5):

```text
first            accept PS-04 LEVEL_M=3.42
second           accept PS-04 LEVEL_M=3.44
replay of first  reject: replay
tampered value   reject: bad MAC
wrong key        reject: bad MAC
stale            reject: outside time window
truncated        reject: malformed
MAC length (hex chars): 64
```

Trabalhe nesta ordem: (1) leia `seal` e identifique a forma canônica; (2) leia `receive` e liste as verificações, em ordem; (3) preveja o resultado de cada teste; (4) execute; (5) para cada rejeição, nomeie a verificação que a pegou. Depois mude a ordem das verificações para que a verificação de reprodução *e a sua atualização de estado* rodem antes da verificação do MAC, e pense no que um atacante poderia fazer agora: enviar mensagens não autenticadas com números de sequência altos e bloquear uma estação. A ordem importa — autentique primeiro, depois confie no conteúdo.

### 15.6 O que esta construção não faz

A chave do laboratório está impressa no código-fonte porque é falsa; em produção, a chave fica num armazenamento protegido, legível apenas pela conta de serviço do relay, e cada estação tem a sua própria chave, para que uma chave roubada não permita a um atacante se passar por todas as estações. As chaves precisam de procedimentos de geração, distribuição, rotação e revogação (Capítulo 18). O transporte aqui não é cifrado; em produção, o trecho relay–historiador usa TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), e se o trecho da estação pode usar TLS depende do que os dispositivos de campo suportam. Muitos dispositivos de campo mais antigos nem conseguem calcular HMACs; nesse caso, o MAC é aplicado por um pequeno gateway na estação, e o enlace gateway–dispositivo precisa ser protegido fisicamente.

### 15.7 Erros comuns e limites

- Usar um hash simples e chamá-lo de autenticação.
- Calcular o MAC sobre um objeto reserializado, em vez dos bytes recebidos.
- Comparar MACs com `==`.
- Atualizar o estado de reprodução antes da autenticação — ou antes que todas as outras verificações tenham passado.
- Uma única chave compartilhada por todas as estações.
- Chaves no código-fonte, em repositórios de configuração ou em tickets.
- Presumir que um MAC válido significa uma leitura correta.

Cada um tem uma consequência no LANTERN. Um hash simples permite que qualquer um que alcance o relay calcule um digest de aparência válida. Uma chave para todas as estações significa que uma chave retirada do gateway da PS-07, onde o arquivo da chave ficava num cartão removível, forja mensagens para todas as catorze estações. E um MAC válido numa leitura de cloro de 9,80 mg/L prova apenas que a PS-07 a enviou, e não que o analisador está certo.

### Exercícios — capítulo 15

**EX043 — Ordem das verificações.** *Objetivo:* ver por que a autenticação vem primeiro. *Entradas:* Laboratório 15. *Restrições:* modifique uma cópia. *Etapas:* (1) mova a verificação de reprodução para antes da verificação do MAC, mantendo a atualização de estado onde está; (2) monte uma mensagem não autenticada para a PS-04 com `seq` 1000000 e um MAC errado; (3) envie-a, e depois uma mensagem genuína com `seq` 3; (4) relate o que acontece e por que a ordem original é mais segura. *Evidência esperada:* código, saída e explicação. *Rubrica:* 3 = mostra que, com o estado atualizado antes da autenticação, um atacante consegue bloquear as mensagens futuras de uma estação (ou, se a atualização de estado ficar depois da verificação do MAC, mostra que não há bloqueio e explica por que a posição da atualização é a verdadeira salvaguarda); a explicação se liga a "autenticar, depois confiar"; 2 = observação sem explicação; 1 = não executado; 0 = nada.

**EX044 — Chaves por estação.** *Objetivo:* estender o projeto. *Entradas:* Laboratório 15. *Restrições:* apenas a biblioteca padrão. *Etapas:* (1) dê a cada estação a sua própria chave num dicionário; (2) busque a chave pelo ID da estação — mas note que o ID da estação fica dentro do corpo; (3) explique como você pode ler com segurança o ID da estação antes de verificar o MAC, e o que você não pode fazer com ele antes da verificação. *Evidência esperada:* código e explicação. *Rubrica:* 3 = interpreta o corpo apenas para selecionar uma chave, verifica o MAC com essa chave antes de usar qualquer outro campo ou atualizar o estado, rejeita estações desconhecidas; explica que o ID não verificado é apenas um seletor de chave; 2 = funciona, explicação rasa; 1 = usa uma única chave; 0 = nada.

**EX045 — Tamanho da janela.** *Objetivo:* escolher a janela de atualidade. *Entradas:* os relógios das estações são mantidos dentro de ±2 s por NTP a partir do relay; a operadora às vezes atrasa mensagens em até 40 s; depois de uma interrupção da operadora, as estações enviam um acúmulo de 24 horas. *Restrições:* um projeto que trate os três. *Etapas:* (1) escolha uma janela para as mensagens ao vivo; (2) explique como os envios de acúmulo devem ser tratados sem abrir uma brecha de reprodução. *Evidência esperada:* meia página. *Rubrica:* 3 = janela ao vivo de cerca de 60–120 s, com raciocínio; acúmulo aceito por um caminho separado e explícito (por exemplo, um modo de acúmulo sinalizado que ainda exige MAC válido e números de sequência estritamente crescentes, com uma idade limitada e um alerta quando usado); 2 = janela certa, acúmulo inseguro ou vago; 1 = janela muito grande para tudo; 0 = nada.

### Síntese do capítulo

Autentique as mensagens com HMAC sobre uma forma canônica definida, compare os MACs em tempo constante e derrote a reprodução com uma janela de tempo e números de sequência por estação levados dentro do corpo autenticado. Autentique primeiro, depois confie no conteúdo e registre-o. Um MAC prova a origem e a integridade, e não a confidencialidade nem a correção do sensor. As chaves precisam do seu próprio ciclo de vida, e cada estação deve ter a sua.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 30

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Infraestrutura crítica e segurança setorial: métodos II

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- conduzir uma rotina de tratamento de vulnerabilidades: recebimento, aplicabilidade, priorização, tratamento e verificação;
- priorizar correções usando evidências de exploração, exposição e consequência para o ativo, e não apenas a nota de severidade;
- planejar a aplicação de patches quando o dispositivo não pode ser corrigido rapidamente, usando controles compensatórios com data de término;
- projetar, executar e registrar backups e **testes de restauração** que provem a recuperação dentro de um tempo-alvo.

Métodos I (Capítulo 14) controlou as mudanças. Métodos II cobre as duas rotinas que mais costumam decidir quão ruim um dia ruim fica: lidar com as vulnerabilidades antes que sejam exploradas, e recuperar quando algo se perde de qualquer forma.

### 16.1 Recebimento de vulnerabilidades e aplicabilidade

Os alertas chegam de fornecedores, de agências nacionais e de listas de discussão de segurança. A primeira pergunta é a **aplicabilidade**: rodamos o produto e a versão afetados, numa configuração em que a falha importa? Isso depende de o inventário (Capítulo 11) estar correto quanto às versões. Registre a decisão — "aplicável", "não aplicável (motivo)", "desconhecido (ação para descobrir)" — para todo alerta que toque um produto do inventário. "Desconhecido" é comum na TO e precisa ter um responsável.

Para o alerta do Arlen 300, o inventário tinha as duas versões: PS04-PLC na 4.2 e PS07-PLC na 3.9.

### 16.2 Priorização

Uma nota de severidade descreve a falha em geral; a sua prioridade depende da sua situação. Três perguntas a tornam mais precisa. **Ela está sendo explorada?** O catálogo Known Exploited Vulnerabilities da CISA lista falhas com evidência de exploração ativa ([CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)); essas entradas passam para a frente. **Ela está exposta?** Uma falha alcançável a partir da internet ou da zona corporativa é mais urgente do que uma alcançável apenas de dentro de um conduíte bem controlado. **Qual é a consequência?** Uma falha num ativo de criticidade 1 na zona das estações importa mais do que uma num quiosque da garagem. A orientação sobre gestão de patches trata isso como um agendamento baseado em risco, com planos de manutenção definidos para diferentes grupos de ativos ([NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final)).

### 16.3 Tratamento quando não dá para aplicar o patch rapidamente

Os controladores das estações podem precisar de firmware certificado pelo fornecedor, de uma visita ao local, de uma janela de interrupção e de novos testes do processo. O tratamento tem então duas partes: **controles compensatórios agora** (restringir mais o conduíte, desabilitar a função vulnerável se não for usada, acrescentar monitoramento de tentativas de exploração, aumentar a revisão da configuração do dispositivo) e **um plano com data** para a correção. Registre ambos, e o dono do risco residual (Capítulo 13). Lembre-se do Capítulo 9: esses itens em aberto há muito tempo precisam aparecer nas suas medidas de patches.

PS04-PLC e PS07-PLC são o caso de Fallowmere: desabilitar a interface web não usada, fechar o caminho corporativo→PS-04, alertar sobre a porta web, e depois o firmware 4.3 nas próximas visitas ao local.

### 16.4 Verificação

Uma correção está completa quando é verificada no dispositivo: a versão é confirmada (a partir do dispositivo ou da sua exportação de engenharia, e não do ticket), o serviço funciona (as verificações do Capítulo 27) e os controles compensatórios que não são mais necessários são removidos sob controle de mudanças — do contrário, as regras temporárias se acumulam.

Para o PS07-PLC, a versão foi lida no dispositivo durante a visita ao local: 3.9, como registrado, então a correção continua em aberto. Quando a 4.3 for instalada, a evidência será a exportação do engenheiro mostrando 4.3, e o alerta sobre a porta web do CLP será mantido ou removido pelo seu próprio registro de mudança.

### 16.5 Backups e testes de restauração

Um backup que nunca foi restaurado é uma esperança. O guia do NIST de planejamento de contingência cobre o planejamento e o teste de backup e recuperação ([NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)), e o guia do NIST sobre recuperação de eventos cibernéticos enfatiza preparar e exercitar a recuperação com antecedência ([NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final)). Para o LANTERN:

- **O que** tem backup: a configuração e a allowlist do relay (já sob controle de versões), as chaves (no próprio backup do seu armazenamento protegido), o banco de dados do historiador, os programas e as configurações dos controladores (pelos engenheiros da Água) e a documentação necessária para reconstruir.
- **Onde**: pelo menos uma cópia offline ou imutável, para que um ransomware ou um erro de administrador não consiga apagar todas as cópias.
- **Metas**: um **objetivo de tempo de recuperação** (RTO — com que rapidez o serviço precisa voltar) e um **objetivo de ponto de recuperação** (RPO — quanta perda de dados é tolerável). Para o HIST-01 em Fallowmere: RTO de 4 horas, RPO de 24 horas.
- **Testes de restauração**: agendados, cronometrados, registrados, com o resultado comparado às metas; o Capítulo 9 mostra como relatá-los com honestidade.

### 16.6 Exemplo resolvido: um alerta para o Arlen 300 (sintético)

Um alerta relata uma falha na interface web de gerenciamento do CLP Arlen 300, firmware abaixo da 4.3, agora listada como explorada em outros lugares (sintético). Aplicabilidade: o PS04-PLC roda a 4.2 e o PS07-PLC roda a 3.9 — ambos aplicáveis. Exposição: a interface web deveria ser alcançável apenas pelo caminho de salto de engenharia; mas a revisão de fluxos do Capítulo 2 encontrou uma estação de trabalho corporativa conversando diretamente com a PS-04. Prioridade: alta nas três perguntas. Tratamento: hoje, confirmar com o engenheiro da Água se a interface web é usada e, se não for, desabilitá-la; fechar o caminho corporativo→PS-04 (já levantado); acrescentar um alerta para qualquer conexão à porta web dos CLPs. Correção: firmware 4.3 nas próximas visitas ao local, com os testes de processo da Água. Verificação: versão lida na exportação de engenharia; alerta e conduíte testados.

### 16.7 Atividade prática: registro de vulnerabilidade

Escreva o registro completo para o alerta do Capítulo 16 ("Exemplo resolvido: um alerta para o Arlen 300"): aplicabilidade por ativo, prioridade com os motivos para cada uma das três perguntas, controles compensatórios com evidências, plano de correção com datas e responsáveis, etapas de verificação e o dono do risco residual.

A prioridade do PS04-PLC se apoia em três respostas: aplicável (a 4.2 está abaixo da 4.3), explorada em outros lugares e exposta, porque a revisão de fluxos viu uma estação de trabalho corporativa conversando com a PS-04. O PS07-PLC é aplicável e explorado, mas nenhum caminho não declarado foi visto, então o seu motivo de exposição é mais fraco. Nomeie a operação de Água como dona do risco residual até que a 4.3 seja verificada nos dois.

### 16.8 Erros comuns e limites

- Priorizar apenas pela nota de severidade.
- Marcar "não aplicável" sem conferir as versões.
- Deixar "desconhecido" sem responsável.
- Controles compensatórios sem data de término, que assim se tornam permanentes.
- Fechar o ticket quando o patch é agendado, e não quando é verificado.
- Backups guardados onde a mesma conta de administrador consegue apagar todas as cópias.
- Medir o sucesso do backup pela conclusão da tarefa, em vez de por testes de restauração.

Os dois CLPs mostram o risco do quinto erro: o ticket fecharia em "firmware 4.3 agendado", enquanto a 3.9 continua rodando na PS-07.

A 4.2 do PS04-PLC teria sido marcada como não aplicável por quem lesse apenas a nota do alerta.

### Exercícios — capítulo 16

**EX046 — Priorize três alertas.** *Objetivo:* aplicar exploração, exposição e consequência. *Entradas:* (a) falha de severidade crítica no navegador do quiosque da garagem, sem exploração conhecida, quiosque na rede da garagem com acesso à internet; (b) falha de severidade média no servidor SSH do relay, listada no KEV, SSH alcançável apenas a partir do host de salto; (c) falha de severidade alta no banco de dados do HIST-01, sem exploração conhecida, alcançável a partir da zona corporativa. *Restrições:* ordene e justifique com uma frase cada. *Etapas:* ordene, depois dê uma data-alvo para cada uma. *Evidência esperada:* tabela. *Rubrica:* 3 = (b) em primeiro lugar por causa da exploração ativa e da criticidade, apesar da nota média e da exposição restrita; depois uma ordenação defensável de (c) e (a), com motivos (consequência do historiador contra a exposição à internet do quiosque); datas proporcionais; 2 = ordenação defensável, motivos rasos; 1 = só pela severidade; 0 = nada.

**EX047 — Plano de controles compensatórios.** *Objetivo:* tratar uma vulnerabilidade que não pode ser corrigida rapidamente. *Entradas:* Capítulo 16 ("Exemplo resolvido: um alerta para o Arlen 300"); o firmware 4.3 só pode ser instalado na PS-07 daqui a 10 semanas. *Restrições:* pelo menos três controles, cada um com evidência e data de término. *Etapas:* escreva o plano. *Evidência esperada:* tabela. *Rubrica:* 3 = desabilitar a interface web se não for usada (evidência: exportação de engenharia), restrição do conduíte verificada por revisão de fluxos, alerta sobre conexões à porta web testado, comparação de configuração mais frequente; todos terminando quando a 4.3 for verificada; 2 = sem datas de término; 1 = "monitorar"; 0 = nada.

**EX048 — Projeto de teste de restauração.** *Objetivo:* projetar um teste de restauração que prove o RTO. *Entradas:* HIST-01, RTO de 4 h, RPO de 24 h. *Restrições:* não pode perturbar a produção; precisa ser repetível. *Etapas:* (1) descreva o ambiente de teste; (2) as etapas e os pontos de cronometragem; (3) os critérios de aprovação; (4) o que é registrado. *Evidência esperada:* uma página. *Rubrica:* 3 = destino de restauração isolado, parte da cópia offline/imutável, cronometra da "decisão de restaurar" até "os operadores conseguem consultar os dados", confere a atualidade dos dados contra o RPO, registra tempos, lacunas e lições, e é agendado com regularidade; 2 = falta a cronometragem ou a verificação do RPO; 1 = "conferir se a tarefa de backup teve sucesso"; 0 = nada.

### Síntese do capítulo

Trate as vulnerabilidades como uma rotina: decida a aplicabilidade a partir do inventário, priorize por exploração, exposição e consequência, aplique controles compensatórios com datas de término onde a aplicação de patches é lenta e verifique as correções no dispositivo. Faça backup do que você precisa para reconstruir, mantenha uma cópia que não possa ser apagada pelas mesmas pessoas que operam a produção, defina o RTO e o RPO e prove-os com testes de restauração cronometrados.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 30

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Infraestrutura crítica e segurança setorial: ferramental

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- configurar sistemas para produzir logs que respondam a perguntas operacionais e de segurança;
- manter os relógios sincronizados e registrar o tempo num formato único e sem ambiguidade;
- **normalizar** logs de fontes diferentes numa estrutura comum;
- escrever e testar uma pequena ferramenta para poder confiar na sua saída, e saber quando usar uma existente em vez disso.

O monitoramento (Capítulo 19), a resolução de problemas (Capítulo 20) e a avaliação (Capítulo 23) dependem todos de logs. A maioria das falhas de log não é a falta de produtos, mas a falta do básico: uma fonte que nunca encaminhou, um carimbo de tempo sem fuso horário, um parser que descarta em silêncio as linhas que não entende.

### 17.1 O que registrar

Registre o que você vai precisar para responder às perguntas que lhe farão: quem fez login, de onde, com que resultado; que configuração mudou; o que o relay aceitou, rejeitou e quarentenou, com contagens; quais fluxos atravessaram fronteiras de zona; quando os serviços iniciaram, pararam ou falharam. O guia do NIST de gestão de logs cobre o planejamento, a geração, a transmissão, o armazenamento e a análise de logs ([NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final)). Encaminhe os logs para fora do host prontamente — não se pode confiar que um host comprometido ou com defeito guarde os seus próprios registros — e monitore se o encaminhamento continua.

### 17.2 Tempo

Ordenar eventos entre sistemas exige um tempo acordado. Sincronize todo host com uma fonte de tempo confiável usando NTP ([RFC 5905](https://www.rfc-editor.org/rfc/rfc5905)); no LANTERN, os relays tomam a hora de dois servidores internos e a fornecem às estações. Registre os carimbos de tempo num formato com deslocamento explícito, como os definidos na [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), e converta para UTC na análise. Monitore o próprio deslocamento do relógio: um host cuja fonte de tempo falhou deriva devagar e em silêncio.

### 17.3 Logs estruturados e syslog

O protocolo syslog, [RFC 5424](https://www.rfc-editor.org/rfc/rfc5424), define uma mensagem com prioridade (facility e severidade), versão, carimbo de tempo, nome do host, nome da aplicação, ID do processo, ID da mensagem, **dados estruturados** (parâmetros chave–valor entre colchetes) e uma mensagem em texto livre. Os dados estruturados são o que torna os logs pesquisáveis: `src="192.0.2.44" user="root"` pode ser contado e filtrado; a mesma informação enterrada em prosa precisa ser adivinhada com padrões. Dispositivos mais antigos costumam enviar o formato BSD anterior, sem ano nem fuso horário; registre essas fontes como de qualidade inferior e converta com cuidado.

### 17.4 Normalização

Um **normalizador** transforma o formato de cada fonte num registro comum: hora em UTC, host, aplicação, severidade e campos nomeados como `src`, `user`, `dst`, `dport`, `action`. As regras posteriores (Capítulo 19) são então escritas uma só vez. Um normalizador precisa **contar o que não consegue interpretar** e relatá-lo: os descartes silenciosos são como um sistema de monitoramento fica cego para a única fonte que mudou de formato.

A linha em formato BSD do relay, na noite do exemplo resolvido, mostra por quê: sem uma contagem de não interpretadas, ela simplesmente teria desaparecido.

A linha do quiosque sem carimbo de tempo algum é o outro caso: o normalizador precisa sinalizá-la, e não carimbá-la com a hora de chegada.

### 17.5 Ferramentas em que você pode confiar

Os implementadores escrevem pequenas ferramentas o tempo todo. A confiança na saída de uma ferramenta vem de: uma declaração clara do que ela trata e do que não trata; testes com casos ruins e de borda (Capítulo 3); contagens de entradas, saídas e rejeições que fecham; saída determinística para a mesma entrada; e controle de versões. Escreva a sua própria ferramenta quando a tarefa for pequena e específica; use uma ferramenta estabelecida e mantida quando a tarefa for geral (um coletor syslog completo, uma biblioteca TLS, um banco de dados). Nunca escreva a sua própria criptografia — use a da biblioteca padrão.

### 17.6 Exemplo resolvido: os logs de uma noite (sintético)

O Laboratório 17 interpreta sete linhas do relay, do firewall, do historiador e do quiosque da garagem. Seis são interpretadas, uma não: uma linha em formato BSD da própria aplicação do relay, revelando que um componente do LANTERN nunca foi configurado para o formato acordado. Uma linha não tem carimbo de tempo algum (o quiosque). A linha do historiador traz `+01:00`; convertida para UTC, ela é 22:02:11 — *antes* dos eventos de SSH, e não depois, como a sua hora local sugere. Ordenada em UTC, a noite se lê assim: erro de cota de disco do historiador às 22:02, um login legítimo de administrador às 22:14, dois logins de root malsucedidos a partir de um endereço externo às 22:15, e um fluxo Modbus corporativo-para-PS-04 às 22:16, a partir da mesma estação de trabalho usada no login de administrador.

### 17.7 Atividade prática: normalizador

**Laboratório 17** (salve como `lab17.py`, execute com `python3 lab17.py`):

```python
# Lab 17 - normalizing RFC 5424-style syslog lines into JSON records (offline, standard library only)
# Synthetic log lines from the relay, historian and firewall. Simplified parser for teaching, not a full RFC 5424 implementation.
import json, re
from datetime import datetime, timezone
LINE = re.compile(r"<(?P<pri>\d{1,3})>1 (?P<ts>\S+) (?P<host>\S+) (?P<app>\S+) (?P<proc>\S+) (?P<msgid>\S+) (?P<sd>-|\[.*?\]) ?(?P<msg>.*)")
SEV = ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug"]
lines = [
 '<86>1 2026-10-11T22:14:03.120Z rly-01 sshd 812 AUTH [meta src="10.40.3.7" user="b.lind"] Accepted publickey',
 '<84>1 2026-10-11T22:15:40.004Z rly-01 sshd 813 AUTH [meta src="192.0.2.44" user="root"] Failed password',
 '<84>1 2026-10-11T22:15:41.917Z rly-01 sshd 813 AUTH [meta src="192.0.2.44" user="root"] Failed password',
 '<134>1 2026-10-11T22:16:00.000Z fw-hub filter - FLOW [flow src="10.40.3.7" dst="10.20.0.11" dport="502" act="allow"]',
 '<131>1 2026-10-11T23:02:11+01:00 hist-01 histsvc 4410 DBERR - write failed: disk quota',
 'Oct 11 22:17:00 rly-01 relay: legacy BSD-format line',
 '<13>1 - kiosk-depot app - - - no timestamp supplied',
]
SDPARAM = re.compile(r'(\w+)="((?:[^"\\]|\\.)*)"')
out, bad = [], 0
for raw in lines:
    m = LINE.fullmatch(raw)
    if not m:
        bad += 1; print("UNPARSED:", raw[:40]); continue
    pri = int(m["pri"])
    rec = {"ts": None if m["ts"] == "-" else m["ts"], "host": m["host"], "app": m["app"],
           "facility": pri // 8, "severity": SEV[pri % 8], "msgid": m["msgid"], "msg": m["msg"]}
    rec.update(dict(SDPARAM.findall(m["sd"])))
    if rec["ts"]:  # normalize every timestamp to UTC so sources can be ordered together
        rec["ts_utc"] = datetime.fromisoformat(rec["ts"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    out.append(rec)
for r in sorted(out, key=lambda r: r.get("ts_utc") or ""):
    print(r.get("ts_utc"), r["host"], r["severity"], r.get("src", "-"), r["msg"] or r["msgid"])
print(json.dumps(out[1], sort_keys=True))
print(f"parsed {len(out)}, unparsed {bad}, missing timestamp {sum(r['ts'] is None for r in out)}")
```

Saída esperada (Python 3.13.5):

```text
UNPARSED: Oct 11 22:17:00 rly-01 relay: legacy BSD
None kiosk-depot notice - no timestamp supplied
2026-10-11T22:02:11.000Z hist-01 err - write failed: disk quota
2026-10-11T22:14:03.120Z rly-01 info 10.40.3.7 Accepted publickey
2026-10-11T22:15:40.004Z rly-01 warning 192.0.2.44 Failed password
2026-10-11T22:15:41.917Z rly-01 warning 192.0.2.44 Failed password
2026-10-11T22:16:00.000Z fw-hub info 10.40.3.7 FLOW
{"app": "sshd", "facility": 10, "host": "rly-01", "msg": "Failed password", "msgid": "AUTH", "severity": "warning", "src": "192.0.2.44", "ts": "2026-10-11T22:15:40.004Z", "ts_utc": "2026-10-11T22:15:40.004Z", "user": "root"}
parsed 6, unparsed 1, missing timestamp 1
```

Confira duas coisas na saída. Primeiro, a contagem de não interpretadas é 1, a linha em formato BSD da aplicação do relay, que é uma falha de configuração num componente do LANTERN, e não ruído. Segundo, a linha `+01:00` do historiador, convertida para UTC, fica em 22:02:11, antes do login de administrador das 22:14 e dos logins de root malsucedidos das 22:15, e não depois deles. Ordenado assim, o fluxo Modbus corporativo-para-PS-04 das 22:16 vem depois de um login de administrador a partir da mesma estação de trabalho, que é a sequência que a Regra B vai sinalizar mais tarde.

### 17.8 Erros comuns e limites

- Registrar tudo em nível de depuração, enchendo os discos (Capítulo 1) e escondendo os eventos que importam.
- Logs mantidos apenas no host que os produziu.
- Carimbos de tempo sem fuso horário; misturar hora local e UTC numa mesma análise.
- Parsers que descartam linhas não interpretáveis sem contá-las.
- Presumir que o encaminhamento de logs ainda funciona porque funcionava no mês passado.
- Construir uma ferramenta caseira onde existe uma mantida, ou criptografia caseira em qualquer caso.

O parser do laboratório é uma simplificação didática da RFC 5424: ele não trata todas as sequências de escape nem múltiplos elementos de dados estruturados. Ele relata o que não consegue interpretar, que é a propriedade que mais importa.

### Exercícios — capítulo 17

**EX049 — Corrija o formato do relay.** *Objetivo:* tratar uma fonte fora do padrão. *Entradas:* a linha não interpretada do Laboratório 17. *Restrições:* duas opções. *Etapas:* (1) descreva corrigir a fonte (mudança de configuração no relay); (2) descreva acrescentar um segundo parser para o formato BSD; (3) diga o que você faria primeiro e por quê, e o que o parser BSD não consegue recuperar. *Evidência esperada:* meia página. *Rubrica:* 3 = corrigir na fonte primeiro (é um componente nosso, sob controle de mudanças), parser BSD como alternativa para dispositivos de terceiros; as linhas BSD não têm ano nem fuso, então o parser precisa presumi-los e marcar os registros como de qualidade inferior; 2 = uma opção; 1 = "ignorar"; 0 = nada.

**EX050 — Ordem dos eventos.** *Objetivo:* ver o efeito dos fusos horários. *Entradas:* a saída do Laboratório 17. *Restrições:* nenhuma. *Etapas:* (1) liste os eventos na ordem dos seus carimbos de tempo *escritos*, ignorando os deslocamentos; (2) liste-os na ordem em UTC; (3) explique como um investigador usando a primeira ordem leria mal o evento do historiador. *Evidência esperada:* duas listas e explicação. *Rubrica:* 3 = o evento do historiador aparece por último na ordem escrita (23:02), mas primeiro em UTC (22:02); o investigador poderia ligar erroneamente o erro de cota de disco aos logins malsucedidos; 2 = listas certas, explicação rasa; 1 = uma lista; 0 = nada.

**EX051 — Conte o que você descarta.** *Objetivo:* acrescentar uma autoverificação à ferramenta. *Entradas:* Laboratório 17. *Restrições:* apenas a biblioteca padrão. *Etapas:* (1) acrescente uma verificação de que o número de linhas de entrada é igual a interpretadas mais não interpretadas, saindo com erro caso contrário; (2) acrescente uma contagem por host das linhas não interpretadas; (3) explique por que um sistema de monitoramento deveria alertar quando a contagem de não interpretadas de um host sobe. *Evidência esperada:* código, saída, explicação. *Rubrica:* 3 = invariante aplicado, contagens por host impressas (rly-01: 1), explicação de que uma mudança de formato numa fonte cega as regras em silêncio; 2 = parcial; 1 = não executado; 0 = nada.

### Síntese do capítulo

Registre o que você vai precisar responder, encaminhe para fora do host e confira se o encaminhamento continua. Sincronize os relógios, registre o tempo com deslocamentos explícitos e analise em UTC. Normalize as fontes numa estrutura única, conte tudo o que você não consegue interpretar e construa pequenas ferramentas com testes e invariantes, para que a sua saída mereça confiança; use ferramentas estabelecidas para os trabalhos gerais e nunca invente criptografia.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 30

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Infraestrutura crítica e segurança setorial: controles

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- selecionar controles para um cenário mapeando a causa e o caminho para as funções de prevenir, detectar e recuperar;
- implementar um controle de modo que ele seja **de alguém, documentado, testável e monitorado**;
- usar um catálogo de controles como o NIST SP 800-53 para conferir a completude sem copiá-lo por inteiro;
- gerenciar um ciclo de vida de chaves como exemplo de um controle que é um processo, e não uma configuração.

O Capítulo 5 apresentou os cartões de controle; o Capítulo 13 produziu cenários. Este capítulo os liga: de quais controles o LANTERN precisa, como implementar cada um para que continue eficaz e como mostrar que ele é eficaz.

### 18.1 Do cenário ao conjunto de controles

Para cada cenário principal, percorra o seu caminho passo a passo e pergunte em cada passo: o que poderia impedir este passo, o que o detectaria e o que recuperaria dele? Para o R2 (uma credencial de fornecedor roubada usada para mudar o setpoint de dosagem da PS-07, Capítulo 13), os passos são: credencial roubada → usada para fazer login → alcança o sistema de controle → muda o setpoint → a qualidade da água muda. Os controles se ligam a cada passo: MFA resistente a phishing e habilitação limitada no tempo (impedir o uso); registro das sessões e alerta para logins do fornecedor fora de uma janela aprovada (detectar); limites de setpoint projetados no CLP (impedir o dano); alerta de telemetria do LANTERN para cloro fora da sua faixa (detectar o efeito); procedimento de dosagem manual e amostragem da qualidade da água (recuperar). A defesa em profundidade (Capítulo 8) é o resultado de fazer esse percurso com honestidade.

### 18.2 Os catálogos como listas de verificação de completude

Os catálogos de controles — o NIST SP 800-53 Rev. 5 é o mais abrangente ([NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) — descrevem os controles por família: controle de acesso, auditoria e responsabilização, gestão de configuração, planejamento de contingência, resposta a incidentes, proteção de sistemas e comunicações, e outras. Use um catálogo depois do percurso do cenário para perguntar "esquecemos alguma família?", e não como uma lista a implementar por inteiro. Na TO, confira os controles do catálogo contra as restrições operacionais descritas no NIST SP 800-82, que fornece orientação específica para TO e um overlay para o SP 800-53 ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

### 18.3 Qualidades da implementação

Um controle que existe no primeiro dia e está ineficaz no nonagésimo é comum. Implemente cada controle com cinco qualidades:

1. **De alguém** — um papel que o mantém e responde por ele.
2. **Documentado** — um cartão de controle (Capítulo 5) dizendo o que ele faz, onde e como falha.
3. **Configurado como código** onde possível — para que o seu estado desejado esteja sob controle de versões e a deriva seja detectável (Capítulo 22).
4. **Testável** — uma forma segura de mostrar que funciona, executada num calendário (Capítulo 23).
5. **Monitorado** — um sinal quando ele deixa de funcionar: um heartbeat, uma contagem, uma verificação de saúde.

### 18.4 Um controle que é um processo: o ciclo de vida das chaves

As chaves HMAC do LANTERN (Capítulo 15) mostram por que alguns controles são processos. Cada chave de estação precisa ser **gerada** com uma fonte aleatória criptograficamente segura; **distribuída** ao gateway da estação e ao relay por uma rota protegida; **guardada** onde apenas o serviço pretendido consegue lê-la; **rotacionada** num calendário e quando saem pessoas com acesso a ela; **revogada** quando uma estação é desativada ou uma chave pode ter sido exposta; e **registrada** — qual versão da chave está ativa onde, sem registrar a própria chave. Uma chave que nunca foi rotacionada é uma chave cuja exposição você não detectaria. A rotação precisa ser ensaiada: se as estações e o relay discordarem sobre a chave ativa, toda mensagem falha na verificação do MAC e a estação fica em silêncio.

### 18.5 Evidências de que um controle funciona

As evidências diferem conforme o tipo de controle. Para um controle de **configuração** (SSH vinculado à interface de gerenciamento), a evidência é o resultado da verificação de deriva e uma tentativa de conexão a partir de um endereço permitido e de um não permitido num teste. Para um controle **detectivo**, a evidência é um evento de teste que produziu um alerta num tempo medido. Para um controle de **processo** (revisão de acessos, rotação de chaves), a evidência é o registro datado da última execução e das suas constatações. Para um controle de **recuperação**, a evidência é uma restauração cronometrada. "Configurado" não é evidência de que funciona.

### 18.6 Exemplo resolvido: cartões de controle para o R2 (sintético)

| Controle | Função | Responsável | Evidência de que funciona | Monitorado por |
|---|---|---|---|---|
| Conta do fornecedor limitada no tempo, com MFA | Prevenir | FSTS Security | Log de habilitação; expiração testada mensalmente | Alerta para login do fornecedor fora da janela |
| Registro das sessões do fornecedor | Detectar | FSTS Security | Amostra de sessão revisada semanalmente | Alerta se o serviço de gravação parar |
| Limites do setpoint de dosagem no CLP | Prevenir o dano | Engenharia da Água | Registro de teste de engenharia; valor relido na visita ao local | Comparação com a linha de base de setpoints aprovada |
| Alerta de telemetria para cloro fora da faixa | Detectar o efeito | Monitoramento da FSTS | Leitura de teste injetada gerou alerta em 2 min | Heartbeat da regra (Capítulo 19) |
| Procedimento de dosagem manual e amostragem | Recuperar | Operação de Água | Registro de exercício nos últimos 12 meses | Calendário de exercícios |

### 18.7 Atividade prática: runbook de rotação de chave

Escreva um runbook de rotação para a chave de uma estação: preparação (nova chave gerada e guardada, relay configurado para aceitar a antiga *e* a nova durante uma sobreposição curta), troca no gateway da estação, verificação (mensagens aceitas com a nova versão da chave; falhas de MAC contadas), remoção da chave antiga e rollback. Declare a duração da sobreposição e o porquê.

Para a PS-07, cuja chave do gateway ficava num cartão removível num gabinete destrancado, a rotação deixou de ser manutenção de rotina: é a resposta a uma constatação física. Uma sobreposição de algumas horas, longa o bastante para confirmar mensagens aceitas sob a nova versão da chave, mantém a estação reportando durante a troca.

### 18.8 Erros comuns e limites

- Selecionar controles de um catálogo sem percorrer um cenário, produzindo muitos controles e lacunas entre eles.
- Controles sem responsável, ou de responsabilidade de uma pessoa em vez de um papel.
- Tratar "configurado" como "eficaz".
- Rotação de chaves nunca ensaiada, e por isso evitada.
- Remover um controle compensatório quando a correção é agendada, e não quando é verificada.

Os cartões do R2 evitam esses erros: cada controle tem um papel responsável e uma evidência, e o teste do alerta de cloro gerou um alerta em 2 minutos.

A rotação de chaves da PS-07 foi evitada durante anos pelo quarto motivo.

### Exercícios — capítulo 18

**EX052 — Percorra um cenário.** *Objetivo:* construir um conjunto de controles a partir de um caminho. *Entradas:* o R3 do Capítulo 13 (o disco do relay enche; telemetria descartada). *Restrições:* pelo menos um controle por passo e por função. *Etapas:* (1) escreva o caminho em passos; (2) ligue a ele controles de prevenir, detectar e recuperar; (3) nomeie a evidência de cada um. *Evidência esperada:* tabela. *Rubrica:* 3 = passos como crescimento → limiar → falha de gravação → mensagens descartadas, com controles como aplicação da retenção, previsão de capacidade e alarme com prazo de reposição (Capítulo 1), alarme de disco e alerta de contagem de rejeições/descartes, buffer nas estações e envio do acúmulo; evidências especificadas; 2 = falta uma função; 1 = um único controle; 0 = nada.

**EX053 — Conferência pelo catálogo.** *Objetivo:* usar um catálogo para conferir a completude. *Entradas:* os cartões de controle do R2 no Capítulo 18 ("Exemplo resolvido: cartões de controle para o R2") e a lista de famílias de controles do SP 800-53 Rev. 5. *Restrições:* cite as famílias pelo identificador. *Etapas:* (1) mapeie cada cartão para uma família; (2) nomeie uma família relevante para o R2 que não tem cartão; (3) proponha um cartão para ela. *Evidência esperada:* tabela com citação. *Rubrica:* 3 = mapeamentos sensatos (por exemplo, AC, AU, CM/SI, IR ou CP) e uma família ausente crível, como segurança de pessoal para a equipe do fornecedor, gestão de riscos da cadeia de suprimentos (SR) para a própria segurança do fornecedor, ou resposta a incidentes (IR) para um incidente de dosagem, com um cartão concreto; 2 = mapeamento certo, família ausente fraca; 1 = sem citação; 0 = nada.

**EX054 — Duração da sobreposição.** *Objetivo:* raciocinar sobre a rotação de chaves. *Entradas:* as estações armazenam em buffer até 24 horas; as mensagens do acúmulo são seladas com a chave ativa no momento em que foram criadas. *Restrições:* o relay deve aceitar o menor número possível de chaves pelo menor tempo possível. *Etapas:* (1) diga por quanto tempo o relay precisa continuar aceitando a chave antiga depois da troca; (2) explique como o relay sabe qual chave tentar. *Evidência esperada:* parágrafo. *Rubrica:* 3 = chave antiga aceita por pelo menos o período de buffer de 24 h (mais uma margem), porque as mensagens do acúmulo carregam MACs da chave antiga; as mensagens carregam um identificador de versão da chave dentro do corpo autenticado ou junto dele, para que o relay selecione a chave em vez de tentar todas; chave antiga removida depois, e a remoção verificada; 2 = sobreposição certa, seleção vaga; 1 = sem sobreposição; 0 = nada.

### Síntese do capítulo

Selecione os controles percorrendo o caminho de cada cenário e ligando controles de prevenir, detectar e recuperar aos seus passos; use os catálogos para conferir a completude. Implemente todo controle com responsável, documentado, configurado como código onde possível, testável e monitorado. Alguns controles são processos — o ciclo de vida das chaves é o exemplo mais claro — e precisam ser ensaiados. "Configurado" nunca é o mesmo que "funciona".

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 30

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Infraestrutura crítica e segurança setorial: monitoramento

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- escrever regras de detecção a partir de cenários e da arquitetura declarada;
- detectar a **ausência** — heartbeats que faltam, fontes silenciosas — assim como a presença;
- ajustar as regras para alertar uma vez por **episódio**, e não por evento, sem perder informação;
- monitorar o monitoramento: saber quando uma regra, uma fonte ou um encaminhador parou de funcionar.

O Capítulo 17 produziu logs normalizados. Este capítulo os transforma em alertas sobre os quais uma pessoa de plantão consegue agir. O objetivo não são muitos alertas; são os poucos certos, cada um apontando para um cenário e uma primeira ação.

### 19.1 De onde vêm as regras

Três fontes produzem as regras do LANTERN. **Cenários** (Capítulo 13): cada passo de um caminho que deixa rastro é uma regra candidata — login do fornecedor fora de uma janela aprovada, cloro fora da sua faixa. **Arquitetura** (Capítulos 2 e 8): qualquer fluxo que viole um conduíte declarado — corporativo para estação numa porta industrial — é uma regra que não precisa de inteligência de ameaças, porque é definida pelo seu próprio projeto. **Comportamentos conhecidos**: logins malsucedidos repetidos a partir de uma mesma origem valem ser conhecidos. A matriz ATT&CK for ICS da MITRE cataloga comportamentos de adversários observados contra sistemas industriais e ajuda a conferir se as regras cobrem as técnicas mais relevantes para os seus cenários ([MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 19.2 A ausência é um sinal

Nos serviços críticos, muitos dos alertas mais importantes são sobre coisas que *param* de acontecer: uma estação que para de reportar, um relay que para de encaminhar, uma fonte de logs que fica em silêncio, um backup que não roda. As regras de ausência precisam de um **ritmo esperado** (um heartbeat a cada cinco minutos) e de uma **tolerância** (alertar depois de 15 minutos de silêncio). Elas pegam interrupções, dispositivos com defeito, cabos cortados, configurações erradas — e atacantes que desabilitam os logs.

A Regra C pegou a PS-09 depois de 40 minutos de silêncio; a sua tolerância de 15 minutos é a escolha de projeto.

### 19.3 Eventos, episódios e qualidade dos alertas

Uma regra que dispara para cada evento correspondente inunda o tecnólogo de plantão: 14 logins malsucedidos viram 14 alertas. Regras melhores alertam uma vez por **episódio** — o primeiro evento numa janela, com uma contagem dos demais — e anexam contexto: zona de origem, criticidade do ativo, eventos recentes relacionados. Acompanhe a **taxa de alarmes falsos** e o **tempo de resposta** de cada regra. Uma regra que disparou cem vezes sem um verdadeiro positivo está treinando as pessoas a ignorá-la; ajuste-a, mude o seu limiar ou encaminhe-a para um relatório diário em vez de um acionamento.

### 19.4 Encaminhamento e primeira ação

Todo alerta precisa de um responsável e de uma **primeira ação** escrita na regra: "Modbus corporativo→estação: conferir se há uma sessão de engenharia aprovada em andamento (calendário de mudanças); se não houver, ligar para a sala de controle da Água e depois preservar os registros de fluxo." Os alertas que afetam o processo físico vão para a operação de Água, além da FSTS. Escreva as primeiras ações antes de ligar uma regra.

A primeira ação da Regra B cumpriu o seu papel na noite do exemplo resolvido: primeiro o calendário de mudanças, depois a sala de controle da Água.

A primeira ação da Regra C, depois do estudo do Capítulo 24, é "ligar para a sala de controle da Água, depois conferir a situação da operadora".

### 19.5 Monitorar o monitoramento

Regras, fontes e encaminhadores falham em silêncio. Monitore: a taxa de eventos de cada fonte (uma regra de ausência para os logs); a contagem de não interpretadas do normalizador (Capítulo 17); o horário da última avaliação de cada regra; e **eventos de teste** periódicos que deveriam produzir alertas conhecidos (Capítulo 23). A orientação do NIST sobre monitoramento contínuo de segurança da informação enfatiza a consciência contínua de se os controles continuam eficazes ([NIST SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

As falhas da Regra B no Laboratório 23, fluxos de um switch de estação que nunca foram exportados para o SIEM, mostram o custo de não monitorar as fontes: a regra estava certa, a sua entrada é que faltava.

### 19.6 Exemplo resolvido: uma noite, três regras (sintético)

O Laboratório 19 aplica três regras a uma noite de eventos e heartbeats. A Regra A (≥10 logins malsucedidos a partir de uma origem em 5 minutos) dispara uma vez para 192.0.2.44. A Regra B (Modbus corporativo→estação) dispara duas vezes para a mesma estação de trabalho, às 22:16 e às 22:31 — dois acionamentos para um episódio; ela deveria ser ajustada para alertar uma vez e atualizar uma contagem. A Regra C (heartbeat ausente por > 15 minutos) dispara às 23:00 para a PS-09, que ficou em silêncio por 40 minutos. Note o que **não** dispara: um único login malsucedido de `e.strand` a partir de um endereço interno, abaixo do limiar da Regra A — corretamente, já que uma senha digitada errado não é um episódio.

Junto com a linha do tempo do Capítulo 17, a Regra B é o alerta que mais importa: a estação de trabalho que fez login como administrador às 22:14 depois conversou em Modbus com um CLP. Primeira ação: conferir o calendário de mudanças; se nenhuma sessão de engenharia foi aprovada, ligar para a sala de controle da Água.

### 19.7 Atividade prática: regras sobre eventos

**Laboratório 19** (salve como `lab19.py`, execute com `python3 lab19.py`):

```python
# Lab 19 - three monitoring rules over normalized events, including "absence" (offline, standard library only)
# Synthetic events for one night at Fallowmere (times are minutes after 22:00 UTC).
events = [  # minute, host, type, fields
 (14, "rly-01", "auth_ok", {"src": "10.40.3.7", "user": "b.lind"}),
 *[(15 + i // 4, "rly-01", "auth_fail", {"src": "192.0.2.44", "user": "root"}) for i in range(14)],
 (16, "fw-hub", "flow", {"src": "10.40.3.7", "dst": "10.20.0.11", "dport": 502}),
 (31, "fw-hub", "flow", {"src": "10.40.3.7", "dst": "10.20.0.11", "dport": 502}),
 (44, "rly-01", "auth_fail", {"src": "10.40.9.9", "user": "e.strand"}),
]
heartbeats = {"PS-04": list(range(0, 120, 5)), "PS-07": list(range(0, 120, 5)),
              "PS-09": [m for m in range(0, 120, 5) if not 50 <= m < 85]}
alerts = []
# Rule A: >=10 failed logins from one source within 5 minutes
fails = [(m, f["src"]) for m, h, t, f in events if t == "auth_fail"]
for src in {s for _, s in fails}:
    times = sorted(m for m, s in fails if s == src)
    for i in range(len(times)):
        if sum(1 for t in times if times[i] <= t < times[i] + 5) >= 10:
            alerts.append((times[i], "A brute-force", src)); break
# Rule B: any flow from corp to a station on an industrial port (not a declared conduit)
for m, h, t, f in events:
    if t == "flow" and f["src"].startswith("10.40.") and f["dst"].startswith("10.20.") and f["dport"] == 502:
        alerts.append((m, "B corp->station Modbus", f"{f['src']}->{f['dst']}"))
# Rule C: heartbeat missing for > 15 minutes (silence is a signal)
for st, beats in heartbeats.items():
    for a, b in zip(beats, beats[1:]):
        if b - a > 15:
            alerts.append((a + 15, "C station silent", f"{st} gap {b - a} min"))
for m, rule, detail in sorted(alerts):
    print(f"22:{m:02d}+  {rule:<24} {detail}" if m < 60 else f"23:{m-60:02d}+  {rule:<24} {detail}")
print("alerts:", len(alerts), "| rule B fired per event, not per episode:", sum(1 for a in alerts if a[1].startswith("B")))
```

Saída esperada (Python 3.13.5):

```text
22:15+  A brute-force            192.0.2.44
22:16+  B corp->station Modbus   10.40.3.7->10.20.0.11
22:31+  B corp->station Modbus   10.40.3.7->10.20.0.11
23:00+  C station silent         PS-09 gap 40 min
alerts: 4 | rule B fired per event, not per episode: 2
```

Conte os alertas por episódio, e não por linha. A Regra A dispara uma vez para 192.0.2.44, a Regra B duas vezes para uma estação de trabalho, às 22:16 e às 22:31, e a Regra C uma vez para a PS-09 às 23:00. São quatro alertas para três episódios; ajustar a Regra B para alertar uma vez e atualizar uma contagem os reduz a três. Depois confirme o não evento: o único login malsucedido de `e.strand` a partir de um endereço interno fica abaixo do limiar da Regra A, como pretendido.

### 19.8 Erros comuns e limites

- Regras sem cenário, responsável ou primeira ação.
- Apenas regras de presença; nada nota o silêncio.
- Um alerta por evento, inundando os respondedores.
- Limiares nunca revistos.
- Presumir que uma regra funciona porque foi implantada; ela precisa ser testada (Capítulo 23).
- Enviar alertas relevantes para o processo apenas à TI.

As regras detectam o que foi previsto. O comportamento imprevisto precisa de pessoas que olhem os dados — caça a ameaças, revisões — e de regras de ausência, que pegam efeitos sem conhecer as causas.

Os dois acionamentos da Regra B para um episódio, na noite do exemplo resolvido, são o terceiro erro.

### Exercícios — capítulo 19

**EX055 — Regra por episódio.** *Objetivo:* reduzir o ruído dos alertas sem perder informação. *Entradas:* Laboratório 19. *Restrições:* apenas a biblioteca padrão. *Etapas:* (1) mude a Regra B para que ela gere um alerta por par origem–destino a cada 60 minutos, registrando a contagem de eventos correspondentes; (2) execute e mostre a saída; (3) explique qual informação é preservada. *Evidência esperada:* código, saída, explicação. *Rubrica:* 3 = um alerta da Regra B com contagem 2 e horários do primeiro e do último; explicação de que as contagens e os horários são preservados para a investigação enquanto o acionamento dispara uma vez; 2 = funciona, falta a contagem; 1 = não executado; 0 = nada.

**EX056 — Primeiras ações.** *Objetivo:* escrever alertas acionáveis. *Entradas:* Regras A, B e C. *Restrições:* no máximo três passos cada; precisa incluir para quem ligar. *Etapas:* escreva a primeira ação de cada uma. *Evidência esperada:* três procedimentos curtos. *Rubrica:* 3 = A: confirmar a exposição do SSH, conferir se houve algum sucesso a partir daquela origem, bloquear na borda sob mudança padrão; B: conferir o calendário de mudanças, ligar para a sala de controle da Água se não aprovado, preservar os fluxos; C: ligar para a sala de controle da Água para confirmar o estado da estação, conferir a situação da operadora, conferir nos logs do relay se há falhas de MAC; 2 = uma fraca; 1 = genérico; 0 = nada.

**EX057 — Monitore o monitor.** *Objetivo:* projetar o automonitoramento. *Entradas:* o pipeline de monitoramento do LANTERN: fontes → encaminhador → normalizador → regras → acionamento. *Restrições:* uma verificação por etapa. *Etapas:* liste a verificação, o seu limiar e quem é alertado. *Evidência esperada:* tabela. *Rubrica:* 3 = ausência da taxa de eventos da fonte, fila/acúmulo do encaminhador, taxa de não interpretadas do normalizador, horário da última execução da regra, teste de acionamento (acionamento sintético agendado e confirmado); limiares e destinatários sensatos; 2 = quatro etapas; 1 = genérico; 0 = nada.

### Síntese do capítulo

Derive as regras de cenários, da sua própria arquitetura e de comportamentos conhecidos; dê a cada uma um responsável e uma primeira ação. Detecte a ausência, assim como a presença. Alerte por episódio, com contagens e contexto, acompanhe os alarmes falsos e os tempos de resposta, e encaminhe os alertas relevantes para o processo à operação. Monitore o monitoramento, porque cada etapa dele pode falhar em silêncio.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 30

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Infraestrutura crítica e segurança setorial: resolução de problemas

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- seguir um método disciplinado de resolução de problemas que funcione quer a falha se revele técnica, humana ou maliciosa;
- **preservar as evidências antes de mudar as coisas**, e saber quando uma falha precisa virar um incidente;
- distinguir as causas comuns de "dados ausentes" — perda, atraso, erro de relógio, filtragem — usando os próprios dados;
- escrever um registro de problema curto que a próxima pessoa consiga usar.

A maior parte da vida profissional de um implementador é gasta com falhas. Nos serviços críticos, algumas falhas são ataques e alguns ataques parecem falhas; o método precisa funcionar para os dois sem atrasar os reparos comuns.

### 20.1 Um método

1. **Defina o sintoma com precisão**: o que está errado, desde quando, para quem, medido como. "PS-07 e PS-09 mostram lacunas no painel desde cerca de 22:50" — e não "a telemetria está quebrada".
2. **Confira primeiro o impacto e a safety**: alguém precisa agir sobre o processo físico agora? Diga à operação de Água no que ela pode e no que não pode confiar.
3. **Preserve antes de mudar**: copie os logs, as configurações e as saídas relevantes, com os horários, antes de reiniciar ou reconfigurar qualquer coisa (veja "Preserve antes de mudar", abaixo).
4. **Liste hipóteses**, incluindo pelo menos uma explicação não maliciosa e uma maliciosa, e qual evidência as distinguiria.
5. **Teste primeiro a hipótese discriminante mais barata**, usando leituras antes de gravações.
6. **Mude uma coisa de cada vez**, sob o tipo de mudança apropriado (Capítulo 14), registrando cada mudança.
7. **Verifique** a correção contra o sintoma original, e observe se ele volta.
8. **Registre** a causa, as evidências, as ações e os itens em aberto.

### 20.2 Preserve antes de mudar

Reiniciar um serviço limpa a sua memória, rotaciona os logs e pode destruir a única evidência do que aconteceu. As recomendações do NIST de resposta a incidentes enfatizam preservar as evidências e coordenar a resposta com a gestão de riscos da organização ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). Para um implementador, a preservação costuma ser rápida: copiar os logs e a configuração do serviço, exportar os registros de fluxo e de alertas relevantes, anotar os processos em execução e as conexões de rede, calcular hashes do que foi copiado e anotar o horário. Se a falha afeta o processo físico, restaurar o serviço pode legitimamente vir primeiro — mas diga isso e registre o que se perdeu.

### 20.3 Quando uma falha vira um incidente

Escale para o processo de incidentes quando qualquer uma destas condições for verdadeira: evidência de acesso ou mudança não autorizados (uma diferença de configuração não aprovada, a conta de alguém que saiu sendo usada — Capítulo 7); um controle de segurança falhou de um modo que poderia ser explorado; dados podem ter ido para onde não deveriam (Capítulo 12); ou a causa não pode ser encontrada e uma causa maliciosa é plausível. Escalar não é uma acusação. Isso traz pessoas com autoridade e deveres diferentes, incluindo as obrigações de notificação do operador (Capítulo 10).

O login de `c.mendes` em 14 de setembro é o gatilho mais claro de Fallowmere.

### 20.4 Dados ausentes: quatro causas comuns

A telemetria ausente é o sintoma mais comum do LANTERN. Os próprios dados costumam discriminar entre as causas:

- **Perdidos** — os números de sequência têm lacunas (Capítulo 15): as mensagens nunca foram recebidas.
- **Atrasados** — sequência completa, mas o horário de recebimento muito atrás do horário da estação, muitas vezes depois de um problema na operadora.
- **Erro de relógio** — sequência completa e chegada pontual, mas os carimbos de tempo da estação deslocados por um valor constante; os dados são arquivados na janela de tempo errada, então um painel que consulta pelo horário da estação mostra uma lacuna.
- **Filtrados** — mensagens recebidas, mas rejeitadas ou quarentenadas (contagens de rejeição subindo no log do relay).

### 20.5 Exemplo resolvido: duas lacunas, duas causas (sintético)

Os operadores relatam lacunas no painel para a PS-07 e a PS-09. O Laboratório 20 examina doze números de sequência de cada estação. Faltam na PS-07 os números de sequência 5–8, com chegada pontual dos demais: os dados se perderam. A PS-09 tem todos os números de sequência e chega pontualmente pelo relógio do relay, mas os carimbos de tempo da estação estão cerca de 422 segundos atrasados: o seu relógio está errado, e a janela do painel perde todos os seus pontos. Os dois sintomas pareciam idênticos no painel; as causas e as correções são completamente diferentes.

Para a PS-09, a próxima pergunta é *por que* o relógio está errado: a estação perdeu o seu caminho NTP até o relay (uma mudança de conduíte? Capítulo 2), ou alguém mudou a configuração de hora da estação? A primeira é uma falha; a segunda pode ser um evento de segurança. Um deslocamento constante de cerca de sete minutos em todas as mensagens é incomum para uma deriva — a deriva é gradual. Preserve os logs de NTP do relay e a configuração do conduíte antes que alguém acerte o relógio.

Para a PS-07, a lacuna de quatro mensagens consecutivas poderia ser uma queda da operadora, uma reinicialização da estação ou rejeições do relay. Confira o log de rejeições do relay naqueles horários antes de ligar para a BayTel: se houve falhas de MAC na PS-07 naquele momento, a causa está no tratamento das chaves (Capítulo 18), e não na operadora.

### 20.6 Atividade prática: discrimine as causas

**Laboratório 20** (salve como `lab20.py`, execute com `python3 lab20.py`):

```python
# Lab 20 - troubleshooting "missing telemetry": sequence gaps versus clock skew (offline, standard library only)
# Synthetic historian extract: station, sequence number, station timestamp (s), relay receive time (s).
rows = {
 "PS-04": [(s, 1000 + 10*s, 1000 + 10*s + 1) for s in range(1, 13)],
 "PS-07": [(s, 1000 + 10*s, 1000 + 10*s + 1) for s in range(1, 13) if s not in (5, 6, 7, 8)],
 "PS-09": [(s, 1000 + 10*s - 420, 1000 + 10*s + 2) for s in range(1, 13)],
}
for st, rs in rows.items():
    seqs = [r[0] for r in rs]
    missing = sorted(set(range(seqs[0], seqs[-1] + 1)) - set(seqs))
    offsets = [recv - ts for _, ts, recv in rs]
    avg = sum(offsets) / len(offsets)
    dx = "data lost in transit or at source" if missing else ("clock skew: station clock behind by ~%d s; data present but filed in the wrong window" % round(avg) if abs(avg) > 60 else "healthy")
    print(f"{st}: received {len(rs)}/{seqs[-1]-seqs[0]+1}, missing seq {missing or '-'}, mean recv-ts offset {avg:+.0f} s -> {dx}")
# A dashboard that queries by station timestamp for window [1050, 1130) would show:
for st, rs in rows.items():
    print(st, "points in dashboard window:", sum(1 for _, ts, _ in rs if 1050 <= ts < 1130))
```

Saída esperada (Python 3.13.5):

```text
PS-04: received 12/12, missing seq -, mean recv-ts offset +1 s -> healthy
PS-07: received 8/12, missing seq [5, 6, 7, 8], mean recv-ts offset +1 s -> data lost in transit or at source
PS-09: received 12/12, missing seq -, mean recv-ts offset +422 s -> clock skew: station clock behind by ~422 s; data present but filed in the wrong window
PS-04 points in dashboard window: 8
PS-07 points in dashboard window: 4
PS-09 points in dashboard window: 0
```

Olhe as colunas das duas estações lado a lado. Os números de sequência da PS-07 saltam de 4 para 9, então quatro mensagens nunca chegaram. Os números de sequência da PS-09 estão completos, mas os seus carimbos de tempo da estação ficam atrás dos horários de chegada do relay em cerca de 422 segundos em todas as mensagens. O primeiro caso é perda; o segundo é tempo. Depois escreva a próxima verificação para cada uma: o log de rejeições do relay e a situação da BayTel para a lacuna da PS-07, e o caminho NTP e a configuração de hora para a PS-09, preservados antes que alguém acerte o relógio.

### 20.7 Erros comuns e limites

- Reiniciar primeiro e investigar depois.
- Uma única hipótese, em geral a mais familiar.
- Várias mudanças de uma vez, de modo que ninguém sabe qual corrigiu — ou qual quebrou outra coisa.
- Tratar toda falha como ataque, ou nenhuma.
- "Corrigir" um relógio ou uma configuração antes de registrar como estava.
- Fechar o ticket sem um registro da causa e das evidências.

Acertar primeiro o relógio da PS-09 teria destruído as evidências para a pergunta dos 422 segundos.

Ligar para a BayTel por causa da lacuna da PS-07 antes de conferir o log de rejeições do relay seria o segundo erro: uma única hipótese, a mais familiar, testada primeiro e possivelmente sozinha.

### Exercícios — capítulo 20

**EX058 — Hipóteses e discriminantes.** *Objetivo:* raciocinar antes de agir. *Entradas:* sintoma: "a contagem de rejeições do relay para a PS-04 subiu de 0 para 300 por hora às 09:00; o painel não mostra dados da PS-04 desde então." *Restrições:* quatro hipóteses, pelo menos uma maliciosa. *Etapas:* para cada uma, dê a evidência que a apoiaria ou a descartaria, e a verificação mais barata. *Evidência esperada:* tabela. *Rubrica:* 3 = por exemplo, chave rotacionada na estação, mas não no relay (falhas de MAC nos motivos de rejeição, calendário de mudanças), salto do relógio da estação (rejeições pela janela), estado de reprodução envenenado (rejeições por reprodução depois de uma sequência alta — Capítulo 29), tráfego forjado (falhas de MAC a partir de um endereço de origem inesperado); as verificações são leituras; 2 = três; 1 = uma; 0 = nada.

**EX059 — Lista de preservação.** *Objetivo:* preservar evidências rapidamente. *Entradas:* o caso do deslocamento do relógio da PS-09. *Restrições:* no máximo dez minutos; nenhuma mudança nos sistemas. *Etapas:* liste o que você copiaria ou registraria, em ordem, e como você mostraria depois que as cópias não foram alteradas. *Evidência esperada:* lista. *Rubrica:* 3 = NTP do relay e logs do relay, configuração do conduíte/firewall e log de mudanças recentes, extrato do historiador, saída de uma análise no estilo do Laboratório 20, horário da coleta, hashes registrados no ticket e cópias guardadas fora do host; 2 = faltam os hashes ou os horários; 1 = "tirar uma captura de tela"; 0 = nada.

**EX060 — Registro do problema.** *Objetivo:* escrever um registro utilizável. *Entradas:* Capítulo 20 ("Exemplo resolvido: duas lacunas, duas causas"), e presuma que a causa da PS-09 foi uma mudança de firewall que bloqueou a udp/123 do relay para a estação dois dias antes. *Restrições:* no máximo 250 palavras; rótulos observado / inferido / feito / em aberto. *Etapas:* escreva o registro. *Evidência esperada:* o registro. *Rubrica:* 3 = sintoma preciso, evidências (deslocamento de ~422 s, sequência completa), causa com a mudança identificada, correção sob controle de mudanças, verificação e itens em aberto (por que a mudança removeu o NTP; por que nenhum alerta disparou para o deslocamento do relógio — acrescentar um); 2 = falta um elemento; 1 = só narrativa; 0 = nada.

### Síntese do capítulo

Resolva problemas com um método: sintoma preciso, safety e impacto primeiro, preservar antes de mudar, várias hipóteses incluindo uma maliciosa, a verificação discriminante mais barata primeiro, uma mudança de cada vez, verificar e registrar. Escale para um incidente quando as evidências sugerirem atividade não autorizada ou exposição. Para dados ausentes, os próprios dados — sequência, chegada, carimbos de tempo, contagens de rejeição — costumam distinguir perda, atraso, erro de relógio e filtragem.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 30

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Infraestrutura crítica e segurança setorial: integração do serviço

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- integrar um serviço técnico com as pessoas e as organizações ao seu redor: operadores, o centro de monitoramento de segurança, fornecedores e planejadores de emergência;
- definir **interfaces** — o que é entregue, em que forma, com que rapidez e a quem —, e não apenas formatos de dados;
- escrever uma matriz de responsabilidades para um serviço compartilhado e testá-la com um cenário;
- ligar o tratamento de incidentes do serviço aos planos de continuidade e de emergência do operador.

A esta altura, o LANTERN é um serviço técnico em funcionamento. Um serviço está integrado quando todos os que dependem dele, ou de quem ele depende, sabem o que esperar e o que fazer. A maioria das falhas nesta etapa não é técnica: um alerta que ninguém assume, um fornecedor que nunca foi avisado de uma mudança, um operador que não sabia que o painel podia estar desatualizado.

### 21.1 As interfaces são acordos

Para cada vizinho, escreva a interface como um acordo:

- **Operação de Água** — o que o LANTERN fornece (telemetria ao historiador em até 60 s, com a idade do valor exibida), o que a Água fornece (solicitações de comissionamento de estações, exportações de engenharia, aprovações relevantes para o processo), como os alertas que afetam o processo chegam à sala de controle e como a Água relata um suposto problema de telemetria.
- **Monitoramento de segurança da FSTS (SOC)** — quais logs e alertas o LANTERN envia, em que formato, com quais primeiras ações; como o SOC escala para o plantão do LANTERN; o que o SOC pode fazer sem perguntar (por exemplo, desabilitar uma conta de fornecedor) e o que não pode (por exemplo, bloquear os conduítes das estações).
- **Fornecedores (Kell, Arlen, BayTel, Halden)** — como são avisados das mudanças que os afetam, como relatam problemas e vulnerabilidades, como funciona o seu acesso (Capítulo 7), com que antecedência avisam das suas próprias mudanças.
- **Planejamento de emergência** — como uma interrupção ou um comprometimento do LANTERN se reflete nos planos de continuidade da Água e do hospital.

### 21.2 Matrizes de responsabilidade

Uma matriz **RACI** registra, para cada atividade, quem é Responsável (executa), quem Aprova/responde (é dono do resultado — exatamente um), quem é Consultado e quem é Informado. Teste-a com um cenário: percorra "relay comprometido às 02:00" e confira se cada passo tem exatamente um papel que responde pelo resultado, se ninguém que precise ser consultado está inalcançável às 02:00, e se as pessoas que precisam agir sobre o processo físico são informadas cedo.

Percorrer "relay comprometido às 02:00" no rascunho de Fallowmere expôs o problema que o exemplo resolvido descreve: ninguém respondia por dizer aos operadores da Água que desconfiassem da telemetria.

### 21.3 Integração dos fornecedores

Os fornecedores fazem parte do serviço. O seu acesso remoto é um caminho para dentro dele; as suas atualizações de software são mudanças nele; as suas interrupções são as suas interrupções. Integrar significa: o acesso deles pelo caminho declarado; os avisos de mudança deles no seu calendário de mudanças; os alertas de segurança deles na sua rotina de vulnerabilidades (Capítulo 16); e cláusulas contratuais que exijam a notificação de incidentes que afetem você. A iniciativa Secure by Design da CISA incentiva os fabricantes a assumir a responsabilidade pelos resultados de segurança dos clientes ([CISA Secure by Design](https://www.cisa.gov/securebydesign)); como cliente, pergunte aos fornecedores como eles atendem a essas expectativas e registre as respostas.

### 21.4 O tratamento de incidentes encontra a continuidade

Um incidente no LANTERN é tratado pelo processo de incidentes da FSTS, mas as suas consequências são geridas pelos arranjos de continuidade e de emergência da Água e do hospital. O ponto de integração é uma lista curta de **gatilhos**: condições sob as quais a FSTS diz à Água "presuma que a telemetria não é confiável — passe a leituras manuais nas estações" ou diz ao hospital "presuma que o gateway clínico está indisponível — use o procedimento da biblioteca de medicamentos em papel". Os gatilhos precisam ser acordados previamente e exercitados (Capítulo 28), porque às 02:00 ninguém deveria estar negociando o que significa "não confiável".

### 21.5 Exemplo resolvido: uma RACI que falhou no teste (sintético)

O rascunho da RACI para "suspeita de comprometimento de um relay" lista: plantão da FSTS — R; líder de segurança da FSTS — A; operação de Água — I; SOC — C; Kell — I. Percorrer o cenário revela três problemas. Primeiro, a decisão de dizer aos operadores da Água que desconfiem da telemetria não tem papel que responda por ela: a segurança da FSTS não consegue julgar o impacto no processo, e a Água é apenas Informada. Correção: o gerente de turno da Água como A pela resposta operacional, o líder de segurança da FSTS como A pela resposta técnica, com um gatilho nomeado para a passagem. Segundo, a Kell é apenas Informada, mas, se o comprometimento veio pelo caminho do fornecedor, a conta da Kell precisa ser desabilitada de imediato e a Kell consultada sobre a sua própria exposição. Terceiro, o SOC é "Consultado", mas, na prática, detecta a maioria dos incidentes; ele deveria ser Responsável pelos primeiros passos de triagem.

### 21.6 Atividade prática: acordos de interface

Escreva um acordo de interface de uma página entre o LANTERN e a operação de Água, cobrindo: o que cada lado fornece, os níveis de serviço (atualidade, exibição da idade do valor), o encaminhamento de alertas, como um suposto problema de telemetria é relatado, os gatilhos para "telemetria não confiável" e a frequência de revisão.

Torne os gatilhos mensuráveis: por exemplo, "telemetria não confiável" é declarada quando as falhas de MAC do relay excedem uma taxa declarada em mais de uma estação, quando duas ou mais estações mostram deslocamentos de relógio como os 422 segundos da PS-09, ou quando a FSTS suspeita do comprometimento de um relay. Declare quem a declara (o gerente de turno da Água, com o aconselhamento da FSTS), como a sala de controle é avisada e que ela é exercitada anualmente.

### 21.7 Erros comuns e limites

- Tratar a integração apenas como formatos de dados e APIs.
- Matrizes RACI com vários papéis que respondem pelo resultado, ou nenhum.
- Fornecedores fora dos processos de mudanças e de vulnerabilidades.
- Planos de continuidade que presumem que o serviço de TI está ou totalmente no ar ou totalmente fora, sem um estado "no ar, mas não confiável".
- Gatilhos definidos, mas nunca exercitados.

O primeiro rascunho da RACI mostra o segundo erro: nenhum papel respondia pela resposta operacional.

A exclusão da Kell dos papéis consultados no rascunho da RACI mostra o terceiro: um fornecedor cuja conta pode ser o caminho de entrada seria apenas informado.

### Exercícios — capítulo 21

**EX061 — Conserte a RACI.** *Objetivo:* corrigir uma matriz de responsabilidades. *Entradas:* o rascunho do Capítulo 21 ("Exemplo resolvido: uma RACI que falhou no teste"). *Restrições:* exatamente um A por atividade; divida atividades se necessário. *Etapas:* escreva a matriz consertada para as atividades: detectar e triar; conter no relay; desabilitar o acesso do fornecedor; decidir a resposta operacional; notificar os reguladores, se exigido; restaurar o serviço. *Evidência esperada:* matriz. *Rubrica:* 3 = um A por linha; SOC R pela triagem; segurança da FSTS A pela contenção técnica; gerente de turno da Água A pela resposta operacional; notificação regulatória com A no papel designado pelo operador, e não na FSTS; Kell C no acesso do fornecedor; 2 = uma linha errada; 1 = continuam vários A; 0 = nada.

**EX062 — Defina um gatilho.** *Objetivo:* tornar preciso o "telemetria não confiável". *Entradas:* os alertas do LANTERN do Capítulo 19 e os desfechos de validação do Capítulo 3. *Restrições:* condições mensuráveis; não pode disparar em falhas comuns de uma única estação. *Etapas:* (1) escreva as condições do gatilho; (2) diga quem o declara e quem o encerra; (3) diga o que a Água faz quando ele é declarado. *Evidência esperada:* meia página. *Rubrica:* 3 = condições como uma mudança não autorizada confirmada num relay, falhas de MAC em várias estações ou falha de integridade do relay; declarado pelo líder de segurança da FSTS com o gerente de turno da Água; a Água passa a leituras manuais e amostragem; a condição de encerramento exige um estado limpo verificado; 2 = condições vagas; 1 = "quando parecer errado"; 0 = nada.

**EX063 — Perguntas ao fornecedor.** *Objetivo:* integrar um fornecedor. *Entradas:* Kell Instruments. *Restrições:* seis perguntas; cada uma ligada a um processo do LANTERN. *Etapas:* escreva as perguntas e o processo que cada uma alimenta. *Evidência esperada:* lista. *Rubrica:* 3 = por exemplo, como a Kell notifica vulnerabilidades (Capítulo 16), como o acesso da sua equipe é controlado e revogado (Capítulo 7), o seu compromisso de notificação de incidentes (este capítulo), como o firmware é assinado (Capítulo 27), as datas de fim de suporte (Capítulo 11), a disponibilidade de SBOM ([CISA SBOM](https://www.cisa.gov/sbom)); 2 = quatro ou cinco; 1 = genérico; 0 = nada.

### Síntese do capítulo

Um serviço está integrado quando todo vizinho — operadores, o SOC, fornecedores, planejadores de emergência — tem uma interface acordada: o que é fornecido, com que rapidez, a quem e o que acontece quando falha. Teste as matrizes de responsabilidade com cenários até que cada atividade tenha um papel que responda por ela. Traga os fornecedores para os processos de mudanças, vulnerabilidades e incidentes. Acorde e exercite os gatilhos que ligam um incidente técnico aos planos de continuidade do operador, incluindo o estado "no ar, mas não confiável".

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue estudando — capítulo 21 de 30

[← Capítulo 20](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Infraestrutura crítica e segurança setorial: automação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- expressar a configuração desejada como código e compará-la automaticamente com o estado real;
- projetar uma automação que **planeja antes de agir**, separa as correções automáticas seguras das mudanças que precisam de aprovação e limita o seu próprio raio de impacto;
- reconhecer quando a própria fonte da verdade pode estar errada, e parar;
- manter a automação dentro do controle de mudanças e produzir evidências a partir dela.

Os Capítulos 6 e 14 descreveram linhas de base e verificações de integridade feitas à mão. Com três relays e um parque crescente, a verificação manual deixa de acontecer. A automação torna confiáveis as verificações de rotina — e torna os erros rápidos e amplos. Este capítulo trata de obter o primeiro sem o segundo.

### 22.1 Configuração como código

Escreva o estado desejado de cada classe de host como dados sob controle de versões: configurações do SSH, endereços de escuta, servidores de hora, encaminhamento de logs, versões de pacotes. Um coletor lê o estado real de cada host (somente leitura), e uma comparação produz a **deriva**: as chaves cujo valor real difere do desejado. O guia do NIST de gestão de configuração descreve o monitoramento das configurações contra linhas de base como uma atividade central ([NIST SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final)); o framework do NIST de desenvolvimento seguro de software aplica disciplinas semelhantes — controle de versões, revisão, pipelines de build protegidos — ao código que o implementa ([NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)).

### 22.2 Planejar, depois agir

Uma boa automação separa o **planejar** do **aplicar**. O plano lista toda mudança pretendida: host, configuração, valor atual, valor desejado e modo. A etapa de aplicação executa um plano aprovado, e não um cálculo novo. Isso dá a uma pessoa a chance de ver o que vai acontecer, dá ao registro de mudança algo específico para aprovar e produz evidências depois.

O plano do Laboratório 22 para o RLY-02 lista duas mudanças, SSH com senha e servidores de hora públicos, com os valores atuais e desejados.

O listener de depuração do RLY-03 aparece no plano como um ticket, e não como uma ação, porque removê-lo poderia destruir a evidência de quem o habilitou.

### 22.3 Correção automática segura versus ticket

Alguma deriva é segura para corrigir automaticamente: configurações de baixo risco, reversíveis e bem compreendidas (desabilitar de novo a autenticação por senha do SSH; restaurar os servidores de hora aprovados; restaurar o encaminhamento de logs). Outra deriva precisa passar pelo controle de mudanças: qualquer coisa que possa mudar o comportamento do serviço (uma versão de pacote), qualquer coisa que possa ser evidência (um listener de depuração inesperado — que pode ser de um atacante ou de um engenheiro, e deve ser preservado antes da remoção, Capítulo 20) e qualquer coisa que afete o processo físico. Escreva a lista de correções automáticas de forma explícita e mantenha-a curta.

### 22.4 Limites do raio de impacto

A automação precisa se proteger contra os seus próprios erros. Limites comuns: aplicar a **um host de cada vez**, verificando cada um antes do próximo; parar na primeira falha; e **parar e escalar se for encontrada deriva demais** — se a maior parte do parque parece ter derivado, a explicação mais provável é que o estado desejado está errado (um commit ruim, um branch errado), e a correção automática espalharia o erro por toda parte. Uma grande interrupção causada por uma atualização defeituosa distribuída a muitos sistemas de uma vez — como o incidente de julho de 2024 que afetou hosts Windows rodando um produto de segurança, descrito pela Microsoft como tendo afetado cerca de 8,5 milhões de dispositivos ([Microsoft, 20 de julho de 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)) — ilustra por que a implantação escalonada e as condições de parada importam para qualquer distribuição automatizada.

### 22.5 Automação é código: trate-a assim

O próprio código da automação e os arquivos de estado desejado têm alto valor: quem consegue mudá-los consegue mudar todos os hosts. Proteja-os com revisão antes do merge, acesso de escrita restrito, commits assinados ou branches protegidos, e logs de cada execução. As credenciais da automação para ler e mudar os hosts são contas privilegiadas (Capítulo 7).

A fusão do NTP no Capítulo 25 é o aviso: um único commit revisado mudou a hora em todos os relays.

Trate a conta que a automação usa para alcançar do RLY-01 ao RLY-03 como a `vendor-kell`: limitada no tempo onde possível, registrada e revisada na revisão trimestral de acessos do Capítulo 7.

### 22.6 Exemplo resolvido: uma execução simulada em três relays (sintético)

O Laboratório 22 compara o estado desejado com três relays. O RLY-01 está conforme. O RLY-02 tem a autenticação por senha do SSH reabilitada e servidores de hora públicos — ambos na lista de correções automáticas. O RLY-03 tem um listener de depuração em todas as interfaces, um pacote do relay mais antigo e nenhum encaminhamento de logs. Dois de três hosts derivaram, mais da metade do parque, então a salvaguarda interrompe a execução. Aqui a interrupção é, num sentido, um alarme falso — a fonte da verdade está bem —, mas a regra está certa em parar: uma pessoa confirma o estado desejado e então aprova a aplicação das três correções automáticas, host por host, enquanto o listener de depuração e a versão do pacote vão para tickets. O listener de depuração no RLY-03 é o mesmo sintoma encontrado pela verificação de integridade no RLY-01 no Capítulo 6: duas vezes é um padrão, e o método de resolução de problemas do Capítulo 20 se aplica.

Note também que a falta de encaminhamento de logs no RLY-03 significa que os seus próprios logs sobre o listener de depuração podem nunca ter chegado ao SIEM — mais um motivo para preservar as evidências locais antes de corrigir.

### 22.7 Atividade prática: plano de deriva

**Laboratório 22** (salve como `lab22.py`, execute com `python3 lab22.py`):

```python
# Lab 22 - automated configuration-drift check with a dry-run plan (offline, standard library only)
# Synthetic desired state (from version control) and actual state (as collected from three relay hosts).
import json
desired = {"ssh.password_auth": False, "ssh.permit_root": False, "relay.listen": "10.30.0.5:8443",
           "relay.debug_listen": None, "ntp.servers": ["10.30.0.1", "10.30.0.2"], "log.forward": "siem-01:6514",
           "pkg.relayd": "2.4.1"}
actual = {
 "rly-01": {**desired},
 "rly-02": {**desired, "ssh.password_auth": True, "ntp.servers": ["pool.example.net"]},
 "rly-03": {**desired, "relay.debug_listen": "0.0.0.0:9000", "pkg.relayd": "2.3.9", "log.forward": None},
}
SAFE_AUTOFIX = {"ssh.password_auth", "ssh.permit_root", "ntp.servers", "log.forward"}  # low-risk, reversible
def plan(host, state):
    steps = []
    for k, want in desired.items():
        have = state.get(k)
        if have != want:
            mode = "auto" if k in SAFE_AUTOFIX else "ticket"
            steps.append({"host": host, "key": k, "have": have, "want": want, "mode": mode})
    return steps
all_steps = [s for h, st in actual.items() for s in plan(h, st)]
for s in all_steps:
    print(f"{s['host']} {s['key']:<20} have={json.dumps(s['have']):<22} want={json.dumps(s['want']):<26} -> {s['mode']}")
print("hosts compliant:", [h for h, st in actual.items() if not plan(h, st)])
print("dry run only: %d auto-fix steps, %d need a change ticket" % (sum(s['mode'] == 'auto' for s in all_steps), sum(s['mode'] == 'ticket' for s in all_steps)))
# Guard: never auto-apply to more than one host at a time, and stop if the host count with drift exceeds half the fleet
drifted = {s['host'] for s in all_steps}
print("guard: drifted hosts %d of %d -> %s" % (len(drifted), len(actual), "HALT and escalate (possible bad source of truth)" if len(drifted) > len(actual) / 2 else "proceed one host at a time"))
```

Saída esperada (Python 3.13.5):

```text
rly-02 ssh.password_auth    have=true                   want=false                      -> auto
rly-02 ntp.servers          have=["pool.example.net"]   want=["10.30.0.1", "10.30.0.2"] -> auto
rly-03 relay.debug_listen   have="0.0.0.0:9000"         want=null                       -> ticket
rly-03 log.forward          have=null                   want="siem-01:6514"             -> auto
rly-03 pkg.relayd           have="2.3.9"                want="2.4.1"                    -> ticket
hosts compliant: ['rly-01']
dry run only: 3 auto-fix steps, 2 need a change ticket
guard: drifted hosts 2 of 3 -> HALT and escalate (possible bad source of truth)
```

Leia primeiro a interrupção. Dois de três relays derivaram, mais da metade do parque, então a execução parou antes de aplicar qualquer coisa. Depois leia o plano por host: a autenticação por senha e os servidores de hora públicos do RLY-02, e a falta de encaminhamento de logs do RLY-03, estão na lista de correções automáticas; o listener de depuração e o pacote do relay mais antigo do RLY-03 não estão, e viram tickets. Antes de aprovar qualquer correção no RLY-03, copie os seus logs locais, porque, sem encaminhamento, eles podem ser o único registro de quando o listener de depuração apareceu.

### 22.8 Erros comuns e limites

- Automação que aplica mudanças sem um plano revisável.
- Listas longas de correções automáticas, incluindo configurações que podem ser evidência ou mudar o comportamento.
- Aplicar a todos os hosts de uma vez.
- Nenhuma condição de parada para "deriva demais".
- Código e credenciais da automação menos protegidos do que os hosts que ela gerencia.
- Tratar a conformidade automatizada como prova de segurança; ela prova apenas as configurações que confere.

A interrupção do Laboratório 22 com dois de três relays derivados é o quarto item feito do jeito certo.

Uma lista de correções automáticas que incluísse o listener de depuração teria removido a evidência de quem o configurou no RLY-03.

### Exercícios — capítulo 22

**EX064 — Aprove o plano.** *Objetivo:* revisar um plano de automação como aprovador de mudanças. *Entradas:* a saída do Laboratório 22. *Restrições:* aprove, modifique ou rejeite cada passo. *Etapas:* (1) decida para cada um dos cinco passos; (2) dê a ordem de aplicação; (3) declare a verificação depois de cada host. *Evidência esperada:* tabela. *Rubrica:* 3 = correções automáticas aprovadas host por host (RLY-02, depois RLY-03), listener de depuração preservado e depois removido sob um ticket após a investigação, atualização do pacote como mudança normal com canário (Capítulo 27), encaminhamento de logs restaurado cedo no RLY-03 para recuperar a visibilidade; verificações nomeadas; 2 = falta a ordem ou a preservação; 1 = aprovar tudo; 0 = nada.

**EX065 — Ajuste a salvaguarda.** *Objetivo:* raciocinar sobre limiares de parada. *Entradas:* a salvaguarda interrompe quando mais da metade do parque tem deriva. *Restrições:* o parque vai crescer para 12 relays. *Etapas:* (1) diga se "mais da metade" ainda é sensato com 12; (2) proponha uma salvaguarda melhor usando o tipo de deriva, e não apenas a contagem de hosts. *Evidência esperada:* parágrafo. *Rubrica:* 3 = reconhece que a mesma chave derivando em muitos hosts sugere uma fonte da verdade ruim, enquanto chaves diferentes em hosts diferentes sugerem mudanças locais; propõe parar quando uma chave difere em mais de uma fração definida dos hosts, ou quando há um commit recente e não revisado no estado desejado; 2 = parcial; 1 = mantém "metade"; 0 = nada.

**EX066 — Proteja o pipeline.** *Objetivo:* proteger a própria automação. *Entradas:* o repositório de estado desejado e a conta da automação. *Restrições:* cinco controles. *Etapas:* liste-os com evidências. *Evidência esperada:* tabela. *Rubrica:* 3 = branch protegido com revisão obrigatória, mantenedores restritos com MFA, commits ou tags assinados, conta da automação limitada aos hosts gerenciados com credenciais num cofre, logs das execuções encaminhados ao SIEM com um alerta para execuções fora do calendário; evidência para cada um; 2 = quatro; 1 = genérico; 0 = nada.

### Síntese do capítulo

Expresse o estado desejado como código, colete o estado real em modo somente leitura e calcule a deriva. Planeje antes de agir; corrija automaticamente apenas uma lista curta de configurações de baixo risco e reversíveis, e mande todo o resto — especialmente qualquer coisa que possa ser evidência — para o controle de mudanças. Limite o raio de impacto: um host de cada vez, parar na falha, interromper quando a deriva parecer uma fonte da verdade ruim. Proteja a automação com o mesmo cuidado que os hosts que ela gerencia.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue estudando — capítulo 22 de 30

[← Capítulo 21](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Infraestrutura crítica e segurança setorial: avaliação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- planejar testes seguros e autorizados que mostrem se os controles funcionam como pretendido;
- escrever **regras de engajamento** para testes num ambiente operacional;
- relatar a eficácia de cada controle com contagens, intervalos e medidas de tempo, usando uma regra de afirmação declarada;
- transformar os resultados da avaliação em trabalho de melhoria e em novos testes.

Os Capítulos 18 e 19 implementaram controles e regras. Este capítulo pergunta se eles funcionam. O guia técnico do NIST de testes de segurança descreve o planejamento, a condução e o relato de testes, incluindo a necessidade de autorização e de regras de engajamento ([NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)). Nos serviços críticos, a ênfase está em testes que sejam **seguros** para o processo físico.

### 23.1 O que testar

Teste cada controle contra a evidência que o seu cartão promete (Capítulo 18). Para os controles detectivos, injete um **evento de teste seguro** que deveria produzir o alerta: uma rajada deliberada de logins malsucedidos a partir de um endereço de teste; um fluxo de teste marcado de uma estação de trabalho de teste para uma porta de teste num CLP sobressalente; um heartbeat de teste pausado. Para os controles preventivos, tente a ação impedida de forma controlada: uma mensagem com um MAC errado; uma conexão a partir de uma zona não permitida. Para os controles de recuperação, execute uma restauração cronometrada (Capítulo 16).

### 23.2 Regras de engajamento

Antes de qualquer teste, escreva e obtenha a assinatura das **regras de engajamento**: finalidade; sistemas no escopo (por identificador) e explicitamente fora do escopo; ações permitidas; janela de tempo; quem está no local ou de plantão; plano de comunicação (quem é avisado antes, durante e depois); condições de parada (qualquer comportamento inesperado do processo interrompe o teste de imediato); como os eventos de teste são marcados para que respondedores e operadores os reconheçam; e como os resultados são guardados. Na zona das estações, prefira testes em equipamentos sobressalentes ou de laboratório, ou no lado do relay do conduíte, e nunca envie tráfego de teste a um controlador em produção sem o acordo explícito da operação para aquele controlador e aquele horário.

### 23.3 Regras de afirmação

Decida antes de testar que resultado contará como "eficaz". Uma **regra de afirmação** pode ser: o limite inferior de Wilson de 95 % da taxa de detecção é pelo menos 0,70 e a mediana do tempo até o alerta cumpre a meta. Fixar a regra de antemão afasta a tentação de escolher depois uma interpretação lisonjeira. A lição do Capítulo 9 se aplica: números pequenos de testes dão intervalos largos, então "8 de 8 detectados" pode ainda não cumprir a regra.

O 8 de 8 da Regra C é o caso: um histórico perfeito cujo limite inferior, 0,68, fica abaixo de 0,70.

### 23.4 Dos resultados ao trabalho

Cada controle "ainda não demonstrado" precisa ou de melhoria (corrigir a regra, a fonte, a configuração), ou de mais testes (se o problema for só o tamanho da amostra). Registre a data do próximo teste. Cada controle "demonstrado eficaz" é testado de novo num calendário, porque os controles se degradam.

O Laboratório 23 separa os seus quatro controles assim. A Regra C precisa apenas de mais testes: um sucesso a mais chegaria justo a 0,70 (0,701), e um segundo daria uma margem (0,722). A Regra B precisa primeiro de melhoria, exportando para o SIEM os fluxos do switch de estação que faltam, e depois de um novo teste. A FIM precisa das duas coisas: verificações mais frequentes nos arquivos críticos, e depois mais testes. A restauração de backup precisa da chave de decifração acrescentada ao runbook, e depois de novos exercícios.

### 23.5 Exemplo resolvido: os testes de controle de um trimestre (sintético)

O Laboratório 23 aplica a regra de afirmação a seis controles. Dois são demonstrados eficazes: a Regra A detectou 12 de 12 testes de força bruta, com mediana de 2 minutos (limite inferior 0,76), e o relay rejeitou todos os 40 testes de falha de MAC (limite inferior 0,91). Quatro ainda não estão demonstrados, por motivos diferentes:

- **Regra B** (Modbus corporativo→estação) detectou apenas 7 de 10. A investigação mostra que as três falhas foram fluxos de teste para um CLP num switch de estação cujos fluxos não são exportados para o SIEM — uma lacuna de fonte, e não uma falha da regra.
- **Regra C** (estação em silêncio) detectou 8 de 8, com mediana de 16 minutos contra uma meta de 20 minutos, mas o limite inferior é 0,68. Aqui o único problema é o tamanho da amostra: um teste bem-sucedido a mais cumpriria a regra por pouco, e dois a cumpririam com margem.
- **FIM** detectou 4 de 6 mudanças não aprovadas, com mediana de 1.440 minutos, porque a verificação de integridade roda uma vez por dia. Ela precisa tanto de melhoria (verificações mais frequentes nos arquivos críticos) quanto de mais testes.
- **Restauração de backup** cumpriu a sua meta 9 de 10 vezes; o limite inferior 0,60 fica abaixo de 0,70. A única falha foi a falta de uma chave de decifração no runbook de restauração — uma questão de processo corrigível.

### 23.6 Atividade prática: avalie os controles

**Laboratório 23** (salve como `lab23.py`, execute com `python3 lab23.py`):

```python
# Lab 23 - evaluating whether the service's controls work, not only whether they exist (offline, standard library only)
# Claim rule used here: 'shown effective' needs the 95% Wilson lower bound >= 0.70 and the time target met.
# Synthetic results of a quarter of control tests at Fallowmere. Each test injects a safe, authorized test event.
import math
tests = {  # control: (test events injected, detected/blocked as specified, median minutes to alert)
 "brute-force alert (rule A)": (12, 12, 2),
 "corp->station Modbus alert (rule B)": (10, 7, 4),
 "station-silent alert (rule C)": (8, 8, 16),
 "MAC rejection at relay": (40, 40, None),
 "FIM unapproved-change alert": (6, 4, 1440),
 "backup restore within 4 h": (10, 9, None),
}
def wilson_low(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n; c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h
target = {"FIM unapproved-change alert": 60, "station-silent alert (rule C)": 20}
for name, (n, k, mins) in tests.items():
    lo = wilson_low(k, n)
    late = name in target and mins is not None and mins > target[name]
    verdict = "shown effective" if lo >= 0.70 and not late else "not yet shown"
    print(f"{name:<36} {k:>2}/{n:<2} low95={lo:.2f} median {'-' if mins is None else mins:>4} min  {verdict}{' (too slow)' if late else ''}")
```

Saída esperada (Python 3.13.5):

```text
brute-force alert (rule A)           12/12 low95=0.76 median    2 min  shown effective
corp->station Modbus alert (rule B)   7/10 low95=0.40 median    4 min  not yet shown
station-silent alert (rule C)         8/8  low95=0.68 median   16 min  not yet shown
MAC rejection at relay               40/40 low95=0.91 median    - min  shown effective
FIM unapproved-change alert           4/6  low95=0.30 median 1440 min  not yet shown (too slow)
backup restore within 4 h             9/10 low95=0.60 median    - min  not yet shown
```

Os dois controles eficazes são a Regra A, 12 de 12 com limite inferior 0,76, e a verificação de MAC do relay, 40 de 40 com limite inferior 0,91. Para cada um dos quatro ainda não demonstrados, escreva uma linha: o motivo (Regra B, uma lacuna de fonte; Regra C, tamanho da amostra; FIM, verificações diárias e poucos testes; restauração, uma lacuna no runbook), a próxima ação e a data do próximo teste. Não arredonde o 0,68 da Regra C para 0,70.

### 23.7 Erros comuns e limites

- Testar sem regras de engajamento escritas, ou com escopo pouco claro.
- Eventos de teste não marcados, que assim disparam uma resposta real — ou eventos reais descartados como testes.
- Regras de afirmação escolhidas depois de ver os resultados.
- Relatar "8/8 = 100 %" sem intervalo.
- Tratar "ainda não demonstrado" como "falhou", ou como "está bem".
- Testes em controladores em produção sem o acordo da operação.

Os testes mostram como os controles respondem aos eventos de teste que você projetou. Adversários reais e falhas reais podem ser diferentes; varie os testes ao longo do tempo e inclua cenários de incidentes ocorridos em outros lugares.

### Exercícios — capítulo 23

**EX067 — Regras de engajamento.** *Objetivo:* autorizar um teste seguro. *Entradas:* um teste da Regra B usando uma estação de trabalho de teste e o CLP Arlen 300 sobressalente do laboratório da FSTS, mais um fluxo de teste para o CLP da PS-04 durante uma visita ao local. *Restrições:* todos os elementos do Capítulo 23 ("Regras de engajamento"). *Etapas:* escreva as regras de engajamento. *Evidência esperada:* uma página. *Rubrica:* 3 = escopo por identificador, com o fluxo para o CLP em produção permitido apenas com a aprovação nominal da Água, um teste somente de leitura ou só de conexão (sem escritas), engenheiro no local, endereço de teste marcado, comunicação à sala de controle e ao SOC, condições de parada explícitas, armazenamento dos resultados; 2 = falta um elemento; 1 = informal; 0 = nada.

**EX068 — Quantos testes a mais?** *Objetivo:* planejar o tamanho da amostra. *Entradas:* Regra C com 8/8. *Restrições:* use o limite inferior de Wilson do Laboratório 23. *Etapas:* encontre o número de sucessos consecutivos adicionais necessários para que o limite inferior chegue a 0,70. *Evidência esperada:* o número e a execução. *Rubrica:* 3 = um sucesso a mais (9/9 dá um limite inferior de cerca de 0,701; 10/10 dá cerca de 0,722), mostrado corretamente, com o comentário de que cumprir um limiar por uma margem de 0,001 é frágil e vale planejar um segundo teste extra; 2 = certo, com método pouco claro; 1 = chutado; 0 = nada.

**EX069 — Diagnostique uma falha.** *Objetivo:* transformar resultados em trabalho. *Entradas:* a Regra B falhou em 3 de 10 testes porque os fluxos de um switch de estação não eram exportados. *Restrições:* plano de correção e de novo teste. *Etapas:* (1) declare a correção; (2) declare o monitoramento que teria detectado a lacuna mais cedo (Capítulo 19); (3) planeje o novo teste. *Evidência esperada:* meia página. *Rubrica:* 3 = habilitar a exportação de fluxos naquele switch sob mudança; acrescentar uma regra de ausência de fonte por exportador de fluxos; testar de novo com pelo menos 10 eventos em todos os switches; atualizar o cartão de controle; 2 = correção sem monitoramento; 1 = "ajustar a regra B"; 0 = nada.

### Síntese do capítulo

Teste os controles contra a evidência que eles prometem, usando eventos de teste seguros e marcados, sob regras de engajamento assinadas que protegem o processo físico. Fixe a regra de afirmação antes de testar, relate contagens com intervalos e medidas de tempo, e distinga "demonstrado eficaz" de "ainda não demonstrado" — e por quê. Transforme todo resultado em melhoria ou em mais testes, e teste de novo num calendário.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue estudando — capítulo 23 de 30

[← Capítulo 22](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Métodos de pesquisa aplicada

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- transformar uma pergunta operacional num estudo pequeno e respondível, com um método declarado;
- escolher uma comparação — antes/depois, com/sem, pareada — e reconhecer o que cada uma pode e não pode mostrar;
- coletar dados de forma ética e segura num ambiente operacional;
- relatar os resultados com os seus limites, para que um gestor possa agir sobre eles sem lê-los além do que dizem.

Os tecnólogos recebem com frequência perguntas que parecem simples — "a nova regra de alerta reduziu o tempo de resposta?", "o RLY-02 está mais lento desde a atualização?", "as nossas visitas às estações encontram deriva de configuração?" — e as respondem com impressões. Este capítulo ensina o estudo pequeno e honesto que fica entre uma impressão e um projeto de pesquisa. Ele lê os métodos publicados para usá-los, e não para produzir métodos novos.

### 24.1 Da pergunta ao estudo

Escreva a pergunta de modo que os dados possam respondê-la: população (quais estações, alertas, hosts), medida (com definição — Capítulo 9), comparação (contra o quê), período e decisão (o que será feito de forma diferente dependendo da resposta). "O novo texto de primeira ação da Regra C reduziu o tempo entre o alerta e a ligação para a sala de controle?" é respondível; "o monitoramento está melhor?" não é.

A pergunta sobre a Regra C nomeia a sua população (alertas de ausência), a medida (minutos até a ligação) e a decisão (adotar o texto ou não).

"O monitoramento está melhor?" não nomeia nenhuma delas.

### 24.2 As comparações e as suas armadilhas

- **Antes/depois** no mesmo sistema é fácil e fraca: qualquer outra coisa que tenha mudado no período (pessoal, estação do ano, carga de trabalho) pode explicar a diferença.
- **Com/sem** — algumas estações ou turnos recebem a mudança, outros não — é mais forte se os grupos forem semelhantes, e mais forte ainda se quem recebe a mudança for decidido por um método justo (alternância, sorteio), e não por quem se voluntariou.
- As comparações **pareadas** — as mesmas pessoas ou os mesmos hosts medidos sob as duas condições — removem as diferenças entre as unidades.

Fique atento à **regressão à média**: mudanças introduzidas depois de um mês excepcionalmente ruim costumam parecer eficazes porque o mês seguinte teria sido melhor de qualquer forma. Fique atento à **agregação** de grupos com linhas de base diferentes (Capítulo 9). E anote a análise antes de ver os resultados — a ideia por trás do pré-registro na pesquisa ([Nosek et al., 2018](https://doi.org/10.1073/pnas.1708274114)) também se aplica em pequena escala: ela impede que você escolha a medida que favorece a mudança.

### 24.3 Coletar dados num ambiente operacional

Use os dados que o serviço já registra, sempre que possível: horários de alerta e de reconhecimento, carimbos de tempo dos tickets, contagens do relay. Se você precisar de dados novos — cronometrar um procedimento manual, perguntar aos operadores —, obtenha o acordo do responsável operacional, torne a participação voluntária para as pessoas, não perturbe a operação e não registre mais informação pessoal do que a pergunta precisa. Os princípios do Menlo Report — respeito às pessoas, beneficência, justiça e respeito à lei e ao interesse público — são uma verificação útil para qualquer estudo que envolva pessoas ou sistemas de TIC ([Menlo Report, 2012](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf)).

### 24.4 Uma análise que cabe nos dados

Para estudos operacionais pequenos, os métodos simples são os melhores e os mais honestos: medianas e percentis (Capítulo 9), diferenças entre grupos com o número de observações declarado, intervalos para proporções (Wilson) e uma verificação de se o resultado sobrevive a explicações alternativas óbvias (remover uma semana incomum; comparar os turnos separadamente). Se a conclusão mudar quando um único dado é removido, diga isso.

O estudo da Regra C fez essa verificação: remover a semana da interrupção da operadora levou a mediana do texto antigo de 14 para 11 minutos, ainda mais lenta que 6.

Comparar os turnos separadamente teria sido a próxima verificação.

### 24.5 Relato

Uma nota de estudo de uma página tem: pergunta; método (população, medida, comparação, período, o que foi decidido de antemão); resultados com contagens; limites e explicações alternativas; e recomendação com a confiança que ela merece. Separe os resultados observados das inferências, como em todo este livro.

Para o estudo da Regra C, os resultados observados são 11 alertas com o texto antigo, com mediana de 14 minutos, e 12 alertas com o texto novo, com mediana de 6; a inferência é que a primeira ação ajuda. A linha de limites nomeia os números pequenos, o efeito da consciência do estudo e a semana da interrupção da operadora.

### 24.6 Exemplo resolvido: o novo texto de primeira ação ajudou? (sintético)

A FSTS reescreveu o alerta da Regra C para incluir uma primeira ação ("ligar para a sala de controle da Água, depois conferir a situação da operadora"). A pergunta: isso encurta o tempo entre o alerta e a ligação para a sala de controle? A equipe alternou o texto antigo e o novo por semana, durante oito semanas, ao longo da escala de plantão, de modo que cada tecnólogo recebeu os dois. Resultados: 11 alertas com o texto antigo, mediana de 14 minutos até a ligação; 12 com o texto novo, mediana de 6 minutos. Todo tecnólogo que recebeu os dois teve uma mediana menor com o texto novo. Limites: números pequenos; os tecnólogos sabiam do estudo (podem ter se esforçado mais); uma semana do texto antigo incluiu uma interrupção da operadora, com muitos alertas de uma vez. Removendo essa semana, a mediana do texto antigo é de 11 minutos — ainda mais lenta que 6. Recomendação: adotar o novo texto para todas as regras de ausência; medir de novo daqui a três meses a partir dos dados de rotina.

### 24.7 Atividade prática: projete um estudo

Escolha uma pergunta entre: (a) a latência p95 do RLY-02 aumentou desde o relayd 2.4.1? (b) as visitas trimestrais às estações encontram deriva que as verificações automatizadas perdem? (c) a revisão de acessos encontra menos problemas a cada trimestre? Escreva o projeto do estudo: pergunta, população, medida, comparação, período, decisão, fonte dos dados, notas éticas e de segurança, análise planejada de antemão.

Para a pergunta (a), a comparação está pronta: o canário do Capítulo 27 mediu a latência p95 do RLY-03 em 41 ms no relayd 2.4.1, contra 37 ms no 2.4.0, durante uma hora noturna. Um estudo estenderia isso a várias semanas de dados de rotina, incluiria o pico da manhã e as execuções semanais de relatórios, e decidiria de antemão que aumento dispararia um rollback.

### 24.8 Erros comuns e limites

- Perguntas que os dados não conseguem responder.
- Comparações antes/depois apresentadas como prova.
- Escolher a medida depois de ver os dados.
- Estudos que perturbam a operação ou coletam dados pessoais desnecessários.
- Resultados relatados sem contagens nem limites.
- Tratar um estudo pequeno como definitivo; ele é evidência para uma decisão, a ser conferida de novo.

O estudo da Regra C evitou o segundo erro ao alternar o texto por semana, em vez de comparar o antes com o depois.

Pedir a opinião dos tecnólogos depois do teste não teria acrescentado nada que os tempos não mostrassem, e teria coletado opiniões pessoais de que o estudo não precisava.

### Exercícios — capítulo 24

**EX070 — Torne-a respondível.** *Objetivo:* reformular perguntas vagas. *Entradas:* (a) "A nossa aplicação de patches é boa?"; (b) "Os fornecedores são um risco?"; (c) "O SOC ajuda?" *Restrições:* cada pergunta reescrita precisa nomear população, medida, comparação e período. *Etapas:* reescreva as três. *Evidência esperada:* três perguntas. *Rubrica:* 3 = específicas, mensuráveis, com comparação e período e uma decisão associada; 2 = uma fraca; 1 = ainda vagas; 0 = nada.

**EX071 — Encontre as fraquezas.** *Objetivo:* criticar um estudo. *Entradas:* "Depois da interrupção de março, acrescentamos a Regra C. Em abril houve 30 % menos reclamações de telemetria do que em março, o que prova que a Regra C funciona." *Restrições:* quatro fraquezas. *Etapas:* nomeie cada uma e proponha um projeto melhor. *Evidência esperada:* lista e projeto. *Rubrica:* 3 = apenas antes/depois, regressão à média depois de um mês incomum, reclamações como medida ruim de detecção, sem contagens nem intervalo, outras mudanças no período; o projeto melhor mede o tempo de detecção nos alertas, com uma comparação; 2 = três; 1 = uma; 0 = nada.

**EX072 — Escreva a nota do estudo.** *Objetivo:* relatar um estudo pequeno. *Entradas:* Capítulo 24 ("Exemplo resolvido: o novo texto de primeira ação ajudou?"). *Restrições:* uma página; títulos do Capítulo 24 ("Relato"). *Etapas:* escreva a nota. *Evidência esperada:* nota. *Rubrica:* 3 = todos os títulos; contagens e medianas; limites incluindo a consciência do estudo, o n pequeno e a semana da interrupção, com a verificação de sensibilidade; recomendação proporcional, com um plano de nova medição; 2 = limites rasos; 1 = defesa da causa; 0 = nada.

### Síntese do capítulo

Transforme as perguntas operacionais em estudos pequenos, com população, medida, comparação, período e decisão declarados. Prefira comparações que descartem as alternativas óbvias — alternância ou pareamento em vez de antes/depois — e decida a análise de antemão. Colete os dados com segurança e ética, com o acordo do responsável operacional, analise de forma simples, confira a sensibilidade e relate contagens e limites, para que o resultado seja usado com a confiança que merece.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue estudando — capítulo 24 de 30

[← Capítulo 23](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto em equipe

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- trabalhar como parte de uma pequena equipe de entrega que constrói e opera um serviço compartilhado;
- dividir o projeto de integração do LANTERN em itens de trabalho com critérios de aceitação e evidências;
- usar a revisão — de código, configuração e documentos — como um controle de segurança;
- conduzir revisões curtas e sem culpados do que deu certo e do que deu errado, e transformá-las em mudanças.

Do Capítulo 26 em diante, o livro passa à entrega, à implantação e ao trabalho de conclusão. Os serviços reais são construídos por equipes, e muitas falhas de segurança são falhas de equipe: uma premissa que ninguém conferiu porque cada um achou que outro tinha conferido, uma mudança incorporada sem revisão porque o revisor estava ocupado. Este capítulo é um ateliê: ele dá uma estrutura para o trabalho em equipe de que o trabalho de conclusão precisa.

### 25.1 A equipe e os seus papéis

Uma equipe de entrega do LANTERN na FSTS tem quatro ou cinco pessoas: um **dono do serviço** (prioriza, fala pelos clientes), dois ou três **tecnólogos** (constroem e operam), um **revisor de segurança** (pode ser um dos tecnólogos, em rodízio) e um **representante do cliente** da operação de Água, que participa das revisões e aceita o trabalho que afeta o processo. Os papéis se revezam onde possível, para que o conhecimento seja compartilhado; nenhuma pessoa deve ser a única que entende o relay ou detém as suas chaves (a independência do Capítulo 8).

### 25.2 Itens de trabalho com critérios de aceitação

Todo item de trabalho declara o que significa "pronto" na forma de **critérios de aceitação** que produzem evidências. "Acrescentar alertas de silêncio de estação" é um desejo. "A Regra C alerta em até 20 minutos depois que o heartbeat de uma estação para, verificado por três silêncios de teste injetados em duas estações; primeira ação escrita e acordada com a sala de controle da Água; cartão de controle atualizado" é um item de trabalho. As evidências passam a fazer parte do registro do trabalho de conclusão.

A fusão do NTP neste capítulo mostra o custo de um critério fraco: "atualizar os servidores NTP" foi cumprido enquanto todos os relays perdiam a sua segunda fonte de tempo. O critério reescrito, "deslocamento < 1 s em todos os relays por 24 h", teria falhado no primeiro dia.

### 25.3 A revisão como controle

A revisão por pares de código, de arquivos de estado desejado, de mudanças de firewall e de runbooks pega erros, espalha o conhecimento e torna mais difícil que uma única conta comprometida ou descuidada mude o serviço sozinha. Torne a revisão **obrigatória** para tudo o que muda o serviço (branches protegidos, Capítulo 22), **específica** (o revisor confere contra os critérios de aceitação e as propriedades de projeto do Capítulo 8, e não apenas o estilo) e **registrada**. Faça rodízio dos revisores, para que a revisão não vire um carimbo de um aprovador habitual.

A fusão do NTP foi revisada, mas quanto à sintaxe; o revisor nunca conferiu se o novo servidor existia.

### 25.4 Ritmo

Um ritmo curto e regular combina com equipes operacionais: uma conversa semanal de planejamento (o que será feito, por quem, com que evidência), uma breve verificação diária (o que está bloqueado) e uma revisão ao fim de cada ciclo (o que foi entregue, mostrado com as suas evidências ao representante do cliente). O trabalho operacional — incidentes, falhas — interrompe o trabalho de projeto; planeje para ele, em vez de fingir que não vai acontecer.

O silêncio da PS-09 e a falha do disco do host de salto são as interrupções para as quais planejar.

Em Fallowmere, foi na verificação diária que o silêncio da PS-09 foi levantado, na manhã seguinte ao disparo da Regra C.

### 25.5 Revisões sem culpados

Quando algo dá errado — uma mudança que falhou, um alerta perdido, um quase acidente —, faça uma curta **revisão sem culpados**: o que aconteceu, o que as pessoas sabiam em cada momento, por que as suas ações faziam sentido para elas naquele momento, que condições permitiram o problema e o que vai mudar. O material de SRE do Google descreve o valor dos postmortems sem culpados para aprender com os incidentes sem desencorajar o relato honesto ([livro de SRE do Google, cultura de postmortem](https://sre.google/sre-book/postmortem-culture/)); o trabalho de Reason sobre o erro humano distingue culpar indivíduos de corrigir as condições do sistema que tornam os erros prováveis ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). O produto são mudanças, cada uma com um responsável — e não uma pessoa a culpar.

### 25.6 Exemplo resolvido: uma fusão que não deveria ter acontecido (sintético)

Durante o projeto, um tecnólogo incorporou uma mudança de estado desejado que removia `10.30.0.2` dos servidores NTP dos relays, com a intenção de substituí-lo por um novo servidor que ainda não tinha sido construído. A automação a aplicou; os relays ficaram com uma fonte de tempo; quando essa fonte reiniciou para manutenção, dois dias depois, os relays derivaram, e as mensagens das estações começaram a falhar na janela de 120 segundos. A revisão sem culpados descobriu: a mudança foi revisada, mas o revisor conferiu a sintaxe, e não se o novo servidor existia; os critérios de aceitação diziam apenas "atualizar os servidores NTP"; o monitoramento de deriva conferia se as configurações correspondiam ao estado desejado, e correspondiam; e não havia alerta para o deslocamento do relógio. Mudanças: a lista de verificação da revisão inclui "todo sistema referenciado existe e responde?"; os critérios de aceitação para mudanças de hora incluem "deslocamento < 1 s em todos os relays por 24 h"; novo alerta para deslocamento do relógio do relay > 2 s. Ninguém foi culpado; três condições foram corrigidas.

### 25.7 Atividade prática: backlog do projeto

Escreva o backlog para o trabalho de conclusão (Capítulo 29): pelo menos dez itens de trabalho cobrindo o relay, a validação, a autenticação, o historiador, os logs, as regras de monitoramento, o acesso, o backup e a restauração, a automação, os runbooks e as evidências. Cada um precisa de critérios de aceitação que produzam evidências e de um papel responsável.

Um item completo como modelo: "Alerta de deslocamento do relógio do relay: alertar quando o deslocamento de qualquer relay exceder 2 s; aceitação, um deslocamento injetado num relay de teste gera o alerta em um ciclo de avaliação e a primeira ação está escrita; responsável, monitoramento da FSTS." Ele vem direto da revisão do NTP. Inclua pelo menos um item que exista apenas para fechar uma lacuna encontrada antes, como a mediana de detecção de 1.440 minutos da FIM.

### 25.8 Erros comuns e limites

- Itens de trabalho sem critérios de aceitação.
- Revisão que confere o estilo, e não a substância; ou um único revisor habitual.
- Um único membro da equipe como a única pessoa que entende um componente.
- Planos que ignoram as interrupções operacionais.
- Revisões de falhas que terminam em "ter mais cuidado".

A revisão do NTP neste capítulo terminou com três condições mudadas, e não com "ter mais cuidado".

A fusão do NTP mostra os dois primeiros: um critério de aceitação vago e uma revisão só da sintaxe. Uma única pessoa entender o armazenamento de chaves é o terceiro, que a passagem do Capítulo 26 expôs quando a equipe que recebia não conseguiu encontrá-lo.

### Exercícios — capítulo 25

**EX073 — Critérios de aceitação.** *Objetivo:* escrever critérios que produzam evidências. *Entradas:* itens de trabalho: (a) "proteger o SSH nos relays"; (b) "backups para o historiador"; (c) "processo de acesso de fornecedores". *Restrições:* cada critério precisa ser verificável por outra pessoa. *Etapas:* reescreva cada um com pelo menos três critérios. *Evidência esperada:* lista. *Rubrica:* 3 = por exemplo, (a) autenticação por senha desligada e listener na interface de gerenciamento em todos os relays (saída da verificação de deriva), conexão a partir da zona corporativa recusada (registro de teste), MFA no host de salto; (b) backup noturno com uma cópia imutável, teste de restauração dentro do RTO registrado; (c) habilitação limitada no tempo testada de ponta a ponta, expiração verificada, ciência da Kell registrada; 2 = critérios parcialmente verificáveis; 1 = desejos reafirmados; 0 = nada.

**EX074 — Lista de verificação da revisão.** *Objetivo:* tornar a revisão substantiva. *Entradas:* o caso do Capítulo 25 ("Exemplo resolvido: uma fusão que não deveria ter acontecido") e as propriedades de projeto do Capítulo 8. *Restrições:* oito itens. *Etapas:* escreva uma lista de verificação para revisar uma mudança de estado desejado. *Evidência esperada:* lista de verificação. *Rubrica:* 3 = inclui a existência e a alcançabilidade dos sistemas referenciados, a direção da confiança preservada, nenhum novo listener em todas as interfaces, segredos fora da mudança, rollback definido, critérios de aceitação e verificação, clientes afetados informados, implantação escalonada; 2 = seis; 1 = itens só de estilo; 0 = nada.

**EX075 — Revisão sem culpados.** *Objetivo:* conduzir uma revisão que produza mudanças. *Entradas:* incidente: um tecnólogo de plantão silenciou a Regra B por 24 horas durante uma noite ruidosa e esqueceu de reativá-la; um fluxo não declarado real ficou sem alerta por três dias. *Restrições:* sem culpados; condições, e não pessoas. *Etapas:* escreva a revisão: linha do tempo, o que fazia sentido no momento, condições, mudanças com responsáveis. *Evidência esperada:* uma página. *Rubrica:* 3 = reconhece o ruído por evento da Regra B (Capítulo 19) como uma causa, a falta de expiração automática dos silenciamentos e a falta de visibilidade das regras silenciadas; mudanças como alertas por episódio, silenciamentos que expiram e aparecem no painel, item na lista de verificação de passagem de turno; 2 = mudanças parciais; 1 = culpa o tecnólogo; 0 = nada.

### Síntese do capítulo

Os serviços são construídos por equipes. Dê aos papéis responsabilidades claras e faça o rodízio deles, para que o conhecimento e o controle não se concentrem numa só pessoa. Escreva itens de trabalho com critérios de aceitação que produzam evidências. Torne a revisão obrigatória, específica e registrada, para que ela funcione como um controle de segurança. Planeje para as interrupções operacionais e aprenda com as falhas por meio de revisões sem culpados, que mudam condições em vez de culpar pessoas.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue estudando — capítulo 25 de 30

[← Capítulo 24](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Infraestrutura crítica e segurança setorial: passagem para a operação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- preparar um serviço para a passagem da equipe de projeto para as pessoas que vão operá-lo todos os dias;
- escrever **runbooks** que um colega competente consiga seguir às 03:00 sem o autor;
- definir a responsabilidade, os níveis de serviço e as evidências de que o serviço está saudável;
- conduzir uma passagem que teste o entendimento, e não apenas entregue documentos.

Um serviço não está pronto quando funciona; está pronto quando outra pessoa consegue operá-lo. Muitos controles de segurança falham na passagem: a pessoa que entendia a rotação de chaves sai do projeto; a equipe de plantão nunca aprendeu o que significa a primeira ação da Regra C; a restauração do backup foi ensaiada apenas pelo seu autor.

### 26.1 O que é entregue

Um pacote de passagem do LANTERN contém:

- **Descrição do serviço** — propósito, clientes, arquitetura com zonas, conduítes e caminhos de gerenciamento (Capítulo 8), e as propriedades de projeto que precisam ser preservadas.
- **Responsabilidade** — dono do serviço, responsável técnico, responsável de segurança, contatos dos clientes, contatos dos fornecedores, com papéis e números fora do horário comercial.
- **Níveis de serviço** — o que os clientes podem esperar (telemetria em até 60 s, idade do valor exibida, RTO de 4 h para o historiador) e como isso é medido (Capítulo 9).
- **Runbooks** para tarefas rotineiras e de emergência (veja "Runbooks que funcionam às 03:00" abaixo).
- **Cartões de controle** para cada controle, com as datas das últimas evidências (Capítulo 18).
- **Monitoramento** — cada regra com a sua primeira ação, e as verificações de automonitoramento (Capítulo 19).
- **Itens em aberto** — problemas conhecidos, riscos aceitos com responsáveis, controles compensatórios com datas de término.
- **Registro de evidências** — o que foi testado e quando (o Capítulo 29 o monta).

### 26.2 Runbooks que funcionam às 03:00

Um bom runbook é escrito para um colega competente que nunca viu este serviço, sob pressão de tempo. Ele declara o seu **propósito** e **quando usá-lo**; os **pré-requisitos** (acesso, ferramentas, aprovações); as **etapas**, numeradas, cada uma com o comando ou ação exata e o que você deve ver; os **pontos de decisão** ("se o log do relay mostrar falhas de MAC, vá para a etapa 9; caso contrário, etapa 12"); as **notas de segurança** onde uma etapa pode afetar a operação; o **rollback**; e **como registrar** o que foi feito. Teste cada runbook fazendo alguém que não seja o autor segui-lo num sistema de teste, cronometrando.

Runbooks centrais do LANTERN: acrescentar ou remover uma estação (mudança padrão); rotacionar a chave de uma estação; reconstruir o host do relay; restaurar o historiador; responder a cada regra de alerta; suspeita de comprometimento do relay (primeiros passos e escalonamento); manutenção planejada com a operação de Água; habilitar o acesso de fornecedores.

### 26.3 Evidências de saúde

A equipe que recebe deve conseguir responder "o LANTERN está saudável?" em dois minutos, a partir de um painel ou de um relatório diário: estações reportando / esperadas; contagens de aceitação, rejeição e quarentena por hora; folga de recursos do relay (Capítulo 1); deslocamentos de relógio; atualidade das fontes de log; último backup bem-sucedido e último teste de restauração; última avaliação das regras; alertas abertos; regras silenciadas e a sua expiração (Capítulo 25).

A passagem deste capítulo encontrou a lacuna: o relatório de saúde dizia "backups OK", mas não mostrava a data do teste de restauração. Para o LANTERN, a verificação de dois minutos mostraria 14 estações esperadas, as contagens de aceitação, rejeição e quarentena, os deslocamentos de relógio contra o alerta de 2 s, o disco do RLY-01 contra o seu alarme de 85 % e qualquer regra silenciada com a sua expiração.

### 26.4 Conduzir a passagem

A passagem é um processo, e não um e-mail. Conduza-a em etapas: apresentação do pacote à equipe que recebe; **acompanhamento**, em que a equipe que recebe executa tarefas rotineiras com a equipe de projeto observando; **acompanhamento invertido**, em que a equipe de projeto observa a equipe que recebe lidar com um alerta de teste injetado e com um runbook; e **aceitação**, em que o dono do serviço e o líder da equipe que recebe aprovam, com os itens em aberto listados. Combine um período de **suporte inicial** em que a equipe de projeto continua disponível.

O acompanhamento invertido de Fallowmere usou um alerta da Regra C injetado para a PS-09.

### 26.5 Exemplo resolvido: uma passagem que encontrou três lacunas (sintético)

Durante o acompanhamento invertido, a equipe de operações da FSTS recebe um alerta de teste da Regra C para a PS-09. O tecnólogo de plantão segue o runbook e liga para a sala de controle da Água — corretamente — e depois confere a situação da operadora, como está escrito. O runbook não menciona conferir o log de falhas de MAC do relay, então o tecnólogo liga para a BayTel; a causa injetada era uma divergência de chave. Segundo, o runbook de rotação de chaves se refere ao "armazenamento de chaves" sem dizer onde ele fica nem quem tem acesso; a equipe que recebe não consegue segui-lo. Terceiro, o relatório de saúde mostra "backups OK", mas não a data do último teste de restauração. As três são corrigidas antes da aceitação; a passagem atrasa uma semana, o que é muito mais barato do que descobrir as lacunas durante um incidente.

### 26.6 Atividade prática: escreva e teste um runbook

Escreva o runbook "Responder à Regra C — estação silenciosa" usando a estrutura de "Runbooks que funcionam às 03:00" acima, incluindo o ponto de decisão do exemplo resolvido acima ("uma passagem que encontrou três lacunas"). Peça a um colega (ou, se estiver estudando sozinho, a você mesmo depois de um dia de intervalo) que o siga com os dados do Laboratório 20 e anote cada ponto em que hesitou.

Use a lição da passagem como ponto de decisão: depois de ligar para a sala de controle da Água, confira o log de falhas de MAC do relay para a estação silenciosa antes de ligar para a BayTel. No teste da passagem, a causa injetada era uma divergência de chave, e o runbook sem essa etapa mandou o tecnólogo de plantão para a operadora. Com os dados do Laboratório 20, a mesma etapa separa as mensagens perdidas da PS-07 do deslocamento de relógio da PS-09.

### 26.7 Erros comuns e limites

- Documentação entregue sem testar se os outros conseguem usá-la.
- Runbooks que dizem "investigar" ou "corrigir o problema".
- Relatórios de saúde que mostram o sucesso da configuração, mas não evidências de eficácia.
- Passagem sem acompanhamento.
- Itens em aberto e riscos aceitos deixados de fora para que o serviço pareça completo.
- Equipe de projeto que desaparece no dia seguinte à aceitação.

O exercício com a PS-09 pegou o segundo erro: "conferir a situação da operadora" mandou o tecnólogo para a BayTel por causa de uma divergência de chave.

A linha "backups OK" sem data de restauração é o terceiro.

### Exercícios — capítulo 26

**EX076 — Crítica de runbook.** *Objetivo:* melhorar um runbook. *Entradas:* "Rotação de chaves: 1. Gerar a nova chave. 2. Colocá-la no relay e na estação. 3. Conferir se funciona. 4. Apagar a chave antiga." *Restrições:* identifique pelo menos seis problemas. *Etapas:* liste os problemas e reescreva. *Evidência esperada:* lista e reescrita. *Rubrica:* 3 = faltam propósito e pré-requisitos, sem local do armazenamento nem acesso, sem período de sobreposição (Capítulo 18), sem verificação específica, sem aviso de safety/operação, sem rollback, chave antiga apagada cedo demais para o acúmulo, sem registro; a reescrita trata deles; 2 = quatro ou cinco; 1 = cosméticos; 0 = nada.

**EX077 — Relatório de saúde.** *Objetivo:* definir as evidências de saúde. *Entradas:* Capítulo 26 ("Evidências de saúde"). *Restrições:* uma tela; no máximo dez itens. *Etapas:* escolha os itens, dê a cada um um limiar verde/âmbar/vermelho e diga quem o lê diariamente. *Evidência esperada:* tabela. *Rubrica:* 3 = itens cobrindo disponibilidade (estações reportando), integridade (rejeição/quarentena), capacidade, tempo, logs, backup/restauração, saúde do monitoramento e silenciamentos; limiares sensatos; leitor nomeado; 2 = oito itens ou limiares fracos; 1 = lista sem limiares; 0 = nada.

**EX078 — Decisão de aceitação.** *Objetivo:* decidir se aceita uma passagem. *Entradas:* todos os runbooks testados, exceto a restauração do historiador (testada apenas pelo seu autor); dois cartões de controle sem datas de evidência; um risco aceito (PS09-RTU sem suporte) com responsável e plano. *Restrições:* aceitar, aceitar com condições ou rejeitar. *Etapas:* decida e justifique, listando as condições com datas. *Evidência esperada:* parágrafo. *Rubrica:* 3 = aceitar com condições: teste independente de restauração do historiador numa data próxima, evidências para os dois controles até uma data, suporte inicial até as condições serem cumpridas; reconhece que o risco aceito está tratado corretamente; 2 = decisão sem condições; 1 = aceitar incondicionalmente; 0 = nada.

### Síntese do capítulo

Um serviço está pronto quando outras pessoas conseguem operá-lo. Entregue um pacote com descrição, responsabilidade, níveis de serviço, runbooks, cartões de controle, monitoramento, itens em aberto e evidências. Escreva runbooks para um colega competente às 03:00 e teste-os com alguém que não seja o autor. Forneça evidências de saúde que mostrem eficácia, e não apenas configuração. Conduza a passagem como apresentação, acompanhamento, acompanhamento invertido e aceitação com suporte inicial, e corrija as lacunas que ela revelar.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue estudando — capítulo 26 de 30

[← Capítulo 25](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Implantação e validação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- preparar uma implantação com **pré-verificações**, incluindo a verificação do que está sendo implantado;
- implantar em etapas, com um **canário** e critérios explícitos de promoção e de rollback;
- validar depois da implantação contra as propriedades funcionais e de segurança do serviço;
- declarar o que uma janela de validação pode e não pode mostrar.

O Capítulo 14 planejou mudanças; o Capítulo 22 automatizou a configuração. Este capítulo trata de implantações de software — uma nova versão do relay, uma atualização do historiador —, em que a mudança é maior e mais difícil de prever. Em serviços críticos, o objetivo é encontrar um problema num único host, num horário tranquilo, com um rollback pronto, e não em todos os hosts no pico da manhã.

### 27.1 Pré-verificações

Antes de implantar: a mudança está aprovada; a operação conhece a janela; um backup da configuração foi feito e o pacote de rollback está preparado; e o **próprio pacote está verificado** — a sua assinatura ou o digest publicado conferido contra o do fornecedor, para que o que você instala seja o que o fornecedor liberou. As orientações de desenvolvimento seguro pedem aos produtores que protejam a integridade do software liberado, por exemplo com assinaturas ([NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)); como implementador, a sua parte nisso é conferi-las, e tratar um pacote não verificável como um achado.

### 27.2 Canários e critérios de promoção

Uma implantação **canário** instala a nova versão primeiro num único host e a compara com os hosts ainda na versão antiga, no mesmo período e sob a mesma carga. O workbook de SRE do Google descreve o canário como uma implantação parcial e limitada no tempo, avaliada contra uma população de controle antes da implantação mais ampla ([workbook de SRE do Google, Canarying releases](https://sre.google/workbook/canarying-releases/)). Escreva os **critérios de promoção** antes de implantar: para o LANTERN, razão de aceitação no máximo 0,2 ponto percentual abaixo do controle; latência p95 no máximo 25 % acima do controle; nenhuma reinicialização; rejeições por MAC inalteradas. Se algum critério falhar, faça o rollback do canário e abra um registro de problema. Se todos passarem, promova um host por vez.

### 27.3 Validação depois da implantação

Depois de atualizar cada host, valide: as propriedades **funcionais** (todas as estações aceitas, latência normal, historiador recebendo); as propriedades de **segurança** (verificações de MAC ainda aplicadas — injete uma mensagem de teste com um MAC errado; listeners inalterados — execute a verificação de deriva; logs ainda encaminhados e interpretados — confira as contagens do normalizador); e as propriedades **operacionais** (alertas ainda avaliados; relatório de saúde verde). As regressões de segurança são fáceis de perder, porque um serviço pode funcionar perfeitamente enquanto uma verificação foi desativada em silêncio.

No RLY-03, a verificação de deriva depois do 2.4.1 ainda mostrava o listener de depuração: a função passou, uma propriedade de segurança não.

### 27.4 O que a janela não consegue mostrar

Um canário de uma hora, à noite, mostra o comportamento sob a carga noturna durante uma hora. Ele não diz nada sobre o pico de demanda da manhã, as execuções semanais de relatórios (Capítulo 1), os relatórios de fim de mês ou os tipos raros de mensagem. Estenda a janela pelos períodos que importam ou declare a lacuna e observe esses períodos de perto depois da promoção.

O canário do relayd 2.4.1 rodou durante uma hora noturna, por isso a sua queda de 0,0010 na razão de aceitação foi registrada como item em aberto para o pico da manhã.

As execuções semanais de relatórios nos dias 6 e 7, com cerca de 62 % de CPU, são outro período que uma hora à noite não consegue mostrar.

### 27.5 Exemplo resolvido: relayd 2.4.1 (sintético)

As pré-verificações passam: mudança aprovada, sala de controle informada, configuração com backup, pacote de rollback preparado, assinatura do pacote verificada. O canário RLY-03 roda o 2.4.1 durante uma hora, contra o RLY-01 no 2.4.0. Razão de aceitação de 0,9985 contra 0,9994 (uma queda de 0,0010, dentro de 0,002); latência p95 de 41 ms contra 37 ms (dentro de 25 %); nenhuma reinicialização; rejeições por MAC inalteradas. Decisão: promover para o RLY-02, depois para o RLY-01. A validação pós-implantação no RLY-03 injeta uma mensagem de teste com MAC errado (rejeitada, como esperado) e executa a verificação de deriva — que ainda mostra o listener de depuração do Capítulo 22, um lembrete de que a implantação não corrigiu a deriva de configuração e não deve ser relatada como se tivesse corrigido. A queda na razão de aceitação, embora dentro dos critérios, é registrada como item em aberto a conferir no pico da manhã.

### 27.6 Atividade prática: decisão do canário

**Laboratório 27** (salve como `lab27.py`, execute com `python3 lab27.py`):

```python
# Lab 27 - pre- and post-deployment validation with a canary and a rollback rule (offline, standard library only)
# Synthetic: relayd 2.4.1 rolled to rly-03 first (canary), compared with rly-01 still on 2.4.0 for one hour.
checks_pre = {"backup of config taken": True, "rollback package staged": True, "change ticket approved": True,
              "operations told (control room)": True, "maintenance window open": True, "signature of package verified": True}
canary = {"msgs_in": 7200, "msgs_accepted": 7189, "mac_rejects": 0, "p95_latency_ms": 41, "cpu_p95": 38, "restarts": 0}
control = {"msgs_in": 7200, "msgs_accepted": 7196, "mac_rejects": 0, "p95_latency_ms": 37, "cpu_p95": 36, "restarts": 0}
limits = {"accept_ratio_drop": 0.002, "latency_ratio": 1.25, "restarts": 0}
print("pre-checks:", "PASS" if all(checks_pre.values()) else "FAIL " + str([k for k, v in checks_pre.items() if not v]))
ra, rc = canary["msgs_accepted"] / canary["msgs_in"], control["msgs_accepted"] / control["msgs_in"]
results = {
  "acceptance ratio": (rc - ra <= limits["accept_ratio_drop"], f"{ra:.4f} vs {rc:.4f} (drop {rc-ra:.4f})"),
  "p95 latency": (canary["p95_latency_ms"] <= control["p95_latency_ms"] * limits["latency_ratio"], f"{canary['p95_latency_ms']} vs {control['p95_latency_ms']} ms"),
  "restarts": (canary["restarts"] <= limits["restarts"], str(canary["restarts"])),
  "MAC rejects unchanged": (canary["mac_rejects"] == control["mac_rejects"], str(canary["mac_rejects"])),
}
for k, (ok, detail) in results.items(): print(f"  {k:<22} {'pass' if ok else 'FAIL'}  {detail}")
print("decision:", "promote to rly-02, then rly-01" if all(ok for ok, _ in results.values()) else "ROLL BACK canary and open problem record")
# What the canary cannot show: a 1-hour window at night says nothing about the morning demand peak or month-end reports.
```

Saída esperada (Python 3.13.5):

```text
pre-checks: PASS
  acceptance ratio       pass  0.9985 vs 0.9994 (drop 0.0010)
  p95 latency            pass  41 vs 37 ms
  restarts               pass  0
  MAC rejects unchanged  pass  0
decision: promote to rly-02, then rly-01
```

Confira cada linha contra os critérios fixados antes da janela: razão de aceitação de 0,9985 contra 0,9994, uma queda de 0,0010, dentro dos 0,002 permitidos; latência p95 de 41 ms contra 37 ms, dentro de 25 %; nenhuma reinicialização; rejeições por MAC inalteradas. Tudo passa, então a decisão é promover para o RLY-02, depois para o RLY-01, um host por vez. A queda, embora dentro dos critérios, fica na lista de itens em aberto para o pico da manhã.

Se a queda tivesse sido de 0,0025, a regra fixada de antemão teria exigido o rollback, por menor que a diferença parecesse.

### 27.7 Erros comuns e limites

- Instalar pacotes sem verificar a sua origem.
- Critérios de promoção decididos depois de ver os resultados do canário.
- Validar a função, mas não as propriedades de segurança.
- Uma janela de canário que perde os períodos de carga real.
- Promover todos os hosts restantes de uma vez depois do canário.
- Rollback nunca testado.

A implantação do relayd 2.4.1 evitou cada um: assinatura verificada, critérios fixados antes do canário, uma mensagem com MAC errado injetada depois e promoção de um host por vez.

O item em aberto para o pico da manhã é a forma de tratar o quarto quando a janela não pode ser mais longa.

### Exercícios — capítulo 27

**EX079 — Reprove o canário.** *Objetivo:* aplicar a regra de rollback. *Entradas:* Laboratório 27. *Restrições:* mude apenas os números do canário. *Etapas:* (1) defina a contagem de aceitas do canário como 7170; (2) execute; (3) declare a decisão e as três primeiras ações. *Evidência esperada:* saída e ações. *Rubrica:* 3 = queda de aceitação ≈ 0,0036 reprova no critério de 0,002, decisão de rollback; ações: rollback do canário sob a mudança, preservar os logs do canário e os motivos de rejeição, abrir registro de problema e informar a sala de controle; 2 = decisão certa, ações rasas; 1 = não executado; 0 = nada.

**EX080 — Conjunto de validação de segurança.** *Objetivo:* especificar as verificações de segurança pós-implantação. *Entradas:* Capítulo 27 ("Validação depois da implantação"). *Restrições:* cinco verificações, cada uma com o resultado esperado. *Etapas:* liste-as. *Evidência esperada:* tabela. *Rubrica:* 3 = teste com MAC errado rejeitado, teste de replay rejeitado, verificação de deriva sem novos listeners, contagem de não interpretados do normalizador inalterada, serviço rodando com conta sem privilégios, teste de alerta ainda dispara; 2 = quatro; 1 = só função; 0 = nada.

**EX081 — Estenda a janela.** *Objetivo:* projetar uma janela de canário que cubra a carga real. *Entradas:* execuções semanais de relatórios nos dias 6–7 (Capítulo 1), pico da manhã das 06:00 às 09:00. *Restrições:* a mudança precisa terminar em dez dias. *Etapas:* proponha a(s) janela(s), os pontos de promoção e os critérios conferidos em cada um. *Evidência esperada:* cronograma. *Rubrica:* 3 = canário cobrindo pelo menos um pico da manhã e uma execução de relatórios antes da promoção, com os critérios avaliados em cada um, depois promoção escalonada dentro dos dez dias; registra a prontidão para rollback durante todo o tempo; 2 = cobre um; 1 = mantém a janela de uma hora; 0 = nada.

### Síntese do capítulo

Implante em etapas. Faça as pré-verificações de aprovações, operação, backups, rollback e da origem do pacote. Use um canário num host contra um controle, com critérios de promoção fixados de antemão; faça o rollback a qualquer falha e promova um host por vez em caso de sucesso. Valide as propriedades funcionais, de segurança e operacionais depois de cada host, e declare com honestidade o que a janela de validação não conseguiu mostrar.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue estudando — capítulo 27 de 30

[← Capítulo 26](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Prática de campo

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- planejar e realizar uma visita a um local operacional remoto com segurança e com o acordo do operador;
- coletar evidências de configuração e de inventário no local sem perturbar o processo;
- trabalhar com a equipe de operação como parceira, respeitando a sua autoridade sobre o processo físico;
- participar de um exercício que teste a integração do serviço com os planos de continuidade.

Grande parte do trabalho de um tecnólogo de serviços críticos acontece longe da mesa: em estações de bombeamento, casas de máquinas, depósitos e salas de equipamentos hospitalares. O trabalho de campo traz riscos físicos, riscos operacionais e riscos de segurança próprios. Este capítulo trata de fazê-lo bem.

### 28.1 Planejar uma visita

Antes de ir à PS-07, combine com a operação de Água: propósito e tarefas; data e hora (evitando o pico de demanda e outros trabalhos planejados); quem da Água estará presente (o trabalho local em equipamentos de controle é feito pelos engenheiros da Água ou com eles); arranjos de acesso (chaves, alarmes, procedimento de trabalho solitário); que equipamento você leva (um laptop limpo, com patches aplicados e dedicado ao trabalho de campo, apenas com as ferramentas necessárias); e o que você vai e não vai tocar. Escreva isso num plano de trabalho curto e obtenha a aprovação como para uma mudança (Capítulo 14).

### 28.2 Safety em primeiro lugar

As regras de safety física nos locais operacionais vêm do operador e da legislação de saúde e segurança do trabalho: espaços confinados, produtos químicos (salas de dosagem de cloro), painéis elétricos, trabalho solitário, clima. Siga a integração do local e as instruções do operador; na dúvida, pare e pergunte. O trabalho de segurança nunca justifica um atalho de safety.

Na PS-07, a sala de dosagem de cloro faz parte do trajeto da visita; o engenheiro da Água conduz e decide onde você pode ficar.

O trabalho solitário numa estação como a PS-09, silenciosa há três semanas, precisa de um arranjo de comunicação periódica com a sala de controle da Água antes da visita, e não depois.

### 28.3 Coleta de evidências no local

As visitas de campo são o momento de verificar o que as fontes remotas não conseguem: a presença física e as etiquetas dos dispositivos (Capítulo 11); as versões de firmware lidas do dispositivo ou da sua exportação de engenharia pelo engenheiro da Água; cabeamento que pode criar caminhos não declarados (um segundo cabo de rede para um modem celular, um laptop deixado conectado); a proteção física do gateway da estação que guarda as chaves HMAC (Capítulo 15); e o estado do buffer local e da hora. Fotografe etiquetas e painéis apenas com permissão e sem capturar senhas ou telas com dados sensíveis. Registre tudo com hora e fonte, como observado / inferido / feito / em aberto.

### 28.4 Mídias removíveis e laptops de campo

O equipamento de campo é um caminho clássico para dentro dos sistemas de controle: pendrives e laptops de manutenção levam malware entre locais e redes. Use mídias dedicadas e verificadas; nunca conecte um dispositivo pessoal; nunca conecte um laptop de campo à rede corporativa e à rede de uma estação ao mesmo tempo; registre o que foi conectado a quê. As metas de desempenho da CISA incluem controles sobre a conexão de dispositivos e mídias não autorizados a redes de TO ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)).

O modem celular da PS-07, instalado pela Kell para suporte remoto e ainda ligado à segunda porta do CLP, mostra o mesmo risco do lado de um fornecedor: uma conexão que ninguém registrou.

### 28.5 Trabalhar com a operação

A equipe de operação tem autoridade sobre o processo e um conhecimento que nenhum documento contém. Pergunte o que ela esperaria ver se a estação estivesse se comportando mal; como a operaria manualmente; o que mudou recentemente. Explique o que você está fazendo em linguagem simples e pare se ela pedir. Muitos dos melhores achados no local vêm de conversas: "às vezes ligamos o laptop do fornecedor naquela porta sobrando" vale mais do que uma varredura.

Na PS-07, o modem foi explicado pelo engenheiro numa frase; nenhuma varredura teria contado a sua história.

### 28.6 Exercícios com os operadores

Um **exercício de mesa** percorre um cenário em discussão; um **exercício funcional** executa algumas ações de verdade, de forma controlada. Para o LANTERN, um exercício anual com a operação de Água testa o gatilho "telemetria não confiável" (Capítulo 21): a FSTS o declara, a sala de controle passa para leituras manuais em estações selecionadas, e os dois lados cronometram cada etapa e registram os problemas. O exercício é planejado com regras de engajamento (Capítulo 23) e condições de parada, e termina com uma revisão sem culpados (Capítulo 25).

As três semanas de silêncio da PS-09 são um bom ponto de partida para um exercício de mesa.

### 28.7 Exemplo resolvido: a visita à PS-07 (sintético)

Você visita a PS-07 com o engenheiro da Água para ler o firmware do CLP (para o aviso do Capítulo 16) e inspecionar o gateway da estação. Achados: o firmware do CLP, lido pelo engenheiro no dispositivo, é o 3.9, como registrado. O gabinete do gateway está destrancado e o seu arquivo de chaves fica num cartão removível — a proteção física é mais fraca do que o projeto supunha. Um modem celular, que não está em nenhum inventário, está conectado à segunda porta do CLP; o engenheiro explica que a Kell o instalou anos atrás para suporte remoto e que ninguém o usa hoje. O relógio da estação está correto. Você não desconecta o modem — isso é uma mudança num local operacional —, mas o registra, fotografa a sua etiqueta com permissão, e o engenheiro abre uma mudança para removê-lo depois que a Água confirmar que nada depende dele. O modem é um conduíte não declarado (Capítulo 2) que nenhum registro de fluxo jamais teria mostrado.

### 28.8 Atividade prática: plano de trabalho de campo

Escreva um plano de trabalho de campo para a visita à PS-09 (discrepâncias do Capítulo 11: firmware não verificado de forma independente, estação silenciosa há três semanas). Inclua todos os elementos de "Planejar uma visita" acima, as notas de safety, as evidências que você pretende coletar, o que você não vai tocar e como os achados serão registrados e encaminhados.

Para a PS-09, a lista de evidências do plano deve incluir o firmware da RTU lido do dispositivo, o relógio da estação contra o do relay e o estado do caminho de NTP, dado o deslocamento de 422 segundos encontrado no Capítulo 20. Liste o que você não vai tocar, como a configuração da RTU e o arquivo de chaves do gateway, e quem abre a mudança se for encontrado um modem como o da PS-07.

### 28.9 Erros comuns e limites

- Visitas sem plano aprovado ou sem o engenheiro da Água.
- Laptops de campo usados para outros trabalhos ou conectados a várias redes.
- Consertar coisas no local sem controle de mudanças.
- Fotografias que capturam senhas ou telas sensíveis.
- Tratar a equipe de operação como obstáculo, e não como parceira.
- Exercícios sem condições de parada.

Desconectar o modem da PS-07 na hora teria sido o terceiro erro, por mais evidente que parecesse a sua falta de uso; a Água confirmou primeiro que nada dependia dele, e o engenheiro abriu a mudança.

O gabinete destrancado do gateway da PS-07 marca um limite da própria visita: você pode registrar que o arquivo de chave HMAC fica em um cartão removível, mas trancar o gabinete ou mover a chave é uma mudança da Água, não sua para fazer no dia.

### Exercícios — capítulo 28

**EX082 — Registre o modem.** *Objetivo:* escrever achados de campo corretamente. *Entradas:* Capítulo 28 ("Exemplo resolvido: a visita à PS-07"). *Restrições:* rótulos observado / inferido / feito / em aberto; nenhuma recomendação de agir sem controle de mudanças. *Etapas:* escreva o registro do achado e diga quais registros precisam ser atualizados. *Evidência esperada:* registro. *Rubrica:* 3 = observado (modem presente, modelo/etiqueta, conectado à porta 2 do CLP, relato do engenheiro), inferido (caminho remoto não declarado, possivelmente ativo), feito (fotografado com permissão, mudança aberta pela Água), em aberto (se está energizado e tem um SIM funcionando, quem detém a conta, data de remoção); inventário, lista de conduítes, registro de fluxos de dados e registro de riscos atualizados; 2 = rótulos misturados; 1 = narrativa; 0 = nada.

**EX083 — Regras do laptop de campo.** *Objetivo:* definir os controles do equipamento de campo. *Entradas:* Capítulo 28 ("Mídias removíveis e laptops de campo"). *Restrições:* seis regras, cada uma com a forma de conferi-la. *Etapas:* escreva-as. *Evidência esperada:* tabela. *Rubrica:* 3 = dispositivo dedicado, com patches e endurecido, sem uso pessoal, nunca com dupla conexão, mídias removíveis verificadas e dedicadas, registro de conexões mantido, dispositivo conferido depois de cada visita; cada uma com uma verificação; 2 = quatro ou cinco; 1 = genéricas; 0 = nada.

**EX084 — Plano de exercício.** *Objetivo:* planejar um exercício funcional. *Entradas:* gatilho "telemetria não confiável" (Capítulo 21). *Restrições:* duas estações; nenhum efeito no abastecimento; uma hora. *Etapas:* escreva objetivos, cenário, participantes, etapas com pontos de cronometragem, condições de parada, notas de safety e como os resultados são registrados. *Evidência esperada:* uma página. *Rubrica:* 3 = objetivos mensuráveis (tempo até declarar, tempo até a primeira leitura manual), cenário realista, autoridade da sala de controle preservada, condições de parada para qualquer preocupação com o processo, safety nos locais, revisão sem culpados agendada; 2 = um elemento fraco; 1 = só exercício de mesa; 0 = nada.

### Síntese do capítulo

O trabalho de campo verifica o que as fontes remotas não conseguem e traz os seus próprios riscos. Planeje as visitas com o operador, siga as regras de safety do local, trabalhe com os engenheiros da operação nos equipamentos de controle e colete evidências sem perturbar o processo nem mudar nada fora do controle de mudanças. Controle rigorosamente os laptops e as mídias de campo. Trate a equipe de operação como parceira e exercite a integração do serviço com os planos de continuidade em exercícios planejados e interrompíveis.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue estudando — capítulo 28 de 30

[← Capítulo 27](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Construção do trabalho de conclusão

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- integrar os componentes construídos ao longo do curso num único serviço monitorado de ponta a ponta;
- injetar falhas de teste seguras e mostrar que o serviço detecta ou rejeita cada uma;
- produzir um **registro de evidências do serviço** que outra pessoa consiga conferir;
- encontrar e explicar um defeito que só aparece quando os componentes são combinados.

Este é o resultado prático do curso: *implementar um serviço de ponta a ponta com controles monitorados*. O Laboratório 29 combina, num único arquivo, a selagem nas estações do Capítulo 15, a validação do Capítulo 3, um historiador num modelo relacional (Capítulo 4), o monitoramento com uma regra de ausência (Capítulo 19) e um registro de evidências com um digest (Capítulos 6 e 20). Ele é pequeno o bastante para ser lido por inteiro; o projeto de conclusão pede que você construa a mesma forma em escala maior.

### 29.1 O que o trabalho de conclusão precisa demonstrar

1. **O caminho dos dados funciona**: as leituras de todas as estações chegam ao historiador, validadas e autenticadas.
2. **Os controles funcionam**: as falhas injetadas — um replay, uma mensagem forjada, um valor fora da faixa e um silêncio de estação — são, cada uma, rejeitadas, colocadas em quarentena ou alertadas.
3. **O monitoramento funciona**: são gerados alertas para cada falha injetada e para nada mais.
4. **As evidências existem**: um registro legível por máquina da execução, com contagens que fecham e um digest, para que mudanças posteriores nele sejam detectáveis.
5. **Os limites estão declarados**: o que a execução não mostra.

### 29.2 A construção

O Laboratório 29 gera duas horas de leituras sintéticas de três estações, com a PS-09 silenciosa do minuto 50 ao 84. Ele injeta quatro testes: um replay de uma mensagem anterior da PS-04, uma mensagem da PS-07 selada com a chave errada e uma leitura de cloro fora da faixa, de 7,5 mg/L, da PS-07, que ocupa o lugar do minuto 20, além do silêncio da PS-09. O relay verifica o MAC, rejeita replays, coloca em quarentena os valores fora da faixa e armazena o resto; o monitoramento acrescenta uma regra de silêncio; o registro de evidências resume a execução.

**Laboratório 29** (salve como `lab29.py`, execute com `python3 lab29.py`):

```python
# Lab 29 - capstone: an end-to-end monitored telemetry service in one file (offline, standard library only)
# Synthetic stations -> authenticated relay -> validated historian (sqlite3) -> monitoring -> evidence record.
import hashlib, hmac, json, random, sqlite3
random.seed(29)
KEY = b"lantern-lab-key-not-real-0001"
LIMITS = {"LEVEL_M": (0.0, 12.0), "CL2_MGL": (0.0, 5.0)}
def seal(m, key=KEY):
    body = json.dumps(m, sort_keys=True, separators=(",", ":"))
    return body + "." + hmac.new(key, body.encode(), hashlib.sha256).hexdigest()
# 1. stations emit one reading per minute for 120 minutes; PS-09 goes silent 50-84; one injected test of each fault
wire, now0 = [], 1_790_000_000
for st, tag, base in (("PS-04", "LEVEL_M", 3.4), ("PS-07", "CL2_MGL", 0.6), ("PS-09", "LEVEL_M", 5.1)):
    for i in range(120):
        if st == "PS-09" and 50 <= i < 85: continue
        if st == "PS-07" and i == 20: continue  # the injected out-of-range test takes this slot
        wire.append((now0 + 60*i, seal({"st": st, "tag": tag, "v": round(base + random.gauss(0, 0.05), 3), "ts": now0 + 60*i, "seq": i})))
wire.append((now0 + 600, wire[3][1]))                                                         # TEST: replay
wire.append((now0 + 900, seal({"st": "PS-07", "tag": "CL2_MGL", "v": 0.6, "ts": now0 + 900, "seq": 999}, key=b"x")))  # TEST: forged
wire.append((now0 + 1200, seal({"st": "PS-07", "tag": "CL2_MGL", "v": 7.5, "ts": now0 + 1200, "seq": 20})))         # TEST: out of range
wire.sort(key=lambda w: w[0])
# 2. relay + historian
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE reading(st TEXT, tag TEXT, v REAL, ts INTEGER, seq INTEGER, PRIMARY KEY(st, seq))")
events, last = [], {}
for t, w in wire:
    body, mac = w.rsplit(".", 1)
    if not hmac.compare_digest(hmac.new(KEY, body.encode(), hashlib.sha256).hexdigest(), mac):
        events.append((t, "mac_reject", "?")); continue
    m = json.loads(body)
    if m["seq"] <= last.get(m["st"], -1):
        events.append((t, "replay_reject", m["st"])); continue
    lo, hi = LIMITS[m["tag"]]
    last[m["st"]] = m["seq"]
    if not lo <= m["v"] <= hi:
        events.append((t, "range_quarantine", m["st"])); continue
    db.execute("INSERT INTO reading VALUES (?,?,?,?,?)", (m["st"], m["tag"], m["v"], m["ts"], m["seq"]))
# 3. monitoring: security events and silence > 15 min
alerts = [(t, kind, st) for t, kind, st in events]
for st, in db.execute("SELECT DISTINCT st FROM reading"):
    ts = [r[0] for r in db.execute("SELECT ts FROM reading WHERE st=? ORDER BY ts", (st,))]
    alerts += [(a + 900, "silence", st) for a, b in zip(ts, ts[1:]) if b - a > 900]
# 4. evidence record
stored = db.execute("SELECT COUNT(*) FROM reading").fetchone()[0]
record = {"period_utc_s": [now0, now0 + 7140], "messages_on_wire": len(wire), "stored": stored,
          "alerts": sorted({(k, s) for _, k, s in alerts}), "injected_tests": 4,
          "injected_tests_detected": len({k for _, k, _ in alerts} & {"replay_reject", "mac_reject", "range_quarantine", "silence"}),
          "alert_count": len(alerts)}
blob = json.dumps(record, sort_keys=True).encode()
print(json.dumps(record, sort_keys=True))
print("evidence sha256:", hashlib.sha256(blob).hexdigest()[:24], "...")
print("PS-07 mean chlorine stored: %.3f mg/L" % db.execute("SELECT AVG(v) FROM reading WHERE st='PS-07'").fetchone()[0])
```

Saída esperada (Python 3.13.5):

```text
{"alert_count": 4, "alerts": [["mac_reject", "?"], ["range_quarantine", "PS-07"], ["replay_reject", "PS-04"], ["silence", "PS-09"]], "injected_tests": 4, "injected_tests_detected": 4, "messages_on_wire": 327, "period_utc_s": [1790000000, 1790007140], "stored": 324}
evidence sha256: aa40e3905d178699f1460e1c ...
PS-07 mean chlorine stored: 0.606 mg/L
```

### 29.3 Ler o registro de evidências

Confira se os números fecham. Mensagens na rede: 120 + 119 + 85 + 3 injetadas = 327. Armazenadas: 324 (todas as leituras genuínas). Não armazenadas: 3 (o replay, a falsificação e a leitura fora da faixa). Alertas: quatro, um de cada tipo, e quatro de quatro testes injetados detectados. O digest permite que qualquer pessoa confirme depois que o registro não foi editado; num serviço real, o registro seria guardado fora do host e o digest escrito no ticket da mudança ou do teste.

Se a contagem de armazenadas fosse 325, uma leitura genuína ficaria sem explicação.

### 29.4 Um defeito que só aparece na combinação

Mude o número de sequência da mensagem fora da faixa injetada de 20 para 1000 — como poderia fazer um gateway de estação defeituoso depois de uma reinicialização — e execute de novo. O resultado muda drasticamente: as leituras armazenadas caem de 324 para 225 e os alertas sobem de 4 para 103. Noventa e nove leituras genuínas da PS-07 são rejeitadas como replays. A causa é que o relay atualiza o seu último número de sequência visto *depois* da autenticação, mas *antes* da verificação de faixa: a mensagem fora da faixa é autêntica, então o seu número de sequência 1000 é registrado, e toda mensagem genuína posterior (sequência 21 a 119) parece um replay.

Cada componente estava "correto" pelos testes do seu próprio capítulo. O Capítulo 3 alertou contra atualizar o estado de replay antes de todas as outras verificações passarem; o Capítulo 15 colocou a atualização depois da autenticação. A combinação mostra o buraco restante: uma mensagem **autêntica, mas implausível** pode envenenar o estado de replay. As correções incluem: atualizar o estado apenas na aceitação *ou* na quarentena de uma mensagem plausível na sequência (rejeitar saltos de sequência maiores que um limite, digamos 1.000 ou um dia de mensagens, a não ser num modo explícito de ressincronização); alertar sobre saltos grandes; e dar aos operadores um procedimento de ressincronização revisado. É exatamente por isso que o trabalho de conclusão testa o serviço integrado, e não apenas as suas partes.

### 29.5 Construir o trabalho de conclusão real

A versão de projeto do trabalho de conclusão, feita em equipe (Capítulo 25), constrói a mesma forma com componentes reais num laboratório: três máquinas virtuais de relay, um banco de dados do historiador, encaminhamento de logs para um coletor, o normalizador, três regras de monitoramento mais o automonitoramento, configuração como código com uma verificação de deriva, um backup e uma restauração cronometrada, runbooks e um pacote de passagem. Use apenas equipamentos de laboratório ou estações simuladas. O entregável é o **registro de evidências do serviço**: para cada requisito de "O que o trabalho de conclusão precisa demonstrar" acima, o teste realizado, a sua data, a saída bruta, o resultado contra uma regra de afirmação declarada de antemão (Capítulo 23) e os itens em aberto.

### 29.6 Erros comuns e limites

- Testar os componentes separadamente e supor que a combinação funciona.
- Registros de evidências cujas contagens não fecham.
- Testes injetados que a equipe projetou para passar.
- Nenhum digest nem cópia das evidências fora do host.
- Omitir a seção "o que isto não mostra": o Laboratório 29 não mostra nada sobre dispositivos de campo reais, o comportamento da operadora, a carga em escala ou atacantes que se adaptam.

O resumo da Equipe A no Capítulo 30 comete o quinto: não declara limite algum.

Uma falsificação injetada construída com a chave real da estação não testaria nada; a equipe precisa projetar testes que possam falhar.

### Exercícios — capítulo 29

**EX085 — Reproduza o defeito.** *Objetivo:* encontrar e explicar um defeito de integração. *Entradas:* Laboratório 29. *Restrições:* mude apenas o número de sequência do teste fora da faixa. *Etapas:* (1) defina-o como 1000 e execute; (2) relate a contagem de armazenadas, a contagem de alertas e quais mensagens foram perdidas; (3) explique a causa em termos da ordem das verificações. *Evidência esperada:* saída e explicação. *Rubrica:* 3 = armazenadas 225, alert_count 103, 99 leituras genuínas da PS-07 rejeitadas como replays, explicação de que o estado foi atualizado por uma mensagem autêntica, mas fora da faixa; 2 = números certos, explicação rasa; 1 = não executado; 0 = nada.

**EX086 — Corrija.** *Objetivo:* corrigir o defeito sem abrir um buraco de replay. *Entradas:* Laboratório 29 com sequência 1000. *Restrições:* apenas a biblioteca padrão; os replays ainda precisam ser rejeitados. *Etapas:* (1) implemente um salto máximo de sequência de 1.000 (rejeitando saltos maiores com um evento distinto `seq_jump_reject`) ou outra correção defensável; (2) execute com a sequência 1000 e com a sequência 20; (3) mostre que o teste de replay continua rejeitado nos dois casos. *Evidência esperada:* código e as duas saídas. *Rubrica:* 3 = o salto de 981 (19→1000) fica dentro de 1.000 — então o aluno precisa notar que um limite de 1.000 não pega este caso e escolher um limite mais apertado ou baseado no tempo (por exemplo, salto não maior que os minutos decorridos mais uma margem), com as 324 armazenadas restauradas e o replay ainda rejeitado; 2 = a correção funciona para este caso, mas falta o raciocínio sobre o limite; 1 = remove a proteção contra replay; 0 = nada.

**EX087 — Revisão do registro de evidências.** *Objetivo:* conferir um registro como avaliador. *Entradas:* a saída do Laboratório 29 com a sequência 20. *Restrições:* verificações apenas a partir do registro e do código do laboratório. *Etapas:* (1) verifique se as contagens fecham; (2) recalcule o digest a partir do JSON impresso e compare os seus primeiros 24 caracteres; (3) liste três limites que o registro deveria declarar. *Evidência esperada:* cálculos e lista. *Rubrica:* 3 = 327 = 324 + 3 confirmado; digest recalculado aplicando o hash à string JSON exata; limites como dados sintéticos, sem dispositivos de campo nem operadora, execução única, sem adversário adaptativo, sem carga em escala; 2 = duas partes; 1 = uma; 0 = nada.

### Síntese do capítulo

O trabalho de conclusão integra o curso num único serviço monitorado e o comprova com testes injetados e um registro de evidências conferível. As contagens precisam fechar, o registro precisa estar protegido por um digest e guardado fora do host, e os seus limites precisam estar declarados. Os testes de integração encontram defeitos que os testes de componentes perdem: aqui, uma mensagem autêntica, mas implausível, envenenou o estado de replay, um buraco visível apenas quando a validação, a autenticação e a ordenação se encontraram.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue estudando — capítulo 29 de 30

[← Capítulo 28](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Avaliação do trabalho de conclusão

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você deve ser capaz de:

- apresentar um projeto de integração para **revisão de projeto**, defendendo as escolhas contra as propriedades de projeto e os riscos;
- montar e apresentar **evidências operacionais** de que os controles funcionam, com regras de afirmação e limites;
- avaliar os seus próprios trabalhos de conclusão e os de outras pessoas contra uma rubrica explícita;
- planejar a prática contínua que mantém um serviço — e as suas competências — atualizados.

O plano de avaliação do curso tem três partes: um **projeto de integração** (Capítulo 29), **evidências operacionais** (o registro de evidências e os resultados dos testes ao longo do tempo) e uma **revisão de projeto**. Este capítulo explica como cada uma é avaliada e fecha o livro olhando para trás, para o método que ele ensinou.

### 30.1 A revisão de projeto

Uma revisão de projeto é uma conversa estruturada em que os revisores testam se o serviço cumpre os seus requisitos e preserva as suas propriedades principais. Prepare: a arquitetura com zonas, conduítes e caminhos de gerenciamento; a propriedade da direção da confiança e como cada mudança a preserva (Capítulo 8); os principais cenários de risco e o conjunto de controles de cada um (Capítulos 13 e 18); o registro de fluxos de dados (Capítulo 12); os riscos aceitos com responsáveis. Os revisores farão perguntas do tipo "o que acontece se…?": se o relay for comprometido; se uma chave vazar; se a operadora falhar; se a fonte da verdade da automação estiver errada; se a pessoa que o construiu sair. Responda com o projeto e as evidências, e diga "não testamos isso" quando for verdade — uma lacuna honesta pontua melhor do que um palpite confiante.

### 30.2 Evidências operacionais

As evidências operacionais são o registro do serviço em funcionamento: relatórios de saúde ao longo de semanas, alertas e o seu tratamento, testes de controles com resultados contra regras de afirmação (Capítulo 23), testes de restauração, revisões de acesso, relatórios de deriva, registros de problemas e revisões sem culpados com as suas mudanças. Os avaliadores procuram: evidências **datadas e com fonte**; **contagens que fecham**; regras de afirmação declaradas **antes** dos resultados; o "ainda não demonstrado" tratado com honestidade; e **limites** declarados (dados sintéticos, equipamentos de laboratório, períodos curtos).

O resumo da Equipe B neste capítulo é o modelo: contagens, um digest, uma regra de afirmação e uma lacuna declarada.

### 30.3 Rubrica de avaliação

| Critério | 3 — forte | 2 — adequado | 1 — fraco | 0 — ausente |
|---|---|---|---|---|
| Função de ponta a ponta | Todos os requisitos do Capítulo 29 ("O que o trabalho de conclusão precisa demonstrar") demonstrados com evidências brutas | Um requisito com evidência rasa | Função afirmada, não mostrada | Não funciona |
| Controles e monitoramento | Cada cenário principal tem controles de prevenção/detecção/recuperação testados contra regras de afirmação; automonitoramento presente | Lacunas num cenário ou sem automonitoramento | Controles configurados, mas não testados | Nenhum |
| Propriedades de projeto | Direção da confiança e independência das camadas preservadas e argumentadas; caminhos de gerenciamento mostrados | Uma propriedade fracamente argumentada | Só o diagrama | Nenhuma |
| Operabilidade e passagem | Runbooks testados por outras pessoas; evidências de saúde; passagem com itens em aberto | Runbooks não testados por outras pessoas | Só documentos | Nenhuma |
| Qualidade das evidências | Datadas, com fonte, fecham, com digest, limites declarados | Uma fraqueza | Várias fraquezas | Nenhuma |
| Honestidade sobre os limites | Lacunas e "ainda não demonstrado" declarados claramente, com planos | Declarados, mas sem planos | Lacunas escondidas | — |
| Safety e ética | Todo o trabalho prático dentro da autorização; nenhum sistema real tocado | — | Pequeno deslize | Atividade não autorizada (reprova no trabalho de conclusão) |

### 30.4 Falhas comuns nos trabalhos de conclusão

Os trabalhos de conclusão que se saem pior raramente são os menos técnicos. São os que apresentam configuração como evidência, escondem um teste que falhou, escolhem as regras de afirmação depois dos resultados, testam só componentes ou descrevem um projeto com o qual as evidências não batem. Os que se saem melhor costumam ser modestos no escopo e exatos nas evidências.

A Equipe A, "totalmente protegido… todos os testes passaram", mostra as duas primeiras falhas.

A Equipe B, ao contrário, relata os testes extras da Regra C, os 4 de 6 da FIM e um comprometimento de chave não testado.

### 30.5 Exemplo resolvido: dois resumos de trabalho de conclusão (sintético)

Equipe A: "O LANTERN está totalmente protegido com HMAC, validação, monitoramento e backups. Todos os testes passaram." Equipe B: "Quatro de quatro falhas injetadas foram detectadas na execução final (digest do registro aa40e3905d17…). A Regra C só cumpriu a sua regra de afirmação depois de testes adicionais (12/12 depois de mais quatro sucessos, limite inferior 0,76); a detecção da FIM ainda não está demonstrada (4/6, verificações diárias lentas demais — mudança aberta). Encontramos e corrigimos um defeito de estado de replay durante a integração (Capítulo 29). A restauração do historiador cumpriu o seu RTO de 4 horas em 9 de 10 exercícios; a falha foi uma lacuna no runbook, corrigida e testada de novo. Não testamos o comprometimento de chaves nem a falha da operadora em escala." O resumo da Equipe B pontua mais em todos os critérios, exceto talvez na confiança — e a confiança não é um critério.

### 30.6 Olhando para trás: o método

O curso ensinou um único método, aplicado trinta vezes: saber o que precisa continuar verdadeiro sobre o serviço; construí-lo para que continue verdadeiro; conferir que continua, com evidências que outra pessoa consiga verificar; perceber rapidamente quando deixa de ser; responder sem destruir evidências; e passá-lo adiante para que outros possam fazer o mesmo. O vocabulário muda com o setor — cloro e bombas na água, bibliotecas de medicamentos num hospital, quadros de horários num depósito —, mas o método se transfere.

A PS-09 percorreu o método inteiro uma vez: silenciosa, reconciliada, alertada, explicada pelo seu relógio.

### 30.7 Prática contínua

Os serviços e as ameaças mudam; as normas também. Mantenha um plano curto de prática contínua: releia as principais normas em que você se apoia quando forem revisadas (NIST CSF 2.0, SP 800-82, os CISA CPGs, as orientações setoriais da sua jurisdição); acompanhe os avisos dos produtos do seu inventário; participe de exercícios; revise um relatório público de incidente por mês em busca de premissas que falharam (Capítulo 5); e busque revisão do seu próprio trabalho. O próximo curso na trilha de estudos, o bacharelado em Cibersegurança, amplia os fundamentos por trás de grande parte do que este livro aplicou.

### 30.8 Atividade prática: autoavaliação

Pontue o seu trabalho de conclusão contra a rubrica de avaliação acima antes que o seu avaliador o faça. Para cada critério abaixo de 3, escreva que evidência o elevaria e quando você poderia produzi-la.

Use o resumo da Equipe B como o padrão das evidências que cada nota exige. Se, no seu registro, a Regra C só cumpriu a regra de afirmação depois de testes extras, diga isso e dê as contagens, como a Equipe B fez com 12 de 12 e limite inferior de 0,76. Se a FIM ainda não estiver demonstrada no seu registro, pontue esse critério com honestidade e nomeie a mudança que o elevaria, como verificações de integridade mais frequentes nos arquivos críticos, com uma data para o novo teste. Uma autoavaliação que difere da do avaliador em mais de um ponto em qualquer critério geralmente indica evidências ausentes, e não um trabalho fraco.

### Exercícios — capítulo 30

**EX088 — Responda aos revisores.** *Objetivo:* defender um projeto com honestidade. *Entradas:* perguntas: (a) "O que acontece se a chave HMAC do relay vazar?"; (b) "E se a pessoa que construiu a automação sair?"; (c) "E se a BayTel ficar fora do ar por um dia?" *Restrições:* responda a partir do projeto e das evidências deste livro; diga onde faltam evidências. *Etapas:* responda a cada uma em 100–150 palavras. *Evidência esperada:* três respostas. *Rubrica:* 3 = (a) chaves por estação limitam o impacto; a detecção por origem inesperada ou anomalias de sequência é fraca — admite a lacuna; runbook de rotação testado; etapas de revogação; (b) revisão, rodízio de papéis, runbooks, pipeline protegido, passagem — com evidências de acompanhamento; (c) as estações guardam 24 h em buffer, alertas de silêncio, gatilho de leituras manuais, folga para o envio do acúmulo — e declara se uma interrupção de um dia já foi exercitada; 2 = uma resposta fraca; 1 = confiante sem evidências; 0 = nada.

**EX089 — Avalie a Equipe A e a Equipe B.** *Objetivo:* aplicar a rubrica. *Entradas:* os resumos do Capítulo 30 ("Exemplo resolvido: dois resumos de trabalho de conclusão"). *Restrições:* pontue apenas o que o resumo mostra. *Etapas:* pontue as duas em cada critério e justifique. *Evidência esperada:* tabela. *Rubrica:* 3 = Equipe A baixa em qualidade das evidências e honestidade (só afirmações), desconhecida nos outros; Equipe B alta em qualidade das evidências e honestidade, de adequada a forte em controles, com lacunas declaradas; o avaliador registra que evidências adicionais são necessárias para cada uma; 2 = notas defensáveis, justificativa rasa; 1 = notas pela confiança do tom; 0 = nada.

**EX090 — Plano de prática contínua.** *Objetivo:* planejar manter-se atualizado. *Entradas:* os produtos do seu inventário e as orientações setoriais da sua jurisdição. *Restrições:* uma página; atividades mensais, trimestrais e anuais; fontes nomeadas com versões. *Etapas:* escreva o plano. *Evidência esperada:* plano. *Rubrica:* 3 = fontes e versões específicas (por exemplo, NIST CSF 2.0, SP 800-82 Rev. 3, CISA CPGs ou NCSC CAF), assinaturas de avisos para os produtos do inventário, leitura mensal de relatórios de incidentes, participação trimestral em exercícios, revisão anual das normas, revisão por pares; carga de trabalho realista; 2 = fontes genéricas; 1 = intenção vaga; 0 = nada.

### Síntese do capítulo

O trabalho de conclusão é avaliado pela revisão de projeto, pelas evidências operacionais e pelo projeto de integração. Os revisores recompensam projetos que preservam as suas propriedades principais, controles testados contra regras de afirmação declaradas de antemão, evidências datadas, com fonte, consistentes e protegidas, e honestidade sobre o que não foi demonstrado. O método do curso — saber o que precisa continuar verdadeiro, construir para isso, conferir, perceber a falha, responder com cuidado, passar adiante — se transfere entre setores e precisa ser mantido atualizado pela prática contínua.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue estudando — capítulo 30 de 30

[← Capítulo 29](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável e explica o que a rubrica recompensa. Uma resposta diferente pode receber a nota máxima quando atende ao mesmo padrão de evidências, escopo e honestidade sobre os limites. Os resultados numéricos vêm dos laboratórios offline deste livro, executados com o Python 3.13.5 e apenas a biblioteca padrão; se a sua saída for diferente, confira primeiro a versão do Python e se você alterou os dados sintéticos. Todos os números descrevem dados sintéticos; nunca os apresente como achados sobre operadores reais.

### Capítulo 1: EX001–EX003

**EX001 — Prazo de reposição versus tempo de aviso.** Espaço livre necessário quando o pedido é aberto = (30 dias de prazo + 7 dias de reserva) × 1,91 GB/dia ≈ 70,7 GB. Abra o pedido quando o espaço usado chegar a cerca de 200 − 70,7 ≈ 129 GB, ou seja, por volta de 65 % de ocupação. O RLY-01 está em 120,9 GB e chegará a 129 GB em cerca de (129,3 − 120,9) / 1,91 ≈ 4,4 dias. O alarme de 85 % dispara com apenas cerca de 15,7 dias de crescimento restantes antes de encher — metade do prazo de compra —, então ele é tardio demais como *gatilho de compra*; mantenha-o como alarme operacional e acrescente um limiar de 65 % para "abrir pedido de capacidade". A nota máxima também observa que corrigir a retenção (EX002) pode tornar a compra desnecessária.

**EX002 — Explique o crescimento.** 120,9 GB ÷ 1,91 GB/dia ≈ 63 dias de dados, mais que o dobro da retenção de 30 dias. *Observado:* uso do disco e taxa de crescimento. *Inferido:* dados com mais de 30 dias estão sendo mantidos. Causas plausíveis: (a) a rotação de logs roda, mas os arquivos antigos não são apagados (contagem de rotação alta demais, ou compressão sem exclusão); (b) o buffer de envio do relay guardou mensagens durante uma antiga interrupção do historiador e nunca as expurgou; (c) um segundo fluxo de log (depuração ou auditoria) está fora da política de rotação. Verificações (somente leitura): listar os arquivos mais antigos por diretório e data de modificação; comparar a configuração de rotação com a política; conferir o tamanho do diretório do buffer e a sua entrada mais antiga. *Em aberto:* causa confirmada — E. Strand, até sexta-feira.

**EX003 — Lista de verificação de falhas silenciosas.** Linhas de exemplo: (1) disco enchendo — % usado e previsão de dias até encher — aviso em 65 %/alarme em 85 % — plantão de plataforma — aumentar a capacidade ou corrigir a retenção; (2) rotação de logs parada — idade do arquivo de log ativo mais antigo — > 2 dias — plantão de plataforma — corrigir a rotação; (3) expiração de certificados — dias até a expiração dos certificados do relay e do historiador — < 30 dias — equipe de plataforma — renovar sob mudança padrão; (4) deriva do relógio — deslocamento em relação ao NTP interno — aviso > 1 s, alarme > 2 s — plantão — conferir a fonte de tempo; (5) tarefa agendada que falhou — resultado da tarefa de backup e idade do teste de restauração — qualquer falha, ou teste de restauração > 90 dias — dono do serviço — executar de novo e investigar. A nota máxima exige limiares mensuráveis, com tempo de aviso e um leitor nomeado.

### Capítulo 2: EX004–EX006

**EX004 — Classifique e priorize.** (1) corporativo 10.40.3.7 → PS-04 tcp/502: observado, mas não declarado; primeiro, porque alcança o processo físico com um protocolo sem autenticação — contatar a operação de Água e o dono da estação de trabalho. (2) RTU da PS-09 silenciosa: declarada, mas não observada; prioridade operacional — a Água pode estar operando às cegas — contatar a sala de controle da Água no mesmo dia. (3) externo 192.0.2.44 → relay tcp/22: observado, mas não declarado; SSH exposto além do host de salto — dono da plataforma da FSTS; conferir se algum login teve sucesso (Capítulo 17). (4) relay → externo tcp/443: observado, mas não declarado; provavelmente tráfego de atualização, a menor consequência — dono da plataforma. Ordenar pela contagem de conversas poria erradamente em primeiro lugar o tráfego entre relay e historiador ou os fluxos das estações; quem decide é a consequência.

**EX005 — Atualize a declaração.** Atualizações do relay: ou acrescentar um conduíte estreito (relay → espelho de atualização nomeado ou, melhor, um servidor de atualização interno da FSTS, tcp/443, propósito "atualizações do SO", responsável Plataforma da FSTS, revisão anual) ou remover o acesso direto à internet e apontar o relay para o servidor de atualização interno; a segunda opção é a preferida, porque o relay não deveria alcançar a internet. Laptop do engenheiro: remover o caminho corporativo → estação; declarar um caminho de engenharia a partir do host de salto de gerenciamento (MFA, registro de sessões) até a interface de engenharia da estação, responsável a engenharia da Água, propósito "configuração do CLP", habilitado apenas para trabalho aprovado. A nota máxima se recusa a "permitir o que foi observado" e põe responsáveis e propósitos em cada nova entrada.

**EX006 — Estenda o laboratório.** Uma mudança mínima: no laço, depois de calcular `key`, acrescente `if "unknown" in key[:2]: print(f"UNKNOWN ZONE {s:>12} -> {d:<12} {p}/{port} n={count}"); continue`. Com a linha acrescentada `10.50.1.9,10.30.0.5,tcp,443,5`, a nova saída inclui `UNKNOWN ZONE    10.50.1.9 -> 10.30.0.5    tcp/443 n=5`. A nota máxima explica que "zona desconhecida" significa que o inventário ou o mapa de zonas está incompleto — uma constatação diferente de um caminho não declarado entre zonas conhecidas.

### Capítulo 3: EX007–EX009

**EX007 — Preveja, depois execute.** Saída para as três linhas acrescentadas: `inf` → `reject: not finite`; `12.0` → `accept` (a verificação de faixa é inclusiva); `-0.0` → `accept` (−0,0 é igual a 0,0, então está dentro da faixa, e a sequência 104 é maior que 103). As contagens passam a `{'accept': 5, 'reject': 7, 'quarantine': 2}`. Um bom comentário observa que −0,0 é inofensivo, mas deveria ser normalizado para 0,0 antes do armazenamento, para que comparações e exibições posteriores sejam consistentes, e que um nível exatamente no limite de 12,0 m poderia, ele próprio, merecer revisão se 12,0 for a altura de transbordamento.

**EX008 — Projeto da quarentena.** As mensagens em quarentena vão para uma tabela separada, com a mensagem bruta, o motivo e a hora, mantidas por 90 dias (mais, se fizerem parte de um incidente). O monitoramento da FSTS as revisa em até uma hora útil durante o dia e, à noite, pelo plantão, quando a regra abaixo dispara. Escalonamento: duas ou mais leituras implausíveis consecutivas de cloro ou de nível de uma estação, ou qualquer leitura implausível de cloro durante uma janela de mudança de dosagem, dispara uma ligação para a sala de controle da Água. A tela do operador mostra "valor retido — em revisão" com a idade do último valor bom, nunca o último valor bom como se fosse atual. A nota máxima vincula o escalonamento ao processo físico e atribui um responsável a cada etapa.

**EX009 — Falhe fechado.** Com o `except: pass` vazio, um valor não numérico como `abc` deixa `v` sem definição na primeira mensagem (um `NameError`, que pode derrubar o relay — uma negação de serviço) ou, num laço, mantém o valor da mensagem *anterior*, que é então verificado e possivelmente aceito como se pertencesse a esta mensagem. Também não há limite inferior, então valores negativos são aceitos, e `nan` passa porque `nan > hi` é falso. Corrigido: `try: v = float(val) except ValueError: return "reject: not numeric"`; `if not math.isfinite(v): return "reject: not finite"`; `if not lo <= v <= hi: return "quarantine: out of physical range"`; depois, as verificações seguintes; o `return "accept"` final só depois de todas as verificações.

### Capítulo 4: EX010–EX012

**EX010 — Encontre o ativo escondido.** Com `JOIN`, a consulta de criticidade 1 imprime apenas `('Water Ops', 3)` e `('Clinical Eng', 1)`; a linha `('(none)', 1)` desaparece, então o total cai de 5 para 4. A PS09-RTU some porque não tem dono, e uma junção interna mantém apenas as linhas com correspondência. Num relatório gerencial, isso significa que o único ativo crítico que ninguém possui — o mais propenso a ser negligenciado — fica ausente da contagem que deveria mostrar a cobertura.

**EX011 — Acrescente uma restrição e uma tabela.** Esquema: `CREATE TABLE review(asset_id TEXT NOT NULL REFERENCES asset(id), reviewed TEXT NOT NULL, reviewer TEXT NOT NULL, result TEXT NOT NULL CHECK (result IN ('ok','issue','not-reachable')))`, com `PRAGMA foreign_keys = ON` executado antes na conexão. Inserir `('NOPE','2026-10-01','b.lind','ok')` gera `sqlite3.IntegrityError: FOREIGN KEY constraint failed`. Consulta: `SELECT a.id FROM asset a WHERE a.criticality = 1 AND NOT EXISTS (SELECT 1 FROM review r WHERE r.asset_id = a.id AND r.reviewed >= '2026-07-14')` — sem nenhuma revisão inserida, os cinco ativos de criticidade 1 aparecem. A nota máxima percebe que uma junção interna com `review` não teria retornado *nenhum* dos ativos nunca revisados.

**EX012 — Da planilha ao modelo.** Falhas: registro duplicado do CLP da PS-03 com caixa diferente ("PLC"/"plc") — chave primária na etiqueta do ativo; variantes de dono "Water Ops"/"water operations" — chave estrangeira para uma tabela de donos; dono registrado como uma pessoa que saiu — dono como papel, com atualizações de entrada–mudança–saída (Capítulo 7); firmware "?" — `NULL` explícito significando desconhecido, consultado como constatação; formatos de data misturados "Jun 2027"/"30/06/27" — datas ISO 8601; "TBC" num campo de data — `NULL` mais um ticket, nunca texto numa coluna de data. A nota máxima associa cada falha a uma escolha de projeto.

### Capítulo 5: EX013–EX015

**EX013 — Precisão dos termos.** Reescrita: "A RTU da PS-09 é um ativo crítico. A conta remota permanente do fornecedor, sem MFA, é uma vulnerabilidade e, como pode ser alcançada de fora, é uma exposição que um grupo criminoso ou um técnico descuidado do fornecedor (ameaças) poderia usar. A habilitação limitada no tempo, com MFA, é o controle ausente." Correções: a conta não é uma ameaça; a RTU é um ativo, e não um risco; o risco é a probabilidade e a consequência de um dano, e não um objeto; "nenhum controle" deveria nomear o controle específico ausente.

**EX014 — Prevenir, detectar, recuperar.** Prevenir: mudanças na configuração do relay apenas por meio de estado desejado sob controle de versão, com revisão por pares (evidência: configurações de branch protegido e registros de revisão). Detectar: alerta de integridade de arquivos na configuração do relay e a regra de silêncio de estação (evidência: uma mudança de teste injetada e um silêncio de teste produziram, cada um, um alerta dentro da meta — Capítulo 23). Recuperar: configuração versionada com um runbook de rollback testado (evidência: rollback cronometrado num relay de teste). A nota máxima dá evidências testáveis, e não "configurado".

**EX015 — Leitura de relatório de incidente.** Do CISA AA21-042A: o aviso recomendou, entre outras medidas, restringir e proteger o software de acesso remoto, não compartilhar senhas, usar sistemas operacionais atualizados e com suporte e manter os sistemas de controle fora da exposição direta à internet, com firewalls. O relato da WUSF (abril de 2023) registra um ex-funcionário da prefeitura dizendo que o evento provavelmente foi erro de um empregado; isso muda a *atribuição*, e não o valor das lições de higiene, e mostra que os primeiros relatos podem ser revistos. Regras do LANTERN: nenhuma ferramenta de acesso remoto em qualquer host de controle ou de relay, a não ser pelo caminho de salto (Capítulo 8); nenhuma conta de administrador compartilhada (Capítulo 7); toda sessão privilegiada registrada, para que se possa responder depois "o que aconteceu" (Capítulo 17).

### Capítulo 6: EX016–EX018

**EX016 — Revisão de endurecimento.** Vincular o SSH apenas à interface de gerenciamento (mudança normal, porque um erro deixa os administradores trancados do lado de fora); remover o listener de depuração em 0.0.0.0:9000 (mudança normal, depois de preservar as evidências de quem o habilitou — Capítulo 20); desabilitar o RPC na porta 111 (mudança padrão, se houver um procedimento); remover o compilador e o ambiente gráfico (mudança padrão); passar o relay de `root` para uma conta dedicada `relay`, com restrições no sistema de arquivos (mudança normal, com testes). Cada mudança tem um motivo vinculado às Seções 6.1–6.2.

**EX017 — Proteja a linha de base.** Projeto 1: depois de cada mudança aprovada, a linha de base é exportada para um armazenamento de gravação única fora do host (um bucket somente de acréscimo ou um servidor que os administradores do relay não conseguem modificar). Projeto 2: o arquivo da linha de base é assinado com uma chave guardada pela equipe de segurança, e não no relay; a comparação verifica a assinatura primeiro. Um atacante com root no relay pode alterar arquivos e até a cópia local da linha de base, mas não consegue alterar a linha de base fora do host ou assinada sem ser detectado. Como a própria ferramenta de comparação no relay poderia ser subvertida, execute também a comparação a partir de fora (coletar os hashes remotamente ou comparar os arquivos coletados fora do host).

**EX018 — Posicionamento no hipervisor.** Compartilhado: o hardware físico e as suas falhas; os administradores do hipervisor (que, na prática, administram todos os convidados); a rede de gerenciamento; o armazenamento e os snapshots; o calendário de patches. Condições para aceitar: gerenciamento do hipervisor na sua própria zona, alcançável apenas a partir do host de salto; um pequeno grupo de administradores do hipervisor, com MFA e registro; redes virtuais separadas, sem ponte entre os convidados voltados para as estações e os voltados para a rede corporativa; folga de capacidade documentada para todos os convidados no pico; plano testado para a perda do host (o que falha para a água *e* para o hospital ao mesmo tempo). Risco residual: um comprometimento ou uma falha do hipervisor afeta dois setores; aceito em conjunto pelos donos dos serviços da Água e do hospital. Rejeitar de pronto, sem condições, recebe menos crédito do que isso.

### Capítulo 7: EX019–EX021

**EX019 — Priorize as constatações.** Hoje: `c.mendes` usada depois da saída — (1) preservar os logs de autenticação e de sessão do HIST-01, (2) desabilitar a conta e abrir um incidente; `vendor-kell`, administrador permanente sem MFA — (1) confirmar com a Água que nenhum trabalho da Kell está em andamento, (2) desabilitar a conta e passar à habilitação limitada no tempo. Nesta semana: `d.reyes` (remover o administrador, confirmar a necessidade com a Engenharia Clínica), `opsuser` (planejar a migração para contas pessoais ou para um cofre sem quebrar a operação de emergência), `f.ito` (identificar; desabilitar se ninguém responder por ela). Neste trimestre: correções de processo para os fluxos de entradas e saídas de pessoal. A nota máxima põe a preservação antes da desabilitação.

**EX020 — Acesso de fornecedor limitado no tempo.** (1) A Kell abre um ticket ou liga para o plantão da FSTS com uma referência de serviço; (2) o plantão confere o serviço com o gerente de turno da Água; (3) o plantão habilita a `vendor-kell` pela ferramenta de acesso por uma janela fixa (por exemplo, quatro horas) — meta de menos de 15 minutos desde o pedido; (4) a Kell se autentica com MFA pelo host de salto; (5) a sessão é gravada ou registrada; (6) um alerta dispara para qualquer login da Kell fora de uma janela habilitada; (7) a conta expira automaticamente; (8) no dia útil seguinte, a Segurança da FSTS revisa o log da sessão contra o serviço. Evidências mantidas: ticket, aprovação, logs de habilitação e de expiração, gravação da sessão, nota de revisão.

**EX021 — Estenda a revisão.** Acrescente depois do laço: construa `admins = {}`, mapeando cada pessoa para o conjunto de sistemas em que é administradora, e então sinalize quem tiver tanto `RLY-01` quanto `HIST-01`. Com a nova conta `("b.lind", "HIST-01", "admin", "2026-10-12", True, "person")`, a saída acrescenta `b.lind       HIST-01  role admin not justified for FSTS Security` e a constatação de concentração `b.lind admin on both RLY-01 and HIST-01`. Nenhuma outra pessoa é sinalizada (e.strand e d.reyes são administradores de um sistema cada). A nota máxima percebe a constatação "não justificado": a tabela de necessidades não dá à Segurança da FSTS nenhum papel no HIST-01.

### Capítulo 8: EX022–EX024

**EX022 — Confira a direção da confiança.** (a) Reprojetar: uma allowlist de estações puxada do historiador torna um sistema da zona corporativa a fonte da configuração de segurança do relay; em vez disso, a allowlist vem do controle de versão, por meio de mudança (Capítulo 14), implantada nos relays. (b) Reprojetar com cuidado: o bloqueio automático no firewall da estação poderia cortar a telemetria legítima ou o acesso de engenharia durante um incidente; ele precisa do acordo da Água, de um modo de falha seguro e de escopo limitado ao tráfego que não é do processo, ou a alertas mais uma confirmação humana com um clique. (c) Aceitável apenas com um novo conduíte declarado, uma entrada no registro de fluxos de dados (Capítulo 12), termos de contrato e de retenção com a Halden, criptografia e monitoramento — e a data de término do piloto.

**EX023 — Independência das camadas.** A dependência comum é uma pessoa e um conjunto de credenciais: firewall, administração do relay, custódia das chaves e monitoramento ficam todos com E. Strand. Um único evento — o comprometimento da conta de E. Strand, ou um erro bem-intencionado — pode desativar todas as camadas e a detecção disso. Mudanças: separar os papéis (a equipe de rede é dona do firewall; a equipe de plataforma, do relay; a equipe de segurança, das regras de monitoramento e da sua revisão) e guardar as chaves num armazenamento com custodiantes separados, para que os administradores do relay não consigam lê-las ou substituí-las sem que se perceba.

**EX024 — Modo degradado.** Operadores: as telas do historiador mostram a idade dos valores aumentando e uma faixa de "relay offline", e não valores congelados apresentados como atuais. Dados: as estações guardam em buffer local (24 h). Alertas: os alertas de saúde do relay e de silêncio de estação chegam ao plantão da FSTS e à sala de controle da Água em 15–20 minutos. Retorno: as estações enviam o acúmulo; o relay precisa de folga para a rajada (Capítulo 1); as mensagens acumuladas são mais antigas que a janela de tempo ao vivo e precisam ser aceitas por um caminho explícito de acúmulo que ainda confira o MAC e a sequência (Capítulo 15), para que a verificação de replay não as rejeite por engano — e não vire um buraco de replay.

### Capítulo 9: EX025–EX027

**EX025 — Reescreva a linha do relatório.** "Correções de fornecedores instaladas: TI corporativa 12/12 (mediana de 5,5 dias); relay/historiador 6/8 (mediana de 18,5 dias, 2 em aberto); controladores das estações 3/8 (mediana de 95 dias, 5 ainda em aberto, todas sob controles compensatórios). A mediana agregada de 9 dias não é relatada porque mistura grupos e exclui as correções em aberto." Deixados de fora: os valores de p90 e as médias (disponíveis no apêndice do relatório), para manter a manchete curta.

**EX026 — Envelheça os itens em aberto.** Valores das estações: instaladas 64, 95, 140; idades das em aberto 20, 45, 70, 130, 200. Ordenados: 20, 45, 64, 70, 95, 130, 140, 200; mediana = (70 + 95) / 2 = 82,5 dias. Isto é um limite inferior, porque a latência final de cada correção em aberto será de pelo menos a sua idade atual; a mediana verdadeira só pode subir à medida que as correções em aberto envelhecem. Ela difere da mediana apenas das instaladas (95 dias) — aqui, menor, porque várias correções em aberto são recentes —, o que mostra por que as duas precisam ser relatadas juntas, em vez de se escolher uma.

**EX027 — Quantos exercícios?** Calculando o limite inferior de Wilson para n sucessos em n: 15/15 dá cerca de 0,796, 16/16 cerca de 0,806. Então são necessários 16 exercícios consecutivos bem-sucedidos — 16 meses, a um exercício por mês. Alternativas: fazer restaurações parciais menores e mais frequentes (uma tabela ou um dia de dados por semana), automatizar os testes de restauração para uma instância de rascunho e manter o exercício completo trimestral; relatar cada tipo separadamente, para que a afirmação corresponda ao teste.

### Capítulo 10: EX028–EX030

**EX028 — Consequência em pessoas e tempo.** Premissas rotuladas como sintéticas. Água: "Cerca de 41.000 pessoas não perdem nada de imediato — a telemetria continua —, mas a FSTS não consegue mudar os relays durante a interrupção; isso só se torna danoso se ocorrer uma falha no relay antes do reparo." Hospital: "Os pacientes com bombas de infusão na Ala 3 (cerca de 30 por vez) podem receber terapia a partir de uma biblioteca de medicamentos desatualizada se a atualização das 06:00 for perdida; danoso a partir das 06:00, porque a atualização corrige um limite de dosagem." Garagem: "Os passageiros veem um quadro de horários desatualizado nos totens a partir do primeiro ônibus da manhã; incômodo, não danoso." O prazo de segurança do paciente das 06:00, no hospital, é o mais cedo.

**EX029 — Mapa de dependências compartilhadas.** Host de salto, SIEM, diretório de identidades, sistema de backup: interdependências cibernéticas e lógicas entre os três clientes. BayTel: uma operadora comum, cibernética/física, para a telemetria da água e a internet do hospital; geográfica, se os dois usam a mesma central. Equipe da FSTS: lógica. Maior falha única: o comprometimento do diretório de identidades (ou de uma conta privilegiada da FSTS nele), que dá acesso aos sistemas de todos os clientes. Mudança: camadas privilegiadas separadas por cliente, com contas de administrador separadas e MFA, para que uma conta comprometida não abranja vários setores; e um segundo caminho de operadora para a telemetria da água.

**EX030 — As evidências que você deve.** Exemplo usando os CISA CPGs (versão consultada e citada): meta de inventário de ativos — evidência: o inventário com as datas da última verificação, relatório mensal de conciliação (Capítulo 11), guardado no sistema de inventário; meta de MFA — evidência: saída da revisão trimestral de acessos com a situação de MFA (Capítulo 7), guardada com o ticket da revisão; meta de coleta de logs — evidência: relatório de atualidade das fontes de log e contagens do normalizador (Capítulos 17 e 19), diário, guardado no SIEM. A nota máxima cita a fonte e a versão e nomeia a frequência e o local.

### Capítulo 11: EX031–EX033

**EX031 — Concilie.** Endereços nos fluxos sem registro no inventário: 10.40.3.7 (uma estação de trabalho corporativa; é também a origem dos fluxos Modbus não declarados — responsável a equipe de desktops da FSTS; registrá-la e encontrar o seu usuário). Ativos do inventário nestas zonas nunca vistos nos fluxos: SW-STN-04 — esperado, porque um switch encaminha tráfego em vez de originá-lo nestes registros de fluxo; verifique-o pelos dados de gerenciamento do switch; PS09-RTU — vista apenas como uma origem declarada com tráfego zero: a estação silenciosa (operação de Água, no mesmo dia). O HIST-01 (10.40.8.20) e os CLPs conciliam. A nota máxima explica por que "não visto" significa coisas diferentes para um switch e para uma RTU.

**EX032 — Controles compensatórios.** (1) Conduíte restrito para que a PS09-RTU só fale com o relay em tcp/502 — evidência: regra de firewall e revisão mensal de fluxos; (2) validação no relay e quarentena por faixa para as tags da PS-09 — evidência: testes no relay no estilo do Laboratório 3; (3) alertas de silêncio de estação e de valor implausível para a PS-09 — evidência: testes injetados (Capítulo 23); (4) RTU reserva na prateleira ou um procedimento de leitura manual testado — evidência: registro do almoxarifado ou registro do exercício; (5) backup da configuração da RTU pela engenharia da Água — evidência: exportação datada. A substituição é responsabilidade do gerente de engenharia da Água, com data-alvo em 14 meses, e os controles terminam quando a substituição for verificada.

**EX033 — Plano de descoberta.** Semanas 1–3: fontes passivas — registros de fluxo dos firewalls do local central e das estações, tabelas MAC/ARP dos switches exportadas pelo engenheiro de rede da Água, exportações de engenharia das configurações dos CLPs/RTUs, registros de compra e de manutenção; montar um inventário preliminar com colunas de "fonte". Semanas 4–12: duas visitas a campo por semana (Capítulo 28) às estações com mais discrepâncias, confirmando os dispositivos físicos e o firmware com o engenheiro da Água. Um método ativo só se justifica se as fontes passivas não conseguirem ver um segmento; nesse caso: acordado com a operação de Água, testado primeiro num dispositivo reserva do mesmo modelo, com taxa limitada, dentro de uma janela aprovada, com um engenheiro no local e uma condição de parada. Cronograma realista: 14 estações, a duas visitas por semana, cabem em sete semanas.

### Capítulo 12: EX034–EX036

**EX034 — Faça a triagem das diferenças.** (1) CLIN-GW → REPORTS, vinculado a pacientes, não registrado: primeira ação — informar o dono dos dados do hospital e combinar a interrupção do fluxo enquanto ele é avaliado; responsável: dono dos dados do hospital, com a Segurança da FSTS. (2) Retenção do DF5 de 400 dias contra 30 na Halden: informar o dono dos dados do hospital; conferir a configuração de retenção da Halden contra o contrato; responsável: dono dos dados do hospital, com o gestor de fornecedores da FSTS. (3) HIST-01 → VENDOR-SUPPORT, em texto claro, não registrado: interromper ou passar para um fluxo criptografado e registrado; responsável: dono dos dados da Água, com a Plataforma da FSTS. Se algum dos dois primeiros precisa ser comunicado fora da FSTS (por exemplo, como violação de dados pessoais) é uma decisão da função de proteção de dados do hospital, e não do tecnólogo.

**EX035 — Escreva uma entrada do registro.** DF7; origem: tarefa de exportação do HIST-01 (não a RTU); destino: endpoint de diagnóstico remoto da Kell; classe de dados: telemetria operacional, apenas a tag LEVEL_M da PS-09, agregados horários; criptografia: TLS 1.3; retenção na Kell: 30 dias, conforme cláusula contratual; propósito: diagnóstico de falhas da RTU durante o período de suporte; responsável: gerente de engenharia da Água; conduíte: novo, declarado, HIST-01 → endpoint da Kell tcp/443; aprovações: dono dos dados da Água, Segurança da FSTS; expiração: 6 meses, renovável depois de revisão. A nota máxima envia os dados a partir de um sistema de nível mais alto, em vez de deixar o fornecedor alcançar a estação.

**EX036 — Estenda a conferência.** Acrescente `APPROVED_PATIENT_DESTS = {"CLIN-GW", "HALDEN-CLOUD"}` e, para cada fluxo observado com classe `patient-linked` cujo destino não esteja nesse conjunto, acrescente o problema "patient-linked data to unapproved destination". Depois de registrar o DF6, a linha CLIN-GW → REPORTS passa a ser `HIGH DF6 CLIN-GW->REPORTS patient-linked data to unapproved destination`, em vez de "unregistered". Explicação: o registro guarda decisões; um fluxo registrado ainda pode ser uma má decisão. Registrar sem revisar faria a conferência passar enquanto os dados de pacientes continuam num sistema corporativo de relatórios usado pela equipe da água.

### Capítulo 13: EX037–EX039

**EX037 — Escreva dois cenários.** BayTel: "Uma falha numa central da BayTel corta os enlaces da operadora de seis estações (PS-08 a PS-13) por oito horas. As estações guardam em buffer local; os operadores perdem as leituras ao vivo da área de abastecimento de cerca de 18.000 pessoas e precisam mandar pessoal para leituras manuais. Controles existentes: buffer nas estações (testado trimestralmente), alertas de silêncio de estação (testados, 8/8), procedimento de leitura manual (exercitado no ano passado). Faixa de consequência 4." Host de salto: "O host de salto da FSTS é comprometido por meio de uma credencial de administrador roubada; o atacante alcança a administração do relay e do gateway do hospital. Consequência: possível falsificação da telemetria para 41.000 pessoas e interrupção do gateway clínico. Controles existentes: MFA (configurado; resistência a phishing não testada), registro de sessões (não testado), alertas de deriva (testados)." Os dois são específicos e nomeiam a situação dos testes.

**EX038 — Produto versus consequência.** "O R3 — o disco do relay enchendo — acontece com mais frequência, então ele pontua mais alto quando multiplicamos o quão provável ele é pelo quão ruim ele é. Mas, se o R3 acontecer, perdemos algumas leituras por algumas horas e conseguimos recuperá-las. O R2 e o R4 podem machucar pessoas: uma dose de cloro errada ou um limite de medicamento errado numa bomba de infusão. Multiplicar trata 'frequente e recuperável' como 'raro e danoso', e não é assim que queremos gastar esforço. Então tratamos primeiro o R2 e o R4. O R3 ainda precisa de ação — e ela é barata: corrigir a falha de retenção e definir um alarme de capacidade mais cedo neste mês."

**EX039 — Do cenário ao trabalho.** Prevenção/redução: (1) acesso da Kell limitado no tempo, com MFA resistente a phishing — responsável Segurança da FSTS — evidência: logs de habilitação e de expiração; (2) registro das sessões remotas do fornecedor — Segurança da FSTS — evidência: revisão amostral das sessões; (3) limites de setpoint de dosagem configurados no CLP da PS-07 — engenharia da Água — evidência: registro de teste de engenharia relido no local. Detecção: (4) alerta do LANTERN para cloro fora da faixa aprovada ou mudando mais rápido que uma taxa definida — monitoramento da FSTS — evidência: leitura de teste injetada; (5) comparação dos valores de setpoint do CLP com uma linha de base aprovada a cada exportação de engenharia — engenharia da Água — evidência: comparação datada.

### Capítulo 14: EX040–EX042

**EX040 — Classifique as mudanças.** (a) Padrão — segue o procedimento da PS-11; aprovada pelo procedimento, registrada. (b) Normal — plano revisado, canário e rollback (Capítulo 27); aprovador: dono do serviço, com a Água informada. (c) Emergência — aprovada pela autoridade de segurança de plantão; revisada no dia útil seguinte. (d) Normal — afeta registros e possivelmente obrigações; aprovador: dono dos dados da Água, com o dono do serviço da FSTS. (e) Normal (tornando-se padrão quando existir um runbook testado) — coordenada com a Água, porque as estações silenciam se as chaves divergirem.

**EX041 — Etapas de verificação.** (1) O log de conexões do relay mostra TLS 1.3 negociado com o HIST-01; (2) o historiador recebe leituras de todas as estações dentro da latência normal de 60 s durante uma hora; (3) as contagens de erros e de rejeições do relay não mudam em relação à hora anterior; (4) a validação de certificados continua aplicada — uma conexão de teste com um host de certificado não confiável falha; (5) a verificação de integridade mostra que só o arquivo de configuração de TLS mudou, sob o número da mudança.

**EX042 — Revise uma mudança de emergência.** Perguntas: por que a rota pelo host de salto falhou? Quem aprovou a regra, e sob qual autoridade de emergência? Quais sistemas foram alcançados por ela durante a janela, e por quem (logs)? A regra ainda está ativa? Decisão: remover a regra sob um registro de mudança; se ela ainda for necessária, restringi-la a um único endereço de administrador por um tempo fixo. Mudança de processo: tornar o host de salto resiliente (segundo host de salto ou um caminho de emergência testado, com registro e alertas) e acrescentar as "regras temporárias", com a sua expiração, ao relatório diário de saúde.

### Capítulo 15: EX043–EX045

**EX043 — Ordem das verificações.** Se apenas a *verificação* de replay for movida para antes da verificação do MAC (com a atualização de estado ainda depois do MAC), a mensagem do atacante com seq 1000000 passa na verificação de replay, falha no MAC e é rejeitada sem atualizar o estado; a seq 3 genuína é então aceita. Se a atualização de estado for movida junto, a mensagem do atacante define a última sequência da PS-04 como 1000000 antes de falhar na autenticação, e a seq 3 genuína é rejeitada como replay — o atacante bloqueou a estação com mensagens não autenticadas. A regra segura: autenticar primeiro e atualizar o estado só depois que todas as verificações passarem.

**EX044 — Chaves por estação.** Interprete o corpo (`json.loads`) apenas para ler `st`, procure `KEYS.get(st)` e rejeite se não existir; verifique o MAC com essa chave; só depois da verificação leia qualquer outro campo ou toque no estado. O ID de estação não verificado é apenas um seletor de chave: se um atacante mentir sobre ele, a verificação do MAC falha, porque ele não tem a chave daquela estação. Não registre campos não verificados como fatos, não atualize o estado com eles e não os use para nenhuma decisão além da seleção da chave.

**EX045 — Tamanho da janela.** Janela ao vivo: cerca de 60–120 s — cobrindo o erro de relógio de ±2 s e o atraso de 40 s da operadora, com margem; os 120 s do laboratório são razoáveis. Acúmulo: as estações marcam os envios de acúmulo (um indicador dentro do corpo autenticado); o relay os aceita por um caminho separado que ainda exige um MAC válido e números de sequência estritamente crescentes, aceita carimbos de tempo de até 24 h de idade apenas neste modo, gera um alerta informativo sempre que o modo de acúmulo é usado e encerra o modo de acúmulo quando as mensagens da estação chegam ao tempo ao vivo. Uma única janela de 24 horas para todas as mensagens tornaria a captura e o replay muito mais fáceis.

### Capítulo 16: EX046–EX048

**EX046 — Priorize três alertas.** Primeiro (b), a falha de SSH do relay: explorada ativamente (KEV) num host de criticidade 1; a exposição restrita reduz, mas não elimina a urgência (o próprio host de salto é um alvo) — meta de poucos dias. Segundo (c), o banco de dados do historiador: severidade alta e alcançável a partir de toda a zona corporativa, num host de criticidade 2 cuja perda afeta os relatórios e as investigações — meta de duas a quatro semanas, antes se aparecer exploração. Terceiro (a), o navegador do totem: severidade crítica e exposto à internet, mas de baixa consequência e rápido de reconstruir — meta dentro do ciclo mensal normal, ou remover o acesso à internet. Uma alternativa defensável troca (a) e (c) se o totem compartilhar uma rede com sistemas da garagem de consequência mais alta.

**EX047 — Plano de controles compensatórios.** (1) Desabilitar a interface web do CLP se a Água confirmar que ela não é usada — evidência: exportação de engenharia mostrando-a desligada — termina quando a 4.3 for verificada; (2) restrição do conduíte: apenas o caminho de salto de engenharia pode alcançar a porta web — evidência: regra de firewall mais revisão de fluxos sem outras origens — termina com a 4.3; (3) alerta para qualquer conexão à porta web do CLP — evidência: testado com uma conexão de teste marcada no CLP reserva — termina com a 4.3; (4) comparação semanal da configuração da PS-07 — evidência: comparações datadas — termina com a 4.3. Dono do risco residual: gerente de engenharia da Água até a verificação.

**EX048 — Projeto de teste de restauração.** Ambiente: um host de restauração isolado numa rede de teste, sem conexão com a produção. Etapas: (T0) decisão de restaurar registrada; recuperar a cópia imutável mais recente; restaurar o banco de dados; iniciar o serviço do historiador; (T1) a conta de teste dos operadores consegue consultar os dados mais recentes. Critérios de aprovação: T1 − T0 ≤ 4 h; dados restaurados mais recentes no máximo 24 h mais antigos que o horário do backup (RPO); checksums ou contagens de linhas conferem com o manifesto do backup. Registro: horários, atualidade dos dados, problemas, desvios do runbook, quem executou. Calendário: teste completo trimestral; teste parcial mensal. Uma mensagem de sucesso da tarefa não é um teste de restauração.

### Capítulo 17: EX049–EX051

**EX049 — Corrija o formato do relay.** Corrija primeiro na origem: o relay é um componente da própria FSTS, então configure a sua biblioteca de logs para emitir RFC 5424 com dados estruturados, sob uma mudança normal, verificada pela queda a zero da contagem de não interpretados do normalizador. Acrescente um parser de formato BSD como alternativa para dispositivos de terceiros que não podem ser alterados. Uma linha BSD não tem ano nem fuso horário ("Oct 11 22:17:00"), então o parser precisa supor os dois (por exemplo, o ano do coletor e o fuso configurado no dispositivo) e marcar o registro como de hora de qualidade inferior; ela também não tem dados estruturados, então os campos precisam ser extraídos por padrão.

**EX050 — Ordem dos eventos.** Ordem escrita (ignorando os deslocamentos): 22:14:03 login no rly-01; 22:15:40 falha; 22:15:41 falha; 22:16:00 FLOW; 23:02:11 erro de cota de disco do historiador (a linha do totem não tem hora). Ordem em UTC: 22:02:11 historiador; 22:14:03; 22:15:40; 22:15:41; 22:16:00. Um investigador que usasse a ordem escrita veria o erro do historiador 46 minutos *depois* dos logins de root que falharam e poderia ligá-lo a eles como consequência de um ataque; em UTC, ele aconteceu *antes*, então não pode ter sido causado por eles.

**EX051 — Conte o que você descarta.** Acrescente `assert len(out) + bad == len(lines), "input/output mismatch"` (ou saia com um erro) depois do laço; mantenha `unparsed_by_host`, tomando o host como o terceiro token separado por espaços das linhas não interpretadas, quando disponível (para a linha BSD, `rly-01`). A saída acrescenta `unparsed by host: {'rly-01': 1}`. Uma contagem crescente de não interpretados para um host significa que aquela fonte mudou de formato ou quebrou; toda regra que depende dela está cega em silêncio, então o sistema de monitoramento deveria alertar sobre isso (Capítulo 19).

### Capítulo 18: EX052–EX054

**EX052 — Percorra um cenário.** Caminho: (1) dados retidos além da política fazem o disco crescer → (2) o disco cruza os limiares → (3) as gravações falham → (4) o relay descarta mensagens. Prevenir: aplicação da retenção e da rotação (evidência: verificação da idade do arquivo mais antigo); previsão de capacidade com um limiar de prazo de reposição (Capítulo 1) (evidência: previsão mensal). Detectar: alarme de uso do disco em 65 %/85 % (testado por um teste sintético de limiar); alerta de contagem de descartes/rejeições do relay e alerta de silêncio de estação (testes injetados). Recuperar: buffer nas estações e envio do acúmulo (testados trimestralmente); runbook para liberar espaço com segurança. Cada um tem evidência nomeada.

**EX053 — Conferência pelo catálogo.** Mapeamentos no SP 800-53 Rev. 5: MFA do fornecedor limitado no tempo → AC (Access Control) e IA (Identification and Authentication); registro de sessões → AU (Audit and Accountability); limites de setpoint do CLP → SI (System and Information Integrity) ou CM (Configuration Management); alerta de cloro → SI (monitoramento do sistema); procedimento de dosagem manual → CP (Contingency Planning). Família ausente: SR (Supply Chain Risk Management) — as próprias práticas de segurança da Kell determinam se as suas credenciais têm chance de ser roubadas. Cartão proposto: "Garantia de segurança do fornecedor — questionário anual e cláusulas contratuais exigindo MFA, revogação do acesso de funcionários em 24 h e notificação de incidentes — responsável o gestor de fornecedores da FSTS — evidência: contrato assinado e resposta anual." IR (Incident Response) para um incidente de dosagem também é aceitável.

**EX054 — Duração da sobreposição.** O relay precisa aceitar a chave antiga por pelo menos 24 horas depois da virada, mais uma margem (digamos, 26–48 horas), porque as mensagens acumuladas criadas antes da virada levam MACs com a chave antiga. Cada mensagem leva um identificador da versão da chave (dentro do corpo autenticado ou como um seletor não autenticado, como o ID da estação no EX044); o relay seleciona a chave pela versão, em vez de tentar todas as chaves. Depois da sobreposição, a chave antiga é removida e a sua remoção verificada — uma mensagem de teste selada com a chave antiga precisa então ser rejeitada.

### Capítulo 19: EX055–EX057

**EX055 — Regra por episódio.** Agrupe os eventos da Regra B por (origem, destino); para cada grupo, abra um episódio no primeiro evento e acrescente a ele os eventos posteriores dentro de 60 minutos. Saída: uma linha como `22:16+  B corp->station Modbus 10.40.3.7->10.20.0.11 (2 events, last 22:31)`; o total de alertas cai de 4 para 3. Preservados: a contagem, o primeiro e o último horário e o par, para que os investigadores não percam nada enquanto o plantão recebe uma chamada em vez de duas.

**EX056 — Primeiras ações.** Regra A: (1) confirmar se o SSH está exposto além do host de salto (não deveria estar — constatação do Capítulo 2); (2) conferir se houve algum login bem-sucedido a partir daquela origem; (3) bloquear a origem na borda sob uma mudança padrão e registrar a exposição como constatação. Regra B: (1) conferir o calendário de mudanças em busca de uma sessão de engenharia aprovada; (2) se não houver, ligar para a sala de controle da Água e pedir que observem a PS-04; (3) preservar os registros de fluxo e identificar o usuário da estação de trabalho. Regra C: (1) ligar para a sala de controle da Água para confirmar o estado da estação; (2) conferir a situação da BayTel; (3) conferir os logs do relay em busca de rejeições por MAC ou por janela daquela estação (a lacuna do Capítulo 26).

**EX057 — Monitore o monitor.** Fontes: regra de ausência da taxa de eventos por fonte (nenhum evento por 15 min de uma fonte que normalmente envia a cada minuto) → SOC. Encaminhador: tamanho da fila/acúmulo > 10 min → plantão de plataforma. Normalizador: proporção de não interpretados > 1 % por host, ou qualquer novo host com linhas não interpretadas → plantão de plataforma. Regras: última avaliação há mais de 5 min → líder do SOC. Acionamento: chamada sintética agendada todos os dias às 10:00, que precisa ser reconhecida em 15 min → gerente de plantão, se não for.

### Capítulo 20: EX058–EX060

**EX058 — Hipóteses e discriminantes.** (1) Divergência de chave depois de uma rotação na estação, mas não no relay: as rejeições são "bad MAC"; conferir o calendário de mudanças e os logs de versão da chave. (2) Salto do relógio da estação: as rejeições são "outside time window"; comparar os carimbos de tempo da estação com os horários de recebimento (método do Laboratório 20). (3) Estado de replay envenenado por uma mensagem autêntica com número de sequência alto: as rejeições são "replay"; procurar um grande salto de sequência logo antes das 09:00 (Capítulo 29). (4) Tráfego forjado: "bad MAC" a partir de um endereço de origem inesperado ou numa taxa incomum, enquanto mensagens genuínas também chegam; conferir os fluxos. Todas as verificações são leituras de logs e de registros.

**EX059 — Lista de preservação.** Na ordem, em até dez minutos: (1) anotar a hora e abrir o ticket; (2) copiar os logs do relay (incluindo os de NTP e de rejeições) dos últimos 7 dias; (3) exportar a configuração do firewall e o seu histórico recente de mudanças para o conduíte relay–estação; (4) exportar o extrato do historiador para a PS-09 e a saída da análise no estilo do Laboratório 20; (5) registrar como texto a saída de `timedatectl`/situação do NTP do relay; (6) calcular o hash de cada arquivo (SHA-256) e escrever os hashes no ticket; (7) guardar as cópias fora do host, no armazenamento de evidências. Nada nos sistemas é alterado.

**EX060 — Registro do problema.** *Observado:* lacuna da PS-09 no painel desde cerca de 22:50 de 9 de outubro; todos os números de sequência presentes; carimbos de tempo da estação cerca de 422 s atrás do horário de recebimento do relay; o log de NTP do relay não mostra nenhuma requisição de hora da PS-09 respondida desde 7 de outubro. *Inferido:* a PS-09 perdeu a sua fonte de tempo; os dados foram arquivados na janela errada, e não perdidos. *Causa:* a mudança de firewall CHG-131, de 7 de outubro, substituiu o conjunto de regras relay→estação e omitiu udp/123. *Feito:* udp/123 restaurado sob a CHG-135; deslocamento da PS-09 < 1 s em 30 min; o painel mostra os dados; registros do historiador reindexados pelo horário de recebimento para o período afetado (CHG-136). *Em aberto:* por que a revisão da mudança não pegou o NTP (lista de verificação de revisão — Capítulo 25) e por que nenhum alerta disparou para o deslocamento do relógio (nova regra: deslocamento da estação > 30 s — monitoramento da FSTS, até 20 de outubro).

### Capítulo 21: EX061–EX063

**EX061 — Conserte a RACI.**

| Atividade | SOC | Plantão da FSTS | Líder de Segurança da FSTS | Gerente de turno da Água | Kell | Papel de conformidade designado pelo operador |
|---|---|---|---|---|---|---|
| Detectar e fazer a triagem | R | C | A | I | — | — |
| Conter no relay | C | R | A | C | I | — |
| Desabilitar o acesso do fornecedor | R | R | A | I | C | — |
| Decidir a resposta operacional (confiança na telemetria, leituras manuais) | I | C | C | A/R | — | I |
| Notificar os reguladores, se exigido | — | — | C | C | — | A/R |
| Restaurar o serviço | I | R | A | C | C | I |

Cada linha tem exatamente um A. A decisão operacional pertence à Água, e a notificação regulatória ao papel designado pelo operador, nunca à FSTS.

**EX062 — Defina um gatilho.** "Telemetria não confiável" é declarada quando qualquer uma destas condições ocorre: (1) uma mudança não autorizada confirmada em qualquer relay (constatação de integridade ou de deriva não explicada por um registro de mudança em até 30 minutos); (2) falhas de MAC de três ou mais estações em até 15 minutos; (3) falha na verificação de integridade do relay ou evidência de comprometimento do relay. As falhas de MAC ou o silêncio de uma única estação *não* a disparam (tratados pelo runbook da Regra C). Declarada em conjunto pelo líder de Segurança da FSTS e pelo gerente de turno da Água; a Água passa as estações afetadas para leituras manuais e aumenta a amostragem de qualidade da água. Encerrada em conjunto quando os relays forem verificados como limpos (reconstrução ou integridade confirmada a partir da linha de base fora do host) e as leituras corresponderem às amostras manuais.

**EX063 — Perguntas ao fornecedor.** (1) Como vocês notificam os clientes sobre vulnerabilidades no firmware Kell R2, e com que rapidez? → rotina de vulnerabilidades (Capítulo 16). (2) Como as credenciais dos seus funcionários são protegidas e revogadas quando eles saem? → acesso (Capítulo 7). (3) Qual é o seu compromisso de nos notificar sobre incidentes que afetem os seus sistemas de suporte remoto? → integração e incidentes (este capítulo). (4) As imagens de firmware são assinadas, e como as verificamos? → implantação (Capítulo 27). (5) Quais são as datas de fim de suporte de cada modelo que operamos? → inventário (Capítulo 11). (6) Vocês podem fornecer um SBOM do firmware da RTU ([CISA SBOM](https://www.cisa.gov/sbom))? → aplicabilidade de vulnerabilidades (Capítulo 16).

### Capítulo 22: EX064–EX066

**EX064 — Aprove o plano.** Ordem: (1) `log.forward` do RLY-03 — aprovar primeiro (automático), para restaurar a visibilidade antes que qualquer outra coisa mude ali; (2) `ssh.password_auth` e `ntp.servers` do RLY-02 — aprovar (automático), verificar a deriva zerada e o deslocamento do relógio < 1 s; (3) `relay.debug_listener` do RLY-03 — modificar: preservar o arquivo de configuração, os detalhes do processo do listener e os logs locais, investigar quem o habilitou (Capítulo 20) e então removê-lo sob um ticket; (4) `pkg.relayd` do RLY-03, 2.3.9 → 2.4.1 — mudança normal com canário (Capítulo 27), fora da execução de deriva. Verificação depois de cada host: verificação de deriva limpa para as chaves aprovadas; o relay aceita as mensagens das estações; o normalizador recebe os seus logs.

**EX065 — Ajuste a salvaguarda.** "Mais da metade dos hosts com deriva" fazia sentido com três hosts, mas é um sinal grosseiro com doze: seis hosts com mudanças locais *diferentes* são um problema de disciplina local, enquanto quatro hosts com a *mesma* chave derivando de forma idêntica sugerem que o estado desejado (ou o coletor) está errado. Salvaguarda melhor: parar se qualquer chave isolada diferir do estado desejado em mais de, digamos, 25 % dos hosts; ou se o repositório de estado desejado tiver um commit não revisado ou muito recente que mexa nessas chaves; e sempre parar se o coletor falhar em qualquer host.

**EX066 — Proteja o pipeline.** (1) Branch principal protegido, com revisão obrigatória por alguém que não seja o autor — evidência: exportação das configurações do repositório; (2) mantenedores limitados à equipe de plataforma, com MFA — evidência: lista de membros na revisão de acessos; (3) commits assinados ou tags de versão assinadas, verificados pela automação antes de aplicar — evidência: log de verificação; (4) conta da automação limitada aos relays gerenciados, com credenciais num cofre, rotacionadas — evidência: log de auditoria do cofre; (5) cada execução registrada no SIEM, com alerta para execuções fora do calendário ou a partir de um host inesperado — evidência: alerta testado.

### Capítulo 23: EX067–EX069

**EX067 — Regras de engajamento.** Propósito: testar a detecção da Regra B. Escopo: a estação de trabalho de teste TW-01 (endereço marcado 10.40.99.99), o Arlen 300 reserva no laboratório da FSTS e — apenas durante a visita, numa data nomeada — um teste de conexão TCP do laptop de engenharia ao CLP da PS-04 em tcp/502, abrindo e fechando uma conexão sem escritas nem leituras Modbus, com a aprovação nominal da Água. Fora do escopo: todas as outras estações e controladores. Janela de tempo: horas declaradas. No local: engenheiro da Água na PS-04. Comunicação: sala de controle da Água e SOC avisados antes, no início e no fim; eventos de teste rotulados "TEST-RULEB" no calendário de mudanças. Condições de parada: qualquer comportamento inesperado do CLP, alarme ou pedido da sala de controle. Resultados: guardados no armazenamento de evidências, com a saída bruta dos alertas e os horários.

**EX068 — Quantos testes a mais?** Mais um sucesso consecutivo: 9/9 dá um limite inferior de Wilson de cerca de 0,7008, logo acima de 0,70; 10/10 dá cerca de 0,7225. Passar um limiar por 0,001 é frágil — uma única falha nos próximos testes o derrubaria de novo —, então planeje pelo menos mais dois testes e relate o intervalo, e não apenas "demonstrado eficaz".

**EX069 — Diagnostique uma falha.** Correção: habilitar a exportação de fluxos no switch da estação que não estava exportando (mudança normal com a Água) e verificar se os seus fluxos aparecem no SIEM. Monitoramento que a teria encontrado antes: uma regra de ausência por exportador (Capítulo 19) e uma verificação de inventário de que todo switch na zona das estações é um exportador de fluxos ativo. Novo teste: pelo menos 10 fluxos de teste marcados, distribuídos por todos os switches das estações, sob regras de engajamento atualizadas; atualizar o cartão de controle da Regra B com o novo resultado e a causa das falhas anteriores.

### Capítulo 24: EX070–EX072

**EX070 — Torne-a respondível.** (a) "Para as correções de fornecedores liberadas entre abril e setembro para ativos de criticidade 1, quais foram a mediana e o p90 de dias até a instalação verificada, por grupo de ativos, incluindo as correções em aberto, em comparação com os seis meses anteriores? Decisão: se financiar uma visita extra às estações por mês." (b) "Nos últimos 12 meses, quantos incidentes ou quase acidentes da FSTS envolveram acesso ou software de fornecedores, em comparação com todos os incidentes? Decisão: se priorizar os controles de acesso de fornecedores no próximo trimestre." (c) "Para os alertas do T3, qual foi o tempo mediano entre a detecção pelo SOC e o reconhecimento pelo plantão da FSTS, em comparação com os alertas que não passaram pelo SOC? Decisão: se encaminhar todos os alertas do LANTERN pelo SOC."

**EX071 — Encontre as fraquezas.** (1) Apenas antes/depois — qualquer outra coisa que tenha mudado em abril poderia explicar o resultado; (2) regressão à média — março foi incomum (uma interrupção), então abril provavelmente seria melhor de qualquer forma; (3) reclamações medem o incômodo dos usuários, e não a detecção; (4) sem contagens nem intervalo ("30 % menos" de quantas?); (5) a Regra C detecta silêncio, então poderia *aumentar* a percepção sem reduzir as reclamações. Projeto melhor: medir o tempo de detecção, do início do silêncio até o alerta, em silêncios de teste e em eventos reais, antes e depois, mais uma comparação com estações ainda não cobertas pela Regra C, se a implantação for escalonada.

**EX072 — Escreva a nota do estudo.** *Pergunta:* acrescentar uma primeira ação à Regra C reduz o tempo entre o alerta e a ligação para a sala de controle? *Método:* escala de plantão, oito semanas, texto antigo/novo do alerta alternado por semana; medida: minutos entre o alerta e a ligação registrada; decidido de antemão: comparar as medianas no total e por tecnólogo. *Resultados:* texto antigo, 11 alertas, mediana de 14 min; texto novo, 12 alertas, mediana de 6 min; todo tecnólogo mais rápido com o texto novo. *Limites:* números pequenos; a equipe sabia do estudo; uma semana do texto antigo teve uma interrupção da operadora com muitos alertas simultâneos — excluindo-a, mediana antiga de 11 min, ainda mais lenta. *Recomendação:* adotar primeiras ações para todas as regras de ausência; medir de novo a partir dos dados de rotina daqui a três meses.

### Capítulo 25: EX073–EX075

**EX073 — Critérios de aceitação.** (a) Proteger o SSH: autenticação por senha desabilitada e SSH vinculado à interface de gerenciamento em todos os relays (saída da verificação de deriva); uma tentativa de conexão a partir de um endereço corporativo fora do host de salto é recusada (registro de teste); o host de salto exige MFA (evidência da revisão de acessos). (b) Backups do historiador: backup noturno com uma cópia imutável (relatório de backup e política de armazenamento); teste de restauração dentro do RTO de 4 h e do RPO de 24 h registrado (Capítulo 16); runbook de restauração seguido por alguém que não seja o seu autor. (c) Acesso de fornecedores: habilitação pelo processo testada de ponta a ponta à noite (registro de teste); expiração automática verificada; a Kell reconheceu o processo por escrito.

**EX074 — Lista de verificação da revisão.** (1) Todo sistema referenciado (servidor, endereço, certificado) existe e responde; (2) a direção da confiança está preservada — nenhum novo caminho para dentro da zona das estações; (3) nenhum novo listener em todas as interfaces; (4) nenhum segredo na mudança; (5) rollback definido e testado, ou trivialmente reversível; (6) critérios de aceitação e etapas de verificação declarados; (7) clientes afetados e operação informados quando necessário; (8) implantação escalonada, um host por vez, com condições de parada.

**EX075 — Revisão sem culpados.** *Linha do tempo:* 01:10, a Regra B disparou repetidamente por uma sessão de engenharia ruidosa, mas conhecida; 01:25, o plantão silenciou a Regra B por 24 h para interromper as chamadas; na passagem de turno da manhã seguinte, o silenciamento não foi mencionado; nos dias 1–3, um fluxo corporativo→estação não declarado ocorreu sem alerta. *O que fazia sentido:* as chamadas eram duplicatas de uma atividade conhecida; silenciar mantinha a atenção nos outros alertas. *Condições:* a Regra B alertava por evento, e não por episódio (Capítulo 19); os silenciamentos não tinham expiração automática nem visibilidade; a lista de verificação da passagem de turno não incluía os silenciamentos. *Mudanças:* alertas por episódio para a Regra B — monitoramento da FSTS; silenciamentos limitados a 4 h, com expiração automática e exibidos no relatório de saúde — equipe de plataforma; item "silenciamentos ativos" na lista de verificação da passagem de turno — dono do serviço.

### Capítulo 26: EX076–EX078

**EX076 — Crítica de runbook.** Problemas: sem propósito nem quando usar; sem pré-requisitos (acesso ao armazenamento de chaves, aprovações, Água informada); "gerar" sem método (fonte aleatória segura, onde); sem local do armazenamento de chaves nem custodiante; sem período de sobreposição (as mensagens acumuladas levam MACs com a chave antiga — Capítulo 18); "conferir se funciona" sem verificações específicas; sem aviso à operação (as estações podem silenciar); sem rollback; apagar a chave antiga imediatamente quebra os envios de acúmulo; sem registro da versão da chave e da hora. Reescrita: propósito; pré-requisitos; gerar no armazenamento de chaves; preparar a nova chave no relay (aceitar a antiga e a nova); avisar a sala de controle; fazer a virada no gateway da estação; verificar se as mensagens são aceitas com a nova versão da chave e a contagem de falhas de MAC é zero; depois de 26–48 h, remover a chave antiga e verificar se uma mensagem de teste com a chave antiga é rejeitada; rollback (voltar a estação à chave antiga durante a sobreposição); registro.

**EX077 — Relatório de saúde.** Itens e limiares (verde/âmbar/vermelho): estações reportando (14/14 / 13 / ≤ 12); rejeições + quarentena por hora (< 10 / 10–50 / > 50); dias até o alarme do disco do relay (> 30 / 10–30 / < 10); deslocamento máximo do relógio (< 1 s / 1–2 s / > 2 s); fontes de log atualizadas (todas / 1 desatualizada / > 1 desatualizada); último backup (< 24 h / 24–48 h / > 48 h); último teste de restauração (< 90 dias / 90–120 / > 120); regras avaliadas (< 5 min / 5–15 / > 15); silenciamentos ativos (0 / 1 com expiração / qualquer um sem expiração); alertas abertos há mais de 4 h (0 / 1–2 / > 2). Lido diariamente às 08:30 pelo líder de operações da FSTS.

**EX078 — Decisão de aceitação.** Aceitar com condições: (1) o runbook de restauração do historiador deve ser executado por um membro da equipe que recebe, cronometrado contra o RTO de 4 h, em até duas semanas; (2) as evidências dos dois controles sem datas devem ser produzidas em até duas semanas; (3) suporte inicial da equipe de projeto até que as duas condições sejam cumpridas. A PS09-RTU sem suporte está tratada corretamente como risco aceito, com responsável e plano, e não bloqueia a aceitação. Rejeitar de pronto atrasaria um serviço que, de resto, está pronto; aceitar incondicionalmente deixaria a capacidade de recuperação mais importante comprovada apenas pelo seu autor.

### Capítulo 27: EX079–EX081

**EX079 — Reprove o canário.** Com 7170 aceitas: razão de aceitação de 0,9958 contra 0,9994, queda de 0,0036, que reprova no critério de 0,002; as outras verificações passam; decisão `ROLL BACK canary and open problem record`. Primeiras ações: (1) fazer o rollback do RLY-03 para o 2.4.0 sob a mudança existente; (2) preservar os logs do canário, especialmente os motivos das 30 mensagens rejeitadas, antes que sejam rotacionados; (3) informar a sala de controle da Água de que a implantação está pausada e abrir um registro de problema com a Kell ou com o mantenedor do relay.

**EX080 — Conjunto de validação de segurança.** (1) Mensagem de teste com MAC errado → rejeitada com "bad MAC"; (2) replay de uma mensagem genuína recente → rejeitada com "replay"; (3) verificação de deriva → nenhum novo listener nem chave de segurança alterada; (4) contagem de não interpretados do normalizador para o host → inalterada (zero); (5) o processo do relay roda com a conta sem privilégios `relay` → confirmado; (6) teste da Regra A injetado a partir de um endereço marcado → alerta dentro da meta.

**EX081 — Estenda a janela.** Dia 1 (terça-feira), 22:00: implantar o canário no RLY-03. Dia 2: avaliar os critérios no pico da manhã, das 06:00 às 09:00. Dias 6–7: manter o canário durante a execução semanal de relatórios, avaliando os critérios durante a execução. Dia 8: se tudo passar, promover para o RLY-02; avaliar no pico da manhã do dia 9. Dia 10: promover para o RLY-01 e validar. Pacote de rollback preparado e testado no dia 1; qualquer falha em qualquer ponto de controle dispara o rollback dos hosts na nova versão. Termina em dez dias.

### Capítulo 28: EX082–EX084

**EX082 — Registre o modem.** *Observado (10 de outubro, 10:40, PS-07, com o engenheiro da Água J. Abara):* modem celular, etiqueta "Kell RS-4", conectado à porta 2 do CLP; LED de energia aceso; fora do inventário e da lista de conduítes; o engenheiro afirma que a Kell o instalou para suporte remoto há cerca de seis anos e acredita que não é usado. *Inferido:* um caminho remoto não declarado até o CLP, que pode estar ativo. *Feito:* etiqueta fotografada com permissão; a Água abriu a mudança CHG-W-221 para confirmar a dependência e removê-lo. *Em aberto:* se há um SIM ativo e quem detém a conta (Água com a Kell, até 17 de outubro); data de remoção; se outras estações têm modems semelhantes (item de levantamento para as visitas restantes). Registros atualizados: inventário, lista de conduítes, registro de fluxos de dados, registro de riscos (novo cenário).

**EX083 — Regras do laptop de campo.** (1) Um laptop de campo dedicado, usado para nada mais — verificação: registro do ativo e log de retirada; (2) com patches e endurecido antes de cada visita — verificação: relatório de conformidade pré-visita; (3) sem uso pessoal nem navegação — verificação: revisão periódica; (4) nunca conectado às redes corporativa e da estação ao mesmo tempo — verificação: log de conexões mantido para cada visita; (5) mídias removíveis dedicadas e verificadas antes e depois de cada uso — verificação: log de varredura; (6) laptop conferido depois de cada visita (integridade e varredura de malware) — verificação: relatório pós-visita.

**EX084 — Plano de exercício.** Objetivos: tempo entre as condições do gatilho e a declaração (meta de 15 min); tempo entre a declaração e a primeira leitura manual em cada estação (meta de 45 min); clareza das comunicações. Cenário: relato sintético de falhas de MAC em três estações (injetado no sistema de teste, não real). Participantes: líder de Segurança da FSTS, gerente de turno da Água, sala de controle, duas pessoas de campo, observador do SOC. Etapas com pontos de cronometragem: T0, sinal injetado; T1, declaração; T2, pessoal de campo despachado; T3, primeiras leituras informadas por telefone; T4, fim declarado. Condições de parada: qualquer alarme real, preocupação com o abastecimento ou pedido da sala de controle. Safety: regras normais de safety do local e de trabalho solitário. Resultados registrados por um cronometrista; revisão sem culpados em até uma semana.

### Capítulo 29: EX085–EX087

**EX085 — Reproduza o defeito.** Com a sequência do teste fora da faixa definida como 1000: `"stored": 225`, `"alert_count": 103`, e os alertas passam a incluir `["replay_reject", "PS-07"]`. Perdidas: 99 leituras genuínas da PS-07 (sequência 21–119). Causa: o relay registra o último número de sequência depois da autenticação, mas antes da verificação de faixa; a mensagem autêntica fora da faixa define a última sequência da PS-07 como 1000, então toda mensagem genuína posterior tem um número menor e é rejeitada como replay.

**EX086 — Corrija.** Um limite de 1.000 não ajuda aqui: o salto de 19 para 1000 é de 981. Um limite baseado no tempo funciona: rejeitar (evento `seq_jump_reject`) quando o salto exceder os minutos decorridos desde a última mensagem aceita da estação mais uma margem de 5. Implementado no Laboratório 29 (acompanhando `last_t` por estação, ao lado de `last`), a execução com a sequência 1000 dá `"stored": 324`, `"alert_count": 4`, com `seq_jump_reject` para a PS-07 no lugar da quarentena por faixa, e o replay da PS-04 continua rejeitado; com a sequência 20, a saída não muda em relação à original (324 armazenadas, quatro alertas). O retorno da PS-09 depois do seu silêncio de 35 minutos é aceito, porque o seu salto de 36 fica dentro de 36 + 5. Observe que `injected_tests_detected` informa 3 com a sequência 1000, porque o conjunto de detecção ainda não inclui `seq_jump_reject` — acrescente-o.

**EX087 — Revisão do registro de evidências.** Contagens: mensagens na rede 327 = 120 (PS-04) + 119 (PS-07, menos o lugar ocupado pelo teste) + 85 (PS-09) + 3 mensagens injetadas; armazenadas 324 = 327 − 3 (replay rejeitado, falsificação rejeitada, fora da faixa em quarentena). Digest: aplicar o hash exatamente à linha JSON impressa (`sha256` dos bytes sem a quebra de linha final) dá um digest que começa com `aa40e3905d178699f1460e1c`, igual ao impresso. Limites a declarar: estações e valores sintéticos; uma única execução de duas horas; sem dispositivos de campo reais, operadora ou carga em escala; sem adversário adaptativo; tratamento de chaves simplificado (chave no código-fonte).

### Capítulo 30: EX088–EX090

**EX088 — Responda aos revisores.** (a) Vazamento de chave: as chaves são por estação, então uma chave vazada permite que um atacante se passe por uma estação, e não por todas; mensagens forjadas passariam pelo MAC e pela validação se fossem plausíveis; a detecção é fraca — números de sequência duplicados vindos de duas origens ou valores em desacordo com as estações vizinhas poderiam mostrá-lo, mas isso não foi testado; resposta: revogar e rotacionar usando o runbook testado e tratar os dados daquela estação como não confiáveis até a rotação. (b) Quem construiu sai: o estado desejado e a automação estão num repositório revisado, com pelo menos dois mantenedores; os runbooks foram seguidos pela equipe que recebe durante o acompanhamento; as credenciais estão num cofre, e não com a pessoa; o acesso é removido pelo processo de saída. (c) BayTel fora do ar por um dia: as estações guardam 24 h em buffer; os alertas de silêncio disparam; a Água passa para leituras manuais; no retorno, o envio do acúmulo foi testado para 4 h, mas não para 24 h — uma lacuna honesta, com um teste planejado.

**EX089 — Avalie a Equipe A e a Equipe B.** Equipe A: função de ponta a ponta 1 (afirmada), controles 1 (configurados, sem resultados de teste), propriedades de projeto — desconhecidas, operabilidade — desconhecida, qualidade das evidências 0–1 (sem datas, contagens nem digest), honestidade 1 (nenhuma lacuna declarada). Equipe B: função 3 (quatro de quatro, com digest), controles 2–3 (regras de afirmação aplicadas, FIM ainda não demonstrada, com mudança aberta), propriedades de projeto — não mostradas no resumo, operabilidade 2 (lacuna no runbook encontrada e corrigida), qualidade das evidências 3, honestidade 3 (áreas não testadas nomeadas). O avaliador pede à Equipe A as evidências brutas e à Equipe B o material da revisão de projeto antes das notas finais.

**EX090 — Plano de prática contínua.** Mensal: ler os avisos dos produtos do inventário (avisos dos fornecedores; feeds dos CERTs nacionais; CISA KEV) e um relatório público de incidente, anotando as premissas que falharam; revisar as tendências do relatório de saúde. Trimestral: participar de um exercício ou teste de controle; revisar as constatações da revisão de acessos e da deriva com um colega. Anual: reler as versões em uso do NIST CSF 2.0, do SP 800-82 Rev. 3 e dos CISA CPGs ou do NCSC CAF, e as orientações setoriais da jurisdição; verificar se houve revisões; atualizar os cartões de controle afetados; buscar uma revisão externa de uma parte do seu próprio trabalho. Carga de trabalho: cerca de quatro horas por mês.

<a id="glossary"></a>

## Glossário

- **Allowlist** — uma lista do que é permitido; tudo o que não está nela é recusado (Capítulos 3, 15).
- **Alerta por episódio** — um grupo de eventos relacionados relatado como um único alerta, com uma contagem (Capítulo 19).
- **Canário** — uma primeira implantação, limitada, comparada com os hosts na versão antiga antes da implantação mais ampla (Capítulo 27).
- **Cenário (de risco)** — uma história específica de causa, caminho, ativo, consequência e controles existentes (Capítulo 13).
- **Conduíte** — um caminho de comunicação declarado e justificado entre duas zonas (Capítulo 2).
- **Controle compensatório** — um controle temporário ou alternativo usado quando a correção normal ainda não é possível (Capítulos 11, 16).
- **Critérios de aceitação** — condições verificáveis, que produzem evidências, que definem quando um item de trabalho está pronto (Capítulo 25).
- **Defesa em profundidade** — vários controles independentes, para que uma falha não leve direto ao dano (Capítulo 8).
- **Deriva** — diferença entre a configuração real de um host e o seu estado desejado (Capítulo 22).
- **Direção da confiança** — no LANTERN, a propriedade de que os dados sobem das estações e os comandos nunca descem pelo serviço (Capítulo 8).
- **Exposição** — se uma ameaça consegue de fato alcançar uma vulnerabilidade (Capítulo 5).
- **Faixa de consequência** — um julgamento de quão ruim seria o resultado de um cenário para as pessoas, medido em pessoas e tempo (Capítulo 13).
- **Folga (headroom)** — capacidade sobrando entre a carga normal de pico e o ponto de degradação (Capítulo 1).
- **HMAC** — um código de autenticação de mensagem construído a partir de uma função de hash e de uma chave secreta ([RFC 2104](https://www.rfc-editor.org/rfc/rfc2104)) (Capítulo 15).
- **Intervalo de Wilson** — um intervalo de confiança para uma proporção que se comporta bem com amostras pequenas (Capítulo 9).
- **Linha de base (de configuração)** — a configuração aprovada para uma classe de sistema, mantida em controle de versão (Capítulo 14).
- **Linha de base (de integridade de arquivos)** — hashes e permissões registrados dos arquivos importantes num momento sabidamente bom (Capítulo 6).
- **Modo degradado** — uma forma deliberadamente projetada de um serviço operar com um componente indisponível (Capítulo 8).
- **Normalização** — converter logs de fontes diferentes numa única estrutura de registro comum (Capítulo 17).
- **Quarentena** — manter de lado, para revisão, uma entrada interpretável, mas implausível, em vez de rejeitá-la ou aceitá-la (Capítulo 3).
- **RACI** — Responsável, Aprovador (Accountable), Consultado, Informado: uma matriz de responsabilidades com um único papel aprovador por atividade (Capítulo 21).
- **Registro de fluxos de dados** — registro de quais dados trafegam entre sistemas, com classe, proteção e retenção (Capítulo 12).
- **Regra de afirmação** — um critério, fixado antes do teste, para declarar um controle eficaz (Capítulo 23).
- **Regras de engajamento** — termos assinados de um teste: escopo, ações, janela, comunicação e condições de parada (Capítulo 23).
- **Replay** — reenviar uma mensagem válida capturada anteriormente (Capítulo 15).
- **Revisão de acessos** — comparação periódica das contas de um sistema com uma lista autoritativa e uma declaração de necessidade (Capítulo 7).
- **Revisão sem culpados** — uma revisão de uma falha que procura condições a mudar, e não pessoas a culpar (Capítulo 25).
- **RPO / RTO** — objetivo de ponto de recuperação (perda de dados tolerável) e objetivo de tempo de recuperação (tempo para restaurar o serviço) (Capítulo 16).
- **Runbook** — procedimento passo a passo escrito para um colega competente sob pressão de tempo (Capítulo 26).
- **Zona** — um grupo de sistemas com confiança e função semelhantes (Capítulo 2).

<a id="references"></a>

## Referências

Leis, normas, orientações e páginas públicas mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas. Uma citação sustenta a afirmação geral ao seu lado no texto, nunca os detalhes do caso sintético.

### Normas, orientações e leis

- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- National Institute of Standards and Technology. [SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- National Institute of Standards and Technology. [SP 800-40 Rev. 4, Guide to Enterprise Patch Management Planning](https://csrc.nist.gov/pubs/sp/800/40/r4/final).
- National Institute of Standards and Technology. [SP 800-41 Rev. 1, Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-123, Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final).
- National Institute of Standards and Technology. [SP 800-125, Guide to Security for Full Virtualization Technologies](https://csrc.nist.gov/pubs/sp/800/125/final).
- National Institute of Standards and Technology. [SP 800-128, Guide for Security-Focused Configuration Management of Information Systems](https://csrc.nist.gov/pubs/sp/800/128/upd1/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).
- National Institute of Standards and Technology. [SP 800-184, Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final).
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29). February 2024.
- National Institute of Standards and Technology. [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
- OWASP Foundation. [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html).

### Protocolos e documentação de software

- Gerhards, R. [RFC 5424: The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424). IETF, 2009.
- Klyne, G., and Newman, C. [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339). IETF, 2002.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, 1997.
- Mills, D., Martin, J., Burbank, J., and Kasch, W. [RFC 5905: Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905). IETF, 2010.
- Python Software Foundation. [hmac — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html) and [sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html). Python 3 documentation.
- Rekhter, Y., et al. [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918). IETF, 1996.
- Arkko, J., Cotton, M., and Vegoda, L. [RFC 5737: IPv4 Address Blocks Reserved for Documentation](https://www.rfc-editor.org/rfc/rfc5737). IETF, 2010.
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, 2018.

### Incidentes, operações e métodos

- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. (eds.). [Site Reliability Engineering, Chapter 15: Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/). O'Reilly / Google, 2016.
- Beyer, B., Murphy, N. R., Rensin, D. K., Kawahara, K., and Thorne, S. (eds.). [The Site Reliability Workbook, Chapter 16: Canarying Releases](https://sre.google/workbook/canarying-releases/). O'Reilly / Google, 2018.
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606, 2018.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320, 768–770, 2000.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine*, 21(6), 11–25, 2001.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.
- Wilson, E. B. [Probable Inference, the Law of Succession, and Statistical Inference](https://doi.org/10.1080/01621459.1927.10502953). *Journal of the American Statistical Association*, 22(158), 209–212, 1927.
