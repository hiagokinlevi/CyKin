# Governança, Riscos e Compliance de Segurança: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 074, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–12 de 30 já estão escritos em português, com os exercícios EX001–EX036 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 13–30 (EX037–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de tecnólogo que constroem, operam e avaliam os processos práticos de GRC de uma organização com várias unidades.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios verificam a atualidade das evidências, calculam a perda esperada, resumem CSVs de testes de controles, acompanham um indicador contra um limiar e conciliam uma lista de funcionários com as contas, sempre sobre dados sintéticos. Os números de risco são ilustrações, as normas são citadas pela edição e parafraseadas, e nada aqui é auditoria, atestação ou aconselhamento jurídico reais. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de tecnólogo ao longo de três anos, em torno do programa de GRC de um grupo odontológico: fundamentos de sistemas, redes, dados e identidade, evidências, contexto e fluxos de dados, cenários e perda esperada, tratamentos, ferramentas, controles, monitoramento, solução de problemas, automação, avaliação, trabalho em equipe, passagem operacional, validação, prática e o projeto final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Priya Natarajan** | Estudante de tecnólogo | Inventada |
| **Sr. Oskar Lind** | Tutor | Inventado |
| **Halden Institute of Technology** | Instituto fictício | Inventado |
| **Riverton Dental Group** | Grupo fictício de 14 clínicas, 250 funcionários | Inventado |

### Fontes principais

ISO 31000:2018 (no Brasil, ABNT NBR ISO 31000:2018); ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) e 27002:2022; NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); PCI DSS v4.0; trust services criteria da AICPA. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

Capítulos 13–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-13), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever os sistemas de que depende uma empresa com várias unidades; (2) listar os ativos que a governança precisa cobrir; (3) ligar os sistemas aos serviços que eles sustentam.

### 1.1 Os sistemas da Riverton

Priya Natarajan é estudante de tecnólogo no fictício Halden Institute of Technology. Seu tutor, o Sr. Oskar Lind, usa um único caso ao longo do curso: o fictício Riverton Dental Group, com catorze clínicas e duzentos e cinquenta funcionários. Cada clínica tem computadores na recepção, aparelhos de imagem odontológica e uma maquininha de cartão. Um sistema de gestão do consultório em nuvem guarda os prontuários e as consultas dos pacientes. Um site de agendamento permite que os pacientes marquem as visitas. Priya aprende que a governança começa por saber quais sistemas existem e o que cada um faz. Com catorze clínicas, um único tipo de aparelho fora da lista, repetido em cada clínica, deixaria catorze lacunas de uma só vez.

### 1.2 Ativos a cobrir

Priya lista os ativos por tipo: hardware, como os computadores da recepção e os aparelhos de imagem; software, como o sistema de gestão do consultório; dados, como os prontuários e as radiografias; e serviços, como o e-mail e o site de agendamento. Para cada um, anota um dono e as clínicas que o usam. Ela descobre que os aparelhos de imagem não constam da lista da TI porque os dentistas os compraram diretamente dos fornecedores. Aprende que as compras feitas por fora da TI criam pontos cegos na governança. O Sr. Lind pergunta quem aplica os patches nos aparelhos de imagem, e ninguém na Riverton sabe responder, o que mostra por que o dono deve ser registrado na compra.

### 1.3 Sistemas e serviços

Priya liga cada sistema aos serviços ao paciente que ele sustenta. O agendamento depende do site e do sistema do consultório. O tratamento depende das imagens e dos prontuários. O faturamento depende das maquininhas de cartão e do sistema do consultório. Esse mapa mostra quais falhas impediriam as clínicas de atender os pacientes, o que mais importa para a Riverton. Ela aprende que as prioridades de governança devem seguir os serviços que importam para os clientes e para o negócio, e não simplesmente os sistemas mais caros ou tecnicamente mais complexos. O sistema do consultório, por exemplo, aparece no agendamento, no tratamento e no faturamento, então sua falha pararia os três serviços.

### Exemplo resolvido

Priya lista os sistemas e os ativos da Riverton, descobre que os aparelhos de imagem faltam nos registros da TI e mapeia os sistemas para os serviços ao paciente.

> **Caso sintético.** O Halden, a Riverton e todos os detalhes são sintéticos.

### Erros e limites

As listas de ativos deixam escapar aparelhos comprados localmente. Os mapas de serviços simplificam as dependências.

### Exercícios

- **EX001 — Ponto cego.** Por que os aparelhos de imagem faltavam na lista da TI? *Rubrica:* 3 = os dentistas os compraram diretamente dos fornecedores;; 2 = compra local;; 1 = nada;; 0 = nenhuma.
- **EX002 — Tipos de ativo.** Cite os quatro tipos de ativo que Priya usou. *Rubrica:* 3 = hardware, software, dados e serviços;; 2 = quatro;; 1 = nada;; 0 = nenhuma.
- **EX003 — Dependência do tratamento.** De que sistemas depende o tratamento? *Rubrica:* 3 = das imagens e dos prontuários;; 2 = imagens;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem

Você vai (1) descrever as redes das clínicas e as conexões com a nuvem; (2) identificar por onde trafegam os dados sensíveis; (3) anotar os riscos de rede para a governança.

### 2.1 As redes das clínicas

Cada clínica da Riverton tem uma rede pequena: computadores da recepção, aparelhos de imagem, uma maquininha de cartão e Wi-Fi de visitantes para os pacientes. Tudo se conecta por um roteador à internet e aos serviços em nuvem. Priya aprende que as maquininhas de cartão devem ficar num segmento de rede separado dos demais aparelhos, já que o PCI DSS v4.0 incentiva a segmentação para limitar o escopo dos ambientes de dados de cartão. Em três clínicas, o Wi-Fi de visitantes compartilha a mesma rede dos computadores da recepção, o que cria um risco desnecessário. Nessas três clínicas, pacientes no Wi-Fi de visitantes alcançam a mesma rede dos computadores que abrem os prontuários.

### 2.2 Dados em trânsito

Os dados dos pacientes trafegam das clínicas para o sistema do consultório em nuvem, dos aparelhos de imagem para o arquivo de imagens e da recepção para os laboratórios por e-mail. Priya verifica se cada caminho é criptografado. O sistema do consultório e o arquivo de imagens usam conexões criptografadas. Os pedidos aos laboratórios às vezes vão por e-mail comum, com nomes de pacientes e detalhes do tratamento. Ela registra isso como risco e sugere a função de mensagens seguras que o sistema do consultório já inclui, mas que poucos funcionários usam. Como essa função já está licenciada, a correção custa tempo de treinamento, e não dinheiro.

### 2.3 Riscos de rede

Priya lista os riscos de rede para a governança: Wi-Fi de visitantes misturado aos aparelhos da clínica, maquininhas não separadas, roteadores com senha padrão em duas clínicas e nenhuma visão central de quais redes das clínicas seguem o desenho padrão. Ela os ordena por impacto e facilidade de correção. Separar o Wi-Fi de visitantes fica em primeiro lugar, porque é simples e reduz a exposição dos aparelhos clínicos. As senhas padrão dos roteadores em duas clínicas vêm logo atrás, pois são igualmente rápidas de trocar. Ela aprende que padrões de rede claros ajudam as organizações com várias unidades a manter as clínicas consistentes.

### Exemplo resolvido

Priya mapeia as redes das clínicas, encontra Wi-Fi de visitantes misturado e e-mails a laboratórios sem criptografia e ordena os riscos de rede.

> **Caso sintético.** As redes das clínicas são sintéticas; o PCI DSS v4.0 é real.

### Erros e limites

Os levantamentos em campo podem deixar escapar mudanças. As verificações de criptografia precisam de confirmação técnica.

### Exercícios

- **EX004 — Lugar da maquininha.** Onde as maquininhas de cartão devem ficar? *Rubrica:* 3 = num segmento de rede separado;; 2 = segmento;; 1 = Wi-Fi de visitantes;; 0 = nenhuma.
- **EX005 — Caminho sem criptografia.** Que caminho de dados nem sempre era criptografado? *Rubrica:* 3 = pedidos aos laboratórios por e-mail comum;; 2 = e-mail ao laboratório;; 1 = nada;; 0 = nenhuma.
- **EX006 — Primeira correção de rede.** Que correção ficou em primeiro lugar? *Rubrica:* 3 = separar o Wi-Fi de visitantes dos aparelhos da clínica;; 2 = Wi-Fi de visitantes;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem

Você vai (1) escrever scripts pequenos que leem listas de governança; (2) contar e filtrar registros; (3) imprimir resultados claros para os gestores.

### 3.1 Ler listas

Priya escreve seu primeiro script em Python para ler a lista de ativos da Riverton a partir de um arquivo CSV. Ele conta os ativos por clínica e lista os que não têm dono. Ela aprende a usar listas, laços e condições, e a tratar um valor ausente sem o programa quebrar. O Sr. Lind explica que os scripts tornam as verificações de governança repetíveis: a mesma lista verificada no mês seguinte será verificada do mesmo jeito, o que a contagem manual não consegue garantir quando a equipe está ocupada. Quando uma nova clínica é acrescentada ao CSV, o script a conta sem nenhuma mudança no código.

### 3.2 Filtrar

Priya filtra os ativos com dados de pacientes que não têm dono e aqueles cuja data da última atualização tem mais de um ano. O script imprime cada um com sua clínica. Aparecem dois aparelhos de imagem e um computador antigo da recepção. Ela aprende que combinar condições concentra a atenção nas lacunas mais arriscadas. Filtrar por sensibilidade e idade ajuda os gestores a decidir o que corrigir primeiro, em vez de receber uma lista longa sem prioridades. Um aparelho de imagem que guarda imagens de pacientes, sem dono e sem atualização há um ano, é exatamente o que o filtro combinado deve pegar.

### 3.3 Saída clara

O Sr. Lind revisa a saída de Priya e pergunta se um gerente de clínica a entenderia. Ela acrescenta cabeçalhos, a data da verificação e uma explicação curta de cada problema. Também ordena os resultados por clínica, para que cada gerente veja os próprios itens. Ela aprende que a saída faz parte do controle: resultados confusos são ignorados, enquanto resultados claros, ordenados e explicados levam os responsáveis a agir. Ordenar por clínica significa que cada um dos catorze gerentes encontra os próprios itens em segundos.

### Exemplo resolvido

Priya escreve contagens e filtros sobre a lista de ativos e reescreve a saída, ordenada por clínica e com explicações.

> **Caso sintético.** A lista de ativos é sintética.

### Erros e limites

Os scripts dependem de entradas corretas. Datas antigas podem ser erros nos dados.

### Exercícios

- **EX007 — Repetibilidade.** Por que os scripts são melhores que a contagem manual para verificações repetidas? *Rubrica:* 3 = a mesma verificação roda do mesmo jeito toda vez;; 2 = repetível;; 1 = nada;; 0 = nenhuma.
- **EX008 — Condições do filtro.** Que duas condições Priya combinou? *Rubrica:* 3 = dados de pacientes sem dono, ou sem atualização há mais de um ano;; 2 = sensibilidade e idade;; 1 = nada;; 0 = nenhuma.
- **EX009 — Mudança na saída.** Como Priya melhorou a saída? *Rubrica:* 3 = cabeçalhos, data, explicações, ordenação por clínica;; 2 = clareza;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem

Você vai (1) modelar os dados de governança como tabelas relacionadas; (2) definir chaves e relacionamentos; (3) evitar duplicação e inconsistência.

### 4.1 Tabelas

Priya desenha tabelas para os dados de governança da Riverton: clínicas, ativos, donos, riscos e controles. Cada tabela tem uma chave: o código da clínica, a etiqueta patrimonial do ativo, a matrícula do dono. Tabelas separadas evitam repetir a mesma informação muitas vezes, como o endereço de uma clínica em cada linha de ativo. Ela aprende que dados bem estruturados facilitam responder perguntas e dificultam a introdução de erros quando as informações mudam. Se uma clínica se muda, por exemplo, o endereço muda numa só linha da tabela de clínicas, e não em cada linha de ativo.

### 4.2 Relacionamentos

Os ativos pertencem às clínicas, os donos respondem pelos ativos, os riscos afetam os ativos e os controles tratam os riscos. Priya desenha esses relacionamentos. Descobre que um controle, os notebooks criptografados, trata vários riscos, e que um risco, o ransomware, afeta muitos ativos. Aprende que relacionamentos muitos-para-muitos precisam de tabelas de ligação. Acertar os relacionamentos permite à Riverton responder perguntas como quais riscos dependem de um controle que falhou, o que é importante nas auditorias. Uma tabela de ligação entre controles e riscos, por exemplo, permite que um único teste de criptografia atualize o status de todos os riscos que ele trata.

### 4.3 Consistência

Na planilha antiga, a mesma clínica aparece como North, North Clinic e N. Priya padroniza os nomes com códigos e acrescenta regras de validação para que só códigos válidos possam ser digitados. Ela aprende que a inconsistência é uma fonte comum de erros nos relatórios: as contagens por clínica estavam erradas porque a mesma clínica era escrita de formas diferentes. Regras simples de dados evitam problemas que, de outro modo, apareceriam nos relatórios ao conselho e nos achados de auditoria. O Sr. Lind observa que as três grafias de North tinham feito essa clínica parecer menor do que era em todas as contagens por clínica.

### Exemplo resolvido

Priya modela os dados de governança em tabelas relacionadas com chaves, usa tabelas de ligação para os relacionamentos muitos-para-muitos e padroniza os códigos das clínicas.

> **Caso sintético.** O modelo de dados é sintético.

### Erros e limites

Os modelos precisam de manutenção. Os códigos também podem ser digitados errado.

### Exercícios

- **EX010 — Exemplo de chave.** Dê uma chave usada nas tabelas de Priya. *Rubrica:* 3 = código da clínica, etiqueta patrimonial ou matrícula;; 2 = chave;; 1 = nada;; 0 = nenhuma.
- **EX011 — Tabelas de ligação.** Quando são necessárias tabelas de ligação? *Rubrica:* 3 = para relacionamentos muitos-para-muitos;; 2 = muitos-para-muitos;; 1 = nada;; 0 = nenhuma.
- **EX012 — Nomes das clínicas.** Que problema os nomes inconsistentes das clínicas causaram? *Rubrica:* 3 = contagens erradas por clínica;; 2 = erros de contagem;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) explicar as ameaças comuns às clínicas odontológicas; (2) ligar as ameaças a controles simples; (3) comunicar a segurança com clareza à equipe clínica.

### 5.1 Ameaças às clínicas

Priya estuda as ameaças mais relevantes para a Riverton: e-mails de phishing dirigidos à recepção, ransomware capaz de parar as clínicas, informações de pacientes enviadas ao destinatário errado, notebooks perdidos e fraude por meio de faturas falsas de fornecedores. Os dados de saúde são valiosos e as clínicas são movimentadas, então os erros acontecem sob pressão de tempo. Ela observa que entender as ameaças do dia a dia ajuda a Riverton a gastar seu esforço limitado em controles que evitam os danos mais comuns, e não cenários raros. As faturas falsas de fornecedores, por exemplo, miram o processo financeiro, e não os dentistas, então seus controles ficam em outro lugar.

### 5.2 Controles simples

Para cada ameaça, Priya lista controles simples: autenticação multifator no e-mail, backups offline do sistema do consultório e do arquivo de imagens, mensagens seguras para informações de pacientes, criptografia dos notebooks e uma confirmação por telefone (callback) quando os dados bancários de um fornecedor mudam. Ela observa que a maioria dos controles já existe nos sistemas da Riverton, mas não está ativada de forma consistente. Aprende que governança muitas vezes significa garantir que os recursos existentes sejam usados, em vez de comprar ferramentas novas. Ativar o callback para dados bancários alterados, por exemplo, exige um procedimento, não uma compra.

### 5.3 Falar com a equipe clínica

Priya prepara uma palestra de dez minutos para a equipe das clínicas. Usa exemplos da prática odontológica, evita o jargão e explica como cada controle protege os pacientes. Incentiva a equipe a relatar os erros depressa, explicando que um e-mail enviado ao destinatário errado e relatado em minutos muitas vezes pode ser recuperado. Ela aprende que os profissionais clínicos respondem a argumentos de segurança do paciente e que mensagens respeitosas e práticas funcionam melhor que medo ou culpa. Apresentar a criptografia dos notebooks como proteção do sigilo do paciente, por exemplo, fala ao que eles já valorizam. Ela encerra mostrando exatamente como relatar um erro.

### Exemplo resolvido

Priya identifica cinco ameaças às clínicas, liga-as a controles já existentes e faz uma palestra prática, centrada no paciente.

> **Caso sintético.** As ameaças e a palestra são sintéticas.

### Erros e limites

As palestras se apagam sem reforço. Os recursos precisam de configuração.

### Exercícios

- **EX013 — Controle contra fraude.** Que controle trata as faturas falsas de fornecedores? *Rubrica:* 3 = callback para dados bancários alterados;; 2 = callback;; 1 = nada;; 0 = nenhuma.
- **EX014 — Recursos existentes.** Que lacuna de governança Priya encontrou nos controles? *Rubrica:* 3 = recursos disponíveis, mas não ativados de forma consistente;; 2 = recursos sem uso;; 1 = nada;; 0 = nenhuma.
- **EX015 — Argumento para clínicos.** Que argumento funciona melhor com a equipe clínica? *Rubrica:* 3 = segurança do paciente;; 2 = pacientes;; 1 = medo;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem

Você vai (1) relacionar as configurações do sistema operacional às políticas da Riverton; (2) entender máquinas virtuais e hospedagem em nuvem; (3) verificar a consistência da configuração entre as clínicas.

### 6.1 Configurações e políticas

A política da Riverton exige bloqueio de tela, atualizações automáticas, criptografia e nenhum direito de administrador local nos computadores da recepção. Priya aprende como cada requisito corresponde a configurações do sistema operacional gerenciadas centralmente pelo gerenciamento de dispositivos. Também aprende que os aparelhos de imagem costumam rodar sistemas operacionais antigos controlados pelos fornecedores, e por isso não conseguem seguir as mesmas configurações. Essas exceções precisam de tratamento à parte, como o isolamento de rede, registrado no registro de riscos. Isolar os aparelhos de imagem num segmento próprio permite que mantenham o software controlado pelo fornecedor, limitando o que consegue alcançá-los.

### 6.2 Virtualização e nuvem

O sistema de gestão do consultório roda em máquinas virtuais hospedadas por um provedor de nuvem. Priya aprende que a virtualização permite que muitos sistemas compartilhem o hardware, enquanto o provedor cuida da camada física. A governança precisa, portanto, definir que tarefas de segurança cabem ao provedor e quais cabem à Riverton. No modelo de responsabilidade compartilhada, o provedor protege a infraestrutura, e a Riverton controla o acesso dos usuários e a configuração. Ela observa que os mal-entendidos sobre essa divisão são fontes comuns de lacunas. O acesso dos usuários ao sistema do consultório, por exemplo, continua sendo tarefa da Riverton, mesmo que o provedor opere os servidores.

### 6.3 Consistência

Priya compara as configurações das catorze clínicas usando o relatório do gerenciamento de dispositivos. Onze clínicas seguem a linha de base. Três têm computadores da recepção com o bloqueio de tela desativado, porque a equipe o achava incômodo nos horários de pico. Ela sugere um tempo de bloqueio maior com um método rápido de desbloqueio, em vez de nenhum bloqueio. Aprende que a inconsistência muitas vezes reflete problemas reais de usabilidade, e que ajustar o controle pode trazer conformidade sem brigar com a equipe das clínicas. Um tempo maior com desbloqueio rápido mantém algum bloqueio nas três clínicas movimentadas, em vez de nenhum.

### Exemplo resolvido

Priya liga a política às configurações, isola os aparelhos de imagem gerenciados pelos fornecedores, esclarece as responsabilidades na nuvem e corrige as inconsistências de bloqueio de tela com um meio-termo utilizável.

> **Caso sintético.** As configurações e as clínicas são sintéticas.

### Erros e limites

Os relatórios podem estar atrasados em relação à realidade. Os termos de responsabilidade compartilhada variam por provedor.

### Exercícios

- **EX016 — Exceção das imagens.** Como devem ser tratados os aparelhos de imagem com sistemas operacionais antigos? *Rubrica:* 3 = isolamento de rede registrado no registro de riscos;; 2 = isolamento;; 1 = nada;; 0 = nenhuma.
- **EX017 — Dever do provedor.** Na responsabilidade compartilhada, o que a Riverton controla? *Rubrica:* 3 = o acesso dos usuários e a configuração;; 2 = acesso;; 1 = infraestrutura;; 0 = nenhuma.
- **EX018 — Correção do bloqueio de tela.** O que Priya sugeriu em vez dos bloqueios desativados? *Rubrica:* 3 = tempo maior com desbloqueio rápido;; 2 = meio-termo utilizável;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem

Você vai (1) gerir as contas ao longo dos eventos do ciclo de vida dos funcionários; (2) aplicar o acesso baseado em papéis; (3) lidar com contas compartilhadas.

### 7.1 Ciclo de vida

As clínicas odontológicas empregam muitos funcionários de meio período e temporários. Priya mapeia como a Riverton cria, altera e remove contas. Os novos funcionários recebem contas depressa, mas dentistas substitutos e auxiliares temporárias muitas vezes mantêm o acesso depois do último plantão, porque os gerentes das clínicas esquecem de avisar a TI. Ela propõe que as contas temporárias sejam criadas com uma data de término que as desative automaticamente, e que os gerentes confirmem as prorrogações. Isso reduz a dependência da memória. Uma data de término definida na criação faz o acesso de um substituto expirar mesmo quando ninguém se lembra de avisar a TI.

### 7.2 Papéis

Priya define papéis para o sistema do consultório: recepcionista, auxiliar de saúde bucal, dentista, técnico em higiene dental e gerente de clínica. Cada papel tem o acesso necessário para suas tarefas. As recepcionistas veem as consultas e os dados de contato, mas não as anotações clínicas. Os dentistas veem os prontuários completos dos próprios pacientes. Ela aprende que o acesso baseado em papéis simplifica a governança, porque as revisões verificam as atribuições de papéis em vez de centenas de permissões individuais, o que as torna mais rápidas e precisas. O Sr. Lind observa que deixar as anotações clínicas fora do papel de recepcionista também reduz quantas pessoas poderiam vazá-las por engano.

### 7.3 Contas compartilhadas

Algumas clínicas usam uma conta compartilhada na recepção para que a equipe troque de usuário depressa. Priya explica que as contas compartilhadas tornam impossível saber quem fez o quê, o que importa nas auditorias de prontuários. Ela sugere a troca rápida de usuário com contas individuais e login curto por crachá. As clínicas aceitam testar primeiro em duas unidades. Ela aprende que eliminar as contas compartilhadas exige uma alternativa utilizável, senão a equipe as recria. Começar por duas unidades permite testar o login por crachá em recepções movimentadas antes que as catorze clínicas o adotem.

### Exemplo resolvido

Priya acrescenta datas de término automáticas às contas temporárias, define cinco papéis no sistema do consultório e testa o login rápido individual no lugar das contas compartilhadas.

> **Caso sintético.** Os papéis e os processos são sintéticos.

### Erros e limites

As datas de término podem cortar um acesso necessário. Os sistemas de crachá custam dinheiro.

### Exercícios

- **EX019 — Correção para temporários.** Como as contas temporárias são controladas? *Rubrica:* 3 = criadas com data de término que as desativa automaticamente;; 2 = expiração;; 1 = nada;; 0 = nenhuma.
- **EX020 — Acesso da recepcionista.** O que as recepcionistas não podem ver? *Rubrica:* 3 = as anotações clínicas;; 2 = anotações;; 1 = consultas;; 0 = nenhuma.
- **EX021 — Problema da conta compartilhada.** Por que as contas compartilhadas da recepção são um problema? *Rubrica:* 3 = é impossível saber quem fez o quê;; 2 = responsabilização;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever um desenho padrão seguro para as clínicas; (2) aplicar proteção em camadas; (3) registrar os desvios em relação ao padrão.

### 8.1 A clínica padrão

Priya ajuda a redigir um desenho padrão para as clínicas da Riverton: segmentos de rede separados para os aparelhos clínicos, a recepção, as maquininhas de cartão e o Wi-Fi de visitantes; computadores gerenciados e criptografados; contas individuais com autenticação multifator para os serviços em nuvem; e backups offline do arquivo de imagens. Um desenho padrão torna as clínicas mais fáceis de dar suporte e de auditar, porque todas devem ser iguais e as diferenças saltam aos olhos. Como todas as clínicas devem seguir o padrão, um Wi-Fi de visitantes ligado aos computadores da recepção numa clínica vira uma exceção óbvia a corrigir.

### 8.2 Camadas

Priya aplica a proteção em camadas ao ransomware. A filtragem de e-mail bloqueia muitos ataques. A autenticação multifator impede que senhas roubadas sejam reaproveitadas. Os controles de dispositivo limitam softwares desconhecidos. Os segmentos de rede limitam a propagação da recepção para as imagens. Os backups offline permitem a recuperação. Ela aprende que cada camada pega parte do que as outras deixam passar, e que uma clínica com todas as camadas é muito mais resiliente do que uma que depende de um único controle forte. Os segmentos entre a recepção e as imagens importam mais justamente quando a filtragem de e-mail e a autenticação já foram contornadas.

### 8.3 Desvios

Duas clínicas em prédios antigos não conseguem instalar cabeamento de rede separado tão cedo. Priya registra cada desvio num registro: o que difere, por quê, o risco e as medidas compensatórias, como a segmentação sem fio, além de uma data de revisão. Ela aprende que registrar os desvios os mantém visíveis e gerenciados. Sem registro, as exceções se espalham em silêncio até que o padrão exista só no papel, o que os auditores descobrem depressa. A segmentação sem fio nos dois prédios antigos dá uma separação parcial até que o cabeamento possa ser instalado, e cada data de revisão obriga a decidir se ele já pode ser instalado.

### Exemplo resolvido

Priya redige um desenho padrão de clínica com quatro segmentos, organiza em camadas as defesas contra ransomware e registra dois desvios ligados aos prédios.

> **Caso sintético.** O desenho é sintético.

### Erros e limites

Os padrões ficam atrás dos novos aparelhos. As medidas compensatórias podem ser mais fracas.

### Exercícios

- **EX022 — Quatro segmentos.** Que quatro segmentos de rede o padrão define? *Rubrica:* 3 = aparelhos clínicos, recepção, maquininhas de cartão, Wi-Fi de visitantes;; 2 = quatro;; 1 = nada;; 0 = nenhuma.
- **EX023 — Benefício do padrão.** Por que um desenho padrão ajuda as auditorias? *Rubrica:* 3 = as diferenças entre as clínicas saltam aos olhos;; 2 = consistência;; 1 = nada;; 0 = nenhuma.
- **EX024 — Registro de desvio.** O que cada registro de desvio inclui? *Rubrica:* 3 = diferença, motivo, risco, medidas compensatórias e data de revisão;; 2 = registro;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) manter um registro de evidências dos controles; (2) verificar a atualidade das evidências; (3) relatar as evidências vencidas.

### 9.1 Registro de evidências

A Riverton coleta evidências de que os controles funcionam: testes de restauração de backup, revisões de acesso, revisões de firewall, ciência das políticas, relatórios de garantia de fornecedores e relatórios de criptografia. Priya monta um registro com cada item, sua data e a idade máxima permitida antes de ser renovado. Ela aprende que as evidências têm prazo de validade: um teste de backup do ano passado diz pouco sobre se os backups funcionam hoje, então as regras de atualidade importam tanto quanto a própria evidência. A idade máxima de cada item vira a regra aplicada na verificação de atualidade que vem a seguir.

### 9.2 Verificar a atualidade

O laboratório verifica seis itens contra seus limites no último dia de setembro. Três estão vencidos. A revisão de acesso do segundo trimestre tem noventa e quatro dias, contra um limite de noventa. A revisão das regras de firewall tem duzentos e trinta e dois dias, contra cento e oitenta. O relatório SOC 2 do fornecedor tem quatrocentos e cinquenta e sete dias, contra um ano. O teste de backup, a ciência das políticas e o relatório de criptografia estão em dia. Priya observa que a revisão de acesso está só um pouco atrasada: quatro dias além dos noventa pedem um lembrete, enquanto o SOC 2 com quatrocentos e cinquenta e sete dias pede escalonamento.

### Laboratório — Verificar a atualidade das evidências

```python
"""Evidence freshness: items older than their allowed age (synthetic Riverton evidence log)."""
from datetime import date
today = date(2026, 9, 30)
log = [("backup restore test", date(2026, 7, 2), 90), ("access review Q2", date(2026, 6, 28), 90),
       ("firewall rule review", date(2026, 2, 10), 180), ("policy acknowledgement", date(2025, 11, 1), 365),
       ("vendor SOC 2 report", date(2025, 6, 30), 365), ("encryption report", date(2026, 9, 15), 30)]
stale = [(n, (today - d).days, m) for n, d, m in log if (today - d).days > m]
for n, age, m in stale: print(f"STALE {n}: {age} days old, limit {m}")
print(f"items {len(log)}; stale {len(stale)}; fresh {len(log) - len(stale)}")
```

Execute com `python3 lab_fresh.py`. Saída verificada:

```text
STALE access review Q2: 94 days old, limit 90
STALE firewall rule review: 232 days old, limit 180
STALE vendor SOC 2 report: 457 days old, limit 365
items 6; stale 3; fresh 3
```

### 9.3 Relatar

Priya relata os itens vencidos com seus donos e o tamanho de cada atraso. Trata o relatório do fornecedor como o mais grave, porque se refere ao provedor do sistema do consultório, que guarda todos os prontuários. Ela pede ao provedor o relatório mais recente. Aprende que medir a atualidade das evidências transforma um arquivo de garantia num controle vivo, e que atrasos pequenos merecem um lembrete, enquanto lacunas longas pedem escalonamento. Pedir ao provedor o relatório mais recente também testa se o contrato dá à Riverton o direito de recebê-lo.

### Exemplo resolvido

Priya monta um registro de evidências com limites de atualidade, encontra três itens vencidos e escala o relatório antigo do fornecedor.

> **Caso sintético.** Os itens de evidência são sintéticos.

### Erros e limites

Evidências atuais ainda podem ser fracas. Os limites são decisões de julgamento.

### Exercícios

- **EX025 — Prazo de validade.** Por que as evidências têm prazo de validade? *Rubrica:* 3 = testes antigos dizem pouco sobre a operação atual do controle;; 2 = atualidade;; 1 = nada;; 0 = nenhuma.
- **EX026 — Contagem de vencidos.** Quantos dos seis itens estavam vencidos? *Rubrica:* 3 = três;; 2 = 3;; 1 = nada;; 0 = nenhuma.
- **EX027 — O mais grave.** Que item vencido era o mais grave, e por quê? *Rubrica:* 3 = o relatório SOC 2 do fornecedor, pois o provedor guarda todos os prontuários;; 2 = fornecedor;; 1 = revisão de acesso;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Governança, riscos e compliance de segurança: orientação

### Objetivos de aprendizagem

Você vai (1) explicar governança, gestão de riscos e compliance num grupo de clínicas; (2) identificar as obrigações da Riverton; (3) descrever os papéis envolvidos.

### 10.1 Três partes

Priya começa as disciplinas de GRC. Governança significa que os líderes da Riverton definem a direção e acompanham o progresso: decidem que riscos são aceitáveis e quem é responsável. Gestão de riscos significa encontrar, avaliar e tratar os riscos de forma estruturada, seguindo princípios como os da ISO 31000:2018 (ABNT NBR ISO 31000:2018). Compliance significa cumprir as obrigações vindas da legislação de dados de saúde, das regras de pagamento com cartão e dos contratos. Ela aprende que as três partes precisam funcionar juntas para que a segurança seja gerida, e não improvisada. Na Riverton, por exemplo, o diretor-geral decidir o risco aceitável é governança, e verificar as obrigações do PCI DSS é compliance.

### 10.2 Obrigações

Priya lista as obrigações da Riverton: a lei de proteção de dados que cobre os prontuários, as regras de sigilo do setor de saúde, o PCI DSS v4.0 para os pagamentos com cartão por meio do seu banco, e os contratos com o provedor do sistema do consultório e com os laboratórios de prótese. Ela separa os deveres legais dos contratuais e dos padrões voluntários que a Riverton pode adotar, como o alinhamento ao NIST CSF 2.0. Aprende que saber de onde vem uma obrigação ajuda a definir sua prioridade e quem precisa ser envolvido. O Sr. Lind acrescenta que os contratos com os laboratórios também entram na lista, já que depois se descobre que dois laboratórios não têm acordo escrito.

### 10.3 Papéis

O diretor-geral da Riverton responde pelo risco. Um gerente de operações coordena a segurança com uma pequena equipe de TI e um prestador externo de suporte. Os gerentes das clínicas são donos dos controles locais, como o acesso da própria equipe. Um encarregado de proteção de dados orienta sobre os dados dos pacientes. Priya desenha um organograma simples desses papéis e observa que as responsabilidades do prestador externo não estão escritas em lugar nenhum. Recomenda esclarecê-las no contrato. Deveres não escritos significam, por exemplo, que ninguém sabe dizer se o prestador de suporte deve aplicar os patches nos roteadores das clínicas.

### Exemplo resolvido

Priya explica as três partes de GRC, lista as obrigações da Riverton por origem e descobre que as responsabilidades do prestador de suporte não estão documentadas.

> **Caso sintético.** A estrutura da Riverton é sintética; a ISO 31000:2018, o PCI DSS v4.0 e o CSF 2.0 são reais.

### Erros e limites

As obrigações legais exigem orientação profissional. Os papéis mudam com o crescimento.

### Exercícios

- **EX028 — Sentido de compliance.** O que compliance significa para a Riverton? *Rubrica:* 3 = cumprir as obrigações da lei, das regras de cartão e dos contratos;; 2 = obrigações;; 1 = nada;; 0 = nenhuma.
- **EX029 — Origem da obrigação.** Por que a origem de uma obrigação importa? *Rubrica:* 3 = define a prioridade e quem se envolve;; 2 = prioridade;; 1 = nada;; 0 = nenhuma.
- **EX030 — Papel não documentado.** As responsabilidades de quem não estavam escritas? *Rubrica:* 3 = as do prestador externo de suporte;; 2 = prestador;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Governança, riscos e compliance de segurança: ativos e contexto

### Objetivos de aprendizagem

Você vai (1) estabelecer o contexto da avaliação de riscos; (2) classificar os ativos de informação; (3) definir os critérios de risco com a direção.

### 11.1 Contexto

Antes de avaliar os riscos, Priya documenta o contexto da Riverton: seus serviços, pacientes, reguladores, fornecedores, planos de crescimento e postura diante do risco. A ISO 31000:2018 começa seu processo estabelecendo escopo, contexto e critérios. O diretor-geral explica que a Riverton planeja abrir três novas clínicas no ano que vem e que a reputação junto aos pacientes é seu maior ativo. Esses fatos definem quais riscos importam mais e quanta interrupção a Riverton pode aceitar. Três novas clínicas no ano que vem significam que o desenho padrão de clínica precisa estar pronto antes da inauguração.

### 11.2 Classificação

Priya classifica as informações em três níveis: pública, como o horário de funcionamento; interna, como as escalas da equipe; e confidencial, como os prontuários e as imagens. Cada nível tem regras de manuseio para armazenamento, compartilhamento e descarte. Os prontuários exigem criptografia e mensagens seguras; os dados internos ficam dentro dos sistemas da Riverton. Ela aprende que classificações simples têm mais chance de ser seguidas do que esquemas complexos, com muitos níveis que a equipe não consegue lembrar. As radiografias caem em confidencial, e por isso herdam automaticamente as regras de criptografia e de mensagens seguras.

### 11.3 Critérios de risco

Com a direção, Priya define critérios de probabilidade e impacto. Os níveis de impacto descrevem os efeitos sobre os pacientes, as finanças, os reguladores e a reputação. Por exemplo, um impacto grave significa clínicas fechadas por mais de um dia ou uma violação de dados notificável que atinja muitos pacientes. Os níveis de probabilidade usam faixas de frequência. Ela aprende que critérios acordados tornam as avaliações consistentes entre avaliadores, e que defini-los com a direção garante que reflitam as prioridades reais da Riverton. Definir o impacto grave como clínicas fechadas por mais de um dia, por exemplo, permite que dois avaliadores pontuem igual o mesmo cenário de ransomware.

### Exemplo resolvido

Priya documenta o contexto da Riverton, define três níveis de classificação e acorda com a direção os critérios de impacto e probabilidade.

> **Caso sintético.** O contexto e os critérios da Riverton são sintéticos; a ISO 31000:2018 é real.

### Erros e limites

Os critérios envolvem julgamento. As classificações são aplicadas de forma errada.

### Exercícios

- **EX031 — Fato de crescimento.** Que mudança planejada afeta o contexto da Riverton? *Rubrica:* 3 = três novas clínicas no ano que vem;; 2 = crescimento;; 1 = nada;; 0 = nenhuma.
- **EX032 — Níveis de classificação.** Quais são os três níveis de classificação? *Rubrica:* 3 = pública, interna, confidencial;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX033 — Impacto grave.** Dê o exemplo de impacto grave. *Rubrica:* 3 = clínicas fechadas por mais de um dia ou violação notificável que atinja muitos pacientes;; 2 = grave;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Governança, riscos e compliance de segurança: fluxos de dados

### Objetivos de aprendizagem

Você vai (1) mapear os fluxos de dados dos pacientes; (2) identificar os terceiros que recebem dados; (3) avaliar os riscos de cada fluxo.

### 12.1 Mapear os fluxos

Priya mapeia como os dados dos pacientes circulam: dos pacientes, pelo site de agendamento, para o sistema do consultório; das clínicas para o arquivo de imagens; dos dentistas para os laboratórios; da recepção para as operadoras e seguradoras, nos pedidos de reembolso; e do sistema do consultório para os backups. Para cada fluxo, registra os dados envolvidos, o meio e o destinatário. O mapa mostra onze fluxos, três dos quais envolvem partes externas além do provedor do sistema do consultório. Os três fluxos externos, para os laboratórios, as seguradoras e o provedor do site de agendamento, são examinados na seção seguinte.

### 12.2 Terceiros

Os laboratórios, as seguradoras e o provedor do site de agendamento recebem dados de pacientes. Priya verifica se cada um tem contrato com cláusulas de proteção de dados. Dois laboratórios não têm acordo escrito. Ela recomenda cláusulas padrão cobrindo sigilo, segurança e notificação de violações. Aprende que os terceiros são muitas vezes o elo mais fraco dos fluxos de dados, porque as organizações supõem, sem verificar, que os fornecedores protegem os dados. Cláusulas padrão para os dois laboratórios sem acordo também dariam à Riverton o direito contratual de ser avisada das violações. Ela ainda pede ao provedor do site de agendamento que confirme suas próprias cláusulas de notificação.

### 12.3 Riscos dos fluxos

Para cada fluxo, Priya anota os riscos: e-mails a laboratórios enviados ao destinatário errado, seguradoras recebendo mais dados do que o necessário e o site de agendamento coletando histórico médico de que não precisa. Ela recomenda reduzir os dados em cada etapa, usar mensagens seguras e revisar o que o formulário de agendamento pergunta. Aprende que a análise dos fluxos de dados revela riscos invisíveis numa lista de ativos, já que o dano muitas vezes ocorre enquanto os dados passam entre sistemas e organizações. O formulário que coleta histórico médico desnecessário, por exemplo, pode ser corrigido simplesmente removendo campos.

### Exemplo resolvido

Priya mapeia onze fluxos de dados de pacientes, encontra dois laboratórios sem acordo e recomenda reduzir os dados em cada etapa.

> **Caso sintético.** Os fluxos e as partes são sintéticos.

### Erros e limites

Os mapas deixam escapar fluxos informais, como fotos tiradas no celular. Os contratos não garantem a prática.

### Exercícios

- **EX034 — Contagem de fluxos.** Quantos fluxos de dados Priya mapeou? *Rubrica:* 3 = onze;; 2 = 11;; 1 = nada;; 0 = nenhuma.
- **EX035 — Acordos ausentes.** Que partes não tinham acordo escrito? *Rubrica:* 3 = dois laboratórios;; 2 = laboratórios;; 1 = seguradoras;; 0 = nenhuma.
- **EX036 — Problema do agendamento.** O que havia de errado com o site de agendamento? *Rubrica:* 3 = coletava histórico médico de que não precisava;; 2 = dados em excesso;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX036 (as de EX037–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Priya Natarajan, o Sr. Oskar Lind, o Halden Institute of Technology, o Riverton Dental Group e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Porque os dentistas os compraram diretamente dos fornecedores, por fora da TI.

**EX002.** Hardware, software, dados e serviços.

**EX003.** Os aparelhos de imagem e os prontuários.

**EX004.** Num segmento de rede separado dos demais aparelhos.

**EX005.** Os pedidos aos laboratórios enviados por e-mail comum.

**EX006.** Separar o Wi-Fi de visitantes dos aparelhos da clínica.

**EX007.** Porque a mesma verificação roda do mesmo jeito toda vez.

**EX008.** Ativos com dados de pacientes sem dono e ativos sem atualização há mais de um ano.

**EX009.** Acrescentou cabeçalhos, a data da verificação e explicações, e ordenou os resultados por clínica.

**EX010.** Por exemplo, o código da clínica, a etiqueta patrimonial ou a matrícula do dono.

**EX011.** Para relacionamentos muitos-para-muitos, como controles que tratam vários riscos.

**EX012.** As contagens por clínica estavam erradas porque a mesma clínica era escrita de formas diferentes.

**EX013.** Um callback quando os dados bancários de um fornecedor mudam.

**EX014.** A maioria dos controles existia nos sistemas da Riverton, mas não estava ativada de forma consistente.

**EX015.** A segurança do paciente, apresentada de forma respeitosa e prática.

**EX016.** Com tratamento à parte, como o isolamento de rede, registrado no registro de riscos.

**EX017.** O acesso dos usuários e a configuração.

**EX018.** Um tempo de bloqueio maior com um método rápido de desbloqueio.

**EX019.** São criadas com uma data de término que as desativa automaticamente, com prorrogações confirmadas pelo gerente.

**EX020.** As anotações clínicas.

**EX021.** Porque é impossível saber quem fez o quê nos prontuários.

**EX022.** Aparelhos clínicos, recepção, maquininhas de cartão e Wi-Fi de visitantes.

**EX023.** Porque todas as clínicas devem ser iguais, e assim as diferenças saltam aos olhos.

**EX024.** O que difere, por quê, o risco, as medidas compensatórias e uma data de revisão.

**EX025.** Porque evidências antigas dizem pouco sobre se os controles funcionam hoje.

**EX026.** Três.

**EX027.** O relatório SOC 2 do fornecedor, porque o provedor do sistema do consultório guarda todos os prontuários.

**EX028.** Cumprir as obrigações vindas da legislação de dados de saúde, das regras de pagamento com cartão e dos contratos.

**EX029.** Porque ajuda a definir a prioridade e quem precisa ser envolvido.

**EX030.** As do prestador externo de suporte.

**EX031.** A abertura de três novas clínicas no ano que vem.

**EX032.** Pública, interna e confidencial.

**EX033.** Clínicas fechadas por mais de um dia, ou uma violação notificável que atinja muitos pacientes.

**EX034.** Onze.

**EX035.** Dois laboratórios.

**EX036.** Coletava histórico médico de que não precisava.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO 31000:2018 e da ABNT NBR ISO/IEC 27001:2022, citadas nesta edição como referências brasileiras e conferidas em suas fontes oficiais; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Associação Brasileira de Normas Técnicas. (2018). *ABNT NBR ISO 31000:2018 — Gestão de riscos — Diretrizes*. ABNT. <https://www.abntcatalogo.com.br/>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
