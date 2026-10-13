# Governança de Dados: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 118, engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 50 já estão escritos em português, com os exercícios EX001–EX060 e suas resoluções com rubricas de 0 a 3; os capítulos 21–50 (EX061–EX150) e os quatro laboratórios estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas serão mantidas idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

Capítulos 21–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

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
- **EX002 — Falha de fluxo.** O que pode significar uma queda brusca na taxa de leituras? *Rubrica:* 3 = um fluxo de dados com falha;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX003 — Efeito da agregação.** O que faz a agregação em totais diários depois de dois anos? *Rubrica:* 3 = reduz muito o armazenamento;; 2 = menciona redução;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX004 — Regra do conjunto vazio.** Que conjunto deveria ser vazio? *Rubrica:* 3 = medidores com leituras mas sem imóvel vinculado;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX005 — Verificação de função.** Quantos medidores correspondiam a dois imóveis? *Rubrica:* 3 = doze;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX006 — Uso do grafo.** O que mostra seguir as arestas no sentido inverso a partir de um relatório? *Rubrica:* 3 = todas as fontes das quais ele depende;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX007 — Efeito da deriva.** Como uma deriva para cima do sensor afeta as estimativas de perdas? *Rubrica:* 3 = as perdas parecem menores;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX008 — Erro de unidade.** O que a confusão de unidades fez com um distrito? *Rubrica:* 3 = inflou mil vezes a demanda;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
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

- **EX010 — Arquivo de rejeitos.** Por que gravar um arquivo de rejeitos em vez de descartar linhas? *Rubrica:* 3 = dá aos donos evidências para corrigir a origem;; 2 = menciona evidências;; 1 = nenhuma;; 0 = nenhuma.
- **EX011 — Política de erros.** O que significa falhar alto na estrutura e baixo no conteúdo? *Rubrica:* 3 = parar quando falta coluna, registrar linhas ruins e continuar;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX012 — Achado da revisão.** O que a revisão de código encontrou? *Rubrica:* 3 = um erro *off-by-one* nos carimbos de data e hora;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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
- **EX014 — Decisão do gestor.** Que decisão o gestor tomou? *Rubrica:* 3 = aprovar a validação de unidades em todos os fluxos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
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
- **EX020 — Julgamento da meta.** Por que o dono não pode afirmar que a meta de 3 por cento foi cumprida? *Rubrica:* 3 = o intervalo inclui valores acima de 3 por cento;; 2 = menciona intervalo;; 1 = nenhuma;; 0 = nenhuma.
- **EX021 — Sinal de controle.** O que causou o dia fora dos limites? *Rubrica:* 3 = uma atualização de firmware em um lote de medidores;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX022 — Limite de sete dias.** Quando um medidor perde leituras? *Rubrica:* 3 = falha mais longa que seu período de armazenamento;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX023 — Horário de verão.** Que problema o horário de verão cria? *Rubrica:* 3 = horas aparentemente duplicadas ou ausentes;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX024 — Limite do checksum.** O que um *checksum* não prova? *Rubrica:* 3 = quem enviou os dados;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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
- **EX026 — Achado do teste.** O que o teste unitário revelou? *Rubrica:* 3 = a regra rejeitava indevidamente trocas de medidor;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX027 — Revisão do domínio.** O que o engenheiro de medição apontou? *Rubrica:* 3 = medidores antigos enviam leituras só uma vez por dia;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX028 — Exemplo de segurança.** Dê uma consequência de dados ruins para a segurança das pessoas. *Rubrica:* 3 = uma leitura de pressão errada deixa um hospital sem água;; 2 = menciona dano;; 1 = nenhuma;; 0 = nenhuma.
- **EX029 — Cuidado com o cadastro.** O que Kofi recomendou para o cadastro prioritário? *Rubrica:* 3 = confirmação anual e acesso restrito;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX030 — Competência.** Por que Kofi encaminhou a mudança na qualidade da água? *Rubrica:* 3 = faltava-lhe competência em química;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX031 — Troca de responsável.** Por que ninguém conseguia responder a perguntas de ponta a ponta? *Rubrica:* 3 = o responsável pela governança muda a cada fronteira;; 2 = menciona fronteiras;; 1 = nenhuma;; 0 = nenhuma.
- **EX032 — Lacuna industrial.** Que lacuna Kofi encontrou na rede industrial? *Rubrica:* 3 = protocolo sem autenticação;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX033 — Dados atrasados.** Quando os atrasos se concentram? *Rubrica:* 3 = em períodos de tempestade;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX034 — Correção de permissão.** O que Kofi mudou no diretório de extratos? *Rubrica:* 3 = leitura só pela conta de processamento e pela equipe de dados;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX035 — Encadeamento de rotinas.** Como as rotinas agora se protegem de entradas ruins? *Rubrica:* 3 = cada uma verifica se a anterior teve sucesso com as contagens esperadas;; 2 = menciona a anterior;; 1 = nenhuma;; 0 = nenhuma.
- **EX036 — Achado da homologação.** O que o teste em homologação detectou? *Rubrica:* 3 = uma mudança na interpretação de carimbos de data e hora;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX037 — Finalidade da chave estrangeira.** O que as chaves estrangeiras garantem aqui? *Rubrica:* 3 = leituras se referem a medidores reais, e medidores a imóveis reais;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX038 — Listas de distritos.** Quantas versões da lista de distritos existiam? *Rubrica:* 3 = três;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX039 — Finalidade do histórico.** Por que guardar datas de início e fim de vigência? *Rubrica:* 3 = para explicar contas antigas com os fatos da época;; 2 = menciona o passado;; 1 = nenhuma;; 0 = nenhuma.

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

- **EX040 — Requisito testável.** Dê um requisito testável do *pipeline*. *Rubrica:* 3 = leituras aceitas têm medidor e unidade válidos; rejeitos relatados em uma hora; totais conciliam;; 2 = um;; 1 = nenhuma;; 0 = nenhuma.
- **EX041 — Achado dos testes de dados.** O que os testes de dados detectaram? *Rubrica:* 3 = um arquivo do fornecedor com nova ordem de colunas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX042 — Valores fixos.** O que substituiu os limiares fixos no código? *Rubrica:* 3 = valores de configuração revisados pelos donos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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
- **EX044 — Conta compartilhada.** Que problema do *data warehouse* Kofi corrigiu? *Rubrica:* 3 = conta compartilhada de analistas substituída por contas nominais;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
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

- **EX046 — Sintoma distante.** Como um defeito de firmware em medidores pode aparecer? *Rubrica:* 3 = como uma reclamação de conta;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
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

- **EX049 — Malha aberta.** Por que a malha de qualidade da Tidewater estava aberta? *Rubrica:* 3 = não havia uma etapa confiável de ação corretiva;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
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

- **EX052 — Regra para dados de teste.** Que regra Kofi propôs para os ambientes de teste? *Rubrica:* 3 = dados pessoais de produção nunca entram em teste;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX053 — Controles por etiqueta.** Por que atrelar os controles a etiquetas de metadados? *Rubrica:* 3 = as proteções se aplicam automaticamente e escalam;; 2 = menciona automático;; 1 = nenhuma;; 0 = nenhuma.
- **EX054 — Responsável pelas etiquetas.** Quem aprova as etiquetas de classificação? *Rubrica:* 3 = os donos dos dados, no registro;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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
- **EX057 — Local da chave.** Onde uma chave estava guardada indevidamente? *Rubrica:* 3 = em um arquivo de script;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

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
- **EX059 — Dever do curador.** O que fazem os curadores? *Rubrica:* 3 = mantêm regras e definições no dia a dia;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX060 — Indicador de foco.** Que indicador os capítulos seguintes acompanham? *Rubrica:* 3 = o indicador de perdas informado ao regulador;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060 (as de EX061–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Kofi Mensah, a Profa. Elena Varga, a Politécnica Northfield, a Tidewater Water e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
