# Governança, Riscos e Compliance de Segurança: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 028, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão na edição em inglês; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais em atividade que migram para funções de GRC e precisam de métodos práticos para riscos, achados, testes de controles e garantia de fornecedores.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios comparam a autoavaliação com a revisão independente, calculam tamanhos de amostra com zero desvios e medem a idade dos achados abertos, sempre sobre dados sintéticos. O relatório SOC 2 revisado é fictício e não é uma atestação; as normas são citadas pela edição e parafraseadas, e nada aqui é aconselhamento jurídico. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma profissional de compliance ao longo de um curso de seis meses, em torno de uma cooperativa de crédito: fundamentos, partes interessadas, prática autorizada, métodos de risco, autoavaliação, fluxo de achados, testes de controles, um caso de fornecedor, relatórios e ética, qualidade dos processos, uma revisão de garantia supervisionada e o portfólio. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Lena Hoffmann** | Profissional de compliance em transição para GRC | Inventada |
| **Sr. Victor Reyes** | Mentor | Inventado |
| **Ashby Professional Academy** | Academia fictícia | Inventada |
| **Marston Credit Union** | Cooperativa fictícia, 400 funcionários | Inventada |

### Fontes principais

ISO 31000:2018 (no Brasil, ABNT NBR ISO 31000:2018); ISO/IEC 27005:2022 e 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); PCI DSS v4.0; trust services criteria da AICPA. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem

Você vai (1) explicar os conceitos centrais de segurança em termos de negócio; (2) relacioná-los aos serviços de uma cooperativa de crédito; (3) reconhecer onde a governança agrega valor.

### 1.1 Conceitos centrais

Lena Hoffmann trabalha há seis anos em compliance na Marston Credit Union, uma cooperativa financeira fictícia, de propriedade dos associados, com quatrocentos funcionários, produtos de poupança e crédito, um aplicativo de mobile banking e serviços de cartão. Ela entra no curso profissional de seis meses da fictícia Ashby Professional Academy, com a mentoria do Sr. Victor Reyes. O primeiro módulo revisita as ideias centrais: confidencialidade, integridade e disponibilidade; ameaças que exploram vulnerabilidades para causar impacto; e controles que previnem, detectam ou corrigem. Ela aprende a explicar cada uma com os serviços da Marston, em vez de definições abstratas.

### 1.2 Aplicar à Marston

Para os dados das contas dos associados, a confidencialidade e a integridade são o que mais importa: vazamentos ou saldos errados abalam a confiança e podem violar a lei. Para o aplicativo, a disponibilidade também importa, já que os associados esperam acesso a qualquer hora. Lena lista as ameaças mais relevantes: tomada de conta por senhas roubadas, fraude por engenharia social contra a equipe da central de atendimento, ransomware afetando o core bancário e erros de fornecedores. Ela aprende que entender o negócio primeiro permite julgar quais controles são proporcionais. A tomada de conta por senhas roubadas, por exemplo, aponta para uma autenticação mais forte no aplicativo, e não para mais treinamento na central.

### 1.3 Onde a governança ajuda

A experiência de Lena em compliance a ajuda a ver onde a governança agrega valor. Existem muitos controles, mas ninguém verifica se funcionam. As decisões de risco são tomadas informalmente pela TI, sem envolver os donos de negócio. O conselho recebe relatórios longos, com pouca análise. Ela vê seu novo papel como ligar essas peças: responsabilidades claras, decisões de risco documentadas com a participação do negócio, controles testados e relatórios ao conselho que permitam decidir. O Sr. Reyes observa que a disciplina de compliance dela é uma base sólida para esse trabalho mais amplo, e acrescenta que as decisões informais da TI são a primeira lacuna a fechar, porque todos os passos seguintes dependem da participação dos donos de negócio.

### Exemplo resolvido

Lena relaciona os conceitos de segurança aos serviços da Marston, lista as principais ameaças e identifica onde a governança agregaria valor.

> **Caso sintético.** A Ashby, a Marston e todos os detalhes são sintéticos.

### Erros e limites

O enquadramento de negócio pode simplificar demais a tecnologia. As listas de ameaças mudam.

### Exercícios

- **EX001 — Prioridades dos dados dos associados.** Que objetivos de segurança mais importam para os dados das contas dos associados? *Rubrica:* 3 = confidencialidade e integridade;; 2 = C e I;; 1 = só disponibilidade;; 0 = nenhuma.
- **EX002 — Disponibilidade do aplicativo.** Por que a disponibilidade importa para o aplicativo? *Rubrica:* 3 = os associados esperam acesso a qualquer hora;; 2 = acesso;; 1 = nada;; 0 = nenhuma.
- **EX003 — Alvo da engenharia social.** Que equipe é alvo da fraude por engenharia social? *Rubrica:* 3 = a equipe da central de atendimento;; 2 = central;; 1 = nada;; 0 = nenhuma.
- **EX004 — Lacunas de governança.** Cite duas lacunas de governança que Lena identificou. *Rubrica:* 3 = controles não testados e decisões de risco informais;; 2 = lacunas;; 1 = nada;; 0 = nenhuma.
- **EX005 — Força do compliance.** Por que a experiência de Lena em compliance é útil? *Rubrica:* 3 = sua disciplina é uma base sólida;; 2 = disciplina;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Governança, riscos e compliance de segurança: contexto de serviços e partes interessadas

### Objetivos de aprendizagem

Você vai (1) identificar as partes interessadas na segurança de uma cooperativa de crédito; (2) mapear suas expectativas; (3) definir a finalidade do programa de GRC.

### 2.1 Partes interessadas

Lena mapeia as partes interessadas: os associados, que confiam suas economias à Marston; o conselho, eleito pelos associados; o regulador financeiro; o fundo garantidor de depósitos; as bandeiras de cartão, por meio das obrigações do PCI DSS v4.0; os auditores; e fornecedores como o provedor do core bancário. Cada um tem expectativas sobre a segurança. Os associados esperam que seu dinheiro e seus dados estejam seguros. O regulador espera uma gestão de riscos sólida e a comunicação tempestiva de incidentes. As bandeiras esperam a proteção dos dados dos portadores de cartão. Ela aprende que a GRC atende a muitos públicos ao mesmo tempo; o fundo garantidor e as bandeiras, por exemplo, pedirão evidências diferentes sobre os mesmos controles.

### 2.2 Expectativas

Lena lista as expectativas de cada parte interessada, como elas são expressas e como a Marston mostra que as atende. As expectativas do regulador chegam por meio de normas e de visitas de supervisão; a Marston mostra conformidade por meio de políticas, relatórios de risco e resultados de auditoria. As expectativas do conselho chegam por meio do apetite a risco; a Marston mostra seu desempenho por meio de relatórios. Ela aprende que mapear as expectativas para as evidências revela onde a Marston não tem um meio claro de mostrar que atende a uma expectativa. Para os associados, por exemplo, a Marston não tem relatório algum mostrando que seus dados estão seguros, o que vira uma lacuna a fechar cedo.

### 2.3 Finalidade do programa

Com esse contexto, Lena redige uma declaração de finalidade para o programa de GRC da Marston: manter o risco de segurança dentro do apetite do conselho, cumprir as obrigações legais e contratuais e dar aos associados, ao conselho e aos reguladores evidências confiáveis de que sua confiança é justificada. O Sr. Reyes pergunta como ela saberia se o programa deu certo. Ela acrescenta resultados mensuráveis, como os principais riscos dentro do apetite, nenhum achado alto em atraso e revisões regulatórias sem ressalvas. Cada resultado pode ser verificado por trimestre, e assim a declaração de finalidade vira algo pelo qual o conselho pode cobrar o programa.

### Exemplo resolvido

Lena mapeia sete partes interessadas, liga as expectativas às evidências e redige uma declaração de finalidade com resultados mensuráveis.

> **Caso sintético.** O contexto da Marston é sintético; o PCI DSS v4.0 é real.

### Erros e limites

As visões das partes interessadas mudam. As declarações de finalidade podem ser vagas.

### Exercícios

- **EX006 — Expectativa do regulador.** O que o regulador espera? *Rubrica:* 3 = gestão de riscos sólida e comunicação tempestiva de incidentes;; 2 = expectativas;; 1 = nada;; 0 = nenhuma.
- **EX007 — Dever perante as bandeiras.** Que obrigação vem das bandeiras de cartão? *Rubrica:* 3 = PCI DSS v4.0;; 2 = PCI;; 1 = nada;; 0 = nenhuma.
- **EX008 — Benefício do mapeamento.** O que o mapeamento das expectativas para as evidências revela? *Rubrica:* 3 = expectativas que a Marston ainda não consegue mostrar que atende;; 2 = lacunas;; 1 = nada;; 0 = nenhuma.
- **EX009 — Finalidade do programa.** Qual é a finalidade do programa de GRC da Marston? *Rubrica:* 3 = manter o risco dentro do apetite, cumprir as obrigações, dar evidências confiáveis;; 2 = finalidade;; 1 = nada;; 0 = nenhuma.
- **EX010 — Resultado de sucesso.** Cite um resultado mensurável que Lena acrescentou. *Rubrica:* 3 = nenhum achado alto em atraso;; 2 = resultado;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e manuseio de evidências

### Objetivos de aprendizagem

Você vai (1) trabalhar dentro dos limites de autoridade e de sigilo; (2) manusear as evidências com segurança; (3) evitar conflitos no trabalho de garantia.

### 3.1 Autoridade

Na nova função, Lena pode pedir evidências a qualquer departamento, mas não pode mudar sistemas nem aprovar exceções por conta própria. Ela aprende a confirmar sua autoridade antes de agir, sobretudo quando lhe pedem para olhar dados de associados. A política interna da Marston só permite que a equipe de GRC acesse dados de associados quando necessário para uma revisão específica, com aprovação e registro em log. Ela aprende que respeitar esses limites protege os associados e mantém seu trabalho defensável. Quando uma revisão precisa de dados de associados, ela agora arquiva a referência da aprovação junto com a evidência, para que o acesso possa ser justificado depois.

### 3.2 Manuseio de evidências

Lena coleta evidências como os aceites das revisões de acesso, relatórios de sistemas e resultados de testes. Ela as guarda numa pasta restrita, nomeia os arquivos de forma consistente, com data e origem, e registra de onde veio cada item. Remove os dados de associados que não são necessários. Aprende que a evidência deve ser completa o bastante para sustentar as conclusões, protegida contra alterações e manuseada conforme sua sensibilidade, sobretudo quando contém informações pessoais ou financeiras. Para o aceite de uma revisão de acesso, ela registra de que sistema ele veio e a data da exportação, para que outro revisor possa obter o mesmo arquivo.

### 3.3 Conflitos

Lena escreveu, no passado, os procedimentos de proteção de dados da Marston. Agora lhe pedem que avalie se eles funcionam. O Sr. Reyes aponta o conflito: ela pode tender a ver com bons olhos o próprio trabalho. Ela declara o conflito e pede a uma colega que revise essa área. Aprende que, no trabalho de garantia, a independência importa, e que declarar e gerir os conflitos é melhor do que fingir que eles não existem. A revisão dos procedimentos de proteção de dados feita pela colega é então relatada em nome da colega, e não de Lena, o que deixa claro para o leitor quem formou aquela conclusão.

### Exemplo resolvido

Lena confirma sua autoridade antes de acessar dados, manuseia as evidências com segurança e declara um conflito ao avaliar os próprios procedimentos.

> **Caso sintético.** As políticas e os papéis são sintéticos.

### Erros e limites

A independência é relativa em equipes pequenas. O manuseio de evidências toma tempo.

### Exercícios

- **EX011 — Limites de Lena.** O que Lena não pode fazer na sua função? *Rubrica:* 3 = mudar sistemas ou aprovar exceções;; 2 = limites;; 1 = nada;; 0 = nenhuma.
- **EX012 — Acesso a dados de associados.** Quando a equipe de GRC pode acessar dados de associados? *Rubrica:* 3 = só quando necessário para uma revisão específica, com aprovação e registro;; 2 = necessidade;; 1 = sempre;; 0 = nenhuma.
- **EX013 — Proteção das evidências.** Que proteções se aplicam às evidências? *Rubrica:* 3 = pasta restrita, nomes consistentes, registro da origem, dados minimizados;; 2 = proteção;; 1 = nada;; 0 = nenhuma.
- **EX014 — Conflito encontrado.** Que conflito Lena tinha? *Rubrica:* 3 = avaliar procedimentos que ela mesma escreveu;; 2 = autorrevisão;; 1 = nada;; 0 = nenhuma.
- **EX015 — Resposta ao conflito.** Como Lena geriu o conflito? *Rubrica:* 3 = declarou-o e pediu a uma colega que revisasse;; 2 = declarar;; 1 = ignorar;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Governança, riscos e compliance de segurança: métodos centrais

### Objetivos de aprendizagem

Você vai (1) conduzir uma avaliação de riscos com um processo consagrado; (2) ligar os riscos ao apetite; (3) registrar as decisões de tratamento.

### 4.1 O processo

Lena aprende o processo de riscos descrito na ISO 31000:2018 (ABNT NBR ISO 31000:2018) e aplicado à segurança da informação na ISO/IEC 27005:2022: estabelecer o contexto, identificar os riscos, analisá-los e avaliá-los, tratá-los, e monitorar e analisar criticamente. Ela conduz uma avaliação do aplicativo de mobile banking da Marston com o dono do produto e as equipes de segurança de TI e de prevenção a fraudes. Eles identificam riscos como tomada de conta, pagamentos fraudulentos a novos favorecidos e indisponibilidades do aplicativo, cada um descrito com causas e consequências. Escrever cada risco como uma causa que leva a uma consequência, como senhas roubadas levando a pagamentos fraudulentos a novos favorecidos, facilita mirar os tratamentos.

### 4.2 Apetite

O conselho da Marston declarou um apetite baixo para perdas financeiras dos associados por fraude e um apetite moderado para indisponibilidades curtas do serviço. Lena compara cada risco com o apetite. A tomada de conta que leva a perdas dos associados está acima do apetite e precisa ser tratada. As indisponibilidades curtas do aplicativo ficam dentro do apetite se recuperadas em até quatro horas. Ela aprende que o apetite transforma a análise em decisões: diz à organização quais riscos exigem ação e quais podem ser aceitos. Como as quatro horas de recuperação são o limiar, a Marston também precisa conseguir mostrar que de fato se recupera em até quatro horas.

### 4.3 Decisões de tratamento

Para a tomada de conta, a equipe escolhe uma autenticação mais forte para novos favorecidos e o monitoramento de transações. O dono do produto aceita ser o dono do tratamento, com uma data-alvo. Para as indisponibilidades, a equipe aceita a capacidade atual de recuperação e documenta a aceitação. Lena registra cada decisão com seu dono, data e motivos. Ela aprende que as decisões registradas mostram aos reguladores e aos auditores que os riscos foram considerados e geridos de forma deliberada. O Sr. Reyes observa que a aceitação documentada das indisponibilidades deve nomear o dono do produto e ser revista se as indisponibilidades passarem a exceder quatro horas.

### Exemplo resolvido

Lena conduz uma avaliação de riscos do aplicativo, compara os riscos com o apetite e registra as decisões de tratamento e de aceitação.

> **Caso sintético.** Os riscos e o apetite são sintéticos; a ISO 31000:2018 e a ISO/IEC 27005:2022 são reais.

### Erros e limites

As oficinas dependem de quem participa. As declarações de apetite podem ser vagas.

### Exercícios

- **EX016 — Etapas do processo.** Cite as principais etapas do processo de riscos. *Rubrica:* 3 = contexto, identificar, analisar, avaliar, tratar, monitorar;; 2 = etapas;; 1 = nada;; 0 = nenhuma.
- **EX017 — Acima do apetite.** Que risco estava acima do apetite? *Rubrica:* 3 = tomada de conta levando a perdas dos associados;; 2 = tomada de conta;; 1 = indisponibilidades;; 0 = nenhuma.
- **EX018 — Tolerância a indisponibilidades.** Quando as indisponibilidades do aplicativo ficam dentro do apetite? *Rubrica:* 3 = se recuperadas em até quatro horas;; 2 = 4 horas;; 1 = nada;; 0 = nenhuma.
- **EX019 — Tratamento da tomada de conta.** Que tratamentos foram escolhidos para a tomada de conta? *Rubrica:* 3 = autenticação mais forte para novos favorecidos e monitoramento de transações;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX020 — Registro das decisões.** Por que registrar as decisões de tratamento? *Rubrica:* 3 = para mostrar que os riscos foram geridos de forma deliberada;; 2 = evidência;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Governança, riscos e compliance de segurança: ferramentas e interpretação

### Objetivos de aprendizagem

Você vai (1) usar os resultados da autoavaliação de controles; (2) compará-los com uma revisão independente; (3) interpretar as diferenças com cuidado.

### 5.1 Autoavaliação

A Marston pede aos donos dos controles que deem notas a seus controles todo trimestre, de zero, não implantado, a quatro, plenamente eficaz e evidenciado. Lena aprende que a autoavaliação (CSA) é barata e engaja os donos, mas tende a ser otimista. Para testar isso, ela compara as notas dos donos com uma revisão independente da auditoria interna em quatro domínios de controle: gestão de acessos, gestão de mudanças, backups e gestão de fornecedores. Ambos usaram a mesma escala e as mesmas definições. Usar definições idênticas significa que qualquer diferença entre os dois conjuntos de notas reflete julgamento, e não escalas diferentes.

### 5.2 A comparação

O laboratório calcula as notas médias. A gestão de acessos se dá três vírgula vinte e cinco, contra dois vírgula cinco na revisão, uma diferença de três quartos de ponto. A gestão de mudanças se dá dois vírgula sessenta e sete, contra um vírgula sessenta e sete, uma diferença de um ponto. Os backups se dão quatro, contra três vírgula cinco. A gestão de fornecedores se dá dois vírgula sessenta e sete, contra um vírgula trinta e três, a maior diferença, de um vírgula trinta e três. Todos os domínios se dão notas acima da revisão. O padrão é consistente, mas é o tamanho de cada diferença que orienta a atenção de Lena na seção seguinte.

### Laboratório — Autoavaliação versus revisão independente

```python
"""Control self-assessment: mean rating (0-4) per domain and the gap to independent review."""
self_r = {"access": [3, 3, 4, 3], "change": [3, 2, 3], "backup": [4, 4], "vendor": [3, 3, 2]}
review = {"access": [2, 3, 3, 2], "change": [2, 1, 2], "backup": [4, 3], "vendor": [1, 2, 1]}
for d in self_r:
    s = sum(self_r[d])/len(self_r[d]); r = sum(review[d])/len(review[d])
    print(f"{d}: self {s:.2f} review {r:.2f} gap {s-r:+.2f}")
```

Execute com `python3 lab_csa.py`. Saída verificada:

```text
access: self 3.25 review 2.50 gap +0.75
change: self 2.67 review 1.67 gap +1.00
backup: self 4.00 review 3.50 gap +0.50
vendor: self 2.67 review 1.33 gap +1.33
```

### 5.3 Interpretar

Lena não conclui que os donos são desonestos. Ela pergunta por que as diferenças variam. Os donos da gestão de fornecedores consideraram os controles funcionando porque os contratos incluem cláusulas de segurança, enquanto os revisores descobriram que ninguém verifica se os fornecedores as cumprem. Os backups têm a menor diferença porque os testes de restauração produzem evidências claras. Ela recomenda endurecer as definições das notas, exigindo evidências, e concentrar a revisão independente nos domínios com as maiores diferenças, a começar pela gestão de fornecedores. Exigir evidências para a nota quatro impediria, por exemplo, que a gestão de fornecedores alegasse eficácia só com base em cláusulas contratuais.

### Exemplo resolvido

Lena compara as autoavaliações com a revisão independente, constata que todos os domínios se superestimam, com a gestão de fornecedores no pior caso, 1,33, e explica por que as diferenças variam.

> **Caso sintético.** As notas são sintéticas.

### Erros e limites

Amostras pequenas de controles. Os revisores podem ser rigorosos demais.

### Exercícios

- **EX021 — Viés da autoavaliação.** Qual é o viés típico da autoavaliação? *Rubrica:* 3 = otimismo;; 2 = otimista;; 1 = pessimista;; 0 = nenhuma.
- **EX022 — Maior diferença.** Que domínio teve a maior diferença? *Rubrica:* 3 = gestão de fornecedores, +1,33;; 2 = fornecedores;; 1 = backup;; 0 = nenhuma.
- **EX023 — Menor diferença.** Por que os backups tiveram a menor diferença? *Rubrica:* 3 = os testes de restauração produzem evidências claras;; 2 = evidências;; 1 = nada;; 0 = nenhuma.
- **EX024 — Causa nos fornecedores.** Por que os donos da gestão de fornecedores superestimaram seus controles? *Rubrica:* 3 = os contratos tinham cláusulas, mas ninguém verificava o cumprimento;; 2 = suposição;; 1 = nada;; 0 = nenhuma.
- **EX025 — Recomendação.** O que Lena recomendou? *Rubrica:* 3 = definições de notas baseadas em evidências e revisão focada nas maiores diferenças;; 2 = duas;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Governança, riscos e compliance de segurança: fluxo operacional

### Objetivos de aprendizagem

Você vai (1) desenhar um fluxo de GRC para os achados; (2) definir metas por severidade; (3) relatar o progresso à direção.

### 6.1 Fluxo dos achados

Lena desenha um fluxo para os achados de auditorias e revisões. Cada achado é registrado com descrição, severidade, dono, ação acordada e data-alvo. Os donos atualizam o progresso todo mês. Quando um dono declara a conclusão, Lena verifica as evidências antes de encerrar. Os achados em atraso são escalados para o executivo a quem o dono responde. Ela aprende que um fluxo claro torna a responsabilização visível e impede que os achados sejam esquecidos depois que o relatório de auditoria é arquivado. Verificar as evidências antes do encerramento impede que um achado seja marcado como resolvido quando só existe um plano.

### 6.2 Metas por severidade

Lena propõe metas por severidade: achados altos encerrados em trinta dias, médios em noventa e baixos em cento e oitenta. Ela explica que as metas precisam ser realistas; um achado alto que exige a substituição de um sistema pode precisar de uma medida provisória acordada e de um plano mais longo. Aprende que datas-alvo sem planos realistas estimulam encerramentos falsos, enquanto planos com medidas provisórias mantêm o risco gerido enquanto as correções mais longas avançam. Um achado alto que exige a substituição de um sistema poderia, por exemplo, ser mantido dentro da meta por uma restrição provisória enquanto a substituição é planejada.

### 6.3 Relatórios

Lena relata mensalmente ao comitê executivo de riscos: achados abertos por severidade, achados em atraso com donos e motivos, e achados encerrados com evidências. Ela começa pelos achados altos em atraso. O comitê pede aos donos dos itens atrasados que expliquem os atrasos. Ela aprende que os relatórios funcionam quando são curtos, consistentes e levam à ação no nível certo, em vez de simplesmente informar que os problemas existem. Começar pelos achados altos em atraso faz o tempo limitado do comitê ir para os itens que mais provavelmente precisam de ajuda executiva.

### Exemplo resolvido

Lena desenha um fluxo de achados com encerramento baseado em evidências, metas por severidade e relatórios mensais ao comitê.

> **Caso sintético.** O fluxo é sintético.

### Erros e limites

As metas podem estimular encerramentos falsos. Os comitês podem não agir.

### Exercícios

- **EX026 — Verificação no encerramento.** O que acontece quando um dono declara a conclusão? *Rubrica:* 3 = Lena verifica as evidências antes de encerrar;; 2 = evidências;; 1 = nada;; 0 = nenhuma.
- **EX027 — Meta dos altos.** Qual é a meta para os achados altos? *Rubrica:* 3 = trinta dias;; 2 = 30;; 1 = nada;; 0 = nenhuma.
- **EX028 — Correções longas.** Como tratar um achado alto que exige a substituição de um sistema? *Rubrica:* 3 = medida provisória e plano mais longo acordado;; 2 = provisória;; 1 = nada;; 0 = nenhuma.
- **EX029 — Abertura do relatório.** Por onde começa o relatório de Lena? *Rubrica:* 3 = pelos achados altos em atraso;; 2 = atrasados;; 1 = nada;; 0 = nenhuma.
- **EX030 — Caminho de escalonamento.** Para onde os achados em atraso são escalados? *Rubrica:* 3 = para o executivo a quem o dono responde;; 2 = executivo;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Governança, riscos e compliance de segurança: controles e verificação

### Objetivos de aprendizagem

Você vai (1) escolher tamanhos de amostra para testar controles; (2) testar a operação de um controle; (3) enunciar as conclusões com seus limites.

### 7.1 Tamanhos de amostra

Lena precisa testar se a autenticação de novos favorecidos da Marston funciona em todos os pagamentos. Testar todos os pagamentos é inviável, então ela amostra. O laboratório calcula a menor amostra sem desvios que sustenta cada taxa de desvio tolerável com noventa e cinco por cento de confiança. Para dez por cento, bastam vinte e nove itens; para cinco por cento, cinquenta e nove; para três por cento, noventa e nove. Ela aprende que conclusões mais apertadas exigem amostras maiores, e que a taxa tolerável deve refletir a importância do controle. Cinquenta e nove é o tamanho que ela vai usar para a autenticação de novos favorecidos na seção seguinte.

### Laboratório — Tamanhos de amostra com zero desvios para três taxas toleráveis

```python
"""Smallest zero-deviation sample whose 95% upper bound meets a tolerable rate: (1-t)^n <= 0.05."""
from math import ceil, log
for t in (0.10, 0.05, 0.03):
    n = ceil(log(0.05)/log(1-t)); print(f"tolerable {t:.0%}: sample {n} with no deviations")
```

Execute com `python3 lab_n.py`. Saída verificada:

```text
tolerable 10%: sample 29 with no deviations
tolerable 5%: sample 59 with no deviations
tolerable 3%: sample 99 with no deviations
```

### 7.2 Testar

Como a autenticação de novos favorecidos protege o dinheiro dos associados, Lena escolhe uma taxa tolerável de cinco por cento e sorteia cinquenta e nove pagamentos a novos favorecidos ao longo do trimestre. Para cada um, verifica se o log de autenticação mostra um segundo fator bem-sucedido antes do pagamento. Os cinquenta e nove mostram. Ela registra o método de amostragem, os itens selecionados, as verificações e os resultados, para que outra pessoa possa repetir o teste. O Sr. Reyes observa que o sorteio ao longo do trimestre inteiro importa, porque uma amostra de uma única semana poderia deixar de fora um período em que o controle falhou.

### 7.3 Conclusões

Lena conclui que, com noventa e cinco por cento de confiança, o controle falhou em no máximo cinco por cento dos pagamentos a novos favorecidos durante o trimestre. Ela anota os limites: o teste cobre só o canal do aplicativo, e não os pagamentos nas agências, e verifica que a autenticação aconteceu, e não que ela resistiria a todos os ataques. Aprende que conclusões claras, com limites declarados, valem mais do que afirmações amplas de que o controle funciona. Os pagamentos nas agências precisariam de uma amostra separada antes que se pudesse afirmar algo sobre todos os pagamentos a novos favorecidos.

### Exemplo resolvido

Lena calcula 29, 59 e 99 como tamanhos de amostra com zero desvios, testa 59 pagamentos sem desvios e enuncia uma conclusão delimitada.

> **Caso sintético.** Os pagamentos e os resultados são sintéticos.

### Erros e limites

A amostragem aleatória deixa passar abusos direcionados. Os logs podem estar incompletos.

### Exercícios

- **EX031 — Amostra de cinco por cento.** Quantos itens sem desvios sustentam uma taxa tolerável de 5%? *Rubrica:* 3 = cinquenta e nove;; 2 = 59;; 1 = 29;; 0 = nenhuma.
- **EX032 — Amostra de três por cento.** Quantos são necessários para 3%? *Rubrica:* 3 = noventa e nove;; 2 = 99;; 1 = nada;; 0 = nenhuma.
- **EX033 — Escolha da taxa.** Por que escolher aqui uma taxa tolerável de 5%? *Rubrica:* 3 = o controle protege o dinheiro dos associados;; 2 = importância;; 1 = nada;; 0 = nenhuma.
- **EX034 — Verificação feita.** O que Lena verificou em cada pagamento? *Rubrica:* 3 = um segundo fator bem-sucedido antes do pagamento, no log;; 2 = verificação do log;; 1 = nada;; 0 = nenhuma.
- **EX035 — Limites do teste.** Cite um limite da conclusão. *Rubrica:* 3 = cobre só o canal do aplicativo;; 2 = escopo;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Governança, riscos e compliance de segurança: análise de caso supervisionada

### Objetivos de aprendizagem

Você vai (1) analisar um caso de governança sob supervisão; (2) identificar falhas de controle e de governança; (3) recomendar melhorias proporcionais.

### 8.1 O caso

O Sr. Reyes entrega a Lena um caso sintético de uma cooperativa de crédito congênere. Um fornecedor que administrava a plataforma de cartões sofreu uma violação, expondo dados de cartão de alguns associados. A cooperativa tinha um contrato com cláusulas de segurança e recebia um certificado anual, mas ninguém revisava o relatório de garantia do fornecedor, que apontava exceções na gestão de acessos. Depois da violação, o regulador perguntou por que as exceções não tinham sido acompanhadas. As exceções não lidas na gestão de acessos são exatamente o tipo de alerta que uma revisão do relatório de garantia teria pegado.

### 8.2 Análise

Lena identifica falhas em vários níveis. No nível do controle, a gestão de acessos do fornecedor tinha fraquezas conhecidas. No nível do processo, os relatórios de garantia eram recebidos, mas não lidos. No nível da governança, ninguém era dono do risco de fornecedores, e o conselho nunca viu esse risco relatado. Ela observa que o padrão espelha a lacuna da própria Marston na gestão de fornecedores, encontrada na autoavaliação. Aprende que os casos valem mais quando revelam padrões relevantes para a própria organização. A maior diferença da autoavaliação da Marston, a gestão de fornecedores com um vírgula trinta e três, vira por isso o foco de suas recomendações.

### 8.3 Recomendações

Lena recomenda que a Marston designe um dono para o risco de fornecedores, revise os relatórios de garantia dos fornecedores críticos com um checklist que destaque as exceções, acompanhe as exceções como achados e relate o risco de fornecedores ao conselho duas vezes por ano. Ela mantém as recomendações proporcionais ao porte da Marston. O Sr. Reyes pergunta como ela mediria o sucesso; ela propõe acompanhar a proporção de fornecedores críticos com relatórios revisados e o tempo de acompanhamento das exceções. As duas medidas podem ser relatadas na atualização semestral sobre o risco de fornecedores ao conselho.

### Exemplo resolvido

Lena analisa a violação num fornecedor de uma congênere, encontra falhas nos níveis de controle, processo e governança e recomenda melhorias proporcionais, com medidas.

> **Caso sintético.** O caso é sintético.

### Erros e limites

Casos isolados podem não se generalizar. A visão retrospectiva faz as falhas parecerem óbvias.

### Exercícios

- **EX036 — Gatilho do caso.** O que motivou a pergunta do regulador? *Rubrica:* 3 = exceções não revisadas no relatório de garantia do fornecedor;; 2 = exceções;; 1 = nada;; 0 = nenhuma.
- **EX037 — Falha de processo.** Qual foi a falha no nível do processo? *Rubrica:* 3 = relatórios de garantia recebidos, mas não lidos;; 2 = não lidos;; 1 = nada;; 0 = nenhuma.
- **EX038 — Falha de governança.** Qual foi a falha no nível da governança? *Rubrica:* 3 = ninguém era dono do risco de fornecedores e o conselho nunca o viu;; 2 = propriedade;; 1 = nada;; 0 = nenhuma.
- **EX039 — Acompanhamento das exceções.** Como as exceções dos fornecedores devem ser tratadas? *Rubrica:* 3 = acompanhadas como achados;; 2 = achados;; 1 = ignoradas;; 0 = nenhuma.
- **EX040 — Medida de sucesso.** Dê uma medida de sucesso que Lena propôs. *Rubrica:* 3 = proporção de fornecedores críticos com relatórios revisados;; 2 = medida;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Comunicação, ética e relatórios

### Objetivos de aprendizagem

Você vai (1) escrever relatórios de governança para executivos e conselhos; (2) comunicar más notícias com honestidade; (3) lidar com pressões de forma ética.

### 9.1 Relatórios ao conselho

Lena redige o relatório trimestral de segurança da Marston ao conselho. Ele começa pelas decisões necessárias e segue com os principais riscos diante do apetite, os achados significativos e seu status, os incidentes e as lições aprendidas, e o risco de fornecedores. Usa linguagem simples e se limita a quatro páginas. Cada risco mostra uma tendência e um dono. Ela aprende que os relatórios ao conselho devem apoiar a supervisão: os conselheiros precisam saber o que está dando errado e o que se pede que decidam. Um conselheiro que leia só a primeira página ainda deve saber que decisões estão sendo pedidas ao conselho.

### 9.2 Más notícias

O relatório precisa incluir a fraqueza na gestão de fornecedores. Um executivo sugere descrevê-la como uma oportunidade de melhoria, e não como uma fraqueza. Lena explica que o conselho precisa de um retrato fiel, e que suavizar a linguagem poderia enganar conselheiros que têm deveres legais de supervisão. Ela aceita apresentar a questão junto com o plano de remediação e o progresso. Aprende que um enquadramento honesto, acompanhado de um plano, preserva a confiança melhor do que o eufemismo. Apresentar a fraqueza com seu plano de remediação permite ao conselho julgar o progresso, em vez de apenas tomar conhecimento de um problema.

### 9.3 Ética

Mais tarde, um gerente pede a Lena que adie o registro de um achado para depois da visita do regulador. Ela recusa, explicando que o achado precisa ser registrado quando identificado e que adiá-lo enganaria o regulador. Oferece-se para ajudar o gerente a preparar um plano de remediação para apresentar junto com o achado. Ela aprende que a ética profissional em GRC muitas vezes significa resistir a pequenas pressões para moldar o registro, e que oferecer ajuda torna a recusa mais fácil de aceitar. Registrar o achado quando identificado também protege o gerente, já que a descoberta posterior do adiamento abalaria a confiança do regulador.

### Exemplo resolvido

Lena escreve um relatório ao conselho centrado em decisões, apresenta uma fraqueza com honestidade e com um plano, e se recusa a adiar o registro de um achado.

> **Caso sintético.** Os cenários são sintéticos.

### Erros e limites

Relatórios honestos podem desgastar relações. O engajamento dos conselhos varia.

### Exercícios

- **EX041 — Abertura do relatório.** Por onde começa o relatório de Lena ao conselho? *Rubrica:* 3 = pelas decisões necessárias;; 2 = decisões;; 1 = riscos;; 0 = nenhuma.
- **EX042 — Risco de suavizar.** Por que não chamar a fraqueza de oportunidade de melhoria? *Rubrica:* 3 = poderia enganar conselheiros com deveres de supervisão;; 2 = honestidade;; 1 = nada;; 0 = nenhuma.
- **EX043 — Enquadramento honesto.** Como Lena apresentou a fraqueza? *Rubrica:* 3 = com o plano de remediação e o progresso;; 2 = plano;; 1 = nada;; 0 = nenhuma.
- **EX044 — Pedido de adiamento.** O que um gerente pediu a Lena? *Rubrica:* 3 = adiar o registro de um achado para depois da visita do regulador;; 2 = adiar;; 1 = nada;; 0 = nenhuma.
- **EX045 — Ajuda na recusa.** O que Lena ofereceu em troca? *Rubrica:* 3 = ajuda para preparar um plano de remediação;; 2 = ajuda;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Governança, riscos e compliance de segurança: qualidade e solução de problemas

### Objetivos de aprendizagem

Você vai (1) medir a qualidade do processo de achados; (2) identificar problemas de envelhecimento; (3) investigar por que os achados empacam.

### 10.1 Envelhecimento

Lena verifica há quanto tempo os achados abertos estão pendentes em relação às metas de sua severidade. O laboratório examina oito achados abertos. Dos três altos, dois passaram da meta de trinta dias, com quarenta e oito e noventa e cinco dias. Dos três médios, um passou dos noventa dias, com cento e trinta. Dos dois baixos, um passou dos cento e oitenta dias, com duzentos. Quatro dos oito achados estão em atraso, metade de todos os itens abertos. O envelhecimento sozinho não explica por que esses quatro empacaram, e por isso ela se volta em seguida para os donos.

### Laboratório — Envelhecimento dos achados abertos por severidade

```python
"""Ageing of open audit findings by severity (synthetic Marston data, days open)."""
f = [("high", 12), ("high", 95), ("medium", 40), ("medium", 130), ("medium", 75), ("low", 200), ("low", 15), ("high", 48)]
lim = {"high": 30, "medium": 90, "low": 180}
for s in ("high", "medium", "low"):
    a = [d for x, d in f if x == s]; over = [d for d in a if d > lim[s]]
    print(f"{s}: open {len(a)}, past {lim[s]}-day target {len(over)} {over}")
print(f"total open {len(f)}; overdue {sum(d > lim[s] for s, d in f)}")
```

Execute com `python3 lab_age.py`. Saída verificada:

```text
high: open 3, past 30-day target 2 [95, 48]
medium: open 3, past 90-day target 1 [130]
low: open 2, past 180-day target 1 [200]
total open 8; overdue 4
```

### 10.2 Por que os achados empacam

Lena entrevista os donos dos quatro achados em atraso. O achado alto de noventa e cinco dias depende de uma mudança no fornecedor, que este não priorizou. O achado alto de quarenta e oito dias tem uma correção pronta, à espera de uma janela de mudança. O dono do achado médio saiu da Marston e ninguém o assumiu. O achado baixo foi considerado sem importância e esquecido. Ela aprende que os dados de envelhecimento mostram onde olhar, mas as conversas revelam as causas, que são diferentes em cada achado. O achado médio órfão, por exemplo, precisa de uma correção de processo, enquanto a questão do fornecedor precisa de pressão contratual.

### 10.3 Correções

Lena propõe correções específicas: escalar a questão do fornecedor pela gestão de contratos, agendar uma janela de mudança extra para a correção pronta, reatribuir automaticamente os achados órfãos quando os donos saem e revisar os achados baixos a cada trimestre, para que sejam corrigidos ou formalmente aceitos. Ela também sugere acrescentar o motivo do atraso a cada achado em atraso no relatório ao comitê. Aprende que melhorar a qualidade do processo significa tratar causas distintas, em vez de aplicar um único empurrão genérico. Os motivos de atraso acrescentados também permitem ao comitê ver se a mesma causa se repete.

### Exemplo resolvido

Lena encontra quatro de oito achados em atraso, descobre quatro causas diferentes nas entrevistas e propõe uma correção específica para cada uma.

> **Caso sintético.** Os achados e as causas são sintéticos.

### Erros e limites

Números pequenos. As entrevistas podem ser defensivas.

### Exercícios

- **EX046 — Contagem de atrasados.** Quantos achados abertos estavam em atraso? *Rubrica:* 3 = quatro de oito;; 2 = 4/8;; 1 = nada;; 0 = nenhuma.
- **EX047 — Altos em atraso.** Que achados altos estavam em atraso? *Rubrica:* 3 = os de 48 e 95 dias;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX048 — Causa do órfão.** Por que o achado médio empacou? *Rubrica:* 3 = o dono saiu e ninguém o assumiu;; 2 = órfão;; 1 = nada;; 0 = nenhuma.
- **EX049 — Correção dos órfãos.** Como os achados órfãos serão evitados? *Rubrica:* 3 = reatribuição automática quando os donos saem;; 2 = reatribuir;; 1 = nada;; 0 = nenhuma.
- **EX050 — Correção dos baixos.** Como os achados baixos devem ser tratados? *Rubrica:* 3 = revisados por trimestre, para corrigir ou aceitar formalmente;; 2 = trimestral;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Laboratório supervisionado

### Objetivos de aprendizagem

Você vai (1) conduzir uma revisão de garantia supervisionada de um fornecedor sintético; (2) ler um relatório de garantia com olhar crítico; (3) registrar os achados.

### 11.1 A tarefa

No laboratório supervisionado, Lena revisa um relatório SOC 2 tipo 2 sintético de um fornecedor fictício de processamento de cartões. O Sr. Reyes pede que ela determine se o relatório cobre os serviços que a Marston usa, se o período é atual, que exceções foram apontadas e que controles complementares a própria Marston precisa operar. Ela usa um checklist baseado nas categorias dos trust services criteria da AICPA, sem tratar o relatório sintético como uma atestação real. O Sr. Reyes acrescenta que cada uma dessas perguntas muda quanto a Marston pode confiar no relatório, então nenhuma pode ser pulada.

### 11.2 Ler com olhar crítico

Lena descobre que o relatório cobre o serviço de processamento de cartões, mas exclui o módulo de monitoramento de fraudes que a Marston também usa. O período terminou há nove meses. Aparecem duas exceções: a remoção atrasada dos acessos de desligados e uma varredura trimestral de vulnerabilidades não realizada. O relatório lista os controles complementares da entidade usuária (CUECs), entre eles o de que a Marston deve revisar o acesso dos próprios usuários ao portal do fornecedor. Ela observa que a Marston nunca fez essa revisão. Essa revisão do portal é um controle complementar da entidade usuária, então a lacuna está na Marston, e não no fornecedor.

### 11.3 Achados

Lena registra os achados: o módulo de fraudes está fora do escopo do relatório, então é preciso uma garantia separada; o período está envelhecendo, então deve ser pedida uma bridge letter; as duas exceções precisam de acompanhamento com o fornecedor; e a Marston precisa começar a revisar os próprios usuários do portal. O Sr. Reyes confirma a análise e observa que os controles complementares costumam ser esquecidos porque as organizações supõem que o fornecedor cuida de tudo. Cada um desses quatro itens é então registrado no seu fluxo de achados, com dono, severidade e data-alvo.

### Exemplo resolvido

Lena revisa um relatório SOC 2 sintético e encontra uma lacuna de escopo, um período envelhecido, duas exceções e um controle complementar nunca executado.

> **Caso sintético.** O relatório e o fornecedor são sintéticos; os trust services criteria da AICPA são reais; isto não é uma atestação.

### Erros e limites

Os relatórios têm escopo limitado. As bridge letters dão garantia limitada.

### Exercícios

- **EX051 — Lacuna de escopo.** O que estava fora do escopo do relatório? *Rubrica:* 3 = o módulo de monitoramento de fraudes;; 2 = módulo de fraudes;; 1 = nada;; 0 = nenhuma.
- **EX052 — Período envelhecido.** Por que pedir uma bridge letter? *Rubrica:* 3 = o período do relatório terminou há nove meses;; 2 = envelhecimento;; 1 = nada;; 0 = nenhuma.
- **EX053 — Exceções.** Que duas exceções o relatório apontou? *Rubrica:* 3 = remoção atrasada de desligados e uma varredura de vulnerabilidades não realizada;; 2 = duas;; 1 = nada;; 0 = nenhuma.
- **EX054 — Controle complementar.** Que controle complementar a Marston nunca tinha executado? *Rubrica:* 3 = revisar o acesso dos próprios usuários ao portal do fornecedor;; 2 = revisão do portal;; 1 = nada;; 0 = nenhuma.
- **EX055 — Erro comum.** Por que os controles complementares costumam ser esquecidos? *Rubrica:* 3 = as organizações supõem que o fornecedor cuida de tudo;; 2 = suposição;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Portfólio de prática e revisão final

### Objetivos de aprendizagem

Você vai (1) montar um portfólio de prática; (2) refletir sobre as competências adquiridas; (3) planejar os próximos passos na prática de GRC.

### 12.1 Portfólio

Lena monta seu portfólio: o mapa de partes interessadas e a declaração de finalidade, a avaliação de riscos do aplicativo, a comparação das autoavaliações, o fluxo de achados e a análise de envelhecimento, o teste de controle por amostragem, o relatório ao conselho e a revisão do relatório do fornecedor. Para cada item, escreve uma nota curta sobre o que fez, que evidências o sustentam e o que aprendeu. Ela remove quaisquer dados reais de associados ou de funcionários, mantendo apenas material sintético ou anonimizado. Cada nota liga um artefato ao capítulo em que foi produzido, para que os avaliadores possam seguir seu raciocínio.

### 12.2 Revisão final

O Sr. Reyes e um segundo avaliador revisam o portfólio. Perguntam como ela lidaria com um regulador que questionasse o tamanho da sua amostra; ela explica a taxa tolerável e a confiança e se oferece para ampliar a amostra, se necessário. Perguntam o que ela achou mais difícil; ela responde que foi resistir às pressões para suavizar os relatórios mantendo boas relações. Eles a julgam competente e destacam sua força em ligar as evidências às conclusões. A pergunta sobre a amostra mostra por que ela registrou a taxa tolerável e a confiança ao fazer o teste no capítulo 7.

### 12.3 Próximos passos

Lena planeja seus próximos passos: assumir a responsabilidade pelo risco de fornecedores na Marston, aprofundar seu conhecimento da ISO/IEC 27001:2022 (ABNT NBR ISO/IEC 27001:2022) para apoiar uma possível certificação e ser mentora de uma colega júnior no manuseio de evidências. Ela se compromete a revisar seus métodos todo ano, à medida que as normas e as ameaças mudam. O Sr. Reyes lembra que a prática de GRC depende de julgamento, honestidade e acompanhamento constante, tanto quanto de frameworks. Assumir o risco de fornecedores também fecha a lacuna de governança que ela identificou no caso da cooperativa congênere.

### Exemplo resolvido

Lena monta um portfólio de sete itens, responde aos avaliadores sobre amostragem e pressões e planeja seus próximos passos.

> **Caso sintético.** O portfólio é sintético; a ISO/IEC 27001:2022 é real.

### Erros e limites

Os portfólios mostram trabalhos selecionados. Os planos mudam com as funções.

### Exercícios

- **EX056 — Nota do portfólio.** Que nota acompanha cada item do portfólio? *Rubrica:* 3 = o que fez, as evidências que o sustentam, o que aprendeu;; 2 = nota;; 1 = nada;; 0 = nenhuma.
- **EX057 — Dados no portfólio.** Que dados Lena removeu do portfólio? *Rubrica:* 3 = dados reais de associados ou funcionários;; 2 = dados reais;; 1 = nada;; 0 = nenhuma.
- **EX058 — Questionamento da amostra.** Como Lena responderia a um regulador que questionasse o tamanho da amostra? *Rubrica:* 3 = explicaria a taxa tolerável e a confiança e se ofereceria para ampliar;; 2 = explicar;; 1 = nada;; 0 = nenhuma.
- **EX059 — Parte mais difícil.** O que Lena achou mais difícil? *Rubrica:* 3 = resistir às pressões para suavizar relatórios mantendo as relações;; 2 = pressão;; 1 = nada;; 0 = nenhuma.
- **EX060 — Próxima função.** Que responsabilidade Lena vai assumir em seguida? *Rubrica:* 3 = o risco de fornecedores;; 2 = risco de fornecedores;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Lena Hoffmann, o Sr. Victor Reyes, a Ashby Professional Academy, a Marston Credit Union e todos os números são sintéticos; o relatório SOC 2 revisado é fictício. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Confidencialidade e integridade.

**EX002.** Porque os associados esperam acessar suas contas a qualquer hora.

**EX003.** A equipe da central de atendimento.

**EX004.** Controles não verificados quanto à eficácia e decisões de risco tomadas informalmente pela TI (também relatórios fracos ao conselho).

**EX005.** Porque a disciplina de compliance é uma base sólida para o trabalho mais amplo de governança.

**EX006.** Uma gestão de riscos sólida e a comunicação tempestiva de incidentes.

**EX007.** As obrigações do PCI DSS v4.0 de proteger os dados dos portadores de cartão.

**EX008.** Onde a Marston não tem um meio claro de mostrar que atende a uma expectativa.

**EX009.** Manter o risco de segurança dentro do apetite, cumprir as obrigações e dar às partes interessadas evidências confiáveis.

**EX010.** Por exemplo, nenhum achado de alta severidade em atraso (ou os principais riscos dentro do apetite, revisões regulatórias sem ressalvas).

**EX011.** Mudar sistemas ou aprovar exceções por conta própria.

**EX012.** Só quando necessário para uma revisão específica, com aprovação e registro em log.

**EX013.** Uma pasta restrita, nomes consistentes, origens registradas e remoção dos dados de associados desnecessários.

**EX014.** Pediram que ela avaliasse procedimentos que ela mesma tinha escrito.

**EX015.** Declarou-o e pediu a uma colega que revisasse essa área.

**EX016.** Estabelecer o contexto, identificar, analisar, avaliar, tratar, e monitorar e analisar criticamente.

**EX017.** Tomada de conta levando a perdas financeiras dos associados.

**EX018.** Quando recuperadas em até quatro horas.

**EX019.** Autenticação mais forte para novos favorecidos e monitoramento de transações.

**EX020.** Para mostrar aos reguladores e auditores que os riscos foram considerados e geridos de forma deliberada.

**EX021.** Tende a ser otimista.

**EX022.** Gestão de fornecedores, com diferença de 1,33.

**EX023.** Porque os testes de restauração produzem evidências claras.

**EX024.** Porque os contratos incluíam cláusulas de segurança, mas ninguém verificava se os fornecedores as cumpriam.

**EX025.** Endurecer as definições das notas para exigir evidências e concentrar a revisão nas maiores diferenças.

**EX026.** Lena verifica as evidências antes de encerrar o achado.

**EX027.** Trinta dias.

**EX028.** Com uma medida provisória acordada e um plano mais longo e realista.

**EX029.** Os achados de alta severidade em atraso.

**EX030.** Para o executivo a quem o dono responde.

**EX031.** Cinquenta e nove.

**EX032.** Noventa e nove.

**EX033.** Porque a autenticação de novos favorecidos protege o dinheiro dos associados, então uma taxa apertada é adequada.

**EX034.** Se o log de autenticação mostrava um segundo fator bem-sucedido antes do pagamento.

**EX035.** Cobre só o canal do aplicativo (e mostra que a autenticação ocorreu, não que resiste a todos os ataques).

**EX036.** Exceções no relatório de garantia do fornecedor que ninguém acompanhou.

**EX037.** Os relatórios de garantia eram recebidos, mas não lidos.

**EX038.** Ninguém era dono do risco de fornecedores e o conselho nunca o viu relatado.

**EX039.** Acompanhadas como achados no fluxo.

**EX040.** A proporção de fornecedores críticos com relatórios revisados (ou o tempo de acompanhamento das exceções).

**EX041.** As decisões que se pede ao conselho que tome.

**EX042.** Porque suavizar a linguagem poderia enganar conselheiros que têm deveres legais de supervisão.

**EX043.** Junto com o plano de remediação e o progresso.

**EX044.** Adiar o registro de um achado para depois da visita do regulador.

**EX045.** Ajuda para preparar um plano de remediação a ser apresentado com o achado.

**EX046.** Quatro de oito.

**EX047.** Dois, com 48 e 95 dias.

**EX048.** O dono saiu da Marston e ninguém o assumiu.

**EX049.** Reatribuindo automaticamente os achados quando os donos saem.

**EX050.** Revisados por trimestre, para que sejam corrigidos ou formalmente aceitos.

**EX051.** O módulo de monitoramento de fraudes que a Marston também usa.

**EX052.** Porque o período do relatório terminou nove meses antes.

**EX053.** A remoção atrasada dos acessos de desligados e uma varredura trimestral de vulnerabilidades não realizada.

**EX054.** Revisar o acesso dos próprios usuários ao portal do fornecedor.

**EX055.** Porque as organizações supõem que o fornecedor cuida de tudo.

**EX056.** O que ela fez, as evidências que o sustentam e o que aprendeu.

**EX057.** Quaisquer dados reais de associados ou de funcionários, mantendo apenas material sintético ou anonimizado.

**EX058.** Explicando a taxa tolerável e o nível de confiança e oferecendo-se para ampliar a amostra.

**EX059.** Resistir às pressões para suavizar os relatórios mantendo boas relações.

**EX060.** A responsabilidade pelo risco de fornecedores na Marston.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO 31000:2018 e da ABNT NBR ISO/IEC 27001:2022, citadas nesta edição como referências brasileiras e conferidas em suas fontes oficiais; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Associação Brasileira de Normas Técnicas. (2018). *ABNT NBR ISO 31000:2018 — Gestão de riscos — Diretrizes*. ABNT. <https://www.abntcatalogo.com.br/>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022c). *ISO/IEC 27005:2022 Information security, cybersecurity and privacy protection — Guidance on managing information security risks*. <https://www.iso.org/standard/80585.html>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
