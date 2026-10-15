# Infraestrutura Crítica e Segurança Setorial: Métodos de Pesquisa de Doutorado e Prática de Tese

- Idioma: português do Brasil (`pt`); trilha de pesquisa de doutorado, dois anos; aproximadamente 1.600 horas de estudo planejado (curso 207 de 207, o último curso da [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–8 de 8 têm texto didático escrito, os exercícios EX001–EX050 e as resoluções correspondentes. Revisão independente por especialistas, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: pesquisadores avançados que já têm experiência de pesquisa e uma pergunta defensável sobre a segurança e a resiliência da infraestrutura crítica — energia, água, saúde, transporte, comunicações, finanças e serviços públicos. Conhecimento de entrada: o conteúdo planejado para as trilhas de [mestrado](../../../../masters-2-years/critical-sector-security/en/book/PLAN.md) e de [pós-graduação](../../../../postgraduate-2-years/critical-sector-security/en/book/PLAN.md) desta área (ainda esboços quando este texto foi escrito), ou experiência profissional equivalente, mais familiaridade prática com probabilidade, teoria básica dos grafos, simulação e entrevistas qualitativas. O [curso de doutorado em segurança de TO, IoT e sistemas ciberfísicos](../../../ot-iot-security/README.md), que o acompanha, estuda a fundo a camada dos sistemas de controle; este livro estuda a camada *setorial e intersetorial* que fica acima dela.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de propriedade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: esta trilha é um projeto educacional independente. Não é um programa de doutorado credenciado, não concede título e não concede autorização para acessar, varrer, testar ou estudar nenhuma infraestrutura, operador, conjunto de dados ou pessoa reais. Toda organização, região, ativo, pessoa, registro, conjunto de dados, benchmark e resultado numérico de um exemplo resolvido é **sintético**, salvo quando uma frase cita explicitamente uma fonte pública. Nada neste livro é um procedimento operacional para uma concessionária real.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão do livro](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia os oito capítulos em ordem. Eles seguem o arco de um único projeto de doutorado. O Capítulo 1 fixa os padrões de integridade, segurança e método que cada passo posterior precisa cumprir, num domínio em que um experimento descuidado pode ferir pessoas. O Capítulo 2 mapeia a fronteira da pesquisa e encontra uma pergunta genuinamente em aberto. O Capítulo 3 a transforma numa contribuição falseável. O Capítulo 4 replica as linhas de base que a contribuição precisa superar e pilota o procedimento do estudo. O Capítulo 5 executa o estudo principal e o valida de forma independente. O Capítulo 6 submete as alegações a uma crítica adversarial de pares e as revisa. O Capítulo 7 monta a tese e seu arquivo de reprodutibilidade sob as regras de proteção da informação que regem os dados de infraestrutura. O Capítulo 8 prepara a defesa e um plano de publicação responsável.

Cada capítulo contém seções didáticas, definições, um exemplo resolvido, uma atividade prática com código offline, uma lista de erros comuns e limites, exercícios numerados e uma síntese. Escreva sua própria resposta a cada exercício antes de abrir as [resoluções](#worked-results). Neste nível, a maioria dos exercícios tem mais de uma resposta defensável; as resoluções mostram uma, e a rubrica mostra o que um revisor recompensaria ou rejeitaria.

Mantenha quatro rótulos em toda nota de pesquisa que escrever enquanto estuda este livro: **observação** (o que uma fonte nomeada registrou), **inferência** (o que você conclui a partir das observações, e sob quais pressupostos), **alegação** (a afirmação que você pretende defender, com seu escopo) e **decisão** (o que alguém escolheu fazer por causa dela). Na pesquisa sobre infraestrutura, um quinto rótulo é indispensável: **consequência** — o efeito físico, sanitário, econômico ou social sobre as pessoas que dependem de um serviço. A maioria dos erros neste campo vem de confundir uma observação cibernética com uma alegação de consequência.

### Por que um curso de doutorado separado sobre infraestrutura crítica

A segurança da tecnologia operacional (TO) pergunta como um sistema de controle pode ser atacado e defendido. A segurança da infraestrutura crítica (IC) faz um conjunto diferente de perguntas: quais *funções* uma sociedade não pode perder, por quanto tempo pode perdê-las, como a perda de uma se propaga para outras, quem é responsável por cada elo, quais regras se aplicam e como evidências sobre tudo isso podem ser reunidas sem pôr em perigo os serviços estudados. A unidade de análise passa do dispositivo e da planta para **o serviço, o setor e o sistema de sistemas**. Uma contribuição de doutorado aqui pode ser um modelo, um método de medição, uma avaliação de política, um estudo empírico de operadores ou um princípio de projeto validado; raramente é um novo exploit, e quase nunca deveria ser.

### O corpus de pesquisa sintético usado neste livro

O livro acompanha um projeto de doutorado inventado, o **Cascade Study**, que pergunta se uma *ordenação de restauração ciente das dependências* — restaurar os alimentadores elétricos na ordem em que os serviços críticos que eles sustentam esgotariam, de outro modo, suas reservas — reduz a perda de serviços críticos depois de uma queda da distribuição induzida por um ciberataque, em comparação com uma ordenação convencional que maximiza os clientes restaurados, e a que custo para os clientes comuns. Seus cenários fictícios são:

| Elemento sintético | Papel no livro | Limite |
|---|---|---|
| **Riverbend Region** — Riverbend Electric Cooperative (REC), Riverbend Water Authority (RWA), St. Calder Hospital, central da Meridian Telecom, despacho de emergência do condado de Riverbend | Contexto principal do estudo, com quatro alimentadores de distribuição F1–F4 (capítulos 1, 3 e 5). | Região inventada; nenhuma concessionária, hospital, operadora, funcionário, ativo ou registro real. |
| **Port Halvard** | Segundo contexto, costeiro, com uma topologia de alimentadores diferente, duas equipes de restauração e contratos de reabastecimento de combustível (validação independente do Capítulo 5, Capítulo 6). | Região inventada. |
| **GridWater-Sim** | Um benchmark de cossimulação "publicado", sintético, cuja linha de base inicialmente não pode ser reproduzida (Capítulo 4). | Benchmark inventado; não é uma ferramenta nem um conjunto de dados reais e não deve ser procurado. |
| Estudos sintéticos **P1–P8** | Artigos fictícios usados para praticar a avaliação crítica e o mapeamento da literatura (Capítulo 2). | Inventados; representam tipos de estudo, e não autores reais. |
| Participantes operadores **P01–P12** | Entrevistados e participantes de exercícios de mesa fictícios (capítulos 1, 5 e 6). | Inventados; nenhum dado de seres humanos aparece em parte alguma deste livro. |

Todos os números produzidos nos laboratórios vêm de dados sintéticos impressos no texto e executados apenas com a biblioteca padrão do Python 3. Eles demonstram um método; não são constatações sobre nenhuma infraestrutura real.

### Política de fontes

Toda afirmação factual sobre uma norma, uma regulamentação, um incidente público ou um estudo publicado remete a uma fonte consultada pelo autor. Normas e regulamentações mudam; cada uma é citada com sua versão e data e deve ser verificada de novo antes que você se apoie nela. Onde um conceito é vocabulário metodológico padrão (por exemplo, a distinção entre verificação e validação de um modelo), o texto diz isso em vez de inventar uma referência. Uma fonte apoia a afirmação geral ao seu lado, nunca os detalhes do caso sintético. Relatórios públicos de incidentes são usados apenas no nível de detalhe que seus editores divulgaram, e nenhuma instrução operacional de ataque é reproduzida.

## Sumário

1. [Integridade e métodos avançados de pesquisa](#ch-01) — a consequência como objeto de estudo, as evidências na pesquisa sobre infraestrutura, segurança e ética do duplo uso, informação protegida, métricas de resiliência e o protocolo defensável.
2. [Infraestrutura crítica e segurança setorial: fronteira da pesquisa](#ch-02) — o panorama de políticas e normas, as famílias de modelagem de interdependências, a pesquisa de detecção e de testbeds, as evidências setoriais e uma lacuna falseável.
3. [Proposta de contribuição original](#ch-03) — mecanismo, grafos de dependência com reservas, hipóteses, linhas de base, explicações rivais e condições de falha declaradas com antecedência.
4. [Replicação da linha de base e piloto](#ch-04) — reproduzir um modelo de inoperabilidade e um benchmark de detecção, armadilhas de avaliação, verificação do modelo e um piloto delimitado.
5. [Estudo principal e validação independente](#ch-05) — experimentos de simulação com incerteza, estudos de mesa com operadores, validação contra o histórico e especialistas, e um segundo contexto.
6. [Crítica de pares e revisão](#ch-06) — circularidade modelo–política, condições de fronteira, inadequação do modelo, resultados negativos, revisão de duplo uso e estreitamento das alegações.
7. [Síntese da tese e arquivo de reprodutibilidade](#ch-07) — estrutura do argumento, liberação de artefatos em níveis sob as regras de informação de infraestrutura, dados sintéticos e documentação do modelo.
8. [Defesa e plano de publicação](#ch-08) — auditoria das alegações, preparação da defesa, veículos, divulgação coordenada, tradução para políticas públicas e o programa de pesquisa pós-doutoral.

As [resoluções](#worked-results) contêm EX001–EX050. Um [glossário](#glossary) e as [referências](#references) encerram o livro.

<a id="ch-01"></a>

## Capítulo 1 — Integridade e métodos avançados de pesquisa

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Definir infraestrutura crítica, função crítica, dependência, interdependência e resiliência com precisão suficiente para que se possa associar uma medição a cada uma, e explicar por que as definições usadas por diferentes governos não são intercambiáveis.
2. Distinguir observações cibernéticas de alegações de consequência e declarar que evidências são necessárias para passar de umas às outras.
3. Aplicar salvaguardas de integridade da pesquisa — pré-especificação, registros de desvios, separação entre trabalho exploratório e confirmatório, declaração de conflitos de interesse — a estudos cujos parceiros são operadores regulados.
4. Identificar os perigos de segurança, duplo uso, jurídicos e de proteção da informação da pesquisa sobre infraestrutura e projetar salvaguardas proporcionais, usando os princípios do Menlo Report como estrutura de trabalho.
5. Escolher e defender métricas de resiliência e de consequência, reconhecendo que a escolha da métrica pode inverter a classificação dos cenários e que as janelas de observação censuram as quedas não recuperadas.
6. Escrever um protocolo de pesquisa que um revisor hostil, mas justo — e o responsável pela segurança de uma concessionária —, conseguiria auditar, incluindo condições de parada.

O capítulo é o contrato metodológico do restante do livro. O Capítulo 2 lê a literatura com o seu vocabulário de evidências; o Capítulo 3 usa o seu modelo de protocolo; os capítulos 4 e 5 usam as suas métricas e ferramentas de validade; os capítulos 6 a 8 usam os seus padrões de integridade, segurança e proteção da informação para julgar o trabalho concluído.

### 1.1 O que se estuda: serviços, funções e consequências

#### 1.1.1 Definições que têm peso

"Infraestrutura crítica" é um termo jurídico e de política pública antes de ser um termo técnico, e sua definição decide para o que um estudo pode generalizar. Nos Estados Unidos, a definição legal do USA PATRIOT Act (42 U.S.C. § 5195c(e)) descreve sistemas e ativos "so vital to the United States that the incapacity or destruction of such systems and assets would have a debilitating impact on security, national economic security, national public health or safety" (tão vitais para os Estados Unidos que a incapacidade ou a destruição desses sistemas e ativos teria um impacto debilitante sobre a segurança, a segurança econômica nacional, a saúde pública nacional ou a segurança pública). A política norte-americana organiza esses ativos em setores; o [National Security Memorandum on Critical Infrastructure Security and Resilience (NSM-22)](https://www.govinfo.gov/content/pkg/DCPD-202400358/html/DCPD-202400358.htm), emitido em 30 de abril de 2024, revogou e substituiu a Presidential Policy Directive 21 (2013), manteve a estrutura setorial, nomeou a Cybersecurity and Infrastructure Security Agency (CISA) como coordenadora nacional e designou as Sector Risk Management Agencies ([visão geral da CISA](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience); [resumo do Congressional Research Service](https://www.congress.gov/crs-product/IF12716)). O resumo do CRS observa que um governo posterior pode revogar ou modificar o NSM-22 sem ação do Congresso, então uma tese precisa citar o instrumento em vigor numa data declarada.

A União Europeia usa dois instrumentos coordenados: a [Diretiva (UE) 2022/2557 relativa à resiliência das entidades críticas (CER)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj), para a resiliência a todos os perigos das entidades críticas designadas, e a [Diretiva (UE) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/), para a cibersegurança das entidades essenciais e importantes. Um estudo que chama um hospital de "infraestrutura crítica" no sentido norte-americano e de "entidade essencial" no sentido da NIS2 não está usando sinônimos: as populações diferem, as obrigações diferem e os limiares de notificação diferem.

Uma lente complementar é a da **função**, e não a do ativo. O [conjunto de National Critical Functions da CISA](https://www.cisa.gov/national-critical-functions-set), publicado em abril de 2019, lista 55 funções agrupadas como *Connect*, *Distribute*, *Manage* e *Supply* — por exemplo, "Distribute electricity" (distribuir eletricidade) ou "Supply water" (fornecer água). As funções atravessam setores e organizações. Para a pesquisa, a lente funcional tem uma vantagem decisiva: ela nomeia algo cuja *perda* pode ser medida (serviço entregue, pessoas afetadas, duração), e não algo cujo *comprometimento* pode ser observado (um host, uma credencial, um controlador).

Definições de trabalho usadas neste livro:

| Termo | Definição de trabalho | O que você precisa medir para usá-la |
|---|---|---|
| **Serviço crítico** | Um serviço cuja interrupção além de uma duração declarada causa danos à saúde, à segurança, à proteção ou a atividades econômicas essenciais de uma população declarada. | População atendida, limiar de dano, duração tolerável da interrupção. |
| **Dependência** | Uma relação unidirecional em que o estado do serviço *B* depende do serviço *A* ([Rinaldi, Peerenboom and Kelly, 2001](https://doi.org/10.1109/37.969131)). | Direção, tipo, reserva, intensidade do acoplamento. |
| **Interdependência** | Uma relação bidirecional: o estado de cada serviço depende do estado do outro, diretamente ou por meio de uma cadeia (mesma fonte). | O ciclo e seus tempos. |
| **Reserva** | Capacidade armazenada que permite a um dependente continuar operando depois de perder um fornecedor: combustível, baterias, armazenamento de água, estoques, procedimentos manuais. | Duração sob carga declarada, e como ela se esgota. |
| **Consequência** | O efeito sobre as pessoas e sobre as funções de que elas dependem, medido em unidades de serviço (clientes-hora, desvios de pacientes, litros não entregues). | Uma unidade, uma população, uma janela de tempo. |
| **Resiliência** | A capacidade de um sistema de resistir, absorver, recuperar-se e adaptar-se a uma perturbação; operacionalizada por métricas sobre uma curva de desempenho (§1.6). | Uma medida de desempenho ao longo do tempo e um resumo escolhido. |

Rinaldi, Peerenboom e Kelly classificam as interdependências como **físicas** (uma saída material de uma é insumo de outra), **cibernéticas** (dependência de informação transmitida por uma infraestrutura de informação), **geográficas** (um evento local afeta componentes colocalizados) e **lógicas** (qualquer outro mecanismo, como mercados ou políticas). Suas seis "dimensões" — ambiente, acoplamento e comportamento de resposta, tipo de falha (em cascata, escalonada, de causa comum), características da infraestrutura, estado de operação e tipo de interdependência — continuam sendo uma checklist útil do que um modelo ignora. Um estudo de doutorado deve declarar quais dessas dimensões modela e quais mantém fixas.

#### 1.1.2 A observação cibernética não é a consequência

O problema epistêmico que define o campo é a distância entre o que se pode observar sobre um evento cibernético e o que aconteceu às pessoas. Considere três exemplos públicos, descritos apenas no nível que seus editores divulgaram:

- O ataque de dezembro de 2015 a três distribuidoras de eletricidade ucranianas interrompeu o fornecimento de energia a cerca de 225.000 clientes por várias horas; o [caso de uso de defesa conjunto do E-ISAC e do SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and) (março de 2016) descreve o roubo de credenciais, a operação remota dos sistemas de gestão da distribuição, malware destrutivo e uma negação de serviço telefônica contra as centrais de atendimento aos clientes. A *consequência* (clientes sem energia, por horas) dependeu da capacidade dos operadores de restaurar manualmente — uma reserva que era organizacional, e não técnica.
- O malware descrito pela CISA como [CrashOverride](https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware) (alerta TA17-163A, junho de 2017) visou subestações de eletricidade na Ucrânia em 2016. Uma análise de capacidades de um malware diz o que *poderia* ser comandado; ela não diz, por si só, o que *foi* perdido.
- A análise da CISA sobre o [HatMan (também conhecido como TRITON ou TRISIS)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf) descreve um malware que visava um sistema instrumentado de segurança. Aqui a consequência mais importante é uma que não ocorreu — e as alegações de pesquisa sobre "quase acidentes" exigem cuidado especial, porque o contrafactual é inobservável.

Cada caso liga uma observação cibernética (malware, acesso, comandos) a uma consequência (queda, desarme, dano evitado) por meio de uma cadeia de mecanismos físicos e organizacionais. Uma alegação de pesquisa que pula a cadeia — "ataques a subestações causam apagões" — não está tão errada quanto sem apoio. Escreva a cadeia explicitamente; cada elo é um lugar onde uma reserva, um procedimento manual, um sistema de proteção ou uma decisão humana pode rompê-la.

#### 1.1.3 A escada de alegações para a pesquisa sobre infraestrutura

O livro de doutorado de RI desta série introduziu uma escada de alegações ([observação, inferência, alegação de caso, alegação de pesquisa](../../../incident-response-resilience/en/book/MANUSCRIPT.md#ch-01)). A pesquisa sobre infraestrutura precisa de mais um degrau, porque as alegações centrais do campo tratam de consequências em sistemas físicos que o pesquisador em geral não consegue observar diretamente:

| Nível | Tipo de afirmação | Exemplo (sintético) | Evidência típica |
|---|---|---|---|
| L1 Observação | Uma fonte nomeada registrou algo. | "O sistema de gestão de interrupções da REC registrou o alimentador F3 aberto às 02:10." | Registro preservado, com o estado do relógio. |
| L2 Inferência | Uma conclusão a partir de observações, sob pressupostos declarados. | "O F3 foi aberto por um comando remoto, e não pela proteção." | Logs de comandos, registros de eventos dos relés, pressupostos declarados. |
| L3 Alegação de caso | Uma afirmação sobre o que aconteceu num evento. | "A estação de tratamento operou com gerador por 7 h e depois perdeu pressão na zona alta." | Registros convergentes de vários proprietários. |
| L4 Alegação de consequência | Uma afirmação sobre os efeitos sobre pessoas ou funções. | "Cerca de 2.500 clientes ficaram sem pressão de água potável por cerca de 5 h." | Registros de serviço, relatos de clientes, verificação em campo. |
| L5 Alegação de pesquisa | Uma afirmação geral sobre uma população de sistemas ou eventos. | "A restauração ciente das dependências reduz a perda de serviços críticos em quedas da distribuição." | Muitos casos, um modelo validado ou um estudo planejado. |

Subir um degrau sempre acrescenta pressupostos. O protocolo da §1.8 exige que toda alegação de uma tese seja marcada com seu degrau e seus pressupostos.

### 1.2 Evidências na pesquisa sobre infraestrutura

#### 1.2.1 Cinco fontes de evidência e seus vieses característicos

1. **Registros de incidentes e relatórios públicos.** Raros, divulgados de forma seletiva, escritos para outros fins que não a pesquisa e moldados pela exposição jurídica. O viés de publicação é extremo: eventos com consequências dramáticas ou adversários atribuíveis são relatados; perturbações absorvidas em silêncio, não. A *população* de incidentes é desconhecida.
2. **Dados operacionais dos parceiros.** Historiadores do SCADA, registros de gestão de interrupções, ordens de serviço, logs de alarmes. Alta fidelidade, mas pertencem ao operador, muitas vezes são protegidos por lei ou contrato e são produzidos por sistemas ajustados para a operação, e não para a medição. A amostragem é decidida pela disposição do parceiro, que se correlaciona com a maturidade.
3. **Testbeds.** Plantas laboratoriais físicas ou híbridas, como o testbed Secure Water Treatment (SWaT) descrito por [Goh, Adepu, Junejo and Mathur (2016)](https://doi.org/10.1007/978-3-319-71368-7_8). Permitem ataques controlados e dados rotulados, ao custo da escala, da idade e do realismo: uma planta didática de seis estágios não é o sistema de água de uma cidade.
4. **Modelos e simulações.** Modelos de redes, de fluxo, de insumo-produto, baseados em agentes, de dinâmica de sistemas e de cossimulação (Capítulo 2). Permitem contrafactuais e escala, mas só provam o que sua estrutura e seus parâmetros permitem; sua validade precisa ser estabelecida, e não presumida ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)).
5. **Pessoas.** Entrevistas, questionários, exercícios de mesa e observação de operadores, gestores de emergência e reguladores. Revelam reservas que existem apenas como prática — soluções manuais de contorno, ajuda mútua informal — e também revelam o que as pessoas *dizem* que fariam, que não é o que fazem sob estresse.

Um trabalho de doutorado forte **triangula**: a previsão de um modelo é conferida com um registro histórico, um experimento em testbed e o julgamento dos operadores, e a tese explica o que cada fonte pode e não pode atestar.

#### 1.2.2 O problema da taxa-base e do denominador

Incidentes de infraestrutura com consequências físicas são raros. Um estudo que coleta "incidentes cibernéticos que afetaram concessionárias" a partir de fontes públicas tem um numerador sem denominador: não consegue dizer com que frequência esses incidentes ocorrem, apenas com que frequência são *relatados*. As taxas exigem uma população definida (todas as concessionárias de um tipo numa jurisdição), um período definido e um mecanismo de notificação com completude conhecida. Regimes de notificação obrigatória podem acabar ajudando: o Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA), dos EUA, exige que a CISA edite regras; a proposta de regra da CISA de 2024 exigiria a notificação dos incidentes abrangidos em até 72 horas e dos pagamentos de resgate em até 24 horas, e a regra final foi enviada para revisão interagências em 1º de outubro de 2026, depois de perder prazos anteriores ([Inside Privacy, 2026](https://www.insideprivacy.com/critical-infrastructure/cisa-submits-final-circia-rule-for-omb-review/)). Até que uma regra final seja publicada e entre em vigor, e até que seus dados sejam disponibilizados aos pesquisadores sob algum regime de acesso, nenhuma tese deve tratar obrigações de notificação como dados.

#### 1.2.3 Retrospectiva, contrafactuais e "quase acidentes"

As alegações de consequência neste campo são muitas vezes contrafactuais: "se os operadores não tivessem passado para o controle manual, a queda teria durado dias". Os contrafactuais só são objetos de pesquisa legítimos quando produzidos por um modelo explícito, cujos pressupostos são divulgados e cuja sensibilidade é relatada. A retrospectiva faz o caminho real parecer inevitável e as alternativas parecerem óbvias; o desenho dos exercícios de mesa do Capítulo 5 mostra como apresentar cenários aos participantes sem o conhecimento do desfecho.

### 1.3 Integridade quando os parceiros são operadores regulados

#### 1.3.1 Pressões específicas do campo

As práticas de pesquisa questionáveis — relato seletivo, análise flexível, formular hipóteses depois de conhecer os resultados — são gerais ([Simmons, Nelson and Simonsohn, 2011](https://doi.org/10.1177/0956797611417632); [Kerr, 1998](https://doi.org/10.1207/s15327957pspr0203_4)). A pesquisa sobre infraestrutura acrescenta quatro pressões:

- **Exposição regulatória.** Um operador parceiro pode temer que uma constatação seja lida como descumprimento. A pressão para suavizar ou adiar resultados é previsível e precisa ser tratada por um acordo de publicação por escrito *antes* do acesso aos dados (§1.5.3).
- **Financiamento por partes interessadas.** Fornecedores de produtos de detecção, associações setoriais e agências financiam pesquisas. Financiamento não é corrupção, mas financiamento não declarado é uma falha de integridade, e o enquadramento favorável do produto de um financiador é um risco conhecido.
- **Classificação e sensibilidade.** Alguns resultados não podem ser publicados por inteiro. A tentação é publicar a parte favorável. A regra deste livro: se um resultado não pode ser publicado, a *existência* da análise retida e sua direção precisam ser reveladas aos examinadores sob o arranjo de acesso, e o texto público não pode alegar mais do que as evidências públicas apoiam.
- **Flexibilidade da simulação.** Um modelo tem muitos parâmetros livres. Ajustá-los até que o método proposto vença é o equivalente, na simulação, ao p-hacking. A salvaguarda é fixar as distribuições dos parâmetros, os conjuntos de cenários e as métricas antes de comparar os métodos (Capítulo 3) e relatar todas as famílias de cenários, e não apenas aquelas em que o método vence.

#### 1.3.2 Pré-especificação para estudos de simulação e de métodos mistos

O pré-registro não é só para experimentos com participantes humanos ([Nosek et al., 2018](https://doi.org/10.1073/pnas.1708274114)). Para um estudo de simulação, pré-especifique: a versão do modelo e seus testes de verificação; as distribuições dos parâmetros e suas fontes; as famílias de cenários e quantos sorteios de cada; as políticas comparadas, incluindo a linha de base mais forte disponível; a métrica primária, a métrica secundária ou de segurança e qualquer margem de não inferioridade; as sementes; e a análise (diferenças pareadas, método dos intervalos). Para entrevistas e exercícios de mesa, pré-especifique a base de amostragem, o protocolo, as categorias iniciais do quadro de codificação e a regra para acrescentar categorias. Um **registro de desvios** anota cada mudança, com a data, o motivo e se os resultados já tinham sido vistos.

#### 1.3.3 Originalidade e proveniência

A literatura sobre infraestrutura está espalhada pela engenharia, pela pesquisa operacional, pela economia, pelas políticas públicas e pela segurança computacional, e a mesma ideia é muitas vezes redescoberta sob nomes diferentes: "restauração ciente das dependências" na engenharia de potência, "priorização da restauração" na gestão de emergências, "criticidade em nível de serviço" na TI. Uma alegação de originalidade de doutorado precisa, portanto, de uma busca entre disciplinas (Capítulo 2) e de uma declaração honesta do que é novo: o método, a aplicação, as evidências ou a síntese.

### 1.4 Segurança, duplo uso e ética

#### 1.4.1 Por que a pesquisa sobre infraestrutura precisa de sua própria análise ética

O [Menlo Report](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) (Dittrich and Kenneally, 2012) adaptou os princípios de Belmont — respeito às pessoas, beneficência, justiça — à pesquisa em tecnologias da informação e comunicação e acrescentou o **respeito à lei e ao interesse público**. Aplicá-lo à pesquisa sobre infraestrutura revela partes interessadas ausentes da maioria dos estudos de segurança: a população atendida pela infraestrutura, que nunca consentiu e pode ser prejudicada por um experimento que dê errado; a equipe do operador, que pode ficar exposta a culpa; e terceiros conectados por interdependência.

| Princípio do Menlo | Aplicação específica à infraestrutura |
|---|---|
| Respeito às pessoas | Consentimento informado da equipe entrevistada ou observada; proteção contra o uso disciplinar dos dados de pesquisa; consentimento separado para gravação de áudio. A população atendida não pode consentir, então seus interesses precisam ser representados pela minimização dos riscos. |
| Beneficência | Nenhum experimento em sistemas de controle em produção. Revisão de segurança física para qualquer laboratório que energize equipamentos. Pesar o benefício de publicar uma vulnerabilidade ou um padrão de fraqueza contra a vantagem que ele dá a um adversário. |
| Justiça | Não concentrar o ônus da pesquisa (e o risco de exposição) em concessionárias pequenas e com poucos recursos, que não podem dizer não a um financiador; não projetar métodos de restauração que prejudiquem sistematicamente uma população sem dizê-lo (a margem de não inferioridade do Capítulo 3). |
| Respeito à lei e ao interesse público | Cumprir os regimes de proteção da informação (§1.5), os controles de exportação quando pertinentes, a legislação sobre uso indevido de computadores e os contratos com os parceiros; ser transparente sobre os métodos, para que o interesse público numa pesquisa responsável seja atendido. |

#### 1.4.2 Regras rígidas usadas neste livro

1. **Nunca teste em produção.** Nenhuma varredura, sondagem, fuzzing ou injeção de comandos contra qualquer sistema operacional em funcionamento, inclusive "apenas ler" com protocolos industriais, sem uma autorização por escrito do proprietário do ativo que nomeie o escopo, o horário, os controles de segurança e uma autoridade de parada. O [Guide to Operational Technology Security, SP 800-82 Rev. 3](https://doi.org/10.6028/NIST.SP.800-82r3) do NIST (setembro de 2023) explica por que a TO difere da TI: a disponibilidade e a segurança predominam, dispositivos podem falhar sob tráfego que os sistemas de TI toleram, e mudanças exigem revisão de engenharia. O NIST divulgou um rascunho público inicial da Revisão 4 em setembro de 2026, com comentários até 30 de novembro de 2026 ([página do CSRC](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); cite a revisão que você usou.
2. **Simule ou emule primeiro.** Use modelos, cossimulação, gêmeos digitais ou testbeds isolados. Quando um testbed físico for usado, ele precisa de seu próprio caso de segurança (pressão, tensão, dosagem química), revisado por um engenheiro qualificado.
3. **Separe a capacidade da consequência na publicação.** Uma tese pode publicar como uma classe de falha se propaga e quais reservas a detêm; não deve publicar uma lista de alvos específica de ativos nem um caminho passo a passo até um efeito físico.
4. **Tenha uma autoridade de parada.** Todo estudo que envolva a equipe ou os sistemas de um parceiro nomeia uma pessoa do lado do parceiro que pode interrompê-lo instantaneamente, e o protocolo diz o que acontece com os dados coletados antes da parada.

#### 1.4.3 Revisão de duplo uso

Uma revisão de duplo uso faz três perguntas antes de qualquer publicação: *Vantagem* — este resultado torna materialmente mais fácil para um adversário causar dano, em comparação com o que já é público? *Valor defensivo* — ele ajuda mais os defensores do que os atacantes, e os defensores têm meios de agir com base nele? *Mitigação* — a parte nociva pode ser generalizada, adiada (até que existam correções) ou passada para acesso controlado sem perda de valor científico? O Capítulo 6 executa uma revisão de duplo uso completa dos resultados do Cascade Study; o Capítulo 8 a situa num cronograma de divulgação coordenada.

### 1.5 Informação protegida e acordos de dados

#### 1.5.1 Regimes que o pesquisador vai encontrar

Os dados de infraestrutura muitas vezes estão sujeitos a regimes jurídicos de proteção distintos da legislação de dados pessoais. Nos Estados Unidos, os exemplos incluem a Protected Critical Infrastructure Information (PCII), a Chemical-terrorism Vulnerability Information (CVI), a Sensitive Security Information (SSI) no transporte e a Critical Energy/Electric Infrastructure Information (CEII) na Federal Energy Regulatory Commission. Seu escopo e suas regras de tratamento são definidos por lei e regulamento e mudam com o tempo; leia a regra vigente e a interpretação do parceiro antes de aceitar os dados. Na UE, a CER e a NIS2 impõem confidencialidade sobre as informações trocadas com as autoridades. Os dados pessoais em notas de entrevistas, escalas e gravações de chamadas estão sujeitos à legislação comum de privacidade (por exemplo, o GDPR na UE; no Brasil, a [LGPD, Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), fiscalizada pela ANPD).

Este livro não dá aconselhamento jurídico. Ele exige que o protocolo (§1.8) nomeie cada regime que possa se aplicar, a pessoa que decidiu se ele se aplica e a consequência para o tratamento.

#### 1.5.2 O teste de sensibilidade da informação

Mesmo sem um regime formal, aplique um teste de sensibilidade a todo artefato: *ele identifica um ativo específico, sua localização, sua vulnerabilidade ou sua dependência de um modo que ajudaria alguém a prejudicá-lo?* Mapas de alimentador para instalação, capacidades de combustível dos geradores, caminhos de comunicação de reserva e prioridades de restauração são exatamente o que um adversário que planeja um efeito em cascata quer. Os dados centrais do Cascade Study — qual alimentador atende qual instalação crítica e quanto dura sua reserva — são, portanto, sensíveis *mesmo quando todos os números são aproximados*. O Capítulo 7 constrói os níveis de liberação que decorrem disso.

#### 1.5.3 Acordos antes do acesso

Negocie antes de coletar qualquer coisa: um acordo de uso de dados (escopo, armazenamento, retenção, destruição, notificação de violações); um acordo de publicação (o parceiro pode revisar quanto a informações protegidas e erros factuais dentro de um prazo fixo, mas não pode vetar constatações de que não goste); uma política de autoria e agradecimentos; e uma cláusula de proteção da equipe (os dados de pesquisa não serão usados para fins disciplinares). Registre os acordos no apêndice do protocolo. Um estudo sem acordo de publicação deu, na prática, um veto ao seu parceiro.

### 1.6 Medição: métricas de resiliência e de consequência

#### 1.6.1 A curva de desempenho

A maioria das métricas quantitativas de resiliência resume uma **curva de desempenho** *Q(t)*: a fração do serviço normal entregue ao longo do tempo, antes, durante e depois de uma perturbação. [Bruneau et al. (2003)](https://doi.org/10.1193/1.1623497) enquadraram a resiliência sísmica das comunidades em termos de probabilidades de falha reduzidas, consequências reduzidas e tempo de recuperação reduzido, e seu amplamente reproduzido "triângulo da resiliência" mede a perda como a área entre o serviço pleno e *Q(t)* durante o período de recuperação. [Haimes (2009)](https://doi.org/10.1111/j.1539-6924.2009.01216.x) argumentou que a resiliência é função da ameaça específica e do estado do sistema, e não uma propriedade única. A [SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1) do NIST (dezembro de 2021) enquadra a ciber-resiliência como a capacidade de antecipar, resistir, recuperar-se e adaptar-se a condições adversas, estresses ou ataques a sistemas que usam recursos cibernéticos ou são viabilizados por eles.

Resumos comuns de *Q(t)*:

| Métrica | Definição | Sensível a | Cega para |
|---|---|---|---|
| Perda de resiliência (área) | ∫ (1 − Q(t)) dt sobre a janela | Profundidade × duração | Se uma perda curta e profunda é pior para as pessoas do que uma longa e rasa |
| Pior desempenho | 1 − min Q(t) | Profundidade | Duração |
| Tempo até a recuperação | Primeiro instante de serviço pleno menos o início da perturbação | Duração | Profundidade |
| Clientes-hora perdidos | Σ clientes × horas sem serviço | População e duração | Criticidade dos clientes |
| Perda ponderada de serviços críticos | Σ peso × horas em que um serviço crítico fica indisponível | Prioridades declaradas com antecedência | Clientes comuns, a menos que incluídos |

Nenhuma métrica é neutra. Cada uma embute um juízo de valor sobre de quem é a perda que conta e sobre como a profundidade se troca pela duração. Um estudo de doutorado precisa justificar sua métrica primária pela decisão que ela informa, relatar pelo menos uma alternativa e mostrar se as conclusões mudam.

#### 1.6.2 Censura

Se um serviço não se recuperou quando a janela de observação se fecha, seu tempo até a recuperação é **censurado**: o valor verdadeiro é pelo menos o valor observado. Tirar a média de durações censuradas como se fossem completas enviesa os resultados para uma recuperação mais rápida. Relate o número de censurados, use métodos de sobrevivência quando a amostra permitir ou estenda a janela. Nas simulações, a janela é uma escolha de desenho; escolha-a de modo que a censura seja rara sob todas as políticas comparadas, ou relate-a.

#### 1.6.3 Validade de construto dos pesos de consequência

Uma métrica de consequência ponderada precisa de pesos. Pesos obtidos de operadores, gestores de emergência ou frameworks publicados de criticidade são juízos de valor, e não medições. Declare-os com antecedência, cite de onde vieram e execute a análise com conjuntos alternativos de pesos (Capítulo 6). Se a conclusão depende de um único conjunto de pesos, a alegação precisa dizê-lo.

### 1.7 Modos de falha comuns nas alegações de pesquisa sobre infraestrutura

- **Salto do cibernético para a consequência.** Tratar o acesso ou a capacidade de um malware como evidência de consequência física.
- **Topologia como realidade.** Usar um diagrama de rede como se ele capturasse fluxos, reservas, proteções e operadores humanos.
- **Generalização a partir do testbed.** Relatar a acurácia de detecção num único testbed pequeno como acurácia "para sistemas de água".
- **Simulação não validada.** Apresentar saídas de modelos sem verificação, sem comparação com nenhum evento histórico e sem análise de sensibilidade.
- **Escolha oportunista de métricas.** Relatar a métrica de resiliência que favorecer o método proposto.
- **Amostragem pelo desfecho dramático.** Construir teoria apenas a partir de incidentes famosos.
- **Ignorar a reserva humana.** Omitir a operação manual, a ajuda mútua e a improvisação, que os relatórios públicos identificam repetidamente como decisivas na restauração.
- **Sensibilidade silenciosa.** Publicar dados que viabilizam a escolha de alvos porque cada número "parecia inofensivo".

### 1.8 Escrevendo um protocolo de pesquisa defensável

Um protocolo para um estudo de infraestrutura contém, no mínimo:

1. **Pergunta e degrau da alegação.** A pergunta de pesquisa, a alegação pretendida, seu degrau (L1–L5) e seu escopo (sistemas, setores, jurisdições, perigos).
2. **Definições e métricas.** Cada construto, sua operacionalização, as métricas primária e secundárias, a janela e a regra de censura.
3. **Fontes de evidência.** Quais das cinco fontes (§1.2.1), por que, e o que cada uma não pode atestar.
4. **Desenho.** Condições de comparação, linhas de base, famílias de cenários, amostragem, atribuição.
5. **Pré-especificação.** O que é fixado antes dos resultados; o registro de desvios.
6. **Segurança e ética.** Análise do Menlo, regras rígidas (§1.4.2), revisão de segurança física, autoridade de parada, aprovação para pesquisa com seres humanos quando aplicável.
7. **Proteção da informação.** Regimes aplicáveis, teste de sensibilidade, armazenamento, níveis de liberação.
8. **Acordos.** Uso de dados, publicação, autoria, proteção da equipe.
9. **Plano de análise.** Estimadores, incerteza, análises de sensibilidade, métricas e pesos alternativos.
10. **Condições de parada e de abandono.** Quando o estudo para (segurança, saída do parceiro, violação de dados) e quando a alegação é abandonada ou estreitada (condições de falha declaradas com antecedência, Capítulo 3).
11. **Conflitos de interesse e financiamento.**
12. **Plano de reprodutibilidade.** O que será liberado em qual nível (Capítulo 7).

### 1.9 Exemplo resolvido: a primeira revisão do protocolo do Cascade Study

O doutorando (sintético) propõe estudar a ordenação da restauração na Riverbend Region. O primeiro rascunho diz: *"Obteremos os registros de interrupções e os logs do SCADA da REC dos últimos cinco anos, identificaremos as quedas relacionadas a eventos cibernéticos e mostraremos que restaurar primeiro os clientes críticos teria reduzido os danos."* Uma revisão do protocolo constata:

| Problema | Por que falha | Revisão |
|---|---|---|
| "Quedas relacionadas a eventos cibernéticos" em cinco anos de uma única cooperativa | Provavelmente zero ou um evento; sem denominador; sem variação a estudar. | Usar as quedas históricas da distribuição *por todas as causas* para calibrar as durações de restauração, e uma cossimulação para os cenários cibernéticos. |
| "Teria reduzido os danos" | Contrafactual sem modelo; retrospectiva. | Modelo explícito com parâmetros declarados com antecedência; estudo de mesa com operadores sem conhecimento do desfecho. |
| "Clientes críticos primeiro" | Indefinido; confunde número de clientes com criticidade. | Definir os serviços críticos (central de telecomunicações, tratamento de água, hospital, despacho), suas reservas e pesos declarados com antecedência. |
| Logs do SCADA solicitados | Alta sensibilidade; desnecessários para a pergunta. | Solicitar resumos da gestão de interrupções em nível de alimentador, agregados; nenhum dado de rede ou de protocolo. |
| Nenhum acordo com o parceiro | Veto do parceiro por padrão. | Acordos de uso de dados e de publicação, com revisão factual de 30 dias e sem veto sobre as constatações. |
| Nenhuma métrica de segurança | Um método que ajuda os hospitais mas deixa milhares de residências no escuro por mais tempo é uma escolha de política. | Métrica secundária: clientes-hora perdidos, com uma margem de não inferioridade justificada com o parceiro (Capítulo 3). |
| O mapa alimentador–instalação apareceria na tese | Valor para a escolha de alvos. | Região sintética no texto público; o mapeamento real apenas num apêndice de acesso controlado, se tanto. |

A pergunta revisada passa a ser: *Em quedas da distribuição que exigem a restauração manual e sequencial dos alimentadores, ordenar a restauração pelo tempo até o impacto dos serviços críticos reduz a perda ponderada de serviços críticos em comparação com a ordenação pelos clientes restaurados, e em quanto aumenta os clientes-hora perdidos?* Ela pode ser respondida, medida, estudada com segurança e é honesta sobre sua troca.

### 1.10 Atividade prática: as métricas de resiliência podem inverter classificações

O laboratório offline a seguir calcula três resumos de três curvas de desempenho sintéticas e indica se cada uma está censurada. Execute-o com Python 3; nenhum pacote é necessário.

```python
# Lab 1 - resilience metrics on three synthetic performance curves (offline, standard library only)
# Q(t) = delivered fraction of normal service (1.0 = full), sampled hourly over a 48-hour window.
def curve(drop_at, depth, hold, recover_hours, window=48):
    q = []
    for t in range(window + 1):
        if t < drop_at:
            q.append(1.0)
        elif t < drop_at + hold:
            q.append(1.0 - depth)
        elif t < drop_at + hold + recover_hours:
            frac = (t - drop_at - hold) / recover_hours
            q.append(round(1.0 - depth * (1 - frac), 4))
        else:
            q.append(1.0)
    return q

def metrics(q):
    loss = sum((1.0 - a) + (1.0 - b) for a, b in zip(q, q[1:])) / 2  # trapezoid, hour units
    worst = 1.0 - min(q)
    down = [t for t, v in enumerate(q) if v < 1.0]
    if not down:
        return round(loss, 2), worst, 0, False
    recovered = q[-1] >= 1.0
    ttr = (max(down) + 1 - min(down)) if recovered else None
    return round(loss, 2), round(worst, 2), ttr, not recovered

scenarios = {
    "A_deep_short": curve(drop_at=2, depth=0.90, hold=3, recover_hours=4),
    "B_shallow_long": curve(drop_at=2, depth=0.25, hold=20, recover_hours=10),
    "C_unrecovered": curve(drop_at=30, depth=0.40, hold=30, recover_hours=6),
}
print("scenario        loss_h  worst  ttr_h  censored")
for name, q in scenarios.items():
    loss, worst, ttr, cens = metrics(q)
    print(f"{name:15} {loss:6.2f}  {worst:5.2f}  {str(ttr):5}  {cens}")
```

Saída esperada:

```text
scenario        loss_h  worst  ttr_h  censored
A_deep_short      4.95   0.90  7      False
B_shallow_long    6.38   0.25  30     False
C_unrecovered     7.40   0.40  None   True
```

Leia a saída com atenção. Pelo *pior desempenho*, A é muito pior do que B; pela *perda de área* e pelo *tempo até a recuperação*, B é pior do que A. O cenário C tem a maior perda de área na janela, mas sua perda é truncada na hora 48: a perda verdadeira é maior, e seu tempo até a recuperação é desconhecido. O laboratório demonstra três pontos da §1.6: as classificações dependem da métrica; a censura esconde os piores casos; e uma única "pontuação de resiliência" esconde um juízo de valor. Se A for uma perda de pressão da água que dispara um aviso de fervura e B for um período de pressão reduzida sem efeito sobre a saúde, nem a área nem a duração capturam a diferença decisiva — um limiar sobre a profundidade, sim.

### 1.11 Erros comuns e limites

- Tratar o rótulo de um setor como a definição de uma população.
- Alegar consequências a partir de observações cibernéticas sem a cadeia física e organizacional.
- Usar uma contagem de ativos ou uma centralidade de rede como medida de consequência.
- Relatar uma única métrica de resiliência sem justificá-la nem testar uma alternativa.
- Tirar a média de tempos de recuperação censurados.
- Solicitar dados operacionais de que a pergunta não precisa.
- Começar a coleta de dados antes que exista um acordo de publicação.
- Tratar "sintético" como motivo para pular o teste de sensibilidade: dados sintéticos calibrados para um lugar real ainda podem identificá-lo.

O limite deste capítulo é que as salvaguardas de integridade reduzem, mas não eliminam, o risco de resultados enganosos. Seu propósito é tornar os erros *detectáveis* por outras pessoas.

### Exercícios — capítulo 1

**EX001 — Auditoria pela escada de alegações.** *Objetivo:* separar observações de alegações de consequência. *Entradas:* a afirmação sintética "Os logs mostram que o atacante acessou o sistema de gestão da distribuição da REC às 01:52; a queda resultante deixou o hospital sem energia e pacientes foram postos em perigo; isso mostra que as cooperativas rurais são o ponto mais fraco da rede elétrica." *Restrições:* use os cinco degraus da §1.1.3. *Passos:* (1) divida a afirmação em suas asserções componentes; (2) atribua um degrau a cada uma; (3) nomeie o pressuposto oculto por trás de cada uma; (4) nomeie uma observação que derrotaria cada uma; (5) reescreva a afirmação para que ela alegue apenas o que as evidências poderiam apoiar. *Evidência esperada:* tabela e reescrita. *Rubrica:* 3 = toda asserção corretamente posicionada na escada, a reserva do gerador do hospital e a generalização sinalizadas, reescrita devidamente delimitada; 2 = uma asserção posicionada errado; 1 = a reescrita ainda alega demais; 0 = nada.

**EX002 — Definição e população.** *Objetivo:* ver como as definições jurídicas mudam a população de um estudo. *Entradas:* o NSM-22 (pela página da CISA), a Diretiva CER e a NIS2, tal como citados na §1.1.1. *Restrições:* não parafraseie de memória; cite o texto definidor em que você se apoia, com o artigo ou a seção. *Passos:* (1) para um hospital regional, uma pequena concessionária de água potável e um processador de pagamentos, declare se cada um está no escopo de cada instrumento e em qual categoria; (2) nomeie uma consequência das diferenças para um estudo comparativo entre jurisdições. *Evidência esperada:* tabela 3 × 3 com citações e um parágrafo. *Rubrica:* 3 = preciso, com citações exatas e uma consequência de desenho sólida; 2 = um erro de categoria; 1 = sem citações; 0 = nada.

**EX003 — Tipificação das interdependências.** *Objetivo:* aplicar os tipos de Rinaldi et al. *Entradas:* as dependências de Riverbend: TEL de F2; HOSP de F2 e de WATER; WATER de F3; o SCADA da água de TEL; o faturamento da cooperativa de eletricidade do processador de pagamentos; as entregas de combustível para os geradores do acesso rodoviário. *Restrições:* um tipo primário por relação, justificado. *Passos:* classifique cada uma como física, cibernética, geográfica ou lógica; identifique qualquer ciclo; declare qual dependência um modelo puro de fluxo de potência omitiria. *Evidência esperada:* tabela e um parágrafo. *Rubrica:* 3 = tipos justificados, ausência de ciclo entre os serviços listados observada, combustível/estrada e faturamento identificados como fora de um modelo de fluxo de potência; 2 = uma classificação errada; 1 = sem justificativa; 0 = nada.

**EX004 — Análise pelo Menlo.** *Objetivo:* identificar as partes interessadas e as salvaguardas. *Entradas:* a pergunta revisada do Cascade Study na §1.9, que inclui entrevistas com despachantes da REC e um exercício de mesa. *Restrições:* use os quatro princípios; pelo menos seis partes interessadas. *Passos:* liste as partes interessadas; para cada princípio, nomeie o principal risco e uma salvaguarda; nomeie a autoridade de parada e os dados que são destruídos se o parceiro se retirar. *Evidência esperada:* tabela de partes interessadas e tabela de salvaguardas. *Rubrica:* 3 = população atendida, risco disciplinar para a equipe, sensibilidade da informação e pressão do parceiro tratados com salvaguardas concretas; 2 = um princípio fraco; 1 = genérico; 0 = nada.

**EX005 — Teste de sensibilidade.** *Objetivo:* decidir o que pode ser publicado. *Entradas:* cinco artefatos: (a) durações de restauração agregadas por classe de alimentador; (b) uma lista de hospitais com os dias de combustível dos geradores; (c) o código do modelo; (d) o quadro de codificação das entrevistas; (e) um mapa de qual alimentador atende a estação regional de tratamento de água. *Restrições:* aplique a §1.5.2; proponha um nível: público, controlado, retido. *Passos:* (1) decida se cada artefato identifica um ativo, uma localização, uma vulnerabilidade ou uma dependência específicos; (2) atribua um nível; (3) justifique o nível; (4) proponha uma transformação que permitiria uma liberação mais ampla. *Evidência esperada:* tabela. *Rubrica:* 3 = (b) e (e) retidos ou transformados, (a) e (c) públicos, (d) público se não houver citações, com transformações; 2 = um mal julgado; 1 = todos públicos ou todos retidos; 0 = nada.

**EX006 — Inversão de métricas.** *Objetivo:* usar o Laboratório 1. *Entradas:* o código do laboratório. *Restrições:* offline. *Passos:* (1) execute o laboratório e registre a saída; (2) acrescente uma quarta métrica, "horas abaixo de 0,5", e relate-a para todos os cenários; (3) mude a janela para 72 horas e relate o que acontece com C; (4) escreva 150 palavras sobre qual métrica você escolheria como primária para um serviço de água potável e por quê. *Evidência esperada:* mudança no código, saídas, parágrafo. *Rubrica:* 3 = valores corretos, C deixa de ser censurado, com perda maior, escolha da métrica justificada por um limiar de saúde; 2 = um valor errado; 1 = sem justificativa; 0 = não executado.

**EX007 — Esqueleto de protocolo.** *Objetivo:* escrever um protocolo auditável. *Entradas:* a pergunta revisada da §1.9. *Restrições:* todos os doze elementos da §1.8; no máximo três páginas. *Passos:* (1) redija, em ordem, cada um dos doze elementos do protocolo da §1.8; (2) marque cada elemento como fixado ou em aberto; (3) escreva duas condições de parada e duas condições de abandono; (4) liste o que um revisor hostil atacaria primeiro. *Evidência esperada:* rascunho do protocolo. *Rubrica:* 3 = todos os elementos concretos, condições de parada e de abandono distintas, proteção da informação específica; 2 = um ou dois elementos vagos; 1 = faltam segurança ou acordos; 0 = nada.

### Síntese do capítulo

A pesquisa sobre infraestrutura estuda as consequências para as pessoas por meio de cadeias de mecanismos físicos, cibernéticos e organizacionais que o pesquisador raramente observa diretamente. Suas evidências vêm de incidentes raros e relatados seletivamente, de dados operacionais protegidos, de testbeds pequenos, de modelos e de pessoas; cada fonte tem vieses característicos e precisa ser triangulada. As salvaguardas de integridade — pré-especificação, registros de desvios, declarações — são necessárias porque os parceiros são regulados, os financiadores têm interesses e as simulações são flexíveis. Os riscos de segurança e de duplo uso são reais: nunca teste em produção, simule primeiro, separe a capacidade da consequência na publicação e nomeie uma autoridade de parada. As informações sobre dependências e reservas são sensíveis mesmo quando aproximadas. As métricas de resiliência embutem juízos de valor; escolha-as para a decisão em questão e mostre se as conclusões sobrevivem às alternativas. O protocolo é o contrato que torna tudo isso auditável.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 08

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestrutura crítica e segurança setorial: fronteira da pesquisa

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Pesquisar a literatura dispersa sobre segurança e resiliência da infraestrutura na engenharia, na pesquisa operacional, na economia, nas políticas públicas e na segurança computacional, com um protocolo documentado e repetível.
2. Explicar as principais famílias de modelos de interdependência, o que cada uma pressupõe e que tipo de alegação cada uma pode apoiar.
3. Ler normas e regulamentações — NIST CSF 2.0, NIST SP 800-82, IEC 62443, NERC CIP, NIS2, CER e orientações setoriais — como *objetos de pesquisa* cuja eficácia é, ela própria, uma questão em aberto.
4. Avaliar criticamente a pesquisa de detecção e de testbeds quanto às armadilhas de avaliação documentadas na literatura de segurança e de séries temporais.
5. Classificar uma lacuna de evidências (ausente, fraca, conflitante, não transferida) e converter um tema numa declaração de contribuição falseável.

O Capítulo 1 forneceu a escada de alegações e as fontes de evidência; este capítulo as usa para ler o campo. O Capítulo 3 transformará a lacuna escolhida aqui numa proposta de contribuição.

### 2.1 Por que a literatura é difícil de encontrar

Um doutorando em segurança da infraestrutura herda pelo menos cinco literaturas que raramente se citam:

| Comunidade | Perguntas típicas | Veículos e vocabulário típicos |
|---|---|---|
| Engenharia de confiabilidade e de risco | Propagação de falhas, restauração, métricas de risco, curvas de resiliência | *Reliability Engineering & System Safety*, *Risk Analysis*; "inoperability", "resilience triangle", "fragility". |
| Engenharia de energia, água e transportes | Física das redes, proteção, sequenciamento da restauração | Periódicos do IEEE de energia e redes inteligentes, periódicos de recursos hídricos; "service restoration", "black start", "pressure zone". |
| Pesquisa operacional | Programação, projeto de redes, interdição | Periódicos de PO; "weighted completion time", "interdiction", "stochastic program". |
| Segurança computacional e de TO | Ataques, detecção, testbeds, protocolos | Conferências de segurança e workshops de segurança de sistemas ciberfísicos; "anomaly detection", "testbed", "threat model". |
| Políticas públicas, direito e gestão | Regulação, parcerias, incentivos, notificação | Periódicos de políticas e relatórios governamentais; "sector risk management", "public–private partnership", "critical entity". |

Veículos dedicados, como o *International Journal of Critical Infrastructure Protection* e a série de conferências CRITIS, fazem a ponte entre algumas dessas comunidades, mas uma busca restrita aos veículos de segurança deixará de fora a maior parte do trabalho sobre restauração e interdependência, e uma busca restrita à engenharia deixará de fora o trabalho orientado por ameaças. O framework de Rinaldi, Peerenboom e Kelly ([2001](https://doi.org/10.1109/37.969131)) é o ancestral comum mais frequente e uma boa semente para o encadeamento de citações nas duas direções.

### 2.2 Mapeamento sistemático entre disciplinas

#### 2.2.1 Escolhendo o tipo de revisão

Uma **revisão sistemática** responde a uma pergunta focada com uma busca exaustiva e uma avaliação crítica formal; uma **revisão de escopo** mapeia a extensão e a natureza de um corpo de trabalhos; uma **revisão narrativa** é uma síntese especializada sem busca reprodutível. Para um capítulo de fronteira de doutorado, uma revisão de escopo com protocolo documentado costuma ser o certo: ela é reprodutível, mostra a forma do campo e identifica onde uma revisão sistemática seria prematura. Relate-a usando os itens pertinentes do [PRISMA 2020](https://doi.org/10.1136/bmj.n71) — fontes da busca, datas, cadeias de busca, triagem, motivos de exclusão e um diagrama de fluxo —, mesmo onde a checklist completa não se aplica.

#### 2.2.2 Um protocolo de busca para o Cascade Study

1. **Pergunta.** O que se sabe sobre o efeito da ordenação da restauração, informada pelas dependências intersetoriais, sobre as consequências das quedas de infraestrutura, incluindo as quedas induzidas por ciberataques?
2. **Blocos de conceitos.** (restoration OR recovery OR "service restoration" OR prioritization) AND (interdependen* OR dependen* OR cascad*) AND (infrastructure OR utility OR "distribution system" OR "lifeline").
3. **Fontes.** Pelo menos um índice de engenharia, um índice acadêmico geral e uma fonte de políticas (relatórios governamentais, relatórios pós-ação), mais o encadeamento de citações para trás e para frente a partir de dois artigos-semente.
4. **Elegibilidade.** Estudos que comparam pelo menos duas ordenações de restauração ou que quantificam a consequência impulsionada por dependências; excluir as classificações de vulnerabilidade puramente topológicas que não modelam o serviço.
5. **Triagem.** Dois triadores numa amostra de títulos e resumos, com a concordância medida antes da divisão do trabalho; divergências resolvidas por discussão e registradas.
6. **Quadro de codificação.** Família de modelo; tipo de validação (nenhuma, de face, histórica, de campo); fonte dos dados; se os autores também construíram o testbed ou o modelo que avaliam; métrica de desfecho; tipo de perigo (natural, acidental, cibernético); linha de base de comparação.
7. **Regra de parada.** Parar o encadeamento quando duas rodadas consecutivas não acrescentarem nenhum estudo elegível.

#### 2.2.3 Avaliação crítica de modelos e simulações

As ferramentas de avaliação clínica se encaixam mal. Para artigos baseados em modelos, avalie: a estrutura do modelo é justificada pelo mecanismo que ele representa? Os parâmetros têm fonte? A implementação foi verificada (o código faz o que o artigo diz)? O modelo foi validado, e contra o quê — validade de face, eventos históricos, dados de campo ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20))? Há uma análise de sensibilidade? A linha de base de comparação é forte? O código e as entradas estão disponíveis? Um artigo de modelagem que não consegue responder às perguntas de verificação e validação apoia, no máximo, uma alegação sobre o modelo, e não sobre a infraestrutura.

### 2.3 O panorama de políticas e normas como objeto de pesquisa

Normas e regulamentações não são apenas pano de fundo; se elas funcionam é uma das maiores questões em aberto do campo. O panorama atual (verifique as versões antes de citar):

- O **NIST Cybersecurity Framework 2.0** ([CSWP 29, fevereiro de 2024](https://doi.org/10.6028/NIST.CSWP.29)) acrescentou uma função *Govern* às funções Identify, Protect, Detect, Respond e Recover. Ele é orientado a resultados e voluntário na maioria dos setores; pergunta de pesquisa: as organizações que o adotam sofrem perturbações menos frequentes ou de menor consequência, e como se saberia disso?
- A **NIST SP 800-82 Rev. 3** ([setembro de 2023](https://doi.org/10.6028/NIST.SP.800-82r3)) ampliou o escopo dos sistemas de controle industrial para a tecnologia operacional e acrescentou um overlay de TO para os controles da SP 800-53 Rev. 5. Um rascunho público inicial da Rev. 4 foi divulgado em setembro de 2026 ([CSRC](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).
- A **ISA/IEC 62443** é uma série de normas para a segurança de sistemas de automação e controle industrial. A parte 3-2 define o sistema em consideração, particiona-o em **zonas** e **condutos**, avalia o risco e atribui um **nível de segurança-alvo (SL-T)**; a parte 3-3 declara os requisitos do sistema sob sete requisitos fundamentais — controle de identificação e autenticação, controle de uso, integridade do sistema, confidencialidade dos dados, fluxo de dados restrito, resposta oportuna a eventos e disponibilidade de recursos ([página de catálogo da IEC 62443-3-2](https://webstore.iec.ch/en/publication/30727)). Pergunta de pesquisa: um SL-T atribuído prediz a resistência a adversários realistas, e como os níveis de segurança alcançados podem ser medidos, em vez de afirmados?
- As normas de confiabilidade **NERC CIP** são obrigatórias para o sistema elétrico de grande porte da América do Norte. Em junho de 2025, a FERC aprovou a [CIP-015-1 sobre monitoramento da segurança da rede interna](https://www.federalregister.gov/documents/2025/07/02/2025-12309/critical-infrastructure-protection-reliability-standard-cip-015-1-cyber-security-internal-network) (Order No. 907), com implementação escalonada ao longo de anos ([página da norma na NERC](https://www.nerc.com/standards/reliability-standards/cip/cip-015-1)). Uma norma obrigatória com implantação escalonada é um experimento natural — se os pesquisadores conseguirem obter dados de desfecho, o que raramente acontece.
- A **NIS2 e a CER da UE** (ambas de 2022) impõem obrigações de gestão de riscos e de notificação às entidades essenciais e importantes e obrigações de resiliência às entidades críticas; a transposição nacional varia, o que cria uma variação entre países de interesse para a pesquisa.
- **Finanças.** O [Guidance on cyber resilience for financial market infrastructures](https://www.bis.org/cpmi/publ/d146.htm) do CPMI–IOSCO (junho de 2016) complementa os Principles for Financial Market Infrastructures; é a fonte da expectativa amplamente discutida de que as operações críticas sejam projetadas para retomar rapidamente depois de uma perturbação, o que cria uma tensão entre a velocidade da retomada e a integridade dos dados — um problema de pesquisa sem resposta assentada.
- A **Consequence-driven Cyber-informed Engineering (CCE)**, desenvolvida no Idaho National Laboratory, avança por quatro fases — priorização das consequências, análise do sistema de sistemas, escolha de alvos baseada nas consequências, e mitigações e proteções ([página do CCE no INL](https://inl.gov/national-security/cce/); [Bochman and Freeman, 2021](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710)). Ela parte das consequências, e não das vulnerabilidades, o que se alinha à ênfase deste livro; se ela produz melhores escolhas de mitigação do que os métodos orientados por vulnerabilidades não foi, até onde o autor sabe, testado com desenhos comparativos.

A lacuna de pesquisa comum a todo o panorama são as **evidências de desfecho**: os frameworks são justificados pelo consenso de especialistas e pelas lições de incidentes, mas estudos comparativos que liguem sua adoção às consequências são raros, porque os dados de desfecho são raros, protegidos e confundidos pela maturidade organizacional.

### 2.4 Famílias de modelagem de interdependências

[Ouyang (2014)](https://doi.org/10.1016/j.ress.2013.06.040) revisou a modelagem e a simulação de sistemas de infraestrutura interdependentes e agrupou as abordagens em empíricas, baseadas em agentes, baseadas em dinâmica de sistemas, baseadas em teoria econômica, baseadas em redes e outras. Cada família apoia um tipo diferente de alegação.

| Família | Ideia central | Apoia alegações sobre | Principais limites |
|---|---|---|---|
| Empírica | Analisar registros de perturbações passadas e de sua propagação | O que aconteceu; frequência dos tipos de dependência nos relatórios | Viés de notificação; poucos eventos; sem contrafactuais |
| Baseada em agentes | Simular tomadores de decisão e ativos autônomos | Comportamento emergente, decisões dos operadores | Muitos parâmetros; validação difícil |
| Dinâmica de sistemas | Estoques, fluxos e laços de realimentação ao longo do tempo | Dinâmica agregada, realimentação de políticas | Grosseira; estrutura presumida |
| Econômica (insumo-produto) | Propagação ao estilo de Leontief da inoperabilidade ou da perda de produção entre setores ([Haimes and Jiang, 2001](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1))) | Perda econômica em nível setorial e classificação | Linear, estática ou quase estática; a agregação setorial esconde as instalações |
| Rede — topologia | Grafos e percolação | Fragilidade estrutural; regimes qualitativos de cascata | Sem fluxos, reservas nem operadores |
| Rede — fluxo | Fluxos físicos (fluxo de potência, hidráulica) em redes | Consequências de engenharia dentro de um setor | Exige muitos dados; acoplamento intersetorial difícil |
| Cossimulação | Acoplar simuladores de domínio (energia, água, comunicações) | Temporização intersetorial com fidelidade física | Erro de integração; sincronização; pesada |

**Cascatas topológicas.** [Buldyrev et al. (2010)](https://doi.org/10.1038/nature08932) mostraram, num modelo de percolação de duas redes interdependentes, que o acoplamento pode produzir um colapso abrupto e catastrófico e que, diferentemente do que ocorre em redes isoladas, distribuições de grau mais amplas podem aumentar a vulnerabilidade a falhas aleatórias. O resultado é um marco do entendimento estrutural. Também é uma fonte frequente de alegações excessivas: o modelo pressupõe dependência de tudo ou nada, nenhuma reserva, nenhuma restauração e padrões de acoplamento específicos. Citá-lo como evidência de que a energia e as comunicações de uma cidade específica vão colapsar abruptamente é um erro de categoria — um entendimento estrutural L5 apresentado como alegação de consequência L4.

**Inoperabilidade de insumo-produto.** O modelo de insumo-produto de inoperabilidade (IIM) escreve o vetor de inoperabilidade de equilíbrio *q* como *q* = *A\*q* + *c\**, de modo que *q* = (*I* − *A\**)⁻¹ *c\**, em que *A\** contém os coeficientes de interdependência e *c\**, uma perturbação inicial. O Capítulo 4 replica um cálculo do IIM e mostra como um erro de convenção da matriz muda silenciosamente os resultados.

**Onde ficam as reservas.** Um tema comum às famílias é que a temporização das consequências é governada pelas **reservas** — combustível dos geradores, autonomia das baterias, armazenamento, estoques, procedimentos manuais —, que a topologia ignora e que os modelos de fluxo muitas vezes mantêm constantes. A pesquisa de restauração na engenharia de potência modela o sequenciamento, mas frequentemente dentro de um único setor e com o objetivo de clientes ou carga restaurados. O Cascade Study fica nessa junção: a temporização intersetorial das reservas como motor da *ordenação da restauração*.

### 2.5 Pesquisa de detecção e de testbeds: a avaliação como fronteira

Boa parte da literatura do lado da segurança estuda a detecção de ataques em processos industriais. Seus problemas estão cada vez mais bem documentados:

- **Avaliação em mundo fechado.** [Sommer and Paxson (2010)](https://doi.org/10.1109/SP.2010.25) argumentaram que a detecção de intrusões por aprendizado de máquina se ajusta mal ao mundo aberto e mutável das redes reais, e que as avaliações muitas vezes não capturam o custo dos erros nem a distância semântica entre uma anomalia e um ataque.
- **Armadilhas na pesquisa de segurança com AM.** [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) identificaram dez armadilhas — entre elas o viés de amostragem, a contaminação de dados (data snooping), correlações espúrias, linhas de base e métricas inadequadas, a falácia da taxa-base, a avaliação apenas em laboratório e modelos de ameaça inadequados — e encontraram várias delas em cada um dos 30 artigos de veículos de ponta que revisaram.
- **Métricas infladas de séries temporais.** [Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) mostraram que o protocolo de *ajuste de pontos*, comum na detecção de anomalias em séries temporais, que marca todo um segmento anômalo como detectado se qualquer ponto dele for sinalizado, pode fazer até pontuações aleatórias parecerem o estado da arte; eles propuseram o PA%K. O Capítulo 4 reproduz o efeito.
- **Testbeds pequenos, antigos e construídos pelos autores.** Conjuntos de dados públicos de testbeds como o SWaT ([Goh et al., 2016](https://doi.org/10.1007/978-3-319-71368-7_8)) e a competição de distribuição de água BATADAL ([Taormina et al., 2018](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969)) viabilizaram comparações, o que é uma contribuição importante. Eles também concentram o campo em poucos sistemas com conjuntos de ataques específicos; os resultados só se transferem para outras plantas por argumentação.

Para uma tese de IC, a detecção importa sobretudo como **reserva contra a consequência**: uma detecção que chega depois de esgotada a reserva de um serviço não muda nada para as pessoas atendidas. Enquadrar a detecção pelo tempo até a consequência, e não pelo F1, é uma ponte pouco explorada entre as duas literaturas.

### 2.6 Evidências setoriais e sobre ameaças

- **Energia.** O ataque de 2015 à distribuição ucraniana, documentado pelo [E-ISAC e pelo SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and), é o caso público mais citado de um ciberataque que causou quedas para clientes; é também um único caso, com a restauração alcançada por meio da operação manual.
- **Água.** Os sistemas de água são numerosos, muitas vezes pequenos e com poucos recursos, o que torna difícil coletar evidências de todo o setor; boa parte do trabalho quantitativo usa redes de distribuição simuladas, como a da BATADAL.
- **Saúde.** [Neprash et al. (2022)](https://doi.org/10.1001/jamahealthforum.2022.4873) documentaram um número crescente de ataques de ransomware a organizações prestadoras de cuidados de saúde dos EUA de 2016 a 2021 e seus efeitos sobre as operações; trabalhos desse tipo ligam um evento cibernético à prestação de cuidados — o degrau da consequência — usando dados públicos e regulatórios.
- **Mudança no modelo de ameaças.** O alerta conjunto [AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) da CISA (fevereiro de 2024) avaliou que um ator patrocinado por um Estado conhecido como Volt Typhoon se pré-posicionou nas redes de TI de organizações de comunicações, energia, transporte e água para viabilizar uma possível perturbação, usando contas válidas e técnicas living-off-the-land. Para a pesquisa, o pré-posicionamento significa que o cenário pertinente é uma perturbação *simultânea, multissetorial e no momento escolhido pelo adversário* — exatamente onde as regras de restauração de um único setor podem falhar.
- **Precedente ciberfísico.** A [análise de Langner de 2013 sobre o Stuxnet](https://archive.org/details/to-kill-a-centrifuge) é um relato clássico de um ataque ciberfísico projetado em torno do conhecimento do processo. Sua lição para a pesquisa de IC é que os ataques com consequência são projetados contra os processos físicos e suas margens de segurança, e é por isso que existem métodos que partem das consequências, como o CCE.

### 2.7 Classificando a lacuna

O livro de doutorado de RI distingue quatro tipos de lacuna de evidências; eles se aplicam aqui sem mudanças:

| Tipo de lacuna | Significado | Exemplo em infraestrutura | Próximo estudo certo |
|---|---|---|---|
| Ausente | Nenhum estudo trata da pergunta | Nenhum teste comparativo do CCE contra a priorização orientada por vulnerabilidades | Primeiro desenho comparativo, mesmo que pequeno |
| Fraca | Existem estudos, mas eles não conseguem apoiar a alegação | Benefícios da ordenação da restauração mostrados apenas em modelos não validados, construídos pelos proponentes | Validação independente; linhas de base mais fortes |
| Conflitante | Estudos críveis discordam | Modelos topológicos e de fluxo classificam os mesmos ativos de modo diferente | Estudo que discrimine entre os mecanismos |
| Não transferida | Existem evidências em outro domínio | Evidências do planejamento de pico hospitalar não aplicadas à ordenação da restauração | Teste de transferência com condições de fronteira explícitas |

### 2.8 Exemplo resolvido: avaliação crítica da literatura sobre ordenação da restauração (sintético)

A revisão de escopo do Cascade Study (sintética) encontrou oito artigos elegíveis, P1–P8:

| ID | Família | Validação | Independente do próprio modelo ou testbed dos autores? | Alegação apoiada |
|---|---|---|---|---|
| P1 | Topologia de rede | Nenhuma | Não | C1 a centralidade identifica os ativos de maior consequência |
| P2 | Topologia de rede | De face (revisão por especialistas) | Não | C1 |
| P3 | Insumo-produto | Histórica (queda regional) | Sim | C2 o IIM classifica os setores pela perda econômica |
| P4 | Baseado em agentes | De face | Não | C3 a restauração ciente das dependências reduz a perda crítica |
| P5 | Cossimulação | Histórica | Não | C3 |
| P6 | Insumo-produto | Histórica | Sim | C2 |
| P7 | Cossimulação | De campo (exercício de concessionária) | Sim | C3 |
| P8 | Empírico | De campo (registros pós-ação) | Sim | C4 a duração da energia de reserva domina a temporização da cascata |

Avaliação crítica: C1 só tem evidências topológicas autovalidadas — é *fraca*. C2 tem duas validações históricas independentes — a alegação mais forte do conjunto, embora trate de perda econômica, e não de serviço. C3 tem três estudos, mas apenas um independente e fortemente validado; P4 e P5 foram avaliados nos próprios modelos dos autores, o que convida à circularidade modelo–política (Capítulo 6). C4 se apoia num único estudo empírico. A fronteira é, portanto, C3: plausível, repetidamente *proposta*, fracamente *testada*.

### 2.9 Atividade prática: codifique o mapa da literatura

```python
# Lab 2 - coding a synthetic literature map for interdependency-modelling claims (offline)
# Fields: id, model family, validation, independent of authors' own testbed?, claim supported
studies = [
    ("P1", "network-topology", "none",       False, "C1"),
    ("P2", "network-topology", "face",       False, "C1"),
    ("P3", "input-output",     "historical", True,  "C2"),
    ("P4", "agent-based",      "face",       False, "C3"),
    ("P5", "co-simulation",    "historical", False, "C3"),
    ("P6", "input-output",     "historical", True,  "C2"),
    ("P7", "co-simulation",    "field",      True,  "C3"),
    ("P8", "empirical",        "field",      True,  "C4"),
]
claims = {
    "C1": "Topological centrality identifies the assets whose loss causes the largest service cascade",
    "C2": "Input-output inoperability ranks sectors by economic loss after a regional outage",
    "C3": "Dependency-aware restoration lowers critical-service loss compared with siloed restoration",
    "C4": "Backup-power duration is the dominant buffer controlling cascade timing",
}
STRONG = {"historical", "field"}
for cid, text in claims.items():
    rows = [s for s in studies if s[4] == cid]
    strong_indep = [s[0] for s in rows if s[2] in STRONG and s[3]]
    if len(strong_indep) >= 2:
        state = "supported (>=2 independent strong validations)"
    elif strong_indep:
        state = "single-source; needs replication"
    else:
        state = "open: no independent strong validation"
    print(f"{cid}: {state}; evidence={[s[0] for s in rows]}; strong+independent={strong_indep}")
```

Saída esperada:

```text
C1: open: no independent strong validation; evidence=['P1', 'P2']; strong+independent=[]
C2: supported (>=2 independent strong validations); evidence=['P3', 'P6']; strong+independent=['P3', 'P6']
C3: single-source; needs replication; evidence=['P4', 'P5', 'P7']; strong+independent=['P7']
C4: single-source; needs replication; evidence=['P8']; strong+independent=['P8']
```

Registre a saída exata no seu diário de reprodução, e não uma paráfrase.

A regra codificada em `STRONG` e no indicador de independência é uma *escolha*. Mudá-la muda quais alegações estão "apoiadas". Um mapa da literatura precisa publicar sua regra de codificação para que os leitores possam discordar dela explicitamente.

Duas verificações valem a pena antes de confiar no mapa. Primeiro, execute-o sem o indicador de independência: C3 passa então a contar P5 como validação forte e é relatada como apoiada, o que mostra quanto do veredito repousa sobre essa única decisão de codificação. Segundo, peça a um segundo codificador que classifique a validação e a independência dos oito artigos sem ver a planilha do primeiro, e registre onde eles divergem. A divergência sobre se um exercício de concessionária conta como validação de campo, como em P7, é uma constatação sobre o quadro de codificação, e o quadro deve ser estreitado antes que o mapa seja usado para escolher uma lacuna.

### 2.10 Do mapa à fronteira: o teste da contribuição

Uma lacuna se torna uma contribuição de doutorado quando passa em quatro testes: **Aberta** — a busca documentada mostra que ela ainda não foi respondida; **Importante** — uma resposta mudaria uma decisão que alguém de fato toma (aqui, a ordenação da restauração nas operações de emergência); **Viável** — dados, modelos, parceiros e ética a permitem dentro do programa; **Falseável** — uma observação declarada mostraria que a alegação está errada. Formato de redação: *"Em [população/contexto], [intervenção], em comparação com [a linha de base mais forte], mudará [a métrica primária] em pelo menos [o menor efeito de interesse] sem piorar [a métrica de segurança] além de [a margem]; isto será refutado se [observação]."*

A declaração do Cascade Study (a ser refinada no Capítulo 3): *Em quedas da distribuição que exigem a restauração manual e sequencial dos alimentadores, ordenar pelo tempo até o impacto dos serviços críticos, em comparação com ordenar pelos clientes restaurados, reduz a perda ponderada de serviços críticos declarada com antecedência em pelo menos 20%, aumentando os clientes-hora perdidos em não mais de 15%; isto é refutado se a redução ficar abaixo de 20% num modelo de uma segunda região construído de forma independente, ou se operadores num exercício de mesa cego não escolherem essa ordenação quando receberem as mesmas informações.*

### 2.11 Erros comuns e limites

- Buscar apenas em veículos de segurança e declarar uma lacuna que a engenharia já preencheu.
- Citar resultados de percolação como previsões de consequência para lugares específicos.
- Tratar as normas como evidências de eficácia, e não como hipóteses sobre ela.
- Comparar artigos de detecção pelo F1 de destaque sem conferir o protocolo de avaliação.
- Contar estudos em vez de avaliar sua independência e sua validação.
- Escrever uma lacuna como um tema ("interdependências em cidades inteligentes"), e não como uma declaração falseável.

- Tratar um veículo dedicado, como a série CRITIS, como se cobrisse o campo inteiro, quando a maior parte do trabalho sobre restauração aparece em veículos de engenharia e de pesquisa operacional.
- Ler a adoção ampla de um framework como evidência de desfecho; a adoção mostra que as pessoas o escolheram, e não que as consequências diminuíram.
- Codificar um artigo como independente porque seus autores são outros que não os proponentes, sem conferir se ele reutiliza o modelo ou o testbed dos proponentes.
- Encerrar cedo o encadeamento de citações porque as primeiras rodadas confirmaram a lacuna esperada.

### Exercícios — capítulo 2

**EX008 — Protocolo de busca.** *Objetivo:* escrever uma busca reprodutível entre disciplinas. *Entradas:* uma pergunta de sua escolha sobre segurança ou resiliência da infraestrutura. *Restrições:* pelo menos três tipos de fonte (índice de engenharia, índice geral, fonte de políticas); encadeamento de citações. *Passos:* (1) declare a pergunta; (2) construa os blocos de conceitos e as cadeias de busca; (3) defina a elegibilidade e os motivos de exclusão; (4) defina a triagem, a concordância e a regra de parada. *Evidência esperada:* protocolo (≤ 2 páginas). *Rubrica:* 3 = repetível, entre disciplinas, concordância medida, regra de parada explícita; 2 = um elemento vago; 1 = apenas uma lista de palavras-chave; 0 = nada.

**EX009 — Avaliação crítica de um artigo de modelagem.** *Objetivo:* avaliar um artigo de simulação quanto à alegação que ele pode apoiar. *Entradas:* o estudo sintético P5 (cossimulação, validação histórica, modelo dos próprios autores). *Restrições:* use a §2.2.3. *Passos:* liste o que você conferiria quanto à estrutura, aos parâmetros, à verificação, à validação, à sensibilidade, à linha de base e à disponibilidade; declare a alegação mais forte que P5 pode apoiar e seu degrau. *Evidência esperada:* formulário de avaliação e uma alegação em uma frase. *Rubrica:* 3 = identifica como decisivos o modelo construído pelos autores, a verificação desconhecida, o evento histórico único e a força da linha de base, alegação limitada ao modelo; 2 = uma questão não percebida; 1 = aceita a alegação como L5; 0 = nada.

**EX010 — Adequação da família de modelos.** *Objetivo:* casar perguntas com famílias de modelagem. *Entradas:* quatro perguntas: (a) Quais setores perdem mais produção depois de uma semana de perda de energia regional? (b) Quanto tempo até um hospital perder a pressão da água depois da queda de um alimentador? (c) Os operadores compartilham combustível informalmente entre concessionárias durante quedas longas? (d) Um sistema de duas redes com acoplamento aleatório é propenso a um colapso abrupto? *Restrições:* uma família primária por pergunta, com um motivo e um limite. *Passos:* (1) reformule o que cada pergunta pede que você preveja ou explique; (2) escolha a família de modelagem primária da §2.4; (3) justifique a escolha pela alegação que ela apoia; (4) nomeie o limite mais importante da família para aquela pergunta. *Evidência esperada:* tabela. *Rubrica:* 3 = (a) insumo-produto, (b) fluxo/cossimulação ou modelo de reservas, (c) empírico/qualitativo ou baseado em agentes informado por entrevistas, (d) topologia/percolação, cada um com limites sólidos; 2 = uma inadequação; 1 = duas ou mais; 0 = nada.

**EX011 — A norma como hipótese.** *Objetivo:* transformar uma norma numa alegação testável. *Entradas:* as zonas, os condutos e o SL-T da IEC 62443-3-2 (§2.3). *Restrições:* uma hipótese testável; nomeie a medida de desfecho e um desenho viável. *Passos:* declare a alegação causal implícita da norma; escreva uma hipótese; proponha um desenho (p. ex., exercícios de red team em zonas de testbed com diferentes SL-T); nomeie dois fatores de confusão. *Evidência esperada:* uma página. *Rubrica:* 3 = hipótese observável, desenho seguro e viável, fatores de confusão reais (habilidade do avaliador, idade dos ativos); 2 = desenho vago; 1 = repete a norma; 0 = nada.

**EX012 — Conserte o mapa da literatura.** *Objetivo:* fazer uma regra de codificação corresponder a um padrão declarado. *Entradas:* Laboratório 2. *Restrições:* offline; mantenha todas as linhas. *Passos:* (1) acrescente um campo `hazard` (P5 e P7 "cyber", todos os demais "all-hazards"); (2) mude a regra para que uma alegação sobre quedas *induzidas por ciberataques* seja apoiada apenas por validações fortes e independentes com perigo "cyber"; (3) execute e registre a saída exata para C3; (4) explique em 100 palavras o que mudou e por que isso importa. *Evidência esperada:* código modificado, saída exata, explicação. *Rubrica:* 3 = código correto; C3 continua com fonte única (apenas P7), e o estudante observa que C1, C2 e C4 agora não têm apoio forte e independente para quedas *induzidas por ciberataques*, com uma explicação clara da transferência entre perigos; 2 = saída correta, explicação rala; 1 = regra errada; 0 = não executado.

**EX013 — Classifique a lacuna.** *Objetivo:* distinguir os tipos de lacuna. *Entradas:* quatro afirmações sintéticas: (a) "Dois estudos com modelos de fluxo discordam sobre se o armazenamento de água ou o combustível dos geradores domina a temporização da queda num hospital"; (b) "Existe pesquisa sobre a capacidade de pico hospitalar, mas nenhum estudo a liga à ordenação da restauração"; (c) "Três white papers de fornecedores alegam que sua plataforma reduz à metade o tempo de restauração"; (d) "Nenhum estudo da nossa busca documentada compara o CCE com a priorização orientada por vulnerabilidades." *Restrições:* um tipo para cada, justificado; proponha o próximo estudo. *Passos:* (1) reformule cada uma como uma pergunta; (2) liste as evidências sobre ela; (3) atribua um tipo de lacuna; (4) nomeie o estudo que a fecharia. *Evidência esperada:* quatro parágrafos. *Rubrica:* 3 = conflitante, não transferida, fraca, ausente, com próximos passos sólidos; 2 = um erro; 1 = dois erros; 0 = nada.

**EX014 — Declaração falseável e memorando de fronteira.** *Objetivo:* converter um tema numa contribuição. *Entradas:* o tema "resiliência dos sistemas de pagamento durante quedas regionais de energia". *Restrições:* use o formato de redação da §2.10; a observação refutadora precisa ser viável; 400–600 palavras; cite apenas fontes que você leu. *Passos:* (1) escreva a declaração; (2) aplique os quatro testes; (3) revise uma vez; (4) explique qual pergunta adjacente precisa ser respondida primeiro e por quê. *Evidência esperada:* declaração, notas dos testes, revisão, memorando. *Rubrica:* 3 = passa em todos os testes, com um refutador viável e uma ordenação justificada das perguntas; 2 = um teste fraco; 1 = ainda é um tema; 0 = nada.

### Síntese do capítulo

A fronteira da segurança da infraestrutura está espalhada por cinco literaturas com vocabulários diferentes; uma busca de doutorado precisa atravessá-las deliberadamente e documentar como. Normas e regulamentações são hipóteses sobre o que reduz a consequência, e as evidências de desfecho a seu respeito são escassas. Os modelos de interdependência vêm em famílias que apoiam alegações diferentes; os resultados topológicos dão entendimento estrutural, os modelos de insumo-produto dão a economia em nível setorial, e os modelos de fluxo ou de cossimulação dão a temporização de engenharia — nenhum substitui a validação. A pesquisa de detecção está melhorando sua prática de avaliação; para a IC, a detecção importa como uma reserva medida contra o tempo até a consequência. Avalie a independência e a validação, e não as contagens. A lacuna do Cascade Study — a ordenação da restauração ciente das dependências é muitas vezes proposta e fracamente testada — é aberta, importante, viável e pode ser tornada falseável.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 08

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Proposta de contribuição original

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Tipificar uma contribuição de doutorado (artefato, método, medição, constatação empírica, teoria) e declarar as evidências que cada tipo exige.
2. Especificar um mecanismo como uma cadeia de elos que prediz um *padrão* de resultados, incluindo onde a intervenção não deveria ajudar.
3. Representar as dependências intersetoriais como um grafo com reservas, calcular o tempo até o impacto e explicar o que a representação deixa de fora.
4. Relacionar a ordenação da restauração com a teoria clássica de programação (scheduling) e usar essa relação para escolher linhas de base e prever trocas.
5. Escrever hipóteses primária, de mecanismo, de contribuição sobre a melhor prática e de não inferioridade, com um menor efeito de interesse justificado.
6. Construir uma tabela de explicações rivais e um conjunto de condições de falha declaradas com antecedência que estreitariam ou abandonariam a alegação.

O Capítulo 2 identificou a lacuna: a ordenação da restauração ciente das dependências é muitas vezes proposta e fracamente testada. Este capítulo a transforma numa proposta que poderia estar errada. O Capítulo 4 replicará as linhas de base e pilotará o procedimento.

### 3.1 Que tipo de contribuição?

| Tipo | Exemplo em segurança de IC | Evidência mínima |
|---|---|---|
| Artefato | Uma cossimulação aberta de distribuição, água e telecomunicações | Testes de verificação; documentação; evidências de uso por outros |
| Método | Um procedimento para calcular prioridades de restauração a partir de dados de dependência | Comparação com a melhor prática atual em métricas declaradas, em mais de um contexto |
| Medição | Um instrumento validado para a duração das reservas ou a acurácia do mapa de dependências | Evidências de confiabilidade e de validade |
| Constatação empírica | "Os operadores já priorizam as instalações críticas, mas não usam a temporização das reservas" | Um estudo amostrado e documentado de operadores |
| Teoria | Um mecanismo que explica quando a ordenação ciente das dependências ajuda | Previsões que o discriminam das rivais, testadas |

A contribuição pretendida do Cascade Study é um **método com um mecanismo**: uma regra para ordenar a restauração (o artefato é incidental) e uma explicação de *quando* ela supera a prática atual. Dizer isso cedo importa, porque "construímos um simulador e nosso método venceu" é uma demonstração de artefato, e não uma contribuição de método.

### 3.2 A ordenação da restauração como problema de programação

Quando uma única equipe de restauração precisa restaurar os alimentadores um de cada vez, a ordenação da restauração é um **problema de programação em máquina única**: cada alimentador *j* é uma tarefa com tempo de processamento *p_j* (manobras manuais, inspeção, reenergização), e o objetivo depende do que está sendo minimizado.

- Se o objetivo for **clientes-hora perdidos**, cada alimentador contribui com (clientes em *j*) × (instante de conclusão *C_j*). Minimizar Σ *w_j C_j* numa máquina é resolvido exatamente ordenando as tarefas por *w_j / p_j* em ordem decrescente — a **regra de Smith** ([Smith, 1956](https://doi.org/10.1002/nav.3800030106)). Com tempos esperados de restauração iguais, isso é simplesmente "mais clientes primeiro". A ordenação convencional usada como linha de base neste livro não é, portanto, ingênua: ela é *ótima para clientes-hora* nesse cenário idealizado.
- Se o objetivo for a **perda de serviços críticos**, um serviço *s* alimentado pelo alimentador *j* só é perdido a partir do momento em que sua reserva *b_s* se esgota até que o alimentador seja restaurado: loss_s = *w_s* × max(0, *C_j* + lag − *b_s*). A reserva funciona como um prazo, e o objetivo se parece com o **atraso ponderado** (weighted tardiness). O atraso ponderado total em máquina única é fortemente NP-difícil ([Lenstra, Rinnooy Kan and Brucker, 1977](https://doi.org/10.1016/S0167-5060(08)70743-X)), então as regras práticas são heurísticas. Ordenar pelo prazo mais cedo — aqui, pelo menor tempo até o impacto — é uma heurística clássica que ignora os pesos.

Essa relação dá ao estudo três coisas que um enquadramento puramente de segurança deixaria escapar. Primeiro, uma **previsão teórica da troca**: qualquer ordenação que se afaste da regra de Smith precisa aumentar os clientes-hora esperados, então uma margem de não inferioridade sobre os clientes-hora não é opcional. Segundo, um **limite superior para o benefício alcançável**: com poucos alimentadores, a enumeração exaustiva dá uma ordenação oráculo para cada sorteio de cenário, o que mostra quanta margem qualquer heurística deixa. Terceiro, **um modo de falha conhecido da heurística proposta**: uma regra do menor tempo até o impacto ignora os pesos e o espalhamento (fan-out), então pode perder para uma regra que restaure o alimentador que protege mais serviços ponderados, mesmo que o primeiro impacto desse alimentador ocorra um pouco mais tarde. O Capítulo 6 mostra exatamente isso.

### 3.3 Grafos de dependência com reservas

#### 3.3.1 Representação

Represente cada relação fornecedor → dependente como uma aresta dirigida rotulada com a reserva do dependente para aquele fornecedor. Se o fornecedor *A* falha no instante *t_A*, o dependente *B* falha em *t_A* + *b_AB*, a menos que seja restaurado antes. Se *B* falha quando *qualquer* de seus fornecedores falha (um "OU" de falhas — sem redundância), o instante de falha de *B* é o mínimo sobre os caminhos de entrada, o que é um cálculo de caminho mínimo com as reservas como pesos das arestas.

#### 3.3.2 Laboratório do tempo até o impacto

```python
# Lab 3 - time-to-impact on a synthetic Riverbend dependency graph (offline, standard library only)
# Edge (supplier -> dependant, buffer_hours): the dependant fails `buffer_hours` after it loses that supplier.
import heapq
edges = [
    ("F2", "TEL", 8),     # telecom central office: batteries plus generator fuel on hand
    ("F2", "HOSP", 26),   # hospital: generator fuel on hand
    ("F3", "WATER", 9),   # treatment plant generator + clearwell storage
    ("F3", "WSCADA", 2),  # water SCADA server UPS
    ("TEL", "WSCADA", 0), # remote telemetry needs the carrier circuit
    ("WATER", "HOSP", 4), # hospital on-site water storage
    ("TEL", "DISPATCH", 1),  # emergency dispatch: ring-down backup lasts 1 h
    ("F1", "RES", 0), ("F4", "COM", 0),
]
def time_to_impact(initial):  # initial: {node: failure time}
    graph = {}
    for s, d, b in edges:
        graph.setdefault(s, []).append((d, b))
    best = dict(initial)
    pq = [(t, n) for n, t in initial.items()]
    heapq.heapify(pq)
    while pq:
        t, n = heapq.heappop(pq)
        if t > best.get(n, float("inf")):
            continue
        for d, b in graph.get(n, []):
            if t + b < best.get(d, float("inf")):
                best[d] = t + b
                heapq.heappush(pq, (t + b, d))
    return best
tti = time_to_impact({"F1": 0, "F2": 0, "F3": 0, "F4": 0})
for node in sorted(tti, key=lambda n: (tti[n], n)):
    print(f"{node:9} fails at t={tti[node]:>3} h")
degree = {}
for s, d, _ in edges:
    degree[s] = degree.get(s, 0) + 1
    degree[d] = degree.get(d, 0) + 1
print("degree ranking:", sorted(degree, key=lambda n: (-degree[n], n))[:4])
```

Saída esperada:

```text
COM       fails at t=  0 h
F1        fails at t=  0 h
F2        fails at t=  0 h
F3        fails at t=  0 h
F4        fails at t=  0 h
RES       fails at t=  0 h
WSCADA    fails at t=  2 h
TEL       fails at t=  8 h
DISPATCH  fails at t=  9 h
WATER     fails at t=  9 h
HOSP      fails at t= 13 h
degree ranking: ['TEL', 'F2', 'F3', 'HOSP']
```

Três lições. **Os caminhos indiretos predominam:** o gerador próprio do hospital dá 26 horas, mas ele falha na hora 13 pelo caminho da água (9 + 4). Um estudo que registrasse apenas a reserva de energia direta de cada instalação erraria sua prioridade em meio dia. **Grau não é consequência:** a centralidade de grau classifica TEL em primeiro lugar, o que é razoável aqui, mas classifica HOSP acima de WATER e nada diz sobre a temporização. **O pressuposto do OU é forte:** o SCADA da água falha na hora 0 + 0 via TEL *somente* se a telemetria não tiver caminho alternativo; em muitas concessionárias, os operadores conseguem operar a estação localmente sem o SCADA, então a falha de WSCADA pode não ter nenhuma consequência para o serviço. O grafo precisa distinguir a *perda de uma função* da *perda de um serviço*.

#### 3.3.3 O que a representação deixa de fora

Arestas com reservas fixas omitem: a **dinâmica do esgotamento** (o combustível de um gerador dura mais em carga parcial); a **redundância** (lógica "E" — um hospital com duas alimentações independentes só falha quando as duas falham); as **dependências da restauração** (um alimentador não pode ser reenergizado sem comunicações com as equipes de campo — uma dependência na direção da *recuperação*); as **reservas humanas** (operação manual, ajuda mútua, entregas de combustível que estendem as reservas se as estradas e as telecomunicações funcionarem); e a **adaptação do adversário** (um adversário que conheça a lista de prioridades pode visar o topo dela). Uma proposta precisa listar quais omissões poderiam inverter suas conclusões e como o estudo vai testá-las (§3.7).

### 3.4 O mecanismo

Um mecanismo é uma cadeia de elos, cada um dos quais poderia falhar, que prediz um *padrão*, e não apenas um efeito médio:

1. Os serviços críticos dependem de reservas cujas durações variam muito (horas para as baterias das telecomunicações e as reservas do despacho, dias para o combustível do hospital).
2. Numa queda de vários alimentadores que exige a restauração manual e sequencial, a ordem de restauração determina quais reservas se esgotam.
3. A prática convencional ou maximiza os clientes restaurados (regra de Smith) ou restaura primeiro os "clientes críticos", numa ordem que não usa a temporização das reservas.
4. Ordenar pelo tempo até o impacto restaura os alimentadores cujos serviços críticos falhariam primeiro, então menos reservas se esgotam.
5. Portanto, a perda ponderada de serviços críticos diminui.

O mecanismo prediz um padrão:

- **Benefício sobre a ordenação pelos clientes** sempre que os serviços críticos estiverem em alimentadores com poucos clientes.
- **Benefício sobre a ordenação por sinalização crítica apenas quando elas discordam** — quando a ordem por tempo das reservas entre os alimentadores críticos difere da ordem por número de clientes entre eles. Quando as ordens coincidem, as duas regras são idênticas e o benefício precisa ser zero.
- **Nenhum benefício quando as reservas excedem o tempo total de restauração** — se toda reserva durar mais do que a queda, a ordenação não pode importar para os serviços críticos.
- **Um custo em clientes-hora** em relação à regra de Smith, maior quando os serviços críticos estão em alimentadores pequenos.
- **Fragilidade diante de erros no mapa** — se o mapa de dependências ou as reservas estiverem errados, a ordenação pode ser pior do que uma simples lista de sinalização.

Um mecanismo que prediz onde a intervenção falha vale mais do que um que prediz apenas o sucesso, porque as falhas são o que o distingue das rivais.

### 3.5 Hipóteses, métricas e o menor efeito de interesse

Métrica primária: **perda ponderada de serviços críticos** numa janela de 72 horas, com pesos declarados com antecedência (hospital 5, água 4, telecomunicações 3, despacho de emergência 4 por hora de serviço), obtidos junto às equipes de gestão de emergências dos parceiros antes de qualquer simulação (Capítulo 1, §1.6.3). Métrica secundária (de segurança): **clientes-hora perdidos** (milhares).

- **H1 (benefício sobre a ordenação pelos clientes).** DEP reduz a perda ponderada média de serviços críticos em pelo menos 20% em comparação com SILO.
- **H2 (contribuição sobre a melhor prática).** DEP reduz a perda ponderada média de serviços críticos em pelo menos 10% em comparação com CRITFLAG (lista de sinalização de clientes críticos ordenada por clientes), em cada região do estudo.
- **H3 (padrão do mecanismo).** A diferença DEP − CRITFLAG é zero quando as duas ordens coincidem e cresce com o número de posições em que elas diferem; ela diminui em direção a zero à medida que as reservas crescem em relação ao tempo de restauração.
- **H4a/H4b (não inferioridade).** DEP aumenta os clientes-hora perdidos médios em no máximo 15% em comparação com SILO (H4a) e com CRITFLAG (H4b).

**Menores efeitos de interesse.** Os limiares de 20% e 10% e a margem de 15% são julgamentos *práticos*, e não convenções estatísticas: os parceiros declararam (sintético) que uma mudança na prática de restauração exige retreinamento, revisão de procedimentos e explicações ao regulador, o que só empreenderiam para uma redução de pelo menos 10% na perda de serviços críticos em relação à sua prática atual de sinalização crítica; e o conselho da cooperativa não aceitaria mais de 15% de clientes-hora adicionais sem consulta pública. Registre quem definiu cada limiar e quando; um limiar escolhido depois de ver os resultados não vale nada.

Observe que a teoria de programação prevê que H4a vai *falhar* sempre que os serviços críticos estiverem em alimentadores pequenos. Declará-la com antecedência mesmo assim é correto: o estudo deve relatar o tamanho da troca com honestidade em vez de escondê-lo, e um teste de não inferioridade que falha é uma constatação para os formuladores de políticas.

### 3.6 Linhas de base

Uma contribuição só é tão forte quanto a linha de base que ela supera.

| Linha de base | Por que incluí-la | O que superá-la mostraria |
|---|---|---|
| **SILO** — mais clientes primeiro | Ótima para clientes-hora com durações iguais (regra de Smith); padrão comum | Que a ordenação ciente da criticidade protege os serviços críticos — esperado e fraco como contribuição |
| **CRITFLAG** — primeiro os alimentadores com alguma instalação crítica listada, por clientes | Representa a prática difundida de manter listas de clientes críticos | A contribuição de fato: que a informação de *temporização* agrega valor além de uma lista |
| **ORACLE** — a melhor de todas as ordenações para cada sorteio (calculável para ≤ 6–7 alimentadores) | Limite superior para qualquer regra | Quanta margem resta; se DEP está perto do ótimo |
| **RANDOM** (opcional) | Verificação de sanidade | Que a métrica não é degenerada |

Superar SILO é necessário, mas não suficiente; a alegação vive ou morre diante de CRITFLAG. O exemplo resolvido em §3.9 mostra como uma proposta que omitisse CRITFLAG teria parecido impressionante e estaria errada.

### 3.7 Explicações rivais

| Rival | Previsão que a apoiaria | Característica do desenho que a testa |
|---|---|---|
| Qualquer lista de criticidade explica o ganho, e não a temporização | DEP ≈ CRITFLAG | Linha de base CRITFLAG; H2 |
| O ganho é um artefato dos pesos | O ganho desaparece com pesos iguais ou alternativos | Sensibilidade aos pesos (Capítulo 6) |
| O ganho é um artefato das reservas curtas na região escolhida | O ganho some com reservas realistas mais longas | Análise de escalonamento das reservas; segunda região com contratos de combustível |
| O modelo foi construído para favorecer DEP (circularidade) | O ganho diminui num modelo construído de forma independente ou com um mapa errado | Segunda região construída por outro modelador a partir dos dados dos parceiros; teste de erro do mapa |
| Os operadores não seguiriam a ordenação | As escolhas no exercício de mesa diferem de DEP mesmo com a exibição do tempo até o impacto | Exercício de mesa cego com operadores (Capítulo 5) |
| O pressuposto de uma equipe determina o resultado | O ganho desaparece com várias equipes | Port Halvard com duas equipes |
| Erro de discretização ou de implementação | Os resultados mudam com o passo de tempo ou a implementação | Verificação contra uma implementação independente baseada em eventos (Capítulo 4) |

### 3.8 Condições de falha e registro de riscos

**Condições de falha declaradas com antecedência** (cada uma corresponde a uma mudança na alegação):

| Condição | Consequência para a alegação |
|---|---|
| H2 falha nas duas regiões | Abandonar a contribuição de método; relatar que a temporização não acrescenta nada mensurável às listas de sinalização crítica; manter a análise de programação como contribuição teórica. |
| H2 falha numa região e se sustenta na outra | Estreitar para as condições que as distinguem; testar H3 para ver se o mecanismo explica a diferença. |
| Padrão de H3 ausente (ganho sem relação com a divergência das ordens) | Mecanismo sem apoio; qualquer ganho fica sem explicação e não deve ser generalizado. |
| H4b falha | Relatar uma troca; o método não é "gratuito" em relação à prática atual. |
| O ganho desmorona com erros plausíveis no mapa | Alegação condicionada à acurácia do mapa; acrescentar a auditoria do mapa como pré-requisito. |
| Os operadores rejeitam a ordenação no exercício de mesa | Alegação limitada a "um apoio à decisão cuja adoção não está comprovada"; estudar as barreiras à adoção. |

**Registro de riscos** (seleção): saída de um parceiro (mitigação: desenho com região sintética que não depende dos dados de um único parceiro); exposição de dados sensíveis (armazenamento em níveis, nenhum mapa real no texto público); erro do simulador (reimplementação independente e testes unitários); participantes do exercício de mesa identificáveis (relato agregado, nenhuma combinação de função com concessionária no texto público); pressão do financiador (acordo de publicação assinado antes do início do trabalho).

### 3.9 Exemplo resolvido: a proposta que quase omitiu a linha de base real

O primeiro rascunho do candidato comparava DEP apenas com SILO e relatava, numa rodada piloto, uma redução de quase 90% na perda ponderada de serviços críticos. A banca de orientação fez duas perguntas: *O que as concessionárias fazem de fato hoje?* e *O que uma ordenação perfeita alcançaria?* Entrevistas (sintéticas) com três despachantes revelaram que as três concessionárias mantêm uma lista de clientes críticos e restauram cedo esses alimentadores. O candidato acrescentou CRITFLAG e ORACLE. O piloto mostrou então DEP e CRITFLAG quase indistinguíveis em Riverbend, ambos longe de ORACLE. O veredito da banca: o número de 90% media o valor de *ter uma lista de clientes críticos*, o que não é novo; a pergunta em aberto é se a *temporização* agrega valor, e Riverbend sozinha — com apenas dois alimentadores críticos, ordenados do mesmo jeito pela maioria das regras — não pode respondê-la. A proposta foi revisada para declarar H2 e H3 com antecedência, para escolher uma segunda região segundo critérios de desenho declarados (mais alimentadores críticos, ordens divergentes de reservas e de clientes, duas equipes, contratos de combustível) *antes* de qualquer simulação nela, e para executar uma análise de muitas regiões em que a divergência entre as ordens varia sistematicamente.

Esta é a decisão de desenho mais importante do livro: **escolha a comparação que representa a melhor prática atual, e não a que faz o método parecer melhor.**

### 3.10 Erros comuns e limites

- Comparar com uma linha de base espantalho (nenhuma priorização, ou aleatória).
- Omitir o lado do custo de uma troca que a teoria de programação prevê.
- Definir "crítico" depois de ver quais instalações se beneficiam.
- Codificar as reservas como valores pontuais, sem incerteza.
- Tratar um grafo com semântica de OU como se modelasse redundância.
- Escrever um mecanismo que prediz apenas o sucesso.
- Definir o menor efeito de interesse por convenção estatística em vez de pela consequência prática.

- Escolher o segundo contexto depois de ver que tipo de região favorece o método, em vez de fixar os critérios de seleção com antecedência.
- Tratar uma regra do menor tempo até o impacto como ótima quando a teoria de programação mostra que o problema ponderado é difícil e que a regra ignora os pesos e o espalhamento.
- Registrar apenas a reserva de energia direta de cada instalação, de modo que caminhos indiretos, como a dependência do hospital em relação à água, passem despercebidos.
- Deixar que o parceiro que fornece os dados também escolha os limiares sem registrar quem os definiu e quando.

### Exercícios — capítulo 3

**EX015 — Tipificação da contribuição.** *Objetivo:* associar alegações a evidências. *Insumos:* quatro alegações de tese sintéticas: (a) "Lançamos o GridWater-Sim 2.0"; (b) "Nosso instrumento de levantamento da duração das reservas é confiável"; (c) "As concessionárias raramente usam a temporização das reservas ao ordenar a restauração"; (d) "A ordenação pelo tempo até o impacto reduz a perda de serviços críticos." *Restrições:* usar §3.1. *Passos:* (1) atribuir a cada alegação um tipo de contribuição; (2) declarar a evidência mínima que esse tipo exige; (3) declarar qual alegação depende de outra; (4) dizer qual alegação o Cascade Study não deve fazer apenas a partir de (a). *Evidência esperada:* tabela. *Rubrica:* 3 = tipos e evidências corretos, (d) dependente de (a) apenas como instrumento, (c) precisa de um estudo empírico amostrado; 2 = um erro; 1 = evidências genéricas; 0 = nada.

**EX016 — Verificação pela teoria de programação.** *Objetivo:* aplicar a regra de Smith. *Insumos:* clientes de Riverbend F1 9000, F2 1200, F3 2500, F4 6000; durações de restauração de 4, 3, 5 e 4 horas, respectivamente; uma equipe. *Restrições:* mostrar os cálculos. *Passos:* (1) calcular w/p para cada alimentador; (2) dar a ordem de Smith; (3) calcular os clientes-hora (milhares) para a ordem de Smith e para a ordem F2, F3, F1, F4; (4) declarar o aumento percentual. *Evidência esperada:* cálculos. *Rubrica:* 3 = ordem F1, F4, F3, F2 (razões 2250, 1500, 500, 400), totais de 135,7 e 227,6 mil clientes-hora, um aumento de 67,7%; 2 = deslize aritmético; 1 = regra errada; 0 = nada.

**EX017 — Extensão do tempo até o impacto.** *Objetivo:* estender o Laboratório 3. *Insumos:* Laboratório 3. *Restrições:* off-line. *Passos:* (1) acrescentar uma dependência de entrega de combustível: a reserva do gerador do hospital passa a 60 h se TEL estiver disponível para pedir combustível, modelada substituindo a reserva F2 → HOSP por 60 e acrescentando TEL → HOSP com reserva 30; (2) executar e registrar o instante de falha de HOSP; (3) explicar por que o resultado não mudou; (4) declarar o que o grafo com semântica de OU não consegue expressar sobre esse arranjo de combustível. *Evidência esperada:* código, saída, explicação. *Rubrica:* 3 = HOSP ainda em 13 h via água; explica que uma *extensão da reserva condicionada a outro serviço* é uma relação E/condicional que o grafo de OU não consegue expressar; 2 = saída correta, explicação parcial; 1 = saída errada; 0 = não executado.

**EX018 — Conjunto de hipóteses.** *Objetivo:* operacionalizar hipóteses. *Insumos:* o mecanismo de §3.4, aplicado a outro domínio de sua escolha (por exemplo, a restauração de sites de telecomunicações após um incidente cibernético numa operadora, com hospitais e despacho como dependentes). *Restrições:* uma hipótese de benefício, uma de contribuição sobre a melhor prática, uma de padrão do mecanismo e uma de não inferioridade; limiares justificados. *Passos:* (1) escrever cada hipótese com população, intervenção, comparador, desfecho e direção; (2) definir cada desfecho operacionalmente; (3) justificar cada limiar por uma consequência prática. *Evidência esperada:* bloco de hipóteses. *Rubrica:* 3 = completas e operacionais, comparador de melhor prática nomeado, limiares justificados por consequências e responsáveis; 2 = um elemento vago; 1 = limiares arbitrários; 0 = nada.

**EX019 — Tabela de explicações rivais.** *Objetivo:* desenhar contra as alternativas. *Insumos:* suas hipóteses do EX018. *Restrições:* pelo menos seis rivais. *Passos:* (1) listar pelo menos seis explicações rivais para um resultado positivo; (2) para cada uma, declarar a previsão que a apoiaria; (3) nomear a característica do desenho que a testa. *Evidência esperada:* tabela. *Rubrica:* 3 = seis ou mais rivais plausíveis, incluindo a adequação da linha de base, os pesos, a circularidade e a adoção, cada uma com uma característica de desenho concreta; 2 = quatro ou cinco; 1 = genéricas; 0 = nada.

**EX020 — Condições de falha e critérios do segundo contexto.** *Objetivo:* tornar a contribuição falseável e evitar a escolha seletiva do contexto de validação. *Insumos:* sua proposta. *Restrições:* pelo menos cinco condições de falha com consequências; critérios de seleção de um segundo contexto escritos *antes* de ele ser modelado. *Passos:* (1) escrever condições de falha associadas a mudanças na alegação; (2) escrever de três a cinco critérios de seleção do contexto derivados do mecanismo; (3) explicar como um revisor poderia verificar que os critérios foram fixados com antecedência. *Evidência esperada:* duas listas e um parágrafo. *Rubrica:* 3 = cada condição muda uma alegação específica, critérios derivados do mecanismo (divergência das ordens, número de equipes, faixa das reservas), pré-registro com carimbo de tempo nomeado; 2 = critérios não derivados do mecanismo; 1 = vagos; 0 = nada.

### Síntese do capítulo

Uma contribuição de doutorado precisa dizer de que tipo ela é e precisa superar a melhor prática atual, e não um espantalho. A ordenação da restauração é um problema de programação: a regra de Smith torna "mais clientes primeiro" ótima para clientes-hora, enquanto os serviços críticos limitados por reservas criam um objetivo de atraso ponderado para o qual as regras simples são heurísticas. Essa teoria prevê a troca, fornece um limite oráculo e expõe a fraqueza da regra proposta. Os grafos de dependência com reservas revelam caminhos indiretos que dominam a temporização, mas sua semântica de OU, suas reservas fixas e as dependências humanas e na direção da recuperação que lhes faltam precisam ser nomeadas. O mecanismo prediz um padrão — benefício apenas onde a temporização e o número de clientes discordam, nenhum quando as reservas são longas, um custo em clientes-hora e fragilidade diante de erros no mapa —, e as hipóteses, as linhas de base, as rivais e as condições de falha são escritas de modo que cada parte desse padrão possa ser mostrada falsa.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 08

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Replicação das linhas de base e piloto

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Distinguir reprodução, replicação e verificações de robustez, e escolher qual delas uma linha de base exige.
2. Reproduzir um cálculo de modelo publicado, declarar uma tolerância com antecedência, diagnosticar uma discrepância e escrever um registro de reprodução.
3. Verificar um simulador com invariantes, testes unitários e uma implementação independente antes de confiar em qualquer comparação que ele produza.
4. Reconhecer artefatos do protocolo de avaliação — ajuste por pontos, vazamento temporal, características específicas do testbed — que inflam as linhas de base de detecção.
5. Obter parâmetros do modelo junto a especialistas e documentá-los com incerteza explícita.
6. Desenhar um piloto delimitado cujo propósito seja a viabilidade, com critérios de prosseguir/não prosseguir, e explicar por que um piloto não deve ser usado para estimar o tamanho do efeito.

O Capítulo 3 fixou as hipóteses, as linhas de base e as condições de falha. Antes que o estudo principal possa comparar DEP com SILO, CRITFLAG e ORACLE, é preciso mostrar que cada número de que essas comparações dependem significa o que alega.

### 4.1 Reprodução, replicação, robustez

As [National Academies (2019)](https://doi.org/10.17226/25303) distinguem a **reprodutibilidade** — obter resultados consistentes usando os mesmos dados de entrada, passos computacionais, métodos e condições de análise — da **replicabilidade** — obter resultados consistentes entre estudos voltados à mesma pergunta, cada um com seus próprios dados. Uma terceira atividade, muitas vezes chamada de verificação de **robustez**, varia as escolhas analíticas sobre os mesmos dados. As teses sobre infraestrutura precisam das três:

| Atividade | Exemplo do Cascade Study | Contra o que protege |
|---|---|---|
| Reprodução | Reexecutar um cálculo de inoperabilidade publicado com a matriz publicada | Leitura errada das convenções; erros de codificação na linha de base |
| Replicação | Construir Port Halvard de forma independente e testar se o resultado de Riverbend se sustenta | Constatações específicas do contexto ou do modelo |
| Robustez | Variar pesos, reservas, passo de tempo, horizonte | Resultados que dependem de uma escolha arbitrária |

### 4.2 Reproduzindo um cálculo de modelo: o modelo insumo-produto de inoperabilidade

#### 4.2.1 O modelo

O modelo insumo-produto de inoperabilidade de Haimes e Jiang ([2001](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1))) adapta a economia de insumo-produto de Leontief à infraestrutura. Cada setor *i* tem uma inoperabilidade *q_i* entre 0 (plenamente operável) e 1 (plenamente inoperável). O equilíbrio após uma perturbação inicial *c\** é *q* = *A\*q* + *c\**, portanto *q* = (*I* − *A\**)⁻¹ *c\**. O elemento *A\*_ij* é a inoperabilidade transmitida ao setor *i* por unidade de inoperabilidade do setor *j*. A convenção importa: a linha é o setor *receptor*, a coluna o setor *fornecedor*. Artigos e softwares diferem na notação, e alguns derivam *A\** das tabelas econômicas de insumo-produto por passos de normalização que são fáceis de errar sutilmente.

#### 4.2.2 Laboratório de reprodução

Um artigo "publicado" sintético relata que, após uma perturbação que torna a energia 50% inoperável, a água atinge uma inoperabilidade de equilíbrio de 0,236 num modelo de três setores. Declare com antecedência uma tolerância de ± 0,005 (arredondamento na publicação) e então reproduza:

```python
# Lab 4a - reproducing an inoperability input-output (IIM) result (offline, standard library only)
# q = (I - A*)^-1 c*. Convention: A*[i][j] = inoperability contributed to sector i per unit inoperability of sector j.
def solve(a, c):
    n = len(c)
    m = [[(1.0 if i == j else 0.0) - a[i][j] for j in range(n)] + [c[i]] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        for r in range(n):
            if r != col:
                f = m[r][col] / m[col][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[col])]
    return [m[i][n] / m[i][i] for i in range(n)]
sectors = ["power", "water", "telecom"]
A = [[0.00, 0.05, 0.10],   # power depends a little on water (cooling) and telecom (SCADA comms)
     [0.40, 0.00, 0.15],   # water depends strongly on power
     [0.30, 0.02, 0.00]]   # telecom depends on power
c = [0.50, 0.00, 0.00]    # initial perturbation: power 50% inoperable
q = solve(A, c)
print("convention A* (row = receiving sector):", [round(x, 3) for x in q])
At = [list(r) for r in zip(*A)]
qt = solve(At, c)
print("transposed by mistake:               ", [round(x, 3) for x in qt])
```

Saída esperada:

```text
convention A* (row = receiving sector): [0.528, 0.236, 0.163]
transposed by mistake:                [0.528, 0.028, 0.057]
```

Com a convenção correta, a reprodução confere (água 0,236). Com a matriz transposta — um erro que não produz aviso, nem falha, e gera um vetor de aparência plausível —, a inoperabilidade da água cai quase uma ordem de grandeza, e a *classificação* dos setores muda: as telecomunicações agora parecem mais afetadas do que a água. O próprio valor da energia coincide nos dois casos, e é exatamente isso que torna o erro perigoso: um replicador que verifique apenas o setor perturbado declararia sucesso.

#### 4.2.3 O registro de reprodução

Um registro de reprodução anota: o valor-alvo e sua fonte (página, tabela); a tolerância, fixada *antes* da execução; o ambiente de software (versão da linguagem, sistema operacional); os insumos e sua procedência; a saída exata; as discrepâncias e seu diagnóstico; e a decisão (reproduzido, reproduzido após correção, não reproduzido). Quando a convenção dos autores originais for ambígua, escreva para eles; registre a correspondência. Uma não reprodução é um resultado, e não um constrangimento, e pertence à tese.

#### 4.2.4 O que um IIM reproduzido pode e não pode sustentar

Reproduzir o cálculo mostra apenas que a aritmética foi compreendida. O IIM continua linear e baseado em equilíbrio: ele não modela reservas, temporização nem ordem de restauração, e seus coeficientes costumam ser derivados de fluxos econômicos, e não de dependências de engenharia. No Cascade Study, ele serve como **verificação cruzada em nível setorial** — os setores que o IIM classifica como mais afetados correspondem aos serviços que o modelo de reservas mostra falhando? —, e não como concorrente do modelo de restauração.

### 4.3 A discrepância do GridWater-Sim (sintética)

O benchmark sintético GridWater-Sim relata, para uma configuração semelhante a Riverbend, uma perda ponderada média de serviços críticos sob a restauração pelos clientes que a reimplementação do candidato não conseguiu reproduzir dentro da tolerância declarada com antecedência. O diagnóstico seguiu a ordem que mais frequentemente encontra a causa:

1. **Insumos.** Foram usadas as mesmas distribuições de parâmetros? A documentação do benchmark dava as distribuições triangulares como (low, mode, high); o `random.triangular` do Python recebe (low, high, mode). Trocar mode e high desloca a média silenciosamente.
2. **Semântica.** "Restaurado" significa reenergizado ou serviço retomado? O GridWater-Sim aplicava um atraso de reinício de uma hora apenas à água; a reimplementação o aplicava a todos os serviços.
3. **Numérica.** O benchmark avançava o tempo em passos fixos; a reimplementação calculava os intervalos exatos de interrupção. Passos fixos introduzem um erro de discretização que depende do passo e de onde os esgotamentos das reservas caem dentro de um passo.
4. **Aleatoriedade.** As sementes e a ordem dos sorteios eram idênticas? A ordem dos sorteios importa: sortear as durações antes das reservas numa implementação e depois na outra produz conjuntos de cenários diferentes a partir da mesma semente.

Depois de alinhar (1) e (2), a diferença restante ficou dentro da tolerância e diminuiu com passos de tempo menores, confirmando (3). A tese registra o benchmark como *reproduzido após a correção de uma ambiguidade na ordem dos parâmetros*, relata os valores original e corrigido e adota a implementação por intervalos exatos, mantendo a versão por passos de tempo como verificação independente.

### 4.4 Verificando um simulador

A verificação pergunta se o modelo está implementado corretamente; a validação pergunta se ele representa o sistema real de forma adequada ao seu propósito ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)). A verificação vem primeiro, porque validar uma implementação defeituosa não tem sentido.

**Invariantes** que qualquer simulador de restauração correto precisa satisfazer:

- Se toda reserva exceder o horizonte, a perda ponderada de serviços críticos é zero sob qualquer ordenação.
- Duas políticas que produzem a mesma ordem produzem resultados idênticos com sorteios idênticos.
- A perda do oráculo é menor ou igual à perda de qualquer política em qualquer sorteio.
- Aumentar uma reserva, mantendo todo o resto fixo, nunca aumenta a perda.
- Os clientes-hora sob a regra de Smith são menores ou iguais aos de qualquer outra ordenação quando as durações de restauração são iguais.
- A perda e os clientes-hora são não negativos e limitados por peso × horizonte e clientes × horizonte.

Os **testes unitários** verificam os menores componentes: a aritmética de intervalos para um único serviço; o efeito de uma dependência com uma reserva local; a atribuição de equipes com duas equipes. Os **testes entre implementações** comparam duas implementações escritas de forma independente sobre sorteios fixos. Os **testes de condições extremas** usam reservas zero, durações zero e um único alimentador. Mantenha os testes no arquivo (Capítulo 7); um revisor que pode executá-los confia mais nas comparações do que um que precisa aceitá-las por fé.

### 4.5 Replicando uma linha de base de detecção: artefatos da avaliação

Embora o Cascade Study não proponha um detector, sua análise do tempo até o impacto depende de quando uma perturbação é reconhecida, e o candidato precisa ser capaz de julgar as linhas de base de detecção relatadas para infraestrutura. Os mecanismos comuns de inflação são escolhas da avaliação, e não propriedades do modelo.

#### 4.5.1 Ajuste por pontos

[Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) mostraram que o ajuste por pontos (point adjustment, PA) — contar um segmento anômalo inteiro como detectado quando qualquer ponto nele é sinalizado — pode fazer pontuações aleatórias parecerem excelentes. O laboratório a seguir reproduz o efeito em rótulos sintéticos:

```python
# Lab 4b - how point adjustment (PA) inflates detection scores (offline, standard library only)
import random
random.seed(42)
N = 2000
labels = [0] * N
for start, length in [(300, 60), (900, 120), (1500, 80)]:
    for t in range(start, start + length):
        labels[t] = 1
scores = [random.random() for _ in range(N)]          # a detector that knows nothing
thr = sorted(scores)[int(0.97 * N)]                    # alarm on the top 3% of scores
pred = [1 if s > thr else 0 for s in scores]
def f1(p, y):
    tp = sum(1 for a, b in zip(p, y) if a and b)
    fp = sum(1 for a, b in zip(p, y) if a and not b)
    fn = sum(1 for a, b in zip(p, y) if b and not a)
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    return round(2 * prec * rec / (prec + rec), 3) if prec + rec else 0.0
def segments(y):
    segs, t = [], 0
    while t < len(y):
        if y[t]:
            s = t
            while t < len(y) and y[t]:
                t += 1
            segs.append((s, t))
        else:
            t += 1
    return segs
def adjust(p, y, k=0.0):
    q = list(p)
    for s, e in segments(y):
        hit = sum(p[s:e]) / (e - s)
        if hit > k:
            for t in range(s, e):
                q[t] = 1
    return q
print("point-wise F1           :", f1(pred, labels))
print("F1 after PA             :", f1(adjust(pred, labels), labels))
print("F1 after PA%K (K = 0.20):", f1(adjust(pred, labels, 0.20), labels))
print("segments hit by >=1 alarm:", sum(1 for s, e in segments(labels) if any(pred[s:e])), "of", len(segments(labels)))
```

Saída esperada:

```text
point-wise F1           : 0.05
F1 after PA             : 0.911
F1 after PA%K (K = 0.20): 0.05
segments hit by >=1 alarm: 3 of 3
```

Um detector sem nenhuma informação alcança 0,911 após o PA porque cada segmento longo contém, por acaso, pelo menos um dos 3% de alarmes aleatórios. O PA%K com K = 20% elimina a inflação aqui. Para a pesquisa em IC, a lição vai além: nenhuma das métricas diz *quando* o primeiro alarme verdadeiro ocorreu em relação ao início do segmento, que é o que importa para as reservas. Uma métrica relevante para a consequência é a **latência de detecção relativa ao tempo até o impacto** — a fração de incidentes detectados antes que a reserva do primeiro serviço dependente se esgote.

#### 4.5.2 Outros artefatos

- **Vazamento temporal.** Divisões aleatórias de séries temporais em treino/teste permitem que um modelo aprenda com o futuro. Use divisões ordenadas no tempo que imitem a implantação.
- **Características específicas do testbed.** Um detector pode aprender assinaturas das ferramentas de injeção de ataques do testbed ou de seus sensores específicos, em vez dos ataques.
- **Cobertura do conjunto de ataques.** Os ataques de um conjunto de dados foram escolhidos por quem o construiu; o desempenho neles diz pouco sobre outras classes de ataques ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)).
- **Taxas de base.** Uma taxa de falsos positivos que parece pequena num conjunto de dados balanceado pode sobrecarregar os operadores em taxas de base realistas ([Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 4.6 Obtendo os parâmetros

As reservas, as durações de restauração e os pesos do modelo vêm de pessoas. A elicitação estruturada com especialistas — preparar os especialistas, pedir quantis em vez de valores únicos, devolver as distribuições implícitas e registrar as justificativas — reduz a ancoragem e o excesso de confiança ([O'Hagan et al., 2006](https://doi.org/10.1002/0470033312)). Para o Cascade Study (sintético):

| Parâmetro | Obtido junto a | Forma | Documentação |
|---|---|---|---|
| Duração da restauração de um alimentador | Três despachantes da REC | Mínimo, mais provável e máximo para manobras manuais sem SCADA | Justificativa por valor; divergências registradas |
| Reserva das telecomunicações | Engenheiro de instalações da operadora | Autonomia das baterias sob a carga medida, horas de combustível do gerador | Pressuposto de carga declarado |
| Reserva da água | Gerente de operações da RWA | Autonomia do gerador mais o rebaixamento do armazenamento até a pressão mínima | Pressuposto de demanda (estação) declarado |
| Reserva do hospital | Diretor de instalações | Combustível disponível na carga típica; horas de água no local | Exigências normativas e estoque real distinguidos |
| Pesos | Painel de gestão de emergências | Comparações pareadas convertidas em pesos | Obtidos antes de qualquer simulação; assinados e datados |

As distribuições triangulares são uma escolha pragmática para elicitações de três pontos; elas não são derivadas da física. O Capítulo 6 testa se as conclusões dependem da família de distribuições.

### 4.7 O piloto

#### 4.7.1 Para que serve um piloto

Um piloto testa a **viabilidade**: se os procedimentos, os materiais, a temporização, os fluxos de dados e os instrumentos funcionam. Ele não é um pequeno estudo principal. Os tamanhos de efeito estimados a partir de pilotos são imprecisos demais para planejar tamanhos de amostra ou sustentar alegações ([Leon, Davis and Kraemer, 2011](https://doi.org/10.1016/j.jpsychires.2010.10.008)). O piloto do Cascade Study teve duas vertentes:

1. **Piloto de simulação.** Executar as quatro políticas em 50 sorteios para verificar se o código, o registro e as invariantes funcionam, se o tempo de execução permite o número planejado de sorteios e se a censura em 72 horas é rara. Os *resultados* do piloto (diferenças entre as políticas) são registrados como exploratórios e não são interpretados.
2. **Piloto do exercício de mesa.** Três operadores (participantes sintéticos P01–P03, não elegíveis para o estudo principal) percorreram um cenário de 40 minutos com e sem uma exibição do tempo até o impacto. Perguntas: Eles entendem a exibição? O cenário revela o desfecho cedo demais? Quanto tempo leva cada decisão? O processo de consentimento e de devolutiva funciona?

#### 4.7.2 Critérios de prosseguir/não prosseguir (declarados com antecedência)

| Critério | Limiar | Resultado do piloto (sintético) | Decisão |
|---|---|---|---|
| Os testes de invariantes passam | Todos | Todos | Prosseguir |
| Censura em 72 h | < 1% dos serviço-sorteios | 0% | Prosseguir |
| Tempo de execução para 500 sorteios, incluindo o oráculo | < 1 hora | Minutos | Prosseguir |
| Os participantes leem a exibição corretamente | ≥ 2 de 3 | 3 de 3 após uma mudança de redação | Prosseguir com revisão |
| O cenário revela o desfecho prematuramente | Não | Sim — um inject mencionava "desvio do hospital" | Revisar o inject; repilotar um participante |
| Duração da sessão | ≤ 60 min | 55 min | Prosseguir |

Toda revisão é registrada no registro de desvios com a data e a confirmação de que não existiam dados do estudo principal.

### 4.8 Exemplo resolvido: o piloto que mudou o cenário

No piloto do exercício de mesa, P02 perguntou por que a reserva do gerador do hospital aparecia como 26 horas quando "todo mundo sabe que a água acaba primeiro". O candidato tinha exibido apenas as reservas diretas de energia. A exibição foi revisada para mostrar o **tempo efetivo até o impacto** (o mínimo sobre todos os caminhos, como no Laboratório 3) ao lado das reservas diretas, com o caminho mostrado. Isso mudou o instrumento — um resultado legítimo de piloto — e levantou uma questão metodológica para o estudo principal: a comparação entre "com exibição" e "sem exibição" passou a testar a exibição do tempo efetivo até o impacto, e não apenas qualquer informação de criticidade. As hipóteses do exercício de mesa foram refinadas de acordo, *antes* do estudo principal, e a mudança foi pré-registrada como uma emenda.

### 4.9 Erros comuns e limites

- Declarar uma reprodução bem-sucedida depois de verificar uma única saída.
- Definir as tolerâncias depois de ver a discrepância.
- Tratar o código do benchmark como a especificação quando ele discorda de seu artigo, ou vice-versa, sem registrar qual foi seguido.
- Validar um simulador antes de verificá-lo.
- Relatar o F1 com ajuste por pontos para detecção em infraestrutura sem a latência relativa à consequência.
- Pedir números únicos aos especialistas e tratá-los como certos.
- Usar os tamanhos de efeito do piloto para planejar ou para alegar.

- Verificar apenas o setor perturbado numa reprodução, como com a energia na matriz de inoperabilidade transposta, que coincide sob as duas convenções.
- Presumir que a ordem dos parâmetros de uma biblioteca corresponde à notação do artigo, como com a distribuição triangular no caso do GridWater-Sim.
- Interpretar as diferenças entre as políticas num piloto, quando o propósito do piloto é a viabilidade e seus resultados são registrados como exploratórios.
- Mudar um instrumento do exercício de mesa após o piloto sem registrar a mudança no registro de desvios.

### Exercícios — capítulo 4

**EX021 — Registro de reprodução.** *Objetivo:* documentar uma tentativa de reprodução. *Insumos:* Laboratório 4a. *Restrições:* executar off-line; tolerância de ± 0,005 fixada antes da execução. *Passos:* (1) registrar o alvo (água 0,236); (2) executar primeiro a matriz transposta e registrar a discrepância; (3) diagnosticar usando a convenção da matriz; (4) executar a convenção correta; (5) escrever a entrada do registro com os detalhes do ambiente. *Evidência esperada:* registro de reprodução. *Rubrica:* 3 = saídas exatas, diagnóstico da convenção, ambiente registrado, observa que a energia coincide nas duas execuções; 2 = falta um elemento; 1 = sem diagnóstico; 0 = não executado.

**EX022 — Análise de perturbações no IIM.** *Objetivo:* usar um modelo reproduzido para uma alegação delimitada. *Insumos:* Laboratório 4a com a convenção correta. *Restrições:* off-line. *Passos:* (1) calcular *q* para as perturbações energia 0,5 e telecomunicações 0,5 separadamente; (2) calcular *q* para as duas juntas; (3) verificar se o resultado conjunto é igual à soma dos resultados separados e explicar por quê; (4) declarar uma alegação que o modelo sustenta e uma que ele não pode sustentar. *Evidência esperada:* três vetores e um parágrafo. *Rubrica:* 3 = vetores corretos, linearidade (superposição) explicada, alegação limitada à inoperabilidade de equilíbrio sem temporização; 2 = vetores corretos, explicação rala; 1 = erros; 0 = nada.

**EX023 — A armadilha da ordem dos parâmetros.** *Objetivo:* detectar um erro silencioso de entrada. *Insumos:* uma distribuição documentada como (low = 4, mode = 8, high = 12). *Restrições:* usar o `random.triangular(low, high, mode)` do Python. *Passos:* (1) calcular a média teórica, (low + mode + high) / 3, para a chamada correta `triangular(4, 12, 8)`; (2) estimar a média da chamada errada `triangular(4, 8, 12)` a partir de 100.000 sorteios com semente e registrar o mínimo e o máximo; explicar o que a chamada errada realmente amostra; declarar qual teste a teria detectado. *Evidência esperada:* duas médias e uma explicação. *Rubrica:* 3 = média correta 8,0; a chamada errada trata 8 como *high* e 12 como *mode*, então a fórmula do CPython retorna 4 + 4·√(2u) para *u* uniforme — valores em [4, ≈ 9,66] com média ≈ 7,77, que nem sequer é uma distribuição triangular; uma verificação da média sozinha é fraca, enquanto verificar se o máximo amostral se aproxima de 12 e traçar um histograma detecta o erro; 2 = erro identificado, teste fraco; 1 = erro não percebido; 0 = nada.

**EX024 — Testes de invariantes.** *Objetivo:* escrever testes de verificação. *Insumos:* as invariantes de §4.4 e o simulador que você vai conhecer no Capítulo 5 (Laboratório 5), ou o seu próprio. *Restrições:* pelo menos quatro invariantes como asserções executáveis. *Passos:* (1) escolher pelo menos quatro invariantes de §4.4; (2) escrever cada uma como uma asserção executável; (3) executar as asserções sobre sorteios fixos; (4) introduzir deliberadamente um defeito, como remover o atraso de reinício de um serviço, e mostrar qual teste falha. *Evidência esperada:* código dos testes e saída antes e depois do defeito. *Rubrica:* 3 = quatro ou mais invariantes significativas, o defeito detectado, explicação do porquê; 2 = os testes rodam, mas o defeito não é detectado; 1 = testes triviais; 0 = nada.

**EX025 — Métrica de detecção relativa à latência.** *Objetivo:* definir uma métrica de detecção relevante para a consequência. *Insumos:* Laboratório 4b e os valores de tempo até o impacto do Laboratório 3 (o primeiro impacto crítico em 2 h para o SCADA da água, 8 h para as telecomunicações). *Restrições:* definir a métrica formalmente. *Passos:* (1) definir "detectado antes do impacto" para um segmento com início conhecido e tempo até o impacto conhecido; (2) calculá-lo para o detector aleatório, tratando cada passo de tempo como 6 minutos e tomando o tempo até o impacto como 2 h para todo segmento; (3) comparar com os valores de F1. *Evidência esperada:* definição, fração calculada, parágrafo. *Rubrica:* 3 = definição sólida e cálculo correto a partir do índice do primeiro alarme em cada segmento, com o contraste com o PA explicado; 2 = definição boa, erro de cálculo; 1 = vaga; 0 = nada.

**EX026 — Plano do piloto.** *Objetivo:* desenhar um piloto de viabilidade. *Insumos:* seu próprio estudo dos exercícios anteriores. *Restrições:* pelo menos seis critérios de prosseguir/não prosseguir com limiares; declaração explícita do que não será estimado. *Passos:* (1) listar as perguntas de viabilidade do piloto; (2) definir limiares declarados com antecedência; (3) definir o que acontece em caso de "não prosseguir" para cada um; (4) definir quem pode participar e por que os participantes do piloto são excluídos do estudo principal. *Evidência esperada:* plano do piloto. *Rubrica:* 3 = critérios mensuráveis, apenas de viabilidade, exclusão justificada, processo de revisão registrado; 2 = um critério vago; 1 = piloto usado para estimar o efeito; 0 = nada.

### Síntese do capítulo

Antes de comparar métodos, garanta que os números significam o que alegam. Reproduza as linhas de base com uma tolerância fixada com antecedência, verifique mais de uma saída e registre as convenções — uma matriz transposta produziu uma resposta plausível e errada que coincidia justamente no valor que um replicador apressado verificaria. Diagnostique as discrepâncias pelos insumos, pela semântica, pela numérica e pela aleatoriedade. Verifique os simuladores com invariantes, testes unitários e uma implementação independente antes de validá-los. Trate com desconfiança as linhas de base de detecção que dependem do ajuste por pontos, de divisões aleatórias ou de um único testbed, e prefira, para a infraestrutura, a latência relativa ao tempo até o impacto. Obtenha os parâmetros com incerteza e procedência. Use o piloto para ajustar os procedimentos e os instrumentos, nunca para estimar efeitos.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 08

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Estudo principal e validação independente

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Desenhar um experimento de simulação pareado com números aleatórios comuns, um número justificado de sorteios e um limite oráculo.
2. Distinguir a incerteza de Monte Carlo da incerteza de parâmetros e da incerteza estrutural, e dizer qual delas um intervalo relatado descreve.
3. Interpretar um padrão misto de hipóteses sustentadas e não sustentadas sem resgatar as favoráveis.
4. Desenhar e analisar um estudo de exercício de mesa cego com operadores cujo desfecho seja a *consequência* das escolhas feitas, e não a preferência declarada.
5. Validar um modelo usando evidências de validade aparente, histórica, de condições extremas e operacional, e declarar o que cada uma estabelece.
6. Executar uma validação independente num segundo contexto selecionado segundo critérios declarados com antecedência e raciocinar sobre a transportabilidade.

O Capítulo 4 verificou o simulador, reproduziu as linhas de base e pilotou os procedimentos. Este capítulo executa o estudo confirmatório exatamente como pré-registrado e então testa se seu resultado se transporta.

### 5.1 Desenhando o experimento de simulação

#### 5.1.1 Comparações pareadas e números aleatórios comuns

Cada sorteio da simulação amostra um cenário: as durações de restauração de todos os alimentadores e as reservas de todos os serviços. Toda política é avaliada sobre *o mesmo* sorteio. Esse desenho de **números aleatórios comuns** remove da comparação a variância compartilhada entre cenários: a quantidade de interesse é a diferença por sorteio entre duas políticas, cuja variância é Var(A) + Var(B) − 2 Cov(A, B). O pareamento ajuda exatamente na medida em que as perdas das duas políticas são positivamente correlacionadas entre os sorteios. Quando duas políticas se compensam — uma protege a água num sorteio em que a outra protege as telecomunicações —, a correlação é fraca e o pareamento ajuda pouco; o EX028 mostra isso acontecendo em Riverbend. Analise as diferenças pareadas mesmo assim, porque elas são o estimando correto, mas não presuma que o pareamento garanta precisão.

#### 5.1.2 Quantos sorteios?

O erro-padrão de Monte Carlo de uma diferença de médias é *s_d* / √*n*, em que *s_d* é o desvio-padrão das diferenças por sorteio. No piloto (Capítulo 4), o desvio-padrão das diferenças DEP − CRITFLAG em Riverbend foi de cerca de 7 horas de serviço ponderadas, então 500 sorteios dão uma semiamplitude de 95% de cerca de 1,96 × 7 / √500 ≈ 0,6. O menor efeito de interesse para H2 é 10% da perda de CRITFLAG; como a perda de CRITFLAG em Riverbend é pequena (cerca de 4), esse limiar é de cerca de 0,4 — menor que a semiamplitude. O pré-registro fixou, portanto, uma **regra de decisão** de três vias: H2 é *sustentada* se o intervalo ficar inteiramente abaixo de −10% da perda média de CRITFLAG, *rejeitada* se ficar inteiramente acima desse limiar (uma redução de pelo menos 10% fica descartada), e *inconclusiva* nos demais casos, quando o remédio planejado eram 2.000 sorteios adicionais sem o oráculo. Registre o cálculo e a regra; não aumente *n* depois de ver um resultado "quase significativo" fora da regra que você escreveu.

#### 5.1.3 O que significa um intervalo de Monte Carlo

Um intervalo bootstrap ou normal sobre os sorteios da simulação descreve a **incerteza de Monte Carlo** — quanto a estimativa se moveria com mais sorteios *deste modelo, com estas distribuições de parâmetros*. Ele nada diz sobre a **incerteza de parâmetros** (se as distribuições obtidas estão certas) nem sobre a **incerteza estrutural** (se a forma do modelo está certa). Com sorteios suficientes, qualquer diferença se torna "estatisticamente significativa" dentro de um modelo. Relate os intervalos de Monte Carlo por completude, mas baseie as alegações nos tamanhos de efeito em relação ao menor efeito de interesse, e trate a incerteza de parâmetros e a estrutural com análises de sensibilidade e validação (§5.4 e Capítulo 6).

### 5.2 O estudo de simulação confirmatório

#### 5.2.1 O simulador

O simulador baseado em eventos abaixo implementa o desenho pré-registrado. Um serviço fica indisponível enquanto seu alimentador está desenergizado além de sua reserva, ou enquanto um serviço do qual ele depende está indisponível além de sua reserva local; um atraso de reinício de uma hora segue a restauração. As equipes pegam o próximo alimentador na ordem da política assim que ficam livres. Os clientes-hora são calculados por alimentador. ORACLE enumera todas as ordenações para cada sorteio. Salve o código como `lab5_mc.py`; o Capítulo 6 o importa.

```python
# Lab 5 - paired Monte Carlo comparison of restoration orderings (offline, standard library only)
# Event-based: a service is unavailable while its feeder is down beyond its buffer, or while a
# service it depends on is unavailable beyond its on-site buffer; restart lag applies after restoration.
import itertools, random, statistics

RIVERBEND = {
    "customers": {"F1": 9000, "F2": 1200, "F3": 2500, "F4": 6000},
    "crews": 1, "dur": (2, 6, 4),          # triangular(low, high, mode) hours per feeder
    "services": {  # name: (feeder, buffer triangular, weight, (depends_on, on-site hours) or None)
        "WATER": ("F3", (4, 14, 8), 4.0, None),
        "TEL":   ("F2", (4, 12, 8), 3.0, None),
        "HOSP":  ("F2", (8, 48, 24), 5.0, ("WATER", 4.0)),
    },
}
PORT_HALVARD = {
    "customers": {"H1": 7000, "H2": 3000, "H3": 1500, "H4": 4000, "H5": 800, "H6": 5000},
    "crews": 2, "dur": (1.5, 5, 3),
    "services": {
        "WATER2":   ("H4", (10, 30, 20), 4.0, None),
        "HOSP2":    ("H2", (48, 96, 72), 5.0, ("WATER2", 6.0)),
        "TEL2":     ("H3", (2, 6, 4), 3.0, None),
        "DISPATCH": ("H5", (1, 3, 2), 4.0, None),
    },
}
H, LAG = 72.0, 1.0

def draw(region, rng, buffer_scale=1.0):
    dur = {f: rng.triangular(*region["dur"]) for f in sorted(region["customers"])}
    buf = {s: rng.triangular(*v[1]) * buffer_scale for s, v in sorted(region["services"].items())}
    return dur, buf

def restore_times(order, dur, crews):
    free, done = [0.0] * crews, {}
    for f in order:
        i = min(range(crews), key=lambda k: free[k])
        free[i] += dur[f]
        done[f] = free[i]
    return done

def outage(region, done, buf):
    """Return {service: (start, end)} of unavailability, clipped to [0, H]."""
    out = {}
    def solve(s):
        if s in out:
            return out[s]
        feeder, _, _, dep = region["services"][s]
        ivs = []
        if buf[s] < done[feeder]:
            ivs.append((buf[s], done[feeder] + LAG))
        if dep:
            d = solve(dep[0])
            if d and d[0] + dep[1] < d[1]:
                ivs.append((d[0] + dep[1], d[1]))
        out[s] = (min(a for a, _ in ivs), max(b for _, b in ivs)) if ivs else None
        return out[s]
    for s in region["services"]:
        solve(s)
    return {s: (max(0.0, iv[0]), min(H, iv[1])) for s, iv in out.items() if iv}

def evaluate(region, order, dur, buf):
    done = restore_times(order, dur, region["crews"])
    loss = sum(region["services"][s][2] * (e - b) for s, (b, e) in outage(region, done, buf).items() if e > b)
    cust_h = sum(c * min(H, done[f]) for f, c in region["customers"].items()) / 1000.0
    return loss, cust_h

def silo(region):
    return sorted(region["customers"], key=lambda f: -region["customers"][f])

def critflag(region, believed_feeder=None):
    feeder_of = {s: v[0] for s, v in region["services"].items()}
    feeder_of.update(believed_feeder or {})   # the critical-customer list may also be out of date
    crit = set(feeder_of.values())
    return sorted(region["customers"], key=lambda f: (f not in crit, -region["customers"][f]))

def dep(region, believed_feeder=None):
    svc = dict(region["services"])
    if believed_feeder:                       # planner's (possibly wrong) dependency map
        for s, f in believed_feeder.items():
            svc[s] = (f,) + svc[s][1:]
    mean = {s: sum(v[1]) / 3 for s, v in svc.items()}
    tti = {}
    def t(s):
        if s not in tti:
            dep_ = svc[s][3]
            tti[s] = min(mean[s], t(dep_[0]) + dep_[1]) if dep_ else mean[s]
        return tti[s]
    key = {f: min([t(s) for s, v in svc.items() if v[0] == f], default=float("inf")) for f in region["customers"]}
    return sorted(region["customers"], key=lambda f: (key[f], -region["customers"][f]))

def experiment(region, n=500, seed=7, buffer_scale=1.0, believed_feeder=None, oracle=True):
    rng = random.Random(seed)
    policies = {"SILO": silo(region), "CRITFLAG": critflag(region, believed_feeder), "DEP": dep(region, believed_feeder)}
    res = {k: [] for k in list(policies) + (["ORACLE"] if oracle else [])}
    cust = {k: [] for k in policies}
    perms = list(itertools.permutations(region["customers"]))
    for _ in range(n):
        dur, buf = draw(region, rng, buffer_scale)
        for k, order in policies.items():
            l, c = evaluate(region, order, dur, buf)
            res[k].append(l)
            cust[k].append(c)
        if oracle:
            res["ORACLE"].append(min(evaluate(region, list(p), dur, buf)[0] for p in perms))
    return policies, res, cust

def boot_ci(x, seed=11, b=1000):
    rng = random.Random(seed)
    means = sorted(statistics.fmean(rng.choices(x, k=len(x))) for _ in range(b))
    return round(means[int(0.025 * b)], 2), round(means[int(0.975 * b)], 2)

if __name__ == "__main__":
    for name, region in (("Riverbend", RIVERBEND), ("Port Halvard", PORT_HALVARD)):
        policies, res, cust = experiment(region)
        print(f"== {name}: orders {policies}")
        for k, v in res.items():
            extra = f"  customer-hours(k) {statistics.fmean(cust[k]):7.1f}" if k in cust else ""
            print(f"  {k:8} weighted critical loss {statistics.fmean(v):6.2f}{extra}")
        d = [a - b for a, b in zip(res["DEP"], res["CRITFLAG"])]
        print("  DEP - CRITFLAG loss: mean", round(statistics.fmean(d), 2), "95% CI", boot_ci(d))
        r = statistics.fmean(cust["DEP"]) / statistics.fmean(cust["SILO"]) - 1
        r2 = statistics.fmean(cust["DEP"]) / statistics.fmean(cust["CRITFLAG"]) - 1
        print("  DEP customer-hours vs SILO:", f"{r:+.1%}", "| vs CRITFLAG:", f"{r2:+.1%}")
```

Saída esperada:

```text
== Riverbend: orders {'SILO': ['F1', 'F4', 'F3', 'F2'], 'CRITFLAG': ['F3', 'F2', 'F1', 'F4'], 'DEP': ['F2', 'F3', 'F1', 'F4']}
  SILO     weighted critical loss  52.75  customer-hours(k)   133.0
  CRITFLAG weighted critical loss   3.97  customer-hours(k)   222.5
  DEP      weighted critical loss   4.32  customer-hours(k)   227.6
  ORACLE   weighted critical loss   1.79
  DEP - CRITFLAG loss: mean 0.35 95% CI (-0.23, 0.97)
  DEP customer-hours vs SILO: +71.2% | vs CRITFLAG: +2.3%
== Port Halvard: orders {'SILO': ['H1', 'H6', 'H4', 'H2', 'H3', 'H5'], 'CRITFLAG': ['H4', 'H2', 'H3', 'H5', 'H1', 'H6'], 'DEP': ['H5', 'H3', 'H4', 'H2', 'H1', 'H6']}
  SILO     weighted critical loss  53.93  customer-hours(k)   103.2
  CRITFLAG weighted critical loss  31.63  customer-hours(k)   148.5
  DEP      weighted critical loss   9.61  customer-hours(k)   163.2
  ORACLE   weighted critical loss   9.61
  DEP - CRITFLAG loss: mean -22.01 95% CI (-22.4, -21.59)
  DEP customer-hours vs SILO: +58.2% | vs CRITFLAG: +9.9%
```

#### 5.2.2 Lendo os resultados à luz das hipóteses

| Hipótese | Riverbend (principal) | Port Halvard (validação independente) | Veredito |
|---|---|---|---|
| H1: DEP reduz a perda em ≥ 20% vs SILO | 52,75 → 4,32 (−92%) | 53,93 → 9,61 (−82%) | Sustentada nas duas |
| H2: DEP reduz a perda em ≥ 10% vs CRITFLAG | +0,35 (intervalo MC de 95% de −0,23 a 0,97), inteiramente acima do limiar de −0,40: uma redução de 10% fica descartada | −22,01 de 31,63 (−70%) | **Não sustentada** em Riverbend; sustentada em Port Halvard |
| H3: o ganho cresce com a divergência das ordens | As ordens diferem em 2 posições (F2/F3 trocados), mas sem ganho | As ordens diferem nas 4 posições críticas; ganho grande | Em parte; Riverbend é uma anomalia a explicar (§5.2.3) |
| H4a: clientes-hora ≤ +15% vs SILO | +71,2% | +58,2% | **Falha** nas duas |
| H4b: clientes-hora ≤ +15% vs CRITFLAG | +2,3% | +9,9% | Sustenta-se nas duas |
| Distância até ORACLE | DEP 4,32 vs ORACLE 1,79 | DEP 9,61 = ORACLE 9,61 | DEP longe do ótimo em Riverbend; ótimo em Port Halvard |

O resumo honesto é misto. A ordenação ciente da criticidade, de *qualquer* tipo, protege os serviços críticos de forma drástica em comparação com a ordenação pelos clientes, a um custo grande em clientes-hora que a teoria de programação previu (Capítulo 3). Se a *temporização* agrega valor sobre uma lista de clientes críticos depende da região: nenhum em Riverbend, muito em Port Halvard. Aplica-se a condição de falha pré-registrada "H2 falha numa região e se sustenta na outra": estreitar a alegação para as condições que distinguem as regiões e testar o mecanismo.

#### 5.2.3 Explicando a anomalia de Riverbend sem resgatar a hipótese

Em Riverbend, DEP restaura F2 (telecomunicações e hospital) antes de F3 (água), porque o tempo esperado até o impacto das telecomunicações (8 h) é um pouco anterior ao da água (8,7 h). CRITFLAG restaura F3 primeiro porque ele tem mais clientes. Mas F3 protege *dois* serviços ponderados — a água diretamente e o hospital por meio de sua dependência da água —, enquanto restaurar F2 primeiro protege as telecomunicações e apenas o caminho de energia do hospital, que tem uma reserva longa. Uma regra do menor tempo até o impacto ignora os **pesos e o espalhamento**; o Capítulo 3 nomeou isso como a fraqueza conhecida da heurística. A perda muito menor de ORACLE confirma que nenhuma das regras está perto do ótimo em Riverbend.

Essa explicação é post hoc. É legítimo relatá-la como uma *hipótese gerada pelo estudo confirmatório*, a ser testada em dados novos (o Capítulo 6 a testa em muitas regiões sintéticas); não é legítimo reexecutar o estudo principal com uma regra revisada e relatar isso como confirmatório.

### 5.3 O estudo de exercício de mesa com operadores

#### 5.3.1 Por que pessoas, e não apenas modelos

Uma regra de restauração que os operadores não seguem não tem consequência. O estudo de exercício de mesa pergunta se, dada a exibição do tempo efetivo até o impacto pilotada no Capítulo 4, operadores experientes escolhem ordenações que o modelo avalia como de menor consequência, e por que sim ou por que não.

#### 5.3.2 Desenho (sintético)

- **Participantes.** Doze operadores e gestores de emergências (P01–P12) de três concessionárias sintéticas, recrutados por meio dos parceiros com consentimento individual, nenhum do piloto. A participação foi voluntária e sem remuneração além das despesas; os gestores não ficaram sabendo quem participou.
- **Cruzamento intrassujeitos.** Cada participante ordenou a restauração em dois cenários isomórficos — topologia semelhante à de Port Halvard com alimentadores renomeados e posições embaralhadas —, uma vez com uma exibição convencional (número de clientes e sinalizações de clientes críticos) e uma vez com a exibição do tempo efetivo até o impacto acrescentada. A ordem das exibições e as versões dos cenários foram contrabalançadas.
- **Cegamento.** Os cenários não continham informações sobre o desfecho; os injects foram verificados no piloto quanto a pistas prematuras. Os analistas que pontuaram as justificativas em texto livre não sabiam qual condição de exibição as produziu.
- **Desfecho.** A *ordenação escolhida*, avaliada no simulador sobre os mesmos 500 sorteios do estudo principal — de modo que o desfecho é a consequência estimada pelo modelo da decisão do participante, e não sua preferência declarada. Secundários: tempo de decisão; códigos das justificativas.
- **Análise.** Comparação pareada de se cada participante escolheu a ordenação DEP sob cada exibição; teste exato de McNemar sobre os pares discordantes; diferenças descritivas de consequência; análise temática das justificativas.

#### 5.3.3 Resultados (sintéticos)

| Exibição convencional → exibição do tempo até o impacto | Participantes |
|---|---|
| Não DEP → DEP | 7 |
| Não DEP → não DEP | 5 |
| DEP → não DEP | 0 |
| DEP → DEP | 0 |

Todos os sete pares discordantes se moveram em direção a DEP. Sob a hipótese nula de que uma troca em qualquer direção é igualmente provável, a probabilidade exata bicaudal de sete ou mais trocas numa direção em sete é 2 × 0,5⁷ = 0,0156. Com doze participantes de três concessionárias, isso é evidência de que a exibição *pode* mudar as escolhas num exercício de mesa, e não uma estimativa de com que frequência os operadores mudariam a prática. Entre os cinco que não adotaram DEP, quatro mantiveram uma ordem semelhante à de CRITFLAG. Os códigos das justificativas (dois codificadores, divergências resolvidas e registradas) incluíram: *expectativa institucional* ("o conselho nos mede pelos clientes restaurados"; 4 participantes), *desconfiança dos números das reservas* ("já vi os registros de combustível dos hospitais — nunca batem com o papel"; 3) e *logística de campo* ("as equipes já estão perto do alimentador grande"; 3). O último tema identifica uma variável que o modelo omite: o tempo de deslocamento entre os alimentadores, que torna as durações de restauração dependentes da ordem.

#### 5.3.4 O que o exercício de mesa pode e não pode sustentar

Ele sustenta: a exibição é compreensível; ela desloca as escolhas no exercício de mesa em direção a uma consequência modelada menor; os operadores levantam objeções específicas que o modelo precisa tratar. Ele não pode sustentar: a adoção no mundo real; efeitos sob estresse, cansaço e informação incompleta; nem efeitos em concessionárias diferentes das três amostradas. Exercícios de mesa também são performances — os participantes sabem que estão sendo observados —, o que empurra para respostas "de aparência correta".

### 5.4 Validando o modelo

Seguindo [Sargent (2013)](https://doi.org/10.1057/jos.2012.20), a validação é evidência de que um modelo é adequado *para o seu propósito pretendido* — aqui, classificar as ordenações de restauração pela consequência sobre os serviços críticos —, e não de que ele é "verdadeiro".

| Tipo de validação | Evidência do Cascade Study (sintética) | O que estabelece | O que não estabelece |
|---|---|---|---|
| Validade aparente | Doze participantes do exercício de mesa e dois engenheiros parceiros revisaram a estrutura e as saídas do modelo | A estrutura é reconhecível pelos profissionais; nenhuma omissão gritante, exceto o tempo de deslocamento | Que os parâmetros estão certos |
| Validação histórica | A queda da tempestade de gelo de 2019 em Riverbend (todas as causas, registro sintético): o modelo, com os tempos de restauração registrados dos alimentadores, previu a perda de pressão da água em 9 h e o desvio do hospital em 13 h; os registros mostram 11 h e nenhum desvio (o hospital recebeu água por caminhão em 10 h) | A temporização da falha da água está na faixa certa; o modelo omite a ajuda mútua (água por caminhão), uma reserva humana | A acurácia para cenários induzidos por ciberataques; qualquer generalização a partir de um único evento |
| Testes de condições extremas | Reservas zero, reservas infinitas, um único alimentador, um serviço | O comportamento nos limites é sensato (invariantes do Capítulo 4) | O comportamento no interior |
| Variabilidade dos parâmetros | Escalonamento das reservas e conjuntos de pesos (Capítulo 6) | Quais conclusões dependem de quais parâmetros | A adequação estrutural |
| Validade operacional | Concordância entre a classificação das ordenações pelo modelo e a classificação especializada dos operadores em seis cenários: 5 das 6 primeiras escolhas coincidem | O modelo classifica as ordenações de modo muito parecido com o dos especialistas em casos familiares | Se algum dos dois está certo em casos não familiares |

A validação histórica produziu uma correção importante: o modelo trata as reservas como fixas, mas os operadores reais estendem as reservas — água por caminhão, entregas de combustível, alívio de carga no hospital. Um modelo sem essas reservas humanas é **conservador quanto à consequência** e pode **exagerar o benefício da reordenação**, porque ignora alternativas que os operadores usariam de qualquer forma. A tese precisa declarar isso.

### 5.5 Validação independente num segundo contexto

#### 5.5.1 Seleção segundo critérios declarados com antecedência

Port Halvard foi escolhida *antes* da simulação, segundo critérios derivados do mecanismo e registrados na emenda ao pré-registro do Capítulo 3: mais alimentadores críticos (quatro), divergência entre a ordem das reservas e a ordem dos clientes entre os alimentadores críticos, duas equipes e reservas hospitalares longas, apoiadas por contratos de combustível. Outro modelador construiu a configuração de Port Halvard a partir da documentação dos parceiros, sem acesso aos resultados de Riverbend. Esses passos reduzem, mas não eliminam, o risco de um contexto de validação que favoreça o método: os próprios critérios foram escolhidos para dar ao mecanismo uma chance de operar. Isso é aceitável para um teste do mecanismo, *não* para uma estimativa de com que frequência o método ajuda em regiões reais. O Capítulo 6 trata da segunda pergunta com muitas regiões geradas aleatoriamente.

#### 5.5.2 Transportabilidade

Um resultado se transporta de um contexto para outro quando a estrutura causal relevante para ele é compartilhada e as diferenças são medidas. [Pearl and Bareinboim (2014)](https://doi.org/10.1214/14-STS486) formalizam quando constatações experimentais podem ser transportadas entre populações. Informalmente, para o Cascade Study: o mecanismo (reservas, restauração sequencial, consequência ponderada) é compartilhado; os *moderadores* que diferem — número de alimentadores críticos, divergência das ordens, número de equipes, duração das reservas — precisam ser medidos em qualquer região-alvo antes que o resultado seja aplicado. Uma concessionária que conhece essas quatro coisas sobre si mesma pode estimar se DEP tende a superar sua lista atual; uma que não as conhece, não pode.

### 5.6 Relatando o estudo principal

Relate, no mínimo: o pré-registro e todas as emendas, com datas; o registro de desvios; cada hipótese com seu veredito, incluindo as falhas; os tamanhos de efeito em relação aos menores efeitos de interesse; os intervalos de Monte Carlo rotulados como tais; as distâncias até ORACLE; o desenho do exercício de mesa, o consentimento, as desistências e os resultados, com os testes exatos e os temas qualitativos; cada tipo de validação, com o que ele estabelece; e a configuração das duas regiões *no nível de detalhe permitido pelos níveis de proteção da informação* (Capítulo 7). Siga uma estrutura de relato reconhecida para estudos de simulação quando existir uma no veículo de publicação pretendido e, para o exercício de mesa, siga as expectativas de transparência da pesquisa com seres humanos na sua área.

### 5.7 Erros comuns e limites

- Analisar as médias de duas políticas separadamente em vez das diferenças pareadas.
- Aumentar o número de sorteios até que uma diferença seja "significativa".
- Apresentar um intervalo de Monte Carlo como incerteza sobre o mundo.
- Reexecutar o estudo confirmatório com uma regra revisada depois de ver os resultados e chamá-lo de confirmatório.
- Escolher um contexto de validação porque o método vai se sair bem nele, sem dizê-lo.
- Medir as preferências declaradas dos operadores em vez das consequências de suas escolhas.
- Tratar a validade aparente como validação dos parâmetros.

- Ler a falha de H2 em Riverbend como motivo para revisar DEP e reexecutar o estudo principal sob o mesmo pré-registro.
- Relatar um deslocamento estatisticamente significativo no exercício de mesa como evidência de adoção, quando doze participantes de três concessionárias mostram apenas que uma exibição pode mudar escolhas.
- Tratar um único evento histórico, como a tempestade de gelo de 2019, como validação para cenários induzidos por ciberataques.
- Omitir a distância até ORACLE, que mostra quão longe qualquer regra está da melhor ordenação.

### Exercícios — capítulo 5

**EX027 — Execute e interprete o estudo principal.** *Objetivo:* reproduzir e interpretar o Laboratório 5. *Insumos:* o código de §5.2.1. *Restrições:* off-line; registrar a saída exata. *Passos:* (1) executar o laboratório; (2) preencher a tabela de hipóteses de §5.2.2 a partir da sua saída; (3) calcular a variação relativa de DEP em relação a CRITFLAG em cada região; (4) escrever um parágrafo de resultados de 150 palavras que um revisor hostil aceitaria. *Evidência esperada:* saída, tabela, parágrafo. *Rubrica:* 3 = saída exata, H2 relatada como falha em Riverbend e sustentada em Port Halvard, falha de H4a relatada, sem resgate; 2 = números corretos, parágrafo exagera; 1 = erros; 0 = não executado.

**EX028 — Pareado versus não pareado.** *Objetivo:* ver por que os números aleatórios comuns importam. *Insumos:* Laboratório 5. *Restrições:* off-line. *Passos:* (1) para Riverbend, calcular o desvio-padrão das perdas de DEP, das perdas de CRITFLAG e das diferenças por sorteio; (2) calcular um intervalo de 95% não pareado para a diferença de médias usando a aproximação normal; (3) comparar com o intervalo pareado; (4) explicar a diferença em 100 palavras. *Evidência esperada:* três desvios-padrão, dois intervalos, explicação. *Rubrica:* 3 = DPs de cerca de 6,36 (DEP), 4,57 (CRITFLAG) e 6,79 (diferenças); intervalo não pareado de cerca de −0,34 a 1,04 contra o pareado de −0,24 a 0,95; explica que o pareamento ajudou apenas modestamente porque as perdas das políticas são fracamente correlacionadas — elas se compensam quanto a qual serviço falha num dado sorteio — e que o DP das diferenças pode exceder o DP de cada política e ainda ficar abaixo de √(Var A + Var B); 2 = números certos, explicação presume que o pareamento sempre reduz a variância; 1 = erro; 0 = nada.

**EX029 — Taxonomia da incerteza.** *Objetivo:* classificar a incerteza. *Insumos:* cinco afirmações: (a) "com 5.000 sorteios o intervalo se estreitaria"; (b) "o combustível do hospital pode ser menor do que o diretor de instalações disse"; (c) "o tempo de deslocamento entre os alimentadores não é modelado"; (d) "os pesos refletem os valores de um único painel"; (e) "as reservas podem não ser triangulares". *Restrições:* classificar cada uma como incerteza de Monte Carlo, de parâmetros, estrutural ou de valores e nomear o método que a trata. *Passos:* (1) classificar cada afirmação; (2) justificar a classe numa frase; (3) nomear o método que reduz ou expõe essa incerteza. *Evidência esperada:* tabela. *Rubrica:* 3 = (a) Monte Carlo, (b) parâmetros, (c) estrutural, (d) valores, (e) parâmetros ou estrutural com justificativa, com métodos adequados; 2 = um erro; 1 = dois ou mais; 0 = nada.

**EX030 — Crítica do desenho do exercício de mesa.** *Objetivo:* fortalecer um desenho com seres humanos. *Insumos:* §5.3.2. *Restrições:* propor pelo menos cinco melhorias dentro dos limites éticos e práticos. *Passos:* (1) identificar as ameaças — características de demanda, amostra pequena, três concessionárias, ausência de pressão de tempo, reconhecimento dos cenários isomórficos; (2) propor uma mudança de desenho para cada uma; (3) declarar quanto custa cada mudança. *Evidência esperada:* tabela. *Rubrica:* 3 = cinco ou mais ameaças reais com mudanças viáveis e custos honestos; 2 = três ou quatro; 1 = genéricas; 0 = nada.

**EX031 — Matriz de evidências de validação.** *Objetivo:* planejar a validação do seu próprio modelo. *Insumos:* um modelo da sua pesquisa ou do Cascade Study. *Restrições:* pelo menos quatro tipos de validação; para cada um, a evidência, o que ela estabelece e o que não estabelece. *Passos:* (1) escolher pelo menos quatro tipos de validação de §5.4; (2) para cada um, declarar a evidência que você coletaria; (3) declarar o que essa evidência estabelece e o que não estabelece; (4) identificar qual validação seria mais danosa à sua alegação se falhasse. *Evidência esperada:* matriz e parágrafo. *Rubrica:* 3 = tipos bem escolhidos, limites honestos, teste mais danoso identificado e planejado cedo; 2 = limites ralos; 1 = apenas validade aparente; 0 = nada.

**EX032 — Memorando de transportabilidade.** *Objetivo:* aconselhar uma terceira concessionária. *Insumos:* uma concessionária sintética com cinco alimentadores, três deles com serviços críticos cuja ordem das reservas coincide com a ordem dos clientes, e uma equipe. *Restrições:* 300 palavras; usar os moderadores de §5.5.2. *Passos:* (1) medir os quatro moderadores para essa concessionária; (2) prever o ganho de DEP sobre CRITFLAG; (3) declarar de que dados você precisaria para mudar a sua previsão. *Evidência esperada:* memorando. *Rubrica:* 3 = prevê nenhum ganho porque as ordens coincidem, explica os moderadores e observa que os pesos ou o espalhamento ainda poderiam importar; 2 = previsão certa, raciocínio ralo; 1 = prevê um ganho; 0 = nada.

### Síntese do capítulo

O estudo principal comparou quatro ordenações sobre sorteios pareados com um limite oráculo. A ordenação ciente da criticidade, de qualquer tipo, protegeu os serviços críticos de forma drástica em comparação com a restauração pelos clientes e custou muito mais clientes-hora do que a margem declarada com antecedência — uma troca para a política pública, e não um ganho gratuito. A informação de temporização nada acrescentou a uma lista de clientes críticos em Riverbend e acrescentou muito em Port Halvard; a explicação post hoc (pesos e espalhamento ignorados por uma regra do menor tempo) é uma hipótese nova, e não um resgate. Um exercício de mesa cego mostrou que uma exibição do tempo até o impacto pode deslocar as escolhas dos operadores em direção a uma consequência modelada menor e trouxe à tona variáveis omitidas, como o tempo de deslocamento das equipes. A validação estabeleceu que o modelo é adequado para classificar ordenações em casos familiares e conservador porque omite as reservas humanas. Os intervalos de Monte Carlo descreveram apenas o ruído da simulação; a incerteza de parâmetros, a estrutural e a de valores ficam para o Capítulo 6.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 08

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Crítica dos pares e revisão

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Organizar a crítica adversarial da própria tese — red-teaming interno, revisão externa estruturada e colaboração adversarial — e registrá-la.
2. Detectar a circularidade entre modelo e política e testá-la com um descompasso deliberado do modelo.
3. Mapear as condições de contorno com análise de sensibilidade e com muitos contextos gerados, reconhecendo que o próprio gerador é um modelo.
4. Distinguir uma revisão confirmatória de uma exploratória e rotular cada uma.
5. Escrever resultados negativos e estreitados de modo que sejam úteis para os outros.
6. Conduzir uma revisão de duplo uso das constatações da pesquisa e decidir o que publicar, generalizar, adiar ou restringir.
7. Escrever uma resposta aos revisores que mude as alegações em vez de defendê-las.

O Capítulo 5 produziu um resultado misto: forte benefício sobre a ordenação pelos clientes, uma troca que não atendeu sua margem, nenhum benefício sobre as listas de sinalização crítica numa região e um grande benefício na outra. É neste capítulo que a tese conquista suas alegações tentando destruí-las.

### 6.1 A crítica como método

A revisão por pares na publicação chega tarde demais e é rasa demais para ser o principal controle de qualidade de um projeto de doutorado. Incorpore a crítica ao projeto:

- **Red team interno.** Antes da submissão, pede-se a um colega que não trabalhou no estudo que quebre a alegação principal, com acesso ao código, aos dados e ao pré-registro. O relatório dele é respondido por escrito.
- **Revisão externa estruturada.** Parceiros e especialistas do domínio revisam a estrutura do modelo e as alegações, usando um formulário que pede a objeção *mais forte*, e não uma impressão geral.
- **Colaboração adversarial.** Onde um pesquisador crível defende uma visão oposta (por exemplo, que a priorização baseada na topologia é suficiente), desenhe um teste conjunto cujos desfechos os dois lados concordem de antemão que mudariam sua visão.
- **Pré-mortem.** Imagine que a tese foi rejeitada na defesa; escreva as razões do examinador. Depois, teste cada razão.

Toda crítica e toda resposta entram no registro de revisões da tese. Os examinadores confiam em trabalhos cujas fraquezas foram visivelmente atacadas.

### 6.2 O relatório do red team sobre o Cascade Study (sintético)

Um red team interno produziu cinco objeções principais:

1. **Circularidade.** "DEP é calculada a partir das próprias reservas e do próprio mapa de dependências do modelo e depois avaliada no mesmo modelo. É claro que se sai bem. Na realidade, o mapa do planejador está errado."
2. **Artefato das reservas curtas.** "As reservas de Riverbend são curtas em relação aos tempos de restauração. Com contratos de combustível realistas, nada do que vocês fizerem importa."
3. **Seleção do contexto.** "Port Halvard foi escolhida para fazer o mecanismo operar. Duas regiões, uma escolhida para o método, não podem estimar com que frequência DEP ajuda."
4. **Fraqueza da heurística.** "O próprio oráculo de vocês mostra que DEP está longe do ótimo em Riverbend. Por que alguém adotaria uma regra que vocês sabem ser subótima?"
5. **Duplo uso.** "Vocês mostraram que a perda de serviços críticos depende de qual alimentador é restaurado primeiro e de se o mapa do planejador está certo. Isso diz a um adversário o que atacar: os dados de prioridade de restauração."

Cada objeção é uma hipótese sobre o resultado. O restante do capítulo as testa.

### 6.3 Atividade prática: condições de contorno, descompasso e muitas regiões

O laboratório importa o simulador do Laboratório 5 (salve-o como `lab5_mc.py` na mesma pasta).

```python
# Lab 6 - boundary conditions, model mismatch and many synthetic regions (offline)
# Save Lab 5 as lab5_mc.py in the same folder first.
import random, statistics
import lab5_mc as m

def mean_gain(region, **kw):
    _, res, cust = m.experiment(region, n=300, oracle=False, **kw)
    return (statistics.fmean(res["DEP"]) - statistics.fmean(res["CRITFLAG"]),
            statistics.fmean(res["DEP"]) - statistics.fmean(res["SILO"]))

print("1) Riverbend buffer scaling: (DEP-CRITFLAG, DEP-SILO) mean loss")
for s in (0.5, 1.0, 2.0, 4.0):
    a, b = mean_gain(m.RIVERBEND, buffer_scale=s)
    print(f"   scale {s:3.1f}: {a:7.2f} {b:7.2f}")

print("2) Model mismatch: water plant truly on F1, planner believes F3")
true = {**m.RIVERBEND, "services": {**m.RIVERBEND["services"], "WATER": ("F1",) + m.RIVERBEND["services"]["WATER"][1:]}}
_, res, _ = m.experiment(true, n=300, oracle=False, believed_feeder={"WATER": "F3"})
print("   mean loss SILO %.2f CRITFLAG %.2f DEP %.2f" % tuple(statistics.fmean(res[k]) for k in ("SILO", "CRITFLAG", "DEP")))

print("3) 200 random synthetic regions: gain of DEP over CRITFLAG vs rank divergence")
def random_region(rng):
    feeders = [f"G{i}" for i in range(1, 6)]
    cust = {f: rng.choice([500, 1000, 2000, 4000, 8000]) for f in feeders}
    crit = rng.sample(feeders, 3)
    services = {}
    for i, f in enumerate(crit):
        lo = rng.choice([1, 4, 12, 36])
        services[f"S{i}"] = (f, (lo, lo * 3, lo * 2), rng.choice([3.0, 4.0, 5.0]), None)
    return {"customers": cust, "crews": 1, "dur": (2, 6, 4), "services": services}
def divergence(region):
    flag = [f for f in m.critflag(region) if f in {v[0] for v in region["services"].values()}]
    depo = [f for f in m.dep(region) if f in flag]
    return sum(1 for a, b in zip(flag, depo) if a != b)
rng = random.Random(2026)
rows = []
for _ in range(200):
    r = random_region(rng)
    _, res, _ = m.experiment(r, n=60, oracle=False)
    rows.append((divergence(r), statistics.fmean(res["DEP"]) - statistics.fmean(res["CRITFLAG"])))
for d in sorted({d for d, _ in rows}):
    g = [x for dd, x in rows if dd == d]
    print(f"   positions differing={d}: regions={len(g):3d} mean gain={statistics.fmean(g):7.2f} share DEP worse={sum(x > 0 for x in g)/len(g):.2f}")
```

Saída esperada:

```text
1) Riverbend buffer scaling: (DEP-CRITFLAG, DEP-SILO) mean loss
   scale 0.5:    6.10  -86.14
   scale 1.0:    0.38  -47.57
   scale 2.0:    0.02   -7.25
   scale 4.0:    0.00    0.00
2) Model mismatch: water plant truly on F1, planner believes F3
   mean loss SILO 29.41 CRITFLAG 26.21 DEP 22.29
3) 200 random synthetic regions: gain of DEP over CRITFLAG vs rank divergence
   positions differing=0: regions= 69 mean gain=   0.00 share DEP worse=0.00
   positions differing=2: regions= 77 mean gain= -11.21 share DEP worse=0.01
   positions differing=3: regions= 54 mean gain= -23.97 share DEP worse=0.00
```

#### 6.3.1 Objeção 1: circularidade

Na parte 2, a estação de água verdadeira está em F1, mas tanto a lista de clientes críticos quanto o planejador de DEP acreditam que ela está em F3. Toda política ciente da criticidade se degrada fortemente: DEP de 4,32 para 22,29, CRITFLAG de 3,97 para 26,21. SILO na verdade melhora (52,75 → 29,41) porque restaura F1 primeiro por razões de clientes e, com isso, acaba restaurando a água. A objeção é **sustentada numa forma mais forte do que a que o red team declarou**: o valor de *qualquer* ordenação ciente da criticidade depende da acurácia do mapa de dependências. A revisão consiste em tornar a acurácia do mapa uma pré-condição declarada da alegação, acrescentar ao método um procedimento de auditoria do mapa e recomendar a medição do erro do mapa em qualquer aplicação de campo. Isso transforma uma fraqueza numa contribuição: um pré-requisito *mensurável* que as concessionárias podem verificar.

#### 6.3.2 Objeção 2: reservas curtas

A parte 1 escalona todas as reservas. À medida que as reservas dobram, a vantagem de DEP sobre SILO cai de 47,57 para 7,25 horas de serviço ponderadas e desaparece com quatro vezes as reservas obtidas. A objeção é **sustentada como condição de contorno**: quando as reservas excedem com folga o tempo total de restauração, a ordenação não importa para os serviços críticos. Essa é exatamente a previsão do mecanismo no Capítulo 3, então o resultado apoia o mecanismo ao mesmo tempo em que limita o escopo da alegação. Ele também revela algo que o red team não levantou: com *metade* das reservas obtidas, DEP é **pior** do que CRITFLAG em 6,10 — a fraqueza da heurística da objeção 4 cresce quando as reservas são curtas, porque os erros sobre qual alimentador protege mais serviços ponderados custam mais.

#### 6.3.3 Objeção 3: seleção do contexto

A parte 3 gera 200 regiões sintéticas com cinco alimentadores, três serviços críticos, números de clientes, faixas de reservas e pesos aleatórios, e as classifica por quantas posições diferem entre as ordens de CRITFLAG e de DEP entre os alimentadores críticos. Onde as ordens coincidem (69 regiões), o ganho é exatamente zero — como precisa ser. Onde diferem em duas posições (77 regiões), DEP reduz a perda média em 11,21 e é pior em cerca de 1% das regiões; onde diferem em três (54 regiões), em 23,97, nunca pior nesta amostra. O padrão previsto por H3 se sustenta em contextos que não foram escolhidos para o método.

A objeção do red team é, no entanto, **parcialmente sustentada**: o gerador sorteia o número de clientes e as reservas de forma independente, e esse pressuposto fixa com que frequência a divergência ocorre. As regiões reais podem ter correlações em qualquer direção. Se os alimentadores grandes tendem a abrigar instalações com reservas longas (hospitais grandes com grandes estoques de combustível), a ordem de maior primeiro de CRITFLAG corre no sentido oposto à ordem de menor reserva primeiro de DEP, e a divergência se torna *mais* comum; se os alimentadores grandes tendem a abrigar serviços de reserva curta (centrais de telecomunicações de áreas densas, a bateria), as duas ordens concordam e a divergência se torna mais rara. A frequência da divergência nas regiões reais é uma pergunta *empírica* que a tese não pode responder com geradores sintéticos; a alegação precisa ficar condicionada à divergência, que uma concessionária pode medir sobre si mesma.

#### 6.3.4 Objeção 4: uma heurística sabidamente subótima

Sustentada. O limite oráculo mostra que uma regra que use os pesos e o espalhamento — por exemplo, ordenar os alimentadores pelo valor ponderado dos serviços que protegem por hora de restauração, levando em conta as dependências — poderia se sair melhor. O candidato pode desenvolver tal regra, mas ela precisa ser rotulada como **exploratória**: ela seria desenhada depois de ver os resultados confirmatórios e precisa ser confirmada em novas configurações (novas regiões, novas sementes, pré-registrada) antes que qualquer alegação seja feita. A tese pode apresentá-la legitimamente como o próximo passo mais promissor.

### 6.4 Análise de sensibilidade além de um fator por vez

Variar um fator por vez (reservas, depois pesos, depois durações) deixa escapar as interações — o resultado do escalonamento das reservas mostra que a fraqueza da heurística interage com a duração das reservas. A **análise de sensibilidade global** varia todos os insumos incertos juntos e reparte a variância da saída entre os insumos e suas interações; [Saltelli et al. (2008)](https://doi.org/10.1002/9780470725184) é uma introdução padrão. Para uma tese, uma sequência prática é: uma triagem de um fator por vez para encontrar os insumos que importam; um desenho estruturado (por exemplo, um fatorial sobre os poucos que importam); e então, se os recursos permitirem, índices baseados em variância. Relate do que a conclusão depende, nos termos do leitor: *"A vantagem de DEP sobre a ordenação por sinalização crítica exige divergência entre as ordens das reservas e dos clientes, um mapa de dependências sem erros de alimentador e reservas menores do que cerca de duas vezes o tempo esperado de restauração."*

A sensibilidade aos valores é distinta da sensibilidade aos parâmetros. Os pesos declarados com antecedência codificam as prioridades de um único painel. Reexecute com conjuntos alternativos de pesos — pesos iguais, pesos de um segundo painel, pesos que incluam os clientes comuns — e relate se as conclusões mudam (EX034).

### 6.5 Resultados negativos e estreitamento

O Cascade Study tem agora uma alegação estreitada:

> Em cenários sintéticos de queda na distribuição que exigem restauração manual sequencial, ordenar pelo tempo até o impacto dos serviços críticos reduz a perda ponderada de serviços críticos declarada com antecedência em relação à ordenação por sinalização de clientes críticos **somente** quando as duas ordens diferem, o mapa de dependências é acurado e as reservas são curtas em relação ao tempo de restauração; onde essas condições se verificam, a redução é grande e os clientes-hora adicionais em relação à ordenação por sinalização ficam dentro de uma margem de 15%. Qualquer ordenação ciente da criticidade protege os serviços críticos muito melhor do que a ordenação pelos clientes, a um custo em clientes-hora de cerca de 60–70% nas regiões estudadas, o que excede a margem declarada com antecedência e é uma troca de política pública, e não uma melhoria técnica. A heurística do menor tempo até o impacto pode ter desempenho inferior ao da ordenação por sinalização quando as reservas são muito curtas, porque ignora os pesos e o espalhamento.

Observe o que a alegação estreitada faz: declara condições que uma concessionária pode medir; relata a margem não atendida; relata onde o método perde; e separa a constatação robusta (ordenação ciente da criticidade versus pelos clientes) da contribuição condicional (temporização versus listas). Um resultado negativo sobre H2 em Riverbend não é escondido; ele é a evidência que define o limite.

**Publique os resultados negativos de forma útil.** Declare a hipótese, o desenho, o tamanho do efeito com seu intervalo e o menor efeito de interesse que ele descarta. "Nenhuma diferença significativa" é inútil; "uma redução de 10% ou mais em relação à ordenação por sinalização fica descartada em Riverbend" é útil.

### 6.6 Revisão de duplo uso das constatações

Aplicando as três perguntas do Capítulo 1 (§1.4.3):

| Constatação | Ganho para um adversário | Valor defensivo | Decisão |
|---|---|---|---|
| A ordenação ciente da criticidade protege os serviços críticos; custo em clientes-hora | Desprezível: amplamente compreendido | Apoia o debate de políticas sobre as prioridades de restauração | Publicar |
| O valor depende da acurácia do mapa de dependências | Moderado: sugere que corromper ou roubar os dados de prioridade de restauração e as listas de clientes críticos poderia amplificar um ataque | Alto: diz às concessionárias que protejam a integridade e a confidencialidade dos dados de prioridade de restauração e que auditem os mapas | Publicar em nível geral com a recomendação defensiva; nenhum exemplo de como alterar esses dados |
| Regiões sintéticas, código e parâmetros | Baixo: lugares inventados | Alto: reprodutibilidade | Publicar (Capítulo 7, nível T0) |
| Faixas de reservas e relações alimentador–instalação derivadas dos parceiros | Alto: informação de alvos | Baixo além do parceiro | Reter; descrever apenas faixas agregadas |
| Justificativas do exercício de mesa | Baixo | Moderado | Publicar os temas sem identificadores de função mais concessionária |

A segunda linha ilustra um padrão recorrente na pesquisa sobre infraestrutura: uma constatação de resiliência muitas vezes funciona também como uma constatação de superfície de ataque. O contexto de ameaça relevante é público — o [AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) da CISA descreve o pré-posicionamento nas redes de TI da infraestrutura, onde os dados de planejamento costumam residir —, então a recomendação defensiva (proteção da integridade e auditoria dos dados de prioridade de restauração) tem valor claro. Coordene com os parceiros e, quando apropriado, com o órgão setorial de compartilhamento de informações pertinente antes da publicação (Capítulo 8).

### 6.7 Respondendo aos revisores

Uma boa carta de resposta cita cada comentário, declara se ele foi aceito, parcialmente aceito ou não aceito, descreve a mudança (com a localização) e — quando não aceito — apresenta evidências, e não opiniões. Mais importante, ela **muda as alegações**, e não apenas a redação. Compare:

- *Defensiva:* "Agradecemos ao revisor. Port Halvard foi selecionada segundo critérios declarados com antecedência, então o viés de seleção não é uma preocupação."
- *Responsiva:* "Parcialmente aceito. Port Halvard foi selecionada segundo critérios derivados do mecanismo e declarados com antecedência, o que a torna um teste justo do mecanismo, mas não uma estimativa de com que frequência DEP ajuda. Acrescentamos uma análise de 200 regiões (§6.3.3), estreitamos a alegação para regiões com divergência das ordens e declaramos que a frequência da divergência nas regiões reais é desconhecida (Limitações, item 4)."

### 6.8 Erros comuns e limites

- Tratar a revisão por pares como um obstáculo em vez de um método.
- Avaliar uma política apenas no modelo usado para derivá-la.
- Relatar apenas a sensibilidade de um fator por vez.
- Tratar um gerador de contextos aleatórios como uma amostra da realidade.
- Apresentar uma revisão exploratória como confirmatória.
- Escrever os resultados negativos como "não significativos".
- Pular a revisão de duplo uso porque os resultados são "apenas simulações".

- Aceitar uma objeção do red team na forma original sem testar se uma versão mais forte se sustenta, como aconteceu com a circularidade.
- Tratar uma condição de contorno como uma derrota em vez de uma previsão confirmada do mecanismo que estreita a alegação.
- Presumir que os pressupostos de independência de um gerador de regiões aleatórias correspondem às regiões reais, onde o número de clientes e as reservas podem ser correlacionados.
- Escrever uma carta de resposta que agradece aos revisores e defende a alegação original em vez de mudá-la onde as evidências o exigem.
- Publicar as faixas de reservas derivadas dos parceiros porque parecem inofensivas de forma agregada.

### Exercícios — capítulo 6

**EX033 — Relatório do red team.** *Objetivo:* atacar a sua própria alegação. *Insumos:* a alegação do Cascade Study antes do estreitamento (resumo do Capítulo 5) ou a sua própria. *Restrições:* pelo menos cinco objeções, cada uma declarada como hipótese testável. *Passos:* (1) escrever cada objeção; (2) dizer que evidência a sustentaria ou a descartaria; (3) desenhar o teste; (4) prever o desfecho antes de executar qualquer coisa. *Evidência esperada:* relatório. *Rubrica:* 3 = objeções específicas e testáveis, incluindo circularidade e seleção do contexto, com previsões registradas antes dos testes; 2 = uma ou duas não testáveis; 1 = genéricas; 0 = nada.

**EX034 — Sensibilidade aos pesos.** *Objetivo:* testar a sensibilidade aos valores. *Insumos:* Laboratório 5 e Laboratório 6. *Restrições:* off-line. *Passos:* (1) definir todos os pesos dos serviços como 1,0 nas duas regiões; (2) reexecutar a comparação principal; (3) registrar as perdas de DEP, CRITFLAG e SILO; (4) declarar se cada veredito da tabela de hipóteses muda; (5) explicar por quê. *Evidência esperada:* código modificado, saídas, parágrafo. *Rubrica:* 3 = saídas exatas, análise correta dos vereditos, explicação ligada ao espalhamento e aos pesos; 2 = saídas certas, explicação rala; 1 = erros; 0 = não executado.

**EX035 — Experimento de erro do mapa.** *Objetivo:* quantificar a fragilidade diante de erros no mapa. *Insumos:* Laboratório 6, parte 2. *Restrições:* off-line. *Passos:* (1) repetir o descompasso com a central de telecomunicações verdadeiramente em F4 enquanto os planejadores acreditam que está em F2; (2) registrar as perdas; (3) comparar com a parte 2; (4) propor um procedimento de auditoria do mapa com uma meta de acurácia mensurável. *Evidência esperada:* saídas e procedimento. *Rubrica:* 3 = saídas corretas, comparação com o descompasso da água, procedimento de auditoria mensurável (verificação de campo amostrada, taxa de acurácia, aprovação do responsável); 2 = procedimento vago; 1 = não executado corretamente; 0 = nada.

**EX036 — Crítica do gerador.** *Objetivo:* reconhecer o gerador como um modelo. *Insumos:* `random_region` no Laboratório 6. *Restrições:* propor uma mudança que codifique uma correlação plausível do mundo real. *Passos:* (1) modificar o gerador para que os alimentadores maiores tendam a abrigar serviços críticos com reservas mais longas; (2) reexecutar a parte 3; (3) comparar a distribuição da divergência e dos ganhos com a parte 3 original; (4) prever, e depois verificar, o que a correlação oposta faria; (5) explicar o que isso significa para a alegação. *Evidência esperada:* código, saída, parágrafo. *Rubrica:* 3 = correlação implementada de forma sensata; o estudante percebe que essa correlação faz as ordens de CRITFLAG e de DEP correrem em sentidos opostos, de modo que a divergência se torna *mais* frequente (as regiões sem divergência caem fortemente), e explica que a correlação oposta a tornaria mais rara, então a alegação precisa continuar condicionada à divergência medida; 2 = implementação sólida, mas a direção do efeito mal interpretada; 1 = sem comparação; 0 = nada.

**EX037 — Decisão de duplo uso.** *Objetivo:* decidir o tratamento de publicação. *Insumos:* quatro constatações da sua própria pesquisa ou: (a) uma lista de concessionárias de água cujo SCADA é alcançável pelo produto de acesso remoto de um fornecedor específico; (b) a observação de que os produtos de acesso remoto são um ponto de entrada comum entre os setores; (c) um método para estimar o tempo até o impacto a partir de dados públicos das instalações; (d) as estimativas de tempo até o impacto de hospitais nomeados numa cidade. *Restrições:* as três perguntas de §1.4.3. *Passos:* (1) avaliar o ganho para cada constatação; (2) avaliar o valor defensivo; (3) decidir entre publicar, generalizar, adiar e restringir; (4) declarar quem deve ser notificado antes da publicação. *Evidência esperada:* tabela. *Rubrica:* 3 = (a) restringir e notificar por divulgação coordenada, (b) publicar, (c) publicar com cuidado, (d) reter ou restringir, com raciocínio sólido; 2 = uma mal avaliada; 1 = duas ou mais; 0 = nada.

**EX038 — Carta de resposta.** *Objetivo:* mudar as alegações em resposta à crítica. *Insumos:* as cinco objeções do red team em §6.2. *Restrições:* uma resposta por objeção; pelo menos duas devem levar a uma alegação mudada. *Passos:* (1) citar cada objeção; (2) marcá-la como aceita, parcialmente aceita ou não aceita; (3) descrever a mudança e sua localização; (4) apresentar evidências para qualquer não aceitação. *Evidência esperada:* carta de resposta. *Rubrica:* 3 = responsiva em vez de defensiva, alegações mudadas onde justificado, trabalho exploratório rotulado; 2 = majoritariamente responsiva; 1 = defensiva; 0 = nada.

### Síntese do capítulo

A crítica faz parte do método. As objeções do red team se tornaram hipóteses e testes. A circularidade foi sustentada numa forma mais forte — toda política ciente da criticidade depende de um mapa de dependências acurado —, o que se tornou uma pré-condição mensurável e uma recomendação defensiva. As reservas curtas foram confirmadas como uma condição de contorno prevista pelo mecanismo, e as reservas muito curtas expuseram a fraqueza da heurística. Uma análise de 200 regiões apoiou o mecanismo em contextos não escolhidos para ele, ao mesmo tempo em que nos lembrou de que um gerador é um modelo. A alegação estreitada declara condições mensuráveis, relata a margem não atendida e separa a constatação robusta da contribuição condicional. A revisão de duplo uso mostrou que uma constatação de resiliência também pode ser uma constatação de superfície de ataque e decidiu o que publicar e em que nível.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 08

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Síntese da tese e arquivo de reprodutibilidade

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Estruturar uma tese como um argumento em que cada alegação está ligada a evidência, garantia, escopo e limitação.
2. Decidir entre uma monografia e uma tese por publicações e integrar qualquer uma delas num único argumento coerente.
3. Desenhar um arquivo de reprodutibilidade em níveis que libere tanto quanto for lícito e seguro, sob a proteção das informações de infraestrutura.
4. Distinguir dados sintéticos inventados de dados sintéticos calibrados a lugares reais e avaliar o risco residual de divulgação.
5. Documentar modelos, conjuntos de dados e estudos de simulação com estruturas reconhecidas.
6. Escrever uma seção de limitações que informe em vez de se desculpar.

O Capítulo 6 produziu a alegação estreitada. Este capítulo monta a tese em torno dela e constrói o arquivo que permite que outros a verifiquem sem expor a infraestrutura que ela estuda.

### 7.1 A tese como argumento

Uma tese não é um relatório de tudo o que foi feito; ela é um argumento a favor de uma contribuição. Um andaime útil é a análise de argumentos de Toulmin ([Toulmin, 1958/2003](https://doi.org/10.1017/CBO9780511840005)): uma **alegação** apoiada por **dados** (evidências) por meio de uma **garantia** (a razão pela qual as evidências apoiam a alegação), com um **respaldo** para a garantia, um **qualificador** (com que força) e **refutações** (condições sob as quais a alegação falha). Aplicado à pesquisa sobre infraestrutura:

| Elemento | Exemplo do Cascade Study |
|---|---|
| Alegação | A ordenação pelo tempo até o impacto reduz a perda ponderada de serviços críticos em relação à ordenação por sinalização crítica quando as ordens divergem, os mapas são acurados e as reservas são curtas. |
| Dados | Simulações pareadas de Riverbend e Port Halvard; análise de 200 regiões; testes de erro do mapa e de escalonamento das reservas. |
| Garantia | O simulador representa o esgotamento das reservas e a restauração sequencial de forma adequada para classificar as ordenações. |
| Respaldo | Testes de verificação; reprodução das linhas de base; validação histórica da temporização da água; validade operacional contra as classificações dos especialistas. |
| Qualificador | Em regiões sintéticas, uma única classe de cenários (quedas na distribuição que exigem restauração manual sequencial), pesos declarados com antecedência. |
| Refutações | Erros no mapa; reservas longas; conjuntos de pesos que favorecem o espalhamento; reservas humanas e tempo de deslocamento omitidos; frequência real da divergência desconhecida. |

Cada capítulo da tese deve contribuir com um elemento identificável. Um capítulo que não fornece nenhum é candidato a apêndice.

### 7.2 Monografia ou tese por publicações

Uma **monografia** apresenta um único argumento integrado; uma **tese por publicações** reúne artigos com uma introdução e uma conclusão integradoras. As teses sobre infraestrutura muitas vezes misturam gêneros — um artigo de modelo, um estudo empírico com operadores, uma análise de políticas —, o que combina com as teses por publicações, mas os capítulos integradores precisam fazer um trabalho real: declarar a alegação abrangente, mostrar como cada artigo contribui com dados ou respaldo, conciliar as diferenças de escopo entre os artigos e apresentar as limitações do conjunto. As normas sobre formato, declarações de coautoria e publicação prévia diferem entre instituições; esta trilha educacional não concede diplomas e não pode orientar sobre as normas de nenhuma instituição, além de apontar que elas precisam ser verificadas cedo.

### 7.3 Estrutura da tese do Cascade Study

1. **Introdução.** Problema, lacuna, tipos de contribuição, alegação abrangente e seu escopo.
2. **Fundamentação.** Definições, literatura de interdependência e resiliência, prática de restauração, teoria de programação (Capítulos 1–2 deste livro).
3. **Método.** Mecanismo, hipóteses, linhas de base, protocolo, ética e proteção da informação (Capítulo 3).
4. **Verificação e linhas de base.** Reproduções, testes de verificação, elicitação e piloto (Capítulo 4).
5. **Estudo principal e validação.** Simulações, exercício de mesa, validação, segunda região (Capítulo 5).
6. **Crítica e limites.** Testes do red team, sensibilidade, análise de muitas regiões, alegação estreitada, revisão de duplo uso (Capítulo 6).
7. **Discussão.** O que os profissionais e os formuladores de políticas podem fazer com a alegação estreitada; o que continua desconhecido.
8. **Limitações.**
9. **Conclusão.**
10. **Apêndices.** Pré-registro e emendas, registro de desvios, listagem dos testes de verificação, protocolos de elicitação, materiais do exercício de mesa, manifesto do arquivo.

### 7.4 O arquivo de reprodutibilidade

#### 7.4.1 Objetivos e restrições

A reprodutibilidade nesta área precisa satisfazer dois objetivos que puxam em direções opostas: permitir que outros verifiquem o trabalho e não publicar informações que ajudem alguém a danificar a infraestrutura ou que identifiquem pessoas. Os [princípios FAIR](https://doi.org/10.1038/sdata.2016.18) — localizáveis, acessíveis, interoperáveis, reutilizáveis — ajudam aqui porque FAIR não significa aberto: os dados podem ser localizáveis e ter suas condições de acesso claramente descritas enquanto o próprio acesso é controlado.

#### 7.4.2 Níveis de liberação

| Nível | Quem pode acessar | O que contém no Cascade Study | Condições |
|---|---|---|---|
| T0 Público | Qualquer pessoa | Código do simulador, testes, definições das regiões sintéticas, sementes, saídas, scripts de análise, materiais do exercício de mesa sem identificadores | Licença declarada; identificador persistente |
| T1 Registrado | Pesquisadores que se registram e aceitam os termos | Faixas de elicitação agregadas, sem a identidade dos parceiros; conjuntos de cenários ampliados | Os termos de uso proíbem a reidentificação e a definição de alvos |
| T2 Controlado | Pesquisadores aprovados sob um acordo e, quando aplicável, aprovação ética | Transcrições pseudonimizadas do exercício de mesa e justificativas codificadas | Acordo de uso de dados; ambiente seguro; auditoria |
| T3 Retido | Não liberado; apenas descrito | Relações alimentador–instalação derivadas dos parceiros, estoques reais das reservas, mapas | Existência e natureza descritas na tese, para que os examinadores saibam o que falta e por quê |

O **manifesto** do arquivo lista cada arquivo com um hash criptográfico e seu nível, para que qualquer pessoa possa verificar que os arquivos públicos são os que foram usados, e os examinadores possam ver o que existe nos níveis mais altos.

#### 7.4.3 Atividade prática: construindo um manifesto em níveis

```python
# Lab 7 - build a tiered reproducibility manifest for a synthetic thesis archive (offline)
import hashlib, json, os, tempfile
files = {
    "code/lab5_mc.py": b"# simulation code\n",
    "data/synthetic_riverbend_params.csv": b"feeder,customers\nF1,9000\nF2,1200\nF3,2500\nF4,6000\n",
    "data/partner_feeder_map.csv": b"feeder,substation,gps\nF2,SUB-7,redacted\n",
    "results/mc_summary.json": b'{"mean_dloss": -46.86}\n',
    "docs/operator_interview_notes.txt": b"P03: we restore by customer count\n",
}
RULES = [  # first matching rule wins; order matters
    ("partner_", "T3-withheld: partner-owned infrastructure detail; describe, do not release"),
    ("interview", "T2-controlled: human-subjects data; release only under approved access agreement"),
    ("synthetic_", "T0-public"),
    ("code/", "T0-public"),
    ("results/", "T0-public"),
]
def tier(path):
    for key, label in RULES:
        if key in path:
            return label
    return "UNCLASSIFIED: stop and review"
with tempfile.TemporaryDirectory() as root:
    manifest = []
    for rel, content in sorted(files.items()):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(content)
        manifest.append({"path": rel, "sha256": hashlib.sha256(content).hexdigest()[:16], "tier": tier(rel)})
    print(json.dumps(manifest, indent=1))
    print("public files:", sum(m["tier"].startswith("T0") for m in manifest), "of", len(manifest))
```

Saída esperada:

```text
[
 {
  "path": "code/lab5_mc.py",
  "sha256": "e9db014f8aeb90da",
  "tier": "T0-public"
 },
 {
  "path": "data/partner_feeder_map.csv",
  "sha256": "160cefe894e75af9",
  "tier": "T3-withheld: partner-owned infrastructure detail; describe, do not release"
 },
 {
  "path": "data/synthetic_riverbend_params.csv",
  "sha256": "66bd4b5c8f37d273",
  "tier": "T0-public"
 },
 {
  "path": "docs/operator_interview_notes.txt",
  "sha256": "35c6e20265ce92c5",
  "tier": "T2-controlled: human-subjects data; release only under approved access agreement"
 },
 {
  "path": "results/mc_summary.json",
  "sha256": "7bde71d2f02e64ad",
  "tier": "T0-public"
 }
]
public files: 3 of 5
```

Duas escolhas de desenho merecem atenção. Primeiro, as regras são **ordenadas** e a primeira correspondência vence: se a regra "synthetic" fosse colocada antes da regra "partner", um arquivo chamado `synthetic_partner_feeders.csv` seria publicado. Ordene primeiro as regras mais restritivas. Segundo, um arquivo sem correspondência retorna **"UNCLASSIFIED: stop and review"** em vez de um nível padrão; um pipeline de liberação deve falhar fechado. Pipelines reais também examinariam o *conteúdo* dos arquivos (coordenadas, identificadores de ativos, nomes), e não apenas os caminhos.

### 7.5 Dados sintéticos: inventados versus calibrados

As regiões deste livro são **inventadas**: seus números foram escolhidos para ensinar e não correspondem a nenhum lugar. Uma tese baseada num parceiro real mais provavelmente produziria dados sintéticos **calibrados** — gerados para corresponder às propriedades estatísticas dos dados reais. A calibração preserva o valor de pesquisa e também preserva parte do risco de divulgação: se a região real tem um único hospital num alimentador pequeno com uma estação de água de reserva curta, uma região sintética calibrada que preserve essas relações ainda pode apontar para ela. Avalie o risco residual explicitamente: uma pessoa informada conseguiria associar a configuração sintética a uma real? Essa associação revelaria algo que ainda não é público? Generalizar (faixas em vez de valores), perturbar e misturar várias configurações reais reduzem o risco; a avaliação e as medidas escolhidas pertencem à documentação do arquivo.

### 7.6 Documentando modelos, dados e estudos

- **Modelos.** Para componentes baseados em agentes, o protocolo ODD — overview, design concepts, details (visão geral, conceitos de desenho, detalhes) — dá uma estrutura padrão ([Grimm et al., 2006](https://doi.org/10.1016/j.ecolmodel.2006.04.023)). Para qualquer simulador, documente o propósito, as entidades e as variáveis de estado, os processos e o escalonamento, os insumos e suas fontes, os testes de verificação e as limitações conhecidas.
- **Conjuntos de dados.** As datasheets registram a motivação, a composição, o processo de coleta, o pré-processamento, os usos, a distribuição e a manutenção ([Gebru et al., 2021](https://doi.org/10.1145/3458723)).
- **Componentes aprendidos.** Se o estudo incluir um modelo aprendido (por exemplo, um detector), um model card registra o uso pretendido, as condições de avaliação e as limitações ([Mitchell et al., 2019](https://doi.org/10.1145/3287560.3287596)).
- **Computação.** Fixe as versões da linguagem e das bibliotecas, registre as sementes, forneça um único comando que regenere todas as tabelas e figuras e inclua os testes de verificação. [Sandve et al. (2013)](https://doi.org/10.1371/journal.pcbi.1003285) dão dez regras práticas.

### 7.7 Escrevendo as limitações

Uma seção de limitações faz parte do argumento: ela declara as condições de refutação e sua direção provável. Seções de limitações fracas listam ressalvas genéricas ("mais pesquisas são necessárias"). As fortes dizem, para cada limitação, *o que* ela é, *como* poderia mudar o resultado e *em que direção*, e *que estudo* a resolveria. Para o Cascade Study:

| Limitação | Efeito possível | Direção | Estudo que a resolve |
|---|---|---|---|
| Reservas humanas (água por caminhão, entregas de combustível, alívio de carga) omitidas | O modelo exagera a consequência de todas as ordenações e o benefício da reordenação | Rumo a um benefício menor | Modelar a extensão das reservas como condicionada às telecomunicações e às estradas; validar contra os registros pós-ação |
| Tempo de deslocamento entre os alimentadores omitido | Ordenações que saltam entre alimentadores distantes custam mais do que o modelado | Rumo a um benefício menor de DEP quando os alimentadores críticos estão dispersos | Acrescentar uma matriz de tempos de deslocamento; reexecutar |
| Apenas regiões sintéticas | Frequência da divergência nas regiões reais desconhecida | Desconhecida | Levantamento com concessionárias medindo a divergência, sob proteção T3 |
| Pesos de um único painel | Os vereditos mudam com os pesos (EX034) | Qualquer uma | Vários painéis; relatar os vereditos por conjunto de pesos |
| Amostra do exercício de mesa de 12 pessoas de 3 concessionárias | Evidências de adoção fracas | Rumo a um exagero da adotabilidade | Estudo maior e estratificado; piloto de campo durante exercícios |
| Classe de cenários cibernéticos limitada a quedas na distribuição que exigem restauração manual | Não cobre ataques às ferramentas de restauração nem aos dados de prioridade | Desconhecida | Família de cenários incluindo ataques à integridade dos dados de planejamento (motivada por §6.6) |

### 7.8 Exemplo resolvido: montando o arquivo

O primeiro plano de arquivo do candidato colocava tudo em T2 "por segurança". A banca o rejeitou: a restrição excessiva impede a verificação e não é segura, apenas irresponsável. O plano revisado usou a tabela de níveis de §7.4.2, publicou todo o código e as configurações sintéticas em T0 com um único comando de regeneração, colocou as transcrições do exercício de mesa em T2 sob os termos de consentimento que os participantes assinaram e registrou o material T3 dos parceiros numa descrição que dizia aos examinadores exatamente quais análises dependiam dele — nenhum dos resultados confirmatórios dependia, por desenho, porque o estudo usou regiões inventadas para todas as alegações públicas e usou os dados dos parceiros apenas para as faixas de elicitação e a validade aparente. Essa decisão de desenho, tomada no Capítulo 1, é o que tornou possível um arquivo em grande parte público.

### 7.9 Erros comuns e limites

- Escrever a tese como um caderno de laboratório cronológico em vez de um argumento.
- Restringir tudo, ou publicar tudo, em vez de usar níveis.
- Igualar FAIR a aberto.
- Tratar os dados sintéticos calibrados como automaticamente seguros.
- Scripts de liberação que falham abertos.
- Seções de limitações sem direção nem estudos que as resolvam.

- Colocar tudo num nível restritivo por segurança, o que impede a verificação e torna o trabalho irresponsável, e não seguro.
- Ordenar as regras de liberação de modo que um padrão permissivo como synthetic corresponda antes de um restritivo como partner.
- Classificar os arquivos apenas pelo nome, sem examinar o conteúdo em busca de coordenadas, identificadores de ativos ou nomes.
- Deixar que os resultados confirmatórios dependam de material retido dos parceiros, de modo que os examinadores não possam verificá-los.
- Omitir um único comando que regenere todas as tabelas e figuras a partir dos arquivos públicos.

### Exercícios — capítulo 7

**EX039 — Mapa do argumento.** *Objetivo:* expor o argumento da tese. *Insumos:* a alegação estreitada de §6.5. *Restrições:* usar os seis elementos de Toulmin. *Passos:* (1) mapear a alegação; (2) marcar qual capítulo da tese fornece cada elemento; (3) identificar a garantia mais fraca e a evidência que a fortaleceria. *Evidência esperada:* mapa e parágrafo. *Rubrica:* 3 = mapa completo, garantia mais fraca corretamente identificada (adequação do modelo para regiões reais, ou reservas humanas omitidas) com um estudo de fortalecimento específico; 2 = um elemento ralo; 1 = apenas alegação e dados; 0 = nada.

**EX040 — Atribuição de níveis.** *Objetivo:* atribuir níveis a um arquivo realista. *Insumos:* dez artefatos: código do simulador; testes de verificação; configuração de Riverbend; formulários de elicitação com os nomes dos parceiros; faixas de elicitação agregadas; áudio do exercício de mesa; justificativas codificadas; formulários de consentimento; o procedimento de restauração de um parceiro; figuras finais. *Restrições:* usar os quatro níveis; justificar cada um. *Passos:* (1) atribuir um nível a cada artefato; (2) justificar o nível numa linha; (3) propor uma transformação que levaria cada item restrito a um nível mais aberto. *Evidência esperada:* tabela. *Rubrica:* 3 = níveis sensatos (código, testes, configurações e figuras T0; faixas agregadas T1; justificativas codificadas T2, ou T1 se desidentificadas; áudio, formulários de consentimento e formulários de elicitação nomeados T2 ou T3; procedimento do parceiro T3) com transformações; 2 = um ou dois mal avaliados; 1 = níveis uniformes; 0 = nada.

**EX041 — Manifesto que falha fechado.** *Objetivo:* melhorar o Laboratório 7. *Insumos:* Laboratório 7. *Restrições:* off-line. *Passos:* (1) acrescentar um arquivo `data/synthetic_partner_feeders.csv`; (2) mostrar que a ordem atual das regras o classifica corretamente e explicar por quê; (3) mover a regra `synthetic_` para o início, reexecutar e registrar a falha; (4) acrescentar uma verificação de conteúdo que recuse o nível público para qualquer arquivo que contenha a cadeia `SUB-`. *Evidência esperada:* código, saídas, explicação. *Rubrica:* 3 = demonstra o risco da ordenação, a verificação de conteúdo funciona, a explicação se liga ao desenho que falha fechado; 2 = parcial; 1 = não executado; 0 = nada.

**EX042 — Avaliação da divulgação residual.** *Objetivo:* avaliar dados sintéticos calibrados. *Insumos:* uma região sintética calibrada a um condado real com um hospital, duas estações de água e cinco alimentadores, preservando qual alimentador abriga o hospital. *Restrições:* usar as perguntas de §7.5. *Passos:* (1) avaliar o risco de reidentificação; (2) avaliar o que uma associação revelaria; (3) propor transformações e avaliar seu custo para o valor de pesquisa. *Evidência esperada:* avaliação de uma página. *Rubrica:* 3 = reconhece a reidentificação pela estrutura única, propõe mistura ou generalização, pondera o valor de pesquisa com honestidade; 2 = avaliação rasa; 1 = declara o sintético seguro; 0 = nada.

**EX043 — Documentação do modelo.** *Objetivo:* documentar o simulador do Laboratório 5. *Insumos:* código do Laboratório 5. *Restrições:* seguir os elementos de modelo de §7.6; no máximo duas páginas. *Passos:* (1) escrever o propósito, as entidades, os processos e o escalonamento; (2) listar os insumos e suas fontes; (3) listar os testes de verificação; (4) listar as limitações conhecidas, incluindo pelo menos três de §7.7. *Evidência esperada:* documento. *Rubrica:* 3 = fiel ao código (intervalos baseados em eventos, atraso de reinício, atribuição das equipes, semântica de OU para as dependências), limitações específicas; 2 = pequenas imprecisões; 1 = genérico; 0 = nada.

**EX044 — Seção de limitações.** *Objetivo:* escrever limitações que informem. *Insumos:* seu próprio estudo ou o Cascade Study. *Restrições:* pelo menos cinco limitações, cada uma com efeito, direção e estudo que a resolva. *Passos:* (1) listar as limitações; (2) declarar o efeito e a direção de cada uma; (3) nomear o estudo que resolveria cada uma; (4) classificá-las por quanto poderiam mudar a alegação principal. *Evidência esperada:* tabela e parágrafo de classificação. *Rubrica:* 3 = específicas, direcionais, com estudos que as resolvam e uma classificação justificada; 2 = faltam direções em algumas; 1 = ressalvas genéricas; 0 = nada.

### Síntese do capítulo

A tese é um argumento: alegação, dados, garantia, respaldo, qualificador e refutações, cada um fornecido por uma parte identificável do trabalho. A pesquisa sobre infraestrutura precisa conciliar a reprodutibilidade com a proteção da infraestrutura estudada e das pessoas envolvidas; os arquivos em níveis com manifestos com hash fazem isso, e os princípios FAIR descrevem o acesso sem implicar abertura. As ferramentas de liberação devem falhar fechadas e verificar o conteúdo, e não apenas os nomes. Os dados sintéticos inventados trazem pouco risco de divulgação; os dados sintéticos calibrados precisam de uma avaliação explícita do risco residual. Documente os modelos, os dados e a computação com estruturas reconhecidas. As limitações declaram a direção e os estudos que as resolvem, o que as transforma na próxima agenda de pesquisa.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 08

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Defesa e plano de publicação

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Auditar o registro de alegações de uma tese em busca de alegações sem apoio, sem escopo e generalizadas em excesso antes da defesa.
2. Preparar-se para uma defesa antecipando as perguntas mais fortes dos examinadores e respondendo com evidências, escopo e limites.
3. Planejar uma sequência de publicações em diferentes comunidades que preserve a integridade do argumento geral.
4. Integrar a divulgação coordenada e a coordenação setorial ao cronograma de publicação quando as constatações tocarem em vulnerabilidades ou superfícies de ataque.
5. Traduzir uma alegação de pesquisa estreitada em recomendações de política e de prática sem inflá-la.
6. Transformar as limitações da tese num programa de pesquisa de pós-doutorado crível.

O Capítulo 7 montou a tese e seu arquivo. Este capítulo prepara o candidato para defendê-la e liberá-la de forma responsável — o passo final do livro e da trilha de estudos de 207 cursos.

### 8.1 A auditoria das alegações

Antes da defesa, toda alegação da tese — no resumo, na introdução, nas conclusões dos capítulos e na conclusão geral — entra num **registro de alegações** com suas evidências, seu escopo e suas limitações. Os resumos e as conclusões são onde o exagero se acumula, porque são escritos por último, com pressa, em busca de impacto.

#### 8.1.1 Atividade prática: uma primeira passada automatizada

```python
# Lab 8 - audit a thesis claim register before the defense (offline)
claims = [
    {"id": "K1", "text": "Dependency-aware restoration reduced weighted critical-service loss in the Riverbend model",
     "evidence": ["Ch5-MC"], "scope": "synthetic model, single crew, 4 feeders", "limits": ["model-policy circularity"], "status": "supported"},
    {"id": "K2", "text": "The benefit persists when generator fuel buffers double",
     "evidence": ["Ch6-boundary"], "scope": "gen_scale 2-4", "limits": [], "status": "supported"},
    {"id": "K3", "text": "Operators would adopt the dependency-aware ordering",
     "evidence": [], "scope": "", "limits": [], "status": "supported"},
    {"id": "K4", "text": "Dependency-aware restoration improves resilience of US utilities",
     "evidence": ["Ch5-MC", "Ch6-PortHalvard"], "scope": "two synthetic regions", "limits": ["no field data"], "status": "supported"},
]
OVERREACH = ("US utilities", "all utilities", "proves", "always")
for c in claims:
    problems = []
    if c["status"] == "supported" and not c["evidence"]:
        problems.append("no evidence for a supported claim")
    if not c["scope"]:
        problems.append("scope missing")
    if not c["limits"]:
        problems.append("no stated limitation")
    if any(w in c["text"] for w in OVERREACH) and "synthetic" in c["scope"]:
        problems.append("text generalizes beyond its synthetic scope")
    print(c["id"], "OK" if not problems else "; ".join(problems))
```

Saída esperada:

```text
K1 OK
K2 no stated limitation
K3 no evidence for a supported claim; scope missing; no stated limitation
K4 text generalizes beyond its synthetic scope
```

O script detecta três falhas clássicas. K2 está sustentada, mas não declara nenhuma limitação — e, no entanto, o Capítulo 6 mostrou que o benefício sobre SILO encolhe fortemente à medida que as reservas crescem, então "persiste quando as reservas dobram" precisa do qualificador de que o benefício cai cerca de 85% com o dobro das reservas. K3 está marcada como sustentada sem nenhuma evidência: o exercício de mesa mostrou que uma exibição *pode deslocar escolhas num exercício de mesa*, o que não é adoção. K4 generaliza de duas regiões sintéticas para "US utilities". Um filtro por palavras-chave é tosco — ele deixaria passar "nationwide" ou "the grid" —, então o script é uma primeira passada; a auditoria decisiva é uma pessoa lendo cada alegação contra o registro.

#### 8.1.2 Alegações corrigidas

| ID | Texto corrigido |
|---|---|
| K1 | No modelo sintético de Riverbend, todas as ordenações cientes da criticidade reduziram a perda ponderada de serviços críticos em cerca de 90% em relação à ordenação pelos clientes, com cerca de 70% a mais de clientes-hora; a ordenação pelo tempo até o impacto não melhorou a ordenação por sinalização crítica ali. |
| K2 | A vantagem da ordenação ciente da criticidade sobre a ordenação pelos clientes caiu cerca de 85% quando as reservas foram dobradas e desapareceu com quatro vezes as reservas obtidas. |
| K3 | Num exercício de mesa com doze participantes de três concessionárias sintéticas, uma exibição do tempo até o impacto deslocou as ordenações escolhidas por sete participantes em direção à ordenação de menor consequência; a adoção na prática não foi estudada. |
| K4 | Em duas regiões sintéticas e 200 regiões geradas, a ordenação pelo tempo até o impacto melhorou a ordenação por sinalização crítica apenas onde suas ordens divergiam; com que frequência isso ocorre nas regiões reais é desconhecido. |

### 8.2 Preparando a defesa

#### 8.2.1 O que os examinadores testam

Os examinadores testam se o candidato é um pesquisador independente: se ele entende os limites da sua contribuição melhor do que ninguém, se consegue defender as escolhas de desenho contra as alternativas e se conhece a literatura bem o bastante para situar o trabalho. Espere perguntas de seis famílias:

| Família | Exemplo de pergunta para o Cascade Study | O que uma resposta forte contém |
|---|---|---|
| Contribuição | "O que há de novo aqui, considerando que as concessionárias já mantêm listas de clientes críticos?" | A alegação estreitada; as condições sob as quais a temporização agrega valor; as pré-condições mensuráveis (divergência, acurácia do mapa); o enquadramento pela teoria de programação. |
| Desenho | "Por que simulação e exercício de mesa em vez de um estudo de campo?" | Segurança e ética (nunca testar em produção); raridade dos eventos reais; o uso da validação histórica; o que um piloto de campo durante exercícios acrescentaria em seguida. |
| Validade | "O resultado não é circular?" | O teste de descompasso; modelador independente para Port Halvard; a análise do gerador; o que continua circular. |
| Valores | "Quem decidiu que os hospitais importam cinco vezes mais do que uma central de telecomunicações, e por que alguém deveria aceitar isso?" | O processo de elicitação, o painel, a data, a sensibilidade dos vereditos aos pesos (EX034), a declaração explícita de que os pesos são uma escolha de política. |
| Ética e duplo uso | "Vocês acabaram de dizer aos adversários que ataquem os dados de prioridade de restauração?" | A revisão de duplo uso; publicação em nível geral; recomendação defensiva; coordenação antes da publicação. |
| Conhecimento da área | "Como seu trabalho se relaciona com as abordagens de engenharia orientadas pela consequência?" | A lógica de consequência primeiro do CCE; a tese como contribuição para o lado da *recuperação*; diferenças na unidade de análise. |

#### 8.2.2 Defesas simuladas

Faça pelo menos duas defesas simuladas: uma com especialistas amigáveis do domínio e uma com um metodologista hostil de fora dele. Registre as perguntas que você não conseguiu responder bem; cada uma é uma lacuna na tese (corrija-a), uma lacuna na sua preparação (estude-a) ou uma pergunta genuinamente em aberto (diga isso na defesa — "não sei, e é assim que eu descobriria" é uma resposta forte).

#### 8.2.3 Respondendo

Responda à pergunta feita, depois apresente as evidências, depois declare o limite. Evite três hábitos: defender uma alegação mais forte do que a tese faz; conceder, por nervosismo, um ponto que a tese de fato trata; e preencher o silêncio com especulação. Quando um examinador propuser uma explicação alternativa que você não testou, a melhor resposta descreve o teste que a distinguiria e o que cada desfecho significaria.

### 8.3 Plano de publicação

#### 8.3.1 Sequenciando os artigos

O Cascade Study se divide naturalmente em artigos para comunidades diferentes:

1. **Artigo de métodos/PO.** A ordenação da restauração sob serviços críticos limitados por reservas: o enquadramento pela programação, o limite oráculo, a heurística e seus modos de falha, a análise de 200 regiões. Público: veículos de confiabilidade, risco e pesquisa operacional.
2. **Artigo de segurança de infraestrutura.** A integridade do mapa de dependências como pré-condição da restauração ciente da criticidade, com os resultados de descompasso e a recomendação defensiva revisada quanto ao duplo uso. Público: veículos de proteção de infraestrutura crítica e workshops de segurança de CPS.
3. **Artigo de fatores humanos.** O estudo de exercício de mesa: exibição, escolhas, justificativas e variáveis omitidas. Público: fatores humanos e gestão de emergências.
4. **Nota de replicação.** A reprodução do GridWater-Sim após a correção de uma ambiguidade na ordem dos parâmetros, com os testes de verificação. Público: a comunidade do benchmark; também valiosa como artigo de dados ou de software.

Publique os componentes T0 do arquivo com identificadores persistentes junto com o primeiro artigo, para que os artigos seguintes citem os mesmos artefatos versionados. Cada artigo precisa declarar o escopo da alegação geral e não deve citar outro artigo da tese como evidência mais forte do que ele é.

#### 8.3.2 Preprints, embargos e resultados sensíveis

Os preprints aceleram o retorno e estabelecem a prioridade. Para resultados que tocam superfícies de ataque, decida *antes* do preprint se a coordenação é necessária (§8.4); um preprint é uma publicação. Financiadores e parceiros podem ter prazos de aviso em seus acordos (Capítulo 1, §1.5.3); respeite-os, e recuse qualquer pedido que equivalha a um veto sobre as constatações.

### 8.4 Divulgação coordenada e coordenação setorial

A pesquisa sobre infraestrutura pode produzir três tipos de constatação sensível, cada um com sua própria via:

| Constatação | Exemplo | Via |
|---|---|---|
| Uma vulnerabilidade de produto | Uma falha no software de gestão de interrupções de um fornecedor encontrada durante a construção do simulador | Divulgação coordenada de vulnerabilidades ao fornecedor, diretamente ou por meio de um coordenador como o [programa de CVD da CISA](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program); a prática internacional é descrita na ISO/IEC 29147 (divulgação) e na ISO/IEC 30111 (tratamento). |
| Uma fraqueza específica de uma organização | A lista de clientes críticos de um parceiro tem atribuições de alimentador erradas | Relato privado ao parceiro, sob o acordo de uso de dados; nunca publicado de forma identificável. |
| Uma superfície de ataque em nível setorial | Os dados de prioridade de restauração e os mapas de dependências são alvos de alto valor cuja corrupção amplifica as quedas | Coordenar com os parceiros e, quando apropriado, com a organização setorial de compartilhamento de informações pertinente antes da publicação; publicar em nível geral, com recomendações defensivas. |

Inclua o período de coordenação no cronograma. A CISA descreve seu processo como abrangendo o contato com o fornecedor, a análise, a coordenação da remediação e a publicação do alerta, e observa que pode divulgar após um período se o fornecedor não responder; leia a política atual em vez de confiar num resumo. A tese registra o que foi divulgado, a quem, quando e o que foi retido.

### 8.5 Traduzindo para a política e a prática

Os públicos de políticas precisam de recomendações que decorram das evidências e digam quão confiantes elas são. A partir da alegação estreitada do Cascade Study, as recomendações defensáveis são:

1. **Explicitar a troca.** Priorizar os serviços críticos na restauração custa aos clientes comuns tempo sem energia; o tamanho desse custo deve ser estimado e discutido nos planos de emergência e, quando apropriado, em consulta pública. (Evidência forte dentro do modelo; a direção é um resultado da teoria de programação.)
2. **Auditar os mapas de dependências.** A restauração ciente da criticidade só é tão boa quanto o mapa alimentador–instalação e os dados das reservas por trás dela; as concessionárias e seus parceiros devem verificá-los regularmente. (Evidência forte de fragilidade dentro do modelo.)
3. **Proteger os dados de prioridade de restauração.** Trate as listas de clientes críticos, os mapas de dependências e os estoques das reservas como sensíveis e críticos quanto à integridade. (Inferência a partir dos resultados de descompasso e dos relatos públicos de ameaças; confiança moderada.)
4. **Medir a divergência antes de mudar a prática.** Uma concessionária pode determinar se a ordenação pelo tempo até o impacto mudaria a ordem atual da sua lista crítica; se não mudar, ela nada ganha ao adotá-la. (Condicionada ao modelo; baixo custo de verificação.)

Essas recomendações se encaixam naturalmente em processos de gestão de riscos que já existem — a gestão de riscos setoriais sob o NSM-22 nos Estados Unidos, as avaliações de risco das entidades críticas sob a Diretiva CER na UE —, sem alegar que qualquer autoridade deva torná-las obrigatórias. Um policy brief tem duas páginas, declara sua base de evidências e seus limites e traz links para a tese e o arquivo.

### 8.6 O programa de pós-doutorado

A tabela de limitações do Capítulo 7 é uma agenda de pesquisa. Um programa crível de três estudos:

1. **Levantamento da divergência em regiões reais** (empírico, protegido): medir, sob proteção T3, com que frequência as ordens pelo tempo até o impacto e pela lista crítica divergem numa amostra de concessionárias. Isso responde à pergunta que os geradores sintéticos não conseguiram responder.
2. **Modelagem das reservas humanas** (modelo + validação): representar a extensão das reservas (entregas de combustível, água por caminhão) como condicionada ao acesso às telecomunicações e às estradas, validar contra os registros pós-ação e testar de novo as alegações sobre a restauração.
3. **Ataques à integridade dos dados de planejamento** (segurança + simulação): modelar a corrupção adversarial dos mapas de dependências e das listas de prioridade, avaliar estratégias de detecção e auditoria e estimar seu valor quanto à consequência — uma continuação direta da constatação de duplo uso, conduzida com parceiros setoriais.

Cada estudo tem uma alegação falseável, um desenho seguro e um modelo de parceria, e cada um mudaria uma decisão que alguém toma.

### 8.7 Exemplo resolvido: uma troca na defesa (sintética)

*Examinador:* "Sua região de Port Halvard foi desenhada para fazer seu método vencer. Por que eu deveria acreditar em qualquer coisa além de Riverbend, onde ele falhou?"

*Candidato:* "O senhor tem razão em que Port Halvard foi selecionada para que o mecanismo pudesse operar; os critérios de seleção foram pré-registrados antes da simulação, e outro modelador a construiu, mas ela é um teste do mecanismo, e não uma estimativa de com que frequência o método ajuda. É por isso que executei a análise de 200 regiões, em que o ganho sobre a ordenação por sinalização é exatamente zero sempre que as duas ordens coincidem e cresce com a divergência, e é por isso que a tese nada alega sobre com que frequência a divergência ocorre nas regiões reais. A falha em Riverbend faz parte da alegação: ela mostra que o método nada acrescenta onde as ordens coincidem ou onde os pesos e o espalhamento favorecem outra ordem. Se o senhor quiser uma estimativa para concessionárias reais, o estudo que eu executaria primeiro é o levantamento da divergência que descrevo na conclusão."

A resposta concede o que é verdadeiro, cita as evidências específicas, reafirma a alegação estreitada e nomeia o próximo estudo. Ela não defende a alegação original, mais ampla.

### 8.8 Erros comuns e limites

- Resumos e conclusões que alegam mais do que os capítulos.
- Tratar a defesa como uma apresentação em vez de um exame da independência.
- Publicar artigos cujas alegações se desviam para além do escopo da tese.
- Postar preprints antes de decidir se a coordenação é necessária.
- Recomendações de política sem níveis de confiança nem links para as evidências.
- Planos de pós-doutorado que repetem a tese em vez de tratar suas limitações.

- Manter um registro de alegações, mas auditá-lo apenas por palavras-chave, o que deixa passar exageros formulados como nationwide ou the grid.
- Responder à explicação alternativa de um examinador defendendo a alegação original em vez de descrever o teste que as distinguiria.
- Postar o artigo de segurança de infraestrutura antes que os parceiros e o órgão setorial de compartilhamento de informações tenham sido consultados sobre a constatação da integridade do mapa.
- Citar um artigo da tese, no artigo seguinte, como evidência mais forte do que ele é.
- Escrever recomendações de política que impliquem uma obrigatoriedade que as evidências não sustentam.

### Exercícios — capítulo 8

**EX045 — Auditoria das alegações.** *Objetivo:* auditar um registro de alegações. *Insumos:* Laboratório 8. *Restrições:* off-line. *Passos:* (1) executar o laboratório e registrar a saída; (2) acrescentar uma alegação K5, "Our method makes the grid resilient to cyber attacks", com evidência `["Ch5-MC"]`, escopo "synthetic model" e limites `["no field data"]`; (3) mostrar que o script não a detecta; (4) melhorar a verificação e reexecutar; (5) escrever o texto corrigido de K5. *Evidência esperada:* código, saídas, alegação corrigida. *Rubrica:* 3 = demonstra a falha de detecção, uma verificação melhorada sensata (por exemplo, termos como "the grid" ou "resilient to" combinados com o escopo sintético), alegação corrigida devidamente delimitada; 2 = verificação melhorada, mas a alegação continua inflada; 1 = não executado; 0 = nada.

**EX046 — Banco de perguntas dos examinadores.** *Objetivo:* preparar-se para a defesa. *Insumos:* sua tese ou o Cascade Study. *Restrições:* pelo menos duas perguntas em cada uma das seis famílias de §8.2.1; uma resposta-modelo de no máximo 120 palavras para as três mais difíceis. *Passos:* (1) escrever pelo menos duas perguntas em cada família; (2) marcar as três mais difíceis; (3) redigir uma resposta-modelo de no máximo 120 palavras para cada uma; (4) identificar qualquer pergunta que revele uma lacuna na tese, e não na sua preparação. *Evidência esperada:* banco de perguntas e respostas. *Rubrica:* 3 = perguntas afiadas e específicas, respostas que seguem o padrão pergunta–evidência–limite, pelo menos uma lacuna real identificada; 2 = respostas defensivas; 1 = perguntas genéricas; 0 = nada.

**EX047 — Plano de publicação.** *Objetivo:* sequenciar os artigos com integridade. *Insumos:* o Cascade Study ou a sua tese. *Restrições:* de três a cinco artigos; público, alegação e evidências de cada um; versionamento do arquivo; pontos de verificação de coordenação. *Passos:* (1) listar os artigos com seus públicos; (2) declarar a alegação de cada artigo e as evidências que ele usa; (3) mapear os artefatos compartilhados e suas versões; (4) marcar onde a coordenação ou a revisão de duplo uso precisa acontecer antes da liberação. *Evidência esperada:* plano com cronograma. *Rubrica:* 3 = artigos distintos e sem sobreposição de alegações, artefatos compartilhados versionados, coordenação posicionada antes de qualquer preprint que toque superfícies de ataque; 2 = sobreposições ou pontos de verificação ausentes; 1 = apenas uma lista de títulos; 0 = nada.

**EX048 — Encaminhamento da divulgação.** *Objetivo:* encaminhar constatações sensíveis. *Insumos:* quatro constatações sintéticas: (a) a concessionária parceira do simulador exporta sua lista de clientes críticos para uma página web interna sem autenticação; (b) um produto comercial de gestão de interrupções aceita importações de configuração não assinadas; (c) em três parceiros, os estoques das reservas no papel excedem os estoques físicos em 20–40%; (d) os procedimentos de rádio das equipes de restauração dependem de um único site repetidor. *Restrições:* vias de §8.4; declarar a temporização e o que é publicado. *Passos:* (1) classificar cada constatação por tipo; (2) escolher a via; (3) declarar quem é notificado e quando; (4) declarar o que acaba sendo publicado e em que nível. *Evidência esperada:* tabela. *Rubrica:* 3 = (a) relato privado ao parceiro, (b) CVD com o fornecedor ou um coordenador, (c) relatos privados mais a publicação geral da lacuna entre os estoques no papel e os físicos, (d) relato privado e uma constatação geral sobre pontos únicos de falha nas comunicações de restauração, com temporização sólida; 2 = um mal encaminhado; 1 = dois ou mais; 0 = nada.

**EX049 — Policy brief.** *Objetivo:* traduzir sem inflar. *Insumos:* a alegação estreitada de §6.5 e as recomendações de §8.5. *Restrições:* duas páginas; nível de confiança e link para as evidências em toda recomendação; um parágrafo sobre o que a pesquisa não mostra. *Passos:* (1) escrever o brief; (2) marcar cada frase como evidência, inferência ou recomendação; (3) remover qualquer frase que não possa ser rastreada até a tese. *Evidência esperada:* brief com as marcações. *Rubrica:* 3 = recomendações rastreáveis e qualificadas, não constatações explícitas, linguagem acessível; 2 = algumas frases não rastreáveis; 1 = advocacia sem evidências; 0 = nada.

**EX050 — Programa de pesquisa de pós-doutorado.** *Objetivo:* converter as limitações em pesquisa. *Insumos:* sua tabela de limitações do EX044 ou §7.7. *Restrições:* três estudos; cada um com uma alegação falseável, um desenho seguro, um modelo de parceria e a decisão que ele mudaria. *Passos:* (1) escolher três limitações; (2) desenhar um estudo para cada uma; (3) ordenar os estudos por dependência e valor; (4) declarar que resultado encerraria o programa. *Evidência esperada:* programa de duas páginas. *Rubrica:* 3 = os estudos tratam diretamente das limitações de maior consequência, são falseáveis e seguros e estão ordenados por dependência, com um resultado de parada honesto; 2 = um estudo fraco; 1 = repete a tese; 0 = nada.

### Síntese do capítulo

A defesa examina a independência: o candidato precisa conhecer os limites da contribuição melhor do que ninguém. Um registro de alegações, auditado por script e por leitura, remove os exageros que se acumulam nos resumos e nas conclusões. As perguntas dos examinadores se enquadram em famílias previsíveis; responda com evidências e limites, e nomeie o estudo que resolveria o que você não sabe. Publique em sequência, em diferentes comunidades, com artefatos compartilhados versionados, e decida sobre a coordenação antes que qualquer preprint toque uma superfície de ataque. Encaminhe de formas diferentes as vulnerabilidades, as fraquezas específicas de organizações e as superfícies de ataque em nível setorial. Traduza as alegações estreitadas em recomendações com níveis de confiança. As limitações se tornam o próximo programa de pesquisa — o fim natural de um curso de doutorado e desta trilha de estudos.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 08

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável e explica o que a rubrica recompensa. Respostas alternativas podem receber a pontuação máxima quando atendem ao mesmo padrão de evidências, escopo e honestidade sobre os limites. Os resultados numéricos vêm dos laboratórios offline deste livro, executados com a biblioteca padrão do Python 3; se sua saída for diferente, confira primeiro a versão do Python, a semente e se você mudou a ordem dos sorteios aleatórios.

### Capítulo 1: EX001–EX007

**EX001 — Auditoria pela escada de alegações.**

| # | Asserção | Degrau | Pressuposto oculto | Observação que a derrota |
|---|---|---|---|---|
| 1 | Os logs mostram um acesso ao sistema de gestão da distribuição (DMS) às 01:52. | L1 se o log estiver preservado com o estado do relógio; caso contrário, L2 | A fonte do log está íntegra e seu relógio está correto; "atacante" já é uma inferência | O log mostra uma sessão agendada de fornecedor; desvio do relógio |
| 2 | O acesso foi feito por um atacante. | L2 | A sessão não era autorizada | A sessão corresponde a um chamado de manutenção autorizado |
| 3 | O acesso causou a queda. | L3, alegação causal de caso | Comandos foram emitidos e o alimentador abriu por causa deles, e não pela proteção | Os registros dos relés mostram um desarme da proteção; nenhum comando nos logs do DMS |
| 4 | O hospital perdeu energia. | L4, consequência | O gerador do hospital não partiu ou ficou sem combustível | Os logs do gerador mostram uma transferência sem interrupção |
| 5 | Pacientes foram postos em perigo. | L4, consequência, forte | Os serviços clínicos foram afetados | O hospital não relata nenhuma mudança nos serviços |
| 6 | As cooperativas rurais são o ponto mais fraco da rede elétrica. | L5, alegação de pesquisa a partir de um único caso | Um caso representa uma população; comparação com outros tipos de concessionária | Qualquer comparação de taxa-base |

Reescrita: "Neste caso sintético, o DMS registrou às 01:52 (relógio do DMS) uma sessão cuja autorização ainda não foi estabelecida. Um alimentador que atende o hospital abriu em algum momento depois disso; não foi estabelecido se um comando causou a abertura, nem se o hospital perdeu energia em vez de transferir para seu gerador. Nenhuma conclusão sobre as cooperativas em geral decorre de um único caso." A pontuação máxima exige sinalizar a reserva do gerador (a razão mais provável para a alegação de consequência ser falsa) e a generalização.

**EX002 — Definição e população.** Uma resposta defensável cita: a definição legal usada pela política norte-americana (42 U.S.C. § 5195c(e)) e a estrutura setorial do NSM-22 pela página da CISA; as definições do artigo 2º da CER de "entidade crítica" e seu anexo de setores; o artigo 3º da NIS2, com os anexos I e II (entidades essenciais e importantes). Classificação típica: o hospital regional pertence ao setor norte-americano Healthcare and Public Health, é provavelmente uma entidade da NIS2 no setor da saúde, dependendo do porte e das regras nacionais, e só pode ser designado entidade crítica pela CER se o Estado-Membro o identificar; a pequena concessionária de água pertence ao setor norte-americano Water, pode ficar abaixo dos limiares de porte da NIS2, a menos que um Estado-Membro lhe aplique as regras, e pertence ao setor de água potável da CER se for designada; o processador de pagamentos pertence ao setor norte-americano Financial Services, está sujeito na UE às regras do setor financeiro (a NIS2 contém disposições de lex specialis em relação a atos setoriais como o DORA) e aos setores bancário ou de infraestruturas do mercado financeiro da CER, se designado. Consequência de desenho: uma comparação entre jurisdições precisa definir sua população por um critério funcional comum (por exemplo, população atendida e função), e não por categoria jurídica, e relatar a situação jurídica de cada unidade como covariável. A rubrica recompensa citações exatas e trata os casos que dependem de designação como condicionais, e não como certos.

**EX003 — Tipificação das interdependências.**

| Relação | Tipo | Justificativa |
|---|---|---|
| TEL de F2 | Física | A eletricidade é um insumo material |
| HOSP de F2 | Física | Idem |
| HOSP de WATER | Física | A água é um insumo material |
| WATER de F3 | Física | Idem |
| SCADA da água de TEL | Cibernética | Dependência de informações transportadas pela rede de telecomunicações |
| Faturamento do processador de pagamentos | Lógica (ou cibernética) | Mecanismo financeiro e contratual; afeta as operações apenas ao longo de dias, e não a entrega do serviço |
| Combustível dos geradores do acesso rodoviário | Física, com um componente geográfico se estradas e alimentadores compartilharem perigos | O combustível é um insumo material; o acesso pode falhar pelo mesmo evento local |

Não existe ciclo entre os serviços listados (nenhum serviço da lista depende de volta de HOSP, WATER ou TEL). Um modelo puro de fluxo de potência omitiria a dependência combustível–estrada, a dependência do faturamento e a dependência do SCADA da água em relação a TEL. A pontuação máxima observa que a ausência de ciclo é uma propriedade desta lista, e não da região: as telecomunicações muitas vezes precisam de água para refrigeração, e as concessionárias de energia precisam das telecomunicações para a restauração, o que criaria ciclos.

**EX004 — Análise pelo Menlo.** Partes interessadas: os despachantes entrevistados; os gestores de emergência no exercício de mesa; a REC, a RWA, o hospital e a operadora como organizações; a população atendida; os reguladores; o financiador; a equipe de pesquisa. Princípio por princípio: *respeito às pessoas* — consentimento individual separado da permissão do empregador, áudio opcional, retirada sem penalidade, nenhum dado para os gestores; *beneficência* — nenhum contato com sistemas em funcionamento, apenas simulação, teste de sensibilidade em todos os artefatos, revisão de segurança física desnecessária porque nada é energizado; *justiça* — não sobrecarregar apenas a menor concessionária; relatar a troca em clientes-hora para que a perda de nenhuma população fique escondida; *lei e interesse público* — acordos de uso de dados e de publicação, regimes de proteção da informação aplicáveis identificados, métodos transparentes. Autoridade de parada: um representante nomeado do parceiro e o pesquisador principal. Na retirada: os dados identificáveis das entrevistas são destruídos; as contribuições agregadas e desidentificadas são mantidas apenas se os termos de consentimento assim previam. A rubrica recompensa salvaguardas concretas, em especial a proteção da equipe contra o uso disciplinar e o tratamento da população atendida como parte interessada.

**EX005 — Teste de sensibilidade.**

| Artefato | Nível | Raciocínio e transformação |
|---|---|---|
| (a) Durações de restauração agregadas por classe de alimentador | Público | Nenhum ativo ou localização específicos; manter as classes amplas |
| (b) Hospitais com os dias de combustível dos geradores | Retido | Identifica instalações específicas e sua reserva — dados para a escolha de alvos. Transformar, se necessário, numa distribuição anônima dos dias de combustível por tipo de instalação |
| (c) Código do modelo | Público | Não contém dados de infraestrutura; conferir que os valores padrão são sintéticos |
| (d) Quadro de codificação das entrevistas | Público | Sem citações nem identificadores; as citações vão para o nível controlado |
| (e) Mapa do alimentador que atende a estação regional de água | Retido | Dependência específica de um ativo específico. Descrever na tese como "mapeamento fornecido pelo parceiro, usado apenas para a elicitação" |

**EX006 — Inversão de métricas.** Saída com a métrica acrescentada (amostras horárias com Q < 0,5): A 5 h, B 0 h, C 0 h. Com uma janela de 72 horas, a perda de C sobe de 7,40 para 13,40 unidades-hora, seu tempo até a recuperação passa a ser de 36 h e ele deixa de ser censurado; A e B não mudam. Para a água potável, uma métrica primária defensável são as **horas abaixo de um limiar de pressão ou de qualidade associado a um aviso de fervura ou à perda da vazão para combate a incêndio**, porque a consequência para a saúde é determinada por limiares; a perda de área e o tempo até a recuperação são secundários. A pontuação máxima nomeia a fonte do limiar (a regulamentação das concessionárias ou as orientações de saúde pública da jurisdição) em vez de inventar um valor e observa que o limiar de 0,5 do laboratório é ilustrativo.

**EX007 — Esqueleto de protocolo.** Um protocolo forte fixa a pergunta e o degrau da alegação (L5 condicional, dentro de uma classe de cenários); define a perda ponderada de serviços críticos e os clientes-hora, uma janela de 72 horas e a regra de censura; nomeia o modelo, a elicitação, o exercício de mesa e os registros históricos como fontes de evidência, com seus limites; especifica as quatro políticas e as duas regiões; pré-especifica os parâmetros, as sementes, as métricas, a margem de não inferioridade e a regra de decisão; contém a análise do Menlo, a regra "nunca teste em produção" e a aprovação para pesquisa com seres humanos para as entrevistas e o exercício de mesa; nomeia os regimes de proteção da informação e o armazenamento; anexa os acordos de uso de dados e de publicação; e lista condições de parada (pedido do parceiro; qualquer violação de dados; qualquer sofrimento de participante) distintas das condições de abandono (H2 falha nas duas regiões; o modelo falha na validação histórica por mais do que uma margem declarada com antecedência). O revisor hostil atacaria primeiro os pesos, a circularidade e a seleção dos contextos.

### Capítulo 2: EX008–EX014

**EX008 — Protocolo de busca.** Um protocolo-modelo para "Incidentes de ransomware em hospitais afetam os desfechos dos pacientes em hospitais vizinhos?": blocos de conceitos (ransomware OR cyberattack OR "cyber incident") AND (hospital OR "health system") AND (diversion OR spillover OR "neighboring" OR "nearby") AND (outcome OR mortality OR "length of stay"); fontes: um índice biomédico, um índice acadêmico geral e relatórios governamentais e setoriais; encadeamento a partir de dois estudos-semente; elegibilidade: estudos com grupo de comparação ou série temporal; triagem por dois revisores numa amostra de 10%, com a concordância relatada antes da divisão; parar quando duas rodadas consecutivas de encadeamento não acrescentarem nada. A rubrica recompensa fontes entre disciplinas e concordância medida.

**EX009 — Avaliação crítica de um artigo de modelagem.** Estrutura: a cossimulação representa as reservas e a restauração? Parâmetros: com fonte ou presumidos? Verificação: nenhuma evidência de testes na descrição — desconhecida. Validação: um evento histórico, usando o modelo dos próprios autores; boa, mas única. Sensibilidade: desconhecida. Linha de base: se a comparação for apenas com a ordenação pelos clientes, é uma linha de base fraca (Capítulo 3). Disponibilidade: desconhecida. Alegação mais forte que pode ser apoiada: "Na cossimulação dos autores, calibrada para um evento histórico, a restauração ciente das dependências reduziu a perda de serviços críticos em comparação com [a linha de base deles]" — uma alegação sobre o modelo (L2–L3), e não sobre a infraestrutura em geral.

**EX010 — Adequação da família de modelos.** (a) Insumo-produto (IIM ou I–O econômico): estima a perda de produção em nível setorial; limite — linear, sem temporização, detalhe das instalações perdido na agregação. (b) Fluxo ou cossimulação, ou um modelo de temporização das reservas como o do Laboratório 3: limite — exige dados em nível de instalação e reservas validadas. (c) Estudo empírico qualitativo (entrevistas, registros pós-ação), possivelmente informando um modelo baseado em agentes: limite — autorrelato e amostras pequenas. (d) Percolação topológica: limite — abstrata; sem reservas nem fluxos; apenas entendimento estrutural.

**EX011 — A norma como hipótese.** Alegação implícita: atribuir e implementar o SL-T por zona reduz a probabilidade de que um adversário com a capacidade correspondente alcance um efeito com consequência. Hipótese: "Em zonas de testbed implementadas segundo os requisitos do SL 3, red teams de capacidade fixa alcançam um efeito predefinido no nível do processo com menos frequência, ou levam mais tempo, do que em zonas de resto idênticas implementadas segundo o SL 1." Desenho: testbed isolado, várias zonas equivalentes, red teams independentes sem conhecimento do SL, efeitos predefinidos simulados, e não físicos. Fatores de confusão: habilidade e cansaço dos red teams; qualidade da implementação independente do SL nominal; aprendizado entre as tentativas. A rubrica recompensa a segurança (apenas testbed) e a medição da segurança alcançada, e não da afirmada.

**EX012 — Conserte o mapa da literatura.** Acrescente um sexto campo e filtre por `s[5] == "cyber"`. Saída para C3: `single-source; needs replication; strong+independent=['P7']`. A situação de C3 não muda porque P7 é ao mesmo tempo independente e cibernético, mas C1, C2 e C4 agora não têm apoio qualificado para alegações sobre quedas *induzidas por ciberataques*. Explicação: as evidências de quedas por todos os perigos só se transferem para quedas induzidas por ciberataques por argumentação — cenários cibernéticos podem ser simultâneos, ter o momento escolhido pelo adversário e corromper as ferramentas de restauração —, então uma alegação cibernética precisa de validação específica para o cibernético ou de um argumento explícito de transferência.

**EX013 — Classifique a lacuna.** (a) *Conflitante*: o próximo estudo discrimina os mecanismos — medir as duas reservas e seu esgotamento nas mesmas instalações. (b) *Não transferida*: o próximo estudo testa se as variáveis do planejamento da capacidade de pico predizem a ordem ótima de restauração. (c) *Fraca*: white papers de fornecedores com conflitos de interesse; o próximo estudo é uma comparação independente com uma linha de base forte. (d) *Ausente*: o próximo estudo é um primeiro desenho comparativo, mesmo que seja uma pequena comparação de mesa entre o CCE e a priorização orientada por vulnerabilidades.

**EX014 — Declaração falseável e memorando de fronteira.** Exemplo de declaração: "Em quedas regionais de energia de mais de oito horas, a aceitação de pagamentos com cartão em mercados e farmácias cai abaixo de 50% do normal nas primeiras quatro horas por causa da dependência do backhaul de telecomunicações e da energia dos pontos de venda, a menos que os estabelecimentos tenham capacidade de autorização off-line; isto é refutado se os registros de transações de duas regiões independentes mostrarem aceitação acima de 50% em quatro horas entre os estabelecimentos sem capacidade off-line." Notas dos testes: aberta (nenhum estudo regional encontrado na busca documentada, hipoteticamente), importante (acesso a alimentos e medicamentos durante as quedas), viável (dados agregados de transações por meio de um parceiro da rede de pagamentos), falseável (observação declarada). O memorando argumenta que o mapeamento das dependências dos estabelecimentos em relação ao backhaul precisa vir primeiro, porque sem ele a aceitação não pode ser atribuída às telecomunicações em vez de à energia. A rubrica recompensa um refutador viável e uma ordem fundamentada das perguntas.

### Capítulo 3: EX015–EX020

**EX015 — Tipificação da contribuição.** (a) Artefato — precisa de documentação, testes de verificação e evidências de uso. (b) Medição — precisa de evidências de confiabilidade (teste–reteste, entre avaliadores) e de validade. (c) Constatação empírica — precisa de um estudo amostrado e documentado das concessionárias, com base amostral e taxas de resposta. (d) Método — precisa de comparação com a melhor prática atual em métricas declaradas, em mais de um contexto. (d) usa (a) como instrumento; (a) sozinha não pode sustentar (d), porque a existência do simulador nada diz sobre se o método supera a prática atual. (c) é uma pré-condição para saber se (d) é novo na prática.

**EX016 — Verificação pela teoria de programação.** Razões *w/p*: F1 9000/4 = 2250; F2 1200/3 = 400; F3 2500/5 = 500; F4 6000/4 = 1500. Ordem de Smith: F1, F4, F3, F2. Instantes de conclusão 4, 8, 13, 16 h → clientes-hora = 9000·4 + 6000·8 + 2500·13 + 1200·16 = 135.700 → 135,7 mil. Ordem F2, F3, F1, F4: conclusões 3, 8, 12, 16 → 1200·3 + 2500·8 + 9000·12 + 6000·16 = 227.600 → 227,6 mil. Aumento de 67,7%. (Nos laboratórios deste livro, os clientes-hora também são contados por alimentador até a restauração; o atraso de reinício se aplica apenas aos serviços críticos.)

**EX017 — Extensão do tempo até o impacto.** Com F2 → HOSP = 60 e TEL → HOSP = 30, o instante de falha do hospital pela energia é min(60, 8 + 30 = 38) = 38 h, mas pela água é 9 + 4 = 13 h, então HOSP ainda falha em 13 h. O resultado não muda porque o caminho determinante é o da água. Mais fundamentalmente, o arranjo "o gerador dura 60 h *se* as telecomunicações funcionarem para pedir combustível, senão 26 h" é uma *reserva condicional* — uma combinação E/OU que um grafo de caminho mínimo com pesos fixos nas arestas não consegue expressar. Modelá-la exige reservas dependentes do estado (como nos intervalos de dependência do Laboratório 5, estendidos) ou uma simulação em que as entregas de combustível são eventos que exigem TEL.

**EX018 — Conjunto de hipóteses.** Exemplo para a restauração de sites de telecomunicações após um incidente cibernético numa operadora: *Benefício* — "Restaurar as estações rádio-base na ordem do tempo até o impacto dos serviços dependentes reduz a perda ponderada da capacidade de chamadas de emergência e da conectividade dos hospitais em ≥ 20% em comparação com a restauração pelo número de assinantes atendidos." *Melhor prática* — "…em ≥ 10% em comparação com a lista de sites prioritários existente da operadora." *Mecanismo* — "O ganho é zero onde a ordem da lista e a ordem do tempo até o impacto coincidem e cresce com a divergência; ele some quando a autonomia das baterias dos sites excede o tempo total de restauração." *Não inferioridade* — "Os assinantes-hora perdidos aumentam em ≤ 15% em comparação com a lista de sites prioritários." Desfechos definidos operacionalmente (por exemplo, tentativas de chamadas de emergência que falham por hora, a partir dos contadores da rede numa simulação). Limiares justificados pelo custo de mudança declarado pela operadora e pelas expectativas de qualidade do serviço do regulador, com responsáveis e datas.

**EX019 — Tabela de explicações rivais.** Rivais: qualquer lista de prioridades explica o ganho (teste: linha de base da lista); pesos (teste: pesos alternativos); baterias curtas na rede escolhida (teste: escalonamento das baterias, segunda rede); circularidade (teste: modelo independente, erro do mapa); adoção (teste: exercício de mesa com engenheiros); equipe única ou deslocamento ignorado (teste: equipes e matriz de deslocamento); o redirecionamento do tráfego para sites vizinhos torna a ordem irrelevante (teste: modelo com cobertura dos vizinhos). A nota máxima inclui pelo menos circularidade, adequação da linha de base, pesos e adoção.

**EX020 — Condições de falha e critérios do segundo contexto.** Condições de falha: como em §3.8, adaptadas. Critérios do segundo contexto derivados do mecanismo: pelo menos três sites de serviços críticos; divergência entre a ordem da lista e a ordem do tempo até o impacto em pelo menos duas posições; faixa das reservas sobrepondo-se ao tempo total de restauração; um modelo de equipes diferente do primeiro contexto. Verificação pelos revisores: uma emenda ao pré-registro com carimbo de tempo (num registro público ou num commit do repositório com tag assinada) datada antes de qualquer simulação do segundo contexto, mais a declaração do modelador de que não teve acesso aos resultados do primeiro contexto.

### Capítulo 4: EX021–EX026

**EX021 — Registro de reprodução.** Alvo: água 0,236 (artigo sintético, Tabela 2). Tolerância de ± 0,005 fixada antes da execução. Execução 1 (matriz transposta): `[0.528, 0.028, 0.057]` — a água difere em 0,208, fora da tolerância; a energia confere. Diagnóstico: o artigo define *A\*_ij* como o efeito de *j* sobre *i*; o arquivo de entrada foi lido por colunas. Execução 2 (convenção correta): `[0.528, 0.236, 0.163]` — reproduzido. Ambiente: versão do Python, sistema operacional, data. Decisão: reproduzido após a correção de um erro de convenção no nosso tratamento da entrada. Observação: a energia coincidir nas duas execuções mostra por que verificar uma única saída é insuficiente.

**EX022 — Análise de perturbações no IIM.** Energia 0,5 sozinha: `[0.528, 0.236, 0.163]`. Telecomunicações 0,5 sozinhas: `[0.057, 0.101, 0.519]`. As duas: `[0.585, 0.336, 0.682]`, que é igual à soma dos dois vetores separados (salvo arredondamento), porque o IIM é linear: *q* = (*I* − *A\**)⁻¹ *c\** e a inversa se distribui sobre a soma das perturbações. Alegação sustentada: "neste modelo linear de equilíbrio, uma perturbação combinada de energia e telecomunicações eleva a inoperabilidade da água a cerca de 0,34". Não sustentada: qualquer coisa sobre temporização, reservas, limiares ou ordem de restauração — e qualquer alegação de que uma inoperabilidade acima de 1 tem significado (modelos lineares podem exceder os limites físicos para perturbações grandes).

**EX023 — A armadilha da ordem dos parâmetros.** Chamada correta `triangular(4, 12, 8)`: média (4 + 8 + 12) / 3 = 8,0. A chamada errada `triangular(4, 8, 12)` passa high = 8 e mode = 12; o CPython calcula *c* = (12 − 4)/(8 − 4) = 2 e retorna 4 + 4·√(2*u*), então os valores vão de 4 a cerca de 9,66 e a média é cerca de 7,77 (uma execução com semente de 100.000 sorteios deu mínimo 4,02, máximo 9,66, média 7,77). A saída não é uma distribuição triangular e excede o "high" documentado de 8, sem nunca chegar a 12. Uma verificação da média sozinha (7,77 contra 8,0) é facilmente descartada como ruído; uma verificação da faixa contra os limites documentados e um histograma revelam o erro imediatamente.

**EX024 — Testes de invariantes.** Exemplos de asserções usando o Laboratório 5: (1) com todas as reservas acima de 72 h, a perda de toda política é 0; (2) `evaluate` com ordens idênticas dá resultados idênticos; (3) ORACLE ≤ cada política em cada sorteio; (4) aumentar a reserva de um serviço em 1 h nunca aumenta a perda sobre sorteios fixos; (5) com durações iguais, os clientes-hora de SILO ≤ os de toda permutação. Remover o atraso de reinício de um serviço *não* é detectado por nenhuma dessas invariantes — isso reduz as perdas de todas as políticas de forma consistente. Ele é detectado por um **teste unitário** sobre um único serviço: alimentador restaurado em 5 h, reserva de 2 h → intervalo de interrupção esperado (2, 6). A nota máxima tira a lição: as invariantes testam a estrutura, os testes unitários testam a semântica; você precisa dos dois.

**EX025 — Métrica de detecção relativa à latência.** Definição: para cada segmento anômalo *k* com início *s_k*, primeiro alarme *a_k* (o primeiro índice sinalizado no segmento) e tempo até o impacto *T_k*, o segmento é "detectado antes do impacto" se *a_k* existir e (*a_k* − *s_k*) × Δ*t* < *T_k*. Com Δ*t* = 6 min e *T* = 2 h (20 passos): o primeiro alarme do segmento 1 está no deslocamento de 21 passos (2,1 h) → não; o do segmento 2 no deslocamento 0 → sim; o do segmento 3 no deslocamento de 29 passos (2,9 h) → não. Fração detectada antes do impacto = 1/3. Contraste: PA-F1 0,911, F1 por pontos 0,05, PA%K 0,05. A métrica de latência mostra que um detector sem nenhuma informação vence a reserva apenas por acaso — uma informação que o PA-F1 esconde por completo.

**EX026 — Plano do piloto.** Um plano forte lista as perguntas de viabilidade (taxa de recrutamento, compreensão dos materiais, duração das sessões, captura de dados, tempo de execução, testes de invariantes), define limiares como em §4.7.2, especifica as respostas de "não prosseguir" (revisar e repilotar; mudar a via de recrutamento; reduzir o escopo), exclui os participantes do piloto do estudo principal porque eles já viram os materiais e suas escolhas estariam contaminadas, e declara explicitamente que nenhum tamanho de efeito será estimado nem relatado como evidência.

### Capítulo 5: EX027–EX032

**EX027 — Execute e interprete o estudo principal.** A saída exata está impressa em §5.2.1. Variação relativa de DEP em relação a CRITFLAG: Riverbend 4,32 / 3,97 − 1 = +8,8% (DEP um pouco pior); Port Halvard 9,61 / 31,63 − 1 = −69,6%. Parágrafo-modelo: "Em relação à ordenação pelos clientes, as duas ordenações cientes da criticidade reduziram a perda ponderada de serviços críticos em mais de 80% nas duas regiões sintéticas, ao mesmo tempo em que aumentaram os clientes-hora em 58–71%, o que excede a margem de 15% declarada com antecedência (H4a não atendida). Em relação à ordenação por sinalização crítica, a ordenação pelo tempo até o impacto não produziu redução em Riverbend (diferença média de +0,35, intervalo de Monte Carlo de 95% de −0,23 a 0,97; uma redução de 10% fica descartada) e produziu uma redução de 70% em Port Halvard, onde igualou o oráculo; os clientes-hora subiram 2,3% e 9,9%, respectivamente, dentro da margem (H4b atendida). Os intervalos refletem apenas o ruído da simulação."

**EX028 — Pareado versus não pareado.** Riverbend, 500 sorteios: DP das perdas de DEP ≈ 6,36, das de CRITFLAG ≈ 4,57, das diferenças por sorteio ≈ 6,79. Intervalo não pareado de 95% para a diferença de médias ≈ 0,35 ± 1,96 × √((6,36² + 4,57²)/500) ≈ −0,34 a 1,04; pareado ≈ −0,24 a 0,95. O pareamento ajudou apenas modestamente. As perdas das duas políticas são fraca e positivamente correlacionadas: em muitos sorteios, uma protege a água e a outra as telecomunicações, então suas perdas se movem em direções diferentes. A variância das diferenças, Var(A) + Var(B) − 2 Cov(A, B), pode, portanto, exceder a variância de qualquer das políticas e ainda ficar abaixo da soma não pareada. Os números aleatórios comuns continuam corretos; seu ganho de precisão é uma questão empírica.

**EX029 — Taxonomia da incerteza.** (a) Monte Carlo — mais sorteios. (b) Parâmetros — elicitação com incerteza, verificação dos estoques, análise de sensibilidade. (c) Estrutural — extensão do modelo (tempos de deslocamento), comparação de estruturas de modelo. (d) Valores — conjuntos alternativos de pesos, relato transparente dos vereditos por conjunto, deliberação com as partes interessadas. (e) Parâmetros (família de distribuições) ou estrutural (se a forma refletir um mecanismo como o esgotamento) — testar famílias alternativas e relatar a sensibilidade.

**EX030 — Crítica do desenho do exercício de mesa.**

| Ameaça | Mudança | Custo |
|---|---|---|
| Características de demanda (os participantes adivinham a resposta "certa") | Incluir cenários de preenchimento em que DEP não é ótima; enquadramento neutro | Sessões mais longas |
| Amostra pequena, três concessionárias | Recrutar em mais concessionárias, estratificadas por porte | Esforço de recrutamento; mais acordos |
| Sem pressão de tempo nem cansaço | Decisões cronometradas dentro de um exercício mais longo; inserção num exercício programado da concessionária | Realismo versus carga; consentimento dos responsáveis pelo exercício |
| Reconhecimento dos cenários isomórficos | Variar mais as características de superfície; separar as sessões por dias | Logística; desistências |
| Exibição testada apenas em combinação com a informação de temporização | Acrescentar um terceiro braço: lista de sinalização com os caminhos mostrados, mas sem os tempos | Mais participantes necessários |
| Desfecho pontuado no mesmo modelo usado para desenhar DEP | Pontuar as escolhas também por um painel independente de especialistas | Tempo do painel |

**EX031 — Matriz de evidências de validação.** Uma resposta forte escolhe validade aparente, histórica, de condições extremas, de variabilidade dos parâmetros e operacional; é honesta quanto à impossibilidade da validação histórica de eventos cibernéticos raros e a substitui por eventos de todas as causas com um argumento de transferência; e identifica o teste mais danoso — para o Cascade Study, a validação histórica da temporização das reservas, porque, se as reservas estiverem sistematicamente erradas, todo resultado de ordenação muda — e o programa para antes do estudo principal.

**EX032 — Memorando de transportabilidade.** A concessionária tem três alimentadores críticos cuja ordem das reservas coincide com a ordem dos clientes, e uma equipe. Moderadores: divergência zero; uma equipe; reservas desconhecidas em relação ao tempo de restauração; acurácia do mapa desconhecida. Previsão: a ordenação pelo tempo até o impacto produzirá a mesma ordem que a lista crítica, então o ganho é zero. Ressalvas: se os pesos ou o espalhamento (um alimentador que protege vários serviços ponderados) diferirem, uma regra ciente dos pesos ainda poderia ajudar — isso está fora da alegação testada. Dados que mudariam a previsão: reservas corrigidas (que poderiam mudar a ordem), evidências de erros no mapa ou dependências que não estejam na lista.

### Capítulo 6: EX033–EX038

**EX033 — Relatório do red team.** As objeções-modelo são as de §6.2, mais, por exemplo, "o horizonte de 72 horas censura as quedas longas" (teste: estender para 120 h e contar os serviços censurados) e "as distribuições triangulares subestimam as caudas" (teste: reservas lognormais com medianas iguais). Cada objeção declara sua previsão antes do teste; por exemplo, "se a circularidade determina o resultado, um mapa errado vai eliminar a vantagem de DEP sobre SILO" — o Capítulo 6 constatou que ele reduziu a vantagem de perda de DEP sobre SILO de cerca de 48 para cerca de 7 horas de serviço ponderadas, enquanto todas as políticas cientes da criticidade se degradaram.

**EX034 — Sensibilidade aos pesos.** Com todos os pesos definidos como 1,0 (500 sorteios, semente 7): Riverbend SILO 15,00, CRITFLAG 1,32, DEP 1,07, ORACLE 0,54; DEP − CRITFLAG −0,25 (intervalo de Monte Carlo de 95% de −0,41 a −0,08). Port Halvard SILO 14,95, CRITFLAG 8,61, DEP 2,49, ORACLE 2,49; DEP − CRITFLAG −6,12 (−6,24 a −6,00). Vereditos: H1 inalterada (sustentada); H2 em Riverbend muda de *rejeitada* para *inconclusiva* sob a regra pré-registrada — a estimativa pontual é uma redução de 19%, mas a extremidade superior do intervalo (−0,08) não fica inteiramente abaixo do limiar (−0,13); H2 em Port Halvard inalterada (sustentada); H4 não afetada (os clientes-hora não dependem dos pesos). Explicação: com os pesos declarados com antecedência, restaurar F3 primeiro protege dois serviços de peso alto (água 4 e o hospital via água 5), o que favorece a ordem de CRITFLAG; com pesos iguais, restaurar cedo as telecomunicações importa relativamente mais e a regra do menor tempo até o impacto de DEP ganha. Conclusão: o veredito de Riverbend depende dos valores; a tese precisa relatar os vereditos por conjunto de pesos.

**EX035 — Experimento de erro do mapa.** Telecomunicações verdadeiramente em F4, planejadores acreditam em F2 (300 sorteios, semente 7, sem oráculo): SILO 29,01, CRITFLAG 26,82, DEP 31,11. Com um mapa correto, CRITFLAG e DEP escolhem ambas F4, F3, F2, F1 e chegam a 4,90. Em comparação com o descompasso da água (§6.3.1), o erro das telecomunicações prejudica DEP ainda mais: DEP se torna a pior das três políticas, porque restaura F2 primeiro, com confiança, por uma central de telecomunicações que não está lá. Procedimento de auditoria: para toda instalação crítica listada, verificação de campo por amostragem do alimentador que a abastece, todo ano e após qualquer reconfiguração da rede; meta de acurácia ≥ 98% numa amostra aleatória de pelo menos 50 pares instalação–alimentador (ou todos, se forem menos); aprovação do responsável; discrepâncias corrigidas em 30 dias; resultados da auditoria armazenados em nível controlado.

**EX036 — Crítica do gerador.** Implementando "alimentadores maiores abrigam serviços de reserva mais longa" (atribuir os níveis de reserva ordenados aos alimentadores críticos ordenados por clientes, a menor reserva ao menor alimentador; 200 regiões, semente 2026): as regiões sem divergência caem de 69 para 9; divergência em duas posições, 77 regiões, ganho médio −24,85; divergência em três posições, 114 regiões, ganho médio −19,02. A correlação oposta (a menor reserva no maior alimentador) dá 162 regiões sem divergência, 35 com duas posições (ganho médio −8,65) e 3 com três (−17,24). Interpretação: o pressuposto de correlação do gerador, e não o método, controla com que frequência DEP ajuda. A alegação precisa continuar condicionada à divergência medida, e a frequência nas regiões reais precisa ser medida, e não simulada.

**EX037 — Decisão de duplo uso.** (a) *Restringir e notificar*: específica, acionável, de ganho alto — divulgação coordenada por meio do fornecedor e de um coordenador; notificar as concessionárias afetadas pelos canais adequados; publicar apenas constatações agregadas após a remediação. (b) *Publicar*: padrão geral amplamente discutido em alertas públicos; valor defensivo alto. (c) *Publicar com cuidado*: o método ajuda os planejadores; evitar liberar pipelines prontos que ingiram dados públicos de instalações de lugares nomeados. (d) *Reter ou restringir*: as estimativas para hospitais nomeados são dados de alvos com pouco valor defensivo além desses hospitais; compartilhar com eles em privado, se forem acuradas.

**EX038 — Carta de resposta.** Respostas-modelo: (1) circularidade — *parcialmente aceita*; testes de descompasso acrescentados, alegação condicionada à acurácia do mapa, auditoria do mapa recomendada. (2) Reservas curtas — *aceita como condição de contorno*; escalonamento das reservas acrescentado, alegação limitada a reservas menores do que cerca de duas vezes o tempo de restauração. (3) Seleção do contexto — *parcialmente aceita*; análise de 200 regiões acrescentada, alegação limitada à divergência medida, frequência nas regiões reais listada como desconhecida. (4) Fraqueza da heurística — *aceita*; regra ciente dos pesos apresentada como trabalho futuro exploratório, e não como resultado. (5) Duplo uso — *aceita*; revisão de duplo uso acrescentada; recomendação sobre os dados de prioridade de restauração publicada em nível geral após coordenação. Cada resposta cita a seção alterada.

### Capítulo 7: EX039–EX044

**EX039 — Mapa do argumento.** Alegação, dados, garantia, respaldo, qualificador e refutações como em §7.1, com os capítulos: dados (Capítulos 5–6), garantia (verificação do Capítulo 4 e validação do Capítulo 5), respaldo (reproduções e testes do Capítulo 4), qualificador (escopo do Capítulo 3 mais as condições do Capítulo 6), refutações (Capítulo 6 e Limitações). Garantia mais fraca: a de que o modelo classifica as ordenações de forma adequada para regiões *reais*, já que a validação histórica cobre um único evento de todas as causas e omite as reservas humanas. Fortalecimento: validação da temporização das reservas contra vários registros pós-ação, com as reservas humanas modeladas explicitamente.

**EX040 — Atribuição de níveis.** Código do simulador T0; testes de verificação T0; configuração de Riverbend T0 (inventada); formulários de elicitação com os nomes dos parceiros T3 (ou T2, se os parceiros consentirem com o acesso controlado) — transformar retirando as identidades e agregando para T1; faixas de elicitação agregadas T1 (T0 se os parceiros concordarem e não restar nenhuma estrutura única); áudio do exercício de mesa T2 — destruir após a transcrição, se o consentimento assim disser; justificativas codificadas T2, ou T1 após a desidentificação e a remoção das combinações de função mais concessionária; formulários de consentimento T2 (administrativos, nunca liberados); procedimento de restauração do parceiro T3 — descrever apenas sua existência e seu papel; figuras finais T0.

**EX041 — Manifesto que falha fechado.** Com a ordem original das regras, `data/synthetic_partner_feeders.csv` corresponde primeiro a `partner_` e é classificado como T3 (correto). Mover a regra `synthetic_` para o início o classifica como T0-public (errado) — um risco de ordenação. Uma verificação de conteúdo: antes de atribuir T0, ler os bytes e recusar T0 se `b"SUB-"` (ou qualquer padrão de uma lista de formatos de identificadores de ativos) ocorrer, retornando "UNCLASSIFIED: stop and review". Lição: coloque primeiro as regras mais restritivas, falhe fechado quando não houver correspondência e verifique o conteúdo além dos nomes.

**EX042 — Avaliação da divulgação residual.** Risco: a configuração (um hospital, duas estações de água, cinco alimentadores, hospital num alimentador específico) é uma impressão digital estrutural quase única do condado; alguém com conhecimento local poderia associá-la. Uma associação revelaria qual alimentador atende o hospital e as reservas obtidas — informação de alvos. Transformações: misturar estruturas de vários condados; generalizar para faixas; abandonar a ligação alimentador–hospital e substituí-la por uma atribuição aleatória que preserve apenas a estatística de interesse (por exemplo, a distribuição da divergência). Custo: ligação mais fraca com o caso real; a tese precisa declarar quais resultados dependem da estrutura preservada.

**EX043 — Documentação do modelo.** Propósito: classificar as ordenações de restauração pela perda ponderada de serviços críticos e pelos clientes-hora em quedas na distribuição que exigem restauração manual sequencial. Entidades: alimentadores (clientes, duração da restauração), serviços (alimentador, reserva, peso, dependência opcional com reserva local), equipes. Processos e escalonamento: as equipes pegam os alimentadores na ordem da política assim que ficam livres; os intervalos de interrupção dos serviços são calculados exatamente, do esgotamento da reserva até a restauração mais um atraso de reinício de uma hora; os intervalos de dependência começam no início da interrupção do fornecedor mais a reserva local e terminam com a restauração do fornecedor; intervalos limitados a 72 h; as dependências têm semântica de OU. Insumos: distribuições triangulares da elicitação; pesos do painel de gestão de emergências. Verificação: as invariantes e os testes unitários do EX024. Limitações: sem tempo de deslocamento; sem extensão das reservas humanas; apenas semântica de OU; reservas fixas (sem dinâmica de esgotamento); uma única classe de cenários.

**EX044 — Seção de limitações.** Uma resposta forte se parece com §7.7, com cinco ou mais limitações, cada uma com efeito, direção e estudo que a resolva, e as classifica: (1) reservas humanas omitidas (poderiam reduzir todos os benefícios da reordenação), (2) regiões sintéticas (frequência da divergência desconhecida), (3) pesos (os vereditos mudam), (4) tempo de deslocamento (reduz o benefício de DEP onde os alimentadores críticos estão dispersos), (5) escala do exercício de mesa (adoção não comprovada).

### Capítulo 8: EX045–EX050

**EX045 — Auditoria das alegações.** A saída original sinaliza K2, K3 e K4 (ver §8.1.1). K5 é relatada como "OK" porque nenhuma das palavras-chave aparece. Verificação melhorada: estender `OVERREACH` com expressões como "the grid", "resilient to", "makes", "secure" ou, melhor, exigir uma expressão de escopo explícita ("in the synthetic…") no texto de qualquer alegação cujo campo de escopo contenha "synthetic". K5 corrigida: "Em duas regiões sintéticas, a ordenação da restauração pelo tempo até o impacto reduziu a perda modelada de serviços críticos após quedas na distribuição, sob condições declaradas; ela não previne ataques cibernéticos, e seu efeito em redes reais não foi testado."

**EX046 — Banco de perguntas dos examinadores.** As três mais difíceis para o Cascade Study, com respostas-modelo: (1) "O resultado não é circular?" — responder com as evidências do descompasso e do modelador independente e admitir o que continua circular (ORACLE e DEP ainda compartilham o modelo). (2) "Por que alguém deveria aceitar os seus pesos?" — não deveria sem escrutínio; descrever a elicitação e a tabela de vereditos por conjunto de pesos; os pesos são um insumo de política que o método torna explícito. (3) "Sem um estudo de campo, o que você sabe sobre as concessionárias reais?" — que as condições para o benefício são mensuráveis; que o levantamento da divergência é o próximo estudo; que nenhuma alegação de campo é feita. Uma lacuna real revelada: a tese não tem evidências sobre se as equipes conseguem seguir um plano reordenado, dados os tempos de deslocamento — uma lacuna no trabalho, a ser declarada como limitação.

**EX047 — Plano de publicação.** Como em §8.3.1, com: o arquivo T0 v1.0 liberado com o artigo 1; os artigos 2–4 citando versões do arquivo; a revisão de duplo uso e a coordenação setorial concluídas antes de qualquer preprint do artigo 2; os prazos de aviso dos parceiros respeitados nos artigos que usam as faixas de elicitação; e uma declaração, em cada artigo, de seu escopo em relação à alegação geral da tese.

**EX048 — Encaminhamento da divulgação.**

| Constatação | Tipo | Via e temporização | Publicado |
|---|---|---|---|
| (a) O parceiro expõe sua lista de clientes críticos | Específica da organização | Relato privado imediato sob o acordo de uso de dados; confirmar a correção | Nunca de forma identificável; possivelmente uma nota geral de que as listas de prioridade precisam de controle de acesso |
| (b) Importações de configuração não assinadas num produto comercial | Vulnerabilidade de produto | CVD com o fornecedor, diretamente ou por um coordenador; publicação após a remediação ou segundo a política do coordenador | Descrição em nível de alerta após a coordenação |
| (c) Estoques das reservas no papel versus físicos | Específica da organização e de nível setorial | Relatos privados a cada parceiro; depois, publicação geral da lacuna | Constatação agregada sem identidades |
| (d) Site repetidor único para os rádios das equipes | Específica da organização, com relevância setorial | Relato privado à concessionária; constatação geral sobre pontos únicos de falha nas comunicações de restauração após a coordenação | Apenas a constatação geral |

**EX049 — Policy brief.** Um brief forte começa pelo problema (a ordem de restauração determina quais serviços críticos falham), declara quatro recomendações com níveis de confiança e links para as evidências (§8.5), inclui um parágrafo "O que esta pesquisa não mostra" (efeitos em concessionárias reais, frequência da divergência, adoção sob estresse, qualquer efeito de prevenção cibernética), usa linguagem simples e traz links para a tese e o arquivo T0. Toda frase é marcada; as frases que não podem ser rastreadas até a tese são removidas.

**EX050 — Programa de pesquisa de pós-doutorado.** Como em §8.6: (1) levantamento da divergência — alegação "a divergência ocorre em pelo menos um quarto das concessionárias pesquisadas", desenho sob proteção T3, modelo de parceria por meio das associações setoriais, decisão mudada: se promover ou não a ordenação pelo tempo até o impacto; (2) modelagem das reservas humanas — alegação "incluir as entregas de combustível e de água reduz o benefício modelado da reordenação em menos da metade", validada contra os registros pós-ação; (3) ataques à integridade dos dados de planejamento — alegação "auditorias do mapa com 98% de acurácia limitam a amplificação da consequência por dados de prioridade corrompidos a um limite declarado". Ordem: (1) primeiro, porque, se a divergência for rara, (2) e (3) importam mais do que mais trabalho de método. Resultado de parada: se o levantamento encontrar divergência em pouquíssimas concessionárias e os erros de mapa forem raros, o programa deve se voltar dos métodos de ordenação para a verificação das reservas.

<a id="glossary"></a>

## Glossário

- **Reserva (buffer)** — Capacidade armazenada (combustível, baterias, armazenamento de água, estoques, procedimentos manuais) que permite a um dependente continuar operando depois de perder um fornecedor, por uma duração que depende da carga.
- **Censura** — Observação incompleta de uma duração porque a janela de observação se fechou antes de o evento (por exemplo, a recuperação) ocorrer.
- **Números aleatórios comuns** — Avaliar todas as políticas comparadas sobre os mesmos sorteios simulados, para que as comparações sejam pareadas.
- **Consequência** — O efeito de uma perturbação sobre as pessoas e as funções de que elas dependem, medido em unidades de serviço ao longo de uma janela de tempo.
- **Ordenação por sinalização crítica (CRITFLAG)** — Neste livro, restaurar primeiro os alimentadores que abrigam instalações críticas listadas, ordenando-os entre si pelos clientes atendidos.
- **Função crítica** — Uma função do governo ou do setor privado cuja perturbação teria um efeito debilitante sobre a segurança, a economia, a saúde pública ou a segurança pública; o conjunto de National Critical Functions da CISA lista 55.
- **Serviço crítico** — Um serviço cuja interrupção além de uma duração declarada prejudica a saúde, a segurança, a proteção ou atividades econômicas essenciais de uma população declarada.
- **Ordenação pelos clientes (SILO)** — Neste livro, restaurar os alimentadores em ordem decrescente de clientes atendidos; ótima para clientes-hora quando as durações são iguais (regra de Smith).
- **Dependência / interdependência** — Uma relação unidirecional / bidirecional em que o estado de um serviço depende do estado de outro (Rinaldi, Peerenboom and Kelly, 2001).
- **Divergência** — O número de posições em que duas ordens de restauração diferem entre os alimentadores críticos; neste livro, o moderador da vantagem da DEP sobre a CRITFLAG.
- **Revisão de duplo uso** — Avaliação da vantagem que um resultado de pesquisa dá aos adversários, de seu valor defensivo e das possíveis mitigações antes da publicação.
- **Ordenação ciente das dependências (DEP)** — Neste livro, restaurar os alimentadores em ordem crescente do menor tempo esperado até o impacto dos serviços críticos que eles sustentam.
- **Modelo de insumo-produto de inoperabilidade (IIM)** — Um modelo linear baseado em Leontief da propagação da inoperabilidade de equilíbrio entre setores (Haimes and Jiang, 2001).
- **Circularidade modelo–política** — Avaliar uma política no mesmo modelo do qual ela foi derivada, de modo que os erros do modelo não possam aparecer como falhas da política.
- **Margem de não inferioridade** — A maior piora de uma métrica secundária ou de segurança aceita em troca de um benefício na métrica primária, fixada com antecedência.
- **Ordenação oráculo** — A melhor ordenação para um dado sorteio, encontrada por enumeração exaustiva; um limite superior para o que qualquer regra poderia alcançar.
- **Curva de desempenho** — A fração do serviço normal entregue ao longo do tempo, antes, durante e depois de uma perturbação.
- **Ajuste de pontos (PA)** — Um protocolo de avaliação que conta todo um segmento anômalo como detectado se qualquer ponto dele for sinalizado; sabidamente infla as pontuações (Kim et al., 2022).
- **Nível de liberação** — O nível de acesso (público, registrado, controlado, retido) em que um artefato do arquivo é disponibilizado.
- **Reprodução / replicação** — Obter resultados consistentes com os mesmos dados e métodos / com novos dados que tratam da mesma pergunta (National Academies, 2019).
- **Perda de resiliência** — A área entre o serviço pleno e a curva de desempenho ao longo de uma janela.
- **Menor efeito de interesse** — O menor efeito que mudaria uma decisão real, justificado pela consequência prática e fixado antes da análise.
- **Nível de segurança-alvo (SL-T)** — Na IEC 62443-3-2, o nível de segurança desejado para uma zona ou um conduto, determinado por meio da avaliação de riscos.
- **Tempo até o impacto** — O tempo, depois de uma falha inicial, em que um serviço dependente falha, calculado sobre todos os caminhos de dependência.
- **Verificação / validação** — Mostrar que um modelo está implementado corretamente / que ele é adequado ao propósito pretendido (Sargent, 2013).
- **Zonas e condutos** — Na IEC 62443, agrupamentos de ativos com requisitos de segurança comuns e dos canais de comunicação entre eles.

<a id="references"></a>

## Referências

Normas, regulamentações e instrumentos de política pública mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas. A lista é idêntica à da edição em inglês, com o acréscimo da LGPD, citada na §1.5.1.

**Políticas, leis e normas**

- Bank for International Settlements, Committee on Payments and Market Infrastructures, and International Organization of Securities Commissions. [Guidance on Cyber Resilience for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d146.htm). June 2016.
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set). April 2019.
- Cybersecurity and Infrastructure Security Agency. [National Security Memorandum on Critical Infrastructure Security and Resilience (overview)](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Congressional Research Service. [The 2024 National Security Memorandum on Critical Infrastructure Security and Resilience](https://www.congress.gov/crs-product/IF12716). IF12716.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- Federal Energy Regulatory Commission. [Critical Infrastructure Protection Reliability Standard CIP-015-1 — Cyber Security — Internal Network Security Monitoring](https://www.federalregister.gov/documents/2025/07/02/2025-12309/critical-infrastructure-protection-reliability-standard-cip-015-1-cyber-security-internal-network). Order No. 907, *Federal Register*, 2 July 2025.
- International Electrotechnical Commission. [IEC 62443-3-2:2020, Security for industrial automation and control systems — Part 3-2: Security risk assessment for system design](https://webstore.iec.ch/en/publication/30727).
- Inside Privacy (Covington & Burling). [CISA Submits Final CIRCIA Rule for OMB Review](https://www.insideprivacy.com/critical-infrastructure/cisa-submits-final-circia-rule-for-omb-review/). October 2026. (Secondary source on regulatory status.)
- NERC. [CIP-015-1 standard page](https://www.nerc.com/standards/reliability-standards/cip/cip-015-1).
- NIST. [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29). NIST CSWP 29, February 2024.
- NIST. Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST SP 800-160 Vol. 2 Rev. 1, December 2021.
- NIST. Stouffer, K., Pease, M., Tang, C., Zimmerman, T., Pillitteri, V., Lightman, S., Hahn, A., Saravia, S., Sherule, A., and Thompson, M. [Guide to Operational Technology (OT) Security](https://doi.org/10.6028/NIST.SP.800-82r3). NIST SP 800-82 Rev. 3, September 2023. [CSRC page with Rev. 4 draft note](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- The White House. [National Security Memorandum on Critical Infrastructure Security and Resilience (NSM-22)](https://www.govinfo.gov/content/pkg/DCPD-202400358/html/DCPD-202400358.htm). 30 April 2024.
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>

**Relatórios de incidentes e de ameaças**

- CISA. [CrashOverride Malware (TA17-163A)](https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware). June 2017.
- CISA. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf).
- CISA and partners. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- E-ISAC and SANS ICS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). 18 March 2016 (archived copy at the National Security Archive).
- Langner, R. [To Kill a Centrifuge: A Technical Analysis of What Stuxnet's Creators Tried to Achieve](https://archive.org/details/to-kill-a-centrifuge). The Langner Group, November 2013 (Internet Archive copy).

**Infraestrutura, resiliência e modelagem**

- Bochman, A. A., and Freeman, S. [Countering Cyber Sabotage: Introducing Consequence-Driven, Cyber-Informed Engineering (CCE)](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710). CRC Press, 2021.
- Bruneau, M., Chang, S. E., Eguchi, R. T., Lee, G. C., O'Rourke, T. D., Reinhorn, A. M., Shinozuka, M., Tierney, K., Wallace, W. A., and von Winterfeldt, D. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra* 19(4), 2003.
- Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., and Havlin, S. [Catastrophic Cascade of Failures in Interdependent Networks](https://doi.org/10.1038/nature08932). *Nature* 464, 2010.
- Goh, J., Adepu, S., Junejo, K. N., and Mathur, A. [A Dataset to Support Research in the Design of Secure Water Treatment Systems](https://doi.org/10.1007/978-3-319-71368-7_8). CRITIS 2016, LNCS 10242.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis* 29(4), 2009.
- Haimes, Y. Y., and Jiang, P. [Leontief-Based Model of Risk in Complex Interconnected Infrastructures](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1)). *Journal of Infrastructure Systems* 7(1), 2001.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- Lenstra, J. K., Rinnooy Kan, A. H. G., and Brucker, P. [Complexity of Machine Scheduling Problems](https://doi.org/10.1016/S0167-5060(08)70743-X). *Annals of Discrete Mathematics* 1, 1977.
- Neprash, H. T., McGlave, C. C., et al. [Trends in Ransomware Attacks on US Hospitals, Clinics, and Other Health Care Delivery Organizations, 2016–2021](https://doi.org/10.1001/jamahealthforum.2022.4873). *JAMA Health Forum* 3(12), 2022.
- Ouyang, M. [Review on Modeling and Simulation of Interdependent Critical Infrastructure Systems](https://doi.org/10.1016/j.ress.2013.06.040). *Reliability Engineering & System Safety* 121, 2014.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine* 21(6), 2001.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation* 7(1), 2013.
- Smith, W. E. [Various Optimizers for Single-Stage Production](https://doi.org/10.1002/nav.3800030106). *Naval Research Logistics Quarterly* 3(1–2), 1956.
- Taormina, R., et al. [Battle of the Attack Detection Algorithms: Disclosing Cyber Attacks on Water Distribution Networks](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969). *Journal of Water Resources Planning and Management* 144(8), 2018.

**Métodos de pesquisa, avaliação e integridade**

- Arp, D., Quiring, E., Pendlebury, F., Warnecke, A., Pierazzi, F., Wressnegger, C., Cavallaro, L., and Rieck, K. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). USENIX Security Symposium, 2022.
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- Gebru, T., Morgenstern, J., Vecchione, B., Wortman Vaughan, J., Wallach, H., Daumé III, H., and Crawford, K. [Datasheets for Datasets](https://doi.org/10.1145/3458723). *Communications of the ACM* 64(12), 2021.
- Grimm, V., et al. [A Standard Protocol for Describing Individual-Based and Agent-Based Models](https://doi.org/10.1016/j.ecolmodel.2006.04.023). *Ecological Modelling* 198(1–2), 2006.
- Kerr, N. L. [HARKing: Hypothesizing After the Results Are Known](https://doi.org/10.1207/s15327957pspr0203_4). *Personality and Social Psychology Review*, 1998.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *Proceedings of the AAAI Conference on Artificial Intelligence* 36(7), 2022.
- Leon, A. C., Davis, L. L., and Kraemer, H. C. [The Role and Interpretation of Pilot Studies in Clinical Research](https://doi.org/10.1016/j.jpsychires.2010.10.008). *Journal of Psychiatric Research* 45(5), 2011.
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596). FAT* 2019.
- National Academies of Sciences, Engineering, and Medicine. [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303). 2019.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *PNAS*, 2018.
- O'Hagan, A., Buck, C. E., Daneshkhah, A., Eiser, J. R., Garthwaite, P. H., Jenkinson, D. J., Oakley, J. E., and Rakow, T. [Uncertain Judgements: Eliciting Experts' Probabilities](https://doi.org/10.1002/0470033312). Wiley, 2006.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71). *BMJ*, 2021.
- Pearl, J., and Bareinboim, E. [External Validity: From Do-Calculus to Transportability Across Populations](https://doi.org/10.1214/14-STS486). *Statistical Science* 29(4), 2014.
- Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M., and Tarantola, S. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology* 9(10), 2013.
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. [False-Positive Psychology](https://doi.org/10.1177/0956797611417632). *Psychological Science*, 2011.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). IEEE Symposium on Security and Privacy, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18). *Scientific Data*, 2016.

Material complementar do OpenCyber Academy: o [livro de doutorado de Resposta a Incidentes](../../../incident-response-resilience/en/book/MANUSCRIPT.md) (escada de alegações e métodos de integridade da pesquisa reutilizados no Capítulo 1) e o [curso de doutorado em segurança de TO, IoT e sistemas ciberfísicos](../../../ot-iot-security/README.md) (camada dos sistemas de controle).

**Limite do caso.** A Riverbend Region, Port Halvard, a Riverbend Electric Cooperative, a Riverbend Water Authority, o St. Calder Hospital, a Meridian Telecom, o GridWater-Sim, os estudos P1–P8, os participantes P01–P12, o Cascade Study e todos os números produzidos pelos laboratórios foram inventados para o ensino. As fontes apoiam as afirmações gerais ao lado das quais são citadas, nunca os detalhes sintéticos.

**Metadados da edição.** Edição em rascunho, outubro de 2026; tradução para o português de outubro de 2026. Revisor: pendente. Verificação A4 para publicação: pendente; uma verificação preliminar de diagramação está registrada na [revisão de progresso](../../../../../STRUCTURE_REVIEW.md#a4-preflight).
