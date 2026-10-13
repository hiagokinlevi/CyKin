# Segurança de TO, IoT e Sistemas Ciberfísicos: Caderno de Trabalho do Operador Técnico

- Idioma: português do Brasil (`pt`); curso técnico, dezoito meses; aproximadamente 1.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–18 de 18 têm texto didático escrito à mão; os exercícios EX001–EX072 têm resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, e suas saídas vêm de execuções reais. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: operadores técnicos e técnicos de manutenção que trabalham em linhas industriais ou ao lado delas e precisam reconhecer e relatar problemas de segurança e ajudar na recuperação.
- Relação com os livros vizinhos: o [livro do curso profissional](../../../../professional-6-months/ot-iot-security/en/book/MANUSCRIPT.md) é mais curto; o [livro de tecnólogo](../../../../technologist-3-years/ot-iot-security/en/book/MANUSCRIPT.md) acrescenta implementação e projeto. **Este livro é procedimental e voltado para o chão de fábrica.**
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação credenciada. Não concede autorização para acessar instalações reais. Todas as instalações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–4 explicam a linha, a segurança física, as redes e os protocolos; os capítulos 5–13 cobrem os controles do dia a dia (registro de ativos, contas, mídias, acesso de fornecedores, registros, alertas, cópias de segurança, segmentação, IoT); os capítulos 14–17 cobrem perceber, relatar, recuperar e controlar mudanças; o capítulo 18 é a vistoria final. Todo capítulo tem objetivos, texto didático, um exemplo resolvido, um caso sintético identificado, erros e limites, quatro exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios dos Capítulos 5, 9 e 11 leem apenas dados locais (`python3 file.py`).

### Caso sintético contínuo

| Elemento | Papel | Limite |
|---|---|---|
| **Harbor Point Food Packaging Line (HPFL)** — CLP da enchedora PLC-FILL, CLP da embaladora PLC-WRAP, painel HMI-1, câmera de visão VIS-CAM, notebook de engenharia ENG-LT, firewall FW-1 | Linha estudada ao longo do livro | Inventada |
| **Tomás Reyes** | Técnico de manutenção na HPFL | Inventado |

### Fontes centrais

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [série ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Lista completa nas [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — O que é a tecnologia operacional numa linha de embalagem

### Objetivos de aprendizagem

Você vai (1) nomear os principais componentes de TO numa linha de embalagem de alimentos; (2) explicar por que as prioridades de TO diferem das da TI de escritório; e (3) descrever o que pode dar errado fisicamente quando um sistema de controle se comporta mal.

### 1.1 A linha como sistema

Uma linha de embalagem transforma filme, bandejas e produto em embalagens seladas e rotuladas. Os controladores lógicos programáveis (CLPs) leem sensores e acionam motores, aquecedores e válvulas muitas vezes por segundo. Os painéis de operação, chamados interfaces homem-máquina (IHMs), mostram o estado da linha e permitem que os operadores a liguem, parem e ajustem. Uma câmera de visão rejeita as embalagens mal seladas. Um notebook de engenharia guarda os programas e é usado para alterá-los. A NIST SP 800-82r3 chama toda essa família de tecnologia operacional: sistemas que monitoram ou controlam processos físicos.

### 1.2 Por que as prioridades diferem

Num escritório, perder a confidencialidade de uma planilha é o dano clássico. Numa linha, as primeiras perguntas são: alguém pode se ferir, o alimento ficará inseguro, a linha vai parar? Um aquecedor de selagem que esquenta demais pode queimar um trabalhador ou deixar embalagens sem selagem e contaminadas. É por isso que, aqui, a disponibilidade e o comportamento seguro vêm antes da confidencialidade, e é por isso que você nunca "simplesmente reinicia" um controlador para ver o que acontece.

Na HPFL, essa ordem molda as pequenas decisões. Tomás não desliga a HMI-1 porque ela parece estranha; primeiro pergunta ao supervisor se é seguro parar a linha. Uma correção que protege dados, mas deixa o aquecedor de selagem sem controle, seria a correção errada, por mais sensata que pareça num escritório.

### 1.3 O que um atacante ou um erro pode mudar

As mesmas mudanças vêm de má-fé ou de erro: um setpoint alterado, um programa substituído, uma IHM bloqueada, uma rede inundada. O MITRE ATT&CK for ICS lista, por exemplo, a T0836 Modify Parameter. O seu trabalho como técnico é perceber essas mudanças, relatá-las e ajudar a restaurar com segurança — não investigar dispositivos por conta própria.

Como a mesma mudança pode vir de qualquer uma das fontes, Tomás registra o que mudou, quando e em qual dispositivo, sem decidir o porquê. Na HPFL, uma velocidade da embaladora alterada pode ser um operador desafogando um acúmulo ou alguém usando indevidamente uma senha; o Capítulo 9 mostra um caso em que foi a primeira hipótese. O relato é igualmente útil nos dois casos.

### Exemplo resolvido (HPFL sintética)

No seu primeiro turno, Tomás Reyes percorre a linha com o supervisor e a desenha: enchedora PLC-FILL, embaladora PLC-WRAP, painel HMI-1, câmera de visão VIS-CAM, notebook de engenharia ENG-LT. Ao lado de cada caixa, escreve uma frase sobre o que acontece fisicamente se aquele item falhar. A frase da embaladora diz: "o filme para, as embalagens se acumulam, risco de enrosco na alimentação."

> **Caso sintético — Harbor Point Food Packaging Line (HPFL).** A planta, Tomás Reyes e todos os números deste livro são inventados para fins didáticos.

### Erros e limites

Um desenho feito numa única volta é incompleto; painéis de reserva e dispositivos sem fio passam despercebidos com facilidade. As consequências são avaliadas com a equipe de operações, não sozinho.

### Exercícios

- **EX001 — Nomear as partes.** Liste quatro componentes de TO da linha da HPFL e a função de cada um. *Rubrica:* 3 = quatro componentes, cada um com a função correta; 2 = três; 1 = só os nomes; 0 = nenhum.
- **EX002 — Escritório versus linha.** Explique em duas frases por que "reinicia e vê" é aceitável para um PC de escritório, mas não para o PLC-WRAP. *Rubrica:* 3 = consequência física mais argumento de estado seguro/produção; 2 = uma razão; 1 = vago; 0 = nenhum.
- **EX003 — Consequência do aquecedor.** Descreva dois danos se o setpoint do aquecedor de selagem for elevado muito acima do normal. *Rubrica:* 3 = risco de queimadura/incêndio e embalagens inseguras ou rejeitadas; 2 = um; 1 = "quebra"; 0 = nenhum.
- **EX004 — Uma técnica do ATT&CK.** Qual técnica do ATT&CK for ICS descreve um setpoint alterado, e a mesma mudança poderia ser acidental? *Rubrica:* 3 = T0836 Modify Parameter e sim, por erro; 2 = só a técnica; 1 = ID errado; 0 = nenhum.

### Síntese

A segurança de TO numa linha começa pela consequência física: pessoas, alimentos e produção vêm primeiro.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 18

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Segurança em primeiro lugar: permissões de trabalho, consequências e quem decide

### Objetivos de aprendizagem

Você vai (1) explicar como as permissões de trabalho e o bloqueio protegem as pessoas; (2) declarar quem tem autoridade para parar ou alterar a linha; e (3) aplicar a regra de que o trabalho de segurança cibernética nunca contorna os controles de segurança física.

### 2.1 Sistemas de segurança física não são ferramentas de segurança cibernética

Cortinas de luz, paradas de emergência e intertravamentos de proteções mantêm as mãos longe das partes em movimento. Eles são projetados e verificados por engenheiros de segurança e precisam continuar funcionando aconteça o que acontecer com a rede. Um técnico de segurança cibernética nunca os desativa, faz jumper ou reconfigura, nem mesmo "temporariamente, para testar".

Na HPFL, isso abrange as cortinas de luz na alimentação da embaladora, as paradas de emergência ao longo da linha e os intertravamentos das portas de proteção. Se uma tarefa de segurança cibernética parecer exigir a alteração de um deles, a tarefa está errada, não o dispositivo de segurança. Pare, pergunte ao supervisor e registre a pergunta.

### 2.2 Permissões de trabalho e bloqueio

O trabalho numa planta em funcionamento exige uma permissão: um registro escrito de quem faz o quê, onde, quando, quais perigos existem e como são controlados. O bloqueio e etiquetagem (lockout/tagout) isola as fontes de energia antes de as mãos entrarem numa máquina. Conectar um notebook ao switch da embaladora também é trabalho na planta: isso pode alterar o tráfego que o CLP vê, então passa pelo mesmo processo de permissão.

A permissão nomeia o responsável, a janela de tempo e o que será tocado. Na HPFL, a permissão de Tomás para fotografar o armário da embaladora dizia que nenhuma ferramenta entraria e que nenhuma conexão seria feita. Pôr isso por escrito protege tanto ele quanto a linha, porque todos sabem o que a tarefa incluía e o que não incluía.

### 2.3 Quem decide

O supervisor de turno decide se a linha funciona. O engenheiro de controle é o dono dos programas dos CLPs. O gerente de qualidade decide se o produto é seguro para expedição. A equipe de segurança cibernética aconselha e relata; não toma essas decisões sozinha. Conhecer essa cadeia poupa tempo num incidente, porque você liga primeiro para a pessoa certa.

Na HPFL, isso significa que uma preocupação de qualidade vai para o gerente de qualidade, uma pergunta sobre a lógica de um CLP para o engenheiro de controle e qualquer coisa sobre parar a linha para o supervisor de turno. Mantenha os nomes e telefones deles na ficha da instalação. Na dúvida sobre quem decide, pergunte primeiro ao supervisor; ele saberá quem mais envolver.

### 2.4 Condições de parada

Toda tarefa tem condições de parada escritas: por exemplo, parar se aparecer qualquer alarme não explicado, se um operador pedir que você pare ou se um dispositivo se comportar de forma diferente do planejado. Parar nunca é um fracasso.

Escreva as condições de parada na permissão antes de começar e combine-as com o supervisor. Quando uma delas ocorrer, pare o trabalho, deixe a área segura, avise o supervisor e registre o que aconteceu. Uma tarefa pode ser retomada depois, sob uma permissão nova ou alterada. Insistir porque o trabalho está quase terminado é como pequenas surpresas viram incidentes.

### Exemplo resolvido (HPFL sintética)

Tomás precisa fotografar as etiquetas do armário da embaladora para o inventário. Ele pede ao supervisor, que emite uma permissão para 10:00–10:20, durante uma troca de filme planejada, anota "porta do armário aberta, nenhuma ferramenta dentro, nenhuma conexão" e nomeia o eletricista que abre o painel. Tomás fotografa, o eletricista fecha a porta e a permissão é encerrada com assinatura.

> **Caso sintético — HPFL.** A permissão e os horários são inventados.

### Erros e limites

Os formulários de permissão variam de uma instalação para outra; siga o local. Uma permissão não torna segura uma tarefa insegura; ela só registra que os perigos foram considerados.

### Exercícios

- **EX005 — Pedido sobre a cortina de luz.** Um colega sugere fazer um jumper na cortina de luz da embaladora enquanto testa o tráfego de rede. O que você faz? *Rubrica:* 3 = recusar, sistemas de segurança intocados, escalar ao supervisor/engenheiro de segurança; 2 = só recusar; 1 = pedir permissão para o jumper; 0 = concordar.
- **EX006 — Por que um notebook precisa de permissão.** Dê uma razão técnica pela qual conectar o ENG-LT ao switch da linha exige permissão. *Rubrica:* 3 = pode alterar o tráfego/broadcasts vistos pelos CLPs ou enviar mudanças, afetando o processo; 2 = risco genérico; 1 = "as regras mandam"; 0 = nenhum.
- **EX007 — Associar decisões a pessoas.** Quem decide (a) se a linha funciona, (b) se um programa de CLP muda, (c) se o produto é expedido? *Rubrica:* 3 = supervisor, engenheiro de controle, gerente de qualidade; 2 = dois certos; 1 = um; 0 = nenhum.
- **EX008 — Escrever condições de parada.** Escreva três condições de parada para fotografar as etiquetas do armário. *Rubrica:* 3 = três condições específicas e observáveis; 2 = duas; 1 = vagas; 0 = nenhum.

### Síntese

Os controles de segurança física são intocáveis, as permissões registram o trabalho e pessoas nomeadas tomam as decisões operacionais.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 18

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Noções básicas de rede na linha

### Objetivos de aprendizagem

Você vai (1) ler um endereço IP e uma máscara de sub-rede; (2) explicar o que switches, VLANs e firewalls fazem numa rede de planta; e (3) esboçar a rede da HPFL a partir de uma descrição.

### 3.1 Endereços e sub-redes

Todo dispositivo em rede tem um endereço IP, como 10.20.1.11. Uma máscara /24 significa que os três primeiros números nomeiam a rede e o último nomeia o dispositivo, então 10.20.1.11 e 10.20.1.12 são vizinhos em 10.20.1.0/24. Os dispositivos da mesma sub-rede conseguem conversar diretamente; o tráfego para outra sub-rede passa por um roteador ou firewall.

Na HPFL, os dispositivos da linha compartilham 10.20.1.0/24, então PLC-FILL, PLC-WRAP, HMI-1 e VIS-CAM conseguem alcançar uns aos outros diretamente. Os escritórios ficam em 10.10.0.0/16, e o tráfego entre as duas redes precisa passar pelo FW-1. Saber disso diz a Tomás que é uma regra de firewall que decide se um PC de escritório consegue chegar a um CLP.

### 3.2 Switches e VLANs

Um switch conecta dispositivos com cabos. Uma VLAN divide um switch físico em redes lógicas separadas, de modo que os dispositivos da linha e os PCs de escritório possam compartilhar o hardware sem compartilhar o tráfego. Um erro numa configuração de VLAN pode conectar silenciosamente duas redes que deveriam ficar separadas, e é por isso que as mudanças em switches exigem o mesmo cuidado que as mudanças em CLPs.

Na HPFL, a linha está na VLAN 20 e os escritórios na VLAN 10. Se uma porta de um switch compartilhado fosse configurada com a VLAN errada, um PC de escritório conectado a ela cairia na rede da linha sem passar pelo FW-1. Relate qualquer dúvida sobre a VLAN de uma porta ao dono da rede, em vez de testá-la.

### 3.3 Firewalls

Um firewall encaminha ou bloqueia o tráfego entre redes de acordo com regras: origem, destino, porta e ação. Numa planta, o firewall importante fica entre a rede de escritório e a linha. Boas regras nomeiam hosts e portas específicos; regras "qualquer para qualquer" anulam o propósito.

Na HPFL, o FW-1 deve permitir que o ENG-LT alcance os CLPs e pouco mais. Cada regra deve ter um comentário dizendo por que existe e quem é o dono. O Capítulo 12 mostra como ler a tabela do FW-1 e o que fazer com uma regra sem dono.

### 3.4 Switches não gerenciáveis e redes sem fio

Pequenos switches não gerenciáveis dentro de armários e pontes sem fio são comuns e muitas vezes não aparecem nos desenhos. Eles importam porque criam conexões que ninguém revisa.

Procure-os durante as vistorias: um pequeno switch dentro de um armário com mais cabos do que o esperado, ou uma ponte sem fio num mastro. Fotografe o que encontrar e relate com a localização. Um dispositivo que liga a rede da linha a outra rede sem passar pelo FW-1 torna as regras do firewall irrelevantes para esse caminho. Pergunte ao dono da rede se cada um é conhecido e aprovado.

### 3.5 Endereços que você não deve presumir

Os dispositivos podem ter uma segunda placa de rede, uma porta serial ou um modem celular que não aparecem no desenho. Pergunte ao dono por todas as interfaces, não só pelo endereço principal.

Registre cada interface no registro de ativos, não só o endereço IP principal. Um modem celular acrescentado por um fabricante de máquinas para suporte remoto é um exemplo comum, e ele pode contornar totalmente o FW-1. Se o dono não souber se um dispositivo tem outras interfaces, consulte o manual ou pergunte ao fornecedor antes de presumir que não tem.

### Exemplo resolvido (HPFL sintética)

O engenheiro de controle diz a Tomás: os dispositivos da linha usam 10.20.1.0/24 na VLAN 20, os escritórios usam 10.10.0.0/16 na VLAN 10, um firewall FW-1 os une e apenas o ENG-LT pode alcançar os CLPs. Tomás desenha duas caixas, coloca PLC-FILL (10.20.1.11), PLC-WRAP (10.20.1.12), HMI-1 (10.20.1.21) e VIS-CAM (10.20.1.31) na caixa da linha e escreve no FW-1 a única regra permitida.

> **Caso sintético — HPFL.** Os endereços e os números de VLAN são inventados.

### Erros e limites

Um desenho descreve a intenção; o cabeamento real pode ser diferente. Confirme contra a configuração dos switches com o dono da rede, nunca sondando os dispositivos.

### Exercícios

- **EX009 — Mesma sub-rede?** 10.20.1.31 e 10.20.2.31 estão na mesma rede /24? Explique. *Rubrica:* 3 = não, o terceiro octeto difere, então são /24 diferentes; 2 = não, sem razão; 1 = sim; 0 = nenhum.
- **EX010 — Erro de VLAN.** O que poderia acontecer se a porta de uma impressora de escritório fosse configurada por engano na VLAN 20? *Rubrica:* 3 = a impressora entra na rede da linha, contornando o FW-1, criando um caminho não revisado; 2 = só "rede errada"; 1 = a impressora para; 0 = nenhum.
- **EX011 — Qualidade da regra.** Reescreva "any → 10.20.1.0/24 any allow" como uma regra que corresponda à intenção da HPFL. *Rubrica:* 3 = origem só o endereço do ENG-LT, destino os CLPs, a porta necessária, allow, mais negação padrão; 2 = específica por host, sem negação; 1 = ainda ampla; 0 = nenhum.
- **EX012 — O switch escondido.** Por que um switch não gerenciável encontrado no armário da embaladora importa para a segurança? *Rubrica:* 3 = ponto de conexão não revisado, sem registros/controle de VLAN, pode estender a rede; 2 = um ponto; 1 = "é velho"; 0 = nenhum.

### Síntese

Endereços, VLANs e regras de firewall decidem quem consegue conversar com um controlador; erros neles abrem caminhos em silêncio.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 18

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Protocolos industriais no nível do operador

### Objetivos de aprendizagem

Você vai (1) descrever o que o Modbus/TCP e protocolos industriais semelhantes transportam; (2) explicar por que muitos não têm autenticação; e (3) reconhecer, a partir de uma descrição, o uso normal e o uso incomum de um protocolo.

### 4.1 O que os protocolos transportam

As IHMs e os CLPs trocam valores: temperaturas, velocidades, contagens, bits de partida e parada. O Modbus, publicado pela Modbus Organization, é um exemplo muito usado; sobre Ethernet, ele se chama Modbus/TCP e normalmente usa a porta 502. Uma requisição diz "ler os registradores 100–110" ou "escrever o valor 180 no registrador 205". Outras famílias comuns incluem EtherNet/IP e PROFINET; a ideia é parecida.

Na HPFL, a HMI-1 lê do PLC-FILL e do PLC-WRAP valores como velocidades e temperaturas e envia escritas quando os operadores apertam botões. O ENG-LT usa uma conexão de programação separada para alterar a lógica dos CLPs. Saber quais conexões são esperadas é o que permite a qualquer pessoa perceber uma inesperada.

### 4.2 Por que falta autenticação

O Modbus clássico não tem nenhuma forma embutida de verificar quem envia uma requisição. Se um dispositivo consegue alcançar o CLP na porta 502, normalmente consegue ler e, muitas vezes, escrever. Isso era aceitável quando a rede era um cabo fechado dentro de um armário. Não é aceitável quando essa rede se conecta aos escritórios ou à internet, e é por isso que a segmentação (Capítulo 12) tem tanto peso.

Na HPFL, isso significa que o firewall e as VLANs são a principal proteção do PLC-FILL e do PLC-WRAP. Se um PC de escritório conseguisse alcançar a porta 502 de qualquer um dos CLPs, poderia enviar escritas idênticas às da HMI-1. Relate imediatamente qualquer sinal de um caminho assim, sem testá-lo.

### 4.3 Padrões normais

Numa linha saudável, o padrão é monótono: a HMI-1 lê os mesmos registradores a cada segundo, e as escritas acontecem quando os operadores apertam botões. Um dispositivo novo enviando escritas, ou leituras de faixas de registradores incomuns, merece ser relatado. Você não precisa decodificar pacotes; precisa saber como é o normal e para quem ligar.

Pôr o padrão normal por escrito também ajuda depois de mudanças. Se um novo dispositivo for acrescentado à linha, o padrão esperado é atualizado no mesmo chamado de mudança. Uma ferramenta de monitoramento operada pelo dono da rede pode então comparar o tráfego real com o padrão escrito, como na anotação do caderno de Tomás.

### 4.4 Não faça experimentos

Enviar requisições de teste a um CLP em funcionamento pode alterar as saídas. O aprendizado de protocolos acontece num simulador ou num CLP de laboratório, nunca na linha.

O engenheiro de controle pode reservar tempo num CLP de laboratório ou num simulador se você quiser praticar. Mesmo as requisições de leitura a um controlador em funcionamento acrescentam carga e podem perturbar dispositivos mais antigos. Se tiver curiosidade sobre o que um registrador contém, pergunte ao engenheiro em vez de consultar o CLP na linha. Aprender num CLP de laboratório permite errar com segurança e ver os efeitos dos erros sem risco.

### Exemplo resolvido (HPFL sintética)

O engenheiro de controle mostra a Tomás um resumo da ferramenta de monitoramento da linha: a HMI-1 lê o PLC-WRAP a cada segundo; o ENG-LT se conectou duas vezes no mês passado, durante mudanças aprovadas. Tomás anota no caderno "escritas só da HMI-1 e do ENG-LT" como o padrão esperado.

> **Caso sintético — HPFL.** O resumo do monitoramento é inventado.

### Erros e limites

Algumas versões mais novas dos protocolos acrescentam recursos de segurança, mas as plantas usam dispositivos antigos por décadas; presuma o caso comum mais fraco, a menos que o dono confirme o contrário.

### Exercícios

- **EX013 — Uma requisição de escrita.** Em palavras simples, o que "escrever 180 no registrador 205" faz no PLC-WRAP, se o registrador 205 for a velocidade da embaladora? *Rubrica:* 3 = ajusta a velocidade para 180, mudança física imediata; 2 = muda um valor; 1 = lê; 0 = nenhum.
- **EX014 — Porta 502 alcançável.** Um tablet de fornecedor na VLAN da linha consegue alcançar a porta 502 do PLC-FILL. Por que isso preocupa? *Rubrica:* 3 = sem autenticação, o tablet pode ler/escrever valores do processo; 2 = "acesso não autorizado"; 1 = rede lenta; 0 = nenhum.
- **EX015 — Encontre o incomum.** Qual é incomum: (a) a HMI-1 lendo a cada segundo, (b) a VIS-CAM escrevendo no PLC-WRAP, (c) o ENG-LT durante uma mudança aprovada? *Rubrica:* 3 = (b), com razão; 2 = só (b); 1 = outro; 0 = nenhum.
- **EX016 — Aprender com segurança.** Onde Tomás deve praticar o envio de requisições Modbus, e por que não na linha? *Rubrica:* 3 = simulador/CLP de laboratório; as requisições alteram saídas reais; 2 = só o lugar; 1 = "na linha, fora do expediente"; 0 = nenhum.

### Síntese

Os protocolos industriais movem valores do processo com pouca ou nenhuma autenticação, então alcançar um dispositivo equivale a controlá-lo.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 18

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Manter um registro de ativos

### Objetivos de aprendizagem

Você vai (1) listar os campos de que um registro de ativos de TO útil precisa; (2) encontrar lacunas num registro com um pequeno script; e (3) explicar por que um registro incompleto atrasa a resposta a incidentes.

### 5.1 O que registrar

Para cada dispositivo: identificador, localização, zona ou VLAN, responsável, fabricante e modelo, versão de firmware, endereço de rede e o que ele controla. A NIST SP 800-82r3 trata o inventário como um alicerce, porque toda atividade posterior — correções, monitoramento, resposta a incidentes — depende de saber o que existe.

Na HPFL, o registro cobre PLC-FILL, PLC-WRAP, HMI-1, VIS-CAM e ENG-LT e, mais tarde, os sensores IoT. Cada campo responde a uma pergunta que alguém fará com pressa: para quem ligar, qual firmware, qual endereço. Um campo faltando é uma constatação a corrigir, não um espaço em branco a tolerar.

### 5.2 De onde vêm os dados

Registros de compra, desenhos de empreiteiros, etiquetas dos armários, o projeto do software de engenharia e, a cargo do dono da rede, o monitoramento passivo da rede. Cada fonte deixa algo de fora, então elas são comparadas.

```python
"""Lab 5: check a synthetic HPFL asset register for missing owner or firmware fields (no scanning)."""
reg = [
    {"id": "PLC-FILL", "zone": "line", "owner": "maintenance", "fw": "3.2"},
    {"id": "PLC-WRAP", "zone": "line", "owner": "maintenance", "fw": ""},
    {"id": "HMI-1", "zone": "line", "owner": "", "fw": "n/a"},
    {"id": "VIS-CAM", "zone": "line", "owner": "quality", "fw": "1.0.7"},
    {"id": "ENG-LT", "zone": "office", "owner": "controls", "fw": "n/a"},
]
for r in reg:
    gaps = [k for k in ("owner", "fw") if not r[k]]
    print(f"{r['id']:9} zone={r['zone']:7} {'OK' if not gaps else 'MISSING ' + ','.join(gaps)}")
print("complete:", sum(1 for r in reg if r["owner"] and r["fw"]), "of", len(reg))
```

Execute com `python3 lab_assets.py`. Saída verificada:

```text
PLC-FILL  zone=line    OK
PLC-WRAP  zone=line    MISSING fw
HMI-1     zone=line    MISSING owner
VIS-CAM   zone=line    OK
ENG-LT    zone=office  OK
complete: 3 of 5
```

Na HPFL, Tomás usou fotografias das etiquetas dos armários para preencher a versão de firmware que faltava no PLC-WRAP. Quando duas fontes discordam, registre as duas e pergunte ao responsável qual está certa. Nunca preencha lacunas sondando dispositivos na linha; o monitoramento é feito apenas pelo dono da rede, de forma passiva.

### 5.3 Lendo o resultado

O script imprime quais registros estão incompletos. O PLC-WRAP não tem firmware registrado, então ninguém consegue dizer se um novo alerta se aplica a ele. A HMI-1 não tem responsável, então ninguém seria chamado se ela se comportasse mal. Três de cinco registros estão completos; essa proporção é uma medida simples para acompanhar todo mês.

A correção de cada lacuna é uma pergunta à pessoa certa. O firmware pode vir de uma etiqueta do armário ou do software do engenheiro de controle; a responsabilidade vem do supervisor. Executar o script de novo depois de cada resposta mostra o progresso, como a nova execução de Tomás mostrou quando os cinco registros ficaram completos.

### 5.4 Mantê-lo vivo

Um registro só é útil se for atualizado quando as coisas mudam. Vincule as atualizações aos chamados de mudança: nenhum dispositivo é instalado, movido ou substituído sem que o registro mude no mesmo chamado.

Acrescente uma verificação do registro ao modelo de chamado de mudança, para que ela não possa ser pulada. Uma vez por mês, compare o registro com o que o monitoramento do dono da rede vê e com uma vistoria dos armários. Todo dispositivo visto, mas não registrado, é relatado e acrescentado, ou removido se ninguém conseguir explicá-lo.

### 5.5 Reservas e dispositivos desativados

CLPs de reserva numa prateleira e dispositivos retirados de serviço também pertencem ao registro, marcados como reserva ou desativados. Uma reserva carregada com um programa antigo pode ser instalada às pressas durante uma pane, e uma IHM desativada jogada numa caçamba ainda pode guardar senhas e configurações de rede.

Antes de instalar uma reserva, verifique se o seu programa corresponde à cópia de segurança verificada do dispositivo que ela substitui. Antes que um dispositivo desativado saia da instalação, apague-o seguindo as instruções do fornecedor e registre que isso foi feito. Os dois passos pertencem à entrada daquele dispositivo no registro.

### Exemplo resolvido (HPFL sintética)

Tomás usa as fotografias do armário do Capítulo 2 para ler a etiqueta de firmware do PLC-WRAP: 2.0. Ele pergunta ao supervisor quem é o responsável pela HMI-1; a resposta é "operações", e ele a registra. Uma nova execução do script agora mostra cinco de cinco completos.

> **Caso sintético — HPFL.** O registro e as etiquetas são inventados.

### Erros e limites

As etiquetas podem estar desatualizadas depois de uma atualização de firmware; confirme pelo software de engenharia, com o engenheiro de controle. Um registro é sensível: também é um mapa para atacantes, então guarde-o com controle de acesso.

### Exercícios

- **EX017 — Campos faltantes.** Nomeie dois campos que faltavam, ou poderiam faltar, no PLC-WRAP e que importam durante um alerta. *Rubrica:* 3 = versão de firmware e modelo/fabricante; 2 = um; 1 = cor ou algo sem relação; 0 = nenhum.
- **EX018 — Proporção depois das correções.** Se o responsável pela HMI-1 for preenchido, mas o firmware do PLC-WRAP continuar em branco, o que a última linha imprime? *Rubrica:* 3 = "complete: 4 of 5"; 2 = 4 sem o formato; 1 = 5; 0 = nenhum.
- **EX019 — Vincular à mudança.** Proponha uma regra que mantenha o registro atualizado. *Rubrica:* 3 = todo chamado de instalação/movimentação/substituição precisa atualizar o registro antes do encerramento; 2 = só revisão periódica; 1 = "ter cuidado"; 0 = nenhum.
- **EX020 — Proteger o registro.** Dê uma razão pela qual o registro não deve ficar numa pasta pública. *Rubrica:* 3 = revela endereços, versões e alvos aos atacantes; 2 = "confidencial"; 1 = é grande; 0 = nenhum.

### Síntese

Um registro completo, atual e protegido é a base sobre a qual se apoia toda outra tarefa de segurança de TO.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 18

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Contas e senhas em IHMs e ferramentas de engenharia

### Objetivos de aprendizagem

Você vai (1) explicar os riscos das contas compartilhadas e padrão; (2) aplicar práticas simples de contas que funcionam no chão de fábrica, em regime de turnos; e (3) lidar corretamente com uma senha esquecida ou vazada.

### 6.1 Contas compartilhadas

Muitas IHMs vêm com uma única conta "operator" usada por todos os turnos. Aí os registros dizem "operator fez isso" e ninguém sabe quem foi. Onde o sistema permitir, dê a cada pessoa a sua própria conta; onde não permitir, registre quem estava no turno e mantenha a senha compartilhada conhecida apenas pela equipe.

Na HPFL, a conta de administrador da HMI-1 era usada pelos operadores para mudar a velocidade da embaladora, como mostra o Capítulo 9, o que tornou a mudança difícil de rastrear. Contas nominais, ou ao menos um registro de turno de quem detinha a senha compartilhada, teriam mostrado a pessoa na hora.

### 6.2 Senhas padrão

As credenciais padrão são publicadas nos manuais, então qualquer pessoa pode consultá-las. A ETSI EN 303 645 faz de "nenhuma senha padrão universal" a sua primeira provisão para a IoT de consumo, e a mesma ideia vale para os dispositivos da planta: troque as senhas padrão antes de um dispositivo entrar em serviço.

Na HPFL, verifique as senhas padrão de todo dispositivo novo antes que ele entre na rede da linha, incluindo a câmera de visão e os sensores IoT. Registre no registro de ativos que a senha padrão foi trocada e quando. Se um dispositivo não permitir trocar a senha padrão, relate isso para que o responsável decida sobre outros controles.

### 6.3 Contas privilegiadas

As contas de administrador da HMI-1 e do software de engenharia conseguem alterar telas, usuários e a lógica. Elas são usadas apenas para trabalho planejado, por pessoas nomeadas, e o seu uso é revisado. Não são o login do dia a dia.

Na HPFL, a senha de administrador da HMI-1 foi encontrada num bilhete adesivo no painel, o que mostra a rapidez com que o acesso privilegiado se espalha quando é usado em tarefas do dia a dia. Revise regularmente os logins de administrador contra o trabalho planejado e retire os direitos de administrador de quem não precisa mais deles no seu papel.

### 6.4 Regras práticas

Use frases-senha longas, mas digitáveis de luvas; não escreva senhas no painel; bloqueie a tela ou saia da sessão ao se afastar; nunca compartilhe uma senha pelo rádio ou por mensagem de texto.

Essas regras servem a um chão de fábrica em que as pessoas usam luvas, compartilham painéis e trabalham sob pressão de tempo. Se uma regra não puder ser seguida na prática, relate isso em vez de ignorá-la em silêncio; o responsável pode encontrar uma forma melhor, como um login por crachá. Revise as regras com cada nova equipe de turno.

### 6.5 Quando uma senha vaza

Relate, e então o responsável a troca num momento que não perturbe a linha. Examine os logins recentes daquela conta (Capítulo 9).

Na HPFL, quando Tomás encontrou a senha de administrador num bilhete adesivo, o engenheiro de controle a trocou na parada planejada seguinte e conferiu o registro de logins em busca de sessões de administrador inesperadas. Registre o vazamento, a troca e a revisão num único relatório. Procure logins em horários estranhos ou de lugares inesperados, e mudanças de setpoint que ninguém consiga explicar. Avise a equipe de turno quando a nova senha estiver em uso.

### Exemplo resolvido (HPFL sintética)

Tomás repara num bilhete adesivo na HMI-1 com "admin / Harbor2024". Ele o fotografa como evidência, remove-o, avisa o supervisor e o engenheiro de controle e escreve um breve relatório. O engenheiro troca a senha de administrador na parada planejada seguinte e confere o registro de logins em busca de sessões de administrador inesperadas.

> **Caso sintético — HPFL.** O bilhete e a senha são inventados.

### Erros e limites

Algumas IHMs antigas não comportam contas individuais; compense com registros de turno e controle físico. Trocar uma senha num sistema em funcionamento pode bloquear os operadores se for feito sem cuidado.

### Exercícios

- **EX021 — Registros e logins compartilhados.** Por que um único login "operator" compartilhado enfraquece uma investigação? *Rubrica:* 3 = não é possível atribuir as ações a uma pessoa; é preciso de registros de turno; 2 = "menos seguro"; 1 = vago; 0 = nenhum.
- **EX022 — Risco das credenciais padrão.** Explique por que senhas padrão são perigosas mesmo numa linha isolada. *Rubrica:* 3 = publicadas, qualquer um com alcance físico/de rede (empreiteiro, notebook) consegue entrar; o isolamento é imperfeito; 2 = um ponto; 1 = "hackers"; 0 = nenhum.
- **EX023 — O bilhete adesivo.** Liste em ordem os passos de Tomás depois de encontrar o bilhete. *Rubrica:* 3 = fotografar, remover, relatar ao supervisor/engenheiro, senha trocada na parada planejada, registros conferidos; 2 = a maioria; 1 = só remover; 0 = nenhum.
- **EX024 — Escolha do login diário.** O engenheiro de controle deve usar a conta de administrador para o monitoramento de rotina? Por quê? *Rubrica:* 3 = não; menor privilégio, reduz mudanças acidentais e uso indevido; 2 = só "não"; 1 = sim; 0 = nenhum.

### Síntese

Contas nominais, senhas padrão trocadas e uso limitado de administrador tornam as ações rastreáveis e mais difíceis de abusar.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 18

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Mídias removíveis e notebooks

### Objetivos de aprendizagem

Você vai (1) explicar como pen drives e notebooks levam malware para as plantas; (2) aplicar uma rotina de varredura e registro para mídias; e (3) decidir quais notebooks podem se conectar à linha.

### 7.1 Como o malware atravessa o isolamento

As linhas sem conexão com a internet ainda recebem arquivos: atualizações de firmware, arquivos de receita, ferramentas de fornecedores e fotos. Cada um chega num pen drive ou num notebook que já esteve em outros lugares. A NIST SP 800-82r3 lista as mídias removíveis como um caminho comum para dentro da TO, e incidentes bem conhecidos se espalharam exatamente assim.

Na HPFL, um fornecedor que chega com um arquivo de receita num pen drive pessoal é um evento de rotina. O arquivo pode ser inofensivo, mas o pen drive já esteve em outras plantas e escritórios. Trate todo arquivo que entra na linha como precisando da mesma rotina, por mais confiável que seja a sua origem.

### 7.2 Uma rotina para mídias

Use apenas pen drives fornecidos pela instalação. Antes que qualquer pen drive chegue a um dispositivo da linha, faça a varredura numa estação de varredura dedicada e atualizada, fora da linha; registre num livro de registro o número do pen drive, os nomes dos arquivos, o resultado da varredura e a pessoa; e mantenha o pen drive sob controle até ser usado. Pen drives desconhecidos encontrados no chão são entregues à segurança, nunca conectados "para ver de quem é".

Na HPFL, a estação de varredura fica fora da linha, e os pen drives da instalação são numerados, como o HP-07. O livro de registro permite a qualquer pessoa rastrear um arquivo até a sua origem se surgir um problema depois. Confira o livro durante as vistorias; um pen drive ausente dele é uma constatação.

### 7.3 Notebooks

Apenas o ENG-LT e os notebooks de fornecedores aprovados se conectam aos equipamentos da linha. Um notebook aprovado tem as correções aplicadas, roda antimalware, não tem software pessoal e é verificado antes de cada visita. O fornecedor cujo notebook não atenda a esse padrão usa, em vez dele, um notebook da instalação com as ferramentas do fornecedor instaladas.

Mantenha no registro de ativos uma lista dos notebooks aprovados, com o responsável e a data da última verificação de cada um. Na HPFL, o ENG-LT é o único notebook da instalação autorizado a programar os CLPs. Um notebook de fornecedor que não possa ser verificado não se conecta; o fornecedor usa um notebook da instalação com as suas ferramentas.

### 7.4 Transferir arquivos sem USB

Algumas instalações movem arquivos por um servidor de transferência controlado na DMZ, em vez de pen drives. Isso mantém um registro de cada arquivo e elimina de vez a necessidade de conectar mídias aos dispositivos da linha.

Na HPFL, a DMZ já tem um servidor de transferência de arquivos. Os arquivos que chegam ali podem ser varridos automaticamente e registrados com remetente e horário, e os dispositivos da linha os buscam por um conduíte documentado. Tirar os pen drives da rotina também elimina o risco de um pen drive se perder no chão de fábrica.

### Exemplo resolvido (HPFL sintética)

Um fornecedor chega com um arquivo de receita num pen drive pessoal. Tomás leva o pen drive à estação de varredura, copia o arquivo para o pen drive da instalação HP-07 depois de uma varredura limpa, registra "HP-07, recipe_v12.csv, limpo, Tomás, 09:30" e entrega o HP-07 ao engenheiro de controle. O pen drive pessoal volta para o fornecedor sem ter sido conectado a nada da linha.

> **Caso sintético — HPFL.** O fornecedor, os números dos pen drives e o arquivo são inventados.

### Erros e limites

Uma varredura limpa significa apenas que nenhum malware conhecido foi encontrado; um malware novo pode passar. Mantenha a rotina mesmo assim: ela corta a maior parte do risco e deixa um registro se algo der errado.

### Exercícios

- **EX025 — Encontrado no chão.** Um pen drive com a etiqueta "Salários 2026" está ao lado da HMI-1. O que você faz? *Rubrica:* 3 = não conectar; entregar à segurança/supervisor; registrar onde foi encontrado; 2 = só entregar; 1 = verificar num PC de escritório; 0 = conectar na IHM.
- **EX026 — Campos do livro de mídias.** Liste quatro campos do livro de registro de mídias. *Rubrica:* 3 = id do pen drive, arquivos, resultado da varredura, pessoa e horário; 2 = três; 1 = um; 0 = nenhum.
- **EX027 — O significado de uma varredura limpa.** Um colega diz "a varredura deu limpo, então o arquivo é seguro". Corrija a afirmação. *Rubrica:* 3 = só não foi encontrado malware conhecido; ameaças novas são possíveis; a rotina ainda reduz o risco; 2 = parcial; 1 = concorda; 0 = nenhum.
- **EX028 — Recusa do notebook do fornecedor.** O notebook do fornecedor não tem antimalware. Que alternativa permite que o trabalho prossiga? *Rubrica:* 3 = notebook da instalação com as ferramentas do fornecedor, ou transferir os arquivos pela estação de varredura; 2 = só reagendar; 1 = permitir mesmo assim; 0 = nenhum.

### Síntese

Todo arquivo que entra na linha passa por um caminho varrido, registrado e controlado; mídias desconhecidas nunca tocam os dispositivos da linha.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 18

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Acesso remoto de fornecedores

### Objetivos de aprendizagem

Você vai (1) descrever como os fornecedores chegam remotamente aos sistemas da planta; (2) explicar as lições do alerta de 2021 sobre a estação de água de Oldsmar; e (3) conduzir uma sessão remota seguindo uma lista de verificação simples.

### 8.1 Por que os fornecedores se conectam

Os fabricantes de máquinas dão suporte remoto aos seus equipamentos para diagnosticar falhas sem viajar. Isso é útil, mas um enlace permanente, sempre ativo, para dentro da linha também é uma porta de entrada permanente para quem roubar as credenciais.

Na HPFL, o fabricante da embaladora precisa ocasionalmente ler os registros de falhas. Essa necessidade é real, e recusar todo acesso remoto significaria esperar dias por uma visita. A resposta é permitir o acesso apenas por uma rota controlada, para um trabalho específico, sob a vigilância da instalação.

### 8.2 O que o alerta constatou

O alerta AA21-042A da CISA descreve o comprometimento de uma estação de tratamento de água nos EUA, em 2021, em que um software de acesso remoto foi usado para chegar a um sistema de controle. Suas recomendações incluem usar autenticação multifator, senhas fortes para a área de trabalho remota, fechar as portas de área de trabalho remota não usadas e auditar as conexões remotas. Esses pontos se aplicam diretamente a uma linha de embalagem.

Na HPFL, isso significa verificar que nenhum software de área de trabalho remota roda diretamente na HMI-1 ou no ENG-LT, que as contas dos fornecedores usam autenticação multifator e que as sessões remotas são registradas e revisadas. A reunião de lições aprendidas do Capítulo 16 encontrou depois uma porta de área de trabalho remota aberta na HMI-1 por um empreiteiro, exatamente o tipo de rota contra a qual o alerta adverte.

### 8.3 Um padrão mais seguro

O acesso remoto passa por um único gateway controlado pela instalação, na DMZ, nunca por software instalado diretamente nas IHMs. Cada fornecedor tem uma conta nominal com autenticação multifator. A conexão fica desabilitada por padrão e é habilitada para uma janela de sessão com chamado. Alguém da instalação acompanha a sessão e pode encerrá-la. As sessões são registradas e revisadas.

Escreva o padrão num procedimento curto que os fornecedores recebem antes da primeira sessão. O supervisor abre um chamado com uma janela de tempo; o técnico habilita a conta e acompanha. Se um fornecedor pedir acesso permanente, o pedido vai para o supervisor e normalmente é recusado.

### 8.4 Encerrar a sessão

Quando o trabalho termina, a conta é desabilitada de novo, a mudança é registrada e o operador confirma que a linha se comporta normalmente. Uma sessão deixada habilitada "para a próxima vez" é a falha mais comum.

Na HPFL, Tomás desabilitou a conta do fornecedor às 14:38, antes do fim da janela, e registrou no chamado os horários de início e de fim. Verifique as contas dos fornecedores toda semana para confirmar que nenhuma ficou habilitada. Uma conta encontrada habilitada fora de um chamado é relatada como constatação. Confirme também que a mudança do fornecedor aparece no registro de ativos.

### Exemplo resolvido (HPFL sintética)

O fabricante da embaladora precisa ler um registro de falhas. O supervisor abre o chamado 4471 para 14:00–14:45. Tomás habilita a conta do fornecedor no gateway, acompanha o compartilhamento de tela, vê que o engenheiro apenas abre o visualizador de falhas e desabilita a conta às 14:38. Ele registra a sessão no chamado, com os horários de início e de fim.

> **Caso sintético — HPFL.** O chamado, o fornecedor e os horários são inventados.

### Erros e limites

Algumas máquinas chegam com modems celulares embutidos para o suporte do fornecedor; eles contornam totalmente o gateway e precisam ser encontrados e controlados. Acompanhar uma sessão não pega tudo; o registro e a revisão acrescentam uma segunda verificação.

### Exercícios

- **EX029 — Recomendações do alerta.** Nomeie três recomendações do AA21-042A. *Rubrica:* 3 = três entre MFA, senhas fortes de RDP, fechar portas de RDP não usadas, auditar as conexões remotas; 2 = duas; 1 = uma; 0 = nenhum.
- **EX030 — Enlace sempre ativo.** Explique por que "o enlace do fornecedor fica sempre ativo, então o suporte é mais rápido" é um risco. *Rubrica:* 3 = entrada permanente para credenciais roubadas, uso sem acompanhamento; 2 = risco vago; 1 = concorda; 0 = nenhum.
- **EX031 — Registro da sessão.** O que Tomás deve escrever no chamado 4471 depois da sessão? *Rubrica:* 3 = nome/conta do fornecedor, início/fim, o que foi feito, conta desabilitada, linha normal; 2 = parte; 1 = "feito"; 0 = nenhum.
- **EX032 — O modem escondido.** Durante uma vistoria, Tomás encontra um modem celular no armário da enchedora. Por que isso é importante? *Rubrica:* 3 = contorna o gateway/MFA/registro, caminho não gerenciado; relatar ao responsável; 2 = um; 1 = removê-lo ele mesmo; 0 = nenhum.

### Síntese

O acesso de fornecedores passa por um único gateway, com contas nominais e multifator, habilitado apenas em janelas acompanhadas e registradas.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 18

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Ler registros e alarmes

### Objetivos de aprendizagem

Você vai (1) distinguir alarmes de processo de eventos relevantes para a segurança; (2) filtrar um registro com um pequeno script; e (3) decidir quando um padrão precisa ser escalado.

### 9.1 Dois tipos de mensagens

As IHMs e os CLPs relatam alarmes de processo, como falta de filme ou um enrosco. Também registram logins, mudanças de configuração e downloads de programas. Os alarmes de processo são tratados pelos operadores; o segundo tipo diz quem fez o quê no sistema, e é ali que as pistas de segurança costumam aparecer.

Na HPFL, os alarmes de falta de filme e de enrosco pertencem aos operadores. Os logins, as mudanças de setpoint e os downloads de programas são os registros a exportar e guardar. Separar os dois mantém a revisão de segurança curta o bastante para acontecer todos os dias.

### 9.2 Padrões que importam

Vários logins com falha seguidos de um sucesso podem significar que alguém adivinhou uma senha. Um setpoint alterado fora de um trabalho planejado, um download de programa que ninguém esperava ou um login de administrador num horário estranho merecem um olhar. Um evento isolado muitas vezes é inocente; o que importa é a sequência.

```python
"""Lab 9: filter a synthetic HMI event log for security-relevant entries."""
log = """06:02 HMI-1 login operator1 ok
06:15 PLC-FILL alarm low-film
07:40 HMI-1 login admin fail
07:41 HMI-1 login admin fail
07:41 HMI-1 login admin fail
07:43 HMI-1 login admin ok
07:45 PLC-WRAP setpoint speed 120->180 by admin
08:10 PLC-FILL alarm jam-cleared"""
fails = 0
for line in log.splitlines():
    t, dev, kind, *rest = line.split()
    if kind == "login" and rest[-1] == "fail":
        fails += 1
    if kind == "setpoint" or (kind == "login" and rest[0] == "admin" and rest[-1] == "ok"):
        print("REVIEW", line)
print("failed logins:", fails)
```

Execute com `python3 lab_logs.py`. Saída verificada:

```text
REVIEW 07:43 HMI-1 login admin ok
REVIEW 07:45 PLC-WRAP setpoint speed 120->180 by admin
failed logins: 3
```

Na HPFL, o laboratório mostra exatamente esse tipo de sequência: três logins de administrador com falha, um sucesso e, dois minutos depois, uma mudança de velocidade. Cada evento isolado poderia ser ignorado. Juntos, levantam uma pergunta que precisa de resposta do supervisor.

### 9.3 Lendo a saída

O script conta três logins de administrador com falha e depois mostra um login de administrador bem-sucedido às 07:43 e uma mudança da velocidade da embaladora de 120 para 180 dois minutos depois. Juntos, formam uma história que vale verificar: havia uma mudança planejada às 07:45, e quem estava conectado?

O script não explica o que aconteceu; apenas separa as linhas sobre as quais vale perguntar. O próximo passo é verificar se havia uma mudança planejada e quem estava no turno. Na HPFL, a resposta se revelou inocente, mas ainda assim valia verificar a sequência.

### 9.4 Escale, não investigue sozinho

O trabalho de Tomás é perceber e relatar com evidências: as linhas do registro, o horário, o que a linha fez. O engenheiro de controle e o líder de segurança decidem o que acontece em seguida.

Relate com as linhas do registro anexadas, o horário em que você as percebeu e o que a linha estava fazendo naquele momento. Não entre nos dispositivos para olhar mais nem troque senhas você mesmo. Se o engenheiro de controle pedir mais evidências, ele dirá o que coletar e como. Guarde uma cópia do que você relatou e de quando enviou.

### 9.5 O horário importa

Os registros só são comparáveis se os relógios dos dispositivos concordam. Anote no seu relato qualquer diferença de relógio que você conheça.

Se a HMI-1 e o PLC-WRAP discordarem em vários minutos, uma mudança de setpoint pode parecer acontecer antes do login que a causou. Pergunte ao engenheiro de controle como os relógios são ajustados na linha e registre qualquer defasagem conhecida no registro de ativos. Ao exportar registros, anote a hora do seu relógio e a hora mostrada em cada dispositivo, para que a diferença possa ser corrigida depois. Um relógio que deriva minutos pode fazer uma sequência inocente parecer suspeita, ou esconder uma suspeita.

### Exemplo resolvido (HPFL sintética)

Tomás pergunta ao supervisor; nenhuma mudança estava planejada. O operador da noite diz que esqueceu a senha de administrador, tentou três vezes, depois se lembrou dela e aumentou a velocidade para desafogar um acúmulo. A mudança é revertida e registrada, e o uso da conta de administrador para mudanças de velocidade é retirado dos operadores.

> **Caso sintético — HPFL.** O registro e a explicação são inventados.

### Erros e limites

Os registros de dispositivos pequenos são curtos e podem se sobrescrever em poucos dias, então exporte-os regularmente. Uma explicação inocente também deve ser registrada.

### Exercícios

- **EX033 — Classificar as entradas.** Quais linhas do registro do laboratório são alarmes de processo e quais são relevantes para a segurança? *Rubrica:* 3 = low-film e jam-cleared são de processo; logins e setpoint, de segurança; 2 = a maioria; 1 = uma; 0 = nenhum.
- **EX034 — Cinco falhas.** Se mais duas linhas de falha de login de administrador forem acrescentadas antes das 07:43, o que a última linha imprime? *Rubrica:* 3 = "failed logins: 5"; 2 = 5; 1 = 3; 0 = nenhum.
- **EX035 — Por que a sequência importa.** Explique por que o login das 07:43 importa mais depois das falhas do que isolado. *Rubrica:* 3 = sucesso depois de falhas sugere adivinhação; ligado à mudança de setpoint; 2 = um ponto; 1 = "é admin"; 0 = nenhum.
- **EX036 — Conteúdo do relato.** Escreva os quatro fatos que Tomás inclui ao relatar a mudança das 07:45. *Rubrica:* 3 = horário, dispositivo, valores da mudança, conta/sequência de logins (mais o efeito na linha); 2 = três; 1 = um; 0 = nenhum.

### Síntese

As pistas de segurança estão nos registros de login e de mudanças; são as sequências, e não as linhas isoladas, que justificam escalar.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 18

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Correções e alertas de segurança

### Objetivos de aprendizagem

Você vai (1) ler um alerta de ICS e encontrar os fatos que importam; (2) cruzar um alerta com o registro de ativos; e (3) explicar por que as plantas muitas vezes mitigam antes de corrigir.

### 10.1 De onde vêm os alertas

Os fornecedores e a CISA publicam alertas para produtos industriais; o índice da CISA os lista com os nomes dos produtos, as versões afetadas, o impacto e as mitigações. Um alerta é o ponto de partida, não a decisão.

Na HPFL, o engenheiro de controle e Tomás acompanham os alertas dos fabricantes do PLC-FILL, do PLC-WRAP, da HMI-1 e da VIS-CAM. Cruzar cada um com o registro de ativos lhes diz rapidamente se alguma ação é necessária, e são os campos de firmware do registro que tornam isso possível. Anote no registro de onde veio cada alerta e quando foi lido, e se foi revisado desde então.

### 10.2 Lendo um alerta

Encontre cinco fatos: produto e modelo, versões afetadas, o que um atacante poderia fazer, se é preciso acesso pela rede ou físico e a correção ou contorno do fornecedor. Depois consulte o registro de ativos: temos esse modelo, nessa versão, alcançável dessa forma?

Na HPFL, o alerta que afetava o PLC-WRAP exigia acesso pela rede à sua porta de programação, e o FW-1 já só permitia isso a partir do ENG-LT. Responder às cinco perguntas deixou isso claro em minutos. Registre as respostas no registro do alerta, mesmo quando o resultado for que nenhuma ação é necessária.

### 10.3 Por que não corrigir imediatamente

Uma atualização de firmware num CLP o para, pode mudar o comportamento e precisa ser testada com o programa. As fábricas de alimentos também precisam de verificações de qualidade depois de mudanças. Por isso, a ordem habitual é: confirmar a exposição, aplicar rapidamente uma mitigação (por exemplo, bloquear o serviço vulnerável no firewall) e depois agendar a correção para uma parada planejada, com um plano de reversão.

Na HPFL, a mitigação para o PLC-WRAP já estava em vigor no FW-1, e a correção foi agendada para uma parada planejada três semanas depois. O plano de reversão deve nomear o programa salvo e a versão de firmware à qual voltar se a atualização causar problemas.

### 10.4 Registrando a decisão

Cada alerta recebe um registro: aplica-se ou não, por quê, mitigação, data planejada da correção, responsável. Uma decisão de não corrigir, com as razões e uma data de revisão, continua sendo uma decisão.

Mantenha os registros num só lugar, ligados ao registro de ativos, para que um leitor posterior veja quais alertas foram considerados e por quê. Revise mensalmente os itens em aberto. Um registro sem data de revisão tende a ser esquecido. Na HPFL, o registro do alerta do PLC-WRAP nomeou a regra já existente do FW-1 como mitigação e deu a data da parada planejada para a correção. Quando a correção for aplicada, o registro é encerrado com a nova versão de firmware.

### 10.5 Atualizações de IHMs e notebooks

As IHMs baseadas em Windows e o ENG-LT também precisam de atualizações do sistema operacional, mas apenas das aprovadas pelo fornecedor da IHM, instaladas durante paradas planejadas.

Pergunte ao fornecedor da IHM quais atualizações estão aprovadas e registre cada atualização no registro de ativos e no chamado de mudança. Depois de atualizar, teste se as telas mostram os valores corretos e se a HMI-1 ainda se comunica com os dois CLPs. As atualizações do ENG-LT seguem a mesma abordagem planejada. Guarde a imagem anterior ou um ponto de restauração, para que a atualização possa ser desfeita se as telas ou a comunicação falharem. Nunca deixe uma IHM se atualizar sozinha pela internet; isso exigiria uma conexão que a linha não deve ter.

### Exemplo resolvido (HPFL sintética)

Um alerta sintético afirma que o firmware 2.0 do modelo de CLP da embaladora permite mudanças de programa sem autenticação pela rede. O registro de ativos (depois do Capítulo 5) diz que o PLC-WRAP roda o 2.0. O engenheiro de controle confirma que o FW-1 já bloqueia a porta de programação para tudo, exceto o ENG-LT, registra isso como mitigação e agenda o firmware 2.3 para a próxima parada planejada, em três semanas.

> **Caso sintético — HPFL.** O alerta e as versões são inventados; os alertas reais estão em cisa.gov.

### Erros e limites

Os alertas podem ser revisados; confira de novo antes de agir. As versões podem aparecer escritas de forma diferente nas etiquetas e no software.

### Exercícios

- **EX037 — Cinco fatos.** Liste os cinco fatos a extrair de um alerta. *Rubrica:* 3 = produto/modelo, versões, impacto, acesso necessário, correção/contorno; 2 = quatro; 1 = dois; 0 = nenhum.
- **EX038 — Aplica-se?** Um alerta afeta as versões anteriores à 2.2 do modelo do PLC-FILL; o PLC-FILL roda a 3.2. Aplica-se? *Rubrica:* 3 = não, a 3.2 é posterior; registrar como não aplicável, com a razão; 2 = não; 1 = sim; 0 = nenhum.
- **EX039 — Mitigar primeiro.** Por que o engenheiro mitiga no FW-1 antes de corrigir o PLC-WRAP? *Rubrica:* 3 = a correção exige parada/testes/qualidade; o firewall reduz a exposição agora; 2 = um; 1 = "preguiça"; 0 = nenhum.
- **EX040 — Registro de uma correção adiada.** Escreva o registro do alerta para o PLC-WRAP. *Rubrica:* 3 = aplica-se, razão, mitigação, data planejada, responsável, revisão; 2 = a maioria; 1 = "corrigir depois"; 0 = nenhum.

### Síntese

Os alertas são cruzados com o registro de ativos, mitigados rapidamente e corrigidos numa parada planejada e testada.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 18

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Cópias de segurança e restauração

### Objetivos de aprendizagem

Você vai (1) listar o que precisa de cópia de segurança numa linha; (2) verificar a integridade das cópias com hashes; e (3) explicar por que uma restauração precisa ser testada.

### 11.1 O que copiar

Programas dos CLPs, projetos e telas das IHMs, arquivos de receita, configurações dos dispositivos (switches, firewall, ajustes da câmera) e os dados de licença do software de engenharia. Sem eles, recuperar-se de uma falha ou de um ataque significa reconstruir de memória.

Na HPFL, isso significa os programas do PLC-FILL e do PLC-WRAP, o projeto da HMI-1, os arquivos de receita, os ajustes da VIS-CAM e as configurações do FW-1 e dos switches da linha. Liste cada item no registro de ativos com a data da sua última cópia. Um item que falta na lista provavelmente também falta nas cópias.

### 11.2 Onde guardar as cópias

Pelo menos uma cópia fora da rede da linha, de preferência offline, para que um malware que cifre a linha não consiga alcançá-la. Etiquete cada uma com dispositivo, data e versão.

Na HPFL, o engenheiro de controle mantém um armazenamento offline, que foi onde se encontrou uma cópia mais antiga e íntegra do programa da embaladora. Mantenha pelo menos duas cópias de cada cópia de segurança importante e registre onde cada uma está. Verifique se a cópia offline pode ser acessada durante um turno da noite. Anote quem pode levar uma cópia para fora da instalação.

### 11.3 Verificando a integridade

Um hash, como o SHA-256, é uma impressão digital de um arquivo: qualquer mudança dá um valor diferente. Registre o hash quando a cópia é feita; confira-o antes de restaurar.

```python
"""Lab 11: verify synthetic PLC backup files against recorded SHA-256 values."""
import hashlib
files = {"PLC-FILL_2026-09.bak": b"fill program v3.2 rungs 1-140",
         "PLC-WRAP_2026-09.bak": b"wrap program v2.0 rungs 1-88 edited"}
recorded = {"PLC-FILL_2026-09.bak": hashlib.sha256(b"fill program v3.2 rungs 1-140").hexdigest(),
            "PLC-WRAP_2026-09.bak": hashlib.sha256(b"wrap program v2.0 rungs 1-88").hexdigest()}
for name, data in files.items():
    h = hashlib.sha256(data).hexdigest()
    print(f"{name:22} {h[:12]} {'MATCH' if h == recorded[name] else 'MISMATCH - do not restore'}")
```

Execute com `python3 lab_hash.py`. Saída verificada:

```text
PLC-FILL_2026-09.bak   0278a5f83d56 MATCH
PLC-WRAP_2026-09.bak   9974ecb17bab MISMATCH - do not restore
```

Guarde os hashes separados das cópias, por exemplo no chamado de mudança ou num registro, para que quem alterar uma cópia não consiga alterar também o seu hash. O Laboratório 11 confere dois arquivos de cópia contra os hashes registrados e mostra como é uma divergência.

### 11.4 Lendo o resultado

A cópia da enchedora corresponde ao hash registrado. A cópia da embaladora não: o seu conteúdo foi editado depois que o hash foi registrado. Restaurá-la poderia carregar um programa que ninguém aprovou, então ela é posta de lado e relatada.

Uma divergência não prova um ataque; prova que o arquivo mudou depois que o seu hash foi registrado. Na HPFL, a edição foi rastreada até um ajuste aprovado, mas não registrado. O procedimento foi atualizado para que toda mudança produza uma nova cópia e um novo hash no mesmo chamado.

### 11.5 Testes de restauração

Uma cópia nunca restaurada é uma esperança, não um plano. Uma ou duas vezes por ano, restaure um programa num CLP de reserva ou de laboratório e compare-o com o que está em funcionamento.

Registre o teste de restauração no registro de ativos, com a data, o dispositivo, a cópia usada e o resultado. Se uma restauração falhar, descubra o porquê antes que uma falha real force a pergunta. Na HPFL, um CLP de reserva da prateleira poderia ser usado para isso, depois de verificar que ele está marcado como reserva no registro.

### 11.6 Com que frequência

Faça cópias depois de cada mudança aprovada e numa data mensal fixa, o que vier primeiro, para que a cópia boa mais recente nunca fique muito atrás do programa em funcionamento.

Na HPFL, as cópias de setembro eram as mais recentes antes da edição da embaladora, e é por isso que uma mudança aprovada posterior, sem uma nova cópia, causou confusão. Vincule as cópias aos chamados de mudança, para que cada mudança aprovada produza uma cópia e um hash novos. Verifique mensalmente se a cópia mais recente de cada dispositivo é mais nova do que a sua última mudança aprovada. Se não for, faça uma nova cópia e registre o hash antes do próximo turno.

### Exemplo resolvido (HPFL sintética)

Tomás relata a divergência. O engenheiro de controle encontra uma cópia mais antiga e íntegra no armazenamento offline e compara o arquivo editado: alguém acrescentou uma linha ao programa da embaladora depois da cópia de setembro, sem chamado de mudança. A edição é rastreada até um ajuste aprovado, mas não registrado; o registro de ativos e o procedimento são atualizados.

> **Caso sintético — HPFL.** Os arquivos e hashes são produzidos pelo laboratório com conteúdo inventado.

### Erros e limites

Um hash que corresponde prova que o arquivo não mudou desde o registro, não que a versão registrada era boa. Os hashes precisam ser guardados separados das cópias.

### Exercícios

- **EX041 — Lista de cópias.** Nomeie cinco coisas que precisam de cópia de segurança na linha da HPFL. *Rubrica:* 3 = cinco itens corretos; 2 = quatro; 1 = dois; 0 = nenhum.
- **EX042 — Decisão diante da divergência.** O que Tomás faz com a cópia da embaladora marcada MISMATCH? *Rubrica:* 3 = não restaurar; pôr de lado; relatar; encontrar uma cópia verificada; 2 = só relatar; 1 = restaurar mesmo assim; 0 = nenhum.
- **EX043 — Um byte alterado.** Se um caractere dos dados da enchedora fosse alterado, o que o laboratório imprimiria para esse arquivo? *Rubrica:* 3 = hash diferente e "MISMATCH - do not restore"; 2 = divergência; 1 = correspondência; 0 = nenhum.
- **EX044 — Onde guardar os hashes.** Por que os hashes são guardados separados dos arquivos de cópia? *Rubrica:* 3 = um atacante que altere as cópias poderia alterar também os hashes no mesmo lugar; 2 = vago; 1 = espaço; 0 = nenhum.

### Síntese

As cópias de segurança ficam offline, etiquetadas, com hash e testadas por restauração; uma divergência impede a restauração.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 18

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Segmentação e regras de firewall

### Objetivos de aprendizagem

Você vai (1) explicar em palavras simples as zonas e os conduítes da IEC 62443; (2) ler uma tabela de regras de firewall; e (3) identificar regras que enfraquecem a segmentação.

### 12.1 Zonas e conduítes

A IEC 62443 agrupa ativos com necessidades de segurança semelhantes em zonas e chama de conduítes as conexões controladas entre elas. Na HPFL: a zona da linha (CLPs, IHM, câmera), uma DMZ (cópia do historiador, gateway de acesso remoto, servidor de transferência de arquivos) e a zona de escritório. O tráfego só atravessa por conduítes protegidos por firewall e documentados.

Escreva cada conduíte com o seu propósito, o tráfego que permite e o seu responsável. Na HPFL, os conduítes são a linha enviando dados ao historiador na DMZ, o ENG-LT alcançando os CLPs e o acesso de fornecedores pelo gateway na DMZ. Qualquer outra coisa que atravesse a fronteira de uma zona é uma constatação.

### 12.2 A DMZ

Os usuários do escritório querem dados de produção; a linha não deve aceitar conexões do escritório. Por isso, a linha envia os dados a um servidor na DMZ, e o escritório os lê ali. Assim, nenhuma conexão precisa ir diretamente do escritório para a linha.

Na HPFL, a linha envia os dados à cópia do historiador na DMZ, e os usuários do escritório os leem ali. O acesso de fornecedores e a transferência de arquivos também chegam na DMZ. Assim, o FW-1 não precisa de nenhuma regra que deixe máquinas do escritório entrarem diretamente na linha, que é exatamente o tipo de regra que o exemplo resolvido abaixo remove.

### 12.3 Lendo as regras

Cada regra tem origem, destino, porta e ação, lidas de cima para baixo; a primeira correspondência vale. Uma última regra "negar tudo" faz com que tudo o que não estiver listado seja bloqueado.

Ler de cima para baixo importa porque uma regra ampla de permissão colocada acima de uma negação estreita torna a negação inútil. Ao revisar uma tabela, pergunte para cada regra: quem é o dono, por que existe e se uma regra acima dela já decide o mesmo tráfego. A tabela do FW-1 na HPFL tem quatro regras, o que facilita praticar.

### 12.4 Regras fracas

Procure origens "any", faixas amplas de portas, regras sem comentário ou sem dono e regras temporárias que nunca foram removidas. Cada uma deve ser questionada e justificada ou removida pelo controle de mudanças.

Na HPFL, a regra 3, de qualquer origem do escritório para qualquer destino da linha, marcada como temporária de 2025, mostrava todos esses sinais de alerta ao mesmo tempo. Ela foi removida pelo controle de mudanças e testada na parada seguinte. Registre cada pergunta levantada e a sua resposta, para que uma regra removida não seja depois acrescentada de novo sem revisão.

### 12.5 Não edite por conta própria

As mudanças no firewall são feitas pelo dono da rede, com um chamado de mudança e um plano de reversão; uma regra errada pode parar a linha.

Se encontrar uma regra fraca, relate-a com o número da regra e a sua razão. O dono da rede decide como mudá-la, prepara uma reversão e testa numa parada planejada. O seu papel é perceber e explicar o risco. Na HPFL, o dono da rede só removeu a regra 3 depois de abrir uma mudança e combinar um teste na parada seguinte. Uma regra alterada por outra pessoa, por mais bem-intencionada, não deixa registro nem reversão e pode parar a linha.

### Exemplo resolvido (HPFL sintética)

Tomás revisa a tabela do FW-1 com o dono da rede. A regra 1 permite o ENG-LT até a porta de programação dos CLPs; a regra 2 deixa a linha enviar dados ao historiador na DMZ; a regra 3, "office any → line any allow — temp 2025", não tem dono. A regra 4 nega tudo. Eles abrem uma mudança para apagar a regra 3, testam na parada seguinte, e depois disso a linha funciona normalmente.

> **Caso sintético — HPFL.** A tabela de regras é inventada.

### Erros e limites

Uma boa tabela de regras pode ser anulada por um switch ou modem não gerenciado que contorne o firewall; as vistorias e os diagramas complementam a revisão das regras.

### Exercícios

- **EX045 — Zonas da HPFL.** Nomeie as três zonas da HPFL e um ativo em cada uma. *Rubrica:* 3 = linha/DMZ/escritório com ativos corretos; 2 = duas; 1 = uma; 0 = nenhum.
- **EX046 — Primeira correspondência.** Com a regra 3 acima da regra 4, o que acontece com o tráfego do escritório para a HMI-1? *Rubrica:* 3 = permitido pela regra 3 antes que a negação se aplique; 2 = permitido; 1 = negado; 0 = nenhum.
- **EX047 — Por que uma DMZ.** Explique como a DMZ permite que a equipe do escritório veja dados de produção sem se conectar à linha. *Rubrica:* 3 = a linha envia ao servidor da DMZ, o escritório lê ali, nenhuma regra escritório→linha; 2 = parcial; 1 = "é mais seguro"; 0 = nenhum.
- **EX048 — Remover uma regra.** Descreva os passos seguros para remover a regra 3. *Rubrica:* 3 = chamado de mudança, o dono confirma, janela planejada, reversão, teste, registro; 2 = alguns; 1 = apagar agora; 0 = nenhum.

### Síntese

As zonas são separadas por conduítes documentados e com dono; regras amplas ou sem dono são removidas pelo controle de mudanças.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 18

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Dispositivos IoT no chão de fábrica

### Objetivos de aprendizagem

Você vai (1) identificar os dispositivos IoT numa linha; (2) verificá-los contra uma linha de base com as provisões da ETSI EN 303 645; e (3) decidir como conectá-los com segurança.

### 13.1 O que conta como IoT aqui

Medidores de energia inteligentes, sensores de vibração sem fio, a câmera de visão, uma impressora de etiquetas conectada à nuvem e tablets usados pela equipe de qualidade. Eles muitas vezes chegam pelas compras, e não pela engenharia, então ninguém os verifica antes.

Na HPFL, a equipe de qualidade pediu sensores de vibração sem fio nos motores da embaladora, e a câmera de visão já está instalada. Cada um desses dispositivos deve aparecer no registro de ativos, com um responsável e a rede que usa. As compras devem envolver o dono da rede antes do pedido. Peça às compras que lhe informem sobre todo dispositivo em rede encomendado.

### 13.2 Uma linha de base para comparar

A ETSI EN 303 645 estabelece provisões básicas de segurança para a IoT de consumo, e a NIST IR 8259 descreve o que os fabricantes devem fazer. Ambas também são listas de verificação úteis para dispositivos de planta. Perguntas a fazer a um fornecedor: há senhas padrão universais? Há uma forma de relatar vulnerabilidades? Serão fornecidas atualizações de software, e por quanto tempo? A comunicação é cifrada? O dispositivo pode ser reinicializado e ter os seus dados apagados?

Envie as perguntas ao fornecedor antes da compra e guarde as respostas com o registro da compra. Onde possível, verifique as alegações na entrega: o dispositivo obriga a trocar a senha na configuração, e ele realmente usa TLS? Uma resposta que não pode ser verificada ainda é útil, mas deve ser marcada como alegação.

### 13.3 Conectar com segurança

Os dispositivos IoT que conversam com a nuvem de um fornecedor pertencem a um segmento próprio, não à VLAN da linha. Permita apenas os endereços de nuvem de que eles precisam, bloqueie-os de alcançar os CLPs e registre-os no registro de ativos com um responsável e um plano de atualizações.

Na HPFL, o dono da rede escolheu uma nova VLAN de IoT para o gateway dos sensores VIB-1 a VIB-4, em vez da VLAN 20 da linha, porque os sensores relatam a uma nuvem do fornecedor. Depois da instalação, verifique com o dono da rede que o gateway não consegue alcançar os CLPs, por meio de uma revisão das regras, e não sondando.

### 13.4 Fim do suporte

Quando um fornecedor deixa de publicar atualizações, planeje a substituição. Um sensor barato deixado sem correções por anos na rede da linha é um ponto de apoio fácil.

Registre no registro de ativos o período de suporte declarado pelo fornecedor, para que o fim do suporte possa ser planejado bem antes de chegar. Na HPFL, o fornecedor dos sensores de vibração prometeu atualizações por cinco anos; a data de substituição pertence ao registro, ao lado da entrada do dispositivo. Se um dispositivo precisar ficar depois do fim do suporte, reforce o seu isolamento e registre a decisão com uma data de revisão. Avise o responsável com bastante antecedência, para que o orçamento possa ser planejado.

### Exemplo resolvido (HPFL sintética)

A qualidade quer sensores de vibração sem fio VIB-1 a VIB-4 nos motores da embaladora, relatando a uma nuvem do fornecedor. Tomás envia ao fornecedor as cinco perguntas. Respostas: senhas únicas por dispositivo, um endereço de divulgação publicado, atualizações por cinco anos, TLS até a nuvem, reinicialização de fábrica documentada. O dono da rede coloca o gateway dos sensores numa nova VLAN de IoT com permissão apenas para os endereços de nuvem do fornecedor.

> **Caso sintético — HPFL.** Os sensores e as respostas do fornecedor são inventados.

### Erros e limites

As respostas dos fornecedores são alegações; verifique o que puder (por exemplo, que o dispositivo obrigou a trocar a senha na configuração). A ETSI EN 303 645 tem como alvo produtos de consumo, então dispositivos industriais podem precisar de requisitos adicionais da IEC 62443-4-2.

### Exercícios

- **EX049 — Identificar IoT.** Liste três dispositivos IoT que poderiam aparecer na HPFL fora dos desenhos de engenharia. *Rubrica:* 3 = três dispositivos plausíveis; 2 = dois; 1 = um; 0 = nenhum.
- **EX050 — Perguntas ao fornecedor.** Escreva as cinco perguntas básicas a um fornecedor. *Rubrica:* 3 = senhas padrão, divulgação, período de atualizações, criptografia, reinicialização/apagamento; 2 = quatro; 1 = duas; 0 = nenhum.
- **EX051 — Posicionamento.** Onde o gateway dos sensores VIB deve se conectar, e o que deve poder alcançar? *Rubrica:* 3 = VLAN de IoT separada; só a nuvem do fornecedor; bloqueado para os CLPs; 2 = só separada; 1 = VLAN da linha; 0 = nenhum.
- **EX052 — Fim das atualizações.** O fornecedor da impressora de etiquetas anuncia o fim do suporte. O que Tomás registra e planeja? *Rubrica:* 3 = situação no registro, nota de risco, isolamento compensatório, plano/data de substituição; 2 = parte; 1 = ignorar; 0 = nenhum.

### Síntese

A IoT do chão de fábrica é verificada contra uma linha de base, isolada ao que precisa e substituída quando o suporte acaba.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 18

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Reconhecer comportamento anormal

### Objetivos de aprendizagem

Você vai (1) descrever como é o normal da linha da HPFL; (2) reconhecer sinais que podem indicar um ataque ou uma falha; e (3) usar os nomes do ATT&CK for ICS para descrever o que viu.

### 14.1 Conhecer o normal

Os operadores conhecem o som, o ritmo e as telas da linha. Os técnicos acrescentam o normal da rede e dos sistemas: quais dispositivos conversam, quais contas entram, com que frequência os programas mudam. Ponha isso por escrito; o "normal" guardado só na cabeça das pessoas desaparece nas trocas de turno.

Na HPFL, Tomás já anotou que as escritas vêm só da HMI-1 e do ENG-LT. Anotações semelhantes podem cobrir os horários típicos de login, a frequência com que os programas dos CLPs mudam e quais dispositivos aparecem na rede. Guarde-as no registro de ativos ou num documento compartilhado, datadas e atualizadas depois de mudanças.

### 14.2 Sinais a relatar

Um setpoint muda sem que ninguém aperte um botão. As telas da IHM congelam ou mostram valores que discordam dos instrumentos locais. Um download de programa aparece no registro sem um trabalho correspondente. Um dispositivo novo aparece na rede. Ocorrem sessões remotas fora de um chamado. A linha para sem causa mecânica.

Relate qualquer um desses com o horário, o dispositivo e o que você viu, e anexe fotografias ou linhas de registro quando puder. Na HPFL, uma divergência entre a HMI-1 e um termômetro portátil revelou-se um sensor com defeito, mas o relato ainda assim levou a um diagnóstico rápido.

### 14.3 Dar nome ao que você viu

O MITRE ATT&CK for ICS oferece nomes compartilhados: T0836 Modify Parameter para setpoints alterados, T0886 Remote Services para o uso indevido do acesso remoto, T0843 Program Download para mudanças inesperadas na lógica. Usar esses nomes num relato ajuda a equipe de segurança, mas relate o que observou, não um palpite sobre o atacante.

Os nomes ajudam quando os relatos são comparados entre turnos ou instalações. Escreva primeiro a observação e depois o nome da técnica, se couber: por exemplo, velocidade da embaladora alterada de 120 para 180 pelo admin às 07:45, o que corresponde a Modify Parameter. Deixe a intenção e a atribuição para a equipe de segurança.

### 14.4 Falha ou ataque?

A maioria dos eventos anormais são falhas ou erros. Isso não importa de início: a resposta é a mesma — manter as pessoas seguras, preservar as evidências, relatar. A causa é decidida depois.

Na HPFL, a divergência de temperatura era um sensor com defeito, e a mudança de velocidade era um ajuste bem-intencionado de um operador. Os dois foram tratados com os mesmos passos: deixar seguro, registrar, relatar. A causa foi encontrada depois, com as evidências que tinham sido guardadas. Tratar todo evento da mesma forma também evita constrangimentos: ninguém é acusado, e nada é descartado cedo demais.

### 14.5 O que não fazer

Não reinicie dispositivos, não apague registros, não desconecte cabos nem "conserte" valores antes que o supervisor e o engenheiro concordem; você poderia destruir as evidências do que aconteceu ou criar um novo perigo.

O supervisor decide se a linha continua funcionando; o engenheiro decide como examinar os dispositivos. A sua parte é fotografar, anotar o horário e ligar. Se um perigo exigir ação imediata, siga os procedimentos normais de segurança e registre o que fez. Na HPFL, Tomás fotografou as duas leituras de temperatura e ligou para o supervisor; não reinicializou o sensor. Essa contenção preservou as evidências que depois mostraram a causa.

### Exemplo resolvido (HPFL sintética)

A HMI-1 mostra a enchedora em temperatura normal, mas o termômetro portátil do operador marca 12 °C a mais. Tomás fotografa as duas leituras, anota o horário e liga para o supervisor, que para a enchedora com segurança. Depois, o engenheiro encontra um sensor com defeito — uma falha, não um ataque —, mas as evidências tornaram o diagnóstico rápido.

> **Caso sintético — HPFL.** As leituras são inventadas.

### Erros e limites

Uma lista de sinais nunca é completa; confie nos operadores experientes que dizem "isto não está certo". O ATT&CK descreve técnicas, não certezas sobre a intenção.

### Exercícios

- **EX053 — A IHM discorda do instrumento.** O que uma diferença entre a IHM e um instrumento local sugere, e qual é a primeira ação? *Rubrica:* 3 = falha de sensor ou tela manipulada; manter seguro/parar via supervisor, registrar evidências; 2 = uma parte; 1 = confiar na IHM; 0 = nenhum.
- **EX054 — Associar técnicas.** Associe ao ATT&CK for ICS: (a) download de programa não planejado; (b) sessão de fornecedor fora de chamado; (c) valor de velocidade alterado. *Rubrica:* 3 = T0843, T0886, T0836; 2 = dois; 1 = um; 0 = nenhum.
- **EX055 — A mesma resposta.** Por que a resposta inicial é a mesma para uma falha e para um ataque? *Rubrica:* 3 = segurança e evidências primeiro, causa desconhecida no início; 2 = parcial; 1 = "não é"; 0 = nenhum.
- **EX056 — Pôr o normal por escrito.** Dê três itens para uma folha de "normal" da HPFL. *Rubrica:* 3 = três itens específicos (quem conversa com quem, padrão de logins, frequência de mudanças etc.); 2 = dois; 1 = vago; 0 = nenhum.

### Síntese

Conhecer o normal permite perceber o anormal; responda pela segurança e pelas evidências antes de decidir a causa.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 18

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Relatar um incidente e primeiras ações

### Objetivos de aprendizagem

Você vai (1) seguir os passos de primeira resposta da HPFL; (2) escrever um primeiro relato claro; e (3) explicar por que as evidências são preservadas antes de a recuperação começar.

### 15.1 Primeiros passos

Deixe as pessoas seguras: o supervisor decide se para ou isola a parte afetada da linha, usando os procedimentos normais. Depois ligue para o contato de incidentes da ficha da instalação. Registre o que vê à medida que avança. Não tente remover malware nem restaurar sistemas você mesmo.

Na HPFL, o supervisor da noite passou a linha para o controle local pelo painel e parou a embaladora antes que algo mais acontecesse. Tomás então fotografou a tela e ligou para o contato de incidentes. Seguir os passos em ordem mantém as pessoas seguras e deixa as evidências intactas.

### 15.2 Um bom primeiro relato

Ele responde: o que você percebeu, onde, quando, quais dispositivos, o que a linha está fazendo agora, o que já foi feito e a quem você avisou. Fatos curtos valem mais do que teorias longas. A NIST SP 800-82r3 enfatiza que a resposta a incidentes de TO precisa ser planejada com as operações, porque ações tomadas em pânico podem prejudicar o processo.

Na HPFL, o relato de Tomás coube em uma frase por ponto e foi enviado em minutos. As correções posteriores foram acrescentadas por escrito, sem alterar o primeiro relato. Guarde uma cópia de todo relato que você enviar, com o horário.

### 15.3 Preservar as evidências

Fotografe as telas, mantenha uma linha do tempo escrita e deixe os dispositivos como estão, a menos que a segurança exija o contrário. Se um dispositivo precisar ser isolado, o engenheiro faz isso por um método planejado — por exemplo, desabilitando uma porta do switch — e registra exatamente quando.

Mantenha a linha do tempo escrita na ordem em que os eventos aconteceram, com horários de uma única referência, como o seu relógio, e anote as diferenças de relógio conhecidas entre os dispositivos. As fotografias devem mostrar juntos o nome do dispositivo e a tela. Guarde as fotografias com a linha do tempo, num só lugar.

### 15.4 Comunicação

Use a lista de contatos da instalação. Não publique nada sobre o incidente em redes sociais ou grupos de conversa. Não contate fornecedores ou autoridades por conta própria, a menos que o líder do incidente peça.

Na HPFL, o líder do incidente decide quem fala com fornecedores, clientes e autoridades. Evite especular com os colegas sobre a causa, porque os boatos se espalham depressa no chão de fábrica. Se alguém de fora perguntar sobre o incidente, encaminhe a pessoa ao líder do incidente. Use os telefones da ficha da instalação, não números salvos por conta própria, porque eles são mantidos atualizados.

### 15.5 Deveres de notificação

Alguns setores e países exigem relatos a reguladores ou à CISA em prazos definidos; o líder do incidente cuida disso, mas é a sua linha do tempo que torna isso possível.

Na HPFL, a linha do tempo de Tomás, com os seus horários e fotografias, deu ao líder do incidente o que era necessário para qualquer notificação exigida. Mantenha-a precisa e completa e passe as correções ao líder por escrito assim que as encontrar. Os horários são o que mais importa: quando o evento foi percebido, quando foi relatado e quando a linha foi parada. Anote-os à medida que acontecem, em vez de reconstruí-los depois.

### Exemplo resolvido (HPFL sintética)

Às 03:10, a HMI-1 mostra uma mensagem de resgate. Tomás avisa o supervisor da noite, que passa a linha para o controle local pelo painel e para a embaladora. Tomás fotografa a tela e liga para o contato de incidentes às 03:14. Seu relato diz: "03:10 tela de resgate na HMI-1; linha em controle local, embaladora parada às 03:12; nenhuma outra tela afetada vista; nada desconectado; supervisor informado."

> **Caso sintético — HPFL.** O incidente é inventado.

### Erros e limites

As listas de contatos ficam desatualizadas; confira-as trimestralmente. Um primeiro relato pode estar errado; corrija-o por escrito, em vez de apagá-lo.

### Exercícios

- **EX057 — Ordenar os passos.** Ponha em ordem: ligar para o contato de incidentes; o supervisor deixa a linha segura; fotografar a tela; restaurar a IHM. *Rubrica:* 3 = segurança, fotografar, ligar; restaurar depois, pelos responsáveis; 2 = quase certo; 1 = restaurar primeiro; 0 = nenhum.
- **EX058 — Melhorar um relato.** Reescreva "a IHM foi hackeada, provavelmente russos" como um primeiro relato factual. *Rubrica:* 3 = horário, dispositivo, observação, estado da linha, ações, quem foi avisado; sem especulação; 2 = parcial; 1 = ainda especulação; 0 = nenhum.
- **EX059 — Desconectar.** Um colega quer desconectar imediatamente o cabo de rede da HMI-1. O que você diz? *Rubrica:* 3 = isolar só via supervisor/engenheiro, de forma planejada e registrada; segurança e evidências; 2 = esperar; 1 = fazer; 0 = nenhum.
- **EX060 — Quem notifica.** Quem decide se é preciso notificar os reguladores ou a CISA? *Rubrica:* 3 = o líder do incidente/a direção; o técnico fornece a linha do tempo; 2 = só o líder; 1 = o técnico sozinho; 0 = nenhum.

### Síntese

Segurança primeiro, fatos registrados, evidências preservadas, as pessoas certas chamadas; a recuperação vem depois.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 18

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Recuperação e retorno à produção

### Objetivos de aprendizagem

Você vai (1) descrever os passos para restaurar uma linha depois de um incidente; (2) verificar os sistemas restaurados antes de religar; e (3) explicar por que as lições aprendidas precisam mudar alguma coisa.

### 16.1 Ordem da recuperação

A recuperação é planejada pelo líder do incidente, pelo engenheiro de controle e pelas operações. Normalmente: confirmar que a causa está contida, reconstruir os computadores afetados a partir de imagens íntegras conhecidas, restaurar os programas dos CLPs a partir de cópias verificadas (Capítulo 11), trocar as senhas que possam ter sido expostas e, depois, testar.

Na HPFL, a HMI-1 foi reconstruída a partir da imagem do fornecedor, os dois programas dos CLPs foram comparados com cópias correspondentes e a senha de administrador foi trocada. Seguir a ordem evita religar com um problema ainda presente. Cada passo é registrado com o horário e a pessoa que o executou.

### 16.2 Verificação antes de religar

Compare os programas restaurados dos CLPs com as cópias verificadas, confira se as telas da IHM mostram valores corretos em relação aos instrumentos locais, confirme que as regras do firewall correspondem à tabela aprovada e rode a linha vazia num ciclo de teste. A qualidade aprova antes que o produto passe.

Na HPFL, o ciclo de teste rodou vazio por 30 minutos, e a qualidade aprovou às 11:20, antes de a produção ser retomada. Registre cada verificação e o seu resultado no arquivo do incidente. Se alguma verificação falhar, a linha não religa até que a causa seja entendida. Guarde os resultados das comparações com o arquivo do incidente.

### 16.3 Vigiar depois

Os atacantes às vezes voltam. Durante dias depois de religar, vigie mais de perto os logins, as sessões remotas e os dispositivos novos, e relate imediatamente qualquer coisa incomum.

Combine com o supervisor quanto tempo dura o período de vigilância e quem revisa os registros a cada dia. Na HPFL, a reunião de lições aprendidas encontrou uma porta de área de trabalho remota alcançável pela internet, aberta por um empreiteiro, o que torna especialmente importante vigiar de perto as sessões remotas. Relate qualquer coisa incomum ao líder do incidente, não só ao seu turno. Anote no arquivo do incidente a data de fim do período de vigilância, para que ele não caduque em silêncio.

### 16.4 Lições aprendidas

Uma reunião curta, em até duas semanas, responde: o que aconteceu, o que funcionou, o que não funcionou, o que muda. Cada mudança tem um responsável e uma data. Uma sessão de lições aprendidas que não muda nada fracassou.

Na HPFL, a reunião de lições aprendidas atribuiu ao dono da rede o fechamento da porta de área de trabalho remota da HMI-1 e uma verificação mensal. Cada ação é acompanhada até ser concluída e mostrar-se eficaz, e as notas da reunião são guardadas com o arquivo do incidente. Convide os operadores que estavam no turno; eles muitas vezes sabem o que funcionou.

### 16.5 Guarda de registros

Mantenha juntos a linha do tempo, as fotografias, as decisões e os resultados dos testes. Eles sustentam o seguro, os reguladores e a próxima melhoria.

Guarde os registros juntos numa pasta ou num chamado, com acesso limitado a quem precisa deles. Inclua o primeiro relato, as suas correções, as fotografias e os resultados do ciclo de teste. A próxima vistoria pode então verificar se as lições foram aplicadas. Guarde os registros pelo tempo que a política da instalação exigir e anote quem pode lê-los. Quando uma seguradora ou um regulador fizer uma pergunta meses depois, a resposta deve vir desses registros, e não da memória, que se apaga depressa.

### 16.6 Comunicar o retorno

Diga a todos os turnos o que mudou: senhas novas, telas que parecem diferentes e quais sinais incomuns relatar durante o período de vigilância.

Na HPFL, isso significou dizer a todos os turnos que a senha de administrador tinha mudado e que sessões remotas inesperadas ou dispositivos novos deviam ser relatados. Uma nota escrita curta deixada na HMI-1, sem senhas, ajuda quem perdeu o briefing. Faça o briefing dos dois turnos seguintes pessoalmente, se possível, e peça que confirmem que entenderam. As perguntas levantadas nesses briefings muitas vezes mostram onde o procedimento precisa ficar mais claro, então registre-as também.

### Exemplo resolvido (HPFL sintética)

Depois do incidente de resgate, a HMI-1 é reconstruída a partir da imagem do fornecedor; os dois programas dos CLPs são comparados com cópias correspondentes e encontrados inalterados. A senha de administrador é trocada. Um ciclo de teste roda vazio por 30 minutos, a qualidade aprova às 11:20 e a produção é retomada. A reunião de lições aprendidas descobre que a HMI-1 tinha uma porta de área de trabalho remota alcançável pela internet, aberta por um empreiteiro; a ação — fechá-la e acrescentar uma verificação mensal — é atribuída ao dono da rede.

> **Caso sintético — HPFL.** A recuperação é inventada.

### Erros e limites

Restaurar a partir de uma cópia feita depois do comprometimento recarrega o problema; datas e hashes verificados importam. A pressão para religar depressa é real; o ciclo de teste é inegociável.

### Exercícios

- **EX061 — Ordem da recuperação.** Ponha em ordem: ciclo de teste; reconstruir a IHM; aprovação da qualidade; trocar as senhas; confirmar a contenção. *Rubrica:* 3 = contenção, reconstrução, senhas, teste, aprovação; 2 = quase; 1 = aleatório; 0 = nenhum.
- **EX062 — Verificações.** Nomeie três verificações antes de religar a linha. *Rubrica:* 3 = programas vs cópia verificada, IHM vs instrumentos, regras do firewall, ciclo de teste vazio; 2 = duas; 1 = uma; 0 = nenhum.
- **EX063 — Cópia ruim.** Por que restaurar uma cópia do dia do incidente poderia ser um erro? *Rubrica:* 3 = pode conter a mudança do atacante; usar a cópia verificada de antes do incidente; 2 = parcial; 1 = sem problema; 0 = nenhum.
- **EX064 — Transformar uma lição em ação.** Escreva a ação da reunião de lições aprendidas da HPFL no formato responsável/data. *Rubrica:* 3 = fechar a porta de RDP + verificação mensal, dono da rede, data; 2 = sem responsável/data; 1 = "ter cuidado"; 0 = nenhum.

### Síntese

Recupere em ordem, verifique antes de religar, vigie depois e transforme as lições em ações com dono.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 18

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Gestão de mudanças e documentação

### Objetivos de aprendizagem

Você vai (1) explicar por que toda mudança na linha precisa de um chamado; (2) escrever uma solicitação de mudança com um plano de reversão; e (3) manter os desenhos e os registros em dia com a realidade.

### 17.1 Por que o controle de mudanças é segurança

A maioria dos problemas nas plantas vem de mudanças que ninguém registrou: uma regra de firewall acrescentada às pressas, um programa editado durante uma pane, uma câmera parafusada por um empreiteiro. Controle de mudanças significa que toda mudança é solicitada, revisada, aprovada, executada e registrada. Ele também facilita perceber uma mudança não registrada, que pode ser o primeiro sinal de um ataque.

Na HPFL, vários problemas deste livro começaram como mudanças não registradas: o programa da embaladora editado no Capítulo 11, a regra temporária de firewall no Capítulo 12 e a porta de área de trabalho remota no Capítulo 16. Cada uma teria ficado visível mais cedo com um chamado.

### 17.2 Uma solicitação de mudança

Ela declara o que vai mudar, por quê, quais dispositivos, quem faz, quando, o risco para o processo, como o sucesso é verificado e como desfazer. Mudanças emergenciais durante uma pane são permitidas, mas são registradas depois, em até um turno.

Na HPFL, a solicitação de Tomás para a atualização da VIS-CAM cobriu tudo isso em poucas linhas. Mantenha o formulário curto, para que as pessoas realmente o usem. O aprovador verifica se o teste de sucesso e a reversão são realistas antes de concordar.

### 17.3 Reversão

Antes da mudança, salve o programa ou a configuração atual e o seu hash. Se a verificação falhar, restaure-o. Uma mudança sem reversão é uma aposta.

Na HPFL, a reversão da VIS-CAM era reinstalar o firmware 1.0.7 a partir de um arquivo salvo, com o seu hash registrado. Teste se o arquivo salvo está completo antes de começar a mudança. Se a própria reversão falhar, pare e chame o engenheiro de controle. Na HPFL, os hashes dos arquivos salvos eram registrados no chamado de mudança, para que um arquivo restaurado pudesse ser verificado antes de ser carregado. Sem isso, uma reversão poderia carregar uma cópia corrompida ou editada sem que ninguém percebesse.

### 17.4 Manter os documentos atualizados

Atualize o registro de ativos, o desenho da rede e a tabela de regras no mesmo chamado. Marque os desenhos com um número de revisão e uma data.

Na HPFL, o desenho da rede ainda estava na revisão 3, enquanto a VLAN de IoT aparecia apenas nos rascunhos da revisão 4, o que a vistoria final encontrou. Atualizar os documentos no mesmo chamado impede que essa lacuna se abra. Quando um desenho mudar, marque a revisão antiga como substituída e guarde-a, para que as decisões passadas ainda possam ser entendidas. Confira os números de revisão em cada vistoria; um desenho cuja revisão está atrás da realidade é, ele mesmo, uma constatação, como a HPFL aprendeu.

### 17.5 Revisores

Quem faz uma mudança não deve ser a única pessoa a aprová-la. Na HPFL, o engenheiro de controle revisa as mudanças de programas, o dono da rede revisa as mudanças de firewall e de switches, e o supervisor confirma a janela de produção. Um segundo par de olhos pega erros de digitação em endereços e valores antes que cheguem à linha.

Registre o nome do revisor no chamado. Se a única pessoa capaz de revisar estiver indisponível, espere a próxima janela, a menos que a mudança seja emergencial.

### Exemplo resolvido (HPFL sintética)

O fornecedor da câmera de visão precisa do firmware 1.1.0 na VIS-CAM. Tomás escreve: "Mudança 512 — atualizar a VIS-CAM de 1.0.7 para 1.1.0 para correção da precisão de rejeição; pelo técnico de qualidade; terça-feira, 06:00, parada planejada; risco: as rejeições deixam de funcionar; verificação: 20 embalagens de teste, incluindo 5 selagens ruins rejeitadas; reversão: reinstalar a 1.0.7 a partir do arquivo salvo, hash registrado." A atualização passa na verificação, e o registro de ativos mostra 1.1.0.

> **Caso sintético — HPFL.** A mudança e a correção do fornecedor são inventadas.

### Erros e limites

O controle de mudanças pode virar um exercício de papelada; mantenha os formulários curtos e exija os campos-chave. As mudanças emergenciais não devem virar o caminho normal.

### Exercícios

- **EX065 — Campos de uma solicitação.** Liste seis campos de uma solicitação de mudança. *Rubrica:* 3 = o quê, por quê, dispositivos, quem, quando, risco, verificação, reversão (quaisquer seis); 2 = quatro; 1 = dois; 0 = nenhum.
- **EX066 — Edição durante a pane.** O engenheiro edita o PLC-FILL durante uma pane às 2 da manhã. O que precisa acontecer depois? *Rubrica:* 3 = registrada como mudança emergencial dentro do turno, nova cópia e hash, registro de ativos atualizado; 2 = só registrar; 1 = nada; 0 = nenhum.
- **EX067 — Verificação reprovada.** O teste da VIS-CAM deixa passar 2 de 5 selagens ruins. O que acontece em seguida? *Rubrica:* 3 = reverter para a 1.0.7, verificar, registrar a falha, contatar o fornecedor; 2 = reverter; 1 = rodar mesmo assim; 0 = nenhum.
- **EX068 — Mudança não registrada.** Por que vale relatar uma mudança não registrada, mesmo que pareça inofensiva? *Rubrica:* 3 = pode ser não autorizada/sinal de ataque; quebra a linha de base e as cópias; 2 = um; 1 = ignorar; 0 = nenhum.

### Síntese

Mudanças solicitadas, revisadas, reversíveis e registradas mantêm a linha conhecida; as não registradas são avisos.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 18

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Projeto final: uma vistoria de segurança da linha

### Objetivos de aprendizagem

Você vai (1) combinar as habilidades do livro numa vistoria planejada; (2) produzir uma lista curta de constatações com prioridades; e (3) apresentá-la ao supervisor e ao engenheiro.

### 18.1 Planejamento

Combine com o supervisor o escopo, a data e a permissão: quais armários, quais registros, nenhuma conexão a dispositivos, condições de parada. Leve o registro de ativos, o desenho da rede, a tabela de regras e os registros de mídias e de acesso remoto.

Escreva o plano na permissão: a janela de tempo, os armários a serem abertos por um eletricista, os registros a verificar e as condições de parada. Na HPFL, a vistoria teve uma permissão de duas horas. Combine de antemão quem vai receber as constatações e quando. Marque a data com bastante antecedência, para que as operações possam se planejar.

### 18.2 O que verificar

Físico: armários trancados, nenhum modem ou switch sem explicação, nenhuma senha nos painéis, nenhum pen drive solto. Registros: registro de ativos completo, cópias recentes e hashes correspondentes, alertas registrados, mudanças encerradas. Acesso: contas de fornecedores desabilitadas fora das sessões, uso de administrador limitado.

Use uma lista de verificação, para que nada passe e para que a próxima vistoria possa ser comparada com esta. Na HPFL, a lista de verificação levou Tomás ao modem no armário da enchedora, às assinaturas antigas do antimalware do ENG-LT, ao desenho desatualizado e a um pen drive de receita ausente do livro de mídias.

### 18.3 Escrever as constatações

Cada constatação: o que você viu, onde, por que importa (consequência), a correção sugerida, o responsável. Guarde as evidências (fotografias, trechos de registros) junto com ela.

Escreva as constatações durante a vistoria ou logo depois, enquanto os detalhes estão frescos. Na HPFL, a constatação do modem celular incluiu a sua localização no armário da enchedora, uma fotografia e a consequência de que alguém poderia alcançar a enchedora de fora. Cada constatação precisa de um responsável que concorde em agir. Mantenha cada constatação em poucas linhas, para que possa ser lida depressa na reunião. Separe o que você viu do que acha que significa.

### 18.4 Priorizar

Ordene pela consequência e pela facilidade: qualquer coisa que dê um caminho não revisado até os CLPs vem primeiro; as arrumações, por último. Apresente com clareza as três primeiras; listas longas escondem os itens importantes.

Na HPFL, o modem veio primeiro, porque era um caminho não revisado até um CLP. As assinaturas antigas do antimalware do ENG-LT vieram em segundo, porque esse notebook programa os CLPs. O pen drive ausente e o desenho desatualizado vieram em seguida. Escreva uma razão de uma linha para cada posição. Combine a ordem com o supervisor, que pode conhecer razões de produção para mudá-la.

### 18.5 Acompanhamento

Combine responsáveis e datas na reunião e depois verifique o progresso mensalmente.

Registre os responsáveis e as datas numa lista curta compartilhada com o supervisor. A cada verificação mensal, anote o que foi concluído e o que atrasou, com o motivo. Na HPFL, a próxima vistoria deve começar confirmando que o modem do armário da enchedora foi desconectado ou posto sob controle. As constatações que continuam atrasando são levadas ao supervisor, em vez de serem carregadas adiante em silêncio. Encerre cada item apenas com evidência de que foi feito.

### 18.6 Apresentar ao supervisor

Use linguagem simples e as consequências com que o supervisor se importa: "este modem pode deixar alguém mudar a enchedora de fora" funciona melhor do que nomes de protocolos. Leve fotografias, limite-se a dez minutos e termine com as decisões de que precisa: responsável, data e qualquer janela de produção. Agradeça aos operadores que ajudaram; a cooperação deles decide se a próxima vistoria será bem-vinda.

Envie depois um resumo escrito curto com as constatações, os responsáveis e as datas. Guarde uma cópia do resumo com as evidências da vistoria, para que a próxima vistoria possa começar verificando o que mudou desde então. Se o supervisor não concordar com uma posição da lista, registre a discordância e o motivo.

### Exemplo resolvido (HPFL sintética)

A vistoria de Tomás, sob uma permissão de duas horas, encontra: (1) um modem celular conectado dentro do armário da enchedora e ausente do registro de ativos; (2) assinaturas do antimalware do ENG-LT com 40 dias; (3) o desenho da rede na revisão 3, enquanto a VLAN de IoT existe apenas nos rascunhos da revisão 4; (4) um pen drive de receita ausente do livro de mídias. Ele classifica o modem em primeiro, o notebook em segundo, o pen drive em terceiro e o desenho em quarto, e o supervisor atribui os responsáveis.

> **Caso sintético — HPFL.** As constatações são inventadas.

### Erros e limites

Uma vistoria é um retrato instantâneo; os problemas voltam sem repetição regular. Ela não substitui uma avaliação profissional segundo a IEC 62443.

### Exercícios

- **EX069 — Escopo da permissão.** Escreva o escopo e três condições de parada para a vistoria. *Rubrica:* 3 = áreas, registros, nenhuma conexão a dispositivos, três paradas específicas; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX070 — Formato da constatação.** Reescreva "modem ruim" como uma constatação completa. *Rubrica:* 3 = o quê/onde/por quê/correção/responsável/evidência; 2 = quatro partes; 1 = duas; 0 = nenhum.
- **EX071 — Classificação.** Justifique classificar o modem acima das assinaturas antigas do antimalware. *Rubrica:* 3 = o modem é um caminho não revisado e ativo até os CLPs; o notebook só é arriscado quando conectado e é controlado; 2 = parcial; 1 = invertido; 0 = nenhum.
- **EX072 — Plano de acompanhamento.** Como Tomás deve garantir que as quatro constatações sejam realmente corrigidas? *Rubrica:* 3 = responsáveis e datas combinados, acompanhados, verificação mensal, evidência de encerramento; 2 = parte; 1 = "lembrar as pessoas"; 0 = nenhum.

### Síntese

Uma vistoria planejada liga inventário, acesso, cópias de segurança, mudanças e evidências em correções classificadas e com dono.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 18

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX072. A Harbor Point Food Packaging Line, Tomás Reyes e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O PLC-FILL controla a enchedora; o PLC-WRAP aciona os motores e os aquecedores da embaladora; a HMI-1 mostra o estado e recebe os comandos dos operadores; a VIS-CAM inspeciona as selagens e rejeita as embalagens ruins; o ENG-LT guarda e altera os programas dos CLPs.

**EX002.** Reiniciar um PC de escritório perde no máximo o trabalho não salvo, enquanto reiniciar o PLC-WRAP para motores e aquecedores no meio do ciclo, pode emperrar o filme ou deixar o produto inseguro, e precisa seguir o procedimento de parada da linha com a concordância das operações.

**EX003.** Uma temperatura de selagem muito mais alta pode chamuscar o filme, iniciar um incêndio ou queimar um trabalhador que esteja desobstruindo um emperramento, e pode produzir embalagens danificadas ou mal seladas que precisam ser rejeitadas como riscos à segurança dos alimentos.

**EX004.** T0836 Modify Parameter; sim — um operador que digita um valor errado causa o mesmo efeito físico, e é por isso que as mudanças são registradas e verificadas, seja qual for a causa.

**EX005.** Recusar e interromper o plano: a cortina de luz é uma função de segurança que nunca deve ser contornada para trabalho de segurança cibernética; relatar a sugestão ao supervisor e encontrar uma abordagem de teste que deixe a segurança intacta, como observar a partir de uma porta espelhada durante uma parada planejada.

**EX006.** Um notebook conectado pode fazer broadcast, solicitar endereços ou rodar software que envia tráfego ao PLC-WRAP, o que pode deixar a comunicação dele mais lenta ou alterar a lógica; assim, o processo pode ser afetado, e o trabalho precisa ser planejado e autorizado.

**EX007.** (a) O supervisor do turno; (b) o engenheiro de controle, dono dos programas dos CLPs; (c) o gerente de qualidade.

**EX008.** Parar se o supervisor ou um operador pedir; parar se algum condutor energizado ou peça móvel ficar exposto além da vista combinada; parar se um alarme sem explicação aparecer na HMI-1 enquanto a porta estiver aberta.

**EX009.** Não. Com máscara /24, os três primeiros octetos são a rede; 10.20.1 e 10.20.2 diferem, então o tráfego entre eles precisa passar por um roteador ou firewall.

**EX010.** A impressora ficaria na VLAN da linha com alcance direto aos CLPs e à HMI-1, contornando as regras do FW-1; qualquer comprometimento da impressora, ou usuários do escritório imprimindo nela, criaria um caminho que ninguém revisou.

**EX011.** "ENG-LT (o seu endereço de escritório) → PLC-FILL e PLC-WRAP apenas na porta de programação, permitir", seguida de "qualquer → 10.20.1.0/24 negar", para que nada mais do escritório alcance a linha.

**EX012.** Qualquer pessoa com um cabo pode entrar na rede da linha por ele, ele não tem VLANs nem registros, e pode ligar o armário a dispositivos que não estão em nenhum desenho; assim, cria conexões que ninguém revisa.

**EX013.** Ele define imediatamente o valor de velocidade da embaladora como 180; o motor acelera sem nenhuma confirmação adicional, o que pode causar emperramentos ou tensão insegura no filme.

**EX014.** O Modbus clássico não verifica identidade, então qualquer coisa que alcance a porta 502 pode ler e possivelmente escrever valores do PLC-FILL; um tablet de fornecedor não gerenciado poderia alterar a enchedora por engano ou se estivesse comprometido.

**EX015.** (b) A VIS-CAM escrevendo no PLC-WRAP: a câmera só deve enviar sinais de rejeição pelo seu caminho definido, e uma escrita vinda dela está fora do padrão esperado da HMI-1 e do ENG-LT.

**EX016.** Num simulador de protocolo ou num CLP de laboratório numa bancada isolada, porque qualquer requisição à linha pode alterar saídas reais e parar ou pôr em perigo a produção.

**EX017.** A versão do firmware (para comparar com os alertas) e a marca e o modelo exatos (os alertas citam produtos específicos); sem eles, não é possível decidir se o PLC-WRAP é afetado.

**EX018.** `complete: 4 of 5` — a HMI-1 passa a OK, mas o PLC-WRAP ainda imprime `MISSING fw`.

**EX019.** Um chamado de mudança que instala, move ou substitui um dispositivo não pode ser encerrado até que o registro do ativo seja atualizado e o nome de quem o atualizou seja anotado no chamado.

**EX020.** Ele lista o endereço, o modelo e o firmware de cada dispositivo, o que diz a um atacante exatamente quais alvos existem e quais fraquezas conhecidas tentar.

**EX021.** Todas as ações aparecem sob um único nome, então o registro não consegue mostrar qual pessoa alterou um valor de referência; os investigadores precisam reconstruí-lo a partir das escalas dos turnos e da memória, o que é lento e pouco confiável.

**EX022.** As senhas padrão estão em manuais públicos, e linhas "isoladas" ainda recebem notebooks de empreiteiros, dispositivos USB e conexões remotas; qualquer pessoa com algum alcance consegue entrar sem esforço.

**EX023.** Fotografar o bilhete como evidência, removê-lo, avisar o supervisor e o engenheiro de controle e escrever um relato curto; o engenheiro troca a senha numa parada planejada e revisa os logins recentes de administrador.

**EX024.** Não. O monitoramento de rotina precisa apenas de direitos de visualização; usar administrador diariamente torna mais prováveis as mudanças acidentais e os danos de uma sessão roubada, então o administrador fica reservado ao trabalho planejado.

**EX025.** Deixá-lo desconectado, anotar onde e quando foi encontrado e entregá-lo à segurança ou ao supervisor; pen drives deixados com rótulos tentadores são um truque conhecido para levar alguém a conectá-los.

**EX026.** Identificador do pen drive, nomes dos arquivos, resultado da varredura, a pessoa que o manuseou e a data e a hora.

**EX027.** "Limpo" significa que o antivírus não encontrou malware conhecido; malware novo ou não reconhecido ainda pode passar, então o arquivo tem risco menor, não é seguro, e o registro mantém um rastro caso surjam problemas.

**EX028.** Usar um notebook gerenciado, da própria instalação, com o software do fornecedor instalado, ou ter os arquivos do fornecedor verificados e levados num pen drive da instalação, para que o notebook não gerenciado nunca se conecte à linha.

**EX029.** Usar autenticação multifator; usar senhas fortes para a área de trabalho remota; fechar as portas de área de trabalho remota não usadas; auditar a atividade de conexões remotas.

**EX030.** Uma conexão permanentemente habilitada pode ser usada por qualquer pessoa que tenha as credenciais do fornecedor, a qualquer hora, sem ninguém observando; assim, uma senha roubada vira um caminho imediato até a linha.

**EX031.** Fornecedor e conta usados, início às 14:00 e fim às 14:38, "apenas visualizou o registro de falhas da embaladora, sem alterações", conta desabilitada, operador confirmou funcionamento normal.

**EX032.** Um modem dá uma rota até a linha que pula o gateway, o MFA e o registro; Tomás deve fotografá-lo e relatá-lo ao supervisor e ao engenheiro de controle, em vez de desconectá-lo ele mesmo.

**EX033.** `06:15 low-film` e `08:10 jam-cleared` são alarmes de processo; os logins às 06:02 e das 07:40 às 07:43 e a mudança do valor de referência às 07:45 são relevantes para a segurança.

**EX034.** `failed logins: 5` — o contador aumenta a cada linha de login terminada em "fail".

**EX035.** Um sucesso logo depois de falhas repetidas sugere que a senha foi adivinhada ou encontrada, e dois minutos depois a mesma conta alterou a velocidade da embaladora; sozinho, um login de administrador poderia ser simplesmente trabalho planejado.

**EX036.** Às 07:45, no PLC-WRAP, o valor de referência de velocidade mudou de 120 para 180 pela conta de administrador; essa conta entrou às 07:43, depois de três falhas desde as 07:40; nenhuma mudança planejada era conhecida.

**EX037.** Produto e modelo; versões afetadas; o que um atacante poderia fazer; se é preciso acesso pela rede ou físico; a correção ou a medida de contorno do fornecedor.

**EX038.** Não. Só as versões anteriores à 2.2 são afetadas, e o PLC-FILL roda a 3.2; registrar "não se aplica — rodando a 3.2" com a data e quem verificou.

**EX039.** Atualizar o CLP exige uma parada de produção, testes com o programa e verificações de qualidade, que levam semanas para organizar; restringir a porta de programação no FW-1 reduz a exposição hoje.

**EX040.** "Aplica-se: PLC-WRAP fw 2.0. Mitigação: o FW-1 permite a porta de programação apenas a partir do ENG-LT. Atualizar para 2.3 na parada planejada daqui a três semanas. Responsável: engenheiro de controle. Revisar se a mitigação mudar."

**EX041.** Os programas do PLC-FILL e do PLC-WRAP, o projeto da HMI-1, os arquivos de receita, as configurações do FW-1 e dos switches e os ajustes da VIS-CAM.

**EX042.** Ele não a restaura; marca-a como suspeita, relata a divergência ao engenheiro de controle e ajuda a localizar uma cópia mais antiga cujo hash corresponda.

**EX043.** Ele imprime um prefixo de hash de 12 caracteres diferente para `PLC-FILL_2026-09.bak` e `MISMATCH - do not restore`, porque qualquer alteração muda o valor SHA-256.

**EX044.** Quem conseguir modificar as cópias no mesmo lugar também poderia reescrever os hashes guardados para que correspondam, então a verificação não provaria nada.

**EX045.** Zona da linha — PLC-WRAP; DMZ — a cópia do historiador ou o gateway de acesso remoto; zona de escritório — os PCs da equipe.

**EX046.** É permitido: a regra 3 casa o tráfego do escritório para qualquer coisa na linha antes de se chegar à negação final, então a HMI-1 é alcançável a partir de todo PC do escritório.

**EX047.** Os sistemas da linha enviam dados para um servidor na DMZ; os usuários do escritório conectam-se apenas a esse servidor, então não há regra que permita aos computadores do escritório iniciar conexões para dentro da zona da linha.

**EX048.** Abrir um chamado de mudança, confirmar com o dono da rede que nada depende da regra 3, agendar uma parada planejada, guardar a configuração antiga como reversão, remover a regra, verificar que os fluxos da linha e da DMZ funcionam e registrar o resultado.

**EX049.** Um medidor inteligente de energia conectado à nuvem, um tablet da equipe de qualidade e uma impressora de etiquetas Wi-Fi.

**EX050.** Cada dispositivo tem uma senha única, em vez de um padrão universal? Como relatamos uma vulnerabilidade a vocês? Por quanto tempo serão fornecidas atualizações de segurança? A comunicação é criptografada? O dispositivo pode ser reiniciado e os nossos dados apagados?

**EX051.** Numa VLAN de IoT dedicada, cujas regras de firewall permitem apenas os endereços de nuvem do fornecedor e bloqueiam toda rota para a zona da linha, os CLPs e a HMI-1.

**EX052.** Marcar a impressora como "fim de suporte" no registro, com a data, anotar o risco, mantê-la isolada no mínimo de tráfego necessário e abrir uma compra de substituição com uma data-alvo.

**EX053.** Ou o sensor ou o mostrador está errado, o que pode ser um sensor com defeito ou um valor manipulado; Tomás registra as duas leituras com a hora, e o supervisor leva a enchedora a uma parada segura antes que alguém faça o diagnóstico.

**EX054.** (a) T0843 Program Download; (b) T0886 Remote Services; (c) T0836 Modify Parameter.

**EX055.** No início ninguém conhece a causa, e nos dois casos as pessoas e o produto precisam ser mantidos seguros e as evidências preservadas para quem fizer o diagnóstico; tratar uma falha como ataque custa pouco, o contrário pode custar muito.

**EX056.** Apenas a HMI-1 e o ENG-LT escrevem nos CLPs; os logins de administrador acontecem apenas durante trabalho com chamado; os programas dos CLPs mudam cerca de uma vez por mês, em paradas planejadas.

**EX057.** O supervisor deixa a linha segura; Tomás fotografa a tela; ele liga para o contato de incidentes; a restauração da HMI-1 acontece depois, decidida pelo líder do incidente e pelo engenheiro.

**EX058.** "03:10, a HMI-1 mostra uma mensagem de resgate. Linha em controle local, embaladora parada às 03:12. Nenhuma outra tela afetada vista. Nada foi desconectado. Supervisor noturno informado; contato de incidentes acionado às 03:14."

**EX059.** Pedir que ele espere o supervisor e o engenheiro: puxar o cabo pode derrubar o painel do qual os operadores dependem e perde informação; o isolamento é feito por um método planejado, como desabilitar a porta do switch, com a hora registrada.

**EX060.** O líder do incidente, com a direção da instalação, decide; a linha do tempo e as fotografias de Tomás dão a eles os fatos de que precisam para cumprir qualquer prazo.

**EX061.** Confirmar a contenção; reconstruir a HMI-1; trocar as senhas; rodar o ciclo de teste; a qualidade aprova.

**EX062.** Comparar os programas dos CLPs com as cópias verificadas; conferir os valores da IHM com os instrumentos locais; confirmar que as regras do FW-1 correspondem à tabela aprovada (e rodar um ciclo de teste vazio).

**EX063.** Uma cópia feita no dia do incidente pode já conter as mudanças ou o malware do atacante, então restaurá-la reinstala o problema; usar a cópia mais recente verificada como feita antes do comprometimento.

**EX064.** "Fechar a porta de área de trabalho remota da HMI-1 e acrescentar uma verificação mensal de exposição externa — responsável: dono da rede — prazo: duas semanas."

**EX065.** O que muda, por quê, quais dispositivos, quem faz, quando, risco para o processo, verificação de sucesso, método de reversão.

**EX066.** A mudança é registrada como mudança emergencial antes do fim do turno, uma nova cópia com o seu hash é guardada, e o registro ou os desenhos são atualizados se algo mudou.

**EX067.** Parar o teste, reinstalar a 1.0.7 a partir do arquivo salvo, confirmar com embalagens de teste que as rejeições voltaram a funcionar, registrar a tentativa fracassada na mudança 512 e enviar o resultado ao fornecedor.

**EX068.** Ninguém consegue dizer se ela foi autorizada; pode ser uma mudança de um atacante, e significa que as cópias e a linha de base do normal já não correspondem à linha.

**EX069.** Escopo: armários da enchedora e da embaladora, área da HMI-1, o registro de ativos, as cópias, os registros de mídias e de acesso remoto; nenhuma conexão a qualquer dispositivo. Parar se aparecer um alarme sem explicação, se o supervisor ou os operadores pedirem, ou se um armário mostrar um perigo energizado além do que a permissão cobre.

**EX070.** "Modem celular conectado dentro do armário do PLC-FILL (foto 3); dá uma rota não gerenciada até a linha, contornando o FW-1 e o gateway remoto; correção: o engenheiro de controle confirma a finalidade, desconecta-o ou o coloca atrás do gateway; responsável: engenheiro de controle."

**EX071.** O modem é uma conexão ativa e não revisada que poderia alcançar os CLPs a qualquer momento, enquanto o ENG-LT só toca a linha sob permissão e as suas assinaturas podem ser atualizadas antes do próximo uso.

**EX072.** Combinar na reunião um responsável e uma data para cada item, registrá-los na planilha de acompanhamento, verificar mensalmente e encerrar cada um apenas com evidência, como uma fotografia ou um registro atualizado.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; verifique novamente as edições antes de citar.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0836 Modify Parameter, T0843 Program Download, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- Modbus Organization. Modbus specifications. <https://www.modbus.org/modbus-specifications>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
