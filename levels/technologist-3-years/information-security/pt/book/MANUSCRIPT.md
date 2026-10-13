# Segurança da Informação: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 071, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 30 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 9–30 (EX025–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de tecnólogo que aprendem a configurar, verificar e manter os controles de segurança da informação de uma instituição de lazer sem fins lucrativos com várias unidades.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios verificam estações de trabalho sintéticas contra uma linha de base de quatro itens, revisam uma lista sintética de regras de firewall em busca de regras amplas, sombreadas e sem uso e analisam um log sintético de autenticação para classificar as origens de logins com falha. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um estudante de tecnólogo desde os sistemas operacionais, as redes, os scripts e os logs, passando pelo endurecimento, pelas correções e pela varredura, depois pelas contas, pela autenticação, pelos segredos, pelos firewalls, pelas redes sem fio, pelos endpoints, pelo e-mail, pelos backups, pela criptografia e pela segurança física, até o monitoramento, os incidentes, os fornecedores, os procedimentos, a automação, a passagem de serviço, um estágio e um projeto aplicado. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Jamal Haddad** | Estudante de tecnólogo | Inventado |
| **Sra. Fiona Grant** | Tutora | Inventada |
| **Northgate College of Technology** | Faculdade fictícia | Inventada |
| **Riverbend Leisure Trust** | Instituição de lazer fictícia sem fins lucrativos, com nove centros, cerca de 350 funcionários e 210 estações de trabalho | Inventada |

### Fontes principais

ISO/IEC 27000:2026; ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); ISO/IEC 27002:2022; FIPS 199, [doi:10.6028/NIST.FIPS.199](https://doi.org/10.6028/NIST.FIPS.199); NIST CSWP 29 (CSF 2.0); Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Começando na Northgate

### Objetivos de aprendizagem

Você vai (1) descrever o papel do tecnólogo na segurança da informação; (2) conhecer o caso que acompanha o livro; (3) planejar o aprendizado prático ao longo de três anos.

### 1.1 O estudante e o papel

Jamal Haddad começa um curso de tecnólogo de três anos em segurança da informação no fictício Northgate College of Technology. Sua tutora é a Sra. Fiona Grant, que trabalhou dez anos como administradora de sistemas antes de lecionar. Ela explica que os tecnólogos são as pessoas que configuram, verificam e mantêm os controles de segurança todos os dias: criam contas, aplicam atualizações, revisam logs e respondem a alertas. O curso é prático, com trabalho de laboratório toda semana e um estágio no último ano. Jamal gosta de problemas práticos.

### 1.2 A organização do caso

A parceira de estágio de Jamal é o fictício Riverbend Leisure Trust, uma instituição sem fins lucrativos que administra nove centros de lazer com piscinas, academias e cafés. Ela emprega cerca de 350 funcionários e usa aproximadamente 210 estações de trabalho, um sistema de associados e reservas, caixas com pagamento por cartão e câmeras de circuito fechado. Os dados pessoais dos associados, os dados de pagamento e os questionários de saúde para o ingresso na academia precisam de proteção. A Sra. Grant observa que as organizações de lazer são alvos frequentes porque guardam dados de pagamento, mas têm equipes de TI pequenas. A equipe de TI é formada por um gerente de TI e um técnico que se desloca entre os centros.

### 1.3 Como o curso funciona

O primeiro ano cobre sistemas operacionais, redes, scripts, logs e conceitos centrais de segurança, terminando com endurecimento, correções e varredura de vulnerabilidades. O segundo ano cobre contas, autenticação, segredos, firewalls, redes sem fio, endpoints, e-mail, backups, criptografia e segurança física. O terceiro ano cobre monitoramento, tratamento de incidentes, fornecedores, procedimentos, conscientização, automação, documentação, o estágio e um projeto aplicado. Jamal observa que cada tema se liga a algo que a equipe de TI de duas pessoas do Riverbend faz toda semana. Ele copia a lista de módulos na primeira página do caderno e marca cada módulo com a tarefa do Riverbend em que espera que ele ajude, para poder verificar depois se a ligação se confirmou.

### 1.4 Hábitos de aprendizagem

A Sra. Grant pede aos estudantes que mantenham um caderno de laboratório registrando cada comando executado, o que ele fez e o que aprenderam. Ela explica que os tecnólogos precisam ser capazes de repetir um trabalho exatamente e explicá-lo a outras pessoas, sobretudo depois de um incidente. Jamal também monta um pequeno laboratório em casa com máquinas virtuais, para poder praticar sem tocar em nenhum sistema real. Ele observa que praticar com segurança num laboratório é o primeiro hábito profissional que o curso ensina. A Sra. Grant confere os cadernos a cada duas semanas.

### Exemplo resolvido

Jamal começa o curso, conhece os nove centros do Riverbend e sua equipe de TI de duas pessoas, mapeia os três anos e inicia um caderno e um laboratório em casa.

> **Caso sintético.** A Northgate, o Riverbend e todas as pessoas são sintéticos.

### Erros e limites

Praticar em sistemas reais sem permissão é inseguro e pode ser ilegal.

### Exercícios

- **EX001 — Trabalho do tecnólogo.** O que os tecnólogos fazem diariamente? *Rubrica:* 3 = configurar, verificar e manter controles;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX002 — Porte do Riverbend.** Quantos funcionários o Riverbend emprega? *Rubrica:* 3 = cerca de 350;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX003 — Propósito do caderno.** Por que manter um caderno de laboratório? *Rubrica:* 3 = para repetir e explicar o trabalho;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — A informação num fundo de lazer

### Objetivos de aprendizagem

Você vai (1) identificar as informações que um fundo de lazer guarda; (2) classificar sua sensibilidade; (3) rastrear onde estão armazenadas e quem as usa.

### 2.1 O que o Riverbend guarda

Jamal lista as informações do Riverbend: nomes, endereços e contatos dos associados; dados de cartões de pagamento processados nos caixas e on-line; dados bancários de débito automático; questionários de saúde da academia; registros e escalas dos funcionários; listas de presença das aulas de natação infantil; e imagens das câmeras. A Sra. Grant pede que ele anote quem usa cada tipo. Os recepcionistas usam os dados dos associados, os instrutores usam os questionários de saúde e a equipe financeira usa os dados bancários. Ele aprende que saber quem precisa da informação é o ponto de partida para decidir quem deve acessá-la. Ele registra cada tipo numa tabela com seus usuários.

### 2.2 Sensibilidade

Jamal classifica a sensibilidade usando três perguntas tiradas dos objetivos de segurança: que dano haveria se a informação fosse divulgada, alterada ou ficasse indisponível? Os questionários de saúde e as listas das crianças são altamente sensíveis à divulgação. Os dados bancários são sensíveis à alteração, porque dados modificados poderiam desviar pagamentos. O sistema de reservas importa sobretudo pela disponibilidade, já que os centros não conseguem receber os associados sem ele. A FIPS 199 descreve essa abordagem de classificar separadamente o impacto sobre a confidencialidade, a integridade e a disponibilidade, e Jamal a considera útil também para organizações pequenas. Ele acrescenta à tabela uma coluna com o objetivo mais importante para cada tipo.

### 2.3 Onde a informação fica

Jamal rastreia o armazenamento. Os dados dos associados ficam num sistema de reservas hospedado na nuvem. Os questionários de saúde ficam em papel no escritório de cada academia e depois são digitalizados para uma unidade compartilhada. As listas de natação são impressas diariamente. As imagens das câmeras ficam em gravadores em cada centro. Ele encontra os questionários digitalizados numa pasta que todos os funcionários podem abrir. Ele relata isso ao gerente de TI do Riverbend, que a restringe a instrutores e gerentes no mesmo dia. Ele acrescenta à tabela uma coluna de armazenamento, anotando para cada tipo se ele fica na nuvem, numa unidade compartilhada, em papel ou num dispositivo local de um centro.

### 2.4 Papel e pessoas

Nem toda informação é digital. Listas impressas deixadas à beira da piscina podem ser lidas por qualquer pessoa que passe. Jamal sugere pranchetas com capa e o recolhimento das listas ao fim de cada sessão para descarte seguro. A Sra. Grant explica que a segurança da informação cobre também o papel e as conversas. Recepcionistas que leem em voz alta os dados de um associado numa fila podem divulgar informações tão facilmente quanto um banco de dados invadido. O gerente do centro testa as pranchetas com capa por um mês e as mantém. Jamal também sugere que os recepcionistas peçam aos associados que confiram os dados numa tela em vez de lê-los em voz alta, e dois centros adotam essa prática.

### Exemplo resolvido

Jamal lista as informações do Riverbend e seus usuários, classifica a sensibilidade por objetivo, encontra uma pasta de questionários compartilhada em excesso e sugere cobrir as listas impressas.

> **Caso sintético.** Os tipos de informação são sintéticos.

### Erros e limites

Formulários sensíveis digitalizados muitas vezes acabam em pastas que todos podem abrir.

### Exercícios

- **EX004 — Usuários dos questionários.** Quem usa os questionários de saúde? *Rubrica:* 3 = os instrutores;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX005 — Risco dos dados bancários.** Qual objetivo importa mais para os dados bancários? *Rubrica:* 3 = integridade;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX006 — Correção da pasta.** O que acontece com a pasta dos questionários? *Rubrica:* 3 = é restrita a instrutores e gerentes;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Administração de sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) gerenciar usuários e permissões em sistemas operacionais comuns; (2) controlar serviços e itens de inicialização; (3) ler informações do sistema com segurança.

### 3.1 Usuários e grupos

No laboratório, Jamal cria contas de usuário e grupos numa máquina virtual de estilo Windows e numa máquina virtual Linux. Ele aprende que as permissões ficam melhor atribuídas a grupos, como recepção ou financeiro, do que a indivíduos, porque as pessoas mudam de função. A Sra. Grant mostra como um único grupo mal configurado pode dar a muitas pessoas acessos que elas não deveriam ter. No Riverbend, ele descobre que a maioria dos funcionários pertence a um grupo com acesso a todas as pastas compartilhadas. Ele propõe quatro grupos baseados nas funções e lista as pastas que cada um deve alcançar.

### 3.2 Direitos de administrador

Jamal aprende a diferença entre contas padrão e contas de administrador. Os administradores podem instalar software, mudar configurações de segurança e ler todos os arquivos. Ele descobre que os computadores da recepção do Riverbend entram automaticamente com uma conta de administrador para que a equipe possa instalar drivers de impressora. Qualquer malware executado nesses computadores ganharia controle total. Ele recomenda contas padrão com um pacote de drivers de impressora pré-instalado, e o gerente de TI concorda em mudar um centro como teste. Depois de um mês, o centro do teste não relata problemas, e o gerente de TI planeja a mudança para os outros oito centros ao longo do período seguinte.

### 3.3 Serviços

Os sistemas operacionais executam serviços em segundo plano, e cada serviço em execução é um possível ponto de entrada. Jamal lista os serviços de uma máquina de laboratório e identifica os desnecessários, como o acesso remoto ao registro e o compartilhamento de arquivos num computador que não compartilha nada. Ele os desativa e confirma que a máquina continua funcionando. A Sra. Grant explica que reduzir os serviços em execução diminui a superfície de ataque, um princípio básico de endurecimento. Ele registra no caderno cada serviço desativado com o motivo e depois usa a lista para montar uma breve lista de verificação de serviços para os novos computadores do Riverbend, que o gerente de TI adota em toda nova instalação.

### 3.4 Investigação segura

Jamal aprende a coletar informações com segurança: listar os usuários conectados, os processos em execução, as conexões de rede abertas e as entradas recentes de log sem alterar nada. Ele escreve esses comandos no caderno. A Sra. Grant explica que, durante um incidente, comandos descuidados podem destruir evidências, por isso os tecnólogos precisam de um conjunto padrão de verificações somente de leitura que possam executar com calma. Ele testa a lista numa máquina de laboratório e confirma que nenhum dos comandos altera arquivos, configurações ou logs. A Sra. Grant pede que ele acrescente um passo registrando a data e a hora de cada comando, para que os leitores posteriores saibam exatamente quando a informação foi coletada e em que ordem.

### Exemplo resolvido

Jamal gerencia usuários por grupo, encontra logins automáticos de administrador na recepção, desativa serviços desnecessários e monta uma lista de verificação de investigação somente de leitura.

> **Caso sintético.** Os sistemas são sintéticos.

### Erros e limites

Logins automáticos de administrador dão a qualquer malware controle total.

### Exercícios

- **EX007 — Permissões por grupo.** Por que atribuir permissões a grupos? *Rubrica:* 3 = as pessoas mudam de função;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX008 — Risco da recepção.** Que risco os computadores da recepção apresentam? *Rubrica:* 3 = login automático de administrador;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX009 — Redução de serviços.** O que faz desativar os serviços desnecessários? *Rubrica:* 3 = diminui a superfície de ataque;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Redes na prática

### Objetivos de aprendizagem

Você vai (1) mapear a rede de uma organização pequena; (2) identificar dispositivos e serviços; (3) separar as redes por finalidade.

### 4.1 Mapeamento

Jamal mapeia a rede de um centro do Riverbend com a permissão do gerente de TI. Ela tem um roteador ligado à internet, um switch, computadores da recepção, computadores do escritório, caixas de cartão, gravadores das câmeras, uma rede sem fio de visitantes e uma rede sem fio da equipe. Ele desenha cada dispositivo e cada conexão. A Sra. Grant pede que ele identifique quais dispositivos lidam com dados de pagamento, porque esses precisam da proteção e da separação mais fortes. Ele confere o desenho com a lista de dispositivos conectados do switch e encontra dois dispositivos que tinha deixado de fora: uma impressora no escritório do gerente e um pequeno ponto de acesso sem fio instalado pelo fornecedor do café.

### 4.2 Endereços e serviços

Jamal registra o endereço de rede de cada dispositivo e os serviços que ele oferece. Primeiro ele usa uma varredura autorizada na rede do laboratório para aprender as ferramentas, depois executa uma varredura limitada no centro fora do horário de funcionamento, com permissão por escrito. Ele encontra um gravador de câmeras que oferece uma interface web com senha padrão. Ele relata o achado, e o gerente de TI troca a senha e restringe o acesso. Ele também confirma que a rede sem fio de visitantes não alcança os computadores da equipe, tentando conectar-se a partir de um notebook na rede de visitantes na cópia de laboratório da configuração. O teste falha, como pretendido, e ele registra o resultado.

### 4.3 Separação

No centro, os caixas de cartão, os computadores da equipe e os gravadores das câmeras compartilham uma única rede. Se um computador da equipe fosse infectado, o malware poderia alcançar os caixas. Jamal propõe segmentos de rede separados: um para os caixas, um para a equipe, um para as câmeras e um para os visitantes, com regras de firewall que permitam apenas o tráfego necessário. A Sra. Grant explica que as normas do setor de cartões de pagamento tratam a separação dos sistemas de cartão das outras redes como um modo de limitar quais sistemas precisam cumprir seus requisitos mais rigorosos. O gerente de TI concorda em começar pelos caixas, porque os dados de pagamento trazem o maior risco, e separar as câmeras em seguida. Jamal redige as regras de firewall necessárias para que os caixas alcancem o provedor de pagamentos e nada mais.

### 4.4 Documentação

Jamal produz um diagrama de rede e uma lista de dispositivos do centro, guardados na documentação de TI do Riverbend. Ele anota a data e quem fez a verificação. A Sra. Grant lembra que a documentação de rede fica desatualizada depressa e deve ser revisada sempre que dispositivos forem acrescentados. O gerente de TI pede a Jamal que repita o mapeamento em mais dois centros durante o estágio. Ele cria um lembrete para revisar o diagrama a cada seis meses e sempre que um novo dispositivo for instalado. O gerente de TI diz que o diagrama é o primeiro registro preciso da rede do centro que ele já teve e pede a Jamal que use o mesmo formato nos outros centros.

### Exemplo resolvido

Jamal mapeia a rede de um centro, encontra por uma varredura autorizada um gravador de câmeras com senha padrão, propõe quatro segmentos e documenta a rede.

> **Caso sintético.** As redes são sintéticas.

### Erros e limites

Fazer varreduras sem permissão por escrito é inaceitável, mesmo numa rede amigável.

### Exercícios

- **EX010 — Identificação de pagamento.** Quais dispositivos precisam ser identificados de modo especial? *Rubrica:* 3 = os que lidam com dados de pagamento;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX011 — Achado na câmera.** O que a varredura encontrou no gravador de câmeras? *Rubrica:* 3 = uma senha padrão;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX012 — Segmentos propostos.** Cite os quatro segmentos propostos. *Rubrica:* 3 = caixas, equipe, câmeras, visitantes;; 2 = todos;; 1 = alguns;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Noções básicas de scripts em Python

### Objetivos de aprendizagem

Você vai (1) escrever scripts simples em Python para tarefas de segurança; (2) ler arquivos CSV e de texto; (3) produzir saídas claras e repetíveis.

### 5.1 Primeiros scripts

Jamal aprende Python usando apenas a biblioteca padrão, para que os scripts rodem em qualquer máquina. Seu primeiro script lê uma lista de contas de usuário do Riverbend num arquivo CSV e conta as contas por grupo. O segundo lista as contas que não fazem login há sessenta dias. A Sra. Grant explica que os scripts transformam verificações manuais lentas em verificações rápidas e repetíveis, o que é essencial para equipes de TI pequenas responsáveis por centenas de dispositivos. Ele executa os dois scripts semanalmente no laboratório e compara os resultados com contagens manuais para confirmar que estão corretos.

### 5.2 Leitura de arquivos

Jamal aprende a ler arquivos de texto e CSV com o módulo csv e a lidar com problemas: linhas vazias, colunas ausentes e valores inesperados. Seu script pula as linhas ruins e as relata, para que os problemas nos dados fiquem visíveis em vez de escondidos. Ele o testa com um arquivo que contém erros deliberados. Ele aprende que os scripts de segurança precisam falhar de forma ruidosa, porque um script que ignora em silêncio metade da entrada dá uma falsa tranquilidade. Seu arquivo de teste contém dez erros deliberados, e o script relata os dez com os números de linha, o que lhe dá confiança de que não vai esconder problemas em dados reais.

### 5.3 Saída clara

Jamal formata a saída para pessoas: um título, a data, os totais e uma lista dos itens que exigem ação, ordenados por importância. Ele também grava os resultados num arquivo CSV para os registros do gerente de TI. A Sra. Grant pede que ele inclua a versão do script e o nome do arquivo de entrada em cada relatório, para que qualquer pessoa possa rastrear um resultado até exatamente o que o produziu. O gerente de TI diz que os relatórios são fáceis de ler e pede a Jamal que use o mesmo formato em todos os scripts que escrever durante o estágio. A Sra. Grant usa um de seus relatórios como exemplo em aula.

### 5.4 Hábitos seguros

Jamal guarda os scripts numa pasta com controle de versão, nunca escreve senhas neles e mantém as saídas que contêm dados pessoais numa pasta restrita. Ele acrescenta comentários explicando por que cada verificação existe. A Sra. Grant observa que os scripts muitas vezes sobrevivem a seus autores, por isso comentários claros e o tratamento seguro dos dados fazem parte de escrever boas ferramentas de segurança. Ele também escreve um breve arquivo README para cada script, explicando o que ele verifica, de que entrada precisa e o que sua saída significa. A Sra. Grant observa que esses arquivos permitem que o gerente de TI execute os scripts depois que Jamal for embora.

### Exemplo resolvido

Jamal escreve scripts com a biblioteca padrão que contam contas e sinalizam inatividade, trata entradas ruins de forma ruidosa, formata saídas rastreáveis e mantém os scripts seguros.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Scripts que pulam em silêncio as entradas ruins dão uma falsa tranquilidade.

### Exercícios

- **EX013 — Script de inatividade.** Quais contas o segundo script lista? *Rubrica:* 3 = sem login há sessenta dias;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX014 — Linhas ruins.** Como o script trata as linhas ruins? *Rubrica:* 3 = pula e as relata;; 2 = correto;; 1 = ignorá-las;; 0 = nenhuma.

- **EX015 — Rastreabilidade.** O que cada relatório inclui para permitir o rastreamento? *Rubrica:* 3 = a versão do script e o nome do arquivo de entrada;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Logs e formatos de log

### Objetivos de aprendizagem

Você vai (1) ler formatos comuns de log; (2) extrair campos com padrões; (3) entender os fusos horários e os relógios nos logs.

### 6.1 Por que os logs importam

Os logs registram o que os sistemas fizeram: logins, falhas, alterações e erros. Jamal aprende que os logs são o meio pelo qual os tecnólogos descobrem o que aconteceu depois de um problema. Os sistemas do Riverbend produzem logs em formatos diferentes: o sistema de reservas exporta CSV, os servidores gravam linhas de texto e o firewall usa um formato próprio. A Sra. Grant explica que conseguir ler qualquer formato é uma habilidade central do tecnólogo. Ele coleta uma linha de exemplo de cada formato e anota os campos no caderno, o que o ajuda depois a reconhecer cada formato rapidamente. O gerente de TI confirma que esses são os logs que ele mais consulta quando algo dá errado num centro.

### 6.2 Extração de campos

Jamal aprende expressões regulares com o módulo re do Python para extrair campos de linhas de texto, como a hora, o nome de usuário e o endereço de origem de um registro de login. Ele pratica com logs sintéticos e testa seu padrão contra linhas incomuns, como nomes de usuário com pontos ou endereços em formatos diferentes. Ele aprende que um padrão que funciona nas primeiras cem linhas pode falhar na milésima, por isso testar com dados variados é importante. Ele mantém um arquivo de teste com linhas incomuns e executa contra ele todo padrão novo antes de usá-lo.

### 6.3 Hora e relógios

Os horários dos logs só ajudam se os relógios estiverem certos. Jamal descobre que o relógio do gravador de câmeras de um centro está onze minutos atrasado, o que confundiria qualquer investigação que comparasse as imagens com os registros dos caixas. Ele também aprende que alguns sistemas registram em hora local e outros em tempo universal. Ele recomenda sincronizar todos os relógios com uma fonte de hora confiável e registrar os fusos horários explicitamente. A Sra. Grant observa que relógios desencontrados já prejudicaram muitas investigações. O gerente de TI configura todos os gravadores e servidores para usar a mesma fonte de hora, e Jamal verifica uma semana depois que todos os relógios coincidem.

### 6.4 Guarda dos logs

Jamal aprende que os logs precisam ser guardados por tempo suficiente para investigar problemas, protegidos contra alteração e armazenados onde os atacantes não possam apagá-los. O Riverbend guarda os logs dos servidores por apenas sete dias em cada servidor. Ele recomenda encaminhá-los a um repositório central mantido por noventa dias, com acesso limitado à equipe de TI. Ele observa que os logs que contêm dados pessoais também precisam seguir as regras de retenção. O gerente de TI monta o repositório central usando espaço já existente nos servidores. Jamal verifica depois de uma semana que os logs de todos os servidores estão chegando e encontra um servidor que não encaminhava por causa de um erro de digitação na configuração.

### Exemplo resolvido

Jamal lê vários formatos de log, extrai campos com padrões testados, encontra um erro de onze minutos no relógio de uma câmera e recomenda o armazenamento central dos logs por noventa dias.

> **Caso sintético.** Os logs são sintéticos.

### Erros e limites

Relógios não sincronizados tornam impossível ordenar os eventos de sistemas diferentes.

### Exercícios

- **EX016 — Módulo de padrões.** Qual módulo extrai os campos? *Rubrica:* 3 = re;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX017 — Erro do relógio.** Quanto o relógio do gravador de câmeras está atrasado? *Rubrica:* 3 = onze minutos;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX018 — Retenção dos logs.** Por quanto tempo os logs centrais devem ser guardados? *Rubrica:* 3 = noventa dias;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Conceitos de segurança na prática

### Objetivos de aprendizagem

Você vai (1) aplicar a confidencialidade, a integridade e a disponibilidade às tarefas diárias; (2) usar o menor privilégio e a defesa em profundidade; (3) relacionar controles a riscos.

### 7.1 Os objetivos no trabalho diário

Jamal liga os três objetivos de segurança a suas tarefas diárias. Restringir a pasta dos questionários protegeu a confidencialidade. Verificar os backups protege a integridade e a disponibilidade. Manter o sistema de reservas corrigido protege os três. A ISO/IEC 27000:2026, a visão geral da família ISO/IEC 27000, descreve a segurança da informação nesses termos. A Sra. Grant pede que ele marque cada tarefa no caderno com o objetivo a que ela serve, o que o ajuda a explicar por que a tarefa importa. Depois de um mês, ele percebe que a maioria de suas tarefas protege a disponibilidade, o que corresponde à necessidade dos centros de continuar recebendo os associados.

### 7.2 Menor privilégio

O artigo de Saltzer e Schroeder de 1975 descreve o menor privilégio: dar a cada usuário e programa apenas o acesso necessário. Jamal o aplica no Riverbend: os recepcionistas precisam de acesso às reservas, mas não às pastas financeiras; os instrutores precisam dos questionários, mas não dos dados de pagamento. Ele observa que o menor privilégio também limita o dano quando uma conta é comprometida, porque o atacante herda apenas os direitos limitados daquela conta. Ele revisa os acessos de cinco contas de amostra em relação às funções e encontra dois recepcionistas que conseguem abrir pastas financeiras. O gerente de TI remove o acesso no mesmo dia, e Jamal anota o resultado no caderno.

### 7.3 Defesa em profundidade

Nenhum controle é perfeito, por isso a segurança usa camadas. Jamal lista as camadas que protegem os caixas do Riverbend: separação da rede, software atualizado, contas restritas, criptografia do terminal de pagamento e monitoramento. Se uma falhar, as outras continuam protegendo. A Sra. Grant explica que a defesa em camadas é especialmente importante em organizações pequenas, onde qualquer controle isolado pode ser mantido por uma única pessoa ocupada. Ele desenha as camadas como anéis em volta dos caixas no caderno. A Sra. Grant pergunta qual anel falharia primeiro se o técnico de TI estivesse de férias por um mês, e ele aponta as atualizações de software, o que o leva a sugerir uma configuração de atualização automática para o fornecedor dos caixas confirmar.

### 7.4 Controles e riscos

Jamal aprende que os controles existem para reduzir riscos específicos. Antes de acrescentar um controle, ele pergunta que risco ele reduz e se esse risco importa. Ele questiona uma proposta de bloquear todos os dispositivos de armazenamento USB na recepção, ao descobrir que a equipe precisa deles para imprimir cartazes. Em vez disso, ele sugere permitir apenas dispositivos criptografados fornecidos pelo Riverbend. A Sra. Grant o elogia por adequar os controles às necessidades reais. O gerente de TI encomenda pen drives criptografados para cada balcão de recepção, e a equipe relata que a mudança não causa dificuldade. Jamal registra a decisão com o risco que ela trata e o motivo pelo qual a proposta original foi alterada.

### Exemplo resolvido

Jamal marca as tarefas por objetivo, aplica o menor privilégio às funções, lista os controles em camadas dos caixas e adapta um controle de USB às necessidades reais.

> **Caso sintético.** Os exemplos são sintéticos.

### Erros e limites

Controles que ignoram as necessidades reais do trabalho acabam contornados.

### Exercícios

- **EX019 — Norma de visão geral.** Qual norma dá a visão geral da família? *Rubrica:* 3 = ISO/IEC 27000:2026;; 2 = correto;; 1 = outra;; 0 = nenhuma.

- **EX020 — Limite do comprometimento.** Como o menor privilégio limita um comprometimento? *Rubrica:* 3 = o atacante herda direitos limitados;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX021 — Alternativa ao USB.** Que alternativa ao USB Jamal sugere? *Rubrica:* 3 = apenas dispositivos criptografados fornecidos pelo Riverbend;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Endurecimento de estações de trabalho

### Objetivos de aprendizagem

Você vai (1) definir uma linha de base para estações de trabalho; (2) verificar automaticamente as estações contra ela; (3) priorizar as correções.

### 8.1 A linha de base

Jamal e o gerente de TI combinam uma linha de base de quatro itens para as estações de trabalho do Riverbend: o firewall local ligado, a criptografia de disco ativada, o bloqueio de tela após alguns minutos e as atualizações automáticas ligadas. Cada item trata um risco claro: ataques pela rede, o furto de um notebook, telas desacompanhadas na recepção e software sem correções. A Sra. Grant aconselha começar com uma linha de base curta que possa ser verificada de forma confiável e acrescentar itens depois. Ele escreve cada item como uma verificação que um script pode executar automaticamente, com um resultado claro de aprovação ou reprovação e a configuração que ela lê.

### 8.2 O laboratório das estações

O laboratório verifica 210 estações de trabalho sintéticas. O firewall está ligado em 201, 95,7 por cento; a criptografia de disco em 164, 78,1 por cento; o bloqueio de tela em 187, 89,0 por cento; e as atualizações automáticas em 196, 93,3 por cento. Apenas 129 estações, 61,4 por cento, cumprem os quatro itens. Jamal observa que a criptografia de disco é o item mais fraco e que o número combinado mostra que quase duas em cada cinco estações falham em pelo menos uma verificação. Ele apresenta os resultados por item e combinados numa tabela curta, e o gerente de TI diz que o número combinado é bem menor do que esperava. Eles concordam que a criptografia deve ser o primeiro foco, porque tem a menor taxa de aprovação e protege contra o furto.

### Laboratório — Verificando configurações sintéticas de estações de trabalho contra uma linha de base de quatro itens

```python
"""Check synthetic workstation settings against a four-item baseline (stdlib only)."""
import random
random.seed(44)
items = ["firewall_on", "disk_encrypted", "screen_lock", "auto_updates"]
fail_p = {"firewall_on": 0.03, "disk_encrypted": 0.12, "screen_lock": 0.09, "auto_updates": 0.05}
ws = [{k: random.random() >= fail_p[k] for k in items} for _ in range(210)]
for k in items:
    ok = sum(w[k] for w in ws)
    print(f"{k}: {ok}/{len(ws)} ({ok/len(ws):.1%})")
allok = sum(all(w.values()) for w in ws)
print(f"all four: {allok}/{len(ws)} ({allok/len(ws):.1%})")
```

Execute com `python3 lab_workstations.py`. Saída verificada:

```text
firewall_on: 201/210 (95.7%)
disk_encrypted: 164/210 (78.1%)
screen_lock: 187/210 (89.0%)
auto_updates: 196/210 (93.3%)
all four: 129/210 (61.4%)
```

### 8.3 Priorização

Jamal ordena as falhas por risco. Os notebooks sem criptografia vêm primeiro, porque saem dos prédios e podem ser furtados. Os computadores da recepção sem bloqueio de tela vêm em seguida, porque os associados passam por eles o tempo todo. Os computadores de mesa em escritórios trancados sem criptografia vêm depois. Ele discute a ordem com o gerente de TI, que concorda e agenda a criptografia dos notebooks para a primeira semana. Ele cria uma lista simples de tarefas com as estações reprovadas agrupadas por centro e por prioridade, para que o técnico possa corrigir várias máquinas em cada visita em vez de viajar repetidamente entre os centros.

### 8.4 Repetição da verificação

Jamal agenda a verificação para rodar mensalmente e relatar os resultados por centro. Depois de dois meses, a parcela que cumpre os quatro itens sobe substancialmente, e as falhas restantes são em sua maioria computadores de mesa antigos com substituição prevista. Ele registra esses casos como exceções com datas de substituição. A Sra. Grant observa que as verificações repetidas transformam uma linha de base de um documento num controle que funciona. Ele acrescenta os resultados mensais a um gráfico que o gerente de TI mostra na reunião trimestral da gerência. A Sra. Grant pede que ele registre as exceções com o motivo e a data de substituição, para que a linha de base continue honesta sobre o que ainda não foi corrigido.

### Exemplo resolvido

Jamal define uma linha de base de quatro itens, descobre que 129 de 210 estações sintéticas (61,4 por cento) cumprem os quatro, prioriza a criptografia dos notebooks e agenda verificações mensais.

> **Caso sintético.** As estações de trabalho são sintéticas; as saídas vêm de lab_workstations.py.

### Erros e limites

Relatar cada item separadamente pode esconder quantas máquinas falham em pelo menos um.

### Exercícios

- **EX022 — Taxa de criptografia.** Que parcela tem criptografia de disco? *Rubrica:* 3 = 164 de 210, 78,1 por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX023 — Taxa combinada.** Quantas cumprem os quatro itens? *Rubrica:* 3 = 129, 61,4 por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX024 — Primeira prioridade.** Quais falhas vêm primeiro? *Rubrica:* 3 = notebooks sem criptografia;; 2 = correto;; 1 = outra;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Jamal Haddad, a Sra. Fiona Grant, o Northgate College of Technology, o Riverbend Leisure Trust e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Configurar, verificar e manter os controles de segurança.

**EX002.** Cerca de 350 funcionários.

**EX003.** Para que o trabalho possa ser repetido exatamente e explicado a outras pessoas.

**EX004.** Os instrutores.

**EX005.** A integridade, porque dados modificados poderiam desviar pagamentos.

**EX006.** Ela é restrita a instrutores e gerentes.

**EX007.** Porque as pessoas mudam de função.

**EX008.** Eles entram automaticamente como administrador.

**EX009.** Diminui a superfície de ataque.

**EX010.** Os dispositivos que lidam com dados de pagamento.

**EX011.** Uma interface web com senha padrão.

**EX012.** Caixas, equipe, câmeras e visitantes.

**EX013.** As contas sem login há sessenta dias.

**EX014.** Ele as pula e as relata.

**EX015.** A versão do script e o nome do arquivo de entrada.

**EX016.** O módulo re.

**EX017.** Onze minutos.

**EX018.** Noventa dias.

**EX019.** A ISO/IEC 27000:2026, a visão geral da família.

**EX020.** O atacante herda apenas os direitos limitados daquela conta.

**EX021.** Permitir apenas dispositivos criptografados fornecidos pelo Riverbend.

**EX022.** 164 de 210, 78,1 por cento.

**EX023.** 129 estações de trabalho, 61,4 por cento.

**EX024.** Os notebooks sem criptografia.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- National Institute of Standards and Technology. (2004). *Standards for security categorization of federal information and information systems* (FIPS 199). https://doi.org/10.6028/NIST.FIPS.199
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
