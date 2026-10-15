# Arquitetura e Engenharia de Segurança: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 030, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

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

- **EX001 — A definição de Owen.** Como Owen descreveu a segurança com suas próprias palavras? *Rubrica:* 3 = manter as informações dos inquilinos privadas, os registros corretos e os serviços funcionando;; 2 = três partes;; 1 = vago;; 0 = nenhuma.

- **EX002 — Exemplo de integridade.** Por que a integridade importa para as contas de aluguel? *Rubrica:* 3 = um saldo errado poderia causar cartas indevidas de cobrança;; 2 = cobrança;; 1 = vago;; 0 = nenhuma.

- **EX003 — Exemplo de disponibilidade.** Que serviço mostra a importância da disponibilidade? *Rubrica:* 3 = reparos, como uma caldeira quebrada no inverno;; 2 = reparos;; 1 = portal;; 0 = nenhuma.

- **EX004 — Limite do curso.** O que o curso fará de Owen? *Rubrica:* 3 = um profissional capaz que sabe quando consultar especialistas;; 2 = profissional;; 1 = especialista;; 0 = nenhuma.

- **EX005 — Temas para especialistas.** Cite um tema que Owen vai encaminhar a especialistas. *Rubrica:* 3 = criptografia, configuração de nuvem ou questões jurídicas;; 2 = um;; 1 = vago;; 0 = nenhuma.

### Síntese

Os profissionais começam ligando os objetivos de segurança a serviços reais e conhecendo os limites da sua competência.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 12)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- **EX006 — Por que nomear responsáveis.** Por que nomear os responsáveis de negócio pelos serviços? *Rubrica:* 3 = só eles podem aceitar trade-offs;; 2 = trade-offs;; 1 = vago;; 0 = nenhuma.

- **EX007 — Preocupação de proteção.** O que a responsável por proteção enfatizou? *Rubrica:* 3 = um novo endereço vazado poderia pôr em perigo alguém fugindo de violência;; 2 = endereço;; 1 = vago;; 0 = nenhuma.

- **EX008 — Acordo no portal.** Como o conflito do portal foi resolvido? *Rubrica:* 3 = verificação extra só para visualizar ou alterar os dados de contato;; 2 = verificação adicional;; 1 = vago;; 0 = nenhuma.

- **EX009 — Dissolver o conflito.** Por que muitos conflitos desaparecem em bons projetos? *Rubrica:* 3 = dados diferentes são protegidos de forma diferente;; 2 = diferenciar;; 1 = vago;; 0 = nenhuma.

- **EX010 — Método das entrevistas.** Como Owen manteve as entrevistas comparáveis? *Rubrica:* 3 = vinte minutos com as mesmas perguntas para todos os responsáveis;; 2 = mesmas perguntas;; 1 = vago;; 0 = nenhuma.

### Síntese

Mapear serviços, donos e necessidades permite que os desenhos protejam o que mais importa, mantendo os serviços utilizáveis.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 12)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- **EX011 — Quem autorizou.** Quem autorizou a revisão de Owen? *Rubrica:* 3 = o responsável pelo sistema e Kwame Asante, chefe de TI;; 2 = os dois;; 1 = vago;; 0 = nenhuma.

- **EX012 — Propósito do checksum.** Por que calcular um checksum de cada exportação? *Rubrica:* 3 = para mostrar depois que ela não foi alterada;; 2 = integridade;; 1 = sigilo;; 0 = nenhuma.

- **EX013 — Dados por engano.** O que Owen fez quando apareceram nomes de inquilinos? *Rubrica:* 3 = parou, informou o responsável e apagou os dados excedentes;; 2 = parar;; 1 = continuou;; 0 = nenhuma.

- **EX014 — Exclusão.** Quando as cópias de trabalho são apagadas? *Rubrica:* 3 = quando o trabalho termina, conforme acordado;; 2 = fim do trabalho;; 1 = nunca;; 0 = nenhuma.

- **EX015 — Exportar, não navegar.** Por que exportar as listas de papéis em vez de navegar pelos registros? *Rubrica:* 3 = para evitar ver dados de inquilinos desnecessários à revisão;; 2 = minimizar;; 1 = rapidez;; 0 = nenhuma.

### Síntese

Trabalho autorizado, tratamento cuidadoso das evidências e o mínimo de dados pessoais protegem tanto a organização quanto o profissional.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 12)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- **EX016 — Anotação sensível.** Que dado sensível aparecia nas anotações de acesso dos reparos? *Rubrica:* 3 = códigos dos cofres de chaves;; 2 = códigos;; 1 = vago;; 0 = nenhuma.

- **EX017 — Ameaça de divulgação.** Que ameaça de divulgação o STRIDE encontrou? *Rubrica:* 3 = códigos dos cofres de chaves visíveis para todos os contratados;; 2 = códigos;; 1 = vago;; 0 = nenhuma.

- **EX018 — Primeiro lugar.** Que ameaça ficou em primeiro no laboratório, e com que nota? *Rubrica:* 3 = divulgação dos códigos dos cofres de chaves, 9;; 2 = códigos;; 1 = indisponibilidade do portal;; 0 = nenhuma.

- **EX019 — Cautela com as notas.** Que cautela Owen fez sobre as notas? *Rubrica:* 3 = orientam a ordem, mas não são medições precisas;; 2 = ordenação;; 1 = vago;; 0 = nenhuma.

- **EX020 — Segundo lugar.** Que ameaça ficou em segundo no laboratório? *Rubrica:* 3 = contas de ex-funcionários dos contratados ainda ativas, 6;; 2 = contas antigas;; 1 = vago;; 0 = nenhuma.

### Síntese

A modelagem, o STRIDE e uma classificação simples transformam um serviço em uma lista priorizada de ameaças.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 12)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- **EX021 — Capacidade existente.** Por que aprender primeiro as ferramentas existentes? *Rubrica:* 3 = as organizações muitas vezes possuem capacidades não usadas;; 2 = já possuídas;; 1 = vago;; 0 = nenhuma.

- **EX022 — Achados reais.** Que dois achados do scanner importavam? *Rubrica:* 3 = uma biblioteca desatualizada e TLS fraco num antigo subdomínio de teste ativo;; 2 = dois;; 1 = vago;; 0 = nenhuma.

- **EX023 — Secure score.** O que uma secure score alta na nuvem não significa? *Rubrica:* 3 = que os dados dos inquilinos estejam seguros;; 2 = não é segurança;; 1 = seguro;; 0 = nenhuma.

- **EX024 — Varredura vazia.** O que pode significar nenhum achado num servidor? *Rubrica:* 3 = o scanner não conseguiu alcançá-lo;; 2 = alcançabilidade;; 1 = seguro;; 0 = nenhuma.

- **EX025 — Anotações das ferramentas.** Que três coisas Owen registra para cada ferramenta? *Rubrica:* 3 = o que mede, o que não consegue ver, como confirmar surpresas;; 2 = duas;; 1 = vago;; 0 = nenhuma.

### Síntese

A saída das ferramentas precisa ser interpretada no contexto, com notas claras sobre o que cada ferramenta mede e o que deixa passar.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 12)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- **EX026 — Etapas entrelaçadas.** Por que acrescentar etapas aos processos existentes? *Rubrica:* 3 = são cumpridas com mais confiabilidade do que procedimentos separados;; 2 = confiabilidade;; 1 = vago;; 0 = nenhuma.

- **EX027 — Prazo de expiração.** Quando as contas dos contratados expiram? *Rubrica:* 3 = após noventa dias, a menos que sejam renovadas;; 2 = noventa dias;; 1 = nunca;; 0 = nenhuma.

- **EX028 — Mudança nos códigos.** Como os códigos dos cofres de chaves foram restringidos? *Rubrica:* 3 = só para o contratado designado e no dia da visita;; 2 = designado;; 1 = vago;; 0 = nenhuma.

- **EX029 — Redução de contas.** Como mudaram as contas ativas de contratados? *Rubrica:* 3 = de 210 para 135;; 2 = caíram;; 1 = vago;; 0 = nenhuma.

- **EX030 — Comunicação de desligamentos.** Em que prazo os contratados precisam comunicar desligamentos? *Rubrica:* 3 = em até dois dias úteis, por contrato;; 2 = dois dias;; 1 = vago;; 0 = nenhuma.

### Síntese

A segurança funciona melhor entrelaçada aos fluxos de trabalho existentes, com a automação mantendo o esforço sustentável.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 12)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- **EX031 — Controle contra adulteração.** Que controle trata as anotações alteradas? *Rubrica:* 3 = um histórico de mudanças que os contratados não conseguem editar;; 2 = histórico;; 1 = vago;; 0 = nenhuma.

- **EX032 — Requisito vago.** Por que "o acesso dos contratados deve ser seguro" é um requisito ruim? *Rubrica:* 3 = não pode ser testado;; 2 = não testável;; 1 = vago;; 0 = nenhuma.

- **EX033 — Cobertura no laboratório.** O que a primeira rodada de testes mostrou no laboratório? *Rubrica:* 3 = 3 de 4 requisitos passaram; a visibilidade do código falhou;; 2 = 3 de 4;; 1 = vago;; 0 = nenhuma.

- **EX034 — Causa da falha.** Por que o teste de visibilidade do código falhou? *Rubrica:* 3 = o fornecedor cortava no fim do dia seguinte;; 2 = corte;; 1 = vago;; 0 = nenhuma.

- **EX035 — Resultado do novo teste.** O que a segunda rodada mostrou no laboratório? *Rubrica:* 3 = os 4 requisitos passaram depois da correção do fornecedor;; 2 = 4 de 4;; 1 = vago;; 0 = nenhuma.

### Síntese

Os controles se tornam confiáveis quando são escritos como requisitos testáveis e verificados com resultados registrados.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 12)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- **EX036 — Perguntas fracas.** Por que as perguntas de identificação eram fracas? *Rubrica:* 3 = criminosos conseguem encontrar a data de nascimento e o endereço;; 2 = dados públicos;; 1 = vago;; 0 = nenhuma.

- **EX037 — Causa no sistema.** Que característica do sistema permitiu a fraude? *Rubrica:* 3 = mudança bancária e reembolso no mesmo dia sem notificação;; 2 = mesmo dia;; 1 = vago;; 0 = nenhuma.

- **EX038 — Princípio.** Que princípio Owen aplicou? *Rubrica:* 3 = separação de privilégio;; 2 = separação;; 1 = menor privilégio;; 0 = nenhuma.

- **EX039 — Mudança nas métricas.** Por que ajustar as métricas da central de atendimento? *Rubrica:* 3 = as metas de tempo de atendimento desestimulavam verificações extras;; 2 = incentivos;; 1 = vago;; 0 = nenhuma.

- **EX040 — Retenção do reembolso.** Por quanto tempo o reembolso fica retido após uma mudança bancária? *Rubrica:* 3 = sete dias;; 2 = sete;; 1 = vago;; 0 = nenhuma.

### Síntese

A análise de casos supervisionada encontra as causas de desenho por trás dos incidentes e as transforma em mudanças aceitas.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 12)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Comunicação, ética e relatórios

### Objetivos de aprendizagem

Você vai (1) escrever um relatório de segurança para tomadores de decisão; (2) lidar com honestidade com um dilema ético; (3) comunicar a incerteza.

### 9.1 Escrever o relatório

Owen escreve seu primeiro relatório formal à liderança da Thornbury sobre o trabalho com os reparos e os reembolsos. Ele começa com um resumo de uma página: o que foi encontrado, o que já foi feito, o que falta e que decisões são necessárias. Os detalhes vêm depois, em seções com evidências. Ele evita jargão e explica as consequências em termos que importam aos líderes, como a segurança dos inquilinos e as perdas financeiras. Ines revisa os rascunhos e pede que ele retire dois parágrafos que descrevem longamente seus métodos, que pertencem a um apêndice, e não ao resumo.

### 9.2 Um dilema ético

Ao revisar os acessos, Owen descobre que uma gerente sênior visualizou várias vezes anotações de proteção de inquilinos fora da sua área. Pode ser legítimo ou pode ser uso indevido. Owen não investiga mais por conta própria nem confronta a gerente. Ele relata os fatos, sem acusações, ao encarregado de proteção de dados, como exige a política da Thornbury, e mantém o assunto em sigilo. Ines explica que os profissionais precisam relatar preocupações pelos canais adequados, evitar agir além da sua autoridade e proteger as pessoas envolvidas até que os fatos sejam estabelecidos.

### 9.3 Comunicar a incerteza

Os líderes perguntam se a Thornbury agora está protegida contra fraudes em reembolsos. Owen responde com honestidade: os novos controles bloqueiam o método usado no caso passado, mas criminosos determinados podem tentar outras rotas, como comprometer o e-mail de um inquilino. Ele informa sua confiança em cada controle e explica o que o monitoramento vai mostrar se as tentativas de fraude continuarem. Declarações claras de incerteza ajudam os líderes a tomar decisões sensatas e evitam a decepção e a desconfiança que seguem as afirmações confiantes demais quando algo depois dá errado. Ele coloca esses níveis de confiança numa tabela curta.

### Exemplo resolvido

Owen escreve um relatório à liderança com um resumo de uma página, relata um possível uso indevido de acesso pelos canais adequados e declara a incerteza com honestidade.

> **Caso sintético.** O relatório e os eventos são sintéticos.

### Erros e limites

Os resumos podem omitir ressalvas importantes. Relatar preocupações pode tensionar as relações de trabalho.

### Exercícios

- **EX041 — Conteúdo do resumo.** O que contém o resumo de uma página? *Rubrica:* 3 = achados, ações tomadas, o que falta e decisões necessárias;; 2 = três;; 1 = vago;; 0 = nenhuma.

- **EX042 — Material de apêndice.** O que Ines pediu que Owen levasse para um apêndice? *Rubrica:* 3 = descrições longas dos métodos;; 2 = métodos;; 1 = vago;; 0 = nenhuma.

- **EX043 — Preocupação com acesso.** Como Owen tratou o acesso da gerente às anotações de proteção? *Rubrica:* 3 = relatou os fatos ao encarregado de proteção de dados sem investigar nem confrontar;; 2 = canal adequado;; 1 = confrontou;; 0 = nenhuma.

- **EX044 — Resposta honesta.** Como Owen respondeu se a Thornbury está protegida contra fraude em reembolsos? *Rubrica:* 3 = os controles bloqueiam o método passado, mas restam outras rotas;; 2 = incerteza;; 1 = sim;; 0 = nenhuma.

- **EX045 — Sigilo.** Por que manter em sigilo a preocupação com o acesso? *Rubrica:* 3 = para proteger as pessoas até que os fatos sejam estabelecidos;; 2 = proteger;; 1 = vago;; 0 = nenhuma.

### Síntese

O reporte profissional é claro para quem decide, ético no tratamento das preocupações e honesto quanto à incerteza.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — aula 09 (capítulo 09 de 12)

[← Capítulo 08](#ch-08) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Arquitetura e engenharia de segurança: qualidade e solução de problemas

### Objetivos de aprendizagem

Você vai (1) revisar a qualidade do trabalho de segurança; (2) solucionar um controle que atrapalha a operação; (3) melhorar sem perder proteção.

### 10.1 Revisão de qualidade

Ines pede a Owen que revise o próprio trabalho anterior como se fosse um auditor. Ele confere se cada achado tem evidência, cada requisito tem um teste, cada decisão tem um responsável e cada documento tem data e versão. Ele encontra duas decisões sem responsável registrado e um requisito testado apenas uma vez, antes de uma atualização do fornecedor. Ele corrige os registros e agenda um novo teste. A autorrevisão regular pega lacunas de qualidade antes que outros as encontrem e cria hábitos que tornam as auditorias posteriores simples.

### 10.2 Um controle que atrapalha

Depois que a retenção dos reembolsos entra em vigor, a central de atendimento relata inquilinos irritados cujos reembolsos legítimos ficam atrasados sete dias após atualizarem os dados bancários, incluindo inquilinos idosos que mudaram de banco depois do fechamento de uma agência. Owen investiga. A retenção funciona como projetado, mas o projeto não considerou os casos legítimos urgentes. Ele se reúne com o financeiro e a central de atendimento para entender o volume: cerca de doze casos legítimos por mês. O controle está certo em princípio, mas rígido demais na prática. Ele registra as reclamações e os volumes como evidência.

### 10.3 Melhorar com segurança

Owen propõe um caminho de exceção: se o inquilino confirmar a mudança por meio de uma ligação de retorno para o telefone cadastrado, feita por outra equipe, a retenção pode ser reduzida para um dia. A exceção exige duas pessoas, preservando a separação de privilégio, e é registrada. O financeiro aceita. As reclamações caem, e nenhuma fraude ocorre pela exceção nos três primeiros meses. Ines observa que bons profissionais ajustam os controles em resposta aos efeitos reais, em vez de defender o projeto original ou remover a proteção sob pressão.

### Exemplo resolvido

Owen revisa o próprio trabalho, investiga as reclamações sobre a retenção dos reembolsos e acrescenta um caminho de exceção com duas pessoas que mantém a proteção.

> **Caso sintético.** Os volumes e os resultados são sintéticos.

### Erros e limites

As exceções podem ser abusadas se as verificações enfraquecerem. Três meses é um período curto de observação.

### Exercícios

- **EX046 — Lacunas da autorrevisão.** O que a autorrevisão de Owen encontrou? *Rubrica:* 3 = duas decisões sem responsável e um requisito testado uma vez antes de uma atualização;; 2 = lacunas;; 1 = vago;; 0 = nenhuma.

- **EX047 — Casos legítimos.** Quantos casos urgentes legítimos ocorrem por mês? *Rubrica:* 3 = cerca de doze;; 2 = doze;; 1 = vago;; 0 = nenhuma.

- **EX048 — Caminho de exceção.** Como a retenção pode ser reduzida? *Rubrica:* 3 = ligação de retorno ao número cadastrado por outra equipe, e então um dia;; 2 = ligação de retorno;; 1 = removida;; 0 = nenhuma.

- **EX049 — Princípio mantido.** Que princípio a exceção preserva? *Rubrica:* 3 = a separação de privilégio, ao exigir duas pessoas;; 2 = duas pessoas;; 1 = vago;; 0 = nenhuma.

- **EX050 — Primeiros resultados.** O que aconteceu nos três primeiros meses da exceção? *Rubrica:* 3 = as reclamações caíram e nenhuma fraude usou a exceção;; 2 = os dois;; 1 = vago;; 0 = nenhuma.

### Síntese

A revisão de qualidade e a resolução ágil de problemas aprimoram os controles sem abandonar o seu propósito protetor.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — aula 10 (capítulo 10 de 12)

[← Capítulo 09](#ch-09) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Laboratório supervisionado

### Objetivos de aprendizagem

Você vai (1) conduzir um laboratório isolado de revisão de acessos; (2) encontrar permissões excessivas; (3) relatar os resultados com cuidado.

### 11.1 O laboratório

Ines propõe um laboratório supervisionado com dados sintéticos modelados no sistema de gestão de casos da Thornbury. A tarefa é comparar as permissões de cada usuário com seu papel no trabalho e identificar o acesso excessivo. O laboratório roda inteiramente offline, sobre nomes e papéis gerados, então nenhum dado de pessoa real está envolvido. Owen primeiro escreve as permissões esperadas para cada papel com a ajuda de uma descrição sintética de papéis, porque uma revisão só é tão boa quanto sua definição do que cada função precisa. Ines aprova as definições de papéis antes que Owen execute a comparação.

### Laboratório — Encontrar permissões além das necessidades do papel

```python
# Compare user permissions with role needs (synthetic case management data).
need = {"housing": {"cases"}, "safeguarding": {"cases", "safeguarding"}, "finance": {"rent"}, "temp": {"cases"}}
users = [("u1", "housing", {"cases"}, True), ("u2", "housing", {"cases", "safeguarding"}, True),
         ("u3", "housing", {"cases", "safeguarding"}, True), ("u4", "safeguarding", {"cases", "safeguarding"}, True),
         ("u5", "finance", {"rent", "case-edit"}, True), ("u6", "finance", {"rent"}, True),
         ("u7", "temp", {"cases"}, False), ("u8", "housing", {"cases"}, True), ("u9", "safeguarding", {"cases", "safeguarding"}, True)]
found = 0
for u, role, has, contract_active in users:
    issues = sorted(has - need[role]) + ([] if contract_active else ["account active after contract end"])
    if issues: found += 1; print(f"{u} ({role}): {', '.join(issues)}")
print(f"{found} of {len(users)} users need action")
```

Execute com `python3 lab_access.py`. Saída verificada:

```text
u2 (housing): safeguarding
u3 (housing): safeguarding
u5 (finance): case-edit
u7 (temp): account active after contract end
4 of 9 users need action
```

### 11.2 Resultados

O laboratório encontra quatro usuários com permissões excessivas: dois agentes de habitação com acesso a anotações de proteção de que não precisam mais depois de mudar de equipe, um assistente financeiro com direitos de edição de casos e um trabalhador temporário cujo contrato terminou, mas cuja conta continua ativa. Owen os ordena por risco: a conta ativa de quem já saiu e o acesso às anotações de proteção primeiro, porque expõem os dados mais sensíveis. Ines confere a ordenação e concorda, observando que ordenar pela sensibilidade ajuda os responsáveis ocupados a agir primeiro nos itens mais importantes.

### 11.3 Relatar com cuidado

Owen escreve o relatório do laboratório como faria no trabalho: nomes de papéis e contagens no texto principal, nomes individuais num apêndice restrito, as ações recomendadas e as evidências de cada uma. Ele observa que o laboratório não conseguia ver as permissões concedidas dentro de documentos ou de pastas compartilhadas fora do sistema. Ines dá uma nota alta ao relatório pelo cuidado com os dados pessoais e pelos limites honestos. Ela o lembra de que uma revisão real também precisaria da confirmação do responsável pelo sistema antes de qualquer acesso ser removido.

### Exemplo resolvido

Owen conduz um laboratório offline de revisão de acessos, encontra quatro permissões excessivas, ordena-as pela sensibilidade e relata com cuidado e com os limites.

> **Caso sintético.** Todos os dados do laboratório são sintéticos.

### Erros e limites

As definições de papéis podem estar erradas. O acesso fora do sistema continua invisível.

### Exercícios

- **EX051 — Definição primeiro.** Por que definir as permissões esperadas antes da revisão? *Rubrica:* 3 = uma revisão só é tão boa quanto sua definição das necessidades;; 2 = referência;; 1 = vago;; 0 = nenhuma.

- **EX052 — Número de achados.** Quantos usuários tinham permissões excessivas no laboratório? *Rubrica:* 3 = 4 de 9;; 2 = quatro;; 1 = vago;; 0 = nenhuma.

- **EX053 — Maiores riscos.** Que achados ficaram no topo? *Rubrica:* 3 = a conta ativa de quem saiu e o acesso desnecessário às anotações de proteção;; 2 = dois;; 1 = financeiro;; 0 = nenhuma.

- **EX054 — Estrutura do relatório.** Onde ficam os nomes individuais no relatório de Owen? *Rubrica:* 3 = num apêndice restrito;; 2 = apêndice;; 1 = texto principal;; 0 = nenhuma.

- **EX055 — Ponto cego do laboratório.** O que o laboratório não conseguia ver? *Rubrica:* 3 = permissões dentro de documentos ou pastas compartilhadas fora do sistema;; 2 = acesso externo;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma revisão de acessos cuidadosa define primeiro as necessidades, classifica o excesso por sensibilidade e relata respeitando os dados pessoais.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — aula 11 (capítulo 11 de 12)

[← Capítulo 10](#ch-10) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Portfólio de prática e revisão final

### Objetivos de aprendizagem

Você vai (1) montar um portfólio de trabalho profissional; (2) revisar o que mudou na Thornbury; (3) planejar a prática contínua.

### 12.1 O portfólio

Owen monta seu portfólio: o mapa de serviços e partes interessadas, o modelo de ameaças dos reparos e a ordenação, o fluxo dos contratados, os requisitos com os resultados da verificação, a análise do caso de reembolso, o relatório à liderança, o projeto do caminho de exceção e o relatório do laboratório. Cada item tem uma nota curta explicando o que ele fez, o que aprendeu e o que faria de outro modo. Os dados pessoais são removidos ou substituídos por exemplos sintéticos. O portfólio mostra a empregadores e avaliadores evidências de habilidade aplicada, e não apenas a frequência ao curso.

### 12.2 O que mudou

Owen revisa os resultados. As contas de contratados caíram de duzentas e dez para cento e trinta e cinco, os códigos dos cofres de chaves agora ficam visíveis apenas aos contratados designados nos dias de visita, as mudanças bancárias exigem confirmação e os reembolsos depois de mudanças ficam retidos, com uma exceção segura. Nenhuma fraude em reembolso foi relatada desde então. Ele tem o cuidado de dizer que a ausência de fraude ao longo de alguns meses não prova que o risco desapareceu, e recomenda monitoramento contínuo e uma revisão anual do modelo de ameaças dos reparos.

### 12.3 Prática contínua

A Thornbury cria uma função de arquiteto de segurança e a oferece a Owen. Ele planeja aprofundar seu conhecimento de identidade e segurança em nuvem, entrar numa comunidade profissional e pedir a Kwame um mentor de uma organização parceira. Ele mantém a lista de encaminhamentos do capítulo 1 e anota quais itens agora consegue tratar sozinho. O retorno final de Ines é que a formação de Owen em gestão de projetos se tornou uma força, porque a arquitetura de segurança consiste em grande parte em coordenar pessoas, decisões e evidências ao longo de uma organização. Ele também agenda uma revisão de seis meses com Ines.

### Exemplo resolvido

Owen monta um portfólio comentado, revisa com cautela as mudanças medidas na Thornbury e planeja o desenvolvimento contínuo numa nova função.

> **Caso sintético.** Os itens do portfólio e os resultados são sintéticos.

### Erros e limites

Os portfólios podem exagerar a contribuição individual. Os resultados de curto prazo podem não durar.

### Exercícios

- **EX056 — Notas do portfólio.** Que nota acompanha cada item do portfólio? *Rubrica:* 3 = o que fez, o que aprendeu e o que mudaria;; 2 = três;; 1 = vago;; 0 = nenhuma.

- **EX057 — Cautela sobre a fraude.** Por que a ausência de fraude relatada não é prova de sucesso? *Rubrica:* 3 = alguns meses sem fraude não provam que o risco desapareceu;; 2 = período curto;; 1 = prova;; 0 = nenhuma.

- **EX058 — Próximo estudo.** O que Owen vai estudar em seguida? *Rubrica:* 3 = identidade e segurança em nuvem;; 2 = identidade;; 1 = vago;; 0 = nenhuma.

- **EX059 — Força da formação.** Por que a formação de Owen se tornou uma força? *Rubrica:* 3 = a arquitetura consiste em grande parte em coordenar pessoas, decisões e evidências;; 2 = coordenação;; 1 = vago;; 0 = nenhuma.

- **EX060 — Dados no portfólio.** Como os dados pessoais são tratados no portfólio? *Rubrica:* 3 = removidos ou substituídos por exemplos sintéticos;; 2 = removidos;; 1 = vago;; 0 = nenhuma.

### Síntese

Um portfólio de trabalhos comentados, uma revisão honesta dos resultados e um plano de crescimento completam a preparação profissional.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — aula 12 (capítulo 12 de 12)

[← Capítulo 11](#ch-11) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Owen Hartley, Ines Carvalho, Kwame Asante, a Meridian Professional Academy, a Thornbury Housing Association e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX041.** O que foi encontrado, o que já foi feito, o que falta e que decisões são necessárias.

**EX042.** Dois parágrafos que descreviam longamente os métodos dele.

**EX043.** Ele relatou os fatos ao encarregado de proteção de dados sem investigar mais nem confrontá-la.

**EX044.** Disse que os controles bloqueiam o método passado, mas que outras rotas, como o e-mail comprometido de um inquilino, continuam possíveis.

**EX045.** Para proteger as pessoas envolvidas até que os fatos sejam estabelecidos.

**EX046.** Duas decisões sem responsável e um requisito testado apenas antes de uma atualização do fornecedor.

**EX047.** Cerca de doze casos legítimos por mês.

**EX048.** Por meio de uma ligação de retorno ao telefone cadastrado, feita por outra equipe, reduzindo a retenção para um dia.

**EX049.** A separação de privilégio, já que são necessárias duas pessoas.

**EX050.** As reclamações caíram e nenhuma fraude ocorreu pela exceção.

**EX051.** Porque uma revisão só é tão boa quanto sua definição do que cada função precisa.

**EX052.** Quatro de nove usuários.

**EX053.** A conta ativa de um contrato encerrado e o acesso desnecessário às anotações de proteção.

**EX054.** Num apêndice restrito, com nomes de papéis e contagens no texto principal.

**EX055.** Permissões concedidas em documentos ou pastas compartilhadas fora do sistema.

**EX056.** O que ele fez, o que aprendeu e o que faria de outro modo.

**EX057.** Porque alguns meses sem fraude não provam que o risco desapareceu.

**EX058.** Identidade e segurança em nuvem.

**EX059.** Porque a arquitetura de segurança consiste em grande parte em coordenar pessoas, decisões e evidências.

**EX060.** São removidos ou substituídos por exemplos sintéticos.

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
