# Segurança da Informação: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 117, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3; os capítulos 11–50 (EX031–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

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

- **EX002 — Fonte silenciosa.** O que pode significar uma queda súbita na taxa de eventos de uma fonte? *Rubrica:* 3 = um encaminhador parado;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX003 — Risco do resumo.** Qual é o risco de resumir logs antigos? *Rubrica:* 3 = perder detalhes de que os investigadores precisam;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX004 — Diferença vazia.** Que diferença de conjuntos deve ser vazia? *Rubrica:* 3 = contas com acesso à folha de pagamento menos funcionários de finanças;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX005 — Contas compartilhadas.** Por que as contas compartilhadas prejudicam a responsabilização? *Rubrica:* 3 = as ações não podem ser rastreadas até uma pessoa;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX006 — Cortando caminhos.** Como muitos caminhos de ataque podem ser cortados de uma vez? *Rubrica:* 3 = remover algumas arestas de confiança;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX007 — Vazamento de rádio.** Por que a cifração importa para o sem fio dos depósitos? *Rubrica:* 3 = os sinais chegam além do prédio;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX008 — Remanência em SSD.** Por que dados excluídos podem sobreviver em unidades de estado sólido? *Rubrica:* 3 = o nivelamento de desgaste mantém cópias antigas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX009 — Autonomia do nobreak.** Que autonomia o nobreak dá com a carga atual? *Rubrica:* 3 = menos de dez minutos;; 2 = correto;; 1 = errado;; 0 = nenhuma.

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

- **EX010 — Contas inativas.** O que o primeiro script conta? *Rubrica:* 3 = contas sem login há noventa dias;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX011 — Lista de permissões.** Como o código de depósito é validado? *Rubrica:* 3 = contra os doze códigos válidos;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX012 — Correção da injeção.** Como o script de redefinição deve chamar os comandos? *Rubrica:* 3 = passar os argumentos como uma lista;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX014 — Fronteiras de confiança.** O que o Prof. Hale pede que ela marque? *Rubrica:* 3 = fronteiras de confiança;; 2 = correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX015 — Resposta do registro.** Por que a pasta foi movida em vez de excluída? *Rubrica:* 3 = as carteiras são retidas para verificações do seguro;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX017 — Estado estacionário.** Qual é a fórmula do acúmulo estacionário? *Rubrica:* 3 = entrada dividida pela taxa de fechamento;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX018 — Reduzir a entrada.** Como a entrada pode ser reduzida? *Rubrica:* 3 = remover software sem uso;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX020 — Semanas de Poisson.** Que modelo descreve as detecções semanais? *Rubrica:* 3 = Poisson com média doze;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX021 — Fator de confusão dos notebooks.** O que poderia explicar menos detecções com notebooks novos? *Rubrica:* 3 = depósitos maiores com equipe de TI;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX022 — Separação do kernel.** O que a separação entre kernel e aplicações impede? *Rubrica:* 3 = uma aplicação ler a memória de outra;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX023 — Lacuna do secure boot.** Por que o secure boot estava desativado em alguns notebooks? *Rubrica:* 3 = um driver antigo;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX024 — Chave de assinatura.** Para onde a chave de assinatura de código deve ir? *Rubrica:* 3 = um token de hardware ou um serviço gerenciado de chaves;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX025 — Módulo de testes.** Que módulo executa os testes dela? *Rubrica:* 3 = unittest;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX026 — Armazenamento de segredos.** De onde a ferramenta lê as credenciais? *Rubrica:* 3 = uma variável de ambiente definida pelo agendador;; 2 = correto;; 1 = código;; 0 = nenhuma.

- **EX027 — Escolha do interpretador.** Por que escrever o próprio interpretador? *Rubrica:* 3 = formato simples, biblioteca sem manutenção;; 2 = correto;; 1 = nada;; 0 = nenhuma.

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

- **EX028 — Relato sem teste.** O que Lindiwe faz ao perceber a exposição? *Rubrica:* 3 = relata sem testar mais;; 2 = correto;; 1 = testa;; 0 = nenhuma.

- **EX029 — Lacuna do aviso.** O que o aviso de monitoramento omitia? *Rubrica:* 3 = o registro da navegação na web;; 2 = correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX030 — Ligação com a segurança física.** Por que os registros de temperatura importam para a segurança das pessoas? *Rubrica:* 3 = a adulteração poderia permitir que medicamentos estragados chegassem aos pacientes;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Lindiwe Dube, o Prof. Marcus Hale, a Brightwater Polytechnic, a Saltmarsh Logistics e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
