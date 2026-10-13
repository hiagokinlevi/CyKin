# Governança de Dados: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 095, bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 40 já estão escritos em português, com os exercícios EX001–EX060, suas resoluções com rubricas de 0 a 3 e o laboratório do capítulo 18; os capítulos 21–40 (EX061–EX120) e os outros dois laboratórios estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas serão mantidas idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de bacharelado que aprendem governança de dados desde os princípios, passando por políticas, qualidade, privacidade e retenção, até um trabalho de conclusão de curso.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios medem a completude de cinco campos em registros sintéticos de fidelidade, conferem códigos de loja com uma lista de referência e contam os registros guardados além de uma regra de retenção de três anos de inatividade. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de bacharelado desde os fundamentos de dados, planilhas, bancos de dados, Python e estatística, passando por papéis, políticas, qualidade, metadados, segurança, privacidade, compartilhamento e retenção na governança, até um projeto em grupo, um estágio e um trabalho de conclusão com defesa oral. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Amara Okafor** | Estudante de bacharelado | Inventada |
| **Dr. Paul Lindqvist** | Tutor | Inventado |
| **Universidade Ridgeway** | Universidade fictícia | Inventada |
| **Harbourline Co-operative** | Cooperativa de supermercados fictícia, com quarenta lojas e cerca de 250.000 membros no programa de fidelidade | Inventada |

### Fontes principais

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-8:2015; Khatri e Brown (2010), [doi:10.1145/1629175.1629210](https://doi.org/10.1145/1629175.1629210); Wang e Strong (1996); Wilkinson et al. (2016); NIST Privacy Framework 1.0; GDPR; LGPD. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

Capítulos 21–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Estudando governança de dados em Ridgeway

### Objetivos de aprendizagem

Você vai (1) descrever o curso e seu caso; (2) explicar por que as organizações governam dados; (3) definir metas pessoais de aprendizagem.

### 1.1 A estudante e o curso

Amara Okafor começa um bacharelado de quatro anos em gestão da informação na fictícia Universidade Ridgeway. Seu tutor, o Dr. Paul Lindqvist, explica que o curso acompanha uma única organização do início ao fim: a Harbourline Co-operative, uma cooperativa de supermercados fictícia com quarenta lojas e cerca de um quarto de milhão de membros no programa de fidelidade. Cada ano acrescenta profundidade, desde as habilidades básicas com dados no primeiro ano até o projeto da governança, um estágio e um trabalho de conclusão nos anos finais. Todos os dados usados nos exercícios e laboratórios são sintéticos, criados para o ensino. Amara está animada.

### 1.2 Por que a Harbourline precisa de governança

A Harbourline guarda dados de vendas, estoque, fornecedores, funcionários e fidelidade. Os gestores reclamam que os relatórios não batem entre si, que ninguém sabe qual lista de clientes é a atual e que um e-mail de marketing recente foi enviado a membros que haviam pedido para não ser contatados. O Dr. Lindqvist explica que esses são problemas de governança: ninguém tem autoridade clara sobre as definições, a qualidade ou os usos permitidos dos dados. A tecnologia sozinha não os resolve, porque as questões de fundo envolvem decisões, responsabilidades e regras que as pessoas da organização precisam acordar. Amara anota essas reclamações.

### 1.3 Como o curso funciona

Cada capítulo apresenta um tema, aplica-o à Harbourline e termina com exercícios. Alguns capítulos incluem laboratórios curtos escritos em Python usando apenas a biblioteca padrão, executados sobre dados sintéticos, com os resultados citados exatamente no texto. Amara é orientada a manter um diário de aprendizagem, anotando perguntas e conexões entre os temas. O Dr. Lindqvist diz que o diário vai ajudá-la mais tarde a escolher o tema do trabalho de conclusão, porque as perguntas recorrentes costumam revelar o que mais interessa a um estudante. Ela começa o diário naquela mesma noite, com três perguntas.

### 1.4 Metas de aprendizagem

Amara escreve três metas: entender por que os dados dão errado nas organizações, aprender habilidades práticas para verificar dados e ser capaz de explicar escolhas de governança a gestores que não são especialistas. O Dr. Lindqvist acrescenta uma quarta: aprender a julgar evidências, porque as decisões de governança devem se apoiar em fatos sobre os dados, e não em impressões. Eles combinam revisar as metas todo ano. Escrever as metas cedo lhe dá um modo de medir o progresso e de ajustar mais tarde a escolha das disciplinas optativas. As metas ficam guardadas no diário.

### Exemplo resolvido

Amara começa o bacharelado, conhece os relatórios divergentes e os e-mails mal direcionados da Harbourline, entende o formato dos capítulos e laboratórios e define quatro metas de aprendizagem com o tutor.

> **Caso sintético.** Ridgeway, a Harbourline e todas as pessoas são sintéticas.

### Erros e limites

Tratar a governança como a compra de um software ignora as decisões e as responsabilidades.

### Exercícios

- **EX001 — Caso do curso.** Que organização o curso acompanha? *Rubrica:* 3 = a Harbourline Co-operative;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX002 — Problema do e-mail.** O que deu errado com um e-mail de marketing? *Rubrica:* 3 = foi enviado a membros que pediram para não ser contatados;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX003 — Quarta meta.** Que meta o tutor acrescentou? *Rubrica:* 3 = aprender a julgar evidências;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — O que são dados

### Objetivos de aprendizagem

Você vai (1) distinguir dados, informação e conhecimento; (2) descrever os tipos de dados; (3) explicar como o contexto molda o significado.

### 2.1 Dados, informação, conhecimento

O Dr. Lindqvist explica que dados são símbolos registrados, como um número em um registro do caixa. Informação é o dado com significado em um contexto, como saber que aquele número é a quantidade de leite vendida na loja doze em uma terça-feira. Conhecimento é a compreensão que permite agir, como saber que as vendas de leite sobem antes dos feriados e encomendar mais estoque. Amara observa que a governança trabalha sobretudo com dados e informação, mas que seu propósito é sustentar um bom conhecimento e boas decisões. Amara concorda.

### 2.2 Tipos de dados

Amara aprende os tipos mais comuns: números para quantidades e preços, texto para nomes e descrições, datas e horas para as transações, códigos para categorias como loja ou produto e valores verdadeiro ou falso para indicadores como o consentimento para marketing. Cada tipo tem regras: um preço não pode ser negativo, uma data precisa existir no calendário e um código precisa constar de uma lista acordada. Conhecer o tipo de cada campo ajuda as pessoas a verificar se um valor sequer faz sentido. Os tipos são documentados.

### 2.3 Contexto e significado

O mesmo valor pode significar coisas diferentes. Na Harbourline, as vendas no sistema financeiro incluem impostos, enquanto as vendas no sistema das lojas os excluem. As duas se chamam vendas. Quando os gestores comparam os relatórios, os números divergem pelo valor do imposto, e cada lado supõe que o outro está errado. Amara percebe que a falta de contexto, e não um erro de aritmética, causa a divergência. Registrar as definições junto com os dados é, portanto, uma das ações de governança mais simples e mais úteis que uma organização pode adotar. Mais tarde, a Harbourline acrescenta as definições aos relatórios.

### 2.4 Estruturados e não estruturados

Os registros do caixa e os níveis de estoque são dados estruturados, guardados em tabelas com campos definidos. E-mails de clientes, contratos com fornecedores e fotografias das lojas são não estruturados, com informações mais difíceis de pesquisar e verificar. A Harbourline tem muito mais dados não estruturados do que imaginava, boa parte em pastas compartilhadas sem dono. O Dr. Lindqvist explica que a governança precisa cobrir os dois, embora os métodos sejam diferentes: dados estruturados se prestam a regras automáticas, enquanto os não estruturados dependem mais de classificação, controle de acesso e retenção. Amara conta milhares de arquivos sem dono em uma única pasta.

### Exemplo resolvido

Amara distingue dados, informação e conhecimento, aprende os tipos de dados e suas regras, descobre que uma diferença de impostos explica relatórios de vendas divergentes e registra dados não estruturados sem dono em pastas compartilhadas.

> **Caso sintético.** Os exemplos são sintéticos.

### Erros e limites

Supor que rótulos idênticos significam definições idênticas gera disputas.

### Exercícios

- **EX004 — Exemplo de conhecimento.** Dê o exemplo de conhecimento usado no curso. *Rubrica:* 3 = as vendas de leite sobem antes dos feriados, então encomenda-se mais;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX005 — Divergência de vendas.** Por que os relatórios de vendas divergiam? *Rubrica:* 3 = o financeiro inclui impostos, as lojas os excluem;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX006 — Exemplo não estruturado.** Cite um exemplo de dado não estruturado na Harbourline. *Rubrica:* 3 = e-mails de clientes, contratos ou fotografias;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Dados nas organizações

### Objetivos de aprendizagem

Você vai (1) rastrear como os dados se movem dentro de uma organização; (2) identificar quem cria e quem usa os dados; (3) explicar por que os problemas aparecem longe de suas causas.

### 3.1 Seguindo uma venda

Amara segue uma única venda pela Harbourline. O caixa registra os itens, os preços e o cartão de fidelidade. O sistema da loja envia os totais ao financeiro toda noite. O sistema de fidelidade acrescenta pontos. O sistema de estoque reduz o inventário. Mais tarde, o marketing analisa as compras para enviar ofertas. Uma única ação no caixa cria dados usados por cinco sistemas e várias equipes. Ela desenha o percurso em um diagrama e percebe que um erro no caixa se espalha pelo financeiro, pelo estoque e pelo marketing. Os funcionários da loja confirmam, em uma reunião curta, que o diagrama está correto.

### 3.2 Quem cria e quem usa

Os funcionários das lojas criam a maior parte dos dados, mas raramente usam relatórios. As equipes da sede usam relatórios, mas raramente veem como os dados são criados. Amara entrevista uma supervisora de loja, que conta que os funcionários muitas vezes digitam um código de produto genérico quando o código de barras falha, para a fila andar. A sede, então, vê vendas estranhas do produto genérico. Nenhum dos lados conhece a situação do outro. Ela conclui que a governança precisa ligar quem cria a quem usa, para que cada um entenda o efeito de suas ações sobre o outro. Amara organiza uma visita conjunta.

### 3.3 Efeitos distantes

Um preço errado cadastrado no sistema de produtos aparece semanas depois como uma divergência de estoque nas lojas e, em seguida, como um problema de margem no financeiro. Quando o financeiro percebe, a causa é difícil de rastrear. Amara compara os problemas de dados à poluição de um rio: o efeito aparece rio abaixo, longe da fonte. A governança precisa de meios para rastrear os efeitos até as causas, e é por isso que os capítulos seguintes tratam em detalhe de linhagem, titularidade e gestão de problemas. Amara anota a comparação com o rio no diário, para uso futuro.

### 3.4 Dados como recurso compartilhado

O Dr. Lindqvist explica que, na Harbourline, os dados são recursos compartilhados, usados por muitas equipes, mas com dono claro em poucos casos. Sem regras, cada equipe otimiza para as próprias necessidades, como fazem os funcionários das lojas com os códigos genéricos. O resultado se parece com o uso excessivo de um pasto comum, em que todos saem perdendo. Amara observa que a governança cria as regras e os papéis que permitem a um recurso compartilhado continuar útil para todos, equilibrando a conveniência local e as necessidades mais amplas de toda a cooperativa. A comparação a ajuda a explicar a governança a amigos que estudam economia.

### Exemplo resolvido

Amara rastreia uma venda por cinco sistemas, descobre que os códigos de produto genéricos digitados nos caixas distorcem os relatórios da sede e compara os problemas de dados à poluição rio abaixo.

> **Caso sintético.** Os sistemas e as entrevistas são sintéticos.

### Erros e limites

Culpar a equipe que percebe um problema ignora sua origem.

### Exercícios

- **EX007 — Sistemas envolvidos.** Quantos sistemas usam os dados de uma única venda? *Rubrica:* 3 = cinco;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX008 — Códigos genéricos.** Por que os funcionários digitam códigos de produto genéricos? *Rubrica:* 3 = para a fila andar quando o código de barras falha;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX009 — Recurso compartilhado.** O que as regras de governança equilibram? *Rubrica:* 3 = a conveniência local e as necessidades mais amplas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Planilhas e seus riscos

### Objetivos de aprendizagem

Você vai (1) reconhecer os erros comuns em planilhas; (2) aplicar controles simples a planilhas; (3) decidir quando os dados devem sair das planilhas.

### 4.1 Planilhas por toda parte

A Harbourline executa muitos processos em planilhas: escalas das lojas, planos de promoções, listas de preços de fornecedores e o resumo semanal de vendas para o conselho. Planilhas são flexíveis e familiares, o que explica sua popularidade. Amara examina o resumo semanal e descobre que ele é montado copiando números de três relatórios, com fórmulas ligando doze abas. Uma única pessoa o mantém. Ela observa que a flexibilidade também facilita os erros, e que processos críticos que dependem da planilha de uma só pessoa criam riscos que a organização pode não enxergar. A responsável costuma estar de férias.

### 4.2 Erros comuns

Amara revisa a pesquisa sobre erros em planilhas e procura no resumo os problemas típicos. Ela encontra um intervalo de fórmula que termina uma linha antes do fim, de modo que a loja mais nova fica fora dos totais. Ela encontra números guardados como texto, que as somas ignoram, e um valor digitado por cima de uma fórmula. Nada disso era visível nos totais finais. Ela explica que os erros em planilhas são comuns em parte porque os resultados parecem arrumados, o que desestimula a verificação. As vendas da loja mais nova estavam fora dos totais do conselho havia três semanas antes da revisão.

### 4.3 Controles simples

Amara propõe controles: uma célula de verificação que compara o total do resumo com o total do relatório de origem, células de fórmula protegidas, histórico de versões em uma unidade compartilhada e uma aba de descrição que explica as fontes e as etapas. Ela sugere também que uma segunda pessoa revise o resumo todo mês. Esses controles custam pouco e capturam os erros que ela encontrou. O Dr. Lindqvist observa que controles proporcionais funcionam melhor com planilhas do que proibi-las, o que raramente dá certo na prática. A responsável concorda com os quatro controles, e a segunda revisora é nomeada na aba de descrição.

### 4.4 Quando seguir adiante

Alguns processos ficam grandes demais para planilhas. Amara sugere critérios: muitos usuários editando ao mesmo tempo, dados que alimentam outros sistemas, relatórios regulatórios ou volumes grandes demais para revisão manual. O resumo do conselho atende a dois critérios, então ela recomenda construí-lo na ferramenta de relatórios, com ligação direta aos dados de origem, eliminando as etapas de cópia. O plano de promoções continua em planilha, com controles. Ela aprende que as decisões de governança sobre ferramentas devem seguir o risco e o uso, e não a moda. Dois meses depois, o conselho recebe seu primeiro resumo gerado pela ferramenta de relatórios, sem etapas de cópia.

### Exemplo resolvido

Amara encontra no resumo do conselho um intervalo de fórmula incompleto, números guardados como texto e uma fórmula sobrescrita, propõe totais de verificação, proteção e revisão e recomenda levar o resumo para a ferramenta de relatórios.

> **Caso sintético.** As planilhas são sintéticas.

### Erros e limites

Totais arrumados não provam que as fórmulas estão corretas; concilie com as fontes.

### Exercícios

- **EX010 — Loja ausente.** Por que a loja mais nova ficou de fora? *Rubrica:* 3 = um intervalo de fórmula terminava uma linha antes;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX011 — Célula de verificação.** O que a célula de verificação compara? *Rubrica:* 3 = o total do resumo com o total do relatório de origem;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX012 — Processo transferido.** Que processo sai das planilhas? *Rubrica:* 3 = o resumo de vendas do conselho;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Bancos de dados e tabelas

### Objetivos de aprendizagem

Você vai (1) descrever tabelas, chaves e relacionamentos; (2) escrever consultas simples; (3) explicar como o projeto do banco de dados sustenta a qualidade dos dados.

### 5.1 Tabelas e chaves

Amara aprende que um banco de dados relacional guarda os dados em tabelas de linhas e colunas. A tabela de membros tem uma linha por membro do programa de fidelidade, identificada por um número de membro que funciona como chave primária. A tabela de compras registra cada compra com o número de membro como chave estrangeira, que a liga ao membro. As chaves impedem membros duplicados e garantem que as compras se refiram a membros que existem. Ela percebe que escolhas de projeto como as chaves impõem regras automaticamente. O banco de dados rejeita uma compra com um número de membro desconhecido.

### 5.2 Consultas

Usando um pequeno banco de dados sintético montado com o módulo sqlite3 do Python, Amara escreve consultas para contar os membros por loja, somar as compras por mês e encontrar membros sem compras em um ano. Ela aprende que uma consulta é uma pergunta precisa, e que a formulação importa: contar compras e contar membros distintos que compraram dão respostas diferentes. Ela registra cada consulta com uma descrição simples, para que outras pessoas possam verificar o que foi perguntado e reutilizá-la depois. Suas descrições ficam em um arquivo compartilhado, com o texto da consulta ao lado.

### 5.3 Projeto e qualidade

Amara descobre que o antigo banco de dados de fidelidade da Harbourline guardava a loja do membro como texto livre, o que produzia variações como Loja 12, loja doze e L12. Os relatórios agrupados por loja dividiam uma loja em várias. Um projeto melhor guarda um código de loja ligado a uma tabela de referência de lojas. Ela explica que um bom projeto evita muitos problemas de qualidade já na entrada, o que é mais barato do que limpá-los depois, e relaciona isso às regras tratadas nos capítulos seguintes. O novo sistema de fidelidade usa códigos de loja, e os antigos valores em texto são mapeados uma única vez.

### 5.4 Normalização em resumo

O Dr. Lindqvist apresenta a normalização: organizar as tabelas para que cada fato seja guardado uma única vez. No banco antigo, o endereço do membro aparece em cada linha de compra, de modo que mudar um endereço deixa as linhas mais antigas inconsistentes. Levar o endereço para a tabela de membros resolve isso. Amara observa que a normalização reduz a inconsistência, mas pode tornar as consultas mais complexas, e que bancos de dados de relatórios às vezes repetem dados de propósito, por desempenho. O equilíbrio certo depende de como os dados são usados. Por esse motivo, o banco de relatórios da Harbourline repete os nomes das lojas nas tabelas de vendas, por projeto.

### Exemplo resolvido

Amara aprende chaves e relacionamentos, escreve consultas em sqlite3 com descrições simples, descobre nomes de lojas em texto livre que dividem os relatórios e vê a normalização eliminar endereços repetidos.

> **Caso sintético.** O banco de dados é sintético.

### Erros e limites

Contar linhas quando a pergunta pede pessoas distintas dá respostas erradas.

### Exercícios

- **EX013 — Papel da chave estrangeira.** A que o número de membro nas compras está ligado? *Rubrica:* 3 = à tabela de membros;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX014 — Problema do texto livre.** O que os nomes de lojas em texto livre causaram? *Rubrica:* 3 = uma loja dividida em várias nos relatórios;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX015 — Contrapartida da normalização.** O que a normalização pode dificultar? *Rubrica:* 3 = as consultas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Python para verificação de dados

### Objetivos de aprendizagem

Você vai (1) ler arquivos de dados com Python; (2) escrever verificações simples; (3) relatar os resultados com clareza.

### 6.1 Lendo arquivos

Amara aprende a ler arquivos separados por vírgula com o módulo csv do Python. Ela abre uma extração sintética de adesões ao programa de fidelidade, lê cada linha como um dicionário indexado pelos nomes das colunas e conta as linhas. Ela aprende a especificar a codificação do arquivo, porque os nomes com acentos apareceram embaralhados quando ela não o fez. Ela observa que ler os dados corretamente é a primeira verificação: se o arquivo for lido errado, todos os resultados seguintes estarão errados, por mais cuidadosa que a análise pareça. Ela passa a declarar a codificação em todo script que escreve depois disso.

### 6.2 Escrevendo verificações

Ela escreve funções que testam uma regra cada: CEP presente, e-mail contendo uma arroba, ano de nascimento entre 1910 e 2010. Cada função devolve verdadeiro ou falso para uma linha. Um laço aplica todas as funções e conta as falhas por regra. Ela mantém as verificações pequenas e com nomes claros, para que um leitor veja exatamente o que cada uma testa. O Dr. Lindqvist explica que verificações simples e legíveis são mais fáceis de confiar e de manter do que verificações engenhosas. Cada função tem um comentário de uma linha que descreve a regra que implementa e sua origem.

### 6.3 Relatando os resultados

O primeiro relatório de Amara lista as falhas como contagens brutas. O tutor pergunta o que as contagens significam sem os totais, então ela acrescenta as porcentagens e o número de linhas verificadas. Ela também lista alguns exemplos de linhas com falha, sem os dados pessoais, para que os leitores vejam como os problemas se parecem. Ela aprende que um bom relatório responde o que foi verificado, quanto falhou, por que isso importa e o que deve acontecer em seguida, nessa ordem. Ela usa essa ordem em todos os relatórios seguintes, e o tutor registra a melhora na nota.

### 6.4 Trabalho repetível

Amara salva o script com comentários e a data da extração usada. Quando o tutor lhe pede para executá-lo de novo sobre uma extração mais recente, leva segundos. Um colega que verificou os dados à mão em uma planilha precisa repetir horas de trabalho. Ela percebe que os scripts tornam as verificações repetíveis e sua lógica visível, o que importa para a governança, porque as verificações devem ser executadas com regularidade e revisadas por outras pessoas, e não feitas uma vez e esquecidas. Mais tarde, o script é compartilhado com a equipe de dados da Harbourline, que o adota.

### Exemplo resolvido

Amara lê uma extração de adesões com a codificação certa, escreve verificações pequenas e bem nomeadas, relata contagens com porcentagens e exemplos e executa de novo o script sobre uma nova extração em segundos.

> **Caso sintético.** As extrações são sintéticas.

### Erros e limites

Relatar contagens sem totais esconde a escala dos problemas.

### Exercícios

- **EX016 — Problema de codificação.** O que aconteceu sem a codificação especificada? *Rubrica:* 3 = os nomes com acentos ficaram embaralhados;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX017 — Regra do ano de nascimento.** Que intervalo a verificação do ano de nascimento usou? *Rubrica:* 3 = de 1910 a 2010;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX018 — Ordem do relatório.** Que ordem um relatório deve seguir? *Rubrica:* 3 = o que foi verificado, quanto falhou, por que importa, o que vem a seguir;; 2 = correto;; 1 = parcial;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Estatística para o trabalho com dados

### Objetivos de aprendizagem

Você vai (1) resumir dados com estatísticas simples; (2) usar amostras para estimar a qualidade; (3) evitar leituras equivocadas comuns.

### 7.1 Resumos

Amara resume valores sintéticos de cestas de compras com o módulo statistics do Python: média, mediana e desvio-padrão. A cesta média é maior que a mediana porque alguns pedidos grandes a puxam para cima. Ela explica que a mediana descreve melhor uma cesta típica, enquanto a média importa para a receita total. A escolha do resumo certo depende da pergunta. Ela observa que os relatórios da Harbourline usavam apenas médias, o que fazia os clientes típicos parecerem gastar mais do que de fato gastam. Amara acrescenta medianas aos relatórios que prepara.

### 7.2 Amostras

Verificar cada registro à mão é impossível. Amara aprende a sortear uma amostra aleatória de registros, verificar cada um com cuidado e estimar a taxa de erros do conjunto inteiro. Usando o módulo random do Python com uma semente fixa, ela sorteia duzentos endereços de membros e encontra certo número com erros. Ela explica que uma amostra aleatória dá uma estimativa justa, enquanto escolher os registros que parecem suspeitos superestima os problemas, porque esses registros não são típicos do conjunto. Ela registra a semente para que a amostra possa ser sorteada de novo.

### 7.3 Incerteza

Uma estimativa amostral tem incerteza. Amara aprende que amostras maiores dão intervalos mais estreitos, e que informar um intervalo é mais honesto do que um número único. Ela explica a um colega que uma taxa de erros de quatro por cento obtida em duzentos registros poderia, plausivelmente, ser um pouco menor ou maior no conjunto completo. O Dr. Lindqvist a incentiva a sempre informar o tamanho da amostra junto com qualquer estimativa, para que os leitores possam julgar por conta própria sua confiabilidade. Amara acrescenta o tamanho da amostra a todas as estimativas do diário.

### 7.4 Leituras equivocadas

Amara reúne as leituras equivocadas mais comuns: confundir porcentagens com pontos percentuais, comparar grupos de tamanhos muito diferentes, tratar correlação como causa e ignorar dados ausentes. Na Harbourline, um relatório afirmava que os membros do programa de fidelidade gastam mais por causa do programa, mas os membros podem simplesmente ser clientes habituais que aderiram. Ela observa que a governança inclui garantir que os relatórios sejam interpretados corretamente, e não apenas que seus números sejam calculados corretamente a partir de dados precisos. Amara escreve uma nota curta sobre cada leitura equivocada para a equipe de dados, com exemplos tirados dos próprios relatórios da Harbourline.

### Exemplo resolvido

Amara compara as cestas média e mediana, estima os erros de endereço a partir de uma amostra aleatória, informa intervalos com o tamanho da amostra e lista leituras equivocadas, como tratar a correlação da fidelidade como causa.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Amostras escolhidas a dedo superestimam os problemas; sorteie as amostras.

### Exercícios

- **EX019 — Cesta típica.** Que resumo descreve melhor uma cesta típica? *Rubrica:* 3 = a mediana;; 2 = correto;; 1 = a média;; 0 = nenhuma.
- **EX020 — Viés da amostra.** Por que não escolher os registros que parecem suspeitos? *Rubrica:* 3 = eles não são típicos e superestimam os problemas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX021 — Afirmação sobre a fidelidade.** Por que a afirmação sobre os gastos dos membros pode estar errada? *Rubrica:* 3 = clientes habituais podem ter mais propensão a aderir;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Escrevendo sobre dados

### Objetivos de aprendizagem

Você vai (1) escrever relatórios claros sobre problemas de dados; (2) adaptar a escrita ao público; (3) usar gráficos com honestidade.

### 8.1 Clareza

O primeiro relatório de Amara sobre a qualidade dos dados de fidelidade tem dez páginas de tabelas. O Dr. Lindqvist lhe pede que diga a constatação principal em uma frase. Ela escreve: cerca de um em cada cinco registros de fidelidade não tem endereço de e-mail, o que limita as ofertas digitais. O resto do relatório passa a sustentar essa frase. Ela aprende que a escrita clara começa por saber qual é o ponto principal, e que as tabelas pertencem aos apêndices, a menos que os leitores precisem delas para acompanhar o argumento. O tutor dá uma nota muito maior ao relatório revisado.

### 8.2 Públicos

Ela escreve duas versões. Para o gerente de marketing, explica o efeito sobre as campanhas e sugere coletar os e-mails no caixa. Para a equipe de dados, detalha as regras usadas, as contagens por loja e o local do script. Cada público recebe o que precisa para agir. Ela observa que um único relatório para todos geralmente não serve bem a ninguém, porque os gestores pulam os detalhes técnicos e a equipe técnica precisa de mais precisão do que os resumos oferecem. Os dois leitores confirmam que sua versão lhes deu o que precisavam para agir.

### 8.3 Gráficos

Amara desenha um gráfico de barras dos e-mails ausentes por loja. Sua primeira versão começa o eixo vertical em quinze por cento, exagerando as diferenças entre as lojas. Uma colega aponta que os gerentes das lojas poderiam se sentir culpados injustamente. Ela refaz o gráfico começando em zero e acrescenta o número de membros por loja. Ela aprende que os gráficos podem enganar mesmo quando os números estão corretos, e que a apresentação honesta faz parte do trabalho responsável com dados. Mais tarde, os gerentes das lojas agradecem pelo gráfico mais justo e pelo contexto acrescentado.

### 8.4 Linguagem simples

Amara substitui jargões como razão de completude por expressões simples como parcela de registros com endereço de e-mail. Ela mantém os termos técnicos onde a precisão importa e os define uma única vez. O gerente de marketing que lê o texto diz que o relatório revisado é o primeiro relatório de dados que ele leu até o fim. O Dr. Lindqvist observa que a governança depende de que não especialistas entendam os problemas de dados, de modo que escrever com simplicidade é uma competência central para quem trabalha na área. Ela mantém uma lista de substitutos simples para os termos mais comuns.

### Exemplo resolvido

Amara reduz um relatório de dez páginas a uma constatação principal, escreve versões para o marketing e para a equipe de dados, refaz a partir do zero um gráfico enganoso e substitui jargões por expressões simples.

> **Caso sintético.** Os relatórios são sintéticos.

### Erros e limites

Eixos truncados exageram as diferenças; comece as barras do zero.

### Exercícios

- **EX022 — Constatação principal.** Qual foi a constatação de Amara em uma frase? *Rubrica:* 3 = cerca de um em cada cinco registros não tem e-mail;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX023 — Correção do gráfico.** Como Amara corrigiu o gráfico? *Rubrica:* 3 = começou o eixo do zero e acrescentou a contagem de membros;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX024 — Substituição do jargão.** O que substituiu razão de completude? *Rubrica:* 3 = parcela de registros com endereço de e-mail;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Direito e dados

### Objetivos de aprendizagem

Você vai (1) apresentar as linhas gerais da legislação de proteção de dados relevante para a Harbourline; (2) identificar as bases legais e os direitos; (3) reconhecer outros deveres legais sobre os dados.

### 9.1 Noções de proteção de dados

Amara estuda o GDPR, o regulamento europeu, como exemplo de lei de proteção de dados. Ele se aplica a dados pessoais, isto é, informações sobre pessoas identificáveis, como os membros do programa de fidelidade e os funcionários. As organizações devem tratar dados pessoais de forma lícita, leal e transparente, para finalidades especificadas, usando apenas o necessário, mantendo-os exatos, guardando-os pelo tempo estritamente necessário e mantendo-os seguros. No Brasil, a LGPD (Lei nº 13.709/2018) enuncia princípios equivalentes em seu art. 6º. Ela observa que vários desses princípios, como a exatidão e a limitação da conservação, também são preocupações da governança de dados. Amara lista cada princípio com um exemplo da Harbourline.

### 9.2 Bases legais

Cada uso de dados pessoais precisa de uma base legal. A Harbourline trata as compras para operar o programa de fidelidade com base em seu contrato com os membros, enquanto os e-mails de marketing precisam de consentimento. Amara descobre que o antigo formulário de adesão embutia o consentimento para marketing na própria adesão ao programa, o que o GDPR não considera um consentimento livre; a LGPD, no art. 8º, § 4º, também exige que o consentimento se refira a finalidades determinadas. Ela recomenda uma caixa de consentimento separada. Ela explica que a governança deve registrar a base de cada uso, para que as equipes saibam o que é permitido. O novo formulário é introduzido no relançamento seguinte do programa.

### 9.3 Direitos

Os membros têm direitos, entre eles o de acessar seus dados, corrigir erros, opor-se ao marketing e, em alguns casos, obter a eliminação dos dados; na LGPD, esses direitos estão no art. 18. Amara revisa como a Harbourline trata os pedidos e descobre que eles chegam às lojas, à sede e por e-mail, sem um registro central. Alguns ficaram sem resposta. Ela recomenda um canal único de entrada e um registro com prazos. Ela observa que atender aos direitos depende de saber onde os dados pessoais estão guardados, o que exige bons metadados e inventários. O encarregado de proteção de dados concorda e cria o registro naquele mesmo mês.

### 9.4 Outros deveres

Além da proteção de dados, a Harbourline precisa guardar os registros financeiros por prazos definidos para fins fiscais, responder a recolhimentos de alimentos por segurança sanitária usando os dados de fornecedores e de lotes e seguir a legislação trabalhista quanto aos registros dos funcionários. Amara lista esses deveres com os dados que cada um exige. Ela percebe que alguns deveres exigem guardar os dados, enquanto outros exigem eliminá-los, de modo que a governança precisa conciliá-los em uma tabela de temporalidade, em vez de deixar cada equipe decidir sozinha. A lista de Amara se torna o ponto de partida da tabela de temporalidade estudada nos capítulos seguintes.

### Exemplo resolvido

Amara apresenta os princípios do GDPR, encontra um consentimento para marketing embutido e recomenda uma caixa separada, centraliza os pedidos de exercício de direitos e lista os deveres fiscais, de recolhimento e trabalhistas que afetam os dados.

> **Caso sintético.** A Harbourline é sintética; o GDPR e a LGPD são reais. Isto não é aconselhamento jurídico.

### Erros e limites

Consentimento embutido não é livre; separe-o.

### Exercícios

- **EX025 — Base para marketing.** De que base legal os e-mails de marketing precisam aqui? *Rubrica:* 3 = consentimento;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX026 — Problema dos direitos.** Que problema Amara encontrou nos pedidos de exercício de direitos? *Rubrica:* 3 = não havia registro central, e alguns ficaram sem resposta;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX027 — Dados de recolhimento.** Que dados sustentam os recolhimentos por segurança dos alimentos? *Rubrica:* 3 = os dados de fornecedores e de lotes;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e dados

### Objetivos de aprendizagem

Você vai (1) aplicar o raciocínio ético aos usos de dados; (2) considerar os efeitos sobre diferentes grupos; (3) explicar o papel da ética ao lado do direito.

### 10.1 Além da lei

Alguns usos de dados são legais, mas questionáveis. A equipe de marketing da Harbourline propõe usar padrões de compra para inferir quais membros estão grávidas e enviar ofertas de produtos para bebês. Amara pondera se os membros esperariam isso, se poderia causar dano caso as ofertas chegassem a um domicílio antes que a pessoa decidisse compartilhar a notícia e se o benefício justifica o risco. Ela conclui que a legalidade é um mínimo, e que a governança deve perguntar também se um uso é justo e esperado. O marketing suspende a proposta para revisão.

### 10.2 Efeitos sobre os grupos

Amara examina uma proposta de oferecer descontos apenas aos membros que usam o aplicativo. Os membros mais velhos e os que não têm smartphone sairiam perdendo. Ela verifica os dados sintéticos de membros e descobre que os usuários do aplicativo são, em sua maioria, mais jovens. Ela sugere oferecer os mesmos descontos por meio de cupons impressos nos caixas. Ela aprende que decisões orientadas por dados podem prejudicar grupos sem que ninguém tenha essa intenção, e que verificar os efeitos entre os grupos deveria ser rotina antes de lançar programas assim. O marketing adota a opção dos cupons na campanha seguinte. Os membros mais velhos a recebem bem.

### 10.3 Modelos de análise

O Dr. Lindqvist apresenta modelos simples: considerar as consequências para todos os afetados, respeitar a autonomia e as expectativas das pessoas, tratar os grupos com justiça e ser transparente sobre as práticas. Amara os aplica à proposta de inferir gravidez e escreve uma avaliação curta recomendando contra ela. O marketing aceita um plano revisto que oferece descontos em produtos para bebês aos membros que escolhem o interesse família em seu perfil. Ela observa que os modelos ajudam a estruturar a discussão, em vez de produzir respostas automáticas. Sua avaliação é guardada como exemplo para revisões futuras. O marketing concorda.

### 10.4 A ética na governança

Amara propõe que o grupo de governança de dados da Harbourline revise os novos usos de dados que levantam questões éticas, usando uma lista de verificação curta. O grupo incluiria pessoas do marketing, das lojas e da proteção de dados. Ela observa que a revisão ética funciona melhor cedo, antes de as campanhas serem desenhadas, e que deve ser rápida para usos de baixo risco. O Dr. Lindqvist acrescenta que as organizações a quem se confiam dados precisam merecer essa confiança continuamente, por meio de suas escolhas. O grupo de governança testa a lista por três meses e constata que a maioria das revisões leva menos de uma hora.

### Exemplo resolvido

Amara avalia uma proposta de inferir gravidez e recomenda contra ela, descobre que descontos exclusivos do aplicativo prejudicam os membros mais velhos, aplica modelos simples e propõe uma lista de verificação ética para novos usos.

> **Caso sintético.** As propostas são sintéticas.

### Erros e limites

Legal não significa aceitável; pergunte se os usos são justos e esperados.

### Exercícios

- **EX028 — Alternativa à inferência.** O que substituiu o plano de inferir gravidez? *Rubrica:* 3 = descontos para membros que escolhem o interesse família;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX029 — Correção do desconto no aplicativo.** Como Amara tratou o desconto exclusivo do aplicativo? *Rubrica:* 3 = cupons impressos nos caixas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX030 — Momento da revisão.** Quando a revisão ética funciona melhor? *Rubrica:* 3 = cedo, antes de as campanhas serem desenhadas;; 2 = correto;; 1 = tarde;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Fundamentos da governança

### Objetivos de aprendizagem

Você vai (1) definir governança de dados; (2) comparar governança e gestão de dados; (3) descrever os modelos usados na prática.

### 11.1 Uma definição

No segundo ano, Amara estuda a governança diretamente. O DAMA-DMBOK2 descreve a governança de dados como o exercício de autoridade, controle e tomada de decisão compartilhada sobre a gestão dos ativos de dados. O Dr. Lindqvist simplifica isso para a Harbourline: decidir quem decide o quê sobre os dados e garantir que essas decisões sejam cumpridas. Amara observa que a definição se concentra nas decisões e na responsabilização, e não na tecnologia, o que explica por que os capítulos anteriores constataram que os problemas persistiam mesmo depois de a Harbourline comprar sistemas novos. Amara escreve a definição simplificada na primeira página de suas anotações.

### 11.2 Governança e gestão

Amara aprende a separar a governança da gestão. A gestão faz o trabalho: opera os bancos de dados, limpa os registros, constrói os relatórios. A governança define a direção e verifica se o trabalho atende aos padrões acordados. Na Harbourline, a equipe de dados gerencia o banco de dados de fidelidade, enquanto um grupo de governança deveria decidir as definições, as metas de qualidade e os usos permitidos. Misturar as duas coisas deixa quem faz o trabalho também decidindo as regras, sem ninguém independente verificando se essas regras servem com justiça à cooperativa inteira. Amara desenha a separação como duas colunas em suas anotações.

### 11.3 Modelos

Amara compara modelos. O DAMA-DMBOK2 organiza a gestão de dados em áreas de conhecimento, com a governança no centro. A ISO/IEC 38505-1 aplica aos dados a norma de governança de TI, pedindo aos órgãos de governança que avaliem, dirijam e monitorem o uso dos dados. Khatri e Brown descrevem cinco domínios de decisão: princípios, qualidade, metadados, acesso e ciclo de vida. Ela explica que os modelos oferecem vocabulário e listas de verificação, mas cada organização precisa adaptá-los a seu porte e a suas necessidades, em vez de copiá-los por inteiro. Amara escolhe os domínios de Khatri e Brown para sua avaliação.

### 11.4 O ponto de partida da Harbourline

Amara avalia a Harbourline pelos domínios de Khatri e Brown. Os princípios não estão escritos. A qualidade é tratada de forma reativa, quando chegam reclamações. Os metadados existem apenas em algumas planilhas. O acesso é concedido pela TI a pedido, sem aprovação de um dono. As decisões de ciclo de vida, como a retenção, ficam a cargo de cada equipe. Ela resume a situação em uma tabela de uma página que o diretor de operações da cooperativa usa mais tarde para defender a criação de um grupo de governança com mandato claro. A tabela de Amara se torna o primeiro documento revisado pelo novo grupo.

### Exemplo resolvido

Amara define a governança como decidir quem decide sobre os dados, separa-a da gestão, compara o DAMA-DMBOK2, a ISO/IEC 38505-1 e Khatri e Brown e avalia a Harbourline pelos cinco domínios.

> **Caso sintético.** A Harbourline é sintética; os modelos são reais.

### Erros e limites

Copiar um modelo completo para uma organização pequena cria burocracia sem uso.

### Exercícios

- **EX031 — Definição do tutor.** Como o tutor simplifica a governança? *Rubrica:* 3 = decidir quem decide o quê sobre os dados e garantir que as decisões sejam cumpridas;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX032 — Cinco domínios.** Cite os cinco domínios de Khatri e Brown. *Rubrica:* 3 = princípios, qualidade, metadados, acesso, ciclo de vida;; 2 = todos;; 1 = alguns;; 0 = nenhuma.
- **EX033 — Prática de acesso.** Como o acesso era concedido na Harbourline? *Rubrica:* 3 = pela TI, a pedido, sem aprovação de um dono;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Papéis e responsabilização

### Objetivos de aprendizagem

Você vai (1) descrever os papéis comuns de governança; (2) atribuir papéis na Harbourline; (3) explicar a responsabilização na prática.

### 12.1 Papéis comuns

Amara estuda os papéis mais comuns. Um conselho ou grupo de governança define prioridades e resolve disputas. Os donos dos dados são gestores seniores que respondem por domínios específicos de dados, como fidelidade ou produtos. Os curadores (*data stewards*) cuidam no dia a dia das definições, das regras de qualidade e dos problemas. Os custodiantes, muitas vezes da TI, operam os sistemas e aplicam os controles. Os usuários seguem as regras e relatam problemas. Ela observa que os nomes variam entre as organizações, mas a separação entre decidir, manter e operar aparece na maioria dos modelos. Amara desenha os papéis em um organograma simples.

### 12.2 Atribuindo os papéis

Amara esboça a atribuição de papéis na Harbourline. O diretor de marketing é dono dos dados de fidelidade, a diretora comercial é dona dos dados de produtos e o diretor financeiro é dono dos números de vendas. Um curador em cada equipe mantém as definições e trata os problemas. Os custodiantes da TI operam os sistemas. O diretor de operações preside o grupo de governança. Cada atribuição inclui uma declaração curta das decisões que o papel pode tomar. Ela discute o rascunho com cada pessoa e o ajusta onde as responsabilidades se sobrepunham ou faltavam na primeira versão. Todos os donos assinam.

### 12.3 Responsabilização

Responsabilização significa responder pelos resultados, o que inclui explicar as falhas e corrigi-las. Amara pergunta ao diretor de marketing o que ele faria se os dados de fidelidade se mostrassem imprecisos. Ele diz que pediria à TI que os corrigisse. Ela explica que, como dono, ele deveria aprovar as regras de qualidade, garantir que sua equipe as siga e decidir as prioridades das correções. A responsabilização não pode ser delegada à TI, embora as tarefas possam. Ele concorda depois de ver exemplos de outras organizações. Ele assina sua declaração de titularidade no fim daquela semana.

### 12.4 Tornando os papéis reais

Papéis que existem só no papel costumam fracassar. Amara recomenda incluir as atribuições de governança nas descrições de cargo, reservar tempo de curadoria nos planos de trabalho e relatar o desempenho dos papéis nas reuniões do grupo de governança. Ela sugere também uma integração curta para novos donos e curadores. O Dr. Lindqvist observa que a falha mais comum é nomear curadores sem lhes dar tempo, de modo que eles tratam a governança como uma tarefa extra, que desaparece quando o resto do trabalho aperta. O diretor de operações inclui tempo de curadoria nos planos de trabalho do ano seguinte de cada equipe, com horas acordadas.

### Exemplo resolvido

Amara descreve os papéis de conselho, dono, curador, custodiante e usuário, atribui-os na Harbourline, deixa claro que o diretor de marketing continua respondendo pelos dados de fidelidade e recomenda descrições de cargo e tempo de curadoria.

> **Caso sintético.** Os papéis são sintéticos.

### Erros e limites

Nomear curadores sem reservar tempo faz o papel desaparecer.

### Exercícios

- **EX034 — Dono da fidelidade.** Quem é dono dos dados de fidelidade? *Rubrica:* 3 = o diretor de marketing;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX035 — Limite da delegação.** O que não pode ser delegado à TI? *Rubrica:* 3 = a responsabilização;; 2 = correto;; 1 = as tarefas;; 0 = nenhuma.
- **EX036 — Falha comum.** Qual é a falha mais comum dos papéis? *Rubrica:* 3 = nomear curadores sem lhes dar tempo;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Políticas e padrões

### Objetivos de aprendizagem

Você vai (1) distinguir políticas, padrões e procedimentos; (2) redigir uma política de dados; (3) manter os documentos de política utilizáveis.

### 13.1 Três níveis

Amara aprende que uma política enuncia princípios e responsabilidades, como os dados devem ter um dono nomeado. Um padrão define requisitos específicos, como todo registro de fidelidade deve ter um código de loja válido da lista de referência. Um procedimento descreve passos, como pedir um novo código de loja. Manter esses níveis separados permite que as políticas fiquem estáveis enquanto os padrões e os procedimentos mudam com mais frequência. Ela descobre que os documentos existentes da Harbourline misturam os três em textos longos e pouco lidos. Amara propõe separá-los.

### 13.2 Redigindo uma política

Amara redige uma política de dados de duas páginas para a Harbourline: propósito, escopo, princípios, papéis, conformidade e revisão. Os princípios incluem: os dados têm donos nomeados, a qualidade é medida e relatada, os dados pessoais são usados apenas para as finalidades declaradas e a retenção segue a tabela de temporalidade. Ela pede comentários aos donos e incorpora suas sugestões. O grupo de governança aprova a política. Ela aprende que uma política curta, que as pessoas leem, é mais eficaz do que uma longa, que elas ignoram. Seu rascunho é mais curto do que qualquer política anterior da Harbourline sobre dados.

### 13.3 Os padrões em detalhe

Sob a política, Amara escreve um padrão de qualidade para os dados de fidelidade: campos obrigatórios, valores permitidos, formatos e níveis-alvo de completude. Ela baseia a forma de medição na ISO 8000-8, que enfatiza que as afirmações sobre qualidade devem dizer como foram medidas. Cada requisito aponta para uma verificação que pode ser executada automaticamente. Ela observa que padrões sem verificações viram aspirações, enquanto padrões com verificações podem ser monitorados e cobrados por meio de relatórios regulares. O padrão é publicado junto com a política e revisado todo ano pelo dono dos dados de fidelidade.

### 13.4 Mantendo os documentos utilizáveis

Amara propõe um único local on-line para políticas, padrões e procedimentos, cada um com dono, versão, data de revisão e um resumo simples. Documentos sem revisão há dois anos são sinalizados. Ela testa a facilidade de encontrá-los pedindo a funcionários das lojas que localizem o procedimento para corrigir endereços de membros; a maioria consegue em poucos minutos. O Dr. Lindqvist lembra-lhe que os documentos são ferramentas para quem trabalha, de modo que a usabilidade importa tanto quanto o conteúdo. Dois funcionários não conseguem encontrá-lo, e o título do procedimento é mudado para as palavras que os funcionários de fato usam.

### Exemplo resolvido

Amara separa política, padrão e procedimento, redige uma política aprovada de duas páginas, escreve um padrão mensurável para os dados de fidelidade e organiza os documentos em um único lugar, com donos e datas de revisão.

> **Caso sintético.** Os documentos são sintéticos; a ISO 8000-8:2015 é real.

### Erros e limites

Políticas longas que misturam níveis não são lidas; separe e encurte.

### Exercícios

- **EX037 — Exemplo de padrão.** Dê o exemplo de padrão usado no curso. *Rubrica:* 3 = todo registro de fidelidade tem um código de loja válido;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX038 — Tamanho da política.** Qual era o tamanho da política de Amara? *Rubrica:* 3 = duas páginas;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX039 — Sinalização de revisão.** Quando os documentos são sinalizados? *Rubrica:* 3 = sem revisão há dois anos;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Dimensões da qualidade de dados

### Objetivos de aprendizagem

Você vai (1) descrever as dimensões comuns da qualidade de dados; (2) escolher as dimensões para um uso; (3) reconhecer que a qualidade depende do uso.

### 14.1 Dimensões

Amara estuda a pesquisa de Wang e Strong, que perguntou aos consumidores de dados o que qualidade significava para eles e agrupou as respostas nas categorias intrínseca, contextual, representacional e de acessibilidade. As dimensões comuns incluem exatidão, completude, consistência, pontualidade, validade e unicidade. Batini e colegas revisam como os métodos medem essas dimensões. Ela observa que a pesquisa partiu da visão dos usuários, e não de definições técnicas, o que sustenta a ideia de que a qualidade depende do uso que se faz dos dados na Harbourline. Amara lista cada dimensão com um exemplo curto da Harbourline, para que os donos possam relacioná-las ao seu trabalho.

### 14.2 Adequação ao uso

O ano de nascimento de um membro pode não importar para enviar recibos, mas é essencial para ofertas ligadas à idade. A exatidão do código de loja importa para os relatórios regionais, mas não para o cálculo de pontos. Amara explica que os mesmos dados podem ser bons o bastante para uma finalidade e inadequados para outra. Ela lista os principais usos dos dados de fidelidade e as dimensões de que cada um mais depende, produzindo uma matriz que mostra onde as melhorias de qualidade trariam mais benefício para a cooperativa. A matriz é compartilhada com os donos para comentários.

### 14.3 Medindo as dimensões

Para cada dimensão, Amara propõe uma medida. A completude é a parcela de registros com valor preenchido. A validade é a parcela que passa nas regras de formato. A unicidade é a parcela de membros sem duplicatas. A pontualidade é a rapidez com que as adesões aparecem no sistema. A exatidão exige comparação com a realidade, como pedir a uma amostra de membros que confirme seus endereços. Ela observa que a exatidão é a mais difícil e mais cara de medir, por isso costuma ser medida por amostragem. Ela sugere consultar uma amostra de cem membros por trimestre.

### 14.4 Dilemas

Melhorar uma dimensão pode prejudicar outra. Exigir o e-mail na adesão aumentaria a completude, mas poderia levar os funcionários a digitar endereços falsos, reduzindo a exatidão, ou desestimular as adesões. Amara recomenda pedir o e-mail oferecendo um benefício claro, como recibos digitais, em vez de torná-lo obrigatório. Ela aprende que as metas de qualidade devem considerar o comportamento, porque as pessoas reagem às regras de maneiras que podem minar o objetivo por trás delas. O dono dos dados de fidelidade concorda, e a opção de recibo digital aumenta a completude dos e-mails sem nenhum relato de endereços falsos nas lojas.

### Exemplo resolvido

Amara estuda as dimensões de qualidade a partir de Wang e Strong e de Batini, mapeia os usos dos dados de fidelidade às dimensões, define medidas e evita a obrigatoriedade do e-mail, que prejudicaria a exatidão.

> **Caso sintético.** As medidas são sintéticas; Wang e Strong (1996) e Batini et al. (2009) são reais.

### Erros e limites

Campos obrigatórios podem produzir valores falsos; considere o comportamento.

### Exercícios

- **EX040 — Base da pesquisa.** De que visão Wang e Strong partiram? *Rubrica:* 3 = a dos consumidores de dados;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX041 — Dimensão mais difícil.** Que dimensão é a mais difícil de medir? *Rubrica:* 3 = a exatidão;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX042 — Abordagem do e-mail.** Como a Harbourline deve incentivar o cadastro de e-mails? *Rubrica:* 3 = oferecendo um benefício claro, como recibos digitais;; 2 = correto;; 1 = obrigatoriedade;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Metadados e catálogos

### Objetivos de aprendizagem

Você vai (1) descrever os tipos de metadados; (2) montar entradas de catálogo simples; (3) explicar como os catálogos sustentam a governança.

### 15.1 Tipos de metadados

Metadados são dados sobre dados. Amara aprende três tipos. Os metadados de negócio explicam o significado, como a definição de membro ativo. Os metadados técnicos descrevem a estrutura, como os tipos de campo e os nomes das tabelas. Os metadados operacionais registram eventos, como a última carga de uma tabela. A Harbourline tem metadados técnicos espalhados em manuais de sistemas, quase nenhum metadado de negócio e metadados operacionais apenas nos registros dos sistemas, que poucas pessoas conseguem ler ou interpretar corretamente. Amara propõe reunir primeiro os metadados de negócio, porque são o tipo que mais falta na Harbourline.

### 15.2 Definindo os termos

Amara começa um glossário. Membro ativo é definido de um jeito pelo marketing, que conta quem fez uma compra em um ano, e de outro pelo financeiro, que conta quem fez uma compra em seis meses. Ela leva as duas definições ao grupo de governança, que acorda uma definição para os relatórios oficiais e permite que o marketing mantenha sua própria medida com outro nome. Ela aprende que os glossários trazem à tona divergências que antes causavam confusão em silêncio. O glossário chega a quarenta termos no primeiro ano, cada um com um dono que aprova sua definição.

### 15.3 Entradas de catálogo

Amara monta entradas de catálogo para os dez conjuntos de dados mais usados: nome, descrição, dono, curador, sistema de origem, frequência de atualização, classificação, medidas de qualidade e termos do glossário vinculados. No começo, ela usa uma tabela compartilhada simples. Os usuários passam a consultar as entradas antes de fazer perguntas à equipe de dados, o que reduz os pedidos repetidos. Ela observa que um catálogo não precisa começar com um software caro, desde que as entradas sejam mantidas e os donos assumam a responsabilidade por mantê-las corretas. Os pedidos à equipe de dados caem visivelmente em dois meses.

### 15.4 Os princípios FAIR

O Dr. Lindqvist apresenta os princípios FAIR de Wilkinson e colegas: os dados devem ser localizáveis, acessíveis, interoperáveis e reutilizáveis (*findable, accessible, interoperable, reusable*). Eles foram escritos para dados de pesquisa, mas também se aplicam aos dados das organizações. Amara relaciona localizável ao catálogo, acessível a procedimentos de acesso claros, interoperável a códigos compartilhados e reutilizável a boas descrições e licenças. Ela observa que FAIR não significa aberto a todos; dados pessoais podem ser localizáveis em um catálogo enquanto o acesso continua restrito. Amara acrescenta uma coluna FAIR à tabela do catálogo.

### Exemplo resolvido

Amara distingue metadados de negócio, técnicos e operacionais, resolve a disputa sobre a definição de membro ativo, monta dez entradas de catálogo em uma tabela compartilhada e relaciona os princípios FAIR à Harbourline.

> **Caso sintético.** As entradas são sintéticas; Wilkinson et al. (2016) é real.

### Erros e limites

FAIR não significa aberto; dados restritos ainda podem ser localizáveis.

### Exercícios

- **EX043 — Disputa sobre membro ativo.** Como o marketing e o financeiro definiam membro ativo? *Rubrica:* 3 = compra em um ano versus em seis meses;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX044 — Início do catálogo.** Que ferramenta Amara usou primeiro? *Rubrica:* 3 = uma tabela compartilhada simples;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX045 — Significado de FAIR.** O que significa FAIR? *Rubrica:* 3 = localizável, acessível, interoperável, reutilizável;; 2 = todos;; 1 = alguns;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Dados de referência e dados mestres

### Objetivos de aprendizagem

Você vai (1) distinguir dados de referência e dados mestres; (2) gerenciar listas de códigos; (3) tratar registros mestres duplicados.

### 16.1 Dois tipos de dados compartilhados

Dados de referência são listas de códigos usadas para classificar outros dados, como os códigos de loja, as categorias de produto e os códigos de país. Dados mestres descrevem as entidades centrais compartilhadas entre os sistemas, como membros, produtos e fornecedores. Amara observa que ambos são usados por muitos processos, de modo que os erros se espalham amplamente. O DAMA-DMBOK2 os trata como uma área de gestão própria. Na Harbourline, cada sistema mantém suas próprias cópias, e ninguém verifica se essas cópias continuam concordando entre si ao longo do tempo. Amara lista cada cópia e onde ela fica.

### 16.2 Listas de códigos

Amara descobre que a lista de lojas existe no sistema dos caixas, no sistema de fidelidade e no financeiro, com diferenças: uma loja fechada ainda ativa na fidelidade, uma loja nova ausente do financeiro e uma loja com dois códigos. Ela propõe uma única lista oficial, de propriedade da área de operações, com as mudanças aprovadas e distribuídas a todos os sistemas. Cada código tem data de início e de fim, para que os dados históricos continuem fazendo sentido depois que lojas abrem, fecham ou mudam de endereço. A área de operações aceita a titularidade e designa um curador para a lista.

### 16.3 Duplicatas nos dados mestres

Às vezes os membros se cadastram duas vezes, com cartões ou endereços de e-mail diferentes. As duplicatas dividem o histórico de compras e fazem as ofertas chegarem em dobro. Amara estuda os métodos de pareamento, desde comparações exatas até abordagens probabilísticas baseadas na teoria de ligação de registros de Fellegi e Sunter, que pondera a concordância em vários campos. Ela propõe uma regra de pareamento simples com nome, CEP e ano de nascimento, com os possíveis pares revisados por um curador antes da fusão, já que fusões erradas misturam dados de pessoas diferentes. O curador revisa toda semana uma fila de possíveis pares e registra cada decisão.

### 16.4 Registros de ouro

Depois do pareamento, a Harbourline precisa de uma única versão confiável de cada membro, às vezes chamada de registro de ouro (*golden record*). Amara propõe regras para escolher os valores quando as duplicatas discordam: o e-mail confirmado mais recentemente, o endereço da última entrega de compra e a data de adesão mais antiga. Cada regra é documentada e aprovada pelo dono dos dados de fidelidade. Ela observa que as regras de sobrevivência são decisões de governança, porque determinam quais fatos a organização vai tratar como verdadeiros. As regras são testadas em duplicatas sintéticas antes de serem aplicadas ao sistema de fidelidade em produção.

### Exemplo resolvido

Amara separa dados de referência e dados mestres, encontra três listas de lojas discordantes e propõe uma única lista com dono e datas, desenha um pareamento de membros revisado por um curador e documenta as regras de sobrevivência.

> **Caso sintético.** Os dados são sintéticos; o DAMA-DMBOK2 e Fellegi e Sunter (1969) são reais.

### Erros e limites

Fusões automáticas sem revisão podem juntar pessoas diferentes.

### Exercícios

- **EX046 — Problemas da lista de lojas.** Cite uma diferença entre as listas de lojas. *Rubrica:* 3 = loja fechada ainda ativa, loja nova ausente ou código duplicado;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.
- **EX047 — Salvaguarda da fusão.** Que salvaguarda se aplica antes da fusão? *Rubrica:* 3 = a revisão dos possíveis pares por um curador;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX048 — E-mail sobrevivente.** Que e-mail sobrevive? *Rubrica:* 3 = o confirmado mais recentemente;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Noções de arquitetura de dados

### Objetivos de aprendizagem

Você vai (1) descrever como os dados fluem entre os sistemas; (2) explicar *data warehouses* e *data lakes*; (3) ligar a arquitetura à governança.

### 17.1 Sistemas e fluxos

Amara mapeia a arquitetura da Harbourline: caixas, um sistema das lojas, fidelidade, produtos, financeiro, estoque e um *data warehouse* de relatórios. Toda noite os dados fluem dos sistemas operacionais para o *data warehouse*, onde os relatórios são construídos. Alguns fluxos são automatizados; outros dependem de funcionários exportando arquivos. Ela observa que as exportações manuais são os pontos onde os dados mais se perdem ou chegam atrasados, e as marca no mapa como candidatas à automação ou, pelo menos, a verificações de completude. O mapa é revisado com a TI, que confirma mais duas exportações manuais que ela não tinha visto.

### 17.2 Data warehouses e data lakes

Um *data warehouse* guarda dados limpos e estruturados, organizados para relatórios. Um *data lake* guarda dados brutos em muitos formatos para análise posterior. A Harbourline tem um *data warehouse* e estuda criar um *data lake* para os dados de cliques do site. Amara explica que *data lakes* sem governança viram pântanos: ninguém sabe o que os arquivos contêm nem se é possível confiar neles. Ela recomenda que qualquer *data lake* tenha entradas de catálogo, donos e regras de retenção desde o primeiro dia. O projeto do *data lake* aceita essas condições antes que qualquer dado de cliques seja carregado nele.

### 17.3 Linhagem

A linhagem descreve de onde os dados vêm e como se transformam. Amara rastreia o número semanal de vendas do conselho de volta, pelo *data warehouse*, até os caixas e o sistema das lojas. Ela encontra uma transformação que exclui as devoluções e que ninguém havia documentado. O financeiro supunha que as devoluções estavam incluídas. Ela registra a linhagem na entrada de catálogo do número. Ela explica que a linhagem ajuda as pessoas a confiar nos números e a encontrar a causa quando eles parecem errados. O financeiro e a equipe de relatórios concordam em identificar claramente, dali em diante, que o número exclui as devoluções.

### 17.4 Arquitetura e governança

Amara observa que as escolhas de arquitetura afetam a governança. *Data warehouses* centrais facilitam definições consistentes, mas podem tornar as equipes mais lentas. Abordagens distribuídas dão liberdade às equipes, mas dificultam a consistência. A Harbourline é pequena o bastante para um *data warehouse* central com donos claros. O Dr. Lindqvist explica que uma boa arquitetura torna fácil fazer a coisa certa, como aplicar classificações automaticamente, enquanto uma arquitetura ruim obriga as pessoas a lembrar de regras que os sistemas poderiam impor por elas. Amara recomenda a classificação automática no *data warehouse* como a primeira melhoria de arquitetura da Harbourline voltada à governança.

### Exemplo resolvido

Amara mapeia os sistemas e sinaliza as exportações manuais, adverte que *data lakes* sem governança viram pântanos, encontra pela linhagem uma exclusão de devoluções não documentada e liga as escolhas de arquitetura à governança.

> **Caso sintético.** A arquitetura é sintética.

### Erros e limites

*Data lakes* sem catálogo e sem donos se tornam inutilizáveis.

### Exercícios

- **EX049 — Fluxos frágeis.** Onde os dados mais se perdem? *Rubrica:* 3 = nas exportações manuais;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX050 — Constatação sobre devoluções.** O que a linhagem revelou? *Rubrica:* 3 = uma exclusão de devoluções não documentada;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX051 — Recomendação para o data lake.** O que qualquer *data lake* deve ter desde o primeiro dia? *Rubrica:* 3 = entradas de catálogo, donos e regras de retenção;; 2 = todos;; 1 = alguns;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Perfilamento de dados

### Objetivos de aprendizagem

Você vai (1) perfilar a completude de um conjunto de dados; (2) interpretar os resultados por campo e por linha; (3) transformar as constatações em ações.

### 18.1 O que é o perfilamento

Perfilar (*data profiling*) significa examinar os dados para entender seu conteúdo e sua qualidade antes de tomar decisões. Amara perfila o arquivo sintético de membros do programa de fidelidade, contando os valores ausentes em cada campo e quantos registros estão completos em todos os campos. Ela explica que o perfilamento costuma ser o primeiro passo de qualquer trabalho de qualidade, porque mostra onde estão os problemas e qual é seu tamanho, o que ajuda os donos a escolher prioridades com base em evidências, e não em reclamações. Amara explica cada passo do script de perfilamento à curadora dos dados de fidelidade, que vai executá-lo de novo mais tarde.

### Laboratório — Completude de cinco campos em 5.000 registros sintéticos de fidelidade

```python
"""Profile completeness of five fields in 5,000 synthetic loyalty records (stdlib only)."""
import random
random.seed(7)
miss = {"member_id": 0.0, "postcode": 0.06, "email": 0.18, "birth_year": 0.31, "store_code": 0.02}
rows = [{f: (None if random.random() < p else "x") for f, p in miss.items()} for _ in range(5000)]
for f in miss:
    print(f"{f:<11} complete {100*sum(r[f] is not None for r in rows)/len(rows):5.1f}%")
print(f"rows complete on all fields: {sum(all(v is not None for v in r.values()) for r in rows)}")
```

Execute com `python3 lab_profile.py`. Saída verificada:

```text
member_id   complete 100.0%
postcode    complete  93.9%
email       complete  82.3%
birth_year  complete  68.6%
store_code  complete  98.3%
rows complete on all fields: 2594
```

### 18.2 Resultados por campo

O laboratório perfila cinco mil registros. O identificador de membro está completo em todos os registros. O código de loja está completo em 98,3 por cento, o CEP em 93,9 por cento, o e-mail em 82,3 por cento e o ano de nascimento em apenas 68,6 por cento. Amara observa que o padrão faz sentido: os identificadores são gerados pelo sistema, enquanto o e-mail e o ano de nascimento dependem de os membros decidirem informá-los, e o ano de nascimento era opcional nos antigos formulários de adesão. O novo formulário mantém o ano de nascimento opcional, mas o pede com uma explicação curta sobre as ofertas ligadas à idade.

### 18.3 Resultados por linha

Apenas 2.594 dos 5.000 registros estão completos nos cinco campos, cerca de 51,9 por cento. Amara explica que a completude por linha é menor do que a de qualquer campo isolado, porque as lacunas caem em registros diferentes. Se uma campanha precisa de e-mail, CEP e ano de nascimento ao mesmo tempo, ela só alcança cerca de metade dos membros. Ela enfatiza que os números por campo, sozinhos, enganariam o marketing sobre quantos membros poderiam receber uma oferta direcionada. O marketing revê sua estimativa para a campanha e planeja o direcionamento com o número realista de membros alcançáveis.

### 18.4 Das constatações às ações

Amara discute os resultados com o dono dos dados de fidelidade. Eles concordam que o ano de nascimento só importa para as ofertas ligadas à idade e não precisa ser buscado para todos. O e-mail importa para os recibos digitais e as ofertas, então o aviso no caixa vai pedi-lo aos membros que não o têm. As lacunas de CEP vêm principalmente de um antigo canal de adesão, que será desativado. Ela registra cada ação com um dono e planeja repetir o perfilamento em três meses para medir a mudança. O dono dos dados de fidelidade aprova as ações no registro de governança.

### Exemplo resolvido

Amara perfila 5.000 registros e encontra o identificador de membro completo, o código de loja em 98,3, o CEP em 93,9, o e-mail em 82,3 e o ano de nascimento em 68,6 por cento, com 2.594 linhas completas em todos os campos, e acorda ações direcionadas.

> **Caso sintético.** Os registros são sintéticos; as saídas vêm de lab_profile.py.

### Erros e limites

A completude por campo superestima as linhas utilizáveis; informe também a completude por linha.

### Exercícios

- **EX052 — Campo mais baixo.** Que campo é o menos completo? *Rubrica:* 3 = o ano de nascimento, com 68,6%;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX053 — Linhas completas.** Quantos registros estão completos em todos os campos? *Rubrica:* 3 = 2.594;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX054 — Ação sobre o ano de nascimento.** O que foi decidido sobre o ano de nascimento? *Rubrica:* 3 = não buscá-lo para todos, pois só é necessário para as ofertas por idade;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Regras de qualidade de dados

### Objetivos de aprendizagem

Você vai (1) escrever regras de qualidade a partir dos padrões; (2) automatizar as verificações; (3) definir limiares e escalonamento.

### 19.1 Regras a partir dos padrões

Amara transforma o padrão dos dados de fidelidade em regras. Cada regra tem um identificador, uma descrição, o campo que verifica, a condição, o dono e o limiar. Por exemplo, a regra LQ-03 verifica se os endereços de e-mail contêm uma arroba e um domínio, tem como dona a curadora dos dados de fidelidade e uma meta de 99 por cento de validade entre os registros com e-mail. Escrever as regras assim as torna testáveis, repetíveis e rastreáveis até o padrão aprovado pelo grupo de governança. O catálogo de regras fica guardado junto com o padrão.

### 19.2 Automatizando as verificações

Ela implementa as regras em um script Python que roda toda noite depois da carga dos dados de fidelidade. Os resultados vão para uma pequena tabela com data, regra, registros verificados e registros com falha. Um gráfico simples mostra as tendências. Amara explica que as verificações automatizadas capturam os problemas logo depois que aparecem, enquanto as manuais acontecem raramente demais e dependem de alguém se lembrar. O script registra as próprias execuções, de modo que uma noite sem execução é percebida, e não pulada em silêncio. A curadora recebe toda manhã um resumo curto dos resultados por e-mail.

### 19.3 Limiares e escalonamento

Cada regra tem um limiar. Se os resultados ficam abaixo dele, a curadora recebe um alerta. Se continuam abaixo por uma semana, o dono é informado. Se continuam abaixo por um mês, o grupo de governança revisa o problema. Amara observa que o escalonamento transforma medições em ação, e que passos claros evitam tanto ignorar os problemas quanto reagir em excesso a noites ruins isoladas, causadas por falhas temporárias de sistema que estão fora do controle de qualquer pessoa. Amara documenta os passos de escalonamento no padrão, para que todos os curadores sigam o mesmo processo.

### 19.4 Mantendo as regras

As regras precisam de manutenção. Quando a Harbourline abre uma loja em uma nova região com outro formato de código postal, a regra do CEP passa a rejeitar indevidamente códigos válidos. Amara atualiza a regra depois que a curadora relata os alertas falsos, registra a mudança e processa de novo os resultados anteriores. Ela aprende que as regras precisam mudar quando o negócio muda, e que toda mudança de regra deve ser revisada e documentada como qualquer outra mudança em um sistema importante. O registro de mudanças mostra quem aprovou a atualização, quando ela foi aplicada e por que era necessária.

### Exemplo resolvido

Amara escreve regras com identificadores, donos e limiares, automatiza as verificações noturnas com execuções registradas, define um escalonamento em três passos e atualiza a regra do CEP para uma nova região.

> **Caso sintético.** As regras são sintéticas.

### Erros e limites

Regras que nunca mudam acabam rejeitando dados válidos.

### Exercícios

- **EX055 — Regra LQ-03.** O que a regra LQ-03 verifica? *Rubrica:* 3 = que os e-mails contêm uma arroba e um domínio;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX056 — Violação de um mês.** Quem revisa os problemas que ficam abaixo do limiar por um mês? *Rubrica:* 3 = o grupo de governança;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX057 — Mudança do CEP.** Por que a regra do CEP mudou? *Rubrica:* 3 = uma nova região usava outro formato;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Gestão de problemas

### Objetivos de aprendizagem

Você vai (1) registrar e acompanhar problemas de dados; (2) encontrar as causas-raiz; (3) encerrar os problemas com evidências.

### 20.1 Registrando os problemas

Os problemas de dados na Harbourline costumavam ser relatados por e-mail e esquecidos. Amara cria um registro de problemas com campos para descrição, quem relatou, data, dados afetados, impacto, dono, situação e solução. Qualquer pessoa pode relatar problemas por meio de um formulário simples. Os curadores fazem a triagem dos problemas novos toda semana, atribuindo prioridade conforme o impacto. Ela observa que um registro torna os problemas visíveis e contáveis, o que permite ao grupo de governança ver padrões e julgar se a situação está melhorando. O registro fica visível para todos os funcionários na intranet.

### 20.2 Causas-raiz

Amara pratica a análise de causa-raiz em um problema em que faltavam pontos de fidelidade em algumas compras. Perguntando por que repetidas vezes, ela descobre que os pontos falhavam quando os caixas estavam sem conexão, que as transações feitas sem conexão eram enviadas depois sem os dados do cartão e que o software do caixa tinha uma configuração conhecida para manter os dados do cartão, que estava desligada. Ligar a configuração corrige a causa. Corrigir os pontos à mão teria tratado apenas o sintoma. O fornecedor dos caixas confirma a configuração e a aplica a todas as lojas em uma semana.

### 20.3 Encerrando os problemas

Os problemas só são encerrados com evidência de que a correção funcionou. Para o problema dos pontos, Amara verifica se as compras sem conexão das duas semanas seguintes receberam pontos. Ela registra a evidência no registro de problemas. Ela também pede à curadora que confirme com quem relatou que o problema foi resolvido. Ela explica que encerrar problemas com base na promessa de uma correção, sem verificar, faz os problemas voltarem sem que ninguém perceba e mina a confiança no processo. Amara acrescenta ao registro uma lista de verificação de encerramento, para que os curadores sigam os mesmos passos.

### 20.4 Aprendendo com o registro

Depois de seis meses, Amara analisa o registro. A maioria dos problemas diz respeito a códigos de loja e a membros duplicados, e muitos vêm de processos manuais. Ela apresenta esses padrões ao grupo de governança, que financia a automação de uma exportação manual e o trabalho de pareamento de duplicatas. O Dr. Lindqvist observa que um registro de problemas não é só uma lista de tarefas, mas uma fonte de evidências para as prioridades e as decisões de investimento da governança. Amara repete a análise a cada seis meses, e a parcela de problemas vindos de processos manuais cai depois da primeira automação.

### Exemplo resolvido

Amara cria um registro de problemas com triagem semanal, rastreia os pontos ausentes até uma configuração do caixa, encerra os problemas apenas com evidências e analisa seis meses de problemas para orientar os investimentos.

> **Caso sintético.** Os problemas são sintéticos.

### Erros e limites

Encerrar problemas sem verificar as correções deixa os problemas voltarem.

### Exercícios

- **EX058 — Causa dos pontos.** O que causou a falta de pontos de fidelidade? *Rubrica:* 3 = uma configuração do caixa para manter os dados do cartão sem conexão estava desligada;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX059 — Evidência de encerramento.** Que evidência encerrou o problema dos pontos? *Rubrica:* 3 = as compras sem conexão de duas semanas receberam pontos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX060 — Padrões do registro.** A que a maioria dos problemas do registro se referia? *Rubrica:* 3 = códigos de loja e membros duplicados;; 2 = ambos;; 1 = um;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060 (as de EX061–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Amara Okafor, o Dr. Paul Lindqvist, a Universidade Ridgeway, a Harbourline Co-operative e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Harbourline Co-operative, uma cooperativa de supermercados fictícia.

**EX002.** Chegou a membros que haviam recusado ser contatados.

**EX003.** Aprender a julgar evidências.

**EX004.** Saber que as vendas de leite sobem antes dos feriados e encomendar mais.

**EX005.** Um incluía impostos e o outro não.

**EX006.** Os contratos com fornecedores.

**EX007.** Cinco.

**EX008.** Para a fila andar quando um código de barras falha.

**EX009.** A conveniência local e as necessidades mais amplas da cooperativa.

**EX010.** Um intervalo de fórmula terminava uma linha antes do fim.

**EX011.** O total do resumo com o total do relatório de origem.

**EX012.** O resumo semanal de vendas do conselho.

**EX013.** A tabela de membros.

**EX014.** Uma loja aparecendo como várias nos relatórios agrupados.

**EX015.** A escrita de consultas, que ficam mais complexas.

**EX016.** Os nomes com acentos apareceram embaralhados.

**EX017.** Entre 1910 e 2010.

**EX018.** O que foi verificado, quanto falhou, por que importa, o que vem a seguir.

**EX019.** A mediana.

**EX020.** Elas superestimam a taxa de erros.

**EX021.** Os membros podem ser clientes habituais que aderiram, e não pessoas mudadas pelo programa.

**EX022.** Cerca de um em cada cinco registros de fidelidade não tem endereço de e-mail.

**EX023.** Ela começou o eixo do zero e acrescentou a contagem de membros.

**EX024.** Parcela de registros com endereço de e-mail.

**EX025.** Consentimento.

**EX026.** Não havia registro central, então alguns pedidos ficaram sem resposta.

**EX027.** Os dados de fornecedores e de lotes.

**EX028.** Oferecer descontos aos membros que escolhem o interesse família.

**EX029.** Oferecer os mesmos descontos por meio de cupons impressos.

**EX030.** Cedo, antes de as campanhas serem desenhadas.

**EX031.** Decidir quem decide o quê sobre os dados e garantir que isso seja cumprido.

**EX032.** Princípios, qualidade, metadados, acesso e ciclo de vida.

**EX033.** Pela TI, a pedido, sem aprovação de um dono.

**EX034.** O diretor de marketing.

**EX035.** A responsabilização, embora as tarefas possam ser delegadas.

**EX036.** Nomear curadores sem reservar tempo para eles.

**EX037.** Todo registro de fidelidade deve ter um código de loja válido.

**EX038.** Duas páginas.

**EX039.** Quando estão sem revisão há dois anos.

**EX040.** Os consumidores de dados.

**EX041.** A exatidão.

**EX042.** Oferecendo um benefício, como os recibos digitais.

**EX043.** O marketing usava um ano, e o financeiro, seis meses.

**EX044.** Uma tabela compartilhada simples.

**EX045.** Localizável, acessível, interoperável e reutilizável.

**EX046.** Uma loja fechada ainda ativa na fidelidade.

**EX047.** Um curador revisa os possíveis pares.

**EX048.** O e-mail confirmado mais recentemente.

**EX049.** Nas exportações manuais.

**EX050.** Uma transformação que excluía as devoluções em silêncio.

**EX051.** Entradas de catálogo, donos e regras de retenção.

**EX052.** O ano de nascimento, com 68,6 por cento.

**EX053.** 2.594 de 5.000.

**EX054.** Não é buscado de modo geral, pois só importa para as ofertas ligadas à idade.

**EX055.** Que os endereços de e-mail contenham uma arroba e um domínio.

**EX056.** O grupo de governança.

**EX057.** Uma loja em uma nova região usava outro formato de código postal.

**EX058.** Uma configuração do caixa que mantém os dados do cartão sem conexão estava desligada.

**EX059.** As compras sem conexão das duas semanas seguintes receberam pontos.

**EX060.** Códigos de loja e membros duplicados.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. *ACM Computing Surveys, 41*(3), 1–52. https://doi.org/10.1145/1541880.1541883
- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Fellegi, I. P., & Sunter, A. B. (1969). A theory for record linkage. *Journal of the American Statistical Association, 64*(328), 1183–1210. https://doi.org/10.1080/01621459.1969.10501049
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-188
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- Khatri, V., & Brown, C. V. (2010). Designing data governance. *Communications of the ACM, 53*(1), 148–152. https://doi.org/10.1145/1629175.1629210
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0*. https://doi.org/10.6028/NIST.CSWP.10
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., et al. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. https://doi.org/10.1038/sdata.2016.18
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
