# Segurança da Informação: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 094, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 40 já estão escritos em português, com os exercícios EX001–EX060 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 21–40 (EX061–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

Capítulos 21–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

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

<a id="ch-11"></a>

## Capítulo 11 — Fundamentos da governança de segurança

### Objetivos de aprendizagem

Você vai (1) explicar o que é a governança de segurança; (2) descrever como os conselhos supervisionam a segurança; (3) relacionar a governança aos frameworks.

### 11.1 O que significa governança

No segundo ano, Aisha estuda a governança de segurança: como uma organização dirige e supervisiona sua segurança. A governança responde quem decide quanto risco é aceitável, quem presta contas e como os líderes sabem se a segurança está funcionando. O Dr. Carrow distingue a governança da gestão. O conselho define a direção e faz perguntas; os gerentes projetam e operam os controles. Aisha observa que, na Ashfield, o conselho aprova o apetite a risco e recebe relatórios trimestrais de segurança, enquanto o gerente de TI opera os controles do dia a dia e relata o progresso para cima. Ela desenha as duas coisas.

### 11.2 O papel do conselho

O conselho da Ashfield inclui voluntários eleitos pelos associados, poucos dos quais têm formação técnica. Aisha pondera do que eles precisam: um quadro claro dos principais riscos, se os controles estão funcionando e que decisões exigem a aprovação deles. Ela revisa um relatório sintético ao conselho cheio de contagens técnicas e sugere substituí-lo por cinco declarações de risco, cada uma com uma tendência e um responsável. O Dr. Carrow observa que uma boa governança depende de informações que os líderes consigam entender e usar para agir, e não do volume. O presidente do conselho recebe bem a mudança.

### 11.3 Frameworks

Aisha estuda o NIST Cybersecurity Framework 2.0, que acrescentou uma função Governar às funções Identificar, Proteger, Detectar, Responder e Recuperar. A função Governar abrange o contexto organizacional, a estratégia de gestão de riscos, os papéis, a política e a supervisão. Ela mapeia os arranjos atuais da Ashfield para esses resultados e descobre que os papéis e a política existem, mas que a gestão de riscos da cadeia de suprimentos é fraca. O Dr. Carrow explica que os frameworks ajudam as organizações a ver as lacunas de forma sistemática, mas que descrevem resultados, em vez de prescrever métodos exatos. Ela apresenta o mapeamento como uma tabela com uma linha por resultado e uma situação simples para cada um.

### 11.4 Apetite a risco

Uma declaração de apetite a risco diz quanto risco uma organização vai aceitar na busca dos seus objetivos. O conselho da Ashfield declara que aceitará um risco baixo para a confidencialidade dos dados dos associados, mas um risco moderado de breves interrupções do serviço fora do horário comercial. Aisha observa que isso orienta as decisões: gastar para evitar a exposição de dados se justifica mais facilmente do que gastar para eliminar breves interrupções noturnas. Ela aprende que as declarações de apetite transformam valores vagos em orientações práticas que os gerentes podem aplicar. Aisha usa a declaração para explicar duas decisões de gasto passadas ao seu grupo de seminário.

### Exemplo resolvido

Aisha separa a governança da gestão, simplifica o relatório ao conselho em cinco declarações de risco, mapeia a Ashfield para os resultados da função Governar do CSF 2.0 e aplica o apetite a risco aos gastos.

> **Caso sintético.** Os arranjos do conselho são sintéticos.

### Erros e limites

Os relatórios ao conselho cheios de contagens técnicas raramente apoiam as decisões.

### Exercícios

- **EX031 — O que o conselho aprova.** O que o conselho da Ashfield aprova? *Rubrica:* 3 = o apetite a risco;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX032 — Lacuna em Governar.** Que resultado da função Governar é fraco na Ashfield? *Rubrica:* 3 = a gestão de riscos da cadeia de suprimentos;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX033 — Efeito do apetite.** Que gasto se justifica mais facilmente? *Rubrica:* 3 = evitar a exposição de dados;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Papéis e responsabilização

### Objetivos de aprendizagem

Você vai (1) definir os principais papéis de segurança; (2) atribuir a responsabilização pelas informações e pelos controles; (3) segregar funções para reduzir fraudes e erros.

### 12.1 Papéis principais

Aisha lista os papéis de segurança na Ashfield. O conselho tem a responsabilização final. O diretor executivo garante os recursos. O gerente de TI lidera as operações de segurança, já que a Ashfield é pequena demais para ter um responsável dedicado à segurança. Os donos da informação, como o chefe de crédito, decidem como suas informações são protegidas. Todos os funcionários seguem as políticas e comunicam incidentes. O Dr. Carrow observa que as organizações pequenas muitas vezes acumulam papéis, o que é aceitável se as responsabilidades estiverem escritas e os conflitos forem administrados abertamente. Aisha escreve as principais atribuições de cada papel numa única frase para o manual dos funcionários.

### 12.2 Responsabilização

Responsabilização significa que uma pessoa nomeada responde por um resultado. Aisha descobre que vários controles da Ashfield não têm um dono nomeado: a revisão do firewall, as verificações de segurança dos fornecedores e os testes de backup. Cada um era tido como trabalho de outra pessoa. Ela redige uma tabela de responsabilidades listando cada controle, seu dono e a frequência com que é executado. O diretor executivo a aprova. Ela aprende que os controles sem dono tendem a parar sem que ninguém perceba, e é por isso que nomear os donos importa. Em um mês, os três controles foram executados pelo menos uma vez sob seus novos donos.

### 12.3 Segregação de funções

A segregação de funções divide as tarefas sensíveis para que nenhuma pessoa sozinha possa concluí-las. Na Ashfield, uma pessoa lança um pagamento e outra o aprova. Aisha descobre que o gerente de TI pode tanto criar contas de usuário quanto aprovar seus acessos, de modo que uma conta não autorizada poderia ser criada sem que ninguém mais soubesse. Ela recomenda que as aprovações de acesso venham dos donos da informação. O Dr. Carrow liga isso ao princípio da separação de privilégios de Saltzer e Schroeder. O chefe de crédito e o chefe de finanças concordam em aprovar os acessos das suas próprias equipes.

### 12.4 Limites das organizações pequenas

A segregação estrita é difícil em equipes pequenas. A Ashfield tem apenas dois funcionários de TI, então, quando um está de férias, o outro precisa fazer tudo. Aisha sugere controles compensatórios: registrar em log todas as ações de administrador e fazer o chefe de operações revisar o log semanalmente. Ela aprende que, quando a segregação é impossível, a detecção e a revisão podem substituí-la em parte, e que documentar esse meio-termo mostra que ela foi uma decisão deliberada, e não um descuido. O chefe de operações faz a primeira revisão semanal com Aisha observando e encontra todas as ações registradas explicadas por um chamado.

### Exemplo resolvido

Aisha lista os papéis, nomeia donos para os controles sem dono, descobre que uma mesma pessoa cria e aprova contas e propõe o registro em log e a revisão onde a segregação é impossível.

> **Caso sintético.** Os papéis são sintéticos.

### Erros e limites

Os controles que ninguém possui tendem a parar sem que ninguém perceba.

### Exercícios

- **EX034 — Controles sem dono.** Cite um controle que não tinha dono. *Rubrica:* 3 = a revisão do firewall;; 2 = um;; 1 = nada;; 0 = nenhuma.

- **EX035 — Conflito de acesso.** Que conflito o gerente de TI tem? *Rubrica:* 3 = cria e aprova contas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX036 — Controle compensatório.** O que compensa a segregação limitada? *Rubrica:* 3 = registro das ações de administrador com revisão semanal;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Políticas e normas

### Objetivos de aprendizagem

Você vai (1) distinguir políticas, normas e procedimentos; (2) escrever uma breve política de segurança; (3) relacionar a política da organização às normas internacionais.

### 13.1 Tipos de documento

Aisha aprende a distinguir os tipos de documento. Uma política declara, em alto nível, o que a organização pretende e exige, como em todo acesso aos dados dos associados precisa ser autorizado. Uma norma interna estabelece requisitos obrigatórios específicos, como em as senhas devem ter pelo menos catorze caracteres. Um procedimento descreve passo a passo como fazer algo. O Dr. Carrow explica que misturar esses tipos produz documentos detalhados demais para serem aprovados e vagos demais para serem seguidos, um problema comum nas organizações pequenas. Ela classifica os documentos da Ashfield nos três tipos.

### 13.2 Escrevendo uma política

Aisha redige uma política de controle de acesso para a Ashfield. Ela declara o propósito, o escopo, os princípios do menor privilégio e da necessidade de conhecer, os papéis responsáveis e como a conformidade é verificada. Ela a mantém em uma página para que os funcionários a leiam. O Dr. Carrow a revisa e pede que ela remova o detalhe técnico sobre o comprimento das senhas, que pertence a uma norma interna que pode ser atualizada sem a aprovação do conselho. A política final é curta e clara. O conselho aprova a política na sua reunião seguinte, sem alterações.

### 13.3 Normas internacionais

Aisha estuda como as organizações usam as normas ISO/IEC. A ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) estabelece os requisitos de um sistema de gestão da segurança da informação, inclusive que a alta direção estabeleça uma política de segurança da informação. A ISO/IEC 27002:2022 dá orientações sobre os controles, inclusive as políticas específicas por tema, como o controle de acesso. A ISO/IEC 27000:2026 oferece a visão geral da família. Ela aprende que a Ashfield não precisa buscar a certificação para se beneficiar do uso dessas normas como orientação. Aisha prepara uma breve tabela mostrando que documentos da Ashfield correspondem a cada um dos principais temas de controle da ISO/IEC 27002 e anota onde a Ashfield ainda não tem nada, como a segurança de fornecedores.

### 13.4 Mantendo as políticas vivas

As políticas ficam desatualizadas. Aisha descobre que a política de uso aceitável da Ashfield se refere a aparelhos de fax e não menciona o armazenamento em nuvem. Ela recomenda uma revisão anual com donos nomeados e um registro de alterações. Ela também sugere um breve questionário no treinamento anual para conferir se os funcionários entendem os requisitos principais. Ela aprende que uma política que ninguém lê nem atualiza oferece pouca proteção, por mais bem escrita que tenha sido originalmente. O responsável pela conformidade assume o calendário de revisões e acrescenta a data de revisão de cada política à agenda do conselho.

### Exemplo resolvido

Aisha distingue política, norma interna e procedimento, escreve uma política de acesso de uma página, a relaciona com a ISO/IEC 27001 e a 27002 e recomenda uma revisão anual.

> **Caso sintético.** As políticas são sintéticas; as normas são parafraseadas.

### Erros e limites

Colocar detalhes técnicos nas políticas obriga o conselho a aprovar mudanças rotineiras.

### Exercícios

- **EX037 — Exemplo de norma interna.** Qual é um exemplo de norma interna? *Rubrica:* 3 = senhas com pelo menos catorze caracteres;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX038 — Detalhe removido.** Que detalhe é removido da política? *Rubrica:* 3 = o comprimento das senhas;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX039 — Política desatualizada.** O que a política de uso aceitável omitia? *Rubrica:* 3 = o armazenamento em nuvem;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Avaliação de riscos

### Objetivos de aprendizagem

Você vai (1) identificar ameaças e vulnerabilidades; (2) estimar a probabilidade e o impacto; (3) produzir um registro de riscos priorizado.

### 14.1 Componentes do risco

Aisha aprende que o risco combina a probabilidade de um evento danoso com o seu impacto. A NIST SP 800-30 Revisão 1 descreve a avaliação de riscos como a identificação das fontes e dos eventos de ameaça, das vulnerabilidades, da probabilidade e do impacto. Ela identifica ameaças à Ashfield, como criminosos que enviam pedidos de pagamento falsos, e vulnerabilidades, como funcionários que não conseguem verificar os pedidos com facilidade. O Dr. Carrow explica que o risco só existe quando uma ameaça consegue explorar uma vulnerabilidade para causar dano a algo de valor. Ela escreve um exemplo de ameaça e de vulnerabilidade para cada um dos principais sistemas da Ashfield.

### 14.2 Estimando

Aisha usa uma escala simples de baixo, médio e alto para a probabilidade e o impacto. Os pedidos de pagamento falsos são prováveis, porque os fraudadores miram as pequenas organizações financeiras, e o impacto é alto, porque se poderia perder dinheiro. Um incêndio na sede é improvável, mas de alto impacto. Ela registra o raciocínio de cada classificação para que outras pessoas possam contestá-lo. Ela aprende que as classificações são julgamentos, e que escrever o raciocínio as torna revisáveis. Seu grupo de seminário contesta duas classificações, e ela muda uma delas depois de ouvir o raciocínio dos colegas.

### 14.3 O registro

Aisha monta para a Ashfield um registro de riscos com dez entradas, cada uma com descrição, dono, probabilidade, impacto, controles atuais e ações planejadas. Ela o ordena pela classificação combinada. Os pedidos de pagamento falsos, o ransomware e o uso indevido dos dados dos associados pela equipe ficam no topo. O gerente de TI e o diretor executivo revisam o registro e definem os donos. O Dr. Carrow observa que um registro só é útil se os donos agirem e se ele for atualizado quando as circunstâncias mudarem. O registro é guardado numa pasta compartilhada, e o gerente de TI acrescenta uma revisão dele a cada relatório trimestral ao conselho.

### 14.4 Tratando os riscos

Para cada risco, a Ashfield escolhe um tratamento: reduzi-lo com controles, transferi-lo por meio de seguros ou contratos, evitá-lo interrompendo uma atividade ou aceitá-lo dentro do apetite. Aisha recomenda reduzir o risco de pagamentos falsos exigindo a verificação por retorno de ligação para números conhecidos. Ela observa que o seguro cibernético transfere parte da perda financeira, mas não o dano à reputação. Ela aprende que as escolhas de tratamento devem ser registradas com seus motivos e aprovadas pelo dono do risco. O diretor executivo aprova a regra do retorno de ligação, e a equipe de finanças recebe uma lista impressa dos números de telefone verificados dos fornecedores.

### Exemplo resolvido

Aisha identifica ameaças e vulnerabilidades, classifica a probabilidade e o impacto com seus motivos, monta um registro de dez entradas e escolhe tratamentos, entre eles a verificação por retorno de ligação.

> **Caso sintético.** O registro é sintético.

### Erros e limites

O seguro transfere parte da perda financeira, mas não o dano à reputação.

### Exercícios

- **EX040 — Fonte da avaliação.** Que publicação orienta a avaliação de riscos? *Rubrica:* 3 = NIST SP 800-30 Revisão 1;; 2 = correto;; 1 = outra;; 0 = nenhuma.

- **EX041 — Principais riscos.** Cite um dos três principais riscos. *Rubrica:* 3 = pedidos de pagamento falsos;; 2 = um;; 1 = nada;; 0 = nenhuma.

- **EX042 — Tratamento dos pagamentos.** Como o risco de pagamentos falsos é reduzido? *Rubrica:* 3 = verificação por retorno de ligação para números conhecidos;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Gestão de ativos

### Objetivos de aprendizagem

Você vai (1) montar um inventário de ativos de informação; (2) classificar os ativos pela sensibilidade; (3) manter o inventário atualizado.

### 15.1 Montando um inventário

Aisha ajuda a Ashfield a montar um inventário de ativos de informação: hardware, software, repositórios de dados e serviços. Ela parte dos registros de compras e da planilha do gerente de TI e depois percorre cada agência. Ela encontra, num armário de uma agência, um dispositivo de armazenamento em rede esquecido, com documentos digitalizados antigos. O Dr. Carrow observa que os inventários muitas vezes deixam passar dispositivos assim, e que percorrer fisicamente os locais ainda encontra coisas que os registros não mostram, sobretudo nas organizações pequenas. Seu inventário final lista o hardware, o software, os repositórios de dados e os serviços externos, com uma linha por ativo e sua localização.

### 15.2 Classificação

Aisha propõe um esquema de classificação simples: público, interno, confidencial e restrito. Os documentos de identidade dos associados e os dados de cartões de pagamento são restritos; os registros de empréstimos são confidenciais; os boletins para os funcionários são internos; o horário de funcionamento das agências é público. Cada classe tem regras de tratamento, como a cifração dos dados restritos nos notebooks. Ela mantém o esquema em quatro níveis para que os funcionários consigam lembrá-lo. O Dr. Carrow observa que os esquemas complexos muitas vezes são ignorados na prática. Ela imprime um guia de uma página com exemplos de cada classe e as regras de tratamento que se aplicam.

### 15.3 Donos e tratamento

Cada ativo do inventário recebe um dono e uma classificação. O dispositivo de armazenamento esquecido é atribuído ao chefe de operações, que decide que os documentos devem ser transferidos para o sistema central e o dispositivo, apagado com segurança. Aisha registra a decisão. Ela aprende que o inventário, a responsabilidade e a classificação, juntos, permitem aplicar os controles certos, porque ninguém consegue proteger um ativo adequadamente sem saber o que ele contém. O apagamento é feito por um fornecedor certificado, que entrega um certificado para o registro.

### 15.4 Mantendo-o atualizado

Aisha recomenda que as novas compras sejam acrescentadas ao inventário antes do uso e que os descartes sejam registrados com evidências da destruição dos dados. Ela sugere uma conferência semestral comparando o inventário com os dispositivos vistos na rede. Ela aprende que um inventário se deteriora rapidamente sem atualizações de rotina, e que ligá-lo aos processos de compra e de descarte o mantém preciso com pouco esforço extra. O gerente de TI concorda em acrescentar uma etapa de inventário ao formulário de compras, para que nada novo chegue à rede sem antes ser registrado.

### Exemplo resolvido

Aisha monta um inventário que encontra um dispositivo de armazenamento esquecido, propõe quatro níveis de classificação, atribui donos e liga o inventário às compras e aos descartes.

> **Caso sintético.** Os ativos são sintéticos.

### Erros e limites

Os esquemas de classificação complexos muitas vezes são ignorados.

### Exercícios

- **EX043 — Dispositivo esquecido.** Que ativo esquecido Aisha encontra? *Rubrica:* 3 = um dispositivo de armazenamento em rede num armário;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX044 — Classe restrita.** Que dados são restritos? *Rubrica:* 3 = documentos de identidade e dados de cartões de pagamento;; 2 = correto;; 1 = outros;; 0 = nenhuma.

- **EX045 — Manutenção do inventário.** Como o inventário é mantido atualizado? *Rubrica:* 3 = ligação às compras e aos descartes, conferência semestral;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Controle de acesso

### Objetivos de aprendizagem

Você vai (1) aplicar o menor privilégio e a necessidade de conhecer; (2) projetar o acesso baseado em papéis; (3) gerenciar admissões, mudanças de função e desligamentos.

### 16.1 Princípios

Aisha aprende dois princípios do controle de acesso. O menor privilégio significa que cada pessoa ou programa tem apenas o acesso necessário para sua tarefa. A necessidade de conhecer significa que o acesso à informação fica limitado a quem precisa dela para o seu trabalho. Saltzer e Schroeder incluíram o menor privilégio entre seus princípios de projeto de 1975. Na Ashfield, os caixas precisam ver os saldos dos associados, mas não aprovar empréstimos; os agentes de crédito precisam dos registros de empréstimos, mas não dos lançamentos contábeis. Ela escreve um breve exemplo para cada papel, mostrando o que ele pode e o que não pode ver no sistema central.

### 16.2 Acesso baseado em papéis

Aisha projeta papéis para a Ashfield: caixa, agente de crédito, finanças e TI. Cada papel tem um conjunto definido de permissões nas aplicações. Os novos funcionários recebem as permissões do seu papel, em vez de copiar as de um colega, o que muitas vezes traz direitos extras. Ela documenta as permissões de cada papel numa tabela aprovada pelos donos da informação. O Dr. Carrow observa que os papéis tornam o acesso mais fácil de revisar, porque os revisores podem comparar as pessoas com seu papel, em vez de julgar cada permissão individualmente. Os donos da informação assinam a tabela, e a TI a usa para cada nova conta.

### 16.3 Admissões, mudanças de função e desligamentos

O acesso muda quando as pessoas entram, mudam de função ou saem. Aisha mapeia o processo da Ashfield. As admissões são configuradas pela TI depois de um pedido dos recursos humanos. Quem muda de função muitas vezes mantém o acesso antigo, porque ninguém o remove. As contas de quem sai são desativadas quando a TI é avisada, o que às vezes acontece dias depois. Ela recomenda que os recursos humanos disparem os três eventos automaticamente e que o acesso antigo de quem muda de função seja removido por padrão. Os recursos humanos concordam em enviar um aviso à TI no mesmo dia para cada evento. Aisha redige o modelo do aviso.

### 16.4 Acesso privilegiado

As contas de administrador podem alterar os sistemas e acessar todos os dados. Aisha recomenda contas de administrador separadas, usadas apenas para a administração, protegidas por autenticação multifator e registradas em log. O trabalho diário usa contas normais. Ela descobre que uma única conta de administrador compartilhada é usada tanto pelos funcionários de TI quanto por um fornecedor. Ela recomenda contas individuais, para que as ações possam ser rastreadas. O Dr. Carrow observa que as contas privilegiadas são o principal alvo dos atacantes depois da entrada inicial. O fornecedor recebe sua própria conta nomeada, que só é habilitada quando ele tem um pedido de suporte aprovado em aberto.

### Exemplo resolvido

Aisha aplica o menor privilégio e a necessidade de conhecer, projeta quatro papéis, mapeia as lacunas de admissão, mudança de função e desligamento e separa as contas privilegiadas.

> **Caso sintético.** Os papéis são sintéticos.

### Erros e limites

Copiar o acesso de um colega muitas vezes concede direitos desnecessários.

### Exercícios

- **EX046 — Acesso dos caixas.** De que os caixas precisam? *Rubrica:* 3 = ver os saldos, não aprovar empréstimos;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX047 — Problema da mudança de função.** O que acontece com o acesso antigo de quem muda de função? *Rubrica:* 3 = muitas vezes é mantido;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX048 — Administrador compartilhado.** Quem compartilha a conta de administrador? *Rubrica:* 3 = os funcionários de TI e um fornecedor;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Autenticação

### Objetivos de aprendizagem

Você vai (1) comparar os fatores de autenticação; (2) explicar a autenticação multifator; (3) reconhecer os ataques à autenticação.

### 17.1 Fatores

A autenticação confirma que alguém é quem diz ser. Aisha aprende três tipos de fator: algo que você sabe, como uma senha; algo que você tem, como um celular ou uma chave física; e algo que você é, como uma impressão digital. Cada um tem fraquezas. As senhas podem ser adivinhadas ou roubadas; os celulares podem ser perdidos; as impressões digitais não podem ser trocadas se forem copiadas. O Dr. Carrow explica que combinar fatores de tipos diferentes torna os ataques muito mais difíceis. Ela lista que fatores a Ashfield já usa para os associados e para os funcionários.

### 17.2 Autenticação multifator

O internet banking da Ashfield usa senhas mais um código enviado por mensagem de texto. Aisha aprende que os códigos por mensagem de texto são melhores do que as senhas sozinhas, mas podem ser interceptados por meio da tomada do número de celular. Os códigos de aplicativo e as chaves físicas são mais fortes. Para o acesso remoto da equipe, ela recomenda códigos de aplicativo e, para os administradores de TI, chaves físicas. Ela observa que a conveniência dos associados importa, então as mudanças para eles exigem comunicação e apoio cuidadosos. Ela redige um folheto para os associados explicando por que os códigos de aplicativo são mais seguros, e a equipe de marketing concorda em incluí-lo nos extratos anuais.

### 17.3 Ataques

Aisha estuda os ataques à autenticação. O phishing engana as pessoas para que digitem suas credenciais em sites falsos. O credential stuffing testa nomes de usuário e senhas vazados de outros serviços. A adivinhação de senhas testa senhas comuns contra muitas contas. O bombardeio de notificações envia repetidos pedidos de aprovação, na esperança de que um usuário cansado aceite um deles. Ela aprende que a autenticação multifator impede muitos desses ataques, mas que métodos resistentes a phishing, como as chaves físicas, são necessários contra os atacantes mais capazes. Ela escreve um breve resumo de cada ataque para o programa de conscientização, em linguagem simples e com um exemplo de mensagem que os funcionários poderiam ver.

### 17.4 Recuperação de contas

Os atacantes muitas vezes miram a recuperação da conta, em vez do login. Se um associado consegue redefinir uma senha respondendo a perguntas fáceis de descobrir, os controles fortes de login são contornados. Aisha revisa o processo sintético de recuperação da Ashfield e descobre que a equipe das agências redefine senhas depois que os associados informam a data de nascimento e o endereço, informações muitas vezes disponíveis publicamente. Ela recomenda documentos de identidade na agência ou a verificação pelo telefone cadastrado. O Dr. Carrow observa que a recuperação costuma ser o ponto mais fraco. Os gerentes das agências concordam com a mudança depois de um breve teste.

### Exemplo resolvido

Aisha compara os tipos de fator, recomenda códigos de aplicativo e chaves físicas, estuda o phishing, o credential stuffing e o bombardeio de notificações e fortalece a fraca recuperação de senhas dos associados.

> **Caso sintético.** Os processos são sintéticos.

### Erros e limites

Os controles fortes de login são contornados se a recuperação da conta for fraca.

### Exercícios

- **EX049 — Fraqueza da impressão digital.** Qual é a fraqueza das impressões digitais? *Rubrica:* 3 = não podem ser trocadas se forem copiadas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX050 — Risco do código por mensagem.** Como os códigos por mensagem de texto podem ser roubados? *Rubrica:* 3 = tomada do número de celular;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX051 — Fraqueza da recuperação.** Que verificação fraca de recuperação as agências usavam? *Rubrica:* 3 = data de nascimento e endereço;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Revisão de acessos

### Objetivos de aprendizagem

Você vai (1) conduzir uma revisão de acessos contra registros oficiais; (2) encontrar desligados e direitos em excesso; (3) relatar e corrigir os achados da revisão.

### 18.1 O propósito das revisões

O acesso se desvia com o tempo, à medida que as pessoas mudam de função, saem e recebem direitos temporários que nunca são removidos. As revisões periódicas de acessos comparam quem tem acesso com quem deveria ter. Aisha planeja uma revisão dos acessos ao sistema bancário central da Ashfield usando duas fontes oficiais: a lista dos recursos humanos, que mostra quem trabalha lá e em que cargo, e a tabela de papéis aprovada pelos donos da informação. O Dr. Carrow enfatiza que as revisões precisam usar dados oficiais, e não a memória de um gerente. Ela agenda a revisão para a primeira semana do trimestre.

### 18.2 O laboratório de acessos

O laboratório monta uma lista sintética de 140 contas da Ashfield, com cargos, situação funcional e acessos às aplicações. Ele encontra dez contas de pessoas que já saíram, mas que continuam ativas. Entre os funcionários atuais, treze têm acessos além do seu cargo, e seis deles têm acesso de administrador que não deveriam ter. Aisha observa que os desligados são o mais urgente, porque ninguém monitora sua atividade e seus antigos colegas não perceberiam um uso indevido. Ela compartilha as três listas com o gerente de TI e com os donos da informação em até uma hora, para que cada dono possa confirmar ou rejeitar os achados da sua área.

### Laboratório — Revisando acessos sintéticos a aplicações em relação à situação no RH e ao cargo

```python
"""Review synthetic application access against HR status and role (stdlib only)."""
import random
random.seed(3)
roles = {"teller": {"core"}, "lending": {"core", "loans"}, "finance": {"core", "ledger"}, "it": {"core", "admin"}}
staff = []
for i in range(140):
    role = random.choice(["teller"] * 5 + ["lending"] * 3 + ["finance"] * 2 + ["it"])
    left = random.random() < 0.1
    apps = set(roles[role])
    if random.random() < 0.08:
        apps.add(random.choice(["loans", "ledger", "admin"]))
    staff.append((f"s{i:03d}", role, left, apps))
leavers_active = [s for s in staff if s[2]]
excess = [s for s in staff if not s[2] and s[3] - roles[s[1]]]
admin_excess = [s for s in excess if "admin" in s[3] - roles[s[1]]]
print(f"accounts {len(staff)}; leavers still active {len(leavers_active)}")
print(f"current staff with access beyond role {len(excess)}; of which admin {len(admin_excess)}")
```

Execute com `python3 lab_access.py`. Saída verificada:

```text
accounts 140; leavers still active 10
current staff with access beyond role 13; of which admin 6
```

### 18.3 Investigando os achados

Aisha confere as dez contas de desligados com o gerente de TI. A maioria pertence a funcionários que saíram durante um período movimentado, em que os formulários de desligamento atrasaram. Duas pertencem a temporários cujos contratos terminaram sem aviso à TI. Nos treze casos de excesso, os donos da informação confirmam que a maioria é resto de cargos anteriores, enquanto dois foram concedidos temporariamente para um projeto. Ela aprende que entender as causas aponta para correções de processo, e não apenas para correções de contas. Ela escreve cada causa ao lado da conta nas suas notas da revisão.

### 18.4 Corrigindo e repetindo

As dez contas de desligados são desativadas no mesmo dia. Os direitos em excesso são removidos depois da confirmação dos donos, exceto uma concessão temporária justificada, registrada com uma data de término. Aisha recomenda revisões trimestrais e o processo automatizado de desligamento proposto antes. O Dr. Carrow observa que a segunda revisão costuma encontrar muito menos problemas, o que, por si só, é evidência de que as mudanças de processo funcionaram. Ela planeja comparar os resultados depois da revisão seguinte. Ela registra cada correção com a data e a pessoa que a confirmou, para que a próxima revisão possa conferir que nada voltou desde então.

### Exemplo resolvido

Aisha revisa 140 contas sintéticas, encontra 10 desligados ativos e 13 funcionários com acesso em excesso (6 com administrador), rastreia as causas e define revisões trimestrais.

> **Caso sintético.** As contas são sintéticas; as saídas vêm de lab_access.py.

### Erros e limites

As revisões baseadas na memória dos gerentes deixam passar desligados e direitos remanescentes.

### Exercícios

- **EX052 — Desligados ativos.** Quantos desligados ainda tinham contas ativas? *Rubrica:* 3 = dez;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX053 — Acesso em excesso.** Quantos funcionários atuais tinham acessos além do seu cargo? *Rubrica:* 3 = treze;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX054 — Administrador em excesso.** Quantos deles tinham acesso de administrador? *Rubrica:* 3 = seis;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Fundamentos de criptografia

### Objetivos de aprendizagem

Você vai (1) explicar a cifração simétrica e a de chave pública; (2) descrever os hashes e as assinaturas digitais; (3) reconhecer os erros criptográficos comuns.

### 19.1 Cifração

A cifração transforma dados legíveis numa forma ilegível usando uma chave. Aisha aprende que a cifração simétrica usa uma única chave compartilhada tanto para cifrar quanto para decifrar e é rápida, por isso protege os dados armazenados e o tráfego de rede. A cifração de chave pública usa um par: uma chave pública que qualquer pessoa pode usar para cifrar e uma chave privada, que só o dono tem, para decifrar. O Dr. Carrow explica que os sites usam as duas juntas: as chaves públicas para combinar uma chave compartilhada e depois a cifração simétrica, pela velocidade. Ela experimenta as duas no laboratório.

### 19.2 Hashes

Uma função de hash produz uma impressão digital de tamanho fixo dos dados. Mudar um único bit da entrada muda a impressão digital por completo, e é impraticável encontrar outra entrada com a mesma impressão digital. Aisha usa o módulo hashlib do Python para calcular as impressões digitais SHA-256 de arquivos sintéticos e confirma que uma pequena mudança produz um resultado diferente. Ela aprende que os hashes verificam a integridade, por exemplo, conferindo que um arquivo baixado é genuíno. Ela registra as duas impressões digitais no diário para mostrar a diferença e explica a ideia ao seu grupo de seminário com um exemplo impresso.

### 19.3 Assinaturas digitais

Uma assinatura digital usa uma chave privada para assinar os dados e a chave pública correspondente para verificá-los. Qualquer pessoa pode conferir a assinatura, mas só quem tem a chave poderia tê-la produzido. Aisha aprende que as atualizações de software são assinadas para que os computadores possam rejeitar versões adulteradas. Na Ashfield, os e-mails assinados poderiam ajudar os associados a reconhecer as mensagens genuínas. O Dr. Carrow observa que as assinaturas oferecem autenticidade e integridade, mas dependem de manter as chaves privadas em segurança. Ela confere que os computadores da Ashfield verificam as atualizações assinadas antes de instalá-las.

### 19.4 Erros comuns

Aisha estuda os erros comuns: inventar algoritmos novos, usar algoritmos ultrapassados, guardar as chaves ao lado dos dados cifrados e deixar de renovar os certificados. Ela descobre que os arquivos de backup da Ashfield são cifrados, mas que a chave está guardada na mesma pasta. Ela recomenda um armazenamento separado para as chaves. Ela aprende que a maioria das falhas criptográficas vem da forma como as chaves são tratadas e os sistemas configurados, e não da quebra da matemática. O gerente de TI transfere a chave para um repositório protegido separado na mesma semana. Aisha então confirma que uma restauração de teste ainda funciona com a chave recuperada do novo local.

### Exemplo resolvido

Aisha compara a cifração simétrica e a de chave pública, calcula impressões digitais SHA-256, explica as atualizações assinadas e encontra as chaves dos backups guardadas ao lado dos backups.

> **Caso sintético.** Os exemplos são sintéticos.

### Erros e limites

Guardar as chaves ao lado dos dados cifrados anula a cifração.

### Exercícios

- **EX055 — Uso da cifração simétrica.** Por que a cifração simétrica é usada para grandes volumes de dados? *Rubrica:* 3 = ela é rápida;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX056 — Propriedade do hash.** O que acontece quando um bit da entrada muda? *Rubrica:* 3 = a impressão digital muda por completo;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX057 — Chave do backup.** Onde a chave do backup estava guardada? *Rubrica:* 3 = na mesma pasta que os backups;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Conscientização em segurança

### Objetivos de aprendizagem

Você vai (1) projetar atividades de conscientização para a equipe; (2) estimular as comunicações; (3) medir os resultados da conscientização.

### 20.1 Por que conscientização

Muitos incidentes começam com uma pessoa: clicar num link de phishing, enviar dados ao destinatário errado ou compartilhar uma senha. Aisha aprende que os programas de conscientização ajudam os funcionários a reconhecer as ameaças e a reagir a elas. A ISO/IEC 27002:2022 inclui a conscientização, a educação e o treinamento entre os seus controles de pessoas. O Dr. Carrow adverte que a conscientização não serve para culpar os funcionários, e que os sistemas devem ser projetados de modo que um único erro não cause um dano grave. Ela lê exemplos de programas de conscientização que melhoraram as comunicações sem culpar quem clicou.

### 20.2 Projetando as atividades

Aisha projeta um programa para a Ashfield: um breve curso anual, dicas mensais de dois minutos por e-mail, exercícios simulados de phishing e conversas nas agências sobre tentativas reais de fraude, com os dados pessoais removidos. Ela adapta o conteúdo aos papéis. Os caixas aprendem a identificar a engenharia social por telefone; a equipe de finanças aprende sobre os pedidos de pagamento falsos. Ela mantém as sessões curtas, porque as longas sessões anuais são logo esquecidas. Ela testa a primeira dica mensal com cinco funcionários, que dizem que ela é clara e leva menos de dois minutos para ser lida. O gerente de TI aprova o programa para o ano seguinte.

### 20.3 Estimulando as comunicações

Comunicar importa mais do que nunca clicar. Aisha recomenda um botão de comunicação no e-mail e um número de telefone simples para a equipe das agências. Toda comunicação recebe um agradecimento, mesmo que a mensagem fosse inofensiva. Quando uma caixa comunica uma ligação suspeita, o gerente de TI descobre que várias agências receberam a mesma ligação. O Dr. Carrow explica que os funcionários que temem ser culpados param de comunicar, o que elimina uma das melhores fontes de detecção da organização. O gerente de TI bloqueia o número de quem ligou e avisa todas as agências em menos de uma hora.

### 20.4 Medindo os resultados

Aisha propõe medidas: a conclusão do treinamento, a parcela de e-mails simulados de phishing comunicados e o tempo até a primeira comunicação de e-mails suspeitos reais. Ela evita usar apenas as taxas de cliques, porque elas dependem da dificuldade de cada simulação. Ela planeja acompanhar as tendências ao longo de um ano. Ela aprende que os resultados da conscientização são mais bem medidos pelo comportamento, sobretudo pelas comunicações, do que apenas pela presença. Ela monta uma planilha simples para acompanhar as três medidas mensalmente, e o gerente de TI concorda em incluir os resultados no relatório trimestral ao conselho.

### Exemplo resolvido

Aisha projeta uma conscientização por papel, com sessões curtas, torna a comunicação fácil e agradecida, usa uma ligação comunicada para detectar uma campanha mais ampla e mede o comportamento.

> **Caso sintético.** O programa é sintético.

### Erros e limites

Culpar os funcionários pelos cliques desestimula as comunicações que detectam os ataques.

### Exercícios

- **EX058 — Tema dos caixas.** O que os caixas aprendem a identificar? *Rubrica:* 3 = a engenharia social por telefone;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX059 — Valor da comunicação.** O que a comunicação de uma caixa revelou? *Rubrica:* 3 = várias agências receberam a mesma ligação;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX060 — Cautela com os cliques.** Por que evitar usar apenas as taxas de cliques? *Rubrica:* 3 = dependem da dificuldade da simulação;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060 (as de EX061–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Aisha Rahimi, o Dr. Neil Carrow, a Pennick University, a Ashfield Credit Union e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** O apetite a risco.

**EX032.** A gestão de riscos da cadeia de suprimentos.

**EX033.** Gastar para evitar a exposição dos dados dos associados.

**EX034.** A revisão do firewall.

**EX035.** Ele pode tanto criar contas quanto aprovar seus acessos.

**EX036.** O registro em log das ações de administrador com uma revisão semanal.

**EX037.** As senhas devem ter pelo menos catorze caracteres.

**EX038.** O requisito de comprimento das senhas.

**EX039.** Qualquer menção ao armazenamento em nuvem.

**EX040.** NIST SP 800-30 Revisão 1.

**EX041.** Os pedidos de pagamento falsos.

**EX042.** A verificação por retorno de ligação para números conhecidos.

**EX043.** Um dispositivo de armazenamento em rede num armário de uma agência.

**EX044.** Os documentos de identidade dos associados e os dados de cartões de pagamento.

**EX045.** Ligando-o às compras e aos descartes, com uma conferência semestral.

**EX046.** Ver os saldos dos associados, mas não aprovar empréstimos.

**EX047.** Muitas vezes ele permanece, porque ninguém o remove.

**EX048.** Os funcionários de TI e um fornecedor.

**EX049.** Elas não podem ser trocadas se forem copiadas.

**EX050.** Por meio da tomada do número de celular.

**EX051.** Os associados informarem a data de nascimento e o endereço.

**EX052.** Dez contas de desligados.

**EX053.** Treze funcionários atuais.

**EX054.** Seis tinham acesso de administrador.

**EX055.** Porque ela é rápida.

**EX056.** A impressão digital muda por completo.

**EX057.** Na mesma pasta que os backups cifrados.

**EX058.** A engenharia social por telefone.

**EX059.** Várias agências receberam a mesma ligação suspeita.

**EX060.** Elas dependem da dificuldade de cada simulação.

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
