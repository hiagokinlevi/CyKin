# Segurança da Informação: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 117, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–50 de 50 têm texto didático escrito à mão; os exercícios EX001–EX150 têm resoluções correspondentes com rubricas de 0 a 3; os quatro laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de engenharia que aprendem a construir, verificar e operar controles de segurança da informação para uma empresa de logística.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios conciliam um inventário sintético de ativos com uma varredura sintética de descoberta, conferem configurações sintéticas de servidores contra três regras de linha de base, detectam rajadas de adivinhação de senhas num log sintético de autenticação e verificam restaurações sintéticas de backup contra somas de verificação SHA-256. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de engenharia desde os fundamentos de matemática, física, programação e sistemas, passando por requisitos de segurança, modelos, ameaças, controles, implementação, verificação, operações e validação, até um projeto final, uma revisão independente, um teste de recuperação, um dossiê de evidências, um trabalho de conclusão e uma defesa final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Lindiwe Dube** | Estudante de engenharia | Inventada |
| **Prof. Marcus Hale** | Orientador | Inventado |
| **Brightwater Polytechnic** | Escola politécnica fictícia | Inventada |
| **Saltmarsh Logistics** | Empresa de logística fictícia, com cerca de 1.800 funcionários, doze depósitos e 2.400 endereços de rede registrados | Inventada |

### Fontes principais

Anderson (2020), [doi:10.1002/9781119644682](https://doi.org/10.1002/9781119644682); ISO/IEC 27000:2026; ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); ISO/IEC 27002:2022; NIST SP 800-53 Rev. 5; NIST SP 800-30 Rev. 1; FIPS 199, [doi:10.6028/NIST.FIPS.199](https://doi.org/10.6028/NIST.FIPS.199); NIST CSWP 29 (CSF 2.0); NIST SP 800-12 Rev. 1; Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) usar taxas de variação para descrever volumes de eventos de segurança; (2) relacionar derivadas ao monitoramento de logs; (3) estimar o armazenamento de logs com uma integral.

### 1.1 A estudante e a empresa

Lindiwe Dube começa um curso de engenharia de cinco anos na fictícia Brightwater Polytechnic, sob orientação do Prof. Marcus Hale. Sua parceira de estágio é a fictícia Saltmarsh Logistics, que emprega cerca de 1.800 pessoas em doze depósitos e opera aproximadamente 2.400 dispositivos em rede, entre eles 300 servidores. Segurança da informação, na Saltmarsh, significa proteger a confidencialidade, a integridade e a disponibilidade dos dados de remessas, de clientes e da folha de pagamento. O Prof. Hale explica que cada disciplina de matemática vai se ligar a uma decisão de segurança real na Saltmarsh, de modo que a teoria seja sempre testada contra um sistema em funcionamento. Ela começa em setembro.

### 1.2 Taxas de variação

O cálculo começa pelas taxas. Se o número de eventos de log de segurança armazenados é uma função do tempo, sua derivada diz à Saltmarsh com que rapidez cresce o armazenamento de logs. Lindiwe estima que servidores, firewalls e notebooks juntos produzem cerca de quarenta milhões de eventos por dia, a uma taxa constante. Quando a Saltmarsh abre um novo depósito, a própria taxa aumenta, então a segunda derivada se torna positiva. Ela aprende que o planejamento da retenção de logs precisa usar a taxa de crescimento, porque um plano baseado apenas no total de hoje vai ficar sem espaço antes do previsto.

### 1.3 Monitoramento com derivadas

Lindiwe aplica a ideia ao monitoramento. Uma queda súbita na taxa de eventos que chegam de um depósito, uma derivada negativa grande, pode significar que um encaminhador de logs parou, e não que o depósito ficou mais tranquilo. Os atacantes às vezes desativam o registro de logs de propósito, então uma fonte silenciosa é ela mesma um sinal de segurança. Ela propõe calcular as taxas de eventos por hora para cada fonte e emitir alertas quando uma taxa cair bruscamente. O Prof. Hale observa que isso transforma uma ideia matemática num controle de detecção para evidências ausentes. A equipe do depósito concorda.

### 1.4 Planejando o armazenamento

A política da Saltmarsh mantém os logs de segurança por um ano on-line e por mais tempo em arquivo. Lindiwe integra a taxa de eventos ao longo de um ano, prevendo dois novos depósitos, e descobre que o total cresce mais rápido do que um simples múltiplo do volume de hoje. O Prof. Hale pede que ela compare a retenção completa com a manutenção apenas de eventos resumidos de autenticação e de firewall depois de noventa dias. A integral mostra grandes economias, mas ela observa que os resumos podem remover detalhes de que um investigador vai precisar depois, então a retenção é ao mesmo tempo uma decisão de custo e de evidência.

### Exemplo resolvido

Lindiwe modela o crescimento dos logs como uma taxa, usa quedas súbitas da taxa para detectar fontes silenciosas e integra ao longo de um ano para comparar a retenção completa com a resumida.

> **Caso sintético.** A Brightwater, a Saltmarsh e todas as pessoas são sintéticas.

### Erros e limites

Tratar uma fonte de logs silenciosa como segura pode esconder um encaminhador desativado.

### Exercícios

- **EX001 — Eventos diários.** Aproximadamente quantos eventos chegam por dia? *Rubrica:* 3 = cerca de quarenta milhões;; 2 = próximo;; 1 = errado;; 0 = nenhuma.

- **EX002 — Fonte silenciosa.** O que pode significar uma queda súbita na taxa de eventos de uma fonte? *Rubrica:* 3 = um encaminhador parado;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX003 — Risco do resumo.** Qual é o risco de resumir logs antigos? *Rubrica:* 3 = perder detalhes de que os investigadores precisam;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 50)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) usar conjuntos para descrever direitos de acesso; (2) modelar confiança e dependências como grafos; (3) expressar regras de segurança em lógica.

### 2.1 Conjuntos de usuários e direitos

Lindiwe descreve o acesso na Saltmarsh como conjuntos: funcionários, contas, grupos e permissões. O conjunto das contas com acesso à folha de pagamento deve ser um subconjunto do grupo de finanças. A diferença de conjuntos torna as violações visíveis: as contas com acesso à folha de pagamento menos os funcionários de finanças deve ser vazio. Se não for, alguém tem direitos fora da sua função. Ela escreve essas condições como regras que podem ser conferidas automaticamente, observando que a notação de conjuntos torna uma política de segurança precisa o bastante para ser testada, e não apenas discutida. Ela executa a verificação sobre uma exportação sintética do diretório e encontra quatro contas desse tipo.

### 2.2 Relações e funções

Uma relação liga contas a pessoas. Lindiwe confere se ela é uma função: cada conta nominal deve pertencer a exatamente uma pessoa. As contas compartilhadas quebram isso, porque as ações não podem ser rastreadas até um indivíduo. Num diretório sintético, ela encontra várias contas de terminais do armazém usadas por turnos inteiros. Ela explica que a responsabilização, uma propriedade central de segurança, depende de esse mapeamento ser uma função, e que as contas de serviço precisam de um dono nomeado, mesmo que nenhuma pessoa faça login com elas. Cada conta de turno é listada.

### 2.3 Grafos de confiança

Lindiwe modela os sistemas da Saltmarsh como um grafo direcionado, com uma aresta onde um sistema confia em outro, por exemplo um servidor de arquivos que aceita logins do diretório. A alcançabilidade mostra o que um atacante poderia alcançar depois de comprometer um nó. Um notebook de depósito comprometido que alcança o diretório pode potencialmente alcançar quase tudo. Ela aprende que a análise de grafos fundamenta o raciocínio sobre caminhos de ataque, e que remover algumas arestas, como uma confiança administrativa desnecessária, pode cortar muitos caminhos de uma vez. Ela desenha o grafo de vinte sistemas centrais.

### 2.4 Lógica para regras

As regras de segurança podem ser declaradas em lógica. Lindiwe escreve: para toda conta, se a conta é privilegiada, então a autenticação multifator está ativada. Ela confere a contrapositiva: qualquer conta sem autenticação multifator não pode ser privilegiada. O Prof. Hale mostra como declarações precisas evitam discussões entre equipes sobre expressões vagas como os administradores devem ser protegidos. Ela aprende que escrever primeiro as regras de forma formal torna as verificações em código e as evidências de auditoria coerentes com a redação da política. Ela lista cinco contas privilegiadas que violam a regra no diretório sintético, e a equipe de identidade concorda em cadastrar cada uma antes da próxima auditoria.

### Exemplo resolvido

Lindiwe usa a diferença de conjuntos para encontrar acessos à folha de pagamento fora da função, confere o mapeamento de contas para pessoas, modela a confiança como um grafo e escreve em lógica uma regra de MFA.

> **Caso sintético.** O diretório é sintético.

### Erros e limites

Uma regra formal ainda pode codificar a política errada; confirme-a com os donos.

### Exercícios

- **EX004 — Diferença vazia.** Que diferença de conjuntos deve ser vazia? *Rubrica:* 3 = contas com acesso à folha de pagamento menos funcionários de finanças;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX005 — Contas compartilhadas.** Por que as contas compartilhadas prejudicam a responsabilização? *Rubrica:* 3 = as ações não podem ser rastreadas até uma pessoa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX006 — Cortando caminhos.** Como muitos caminhos de ataque podem ser cortados de uma vez? *Rubrica:* 3 = remover algumas arestas de confiança;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 50)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar propriedades físicas à segurança; (2) explicar canais laterais e remanência de mídia; (3) considerar ameaças ambientais à disponibilidade.

### 3.1 Física e informação

Os computadores armazenam e transportam informação como estados físicos: cargas, domínios magnéticos e sinais em fios ou no ar. Lindiwe aprende que as propriedades físicas criam efeitos de segurança. Os sinais sem fio de um ponto de acesso de depósito vazam para além do prédio, então um atacante no estacionamento pode recebê-los. A cifração protege a confidencialidade onde a física não consegue. Ela observa que o projeto de segurança deve partir do que fisicamente chega a um adversário, e não de onde o diagrama de rede desenha sua fronteira. Ela mede a intensidade do sinal na cerca do depósito com um aplicativo simples de celular.

### 3.2 Canais laterais

Os dispositivos emitem informação por meio do consumo de energia, do tempo, do som e da radiação eletromagnética. Uma operação criptográfica que demora um pouco mais para algumas chaves pode revelar essas chaves a um observador cuidadoso. Lindiwe lê como esses canais laterais foram explorados em pesquisas e por que as implementações de tempo constante importam. Na Saltmarsh, a lição prática é mais estreita: usar bibliotecas criptográficas bem revisadas em vez de código caseiro, já que os autores das bibliotecas tratam de comportamentos de tempo que os desenvolvedores de aplicações raramente consideram. Lindiwe confere quais bibliotecas os serviços de pagamento e de login da Saltmarsh usam e confirma que ambos dependem de implementações amplamente revisadas, mantidas por grandes comunidades.

### 3.3 Remanência e descarte

Os dados persistem fisicamente depois da exclusão. Nos discos magnéticos, os arquivos excluídos permanecem até serem sobrescritos; nas unidades de estado sólido, o nivelamento de desgaste pode manter cópias antigas em blocos que o sistema operacional não consegue endereçar. A Saltmarsh desativa cerca de cem notebooks por ano. Lindiwe recomenda a cifração de disco completo desde o início, para que destruir a chave torne ilegíveis os dados restantes, além da destruição certificada das unidades que guardaram dados da folha de pagamento. Ela aprende que o descarte é um problema de física tanto quanto de política. Os certificados do fornecedor de descarte agora são arquivados com o registro de cada ativo.

### 3.4 Ambiente e disponibilidade

O calor, a energia e a água ameaçam a disponibilidade. Uma sala de servidores acima da temperatura de projeto reduz o desempenho dos processadores e encurta a vida dos componentes; uma queda de energia sem backup impede os depósitos de faturar. Lindiwe inspeciona a sala de servidores principal da Saltmarsh e encontra uma refrigeração adequada, mas um nobreak dimensionado anos atrás para menos servidores. Ela calcula que sua autonomia com a carga atual é de menos de dez minutos. O Prof. Hale observa que as falhas de disponibilidade muitas vezes começam com uma física que ninguém conferiu de novo. O gerente de instalações encomenda uma unidade maior depois de ler o cálculo, e Lindiwe acrescenta uma verificação anual de carga ao calendário de manutenção.

### Exemplo resolvido

Lindiwe liga o vazamento de rádio, os canais laterais, a remanência e a capacidade de energia a controles de segurança na Saltmarsh, recomendando cifração, bibliotecas revisadas e uma revisão do nobreak.

> **Caso sintético.** As medições são sintéticas.

### Erros e limites

Excluir arquivos não remove os dados da mídia de armazenamento.

### Exercícios

- **EX007 — Vazamento de rádio.** Por que a cifração importa para o sem fio dos depósitos? *Rubrica:* 3 = os sinais chegam além do prédio;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX008 — Remanência em SSD.** Por que dados excluídos podem sobreviver em unidades de estado sólido? *Rubrica:* 3 = o nivelamento de desgaste mantém cópias antigas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX009 — Autonomia do nobreak.** Que autonomia o nobreak dá com a carga atual? *Rubrica:* 3 = menos de dez minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 50)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever Python simples para processar dados de segurança; (2) validar entradas não confiáveis; (3) tratar erros sem escondê-los.

### 4.1 Primeiros scripts

Lindiwe escreve seus primeiros scripts em Python sobre dados sintéticos da Saltmarsh. Um deles lê uma lista de contas de usuário e conta as que não têm login há noventa dias, candidatas à desativação. Ela usa apenas a biblioteca padrão, para que o script rode na máquina de qualquer analista sem instalar pacotes. O Prof. Hale pede que ela imprima as contagens com rótulos claros, porque um relatório de segurança que diz apenas 37, sem contexto, será mal entendido pelos gerentes que o recebem. O script encontra trinta e sete contas inativas no arquivo sintético.

### 4.2 Entradas não confiáveis

As entradas vindas de fora de um programa não podem ser confiáveis. Lindiwe escreve uma função que aceita um código de depósito digitado por um usuário e o confere contra os doze códigos válidos antes de usá-lo num caminho de arquivo. Sem essa verificação, uma entrada com sequências de ponto-ponto-barra poderia fazer o programa ler arquivos fora da sua pasta. Ela aprende que validar a entrada contra uma lista de permissões, em vez de tentar bloquear padrões ruins conhecidos, é o padrão mais seguro. Ela testa a função com dez códigos deliberadamente malformados.

### 4.3 Erros e logs

Os programas falham, e a forma como falham importa. O primeiro script de Lindiwe parava silenciosamente quando uma linha do arquivo de contas estava malformada. Ela o reescreve para registrar o número da linha e o motivo, pular a linha ruim e relatar ao final a contagem de linhas puladas. O Prof. Hale explica que as falhas silenciosas são perigosas nas ferramentas de segurança, porque uma varredura que pula em silêncio metade dos seus alvos ainda produz um relatório tranquilizador. No arquivo sintético, a nova versão pula três linhas malformadas e as relata pelo número, para que o dono dos dados possa corrigir os registros de origem.

### 4.4 Lendo código com olhar crítico

Lindiwe lê um script curto que um colega escreveu para redefinir senhas. Ele monta um comando de shell juntando strings que incluem o nome de usuário. Ela percebe que um nome de usuário contendo um ponto e vírgula poderia injetar um segundo comando. Ela sugere passar os argumentos como uma lista ao módulo subprocess, para que nenhum shell os interprete. O Prof. Hale diz que revisar o código dos outros em busca desses padrões é um dos hábitos mais valiosos que um engenheiro pode construir cedo. O colega concorda, atualiza o script e pede que ela revise o próximo.

### Exemplo resolvido

Lindiwe escreve scripts com a biblioteca padrão e saída rotulada, valida os códigos de depósito contra uma lista de permissões, registra as linhas puladas e identifica um risco de injeção de comandos.

> **Caso sintético.** Os scripts e os dados são sintéticos.

### Erros e limites

Bloquear entradas ruins conhecidas é mais fraco do que permitir apenas entradas boas conhecidas.

### Exercícios

- **EX010 — Contas inativas.** O que o primeiro script conta? *Rubrica:* 3 = contas sem login há noventa dias;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX011 — Lista de permissões.** Como o código de depósito é validado? *Rubrica:* 3 = contra os doze códigos válidos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX012 — Correção da injeção.** Como o script de redefinição deve chamar os comandos? *Rubrica:* 3 = passar os argumentos como uma lista;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 50)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever achados de segurança claros; (2) apresentar o risco a não especialistas; (3) documentar as decisões para leitores futuros.

### 5.1 Escrevendo achados

A primeira tarefa de Lindiwe no estágio é redigir um achado: um compartilhamento de arquivos legível por todos os funcionários contém carteiras de motorista digitalizadas. O Prof. Hale mostra uma estrutura: o que foi encontrado, onde, por que importa, qual a probabilidade de uso indevido e o que fazer. Ela evita jargões como legível por todos no resumo e escreve que qualquer funcionário pode abrir a pasta. O achado é curto, específico e dá ao dono uma próxima ação clara. O dono da pasta, um administrador de depósito, move as digitalizações para um compartilhamento restrito na mesma tarde.

### 5.2 Apresentando o risco

Lindiwe apresenta três achados aos gerentes dos depósitos. Em vez de pontuações, ela descreve consequências plausíveis: a digitalização roubada de uma carteira poderia sustentar uma fraude de identidade contra um motorista. Os gerentes perguntam que achado corrigir primeiro. Ela explica a probabilidade e o impacto em termos simples e recomenda começar pela pasta das carteiras, porque a exposição é ampla e a correção é rápida. Ela aprende que a comunicação de riscos tem sucesso quando os ouvintes podem agir imediatamente. Dois gerentes pedem a mesma apresentação para seus supervisores, e Lindiwe a reduz a uma única página com os três achados e seus donos.

### 5.3 Diagramas

Lindiwe desenha um diagrama de rede simples para a apresentação, mostrando os depósitos, a sede e o serviço de e-mail em nuvem. O Prof. Hale pede que ela marque as fronteiras de confiança, onde os dados passam de uma zona de controle para outra, porque é ali que os controles devem ficar. Ela remove os ícones decorativos e rotula cada seta com os dados que ela transporta. O diagrama se torna uma ferramenta de discussão, e não uma figura, e os leitores futuros podem atualizá-lo. Ela guarda o diagrama junto com a documentação de rede atual.

### 5.4 Registros de decisão

As decisões se apagam da memória. Lindiwe escreve um breve registro de decisão para a pasta das carteiras: contexto, opções consideradas, decisão, dono e data. Meses depois, um auditor pergunta por que a pasta foi movida em vez de excluída, e o registro responde de imediato: as carteiras dos motoristas precisam ser retidas para verificações do seguro. Ela aprende que registrar os motivos protege uma organização de repetir debates e ajuda os auditores a ver que os riscos foram tratados de forma deliberada. A Saltmarsh adota o modelo dela para todas as decisões de segurança, e os registros ficam numa pasta compartilhada com o nome do dono em cada um, o que torna as auditorias posteriores mais rápidas.

### Exemplo resolvido

Lindiwe escreve um achado estruturado sobre as digitalizações expostas de carteiras, o apresenta pelas consequências, desenha um diagrama com fronteiras de confiança e registra a decisão.

> **Caso sintético.** Os achados são sintéticos.

### Erros e limites

Um achado sem dono e sem ação claros raramente é corrigido.

### Exercícios

- **EX013 — Estrutura do achado.** Cite as partes de um achado. *Rubrica:* 3 = o quê, onde, por quê, probabilidade, ação;; 2 = a maioria;; 1 = poucas;; 0 = nenhuma.

- **EX014 — Fronteiras de confiança.** O que o Prof. Hale pede que ela marque? *Rubrica:* 3 = fronteiras de confiança;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX015 — Resposta do registro.** Por que a pasta foi movida em vez de excluída? *Rubrica:* 3 = as carteiras são retidas para verificações do seguro;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 50)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) modelar crescimento e decaimento em processos de segurança; (2) usar modelos exponenciais para o acúmulo de vulnerabilidades; (3) interpretar a meia-vida da exposição.

### 6.1 Decaimento exponencial

Muitos processos de segurança decaem de forma aproximadamente exponencial. Se a Saltmarsh corrige uma fração fixa das vulnerabilidades abertas a cada semana, o acúmulo cai na mesma proporção toda semana. Lindiwe ajusta esse modelo a dados sintéticos: cerca de quinze por cento dos achados abertos são fechados por semana. Resolver a equação diferencial dá uma curva que ela pode comparar com as metas. O Prof. Hale observa que o modelo é simples, mas útil para perguntar se uma meta é alcançável com o esforço atual. Lindiwe traça a curva ajustada contra doze semanas de dados sintéticos de fechamento.

### 6.2 Meia-vida da exposição

A partir da taxa de decaimento, Lindiwe calcula uma meia-vida: o tempo para que metade de um conjunto de vulnerabilidades novas seja corrigida. A quinze por cento por semana, a meia-vida é de pouco mais de quatro semanas. As vulnerabilidades críticas exploradas ativamente precisam de um fechamento muito mais rápido. Ela conclui que uma única taxa semanal esconde diferenças importantes e que a Saltmarsh deve acompanhar taxas separadas por gravidade, já que uma média confortável para achados baixos pode ser perigosa para os críticos. Ela propõe painéis separados para cada gravidade.

### 6.3 Entrada e acúmulo

O acúmulo também cresce à medida que novas vulnerabilidades são divulgadas. Lindiwe escreve uma equação diferencial com entrada constante e fechamento proporcional. Seu estado estacionário é igual à entrada dividida pela taxa de fechamento. Com cerca de sessenta achados novos por semana, o acúmulo se estabiliza perto de quatrocentos. Para reduzi-lo à metade, a Saltmarsh precisa dobrar a taxa de fechamento ou reduzir a entrada à metade, por exemplo removendo software sem uso. Ela aprende que reduzir o que está instalado pode ser tão eficaz quanto trabalhar mais rápido. Ela lista onze aplicativos sem uso que poderiam ser removidos.

### 6.4 Limites do modelo

Os fechamentos reais são irregulares: os dias de correção fecham muitos de uma vez e os sistemas difíceis se arrastam. Lindiwe compara o modelo suave com dados semanais sintéticos e vê grandes desvios em torno das liberações mensais de correções. O Prof. Hale explica que os modelos orientam o raciocínio, mas precisam ser conferidos contra as observações, e que um engenheiro deve declarar os pressupostos ao lado de qualquer projeção. Ela acrescenta ao relatório uma frase observando que o modelo ignora os sistemas que não podem ser corrigidos sem o suporte do fornecedor. Ela mostra os desvios num gráfico no relatório.

### Exemplo resolvido

Lindiwe modela o fechamento de vulnerabilidades como decaimento exponencial, calcula uma meia-vida de quatro semanas, deriva um acúmulo estacionário perto de quatrocentos e anota os limites do modelo.

> **Caso sintético.** As taxas são sintéticas.

### Erros e limites

Uma única taxa média de fechamento esconde o tratamento lento dos achados críticos.

### Exercícios

- **EX016 — Meia-vida.** Qual é a meia-vida com fechamento semanal de quinze por cento? *Rubrica:* 3 = pouco mais de quatro semanas;; 2 = próximo;; 1 = errado;; 0 = nenhuma.

- **EX017 — Estado estacionário.** Qual é a fórmula do acúmulo estacionário? *Rubrica:* 3 = entrada dividida pela taxa de fechamento;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX018 — Reduzir a entrada.** Como a entrada pode ser reduzida? *Rubrica:* 3 = remover software sem uso;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 50)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar taxas a partir de dados de segurança; (2) raciocinar sobre taxas-base nos alertas; (3) quantificar a incerteza.

### 7.1 Estimando taxas

Lindiwe estima com que frequência os funcionários da Saltmarsh relatam e-mails de phishing. Pelos dados sintéticos, 180 de 1.800 funcionários relataram pelo menos uma mensagem num trimestre, uma proporção de dez por cento. Ela calcula um intervalo de confiança e o encontra razoavelmente estreito, porque a amostra é grande. O Prof. Hale pede que ela declare o que a proporção descreve, os funcionários que relataram pelo menos uma vez, para que ninguém a confunda com a parcela dos e-mails de phishing que são relatados. Ela relata o intervalo junto com a proporção. A equipe de segurança usa o número como linha de base para futuras campanhas de conscientização.

### 7.2 Taxas-base

Uma regra de alerta sinaliza logins suspeitos com sensibilidade de noventa e nove por cento e especificidade de noventa e nove por cento. Lindiwe calcula o que acontece quando apenas um login em dez mil é malicioso. Num milhão de logins, cerca de noventa e nove ataques verdadeiros são sinalizados, junto com cerca de dez mil alarmes falsos. A maioria dos alertas é falsa, mesmo que a regra pareça precisa. Ela aprende que as taxas-base dominam a qualidade dos alertas e que os analistas devem esperar muitos falsos positivos na detecção de eventos raros. A equipe de monitoramento confirma que isso corresponde à sua experiência diária com os alertas de login.

### 7.3 Variação

As contagens semanais de detecções de malware variam mesmo quando nada muda. Lindiwe as modela como um processo de Poisson com média de doze por semana e mostra que semanas com dezoito ou mais acontecem ocasionalmente por acaso. Os gerentes tinham tratado uma semana assim como um surto. Ela recomenda limites de controle que marquem as semanas realmente incomuns. O Prof. Hale observa que entender a variação comum evita tanto o pânico com o ruído quanto a complacência diante de mudanças reais. Ela traça um ano de contagens semanais sintéticas com os limites desenhados como linhas horizontais.

### 7.4 Comparando grupos

A Saltmarsh quer saber se os depósitos com notebooks mais novos têm menos detecções de malware. Lindiwe adverte que os notebooks mais novos foram para os depósitos maiores, que também têm equipe de TI dedicada, então qualquer diferença poderia refletir a equipe, e não o hardware. Ela propõe comparar as taxas de detecção por dispositivo dentro de depósitos de porte semelhante. Ela aprende que a confusão é a principal armadilha dos dados observacionais de segurança e que as comparações precisam de um desenho cuidadoso. O gerente de TI concorda em fornecer as contagens de dispositivos por depósito. Lindiwe observa que, mesmo em depósitos semelhantes, a idade dos notebooks ainda pode estar correlacionada com outras diferenças que ela não consegue medir.

### Exemplo resolvido

Lindiwe estima uma taxa de relatos de dez por cento, mostra que as taxas-base tornam falsa a maioria dos alertas, modela as detecções semanais como Poisson e aponta a confusão numa comparação de notebooks.

> **Caso sintético.** Os números são sintéticos.

### Erros e limites

Um detector que parece preciso ainda pode produzir alertas em sua maioria falsos.

### Exercícios

- **EX019 — Alarmes falsos.** Aproximadamente quantos alarmes falsos ocorrem por milhão de logins? *Rubrica:* 3 = cerca de dez mil;; 2 = próximo;; 1 = errado;; 0 = nenhuma.

- **EX020 — Semanas de Poisson.** Que modelo descreve as detecções semanais? *Rubrica:* 3 = Poisson com média doze;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX021 — Fator de confusão dos notebooks.** O que poderia explicar menos detecções com notebooks novos? *Rubrica:* 3 = depósitos maiores com equipe de TI;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 50)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) explicar como o hardware impõe o isolamento; (2) descrever a inicialização confiável; (3) relacionar o firmware ao risco de segurança.

### 8.1 Níveis de privilégio

Os processadores executam código em diferentes níveis de privilégio. O kernel do sistema operacional roda com controle total, enquanto as aplicações rodam restritas e precisam pedir ao kernel para acessar o hardware. Lindiwe aprende que essa separação impede uma aplicação comprometida de ler diretamente a memória de outro programa. As unidades de gerenciamento de memória impõem as fronteiras entre os processos. O Prof. Hale explica que grande parte da segurança de software depende de esses recursos de hardware funcionarem corretamente, e é por isso que as falhas de processador afetam todos ao mesmo tempo. Lindiwe lê sobre falhas de processador que permitiram a programas inferir o conteúdo da memória através dessa fronteira.

### 8.2 Inicialização confiável

Quando um notebook liga, o firmware carrega um bootloader, que carrega o sistema operacional. Se um atacante alterar qualquer etapa, as verificações de segurança posteriores podem ser contornadas. O secure boot verifica uma assinatura digital em cada etapa e se recusa a executar código não assinado. Lindiwe confere um inventário sintético dos notebooks da Saltmarsh e encontra um pequeno grupo com o secure boot desativado por causa de um driver antigo. Ela recomenda substituir o driver para que o recurso possa ser ativado em toda a frota. A equipe de desktops agenda a substituição do driver para o próximo trimestre.

### 8.3 Firmware

O firmware das placas de rede, dos discos e das controladoras de gerenciamento roda abaixo do sistema operacional e raramente é atualizado. Lindiwe aprende que as controladoras de gerenciamento dos servidores muitas vezes têm sua própria interface de rede e suas próprias senhas. Na Saltmarsh, várias controladoras ainda usam as credenciais de fábrica na rede de servidores. Ela recomenda movê-las para uma rede de gerenciamento separada e trocar as credenciais. O Prof. Hale observa que os atacantes preferem as camadas que os defensores esquecem de monitorar. Lindiwe também lista as versões de firmware do inventário sintético e descobre que a maioria das controladoras de gerenciamento não foi atualizada desde a instalação, o que ela acrescenta ao acúmulo de correções.

### 8.4 Módulos de segurança de hardware

Algumas chaves precisam de uma proteção mais forte do que o software oferece. Um módulo de segurança de hardware guarda as chaves dentro de um hardware resistente a violação e executa operações criptográficas sem revelá-las. Lindiwe aprende que o provedor de pagamentos da Saltmarsh usa esses módulos, enquanto a chave de assinatura de código da própria Saltmarsh fica num arquivo num servidor de build. Ela recomenda movê-la para um token de hardware ou um serviço gerenciado de chaves, para que roubar o servidor de build não dê a um atacante a capacidade de assinar atualizações maliciosas. O líder de desenvolvimento concorda em orçar a mudança antes da próxima versão.

### Exemplo resolvido

Lindiwe liga os níveis de privilégio, o secure boot, as credenciais das controladoras de gerenciamento e a proteção de chaves em hardware a melhorias concretas na Saltmarsh.

> **Caso sintético.** Os inventários são sintéticos.

### Erros e limites

O firmware e as controladoras de gerenciamento muitas vezes ficam com as credenciais de fábrica.

### Exercícios

- **EX022 — Separação do kernel.** O que a separação entre kernel e aplicações impede? *Rubrica:* 3 = uma aplicação ler a memória de outra;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX023 — Lacuna do secure boot.** Por que o secure boot estava desativado em alguns notebooks? *Rubrica:* 3 = um driver antigo;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX024 — Chave de assinatura.** Para onde a chave de assinatura de código deve ir? *Rubrica:* 3 = um token de hardware ou um serviço gerenciado de chaves;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 50)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar ferramentas de segurança maiores; (2) testar código com casos conhecidos; (3) tratar segredos com segurança nos programas.

### 9.1 Estruturando ferramentas

Os scripts de Lindiwe crescem, então ela os organiza em funções com entradas e saídas claras: uma lê as contas, uma aplica as regras e uma escreve os relatórios. Cada função faz uma única tarefa e pode ser testada sozinha. O Prof. Hale explica que a estrutura importa mais nas ferramentas de segurança do que em outros lugares, porque um bug escondido pode relatar que tudo está em conformidade quando não está, e ninguém vai perceber até que um incidente prove o contrário. Ela também escreve uma breve descrição no início de cada função explicando o que ela verifica.

### 9.2 Testando com casos conhecidos

Lindiwe escreve testes usando pequenas entradas sintéticas cujas respostas corretas ela conhece: uma conta sem autenticação multifator e com direitos de administrador deve ser sinalizada; uma conta normal não deve. Ela executa os testes depois de cada mudança usando o módulo padrão unittest. Quando uma mudança posterior quebra a verificação de administradores, um teste falha de imediato. Ela aprende que os testes são a evidência de que uma verificação de segurança faz o que seu nome promete. No fim do semestre, seu arquivo de testes tem vinte casos, cada um com o nome da regra que verifica.

### 9.3 Tratando segredos

Uma ferramenta precisa chamar o diretório da Saltmarsh usando a senha de uma conta de serviço. A primeira versão de Lindiwe guardava a senha no script, que depois foi compartilhado num canal de chat. Ela reescreve a ferramenta para ler as credenciais de uma variável de ambiente definida pelo agendador e pede que a senha exposta seja trocada. O Prof. Hale observa que os segredos no código acabam em backups, repositórios e mensagens, muito além do público pretendido. A equipe do diretório rotaciona a senha em menos de uma hora depois do relato dela.

### 9.4 Dependências e cadeia de suprimentos

Lindiwe pensa em acrescentar uma biblioteca de terceiros para interpretar um formato de log. Ela confere quem a mantém, quando foi atualizada pela última vez e se tem vulnerabilidades conhecidas. Ela decide escrever ela mesma um pequeno interpretador, porque o formato é simples e a biblioteca não é mantida. Ela aprende que cada dependência amplia o código em que uma organização confia, e que manter as ferramentas de segurança pequenas reduz essa exposição. Seu interpretador tem oitenta linhas e é coberto por testes próprios. O Prof. Hale pede que ela registre os motivos dessa escolha num breve registro de decisão.

### Exemplo resolvido

Lindiwe estrutura sua ferramenta em funções testáveis, acrescenta testes unitários com casos conhecidos, move uma senha vazada para uma variável de ambiente e evita uma dependência sem manutenção.

> **Caso sintético.** O código é sintético.

### Erros e limites

Uma senha incluída no código deve ser tratada como exposta e trocada.

### Exercícios

- **EX025 — Módulo de testes.** Que módulo executa os testes dela? *Rubrica:* 3 = unittest;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX026 — Armazenamento de segredos.** De onde a ferramenta lê as credenciais? *Rubrica:* 3 = uma variável de ambiente definida pelo agendador;; 2 = parcialmente correto;; 1 = código;; 0 = nenhuma.

- **EX027 — Escolha do interpretador.** Por que escrever o próprio interpretador? *Rubrica:* 3 = formato simples, biblioteca sem manutenção;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — aula 09 (capítulo 09 de 50)

[← Capítulo 08](#ch-08) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética profissional ao trabalho de segurança; (2) tratar vulnerabilidades descobertas com responsabilidade; (3) respeitar a privacidade no monitoramento.

### 10.1 Dever profissional

Os engenheiros têm deveres para com o público, e não apenas para com os empregadores. Lindiwe lê códigos profissionais que enfatizam a honestidade, a competência e a proteção das pessoas contra danos. No trabalho de segurança, isso significa não exagerar a garantia, não usar acessos além do que uma tarefa exige e relatar os riscos mesmo quando é inconveniente. O Prof. Hale discute um caso em que um engenheiro aprovou um sistema como seguro sob pressão de prazo; os dados dos clientes foram expostos depois. Lindiwe observa que as assinaturas carregam responsabilidade. Ela escreve uma breve reflexão sobre o caso para o portfólio do curso.

### 10.2 Testes autorizados

Durante o estágio, Lindiwe percebe que uma página web de um depósito parece revelar os detalhes de rastreamento de outros clientes quando um número no endereço é alterado. Ela não explora mais para ver quantos dados estão expostos. Ela relata o que viu ao gerente do estágio, que confirma que ela não está autorizada a testar o site. A equipe de segurança investiga e corrige o problema. Ela aprende que a curiosidade precisa ficar dentro da autorização escrita, mesmo com boas intenções. O gerente agradece por ela ter parado quando parou.

### 10.3 Privacidade no monitoramento

O monitoramento de segurança registra o que os funcionários fazem. Lindiwe ajuda a revisar o aviso de monitoramento da Saltmarsh e descobre que ele não menciona que a navegação na web é registrada. Ela recomenda atualizar o aviso, limitar quem pode ver os logs de navegação e mantê-los apenas pelo tempo necessário para fins de segurança. O Prof. Hale explica que um monitoramento que os funcionários desconhecem prejudica a confiança e pode violar as regras de proteção de dados. O diretor de recursos humanos e o líder de segurança aprovam juntos o aviso revisado, e os funcionários o recebem por e-mail com uma breve explicação do que é registrado e por quê.

### 10.4 Ligações com a segurança física

Alguns sistemas da Saltmarsh afetam a segurança física das pessoas: os reboques refrigerados transportam medicamentos, e seus dados de temperatura precisam ser exatos. Um registro de temperatura adulterado poderia permitir que medicamentos estragados chegassem aos pacientes. Lindiwe observa que as falhas de integridade aqui são falhas de segurança física, e não apenas problemas de dados. Ela recomenda proteção de integridade para os registros dos sensores e um escalonamento claro quando houver leituras ausentes. Ela aprende que a engenharia de segurança às vezes protege vidas, além de informações. A equipe da frota acrescenta uma verificação que dispara um alarme quando o registro de temperatura de um reboque tem lacunas, e Lindiwe documenta a nova regra no relatório de estágio.

### Exemplo resolvido

Lindiwe relata uma possível exposição de dados sem testá-la, recomenda um aviso de monitoramento mais claro e liga a integridade dos registros de temperatura à segurança dos pacientes.

> **Caso sintético.** Os incidentes são sintéticos.

### Erros e limites

Testar um sistema em produção sem autorização não é aceitável, mesmo para ajudar.

### Exercícios

- **EX028 — Relato sem teste.** O que Lindiwe faz ao perceber a exposição? *Rubrica:* 3 = relata sem testar mais;; 2 = parcialmente correto;; 1 = testa;; 0 = nenhuma.

- **EX029 — Lacuna do aviso.** O que o aviso de monitoramento omitia? *Rubrica:* 3 = o registro da navegação na web;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX030 — Ligação com a segurança física.** Por que os registros de temperatura importam para a segurança das pessoas? *Rubrica:* 3 = a adulteração poderia permitir que medicamentos estragados chegassem aos pacientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — aula 10 (capítulo 10 de 50)

[← Capítulo 09](#ch-09) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar como os pacotes se movem entre redes; (2) identificar fraquezas de protocolos; (3) aplicar a segmentação para limitar ataques.

### 11.1 Camadas e pacotes

Lindiwe estuda como os dados atravessam a rede da Saltmarsh. As aplicações entregam os dados aos protocolos de transporte, que entregam os pacotes à camada de rede para o roteamento entre os depósitos e a sede. Cada camada acrescenta cabeçalhos que os dispositivos leem para decidir para onde os pacotes vão. Ela captura tráfego sintético num laboratório e identifica endereços, portas e protocolos. O Prof. Hale explica que os atacantes exploram as mesmas camadas, então entender o tráfego normal é o primeiro passo para reconhecer o tráfego incomum nas ferramentas de monitoramento da Saltmarsh. Ela rotula cada fluxo capturado por depósito e aplicação.

### 11.2 Fraquezas de protocolos

Muitos protocolos antigos foram projetados para redes confiáveis e enviam dados sem cifração. Lindiwe descobre que algumas impressoras de depósito ainda são gerenciadas por um protocolo que envia senhas em texto claro. Qualquer pessoa que capture o tráfego no mesmo segmento de rede poderia lê-las. Ela recomenda passar para um gerenciamento cifrado ou, onde as impressoras não o suportarem, isolá-las. Ela aprende que a escolha do protocolo é uma decisão de segurança, e que os dispositivos legados muitas vezes forçam concessões que precisam ser documentadas e contidas, e não ignoradas. O fornecedor das impressoras confirma isso.

### 11.3 Resolução de nomes

O sistema de nomes de domínio traduz nomes em endereços. Se um atacante conseguir alterar as respostas, os usuários podem se conectar a um servidor falso sem perceber. Lindiwe revisa os resolvedores da Saltmarsh e confirma que eles encaminham apenas para serviços superiores aprovados e registram as consultas. Os logs ajudam a detectar malware que contata domínios incomuns. O Prof. Hale observa que a resolução de nomes é um caminho comum tanto para o ataque quanto para a detecção, então sua configuração merece a mesma atenção que os firewalls, embora muitas vezes receba bem menos. Ela compartilha a revisão dos resolvedores com as operações.

### 11.4 Segmentação

Os depósitos da Saltmarsh originalmente compartilhavam uma única rede plana, então um notebook comprometido podia alcançar diretamente os servidores da folha de pagamento. Lindiwe ajuda a projetar segmentos: dispositivos de escritório, leitores do armazém, impressoras, servidores e interfaces de gerenciamento, cada um com regras de firewall que permitem apenas o tráfego necessário entre eles. Ela estima que a segmentação remove a maioria dos caminhos diretos dos notebooks dos depósitos até os servidores sensíveis. Ela aprende que a segmentação não impede um atacante de entrar, mas limita até onde ele se move, o que ganha tempo para a detecção e reduz os danos. A equipe de rede agenda a migração do primeiro depósito para a semana de parada da primavera.

### Exemplo resolvido

Lindiwe mapeia o tráfego por camada, sinaliza o gerenciamento das impressoras em texto claro, revisa o registro dos resolvedores e projeta segmentos que cortam os caminhos diretos dos notebooks dos depósitos até os servidores.

> **Caso sintético.** O tráfego e os projetos são sintéticos.

### Erros e limites

Uma rede plana permite que um único dispositivo comprometido alcance tudo.

### Exercícios

- **EX031 — Risco do texto claro.** Que risco o protocolo de gerenciamento das impressoras representa? *Rubrica:* 3 = senhas enviadas em texto claro;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX032 — Logs dos resolvedores.** O que os logs dos resolvedores podem ajudar a detectar? *Rubrica:* 3 = malware que contata domínios incomuns;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX033 — Valor da segmentação.** O que a segmentação limita principalmente? *Rubrica:* 3 = até onde os atacantes se movem;; 2 = parcialmente correto;; 1 = a entrada;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — aula 11 (capítulo 11 de 50)

[← Capítulo 10](#ch-10) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) explicar o isolamento de processos e as permissões; (2) endurecer as configurações do sistema operacional; (3) coletar logs úteis do sistema.

### 12.1 Processos e permissões

Os sistemas operacionais executam programas como processos pertencentes a contas de usuário, e as permissões decidem o que cada conta pode ler, gravar ou executar. Lindiwe examina um servidor de arquivos sintético da Saltmarsh e descobre que um serviço de backup roda com a conta mais poderosa. Se o serviço fosse comprometido, o atacante ganharia controle total. Ela recomenda uma conta dedicada apenas com os direitos de que os backups precisam. O Prof. Hale observa que executar os serviços com privilégio mínimo limita o dano que qualquer falha isolada pode causar. A equipe de servidores concorda.

### 12.2 Endurecimento

As instalações padrão favorecem a conveniência. Lindiwe percorre uma lista de verificação de endurecimento para os servidores Linux da Saltmarsh: desativar o login remoto de root, remover serviços sem uso, aplicar atualizações dentro de um prazo definido e cifrar os discos. Ela aprende que cada item reduz a superfície de ataque ou limita o impacto de um dispositivo roubado. Ela também aprende que as listas de verificação se desviam com o tempo: servidores configurados corretamente no ano passado podem ter mudado desde então, e é por isso que capítulos posteriores medem a conformidade automaticamente em vez de confiar nos registros de instalação. Ela registra quais itens da lista cada servidor sintético já atende e quais precisam de trabalho.

### 12.3 Registro de logs do sistema

Os sistemas operacionais registram logins, mudanças de privilégio e falhas de serviços. Lindiwe configura servidores sintéticos para encaminhar esses logs a um coletor central, para que um atacante que ganhe o controle de um servidor não possa simplesmente apagar as evidências locais. Ela escolhe os eventos com cuidado, porque registrar tudo produz ruído e custo. O Prof. Hale pede que ela justifique cada tipo de evento por uma pergunta de investigação que ele responderia, como quem usou direitos de administrador neste servidor na semana passada, o que mantém o registro com propósito. O coletor guarda os logs por um ano.

### 12.4 Atualizações

As atualizações do sistema operacional corrigem vulnerabilidades, mas podem quebrar aplicações. A Saltmarsh adia as atualizações em alguns servidores porque uma aplicação do armazém certa vez falhou depois de uma atualização. Lindiwe propõe um grupo de teste de servidores que recebe as atualizações primeiro, com promoção automática para os demais depois de uma semana sem problemas. Ela aprende que processos de atualização confiáveis são em si um controle de segurança, porque o medo de quebrar algo é um dos motivos mais comuns pelos quais as organizações deixam vulnerabilidades conhecidas abertas por meses. O dono da aplicação do armazém concorda em entrar no grupo de teste.

### Exemplo resolvido

Lindiwe move um serviço de backup para uma conta de privilégio mínimo, aplica uma lista de verificação de endurecimento, encaminha logs com propósito para um coletor central e propõe atualizações em etapas.

> **Caso sintético.** Os servidores são sintéticos.

### Erros e limites

Logs guardados apenas no servidor podem ser apagados por um atacante que o controla.

### Exercícios

- **EX034 — Conta de backup.** Que conta o serviço de backup deve usar? *Rubrica:* 3 = uma conta dedicada de privilégio mínimo;; 2 = parcialmente correto;; 1 = administrador;; 0 = nenhuma.

- **EX035 — Logs centrais.** Por que encaminhar os logs a um coletor central? *Rubrica:* 3 = os atacantes não podem apagar as evidências locais;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX036 — Atualizações em etapas.** O que Lindiwe propõe para as atualizações? *Rubrica:* 3 = primeiro um grupo de teste, depois a promoção após uma semana;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — aula 12 (capítulo 12 de 50)

[← Capítulo 11](#ch-11) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) proteger bancos de dados contra ataques comuns; (2) controlar o acesso a campos sensíveis; (3) projetar backups que sustentem a recuperação.

### 13.1 Acesso ao banco de dados

O banco de dados de remessas da Saltmarsh guarda endereços de clientes e observações de entrega. Lindiwe descobre que a aplicação web se conecta com uma conta que pode ler, alterar e excluir todas as tabelas. Ela recomenda contas separadas para leitura e gravação, cada uma limitada às tabelas necessárias. Se a aplicação fosse comprometida, o atacante poderia então fazer menos. O Prof. Hale explica que as permissões de banco de dados muitas vezes são concedidas de forma ampla durante o desenvolvimento e nunca são restringidas, então revisá-las é valioso no início de qualquer avaliação. Os desenvolvedores criam as duas novas contas em uma semana.

### 13.2 Injeção

Lindiwe estuda como as aplicações montam as consultas ao banco de dados. Um código que insere a entrada do usuário diretamente no texto da consulta permite a injeção, em que uma entrada elaborada muda o significado da consulta. Ela revisa uma página de busca sintética e descobre que ela monta as consultas juntando strings. Ela a reescreve para usar consultas parametrizadas, de modo que a entrada seja sempre tratada como dado. Ela aprende que a injeção continua comum porque montar strings é fácil, e que a revisão de código e os testes precisam procurá-la especificamente. Ela acrescenta um teste que envia uma aspa e um ponto e vírgula.

### 13.3 Campos sensíveis

Alguns campos, como os números das carteiras de motorista, precisam de proteção mais forte que outros. Lindiwe pensa em cifrá-los no nível do campo, para que os administradores do banco de dados e os backups vejam apenas texto cifrado. As aplicações que precisam dos valores os decifram com chaves guardadas separadamente. Ela anota o custo: buscar e ordenar campos cifrados fica mais difícil. O Prof. Hale pede que ela justifique a cifração de campos por quem deve e quem não deve ver os valores, e não por um desejo geral de cifrar tudo. Ela conclui que apenas os números das carteiras justificam a cifração de campo na Saltmarsh.

### 13.4 Backups para a recuperação

Os backups protegem a disponibilidade e a integridade, mas só se puderem ser restaurados. Lindiwe aprende que o ransomware muitas vezes ataca os backups primeiro, então as cópias precisam ficar onde um atacante que controla a rede principal não consiga excluí-las. A Saltmarsh mantém backups noturnos num compartilhamento de rede acessível a partir dos servidores. Ela recomenda uma cópia adicional que não possa ser alterada por um período definido. Ela também observa que as restaurações precisam ser testadas, um tema a que o curso volta com um laboratório de verificação. A equipe de infraestrutura orça a cópia imutável.

### Exemplo resolvido

Lindiwe restringe as contas do banco de dados, substitui as consultas montadas com strings por consultas parametrizadas, pondera a cifração de campo para os números das carteiras e recomenda cópias de backup imutáveis.

> **Caso sintético.** Os bancos de dados são sintéticos.

### Erros e limites

Um backup acessível e excluível a partir da rede principal pode não sobreviver ao ransomware.

### Exercícios

- **EX037 — Contas do banco de dados.** O que Lindiwe recomenda para o acesso da aplicação ao banco de dados? *Rubrica:* 3 = contas separadas e limitadas de leitura e gravação;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX038 — Correção da injeção.** Como ela corrige a página de busca? *Rubrica:* 3 = consultas parametrizadas;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX039 — Cópia de backup.** Que cópia de backup extra ela recomenda? *Rubrica:* 3 = uma que não possa ser alterada por um período definido;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — aula 13 (capítulo 13 de 50)

[← Capítulo 12](#ch-12) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) integrar a segurança ao ciclo de vida do desenvolvimento; (2) usar uma revisão de código atenta às ameaças; (3) gerenciar vulnerabilidades nas dependências.

### 14.1 Segurança no ciclo de vida

Os desenvolvedores da Saltmarsh constroem um aplicativo para os motoristas registrarem as confirmações de entrega. Lindiwe aprende que a segurança acrescentada no fim é cara, enquanto a segurança considerada desde os requisitos é mais barata. Ela ajuda a escrever os requisitos de segurança: os motoristas se autenticam com suas próprias contas, as confirmações não podem ser alteradas depois de enviadas e os dados de localização são guardados apenas enquanto puderem surgir disputas. O Prof. Hale observa que requisitos claros dão aos testadores algo concreto para conferir, em vez de uma instrução vaga para tornar o aplicativo seguro. O dono do produto aceita os três requisitos.

### 14.2 Revisão de código

Lindiwe participa das revisões de código do aplicativo dos motoristas. Ela procura os padrões que aprendeu: consultas montadas com strings, segredos no código, ausência de validação de entradas e permissões conferidas apenas na interface do usuário. Numa mudança, o aplicativo esconde dos motoristas um botão de exclusão, mas o servidor aceita pedidos de exclusão de qualquer pessoa logada. Ela explica que toda verificação precisa acontecer no servidor, porque os atacantes não usam a interface oficial. O desenvolvedor corrige a verificação no servidor no mesmo dia e acrescenta um teste que envia um pedido de exclusão a partir de uma conta de motorista e espera uma recusa.

### 14.3 Gestão de dependências

O aplicativo dos motoristas usa dezenas de bibliotecas de código aberto. Lindiwe monta uma lista das dependências com as versões e a confere toda semana contra bases públicas de vulnerabilidades. Uma biblioteca tem uma falha conhecida que permite negação de serviço, e existe uma atualização. Os desenvolvedores a atualizam depois de executar seus testes. Ela aprende que a maior parte do código das aplicações é emprestada, então saber o que está incluído é essencial, e que uma lista de dependências é em si um registro de segurança. A verificação semanal leva poucos minutos e roda automaticamente no servidor de build, enviando os resultados ao canal da equipe.

### 14.4 Integridade do build

O código é transformado em pacotes instaláveis por um servidor de build. Se um atacante alterar o build, todos os usuários recebem software malicioso. Lindiwe recomenda que os builds rodem a partir de scripts sob controle de versão, que os servidores de build sejam isolados e que os pacotes sejam assinados com uma chave protegida. O Prof. Hale liga isso à recomendação anterior dela sobre a chave de assinatura de código. Ela aprende que o caminho do código-fonte até o dispositivo do usuário faz parte da superfície de ataque e precisa ser protegido. O líder de desenvolvimento acrescenta essas etapas ao roteiro.

### Exemplo resolvido

Lindiwe escreve requisitos de segurança para um aplicativo de motoristas, encontra na revisão uma lacuna de autorização no servidor, acompanha as dependências semanalmente e recomenda um pipeline de build protegido.

> **Caso sintético.** O aplicativo é sintético.

### Erros e limites

Esconder um botão na interface não impede os pedidos ao servidor.

### Exercícios

- **EX040 — Falha da exclusão.** Que falha a revisão de código encontra? *Rubrica:* 3 = o servidor aceita pedidos de exclusão de qualquer pessoa logada;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX041 — Verificação das dependências.** Com que frequência as dependências são conferidas? *Rubrica:* 3 = semanalmente;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX042 — Proteção do build.** Cite uma proteção do build que ela recomenda. *Rubrica:* 3 = pacotes assinados;; 2 = uma;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — aula 14 (capítulo 14 de 50)

[← Capítulo 13](#ch-13) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) definir confidencialidade, integridade e disponibilidade; (2) categorizar sistemas pelo impacto; (3) relacionar ameaças, vulnerabilidades e risco.

### 15.1 Três objetivos

Lindiwe estuda os objetivos de segurança usados em toda a área. A FIPS 199 define três: a confidencialidade, que preserva as restrições autorizadas de acesso e divulgação; a integridade, que protege contra modificação ou destruição indevidas; e a disponibilidade, que garante acesso oportuno e confiável. A ISO/IEC 27000:2026, a visão geral atual da família ISO/IEC 27000, descreve a segurança da informação nos mesmos três termos. Ela os aplica à Saltmarsh: a folha de pagamento precisa de confidencialidade, os registros de entrega precisam de integridade e o sistema de despacho precisa de disponibilidade durante o horário de trabalho. O Prof. Hale pede que ela justifique cada escolha descrevendo o que aconteceria se aquele objetivo falhasse durante um dia de trabalho inteiro.

### 15.2 Categorizando sistemas

A FIPS 199 pergunta quão grave seria o impacto se cada objetivo fosse perdido: baixo, moderado ou alto. Lindiwe categoriza cinco sistemas da Saltmarsh. A folha de pagamento é alta em confidencialidade; o despacho é alto em disponibilidade; o site público é baixo em confidencialidade, mas moderado em integridade, já que uma desfiguração prejudica a reputação. O Prof. Hale explica a marca d'água mais alta: a categoria geral toma a mais alta das três. Ela aprende que a categorização concentra o esforço nos sistemas cuja falha mais prejudicaria. Ela registra cada categorização com uma justificativa de uma linha para a classificação.

### 15.3 Ameaças e vulnerabilidades

Uma ameaça é algo que poderia causar dano, como um grupo criminoso em busca de resgate. Uma vulnerabilidade é uma fraqueza que uma ameaça poderia explorar, como um servidor sem correções. O risco combina a probabilidade de uma ameaça explorar uma vulnerabilidade com o impacto, caso isso ocorra. Lindiwe lê a NIST SP 800-30 Revisão 1, que descreve essa abordagem de avaliação de riscos. Ela observa que o risco só existe quando ameaça, vulnerabilidade e impacto se juntam para um sistema específico. Ela anota um exemplo de cada para o sistema de despacho.

### 15.4 Controles

Os controles reduzem o risco ao prevenir, detectar ou corrigir danos. Lindiwe classifica exemplos na Saltmarsh: a autenticação multifator previne o sequestro de contas, os alertas de logs detectam atividades suspeitas e os backups corrigem os danos depois de um ransomware. Ela aprende que depender de um único tipo é frágil, porque a prevenção acaba falhando. O Prof. Hale apresenta a defesa em profundidade, que combina vários controles independentes para que a falha de um não exponha completamente o sistema, e pede que ela a demonstre para a folha de pagamento. Para a folha de pagamento, ela lista como camadas separadas a autenticação multifator, o acesso restrito pela rede, as revisões de acesso, os alertas sobre exportações em massa e os backups testados.

### Exemplo resolvido

Lindiwe define os três objetivos a partir da FIPS 199, categoriza cinco sistemas pela marca d'água mais alta, separa ameaça de vulnerabilidade e monta controles em camadas para a folha de pagamento.

> **Caso sintético.** As categorizações são sintéticas.

### Erros e limites

Chamar uma vulnerabilidade de risco ignora a ameaça e o impacto.

### Exercícios

- **EX043 — Definição de integridade.** Como a FIPS 199 define a integridade? *Rubrica:* 3 = proteção contra modificação ou destruição indevidas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX044 — Marca d'água mais alta.** O que é a marca d'água mais alta? *Rubrica:* 3 = a categoria geral é a mais alta das três;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX045 — Defesa em profundidade.** O que é a defesa em profundidade? *Rubrica:* 3 = vários controles independentes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — aula 15 (capítulo 15 de 50)

[← Capítulo 14](#ch-14) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) aplicar o pensamento sistêmico à segurança; (2) gerenciar requisitos e interfaces; (3) planejar a segurança ao longo do ciclo de vida do sistema.

### 16.1 Pensamento sistêmico

A segurança de um sistema depende de como suas partes interagem. Lindiwe estuda o sistema de despacho da Saltmarsh: uma aplicação web, um banco de dados, uma fila de mensagens, os celulares dos motoristas e um serviço externo de mapas. Uma fraqueza em qualquer interface poderia afetar o todo. O Prof. Hale pede que ela liste cada interface com os dados que a atravessam e a confiança presumida. Ela descobre que o serviço de mapas recebe os endereços de entrega completos, algo que ninguém tinha considerado quando o contrato foi assinado. A equipe de compras revisa o contrato e pergunta ao fornecedor por quanto tempo os endereços são guardados.

### 16.2 Rastreabilidade dos requisitos

Lindiwe rastreia cada requisito de segurança até o componente que o implementa e o teste que o verifica. Por exemplo, o requisito de que as confirmações não podem ser alteradas depois de enviadas corresponde a uma restrição do banco de dados e a um teste que tenta uma atualização. Ela encontra dois requisitos sem teste. O Prof. Hale explica que a rastreabilidade mostra as lacunas cedo e dá evidências aos auditores, porque um requisito sem teste é apenas uma intenção que ninguém conferiu. Os desenvolvedores escrevem os dois testes que faltavam antes da próxima versão, e Lindiwe atualiza sua tabela de rastreabilidade para mostrar cada requisito coberto.

### 16.3 Ciclo de vida

As necessidades de segurança mudam ao longo da vida de um sistema: projeto, construção, operação, mudança e desativação. Lindiwe observa que a desativação muitas vezes é esquecida. Um servidor de despacho antigo, substituído no ano passado, ainda roda com software desatualizado e guarda cópias de dados de clientes. Ela recomenda uma lista de verificação de desativação que cubra a exclusão dos dados, a remoção das contas e a desconexão da rede. Ela aprende que cada etapa do ciclo de vida precisa de atividades de segurança explícitas, e não apenas o projeto e a construção. O servidor antigo é apagado e desconectado em menos de um mês depois do relatório dela. A equipe de infraestrutura acrescenta a lista de verificação de desativação ao seu processo padrão de mudanças, para que as futuras desativações sigam as mesmas etapas.

### 16.4 Compromissos

A engenharia de sistemas equilibra necessidades concorrentes. Uma autenticação mais forte para os motoristas acrescenta alguns segundos por entrega, o que pesa ao longo de milhares de entregas por dia. Lindiwe mede o tempo acrescentado por um aviso sintético de multifator e propõe lembrar os dispositivos confiáveis durante um turno. O Prof. Hale observa que as escolhas de segurança que ignoram o custo operacional tendem a ser contornadas, e que documentar os compromissos abertamente ajuda os gerentes a aceitar deliberadamente o risco restante. O aviso sintético acrescenta cerca de quatro segundos por login. Com os dispositivos lembrados, os motoristas se autenticam uma vez por turno em vez de a cada entrega, e o gerente de operações aceita esse desenho.

### Exemplo resolvido

Lindiwe lista as interfaces do despacho e descobre endereços compartilhados com um serviço de mapas, rastreia os requisitos até os testes, acrescenta uma lista de verificação de desativação e equilibra o atraso da autenticação com o tempo de entrega.

> **Caso sintético.** Os sistemas são sintéticos.

### Erros e limites

Servidores desativados e esquecidos muitas vezes mantêm dados antigos e vulnerabilidades antigas.

### Exercícios

- **EX046 — Dados dos mapas.** Que dados o serviço de mapas recebe? *Rubrica:* 3 = os endereços de entrega completos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX047 — Requisitos sem teste.** Quantos requisitos não tinham teste? *Rubrica:* 3 = dois;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX048 — Lista de desativação.** O que a lista de verificação de desativação cobre? *Rubrica:* 3 = exclusão dos dados, remoção das contas, desconexão;; 2 = todos;; 1 = alguns;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — aula 16 (capítulo 16 de 50)

[← Capítulo 15](#ch-15) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) descrever os processos de segurança como laços de realimentação; (2) medir o atraso do laço; (3) evitar respostas instáveis.

### 17.1 Laços de realimentação

A teoria de controle estuda sistemas que medem sua saída e se ajustam. Lindiwe vê as operações de segurança como um laço: os sensores produzem logs, os analistas detectam problemas, os respondentes agem e o ambiente muda. Se qualquer etapa for lenta, o laço responde tarde. Ela mapeia o laço da Saltmarsh para logins suspeitos e descobre que a etapa mais lenta é a espera para que um analista revise os alertas durante a noite. O Prof. Hale observa que pensar em realimentação mostra onde o atraso se acumula. Ela desenha o laço com o tempo que cada etapa leva nos registros sintéticos, marcando em vermelho a etapa da revisão noturna para discussão.

### 17.2 Atraso

O atraso importa porque os atacantes se movem durante ele. Lindiwe estima os tempos a partir de registros sintéticos: detecção em minutos, triagem em horas durante o dia, mas em até doze horas durante a noite, e resposta logo depois da triagem. Ela recomenda a contenção automatizada para alertas de alta confiança, como bloquear uma conta depois de uma adivinhação de senhas confirmada, para que o laço se feche sem esperar por uma pessoa. Ela aprende que reduzir o atraso mais lento ajuda mais do que acelerar etapas que já são rápidas. O líder de segurança aprova um teste de bloqueio automatizado por um mês.

### 17.3 Estabilidade

A realimentação pode reagir em excesso. Se uma regra automatizada bloquear as contas depois de algumas falhas de login, os atacantes podem bloquear muitos funcionários de propósito, transformando um controle numa negação de serviço. Lindiwe propõe respostas graduais: primeiro desacelerar as tentativas de login, depois exigir verificação adicional e bloquear apenas diante de sinais fortes. O Prof. Hale compara isso ao amortecimento nos sistemas de controle, que evita a oscilação. Ela aprende que a força da resposta deve corresponder à confiança no sinal. A equipe de monitoramento adota a abordagem gradual e registra com que frequência cada etapa é acionada durante o teste.

### 17.4 Medindo o laço

Lindiwe propõe medir o laço rotineiramente: tempo para detectar, tempo para triar e tempo para conter, relatados mensalmente. Ela observa que as médias escondem as caudas longas, então relata as medianas e o décimo mais lento. O Prof. Hale pede que ela defina com precisão os eventos de início e de fim, porque analistas diferentes podem registrar os tempos de formas diferentes. Ela aprende que medir um processo de forma consistente é o primeiro passo para melhorá-lo, um tema que volta nos capítulos posteriores sobre medição. Ela redige um modelo de relatório mensal para o líder de segurança.

### Exemplo resolvido

Lindiwe mapeia o laço dos alertas de login, descobre que a triagem noturna é a etapa mais lenta, propõe contenção automatizada com respostas graduais e define as métricas do laço.

> **Caso sintético.** Os tempos são sintéticos.

### Erros e limites

Bloqueios automáticos agressivos podem se tornar uma negação de serviço.

### Exercícios

- **EX049 — Etapa mais lenta.** Qual é a etapa mais lenta do laço? *Rubrica:* 3 = a revisão noturna pelo analista;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX050 — Resposta gradual.** O que vem antes de bloquear uma conta? *Rubrica:* 3 = desacelerar as tentativas, depois verificação extra;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX051 — Métricas do laço.** Que estatísticas ela relata? *Rubrica:* 3 = medianas e o décimo mais lento;; 2 = parcialmente correto;; 1 = médias;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — aula 17 (capítulo 17 de 50)

[← Capítulo 16](#ch-16) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) aplicar os princípios clássicos de projeto; (2) projetar zonas e fronteiras de confiança; (3) avaliar arquiteturas contra os princípios.

### 18.1 Princípios de projeto

Lindiwe lê o artigo de Saltzer e Schroeder de 1975 sobre a proteção da informação em sistemas computacionais. Ele lista princípios que ainda orientam a arquitetura: economia de mecanismo, padrões à prova de falhas, mediação completa, projeto aberto, separação de privilégios, privilégio mínimo, mínimo mecanismo comum e aceitabilidade psicológica. Ela os relaciona à Saltmarsh. Padrões à prova de falhas significam que os novos funcionários não recebem acesso até a aprovação; mediação completa significa que cada pedido é conferido, e não apenas o primeiro. Ela observa que os princípios são antigos, mas amplamente citados. O Prof. Hale pede que ela dê um exemplo da Saltmarsh para cada princípio.

### 18.2 Zonas e fronteiras

Lindiwe projeta zonas para a Saltmarsh: uma zona voltada para a internet para o site e a interface do aplicativo dos motoristas, uma zona interna para os funcionários, uma zona restrita para a folha de pagamento e uma zona de gerenciamento para os administradores. O tráfego entre as zonas passa por controles que impõem regras. Ela marca as fronteiras de confiança no diagrama anterior. O Prof. Hale pergunta que princípio cada fronteira sustenta; ela identifica o privilégio mínimo e a mediação completa como os principais. Ela lista numa tabela o tráfego permitido entre cada par de zonas, e a equipe de rede a usa como conjunto inicial de regras.

### 18.3 Avaliando opções

Existem duas opções de arquitetura para a interface do aplicativo dos motoristas: acesso direto ao banco de dados do despacho ou um serviço intermediário que expõe apenas as funções necessárias. Lindiwe avalia as duas contra os princípios. O serviço intermediário segue melhor o privilégio mínimo e a economia de mecanismo, porque o banco de dados nunca é exposto. Ele acrescenta trabalho de desenvolvimento. Ela registra a avaliação num registro de decisão, e os desenvolvedores escolhem o serviço intermediário. O registro de decisão lista as duas opções, os princípios que cada uma sustenta e o tempo extra estimado de desenvolvimento. O Prof. Hale elogia o registro por tornar o raciocínio visível.

### 18.4 Projeto aberto

Saltzer e Schroeder defenderam que a segurança não deve depender de os atacantes desconhecerem o projeto. Lindiwe aplica isso à ferramenta própria de transferência de arquivos da Saltmarsh, cuja segurança dependia de uma porta não documentada. Ela recomenda autenticação e cifração que continuem seguras mesmo que o projeto seja publicado. O Prof. Hale observa que o projeto aberto também permite a revisão, já que especialistas externos podem examinar um projeto publicado e encontrar fraquezas antes dos atacantes. A ferramenta é substituída por um serviço padrão de transferência cifrada dentro do ano. Sua configuração é documentada abertamente para a equipe de operações.

### Exemplo resolvido

Lindiwe relaciona os princípios de Saltzer e Schroeder à Saltmarsh, projeta quatro zonas, escolhe um serviço intermediário pelo privilégio mínimo e substitui a dependência do sigilo do projeto.

> **Caso sintético.** As arquiteturas são sintéticas.

### Erros e limites

Depender de uma porta não documentada é obscuridade, não proteção.

### Exercícios

- **EX052 — Padrões à prova de falhas.** O que os padrões à prova de falhas significam para os novos funcionários? *Rubrica:* 3 = nenhum acesso até a aprovação;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX053 — Opção escolhida.** Que opção os desenvolvedores escolhem? *Rubrica:* 3 = o serviço intermediário;; 2 = parcialmente correto;; 1 = direta;; 0 = nenhuma.

- **EX054 — Projeto aberto.** De que a ferramenta de transferência dependia? *Rubrica:* 3 = uma porta não documentada;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — aula 18 (capítulo 18 de 50)

[← Capítulo 17](#ch-17) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) gerenciar as identidades ao longo do seu ciclo de vida; (2) aplicar a autenticação multifator; (3) usar a criptografia de forma adequada.

### 19.1 Ciclo de vida das identidades

Toda conta segue um ciclo de vida: a criação quando alguém entra, as mudanças quando a pessoa muda de função e a remoção quando ela sai. Lindiwe descobre que os desligados da Saltmarsh são removidos do diretório, mas não do sistema de roteamento dos depósitos, que tem contas próprias. Ela recomenda ligar todos os sistemas a uma única fonte de identidade, para que o desligamento acione a remoção em todos os lugares. O Prof. Hale observa que as contas órfãs são um caminho comum para o uso indevido, porque ninguém percebe quando estão sendo usadas. A equipe de identidade concorda em conectar o sistema de roteamento no próximo trimestre.

### 19.2 Autenticação multifator

As senhas sozinhas são fracas porque podem ser adivinhadas, reutilizadas ou capturadas por phishing. A autenticação multifator exige um segundo fator, como um código de um aplicativo ou uma chave de hardware. Lindiwe compara as opções para a Saltmarsh. As chaves de hardware resistem melhor ao phishing; os avisos por aplicativo são mais fáceis de implantar, mas podem ser aprovados por usuários cansados que aceitam pedidos inesperados. Ela recomenda chaves de hardware para os administradores e códigos por aplicativo para os demais funcionários, com a ampliação posterior dos métodos resistentes a phishing. O líder de segurança aprova o plano, começando pelos vinte administradores.

### 19.3 Fundamentos de criptografia

Lindiwe estuda a cifração simétrica, em que uma única chave cifra e decifra, e a criptografia de chave pública, em que uma chave pública cifra ou verifica e uma chave privada decifra ou assina. As funções de hash produzem impressões digitais de tamanho fixo dos dados. Ela aprende que a segurança de cada uma depende de manter as chaves em segredo e de usar algoritmos e bibliotecas bem revisados. O Prof. Hale adverte que projetar novos esquemas criptográficos é um campo especializado e que os engenheiros devem usar os já estabelecidos. Ela pratica com o módulo hashlib do Python, calculando impressões digitais de arquivos sintéticos.

### 19.4 Gerenciamento de chaves

A maioria das falhas criptográficas vem do manuseio das chaves, e não dos algoritmos. Lindiwe revisa como a Saltmarsh gerencia os certificados dos seus sites. Dois certificados expiraram no ano passado, causando indisponibilidades, porque a renovação dependia de alguém se lembrar. Ela recomenda um inventário de certificados e chaves com donos e datas de expiração, além da renovação automatizada sempre que possível. Ela aprende que o gerenciamento de chaves é uma disciplina operacional tanto quanto técnica. O inventário lista quarenta certificados na exportação sintética. Seis expiram em até noventa dias, e a equipe de operações os renova de imediato enquanto a automação é configurada.

### Exemplo resolvido

Lindiwe liga a remoção dos desligados a uma única fonte de identidade, escolhe chaves de hardware para os administradores, revisa os blocos de construção criptográficos e propõe um inventário de certificados com renovação automatizada.

> **Caso sintético.** Os sistemas são sintéticos.

### Erros e limites

Os avisos de aprovação por aplicativo podem ser aceitos por usuários que não iniciaram um login.

### Exercícios

- **EX055 — Contas órfãs.** De onde os desligados não eram removidos? *Rubrica:* 3 = o sistema de roteamento dos depósitos;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX056 — Fator dos administradores.** Que fator ela recomenda para os administradores? *Rubrica:* 3 = chaves de hardware;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX057 — Indisponibilidades por certificados.** Por que os certificados expiraram? *Rubrica:* 3 = a renovação dependia da memória;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue estudando — aula 19 (capítulo 19 de 50)

[← Capítulo 18](#ch-18) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Segurança da informação: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) situar o trabalho de engenharia dentro das normas de gestão; (2) usar catálogos de controles e frameworks; (3) entender o escopo de um sistema de gestão da segurança da informação.

### 20.1 Sistemas de gestão

Lindiwe aprende que a ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) especifica requisitos para um sistema de gestão da segurança da informação: uma forma estruturada de entender o contexto, avaliar e tratar riscos, definir objetivos, operar controles, monitorar o desempenho e melhorar. A Saltmarsh está considerando a certificação porque grandes clientes a pedem. O Prof. Hale explica que a norma pede à organização que decida de que controles precisa com base no risco e que registre essas decisões numa declaração de aplicabilidade, com os motivos da inclusão ou da exclusão. Lindiwe redige uma entrada de exemplo para a autenticação multifator.

### 20.2 Orientação sobre controles

A ISO/IEC 27002:2022 dá orientações sobre os controles de segurança da informação, agrupados como controles organizacionais, de pessoas, físicos e tecnológicos. Lindiwe relaciona seu trabalho anterior a esses grupos: o aviso de monitoramento é organizacional, a conscientização sobre phishing diz respeito às pessoas, a energia da sala de servidores é física e a autenticação multifator é tecnológica. Ela observa que a ISO/IEC 27002 orienta a implementação, mas não torna por si só uma organização conforme à ISO/IEC 27001, que tem requisitos próprios. O Prof. Hale pede que ela guarde a tabela de correspondência, porque ela vai ajudar a Saltmarsh a preparar sua declaração de aplicabilidade mais adiante no curso.

### 20.3 Recursos do NIST

Lindiwe também estuda os recursos do NIST. O Cybersecurity Framework 2.0 organiza os resultados em seis funções: Governar, Identificar, Proteger, Detectar, Responder e Recuperar. A NIST SP 800-53 Revisão 5 oferece um catálogo detalhado de controles em famílias como controle de acesso e auditoria e responsabilização. A NIST SP 800-12 Revisão 1 apresenta os conceitos de segurança da informação para um público geral. Ela aprende que os frameworks expressam o que alcançar, enquanto os catálogos descrevem os controles em detalhe. Ela mantém uma breve tabela que mostra que recurso responde a que pergunta: frameworks para os resultados, catálogos para os controles detalhados e introduções para a terminologia. O Prof. Hale aprova a tabela.

### 20.4 Escopo

Antes de construir um sistema de gestão, a Saltmarsh precisa definir o escopo: que locais, sistemas e processos estão incluídos. Lindiwe ajuda a redigir um escopo que cobre a sede, todos os depósitos e os sistemas de despacho, da folha de pagamento e de clientes, mas não uma subsidiária administrada separadamente. O Prof. Hale observa que um escopo estreito é mais fácil de certificar, mas pode enganar os clientes, então a declaração de escopo precisa deixar claro o que está excluído e por quê. O rascunho do escopo é revisado pelo diretor-geral e pelo gerente da própria subsidiária, que concorda em aderir depois.

### Exemplo resolvido

Lindiwe situa seu trabalho na ISO/IEC 27001 e na 27002, o relaciona às funções do CSF 2.0 e às famílias da SP 800-53 e redige um escopo para o sistema de gestão da Saltmarsh.

> **Caso sintético.** O escopo é sintético; as normas são parafraseadas.

### Erros e limites

Implementar apenas as orientações da ISO/IEC 27002 não torna uma organização conforme à ISO/IEC 27001.

### Exercícios

- **EX058 — Declaração de aplicabilidade.** O que registra as decisões sobre controles com seus motivos? *Rubrica:* 3 = declaração de aplicabilidade;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX059 — Grupos de controles.** Cite os quatro grupos de controles da ISO/IEC 27002. *Rubrica:* 3 = organizacionais, de pessoas, físicos, tecnológicos;; 2 = todos;; 1 = alguns;; 0 = nenhuma.

- **EX060 — Funções do CSF.** Cite as seis funções do CSF 2.0. *Rubrica:* 3 = Governar, Identificar, Proteger, Detectar, Responder, Recuperar;; 2 = todas;; 1 = algumas;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue estudando — aula 20 (capítulo 20 de 50)

[← Capítulo 19](#ch-19) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Segurança da informação: requisitos

### Objetivos de aprendizagem

Você vai (1) derivar requisitos de segurança a partir de riscos e obrigações; (2) escrever requisitos testáveis; (3) priorizar os requisitos pelo impacto.

### 21.1 Fontes de requisitos

Lindiwe reúne os requisitos de segurança da Saltmarsh a partir de várias fontes: avaliações de risco, contratos com clientes, a lei de proteção de dados, as condições do seguro e o escopo do sistema de gestão. Um grande cliente do varejo exige que os fornecedores usem autenticação multifator para o acesso remoto e relatem incidentes em até vinte e quatro horas. A seguradora exige backups offline testados. Ela registra cada requisito com sua fonte, para que os leitores futuros saibam por que ele existe e se pode mudar caso a fonte mude, por exemplo quando um contrato termina. Ela mantém a lista num registro compartilhado.

### 21.2 Redação testável

Muitos requisitos chegam vagos, como os sistemas devem ser seguros. Lindiwe os reescreve para que um teste possa mostrar aprovação ou reprovação: o acesso remoto aos sistemas internos exige um segundo fator; os discos dos servidores são cifrados; as correções de segurança classificadas como críticas são aplicadas em até catorze dias. O Prof. Hale pede que ela evite palavras como adequado e apropriado, a menos que venham seguidas de um limiar mensurável. Ela aprende que os requisitos testáveis são a ponte entre a política e a verificação, da qual os capítulos posteriores dependem. Cada requisito reescrito também indica seu dono.

### 21.3 Priorizando

Nem todo requisito importa da mesma forma. Lindiwe os ordena pelo impacto da falha, usando as categorias da FIPS 199 vistas antes: os requisitos que protegem sistemas de alto impacto, como a folha de pagamento e o despacho, vêm primeiro. Os requisitos impostos por contratos com multas também ficam no alto. Ela produz uma lista de vinte requisitos em três faixas de prioridade. O líder de segurança a usa para planejar o trabalho do ano, aceitando que os itens das faixas inferiores podem esperar enquanto as lacunas da faixa alta são corrigidas. Ela marca cada requisito com sua faixa e sua fonte no registro, para que o plano possa ser rastreado até os motivos por trás dele.

### 21.4 Conflitos

Os requisitos às vezes entram em conflito. O cliente do varejo quer logs detalhados guardados por um ano; os princípios de proteção de dados empurram para guardar dados pessoais apenas pelo tempo necessário. Lindiwe propõe guardar os logs de segurança por um ano, com acesso restrito à equipe de segurança e com os campos pessoais minimizados sempre que possível. O Prof. Hale observa que resolver os conflitos abertamente, com os motivos registrados, é melhor do que deixar uma equipe ignorar em silêncio um requisito que considera inconveniente. O encarregado de proteção de dados e o líder de segurança assinam a abordagem combinada, e Lindiwe a registra no log de decisões com uma data de revisão.

### Exemplo resolvido

Lindiwe coleta requisitos de riscos, contratos, leis e seguros, os reescreve como declarações testáveis, os ordena em três faixas e resolve um conflito de retenção.

> **Caso sintético.** Os requisitos são sintéticos.

### Erros e limites

Um requisito sem um limiar mensurável não pode ser verificado.

### Exercícios

- **EX061 — Exigências do cliente.** O que o cliente do varejo exige? *Rubrica:* 3 = MFA para acesso remoto e relatos de incidentes em 24 horas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX062 — Requisito de correções.** Com que rapidez as correções críticas devem ser aplicadas? *Rubrica:* 3 = em até catorze dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX063 — Conflito de retenção.** Como se resolve o conflito de retenção de logs? *Rubrica:* 3 = um ano, com acesso restrito e campos minimizados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue estudando — aula 21 (capítulo 21 de 50)

[← Capítulo 20](#ch-20) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Segurança da informação: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) construir um modelo de ativos; (2) conciliar os registros com a realidade observada; (3) atribuir donos aos ativos.

### 22.1 Por que os modelos de ativos importam

As organizações não conseguem proteger o que não sabem que têm. Lindiwe constrói um modelo dos ativos da Saltmarsh: dispositivos, aplicações, repositórios de dados e as relações entre eles. O ponto de partida é o inventário de ativos mantido pela equipe de TI. O Prof. Hale adverte que os inventários se afastam da realidade, à medida que dispositivos são acrescentados sem registro e os antigos permanecem depois de removidos, então o inventário precisa ser conferido contra o que de fato está na rede antes de merecer confiança. Ela pede primeiro à equipe de TI a exportação mais recente do inventário.

### 22.2 O laboratório de conciliação

O laboratório compara um inventário sintético de 2.400 endereços com uma varredura sintética de descoberta que encontrou 2.373 hosts ativos. Noventa endereços registrados não responderam, então podem estar desativados, desligados ou registrados de forma errada. Sessenta e três hosts que responderam não estavam no inventário, todos numa faixa de endereços que ninguém tinha documentado. Dos hosts vistos na rede, 97,3 por cento estavam registrados. Lindiwe observa que as duas lacunas precisam ser investigadas, por motivos diferentes. Ela apresenta os três números numa única tabela para a equipe de rede, com a faixa não registrada destacada para acompanhamento urgente.

### Laboratório — Conciliando um inventário sintético de ativos com uma varredura sintética de descoberta

```python
"""Reconcile a synthetic asset register against a synthetic network discovery scan (stdlib only)."""
import random
random.seed(8)
register = {f"10.20.{i//250}.{i%250+1}" for i in range(2400)}
seen = set(random.sample(sorted(register), 2310))                 # 90 registered hosts not seen
unknown = {f"10.30.0.{i}" for i in range(1, 64)}                   # hosts nobody registered
scan = seen | unknown
print(f"register {len(register)}; scan {len(scan)}")
print(f"registered but not seen {len(register - scan)}; seen but unregistered {len(scan - register)}")
print(f"register coverage of scan {len(scan & register)/len(scan):.1%}")
```

Execute com `python3 lab_assets.py`. Saída verificada:

```text
register 2400; scan 2373
registered but not seen 90; seen but unregistered 63
register coverage of scan 97.3%
```

### 22.3 Investigando as lacunas

Os sessenta e três hosts não registrados importam mais, porque dispositivos desconhecidos ficam sem correções e sem monitoramento. Lindiwe pergunta à equipe de rede sobre a faixa não documentada e descobre que ela pertence ao sistema de câmeras de um depósito, instalado por um terceirizado. Os noventa endereços registrados silenciosos importam menos para o risco imediato, mas minam a confiança no inventário. Ela propõe conferi-los contra os registros de descarte e marcar as desativações confirmadas. O Prof. Hale observa que uma única varredura pode deixar passar dispositivos desligados naquele momento, então as varreduras devem se repetir. A faixa das câmeras é varrida de novo.

### 22.4 Donos

Todo ativo precisa de um dono que decida como ele é protegido e responda por ele. Lindiwe acrescenta um campo de dono ao modelo e descobre que o sistema de câmeras não tem dono nenhum, porque o terceirizado saiu e o gerente do depósito presumiu que a TI era a responsável. Ela providencia para que o gerente do depósito seja o dono, com o apoio da TI. Ela aprende que as lacunas de propriedade muitas vezes explicam as lacunas técnicas, já que ninguém corrige o que não pertence a ninguém. O gerente do depósito assina o registro de propriedade, e o sistema de câmeras é incluído no cronograma de correções.

### Exemplo resolvido

Lindiwe concilia 2.400 endereços registrados com 2.373 hosts varridos, encontra 90 registros silenciosos e 63 câmeras não registradas, investiga ambos e atribui um dono.

> **Caso sintético.** Os endereços são sintéticos; as saídas vêm de lab_assets.py.

### Erros e limites

Um inventário de ativos que nunca é conciliado dá uma falsa confiança.

### Exercícios

- **EX064 — Hosts não registrados.** Quantos hosts foram vistos, mas não estavam registrados? *Rubrica:* 3 = sessenta e três;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX065 — Registros silenciosos.** Quantos endereços registrados não responderam? *Rubrica:* 3 = noventa;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX066 — Dono das câmeras.** Quem se torna o dono do sistema de câmeras? *Rubrica:* 3 = o gerente do depósito;; 2 = parcialmente correto;; 1 = TI;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue estudando — aula 22 (capítulo 22 de 50)

[← Capítulo 21](#ch-21) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Segurança da informação: análise de ameaças e falhas

### Objetivos de aprendizagem

Você vai (1) modelar ameaças de forma sistemática; (2) analisar modos de falha; (3) ligar as ameaças aos controles.

### 23.1 Modelagem de ameaças

Lindiwe modela as ameaças ao sistema de despacho com um método simples: para cada componente e fluxo de dados, perguntar como um atacante poderia falsificar uma identidade, adulterar dados, negar ações, divulgar informações, negar serviço ou obter privilégios. A interface do aplicativo dos motoristas enfrenta falsificação se as credenciais dos motoristas forem roubadas e adulteração se as confirmações puderem ser alteradas. Ela registra cada ameaça com o componente, o atacante provável e os controles existentes, produzindo uma tabela com base na qual os desenvolvedores podem agir. Os desenvolvedores revisam a tabela na próxima reunião de planejamento.

### 23.2 Atacantes

O Prof. Hale pede que ela nomeie atacantes realistas, em vez de imaginar um único adversário todo-poderoso. Para a Saltmarsh, ela lista grupos criminosos em busca de resgate, fraudadores que desviam entregas de mercadorias valiosas, pessoas internas curiosas e erros por descuido. Cada um tem objetivos e habilidades diferentes. Os grupos de resgate visam a disponibilidade e os backups; os fraudadores visam a integridade dos endereços; as pessoas internas visam a confidencialidade dos dados de clientes. Ela aprende que nomear os atacantes afina as prioridades, já que os controles podem ser ajustados às ameaças mais prováveis. Ela anota o tipo de atacante ao lado de cada ameaça na tabela, para maior clareza.

### 23.3 Análise de falhas

Nem todo dano é malicioso. Lindiwe aplica a análise de modos de falha ao despacho: o que acontece se o banco de dados falhar, se a fila de mensagens encher ou se o serviço de mapas ficar indisponível? Para cada caso, ela estima a gravidade e a rapidez com que seria percebido. Uma fila de mensagens cheia atrasaria as confirmações em silêncio, então ninguém perceberia por horas. Ela recomenda monitorar o tamanho da fila. Ela aprende que as análises de segurança e de confiabilidade se sobrepõem, já que as falhas de disponibilidade parecem semelhantes qualquer que seja sua causa. A equipe de operações configura um alerta para quando a fila passar de um tamanho definido.

### 23.4 Ligando aos controles

Lindiwe liga cada ameaça e falha significativa aos controles: o roubo de credenciais à autenticação multifator, a adulteração de endereços a alertas de mudança e aprovações, as falhas da fila ao monitoramento e o ransomware aos backups imutáveis. Algumas ameaças ainda não têm um controle adequado, como as pessoas internas que exportam listas de clientes. Ela as registra como lacunas para o registro de riscos. O Prof. Hale observa que uma lista honesta de lacunas é mais útil do que uma longa lista de controles que dá a entender que nada falta. O líder de segurança acrescenta a lacuna das pessoas internas ao registro de riscos, com um dono.

### Exemplo resolvido

Lindiwe modela as ameaças ao despacho por categoria, nomeia quatro tipos realistas de atacante, analisa modos de falha como uma fila de mensagens cheia e liga as ameaças aos controles e às lacunas.

> **Caso sintético.** As análises são sintéticas.

### Erros e limites

Modelar apenas um adversário poderoso deixa passar as ameaças comuns e mais simples.

### Exercícios

- **EX067 — Alvo dos fraudadores.** O que os fraudadores visam? *Rubrica:* 3 = a integridade dos endereços de entrega;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX068 — Falha silenciosa.** Que falha passaria despercebida por horas? *Rubrica:* 3 = uma fila de mensagens cheia;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX069 — Lacuna aberta.** Que ameaça não tem um controle adequado? *Rubrica:* 3 = pessoas internas que exportam listas de clientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue estudando — aula 23 (capítulo 23 de 50)

[← Capítulo 22](#ch-22) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Segurança da informação: métodos I

### Objetivos de aprendizagem

Você vai (1) planejar uma avaliação de segurança; (2) coletar evidências de forma sistemática; (3) separar as observações das conclusões.

### 24.1 Planejando uma avaliação

Lindiwe planeja sua primeira avaliação formal de um depósito. Ela escreve o escopo, os objetivos, os métodos, o cronograma e a autorização, e o gerente do depósito e o líder de segurança a assinam. Os métodos incluem entrevistas, revisão de configurações, uma varredura de rede dentro do segmento do depósito e uma inspeção dos controles físicos. O Prof. Hale ressalta que a autorização escrita protege tanto o avaliador quanto a organização, especialmente nas varreduras que poderiam perturbar equipamentos se executadas sem cuidado. O plano também declara em que horários as varreduras podem rodar, evitando o período movimentado do despacho da manhã, quando os sistemas do depósito carregam sua carga mais pesada.

### 24.2 Coleta de evidências

Durante a avaliação, Lindiwe registra as evidências com horário, fonte e método: capturas de tela das configurações, saídas das varreduras e anotações de entrevistas assinadas pelos entrevistados. Ela guarda as evidências numa pasta restrita, com somas de verificação, para que os leitores futuros possam confirmar que nada mudou. Ela aprende que as conclusões são tão fortes quanto as evidências por baixo delas, e que registrar como as evidências foram obtidas permite que outros julguem sua confiabilidade e repitam as verificações. Ela lista cada item de evidência num índice com sua soma de verificação, para que um revisor possa escolher qualquer item e confirmar que corresponde ao registro original.

### 24.3 Observações e conclusões

Lindiwe separa o que observou do que conclui. Ela observou que o drive de backup do depósito fica num escritório destrancado; conclui que os backups poderiam ser roubados ou danificados. Ela observou que dois funcionários compartilham um login no terminal de recebimento de mercadorias; conclui que as ações ali não podem ser atribuídas. O Prof. Hale explica que essa separação permite que os leitores aceitem os fatos mesmo que pesem as conclusões de forma diferente. Ela aplica esse formato a cada achado do relatório. O gerente do depósito diz depois que a separação tornou os achados mais fáceis de aceitar e de pôr em prática.

### 24.4 Relatório

O relatório dela lista oito achados, cada um com evidência, conclusão, classificação de risco e recomendação. Ela compartilha um rascunho com o gerente do depósito, que corrige um erro factual: uma porta que ela pensava estar destrancada tem uma fechadura com código que ela não tinha visto. Ela revisa o achado. Ela aprende que conferir os fatos com os responsáveis melhora a exatidão e a aceitação, e que defender um erro para proteger o próprio relatório prejudica a credibilidade. O relatório final vai para o líder de segurança e para o gerente do depósito. Em um mês, seis dos oito achados estão encerrados, e os dois restantes têm datas combinadas.

### Exemplo resolvido

Lindiwe planeja e autoriza uma avaliação de depósito, registra as evidências com somas de verificação, separa as observações das conclusões e corrige um erro factual depois da revisão.

> **Caso sintético.** A avaliação é sintética.

### Erros e limites

Misturar observações com conclusões torna os relatórios mais difíceis de verificar.

### Exercícios

- **EX070 — Plano assinado.** Quem assina o plano de avaliação? *Rubrica:* 3 = o gerente do depósito e o líder de segurança;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX071 — Integridade das evidências.** Como ela protege a integridade das evidências? *Rubrica:* 3 = somas de verificação numa pasta restrita;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX072 — Erro corrigido.** Que erro factual é corrigido? *Rubrica:* 3 = uma porta com fechadura com código que ela não tinha visto;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue estudando — aula 24 (capítulo 24 de 50)

[← Capítulo 23](#ch-23) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) projetar uma melhoria de segurança sob restrições; (2) apresentar opções às partes interessadas; (3) iterar um projeto a partir da crítica.

### 25.1 O briefing

O briefing do ateliê de projeto pede que a equipe de Lindiwe proteja o acesso remoto dos supervisores dos depósitos da Saltmarsh, que hoje se conectam de casa usando apenas senhas. As restrições incluem um orçamento pequeno, supervisores com pouca experiência técnica e a exigência de segundo fator do cliente do varejo. A equipe precisa entregar um projeto, uma estimativa de custo e um plano de implantação em seis semanas. O Prof. Hale faz o papel do cliente e questiona cada pressuposto da equipe. A equipe tem quatro membros, cada um liderando uma parte do trabalho: projeto, custo, implantação e documentação.

### 25.2 Opções

A equipe desenvolve três opções: uma rede privada virtual com códigos por aplicativo, um portal web com chaves de hardware e um serviço gerenciado de área de trabalho remota com autenticação multifator embutida. Eles comparam custo, segurança, facilidade de uso e carga de suporte. O portal com chaves de hardware resiste melhor ao phishing, mas exige enviar as chaves aos supervisores pelo correio. A rede privada virtual é familiar, mas dá acesso amplo à rede depois de conectada, o que conflita com o privilégio mínimo. A equipe registra as notas de cada opção numa tabela compartilhada, para que o cliente veja como cada julgamento foi alcançado.

### 25.3 Crítica

Na revisão de meio de percurso, o Prof. Hale pergunta o que acontece quando um supervisor perde uma chave numa sexta-feira à noite. A equipe não tem resposta. Eles acrescentam um processo de recuperação que usa uma segunda chave registrada guardada em casa e uma ligação verificada para a central de atendimento. Os colegas também apontam que a opção de área de trabalho remota depende de um único fornecedor. A equipe registra esses pontos e revisa as notas de cada opção. Eles também entrevistam dois supervisores sobre a configuração que têm em casa e descobrem que um deles compartilha o computador com familiares.

### 25.4 Projeto final

A equipe recomenda o portal web com duas chaves de hardware por supervisor, acesso apenas às aplicações de que os supervisores precisam e um processo de recuperação documentado. Eles estimam o custo por supervisor e uma implantação de quatro semanas, depósito por depósito. O Prof. Hale elogia o processo de recuperação como a parte que a maioria dos projetos esquece. Lindiwe reflete que a crítica melhorou o projeto mais do que qualquer escolha técnica isolada, porque expôs situações que ninguém tinha imaginado. O cliente aceita o projeto, e o líder de segurança da Saltmarsh pede para usar o processo de recuperação como modelo para outros serviços.

### Exemplo resolvido

A equipe de Lindiwe compara três opções de acesso remoto, acrescenta um processo de recuperação depois da crítica e recomenda um portal com duas chaves de hardware por supervisor.

> **Caso sintético.** O briefing do ateliê é sintético.

### Erros e limites

Um projeto de autenticação forte sem um processo de recuperação falha na primeira chave perdida.

### Exercícios

- **EX073 — Restrições do ateliê.** Cite uma restrição do briefing. *Rubrica:* 3 = orçamento pequeno;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX074 — Desvantagem da VPN.** Que desvantagem a opção de VPN tem? *Rubrica:* 3 = acesso amplo à rede depois de conectada;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX075 — Processo de recuperação.** Que processo de recuperação é acrescentado? *Rubrica:* 3 = segunda chave em casa e ligação verificada;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue estudando — aula 25 (capítulo 25 de 50)

[← Capítulo 24](#ch-24) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Segurança da informação: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar arquiteturas de perímetro e centradas na identidade; (2) avaliar opções em nuvem e locais; (3) escolher uma arquitetura com os motivos registrados.

### 26.1 Modelos de perímetro

A arquitetura tradicional da Saltmarsh confia nos dispositivos dentro da rede e defende a borda com firewalls. Lindiwe observa que esse modelo se enfraquece quando os funcionários trabalham remotamente, as aplicações vão para serviços em nuvem e os atacantes entram por phishing. Uma vez dentro, um atacante herda a confiança. O Prof. Hale explica que o perímetro continua útil, mas já não é suficiente, porque a linha entre dentro e fora se tornou difusa para a maioria das organizações. Lindiwe ilustra isso com um incidente sintético em que um notebook vítima de phishing na rede interna alcançou um compartilhamento de arquivos com exportações da folha de pagamento, porque nada dentro do firewall conferia quem estava pedindo.

### 26.2 Modelos centrados na identidade

Uma alternativa confere a identidade, a saúde do dispositivo e o contexto de cada pedido, independentemente da localização na rede. Lindiwe esboça como a aplicação de despacho da Saltmarsh funcionaria: cada pedido é autenticado, o dispositivo é conferido quanto às correções em dia e o acesso é limitado à função do usuário. Essa abordagem segue o princípio da mediação completa de Saltzer e Schroeder. Ela observa que isso exige um gerenciamento de identidades maduro, um inventário de dispositivos e registro de logs, que a Saltmarsh tem apenas em parte. Ela lista as capacidades que faltam: um inventário completo de dispositivos, um relato consistente da saúde dos dispositivos e o registro de cada decisão de acesso às aplicações.

### 26.3 Nuvem e local

A Saltmarsh está considerando levar a folha de pagamento para um serviço em nuvem. Lindiwe compara as responsabilidades de segurança: o provedor protege sua infraestrutura, enquanto a Saltmarsh continua responsável pelas contas de usuário, pela configuração e pelos dados. Ela lista perguntas ao provedor sobre cifração, registro de logs, certificações e notificação de incidentes. O Prof. Hale adverte que os serviços em nuvem deslocam as responsabilidades, mas não as eliminam, e que armazenamentos em nuvem mal configurados causaram muitas exposições. Ela redige o questionário para o provedor com doze perguntas, e a equipe de compras concorda em enviá-lo com os documentos da licitação.

### 26.4 Escolhendo

Lindiwe recomenda uma abordagem em etapas: manter a segmentação e os firewalls, colocar primeiro as aplicações de alto valor atrás de um acesso ciente da identidade e avaliar a folha de pagamento em nuvem com uma revisão contratual. Ela registra a decisão com os motivos: a redução do risco no acesso remoto, a viabilidade diante da maturidade atual da identidade e o custo. O Prof. Hale observa que as escolhas de arquitetura raramente são de tudo ou nada, e que um caminho em etapas permite que a organização construa as capacidades que cada etapa exige. O diretor-geral aprova a primeira etapa, começando pelo despacho e pela folha de pagamento. Lindiwe marca uma revisão depois de seis meses para decidir se a próxima etapa deve prosseguir.

### Exemplo resolvido

Lindiwe compara os modelos de perímetro e centrados na identidade, lista as responsabilidades compartilhadas da folha de pagamento em nuvem e recomenda uma transição em etapas com os motivos registrados.

> **Caso sintético.** As arquiteturas são sintéticas.

### Erros e limites

Ir para um serviço em nuvem não transfere a responsabilidade pelas contas e pela configuração.

### Exercícios

- **EX076 — Fraqueza do perímetro.** Por que o modelo de perímetro é insuficiente? *Rubrica:* 3 = os atacantes dentro herdam a confiança;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX077 — Ligação com a mediação.** Que princípio a verificação centrada na identidade segue? *Rubrica:* 3 = mediação completa;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX078 — Responsabilidade na nuvem.** O que continua sendo responsabilidade da Saltmarsh na nuvem? *Rubrica:* 3 = contas, configuração e dados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue estudando — aula 26 (capítulo 26 de 50)

[← Capítulo 25](#ch-25) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Segurança da informação: projeto de controles

### Objetivos de aprendizagem

Você vai (1) projetar controles preventivos, de detecção e corretivos; (2) especificar a operação do controle e suas evidências; (3) avaliar o custo e a eficácia dos controles.

### 27.1 Projetando um controle

Lindiwe projeta um controle para as mudanças de endereço no despacho, em resposta à ameaça de fraude identificada antes. Parte preventiva: as mudanças de endereço de entrega dos pedidos de alto valor exigem a aprovação de uma segunda pessoa. Parte de detecção: um alerta dispara quando um endereço muda menos de uma hora antes do despacho. Parte corretiva: as mudanças suspeitas são revertidas e o cliente é contatado. O Prof. Hale pede que ela especifique quem opera cada parte e que evidência mostra que ela foi executada. Ela escreve o projeto como uma descrição de controle de uma página, com dono, frequência e evidência.

### 27.2 Evidências de operação

Um controle que não consegue mostrar que foi executado não pode ser auditado. Lindiwe especifica as evidências: registros de aprovação com os dois nomes e os horários, logs de alertas com anotações do tratamento e uma revisão mensal por amostragem feita pelo líder de segurança. Ela observa que a ISO/IEC 27001 espera que as organizações monitorem e meçam seus controles, então as evidências não são opcionais. Ela aprende a projetar a coleta de evidências dentro do controle desde o início, em vez de reconstruí-la antes de uma auditoria. O líder de segurança concorda em fazer a revisão mensal por amostragem e registrar quaisquer exceções encontradas.

### 27.3 Custo e atrito

A aprovação por uma segunda pessoa atrasa os pedidos urgentes. Lindiwe aplica o controle apenas aos pedidos acima de um limite de valor, fixado onde a perda por fraude superaria o custo do atraso. Ela estima que cerca de cinco por cento dos pedidos o ultrapassam. O Prof. Hale observa que os controles aplicados a tudo muitas vezes são contornados, enquanto os controles direcionados continuam sustentáveis. Ela registra o limite e seu raciocínio para que ele possa ser ajustado à medida que os padrões de fraude mudarem. O gerente de operações concorda com o limite depois de ver a estimativa e pede uma revisão após três meses de operação.

### 27.4 Eficácia

Lindiwe propõe medir a eficácia: quantas mudanças suspeitas o alerta pega, quantas aprovações são rejeitadas e se as perdas por fraude caem. Ela observa que os eventos raros tornam a eficácia difícil de medir rapidamente, então ela também vai testar o controle encenando mudanças suspeitas sintéticas e conferindo se os alertas disparam. Ela aprende que testar com casos plantados dá evidências mesmo quando os ataques reais são raros demais para contar. Ela planeja encenar uma mudança suspeita sintética por mês e registrar se o alerta disparou e com que rapidez foi tratado.

### Exemplo resolvido

Lindiwe projeta um controle em camadas para as mudanças de endereço, especifica suas evidências, o direciona aos pedidos de alto valor e planeja testá-lo com casos plantados.

> **Caso sintético.** Os controles são sintéticos.

### Erros e limites

Um controle que não deixa evidências não pode ser mostrado em funcionamento.

### Exercícios

- **EX079 — Parte preventiva.** Qual é a parte preventiva do controle de endereços? *Rubrica:* 3 = aprovação por uma segunda pessoa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX080 — Parcela direcionada.** Aproximadamente que parcela dos pedidos ultrapassa o limite? *Rubrica:* 3 = cerca de cinco por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX081 — Testes plantados.** Como o controle é testado apesar da raridade das fraudes? *Rubrica:* 3 = encenando mudanças suspeitas sintéticas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue estudando — aula 27 (capítulo 27 de 50)

[← Capítulo 26](#ch-26) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Segurança da informação: implementação I

### Objetivos de aprendizagem

Você vai (1) implementar linhas de base de configuração; (2) medir a conformidade automaticamente; (3) priorizar a correção a partir dos resultados.

### 28.1 Linhas de base

Lindiwe transforma a lista de verificação de endurecimento vista antes numa linha de base que pode ser conferida automaticamente. Ela escolhe três regras para a primeira versão: login remoto de root desativado, correções de segurança com no máximo trinta dias e discos cifrados. Cada regra é escrita de modo que um script possa ler a configuração e devolver aprovação ou reprovação. O Prof. Hale aconselha começar com poucas regras que importam, em vez de centenas que sobrecarregam as equipes que recebem os resultados. As equipes de servidores revisam as três regras antes da primeira execução.

### 28.2 O laboratório da linha de base

O laboratório confere um conjunto sintético de 300 servidores. O login remoto de root está desativado em 278 servidores, 92,7 por cento. As correções têm no máximo trinta dias em 253, 84,3 por cento. Os discos estão cifrados em 277, 92,3 por cento. Apenas 216 servidores, 72,0 por cento, passam nas três regras. Lindiwe observa que cada regra sozinha parece razoavelmente boa, mas o número combinado mostra que mais de um quarto dos servidores falha em pelo menos um requisito. Ela compartilha os resultados com cada equipe de servidores, junto com a lista dos seus servidores reprovados, para que as equipes possam começar a trabalhar de imediato, em vez de esperar um relatório formal.

### Laboratório — Conferindo 300 configurações sintéticas de servidores contra três regras de linha de base

```python
"""Check synthetic server configurations against three hardening baseline rules (stdlib only)."""
import random
random.seed(29)
servers = []
for i in range(300):
    servers.append({
        "ssh_root_login": random.random() < 0.06,      # True = permitted (fail)
        "patch_age_days": int(random.expovariate(1/18)),
        "disk_encrypted": random.random() < 0.93,
    })
r1 = sum(not s["ssh_root_login"] for s in servers)
r2 = sum(s["patch_age_days"] <= 30 for s in servers)
r3 = sum(s["disk_encrypted"] for s in servers)
allp = sum((not s["ssh_root_login"]) and s["patch_age_days"] <= 30 and s["disk_encrypted"] for s in servers)
n = len(servers)
print(f"root login disabled {r1}/{n} ({r1/n:.1%}); patched within 30 days {r2}/{n} ({r2/n:.1%}); disk encrypted {r3}/{n} ({r3/n:.1%})")
print(f"all three rules {allp}/{n} ({allp/n:.1%})")
```

Execute com `python3 lab_baseline.py`. Saída verificada:

```text
root login disabled 278/300 (92.7%); patched within 30 days 253/300 (84.3%); disk encrypted 277/300 (92.3%)
all three rules 216/300 (72.0%)
```

### 28.3 Priorizando a correção

Lindiwe ordena as falhas pela categoria do servidor. Os servidores dos sistemas de alto impacto, como a folha de pagamento, vêm primeiro, depois os expostos à internet. Dentro de cada grupo, ela corrige primeiro os itens mais rápidos: desativar o login de root leva minutos, enquanto cifrar um disco existente exige uma parada. O Prof. Hale observa que combinar o impacto com o esforço produz um plano que as equipes podem seguir semana a semana, em vez de uma única lista grande que desestimula a ação. As equipes concordam em fechar todas as falhas de login de root em uma semana e planejar a cifração ao longo do próximo trimestre.

### 28.4 Mantendo a conformidade

A conformidade medida uma única vez se deteriora. Lindiwe agenda a verificação para rodar semanalmente e relatar a porcentagem que passa em todas as regras, separada por equipe. Ela acrescenta novas regras gradualmente, cada uma anunciada com antecedência. As equipes podem ver a própria tendência. Ela aprende que uma medição automatizada e repetida transforma uma linha de base de documento em controle em operação, e que a transparência sobre os resultados de cada equipe estimula a melhoria sem precisar de uma auditoria formal. Depois de três meses, ela planeja comparar a tendência de cada equipe com o número inicial de 72,0 por cento e relatar o progresso ao líder de segurança.

### Exemplo resolvido

Lindiwe implementa três regras de linha de base, descobre que 72,0 por cento dos 300 servidores passam nas três, prioriza pelo impacto e pelo esforço e agenda verificações semanais.

> **Caso sintético.** Os servidores são sintéticos; as saídas vêm de lab_baseline.py.

### Erros e limites

Relatar cada regra sozinha pode esconder quantos servidores falham em pelo menos uma.

### Exercícios

- **EX082 — Taxa do login de root.** Que parcela tem o login remoto de root desativado? *Rubrica:* 3 = 278, 92,7 por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX083 — Taxa de correções.** Que parcela está corrigida dentro de trinta dias? *Rubrica:* 3 = 253, 84,3 por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX084 — As três.** Quantos servidores passam nas três regras? *Rubrica:* 3 = 216, 72,0 por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue estudando — aula 28 (capítulo 28 de 50)

[← Capítulo 27](#ch-27) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Segurança da informação: medição

### Objetivos de aprendizagem

Você vai (1) projetar uma medida de detecção; (2) distinguir padrões de ataque de ruído benigno; (3) relatar os resultados de detecção com honestidade.

### 29.1 Medindo a adivinhação de senhas

A Saltmarsh quer saber com que frequência as contas enfrentam adivinhação de senhas. Lindiwe define uma medida: uma conta é sinalizada se tiver dez ou mais falhas de login em qualquer janela de cinco minutos. Os erros comuns de digitação produzem algumas falhas espalhadas ao longo do dia, enquanto a adivinhação produz muitas em rápida sucessão. Ela escolhe a janela e o limiar antes de olhar os dados e os registra para que os resultados futuros possam ser comparados com a mesma definição. O líder de segurança aprova a definição antes que Lindiwe a execute sobre quaisquer dados.

### 29.2 O laboratório dos logins

O laboratório monta um dia sintético de 1.672 falhas de login em 863 contas. Três contas são sinalizadas: u17, u402 e u977, com 40, 42 e 40 falhas, respectivamente, todas em rajadas curtas. A conta com mais falhas no total, u1200, tem 61, mas elas estão espalhadas a cada poucos minutos ao longo do dia, então ela não é sinalizada. Lindiwe investiga e descobre um cliente de sincronização quebrado que tenta de novo com uma senha antiga. Ela registra a explicação ao lado da conta no relatório, para que ninguém confunda as falhas do cliente com um ataque. A central de atendimento confirma que a usuária tinha trocado a senha na semana anterior.

### Laboratório — Detectando rajadas de adivinhação de senhas num log sintético de autenticação

```python
"""Detect password-guessing bursts in a synthetic authentication log (stdlib only)."""
import random
from collections import defaultdict
random.seed(5)
events = []
for u in range(1500):                                  # ordinary mistyping
    for _ in range(random.choice([0, 0, 0, 1, 1, 2, 3])):
        events.append((f"u{u}", random.uniform(0, 86400)))
for u in ["u17", "u402", "u977"]:                      # guessing bursts
    start = random.uniform(0, 80000)
    events += [(u, start + random.uniform(0, 240)) for _ in range(40)]
for u in ["u1200"]:                                    # a broken sync client retrying slowly
    events += [(u, k * 400.0) for k in range(60)]
by = defaultdict(list)
for u, t in events: by[u].append(t)
flag = []
for u, ts in by.items():
    ts.sort()
    if any(ts[j + 9] - ts[j] <= 300 for j in range(len(ts) - 9)):
        flag.append(u)
total = sorted(by, key=lambda u: -len(by[u]))[:4]
print(f"failed logins {len(events)}; accounts with failures {len(by)}")
print(f"flagged (10 failures within 5 min): {sorted(flag)}")
print(f"top accounts by total failures: {[(u, len(by[u])) for u in total]}")
```

Execute com `python3 lab_logins.py`. Saída verificada:

```text
failed logins 1672; accounts with failures 863
flagged (10 failures within 5 min): ['u17', 'u402', 'u977']
top accounts by total failures: [('u1200', 61), ('u402', 42), ('u17', 40), ('u977', 40)]
```

### 29.3 Por que a taxa supera o total

Ordenar as contas pelo total de falhas teria posto o cliente quebrado em primeiro lugar e o misturado com a adivinhação real. A medida por janela separa a adivinhação rápida das novas tentativas lentas. Lindiwe observa que os atacantes também podem adivinhar devagar para evitar a detecção, então a medida pega os ataques ruidosos, mas não os pacientes. Ela acrescenta um segundo indicador, mais fraco: contas com falhas vindas de muitos endereços diferentes num dia. O Prof. Hale valoriza que ela declare o que a medida não consegue ver. Ela documenta os dois indicadores juntos numa breve nota.

### 29.4 Relatando

Lindiwe relata as três contas sinalizadas à equipe de segurança, que redefine suas senhas e confirma que a autenticação multifator está ativada. Ela também relata o cliente quebrado à central de atendimento, que o corrige. Seu relatório mensal mostra o número de contas sinalizadas, a definição usada e seu ponto cego conhecido. Ela aprende que uma medida só é útil quando sua definição e seus limites acompanham o número. O líder de segurança distribui o relatório aos gerentes de TI todo mês, e a definição é acrescentada ao manual de métricas de segurança.

### Exemplo resolvido

Lindiwe sinaliza três contas com rajadas de 40 a 42 falhas entre 1.672 falhas de login, separa um cliente que tenta de novo devagar com 61 falhas e relata a medida com seu ponto cego.

> **Caso sintético.** Os logs são sintéticos; as saídas vêm de lab_logins.py.

### Erros e limites

Ordenar pelo total de falhas confunde clientes quebrados com ataques.

### Exercícios

- **EX085 — Contas sinalizadas.** Que contas são sinalizadas? *Rubrica:* 3 = u17, u402 e u977;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX086 — Conta do topo.** Por que u1200 não é sinalizada? *Rubrica:* 3 = falhas espalhadas ao longo do dia;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX087 — Ponto cego.** O que a medida por janela deixa passar? *Rubrica:* 3 = a adivinhação lenta e paciente;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue estudando — aula 29 (capítulo 29 de 50)

[← Capítulo 28](#ch-28) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) verificar controles com testes planejados; (2) registrar as evidências dos testes; (3) distinguir a falha de um teste da falha de um controle.

### 30.1 Plano de testes

No laboratório de verificação, Lindiwe escreve um plano de testes para quatro controles que ajudou a construir: a verificação da linha de base, a medida de adivinhação de senhas, o alerta de mudança de endereço e a conciliação de ativos. Para cada um, ela define as entradas, os resultados esperados e os critérios de aprovação. A verificação da linha de base deve reprovar um servidor plantado com o login de root ativado; a medida de adivinhação deve sinalizar uma rajada plantada de dez falhas em quatro minutos. O Prof. Hale aprova o plano antes do início dos testes. Cada teste é listado numa única tabela com sua entrada plantada e o resultado esperado.

### 30.2 Executando os testes

Lindiwe executa os testes sobre dados sintéticos. A verificação da linha de base reprova corretamente o servidor plantado. A medida de adivinhação sinaliza a rajada plantada e ignora uma sequência lenta plantada, como pretendido. O alerta de endereço dispara para uma mudança plantada uma hora antes do despacho. A conciliação de ativos lista corretamente um host não registrado plantado. Ela registra cada execução com a data, as entradas, as saídas e a versão de cada script, para que os resultados possam ser reproduzidos. Os quatro controles passam nos seus primeiros casos planejados. Ela guarda as entradas plantadas junto com os scripts.

### 30.3 Um teste reprovado

Um teste falha: uma rajada plantada de exatamente dez falhas que abrange precisamente cinco minutos não é sinalizada. Lindiwe examina o código e descobre que a comparação trata o limite de forma incoerente com sua definição escrita. Ela corrige o código, executa de novo todos os testes e confirma que o caso plantado agora é sinalizado e que os resultados anteriores não mudaram. O Prof. Hale observa que os casos-limite são onde as definições e o código mais costumam discordar. Ela acrescenta o caso-limite ao conjunto permanente de testes, para que o mesmo erro seja pego de novo. A correção é uma única comparação alterada.

### 30.4 Teste versus controle

Lindiwe reflete sobre o que o teste reprovado significou. O controle em si, detectar a adivinhação, era sólido; a implementação tinha um erro de limite. Se o teste não existisse, um ataque real exatamente no limite teria passado despercebido. Ela escreve no relatório do laboratório que os testes verificam as implementações contra as definições, e que manter os casos de teste plantados de forma permanente permite conferir rapidamente as mudanças futuras. O Prof. Hale pede que ela apresente esse exemplo à turma, porque ele mostra com clareza por que a verificação precisa de casos planejados em cada limite, e não apenas de entradas típicas.

### Exemplo resolvido

Lindiwe testa quatro controles com casos plantados, encontra um erro de limite na medida de adivinhação, o corrige e executa de novo todos os testes.

> **Caso sintético.** Os testes são sintéticos.

### Erros e limites

Os casos-limite não testados muitas vezes revelam discordância entre a definição e o código.

### Exercícios

- **EX088 — Rajada plantada.** Que rajada plantada deve ser sinalizada? *Rubrica:* 3 = dez falhas em quatro minutos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX089 — Teste reprovado.** Que caso plantado falhou no início? *Rubrica:* 3 = dez falhas abrangendo exatamente cinco minutos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX090 — Testes permanentes.** Por que manter os casos plantados de forma permanente? *Rubrica:* 3 = para conferir rapidamente as mudanças futuras;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue estudando — aula 30 (capítulo 30 de 50)

[← Capítulo 29](#ch-29) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Segurança da informação: implementação II

### Objetivos de aprendizagem

Você vai (1) implantar a autenticação multifator em escala; (2) gerenciar exceções; (3) acompanhar a adoção em relação a um plano.

### 31.1 Plano de implantação

No quarto ano, Lindiwe ajuda a implementar o plano de autenticação multifator aprovado antes. Os administradores vêm primeiro, com chaves físicas; depois a equipe de escritório, com códigos de aplicativo; depois a equipe do armazém, que compartilha terminais e precisa de outra abordagem. Ela escreve um cronograma por depósito, com sessões de treinamento, preparação da central de atendimento e uma data a partir da qual as senhas sozinhas deixam de funcionar. O Prof. Hale pede que ela planeje a comunicação com o mesmo cuidado que a configuração, porque usuários surpreendidos geram chamados de suporte e soluções de contorno. O líder de segurança aprova o cronograma e as datas de treinamento.

### 31.2 Terminais do armazém

A equipe do armazém usa terminais compartilhados com luvas nas mãos, então as notificações no celular são pouco práticas. A equipe de Lindiwe testa logins de curta duração por aproximação do crachá, combinados com um código pessoal, de modo que cada pessoa seja identificada individualmente e as contas compartilhadas desapareçam. O depósito de teste relata logins mais rápidos do que com a antiga senha compartilhada. Ela aprende que as melhorias de segurança que também eliminam atrito se espalham depressa, enquanto as que acrescentam atrito precisam de uma justificativa forte e de apoio para serem aceitas por uma equipe ocupada. Os leitores de crachá são instalados em todos os terminais do armazém ao longo dos dois meses seguintes.

### 31.3 Exceções

Algumas contas não conseguem usar a autenticação multifator de imediato: uma integração antiga de scanner e duas contas de serviço usadas por fornecedores. Lindiwe registra cada exceção com um dono, um motivo, controles compensatórios, como restrições de rede, e uma data de expiração. O Prof. Hale explica que as exceções sem data de expiração se tornam fraquezas permanentes. Ela programa lembretes três semanas antes de cada expiração, para que os donos tenham de resolver o problema ou justificar uma prorrogação ao líder de segurança. A exceção da integração do scanner é encerrada após três meses, quando o fornecedor entrega uma atualização com suporte a certificados.

### 31.4 Acompanhando a adoção

Lindiwe acompanha a adoção semanalmente: a parcela de contas cadastradas, a parcela de logins que usam um segundo fator e o número de exceções abertas. A adoção entre os administradores chega a todas as contas na primeira quinzena, a equipe de escritório acompanha ao longo de dois meses e os depósitos do armazém avançam um de cada vez. Ela relata o progresso em relação ao plano ao líder de segurança. Ela observa que contar apenas os cadastros poderia enganar, já que os usuários cadastrados ainda poderiam entrar com os métodos antigos até que estes sejam desativados. A desativação dos métodos antigos vem em seguida.

### Exemplo resolvido

Lindiwe implanta a autenticação multifator em fases, por grupo, usa a aproximação do crachá nos terminais do armazém, registra as exceções com datas de expiração e acompanha tanto os cadastros quanto o uso real do segundo fator.

> **Caso sintético.** A implantação é sintética.

### Erros e limites

As exceções sem data de expiração se tornam fraquezas permanentes.

### Exercícios

- **EX091 — Ordem de implantação.** Que grupo vem primeiro? *Rubrica:* 3 = os administradores, com chaves físicas;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX092 — Método do armazém.** Como a equipe do armazém faz login? *Rubrica:* 3 = aproximação do crachá com um código pessoal;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX093 — Medidas de adoção.** Que três medidas de adoção são acompanhadas? *Rubrica:* 3 = parcela cadastrada, logins com segundo fator, exceções abertas;; 2 = todas;; 1 = algumas;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-31 -->
### Continue estudando — aula 31 (capítulo 31 de 50)

[← Capítulo 30](#ch-30) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Segurança da informação: confiabilidade

### Objetivos de aprendizagem

Você vai (1) verificar a integridade dos backups com somas de verificação; (2) medir o sucesso das restaurações; (3) definir objetivos de recuperação.

### 32.1 Restaurações como evidência

A Saltmarsh acredita que seus backups funcionam porque as rotinas de backup relatam sucesso. Lindiwe explica que uma rotina de backup bem-sucedida mostra que os dados foram copiados, não que podem ser restaurados intactos. Ela propõe testes regulares de restauração que comparem os arquivos restaurados com as somas de verificação registradas no momento do backup. Se um arquivo estiver faltando ou sua soma de verificação for diferente, a restauração falhou para aquele arquivo. O Prof. Hale observa que somente os testes de restauração dão evidências para a exigência da seguradora de backups testados. O líder de segurança agenda o primeiro teste de restauração para o mês seguinte.

### 32.2 O laboratório da restauração

O laboratório cria 500 arquivos sintéticos, registra uma soma de verificação SHA-256 para cada um usando o módulo hashlib do Python e simula uma restauração. Cinco arquivos estão faltando na restauração e três têm somas de verificação divergentes, causadas por um único bit invertido. Isso deixa 492 arquivos verificados, 98,4 por cento. Lindiwe observa que a rotina de backup teria relatado sucesso e que, sem as somas de verificação, os três arquivos corrompidos pareceriam normais até alguém abri-los. Ela mostra ao líder de segurança a lista dos arquivos faltantes e corrompidos, e a equipe concorda em executar a mesma verificação mensalmente, sobre uma amostra rotativa de pastas de todos os servidores.

### Laboratório — Verificando restaurações sintéticas de backup contra somas de verificação SHA-256

```python
"""Verify synthetic backup restores against SHA-256 checksums (stdlib only)."""
import hashlib, random
random.seed(12)
files = {f"file{i}": random.randbytes(256) for i in range(500)}
manifest = {k: hashlib.sha256(v).hexdigest() for k, v in files.items()}
restored = {}
for k, v in files.items():
    r = random.random()
    if r < 0.006: continue                                    # missing from restore
    if r < 0.014: v = v[:-1] + bytes([v[-1] ^ 1])            # one bit flipped
    restored[k] = v
missing = [k for k in files if k not in restored]
bad = [k for k in restored if hashlib.sha256(restored[k]).hexdigest() != manifest[k]]
ok = len(files) - len(missing) - len(bad)
print(f"files {len(files)}; missing {len(missing)}; checksum mismatch {len(bad)}; verified {ok} ({ok/len(files):.1%})")
```

Execute com `python3 lab_restore.py`. Saída verificada:

```text
files 500; missing 5; checksum mismatch 3; verified 492 (98.4%)
```

### 32.3 Investigando as falhas

Lindiwe rastreia os cinco arquivos faltantes até uma pasta acrescentada depois que a seleção do backup foi configurada, de modo que ela nunca foi incluída. Os três arquivos corrompidos vêm de um disco com defeito no servidor de backup. As duas causas têm correção: a seleção é alterada para incluir todas as pastas sob uma pasta-mãe, e o disco é substituído. Ela aprende que os testes de restauração encontram problemas de configuração e de hardware que o monitoramento das rotinas de backup, sozinho, não consegue revelar. O teste mensal de restauração seguinte, executado depois das duas correções, verifica todos os arquivos da sua amostra.

### 32.4 Objetivos de recuperação

Lindiwe ajuda a Saltmarsh a definir objetivos de recuperação: quantos dados o negócio pode se permitir perder e com que rapidez cada sistema precisa voltar. O despacho pode perder no máximo uma hora de dados e precisa voltar em até quatro horas; a folha de pagamento pode perder um dia, mas precisa estar de volta antes do processamento dos pagamentos. Esses objetivos determinam a frequência dos backups e os métodos de restauração. O Prof. Hale observa que os objetivos acordados com os donos do negócio transformam os backups de um hábito técnico num compromisso. Os objetivos são aprovados pelo diretor de operações e pelo diretor financeiro.

### Exemplo resolvido

Lindiwe verifica uma restauração sintética de 500 arquivos com somas de verificação SHA-256, encontra 5 faltantes e 3 corrompidos (492 verificados, 98,4 por cento), rastreia as causas e define objetivos de recuperação.

> **Caso sintético.** Os arquivos são sintéticos; as saídas vêm de lab_restore.py.

### Erros e limites

Uma rotina de backup bem-sucedida não prova que os dados podem ser restaurados intactos.

### Exercícios

- **EX094 — Números da restauração.** Quantos arquivos foram verificados? *Rubrica:* 3 = 492, 98,4 por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX095 — Causa dos faltantes.** Por que cinco arquivos estavam faltando? *Rubrica:* 3 = uma pasta acrescentada depois que a seleção foi configurada;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX096 — Objetivos do despacho.** Quais são os objetivos de recuperação do despacho? *Rubrica:* 3 = perder no máximo uma hora, voltar em até quatro horas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-32 -->
### Continue estudando — aula 32 (capítulo 32 de 50)

[← Capítulo 31](#ch-31) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Segurança da informação: segurança e resiliência

### Objetivos de aprendizagem

Você vai (1) planejar a continuidade da operação durante incidentes; (2) projetar alternativas manuais; (3) exercitar planos de resiliência.

### 33.1 Resiliência

Resiliência significa continuar o trabalho essencial durante uma interrupção e se recuperar rapidamente. Lindiwe pergunta aos gerentes de operações da Saltmarsh o que precisa continuar se os sistemas falharem: as entregas de medicamentos refrigerados, a folha de pagamento e a comunicação com os clientes. Ela monta uma lista dos serviços essenciais com os sistemas de que cada um depende. O Prof. Hale explica que o planejamento da resiliência parte dos serviços que o negócio não pode interromper, e não dos sistemas, porque vários sistemas muitas vezes sustentam um serviço e um sistema pode sustentar vários. Lindiwe registra os serviços numa tabela, com os sistemas de que dependem e a maior interrupção tolerável de cada um, conforme acordado com os gerentes.

### 33.2 Alternativas manuais

Se o despacho falhar, os depósitos não conseguem imprimir as listas de entrega. Lindiwe trabalha com os supervisores dos depósitos para projetar uma alternativa manual: uma lista impressa toda noite com as entregas do dia seguinte, guardada num armário trancado, e formulários de confirmação em papel lançados depois no sistema. Para as cargas refrigeradas, os motoristas levam registradores de temperatura independentes, que não dependem da rede. Ela aprende que as melhores alternativas são simples, praticadas e independentes dos sistemas que substituem. Os supervisores testam a lista impressa e os formulários em papel durante um turno tranquilo de domingo, e os motoristas acham os formulários fáceis de preencher.

### 33.3 Exercícios

Os planos que nunca são exercitados muitas vezes falham. Lindiwe organiza um exercício de mesa: um ransomware cifrou o servidor do despacho numa segunda-feira de manhã. Os gerentes percorrem suas ações passo a passo. Eles descobrem que ninguém sabe onde as listas impressas ficam guardadas num dos depósitos e que a lista de contatos de incidentes contém duas pessoas que já saíram da empresa. O Prof. Hale observa que encontrar esse tipo de problema num exercício é exatamente o propósito, e que todo exercício deveria produzir uma breve lista de melhorias. A lista de melhorias tem sete itens.

### 33.4 Segurança física e integridade

Lindiwe retoma a preocupação com a segurança das pessoas do seu primeiro ano: os registros de temperatura dos medicamentos. Durante um incidente cibernético, os registros podem ser perdidos ou alterados. Ela recomenda que os registradores independentes dos motoristas sejam lidos no momento da entrega e que seus resultados sejam guardados separadamente, para que a evidência de temperaturas seguras sobreviva a um comprometimento do sistema. O gerente da frota aceita a recomendação. Ela aprende que a resiliência dos dados ligados à segurança das pessoas precisa de evidências independentes, e não apenas de backups do mesmo sistema. Lindiwe acrescenta esse requisito ao plano de resiliência, e a equipe da frota o inclui no treinamento dos motoristas.

### Exemplo resolvido

Lindiwe identifica os serviços essenciais, projeta alternativas impressas e independentes, conduz um exercício de mesa de ransomware que expõe contatos desatualizados e protege as evidências de temperatura de forma independente.

> **Caso sintético.** Os planos e os exercícios são sintéticos.

### Erros e limites

Um plano de resiliência que nunca foi exercitado costuma conter detalhes desatualizados.

### Exercícios

- **EX097 — Serviços essenciais.** Cite um serviço essencial identificado. *Rubrica:* 3 = as entregas de medicamentos refrigerados;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX098 — Descoberta do exercício.** O que o exercício revelou? *Rubrica:* 3 = o local desconhecido das listas impressas e contatos desatualizados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX099 — Evidência de temperatura.** Como a evidência de temperatura é protegida? *Rubrica:* 3 = registradores independentes lidos na entrega;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-33 -->
### Continue estudando — aula 33 (capítulo 33 de 50)

[← Capítulo 32](#ch-32) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Segurança da informação: integração

### Objetivos de aprendizagem

Você vai (1) proteger as integrações entre sistemas e parceiros; (2) gerenciar as credenciais de interfaces de programação de aplicações; (3) monitorar os dados trocados com terceiros.

### 34.1 Integrações com parceiros

A Saltmarsh troca dados com varejistas, transportadoras e uma empresa de processamento de folha de pagamento por meio de interfaces automatizadas. Lindiwe lista cada integração com seus dados, sua direção, seu método de autenticação e seu dono. Ela descobre que a conexão de uma transportadora usa uma senha fixa enviada em cada requisição por um canal cifrado, enquanto outra usa certificados. O Prof. Hale observa que as integrações são facilmente esquecidas depois de configuradas e muitas vezes têm acesso amplo, o que as torna atraentes para atacantes. Ela completa a lista com onze integrações e confirma um dono para cada uma com o gerente de negócio responsável.

### 34.2 Credenciais das interfaces

As credenciais das interfaces exigem o mesmo cuidado que as senhas da equipe. Lindiwe recomenda que cada integração tenha sua própria credencial, limitada às operações de que precisa, guardada num cofre de segredos gerenciado e trocada segundo um cronograma. Ela descobre que duas transportadoras compartilham uma única credencial, de modo que revogar o acesso de uma interromperia a outra. Separá-las exige uma semana de coordenação, mas significa que cada parceiro poderá ser gerenciado de forma independente no futuro. Ela move as duas credenciais para o cofre de segredos gerenciado e define a troca a cada noventa dias.

### 34.3 Minimização de dados

A empresa de folha de pagamento recebe os registros completos dos funcionários, inclusive os contatos de emergência, de que não precisa. Lindiwe revisa os campos com a equipe de recursos humanos e remove da exportação seis campos desnecessários. Ela explica que cada campo compartilhado é um campo que pode vazar dos sistemas do parceiro, e que minimizar os dados compartilhados reduz a exposição da Saltmarsh sem nenhum controle técnico. A empresa confirma que a exportação reduzida atende às suas necessidades. A equipe de recursos humanos atualiza a especificação da exportação e registra os motivos da remoção de cada campo.

### 34.4 Monitorando as trocas

Lindiwe configura o monitoramento das interfaces: volumes por parceiro por dia, taxas de erro e padrões incomuns de requisição. Um aumento repentino nas requisições de endereços de clientes feitas com a credencial de um varejista sugeriria uso indevido. Ela define os limiares a partir de três meses de histórico sintético. O Prof. Hale pergunta quem responde a um alerta nos fins de semana; ela acrescenta o dono da integração à escala de plantão, para que os alertas tenham um destinatário claro. O primeiro mês produz dois alertas, ambos explicados por promoções planejadas num dos varejistas, e ela ajusta os limiares de acordo.

### Exemplo resolvido

Lindiwe inventaria as integrações com parceiros, separa uma credencial compartilhada entre transportadoras, remove seis campos desnecessários da folha de pagamento e monitora os volumes das interfaces com um responsável nomeado.

> **Caso sintético.** As integrações são sintéticas.

### Erros e limites

Uma credencial compartilhada entre parceiros não pode ser revogada para um sem afetar o outro.

### Exercícios

- **EX100 — Credencial compartilhada.** Que problema duas transportadoras criaram? *Rubrica:* 3 = compartilhavam uma única credencial;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX101 — Campos removidos.** Quantos campos desnecessários foram removidos? *Rubrica:* 3 = seis;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX102 — Sinal de uso indevido.** O que sugeriria o uso indevido da credencial de um varejista? *Rubrica:* 3 = um aumento repentino nas requisições de endereços;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-34 -->
### Continue estudando — aula 34 (capítulo 34 de 50)

[← Capítulo 33](#ch-33) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 35 →](#ch-35)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) projetar uma capacidade de monitoramento de segurança; (2) justificar as escolhas de projeto com evidências; (3) apresentar um projeto a quem decide.

### 35.1 O enunciado

O segundo ateliê de projeto pede que a equipe de Lindiwe projete o monitoramento de segurança da Saltmarsh dentro de um orçamento anual fixo. As opções vão de uma equipe interna, que a Saltmarsh não consegue manter vinte e quatro horas por dia, a um serviço gerenciado externo. O projeto precisa usar as medidas de detecção já construídas, cumprir a exigência do cliente varejista de comunicar incidentes em vinte e quatro horas e proteger a privacidade da equipe, como prometido no aviso de monitoramento. A equipe tem oito semanas e precisa apresentar a uma banca que faz o papel do conselho, com um projeto escrito, uma estimativa de custos e um resumo de uma página.

### 35.2 Evidências para as escolhas

A equipe usa as evidências reunidas ao longo do curso: as taxas de eventos do primeiro ano, os atrasos de malha medidos no trabalho de controle e realimentação e o cálculo de alarmes falsos da estatística. Eles estimam os volumes de alertas e o tempo de analista necessário. O monitoramento interno precisaria de pelo menos cinco analistas para uma cobertura contínua, o que excede o orçamento. Um projeto híbrido, com um serviço externo à noite e a equipe da Saltmarsh durante o dia, cabe no orçamento. Eles mostram o cálculo num apêndice, para que a banca possa conferir cada passo.

### 35.3 Salvaguardas de privacidade

A equipe projeta salvaguardas: os logs de navegação ficam visíveis apenas para a equipe de segurança, os analistas externos veem identificadores de conta pseudônimos até que um incidente seja confirmado e há revisões trimestrais de quem acessou os logs. O Prof. Hale questiona se os pseudônimos atrasam as investigações; a equipe mostra que a correspondência pode ser revelada em minutos por um gerente de plantão da Saltmarsh. Os colegas consideram isso um equilíbrio sensato entre a privacidade e a velocidade de resposta. A equipe redige as salvaguardas como cláusulas do contrato com o prestador externo, para que sejam exigíveis, e não promessas informais.

### 35.4 Apresentando

A equipe apresenta a uma banca que faz o papel do conselho da Saltmarsh. Eles começam pelo problema de negócio, a obrigação das vinte e quatro horas e as lacunas noturnas, e depois mostram as opções, os custos e os riscos. A banca pergunta o que acontece se o prestador externo deixar passar um alerta; a equipe aponta os termos do contrato e as revisões mensais por amostragem. Lindiwe aprende que quem decide quer as consequências e os compromissos explicados com clareza, com o detalhe técnico disponível, mas sem estar à frente. A banca aprova o projeto híbrido para um levantamento de custos mais detalhado, e o Prof. Hale dá uma nota alta à apresentação pela clareza.

### Exemplo resolvido

A equipe de Lindiwe usa medições anteriores para dimensionar o monitoramento, escolhe um modelo híbrido dentro do orçamento, acrescenta pseudonimização com revelação rápida e apresenta os riscos e os custos a um conselho simulado.

> **Caso sintético.** O ateliê é sintético.

### Erros e limites

Projetar o monitoramento sem estimar o volume de alertas leva a equipes com pessoal insuficiente.

### Exercícios

- **EX103 — Equipe interna.** De quantos analistas uma cobertura interna contínua precisaria? *Rubrica:* 3 = pelo menos cinco;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX104 — Modelo híbrido.** O que é o modelo híbrido? *Rubrica:* 3 = serviço externo à noite, equipe da Saltmarsh de dia;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX105 — Revelação dos pseudônimos.** Quem pode revelar as identidades pseudônimas? *Rubrica:* 3 = um gerente de plantão da Saltmarsh;; 2 = parcialmente correto;; 1 = os analistas;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-35 -->
### Continue estudando — aula 35 (capítulo 35 de 50)

[← Capítulo 34](#ch-34) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 36 →](#ch-36)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-36"></a>

## Capítulo 36 — Segurança da informação: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) avaliar o custo de desempenho dos controles de segurança; (2) escalar o processamento de segurança com o crescimento; (3) testar os controles sob carga.

### 36.1 O custo dos controles

Os controles de segurança consomem recursos. A cifração usa tempo de processador, o registro de logs usa armazenamento e capacidade de rede, e a inspeção acrescenta latência. Lindiwe mede um teste sintético: ativar a cifração de disco completo em notebooks modernos acrescenta uma pequena sobrecarga de processamento que os usuários não percebem, enquanto inspecionar todo o tráfego web cifrado no firewall do depósito praticamente dobra a carga do seu processador. Ela recomenda inspecionar apenas as categorias de tráfego com risco claro, em vez de tudo. A equipe de redes adota a abordagem seletiva e documenta exatamente quais categorias de tráfego são inspecionadas.

### 36.2 Escalando os logs

A Saltmarsh planeja três novos depósitos. Lindiwe usa seu modelo do primeiro ano para estimar os eventos extras por dia e confere se o coletor de logs consegue absorvê-los. No ritmo atual de crescimento, o coletor atinge sua capacidade em até dezoito meses. Ela propõe filtrar os eventos de pouco valor na origem e acrescentar um segundo coletor antes do limite. O Prof. Hale observa que os sistemas de segurança que descartam dados silenciosamente sob carga são piores do que os que falham de forma ruidosa. A equipe de infraestrutura inclui o segundo coletor no orçamento do ano seguinte.

### 36.3 Testes de carga

Lindiwe testa a medida de adivinhação de senhas com dez vezes o volume de logs atual, usando dados sintéticos. Ela termina em poucos segundos, bem dentro da janela de relatório. Ela também testa a conciliação de ativos com dez mil hosts; ela continua rápida porque usa operações de conjuntos. Ela registra os testes para que o crescimento futuro possa ser conferido em relação a eles. Ela aprende que as ferramentas da biblioteca padrão escalam bem para volumes moderados quando os algoritmos são escolhidos com bom senso. Os registros dos testes incluem o tamanho dos dados e o tempo de execução de cada script.

### 36.4 Compromissos em escala

À medida que os volumes crescem, a Saltmarsh precisa escolher entre manter todos os detalhes e reduzir o custo. Lindiwe propõe manter completos os eventos de autenticação e de administração, que são centrais para as investigações, e resumir os eventos rotineiros de permissão do firewall depois de trinta dias. Ela documenta quais perguntas de investigação ficam mais difíceis de responder depois do resumo. O líder de segurança aceita a proposta, com uma revisão após um ano, reconhecendo que o compromisso pode precisar de ajustes. Ela lista as perguntas afetadas num apêndice da política de retenção, para que os investigadores saibam de antemão que detalhes continuam disponíveis.

### Exemplo resolvido

Lindiwe mede a sobrecarga dos controles, descobre que o coletor de logs atinge sua capacidade em dezoito meses, testa a detecção sob carga com dez vezes o volume e propõe manter completos os eventos de autenticação, resumindo os logs rotineiros do firewall.

> **Caso sintético.** As medições são sintéticas.

### Erros e limites

Os sistemas de segurança que descartam dados silenciosamente sob carga dão uma falsa garantia.

### Exercícios

- **EX106 — Custo da inspeção.** O que faz a inspeção de todo o tráfego cifrado? *Rubrica:* 3 = praticamente dobra a carga do processador do firewall;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX107 — Capacidade do coletor.** Quando o coletor atinge sua capacidade? *Rubrica:* 3 = em até dezoito meses;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX108 — Eventos mantidos.** Que eventos são mantidos completos? *Rubrica:* 3 = os eventos de autenticação e de administração;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-36 -->
### Continue estudando — aula 36 (capítulo 36 de 50)

[← Capítulo 35](#ch-35) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 37 →](#ch-37)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-37"></a>

## Capítulo 37 — Segurança da informação: operações

### Objetivos de aprendizagem

Você vai (1) conduzir as rotinas de operações de segurança; (2) tratar incidentes com um processo definido; (3) aprender com os incidentes sem atribuir culpa.

### 37.1 Rotinas diárias

As operações de segurança da Saltmarsh funcionam com base em rotinas: revisar os alertas da noite, conferir os backups que falharam, revisar as novas exceções e confirmar que as verificações agendadas foram executadas. Lindiwe escreve uma lista de verificação para o turno da manhã e cronometra cerca de quarenta minutos. O Prof. Hale observa que as rotinas pegam os desvios antes que se tornem incidentes, e que as listas de verificação escritas permitem que funcionários novos cubram ausências sem pular passos que os funcionários experientes executam de memória. Ela testa a lista com dois analistas durante a primeira semana deles, e ambos a completam sem precisar da ajuda de colegas experientes.

### 37.2 Tratamento de incidentes

Lindiwe ajuda a escrever o processo de incidentes da Saltmarsh usando como guia as funções Detectar, Responder e Recuperar do NIST Cybersecurity Framework 2.0, com passos práticos para analisar, conter, erradicar, recuperar e comunicar. Cada passo tem um dono e um modelo. Quando ocorre um incidente sintético, uma conta vítima de phishing que envia faturas a clientes, a equipe segue o processo: bloqueia a conta, remove as regras de encaminhamento, avisa os clientes e comunica o cliente varejista dentro das vinte e quatro horas exigidas. O incidente inteiro é encerrado em dois dias, e Lindiwe registra a linha do tempo no registro de incidentes.

### 37.3 Revisão pós-incidente

Depois do incidente, Lindiwe conduz uma revisão. A pergunta não é quem clicou, mas por que o ataque teve sucesso e como torná-lo mais difícil. A revisão descobre que a conta não tinha autenticação multifator porque estava numa lista de exceções cuja expiração tinha sido prorrogada duas vezes sem revisão. A correção é uma regra segundo a qual uma segunda prorrogação precisa da aprovação do líder de segurança. Ela aprende que as revisões sem culpa revelam fraquezas de processo que a busca de culpados esconderia. O líder de segurança aprova a nova regra na mesma semana.

### 37.4 Métricas

Lindiwe relata métricas operacionais mensalmente: alertas tratados, tempo mediano até a contenção, exceções abertas, conformidade com a linha de base e resultados dos testes de restauração. Ela evita metas que estimulem manipulação, como recompensar menos alertas, o que poderia ser alcançado desligando a detecção. O Prof. Hale explica que boas métricas de segurança descrevem o estado dos controles e a velocidade da resposta, e que os números enviados aos gerentes devem sempre vir acompanhados de contexto. Ela inclui um breve comentário em cada relatório mensal explicando qualquer mudança significativa, para que os leitores não interpretem um aumento de alertas como uma piora da segurança.

### Exemplo resolvido

Lindiwe escreve uma lista de verificação matinal de quarenta minutos, conduz um incidente de conta vítima de phishing por um processo definido, faz uma revisão sem culpa que encontra uma exceção prorrogada repetidas vezes e relata métricas equilibradas.

> **Caso sintético.** O incidente é sintético.

### Erros e limites

Recompensar menos alertas pode estimular o desligamento da detecção.

### Exercícios

- **EX109 — Duração da lista.** Quanto tempo leva a lista de verificação matinal? *Rubrica:* 3 = cerca de quarenta minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX110 — Ações no incidente.** Cite uma ação de contenção tomada. *Rubrica:* 3 = bloquear a conta;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX111 — Causa raiz.** Por que a conta não tinha autenticação multifator? *Rubrica:* 3 = uma exceção prorrogada duas vezes sem revisão;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-37 -->
### Continue estudando — aula 37 (capítulo 37 de 50)

[← Capítulo 36](#ch-36) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 38 →](#ch-38)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-38"></a>

## Capítulo 38 — Segurança da informação: validação

### Objetivos de aprendizagem

Você vai (1) validar que os controles atendem às necessidades do negócio; (2) reunir o retorno dos usuários e dos donos; (3) distinguir a verificação da validação.

### 38.1 Verificação e validação

Lindiwe distingue duas perguntas. A verificação pergunta se um controle foi construído conforme especificado; seus testes de laboratório responderam a isso. A validação pergunta se o controle atende à necessidade real. A medida de adivinhação de senhas funciona conforme especificado, mas ela ajuda a Saltmarsh a reduzir a tomada de contas? Ela projeta atividades de validação: entrevistas com a equipe de segurança sobre a utilidade dos alertas, revisão dos incidentes para ver se as medidas os detectaram e comparação com os objetivos do negócio. O Prof. Hale pede que ela aplique essas atividades a todos os controles construídos durante o curso e relate os resultados em conjunto.

### 38.2 Retorno dos donos

Lindiwe entrevista os donos dos sistemas sobre os controles que os afetam. O dono do despacho acha útil a aprovação das mudanças de endereço, mas diz que o limite pega sem necessidade alguns grandes clientes regulares. O dono da folha de pagamento quer relatórios de linha de base mais claros. Ela registra cada ponto e propõe ajustes. O Prof. Hale observa que a visão dos donos revela se os controles se encaixam no trabalho, o que os testes sozinhos não conseguem mostrar, e que os controles de que os donos não gostam muitas vezes são enfraquecidos discretamente. Ela eleva um pouco o limite para os clientes com histórico verificado e registra a mudança com seu raciocínio.

### 38.3 Evidências da revisão de incidentes

Lindiwe revisa seis incidentes sintéticos do ano. Quatro foram detectados por controles construídos durante o curso, um por uma reclamação de cliente e um por uma notificação externa. As duas detecções perdidas apontam lacunas: nenhum monitoramento das regras de encaminhamento de e-mail e nenhum alerta para downloads em massa do portal de clientes. Ela acrescenta as duas ao plano de melhorias. Ela aprende que os incidentes fornecem as evidências de validação mais diretas. As duas lacunas recebem donos nomeados e datas-alvo no plano de melhorias.

### 38.4 Relatório de validação

Seu relatório informa, para cada controle, se ele está verificado, validado, parcialmente validado ou ainda não validado, com as evidências. A medida de adivinhação de senhas está validada por dois incidentes detectados; o controle de mudança de endereço está verificado, mas ainda não validado, porque nenhuma tentativa de fraude ocorreu. O Prof. Hale elogia a distinção honesta. Ela observa que alegar validação sem evidências enganaria o conselho sobre o quanto os controles protegem o negócio. O relatório é apresentado ao comitê de segurança da Saltmarsh, que pede uma nova avaliação depois de seis meses.

### Exemplo resolvido

Lindiwe distingue a verificação da validação, reúne o retorno dos donos, encontra duas lacunas de detecção a partir de seis incidentes e relata o estado de validação de cada controle com evidências.

> **Caso sintético.** Os incidentes são sintéticos.

### Erros e limites

Um controle pode ser construído corretamente e ainda assim não atender à necessidade real.

### Exercícios

- **EX112 — Incidentes detectados.** Quantos dos seis incidentes os controles do curso detectaram? *Rubrica:* 3 = quatro;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX113 — Lacunas perdidas.** Cite uma lacuna de detecção encontrada. *Rubrica:* 3 = as regras de encaminhamento de e-mail;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX114 — Estado do controle de endereço.** Qual é o estado do controle de mudança de endereço? *Rubrica:* 3 = verificado, mas ainda não validado;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-38 -->
### Continue estudando — aula 38 (capítulo 38 de 50)

[← Capítulo 37](#ch-37) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 39 →](#ch-39)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-39"></a>

## Capítulo 39 — Segurança da informação: manutenibilidade

### Objetivos de aprendizagem

Você vai (1) manter as ferramentas de segurança fáceis de manter; (2) documentar os controles para os sucessores; (3) planejar a rotatividade da equipe.

### 39.1 Código fácil de manter

Os scripts de Lindiwe agora executam as verificações de linha de base, a medida de adivinhação e os testes de restauração da Saltmarsh. Ela vai sair no fim do curso, então outras pessoas precisam mantê-los. Ela revisa a clareza do seu código: nomes descritivos, comentários que explicam o porquê, e não o quê, testes para cada regra e um único arquivo de configuração para os limiares. O Prof. Hale observa que as ferramentas de segurança muitas vezes falham quando seu autor vai embora, porque ninguém as entende bem o suficiente para alterá-las com segurança. Ela também remove duas funções sem uso encontradas durante a revisão.

### 39.2 Runbooks

Para cada controle, Lindiwe escreve um runbook: propósito, agenda, entradas, como ler os resultados, problemas comuns e com quem falar. O runbook do teste de restauração explica o que fazer quando as somas de verificação divergem, inclusive conferir a saúde do disco e executar de novo a restauração. Ela pede que um colega sem nenhum envolvimento siga cada runbook. Dois passos se mostram pouco claros, e ela os reescreve. Ela aprende que a documentação é testada pelo uso, e não pela leitura do próprio autor. Os runbooks finais são guardados junto com os scripts no controle de versão.

### 39.3 Transferência de responsabilidade

Lindiwe define donos para cada ferramenta na equipe de TI da Saltmarsh e conduz sessões de passagem. Cada dono executa a ferramenta uma vez com ela observando e depois uma vez sozinho. Ela atualiza o modelo de ativos e os registros de decisão para nomear os novos donos. O Prof. Hale explica que a transferência de responsabilidade é um controle por si só: sem ela, as ferramentas ficam órfãs, exatamente como o sistema de câmeras que ela encontrou no terceiro ano. Os novos donos assinam os registros de passagem, e Lindiwe continua disponível por e-mail para dúvidas durante seu último período.

### 39.4 Dependência de pessoas

Lindiwe observa que alguns controles dependem de uma única pessoa, como a revisão mensal por amostragem do líder de segurança. Se essa pessoa estiver ausente, o controle para. Ela recomenda substitutos para cada controle que depende de uma pessoa e os registra nos runbooks. Ela aprende que a facilidade de manutenção se aplica aos processos e às pessoas, assim como ao código, e que a resiliência contra a ausência de funcionários faz parte da engenharia de segurança. Cada substituto executa o controle uma vez durante o período de passagem, e os runbooks registram seus nomes e as datas em que o executaram pela última vez, para que o líder de segurança possa ver quem está pronto.

### Exemplo resolvido

Lindiwe melhora a clareza do código, escreve runbooks testados por um colega, transfere a responsabilidade pelas ferramentas com execuções supervisionadas e acrescenta substitutos para os controles que dependem de uma pessoa.

> **Caso sintético.** As ferramentas e a equipe são sintéticas.

### Erros e limites

As ferramentas cujos autores saem sem fazer a passagem ficam sem manutenção.

### Exercícios

- **EX115 — Configuração.** Onde ficam os limiares? *Rubrica:* 3 = num único arquivo de configuração;; 2 = parcialmente correto;; 1 = no código;; 0 = nenhuma.

- **EX116 — Teste dos runbooks.** Como os runbooks são testados? *Rubrica:* 3 = um colega segue cada um deles;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX117 — Substitutos.** Por que acrescentar substitutos? *Rubrica:* 3 = os controles param quando uma pessoa está ausente;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-39 -->
### Continue estudando — aula 39 (capítulo 39 de 50)

[← Capítulo 38](#ch-38) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 40 →](#ch-40)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem

Você vai (1) verificar os controles de ponta a ponta; (2) testar a detecção com ataques simulados; (3) registrar os resultados para um dossiê de evidências.

### 40.1 Testes de ponta a ponta

No segundo laboratório de verificação, Lindiwe testa os controles do evento até a resposta. Ela planta uma rajada sintética de adivinhação de senhas e a acompanha até o fim: a medida sinaliza a conta, o alerta chega ao analista de plantão, o analista bloqueia a conta e o chamado registra cada passo com os horários. O Prof. Hale explica que os testes de ponta a ponta encontram falhas de passagem entre ferramentas e pessoas que os testes de componentes isolados deixam escapar. A cadeia inteira se completa em onze minutos no teste sintético, e ela registra o tempo gasto em cada passo.

### 40.2 Ataques simulados

Com autorização por escrito, Lindiwe executa ataques simulados num ambiente de teste que espelha a rede da Saltmarsh: uma conta vítima de phishing que cria uma regra de encaminhamento, um download em massa do portal de clientes e uma mudança de endereço de entrega uma hora antes do despacho. Ela confere que controles detectam cada um. A regra de encaminhamento agora dispara um alerta, depois que a lacuna encontrada na validação foi corrigida. O alerta de download em massa dispara tarde porque seu limiar está alto demais. O alerta de mudança de endereço dispara como projetado, em até dois minutos depois da mudança.

### 40.3 Corrigindo e testando de novo

Lindiwe reduz o limiar de download em massa usando o histórico sintético do capítulo de integração e depois executa de novo a simulação. O alerta agora dispara em poucos minutos. Ela registra os dois resultados, o de antes e o de depois, para que o dossiê de evidências mostre a melhoria e sua causa. O Prof. Hale observa que registrar as falhas e as correções juntas é mais convincente do que mostrar apenas os resultados finais aprovados, porque demonstra que os testes de fato influenciaram os controles. Ela também acrescenta o caso do download em massa ao conjunto permanente de testes usado depois de cada mudança de configuração.

### 40.4 Evidências para o dossiê

Lindiwe reúne todos os registros dos testes: planos, autorizações, entradas, saídas, tempos e correções. Ela os guarda com somas de verificação e um índice. Ela planeja usá-los no dossiê de evidências do último ano, em que cada afirmação sobre a segurança da Saltmarsh precisa apontar para evidências específicas. Ela aprende que um registro de testes bem organizado torna o trabalho de garantia posterior mais rápido e mais confiável. O Prof. Hale revisa o índice e pede que ela acrescente uma breve descrição do propósito de cada teste, para que leitores que não conhecem os controles possam entender por que cada teste foi executado e o que significa uma aprovação ou uma reprovação.

### Exemplo resolvido

Lindiwe testa a detecção de adivinhação de ponta a ponta, simula três ataques, corrige um alerta de download em massa que disparava tarde e testa de novo, e guarda todos os registros para o dossiê.

> **Caso sintético.** Os testes são sintéticos.

### Erros e limites

Mostrar apenas os testes finais aprovados esconde como os controles foram melhorados.

### Exercícios

- **EX118 — Passos de ponta a ponta.** Cite um passo acompanhado de ponta a ponta. *Rubrica:* 3 = o analista bloqueia a conta;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX119 — Alerta atrasado.** Que alerta disparou tarde? *Rubrica:* 3 = o de download em massa;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX120 — Antes e depois.** Por que registrar os resultados de antes e de depois da correção? *Rubrica:* 3 = mostra a melhoria e sua causa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-40 -->
### Continue estudando — aula 40 (capítulo 40 de 50)

[← Capítulo 39](#ch-39) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 41 →](#ch-41)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-41"></a>

## Capítulo 41 — Segurança da informação: otimização do sistema

### Objetivos de aprendizagem

Você vai (1) reduzir o custo da segurança sem reduzir a proteção; (2) remover controles redundantes; (3) priorizar os investimentos pela redução de risco.

### 41.1 Encontrando desperdício

No último ano, Lindiwe revisa os gastos e o esforço de segurança da Saltmarsh. Ela encontra ferramentas sobrepostas: dois produtos que varrem os notebooks em busca de vulnerabilidades e três lugares distintos em que listas de contas são mantidas à mão. Cada sobreposição custa licenças e tempo da equipe, e listas incoerentes criam lacunas. O Prof. Hale pede que ela mostre quais controles cada ferramenta sustenta antes de recomendar a remoção, porque uma ferramenta que parece redundante pode cobrir um caso que a outra deixa escapar. Ela lista todas as ferramentas de segurança, com o custo da licença, o dono e os controles que sustentam, numa única tabela compartilhada.

### 41.2 Consolidação

Lindiwe mapeia os dois scanners de notebooks em relação aos ativos que cobrem. Um cobre todos os notebooks, inclusive os terminais do armazém; o outro deixa de fora os terminais, mas oferece relatórios de que os gerentes gostam. Ela recomenda manter o primeiro e recriar os relatórios úteis a partir dos seus dados. Para as listas de contas, ela propõe gerar as três a partir da fonte única de identidades configurada antes. As mudanças economizam custos de licença e eliminam atualizações manuais que tinham causado erros em revisões de acesso anteriores. O líder de segurança aprova as duas mudanças, e a licença do segundo scanner não é renovada.

### 41.3 Risco por libra

Lindiwe ordena os investimentos propostos pela redução de risco estimada por unidade de custo. Os backups imutáveis e a autenticação multifator para as contas de fornecedores restantes ficam no topo, porque tratam as ameaças mais danosas a baixo custo. Um produto de análise avançada proposto fica mal colocado, já que as lacunas de detecção atuais da Saltmarsh são básicas. Ela observa que suas estimativas são aproximadas, mas que ordená-las abertamente torna as premissas visíveis e ajuda os gerentes a questioná-las, em vez de aceitar as alegações dos fornecedores. Ela apresenta a ordenação ao diretor financeiro com as premissas listadas ao lado de cada estimativa, convidando a contestação.

### 41.4 Medindo depois da mudança

Depois da consolidação, Lindiwe confere que nada foi perdido: o scanner que ficou ainda cobre todos os ativos do modelo conciliado, e as revisões de acesso baseadas na fonte única de identidades não encontram nenhuma conta faltando. Ela registra essas verificações como evidência. O Prof. Hale observa que a otimização precisa provar que a proteção foi preservada; do contrário, a economia pode simplesmente transferir o custo para um incidente futuro. Ela repete a verificação de cobertura um mês depois e de novo encontra todos os ativos cobertos. O diretor financeiro recebe uma breve nota confirmando que a economia não reduziu a proteção, com as evidências anexadas para auditoria.

### Exemplo resolvido

Lindiwe remove um scanner de notebooks redundante depois de conferir a cobertura, gera as listas de contas a partir de uma única fonte, ordena os investimentos pela redução de risco por custo e verifica a cobertura depois das mudanças.

> **Caso sintético.** Os custos e as ferramentas são sintéticos.

### Erros e limites

Remover uma ferramenta sem conferir a cobertura pode abrir lacunas despercebidas.

### Exercícios

- **EX121 — Scanner mantido.** Que scanner de notebooks é mantido? *Rubrica:* 3 = o que cobre os terminais do armazém;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX122 — Listas de contas.** Como as três listas de contas são produzidas depois da mudança? *Rubrica:* 3 = a partir da fonte única de identidades;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX123 — Compra mal colocada.** Que investimento fica mal colocado? *Rubrica:* 3 = um produto de análise avançada;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-41 -->
### Continue estudando — aula 41 (capítulo 41 de 50)

[← Capítulo 40](#ch-40) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 42 →](#ch-42)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-42"></a>

## Capítulo 42 — Segurança da informação: pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa aplicada a partir de dados operacionais; (2) projetar uma comparação justa; (3) relatar os achados com seus limites.

### 42.1 Pergunta

A pesquisa aplicada de Lindiwe pergunta se os depósitos com login por aproximação do crachá nos terminais do armazém têm menos incidentes de uso indevido de contas do que os depósitos que ainda aguardam a implantação. A pergunta nasce da implantação da autenticação multifator, que chegou aos depósitos em etapas, por razões práticas. O Prof. Hale aponta que as implantações em etapas criam comparações naturais, mas que a ordem dos depósitos foi escolhida pelo tamanho, o que poderia enviesar qualquer diferença. Ela escreve a pergunta numa única frase e a confere com o líder de segurança, que confirma que o registro de incidentes guarda os detalhes necessários de todos os depósitos. O Prof. Hale aprova a pergunta.

### 42.2 Desenho

Lindiwe compara as taxas de incidentes por cem funcionários antes e depois da implantação nos depósitos que adotaram cedo com as dos depósitos que adotaram tarde, usando o período em que os depósitos tardios ainda não tinham começado. Ela confere que as taxas de incidentes dos dois grupos eram parecidas antes da implantação. Ela define os incidentes com precisão a partir do registro de incidentes: uso confirmado de uma conta por alguém que não é seu dono. Ela fixa essa definição e a comparação antes de examinar os resultados. O Prof. Hale revisa o plano e confirma que ele foi fixado antes de os resultados serem examinados.

### 42.3 Achados

Os dados sintéticos mostram menos incidentes depois da implantação nos depósitos que adotaram cedo e pouca mudança nos depósitos tardios ao longo dos mesmos meses. No entanto, os incidentes são raros, apenas um punhado em cada grupo, então a diferença é incerta. Lindiwe relata as contagens, as taxas e a comparação, afirmando que a direção apoia a implantação, mas que a evidência é fraca. O Prof. Hale a elogia por não transformar uma contagem pequena numa afirmação confiante. Ela apresenta as contagens numa tabela simples, com os dois períodos para os dois grupos, para que os leitores possam ver diretamente os números pequenos.

### 42.4 O valor do estudo

Lindiwe argumenta que o principal valor do estudo é um método reutilizável: definir os incidentes de forma coerente, usar as implantações em etapas como comparações e conferir a semelhança antes da implantação. A Saltmarsh pode repeti-lo à medida que mais dados se acumulam. Ela também observa que o fim dos logins compartilhados é, por si só, um ganho de responsabilização, independentemente das contagens de incidentes. Ela aprende que a pesquisa aplicada em segurança muitas vezes produz métodos e evidências modestas, e não respostas definitivas. O líder de segurança pede que ela escreva o método como um breve procedimento, para que a equipe possa refazer a comparação todos os anos, à medida que o registro de incidentes cresce.

### Exemplo resolvido

Lindiwe compara os depósitos que adotaram cedo e tarde a aproximação do crachá usando uma definição fixa de incidente, encontra uma direção favorável, mas incerta, a partir de contagens pequenas e enfatiza um método reutilizável.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Contagens pequenas de incidentes não sustentam conclusões confiantes.

### Exercícios

- **EX124 — Comparação natural.** O que criou a comparação natural? *Rubrica:* 3 = a implantação em etapas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX125 — Definição de incidente.** Como um incidente é definido? *Rubrica:* 3 = uso de uma conta por alguém que não é seu dono;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX126 — Força da evidência.** Quão forte é a evidência? *Rubrica:* 3 = favorável, mas fraca;; 2 = parcialmente correto;; 1 = forte;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-42 -->
### Continue estudando — aula 42 (capítulo 42 de 50)

[← Capítulo 41](#ch-41) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 43 →](#ch-43)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-43"></a>

## Capítulo 43 — Prática na indústria ou no serviço público

### Objetivos de aprendizagem

Você vai (1) trabalhar dentro de uma equipe profissional de segurança; (2) tratar informações confidenciais com responsabilidade; (3) refletir sobre a prática profissional.

### 43.1 O estágio

Lindiwe passa um semestre trabalhando em tempo integral na equipe de segurança da Saltmarsh. Ela participa da reunião diária em pé, assume uma parte das revisões de alertas e apoia a preparação de uma auditoria. Ela percebe quanto do trabalho envolve coordenação: convencer os donos a corrigir os achados, agendar as mudanças em torno dos picos dos depósitos e explicar os riscos à área financeira. O Prof. Hale a visita no meio do estágio e pergunta que habilidades ela mais usa; ela responde que escrita e negociação, mais do que programação. Ela mantém um diário semanal registrando o que fez, o que aprendeu e que conversas mudaram decisões.

### 43.2 Confidencialidade

O estágio dá a Lindiwe acesso a informações sensíveis: detalhes de incidentes, listas de vulnerabilidades e reclamações de clientes. Ela assina um acordo de confidencialidade e segue a regra de que os trabalhos do curso usam apenas dados sintéticos. Quando um colega de turma pergunta sobre um incidente real, ela se recusa a compartilhar detalhes. O Prof. Hale observa que a confiança profissional depende da discrição, e que a equipe de segurança precisa dar o exemplo do tratamento que pede aos outros. Suas reflexões para o curso descrevem os tipos de trabalho que ela fez sem revelar nenhum nome, sistema ou detalhe de incidente real.

### 43.3 Preparação para a auditoria

A Saltmarsh se prepara para uma auditoria externa do seu sistema de gestão. Lindiwe ajuda a reunir as evidências: os registros de avaliação de riscos, a declaração de aplicabilidade, as revisões de acesso e os resultados dos testes de restauração. Ela encontra dois controles listados como implementados cujas evidências estão incompletas. Em vez de apresentá-los como completos, a equipe os marca como em andamento, com datas. Mais tarde, o auditor registra a honestidade de forma favorável. Ela aprende que as auditorias recompensam registros precisos mais do que afirmações bem polidas. Lindiwe acrescenta as lacunas de evidência ao rastreador da equipe, com donos.

### 43.4 Reflexão

No fim do estágio, Lindiwe escreve uma reflexão sobre a prática profissional. Ela observa que a habilidade técnica conquista credibilidade, mas que a influência vem de entender o negócio e se comunicar com clareza. Ela também observa o lado emocional dos incidentes: os funcionários cujas contas sofreram phishing se sentiram constrangidos, e um tratamento calmo e sem culpa os ajudou a comunicar rapidamente na vez seguinte. O Prof. Hale pede que ela leve essas lições para o projeto final. Ela compartilha a reflexão com o líder de segurança, que acrescenta dois pontos, do ponto de vista da equipe, sobre como as perguntas dela melhoraram a própria documentação da equipe.

### Exemplo resolvido

Lindiwe trabalha na equipe de segurança da Saltmarsh, mantém os detalhes reais em sigilo, ajuda a preparar evidências de auditoria honestas e reflete sobre a comunicação e o tratamento sem culpa.

> **Caso sintético.** O estágio é sintético.

### Erros e limites

Apresentar controles incompletos como implementados engana os auditores.

### Exercícios

- **EX127 — Habilidades mais usadas.** Que habilidades Lindiwe mais usa? *Rubrica:* 3 = escrita e negociação;; 2 = parcialmente correto;; 1 = programação;; 0 = nenhuma.

- **EX128 — Evidências incompletas.** Como os dois controles incompletos são apresentados? *Rubrica:* 3 = como em andamento, com datas;; 2 = parcialmente correto;; 1 = completos;; 0 = nenhuma.

- **EX129 — Efeito da ausência de culpa.** O que o tratamento sem culpa estimulou? *Rubrica:* 3 = comunicação mais rápida na vez seguinte;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-43 -->
### Continue estudando — aula 43 (capítulo 43 de 50)

[← Capítulo 42](#ch-42) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 44 →](#ch-44)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-44"></a>

## Capítulo 44 — Projeto final de engenharia I

### Objetivos de aprendizagem

Você vai (1) definir um problema de projeto final com um cliente; (2) planejar um projeto substancial de engenharia de segurança; (3) gerenciar o escopo e o risco.

### 44.1 Definição do problema

O projeto final de Lindiwe trata de um problema identificado pela Saltmarsh: recuperar o despacho em até quatro horas depois de um ransomware, o objetivo acordado antes. Os backups atuais estão verificados, mas ninguém jamais reconstruiu do zero o serviço de despacho inteiro. O projeto final vai projetar, construir e testar um processo de recuperação num ambiente isolado. O Prof. Hale e o líder de segurança assinam a declaração do problema, que lista as entregas, as restrições e o critério de sucesso. O líder de segurança também confirma quais sistemas podem ser copiados para o ambiente isolado e que apenas dados sintéticos de clientes serão usados.

### 44.2 Plano

Lindiwe divide o projeto em etapas: documentar as dependências do despacho, construir um ambiente de recuperação isolado, automatizar por script a reconstrução de cada componente, restaurar os dados a partir dos backups imutáveis e executar ensaios cronometrados. Cada etapa tem uma entrega e uma revisão. Ela identifica riscos para o próprio projeto, como atrasos na obtenção do hardware de teste, e planeja alternativas, inclusive usar máquinas virtuais num servidor reserva se o hardware chegar atrasado. Ela marca reuniões de revisão quinzenais com o Prof. Hale e o líder de segurança, cada uma dedicada a uma etapa.

### 44.3 Dependências

Documentar as dependências revela surpresas. O despacho precisa do diretório para os logins, da fila de mensagens, do serviço de mapas, de certificados e de um servidor de licenças para um dos componentes. O servidor de licenças não aparecia em nenhum diagrama. Sem ele, o serviço reconstruído se recusaria a iniciar. Lindiwe o acrescenta ao modelo de ativos e ao plano de recuperação. O Prof. Hale observa que as dependências ocultas são um motivo comum para a recuperação levar muito mais tempo do que o planejado. Ela também registra a versão e o dono de cada dependência, para que o plano de recuperação possa ser mantido atualizado.

### 44.4 Controle do escopo

No meio do projeto, o gerente de operações pergunta se o projeto final poderia cobrir também a recuperação da folha de pagamento. Lindiwe avalia o esforço e explica que acrescentar a folha de pagamento arriscaria não terminar nenhuma das duas direito. Ela propõe documentar apenas as dependências da folha de pagamento, como insumo para um projeto posterior. O cliente concorda. Ela aprende que proteger o escopo faz parte de entregar valor, e que dizer não com uma razão clara preserva a confiança melhor do que prometer demais. Ela registra a decisão no diário do projeto, com a concordância do gerente de operações e uma nota sobre o esforço extra estimado.

### Exemplo resolvido

Lindiwe define um projeto final de recuperação do despacho com uma meta de quatro horas, planeja entregas em etapas, encontra uma dependência oculta de servidor de licenças e protege o escopo adiando a folha de pagamento.

> **Caso sintético.** O projeto final é sintético.

### Erros e limites

As dependências não documentadas tornam a recuperação muito mais lenta do que o planejado.

### Exercícios

- **EX130 — Critério de sucesso.** Qual é o critério de sucesso do projeto final? *Rubrica:* 3 = recuperar o despacho em até quatro horas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX131 — Dependência oculta.** Que dependência faltava nos diagramas? *Rubrica:* 3 = um servidor de licenças;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX132 — Decisão de escopo.** O que é feito em relação à folha de pagamento? *Rubrica:* 3 = documentar apenas as dependências;; 2 = parcialmente correto;; 1 = recuperação completa;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-44 -->
### Continue estudando — aula 44 (capítulo 44 de 50)

[← Capítulo 43](#ch-43) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 45 →](#ch-45)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-45"></a>

## Capítulo 45 — Revisão independente de projeto

### Objetivos de aprendizagem

Você vai (1) preparar um projeto para revisão independente; (2) responder aos achados do revisor; (3) registrar os resultados da revisão.

### 45.1 Preparando a revisão

Antes de construir, Lindiwe submete seu projeto de recuperação à revisão independente de um engenheiro de outra organização, organizada pelo Prof. Hale. Ela prepara um pacote: a declaração do problema, a arquitetura, a lista de dependências, os passos de recuperação, o plano de testes e os riscos conhecidos. Ela escreve um breve guia explicando de que retorno mais precisa. O Prof. Hale observa que os revisores dão um retorno melhor quando o autor declara honestamente as questões em aberto, em vez de apresentar o projeto como acabado. O revisor recebe o pacote completo duas semanas antes da reunião formal de revisão.

### 45.2 Achados

O revisor levanta quatro achados. O ambiente de recuperação usa as mesmas credenciais de administrador da produção, de modo que um atacante que as possuísse também poderia danificar a recuperação. Os scripts de recuperação estão guardados num servidor que o ransomware poderia cifrar. O plano de testes não inclui restaurar a partir de backups com mais de um dia, para o caso de os backups recentes estarem corrompidos. Por fim, o projeto não diz quem decide iniciar a recuperação. Ela agradece ao revisor e faz uma pergunta de acompanhamento sobre cada achado, para ter certeza de que o entendeu corretamente.

### 45.3 Respostas

Lindiwe responde a cada achado. Ela cria credenciais separadas para o ambiente de recuperação, guardadas offline. Ela guarda os scripts no controle de versão, com uma cópia offline. Ela acrescenta um teste de restauração a partir de backups de uma semana. Ela escreve uma regra de decisão: o líder de segurança e o diretor de operações autorizam a recuperação em conjunto, com substitutos nomeados. Ela registra cada resposta numa tabela, com a concordância do revisor anotada ao lado de cada uma. O revisor examina o projeto atualizado duas semanas depois e confirma por escrito que os quatro achados estão resolvidos.

### 45.4 O valor da revisão

Lindiwe reflete que três dos quatro achados diziam respeito à própria recuperação estar vulnerável ao mesmo ataque a que ela deveria sobreviver. Ela tinha se concentrado na velocidade da reconstrução e deixado isso passar. O Prof. Hale observa que os revisores independentes trazem premissas diferentes, e é exatamente por isso que as revisões encontram problemas que os autores não conseguem encontrar. O registro da revisão entra no dossiê de evidências. Ela acrescenta ao plano da tese uma seção descrevendo a revisão e seu efeito sobre o projeto, porque acredita que outros engenheiros se beneficiariam de ver como suas premissas mudaram depois de um escrutínio independente.

### Exemplo resolvido

Lindiwe prepara um pacote de revisão, recebe quatro achados, entre eles as credenciais compartilhadas e os scripts expostos, e responde com credenciais offline, scripts offline, testes de restauração mais antigos e uma regra de decisão.

> **Caso sintético.** A revisão é sintética.

### Erros e limites

Um ambiente de recuperação que compartilha as credenciais da produção pode ser destruído pelo mesmo atacante.

### Exercícios

- **EX133 — Achado sobre credenciais.** Que problema de credenciais o revisor encontrou? *Rubrica:* 3 = a recuperação usa as credenciais de administrador da produção;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX134 — Backups mais antigos.** Que teste foi acrescentado para os backups mais antigos? *Rubrica:* 3 = restaurar a partir de backups de uma semana;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX135 — Decisão de recuperação.** Quem autoriza a recuperação? *Rubrica:* 3 = o líder de segurança e o diretor de operações;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-45 -->
### Continue estudando — aula 45 (capítulo 45 de 50)

[← Capítulo 44](#ch-44) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 46 →](#ch-46)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-46"></a>

## Capítulo 46 — Projeto final de engenharia II

### Objetivos de aprendizagem

Você vai (1) construir e testar uma capacidade de recuperação; (2) medir em relação a um objetivo; (3) iterar até que o objetivo seja atingido.

### 46.1 Construindo

Lindiwe constrói o ambiente de recuperação em máquinas virtuais isoladas e escreve scripts para reconstruir cada componente do despacho: a conexão com o diretório, a fila de mensagens, o banco de dados, os servidores de aplicação, os certificados e o servidor de licenças. Cada script é idempotente, produzindo o mesmo resultado quando executado duas vezes, de modo que uma falha parcial pode ser repetida com segurança. Ela testa os scripts individualmente antes de combiná-los, mantendo um registro dos problemas encontrados e corrigidos. Ela guarda todos os scripts no controle de versão e registra cada execução de teste, com a data e o resultado, num diário do projeto.

### 46.2 Primeiro ensaio

O primeiro ensaio cronometrado leva seis horas e quarenta minutos, bem acima do objetivo de quatro horas. A maior parte do tempo vai para restaurar o banco de dados a partir do backup e para os passos manuais dos certificados. Lindiwe registra a linha do tempo minuto a minuto. O Prof. Hale lembra que um primeiro ensaio reprovado é normal e que a linha do tempo mostra exatamente onde trabalhar, o que é mais útil do que uma vaga impressão de que a recuperação é lenta. Ela compartilha a linha do tempo com o líder de segurança, destacando as duas maiores fontes de atraso.

### 46.3 Melhorias

Lindiwe faz três mudanças: restaurar o banco de dados a partir de um snapshot mais recente guardado no sistema de backup imutável, automatizar a instalação dos certificados e iniciar em paralelo os componentes independentes. O segundo ensaio leva quatro horas e dez minutos. Uma terceira mudança, preparar de antemão as imagens dos servidores de aplicação, leva o terceiro ensaio a três horas e vinte minutos, dentro do objetivo. Ela registra cada mudança e seu efeito sobre a linha do tempo. O Prof. Hale pede que ela coloque os três ensaios lado a lado num gráfico, mostrando como cada mudança encurtou uma parte específica da linha do tempo.

### 46.4 Repetibilidade

Um único ensaio bem-sucedido pode ser sorte. Lindiwe executa mais dois ensaios, em dias diferentes, com membros diferentes da equipe seguindo o runbook. Ambos terminam em até quatro horas. Ela observa que o passo mais lento que resta é a restauração do banco de dados, que cresce com o volume de dados, então o objetivo pode deixar de ser cumprido à medida que os dados do despacho crescerem. Ela recomenda repetir o ensaio a cada seis meses e depois de grandes mudanças. O líder de segurança inclui o ensaio semestral no calendário de segurança e designa um dono. Lindiwe escreve o procedimento para que funcionários novos possam conduzi-lo.

### Exemplo resolvido

Lindiwe constrói scripts de recuperação idempotentes, mede um primeiro ensaio de 6 horas e 40 minutos, melhora para 3 horas e 20 minutos e confirma a repetibilidade com outras pessoas da equipe.

> **Caso sintético.** Os ensaios são sintéticos.

### Erros e limites

Um único ensaio de recuperação bem-sucedido não prova que a recuperação é confiável.

### Exercícios

- **EX136 — Tempo do primeiro ensaio.** Quanto tempo levou o primeiro ensaio? *Rubrica:* 3 = seis horas e quarenta minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX137 — Significado de idempotente.** O que idempotente significa para os scripts dela? *Rubrica:* 3 = o mesmo resultado quando executados duas vezes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX138 — Passo lento restante.** Qual continua sendo o passo mais lento? *Rubrica:* 3 = a restauração do banco de dados;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-46 -->
### Continue estudando — aula 46 (capítulo 46 de 50)

[← Capítulo 45](#ch-45) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 47 →](#ch-47)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-47"></a>

## Capítulo 47 — Ensaio de falha e recuperação

### Objetivos de aprendizagem

Você vai (1) conduzir um exercício de falha realista; (2) observar o desempenho humano e técnico; (3) produzir lições para melhoria.

### 47.1 Cenário

Com a aprovação dos diretores da Saltmarsh, Lindiwe conduz um ensaio completo de recuperação no ambiente isolado, tratando-o como um incidente real. O cenário: às seis horas de uma segunda-feira de manhã, um ransomware cifrou os servidores do despacho e o compartilhamento dos backups noturnos. Restam apenas os backups imutáveis. A equipe de incidentes não conhece o cenário com antecedência. O Prof. Hale e o líder de segurança observam, registrando as decisões e os horários sem intervir. Lindiwe prepara os materiais do cenário, uma linha do tempo dos eventos injetados e uma ficha de observação para registrar o que acontece.

### 47.2 Desempenho

A equipe segue o processo de incidentes: detecção, decisão de recuperar, autorização pelos diretores nomeados e execução do runbook. A reconstrução se completa em três horas e trinta e cinco minutos. Ocorrem dois problemas. O gerente de plantão não consegue encontrar de início as credenciais offline, perdendo vinte minutos. Os dados restaurados são verificados com somas de verificação, e um lote é reprovado na verificação, então a equipe o restaura a partir do snapshot anterior. A equipe registra todas as ações no registro do incidente, que Lindiwe usa depois para reconstruir a linha do tempo com precisão.

### 47.3 Fatores humanos

Lindiwe observa que o estresse afetou a comunicação: duas pessoas executaram o mesmo script ao mesmo tempo, e os supervisores dos depósitos não foram avisados de quando passar para as listas impressas. Ela observa que esses são problemas de processo, e não falhas individuais. Ela recomenda um único papel de coordenador durante a recuperação e um modelo de mensagem para os depósitos. O Prof. Hale observa que os ensaios de recuperação testam as pessoas e a comunicação tanto quanto a tecnologia. Ela discute suas observações com os participantes numa breve conversa de encerramento, e eles concordam com as mudanças propostas e acrescentam uma própria, sobre as passagens de turno.

### 47.4 Lições

O relatório de lições lista cinco melhorias: etiquetar e conferir mensalmente o armazenamento das credenciais offline, acrescentar um papel de coordenador, usar o modelo de mensagem para os depósitos, automatizar a verificação por somas de verificação dos lotes restaurados e repetir o ensaio anualmente com pessoas diferentes. Cada uma tem um dono e uma data. Lindiwe observa que o ensaio cumpriu o objetivo apesar dos problemas, o que dá confiança e, ao mesmo tempo, mostra exatamente onde a margem poderia ser perdida. Os diretores aprovam as melhorias e pedem uma breve atualização do progresso em três meses, que Lindiwe agenda antes do fim do seu curso.

### Exemplo resolvido

Lindiwe conduz um ensaio de recuperação não anunciado, concluído em 3 horas e 35 minutos, observa problemas de credenciais e de comunicação e registra cinco melhorias com donos.

> **Caso sintético.** O ensaio é sintético.

### Erros e limites

Os ensaios de recuperação que testam apenas a tecnologia deixam passar as falhas de comunicação.

### Exercícios

- **EX139 — Duração do ensaio.** Quanto tempo levou a reconstrução? *Rubrica:* 3 = três horas e trinta e cinco minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX140 — Atraso das credenciais.** Quanto tempo se perdeu procurando as credenciais? *Rubrica:* 3 = vinte minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX141 — Papel de coordenador.** Por que acrescentar um papel de coordenador? *Rubrica:* 3 = duas pessoas executaram o mesmo script;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-47 -->
### Continue estudando — aula 47 (capítulo 47 de 50)

[← Capítulo 46](#ch-46) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 48 →](#ch-48)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-48"></a>

## Capítulo 48 — Dossiê de evidências

### Objetivos de aprendizagem

Você vai (1) reunir evidências que sustentem afirmações de segurança; (2) ligar cada afirmação a registros verificáveis; (3) declarar as limitações das evidências.

### 48.1 Afirmações

Lindiwe reúne um dossiê de evidências para os diretores e os auditores da Saltmarsh. Ela lista as afirmações: os ativos são conciliados semanalmente; os servidores atendem às regras de linha de base numa taxa medida; a adivinhação de senhas é detectada; os backups são verificados por testes de restauração; o despacho pode ser recuperado em até quatro horas. Cada afirmação precisa apontar para evidências. O Prof. Hale a adverte para não incluir afirmações que ela não consiga sustentar, por mais desejáveis que pareçam. Ela redige cada afirmação como uma única frase, a confere com o dono do controle e remove uma afirmação sobre a conscientização sobre phishing que não conseguia sustentar.

### 48.2 Ligando as evidências

Para cada afirmação, Lindiwe liga os registros: os relatórios de conciliação, com os números originais do laboratório, de 63 hosts não registrados e 90 hosts silenciosos, e as melhorias posteriores; os resultados da linha de base, começando em 72,0 por cento passando em todas as regras; as detecções da medida de adivinhação e seu teste de limite; os testes de restauração, começando em 98,4 por cento verificados; e as linhas do tempo dos ensaios de recuperação. Cada registro é indexado com uma soma de verificação. Um leitor consegue rastrear qualquer afirmação até sua fonte em minutos. O índice lista a data, o dono, o nome do arquivo e a soma de verificação de cada registro, agrupados pela afirmação que sustentam.

### 48.3 Limitações

O dossiê declara os limites com franqueza. A medida de adivinhação deixa passar os ataques lentos. O controle de mudança de endereço está verificado, mas não validado. Os ensaios de recuperação foram executados num ambiente isolado, que pode ser diferente de um incidente real. As regras de linha de base cobrem três configurações, e não o endurecimento completo. Lindiwe observa que declarar os limites torna o dossiê mais crível, porque os leitores podem ver o que foi e o que não foi demonstrado. O Prof. Hale revisa a seção e pede que ela coloque cada limitação logo depois da afirmação que ela afeta, para que os leitores não possam deixá-la passar.

### 48.4 Uso

O líder de segurança usa o dossiê na auditoria externa e na resposta a uma concorrência de um novo cliente. O auditor examina uma amostra de cinco afirmações e rastreia cada uma até as evidências sem dificuldade. Lindiwe aprende que um dossiê construído a partir de registros criados durante o trabalho normal custa pouco para manter, enquanto um montado sob a pressão de um prazo tende a conter lacunas e números incoerentes. O líder de segurança inclui o dossiê no trabalho de rotina da equipe, atribuindo ao dono de cada afirmação a tarefa de atualizar suas evidências depois de cada teste ou mudança relevante.

### Exemplo resolvido

Lindiwe reúne cinco afirmações, liga cada uma a registros com somas de verificação, inclusive os números dos laboratórios, declara quatro limitações e apoia uma auditoria que rastreia com facilidade as afirmações da amostra.

> **Caso sintético.** O dossiê é sintético.

### Erros e limites

Incluir afirmações sem evidências mina o dossiê inteiro.

### Exercícios

- **EX142 — Afirmação do dossiê.** Cite uma afirmação do dossiê. *Rubrica:* 3 = o despacho pode ser recuperado em até quatro horas;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX143 — Taxa inicial da linha de base.** Com que taxa de linha de base o registro começa? *Rubrica:* 3 = 72,0 por cento passando em todas as regras;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX144 — Amostra do auditor.** Quantas afirmações o auditor examinou na amostra? *Rubrica:* 3 = cinco;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-48 -->
### Continue estudando — aula 48 (capítulo 48 de 50)

[← Capítulo 47](#ch-47) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 49 →](#ch-49)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-49"></a>

## Capítulo 49 — Tese de engenharia

### Objetivos de aprendizagem

Você vai (1) escrever uma tese de engenharia em torno de um argumento central; (2) apresentar o projeto, as evidências e a avaliação; (3) refletir sobre a contribuição e os limites.

### 49.1 Argumento

A tese de Lindiwe argumenta que uma organização pequena pode alcançar uma recuperação verificável de ransomware dentro dos objetivos do negócio, combinando backups imutáveis, verificação por somas de verificação, reconstruções por script e ensaios regulares. O argumento se apoia no seu projeto final e no seu dossiê. O Prof. Hale pede que ela declare o argumento no primeiro parágrafo e faça cada capítulo contribuir para ele, para que os leitores possam acompanhar por que cada parte existe. Ela escreve um roteiro de uma página listando cada capítulo e a parte do argumento que ele sustenta, e o Prof. Hale o usa para guiar sua leitura dos rascunhos.

### 49.2 Estrutura

A tese tem capítulos sobre contexto e requisitos, trabalhos relacionados, análise de dependências, projeto e revisão, implementação, ensaios e resultados, avaliação e limitações. Os trabalhos relacionados se apoiam no Security Engineering de Anderson, na NIST SP 800-30 Revisão 1, para a avaliação de riscos, e na ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022), para o contexto do sistema de gestão. Ela cita cada fonte para pontos específicos, e não como decoração, e parafraseia as normas, em vez de citar passagens longas. Cada capítulo começa com um breve parágrafo que declara seu propósito e termina com um resumo do que mostrou. O Prof. Hale acha essa estrutura útil.

### 49.3 Avaliação

Lindiwe avalia o trabalho em relação ao objetivo: os ensaios cumpriram as quatro horas repetidas vezes, com o último ensaio, não anunciado, em três horas e trinta e cinco minutos. Ela também avalia em relação ao custo, mostrando que o ambiente de recuperação usa hardware existente. Ela compara com a situação anterior ao projeto, quando nenhuma reconstrução completa jamais tinha sido tentada. Ela toma o cuidado de descrever os resultados como válidos para o ambiente e os volumes de dados da Saltmarsh. Ela apresenta todos os tempos dos ensaios numa única tabela, com as mudanças feitas entre os ensaios, para que os examinadores possam ver como o resultado foi alcançado.

### 49.4 Contribuição e limites

Lindiwe identifica sua contribuição como um método de recuperação testado e documentado, com uma linha do tempo medida, mais o achado de que os ambientes de recuperação precisam estar isolados das credenciais da produção. Os limites incluem uma única organização, um ambiente de ensaio isolado e volumes de dados crescentes que ameaçam o objetivo. O Prof. Hale aprova a tese para submissão, observando que sua honestidade sobre os limites a fortalece, em vez de enfraquecê-la. Ela também sugere trabalhos futuros: testar a recuperação da folha de pagamento, medir como o crescimento do banco de dados afeta o tempo de restauração e repetir o ensaio com uma equipe de incidentes real de outra organização.

### Exemplo resolvido

Lindiwe argumenta a favor de uma recuperação verificável de ransomware numa organização pequena, estrutura os capítulos em torno do argumento, avalia em relação ao objetivo de quatro horas e declara a contribuição e os limites.

> **Caso sintético.** A tese é sintética.

### Erros e limites

Citar as fontes como decoração, e não para pontos específicos, enfraquece uma tese.

### Exercícios

- **EX145 — Argumento da tese.** O que a tese argumenta? *Rubrica:* 3 = organizações pequenas podem alcançar uma recuperação verificável;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX146 — Fonte de risco.** Que fonte sustenta a avaliação de riscos? *Rubrica:* 3 = NIST SP 800-30 Revisão 1;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX147 — Achado principal.** Que achado principal diz respeito aos ambientes de recuperação? *Rubrica:* 3 = precisam estar isolados das credenciais da produção;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-49 -->
### Continue estudando — aula 49 (capítulo 49 de 50)

[← Capítulo 48](#ch-48) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 50 →](#ch-50)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-50"></a>

## Capítulo 50 — Defesa final

### Objetivos de aprendizagem

Você vai (1) defender o trabalho de engenharia diante de examinadores; (2) responder a questionamentos sobre as evidências e a generalização; (3) planejar a continuidade do aprendizado.

### 50.1 Preparação

Lindiwe prepara uma apresentação de trinta minutos: o problema, o projeto, os achados da revisão, os ensaios e as evidências. Ela ensaia com colegas de turma que fazem perguntas hostis. Ela prepara slides de reserva com as linhas do tempo e os registros das somas de verificação. O Prof. Hale a aconselha a responder apenas o que consegue sustentar e a dizer com clareza quando uma pergunta vai além das suas evidências, porque os examinadores respeitam limites precisos mais do que palpites confiantes. Ela também prepara uma breve demonstração do script de verificação da restauração rodando sobre arquivos sintéticos, para o caso de os examinadores pedirem para vê-lo funcionando.

### 50.2 Questionamentos

Um examinador pergunta se a recuperação funcionaria caso os atacantes estivessem dentro da rede havia meses. Lindiwe responde que os backups imutáveis cobrem um período fixo e que os testes de restauração com backups de uma semana passaram, mas que um comprometimento não detectado por mais tempo poderia contaminar os backups; detectar as intrusões mais cedo é o controle complementar. Outro pergunta por que ela confiou nas somas de verificação registradas no sistema de backup; ela explica que o manifesto é, ele próprio, guardado de forma imutável junto com os backups. Um terceiro examinador pergunta sobre o custo, e ela mostra o hardware reaproveitado para o ambiente.

### 50.3 Resultado

Os examinadores aprovam Lindiwe com louvor, elogiando os ensaios medidos, a revisão independente e o dossiê. Eles sugerem que ela publique o método de recuperação como um guia para profissionais. A Saltmarsh lhe oferece um cargo na sua equipe de segurança. Ela reflete que o curso ligou a matemática, os sistemas e a gestão numa única prática de engenharia voltada para proteger as informações de uma organização real. Ela aceita o cargo e concorda em conduzir o próximo ensaio anual de recuperação. O parecer dos examinadores recomenda seu dossiê como exemplo para os futuros estudantes, e o Prof. Hale pede que ela fale à turma do ano seguinte sobre o projeto final.

### 50.4 Continuidade do aprendizado

Lindiwe planeja a continuidade do aprendizado: uma certificação profissional, um estudo mais aprofundado da resposta a incidentes e a manutenção das suas habilidades de recuperação por meio dos ensaios anuais da Saltmarsh. O Prof. Hale lembra que as normas e as ameaças mudam; a própria ISO/IEC 27000 foi revisada em 2026. O próximo curso desta área, governança de dados, examina como são tomadas as decisões sobre a qualidade, a propriedade e o uso dos dados, o que complementa os controles de segurança que ela construiu. Ela também planeja orientar um estagiário na Saltmarsh, transmitindo os hábitos que aprendeu: medir com cuidado, testar nos limites e declarar os limites.

### Exemplo resolvido

Lindiwe defende seu trabalho de recuperação, responde a questionamentos sobre comprometimentos de longo prazo e a confiança nas somas de verificação, é aprovada com louvor e planeja a continuidade do aprendizado.

> **Caso sintético.** A defesa é sintética.

### Erros e limites

Responder além das próprias evidências mina uma defesa.

### Exercícios

- **EX148 — Comprometimento longo.** O que complementa os backups imutáveis contra um comprometimento longo? *Rubrica:* 3 = detectar as intrusões mais cedo;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX149 — Armazenamento do manifesto.** Onde o manifesto das somas de verificação é guardado? *Rubrica:* 3 = de forma imutável, junto com os backups;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX150 — Resultado da defesa.** Qual é o resultado da defesa? *Rubrica:* 3 = aprovação com louvor;; 2 = parcialmente correto;; 1 = reprovação;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-50 -->
### Continue estudando — aula 50 (capítulo 50 de 50)

[← Capítulo 49](#ch-49) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX150. Lindiwe Dube, o Prof. Marcus Hale, a Brightwater Polytechnic, a Saltmarsh Logistics e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Cerca de quarenta milhões de eventos por dia.

**EX002.** Um encaminhador de logs parado ou desativado.

**EX003.** Perder detalhes de que um investigador pode precisar depois.

**EX004.** As contas com acesso à folha de pagamento menos os funcionários de finanças.

**EX005.** As ações não podem ser rastreadas até um indivíduo.

**EX006.** Removendo algumas arestas de confiança desnecessárias.

**EX007.** Os sinais sem fio chegam a atacantes fora do prédio.

**EX008.** O nivelamento de desgaste pode manter cópias antigas em blocos não endereçáveis.

**EX009.** Menos de dez minutos.

**EX010.** Contas sem login há noventa dias.

**EX011.** Contra uma lista de permissões com os doze códigos válidos.

**EX012.** Passar os argumentos como uma lista, sem shell.

**EX013.** O que foi encontrado, onde, por que importa, a probabilidade e a ação.

**EX014.** As fronteiras de confiança, onde os dados passam de uma zona de controle para outra.

**EX015.** As carteiras precisam ser retidas para verificações do seguro.

**EX016.** Pouco mais de quatro semanas.

**EX017.** A entrada dividida pela taxa de fechamento.

**EX018.** Removendo software sem uso.

**EX019.** Cerca de dez mil alarmes falsos.

**EX020.** Um processo de Poisson com média de doze por semana.

**EX021.** Depósitos maiores com equipe de TI dedicada.

**EX022.** Uma aplicação comprometida ler a memória de outro programa.

**EX023.** Por causa de um driver antigo.

**EX024.** Para um token de hardware ou um serviço gerenciado de chaves.

**EX025.** O módulo padrão unittest.

**EX026.** Uma variável de ambiente definida pelo agendador.

**EX027.** O formato é simples e a biblioteca não tem manutenção.

**EX028.** Ela o relata sem explorar mais.

**EX029.** Que a navegação na web é registrada.

**EX030.** Registros adulterados poderiam permitir que medicamentos estragados chegassem aos pacientes.

**EX031.** Senhas são enviadas em texto claro pela rede.

**EX032.** Malware que contata domínios incomuns.

**EX033.** Até onde um atacante pode se mover depois de entrar.

**EX034.** Uma conta dedicada apenas com os direitos de que os backups precisam.

**EX035.** Para que um atacante no servidor não possa apagar as evidências.

**EX036.** Primeiro um grupo de teste, com promoção para os demais depois de uma semana.

**EX037.** Contas separadas de leitura e gravação, limitadas às tabelas necessárias.

**EX038.** Usando consultas parametrizadas.

**EX039.** Uma cópia imutável que não pode ser alterada por um período definido.

**EX040.** O servidor aceita pedidos de exclusão de qualquer usuário logado.

**EX041.** Toda semana, contra bases de vulnerabilidades.

**EX042.** Assinar os pacotes com uma chave protegida.

**EX043.** A proteção contra modificação ou destruição indevidas da informação.

**EX044.** A categoria geral toma o mais alto dos três impactos.

**EX045.** Combinar vários controles independentes.

**EX046.** Os endereços de entrega completos.

**EX047.** Dois requisitos.

**EX048.** A exclusão dos dados, a remoção das contas e a desconexão da rede.

**EX049.** Esperar durante a noite que um analista revise os alertas.

**EX050.** Desacelerar as tentativas e depois exigir verificação adicional.

**EX051.** As medianas e o décimo mais lento.

**EX052.** Os novos funcionários não recebem acesso até a aprovação.

**EX053.** O serviço intermediário que expõe apenas as funções necessárias.

**EX054.** Uma porta não documentada.

**EX055.** Do sistema de roteamento dos depósitos.

**EX056.** Chaves de segurança de hardware.

**EX057.** A renovação dependia de alguém se lembrar.

**EX058.** A declaração de aplicabilidade.

**EX059.** Organizacionais, de pessoas, físicos e tecnológicos.

**EX060.** Governar, Identificar, Proteger, Detectar, Responder e Recuperar.

**EX061.** Autenticação multifator para o acesso remoto e relatos de incidentes em até 24 horas.

**EX062.** Em até catorze dias.

**EX063.** Guardar os logs por um ano, com acesso restrito e campos pessoais minimizados.

**EX064.** Sessenta e três hosts.

**EX065.** Noventa endereços registrados.

**EX066.** O gerente do depósito, com o apoio da TI.

**EX067.** A integridade dos endereços de entrega.

**EX068.** Uma fila de mensagens cheia que atrasa as confirmações.

**EX069.** Pessoas internas que exportam listas de clientes.

**EX070.** O gerente do depósito e o líder de segurança.

**EX071.** Guardando as evidências com somas de verificação numa pasta restrita.

**EX072.** Uma porta que ela pensava estar destrancada tem uma fechadura com código.

**EX073.** Um orçamento pequeno.

**EX074.** Dá acesso amplo à rede depois de conectada.

**EX075.** Uma segunda chave registrada e uma ligação verificada para a central de atendimento.

**EX076.** Uma vez dentro, um atacante herda a confiança.

**EX077.** A mediação completa.

**EX078.** As contas de usuário, a configuração e os dados.

**EX079.** A aprovação por uma segunda pessoa das mudanças de endereço de alto valor.

**EX080.** Cerca de cinco por cento dos pedidos.

**EX081.** Encenando mudanças suspeitas sintéticas e conferindo os alertas.

**EX082.** 278 servidores, 92,7 por cento.

**EX083.** 253 servidores, 84,3 por cento.

**EX084.** 216 servidores, 72,0 por cento.

**EX085.** u17, u402 e u977.

**EX086.** Suas 61 falhas estão espalhadas ao longo do dia, e não em rajadas.

**EX087.** A adivinhação de senhas lenta e paciente.

**EX088.** Dez falhas em até quatro minutos.

**EX089.** Uma rajada de dez falhas abrangendo exatamente cinco minutos.

**EX090.** Para que as mudanças futuras possam ser conferidas rapidamente.

**EX091.** Os administradores, com chaves físicas.

**EX092.** A aproximação do crachá combinada com um código pessoal.

**EX093.** As contas cadastradas, os logins que usam um segundo fator e as exceções abertas.

**EX094.** 492 arquivos, 98,4 por cento.

**EX095.** Estavam numa pasta acrescentada depois que a seleção do backup foi definida.

**EX096.** Perder no máximo uma hora de dados e voltar em até quatro horas.

**EX097.** As entregas de medicamentos refrigerados.

**EX098.** Um local desconhecido das listas impressas e pessoas que já saíram na lista de contatos.

**EX099.** Registradores independentes, lidos na entrega e guardados separadamente.

**EX100.** Elas compartilhavam uma única credencial.

**EX101.** Seis campos.

**EX102.** Um aumento repentino nas requisições de endereços de clientes.

**EX103.** Pelo menos cinco analistas.

**EX104.** Um serviço externo à noite e a equipe da Saltmarsh de dia.

**EX105.** Um gerente de plantão da Saltmarsh, em minutos.

**EX106.** Praticamente dobra a carga do processador do firewall.

**EX107.** Em até dezoito meses.

**EX108.** Os eventos de autenticação e de administração.

**EX109.** Cerca de quarenta minutos.

**EX110.** Bloquear a conta vítima de phishing.

**EX111.** Sua exceção foi prorrogada duas vezes sem revisão.

**EX112.** Quatro incidentes.

**EX113.** Nenhum monitoramento das regras de encaminhamento de e-mail.

**EX114.** Verificado, mas ainda não validado.

**EX115.** Num único arquivo de configuração.

**EX116.** Um colega sem nenhum envolvimento segue cada runbook.

**EX117.** Alguns controles param se uma única pessoa estiver ausente.

**EX118.** O analista bloqueia a conta sinalizada.

**EX119.** O alerta de download em massa.

**EX120.** Para mostrar a melhoria e sua causa.

**EX121.** O que cobre todos os notebooks, inclusive os terminais do armazém.

**EX122.** Geradas a partir da fonte única de identidades.

**EX123.** Um produto de análise avançada.

**EX124.** A implantação em etapas pelos depósitos.

**EX125.** Uso confirmado de uma conta por alguém que não é seu dono.

**EX126.** A direção é favorável, mas a evidência é fraca.

**EX127.** Escrita e negociação.

**EX128.** Como em andamento, com datas-alvo.

**EX129.** Que os funcionários comunicassem rapidamente na vez seguinte.

**EX130.** Recuperar o despacho em até quatro horas.

**EX131.** Um servidor de licenças para um dos componentes.

**EX132.** Apenas suas dependências são documentadas, para um projeto posterior.

**EX133.** O ambiente de recuperação usa as credenciais de administrador da produção.

**EX134.** Restaurar a partir de backups de uma semana.

**EX135.** O líder de segurança e o diretor de operações, em conjunto.

**EX136.** Seis horas e quarenta minutos.

**EX137.** Executar um script duas vezes dá o mesmo resultado.

**EX138.** A restauração do banco de dados.

**EX139.** Três horas e trinta e cinco minutos.

**EX140.** Vinte minutos.

**EX141.** Duas pessoas executaram o mesmo script ao mesmo tempo, sob estresse.

**EX142.** O despacho pode ser recuperado em até quatro horas.

**EX143.** 72,0 por cento dos servidores passando em todas as regras.

**EX144.** Cinco afirmações.

**EX145.** Que uma organização pequena pode alcançar uma recuperação verificável de ransomware dentro dos objetivos.

**EX146.** NIST SP 800-30 Revisão 1.

**EX147.** Eles precisam estar isolados das credenciais da produção.

**EX148.** Detectar as intrusões mais cedo.

**EX149.** De forma imutável, junto com os backups.

**EX150.** Aprovação com louvor.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. https://doi.org/10.1002/9781119644682
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5
- National Institute of Standards and Technology. (2004). *Standards for security categorization of federal information and information systems* (FIPS 199). https://doi.org/10.6028/NIST.FIPS.199
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- Nieles, M., Dempsey, K., & Pillitteri, V. Y. (2017). *An introduction to information security* (NIST SP 800-12 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-12r1
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
