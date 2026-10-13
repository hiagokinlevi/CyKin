# Governança de Dados: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 072, curso superior de tecnologia (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 30 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–30 (EX031–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de tecnologia que vão construir e operar as verificações, os scripts, os dicionários e os relatórios que fazem a governança de dados funcionar no dia a dia.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios validam códigos de prioridade e a ordem das datas em ordens de reparo sintéticas, pseudonimizam identificadores de inquilinos com hashes com chave e medem os reparos emergenciais concluídos em até vinte e quatro horas por duas prestadoras sintéticas. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um estudante de tecnologia desde arquivos, SQL, Python e formatos de dados, passando por verificações de qualidade, correções na origem, códigos de referência, dicionários, linhagem, acesso, pseudonimização, solicitações de titulares, retenção e dados de prestadoras, até painéis, relatórios regulatórios, incidentes, automação, um estágio e um projeto aplicado. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Ravi Desai** | Estudante de tecnologia | Inventado |
| **Sra. Hannah Moreau** | Instrutora | Inventada |
| **Eastgate Institute of Technology** | Instituto fictício | Inventado |
| **Calder Valley Housing Association** | Associação habitacional fictícia, com cerca de 9.000 moradias e 30.000 ordens de reparo por ano | Inventada |

### Fontes principais

DAMA-DMBOK2 (2017); ISO 8000-8:2015; Wang e Strong (1996); NIST SP 800-188; GDPR; LGPD. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Começando no Eastgate

### Objetivos de aprendizagem

Você vai (1) descrever a trilha de tecnólogo e seu caso; (2) explicar o foco aplicado do curso; (3) montar um ambiente de trabalho.

### 1.1 O estudante

Ravi Desai começa um curso superior de tecnologia em gestão de dados, com três anos de duração, no fictício Eastgate Institute of Technology. Sua instrutora, a Sra. Hannah Moreau, explica que o curso forma tecnólogos que constroem e operam as ferramentas, as verificações e os relatórios que fazem a governança de dados funcionar no dia a dia. Ao longo do curso, Ravi trabalha com uma organização parceira fictícia, a Calder Valley Housing Association, dona de cerca de nove mil moradias e responsável por umas trinta mil ordens de reparo por ano. Todos os dados usados nos laboratórios são sintéticos. Ravi está animado.

### 1.2 Foco aplicado

A Sra. Moreau explica a diferença entre este curso e um bacharelado. Ravi vai passar a maior parte do tempo fazendo: escrevendo consultas, scripts e verificações de validação, construindo painéis, mantendo dicionários e apoiando os curadores de dados. A teoria aparece onde ajuda a prática. Cada capítulo tem uma tarefa prática ligada à Calder Valley. Ela observa que os tecnólogos costumam ser os primeiros a perceber problemas nos dados, por isso precisam entender governança o bastante para levá-los às pessoas certas e explicar seus efeitos com clareza. Ravi gosta da ênfase prática.

### 1.3 Ambiente de trabalho

Ravi monta seu ambiente: uma instalação de Python usando apenas a biblioteca padrão, um editor de texto, um pequeno banco SQLite com dados sintéticos da Calder Valley e um repositório de controle de versão para seus scripts. A Sra. Moreau insiste em que todo script seja salvo no repositório com uma breve descrição. Ela explica que esse hábito importa na prática, porque scripts escritos para verificações pontuais muitas vezes viram processos essenciais que ninguém consegue encontrar nem explicar depois que o autor sai. Ravi escreve a primeira descrição do repositório naquela mesma tarde.

### 1.4 As necessidades da Calder Valley

A gerente de dados da Calder Valley, uma figura fictícia chamada Sra. Okonjo, encontra a turma. Ela explica que a associação precisa informar o desempenho dos reparos ao órgão regulador, responder às solicitações dos inquilinos sobre seus dados e gerenciar as prestadoras que executam a maior parte dos reparos. Os dados vêm de um sistema de gestão habitacional, dos portais das prestadoras e de planilhas. Ela pede aos estudantes ajuda com problemas práticos, a começar pela qualidade dos registros de ordens de reparo, que alimentam todos os relatórios de desempenho. A turma decide começar por um levantamento dos campos das ordens e de seus usos.

### Exemplo resolvido

Ravi começa o curso de tecnologia, conhece seu foco aplicado, monta um ambiente Python só com a biblioteca padrão e controle de versão e conhece a gerente de dados da Calder Valley, que descreve as necessidades de relatórios de reparo.

> **Caso sintético.** O Eastgate, a Calder Valley e todas as pessoas são sintéticos.

### Erros e limites

Scripts mantidos fora do controle de versão viram processos que ninguém sabe explicar.

### Exercícios

- **EX001 — Tamanho da parceira.** Quantas moradias a Calder Valley possui? *Rubrica:* 3 = cerca de nove mil;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX002 — Papel do tecnólogo.** O que os tecnólogos constroem e operam? *Rubrica:* 3 = ferramentas, verificações e relatórios para a governança;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX003 — Primeiro problema.** Por qual problema a Sra. Okonjo pede que os estudantes comecem? *Rubrica:* 3 = a qualidade dos registros de ordens de reparo;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Dados em uma associação habitacional

### Objetivos de aprendizagem

Você vai (1) identificar os principais conjuntos de dados de uma associação habitacional; (2) mapear como fluem os dados de reparo; (3) reconhecer quem depende deles.

### 2.1 Principais conjuntos de dados

Ravi lista os principais conjuntos de dados da Calder Valley: imóveis com endereços, tipos e componentes como caldeiras; inquilinos e contratos de locação; ordens de reparo com prioridade, datas e prestadora; contas de aluguel; reclamações; e inspeções de segurança, como as verificações de gás. Todos ficam no sistema de gestão habitacional, exceto as atualizações das prestadoras, que chegam por um portal. Ele observa que os imóveis ligam tudo, porque reparos, locações e inspeções se referem a um identificador de imóvel. Ravi registra cada conjunto em uma lista simples, com seu sistema, seu dono, quando conhecido, e a ligação com o imóvel.

### 2.2 Acompanhando um reparo

Ravi acompanha um reparo. Um inquilino informa um vazamento por telefone. Um atendente cria uma ordem com um código de prioridade e designa uma prestadora. A prestadora comparece, atualiza o portal com os detalhes da conclusão, e o portal envia os dados de volta ao sistema habitacional toda noite. Os relatórios usam as ordens concluídas. Ele encontra três passagens em que os dados são digitados ou transferidos, cada uma um ponto por onde erros podem entrar, e as marca em um diagrama. A Sra. Okonjo confirma que o diagrama corresponde ao modo como os reparos realmente funcionam.

### 2.3 Quem depende dos dados de reparo

Muita gente depende dos dados de reparo: inquilinos esperando reparos, atendentes respondendo a perguntas, gestores acompanhando as prestadoras, o financeiro pagando faturas e o órgão regulador avaliando o desempenho. Ravi observa que um erro na data de conclusão pode fazer um reparo atrasado parecer em dia, enganando o regulador, ou fazer um reparo em dia parecer atrasado, levando a uma multa injusta para uma prestadora. Entender quem depende dos dados explica por que a qualidade importa além da equipe de dados. Ravi acrescenta cada grupo ao diagrama, para que o efeito dos erros em cada passagem fique visível de relance.

### 2.4 Dados de segurança

Alguns dados afetam diretamente a segurança dos inquilinos. As verificações de segurança do gás devem ser feitas todo ano, e os registros precisam mostrar quando cada uma aconteceu. A Sra. Moreau ressalta que erros nesses dados são graves: um registro ausente pode significar uma verificação não realizada. Ravi aprende que os dados que sustentam deveres legais de segurança exigem os controles mais rigorosos e que os tecnólogos devem apontar imediatamente qualquer dúvida sobre esses registros, em vez de esperar pelos relatórios de rotina. Ravi anota que os registros de gás pertencem à gerente de conformidade, que deve ser avisada de qualquer dúvida.

### Exemplo resolvido

Ravi lista os conjuntos de dados da Calder Valley, com o imóvel como elo, acompanha um reparo por três passagens, identifica quem depende dos dados, dos inquilinos ao regulador, e aprende que os dados de segurança exigem os controles mais rigorosos.

> **Caso sintético.** Os conjuntos de dados são sintéticos.

### Erros e limites

Tratar registros de segurança como dados de rotina atrasa ações urgentes.

### Exercícios

- **EX004 — Entidade de ligação.** O que liga a maioria dos conjuntos de dados? *Rubrica:* 3 = o identificador do imóvel;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX005 — Número de passagens.** Quantas passagens Ravi encontrou em um reparo? *Rubrica:* 3 = três;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX006 — Frequência da verificação de gás.** Com que frequência as verificações de gás devem ocorrer? *Rubrica:* 3 = todo ano;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Higiene de planilhas e arquivos

### Objetivos de aprendizagem

Você vai (1) organizar arquivos compartilhados; (2) aplicar convenções de nomes e de versões; (3) reduzir riscos em processos baseados em planilhas.

### 3.1 Unidades compartilhadas

A unidade compartilhada da Calder Valley contém milhares de arquivos com nomes como final, final2 e use este. Ravi examina uma pasta e encontra quatro versões da lista de preços das prestadoras, sem nenhum modo de saber qual é a vigente. Ele propõe uma estrutura com pastas por função, uma convenção de nomes que inclui data e versão e uma pasta de arquivo para as versões antigas. Os donos de cada pasta de primeiro nível aprovam a estrutura e se comprometem a mantê-la organizada. A pasta de arquivo mantém as versões antigas disponíveis sem confundir quem usa as atuais.

### 3.2 Convenções de nomes

A convenção de Ravi usa a data na ordem ano-mês-dia, um assunto curto e um número de versão, como 2026-02-14 precos prestadoras v3. Datas nessa ordem ficam corretamente ordenadas. Ele explica que convenções só funcionam se todos as seguem, por isso escreve um guia de uma página com exemplos e pede aos líderes de equipe que lembrem as pessoas. Depois de um mês, ele confere uma amostra de arquivos novos e vê que a maioria segue a convenção. Os poucos que não seguem são renomeados pelos donos após um lembrete gentil dos líderes, e a amostra é repetida um mês depois.

### 3.3 Riscos das planilhas

A planilha de desempenho dos reparos copia dados de uma exportação do sistema habitacional, aplica fórmulas e produz números para os gestores. Ravi encontra uma fórmula que se refere a um intervalo fixo de linhas e deixa de fora as linhas novas, além de uma célula de ajuste manual sem nenhuma anotação. Ele acrescenta uma verificação que compara a contagem de linhas com a exportação, protege as células de fórmula e cria uma coluna de notas que explica os ajustes manuais. Também registra quem prepara a planilha a cada mês. Quem a prepara agora assina uma pequena lista de verificação confirmando que a contagem de linhas bateu antes de enviar os números.

### 3.4 Dados pessoais em arquivos

Ravi procura na unidade compartilhada arquivos com nomes e telefones de inquilinos. Encontra várias listas antigas de ligações em pastas acessíveis a todos os funcionários. Ele as informa à Sra. Okonjo, que pede aos donos que revisem e eliminem os arquivos desnecessários e movam os demais para pastas restritas. A Sra. Moreau explica que arquivos sem gestão são uma fonte comum de vazamentos e de retenção excessiva, e que os tecnólogos conseguem encontrá-los com buscas simples; no Brasil, guardar dados além do necessário contraria o princípio da necessidade da LGPD (art. 6º, III). A busca é repetida a cada trimestre, e o número de arquivos expostos cai de forma constante.

### Exemplo resolvido

Ravi reorganiza uma pasta compartilhada com quatro versões da lista de preços, escreve um guia de nomes com datas, acrescenta a uma planilha verificações de contagem de linhas e encontra listas antigas de ligações de inquilinos em pastas abertas.

> **Caso sintético.** Os arquivos são sintéticos.

### Erros e limites

Convenções sem orientação e sem verificação são ignoradas.

### Exercícios

- **EX007 — Versões da lista de preços.** Quantas versões da lista de preços Ravi encontrou? *Rubrica:* 3 = quatro;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX008 — Ordem das datas.** Por que usar datas no formato ano-mês-dia? *Rubrica:* 3 = elas ficam corretamente ordenadas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX009 — Listas de ligações.** O que Ravi encontrou em pastas abertas? *Rubrica:* 3 = listas antigas de ligações com nomes e telefones de inquilinos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — SQL para verificações de governança

### Objetivos de aprendizagem

Você vai (1) escrever consultas SQL para verificar dados; (2) encontrar órfãos e duplicatas; (3) salvar consultas como verificações reutilizáveis.

### 4.1 Consultas básicas

Usando SQLite, Ravi escreve consultas sobre tabelas sintéticas da Calder Valley. Ele conta as ordens por prioridade, encontra ordens sem prestadora e lista os imóveis sem verificação de gás registrada no último ano. Cada consulta responde a uma pergunta de governança. A Sra. Moreau pede que ele escreva a pergunta como comentário acima de cada consulta, para que outras pessoas entendam seu propósito. Ele observa que o SQL costuma ser o caminho mais rápido para responder a perguntas de qualidade em sistemas construídos sobre bancos relacionais. Os comentários tornam suas consultas fáceis de revisar.

### 4.2 Órfãos

Um órfão é um registro que se refere a algo que não existe, como uma ordem que aponta para um identificador de imóvel ausente da tabela de imóveis. Ravi usa um left join para encontrar as ordens cujo imóvel não existe. Encontra algumas, criadas quando imóveis foram vendidos e removidos do sistema enquanto ainda havia ordens abertas. Ele as informa ao curador de reparos, que encerra as ordens e pede à TI que impeça a exclusão de imóveis com ordens abertas. A TI aplica a restrição em um mês, e a verificação passa a rodar toda semana para confirmar que nenhum novo órfão aparece.

### 4.3 Duplicatas

Ravi procura ordens duplicadas: o mesmo imóvel, a mesma descrição do problema e datas com até dois dias de diferença. Ele usa um self-join e encontra pares em que os inquilinos informaram o problema duas vezes e os atendentes criaram duas ordens. As duplicatas inflam as contagens e podem mandar duas prestadoras ao mesmo endereço. Ele mostra exemplos à gerente da central de atendimento, que acrescenta uma etapa: verificar se já há ordens abertas no imóvel antes de criar uma nova. O número de duplicatas cai no mês seguinte, e as prestadoras relatam menos visitas desperdiçadas.

### 4.4 Verificações reutilizáveis

Ravi salva as consultas úteis no repositório com nome, propósito, dono e resultado esperado. Ele cria um pequeno script Python com sqlite3 que executa todas as verificações salvas e grava os resultados em uma tabela, com a data. A Sra. Moreau observa que transformar consultas em uma biblioteca de verificações as torna repetíveis e revisáveis, e que é assim que muitas organizações constroem seu primeiro monitoramento de qualidade de dados antes de comprar qualquer ferramenta especializada. O curador revisa a tabela de resultados toda manhã e abre um registro de problema quando um resultado muda de forma inesperada.

### Exemplo resolvido

Ravi escreve verificações SQL comentadas, encontra ordens órfãs de imóveis vendidos, encontra ordens duplicadas causadas por relatos repetidos e cria um script que executa as verificações salvas e registra os resultados.

> **Caso sintético.** As tabelas são sintéticas.

### Erros e limites

Consultas sem comentário perdem seu propósito; escreva a pergunta.

### Exercícios

- **EX010 — Causa dos órfãos.** Por que existiam ordens órfãs? *Rubrica:* 3 = imóveis vendidos e removidos com ordens abertas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX011 — Regra de duplicata.** Como Ravi definiu uma ordem duplicada? *Rubrica:* 3 = mesmo imóvel e mesmo problema em até dois dias;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX012 — Correção na central.** Que etapa a central de atendimento acrescentou? *Rubrica:* 3 = verificar antes se há ordens abertas no imóvel;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Fundamentos de scripts em Python

### Objetivos de aprendizagem

Você vai (1) escrever scripts Python para tarefas com dados; (2) tratar arquivos e erros; (3) estruturar scripts para reutilização.

### 5.1 Primeiros scripts

Ravi escreve scripts Python que leem exportações CSV do portal das prestadoras com o módulo csv, contam linhas e resumem as ordens por situação. Ele usa funções para cada etapa: ler, verificar e resumir. A Sra. Moreau revisa o código e pede nomes mais claros, como count_jobs_by_status em vez de f2. Ela explica que nomes claros tornam os scripts legíveis meses depois, quando o autor já esqueceu os detalhes e um colega precisa entendê-los depressa. Ravi renomeia todas as funções de seus scripts naquela semana e passa a revisar os nomes antes de cada envio ao repositório.

### 5.2 Tratando erros

As exportações das prestadoras às vezes chegam sem colunas ou com linhas em branco a mais. O primeiro script de Ravi quebra com esses arquivos. Ele acrescenta verificações que confirmam a presença das colunas esperadas e ignoram linhas em branco, com mensagens claras explicando cada problema. Quando falta uma coluna, o script para e informa qual é, em vez de produzir resultados errados em silêncio. Ele aprende que parar de forma ruidosa é melhor do que continuar quieto com dados ruins. Acrescenta ao repositório um pequeno conjunto de arquivos defeituosos de teste, para conferir esses comportamentos sempre que o script mudar.

### 5.3 Datas e números

Os dados de reparo contêm datas em vários formatos, porque as prestadoras usam sistemas diferentes. Ravi usa o módulo datetime para interpretar cada formato esperado e registra todo valor que não corresponde a nenhum. Também converte custos de texto para números com cuidado, tratando símbolos de moeda e separadores. Ele descobre que uma prestadora usa a ordem dia-mês e outra a ordem mês-dia, o que tinha feito datas de conclusão serem lidas errado em relatórios anteriores. Ravi leva o caso ao curador, que pede às duas prestadoras que confirmem seus formatos, e os relatórios anteriores são corrigidos com uma nota explicando a mudança.

### 5.4 Estrutura para reutilização

Ravi organiza seus scripts em um módulo com funções compartilhadas para ler arquivos, interpretar datas e gravar resultados, além de pequenos scripts separados para cada tarefa. Ele escreve testes simples para o interpretador de datas, com exemplos de cada prestadora. A Sra. Moreau observa que funções reutilizáveis fazem com que uma correção, como um novo formato de data, seja feita em um só lugar, o que reduz a chance de scripts diferentes tratarem os mesmos dados de modos diferentes. Quando uma terceira prestadora chega, Ravi acrescenta seu formato ao interpretador compartilhado e todos os scripts passam a tratá-lo corretamente.

### Exemplo resolvido

Ravi escreve scripts baseados em funções com nomes claros, interrompe a execução com aviso quando falta uma coluna, descobre a confusão entre as ordens dia-mês e mês-dia das prestadoras e organiza funções compartilhadas com testes.

> **Caso sintético.** As exportações são sintéticas.

### Erros e limites

Scripts que continuam em silêncio diante de entradas ruins produzem resultados errados.

### Exercícios

- **EX013 — Conselho sobre nomes.** Que conselho sobre nomes a Sra. Moreau deu? *Rubrica:* 3 = usar nomes descritivos como count_jobs_by_status;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX014 — Coluna ausente.** O que o script faz quando falta uma coluna? *Rubrica:* 3 = para e informa qual é;; 2 = correto;; 1 = continua;; 0 = nenhuma.
- **EX015 — Confusão de datas.** Que problema de datas Ravi encontrou? *Rubrica:* 3 = prestadoras usavam as ordens dia-mês e mês-dia;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Formatos e troca de dados

### Objetivos de aprendizagem

Você vai (1) comparar formatos de dados comuns; (2) definir especificações de troca; (3) validar arquivos recebidos.

### 6.1 Formatos comuns

Ravi compara os formatos usados na Calder Valley: CSV nas exportações das prestadoras, JSON vindo do portal dos inquilinos, arquivos de largura fixa do antigo sistema de aluguéis e planilhas dos gestores. O CSV é simples, mas não tem tipos; o JSON carrega estrutura, mas pode variar de um registro para outro; os arquivos de largura fixa exigem posições exatas de coluna. Ele usa os módulos csv e json do Python para ler cada um, anotando os problemas típicos de cada formato. Escreve uma nota curta por formato, descrevendo esses problemas e como seus scripts os tratam, para que os colegas reaproveitem a abordagem.

### 6.2 Especificações de troca

Para reduzir problemas, Ravi ajuda a escrever uma especificação de troca para os arquivos das prestadoras: padrão de nome do arquivo, codificação, delimitador, nomes e ordem das colunas, tipos de dados, datas no formato ano-mês-dia, valores permitidos para situação e prioridade e o que fazer quando uma ordem é cancelada. O curador de reparos a aprova e a envia a todas as prestadoras. Ele observa que uma especificação transforma suposições em acordos e permite rejeitar arquivos que não a cumprem. A especificação é publicada com um arquivo de exemplo contra o qual as prestadoras podem testar.

### 6.3 Validando arquivos

Ravi escreve um validador que confere cada arquivo recebido de uma prestadora com a especificação antes da carga. Arquivos que passam em todas as verificações são carregados automaticamente; os que falham ficam retidos, e a prestadora recebe por e-mail um relatório com os problemas. No primeiro mês, duas prestadoras enviam arquivos fora da especificação, e as duas os corrigem em poucos dias. Ele observa que a validação automática transfere o trabalho de correção para a origem, onde os erros podem ser corrigidos de verdade. As prestadoras passam a testar seus arquivos antes do envio, e as retenções ficam raras depois dos dois primeiros meses.

### 6.4 Mudanças de versão

Quando uma prestadora atualiza seu sistema, surge uma coluna nova, e o validador retém o arquivo. Ravi consulta o curador, que conclui que a coluna é inofensiva e atualiza a especificação para a versão dois, permitindo uma coluna extra opcional. A Sra. Moreau observa que as especificações precisam de controle de versão como o código, para que todos saibam qual versão vale e para que as mudanças sejam deliberadas, e não acidentais, com registro de quem aprovou cada uma. O histórico da especificação fica no repositório ao lado do código do validador, de modo que cada versão possa ser associada ao validador que a aplicou.

### Exemplo resolvido

Ravi compara os formatos CSV, JSON, largura fixa e planilha, ajuda a escrever uma especificação de troca para as prestadoras, constrói um validador que retém arquivos fora da especificação e conduz uma mudança de versão da especificação.

> **Caso sintético.** Os arquivos e as especificações são sintéticos.

### Erros e limites

Aceitar arquivos sem validação leva os erros da origem para os relatórios.

### Exercícios

- **EX016 — Fraqueza do CSV.** Qual é a principal fraqueza do CSV? *Rubrica:* 3 = não ter tipos de dados;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX017 — Arquivos reprovados.** O que acontece com os arquivos que falham na validação? *Rubrica:* 3 = ficam retidos e a prestadora recebe um relatório por e-mail;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX018 — Mudança da versão dois.** O que a versão dois da especificação passou a permitir? *Rubrica:* 3 = uma coluna extra opcional;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Conceitos de qualidade de dados

### Objetivos de aprendizagem

Você vai (1) aplicar dimensões de qualidade aos dados de reparo; (2) escolher medidas para cada uma; (3) relacionar a qualidade aos usos.

### 7.1 Dimensões

A Sra. Moreau apresenta as dimensões de qualidade da pesquisa de Wang e Strong: exatidão, completude, consistência, pontualidade e validade, entre outras. Ravi as aplica às ordens de reparo. Completude significa que as ordens têm prioridade, datas e prestadora. Validade significa que códigos e datas seguem as regras. Exatidão significa que as datas de conclusão refletem quando o trabalho de fato terminou. Pontualidade significa que as atualizações chegam logo depois do serviço. Consistência significa que o sistema habitacional e o portal concordam sobre a mesma ordem. Ravi escreve um exemplo curto de falha para cada dimensão, o que ajuda colegas e curadores a entendê-las depressa.

### 7.2 Medidas

Para cada dimensão, Ravi escreve uma medida. Completude é a parcela de ordens com todos os campos obrigatórios. Validade é a parcela que passa nas regras de código e de data. Consistência é a parcela de ordens cuja situação coincide entre os sistemas. Pontualidade é a parcela de conclusões atualizadas em até um dia. A exatidão é verificada por amostragem, comparando as datas de conclusão com as confirmações dos inquilinos. Ele registra cada medida com sua fórmula, para que os resultados possam ser reproduzidos. O curador revisa as fórmulas e acorda as metas de cada medida com a gerente de dados.

### 7.3 Qualidade e uso

Ravi aprende que a qualidade depende do uso. Para pagar as prestadoras, o que mais importa é a exatidão dos custos. Para os relatórios ao regulador, importam sobretudo as datas de conclusão e as prioridades. Para a comunicação com os inquilinos, importam os dados de contato. Ele monta uma tabela que liga cada uso às dimensões de que depende, o que ajuda a Sra. Okonjo a explicar aos gestores por que alguns problemas exigem atenção urgente e outros podem esperar. A ISO 8000-8 apoia a prática de declarar como cada afirmação de qualidade foi medida. Os gestores decidem priorizar a exatidão das datas de conclusão no trimestre seguinte.

### 7.4 Qualidade como hábito

A Sra. Moreau explica que a qualidade não é um projeto com data para acabar, mas um hábito incorporado ao trabalho diário. Os tecnólogos apoiam esse hábito executando verificações automaticamente, tornando os resultados visíveis e ajudando as pessoas a corrigir as causas. Ravi anota em seu diário que as melhores melhorias de qualidade que viu até agora vieram de pequenas mudanças de processo na origem, como a central de atendimento verificar ordens abertas, e não de grandes mutirões de limpeza. A Sra. Moreau pede à turma que reúna exemplos assim ao longo de todo o curso, para discuti-los em aula no fim de cada semestre.

### Exemplo resolvido

Ravi aplica as dimensões de qualidade às ordens de reparo, escreve uma fórmula para cada uma, liga os usos às dimensões de que dependem e observa que pequenas mudanças na origem são as que mais melhoram a qualidade.

> **Caso sintético.** As medidas são sintéticas; Wang e Strong (1996) e a ISO 8000-8:2015 são reais.

### Erros e limites

Uma única nota de qualidade para todos os usos esconde o que importa para cada um.

### Exercícios

- **EX019 — Medida de consistência.** Como a consistência é medida? *Rubrica:* 3 = parcela de ordens com a mesma situação nos dois sistemas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX020 — Foco do regulador.** Que dimensões importam para os relatórios ao regulador? *Rubrica:* 3 = datas de conclusão e prioridades;; 2 = ambas;; 1 = uma;; 0 = nenhuma.
- **EX021 — Melhores melhorias.** De onde vieram as melhores melhorias? *Rubrica:* 3 = de pequenas mudanças de processo na origem;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Validando ordens de reparo

### Objetivos de aprendizagem

Você vai (1) validar registros de ordens com duas regras; (2) combinar os resultados das regras; (3) relatar as constatações ao curador.

### 8.1 As regras

Ravi valida as ordens de reparo com duas regras acordadas com o curador de reparos. O código de prioridade deve ser E, de emergência, U, de urgente, R, de rotina, ou P, de planejado. A data de conclusão não pode ser anterior à data de abertura da ordem. As duas regras importam para os relatórios regulatórios, porque a prioridade define o prazo-alvo e as datas definem se o prazo foi cumprido. Ele escreve cada regra como uma pequena função com nome claro, e o curador aprova as duas funções depois de conferi-las com exemplos reais de ordens anonimizadas.

```python
"""Validate 6,000 synthetic repair job records: priority code and date order (stdlib only)."""
import random, datetime as dt
random.seed(21)
codes = ["E", "U", "R", "P"]
bad_code = bad_date = both = 0
for i in range(6000):
    c = random.choice(codes) if random.random() > 0.03 else random.choice(["", "X", "e"])
    raised = dt.date(2026, 1, 1) + dt.timedelta(days=random.randint(0, 180))
    done = raised + dt.timedelta(days=random.randint(0, 30) if random.random() > 0.02 else -random.randint(1, 10))
    bc, bd = c not in codes, done < raised
    bad_code += bc; bad_date += bd; both += bc and bd
print(f"jobs 6000; invalid priority {bad_code}; completed before raised {bad_date}; both {both}")
print(f"valid on both rules {6000 - bad_code - bad_date + both} ({100*(6000 - bad_code - bad_date + both)/6000:.1f}%)")
```

Execute com `python3 lab_jobs.py`. Saída verificada:

```text
jobs 6000; invalid priority 167; completed before raised 122; both 8
valid on both rules 5719 (95.3%)
```

### 8.2 Resultados

O laboratório verifica seis mil ordens sintéticas. Cento e sessenta e sete têm prioridade inválida, como um campo em branco, uma letra desconhecida ou um e minúsculo. Cento e vinte e duas foram concluídas antes de serem abertas. Oito falham nas duas regras. No total, 5.719 ordens, ou 95,3 por cento, passam nas duas regras. Ravi observa que as ordens que falham nas duas regras são contadas uma única vez no total, e por isso as falhas não podem simplesmente ser somadas. Ele apresenta os resultados em uma pequena tabela, com o número combinado primeiro e, em seguida, as falhas de cada regra.

### 8.3 Causas

Ravi examina uma amostra de ordens reprovadas e as discute com o curador. O e minúsculo vem de um portal de prestadora que não converte maiúsculas e minúsculas. Os campos em branco vêm de ordens criadas às pressas durante tempestades. A conclusão antes da abertura geralmente significa que um atendente criou a ordem depois que a prestadora já tinha resolvido uma emergência, registrando como data de abertura a data da ligação. Cada causa sugere uma correção diferente, da conversão de maiúsculas a orientações mais claras para emergências. Ravi registra cada causa com o número de uma ordem de exemplo em suas anotações.

### 8.4 Relatório

Ravi apresenta ao curador as contagens, a taxa combinada de aprovação, exemplos sem os dados dos inquilinos, as causas prováveis e as correções sugeridas. O curador aceita a conversão de maiúsculas e pede aos atendentes que registrem o horário do relato original nas emergências. Ravi acrescenta as duas regras à biblioteca de verificações, para rodarem toda noite. A Sra. Moreau observa que relatar as causas junto com as contagens ajuda o curador a agir, em vez de apenas se preocupar com um número. O curador apresenta o relatório na reunião mensal de reparos, e os gestores decidem acompanhar a taxa de aprovação todo mês.

### Exemplo resolvido

Ravi valida 6.000 ordens e encontra 167 prioridades inválidas, 122 conclusões anteriores à abertura e 8 ordens com as duas falhas, com 5.719 (95,3 por cento) válidas; ele investiga as causas e acrescenta as regras às verificações noturnas.

> **Caso sintético.** As ordens são sintéticas; as saídas vêm de lab_jobs.py.

### Erros e limites

Somar as contagens de falhas conta duas vezes os registros que falham em mais de uma regra.

### Exercícios

- **EX022 — Parcela válida.** Que parcela das ordens passa nas duas regras? *Rubrica:* 3 = 95,3% (5.719);; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX023 — Causa do minúsculo.** De onde vem o e minúsculo? *Rubrica:* 3 = de um portal que não converte maiúsculas e minúsculas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX024 — Causa das datas.** Por que algumas ordens foram concluídas antes de serem abertas? *Rubrica:* 3 = ordens de emergência criadas depois do conserto;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Corrigindo problemas na origem

### Objetivos de aprendizagem

Você vai (1) distinguir correções na origem de limpezas posteriores; (2) implantar controles na origem; (3) medir o efeito.

### 9.1 Limpar versus corrigir

Ravi poderia corrigir as prioridades inválidas toda noite com um script, convertendo as letras minúsculas e adivinhando os campos em branco. A Sra. Moreau pergunta o que aconteceria no mês seguinte: os mesmos erros voltariam a chegar, e os palpites poderiam estar errados. Ela explica que a limpeza posterior trata sintomas, enquanto a correção na origem previne os erros. A limpeza pode ser necessária por algum tempo, mas deve vir acompanhada de uma correção na origem e ser registrada, para que os relatórios mostrem o que foi alterado. Ravi decide buscar primeiro as correções na origem, registrando qualquer limpeza temporária.

### 9.2 Controles na origem

Ravi trabalha com a equipe do portal das prestadoras para converter os códigos de prioridade em maiúsculas e rejeitar campos em branco antes do envio. No sistema habitacional, os atendentes agora escolhem a prioridade em uma lista suspensa, em vez de digitá-la. Para as emergências, um campo novo registra o horário em que o inquilino relatou o problema pela primeira vez, de modo que ordens criadas depois mantêm o horário correto de abertura. Cada mudança é testada com ordens sintéticas antes da liberação. A equipe do portal e a TI liberam as mudanças juntas depois dos testes, com a aprovação do curador.

### 9.3 Medindo o efeito

Depois das mudanças, Ravi repete a validação em um novo mês de ordens sintéticas desenhadas para refletir o novo processo. As prioridades inválidas caem bastante, e os erros de conclusão antes da abertura também, à medida que os atendentes usam o campo novo. Ele relata a comparação de antes e depois ao curador, observando que os dados sintéticos do novo mês refletem suas suposições sobre as mudanças e que só o monitoramento real confirmará se a melhora se mantém. Ele agenda uma conferência dos resultados reais para três meses depois, sob responsabilidade do curador, que os relatará ao gerente de reparos.

### 9.4 A limpeza que resta

Alguns registros antigos ainda contêm erros. Ravi e o curador decidem corrigir as prioridades históricas quando o valor correto puder ser confirmado pela descrição da ordem, marcando cada correção com um código de motivo, e deixar as demais sinalizadas como desconhecidas. Ele observa que as correções precisam ser rastreáveis, para que quem revisar relatórios antigos veja quais valores mudaram, quando e por quê, e que adivinhar em silêncio prejudicaria a confiança nos relatórios. Os registros sinalizados aparecem em um relatório separado, para que os gestores saibam quais números passados carregam incerteza.

### Exemplo resolvido

Ravi escolhe correções na origem em vez da limpeza noturna, acrescenta a conversão para maiúsculas, a rejeição de campos em branco, as listas suspensas e um campo com o horário do primeiro relato, mede o efeito e corrige registros antigos apenas com códigos de motivo rastreáveis.

> **Caso sintético.** As mudanças são sintéticas.

### Erros e limites

Correções silenciosas feitas depois escondem erros recorrentes na origem.

### Exercícios

- **EX025 — Problema da limpeza.** Por que a limpeza noturna não basta? *Rubrica:* 3 = os mesmos erros voltam e os palpites podem estar errados;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX026 — Campo para emergências.** Que campo novo apoia as ordens de emergência? *Rubrica:* 3 = o horário em que o inquilino relatou o problema pela primeira vez;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX027 — Correções históricas.** Como as correções históricas são marcadas? *Rubrica:* 3 = com um código de motivo;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Códigos de referência e tabelas de consulta

### Objetivos de aprendizagem

Você vai (1) gerenciar listas de códigos de referência; (2) manter as tabelas de consulta consistentes entre sistemas; (3) tratar mudanças de códigos ao longo do tempo.

### 10.1 Listas de códigos

A Calder Valley usa muitas listas de códigos: prioridades, tipos de serviço, tipos de imóvel, identificadores de prestadoras e categorias de reclamação. Ravi descobre que as listas de tipos de serviço diferem entre o sistema habitacional e o portal das prestadoras, com alguns códigos presentes em um e ausentes no outro. Ele cria uma lista mestra em uma tabela de referência, sob responsabilidade do curador de reparos, e uma tabela de correspondência que liga os códigos do portal aos códigos mestres. Códigos sem correspondência são sinalizados na carga dos arquivos. O curador aprova a lista e a correspondência depois de conferir cada código com a central e as prestadoras.

### 10.2 Consistência

Ravi escreve uma verificação noturna que compara as listas de códigos de cada sistema com a lista mestra. As diferenças aparecem em um relatório curto para o curador. Quando um novo tipo de serviço é necessário, o curador primeiro o acrescenta à lista mestra, e só depois a TI e a equipe do portal o incluem em seus sistemas. Ele observa que essa ordem impede que os sistemas se afastem um do outro, o que antes fazia os relatórios descartarem ordens com códigos que a ferramenta de relatórios não reconhecia. O relatório costuma vir vazio, sinal de que o processo funciona como esperado.

### 10.3 Mudanças ao longo do tempo

Os códigos mudam. A Calder Valley funde dois tipos de serviço, reparo de reboco e reparo de parede, em um só. Ravi acrescenta datas de início e de fim à lista mestra, para que os relatórios históricos continuem mostrando os tipos antigos nos períodos passados enquanto as ordens novas usam o código fundido. Ele cria uma correspondência para os relatórios de tendência que precisam de categorias consistentes ao longo do tempo. Explica que apagar códigos antigos quebraria os relatórios históricos. O curador aprova as datas de fim e a correspondência, e Ravi testa os relatórios de tendência para confirmar que os períodos passados mostram as categorias esperadas.

### 10.4 Documentação

Cada código tem uma descrição, exemplos e a data em que passou a valer. Ravi publica a lista mestra na intranet para que os atendentes possam conferir os significados. Uma atendente percebe que dois códigos têm descrições quase idênticas e pergunta qual deve usar. O curador esclarece a diferença e atualiza as descrições. A Sra. Moreau observa que publicar as listas de códigos provoca perguntas úteis, o que melhora a consistência mais do que mantê-las escondidas em tabelas de sistema. Os atendentes agora consultam a lista publicada com frequência, e cai o número de ordens registradas com o tipo errado.

### Exemplo resolvido

Ravi cria uma lista mestra de tipos de serviço com correspondências para o portal, executa verificações noturnas de consistência, acrescenta datas de início e de fim para um código fundido e publica descrições que provocam um esclarecimento útil.

> **Caso sintético.** As listas de códigos são sintéticas.

### Erros e limites

Apagar códigos antigos quebra os relatórios históricos; encerre-os com uma data de fim.

### Exercícios

- **EX028 — Dono da lista mestra.** Quem é o dono da lista mestra de tipos de serviço? *Rubrica:* 3 = o curador de reparos;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX029 — Ordem das mudanças.** Que ordem se segue para novos tipos de serviço? *Rubrica:* 3 = primeiro a lista mestra, depois os sistemas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX030 — Tipos fundidos.** Que tipos de serviço foram fundidos? *Rubrica:* 3 = reparo de reboco e reparo de parede;; 2 = ambos;; 1 = um;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Ravi Desai, a Sra. Hannah Moreau, o Eastgate Institute of Technology, a Calder Valley Housing Association e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Cerca de nove mil.

**EX002.** As ferramentas, as verificações e os relatórios que fazem a governança funcionar.

**EX003.** A qualidade dos registros de ordens de reparo.

**EX004.** O identificador do imóvel.

**EX005.** Três.

**EX006.** Todo ano.

**EX007.** Quatro.

**EX008.** Elas ficam corretamente ordenadas.

**EX009.** Listas antigas de ligações com nomes e telefones de inquilinos.

**EX010.** Imóveis foram removidos enquanto ainda havia ordens abertas.

**EX011.** Mesmo imóvel, mesma descrição e datas com até dois dias de diferença.

**EX012.** Verificar se há ordens abertas no imóvel antes de criar uma nova.

**EX013.** Usar nomes descritivos, como count_jobs_by_status.

**EX014.** Para e informa qual coluna está faltando.

**EX015.** Uma prestadora usava a ordem dia-mês e outra, a ordem mês-dia.

**EX016.** Não carrega tipos de dados.

**EX017.** Ficam retidos, e a prestadora recebe um relatório com os problemas.

**EX018.** Uma coluna extra opcional.

**EX019.** A parcela de ordens cuja situação coincide entre os sistemas.

**EX020.** A exatidão das datas de conclusão e das prioridades.

**EX021.** Pequenas mudanças de processo na origem.

**EX022.** 95,3 por cento, 5.719 ordens.

**EX023.** Um portal de prestadora que não converte maiúsculas e minúsculas.

**EX024.** Os atendentes criavam as ordens de emergência depois que as prestadoras já as tinham resolvido.

**EX025.** Os erros continuam chegando e os palpites podem estar errados.

**EX026.** O horário em que o inquilino relatou o problema pela primeira vez.

**EX027.** Com um código de motivo.

**EX028.** O curador de reparos.

**EX029.** Acrescentar primeiro à lista mestra e depois a cada sistema.

**EX030.** Reparo de reboco e reparo de parede.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-188
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
