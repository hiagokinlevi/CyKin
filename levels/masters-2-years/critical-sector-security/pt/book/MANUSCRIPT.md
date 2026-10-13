# Infraestrutura Crítica e Segurança Setorial: Desenho de Pesquisa Aplicada e a Dissertação de Mestrado

- Idioma: português do Brasil (`pt`); curso de mestrado, dois anos; aproximadamente 1.200 horas de estudo planejado (curso 184 de 207 da [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 8 já estão escritos em português, com os exercícios EX001–EX026 e suas resoluções; os capítulos 5–8 (EX027–EX050) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: pesquisadores iniciantes que conhecem a área pela prática ou por estudos anteriores e agora precisam responder a uma pergunta delimitada sobre a segurança e a resiliência da infraestrutura crítica — saúde, energia, água, transporte, comunicações, finanças e serviços públicos — com evidências que outra pessoa possa verificar. Conhecimento de entrada: o conteúdo planejado para as trilhas de [engenharia](../../../../engineering-5-years/critical-sector-security/en/book/PLAN.md) ou de [bacharelado](../../../../bachelors-4-years/critical-sector-security/en/book/PLAN.md) desta área (ainda esboços quando este texto foi escrito), ou experiência profissional equivalente, mais estatística introdutória (médias, variância, intervalos de confiança, regressão linear) e a capacidade de executar um script curto em Python.
- Relação com o curso de doutorado: o [livro de doutorado desta área](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) pede a um pesquisador que faça e defenda uma contribuição *original* — um método novo, validado de forma independente, com um programa de publicações. Este livro de mestrado pede algo diferente e anterior: **desenhar, pilotar e executar bem um estudo empírico com revisão ética**, relatar exatamente o que ele pode e não pode mostrar e defendê-lo diante dos examinadores. Onde o livro de doutorado constrói simulações e replica linhas de base, este livro trabalha sobretudo com dados observacionais, desenhos quase experimentais e entrevistas, porque é a isso que a maioria dos projetos de mestrado nesta área consegue ter acesso.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de titularidade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: este curso é um projeto educacional independente. Não é um programa de mestrado credenciado, não concede diploma e não concede nenhuma autorização para acessar, varrer, testar ou estudar qualquer infraestrutura, operador, conjunto de dados ou pessoa reais. Toda organização, região, hospital, pessoa, registro, conjunto de dados e resultado numérico de um exemplo resolvido é **sintético**, a menos que uma frase cite explicitamente uma fonte pública. Nada neste livro é um procedimento operacional para um hospital, uma concessionária ou um serviço de emergência reais, e nada nele é aconselhamento jurídico ou clínico.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão de livros](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia os oito capítulos em ordem; juntos, eles acompanham uma dissertação de mestrado da primeira ideia até a banca. O Capítulo 1 transforma um tema numa pergunta respondível e constrói uma busca bibliográfica documentada. O Capítulo 2 é o seminário avançado: ele examina como os setores diferem, que evidências existem para cada um e como ler criticamente um artigo setorial. O Capítulo 3 escolhe um desenho, escreve a submissão ao comitê de ética e monta um projeto reprodutível antes que chegue qualquer dado. O Capítulo 4 lista as explicações que poderiam produzir os mesmos dados que a hipótese e constrói os testes que as separam. O Capítulo 5 escreve a proposta e executa um piloto cuja tarefa é testar a viabilidade, e não encontrar um efeito. O Capítulo 6 coleta e analisa os dados, quantitativos e qualitativos. O Capítulo 7 escreve a dissertação e suas limitações. O Capítulo 8 prepara o exame independente, a defesa oral e o compartilhamento responsável dos resultados.

Cada capítulo contém seções didáticas, definições, um exemplo resolvido, uma atividade prática com um laboratório offline em Python, uma lista de erros comuns e limites, exercícios numerados e uma síntese. Os laboratórios usam apenas a biblioteca padrão do Python 3; não é preciso acesso à rede, pacotes nem dados reais. Escreva sua resposta a cada exercício antes de abrir as [resoluções](#worked-results). Muitos exercícios têm mais de uma resposta defensável; a resolução mostra uma, e a rubrica mostra o que um examinador recompensaria.

Mantenha quatro rótulos em toda nota de pesquisa que escrever enquanto estuda: **observação** (o que uma fonte nomeada registrou), **inferência** (o que você conclui, sob quais pressupostos), **alegação** (o que você pretende defender, com seu escopo) e **decisão** (o que alguém escolheu fazer por causa disso). A pesquisa sobre infraestrutura acrescenta um quinto: **consequência** — o efeito sobre as pessoas que dependem de um serviço. O erro mais comum no nível do mestrado não é um cálculo errado; é um cálculo correto ligado a uma alegação maior do que o desenho consegue sustentar.

### O que "pesquisa aplicada" significa neste nível

Uma dissertação de mestrado nesta área costuma ser julgada por quatro coisas: se a pergunta é clara e vale a pena ser respondida; se o desenho se ajusta à pergunta e aos dados efetivamente disponíveis; se a análise foi feita com competência e de forma reprodutível; e se as conclusões ficam dentro das evidências. A originalidade é bem-vinda, mas não é exigida no sentido do doutorado. Uma replicação bem executada de um desenho publicado numa nova região, um estudo descritivo cuidadoso de algo que ninguém mediu ou um estudo de métodos mistos que explica *por que* um efeito observado ocorreu são todas contribuições legítimas de mestrado. O que não é aceitável é uma dissertação cujas alegações não possam ser verificadas, cujos dados tenham sido obtidos sem a devida aprovação ou cuja seção de limitações liste fraquezas sem dizer em que direção elas enviesam a resposta.

### A dissertação sintética usada neste livro

O livro acompanha um projeto de mestrado inventado, o **Spillover Study**. Sua pergunta, refinada no Capítulo 1, é: *quando um sistema hospitalar é perturbado por um ataque de ransomware e desvia ambulâncias, quanto aumentam as chegadas de ambulâncias e os tempos de espera nos hospitais vizinhos, e esse aumento diminui com a distância?* A pergunta segue uma linha real de trabalhos publicados — [Dameff et al. (2023)](https://doi.org/10.1001/jamanetworkopen.2023.12270) relataram aumento de volume, de chegadas de ambulâncias e dos tempos de espera em departamentos de emergência adjacentes a um sistema de saúde sob um ataque de ransomware de um mês, em 2021 —, mas todo lugar, organização, pessoa e número do Spillover Study é fictício.

| Elemento sintético | Papel no livro | Limite |
|---|---|---|
| **Tamsin Valley** — Kestrel Health (dois hospitais, atacados), Alder Point Hospital (AP, a 6 km), Brookfield Community Hospital (BF, 14 km), Calloway General (CG, 38 km), Tamsin Valley EMS, central de despacho do condado, Tamsin Valley Healthcare Coalition | Região do estudo. O dia 0 é o início de um desvio de ambulâncias de 21 dias no Kestrel (Capítulos 3–8). | Região inventada; nenhum hospital, órgão, funcionário, paciente ou registro real. |
| **Wexmoor** — Wexmoor General (W1) e St. Aldric (W2) | Região de comparação não afetada, com padrão sazonal semelhante (Capítulos 3, 4, 6, 8). | Inventada. |
| Registros de busca com DOIs começando por `10.9999/syn` | Uma exportação de busca sintética para praticar a deduplicação e a triagem (Capítulo 1). | Registros inventados; o prefixo não pertence a nenhuma editora real e não deve ser buscado. |
| Entrevistados **I01–I10** | Gestores de departamentos de emergência, supervisores de EMS e equipe da coalizão (Capítulos 3, 5, 6). | Inventados; nenhum dado de seres humanos aparece neste livro. |
| O candidato e o orientador | As pessoas cujas decisões os exemplos resolvidos acompanham. | Papéis inventados, não pessoas reais. |

Os laboratórios geram todos os dados a partir de números aleatórios com semente impressos no texto. Como os dados são sintéticos, o livro pode dizer algo que um estudo real nunca sabe: o efeito **verdadeiro** embutido no gerador. As chegadas de Alder Point foram geradas com um aumento de 22% durante o desvio, as de Brookfield com 10% e as de Calloway com nenhum. Vários capítulos usam esse privilégio para mostrar com que frequência métodos honestos deixam de detectar ou descrevem mal um efeito real. Nunca apresente nenhum número dos laboratórios como constatação sobre hospitais reais.

### Política de fontes

Toda afirmação factual sobre uma lei, uma norma, um incidente público ou um estudo publicado remete a uma fonte consultada pelo autor em outubro de 2026. Leis e normas mudam; cada uma é citada com sua versão e data e deve ser verificada de novo antes que você se apoie nela. Onde uma afirmação é vocabulário metodológico padrão — por exemplo, que um intervalo de confiança descreve a incerteza amostral sob um modelo —, o texto diz isso em vez de inventar uma referência. Uma fonte apoia a afirmação geral ao seu lado, nunca os detalhes do caso sintético. Incidentes públicos são descritos apenas no nível de detalhe que seus editores divulgaram e, onde evidências posteriores revisaram um relato inicial, ambos são citados.

## Sumário

1. [Pergunta de pesquisa e método de revisão da literatura](#ch-01) — do tema à pergunta respondível, escopo da alegação, busca documentada entre disciplinas e na literatura cinzenta, deduplicação, triagem dupla e a matriz de conceitos.
2. [Infraestrutura crítica e segurança setorial: seminário avançado](#ch-02) — perfis setoriais e unidades de consequência, o que os catálogos públicos de incidentes podem e não podem dizer, leitura e apresentação de um artigo setorial e casos documentados cujo primeiro relato foi revisado.
3. [Desenho do estudo, ética e reprodutibilidade](#ch-03) — escolha entre desenhos quase experimentais e qualitativos, análise do desenho antes dos dados, revisão ética, proteção de dados e sensibilidade das informações de infraestrutura, e um projeto reprodutível.
4. [Infraestrutura crítica e segurança setorial: explicações concorrentes](#ch-04) — múltiplas hipóteses de trabalho, diagramas causais, regiões de comparação, controles negativos, testes placebo e dose–resposta como evidência discriminante.

Capítulos 5–8: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

As [resoluções](#worked-results) contêm EX001–EX026. Um [glossário](#glossary) e as [referências](#references) encerram o livro.

<a id="ch-01"></a>

## Capítulo 1 — Pergunta de pesquisa e método de revisão da literatura

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Passar de um tema ("ransomware em hospitais"), por um problema, a uma única pergunta de pesquisa respondível, e testá-la segundo os critérios FINER e uma versão do PICOT para infraestrutura.
2. Classificar uma pergunta como descritiva, associativa, causal, explicativa ou avaliativa, e declarar o tipo de desenho e de alegação que cada uma permite.
3. Definir a quantidade que o estudo vai estimar — seu **estimando** — em palavras precisas o bastante para que dois analistas calculem a mesma coisa.
4. Escolher um tipo de revisão (narrativa, de escopo, sistemática) adequado a uma dissertação de mestrado e justificá-lo.
5. Construir, executar e documentar uma busca interdisciplinar que inclua a literatura cinzenta, testá-la contra itens conhecidos e encerrá-la por uma regra declarada com antecedência.
6. Deduplicar registros, triá-los com dois revisores, medir a concordância com o kappa de Cohen, reparar os critérios de elegibilidade onde a discordância se concentra e relatar um diagrama de fluxo.
7. Organizar o que foi encontrado numa matriz de conceitos, em vez de um resumo autor por autor.

O capítulo fixa a pergunta e o mapa de evidências que todos os capítulos seguintes usam. O Capítulo 2 amplia o mapa para os outros setores; o Capítulo 3 escolhe um desenho para a pergunta fixada aqui; o Capítulo 4 lista as explicações rivais que a literatura já levantou; o Capítulo 7 escreve o capítulo de revisão da literatura a partir da matriz de conceitos construída aqui.

### 1.1 Do tema ao problema e à pergunta

#### 1.1.1 Três coisas diferentes

A maioria das dissertações começa com um **tema**, que é uma área de interesse: "ataques cibernéticos a hospitais". Um tema não pode ser respondido. Um **problema** é uma lacuna entre o que se sabe e o que alguém precisa saber para agir: "os planejadores regionais de emergência não sabem quanto um desvio induzido por ataque cibernético num hospital sobrecarrega seus vizinhos, então os acordos de ajuda mútua são escritos sem números." Uma **pergunta de pesquisa** é a pergunta específica cuja resposta reduziria essa lacuna: "Durante um desvio de ambulâncias induzido por ransomware, quanto mudam as chegadas diárias de ambulâncias nos hospitais num raio de 40 km, em relação ao que seria esperado sem o desvio?"

O movimento do tema à pergunta é um estreitamento, e todo estreitamento é uma decisão que você precisa ser capaz de defender. Estreitar para as *chegadas de ambulâncias* em vez de "danos aos pacientes" troca importância por mensurabilidade. Estreitar para *uma região* troca generalidade por profundidade e acesso aos dados. Estreitar para o *desvio induzido por ransomware* em vez de "incidentes cibernéticos" torna a exposição observável: um desvio tem um início e um fim que um serviço de atendimento médico de emergência (EMS) registra, enquanto "um incidente cibernético" pode permanecer desconhecido até para o próprio hospital por semanas.

#### 1.1.2 FINER e um PICOT para infraestrutura

Os pesquisadores clínicos testam as perguntas segundo os critérios FINER — viável (feasible), interessante, nova (novel), ética e relevante — e as estruturam com o PICOT: população, intervenção, comparação, desfecho (outcome) e tempo ([Farrugia et al., 2010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912019/), resumindo o *Designing Clinical Research* de Hulley e colaboradores). Ambos se transferem para a pesquisa sobre infraestrutura com uma mudança: a maioria dos estudos de infraestrutura observa uma **exposição** que o pesquisador não atribuiu, então o "I" se torna "E".

| Elemento | Significado na pesquisa sobre infraestrutura | Spillover Study (primeira versão) |
|---|---|---|
| **P**opulação / unidades | As unidades prestadoras de serviço estudadas: hospitais, departamentos de emergência, alimentadores, sistemas de água, processadores de pagamento. Declare a unidade de análise e a unidade de observação (elas podem diferir: a unidade pode ser um hospital-dia). | Departamentos de emergência (DEs) de Tamsin Valley, exceto os do Kestrel; unidade de observação: o DE-dia. |
| **E**xposição | O evento ou a condição cuja consequência é estudada, definido de modo que seu início e seu fim sejam observáveis. | Desvio de ambulâncias no Kestrel causado por um ataque de ransomware (dias 0–20). |
| **C**omparação | Com o que a experiência dos expostos é comparada: as mesmas unidades antes, unidades não expostas ao mesmo tempo, ou ambos. | Os mesmos DEs nos 180 dias anteriores; os DEs de Wexmoor nos mesmos dias. |
| Desfecho (**O**utcome) | Uma consequência medida em unidades de serviço. Nomeie o desfecho primário e no máximo alguns secundários. | Primário: chegadas diárias de ambulâncias. Secundário: mediana dos minutos entre a chegada e o primeiro atendimento clínico. |
| **T**empo | Janela, seguimento e resolução (por hora, por dia, por mês). | Diária, do dia −180 ao dia +89. |

O FINER é uma triagem, não uma pontuação. **Viável** significa que os dados existem, que você pode obtê-los licitamente dentro do tempo do curso e que a análise está ao alcance da sua competência. **Interessante** significa que alguém que precisa tomar uma decisão se importa com a resposta. **Nova**, no nível do mestrado, inclui "medido pela primeira vez neste contexto" e "replicado com um desenho mais forte". **Ética** significa que um comitê de ética poderia aprová-la (Capítulo 3). **Relevante** significa que a resposta mudaria um plano, uma política ou um estudo posterior.

#### 1.1.3 Tipos de pergunta e as alegações que permitem

| Tipo | Forma | Exemplo | O que o desenho precisa fornecer | Alegação mais forte |
|---|---|---|---|---|
| Descritiva | Quanto, com que frequência, o quê? | Quantas horas de desvio de ambulâncias os DEs de Tamsin Valley registraram no ano passado, por causa? | Uma população definida e registros completos. | Uma quantidade medida nessa população. |
| Associativa | X está associado a Y? | As horas de desvio são maiores nos DEs mais próximos de um hospital em desvio? | Variação em X e Y; ajuste para os fatores de confusão óbvios. | Uma associação, com seu tamanho e sua incerteza. |
| Causal | Quanto X mudou Y? | Quanto o desvio do Kestrel aumentou as chegadas em Alder Point? | Um contrafactual crível: o que teria acontecido sem X (Capítulos 3–4). | Uma estimativa de efeito sob pressupostos declarados. |
| Explicativa | Por que ou como X mudou Y? | Por meio de quais decisões os despachantes redistribuíram os pacientes? | Evidências de processo: entrevistas, documentos, registros. | Um mecanismo apoiado por relatos convergentes. |
| Avaliativa | Uma medida funcionou? | O protocolo de desvio da coalizão encurtou os tempos de espera? | Um desenho causal mais uma definição operacional de "funcionar". | Um efeito da medida, sob pressupostos. |

A pergunta primária do Spillover Study é causal; a secundária, explicativa. Essa combinação — uma estimativa quantitativa mais uma explicação do mecanismo — é típica de uma dissertação de mestrado forte e é a razão pela qual este livro ensina as duas vertentes.

### 1.2 O estimando: diga exatamente que número você vai produzir

Uma pergunta em palavras ainda deixa espaço para muitos números diferentes. "Quanto as chegadas aumentam?" poderia significar o aumento no primeiro dia, o aumento médio durante o desvio, o aumento em relação ao ano anterior, o aumento em relação a uma região de comparação ou o total de pacientes adicionais. Um **estimando** é a quantidade precisa que um estudo pretende estimar, definida antes que os dados sejam vistos. Um modelo útil tem cinco partes:

1. **Unidades:** quais unidades e quais dias (DE de Alder Point, dias 0–20).
2. **Desfecho:** o que é contado e como (chegadas de ambulâncias por dia corrido, conforme registradas no livro de chegadas do DE).
3. **Contraste:** em comparação com o quê (as chegadas que teriam ocorrido na ausência do desvio).
4. **Resumo:** a escala (razão entre a média observada e a contrafactual, relatada como variação percentual).
5. **População de inferência:** sobre quem é a resposta (este DE durante este evento — não "os hospitais em geral").

O estimando primário do Spillover Study é, portanto: *para cada DE vizinho, a variação percentual da média diária de chegadas de ambulâncias durante os dias 0–20, em relação às chegadas esperadas a partir da tendência pré-evento desse DE e da variação simultânea nos DEs não afetados de Wexmoor.* O contrafactual "teria ocorrido" nunca é observado; os Capítulos 3 e 4 decidem como aproximá-lo. Escrever o estimando primeiro evita uma falha comum: escolher a comparação depois de ver qual delas dá o número mais impressionante.

#### 1.2.1 Escopo da alegação

O [livro de doutorado desta área](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md#ch-01) descreve uma escada de cinco degraus, da observação à alegação de pesquisa. No nível do mestrado, a disciplina essencial é mais simples: **escreva a alegação que você espera fazer e o escopo que ela terá antes de começar**, e depois verifique, no fim, se as evidências chegaram lá. O Spillover Study espera alegar: *"Num evento regional sintético, as chegadas de ambulâncias no DE vizinho mais próximo aumentaram durante o desvio num montante que estimamos com incerteza declarada, e o aumento foi menor nos DEs mais distantes."* Ele não espera alegar que o ransomware prejudica os pacientes, que todas as regiões se comportam assim nem que as políticas de desvio devam mudar — embora a discussão possa sugerir quais estudos poderiam sustentar essas alegações maiores.

### 1.3 Para que serve uma revisão da literatura

No nível do mestrado, a revisão tem quatro tarefas: mostrar que a pergunta está em aberto ou vale a pena ser feita de novo; encontrar os **métodos e as medidas** que outros usaram, para que você não os reinvente; encontrar as **explicações rivais** já levantadas (Capítulo 4); e situar o resultado final no contexto. Ela não é uma bibliografia anotada nem uma demonstração de quanto você leu.

| Tipo de revisão | Propósito | Requisitos do método | Adequada a um projeto de mestrado quando |
|---|---|---|---|
| Narrativa (tradicional) | Síntese e argumentação especializadas | Poucas regras formais; risco de citação seletiva | A revisão apoia um estudo empírico primário e a área é pequena |
| De escopo | Mapear a extensão, a variedade e a natureza das evidências; esclarecer conceitos | Arcabouço de [Arksey and O'Malley (2005)](https://doi.org/10.1080/1364557032000119616); relato segundo o [PRISMA-ScR (Tricco et al., 2018)](https://doi.org/10.7326/M18-0850) | A literatura está espalhada entre disciplinas e a pergunta ainda está sendo moldada |
| Sistemática | Responder a uma pergunta focada com busca exaustiva e avaliação crítica | Protocolo, triagem dupla, risco de viés, relato segundo o [PRISMA 2020](https://doi.org/10.1136/bmj.n71) | A revisão *é* a dissertação, e há literatura suficiente para sintetizar |
| Integrativa / semissistemática | Combinar tipos diversos de estudo numa síntese conceitual | Busca documentada com síntese flexível ([Snyder, 2019](https://doi.org/10.1016/j.jbusres.2019.07.039)) | A área mistura trabalhos empíricos, técnicos e de políticas |

Para o Spillover Study, a revisão é uma **revisão de escopo estruturada** que apoia um estudo empírico: busca documentada, elegibilidade explícita, dois revisores numa amostra, um diagrama de fluxo e uma matriz de conceitos — mas sem pontuação formal do risco de viés nem metanálise, porque o punhado de estudos relevantes usa desenhos incomparáveis. Declare essa escolha e sua razão no capítulo de métodos; um leitor nunca deveria ter de adivinhar se uma revisão pretendia ser exaustiva.

### 1.4 Buscando entre disciplinas

#### 1.4.1 Por que a literatura sobre infraestrutura é dispersa

As evidências sobre a pergunta do Spillover estão espalhadas entre medicina de emergência, pesquisa em serviços de saúde, economia da saúde, medicina de desastres, segurança da informação, administração pública e auditoria governamental. A mesma ideia tem nomes diferentes: "ambulance diversion", "ED crowding", "regional surge", "patient redistribution", "blast radius". As bases de segurança raramente indexam as operações hospitalares; as bases médicas raramente indexam os artigos de conferências de segurança; e algumas das evidências mais informativas — relatórios de auditoria, declarações de reguladores, relatórios pós-ação, relatórios de exercícios das coalizões de saúde — são **literatura cinzenta** que nenhuma base bibliográfica indexa.

#### 1.4.2 Blocos de conceitos

Construa a busca a partir de blocos de conceitos combinados com AND; dentro de cada bloco, sinônimos combinados com OR:

- **Bloco A — exposição cibernética:** ransomware OR cyberattack OR "cyber attack" OR "cyber incident" OR "IT outage" OR "downtime" OR "information system failure".
- **Bloco B — cenário:** hospital OR "emergency department" OR "health system" OR "health care delivery organization" OR EMS OR ambulance.
- **Bloco C — consequência regional:** diversion OR crowding OR "neighbouring" OR "neighboring" OR adjacent OR regional OR spillover OR "surge".

Incluir "downtime" e "IT outage" no Bloco A é uma escolha deliberada: as interrupções não maliciosas produzem efeitos operacionais semelhantes e podem fornecer métodos e rivais (Capítulo 4). Registre a escolha; ela amplia o trabalho de triagem e precisa ser tratada pelos critérios de elegibilidade.

#### 1.4.3 Fontes e o teste dos itens conhecidos

Busque em pelo menos um índice biomédico, um índice acadêmico geral e um índice de computação, mais um plano para a literatura cinzenta: tribunais de contas e órgãos de auditoria governamentais, ministérios e agências de saúde, órgãos de coordenação setorial, associações de hospitais e relatórios das coalizões. Antes de executar a busca completa, monte um **conjunto de itens conhecidos** — estudos que você já sabe serem relevantes — e verifique se a sua busca os encontra. Para a pergunta do Spillover, um conjunto razoável de itens conhecidos é [Dameff et al. (2023)](https://doi.org/10.1001/jamanetworkopen.2023.12270), [Ghafur et al. (2019)](https://doi.org/10.1038/s41746-019-0161-6) sobre o WannaCry no NHS inglês e [Neprash et al. (2022)](https://doi.org/10.1001/jamahealthforum.2022.4873) sobre as tendências do ransomware nas organizações prestadoras de cuidados de saúde dos EUA. Uma busca que deixa escapar um item conhecido é estreita demais; revise-a e registre a revisão.

#### 1.4.4 Encadeamento de citações e encerramento

As buscas em bases deixam escapar artigos que usam vocabulário inesperado. O **encadeamento para trás** lê as listas de referências dos estudos incluídos; o **encadeamento para a frente** encontra artigos posteriores que os citam. [Wohlin (2014)](https://doi.org/10.1145/2601248.2601268) dá diretrizes para essa "bola de neve" (snowballing) e mostra que ela pode complementar ou substituir a busca em bases em algumas áreas. Decida com antecedência quando parar: por exemplo, *após duas rodadas consecutivas de encadeamento que não acrescentem nenhum estudo incluído*. Registre cada busca num **registro de buscas**: data, fonte, expressão exata, filtros, número de resultados e quem a executou.

### 1.5 Dos registros aos estudos incluídos

#### 1.5.1 Deduplicação

O mesmo artigo aparece em várias bases, com maiúsculas, pontuação e hifenização diferentes e às vezes sem DOI. Deduplique antes da triagem, para que dois revisores não triem o mesmo estudo duas vezes e o diagrama de fluxo seja honesto. Um procedimento sólido em duas passadas é: (1) casar os DOIs exatos após converter para minúsculas; (2) entre os restantes, casar os títulos normalizados mais o ano — minúsculas, sem pontuação, espaços colapsados e variantes conhecidas normalizadas (por exemplo, "turn-around" e "turnaround"). Inspecione a olho cada correspondência automática num projeto pequeno; as regras automáticas podem fundir artigos diferentes com títulos genéricos ("Editorial", "Correction").

#### 1.5.2 Triagem em duas etapas e concordância

Trie os títulos e os resumos segundo os critérios de elegibilidade e depois leia os textos completos de tudo o que passar. No nível do mestrado, muitas vezes dois revisores não conseguem triar tudo; um meio-termo defensável é que um segundo revisor (um colega ou o orientador) trie de forma independente uma amostra, a concordância seja medida, os critérios sejam reparados onde a discordância se concentra e o primeiro revisor então trie o restante com os critérios reparados.

A concordância é medida com o **kappa de Cohen** ([Cohen, 1960](https://doi.org/10.1177/001316446002000104)), que corrige a concordância observada *p*ₒ pela concordância *p*ₑ esperada ao acaso a partir da taxa de inclusão de cada revisor: κ = (*p*ₒ − *p*ₑ) / (1 − *p*ₑ). Dois revisores que incluem, cada um, metade dos registros concordariam metade das vezes só por acaso, então 80% de concordância bruta pode não impressionar. As faixas de interpretação variam, e [McHugh (2012)](https://doi.org/10.11613/BM.2012.031) argumenta que as faixas mais citadas são lenientes demais para a pesquisa em saúde, em que baixa concordância significa dados não confiáveis. Trate o kappa como um diagnóstico: **onde** os revisores discordam diz qual critério está pouco claro.

#### 1.5.3 O diagrama de fluxo

Relate os registros identificados por fonte, as duplicatas removidas, os registros triados, os registros excluídos, os textos completos avaliados, os textos completos excluídos *com as razões* e os estudos incluídos. O PRISMA 2020 fornece um diagrama de fluxo padrão ([Page et al., 2021](https://doi.org/10.1136/bmj.n71)). Mesmo uma revisão não sistemática se beneficia dele, porque ele permite que um examinador veja o denominador por trás de "a literatura mostra".

### 1.6 Síntese por conceito, e não por autor

[Webster and Watson (2002)](https://www.jstor.org/stable/4132319) recomendaram que as revisões sejam **centradas em conceitos**, e não em autores: em vez de um parágrafo por artigo ("Smith constatou…; Jones constatou…"), organize a revisão em torno dos conceitos de que a pergunta precisa e mostre quais estudos informam cada um. Uma **matriz de conceitos** tem os estudos como linhas e os conceitos como colunas. Para o Spillover Study, as colunas são: unidade de análise; definição da exposição; comparação; desfecho; desenho; o que o estudo pode sustentar; rivais que levanta.

| Estudo | Unidade | Exposição | Comparação | Desfechos relevantes para o transbordamento | Desenho (como publicado) | O que pode sustentar |
|---|---|---|---|---|---|---|
| [Dameff et al., 2023](https://doi.org/10.1001/jamanetworkopen.2023.12270) | Dois DEs adjacentes a uma organização atacada | Ataque de ransomware de um mês a quatro hospitais adjacentes (maio de 2021) | Os mesmos DEs nas quatro semanas anteriores e posteriores | Censo, chegadas de ambulâncias, tempos de espera, saídas sem atendimento, tempo de permanência, desvio do EMS do condado, métricas de AVC | Coorte antes e depois | Uma associação entre o período do ataque e a sobrecarga nos DEs vizinhos numa região |
| [Ghafur et al., 2019](https://doi.org/10.1038/s41746-019-0161-6) | Trusts do NHS inglês | WannaCry (maio de 2017) | Semanas de linha de base; trusts infectados versus não infectados | Internações, atendimentos de A&E, cancelamentos de ambulatório, óbitos em A&E | Análise retrospectiva das Hospital Episode Statistics | Reduções de atividade nos trusts infectados; nenhuma variação detectável nos óbitos em A&E (uma medida grosseira de dano, como os autores observam) |
| [Neprash et al., 2022](https://doi.org/10.1001/jamahealthforum.2022.4873) | Organizações prestadoras de cuidados de saúde dos EUA | Ataques de ransomware numa base construída a partir de relatos públicos, 2016–2021 | Tendências temporais | Frequência, exposição de PHI, interrupção operacional, incluindo desvio de ambulâncias | Coorte de ataques relatados | Tendências e características dos ataques *relatados* |

A matriz torna a lacuna visível: um estudo antes e depois de DEs vizinhos, nenhum estudo com uma região de comparação não afetada e nenhum estudo sobre se a sobrecarga diminui com a distância. Essa é a justificativa do Spillover Study.

### 1.7 Ler um estudo pelo desenho, e não só pelas constatações

Ao extrair um estudo, registre não apenas o que ele constatou, mas o que ele **poderia** ter constatado. Pergunte: Qual é a unidade? A exposição é definida por seu início e seu fim? Qual é a comparação, e o que mais mudou entre os períodos comparados? O desfecho é uma consequência (pacientes atrasados) ou uma atividade (atendimentos contados)? Para que população o resultado poderia ser generalizado? Uma comparação antes e depois dentro das mesmas unidades, por exemplo, não consegue separar a exposição de tudo o mais que mudou ao mesmo tempo — estação do ano, política, quadro de pessoal, uma epidemia simultânea. Dizer isso não é uma crítica aos autores; é a evidência que o seu próprio desenho precisa superar.

### 1.8 Exemplo resolvido: do tema à pergunta do Spillover (sintético)

O primeiro parágrafo da proposta do candidato dizia: *"Esta dissertação investigará o impacto dos ataques cibernéticos sobre os hospitais e mostrará que eles põem em perigo os pacientes em toda a região."* A revisão do orientador:

| Problema | Por que falha | Revisão |
|---|---|---|
| "Investigar o impacto dos ataques cibernéticos sobre os hospitais" | Um tema, não uma pergunta; "impacto" não está definido. | Nomear o desfecho: chegadas diárias de ambulâncias e tempo de espera nos DEs vizinhos. |
| "Mostrar que eles põem em perigo os pacientes" | Pressupõe a resposta; um desenho para "mostrar" não pode falhar. | Perguntar "quanto" e permitir zero como resposta. |
| "Em toda a região" | Nenhuma unidade nem fronteira. | DEs num raio de 40 km do sistema atacado; a distância como moderador. |
| "Ataques cibernéticos" | Exposição não observável nem datada. | Desvio de ambulâncias causado por um ataque de ransomware, com início e fim registrados pelo EMS. |
| Nenhuma comparação | Um antes e depois sozinho não consegue separar o ataque da estação do ano. | Acrescentar uma região de comparação não afetada. |
| Nenhum mecanismo | Mesmo um número crível não diria aos planejadores o que mudar. | Pergunta explicativa secundária com entrevistas com as equipes do DE, do EMS e da coalizão. |
| "Os pacientes são postos em perigo" | Os desfechos dos pacientes exigem dados clínicos e aprovações além do cronograma de um mestrado. | Manter os desfechos dos pacientes fora do escopo; nomeá-los como trabalho futuro. |

Perguntas finais:

- **RQ1 (causal):** Durante um desvio de ambulâncias induzido por ransomware num sistema hospitalar, em que percentual variam as chegadas diárias de ambulâncias em cada DE vizinho em relação ao contrafactual estimado a partir de sua própria tendência pré-evento e de uma região de comparação não afetada?
- **RQ2 (associativa):** Essa variação diminui com a distância do sistema em desvio?
- **RQ3 (explicativa):** Segundo os gestores dos DEs, os supervisores do EMS e a equipe da coalizão, por meio de quais decisões e restrições a carga foi redistribuída?

### 1.9 Atividade prática: deduplicar, triar e medir a concordância

O laboratório abaixo contém uma exportação sintética de 20 registros de três bases e de uma busca na literatura cinzenta. Ele os deduplica em duas passadas, toma as decisões de dois revisores sobre títulos e resumos dos registros restantes, calcula o kappa e lista as discordâncias. Execute-o com o Python 3; nenhum pacote é necessário.

```python
# Lab 1 - deduplicate a synthetic search export, measure screening agreement, count the flow (offline)
# Each record: (source, title, year, doi_or_empty). Decisions: reviewer A and B, I = include, X = exclude.
import re

RECORDS = [
    ("medline", "Ransomware and emergency department crowding at neighbouring hospitals", 2023, "10.9999/syn.001"),
    ("scopus",  "Ransomware and Emergency Department Crowding at Neighbouring Hospitals.", 2023, "10.9999/SYN.001"),
    ("ieee",    "Anomaly detection for water distribution SCADA", 2019, "10.9999/syn.002"),
    ("medline", "Hospital IT downtime and laboratory turnaround times", 2021, ""),
    ("scopus",  "Hospital IT downtime and laboratory turn-around times", 2021, "10.9999/syn.003"),
    ("grey",    "After-action report: regional EMS diversion during a hospital network outage", 2022, ""),
    ("scopus",  "Ambulance diversion policies and patient outcomes: a review", 2018, "10.9999/syn.004"),
    ("medline", "Ambulance diversion policies and patient outcomes - a review", 2018, ""),
    ("ieee",    "Cyber-physical attack graphs for substations", 2020, "10.9999/syn.005"),
    ("grey",    "State health department memo on downtime procedures", 2024, ""),
    ("scopus",  "Interrupted time series of ED arrivals after hospital closure", 2017, "10.9999/syn.006"),
    ("medline", "Mortality after hospital cyberattacks in Medicare beneficiaries", 2024, "10.9999/syn.007"),
    ("scopus",  "Mortality after hospital cyberattacks in Medicare beneficiaries", 2024, "10.9999/syn.007"),
    ("ieee",    "A survey of ransomware families 2015-2022", 2022, "10.9999/syn.008"),
    ("grey",    "Regional healthcare coalition cyber-incident exercise report", 2023, ""),
    ("medline", "Stroke care times during regional diversion", 2020, "10.9999/syn.009"),
    ("scopus",  "Electronic health record downtime: a scoping review", 2022, "10.9999/syn.010"),
    ("medline", "Electronic Health Record Downtime: A Scoping Review", 2022, "10.9999/syn.010"),
    ("ieee",    "Blockchain for hospital supply chains", 2021, "10.9999/syn.011"),
    ("grey",    "Vendor white paper: ransomware readiness in hospitals", 2023, ""),
]

def norm_title(t):
    t = t.lower().replace("turn-around", "turnaround")
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return " ".join(t.split())

def key(rec):
    _, title, year, doi = rec
    return ("doi", doi.lower()) if doi else ("ty", norm_title(title), year)

seen, unique, dup = {}, [], 0
for rec in RECORDS:                       # pass 1: DOI or title+year
    k = key(rec)
    if k in seen:
        dup += 1
        continue
    seen[k] = rec
    unique.append(rec)
by_title = {}
final = []
for rec in unique:                        # pass 2: same normalized title+year, one record lacks a DOI
    tk = (norm_title(rec[1]), rec[2])
    if tk in by_title:
        dup += 1
        continue
    by_title[tk] = rec
    final.append(rec)

# Title/abstract screening decisions by two reviewers, in the order of `final`
A = "I X I I I X X I I X I I I X X".split()
B = "I X I I I X I I I X X I I X I".split()

def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return po, pe, (po - pe) / (1 - pe)

po, pe, k = kappa(A, B)
both = sum(x == y == "I" for x, y in zip(A, B))
disagree = [final[i][1] for i in range(len(final)) if A[i] != B[i]]
print(f"records identified: {len(RECORDS)}  duplicates removed: {dup}  screened: {len(final)}")
print(f"agreement po={po:.3f} pe={pe:.3f} kappa={k:.3f}")
print(f"both include: {both}  disagreements: {len(disagree)}")
for t in disagree:
    print("  resolve:", t)
```

Saída esperada:

```text
records identified: 20  duplicates removed: 5  screened: 15
agreement po=0.800 pe=0.533 kappa=0.571
both include: 8  disagreements: 3
  resolve: State health department memo on downtime procedures
  resolve: Regional healthcare coalition cyber-incident exercise report
  resolve: Vendor white paper: ransomware readiness in hospitals
```

Cinco duplicatas foram removidas: três pelo DOI (uma com o DOI em maiúsculas diferentes) e duas pelo título normalizado e pelo ano, incluindo um par que diferia apenas por "turn-around" versus "turnaround" e outro que diferia apenas por um travessão versus dois-pontos. A concordância bruta nos 15 registros triados é de 80%, mas a concordância ao acaso é de 53%, então κ = 0,571 — moderada, na melhor das hipóteses. O valor diagnóstico está na lista: **as três discordâncias são literatura cinzenta** (um memorando de um departamento estadual de saúde, um relatório de exercício de uma coalizão e um white paper de fornecedor). Os critérios nada diziam sobre a literatura cinzenta. Repare-os antes de continuar a triagem: por exemplo, incluir relatórios governamentais, de reguladores, de coalizões e pós-ação que descrevam os efeitos operacionais de um evento específico; excluir material de marketing de fornecedores e documentos que descrevam procedimentos sem relatar efeitos. Depois, trie de novo a amostra e recalcule o kappa.

### 1.10 Erros comuns e limites

- Começar com uma conclusão ("mostrar que…") em vez de uma pergunta que possa dar em qualquer direção.
- Fazer uma pergunta causal com um desenho que só consegue descrever.
- Deixar o estimando indefinido até a análise e então escolher a comparação que dá o maior efeito.
- Buscar na base de uma única disciplina e chamar o resultado de "a literatura".
- Ignorar a literatura cinzenta numa área em que auditorias, declarações de reguladores e relatórios pós-ação trazem boa parte das evidências — ou incluí-la sem critérios.
- Relatar a concordância bruta sem corrigir pelo acaso, ou relatar o kappa sem examinar onde está a discordância.
- Escrever a revisão autor por autor em vez de conceito por conceito.
- Tratar a constatação de um estudo como transferível sem registrar sua unidade, sua comparação e seu contexto.

O limite de uma revisão de mestrado é o tempo: ela não será exaustiva e não deve fingir que é. Sua credibilidade vem de uma busca documentada e repetível e de uma declaração honesta do que não foi buscado.

### Exercícios — capítulo 1

**EX001 — Do tema à pergunta.** *Objetivo:* estreitar um tema até uma pergunta respondível. *Insumos:* o tema "incidentes cibernéticos em concessionárias de água potável". *Restrições:* uma pergunta primária; uma exposição observável e datada; um desfecho em unidades de serviço. *Passos:* (1) declarar um problema que um tomador de decisão enfrenta; (2) escrever uma pergunta na forma PICOT para infraestrutura; (3) testá-la segundo cada critério FINER, numa frase; (4) declarar a alegação que você espera fazer e seu escopo. *Evidência esperada:* um memorando de meia página. *Rubrica:* 3 = pergunta respondível com dados plausíveis, exposição e desfecho observáveis, FINER aplicado com honestidade (incluindo o que não é viável), alegação delimitada ao desenho; 2 = um elemento vago; 1 = ainda um tema; 0 = nada.

**EX002 — Tipos de pergunta.** *Objetivo:* associar perguntas a desenhos e alegações. *Insumos:* (a) "Quantas horas de desvio de ambulâncias foram registradas no condado em 2024, por causa?" (b) "Os DEs que adotaram simulados de indisponibilidade têm tempos de espera menores durante as interrupções de TI?" (c) "Quanto o desvio aumentou as chegadas em Alder Point?" (d) "Por que os despachantes levaram pacientes com AVC para além do hospital aberto mais próximo?" (e) "O novo protocolo de desvio da coalizão reduziu o tempo em desvio?" *Restrições:* usar a tabela de §1.1.3. *Passos:* classificar cada uma; nomear o desenho mínimo; nomear a alegação mais forte. *Evidência esperada:* tabela. *Rubrica:* 3 = todas classificadas corretamente, com desenhos que de fato sustentariam as alegações, e (b) reconhecida como associativa, a menos que a adoção dos simulados possa ser tratada como uma exposição com um contrafactual crível; 2 = um erro; 1 = desenhos genéricos; 0 = nada.

**EX003 — Estratégia de busca e teste dos itens conhecidos.** *Objetivo:* construir uma busca documentada e interdisciplinar. *Insumos:* RQ1–RQ3 de §1.8. *Restrições:* três blocos de conceitos; pelo menos três fontes bibliográficas de disciplinas diferentes e um plano para a literatura cinzenta com pelo menos quatro tipos de fonte. *Passos:* (1) escrever os blocos; (2) listar as fontes e justificar cada uma; (3) definir um conjunto de três estudos conhecidos e descrever como você verificaria se cada um é recuperado; (4) definir uma regra de encerramento para o encadeamento de citações; (5) desenhar um modelo de registro de buscas. *Evidência esperada:* protocolo de uma página e modelo de registro. *Rubrica:* 3 = os blocos incluem sinônimos de várias disciplinas, a literatura cinzenta é especificada por tipo de fonte, o teste dos itens conhecidos e a regra de encerramento são concretos; 2 = falta um elemento; 1 = busca numa única disciplina; 0 = nada.

**EX004 — Deduplicação e concordância.** *Objetivo:* testar se a deduplicação pelo título detecta um registro quase duplicado da literatura cinzenta e ver como uma única discordância entre revisores move o kappa de Cohen. *Insumos:* código do Laboratório 1. *Restrições:* off-line. *Passos:* (1) executar o laboratório e registrar a saída; (2) acrescentar um registro `("grey", "Ransomware & emergency department crowding at neighbouring hospitals", 2023, "")` ao fim de `RECORDS`, acrescentar `I` às cadeias de decisões dos dois revisores (o registro só chega à triagem se a deduplicação deixá-lo passar), reexecutar e relatar se o procedimento em duas passadas o removeu, e por quê; (3) mudar a decisão do revisor B sobre "Cyber-physical attack graphs for substations" de X para I e relatar o novo kappa; (4) explicar em 100 palavras por que uma discordância a mais muda o kappa mais do que a concordância bruta sugere. *Evidência esperada:* saídas e explicação. *Rubrica:* 3 = saídas corretas, a falha do "e comercial" diagnosticada com uma correção proposta, kappa recalculado corretamente, correção pelo acaso explicada; 2 = um erro; 1 = não executado; 0 = nada.

**EX005 — Repare os critérios de elegibilidade.** *Objetivo:* transformar a discordância em critérios mais claros. *Insumos:* as três discordâncias do Laboratório 1. *Restrições:* os critérios precisam ser decidíveis a partir de um título e de um resumo ou da primeira página de um relatório. *Passos:* (1) escrever critérios de inclusão e exclusão para a literatura cinzenta; (2) aplicá-los aos três registros; (3) declarar o que você faria com um registro que ainda não consegue decidir. *Evidência esperada:* critérios e decisões. *Rubrica:* 3 = critérios decidíveis, decisões consistentes, registros indecidíveis enviados à revisão do texto completo em vez de excluídos; 2 = uma decisão inconsistente; 1 = os critérios repetem o tema; 0 = nada.

**EX006 — Matriz de conceitos.** *Objetivo:* sintetizar por conceito. *Insumos:* os três estudos de §1.6 mais o [relatório do NAO sobre o WannaCry e o NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) (outubro de 2017). *Restrições:* ler você mesmo o resumo do NAO; citar os números com sua fonte. *Passos:* (1) acrescentar o relatório do NAO como uma linha; (2) acrescentar uma coluna "rivais que o estudo levanta ou deixa em aberto"; (3) escrever um parágrafo de 200 palavras, centrado em conceitos, sobre os "efeitos regionais dos incidentes cibernéticos em hospitais". *Evidência esperada:* matriz e parágrafo. *Rubrica:* 3 = linha do NAO acurada (escopo da interrupção e a distinção entre cancelamentos registrados e estimados), rivais específicos, parágrafo organizado por conceito; 2 = parágrafo autor por autor; 1 = números sem fonte; 0 = nada.

**EX007 — Memorando do estimando e do escopo.** *Objetivo:* definir exatamente o que será estimado. *Insumos:* RQ1 e RQ2. *Restrições:* o modelo de cinco partes de §1.2. *Passos:* (1) escrever o estimando de RQ1; (2) escrever um para RQ2; (3) listar dois estimandos que um analista descuidado poderia calcular em vez deles e por que diferem; (4) declarar a alegação esperada e as alegações explicitamente fora do escopo. *Evidência esperada:* uma página. *Rubrica:* 3 = estimandos inequívocos, com um contraste contrafactual, alternativas genuinamente diferentes (por exemplo, o aumento no primeiro dia, o aumento em relação ao ano anterior), alegações fora do escopo explícitas; 2 = um estimando ambíguo; 1 = sem contraste; 0 = nada.

### Síntese do capítulo

Uma dissertação se apoia em sua pergunta. Passe do tema ao problema e à pergunta deliberadamente, tornando cada estreitamento defensável; teste a pergunta segundo o FINER e escreva-a numa forma PICOT para infraestrutura, com uma exposição observável e um desfecho de consequência. Classifique a pergunta, porque seu tipo decide o desenho e a alegação mais forte disponível. Defina o estimando antes de ver os dados. Escolha um tipo de revisão que se ajuste ao projeto e diga isso. Busque entre disciplinas e na literatura cinzenta, teste a busca com itens conhecidos, encadeie as citações até um ponto de encerramento declarado com antecedência e registre tudo. Deduplique, trie com um segundo revisor pelo menos numa amostra, use o kappa como diagnóstico de critérios pouco claros e relate o fluxo. Sintetize por conceito: a matriz de conceitos mostra tanto o que se sabe quanto a lacuna que o seu estudo vai preencher.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 08

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestrutura crítica e segurança setorial: seminário avançado

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Descrever, para cada setor principal, sua unidade de consequência característica, suas reservas, seus instrumentos de governança e as evidências que um pesquisador de mestrado pode obter de forma realista.
2. Distinguir as **cascatas de dependências** (um fornecedor falha e seus dependentes falham depois de suas reservas) do **transbordamento por transferência de carga** (os pares absorvem a demanda de uma unidade que falhou), e reconhecer qual delas um estudo mede.
3. Tratar os catálogos públicos de incidentes como dados com um processo de seleção e quantificar como uma divulgação que cresce com a gravidade infla a gravidade aparente e como uma mudança nas regras de notificação cria uma tendência espúria.
4. Codificar incidentes cujo primeiro relato público foi depois revisado, sem repetir o primeiro relato nem apagá-lo.
5. Ler um artigo setorial com um protocolo crítico fixo e apresentá-lo num seminário de modo que a discussão seja sobre evidências, e não sobre opiniões.

Este capítulo amplia o mapa de evidências construído no Capítulo 1 de um setor para a área. O [capítulo de fronteira da pesquisa](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md#ch-02) do livro de doutorado examina as normas como hipóteses e as famílias de modelos de interdependência; este seminário não repete esse exame. Ele se concentra no que um pesquisador iniciante precisa: como os setores diferem nas consequências que produzem e nas evidências que deixam, como ler as evidências que existem e como discuti-las com os colegas.

### 2.1 Para que serve o seminário

Um seminário de pesquisa treina três hábitos de que uma dissertação precisa e que as aulas expositivas não treinam: ler um artigo pelo que ele pode sustentar, apresentar com justiça o trabalho de outra pessoa antes de criticá-lo e aceitar críticas à sua própria leitura. Cada sessão deste curso segue o mesmo protocolo, que você vai reutilizar ao escrever a revisão da literatura do Capítulo 7:

1. **Alegação.** O que o artigo alega, com que escopo? Cite a frase.
2. **Evidências.** Que dados, de quais unidades, em que período?
3. **Garantia.** Por que essas evidências sustentam essa alegação — que lógica de desenho as liga?
4. **Rivais.** O que mais poderia ter produzido as mesmas evidências? Quais rivais o artigo trata, e como?
5. **Transferência.** A quais outras unidades, setores ou jurisdições o resultado poderia se aplicar, e sob quais condições?
6. **E daí.** Que decisão ou estudo posterior ele informa?
7. **Próximo estudo.** Que estudo único mais reduziria a incerteza restante?

O apresentador responde às perguntas 1–3 e 5–6 nos termos do próprio artigo e depois abre as perguntas 4 e 7 ao grupo. A crítica a um artigo publicado não é um veredito sobre seus autores; a maioria das limitações decorre dos dados que existiam.

### 2.2 Perfis setoriais

Os setores diferem no que se perde, com que rapidez e para quem, em quem os regula e em quais evidências chegam ao registro público. Os perfis a seguir são um ponto de partida; cada instrumento é citado com sua versão e data e deve ser verificado de novo antes que você se apoie nele.

| Setor | Unidade de consequência típica | Reservas principais | Exemplos de instrumentos de governança | Evidências que um estudante de mestrado geralmente consegue obter | Caso público discutido neste livro |
|---|---|---|---|---|---|
| Saúde | Pacientes atrasados, desviados ou prejudicados; procedimentos e consultas adiados | Procedimentos de indisponibilidade, prontuários em papel, pessoal, ajuda mútua regional, capacidade de outros hospitais | As [HPH Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html) dos EUA (voluntárias, janeiro de 2024); a saúde é um setor da [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) na UE | Dados agregados de atividade (com aprovação), declarações públicas, auditorias, entrevistas | Dameff et al. (2023); WannaCry e o NHS; Synnovis (2024); Change Healthcare (2024) |
| Energia — eletricidade | Clientes e clientes-hora sem energia; cargas críticas perdidas | Geradores, armazenamento, operação manual, manobras | [Normas CIP da NERC](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) (obrigatórias para o sistema elétrico de grande porte da América do Norte); setor de energia da NIS2 | Estatísticas de interrupções, relatórios pós-ação públicos; raramente dados operacionais | Ucrânia, 2015 (ver o livro de doutorado, Capítulo 1) |
| Energia — petróleo e gás, dutos | Produto não entregue; desabastecimento | Estoques, transporte alternativo | Diretivas de segurança de dutos emitidas pela Transportation Security Administration dos EUA após o Colonial Pipeline, conforme descrito pela [CISA (2023)](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years) | Cronologias públicas, relatórios de situação das agências de energia, dados de preço e de abastecimento | Colonial Pipeline (2021) |
| Água | Pessoas sem água segura ou sem pressão; avisos emitidos | Armazenamento, dosagem manual, interconexões | O [America's Water Infrastructure Act of 2018](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans) dos EUA, que exige que os sistemas comunitários de água que atendem mais de 3.300 pessoas concluam avaliações de risco e resiliência e planos de resposta a emergências | Avisos à população, resumos dos reguladores, levantamentos com concessionárias pequenas | Oldsmar (2021) e sua revisão posterior |
| Finanças | Transações não processadas; liquidação atrasada; clientes impossibilitados de pagar | Processamento manual, sites de contingência, canais alternativos de pagamento | O [Digital Operational Resilience Act, Regulamento (UE) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), da UE; a [orientação do CPMI–IOSCO](https://www.bis.org/cpmi/publ/d146.htm) (junho de 2016) para as infraestruturas do mercado financeiro | Publicações de supervisão, estatísticas agregadas; dados das empresas quase nunca | A interrupção de pagamentos e de faturamento de convênios da Change Healthcare (2024), onde saúde e finanças se encontram |
| Comunicações e TI compartilhada | Usuários ou organizações sem serviço; serviços dependentes degradados | Enlaces redundantes, procedimentos de contingência | Regras setoriais de telecomunicações; as [CPGs intersetoriais da CISA](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) | Declarações dos provedores, relatórios de interrupção | A atualização defeituosa de software de segurança de julho de 2024 (não maliciosa) |
| Serviços públicos e de emergência | Chamadas não atendidas, respostas atrasadas | Centrais de despacho vizinhas, despacho manual | Regras nacionais de comunicações de emergência; a [CER](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) e a NIS2 na UE | Agregados do despacho e do EMS, relatórios pós-ação | O desvio do EMS do condado relatado por Dameff et al. (2023) |

Duas características da tabela importam para o desenho da pesquisa. Primeiro, a **unidade de consequência** difere por setor, então um estudo intersetorial que compara o "impacto" sem uma unidade comum está comparando coisas incomensuráveis; escolha uma unidade funcional comum (pessoas sem um serviço por uma duração declarada) ou fique dentro de um setor. Segundo, a **disponibilidade das evidências** é inversamente relacionada à sensibilidade: os setores cujos dados operacionais responderiam às melhores perguntas são os que menos provavelmente os liberam. Um projeto de mestrado realista escolhe uma pergunta que dados agregados, públicos ou consentidos consigam responder.

### 2.3 Como os incidentes setoriais se tornam regionais

#### 2.3.1 Dois mecanismos de propagação

O livro de doutorado modela as **cascatas de dependências**: um fornecedor falha, e cada dependente falha quando sua reserva se esgota — um hospital perde a pressão da água horas depois que uma estação de tratamento perde a energia. O Spillover Study mede um mecanismo diferente, o **transbordamento por transferência de carga**: uma unidade falha ou se retira, e sua demanda passa para pares que não falharam. As ambulâncias desviadas do Kestrel chegam a Alder Point; os pacientes que não conseguem aviar uma receita numa farmácia vão a outra; os clientes de um processador de pagamentos que falhou fazem fila nos bancos. A transferência de carga é muitas vezes mais rápida do que uma cascata de dependências (ela começa assim que a unidade se retira) e é limitada pela **capacidade ociosa** dos pares, e não pelas reservas.

| Característica | Cascata de dependências | Transbordamento por transferência de carga |
|---|---|---|
| Caminho | Fornecedor → dependente | Unidade que falhou → pares |
| Temporização | Depois que a reserva do dependente se esgota | Imediatamente, na retirada |
| Fator limitante | Tamanho da reserva e tempo de restauração | Capacidade ociosa dos pares e distância |
| Medição típica | Tempo até o impacto, horas de serviço perdidas | Demanda excedente nos pares, tempos de espera, recusas |
| Exemplo em fontes públicas | A paralisação do Colonial Pipeline e seus efeitos na distribuição de combustível ([U.S. Department of Energy](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident)) | Aumento de volume nos DEs adjacentes a um sistema atacado ([Dameff et al., 2023](https://doi.org/10.1001/jamanetworkopen.2023.12270)) |

Os eventos reais geralmente envolvem os dois. Durante o ataque de ransomware ao laboratório de patologia Synnovis, em junho de 2024, a dependência eram os serviços laboratoriais de que os hospitais dependiam; o [NHS England relatou](https://www.england.nhs.uk/london/2024/06/14/update-on-cyber-incident-clinical-impact-in-south-east-london-friday-14-june-2024/) que, na primeira semana (3–9 de junho), o King's College Hospital e o Guy's and St Thomas' adiaram 814 procedimentos eletivos e 861 consultas ambulatoriais hospitalares e comunitárias, e o trabalho foi redirecionado para outros prestadores — transferência de carga. Uma dissertação deve nomear qual mecanismo ela mede, porque o desenho, o desfecho e as implicações para as políticas diferem.

#### 2.3.2 Concentração e serviços compartilhados

Quando muitas organizações dependem de um único prestador de serviço, um incidente no prestador se torna simultâneo em todas elas. O [levantamento da AHA](https://www.aha.org/2024-03-15-aha-survey-change-healthcare-cyberattack-significantly-disrupts-patient-care-hospitals-finances) com quase 1.000 hospitais, em março de 2024, relatou que 94% sofreram um impacto financeiro do ataque cibernético à Change Healthcare, que interrompeu o faturamento de convênios e o processamento de pagamentos. Um exemplo não malicioso mostra o mesmo ponto estrutural: a Microsoft [estimou](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/) que uma atualização defeituosa de software de segurança em julho de 2024 afetou 8,5 milhões de dispositivos Windows — menos de um por cento de todas as máquinas Windows —, mas interrompeu serviços amplamente porque as máquinas afetadas estavam concentradas em empresas que operavam serviços críticos. Para os pesquisadores, os incidentes de concentração são experimentos naturais com muitas unidades expostas simultaneamente, mas pode não haver nenhum grupo de comparação não exposto do mesmo tipo.

### 2.4 Os catálogos públicos de incidentes são amostras, e não populações

A maior parte das evidências intersetoriais vem de catálogos montados a partir de relatos públicos: notícias, notificações regulatórias de violações, declarações de empresas e alertas de agências. [Neprash et al. (2022)](https://doi.org/10.1001/jamahealthforum.2022.4873) construíram uma base desse tipo para os ataques de ransomware às organizações prestadoras de cuidados de saúde dos EUA e relataram 374 ataques de 2016 a 2021, uma contagem anual que mais do que dobrou, de 43 para 91, e interrupção operacional em 44,4% dos ataques, incluindo desvio de ambulâncias em 16 (4,3%). Os autores enquadram suas contagens como ataques que se tornaram publicamente conhecidos. Esse enquadramento importa, porque o conteúdo de um catálogo é moldado por dois processos que nada têm a ver com a incidência verdadeira:

1. **Divulgação dependente da gravidade.** Interrupções longas e visíveis têm mais probabilidade de ser relatadas do que as curtas, absorvidas internamente. A gravidade média do catálogo é, portanto, maior do que a da população.
2. **Mudanças nas regras de notificação e na atenção.** Uma nova obrigação de notificação, uma mudança na prática de publicação de um regulador ou um surto de atenção da mídia aumentam a fração de incidentes que se tornam públicos. As contagens sobem mesmo que a incidência não suba.

Nenhum dos dois processos torna os catálogos inúteis. Eles os tornam adequados para algumas perguntas (que tipos de interrupção ocorreram; que características aparecem entre os eventos relatados; como os eventos relatados mudaram após uma regra) e inadequados para outras (com que frequência os incidentes ocorrem; quão grave é um incidente típico; se a incidência está aumentando), a menos que o processo de divulgação seja modelado. O Laboratório 2 mostra o tamanho das duas distorções numa população sintética.

### 2.5 Quando o primeiro relato é revisado

Os registros públicos de incidentes de infraestrutura são revisados à medida que as investigações avançam. Dois casos documentados mostram por que um pesquisador precisa registrar **o que foi alegado, por quem, quando e como isso foi depois revisado**.

- **Oldsmar, Flórida, fevereiro de 2021.** As primeiras declarações públicas descreveram um invasor remoto elevando o ponto de ajuste do hidróxido de sódio numa estação de tratamento de água, e a CISA emitiu um alerta conjunto, o [AA21-042A, "Compromise of U.S. Water Treatment Facility"](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Em abril de 2023, o então administrador municipal disse que o FBI havia concluído que o incidente provavelmente tinha sido causado por um funcionário, e um porta-voz do FBI disse que a investigação "não conseguiu confirmar que este incidente foi iniciado por uma intrusão cibernética direcionada" ([WUSF, 13 de abril de 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). O incidente ainda aparece em muitas listas de ataques cibernéticos ao setor de água.
- **Düsseldorf, Alemanha, setembro de 2020.** Um ataque de ransomware perturbou o hospital universitário, uma paciente foi levada a um hospital mais distante e morreu, e o Ministério Público abriu uma investigação por homicídio culposo que atraiu atenção mundial como possivelmente a primeira morte causada por ransomware. Em novembro de 2020, o Ministério Público concluiu que o atraso não foi decisivo para o desfecho ([MIT Technology Review, 12 de novembro de 2020](https://www.technologyreview.com/2020/11/12/1012015/ransomware-did-not-kill-a-german-hospital-patient/)).

Nenhuma das revisões mostra que o risco subjacente é imaginário. Ambas mostram que um catálogo que codifica o primeiro relato como fato — "intrusão cibernética numa estação de água", "morte causada por ransomware" — contém erros que se propagam para toda análise que o usa. Um esquema de codificação sólido armazena, para cada incidente, a alegação, sua fonte, o tipo de fonte (oficial, empresa, mídia), a data da alegação, a situação atual (confirmada, contestada, revisada, desconhecida) e a data da última verificação. Uma fonte secundária que repete o primeiro relato não é uma confirmação independente dele.

### 2.6 Lendo um artigo setorial: um seminário resolvido

O protocolo do seminário (§2.1) aplicado a [Dameff et al. (2023)](https://doi.org/10.1001/jamanetworkopen.2023.12270), usando apenas o que o resumo e o artigo publicados declaram:

1. **Alegação.** Os hospitais adjacentes a organizações prestadoras de cuidados de saúde sob ataque de ransomware "podem ver aumentos no censo de pacientes e podem enfrentar restrições de recursos que afetam o atendimento sensível ao tempo", e esses ataques devem ser considerados um desastre regional.
2. **Evidências.** Dois DEs acadêmicos urbanos no condado de San Diego; 19.857 atendimentos no DE; três fases de quatro semanas em torno de um ataque a uma organização distinta, iniciado em 1º de maio de 2021: antes (3–30 de abril), ataque e recuperação (1–28 de maio), depois (29 de maio–25 de junho). A organização atacada respondia por cerca de um quarto das altas hospitalares da região.
3. **Garantia.** Se nada mais mudou entre as fases, as diferenças entre as fases estão associadas ao ataque.
4. **Rivais (para o grupo).** A mudança sazonal de abril para junho; a situação da COVID-19 em evolução na primavera de 2021; outros eventos regionais; muitos desfechos comparados, o que aumenta a chance de que algumas diferenças surjam por acaso. O desenho compara as fases dentro dos mesmos DEs; ele não inclui uma região de comparação não afetada, que é o principal acréscimo que um estudo de seguimento poderia fazer.
5. **Transferência.** Para regiões em que uma organização detém uma grande parcela da capacidade, de modo que sua retirada desloca uma carga substancial; menos para regiões com muitos prestadores pequenos.
6. **E daí.** O planejamento regional para desastres cibernéticos, a ajuda mútua e os protocolos de desvio do EMS — a própria conclusão do artigo — e a justificativa para medir os efeitos regionais em outros eventos.
7. **Próximo estudo.** Um desenho controlado: os mesmos desfechos em DEs comparáveis não afetados nas mesmas semanas, mais um gradiente de distância. Esse é o desenho do Spillover Study.

Observe o tom. O artigo fez a primeira medição publicada de um efeito regional; a crítica do seminário identifica o que um *próximo* estudo pode acrescentar, e não o que os autores "erraram".

### 2.7 Apresentando no seminário

Uma apresentação de dez minutos tem uma forma fixa: um slide para a pergunta e por que ela importa; um para o desenho (unidades, exposição, comparação, desfecho, período); um para o resultado principal nas palavras dos autores, com sua incerteza; um para o que o desenho descarta e o que deixa em aberto; um para o próximo estudo. Coloque os rivais no slide como perguntas, e não como acusações. Ao ser questionado, separe três tipos de resposta: "o artigo diz…", "eu infiro…" e "não sei; isso exigiria…". Os mesmos três registros vão servir na defesa oral (Capítulo 8).

### 2.8 Exemplo resolvido: uma contradição aparente (exercício do seminário)

No seminário, um participante objeta: "Ghafur et al. constataram que o WannaCry *reduziu* a atividade hospitalar, e o NHS não viu aumento nos óbitos; Dameff et al. constataram que o ransomware *aumentou* a atividade. As evidências se contradizem." O seminário resolve a questão com a matriz de conceitos:

| Dimensão | [Ghafur et al., 2019](https://doi.org/10.1038/s41746-019-0161-6) | [Dameff et al., 2023](https://doi.org/10.1001/jamanetworkopen.2023.12270) |
|---|---|---|
| Unidades medidas | Trusts infectados (e todos os trusts) | DEs não afetados adjacentes à organização atacada |
| Direção esperada | As unidades infectadas fazem menos (consultas canceladas, menos internações) | Os vizinhos absorvem a demanda deslocada |
| Sistema de saúde | NHS inglês, maio de 2017 | Condado de San Diego, maio de 2021 |
| Duração | Uma semana de perturbação aguda | Ataque e recuperação de um mês |
| Desfecho de dano | Óbitos em A&E: nenhuma variação detectável, descrita pelos autores como uma medida grosseira | Métricas do atendimento ao AVC e tempos de processo |

As constatações são complementares: a atividade de uma unidade atacada cai e a de seus vizinhos sobe. Juntas, elas sugerem o mecanismo do Spillover Study. O resultado "nenhuma variação na mortalidade" também não é evidência de ausência de dano; é a ausência de variação detectada num desfecho grosseiro ao longo de uma semana. A [investigação do NAO](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) acrescenta o escopo: pelo menos 81 dos 236 trusts da Inglaterra foram afetados, junto com 603 organizações de atenção primária e outras do NHS, e o NHS England registrou 6.912 consultas canceladas, ao mesmo tempo em que estimou que mais de 19.000 foram canceladas no total — um lembrete de que as contagens registradas e os totais estimados são quantidades diferentes.

### 2.9 Atividade prática: o que um catálogo faz com a gravidade e a tendência

O laboratório cria uma população sintética de 2.400 incidentes que interrompem serviços, 400 por ano durante seis anos, de modo que a incidência verdadeira é constante. As durações das interrupções são log-normais, com mediana de 6 horas. Cada incidente é divulgado com uma probabilidade que cresce com a duração (50% em 24 horas), e uma obrigação de notificação a partir do ano 4 multiplica a divulgação por 1,8.

```python
# Lab 2 - what a public incident catalogue does to severity and trend (offline, standard library only)
# Synthetic population of service-disrupting incidents over six years. Each has an outage duration (hours).
# Disclosure probability rises with duration; a reporting mandate raises disclosure from year 4.
import math, random

rng = random.Random(42)
TRUE_PER_YEAR = 400                      # constant true incidence: there is NO real trend

def p_report(hours, year):
    base = 1 / (1 + math.exp(-(math.log(hours) - math.log(24)) * 1.5))   # 50% at 24 h
    return min(1.0, base * (1.0 if year < 4 else 1.8))                   # mandate from year 4

pop = []
for year in range(1, 7):
    for _ in range(TRUE_PER_YEAR):
        hours = rng.lognormvariate(math.log(6), 1.2)                       # median 6 h
        pop.append((year, hours, rng.random() < p_report(hours, year)))

def summary(rows):
    h = sorted(r[1] for r in rows)
    n = len(h)
    med = h[n // 2] if n % 2 else (h[n // 2 - 1] + h[n // 2]) / 2
    return n, sum(h) / n, med, sum(x > 24 for x in h) / n

print("set           n     mean_h  median_h  share>24h")
for label, rows in (("population", pop), ("catalogue", [r for r in pop if r[2]])):
    n, mean, med, big = summary(rows)
    print(f"{label:12} {n:5d}  {mean:7.1f}  {med:8.1f}  {big:9.2f}")
print("year  true  catalogued")
for y in range(1, 7):
    print(f"{y:4d}  {sum(r[0] == y for r in pop):4d}  {sum(r[0] == y and r[2] for r in pop):10d}")
```

Saída esperada:

```text
set           n     mean_h  median_h  share>24h
population    2400     12.8       6.1       0.13
catalogue      646     29.2      18.4       0.40
year  true  catalogued
   1   400          99
   2   400          73
   3   400          90
   4   400         125
   5   400         133
   6   400         126
```

Leia as duas tabelas. A interrupção média do catálogo (29,2 h) é mais que o dobro da da população (12,8 h); sua mediana é três vezes maior; e a parcela de incidentes com mais de 24 horas sobe de 13% para 40%. Um estudo que descrevesse os incidentes "típicos" a partir do catálogo os exageraria muito. As contagens anuais mostram um degrau de cerca de 87 por ano para cerca de 128 por ano após a obrigação — um "aumento" de 47% numa população cuja incidência nunca mudou. Uma análise honesta de um catálogo ou se restringe às perguntas que a seleção não distorce, ou modela o processo de divulgação com pressupostos declarados, ou usa um denominador externo (por exemplo, todos os incidentes notificados sob uma obrigação de completude conhecida).

### 2.10 Erros comuns e limites

- Comparar o "impacto" entre setores sem uma unidade de consequência comum.
- Confundir as cascatas de dependências com o transbordamento por transferência de carga e, por isso, medir o desfecho errado.
- Tratar as contagens de um catálogo público como incidência, ou as médias do catálogo como a gravidade típica.
- Ler um aumento nos incidentes notificados após uma obrigação como um aumento nos ataques.
- Codificar um relato público inicial como fato e nunca revisitá-lo.
- Tratar uma fonte secundária que repete um primeiro relato como confirmação independente.
- Criticar um artigo por não fazer o que seus dados nunca poderiam sustentar, em vez de identificar o próximo estudo.
- Tratar "nenhuma variação detectada" num desfecho grosseiro como evidência de ausência de efeito.

O limite de um seminário é que ele lê apenas o que foi publicado. As evidências não publicadas — incidentes nunca divulgados, dados operacionais nunca liberados — ficam fora dele, e o seminário deve dizer isso em vez de presumir que o registro publicado é completo.

### Exercícios — capítulo 2

**EX008 — Perfil setorial.** *Objetivo:* traçar o perfil de um setor como cenário de pesquisa. *Insumos:* a tabela de §2.2. *Restrições:* escolher um setor que não seja a saúde; citar pelo menos duas fontes primárias para seus instrumentos e um caso público documentado. *Passos:* (1) definir a unidade de consequência; (2) listar as reservas; (3) nomear os instrumentos de governança, com versão e data; (4) listar as evidências que um estudante de mestrado poderia obter licitamente; (5) propor uma pergunta respondível que essas evidências possam sustentar. *Evidência esperada:* perfil de uma página. *Rubrica:* 3 = unidade de consequência precisa, instrumentos citados com exatidão, evidências realistas, pergunta ajustada às evidências; 2 = um elemento vago; 1 = sem citações; 0 = nada.

**EX009 — Distorção do catálogo.** *Objetivo:* separar o viés de tendência que uma obrigação de notificação cria do viés de gravidade que a divulgação seletiva cria num catálogo de incidentes. *Insumos:* código do Laboratório 2. *Restrições:* off-line; não mudar a semente. *Passos:* (1) executar o laboratório e registrar a saída; (2) definir o multiplicador da obrigação como 1,0 e relatar a média, a mediana, a parcela acima de 24 horas e as contagens anuais do catálogo; (3) explicar por que a distorção da gravidade persiste sem a obrigação; (4) propor uma pergunta que este catálogo *consegue* responder sem modelar a divulgação. *Evidência esperada:* saídas e dois parágrafos. *Rubrica:* 3 = saídas corretas, distorção da gravidade atribuída à divulgação dependente da gravidade, distorção da tendência atribuída à obrigação, uma pergunta respondível defensável; 2 = falta uma explicação; 1 = não executado; 0 = nada.

**EX010 — Protocolo do seminário.** *Objetivo:* aplicar o protocolo de sete perguntas. *Insumos:* [Ghafur et al. (2019)](https://doi.org/10.1038/s41746-019-0161-6). *Restrições:* usar apenas o que o artigo declara; citar sua alegação. *Passos:* responder às sete perguntas de §2.1; marcar quais rivais o artigo trata, e como. *Evidência esperada:* uma página. *Rubrica:* 3 = alegação citada, desenho descrito com acurácia (fonte de dados, comparação, desfechos), rivais específicos, próximo estudo viável; 2 = uma pergunta rala; 1 = opinião em vez de evidências; 0 = nada.

**EX011 — Classificação do mecanismo.** *Objetivo:* distinguir os mecanismos de propagação. *Insumos:* (a) a paralisação do Colonial Pipeline e seus efeitos no abastecimento de combustível (página do DOE); (b) a Synnovis e os procedimentos adiados (NHS England); (c) a Change Healthcare e o fluxo de caixa dos hospitais (AHA); (d) o desvio do Kestrel e as chegadas em Alder Point (sintético). *Restrições:* usar §2.3.1. *Passos:* classificar cada um como cascata de dependências, transbordamento por transferência de carga ou ambos; nomear a unidade de consequência; nomear o fator limitante. *Evidência esperada:* tabela. *Rubrica:* 3 = classificações justificadas, "ambos" reconhecido onde a substituição se segue à falha de uma dependência, fatores limitantes específicos; 2 = uma classificação errada; 1 = sem justificativa; 0 = nada.

**EX012 — Codificando um incidente revisado.** *Objetivo:* desenhar uma entrada de catálogo que sobreviva à revisão. *Insumos:* as fontes sobre Oldsmar em §2.5. *Restrições:* no mínimo os campos de §2.5. *Passos:* (1) escrever a entrada como ela estaria em março de 2021; (2) atualizá-la para abril de 2023; (3) declarar como uma análise que conta as "intrusões confirmadas em concessionárias de água" deve tratar a entrada; (4) declarar como você verificaria a situação da entrada antes de usá-la em 2026. *Evidência esperada:* duas entradas e um parágrafo. *Rubrica:* 3 = as duas entradas preservam a fonte, a data e a situação, regra de análise explícita, procedimento de nova verificação concreto; 2 = histórico perdido na atualização; 1 = a entrada afirma uma causa; 0 = nada.

**EX013 — Contradição aparente.** *Objetivo:* resolver constatações que parecem conflitantes. *Insumos:* as alegações "o WannaCry reduziu a atividade nos trusts infectados do NHS" e "o ransomware aumentou o volume nos DEs vizinhos em San Diego". *Restrições:* usar uma matriz de conceitos com pelo menos cinco dimensões. *Passos:* (1) construir a matriz; (2) declarar se as constatações conflitam; (3) declarar que estudo único poderia testar o mecanismo combinado. *Evidência esperada:* matriz e parágrafo. *Rubrica:* 3 = unidades e direção distinguidas, limitação da medida de dano observada, estudo combinado que mede tanto as unidades atacadas quanto as vizinhas; 2 = falta uma dimensão; 1 = afirma uma contradição; 0 = nada.

**EX014 — Apresentação no seminário.** *Objetivo:* apresentar um artigo com justiça. *Insumos:* um artigo setorial publicado, de sua escolha, com um resultado quantitativo. *Restrições:* cinco slides como em §2.7; rivais apresentados como perguntas. *Passos:* (1) preparar os slides; (2) escrever três perguntas que você espera e suas respostas nos três registros ("o artigo diz", "eu infiro", "não sei; isso exigiria"); (3) depois de apresentar aos colegas, registrar um ponto em que a sua leitura mudou. *Evidência esperada:* roteiro dos slides, folha de perguntas e reflexão. *Rubrica:* 3 = resumo justo antes da crítica, rivais precisos, registros usados corretamente, reflexão honesta; 2 = a crítica precede o resumo; 1 = baseada em opinião; 0 = nada.

### Síntese do capítulo

Os setores diferem no que perdem, com que rapidez e para quem; em quem os governa; e em quais evidências chegam à vista do público. Escolha uma unidade de consequência comum ou fique dentro de um setor. Distinga as cascatas de dependências do transbordamento por transferência de carga e meça o mecanismo que você alega. Os catálogos públicos são amostras moldadas pela divulgação dependente da gravidade e pelas mudanças nas regras de notificação: suas médias exageram a gravidade típica e suas tendências podem ser artefatos. Os relatos públicos iniciais são revisados — Oldsmar e Düsseldorf são exemplos documentados —, então codifique as alegações com fonte, data e situação, e verifique-as de novo antes de usá-las. Leia os artigos com um protocolo fixo, resuma com justiça antes de criticar e transforme a crítica no desenho do próximo estudo.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 08

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Desenho do estudo, ética e reprodutibilidade

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Comparar os desenhos disponíveis para uma pergunta causal sobre um evento de infraestrutura não planejado — antes e depois, série temporal interrompida, série temporal interrompida controlada, diferença em diferenças, controle sintético, estudo de caso e métodos mistos — e escolher um pelos pressupostos de que precisa e pelos dados que exige.
2. Nomear as principais ameaças à validade interna, de construto, de conclusão estatística e externa, e associar cada uma a uma característica do desenho que a reduza.
3. Executar uma **análise do desenho** antes do acesso aos dados: estimar quão grande precisa ser um efeito para que o desenho planejado o detecte e quão enviesado seria um desenho mais simples.
4. Preparar uma submissão ao comitê de ética para um estudo que combina dados operacionais agregados e entrevistas, incluindo os riscos para os funcionários, as organizações e o público, e as salvaguardas de sensibilidade da informação.
5. Especificar acordos de dados e um plano de gestão de dados proporcionais à sensibilidade dos dados.
6. Montar um projeto reprodutível — estrutura, ambiente, sementes, livro de códigos, controle de versões e um plano de pré-análise registrado — antes que cheguem os primeiros dados.

O capítulo transforma o estimando do Capítulo 1 num desenho. O Capítulo 4 examina as explicações rivais que o desenho precisa derrotar; o Capítulo 5 testa a viabilidade; o Capítulo 6 executa a análise especificada aqui.

### 3.1 Desenhos para um evento que ninguém atribuiu

#### 3.1.1 O problema central

Um ataque de ransomware não é um experimento: ninguém o atribuiu aleatoriamente ao Kestrel nem escolheu o seu momento para ajudar os pesquisadores. Todo desenho para o Spillover Study é, portanto, uma forma de **aproximar o contrafactual** — como teriam sido as chegadas em Alder Point sem o desvio — a partir dos dados que existem. Os desenhos diferem em onde encontram essa aproximação e nos pressupostos que a tornam válida.

| Desenho | O contrafactual vem de | Pressuposto-chave | Dados necessários | Principal fraqueza |
|---|---|---|---|---|
| Antes e depois | O nível das mesmas unidades antes do evento | Nada mais mudou entre os períodos | Algumas semanas antes e durante | Confundido pela estação do ano, pelas tendências e por eventos simultâneos |
| Série temporal interrompida (ITS) | A tendência pré-evento das mesmas unidades, projetada para a frente | A tendência pré-evento teria continuado; nenhum choque simultâneo | Muitos pontos no tempo antes e depois ([Wagner et al., 2002](https://doi.org/10.1046/j.1365-2710.2002.00430.x); [Lopez Bernal et al., 2017](https://doi.org/10.1093/ije/dyw098)) | Um choque simultâneo (uma epidemia, uma mudança de política) é atribuído ao evento |
| ITS controlada / diferença em diferenças | A tendência pré-evento mais a variação simultânea nas unidades de comparação não expostas | As unidades tratadas e de comparação teriam variado da mesma forma ("tendências paralelas") | Séries temporais das unidades tratadas e de comparação | Falha se a região de comparação sofrer um choque diferente ([Roth et al., 2023](https://doi.org/10.1016/j.jeconom.2023.03.008)) |
| Controle sintético | Uma combinação ponderada de muitas unidades não expostas que reproduz a trajetória pré-evento da unidade tratada | A combinação ponderada teria acompanhado a unidade sem o evento | Muitas unidades doadoras potenciais e um período prévio longo ([Abadie, 2021](https://doi.org/10.1257/jel.20191450)) | Poucos doadores numa região; ajuste ruim no período prévio |
| Estudo de caso / rastreamento de processos | Relatos do que aconteceu e por quê | Relatos convergentes e independentes | Documentos, entrevistas, registros | Não consegue quantificar um tamanho de efeito por si só |
| Métodos mistos | Estimativa quantitativa mais evidências de processo | Cada vertente válida em seus próprios termos; integração explícita | Ambos os anteriores ([Fetters et al., 2013](https://doi.org/10.1111/1475-6773.12117)) | O dobro do trabalho; a integração muitas vezes fica implícita |

Se o estudo agregar vários eventos em momentos diferentes — por exemplo, ataques a diferentes sistemas hospitalares em anos diferentes —, a diferença em diferenças padrão com efeitos fixos bidirecionais pode dar pesos enganosos a algumas comparações; [Goodman-Bacon (2021)](https://doi.org/10.1016/j.jeconom.2021.03.014) decompõe o estimador e Roth et al. (2023) examinam as alternativas. Um estudo de mestrado de um único evento evita esse problema, mas abre mão da generalidade.

#### 3.1.2 A escolha do Spillover Study

O estudo usa uma **série temporal interrompida controlada** para a RQ1 e a RQ2: chegadas diárias de ambulâncias em cada DE vizinho durante 180 dias antes e 90 dias depois do dia 0, em relação aos DEs de Wexmoor agregados, com uma tendência linear, um degrau para a janela de 21 dias do desvio e um degrau para o período seguinte. Ele acrescenta **entrevistas** para a RQ3. As razões, registradas na proposta: a região de comparação remove a variação sazonal compartilhada (uma ITS não controlada não consegue); dois DEs de Wexmoor são doadores de menos para um controle sintético; os dados diários dão pontos no tempo suficientes para a tendência; e os planejadores precisam do *mecanismo* (RQ3) tanto quanto do número.

Uma revisão metodológica dos estudos de ITS que avaliaram intervenções em sistemas de saúde constatou que 81% não usaram nenhuma série de controle, apenas 55% consideraram a autocorrelação, 20,8% a sazonalidade e 8,3% a não estacionariedade, e apenas 49,2% especificaram a forma esperada do impacto ([Hategeka et al., 2020](https://doi.org/10.1136/bmjgh-2020-003567)). Essas são as falhas comuns que o desenho deste capítulo foi construído para evitar.

### 3.2 Ameaças à validade

O vocabulário a seguir é padrão nos métodos quase experimentais. Associe cada ameaça à característica do desenho que a trata — e admita as ameaças que nenhuma característica trata.

| Validade | Ameaça | No Spillover Study | Resposta do desenho |
|---|---|---|---|
| Interna | **História**: outro evento coincide com a exposição | Uma temporada de doenças respiratórias começa perto do dia 0 | Região de comparação com a mesma estação; testes placebo (Capítulo 4) |
| Interna | **Maturação / tendência** | O crescimento populacional aumenta as chegadas lentamente | Tendência linear ao longo de 180 dias pré-evento |
| Interna | **Instrumentação**: a medição muda | Alder Point muda seu sistema de registro de chegadas | Perguntar aos parceiros sobre mudanças de sistema; verificar descontinuidades (Capítulo 5) |
| Interna | **Regressão à média** | O evento "começou" num dia já escolhido porque parecia incomum | Dia 0 definido pelo registro de desvios do EMS, e não pelos dados de desfecho ([Barnett et al., 2005](https://doi.org/10.1093/ije/dyh299)) |
| Interna | **Seleção** | A região de comparação difere sistematicamente | Verificar se as trajetórias pré-evento são semelhantes; relatar as diferenças |
| De construto | O desfecho não mede o construto | "Chegadas de ambulâncias" conta transportes, e não a necessidade dos pacientes | Declarar o construto com exatidão; triangular com as entrevistas |
| De conclusão estatística | Baixo poder; autocorrelação; muitos desfechos | Um evento, contagens diárias, dois desfechos | Análise do desenho (§3.3); intervalos robustos (Capítulo 6); um único desfecho primário |
| Externa | Transferência para outras regiões | Uma região com um sistema dominante | Delimitar a alegação; descrever a estrutura da região para que outros possam julgar a transferência |

### 3.3 Análise do desenho antes dos dados

#### 3.3.1 Por que calcular antes de coletar

Para um experimento planejado, um cálculo de tamanho de amostra fixa quantos participantes recrutar. Um estudo observacional de um único evento não pode recrutar mais eventos, mas pode e deve perguntar, antes do acesso aos dados: **quão grande precisa ser um efeito para que este desenho o detecte, e quão errado estaria um desenho mais simples?** [Lakens (2022)](https://doi.org/10.1525/collabra.33267) lista seis formas de justificar um tamanho de amostra, entre elas medir (quase) toda a população, aceitar restrições de recursos e planejar para uma acurácia desejada; seja qual for a usada, o pesquisador deve declarar sobre quais efeitos os dados podem e não podem informar. Para o Spillover Study, a amostra é fixada pelo evento: um desvio de 21 dias e tantos dias pré-evento quantos os parceiros puderem fornecer.

#### 3.3.2 O menor efeito de interesse

Uma análise do desenho precisa de um efeito de referência. A coalizão de Tamsin Valley (sintética) aciona a ajuda mútua quando um DE espera quatro ou mais chegadas de ambulâncias adicionais por dia — cerca de 10% sobre a linha de base de 40 de Alder Point. Isso dá ao estudo um **menor efeito de interesse** ancorado numa decisão real: 10%. Escreva de onde veio o número; um tamanho de efeito inventado para fazer um estudo parecer ter poder adequado é uma fraqueza comum e facilmente detectada.

#### 3.3.3 Simulando o desenho

O laboratório abaixo simula o estudo planejado muitas vezes sob verdades conhecidas, usando chegadas diárias sintéticas com variação por dia da semana e variação adicional de um dia para o outro. Ele compara um desenho **não controlado** (a variação do DE tratado em relação à sua própria linha de base) com um desenho **controlado** (a mesma variação menos a variação num DE de comparação não afetado), para linhas de base de 28, 90 e 180 dias, com e sem um aumento sazonal compartilhado que começa perto do dia 0. Ele relata o efeito médio estimado (viés) e a parcela dos estudos simulados em que o intervalo de 95% exclui o zero ("sinalizados").

```python
# Lab 3 - design check before data access: bias and detection of two designs (offline, standard library only)
# Synthetic daily ambulance arrivals at a neighbouring hospital (treated) and an unaffected comparison hospital.
# Days -pre..-1 are baseline; days 0..20 are the 21-day diversion window at the attacked hospital.
import math, random

DOW = [1.08, 1.02, 1.00, 0.98, 1.00, 0.96, 0.96]

def poisson(rng, lam):                        # Knuth's method; adequate for lam < ~500
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1

def season(t, ramp):                          # respiratory season starting around day 0, shared by both
    return 1 + (0.18 / (1 + math.exp(-(t - 10) / 6)) if ramp else 0.0)

def day(rng, base, t, effect, ramp):
    lam = base * DOW[t % 7] * season(t, ramp) * (1 + effect) * rng.gammavariate(60, 1 / 60)
    return poisson(rng, lam)

def mean_var(x):
    m = sum(x) / len(x)
    return m, sum((v - m) ** 2 for v in x) / (len(x) - 1)

def log_ratio(pre, ev):                       # log(mean_event / mean_pre) and its approximate SE
    mp, vp = mean_var(pre)
    me, ve = mean_var(ev)
    return math.log(me / mp), math.sqrt(ve / (len(ev) * me ** 2) + vp / (len(pre) * mp ** 2))

def one_study(rng, pre_len, effect, ramp):
    days = range(-pre_len, 21)
    tr = {t: day(rng, 40, t, effect if t >= 0 else 0.0, ramp) for t in days}
    co = {t: day(rng, 35, t, 0.0, ramp) for t in days}
    pre, ev = [t for t in days if t < 0], [t for t in days if t >= 0]
    u, su = log_ratio([tr[t] for t in pre], [tr[t] for t in ev])           # uncontrolled pre/post
    c1, s1 = log_ratio([co[t] for t in pre], [co[t] for t in ev])
    return (u, su), (u - c1, math.sqrt(su ** 2 + s1 ** 2))                  # controlled (DiD on logs)

def run(pre_len, effect, ramp, sims=400, seed=11):
    rng = random.Random(seed)
    res = {"uncontrolled": [], "controlled": []}
    for _ in range(sims):
        a, b = one_study(rng, pre_len, effect, ramp)
        res["uncontrolled"].append(a)
        res["controlled"].append(b)
    out = {}
    for k, v in res.items():
        est = [math.exp(e) - 1 for e, _ in v]
        hits = sum(abs(e) / s > 1.96 for e, s in v) / sims
        out[k] = (sum(est) / sims, hits)
    return out

if __name__ == "__main__":
    print("season  true  pre_days  design        mean_est  share_flagged")
    for ramp in (False, True):
        for effect in (0.0, 0.10):
            for pre_len in (28, 90, 180):
                r = run(pre_len, effect, ramp)
                for k in ("uncontrolled", "controlled"):
                    m, h = r[k]
                    print(f"{'ramp' if ramp else 'flat':6}  {effect:4.2f}  {pre_len:8d}  {k:12}  {m:+8.3f}  {h:13.2f}")
```

Saída esperada (cerca de três segundos):

```text
season  true  pre_days  design        mean_est  share_flagged
flat    0.00        28  uncontrolled    +0.004           0.06
flat    0.00        28  controlled      +0.010           0.04
flat    0.00        90  uncontrolled    +0.001           0.04
flat    0.00        90  controlled      +0.004           0.02
flat    0.00       180  uncontrolled    +0.004           0.05
flat    0.00       180  controlled      +0.000           0.04
flat    0.10        28  uncontrolled    +0.102           0.39
flat    0.10        28  controlled      +0.115           0.24
flat    0.10        90  uncontrolled    +0.105           0.52
flat    0.10        90  controlled      +0.110           0.33
flat    0.10       180  uncontrolled    +0.101           0.52
flat    0.10       180  controlled      +0.109           0.29
ramp    0.00        28  uncontrolled    +0.084           0.27
ramp    0.00        28  controlled      +0.003           0.07
ramp    0.00        90  uncontrolled    +0.088           0.40
ramp    0.00        90  controlled      +0.002           0.06
ramp    0.00       180  uncontrolled    +0.096           0.52
ramp    0.00       180  controlled      +0.006           0.07
ramp    0.10        28  uncontrolled    +0.191           0.84
ramp    0.10        28  controlled      +0.105           0.23
ramp    0.10        90  uncontrolled    +0.198           0.94
ramp    0.10        90  controlled      +0.106           0.28
ramp    0.10       180  uncontrolled    +0.202           0.97
ramp    0.10       180  controlled      +0.106           0.31
```

Quatro conclusões se seguem, e a proposta precisa declará-las antes que qualquer dado seja visto:

1. **Sem uma mudança sazonal, os dois desenhos são não enviesados**, e o desenho não controlado sinaliza um efeito verdadeiro de 10% com mais frequência (cerca de 52% contra cerca de 30% com 90 ou 180 dias de linha de base) porque subtrair uma série de comparação acrescenta o ruído dela.
2. **Com um aumento sazonal compartilhado, o desenho não controlado fica muito enviesado.** Quando o efeito verdadeiro é zero, ele estima cerca de +8% a +10% e sinaliza um efeito inexistente em 27% a 52% dos estudos — *com mais frequência com linhas de base mais longas*, porque a linha de base então recua mais para dentro da estação baixa. Mais dados não corrigiram um problema de desenho; tornaram a conclusão falsa mais confiante.
3. **O desenho controlado remove o viés sazonal** (estimativas médias perto de zero; sinalizado em 6–7% dos estudos nulos, perto dos 5% nominais, dados os erros-padrão aproximados), mas detecta um efeito verdadeiro de 10% em apenas 23–31% dos estudos.
4. Portanto, **um único DE vizinho não consegue detectar de forma confiável o menor efeito de interesse**. O estudo deve ser enquadrado como *estimação com intervalos*, e não como um teste que "mostra" o transbordamento; ele deve relatar o intervalo e os efeitos que descarta; e o gradiente de distância da RQ2 deve ser lido nos três vizinhos, e não a partir de um único teste. (As estimativas controladas têm média de cerca de 0,105–0,115 quando a verdade é 0,10 porque a média das razões logarítmicas exponenciadas é ligeiramente maior do que a média exponenciada — um viés pequeno e conhecido.)

### 3.4 Revisão ética

#### 3.4.1 O que precisa de revisão

Entrevistas com gestores de DEs, supervisores do EMS e equipe da coalizão são pesquisa com seres humanos em quase todas as jurisdições e precisam de aprovação do comitê de ética em pesquisa ou do institutional review board da instituição antes do recrutamento. Nos Estados Unidos, a [Common Rule (45 CFR Part 46)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46) define a pesquisa com seres humanos e as categorias que podem ser dispensadas; é a instituição, e não o estudante, que decide se um estudo se enquadra. As contagens diárias agregadas por DE geralmente não contêm informações sobre indivíduos, mas a instituição pode ainda assim exigir revisão, e um custodiante dos dados pode exigir sua própria aprovação. Na UE, os dados de saúde são uma categoria especial segundo o [artigo 9º do GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), e o tratamento para pesquisa científica se apoia nas salvaguardas do artigo 89. No Brasil, o dado referente à saúde é dado pessoal sensível (art. 5º, II, da [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)), e seu tratamento para a realização de estudos por órgão de pesquisa é admitido pelo art. 11, II, "c", garantida, sempre que possível, a anonimização. Se algum dia fossem necessários registros individuais, os dados de saúde dos EUA trariam os padrões de desidentificação da HIPAA Privacy Rule e, para um conjunto limitado de dados, um acordo de uso de dados ([orientação do HHS](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html)). O Spillover Study evita totalmente os registros individuais — a minimização de dados é a salvaguarda ética mais forte disponível.

#### 3.4.2 Riscos próprios dos estudos de infraestrutura

Os princípios do [Menlo Report](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) — respeito às pessoas, beneficência, justiça e respeito à lei e ao interesse público — estruturam a análise de riscos. Neste estudo, os principais riscos são:

- **Para os entrevistados:** serem culpados por decisões tomadas durante o incidente; revelação da identidade pela combinação de função e organização (há um único supervisor de operações do EMS em Tamsin Valley); consequências profissionais por criticar um empregador ou um hospital vizinho.
- **Para as organizações:** dano à reputação ("Alder Point não deu conta"); exposição regulatória; revelação de fraquezas de segurança no Kestrel.
- **Para o público:** uma constatação publicada como "os DEs desta região perdem um quarto de sua capacidade ociosa quando um sistema desvia" poderia, combinada com outras informações, ajudar um adversário a escolher um alvo que maximize o dano regional. O [teste de sensibilidade da informação](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md#ch-01) do livro de doutorado se aplica: um artefato identifica um ativo específico, sua vulnerabilidade ou sua dependência de uma forma que ajudaria alguém a danificá-lo?
- **Para o pesquisador:** pressão dos parceiros para suavizar os resultados; acesso a informações para cujo manuseio o pesquisador não foi treinado.

#### 3.4.3 Salvaguardas

| Risco | Salvaguarda |
|---|---|
| Identificação dos entrevistados | Categorias de função amplas o bastante para conter várias pessoas; citações verificadas quanto a detalhes identificadores; nomes das organizações substituídos em todos os produtos |
| Culpa | Perguntas sobre sistemas e restrições, e não sobre decisões individuais; o termo de consentimento declara que os dados não serão compartilhados com os empregadores |
| Desistência | Os participantes podem desistir até uma data declarada, antes da finalização da análise; seus dados são então apagados |
| Dano organizacional | Os parceiros revisam as minutas quanto a erros factuais e informações protegidas dentro de um prazo fixo, sem veto sobre as constatações |
| Risco de definição de alvos pelo público | Nenhum número de capacidade por instalação publicado; apenas síntese regional; constatações sobre fraquezas específicas encaminhadas em privado à organização em questão |
| Células pequenas | Suprimir ou agregar as contagens abaixo do tamanho mínimo de célula do custodiante |
| Contato com sistemas | Nenhum: o estudo nunca toca, varre ou testa nenhum sistema hospitalar, do EMS ou do despacho; usa apenas os dados fornecidos pelos custodiantes e as entrevistas |

#### 3.4.4 A submissão

Uma submissão típica contém: a pergunta e seu benefício; o desenho e as fontes de dados; o recrutamento, o consentimento e a desistência; os riscos e as salvaguardas; o manuseio, o armazenamento, a retenção e a destruição dos dados; a divulgação; os conflitos de interesse; e a formação do pesquisador. Anexe o roteiro de entrevista, a folha de informações, o termo de consentimento e os acordos de dados. Escreva para um membro do comitê que não é especialista em segurança: explique em linguagem simples por que uma constatação sobre a capacidade regional é sensível.

### 3.5 Acordos de dados e o plano de gestão de dados

Antes que qualquer dado se mova, coloque por escrito: quais dados, em que nível de agregação, para qual período; a limitação da finalidade; o local de armazenamento e o acesso; a retenção e a destruição; a revisão antes da publicação (apenas revisão factual e de informações protegidas, dentro de um número fixo de dias, sem veto); o reconhecimento e a autoria; e a notificação de violações. Um **plano de gestão de dados** registra então, para cada ativo de dados, sua fonte, seu nível de sensibilidade, seu formato, seu local, quem pode acessá-lo, a retenção e o que pode ser compartilhado no fim. Use os níveis de sensibilidade de forma consistente em todo o projeto:

| Nível | Conteúdo no Spillover Study | Manuseio |
|---|---|---|
| Público | Código, dados de teste sintéticos, livro de códigos, resultados regionais agregados | Repositório |
| Restrito | Contagens diárias por DE fornecidas pelos custodiantes | Armazenamento institucional criptografado; acesso nominal; destruídas após o período de retenção |
| Confidencial | Gravações das entrevistas, transcrições antes da desidentificação, termos de consentimento | Criptografados, separados dos dados; gravações destruídas após a transcrição, se o consentimento assim declarar |

### 3.6 Um projeto reprodutível desde o primeiro dia

A reprodutibilidade é mais fácil de construir do que de adaptar depois. [Sandve et al. (2013)](https://doi.org/10.1371/journal.pcbi.1003285) dão dez regras, entre elas: registrar como cada resultado foi produzido; evitar a manipulação manual dos dados; arquivar as versões exatas dos programas externos; colocar os scripts próprios sob controle de versões; registrar os resultados intermediários; e anotar as sementes dos processos aleatórios. O manual comunitário [The Turing Way](https://book.the-turing-way.org/) desdobra essas regras em prática. Os [princípios FAIR](https://doi.org/10.1038/sdata.2016.18) — localizáveis, acessíveis, interoperáveis, reutilizáveis — se aplicam ao que pode ser compartilhado; para dados restritos, metadados FAIR podem descrever um conjunto de dados que não pode ser liberado.

Uma estrutura mínima:

```text
spillover-study/
  README.md            question, how to run everything, environment, contacts
  data/raw/            read-only copies as received (restricted; never in version control)
  data/derived/        produced only by scripts
  code/01_audit.py     numbered in execution order
  code/02_build.py
  code/03_analysis.py
  output/              tables and figures, regenerated by scripts
  docs/codebook.md     every variable: source, definition, unit, missing-value code
  docs/deviations.md   every change to the plan, dated, with reason and whether results had been seen
  docs/environment.txt Python version and package versions
```

Um **plano de pré-análise** fixa, antes que os dados de desfecho sejam examinados: os estimandos, os desfechos primário e secundários, as unidades de comparação, as janelas, o modelo, o método dos intervalos, as verificações de robustez e como os desvios serão relatados. Registrá-lo com carimbo de tempo — por exemplo, nos [OSF Registries](https://osf.io/registries) — torna o plano verificável; [Nosek et al. (2018)](https://doi.org/10.1073/pnas.1708274114) descrevem por que o pré-registro distingue a previsão da pós-dição. Num estudo observacional, os dados podem já existir, então declare com honestidade o que tinha sido visto quando o plano foi registrado (por exemplo, "os dados pré-evento de um DE foram examinados durante o piloto apenas quanto à completude").

### 3.7 Exemplo resolvido: as perguntas do comitê de ética (sintético)

O comitê devolveu a primeira submissão do candidato com cinco perguntas. As respostas do candidato:

| Pergunta do comitê | Resposta |
|---|---|
| "Por que as entrevistas são necessárias? Os dados sozinhos não poderiam responder à pergunta?" | Os dados estimam *quanto* da carga se deslocou (RQ1–2), mas não *como* (RQ3). Os planejadores precisam do mecanismo para mudar os protocolos. Dez entrevistas de 45 minutos cada. |
| "Os participantes poderiam ser identificados?" | Sim, pela função e pela organização. As funções serão relatadas como "liderança do DE", "operações do EMS" ou "coalizão", cada uma contendo pelo menos três participantes; os nomes das organizações serão removidos; as citações serão revisadas. |
| "E se um participante descrever um erro que prejudicou um paciente?" | O roteiro evita casos clínicos individuais. Se algum for relatado espontaneamente, não será registrado de forma identificável; a folha de informações explica os limites da confidencialidade exigidos por lei. |
| "Os resultados poderiam ajudar um atacante?" | Estimativas de capacidade por instalação não serão publicadas; a dissertação relata padrões regionais e o gradiente de distância. Fraquezas específicas serão relatadas em privado à organização em questão. |
| "Quem pode interromper o estudo?" | O orientador, o comitê e qualquer parceiro, quanto aos seus próprios dados; os participantes, quanto às suas próprias entrevistas, até a data de desistência declarada. |

A submissão foi aprovada com uma condição: o termo de consentimento tinha de declarar que o pesquisador não é empregado de nenhuma organização participante e não compartilhará com elas dados identificáveis.

### 3.8 Erros comuns e limites

- Escolher um desenho antes e depois porque os dados são fáceis e depois alegar um efeito causal.
- Usar uma ITS não controlada quando um choque compartilhado (estação do ano, epidemia, política) é plausível.
- Presumir tendências paralelas sem inspecionar as trajetórias pré-evento.
- Executar um cálculo de poder com um tamanho de efeito escolhido para fazer o estudo parecer adequado, em vez de um menor efeito de interesse ligado a uma decisão.
- Acreditar que mais dados de linha de base sempre reduzem o viés; com uma tendência ou uma mudança sazonal, eles podem aumentá-lo.
- Enviar uma submissão ao comitê de ética que trate os dados agregados de infraestrutura como isentos de risco.
- Concordar com uma revisão pelos parceiros sem prazo e sem uma cláusula de "nenhum veto sobre as constatações".
- Montar a reprodutibilidade no fim; edições manuais nos arquivos de dados que nenhum script registra.
- Registrar um plano de pré-análise sem declarar quais dados já tinham sido vistos.

O limite do desenho é que ele só consegue reduzir, e não eliminar, a dependência de pressupostos não testáveis. Uma ITS controlada só é crível se a região de comparação não tiver sofrido um choque diferente ao mesmo tempo; o Capítulo 4 testa esse pressuposto até onde os dados permitem.

### Exercícios — capítulo 3

**EX015 — Escolha e defenda um desenho.** *Objetivo:* selecionar um desenho pelos pressupostos e pelos dados. *Insumos:* os desenhos de §3.1.1; um cenário em que um processador regional de pagamentos sofreu uma interrupção de três dias e você tem as contagens semanais de transações com cartão de 40 categorias de comércio na região afetada e em três regiões não afetadas, ao longo de dois anos. *Restrições:* um desenho primário e um desenho de robustez. *Passos:* (1) declarar o estimando; (2) comparar pelo menos três desenhos quanto ao pressuposto, aos dados e à fraqueza; (3) escolher; (4) dizer o que faria você abandonar a escolha. *Evidência esperada:* uma página. *Rubrica:* 3 = consequência da resolução semanal para um evento de três dias reconhecida, pressupostos de tendências paralelas ou do conjunto de doadores declarados e verificáveis, condição de abandono concreta; 2 = um desenho mal descrito; 1 = sem pressupostos; 0 = nada.

**EX016 — Análise do desenho.** *Objetivo:* encontrar o menor efeito de transbordamento que um desenho antes e depois controlado consegue detectar de forma confiável e reenquadrar a RQ1 para se ajustar a esse poder. *Insumos:* código do Laboratório 3. *Restrições:* off-line; manter a semente 11 e as 400 simulações. *Passos:* (1) executar o laboratório e registrar a saída; (2) acrescentar um efeito verdadeiro de 0,20 e relatar a parcela sinalizada do desenho controlado para 28, 90 e 180 dias de linha de base sob o aumento sazonal; (3) declarar o menor efeito que o desenho controlado detecta em pelo menos cerca de três quartos dos estudos com 180 dias; (4) reescrever a RQ1 como uma pergunta de estimação que este desenho consiga responder com honestidade. *Evidência esperada:* saídas, uma frase sobre os efeitos detectáveis, RQ1 revisada. *Rubrica:* 3 = valores corretos, efeito detectável declarado como cerca de 20%, e não 10%, RQ1 reenquadrada para a estimação; 2 = um valor errado; 1 = não executado; 0 = nada.

**EX017 — Riscos na submissão ao comitê de ética.** *Objetivo:* identificar e mitigar riscos. *Insumos:* um estudo que entrevista operadores de concessionárias de água sobre uma interrupção do sistema de desinfecção numa concessionária pequena. *Restrições:* usar os quatro princípios do Menlo; pelo menos cinco partes interessadas. *Passos:* (1) listar as partes interessadas e os riscos; (2) propor salvaguardas; (3) identificar o risco de sensibilidade da informação específico de uma concessionária pequena; (4) redigir as duas frases da folha de informações sobre os limites da confidencialidade. *Evidência esperada:* tabela e texto redigido. *Rubrica:* 3 = risco de identificação numa população pequena reconhecido, risco de definição de alvos pelo público tratado, salvaguardas concretas, texto da folha de informações honesto quanto aos limites; 2 = um princípio ralo; 1 = genérico; 0 = nada.

**EX018 — Plano de gestão de dados.** *Objetivo:* classificar e manusear os dados por nível. *Insumos:* os ativos do Spillover Study: contagens diárias dos custodiantes; contagens de Wexmoor de um painel público; gravações das entrevistas; transcrições; livro de códigos; código de análise; termos de consentimento; os limiares de ajuda mútua da coalizão. *Restrições:* os três níveis de §3.5. *Passos:* atribuir a cada um nível, armazenamento, acesso, retenção e compartilhamento no fim do projeto. *Evidência esperada:* tabela. *Rubrica:* 3 = níveis consistentes com a sensibilidade (gravações e termos de consentimento confidenciais, contagens dos custodiantes restritas, código e livro de códigos públicos), dados do painel público tratados segundo seus termos, limiares de ajuda mútua tratados como sensíveis; 2 = um mal atribuído; 1 = tudo público ou tudo confidencial; 0 = nada.

**EX019 — Plano de pré-análise.** *Objetivo:* fixar a análise antes que os desfechos sejam vistos. *Insumos:* §3.1.2 e os estimandos do Capítulo 1. *Restrições:* no máximo duas páginas. *Passos:* especificar os estimandos, os desfechos (primário e secundários), a comparação, as janelas, o modelo, o método dos intervalos, as verificações de robustez, o tratamento da multiplicidade e a regra dos desvios; declarar quais dados tinham sido vistos no registro. *Evidência esperada:* plano. *Rubrica:* 3 = cada elemento específico o bastante para que outro analista produza a mesma estimativa, regra dos desvios explícita, acesso prévio aos dados declarado; 2 = um elemento vago; 1 = modelo não especificado; 0 = nada.

**EX020 — Auditoria da reprodutibilidade.** *Objetivo:* testar se um projeto pode ser reexecutado. *Insumos:* uma pasta com os laboratórios dos Capítulos 1 e 3 e suas saídas. *Restrições:* uma segunda pessoa o reexecuta apenas a partir do README. *Passos:* (1) escrever o README; (2) registrar o ambiente; (3) pedir a outra pessoa que o reexecute; (4) listar cada ponto em que ela precisou perguntar algo a você e corrigi-lo. *Evidência esperada:* README, arquivo de ambiente e uma lista de problemas com as correções. *Rubrica:* 3 = a reexecução teve sucesso com saídas idênticas e cada pergunta foi respondida no README; 2 = resta um passo manual; 1 = saídas diferentes sem explicação; 0 = nada.

### Síntese do capítulo

Um evento de infraestrutura não planejado não oferece aleatorização, então todo desenho é uma aproximação de um contrafactual, e sua credibilidade se apoia em pressupostos que você precisa declarar. Uma série temporal interrompida controlada remove os choques sazonais compartilhados que um antes e depois ou uma ITS não controlada atribuiriam ao evento; as entrevistas fornecem o mecanismo. Associe cada ameaça à validade a uma característica do desenho, ou admita-a. Simule o desenho antes do acesso aos dados: o Laboratório 3 mostra que um aumento sazonal compartilhado torna um desenho não controlado confiantemente errado — e mais ainda com linhas de base mais longas —, enquanto o desenho controlado é quase não enviesado, mas impreciso demais para detectar um efeito de 10% num único DE. Enquadre o estudo como estimação. A revisão ética precisa cobrir os entrevistados, as organizações e o público, porque as constatações sobre a capacidade regional podem ser sensíveis. Os acordos, os níveis e um projeto reprodutível com um plano de pré-análise registrado vêm antes do primeiro arquivo de dados.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 08

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Infraestrutura crítica e segurança setorial: explicações concorrentes

### Objetivos de aprendizagem e conexão

Ao fim deste capítulo, o estudante será capaz de:

1. Aplicar o método das hipóteses de trabalho múltiplas: listar todas as explicações que poderiam produzir os dados observados antes de favorecer uma delas.
2. Derivar, para cada rival, uma **previsão que difere** da previsão da hipótese principal e escolher os dados capazes de distingui-las.
3. Desenhar um diagrama causal para um evento de infraestrutura, identificar os caminhos que enviesariam uma comparação e dizer o que precisa ser medido ou contornado pelo desenho.
4. Usar populações de comparação, controles negativos, datas placebo, gradientes de dose–resposta e alinhamento temporal como evidência discriminante e declarar o pressuposto em que cada um se apoia.
5. Analisar casos públicos documentados em que uma explicação cibernética concorreu com outra explicação e dizer qual evidência decidiu entre elas.
6. Executar um laboratório em que uma comparação ingênua atribui um aumento sazonal a um incidente e mostrar como uma região de comparação e janelas placebo o expõem.

O Capítulo 3 escolheu um desenho; este capítulo o ataca. A tabela de rivais construída aqui torna-se a seção de robustez do Capítulo 6, as limitações do Capítulo 7 e as perguntas dos examinadores do Capítulo 8.

### 4.1 Hipóteses de trabalho múltiplas e inferência forte

Em 1890, o geólogo T. C. Chamberlin alertou contra a "teoria dominante": quando um pesquisador tem uma explicação favorita, as evidências são selecionadas inconscientemente para se ajustarem a ela. Seu remédio era manter **hipóteses de trabalho múltiplas** ao mesmo tempo, de modo que cada observação seja pesada contra todas elas ([Chamberlin, reimpresso em 1965](https://doi.org/10.1126/science.148.3671.754)). [Platt (1964)](https://doi.org/10.1126/science.146.3642.347) transformou isso num procedimento que chamou de **inferência forte**: conceber hipóteses alternativas; conceber um experimento crucial cujos resultados possíveis excluam uma ou mais delas; realizá-lo; repetir. Pesquisadores de infraestrutura raramente realizam experimentos, mas a lógica sobrevive: para cada rival, encontre uma observação que o rival preveja de forma diferente da sua hipótese.

A regra prática deste curso: **uma explicação rival não está tratada até que você tenha declarado o que ela prevê que a sua hipótese não prevê — e tenha olhado.** "Controlamos a sazonalidade" não é uma resposta; "um aumento sazonal também apareceria em Wexmoor, e a estimativa é líquida da variação de Wexmoor" é.

### 4.2 O que a hipótese do transbordamento prevê

Antes de listar os rivais, escreva o padrão completo de previsões da hipótese principal. Se o desvio de ambulâncias do Kestrel deslocou carga para os seus vizinhos, então:

1. **Tempo:** as chegadas aos vizinhos sobem quando o registro de desvios do EMS diz que o desvio começou, e não antes, e voltam a cair quando ele termina (talvez com uma cauda curta).
2. **Lugar:** o aumento é maior nos DEs mais próximos (um gradiente de distância).
3. **População:** não há aumento correspondente numa região não afetada nos mesmos dias.
4. **Canal:** as chegadas de ambulâncias sobem mais do que as chegadas espontâneas, se o DE do Kestrel permaneceu aberto aos pacientes que chegam por conta própria.
5. **Mecanismo:** os registros de destino do EMS mostram transportes que normalmente teriam ido para o Kestrel indo para os vizinhos; a equipe descreve a redistribuição.

Um rival que reproduza todas as cinco previsões não pode ser distinguido por estes dados. A maioria dos rivais falha em pelo menos uma, e essa falha é o teste.

### 4.3 Rivais no Spillover Study

| Rival | O que ele preveria | Evidência discriminante |
|---|---|---|
| R1 Surto respiratório sazonal | Aumento nos DEs de todas as regiões, começando com a estação, e não com o desvio; sem gradiente de distância; as chegadas espontâneas também sobem | Variação da região de comparação; canal das chegadas espontâneas; datas placebo em estações anteriores |
| R2 Evento regional simultâneo (onda de calor, aglomeração em massa, interdição de estrada) | Aumento ligado às datas e à geografia do evento | Calendários de eventos; clima; dados viários; alinhamento temporal |
| R3 Mudança de política do EMS ao mesmo tempo | Deslocamento dos destinos a partir da data da política, possivelmente durando além do desvio | Registro de políticas do EMS; entrevistas; persistência após o dia 20 |
| R4 Mudança de medição (novo sistema de registro num vizinho; perda de dados do próprio Kestrel) | Degrau na série coincidindo com a mudança de sistema; possivelmente em todos os desfechos daquele sistema | Perguntas aos parceiros; verificações de descontinuidade em desfechos não relacionados do mesmo sistema |
| R5 Regressão à média | Evento datado por um valor incomum do desfecho; queda posterior em direção à média | Dia 0 definido pelo registro de desvios, independentemente dos desfechos ([Barnett et al., 2005](https://doi.org/10.1093/ije/dyh299)) |
| R6 Antecipação | Variação antes do dia 0 (rumores, interrupções parciais) | Inspecionar os dias −14 a −1; entrevistas sobre a fase inicial do incidente |
| R7 Acaso | Estimativas dentro da faixa de eventos falsos em períodos normais | Distribuição de placebos no tempo; intervalos |
| R8 Choque diferente na região de comparação | Wexmoor varia por razões próprias, enviesando a diferença | Comparar cada DE de Wexmoor separadamente; verificar os eventos próprios de Wexmoor; unidades de comparação alternativas (Capítulo 8) |
| R9 Desvio não cibernético no Kestrel em outros momentos | Aumentos semelhantes em outros episódios de desvio | Analisar os desvios não cibernéticos como verificação do mecanismo (uma força, e não uma ameaça, se o padrão for semelhante) |

Observe o papel de R9. Se os desvios comuns do Kestrel por superlotação também deslocam carga para Alder Point, isso sustenta o mecanismo e sugere que o que importa é o **desvio**, e não o **ransomware** — o que estreita a alegação com honestidade. A exposição do estudo é o "desvio induzido por ransomware"; se um desvio por ransomware difere de um comum (mais longo, menos previsível, com os sistemas de informação fora do ar no hospital que desvia) é outra pergunta.

### 4.4 Diagramas causais

Um **diagrama causal** (grafo acíclico dirigido, DAG) representa as variáveis como nós e os efeitos causais presumidos como setas. Seu valor está em tornar os pressupostos visíveis e em dizer quais comparações são enviesadas por quais caminhos ([Greenland, Pearl e Robins, 1999](https://doi.org/10.1097/00001648-199901000-00008); [Hernán e Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook)). Para o Spillover Study, pense na "exposição" como *estar no período do desvio* e no desfecho como *as chegadas a Alder Point naquele dia*:

```text
Attack ──► Diversion ──► EMS destination choices ──► Arrivals at AP
                                                       ▲   ▲
Calendar time ──► Season ──────────────────────────────┘   │
      │                                                     │
      └──────────► (period: before vs during) ── Trend ─────┘

Season ──► Arrivals in Wexmoor          Distance (AP, BF, CG) modifies EMS destination choices
```

Descrição textual do diagrama: o ataque causa o desvio, que altera as escolhas de destino do EMS, que aumentam as chegadas a Alder Point. O tempo de calendário determina tanto se um dia está no período do desvio quanto a estação; a estação também aumenta as chegadas a Alder Point e em Wexmoor. A distância modifica a intensidade com que o desvio altera os destinos em cada vizinho.

O diagrama mostra por que uma comparação antes e depois é enviesada: "antes versus durante" está ligado ao tempo de calendário, e o tempo de calendário chega ao desfecho pela estação — um **caminho de porta dos fundos** do período de exposição até o desfecho que não passa pelo desvio. Ajustar diretamente pela estação é impossível (ela não é medida com precisão), mas as chegadas de Wexmoor são causadas pela estação e não pelo desvio, então subtrair a variação de Wexmoor remove o caminho sazonal *se* a estação afetar as duas regiões da mesma forma. Esse "se" é o pressuposto de tendências paralelas do Capítulo 3, agora visível como um pressuposto sobre setas.

### 4.5 Ferramentas discriminantes e seus pressupostos

| Ferramenta | Como funciona | Pressuposto em que se apoia |
|---|---|---|
| **População de comparação** | Uma população não exposta compartilha as causas rivais; sua variação estima a contribuição dos rivais | Ela compartilha os rivais por igual e não tem um rival próprio (R8) |
| **População de controle negativo** | Uma população que *não pode* ser afetada pela exposição; qualquer "efeito" nela revela viés no método ([Lipsitch et al., 2010](https://doi.org/10.1097/EDE.0b013e3181d61eeb)) | Está sujeita aos mesmos vieses da população tratada |
| **Desfecho de controle negativo** | Um desfecho que a exposição não pode afetar, mas os confundidores podem; um "efeito" sobre ele sinaliza confundimento (mesma fonte) | A exposição realmente não pode afetá-lo — argumente isso, não o presuma |
| **Placebo no tempo** | Aplicar a análise a datas de evento falsas em que nada aconteceu; a estimativa real deve ser incomum entre elas | As janelas falsas se parecem com a real em estação e ruído |
| **Dose–resposta** | Uma exposição maior (DE mais próximo) deve produzir um efeito maior | A distância é uma aproximação válida da intensidade da exposição |
| **Alinhamento temporal** | A variação deve começar e terminar com a exposição registrada independentemente do desfecho | Existem registros independentes da exposição, e eles são exatos |
| **Evidência do mecanismo** | Os registros de destino e as entrevistas mostram o caminho | Os registros estão completos; os relatos não foram moldados pela retrospectiva |

Duas cautelas. Primeiro, controles negativos precisam de argumentos, não de rótulos. As chegadas espontâneas a Alder Point parecem um desfecho de controle negativo para um desvio de *ambulâncias*, mas, se os pacientes que teriam ido por conta própria ao Kestrel também foram para outro lugar, as chegadas espontâneas estão parcialmente expostas; use-as como comparação de canais (previsão 4), e não como um controle negativo puro. Segundo, entrevistas realizadas depois de um incidente estão sujeitas ao **viés de retrospectiva**: conhecer o desfecho muda o julgamento das pessoas sobre quão previsível ele era ([Fischhoff, 1975](https://doi.org/10.1037/0096-1523.1.3.288)). Pergunte sobre o que se sabia e o que se decidiu em cada momento, ancorado em registros datados, em vez de "o que deu errado".

### 4.6 Explicações concorrentes em casos documentados

Os incidentes públicos de infraestrutura mostram repetidamente uma explicação cibernética concorrendo com outra. Os casos abaixo são descritos apenas no nível em que suas fontes públicas os relatam.

| Caso | Explicações concorrentes | Evidência que discriminou, conforme relatado publicamente | Lição para o desenho da pesquisa |
|---|---|---|---|
| Estação de tratamento de água de Oldsmar, 2021 | Intrusão remota versus ação de um funcionário | Segundo o ex-administrador municipal, o FBI não encontrou evidências de acesso externo; um porta-voz do FBI disse que não podia confirmar uma intrusão direcionada ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)); o alerta [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a) da CISA havia relatado um comprometimento | Codifique as causas dos incidentes com status e fonte; um alerta não é uma constatação final |
| Hospital de Düsseldorf, 2020 | Atraso no tratamento causado pelo ataque versus a condição subjacente da paciente | Os promotores concluíram, após a autópsia, que o atraso não foi decisivo ([MIT Technology Review, 2020](https://www.technologyreview.com/2020/11/12/1012015/ransomware-did-not-kill-a-german-hospital-patient/)) | Alegações sobre desfechos individuais precisam de um contrafactual para o indivíduo; desenhos no nível da população fazem uma pergunta diferente |
| Colonial Pipeline, 2021 | Oleoduto parado porque os sistemas operacionais foram atacados versus uma parada preventiva após um ataque de ransomware à empresa | O DOE descreve a empresa como tendo "proactively shut down its pipeline system in response to a ransomware attack" ([DOE](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident)) | Uma consequência pode ser causada pela *resposta* a um ataque; um estudo precisa modelar decisões, e não apenas comprometimentos |
| Interrupção global de julho de 2024 | Ataque cibernético versus atualização de software defeituosa | A Microsoft atribuiu a interrupção a uma atualização defeituosa de um software de segurança em 8,5 milhões de dispositivos ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)) | Falhas não maliciosas produzem consequências semelhantes às cibernéticas; são ao mesmo tempo rivais e comparações úteis |

A linha da Colonial merece ênfase para o Spillover Study. O desvio do Kestrel foi uma **decisão** tomada em resposta ao ataque, e não uma consequência mecânica dele. O mesmo ataque num hospital com outra liderança, outros procedimentos ou outras informações poderia ter levado a um desvio mais curto ou a nenhum. A exposição do estudo é, portanto, o desvio, e sua alegação diz respeito às consequências do desvio; ela não deve ser lida como uma estimativa do efeito do ransomware enquanto tal.

### 4.7 Exemplo resolvido: a tabela de rivais na proposta (sintético)

O primeiro parágrafo do candidato sobre os rivais dizia: *"Possíveis confundidores, como a sazonalidade, foram controlados pelo uso de uma região de comparação."* O orientador pediu a previsão distinta e o teste de cada rival. A seção revisada da proposta:

- **R1 Estação.** Prevê um aumento também em Wexmoor. *Teste:* relatar a variação pré/pós da própria Wexmoor (uma população de controle negativo); estimar os efeitos líquidos de Wexmoor; executar janelas placebo. *Se falhar:* se a variação de Wexmoor for tão grande quanto a de Alder Point, a estimativa de transbordamento fica perto de zero, e o estudo o diz.
- **R3 Política do EMS.** Prevê uma variação que começa numa data de política e persiste. *Teste:* solicitar o registro de políticas do EMS para os dias −60 a +90; perguntar aos supervisores do EMS (RQ3). *Se falhar:* relatar a mudança de política como uma cointervenção e estreitar a alegação.
- **R4 Medição.** Prevê um degrau em todos os desfechos do sistema de Alder Point. *Teste:* perguntar ao custodiante sobre mudanças de sistema; inspecionar as chegadas espontâneas e os tempos de espera em busca do mesmo degrau.
- **R6 Antecipação.** Prevê uma variação antes do dia 0. *Teste:* inspecionar os dias −14 a −1 no gráfico de estudo de evento; perguntar aos entrevistados quando souberam do ataque.
- **R7 Acaso.** *Teste:* a posição da estimativa real entre as janelas placebo; intervalos.
- **R8 Choque na comparação.** *Teste:* estimar contra cada DE de Wexmoor separadamente e agregado (a curva de especificação do Capítulo 8); perguntar ao custodiante de Wexmoor sobre eventos.

Um rival que o estudo não consegue testar — por exemplo, uma mudança não registrada na forma como as próprias ambulâncias do Kestrel eram despachadas — vai para as limitações, com sua direção provável (Capítulo 7).

### 4.8 Atividade prática: a estação que parecia transbordamento

Salve o arquivo a seguir como `lab4_data.py`; os Laboratórios 6 e 8 o importam. Ele gera os dados sintéticos de Tamsin Valley e Wexmoor para os dias −180 a +89, com variação por dia da semana, variação adicional de um dia para o outro, dois feriados regionais e uma estação respiratória que começa a subir perto do dia 0 nas duas regiões. Os efeitos verdadeiros de transbordamento estão fixados no dicionário `TRUE`: +22% em Alder Point nos dias 0–20 (+5% nos dias 21–34), +10% em Brookfield (+2%) e nenhum em Calloway. O script então compara uma estimativa ingênua antes e depois (28 dias antes versus os dias 0–20) com a mesma variação expressa em relação a Wexmoor e executa a comparação ingênua em 19 janelas falsas de 21 dias na linha de base.

```python
# Lab 4 - competing explanations for a post-incident rise in ambulance arrivals (offline, standard library only)
# Save as lab4_data.py: Labs 6 and 8 import make_region() from it.
# Synthetic Tamsin Valley (treated region) and Wexmoor (comparison region); day 0 = start of the
# 21-day ambulance diversion at the attacked Kestrel hospitals. Days -180..89.
import math, random

DOW = [1.08, 1.02, 1.00, 0.98, 1.00, 0.96, 0.96]
BASE = {"AP": 40, "BF": 30, "CG": 22, "W1": 35, "W2": 28}           # ambulance arrivals per day
DIST_KM = {"AP": 6, "BF": 14, "CG": 38}                            # distance from Kestrel
TRUE = {"AP": (0.22, 0.05), "BF": (0.10, 0.02), "CG": (0.0, 0.0)}  # (days 0-20, days 21-34)
HOLIDAYS = {-100, 45}                                              # regional holidays, both regions
DAYS = range(-180, 90)

def poisson(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1

def season(t, amp):
    return 1 + amp / (1 + math.exp(-(t - 10) / 6))

def effect(site, t):
    during, tail = TRUE.get(site, (0.0, 0.0))
    return during if 0 <= t <= 20 else tail if 21 <= t <= 34 else 0.0

def make_region(seed=2026):
    rng = random.Random(seed)
    data = {}
    for site, base in BASE.items():
        amp = 0.18 if site in TRUE else 0.17
        series = {}
        for t in DAYS:
            lam = base * DOW[t % 7] * season(t, amp) * (1 + effect(site, t))
            lam *= (0.85 if t in HOLIDAYS else 1.0) * rng.gammavariate(60, 1 / 60)
            series[t] = poisson(rng, lam)
        data[site] = series
    wait = {}                                                     # AP median minutes to provider
    for t in DAYS:
        wait[t] = max(5.0, rng.gauss(28 + (4 if 0 <= t <= 20 else 0) + 3 * (season(t, 0.18) - 1) / 0.18, 6))
    data["AP_wait"] = wait
    return data

def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs)

def naive(series, pre=(-28, -1), ev=(0, 20)):
    return mean(series[t] for t in range(pre[0], pre[1] + 1)), mean(series[t] for t in range(ev[0], ev[1] + 1))

if __name__ == "__main__":
    d = make_region()
    comp = {t: d["W1"][t] + d["W2"][t] for t in DAYS}
    print("site  km  pre28  event  naive_change  relative_to_Wexmoor")
    cp, ce = naive(comp)
    for s in ("AP", "BF", "CG", "W1", "W2"):
        p, e = naive(d[s])
        rel = (e / p) / (ce / cp) - 1
        km = DIST_KM.get(s, "-")
        print(f"{s:4}  {str(km):>2}  {p:5.1f}  {e:5.1f}  {e / p - 1:+12.3f}  {rel:+19.3f}")
    print(f"Wexmoor pooled pre/post change: {ce / cp - 1:+.3f}  (no exposure: a negative-control population)")
    # placebo-in-time: the same naive comparison at 21-day windows that end before day 0
    pl = []
    for start in range(-150, -21, 7):
        p, e = naive(d["AP"], pre=(start - 28, start - 1), ev=(start, start + 20))
        pl.append(e / p - 1)
    print(f"AP naive placebo windows: n={len(pl)} min={min(pl):+.3f} max={max(pl):+.3f}")
```

Saída esperada:

```text
site  km  pre28  event  naive_change  relative_to_Wexmoor
AP     6   38.4   51.1        +0.330               +0.246
BF    14   30.4   33.8        +0.112               +0.042
CG    38   22.6   24.5        +0.081               +0.013
W1     -   33.5   37.0        +0.106               +0.036
W2     -   28.1   28.7        +0.022               -0.043
Wexmoor pooled pre/post change: +0.067  (no exposure: a negative-control population)
AP naive placebo windows: n=19 min=-0.064 max=+0.091
```

Leia a saída como um seminário a leria:

- **As estimativas ingênuas superestimam em toda parte.** Alder Point parece subir 33,0% quando a verdade do gerador é 22%; Calloway, a 38 km e de fato não afetado, parece subir 8,1%.
- **A população de controle negativo expõe o viés.** Wexmoor, que não pode ser afetada pelo desvio do Kestrel, "subiu" 6,7% (W1, 10,6%). Qualquer método que encontre um efeito em Wexmoor está medindo outra coisa que não o transbordamento — aqui, a estação.
- **Em relação a Wexmoor, surge um gradiente:** +24,6% a 6 km, +4,2% a 14 km e +1,3% a 38 km. A estimativa de Alder Point está perto da verdade. A de Brookfield é menos da metade dos seus 10% verdadeiros — as estimativas de um único DE são ruidosas, como o Laboratório 3 alertou.
- **As janelas placebo calibram o método ingênuo.** Em 19 janelas falsas durante períodos comuns de linha de base, a variação ingênua em Alder Point foi de −6,4% a +9,1%. Uma variação de +33% está muito fora dessa faixa, então o acaso (R7) é uma explicação improvável para Alder Point — mas as janelas placebo ficam numa linha de base sem estação, então não testam R1. É por isso que as duas ferramentas são necessárias.

Os números em relação a Wexmoor neste laboratório são razões brutas de médias. O Capítulo 6 os substitui por uma série temporal interrompida controlada que também modela a tendência e dá intervalos robustos à autocorrelação.

### 4.9 Erros comuns e limites

- Nomear um rival e declará-lo "controlado" sem declarar a sua previsão distinta.
- Tratar uma região de comparação como automaticamente válida; tendências paralelas são um pressuposto que pode falhar.
- Rotular um desfecho como controle negativo sem argumentar que a exposição não pode afetá-lo.
- Usar janelas placebo de outra estação e tratá-las como um teste do confundimento sazonal.
- Entrevistar em busca de "o que deu errado" e receber retrospectiva.
- Alegar o efeito do "ransomware" quando a exposição foi uma decisão humana tomada em resposta a ele.
- Repetir um relato público inicial de um caso (Oldsmar, Düsseldorf) como se estivesse resolvido.
- Parar a busca por rivais quando o primeiro é tratado.

O limite das ferramentas deste capítulo é que cada uma se apoia num pressuposto que não pode ser totalmente testado com os mesmos dados. A defesa contra esse limite é a triangulação: quando as evidências de tempo, lugar, população, canal e mecanismo apontam todas na mesma direção, os rivais restantes precisam explicar todas elas ao mesmo tempo.

### Exercícios — capítulo 4

**EX021 — Tabela de rivais.** *Objetivo:* listar rivais com previsões distintas. *Insumos:* uma constatação sintética: "após um ataque de ransomware a uma rede regional de farmácias, as dispensações de receitas nas farmácias independentes num raio de 10 km subiram 18% nas duas semanas seguintes." *Restrições:* pelo menos seis rivais. *Passos:* (1) declarar as cinco previsões da hipótese principal (tempo, lugar, população, canal, mecanismo); (2) para cada rival, declarar o que ele prevê de forma diferente; (3) nomear os dados que discriminariam. *Evidência esperada:* tabela. *Rubrica:* 3 = os rivais incluem estação, eventos simultâneos (por exemplo, mudanças de operadoras de planos), medição e choque na região de comparação, cada um com uma previsão distinta e testável; 2 = um rival sem previsão distinta; 1 = lista genérica; 0 = nada.

**EX022 — Duração da linha de base e a estimativa ingênua.** *Objetivo:* mostrar por que um período prévio mais longo desloca a estimativa ingênua antes e depois, enquanto a estimativa relativa a Wexmoor quase não se move. *Insumos:* código do Laboratório 4. *Restrições:* off-line; não alterar a semente. *Passos:* (1) executar o laboratório e registrar a saída; (2) mudar a linha de base ingênua de 28 para 56 dias (`pre=(-56, -1)`) para todos os locais, incluindo a comparação agregada, e relatar as variações ingênuas e relativas a Wexmoor; (3) explicar por que as estimativas ingênuas mudaram, mas as relativas mudaram pouco. *Evidência esperada:* saídas e um parágrafo. *Rubrica:* 3 = valores corretos, explicação de que a estação atinge as duas regiões, de modo que a razão cancela a maior parte do seu efeito, enquanto a estimativa ingênua depende de quanto da linha de base pré-estação ela inclui; 2 = um valor errado; 1 = não executado; 0 = nada.

**EX023 — Diagrama causal.** *Objetivo:* tornar os pressupostos explícitos. *Insumos:* o Spillover Study com um fato a mais: durante o desvio, o condado também abriu uma tenda temporária de pronto atendimento perto de Brookfield. *Restrições:* DAG em texto ou desenhado, com uma descrição textual. *Passos:* (1) acrescentar a tenda ao diagrama; (2) identificar como ela enviesa a estimativa de Brookfield e em que direção; (3) propor dados ou um desenho para tratá-la; (4) declarar se ela ameaça a estimativa de Alder Point. *Evidência esperada:* diagrama, descrição e parágrafo. *Rubrica:* 3 = tenda mostrada como uma cointervenção que afeta as chegadas a Brookfield (provavelmente reduzindo as chegadas espontâneas e possivelmente as de ambulâncias), direção fundamentada, resposta concreta (análise por canal, dados de atendimento da tenda, sensibilidade), Alder Point avaliado pela distância e pela área de captação; 2 = direção não declarada; 1 = diagrama sem fundamentação; 0 = nada.

**EX024 — Controles negativos.** *Objetivo:* argumentar, não rotular. *Insumos:* controles negativos candidatos: (a) chegadas de ambulâncias em Wexmoor; (b) chegadas espontâneas a Alder Point; (c) infusões ambulatoriais agendadas em Alder Point; (d) chegadas de ambulâncias em Calloway. *Restrições:* usar a lógica de Lipsitch et al. *Passos:* para cada um, declarar se é uma população ou um desfecho de controle negativo, se a exposição poderia afetá-lo, se ele compartilha os confundidores, e o seu veredito. *Evidência esperada:* tabela. *Rubrica:* 3 = (a) aceita como população, com a ressalva da estação paralela, (b) rejeitada como controle negativo puro, mas útil para o canal, (c) não afetada pelo desvio, mas provavelmente também não pela estação, portanto fraca, (d) rejeitada porque Calloway faz parte do gradiente de distância da hipótese; 2 = um veredito sem justificativa; 1 = apenas rótulos; 0 = nada.

**EX025 — Uma explicação concorrente documentada.** *Objetivo:* analisar um caso público. *Insumos:* as fontes de Düsseldorf em §4.6 e §2.5. *Restrições:* não especular além das fontes. *Passos:* (1) declarar as duas explicações concorrentes; (2) declarar qual evidência decidiu entre elas, conforme relatado; (3) explicar por que uma alegação sobre uma morte individual e uma alegação no nível da população sobre desvios e desfechos exigem desenhos diferentes; (4) propor uma pergunta no nível da população que possa ser estudada de forma ética. *Evidência esperada:* uma página. *Rubrica:* 3 = explicações declaradas, conclusão baseada na autópsia relatada com a fonte, contrafactual individual versus populacional distinguido, desenho populacional ético proposto (por exemplo, emergências sensíveis ao tempo durante desvios, usando dados agregados de registros); 2 = falta um elemento; 1 = especulação; 0 = nada.

**EX026 — A decisão como exposição.** *Objetivo:* separar o ataque da resposta. *Insumos:* a linha da Colonial Pipeline em §4.6 e o desvio do Kestrel. *Restrições:* meia página. *Passos:* (1) explicar por que a exposição do Spillover Study é o desvio; (2) listar duas formas pelas quais o mesmo ataque poderia ter produzido um desvio diferente; (3) reescrever a alegação do estudo de modo que ela não exagere o papel do ransomware; (4) propor uma pergunta sobre as *decisões* de desvio para um estudo posterior. *Evidência esperada:* parágrafo e alegação. *Rubrica:* 3 = resposta como causa articulada, decisões alternativas plausíveis, alegação delimitada ao desvio, pergunta sobre decisões respondível; 2 = alegação ainda sobre o ransomware em geral; 1 = confunde ataque e desvio; 0 = nada.

### Síntese do capítulo

Mantenha várias explicações ao mesmo tempo e procure observações que as separem. Escreva o padrão completo da hipótese principal — tempo, lugar, população, canal, mecanismo — e exija que cada rival explique todo ele. Um diagrama causal mostra por que uma comparação antes e depois é enviesada pela estação e de que pressuposto uma região de comparação precisa. Populações de comparação, controles negativos, datas placebo, dose–resposta e alinhamento temporal discriminam, cada um, sob um pressuposto que você precisa argumentar. Os casos públicos mostram explicações cibernéticas concorrendo com erro do operador, doença subjacente, decisões preventivas e atualizações defeituosas; a lição é registrar o status e modelar as decisões. O Laboratório 4 mostra um método ingênuo encontrando "transbordamento" a 38 km e numa região não afetada, e uma região de comparação revelando um gradiente próximo da verdade.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 08

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (inglês) →](../../en/book/MANUSCRIPT.md#ch-05)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável e explica o que a rubrica recompensa. Uma resposta diferente pode receber a pontuação máxima quando atende ao mesmo padrão de evidências, escopo e honestidade sobre os limites. Os resultados numéricos vêm dos laboratórios offline deste livro, executados com o Python 3 (a versão 3.13 foi usada neste rascunho) e apenas a biblioteca padrão; se sua saída for diferente, confira primeiro a versão do Python, a semente e se você mudou a ordem dos sorteios aleatórios. Esta edição parcial traz as resoluções de EX001–EX026; as de EX027–EX050 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

### Capítulo 1: EX001–EX007

**EX001 — Do tema à pergunta.** *Problema:* os reguladores estaduais de água potável e as associações de concessionárias não sabem com que frequência os incidentes cibernéticos em concessionárias pequenas interrompem o tratamento ou o monitoramento, nem por quanto tempo, então os programas de apoio não podem ser direcionados. *Pergunta (forma PICOT):* entre os sistemas comunitários de água que atendem de 3.300 a 50.000 pessoas num estado (P), com que frequência os incidentes cibernéticos notificados à agência estadual de primazia (E) coincidiram com uma interrupção registrada do tratamento ou do monitoramento, em comparação com as falhas de equipamento não cibernéticas (C), medida como o número e a duração das interrupções (O) ao longo de cinco anos (T)? *FINER:* viável apenas se os registros de incidentes da agência de primazia distinguirem as causas e puderem ser compartilhados de forma agregada — verifique isso primeiro; interessante para a agência e para as concessionárias; nova se não existir nenhuma descrição em nível estadual; ética porque os registros agregados não envolvem indivíduos, embora o risco de identificação das concessionárias pequenas precise ser tratado (Capítulo 3); relevante porque mostraria se as causas cibernéticas são uma parcela significativa das interrupções. *Alegação esperada:* "Num estado, ao longo de cinco anos, os incidentes cibernéticos registrados responderam por uma parcela declarada das interrupções do tratamento ou do monitoramento, com durações declaradas." *Fora do escopo:* a incidência dos incidentes não notificados; os efeitos sobre a saúde. A nota máxima exige honestidade sobre a viabilidade (os registros podem não codificar a causa de forma confiável) e uma alegação limitada aos incidentes notificados.

**EX002 — Tipos de pergunta.**

| P | Tipo | Desenho mínimo | Alegação mais forte |
|---|---|---|---|
| (a) | Descritiva | Registro completo dos desvios do condado em 2024, com códigos de causa | Horas de desvio por causa naquele condado e naquele ano |
| (b) | Associativa (causal só com mais) | Comparação transversal ou em painel de DEs com e sem simulados, ajustada por porte e perfil de casos | Uma associação entre a adoção dos simulados e os tempos de espera durante as interrupções; causal apenas se o momento da adoção puder ser explorado (por exemplo, uma implantação escalonada) com comparações críveis |
| (c) | Causal | ITS controlada ou equivalente | Variação percentual em relação a um contrafactual, sob pressupostos declarados |
| (d) | Explicativa | Entrevistas com despachantes e equipes, registros do despacho | Um mecanismo apoiado por relatos convergentes |
| (e) | Avaliativa (causal) | ITS em torno do início do protocolo, idealmente com uma região de comparação | Efeito do protocolo sobre o tempo em desvio, sob pressupostos |

O ponto-chave da rubrica é (b): a adoção dos simulados é escolhida pelos hospitais, então os hospitais mais bem geridos tanto adotam os simulados quanto têm esperas menores; sem um desenho que trate disso, a alegação é associativa.

**EX003 — Estratégia de busca e teste dos itens conhecidos.** Blocos como em §1.4.2, com acréscimos como "health information technology failure", "cyber incident" e "EHR outage" no Bloco A e "regional surge", "patient redistribution" e "mutual aid" no Bloco C. Fontes: um índice biomédico (para medicina de emergência e serviços de saúde), um índice acadêmico geral (para economia e administração pública) e um índice de computação (para segurança), cada um justificado pela disciplina que cobre. Literatura cinzenta: órgãos de auditoria (por exemplo, o NAO), agências e ministérios da saúde, declarações de reguladores, relatórios pós-ação de coalizões de saúde e de EMS, levantamentos de associações de hospitais (por exemplo, o da AHA) e órgãos de coordenação setorial. Conjunto de itens conhecidos: Dameff et al. (2023), Ghafur et al. (2019), Neprash et al. (2022); verificar buscando em cada fonte e confirmando que o item aparece nos resultados, revisando a expressão se não aparecer e registrando a revisão. Regra de encerramento: duas rodadas consecutivas de encadeamento sem nenhum novo estudo incluído. Campos do registro: data, fonte, expressão exata, filtros, resultados, nome do arquivo exportado, pessoa. A rubrica recompensa uma busca que encontraria o relatório do NAO — impossível apenas por meio de bases bibliográficas — e uma verificação de itens conhecidos que seja de fato executável.

**EX004 — Deduplicação e concordância.** (1) A saída esperada como em §1.9: 20 identificados, 5 duplicatas, 15 triados, κ = 0,571. (2) Com o registro do "e comercial" acrescentado e `I` acrescentado para os dois revisores, a saída é `records identified: 21  duplicates removed: 5  screened: 16`, `po=0.812 pe=0.547 kappa=0.586`: o registro **não** foi removido. O título normalizado "ransomware emergency department crowding at neighbouring hospitals" difere de "ransomware and emergency department crowding…" porque o normalizador retira o "&", mas não o converte em "and". Correção: substituir "&" por " and " antes de retirar a pontuação e acrescentar uma revisão manual das quase correspondências (por exemplo, títulos cujas formas normalizadas diferem por uma palavra). (3) Partindo do laboratório original, mudar para I a decisão de B sobre o artigo das subestações dá `po=0.733 pe=0.547 kappa=0.412`. (4) A concordância bruta caiu 6,7 pontos, mas o kappa caiu de 0,571 para 0,412 porque o kappa reescala a concordância acima do acaso para a faixa restante: com a concordância ao acaso perto de 0,55, apenas 0,45 da escala é "conquistado", então uma discordância a mais entre 15 registros remove uma grande parte dele.

**EX005 — Repare os critérios de elegibilidade.** Critérios para a literatura cinzenta: *incluir* relatórios de órgãos governamentais, reguladores, órgãos de auditoria, coalizões de saúde, agências de EMS ou associações de hospitais que descrevam os efeitos operacionais (atividade, desvio, atrasos, cancelamentos) de um incidente cibernético ou de uma interrupção de TI específicos sobre uma ou mais organizações de saúde; *excluir* documentos que descrevam procedimentos, orientações ou produtos sem relatar os efeitos de um evento, e material de marketing de fornecedores. Decisões: o memorando do departamento estadual de saúde sobre procedimentos de indisponibilidade → excluir (procedimento sem efeitos), a menos que o texto completo relate os efeitos de um evento; o relatório de exercício da coalizão → excluir para RQ1–2 (um exercício não é um evento), mas mantê-lo numa lista separada de "métodos e planejamento", útil para a RQ3 e para a discussão; o white paper do fornecedor → excluir. Um registro que continue indecidível pela primeira página vai para a revisão do texto completo em vez de ser excluído, para que a incerteza não reduza silenciosamente a base de evidências.

**EX006 — Matriz de conceitos.** Linha do NAO: *unidade* — organizações do NHS na Inglaterra; *exposição* — WannaCry, maio de 2017; *comparação* — nenhuma no sentido estatístico; uma investigação do que aconteceu e por quê; *desfechos* — pelo menos 81 dos 236 trusts afetados, mais 603 organizações de atenção primária e outras do NHS (incluindo 595 consultórios de clínica geral); 6.912 consultas registradas como canceladas e um total estimado de mais de 19.000; *desenho* — investigação de auditoria; *sustenta* — a escala da interrupção e a diferença entre os cancelamentos registrados e os estimados; *rivais levantados ou deixados em aberto* — registro incompleto; desconexão preventiva por organizações não afetadas. Parágrafo-modelo: "As evidências sobre os efeitos regionais vêm de três tipos de estudo. As investigações de auditoria (NAO, 2017) estabelecem a escala da interrupção, mas se apoiam em contagens registradas que subestimam os totais. As análises de dados administrativos (Ghafur et al., 2019) quantificam a redução da atividade nos trusts infectados — cerca de 6% menos internações por hospital infectado por dia — e não encontram diferença nos óbitos em A&E, uma medida que os autores chamam de grosseira. Um estudo antes e depois de DEs vizinhos (Dameff et al., 2023) associa um período de ataque a um aumento de volume em vizinhos não afetados. Nenhum estudo ainda compara os vizinhos com uma região não afetada nem examina a distância…" A rubrica recompensa a distinção entre registrado e estimado e a organização por conceito.

**EX007 — Memorando do estimando e do escopo.** Estimando da RQ1: "Para cada um de Alder Point, Brookfield e Calloway: exp(β₂) − 1, a diferença percentual entre a média diária de chegadas de ambulâncias durante os dias 0–20 e as chegadas esperadas a partir da tendência pré-evento do DE, ajustada pela variação simultânea das chegadas agregadas de Wexmoor." RQ2: "o padrão dessas três estimativas em função da distância, resumido como a diferença entre a estimativa do DE mais próximo e a média das estimativas dos dois DEs mais distantes, com intervalos." Estimandos alternativos que um analista descuidado poderia calcular: o aumento no primeiro dia (capta apenas o choque inicial); o aumento em relação aos mesmos dias do ano anterior (confundido por um ano de tendência e por uma estação diferente); o número total de pacientes adicionais em 21 dias (uma escala diferente, sensível ao tamanho da linha de base). Alegação esperada como em §1.2.1; fora do escopo: desfechos dos pacientes, o efeito do ransomware como distinto do desvio, outras regiões.

### Capítulo 2: EX008–EX014

**EX008 — Perfil setorial (exemplo: água).** Unidade de consequência: pessoas atendidas por um sistema sem água que atenda a um limiar declarado de pressão ou de qualidade, por uma duração declarada, e o número e a duração dos avisos à população. Reservas: armazenamento, dosagem e monitoramento manuais, interconexões com sistemas vizinhos, distribuição de água engarrafada. Instrumentos: o America's Water Infrastructure Act of 2018 (avaliações de risco e resiliência e planos de resposta a emergências para os sistemas comunitários de água que atendem mais de 3.300 pessoas, segundo a página da EPA); na UE, a água potável é um setor da NIS2 e da CER. Evidências: avisos à população (públicos), resumos da agência estadual de primazia, levantamentos com concessionárias, entrevistas; raramente dados operacionais. Pergunta: "Num estado, quantos avisos de fervura da água, ao longo de cinco anos, foram atribuídos pela agência de primazia a falhas de equipamento ou do sistema de controle, e quanto tempo duraram?" Caso público: Oldsmar, codificado com sua revisão (§2.5). A nota máxima exige citações exatas dos instrumentos e uma pergunta ajustada às evidências públicas ou agregadas.

**EX009 — Distorção do catálogo.** (1) Saída como em §2.9. (2) Com o multiplicador em 1,0: a população não muda; catálogo `n=491, mean 31.8 h, median 18.9 h, share>24h 0.42`; contagens anuais catalogadas 99, 73, 90, 75, 77, 77. (3) A distorção da gravidade persiste porque é causada pela divulgação dependente da gravidade, que opera todos os anos independentemente da obrigação; a obrigação muda apenas quantos incidentes são divulgados, e não quais são favorecidos. (A média do catálogo sobe ligeiramente sem a obrigação porque a obrigação admite proporcionalmente mais incidentes curtos.) A tendência desaparece: os anos 4–6 agora se parecem com os anos 1–3, salvo pelo ruído. (4) Pergunta respondível: "Entre os incidentes catalogados, a parcela que envolve uma característica específica (por exemplo, desvio de ambulâncias) mudou após a obrigação?" — ainda afetada se a obrigação mudar *quais* incidentes são divulgados, então as respostas mais seguras descrevem características dentro do catálogo, e não taxas. A rubrica recompensa atribuir cada distorção ao seu mecanismo.

**EX010 — Protocolo do seminário sobre Ghafur et al. (2019).** *Alegação (citada do resumo):* "Entre os hospitais infectados pelo ransomware WannaCry, houve uma redução significativa no número de atendimentos e de internações, o que correspondeu a £5,9 milhões em atividade hospitalar perdida. Não houve aumento relatado da mortalidade, embora esta seja uma medida grosseira de dano ao paciente." *Evidências:* Hospital Episode Statistics dos trusts do NHS na Inglaterra, de 1º de abril a 30 de junho de 2017, agregadas por hospital-dia; 34 trusts infectados comparados com trusts não infectados. *Desenho:* diferença em diferenças por mínimos quadrados ordinários com efeitos fixos de hospital e termos de dia da semana e de feriado bancário, comparando a semana do WannaCry com semanas de linha de base; os desfechos foram consultas ambulatoriais canceladas, internações eletivas e de emergência, atendimentos de A&E e óbitos em A&E. *Garantia:* os trusts não infectados mostram o que os trusts infectados teriam feito naquela semana. *Rivais que o artigo trata:* a flutuação nacional (as semanas anteriores e posteriores são modeladas e a variação de todos os trusts se mostra dentro da volatilidade normal); as diferenças invariantes no tempo entre hospitais (efeitos fixos). *Rivais que ele levanta ou deixa em aberto:* a falha de registro nos trusts infectados — os próprios autores observam que, se os sistemas usados para codificar os dados administrativos estavam fora do ar, os dados podem não refletir plenamente os eventos, um rival de medição específico dos estudos de interrupção de TI; trusts "afetados", mas não infectados, que se desconectaram por precaução, o que complica o grupo de comparação (o artigo os testa separadamente); e a transferência de carga para os vizinhos, que o artigo nomeia como lacuna ("não temos nenhuma compreensão do efeito de rede"). *Transferência:* para sistemas de saúde centralizados, com dados comparáveis e ataques curtos. *E daí:* mesmo um ataque curto teve custos mensuráveis de atividade e financeiros. *Próximo estudo:* a atividade dos hospitais vizinhos durante fechamentos e desvios, que é exatamente a pergunta do Spillover Study. A nota máxima inclui o rival da falha de registro e uma descrição acurada da comparação.

**EX011 — Classificação do mecanismo.**

| Caso | Mecanismo | Unidade de consequência | Fator limitante |
|---|---|---|---|
| (a) Colonial Pipeline | Cascata de dependências (a distribuição de combustível depende do duto), com transferência de carga para rotas alternativas de abastecimento | Produto não entregue; déficits de abastecimento | Estoques e capacidade de transporte alternativo |
| (b) Synnovis | Ambos: os hospitais dependiam dos serviços de patologia (cascata); o trabalho foi redirecionado para outros prestadores (transferência de carga) | Procedimentos e consultas adiados | Capacidade laboratorial em outros lugares |
| (c) Change Healthcare | Cascata de dependências pelo faturamento de convênios e pelo processamento de pagamentos | Perturbação do fluxo de caixa; faturas atrasadas | Processadores alternativos e reservas de caixa |
| (d) Desvio do Kestrel | Transbordamento por transferência de carga | Chegadas excedentes e tempo de espera nos vizinhos | Capacidade ociosa e rotas dos vizinhos |

A rubrica recompensa reconhecer "ambos" onde a substituição se segue à falha de uma dependência.

**EX012 — Codificando um incidente revisado.** Entrada de março de 2021: *alegação* — "um usuário remoto não autorizado mudou o ponto de ajuste do hidróxido de sódio na estação de tratamento de água de Oldsmar"; *fonte* — alerta da CISA AA21-042A e declarações públicas das autoridades locais; *tipo de fonte* — oficial; *data da alegação* — fevereiro de 2021; *situação* — relatada, sob investigação; *última verificação* — março de 2021. Atualização de abril de 2023: manter a alegação original e suas fontes, acrescentar *revisão* — "o ex-administrador municipal declarou que o FBI concluiu que o evento provavelmente foi causado por um funcionário; o FBI disse que não pôde confirmar uma intrusão direcionada" (WUSF, 13 de abril de 2023); *situação* — contestada (ou "não confirmada"); *última verificação* — abril de 2023. Regra de análise: uma análise que conta as intrusões confirmadas exclui a entrada, enquanto uma análise de sensibilidade que inclui as entradas contestadas relata as duas contagens. Procedimento de nova verificação para 2026: buscar declarações oficiais posteriores a abril de 2023 (registros do FBI, atualizações do alerta da CISA), registrar o que foi encontrado e a data.

**EX013 — Contradição aparente.** Dimensões da matriz: unidades (trusts infectados versus vizinhos não afetados), direção esperada (a atividade cai versus sobe), sistema de saúde e ano (NHS 2017 versus San Diego 2021), duração (cerca de uma semana versus um mês), desfechos (internações, atendimentos, cancelamentos, óbitos em A&E versus censo, chegadas, esperas, métricas de AVC), desenho (dados administrativos com linha de base e comparação entre infectados e não infectados versus antes e depois dentro dos vizinhos). Elas não conflitam: medem as extremidades opostas da mesma transferência de carga. Um estudo combinado mediria tanto a atividade perdida da organização atacada quanto a atividade ganha pelos vizinhos no mesmo evento, com uma região de comparação não afetada, para que o efeito regional líquido e sua redistribuição possam ser estimados juntos.

**EX014 — Apresentação no seminário.** Avaliada pela rubrica. Uma entrega de nota máxima resume o artigo nos termos dele antes da crítica; apresenta os rivais como perguntas ("A variação de abril para maio poderia refletir a estação do ano?"); e usa os três registros nas respostas preparadas — por exemplo: "O artigo diz que a organização atacada respondia por cerca de um quarto das altas da região. Eu infiro que a retirada de uma organização menor deslocaria menos carga. Não sei como o resultado diferiria numa região com muitos prestadores; isso exigiria uma comparação entre várias regiões." A reflexão nomeia uma mudança específica de leitura provocada pelos colegas.

### Capítulo 3: EX015–EX020

**EX015 — Escolha e defenda um desenho.** Estimando: variação percentual das transações semanais com cartão por categoria de comércio na região afetada durante a semana da interrupção, em relação ao contrafactual obtido da tendência da própria região e das regiões não afetadas. Comparação: ITS não controlada (falha se ocorrer um choque nacional naquela semana — feriados, dias de pagamento); ITS controlada/diferença em diferenças com três regiões não afetadas (precisa de tendências paralelas; verificável ao longo de dois anos de dados semanais); controle sintético com três regiões doadoras × 40 categorias (possível no nível da categoria, mas três regiões doadoras são um conjunto ralo). Escolha: ITS controlada por categoria, com um controle sintético como robustez. Percepção-chave para a nota máxima: a resolução semanal dilui uma interrupção de três dias — a interrupção ocupa no máximo três sétimos de uma semana —, então os efeitos serão atenuados e a recuperação dentro da mesma semana pode anular parte da queda; peça dados diários antes de se comprometer. Abandono: as razões do período prévio entre a região afetada e as de comparação mostram tendências divergentes ou rupturas que o modelo não consegue absorver.

**EX016 — Análise do desenho.** (1) Saída como em §3.3.3. (2) Com um efeito verdadeiro de 0,20 sob o aumento sazonal, as estimativas médias do desenho controlado são cerca de +0,196, +0,202 e +0,199, e suas parcelas sinalizadas são 0,56 (28 dias), 0,73 (90 dias) e 0,77 (180 dias); o desenho não controlado sinaliza todos os estudos simulados (1,00), mas suas estimativas médias são cerca de +0,30 — enviesadas para cima pela estação. (3) O desenho controlado detecta um efeito de cerca de 20% em aproximadamente três quartos dos estudos com 180 dias de linha de base; não consegue detectar 10% de forma confiável. (4) RQ1 revisada: "Quanto variaram as chegadas diárias de ambulâncias em cada DE vizinho durante o desvio em relação ao contrafactual ajustado pela comparação, e quais variações os dados conseguem descartar?" A rubrica premia a passagem de um enquadramento de teste para um enquadramento de estimação e a declaração honesta do efeito detectável.

**EX017 — Riscos na submissão ao comitê de ética.** Partes interessadas: os operadores entrevistados; a concessionária; seus clientes; a agência reguladora com primazia; as concessionárias vizinhas que compartilham pessoal ou interconexões; o pesquisador. Riscos e salvaguardas por princípio do Menlo: *respeito às pessoas* — uma concessionária pequena pode ter dois ou três operadores, então qualquer descrição de função os identifica; relatar as funções apenas no nível do setor, revisar as citações, permitir a desistência; *beneficência* — publicar que o monitoramento da desinfecção de uma concessionária pequena falhou por horas poderia revelar uma fraqueza que outros poderiam explorar; reter a identidade da instalação e os detalhes técnicos, compartilhar os detalhes em privado com a concessionária; *justiça* — evitar concentrar o ônus da pesquisa em concessionárias pequenas e com poucos recursos que não podem recusar um pesquisador ligado a um regulador; *lei e interesse público* — cumprir quaisquer obrigações de confidencialidade relativas às informações de segurança da concessionária e as regras da instituição para pesquisa com seres humanos. Texto da folha de informações: "Não usaremos o seu nome nem o nome da sua concessionária em nada que publicarmos e removeremos os detalhes que possam identificá-lo. Como poucas pessoas fazem o seu trabalho nesta região, alguém que conheça bem a concessionária ainda poderia reconhecê-lo, e não podemos descartar isso por completo."

**EX018 — Plano de gestão de dados.**

| Ativo | Nível | Armazenamento e acesso | Retenção | Compartilhamento no fim do projeto |
|---|---|---|---|---|
| Contagens diárias dos custodiantes | Restrito | Armazenamento institucional criptografado; candidato e orientador | Conforme o acordo (por exemplo, cinco anos), depois destruídas | Não compartilhadas; acesso por meio dos custodiantes |
| Contagens do painel de Wexmoor | Fonte pública, termos registrados | Armazenamento do projeto com a data de captura | Conforme os termos do painel | Compartilhadas se os termos permitirem a redistribuição; caso contrário, compartilhar o método de captura |
| Gravações das entrevistas | Confidencial | Criptografadas, separadas dos dados | Destruídas após a transcrição e a verificação | Nunca |
| Transcrições desidentificadas | Confidencial (no máximo restrito) | Criptografadas | Conforme o consentimento | Não compartilhadas; apenas citações na dissertação |
| Livro de códigos (dados e qualitativo) | Público | Repositório | Permanente | Compartilhado |
| Código de análise e dados de teste sintéticos | Público | Repositório | Permanente | Compartilhados sob uma licença aberta |
| Termos de consentimento | Confidencial | Trancados ou criptografados, separados | Conforme a política institucional | Nunca |
| Limiares de ajuda mútua da coalizão | Restrito (sensível) | Criptografados | Conforme o acordo | Não compartilhados; descritos apenas de forma geral |

**EX019 — Plano de pré-análise.** Um plano de nota máxima fixa: os estimandos (EX007); o desfecho primário (chegadas diárias de ambulâncias, conforme definidas nos dicionários de dados dos custodiantes) e o desfecho secundário (mediana diária de minutos da chegada até o primeiro clínico); a comparação (DEs de Wexmoor agregados); as janelas (dias −180 a +89; desvio 0–20; período posterior 21–89); o modelo (§6.2, razão logarítmica com deslocamento de 0,5, tendência linear, dois degraus); os intervalos (Newey–West, defasagem 7; defasagens 0 e 14 como sensibilidade); a robustez (cada DE de Wexmoor separadamente; linhas de base de 90 e 120 dias; janelas do evento de 14 e 28 dias; feriados excluídos; janelas placebo); a multiplicidade (um desfecho primário; três locais relatados em conjunto; desfecho secundário descrito como tal); os desvios (registro datado com a razão e se os resultados tinham sido vistos); o acesso prévio aos dados ("um extrato de 35 dias de linha de base de Alder Point, anterior ao dia −60, foi examinado apenas quanto à completude").

**EX020 — Auditoria da reprodutibilidade.** Avaliado pela rubrica. Problemas típicos que uma segunda pessoa encontra: o README não diz que o Laboratório 6 precisa do Laboratório 4 salvo como `lab4_data.py` na mesma pasta; a versão do Python não está registrada; uma saída foi produzida com uma semente editada; o Laboratório 3 leva vários segundos e parece travado. Correções: ordem de execução e nomes de arquivo explícitos; `python3 --version` registrado em `environment.txt`; sementes declaradas junto a cada comando; tempos de execução esperados declarados.

### Capítulo 4: EX021–EX026

**EX021 — Tabela de rivais (exemplo das farmácias).** Previsões da hipótese principal: as dispensações sobem nas independentes quando começa a interrupção da rede e voltam a cair quando ela termina; o aumento é maior perto das lojas da rede; não há aumento em áreas comparáveis não afetadas; o canal são as transferências de clientes novos (pacientes novos na farmácia independente), e não pacientes existentes dispensando mais; os farmacêuticos relatam transferências. Rivais: *estação* (receitas da estação respiratória — prevê aumentos em toda parte; testar com uma área de comparação); *mudança de operadora ou de formulário naquela semana* (prevê variações ligadas a medicamentos ou planos específicos; testar por classe de medicamento e por pagador); *medição* (um acúmulo no sistema de autorizações liberando dispensações atrasadas — prevê um pico de dispensações datadas antes, mas processadas tarde; testar a data da dispensação versus a data do processamento); *choque na comparação* (testar cada área de comparação separadamente); *fechamentos de lojas da rede não relacionados ao ataque* (testar os registros por loja); *acaso* (semanas placebo). A nota máxima exige previsões distintas, e não uma lista de temas.

**EX022 — Duração da linha de base e a estimativa ingênua.** Com `pre=(-56, -1)` para todos os locais e para a comparação agregada:

| Local | Pré (56 dias) | Evento | Variação ingênua | Relativa a Wexmoor |
|---|---:|---:|---:|---:|
| AP | 39,2 | 51,1 | +0,302 | +0,235 |
| BF | 30,2 | 33,8 | +0,118 | +0,060 |
| CG | 22,9 | 24,5 | +0,069 | +0,014 |
| W1 | 35,3 | 37,0 | +0,050 | −0,004 |
| W2 | 27,1 | 28,7 | +0,059 | +0,005 |

A variação de Wexmoor agregada é +0,054. As estimativas ingênuas mudam (Alder Point de +33,0% para +30,2%) porque a linha de base agora cobre outro trecho da série, com outro ruído e um nível sazonal ligeiramente diferente; as estimativas relativas mudam pouco (Alder Point de +24,6% para +23,5%; Calloway de +1,3% para +1,4%) porque a estação afeta as duas regiões de forma semelhante, de modo que a parte da estação que a linha de base inclui é em grande parte cancelada na razão. W1 e W2 em relação a Wexmoor agregada ficam perto de zero por construção, já que compõem a comparação agregada.

**EX023 — Diagrama causal.** Acrescente um nó "Tenda" com as setas Tenda → chegadas espontâneas a Brookfield (forte) e Tenda → chegadas de ambulâncias a Brookfield (possível, se o EMS levou pacientes de baixa gravidade à tenda). A tenda é uma **cointervenção** simultânea ao desvio e concentrada perto de Brookfield. Se ela absorveu pacientes de baixa gravidade, ela *reduz* as chegadas a Brookfield e enviesa a estimativa de transbordamento de Brookfield **em direção a zero** (ou abaixo). Ela também distorce o gradiente da RQ2, fazendo a queda de Alder Point para Brookfield parecer mais acentuada. Respostas: obter o atendimento diário da tenda; analisar separadamente os canais de ambulâncias e de chegadas espontâneas; executar uma análise de sensibilidade que acrescente de volta os atendimentos da tenda que os registros do EMS atribuem à área de captação de Brookfield. Alder Point é menos afetado se a sua área de captação não se sobrepõe à da tenda; verificar com os registros de destino do EMS.

**EX024 — Controles negativos.**

| Candidato | Tipo | A exposição poderia afetá-lo? | Compartilha os confundidores? | Veredito |
|---|---|---|---|---|
| (a) Chegadas em Wexmoor | População | Não (outra região, sem EMS compartilhado) | Sim, a estação, se for semelhante | Aceitar, com a ressalva da estação paralela |
| (b) Chegadas espontâneas a Alder Point | Desfecho | Sim, se os pacientes que teriam ido por conta própria ao Kestrel foram para outro lugar | Sim | Rejeitar como controle negativo puro; usar como comparação de canais |
| (c) Infusões ambulatoriais agendadas em Alder Point | Desfecho | Improvável | Provavelmente não — o atendimento agendado não é movido pela estação respiratória | Fraco: não revelaria o confundimento sazonal |
| (d) Chegadas em Calloway | População/desfecho | Possivelmente, num nível pequeno — faz parte da hipótese da distância | Sim | Rejeitar: usá-lo como controle negativo presume a resposta da RQ2 |

**EX025 — Uma explicação concorrente documentada.** Explicações: o atraso no tratamento causado pelo desvio decorrente do ataque causou a morte, versus a condição subjacente da paciente. Conforme relatado publicamente, os promotores concluíram, após a autópsia, que o atraso não foi decisivo e que a condição médica sozinha causou a morte (MIT Technology Review, novembro de 2020). Uma alegação sobre uma morte individual exige o contrafactual individual — *esta* paciente teria sobrevivido com um tratamento mais precoce? —, que uma autópsia e uma revisão clínica às vezes conseguem tratar; uma alegação no nível da população pergunta se os desfechos de um *grupo* de pacientes sensíveis ao tempo pioram durante os desvios, o que exige comparar grupos e não diz nada definitivo sobre nenhuma morte isolada. Pergunta populacional ética: "Durante desvios de ambulâncias num centro regional de AVC, os tempos da porta ao tratamento dos pacientes com AVC na região variaram, em relação a períodos comparáveis sem desvio?" — usando dados agregados ou de registros, com as aprovações adequadas.

**EX026 — A decisão como exposição.** A exposição do estudo é o desvio porque foi ele que deslocou as ambulâncias; o ataque importou por meio da decisão de desviar. Duas decisões alternativas: o Kestrel poderia ter permanecido aberto às ambulâncias com procedimentos de contingência (sem desvio, pouco transbordamento), ou desviado apenas categorias específicas, como AVC e trauma (transbordamento parcial concentrado nos centros especializados). Alegação reescrita: "Num evento sintético, um desvio de ambulâncias de 21 dias após um ataque de ransomware foi seguido de um aumento estimado de 24% nas chegadas de ambulâncias ao DE vizinho mais próximo; o resultado diz respeito às consequências do desvio tal como decidido, e não do ransomware enquanto tal." Pergunta posterior: "Que informações e critérios os dirigentes hospitalares usam para decidir se e por quanto tempo desviar ambulâncias durante um incidente cibernético, e como essas decisões variam?"

<a id="glossary"></a>

## Glossário

- **Trilha de auditoria (audit trail)** — O livro de códigos, os memorandos e as versões de uma análise qualitativa que permitem a outra pessoa acompanhar como os códigos se tornaram temas.
- **Autocorrelação** — Correlação entre os valores de uma série (ou os resíduos de um modelo) em dias próximos; ela deixa as estimativas de mínimos quadrados sem viés, mas torna errados seus erros-padrão usuais.
- **Kappa de Cohen (κ)** — Concordância entre dois avaliadores além da que suas frequências marginais produziriam ao acaso: (observada − acaso) / (1 − acaso).
- **Matriz de conceitos** — Uma tabela que organiza os estudos pelos conceitos de que trata uma revisão (unidades, exposição, comparação, desfechos, desenho, rivais), para que a síntese avance por conceito, e não autor por autor.
- **Série temporal interrompida controlada (CITS)** — Uma série temporal interrompida analisada em relação a uma série de comparação que não foi exposta, para que os choques compartilhados, como a estação do ano, sejam removidos.
- **Caminho crítico** — A cadeia de tarefas cujo atraso atrasa o projeto inteiro; numa dissertação de mestrado, geralmente as aprovações e os acordos de dados.
- **Cascata de dependências** — A propagação de uma perturbação de um fornecedor que falhou para os serviços que dependem dele.
- **Análise do desenho** — Simular um estudo planejado sobre dados gerados com efeitos conhecidos para conhecer seu viés, sua precisão e sua probabilidade de detectar efeitos de tamanho plausível antes de coletar os dados reais.
- **Registro de desvios** — Um registro datado de cada mudança num plano registrado, sua razão e se os dados de desfecho já tinham sido vistos quando ela foi feita.
- **Grafo acíclico dirigido (DAG)** — Um diagrama das relações causais presumidas, usado para identificar fatores de confusão, mediadores e colisores.
- **Limitação direcional** — Uma limitação declarada com a direção provável e o tamanho aproximado de seu viés, o que foi feito a respeito e o que a resolveria.
- **Discordância** — Em métodos mistos, um resultado numa vertente que conflita com a outra; relatado e explicado, em vez de resolvido deixando uma vertente vencer.
- **Desvio (desvio de ambulâncias)** — O pedido de um hospital para que as ambulâncias levem os pacientes a outros hospitais; neste livro, a exposição do Spillover Study.
- **Estimando** — A quantidade precisa que um estudo pretende estimar: unidade, desfecho, contraste de exposição, janela de tempo e medida-resumo.
- **FINER** — Viável (feasible), interessante, nova (novel), ética e relevante: critérios para uma pergunta de pesquisa.
- **Literatura cinzenta** — Relatórios e documentos produzidos fora da publicação acadêmica comercial (auditorias, relatórios de agências, revisões pós-ação).
- **Poder de informação (information power)** — A ideia de que, quanto mais informação relevante cada participante tiver para um objetivo estreito, menos entrevistas são necessárias.
- **Exibição conjunta (joint display)** — Uma tabela que emparelha os resultados quantitativos com as constatações qualitativas e declara uma metainferência para cada linha.
- **Conjunto de itens conhecidos** — Estudos que já se sabe serem relevantes, usados para verificar se uma estratégia de busca os recupera.
- **Transbordamento por transferência de carga** — A propagação de uma perturbação por substituição: a demanda que o prestador perturbado não consegue atender passa para outros.
- **Metainferência** — A conclusão tirada da integração de duas vertentes: confirmação, expansão ou discordância.
- **Múltiplas hipóteses de trabalho** — Manter várias explicações ao mesmo tempo e desenhar evidências que discriminem entre elas.
- **Controle negativo** — Um desfecho ou uma população que a exposição não deveria afetar, mas que compartilha os fatores de confusão do estudo, usado para detectar viés.
- **Erros-padrão de Newey–West (HAC)** — Erros-padrão robustos à heterocedasticidade e à autocorrelação até uma defasagem escolhida, usando pesos de Bartlett decrescentes.
- **Tendências paralelas** — O pressuposto de que, sem a exposição, as séries tratada e de comparação teriam se movido juntas.
- **PICOT (forma para infraestrutura)** — População ou unidades, exposição, comparação, desfecho e tempo, usados para tornar uma pergunta respondível.
- **Estudo piloto (de viabilidade)** — Um estudo pequeno que testa se o estudo principal pode ser feito como planejado — dados, instrumentos e procedimentos —, e não se a hipótese é verdadeira.
- **Teste placebo no tempo** — Ajustar o modelo principal a janelas anteriores ao evento real, onde nenhum efeito deveria existir, e classificar a estimativa real entre as estimativas placebo.
- **Plano de pré-análise** — Uma especificação registrada e datada dos estimandos, dos desfechos, dos modelos e das verificações de robustez, escrita antes que os dados de desfecho sejam vistos.
- **Critérios de progressão** — Limiares definidos antes de um piloto que decidem se o estudo principal prossegue, prossegue após emenda ou para.
- **Procedência (de um número)** — O caminho rastreável de um número no texto de volta ao código e à saída que o produziram.
- **Regressão à média** — A tendência de medições incomumente extremas serem seguidas por outras menos extremas, o que pode imitar um efeito quando as unidades são selecionadas por valores extremos.
- **Viés de relato (viés de catálogo)** — Distorção nos catálogos de incidentes porque quais incidentes são divulgados depende de sua gravidade, das obrigações e da atenção.
- **Registro de resultados e alegações** — Uma tabela que liga cada alegação da dissertação a seu resultado, à força das evidências e ao verbo que as evidências permitem.
- **Revisão de escopo** — Uma revisão que mapeia a extensão e os tipos de evidências sobre uma pergunta ampla, em vez de agregar efeitos.
- **Regressão segmentada** — Regressão com termos de nível e de inclinação que mudam numa interrupção; o modelo usual para séries temporais interrompidas.
- **Curva de especificação** — O conjunto de estimativas de todas as escolhas analíticas razoáveis, exibidas juntas para que nenhuma escolha isolada carregue a conclusão.
- **Controle sintético** — Uma combinação ponderada de unidades não expostas, escolhida para reproduzir a trajetória pré-evento da unidade exposta, usada como seu contrafactual.
- **Análise temática** — Um método para identificar, analisar e relatar padrões de significado em dados qualitativos, em seis fases.

<a id="references"></a>

## Referências

Leis, orientações e páginas públicas de incidentes mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas. A lista é idêntica à da edição em inglês, com o acréscimo da LGPD, citada na §3.4.

**Políticas, leis e normas**

- Bank for International Settlements, Committee on Payments and Market Infrastructures, and International Organization of Securities Commissions. [Guidance on Cyber Resilience for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d146.htm). June 2016.
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- European Union. [Regulation (EU) 2022/2554 on digital operational resilience for the financial sector (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Department of Health and Human Services. [Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html).
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).
- U.S. Government. [45 CFR Part 46 — Protection of Human Subjects](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46). Electronic Code of Federal Regulations.

**Incidentes e evidências setoriais**

- American Hospital Association. [AHA Survey: Change Healthcare Cyberattack Significantly Disrupts Patient Care, Hospitals' Finances](https://www.aha.org/2024-03-15-aha-survey-change-healthcare-cyberattack-significantly-disrupts-patient-care-hospitals-finances). 15 March 2024.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Dameff, C., Tully, J., Chan, T. C., et al. [Ransomware Attack Associated With Disruptions at Adjacent Emergency Departments in the US](https://doi.org/10.1001/jamanetworkopen.2023.12270). *JAMA Network Open*, 6(5), e2312270, 2023.
- Ghafur, S., Kristensen, S., Honeyford, K., Martin, G., Darzi, A., and Aylin, P. [A Retrospective Impact Analysis of the WannaCry Cyberattack on the NHS](https://doi.org/10.1038/s41746-019-0161-6). *npj Digital Medicine*, 2, 98, 2019.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- MIT Technology Review. [Ransomware Did Not Kill a German Hospital Patient](https://www.technologyreview.com/2020/11/12/1012015/ransomware-did-not-kill-a-german-hospital-patient/). 12 November 2020.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Neprash, H. T., McGlave, C. C., Cross, D. A., et al. [Trends in Ransomware Attacks on US Hospitals, Clinics, and Other Health Care Delivery Organizations, 2016–2021](https://doi.org/10.1001/jamahealthforum.2022.4873). *JAMA Health Forum*, 3(12), e224873, 2022.
- NHS England (London). [Update on Cyber Incident: Clinical Impact in South East London — Friday 14 June 2024](https://www.england.nhs.uk/london/2024/06/14/update-on-cyber-incident-clinical-impact-in-south-east-london-friday-14-june-2024/). 14 June 2024.
- U.S. Department of Energy, Office of Cybersecurity, Energy Security, and Emergency Response. [Colonial Pipeline Cyber Incident](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident).
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Perguntas, revisões e argumentação**

- Arksey, H., and O'Malley, L. [Scoping Studies: Towards a Methodological Framework](https://doi.org/10.1080/1364557032000119616). *International Journal of Social Research Methodology*, 8(1), 19–32, 2005.
- Chamberlin, T. C. [The Method of Multiple Working Hypotheses](https://doi.org/10.1126/science.148.3671.754). *Science*, 148(3671), 754–759, 1965 (reprint of the 1890 paper).
- Farrugia, P., Petrisor, B. A., Farrokhyar, F., and Bhandari, M. [Research Questions, Hypotheses and Objectives](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912019/). *Canadian Journal of Surgery*, 53(4), 278–281, 2010.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71). *BMJ*, 372, n71, 2021.
- Platt, J. R. [Strong Inference](https://doi.org/10.1126/science.146.3642.347). *Science*, 146(3642), 347–353, 1964.
- Snyder, H. [Literature Review as a Research Methodology: An Overview and Guidelines](https://doi.org/10.1016/j.jbusres.2019.07.039). *Journal of Business Research*, 104, 333–339, 2019.
- Tricco, A. C., Lillie, E., Zarin, W., et al. [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/M18-0850). *Annals of Internal Medicine*, 169(7), 467–473, 2018.
- Webster, J., and Watson, R. T. [Analyzing the Past to Prepare for the Future: Writing a Literature Review](https://www.jstor.org/stable/4132319). *MIS Quarterly*, 26(2), xiii–xxiii, 2002.
- Wohlin, C. [Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering](https://doi.org/10.1145/2601248.2601268). *Proceedings of the 18th International Conference on Evaluation and Assessment in Software Engineering (EASE)*, 2014.

**Desenho e análise quantitativos**

- Abadie, A. [Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects](https://doi.org/10.1257/jel.20191450). *Journal of Economic Literature*, 59(2), 391–425, 2021.
- Barnett, A. G., van der Pols, J. C., and Dobson, A. J. [Regression to the Mean: What It Is and How to Deal With It](https://doi.org/10.1093/ije/dyh299). *International Journal of Epidemiology*, 34(1), 215–220, 2005.
- Durbin, J., and Watson, G. S. [Testing for Serial Correlation in Least Squares Regression. I](https://doi.org/10.1093/biomet/37.3-4.409). *Biometrika*, 37(3–4), 409–428, 1950.
- Gelman, A., and Loken, E. [The Statistical Crisis in Science](https://doi.org/10.1511/2014.111.460). *American Scientist*, 102(6), 460, 2014.
- Goodman-Bacon, A. [Difference-in-Differences with Variation in Treatment Timing](https://doi.org/10.1016/j.jeconom.2021.03.014). *Journal of Econometrics*, 225(2), 254–277, 2021.
- Greenland, S., Pearl, J., and Robins, J. M. [Causal Diagrams for Epidemiologic Research](https://doi.org/10.1097/00001648-199901000-00008). *Epidemiology*, 10(1), 37–48, 1999.
- Hategeka, C., Ruton, H., Karamouzian, M., Lynd, L. D., and Law, M. R. [Use of Interrupted Time Series Methods in the Evaluation of Health System Quality Improvement Interventions: A Methodological Systematic Review](https://doi.org/10.1136/bmjgh-2020-003567). *BMJ Global Health*, 5, e003567, 2020.
- Hernán, M. A., and Robins, J. M. [Causal Inference: What If](https://miguelhernan.org/whatifbook). Chapman & Hall/CRC, 2020 (open online edition).
- Lakens, D. [Sample Size Justification](https://doi.org/10.1525/collabra.33267). *Collabra: Psychology*, 8(1), 33267, 2022.
- Lipsitch, M., Tchetgen Tchetgen, E., and Cohen, T. [Negative Controls: A Tool for Detecting Confounding and Bias in Observational Studies](https://doi.org/10.1097/EDE.0b013e3181d61eeb). *Epidemiology*, 21(3), 383–388, 2010.
- Lopez Bernal, J., Cummins, S., and Gasparrini, A. [Interrupted Time Series Regression for the Evaluation of Public Health Interventions: A Tutorial](https://doi.org/10.1093/ije/dyw098). *International Journal of Epidemiology*, 46(1), 348–355, 2017.
- Newey, W. K., and West, K. D. [A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix](https://doi.org/10.2307/1913610). *Econometrica*, 55(3), 703–708, 1987.
- Roth, J., Sant'Anna, P. H. C., Bilinski, A., and Poe, J. [What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature](https://doi.org/10.1016/j.jeconom.2023.03.008). *Journal of Econometrics*, 235(2), 2218–2244, 2023.
- Simonsohn, U., Simmons, J. P., and Nelson, L. D. [Specification Curve Analysis](https://doi.org/10.1038/s41562-020-0912-z). *Nature Human Behaviour*, 4, 1208–1214, 2020.
- Steegen, S., Tuerlinckx, F., Gelman, A., and Vanpaemel, W. [Increasing Transparency Through a Multiverse Analysis](https://doi.org/10.1177/1745691616658637). *Perspectives on Psychological Science*, 11(5), 702–712, 2016.
- Wagner, A. K., Soumerai, S. B., Zhang, F., and Ross-Degnan, D. [Segmented Regression Analysis of Interrupted Time Series Studies in Medication Use Research](https://doi.org/10.1046/j.1365-2710.2002.00430.x). *Journal of Clinical Pharmacy and Therapeutics*, 27(4), 299–309, 2002.
- Wasserstein, R. L., and Lazar, N. A. [The ASA Statement on p-Values: Context, Process, and Purpose](https://doi.org/10.1080/00031305.2016.1154108). *The American Statistician*, 70(2), 129–133, 2016.

**Métodos qualitativos e mistos**

- Braun, V., and Clarke, V. [Using Thematic Analysis in Psychology](https://doi.org/10.1191/1478088706qp063oa). *Qualitative Research in Psychology*, 3(2), 77–101, 2006.
- Cohen, J. [A Coefficient of Agreement for Nominal Scales](https://doi.org/10.1177/001316446002000104). *Educational and Psychological Measurement*, 20(1), 37–46, 1960.
- Fetters, M. D., Curry, L. A., and Creswell, J. W. [Achieving Integration in Mixed Methods Designs — Principles and Practices](https://doi.org/10.1111/1475-6773.12117). *Health Services Research*, 48(6 Pt 2), 2134–2156, 2013.
- Fischhoff, B. [Hindsight ≠ Foresight: The Effect of Outcome Knowledge on Judgment Under Uncertainty](https://doi.org/10.1037/0096-1523.1.3.288). *Journal of Experimental Psychology: Human Perception and Performance*, 1(3), 288–299, 1975.
- Guest, G., Bunce, A., and Johnson, L. [How Many Interviews Are Enough? An Experiment with Data Saturation and Variability](https://doi.org/10.1177/1525822X05279903). *Field Methods*, 18(1), 59–82, 2006.
- Malterud, K., Siersma, V. D., and Guassora, A. D. [Sample Size in Qualitative Interview Studies: Guided by Information Power](https://doi.org/10.1177/1049732315617444). *Qualitative Health Research*, 26(13), 1753–1760, 2016.
- McHugh, M. L. [Interrater Reliability: The Kappa Statistic](https://doi.org/10.11613/BM.2012.031). *Biochemia Medica*, 22(3), 276–282, 2012.
- O'Connor, C., and Joffe, H. [Intercoder Reliability in Qualitative Research: Debates and Practical Guidelines](https://doi.org/10.1177/1609406919899220). *International Journal of Qualitative Methods*, 19, 2020.

**Pilotos, relato, reprodutibilidade e exame**

- Benchimol, E. I., Smeeth, L., Guttmann, A., et al. [The REporting of Studies Conducted Using Observational Routinely-Collected Health Data (RECORD) Statement](https://doi.org/10.1371/journal.pmed.1001885). *PLOS Medicine*, 12(10), e1001885, 2015.
- Eldridge, S. M., Chan, C. L., Campbell, M. J., et al. [CONSORT 2010 Statement: Extension to Randomised Pilot and Feasibility Trials](https://doi.org/10.1136/bmj.i5239). *BMJ*, 355, i5239, 2016.
- Lancaster, G. A., Dodd, S., and Williamson, P. R. [Design and Analysis of Pilot Studies: Recommendations for Good Practice](https://doi.org/10.1111/j..2002.384.doc.x). *Journal of Evaluation in Clinical Practice*, 10(2), 307–312, 2004.
- Leon, A. C., Davis, L. L., and Kraemer, H. C. [The Role and Interpretation of Pilot Studies in Clinical Research](https://doi.org/10.1016/j.jpsychires.2010.10.008). *Journal of Psychiatric Research*, 45(5), 626–629, 2011.
- Mullins, G., and Kiley, M. ['It's a PhD, Not a Nobel Prize': How Experienced Examiners Assess Research Theses](https://doi.org/10.1080/0307507022000011507). *Studies in Higher Education*, 27(4), 369–386, 2002.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606, 2018.
- O'Brien, B. C., Harris, I. B., Beckman, T. J., Reed, D. A., and Cook, D. A. [Standards for Reporting Qualitative Research: A Synthesis of Recommendations (SRQR)](https://doi.org/10.1097/ACM.0000000000000388). *Academic Medicine*, 89(9), 1245–1251, 2014.
- Open Science Framework. [OSF Registries](https://osf.io/registries).
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLOS Computational Biology*, 9(10), e1003285, 2013.
- Thabane, L., Ma, J., Chu, R., et al. [A Tutorial on Pilot Studies: The What, Why and How](https://doi.org/10.1186/1471-2288-10-1). *BMC Medical Research Methodology*, 10, 1, 2010.
- The Turing Way Community. [The Turing Way: A Handbook for Reproducible, Ethical and Collaborative Research](https://book.the-turing-way.org/).
- Tong, A., Sainsbury, P., and Craig, J. [Consolidated Criteria for Reporting Qualitative Research (COREQ): A 32-Item Checklist for Interviews and Focus Groups](https://doi.org/10.1093/intqhc/mzm042). *International Journal for Quality in Health Care*, 19(6), 349–357, 2007.
- von Elm, E., Altman, D. G., Egger, M., et al. [The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) Statement: Guidelines for Reporting Observational Studies](https://doi.org/10.1016/S0140-6736(07)61602-X). *The Lancet*, 370(9596), 1453–1457, 2007.
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18). *Scientific Data*, 3, 160018, 2016.

Material complementar do CyberABC: o [livro de doutorado sobre Infraestrutura Crítica](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md), que leva os métodos de pesquisa deste livro a uma contribuição original baseada em simulação.

**Limite do caso.** Tamsin Valley, Kestrel Health, o Alder Point Hospital, o Brookfield Community Hospital, o Calloway General, o Tamsin Valley EMS, a central de despacho do condado, a Tamsin Valley Healthcare Coalition, a região de Wexmoor e seus hospitais, os entrevistados I01–I10, os registros com DOIs começando por 10.9999/syn, o Spillover Study e todos os números produzidos pelos laboratórios foram inventados para o ensino. As fontes apoiam as afirmações gerais ao lado das quais são citadas, nunca os detalhes sintéticos.

**Metadados da edição.** Edição em rascunho, outubro de 2026; tradução para o português de outubro de 2026. Revisor: pendente. Verificação A4: ainda não renderizada.
