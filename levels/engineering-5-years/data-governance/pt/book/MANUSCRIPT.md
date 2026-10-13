# Governança de Dados: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 118, engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–50 de 50 têm texto didático escrito à mão; os exercícios EX001–EX150 têm resoluções correspondentes com rubricas de 0 a 3; os quatro laboratórios offline (capítulos 22, 28, 29 e 32) usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de engenharia que aprendem a construir, verificar e operar a governança de dados de medidores e sensores de uma companhia de saneamento.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios rastreiam a linhagem a montante e lacunas de titularidade em um grafo sintético de *pipeline*, calculam taxas de aprovação de três regras de leitura de medidores, medem a pontualidade dos fluxos em relação a um nível de serviço às 06:00 e conciliam leituras de campo sintéticas com o faturamento. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um estudante de engenharia desde os fundamentos de matemática, medição, programação e sistemas, passando por requisitos, modelos, controles, implementação, verificação, operação e validação da governança, até um projeto final, um ensaio de recuperação, um dossiê de evidências, um trabalho de conclusão e a defesa final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Kofi Mensah** | Estudante de engenharia | Inventado |
| **Profa. Elena Varga** | Orientadora | Inventada |
| **Politécnica Northfield** | Politécnica fictícia | Inventada |
| **Tidewater Water** | Companhia de saneamento fictícia, com cerca de 400.000 clientes e 90.000 medidores inteligentes | Inventada |

### Fontes principais

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-8:2015; Khatri e Brown (2010), [doi:10.1145/1629175.1629210](https://doi.org/10.1145/1629175.1629210); Wang e Strong (1996); Batini et al. (2009); NIST SP 800-188; NIST SP 800-30r1. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) usar taxas de variação para descrever fluxos de dados; (2) relacionar derivadas ao monitoramento de volumes de dados; (3) ler uma curva de crescimento para planejar armazenamento.

### 1.1 O estudante e a companhia de saneamento

Kofi Mensah inicia um curso de engenharia de cinco anos na fictícia Politécnica Northfield, sob orientação da Profa. Elena Varga. A empresa parceira do estágio é a fictícia Tidewater Water, que abastece cerca de 400.000 clientes, lê 90.000 medidores inteligentes a cada hora e monitora sua rede de tubulações com sensores de vazão. Na Tidewater, governança de dados significa decidir quem é dono dos dados de medidores, sensores e clientes, que regras de qualidade se aplicam e por quanto tempo os registros são guardados. A Profa. Varga explica que cada disciplina de matemática será ligada a essas decisões por meio dos dados da Tidewater. As leituras chegam sem parar.

### 1.2 Taxas de variação

O cálculo começa pelas taxas de variação. Se o volume de leituras de medidores armazenadas é uma função do tempo, sua derivada diz à Tidewater com que rapidez o armazenamento cresce. Kofi modela as leituras armazenadas como leituras por hora multiplicadas pelo número de medidores e pelas horas decorridas, o que dá uma taxa constante de cerca de 2,16 milhões de leituras por dia. Quando a Tidewater acrescenta 10.000 medidores a cada trimestre, a própria taxa aumenta, e a segunda derivada passa a ser positiva. Ele aprende que um plano de governança para retenção precisa usar a taxa, e não apenas o total atual.

### 1.3 Monitoramento com derivadas

Kofi aplica a ideia ao monitoramento. Uma queda brusca na taxa de leituras recebidas, isto é, uma grande variação negativa da derivada, pode indicar que um fluxo de dados falhou, e não que os clientes deixaram de usar água. Hoje a equipe de dados da Tidewater acompanha apenas totais diários, que escondem problemas hora a hora. Kofi propõe calcular a taxa por hora e sinalizar variações maiores que uma fração definida. Ele observa que essa visão matemática se torna um controle de governança, porque um fluxo ausente afeta o faturamento e os relatórios de perdas mais adiante na cadeia.

### 1.4 Planejando o armazenamento

Com uma integral, Kofi estima o armazenamento total ao longo de sete anos, o prazo que a tabela de temporalidade da Tidewater fixa para as evidências de faturamento. Com o número de medidores crescendo linearmente, o total de leituras cresce de forma quadrática no tempo, de modo que o armazenamento no sétimo ano supera em muito um simples múltiplo do primeiro. A Profa. Varga pede que ele compare isso com uma política que agrega as leituras horárias em totais diários depois de dois anos. A integral mostra uma grande redução, o que ilustra como as decisões de retenção também são decisões de engenharia sobre custo e risco.

### Exemplo resolvido

Kofi modela o crescimento do armazenamento como uma taxa, usa variações dessa taxa para detectar fluxos com falha e integra ao longo de sete anos para comparar a retenção completa com a agregação depois de dois anos.

> **Caso sintético.** Northfield, Tidewater e todas as pessoas são sintéticos.

### Erros e limites

O crescimento linear é uma suposição; revise-a quando os planos de instalação de medidores mudarem.

### Exercícios

- **EX001 — Taxa diária.** Aproximadamente quantas leituras chegam por dia? *Rubrica:* 3 = cerca de 2,16 milhões;; 2 = próximo;; 1 = errado;; 0 = nenhuma.
- **EX002 — Falha de fluxo.** O que pode significar uma queda brusca na taxa de leituras? *Rubrica:* 3 = um fluxo de dados com falha;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX003 — Efeito da agregação.** O que faz a agregação em totais diários depois de dois anos? *Rubrica:* 3 = reduz muito o armazenamento;; 2 = menciona redução;; 1 = vago;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) usar conjuntos e relações para descrever a titularidade dos dados; (2) modelar dependências como grafos; (3) raciocinar sobre chaves e funções.

### 2.1 Conjuntos de dados

Kofi descreve os dados da Tidewater como conjuntos: clientes, imóveis, medidores e leituras. A interseção dos clientes com uma lista de atendimento prioritário identifica domicílios vulneráveis que precisam de apoio extra durante interrupções no abastecimento. As operações de conjuntos tornam precisas as perguntas de governança. Por exemplo, o conjunto de medidores com leituras, mas sem imóvel vinculado, deveria ser vazio; se não for, algumas leituras não podem ser faturadas nem explicadas. Ele escreve essas condições como regras que depois podem ser verificadas automaticamente nos dados reais. Cada regra nomeia os conjuntos que compara e o resultado esperado.

### 2.2 Relações e chaves

Uma relação liga elementos de dois conjuntos, como medidores e imóveis. Kofi verifica se ela é uma função: cada medidor deveria corresponder a exatamente um imóvel em cada momento. Na réplica sintética, doze medidores correspondem a dois imóveis por causa de uma antiga migração de dados. Ele explica que uma chave é um atributo que identifica cada elemento de forma única, e que chaves quebradas criam ambiguidade sobre quem é dono de qual leitura. Definir chaves e verificá-las é uma das primeiras tarefas da governança de dados.

### 2.3 Grafos de dependências

Kofi modela os sistemas da Tidewater como um grafo dirigido, com uma aresta de cada sistema para os sistemas que usam seus dados. O sistema de faturamento depende das leituras dos medidores e das tarifas; o relatório de perdas depende dos volumes faturados e das vazões dos sensores. Seguir as arestas no sentido inverso, a partir de um relatório, mostra todas as fontes das quais ele depende. Ele observa que a alcançabilidade em grafos será a base da análise de linhagem mais adiante no curso, quando ele rastrear exatamente quais fontes alimentam um número apresentado ao conselho da Tidewater. Ciclos são sinalizados.

### 2.4 Lógica para regras

As regras de governança podem ser expressas em lógica. Kofi escreve: para toda leitura, se o medidor está ativo, então a leitura tem um imóvel. Ele também escreve a contrapositiva e a verifica com exemplos. A Profa. Varga mostra como regras lógicas precisas evitam desentendimentos entre equipes, porque frases ambíguas como todas as leituras devem ser válidas escondem significados diferentes. Ele aprende que escrever as regras formalmente antes torna mais consistentes tanto sua implementação posterior em código quanto sua explicação aos gestores. Regras formais também facilitam derivar casos de teste depois.

### Exemplo resolvido

Kofi usa conjuntos para definir condições de regras, encontra doze medidores vinculados a dois imóveis, modela os sistemas como um grafo de dependências e escreve regras de qualidade em forma lógica.

> **Caso sintético.** A réplica é sintética.

### Erros e limites

Regras formais ainda podem codificar o requisito errado; valide-as com os donos dos dados.

### Exercícios

- **EX004 — Regra do conjunto vazio.** Que conjunto deveria ser vazio? *Rubrica:* 3 = medidores com leituras mas sem imóvel vinculado;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX005 — Verificação de função.** Quantos medidores correspondiam a dois imóveis? *Rubrica:* 3 = doze;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX006 — Uso do grafo.** O que mostra seguir as arestas no sentido inverso a partir de um relatório? *Rubrica:* 3 = todas as fontes das quais ele depende;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar a medição física à qualidade dos dados; (2) explicar o erro e a deriva de sensores; (3) registrar metadados de medição.

### 3.1 Medição e dados

Os sensores de vazão da Tidewater convertem grandezas físicas em números. Kofi aprende que toda medição tem incerteza, vinda do instrumento, da instalação e do ambiente. Um sensor de vazão próximo a uma curva da tubulação lê de forma diferente de outro instalado em um trecho reto. Por isso, a governança de dados precisa registrar como cada valor foi medido, porque um número sem o contexto da medição pode ser mal utilizado. Ele observa que a ênfase da ISO 8000 em requisitos inclui saber se os dados são precisos o bastante para o uso pretendido. O contexto acompanha os valores.

### 3.2 Erro e deriva

A exatidão dos sensores muda com o tempo. Incrustações dentro dos tubos e o envelhecimento da eletrônica causam deriva, uma mudança lenta e sistemática nas leituras. Kofi estuda dados sintéticos de um sensor que lê dois por cento acima do real depois de três anos. Se a deriva não for detectada, as estimativas de perdas caem, porque o volume fornecido parece maior do que é. Ele propõe comparar anualmente os sensores com medidores de referência calibrados e registrar as datas de calibração como metadados, para que os analistas possam excluir ou corrigir leituras fora do período de calibração. Sem uma medição de referência independente, a deriva é invisível.

### 3.3 Unidades e conversões

Um erro comum nos dados de companhias de saneamento é a confusão de unidades: metros cúbicos versus litros, ou vazões horárias versus diárias. Kofi encontra um caso sintético em que as leituras de um distrito foram armazenadas em litros enquanto as demais usavam metros cúbicos, o que inflou mil vezes a demanda desse distrito em um relatório. Ele recomenda armazenar a unidade explicitamente com cada valor e validar, na ingestão, se ela corresponde à esperada. A lição de física vira uma regra de governança: nunca armazene um valor medido sem a sua unidade. Unidades são campos obrigatórios.

### 3.4 Metadados de medição

Kofi projeta um registro de metadados para cada sensor: identificador, localização, tipo, unidade, classe de exatidão, data de instalação, data da última calibração e responsável. O registro permite que analistas julguem se as leituras atendem às suas necessidades e que engenheiros programem a manutenção. A Profa. Varga lembra que metadados também são dados e precisam de regras de qualidade próprias, como a de que datas de calibração não podem estar no futuro. Kofi inclui o registro em suas notas de governança como o primeiro exemplo de gestão de metadados. Cada campo tem um formato definido e um responsável por mantê-lo atualizado.

### Exemplo resolvido

Kofi explica a incerteza de medição, modela o efeito de uma deriva de dois por cento sobre as perdas, encontra um erro de litros versus metros cúbicos e projeta metadados de sensores com datas de calibração.

> **Caso sintético.** Os dados de sensores são sintéticos; a ISO 8000-1:2022 é real.

### Erros e limites

A calibração reduz a incerteza, mas não a elimina; informe-a.

### Exercícios

- **EX007 — Efeito da deriva.** Como uma deriva para cima do sensor afeta as estimativas de perdas? *Rubrica:* 3 = as perdas parecem menores;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX008 — Erro de unidade.** O que a confusão de unidades fez com um distrito? *Rubrica:* 3 = inflou mil vezes a demanda;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX009 — Campos de metadados.** Cite três campos de metadados de sensor. *Rubrica:* 3 = identificador, localização, tipo, unidade, exatidão, instalação, calibração, responsável;; 2 = três;; 1 = um;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever scripts que leem e validam arquivos de dados; (2) tratar erros de forma explícita; (3) manter o código legível para revisores.

### 4.1 Lendo arquivos de dados

Kofi escreve seus primeiros scripts em Python usando o módulo csv da biblioteca padrão para ler leituras sintéticas de medidores. Cada linha tem um identificador de medidor, um carimbo de data e hora, uma leitura e uma unidade. Ele aprende a ler os arquivos linha a linha, converter textos em números com cuidado e guardar os valores originais para fins de rastreabilidade. A Profa. Varga exige dados sintéticos em todos os exercícios, porque scripts de estudantes costumam imprimir dados durante a depuração e nunca devem expor informações reais de clientes. Cada script também imprime, ao final, quantas linhas foram lidas, aceitas e rejeitadas.

### 4.2 Validação no código

Kofi acrescenta verificações: o identificador do medidor precisa seguir um padrão, o carimbo de data e hora precisa ser interpretável, a leitura precisa ser um número não negativo e a unidade precisa ser metros cúbicos. As linhas que falham vão para um arquivo de rejeitos, com o motivo, e não são descartadas em silêncio. Ele explica que o descarte silencioso esconde problemas de qualidade dos donos dos dados, enquanto um arquivo de rejeitos lhes dá evidências para corrigir a origem. Contar os rejeitos por motivo também mostra quais problemas são mais comuns. O motivo mais frequente na primeira execução é a falta de unidade.

### 4.3 Tratando erros

Quando falta uma coluna em um arquivo, o script de Kofi para com uma mensagem clara, em vez de adivinhar. Quando uma única linha está malformada, ele registra o problema e continua. Ele distingue os erros que tornam todo o resultado não confiável dos erros que afetam apenas um registro. A Profa. Varga chama isso de falhar alto na estrutura e falhar baixo no conteúdo, e observa que a governança depende de scripts que tornam os problemas visíveis, em vez de produzir resultados confiantes a partir de entradas quebradas. Os dois comportamentos são testados com arquivos propositalmente defeituosos.

### 4.4 Código legível

Kofi dá nomes claros às variáveis, escreve uma docstring explicando o que cada script lê e produz e mantém as funções curtas. Um colega revisa o código e encontra um erro de deslocamento de uma unidade (*off-by-one*) no tratamento dos carimbos de data e hora, que Kofi corrige e cobre com um teste. Ele aprende que a revisão de código é um controle de qualidade do próprio código que impõe a qualidade dos dados, e que código legível é mais fácil de revisar, manter e confiar quando outras pessoas dependem do resultado. O teste agora roda automaticamente sempre que alguém altera a função de carimbo de data e hora.

### Exemplo resolvido

Kofi lê arquivos de medidores com csv, valida quatro campos, grava rejeitos com motivos, interrompe a execução em erros estruturais e corrige, com um teste, um defeito de carimbo de data e hora encontrado na revisão.

> **Caso sintético.** Os arquivos são sintéticos.

### Erros e limites

As regras de validação no código se afastam das regras escritas; revise as duas juntas.

### Exercícios

- **EX010 — Arquivo de rejeitos.** Por que gravar um arquivo de rejeitos em vez de descartar linhas? *Rubrica:* 3 = dá aos donos evidências para corrigir a origem;; 2 = menciona evidências;; 1 = vago;; 0 = nenhuma.
- **EX011 — Política de erros.** O que significa falhar alto na estrutura e baixo no conteúdo? *Rubrica:* 3 = parar quando falta coluna, registrar linhas ruins e continuar;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX012 — Achado da revisão.** O que a revisão de código encontrou? *Rubrica:* 3 = um erro *off-by-one* nos carimbos de data e hora;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever notas técnicas claras sobre dados; (2) apresentar achados de qualidade de dados a não especialistas; (3) documentar decisões.

### 5.1 Escrevendo para engenheiros

Kofi escreve uma nota técnica sobre o erro de unidade do Capítulo 3. A Profa. Varga pede uma estrutura fixa: resumo, contexto, método, achados, impacto e recomendações. O resumo apresenta o problema e sua consequência em duas frases: as leituras de um distrito foram armazenadas em litros, o que inflou sua demanda no relatório mensal. Assim, os engenheiros que leem a nota decidem rapidamente se vale a pena continuar. Uma estrutura clara torna as notas mais fáceis de encontrar e reutilizar quando um problema parecido surgir anos depois. As notas ficam em um índice compartilhado.

### 5.2 Escrevendo para gestores

Para o gerente de operações da Tidewater, Kofi escreve uma versão de uma página, sem código nem fórmulas. Ela explica o que deu errado, quais relatórios foram afetados, o que já foi corrigido e qual decisão é necessária: a aprovação para incluir a validação de unidades em todos os fluxos de dados. Ele inclui um gráfico comparando a demanda informada com a corrigida. O gerente aprova a mudança no mesmo dia. Kofi aprende que os gestores precisam da decisão e de suas consequências, não de todo o percurso técnico que levou até elas. O gráfico usa rótulos de eixo em linguagem simples.

### 5.3 Apresentando a incerteza

Quando apresenta estimativas de perdas afetadas pela deriva dos sensores, Kofi mostra faixas em vez de números únicos e explica em palavras simples por que a faixa existe. Alguns gestores preferem um único número, então ele dá uma estimativa central e mantém a faixa visível. A Profa. Varga observa que esconder a incerteza pode levar a decisões ruins, enquanto sobrecarregar as pessoas com detalhes técnicos pode levar a nenhuma decisão. A habilidade está em mostrar incerteza suficiente para ser honesto e útil. A faixa aparece em todos os slides.

### 5.4 Registros de decisão

Kofi inicia um registro das decisões de governança de dados da Tidewater: data, decisão, quem decidiu, opções consideradas e evidências. A primeira entrada registra a aprovação da validação de unidades. Ele explica que o DAMA-DMBOK2 enfatiza políticas e decisões documentadas, porque as organizações esquecem por que as regras existem. Meses depois, quando alguém pergunta por que um fluxo é rejeitado por unidade errada, o registro responde sem depender da memória de ninguém. O registro fica no mesmo repositório do código de validação, de modo que código e justificativas permanecem juntos.

### Exemplo resolvido

Kofi escreve uma nota técnica estruturada e uma versão de uma página para o gestor, que obtém a aprovação da validação de unidades, apresenta as perdas como uma faixa e inicia um registro de decisões.

> **Caso sintético.** As notas são sintéticas; o DAMA-DMBOK2 é real.

### Erros e limites

Resumos curtos podem perder ressalvas; mantenha visível a principal limitação.

### Exercícios

- **EX013 — Estrutura da nota.** Que estrutura a Profa. Varga exigiu? *Rubrica:* 3 = resumo, contexto, método, achados, impacto, recomendações;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX014 — Decisão do gestor.** Que decisão o gestor tomou? *Rubrica:* 3 = aprovar a validação de unidades em todos os fluxos;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX015 — Conteúdo do registro.** O que contém um registro de decisão? *Rubrica:* 3 = data, decisão, quem decidiu, opções, evidências;; 2 = a maioria;; 1 = um;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar integrais para calcular volumes a partir de vazões; (2) estimar erros numéricos; (3) relacionar acumulação e conciliação.

### 6.1 Da vazão ao volume

Os sensores da Tidewater registram a vazão a cada quinze minutos. O volume fornecido em um dia é a integral da vazão ao longo do tempo. Kofi a aproxima pela regra dos trapézios com dados sintéticos e compara o resultado com o volume calculado pelo macromedidor do distrito. Os dois concordam com diferença de meio por cento. Ele explica que esse cálculo alimenta a estimativa de perdas, de modo que o método usado para integrar a vazão é, ele próprio, uma decisão de processamento de dados que deve ser documentada e aplicada de forma consistente. O método é incluído no padrão de relatórios.

### 6.2 Erro numérico

Kofi testa como o intervalo de amostragem afeta o erro. Com amostras horárias em vez de amostras de quinze minutos, a estimativa pelos trapézios perde picos curtos de demanda e difere do macromedidor em dois por cento. Ele mostra que reduzir o intervalo à metade divide o erro aproximadamente por quatro em vazões suaves, como a teoria prevê, mas não em picos repentinos. O achado alimenta uma pergunta de governança: que intervalo de amostragem é necessário para que os dados sirvam ao relatório de perdas, e quem define esse requisito? O relatório de perdas precisa de dados de quinze minutos.

### 6.3 Acumulação e conciliação

Integrais acumulam. Pequenos erros na vazão se somam, ao longo de um mês, em grandes diferenças de volume. Kofi calcula uma conciliação mensal entre o volume fornecido, medido pelos sensores, e o volume faturado, medido pelos hidrômetros. A diferença representa perdas, mais erro de medição, mais diferenças de calendário nas leituras. Ele aprende que a conciliação é um controle central de governança de dados no saneamento, porque liga duas fontes independentes e revela quando uma delas tem um problema. A diferença de cada mês é acompanhada ao longo do tempo, e um salto repentino leva a verificar os dois fluxos antes que alguém conclua que as perdas aumentaram.

### 6.4 Séries para previsão

Kofi usa uma expansão em série simples para aproximar uma curva de demanda que sobe pela manhã. Os primeiros termos capturam a maior parte da forma, enquanto os termos seguintes acrescentam pouco. A Profa. Varga explica que a mesma ideia aparece na governança de dados: um pequeno número de medidas de qualidade bem escolhidas costuma capturar a maior parte do risco, enquanto muitas medidas extras acrescentam custo e confusão. Kofi registra isso como um princípio de projeto para o trabalho de medição que fará nos capítulos seguintes. Menos medidas, e melhores, vencem.

### Exemplo resolvido

Kofi integra a vazão pela regra dos trapézios com diferença de meio por cento em relação ao macromedidor, mostra que a amostragem horária eleva o erro para dois por cento e liga a acumulação à conciliação mensal.

> **Caso sintético.** Os dados de vazão são sintéticos.

### Erros e limites

A regra dos trapézios supõe vazão suave entre as amostras; picos a invalidam.

### Exercícios

- **EX016 — Concordância da integração.** Quão perto do macromedidor ficou a estimativa pelos trapézios? *Rubrica:* 3 = dentro de meio por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX017 — Erro horário.** Que erro a amostragem horária produziu? *Rubrica:* 3 = cerca de dois por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX018 — Componentes da conciliação.** O que contém a diferença entre fornecido e faturado? *Rubrica:* 3 = perdas, erro de medição, diferenças de calendário;; 2 = todos;; 1 = um;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar taxas de erro a partir de amostras; (2) construir intervalos de confiança; (3) usar limites de controle para monitorar a qualidade.

### 7.1 Amostragem para qualidade

A Tidewater não consegue inspecionar cada leitura manualmente, então Kofi trabalha com amostras. Ele sorteia 400 leituras sintéticas e confere cada uma com a fotografia do medidor tirada pela equipe de campo. Oito discordam. A taxa de erro estimada é de 2 por cento. Ele explica que uma amostra aleatória permite uma estimativa válida da taxa de erro de toda a população, enquanto amostras escolhidas por conveniência, como apenas os medidores de fácil acesso, podem ser enviesadas e induzir a decisões erradas sobre a qualidade dos dados. A amostra é sorteada por um script com semente fixa, para que qualquer pessoa possa sortear os mesmos medidores e repetir as verificações.

### 7.2 Intervalos de confiança

Kofi calcula um intervalo de confiança de 95 por cento para a taxa de erro pelo método de Wilson, que se comporta bem com proporções pequenas. O intervalo vai de cerca de 1,0 a 3,9 por cento. Ele informa o intervalo, e não apenas a estimativa pontual, porque a meta de qualidade da Tidewater é de 3 por cento e o intervalo inclui valores acima disso. Portanto, o dono dos dados não pode afirmar com confiança que a meta foi cumprida, e Kofi recomenda uma amostra maior no trimestre seguinte. Com 400 leituras e oito erros, o intervalo é largo; uma amostra de 1.600 o estreitaria consideravelmente.

### 7.3 Gráficos de controle

Para o monitoramento contínuo, Kofi plota a proporção diária de leituras rejeitadas com limites de controle a três desvios-padrão da média de longo prazo. Pontos fora dos limites sinalizam uma mudança que vale investigar. Nos dados sintéticos, um dia ultrapassa o limite superior, e a causa se revela uma atualização de firmware em um lote de medidores. Ele aprende que os gráficos de controle separam a variação normal dos problemas reais e evitam que as equipes persigam ruído aleatório ou ignorem mudanças reais. O firmware do lote é revertido, e no dia seguinte a proporção volta para dentro dos limites.

### 7.4 Estatística e governança

A Profa. Varga liga a estatística à governança. Metas de qualidade significam pouco se não forem bem medidas. Uma meta de 3 por cento de erros exige um plano de amostragem, um método de intervalo e um responsável que aja quando os limites forem ultrapassados. Kofi inclui esses elementos em um padrão de medição para os dados de medidores da Tidewater. Ele observa que Batini e colegas descrevem a avaliação como uma etapa das metodologias de qualidade, e que a estatística transforma a avaliação de opinião em evidência que gestores e auditores podem verificar. O padrão nomeia o responsável por cada etapa e a ação exigida.

### Exemplo resolvido

Kofi estima uma taxa de erro de 2 por cento a partir de 400 leituras sorteadas, informa um intervalo de Wilson de cerca de 1,0 a 3,9 por cento, detecta uma mudança de firmware com um gráfico de controle e escreve um padrão de medição.

> **Caso sintético.** As leituras são sintéticas; Batini et al. (2009) é real.

### Erros e limites

Os limites de controle supõem processos estáveis; recalcule-os depois de mudanças conhecidas.

### Exercícios

- **EX019 — Estimativa de erro.** Que taxa de erro a amostra indicou? *Rubrica:* 3 = 2 por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX020 — Julgamento da meta.** Por que o dono não pode afirmar que a meta de 3 por cento foi cumprida? *Rubrica:* 3 = o intervalo inclui valores acima de 3 por cento;; 2 = menciona intervalo;; 1 = vago;; 0 = nenhuma.
- **EX021 — Sinal de controle.** O que causou o dia fora dos limites? *Rubrica:* 3 = uma atualização de firmware em um lote de medidores;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) relacionar os limites do hardware ao tratamento de dados; (2) entender os dispositivos de borda na medição; (3) considerar a integridade na transmissão e no armazenamento.

### 8.1 Dispositivos de borda

Cada medidor inteligente contém um pequeno processador, memória e um rádio. Kofi aprende que os medidores guardam as leituras localmente e as transmitem em lotes, de modo que uma falha de rádio causa atraso, e não perda, dos dados, até o limite da memória. Um medidor com sete dias de armazenamento perde leituras se ficar mais tempo sem transmitir. A governança precisa conhecer esses limites, porque uma regra que marca leituras atrasadas como inválidas rejeitaria indevidamente dados legítimos que chegaram atrasados depois de uma falha. A regra de dados atrasados é ajustada de acordo.

### 8.2 Representação de dados

Kofi estuda como as leituras são representadas. Os medidores guardam contagens inteiras de litros para evitar arredondamentos de ponto flutuante, e o sistema central (*head-end*) converte os valores para metros cúbicos. Um defeito que converte duas vezes divide os valores por mil. Ele também nota que os carimbos de data e hora são guardados em UTC nos medidores, mas exibidos no horário local, e que as mudanças de horário de verão criam horas aparentemente duplicadas ou ausentes. Escolhas de representação são detalhes de engenharia de baixo nível com efeitos diretos sobre a qualidade dos dados de faturamento. Os carimbos passam a ser guardados em UTC em todos os sistemas, e o horário local é usado apenas para exibição aos clientes.

### 8.3 Verificações de integridade

Os medidores anexam uma soma de verificação (*checksum*) a cada lote, para que o receptor detecte corrupção na transmissão. Kofi explica que um *checksum* detecta erros acidentais, mas não prova quem enviou os dados. A Tidewater também usa autenticação de mensagens para mostrar que as leituras vieram de medidores genuínos. Ele mapeia onde cada verificação acontece e descobre que as leituras passam por uma plataforma do fornecedor onde as verificações não são registradas, o que cria uma lacuna de evidências sobre a integridade entre o medidor e os sistemas da Tidewater. O fornecedor concorda em registrar as verificações.

### 8.4 Camadas de armazenamento

A Tidewater guarda as leituras recentes em armazenamento rápido, para o faturamento, e as mais antigas em armazenamento de arquivo, mais barato. Kofi observa que mover dados entre camadas é um ponto em que dados podem ser perdidos ou alterados. Ele recomenda comparar contagens de registros e *checksums* antes e depois de cada migração. A Profa. Varga explica que decisões de arquitetura, como a separação em camadas, também são decisões de governança, porque determinam a rapidez com que os dados podem ser recuperados para consultas de clientes, auditorias ou demandas judiciais. O primeiro teste de migração revela que faltam três dias de leituras na cópia de arquivo.

### Exemplo resolvido

Kofi liga os limites de memória dos medidores às regras de dados atrasados, encontra riscos de dupla conversão e de horário de verão, mapeia as verificações de integridade com uma lacuna no fornecedor e recomenda contagens e *checksums* nas migrações entre camadas.

> **Caso sintético.** Os dispositivos são sintéticos.

### Erros e limites

*Checksums* detectam acidentes, não adulterações; use autenticação para comprovar a origem.

### Exercícios

- **EX022 — Limite de sete dias.** Quando um medidor perde leituras? *Rubrica:* 3 = falha mais longa que seu período de armazenamento;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX023 — Horário de verão.** Que problema o horário de verão cria? *Rubrica:* 3 = horas aparentemente duplicadas ou ausentes;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX024 — Limite do checksum.** O que um *checksum* não prova? *Rubrica:* 3 = quem enviou os dados;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar o código de processamento de dados em módulos testados; (2) escrever testes unitários para regras de qualidade; (3) usar controle de versão para mudanças de regras.

### 9.1 Módulos

Kofi reorganiza seus scripts em módulos: um para ler arquivos, um para as regras de validação e um para os relatórios. Cada módulo tem uma interface clara. O módulo de validação expõe uma lista de regras, cada uma com nome, descrição e função. Essa estrutura permite que os donos dos dados leiam as descrições das regras sem ler código, e que os engenheiros acrescentem ou alterem regras sem mexer no leitor nem no gerador de relatórios. Ele observa que uma separação clara reduz a chance de mudanças acidentais afetarem comportamentos não relacionados. As descrições das regras formam um catálogo.

### 9.2 Testes unitários para regras

Para cada regra, Kofi escreve testes unitários com casos sintéticos que devem passar e casos que devem falhar. O teste da regra que proíbe leituras menores que a anterior inclui uma troca de medidor, em que as leituras voltam legitimamente a zero. A primeira versão da regra rejeita trocas de forma indevida, e o teste revela isso. Ele acrescenta à regra um indicador de troca de medidor. A Profa. Varga enfatiza que os testes documentam o comportamento pretendido das regras tão claramente quanto qualquer política escrita. O indicador vem do sistema de ordens de serviço.

### 9.3 Controle de versão

Todas as mudanças de regras passam pelo controle de versão, com uma mensagem explicando o motivo. Quando a exceção para troca de medidor é incluída, a mensagem do commit aponta para o registro de decisão. Kofi consegue mostrar exatamente quando uma regra mudou e comparar os relatórios de qualidade antes e depois. Ele explica que o histórico de versões é evidência para auditores e para donos de dados que notam uma mudança repentina na taxa de rejeição e querem saber se mudaram os dados ou as regras. Toda mudança na lista de regras é revisada por um segundo engenheiro antes de entrar no ramo principal.

### 9.4 Revisão de código para regras de dados

Kofi pede a um engenheiro de medição, e não só a um programador, que revise as regras. O engenheiro aponta que alguns medidores mais antigos enviam leituras apenas uma vez por dia, de modo que uma regra de completude horária os reprovaria injustamente. Kofi acrescenta o tipo de medidor como parâmetro. Ele aprende que especialistas do domínio encontram erros que revisores de código não veem, e que as regras de governança precisam de correção técnica e de correção de negócio para serem úteis, e não apenas aplicáveis. Os medidores diários passam a ser avaliados por uma regra de completude diária, e sua taxa de rejeição cai ao mesmo nível dos medidores horários.

### Exemplo resolvido

Kofi organiza o código em módulos com regras nomeadas, escreve testes que encontram um erro na troca de medidores, liga as mudanças de regras às decisões no controle de versão e obtém uma revisão do domínio que acrescenta o tipo de medidor.

> **Caso sintético.** O código e os dados são sintéticos.

### Erros e limites

Os testes cobrem apenas os casos que alguém imaginou; acrescente casos tirados de incidentes reais.

### Exercícios

- **EX025 — Estrutura da regra.** O que cada regra expõe? *Rubrica:* 3 = nome, descrição e função;; 2 = todos;; 1 = um;; 0 = nenhuma.
- **EX026 — Achado do teste.** O que o teste unitário revelou? *Rubrica:* 3 = a regra rejeitava indevidamente trocas de medidor;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX027 — Revisão do domínio.** O que o engenheiro de medição apontou? *Rubrica:* 3 = medidores antigos enviam leituras só uma vez por dia;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética da engenharia a decisões sobre dados; (2) considerar os impactos de dados ruins sobre a segurança das pessoas; (3) lidar com conflitos de interesse.

### 10.1 Ética no trabalho com dados

Os códigos de ética da engenharia pedem que os engenheiros coloquem a segurança e o bem-estar do público acima de tudo e ajam com honestidade dentro de sua competência. Kofi aplica esses deveres aos dados. Uma leitura errada de um sensor de pressão pode levar os operadores a reduzir a pressão e deixar um hospital sem água, enquanto uma leitura errada de qualidade da água pode esconder uma contaminação. A governança de dados tem, portanto, consequências para a segurança, e os engenheiros que gerenciam dados compartilham a responsabilidade por elas mesmo sem nunca tocar em um tubo. Kofi escreve esses deveres no alto de seu caderno do curso, para lembrar por que seu trabalho com dados importa.

### 10.2 Clientes vulneráveis

A Tidewater mantém um cadastro de atendimento prioritário de clientes que dependem de água para equipamentos médicos ou precisam de ajuda durante interrupções. Kofi reconhece que esse cadastro contém informações de saúde e precisa ser exato, seguro e usado apenas para sua finalidade. Um cadastro desatualizado pode fazer com que um cliente em diálise domiciliar não seja avisado durante uma falta de água. Ele recomenda uma confirmação anual com cada cliente cadastrado e limites rígidos de acesso, equilibrando segurança e privacidade. Somente a equipe de incidentes e o atendimento ao cliente podem abrir o cadastro, e cada acesso é registrado.

### 10.3 Relatórios honestos

O supervisor de Kofi na Tidewater pede que ele apresente apenas a estimativa de perdas que fica dentro da meta regulatória, omitindo a estimativa mais alta, que considera a deriva dos sensores. Kofi reconhece um conflito entre a pressão para parecer bem e o dever de relatar com honestidade. Ele apresenta as duas estimativas, explica a deriva e recomenda calibração. A Profa. Varga o apoia e observa que os reguladores confiam nos dados das companhias, de modo que relatórios seletivos podem distorcer decisões públicas. Mais tarde, o supervisor lhe agradece, porque naquele mesmo ano a auditoria do regulador pergunta justamente sobre a calibração dos sensores.

### 10.4 Competência e limites

Pedem a Kofi que aprove uma mudança no processamento dos dados de qualidade da água. Ele reconhece que não tem o conhecimento de química necessário para julgar se a mudança poderia mascarar uma contaminação e encaminha a decisão a uma cientista qualificada em qualidade da água. Ele registra o encaminhamento no registro de decisões. A Profa. Varga explica que conhecer os limites da própria competência é um dever ético, especialmente quando decisões sobre dados podem afetar a saúde e a segurança públicas. A cientista aprova uma versão revisada da mudança, depois de acrescentar uma verificação que sinaliza leituras acima do limite de segurança.

### Exemplo resolvido

Kofi liga erros de dados à segurança das pessoas, protege o cadastro de atendimento prioritário, apresenta as duas estimativas de perdas apesar da pressão e encaminha uma decisão sobre qualidade da água que está além de sua competência.

> **Caso sintético.** Os casos são sintéticos.

### Erros e limites

A pressão ética costuma ser sutil; registre as decisões e seus motivos.

### Exercícios

- **EX028 — Exemplo de segurança.** Dê uma consequência de dados ruins para a segurança das pessoas. *Rubrica:* 3 = uma leitura de pressão errada deixa um hospital sem água;; 2 = menciona dano;; 1 = vago;; 0 = nenhuma.
- **EX029 — Cuidado com o cadastro.** O que Kofi recomendou para o cadastro prioritário? *Rubrica:* 3 = confirmação anual e acesso restrito;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX030 — Competência.** Por que Kofi encaminhou a mudança na qualidade da água? *Rubrica:* 3 = faltava-lhe competência em química;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) rastrear como os dados de medidores e sensores atravessam as redes; (2) avaliar escolhas de protocolo quanto à integridade e à disponibilidade; (3) documentar os fluxos de dados na rede para fins de governança.

### 11.1 Caminhos pela rede

As leituras dos medidores viajam por rádio até concentradores instalados em postes, depois por uma rede móvel até a plataforma central (*head-end*) de um fornecedor e, por fim, pela internet até o data center da Tidewater. As leituras dos sensores seguem um caminho separado, por uma rede industrial privada, até o sistema de controle. Kofi desenha os dois caminhos e identifica cada salto com o protocolo, o operador e se os dados estão criptografados. Ele descobre que o responsável pela governança muda a cada fronteira, o que explica por que ninguém conseguia responder a perguntas sobre atrasos ou perdas de ponta a ponta.

### 11.2 Protocolos e integridade

O caminho dos medidores usa um protocolo criptografado e autenticado do concentrador até o *head-end*, de modo que as leituras ficam protegidas contra adulteração em trânsito. A rede industrial usa um protocolo mais antigo, sem autenticação, que depende do isolamento da rede. Kofi observa que isso não torna errados os dados dos sensores, mas significa que a Tidewater não consegue provar, só pelo protocolo, que uma leitura veio de um sensor genuíno. Ele registra a lacuna e recomenda monitorar o aparecimento de dispositivos inesperados na rede industrial. Agora um alerta dispara para dispositivos desconhecidos.

### 11.3 Disponibilidade e armazenamento temporário

Falhas de rede atrasam os dados. Os concentradores guardam leituras por até dois dias, e a rede móvel às vezes cai por horas. Kofi mede, em registros sintéticos, com que frequência as leituras chegam com mais de seis horas de atraso e descobre que a maioria dos atrasos se concentra em períodos de tempestade. Ele argumenta que os consumidores dos dados, como o faturamento, precisam saber com quanto atraso os dados podem chegar legitimamente, para não tratarem leituras atrasadas como ausentes nem estimarem contas sem necessidade antes da chegada das leituras reais. A equipe de faturamento agora espera quarenta e oito horas.

### 11.4 Documentando os fluxos

Kofi produz um documento de fluxos de dados na rede com cada salto, responsável, protocolo, criptografia, armazenamento temporário e latência típica. O documento é revisado pela equipe de redes e pelo líder de governança de dados. Ele passa a ser a referência quando a Tidewater negocia um acordo de nível de serviço com o fornecedor de medição. A Profa. Varga observa que um responsável pela governança não pode prestar contas por dados que não consegue ver, e que documentar os fluxos através das fronteiras organizacionais é o que torna a responsabilização possível na prática. O acordo com o fornecedor agora inclui um atraso máximo para leituras armazenadas depois de uma falha.

### Exemplo resolvido

Kofi rastreia os caminhos de medidores e sensores, encontra um protocolo industrial sem autenticação, mede atrasos ligados a tempestades e documenta cada salto com responsáveis e latências.

> **Caso sintético.** As redes são sintéticas.

### Erros e limites

Documentos de fluxo envelhecem depressa; revise-os depois de mudanças na rede.

### Exercícios

- **EX031 — Troca de responsável.** Por que ninguém conseguia responder a perguntas de ponta a ponta? *Rubrica:* 3 = o responsável pela governança muda a cada fronteira;; 2 = menciona fronteiras;; 1 = vago;; 0 = nenhuma.
- **EX032 — Lacuna industrial.** Que lacuna Kofi encontrou na rede industrial? *Rubrica:* 3 = protocolo sem autenticação;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX033 — Dados atrasados.** Quando os atrasos se concentram? *Rubrica:* 3 = em períodos de tempestade;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) relacionar os controles do sistema operacional à proteção de dados; (2) gerenciar com confiabilidade as rotinas agendadas de dados; (3) manter úteis os registros de auditoria.

### 12.1 Arquivos e permissões

O processamento de dados da Tidewater roda em servidores Linux. Kofi revisa as permissões de arquivo dos diretórios que guardam extratos de clientes e descobre que um deles pode ser lido por qualquer usuário do servidor. Ele explica que as permissões do sistema operacional são a última linha de defesa quando os controles da aplicação falham. Ele restringe a leitura do diretório à conta de processamento e ao grupo da equipe de dados e documenta as permissões esperadas, para que verificações posteriores comparem a configuração real com a pretendida. Um script semanal faz essa comparação.

### 12.2 Rotinas agendadas

Rotinas noturnas carregam as leituras dos medidores, aplicam as regras de qualidade e publicam relatórios. Kofi descobre que, se uma rotina falha, a seguinte roda mesmo assim sobre dados incompletos e publica resultados enganosos. Ele altera o agendamento para que cada rotina verifique se a anterior terminou com sucesso e produziu a contagem de linhas esperada. Rotinas que não podem rodar enviam um alerta. Ele observa que as dependências entre rotinas são, na prática, linhagem de dados, e que torná-las explícitas impede a propagação silenciosa de falhas. O alerta vai para o engenheiro de dados de plantão.

### 12.3 Registros de auditoria

O sistema operacional registra logins e comandos. Kofi verifica se os registros dos servidores de dados são enviados a um repositório central, onde os administradores não podem alterá-los, e se são mantidos por um ano. Ele encontra um servidor cujos registros ficavam apenas na máquina e eram sobrescritos depois de uma semana. Sem registros, a Tidewater não conseguiria mostrar, durante uma investigação, quem acessou um extrato de clientes. Ele inclui o servidor no registro centralizado e cria uma verificação semanal de que todos os servidores de dados estão enviando registros. A verificação avisa por e-mail quais servidores estão faltando.

### 12.4 Atualizações e mudanças

Kofi participa do ciclo mensal de atualizações de segurança. Antes de atualizar os servidores de dados, a equipe roda uma rotina de teste em um servidor de homologação para confirmar que as novas bibliotecas não alteram os resultados. Em um ciclo, uma biblioteca de datas atualizada muda a forma de interpretar carimbos de data e hora ambíguos. O teste detecta a diferença antes da produção. Ele aprende que a manutenção dos sistemas pode alterar o processamento de dados em silêncio, por isso a governança precisa de testes de regressão para os resultados dos dados, e não só para as funcionalidades das aplicações. O script de comparação é mantido e passa a rodar em todo ciclo de atualização.

### Exemplo resolvido

Kofi restringe um diretório de extratos legível por todos, encadeia as rotinas ao sucesso das anteriores, centraliza os registros de um servidor e detecta em homologação uma mudança na interpretação de datas antes da atualização.

> **Caso sintético.** Os servidores são sintéticos.

### Erros e limites

As permissões se desviam depois de correções emergenciais; verifique-as com regularidade.

### Exercícios

- **EX034 — Correção de permissão.** O que Kofi mudou no diretório de extratos? *Rubrica:* 3 = leitura só pela conta de processamento e pela equipe de dados;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX035 — Encadeamento de rotinas.** Como as rotinas agora se protegem de entradas ruins? *Rubrica:* 3 = cada uma verifica se a anterior teve sucesso com as contagens esperadas;; 2 = menciona a anterior;; 1 = vago;; 0 = nenhuma.
- **EX036 — Achado da homologação.** O que o teste em homologação detectou? *Rubrica:* 3 = uma mudança na interpretação de carimbos de data e hora;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) projetar esquemas que codifiquem regras de governança; (2) usar restrições e dados de referência; (3) gerenciar dados mestres de clientes e imóveis.

### 13.1 Esquemas como regras

Kofi projeta um esquema relacional para clientes, imóveis, medidores e leituras. As chaves primárias tornam cada entidade única, e as chaves estrangeiras garantem que uma leitura se refira a um medidor real e um medidor a um imóvel real. Restrições de não nulidade impõem os campos obrigatórios. Ele explica que colocar as regras no esquema faz com que o próprio banco de dados recuse dados inválidos, em vez de depender de cada aplicação para verificá-los. O esquema se torna uma declaração precisa e aplicável de parte do padrão de dados da Tidewater. As inserções rejeitadas são registradas com os motivos.

### 13.2 Dados de referência

Códigos de tarifa, tipos de medidor e códigos de distrito são dados de referência: listas pequenas e controladas, usadas por vários sistemas. Kofi encontra três versões da lista de distritos em sistemas diferentes, com um distrito renomeado em apenas duas delas. Ele propõe uma única tabela de referência, sob responsabilidade da equipe de planejamento da rede, com cada mudança datada e aprovada. O DAMA-DMBOK2 trata os dados de referência e os dados mestres como uma área de gestão própria, porque as inconsistências em listas compartilhadas se propagam para todos os relatórios que as usam. Os outros sistemas agora copiam a tabela todas as noites.

### 13.3 Dados mestres

Os registros de clientes e imóveis são dados mestres, compartilhados pelo faturamento, pelo atendimento e pelas operações de campo. Kofi encontra imóveis duplicados, criados quando a equipe de campo cadastra novas ligações sem pesquisar antes. Ele projeta uma etapa de correspondência que compara endereços normalizados e coordenadas antes de criar um imóvel novo, e um papel de curador nas operações de atendimento, responsável por resolver as possíveis duplicatas. Ele observa que a qualidade dos dados mestres depende tanto do processo e da titularidade quanto do projeto do banco de dados. O curador esvazia toda semana a fila de possíveis duplicatas.

### 13.4 Histórico e mudanças

Clientes se mudam, tarifas mudam e medidores são trocados. Kofi projeta tabelas que guardam o histórico com datas de início e fim de vigência, para que contas antigas possam ser explicadas com os fatos que valiam na época. Sem histórico, um cliente que questionasse uma conta antiga veria a tarifa de hoje e ficaria confuso. Ele testa o projeto com exemplos sintéticos, inclusive um medidor trocado no meio do mês, e confirma que os cálculos de faturamento batem com os fatos de cada período. A equipe de atendimento confirma que a visão de histórico responde a dúvidas que antes ela encaminhava ao faturamento.

### Exemplo resolvido

Kofi codifica chaves e restrições em um esquema, consolida três listas de distritos em dados de referência com responsável, acrescenta a correspondência de imóveis duplicados com um curador e guarda o histórico datado.

> **Caso sintético.** Os esquemas são sintéticos; o DAMA-DMBOK2 é real.

### Erros e limites

Restrições podem bloquear correções urgentes; defina um processo controlado de exceção.

### Exercícios

- **EX037 — Finalidade da chave estrangeira.** O que as chaves estrangeiras garantem aqui? *Rubrica:* 3 = leituras se referem a medidores reais, e medidores a imóveis reais;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX038 — Listas de distritos.** Quantas versões da lista de distritos existiam? *Rubrica:* 3 = três;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX039 — Finalidade do histórico.** Por que guardar datas de início e fim de vigência? *Rubrica:* 3 = para explicar contas antigas com os fatos da época;; 2 = menciona o passado;; 1 = vago;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) aplicar práticas de requisitos e testes a *pipelines* de dados; (2) gerenciar as versões da lógica de dados; (3) projetar pensando na manutenibilidade.

### 14.1 Requisitos para pipelines

Kofi escreve os requisitos do *pipeline* de dados de medidores como afirmações testáveis: toda leitura aceita tem medidor e unidade válidos; as leituras rejeitadas são relatadas com os motivos em até uma hora; os totais diários de cada distrito batem com a soma das leituras. Cada requisito tem um responsável e um teste de aceitação. Ele explica que requisitos vagos, como os dados devem ser exatos, não podem ser testados e, portanto, não se pode demonstrar que foram cumpridos nem rastrear sua falha. Os responsáveis aprovam cada teste de aceitação.

### 14.2 Testando pipelines

Kofi monta três camadas de testes. Os testes unitários verificam regras individuais. Os testes de integração passam um pequeno conjunto de dados sintéticos por todo o *pipeline* e comparam os resultados com os esperados. Os testes de dados rodam sobre os resultados de produção e verificam propriedades como contagens de linhas dentro das faixas esperadas e ausência de consumo negativo. Os testes de dados detectam um problema que os unitários não poderiam pegar: um arquivo do fornecedor chega com uma nova ordem de colunas, e as leituras caem nos campos errados até que o leitor seja atualizado. Agora uma verificação dos nomes das colunas roda primeiro.

### 14.3 Gestão de versões

As mudanças na lógica do *pipeline* seguem um processo de liberação: revisão de código, testes, uma execução em homologação sobre a réplica sintética do mês anterior e uma comparação dos resultados. Diferenças acima das tolerâncias acordadas precisam ser explicadas antes da liberação. Kofi argumenta que as versões do *pipeline* merecem o mesmo cuidado que o software voltado aos clientes, porque uma pequena mudança em uma regra pode alterar milhares de contas. Cada nota de versão aponta para o registro de decisão que justificou a mudança da regra. No último trimestre, duas versões foram retidas porque diferenças não explicadas excederam as tolerâncias.

### 14.4 Manutenibilidade

Kofi documenta o *pipeline* com um diagrama, um catálogo de regras e um guia de operação. Ele remove código sem uso e substitui limiares fixos no código por valores de configuração que os donos dos dados podem revisar. A Profa. Varga explica que a manutenibilidade é uma preocupação de governança: quando a pessoa que construiu um *pipeline* vai embora, a organização ainda precisa conseguir explicá-lo e alterá-lo. *Pipelines* sem manutenção viram caixas-pretas cujos resultados ninguém consegue justificar. Uma nova integrante da equipe usa o guia de operação para reexecutar uma carga com falha em sua primeira semana, sem ajuda.

### Exemplo resolvido

Kofi escreve requisitos testáveis para o *pipeline*, monta testes unitários, de integração e de dados que detectam uma mudança na ordem das colunas, acrescenta comparações nas liberações e documenta o *pipeline* para facilitar a manutenção.

> **Caso sintético.** O *pipeline* é sintético.

### Erros e limites

Tolerâncias largas demais escondem mudanças reais; revise-as com os responsáveis.

### Exercícios

- **EX040 — Requisito testável.** Dê um requisito testável do *pipeline*. *Rubrica:* 3 = leituras aceitas têm medidor e unidade válidos; rejeitos relatados em uma hora; totais conciliam;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX041 — Achado dos testes de dados.** O que os testes de dados detectaram? *Rubrica:* 3 = um arquivo do fornecedor com nova ordem de colunas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX042 — Valores fixos.** O que substituiu os limiares fixos no código? *Rubrica:* 3 = valores de configuração revisados pelos donos;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) aplicar confidencialidade, integridade e disponibilidade aos dados de uma companhia de saneamento; (2) escolher controles de acesso para conjuntos de dados; (3) relacionar incidentes de segurança à governança de dados.

### 15.1 Três propriedades

Kofi aplica as propriedades clássicas de segurança aos dados da Tidewater. A confidencialidade protege os dados dos clientes e o cadastro de atendimento prioritário. A integridade protege as leituras dos medidores e os valores dos sensores contra alterações não autorizadas, o que importa para o faturamento e para a segurança das pessoas. A disponibilidade garante que os operadores vejam os dados dos sensores durante incidentes. Conjuntos de dados diferentes exigem ênfases diferentes: os dados do sistema de controle precisam primeiro de disponibilidade e integridade, enquanto os dados de clientes precisam de confidencialidade. A governança atribui essas prioridades para que os engenheiros saibam quais concessões são aceitáveis. As prioridades ficam registradas no catálogo de cada conjunto de dados, para que os engenheiros as vejam ao construir sistemas.

### 15.2 Acesso por papel

Kofi projeta um controle de acesso baseado em papéis para os conjuntos de dados. Os analistas de faturamento veem leituras e tarifas, mas não o cadastro prioritário. A equipe de campo vê os dados de imóvel e medidor das ordens de serviço atribuídas a ela. Os cientistas de dados trabalham com extratos pseudonimizados, com os identificadores de clientes substituídos. Cada papel é aprovado pelo dono dos dados. Ele descobre que os analistas compartilham uma única conta no *data warehouse*, o que impede a responsabilização, e a substitui por contas nominais ligadas a papéis. Cada dono revisa os acessos a cada trimestre, e papéis sem uso são removidos.

### 15.3 Incidentes e dados

Quando o notebook de um prestador de serviço com um extrato de clientes é furtado, Kofi ajuda a analisar o incidente. O extrato continha nomes e endereços de um distrito e não estava criptografado. Como se tratava de dados pessoais, o encarregado de proteção de dados avalia a notificação prevista no artigo 33 do GDPR (no Brasil, a comunicação equivalente à autoridade nacional e aos titulares está no art. 48 da LGPD). Kofi rastreia por que o extrato existia: um pedido avulso aprovado informalmente. Ele recomenda que os extratos sigam um processo de solicitação com aprovação do dono, campos mínimos, criptografia e data de expiração. Os clientes do distrito recebem uma carta explicando o que aconteceu.

### 15.4 Segurança e governança juntas

Kofi observa que os controles de segurança protegem os dados, enquanto a governança decide que dados devem existir, quem é dono deles e para quais finalidades. O extrato furtado teria sido inofensivo se a governança tivesse recusado campos desnecessários ou exigido pseudonimização. A Profa. Varga explica que as duas disciplinas compartilham ferramentas como controle de acesso e registros, mas respondem a perguntas diferentes, e que organizações eficazes as conectam por meio de titularidade e políticas compartilhadas. Na Tidewater, o gerente de segurança e o líder de governança de dados agora se reúnem todo mês e mantêm um único registro de riscos de dados.

### Exemplo resolvido

Kofi atribui prioridades de segurança por conjunto de dados, projeta um acesso por papéis com contas nominais no *data warehouse*, analisa um extrato furtado e recomenda um processo governado de extratos.

> **Caso sintético.** O incidente é sintético; o artigo 33 do GDPR e o art. 48 da LGPD são reais.

### Erros e limites

Dados pseudonimizados continuam sendo dados pessoais; proteja-os de acordo.

### Exercícios

- **EX043 — Prioridade dos dados de controle.** Quais propriedades vêm primeiro para os dados do sistema de controle? *Rubrica:* 3 = disponibilidade e integridade;; 2 = ambas;; 1 = uma;; 0 = nenhuma.
- **EX044 — Conta compartilhada.** Que problema do *data warehouse* Kofi corrigiu? *Rubrica:* 3 = conta compartilhada de analistas substituída por contas nominais;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX045 — Regras para extratos.** Cite duas regras para extratos futuros. *Rubrica:* 3 = aprovação do dono, campos mínimos, criptografia, expiração;; 2 = duas;; 1 = uma;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) enxergar a governança de dados como parte de um sistema de sistemas; (2) gerenciar interfaces e requisitos entre equipes; (3) aplicar o pensamento de ciclo de vida aos dados.

### 16.1 Um sistema de sistemas

O ambiente de dados da Tidewater inclui medidores, o *head-end* do fornecedor, o faturamento, o atendimento ao cliente, o sistema de controle, o *data warehouse* e os relatórios regulatórios. Cada um pertence a uma equipe ou empresa diferente. Kofi usa a engenharia de sistemas para enxergá-los como um único sistema cujo comportamento emerge das interações. Um problema de qualidade costuma aparecer longe de sua causa, como quando um defeito de firmware em medidores surge na forma de uma reclamação de conta. O pensamento sistêmico o ajuda a rastrear efeitos através das fronteiras, em vez de corrigir sintomas localmente. Kofi rastreia assim três reclamações recentes.

### 16.2 Controle de interfaces

Kofi escreve documentos de controle de interface para as principais trocas de dados: o arquivo de leituras de medidores enviado pelo fornecedor e o fluxo diário de volumes vindo do sistema de controle. Cada documento define campos, unidades, formatos, horários, tratamento de erros e a quem recorrer. Quando o fornecedor muda um campo, o documento exige aviso prévio e testes. Ele explica que os documentos de interface transformam suposições informais em requisitos acordados, que são a base para cobrar dos parceiros quando os dados não chegam como esperado. Os dois parceiros assinam formalmente os documentos.

### 16.3 Ciclo de vida dos dados

Kofi mapeia o ciclo de vida dos dados de medição: criação no medidor, transmissão, validação, uso no faturamento, análise, arquivamento e eliminação. Em cada etapa, anota o responsável, as regras de qualidade, os controles de segurança e o prazo de retenção. A ISO/IEC 38505-1 incentiva os órgãos de governança a considerar o valor, o risco e as restrições dos dados ao longo de todo o ciclo de vida. Kofi descobre que a eliminação é a etapa menos definida; ninguém havia decidido quando as leituras horárias deveriam ser eliminadas ou agregadas depois do fim dos prazos de evidência de faturamento. O conselho é chamado a tomar essa decisão.

### 16.4 Rastreabilidade de requisitos

Kofi monta uma matriz de rastreabilidade que liga os requisitos de governança, como faturamento exato e limites de retenção, aos requisitos de sistema, aos testes e às evidências. Cada obrigação regulatória remete a pelo menos um controle e um teste. Aparecem lacunas onde as obrigações não têm teste, como a eliminação dos dados horários depois de sete anos. Ele acrescenta requisitos e testes para cobri-las. A Profa. Varga observa que a rastreabilidade permite aos engenheiros responder às perguntas dos auditores com evidências, e não com promessas. A matriz é atualizada sempre que muda uma norma ou um sistema e é revisada a cada trimestre.

### Exemplo resolvido

Kofi trata os dados da Tidewater como um sistema de sistemas, escreve documentos de controle de interface, mapeia o ciclo de vida dos dados e constata que a eliminação não está definida, e monta uma matriz de rastreabilidade.

> **Caso sintético.** Os sistemas são sintéticos; a ISO/IEC 38505-1:2017 é real.

### Erros e limites

Documentos de interface falham se os parceiros não estiverem obrigados a cumpri-los; cite-os nos contratos.

### Exercícios

- **EX046 — Sintoma distante.** Como um defeito de firmware em medidores pode aparecer? *Rubrica:* 3 = como uma reclamação de conta;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX047 — Campos da interface.** O que define um documento de controle de interface? *Rubrica:* 3 = campos, unidades, formatos, horários, tratamento de erros, contatos;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX048 — Etapa mais fraca.** Qual etapa do ciclo de vida estava menos definida? *Rubrica:* 3 = a eliminação;; 2 = correto;; 1 = outra;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) aplicar conceitos de realimentação aos processos de qualidade de dados; (2) projetar malhas de medição e correção; (3) evitar malhas instáveis ou lentas.

### 17.1 Malhas de realimentação

Um sistema de controle mede uma saída, compara-a com uma meta e age para reduzir a diferença. Kofi enxerga a gestão da qualidade de dados da mesma forma: medir as taxas de rejeição, compará-las com metas e corrigir as causas. A Tidewater já mede os rejeitos, mas não tem uma etapa confiável de ação, então a malha está aberta. Ele propõe uma revisão semanal em que os donos dos dados recebem seus números de rejeição e precisam registrar uma ação corretiva para qualquer número acima da meta, fechando a malha. A revisão leva trinta minutos às segundas-feiras.

### 17.2 Atraso e estabilidade

Malhas de realimentação com atrasos longos podem oscilar. Kofi percebe que a Tidewater muda os limiares de validação dos medidores depois das reclamações de cada mês, mas as reclamações chegam semanas depois das contas, de modo que os limiares vão e voltam. Ele recomenda basear as mudanças nos dados semanais de rejeição, que chegam depressa, e limitar as alterações de limiar a pequenos passos. Ele explica que os mesmos princípios que estabilizam bombas e válvulas também estabilizam os processos organizacionais que reagem a medições de qualidade de dados. Agora, mudanças de limiar exigem uma justificativa escrita e uma verificação uma semana depois.

### 17.3 Causas-raiz

Uma boa malha corrige causas, não sintomas. Quando as leituras de um distrito falham repetidamente na validação, a equipe as libera manualmente toda semana. Kofi rastreia as falhas até um lote de medidores com um defeito de firmware e pede ao fornecedor que o corrija. As liberações manuais cessam. Ele observa que corrigir registros individuais para sempre é como um controlador que compensa um sensor quebrado sem que ninguém o conserte, e que a análise de causa-raiz deve fazer parte de toda malha de qualidade. O fornecedor entrega a correção de firmware em um mês.

### 17.4 Medindo a malha

Kofi mede a própria malha: o tempo entre um número ultrapassar a meta e o registro de uma ação, e o tempo entre a ação e a melhora. No início, as ações levam três semanas para ser registradas. Depois da nomeação de responsáveis, levam uma semana. Ele apresenta o desempenho da malha ao grupo de governança de dados como evidência de que o processo funciona. A Profa. Varga observa que os processos de governança, assim como os sistemas de controle, devem ser medidos pela qualidade de sua resposta, e não apenas pelo fato de existirem. A melhora vem, em média, cerca de duas semanas depois.

### Exemplo resolvido

Kofi fecha uma malha de qualidade aberta com ações semanais dos donos, estabiliza limiares oscilantes com dados mais rápidos e passos pequenos, corrige uma causa de firmware e mede o tempo de resposta da malha.

> **Caso sintético.** Os processos são sintéticos.

### Erros e limites

Metas demais sobrecarregam os donos; mantenha as malhas focadas.

### Exercícios

- **EX049 — Malha aberta.** Por que a malha de qualidade da Tidewater estava aberta? *Rubrica:* 3 = não havia uma etapa confiável de ação corretiva;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX050 — Correção da oscilação.** Como Kofi impediu que os limiares oscilassem? *Rubrica:* 3 = dados semanais de rejeição e passos pequenos;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX051 — Velocidade da malha.** Com que rapidez as ações passaram a ser registradas depois da nomeação de responsáveis? *Rubrica:* 3 = uma semana em vez de três;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) projetar proteção em camadas para plataformas de dados; (2) separar ambientes; (3) posicionar os controles de governança na arquitetura.

### 18.1 Camadas

Kofi projeta uma arquitetura de segurança para a plataforma de dados da Tidewater em camadas: segmentação de rede separando o sistema de controle dos sistemas corporativos, gestão de identidades e acessos, criptografia em repouso e em trânsito, registros e monitoramento, e controles no nível dos dados, como o mascaramento dos identificadores de clientes. Ele explica que as camadas fazem com que a falha de um controle não exponha tudo. A arquitetura é revisada em conjunto pela equipe de segurança e pelo líder de governança de dados, já que cada camada afeta as duas áreas. Cada camada tem um responsável nomeado e um calendário de testes.

### 18.2 Ambientes

Os ambientes de desenvolvimento, teste e produção são separados. Kofi descobre que os desenvolvedores vinham copiando dados reais de clientes da produção para os ambientes de teste a fim de reproduzir defeitos. Ele propõe um gerador de dados sintéticos que produza clientes, imóveis e leituras realistas, com as mesmas propriedades estatísticas, além de uma regra rígida: dados pessoais de produção nunca entram em teste. A NIST SP 800-188 discute dados sintéticos e abordagens de desidentificação, e ele a usa para julgar quais propriedades o gerador deve preservar. O próprio gerador é testado para garantir que nenhum registro real possa ser reproduzido a partir de sua saída.

### 18.3 Controles de governança na arquitetura

Kofi posiciona os controles de governança em pontos específicos: regras de qualidade na ingestão, etiquetas de classificação em cada conjunto de dados do catálogo, políticas de acesso aplicadas pelo *data warehouse* com base nessas etiquetas e rotinas de retenção que leem as etiquetas para decidir a eliminação. Ele argumenta que controles atrelados a metadados escalam melhor do que controles escritos em cada aplicação. Quando um novo conjunto de dados é etiquetado como contendo dados pessoais, as proteções se aplicam automaticamente, em vez de depender de alguém se lembrar. As mudanças de etiqueta são registradas e revisadas pelo dono.

### 18.4 Revisão

A revisão de arquitetura levanta preocupações sobre o desempenho do mascaramento em consultas grandes e sobre quem mantém as etiquetas de classificação. Kofi roda um teste mostrando que o mascaramento acrescenta um atraso aceitável e propõe que os donos dos dados aprovem as etiquetas ao registrar os conjuntos de dados. A Profa. Varga observa que a arquitetura é um conjunto de decisões com concessões, e que registrar as alternativas rejeitadas, como criptografar cada coluna individualmente, ajuda os futuros engenheiros a entender o projeto escolhido. O registro de decisão lista essa alternativa, seu custo e o motivo pelo qual a banca de revisão não a escolheu.

### Exemplo resolvido

Kofi projeta a segurança em camadas da plataforma de dados, substitui dados de produção por dados sintéticos nos testes, atrela acesso e retenção a etiquetas de classificação e registra as concessões discutidas na revisão.

> **Caso sintético.** A arquitetura é sintética; a NIST SP 800-188 é real.

### Erros e limites

As etiquetas só valem o que vale sua manutenção; audite-as.

### Exercícios

- **EX052 — Regra para dados de teste.** Que regra Kofi propôs para os ambientes de teste? *Rubrica:* 3 = dados pessoais de produção nunca entram em teste;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX053 — Controles por etiqueta.** Por que atrelar os controles a etiquetas de metadados? *Rubrica:* 3 = as proteções se aplicam automaticamente e escalam;; 2 = menciona automático;; 1 = vago;; 0 = nenhuma.
- **EX054 — Responsável pelas etiquetas.** Quem aprova as etiquetas de classificação? *Rubrica:* 3 = os donos dos dados, no registro;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) gerenciar identidades de pessoas e de dispositivos; (2) usar *hashes* para pseudonimização; (3) governar chaves criptográficas.

### 19.1 Pessoas e dispositivos

A Tidewater gerencia identidades de funcionários, prestadores de serviço e 90.000 medidores. Cada medidor tem uma identidade criptográfica usada para autenticar suas leituras. Kofi aprende que as identidades de dispositivos precisam ser governadas como as contas de funcionários: emitidas, registradas, renovadas e revogadas quando um medidor é retirado. Ele encontra 230 medidores retirados de serviço cujas identidades continuavam válidas na plataforma *head-end*. Um medidor furtado poderia, portanto, continuar enviando leituras que seriam aceitas, e por isso ele recomenda vincular a revogação à ordem de serviço de retirada do medidor. A etapa de revogação agora é automática.

### 19.2 Pseudonimização com hashes com chave

Para as análises, os cientistas de dados precisam ligar as leituras de um cliente ao longo do tempo sem ver nomes nem números de conta. Kofi substitui os números de conta por *hashes* com chave, usando o módulo hmac do Python e uma chave secreta guardada pela equipe de dados. A mesma conta sempre produz o mesmo pseudônimo, o que permite a ligação, enquanto a chave impede que outras pessoas o recalculem. Ele observa que o resultado é pseudonimizado, não anônimo, e por isso continua sendo dado pessoal segundo o GDPR (e também segundo a LGPD) e precisa de proteção. Apenas duas pessoas nomeadas podem ler a chave.

### 19.3 Gestão de chaves

As chaves protegem os dados dos medidores, a criptografia do *data warehouse* e os pseudônimos. Kofi redige as regras de governança das chaves: cada chave tem um responsável, uma finalidade, um local de armazenamento, um calendário de renovação e um procedimento de recuperação. As chaves dos pseudônimos são renovadas todo ano, e as antigas são guardadas apenas pelo tempo necessário para ligar análises históricas. Ele encontra uma chave de pseudonimização gravada em um arquivo de script e a transfere para o serviço de gestão de chaves, com acesso limitado a duas pessoas. Os procedimentos de recuperação são testados uma vez por ano, restaurando uma chave do backup em um exercício controlado.

### 19.4 Criptografia e confiança

Kofi reflete que a criptografia oferece garantias técnicas fortes, mas transfere a confiança para as chaves e para as pessoas que as gerenciam. Se os detentores das chaves saírem sem passar o bastão, os dados podem se tornar inutilizáveis; se as chaves vazarem, as proteções desaparecem. A Profa. Varga explica que é por isso que a gestão de chaves é um tema de governança, e não apenas técnico, e que as decisões sobre quem pode deter chaves devem ser registradas e revisadas como qualquer outra decisão sobre dados. Os detentores de chaves da Tidewater agora constam do registro de governança de dados e são revistos anualmente.

### Exemplo resolvido

Kofi encontra 230 medidores retirados com identidades válidas, vincula a revogação às ordens de serviço, pseudonimiza contas com *hashes* com chave, redige a governança de chaves e tira uma chave de dentro de um script.

> **Caso sintético.** As identidades e as chaves são sintéticas.

### Erros e limites

*Hashes* com chave resistem a pessoas de fora, mas não a quem detém a chave.

### Exercícios

- **EX055 — Identidades obsoletas.** Quantos medidores retirados ainda tinham identidades válidas? *Rubrica:* 3 = 230;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX056 — Status do pseudônimo.** Pseudônimos gerados por *hash* com chave são anônimos? *Rubrica:* 3 = não, continuam sendo dados pessoais;; 2 = correto;; 1 = sim;; 0 = nenhuma.
- **EX057 — Local da chave.** Onde uma chave estava guardada indevidamente? *Rubrica:* 3 = em um arquivo de script;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Governança de dados: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) definir governança de dados para uma organização de engenharia; (2) mapear direitos de decisão; (3) delimitar o escopo dos capítulos especializados.

### 20.1 O que governança significa aqui

Kofi define a governança de dados na Tidewater como o sistema de direitos de decisão, políticas, papéis e controles que garante que os dados de medidores, sensores, clientes e ativos sejam adequados aos seus usos e tratados de forma lícita. O DAMA-DMBOK2 descreve a governança como autoridade e controle sobre ativos de dados, enquanto a ISO/IEC 38505-1 pede ao órgão de governança que dirija, avalie e monitore o uso dos dados. Ele observa que os dezenove capítulos anteriores forneceram os fundamentos de engenharia dos quais a governança agora depende. Kofi apresenta essa definição à chefe de dados, que a adota no estatuto de governança da Tidewater.

### 20.2 Direitos de decisão

Kofi usa os domínios de Khatri e Brown para mapear os direitos de decisão na Tidewater: princípios de dados, qualidade, metadados, acesso e ciclo de vida. Para cada um, registra quem decide, quem contribui e quem é informado. O mapa mostra que as regras de qualidade dos dados de medidores são decididas por quem escreve o código do *pipeline*, enquanto as decisões de retenção não são tomadas por ninguém. Ele apresenta essas lacunas à chefe de dados, que concorda em designar responsáveis para cada domínio. Cada designação é datada e registrada no estatuto.

### 20.3 Papéis

Kofi propõe papéis: um conselho de governança de dados presidido pelo diretor de operações, donos de dados para cada grande domínio, curadores que mantêm regras e definições no dia a dia e custodiantes em TI que operam os sistemas. Ele escreve uma descrição curta das decisões e deveres de cada papel. Ele insiste que os donos precisam ter autoridade sobre os processos que geram seus dados; caso contrário, passam a responder por problemas que não conseguem resolver, o que gera frustração em vez de melhoria. O conselho aprova as descrições dos papéis.

### 20.4 Escopo do trabalho especializado

Kofi define o escopo dos capítulos restantes: requisitos, modelos, ameaças, métodos, arquitetura, controles, implementação, medição, confiabilidade, segurança, integração, desempenho, operação, validação e manutenibilidade, tudo aplicado à cadeia de dados da Tidewater que vai do medidor ao relatório do conselho. A Profa. Varga aprova o foco no indicador de perdas informado ao regulador, porque ele depende de muitos sistemas e equipes, o que o torna um bom teste de governança através das fronteiras da engenharia. O indicador de perdas combina leituras de medidores, vazões de sensores, cadastros de ativos da rede e estimativas, de modo que cada capítulo especializado a seguir testa uma parte diferente da mesma cadeia, do medidor ao regulador.

### Exemplo resolvido

Kofi define a governança para a Tidewater, mapeia os direitos de decisão e descobre que a qualidade é decidida por quem escreve o código e a retenção por ninguém, propõe os papéis de conselho, dono, curador e custodiante e delimita o trabalho seguinte em torno do indicador de perdas.

> **Caso sintético.** A Tidewater é sintética; DAMA-DMBOK2, ISO/IEC 38505-1:2017 e Khatri e Brown (2010) são reais.

### Erros e limites

Organogramas de papéis não criam autoridade; confirme-a nas descrições de cargo.

### Exercícios

- **EX058 — Direitos sobre retenção.** Quem decidia a retenção antes do mapa? *Rubrica:* 3 = ninguém;; 2 = correto;; 1 = alguém;; 0 = nenhuma.
- **EX059 — Dever do curador.** O que fazem os curadores? *Rubrica:* 3 = mantêm regras e definições no dia a dia;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX060 — Indicador de foco.** Que indicador os capítulos seguintes acompanham? *Rubrica:* 3 = o indicador de perdas informado ao regulador;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-21"></a>

## Capítulo 21 — Governança de dados: requisitos

### Objetivos de aprendizagem

Você vai (1) derivar requisitos de governança da regulação e das necessidades do negócio; (2) escrevê-los como afirmações testáveis; (3) acordar prioridades com os donos.

### 21.1 Fontes dos requisitos

Kofi reúne os requisitos do indicador de perdas a partir de quatro fontes: as orientações do regulador para os relatórios, as metas próprias da Tidewater de redução de perdas, a legislação de proteção de dados aplicável aos dados de clientes usados nos volumes faturados e as necessidades dos engenheiros de rede, que usam as perdas por distrito para planejar reparos. Ele lista cada fonte com a cláusula ou a reunião em que a necessidade foi declarada. Ele explica que requisitos sem fonte registrada são difíceis de defender quando os orçamentos são cortados ou as prioridades mudam. A lista de fontes fica guardada junto com os requisitos.

### 21.2 Afirmações testáveis

Ele reescreve necessidades vagas como afirmações testáveis. As perdas devem ser confiáveis passa a ser: o número mensal de perdas é calculado a partir de volumes que conciliam com totais independentes dentro de um por cento, e cada entrada tem um dono nomeado. Os dados devem ser pontuais passa a ser: o fluxo diário de volumes chega até as 06:00 em pelo menos 95 por cento dos dias. Cada afirmação nomeia uma medida, um limiar e um dono que responde por ela. Essas afirmações depois se tornam os testes dos laboratórios de verificação. Redações vagas são devolvidas a quem as escreveu.

### 21.3 Conflitos

Alguns requisitos entram em conflito. Os engenheiros de rede querem as perdas por rua, o que exigiria volumes faturados por cliente, enquanto o encarregado de proteção de dados quer que os analistas vejam apenas dados agregados. Kofi propõe a agregação por distrito, com no mínimo cinquenta imóveis por área, o que apoia o planejamento de reparos sem expor o consumo individual. O acordo é registrado com seus motivos e aprovado pelos dois donos. Ele observa que conflitos tratados abertamente produzem projetos melhores do que conflitos descobertos depois que os sistemas estão construídos. O encarregado de proteção de dados assina a nota final.

### 21.4 Prioridades

Com vinte e quatro requisitos listados, Kofi pede aos donos que os ordenem pelo impacto no número do regulador e nos clientes. A designação de donos, a conciliação e a pontualidade ficam no topo. Os padrões de documentação ficam mais abaixo. Ele usa a ordenação para planejar os capítulos especializados, atacando primeiro os requisitos de maior impacto. A Profa. Varga lembra que listas de requisitos sem ordem incentivam as equipes a fazer primeiro os itens mais fáceis, o que pode deixar os riscos mais importantes sem tratamento por meses enquanto o esforço vai para outro lado. A lista ordenada é publicada na página de governança da intranet.

### Exemplo resolvido

Kofi reúne os requisitos do indicador de perdas a partir de quatro fontes, reescreve-os como afirmações testáveis, resolve o conflito sobre o nível de rua com a agregação por distrito e ordena vinte e quatro requisitos com os donos.

> **Caso sintético.** Os requisitos são sintéticos.

### Erros e limites

Um limiar sem método de medição não é testável; defina os dois.

### Exercícios

- **EX061 — Requisito de pontualidade.** Que afirmação de pontualidade Kofi escreveu? *Rubrica:* 3 = fluxo até as 06:00 em pelo menos 95% dos dias;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX062 — Conflito da rua.** Como foi resolvido o conflito sobre o nível de rua? *Rubrica:* 3 = agregação por distrito com pelo menos cinquenta imóveis;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX063 — Topo da lista.** Quais requisitos ficaram no topo? *Rubrica:* 3 = designação de donos, conciliação e pontualidade;; 2 = a maioria;; 1 = um;; 0 = nenhuma.

<a id="ch-22"></a>

## Capítulo 22 — Governança de dados: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) modelar fluxos de dados e a linhagem de um indicador; (2) encontrar lacunas de titularidade a partir de um grafo de linhagem; (3) manter os modelos atualizados.

### 22.1 Modelando a cadeia

Kofi modela o indicador de perdas como um grafo dirigido. O número do relatório do conselho depende de um indicador-chave de desempenho, que depende do volume faturado e do volume fornecido. O volume faturado depende das leituras dos medidores e das tarifas; as leituras dependem em parte de leituras manuais feitas em um aplicativo de campo; o volume fornecido depende dos dados brutos de vazão dos sensores. Cada nó é um conjunto de dados ou um cálculo com um dono. O grafo torna explícitas as dependências, que uma descrição escrita do processo tende a embaralhar. Os nós têm nomes.

### Laboratório — Linhagem a montante e lacunas de titularidade do número de perdas


```python
"""Trace upstream lineage of a published figure through a synthetic pipeline graph (stdlib only)."""
edges = {
    "board_report.leakage_pct": ["kpi.leakage"],
    "kpi.leakage": ["billing.volume_billed", "scada.volume_supplied"],
    "billing.volume_billed": ["meters.reading", "customers.tariff"],
    "scada.volume_supplied": ["sensors.flow_raw"],
    "meters.reading": ["field_app.manual_read"],
    "customers.tariff": [], "sensors.flow_raw": [], "field_app.manual_read": [],
}
owners = {"kpi.leakage": "ops analytics", "billing.volume_billed": "billing", "scada.volume_supplied": "network ops",
          "meters.reading": "metering", "customers.tariff": "billing", "sensors.flow_raw": None, "field_app.manual_read": None}
def up(n, seen):
    for p in edges.get(n, []):
        if p not in seen: seen.add(p); up(p, seen)
    return seen
src = up("board_report.leakage_pct", set())
print(f"upstream nodes {len(src)}; sources {sorted(n for n in src if not edges[n])}")
print(f"nodes without an owner: {sorted(n for n in src if owners.get(n) is None)}")
```

Execute com `python3 lab_lineage.py`. Saída verificada:

```text
upstream nodes 7; sources ['customers.tariff', 'field_app.manual_read', 'sensors.flow_raw']
nodes without an owner: ['field_app.manual_read', 'sensors.flow_raw']
```

### 22.2 O que o rastreamento mostra

Ao rodar o laboratório, aparecem sete nós a montante do número do conselho. Três são fontes sem entradas adicionais: as tarifas dos clientes, as leituras manuais do aplicativo de campo e os dados brutos de vazão dos sensores. Dois nós não têm dono: as leituras manuais e as vazões brutas dos sensores. Ambos alimentam o número que o regulador vê. Kofi observa que as entradas mais básicas, mais próximas do mundo físico, são justamente onde falta titularidade, porque ficam entre equipes de engenharia e ninguém as reivindicou. Kofi relata as duas lacunas.

### 22.3 Fechando as lacunas

Kofi propõe donos para as duas lacunas: o gerente de medição para as leituras manuais e o gerente de operação da rede para os dados brutos de vazão. Cada um aceita depois de combinar o que significa ser dono: aprovar regras de qualidade, responder a problemas em prazos acordados e aprovar mudanças. Ele acrescenta os donos ao grafo e roda o rastreamento de novo, que agora não mostra nenhum nó sem dono. A nova execução vira uma verificação mensal, já que novos conjuntos de dados acrescentados à cadeia podem reabrir lacunas. Os dois donos assinam uma breve declaração de titularidade.

### 22.4 Mantendo os modelos atualizados

Modelos de linhagem envelhecem à medida que os sistemas mudam. Kofi propõe que qualquer mudança no *pipeline* de perdas atualize o grafo na mesma versão, o que é garantido por uma lista de verificação da revisão. Ele também compara o grafo com os registros de consultas do *data warehouse* a cada trimestre, para encontrar dependências que existem na prática, mas não no modelo. A Profa. Varga explica que um modelo que se afasta da realidade é pior do que nenhum, porque as pessoas confiam nele e tomam decisões com base em suposições erradas. Aparecem duas dessas dependências, e ambas são acrescentadas prontamente.

### Exemplo resolvido

Kofi modela a cadeia de perdas como um grafo, rastreia sete nós a montante, com três fontes e dois nós sem dono, designa donos e mantém o modelo atualizado com verificações nas versões e comparações com os registros.

> **Caso sintético.** O grafo é sintético; as saídas vêm de lab_lineage.py.

### Erros e limites

A linhagem estática não vê dependências em tempo de execução; compare-a com os registros.

### Exercícios

- **EX064 — Contagem a montante.** Quantos nós a montante há por trás do número do conselho? *Rubrica:* 3 = sete;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX065 — Nós sem dono.** Quais nós não tinham dono? *Rubrica:* 3 = field_app.manual_read e sensors.flow_raw;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX066 — Verificação de desvio.** Como Kofi encontra dependências ausentes do modelo? *Rubrica:* 3 = comparação trimestral com os registros de consultas;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-23"></a>

## Capítulo 23 — Governança de dados: análise de ameaças e falhas

### Objetivos de aprendizagem

Você vai (1) analisar ameaças e modos de falha que afetam dados governados; (2) ordená-los por probabilidade e impacto; (3) associar mitigações a donos.

### 23.1 Modos de falha

Kofi faz uma análise de modos de falha e efeitos (FMEA) na cadeia de perdas. Para cada nó, pergunta como ele pode falhar, que efeito a falha teria sobre o número e como seria detectada. Os modos de falha incluem um sensor de vazão travado, que informa valores constantes; um extrato de faturamento sem um distrito; uma mudança de tarifa aplicada com atraso; e uma leitura manual digitada com erro de casa decimal. Cada modo de falha recebe notas de severidade, ocorrência e detecção acordadas com os donos envolvidos. As notas são registradas.

### 23.2 Ameaças

Ele acrescenta ameaças intencionais, usando a NIST SP 800-30r1 como guia: um usuário interno que altera leituras para esconder um erro de faturamento, um código malicioso na rede de controle que corrompe dados dos sensores e um funcionário do fornecedor que muda o formato de um arquivo sem aviso. Para cada ameaça, identifica a origem, a vulnerabilidade explorada e o impacto sobre o número de perdas. Ele observa que ameaças e falhas acidentais muitas vezes produzem os mesmos sintomas, por isso os controles de detecção devem servir aos dois propósitos, em vez de serem projetados separadamente. Cada ameaça tem um dono.

### 23.3 Ordenação

Kofi ordena a lista combinada. Um sensor de vazão travado fica em primeiro lugar, porque é provável, afeta diretamente o volume fornecido e pode passar semanas sem ser notado. A falta de distritos no faturamento fica em segundo. A ameaça interna tem probabilidade menor, mas impacto alto. Ele mostra a ordenação aos donos, que concordam que a melhoria da detecção nos sensores deve ser o primeiro investimento, já que detectar mais cedo reduz o impacto de todas as falhas a jusante na cadeia. A ordenação é revista depois que os primeiros detectores funcionam por três meses.

### 23.4 Mitigações

Cada item no topo recebe uma mitigação e um dono: um detector de linha reta (*flat-line*) nos sensores de vazão, a cargo da operação da rede; uma verificação de completude por distrito, a cargo do faturamento; e registros à prova de adulteração para edições de leituras, a cargo da medição. Kofi registra o risco residual depois de cada mitigação. A Profa. Varga observa que uma análise ordenada com donos nomeados é o que transforma uma lista de preocupações em um plano de governança, porque diz quem faz o quê primeiro e como alguém saberá se funcionou. Os riscos residuais são relatados a cada trimestre.

### Exemplo resolvido

Kofi analisa modos de falha e ameaças na cadeia de perdas, coloca o sensor de vazão travado em primeiro lugar e atribui detectores, verificações de completude e registros à prova de adulteração aos donos.

> **Caso sintético.** A análise é sintética; a NIST SP 800-30r1 é real.

### Erros e limites

Notas definidas por uma só pessoa são palpites; acorde-as com os donos.

### Exercícios

- **EX067 — Maior risco.** Qual falha ficou em primeiro lugar? *Rubrica:* 3 = um sensor de vazão travado;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX068 — Sintomas comuns.** Por que a detecção deve servir a ameaças e a falhas? *Rubrica:* 3 = muitas vezes produzem os mesmos sintomas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX069 — Mitigação dos sensores.** Que mitigação trata os sensores travados? *Rubrica:* 3 = um detector *flat-line* a cargo da operação da rede;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-24"></a>

## Capítulo 24 — Governança de dados: métodos I

### Objetivos de aprendizagem

Você vai (1) escolher dimensões de qualidade para a cadeia de perdas; (2) selecionar métodos de medição; (3) definir limiares com os donos.

### 24.1 Escolhendo as dimensões

Kofi seleciona dimensões de qualidade do arcabouço de Wang e Strong e da revisão de Batini: completude, validade, acurácia, pontualidade e consistência. Para os sensores de vazão, acurácia e completude são as mais importantes. Para os volumes faturados, a consistência com as leituras dos medidores é a principal. Para o número do conselho, importam a pontualidade e a rastreabilidade. Ele explica que escolher as dimensões por conjunto de dados evita medir tudo em toda parte, o que desperdiça esforço e enterra os sinais importantes entre outros menos relevantes. Kofi registra no catálogo as dimensões escolhidas para cada conjunto de dados, com uma frase explicando por que cada uma importa para quem usa aqueles dados.

### 24.2 Métodos de medição

Para cada dimensão, ele define um método. A completude é a proporção das leituras esperadas que foram recebidas. A validade é a proporção que passa nas regras de formato e de faixa. A acurácia dos sensores é verificada com um medidor de referência portátil durante as visitas de manutenção. A consistência compara os volumes faturados com os totais dos medidores. A pontualidade é o horário de chegada em relação ao prazo acordado. A ISO 8000-8 enfatiza que as afirmações sobre qualidade devem informar como foram medidas, por isso cada método é registrado com sua fórmula. Cada fórmula também é implementada uma única vez na biblioteca compartilhada, para que todas as equipes a calculem da mesma forma.

### 24.3 Limiares

Kofi acorda limiares com os donos: completude de pelo menos 99 por cento por distrito por dia, validade de pelo menos 98 por cento, acurácia dos sensores dentro de dois por cento da referência e chegada até as 06:00 em 95 por cento dos dias. Os limiares se baseiam no desempenho sintético do ano anterior e na tolerância do regulador. Ele registra que os limiares serão revistos depois de seis meses, porque foram definidos com poucos dados e podem se mostrar rígidos ou frouxos demais na prática. A data da revisão é lançada no calendário de governança, para não ser esquecida.

### 24.4 Limitações dos métodos

Cada método tem limites. As verificações com o medidor de referência só acontecem durante a manutenção, então a acurácia é amostrada, não contínua. As regras de validade pegam valores impossíveis, mas não valores plausíveis e errados. Kofi lista as limitações ao lado de cada método e planeja verificações complementares, como comparar sensores vizinhos. A Profa. Varga enfatiza que declarar as limitações protege a organização do excesso de confiança e ajuda os leitores a julgar quanto peso uma nota de qualidade pode ter em uma decisão. As limitações aparecem no painel ao lado de cada nota, para que os leitores as vejam no momento em que interpretam um número.

### Exemplo resolvido

Kofi escolhe dimensões por conjunto de dados, define métodos de medição com fórmulas, acorda limiares com os donos para revisão em seis meses e lista as limitações dos métodos com verificações complementares.

> **Caso sintético.** Os limiares são sintéticos; Wang e Strong (1996), Batini et al. (2009) e ISO 8000-8:2015 são reais.

### Erros e limites

Limiares copiados de outra companhia ignoram as condições locais.

### Exercícios

- **EX070 — Dimensões dos sensores.** Quais dimensões mais importam para os sensores de vazão? *Rubrica:* 3 = acurácia e completude;; 2 = ambas;; 1 = uma;; 0 = nenhuma.
- **EX071 — Método de acurácia.** Como a acurácia dos sensores é verificada? *Rubrica:* 3 = com um medidor de referência portátil durante a manutenção;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX072 — Limite da validade.** O que as regras de validade não pegam? *Rubrica:* 3 = valores plausíveis, mas errados;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) produzir um primeiro projeto para dados de perdas governados; (2) apresentá-lo para crítica; (3) revisá-lo depois do retorno.

### 25.1 O enunciado

O primeiro ateliê de projeto pede a Kofi que produza, em duas semanas, um projeto de governança para a cadeia de perdas: donos, regras, linhagem, monitoramento e relatórios. Ele trabalha com dois colegas que fazem o papel dos donos da operação da rede e do faturamento. O enunciado exige um resumo de uma página, um diagrama de linhagem, um catálogo de regras e um esboço de painel de monitoramento. O formato do ateliê imita a prática profissional, em que os projetos são apresentados a pares e partes interessadas antes de se comprometerem recursos para construí-los. Cada estudante também escreve uma reflexão.

### 25.2 Primeiro projeto

O projeto de Kofi coloca todas as regras em um serviço central de qualidade pelo qual passam todos os conjuntos de dados. O serviço registra os resultados em um único banco de dados e alimenta um único painel. Os donos recebem e-mails diários com seus números. Ele argumenta que a centralização traz consistência e um único lugar para olhar. Os colegas questionam se um único serviço daria conta de dados de sensores chegando a cada minuto ao lado de extratos mensais de faturamento, e se os donos continuariam lendo e-mails diários por muito tempo. Kofi anota as duas perguntas para a banca e admite que ainda não tem respostas.

### 25.3 Crítica

A banca do ateliê, conduzida pela Profa. Varga, elogia o trabalho de linhagem e titularidade, mas critica o serviço central como ponto único de falha. Se ele parar, nenhum dado é verificado. Os avaliadores também observam que os e-mails diários logo seriam ignorados. Um deles sugere rodar as regras perto de cada fonte, com os resultados indo para um repositório comum, e alertar os donos apenas quando os limiares forem ultrapassados, junto com um resumo semanal que mostre as tendências ao longo do tempo. A banca entrega o retorno por escrito em até dois dias depois da sessão.

### 25.4 Revisão

Kofi revisa o projeto: as regras rodam dentro de cada *pipeline* usando uma biblioteca de regras compartilhada, os resultados vão para um repositório comum, os alertas só disparam quando um limiar é ultrapassado e os donos recebem um resumo semanal de tendências. Ele registra o projeto original, a crítica e os motivos das mudanças em um registro de decisão. Ele reflete que a crítica melhorou o projeto porque a banca olhou para as falhas e para o comportamento humano, aspectos que ele havia subestimado ao se concentrar na consistência técnica. A banca aceita o projeto revisado na sessão seguinte.

### Exemplo resolvido

O primeiro projeto de Kofi, centralizado, é criticado como ponto único de falha e por depender de e-mails fáceis de ignorar; ele o revisa para regras distribuídas, um repositório comum de resultados, alertas por violação de limiar e resumos semanais.

> **Caso sintético.** O ateliê é sintético.

### Erros e limites

Defender um projeto em vez de ouvir desperdiça a crítica.

### Exercícios

- **EX073 — Fraqueza central.** Que fraqueza a banca viu no serviço central? *Rubrica:* 3 = ponto único de falha;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX074 — Mudança nos alertas.** Como as notificações aos donos foram alteradas? *Rubrica:* 3 = alertas só em violações, mais um resumo semanal;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX075 — Subestimado.** O que Kofi havia subestimado? *Rubrica:* 3 = as falhas e o comportamento humano;; 2 = ambos;; 1 = um;; 0 = nenhuma.

<a id="ch-26"></a>

## Capítulo 26 — Governança de dados: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar arquiteturas para dados governados; (2) avaliá-las em relação aos requisitos; (3) registrar a escolha.

### 26.1 Três opções

Kofi compara três arquiteturas para os dados governados da Tidewater. Um *data warehouse* central com uma camada de governança reúne todos os dados tratados em um só lugar. Uma *data mesh* dá a cada equipe de domínio a responsabilidade de publicar seus dados como um produto, seguindo padrões acordados. Uma solução híbrida mantém um *data warehouse* central para os relatórios regulatórios, enquanto os domínios são donos dos dados operacionais. Ele descreve os fluxos de dados, o modelo de titularidade e os controles que cada opção exigiria para atender aos requisitos do capítulo 21. Cada opção é desenhada com a mesma notação, para facilitar a comparação.

### 26.2 Avaliação

Ele pontua cada opção em relação aos requisitos ordenados. O *data warehouse* central vai bem em consistência e conciliação, mas mal em titularidade, porque a equipe central se torna dona de fato. A *data mesh* vai bem em titularidade, mas mal na conciliação entre domínios, dado o nível atual de maturidade da Tidewater. A híbrida tem o melhor resultado geral: os números regulatórios continuam conciliados de forma central, enquanto as equipes de domínio são donas de seus dados de origem e os publicam com regras de qualidade e metadados padronizados. Kofi mostra a planilha de pontuação aos donos, para que contestem qualquer nota que considerem injusta.

### 26.3 Custos e competências

Kofi estima custos e competências. A *data mesh* exige que cada equipe de domínio tenha competências de engenharia de dados, que a Tidewater não tem fora da equipe de análise. A híbrida exige treinamento para donos e curadores de domínio, mas não novas equipes de engenharia. Ele inclui um plano de três anos para desenvolver competências, depois do qual mais responsabilidade poderia passar aos domínios. Ele observa que as escolhas de arquitetura precisam caber nas capacidades da organização, e não apenas em suas aspirações, ou fracassam na implementação. O plano nomeia cursos, mentores e pontos de controle em que o progresso será revisto formalmente.

### 26.4 Registrando a escolha

Kofi escreve um registro de decisão de arquitetura escolhendo a híbrida, com as alternativas, as notas, os custos, os riscos e as condições para reabrir a decisão, como as equipes de domínio atingirem níveis de competência acordados. O conselho de governança o aprova. A Profa. Varga observa que registrar as condições para reabrir uma escolha mantém vivas as decisões de arquitetura, porque incentiva a organização a reconsiderá-las quando as circunstâncias mudam, em vez de defender por hábito uma escolha ultrapassada. O registro fica junto com os demais registros de decisão, e a agenda do conselho marca uma revisão depois de dezoito meses para verificar se as condições foram atendidas.

### Exemplo resolvido

Kofi compara as arquiteturas central, *mesh* e híbrida, pontua-as em relação aos requisitos, escolhe a híbrida considerando as competências da Tidewater e registra as condições para reabrir a decisão.

> **Caso sintético.** As opções são sintéticas.

### Erros e limites

Arquiteturas da moda podem não servir; pontue-as em relação aos seus requisitos.

### Exercícios

- **EX076 — Fraqueza da mesh.** Por que a *data mesh* teve nota baixa na Tidewater? *Rubrica:* 3 = conciliação fraca entre domínios na maturidade atual;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX077 — Opção escolhida.** Que arquitetura foi escolhida? *Rubrica:* 3 = a híbrida;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX078 — Condição para reabrir.** Dê uma condição para reabrir a decisão. *Rubrica:* 3 = equipes de domínio atingirem níveis de competência acordados;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-27"></a>

## Capítulo 27 — Governança de dados: projeto de controles

### Objetivos de aprendizagem

Você vai (1) projetar controles preventivos, detectivos e corretivos para dados; (2) definir a titularidade dos controles; (3) definir as evidências dos controles.

### 27.1 Tipos de controle

Kofi projeta controles de três tipos para a cadeia de perdas. Controles preventivos impedem a entrada de dados ruins: restrições de esquema e validação de entrada no aplicativo de campo. Controles detectivos encontram problemas: regras diárias de qualidade, detectores *flat-line* e conciliação. Controles corretivos resolvem problemas: procedimentos documentados para solicitar arquivos novamente, corrigir leituras com aprovação e republicar números. Ele explica que depender só da detecção deixa os donos eternamente limpando dados, enquanto a prevenção reduz o volume de problemas na origem. Cada tipo tem um dono nomeado no catálogo.

### 27.2 Catálogo de controles

Cada controle do catálogo tem identificador, finalidade, tipo, dono, frequência, evidência produzida e requisito vinculado. Por exemplo, o controle DQ-04 verifica diariamente a completude por distrito, pertence ao faturamento, produz uma tabela de resultados e atende ao requisito de completude. O catálogo contém trinta e um controles. Ele os associa aos riscos do capítulo 23 e descobre que dois riscos médios não têm controle, então projeta controles adicionais para eles antes do início da implementação. O catálogo fica no repositório, sob controle de versão, de modo que toda mudança em um controle é rastreável.

### 27.3 Evidências

Para cada controle, Kofi define que evidência mostra que ele funcionou: resultados de regras armazenados com data e hora, registros de alertas, registros de aprovação de correções. Ele explica que os auditores vão perguntar não só se os controles existem, mas se rodaram e se os problemas tiveram acompanhamento. Evidências geradas automaticamente e guardadas de forma centralizada são mais confiáveis do que evidências montadas à mão antes das auditorias, que tendem a ser incompletas e chegam tarde demais para revelar problemas. Kofi configura cada controle para gravar suas evidências em um repositório compartilhado, com retenção de sete anos.

### 27.4 Teste dos controles

Kofi planeja os testes dos controles. A cada trimestre, um curador testa uma amostra de controles introduzindo erros sintéticos em um ambiente de teste e confirmando que os controles os detectam e que os alertas chegam aos donos. Controles que falham no teste são corrigidos e testados de novo. A Profa. Varga observa que controles não testados oferecem conforto, e não garantia, e que injetar erros de propósito é uma das poucas formas de confirmar que os controles detectivos funcionam antes que uma falha real dependa deles. Os resultados dos testes são relatados ao conselho de governança a cada trimestre.

### Exemplo resolvido

Kofi projeta controles preventivos, detectivos e corretivos, monta um catálogo de trinta e um controles, cobre duas lacunas, define evidências automáticas e planeja testes trimestrais com injeção de erros.

> **Caso sintético.** Os controles são sintéticos.

### Erros e limites

Controles sem evidência não podem ser demonstrados.

### Exercícios

- **EX079 — Exemplo corretivo.** Dê um controle corretivo. *Rubrica:* 3 = nova solicitação de arquivos, correções aprovadas ou republicação de números;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX080 — Tamanho do catálogo.** Quantos controles há no catálogo? *Rubrica:* 3 = trinta e um;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX081 — Método de teste.** Como os controles são testados a cada trimestre? *Rubrica:* 3 = injetando erros sintéticos em teste;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-28"></a>

## Capítulo 28 — Governança de dados: implementação I

### Objetivos de aprendizagem

Você vai (1) implementar regras de qualidade de dados em código; (2) medir taxas de aprovação; (3) interpretar resultados combinados.

### 28.1 A biblioteca de regras

Kofi implementa as primeiras regras de qualidade em uma biblioteca compartilhada, usada por todos os *pipelines*. Cada regra é uma função com identificador, descrição, dono e limiar lido da configuração. As três primeiras regras verificam se o identificador do medidor está presente, se a leitura não é menor que a anterior do mesmo medidor e se o consumo diário é inferior a 300 metros cúbicos, quantidade implausível para qualquer cliente residencial ou pequeno comércio da área da Tidewater. Cada regra também está documentada no catálogo.

### Laboratório — Taxas de aprovação de três regras de leitura em 10.000 linhas sintéticas


```python
"""Run validation rules on synthetic meter readings and report pass rates (stdlib only)."""
import random
random.seed(8)
rows = []
for i in range(10000):
    prev = random.uniform(100, 5000); cur = prev + random.uniform(0, 60)
    if random.random() < 0.02: cur = prev - random.uniform(1, 50)        # rollback
    if random.random() < 0.01: cur = prev + random.uniform(500, 2000)    # spike
    mid = f"M{i:06d}" if random.random() > 0.005 else ""
    rows.append((mid, prev, cur))
rules = {
    "meter id present": lambda r: bool(r[0]),
    "reading not below previous": lambda r: r[2] >= r[1],
    "daily use under 300 m3": lambda r: r[2] - r[1] < 300,
}
for name, f in rules.items():
    ok = sum(1 for r in rows if f(r)); print(f"{name:28s} pass {ok/len(rows):.3f}")
allok = sum(1 for r in rows if all(f(r) for f in rules.values()))
print(f"rows passing all rules {allok} of {len(rows)} ({100*allok/len(rows):.1f}%)")
```

Execute com `python3 lab_rules.py`. Saída verificada:

```text
meter id present             pass 0.995
reading not below previous   pass 0.980
daily use under 300 m3       pass 0.990
rows passing all rules 9650 of 10000 (96.5%)
```

### 28.2 Executando as regras

O laboratório aplica as regras a 10.000 leituras sintéticas. A regra do identificador do medidor aprova 99,5 por cento das linhas; a regra de não ser menor que a anterior, 98,0 por cento; e a regra do consumo diário, 99,0 por cento. As linhas aprovadas nas três regras somam 9.650, ou 96,5 por cento. Kofi observa que a taxa combinada é menor que qualquer taxa isolada, porque as falhas caem em linhas diferentes. Os donos veem as taxas de suas próprias regras, mas o número combinado é o que o faturamento de fato recebe. Por isso, Kofi pede que o painel mostre com destaque o número de todas as regras, com as taxas individuais logo abaixo para os donos que precisam investigar suas próprias falhas.

### 28.3 Interpretando as falhas

Kofi examina as falhas. As leituras menores que a anterior vêm principalmente de trocas de medidor, em que o novo medidor começa do zero. Não se trata de erro na leitura, mas da falta de vínculo entre o medidor antigo e o novo. Ele trabalha com a medição para registrar as trocas, de modo que a regra compare apenas leituras do mesmo medidor. Os identificadores ausentes vêm de leituras manuais digitadas sem leitura do código, o que o aplicativo de campo passará a impedir ao exigir a leitura. As duas correções entram na próxima versão.

### 28.4 Em relação aos limiares

Em comparação com os limiares acordados no capítulo 24, a validade de 96,5 por cento fica abaixo da meta de 98 por cento. Kofi relata isso com honestidade ao conselho de governança, com as causas encontradas e as correções planejadas, e estima que só a correção das trocas já elevaria a taxa combinada acima da meta. A Profa. Varga observa que relatar uma meta não atingida com um plano crível gera mais confiança do que baixar os limiares para que os números pareçam aceitáveis. O conselho aceita o plano e pede uma atualização depois da próxima versão, com as taxas recalculadas sobre dados novos.

### Exemplo resolvido

Kofi implementa uma biblioteca de regras compartilhada, aplica três regras a 10.000 linhas, com taxas de aprovação de 99,5, 98,0 e 99,0 por cento e 96,5 por cento aprovadas em todas, rastreia as causas e relata o não atingimento da meta.

> **Caso sintético.** Os dados são sintéticos; as saídas vêm de lab_rules.py.

### Erros e limites

A média das taxas por regra superestima a qualidade; informe a taxa de todas as regras.

### Exercícios

- **EX082 — Taxa de todas as regras.** Que proporção das linhas passou em todas as regras? *Rubrica:* 3 = 96,5% (9.650 de 10.000);; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX083 — Causa das leituras menores.** O que causou principalmente as leituras menores que a anterior? *Rubrica:* 3 = trocas de medidor começando do zero;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX084 — Tratamento da meta.** Como Kofi lidou com a meta não atingida? *Rubrica:* 3 = relatou com honestidade, com causas e correções;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-29"></a>

## Capítulo 29 — Governança de dados: medição

### Objetivos de aprendizagem

Você vai (1) medir a pontualidade em relação a um nível de serviço; (2) encontrar padrões nas violações; (3) relatar o desempenho do serviço.

### 29.1 O nível de serviço

O fluxo diário de volume fornecido precisa chegar ao *data warehouse* até as 06:00, para que a visão matinal de perdas esteja pronta para os engenheiros de rede. Kofi mede os horários de chegada ao longo de noventa dias sintéticos. Ele registra o horário em que cada fluxo chega e o compara com o prazo. Ele explica que um nível de serviço só é útil se for medido continuamente e relatado tanto ao fornecedor quanto ao consumidor, para que cada lado saiba se o acordo está sendo cumprido. Aqui, o fornecedor é a operação da rede, que roda a rotina de exportação todas as manhãs.

### Laboratório — Chegadas do fluxo em relação ao nível de serviço das 06:00 em 90 dias sintéticos


```python
"""Measure daily feed timeliness against a 06:00 service level over 90 synthetic days (stdlib only)."""
import random
random.seed(19)
arr = [random.gauss(5.2, 0.6) + (1.5 if 40 <= d < 47 else 0) for d in range(90)]   # hours after midnight
late = [d for d, a in enumerate(arr) if a > 6.0]
print(f"days {len(arr)}; feed after 06:00 on {len(late)} days ({100*len(late)/len(arr):.1f}%)")
print(f"late days in the week 40-46: {sum(1 for d in late if 40 <= d < 47)} of 7")
```

Execute com `python3 lab_sla.py`. Saída verificada:

```text
days 90; feed after 06:00 on 11 days (12.2%)
late days in the week 40-46: 7 of 7
```

### 29.2 Resultados

O laboratório mostra que o fluxo chegou depois das 06:00 em 11 de 90 dias, ou 12,2 por cento. A meta do nível de serviço é de 95 por cento no horário, o que admite cerca de quatro ou cinco dias de atraso; a Tidewater alcançou 87,8 por cento. Os sete dias da semana entre o dia 40 e o dia 46 tiveram atraso. Os outros quatro dias de atraso ficaram espalhados. Kofi observa que um único número-resumo esconde esse padrão, que aponta para um evento específico, e não para uma lentidão geral. Kofi plota os horários diários de chegada para que o agrupamento fique visível de relance para qualquer leitor.

### 29.3 Encontrando a causa

Kofi investiga a semana de atrasos com a operação da rede. Naquela semana, uma atualização do sistema de controle acrescentou uma rotina de backup que rodava antes da exportação, atrasando o fluxo em cerca de uma hora e meia todos os dias. Ninguém ligou a atualização ao atraso do fluxo, porque a equipe do *data warehouse* não foi avisada da mudança. Ele recomenda que mudanças que afetem o horário da exportação sejam comunicadas ao dono dos dados e que a rotina de backup da atualização seja movida. A rotina de backup é reagendada para depois da exportação.

### 29.4 Relatando o serviço

Kofi projeta um relatório mensal de serviço com o percentual no horário, um gráfico das chegadas diárias com o prazo marcado, os agrupamentos de violações e as causas encontradas. O relatório vai para o dono na operação da rede e para os consumidores dos dados. A Profa. Varga observa que mostrar o gráfico diário, e não apenas o percentual, permite que os leitores vejam os padrões por conta própria, e que os relatórios de serviço devem explicar as violações, e não apenas contá-las, já que a contagem sozinha não dá base para melhorar. O primeiro relatório é discutido na reunião mensal de operações.

### Exemplo resolvido

Kofi mede 11 dias de atraso em 90 (12,2 por cento), com todos os sete dias da semana 40 a 46 atrasados, rastreia a causa até a rotina de backup de uma atualização e projeta um relatório mensal de serviço com gráfico diário.

> **Caso sintético.** As chegadas são sintéticas; as saídas vêm de lab_sla.py.

### Erros e limites

Médias escondem agrupamentos; plote os valores diários.

### Exercícios

- **EX085 — Proporção de atrasos.** Em que proporção dos dias o fluxo atrasou? *Rubrica:* 3 = 12,2% (11 de 90);; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX086 — Causa do agrupamento.** O que causou a semana de atrasos? *Rubrica:* 3 = a rotina de backup de uma atualização rodando antes da exportação;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX087 — Dias espalhados.** Quantos dias de atraso ficaram fora daquela semana? *Rubrica:* 3 = quatro;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) verificar se os controles implementados atendem aos requisitos; (2) usar a injeção de erros sintéticos; (3) relatar os resultados da verificação.

### 30.1 Plano de verificação

O primeiro laboratório de verificação confere se os controles implementados até agora atendem aos requisitos do capítulo 21. Kofi escreve um plano que lista cada requisito, o controle que deveria atendê-lo, o método de teste e o critério de aprovação. Por exemplo, o requisito de completude é verificado retirando um distrito de um extrato sintético de faturamento e confirmando que o controle DQ-04 dispara um alerta em até uma hora. A Profa. Varga revisa o plano antes do início dos testes. Cada teste tem um critério de aprovação acordado de antemão.

### 30.2 Injeção de erros

Kofi prepara um conjunto de dados sintéticos com erros conhecidos: distritos ausentes, leituras menores que as anteriores, vazões negativas, um sensor travado e um arquivo com colunas trocadas. Ele roda o *pipeline* e registra quais controles detectam quais erros. Dos doze erros injetados, dez são detectados. O sensor travado escapa porque o detector *flat-line* precisa de seis horas de valores constantes, e a injeção durou quatro. As colunas trocadas passam porque ambas contêm números plausíveis. Kofi registra as duas falhas no diário de testes, e ambas são investigadas.

### 30.3 Respondendo às falhas

Sobre o sensor travado, Kofi discute com a operação da rede se quatro horas de vazão constante são suspeitas. Eles concluem que, para adutoras de grande porte, são, e reduzem a janela desses sensores para três horas. Para as colunas trocadas, ele acrescenta uma verificação que compara a distribuição de cada coluna com seu histórico, o que sinalizaria valores invertidos. Ele roda a injeção de novo, e os doze erros são detectados. Cada mudança é registrada no catálogo de controles com seu motivo. Os dois donos aprovam as duas mudanças por escrito, com data.

### 30.4 Relatório de verificação

O relatório lista os requisitos, os controles, os testes, os resultados antes e depois das mudanças e as limitações restantes. Kofi observa que a verificação mostra que os controles funcionam com erros conhecidos, e não que pegam todos os problemas possíveis. A Profa. Varga explica que a verificação responde se construímos os controles do jeito certo, enquanto a validação, mais adiante no curso, pergunta se construímos os controles certos para as pessoas que dependem do número de perdas. O relatório é arquivado com o catálogo de controles e se torna a linha de base com a qual o segundo laboratório de verificação vai comparar seus próprios resultados.

### Exemplo resolvido

Kofi injeta doze erros, detecta dez, encurta a janela *flat-line* das adutoras grandes, acrescenta verificações de distribuição para colunas trocadas, roda de novo com os doze erros detectados e relata as limitações.

> **Caso sintético.** O laboratório é sintético.

### Erros e limites

Passar em testes com erros injetados não prova completude; declare os limites.

### Exercícios

- **EX088 — Contagem de detecções.** Quantos erros injetados foram detectados no início? *Rubrica:* 3 = dez de doze;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX089 — Correção das colunas trocadas.** Que verificação pega colunas trocadas? *Rubrica:* 3 = comparar a distribuição de cada coluna com o histórico;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX090 — Verificação versus validação.** A que pergunta a verificação responde? *Rubrica:* 3 = se os controles foram construídos do jeito certo;; 2 = correto;; 1 = vago;; 0 = nenhuma.
<a id="ch-31"></a>

## Capítulo 31 — Governança de dados: implementação II

### Objetivos de aprendizagem

Você vai (1) implementar metadados e entradas de catálogo para dados governados; (2) automatizar a titularidade e a classificação; (3) tornar a governança visível para os usuários.

### 31.1 O catálogo

Kofi implanta um catálogo de dados para a cadeia de perdas. Cada conjunto de dados ganha uma entrada com sua descrição, dono, curador, classificação, regras de qualidade, vínculos de linhagem, agenda de atualização e prazo de retenção. Ele preenche as entradas dos sete nós a montante e do número do conselho e, depois, acrescenta os sistemas de origem. Quem procura o volume fornecido agora encontra uma única entrada oficial, em vez de várias tabelas parecidas com diferenças pouco claras. Ele explica que o catálogo transforma decisões de governança em informação que as pessoas encontram justamente quando estão procurando dados.

### 31.2 Automatizando os metadados

Entradas de catálogo mantidas à mão ficam desatualizadas. Kofi automatiza o que é possível: detalhes de esquema, horários de atualização e resultados de qualidade são puxados toda noite do *data warehouse* e da biblioteca de regras. Donos e descrições continuam manuais, mas são verificados quanto à defasagem; entradas sem revisão há um ano são sinalizadas aos curadores. Ele observa que a automação mantém corretos os fatos técnicos, enquanto a revisão humana mantém correto o significado, e que os dois exigem processos de manutenção diferentes, porque mudam por motivos diferentes e em ritmos diferentes. Os curadores tratam as entradas sinalizadas todo mês.

### 31.3 A classificação na prática

Cada conjunto de dados é classificado como público, interno, confidencial ou restrito. Os volumes de faturamento de clientes são confidenciais; o cadastro de serviços prioritários é restrito. Kofi vincula as classificações às políticas de acesso do *data warehouse*, de modo que mudar uma classificação muda quem pode ler os dados sem pedidos separados. Quando um analista cria uma tabela derivada que cruza dados confidenciais de faturamento, a classificação é herdada automaticamente. Ele testa a herança com tabelas sintéticas para confirmar que dados derivados nunca recebem classificação inferior à de suas entradas. Os pedidos de acesso caem, porque as permissões acompanham a classificação.

### 31.4 Governança visível

Kofi acrescenta selos de qualidade às entradas do catálogo, mostrando a taxa de aprovação mais recente em todas as regras e o desempenho em relação ao nível de serviço. Os usuários conseguem ver se um conjunto de dados está confiável no momento, antes de usá-lo. Os engenheiros de rede passam a consultar os selos antes de planejar reparos e a questionar os donos sobre notas ruins. A Profa. Varga observa que a visibilidade cria uma pressão saudável, porque os donos preferem corrigir os problemas a deixar que colegas vejam notas ruins persistentes, e os usuários ganham a informação de que precisam para julgar a adequação. Os selos apontam para a descrição das regras por trás de cada nota.

### Exemplo resolvido

Kofi monta as entradas de catálogo da cadeia de perdas, automatiza os metadados técnicos com verificação de entradas defasadas, vincula a classificação ao acesso com herança e acrescenta selos de qualidade que os engenheiros consultam.

> **Caso sintético.** O catálogo é sintético.

### Erros e limites

Selos podem enganar quando as regras são fracas; vincule-os à descrição das regras.

### Exercícios

- **EX091 — Campos automatizados.** Quais metadados são puxados automaticamente? *Rubrica:* 3 = detalhes de esquema, horários de atualização e resultados de qualidade;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX092 — Regra de herança.** Que classificação recebe uma tabela derivada? *Rubrica:* 3 = nunca inferior à de suas entradas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX093 — Efeito dos selos.** Como os selos mudaram o comportamento dos engenheiros? *Rubrica:* 3 = eles consultam os selos e questionam os donos sobre notas ruins;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-32"></a>

## Capítulo 32 — Governança de dados: confiabilidade

### Objetivos de aprendizagem

Você vai (1) conciliar dados entre sistemas; (2) quantificar as lacunas de conciliação; (3) atribuir e acompanhar as quebras de conciliação.

### 32.1 Por que conciliar

O número de perdas subtrai o volume faturado do volume fornecido. Se o faturamento perde leituras de medidores, o volume faturado cai e as perdas parecem maiores do que realmente são. Kofi concilia as leituras de campo dos medidores com as leituras registradas no faturamento, para medir com que confiabilidade os dados passam de um sistema ao outro. A conciliação é um dos controles de dados mais antigos, usado na contabilidade muito antes dos computadores, e continua eficaz porque compara registros independentes dos mesmos fatos, em vez de confiar em qualquer um deles. Kofi a executa todo mês.

### Laboratório — Conciliando 8.000 leituras de campo com os registros de faturamento

```python
"""Reconcile monthly meter reads between field app and billing system (stdlib only)."""
import random
random.seed(27)
field = {f"M{i:05d}": round(random.uniform(10, 40), 1) for i in range(8000)}
billing = dict(field)
for k in random.sample(list(field), 120): del billing[k]                    # lost in transfer
for k in random.sample(list(billing), 60): billing[k] = round(billing[k] * 10, 1)  # unit error
missing = [k for k in field if k not in billing]
mismatch = [k for k in billing if abs(billing[k] - field[k]) > 0.05]
print(f"field reads {len(field)}; missing in billing {len(missing)}; value mismatches {len(mismatch)}")
print(f"reconciled share {100*(len(field)-len(missing)-len(mismatch))/len(field):.2f}%")
```

Execute com `python3 lab_reconcile.py`. Saída verificada:

```text
field reads 8000; missing in billing 120; value mismatches 60
reconciled share 97.75%
```

### 32.2 Resultados da conciliação

O laboratório compara oito mil leituras de campo sintéticas com o faturamento. Cento e vinte leituras simplesmente não existem no faturamento, e sessenta aparecem com valor diferente. A parcela conciliada, isto é, leituras presentes e com valores coincidentes, é de 97,75 por cento. Kofi explica que os dois tipos de quebra têm causas e donos diferentes: leituras ausentes costumam vir de falhas de transferência, enquanto divergências de valor costumam vir de correções manuais feitas no faturamento que não foram aplicadas de volta ao repositório de dados dos medidores. Cada tipo de quebra é contado separadamente.

### 32.3 Efeito sobre as perdas

Kofi estima o efeito das leituras ausentes sobre o número de perdas. Como cada leitura ausente reduz o volume faturado, as perdas ficam superestimadas. Ele calcula o volume associado às leituras ausentes nos dados sintéticos e mostra que ele eleva visivelmente as perdas nos dois distritos com mais quebras. Isso explica por que esses distritos pareciam perder mais água do que distritos vizinhos com tubulações semelhantes, e evita que equipes de reparo sejam enviadas aos lugares errados. Os números corrigidos são compartilhados com os planejadores.

### 32.4 Acompanhando as quebras

Cada quebra vira um registro com dono, causa e situação. As falhas de transferência vão para a equipe de integração; as divergências, para o faturamento. Kofi define a meta de resolver as quebras em dez dias úteis e informa o envelhecimento toda semana. Quebras mais antigas que a meta são escaladas ao comitê de governança. A Profa. Varga explica que conciliação sem acompanhamento das quebras mede os problemas sem corrigi-los, e que os relatórios de envelhecimento mostram se as equipes estão dando conta ou ficando para trás. O primeiro relatório de envelhecimento mostra que a maioria das quebras é fechada dentro da meta.

### Exemplo resolvido

Kofi concilia 8.000 leituras de campo, encontra 120 ausentes no faturamento e 60 divergências, com 97,75 por cento conciliados, relaciona as quebras às perdas superestimadas e acompanha as quebras por dono e por idade.

> **Caso sintético.** As leituras são sintéticas; as saídas vêm de lab_reconcile.py.

### Erros e limites

Conciliar um sistema consigo mesmo não prova nada; use registros independentes.

### Exercícios

- **EX094 — Parcela conciliada.** Que parcela das leituras foi conciliada? *Rubrica:* 3 = 97,75%;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX095 — Efeito das leituras ausentes.** Como as leituras ausentes afetam as perdas? *Rubrica:* 3 = elas as superestimam;; 2 = correto;; 1 = subestimam;; 0 = nenhuma.
- **EX096 — Dono das divergências.** Quem é dono das divergências de valor? *Rubrica:* 3 = o faturamento;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-33"></a>

## Capítulo 33 — Governança de dados: segurança e resiliência

### Objetivos de aprendizagem

Você vai (1) relacionar a governança de dados à segurança física; (2) projetar um suprimento de dados resiliente para a operação; (3) planejar modos degradados.

### 33.1 Dados e segurança

Alguns dados da Tidewater afetam a segurança física. As leituras de pressão e vazão orientam decisões de manobra de válvulas; as leituras de cloro protegem a saúde pública. Kofi distingue esses dados relevantes para a segurança dos dados de negócio. Mudanças em suas regras de qualidade, fontes ou processamento exigem a revisão do engenheiro de segurança operacional, além da do dono dos dados. Ele explica que um processo de governança desenhado para dados de faturamento, em que os erros podem ser corrigidos depois, não basta para dados cujos erros podem levar a ações inseguras. Kofi lista esses conjuntos de dados explicitamente.

### 33.2 Suprimento resiliente

Os operadores precisam dos dados dos sensores durante incidentes, justamente quando redes e sistemas estão sob estresse. Kofi revisa a resiliência do suprimento de dados dos sensores: caminhos de comunicação redundantes para os locais críticos, painéis locais nas estações de tratamento e um segundo servidor de histórico em outro prédio. Ele descobre que o painel de perdas depende de um único servidor do *data warehouse*, o que é aceitável para o planejamento, mas não para a resposta a incidentes. Ele recomenda que a resposta a incidentes nunca dependa da plataforma analítica para leituras críticas. Os operadores aprovam a recomendação por escrito.

### 33.3 Modos degradados

Kofi escreve procedimentos para modos degradados: o que os operadores fazem quando os dados dos sensores estão ausentes, atrasados ou sob suspeita de erro. Os procedimentos incluem usar leituras manuais feitas pela equipe local, comparar com sensores vizinhos e marcar no registro de operação as decisões tomadas com dados degradados. Ele testa os procedimentos em um exercício de mesa com os operadores, que apontam que as leituras manuais precisam de formulários e unidades padronizados para serem utilizáveis, o que ele acrescenta ao procedimento. Um segundo exercício, com os formulários revisados, transcorre sem problemas, e os operadores guardam cópias na sala de controle.

### 33.4 Aprendendo com incidentes

Depois de cada incidente operacional, Kofi propõe uma revisão de dados que pergunta se os dados contribuíram, se os controles de qualidade detectaram os problemas e se os procedimentos de modo degradado funcionaram. As constatações retroalimentam controles e procedimentos. A Profa. Varga relaciona isso à prática da engenharia de segurança, em que aprender com incidentes sem buscar culpados é essencial, e observa que a governança de dados em contextos de segurança deve tomar emprestadas essas práticas, em vez de depender só de verificações de conformidade. A primeira revisão desse tipo, depois do rompimento de uma adutora, constata que um alarme de pressão foi ignorado porque já havia disparado falsamente muitas vezes.

### Exemplo resolvido

Kofi separa os dados relevantes para a segurança, com revisão adicional, avalia a resiliência do suprimento dos sensores, escreve e testa procedimentos de modo degradado e acrescenta revisões de dados após incidentes.

> **Caso sintético.** Os cenários são sintéticos.

### Erros e limites

Tratar dados de segurança como dados de negócio subestima o dano.

### Exercícios

- **EX097 — Revisor adicional.** Quem mais revisa mudanças em dados relevantes para a segurança? *Rubrica:* 3 = o engenheiro de segurança operacional;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX098 — Dependência do painel.** Por que a resposta a incidentes não deve depender do painel de perdas? *Rubrica:* 3 = ele depende de um único servidor do *data warehouse*;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX099 — Constatação do exercício de mesa.** O que os operadores apontaram? *Rubrica:* 3 = as leituras manuais precisam de formulários e unidades padronizados;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-34"></a>

## Capítulo 34 — Governança de dados: integração

### Objetivos de aprendizagem

Você vai (1) integrar os controles de governança entre equipes e sistemas; (2) gerenciar mudanças nas interfaces; (3) testar de ponta a ponta.

### 34.1 Juntando as peças

A esta altura Kofi já tem donos, regras, linhagem, entradas de catálogo, conciliação e relatórios de serviço, construídos em sistemas diferentes por equipes diferentes. Integrar significa garantir que funcionem juntos: as falhas de regras aparecem nos selos do catálogo, a linhagem aponta para os donos, as quebras de conciliação chegam às filas certas e os relatórios de serviço incluem as causas vindas das revisões de incidentes. Ele constrói um mapa de integração que mostra cada conexão entre os componentes de governança e o sistema que implementa cada uma. O mapa mostra quais conexões são automáticas e quais dependem de alguém se lembrar de um passo manual, e esses passos manuais viram candidatos à automação.

### 34.2 Mudanças nas interfaces

Kofi introduz um processo de aviso de mudança para as interfaces da cadeia de perdas. Qualquer equipe que altere um campo, uma agenda ou um formato deve avisar os donos afetados com duas semanas de antecedência, junto com um arquivo de teste. Quando o fornecedor dos medidores planeja uma atualização de *firmware* que muda a precisão dos carimbos de tempo, o aviso permite que o faturamento ajuste seu analisador antes de a mudança entrar em produção. Antes, mudanças assim só eram descobertas depois das falhas, quando leituras já tinham sido perdidas ou atribuídas errado. O fornecedor aceita o processo e indica um contato para os avisos.

### 34.3 Testes de ponta a ponta

Kofi projeta um teste de ponta a ponta que empurra um dia sintético de dados, vindo de medidores e sensores simulados, por todos os sistemas até o número de perdas. O teste verifica se os valores esperados aparecem em cada etapa, se os controles disparam diante de erros injetados e se os selos do catálogo são atualizados. A primeira execução revela que os resultados da conciliação chegam à fila de quebras, mas não ao catálogo, de modo que o selo mostra números defasados. Ele corrige a conexão e executa o teste de novo com sucesso. Agora o teste roda automaticamente depois de cada versão.

### 34.4 Titularidade da integração

Kofi observa que os problemas de integração ficam entre as equipes, então por padrão ninguém é dono deles. Ele propõe que o líder de governança de dados seja dono do teste de ponta a ponta e do mapa de integração, e que cada equipe seja dona de seus componentes. A Profa. Varga explica que a titularidade da integração evita a falha comum em que cada componente funciona isoladamente, mas o conjunto falha, e que alguém precisa responder por como as peças funcionam juntas através das fronteiras organizacionais. O comitê de governança confirma a atribuição e acrescenta o resultado do teste de ponta a ponta ao seu painel mensal de saúde da governança.

### Exemplo resolvido

Kofi mapeia as conexões entre os componentes de governança, introduz avisos de mudança que capturam uma alteração nos carimbos de tempo, constrói um teste de ponta a ponta que encontra um selo defasado e atribui a titularidade da integração.

> **Caso sintético.** Os sistemas são sintéticos.

### Erros e limites

Testes de componentes aprovados não significam que o sistema funciona.

### Exercícios

- **EX100 — Prazo do aviso.** Com quanta antecedência as mudanças de interface precisam ser avisadas? *Rubrica:* 3 = duas semanas, com um arquivo de teste;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX101 — Constatação de ponta a ponta.** O que a primeira execução de ponta a ponta revelou? *Rubrica:* 3 = os resultados da conciliação não chegavam ao catálogo;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX102 — Dono da integração.** Quem é dono do teste de ponta a ponta? *Rubrica:* 3 = o líder de governança de dados;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) projetar a governança de uma nova fonte de dados; (2) aplicar as lições do primeiro ateliê; (3) defender o projeto sob questionamento.

### 35.1 A nova fonte

O segundo ateliê de projeto introduz uma nova fonte de dados: registradores acústicos que escutam vazamentos nas tubulações e enviam resumos diários de ruído. A Tidewater planeja instalar dois mil registradores. Kofi precisa projetar a governança dos dados desses registradores, incluindo donos, regras, linhagem até o processo de perdas, questões de privacidade e retenção. O enunciado exige que o projeto reaproveite os componentes existentes sempre que possível e justifique qualquer componente novo, refletindo a lição de que a governança deve escalar sem reconstruir tudo. A instalação está prevista para dois anos.

### 35.2 Reaproveitando componentes

Kofi reaproveita a biblioteca de regras para as verificações de faixa e de completude, o catálogo para os metadados, o processo de aviso de mudança para a interface com o fornecedor e o padrão de conciliação para comparar os alertas dos registradores com os vazamentos confirmados pelas equipes de reparo. Ele acrescenta um único componente novo: um *model card* que descreve como o algoritmo do fornecedor transforma ruído em probabilidade de vazamento, incluindo sua taxa conhecida de falsos positivos. Ele explica que saídas algorítmicas precisam de documentação própria, porque sua qualidade depende de dados de treinamento que os usuários não conseguem ver. O fornecedor informa a taxa.

### 35.3 Questões de privacidade

Registradores instalados em tubulações em frente a residências poderiam captar sons além do ruído da tubulação. Kofi consulta a especificação do fornecedor e confirma que o dispositivo registra apenas resumos de frequência, não áudio. Ele registra isso na avaliação de impacto sobre a proteção de dados e exige que o fornecedor avise qualquer mudança que passe a captar áudio. A banca questiona se os resumos poderiam revelar padrões de atividade doméstica. Ele admite a possibilidade para registradores próximos a uma única residência e propõe agregar os resumos diários antes que os analistas os vejam. A banca aceita a proposta com uma cláusula de revisão.

### 35.4 Defendendo o projeto

A banca testa o projeto de Kofi com cenários: uma atualização de *firmware* aumenta os falsos positivos, os registradores de um distrito param de reportar e um jornalista pergunta se a Tidewater escuta as casas. Ele responde a cada um usando os componentes e registros de seu projeto. A banca nota uma melhora em relação ao primeiro ateliê, sobretudo na antecipação de falhas e das preocupações das pessoas. A Profa. Varga comenta que os melhores projetos mostram seu raciocínio, para que os revisores possam testá-los em vez de simplesmente confiar no projetista. A banca aprova o projeto, pedindo pequenas mudanças de redação.

### Exemplo resolvido

Kofi projeta a governança dos registradores acústicos reaproveitando regras, catálogo, avisos e conciliação, acrescenta um *model card*, trata a privacidade com resumos e agregação e defende o projeto diante de cenários.

> **Caso sintético.** Os registradores são sintéticos.

### Erros e limites

Garantias de fornecedores precisam de verificação; consulte as especificações.

### Exercícios

- **EX103 — Componente novo.** Que componente novo Kofi acrescentou? *Rubrica:* 3 = um *model card* para o algoritmo de vazamentos;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX104 — Verificação de áudio.** Os registradores gravam áudio? *Rubrica:* 3 = não, apenas resumos de frequência;; 2 = correto;; 1 = sim;; 0 = nenhuma.
- **EX105 — Elogio da banca.** Que melhora a banca notou? *Rubrica:* 3 = a antecipação de falhas e das preocupações das pessoas;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-36"></a>

## Capítulo 36 — Governança de dados: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) manter os controles de governança eficientes à medida que os dados crescem; (2) medir o custo dos controles; (3) priorizar os controles pelo valor.

### 36.1 Crescimento

As leituras dos medidores inteligentes passam de diárias a horárias à medida que a Tidewater atualiza os medidores, o que multiplica o volume por vinte e quatro. Os registradores acústicos acrescentam ainda mais. Kofi estima que a biblioteca de regras levaria muito mais tempo por noite no novo volume se fosse executada sem mudanças. Ele explica que os controles de governança são cargas de trabalho com custos, e que projetos que funcionam na escala de hoje podem falhar quando os volumes aumentam, provocando verificações atrasadas ou controles pulados que minam toda a abordagem de governança. Kofi apresenta a estimativa antes de a troca de medidores começar, para que as mudanças fiquem prontas a tempo.

### 36.2 Tornando os controles eficientes

Kofi altera as regras para processar apenas registros novos e alterados, em vez de históricos completos, particiona os dados por distrito para que as verificações rodem em paralelo e leva as verificações simples de faixa para a etapa de ingestão, onde os dados já estão sendo lidos. Ele mede o tempo de execução em um conjunto de dados sintético no novo volume e confirma que as verificações noturnas agora terminam bem antes do prazo da manhã. Ele documenta as escolhas de projeto para que futuros engenheiros entendam por que as verificações estão estruturadas assim. As verificações de faixa na ingestão também rejeitam leituras ruins mais cedo.

### 36.3 Custo dos controles

Kofi registra o custo computacional e o tempo de pessoal de cada controle. Uma comparação detalhada de distribuições em todas as colunas custa muito mais do que suas constatações justificam para tabelas de baixo risco. Ele propõe uma frequência baseada em risco: dados de alto risco verificados continuamente, de risco médio diariamente e de baixo risco semanalmente. O comitê de governança aprova a abordagem. Ele observa que a governança disputa recursos com outros trabalhos, de modo que mostrar o valor em relação ao custo ajuda a manter o apoio dos gestores que precisam financiá-la. O nível de risco de cada conjunto de dados fica registrado no catálogo, para que a agenda decorra automaticamente da classificação.

### 36.4 O valor dos controles

Para priorizar, Kofi lista, para cada controle, os problemas que ele detectou em seis meses e o impacto deles. Alguns controles não encontraram nada, o que pode significar que o risco não existe ou que o controle é fraco. Ele testa os controles silenciosos por injeção antes de aposentar qualquer um, e aposenta dois que duplicam verificações mais fortes. A Profa. Varga enfatiza que controles que nunca disparam devem ser testados, e não presumidos inúteis, já que o silêncio pode refletir sucesso ou falha. Os demais controles silenciosos permanecem, porque a injeção mostrou que cada um ainda detecta os erros para os quais foi projetado.

### Exemplo resolvido

Kofi prepara os controles para os dados horários dos medidores com verificações incrementais, particionadas e antecipadas, registra o custo dos controles, aplica frequência baseada em risco e testa os controles silenciosos antes de aposentar os duplicados.

> **Caso sintético.** Os volumes são sintéticos.

### Erros e limites

Aposentar controles silenciosos sem testá-los pode remover uma proteção necessária.

### Exercícios

- **EX106 — Crescimento do volume.** Por quanto a leitura horária multiplica o volume? *Rubrica:* 3 = vinte e quatro vezes;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX107 — Mudança de eficiência.** Cite uma mudança de eficiência. *Rubrica:* 3 = processamento incremental, partições por distrito ou verificações na ingestão;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX108 — Controles silenciosos.** O que Kofi fez antes de aposentar controles silenciosos? *Rubrica:* 3 = testou-os por injeção;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-37"></a>

## Capítulo 37 — Governança de dados: operação

### Objetivos de aprendizagem

Você vai (1) conduzir a governança como operação diária; (2) tratar incidentes de dados; (3) manter *runbooks* e plantão.

### 37.1 Operação diária

A governança precisa de rotinas. Kofi define um ciclo diário: os controles noturnos rodam, os alertas chegam aos donos até as sete da manhã, os curadores fazem a triagem dos alertas até as nove e a visão matinal das perdas é publicada com os selos de qualidade. Toda semana, os donos revisam as tendências e o envelhecimento das quebras. Todo mês, o comitê de governança revisa os relatórios de serviço e as decisões. Ele documenta o ciclo em um calendário de operação, para que todos saibam quando esperar informações e quando precisam agir sobre elas. O calendário é compartilhado com todos os donos e curadores, e lembretes são enviados automaticamente antes de cada reunião de revisão.

### 37.2 Incidentes de dados

Um incidente de dados é um evento em que a qualidade ou a disponibilidade dos dados cai a ponto de afetar decisões. Kofi define níveis de severidade, desde a falta de dados de um único distrito até um número de perdas errado enviado ao regulador. Cada nível tem tempos de resposta, regras de comunicação e um líder. Quando uma extração do faturamento falha em um dia de envio de relatório, o líder do incidente avisa o contato do regulador de que os números chegarão com um dia de atraso, em vez de enviar números estimados em silêncio. O contato do regulador agradece à Tidewater pelo aviso antecipado.

### 37.3 Runbooks

Para os alertas mais comuns, Kofi escreve *runbooks*: guias passo a passo que explicam como confirmar o problema, as causas prováveis, as correções e quem deve ser informado. O *runbook* de um sensor de vazão travado explica como comparar com os sensores vizinhos, pedir uma visita ao local e marcar os dados afetados. Ele testa os *runbooks* pedindo a um curador que não os escreveu que siga cada um diante de um incidente sintético, e revisa os passos que causam confusão durante o teste. Os *runbooks* ficam guardados junto aos alertas que cobrem, de modo que o link aparece em cada mensagem de alerta.

### 37.4 Plantão

Alertas de dados podem ocorrer de madrugada. Kofi propõe uma escala de plantão entre os engenheiros de dados para os dados críticos, como os fluxos de sensores relevantes para a segurança, com escalonamento claro para os engenheiros de operação. Alertas não críticos esperam até a manhã. Ele revisa o volume de alertas para garantir que o pessoal de plantão não seja acordado por questões que poderiam esperar. A Profa. Varga observa que uma operação sustentável exige atenção à carga de trabalho das pessoas, porque engenheiros de plantão exaustos cometem erros e vão embora. Os limiares que acordam pessoas sem necessidade são ajustados depois de cada revisão mensal dos alertas noturnos e de seus desfechos.

### Exemplo resolvido

Kofi define rotinas de governança diárias, semanais e mensais, estabelece a severidade dos incidentes de dados com comunicação ao regulador, testa os *runbooks* com um curador e desenha uma escala de plantão sustentável.

> **Caso sintético.** A operação é sintética.

### Erros e limites

Enviar estimativas em silêncio destrói a confiança; comunique os atrasos.

### Exercícios

- **EX109 — Horário da triagem.** Até quando os curadores fazem a triagem dos alertas? *Rubrica:* 3 = até as nove da manhã;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX110 — Falha no dia do relatório.** O que o líder do incidente fez quando uma extração falhou no dia do relatório? *Rubrica:* 3 = avisou o regulador de que os números atrasariam um dia;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX111 — Teste dos runbooks.** Como os *runbooks* são testados? *Rubrica:* 3 = um curador que não os escreveu os segue diante de um incidente sintético;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-38"></a>

## Capítulo 38 — Governança de dados: validação

### Objetivos de aprendizagem

Você vai (1) validar a governança com as pessoas que usam os dados; (2) reunir evidências de utilidade; (3) fazer ajustes com base nas constatações.

### 38.1 Perguntas de validação

A verificação mostrou que os controles funcionam como projetados; a validação pergunta se o projeto atende aos usuários. Kofi entrevista engenheiros de rede, analistas de faturamento, a gerente de relatórios regulatórios e duas pessoas da operação. Ele pergunta se confiam mais no número de perdas do que há um ano, se os selos e alertas ajudam no trabalho e o que ainda causa problemas. Ele também verifica se as equipes de reparo encontraram vazamentos nos distritos que o número aprimorado priorizou, o que é uma medida de resultado. As entrevistas seguem um roteiro escrito, para que as respostas possam ser comparadas com justiça.

### 38.2 Constatações

Os usuários relatam mais confiança e citam os selos e a conciliação. Os engenheiros de rede dizem que as perdas por distrito agora batem melhor com a experiência de campo. Porém, os analistas de faturamento acham alguns alertas confusos, porque os nomes das regras são técnicos. A equipe de operação raramente usa o catálogo e prefere ligar para colegas. As equipes de reparo encontraram vazamentos confirmados a uma taxa maior nos distritos priorizados do que antes, embora Kofi observe que outras mudanças, como novas equipes, também podem explicar parte da melhora. Kofi relata essas constatações ao comitê de governança, incluindo as negativas, para que o quadro seja equilibrado e crível.

### 38.3 Ajustes

Kofi reescreve as mensagens de alerta em linguagem simples, com ações sugeridas. Para a equipe de operação, ele leva as informações principais do catálogo para o painel da sala de controle que ela já usa, em vez de esperar que visite o catálogo. Ele planeja uma revisão de acompanhamento em seis meses. Ele observa que a validação às vezes mostra que bons controles ficam sem uso porque não se encaixam no modo como as pessoas trabalham, e que adaptar a forma de entrega pode importar tanto quanto aprimorar os controles. Os analistas de faturamento confirmam que é muito mais fácil agir com base nos alertas reescritos.

### 38.4 Evidências de valor

Kofi reúne as evidências de validação para o comitê de governança: os temas das entrevistas, a comparação das confirmações de vazamento com suas ressalvas e o uso dos selos e do catálogo. A Profa. Varga lembra-o de separar o que os usuários disseram do que foi medido, e de evitar afirmar que a governança causou a melhora na localização de vazamentos sem evidências mais fortes. O comitê aceita as evidências como animadoras e pede um desenho de comparação melhor para o ano seguinte. Kofi concorda em trabalhar com a equipe de análise em uma comparação que leve em conta as mudanças de equipes e os padrões sazonais.

### Exemplo resolvido

Kofi entrevista usuários e verifica as confirmações de vazamento, encontra mais confiança, mas alertas confusos e um catálogo sem uso, reescreve os alertas, leva informações aos painéis da sala de controle e relata as evidências com ressalvas.

> **Caso sintético.** As entrevistas e os resultados são sintéticos.

### Erros e limites

A satisfação dos usuários, sozinha, não demonstra eficácia; combine-a com medidas de resultado.

### Exercícios

- **EX112 — Queixa do faturamento.** O que confundia os analistas de faturamento? *Rubrica:* 3 = os nomes técnicos das regras nos alertas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX113 — Correção para a operação.** Como Kofi alcançou a equipe de operação? *Rubrica:* 3 = com as informações principais do catálogo no painel da sala de controle;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX114 — Cautela causal.** Contra o que a Profa. Varga alertou? *Rubrica:* 3 = afirmar que a governança causou a melhora na localização de vazamentos sem evidências mais fortes;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-39"></a>

## Capítulo 39 — Governança de dados: manutenibilidade

### Objetivos de aprendizagem

Você vai (1) manter a governança sustentável enquanto pessoas e sistemas mudam; (2) gerenciar a transferência de conhecimento; (3) aposentar controles e dados obsoletos.

### 39.1 As pessoas mudam

Donos e curadores mudam de função. Kofi descobre que, quando a curadora do faturamento saiu, ninguém atualizou os dados de referência das tarifas por dois meses. Ele propõe listas de verificação de passagem para os papéis de governança, substitutos para cada dono e curador e uma confirmação anual de que os ocupantes ainda exercem seus papéis. Os registros de titularidade no catálogo são vinculados ao diretório de funcionários, de modo que um desligamento dispara um lembrete ao líder de governança para designar um sucessor. Os substitutos participam das revisões mensais dos donos, e assim já conhecem as questões em aberto quando precisam assumir um papel.

### 39.2 Transferência de conhecimento

Muito do conhecimento de governança está na cabeça das pessoas: por que um limiar foi definido, qual contato do fornecedor de fato resolve os problemas. Kofi incentiva os donos a escrever notas curtas nos registros de decisão e nos *runbooks*. Ele conduz uma sessão em que curadores que saem e que chegam percorrem juntos as quebras em aberto. Ele explica que uma governança manutenível depende de razões registradas, pois, sem elas, as pessoas novas desfazem escolhas sensatas ou preservam escolhas ultrapassadas sem saber por que existem. A sessão é registrada em notas e repetida sempre que um papel de curador muda de mãos.

### 39.3 Aposentando coisas

Conjuntos de dados e controles que não são mais necessários continuam custando esforço e carregando risco. Kofi introduz uma revisão anual das entradas do catálogo, aposentando os conjuntos de dados sem uso recente depois de consultar os donos e aplicar as regras de retenção. Ele encontra extrações antigas com dados de clientes usadas pela última vez há anos e providencia sua eliminação, com registro das aprovações. A aposentadoria de controles segue a abordagem do teste por injeção dos capítulos anteriores. A revisão também encontra três tabelas que ninguém sabe explicar, que são arquivadas e sinalizadas até que se identifique um dono ou que possam ser eliminadas.

### 39.4 Sustentando o esforço

Kofi mede o esforço de governança: as horas gastas por donos e curadores a cada mês. Ele constata que o esforço está concentrado em poucas pessoas, o que traz risco de esgotamento e de pontos únicos de falha. Ele propõe distribuir as tarefas de curadoria e automatizar as verificações repetitivas. A Profa. Varga observa que a governança muitas vezes fracassa não por mau projeto, mas por cansaço, quando os participantes entusiasmados do início se esgotam, e que o esforço sustentável precisa ser planejado tão deliberadamente quanto qualquer controle. O comitê de governança concorda em incluir o tempo de curadoria nos planos de trabalho, para que esse trabalho seja reconhecido, e não feito por cima das outras tarefas.

### Exemplo resolvido

Kofi acrescenta listas de passagem, substitutos e vínculos com o diretório, registra as razões para transferir conhecimento, aposenta extrações antigas com aprovação e distribui o esforço de curadoria para evitar o cansaço.

> **Caso sintético.** Os papéis são sintéticos.

### Erros e limites

Uma governança que depende de poucos entusiastas é frágil; planeje a rotatividade.

### Exercícios

- **EX115 — Saída da curadora.** O que aconteceu quando a curadora do faturamento saiu? *Rubrica:* 3 = os dados de referência das tarifas ficaram dois meses sem atualização;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX116 — Gatilho do desligamento.** O que dispara a designação de um sucessor? *Rubrica:* 3 = os vínculos com o diretório, que lembram o líder de governança;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX117 — Risco do esforço.** Que risco o esforço concentrado criava? *Rubrica:* 3 = esgotamento e pontos únicos de falha;; 2 = ambos;; 1 = um;; 0 = nenhuma.

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem

Você vai (1) reverificar a cadeia governada depois das mudanças; (2) comparar com o primeiro laboratório; (3) relatar as lacunas residuais.

### 40.1 Escopo

O segundo laboratório de verificação repete os testes do primeiro e acrescenta novos para os componentes construídos desde então: herança de classificação no catálogo, encaminhamento das quebras de conciliação, avisos de mudança, modos degradados e regras para os dados dos registradores. Kofi atualiza o plano de verificação com cada requisito, controle, teste e critério de aprovação. Ele inclui também testes para o volume de dados horário, já que mudanças de desempenho poderiam fazer os controles perderem seus prazos e, portanto, falharem mesmo com a lógica correta. Kofi acrescenta ainda um inventário de todas as ferramentas que podem ler ou gravar dados governados, que passa a fazer parte do plano.

### 40.2 Resultados

Todos os doze erros injetados originalmente são detectados, o que confirma que as correções do primeiro laboratório continuam eficazes. Dos testes novos, a maioria passa. Dois falham: uma tabela derivada criada por uma ferramenta pouco usada não herdou a classificação, e um alerta de modo degradado chegou à equipe errada por causa de uma lista de contatos desatualizada. Os testes de desempenho mostram que as verificações terminam antes do prazo no volume horário, com folga para crescer. Kofi observa que as duas falhas envolvem partes do sistema que foram acrescentadas ou alteradas fora do processo principal de versões, o que sugere que falta ali uma etapa de revisão.

### 40.3 Corrigindo as lacunas

Kofi trabalha com a equipe do *data warehouse* para aplicar a herança de classificação à ferramenta pouco usada e substitui a lista de contatos por links para a escala de plantão. Ele executa os dois testes de novo, com sucesso. Ele observa que as duas falhas vieram de componentes fora do caminho principal, que os testes costumam deixar escapar, e recomenda que as verificações futuras incluam um inventário de todas as ferramentas e pontos de contato que tocam dados governados. O inventário é montado durante o laboratório e encontra mais duas ferramentas, um suplemento de relatórios e um utilitário de exportação, que entram no plano de testes e passam nos testes.

### 40.4 Comparação e relatório

O relatório compara o primeiro e o segundo laboratórios: mais requisitos cobertos, mais controles, menos falhas em relação ao número de testes e correções mais rápidas. Ele lista as lacunas residuais, como os testes limitados do algoritmo dos registradores. A Profa. Varga observa que repetir a verificação depois de mudanças é essencial, porque os sistemas se desviam, e que comparar os resultados ao longo do tempo mostra se a governança está amadurecendo ou apenas acumulando papelada. O relatório é apresentado ao comitê de governança com um resumo curto para não especialistas, e o comitê decide que a verificação será repetida todo ano e depois de qualquer mudança importante na cadeia de perdas.

### Exemplo resolvido

Kofi reverifica a cadeia, detecta todos os erros originais, encontra uma lacuna de herança e uma lista de contatos desatualizada, corrige ambas e relata o progresso e as lacunas residuais em relação ao primeiro laboratório.

> **Caso sintético.** O laboratório é sintético.

### Erros e limites

Testar só o caminho principal deixa escapar rotas laterais para os dados governados.

### Exercícios

- **EX118 — Falhas novas.** Quantos testes novos falharam? *Rubrica:* 3 = dois;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX119 — Correção dos contatos.** O que substituiu a lista de contatos desatualizada? *Rubrica:* 3 = links para a escala de plantão;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX120 — Lição das rotas laterais.** De onde vieram as duas falhas? *Rubrica:* 3 = de componentes fora do caminho principal;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-41"></a>

## Capítulo 41 — Governança de dados: otimização de sistemas

### Objetivos de aprendizagem

Você vai (1) otimizar a cadeia governada como um todo; (2) equilibrar qualidade, custo e pontualidade; (3) evitar otimizar uma parte à custa das demais.

### 41.1 Visão da cadeia inteira

Kofi procura melhorias em toda a cadeia de perdas, e não dentro de equipes isoladas. O faturamento havia ajustado sua extração para rodar mais rápido pulando uma etapa de validação, o que empurrou os erros para a conciliação, mais adiante, onde corrigi-los levava muito mais tempo. Ele mostra o dilema com tempos de execução e contagens de quebras. A cadeia inteira funciona melhor quando o faturamento restaura a validação, mesmo que a etapa do faturamento em si fique mais lenta. A otimização local tinha piorado o sistema como um todo, enquanto cada equipe acreditava estar ajudando. O faturamento concorda.

### 41.2 Equilibrando objetivos

Qualidade, custo e pontualidade puxam em direções diferentes. Prazos mais cedo deixam menos tempo para as verificações; mais verificações custam mais computação e tempo de pessoal. Kofi monta uma tabela simples que mostra, para várias opções de agenda, as taxas esperadas de pontualidade, a cobertura das verificações e o custo. Os donos escolhem uma opção que mantém as verificações completas para os dados de alto risco e leva as verificações de baixo risco para mais tarde no dia. Ele explica que tornar os dilemas explícitos permite que os donos escolham conscientemente, em vez de descobri-los quando algo quebra inesperadamente. A opção escolhida é registrada com suas razões.

### 41.3 Gargalos

Kofi identifica o gargalo da cadeia: a aprovação manual das correções de leituras, que espera por um único supervisor. As correções se acumulam antes do fim do mês, atrasando a conciliação e o número de perdas. Ele propõe delegar a aprovação das correções pequenas a curadores treinados, com os supervisores aprovando as grandes e revisando uma amostra das pequenas. A fila anda mais rápido, e a amostragem de auditoria não mostra aumento de correções incorretas. Melhorar o gargalo ajuda a cadeia inteira muito mais do que acelerar etapas que já eram rápidas. Os supervisores concordam.

### 41.4 Medindo a melhora

Kofi mede a cadeia antes e depois das mudanças: o tempo entre a leitura do medidor e o número de perdas, a parcela de números publicados no prazo e o número de reapresentações. Os três melhoram no trimestre seguinte. A Profa. Varga observa que medidas do sistema impedem que as equipes declarem sucesso em medidas locais enquanto o resultado geral fica estagnado, e que a pontualidade e a estabilidade do número de perdas são o que o regulador e os engenheiros de rede de fato vivenciam. Kofi acrescenta as três medidas da cadeia ao painel mensal do comitê de governança, para que qualquer tendência de piora fique visível cedo para todos.

### Exemplo resolvido

Kofi reverte um atalho local do faturamento que prejudicava a cadeia, apresenta dilemas explícitos, alivia o gargalo de aprovação de correções delegando aprovações a curadores e mede a melhora no nível da cadeia.

> **Caso sintético.** Os tempos são sintéticos.

### Erros e limites

Otimizar a medida de uma equipe pode prejudicar o sistema; meça a cadeia.

### Exercícios

- **EX121 — Atalho do faturamento.** O que o atalho do faturamento causou? *Rubrica:* 3 = erros empurrados para a conciliação, mais lenta;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX122 — Gargalo.** Qual era o gargalo? *Rubrica:* 3 = a aprovação manual das correções por um único supervisor;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX123 — Medidas da cadeia.** Cite as três medidas da cadeia. *Rubrica:* 3 = tempo da leitura ao número, parcela no prazo e reapresentações;; 2 = todas;; 1 = algumas;; 0 = nenhuma.

<a id="ch-42"></a>

## Capítulo 42 — Governança de dados: pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa a partir da prática de governança; (2) desenhar um estudo com dados sintéticos; (3) relatar as constatações com seus limites.

### 42.1 A pergunta

A pesquisa aplicada de Kofi pergunta se as quebras de conciliação preveem erros nas estimativas de perdas por distrito. Se previrem, a contagem de quebras poderia servir de alerta antecipado antes da publicação dos números. Ele formula a pergunta com precisão: em dados distritais sintéticos, o número de quebras de conciliação em um mês está associado ao tamanho das correções posteriores do número de perdas daquele distrito? Ele observa que a pergunta é útil para a Tidewater porque permitiria aos curadores concentrar o esforço de verificação onde os erros são prováveis. A Profa. Varga a aprova.

### 42.2 Desenho do estudo

Kofi gera dados sintéticos para quarenta distritos ao longo de vinte e quatro meses, com quebras e correções ligadas por uma relação conhecida mais ruído. Ele ajusta uma relação linear simples usando o módulo statistics do Python e verifica se a inclinação estimada recupera a relação que ele mesmo embutiu. Ele explica que testar métodos em dados sintéticos com respostas conhecidas mostra se a análise consegue encontrar um efeito real antes de aplicá-la a dados reais, nos quais a resposta verdadeira é desconhecida. Ele fixa a semente aleatória para que os resultados se repitam exatamente.

### 42.3 Interpretando os resultados

A análise recupera uma associação positiva próxima do valor embutido, com grande variação entre os distritos. Kofi adverte que recuperar um efeito plantado mostra apenas que o método funciona, não que os distritos reais se comportem assim. Ele esboça um plano para aplicar o método a dados distritais reais anonimizados, com a aprovação da Tidewater, usando a discussão de validade de Shadish, Cook e Campbell para orientar quais explicações alternativas, como o tamanho do distrito, precisam ser verificadas. Ele observa também que a força da associação nos dados reais pode ser muito menor do que no exemplo plantado.

### 42.4 Relatando

Kofi escreve um artigo curto com a pergunta, o desenho sintético, os resultados, os limites e um plano para os dados reais. Ele compartilha o código para que outros possam reproduzir os resultados sintéticos. A Profa. Varga observa que uma declaração clara do que o estudo pode e não pode mostrar é a parte mais valiosa da pesquisa aplicada para os profissionais, que de outro modo leem nos resultados mais do que eles sustentam, sobretudo quando os resultados confirmam o que já queriam acreditar. O artigo é apresentado em um seminário do departamento, onde as perguntas afiam a seção de limites.

### Exemplo resolvido

Kofi pergunta se as quebras de conciliação preveem correções das perdas, testa o método em distritos sintéticos com uma relação plantada, recupera-a, declara os limites e planeja um estudo com dados reais.

> **Caso sintético.** Os dados são sintéticos; Shadish, Cook e Campbell (2002) é real.

### Erros e limites

Recuperar um efeito plantado não prova um efeito real.

### Exercícios

- **EX124 — Pergunta de pesquisa.** O que Kofi perguntou? *Rubrica:* 3 = se as quebras preveem correções posteriores das perdas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX125 — Propósito do sintético.** Por que usar dados sintéticos com respostas conhecidas? *Rubrica:* 3 = para verificar se o método consegue encontrar um efeito real;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX126 — Explicação alternativa.** Cite uma explicação alternativa a verificar. *Rubrica:* 3 = o tamanho do distrito;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-43"></a>

## Capítulo 43 — Prática na indústria ou no serviço público

### Objetivos de aprendizagem

Você vai (1) aplicar a governança em uma empresa de saneamento em funcionamento; (2) adaptar métodos acadêmicos a restrições práticas; (3) refletir sobre a conduta profissional.

### 43.1 O estágio

Kofi passa um período de estágio na equipe de dados da Tidewater. Ele sai dos exercícios do curso para o trabalho diário real, embora todos os exemplos deste livro continuem sintéticos. Ele participa da triagem matinal, escreve *runbooks* e apoia um envio regulatório. Ele percebe que restrições práticas, como tempo limitado, prioridades concorrentes e sistemas legados, moldam o que a governança consegue alcançar. Os métodos do curso continuam úteis, mas precisam de adaptação, por exemplo uma análise de falhas mais leve para mudanças pequenas. Ele mantém um diário semanal do que adapta e por quê.

### 43.2 Trabalhando com os donos

Os donos têm outros trabalhos. Kofi aprende a preparar resumos curtos com perguntas claras, para que os donos possam decidir depressa. Quando o gerente de medição está ocupado demais para revisar as mudanças de regras, Kofi propõe uma revisão mensal em lote, em vez de pedidos avulsos, o que o gerente aceita. Ele reflete que respeitar o tempo dos donos torna mais provável o apoio à governança, enquanto exigir atenção para cada pequena pergunta tende a fazer os donos evitarem o processo. Outros donos pedem o mesmo arranjo mensal, que se torna a abordagem padrão da equipe.

### 43.3 Um envio regulatório

Kofi ajuda a preparar o envio anual sobre perdas. Ele reúne as evidências: linhagem, resultados dos controles, conciliação, relatórios de serviço e constatações da validação. O revisor do regulador pergunta como a Tidewater sabe que os sensores de vazão são precisos. Kofi apresenta as verificações com o medidor de referência e seus limites e cita as melhorias planejadas. O revisor aceita as evidências e registra os limites. Ele vê como o trabalho de governança dos capítulos anteriores se transforma em respostas que terceiros consideram críveis. O revisor também pede que o envio do ano seguinte mostre o progresso nas melhorias que Kofi listou, e a equipe as acrescenta ao seu plano.

### 43.4 Conduta profissional

Durante o estágio, Kofi percebe que um colega está editando uma leitura sem a aprovação exigida, para cumprir um prazo. Ele trata do assunto em particular, explicando o risco, e o colega submete a edição à aprovação. Kofi reflete sobre o dever de manter os controles mesmo sob pressão. A Profa. Varga observa que os conselhos profissionais esperam que os engenheiros ajam com integridade e manifestem suas preocupações, e que pequenos deslizes tolerados sob pressão enfraquecem aos poucos os controles que protegem os clientes e o público. Ele não leva o caso adiante, pois a edição foi corrigida.

### Exemplo resolvido

Kofi adapta os métodos durante o estágio, agrupa as revisões dos donos, apoia um envio regulatório com evidências e limites e trata com profissionalismo uma edição não aprovada.

> **Caso sintético.** O estágio é sintético.

### Erros e limites

Contornar controles sob pressão de prazo os corrói; manifeste suas preocupações.

### Exercícios

- **EX127 — Tempo dos donos.** Como Kofi respeitou o tempo do gerente de medição? *Rubrica:* 3 = com uma revisão mensal em lote das mudanças de regras;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX128 — Pergunta do regulador.** O que o revisor do regulador perguntou? *Rubrica:* 3 = como a Tidewater sabe que os sensores de vazão são precisos;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX129 — Edição não aprovada.** Como Kofi lidou com a edição não aprovada? *Rubrica:* 3 = tratou do assunto em particular e a edição foi submetida à aprovação;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-44"></a>

## Capítulo 44 — Projeto final de engenharia I

### Objetivos de aprendizagem

Você vai (1) definir um projeto final sobre dados governados; (2) planejar escopo, riscos e evidências; (3) acordar os critérios de sucesso.

### 44.1 Escolha do projeto

O projeto final de Kofi consiste em projetar e demonstrar um pacote de governança para o programa de gestão de pressão, que ajusta válvulas para reduzir as perdas. Os dados de pressão afetam a segurança e as perdas, de modo que o projeto combina lições de todo o curso. Ele o escolhe porque o programa está em expansão e seus dados hoje não têm donos, regras nem linhagem. O projeto final precisa produzir uma demonstração funcional com dados sintéticos, documentação e evidências de que os controles funcionam. O diretor de operação apoia a escolha e concorda em ceder um engenheiro como contato, o que torna o projeto relevante para a Tidewater.

### 44.2 Escopo

Kofi limita o escopo aos dados dos sensores de pressão, às configurações das válvulas e ao vínculo entre as mudanças de pressão e as estimativas de perdas em três distritos sintéticos. Ele exclui a lógica de controle das próprias válvulas, que pertence aos engenheiros de operação. Um escopo claro impede que o projeto cresça além do que um único estudante consegue entregar em um semestre. Ele lista as entregas: linhagem, mapa de donos, catálogo de regras, testes dos controles, um esboço de painel e um registro de decisão para cada escolha importante. A declaração de escopo é assinada pela Profa. Varga e pelo engenheiro de operação.

### 44.3 Riscos

Ele identifica os riscos do projeto: dados sintéticos que não reflitam o comportamento real da pressão, acesso limitado aos engenheiros de operação e tempo perdido com problemas de ferramentas. Para cada risco ele planeja uma resposta, como validar cedo os padrões sintéticos com um engenheiro de operação e manter o código simples, usando apenas a biblioteca padrão. Ele revisa os riscos toda semana. A Profa. Varga lembra-o de que a gestão de riscos de projeto é uma competência profissional por si só, separada do conteúdo técnico. O registro de riscos é guardado junto com os arquivos do projeto.

### 44.4 Critérios de sucesso

Kofi acorda os critérios de sucesso com a Profa. Varga e um engenheiro de operação: donos nomeados e aceitos para todos os conjuntos de dados do escopo, regras que cubram os limiares relevantes para a segurança, erros injetados detectados a uma taxa acordada e uma demonstração compreendida por um público da operação. Cada critério tem uma medida. Ele observa que acordar os critérios no início evita disputas posteriores sobre o sucesso do projeto e concentra o esforço no que importa para as pessoas que usarão os resultados. Os critérios são escritos no plano do projeto e não podem ser mudados sem acordo.

### Exemplo resolvido

Kofi escolhe a governança da gestão de pressão, limita o escopo a sensores, configurações de válvulas e três distritos, planeja os riscos com validação antecipada e acorda critérios de sucesso mensuráveis.

> **Caso sintético.** O projeto é sintético.

### Erros e limites

Escopo pouco claro é a falha mais comum em projetos finais; escreva-o.

### Exercícios

- **EX130 — Área excluída.** O que Kofi excluiu do escopo? *Rubrica:* 3 = a lógica de controle das válvulas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX131 — Resposta ao risco sintético.** Como Kofi vai verificar os dados sintéticos de pressão? *Rubrica:* 3 = validando cedo os padrões com um engenheiro de operação;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX132 — Critério de público.** Quem precisa compreender a demonstração? *Rubrica:* 3 = um público da operação;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-45"></a>

## Capítulo 45 — Revisão independente de projeto

### Objetivos de aprendizagem

Você vai (1) preparar um projeto para revisão independente; (2) responder às constatações dos revisores; (3) registrar as decisões após a revisão.

### 45.1 Preparação

Na metade do projeto final, o projeto de Kofi passa por uma revisão independente feita por um engenheiro de outra empresa de saneamento e por um consultor de governança de dados, nenhum deles envolvido no trabalho. Ele prepara um pacote de revisão: enunciado do problema, escopo, projeto, registros de decisão, planos de teste e fragilidades conhecidas. Ele lista as fragilidades abertamente, para que os revisores gastem seu tempo com os problemas desconhecidos. A Profa. Varga explica que a revisão independente é valiosa justamente porque os revisores não têm as premissas do projetista e vão questionar o que ele dá como certo. O pacote é enviado com uma semana de antecedência.

### 45.2 Constatações

Os revisores levantam três constatações. Primeira: as regras tratam todos os sensores de pressão da mesma forma, embora os sensores em pontos críticos precisem de limiares mais rigorosos. Segunda: a linhagem termina na estimativa de perdas e não mostra onde os dados de pressão alimentam a análise de reclamações de clientes. Terceira: o mapa de donos nomeia o gerente de operação para todos os dados de pressão, o que concentra demais em uma única pessoa. Eles também elogiam os registros de decisão, que tornam o raciocínio fácil de acompanhar e de testar. Cada constatação é escrita com uma explicação e as evidências que levaram os revisores a levantá-la.

### 45.3 Respondendo

Kofi responde por escrito a cada constatação: acrescenta categorias de sensores com limiares diferentes, estende a linhagem até a análise de reclamações depois de confirmar a dependência com a equipe de atendimento e divide a titularidade entre o gerente de operação, para os locais críticos, e os gerentes distritais, para os demais. Para cada resposta ele registra a mudança, o raciocínio e a preocupação residual. Ele discute uma constatação da qual discorda em parte, explicando suas razões, e os revisores aceitam um meio-termo. O meio-termo diz respeito ao número de categorias de sensores, que é reduzido de cinco para três.

### 45.4 Depois da revisão

O registro da revisão lista as constatações, as respostas, as mudanças e os itens em aberto. Ele entra no dossiê de evidências do projeto final. Kofi reflete que os revisores encontraram problemas que ele não tinha visto, apesar do trabalho cuidadoso, porque a familiaridade esconde as lacunas. A Profa. Varga observa que acolher a revisão, em vez de se defender dela, é sinal de um engenheiro maduro, e que uma trilha de revisão documentada mostra aos avaliadores como o projeto melhorou, o que convence mais do que um projeto apresentado como se fosse impecável desde o início. Os itens em aberto são agendados para a segunda metade do projeto final.

### Exemplo resolvido

Kofi prepara um pacote de revisão que lista as fragilidades, recebe três constatações sobre limiares, linhagem e titularidade, responde por escrito com mudanças e um meio-termo negociado e registra a revisão.

> **Caso sintético.** A revisão é sintética.

### Erros e limites

Esconder fragilidades conhecidas desperdiça o tempo dos revisores.

### Exercícios

- **EX133 — Constatação sobre limiares.** O que os revisores disseram sobre os limiares? *Rubrica:* 3 = sensores críticos precisam de limiares mais rigorosos;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX134 — Mudança de titularidade.** Como a titularidade foi dividida? *Rubrica:* 3 = gerente de operação para os locais críticos, gerentes distritais para os demais;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX135 — Por que revisar.** Por que os revisores independentes são valiosos? *Rubrica:* 3 = eles não têm as premissas do projetista;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-46"></a>

## Capítulo 46 — Projeto final de engenharia II

### Objetivos de aprendizagem

Você vai (1) construir e testar o pacote de governança do projeto final; (2) demonstrá-lo; (3) avaliá-lo em relação aos critérios de sucesso.

### 46.1 Construção

Kofi constrói o pacote com dados sintéticos: um gerador de dados de pressão com ciclos diários realistas, a biblioteca de regras estendida com as categorias de sensores, a linhagem incluindo a análise de reclamações, as entradas de catálogo e um painel de alertas. Ele usa apenas a biblioteca padrão do Python, como planejado, o que mantém o código legível para os engenheiros de operação. Ele documenta cada componente com seu propósito, dono e teste. A construção segue o processo de versões dos capítulos anteriores, com revisão de código por um colega e testes antes de cada integração. Cada integração é registrada.

### 46.2 Testes

Ele injeta erros nos dados sintéticos: sensores travados, picos súbitos, horas ausentes e uma configuração de válvula alterada sem registro. Os controles detectam a maioria dos erros. As horas ausentes em um distrito são detectadas com atraso, porque a verificação de completude roda diariamente, e não a cada hora. Ele passa a verificação para horária nos locais críticos. Uma nova execução detecta todos os erros injetados dentro dos tempos acordados, e ele registra as duas execuções no registro de testes, com a mudança feita entre elas. A mudança é aprovada pelo engenheiro de operação.

### 46.3 Demonstração

Kofi demonstra o pacote para um público formado por pessoas da operação, um dono e a Profa. Varga. Ele percorre um incidente: um sensor travado em um local crítico, o alerta, o *runbook*, o procedimento de modo degradado e o efeito sobre a estimativa de perdas. As pessoas da operação fazem perguntas práticas sobre o volume de alertas e os alarmes falsos. Ele mostra as estatísticas de alertas do período de testes. O público confirma que entendeu a demonstração e que conseguiria usar o painel. Também sugere acrescentar mapas com a localização dos sensores, que Kofi inclui depois.

### 46.4 Avaliação

Kofi avalia o projeto em relação aos critérios de sucesso. Os donos estão nomeados e aceitos para todos os conjuntos de dados; as regras cobrem os limiares relevantes para a segurança; todos os erros injetados foram detectados depois da mudança para a verificação horária; o público da operação entendeu a demonstração. Ele registra os limites: dados sintéticos não captam todo o comportamento real, e a operação de longo prazo não foi testada. A Profa. Varga aprova a avaliação, elogiando a honestidade sobre os limites ao lado de evidências claras para cada critério. A avaliação é escrita como um relatório curto, em que cada critério é seguido de sua medida, do resultado alcançado e das evidências que o sustentam, para que os examinadores possam verificar cada afirmação.

### Exemplo resolvido

Kofi constrói com a biblioteca padrão um pacote de governança para os dados de pressão, encontra a detecção tardia de horas ausentes e passa a verificações horárias nos locais críticos, demonstra o percurso de um incidente e avalia o projeto pelos critérios.

> **Caso sintético.** O pacote e os dados são sintéticos.

### Erros e limites

Demonstrações que escondem falhas enganam; mostre o registro de testes.

### Exercícios

- **EX136 — Detecção tardia.** O que foi detectado com atraso no início? *Rubrica:* 3 = horas ausentes em um distrito;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX137 — Correção da detecção tardia.** O que a corrigiu? *Rubrica:* 3 = verificações horárias de completude nos locais críticos;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX138 — Limites declarados.** Cite um limite declarado por Kofi. *Rubrica:* 3 = dados sintéticos ou operação de longo prazo não testada;; 2 = um;; 1 = vago;; 0 = nenhuma.

<a id="ch-47"></a>

## Capítulo 47 — Ensaio de falha e recuperação

### Objetivos de aprendizagem

Você vai (1) conduzir um ensaio de falha e recuperação com dados governados; (2) medir a recuperação; (3) aprimorar os procedimentos de recuperação.

### 47.1 O ensaio

Kofi conduz um ensaio em que a plataforma de dados de pressão falha durante um dia simulado de alta demanda. O cenário sintético retira do ar o servidor de histórico principal por três horas. O ensaio testa se os operadores conseguem continuar com segurança usando os procedimentos de modo degradado, se os dados são recuperados por completo depois e se os registros de governança mostram o que aconteceu. Participam dois operadores, uma curadora de dados e o engenheiro de plantão. A Profa. Varga observa e registra os tempos sem intervir, para que o ensaio reflita como a equipe realmente responde. Todos recebem as instruções antes.

### 47.2 Durante a falha

Os operadores passam para os painéis locais e as leituras manuais em quinze minutos, seguindo o procedimento. O engenheiro de plantão recebe o alerta prontamente, mas perde tempo procurando as instruções de recuperação, que estavam guardadas no servidor que falhou. A curadora marca os dados afetados no registro. Kofi observa que guardar as instruções de recuperação no próprio sistema a ser recuperado é um erro clássico, e que o ensaio o revelou em um ambiente seguro, e não durante um incidente real. Ele registra o atraso para encontrar as instruções, com sua duração.

### 47.3 Recuperação

Depois que o servidor de histórico volta, as leituras armazenadas nos *buffers* dos dispositivos locais são recarregadas. Kofi concilia as leituras recarregadas com os *buffers* locais e encontra uma pequena lacuna em que um *buffer* ficou cheio e sobrescreveu dados mais antigos. Ele mede o tempo e a completude da recuperação e registra a lacuna com sua causa. A operação da rede concorda em aumentar o tamanho dos *buffers* nos locais críticos. Ele observa que a recuperação só está completa quando os dados estão conciliados, e não simplesmente quando os sistemas reiniciam. Os resultados da conciliação são anexados ao relatório do ensaio para o comitê de governança.

### 47.4 Melhorias

Kofi registra as melhorias: instruções de recuperação transferidas para um local separado, com cópias impressas, *buffers* maiores nos locais críticos e uma etapa de conciliação acrescentada ao *runbook* de recuperação. Um segundo ensaio curto confirma que o engenheiro encontra as instruções rapidamente. A Profa. Varga observa que os ensaios são valiosos porque expõem dependências que os documentos escondem, e que governar dados inclui planejar a sobrevivência dos dados às falhas, e não apenas sua qualidade na operação normal. O comitê pede que um ensaio semelhante seja realizado todo ano, com participantes e cenários diferentes.

### Exemplo resolvido

Kofi conduz um ensaio de falha do servidor de histórico, encontra instruções de recuperação guardadas no servidor que falhou e uma lacuna por sobrescrita de *buffer*, e aprimora a guarda das instruções, o tamanho dos *buffers* e a conciliação na recuperação.

> **Caso sintético.** O ensaio é sintético.

### Erros e limites

Declarar a recuperação quando os sistemas reiniciam ignora os dados perdidos; concilie primeiro.

### Exercícios

- **EX139 — Problema das instruções.** Onde estavam guardadas as instruções de recuperação? *Rubrica:* 3 = no servidor que falhou;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX140 — Causa da lacuna.** O que causou a lacuna de dados? *Rubrica:* 3 = um *buffer* ficou cheio e sobrescreveu dados mais antigos;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX141 — Definição de recuperação.** Quando a recuperação está completa? *Rubrica:* 3 = quando os dados estão conciliados;; 2 = correto;; 1 = ao reiniciar;; 0 = nenhuma.

<a id="ch-48"></a>

## Capítulo 48 — Dossiê de evidências

### Objetivos de aprendizagem

Você vai (1) montar um dossiê de evidências para dados governados; (2) vincular as afirmações às evidências; (3) empacotá-lo para avaliadores e reguladores.

### 48.1 Propósito

Kofi monta um dossiê de evidências para o projeto final e para o trabalho mais amplo de governança das perdas. O dossiê deve permitir que um avaliador ou regulador verifique as afirmações sem pedir explicações a Kofi. Cada afirmação, como a de que os dados de pressão têm donos nomeados ou a de que os controles detectam sensores travados, aponta para evidências: registros de titularidade, registros de testes, constatações de revisão, relatórios de ensaios e registros de decisão. Ele explica que um dossiê é um argumento sustentado por evidências, e não uma pilha de documentos. Cada vínculo é conferido antes de o dossiê ser emitido.

### 48.2 Estrutura

Kofi estrutura o dossiê em torno dos requisitos: para cada requisito, a afirmação, os controles, as evidências e as limitações. Um índice permite saltar para qualquer requisito. Os arquivos de evidência são guardados com datas e versões, e sua integridade é registrada com *hashes* calculados com o hashlib do Python, para que os leitores possam confirmar que os arquivos não mudaram desde a montagem. Ele inclui também o registro da revisão independente e suas respostas, que mostram como o projeto evoluiu. O *hash* de cada arquivo aparece no índice ao lado de seu título, data e número de versão.

### 48.3 Vinculando as afirmações

Kofi verifica se cada afirmação tem evidência e encontra duas sem ela: a de que os curadores foram treinados e a de que as regras de retenção se aplicam aos dados de pressão. Para o treinamento, ele obtém as listas de presença. Para a retenção, descobre que a regra existe na política, mas nunca foi configurada para os dados de pressão; então ele a configura, testa e acrescenta o resultado. Ele observa que montar as evidências pode revelar distâncias entre a política e a prática que ninguém havia notado. As duas novas evidências entram no índice com seus *hashes*.

### 48.4 Público

Kofi escreve um resumo para não especialistas e deixa os detalhes técnicos nos apêndices. Ele pede a uma colega que não conhece o projeto que encontre as evidências de três afirmações escolhidas ao acaso, cronometrando a busca. Cada uma leva menos de cinco minutos. A Profa. Varga observa que os dossiês funcionam quando os leitores conseguem navegar neles sozinhos, e que a disciplina de comprovar cada afirmação torna os engenheiros mais cuidadosos com o que afirmam desde o início. Kofi revisa duas entradas do índice que atrasaram a colega, deixando seus títulos mais claros e acrescentando remissões a partir dos requisitos relacionados.

### Exemplo resolvido

Kofi estrutura um dossiê por requisito, com arquivos de evidência protegidos por *hash*, encontra duas afirmações sem sustentação e fecha uma lacuna na configuração da retenção, e testa a navegação com uma colega que não conhece o projeto.

> **Caso sintético.** O dossiê é sintético.

### Erros e limites

Afirmações sem evidência enfraquecem o dossiê inteiro; retire-as ou sustente-as.

### Exercícios

- **EX142 — Propósito do hash.** Por que os arquivos de evidência recebem *hash*? *Rubrica:* 3 = para confirmar que não mudaram;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX143 — Lacuna de retenção.** O que a afirmação sobre retenção revelou? *Rubrica:* 3 = a regra nunca foi configurada para os dados de pressão;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX144 — Teste de navegação.** Como a navegação foi testada? *Rubrica:* 3 = uma colega que não conhecia o projeto encontrou as evidências de afirmações aleatórias;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-49"></a>

## Capítulo 49 — Trabalho de conclusão de engenharia

### Objetivos de aprendizagem

Você vai (1) escrever um trabalho de conclusão de engenharia sobre governança de dados; (2) apresentar projeto, evidências e avaliação; (3) discutir a contribuição e os limites.

### 49.1 O argumento do trabalho

O trabalho de conclusão de Kofi sustenta que métodos de engenharia, como controle de interfaces, verificação, análise de falhas e ensaios de recuperação, tornam a governança de dados em empresas de saneamento mais confiável do que abordagens baseadas apenas em políticas. Ele apoia o argumento no trabalho com a cadeia de perdas e no projeto final sobre pressão, ambos com dados sintéticos. Ele apresenta a contribuição como um método prático para aplicar a disciplina da engenharia à governança e a posiciona em relação ao DAMA-DMBOK2 e à ISO/IEC 38505-1, que descrevem as funções da governança, mas deixam em aberto os métodos de engenharia. A Profa. Varga aprova esse enquadramento depois de discuti-lo.

### 49.2 Estrutura

O trabalho tem capítulos sobre contexto, literatura, método, a cadeia de perdas, o projeto final, avaliação e discussão. O capítulo de literatura revisa os modelos de qualidade de dados, os direitos de decisão na governança, normas como a ISO 8000 e princípios de gestão de dados como os FAIR. O capítulo de método explica como cada técnica de engenharia foi adaptada. Os capítulos de resultados apresentam projetos, testes e ensaios com evidências tiradas do dossiê. Kofi escreve o capítulo de avaliação em torno dos critérios de sucesso acordados no início do projeto final. Cada capítulo começa com a afirmação que sustenta e termina com um resumo.

### 49.3 Limites

Kofi dedica uma seção aos limites. Todos os dados eram sintéticos, de modo que os efeitos sobre a operação real continuam sem teste. O trabalho se passou em uma única empresa fictícia, então generalizar para outras exige cuidado. Algumas avaliações dependeram de grupos pequenos de usuários. Ele sugere trabalhos futuros: aplicar os métodos a dados reais anonimizados, comparar com empresas que usam governança baseada em políticas e medir os custos de longo prazo. A Profa. Varga observa que uma seção de limites forte aumenta, em vez de reduzir, a credibilidade do trabalho. Cada limite é vinculado a um item específico de trabalho futuro.

### 49.4 Processo de escrita

Kofi escreve o trabalho ao longo de quatro meses, compartilhando os capítulos com a Profa. Varga para receber comentários. As primeiras versões descrevem as atividades em sequência; os comentários o levam a organizar o texto em torno do argumento. Ele confere cada citação com a fonte original e usa os registros de decisão e o dossiê como evidência primária. Ele reflete que escrever esclareceu seu próprio pensamento, porque explicar por que cada método importava expôs premissas que ele havia adotado sem perceber durante o projeto. Ele mantém um registro dos comentários recebidos e das mudanças feitas, que inclui como apêndice.

### Exemplo resolvido

Kofi sustenta que métodos de engenharia fortalecem a governança de dados em saneamento, estrutura o trabalho em torno de evidências e critérios, declara os limites dos dados sintéticos e do caso único e reorganiza as versões em torno do argumento.

> **Caso sintético.** O trabalho é sintético; as normas e os modelos citados são reais.

### Erros e limites

Trabalhos organizados como diários escondem o argumento; organize-os em torno das afirmações.

### Exercícios

- **EX145 — Tese do trabalho.** O que o trabalho sustenta? *Rubrica:* 3 = que métodos de engenharia tornam a governança de dados em saneamento mais confiável;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX146 — Trabalho futuro.** Cite um item de trabalho futuro. *Rubrica:* 3 = dados reais anonimizados, comparação com outras empresas ou custos de longo prazo;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX147 — Mudança pelos comentários.** Como os comentários mudaram as versões? *Rubrica:* 3 = reorganizadas em torno do argumento;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-50"></a>

## Capítulo 50 — Defesa final

### Objetivos de aprendizagem

Você vai (1) defender um trabalho de conclusão de engenharia diante de examinadores; (2) responder a questionamentos com evidências; (3) refletir sobre seu crescimento profissional.

### 50.1 Preparando a defesa

Kofi prepara uma apresentação de vinte minutos que cobre o argumento, os principais projetos, as evidências e os limites. Ele antecipa as perguntas pedindo aos colegas que façam o papel de examinadores e questionem cada afirmação. Ele prepara slides de reserva com registros de testes, tempos dos ensaios e constatações das revisões. Ele treina explicar os pontos técnicos em linguagem simples, já que um dos examinadores é do regulador e não engenheiro, e a apresentação precisa funcionar tanto para especialistas quanto para o público geral. Ele também ensaia o tempo com cuidado, cortando slides até que a fala caiba com folga no tempo permitido, sobrando espaço para uma pergunta inesperada no final.

### 50.2 Perguntas

Os examinadores perguntam por que resultados sintéticos deveriam convencer uma empresa a investir, como os métodos funcionariam em uma empresa menor, com menos pessoal, e se os controles de governança poderiam atrasar a resposta a emergências. Kofi responde com evidências e limites: os testes sintéticos mostram que os métodos funcionam mecanicamente, empresas menores poderiam adotar um conjunto reduzido, priorizado pelo risco, e os procedimentos de segurança mantêm as ações de emergência independentes da aprovação da governança, embora registradas para revisão posterior. Cada resposta remete a uma página específica do trabalho ou do dossiê, para que os examinadores possam conferir as evidências por conta própria.

### 50.3 Um momento difícil

O examinador do regulador contesta uma afirmação do trabalho de que os números de perdas ficaram mais precisos, apontando que as evidências mostram mais consistência, e não precisão comprovada. Kofi concorda, explica a diferença e se oferece para revisar a redação. Os examinadores apreciam a resposta. Mais tarde, a Profa. Varga lhe diz que aceitar com elegância um questionamento válido demonstrou a integridade que os examinadores procuram, e que afirmações exageradas são comuns em trabalhos de conclusão e fáceis de corrigir quando o autor escuta. A redação revisada passa a ser uma das pequenas correções exigidas.

### 50.4 Reflexão

Depois de ser aprovado com pequenas correções, Kofi reflete sobre seu crescimento ao longo de cinco anos: da programação e da medição básicas ao projeto, teste e defesa da governança de dados complexos de saneamento. O que ele mais valoriza são os hábitos da evidência, da revisão e da honestidade sobre os limites. Ele planeja entrar para a equipe de dados da Tidewater e continuar seu desenvolvimento profissional. O próximo curso desta área trata de privacidade e proteção de dados, onde os dados governados encontram os direitos das pessoas que eles descrevem. Ele agradece à orientadora e aos colegas nos agradecimentos.

### Exemplo resolvido

Kofi se prepara para uma banca mista, responde a perguntas sobre poder de convencimento, empresas pequenas e emergências, aceita um questionamento válido sobre precisão e consistência e reflete sobre cinco anos de crescimento.

> **Caso sintético.** A defesa é sintética.

### Erros e limites

Defender uma afirmação exagerada prejudica a credibilidade; corrija-a.

### Exercícios

- **EX148 — Pergunta sobre emergências.** Como os procedimentos de segurança tratam as emergências? *Rubrica:* 3 = as ações de emergência ficam independentes da aprovação, mas são registradas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX149 — Questionamento sobre precisão.** O que o examinador do regulador contestou? *Rubrica:* 3 = afirmou-se precisão, mas mostrou-se consistência;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX150 — Hábitos valorizados.** Quais hábitos Kofi mais valoriza? *Rubrica:* 3 = evidência, revisão e honestidade sobre os limites;; 2 = todos;; 1 = alguns;; 0 = nenhuma.


<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX150. Kofi Mensah, a Profa. Elena Varga, a Politécnica Northfield, a Tidewater Water e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Cerca de 2,16 milhões de leituras por dia.

**EX002.** Um fluxo com falha, e não um consumo menor de água.

**EX003.** Reduz bastante o armazenamento total em sete anos.

**EX004.** Medidores com leituras, mas sem imóvel vinculado.

**EX005.** Doze.

**EX006.** Todas as fontes das quais o relatório depende.

**EX007.** O volume fornecido parece maior, e as perdas estimadas caem.

**EX008.** Inflou mil vezes a demanda desse distrito.

**EX009.** Unidade, data da última calibração e responsável.

**EX010.** Mostra aos donos dos dados o que falhou e por quê.

**EX011.** Parar quando a estrutura está errada; registrar e seguir em linhas ruins isoladas.

**EX012.** Um erro *off-by-one* no tratamento dos carimbos de data e hora.

**EX013.** Resumo, contexto, método, achados, impacto e recomendações.

**EX014.** A aprovação para incluir a validação de unidades em todos os fluxos de dados.

**EX015.** Data, decisão, quem decidiu, opções consideradas e evidências.

**EX016.** Com diferença de até meio por cento.

**EX017.** Cerca de dois por cento.

**EX018.** Perdas, mais erro de medição, mais diferenças de calendário.

**EX019.** 2 por cento (8 de 400).

**EX020.** O intervalo vai acima de 3 por cento.

**EX021.** Uma atualização de firmware em um lote de medidores.

**EX022.** Quando fica sem transmitir por mais tempo que seus sete dias de armazenamento.

**EX023.** Horas aparentemente duplicadas ou ausentes no horário local.

**EX024.** A origem dos dados.

**EX025.** Um nome, uma descrição e uma função.

**EX026.** A regra rejeitava trocas legítimas de medidor.

**EX027.** Medidores antigos enviam leituras diárias, e a completude horária os reprovaria.

**EX028.** Uma leitura de pressão errada poderia deixar um hospital sem água.

**EX029.** Confirmação anual com cada cliente e limites rígidos de acesso.

**EX030.** Faltava-lhe competência para julgar o risco de contaminação.

**EX031.** A titularidade mudava a cada fronteira da rede.

**EX032.** Seu protocolo não autentica os sensores.

**EX033.** Em períodos de tempestade.

**EX034.** Limitou o acesso à conta de processamento e ao grupo da equipe de dados.

**EX035.** Cada rotina verifica se a anterior terminou com as contagens de linhas esperadas.

**EX036.** A atualização de uma biblioteca de datas que mudava a interpretação dos carimbos de data e hora.

**EX037.** Que as leituras apontem para medidores reais, e os medidores para imóveis reais.

**EX038.** Três.

**EX039.** Para que contas antigas possam ser explicadas com os fatos que valiam na época.

**EX040.** Toda leitura aceita tem medidor e unidade válidos.

**EX041.** Um arquivo do fornecedor que chegou com uma nova ordem de colunas.

**EX042.** Valores de configuração que os donos dos dados podem revisar.

**EX043.** Disponibilidade e integridade.

**EX044.** Uma conta compartilhada de analistas, substituída por contas nominais.

**EX045.** Aprovação do dono e criptografia.

**EX046.** Como uma reclamação de conta de cliente, longe de sua causa.

**EX047.** Campos, unidades, formatos, horários, tratamento de erros e contatos.

**EX048.** A eliminação.

**EX049.** Os rejeitos eram medidos, mas ninguém agia sobre eles de forma confiável.

**EX050.** Usar dados semanais de rejeição e limitar as mudanças a passos pequenos.

**EX051.** Uma semana, em vez de três.

**EX052.** Dados pessoais de produção nunca entram em teste; usam-se dados sintéticos.

**EX053.** Novos conjuntos etiquetados recebem as proteções automaticamente.

**EX054.** Os donos dos dados, no registro dos conjuntos de dados.

**EX055.** 230.

**EX056.** Não; são pseudonimizados e continuam sendo dados pessoais.

**EX057.** Em um arquivo de script; agora está no serviço de gestão de chaves.

**EX058.** Ninguém.

**EX059.** Mantêm regras e definições no dia a dia.

**EX060.** O indicador de perdas informado ao regulador.

**EX061.** O fluxo diário de volumes chega até as 06:00 em pelo menos 95 por cento dos dias.

**EX062.** Agregação por distrito, com no mínimo cinquenta imóveis.

**EX063.** Designação de donos, conciliação e pontualidade.

**EX064.** Sete.

**EX065.** As leituras manuais do aplicativo de campo e as vazões brutas dos sensores.

**EX066.** Comparando o grafo com os registros de consultas do *data warehouse* a cada trimestre.

**EX067.** Um sensor de vazão travado.

**EX068.** Porque ameaças e falhas acidentais costumam parecer iguais.

**EX069.** Um detector *flat-line* a cargo da operação da rede.

**EX070.** Acurácia e completude.

**EX071.** Com um medidor de referência portátil durante as visitas de manutenção.

**EX072.** Valores plausíveis e errados.

**EX073.** Era um ponto único de falha.

**EX074.** Alertas só em violações, mais um resumo semanal de tendências.

**EX075.** As falhas e o comportamento humano.

**EX076.** A conciliação entre domínios era fraca na maturidade atual.

**EX077.** A híbrida.

**EX078.** As equipes de domínio atingirem níveis de competência acordados.

**EX079.** Um procedimento documentado para corrigir leituras com aprovação.

**EX080.** Trinta e um.

**EX081.** Injetando erros sintéticos em um ambiente de teste.

**EX082.** 96,5 por cento, 9.650 de 10.000 linhas.

**EX083.** Trocas de medidor, em que os medidores novos começam do zero.

**EX084.** Relatou com as causas e um plano de correção, em vez de baixar o limiar.

**EX085.** 12,2 por cento, 11 de 90 dias.

**EX086.** Uma atualização do sistema de controle acrescentou uma rotina de backup antes da exportação.

**EX087.** Quatro.

**EX088.** Dez de doze.

**EX089.** Comparar a distribuição de cada coluna com seu histórico.

**EX090.** Se construímos os controles do jeito certo.

**EX091.** Detalhes de esquema, horários de atualização e resultados de qualidade.

**EX092.** Nunca inferior à de sua entrada mais sensível.

**EX093.** Eles consultam os selos antes de usar os dados e questionam os donos sobre notas ruins.

**EX094.** 97,75 por cento.

**EX095.** Elas fazem as perdas parecerem maiores do que são.

**EX096.** O faturamento.

**EX097.** O engenheiro de segurança operacional.

**EX098.** Ele depende de um único servidor do *data warehouse*.

**EX099.** As leituras manuais precisam de formulários e unidades padronizados.

**EX100.** Duas semanas, com um arquivo de teste.

**EX101.** Os resultados da conciliação não chegavam aos selos do catálogo.

**EX102.** O líder de governança de dados.

**EX103.** Um *model card* que descreve o algoritmo de vazamentos do fornecedor.

**EX104.** Não, apenas resumos de frequência.

**EX105.** Melhor antecipação de falhas e das preocupações das pessoas.

**EX106.** Vinte e quatro vezes.

**EX107.** Processar apenas os registros novos e alterados.

**EX108.** Testou-os por injeção de erros.

**EX109.** Até as nove da manhã.

**EX110.** Informou o contato do regulador sobre um atraso de um dia.

**EX111.** Outro curador os segue durante um incidente sintético.

**EX112.** Alertas com nomes técnicos de regras.

**EX113.** Acrescentando as informações principais do catálogo ao painel da sala de controle.

**EX114.** Afirmar que a governança causou a melhora sem evidências mais fortes.

**EX115.** Os dados de referência das tarifas ficaram dois meses sem atualização.

**EX116.** Um desligamento no diretório de funcionários dispara um lembrete.

**EX117.** Esgotamento e pontos únicos de falha.

**EX118.** Dois.

**EX119.** Links para a escala de plantão.

**EX120.** Componentes fora do caminho principal.

**EX121.** Os erros foram empurrados para etapas posteriores, onde corrigi-los levava mais tempo.

**EX122.** A aprovação manual das correções de leituras por um único supervisor.

**EX123.** Tempo até o número, parcela no prazo e reapresentações.

**EX124.** Se as quebras de conciliação preveem correções das perdas por distrito.

**EX125.** Para verificar se o método recupera um efeito conhecido.

**EX126.** O tamanho do distrito.

**EX127.** Propondo uma revisão mensal em lote.

**EX128.** Como a Tidewater sabe que os sensores de vazão são precisos.

**EX129.** Ele tratou do assunto em particular, e o colega submeteu a edição à aprovação.

**EX130.** A lógica de controle das válvulas.

**EX131.** Validando cedo os padrões com um engenheiro de operação.

**EX132.** Um público da operação.

**EX133.** Sensores em pontos críticos precisam de limiares mais rigorosos.

**EX134.** Os locais críticos ao gerente de operação; os demais, aos gerentes distritais.

**EX135.** Eles não compartilham as premissas do projetista.

**EX136.** Horas ausentes em um distrito.

**EX137.** Verificações horárias de completude nos locais críticos.

**EX138.** Dados sintéticos não captam todo o comportamento real.

**EX139.** No servidor que havia falhado.

**EX140.** Um *buffer* local ficou cheio e sobrescreveu leituras mais antigas.

**EX141.** Quando os dados estão conciliados, e não quando os sistemas reiniciam.

**EX142.** Para que os leitores possam confirmar que os arquivos não mudaram.

**EX143.** A regra da política nunca havia sido configurada para os dados de pressão.

**EX144.** Uma colega encontrou as evidências de três afirmações aleatórias, cada uma em menos de cinco minutos.

**EX145.** Que métodos de engenharia tornam a governança de dados em saneamento mais confiável do que apenas as políticas.

**EX146.** Aplicar os métodos a dados reais anonimizados.

**EX147.** De uma sequência de atividades para uma estrutura baseada no argumento.

**EX148.** As ações de emergência não esperam a aprovação da governança, mas são registradas para revisão.

**EX149.** As evidências mostravam consistência, não precisão comprovada.

**EX150.** Evidência, revisão e honestidade sobre os limites.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. *ACM Computing Surveys, 41*(3), 1–52. https://doi.org/10.1145/1541880.1541883
- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-188
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- Khatri, V., & Brown, C. V. (2010). Designing data governance. *Communications of the ACM, 53*(1), 148–152. https://doi.org/10.1145/1629175.1629210
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
