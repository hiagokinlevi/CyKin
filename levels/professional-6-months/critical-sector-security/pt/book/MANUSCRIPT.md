# Infraestrutura Crítica e Segurança Setorial: Coordenação, Governança e Exercícios para Profissionais

- Idioma: português do Brasil (`pt`); curso profissional, seis meses; aproximadamente 360 horas de estudo planejado (curso 046 de 207 da [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito, cinco laboratórios offline, os exercícios EX001–EX060 e as resoluções correspondentes. Revisão independente por especialistas, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: profissionais em início de carreira que vão **coordenar** a segurança numa organização que presta um serviço essencial — coordenadores de segurança ou de resiliência recém-nomeados, supervisores de operações que herdaram atribuições cibernéticas, responsáveis por risco e conformidade, planejadores de continuidade e gerentes de projeto em água, energia, saúde, transporte, finanças e serviços públicos. Conhecimento de entrada: noções básicas de segurança e uma compreensão prática de como o serviço em questão é prestado.
- Como este curso difere dos vizinhos. O [livro técnico](../../../../technical-18-months/critical-sector-security/en/book/MANUSCRIPT.md) ensina profundidade prática: decodificar protocolos, endurecer hosts, configurar firewalls. O [livro de tecnólogo](../../../../technologist-3-years/critical-sector-security/en/book/MANUSCRIPT.md) ensina implementadores a construir e entregar um serviço monitorado. O [livro rápido](../../../../rapid-1-month/critical-sector-security/en/book/MANUSCRIPT.md) é uma primeira introdução. **Este livro profissional trata de coordenação e governança**: quem decide, quem é informado, quem responde, como o risco é classificado e aceito, como os fornecedores são cobrados, como um exercício de mesa é desenhado e avaliado, e como tudo isso é mostrado a um conselho ou regulador com evidências. Você não vai configurar nada neste livro. Vai aprender a fazer as perguntas que garantem que as pessoas certas configurem as coisas certas, na ordem certa, e consigam prová-lo.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de titularidade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: este curso é um projeto educacional independente. Não é um programa credenciado, não concede qualificação e não concede nenhuma autoridade sobre, ou acesso a, qualquer infraestrutura, operador, conjunto de dados ou pessoa reais. Toda organização, lugar, pessoa, contrato, prazo, linha de log e número de um exemplo resolvido ou laboratório é **sintético**, a menos que uma frase cite explicitamente uma fonte pública. Os prazos de notificação de "Kestrel Vale" são ilustrativos: as obrigações reais vêm da sua própria lei, regulador, licença e contratos. Nada neste livro é aconselhamento jurídico, clínico ou regulatório.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão de livros](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os doze capítulos acompanham um **coordenador de resiliência cibernética** recém-nomeado ao longo de seis meses numa empresa de água de porte médio. O resultado do curso é **operar um fluxo de coordenação repetível e comunicar constatações** sobre a segurança de infraestrutura crítica, sob supervisão.

- **Meses 1–2 (Capítulos 1–4)** constroem a base: para que serve um coordenador, o serviço e as suas partes interessadas, trabalho autorizado e registros de decisão, e um registro de riscos orientado por consequências.
- **Meses 3–4 (Capítulos 5–8)** transformam isso num programa em funcionamento: frameworks e avaliações lidos de forma crítica, papéis e uma matriz RACI, controles com dono e verificados com evidências, e um caso supervisionado de acesso de fornecedor.
- **Meses 5–6 (Capítulos 9–12)** testam e apresentam o programa: notificação e comunicação de crise, encontrar e corrigir falhas no próprio programa, um exercício de mesa completo e um portfólio final com uma apresentação ao conselho.

Cada capítulo tem objetivos de aprendizagem, seções didáticas com definições, um exemplo resolvido, uma atividade prática, erros comuns e limites, cinco exercícios numerados e uma síntese. Cinco capítulos contêm um laboratório curto em Python. Os laboratórios não são aulas de programação: cada um é uma lista de verificação tornada executável, para que você veja exatamente qual regra sinaliza qual registro e possa discutir com a regra. Eles usam apenas a biblioteca padrão do Python 3 (as saídas deste rascunho foram produzidas com o Python 3.13.5), não precisam de rede, pacotes, privilégios nem dados reais, e toda saída está impressa no texto. Você pode fazer todos os exercícios sem executar código, lendo a saída impressa. Escreva sua resposta a cada exercício antes de abrir as [resoluções](#worked-results); a rubrica de 0 a 3 mostra o que um avaliador recompensa, e uma resposta diferente e defensável pode receber a pontuação máxima.

Mantenha quatro rótulos em toda nota de coordenação: **decidido** (o que foi decidido, por quem, quando e com base em quê), **pressuposto** (aquilo de que a decisão depende e que ninguém verificou), **devido** (o que alguém prometeu, a quem e até quando) e **em aberto** (o que é desconhecido, e quem está descobrindo).

### O cenário sintético usado neste livro

| Elemento sintético | Papel no livro | Limite |
|---|---|---|
| **Kestrel Vale** — uma região fictícia, com o seu próprio regulador e CSIRT nacional fictícios | Cenário de todos os exemplos. | Lugar e lei inventados. |
| **Kestrel Water** — empresa de água potável, 180.000 pessoas, estação de tratamento KW-TW e estações de bombeamento/dosagem KW-01 a KW-12 | Empregadora do leitor. O leitor é o **coordenador de resiliência cibernética**, subordinado ao diretor de operações. | Inventada. |
| Pessoas: A. Mensah (gerente de operações), L. Ferreira (líder de segurança, em tempo parcial, do departamento de TI), J. Tan (engenheiro de sistemas de controle), C. Okafor (atendimento ao cliente e faturamento), R. Adeyemi (comunicação), M. Holt (diretor-presidente), E. Varga (diretor de operações), T. Lindqvist (presidente do comitê de auditoria e riscos do conselho) | Colegas. | Inventadas; nenhuma pessoa real. |
| **Kestrel Vale Regional Operations Centre (KVROC)** | Serviço de monitoramento compartilhado usado pela empresa. | Inventado. |
| **Kestrel Grid**, **Kestrel General Hospital** | Fornecedor de energia e o cliente mais crítico. | Inventados. |
| Fornecedores HydroLogic Ltd, ScadaCo, Vale Pumps, MeterWorks, Northgate Integration | Terceiros nos Capítulos 8–11. | Inventados; qualquer semelhança com empresas reais é acidental. |

Como os dados são sintéticos, o livro pode dizer o que um coordenador real raramente sabe com certeza. Use isso para aprender como os programas falham, nunca como evidência sobre organizações reais.

### Política de fontes

Toda afirmação factual sobre um framework, uma lei, uma norma, um incidente público ou uma orientação publicada remete a uma fonte consultada em outubro de 2026. Normas, orientações e leis mudam e diferem entre jurisdições: verifique cada uma de novo antes de se apoiar nela. O vocabulário comum de gestão (RACI, dono do risco, declaração provisória) não recebe uma referência inventada. Uma citação apoia a afirmação geral ao seu lado, nunca os detalhes sintéticos. Incidentes públicos são descritos apenas no nível em que os seus editores os divulgaram.

### Regras profissionais para o trabalho de coordenação

1. Você coordena; não autoriza a si mesmo. Toda avaliação, teste, sessão de fornecedor ou mudança precisa da aprovação de quem é dono do serviço afetado (Capítulo 3).
2. As operações têm a última palavra sobre a segurança física. Uma recomendação de segurança que possa afetar o tratamento, a pressão ou a dosagem passa pelo gerente de operações, sempre.
3. Nunca peça a ninguém que "só dê uma olhada" num sistema de controle em produção sem essa aprovação, e nunca encaminhe credenciais, diagramas de rede ou mapas de registradores por e-mail ou chat comuns.
4. Relate o que você sabe, rotule o que você pressupõe e corrija prontamente o que errou (Capítulo 9).
5. Trate as pessoas como a força do sistema. Exercícios testam planos, não indivíduos (Capítulo 11).

## Sumário

1. [Fundamentos de segurança para profissionais](#ch-01) — serviços essenciais, consequência, o trabalho do coordenador e a linguagem do risco.
2. [Contexto de serviço e de partes interessadas](#ch-02) — funções críticas, dependências e as pessoas que precisam estar na sala.
3. [Prática autorizada e tratamento de evidências](#ch-03) — quem pode autorizar o quê, registros de decisão e compartilhamento de informações.
4. [Métodos centrais](#ch-04) — um registro de riscos orientado por consequências, titularidade e aceitação. Laboratório 4.
5. [Ferramentas e interpretação](#ch-05) — frameworks, avaliações, notas de maturidade e métricas lidos de forma crítica.
6. [Fluxo operacional](#ch-06) — papéis, uma matriz RACI, governança de mudanças de TI/TO e escalonamento. Laboratório 6.
7. [Controles e verificação](#ch-07) — titularidade dos controles, níveis de garantia e exceções com prazo.
8. [Análise supervisionada de caso](#ch-08) — um caso de acesso remoto de fornecedor e a governança de terceiros. Laboratório 8.
9. [Comunicação, ética e relato](#ch-09) — prazos de notificação, clientes críticos, declarações provisórias e honestidade. Laboratório 9.
10. [Qualidade e resolução de problemas](#ch-10) — diagnosticar um programa de coordenação que não está funcionando. Laboratório 10.
11. [Laboratório supervisionado](#ch-11) — desenhar, conduzir e avaliar um exercício de mesa.
12. [Portfólio de prática e revisão final](#ch-12) — portfólio, apresentação ao conselho e um plano de 90 dias.

Apêndices: [Resoluções e notas de avaliação](#worked-results) · [Glossário](#glossary) · [Referências](#references).

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- explicar o que torna um serviço "essencial" e por que a sua segurança é julgada pela **consequência** para as pessoas, e não pelo dano aos computadores;
- descrever o trabalho do coordenador e distingui-lo do trabalho do engenheiro, do analista de segurança e do executivo;
- usar o vocabulário central do risco — ativo, ameaça, vulnerabilidade, probabilidade, consequência, dono do risco, apetite a risco — com precisão suficiente para que os colegas possam agir a partir das suas frases;
- situar o seu trabalho dentro de um framework reconhecido (as seis funções do NIST Cybersecurity Framework 2.0) sem confundir o framework com o trabalho.

Este capítulo pressupõe apenas noções básicas de segurança. Tudo o que vem depois no livro se apoia nas distinções feitas aqui.

### 1.1 O que é um serviço essencial

Um **serviço essencial** é aquele cuja interrupção prejudica pessoas, a economia ou a ordem pública rapidamente e em grande escala: água potável, eletricidade, saúde, transporte, pagamentos, comunicações de emergência. Os governos os listam de formas diferentes. Os Estados Unidos agrupam dezesseis setores de infraestrutura crítica ([CISA, Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors)) e descrevem as **funções críticas nacionais** subjacentes — por exemplo, "fornecer água" ou "prestar atendimento médico" — que atravessam os setores ([CISA, National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set)). A Diretiva NIS2 da União Europeia nomeia setores de "alta criticidade" e impõe obrigações a entidades essenciais e importantes, inclusive aos seus órgãos de gestão ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)).

A ideia útil em todas essas listas é a mesma: o que se protege é uma **função entregue a pessoas**, não um prédio ou um servidor. A Kestrel Water não existe para operar computadores; existe para que 180.000 pessoas possam beber água segura, com pressão adequada, a cada hora de cada dia. Os seus computadores importam na medida em que a função depende deles.

### 1.2 Consequência primeiro

Num escritório, a tríade clássica da segurança costuma ser recitada como confidencialidade, integridade e disponibilidade, nessa ordem. Num serviço essencial, a ordem de preocupação geralmente muda. O guia do NIST para a segurança da tecnologia operacional observa que os sistemas de TO afetam diretamente o mundo físico e que as suas prioridades — segurança humana, disponibilidade e integridade do controle — diferem das prioridades típicas de TI ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

Para um coordenador, isso tem um significado prático. Ao classificar um problema, pergunte nesta ordem:

1. **Isso pode ferir alguém?** (dosagem química errada, perda de pressão para um hospital, um trabalhador exposto a uma bomba em movimento);
2. **Isso pode parar o serviço, por quanto tempo e para quantas pessoas?**
3. **Isso pode tornar o serviço não confiável** — operadores já sem certeza de que as telas mostram a verdade?
4. **Isso pode expor informações** — dados de clientes, projetos de rede, relatórios de vulnerabilidades?

Um vazamento de dados do sistema de faturamento é grave e pode acarretar obrigações legais, mas uma mudança silenciosa num setpoint de cloro é uma categoria diferente de problema. Um coordenador que não consegue explicar essa diferença numa frase a um conselho verá o dinheiro ir para o lugar errado.

### 1.3 O trabalho do coordenador

O diretor de operações da Kestrel Water, E. Varga, escreveu a descrição do novo cargo. O seu núcleo são três verbos: **conectar**, **viabilizar decisões** e **evidenciar**.

- **Conectar.** Operações, TI, engenharia, atendimento ao cliente, comunicação, fornecedores e a diretoria detêm, cada um, parte do quadro. O coordenador garante que as partes se encontrem: as pessoas certas ficam sabendo de um risco, de uma mudança ou de um incidente a tempo.
- **Viabilizar decisões.** O coordenador raramente toma as decisões importantes. O gerente de operações decide se uma estação será operada manualmente; o diretor-presidente decide o que dizer ao público. O coordenador garante que a decisão tenha um dono, as informações de que precisa, um prazo e um registro.
- **Evidenciar.** O coordenador consegue mostrar, a um conselho, auditor ou regulador, o que foi decidido, por quê e se foi feito.

O coordenador **não** é o engenheiro que reconfigura o firewall, o analista que lê os logs nem o executivo que aceita o risco. Confundir esses papéis é a falha mais comum dos novos coordenadores: ou tentam fazer eles mesmos o trabalho técnico (e perdem de vista o programa), ou tomam decisões que pertencem a alguém com autoridade sobre o serviço (e depois são desautorizados ou culpados).

### 1.4 O vocabulário do risco

Palavras precisas economizam horas de reunião. As definições a seguir seguem o uso comum da [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), simplificadas para a prática:

- **Ativo** — qualquer coisa de que o serviço depende: equipamentos, software, dados, pessoas, fornecedores, prédios.
- **Ameaça** — uma circunstância ou um agente com potencial de causar dano (um grupo criminoso, uma atualização descuidada, uma enchente).
- **Vulnerabilidade** — uma fraqueza que uma ameaça poderia explorar (uma conta de fornecedor sem autenticação multifator).
- **Probabilidade** — quão provável é que o dano aconteça num dado período, considerados os controles existentes.
- **Consequência** (ou impacto) — o que acontece com o serviço e com as pessoas se o dano acontecer.
- **Risco** — a combinação: uma declaração do que pode acontecer, como, com que probabilidade e com que gravidade.
- **Dono do risco** — a pessoa com autoridade e orçamento para decidir como o risco é tratado. Em geral, um gestor do serviço afetado, não o coordenador.
- **Apetite a risco** — quanto risco a liderança da organização está disposta a aceitar na busca dos seus objetivos, declarado de antemão.
- **Tratamento** — reduzir, evitar, transferir (por exemplo, por seguro ou contrato) ou aceitar o risco.

Uma declaração de risco bem formada tem uma causa, um evento e uma consequência: "*Como* a conta remota do fornecedor de bombas não tem segundo fator, *um atacante com a senha do fornecedor poderia* entrar nos controladores das estações *e alterar os setpoints das bombas, causando* perda de pressão para até 20.000 clientes, incluindo o hospital." Compare com "risco de acesso de fornecedor", que ninguém consegue assumir nem tratar.

### 1.5 Frameworks como mapas

O NIST Cybersecurity Framework 2.0 organiza resultados em seis funções: **Governar, Identificar, Proteger, Detectar, Responder e Recuperar** ([NIST CSWP 29, The NIST Cybersecurity Framework 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)). A versão 2.0 acrescentou Governar, que abrange estratégia, papéis, política, gestão de riscos e risco da cadeia de suprimentos — a maior parte do assunto deste livro. O Cyber Assessment Framework do Reino Unido, escrito para operadores de serviços essenciais, organiza-se em torno de objetivos como gerenciar o risco de segurança e minimizar o impacto de incidentes ([NCSC, Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf)).

Um framework é um mapa de resultados. Ele diz o que um bom programa alcança, não como a sua empresa deve alcançá-lo, e certamente não que você o alcançou. O Capítulo 5 mostra como ler avaliações baseadas em frameworks sem se deixar enganar por elas.

### 1.6 Exemplo resolvido: a primeira semana (sintético)

No primeiro dia, a nova coordenadora recebe três pedidos:

1. O departamento de TI pede que ela "dê o aval" a um novo antivírus para os computadores da sala de controle até sexta-feira.
2. O presidente do comitê de auditoria do conselho, T. Lindqvist, pede "a nossa nota de risco cibernético" para a reunião do comitê do mês que vem.
3. O gerente de operações, A. Mensah, comenta que um fornecedor de bombas "às vezes entra de casa" para consertar a estação KW-07.

Uma resposta fraca os trata como três tarefas. A resposta de um coordenador os ordena por consequência e por quem é dono da decisão:

| Pedido | Pergunta de consequência | Decisão de quem? | Ação do coordenador |
|---|---|---|---|
| Antivírus nos PCs da sala de controle | O produto pode bloquear ou deixar lentas as telas dos operadores? (A NIST SP 800-82 alerta que ferramentas de TI podem perturbar a TO) | Gerente de operações, assessorado pelo engenheiro de sistemas de controle e pelo fornecedor | Perguntar a J. Tan se o fornecedor do sistema de controle suporta o produto; organizar um teste numa máquina fora de produção; **não** dar o aval sozinha. |
| A "nota de risco" do conselho | Que decisão o conselho tomará com ela? | Conselho (apetite); diretoria (tratamento) | Oferecer, em vez de um número único, uma lista curta dos principais riscos classificados por consequência, com donos e datas (Capítulo 4). |
| Acessos do fornecedor a partir de casa | Outra pessoa poderia usar esse acesso para mudar as configurações das bombas? | O gerente de operações é dono da estação; o líder de segurança assessora | Registrar como risco candidato, com uma declaração completa de causa-evento-consequência; agendar uma revisão de acesso de fornecedores (Capítulo 8). |

O terceiro item, levantado casualmente, é o de maior consequência. Coordenadores aprendem a ouvir o risco na conversa.

### 1.7 Atividade prática

Escolha um serviço essencial que você conheça (o seu próprio empregador, ou um serviço público descrito numa reportagem). Escreva, em no máximo uma página: a função que ele entrega às pessoas; três coisas de que ele depende; e uma declaração de risco bem formada, com causa, evento e consequência. Marque quais partes você sabe e quais você pressupõe.

Depois entregue a página a um colega e peça que ele nomeie o dono do risco apenas a partir da sua declaração. Se ele não conseguir, a consequência ou o serviço afetado provavelmente estão vagos demais. Compare a sua função com a frase da Kestrel Water sobre água segura, com pressão adequada, para 180.000 pessoas: ela nomeia quem é atendido e do que essas pessoas precisam.

### 1.8 Erros comuns e limites

- Tratar a "segurança" como propriedade do departamento de TI. Num serviço essencial, as operações são donas da consequência.
- Escrever riscos como substantivos ("ransomware", "insider") em vez de declarações que alguém possa assumir.
- Pedir uma nota de risco única. Notas escondem qual serviço, quais pessoas e qual decisão.
- Confundir um perfil de framework com evidência de que os controles funcionam.
- Este capítulo simplifica: métodos reais de risco (Capítulo 4) exigem calibração, dados e julgamento, e as leis diferem entre países.

- Dar o aval a uma mudança que pertence a outra pessoa, como a coordenadora evitou com o pedido do antivírus para os computadores da sala de controle.
- Tratar um comentário casual, como o de um fornecedor que às vezes entra de casa, como conversa à toa em vez de um risco candidato.

### Exercícios — capítulo 1

**EX001 — Reescreva riscos.** *Objetivo:* produzir declarações de risco que possam ser assumidas. *Insumos:* as entradas de registro "ransomware", "PCs antigos" e "acesso de fornecedor". *Passos:* reescrever cada uma como uma declaração de causa-evento-consequência situada na Kestrel Water. *Evidência esperada:* três declarações. *Rubrica:* 3 = cada uma tem causa, evento e uma consequência para o serviço medida em pessoas ou tempo, e nomeia a função afetada; 2 = uma não tem consequência; 1 = ainda genéricas; 0 = nada.

**EX002 — Ordem de preocupação.** *Objetivo:* aplicar a classificação com a consequência primeiro. *Insumos:* quatro eventos: (a) banco de dados de faturamento copiado por um intruso; (b) telas dos operadores na KW-03 congelam por 40 minutos; (c) setpoint de cloro na KW-05 alterado sem aprovação; (d) diagrama da rede interna enviado por e-mail a um endereço errado. *Passos:* classificá-los e justificar. *Evidência esperada:* classificação com uma frase para cada um. *Rubrica:* 3 = (c) primeiro por razões de segurança, (b) em segundo pela perda de visão e possível perda de controle, depois (d) e (a), com raciocínio sobre quem é prejudicado e como; observa que obrigações legais ainda podem tornar (a) urgente; 2 = apenas os dois primeiros corretos; 1 = classifica (a) em primeiro sem raciocínio; 0 = nada.

**EX003 — Limites de papel.** *Objetivo:* separar coordenação de autoridade. *Insumos:* o pedido do antivírus na seção 1.6. *Passos:* escrever o e-mail que você enviaria à TI e a A. Mensah. *Evidência esperada:* duas mensagens curtas. *Rubrica:* 3 = recusa o aval exclusivo, nomeia o dono da decisão, pede a compatibilidade do fornecedor, um teste fora de produção e um plano de reversão, propõe uma data; 2 = dono correto sem pedido de teste; 1 = dá o aval; 0 = nada.

**EX004 — Mapeie para o CSF 2.0.** *Objetivo:* usar um framework como mapa. *Insumos:* os três pedidos da seção 1.6. *Passos:* atribuir cada um a uma ou mais funções do CSF 2.0 e explicar. *Evidência esperada:* três atribuições. *Rubrica:* 3 = antivírus → Proteger (e Governar, pelos direitos de decisão); nota de risco → Governar; acessos do fornecedor → Governar (cadeia de suprimentos) e Identificar/Proteger; observa que um rótulo de função não é evidência; 2 = rótulos sem razões; 1 = um rótulo; 0 = nada.

**EX005 — Ouça o risco.** *Objetivo:* identificar o risco na conversa. *Insumos:* o comentário "o turno da noite deixa a porta da estação escorada aberta porque o leitor de crachá é lento." *Passos:* escrever uma declaração de risco, nomear um provável dono e uma pergunta que você faria antes de propor qualquer correção. *Evidência esperada:* declaração, dono, pergunta. *Rubrica:* 3 = a declaração liga o acesso físico ao equipamento de controle e à consequência; o dono é o gerente da estação ou de operações; a pergunta respeita o motivo de a equipe agir assim (por exemplo, quão lento é, e a porta é necessária como saída de emergência?); 2 = sem pergunta; 1 = culpa a equipe; 0 = nada.

### Síntese do capítulo

Um serviço essencial é uma função entregue a pessoas, e a sua segurança se mede pela consequência: segurança das pessoas, continuidade, confiabilidade e, depois, confidencialidade. O coordenador conecta as pessoas que detêm partes do quadro, garante que as decisões tenham donos e registros, e guarda as evidências. Declarações de risco precisas e um framework usado como mapa — e não como prova — são as primeiras ferramentas do trabalho.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestrutura crítica e segurança setorial: contexto de serviço e de partes interessadas

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- descrever um serviço crítico como uma cadeia de funções e dependências, a montante e a jusante;
- construir um mapa de partes interessadas que distinga quem decide, quem precisa ser informado e quem pode ajudar;
- reconhecer como os setores diferem — água, energia, saúde, transporte, finanças — no que "dano" significa e em quem os regula;
- identificar efeitos em cascata entre setores e a coordenação que eles exigem.

O Capítulo 1 definiu o serviço pela sua consequência. Este capítulo desenha as pessoas e as dependências ao redor dele.

### 2.1 Um serviço é uma cadeia

A água potável da Kestrel Water passa por uma cadeia: captação no rio, tratamento na KW-TW, dosagem química, bombeamento e armazenamento nas estações KW-01 a KW-12, distribuição, medição e faturamento. Cada elo depende de coisas que a empresa não controla totalmente: eletricidade da Kestrel Grid, produtos químicos entregues por rodovia, telecomunicações para a telemetria, um serviço de monitoramento no KVROC, software e manutenção de fornecedores, e pessoas com habilidades escassas.

As funções críticas nacionais da CISA descrevem essa visão no nível nacional: funções como "fornecer água" dependem de outras, como "fornecer eletricidade" e "fornecer conteúdo, informação e serviços de comunicação baseados na internet" ([CISA, National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set)). A versão do coordenador é local e concreta: um mapa de dependências de uma página que um novo gestor consiga ler em cinco minutos.

### 2.2 A montante, a jusante, compartilhadas

Três tipos de dependência importam para um coordenador:

- **A montante** — aquilo de que o serviço precisa: energia, produtos químicos, comunicações, fornecedores, pessoal.
- **A jusante** — quem precisa do serviço e quanto: residências, escolas, a unidade de esterilização e a diálise do hospital, hidrantes, empresas de alimentos.
- **Compartilhadas** — componentes ou pessoas de que várias funções dependem ao mesmo tempo: uma única operadora de telecomunicações para toda a telemetria, um único engenheiro do fornecedor que conhece todas as estações, um único centro de monitoramento compartilhado.

As dependências compartilhadas são onde eventos isolados se tornam interrupções amplas. A pergunta mais valiosa de um coordenador em qualquer reunião costuma ser: "*O que mais usa isso?*"

### 2.3 Partes interessadas e os seus papéis

Uma **parte interessada** é qualquer pessoa que afeta a segurança do serviço ou é afetada por ela. Para a coordenação, classifique cada uma pelo que você precisa dela:

| Classe | Significado | Exemplos na Kestrel Water |
|---|---|---|
| **Decide** | Tem autoridade sobre o serviço, o orçamento ou a mensagem pública | Diretor-presidente, diretor de operações, gerente de operações, conselho |
| **Executa** | Realiza o trabalho | Engenheiro de sistemas de controle, TI, fornecedores, analistas do KVROC, operadores de turno |
| **Precisa ser informado** | Tem direito legal, contratual ou de segurança de saber | Regulador e CSIRT nacional, Kestrel General Hospital, autoridade de saúde pública, seguradora |
| **Pode ajudar** | Oferece capacidade ou informação | Grupo setorial de compartilhamento de informações, CSIRT nacional, parceiros de ajuda mútua, sala de controle da Kestrel Grid |
| **É afetado** | Sofre a consequência | Clientes, funcionários, empresas de água vizinhas |

Uma parte interessada pode estar em várias classes. O hospital "precisa ser informado" quando a qualidade ou a pressão da água estão em risco e também "é afetado"; ele também pode "ajudar", dizendo quais dos seus sistemas mais precisam de água.

### 2.4 Como os setores diferem

O padrão de coordenação é comum, mas o significado do dano e o cenário regulatório diferem:

- **Água**: a saúde pública é a consequência dominante; os operadores costumam manter locais pequenos, com pouco pessoal; a operação manual muitas vezes é possível por algum tempo. A CISA e parceiros publicaram alertas específicos para o setor de água depois de ataques a controladores expostos à internet ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)).
- **Eletricidade**: equilíbrio em tempo real e falhas em cascata entre redes; as interrupções afetam todos os outros setores. Os ataques de 2015 a distribuidoras ucranianas causaram interrupções para os clientes e foram seguidos de restabelecimento manual ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)).
- **Saúde**: segurança do paciente e continuidade clínica; muitos dispositivos médicos conectados; a equipe clínica decide sobre desvio de pacientes e procedimentos de contingência.
- **Transporte e dutos**: segurança da movimentação e do abastecimento de combustível; sistemas de negócio podem forçar paralisações operacionais mesmo quando os sistemas de controle não foram tocados. No caso do ransomware DarkSide em 2021, a CISA e o FBI emitiram um alerta sobre ataques à rede de TI de uma empresa de infraestrutura crítica ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)).
- **Finanças**: integridade das transações e confiança pública; forte regulação já existente sobre resiliência operacional.

A lição profissional: ao coordenar entre setores (água com energia, hospital com água), traduza a sua consequência para a deles. "Estação KW-02 fora do ar" não significa nada para o hospital; "pressão mais baixa no lado leste das 14:00 até cerca das 18:00, água segura para beber" significa.

### 2.5 Exemplo resolvido: a dependência do hospital (sintético)

O Kestrel General Hospital é abastecido pela zona leste, alimentada pelas estações KW-02 e KW-07. A coordenadora faz quatro perguntas e registra as respostas:

| Pergunta | Resposta (sintética) | Fonte |
|---|---|---|
| Para que o hospital usa água que não pode esperar? | Central de esterilização, diálise, cozinhas, combate a incêndio, resfriamento do setor de imagem | Gerente de infraestrutura predial do hospital, reunião de 12 de fevereiro |
| Por quanto tempo ele aguenta sem o abastecimento da rede? | Cerca de 6 horas com água armazenada para os usos prioritários | Plano de continuidade de negócios do próprio hospital (não visto; pressuposto) |
| Quem no hospital precisa ser chamado, de dia e de noite? | Plantão da infraestrutura predial; fora do horário, o gerente de plantão do local | Confirmado pela central telefônica do hospital |
| O que o nosso contrato ou acordo promete? | Uma ligação em até 2 horas após qualquer evento que possa afetar o abastecimento ou a qualidade | Acordo de fornecimento, cláusula 7 |

A coordenadora então marca "6 horas" como **pressuposto**, porque não viu o plano. Um pressuposto do qual uma decisão depende é uma tarefa: ela pede para ver a seção relevante. Esse padrão — registrar a fonte e o grau de confiança de cada fato de dependência — percorre todo o livro.

### 2.6 Atividade prática

Desenhe um mapa de dependências para um serviço essencial com pelo menos cinco dependências a montante, três a jusante e uma compartilhada. Para cada uma, nomeie um contato e diga se você verificou a informação ou a pressupôs.

Use a tabela do hospital como modelo: para cada dependência, registre a resposta, a sua fonte e se você mesmo viu a evidência. Todo fato marcado como pressuposto deve virar uma tarefa, com uma pessoa a quem perguntar. Date o mapa e nomeie quem vai revisá-lo, porque fornecedores, contatos e tempos de autonomia mudam. Um mapa sem dependência compartilhada geralmente significa que você ainda não perguntou o que mais usa a operadora, o serviço de monitoramento ou o único engenheiro que conhece todas as estações.

### 2.7 Erros comuns e limites

- Mapear sistemas em vez de funções — uma lista de servidores não é um mapa de dependências.
- Esquecer as pessoas como dependências (um único especialista, um único gerente de plantão).
- Tratar as partes interessadas que "precisam ser informadas" como opcionais até um incidente.
- Falar o jargão do próprio setor com outro setor.
- Mapas de dependências envelhecem; date-os e defina um responsável pela revisão.

- Aceitar o tempo de autonomia de um cliente crítico sem ver o plano de onde ele vem, como a coordenadora evitou com as seis horas do hospital.
- Descrever uma interrupção nos seus próprios termos para outro setor, em vez de dizer o que ela significa para ele, como pressão mais baixa das 14:00 até cerca das 18:00, com água segura para beber.

### Exercícios — capítulo 2

**EX006 — Classifique as partes interessadas.** *Objetivo:* usar as cinco classes. *Insumos:* regulador, KVROC, HydroLogic Ltd, uma escola local, o diretor-presidente, a sala de controle da Kestrel Grid. *Passos:* classificar cada um, admitindo mais de uma classe. *Evidência esperada:* tabela com uma razão por linha. *Rubrica:* 3 = classes defensáveis, com várias classes onde se justifica (por exemplo, a Kestrel Grid como dependência a montante, "pode ajudar" e também "precisa ser informada" se a carga da empresa mudar); 2 = uma classe para cada; 1 = várias erradas; 0 = nada.

**EX007 — Encontre a dependência compartilhada.** *Objetivo:* identificar pontos únicos. *Insumos:* a telemetria das doze estações usa uma única operadora; o KVROC monitora três empresas; um único engenheiro da HydroLogic atende todas as estações. *Passos:* explicar a consequência de perder cada um e a pergunta de coordenação que você levantaria. *Evidência esperada:* três análises curtas. *Rubrica:* 3 = reconhece a perda de visão de todas as estações (operadora), o impacto compartilhado entre empresas e o monitoramento reduzido (KVROC), o risco de pessoa-chave (engenheiro); levanta "o que mais usa isso" e a contingência; 2 = dois de três; 1 = apenas lista; 0 = nada.

**EX008 — Traduza a consequência.** *Objetivo:* comunicar entre setores. *Insumos:* "A KW-07 operará em manual a partir das 10:00 por seis horas devido a um suposto comprometimento do enlace do fornecedor." *Passos:* reescrever para o gerente de infraestrutura predial do hospital. *Evidência esperada:* mensagem com menos de 80 palavras. *Rubrica:* 3 = declara o efeito no abastecimento nos termos do hospital (pressão, segurança, duração), o que o hospital deve fazer, o horário da próxima atualização e um contato; evita detalhes técnicos e especulação; 2 = falta a próxima atualização; 1 = encaminha a frase técnica; 0 = nada.

**EX009 — Verifique um pressuposto.** *Objetivo:* gerenciar o grau de confiança. *Insumos:* o pressuposto das "6 horas" na seção 2.5. *Passos:* descrever como você o verificaria e o que faria se o número real fosse 2 horas. *Evidência esperada:* plano e consequência. *Rubrica:* 3 = pedir a seção específica do plano ou uma reunião com a infraestrutura predial, registrar data e fonte; com 2 horas, a promessa de notificação em 2 horas se torna inadequada, então revisar o acordo e planejar um abastecimento alternativo (caminhões-pipa) com o hospital; 2 = apenas a verificação; 1 = aceita o pressuposto; 0 = nada.

**EX010 — Diferença setorial.** *Objetivo:* reconhecer o significado setorial do dano. *Insumos:* a mesma infecção por ransomware da TI de negócio em (a) uma empresa de água e (b) um operador de oleoduto. *Passos:* explicar por que cada um poderia paralisar as operações mesmo com os sistemas de controle limpos, citando o alerta público pertinente quando apropriado. *Evidência esperada:* dois parágrafos. *Rubrica:* 3 = explica a dependência das operações em relação às funções de negócio (faturamento, programação, monitoramento) e a cautela quanto à propagação, cita o AA21-131A apenas no nível em que foi publicado e evita afirmações além dele; 2 = genérico; 1 = pressupõe que a TO foi atingida; 0 = nada.

### Síntese do capítulo

Um serviço crítico é uma cadeia de funções com dependências a montante, a jusante e compartilhadas, e um conjunto de partes interessadas que decidem, executam, precisam ser informadas, podem ajudar ou são afetadas. Os setores diferem no que o dano significa; por isso, o coordenador traduz as consequências para os termos do setor que as recebe. Registre a fonte e o grau de confiança de cada fato de dependência; um pressuposto não verificado por trás de uma decisão é uma tarefa.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e tratamento de evidências

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- explicar quem pode autorizar trabalho de segurança num serviço essencial e o que contém uma autorização válida;
- escrever um **registro de decisão** que resista às perguntas de um regulador ou auditor um ano depois;
- gerenciar as evidências que um programa de coordenação produz: o que guardar, onde, por quanto tempo e quem pode vê-las;
- compartilhar informações sensíveis com parceiros usando um esquema de marcação acordado (o Traffic Light Protocol).

O Capítulo 2 identificou quem decide. Este capítulo torna as suas decisões explícitas, registradas e seguras para compartilhar.

### 3.1 Por que a autorização é um problema de coordenação

O trabalho de segurança num serviço essencial — uma avaliação, uma varredura de vulnerabilidades, uma sessão de manutenção de fornecedor, um teste de intrusão, até mesmo "só dar uma olhada" na configuração de um controlador — pode afetar o serviço. Em ambientes de controle, o NIST observa que algumas atividades rotineiras de TI, incluindo a varredura ativa, podem perturbar as operações ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). A autorização existe para que a pessoa responsável pela consequência concorde de antemão com o que vai acontecer, e para que todos possam depois mostrar o que foi acordado.

O coordenador costuma ser quem **monta** uma autorização: redige o escopo, obtém as assinaturas certas, distribui o documento e o guarda. Raramente é quem a **concede**.

### 3.2 O que contém uma autorização válida

Use os elementos a seguir para qualquer avaliação, teste ou trabalho de terceiros em sistemas operacionais. O guia de testes do NIST descreve regras de engajamento com conteúdo semelhante para avaliações técnicas ([NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)).

| Elemento | Pergunta que responde |
|---|---|
| Finalidade | Por que este trabalho está sendo feito? |
| Sistemas no escopo — e fora dele | Exatamente quais locais, sistemas e contas; e quais estão excluídos (por exemplo, controladores de dosagem, sistemas de segurança) |
| Atividades permitidas — e proibidas | O que pode ser feito (ler a configuração, revisar documentos) e o que não pode (escrever, reiniciar, varredura ativa) |
| Pessoas | Quem fará o trabalho, nominalmente, e quem supervisiona |
| Janela | Data e hora de início e de fim, com fuso horário |
| Condições | Operações presentes; condições de parada; canal de comunicação |
| Tratamento de dados | O que pode ser copiado, onde é armazenado, quando é destruído |
| Autoridade | Nome, função e assinatura do dono do serviço (e do gerente do fornecedor, quando pertinente) |

Uma **condição de parada** é um evento acordado de antemão que encerra o trabalho imediatamente — "qualquer alarme inesperado na estação; qualquer pedido de um operador; qualquer perda de visão nas telas dos operadores". As condições de parada transformam "tome cuidado" em algo verificável.

### 3.3 Registros de decisão

A coordenação produz decisões: aceitar um risco, adiar uma correção, isolar uma estação, notificar um regulador. Um **registro de decisão** é uma nota curta e datada que registra:

1. a decisão, numa frase;
2. quem a tomou, e sob qual autoridade;
3. as opções consideradas e por que esta foi escolhida;
4. as informações disponíveis na época, e o que era desconhecido;
5. condições e data de revisão ("rever se o fornecedor lançar uma correção, ou até 30 de junho");
6. quem foi informado.

O objetivo do item 4 é a justiça com quem decidiu. Uma decisão tomada às 02:00 com informações parciais pode ser boa mesmo que o resultado seja ruim. Sem um registro, a retrospectiva reescreve a história. Com um registro, a organização consegue aprender quais decisões foram ruins e quais foram azaradas.

### 3.4 Tratamento de evidências pelo coordenador

Um coordenador lida com três tipos de evidência:

- **Evidências de governança** — autorizações, registros de decisão, aceitações de risco, atas de reunião, relatórios de exercícios. Guardadas como registro da organização; proteja a integridade (quem mudou o quê) e retenha conforme a política.
- **Evidências de incidente** — logs, imagens e e-mails reunidos durante um incidente. A sua coleta é trabalho técnico; o coordenador garante que ela seja pedida cedo, que a custódia seja registrada e que o acesso seja limitado. As orientações do NIST para resposta a incidentes enfatizam a preparação da coleta de evidências antes que os incidentes aconteçam ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).
- **Informações sensíveis de projeto** — diagramas de rede, relatórios de vulnerabilidades, listas de acesso de fornecedores. Não são evidência de irregularidade, mas são muito úteis a um atacante. Armazene-as num local com controle de acesso, nunca em conversas gerais de e-mail.

Três regras práticas: um local oficial por tipo de registro; um dono nomeado para cada local; e nenhum segredo (senhas, chaves) em nenhum registro.

### 3.5 Compartilhamento: o Traffic Light Protocol

Os parceiros — o CSIRT nacional, um grupo setorial de compartilhamento de informações, o hospital — precisam de informações para se proteger. O **Traffic Light Protocol (TLP)** é um esquema de marcação amplamente usado que diz aos destinatários até onde podem compartilhá-las ([FIRST, TLP 2.0](https://www.first.org/tlp/)):

- **TLP:RED** — apenas para os destinatários nomeados;
- **TLP:AMBER** — os destinatários podem compartilhar dentro da sua organização e com os clientes dela, conforme a necessidade de saber; **TLP:AMBER+STRICT** limita o compartilhamento apenas à organização do destinatário;
- **TLP:GREEN** — pode ser compartilhado dentro da comunidade do destinatário, não publicamente;
- **TLP:CLEAR** — sem restrição além dos direitos autorais normais.

O TLP marca a permissão de compartilhamento, não uma classificação de confidencialidade, e não substitui obrigações legais. Marque a linha de assunto e o início da mensagem, e escolha o rótulo menos restritivo que ainda proteja as pessoas.

### 3.6 Exemplo resolvido: autorizando a avaliação de um fornecedor (sintético)

A ScadaCo oferece uma "verificação de saúde de segurança" gratuita do sistema de controle da estação de tratamento. A coordenadora redige a autorização:

- **Finalidade:** revisar a configuração dos servidores de supervisão segundo o guia de endurecimento da ScadaCo.
- **No escopo:** os dois servidores de supervisão da KW-TW e a sua documentação. **Fora do escopo:** todos os controladores das estações, o sistema de dosagem, o firewall da rede.
- **Permitido:** revisão somente leitura de arquivos de configuração exportados, entrevista supervisionada com J. Tan. **Proibido:** varredura de rede, instalação de software, alteração de qualquer configuração, cópia de dados para fora do local, exceto o relatório final.
- **Pessoas:** M. Ilic (ScadaCo), supervisionado por J. Tan.
- **Janela:** 21 de abril de 2026, 09:00–13:00, horário local.
- **Condições de parada:** qualquer pedido de um operador; qualquer alarme na KW-TW.
- **Tratamento de dados:** o relatório é marcado como TLP:AMBER+STRICT, entregue pelo serviço seguro de transferência de arquivos acordado e armazenado na biblioteca de registros de segurança; a ScadaCo apaga as anotações de trabalho em até 14 dias e confirma por escrito.
- **Autoridade:** A. Mensah (gerente de operações, dono da KW-TW); o gerente de serviços da ScadaCo assina em conjunto.

No dia, M. Ilic pede para "rodar rapidinho uma ferramenta de descoberta para conferir as versões". J. Tan recusa, porque a autorização proíbe varreduras, e registra o pedido. O registro de decisão anota a recusa e que a verificação de versões será feita a partir da documentação. Isso é a autorização funcionando como pretendido.

### 3.7 Atividade prática

Pegue qualquer visita rotineira de fornecedor numa organização que você conheça e escreva a sua autorização no formato da tabela da seção 3.2. Marque quais elementos você não conseguiu preencher; essas são as lacunas na prática dessa organização.

Escolha uma visita que toque um sistema que preocuparia alguém, como uma sessão de manutenção num controlador, e não uma faxina ou uma entrega. Escreva as condições de parada como eventos que qualquer pessoa no local consiga reconhecer. Depois pergunte a quem assinaria como dono do serviço se concorda com o seu escopo e as suas exclusões; a resposta costuma revelar um sistema que você esqueceu. Guarde o seu rascunho e os comentários dessa pessoa juntos, como evidência da lacuna que você encontrou.

### 3.8 Erros comuns e limites

- "OK verbal" de alguém sem autoridade sobre o serviço.
- Escopo escrito como "a rede de TO", sem exclusões.
- Nenhuma condição de parada, ou condições de parada que ninguém no local conhece.
- Registros de decisão escritos depois que o resultado é conhecido.
- Enviar informações de projeto como anexos de e-mail comuns.
- Usar o TLP como se fosse uma classificação legal ou para esconder informações de quem precisa delas.

- Deixar o fornecedor redefinir o trabalho no próprio dia, como o pedido da ScadaCo para rodar uma ferramenta de descoberta teria feito se J. Tan não o tivesse recusado.
- Não manter registro de uma recusa, de modo que um revisor posterior não consegue ver que a autorização foi cumprida.

### Exercícios — capítulo 3

**EX011 — Conserte uma autorização.** *Objetivo:* encontrar os elementos ausentes. *Insumos:* "OK para a Northgate fazer um pentest na rede de TO semana que vem — A. Mensah (pelo chat)". *Passos:* listar os elementos ausentes e reescrevê-la. *Evidência esperada:* lista de lacunas e reescrita. *Rubrica:* 3 = identifica finalidade, escopo e exclusões, atividades permitidas/proibidas, pessoas nomeadas, janela com fuso horário, condições de parada, tratamento de dados e autoridade por escrito; a reescrita exclui os sistemas de segurança e de dosagem e prefere métodos não intrusivos; 2 = a maioria dos elementos; 1 = edições pequenas; 0 = nada.

**EX012 — Escreva um registro de decisão.** *Objetivo:* registrar uma decisão com justiça. *Insumos:* às 02:10, o gerente de plantão decidiu manter a KW-05 em automático apesar de um login remoto inexplicado, porque a operação manual exigia convocar pessoal, com 90 minutos de espera. *Passos:* escrever o registro em seis partes. *Evidência esperada:* o registro. *Rubrica:* 3 = as seis partes, com os desconhecidos declarados na época (se o login era malicioso), condições (vigiar os valores de dosagem, rever às 06:00) e quem foi informado; 2 = faltam opções ou desconhecidos; 1 = apenas narrativa; 0 = nada.

**EX013 — Escolha um rótulo TLP.** *Objetivo:* aplicar o TLP 2.0. *Insumos:* (a) indicadores de uma campanha de phishing contra empresas de água, a enviar ao grupo setorial; (b) um relatório que nomeia os modelos de controladores sem correção da Kestrel Water, para o KVROC; (c) um aviso público para os clientes. *Passos:* escolher os rótulos e justificar. *Evidência esperada:* três rótulos. *Rubrica:* 3 = (a) GREEN (benefício à comunidade), (b) AMBER+STRICT ou RED (sensível para a empresa; o KVROC precisa dele), (c) CLEAR; razões dadas; 2 = rótulos sem razões; 1 = tudo RED; 0 = nada.

**EX014 — Locais das evidências.** *Objetivo:* organizar as evidências de governança. *Insumos:* autorizações na caixa de entrada de um engenheiro, aceitações de risco em atas do conselho, relatórios de exercícios num drive compartilhado, listas de acesso de fornecedores numa planilha enviada por e-mail todo mês. *Passos:* propor um esquema. *Evidência esperada:* esquema de um parágrafo, com donos. *Rubrica:* 3 = um local oficial com controle de acesso por tipo de registro, donos nomeados, retenção, histórico de versões, parar de enviar listas de acesso por e-mail; 2 = local sem donos; 1 = "usar o SharePoint"; 0 = nada.

**EX015 — Teste da condição de parada.** *Objetivo:* tornar a cautela verificável. *Insumos:* uma atualização de firmware de fornecedor na KW-09 programada para 13:00–15:00. *Passos:* escrever três condições de parada e dizer quem tem autoridade para acioná-las. *Evidência esperada:* condições e autoridade. *Rubrica:* 3 = condições observáveis (alarme inesperado, perda de visão, ultrapassagem das 15:00, pedido de um operador) e o operador de turno ou o gerente de operações podem parar sem justificativa; 2 = condições vagas; 1 = o fornecedor decide; 0 = nada.

### Síntese do capítulo

A autorização faz o dono da consequência concordar de antemão com exatamente o que vai acontecer e permite que todos o provem depois. Uma autorização válida tem escopo com exclusões, atividades permitidas e proibidas, pessoas nomeadas, uma janela, condições de parada, tratamento de dados e autoridade por escrito. Os registros de decisão capturam o que se sabia na época; as evidências de governança ficam em locais controlados e com dono; o TLP diz aos parceiros até onde podem compartilhar.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Infraestrutura crítica e segurança setorial: métodos centrais

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- conduzir um ciclo simples e repetível de avaliação de riscos para um serviço essencial e manter um registro de riscos utilizável;
- explicar por que multiplicar probabilidade por consequência pode enganar em infraestrutura crítica e como classificar com a consequência primeiro;
- garantir que todo risco tenha um dono, um tratamento, uma data-limite e uma data de revisão, e detectar quando não tem;
- registrar adequadamente uma aceitação de risco, com autoridade, condições e validade.

Os Capítulos 1–3 deram a você linguagem, contexto e registros. Este capítulo os transforma no método central do coordenador.

### 4.1 O ciclo de avaliação de riscos

O NIST descreve a avaliação de riscos como um processo de preparar, conduzir, comunicar e manter a avaliação ([NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). Para um coordenador, um ciclo viável tem cinco passos:

1. **Enquadrar** — qual serviço, qual horizonte de tempo, quais consequências contam e qual é o apetite da liderança.
2. **Identificar** — reunir riscos candidatos a partir de incidentes, auditorias, conversas com a equipe, revisões de fornecedores, alertas e exercícios.
3. **Analisar** — escrever cada um como causa-evento-consequência; estimar a probabilidade e a consequência com as pessoas que sabem.
4. **Decidir** — o dono do risco escolhe um tratamento e uma data; a aceitação vai para o nível de autoridade adequado.
5. **Monitorar** — revisar segundo um calendário e quando algo mudar; reportar os principais riscos para cima.

O registro é a memória desse ciclo. Se o registro está desatualizado, o ciclo parou, diga a política o que disser.

### 4.2 Escalas e os seus limites

A maioria das organizações pontua a probabilidade e a consequência em escalas de 1 a 5. Torne-as significativas ancorando cada nível nos termos do seu serviço. Uma escala de consequência para a Kestrel Water poderia ser:

| Nível | Consequência (ancorada) |
|---|---|
| 5 | Risco à saúde ou à vida; água imprópria chega aos clientes; ou perda de abastecimento a um cliente crítico além do seu tempo de autonomia |
| 4 | Perda de abastecimento ou de pressão para mais de 10.000 pessoas por mais de 12 horas; provável ação coercitiva do regulador |
| 3 | Perda localizada de abastecimento; custo significativo; exposição de dados de clientes com dever de notificação |
| 2 | Perturbação absorvida pela operação manual; custo interno |
| 1 | Efeito desprezível sobre o serviço |

O produto usual, probabilidade × consequência, é conveniente, mas tem dois problemas conhecidos. Primeiro, permite que um problema menor e frequente fique acima de um catastrófico e raro (4 × 3 = 12 vence 2 × 5 = 10). Segundo, os números são rótulos ordinais, não medições, de modo que a aritmética sobre eles é mais fraca do que parece. Em serviços essenciais, uma convenção sensata é classificar com a **consequência primeiro** — tudo o que possa ferir pessoas ou exceder o tempo de autonomia de um cliente crítico vai para o topo — e usar o produto apenas para ordenar riscos de consequência semelhante. Seja qual for a regra escolhida, escreva-a, para que a classificação seja reproduzível e discutível.

### 4.3 Titularidade e higiene

Um risco sem dono é uma preocupação, não um risco gerenciado. A higiene do registro significa que cada entrada tem: um dono com autoridade sobre o serviço afetado; uma decisão de tratamento; uma data-limite para o tratamento; uma data da última revisão; e um link para a evidência do progresso. Um coordenador verifica a higiene com regularidade, porque a deterioração do registro é silenciosa: ninguém percebe que um risco "alto" foi revisto pela última vez há oito meses até que algo aconteça.

No Laboratório 4, o R02 mostra as três falhas ao mesmo tempo: sem dono, uma revisão de sete meses atrás e um tratamento atrasado, num risco de nível 5.

### 4.4 Aceitar riscos

A aceitação é um tratamento legítimo — nenhuma organização consegue consertar tudo de uma vez. Uma aceitação adequada registra quem aceitou o risco (num nível de autoridade compatível com a sua consequência), quais medidas compensatórias se aplicam, em que condições a aceitação caduca e quando ela expira. A NIS2 exige que os órgãos de gestão das entidades essenciais e importantes aprovem as medidas de gestão de riscos de cibersegurança e supervisionem a sua implementação ([Directive (EU) 2022/2555, Article 20](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Seja qual for a sua jurisdição, riscos com consequência de nível 5 devem ser aceitos pela diretoria ou pelo conselho, nunca silenciosamente pelo coordenador.

### 4.5 Exemplo resolvido: revisando o registro (sintético)

Em março, a coordenadora revisa o registro da Kestrel Water antes da reunião do comitê de auditoria e riscos do conselho. Ela usa o **Laboratório 4**, que codifica a convenção de classificação e as verificações de higiene para que qualquer pessoa possa executá-las de novo.

**Laboratório 4** (salve como `lab04.py` e execute com `python3 lab04.py`):

```python
# Lab 4 - consequence-led risk register review (offline, standard library only; all data synthetic)
import datetime as dt
TODAY = dt.date(2026, 3, 2)
# id, title, owner, likelihood 1-5, consequence 1-5, service affected, last review, treatment due
REGISTER = [
    ("R01", "Remote vendor access to station RTUs without MFA", "A. Mensah", 4, 5, "drinking water", "2026-01-10", "2026-04-30"),
    ("R02", "Single engineer knows chlorine dosing logic",       "",          3, 5, "drinking water", "2025-08-01", "2026-02-01"),
    ("R03", "Billing portal phishing of customer accounts",      "C. Okafor", 5, 3, "billing",        "2026-02-20", "2026-06-30"),
    ("R04", "Historian backups never test-restored",             "J. Tan",    3, 4, "drinking water", "2025-12-15", "2026-01-31"),
    ("R05", "Grid supply loss at pumping station KW-07",         "A. Mensah", 2, 5, "drinking water", "2026-02-01", "2026-09-30"),
    ("R06", "Office printer firmware outdated",                  "IT desk",   4, 1, "office IT",      "2026-02-25", "2026-05-31"),
    ("R07", "Hospital not told of planned pressure work",        "L. Ferreira",3, 4, "hospital supply","2025-06-30", "2026-03-31"),
]
SERVICE_WEIGHT = {"drinking water": 3, "hospital supply": 3, "billing": 1, "office IT": 0}
rows = []
for rid, title, owner, l, c, svc, rev, due in REGISTER:
    score = l * c
    flags = []
    if not owner: flags.append("NO OWNER")
    if (TODAY - dt.date.fromisoformat(rev)).days > 180: flags.append("REVIEW STALE")
    if dt.date.fromisoformat(due) < TODAY: flags.append("TREATMENT OVERDUE")
    if c == 5: flags.append("SEVERE CONSEQUENCE")
    rows.append((score, c, SERVICE_WEIGHT[svc], rid, title, flags))
print("Ranked by score only:")
for score, c, w, rid, title, flags in sorted(rows, key=lambda r: (-r[0], r[3])):
    print(f"  {rid} score={score:2d}")
print("Ranked by consequence, then service weight, then score:")
for i, (score, c, w, rid, title, flags) in enumerate(sorted(rows, key=lambda r: (-r[1], -r[2], -r[0], r[3])), 1):
    print(f"  {i}. {rid} c={c} w={w} score={score:2d} {'; '.join(flags) or 'ok'}")
print("Needs governance action:", ", ".join(r[3] for r in sorted(rows, key=lambda r: r[3]) if any(f != 'SEVERE CONSEQUENCE' for f in r[5])))
```

Saída esperada (Python 3.13.5):

```text
Ranked by score only:
  R01 score=20
  R02 score=15
  R03 score=15
  R04 score=12
  R07 score=12
  R05 score=10
  R06 score= 4
Ranked by consequence, then service weight, then score:
  1. R01 c=5 w=3 score=20 SEVERE CONSEQUENCE
  2. R02 c=5 w=3 score=15 NO OWNER; REVIEW STALE; TREATMENT OVERDUE; SEVERE CONSEQUENCE
  3. R05 c=5 w=3 score=10 SEVERE CONSEQUENCE
  4. R04 c=4 w=3 score=12 TREATMENT OVERDUE
  5. R07 c=4 w=3 score=12 REVIEW STALE
  6. R03 c=3 w=1 score=15 ok
  7. R06 c=1 w=0 score= 4 ok
Needs governance action: R02, R04, R07
```

Leia as duas classificações. Só pela pontuação, o risco de phishing do faturamento R03 (15) empata com o R02 e fica acima do R05 — uma perda de energia da rede numa estação de bombeamento que poderia deixar milhares de pessoas sem água. Classificados pela consequência e depois pela importância do serviço afetado, os três riscos de nível 5 da água potável vêm primeiro. As sinalizações de higiene mostram onde a governança, e não a tecnologia, está falhando: o R02 (um único engenheiro que entende a lógica de dosagem de cloro) está **sem dono**, não é revisto há sete meses e o seu tratamento está atrasado; o teste de restauração do R04 está atrasado; a revisão do R07 está desatualizada. Esses três vão ao comitê como **ações de governança**, com um dono proposto para o R02 (A. Mensah, que é dono da dosagem).

Note o que o laboratório não faz. Ele não diz se a "probabilidade 4" do R01 está certa — isso vem da conversa com as pessoas que conhecem o fornecedor e a ameaça. Ele torna explícita a regra de classificação e repetíveis as verificações de higiene; não faz o julgamento por você.

### 4.6 Atividade prática

Mude a chave de classificação do Laboratório 4 para ordenar apenas pela pontuação e mostre o resultado a um colega. Pergunte qual ordem ele defenderia numa reunião do conselho depois de uma falha de pressão no hospital. Depois escreva a regra de classificação da sua organização em duas frases.

Observe onde o R03 e o R05 caem em cada ordem, porque esse é o argumento que você enfrentaria depois de uma interrupção: um risco de phishing do faturamento classificado acima da perda de abastecimento numa estação de bombeamento é difícil de defender. Depois acrescente um risco inventado com consequência 5 e probabilidade 1 e verifique onde ele cai em cada regra. Por fim, execute as verificações de higiene com outra data TODAY, por exemplo seis meses depois, e veja quais revisões e tratamentos ficam desatualizados ou atrasados sem que ninguém perceba.

### 4.7 Erros comuns e limites

- Escalas sem âncoras, de modo que "4" significa coisas diferentes para pessoas diferentes.
- Aritmética sobre pontuações ordinais apresentada como precisão ("risco 13,6").
- Donos que são coordenadores ou comitês, em vez de gestores com autoridade.
- Aceitações sem validade, que se tornam permanentes por omissão.
- Registros que listam tecnologias ("SCADA") em vez de declarações de risco.
- Tratar o registro como o objetivo; ele é apenas a memória das decisões.

- Deixar um risco de nível 5 sem dono porque ninguém o quer, como aconteceu com o R02 durante meses.
- Pontuar a probabilidade sem conversar com as pessoas que conhecem o fornecedor ou a ameaça, de modo que o número reflete o palpite do coordenador.

### Exercícios — capítulo 4

**EX016 — Ancore uma escala.** *Objetivo:* tornar a probabilidade significativa. *Insumos:* a escala de consequência da seção 4.2. *Passos:* escrever uma escala de probabilidade de cinco níveis ancorada em tempo e evidências. *Evidência esperada:* a escala. *Rubrica:* 3 = níveis ligados a períodos ou evidências (por exemplo, 5 = já ocorreu aqui no último ano ou está sendo ativamente tentado no setor; 1 = nenhuma ocorrência conhecida no setor, exigiria várias condições improváveis); observa que os controles existentes são levados em conta; 2 = apenas períodos; 1 = palavras como "alta"; 0 = nada.

**EX017 — Leia o Laboratório 4.** *Objetivo:* interpretar a classificação e a higiene. *Insumos:* a saída do Laboratório 4. *Passos:* explicar por que o R03 passa de segundo empatado para sexto e por que o R05 sobe; listar as ações de governança e quem deve ser dono de cada uma. *Evidência esperada:* explicação e lista. *Rubrica:* 3 = o R03 tem consequência 3 sobre o faturamento; o R05 tem consequência 5 sobre a água potável; ações: dono do R02 (A. Mensah) e tratamento atrasado, teste de restauração atrasado do R04 (J. Tan, com A. Mensah como dono do serviço), revisão desatualizada do R07 (L. Ferreira, ou passar ao coordenador pela interlocução com o hospital); 2 = explicação sem donos; 1 = repete a saída; 0 = nada.

**EX018 — Aceite um risco adequadamente.** *Objetivo:* registrar a aceitação. *Insumos:* o conselho decide que não pode financiar a substituição dos controladores da estação KW-10 este ano. *Passos:* redigir o registro de aceitação. *Evidência esperada:* registro. *Rubrica:* 3 = nomeia a declaração de risco, a autoridade que aceita (diretor-presidente ou conselho, dada a consequência), medidas compensatórias (por exemplo, nenhum acesso remoto, monitoramento pelo KVROC, peças de reposição), condições que encerram a aceitação (novo alerta, incidente), data de validade e responsável pela revisão; 2 = sem validade; 1 = "aceito"; 0 = nada.

**EX019 — Estenda o laboratório.** *Objetivo:* codificar outra regra de higiene. *Insumos:* Laboratório 4. *Passos:* acrescentar uma sinalização "ACCEPTANCE EXPIRED" usando um novo campo, testá-la com uma aceitação expirada e uma válida e mostrar a saída. *Evidência esperada:* mudança no código e saída. *Rubrica:* 3 = campo acrescentado em todas as linhas, regra correta, dois casos de teste demonstram os dois resultados, e "Needs governance action" inclui a expirada; 2 = funciona sem testes; 1 = apenas a regra; 0 = nada.

**EX020 — Apresente ao comitê.** *Objetivo:* comunicar o registro. *Insumos:* a saída do Laboratório 4. *Passos:* escrever o resumo de uma página para o comitê de auditoria e riscos. *Evidência esperada:* resumo. *Rubrica:* 3 = principais riscos classificados por consequência, em linguagem simples, com donos e datas, ações de governança com as decisões solicitadas, declaração explícita da regra de classificação e dos seus limites, nenhuma "nota" única; 2 = lista riscos sem pedidos; 1 = cola a tabela; 0 = nada.

### Síntese do capítulo

A avaliação de riscos é um ciclo — enquadrar, identificar, analisar, decidir, monitorar — e o registro é a sua memória. Ancore as escalas nos termos do seu serviço, classifique com a consequência primeiro em serviços essenciais e trate as pontuações como ordinais. Todo risco precisa de um dono com autoridade, um tratamento, datas e evidências; a aceitação só é legítima com autoridade compatível, condições e validade.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Infraestrutura crítica e segurança setorial: ferramentas e interpretação

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- escolher entre os principais frameworks e linhas de base públicos para um serviço essencial e explicar para que serve cada um;
- ler de forma crítica uma autoavaliação ou uma nota de maturidade: o que ela mede, quem a produziu e o que ela não consegue mostrar;
- desenhar um pequeno conjunto de métricas do programa que conduzam decisões, em vez de enfeitar relatórios;
- interpretar constatações técnicas entregues por engenheiros e fornecedores bem o bastante para fazer as perguntas de acompanhamento certas.

As "ferramentas" do coordenador são, na maior parte, documentos e medidas. O Capítulo 4 construiu o registro; este capítulo fornece as réguas externas e os números que reportam sobre ele.

### 5.1 O panorama dos frameworks

Você vai encontrar várias referências que se sobrepõem. Cada uma tem uma finalidade distinta:

| Referência | Para que serve | Uso típico pelo coordenador |
|---|---|---|
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Taxonomia de resultados (Governar, Identificar, Proteger, Detectar, Responder, Recuperar) | Estruturar o programa e os perfis; conversar com a diretoria |
| [CISA Cross-Sector Cybersecurity Performance Goals (CPGs)](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) | Um subconjunto priorizado de práticas de alto impacto para infraestrutura crítica | Linha de base rápida; encontrar primeiro as lacunas óbvias |
| [NCSC Cyber Assessment Framework (CAF)](https://www.ncsc.gov.uk/collection/caf) | Avaliação baseada em resultados para operadores de serviços essenciais, com indicadores de boas práticas | Autoavaliação estruturada, diálogo com o regulador (contexto do Reino Unido) |
| [Série ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | Normas para a segurança de sistemas de automação e controle industrial, cobrindo proprietários de ativos, integradores e fornecedores de produtos | Requisitos de aquisição e de fornecedores; expectativas do programa para a TO |
| [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Orientações para proteger a TO | Vocabulário compartilhado com os engenheiros |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Catálogo de controles de segurança e privacidade | Linguagem detalhada de controles, quando necessária |

A regra do coordenador: **uma estrutura principal** (por exemplo, o CSF 2.0) para o programa, com as outras referências mapeadas para ela, em vez de quatro planilhas paralelas. Os requisitos regulatórios da sua jurisdição vêm primeiro; os frameworks ajudam a cumpri-los, não os substituem.

### 5.2 Lendo uma avaliação

Um resultado de avaliação como "Proteger: 2,4 / 4" ou "cobertura dos CPGs de 71%" convida a uma falsa confiança. Antes de repeti-lo, faça cinco perguntas:

1. **O que foi avaliado?** Quais locais, sistemas e processos — e quais não foram?
2. **Quem avaliou, e como?** Autoavaliação pelo dono do sistema, um par, um avaliador independente? Por entrevista, revisão de documentos ou teste?
3. **O que conta como "atendido"?** Uma política escrita, uma política em uso ou uma política que comprovadamente funciona?
4. **Quando?** Avaliações envelhecem depressa depois de reorganizações, trocas de fornecedor e incidentes.
5. **Que decisão ela apoia?** Se nenhuma decisão muda em função do número, ele é enfeite.

Uma autoavaliação tem valor — é barata e constrói entendimento —, mas mede aquilo em que os donos acreditam. O Capítulo 7 acrescenta formas de obter evidências mais fortes.

### 5.3 Métricas que conduzem decisões

Boas métricas de programa têm três propriedades em comum: relacionam-se a uma consequência ou a um controle que protege contra ela; o seu dono consegue alterá-las; e um limiar dispara uma ação conhecida. Compare:

| Métrica fraca | Métrica melhor | Ação no limiar |
|---|---|---|
| Número de políticas de segurança | % dos riscos de nível 5 com dono e tratamento dentro do prazo | Abaixo de 100% → escalonamento à diretoria |
| E-mails de phishing bloqueados | Mediana do tempo entre o fim do contrato de um fornecedor e a remoção da conta | Acima de 5 dias úteis → revisão do processo de acesso |
| Vulnerabilidades encontradas | % de interfaces operacionais expostas à internet (deveria ser zero) | Qualquer uma → notificação imediata ao dono |
| Conclusão de treinamentos | % de gerentes de plantão que participaram de um exercício nos últimos 12 meses | Abaixo de 80% → agendar exercício |

Contagens de atividade ("bloqueamos 40.000 ataques") são fáceis de produzir e raramente úteis para decisões. Prefira medidas de exposição, tempestividade e cobertura das coisas que mais importam.

### 5.4 Interpretando constatações técnicas

Engenheiros, o KVROC e fornecedores enviam constatações. Você não precisa verificá-las tecnicamente, mas precisa fazer perguntas que as deixem prontas para decisão:

- **O que é afetado** — qual local, qual função, qual nível de consequência?
- **Como você sabe** — observado diretamente, inferido ou relatado por uma ferramenta que pode estar errada?
- **Qual é a exposição** — alcançável a partir da internet, da rede de escritório, apenas no local?
- **Qual é a ação recomendada, por quem, até quando, e o que ela perturba?**
- **Existe um alerta público?** Se existir, coloque o link; alertas como o da CISA para o setor de água sobre controladores expostos à internet com senhas padrão ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)) ajudam a diretoria a entender que uma constatação não é hipotética.

### 5.5 Exemplo resolvido: uma autoavaliação pelos CPGs (sintético)

L. Ferreira preencheu uma lista de verificação dos CPGs para a Kestrel Water e relata "71% das metas atendidas". A coordenadora faz as cinco perguntas e descobre: a avaliação cobriu a rede corporativa e a estação de tratamento, mas **não** as doze estações; as respostas eram "sim" se existisse uma política; e ela foi feita antes da mudança no arranjo de acesso remoto da HydroLogic. Dois itens "atendidos" — sobre autenticação multifator para acesso remoto e sobre a revogação de credenciais de funcionários que saem — não têm evidência para as contas de fornecedores.

Ela relata à diretoria: "*Uma autoavaliação da TI corporativa e da estação de tratamento constatou que a maioria das práticas de base está implementada no papel. Ela não cobriu as estações, e dois itens que mais importam para as estações — autenticação multifator para acesso remoto e remoção tempestiva de contas — não estão verificados para os fornecedores. Proponho uma revisão do acesso de fornecedores em maio (Capítulo 8) e repetir a avaliação, incluindo as estações, até setembro.*" Os 71% ficam num apêndice.

### 5.6 Atividade prática

Pegue qualquer painel público ou declaração de relatório anual sobre cibersegurança (por exemplo, "100% da equipe treinada"). Aplique as cinco perguntas e reescreva-a como uma declaração pronta para decisão, anotando o que você precisaria saber.

Escreva a sua reescrita na mesma forma do relatório da coordenadora sobre a autoavaliação pelos CPGs: o que foi coberto, como foi julgado, o que ficou de fora e que decisão decorre. Se a declaração não apoia nenhuma decisão, diga isso; isso já é uma constatação. Mantenha o número original, mas coloque-o depois do contexto, e não na frente. Anote a data da declaração e se algo mudou desde então, como uma reorganização ou um novo fornecedor.

### 5.7 Erros comuns e limites

- Usar vários frameworks em paralelo sem mapeamento.
- Relatar percentuais sem escopo e método.
- Escolher métricas porque os dados são fáceis de obter.
- Tratar o marketing de um fornecedor ("conforme a 62443") como uma avaliação da sua instalação.
- Esquecer que frameworks e linhas de base são revisados; cite a versão e a data.

- Contar uma meta como atendida porque existe uma política, como fez a autoavaliação pelos CPGs, sem perguntar se ela está em uso ou se comprovadamente funciona.
- Deixar de fora parte do serviço, como as doze estações, e ainda assim relatar um único número para a empresa inteira.
- Repetir um resultado de avaliação à diretoria antes de perguntar quando ela foi feita e o que mudou desde então.

### Exercícios — capítulo 5

**EX021 — Escolha uma estrutura principal.** *Objetivo:* selecionar e mapear frameworks. *Insumos:* a Kestrel Water precisa reportar ao seu regulador, compra sistemas de TO de fornecedores e tem um conselho pouco familiarizado com segurança. *Passos:* propor uma estrutura principal e como os CPGs e a 62443 se relacionam com ela. *Evidência esperada:* uma justificativa curta. *Rubrica:* 3 = requisitos regulatórios primeiro, CSF 2.0 como estrutura do programa para o conselho, CPGs como linha de base priorizada mapeada para ele, 62443 usada para requisitos de fornecedores e de aquisição; 2 = escolha sem mapeamento; 1 = "fazer todos"; 0 = nada.

**EX022 — Interrogue uma nota.** *Objetivo:* aplicar as cinco perguntas. *Insumos:* "Maturidade em Detectar 3,1/5, acima de 2,6". *Passos:* escrever as cinco perguntas aplicadas a essa nota e dizer que resposta tornaria a melhora crível. *Evidência esperada:* perguntas e critérios. *Rubrica:* 3 = pergunta escopo, avaliador e método, definição dos níveis, data e decisão apoiada; crível se o escopo e o método forem os mesmos, independente ou baseada em evidências, e ligada a um resultado observado (por exemplo, a detecção de uma injeção de exercício); 2 = apenas perguntas; 1 = aceita; 0 = nada.

**EX023 — Conserte as métricas.** *Objetivo:* desenhar métricas que conduzam decisões. *Insumos:* relatório mensal atual: e-mails bloqueados, detecções de antivírus, políticas aprovadas, equipe treinada. *Passos:* substituir por quatro métricas, incluindo dono e ação no limiar. *Evidência esperada:* tabela. *Rubrica:* 3 = métricas ligadas à consequência e ao controle (por exemplo, higiene dos riscos de nível 5, tempo de remoção de contas de fornecedores, exposição de interfaces operacionais, participação em exercícios), cada uma com dono e ação; 2 = métricas sem ações; 1 = mudanças cosméticas; 0 = nada.

**EX024 — Deixe uma constatação pronta para decisão.** *Objetivo:* questionar uma constatação técnica. *Insumos:* e-mail do KVROC: "Vimos RDP da internet para o hmi-02 ontem à noite, recomendamos bloquear." *Passos:* escrever a resposta. *Evidência esperada:* resposta. *Rubrica:* 3 = pergunta a qual local e função o hmi-02 serve, se a conexão teve sucesso, a origem e as evidências, se ainda está exposto; pergunta quem pode bloquear e o que o bloqueio perturba (acesso de fornecedor?); envolve o dono operacional; trata como potencialmente urgente; 2 = pergunta parte disso; 1 = "favor bloquear"; 0 = nada.

**EX025 — Relate com honestidade.** *Objetivo:* comunicar os limites de uma avaliação. *Insumos:* o exemplo resolvido 5.5. *Passos:* reescrever a mensagem da diretoria para o conselho em menos de 100 palavras. *Evidência esperada:* mensagem. *Rubrica:* 3 = declara com clareza a lacuna de cobertura e os itens não verificados, dá o plano e a data, evita o percentual como manchete; 2 = menciona o percentual primeiro, mas inclui os limites; 1 = "71% conforme"; 0 = nada.

### Síntese do capítulo

Frameworks e linhas de base são réguas: escolha uma estrutura principal, cumpra a lei primeiro e mapeie o resto. Leia toda avaliação pelo escopo, método, definição, data e decisão apoiada. Meça a exposição, a tempestividade e a cobertura do que importa, com donos e ações nos limiares. Deixe as constatações técnicas prontas para decisão perguntando o quê, como se sabe, quão exposto, quem age e o que é perturbado.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Infraestrutura crítica e segurança setorial: fluxo operacional

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- definir os papéis de que um programa de segurança de infraestrutura crítica precisa e como eles se relacionam com as operações;
- construir e verificar uma matriz RACI para que toda atividade-chave tenha exatamente uma pessoa que responde por ela e um líder claro;
- conduzir a governança de mudanças entre TI e TO sem bloquear as operações nem contornar a segurança;
- desenhar um caminho de escalonamento, do operador de turno até a diretoria, que funcione às 03:00 de um domingo.

O Capítulo 5 deu a você réguas. Este capítulo faz o programa funcionar no dia a dia.

### 6.1 Papéis

No porte da Kestrel Water, os papéis abaixo podem ser divididos entre um punhado de pessoas. O que importa é que cada um seja atribuído:

- **Patrocinador executivo** (diretor de operações) — é dono do programa, aceita riscos altos, resolve conflitos entre departamentos.
- **Donos de serviço** (gerente de operações para o tratamento e as estações; gerente de atendimento ao cliente para o faturamento) — são donos dos riscos e das decisões dos seus serviços.
- **Coordenador** — conduz o ciclo: registro, registros de decisão, exercícios, relatórios, revisões de fornecedores.
- **Líder de segurança** — assessoria técnica de segurança e interlocução de monitoramento com o KVROC.
- **Engenheiro de sistemas de controle** — configuração e mudanças nos sistemas operacionais.
- **Líder de comunicação** — mensagens ao público e à imprensa.
- **Líder de incidente** (em rodízio, de plantão) — comanda a resposta quando um incidente é declarado.
- **Fornecedores** — trabalham sob autorização; nunca são donos de decisões sobre o seu serviço.

As orientações do NIST para resposta a incidentes enfatizam a definição de papéis e responsabilidades, incluindo os de fora da equipe de segurança, antes dos incidentes ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).

### 6.2 RACI

Uma matriz **RACI** lista atividades contra pessoas, com uma letra para cada: **R**esponsável (executa o trabalho), **A**provador (responde pelo resultado e dá a aprovação final — exatamente um por atividade), **C**onsultado (contribuição de mão dupla antes da decisão), **I**nformado (avisado depois). Duas regras pegam a maioria dos defeitos:

1. Exatamente um **A** por atividade. Zero significa que ninguém responde; dois significa que cada um pressupõe que o outro vai responder.
2. Pelo menos um **R** e, quando houver vários, um líder nomeado.

Acrescente duas verificações do coordenador: ninguém deve ser o aprovador do próprio acesso ou do próprio trabalho; e ninguém deve acumular tantas entradas R e A num incidente que se torne um gargalo.

### 6.3 Governança de mudanças entre TI e TO

Mudanças nos sistemas operacionais podem afetar o processo físico. Um processo de mudanças viável para uma empresa pequena tem três classes:

- **Padrão** — pré-aprovada, de baixo risco, repetível (substituir o teclado defeituoso de um operador): registre-a.
- **Normal** — avaliada e aprovada pelo dono do serviço, com um plano de teste ou de reversão e uma janela acordada com as operações.
- **Emergencial** — necessária agora para proteger pessoas ou o serviço; aprovada verbalmente pelo líder de incidente ou pelo dono do serviço, registrada em até 24 horas e revista depois.

O interesse do coordenador é que mudanças relevantes para a segurança (novo acesso remoto, mudanças em regras de firewall, novos fornecedores, software nos computadores da sala de controle) não possam escorregar para a classe "padrão", e que as mudanças emergenciais feitas durante incidentes sejam revistas em vez de se tornarem permanentes.

### 6.4 Escalonamento

Um caminho de escalonamento responde, para cada nível de gravidade: quem é chamado, por quem, como, em quanto tempo e o que acontece se a pessoa não atender. Escreva-o como uma tabela com substitutos, teste-o (Capítulo 11) e coloque-o onde os operadores do turno da noite possam encontrá-lo sem um computador — um cartão impresso na sala de controle —, porque o incidente pode ter levado os computadores.

O cartão da Kestrel Water lista o líder de incidente, o gerente de operações e o líder de segurança, com um substituto nomeado para cada um, além de números de celular que não dependem da rede corporativa.

### 6.5 Exemplo resolvido: verificando a RACI de incidentes (sintético)

A coordenadora redige a RACI de incidentes da Kestrel Water e executa o **Laboratório 6**, que aplica as regras da seção 6.2.

**Laboratório 6** (salve como `lab06.py` e execute com `python3 lab06.py`):

```python
# Lab 6 - RACI matrix check for incident coordination (offline, standard library only; synthetic)
PEOPLE = ["Coordinator", "Ops manager", "Security lead", "Comms", "Vendor", "CEO"]
# activity -> one letter per person (R responsible, A accountable, C consulted, I informed, - none)
RACI = {
    "Declare cyber incident":            "R A C I - I",
    "Decide to isolate stations":        "C A R I C I",
    "Switch stations to manual operation":"I A - - - I",
    "Notify regulator":                  "R - C C - A",
    "Brief hospital (critical customer)":"R C I R - A",
    "Approve vendor remote session":     "C A A - R -",
    "Public statement":                  "C C C R - -",
}
issues = []
load = {p: 0 for p in PEOPLE}
for act, codes in RACI.items():
    c = codes.split()
    assert len(c) == len(PEOPLE), act
    a = [p for p, x in zip(PEOPLE, c) if x == "A"]
    r = [p for p, x in zip(PEOPLE, c) if x == "R"]
    for p, x in zip(PEOPLE, c):
        if x in "RA": load[p] += 1
    if len(a) != 1: issues.append(f"{act}: {len(a)} accountable ({', '.join(a) or 'none'})")
    if not r: issues.append(f"{act}: nobody responsible")
    if len(r) > 1: issues.append(f"{act}: {len(r)} responsible ({', '.join(r)}) - name a lead")
    if act.startswith("Approve") and c[PEOPLE.index("Vendor")] in "RA":
        issues.append(f"{act}: vendor is responsible for approving its own access")
for i in issues: print("ISSUE", i)
print("R/A load:", ", ".join(f"{p}={n}" for p, n in load.items()))
print(f"{len(issues)} issues in {len(RACI)} activities")
```

Saída esperada (Python 3.13.5):

```text
ISSUE Switch stations to manual operation: nobody responsible
ISSUE Brief hospital (critical customer): 2 responsible (Coordinator, Comms) - name a lead
ISSUE Approve vendor remote session: 2 accountable (Ops manager, Security lead)
ISSUE Approve vendor remote session: vendor is responsible for approving its own access
ISSUE Public statement: 0 accountable (none)
R/A load: Coordinator=3, Ops manager=4, Security lead=2, Comms=2, Vendor=1, CEO=2
5 issues in 7 activities
```

Cinco defeitos em sete atividades:

- **Switch stations to manual operation** (passar as estações para operação manual) tem um aprovador (o gerente de operações), mas nenhum responsável — na prática, quem faz isso são os operadores de turno e os técnicos de plantão, e eles não estão na matriz. A correção é acrescentar o supervisor de turno como R.
- **Brief hospital** (informar o hospital) tem dois responsáveis. A coordenadora e a comunicação podem achar, cada uma, que a outra ligou. Nomeie a coordenadora como líder (é uma interlocução operacional), com a comunicação consultada sobre a redação.
- **Approve vendor remote session** (aprovar a sessão remota do fornecedor) tem dois aprovadores e lista o fornecedor como responsável. O gerente de operações deve ser o único A (é dono das estações); o líder de segurança é C; o fornecedor *solicita* o acesso e é I quanto à decisão — uma parte nunca deve aprovar o próprio acesso.
- **Public statement** (declaração pública) não tem aprovador. O diretor-presidente deve ser A, e a comunicação, R.

A linha de carga mostra o gerente de operações com quatro entradas R/A — durante um incidente, a mesma pessoa está operando a planta. A coordenadora propõe um substituto para as entradas ligadas ao incidente. O laboratório verifica apenas a estrutura; se as pessoas certas foram escolhidas é um julgamento do patrocinador executivo.

### 6.6 Atividade prática

Escreva uma RACI para "integrar um novo fornecedor com acesso remoto" usando pelo menos cinco papéis e verifique-a contra as quatro regras, à mão ou editando o Laboratório 6.

Inclua o fornecedor como papel e garanta que ele nunca aprove o próprio acesso, o que o Laboratório 6 verifica explicitamente. Nomeie quem é o aprovador da criação da conta, quem verifica se o contrato tem as cláusulas de segurança e quem é informado quando a conta é habilitada. Depois conte as entradas R e A de cada pessoa: se um nome aparece em quase todas as linhas, a integração vai travar sempre que essa pessoa estiver de folga. Mostre o resultado ao gerente de operações e pergunte se falta alguém.

### 6.7 Erros comuns e limites

- Comitês como aprovadores ("o conselho de segurança").
- RACIs escritas só para dias normais, não para incidentes.
- Mudanças emergenciais nunca revistas.
- Listas de escalonamento sem substitutos, ou guardadas apenas na rede.
- Uma RACI é um contrato social: publique-a, repasse-a com cada pessoa e atualize-a depois de reorganizações.

- Deixar fora da matriz as pessoas que de fato fazem o trabalho, como o Laboratório 6 constatou com os operadores de turno na operação manual.
- Permitir que uma parte aprove o próprio acesso, como um fornecedor marcado como responsável por aprovar a sua sessão remota.
- Dar a uma pessoa tantas entradas R e A que o incidente passa a depender só dela.

### Exercícios — capítulo 6

**EX026 — Conserte a RACI.** *Objetivo:* corrigir defeitos. *Insumos:* a matriz do Laboratório 6. *Passos:* propor linhas corrigidas para os cinco problemas e executar de novo a verificação (à mão ou com código). *Evidência esperada:* matriz corrigida e resultado limpo. *Rubrica:* 3 = zero problemas, o fornecedor nunca é A nem R na aprovação, um papel de turno acrescentado para a operação manual, um único líder para informar o hospital, o diretor-presidente como aprovador da declaração pública; 2 = resta um problema; 1 = parcial; 0 = nada.

**EX027 — Classifique mudanças.** *Objetivo:* aplicar as classes de mudança. *Insumos:* (a) nova regra de firewall permitindo uma VPN de fornecedor; (b) substituir a bateria defeituosa de um nobreak no armário de uma estação; (c) desabilitar uma conta comprometida durante um incidente; (d) instalar um agente de monitoramento no historiador. *Passos:* classificar e justificar. *Evidência esperada:* quatro classes. *Rubrica:* 3 = (a) normal (relevante para a segurança), (b) padrão, se existir um procedimento pré-aprovado, (c) emergencial com revisão posterior, (d) normal, com verificação de compatibilidade junto ao fornecedor; 2 = três certas; 1 = todas padrão; 0 = nada.

**EX028 — Cartão de escalonamento.** *Objetivo:* desenhar um caminho de escalonamento utilizável. *Insumos:* os papéis da seção 6.1. *Passos:* escrever o cartão impresso para os operadores do turno da noite para um suposto evento cibernético. *Evidência esperada:* conteúdo do cartão. *Rubrica:* 3 = gatilhos observáveis, primeira ligação e substituto com espaços para os números de telefone, limites de tempo, o que fazer enquanto isso (segurança primeiro, não desligar computadores sem instrução, anotar os horários), quando ligar diretamente para o líder de incidente; 2 = sem substitutos; 1 = "ligar para a TI"; 0 = nada.

**EX029 — Análise de gargalo.** *Objetivo:* usar a linha de carga. *Insumos:* a saída de carga do Laboratório 6. *Passos:* propor como reduzir a carga do gerente de operações durante incidentes sem enfraquecer a sua autoridade sobre a segurança. *Evidência esperada:* proposta. *Rubrica:* 3 = mantém as decisões de segurança com as operações, mas delega a interlocução e a aprovação de fornecedores a um substituto nomeado ou ao líder de incidente, com o gerente de operações consultado; 2 = delegação sem a ressalva de segurança; 1 = passa as decisões de segurança para a TI; 0 = nada.

**EX030 — Revisão de mudanças emergenciais.** *Objetivo:* encerrar mudanças emergenciais. *Insumos:* durante um incidente, um engenheiro acrescentou uma regra de firewall bloqueando todo acesso de fornecedores e criou uma conta temporária de administrador local. *Passos:* descrever a revisão pós-incidente. *Evidência esperada:* passos da revisão. *Rubrica:* 3 = listar as mudanças emergenciais a partir do registro, decidir manter/modificar/reverter cada uma, com dono, remover a conta temporária, restabelecer o acesso de fornecedores apenas pelo processo normal, atualizar a documentação; 2 = alguns passos; 1 = "deixar como está"; 0 = nada.

### Síntese do capítulo

Um programa funciona com papéis atribuídos, uma RACI com um aprovador por atividade e um líder nomeado, uma governança de mudanças que mantém visíveis as mudanças relevantes para a segurança e um caminho de escalonamento que funciona offline, de noite. Verifique a estrutura da RACI, a titularidade das aprovações e a carga durante incidentes; revise toda mudança emergencial depois do evento.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Infraestrutura crítica e segurança setorial: controles e verificação

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- descrever um controle em termos que um gestor possa assumir: objetivo, dono, operação e evidência;
- distinguir níveis de garantia — declarado, documentado, observado, testado — e decidir de qual nível cada controle precisa;
- planejar um programa de verificação proporcional para os controles que protegem contra consequências de nível 5;
- gerenciar exceções a controles como decisões de risco com prazo e com dono.

O Capítulo 6 fez o programa funcionar. Este capítulo pergunta se as suas proteções realmente funcionam.

### 7.1 O que é um controle, para um gestor

Um **controle** é uma medida que modifica o risco (a [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) cataloga milhares deles). Para fins de coordenação, descreva cada controle importante num único cartão:

- **Objetivo** — qual risco ele trata e como ("impede o uso de uma senha roubada de fornecedor para entrar nas estações");
- **Dono** — quem responde pelo seu funcionamento;
- **Operação** — o que acontece, com que frequência e por quem ("o gateway de acesso remoto exige um segundo fator para toda conta de fornecedor");
- **Evidência** — o que mostraria que ele está funcionando, e onde é guardada;
- **Sinal de falha** — o que você veria se ele parasse de funcionar.

Controles sem dono se deterioram, assim como riscos sem dono.

### 7.2 Níveis de garantia

Quão seguro você está de que um controle funciona? Quatro níveis úteis:

| Nível | Significado | Exemplo de evidência |
|---|---|---|
| Declarado | Alguém diz que ele existe | "Sim, os fornecedores usam MFA", numa reunião |
| Documentado | Uma política ou um projeto o descreve | Norma de acesso remoto v2 |
| Observado | Registros mostram que ele está operando | Exportação da configuração do gateway; logs de login mostrando eventos de segundo fator |
| Testado | Um teste deliberado mostrou que ele impede o que deve impedir | Uma tentativa supervisionada de login só com senha é recusada, registrada num relatório de teste |

Níveis mais altos custam mais. Um programa proporcional busca o nível **testado** para os controles que protegem contra consequências de nível 5, **observado** para os níveis 3–4, e aceita **documentado** para o restante. As orientações do NIST sobre monitoramento contínuo descrevem a manutenção de uma consciência permanente sobre se os controles continuam eficazes ([NIST SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

### 7.3 Quem verifica

- **Primeira linha** — os donos dos controles verificam os próprios controles (autoavaliação, verificações de rotina).
- **Segunda linha** — o coordenador ou a função de segurança revisa as evidências e faz amostragens.
- **Terceira linha** — a auditoria interna ou um avaliador independente dá garantia ao conselho.

O coordenador costuma desenhar o plano de verificação e conduzir as verificações de segunda linha. Testes em sistemas operacionais precisam ser autorizados como qualquer outro trabalho (Capítulo 3), e, em ambientes de controle, um "teste" muitas vezes é uma revisão de configuração e de logs, e não uma tentativa ativa.

As verificações de segunda linha devem amostrar as evidências diretamente, em vez de aceitar o resumo do dono.

### 7.4 Exceções

Às vezes um controle não pode ser aplicado: um controlador antigo de estação não suporta um segundo fator; um dispositivo médico não pode receber correções sem perder a sua certificação. Uma **exceção** é uma decisão registrada e com dono de operar sem o controle, o que é uma forma de aceitação de risco (Capítulo 4). Ela precisa de: o controle e o sistema em questão; o motivo; medidas compensatórias; a autoridade que aceita; uma data de validade; e um plano para eliminar a exceção. Um registro de exceções é revisto junto com o registro de riscos.

Na Kestrel Water, a exceção do controlador da KW-10 foi ao conselho com validade até março.

### 7.5 Exemplo resolvido: verificando três controles (sintético)

A coordenadora escolhe três controles que protegem contra riscos de nível 5 e verifica cada um:

| Controle | Declarado / documentado | Observado | Testado | Constatação |
|---|---|---|---|---|
| C1: MFA para todo acesso remoto de fornecedores | Sim — norma de acesso remoto v2 | A exportação do gateway mostra MFA em 5 de 6 contas de fornecedores | Ainda não | A conta da ScadaCo não tem MFA (confirmado depois no Laboratório 8). **Lacuna.** |
| C2: Backups do historiador restauráveis em até 24 h | Sim — procedimento de backup | Os jobs de backup têm sucesso todas as noites | Último teste de restauração: nunca | **Não verificado** — backup bem-sucedido ≠ restauração bem-sucedida (ligado ao risco R04). |
| C3: Limites de dosagem impostos na lógica do controlador | Sim — documento de projeto | Limites visíveis na revisão de configuração feita por J. Tan | Teste de bancada supervisionado pelo fornecedor num controlador reserva, registrado em 3 de fevereiro | **Verificado** no nível testado para o reserva; a configuração de produção coincide por checksum. |

O plano de verificação que se segue: corrigir o C1 em até 30 dias (dono: A. Mensah); agendar um teste de restauração do C2 em até 60 dias, com resultado cronometrado (dono: J. Tan); repetir a verificação do C3 depois de qualquer mudança de lógica. A coordenadora relata o nível de garantia de cada controle, e não uma declaração única de "controles eficazes".

### 7.6 Atividade prática

Escreva cartões de controle (objetivo, dono, operação, evidência, sinal de falha) para dois controles de uma organização que você conheça e atribua a cada um o nível de garantia atual, com justificativa.

Para cada cartão, diga como o sinal de falha apareceria na prática, por exemplo um login de fornecedor sem evento de segundo fator no log do gateway. Explique por que você escolheu o nível de garantia, citando as evidências que você de fato viu. Depois decida que nível o controle deveria atingir, dada a consequência contra a qual protege, e que passo o elevaria, por exemplo um teste de restauração para um backup que só foi observado tendo sucesso. Mantenha os cartões curtos o bastante para que um dono os atualize.

### 7.7 Erros comuns e limites

- Igualar "o job teve sucesso" a "o controle funciona" (backups, correções).
- Verificação apenas nos níveis declarado ou documentado para controles críticos.
- Testes ativos de sistemas operacionais sem autorização e sem a concordância das operações.
- Exceções sem validade, que silenciosamente se tornam o projeto.
- Relatar controles como "eficazes" sem dizer como isso foi estabelecido.

- Tratar a própria declaração de um fornecedor de que a MFA está habilitada como evidência observada, quando só a exportação do gateway a mostra.
- Verificar um controle uma vez e nunca mais, de modo que uma mudança posterior de configuração o remove silenciosamente.
- Testar um sistema reserva ou de bancada e esquecer de confirmar que a produção coincide, como o C3 fez por checksum.

### Exercícios — capítulo 7

**EX031 — Escreva um cartão de controle.** *Objetivo:* tornar um controle assumível. *Insumos:* "As contas de fornecedores são removidas quando os contratos terminam." *Passos:* escrever o cartão em cinco partes. *Evidência esperada:* cartão. *Rubrica:* 3 = objetivo ligado a um risco, dono com autoridade (gerente de operações ou dono do contrato), operação com gatilho e prazo, evidência (conciliação mensal das contas com os contratos), sinal de falha (existem contas de contratos encerrados); 2 = falta o sinal de falha; 1 = repete a frase; 0 = nada.

**EX032 — Atribua metas de garantia.** *Objetivo:* aplicar a proporcionalidade. *Insumos:* controles: MFA para acesso de fornecedores; política de senhas para notebooks do escritório; procedimento de operação manual das estações; crachás de visitante na sede. *Passos:* atribuir os níveis de garantia-alvo e justificar pela consequência. *Evidência esperada:* quatro metas. *Rubrica:* 3 = testado para a MFA de fornecedores e para a operação manual (por exercício ou simulado), documentado ou observado para os demais, com raciocínio; 2 = metas sem razões; 1 = tudo testado; 0 = nada.

**EX033 — Desenhe um teste de restauração.** *Objetivo:* verificar o C2. *Insumos:* o exemplo resolvido. *Passos:* esboçar o teste, os critérios de sucesso e a autorização. *Evidência esperada:* esboço. *Rubrica:* 3 = restauração num ambiente isolado, não na produção; cronometrada contra o objetivo de 24 h; verifica a completude dos dados para um período escolhido; autorizado pelo dono do serviço; resultado registrado com data e evidência; 2 = sem critérios de sucesso; 1 = "conferir os logs de backup"; 0 = nada.

**EX034 — Escreva uma exceção.** *Objetivo:* gerenciar uma lacuna de controle. *Insumos:* o controlador da KW-10 não suporta MFA para o acesso local de engenharia. *Passos:* redigir a exceção. *Evidência esperada:* registro de exceção. *Rubrica:* 3 = controle e sistema, motivo, medidas compensatórias (nenhum caminho remoto, controle de acesso físico, monitoramento de mudanças), autoridade que aceita compatível com a consequência, validade, plano de eliminação; 2 = sem validade; 1 = "não é possível"; 0 = nada.

**EX035 — Relate a garantia.** *Objetivo:* comunicar a verificação com honestidade. *Insumos:* a tabela do exemplo resolvido. *Passos:* escrever três linhas para a diretoria, uma por controle. *Evidência esperada:* três linhas. *Rubrica:* 3 = cada uma declara o nível de garantia alcançado, a lacuna ou o resultado, o dono e a data; evita "eficaz" sem evidência; 2 = faltam datas; 1 = "controles eficazes"; 0 = nada.

### Síntese do capítulo

Um controle é algo que um gestor pode assumir: objetivo, dono, operação, evidência e sinal de falha. A garantia sobe de declarado para documentado, observado e testado; busque o nível testado nos controles que protegem contra as piores consequências. Verifique de forma proporcional pelas três linhas, autorize os testes como qualquer outro trabalho e mantenha as exceções com dono, compensadas e com prazo.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 12

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Infraestrutura crítica e segurança setorial: análise supervisionada de caso

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- analisar um problema de acesso de fornecedor como um caso de governança: contratos, contas, pessoas e evidências;
- conduzir uma revisão periódica do acesso remoto de terceiros e agir sobre as suas constatações de forma proporcional;
- inscrever requisitos de segurança para fornecedores nos contratos e na integração;
- apresentar uma análise de caso a um supervisor com as decisões solicitadas, as evidências anexadas e a incerteza rotulada.

Este é o primeiro caso supervisionado do livro. Ele reúne risco (Capítulo 4), papéis (Capítulo 6) e verificação de controles (Capítulo 7).

### 8.1 Por que os fornecedores importam tanto aqui

Os serviços essenciais dependem de fornecedores para equipamentos, software, manutenção e monitoramento. O acesso remoto de fornecedores é conveniente — um especialista em bombas consegue resolver um problema a 200 quilômetros de distância, à noite — e é também uma via recorrente de comprometimento. As orientações da CISA sobre mitigações primárias para a TO incluem, entre as prioridades, reduzir a exposição e proteger o acesso remoto ([CISA, Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology)). As orientações do NIST sobre a cadeia de suprimentos tratam os fornecedores como parte do risco da organização e recomendam integrar a gestão de riscos da cadeia de suprimentos à governança e às aquisições ([NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)). A NIS2 inclui a segurança da cadeia de suprimentos entre as medidas de gestão de riscos que as entidades precisam adotar ([Directive (EU) 2022/2555, Article 21](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)).

### 8.2 O ciclo de vida do fornecedor

A governança de um fornecedor com acesso segue um ciclo de vida:

1. **Selecionar** — perguntas de segurança na aquisição, proporcionais ao acesso solicitado.
2. **Contratar** — obrigações de segurança: pessoas nomeadas, MFA, notificação de incidentes e de desligamentos de pessoal, direito de revisão, tratamento de dados, apoio à sua resposta a incidentes.
3. **Integrar** — contas criadas por pessoa nomeada, acesso mínimo, processo de aprovação de sessões (Capítulo 6).
4. **Operar** — sessões aprovadas, registradas e revistas; revisões periódicas de acesso.
5. **Mudar** — novos funcionários, novos sistemas, fusões: nova revisão.
6. **Encerrar** — contas removidas, dados devolvidos ou destruídos, confirmação registrada.

A maioria dos problemas reais fica nas junções: um contrato que terminou, mas cuja conta sobreviveu; um engenheiro que saiu do fornecedor, mas cuja senha não saiu.

### 8.3 A revisão de acesso

Uma **revisão de acesso** periódica concilia três fontes: a lista de contas (o que existe), o registro de contratos (o que deveria existir) e os registros de sessão (o que é usado). Constatações típicas e respostas proporcionais:

| Constatação | Por que importa | Resposta proporcional |
|---|---|---|
| Conta de contrato encerrado | Ninguém responde pelo seu uso | Desabilitar agora; confirmar com o fornecedor |
| Sem uso há mais de 90 dias | Exposição desnecessária | Desabilitar; reabilitar a pedido, pelo processo |
| Conta compartilhada ou sem nome | As ações não podem ser atribuídas | Substituir por contas nomeadas; enquanto isso, restringir |
| Sem MFA | Só a senha concede o acesso | Corrigir ou registrar uma exceção com prazo |
| Uso muito acima do esperado | Pode ser um projeto legítimo, mau uso ou comprometimento | Perguntar ao fornecedor e ao dono interno; revisar os registros de sessão antes de concluir |

A última linha exige cuidado. Volume incomum é uma **pergunta**, não uma acusação.

### 8.4 Caso resolvido: a revisão de maio (sintético)

Depois das lacunas de controle do Capítulo 7, a coordenadora conduz a primeira revisão de acesso de fornecedores em 4 de maio de 2026, sob uma autorização de A. Mensah que permite a exportação somente leitura da lista de contas e do log de sessões do gateway. O **Laboratório 8** reproduz a conciliação.

**Laboratório 8** (salve como `lab08.py` e execute com `python3 lab08.py`):

```python
# Lab 8 - third-party remote-access review (offline, standard library only; all data synthetic)
import datetime as dt
TODAY = dt.date(2026, 5, 4)
# account, supplier, named person, MFA, contract end, last session, sessions in 90 days
ACCOUNTS = [
    ("v-hydro1",  "HydroLogic Ltd",  "P. Novak",  True,  "2027-03-31", "2026-04-28", 6),
    ("v-hydro2",  "HydroLogic Ltd",  "",          True,  "2027-03-31", "2026-04-30", 11),
    ("v-scadaco", "ScadaCo",         "M. Ilic",   False, "2026-12-31", "2026-03-15", 2),
    ("v-pumps",   "Vale Pumps",      "D. Ruiz",   True,  "2025-11-30", "2026-02-10", 1),
    ("v-meter",   "MeterWorks",      "K. Sato",   True,  "2026-09-30", "2025-10-02", 0),
    ("v-integr",  "Northgate Integration", "S. Brandt", True, "2026-08-31", "2026-05-01", 19),
]
SESSIONS_EXPECTED = {"HydroLogic Ltd": 8, "ScadaCo": 4, "Vale Pumps": 2, "MeterWorks": 2, "Northgate Integration": 4}
for acct, sup, person, mfa, end, last, n90 in ACCOUNTS:
    f = []
    if not person: f.append("shared/unnamed account")
    if not mfa: f.append("no MFA")
    if dt.date.fromisoformat(end) < TODAY: f.append("contract ended - disable")
    if (TODAY - dt.date.fromisoformat(last)).days > 90: f.append("unused >90 days - disable")
    if n90 > 2 * SESSIONS_EXPECTED[sup]: f.append(f"{n90} sessions vs ~{SESSIONS_EXPECTED[sup]} expected - ask why")
    print(f"{acct:10s} {sup:22s} {'OK' if not f else '; '.join(f)}")
```

Saída esperada (Python 3.13.5):

```text
v-hydro1   HydroLogic Ltd         OK
v-hydro2   HydroLogic Ltd         shared/unnamed account
v-scadaco  ScadaCo                no MFA
v-pumps    Vale Pumps             contract ended - disable
v-meter    MeterWorks             unused >90 days - disable
v-integr   Northgate Integration  19 sessions vs ~4 expected - ask why
```

A análise da coordenadora, rotulada:

- **Decidido (por A. Mensah, 4 de maio):** desabilitar hoje `v-pumps` (o contrato da Vale Pumps terminou em novembro) e `v-meter` (sem uso desde outubro); substituir `v-hydro2` por uma conta nomeada em até 14 dias e, enquanto isso, restringi-la a sessões supervisionadas.
- **Devido:** a ScadaCo deve habilitar a MFA em `v-scadaco` em até 30 dias, ou uma exceção deve ser proposta com medidas compensatórias (Capítulo 7); dono: A. Mensah.
- **Em aberto:** `v-integr` — a Northgate Integration teve 19 sessões em 90 dias, contra cerca de 4 esperadas. A coordenadora **não** conclui que houve mau uso. Ela pergunta a J. Tan se algum projeto explica isso e pede ao gerente de conta da Northgate o registro de trabalho. J. Tan responde que a Northgate está comissionando o novo enlace de telemetria da KW-11, aprovado em março; o registro de trabalho coincide com 17 das 19 sessões. Duas sessões, em 12 e 19 de abril às 02:00, não estão no registro de trabalho. Essas duas são passadas ao líder de segurança e ao KVROC para revisão dos registros de sessão, pelo caminho de escalonamento de incidentes, e o fornecedor só é informado depois que o líder de segurança concordar.
- **Pressuposto:** a exportação do gateway está completa. (Próxima revisão: comparar também com as origens permitidas no firewall.)

O caso mostra a disciplina do coordenador: agir depressa sobre falhas claras de governança, perguntar antes de acusar, escalar a atividade residual não explicada pelo caminho adequado e registrar o que é pressuposto.

### 8.5 Requisitos de contrato e de integração

A partir do caso, a coordenadora redige cláusulas-padrão para novos contratos de fornecedores com acesso remoto: apenas pessoas nomeadas; MFA; sessões apenas pelo gateway da empresa, aprovadas por sessão ou por janela programada; o fornecedor deve notificar a empresa em até 24 horas sobre o desligamento de funcionários e prontamente sobre qualquer incidente de segurança que possa afetar a empresa; registros de trabalho disponíveis a pedido; cooperação na resposta a incidentes; exclusão dos dados da empresa ao fim do contrato, confirmada por escrito. A ISA/IEC 62443 inclui requisitos para prestadores de serviços e integradores que podem embasar essas cláusulas ([visão geral da ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). A redação jurídica cabe à sua equipe jurídica; o seu trabalho é especificar o resultado de segurança.

### 8.6 Apresentação supervisionada

Apresente o caso ao seu supervisor (aqui, E. Varga) em cinco partes: o que foi revisto e sob qual autoridade; constatações com evidências; decisões já tomadas e por quem; decisões solicitadas ao supervisor (orçamento para a MFA do lado da ScadaCo, aprovação das cláusulas contratuais); e perguntas em aberto, com donos e datas.

Mantenha cada parte curta e rotulada, para que o supervisor possa interrompê-lo em qualquer ponto e ainda saber o que está decidido e o que está sendo pedido. Na revisão de maio, as duas sessões inexplicadas da Northgate pertencem às perguntas em aberto, com o seu dono, e não às constatações. Leve a saída do Laboratório 8 e a autorização como anexos, e declare com clareza o que foi pressuposto, como a completude da exportação do gateway. Termine repetindo as decisões solicitadas e a data até a qual são necessárias.

### 8.7 Erros comuns e limites

- Tratar uma atividade incomum como prova de comprometimento — ou ignorá-la como "provavelmente é o projeto".
- Remover um acesso necessário para suporte crítico à segurança sem uma alternativa.
- Revisões que usam uma única fonte (contas sem contratos ou sessões).
- Cláusulas contratuais que não podem ser verificadas.
- O laboratório modela um único gateway; ambientes reais têm vários caminhos de acesso (linha discada, modems celulares, ferramentas remotas instaladas pelo fornecedor) que a revisão precisa encontrar.

- Desabilitar a conta de um fornecedor cujo suporte é necessário para um problema de dosagem em andamento, sem providenciar uma alternativa.
- Encerrar uma revisão quando as constatações óbvias foram corrigidas, enquanto duas sessões inexplicadas continuam em aberto sem dono.

### Exercícios — capítulo 8

**EX036 — Leia o Laboratório 8.** *Objetivo:* interpretar os resultados da revisão. *Insumos:* a saída do Laboratório 8. *Passos:* para cada conta, declarar a constatação, o risco e a resposta proporcional, com dono. *Evidência esperada:* seis linhas. *Rubrica:* 3 = coincide com a seção 8.4, incluindo a contenção em relação a `v-integr` e uma alternativa para `v-scadaco`; 2 = ações corretas, mas acusatório quanto a `v-integr`; 1 = desabilita tudo; 0 = nada.

**EX037 — Estenda a revisão.** *Objetivo:* acrescentar uma fonte. *Insumos:* Laboratório 8. *Passos:* acrescentar uma data de "última confirmação de pessoal" por conta e sinalizar as contas cujo fornecedor não confirma a sua lista de pessoal há 180 dias; mostrar a saída. *Evidência esperada:* código e saída. *Rubrica:* 3 = campo acrescentado em todas as linhas, com valores de teste que disparam e que não disparam, saída mostrada, explica por que a confirmação de pessoal importa (desligamentos); 2 = sem explicação; 1 = apenas a regra; 0 = nada.

**EX038 — Redija cláusulas contratuais.** *Objetivo:* especificar as obrigações do fornecedor. *Insumos:* seção 8.5. *Passos:* escrever cinco cláusulas verificáveis em linguagem simples. *Evidência esperada:* cláusulas. *Rubrica:* 3 = cada cláusula tem uma obrigação mensurável e uma forma de verificação (por exemplo, aviso de desligamento de pessoal em até 24 horas, verificado na revisão trimestral); 2 = não verificáveis; 1 = "o fornecedor será seguro"; 0 = nada.

**EX039 — Trate as duas sessões noturnas.** *Objetivo:* escalar adequadamente uma atividade inexplicada. *Insumos:* seção 8.4. *Passos:* escrever a mensagem ao líder de segurança e a decisão de que você precisa. *Evidência esperada:* mensagem. *Rubrica:* 3 = fatos com horários em UTC e fonte, o que se sabe (17 de 19 explicadas), o que não se sabe, pedido de revisão dos registros de sessão pelo caminho de escalonamento, orientação para ainda não alertar o fornecedor, tratamento sensível (TLP:RED ou AMBER+STRICT), horário da próxima verificação; 2 = sem orientação de tratamento; 1 = "favor investigar a Northgate"; 0 = nada.

**EX040 — Apresente o caso.** *Objetivo:* apresentação supervisionada. *Insumos:* seção 8.6. *Passos:* escrever o briefing em cinco partes em menos de 300 palavras. *Evidência esperada:* briefing. *Rubrica:* 3 = as cinco partes, decisões solicitadas explicitamente, incerteza rotulada, nenhuma acusação sem fundamento; 2 = faltam as decisões solicitadas; 1 = apenas narrativa; 0 = nada.

### Síntese do capítulo

O acesso de fornecedores é governado ao longo de um ciclo de vida — selecionar, contratar, integrar, operar, mudar, encerrar —, e a maioria das falhas fica nas junções. Uma revisão de acesso concilia contas, contratos e sessões; responda de forma proporcional, trate as anomalias como perguntas e escale o que continuar inexplicado pelo caminho adequado. Transforme as lições em requisitos contratuais verificáveis e apresente os casos com as decisões solicitadas e a incerteza rotulada.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 12

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Comunicação, ética e relato

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- identificar todas as obrigações de notificação que um incidente pode disparar — legais, regulatórias, contratuais, de seguro — e controlar os seus prazos;
- escrever uma declaração provisória e um informe a um cliente crítico que sejam precisos, úteis e honestos quanto à incerteza;
- aplicar princípios éticos à comunicação: veracidade, proporcionalidade, justiça com as pessoas e correção de erros;
- relatar incidentes e a situação do programa à diretoria e ao conselho numa forma que apoie decisões.

Os Capítulos 1–8 construíram e exercitaram o programa internamente. Este capítulo se volta para fora.

### 9.1 Quem precisa ser informado, e quando

Um incidente num serviço essencial pode disparar vários relógios ao mesmo tempo. Pela NIS2, por exemplo, as entidades precisam enviar ao CSIRT nacional ou à autoridade competente um **alerta inicial em até 24 horas** depois de tomarem conhecimento de um incidente significativo, uma **notificação do incidente em até 72 horas** e um **relatório final em até um mês** após a notificação ([Directive (EU) 2022/2555, Article 23](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Outras jurisdições, setores e contratos fixam gatilhos e prazos diferentes; violações de dados pessoais podem acarretar obrigações separadas; as seguradoras costumam exigir aviso imediato. Um coordenador prepara de antemão um **registro de notificações**: cada obrigação, o seu gatilho, destinatário, prazo, conteúdo, dono e canal.

Dois detalhes decidem se você cumpre um prazo: **o que dispara o relógio** (detecção, conhecimento, determinação de que o incidente é "significativo") e **quem registra esse momento**. Combine os dois antes dos incidentes e registre o horário de início em UTC no log de decisões.

### 9.2 Clientes críticos

Hospitais, casas de repouso, pacientes de diálise, outras empresas de serviços públicos e serviços de emergência podem precisar agir antes do público. As suas necessidades são práticas: o que é afetado, o que devem fazer, por quanto tempo, quando vem a próxima atualização e para quem ligar. Os acordos com eles (Capítulo 2) muitas vezes prometem uma ligação num prazo curto. Mantenha os seus contatos testados e a mensagem livre de detalhes técnicos.

O acordo do Kestrel General Hospital promete uma ligação em até duas horas após qualquer evento que possa afetar o abastecimento ou a qualidade; os contatos são o plantão da infraestrutura predial e, fora do horário, o gerente de plantão do local.

### 9.3 Comunicação pública

Uma **declaração provisória** é uma mensagem curta e factual emitida cedo, antes que o quadro completo seja conhecido. Ela diz o que se sabe, o que a organização está fazendo, o que (se for o caso) o público deve fazer e quando virão mais informações. Ela não especula sobre causa ou autoria, não minimiza ("sem impacto") sem evidência e não revela detalhes úteis a um atacante. O líder de comunicação redige; o executivo aprovador aprova (Capítulo 6); as operações confirmam que qualquer afirmação de segurança ("a água é segura para beber") é verdadeira.

### 9.4 Ética

A comunicação sobre serviços essenciais tem o peso da segurança pública. Quatro princípios:

- **Veracidade** — nunca afirme como fato o que é pressuposto; nunca negue o que você sabe.
- **Proporcionalidade** — detalhe suficiente para que as pessoas se protejam, e não mais; evite causar alarme desnecessário e evite ajudar atacantes.
- **Justiça com as pessoas** — não nomeie nem culpe publicamente um funcionário ou fornecedor com base em informações incompletas; o erro humano costuma ser um problema do sistema.
- **Correção** — quando uma declaração se revelar errada, corrija-a pronta e visivelmente.

Internamente, uma cultura de relato **sem culpa** — as pessoas relatam erros e quase acidentes sem medo — dá ao coordenador os sinais precoces de que o relato externo depende.

### 9.5 Exemplo resolvido: os relógios de sábado (sintético)

No sábado, 13 de junho de 2026, às 21:40 UTC, o líder de incidente determina que um acesso não autorizado à rede de supervisão é um incidente significativo. As regras fictícias de Kestrel Vale espelham o padrão de 24 h / 72 h / um mês da NIS2; o acordo do hospital exige uma ligação em até 2 horas; a apólice de seguro exige aviso em até 48 horas. Na terça-feira à noite, a coordenadora confere o registro com o **Laboratório 9**.

**Laboratório 9** (salve como `lab09.py` e execute com `python3 lab09.py`):

```python
# Lab 9 - notification clocks after an incident (offline, standard library only; synthetic obligations)
# The deadlines are ILLUSTRATIVE for the fictional Kestrel Vale jurisdiction; real duties come from your own
# law, regulator and contracts. The 24 h / 72 h / one-month pattern mirrors EU NIS2 Article 23.
from datetime import datetime, timedelta, timezone
UTC = timezone.utc
aware = datetime(2026, 6, 13, 21, 40, tzinfo=UTC)        # incident judged significant (Saturday evening)
OBLIGATIONS = [  # name, hours after awareness, recipient
    ("Critical-customer call (contract)", 2,      "Kestrel General Hospital"),
    ("Regulator early warning",          24,     "Kestrel Vale CSIRT"),
    ("Insurer notice (policy)",          48,     "insurer"),
    ("Regulator incident notification",  72,     "Kestrel Vale CSIRT"),
    ("Regulator final report",           24*30,  "Kestrel Vale CSIRT"),   # 'one month' modelled as 30 days
]
SENT = {"Critical-customer call (contract)": datetime(2026, 6, 13, 23, 55, tzinfo=UTC),
        "Regulator early warning": datetime(2026, 6, 14, 18, 5, tzinfo=UTC),
        "Regulator incident notification": datetime(2026, 6, 16, 22, 30, tzinfo=UTC)}
NOW = datetime(2026, 6, 16, 23, 0, tzinfo=UTC)
for name, h, who in OBLIGATIONS:
    due = aware + timedelta(hours=h)
    sent = SENT.get(name)
    if sent:
        delta = (sent - due).total_seconds() / 3600
        state = f"sent {sent:%a %d %H:%M}Z, {'LATE by' if delta > 0 else 'early by'} {abs(delta):.2f} h"
    else:
        state = "OVERDUE - not sent" if NOW > due else f"open, {(due - NOW).total_seconds()/3600:.1f} h left"
    print(f"{name:35s} due {due:%a %d %b %H:%M}Z  {state}")
```

Saída esperada (Python 3.13.5):

```text
Critical-customer call (contract)   due Sat 13 Jun 23:40Z  sent Sat 13 23:55Z, LATE by 0.25 h
Regulator early warning             due Sun 14 Jun 21:40Z  sent Sun 14 18:05Z, early by 3.58 h
Insurer notice (policy)             due Mon 15 Jun 21:40Z  OVERDUE - not sent
Regulator incident notification     due Tue 16 Jun 21:40Z  sent Tue 16 22:30Z, LATE by 0.83 h
Regulator final report              due Mon 13 Jul 21:40Z  open, 646.7 h left
```

Surgem três problemas. A ligação ao hospital atrasou 15 minutos: a coordenadora estava ao telefone com o oficial de plantão do regulador, e o líder de comunicação achava que ela ligaria para o hospital — o defeito dos dois responsáveis do Capítulo 6 na vida real. A seguradora nunca foi notificada: ninguém tinha a apólice no registro de notificações. A notificação de 72 horas ao regulador atrasou 50 minutos porque a aprovação do diretor-presidente foi pedida às 21:00 para um prazo às 21:40. O alerta inicial, preparado a partir de um modelo, saiu antes do prazo.

A coordenadora registra esses fatos no log de decisões, sem culpa, notifica imediatamente a seguradora com uma explicação e acrescenta duas ações para a revisão: incluir a obrigação do seguro no registro, com um dono, e fixar prazos internos para as aprovações (por exemplo, "aprovação pedida no máximo 6 horas antes do prazo externo"). O laboratório calcula os relógios; ele não decide o que conta como "tomar conhecimento" — isso continua sendo um julgamento documentado.

### 9.6 Relatos à diretoria e ao conselho

Um relatório curto de incidente para a diretoria cobre: o que aconteceu (fatos, com grau de confiança rotulado); impacto no serviço e nas pessoas; o que foi feito e decidido; obrigações cumpridas e perdidas; riscos atuais; decisões necessárias. Os relatórios do programa (mensais ou trimestrais) usam as métricas que conduzem decisões do Capítulo 5 e os principais riscos classificados por consequência do Capítulo 4.

Para o incidente de sábado, o relatório à diretoria mostraria que a ligação ao hospital atrasou quinze minutos, que a seguradora não foi avisada e que a notificação de 72 horas atrasou, com as causas encontradas e não nomes. Ele terminaria com as duas ações para o registro e os prazos de aprovação, pedindo à diretoria que confirme ambas. Mantenha-o em uma página e anexe os cálculos dos relógios, para que um leitor possa conferir cada horário sem confiar no resumo.

### 9.7 Atividade prática

Redija um registro de notificações para uma organização que você conheça, com pelo menos cinco obrigações. Para cada uma, escreva o que dispara o relógio e quem o registra. Marque qualquer obrigação cuja fonte você não verificou.

Inclua contratos e seguros, além da lei, já que o incidente de sábado mostrou que o prazo de aviso de uma seguradora pode ser perdido simplesmente porque ninguém o listou. Para cada obrigação, nomeie um dono, fixe um prazo interno de aprovação anterior ao externo e registre o documento-fonte com a sua cláusula. Verifique se duas obrigações são disparadas pelo mesmo momento; se forem, combine quem registra esse momento e em qual fuso horário. Revise o registro sempre que um contrato ou uma apólice for renovado.

### 9.8 Erros comuns e limites

- Obrigações de notificação descobertas durante o incidente.
- Nenhum prazo interno para as aprovações, de modo que o prazo externo é perdido.
- Declarações provisórias que prometem "sem impacto" antes de haver evidência.
- Nomear pessoas ou fornecedores prematuramente.
- As obrigações legais reais variam; confirme as suas com a assessoria jurídica e com o seu regulador. Os relógios deste livro são ilustrativos.

- Deixar uma ligação, como o informe ao hospital, a cargo de duas pessoas que pressupõem, cada uma, que a outra vai fazê-la.
- Iniciar cada relógio a partir de um momento diferente porque ninguém combinou o que conta como tomar conhecimento.
- Esquecer as obrigações contratuais e de seguro porque o registro só lista reguladores.

### Exercícios — capítulo 9

**EX041 — Leia o Laboratório 9.** *Objetivo:* interpretar os relógios de notificação. *Insumos:* a saída do Laboratório 9. *Passos:* para cada obrigação, declarar a situação e a causa raiz de qualquer perda de prazo, usando a seção 9.5. *Evidência esperada:* cinco linhas. *Rubrica:* 3 = hospital atrasado 0,25 h (responsabilidade pouco clara), alerta inicial cumprido, seguradora em atraso (fora do registro), notificação atrasada 0,83 h (aprovação tardia), relatório final em aberto, com 646,7 h; as causas raiz são de processo, não de pessoas; 2 = apenas as situações; 1 = parcial; 0 = nada.

**EX042 — Escreva uma declaração provisória.** *Objetivo:* comunicar cedo e com honestidade. *Insumos:* a empresa está investigando um acesso não autorizado a sistemas que monitoram o tratamento da água; a equipe de operações está operando duas estações manualmente; os testes de qualidade da água estão normais. *Passos:* escrever uma declaração com menos de 120 palavras. *Evidência esperada:* declaração. *Rubrica:* 3 = apenas fatos, o que está sendo feito, o que os clientes devem fazer (nada, salvo orientação; como virão as atualizações), horário da próxima atualização, nenhuma especulação nem detalhe útil a um atacante, afirmação de segurança só conforme confirmada pelas operações; 2 = pequena especulação; 1 = "sem impacto, tudo bem"; 0 = nada.

**EX043 — Informe o hospital.** *Objetivo:* comunicação com um cliente crítico. *Insumos:* o mesmo incidente; a pressão na zona leste pode cair por até 4 horas amanhã, durante uma comutação controlada. *Passos:* escrever o roteiro da ligação. *Evidência esperada:* roteiro. *Rubrica:* 3 = efeito nos termos do hospital, horários, segurança da água, o que o hospital pode precisar fazer (água armazenada, prioridades), próxima atualização, contato 24 h; pergunta do que o hospital precisa; 2 = nenhuma pergunta ao hospital; 1 = detalhe técnico; 0 = nada.

**EX044 — Dilema ético.** *Objetivo:* aplicar os princípios. *Insumos:* um jornalista pergunta se o engenheiro de um fornecedor causou o incidente; evidências internas sugerem o envolvimento de um notebook roubado do fornecedor, não confirmado. *Passos:* escrever a resposta e justificá-la. *Evidência esperada:* resposta e raciocínio. *Rubrica:* 3 = recusa-se a atribuir ou nomear com base em informação não confirmada, explica que a investigação está em andamento, compromete-se a atualizar, o raciocínio cita veracidade e justiça; 2 = resposta correta sem raciocínio; 1 = nomeia o fornecedor; 0 = nada.

**EX045 — Conserte o processo de aprovação.** *Objetivo:* evitar notificações atrasadas. *Insumos:* seção 9.5. *Passos:* desenhar prazos internos e delegação para os três relógios externos. *Evidência esperada:* desenho. *Rubrica:* 3 = prazos internos antes de cada prazo externo, aprovadores substitutos nomeados para quando o diretor-presidente não estiver disponível, modelos preparados, início do relógio registrado em UTC pelo líder de incidente, seguradora incluída no registro; 2 = apenas os prazos; 1 = "ser mais rápido"; 0 = nada.

### Síntese do capítulo

Os incidentes disparam vários relógios ao mesmo tempo; conheça-os de antemão, combine o que dispara cada um e quem o registra, e fixe prazos internos de aprovação anteriores aos externos. Clientes críticos precisam de mensagens práticas e cedo; o público precisa de declarações provisórias verdadeiras e proporcionais. Comunique sem culpa nem especulação, corrija os erros visivelmente e relate à diretoria com fatos, impacto, decisões e obrigações.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 12

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Infraestrutura crítica e segurança setorial: qualidade e resolução de problemas

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- reconhecer os padrões comuns de falha dos programas de coordenação de segurança;
- resolver uma falha de coordenação com método — sintoma, hipóteses, evidências, causa, correção — em vez de culpar pessoas;
- medir a qualidade das decisões num exercício ou incidente, e não apenas a sua rapidez;
- conduzir um processo de ações corretivas que de fato encerre as ações.

O Capítulo 9 expôs falhas reais de coordenação. Este capítulo trata o próprio programa como um sistema que pode ser diagnosticado e melhorado.

### 10.1 Como os programas falham

A maioria das falhas de coordenação cai em poucos padrões:

- **Lacunas de titularidade** — atividades ou riscos sem uma pessoa que responda por eles (Capítulos 4 e 6).
- **Responsabilidade duplicada** — duas pessoas acham, cada uma, que a outra agiu.
- **Informação desatualizada** — contatos, mapas de dependências, listas de fornecedores ou registros que estavam certos no ano passado.
- **Controles de papel** — documentados, mas nunca observados nem testados (Capítulo 7).
- **Gargalos** — uma única pessoa em todos os caminhos críticos.
- **Deterioração das ações** — lições identificadas depois de cada exercício e nunca implementadas.
- **Rapidez sem qualidade** — decisões tomadas a tempo, mas sem justificativa, com informações erradas ou sem as pessoas certas.

### 10.2 Resolvendo uma falha de coordenação

Use a mesma disciplina que os engenheiros usam para falhas técnicas:

1. **Declare o sintoma** com precisão ("o hospital recebeu a ligação 15 minutos depois das 2 horas contratuais").
2. **Liste as hipóteses** ("ninguém era dono da ligação"; "o número de contato estava errado"; "o relógio de 2 horas começou em momentos diferentes para pessoas diferentes").
3. **Reúna evidências** — logs de decisão, registros de chamadas, entrevistas — sem culpa.
4. **Elimine** as hipóteses que as evidências contradizem.
5. **Corrija a causa**, e não o sintoma, e decida como você vai verificar a correção.

Um hábito útil: pergunte "o que fez disso a coisa razoável a fazer naquele momento?". As pessoas raramente agem com descuido numa crise; agem com as informações e os papéis que tinham.

### 10.3 Qualidade das decisões

A tempestividade é fácil de medir; a qualidade é mais difícil, porém mais importante. Para cada decisão-chave num exercício ou incidente, verifique: ela tinha um dono? Foi tomada dentro do tempo-alvo? A justificativa foi registrada? As pessoas que precisavam ser consultadas foram consultadas? Ela se baseou em informações verificadas, com os pressupostos rotulados? O guia do NIST para programas de teste, treinamento e exercícios descreve a avaliação de exercícios em relação aos objetivos e o registro das lições ([NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final)).

### 10.4 Exemplo resolvido: o log do exercício de mesa de maio (sintético)

No exercício de mesa DRY CREEK, de maio (o seu desenho é o exemplo resolvido do Capítulo 11), um avaliador manteve um log de decisões. O **Laboratório 10** o verifica.

**Laboratório 10** (salve como `lab10.py` e execute com `python3 lab10.py`):

```python
# Lab 10 - tabletop decision-log quality check (offline, standard library only; synthetic exercise log)
import csv, io
LOG = """minute,inject,decision,owner,target_min,taken_min,recorded_rationale
0,I1 HMI shows unexpected setpoint change,convene incident team,Coordinator,15,9,yes
20,I2 vendor reports stolen laptop,suspend vendor remote access,Ops manager,30,52,yes
35,I3 station KW-04 dosing alarm,switch KW-04 to manual,Ops manager,10,6,no
50,I4 journalist calls,holding statement,,30,41,yes
65,I5 hospital asks about water safety,brief hospital,Coordinator,20,,no
80,I6 regulator early-warning clock,send early warning,Coordinator,60,44,yes
"""
rows = list(csv.DictReader(io.StringIO(LOG)))
met = 0
for r in rows:
    f = []
    if not r["owner"]: f.append("no owner")
    if not r["taken_min"]: f.append("no decision taken")
    elif int(r["taken_min"]) > int(r["target_min"]): f.append(f"late {int(r['taken_min'])-int(r['target_min'])} min")
    else: met += 1
    if r["recorded_rationale"] != "yes": f.append("no rationale recorded")
    print(f"{r['inject'][:2]} {r['decision']:30s} {'ok' if not f else '; '.join(f)}")
print(f"decisions within target: {met}/{len(rows)}")
```

Saída esperada (Python 3.13.5):

```text
I1 convene incident team          ok
I2 suspend vendor remote access   late 22 min
I3 switch KW-04 to manual         no rationale recorded
I4 holding statement              no owner; late 11 min
I5 brief hospital                 no decision taken; no rationale recorded
I6 send early warning             ok
decisions within target: 3/6
```

A manchete "3/6 dentro do alvo" esconde mais do que mostra:

- A decisão do I3, de passar a KW-04 para o manual, foi rápida (6 minutos contra 10) e contada como no prazo, mas **nenhuma justificativa foi registrada**. Para uma decisão relacionada à segurança, isso importa: num incidente real, a revisão não saberia se ela foi tomada por causa dos dados de dosagem, por precaução ou por palpite.
- A declaração provisória do I4 **não tinha dono** — de novo o defeito de comunicação do Capítulo 6 — e atrasou.
- O I5, o informe ao hospital, **nunca foi decidido**. No hot wash, os participantes disseram que "acharam que a comunicação estava cuidando disso".
- O I2, a suspensão do acesso do fornecedor, atrasou 22 minutos. Os participantes explicaram que ninguém sabia se suspender o acesso da HydroLogic interromperia o suporte a um problema de dosagem então em andamento. Essa é uma causa de **informação ausente**, não de lentidão.

A tabela de resolução de problemas da coordenadora:

| Sintoma | Hipóteses | Evidências | Causa | Correção | Verificar por |
|---|---|---|---|---|---|
| Informe ao hospital do I5 não feito | Sem dono; contato desconhecido; esquecido sob carga | Hot wash: "acharam que a comunicação estava cuidando disso"; a RACI tinha dois R | Responsabilidade duplicada | Um único líder na RACI; ligação ao hospital na lista de verificação do incidente | Injeção sobre o hospital no próximo exercício |
| Suspensão do fornecedor do I2 atrasada | Aprovação pouco clara; impacto desconhecido | Os participantes perguntaram quem depende do acesso da HydroLogic | Informação de dependência ausente | Acrescentar "quem depende do acesso deste fornecedor" ao registro de fornecedores | A revisão do Laboratório 8 inclui a coluna de dependência |
| I3 sem justificativa | O modelo de log não tem o campo; pressão do tempo | O modelo não tem coluna de justificativa | Desenho da ferramenta | Acrescentar o campo de justificativa; papel de escriba | Nova execução do Laboratório 10 mostra a justificativa |

### 10.5 Encerrando ações corretivas

As lições não melhoram nada até se tornarem ações com donos, datas e verificação — e serem encerradas. Acompanhe-as num único lugar, revise-as no comitê de riscos e verifique cada encerramento com evidências (o próximo exercício, um teste, um documento). Uma métrica útil do programa é o percentual de ações de exercícios encerradas e verificadas dentro do prazo.

Na revisão do DRY CREEK, cada correção tem uma verificação correspondente: a próxima injeção do exercício sobre o hospital, um registro de fornecedores com coluna de dependência conferido na próxima revisão de acesso e uma nova execução do Laboratório 10 mostrando as justificativas registradas.

### 10.6 Atividade prática

Pegue uma falha recente de qualquer equipe que você conheça (um prazo perdido, uma tarefa duplicada). Preencha a tabela de resolução de problemas sem nomear pessoas e proponha uma correção com um método de verificação.

Escreva o sintoma como um fato preciso, com horários ou contagens, como no exemplo do hospital, e não como um julgamento. Liste pelo menos três hipóteses antes de procurar evidências e anote qual evidência descartou cada uma. Pergunte o que tornou a ação razoável para as pessoas envolvidas naquele momento. Depois escolha uma correção que mude um papel, uma ferramenta ou uma informação, e não uma que peça às pessoas que se esforcem mais, e diga como você saberá que ela funcionou, por exemplo no próximo exercício ou revisão.

### 10.7 Erros comuns e limites

- Relatar o sucesso de um exercício apenas pela rapidez.
- Concluir "erro humano" e parar por aí.
- Correções que são exortações ("comunicar melhor").
- Ações sem verificação, encerradas pela palavra do dono.
- Corrigir em excesso com processos pesados que atrasam as respostas reais; mantenha as correções proporcionais.

- Corrigir o sintoma, como lembrar a equipe de ligar para o hospital, enquanto a RACI ainda lista duas pessoas responsáveis.
- Contar uma decisão rápida como boa quando nenhuma justificativa foi registrada, como na passagem da KW-04 para o manual no DRY CREEK.
- Acompanhar as ações em vários lugares, de modo que ninguém consegue ver quais estão atrasadas.

### Exercícios — capítulo 10

**EX046 — Leia o Laboratório 10.** *Objetivo:* interpretar a qualidade das decisões. *Insumos:* a saída do Laboratório 10. *Passos:* explicar por que "3/6 dentro do alvo" superestima o desempenho e nomear o defeito mais grave. *Evidência esperada:* explicação. *Rubrica:* 3 = o I3 foi contado no prazo sem justificativa; o I5 nem foi tomado (risco para um cliente crítico); o I4 sem dono; o mais grave é o I5 ou o I3, com raciocínio; 2 = lista os defeitos sem julgamento; 1 = aceita 3/6; 0 = nada.

**EX047 — Acrescente uma regra de qualidade.** *Objetivo:* codificar outra verificação. *Insumos:* Laboratório 10. *Passos:* acrescentar as colunas `safety` e `consulted`; sinalizar qualquer decisão relacionada à segurança cujo dono não seja o gerente de operações e em que o gerente de operações não tenha sido consultado; testar com as seis linhas originais mais uma linha inventada em que o líder de segurança decide isolar uma estação sem consultar as operações; mostrar a saída. *Evidência esperada:* código e saída. *Rubrica:* 3 = colunas preenchidas em todas as linhas, regra restrita às decisões de segurança, a linha inventada sinalizada e o I3 (de dono das operações) não sinalizado, com esse resultado explicado; 2 = a regra sinaliza toda linha sem entrada de consultado; 1 = apenas a regra; 0 = nada.

**EX048 — Resolva o I4.** *Objetivo:* aplicar a seção 10.2. *Insumos:* a linha do I4 e a RACI do Capítulo 6. *Passos:* preencher a tabela de resolução de problemas para a declaração provisória. *Evidência esperada:* uma linha da tabela, com hipóteses. *Rubrica:* 3 = pelo menos duas hipóteses, evidência (a RACI não tinha A para a declaração pública), causa, correção (diretor-presidente A, comunicação R, modelo), verificação (próximo exercício); 2 = sem verificação; 1 = "a comunicação foi lenta"; 0 = nada.

**EX049 — Diagnostique a informação desatualizada.** *Objetivo:* reconhecer a deterioração. *Insumos:* num incidente, o número do hospital para fora do horário caiu numa linha desligada. *Passos:* propor uma análise de causa e uma correção duradoura. *Evidência esperada:* análise e correção. *Rubrica:* 3 = causa: nenhum dono nem calendário para a verificação dos contatos; correção: ligações de teste trimestrais com dono, atualização nas reorganizações do hospital, segunda via de contato; métrica de verificação; 2 = atualização pontual; 1 = culpa; 0 = nada.

**EX050 — Encerre as ações.** *Objetivo:* desenhar o acompanhamento das ações corretivas. *Insumos:* as três correções da seção 10.4. *Passos:* escrever um log de ações com dono, prazo, evidência de encerramento e método de verificação. *Evidência esperada:* log. *Rubrica:* 3 = cada uma tem um dono com autoridade, data realista, evidência de encerramento distinta da declaração do dono e verificação num exercício ou revisão posterior; 2 = sem verificação; 1 = apenas a lista; 0 = nada.

### Síntese do capítulo

Os programas de coordenação falham de maneiras reconhecíveis — lacunas de titularidade, responsabilidade duplicada, informação desatualizada, controles de papel, gargalos, deterioração das ações e rapidez sem qualidade. Resolva-as como falhas, do sintoma às hipóteses e evidências até a causa, sem culpa. Meça a qualidade das decisões, não só a rapidez, e encerre as ações corretivas apenas com evidências verificadas.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 12

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Laboratório supervisionado

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- desenhar um **exercício de mesa** baseado em discussão para um serviço essencial, com objetivos, cenário, injeções, papéis e critérios de avaliação;
- facilitá-lo de forma segura e justa, mantendo-o como um teste de planos e não de pessoas;
- avaliá-lo com um hot wash, um relatório pós-ação e um plano de melhoria;
- avaliar o desenho de um exercício segundo uma rubrica, sob supervisão.

Para um coordenador profissional, o laboratório é a sala do exercício. Este capítulo reúne tudo o que veio até aqui — partes interessadas, autorização, risco, RACI, acesso de fornecedores, relógios de notificação, qualidade das decisões — num único exercício supervisionado.

### 11.1 Tipos de exercício

Os programas de exercícios distinguem os exercícios **baseados em discussão** (seminários, oficinas, exercícios de mesa), em que os participantes conversam sobre um cenário, dos exercícios **baseados em operações** (simulados, exercícios funcionais, exercícios em escala real), em que eles executam ações. O Homeland Security Exercise and Evaluation Program (HSEEP), dos EUA, apresenta essa progressão e um ciclo de desenhar–conduzir–avaliar–melhorar ([FEMA, HSEEP](https://www.fema.gov/emergency-managers/national-preparedness/exercises/hseep)). O guia do NIST cobre programas de teste, treinamento e exercícios para planos de TI ([NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final)). A CISA publica pacotes prontos de exercícios de mesa para cenários de infraestrutura crítica ([CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages)), e o NCSC do Reino Unido oferece o "Exercise in a Box" ([NCSC, Exercise in a Box](https://www.ncsc.gov.uk/information/exercise-in-a-box)).

Um exercício de mesa é o primeiro passo certo: barato, seguro — nada toca um sistema em produção — e excelente para expor lacunas de papéis, informação e comunicação.

### 11.2 Desenho

Um documento de desenho tem sete partes:

1. **Objetivos** — de três a cinco, cada um **observável**: "Em até 30 minutos após a injeção pertinente, a equipe decide se suspende o acesso do fornecedor, com dono e justificativa registrados." Evite "testar a nossa resposta".
2. **Escopo e pressupostos** — quais planos são testados, quais equipes participam, o que está fora do escopo ("o processo técnico de perícia não é encenado").
3. **Cenário** — plausível, sintético, adequado ao setor, baseado em informações públicas sobre ameaças num nível geral; nunca no erro de um colega real.
4. **Injeções** — informações novas em momentos definidos (um alarme, uma ligação, um jornalista, um prazo do regulador). Cada injeção corresponde a pelo menos um objetivo e tem uma decisão esperada.
5. **Papéis** — participantes (decidem como decidiriam na realidade), facilitador (controla o relógio, apresenta as injeções, mantém a discussão andando), avaliadores (observam em relação aos objetivos, mantêm o log de decisões), escriba e um **oficial de segurança**, ou agente de confiança, que pode pausar o exercício.
6. **Critérios de avaliação** — o que significam "atendido", "parcialmente atendido" e "não atendido" para cada objetivo.
7. **Logística e regras** — data, sala, nenhum sistema real tocado, "exercício, exercício, exercício" em toda injeção escrita para que nada possa ser confundido com um evento real, e uma frase de parada para o mundo real.

### 11.3 Facilitação

Abra com as regras básicas: isto testa planos, não pessoas; não há perguntas capciosas; decidam como decidiriam na realidade; digam quando precisariam de informações que não têm. Mantenha o relógio honesto e resista a resgatar os participantes — se a equipe não tem como falar com o hospital, a lacuna é a constatação. Registre decisões, não opiniões sobre o desempenho.

No DRY CREEK, o facilitador não forneceu o contato que faltava do hospital nem atribuiu a ligação quando os participantes hesitaram; esse silêncio produziu a constatação mais clara do exercício.

### 11.4 Avaliação e melhoria

Logo depois: um **hot wash** — cada participante diz o que funcionou e o que não funcionou. Em até duas semanas: um **relatório pós-ação** (AAR) que classifica cada objetivo com evidências do log de decisões, e um **plano de melhoria** que transforma as constatações em ações com dono, data e verificáveis (Capítulo 10). O AAR é compartilhado no nível de TLP adequado; ele nomeia lacunas em planos e ferramentas, não pessoas.

O relatório do DRY CREEK classificou o O3 como não atendido e o transformou numa ação com dono, data e uma injeção de novo teste.

### 11.5 Exemplo resolvido: o exercício "DRY CREEK" (sintético)

**Objetivos.** (O1) Declarar ou descartar um incidente cibernético em até 15 minutos após o primeiro indicador, com justificativa. (O2) Decidir sobre a suspensão do acesso remoto de um fornecedor em até 30 minutos, sabendo quais operações dependem dele. (O3) Informar o hospital dentro do seu acordo de 2 horas, com um único líder nomeado. (O4) Cumprir o prazo ilustrativo do alerta inicial ao regulador com uma mensagem aprovada. (O5) Emitir uma declaração provisória com um aprovador definido em até 45 minutos após o contato da imprensa.

**Cenário.** Numa sexta-feira à noite, é comunicado o roubo do notebook de um engenheiro da HydroLogic; uma hora depois, o KVROC relata uma sessão remota à estação KW-04 a partir da conta da HydroLogic num horário incomum, e um operador vê uma mudança inesperada de setpoint de dosagem, que os limites do controlador rejeitam. Tudo sintético.

**Tabela de injeções (trecho).**

| Tempo | Injeção | Objetivos | Decisão esperada |
|---|---|---|---|
| 00:00 | Ligação do KVROC: sessão incomum de fornecedor na KW-04 | O1 | Convocar a equipe de incidente; registrar o horário de início |
| 00:10 | Operador: tentativa de mudança de setpoint, rejeitada pelos limites | O1 | Declarar o incidente; avaliação de segurança pelas operações |
| 00:20 | HydroLogic: notebook do engenheiro roubado ontem | O2 | Suspender o acesso da HydroLogic; providenciar suporte alternativo para a dosagem |
| 00:40 | A infraestrutura predial do hospital liga perguntando sobre boatos | O3 | O líder nomeado informa o hospital; próxima atualização marcada |
| 00:55 | Um jornalista local liga para a comunicação | O5 | Declaração provisória aprovada pelo diretor-presidente |
| 01:20 | Facilitador: "já se passaram 20 horas desde a determinação" | O4 | Alerta inicial aprovado e enviado |

**Papéis.** Participantes: E. Varga (diretoria), A. Mensah, L. Ferreira, R. Adeyemi, o engenheiro de plantão, e M. Holt, que entra às 00:55. Facilitador: a coordenadora. Avaliadores: um auditor interno e uma coordenadora par de uma empresa vizinha, sob acordo de confidencialidade. Oficial de segurança: supervisor de turno, com a frase de parada "mundo real, mundo real".

**Avaliação (a partir do log do avaliador, analisado com o método do Laboratório 10).** O1 atendido (9 minutos, justificativa registrada). O2 parcialmente atendido — decisão aos 52 minutos, porque ninguém sabia quem mais dependia do acesso da HydroLogic. O3 não atendido — a ligação ao hospital nunca foi atribuída. O4 atendido. O5 parcialmente atendido — declaração emitida com atraso, sem dono até a chegada do diretor-presidente. Essas constatações alimentaram diretamente as ações corretivas do Capítulo 10.

### 11.6 Rubrica de desenho de exercícios

| Critério | 3 (excelente) | 1 (fraco) |
|---|---|---|
| Objetivos | Observáveis, com prazo, ligados aos planos | "Testar a resposta" |
| Cenário | Plausível, sintético, específico do setor, proporcional | Hollywoodiano ou o erro de um colega real |
| Injeções | Cada uma ligada a objetivos, com decisões esperadas | Surpresas aleatórias |
| Papéis e segurança | Facilitador, avaliadores, oficial de segurança, frase de parada; nenhum sistema em produção | Os participantes avaliam a si mesmos; sistemas em produção tocados |
| Avaliação | Critérios definidos de antemão; log de decisões; AAR e plano de melhoria com donos | Balanço baseado em impressões |
| Ética | Testa planos, não pessoas; constatações anonimizadas | Pontua indivíduos |

Use a rubrica no desenho do DRY CREEK: os seus objetivos são observáveis e têm prazo, e cada injeção corresponde a um deles.

### 11.7 Atividade prática (supervisionada)

Desenhe um exercício de mesa de 90 minutos para um serviço essencial de sua escolha usando as sete partes da seção 11.2, com pelo menos quatro objetivos e seis injeções. Peça ao seu supervisor ou a um par que o pontue segundo a rubrica antes de conduzi-lo.

Baseie o cenário em informações públicas sobre ameaças num nível geral, como o DRY CREEK usou um notebook roubado de fornecedor e uma sessão remota incomum, e nunca no erro de um colega real. Ligue cada injeção a um objetivo, com uma decisão esperada, e nomeie um oficial de segurança com uma frase de parada. Marque toda injeção escrita como exercício. Depois da pontuação, revise o desenho e registre o que o revisor mudou, para que o supervisor veja como o retorno foi usado.

### 11.8 Erros comuns e limites

- Objetivos demais; nada é avaliado adequadamente.
- Cenários tão graves que todos os planos falham e nada específico é aprendido.
- Facilitadores que resgatam os participantes ou deixam as pessoas mais graduadas dominarem.
- Injeções do exercício que poderiam ser confundidas com mensagens reais.
- AARs que nunca viram ações.
- Um exercício de mesa mostra se os planos e os papéis fazem sentido; não mostra que os procedimentos podem ser executados com rapidez — isso exige simulados.

- Escolher avaliadores que também são participantes, de modo que ninguém observa as decisões de forma independente.
- Ignorar um comentário do hot wash como "achamos que a comunicação estava cuidando disso", que no DRY CREEK apontou a causa real.

### Exercícios — capítulo 11

**EX051 — Torne os objetivos observáveis.** *Objetivo:* escrever objetivos avaliáveis. *Insumos:* "Testar a nossa comunicação", "Verificar a gestão de fornecedores", "Ver se as pessoas conhecem o plano". *Passos:* reescrever cada um. *Evidência esperada:* três objetivos. *Rubrica:* 3 = cada um declara uma decisão ou ação, um prazo e o que é registrado; 2 = sem prazos; 1 = ainda vagos; 0 = nada.

**EX052 — Escreva injeções.** *Objetivo:* ligar as injeções aos objetivos. *Insumos:* os objetivos do DRY CREEK. *Passos:* escrever duas novas injeções que testem o O2 e o O4 com mais profundidade, com as decisões esperadas. *Evidência esperada:* duas linhas de injeção. *Rubrica:* 3 = plausíveis, sintéticas, cada uma ligada a um objetivo e com decisão esperada (por exemplo, a HydroLogic pede para se reconectar para consertar a dosagem; o oficial de plantão do regulador pede uma atualização antes do prazo); marcadas como "exercício"; 2 = não ligadas; 1 = irrealistas; 0 = nada.

**EX053 — Pontue um desenho.** *Objetivo:* aplicar a rubrica. *Insumos:* o desenho de um colega: um único objetivo, "testar a resposta a incidentes"; o cenário é um ataque de um Estado-nação que causa o rompimento de uma barragem; o diretor-presidente avalia; as injeções são enviadas da conta real de e-mail do diretor-presidente. *Passos:* pontuar cada critério e propor correções. *Evidência esperada:* pontuações e correções. *Rubrica:* 3 = notas baixas em objetivos, proporção do cenário, independência dos papéis/avaliação e segurança (o e-mail real arrisca confusão); correções para cada um; 2 = correções sem pontuações; 1 = aceita; 0 = nada.

**EX054 — Escreva o resumo do AAR.** *Objetivo:* avaliar em relação aos objetivos. *Insumos:* a avaliação do DRY CREEK na seção 11.5. *Passos:* escrever a tabela-resumo do AAR com classificação, evidência e ação recomendada por objetivo. *Evidência esperada:* cinco linhas. *Rubrica:* 3 = classificações coerentes com as evidências, ações com dono e verificáveis, nenhuma pessoa culpada; 2 = ações vagas; 1 = narrativa; 0 = nada.

**EX055 — Desafio de facilitação.** *Objetivo:* lidar com um problema de facilitação. *Insumos:* no exercício, o diretor-presidente domina e decide tudo, inclusive o isolamento técnico. *Passos:* descrever o que o facilitador faz durante e depois. *Evidência esperada:* ações. *Rubrica:* 3 = durante: convidar os donos dos papéis pelo nome, perguntar "quem decidiria isto na realidade?", registrar; depois: levantar no AAR como constatação de clareza de plano/papéis, conversar com o executivo em particular e com respeito; 2 = apenas depois; 1 = ignora; 0 = nada.

### Síntese do capítulo

Um exercício de mesa é o laboratório do coordenador: seguro, barato e poderoso para expor lacunas de papéis, informação e comunicação. Desenhe-o com objetivos observáveis, um cenário sintético plausível, injeções ligadas aos objetivos, avaliadores independentes e um oficial de segurança. Facilite para testar planos, não pessoas; avalie com um hot wash, um relatório pós-ação e um plano de melhoria cujas ações tenham dono e sejam verificadas.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 12

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Portfólio de prática e revisão final

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

- montar um portfólio profissional que mostre, com evidências, o que você consegue fazer como coordenador;
- apresentar ao conselho, em dez minutos, a segurança da infraestrutura crítica, com as decisões solicitadas;
- escrever um plano realista de 90 dias para um novo cargo de coordenação;
- avaliar o seu próprio trabalho em relação ao resultado do curso e identificar o que ainda precisa aprender.

Este capítulo encerra o curso: ele reúne os resultados dos Capítulos 1–11 e testa se você consegue **operar um fluxo de trabalho repetível e comunicar constatações**.

### 12.1 O portfólio

O portfólio de um coordenador não é um certificado; é um conjunto de produtos de trabalho que outra pessoa poderia verificar. Monte-o a partir dos exercícios que você concluiu, sanitizados e claramente marcados como trabalho do curso sobre dados sintéticos:

| Artefato | Do capítulo | O que mostra |
|---|---|---|
| Mapa de dependências e de partes interessadas | 2 | Você consegue ver o serviço e as suas pessoas |
| Autorização e registro de decisão | 3 | Você torna o trabalho e as decisões responsabilizáveis |
| Trecho do registro de riscos com a regra de classificação | 4 | Você consegue classificar pela consequência e manter a higiene |
| Conjunto de métricas com limiares | 5 | Você mede o que conduz decisões |
| RACI corrigida e cartão de escalonamento | 6 | Você torna os papéis inequívocos |
| Cartões de controle e plano de verificação | 7 | Você sabe a diferença entre declarado e testado |
| Briefing do caso de acesso de fornecedores | 8 | Você consegue analisar e apresentar um caso com justiça |
| Registro de notificações e declaração provisória | 9 | Você consegue se voltar para fora com honestidade e no prazo |
| Tabela de resolução de problemas e log de ações | 10 | Você melhora o programa, e não apenas relata sobre ele |
| Desenho do exercício de mesa, AAR e plano de melhoria | 11 | Você consegue testar o sistema inteiro com segurança |

Acrescente uma **reflexão** de uma página: o que você faria diferente e uma área sobre a qual precisa aprender mais (por exemplo, os fundamentos técnicos de TO do curso técnico, ou as obrigações legais da sua jurisdição).

### 12.2 A apresentação ao conselho

Os conselhos dos operadores de serviços essenciais carregam cada vez mais uma responsabilidade explícita pela gestão de riscos de cibersegurança (por exemplo, os requisitos da NIS2 para os órgãos de gestão, [Directive (EU) 2022/2555, Article 20](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Uma apresentação de dez minutos tem cinco partes:

1. **Contexto** — o serviço, a consequência que importa e o quadro de ameaças no nível dos alertas públicos.
2. **Onde estamos** — os principais riscos classificados por consequência, com donos e datas; os níveis de garantia dos controles-chave.
3. **O que aprendemos** — o último exercício ou incidente, em duas ou três constatações.
4. **O que estamos fazendo** — o plano, com o progresso em relação a ele.
5. **O que precisamos de vocês** — decisões: aceitações de risco, orçamento, declarações de apetite, prioridades.

Evite jargão, notas únicas e medo. Os conselhos agem a partir de consequências claras, planos críveis e pedidos específicos.

### 12.3 O plano de 90 dias

Os primeiros 90 dias de um novo coordenador, destilados deste livro:

- **Dias 1–30: ouvir e mapear.** Conhecer todas as partes interessadas que "decidem" e que "precisam ser informadas"; esboçar o mapa de dependências; ler o registro de riscos, o histórico de incidentes e a lista de fornecedores; registrar o que é pressuposto.
- **Dias 31–60: resolver a titularidade.** Donos para todo risco de nível 5; uma RACI para incidentes; um cartão de escalonamento; um registro de notificações; uma primeira revisão de acesso de fornecedores.
- **Dias 61–90: testar e relatar.** Um primeiro exercício de mesa sobre o cenário de alta consequência mais provável; um AAR e um plano de melhoria; uma primeira apresentação ao conselho com as decisões solicitadas.

Resista à tentação de começar com um novo framework, uma nova ferramenta ou uma política longa. Titularidade, informação e ensaio primeiro.

### 12.4 Exemplo resolvido: a apresentação ao conselho de outubro (sintético)

A apresentação de dez minutos da coordenadora ao comitê de auditoria e riscos da Kestrel Water, presidido por T. Lindqvist, em resumo:

1. *Contexto.* "O nosso trabalho é água segura para 180.000 pessoas, incluindo o Kestrel General Hospital. Alertas públicos descrevem ataques a controladores de água expostos à internet ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)); verificamos e não temos nenhum exposto, o que foi confirmado em setembro."
2. *Onde estamos.* "Três riscos poderiam afetar a saúde ou o hospital; todos agora têm donos. A MFA de fornecedores está implementada para cinco de seis fornecedores e verificada por teste para dois; a restauração do historiador foi testada em agosto, em 19 horas, contra um objetivo de 24 horas."
3. *O que aprendemos.* "O exercício DRY CREEK mostrou que não sabíamos quem liga para o hospital e que suspender um fornecedor é lento quando não sabemos quem depende dele. As duas coisas foram corrigidas; vamos testar de novo em janeiro."
4. *O que estamos fazendo.* "Cinco de sete ações do exercício encerradas e verificadas; duas vencem em novembro."
5. *O que precisamos.* "Primeiro, aceitar a exceção do controlador da KW-10 até março, com medidas compensatórias. Segundo, aprovar as cláusulas contratuais de fornecedores para todas as renovações. Terceiro, definir uma declaração de apetite: nenhum risco de nível 5 sem tratamento financiado por mais de 12 meses."

Cada número tem uma fonte no portfólio. Nada é uma nota única.

### 12.5 Revisão final

O resultado do curso pede que você opere um fluxo de trabalho repetível e comunique constatações. Confira-se em relação ao ciclo:

- **Enquadrar e identificar** — você consegue descrever um serviço pela consequência e encontrar riscos na conversa?
- **Analisar e decidir** — você consegue escrever riscos assumíveis, classificá-los de forma reproduzível e registrar decisões e aceitações?
- **Organizar** — você consegue atribuir papéis, governar mudanças e escalar?
- **Verificar** — você consegue distinguir declarado de testado e desenhar verificações proporcionais?
- **Comunicar** — você consegue cumprir prazos e informar clientes, o público e o conselho com honestidade?
- **Melhorar** — você consegue testar com um exercício e encerrar ações com evidências?

Onde a resposta for "ainda não", o número do capítulo diz para onde voltar.

### 12.6 Atividade prática

Monte o seu portfólio a partir das suas respostas aos exercícios. Peça a um par que o revise segundo a rubrica final (EX060) e que tente verificar três afirmações apenas a partir das suas evidências.

Escolha afirmações que importem, como "MFA de fornecedores verificada por teste para dois fornecedores" ou "historiador restaurado em 19 horas", e veja se o seu par consegue encontrar, só pelo portfólio, o registro, a data e o dono por trás de cada uma. Onde não conseguir, corrija a evidência, e não a redação. Marque claramente cada item como trabalho do curso sobre dados sintéticos e remova qualquer coisa que possa identificar uma organização ou pessoa real antes de compartilhá-lo.

### 12.7 Erros comuns e limites

- Portfólios de certificados em vez de produtos de trabalho.
- Apresentações ao conselho sem pedidos.
- Planos de 90 dias que começam por ferramentas.
- Apresentar trabalho sintético do curso como constatações organizacionais reais.
- Este curso não faz de você um especialista técnico em TO nem um advogado; saiba quando chamar um.

- Relatar uma afirmação ao conselho sem fonte no portfólio, de modo que ninguém consegue conferi-la depois.
- Pedir uma decisão ao conselho sem dizer o que acontece se ele a recusar, por exemplo por quanto tempo a exceção da KW-10 continuaria de outra forma.
- Atualizar o portfólio uma vez e deixá-lo envelhecer depois do fim do curso.

### Exercícios — capítulo 12

**EX056 — Índice do portfólio.** *Objetivo:* reunir evidências. *Insumos:* as suas respostas aos exercícios. *Passos:* produzir o índice do portfólio com o artefato, o capítulo e a afirmação que cada um sustenta. *Evidência esperada:* índice com pelo menos oito artefatos. *Rubrica:* 3 = cada artefato ligado a uma afirmação e a um exercício específicos, sanitizado e rotulado como sintético; 2 = índice sem afirmações; 1 = lista de capítulos; 0 = nada.

**EX057 — Apresentação ao conselho.** *Objetivo:* comunicar à governança. *Insumos:* a seção 12.2 e o seu portfólio. *Passos:* escrever o roteiro da apresentação (no máximo 600 palavras). *Evidência esperada:* roteiro. *Rubrica:* 3 = cinco partes, consequências em linguagem simples, números com fonte, níveis de garantia declarados, três pedidos específicos; nenhuma nota única; 2 = sem pedidos; 1 = relatório técnico; 0 = nada.

**EX058 — Plano de 90 dias.** *Objetivo:* planejar um cargo. *Insumos:* um novo cargo de coordenador numa rede hospitalar regional. *Passos:* escrever o plano de 90 dias com três fases e entregas. *Evidência esperada:* plano. *Rubrica:* 3 = adapta-se à saúde (liderança clínica como tomadora de decisões, dispositivos médicos, segurança do paciente, dependências internas críticas), titularidade antes das ferramentas, exercício e relatório ao conselho até o dia 90; 2 = genérico; 1 = começa pelas ferramentas; 0 = nada.

**EX059 — Verifique uma afirmação.** *Objetivo:* testar as evidências. *Insumos:* a afirmação "a restauração do historiador foi testada em agosto, em 19 horas". *Passos:* listar as evidências que você esperaria encontrar no portfólio para sustentá-la e duas perguntas que um auditor cético faria. *Evidência esperada:* lista e perguntas. *Rubrica:* 3 = plano de teste, autorização, log cronometrado, registro do resultado, verificação da completude dos dados; perguntas sobre o escopo (restauração completa ou parcial) e o ambiente (isolado ou semelhante à produção); 2 = apenas as evidências; 1 = "confiar no engenheiro"; 0 = nada.

**EX060 — Autoavaliação.** *Objetivo:* refletir em relação ao resultado do curso. *Insumos:* seção 12.5. *Passos:* atribuir-se de 0 a 3 nas seis áreas do ciclo, com evidência para cada uma, e um plano de aprendizagem para as duas mais baixas. *Evidência esperada:* seis notas e um plano. *Rubrica:* 3 = notas honestas, cada uma sustentada por um artefato do portfólio, plano de aprendizagem específico, com recursos e datas; 2 = notas sem evidência; 1 = tudo 3; 0 = nada.

### Síntese do capítulo

Um coordenador profissional demonstra competência por meio de produtos de trabalho verificáveis: mapas, registros, cadastros, RACIs, cartões de controle, briefings de casos, registros de notificações, relatórios de exercícios e planos de melhoria. Apresente-se aos conselhos com consequências, evidências e pedidos específicos; comece um novo cargo pela titularidade, pela informação e pelo ensaio; e avalie-se com honestidade em relação ao ciclo completo — enquadrar, decidir, organizar, verificar, comunicar, melhorar.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 12

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Estas são respostas-modelo. Uma resposta diferente que atenda ao padrão de evidências e de honestidade sobre os limites exigido pela rubrica recebe a pontuação máxima. Todas as organizações, pessoas e dados são sintéticos.

### Capítulo 1

**EX001.** (1) "Como os computadores do escritório e da sala de controle compartilham uma rede e serviços de área de trabalho remota sem correções, um ransomware que entrasse por phishing poderia criptografar as estações de trabalho dos operadores na KW-TW, forçando a operação manual do tratamento por dias e pondo em risco o abastecimento de 180.000 pessoas." (2) "Como os PCs da sala de controle rodam um sistema operacional sem suporte, para o qual não saem correções, uma falha conhecida poderia ser usada para desativar as telas dos operadores, causando perda de visão da dosagem e da pressão até que as substituições sejam instaladas." (3) "Como a conta remota de um fornecedor de bombas não tem segundo fator, qualquer pessoa com a sua senha poderia entrar nos controladores das estações e alterar os setpoints das bombas, causando perda de pressão para até 20.000 clientes, incluindo o hospital." Cada uma nomeia causa, evento e consequência em pessoas ou tempo.

**EX002.** (c) primeiro: uma mudança não aprovada no cloro ameaça diretamente a saúde. (b) em segundo: 40 minutos sem visão significam que os operadores não conseguem ver nem corrigir o processo, e isso pode indicar interferência. (d) em terceiro: o diagrama ajuda um atacante a planejar e precisa ser recolhido e avaliado. (a) em quarto pela consequência operacional — mas pode acarretar deveres de notificação de dados pessoais com prazos curtos, de modo que pode ser o primeiro em **urgência de ação** para a equipe jurídica. Classificar pela consequência não significa ignorar obrigações.

**EX003.** À TI: "Obrigada — não posso aprovar isto sozinha, porque roda nas estações de trabalho dos operadores e pode afetar o sistema de controle. A decisão é de A. Mensah, como dono. Vocês poderiam perguntar ao fornecedor do sistema de controle se o produto é suportado e propor um teste numa máquina fora de produção, com um plano de reversão? Vou marcar 30 minutos com as Operações na próxima terça-feira." A A. Mensah: um resumo, o pedido e a data proposta. A pontuação máxima exige nenhuma aprovação exclusiva e um dono nomeado.

**EX004.** Antivírus: Proteger (segurança de plataforma) e Governar (quem decide sobre mudanças nos sistemas operacionais). Nota de risco: Governar (estratégia de gestão de riscos, supervisão). Acessos do fornecedor: Governar (gestão de riscos da cadeia de suprimentos), Identificar (ativos e risco), Proteger (identidade e acesso). Um rótulo mostra onde o tema se situa, não se algo funciona.

**EX005.** Risco: "Como a porta da estação fica escorada aberta à noite, uma pessoa não autorizada poderia entrar na KW-03 e adulterar o equipamento de controle, causando operação insegura ou perda de abastecimento." Dono: gerente de operações (ou gerente da estação). Pergunta: "Quão lento é o leitor, e a porta também é usada como saída de emergência ou para entregas à noite?" — a correção pode ser um leitor mais rápido, não uma advertência.

### Capítulo 2

**EX006.** Regulador: precisa ser informado; pode ajudar (orientações). KVROC: executa (monitoramento); pode ajudar; dependência compartilhada. HydroLogic: executa; dependência a montante; precisa ser informada sobre incidentes relevantes, por contrato. Escola: é afetada; possivelmente precisa ser informada se abriga pessoas vulneráveis (política local). Diretor-presidente: decide. Sala de controle da Kestrel Grid: dependência a montante; pode ajudar (prioridades de restabelecimento); precisa ser informada quando grandes mudanças de carga forem planejadas.

**EX007.** Operadora: perdê-la remove a telemetria das doze estações de uma vez — os operadores perdem a visão em toda parte; pergunta: existe um segundo caminho ou um plano de leitura manual? KVROC: uma interrupção ou um comprometimento afeta três empresas e reduz a detecção; pergunta: o que acontece com o monitoramento se o KVROC estiver indisponível, e quem mais depende dele? Engenheiro da HydroLogic: risco de pessoa-chave — uma doença ou saída deixa ninguém capaz de consertar as estações; pergunta: o conhecimento está documentado, e há um segundo engenheiro? A pergunta comum: "O que mais usa isso?"

**EX008.** "Kestrel Water para a Infraestrutura Predial do Hospital: a partir das 10:00 de hoje, por cerca de seis horas, estamos operando em controle manual, por precaução, a estação de bombeamento que atende o seu local. A água continua segura para beber. A pressão pode ficar um pouco mais baixa; não esperamos interrupção. Por favor, deixem pronto o seu plano de água armazenada, por garantia. Próxima atualização até as 12:00, ou antes se algo mudar. Contato: coordenador de plantão, [número 24 h]." (Menos de 80 palavras, sem detalhes técnicos.)

**EX009.** Pedir ao gerente de infraestrutura predial a seção pertinente do plano de continuidade do hospital ou uma reunião curta; registrar data e fonte; mudar a entrada de "pressuposto" para "verificado (fonte, data)". Se o número real for 2 horas, a promessa de ligar "em até 2 horas" não deixa tempo para agir: renegociar para uma notificação muito mais curta (por exemplo, 30 minutos), planejar um abastecimento alternativo com o hospital (caminhões-pipa, válvulas prioritárias) e abrir um risco de nível 5 para essa dependência.

**EX010.** Empresa de água: se o faturamento, a programação ou o monitoramento remoto forem criptografados, os gestores podem parar ou restringir a operação automatizada, por precaução contra a propagação e porque não conseguem ver nem cobrar o serviço; a operação pode continuar manualmente. Oleoduto: o alerta AA21-131A da CISA descreve o ransomware DarkSide visando a rede de TI de uma empresa de infraestrutura crítica e insta a medidas para evitar a interrupção dos negócios; as operações podem ser paralisadas quando os sistemas de negócio necessários para conduzi-las estão indisponíveis ou quando o operador opta pela cautela. A pontuação máxima evita afirmar que os sistemas de controle foram comprometidos e fica no nível do alerta.

### Capítulo 3

**EX011.** Ausentes: finalidade; sistemas exatos e exclusões; atividades permitidas e proibidas; testadores e supervisor nomeados; janela com fuso horário; condições de parada; tratamento de dados; autoridade por escrito (um chat não é registro; quem na Northgate assina em conjunto?). Reescrita: "Finalidade: avaliar a exposição da rede de supervisão a partir da rede de escritório. No escopo: o firewall entre as zonas de escritório e de supervisão, os dois servidores de supervisão da KW-TW. Fora do escopo: controladores das estações, sistema de dosagem, intertravamentos de segurança. Permitido: revisão de configuração, revisão passiva de tráfego a partir de uma porta espelhada aprovada; proibido: varredura ativa de controladores, exploração, qualquer escrita. Pessoas: S. Brandt (Northgate), supervisionado por J. Tan. Janela: 9 de junho de 2026, 09:00–15:00, horário local. Parada: qualquer alarme, perda de visão, pedido de um operador. Dados: relatório TLP:AMBER+STRICT por transferência segura; anotações de trabalho apagadas em até 14 dias. Autoridade: A. Mensah (assinado), gerente de serviços da Northgate (assinado em conjunto)."

**EX012.** Decisão: manter a KW-05 em automático. Por: gerente de plantão, segundo o procedimento de incidentes das operações, 02:10, horário local. Opções: (a) operação manual — convocação de 90 minutos, risco de erros de manuseio à noite; (b) permanecer em automático, com vigilância — escolhida. Sabido: um login remoto inexplicado às 01:52; valores de dosagem normais; limites ativos. Desconhecido: se o login era malicioso; se a conta foi mal usada em outro lugar. Condições: o operador vigia a dosagem e a pressão a cada 15 minutos; passa para o manual diante de qualquer mudança inesperada; rever às 06:00 com o líder de segurança. Informados: líder de segurança, líder de incidente, gerente de operações (mensagem às 02:15).

**EX013.** (a) TLP:GREEN — o setor se beneficia e a informação não é específica da empresa. (b) TLP:AMBER+STRICT (ou RED, se só analistas nomeados do KVROC precisarem dela) — revela as fraquezas da empresa. (c) TLP:CLEAR — destinado ao público.

**EX014.** Uma biblioteca de registros com controle de acesso, com pastas por tipo de registro: autorizações e registros de decisão (dono: coordenador); aceitações de risco e exceções (dono: coordenador; decisões por autoridades nomeadas, com links nas atas do conselho); relatórios de exercícios (dono: coordenador); listas de acesso de fornecedores (dono: gerente de operações; exportadas do gateway, nunca enviadas por e-mail). Histórico de versões ativado, retenção conforme a política, acesso revisto duas vezes por ano.

**EX015.** Parar se: qualquer alarme inesperado na KW-09 ou nas vizinhas; qualquer perda de visão nas telas dos operadores; a atualização passar das 15:00; o controlador não voltar ao estado esperado dentro do tempo planejado; o operador de turno pedir. O operador de turno e o gerente de operações podem parar o trabalho a qualquer momento, sem justificativa; o fornecedor precisa parar e deixar o sistema no estado seguro acordado.

### Capítulo 4

**EX016.** 5: ocorreu aqui nos últimos 12 meses, ou está sendo ativamente tentado contra operadores semelhantes agora (alerta público). 4: ocorreu no setor nos últimos 2 anos, com as condições presentes aqui. 3: ocorreu no setor; exigiria mais uma condição aqui. 2: conhecido em outros setores; exigiria várias condições. 1: nenhuma ocorrência conhecida; exigiria várias condições improváveis. As classificações levam em conta os controles que existem e estão verificados (Capítulo 7).

**EX017.** O R03 tem a segunda pontuação empatada (15), mas consequência 3 sobre o faturamento (peso de serviço 1), por isso cai para sexto pela regra da consequência primeiro. A pontuação do R05 é 10, mas a consequência 5 sobre a água potável o eleva para terceiro. Ações de governança: R02 — atribuir um dono (A. Mensah, que é dono da dosagem), definir nova data de tratamento, revisar agora; R04 — teste de restauração atrasado (J. Tan executa; A. Mensah como dono do serviço); R07 — revisão desatualizada (a coordenadora, como interlocutora com o hospital, ou L. Ferreira, como dono registrado, revisa com o hospital).

**EX018.** "Risco R10: Como os controladores da estação KW-10 estão sem suporte e não podem ser corrigidos, uma fraqueza conhecida poderia ser usada para parar o bombeamento, causando perda de abastecimento para cerca de 8.000 pessoas. Aceito por: diretor-presidente, M. Holt, em nome do conselho, 14 de outubro de 2026. Medidas compensatórias: nenhum acesso remoto à KW-10; monitoramento da rede da estação pelo KVROC; controle de acesso físico; controladores reserva mantidos; procedimento de operação manual treinado. Caduca se: um alerta público mostrar exploração ativa, ocorrer um incidente na KW-10 ou uma medida compensatória falhar. Validade: 31 de março de 2027. Responsável pela revisão: A. Mensah; o coordenador acompanha."

**EX019.** Acrescentar um oitavo campo `acceptance_expiry` (None onde não houver aceitação), por exemplo R05 "2026-02-28" (expirada) e R06 "2026-12-31" (válida). Regra: `if exp and dt.date.fromisoformat(exp) < TODAY: flags.append("ACCEPTANCE EXPIRED")`. A saída agora mostra o R05 com "ACCEPTANCE EXPIRED" e o R06 sem ela, e "Needs governance action" passa a ser R02, R04, R05, R07. A pontuação máxima mostra os dois casos.

**EX020.** Resumo: "A nossa regra de classificação coloca em primeiro lugar tudo o que possa afetar a saúde ou o hospital e depois usa a probabilidade. Principais riscos: (1) acesso remoto de fornecedores sem MFA — dono A. Mensah, correção até 30 de abril; (2) só um engenheiro entende a lógica de dosagem — atualmente sem dono; pedimos ao comitê que confirme A. Mensah como dono e financie a documentação e um segundo engenheiro até setembro; (3) perda de energia da rede na KW-07 — estudo de gerador de reserva previsto para setembro. Ações de governança: o teste de restauração do historiador está atrasado (agora marcado para abril) e a revisão do risco de abastecimento do hospital está desatualizada (reunião marcada para março). Limites: as classificações de probabilidade são julgamentos de especialistas; a classificação é reproduzível a partir da regra anexa." Nenhuma nota única.

### Capítulo 5

**EX021.** Requisitos regulatórios primeiro (são obrigatórios). Usar o CSF 2.0 como estrutura do programa e para os relatórios ao conselho, porque é baseado em resultados e inclui Governar. Usar os CPGs como linha de base priorizada, mapeada para as funções do CSF, para encontrar depressa as lacunas de alto impacto. Usar a ISA/IEC 62443 para as aquisições de TO e os requisitos de fornecedores (requisitos para prestadores de serviços e para produtos), referenciada a partir dos resultados de cadeia de suprimentos de Governar.

**EX022.** Escopo: os mesmos sistemas e locais da avaliação de 2,6? Avaliador e método: autoavaliação, par ou independente; entrevista ou evidências? Definição: o que significa o nível 3, e isso mudou? Data: antes ou depois da mudança no contrato do KVROC? Decisão: o que faremos de diferente por causa do 3,1? Crível se o escopo e o método forem os mesmos, baseada em evidências ou independente, e ligada a um resultado observado, como o KVROC detectar as injeções do exercício dentro do tempo-alvo.

**EX023.** (1) % dos riscos de nível 5 com dono e tratamento dentro do prazo — dono: coordenador; < 100% → escalonamento à diretoria. (2) Mediana de dias úteis entre o fim do contrato do fornecedor ou o desligamento de um funcionário e a remoção da conta — dono: gerente de operações; > 5 → revisão do processo de acesso. (3) Número de interfaces operacionais alcançáveis a partir da internet — dono: líder de segurança; > 0 → notificação imediata ao dono e correção. (4) % de gerentes de plantão num exercício nos últimos 12 meses — dono: coordenador; < 80% → agendar exercício.

**EX024.** "Obrigada — isto pode ser urgente. A qual local e função o hmi-02 serve? A conexão teve sucesso ou foi apenas tentada, e qual é a origem e a evidência (trecho de log com horários em UTC)? Ele ainda está alcançável agora? Bloquear pode cortar o acesso legítimo de um fornecedor — quem usa esse caminho? Estou ligando agora para A. Mensah, como dono; por favor, fiquem de prontidão para bloquear com a aprovação dele, e tratem isto pelo caminho de escalonamento de incidentes até sabermos mais."

**EX025.** "Avaliamos a TI do escritório e a estação de tratamento segundo uma linha de base nacional; a maioria das práticas existe no papel. As doze estações de bombeamento não foram incluídas, e duas práticas que mais importam para elas — autenticação forte para o acesso de fornecedores e remoção tempestiva de contas — não estão verificadas. Revisaremos o acesso de fornecedores em maio e reavaliaremos, incluindo as estações, até setembro."

### Capítulo 6

**EX026.** Acrescentar um sétimo papel, "Shift supervisor" (supervisor de turno), e corrigir as linhas (Coordinator, Ops manager, Security lead, Comms, Vendor, CEO, Shift supervisor): `Switch stations to manual` — `I A - - - I R`; `Brief hospital` — `R C I C - A -` (a coordenadora é a única líder, a comunicação é consultada sobre a redação); `Approve vendor remote session` — `C A R - I - I` (o gerente de operações é o único A, o líder de segurança verifica o pedido, o fornecedor é apenas informado); `Public statement` — `C C C R - A -`; as demais linhas ganham `I`, `C` ou `-` para o supervisor de turno. Executar de novo o Laboratório 6 com essas linhas imprime "0 issues in 7 activities" e a linha de carga `Coordinator=3, Ops manager=4, Security lead=2, Comms=1, Vendor=0, CEO=3, Shift supervisor=1`. O gerente de operações ainda acumula quatro entradas R/A, o que o EX029 trata.

**EX027.** (a) Normal: novo caminho de acesso relevante para a segurança; aprovação do dono, revisão da regra e validade. (b) Padrão, se existir um procedimento pré-aprovado para a troca de baterias; caso contrário, normal. (c) Emergencial: aprovada pelo líder de incidente, registrada em até 24 horas, revista depois. (d) Normal: verificação de compatibilidade com o fornecedor, teste, plano de reversão.

**EX028.** Cartão: "Suspeita de evento cibernético — ligue se: as telas mostrarem mudanças que ninguém fez; houver logins ou mensagens inesperados; os controles não responderem; o KVROC ligar. 1) Mantenha o processo seguro — siga os procedimentos operacionais normais; passe para o manual apenas como os procedimentos permitem. 2) Não desligue nem reinicie computadores, a menos que instruído. 3) Anote os horários e o que você viu. 4) Ligue para o líder de incidente de plantão [número]; sem resposta em 10 minutos → substituto [número]; depois, gerente de operações [número]. 5) Perigo imediato para pessoas ou para a qualidade da água → gerente de operações diretamente e procedimentos de emergência."

**EX029.** Manter as decisões de segurança (operação manual, isolamento que afete o processo) com o gerente de operações. Delegar a aprovação de sessões de fornecedores durante incidentes a um substituto nomeado das operações ou ao líder de incidente, com as operações consultadas; passar a interlocução com o hospital ao coordenador; garantir que um gerente de operações substituto esteja de plantão, para que a planta sempre tenha alguém focado nela.

**EX030.** Listar as mudanças emergenciais a partir do log do incidente; para cada uma, decidir manter, modificar ou reverter, com um dono: a regra de "bloquear todo acesso de fornecedores" passa a ser uma mudança normal — restabelecer o acesso fornecedor a fornecedor, pelo processo normal de aprovação, depois de concluída a revisão; remover a conta temporária de administrador local e verificar a remoção; atualizar diagramas e registros; registrar a revisão como um registro de decisão.

### Capítulo 7

**EX031.** Objetivo: impedir o uso de contas de fornecedores por pessoas que já não estão sob contrato (risco R01 e riscos de desligamento no fornecedor). Dono: gerente de operações (como dono do contrato e das estações). Operação: quando um contrato termina ou o fornecedor notifica o desligamento de um funcionário, a conta é desabilitada em até 5 dias úteis; todo mês, o coordenador concilia as contas do gateway com o registro de contratos. Evidência: registro de conciliação e exportação do gateway, guardados na biblioteca de registros. Sinal de falha: qualquer conta cujo contrato terminou ou cuja pessoa nomeada saiu.

**EX032.** MFA de fornecedores: testado (protege contra consequências de nível 5; login supervisionado só com senha recusado). Procedimento de operação manual: testado por simulados ou exercícios (é a alternativa de segurança). Política de senhas dos notebooks do escritório: observado (exportação de configuração) — consequência de nível 3. Crachás de visitante na sede: documentado ou observado — consequência menor para o serviço.

**EX033.** Restaurar o backup mais recente do historiador num ambiente isolado (não na produção), autorizado por A. Mensah, com J. Tan executando. Iniciar um cronômetro na decisão de restaurar; sucesso se o historiador estiver utilizável em até 24 horas e os dados de um período escolhido de 7 dias estiverem completos em comparação com uma referência conhecida. Registrar horários, passos, problemas e resultado num relatório de teste; arquivá-lo e atualizar o nível de garantia do controle C2 para "testado", com data.

**EX034.** "Exceção E-07: controle 'MFA para acesso de engenharia' não aplicado à interface local de engenharia da KW-10. Motivo: o firmware do controlador não o suporta; substituição planejada. Compensações: nenhum caminho remoto até a KW-10; armário trancado, com registro das chaves; checksums de configuração comparados semanalmente; o KVROC alerta sobre qualquer sessão de engenharia. Aceita por: diretor de operações E. Varga (consequência 4), 1º de outubro de 2026. Validade: 31 de março de 2027. Plano de eliminação: substituição do controlador no programa de investimentos de 2027; dono: A. Mensah."

**EX035.** C1, MFA de fornecedores: observada em 5 de 6 contas; lacuna da ScadaCo a corrigir até 3 de junho (A. Mensah). C2, restauração do historiador: backups observados todas as noites, mas restauração nunca testada; teste marcado em até 60 dias (J. Tan). C3, limites de dosagem: testados num controlador reserva em 3 de fevereiro, e a produção coincide por checksum; verificar de novo após qualquer mudança de lógica (J. Tan).

### Capítulo 8

**EX036.** `v-hydro1`: sem constatação; manter. `v-hydro2`: conta sem nome — ações não atribuíveis; substituir por conta nomeada em até 14 dias, com sessões supervisionadas enquanto isso (A. Mensah). `v-scadaco`: sem MFA — só a senha concede o acesso; a ScadaCo deve habilitá-la em até 30 dias ou haverá exceção com medidas compensatórias; manter uma alternativa supervisionada para suporte urgente (A. Mensah). `v-pumps`: contrato encerrado — desabilitar agora e confirmar com a Vale Pumps. `v-meter`: sem uso há > 90 dias — desabilitar; reabilitar a pedido. `v-integr`: 19 contra ~4 sessões — perguntar a J. Tan e à Northgate; um projeto explica 17; escalar as duas sessões noturnas inexplicadas ao líder de segurança. Nenhuma acusação.

**EX037.** Acrescentar um campo `staff_confirmed` (data em que o fornecedor confirmou pela última vez a sua lista de pessoas com acesso), por exemplo "2026-04-01" para a HydroLogic e "2025-09-15" para a Northgate. Regra: `if (TODAY - dt.date.fromisoformat(conf)).days > 180: f.append("staff list unconfirmed >180 days")`. A saída então mostra a sinalização em `v-integr` e não em `v-hydro1`. Isso importa porque os desligamentos de pessoal nos fornecedores são uma forma comum de credenciais válidas sobreviverem aos seus donos.

**EX038.** (1) Só as pessoas nomeadas no Anexo A podem acessar; mudanças notificadas por escrito antes do acesso (verificado em cada revisão trimestral). (2) Toda sessão remota usa o gateway da empresa com autenticação multifator (verificado pela configuração e pelos logs do gateway). (3) O fornecedor notifica a empresa em até 24 horas quando uma pessoa da lista sai ou perde um dispositivo usado para o acesso (verificado pela confirmação trimestral da lista de pessoal). (4) O fornecedor entrega os registros de trabalho de qualquer sessão em até 2 dias úteis após o pedido (verificado por amostragem). (5) Ao fim do contrato, o fornecedor confirma por escrito, em até 14 dias, que os dados da empresa foram apagados (verificado pelo registro na biblioteca).

**EX039.** "TLP:AMBER+STRICT. L. — a revisão de acesso de fornecedores encontrou 19 sessões da Northgate em 90 dias. J. Tan e o registro de trabalho da Northgate explicam 17 (comissionamento da telemetria da KW-11, aprovado em março). Duas estão inexplicadas: 12 de abril e 19 de abril, ambas começando às 02:00, horário local (01:00 UTC); origem e destino na exportação do gateway anexa. Desconhecido: quem se conectou e o que foi feito. Peço que você revise os registros de sessão pelo caminho de escalonamento de incidentes e oriente se devemos restringir a conta. Por favor, não contate a Northgate até decidir. Volto a falar com você às 16:00."

**EX040.** (1) Revisado: as seis contas de fornecedores no gateway de acesso remoto, 4 de maio, exportação somente leitura autorizada por A. Mensah. (2) Constatações: uma conta sem nome, uma sem MFA, uma de contrato encerrado, uma sem uso, uma com volume incomum (evidências anexas). (3) Decidido por A. Mensah: duas contas desabilitadas; substituta nomeada em até 14 dias. (4) Solicitado a você: aprovar as cláusulas contratuais-padrão para as renovações; aprovar orçamento para a MFA da ScadaCo, se ela não puder custeá-la; confirmar revisões mensais. (5) Em aberto: duas sessões noturnas inexplicadas da Northgate — com o líder de segurança, atualização na sexta-feira; pressuposto de que o gateway é o único caminho de acesso — comparação com o firewall até junho (J. Tan).

### Capítulo 9

**EX041.** Ligação ao hospital: prazo 23:40Z de sábado, feita às 23:55Z — 0,25 h de atraso; causa: duas pessoas acreditavam que a outra ligaria (responsabilidade duplicada). Alerta inicial: prazo 21:40Z de domingo, enviado às 18:05Z — 3,58 h antes do prazo; o modelo funcionou. Seguradora: prazo 21:40Z de segunda-feira — em atraso, não enviado; causa: obrigação ausente do registro. Notificação do incidente: prazo 21:40Z de terça-feira, enviada às 22:30Z — 0,83 h de atraso; causa: aprovação pedida 40 minutos antes do prazo. Relatório final: em aberto, faltando 646,7 h. Todas as causas são lacunas de processo.

**EX042.** "A Kestrel Water está investigando um acesso não autorizado a sistemas de computador que nos ajudam a monitorar o tratamento da água. Por precaução, os nossos operadores estão operando manualmente duas estações de bombeamento. Os testes de qualidade da água estão normais e a água da torneira continua segura para beber. Você não precisa fazer nada. Estamos trabalhando com as autoridades competentes e atualizaremos esta página e as nossas redes sociais até as 18:00 de hoje, ou antes, se algo mudar."

**EX043.** "Aqui é [nome], coordenador de plantão da Kestrel Water. Amanhã, entre 09:00 e 13:00, vamos comutar de forma controlada as estações que atendem o seu local. A água continua segura para beber. A pressão pode cair no lado leste por até quatro horas; o abastecimento não deve parar. Por favor, confiram os arranjos de água armazenada para a esterilização e a diálise. Há algo no seu local que precise de pressão total nessa janela, ou um horário que seria pior para vocês? Ligo de novo amanhã às 08:00 para confirmar; o nosso número 24 horas é [número]."

**EX044.** "Estamos investigando com as autoridades competentes e não seria correto especular sobre a causa ou sobre qualquer pessoa ou empresa enquanto esse trabalho continua. Compartilharemos o que pudermos quando pudermos confirmar." Raciocínio: a informação não está confirmada (veracidade); nomear um fornecedor ou uma pessoa poderia prejudicá-los injustamente e pode estar errado (justiça); comprometemo-nos a atualizar (correção e transparência).

**EX045.** Prazos internos: ligação ao hospital — o dono (coordenador) liga em até 60 minutos do início do relógio; alerta inicial — rascunho com 12 h, aprovação pedida até 18 h; notificação do incidente — rascunho com 48 h, aprovação pedida até 60 h; seguradora — incluída no registro, notificada junto com o alerta inicial. Delegação: se o diretor-presidente não estiver disponível, o diretor de operações aprova, e depois o diretor de operações substituto. Modelos preparados para cada uma. O líder de incidente registra o início do relógio em UTC no log de decisões.

### Capítulo 10

**EX046.** "3/6" conta o I3 como sucesso, embora nenhuma justificativa tenha sido registrada para uma decisão de segurança, e trata o I5 — um cliente crítico nunca informado — como apenas uma falha entre seis. O I4 não tinha dono. O defeito mais grave é o I5: num incidente real, o hospital não teria sido avisado (ou o I3, se você argumentar que decisões de segurança não registradas são piores; exige-se raciocínio).

**EX047.** Acrescentar as colunas `safety` (yes para o I2 e o I3) e `consulted` (por exemplo, I3 "Security lead", I2 "Coordinator") e a regra `if r["safety"] == "yes" and r["owner"] != "Ops manager" and "Ops manager" not in r["consulted"]: f.append("operations not consulted")`. Com as seis linhas originais, a nova sinalização nunca dispara — o I2 e o I3 têm ambos o gerente de operações como dono, de modo que a autoridade sobre a segurança estava onde deveria. A linha inventada `95,I7 station alarm,isolate KW-09 network,Security lead,15,12,yes,yes,Coordinator` é sinalizada com "operations not consulted". Explicar por que o I3 corretamente não é sinalizado recebe a pontuação máxima; forçar uma sinalização no I3, não.

**EX048.** Sintoma: declaração provisória 11 minutos atrasada e sem dono. Hipóteses: (1) nenhum aprovador definido; (2) nenhum modelo; (3) o líder de comunicação não sabia o que podia ser dito. Evidências: a RACI do Capítulo 6 não tinha A para a declaração pública; no hot wash, disseram "esperando alguém mais graduado". Causa: lacuna de titularidade. Correção: diretor-presidente como aprovador, comunicação como responsável, modelo pré-aprovado, aprovador substituto. Verificar: injeção de imprensa no próximo exercício, declaração em até 45 minutos, com o aprovador registrado.

**EX049.** Causa: nenhum dono nem calendário para verificar os contatos críticos; o hospital se reorganizou e ninguém foi avisado. Correção: o coordenador é dono da lista de contatos críticos; ligações de teste trimestrais registradas; o acordo com o hospital exige a notificação de mudanças de contato; uma segunda via (central telefônica do hospital até o gerente de plantão do local). Métrica: % dos contatos críticos verificados no último trimestre (meta de 100%).

**EX050.** A1: um único líder para o informe ao hospital na RACI e na lista de verificação — dono E. Varga; prazo 30 de junho; evidência de encerramento: RACI v2 publicada; verificação: injeção sobre o hospital no exercício de janeiro. A2: coluna "quem depende do acesso deste fornecedor" no registro de fornecedores — dono A. Mensah; prazo 31 de julho; evidência: exportação do registro; verificação: próxima revisão do Laboratório 8. A3: campo de justificativa e papel de escriba no modelo de log de decisões — dono: coordenador; prazo 15 de junho; evidência: modelo v2; verificação: nova execução do Laboratório 10 sobre o próximo exercício mostra justificativa em todas as decisões.

### Capítulo 11

**EX051.** (1) "Em até 20 minutos após a injeção de imprensa, uma declaração provisória é aprovada pelo executivo aprovador, e o horário da aprovação é registrado." (2) "Em até 30 minutos após a injeção de comprometimento do fornecedor, a equipe decide se suspende o acesso desse fornecedor, registra o dono e a justificativa e identifica quem depende dele." (3) "Quando a injeção do operador do turno da noite é apresentada, o papel do operador chega ao líder de incidente ou ao substituto em até 10 minutos usando apenas o cartão de escalonamento impresso."

**EX052.** Injeção do O2 (00:35): "O engenheiro de plantão da HydroLogic liga: eles precisam se reconectar agora para consertar uma falha numa bomba dosadora da KW-02." Esperado: recusar a reconexão remota; providenciar suporte supervisionado no local ou operação manual; registrar a decisão. Injeção do O4 (01:10): "O oficial de plantão do regulador envia um e-mail perguntando se um alerta inicial está a caminho, com prazo em 4 horas." Esperado: confirmar a via de aprovação e enviar dentro do prazo; registrar o horário. Ambas marcadas como "EXERCÍCIO — EXERCÍCIO — EXERCÍCIO".

**EX053.** Objetivos 1 (vago; reescrever como observável). Cenário 1 (catastrófico e implausível; nada específico é aprendido; usar um cenário plausível de comprometimento de fornecedor). Injeções 1 (não ligadas). Papéis e segurança 0 (o diretor-presidente avalia o próprio exercício; a conta real de e-mail arrisca confusão com um evento real; usar um canal marcado do exercício, avaliadores independentes, oficial de segurança). Avaliação 1 (sem critérios). Ética: risco de julgar pessoas; reafirmar as regras básicas.

**EX054.** O1 atendido — declarado aos 9 min, com justificativa; ação: nenhuma. O2 parcialmente atendido — 52 min contra 30; dependência desconhecida; ação: coluna de dependência no registro de fornecedores (A. Mensah, julho). O3 não atendido — sem dono; ação: um único líder na RACI e na lista de verificação (E. Varga, junho). O4 atendido — alerta inicial aprovado e enviado; ação: nenhuma, manter o modelo. O5 parcialmente atendido — atrasado, sem dono até a chegada do diretor-presidente; ação: diretor-presidente como aprovador, aprovador substituto, modelo (R. Adeyemi, junho). Nenhuma pessoa apontada como culpada.

**EX055.** Durante: agradecer ao diretor-presidente e então perguntar diretamente ao gerente de operações: "Na realidade, quem decidiria sobre isolar a KW-04?"; convidar cada dono de papel pelo nome; registrar quem decidiu. Depois: registrar no AAR como "os direitos de decisão sobre o isolamento técnico estavam pouco claros na prática", com uma ação para confirmá-los na RACI; informar antes o diretor-presidente, em particular e com respeito, sobre a constatação do AAR, apresentando-a como uma questão do plano.

### Capítulo 12

**EX056.** Índice de exemplo: 1. Mapa de dependências (EX009) — "Verifico os pressupostos por trás das decisões sobre clientes críticos." 2. Reescrita da autorização (EX011) — "Torno responsabilizável o trabalho em sistemas operacionais." 3. Registro de decisão (EX012) — "Registro decisões com justiça, com os desconhecidos." 4. Resumo do registro (EX020) — "Classifico pela consequência e mantenho a higiene." 5. Métricas (EX023) — "Meço o que conduz decisões." 6. RACI e cartão (EX026, EX028) — "Torno os papéis inequívocos." 7. Cartões de controle e plano (EX031, EX033) — "Distingo declarado de testado." 8. Caso do fornecedor (EX040) — "Analiso casos com justiça." 9. Desenho das notificações (EX045) — "Cumpro os prazos." 10. AAR e log de ações (EX054, EX050). Todos rotulados como "trabalho do curso sobre dados sintéticos".

**EX057.** Um roteiro que segue a seção 12.4: contexto em termos de consequência, com um alerta com fonte; principais riscos com donos e níveis de garantia; duas ou três constatações do exercício e as suas correções; progresso em relação ao plano; três pedidos (a aceitação de uma exceção com validade, cláusulas contratuais, uma declaração de apetite). Cada número rastreável até o portfólio.

**EX058.** Dias 1–30: conhecer a liderança clínica e a de infraestrutura predial, a equipe de dispositivos médicos, a TI, os fornecedores e o contato no regulador; mapear os serviços clínicos e as suas dependências (energia, água, gases medicinais, redes, dispositivos); ler o histórico de incidentes. Dias 31–60: donos para os riscos de nível de segurança do paciente, RACI de incidentes incluindo os tomadores de decisão clínicos (desvio de pacientes, procedimentos de contingência), cartão de escalonamento, registro de notificações (incluindo eventuais obrigações do setor de saúde), revisão dos fornecedores que mantêm dispositivos. Dias 61–90: exercício de mesa sobre a perda dos sistemas clínicos, com a liderança clínica participando, AAR, apresentação ao conselho com pedidos.

**EX059.** Evidências: plano de teste autorizado; log cronometrado (início, passos, fim); registro do resultado, com verificação da completude dos dados em relação a um período de referência; problemas e correções; aprovação do dono do serviço. Perguntas do auditor: "Foi uma restauração completa do sistema ou só do banco de dados?" e "Foi restaurado num ambiente isolado semelhante à produção, e o mesmo tempo valeria para uma interrupção do local inteiro?"

**EX060.** Modelo: Enquadrar e identificar 3 (EX001, EX005); Analisar e decidir 2 (EX017, EX018 — a calibração da probabilidade ainda é fraca); Organizar 3 (EX026); Verificar 2 (EX033 — nunca desenhei um teste real com um engenheiro); Comunicar 3 (EX042, EX043); Melhorar 2 (EX050). Plano de aprendizagem: estudar os Capítulos 5–9 do curso técnico para os fundamentos de verificação em TO até dezembro; calibrar a probabilidade com dois alertas setoriais por mês e uma revisão por um coordenador par até janeiro.

<a id="glossary"></a>

## Glossário

- **Aprovador (Accountable, na RACI)** — a única pessoa que responde pelo resultado de uma atividade e dá a aprovação final.
- **Relatório pós-ação (AAR)** — um relatório que avalia um exercício ou incidente em relação aos objetivos, com evidências e recomendações.
- **Nível de garantia** — quão solidamente a operação de um controle está estabelecida: declarado, documentado, observado ou testado.
- **Autorização** — uma aprovação escrita e específica do dono da consequência, que define escopo, atividades, pessoas, janela, condições de parada e tratamento de dados.
- **Cliente crítico** — um destinatário do serviço para quem a interrupção prejudica pessoas rapidamente (por exemplo, um hospital).
- **Registro de decisão** — um registro datado de uma decisão, de quem a tomou, das opções, das informações conhecidas e desconhecidas, das condições e dos destinatários.
- **Serviço essencial** — um serviço cuja interrupção prejudica pessoas, a economia ou a ordem pública rapidamente e em grande escala.
- **Exceção** — uma decisão com dono, compensada e com prazo de operar sem um controle exigido.
- **Declaração provisória** — uma mensagem pública inicial e factual, emitida antes que o quadro completo seja conhecido.
- **Hot wash** — a conversa de balanço imediata após um exercício.
- **Injeção** — uma informação do cenário, apresentada num momento definido durante um exercício.
- **Registro de notificações** — uma lista de todas as obrigações externas de informar, com gatilho, destinatário, prazo, dono e canal.
- **RACI** — uma matriz de atividades contra papéis: Responsável, Aprovador (Accountable), Consultado, Informado.
- **Apetite a risco** — a quantidade de risco que a liderança está disposta a aceitar, declarada de antemão.
- **Dono do risco** — a pessoa com autoridade e orçamento para decidir como um risco é tratado.
- **Condição de parada** — um evento observável, acordado de antemão, que encerra imediatamente um trabalho autorizado.
- **Exercício de mesa** — um exercício baseado em discussão, no qual os participantes conversam sobre a sua resposta a um cenário.
- **Traffic Light Protocol (TLP)** — um esquema de marcação que indica até onde os destinatários podem compartilhar uma informação.

<a id="references"></a>

## Referências

Normas, leis, orientações e páginas públicas mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas. Uma citação apoia a afirmação geral ao seu lado no texto, nunca os detalhes do caso sintético. A lista é idêntica à da edição em inglês.

### Leis, frameworks e orientações

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
- Cybersecurity and Infrastructure Security Agency. [CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages).
- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency and Federal Bureau of Investigation. [DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks (AA21-131A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a). May 2021.
- Cybersecurity and Infrastructure Security Agency et al. [IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities (AA23-335A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). December 2023.
- European Parliament and Council. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj), in particular Articles 20, 21 and 23.
- Federal Emergency Management Agency. [Homeland Security Exercise and Evaluation Program (HSEEP)](https://www.fema.gov/emergency-managers/national-preparedness/exercises/hseep).
- FIRST. [Traffic Light Protocol (TLP) version 2.0](https://www.first.org/tlp/).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Cyber Security Centre (UK). [Exercise in a Box](https://www.ncsc.gov.uk/information/exercise-in-a-box).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0, CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), February 2024; [Cybersecurity Framework home](https://www.nist.gov/cyberframework).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-84, Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).
- National Institute of Standards and Technology. [SP 800-161 Rev. 1, Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).

### Documentação de software

- Python Software Foundation. [csv](https://docs.python.org/3/library/csv.html) and [datetime](https://docs.python.org/3/library/datetime.html). Python 3 documentation.
