# Infraestrutura Crítica e Segurança Setorial: Prática Técnica Aplicada

- Idioma: português do Brasil (`pt`); curso técnico, dezoito meses; aproximadamente 1.200 horas de estudo planejado (curso 069 de 207 da [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–5 de 18 já estão escritos em português, com os exercícios EX001–EX020 e suas resoluções; os capítulos 6–18 (EX021–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: operadores técnicos — técnicos de redes e de sistemas, técnicos de SCADA e de telemetria, analistas de segurança júnior em centros de operações — que já conhecem redes, sistemas operacionais e scripts básicos e agora trabalham em sistemas que movem água, energia ou o ar dos pacientes. Conhecimento de entrada: redes, sistemas operacionais, scripts e prática segura de laboratório.
- Como este curso difere dos vizinhos. O [livro de tecnólogo](../../../../technologist-3-years/critical-sector-security/en/book/MANUSCRIPT.md) ensina implementadores a construir, operar e entregar um serviço monitorado completo. Os cursos [profissional](../../../../professional-6-months/critical-sector-security/en/book/MANUSCRIPT.md) e [rápido](../../../../rapid-1-month/critical-sector-security/en/book/MANUSCRIPT.md) tratam de decisões gerenciais e de uma primeira introdução. **Este livro técnico trata da profundidade técnica prática**: abrir os pacotes dos protocolos industriais, auditar e endurecer hosts, configurar e verificar firewalls de conduítes, detectar modos de falha e comandos não autorizados, resolver problemas eliminando hipóteses e produzir evidências que outro técnico possa conferir. Todo capítulo pergunta: *o que exatamente você digitaria, leria, mudaria ou testaria, e como provaria isso?*
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de titularidade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: este curso é um projeto educacional independente. Não é um programa credenciado, não concede qualificação e não concede nenhuma autorização para acessar, varrer, testar ou alterar qualquer infraestrutura, operador, dispositivo, conjunto de dados ou pessoa reais. Toda organização, lugar, pessoa, endereço, registro, quadro, valor e resultado numérico de um exemplo resolvido ou laboratório é **sintético**, a menos que uma frase cite explicitamente uma fonte pública. Os endereços IP vêm de faixas privadas ([RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)) ou de documentação ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)). Nada neste livro é um procedimento operacional para uma concessionária, um hospital ou uma rede elétrica reais, e nada nele é aconselhamento jurídico, clínico ou regulatório.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão de livros](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os dezoito capítulos acompanham um técnico ao longo de dezoito meses num centro regional de operações. O resultado do curso é prático: **diagnosticar falhas, configurar controles e verificar resultados** em infraestrutura crítica, num laboratório reprodutível e sob supervisão.

- **Etapa 1 (Capítulos 1–6)** trata da arquitetura de serviço e dos orçamentos de varredura, da decodificação de Modbus/TCP, da auditoria de hosts e contas, da análise estrita de dados, do escopo técnico e das evidências, e do modelo de sistema de zonas e conduítes.
- **Etapa 2 (Capítulos 7–12)** trata de telemetria e tempo, modos de falha, ferramentas e verificação da camada de enlace do DNP3, configuração de firewalls, verificação por testes rastreáveis e o primeiro laboratório contido (um respondedor Modbus com política de escrita).
- **Etapa 3 (Capítulos 13–18)** trata da resolução de problemas orientada por hipóteses, da automação para detecção de deriva, da análise de dependências, da documentação técnica e da segurança, do segundo laboratório contido (um pipeline de detecção) e de um projeto supervisionado com um pacote de evidências selado.

Cada capítulo tem objetivos de aprendizagem, seções didáticas com definições, um exemplo resolvido, uma atividade prática, erros comuns e limites, quatro exercícios numerados e uma síntese. Quinze capítulos contêm um laboratório em Python. Os laboratórios usam apenas a biblioteca padrão do Python 3 (as saídas deste rascunho foram produzidas com o Python 3.13.5); não precisam de rede, pacotes, privilégios nem dados reais, e toda saída está impressa no texto para que você confira sua execução. O Laboratório 12 usa `socket.socketpair()`, que conecta dois sockets dentro de um único processo e não alcança nenhuma rede. Os laboratórios que gravam arquivos o fazem apenas dentro de um diretório temporário que criam e removem. Escreva sua resposta a cada exercício antes de abrir as [resoluções](#worked-results); a rubrica de 0 a 3 mostra o que um avaliador recompensa, e uma resposta diferente e defensável pode receber a pontuação máxima.

Mantenha quatro rótulos em toda nota de trabalho: **observado** (o que uma ferramenta ou pessoa nomeada registrou, com horário UTC e fonte), **inferido** (o que você conclui e por quê), **feito** (o que você mudou, sob qual registro de mudança) e **em aberto** (o que ainda é desconhecido, e quem é o responsável).

### O cenário sintético usado neste livro

| Elemento sintético | Papel no livro | Limite |
|---|---|---|
| **Kestrel Vale** — uma região fictícia | Cenário de todos os exemplos. | Lugar inventado. |
| **Kestrel Vale Regional Operations Centre (KVROC)** | Opera os sistemas de supervisão de três operadores. O leitor é um **técnico**; L. Ferreira é a líder de segurança; J. Tan e R. Kaur são colegas. | Inventado; nenhuma organização ou pessoa real. |
| **Kestrel Water** — estações KW-01 a KW-12 (RTUs em 10.10.*n*.2), A. Mensah gerente de operações | Principal fonte dos exemplos de Modbus/TCP. | Inventada. |
| Subestação **SS-3** da **Kestrel Grid** (endereço de outstation DNP3 10; endereço de mestre 1; front end fep-01) | Exemplos de DNP3. | Inventada. |
| Sistema de gestão predial do **Kestrel General Hospital** | Exemplos de dependência na saúde. | Inventado. |
| Os hosts scada-01, eng-ws-15, hmi-02, hist-02, jump-01, fw-01, ntp-ops, ad-ops, esx-02/03 e todo quadro, linha de log, valor e horário | Contexto dos laboratórios e exercícios. | Inventados. |

Como os dados são sintéticos, o livro pode dizer o que um técnico real raramente sabe com certeza. Use isso para aprender como as verificações falham, nunca como evidência sobre organizações reais.

### Política de fontes

Toda afirmação factual sobre um protocolo, uma norma, um incidente público ou uma orientação publicada remete a uma fonte consultada em outubro de 2026. Normas e orientações mudam: verifique cada uma de novo antes de se apoiar nela. O vocabulário profissional comum não recebe uma referência inventada. Uma citação apoia a afirmação geral ao seu lado, nunca os detalhes sintéticos. Incidentes públicos são descritos apenas no nível de detalhe que seus editores divulgaram, e nunca como técnica.

### Regras de segurança para o trabalho prático

1. Pratique apenas nos laboratórios do livro, em equipamentos seus ou em sistemas cujo dono lhe tenha dado permissão **escrita e específica**, nomeando sistemas, ações e janela (Capítulo 5).
2. Nunca conecte um scanner, um notebook de testes ou um script a uma rede de controle em produção sem essa permissão e sem a concordância das pessoas responsáveis pelo processo físico. Em tecnologia operacional, uma leitura pode ser uma ação.
3. Nunca mexa em sistemas de proteção ou de segurança funcional como parte do trabalho de segurança (Capítulo 16).
4. Se notar uma fraqueza num sistema real, pare, registre o que viu e relate-a em particular ao dono ou por divulgação coordenada. Não a "confirme".
5. Mantenha segredos fora de notas, chamados e capturas de tela.

## Sumário

1. [Computação e arquitetura de serviço](#ch-01) — camadas, três caminhos e o orçamento do ciclo de varredura.
2. [Redes e protocolos](#ch-02) — protocolos industriais sem autenticação e decodificação de Modbus/TCP.
3. [Sistemas operacionais e identidades](#ch-03) — configuração efetiva do SSH, UIDs, contas de serviço e grupos.
4. [Scripts e formatos de dados](#ch-04) — análise estrita de CSV/JSON, ordem de validação e coordenadas de registro.
5. [Escopo de segurança e evidências](#ch-05) — escopo técnico, passivo primeiro, evidências verificáveis.

Capítulos 6–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-06), até a chegada dos próximos lotes.

Apêndices: [Resoluções e notas de avaliação](#worked-results) · [Glossário](#glossary) · [Referências](#references).

<a id="ch-01"></a>

## Capítulo 1 — Computação e arquitetura de serviço

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- desenhar a arquitetura técnica de um serviço de controle supervisório — dispositivos de campo, enlaces de comunicação, servidores de front end e SCADA, historiador, IHM, estação de engenharia, plano de gerência — e dizer qual componente faz o quê;
- distinguir o **caminho de controle**, o **caminho de monitoramento** e o **caminho de gerência**, e explicar por que um técnico protege cada um de modo diferente;
- calcular um **orçamento do ciclo de varredura** e usá-lo para prever o que um enlace lento ou morto faz com a atualidade dos dados do operador;
- identificar os componentes de plataforma compartilhados (hosts de virtualização, diretório, tempo, armazenamento) cuja falha atravessa as fronteiras entre serviços.

Este é o primeiro capítulo de um curso prático. Tudo o que vem depois — decodificação de protocolos, endurecimento, detecção, resolução de problemas — pressupõe que você consiga apontar para uma caixa do diagrama e dizer que tráfego ela envia, o que armazena e o que quebra se ela parar. O conhecimento de entrada (redes, sistemas operacionais, scripts) é pressuposto; o elemento novo é o processo físico do outro lado do fio.

### 1.1 As camadas de um serviço de controle supervisório

A maioria dos serviços de setores críticos que movem água, energia, ar ou pessoas compartilha uma forma em camadas reconhecível. O guia do NIST para tecnologia operacional descreve os mesmos componentes em termos gerais ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); os nomes abaixo são os usados neste livro.

- **Dispositivos de campo**: sensores (nível, vazão, cloro, pressão, temperatura, corrente), atuadores (bombas, válvulas, disjuntores) e os controladores que os conectam — **CLPs** (controladores lógicos programáveis), que executam lógica local, e **RTUs** (unidades terminais remotas), construídas para locais remotos com comunicações limitadas.
- **Enlaces de comunicação**: fibra, rádio licenciado, roteadores celulares, linhas dedicadas ou a rede MPLS de uma operadora. Sua latência, perda e custo moldam tudo o que está acima deles.
- **Processador de front end (FEP) ou servidor SCADA**: faz a varredura dos dispositivos de campo, aplica escalas e alarmes e mantém o estado atual do processo.
- **Historiador**: armazena séries temporais para relatórios, investigações e registros regulatórios.
- **IHM** (interface humano–máquina): as telas do operador, a partir das quais são emitidos comandos como "ligar bomba 2".
- **Estação de engenharia**: guarda os projetos dos controladores e as ferramentas do fabricante que alteram a lógica dos controladores; o computador mais poderoso do sistema.
- **Plano de gerência**: hosts de salto (jump hosts), serviços de diretório, servidores de tempo, backup, gerência de virtualização e o coletor de monitoramento.

### 1.2 Três caminhos, três problemas de proteção

Um técnico deve ser capaz de traçar três caminhos diferentes no diagrama.

O **caminho de controle** leva comandos ao processo: IHM → servidor SCADA → enlace → controlador → atuador. A integridade e a disponibilidade desse caminho são o que mantém as pessoas em segurança; uma escrita não autorizada ou corrompida aqui é o pior caso deste livro.

O **caminho de monitoramento** traz as medições de volta: sensor → controlador → enlace → servidor SCADA → historiador e IHM. Se ele estiver errado, os operadores agem com base em informação falsa — uma falha que pode ser tão perigosa quanto um comando ruim, e mais difícil de notar.

O **caminho de gerência** altera o próprio sistema: um engenheiro carregando uma nova lógica, um administrador aplicando patches no historiador, um fornecedor se conectando para diagnosticar uma falha. É usado raramente, mas concentra o maior privilégio, e é onde, segundo os relatos, começou a maioria das intrusões reais em ambientes de controle; o alerta da CISA sobre os ataques de dezembro de 2015 a distribuidoras ucranianas descreve acesso remoto e uso de credenciais antes do impacto operacional ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)).

Os três caminhos muitas vezes compartilham cabos, switches e servidores. Desenhá-los separadamente é como você descobre que um notebook de "monitoramento" no switch do centro de controle também alcança as portas de programação dos controladores.

### 1.3 Varredura e atualidade

A maioria dos protocolos de estação deste livro é de **requisição–resposta**: o servidor SCADA pergunta, o dispositivo responde. O tempo para atualizar cada estação uma vez é o **ciclo de varredura**. Para cada estação, ele é aproximadamente *varreduras por ciclo × (tempo de ida e volta do enlace + tempo de resposta do dispositivo)*. Se o servidor varre as estações uma após a outra num único canal, o ciclo é a **soma** sobre as estações; se ele tem um canal independente por estação, o ciclo é definido pela estação **mais lenta**.

Duas consequências importam para o trabalho de segurança. Primeiro, um enlace lento (um roteador celular congestionado, um caminho de rádio degradado) estica o ciclo para todos os varridos depois dele. Segundo, um dispositivo que não responde custa o **timeout** inteiro a cada varredura, de modo que uma estação morta pode esticar o ciclo mais do que uma lenta. Os requisitos de atualidade — "toda estação atualizada pelo menos a cada 5 s" — dependem, portanto, dos timeouts e do número de tentativas, além da velocidade do enlace, e um controle de segurança que acrescenta latência (uma VPN, um proxy de inspeção) precisa ser verificado frente a esse orçamento antes de ser instalado.

### 1.4 Plataformas compartilhadas

Os centros de controle modernos executam seus servidores SCADA, historiadores e diretório em hosts de virtualização, muitas vezes compartilhados entre serviços. Um hipervisor, diretório, fonte de tempo ou storage compartilhado é um ponto em que uma falha num setor se torna uma falha em vários. O Laboratório 15, no Capítulo 15, rastreia essas dependências com código; aqui, apenas aprenda a marcar cada componente compartilhado no diagrama com os serviços que dependem dele.

No KVROC, o host esx-02 executa o servidor SCADA, o historiador e o servidor do sistema de gestão predial do hospital, de modo que uma indisponibilidade dele ou um patch ruim pode afetar juntos o monitoramento da água e o da saúde. Marque cada componente compartilhado com todos os serviços que dependem dele e pergunte quem é o dono do host quando esses serviços discordam sobre uma janela de mudança.

### 1.5 Exemplo resolvido: o centro de operações de Kestrel Vale (sintético)

Você é técnico no **Kestrel Vale Regional Operations Centre (KVROC)**, que opera os sistemas de supervisão da **Kestrel Water** (12 estações, KW-01 a KW-12), o monitoramento dos sistemas de gestão predial do **Kestrel General Hospital** e o front end de telecontrole de uma subestação (**SS-3**) da **Kestrel Grid**. As RTUs das estações ficam em 10.10.0.0/16 (KW-*n* é 10.10.*n*.2); o centro de controle é 10.20.0.0/24 (servidor SCADA `scada-01` 10.20.0.10, estação de engenharia `eng-ws-15` 10.20.0.15, historiador `hist-02` 10.20.0.21); as mesas corporativas ficam em 10.30.0.0/16; a rede de gerência é 10.90.0.0/24 (host de salto `jump-01` 10.90.0.20). Todos os nomes e endereços são fictícios.

As operações exigem toda estação atualizada em até 5 segundos. O `scada-01` varre as doze estações num único canal. O Laboratório 1 calcula o orçamento.

**Laboratório 1** (salve como `lab01.py` e execute com `python3 lab01.py`):

```python
# Lab 1 - poll-cycle budget for a SCADA server polling stations (offline, standard library only)
# Synthetic Kestrel Water figures. Each poll = request + response over the link plus device turnaround.
stations = {  # name: (link, round-trip ms on the link, device turnaround ms, polls per cycle)
 "KW-01": ("fibre", 4, 20, 3), "KW-02": ("fibre", 4, 20, 3), "KW-03": ("fibre", 5, 25, 3),
 "KW-04": ("cellular", 180, 40, 4), "KW-05": ("cellular", 210, 40, 4), "KW-06": ("cellular", 650, 40, 4),
 "KW-07": ("radio", 420, 60, 3), "KW-08": ("radio", 460, 60, 3), "KW-09": ("cellular", 190, 40, 4),
 "KW-10": ("fibre", 4, 20, 3), "KW-11": ("radio", 440, 60, 3), "KW-12": ("cellular", 200, 40, 4),
}
REQUIRED_S = 5.0          # operations require every station refreshed at least every 5 s
TIMEOUT_MS = 1500         # a poll that gets no reply costs the full timeout
def cycle(stations, sequential=True, dead=()):
    per = {}
    for n, (link, rtt, turn, polls) in stations.items():
        per[n] = polls * (TIMEOUT_MS if n in dead else rtt + turn)
    return (sum(per.values()) if sequential else max(per.values())) / 1000, per
c, per = cycle(stations)
print(f"sequential cycle {c:.2f} s (requirement {REQUIRED_S} s) -> {'OK' if c <= REQUIRED_S else 'FAILS'}")
worst = max(per, key=per.get); print(f"slowest station {worst}: {per[worst] / 1000:.2f} s per cycle")
c2, _ = cycle(stations, dead={"KW-06"})
print(f"sequential with KW-06 not answering: {c2:.2f} s")
c3, _ = cycle(stations, sequential=False, dead={"KW-06"})
print(f"one polling channel per station, KW-06 dead: {c3:.2f} s")
```

Saída esperada (Python 3.13.5):

```text
sequential cycle 11.33 s (requirement 5.0 s) -> FAILS
slowest station KW-06: 2.76 s per cycle
sequential with KW-06 not answering: 14.57 s
one polling channel per station, KW-06 dead: 6.00 s
```

O resultado diz que o requisito já não é atendido (11,33 s), principalmente por causa das estações celulares e de rádio, sendo KW-06 a mais lenta. Uma KW-06 morta acrescenta outros 3,24 s, porque cada varredura sem resposta custa 1,5 s. Mesmo com um canal por estação, o ciclo é de 6,00 s enquanto a KW-06 estiver morta: canais por estação eliminam o problema da *soma*, mas não o problema do *timeout*. Um técnico a quem se pede "acrescentar um túnel criptografado às estações celulares" agora sabe qual pergunta fazer primeiro: quantos milissegundos ele acrescenta por varredura, e o que isso faz com um ciclo que já não atende ao requisito?

### 1.6 Atividade prática: desenhe o seu próprio diagrama de três caminhos

Usando a descrição do KVROC, desenhe os caminhos de controle, de monitoramento e de gerência em três cores. Marque todo componente que aparece em mais de um caminho e todo componente de plataforma compartilhado. Guarde o desenho: os Capítulos 6, 10 e 15 o refinam.

Use três cores ou três camadas de página, para que um switch ou um host de salto compartilhado se destaque. Depois verifique se a eng-ws-15 aparece tanto no caminho de gerência quanto no de controle: se aparecer, um comprometimento dessa estação alcança todas as estações. Guarde o desenho junto com o orçamento do Laboratório 1, porque uma proposta posterior de túnel ou de criptografia terá de ser julgada frente aos caminhos e ao ciclo de varredura.

### 1.7 Erros comuns e limites

- Desenhar apenas a rede e esquecer o caminho de gerência, que é onde o privilégio está.
- Tratar o historiador como "apenas TI"; ele costuma ser a ponte entre as redes de controle e corporativa.
- Medir a velocidade do enlace, mas não os timeouts e as novas tentativas; dispositivos mortos dominam os ciclos de varredura.
- Presumir que uma arquitetura paralela resolve a atualidade; ela muda a aritmética, não o timeout.
- O modelo do Laboratório 1 ignora novas tentativas, a contenção em linhas seriais e o overhead do protocolo; trate seus números como uma primeira estimativa e depois meça.

- Esquecer que uma estação morta custa o timeout inteiro a cada varredura, de modo que uma única RTU que não responde pode esticar o ciclo mais do que uma lenta.
- Desenhar os caminhos de controle e de monitoramento e deixar de fora o host de salto, o diretório e o servidor de tempo.
- Tratar os números do Laboratório 1 como valores medidos, e não como uma primeira estimativa que ainda precisa ter as novas tentativas e o overhead do protocolo verificados no local.

### Exercícios — capítulo 1

**EX001 — Classificação de caminhos.** *Objetivo:* separar os três caminhos. *Insumos:* estes fluxos: IHM → scada-01 "ligar bomba 2"; RTU da KW-04 → scada-01 leitura de nível; eng-ws-15 → KW-04 download de projeto; jump-01 → hist-02 SSH; hist-02 → servidor corporativo de relatórios exportação CSV. *Passos:* classificar cada um como controle, monitoramento ou gerência (ou uma combinação) e declarar a pior consequência se uma parte não autorizada pudesse alterá-lo. *Evidência esperada:* uma tabela de cinco linhas. *Rubrica:* 3 = classes corretas, com o download de projeto reconhecido como a ação de gerência mais perigosa e a exportação CSV reconhecida como um fluxo de monitoramento entre zonas; 2 = uma classificação errada; 1 = classes sem consequências; 0 = nada.

**EX002 — Conserte o ciclo no papel.** *Objetivo:* usar o modelo de ciclo de varredura. *Insumos:* Laboratório 1. *Passos:* propor duas mudanças que levem o ciclo sequencial abaixo de 5 s com todas as estações saudáveis e dizer qual também limita o efeito de uma estação morta. Alterar o laboratório para testá-las. *Evidência esperada:* parâmetros modificados e os novos tempos de ciclo impressos. *Rubrica:* 3 = mudanças realistas (canais separados para os tipos de enlace lentos, menos varreduras por ciclo para as estações lentas, um timeout mais curto com uma política de novas tentativas justificada) e verificadas executando o laboratório; 2 = corretas, mas não verificadas; 1 = apenas "comprar enlaces mais rápidos"; 0 = nada.

**EX003 — Impacto do túnel.** *Objetivo:* verificar um controle de segurança frente a um orçamento operacional. *Insumos:* um túnel criptografado proposto acrescenta 35 ms a cada ida e volta nas cinco estações celulares. *Passos:* calcular o efeito sobre o ciclo sequencial e sobre o desenho com um canal por estação. *Evidência esperada:* aritmética e uma recomendação. *Rubrica:* 3 = aumentos corretos (5 estações × 4 varreduras × 35 ms = 0,70 s no sequencial; 0,14 s no ciclo próprio da estação celular mais lenta) e uma recomendação que vincula o túnel ao novo desenho dos canais; 2 = aritmética certa, recomendação fraca; 1 = apenas qualitativo; 0 = nada.

**EX004 — Lista de plataformas compartilhadas.** *Objetivo:* encontrar dependências entre serviços. *Insumos:* a descrição do KVROC e o seu diagrama. *Passos:* listar quatro componentes que provavelmente são compartilhados pelos serviços de água, hospital e rede elétrica e, para cada um, a primeira pergunta que você faria ao dono. *Evidência esperada:* quatro linhas. *Rubrica:* 3 = por exemplo, hosts de virtualização, diretório, fonte de tempo e coletor de monitoramento, cada um com uma pergunta específica (folga de capacidade, grupo administrativo, redundância da fonte de tempo, comportamento quando cheio); 2 = perguntas genéricas; 1 = apenas componentes; 0 = nada.

### Síntese do capítulo

Um serviço de setor crítico é um conjunto de camadas unidas por três caminhos. Comandos, medições e mudanças percorrem rotas diferentes e falham de modos diferentes; o caminho de gerência concentra o maior privilégio. A varredura de requisição–resposta faz da atualidade uma questão de aritmética, e são os timeouts, não a largura de banda, que costumam decidi-la. Cada capítulo seguinte acrescenta uma técnica a um desses caminhos; mantenha, portanto, o diagrama e o orçamento à mão.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 18

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- explicar por que a maioria dos protocolos industriais não tem autenticação, e o que isso significa para quem consegue alcançar a porta de um controlador;
- decodificar um quadro Modbus/TCP à mão e em código: cabeçalho MBAP, identificador de unidade, código de função, endereço e quantidade;
- distinguir funções de leitura de funções de escrita e reconhecer as funções de diagnóstico e de identificação que merecem revisão;
- transformar um decodificador numa primeira detecção: escritas vindas de qualquer host que não seja a origem de engenharia autorizada.

O Capítulo 1 desenhou os caminhos. Este capítulo abre os pacotes dos caminhos de controle e de monitoramento, para que os capítulos seguintes possam filtrá-los, verificá-los e detectá-los.

### 2.1 Protocolos industriais e confiança

Protocolos como o Modbus e o DNP3 foram projetados para redes seriais fechadas, em que se presumia que tudo o que estivesse no fio pertencia a elas. Suas versões TCP/IP mantiveram esse pressuposto: um dispositivo Modbus/TCP clássico aceita uma escrita válida de **qualquer** host que consiga abrir uma conexão TCP com a porta 502. Existem variantes seguras — a Modbus Organization publica uma especificação Modbus/TCP Security que usa TLS ([Modbus specifications](https://www.modbus.org/modbus-specifications)), e o DNP3 tem o Secure Authentication ([DNP Users Group overview](https://www.dnp.org/About/Overview-of-DNP3-Protocol)) —, mas os dispositivos instalados muitas vezes não as suportam. Até que suportem, **alcançabilidade é autorização**, e os controles de rede dos Capítulos 10 e 11 são a principal defesa.

### 2.2 O modelo de dados do Modbus

Um dispositivo Modbus expõe quatro tabelas: **coils** (um bit, leitura e escrita), **entradas discretas** (um bit, somente leitura), **registradores de entrada** (16 bits, somente leitura) e **registradores de retenção** (holding registers; 16 bits, leitura e escrita). O que um registrador *significa* — nível em centímetros, um setpoint de bomba, um sinalizador de modo — é definido pela configuração do dispositivo e documentado num **mapa de registradores**. O protocolo em si carrega números, não significados; assim, um decodificador pode lhe dizer "escrita no registrador de retenção 7", mas só o mapa de registradores lhe diz que o registrador 7 é o setpoint da bomba 2.

Os códigos de função públicos comuns são 1 (ler coils), 2 (ler entradas discretas), 3 (ler registradores de retenção), 4 (ler registradores de entrada), 5 (escrever um coil), 6 (escrever um registrador), 15 (escrever vários coils), 16 (escrever vários registradores), 8 (diagnóstico) e 43/14 (ler a identificação do dispositivo). Os códigos de função são definidos na especificação Modbus Application Protocol publicada pela Modbus Organization ([Modbus specifications](https://www.modbus.org/modbus-specifications)).

### 2.3 O cabeçalho MBAP

Sobre TCP, cada requisição Modbus começa com um **cabeçalho MBAP** de 7 bytes, seguido da unidade de dados do protocolo (PDU):

| Bytes | Campo | Observações |
|---|---|---|
| 0–1 | Identificador de transação | Associa uma resposta à sua requisição. |
| 2–3 | Identificador de protocolo | Sempre 0 para o Modbus. |
| 4–5 | Comprimento | Número de bytes que **seguem** este campo (id de unidade + PDU). |
| 6 | Identificador de unidade | Endereça um dispositivo atrás de um gateway; muitas vezes 1 ou 255. |
| 7 | Código de função | O que fazer. |
| 8– | Dados | Para os códigos 1–6: um endereço de 2 bytes e uma quantidade ou valor de 2 bytes. |

Todos os campos de vários bytes são big-endian. O módulo `struct` do Python os decodifica com o formato `>HHHBB` ([Python struct](https://docs.python.org/3/library/struct.html)). O quadro `00 03 00 00 00 06 01 06 00 07 01 2c` se lê, portanto: transação 3, protocolo 0, seguem seis bytes, unidade 1, função 6 (escrever um registrador), registrador 7, valor 0x012C = 300.

Duas verificações de consistência pegam a maior parte do tráfego malformado ou não Modbus na porta 502: o identificador de protocolo deve ser 0, e o campo de comprimento deve ser igual ao número de bytes depois dele. Uma ferramenta de detecção que pula essas verificações vai ler lixo como se fossem comandos.

### 2.4 Exemplo resolvido: uma captura da KW-04 (sintético)

Um técnico exportou oito requisições enviadas à RTU da KW-04 (10.10.4.2) durante uma manhã de manutenção. A política do KVROC diz que só a estação de engenharia `eng-ws-15` (10.20.0.15) pode escrever nos controladores das estações; o `scada-01` (10.20.0.10) apenas lê.

**Laboratório 2** (salve como `lab02.py` e execute com `python3 lab02.py`):

```python
# Lab 2 - decode Modbus/TCP frames and flag writes (offline, standard library only)
# Synthetic capture from Kestrel Water station KW-04; addresses are private (RFC 1918).
import struct
ENGINEERING = {"10.20.0.15"}          # only the engineering workstation may write
WRITE_FC = {5: "write single coil", 6: "write single register",
            15: "write multiple coils", 16: "write multiple registers"}
READ_FC = {1: "read coils", 2: "read discrete inputs", 3: "read holding registers", 4: "read input registers"}
capture = [  # (source, destination, frame as hex)
    ("10.20.0.10", "10.10.4.2", "000100000006010300000004"),
    ("10.20.0.10", "10.10.4.2", "000200000006010400100002"),
    ("10.20.0.15", "10.10.4.2", "00030000000601060007012c"),
    ("10.30.3.7",  "10.10.4.2", "000400000006010500a0ff00"),
    ("10.30.3.7",  "10.10.4.2", "00050000000b011000070002040064000a"),
    ("10.20.0.10", "10.10.4.2", "0006000000060103"),
    ("10.20.0.10", "10.10.4.2", "000700010006010300000004"),
    ("10.20.0.10", "10.10.4.2", "000800000006012b0e010000"),
]
def decode(hexframe):
    b = bytes.fromhex(hexframe)
    if len(b) < 8: return None, "short frame (< 8 bytes)"
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", b[:8])
    if pid != 0: return None, f"protocol id {pid} is not 0 (not Modbus)"
    if length != len(b) - 6: return None, f"length field {length} but {len(b) - 6} bytes follow"
    addr, qty = struct.unpack(">HH", b[8:12]) if len(b) >= 12 else (None, None)
    return (tid, unit, fc, addr, qty), None
for src, dst, h in capture:
    d, err = decode(h)
    if err: print(f"{src:<11} -> {dst}  MALFORMED  {err}"); continue
    tid, unit, fc, addr, qty = d
    if fc in WRITE_FC:
        verdict = "ok (engineering)" if src in ENGINEERING else "ALERT unauthorized write"
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {WRITE_FC[fc]:<24} addr={addr} value/qty={qty}  {verdict}")
    elif fc in READ_FC:
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {READ_FC[fc]:<24} addr={addr} qty={qty}  ok")
    else:
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {'other function':<24}  REVIEW (not on read/write list)")
```

Saída esperada (Python 3.13.5):

```text
10.20.0.10  -> 10.10.4.2  tid=1 unit=1 fc=3  read holding registers   addr=0 qty=4  ok
10.20.0.10  -> 10.10.4.2  tid=2 unit=1 fc=4  read input registers     addr=16 qty=2  ok
10.20.0.15  -> 10.10.4.2  tid=3 unit=1 fc=6  write single register    addr=7 value/qty=300  ok (engineering)
10.30.3.7   -> 10.10.4.2  tid=4 unit=1 fc=5  write single coil        addr=160 value/qty=65280  ALERT unauthorized write
10.30.3.7   -> 10.10.4.2  tid=5 unit=1 fc=16 write multiple registers addr=7 value/qty=2  ALERT unauthorized write
10.20.0.10  -> 10.10.4.2  MALFORMED  length field 6 but 2 bytes follow
10.20.0.10  -> 10.10.4.2  MALFORMED  protocol id 1 is not 0 (not Modbus)
10.20.0.10  -> 10.10.4.2  tid=8 unit=1 fc=43 other function            REVIEW (not on read/write list)
```

Lendo a saída linha a linha: as leituras do SCADA são normais; a estação de engenharia escreveu o valor 300 no registrador 7 — esperado, se houver um chamado de mudança; uma mesa corporativa (10.30.3.7) escreveu ON no coil 160 (0xFF00 = 65280) e depois escreveu dois registradores a partir do 7. Essas duas linhas são a constatação da manhã: um host da zona corporativa consegue alcançar um controlador de estação e alterá-lo. Dois quadros estão malformados — um truncado, outro com identificador de protocolo diferente de zero —, e a função 43 (identificação do dispositivo) não é nem uma leitura de dados do processo nem uma escrita, por isso é marcada para revisão: uma consulta de identificação vinda de um servidor SCADA conhecido pode ser um recurso do fornecedor; a mesma consulta vinda de um host desconhecido é reconhecimento clássico (o MITRE lista a descoberta de informações de sistemas remotos entre as técnicas de ICS: [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 2.5 Atividade prática

Decodifique à mão os três quadros abaixo, depois acrescente-os ao Laboratório 2 e confirme: `000900000006010100000010`, `000a0000000601050003 0000` (remova o espaço), `000b00000006020300640001`. Anote a função, o endereço e a quantidade ou o valor de cada um, e se o identificador de unidade é o que você espera para a KW-04.

Escreva a função, o endereço e a quantidade ou o valor de cada quadro, e se o identificador de unidade corresponde ao que a KW-04 usa. Depois acrescente os quadros ao Laboratório 2 e confirme que a sua decodificação à mão coincide com a do script. Se um quadro tiver um espaço no hexadecimal, remova-o antes de colar; os espaços não fazem parte da captura.

### 2.6 Erros comuns e limites

- Tratar o tráfego da porta 502 como Modbus sem verificar o identificador de protocolo e o comprimento.
- Ler números de registradores como significados sem o mapa de registradores do dispositivo.
- Alertar sobre toda consulta de função 43, ou sobre nenhuma; o contexto (origem, frequência) decide.
- Esquecer que as respostas também importam: uma resposta de exceção (código de função + 0x80) diz que uma requisição foi recusada (Capítulo 12).
- Um decodificador vê apenas o que o ponto de captura vê: o tráfego entre dois dispositivos no mesmo switch de estação nunca chega a um sensor do centro de controle.

- Alertar sobre toda escrita sem verificar se a origem é a estação de engenharia nomeada na política.
- Tratar um quadro malformado como ataque quando ele pode ser uma exportação truncada ou uma sondagem não Modbus; relate-o primeiro como malformado.
- Presumir que um decodificador no centro de controle vê o tráfego entre dois dispositivos no mesmo switch de estação.

### Exercícios — capítulo 2

**EX005 — Decodificação à mão.** *Objetivo:* ler os campos MBAP e PDU sem código. *Insumos:* `0010000000060110000a0002` está truncado; `001100000006010f00000008`. *Passos:* decodificar cada campo que puder e declarar se cada quadro é válido. *Evidência esperada:* tabelas de campos com o raciocínio. *Rubrica:* 3 = reconhece o primeiro como função 16 sem a contagem de bytes e os valores (o comprimento 6 é coerente com o que está presente, mas uma fc 16 válida precisa de mais), e o segundo como função 15 no endereço 0 para 8 coils, também incompleto sem contagem de bytes e dados; 2 = campos certos, validade não percebida; 1 = parcial; 0 = nada.

**EX006 — Estenda o decodificador.** *Objetivo:* melhorar uma ferramenta de detecção. *Insumos:* Laboratório 2. *Passos:* (1) para a função 16, decodificar também a contagem de bytes e os valores dos registradores; (2) imprimir os valores do quadro de 10.30.3.7. *Evidência esperada:* alteração no código e a nova linha de saída. *Rubrica:* 3 = contagem de bytes 4 e valores 100 e 10 impressos, com uma verificação de que a contagem de bytes é igual a 2 × quantidade; 2 = valores sem verificação; 1 = tentativa; 0 = nada.

**EX007 — Política de escrita como dados.** *Objetivo:* expressar uma lista de permissões com precisão. *Insumos:* a política do KVROC. *Passos:* escrever uma lista de permissões com entradas (origem, faixa de destino, códigos de função) para a operação normal e para uma janela de manutenção aprovada, e dizer quem alterna entre elas. *Evidência esperada:* duas tabelas curtas e um responsável. *Rubrica:* 3 = códigos somente de leitura do SCADA para todas as estações; escritas da engenharia apenas para a estação nomeada no chamado e apenas durante a janela; alternância a cargo do plantão do KVROC, com aprovação da Kestrel Water; 2 = sem janela; 1 = vago; 0 = nada.

**EX008 — Reconhecimento ou recurso?** *Objetivo:* raciocinar sobre tráfego ambíguo. *Insumos:* consultas de função 43 do `scada-01` a cada 24 h para todas as estações, e a mesma consulta de 10.20.0.31 para quatro estações em três segundos. *Passos:* decidir qual exige ação e o que você verificaria primeiro. *Evidência esperada:* uma nota curta. *Rubrica:* 3 = a consulta diária do SCADA tratada como provável recurso de inventário, a confirmar com o fornecedor; a rajada de um host desconhecido tratada como constatação prioritária — identificar 10.20.0.31 (o Capítulo 17 volta a ele) sem sondá-lo; 2 = prioridade certa, verificações fracas; 1 = ambas ignoradas ou ambas alarmadas; 0 = nada.

### Síntese do capítulo

Os protocolos industriais clássicos confiam em quem consegue alcançá-los; portanto, a posição na rede é autoridade. Os quadros Modbus/TCP têm uma estrutura fixa e verificável; decodificá-los corretamente — incluindo as verificações de comprimento e de protocolo — é a base de todo filtro e detecção posteriores. Escritas vindas do lugar errado são a primeira regra; funções de identificação e de diagnóstico precisam de contexto; e um decodificador só vê o que o seu ponto de captura vê.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 18

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- auditar um host Linux que dá suporte a um serviço de controle: serviços em escuta, configurações do daemon SSH, contas locais e grupos privilegiados;
- explicar por que o `sshd` adota o **primeiro** valor que lê para a maioria das palavras-chave, e como isso derrota edições descuidadas;
- identificar contas equivalentes a root, contas de serviço com shells interativos e contas que nenhuma pessoa atual possui;
- transformar as constatações numa mudança de endurecimento priorizada que não tranque os operadores do lado de fora.

Os Capítulos 1–2 descreveram o serviço e o seu tráfego. Os servidores do centro de controle — historiador, servidor SCADA, host de salto — executam sistemas operacionais comuns; este capítulo torna a configuração deles algo que você pode verificar, e não presumir.

### 3.1 O que endurecimento significa no nível do técnico

Endurecer é remover o que não é necessário e restringir o que é. Para um servidor num ambiente de controle, isso significa: serviços escutando apenas nas interfaces de que precisam; acesso administrativo apenas pelo caminho de gerência; nenhuma conta compartilhada ou órfã; contas de serviço que não conseguem fazer login interativo; e uma configuração registrada, para que a deriva possa ser detectada (Capítulo 14). O guia geral de servidores do NIST dá a lista de verificação mais ampla ([SP 800-123](https://csrc.nist.gov/pubs/sp/800/123/final)); as Cross-Sector Cybersecurity Performance Goals da CISA resumem as práticas de contas e credenciais que mais costumam faltar ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)).

### 3.2 Ler corretamente a configuração do sshd

O daemon do OpenSSH lê o `sshd_config` de cima para baixo e, para a maioria das palavras-chave, **o primeiro valor obtido é o usado**; as linhas posteriores para a mesma palavra-chave são ignoradas ([sshd_config(5)](https://man.openbsd.org/sshd_config)). Os comentários começam com `#`. Assim, um arquivo que tem `PasswordAuthentication yes` perto do topo e a correção posterior de alguém, `PasswordAuthentication no`, no final continua permitindo senhas. A verificação confiável é a configuração efetiva: num host real, `sshd -T` a imprime; no Laboratório 3, o analisador guarda o primeiro valor, como faz o daemon.

Configurações que importam num host do centro de controle: `ListenAddress` restrito à interface de gerência; `PermitRootLogin no`; `PasswordAuthentication no` assim que chaves ou certificados funcionarem; `X11Forwarding no`; um `MaxAuthTries` baixo; e `AllowGroups` nomeando um grupo cujos membros você também revisa.

### 3.3 Contas e identidades

No Linux, privilégio é um número: **UID 0** é root, seja qual for o nome da conta. Uma conta extra com UID 0 ("backup2", "support") é uma segunda senha de root que ninguém troca. **Contas de serviço** (UIDs abaixo de 1000 por convenção em muitas distribuições) executam daemons; devem ter um shell não interativo como `/usr/sbin/nologin`, para que uma credencial de serviço roubada não possa ser usada para fazer login. **Contas de pessoas** devem corresponder a alguém da lista atual de autorizações; uma conta de fornecedor que fica permanentemente no `sudo` é um privilégio permanente que deveria ter prazo (Capítulo 10). A participação em grupos faz parte da identidade: estar no `sudo` ou no `ops-admins` muitas vezes importa mais do que a própria conta.

### 3.4 Exemplo resolvido: auditoria do HIST-02 (sintético)

O `hist-02` armazena as séries temporais da Kestrel Water. Política do KVROC: SSH apenas no endereço de gerência 10.90.0.21; nenhum login de root; apenas chaves; no máximo três tentativas; apenas J. Tan e R. Kaur autorizados.

**Laboratório 3** (salve como `lab03.py` e execute com `python3 lab03.py`):

```python
# Lab 3 - audit a host configuration and its local accounts (offline, standard library only)
# Synthetic files from historian host HIST-02 at the Kestrel Vale operations centre.
sshd_config = """
Port 22
ListenAddress 0.0.0.0
PermitRootLogin yes
PasswordAuthentication yes
# PasswordAuthentication no
PubkeyAuthentication yes
X11Forwarding yes
MaxAuthTries 6
AllowGroups ops-admins
"""
passwd = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
histsvc:x:998:998:historian service:/opt/hist:/bin/bash
jtan:x:1001:1001:J. Tan:/home/jtan:/bin/bash
rkaur:x:1002:1002:R. Kaur:/home/rkaur:/bin/bash
backup2:x:0:0:temp backup:/root:/bin/bash
vendor:x:1003:1003:vendor support:/home/vendor:/bin/bash"""
group = """ops-admins:x:1100:jtan,vendor
sudo:x:27:jtan,rkaur,vendor"""
policy = {"PermitRootLogin": "no", "PasswordAuthentication": "no", "X11Forwarding": "no",
          "ListenAddress": "10.90.0.21", "MaxAuthTries": "3"}
roster = {"jtan", "rkaur"}                     # people currently authorized on HIST-02
eff = {}
for line in sshd_config.splitlines():
    line = line.split("#", 1)[0].strip()
    if not line: continue
    key, val = line.split(None, 1)
    eff.setdefault(key, val)                   # sshd uses the FIRST value it reads for a keyword
findings = []
for k, want in policy.items():
    if eff.get(k) != want: findings.append(f"sshd {k} is {eff.get(k)!r}, policy {want!r}")
for line in passwd.splitlines():
    name, _, uid, gid, gecos, home, shell = line.split(":")
    if uid == "0" and name != "root": findings.append(f"account {name} has UID 0 (root equivalent)")
    if 0 < int(uid) < 1000 and shell.endswith("sh") and not shell.endswith("nologin"):
        findings.append(f"service account {name} has interactive shell {shell}")
    if int(uid) >= 1000 and name not in roster: findings.append(f"person account {name} not on roster")
for line in group.splitlines():
    g, _, _, members = line.split(":")
    for m in members.split(","):
        if m and m not in roster: findings.append(f"group {g} contains {m} (not on roster)")
for f in findings: print(f)
print("findings:", len(findings))
```

Saída esperada (Python 3.13.5):

```text
sshd PermitRootLogin is 'yes', policy 'no'
sshd PasswordAuthentication is 'yes', policy 'no'
sshd X11Forwarding is 'yes', policy 'no'
sshd ListenAddress is '0.0.0.0', policy '10.90.0.21'
sshd MaxAuthTries is '6', policy '3'
service account histsvc has interactive shell /bin/bash
account backup2 has UID 0 (root equivalent)
person account vendor not on roster
group ops-admins contains vendor (not on roster)
group sudo contains vendor (not on roster)
findings: 10
```

Dez constatações. Repare na linha `PasswordAuthentication`: o arquivo contém um `no` comentado, que alguns revisores leem como "já corrigido". É um comentário, e o valor efetivo é `yes`. As constatações mais perigosas são `backup2` com UID 0 (um segundo root não gerenciado) e `vendor` no `sudo` (acesso privilegiado permanente de fornecedor). A conta de serviço do historiador com `/bin/bash` importa porque as credenciais do serviço ficam armazenadas em disco para o historiador usá-las.

Uma ordem segura de endurecimento: (1) confirmar um login funcional por chave para J. Tan e R. Kaur a partir do `jump-01`; (2) restringir `ListenAddress`, `PermitRootLogin` e `PasswordAuthentication` numa única mudança, mantendo uma sessão existente aberta enquanto testa uma nova; (3) remover `backup2` depois de preservar o seu histórico de logins; (4) remover `vendor` do `sudo` e passar o acesso do fornecedor para um procedimento com prazo; (5) definir o shell da conta de serviço como `nologin` depois de verificar que nenhum script de manutenção faz login com ela.

### 3.5 Atividade prática

Numa máquina virtual sua, execute `sshd -T | sort` e compare a saída com o arquivo. Acrescente uma palavra-chave duplicada mais abaixo no arquivo, recarregue e confirme que o primeiro valor vence. Registre a versão exata do OpenSSH, porque o comportamento dos blocos `Include` e `Match` varia conforme a versão.

Registre a versão do OpenSSH e o caminho de cada arquivo que o `sshd -T` mostra como incluído. Depois de recarregar, abra uma segunda sessão antes de fechar a primeira, para que uma mudança ruim em ListenAddress ou AllowGroups não possa trancá-lo do lado de fora. Compare os valores efetivos com a tabela de política do Laboratório 3 e anote qualquer palavra-chave que apareça duas vezes no arquivo.

### 3.6 Erros comuns e limites

- Ler o arquivo em vez da configuração efetiva.
- Corrigir as configurações do SSH a partir da única sessão aberta e trancar todos do lado de fora; sempre teste antes uma segunda sessão.
- Verificar nomes de contas em vez de UIDs.
- Remover o shell de uma conta de serviço sem verificar os scripts que dependem dele.
- O Laboratório 3 não trata arquivos `Include` nem blocos `Match`; auditorias reais precisam tratar.

- Editar PasswordAuthentication no final do arquivo enquanto um yes anterior continua vencendo.
- Remover vendor do sudo sem um procedimento com prazo para a próxima visita de suporte.
- Verificar nomes de contas em vez de UIDs, de modo que um segundo root chamado backup2 passa despercebido.

### Exercícios — capítulo 3

**EX009 — O primeiro valor vence.** *Objetivo:* raciocinar sobre a configuração efetiva. *Insumos:* o `sshd_config` do Laboratório 3. *Passos:* (1) prever o `PasswordAuthentication` efetivo se a linha comentada for descomentada e deixada onde está; (2) dizer onde a correção precisa ficar. *Evidência esperada:* previsão e posição. *Rubrica:* 3 = continua `yes`, porque a linha anterior vence; a correção substitui a primeira ocorrência (ou a linha anterior é apagada), verificada com `sshd -T`; 2 = resposta certa, sem verificação; 1 = prevê `no`; 0 = nada.

**EX010 — Priorize as constatações do HIST-02.** *Objetivo:* ordenar as mudanças por risco e segurança. *Insumos:* a saída do Laboratório 3. *Passos:* agrupar as dez constatações em hoje / esta semana / próxima janela de manutenção, com justificativas de uma linha e uma etapa de preservação onde necessário. *Evidência esperada:* uma lista em três grupos. *Rubrica:* 3 = `backup2` com UID 0 e `vendor` no sudo hoje, com o histórico de logins preservado antes; vinculação do SSH e configurações de root/senha como uma única mudança testada; shell do serviço depois da verificação dos scripts; 2 = sensata, mas sem preservação; 1 = sem ordem; 0 = nada.

**EX011 — Estenda a auditoria.** *Objetivo:* acrescentar uma verificação. *Insumos:* Laboratório 3. *Passos:* acrescentar uma verificação que sinalize qualquer conta diferente de `root` cujo shell seja interativo e cujo diretório pessoal seja `/root` ou `/`. Relatar a nova saída. *Evidência esperada:* código e saída. *Rubrica:* 3 = sinaliza `backup2` (diretório `/root`) e somente ela; explica por que diretórios pessoais compartilhados escondem a responsabilização; 2 = funciona, sem explicação; 1 = tentativa; 0 = nada.

**EX012 — Desenho de conta de serviço.** *Objetivo:* desenhar uma identidade não interativa. *Insumos:* o serviço do historiador precisa ler arquivos em `/opt/hist` e escrever no seu banco de dados. *Passos:* especificar a faixa de UID, o shell, o diretório pessoal, o grupo, as permissões de arquivo e como sua credencial é armazenada e trocada. *Evidência esperada:* uma especificação curta. *Rubrica:* 3 = UID de sistema, shell `nologin`, grupo dedicado, modos de arquivo de privilégio mínimo, credencial legível apenas pelo serviço, responsável e intervalo de troca; 2 = uma lacuna; 1 = genérica; 0 = nada.

### Síntese do capítulo

O endurecimento do sistema operacional é verificável: configurações efetivas, UIDs, shells e participação em grupos podem ser lidos e comparados com uma política escrita. Saiba como o daemon realmente lê o seu arquivo, olhe os números em vez dos nomes e ordene as mudanças de modo a nunca trancar do lado de fora as pessoas que operam o serviço.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 18

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- analisar dados operacionais em CSV e JSON com a biblioteca padrão, sem divisão de strings escrita à mão;
- validar cada registro frente a um esquema explícito: número de campos, unidades, forma numérica, finitude, formato de timestamp e faixa física;
- relatar cada problema com as suas **coordenadas de registro** (arquivo e linha), para que outra pessoa possa encontrá-lo;
- escolher entre **rejeitar** e **pôr em quarentena**, e resumir os resultados num formato legível por máquina.

Os scripts do técnico nos capítulos seguintes — decodificadores, auditores, detectores — leem todos dados produzidos por outra pessoa. Este capítulo os torna rigorosos quanto ao que aceitam, porque um script que "conserta" silenciosamente uma entrada ruim produz respostas erradas com confiança.

### 4.1 Formatos que você vai encontrar

- **CSV** — exportações de historiadores, IHMs e planilhas. A RFC 4180 descreve o formato comum, incluindo as aspas: um campo que contém uma vírgula precisa estar entre aspas duplas ([RFC 4180](https://www.rfc-editor.org/rfc/rfc4180)). Dividir linhas nas vírgulas quebra no primeiro valor entre aspas; use o `csv.reader`, que também acompanha o `line_num`.
- **JSON** — APIs, exportações de configuração e saída de ferramentas ([RFC 8259](https://www.rfc-editor.org/rfc/rfc8259)). Use `json.loads`; note que o analisador do Python aceita os tokens não padronizados `NaN` e `Infinity`, a menos que você passe `parse_constant` para rejeitá-los.
- **Timestamps** — use RFC 3339 / ISO 8601 com deslocamento explícito, de preferência UTC com `Z` ([RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)). Um timestamp sem deslocamento é ambíguo em até um dia e nas mudanças de horário de verão.
- **Quadros binários** — a decodificação com `struct` do Capítulo 2; sempre verifique os comprimentos antes de desempacotar.

### 4.2 Uma ordem de validação que falha fechada

Verifique numa ordem em que cada etapa possa presumir que as anteriores passaram:

1. **Estrutura**: o número certo de campos. Se não, nada mais no registro é confiável — rejeitar.
2. **Identidade e tipo**: estação e tag conhecidas; unidade conforme o esquema (um nível em pés não é um nível em metros); o valor é interpretável como número.
3. **Finitude**: `float("nan")` e `float("inf")` são interpretados com sucesso, mas não são medições — rejeitar.
4. **Tempo**: o timestamp é interpretado no formato combinado; não está no futuro além de uma pequena tolerância.
5. **Plausibilidade**: o valor está dentro da faixa física do instrumento e do processo.

**Rejeite** o que não pode ser interpretado (estrutura errada, unidade errada, não é número). **Ponha em quarentena** o que é interpretável, mas implausível (fora da faixa, tempo futuro): uma falha real de sensor e um ataque real se parecem com isso, e um operador precisa vê-lo, em vez de vê-lo descartado em silêncio. Nunca force a conversão: transformar `"12,5"` em 12,5 ou 125 adivinhando o separador decimal cria dados que nunca foram medidos.

### 4.3 Coordenadas de registro

Toda constatação deve dizer de onde veio — arquivo, linha e campo —, para que outra pessoa possa verificá-la. O `csv.reader.line_num` conta as linhas físicas lidas até então, incluindo o cabeçalho, de modo que a primeira linha de dados é a linha 2. Campos entre aspas que contêm quebras de linha fazem as linhas físicas diferirem dos registros; o `line_num` informa a linha em que o registro terminou, o que continua sendo uma coordenada utilizável.

Quando colar uma constatação num chamado, mantenha o número da linha junto ao nome da estação, para que a próxima pessoa possa abrir a exportação e ir direto à linha. Se um campo entre aspas ocupar várias linhas, diga isso, porque a coordenada passa a marcar o fim do registro, e não o seu início.

### 4.4 Exemplo resolvido: validar uma exportação de estações (sintético)

Uma exportação do historiador da Kestrel Water lista uma leitura por estação. O momento da análise é 06:00Z de 12 de outubro de 2026.

**Laboratório 4** (salve como `lab04.py` e execute com `python3 lab04.py`):

```python
# Lab 4 - validate a telemetry export with record coordinates (offline, standard library only)
# Synthetic CSV export from Kestrel Water stations; "now" is 2026-10-12T06:00:00Z.
import csv, io, json, math
from datetime import datetime, timezone
export = """station,tag,value,unit,ts
KW-01,LEVEL_M,3.42,m,2026-10-12T05:58:00Z
KW-02,CL2_MGL,0.61,mg/L,2026-10-12T05:58:00Z
KW-03,LEVEL_M,,m,2026-10-12T05:58:00Z
KW-04,CL2_MGL,7.9,mg/L,2026-10-12T05:58:00Z
KW-05,FLOW_LS,"12,5",L/s,2026-10-12T05:58:00Z
KW-06,LEVEL_M,2.10,ft,2026-10-12T05:58:00Z
KW-07,LEVEL_M,2.95,m,2026-10-12 05:58
KW-08,LEVEL_M,nan,m,2026-10-12T05:58:00Z
KW-09,FLOW_LS,41.0,L/s,2026-10-12T07:15:00Z
KW-10,LEVEL_M,1.88,m,2026-10-12T05:58:00Z,extra
"""
SCHEMA = {"LEVEL_M": ("m", 0.0, 12.0), "CL2_MGL": ("mg/L", 0.0, 5.0), "FLOW_LS": ("L/s", 0.0, 400.0)}
now = datetime(2026, 10, 12, 6, 0, tzinfo=timezone.utc)
result = {"accept": [], "reject": [], "quarantine": []}
reader = csv.reader(io.StringIO(export))
header = next(reader)
for row in reader:
    where = f"line {reader.line_num}"
    if len(row) != len(header): result["reject"].append((where, f"{len(row)} fields, expected {len(header)}")); continue
    r = dict(zip(header, row))
    unit, lo, hi = SCHEMA[r["tag"]]
    if r["unit"] != unit: result["reject"].append((where, f"{r['station']} unit {r['unit']!r}, expected {unit!r}")); continue
    try: v = float(r["value"])
    except ValueError: result["reject"].append((where, f"{r['station']} value {r['value']!r} not a number")); continue
    if not math.isfinite(v): result["reject"].append((where, f"{r['station']} value not finite")); continue
    try:
        ts = datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError: result["reject"].append((where, f"{r['station']} timestamp {r['ts']!r} not RFC 3339 UTC")); continue
    if ts > now: result["quarantine"].append((where, f"{r['station']} timestamp {(ts - now).seconds // 60} min in the future")); continue
    if not lo <= v <= hi: result["quarantine"].append((where, f"{r['station']} {r['tag']}={v} outside {lo}-{hi}")); continue
    result["accept"].append((where, r["station"]))
for k in ("reject", "quarantine"):
    for where, why in result[k]: print(f"{k:<10} {where:<8} {why}")
print(json.dumps({k: len(v) for k, v in result.items()}))
```

Saída esperada (Python 3.13.5):

```text
reject     line 4   KW-03 value '' not a number
reject     line 6   KW-05 value '12,5' not a number
reject     line 7   KW-06 unit 'ft', expected 'm'
reject     line 8   KW-07 timestamp '2026-10-12 05:58' not RFC 3339 UTC
reject     line 9   KW-08 value not finite
reject     line 11  6 fields, expected 5
quarantine line 5   KW-04 CL2_MGL=7.9 outside 0.0-5.0
quarantine line 10  KW-09 timestamp 75 min in the future
{"accept": 2, "reject": 6, "quarantine": 2}
```

Só duas das dez linhas são aceitas. Cada rejeição nomeia a sua linha: um valor vazio (linha 4), uma vírgula decimal dentro de um campo entre aspas (linha 6), um nível em pés (linha 7), um timestamp sem segundos nem deslocamento (linha 8), `nan` (linha 9) e um campo a mais (linha 11). As linhas em quarentena são as interessantes: cloro a 7,9 mg/L está fora da faixa do instrumento — uma falha de sensor, um erro de escala ou um valor manipulado —, e o timestamp da KW-09 está 75 minutos no futuro, o que, no Capítulo 7, você aprenderá a suspeitar ser um problema de relógio. Ambas são passadas a uma pessoa, com as suas coordenadas.

O resumo em JSON na última linha é deliberadamente legível por máquina, para que um job de monitoramento possa alertar quando a contagem de rejeições subir.

### 4.5 Atividade prática

Acrescente ao Laboratório 4 uma verificação de identidade da estação: só KW-01 a KW-12 são válidas. Depois acrescente uma linha `KW-13,LEVEL_M,2.0,m,2026-10-12T05:58:00Z` e confirme que ela é rejeitada com o seu número de linha. Por fim, faça o analisador de timestamps aceitar um deslocamento explícito `+00:00`, além de `Z`, sem aceitar timestamps ingênuos (sem fuso).

Rejeite a KW-13 com o seu número de linha e um motivo que nomeie o conjunto permitido. Para os timestamps, aceite tanto Z quanto um deslocamento explícito de mais zero, e continue rejeitando um horário local sem fuso. Execute o laboratório de novo e confirme que a contagem de rejeições do resumo em JSON aumenta em um para a nova estação.

### 4.6 Erros comuns e limites

- Dividir o CSV nas vírgulas.
- Forçar a conversão de valores ambíguos em vez de rejeitá-los.
- Deixar `nan` passar porque `nan > hi` é falso.
- Aceitar timestamps ingênuos e presumir horário local.
- Relatar "6 rejeitados" sem coordenadas, o que ninguém consegue verificar.
- O Laboratório 4 verifica leituras isoladas; taxa de variação e valores travados exigem uma série (Capítulo 8).

- Deixar nan passar porque as comparações com ele são falsas, de modo que uma verificação de faixa nunca dispara.
- Relatar apenas totais, sem coordenadas, de modo que ninguém consegue encontrar as linhas ruins.
- Converter à força uma vírgula decimal num float e gravar o valor inventado no historiador.

### Exercícios — capítulo 4

**EX013 — Preveja antes de executar.** *Objetivo:* raciocinar sobre o validador. *Insumos:* o Laboratório 4 com três novas linhas: `KW-11,LEVEL_M,12.0,m,2026-10-12T05:59:00Z`; `KW-12,LEVEL_M,inf,m,2026-10-12T05:59:00Z`; `KW-02,CL2_MGL,-0.0,mg/L,2026-10-12T05:59:00Z`. *Passos:* prever cada veredito e o novo resumo, depois executar. *Evidência esperada:* previsões, saída real, explicação de qualquer surpresa. *Rubrica:* 3 = aceitar, rejeitar (não finito), aceitar; resumo `{"accept": 4, "reject": 7, "quarantine": 2}`; observa que −0,0 deveria ser normalizado; 2 = um errado, mas explicado; 1 = palpites; 0 = nada.

**EX014 — Rejeitar ou pôr em quarentena?** *Objetivo:* aplicar a distinção. *Insumos:* (a) vazão de −3,0 L/s; (b) unidade "M" em vez de "m"; (c) nível de 11,9 m num tanque de 12 m; (d) timestamp 4 s no futuro. *Passos:* decidir e justificar. *Evidência esperada:* quatro vereditos. *Rubrica:* 3 = (a) quarentena (interpretável, implausível; pode ser fluxo reverso ou offset); (b) rejeitar, ou normalizar apenas se o esquema permitir explicitamente unidades sem distinção de maiúsculas — não adivinhar; (c) aceitar, talvez com um alarme de nível alto; (d) aceitar dentro de uma tolerância de relógio combinada; 2 = um fraco; 1 = rejeita todos; 0 = nada.

**EX015 — JSON com armadilhas.** *Objetivo:* endurecer a análise de JSON. *Insumos:* `{"station": "KW-03", "value": NaN}`. *Passos:* mostrar o que o `json.loads` devolve por padrão e escrever a mudança de uma linha que o rejeita. *Evidência esperada:* código e comportamento. *Rubrica:* 3 = por padrão devolve um float `nan`; `json.loads(s, parse_constant=lambda c: (_ for _ in ()).throw(ValueError(c)))` ou uma função equivalente que lança exceção; explica que a RFC 8259 não permite NaN; 2 = funciona, sem explicação; 1 = tentativa; 0 = nada.

**EX016 — Resumo para monitoramento.** *Objetivo:* desenhar um resultado legível por máquina. *Insumos:* Laboratório 4. *Passos:* estender o resumo em JSON com contagens por motivo e por estação e propor uma condição de alerta sobre ele. *Evidência esperada:* JSON de exemplo e a condição. *Rubrica:* 3 = chaves estáveis, contagens por motivo, alerta como "qualquer quarentena de CL2_MGL, ou rejeições > 10 % das linhas em duas exportações consecutivas"; 2 = sem divisão por motivo; 1 = apenas prosa; 0 = nada.

### Síntese do capítulo

Os dados operacionais chegam malformados, ambíguos e, às vezes, hostis. Analise com analisadores de verdade, valide numa ordem que falhe fechada, nunca force conversões e relate cada constatação com coordenadas. Rejeite o que não consegue interpretar; ponha em quarentena o que consegue interpretar, mas não deveria acreditar; e mantenha os resumos legíveis por máquina, para que o próprio validador possa ser monitorado.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 18

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Escopo de segurança e evidências

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- escrever um **escopo técnico** para uma tarefa num ambiente crítico: sistemas, ações permitidas, janela de tempo, contatos e condições de parada;
- explicar por que, em tecnologia operacional, uma observação passiva é preferida e uma ativa precisa de aprovação explícita;
- coletar evidências técnicas de modo que outra pessoa possa verificá-las: o quê, de onde, quando (UTC), por quem, como, e o seu hash;
- separar **observado**, **inferido**, **feito** e **em aberto** em toda nota de trabalho.

Os Capítulos 1–4 lhe deram ferramentas. Antes de apontar qualquer uma delas para um sistema real, este capítulo define o que você tem permissão para tocar e como vai provar o que viu.

### 5.1 Escopo é um controle de segurança

Numa rede de escritório, uma varredura afobada desperdiça tempo. Numa rede de controle, ela pode parar um processo: alguns controladores e pilhas de rede mais antigas se comportam mal quando sondados, e uma "leitura" pode disparar diagnósticos do fornecedor ou encher uma tabela de sessões. O guia de TO do NIST recomenda cautela com a varredura ativa em ambientes operacionais e prefere métodos passivos sempre que possível ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); o guia de testes do NIST descreve regras de engajamento para qualquer avaliação ([SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)).

Um escopo técnico responde, por escrito, antes de o trabalho começar:

- **Propósito** — que pergunta o trabalho responde.
- **Sistemas no escopo** — hosts e endereços nomeados; todo o resto fica fora.
- **Ações permitidas** — por exemplo, "ler a configuração em execução", "captura passiva na porta SPAN", "um teste de conexão TCP à porta 502, sem requisição Modbus".
- **Janela** — data e horários, com a concordância do operador.
- **Pessoas** — quem autorizou (o dono do sistema), quem está no local, quem na sala de controle é informado.
- **Condições de parada** — qualquer comportamento inesperado de dispositivo, alarme ou pedido das operações.
- **Tratamento das evidências** — onde os resultados ficam armazenados e quem pode lê-los.

### 5.2 Passivo primeiro

Muitas perguntas podem ser respondidas sem enviar um pacote: exportações de configuração, logs de firewall, tabelas MAC de switches, uma captura passiva de uma porta espelho (SPAN), os próprios registros do historiador. Prefira esses. Quando um teste ativo for realmente necessário — por exemplo, para verificar uma regra de bloqueio no Capítulo 11 —, faça o menor teste que responda à pergunta, a partir de uma origem nomeada, num horário combinado.

Prefira uma captura SPAN ou uma exportação de configuração antes de qualquer teste de conexão. Quando um teste ativo for necessário, use um endereço de origem identificado, a menor ação que responda à pergunta e uma janela combinada, com as operações informadas no início e no fim.

### 5.3 O que torna utilizáveis as evidências técnicas

Uma captura de tela de um terminal prova pouco. Evidências utilizáveis registram:

1. **O quê** — a saída ou o arquivo bruto, não um resumo.
2. **Origem** — host e ferramenta, com versão.
3. **Tempo** — em UTC, com o deslocamento do relógio do host, se conhecido (Capítulo 7).
4. **Coletor** — quem executou.
5. **Método** — o comando ou a consulta exatos.
6. **Integridade** — um hash SHA-256 registrado no momento da coleta, para que cópias posteriores possam ser conferidas ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)); o Capítulo 18 sela um pacote inteiro.

O guia do NIST sobre a integração de técnicas forenses à resposta a incidentes discute a ordem de coleta e de preservação ([SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final)). No nível do técnico, a regra é simples: **preserve antes de mudar**. Se você está prestes a consertar algo que pode ser evidência de uso indevido, colete-o primeiro.

### 5.4 Quatro rótulos

Toda nota que você escreve neste curso usa quatro rótulos. **Observado**: o que uma ferramenta ou pessoa registrou, com origem e horário. **Inferido**: o que você conclui, e por quê. **Feito**: o que você mudou, sob qual registro de mudança. **Em aberto**: o que continua desconhecido, e quem é o responsável. Misturá-los — "a RTU foi comprometida", quando você observou apenas uma sessão de configuração — é como se espalham as conclusões erradas.

Uma nota que diz apenas "RTU comprometida" falha no teste: mistura inferência com observação. Escreva os quatro rótulos em toda nota de trabalho deste curso, incluindo a verificação de alcançabilidade da KW-04, para que o leitor possa ver o que foi medido e o que continua em aberto.

### 5.5 Exemplo resolvido: o escopo da verificação da KW-04 (sintético)

Depois que o Laboratório 2 mostrou escritas vindas de uma mesa corporativa, L. Ferreira (líder de segurança do KVROC) pede que você confirme se a zona corporativa consegue alcançar a porta 502 das estações. Um escopo sólido:

| Elemento | Conteúdo |
|---|---|
| Propósito | Confirmar ou refutar a alcançabilidade da zona corporativa até tcp/502 da KW-04. |
| No escopo | Configuração e logs do fw-01 (leitura); uma conexão TCP da mesa de testes 10.30.99.9 para 10.10.4.2:502, sem carga Modbus. |
| Fora do escopo | Todas as outras estações; qualquer requisição Modbus; a mesa 10.30.3.7 (preservar, não tocar). |
| Janela | 13 out. 2026, 10:00–10:30, horário local, combinada com A. Mensah (operações da Kestrel Water). |
| Pessoas | Autorizador A. Mensah; operador da sala de controle da Kestrel Water informado no início e no fim. |
| Parada | Qualquer alarme da KW-04, perda de comunicação ou pedido do operador. |
| Evidências | Exportação da configuração do firewall, saída do teste de conexão, linhas de log do fw-01; hashes na pasta do caso. |

A nota de trabalho depois do teste diz: *Observado* — conexão de 10.30.99.9 para 10.10.4.2:502 concluída às 08:04:11Z; o fw-01 registrou permissão pela regra R4. *Inferido* — os hosts corporativos conseguem alcançar o Modbus das estações por causa da R4 (Capítulo 10). *Feito* — nada foi mudado. *Em aberto* — quem criou a R4 e por quê (responsável: L. Ferreira).

### 5.6 Atividade prática

Escreva um escopo para uma captura passiva de 24 horas na porta SPAN do switch do centro de controle. Inclua limites de armazenamento e quem pode ler a captura, já que ela conterá valores do processo e possivelmente credenciais enviadas em texto claro.

Declare um tamanho máximo de arquivo e um período de retenção, porque um dia de valores do processo e de credenciais em texto claro é, ao mesmo tempo, grande e sensível. Nomeie quem pode ler a captura e onde ela fica armazenada, e diga que a captura para se a porta espelho do switch afetar o encaminhamento. Marque a atividade como passiva e liste condições de parada que incluam qualquer pedido do operador.

### 5.7 Erros comuns e limites

- Começar o trabalho com um "pode ir" verbal.
- Varrer uma sub-rede para "ver o que tem lá" numa rede de controle.
- Coletar evidências sem horários em UTC nem hashes.
- Consertar primeiro e coletar depois.
- Tratar o escopo como burocracia: é ele que impede que um teste vire um incidente.

- Começar a partir de um "pode ir" verbal e escrever o escopo depois.
- Varrer uma sub-rede numa rede de controle para descobrir dispositivos.
- Consertar uma constatação antes de coletar as evidências que a mostraram. Um escopo escrito depois do trabalho não pode proteger o processo durante ele.

### Exercícios — capítulo 5

**EX017 — Conserte um escopo.** *Objetivo:* encontrar os elementos que faltam. *Insumos:* "Rodar uma varredura em 10.10.0.0/16 na terça para achar portas abertas. Aprovado pela TI." *Passos:* listar cada defeito e reescrever. *Evidência esperada:* lista de defeitos e escopo reescrito. *Rubrica:* 3 = identifica o autorizador errado (é preciso o dono do sistema), a faixa ilimitada, a varredura ativa em TO, a falta de janela, de condições de parada e de tratamento das evidências; a reescrita prefere fontes passivas de inventário; 2 = a maioria dos defeitos; 1 = cosmético; 0 = nada.

**EX018 — Rotule a nota.** *Objetivo:* separar observação e inferência. *Insumos:* "O fornecedor hackeou a KW-09 ontem à noite — a configuração da RTU mudou e os dados pararam, então eu a reiniciei." *Passos:* reescrever com os quatro rótulos. *Evidência esperada:* nota rotulada. *Rubrica:* 3 = observado (horário da sessão de configuração, lacuna nos dados), inferido (possível mudança não aprovada; autoria desconhecida), feito (reinício — e a perda de evidências que ele causou), em aberto (quem, por quê; responsável); 2 = rótulos sem perceber a perda de evidências; 1 = parcial; 0 = nada.

**EX019 — Registro de evidência.** *Objetivo:* produzir evidência verificável. *Insumos:* você exporta o conjunto de regras do fw-01 para `fw-01-rules-20261013.txt`. *Passos:* escrever os campos do registro de evidência e o comando que produz o seu hash no Linux. *Evidência esperada:* registro e `sha256sum fw-01-rules-20261013.txt`. *Rubrica:* 3 = os seis elementos, horário UTC com a fonte do relógio, hash guardado separado do arquivo; 2 = falta um; 1 = apenas o hash; 0 = nada.

**EX020 — Alternativas passivas.** *Objetivo:* evitar testes ativos desnecessários. *Insumos:* três perguntas: quais hosts conversam com a KW-07; que firmware a KW-07 executa; se a KW-07 aceita telnet. *Passos:* propor um método passivo ou somente de leitura para cada uma e dizer quando um teste ativo ainda se justificaria. *Evidência esperada:* três linhas. *Rubrica:* 3 = logs de fluxo ou captura SPAN; registros de ativos ou a ferramenta do fornecedor durante uma sessão de engenharia aprovada; exportação de configuração ou a documentação do fornecedor, com uma verificação ativa apenas numa janela com escopo e com as operações presentes; 2 = um fraco; 1 = todos ativos; 0 = nada.

### Síntese do capítulo

Em ambientes críticos, o escopo protege o processo tanto quanto quem testa. Escreva-o antes de começar, prefira métodos passivos e torne cada evidência verificável por outra pessoa: bruta, com origem, com horário em UTC, atribuída e com hash. Preserve antes de mudar e mantenha separados o observado, o inferido, o feito e o em aberto.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 18

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (inglês) →](../../en/book/MANUSCRIPT.md#ch-06)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável e o que a rubrica recompensa. Uma resposta diferente recebe a pontuação máxima quando atende ao mesmo padrão de evidências, escopo e honestidade sobre os limites. Os resultados numéricos vêm dos laboratórios offline deste livro, executados com o Python 3.13.5 e apenas a biblioteca padrão; quando um resultado depende de um laboratório modificado, a modificação é descrita para que você possa reproduzi-la. Todos os números descrevem dados sintéticos; nunca os apresente como constatações sobre operadores reais. Esta edição parcial traz as resoluções de EX001–EX020; as de EX021–EX072 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

### Capítulo 1: EX001–EX004

**EX001 — Classificação de caminhos.** IHM → scada-01 "ligar bomba 2": controle; pior caso, um acionamento ou desligamento não autorizado de uma bomba (transbordamento, transiente de pressão). KW-04 → scada-01 leitura: monitoramento; pior caso, os operadores agem com base num nível falso. eng-ws-15 → KW-04 download de projeto: gerência (e, indiretamente, controle); pior caso, lógica do controlador substituída — a ação mais perigosa da lista, porque muda o que o controlador faz mesmo que nenhum outro comando seja enviado. jump-01 → hist-02 SSH: gerência; pior caso, registros históricos alterados ou apagados, ou um ponto de apoio na Z2. hist-02 → CSV corporativo: dados de monitoramento saindo da zona de controle; pior caso, divulgação de dados operacionais ou, se implementado como pull, uma credencial corporativa dentro da Z2 (Capítulo 15).

**EX002 — Conserte o ciclo no papel.** Exemplo: (1) varrer as quatro estações de fibra e as cinco celulares em canais separados das três estações de rádio (três canais: fibra 0,31 s, celular 6,52 s, rádio 4,50 s — o celular continua lento demais); (2) reduzir as varreduras por ciclo das celulares de 4 para 2, combinando as leituras de registradores numa única requisição (canal celular 3,26 s), e dar à KW-06 um canal próprio (2 varreduras × 690 ms = 1,38 s; celulares restantes 1,88 s). Com canais de ≤ 4,5 s, todas as estações saudáveis atendem aos 5 s. Limitar uma estação morta: um timeout de 800 ms sem nova tentativa imediata mantém uma KW-06 morta em 1,6 s no seu próprio canal. A pontuação máxima verifica editando `stations`, `TIMEOUT_MS` e a função `cycle` e relata os valores impressos; qualquer configuração que execute e atenda ao requisito recebe crédito, se o timeout for justificado frente à latência real do enlace.

**EX003 — Impacto do túnel.** Sequencial: 5 estações celulares × 4 varreduras × 35 ms = 700 ms, logo 11,33 → 12,03 s. Canais por estação: o ciclo próprio de cada estação celular sobe 4 × 35 = 140 ms; a KW-06 passa a 2,90 s, ainda abaixo de 5 s. Recomendação: o túnel só é aceitável junto com o novo desenho dos canais (EX002), e a sua latência deve ser medida num piloto, não presumida.

**EX004 — Lista de plataformas compartilhadas.** Hosts de virtualização — "Qual é a folga se um host falhar, e quais convidados reiniciam onde?" Diretório — "Quem está nos grupos de administradores, e os operadores conseguem entrar na IHM se o diretório estiver inalcançável?" Fonte de tempo — "Qual é a referência, há uma segunda, e o deslocamento é monitorado?" Coletor de monitoramento — "O que acontece quando o disco dele enche ou ele para — as fontes armazenam em buffer, e alguém é alertado?"

### Capítulo 2: EX005–EX008

**EX005 — Decodificação à mão.** Quadro 1: tid 0x0010 = 16, protocolo 0, comprimento 6, unidade 1, função 16 (escrever vários registradores), endereço inicial 10, quantidade 2 — mas a função 16 também precisa levar uma contagem de bytes (4) e quatro bytes de valores, de modo que a PDU está incompleta; um analisador correto a rejeita, mesmo que o comprimento MBAP corresponda aos bytes presentes. Quadro 2: tid 17, comprimento 6, unidade 1, função 15 (escrever vários coils), endereço 0, quantidade 8 — também sem a sua contagem de bytes (1) e o byte dos coils. A pontuação máxima observa que as verificações do MBAP sozinhas não validam uma PDU; cada função tem a sua própria estrutura.

**EX006 — Estenda o decodificador.** No ramo de escrita: `if fc in (15, 16): bc = b[12]; data = b[13:13 + bc]` e, para a 16, `vals = struct.unpack(f">{qty}H", data)` depois de verificar `bc == 2 * qty and len(data) == bc`. Para o quadro de 10.30.3.7, `...011000070002040064000a`, a contagem de bytes é 4 e os valores são 100 e 10 — dois registradores a partir do 7 (o setpoint e o registrador seguinte).

**EX007 — Política de escrita como dados.** Normal: (10.20.0.10, 10.10.0.0/16, {1, 2, 3, 4}). Janela de manutenção: acrescentar (10.20.0.15, a estação nomeada no chamado, {3, 5, 6, 15, 16}) apenas durante a janela. O plantão do KVROC liga e desliga a política mediante um chamado aprovado pelas operações da Kestrel Water; a alternância é registrada, e a janela expira automaticamente.

**EX008 — Reconhecimento ou recurso?** A consulta diária do scada-01 é coerente com um recurso de inventário; confirme na documentação do fornecedor do SCADA e acrescente-a ao modelo como um fluxo esperado. A rajada de três segundos de 10.20.0.31 é prioritária: um host desconhecido na Z2 consultando a identificação de várias estações tem a forma de reconhecimento. As primeiras verificações são somente de leitura: registros de DHCP e do switch para o endereço, o inventário de ativos, os logs do host de salto e do diretório para esse host. Não o sonde. O Capítulo 17 mostra o que ele fez em seguida.

### Capítulo 3: EX009–EX012

**EX009 — O primeiro valor vence.** Se a linha comentada for descomentada onde está (depois de `PasswordAuthentication yes`), o valor efetivo continua `yes`, porque o sshd usa o primeiro valor lido. A correção precisa substituir a primeira ocorrência (ou apagá-la) e depois ser confirmada com `sshd -T | grep -i passwordauthentication`.

**EX010 — Priorize as constatações do HIST-02.** Hoje: preservar `last`/`lastlog`/os logs de autenticação de `backup2` e `vendor`; remover `backup2` (UID 0) e remover `vendor` do `sudo` e do `ops-admins`. Esta semana, como uma única mudança testada a partir de uma sessão aberta: `ListenAddress 10.90.0.21`, `PermitRootLogin no`, `PasswordAuthentication no` (depois de confirmar os logins por chave das duas pessoas autorizadas), `X11Forwarding no`, `MaxAuthTries 3`. Próxima janela: definir o shell de `histsvc` como `/usr/sbin/nologin` depois de verificar os jobs agendados e os scripts. O acesso do fornecedor passa para o processo com prazo do Capítulo 10.

**EX011 — Estenda a auditoria.** Acrescentar dentro do laço do passwd: `if name != "root" and home in ("/root", "/") and not shell.endswith("nologin"): findings.append(f"account {name} has interactive shell and home {home}")`. A saída acrescenta `account backup2 has interactive shell and home /root`, com 11 constatações. Um diretório pessoal compartilhado mistura o histórico do shell e as chaves entre identidades, de modo que as ações não podem ser atribuídas.

**EX012 — Desenho de conta de serviço.** UID de sistema (por exemplo, 998), shell `/usr/sbin/nologin`, diretório pessoal `/opt/hist` pertencente a root e legível pelo grupo `histsvc`; diretório de dados gravável apenas por `histsvc`; credencial do banco de dados num arquivo com modo 0400 pertencente a `histsvc`, ou no cofre de segredos da plataforma; trocada anualmente e depois de qualquer mudança de pessoal com acesso, responsável a equipe de plataforma do KVROC; a conta nunca é usada por pessoas.

### Capítulo 4: EX013–EX016

**EX013 — Preveja antes de executar.** KW-11 12.0 → aceitar (faixa inclusiva); KW-12 `inf` → rejeitar "value not finite" (linha 13); KW-02 −0.0 → aceitar. Resumo `{"accept": 4, "reject": 7, "quarantine": 2}` (verificado executando). Normalizar −0,0 para 0,0 antes de armazenar.

**EX014 — Rejeitar ou pôr em quarentena?** (a) Quarentena: interpretável, mas fora da faixa — fluxo reverso, offset do sensor ou manipulação. (b) Rejeitar, a menos que o esquema defina explicitamente as unidades sem distinção de maiúsculas; nunca adivinhar. (c) Aceitar; um alarme de nível alto do processo é ferramenta do operador, não do validador. (d) Aceitar se estiver dentro de uma tolerância de relógio combinada (por exemplo, 5 s); caso contrário, quarentena como problema de relógio.

**EX015 — JSON com armadilhas.** `json.loads('{"station": "KW-03", "value": NaN}')` devolve `{'station': 'KW-03', 'value': nan}`. Defina `def no_const(c): raise ValueError(f"non-standard JSON constant {c}")` e chame `json.loads(s, parse_constant=no_const)`; agora ele lança exceção. A RFC 8259 não permite NaN nem Infinity.

**EX016 — Resumo para monitoramento.** Exemplo: `{"accept": 2, "reject": 6, "quarantine": 2, "by_reason": {"not a number": 2, "unit": 1, "timestamp": 1, "not finite": 1, "field count": 1, "range": 1, "future": 1}, "by_station": {"KW-03": 1, ...}}`. Alerta: qualquer quarentena de uma tag CL2_MGL, ou rejeições acima de 10 % das linhas em duas exportações consecutivas, ou a ausência total da exportação.

### Capítulo 5: EX017–EX020

**EX017 — Conserte um escopo.** Defeitos: a "TI" não é a dona do sistema (a Kestrel Water precisa autorizar); 10.10.0.0/16 são todas as estações; varredura ativa numa rede de controle; nenhuma janela ou horário; nenhuma ação permitida; nenhuma condição de parada; nenhum contato; nenhum tratamento das evidências. Reescrita: propósito "estabelecer os serviços expostos pelas RTUs das estações"; método primeiro a partir dos registros de ativos, das exportações de configuração e de uma captura passiva de 24 h; se restar uma lacuna, um teste de conexão por porta nomeada numa estação nomeada, numa janela combinada, com a sala de controle informada, autorizado por A. Mensah, parada a qualquer alarme, evidências com hash na pasta do caso.

**EX018 — Rotule a nota.** *Observado:* sessão de configuração da RTU KW-09 às 06:41Z (relógio corrigido); as leituras pararam às 07:05Z. *Inferido:* possível mudança não aprovada; quem a fez é desconhecido — "fornecedor" não está estabelecido. *Feito:* RTU reiniciada às 07:30Z por mim, sem preservação — a configuração em execução e o log da sessão anteriores ao reinício podem estar perdidos. *Em aberto:* quem abriu a sessão e por quê; se existe uma exportação de configuração ou um backup de antes do reinício; responsável L. Ferreira.

**EX019 — Registro de evidência.** O quê: `fw-01-rules-20261013.txt` (exportação bruta). Origem: fw-01, CLI de gerência, versão do firmware registrada. Tempo: 2026-10-13T08:12:40Z, host coletor sincronizado com o ntp-ops (deslocamento de +0,1 s). Coletor: R. Kaur. Método: o comando exato de exportação. Integridade: a saída de `sha256sum fw-01-rules-20261013.txt` registrada no registro do caso, guardada separada do arquivo.

**EX020 — Alternativas passivas.** Quem conversa com a KW-07: logs de fluxo do fw-01 e do roteador, ou uma captura SPAN. Firmware: registros de ativos, o inventário da ferramenta do fornecedor durante uma sessão de engenharia aprovada. Telnet: a exportação de configuração da RTU e a documentação do fornecedor sobre os serviços padrão. Um teste ativo só se justifica se os registros forem conflitantes, numa janela com escopo e com as operações presentes, como um único teste de conexão.

<a id="glossary"></a>

## Glossário

- **Conduíte** — um caminho de comunicação declarado entre zonas, com propósito, protocolo, direção e responsável (Capítulo 6).
- **Laboratório contido** — um laboratório que, tecnicamente, não consegue afetar nada fora de si mesmo (Capítulo 12).
- **CRC** — verificação de redundância cíclica; detecta corrupção acidental, não falsificação (Capítulo 9).
- **Deriva** — diferença entre a configuração real de um host e o seu manifesto aprovado (Capítulo 14).
- **Configuração efetiva** — as configurações que um programa realmente usa depois de analisar os seus arquivos, por exemplo `sshd -T` (Capítulo 3).
- **Episódio** — um grupo de alertas relacionados, relatado como um único item, com contagem e intervalo de tempo (Capítulo 17).
- **Resposta de exceção (Modbus)** — uma resposta cujo código de função tem o bit mais alto ligado, com um código de exceção como 01, 02 ou 03 (Capítulo 12).
- **Teste de resposta conhecida** — conferir uma ferramenta frente a uma entrada e uma saída publicadas antes de confiar nela (Capítulo 9).
- **Cabeçalho MBAP** — o cabeçalho de 7 bytes do Modbus Application Protocol sobre TCP (Capítulo 2).
- **Teste negativo / positivo** — um teste de que uma ação proibida falha / de que uma função necessária continua funcionando (Capítulo 11).
- **Ciclo de varredura** — tempo para atualizar uma vez cada dispositivo varrido (Capítulo 1).
- **Quarentena** — guardar para revisão uma entrada interpretável, mas implausível (Capítulo 4).
- **Coordenadas de registro** — arquivo, linha e campo que identificam de onde veio uma constatação (Capítulo 4).
- **Selo** — o resumo criptográfico (digest) de um manifesto de evidências, registrado fora do pacote (Capítulo 18).
- **Regra sombreada** — uma regra de firewall que nunca tem efeito porque uma regra anterior casa com todo o seu tráfego com a ação oposta (Capítulo 10).
- **Valor travado** — uma leitura repetida por mais tempo do que o processo permite (Capítulo 8).
- **Rastreabilidade** — o vínculo entre cada requisito e os testes e evidências que o verificam (Capítulo 11).
- **Dispositivo transitório** — um notebook ou mídia que se move entre zonas ou locais (Capítulo 16).
- **UID 0** — a identidade root no Linux, seja qual for o nome da conta (Capítulo 3).
- **Zona** — um grupo de ativos com requisitos de segurança semelhantes (Capítulo 6).

<a id="references"></a>

## Referências

Normas, orientações e páginas públicas mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas. Uma citação apoia a afirmação geral ao seu lado no texto, nunca os detalhes do caso sintético. A lista é idêntica à da edição em inglês.

### Normas e orientações

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities (AA23-335A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). December 2023.
- Cybersecurity and Infrastructure Security Agency. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- Cybersecurity and Infrastructure Security Agency. [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- DNP Users Group. [Overview of DNP3 Protocol](https://www.dnp.org/About/Overview-of-DNP3-Protocol). (The full protocol is standardized as IEEE Std 1815.)
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- Modbus Organization. [Modbus specifications](https://www.modbus.org/modbus-specifications) — Modbus Application Protocol, Messaging on TCP/IP Implementation Guide, and Modbus/TCP Security.
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final).
- National Institute of Standards and Technology. [SP 800-41 Rev. 1, Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-86, Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final).
- National Institute of Standards and Technology. [SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-123, Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final).
- National Institute of Standards and Technology. [SP 800-128, Guide for Security-Focused Configuration Management of Information Systems](https://csrc.nist.gov/pubs/sp/800/128/upd1/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).

### Protocolos, algoritmos e documentação de software

- Arkko, J., Cotton, M., and Vegoda, L. [RFC 5737: IPv4 Address Blocks Reserved for Documentation](https://www.rfc-editor.org/rfc/rfc5737). IETF, 2010.
- Bray, T. (ed.). [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259). IETF, 2017.
- Cook, G. [Catalogue of parametrised CRC algorithms with 16-bit width (CRC-16/DNP)](https://reveng.sourceforge.io/crc-catalogue/16.htm).
- Gerhards, R. [RFC 5424: The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424). IETF, 2009.
- Klyne, G., and Newman, C. [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339). IETF, 2002.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, 1997.
- Mills, D., Martin, J., Burbank, J., and Kasch, W. [RFC 5905: Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905). IETF, 2010.
- OpenBSD project. [sshd_config(5) manual page](https://man.openbsd.org/sshd_config).
- Python Software Foundation. [struct](https://docs.python.org/3/library/struct.html), [socket](https://docs.python.org/3/library/socket.html), [hashlib](https://docs.python.org/3/library/hashlib.html) and [ipaddress](https://docs.python.org/3/library/ipaddress.html). Python 3 documentation.
- Rekhter, Y., et al. [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918). IETF, 1996.
- Shafranovich, Y. [RFC 4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://www.rfc-editor.org/rfc/rfc4180). IETF, 2005.

### Pesquisa

- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine*, 21(6), 11–25, 2001.
