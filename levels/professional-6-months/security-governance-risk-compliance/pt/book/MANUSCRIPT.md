# Governança, Riscos e Compliance de Segurança: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 028, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Lena Hoffmann, o Sr. Victor Reyes, a Ashby Professional Academy, a Marston Credit Union e todos os números são sintéticos; o relatório SOC 2 revisado é fictício. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
