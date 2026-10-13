# Arquitetura e Engenharia de Segurança: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 030, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 12 já estão escritos em português, com os exercícios EX001–EX040 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 9–12 (EX041–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais em atividade que migram de funções vizinhas para a prática de arquitetura de segurança.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios ordenam ameaças, rastreiam requisitos até os resultados de testes e comparam permissões com as necessidades dos papéis, sempre sobre dados sintéticos; nada toca um sistema real ou dados pessoais reais. Projetos de produção usam produtos e normas avaliados; nunca crie sua própria criptografia. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um profissional em transição de carreira numa associação de habitação: fundamentos, contexto de serviços e prática autorizada; métodos centrais, ferramentas, fluxo operacional, controles e verificação; um caso supervisionado, comunicação e ética, qualidade e solução de problemas; um laboratório supervisionado e o portfólio de prática. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Owen Hartley** | Aluno do curso profissional, ex-gerente de projetos | Inventado |
| **Ines Carvalho** | Mentora | Inventada |
| **Kwame Asante** | Chefe de TI da Thornbury | Inventado |
| **Meridian Professional Academy** | Provedora fictícia de formação | Inventada |
| **Thornbury Housing Association** | Locadora social fictícia de 4.000 moradias | Inventada |

### Fontes principais

Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Anderson, *Security Engineering* 3e (2020); Shostack, *Threat Modeling* (2014); NIST [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1) e [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5); ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem

Você vai (1) enunciar em termos práticos os objetivos centrais da segurança; (2) aplicá-los aos serviços de uma associação de habitação; (3) reconhecer os limites de um curso curto.

### 1.1 Ponto de partida

Owen Hartley é um gerente de projetos que está migrando para a arquitetura de segurança por meio de um curso profissional de seis meses na fictícia Meridian Professional Academy. Sua mentora é Ines Carvalho. Ele trabalha na fictícia Thornbury Housing Association, que administra quatro mil moradias alugadas e mantém um portal do inquilino, um sistema de reparos, um serviço de pagamento de aluguel e uma central de atendimento. Ines pede que ele descreva a segurança com suas próprias palavras. Owen chega a manter as informações dos inquilinos privadas, os registros corretos e os serviços funcionando, o que corresponde a confidencialidade, integridade e disponibilidade.

### 1.2 Aplicar os objetivos

Owen aplica os três objetivos à Thornbury. A confidencialidade importa mais para as fichas dos inquilinos, que incluem dados de benefícios sociais, necessidades de saúde e anotações de proteção (safeguarding) sobre moradores vulneráveis. A integridade importa para as contas de aluguel, porque um saldo errado poderia levar a cartas indevidas de cobrança de atrasados. A disponibilidade importa para o sistema de reparos, porque uma caldeira quebrada no inverno não pode esperar. Mapear os objetivos para serviços reais o ajuda a explicar aos colegas por que a segurança não é uma preferência da TI, e sim uma forma de proteger os inquilinos de danos concretos que eles reconheceriam de imediato.

### 1.3 Limites de um curso curto

Ines é honesta sobre o curso: seis meses farão de Owen um profissional capaz de aplicar métodos, ler evidências e trabalhar com especialistas, e não um especialista em todas as áreas. Ele vai aprender quando pedir ajuda, por exemplo em criptografia, configuração de nuvem ou questões jurídicas. Anderson (2020) enfatiza que a engenharia de segurança abrange muitas disciplinas, então saber onde termina a própria competência faz parte da prática profissional. Owen escreve uma lista curta de temas que vai encaminhar a especialistas, que ele planeja revisitar à medida que sua experiência crescer.

### Exemplo resolvido

Owen define os três objetivos de segurança em termos simples, mapeia cada um para um serviço da Thornbury e lista os temas que vai encaminhar a especialistas.

> **Caso sintético.** A Thornbury, a Meridian e todas as pessoas são sintéticas; Anderson (2020) é real.

### Erros e limites

Definições em linguagem simples simplificam. As listas de encaminhamento precisam ser revisitadas conforme as habilidades crescem.

### Exercícios

- **EX001 — A definição de Owen.** Como Owen descreveu a segurança com suas próprias palavras? *Rubrica:* 3 = manter as informações dos inquilinos privadas, os registros corretos e os serviços funcionando;; 2 = três partes;; 1 = nenhuma;; 0 = nenhuma.

- **EX002 — Exemplo de integridade.** Por que a integridade importa para as contas de aluguel? *Rubrica:* 3 = um saldo errado poderia causar cartas indevidas de cobrança;; 2 = cobrança;; 1 = nenhuma;; 0 = nenhuma.

- **EX003 — Exemplo de disponibilidade.** Que serviço mostra a importância da disponibilidade? *Rubrica:* 3 = reparos, como uma caldeira quebrada no inverno;; 2 = reparos;; 1 = portal;; 0 = nenhuma.

- **EX004 — Limite do curso.** O que o curso fará de Owen? *Rubrica:* 3 = um profissional capaz que sabe quando consultar especialistas;; 2 = profissional;; 1 = especialista;; 0 = nenhuma.

- **EX005 — Temas para especialistas.** Cite um tema que Owen vai encaminhar a especialistas. *Rubrica:* 3 = criptografia, configuração de nuvem ou questões jurídicas;; 2 = um;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Arquitetura e engenharia de segurança: contexto de serviços e partes interessadas

### Objetivos de aprendizagem

Você vai (1) mapear os serviços e as partes interessadas da Thornbury; (2) registrar suas necessidades de segurança; (3) lidar com necessidades conflitantes.

### 2.1 Serviços e responsáveis

Owen lista os principais serviços da Thornbury e seus responsáveis de negócio: o portal do inquilino, do atendimento ao cliente; os reparos, da equipe de imóveis; o aluguel, do financeiro; a central de atendimento, de operações; e a gestão de casos de inquilinos vulneráveis, da responsável por proteção (safeguarding). Cada serviço também depende da TI e de fornecedores externos. Nomear os responsáveis importa porque as decisões de arquitetura envolvem trade-offs que só o responsável de negócio pode aceitar, como um login mais lento em troca de uma proteção mais forte dos dados dos inquilinos.

### 2.2 Necessidades das partes interessadas

Owen entrevista cada responsável por vinte minutos, usando as mesmas perguntas: que dados o serviço guarda, o que mais doeria se ele falhasse ou vazasse, quem o usa e de onde, e que regras se aplicam. A responsável por proteção enfatiza que o vazamento do novo endereço de um inquilino poderia colocar em perigo alguém fugindo de violência doméstica. O financeiro se preocupa mais com fraude em pagamentos. O atendimento ao cliente quer que o portal continue fácil para os inquilinos idosos. Registrar as necessidades nas palavras dos próprios responsáveis gera confiança e mantém a arquitetura ancorada em consequências reais.

### 2.3 Necessidades conflitantes

As necessidades entram em conflito. O atendimento ao cliente quer um login simples no portal; a responsável por proteção quer proteção forte dos endereços. Owen propõe um projeto em que a maioria das funções do portal usa o login simples, enquanto visualizar ou alterar os dados de contato exige uma etapa extra de verificação. Os dois responsáveis aceitam. Ele registra o acordo e os motivos numa nota de decisão curta. Ines aponta que muitos conflitos desaparecem quando um projeto trata dados diferentes de forma diferente, em vez de aplicar o mesmo nível de proteção a tudo da mesma maneira.

### Exemplo resolvido

Owen mapeia cinco serviços para seus responsáveis, registra as necessidades em entrevistas curtas e resolve um conflito no portal protegendo mais os dados de contato.

> **Caso sintético.** Os serviços e as pessoas são sintéticos.

### Erros e limites

Entrevistas curtas deixam detalhes de fora. Os responsáveis podem não prever todas as consequências.

### Exercícios

- **EX006 — Por que nomear responsáveis.** Por que nomear os responsáveis de negócio pelos serviços? *Rubrica:* 3 = só eles podem aceitar trade-offs;; 2 = trade-offs;; 1 = nenhuma;; 0 = nenhuma.

- **EX007 — Preocupação de proteção.** O que a responsável por proteção enfatizou? *Rubrica:* 3 = um novo endereço vazado poderia pôr em perigo alguém fugindo de violência;; 2 = endereço;; 1 = nenhuma;; 0 = nenhuma.

- **EX008 — Acordo no portal.** Como o conflito do portal foi resolvido? *Rubrica:* 3 = verificação extra só para visualizar ou alterar os dados de contato;; 2 = verificação adicional;; 1 = nenhuma;; 0 = nenhuma.

- **EX009 — Dissolver o conflito.** Por que muitos conflitos desaparecem em bons projetos? *Rubrica:* 3 = dados diferentes são protegidos de forma diferente;; 2 = diferenciar;; 1 = nenhuma;; 0 = nenhuma.

- **EX010 — Método das entrevistas.** Como Owen manteve as entrevistas comparáveis? *Rubrica:* 3 = vinte minutos com as mesmas perguntas para todos os responsáveis;; 2 = mesmas perguntas;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e manuseio de evidências

### Objetivos de aprendizagem

Você vai (1) obter autorização antes do trabalho de segurança; (2) manusear evidências com cuidado; (3) proteger os dados pessoais durante as revisões.

### 3.1 Autorização primeiro

Owen quer revisar o acesso ao sistema de gestão de casos. Ines insiste em que ele obtenha primeiro uma autorização por escrito do responsável pelo sistema e do chefe de TI, Kwame Asante, dizendo o que ele pode examinar, quando e por quê. Mesmo um funcionário interno pode causar dano ou violar uma política ao examinar sistemas sem permissão, especialmente sistemas que guardam anotações de proteção. A autorização também protege Owen se mais tarde surgirem perguntas sobre por que ele acessou registros sensíveis. Ele a guarda com seus papéis de trabalho.

### 3.2 Manusear evidências

Durante a revisão, Owen exporta as listas de usuários e de papéis, em vez de navegar pelas fichas dos inquilinos. Ele registra o que exportou, quando e de qual sistema, e guarda os arquivos numa pasta restrita. Ele calcula um checksum de cada exportação para poder mostrar depois que ela não foi alterada. Se os achados dele levarem a uma ação disciplinar, as evidências precisam resistir a contestação. O manuseio cuidadoso também significa apagar as cópias quando o trabalho terminar, conforme acordado na autorização, em vez de guardá-las indefinidamente.

### 3.3 Proteger os dados pessoais

A revisão de Owen precisa dos nomes dos funcionários com acesso, mas não dos dados dos inquilinos. Quando um relatório de papéis inclui por engano nomes de inquilinos, ele para, informa o responsável pelo sistema e apaga os dados excedentes. Ele redige seus achados usando nomes de papéis e contagens, mencionando pessoas apenas quando necessário. A ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) espera que o manuseio de informações siga regras acordadas, e a legislação de proteção de dados limita o uso à finalidade acordada. Minimizar os dados pessoais numa revisão reduz o dano caso os arquivos da revisão venham a ser expostos.

### Exemplo resolvido

Owen obtém autorização por escrito, exporta as listas de papéis e calcula seus checksums, guarda-as com segurança e apaga os dados de inquilinos incluídos por engano.

> **Caso sintético.** Os sistemas e os eventos são sintéticos; a ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) é real.

### Erros e limites

As autorizações podem ser vagas. Os checksums provam a integridade, e não a completude.

### Exercícios

- **EX011 — Quem autorizou.** Quem autorizou a revisão de Owen? *Rubrica:* 3 = o responsável pelo sistema e Kwame Asante, chefe de TI;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX012 — Propósito do checksum.** Por que calcular um checksum de cada exportação? *Rubrica:* 3 = para mostrar depois que ela não foi alterada;; 2 = integridade;; 1 = sigilo;; 0 = nenhuma.

- **EX013 — Dados por engano.** O que Owen fez quando apareceram nomes de inquilinos? *Rubrica:* 3 = parou, informou o responsável e apagou os dados excedentes;; 2 = parar;; 1 = continuou;; 0 = nenhuma.

- **EX014 — Exclusão.** Quando as cópias de trabalho são apagadas? *Rubrica:* 3 = quando o trabalho termina, conforme acordado;; 2 = fim do trabalho;; 1 = nunca;; 0 = nenhuma.

- **EX015 — Exportar, não navegar.** Por que exportar as listas de papéis em vez de navegar pelos registros? *Rubrica:* 3 = para evitar ver dados de inquilinos desnecessários à revisão;; 2 = minimizar;; 1 = rapidez;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Arquitetura e engenharia de segurança: métodos centrais

### Objetivos de aprendizagem

Você vai (1) modelar os fluxos de dados de um serviço; (2) aplicar o STRIDE para encontrar ameaças; (3) ordenar as ameaças para tratamento.

### 4.1 Modelar o serviço de reparos

Owen modela o serviço de reparos: os inquilinos relatam reparos pelo portal ou pela central de atendimento; o sistema de reparos cria as ordens de serviço; as ordens vão para as empresas contratadas por um portal de fornecedores; os contratados atualizam as ordens pelo celular; os inquilinos recebem atualizações por mensagem de texto. Ele rotula os dados de cada fluxo, incluindo nomes, endereços e telefones dos inquilinos e anotações de acesso, como os códigos de cofres de chaves (key safes). Ele marca as fronteiras de confiança entre a Thornbury e os contratados e entre a Thornbury e o provedor de mensagens. O modelo leva duas horas com a equipe de imóveis e se torna a base da análise.

### 4.2 Aplicar o STRIDE

Owen aplica o STRIDE de Shostack (2014). Spoofing: um ex-funcionário de um contratado ainda poderia entrar no portal de fornecedores. Tampering: as anotações das ordens poderiam ser alteradas para esconder visitas não realizadas. Repudiation: os contratados poderiam negar ter recebido ordens se não houver registro. Information disclosure: os códigos dos cofres de chaves ficam visíveis para todos os contratados, e não só para o designado. Denial of service: o portal de fornecedores não tem contingência. Elevation of privilege: as contas dos contratados conseguem ver as ordens de outros contratados. Ele lista cada ameaça com o elemento que ela afeta.

### Laboratório — Ordenação das ameaças dos reparos por probabilidade e impacto

```python
# Rank repairs-service threats by likelihood x impact (1-3 scales, synthetic ratings).
threats = {"key safe codes visible to all contractors": (3, 3), "former contractor accounts still active": (2, 3),
           "contractors see other contractors' jobs": (3, 2), "job notes altered to hide missed visits": (2, 2),
           "no record of job receipt": (2, 1), "supplier portal outage without fallback": (1, 3)}
for i, (t, (l, imp)) in enumerate(sorted(threats.items(), key=lambda x: -x[1][0] * x[1][1]), 1):
    print(f"{i}. {t}: likelihood {l} x impact {imp} = {l * imp}")
```

Execute com `python3 lab_rank.py`. Saída verificada:

```text
1. key safe codes visible to all contractors: likelihood 3 x impact 3 = 9
2. former contractor accounts still active: likelihood 2 x impact 3 = 6
3. contractors see other contractors' jobs: likelihood 3 x impact 2 = 6
4. job notes altered to hide missed visits: likelihood 2 x impact 2 = 4
5. supplier portal outage without fallback: likelihood 1 x impact 3 = 3
6. no record of job receipt: likelihood 2 x impact 1 = 2
```

### 4.3 Ordenar

Owen classifica cada ameaça em probabilidade e impacto numa escala de um a três com a equipe de imóveis, seguindo a estrutura do NIST SP 800-30 Rev. 1, e as multiplica para obter uma ordem simples. O laboratório ordena as ameaças. A divulgação dos códigos dos cofres de chaves fica em primeiro, porque é provável e poderia permitir que alguém entrasse na casa de um inquilino vulnerável. As contas de ex-funcionários dos contratados ficam em segundo. Ele apresenta a ordenação com os motivos, observando que notas simples orientam a ordem do trabalho, mas não devem ser tratadas como medições precisas.

### Exemplo resolvido

Owen modela o serviço de reparos, encontra seis ameaças com o STRIDE e as ordena com a equipe de imóveis, colocando em primeiro a exposição dos códigos dos cofres de chaves.

> **Caso sintético.** O serviço e as classificações são sintéticos; Shostack (2014) e o SP 800-30 Rev. 1 são reais.

### Erros e limites

Notas multiplicadas sugerem uma falsa precisão. Os modelos deixam de fora canais informais, como celulares pessoais.

### Exercícios

- **EX016 — Anotação sensível.** Que dado sensível aparecia nas anotações de acesso dos reparos? *Rubrica:* 3 = códigos dos cofres de chaves;; 2 = códigos;; 1 = nenhuma;; 0 = nenhuma.

- **EX017 — Ameaça de divulgação.** Que ameaça de divulgação o STRIDE encontrou? *Rubrica:* 3 = códigos dos cofres de chaves visíveis para todos os contratados;; 2 = códigos;; 1 = nenhuma;; 0 = nenhuma.

- **EX018 — Primeiro lugar.** Que ameaça ficou em primeiro no laboratório, e com que nota? *Rubrica:* 3 = divulgação dos códigos dos cofres de chaves, 9;; 2 = códigos;; 1 = indisponibilidade do portal;; 0 = nenhuma.

- **EX019 — Cautela com as notas.** Que cautela Owen fez sobre as notas? *Rubrica:* 3 = orientam a ordem, mas não são medições precisas;; 2 = ordenação;; 1 = nenhuma;; 0 = nenhuma.

- **EX020 — Segundo lugar.** Que ameaça ficou em segundo no laboratório? *Rubrica:* 3 = contas de ex-funcionários dos contratados ainda ativas, 6;; 2 = contas antigas;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Arquitetura e engenharia de segurança: ferramentas e interpretação

### Objetivos de aprendizagem

Você vai (1) usar ferramentas simples para examinar acessos e configurações; (2) interpretar corretamente a saída das ferramentas; (3) evitar leituras equivocadas comuns.

### 5.1 Ferramentas disponíveis

Owen não precisa de ferramentas avançadas para começar. Ele usa os relatórios administrativos do provedor de identidade, a página de recomendações de segurança do provedor de nuvem, a exportação de usuários do portal de fornecedores e uma planilha. Kwame também lhe dá acesso somente de leitura ao scanner de vulnerabilidades que a Thornbury já roda todo mês contra seus serviços públicos. Ines o incentiva a aprender o que as ferramentas existentes conseguem mostrar antes de pedir novas, porque as organizações muitas vezes já possuem capacidades que ninguém tem tempo de usar bem. Ele lista cada ferramenta, seu responsável e o acesso que tem a ela.

### 5.2 Interpretar a saída

O scanner relata quarenta achados no portal do inquilino. A primeira reação de Owen é alarme, mas ele lê cada um. A maioria é informativa, como os banners de versão do servidor. Dois são classificados como altos: uma biblioteca desatualizada e uma configuração fraca de TLS num antigo subdomínio de teste que ainda aponta para um servidor ativo. Ele confirma com o desenvolvedor que o subdomínio de teste não é usado e pede que seja removido. Interpretar significa conferir o que cada achado de fato significa no contexto, em vez de contar achados ou confiar apenas nos rótulos de severidade.

### 5.3 Leituras equivocadas comuns

Owen reúne as leituras equivocadas que quase fez. Uma página de nuvem mostrando uma secure score alta não significa que os dados dos inquilinos estejam seguros; ela mede configurações contra uma lista do fornecedor. Um relatório de identidade sem logins arriscados pode refletir um recurso desligado. Um scanner sem achados num servidor pode significar que ele não conseguiu alcançá-lo. Para cada ferramenta, ele anota o que ela mede, o que ela não consegue ver e como confirmar um resultado surpreendente. Esse hábito torna seus relatórios posteriores muito mais confiáveis.

### Exemplo resolvido

Owen usa as ferramentas existentes, interpreta quarenta achados do scanner para encontrar dois problemas reais e registra as leituras equivocadas comuns de três ferramentas.

> **Caso sintético.** As ferramentas e os achados são sintéticos.

### Erros e limites

Os rótulos de severidade são genéricos. As lacunas de cobertura das ferramentas passam despercebidas com facilidade.

### Exercícios

- **EX021 — Capacidade existente.** Por que aprender primeiro as ferramentas existentes? *Rubrica:* 3 = as organizações muitas vezes possuem capacidades não usadas;; 2 = já possuídas;; 1 = nenhuma;; 0 = nenhuma.

- **EX022 — Achados reais.** Que dois achados do scanner importavam? *Rubrica:* 3 = uma biblioteca desatualizada e TLS fraco num antigo subdomínio de teste ativo;; 2 = dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX023 — Secure score.** O que uma secure score alta na nuvem não significa? *Rubrica:* 3 = que os dados dos inquilinos estejam seguros;; 2 = não é segurança;; 1 = seguro;; 0 = nenhuma.

- **EX024 — Varredura vazia.** O que pode significar nenhum achado num servidor? *Rubrica:* 3 = o scanner não conseguiu alcançá-lo;; 2 = alcançabilidade;; 1 = seguro;; 0 = nenhuma.

- **EX025 — Anotações das ferramentas.** Que três coisas Owen registra para cada ferramenta? *Rubrica:* 3 = o que mede, o que não consegue ver, como confirmar surpresas;; 2 = duas;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Arquitetura e engenharia de segurança: fluxo operacional

### Objetivos de aprendizagem

Você vai (1) encaixar verificações de segurança nos fluxos de trabalho existentes; (2) desenhar um fluxo de acesso para contratados; (3) reduzir o esforço manual.

### 6.1 Trabalhar com os processos existentes

A Thornbury já tem processos para cadastrar contratados, abrir mudanças de TI e tratar reclamações. Owen acrescenta etapas de segurança a esses processos, em vez de criar processos separados. O cadastro de contratados ganha uma etapa para acordar as regras de manuseio de dados e as contas nominais. As mudanças de TI ganham três perguntas de segurança. As reclamações que mencionam o manuseio de dados são copiadas ao encarregado de proteção de dados. Ines observa que as etapas de segurança entrelaçadas em fluxos familiares são cumpridas com muito mais confiabilidade do que procedimentos de segurança separados, que as pessoas precisam lembrar de seguir. Owen acorda cada mudança primeiro com o responsável pelo processo.

### 6.2 Fluxo de acesso dos contratados

Para a ameaça dos ex-funcionários dos contratados, Owen desenha um fluxo. Os contratados solicitam contas para funcionários nominais pelo portal de fornecedores; a equipe de imóveis aprova; as contas expiram após noventa dias, a menos que sejam renovadas; e os contratados precisam comunicar os desligamentos em até dois dias úteis, o que fica escrito nos contratos. Todo mês, a equipe de imóveis recebe uma lista das contas sem uso há trinta dias e confirma se deve mantê-las. O fluxo acaba com os logins compartilhados e dá à Thornbury um registro claro de quem pode ver as ordens de serviço dos inquilinos.

### 6.3 Reduzir o esforço manual

Owen pergunta ao fornecedor do portal de fornecedores se os relatórios de expiração e de contas sem uso podem ser automatizados. Podem, por meio de configurações existentes. Ele também providencia que os códigos dos cofres de chaves apareçam apenas na ordem do contratado designado e apenas no dia da visita. A verificação mensal da equipe de imóveis agora leva quinze minutos. Ele mede a mudança: as contas ativas de contratados caem de duzentas e dez para cento e trinta e cinco depois da primeira revisão. Menos trabalho manual torna o fluxo sustentável para uma equipe ocupada.

### Exemplo resolvido

Owen acrescenta etapas de segurança aos processos existentes, desenha um fluxo de acesso com expiração para os contratados e automatiza relatórios, reduzindo as contas de 210 para 135.

> **Caso sintético.** Os processos e os números são sintéticos.

### Erros e limites

As cláusulas contratuais dependem de cobrança. A expiração automática pode bloquear funcionários ativos.

### Exercícios

- **EX026 — Etapas entrelaçadas.** Por que acrescentar etapas aos processos existentes? *Rubrica:* 3 = são cumpridas com mais confiabilidade do que procedimentos separados;; 2 = confiabilidade;; 1 = nenhuma;; 0 = nenhuma.

- **EX027 — Prazo de expiração.** Quando as contas dos contratados expiram? *Rubrica:* 3 = após noventa dias, a menos que sejam renovadas;; 2 = noventa dias;; 1 = nunca;; 0 = nenhuma.

- **EX028 — Mudança nos códigos.** Como os códigos dos cofres de chaves foram restringidos? *Rubrica:* 3 = só para o contratado designado e no dia da visita;; 2 = designado;; 1 = nenhuma;; 0 = nenhuma.

- **EX029 — Redução de contas.** Como mudaram as contas ativas de contratados? *Rubrica:* 3 = de 210 para 135;; 2 = caíram;; 1 = nenhuma;; 0 = nenhuma.

- **EX030 — Comunicação de desligamentos.** Em que prazo os contratados precisam comunicar desligamentos? *Rubrica:* 3 = em até dois dias úteis, por contrato;; 2 = dois dias;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Arquitetura e engenharia de segurança: controles e verificação

### Objetivos de aprendizagem

Você vai (1) selecionar controles para as principais ameaças; (2) escrever requisitos verificáveis; (3) conferir se os controles funcionam.

### 7.1 Selecionar os controles

Para as principais ameaças dos reparos, Owen seleciona controles com a equipe de imóveis e a TI. Exposição dos códigos dos cofres de chaves: mostrar os códigos apenas ao contratado designado no dia da visita, como feito no capítulo 6, e registrar cada visualização. Contas de ex-funcionários dos contratados: o fluxo de acesso com expiração. Visibilidade entre contratados: restringir cada conta de contratado às suas próprias ordens. Anotações alteradas: manter um histórico de mudanças que os contratados não conseguem editar. Ele confere as escolhas contra as famílias de controles do NIST SP 800-53 Rev. 5, o que confirma que cobriu controle de acesso, auditoria e responsabilização.

### 7.2 Requisitos verificáveis

Owen transforma os controles em enunciados que podem ser conferidos: uma conta de contratado só consegue ver as ordens atribuídas à sua empresa; um código de cofre de chaves só fica visível na data da visita; toda visualização de código é registrada com usuário e horário; as edições das anotações das ordens preservam a versão anterior. Requisitos vagos, como "o acesso dos contratados deve ser seguro", não podem ser testados. Escrevê-los com precisão também ajuda o fornecedor, que pode confirmar quais deles o produto suporta e fazer orçamento dos que exigem configuração.

### Laboratório — Rastreamento dos requisitos até os resultados da verificação

```python
# Trace requirements to verification results, before and after the vendor fix (synthetic).
reqs = {"R1 contractor sees own company's jobs only": "pass",
        "R2 key safe code visible only on visit date": "fail (visible until end of next day)",
        "R3 every code view logged with user and time": "pass",
        "R4 job note edits keep previous version": "pass"}
for r, res in reqs.items(): print(f"{r}: {res}")
print(f"round 1: {sum(v == 'pass' for v in reqs.values())}/{len(reqs)} passed")
reqs["R2 key safe code visible only on visit date"] = "pass (after vendor cutoff change)"
print(f"round 2: {sum(v.startswith('pass') for v in reqs.values())}/{len(reqs)} passed")
```

Execute com `python3 lab_trace.py`. Saída verificada:

```text
R1 contractor sees own company's jobs only: pass
R2 key safe code visible only on visit date: fail (visible until end of next day)
R3 every code view logged with user and time: pass
R4 job note edits keep previous version: pass
round 1: 3/4 passed
round 2: 4/4 passed
```

### 7.3 Conferir se funcionam

Owen e um testador usam duas contas de contratado de teste para conferir cada requisito. O laboratório rastreia cada requisito até o resultado do teste. Três passam. O teste de visibilidade do código falha: os códigos continuam visíveis por um dia depois da visita, porque o fornecedor usa o fim do dia seguinte como corte. O fornecedor muda a configuração e o novo teste passa. Owen registra os resultados numa tabela ligada às ameaças, para que qualquer pessoa veja quais ameaças são tratadas por controles verificados e quais ainda dependem de promessas não verificadas.

### Exemplo resolvido

Owen seleciona controles para quatro ameaças, escreve quatro requisitos testáveis e os verifica, pegando um erro no corte de visibilidade dos códigos.

> **Caso sintético.** Os controles e os testes são sintéticos; o SP 800-53 Rev. 5 é real.

### Erros e limites

As contas de teste podem não refletir o volume real de dados. As configurações do fornecedor podem voltar ao padrão após atualizações.

### Exercícios

- **EX031 — Controle contra adulteração.** Que controle trata as anotações alteradas? *Rubrica:* 3 = um histórico de mudanças que os contratados não conseguem editar;; 2 = histórico;; 1 = nenhuma;; 0 = nenhuma.

- **EX032 — Requisito vago.** Por que "o acesso dos contratados deve ser seguro" é um requisito ruim? *Rubrica:* 3 = não pode ser testado;; 2 = não testável;; 1 = nenhuma;; 0 = nenhuma.

- **EX033 — Cobertura no laboratório.** O que a primeira rodada de testes mostrou no laboratório? *Rubrica:* 3 = 3 de 4 requisitos passaram; a visibilidade do código falhou;; 2 = 3 de 4;; 1 = nenhuma;; 0 = nenhuma.

- **EX034 — Causa da falha.** Por que o teste de visibilidade do código falhou? *Rubrica:* 3 = o fornecedor cortava no fim do dia seguinte;; 2 = corte;; 1 = nenhuma;; 0 = nenhuma.

- **EX035 — Resultado do novo teste.** O que a segunda rodada mostrou no laboratório? *Rubrica:* 3 = os 4 requisitos passaram depois da correção do fornecedor;; 2 = 4 de 4;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura e engenharia de segurança: análise de caso supervisionada

### Objetivos de aprendizagem

Você vai (1) analisar um incidente sob supervisão; (2) separar causas de sintomas; (3) recomendar mudanças de projeto.

### 8.1 O caso

Ines dá a Owen um caso supervisionado do histórico da Thornbury, anonimizado. Um atendente da central alterou os dados bancários de um inquilino para reembolsos de aluguel depois que quem ligou passou nas perguntas básicas de identificação. O reembolso foi para a conta de um criminoso. O inquilino percebeu semanas depois. Owen lê as anotações da ligação, os logs do sistema e o relatório da investigação. Ele monta primeiro uma linha do tempo, depois lista os sintomas, como o reembolso extraviado, e os separa das causas. Ines revisa cada etapa e questiona as suposições iniciais dele sobre de quem foi a culpa.

### 8.2 Causas

Owen identifica causas em vários níveis. As perguntas de identificação usavam informações que criminosos conseguem encontrar, como a data de nascimento e o endereço. O sistema permitia alterar os dados bancários e emitir um reembolso no mesmo dia, sem nenhuma notificação ao inquilino. O atendente era medido pelo tempo de atendimento das ligações, o que desestimulava verificações extras. Nenhuma pessoa sozinha falhou; o projeto tornou a fraude fácil. Ele faz referência à separação de privilégio de Saltzer e Schroeder (1975), que sugere que mudanças sensíveis precisam de mais de uma condição independente.

### 8.3 Recomendações

Owen recomenda: confirmar as mudanças bancárias por um código enviado ao telefone ou e-mail cadastrado do inquilino; uma retenção de sete dias nos reembolsos depois de mudanças bancárias; notificação automática ao inquilino de qualquer mudança; e ajustar as métricas da central de atendimento para que o tempo de verificação não seja penalizado. Ele estima o custo e o efeito de cada uma. Kwame e a chefe do financeiro aceitam as quatro. Ines observa que a análise de casos é valiosa quando muda o projeto, e não quando simplesmente atribui a culpa ao atendente envolvido.

### Exemplo resolvido

Owen analisa um caso anonimizado de fraude em reembolso, identifica as causas de projeto usando a separação de privilégio e recomenda quatro mudanças aceitas.

> **Caso sintético.** O caso é sintético; Saltzer e Schroeder (1975) é real.

### Erros e limites

Casos históricos têm evidências faltantes. As retenções podem atrasar reembolsos legítimos.

### Exercícios

- **EX036 — Perguntas fracas.** Por que as perguntas de identificação eram fracas? *Rubrica:* 3 = criminosos conseguem encontrar a data de nascimento e o endereço;; 2 = dados públicos;; 1 = nenhuma;; 0 = nenhuma.

- **EX037 — Causa no sistema.** Que característica do sistema permitiu a fraude? *Rubrica:* 3 = mudança bancária e reembolso no mesmo dia sem notificação;; 2 = mesmo dia;; 1 = nenhuma;; 0 = nenhuma.

- **EX038 — Princípio.** Que princípio Owen aplicou? *Rubrica:* 3 = separação de privilégio;; 2 = separação;; 1 = menor privilégio;; 0 = nenhuma.

- **EX039 — Mudança nas métricas.** Por que ajustar as métricas da central de atendimento? *Rubrica:* 3 = as metas de tempo de atendimento desestimulavam verificações extras;; 2 = incentivos;; 1 = nenhuma;; 0 = nenhuma.

- **EX040 — Retenção do reembolso.** Por quanto tempo o reembolso fica retido após uma mudança bancária? *Rubrica:* 3 = sete dias;; 2 = sete;; 1 = nenhuma;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX040 (as de EX041–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Owen Hartley, Ines Carvalho, Kwame Asante, a Meridian Professional Academy, a Thornbury Housing Association e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Manter as informações dos inquilinos privadas, os registros corretos e os serviços funcionando.

**EX002.** Porque um saldo errado poderia levar a cartas indevidas de cobrança de atrasados.

**EX003.** O sistema de reparos, já que uma caldeira quebrada no inverno não pode esperar.

**EX004.** Um profissional capaz, que sabe aplicar métodos e quando encaminhar a especialistas.

**EX005.** Criptografia, configuração de nuvem ou questões jurídicas, como a legislação de proteção de dados.

**EX006.** Porque só os responsáveis de negócio podem aceitar trade-offs, como um login mais lento em troca de uma proteção mais forte.

**EX007.** Que o vazamento de um novo endereço poderia pôr em perigo um inquilino fugindo de violência doméstica.

**EX008.** Login simples para a maioria das funções, com verificação extra para os dados de contato.

**EX009.** Porque o projeto protege dados diferentes em níveis diferentes, em vez de tratar tudo igual.

**EX010.** Ele deu a cada responsável vinte minutos e fez as mesmas perguntas.

**EX011.** O responsável pelo sistema e Kwame Asante, o chefe de TI.

**EX012.** Para mostrar depois que a exportação não foi alterada.

**EX013.** Ele parou, informou o responsável pelo sistema e apagou os dados excedentes.

**EX014.** Quando o trabalho termina, conforme acordado na autorização.

**EX015.** Para evitar ver fichas de inquilinos de que a revisão de acesso não precisava.

**EX016.** Os códigos dos cofres de chaves para entrar nas casas dos inquilinos.

**EX017.** Os códigos dos cofres de chaves visíveis para todos os contratados, e não só para o designado.

**EX018.** A divulgação dos códigos dos cofres de chaves, com nota 9.

**EX019.** Que notas simples orientam a ordem do trabalho, mas não são medições precisas.

**EX020.** Contas de ex-funcionários dos contratados ainda ativas, com nota 6.

**EX021.** Porque as organizações muitas vezes já possuem capacidades que ninguém usa bem.

**EX022.** Uma biblioteca desatualizada e TLS fraco num subdomínio de teste sem uso que aponta para um servidor ativo.

**EX023.** Não significa que os dados dos inquilinos estejam seguros, apenas que as configurações correspondem a uma lista do fornecedor.

**EX024.** Que o scanner pode não ter conseguido alcançá-lo.

**EX025.** O que ela mede, o que ela não consegue ver e como confirmar um resultado surpreendente.

**EX026.** Porque as etapas em fluxos familiares são seguidas com mais confiabilidade do que procedimentos separados.

**EX027.** Após noventa dias, a menos que sejam renovadas.

**EX028.** São mostrados apenas na ordem do contratado designado e apenas no dia da visita.

**EX029.** Caíram de 210 para 135 depois da primeira revisão.

**EX030.** Em até dois dias úteis, como exigência contratual.

**EX031.** Um histórico de mudanças que os contratados não conseguem editar.

**EX032.** Porque não pode ser testado nem confirmado por um fornecedor.

**EX033.** Três de quatro passaram, e o requisito de visibilidade do código falhou.

**EX034.** O corte do fornecedor era o fim do dia seguinte, e não o dia da visita.

**EX035.** Os quatro requisitos passaram depois que o fornecedor mudou o corte.

**EX036.** Porque se apoiavam em informações que criminosos encontram facilmente, como a data de nascimento e o endereço.

**EX037.** Os dados bancários podiam mudar e um reembolso podia ser emitido no mesmo dia, sem notificação ao inquilino.

**EX038.** A separação de privilégio, que exige mais de uma condição independente para mudanças sensíveis.

**EX039.** Porque as metas de tempo de atendimento desestimulavam os atendentes de fazer verificações extras.

**EX040.** Sete dias.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
