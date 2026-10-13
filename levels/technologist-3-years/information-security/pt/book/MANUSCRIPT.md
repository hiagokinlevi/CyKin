# Segurança da Informação: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 071, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–16 de 30 já estão escritos em português, com os exercícios EX001–EX048 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 17–30 (EX049–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) |

Capítulos 17–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-17), até a chegada dos próximos lotes.

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

<a id="ch-09"></a>

## Capítulo 9 — Gestão de correções

### Objetivos de aprendizagem

Você vai (1) executar um ciclo de correções; (2) testar as atualizações antes da implantação ampla; (3) lidar com sistemas que não podem ser corrigidos rapidamente.

### 9.1 O ciclo

Jamal aprende o ciclo de correções: saber das novas atualizações, avaliar sua importância, testá-las, implantá-las e confirmar a instalação. O gerente de TI do Riverbend recebe os avisos dos fabricantes e consulta um catálogo público de vulnerabilidades sabidamente exploradas. As atualizações para falhas exploradas ativamente têm prioridade. A Sra. Grant explica que um ciclo confiável e rotineiro protege melhor do que surtos ocasionais de esforço depois de notícias na imprensa. Ele escreve o ciclo como uma lista de verificação mensal com datas para cada etapa e o responsável, para que o gerente de TI e o técnico saibam exatamente o que fazer e quando. A lista inclui um passo para consultar toda semana o catálogo de vulnerabilidades exploradas.

### 9.2 Testes

As atualizações podem quebrar coisas. Jamal monta um grupo de teste de cinco estações de trabalho, uma de cada tipo de função, que recebe as atualizações primeiro. Depois de dois dias sem problemas, as atualizações vão para todas as estações. Quando uma atualização quebra o driver de uma impressora da recepção, o grupo de teste detecta o problema antes que ele chegue a todos os centros. Ele registra o problema e a correção no log de TI. A Sra. Grant observa que os grupos de teste devem incluir as máquinas mais incomuns, como os computadores da recepção com impressoras, porque são as mais propensas a quebrar. Jamal acrescenta mais duas máquinas ao grupo por esse motivo.

### 9.3 Servidores e nuvem

O sistema de reservas do Riverbend é hospedado na nuvem, por isso seu fornecedor cuida das correções dos servidores. Jamal consulta o contrato e descobre que o fornecedor se compromete a corrigir os problemas críticos em até catorze dias. O Riverbend continua corrigindo seu próprio servidor de arquivos e os gravadores das câmeras. As atualizações dos gravadores são raras e precisam ser baixadas manualmente, por isso ele acrescenta uma verificação trimestral ao calendário. Ele também pede ao fornecedor um resumo de seu desempenho recente nas correções, que o fornecedor envia. O resumo mostra que os problemas críticos foram corrigidos dentro do prazo acordado no último ano. Jamal arquiva o resumo com o contrato e cria um lembrete para pedi-lo anualmente.

### 9.4 Sistemas que ficam para trás

Alguns sistemas não podem ser corrigidos rapidamente. Um antigo controlador dos produtos químicos da piscina roda um software que o fornecedor não atualiza mais. Jamal recomenda isolá-lo num segmento de rede próprio, bloquear o acesso à internet e perguntar ao fornecedor sobre a substituição. A Sra. Grant observa que o isolamento reduz o risco quando a correção é impossível, mas deve ser registrado como uma exceção temporária com data de revisão. O fornecedor oferece um controlador substituto a preço reduzido, e o gerente do centro o inclui no orçamento do ano seguinte. Jamal registra a exceção com seus controles e a data de revisão no log de TI e verifica que o isolamento funciona testando a partir de um computador da equipe.

### Exemplo resolvido

Jamal segue o ciclo de correções, usa um grupo de teste de cinco máquinas que detecta um problema de impressora, confere o compromisso do fornecedor de nuvem e isola um controlador de piscina que não pode ser corrigido.

> **Caso sintético.** Os sistemas são sintéticos.

### Erros e limites

Implantar atualizações não testadas em todos os lugares ao mesmo tempo pode quebrar todos os centros.

### Exercícios

- **EX025 — Atualizações prioritárias.** Quais atualizações têm prioridade? *Rubrica:* 3 = as de falhas exploradas ativamente;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX026 — Grupo de teste.** Quantas estações de trabalho há no grupo de teste? *Rubrica:* 3 = cinco;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX027 — Controlador da piscina.** Como o controlador da piscina é protegido? *Rubrica:* 3 = segmento isolado sem internet;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Varredura de vulnerabilidades

### Objetivos de aprendizagem

Você vai (1) executar varreduras de vulnerabilidades autorizadas; (2) interpretar os resultados das varreduras; (3) verificar as correções.

### 10.1 Varredura autorizada

Os varredores de vulnerabilidades verificam os sistemas em busca de fraquezas conhecidas. Jamal aprende que a varredura precisa ser autorizada por escrito, agendada para evitar os horários de movimento e limitada aos sistemas combinados. O gerente de TI do Riverbend aprova uma varredura mensal da sede e de um centro, fora do horário de funcionamento. A Sra. Grant lembra aos estudantes que fazer varredura no sistema de outra pessoa sem permissão é ilegal em muitos países. Jamal guarda uma cópia da aprovação assinada com os resultados da varredura. Ele executa a primeira varredura com o gerente de TI acompanhando, para que qualquer efeito inesperado nos sistemas do centro possa ser tratado imediatamente.

### 10.2 Leitura dos resultados

A varredura produz uma longa lista de achados com classificações de severidade. Jamal aprende que os varredores produzem falsos positivos, relatando uma fraqueza que não está presente, e que as classificações de severidade não levam em conta o contexto local. Um achado classificado como alto numa impressora interna pode importar menos do que um achado médio num sistema exposto à internet. Ele ordena os achados por severidade e exposição e verifica manualmente os primeiros itens. Ele confirma dois falsos positivos conferindo diretamente as versões do software e os registra para que possam ser ignorados nas varreduras futuras.

### 10.3 Correção

Jamal trabalha com o gerente de TI para corrigir os principais achados: uma ferramenta de acesso remoto desatualizada no servidor de arquivos, uma configuração de criptografia fraca num site interno e o firmware antigo do gravador de câmeras. Cada correção é registrada com a data e o responsável. Ele aprende que registros claros ajudam quando auditores ou seguradoras perguntam se as fraquezas conhecidas foram tratadas. O gerente de TI atualiza a ferramenta de acesso remoto e aplica a nova configuração de criptografia, enquanto Jamal baixa e instala o firmware do gravador de câmeras durante um período com o centro fechado. Cada mudança é testada antes que o centro reabra.

### 10.4 Verificação

Depois de corrigir, Jamal executa de novo a varredura nos sistemas afetados para confirmar que os achados sumiram. Um permanece, porque a ferramenta de acesso remoto tinha duas instalações. Ele remove a segunda e repete a varredura com sucesso. A Sra. Grant observa que a verificação é essencial, porque presumir que uma correção funcionou sem conferir é uma fonte comum de fraquezas que persistem. Jamal acrescenta um passo de nova varredura à lista de verificação mensal, para que toda correção seja confirmada antes de o achado ser encerrado. Ele também registra a segunda instalação no caderno como lição: os inventários de software instalado devem ser conferidos antes de presumir que uma única correção está completa.

### Exemplo resolvido

Jamal executa varreduras mensais autorizadas, ordena os achados por severidade e exposição, corrige três achados principais e verifica com uma nova varredura, detectando uma segunda instalação.

> **Caso sintético.** As varreduras são sintéticas.

### Erros e limites

Presumir que uma correção funcionou sem uma nova varredura deixa as fraquezas no lugar.

### Exercícios

- **EX028 — Aprovação da varredura.** Quem aprova a varredura? *Rubrica:* 3 = o gerente de TI, por escrito;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX029 — Falso positivo.** O que é um falso positivo? *Rubrica:* 3 = uma fraqueza relatada que não está presente;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX030 — Achado remanescente.** Por que um achado permaneceu depois da correção? *Rubrica:* 3 = uma segunda instalação da ferramenta;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Administração de contas

### Objetivos de aprendizagem

Você vai (1) conduzir os processos de admissão, mudança de função e desligamento; (2) lidar com contas compartilhadas e contas de serviço; (3) revisar as contas regularmente.

### 11.1 Admissões

No segundo ano, Jamal ajuda o gerente de TI do Riverbend na administração de contas. Salva-vidas e professores de natação temporários são admitidos em grande número antes do verão. Cada um precisa de uma conta para o sistema de reservas e para a escala da equipe, mas de nada mais. Jamal cria um modelo para cada função, para que as novas contas recebam exatamente o acesso certo. A Sra. Grant explica que os modelos evitam o erro comum de copiar a conta de um colega existente, que carrega direitos extras de que a pessoa nova não precisa. Os modelos também tornam a configuração mais rápida nos períodos de movimento.

### 11.2 Mudanças de função e desligamentos

Quando os funcionários mudam de função, os acessos antigos devem ser removidos. Jamal encontra uma ex-recepcionista, agora instrutora, que ainda tem acesso de recepção às telas de pagamento dos associados. Quando os funcionários saem, as contas devem ser desativadas no último dia. O Riverbend depende de os gerentes dos centros mandarem e-mail à TI, o que muitas vezes acontece com atraso. Jamal propõe um relatório semanal do sistema de folha de pagamento listando os desligamentos, que a TI confere com as contas ativas. O gerente de TI concorda em testá-lo por um período e registrar quantas remoções atrasadas ele encontra.

### 11.3 Contas compartilhadas e de serviço

As contas compartilhadas tornam impossível saber quem fez o quê. A recepção de cada centro usa um único login compartilhado. Jamal propõe logins individuais com uma entrada rápida por crachá, para que as ações sejam rastreáveis sem atrasar a recepção. As contas de serviço, usadas por software e não por pessoas, precisam de responsáveis nomeados e de senhas fortes guardadas com segurança. Ele lista as contas de serviço do Riverbend e encontra uma usada por uma antiga ferramenta de backup que não roda mais. Ele a desativa depois de confirmar com o gerente de TI. A entrada por crachá é testada primeiro num centro.

### 11.4 Revisões

Jamal conduz uma revisão trimestral de contas: comparar as contas ativas com a lista de funcionários, conferir o acesso de cada conta com o modelo da função e listar as contas sem uso há sessenta dias. Sua primeira revisão encontra vários temporários do verão passado ainda ativos e duas contas com acesso financeiro sem explicação. Todos os problemas são corrigidos em uma semana. A Sra. Grant observa que as revisões regulares pegam o que os processos deixam passar e que a segunda revisão costuma ser muito mais limpa, o que é em si uma evidência de melhoria. Ele registra os achados e as correções de cada revisão.

### Exemplo resolvido

Jamal cria modelos por função para os temporários admitidos, encontra uma pessoa que mudou de função com acesso antigo, propõe um relatório de desligamentos da folha de pagamento, substitui os logins compartilhados da recepção e conduz uma revisão trimestral.

> **Caso sintético.** As contas são sintéticas.

### Erros e limites

Copiar a conta de um colega para criar uma nova espalha acessos desnecessários.

### Exercícios

- **EX031 — Acesso dos temporários.** De que acesso os temporários precisam? *Rubrica:* 3 = apenas o sistema de reservas e a escala;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX032 — Relatório de desligamentos.** Que fonte lista os desligamentos semanalmente? *Rubrica:* 3 = o sistema de folha de pagamento;; 2 = correto;; 1 = outra;; 0 = nenhuma.

- **EX033 — Conta de serviço antiga.** Qual conta de serviço é desativada? *Rubrica:* 3 = uma usada por uma antiga ferramenta de backup;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Autenticação multifator

### Objetivos de aprendizagem

Você vai (1) escolher segundos fatores para usuários diferentes; (2) implantar a autenticação multifator em etapas; (3) apoiar os usuários e lidar com dispositivos perdidos.

### 12.1 Escolha dos fatores

Jamal compara os segundos fatores para o Riverbend. Os códigos gerados por aplicativo servem para a equipe de escritório com smartphones. As chaves físicas servem para os dois funcionários de TI, cujas contas são as mais poderosas e as mais visadas. Os códigos por mensagem de texto são mais fracos, mas podem servir para os funcionários eventuais que não querem aplicativos nos celulares pessoais. A Sra. Grant explica que a escolha equilibra proteção, custo e praticidade e que os métodos resistentes a phishing, como as chaves físicas, dão a proteção mais forte contra páginas de login falsas. Ele resume as opções numa tabela com o custo, a força e a facilidade de uso para cada grupo.

### 12.2 Implantação em etapas

Jamal planeja a implantação em etapas: primeiro a equipe de TI, depois os gerentes, depois a equipe de escritório e, por fim, todos os demais funcionários. Cada etapa tem uma data, um guia e uma sessão de apoio. Ele começa pelo sistema de e-mail, porque contas de e-mail comprometidas são usadas com frequência para enviar faturas fraudulentas. O gerente de TI aprova o plano. Jamal aprende que as etapas permitem à equipe corrigir problemas com um grupo pequeno antes que eles afetem todos. Ele escreve uma mensagem curta para cada etapa explicando por que a mudança importa, e o gerente de TI a envia duas semanas antes do início da etapa.

### 12.3 Apoio aos usuários

Alguns funcionários têm dificuldade com a configuração. Jamal escreve um guia de uma página com capturas de tela e faz sessões de atendimento livre em cada centro. Ele descobre que celulares mais antigos não conseguem instalar o aplicativo autenticador, por isso oferece códigos por mensagem de texto como alternativa para esses funcionários. Os pedidos de apoio atingem o pico na primeira semana e depois caem. A Sra. Grant observa que um bom apoio reduz a resistência e impede que os funcionários procurem formas de contornar o novo controle. Ele registra cada pedido de apoio com a causa, e a mais comum, o relógio do celular configurado errado, é acrescentada ao guia.

### 12.4 Dispositivos perdidos

Celulares se perdem. Jamal escreve um procedimento: o funcionário comunica a perda à TI, a TI remove o dispositivo perdido da conta depois de confirmar a identidade por um número de telefone conhecido ou pessoalmente, e o funcionário registra um novo dispositivo. Ele configura códigos de reserva para a equipe de TI, guardados com segurança. Ele aprende que os procedimentos de recuperação precisam ser tão seguros quanto o próprio login, porque os atacantes muitas vezes miram a recuperação em vez do login principal. Ele testa o procedimento com um colega que finge ter perdido o celular.

### Exemplo resolvido

Jamal escolhe os fatores por grupo de usuários, implanta em etapas começando pelo e-mail, apoia a equipe com guias e alternativas e escreve um procedimento seguro para dispositivos perdidos.

> **Caso sintético.** A implantação é sintética.

### Erros e limites

Um procedimento de recuperação fraco permite que os atacantes contornem a autenticação multifator.

### Exercícios

- **EX034 — Fator da TI.** Qual fator serve para a equipe de TI? *Rubrica:* 3 = chaves físicas;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX035 — Primeiro sistema.** Qual sistema recebe primeiro a autenticação multifator? *Rubrica:* 3 = o e-mail;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX036 — Celulares antigos.** Que alternativa serve para quem tem celulares antigos? *Rubrica:* 3 = códigos por mensagem de texto;; 2 = correto;; 1 = outra;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Senhas e segredos

### Objetivos de aprendizagem

Você vai (1) definir regras práticas de senha; (2) gerenciar segredos compartilhados com um gerenciador de senhas; (3) remover segredos de scripts e documentos.

### 13.1 Regras de senha

As regras antigas do Riverbend obrigavam a trocar a senha todo mês, o que levava os funcionários a acrescentar um número à mesma palavra a cada vez. Jamal recomenda frases-senha mais longas, a verificação contra listas de senhas vazadas, a autenticação multifator e trocas apenas quando houver suspeita de comprometimento. A Sra. Grant explica que as regras que ignoram o comportamento humano produzem senhas previsíveis. O gerente de TI adota as novas regras depois que Jamal mostra exemplos dos padrões previsíveis que os funcionários vinham usando. Ele também sugere que o sistema de reservas dos associados adote a mesma verificação de senhas vazadas, e o fornecedor concorda em ativá-la.

### 13.2 Gerenciadores de senhas

A equipe de TI administra muitas senhas de roteadores, gravadores de câmeras, portais de fornecedores e contas de serviço. Elas ficavam numa planilha no servidor de arquivos. Jamal recomenda um gerenciador de senhas com contas individuais para cada membro da equipe de TI, compartilhando apenas as entradas de que cada um precisa, e um log de acesso. Ele transfere as entradas e apaga a planilha. Ele aprende que os gerenciadores de senhas tornam práticas as senhas fortes e únicas, porque ninguém precisa memorizá-las. Cada membro da equipe de TI vê apenas as entradas necessárias para seu trabalho, e o log mostra quem abriu cada entrada.

### 13.3 Segredos em scripts

Jamal encontra um script de backup com a senha de uma conta de serviço escrita dentro dele. Qualquer pessoa que consiga ler o script pode usar a senha. Ele reescreve o script para ler a senha de um arquivo de configuração protegido, legível apenas pela conta de serviço, e pede ao gerente de TI que troque a senha exposta. A Sra. Grant observa que os segredos em scripts muitas vezes se espalham por cópias, backups e pastas compartilhadas. Ele procura senhas semelhantes nos outros scripts do servidor e encontra mais duas, que corrige da mesma forma.

### 13.4 Segredos em documentos

Jamal procura na unidade compartilhada do Riverbend, com permissão, documentos que contenham a palavra senha. Ele encontra um guia de configuração dos gravadores de câmeras que lista as senhas atuais e uma antiga nota de passagem de serviço com as credenciais dos roteadores. Ele remove as senhas dos dois documentos, substituindo-as por uma referência ao gerenciador de senhas, e manda trocar as senhas afetadas. Ele aprende que procurar periodicamente segredos expostos é uma verificação simples e valiosa. Ele acrescenta a busca à lista de verificação mensal, para que novas exposições sejam encontradas depressa em vez de ficarem anos esquecidas em pastas compartilhadas.

### Exemplo resolvido

Jamal substitui as trocas mensais obrigatórias por frases-senha e verificação de vazamentos, transfere as senhas da TI para um gerenciador de senhas e remove segredos de um script e de documentos.

> **Caso sintético.** Os segredos são sintéticos.

### Erros e limites

Uma senha escrita num script fica exposta a qualquer pessoa que consiga lê-lo.

### Exercícios

- **EX037 — Efeito da regra antiga.** O que as trocas mensais obrigatórias provocaram? *Rubrica:* 3 = acrescentar um número à mesma palavra;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX038 — Substituto da planilha.** O que substitui a planilha de senhas? *Rubrica:* 3 = um gerenciador de senhas;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX039 — Achados nos documentos.** O que a busca nos documentos encontrou? *Rubrica:* 3 = senhas das câmeras e credenciais dos roteadores;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Firewalls e segmentação

### Objetivos de aprendizagem

Você vai (1) revisar as regras de firewall de forma sistemática; (2) encontrar regras amplas demais, sombreadas e sem uso; (3) limpar as regras com segurança.

### 14.1 Por que revisar as regras

As regras de firewall se acumulam ao longo dos anos à medida que fornecedores e funcionários pedem acesso. As regras antigas raramente são removidas, porque ninguém se lembra por que existem e todos têm medo de quebrar alguma coisa. Pedem a Jamal que revise a lista de regras do firewall da sede do Riverbend. A Sra. Grant explica três problemas comuns: regras que permitem demais, regras que nunca podem ter efeito porque uma regra anterior já corresponde ao mesmo tráfego e regras que não são usadas há muito tempo. Ele exporta a lista de regras com noventa dias de contagens de acertos.

### 14.2 O laboratório do firewall

O laboratório revisa uma lista sintética de doze regras com as contagens de acertos de noventa dias. A regra 11 permite qualquer tráfego de qualquer origem para qualquer destino. Como o firewall aplica a primeira regra correspondente, a regra 11 torna inalcançável a regra final de bloqueio, a regra 12, que tem zero acertos. A regra 9 duplica a regra 1 e é sombreada por ela. As regras 6, 9, 10 e 12 têm zero acertos, incluindo a regra 6, que permite a um fornecedor acesso por área de trabalho remota aos caixas. Ele apresenta os achados ao gerente de TI numa tabela curta que lista cada regra, seus acertos e o problema encontrado, se houver, com uma ação proposta para cada uma.

### Laboratório — Revisando uma lista sintética de regras de firewall em busca de regras amplas, sombreadas e sem uso

```python
"""Review a synthetic firewall rule list for any-any rules, shadowed rules and unused rules (stdlib only)."""
rules = [
 (1, "allow", "staff", "internet", "443", 51234), (2, "allow", "staff", "internet", "80", 20877),
 (3, "allow", "staff", "booking", "443", 9411), (4, "allow", "guest", "internet", "443", 40210),
 (5, "deny", "guest", "staff", "any", 1876), (6, "allow", "supplier", "tills", "3389", 0),
 (7, "allow", "staff", "tills", "443", 2210), (8, "allow", "cctv", "internet", "any", 1530),
 (9, "allow", "staff", "internet", "443", 0), (10, "allow", "mgmt", "switches", "22", 0),
 (11, "allow", "any", "any", "any", 312), (12, "deny", "any", "any", "any", 0),
]
anyany = [r[0] for r in rules if r[2] == "any" and r[3] == "any" and r[4] == "any" and r[1] == "allow"]
def shadowed(rs):
    out = []
    for i, r in enumerate(rs):
        for p in rs[:i]:
            if p[2] in ("any", r[2]) and p[3] in ("any", r[3]) and p[4] in ("any", r[4]):
                out.append((r[0], p[0])); break
    return out
unused = [r[0] for r in rules if r[5] == 0]
print(f"rules {len(rules)}; allow any-any: {anyany}")
print(f"shadowed (rule, by): {shadowed(rules)}")
print(f"zero hits in 90 days: {unused}")
print(f"after removing rule 11, shadowed: {shadowed([r for r in rules if r[0] != 11])}")
```

Execute com `python3 lab_firewall.py`. Saída verificada:

```text
rules 12; allow any-any: [11]
shadowed (rule, by): [(9, 1), (12, 11)]
zero hits in 90 days: [6, 9, 10, 12]
after removing rule 11, shadowed: [(9, 1)]
```

### 14.3 Interpretação

A regra que permite tudo para tudo é o achado mais grave, porque significa que o firewall na prática permite qualquer coisa que não tenha correspondido antes, e a regra de bloqueio destinada a barrar todo o resto nunca se aplica. Jamal pergunta sobre ela ao gerente de TI; ela foi acrescentada durante um problema de rede há dois anos como solução temporária. A regra sem uso de área de trabalho remota do fornecedor também é preocupante, porque a área de trabalho remota para os caixas é uma via comum de entrada de ransomware. A regra 10, para administrar os switches, está sem uso, mas é legítima. Ele registra o histórico de cada achado.

### 14.4 Limpeza segura

Jamal propõe mudanças: remover a regra 11, para que o bloqueio final tenha efeito; remover a regra duplicada 9; remover a regra 6 do fornecedor depois de confirmar com ele; e manter a regra 10 com uma nota explicando sua finalidade. O laboratório mostra que, depois de remover a regra 11, apenas a regra 9 continua sombreada. O gerente de TI faz as mudanças num período tranquilo, com um plano de reversão, monitora problemas por uma semana e registra cada mudança. O fornecedor confirma que não precisa mais da regra 6. Depois de uma semana sem problemas, Jamal agenda uma revisão da lista de regras a cada seis meses.

### Exemplo resolvido

Jamal revisa doze regras sintéticas, encontra uma regra que permite tudo para tudo e torna inalcançável o bloqueio final, uma duplicata e uma regra sem uso de área de trabalho remota do fornecedor, e faz a limpeza com segurança.

> **Caso sintético.** As regras são sintéticas; as saídas vêm de lab_firewall.py.

### Erros e limites

Uma regra que permite tudo acima do bloqueio final torna o bloqueio inútil.

### Exercícios

- **EX040 — Regra ampla.** Qual regra permite qualquer tráfego? *Rubrica:* 3 = a regra 11;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX041 — Bloqueio inalcançável.** Por que a regra 12 tem zero acertos? *Rubrica:* 3 = a regra 11 corresponde antes;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX042 — Regra do fornecedor.** O que a regra 6, sem uso, permite? *Rubrica:* 3 = área de trabalho remota do fornecedor para os caixas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Segurança sem fio

### Objetivos de aprendizagem

Você vai (1) configurar redes sem fio seguras; (2) separar as redes sem fio de visitantes e da equipe; (3) encontrar pontos de acesso não autorizados.

### 15.1 A rede sem fio da equipe

A rede sem fio da equipe do Riverbend usa uma única senha compartilhada por todos e inalterada há anos, conhecida por muitos ex-funcionários. Jamal recomenda a entrada individual na rede sem fio da equipe com as contas normais de cada um, para que quem sai perca o acesso sem fio quando a conta for desativada. Onde os dispositivos não suportam isso, como alguns tablets usados para as listas de presença das aulas, ele recomenda uma rede separada com uma senha forte trocada a cada período. O gerente de TI configura a entrada individual num centro como teste e a estende a todos os centros depois de um mês. Os tablets das listas passam para uma rede própria com uma senha nova.

### 15.2 A rede sem fio de visitantes

Os associados usam a rede sem fio de visitantes nos cafés e nas salas de convivência. Jamal verifica que a rede de visitantes está separada das redes da equipe e dos caixas e que os visitantes não veem os dispositivos uns dos outros. Ele também confere a página de boas-vindas da rede de visitantes, que pede um endereço de e-mail. Ele sugere explicar como o endereço é usado e oferecer acesso sem ele. A Sra. Grant observa que as redes de visitantes precisam ser isoladas, porque o Riverbend não tem como controlar os dispositivos que os visitantes trazem. A gerente de marketing concorda em atualizar o texto da página de boas-vindas em até um mês.

### 15.3 Pontos de acesso não autorizados

Jamal percorre dois centros com um notebook que lista as redes sem fio próximas. Ele encontra um ponto de acesso com nome parecido com o de uma rede da equipe, mas que não foi instalado pela TI. Descobre-se que o fornecedor do café o instalou para seu terminal de cartão. Ele se conecta diretamente à rede da equipe. Jamal relata o achado, e o gerente de TI providencia que o terminal do fornecedor use uma conexão separada adequada. Jamal aprende que os pontos de acesso não autorizados muitas vezes vêm de fornecedores resolvendo os próprios problemas. Ele acrescenta uma verificação da rede sem fio a suas visitas.

### 15.4 Configurações

Jamal confere as configurações da rede sem fio: criptografia moderna ativada, versões antigas do protocolo desativadas, interfaces de administração inalcançáveis a partir das redes de visitantes e firmware atualizado. O ponto de acesso de um centro ainda permite um modo de criptografia antigo e fraco, por compatibilidade com uma impressora velha. Ele passa a impressora para uma conexão cabeada e desativa o modo fraco. A Sra. Grant observa que as configurações de compatibilidade muitas vezes mantêm fraquezas vivas muito depois de deixarem de ser necessárias. Ele registra as configurações de cada ponto de acesso na documentação de rede, para que o gerente de TI possa conferi-las depois de qualquer mudança ou atualização de firmware.

### Exemplo resolvido

Jamal substitui uma senha compartilhada da rede sem fio da equipe por entrada individual, confere o isolamento dos visitantes, encontra um ponto de acesso de fornecedor ligado à rede da equipe e remove um modo de criptografia fraco.

> **Caso sintético.** As redes são sintéticas.

### Erros e limites

As senhas compartilhadas de rede sem fio continuam conhecidas por ex-funcionários.

### Exercícios

- **EX043 — Problema da senha compartilhada.** Por que a senha compartilhada da rede sem fio da equipe é um problema? *Rubrica:* 3 = é conhecida por ex-funcionários;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX044 — Ponto de acesso clandestino.** Quem instalou o ponto de acesso não autorizado? *Rubrica:* 3 = o fornecedor do café;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX045 — Modo fraco.** Por que um modo de criptografia fraco estava ativado? *Rubrica:* 3 = por causa de uma impressora velha;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Proteção de endpoints

### Objetivos de aprendizagem

Você vai (1) implantar ferramentas de proteção de endpoints; (2) responder a alertas dos endpoints; (3) controlar a instalação de software.

### 16.1 Ferramentas de endpoint

O software de proteção de endpoints detecta e bloqueia malware e comportamentos suspeitos nos computadores. O Riverbend usa um produto, mas Jamal descobre que ele está instalado apenas na maioria das estações de trabalho, e vários computadores da recepção ficaram sem ele depois de uma reinstalação. Ele compara a lista do console do produto com o inventário e o instala nas máquinas que faltavam. A Sra. Grant observa que lacunas de cobertura são comuns e que conferir a cobertura com o inventário deveria ser uma tarefa mensal de rotina. Ele acrescenta à lista de verificação uma comparação mensal da cobertura e envia ao gerente de TI a lista das máquinas que estiverem faltando.

### 16.2 Alertas

Jamal aprende a revisar os alertas dos endpoints. A maioria é de baixo risco: software de publicidade bloqueado ou downloads suspeitos interrompidos automaticamente. Um alerta mostra um script tentando rodar a partir de um anexo de fatura baixado num computador do financeiro. A ferramenta o bloqueou. Jamal verifica se aconteceu mais alguma coisa, não encontra nada e relata a tentativa para que o gerente de TI possa alertar a equipe. Ele aprende a tratar ataques bloqueados como sinais de que alguém está mirando a organização. O gerente de TI envia um breve alerta à equipe do financeiro descrevendo o e-mail da fatura.

### 16.3 Controle de software

Os funcionários às vezes instalam ferramentas gratuitas, algumas das quais trazem software indesejado. Jamal recomenda que só a TI possa instalar software, com um formulário simples de pedido e uma lista de aplicativos aprovados. Ele também recomenda permitir que apenas aplicativos aprovados rodem nos computadores dos caixas, que fazem um único trabalho. A Sra. Grant explica que a lista de permissão é muito eficaz em máquinas de finalidade única, embora seja mais difícil em computadores gerais de escritório. O gerente de TI aprova o formulário de pedido e a lista aprovada. Nos caixas, a lista de permissão é testada num centro e depois implantada nos nove, sem problemas relatados pela equipe.

### 16.4 Mídias removíveis

O malware pode se espalhar por pen drives. Jamal configura a proteção de endpoints para examinar automaticamente as mídias removíveis e bloqueia a execução automática de programas a partir delas. Junto com a decisão anterior de fornecer pen drives criptografados do Riverbend, isso reduz o risco e mantém o trabalho possível. Ele documenta as configurações para que sejam aplicadas aos novos computadores. Ele testa as configurações com um arquivo de teste inofensivo num pen drive no laboratório e confirma que a execução automática é bloqueada e que o exame roda. O gerente de TI aprova a aplicação das configurações a todos os computadores do Riverbend pelo sistema de gestão de dispositivos, e Jamal confere uma amostra de computadores uma semana depois para confirmar que as configurações chegaram.

### Exemplo resolvido

Jamal corrige lacunas de cobertura dos endpoints, investiga um script de fatura bloqueado, restringe a instalação de software, aplica lista de permissão aos aplicativos dos caixas e examina as mídias removíveis.

> **Caso sintético.** Os alertas são sintéticos.

### Erros e limites

A proteção de endpoints protege apenas as máquinas em que está instalada.

### Exercícios

- **EX046 — Lacuna de cobertura.** Onde faltava a proteção de endpoints? *Rubrica:* 3 = computadores da recepção após a reinstalação;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX047 — Alerta do financeiro.** O que o alerta do financeiro mostrou? *Rubrica:* 3 = um script vindo de um anexo de fatura;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX048 — Lista de permissão.** Onde a lista de permissão é mais eficaz? *Rubrica:* 3 = máquinas de finalidade única, como os caixas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX048 (as de EX049–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Jamal Haddad, a Sra. Fiona Grant, o Northgate College of Technology, o Riverbend Leisure Trust e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX025.** As atualizações para falhas exploradas ativamente.

**EX026.** Cinco estações de trabalho.

**EX027.** Isolando-o num segmento próprio sem acesso à internet.

**EX028.** O gerente de TI do Riverbend, por escrito.

**EX029.** Uma fraqueza relatada que na verdade não está presente.

**EX030.** A ferramenta de acesso remoto tinha uma segunda instalação.

**EX031.** Apenas o sistema de reservas e a escala da equipe.

**EX032.** Um relatório semanal do sistema de folha de pagamento.

**EX033.** A conta usada por uma antiga ferramenta de backup.

**EX034.** Chaves físicas.

**EX035.** O sistema de e-mail.

**EX036.** Códigos por mensagem de texto.

**EX037.** Os funcionários acrescentavam um número à mesma palavra a cada vez.

**EX038.** Um gerenciador de senhas com contas individuais.

**EX039.** Senhas dos gravadores de câmeras e credenciais dos roteadores.

**EX040.** A regra 11.

**EX041.** A regra 11 corresponde antes a todo o tráfego.

**EX042.** Acesso do fornecedor por área de trabalho remota aos caixas.

**EX043.** Ela é conhecida por muitos ex-funcionários.

**EX044.** O fornecedor do café.

**EX045.** Por compatibilidade com uma impressora velha.

**EX046.** Em vários computadores da recepção depois de uma reinstalação.

**EX047.** Um script tentando rodar a partir de um anexo de fatura baixado.

**EX048.** Em máquinas de finalidade única, como os caixas.

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
