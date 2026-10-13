# Segurança da Informação: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 094, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 40 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3; os capítulos 11–40 (EX031–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de bacharelado que aprendem como uma pequena organização financeira protege as informações dos seus associados por meio da governança, dos controles técnicos, das operações e da medição.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios revisam acessos sintéticos a aplicações em relação à situação no RH e ao cargo, medem achados sintéticos de vulnerabilidades em relação às metas de correção e geram hashes de senhas sintéticas com PBKDF2 com sal, conferindo-as contra uma pequena lista de senhas vazadas. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de bacharelado desde a computação, as redes, a programação, a estatística, a escrita, o direito e a ética, passando pela governança, pelo risco, pelo acesso e pela criptografia, depois pela segurança operacional, pela medição e pela auditoria, até a gestão de mudanças, um projeto em grupo, um estágio e um trabalho de conclusão. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Aisha Rahimi** | Estudante de bacharelado | Inventada |
| **Dr. Neil Carrow** | Tutor pessoal | Inventado |
| **Pennick University** | Universidade fictícia | Inventada |
| **Ashfield Credit Union** | Cooperativa de crédito fictícia, com cerca de 140 funcionários, quatro agências e 35.000 associados | Inventada |

### Fontes principais

Anderson (2020), [doi:10.1002/9781119644682](https://doi.org/10.1002/9781119644682); ISO/IEC 27000:2026; ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); ISO/IEC 27002:2022; NIST SP 800-53 Rev. 5; NIST SP 800-30 Rev. 1; FIPS 199, [doi:10.6028/NIST.FIPS.199](https://doi.org/10.6028/NIST.FIPS.199); NIST CSWP 29 (CSF 2.0); Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Shadish, Cook e Campbell (2002). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Estudando segurança da informação em Pennick

### Objetivos de aprendizagem

Você vai (1) descrever o que um bacharelado em segurança da informação abrange; (2) conhecer o caso que acompanha o curso; (3) planejar hábitos de estudo para um curso de quatro anos.

### 1.1 A estudante e o curso

Aisha Rahimi começa um bacharelado de quatro anos em segurança da informação na fictícia Pennick University. Seu tutor pessoal é o Dr. Neil Carrow, que leciona a disciplina de fundamentos do primeiro ano. O curso trata de como as organizações protegem a informação: a tecnologia envolvida, as pessoas que a usam, as regras que a governam e as formas de medir a segurança. O Dr. Carrow explica que a segurança não é apenas um assunto técnico, e que os formados precisam explicar os riscos com clareza a gerentes que não são especialistas. Aisha escolheu o curso depois que um parente foi vítima de uma fraude on-line.

### 1.2 A organização do caso

Ao longo do curso, Aisha trabalha com a fictícia Ashfield Credit Union, uma cooperativa de poupança e empréstimo pertencente aos associados, com cerca de 140 funcionários, quatro agências e aproximadamente 35.000 associados. A Ashfield guarda saldos de poupança, registros de empréstimos, documentos de identidade e dados de pagamento. Uma violação prejudicaria diretamente os associados e abalaria a confiança numa organização pequena que depende da sua reputação local. O Dr. Carrow organizou a parceria para que os estudantes possam ver como cada tema se aplica a um tipo real de organização, usando dados sintéticos em todos os exercícios. Cada disciplina a utiliza.

### 1.3 Como o curso é organizado

O primeiro ano constrói os fundamentos: computadores, redes, programação, estatística, escrita, direito e ética. O segundo ano introduz a governança de segurança, o risco, o controle de acesso e a criptografia. O terceiro ano trata da segurança operacional: vulnerabilidades, configuração, monitoramento, incidentes, backups, fornecedores e medição. O último ano inclui a gestão de mudanças, um projeto em grupo, um estágio, métodos de pesquisa e um trabalho de conclusão. Aisha observa que cada ano se apoia no anterior, de modo que as lacunas deixadas no início ficam mais difíceis de preencher depois. Ela imprime o mapa das disciplinas e o prende acima da escrivaninha, marcando que disciplinas dependem de quais anteriores.

### 1.4 Hábitos de estudo

O Dr. Carrow aconselha Aisha a manter um diário de aprendizagem, registrando uma ideia de segurança por semana e como ela se aplica à Ashfield. Ele também recomenda ler fontes primárias, como normas e artigos conhecidos, em vez de depender apenas de resumos. Aisha reserva duas horas toda sexta-feira para revisão. Ela aprende que a segurança muda depressa, então o hábito de conferir as fontes atuais e suas edições importa tanto quanto lembrar qualquer fato isolado. Seu primeiro registro no diário descreve por que uma pequena cooperativa de crédito é um alvo atraente para fraudadores, que esperam defesas mais fracas do que nos grandes bancos.

### Exemplo resolvido

Aisha começa o curso, conhece o caso da Ashfield, mapeia os quatro anos de estudo e cria um hábito de revisão semanal.

> **Caso sintético.** A Pennick, a Ashfield e todas as pessoas são sintéticas.

### Erros e limites

Tratar a segurança como algo puramente técnico ignora as pessoas, as regras e a medição.

### Exercícios

- **EX001 — Tamanho do caso.** Quantos associados a Ashfield tem? *Rubrica:* 3 = aproximadamente 35.000;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX002 — Último ano.** O que o último ano inclui? *Rubrica:* 3 = gestão de mudanças, projeto em grupo, estágio, pesquisa e trabalho de conclusão;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.

- **EX003 — Hábito semanal.** Que hábito de diário o Dr. Carrow aconselha? *Rubrica:* 3 = uma ideia de segurança por semana aplicada à Ashfield;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — O que é segurança da informação

### Objetivos de aprendizagem

Você vai (1) definir confidencialidade, integridade e disponibilidade; (2) aplicá-las a exemplos; (3) explicar por que a segurança apoia os objetivos da organização.

### 2.1 Três objetivos

Aisha aprende os três objetivos que definem a segurança da informação. A FIPS 199, uma norma federal dos Estados Unidos, define a confidencialidade como a preservação das restrições autorizadas ao acesso e à divulgação, a integridade como a proteção contra a modificação ou a destruição indevidas, e a disponibilidade como a garantia de acesso e uso oportunos e confiáveis da informação. A ISO/IEC 27000:2026 descreve a segurança da informação nos mesmos três termos. O Dr. Carrow observa que esses objetivos são amplamente usados porque cobrem a maioria das formas pelas quais a informação pode ser prejudicada. Aisha copia as três definições no seu diário e escreve um exemplo da Ashfield ao lado de cada uma.

### 2.2 Aplicando os objetivos

Aisha aplica os objetivos à Ashfield. Os documentos de identidade dos associados precisam de confidencialidade, porque sua exposição poderia possibilitar fraudes. Os saldos das contas precisam de integridade, porque um saldo alterado significaria que alguém perde dinheiro. O serviço de internet banking precisa de disponibilidade, porque os associados esperam ver seu dinheiro quando quiserem. Ela observa que cada informação costuma precisar dos três em algum grau, mas que um deles muitas vezes importa mais, o que ajuda a decidir para onde vai o esforço. Ela registra o objetivo mais importante de cada item numa tabela simples, que vai reutilizar quando o curso chegar à avaliação de riscos, no segundo ano.

### 2.3 Além da tríade

O Dr. Carrow apresenta propriedades relacionadas. A autenticidade significa confirmar que uma informação ou uma pessoa é genuína; a responsabilização significa que as ações podem ser rastreadas até quem as executou; o não repúdio significa que alguém não consegue negar de forma crível uma ação que realizou. Na Ashfield, uma aprovação de empréstimo precisa ser rastreável até o agente que a aprovou. Aisha aprende que essas propriedades ampliam os três objetivos e muitas vezes dependem de uma boa gestão de identidades e da manutenção de registros. Ela acrescenta as três propriedades à tabela do diário, anotando para cada registro da Ashfield se a responsabilização ou a autenticidade importa tanto quanto os três objetivos originais.

### 2.4 Segurança e objetivos

A segurança existe para apoiar o propósito da Ashfield, e não como um fim em si mesma. Um controle que impede os associados de acessar suas poupanças pode proteger a confidencialidade, mas prejudica a disponibilidade e a confiança. Aisha aprende que uma boa segurança equilibra a proteção com a usabilidade e o custo. O Dr. Carrow pede que ela se lembre de que os profissionais de segurança ajudam as organizações a assumir riscos sensatos, e não a evitar todo risco, porque uma cooperativa de crédito que recusasse todo risco não conseguiria emprestar dinheiro algum. Aisha escreve um breve parágrafo no diário descrevendo um controle do seu próprio banco que ela acha irritante e pergunta se a proteção que ele oferece justifica o incômodo.

### Exemplo resolvido

Aisha define os três objetivos a partir da FIPS 199, os aplica às informações da Ashfield, acrescenta a autenticidade e a responsabilização e liga a segurança aos objetivos da Ashfield.

> **Caso sintético.** Os exemplos são sintéticos.

### Erros e limites

Maximizar um objetivo pode prejudicar os outros.

### Exercícios

- **EX004 — Definição de disponibilidade.** Como a FIPS 199 define a disponibilidade? *Rubrica:* 3 = acesso e uso oportunos e confiáveis;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX005 — Objetivo dos saldos.** Que objetivo importa mais para os saldos? *Rubrica:* 3 = integridade;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX006 — Rastreabilidade dos empréstimos.** Que propriedade torna rastreáveis as aprovações de empréstimos? *Rubrica:* 3 = responsabilização;; 2 = correto;; 1 = outra;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — A informação nas organizações

### Objetivos de aprendizagem

Você vai (1) identificar as informações que uma organização guarda; (2) rastrear como as informações circulam; (3) reconhecer quem é responsável por elas.

### 3.1 O que a Ashfield guarda

Aisha lista as informações que a Ashfield guarda: dados de identificação dos associados, registros de poupança e de empréstimos, dados de cartões de pagamento, registros dos funcionários, atas do conselho e contratos com fornecedores. Parte delas fica no sistema bancário central, parte no e-mail e em pastas compartilhadas e parte em papel nas agências. O Dr. Carrow aponta que as informações em papel e em conversas também precisam de proteção, e que muitas violações envolvem informações fora dos sistemas principais. Ela também observa as fichas de adesão em papel guardadas nos armários das agências e as pastas de empréstimo à espera de digitalização numa bandeja destrancada, como exemplos de informações fora de qualquer sistema computacional.

### 3.2 Fluxos

A informação se movimenta. Os documentos de identidade de um novo associado são digitalizados numa agência, enviados ao sistema central e conferidos por um responsável pela conformidade. Os pedidos de empréstimo passam da equipe da agência para os agentes de crédito e daí para um comitê de crédito. Aisha desenha esses fluxos e anota onde a informação sai da Ashfield, por exemplo para uma agência de informações de crédito e para um processador de cartões. Ela aprende que cada fluxo é um ponto em que a informação pode ser interceptada, alterada ou perdida. Ela rotula cada seta do diagrama com a informação que ela transporta e o método usado para enviá-la.

### 3.3 Responsabilidade

Todo tipo de informação precisa de alguém responsável por decidir como ela é protegida. Na Ashfield, o chefe de crédito é responsável pelos registros de empréstimos, e o responsável pela conformidade, pelos documentos de identidade. Aisha descobre que ninguém é claramente responsável pelas pastas compartilhadas, onde os funcionários salvam cópias de relatórios. O Dr. Carrow explica que as informações sem dono tendem a se acumular sem controles, e que atribuir a responsabilidade costuma ser o primeiro passo prático de segurança. Mais tarde, o diretor executivo da Ashfield atribui as pastas compartilhadas ao chefe de operações, que começa pedindo às equipes que apaguem as cópias antigas.

### 3.4 Valor e dano

Aisha estima o dano caso cada tipo de informação fosse exposto, alterado ou ficasse indisponível. A exposição dos documentos de identidade poderia possibilitar fraudes contra os associados; registros de empréstimos alterados poderiam esconder empréstimos ruins; a indisponibilidade do sistema bancário central interrompe todas as transações. Ela ordena as informações pelo dano potencial. Ela aprende que essa ordenação orienta onde gastar o esforço de segurança limitado, e que ela precisa ser revista quando a organização muda. Ela apresenta a ordenação ao seu grupo de seminário, que contesta duas das posições. Depois da discussão, ela sobe as atas do conselho, porque contêm decisões confidenciais sobre perdas com empréstimos e sobre funcionários.

### Exemplo resolvido

Aisha lista as informações da Ashfield, desenha os fluxos, inclusive os externos, encontra pastas compartilhadas sem dono e ordena as informações pelo dano potencial.

> **Caso sintético.** Os tipos de informação são sintéticos.

### Erros e limites

Ignorar o papel e as pastas compartilhadas deixa muita informação sem proteção.

### Exercícios

- **EX007 — Destinatários externos.** Cite um destinatário externo de informações da Ashfield. *Rubrica:* 3 = uma agência de informações de crédito;; 2 = um;; 1 = nada;; 0 = nenhuma.

- **EX008 — Repositório sem dono.** Que repositório não tinha uma pessoa responsável? *Rubrica:* 3 = as pastas compartilhadas;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX009 — Propósito da ordenação.** O que a ordenação pelo dano orienta? *Rubrica:* 3 = onde gastar o esforço de segurança;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Computadores e sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) descrever como os computadores executam programas; (2) explicar as contas de usuário e as permissões; (3) reconhecer por que as atualizações importam.

### 4.1 Como os computadores executam programas

Aisha aprende que um computador executa programas sob um sistema operacional, que gerencia a memória, os arquivos e os dispositivos. Cada programa roda como um processo, e o sistema operacional mantém os processos separados, para que um não possa interferir diretamente no outro. Os computadores das agências da Ashfield rodam um sistema operacional de desktop comum, enquanto seus servidores rodam outro. O Dr. Carrow explica que entender esses fundamentos ajuda a equipe de segurança a ver como os ataques funcionam e por que certos controles são necessários. Aisha instala uma máquina virtual no seu notebook para poder explorar um sistema operacional com segurança, sem afetar os próprios arquivos.

### 4.2 Contas e permissões

Os sistemas operacionais usam contas para decidir quem pode fazer o quê. As contas comuns podem executar programas e usar seus próprios arquivos; as contas de administrador podem instalar software e alterar configurações. Aisha descobre que alguns funcionários das agências da Ashfield usam contas de administrador todos os dias, porque uma aplicação antiga um dia precisou disso. Se um desses funcionários abrir um anexo malicioso, o malware também ganha direitos de administrador. Ela recomenda contas comuns para o trabalho diário. O gerente de TI da Ashfield testa a aplicação antiga com uma conta comum e descobre que agora ela funciona, então as contas de administrador de uso diário podem ser removidas.

### 4.3 Atualizações

O software contém falhas, e os fornecedores publicam atualizações para corrigi-las. Os atacantes estudam as atualizações para descobrir o que foi corrigido e então miram os sistemas ainda não atualizados. Aisha confere uma lista sintética dos computadores da Ashfield e encontra vários com semanas de atraso nas atualizações, porque os funcionários adiam as reinicializações. Ela recomenda a instalação automática fora do horário das agências. O Dr. Carrow observa que aplicar as atualizações prontamente é uma das práticas de segurança mais eficazes e menos glamorosas. O gerente de TI concorda em agendar as reinicializações à noite, e Aisha sugere relatar todo mês o número de computadores com mais de duas semanas de atraso.

### 4.4 Fundamentos de malware

Malware é software projetado para causar dano: roubar informações, cifrar arquivos para pedir resgate ou dar aos atacantes o controle remoto. Ele muitas vezes chega por anexos de e-mail, sites maliciosos ou mídias removíveis infectadas. Aisha aprende como o antivírus e as ferramentas de endpoint mais recentes detectam comportamentos suspeitos, e por que eles não bastam sozinhos. Ela observa que as contas comuns, as atualizações rápidas e o cuidado com o e-mail, juntos, reduzem a chance de sucesso do malware. Ela escreve um breve registro no diário comparando como cada controle teria impedido uma infecção por ransomware descrita numa notícia que leu naquela semana, o que a ajuda a lembrar por que as camadas importam.

### Exemplo resolvido

Aisha aprende a separação de processos, encontra o uso diário de contas de administrador nas agências, recomenda atualizações automáticas e liga as defesas contra malware às contas e às atualizações.

> **Caso sintético.** Os computadores são sintéticos.

### Erros e limites

O uso diário de contas de administrador dá ao malware direitos de administrador.

### Exercícios

- **EX010 — Causa do administrador.** Por que alguns funcionários usam contas de administrador? *Rubrica:* 3 = uma aplicação antiga um dia precisou disso;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX011 — Atraso nas atualizações.** Por que alguns computadores estão atrasados nas atualizações? *Rubrica:* 3 = os funcionários adiam as reinicializações;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX012 — Vias do malware.** Cite uma forma pela qual o malware chega. *Rubrica:* 3 = anexos de e-mail;; 2 = uma;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Redes e a internet

### Objetivos de aprendizagem

Você vai (1) descrever como as redes conectam computadores; (2) explicar os firewalls e a cifração em trânsito; (3) reconhecer as ameaças de rede comuns.

### 5.1 Como as redes conectam

Aisha aprende que as redes conectam dispositivos para que possam trocar dados. As agências da Ashfield se conectam à sede por enlaces cifrados, e a sede se conecta à internet e ao processador de cartões. Cada dispositivo tem um endereço, e os roteadores encaminham os dados entre as redes. O Dr. Carrow desenha a rede num quadro branco e pede que os estudantes marquem por onde trafegam os dados dos associados, o que os ajuda a ver onde a proteção é necessária. Aisha redesenha o diagrama com capricho em casa e marca a conexão com o processador de cartões como o enlace externo mais sensível.

### 5.2 Firewalls

Um firewall controla que tráfego pode passar entre as redes. O firewall da Ashfield permite o tráfego web para o site de internet banking e bloqueia a maioria das outras conexões de entrada. Aisha aprende que as regras de firewall se acumulam com o tempo e muitas vezes incluem exceções antigas de que ninguém se lembra. Ela revisa uma lista sintética de regras e encontra uma regra que permite acesso de área de trabalho remota de qualquer lugar, criada para um fornecedor anos atrás. Ela recomenda removê-la depois de conferir com o fornecedor. O fornecedor confirma que agora usa um serviço seguro de acesso remoto, então a regra antiga é removida sem transtornos.

### 5.3 Cifração em trânsito

Quando os dados atravessam as redes, outras pessoas podem conseguir lê-los. A cifração em trânsito, como o protocolo seguro usado pelos sites, protege a confidencialidade e a integridade ao longo do caminho. Aisha confere que o internet banking da Ashfield a utiliza e que as versões antigas e fracas do protocolo estão desativadas. Ela aprende que a cifração protege os dados enquanto se movem, mas não depois que chegam a um servidor comprometido, então outros controles continuam necessários. Ela usa um verificador on-line gratuito contra um site de teste para ver que versões do protocolo ele aceita e registra os resultados no diário.

### 5.4 Ameaças de rede

Aisha estuda as ameaças comuns: atacantes que varrem a rede em busca de serviços abertos, que interceptam o tráfego em redes sem fio desprotegidas e que sobrecarregam os serviços com tráfego para deixá-los indisponíveis. A rede sem fio das agências da Ashfield para os associados é separada das redes da equipe, o que limita o risco. O Dr. Carrow observa que separar as redes pelo propósito é um controle simples, mas poderoso, porque um problema numa rede não chega automaticamente às outras. Aisha confere que a rede sem fio dos associados não alcança a impressora da equipe, o que confirma que a separação funciona. Ela registra esse teste no diário como um exemplo de verificar um controle, em vez de presumir que ele funciona.

### Exemplo resolvido

Aisha mapeia a rede da Ashfield, encontra uma antiga regra aberta de área de trabalho remota, confere a cifração em trânsito e confirma que a rede sem fio dos associados é separada.

> **Caso sintético.** As redes são sintéticas.

### Erros e limites

As exceções antigas de firewall muitas vezes continuam abertas muito depois de terem perdido seu propósito.

### Exercícios

- **EX013 — Regra antiga.** Que regra antiga Aisha encontra? *Rubrica:* 3 = acesso de área de trabalho remota de qualquer lugar;; 2 = correto;; 1 = outra;; 0 = nenhuma.

- **EX014 — Limites da cifração em trânsito.** O que a cifração em trânsito não protege? *Rubrica:* 3 = os dados num servidor comprometido;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX015 — Rede sem fio dos associados.** Como a rede sem fio dos associados é protegida? *Rubrica:* 3 = separada das redes da equipe;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Python para verificações de segurança

### Objetivos de aprendizagem

Você vai (1) escrever scripts simples em Python; (2) ler e conferir arquivos de dados; (3) produzir resultados claros para outras pessoas.

### 6.1 Começando

Aisha escreve seus primeiros scripts em Python usando apenas a biblioteca padrão, para que rodem em qualquer computador da universidade ou da Ashfield sem instalações extras. Seu primeiro script lê de um arquivo de texto uma lista sintética de contas de funcionários e conta quantas existem. O Dr. Carrow explica que os scripts permitem que a equipe de segurança confira milhares de registros de forma rápida e coerente, onde a conferência manual seria lenta e sujeita a erros. Ela escreve o script num editor de texto simples, o executa pela linha de comando e confere a contagem com o número de linhas do arquivo. Os dois números coincidem.

### 6.2 Conferindo dados

O script seguinte de Aisha confere a data do último login de cada conta. As contas sem login há noventa dias são listadas para revisão. Ela usa o módulo datetime para comparar as datas. Quando uma linha tem a data faltando, o script a registra separadamente, em vez de travar. Ela aprende que os dados reais contêm lacunas e erros, e que um bom script de conferência relata os problemas da sua entrada com a mesma clareza dos resultados que foi escrito para encontrar. Três linhas do arquivo sintético não têm data.

### 6.3 Saída clara

O Dr. Carrow pede que Aisha torne sua saída legível para os gerentes. Ela imprime um título, a data da conferência, o número de contas conferidas, o número de contas sinalizadas e uma lista das contas sinalizadas com as datas do último login. Ela também salva os resultados num arquivo CSV usando o módulo csv. Ela aprende que a pessoa que lê um relatório de segurança muitas vezes decide o que acontece em seguida, então a clareza importa. O Dr. Carrow avalia a segunda versão como clara e pede que a turma use o formato dela como modelo para os relatórios seguintes.

### 6.4 Mantendo os scripts seguros

Os scripts de Aisha lidam com dados sensíveis. Ela os guarda, junto com suas saídas, numa pasta protegida, nunca envia por e-mail para endereços pessoais resultados que contenham nomes de contas e apaga os arquivos temporários depois do uso. Ela também evita escrever senhas dentro dos scripts. O Dr. Carrow observa que as ferramentas de segurança podem se tornar riscos de segurança se suas saídas vazarem, porque uma lista de contas inativas é útil para um atacante que procura logins sem monitoramento. Ela escreve uma breve lista de verificação para o tratamento das saídas e a anexa a cada pasta de scripts, para que os colegas que trabalham com ela sigam as mesmas regras.

### Exemplo resolvido

Aisha escreve scripts com a biblioteca padrão que contam contas, sinalizam inatividade de noventa dias, tratam datas faltantes e produzem relatórios legíveis e arquivos CSV guardados com segurança.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Os relatórios de segurança vazados podem ajudar os atacantes.

### Exercícios

- **EX016 — Limiar de inatividade.** Que contas são sinalizadas? *Rubrica:* 3 = sem login há noventa dias;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX017 — Datas faltantes.** Como o script trata as datas faltantes? *Rubrica:* 3 = as registra separadamente;; 2 = correto;; 1 = trava;; 0 = nenhuma.

- **EX018 — Risco de vazamento.** Por que uma lista de contas inativas poderia ajudar os atacantes? *Rubrica:* 3 = ela mostra logins sem monitoramento;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Estatística para o trabalho de segurança

### Objetivos de aprendizagem

Você vai (1) resumir dados de segurança com estatísticas simples; (2) interpretar proporções e médias; (3) reconhecer comparações enganosas.

### 7.1 Contagens e proporções

Aisha aprende que muitas medidas de segurança são contagens e proporções: o número de computadores sem correção, a parcela da equipe que concluiu o treinamento, a proporção de testes de phishing comunicados. Ela calcula que 112 dos 140 funcionários sintéticos concluíram o treinamento anual, oitenta por cento. O Dr. Carrow pede que ela sempre informe o denominador, porque uma contagem de 112 significa pouco sem saber que é de um total de 140. Ela também informa os vinte e oito funcionários que não o concluíram, listados por agência, para que os gerentes possam cobrar. O Dr. Carrow observa que o mesmo número pode ser apresentado como conclusão ou como lacuna, e as duas visões são úteis.

### 7.2 Médias e dispersão

Aisha calcula quanto tempo a Ashfield leva para fechar os achados de segurança. A média é de vinte e seis dias, mas alguns achados levaram mais de cem dias. A mediana é de quinze dias. Ela aprende que a média é puxada para cima pelos valores extremos, de modo que a mediana muitas vezes descreve melhor um caso típico. Ela informa as duas, mais os casos mais longos, porque esses achados que se arrastam podem representar o maior risco. Ela desenha um gráfico simples dos tempos de fechamento, que mostra a maioria dos achados sendo fechada em até um mês e uma cauda longa de achados lentos.

### 7.3 Comparando grupos

Os gerentes da Ashfield querem saber qual agência é a mais segura. Aisha observa que a maior agência tem mais incidentes, mas também mais funcionários e mais transações. Comparar as contagens brutas a culparia injustamente. Ela calcula os incidentes por cem funcionários, o que muda a ordenação. O Dr. Carrow explica que as taxas permitem uma comparação justa entre grupos de tamanhos diferentes. Com as taxas, a maior agência passa da pior para a segunda melhor, e a menor agência, que teve poucos incidentes no total, acaba tendo a maior taxa. Os gerentes da Ashfield se surpreendem e pedem que ela repita a análise a cada trimestre.

### 7.4 Incerteza

Com números pequenos, as diferenças podem surgir por acaso. Uma agência teve três comunicações de phishing no mês passado e sete neste mês. Aisha explica que essa mudança pode não significar nada, porque contagens tão pequenas variam naturalmente. Ela sugere observar vários meses antes de tirar conclusões. Ela aprende que os relatórios de segurança devem evitar tratar a variação normal como uma mudança significativa. Ela mostra aos gerentes doze meses de comunicações por agência num único gráfico, em que as altas e baixas de um mês para o outro ficam claramente visíveis. Os gerentes concordam em revisar as tendências trimestralmente, em vez de reagir a meses isolados, o que reduz as preocupações desnecessárias.

### Exemplo resolvido

Aisha informa a conclusão do treinamento com seu denominador, compara a média e a mediana dos tempos de fechamento, usa taxas para comparar as agências e alerta para a variação por acaso.

> **Caso sintético.** Os números são sintéticos.

### Erros e limites

Comparar contagens brutas entre grupos de tamanhos diferentes engana.

### Exercícios

- **EX019 — Taxa de treinamento.** Que parcela da equipe concluiu o treinamento? *Rubrica:* 3 = 112 de 140, oitenta por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX020 — Mediana de fechamento.** Qual é a mediana do tempo de fechamento? *Rubrica:* 3 = quinze dias;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX021 — Comparação justa.** Como as agências são comparadas de forma justa? *Rubrica:* 3 = incidentes por cem funcionários;; 2 = correto;; 1 = contagens brutas;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Escrevendo sobre segurança

### Objetivos de aprendizagem

Você vai (1) escrever relatórios de segurança claros; (2) adaptar a escrita a leitores diferentes; (3) citar as fontes corretamente.

### 8.1 Escrita clara

O primeiro trabalho de Aisha é um relatório de uma página sobre as contas inativas da Ashfield. O Dr. Carrow devolve o rascunho marcado com perguntas: qual é o problema, por que ele importa, o que deve ser feito e por quem? Ela o reescreve com um breve resumo no topo, as evidências, o risco e uma recomendação com um responsável. Ela aprende que os leitores ocupados muitas vezes leem apenas o primeiro parágrafo, então ele precisa conter a mensagem principal. O Dr. Carrow dá uma nota alta ao relatório reescrito e comenta que ele permite agir de imediato.

### 8.2 Leitores diferentes

Aisha escreve duas versões do mesmo achado. Para o conselho da Ashfield, ela explica que ex-funcionários ainda poderiam acessar os registros dos associados e que a correção é uma conferência mensal ligada aos procedimentos de desligamento. Para a equipe de TI, ela lista as contas e os passos exatos para desativá-las. O Dr. Carrow observa que os fatos são os mesmos, mas que os leitores precisam de detalhes diferentes para agir. Ela confere as duas versões com um colega que faz o papel de cada leitor, e ele confirma que sabe o que fazer depois de ler. O Dr. Carrow guarda as duas como exemplos.

### 8.3 Citando as fontes

Aisha aprende a citar as fontes com precisão. Quando se refere a uma norma, ela informa o número, a edição e o ano, como em ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022). Quando cita um artigo, ela inclui os autores, o ano, o título e um identificador persistente, se houver. O Dr. Carrow adverte que as normas mudam, então citar a edição informa aos leitores exatamente em que versão ela se baseou, e que ela nunca deve citar uma fonte que não conferiu. Ela monta para o seu diário uma lista de referências que inclui a edição ou o identificador de cada fonte e a data em que a conferiu.

### 8.4 Evitando o alarmismo

A escrita sobre segurança pode resvalar para o alarme. O rascunho de Aisha descrevia uma regra de firewall aberta como catastrófica. O Dr. Carrow pergunta que evidência sustenta essa palavra. Ela reescreve o trecho para informar a regra, o que um atacante poderia fazer e qual a probabilidade disso. Ela aprende que uma linguagem comedida constrói credibilidade, e que os leitores que ouvem alarmes com frequência demais deixam de prestar atenção. O achado revisado informa que a regra permitia conexões de qualquer endereço e que o serviço de área de trabalho remota tinha sido corrigido recentemente, o que reduz a probabilidade imediata, mas não elimina a necessidade de fechá-la.

### Exemplo resolvido

Aisha reescreve um relatório com o resumo primeiro, produz versões para o conselho e para a TI, cita as normas pela edição e substitui a linguagem alarmista por evidências.

> **Caso sintético.** Os relatórios são sintéticos.

### Erros e limites

Citar uma norma sem sua edição deixa os leitores sem saber que versão se aplica.

### Exercícios

- **EX022 — Perguntas do relatório.** Que quatro perguntas um relatório deve responder? *Rubrica:* 3 = problema, importância, ação, responsável;; 2 = todas;; 1 = algumas;; 0 = nenhuma.

- **EX023 — Versão para o conselho.** O que a versão para o conselho enfatiza? *Rubrica:* 3 = ex-funcionários poderiam acessar os registros;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX024 — Citação da edição.** Por que citar a edição de uma norma? *Rubrica:* 3 = as normas mudam;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Direito e segurança

### Objetivos de aprendizagem

Você vai (1) identificar as leis relevantes para a segurança da informação; (2) explicar as obrigações de proteger dados pessoais; (3) reconhecer os limites legais das atividades de segurança.

### 9.1 Por que o direito importa

Aisha aprende que as leis moldam a segurança da informação de várias formas. A legislação de proteção de dados exige que as organizações protejam os dados pessoais com segurança adequada. Os reguladores financeiros esperam que instituições como as cooperativas de crédito gerenciem os riscos operacionais, inclusive os riscos cibernéticos. As leis sobre uso indevido de computadores tornam crime o acesso não autorizado. O Dr. Carrow explica que as leis específicas dependem do país, então o curso ensina princípios e pede que os estudantes confiram a lei aplicável onde trabalham. Aisha monta uma tabela listando cada tipo de lei e a atividade da Ashfield que ela afeta.

### 9.2 Dados pessoais

A Ashfield guarda dados pessoais de associados e funcionários. As leis de proteção de dados de muitos países exigem segurança adequada ao risco, limites para o tempo de guarda dos dados e a notificação de certas violações aos reguladores e às pessoas afetadas. Aisha observa que essas obrigações tornam a segurança um dever legal, e não apenas uma boa prática. Ela aprende que uma violação pode levar a sanções regulatórias e a pedidos de indenização, além da perda de confiança. Ela observa que o responsável pela conformidade da Ashfield é quem decidiria se uma violação precisa ser comunicada, e que a equipe de segurança precisa fornecer os fatos rapidamente.

### 9.3 Acesso não autorizado

As leis sobre uso indevido de computadores tornam crime acessar sistemas sem permissão. Aisha aprende que isso também se aplica aos testes de segurança: testar os sistemas da Ashfield sem autorização por escrito poderia ser ilegal, mesmo com a intenção de ajudar. O Dr. Carrow explica que os testadores profissionais sempre trabalham sob acordos assinados que definem o escopo e o período. Os estudantes nunca devem testar sistemas reais que não sejam seus ou que não tenham permissão para testar. Aisha assina o acordo de testes éticos da universidade, que confirma que os exercícios do curso usam apenas sistemas de laboratório e dados sintéticos fornecidos pelo departamento.

### 9.4 Contratos

Os contratos da Ashfield com os fornecedores incluem obrigações de segurança, como proteger os dados dos associados e comunicar incidentes. Aisha revisa um contrato sintético com o processador de cartões e encontra cláusulas claras de comunicação de incidentes, mas nenhum direito da Ashfield de verificar a segurança do fornecedor. Ela recomenda acrescentar direitos de auditoria na renovação. Ela aprende que os contratos estendem as obrigações de segurança para além dos muros da própria organização. O chefe de operações da Ashfield concorda e acrescenta a mudança à lista de verificação da renovação. Aisha também observa que os contratos devem dizer com que rapidez um fornecedor precisa comunicar incidentes, e descobre que este exige aviso em até vinte e quatro horas.

### Exemplo resolvido

Aisha identifica as leis de proteção de dados, a regulação e as leis sobre uso indevido, liga as obrigações sobre dados pessoais à segurança, insiste na autorização por escrito para os testes e encontra um direito de auditoria faltando num contrato.

> **Caso sintético.** As leis variam conforme o país; o contrato é sintético.

### Erros e limites

Testar sistemas sem autorização por escrito pode ser crime.

### Exercícios

- **EX025 — Tipos de lei.** Cite um tipo de lei que molda a segurança. *Rubrica:* 3 = a legislação de proteção de dados;; 2 = um;; 1 = nada;; 0 = nenhuma.

- **EX026 — Regra dos testes.** O que os testadores precisam sempre ter? *Rubrica:* 3 = autorização assinada que defina o escopo;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX027 — Lacuna do contrato.** O que faltava no contrato com o processador de cartões? *Rubrica:* 3 = direitos de auditoria;; 2 = correto;; 1 = outra;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança

### Objetivos de aprendizagem

Você vai (1) aplicar o raciocínio ético às decisões de segurança; (2) equilibrar o monitoramento e a privacidade; (3) tratar com responsabilidade as fraquezas descobertas.

### 10.1 Raciocínio ético

Os profissionais de segurança muitas vezes têm acesso a informações sensíveis e a ferramentas poderosas. Aisha discute casos em que funcionários usaram mal seu acesso, como consultar os registros de um vizinho por curiosidade. O Dr. Carrow explica que a ética profissional exige usar o acesso apenas para fins autorizados, ser honesto sobre os riscos e respeitar as pessoas afetadas pelas decisões de segurança. Aisha observa que legal e ético não são a mesma coisa, e que algumas ações legais continuam sendo erradas. A turma discute um caso em que um funcionário consultou a conta de uma celebridade e foi demitido.

### 10.2 Monitoramento e privacidade

A Ashfield monitora o e-mail da equipe em busca de sinais de fraude. Aisha pondera até onde o monitoramento deve ir. O monitoramento protege os associados, mas o monitoramento excessivo trata os funcionários como suspeitos e pode invadir mensagens privadas. Ela sugere avisos claros, limitar o monitoramento aos sistemas de trabalho, restringir quem pode ver os resultados e revisar se ele continua necessário. Ela aprende que a proporcionalidade é o teste ético central do monitoramento. O aviso de monitoramento da Ashfield é revisado pelo responsável pela conformidade, que acrescenta uma frase explicando que as mensagens pessoais não são lidas, a menos que haja suspeita de fraude aprovada por dois gerentes.

### 10.3 Fraquezas descobertas

Durante um exercício em aula com um site público, um colega percebe uma fraqueza no site de uma organização real. O grupo de Aisha discute o que fazer. Eles concordam em não explorar mais e em comunicá-la pelo contato publicado pela organização para questões de segurança, se houver um. O Dr. Carrow explica a divulgação coordenada: avisar a organização em particular e dar tempo para a correção antes de qualquer discussão pública. O grupo registra o que viu, informa o Dr. Carrow e redige uma breve mensagem para a organização, que o Dr. Carrow revisa antes que ela seja enviada pelo canal oficial.

### 10.4 Justiça

As decisões de segurança afetam as pessoas de forma desigual. Uma regra que bloqueia logins vindos do exterior pode impedir fraudes, mas também bloqueia os associados que estão viajando ou morando fora do país. Aisha sugere permitir que os associados registrem suas viagens e oferecer uma verificação alternativa. Ela aprende que uma segurança justa considera quem carrega o peso dos controles, e que as pessoas mais afetadas devem ter um meio de levantar problemas e ser ouvidas. A Ashfield adota a opção de registro de viagens, e as reclamações dos associados sobre logins bloqueados caem no trimestre seguinte. Aisha observa que a mudança também melhorou a detecção de fraudes, porque os logins inesperados vindos do exterior agora se destacam com mais clareza.

### Exemplo resolvido

Aisha separa o legal do ético, aplica a proporcionalidade ao monitoramento da equipe, segue a divulgação coordenada para uma fraqueza encontrada e considera a justiça dos bloqueios geográficos de login.

> **Caso sintético.** Os casos são sintéticos.

### Erros e limites

Usar um acesso autorizado por curiosidade pessoal é uma quebra de confiança.

### Exercícios

- **EX028 — Teste do monitoramento.** Qual é o teste ético central do monitoramento? *Rubrica:* 3 = proporcionalidade;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX029 — Abordagem de divulgação.** Como a fraqueza encontrada deve ser tratada? *Rubrica:* 3 = comunicada em particular pelo contato publicado;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX030 — Grupo bloqueado.** Quem é afetado injustamente pelos bloqueios de logins do exterior? *Rubrica:* 3 = os associados no exterior;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Aisha Rahimi, o Dr. Neil Carrow, a Pennick University, a Ashfield Credit Union e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Aproximadamente 35.000 associados.

**EX002.** A gestão de mudanças, um projeto em grupo, um estágio, métodos de pesquisa e um trabalho de conclusão.

**EX003.** Registrar uma ideia de segurança por semana e sua aplicação à Ashfield.

**EX004.** A garantia de acesso e uso oportunos e confiáveis da informação.

**EX005.** A integridade.

**EX006.** A responsabilização.

**EX007.** Uma agência de informações de crédito.

**EX008.** As pastas compartilhadas.

**EX009.** Onde gastar o esforço de segurança limitado.

**EX010.** Uma aplicação antiga um dia precisou disso.

**EX011.** Os funcionários adiam as reinicializações.

**EX012.** Por anexos de e-mail.

**EX013.** Uma regra que permite acesso de área de trabalho remota de qualquer lugar.

**EX014.** Os dados depois que chegam a um servidor comprometido.

**EX015.** Ela é separada das redes da equipe.

**EX016.** As contas sem login há noventa dias.

**EX017.** As registra separadamente, em vez de travar.

**EX018.** Ela aponta logins que ninguém está vigiando.

**EX019.** 112 de 140 funcionários, oitenta por cento.

**EX020.** Quinze dias.

**EX021.** Usando os incidentes por cem funcionários.

**EX022.** Qual é o problema, por que ele importa, o que fazer e por quem.

**EX023.** Que ex-funcionários ainda poderiam acessar os registros dos associados.

**EX024.** Porque as normas mudam de uma edição para outra.

**EX025.** A legislação de proteção de dados.

**EX026.** Acordos assinados que definam o escopo e o período.

**EX027.** Um direito da Ashfield de verificar a segurança do fornecedor.

**EX028.** A proporcionalidade.

**EX029.** Comunicá-la em particular pelo contato de segurança da organização.

**EX030.** Os associados que estão viajando ou morando fora do país.

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
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.
