# Governança, Riscos e Compliance de Segurança: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 074, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–30 de 30 têm texto didático escrito à mão na edição em inglês; os exercícios EX001–EX090 têm resoluções correspondentes com rubricas de 0 a 3; os cinco laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

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

- **EX001 — Ponto cego.** Por que os aparelhos de imagem faltavam na lista da TI? *Rubrica:* 3 = os dentistas os compraram diretamente dos fornecedores;; 2 = compra local;; 1 = vago;; 0 = nenhuma.
- **EX002 — Tipos de ativo.** Cite os quatro tipos de ativo que Priya usou. *Rubrica:* 3 = hardware, software, dados e serviços;; 2 = quatro;; 1 = vago;; 0 = nenhuma.
- **EX003 — Dependência do tratamento.** De que sistemas depende o tratamento? *Rubrica:* 3 = das imagens e dos prontuários;; 2 = imagens;; 1 = vago;; 0 = nenhuma.

### Síntese

Conhecer os sistemas, os ativos e os serviços que eles sustentam é onde a governança começa.

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
- **EX005 — Caminho sem criptografia.** Que caminho de dados nem sempre era criptografado? *Rubrica:* 3 = pedidos aos laboratórios por e-mail comum;; 2 = e-mail ao laboratório;; 1 = vago;; 0 = nenhuma.
- **EX006 — Primeira correção de rede.** Que correção ficou em primeiro lugar? *Rubrica:* 3 = separar o Wi-Fi de visitantes dos aparelhos da clínica;; 2 = Wi-Fi de visitantes;; 1 = vago;; 0 = nenhuma.

### Síntese

Mapas de rede revelam por onde os dados trafegam sem proteção e onde a segmentação é necessária.

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

- **EX007 — Repetibilidade.** Por que os scripts são melhores que a contagem manual para verificações repetidas? *Rubrica:* 3 = a mesma verificação roda do mesmo jeito toda vez;; 2 = repetível;; 1 = vago;; 0 = nenhuma.
- **EX008 — Condições do filtro.** Que duas condições Priya combinou? *Rubrica:* 3 = dados de pacientes sem dono, ou sem atualização há mais de um ano;; 2 = sensibilidade e idade;; 1 = vago;; 0 = nenhuma.
- **EX009 — Mudança na saída.** Como Priya melhorou a saída? *Rubrica:* 3 = cabeçalhos, data, explicações, ordenação por clínica;; 2 = clareza;; 1 = vago;; 0 = nenhuma.

### Síntese

Scripts simples com saída clara tornam as verificações de governança repetíveis e acionáveis.

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

- **EX010 — Exemplo de chave.** Dê uma chave usada nas tabelas de Priya. *Rubrica:* 3 = código da clínica, etiqueta patrimonial ou matrícula;; 2 = chave;; 1 = vago;; 0 = nenhuma.
- **EX011 — Tabelas de ligação.** Quando são necessárias tabelas de ligação? *Rubrica:* 3 = para relacionamentos muitos-para-muitos;; 2 = muitos-para-muitos;; 1 = vago;; 0 = nenhuma.
- **EX012 — Nomes das clínicas.** Que problema os nomes inconsistentes das clínicas causaram? *Rubrica:* 3 = contagens erradas por clínica;; 2 = erros de contagem;; 1 = vago;; 0 = nenhuma.

### Síntese

Tabelas relacionadas, com chaves e validação, mantêm os dados de governança consistentes.

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

- **EX013 — Controle contra fraude.** Que controle trata as faturas falsas de fornecedores? *Rubrica:* 3 = callback para dados bancários alterados;; 2 = callback;; 1 = vago;; 0 = nenhuma.
- **EX014 — Recursos existentes.** Que lacuna de governança Priya encontrou nos controles? *Rubrica:* 3 = recursos disponíveis, mas não ativados de forma consistente;; 2 = recursos sem uso;; 1 = vago;; 0 = nenhuma.
- **EX015 — Argumento para clínicos.** Que argumento funciona melhor com a equipe clínica? *Rubrica:* 3 = segurança do paciente;; 2 = pacientes;; 1 = medo;; 0 = nenhuma.

### Síntese

O letramento em segurança liga as ameaças comuns a controles simples já existentes e a uma comunicação respeitosa.

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

- **EX016 — Exceção das imagens.** Como devem ser tratados os aparelhos de imagem com sistemas operacionais antigos? *Rubrica:* 3 = isolamento de rede registrado no registro de riscos;; 2 = isolamento;; 1 = vago;; 0 = nenhuma.
- **EX017 — Dever do provedor.** Na responsabilidade compartilhada, o que a Riverton controla? *Rubrica:* 3 = o acesso dos usuários e a configuração;; 2 = acesso;; 1 = infraestrutura;; 0 = nenhuma.
- **EX018 — Correção do bloqueio de tela.** O que Priya sugeriu em vez dos bloqueios desativados? *Rubrica:* 3 = tempo maior com desbloqueio rápido;; 2 = meio-termo utilizável;; 1 = vago;; 0 = nenhuma.

### Síntese

As configurações impõem a política, mas as exceções e as responsabilidades compartilhadas precisam de governança explícita.

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

- **EX019 — Correção para temporários.** Como as contas temporárias são controladas? *Rubrica:* 3 = criadas com data de término que as desativa automaticamente;; 2 = expiração;; 1 = vago;; 0 = nenhuma.
- **EX020 — Acesso da recepcionista.** O que as recepcionistas não podem ver? *Rubrica:* 3 = as anotações clínicas;; 2 = anotações;; 1 = consultas;; 0 = nenhuma.
- **EX021 — Problema da conta compartilhada.** Por que as contas compartilhadas da recepção são um problema? *Rubrica:* 3 = é impossível saber quem fez o quê;; 2 = responsabilização;; 1 = vago;; 0 = nenhuma.

### Síntese

A governança de identidades lida com equipes temporárias, acesso baseado em funções e alternativas utilizáveis às contas compartilhadas.

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

- **EX022 — Quatro segmentos.** Que quatro segmentos de rede o padrão define? *Rubrica:* 3 = aparelhos clínicos, recepção, maquininhas de cartão, Wi-Fi de visitantes;; 2 = quatro;; 1 = vago;; 0 = nenhuma.
- **EX023 — Benefício do padrão.** Por que um desenho padrão ajuda as auditorias? *Rubrica:* 3 = as diferenças entre as clínicas saltam aos olhos;; 2 = consistência;; 1 = vago;; 0 = nenhuma.
- **EX024 — Registro de desvio.** O que cada registro de desvio inclui? *Rubrica:* 3 = diferença, motivo, risco, medidas compensatórias e data de revisão;; 2 = registro;; 1 = vago;; 0 = nenhuma.

### Síntese

Desenhos padronizados, com proteção em camadas e um registro de desvios, mantêm consistente a segurança em várias unidades.

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

- **EX025 — Prazo de validade.** Por que as evidências têm prazo de validade? *Rubrica:* 3 = testes antigos dizem pouco sobre a operação atual do controle;; 2 = atualidade;; 1 = vago;; 0 = nenhuma.
- **EX026 — Contagem de vencidos.** Quantos dos seis itens estavam vencidos? *Rubrica:* 3 = três;; 2 = 3;; 1 = vago;; 0 = nenhuma.
- **EX027 — O mais grave.** Que item vencido era o mais grave, e por quê? *Rubrica:* 3 = o relatório SOC 2 do fornecedor, pois o provedor guarda todos os prontuários;; 2 = fornecedor;; 1 = revisão de acesso;; 0 = nenhuma.

### Síntese

Regras de atualidade das evidências mantêm a garantia em dia e destacam o que precisa ser renovado.

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

- **EX028 — Sentido de compliance.** O que compliance significa para a Riverton? *Rubrica:* 3 = cumprir as obrigações da lei, das regras de cartão e dos contratos;; 2 = obrigações;; 1 = vago;; 0 = nenhuma.
- **EX029 — Origem da obrigação.** Por que a origem de uma obrigação importa? *Rubrica:* 3 = define a prioridade e quem se envolve;; 2 = prioridade;; 1 = vago;; 0 = nenhuma.
- **EX030 — Papel não documentado.** As responsabilidades de quem não estavam escritas? *Rubrica:* 3 = as do prestador externo de suporte;; 2 = prestador;; 1 = vago;; 0 = nenhuma.

### Síntese

A orientação em GRC conecta direção, gestão de riscos e obrigações por meio de papéis claros.

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

- **EX031 — Fato de crescimento.** Que mudança planejada afeta o contexto da Riverton? *Rubrica:* 3 = três novas clínicas no ano que vem;; 2 = crescimento;; 1 = vago;; 0 = nenhuma.
- **EX032 — Níveis de classificação.** Quais são os três níveis de classificação? *Rubrica:* 3 = pública, interna, confidencial;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX033 — Impacto grave.** Dê o exemplo de impacto grave. *Rubrica:* 3 = clínicas fechadas por mais de um dia ou violação notificável que atinja muitos pacientes;; 2 = grave;; 1 = vago;; 0 = nenhuma.

### Síntese

Contexto, classificação e critérios acordados tornam as avaliações de risco consistentes e relevantes.

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

- **EX034 — Contagem de fluxos.** Quantos fluxos de dados Priya mapeou? *Rubrica:* 3 = onze;; 2 = 11;; 1 = vago;; 0 = nenhuma.
- **EX035 — Acordos ausentes.** Que partes não tinham acordo escrito? *Rubrica:* 3 = dois laboratórios;; 2 = laboratórios;; 1 = seguradoras;; 0 = nenhuma.
- **EX036 — Problema do agendamento.** O que havia de errado com o site de agendamento? *Rubrica:* 3 = coletava histórico médico de que não precisava;; 2 = dados em excesso;; 1 = vago;; 0 = nenhuma.

### Síntese

Mapas de fluxo de dados revelam riscos de terceiros e de minimização que as listas de ativos não percebem.

<a id="ch-13"></a>

## Capítulo 13 — Governança, riscos e compliance de segurança: cenários de risco

### Objetivos de aprendizagem

Você vai (1) escrever cenários de risco para a Riverton; (2) identificar causas e consequências; (3) escolher cenários para análise detalhada.

### 13.1 Escrever cenários

Priya escreve os cenários de risco como histórias curtas, com uma causa, um evento e consequências. Um ransomware criptografa os computadores da recepção de uma clínica e se espalha para o arquivo de imagens, parando o atendimento por dias. Uma recepcionista envia o prontuário de um paciente ao laboratório errado. Um script malicioso no site de agendamento captura dados de cartão. Um notebook com listas de pacientes sem criptografia é furtado de um carro. Ela aprende que os cenários ajudam os gestores a imaginar os riscos de forma concreta e a julgá-los com bom senso. A história do notebook furtado, por exemplo, aponta direto para a criptografia como o controle que mudaria seu desfecho.

### 13.2 Causas e consequências

Para cada cenário, Priya lista as causas, como phishing ou falta de segmentação, e as consequências para os pacientes, as finanças, os reguladores e a reputação. No cenário de ransomware, as consequências incluem consultas canceladas, perda de receita, notificação ao regulador se houver prontuários afetados e reclamações de pacientes. Ela aprende que listar as causas aponta para os controles preventivos, enquanto listar as consequências aponta para o planejamento de recuperação e resposta. No ransomware, o phishing como causa aponta para os controles de e-mail, e as consultas canceladas apontam para a recuperação. Nos prontuários enviados ao destinatário errado, a causa costuma ser uma escolha apressada na recepção.

### 13.3 Escolher cenários

Com o gerente de operações, Priya escolhe quatro cenários para análise detalhada, com base no impacto provável e na preocupação da direção: ransomware numa clínica, prontuários enviados ao destinatário errado, captura de dados de cartão (skimming) no site de agendamento e notebooks perdidos. Os demais cenários ficam registrados para revisão posterior. Ela aprende que o esforço de análise deve se concentrar nos cenários que mais importam, e que uma lista curta e bem escolhida é mais útil do que uma lista longa que ninguém analisa. Registrar os outros cenários os mantém no registro para a próxima revisão, em vez de descartá-los.

### Exemplo resolvido

Priya escreve quatro cenários com causas e consequências e os seleciona para análise detalhada.

> **Caso sintético.** Os cenários são sintéticos.

### Erros e limites

Os cenários refletem os limites da imaginação. A seleção envolve julgamento.

### Exercícios

- **EX037 — Estrutura do cenário.** Que três partes cada cenário contém? *Rubrica:* 3 = causa, evento e consequências;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX038 — Uso das causas.** Para onde apontam as causas listadas? *Rubrica:* 3 = para os controles preventivos;; 2 = prevenção;; 1 = recuperação;; 0 = nenhuma.
- **EX039 — Lista curta.** Por que se concentrar numa lista curta de cenários? *Rubrica:* 3 = o esforço deve ir para onde mais importa;; 2 = foco;; 1 = vago;; 0 = nenhuma.

### Síntese

Cenários concretos ligam as causas à prevenção e as consequências à resposta.

<a id="ch-14"></a>

## Capítulo 14 — Governança, riscos e compliance de segurança: métodos I

### Objetivos de aprendizagem

Você vai (1) estimar a perda anual esperada dos cenários; (2) comparar os cenários em dinheiro; (3) reconhecer a incerteza das estimativas.

### 14.1 Estimar

Para os quatro cenários escolhidos, Priya pede aos gestores que estimem quantas vezes por ano cada um pode acontecer e um custo típico quando acontece. O ransomware numa clínica poderia acontecer cerca de uma vez a cada sete anos, a cento e oitenta mil. Os prontuários enviados ao destinatário errado, duas vezes por ano, a quatro mil. O skimming de cartão, uma vez em vinte anos, a duzentos e vinte mil. Um notebook perdido, uma vez por ano, a nove mil. Essas frequências e custos aproximados alimentam diretamente a comparação de perda esperada da seção seguinte.

### 14.2 Comparar

O laboratório multiplica a frequência pelo custo. O ransomware tem a maior perda anual esperada, vinte e sete mil; o skimming de cartão, onze mil; os notebooks perdidos, nove mil; e os prontuários enviados ao destinatário errado, oito mil. O total é de cinquenta e cinco mil por ano. Priya observa que os prontuários enviados errado acontecem com mais frequência, mas custam menos por ano, enquanto o ransomware é raro, mas o mais caro. A perda esperada ajuda a comparar cenários muito diferentes numa só escala. Poder pôr o ransomware em vinte e sete mil e os prontuários em oito mil na mesma escala é o que torna o ranking possível.

### Laboratório — Perda anual esperada de quatro cenários da Riverton

```python
"""Expected annual loss per scenario and in total (synthetic Riverton estimates)."""
sc = [("ransomware at a clinic", 0.15, 180_000), ("patient record misdirected", 2.0, 4_000),
      ("card skimming on booking site", 0.05, 220_000), ("lost clinic laptop", 1.0, 9_000)]
for n, f, m in sc: print(f"{n}: {f} x {m:,} = {f*m:,.0f}")
print(f"total {sum(f*m for _, f, m in sc):,.0f}")
```

Execute com `python3 lab_ale.py`. Saída verificada:

```text
ransomware at a clinic: 0.15 x 180,000 = 27,000
patient record misdirected: 2.0 x 4,000 = 8,000
card skimming on booking site: 0.05 x 220,000 = 11,000
lost clinic laptop: 1.0 x 9,000 = 9,000
total 55,000
```

### 14.3 Incerteza

O Sr. Lind pergunta quão confiantes os gestores estavam. Priya admite que as estimativas são aproximadas e que o custo do ransomware poderia ser muito maior se prontuários fossem roubados e muitos pacientes precisassem ser notificados. Ela registra cada estimativa com um valor baixo e um alto e anota a fonte. Aprende que números únicos são úteis para comparar, mas devem sempre ser lidos com sua incerteza, sobretudo nos eventos raros e graves, em que as médias escondem o que poderia de fato acontecer. No ransomware, por exemplo, o valor alto incluiria os custos de notificação caso prontuários fossem roubados.

### Exemplo resolvido

Priya calcula perdas anuais esperadas que somam cinquenta e cinco mil, com o ransomware no topo, a vinte e sete mil, e registra faixas para a incerteza.

> **Caso sintético.** As estimativas são sintéticas.

### Erros e limites

As estimativas dos gestores são aproximadas. As médias escondem desfechos graves.

### Exercícios

- **EX040 — Maior cenário.** Que cenário tem a maior perda anual esperada? *Rubrica:* 3 = ransomware, a 27 mil;; 2 = ransomware;; 1 = prontuários;; 0 = nenhuma.
- **EX041 — Perda total.** Qual é a perda anual esperada total? *Rubrica:* 3 = 55 mil;; 2 = 55.000;; 1 = vago;; 0 = nenhuma.
- **EX042 — Frequente, mas pequeno.** Que cenário acontece com mais frequência, mas custa menos por ano? *Rubrica:* 3 = prontuários enviados errado, a 8 mil;; 2 = prontuários;; 1 = vago;; 0 = nenhuma.

### Síntese

A perda esperada coloca cenários diferentes em uma mesma escala, mas precisa ser lida junto com a sua incerteza.

<a id="ch-15"></a>

## Capítulo 15 — Governança, riscos e compliance de segurança: laboratório guiado

### Objetivos de aprendizagem

Você vai (1) conduzir uma oficina guiada de avaliação de riscos; (2) registrar os resultados num registro; (3) acordar os donos dos tratamentos.

### 15.1 Oficina

Priya conduz uma oficina guiada com o gerente de operações, dois gerentes de clínica, o líder de TI e o encarregado de proteção de dados. Eles revisam os quatro cenários, as estimativas de perda esperada e os critérios. Cada participante dá sua opinião sobre probabilidade e impacto antes da discussão, para evitar que quem fala primeiro ancore todos os outros. As diferenças são discutidas e o grupo acorda as notas, registrando nas anotações qualquer discordância forte. Colher as opiniões antes da discussão importa aqui, porque o líder de TI e os gerentes de clínica podem ver a probabilidade do ransomware de modos muito diferentes.

### 15.2 Registro

Priya registra os resultados no registro de riscos da Riverton: cenário, dono, controles atuais, notas, faixa de perda esperada e tratamento proposto. Para o ransomware, o tratamento inclui concluir a segmentação de rede e testar os backups offline. Para os prontuários enviados errado, inclui mensagens seguras e orientação à equipe. Ela aprende que uma entrada do registro deve ser completa o bastante para que alguém que faltou à oficina entenda o risco e o que será feito. A entrada do ransomware, por exemplo, deve citar a segmentação e o teste dos backups offline, para que o leitor saiba exatamente o que muda.

### 15.3 Donos e prazos

Cada tratamento recebe um dono e uma data-alvo acordados na oficina. O líder de TI é dono da segmentação, prevista para quatro meses; os gerentes das clínicas são donos da adoção das mensagens seguras, prevista para dois meses. Priya agenda uma revisão de acompanhamento. Ela aprende que tratamentos sem dono e sem prazo raramente acontecem, e que acordá-los na própria reunião, em vez de atribuí-los depois, aumenta o comprometimento. O Sr. Lind sugere verificar primeiro, no acompanhamento, a meta de dois meses das mensagens seguras, já que ela vence antes da segmentação.

### Exemplo resolvido

Priya conduz uma oficina com opiniões iniciais independentes, registra quatro riscos e acorda donos e prazos para os tratamentos.

> **Caso sintético.** A oficina é sintética.

### Erros e limites

As oficinas refletem quem comparece. Os prazos escorregam.

### Exercícios

- **EX043 — Defesa contra a ancoragem.** Como Priya evitou a ancoragem na oficina? *Rubrica:* 3 = cada participante deu sua opinião antes da discussão;; 2 = opiniões independentes;; 1 = vago;; 0 = nenhuma.
- **EX044 — Tratamento do ransomware.** Que tratamentos foram propostos para o ransomware? *Rubrica:* 3 = segmentação de rede e teste dos backups offline;; 2 = dois;; 1 = vago;; 0 = nenhuma.
- **EX045 — Comprometimento.** Por que acordar donos e prazos na própria reunião? *Rubrica:* 3 = aumenta o comprometimento;; 2 = comprometimento;; 1 = vago;; 0 = nenhuma.

### Síntese

Oficinas guiadas, com visões independentes e donos acordados, produzem registros acionáveis.

<a id="ch-16"></a>

## Capítulo 16 — Governança, riscos e compliance de segurança: métodos II

### Objetivos de aprendizagem

Você vai (1) escolher opções de tratamento de riscos; (2) estimar o risco residual após o tratamento; (3) documentar as decisões de aceitação de riscos.

### 16.1 Opções de tratamento

Priya aprende quatro opções de tratamento: evitar a atividade, reduzir o risco com controles, compartilhá-lo por meio de seguro ou contratos, ou aceitá-lo. Para o skimming no site de agendamento, a Riverton poderia evitar o risco passando o pagamento com cartão para uma página hospedada pelo seu provedor de pagamentos, tirando por completo os dados de cartão do próprio site. Para o ransomware, ela escolhe reduzir o risco com segmentação e backups e compartilhar parte dele por meio de seguro cibernético. Cada escolha depende do custo, da eficácia e do apetite acordado com a direção.

### 16.2 Risco residual

Depois de escolher os tratamentos, Priya estima o risco residual. Com segmentação e backups testados, o custo esperado do cenário de ransomware cai, porque a propagação fica limitada e a recuperação é mais rápida. Passar para uma página de pagamento hospedada reduz drasticamente o risco de skimming, já que os dados de cartão deixam de passar pelo site da Riverton. Ela registra as estimativas residuais ao lado das originais, para que os gestores vejam o que cada tratamento consegue e se o risco restante está dentro do apetite. A estimativa do skimming, por exemplo, deve cair bem abaixo dos onze mil originais quando os dados de cartão saírem do site da Riverton.

### 16.3 Aceitação

Algum risco permanece. O diretor-geral aceita formalmente o risco residual dos notebooks perdidos, porque a criptografia torna improvável a exposição dos dados e os custos de reposição são modestos. Priya registra a aceitação com a data, os motivos, as condições e uma data de revisão. A ISO/IEC 27001:2022 espera que os donos dos riscos aprovem os planos de tratamento e aceitem os riscos residuais. Ela aprende que a aceitação formal torna as decisões responsabilizáveis e impede que os riscos sejam ignorados em silêncio. O Sr. Lind pergunta o que mudaria a decisão, e Priya registra a condição de que notebooks sem criptografia encontrados depois a reabririam.

### Exemplo resolvido

Priya aplica quatro opções de tratamento, estima o risco residual após a segmentação e a página de pagamento hospedada e registra a aceitação formal dos notebooks.

> **Caso sintético.** Os tratamentos e as estimativas são sintéticos; a ISO/IEC 27001:2022 é real.

### Erros e limites

As estimativas residuais são incertas. As condições do seguro limitam a cobertura.

### Exercícios

- **EX046 — Exemplo de evitar.** Como a Riverton pode evitar o risco de skimming? *Rubrica:* 3 = passar o pagamento com cartão para uma página hospedada;; 2 = página hospedada;; 1 = vago;; 0 = nenhuma.
- **EX047 — Finalidade do residual.** Por que registrar o residual ao lado das estimativas originais? *Rubrica:* 3 = para mostrar o que os tratamentos conseguem diante do apetite;; 2 = comparação;; 1 = vago;; 0 = nenhuma.
- **EX048 — Risco aceito.** Que risco residual o diretor-geral aceitou? *Rubrica:* 3 = notebooks perdidos;; 2 = notebooks;; 1 = ransomware;; 0 = nenhuma.

### Síntese

As escolhas de tratamento, as estimativas residuais e a aceitação formal completam o processo de risco.

<a id="ch-17"></a>

## Capítulo 17 — Governança, riscos e compliance de segurança: ferramentas

### Objetivos de aprendizagem

Você vai (1) usar scripts para processar os resultados dos testes de controles; (2) resumir os resultados por unidade; (3) identificar padrões entre as unidades.

### 17.1 Resultados de testes como dados

A Riverton começa a testar três controles em quatro clínicas-piloto: backups, bloqueio de tela e revisões de acesso. Os resultados são registrados num arquivo CSV compartilhado, com a clínica, o controle e aprovado ou reprovado. Priya escreve um script com o módulo csv da biblioteca padrão do Python para ler o arquivo e resumir os resultados. Ela aprende que formatos de dados simples e consistentes facilitam as ferramentas, e que um CSV com colunas claras sustenta análises úteis sem software caro. Doze linhas de clínica, controle e resultado bastam para mostrar que clínica precisa de ajuda primeiro.

### 17.2 Resumo por clínica

O laboratório lê doze resultados. A South passa nos três controles. A North e a West passam em dois de três. A East passa em apenas um de três. As falhas são a revisão de acesso na North, o bloqueio de tela e a revisão de acesso na East e o backup na West. Priya imprime o resumo para o gerente de operações e envia a cada gerente de clínica as próprias falhas, com uma nota sobre o que cada controle exige. A East, que falha em dois de três, recebe atenção primeiro, mas a seção seguinte mostra que as falhas de revisão de acesso têm uma causa comum.

### Laboratório — Taxas de aprovação por clínica a partir de um arquivo CSV

```python
"""Parse control test results and compute pass rates per clinic (synthetic CSV)."""
import csv, io
data = """clinic,control,result
North,backup,pass
North,screenlock,pass
North,access,fail
East,backup,pass
East,screenlock,fail
East,access,fail
South,backup,pass
South,screenlock,pass
South,access,pass
West,backup,fail
West,screenlock,pass
West,access,pass
"""
rows = list(csv.DictReader(io.StringIO(data))); by = {}
for r in rows: by.setdefault(r["clinic"], []).append(r["result"] == "pass")
for c, v in by.items(): print(f"{c}: {sum(v)}/{len(v)} passed")
fails = [f"{r['clinic']}/{r['control']}" for r in rows if r["result"] == "fail"]
print("failures:", ", ".join(fails))
```

Execute com `python3 lab_tests.py`. Saída verificada:

```text
North: 2/3 passed
East: 1/3 passed
South: 3/3 passed
West: 2/3 passed
failures: North/access, East/screenlock, East/access, West/backup
```

### 17.3 Padrões

Olhando para todas as clínicas, Priya vê que a revisão de acesso falhou em duas das quatro, mais do que qualquer outro controle. Ela pergunta por quê e descobre que os gerentes das clínicas não receberam as listas de contas a tempo. É um problema de processo, e não local, então ela recomenda corrigir a distribuição central das listas, em vez de culpar clínicas individuais. Aprende que as ferramentas valem mais quando ajudam a achar padrões que apontam para as causas-raiz. Corrigir uma vez a distribuição das listas deve melhorar os resultados da revisão de acesso em todas as clínicas, e não só na North e na East.

### Exemplo resolvido

Priya resume doze resultados de testes, constata que a East é a mais fraca e a South a mais forte e atribui as falhas repetidas de revisão de acesso à distribuição atrasada das listas.

> **Caso sintético.** Os resultados dos testes são sintéticos.

### Erros e limites

Quatro clínicas são um piloto pequeno. Aprovado ou reprovado perde detalhes.

### Exercícios

- **EX049 — Clínica mais forte.** Que clínica passou nos três controles? *Rubrica:* 3 = South;; 2 = South, hesitando com East;; 1 = East;; 0 = nenhuma.
- **EX050 — Lista de falhas.** Liste as quatro falhas. *Rubrica:* 3 = North acesso, East bloqueio de tela, East acesso, West backup;; 2 = quatro;; 1 = vago;; 0 = nenhuma.
- **EX051 — Causa do padrão.** Por que a revisão de acesso falhou em duas clínicas? *Rubrica:* 3 = os gerentes receberam as listas de contas atrasadas;; 2 = processo;; 1 = vago;; 0 = nenhuma.

### Síntese

Ferramentas simples resumem os resultados e revelam padrões entre unidades que apontam para as causas-raiz.

<a id="ch-18"></a>

## Capítulo 18 — Governança, riscos e compliance de segurança: controles

### Objetivos de aprendizagem

Você vai (1) documentar os controles com donos e frequências; (2) mapear os controles para as obrigações; (3) preparar uma declaração de aplicabilidade simples.

### 18.1 Documentar os controles

Priya documenta os controles-chave da Riverton num registro de controles: nome, objetivo, dono, frequência, como opera e a evidência produzida. Por exemplo, o teste mensal de backup tem como dono o líder de TI, restaura cinco arquivos de amostra do arquivo de imagens e produz um registro de teste datado. Ela aprende que uma documentação clara permite que qualquer pessoa teste um controle e que os donos saibam exatamente o que se espera deles, o que reduz as divergências nas auditorias. Cinco arquivos de amostra do arquivo de imagens dão um teste concreto e repetível, que qualquer técnico consegue fazer.

### 18.2 Mapear para as obrigações

Priya mapeia cada controle para as obrigações que ele apoia. A criptografia apoia a lei de proteção de dados. A segmentação das maquininhas de cartão apoia o PCI DSS v4.0. As revisões de acesso apoiam tanto a proteção de dados quanto os compromissos contratuais com o provedor do sistema do consultório. O mapeamento mostra quais obrigações dependem de quais controles, para que o impacto de um controle que falhou possa ser avaliado em termos de compliance. Ela aprende que um controle muitas vezes apoia várias obrigações, o que aumenta sua importância. As revisões de acesso, que apoiam a lei e o contrato com o provedor, ficam por isso entre os controles mais importantes da Riverton.

### 18.3 Declaração de aplicabilidade

A Riverton estuda obter a certificação ISO/IEC 27001:2022 em dois anos. Priya prepara um rascunho de declaração de aplicabilidade (SoA) que lista os controles de referência da ISO/IEC 27002:2022 e se cada um se aplica, com os motivos. Os controles de desenvolvimento seguro de software são marcados como não aplicáveis, porque a Riverton não desenvolve software, embora os controles de fornecedores cubram seus provedores. Ela aprende que preparar a declaração cedo esclarece o escopo e evidencia as lacunas muito antes de uma auditoria. Marcar os controles de fornecedores como aplicáveis deixa claro como a Riverton cobre o provedor do sistema do consultório.

### Exemplo resolvido

Priya monta um registro de controles, mapeia os controles para as obrigações e redige uma declaração de aplicabilidade com exclusões justificadas.

> **Caso sintético.** Os controles são sintéticos; a ISO/IEC 27001:2022, a 27002:2022 e o PCI DSS v4.0 são reais.

### Erros e limites

Os registros envelhecem. Os mapeamentos podem exagerar a cobertura.

### Exercícios

- **EX052 — Controle de backup.** Como opera o teste mensal de backup? *Rubrica:* 3 = o líder de TI restaura cinco arquivos de amostra e registra o resultado;; 2 = teste de restauração;; 1 = vago;; 0 = nenhuma.
- **EX053 — Várias obrigações.** Por que um controle que apoia várias obrigações importa mais? *Rubrica:* 3 = sua falha afeta várias obrigações;; 2 = importância;; 1 = vago;; 0 = nenhuma.
- **EX054 — Não aplicável.** Por que os controles de desenvolvimento seguro não se aplicam? *Rubrica:* 3 = a Riverton não desenvolve software;; 2 = sem desenvolvimento;; 1 = vago;; 0 = nenhuma.

### Síntese

Controles documentados e mapeados para as obrigações mostram para que serve cada controle e o que significa a sua falha.

<a id="ch-19"></a>

## Capítulo 19 — Governança, riscos e compliance de segurança: monitoramento

### Objetivos de aprendizagem

Você vai (1) definir indicadores-chave de risco; (2) acompanhar os indicadores no tempo contra limiares; (3) responder às violações de limiares.

### 19.1 Escolher indicadores

Priya ajuda a escolher indicadores-chave de risco (KRIs) que avisem cedo quando o risco sobe. Um deles é o número de vulnerabilidades críticas sem patch nos computadores da Riverton no fim do mês, com limiar de dez. Outros incluem revisões de acesso atrasadas e itens de evidência vencidos. Ela aprende que bons indicadores são mensuráveis a partir dos sistemas existentes, ligados a riscos específicos e revisados com regularidade, para que valores em alta provoquem ação antes que os incidentes ocorram. Um limiar de dez para as vulnerabilidades críticas, por exemplo, dá a quem revisa todo mês um ponto claro a partir do qual agir.

### 19.2 A tendência

O laboratório mostra seis meses do indicador de vulnerabilidades: seis em abril, oito em maio, doze em junho, catorze em julho, nove em agosto e sete em setembro. Junho e julho violam o limiar, com o pico de catorze em julho. Priya investiga e descobre que uma atualização do fornecedor do software de imagens atrasou, impedindo os patches do sistema operacional nos computadores da recepção que compartilham software com os aparelhos de imagem. A causa estava num fornecedor, então o indicador apontou para uma questão contratual, e não para a aplicação de patches pela equipe de TI.

### Laboratório — Tendência do indicador de vulnerabilidades contra um limiar

```python
"""KRI trend: unpatched critical vulnerabilities per month vs threshold 10 (synthetic)."""
months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]; vals = [6, 8, 12, 14, 9, 7]
for m, v in zip(months, vals): print(f"{m}: {v}{'  BREACH' if v > 10 else ''}")
print(f"breaches {sum(v > 10 for v in vals)}; peak {max(vals)} in {months[vals.index(max(vals))]}")
```

Execute com `python3 lab_trend.py`. Saída verificada:

```text
Apr: 6
May: 8
Jun: 12  BREACH
Jul: 14  BREACH
Aug: 9
Sep: 7
breaches 2; peak 14 in Jul
```

### 19.3 Responder

Quando o limiar foi violado, o líder de TI deveria ter escalado, mas ninguém acompanhava o indicador todo mês. Priya recomenda designar um dono para revisar os indicadores mensalmente e uma regra pela qual duas violações seguidas vão para o gerente de operações. Também sugere pedir no contrato que o fornecedor de imagens informe os prazos de atualização. Ela aprende que os indicadores só ajudam se alguém os acompanha e tem ações acordadas para quando os limiares são ultrapassados. Com a revisão mensal, a violação de junho, com doze, teria sido escalada antes do pico de catorze em julho.

### Exemplo resolvido

Priya acompanha um indicador de vulnerabilidades com duas violações e pico de catorze em julho, atribui-as a um atraso do fornecedor e define uma regra de escalonamento.

> **Caso sintético.** Os valores do indicador são sintéticos.

### Erros e limites

Os limiares são decisões de julgamento. Os indicadores podem ser manipulados.

### Exercícios

- **EX055 — Limiar.** Que limiar se aplica às vulnerabilidades críticas sem patch? *Rubrica:* 3 = dez;; 2 = 10;; 1 = vago;; 0 = nenhuma.
- **EX056 — Meses de violação.** Que meses violaram o limiar? *Rubrica:* 3 = junho e julho;; 2 = dois;; 1 = vago;; 0 = nenhuma.
- **EX057 — Regra de escalonamento.** Que regra de escalonamento Priya recomendou? *Rubrica:* 3 = duas violações seguidas vão para o gerente de operações;; 2 = regra;; 1 = vago;; 0 = nenhuma.

### Síntese

Os indicadores só alertam quando os donos os acompanham e ações acordadas se seguem às violações.

<a id="ch-20"></a>

## Capítulo 20 — Governança, riscos e compliance de segurança: solução de problemas

### Objetivos de aprendizagem

Você vai (1) investigar por que um controle não está funcionando; (2) separar problemas de desenho, de operação e de evidência; (3) corrigir a coisa certa.

### 20.1 Um controle que falha

O bloqueio de tela falha nos testes em várias clínicas, apesar da política e das configurações centrais. Priya investiga. Verifica a configuração do gerenciamento de dispositivos, visita duas clínicas e conversa com as recepcionistas. Ela aprende a separar três tipos de problema: de desenho, quando o próprio controle é inadequado; de operação, quando ele é adequado mas não é executado; e de evidência, quando ele funciona mas falta a prova. Cada um pede uma correção diferente, então o diagnóstico vem antes da ação. Visitar duas clínicas, em vez de só ler relatórios, é o que lhe permite distinguir esses três tipos de problema.

### 20.2 Diagnóstico

Priya descobre que a configuração central estava correta, mas as recepcionistas tinham encontrado um jeito de manter as telas acesas usando um reprodutor de mídia nos horários de pico, porque desbloquear repetidamente atrasava o check-in dos pacientes. O desenho não cabia no trabalho. Em outra clínica, o bloqueio funcionava, mas o teste registrou falha porque o testador verificou um computador reserva não gerenciado. Esse era um problema de evidência. Ela aprende que um mesmo sintoma pode esconder causas diferentes em lugares diferentes. O truque do reprodutor de mídia é um problema de desenho; o computador reserva não gerenciado, um problema de evidência.

### 20.3 Corrigir

Para o problema de desenho, Priya propõe o desbloqueio por crachá, que leva um segundo. Para o problema de evidência, atualiza as instruções de teste para verificar apenas os computadores gerenciados da recepção e registrar o reserva como um ativo separado. Ela evita recomendar medidas disciplinares contra as recepcionistas, já que o contorno revelou um problema de usabilidade. Aprende que solucionar problemas em controles de governança se parece com solucionar problemas de tecnologia: testar hipóteses, reunir evidências e corrigir a causa real. Registrar o computador reserva como ativo separado também o traz para o inventário, onde pode ser gerenciado ou aposentado.

### Exemplo resolvido

Priya separa problemas de desenho, operação e evidência, encontra um contorno de usabilidade e um erro de teste e corrige cada um da forma adequada.

> **Caso sintético.** A investigação é sintética.

### Erros e limites

Os contornos podem esconder uso malicioso. Os sistemas de crachá precisam de suporte.

### Exercícios

- **EX058 — Tipos de problema.** Que três tipos de problema de controle Priya separou? *Rubrica:* 3 = desenho, operação e evidência;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX059 — Causa do contorno.** Por que as recepcionistas mantinham as telas acesas? *Rubrica:* 3 = desbloquear repetidamente atrasava o check-in dos pacientes;; 2 = usabilidade;; 1 = preguiça;; 0 = nenhuma.
- **EX060 — Erro de evidência.** Que problema de evidência Priya encontrou? *Rubrica:* 3 = o testador verificou um computador reserva não gerenciado;; 2 = escopo do teste;; 1 = vago;; 0 = nenhuma.

### Síntese

Resolver problemas em controles significa diagnosticar separadamente os problemas de desenho, de operação e de evidências.

<a id="ch-21"></a>

## Capítulo 21 — Governança, riscos e compliance de segurança: integração de serviços

### Objetivos de aprendizagem

Você vai (1) integrar a GRC ao gerenciamento de serviços de TI; (2) ligar mudanças e incidentes aos riscos; (3) usar os chamados como evidência.

### 21.1 Integração

A equipe de TI da Riverton usa um sistema de chamados para solicitações, incidentes e mudanças. Priya propõe integrar a ele as tarefas de governança: os testes de controles viram chamados agendados, os tratamentos de risco viram itens de trabalho acompanhados e as exceções viram chamados com data de expiração. Ela aprende que integrar ao gerenciamento de serviços já existente reduz o esforço duplicado e garante que o trabalho de governança fique visível para quem o executa, em vez de viver numa planilha à parte. Os chamados de exceção com data de expiração, por exemplo, tornam o registro de desvios do capítulo 8 algo que a equipe de TI vê todo dia.

### 21.2 Mudanças e incidentes

Priya liga as mudanças e os incidentes aos riscos. Uma mudança que altera as redes das clínicas precisa referenciar o risco de segmentação de rede e ser conferida contra o desenho padrão. Um incidente envolvendo um e-mail enviado ao destinatário errado atualiza a probabilidade desse risco. Ela aprende que essa ligação transforma a atividade diária de TI em evidência sobre o risco e a eficácia dos controles, ajudando a governança a se manter atual entre as revisões formais. Ligar o incidente do e-mail enviado errado ao seu risco, por exemplo, dá à próxima revisão do registro evidências reais sobre a probabilidade.

### 21.3 Chamados como evidência

Os auditores podem amostrar chamados para verificar os controles. Um chamado agendado de teste de backup inclui a data, as etapas, o resultado e o registro de teste anexado. Priya define campos obrigatórios para que os chamados contenham informação suficiente para servir de evidência. Ela aprende que a evidência embutida no trabalho normal é mais confiável e menos trabalhosa do que a evidência montada pouco antes de uma auditoria, o que muitas vezes revela lacunas que não podem ser corrigidas retroativamente. Campos obrigatórios como o registro de teste anexado tornam um chamado utilizável por um auditor sem pedir ao líder de TI que o explique.

### Exemplo resolvido

Priya integra os testes de controles, os tratamentos e as exceções ao sistema de chamados e define os campos de evidência.

> **Caso sintético.** A configuração dos chamados é sintética.

### Erros e limites

Os campos dos chamados são pulados. As ligações exigem disciplina.

### Exercícios

- **EX061 — Exceções como chamados.** Como as exceções são tratadas no sistema de chamados? *Rubrica:* 3 = como chamados com data de expiração;; 2 = expiração;; 1 = vago;; 0 = nenhuma.
- **EX062 — Ligação com incidentes.** Como um incidente de e-mail enviado errado afeta o registro? *Rubrica:* 3 = atualiza a probabilidade desse risco;; 2 = atualização;; 1 = vago;; 0 = nenhuma.
- **EX063 — Momento da evidência.** Por que a evidência embutida no trabalho normal é melhor? *Rubrica:* 3 = mais confiável e menos trabalhosa que a montada antes da auditoria;; 2 = embutida;; 1 = vago;; 0 = nenhuma.

### Síntese

Integrar GRC à gestão de serviços faz com que o trabalho diário produza evidências de governança.

<a id="ch-22"></a>

## Capítulo 22 — Governança, riscos e compliance de segurança: automação

### Objetivos de aprendizagem

Você vai (1) automatizar uma verificação de conciliação; (2) interpretar os achados automatizados; (3) manter pessoas no circuito.

### 22.1 Conciliação

Priya automatiza uma verificação comum: comparar a lista de funcionários do RH com as contas do sistema do consultório. Um script lê as duas listas e relata as contas de pessoas marcadas como desligadas e as contas que não correspondem a ninguém na lista. Rodá-lo toda semana substitui uma comparação manual que tomava horas de um gerente de clínica a cada trimestre e muitas vezes era pulada. As execuções semanais também fazem a conta de um desligado ser encontrada em dias, e não na comparação trimestral seguinte. O script imprime cada achado com a clínica, para que o gerente certo possa confirmá-lo.

### 22.2 Achados

O laboratório compara uma lista de amostra com cinco pessoas e sete contas. Dois desligados, b.osei e d.wu, ainda têm contas. Duas contas, f.temp e g.test, não correspondem a ninguém na lista. São quatro problemas em sete contas. Priya investiga: f.temp foi criada para um dentista substituto e nunca removida, e g.test foi deixada pelo provedor do sistema do consultório depois da implantação. As duas contas órfãs são desativadas após confirmação com seus prováveis donos. O Sr. Lind observa que g.test mostra como o trabalho de implantação de um fornecedor pode deixar acessos para trás, o que o contrato com o provedor deveria tratar.

### Laboratório — Conciliar a lista do RH com as contas do sistema

```python
"""Reconcile HR roster with system accounts: leavers with access and orphan accounts."""
roster = {"a.khan": "active", "b.osei": "left", "c.lopez": "active", "d.wu": "left", "e.roy": "active"}
accounts = ["a.khan", "b.osei", "c.lopez", "d.wu", "f.temp", "e.roy", "g.test"]
leavers = [a for a in accounts if roster.get(a) == "left"]
orphans = [a for a in accounts if a not in roster]
print("leavers with accounts:", leavers); print("orphan accounts:", orphans)
print(f"accounts {len(accounts)}; issues {len(leavers) + len(orphans)}")
```

Execute com `python3 lab_recon.py`. Saída verificada:

```text
leavers with accounts: ['b.osei', 'd.wu']
orphan accounts: ['f.temp', 'g.test']
accounts 7; issues 4
```

### 22.3 Pessoas no circuito

Priya não deixa o script desativar contas automaticamente. Uma pessoa confere cada achado primeiro, porque um desligado pode ter voltado ou uma conta pode pertencer a um fornecedor com um motivo válido. Ela aprende que a automação deve cuidar da comparação repetitiva, enquanto as pessoas tomam as decisões que precisam de contexto. Os achados automatizados também precisam de donos, senão se acumulam sem leitura, o que anula o propósito de automatizar a verificação. Um substituto que volta, por exemplo, pode aparecer como desligado na lista e precisar da conta na semana seguinte.

### Exemplo resolvido

Priya automatiza a conciliação da lista de funcionários, encontra dois desligados e duas contas órfãs entre sete e mantém a confirmação humana antes de desativar.

> **Caso sintético.** Os nomes e as contas são sintéticos.

### Erros e limites

Divergências de nomes causam falsos achados. Relatórios não lidos anulam a automação.

### Exercícios

- **EX064 — Contas de desligados.** Que desligados ainda tinham contas? *Rubrica:* 3 = b.osei e d.wu;; 2 = dois;; 1 = vago;; 0 = nenhuma.
- **EX065 — Origem das órfãs.** De onde vieram as contas órfãs? *Rubrica:* 3 = uma conta de substituto e uma conta de teste do provedor;; 2 = origens;; 1 = vago;; 0 = nenhuma.
- **EX066 — Decisão manual.** Por que não desativar as contas automaticamente? *Rubrica:* 3 = os achados precisam de contexto que uma pessoa deve verificar;; 2 = contexto;; 1 = vago;; 0 = nenhuma.

### Síntese

A automação deve fazer a comparação repetitiva, enquanto as pessoas tomam as decisões que dependem de contexto.

<a id="ch-23"></a>

## Capítulo 23 — Governança, riscos e compliance de segurança: avaliação

### Objetivos de aprendizagem

Você vai (1) avaliar o primeiro ano do programa de GRC; (2) usar evidências para julgar o progresso; (3) recomendar melhorias.

### 23.1 Perguntas da avaliação

Depois de um ano, Priya ajuda a avaliar o programa da Riverton. Ela pergunta: os principais riscos estão menores? Os controles estão operando? As evidências estão em dia? Os donos estão engajados? Reúne dados do registro, dos resultados de testes, das tendências dos indicadores, do registro de evidências e de uma pesquisa curta com os gerentes das clínicas. Ela aprende que a avaliação deve usar várias fontes, já que qualquer medida isolada pode enganar, e que as perguntas devem ser definidas antes de olhar os dados. Definir as perguntas antes impede que a avaliação destaque só as medidas que melhoraram.

### 23.2 Achados

O risco de ransomware está menor: a segmentação está concluída em doze das catorze clínicas e os backups são testados todo mês. O risco de skimming caiu drasticamente após a passagem para a página de pagamento hospedada. Os testes de controles passam com mais frequência do que no piloto. A atualidade das evidências melhorou, embora os relatórios de fornecedores continuem atrasados. Os gerentes das clínicas dizem que as tarefas estão mais claras, mas que a revisão de acesso continua demorada. Priya apresenta os achados com as evidências de cada um. O atraso dos relatórios de fornecedores repete o problema de atualidade do capítulo 9, então a causa está nos contratos, e não nas clínicas.

### 23.3 Recomendações

Priya recomenda concluir a segmentação nas duas últimas clínicas, automatizar as listas da revisão de acesso, incluir o pedido de relatórios dos fornecedores nas renovações de contrato e simplificar o checklist dos gerentes de clínica. Também recomenda preparar a certificação ISO/IEC 27001:2022 para o ano que vem. Ela aprende que as avaliações são úteis quando levam a melhorias específicas e que reconhecer o progresso motiva a equipe a continuar o trabalho. Cada recomendação responde a um achado específico, como a revisão de acesso ainda demorada, e pode ser acompanhada como ação com dono no sistema de chamados.

### Exemplo resolvido

Priya avalia o programa com cinco fontes, constata a redução dos riscos de ransomware e de cartão e recomenda quatro melhorias.

> **Caso sintético.** Os dados da avaliação são sintéticos; a ISO/IEC 27001:2022 é real.

### Erros e limites

Um ano é pouco tempo. As respostas da pesquisa podem ser educadas demais.

### Exercícios

- **EX067 — Fontes da avaliação.** Que fontes a avaliação usou? *Rubrica:* 3 = registro, resultados de testes, indicadores, registro de evidências e pesquisa;; 2 = cinco;; 1 = vago;; 0 = nenhuma.
- **EX068 — Progresso da segmentação.** Quantas clínicas concluíram a segmentação? *Rubrica:* 3 = doze de catorze;; 2 = 12/14;; 1 = vago;; 0 = nenhuma.
- **EX069 — Carga restante.** Que tarefa continuou demorada? *Rubrica:* 3 = a revisão de acesso;; 2 = revisão de acesso, hesitando com outra opção;; 1 = vago;; 0 = nenhuma.

### Síntese

A avaliação com várias fontes mostra o progresso e aponta melhorias específicas.

<a id="ch-24"></a>

## Capítulo 24 — Métodos de pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) desenhar um pequeno estudo aplicado em GRC; (2) escolher dados e métodos adequados; (3) relatar os achados com seus limites.

### 24.1 Pergunta

Priya desenha um pequeno estudo: enviar aos gerentes das clínicas listas de revisão de acesso pré-preenchidas, com descrições dos papéis, reduz o tempo que eles gastam nas revisões? Ela define o tempo gasto como os minutos informados num registro curto, e a qualidade como o número de direitos inadequados encontrados por uma segunda verificação. Aprende que as perguntas aplicadas devem ser estreitas, mensuráveis e úteis para a organização, e não perguntas amplas que não podem ser respondidas num semestre. Medir a qualidade por uma segunda verificação protege contra listas que economizam tempo escondendo direitos inadequados.

### 24.2 Método

Sete clínicas recebem as listas novas e sete continuam com as antigas durante um trimestre, com a alocação feita por sorteio de nomes. Priya registra o tempo e a qualidade de cada uma. Ela anota as ameaças: os gerentes sabem que estão sendo estudados, as clínicas diferem em tamanho e um trimestre pode ser atípico. Aprende que a alocação aleatória ajuda a comparabilidade, mas não elimina todas as diferenças quando os grupos são pequenos. O sorteio evita, por exemplo, que as clínicas maiores fiquem todas com as listas novas. Ela registra cada ameaça no relatório para que os leitores pesem o resultado por conta própria.

### 24.3 Achados

Os gerentes com as listas novas informam uma mediana de quarenta minutos, contra noventa com as listas antigas. A segunda verificação encontra números semelhantes de direitos inadequados nos dois grupos. Priya relata que as listas novas economizaram tempo sem reduzir a qualidade neste pequeno estudo, deixando claros os limites. Ela aprende que o relato honesto de um estudo pequeno ainda pode sustentar uma decisão prática, desde que sua incerteza fique clara. Quarenta contra noventa minutos é uma diferença grande, mas sete clínicas por grupo são poucas para descartar totalmente o acaso.

### Exemplo resolvido

Priya aloca catorze clínicas por sorteio, encontra tempos medianos de revisão de quarenta contra noventa minutos, com qualidade semelhante, e relata os limites.

> **Caso sintético.** O estudo é sintético.

### Erros e limites

Tempo autodeclarado. Sete clínicas por grupo.

### Exercícios

- **EX070 — Medida de qualidade.** Como se mede a qualidade da revisão? *Rubrica:* 3 = direitos inadequados encontrados por uma segunda verificação;; 2 = segunda verificação;; 1 = vago;; 0 = nenhuma.
- **EX071 — Alocação.** Como as clínicas foram alocadas? *Rubrica:* 3 = por sorteio de nomes;; 2 = aleatória;; 1 = vago;; 0 = nenhuma.
- **EX072 — Resultado de tempo.** Que tempos medianos os grupos informaram? *Rubrica:* 3 = quarenta contra noventa minutos;; 2 = 40 contra 90;; 1 = vago;; 0 = nenhuma.

### Síntese

Estudos aplicados pequenos e bem desenhados sustentam decisões quando os seus limites são declarados.

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto em equipe

### Objetivos de aprendizagem

Você vai (1) trabalhar em equipe numa entrega de GRC; (2) dividir o trabalho e revisar a produção uns dos outros; (3) apresentar a um cliente.

### 25.1 O briefing

No ateliê de equipe, a Riverton pede ao grupo de Priya um pacote de integração para as três novas clínicas: um checklist de configuração segura, a lista dos controles de que o gerente da clínica é dono, os requisitos de evidência e uma sessão curta de treinamento. A equipe tem quatro membros com pontos fortes diferentes: redes, documentação, desenho de treinamentos e dados. Eles acordam papéis, prazos e uma pasta compartilhada. O Sr. Lind sugere que a especialista em dados verifique se cada requisito de evidência pode de fato ser produzido pelos sistemas das novas clínicas, antes que o pacote seja entregue ao cliente.

### 25.2 Revisão por pares

O trabalho de cada membro é revisado por outro antes da entrega. Os requisitos de evidência de Priya são revisados pelo especialista em documentação, que encontra dois termos usados de forma inconsistente. O desenho do treinamento é revisado por Priya, que sugere acrescentar um cenário sobre e-mails a laboratórios enviados ao destinatário errado. A revisão por pares pega erros e melhora a clareza. Ela aprende que revisar o trabalho dos outros é uma competência em si, que exige um retorno específico e respeitoso. O cenário dos e-mails a laboratórios parte de um risco que a Riverton já registrou, então o treinamento continua relevante.

### 25.3 Apresentação ao cliente

A equipe apresenta ao gerente de operações da Riverton e a uma gerente de clínica. Eles percorrem o checklist e demonstram o cenário de treinamento. A gerente de clínica pede uma versão do checklist em uma página, que a equipe produz no dia seguinte. Priya aprende que os clientes valorizam a usabilidade prática, e que ouvir o retorno durante uma apresentação é tão importante quanto apresentá-la bem. Um checklist de uma página tem mais chance de ser usado numa clínica nova e movimentada do que um documento mais longo, que ficaria esquecido numa gaveta da recepção.

### Exemplo resolvido

A equipe de Priya produz um pacote de integração para as novas clínicas, usa a revisão por pares para pegar inconsistências e adapta o checklist após o retorno do cliente.

> **Caso sintético.** O projeto é sintético.

### Erros e limites

A dinâmica das equipes varia. Os pedidos do cliente podem ampliar o escopo.

### Exercícios

- **EX073 — Conteúdo do pacote.** O que contém o pacote de integração? *Rubrica:* 3 = checklist de configuração, controles do gerente, requisitos de evidência, treinamento;; 2 = quatro partes;; 1 = vago;; 0 = nenhuma.
- **EX074 — Achado da revisão.** O que a revisão por pares encontrou no trabalho de Priya? *Rubrica:* 3 = dois termos usados de forma inconsistente;; 2 = inconsistência;; 1 = vago;; 0 = nenhuma.
- **EX075 — Pedido do cliente.** O que a gerente de clínica pediu? *Rubrica:* 3 = um checklist em uma página;; 2 = uma página;; 1 = vago;; 0 = nenhuma.

### Síntese

Projetos em equipe dão certo com papéis claros, revisão por pares e capacidade de resposta aos clientes.

<a id="ch-26"></a>

## Capítulo 26 — Governança, riscos e compliance de segurança: passagem operacional

### Objetivos de aprendizagem

Você vai (1) passar os processos de GRC para a equipe de operações; (2) escrever runbooks; (3) confirmar a prontidão antes da passagem.

### 26.1 Runbooks

Priya prepara runbooks para os processos que ajudou a construir: a conciliação semanal da lista de funcionários, a revisão mensal dos indicadores, a verificação de atualidade das evidências e a revisão trimestral de acesso. Cada runbook lista a finalidade, as etapas, as ferramentas, as saídas esperadas, o que fazer quando algo falha e quem contatar. Ela os escreve para uma pessoa que nunca fez a tarefa. Aprende que os runbooks tornam os processos independentes de quem os desenhou. A seção sobre o que fazer quando algo falha é a que mais importa, já que o coordenador vai enfrentá-la sem Priya por perto.

### 26.2 Prontidão

Antes da passagem, Priya observa o novo coordenador da equipe de TI executar cada processo usando apenas o runbook. O coordenador conclui três dos quatro sem ajuda. Na revisão dos indicadores, ele não tem certeza do que conta como escalonamento, então Priya acrescenta exemplos. Ela aprende que a prontidão deve ser demonstrada, e não presumida, e que o melhor teste de uma documentação é outra pessoa usá-la com sucesso. Os exemplos de escalonamento acrescentados fecham a única lacuna que o coordenador encontrou, e assim os runbooks ficam prontos para a passagem.

### 26.3 Propriedade

Priya confirma que cada processo tem um dono, um substituto e um lugar no calendário de governança. Ela combina que ficará disponível para dúvidas durante um mês, depois do qual o coordenador assume toda a responsabilidade. Aprende que um fim claro do apoio ajuda o novo dono a assumir a responsabilidade, enquanto um período curto de apoio reduz o risco de erros iniciais passarem despercebidos. Nomear um substituto para cada processo evita que a conciliação semanal pare quando o coordenador estiver ausente, por férias ou por doença.

### Exemplo resolvido

Priya escreve quatro runbooks, testa a prontidão observando o coordenador e confirma donos, substitutos e um mês de apoio.

> **Caso sintético.** A passagem é sintética.

### Erros e limites

Os runbooks envelhecem. Os substitutos podem não ter prática.

### Exercícios

- **EX076 — Público do runbook.** Para quem os runbooks devem ser escritos? *Rubrica:* 3 = para alguém que nunca fez a tarefa;; 2 = iniciante;; 1 = especialista;; 0 = nenhuma.
- **EX077 — Lacuna de prontidão.** Que processo precisou de mais orientação? *Rubrica:* 3 = o escalonamento na revisão dos indicadores;; 2 = escalonamento;; 1 = vago;; 0 = nenhuma.
- **EX078 — Período de apoio.** Por quanto tempo Priya ficará disponível após a passagem? *Rubrica:* 3 = um mês;; 2 = 1 mês;; 1 = vago;; 0 = nenhuma.

### Síntese

Os repasses dão certo quando os runbooks são testados pelos novos donos e o suporte tem um fim claro.

<a id="ch-27"></a>

## Capítulo 27 — Implantação e validação

### Objetivos de aprendizagem

Você vai (1) implantar o desenho padrão de clínica numa nova unidade; (2) validar os controles antes da inauguração; (3) registrar as evidências da validação.

### 27.1 Implantação

A primeira clínica nova está pronta para abrir. Priya apoia a implantação do desenho padrão: segmentos de rede, computadores gerenciados, maquininhas de cartão no próprio segmento, Wi-Fi de visitantes separado, aparelhos de imagem isolados e contas criadas com data de término para os temporários. Ela segue o checklist de integração produzido por sua equipe e registra cada etapa concluída com a data e o responsável. Registrar quem concluiu cada etapa dá à validação da seção seguinte uma trilha contra a qual conferir. O checklist também lista quem é dono de cada controle depois que a clínica abrir.

### 27.2 Validação

Antes de a clínica abrir, Priya valida os controles-chave. Verifica que o Wi-Fi de visitantes não alcança os aparelhos da clínica, que as maquininhas estão no seu segmento, que os computadores da recepção estão criptografados e bloqueiam corretamente, que os backups do arquivo de imagens rodam e que só funcionários autorizados têm contas. Uma verificação falha: um aparelho de imagem foi ligado ao segmento da recepção. O fornecedor corrige e Priya testa de novo com sucesso. Um aparelho de imagem no segmento da recepção é exatamente o caminho de propagação que o isolamento do desenho padrão deve bloquear.

### 27.3 Evidências

Priya registra os resultados da validação, com capturas de tela e notas de teste, no registro de evidências, marcando-os com o código da clínica e a data. O gerente de operações aprova a inauguração com base no relatório de validação. Ela aprende que validar antes de entrar em operação sai muito mais barato do que corrigir problemas depois que os pacientes chegam, e que um relatório de validação assinado dá à direção uma base clara para a decisão de abrir. Marcar as evidências com o código da clínica permite encontrar os registros da nova clínica ao lado dos das outras catorze.

### Exemplo resolvido

Priya implanta o desenho padrão numa nova clínica, valida cinco controles, corrige um aparelho de imagem mal posicionado e registra as evidências de aprovação.

> **Caso sintético.** A implantação é sintética.

### Erros e limites

A validação é uma fotografia de um momento. Os fornecedores podem religar aparelhos depois.

### Exercícios

- **EX079 — Verificação que falhou.** Que verificação da validação falhou? *Rubrica:* 3 = um aparelho de imagem no segmento da recepção;; 2 = imagem;; 1 = vago;; 0 = nenhuma.
- **EX080 — Base da aprovação.** Com base em quê o gerente de operações aprovou a inauguração? *Rubrica:* 3 = no relatório de validação;; 2 = relatório;; 1 = vago;; 0 = nenhuma.
- **EX081 — Valor antes da inauguração.** Por que validar antes de abrir? *Rubrica:* 3 = corrigir problemas antes de os pacientes chegarem é mais barato;; 2 = custo;; 1 = vago;; 0 = nenhuma.

### Síntese

Validar os controles antes da entrada em produção dá à gestão uma base clara e baseada em evidências para seguir em frente.

<a id="ch-28"></a>

## Capítulo 28 — Prática de campo

### Objetivos de aprendizagem

Você vai (1) aplicar competências de GRC num estágio supervisionado; (2) apoiar uma avaliação externa; (3) refletir sobre a conduta profissional.

### 28.1 Estágio

Priya passa um período de estágio com a equipe de operações da Riverton. Ela apoia o trabalho de rotina: revisar indicadores, verificar a atualidade das evidências, cobrar ações atrasadas e ajudar os gerentes das clínicas nas revisões de acesso. Aprende que boa parte do trabalho de GRC é acompanhamento constante, e não análise dramática, e que paciência e boas relações com a equipe ocupada das clínicas importam tanto quanto o conhecimento técnico. Cobrar ações atrasadas, por exemplo, depende de os gerentes confiarem que ela está ajudando, e não fiscalizando. Essas relações depois facilitam levantar achados incômodos.

### 28.2 Apoio à avaliação

O banco da Riverton pede uma autoavaliação PCI DSS por causa dos pagamentos com cartão. Com a página de pagamento hospedada e as maquininhas segmentadas, o escopo da Riverton é pequeno. Priya ajuda a reunir as evidências: diagramas de rede, inventários das maquininhas e a confirmação de conformidade do provedor de pagamentos. Ela aprende que as decisões de arquitetura anteriores tornaram a avaliação muito mais fácil, e que o trabalho de compliance é moldado por escolhas de desenho feitas muito antes de a avaliação começar. Os dados de cartão nunca tocarem o site da Riverton tiram do escopo a maioria dos sistemas que uma avaliação maior examinaria.

### 28.3 Conduta profissional

Durante o estágio, uma gerente de clínica pede a Priya que marque como concluída uma revisão de acesso atrasada, para evitar um escalonamento. Ela recusa com educação, explica que o registro precisa refletir a realidade e se oferece para ajudar a concluir a revisão naquela tarde. As duas a terminam juntas. Ela reflete que conduta profissional significa manter os registros honestos enquanto ajuda as pessoas a cumprir suas obrigações, e que recusar com gentileza e oferecer ajuda preserva a relação de trabalho. Concluir a revisão naquela tarde permitiu que o registro mostrasse com honestidade que ela foi feita, só um pouco atrasada.

### Exemplo resolvido

Priya apoia o trabalho de rotina de GRC, ajuda numa autoavaliação PCI DSS de escopo pequeno e se recusa a falsificar um registro enquanto ajuda a concluir a revisão.

> **Caso sintético.** O estágio é sintético; o PCI DSS é real.

### Erros e limites

A qualidade dos estágios varia. A pressão pode ser sutil.

### Exercícios

- **EX082 — Trabalho de rotina.** Em que consiste boa parte do trabalho de GRC? *Rubrica:* 3 = acompanhamento constante;; 2 = acompanhamento;; 1 = análise;; 0 = nenhuma.
- **EX083 — Motivo do escopo pequeno.** Por que o escopo PCI DSS da Riverton era pequeno? *Rubrica:* 3 = página de pagamento hospedada e maquininhas segmentadas;; 2 = desenho;; 1 = vago;; 0 = nenhuma.
- **EX084 — Resposta íntegra.** Como Priya respondeu ao pedido de marcar uma revisão como concluída? *Rubrica:* 3 = recusou e ajudou a concluí-la;; 2 = ajuda honesta;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática de campo mostra que o trabalho de GRC é constante, moldado pelo desenho e fundamentado em registros honestos.

<a id="ch-29"></a>

## Capítulo 29 — Construção do projeto final

### Objetivos de aprendizagem

Você vai (1) construir uma ferramenta de GRC para a Riverton como projeto final; (2) testá-la com usuários; (3) documentá-la para manutenção.

### 29.1 A ferramenta

Em seu projeto final, Priya constrói um pequeno painel de governança com a biblioteca padrão do Python, que lê o registro de riscos, os resultados dos testes de controles, os valores dos indicadores e o registro de evidências, e produz um resumo semanal em HTML para o gerente de operações. Ele destaca ações atrasadas, evidências vencidas, violações de limiares e controles que falharam, cada item com seu dono. Ela mantém o desenho simples para que o coordenador de TI da Riverton consiga mantê-lo. Usar só a biblioteca padrão significa que o coordenador não precisa de pacotes extras para mantê-lo funcionando.

### 29.2 Testes

Priya testa a ferramenta com dados de amostra que contêm problemas conhecidos, verificando se cada um é relatado corretamente. Depois pede ao gerente de operações e a dois gerentes de clínica que usem o resumo por duas semanas. Eles o acham útil, mas pedem um filtro por clínica. Um gerente percebe que uma ação resolvida ainda aparece porque o arquivo de origem não foi atualizado, o que leva Priya a acrescentar ao resumo a data da última atualização de cada fonte. Essa data permite ao leitor julgar se um item está de fato aberto ou só se baseia em dados desatualizados.

### 29.3 Documentação

Priya documenta a ferramenta: finalidade, entradas, saídas, como executá-la, como acrescentar uma nova verificação, limitações conhecidas e quem a mantém. Ela guarda o código no repositório da Riverton, com um registro de mudanças. Aprende que uma ferramenta de projeto final só dá certo se continuar útil depois que a estudante sai, o que depende de simplicidade, documentação e um mantenedor nomeado. A seção sobre como acrescentar uma nova verificação é a que mais importa, porque as necessidades da Riverton vão mudar depois que ela sair. O registro de mudanças mostra o que mudou entre as versões e por quê.

### Exemplo resolvido

Priya constrói um resumo semanal de governança, testa-o com problemas conhecidos e com usuários, acrescenta um filtro por clínica e as datas das fontes e documenta a manutenção.

> **Caso sintético.** A ferramenta e os dados são sintéticos.

### Erros e limites

Os painéis podem ser ignorados. A qualidade dos dados de origem limita o valor.

### Exercícios

- **EX085 — Destaques.** O que o resumo semanal destaca? *Rubrica:* 3 = ações atrasadas, evidências vencidas, violações de limiares, controles que falharam;; 2 = quatro;; 1 = vago;; 0 = nenhuma.
- **EX086 — Datas das fontes.** Por que Priya acrescentou a data da última atualização de cada fonte? *Rubrica:* 3 = uma ação resolvida aparecia porque uma fonte estava desatualizada;; 2 = atualidade;; 1 = vago;; 0 = nenhuma.
- **EX087 — Valor duradouro.** De que depende o valor duradouro? *Rubrica:* 3 = simplicidade, documentação e um mantenedor nomeado;; 2 = manutenibilidade;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma ferramenta de projeto final precisa ser testada com usuários e documentada para que outras pessoas possam mantê-la.

<a id="ch-30"></a>

## Capítulo 30 — Avaliação do projeto final

### Objetivos de aprendizagem

Você vai (1) apresentar um projeto final aos avaliadores; (2) avaliá-lo contra critérios; (3) refletir sobre seu desenvolvimento como tecnólogo.

### 30.1 Apresentação

Priya apresenta seu projeto final ao Sr. Lind e ao gerente de operações da Riverton. Explica o problema, o desenho, os testes, o retorno dos usuários e a documentação, e depois demonstra um resumo semanal. Os avaliadores perguntam como a ferramenta lida com arquivos ausentes; ela mostra que a ferramenta relata as fontes ausentes com clareza, em vez de omiti-las em silêncio. Também perguntam como ela protegeu os dados dos pacientes; ela explica que a ferramenta lê apenas registros de governança, e não prontuários. O Sr. Lind acrescenta que ler apenas registros de governança também mantém a ferramenta fora do escopo das regras de tratamento de dados de pacientes.

### 30.2 Avaliação

Os avaliadores julgam pelos critérios acordados no início: utilidade para a Riverton, correção, manutenibilidade, documentação e conduta profissional. O gerente de operações relata que o resumo substituiu a pauta de uma reunião semanal e que as ações atrasadas diminuíram depois de sua introdução, embora outras mudanças também tenham contribuído. Priya recebe notas altas, com a sugestão de acrescentar gráficos simples de tendência numa versão futura. A ressalva do gerente de que outras mudanças também contribuíram é o mesmo limite de atribuição que Priya declarou em seu próprio estudo.

### 30.3 Reflexão

Priya reflete sobre os três anos. Aprendeu a ver a GRC como trabalho prático: conhecer os ativos, mapear os dados, estimar os riscos, documentar os controles, acompanhar os indicadores e corrigir as causas-raiz. Também aprendeu que são as pessoas que fazem a governança funcionar e que a comunicação clara e respeitosa importa tanto quanto as ferramentas. O Sr. Lind observa que o hábito dela de conferir as evidências antes de declarar sucesso vai lhe servir bem em qualquer função. A recusa em marcar como concluída uma revisão de acesso durante o estágio é um exemplo desse hábito na prática.

### Exemplo resolvido

Priya apresenta e demonstra seu projeto final, é avaliada em cinco critérios e reflete sobre seu desenvolvimento.

> **Caso sintético.** A avaliação é sintética.

### Erros e limites

As avaliações amostram competências. As melhorias relatadas têm várias causas.

### Exercícios

- **EX088 — Arquivos ausentes.** Como a ferramenta lida com arquivos de origem ausentes? *Rubrica:* 3 = relata-os com clareza;; 2 = explícita;; 1 = em silêncio;; 0 = nenhuma.
- **EX089 — Dados de pacientes.** A ferramenta lê prontuários? *Rubrica:* 3 = não, apenas registros de governança;; 2 = não;; 1 = sim;; 0 = nenhuma.
- **EX090 — Sugestão futura.** O que os avaliadores sugeriram para uma versão futura? *Rubrica:* 3 = gráficos simples de tendência;; 2 = gráficos;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma avaliação de projeto final confirma o valor prático e reflete sobre o crescimento como tecnólogo de GRC.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX090. Priya Natarajan, o Sr. Oskar Lind, o Halden Institute of Technology, o Riverton Dental Group e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX037.** Uma causa, um evento e consequências.

**EX038.** Os controles preventivos.

**EX039.** Porque o esforço de análise deve ir para os cenários que mais importam.

**EX040.** Ransomware numa clínica, a 27 mil.

**EX041.** 55 mil.

**EX042.** Prontuários enviados ao destinatário errado, a 8 mil por ano.

**EX043.** Cada participante deu sua opinião antes da discussão.

**EX044.** Concluir a segmentação de rede e testar os backups offline.

**EX045.** Porque acordá-los na própria reunião aumenta o comprometimento.

**EX046.** Passando o pagamento com cartão para uma página hospedada pelo seu provedor de pagamentos.

**EX047.** Para que os gestores vejam o que cada tratamento consegue e se o risco restante está dentro do apetite.

**EX048.** O risco residual dos notebooks perdidos.

**EX049.** South.

**EX050.** Revisão de acesso na North, bloqueio de tela na East, revisão de acesso na East e backup na West.

**EX051.** Porque os gerentes das clínicas não receberam as listas de contas a tempo.

**EX052.** O líder de TI restaura cinco arquivos de amostra do arquivo de imagens e registra um resultado de teste datado.

**EX053.** Porque sua falha afeta o cumprimento de várias obrigações ao mesmo tempo.

**EX054.** Porque a Riverton não desenvolve software, embora os controles de fornecedores cubram seus provedores.

**EX055.** Dez.

**EX056.** Junho (12) e julho (14).

**EX057.** Duas violações seguidas são escaladas para o gerente de operações.

**EX058.** Problemas de desenho, de operação e de evidência.

**EX059.** Porque desbloquear repetidamente atrasava o check-in dos pacientes.

**EX060.** O testador verificou um computador reserva não gerenciado, registrando uma falsa falha.

**EX061.** Como chamados com data de expiração.

**EX062.** Atualiza a probabilidade do risco de e-mail enviado ao destinatário errado.

**EX063.** Porque é mais confiável e menos trabalhosa do que a evidência montada pouco antes de uma auditoria.

**EX064.** b.osei e d.wu.

**EX065.** f.temp era a conta de um substituto nunca removida; g.test foi deixada pelo provedor após a implantação.

**EX066.** Porque um desligado pode ter voltado ou um fornecedor pode ter um motivo válido, então uma pessoa precisa conferir.

**EX067.** O registro, os resultados dos testes, as tendências dos indicadores, o registro de evidências e uma pesquisa com os gerentes.

**EX068.** Doze de catorze.

**EX069.** A revisão de acesso.

**EX070.** Pelo número de direitos inadequados encontrados por uma segunda verificação.

**EX071.** Por sorteio de nomes, sete para cada grupo.

**EX072.** Quarenta minutos com as listas novas e noventa com as antigas.

**EX073.** Um checklist de configuração segura, os controles de que o gerente da clínica é dono, os requisitos de evidência e uma sessão curta de treinamento.

**EX074.** Dois termos usados de forma inconsistente.

**EX075.** Uma versão do checklist em uma página.

**EX076.** Uma pessoa que nunca fez a tarefa.

**EX077.** A revisão mensal dos indicadores, especificamente o que conta como escalonamento.

**EX078.** Um mês.

**EX079.** Um aparelho de imagem estava ligado ao segmento da recepção.

**EX080.** O relatório de validação.

**EX081.** Porque corrigir problemas antes de entrar em operação é muito mais barato do que depois que os pacientes chegam.

**EX082.** Acompanhamento constante, como cobrar ações e conferir evidências.

**EX083.** Por causa da página de pagamento hospedada e das maquininhas segmentadas.

**EX084.** Recusou com educação e ajudou a gerente a concluir a revisão naquela tarde.

**EX085.** Ações atrasadas, evidências vencidas, violações de limiares e controles que falharam, cada um com seu dono.

**EX086.** Porque uma ação resolvida ainda aparecia quando seu arquivo de origem não tinha sido atualizado.

**EX087.** Simplicidade, documentação e um mantenedor nomeado.

**EX088.** Relata as fontes ausentes com clareza, em vez de omiti-las em silêncio.

**EX089.** Não; lê apenas registros de governança.

**EX090.** Acrescentar gráficos simples de tendência.

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
