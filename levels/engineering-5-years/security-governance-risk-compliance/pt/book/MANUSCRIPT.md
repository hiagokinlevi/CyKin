# Governança, Riscos e Compliance de Segurança: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 120, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 50 já estão escritos em português, com os exercícios EX001–EX060 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 21–50 (EX061–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de engenharia que projetam, verificam e operam um programa de governança, riscos e compliance de segurança como um sistema de engenharia.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios calculam perda esperada, validação de registros, risco residual, taxas de aprovação de controles, falha em camadas, limites de amostragem por atributos, otimização de orçamento e digests de evidências, sempre sobre dados sintéticos. Os números de risco são ilustrações, as normas são citadas pela edição e parafraseadas, e nada aqui é auditoria, atestação ou aconselhamento jurídico reais. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de engenharia num curso de cinco anos centrado no programa de GRC de uma cooperativa de energia elétrica: fundamentos, grandezas e dados de risco, requisitos e modelos, projeto e implementação de controles, medição, verificação e validação, operações e otimização, o projeto final, o dossiê de evidências, a tese e a defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Nadia Okafor** | Estudante de engenharia | Inventada |
| **Prof. Tomas Brenner** | Orientador | Inventado |
| **Kestrel Polytechnic** | Universidade fictícia | Inventada |
| **Ardwell Power Cooperative** | Distribuidora de energia elétrica fictícia, 900 funcionários | Inventada |

### Fontes principais

ISO 31000:2018 (no Brasil, ABNT NBR ISO 31000:2018); ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022), 27002:2022 e 27005:2022; NIST [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1), [SP 800-37 Rev. 2](https://doi.org/10.6028/NIST.SP.800-37r2), [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5) e [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); COBIT 2019; PCI DSS v4.0; Cox (2008), [doi:10.1111/j.1539-6924.2008.01030.x](https://doi.org/10.1111/j.1539-6924.2008.01030.x); Gordon e Loeb (2002), [doi:10.1145/581271.581274](https://doi.org/10.1145/581271.581274). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

Capítulos 21–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) descrever com taxas um risco que muda ao longo do tempo; (2) identificar quando a exposição cresce ou diminui; (3) usar a acumulação para totalizar a exposição num período.

### 1.1 Taxas na governança

Nadia Okafor é estudante de engenharia na fictícia Kestrel Polytechnic. Seu orientador, o Prof. Tomas Brenner, liga cada disciplina básica a um único caso: a fictícia Ardwell Power Cooperative, uma distribuidora de energia elétrica com novecentos funcionários, um portal de pagamento para clientes e acesso remoto para os fornecedores que mantêm seus sistemas de controle. Em cálculo, Nadia aprende que a derivada mede a rapidez com que algo muda. Na Ardwell, o número de achados de auditoria em aberto muda a cada mês. Sua taxa de variação mostra se o backlog está diminuindo, estável ou crescendo, o que interessa mais ao conselho do que uma contagem mensal isolada.

### 1.2 Ler a curva

Nadia traça os achados em aberto depois da última auditoria externa. A contagem salta quando o relatório chega e depois cai à medida que as equipes fecham os itens, rápido no início e devagar depois, porque restam os achados mais difíceis. A derivada é fortemente negativa no começo e se achata mais tarde. Onde a curva se achata, a atenção da gestão costuma diminuir, e os achados antigos ficam parados. Nadia aprende que uma previsão em linha reta prometeria, de forma equivocada, que todo achado se fecha numa data fixa. Escolher uma forma realista para a resposta das organizações é a primeira decisão de modelagem na análise de governança.

### 1.3 Acumular a exposição

A integração soma uma taxa ao longo do tempo. Nadia a usa para definir a exposição a partir de uma fraqueza conhecida: cada dia em que um servidor exposto à internet continua sem patch aumenta a janela em que um atacante poderia explorá-lo. A área sob a curva das fraquezas em aberto ao longo do tempo é a exposição acumulada. Fechar os achados mais depressa reduz essa área mesmo que a contagem final seja a mesma. Isso dá à Ardwell uma medida de governança melhor do que o número de achados fechados, porque premia a rapidez nas fraquezas que importam.

### Exemplo resolvido

Nadia descreve o backlog de achados de auditoria como uma curva, lê sua taxa de variação e define a exposição acumulada como uma área.

> **Caso sintético.** A Kestrel, a Ardwell e todos os números são sintéticos.

### Erros e limites

Curvas suaves escondem dados mensais irregulares. As áreas de exposição ignoram a gravidade de cada fraqueza.

### Exercícios

- **EX001 — Tendência do backlog.** O que a taxa de variação dos achados em aberto diz ao conselho? *Rubrica:* 3 = se o backlog está diminuindo, estável ou crescendo;; 2 = tendência;; 1 = nada;; 0 = nenhuma.
- **EX002 — Sentido do achatamento.** Por que o achatamento da curva importa? *Rubrica:* 3 = a atenção diminui e os achados difíceis ficam parados;; 2 = achados parados;; 1 = nada;; 0 = nenhuma.
- **EX003 — Integral da exposição.** Como Nadia define a exposição acumulada? *Rubrica:* 3 = a área sob as fraquezas em aberto ao longo do tempo;; 2 = área;; 1 = contagem;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) escrever regras de política em lógica; (2) encontrar conflitos entre regras; (3) usar conjuntos para comparar quem tem acesso com quem deveria ter.

### 2.1 Políticas como lógica

Nadia traduz duas políticas da Ardwell para a lógica. Uma diz que toda sessão remota ao sistema de controle deve usar autenticação multifator. Outra diz que os fornecedores podem se conectar em emergências sem demora. Escritas como proposições, as duas entram em choque quando o token de um fornecedor falha durante uma interrupção do fornecimento. A lógica precisa expõe o conflito antes que um engenheiro tenha de decidir sob pressão qual regra quebrar. Nadia propõe uma regra de emergência explícita, com um mecanismo alternativo pré-aprovado e revisão posterior, para que a exceção faça parte da política, e não seja um contorno sem documentação.

### 2.2 Conjuntos de acesso

Com conjuntos, Nadia compara as pessoas com acesso ao sistema de controle com as pessoas cujo papel o exige. A diferença entre os conjuntos revela sete contas de funcionários que mudaram de função. A interseção entre fornecedores e contas sem autenticação multifator mostra duas contas de fornecedores em risco. Os conjuntos transformam preocupações vagas em listas exatas sobre as quais os responsáveis podem agir. Também facilitam testar se uma mudança proposta amplia ou restringe os acessos, que é a pergunta básica de toda decisão de governança de acessos que a Ardwell toma.

### 2.3 Contar combinações

Nadia conta os conflitos de segregação de funções no sistema financeiro da Ardwell. Existem cinco permissões sensíveis, e a política proíbe que uma mesma pessoa tenha ao mesmo tempo cadastrar fornecedor e aprovar pagamento, ou aprovar pagamento e conciliar banco. Ela conta os pares de permissões, lista os proibidos e depois confere os conjuntos de permissões dos funcionários contra a lista. A contagem torna a regra testável por um script simples. Também mostra com que rapidez as verificações crescem quando se acrescentam permissões, um motivo para manter simples o desenho dos papéis e automatizar a detecção de conflitos.

### Exemplo resolvido

Nadia expõe em lógica um conflito entre políticas, encontra sete contas obsoletas por diferença de conjuntos e conta os pares de permissões proibidos.

> **Caso sintético.** As políticas, as contas e as contagens são sintéticas.

### Erros e limites

A lógica captura as regras escritas, não a prática real. As listas de conjuntos ficam desatualizadas depressa.

### Exercícios

- **EX004 — Choque na emergência.** Que duas políticas entram em choque durante uma interrupção? *Rubrica:* 3 = MFA obrigatória e acesso imediato de fornecedores em emergências;; 2 = conflito;; 1 = nada;; 0 = nenhuma.
- **EX005 — Contas obsoletas.** Quantas contas obsoletas do sistema de controle a diferença de conjuntos revelou? *Rubrica:* 3 = sete;; 2 = 7;; 1 = nada;; 0 = nenhuma.
- **EX006 — Pares proibidos.** Cite um par de permissões proibido. *Rubrica:* 3 = cadastrar fornecedor com aprovar pagamento;; 2 = par de SoD;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar a infraestrutura física ao escopo da governança; (2) raciocinar sobre energia, calor e falhas em salas de dados; (3) incluir os controles físicos na análise de riscos.

### 3.1 Escopo físico

Os sistemas de informação da Ardwell funcionam em lugares físicos: uma sala de dados na sede, subestações com equipamentos de controle e um site de contingência. Nadia aprende que o escopo da governança precisa incluir esses lugares, porque a ISO/IEC 27002:2022 agrupa controles físicos, como áreas seguras, proteção de equipamentos e utilidades de suporte, ao lado dos organizacionais e tecnológicos. A física a ajuda a entender por quê. Energia elétrica, calor e vibração afetam o funcionamento dos equipamentos, e um programa de segurança que os ignora deixa riscos de disponibilidade sem gestão. Nadia acrescenta cada site à declaração de escopo, com um responsável nomeado.

### 3.2 Calor e energia

Cada watt consumido pelos servidores vira calor que a refrigeração precisa remover. Nadia calcula que, se a refrigeração falhar na sala de dados, a temperatura sobe continuamente até os equipamentos se desligarem sozinhos. O tempo até o desligamento depende da carga térmica e da massa térmica da sala. Ela mostra que o monitoramento da Ardwell deveria alertar bem antes desse tempo, e que um registro de risco para falha de refrigeração precisa de um responsável na área de facilities, e não só em TI. A física liga assim um cálculo de engenharia a uma decisão de governança sobre responsabilidade e resposta.

### 3.3 Subestações

Nas subestações, os equipamentos ficam em ambientes hostis e com segurança física limitada. Nadia observa que um armário trancado resiste a uma adulteração casual, mas não a um atacante determinado e com ferramentas. Os controles físicos precisam, portanto, de detecção, como sensores de porta, além de retardo. Ela registra o acesso às subestações como um risco separado, porque combina caminhos físicos e digitais até o sistema de controle. O professor dela ressalta que o risco físico é fácil de esquecer em avaliações feitas de escritório, por isso as visitas aos locais continuam fazendo parte da boa prática de governança.

### Exemplo resolvido

Nadia inclui as salas de dados e as subestações no escopo, liga a física da refrigeração a um responsável pelo risco e combina o retardo físico com a detecção.

> **Caso sintético.** Os sites da Ardwell são sintéticos; a ISO/IEC 27002:2022 é real.

### Erros e limites

Modelos simples de calor ignoram o fluxo de ar. Os controles físicos se degradam sem inspeção.

### Exercícios

- **EX007 — Grupos de controles.** Que grupo de controles da ISO/IEC 27002:2022 cobre as áreas seguras? *Rubrica:* 3 = controles físicos;; 2 = físicos;; 1 = nada;; 0 = nenhuma.
- **EX008 — Responsável pela refrigeração.** Quem deve ser o responsável pelo registro de risco de falha de refrigeração? *Rubrica:* 3 = facilities, não só TI;; 2 = facilities;; 1 = nada;; 0 = nenhuma.
- **EX009 — Retardo e detecção.** Por que as subestações precisam de sensores de porta além das fechaduras? *Rubrica:* 3 = as fechaduras retardam, mas não detectam um atacante determinado;; 2 = detecção;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) representar registros de governança em código; (2) escrever verificações simples sobre eles; (3) manter os scripts legíveis para os auditores.

### 4.1 Registros como dados

O primeiro programa de Nadia lê a lista de políticas da Ardwell como registros estruturados: título, responsável, data de aprovação e data da próxima revisão. Representar as políticas como dados, e não como prosa, permite que um programa as confira. Ela guarda a lista num arquivo CSV e a lê com a biblioteca padrão do Python. O professor insiste em nomes de campos claros e num registro por linha, porque os dados de governança serão lidos por pessoas que não são programadoras, incluindo os auditores internos, que precisam entender o que o script verifica e por quê.

### 4.2 Verificações simples

Nadia escreve funções que sinalizam políticas sem responsável e políticas com revisão vencida. Testa cada função numa pequena lista feita à mão, em que conhece a resposta certa, incluindo casos-limite como uma revisão que vence hoje. Quando uma verificação falha, o programa imprime o título da política e o motivo, e não só uma contagem. Ela aprende que o valor de um script de governança está numa saída acionável: um responsável consegue corrigir uma política específica, mas não consegue fazer nada com um número sem explicação.

### 4.3 Código legível

O Prof. Brenner revisa o código de Nadia com olhar de auditor. Cada função tem uma docstring curta que explica a regra aplicada e de onde ela vem, como a política da Ardwell sobre políticas. Constantes como o intervalo de revisão têm nome, em vez de ficarem escondidas como números soltos. Ele explica que, quando os scripts produzem evidências de compliance, o próprio script passa a fazer parte da evidência, então precisa ser compreensível e estar sob controle de versão. Nadia faz commit do código num repositório, com um histórico curto de cada mudança.

### Exemplo resolvido

Nadia lê as políticas de um CSV, sinaliza responsáveis ausentes e revisões vencidas com os motivos e documenta as regras para os auditores.

> **Caso sintético.** Os registros de políticas são sintéticos.

### Erros e limites

Os scripts conferem só o que está registrado. Dados errados produzem saídas erradas e confiantes.

### Exercícios

- **EX010 — Campos da política.** Que campos cada registro de política contém? *Rubrica:* 3 = título, responsável, data de aprovação, data da próxima revisão;; 2 = quatro campos;; 1 = nada;; 0 = nenhuma.
- **EX011 — Saída acionável.** Por que imprimir o título da política e o motivo, e não só uma contagem? *Rubrica:* 3 = os responsáveis podem agir sobre itens específicos;; 2 = acionável;; 1 = nada;; 0 = nenhuma.
- **EX012 — Script como evidência.** Por que os scripts de compliance precisam ser legíveis e versionados? *Rubrica:* 3 = o script passa a fazer parte da evidência;; 2 = evidência;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever para conselhos, auditores e engenheiros; (2) apresentar o risco com sua incerteza; (3) estruturar um memorando curto de governança.

### 5.1 Três públicos

Nadia aprende que as mensagens de governança chegam a três públicos com necessidades diferentes. Os conselhos precisam de decisões, opções e consequências em linguagem simples. Os auditores precisam de afirmações precisas ligadas a evidências. Os engenheiros precisam de ações específicas e prazos. Um único documento raramente serve aos três, então ela pratica escrever, a partir da mesma análise, um resumo de uma página para o conselho, uma tabela de evidências para os auditores e uma lista de tarefas para os engenheiros. Cada versão é exata, mas destaca detalhes diferentes, e ela confere que as três nunca se contradizem.

### 5.2 Declarar a incerteza

Seu primeiro resumo para o conselho diz que o ransomware vai custar à Ardwell noventa mil por ano. O Prof. Brenner pergunta como ela sabe. Ela reescreve: sob premissas declaradas, a perda anual esperada é de cerca de noventa mil, com uma faixa ampla, porque a estimativa de frequência é incerta. Ele explica que os conselhos decidem melhor quando veem a incerteza com honestidade, e que a falsa precisão corrói a confiança quando a realidade é diferente. Hubbard e Seiersen (2016) desenvolvem esse argumento em detalhe para o risco de cibersegurança. Ela mantém a faixa em todas as versões seguintes.

### 5.3 Estrutura do memorando

Nadia adota uma estrutura de memorando para decisões de governança: a decisão necessária, a recomendação, as opções consideradas, o risco e o custo de cada uma, as premissas e as evidências. Ela o limita a duas páginas e leva os detalhes para apêndices. Também acrescenta uma linha dizendo quem foi consultado, porque as decisões de governança afetam muitas equipes. O professor observa que memorandos claros criam um registro do motivo de cada decisão, o que depois apoia as auditorias e ajuda os sucessores a entender escolhas passadas. Ela arquiva cada memorando com suas evidências.

### Exemplo resolvido

Nadia escreve uma única análise para três públicos, declara a incerteza em torno da perda esperada e usa uma estrutura de memorando de decisão.

> **Caso sintético.** Os números são sintéticos; Hubbard e Seiersen (2016) é real.

### Erros e limites

A linguagem simples pode perder nuances. Apêndices longos ficam sem leitura.

### Exercícios

- **EX013 — O que o conselho precisa.** De que os conselhos precisam nas mensagens de governança? *Rubrica:* 3 = decisões, opções e consequências em linguagem simples;; 2 = decisões;; 1 = nada;; 0 = nenhuma.
- **EX014 — Afirmação revista.** Como Nadia reescreveu sua afirmação sobre o ransomware? *Rubrica:* 3 = perda esperada sob premissas declaradas, com uma faixa ampla;; 2 = incerteza;; 1 = certeza;; 0 = nenhuma.
- **EX015 — Linha de consultados.** Por que acrescentar ao memorando quem foi consultado? *Rubrica:* 3 = as decisões de governança afetam muitas equipes;; 2 = registro;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar modelos exponenciais de crescimento e decaimento; (2) modelar como a eficácia de um controle decai sem manutenção; (3) comparar o desconto de perdas futuras.

### 6.1 Decaimento exponencial

Em Cálculo II, Nadia estuda funções exponenciais. Ela modela como a proporção de contas com acesso correto decai depois de uma revisão: a cada mês, alguns funcionários mudam de função sem que seus acessos sejam atualizados, então a correção cai numa fração aproximadamente constante. O modelo prevê que a correção cai à metade num período fixo se nada for feito. As revisões periódicas reiniciam a curva. Isso dá uma razão matemática para a frequência de revisão importar e liga o cálculo a uma pergunta que os auditores da Ardwell já fazem. Nadia traça as duas curvas para compará-las.

### 6.2 Escolher os intervalos

Com o modelo de decaimento, Nadia pergunta com que frequência as revisões precisam acontecer para manter a correção acima de uma meta. Se a correção cai alguns pontos percentuais por mês, uma revisão trimestral a mantém acima da meta, enquanto uma revisão anual a deixa cair muito abaixo até o fim do ano. Ela observa que a taxa de decaimento depende da movimentação de pessoal, então departamentos com alta rotatividade precisam de revisões mais frequentes. O modelo apoia um calendário baseado em risco, e não um intervalo único para todos, o que a ISO/IEC 27002:2022 permite. Ela compartilha esse resultado.

### 6.3 Descontar perdas

Nadia também aprende a descontar valores futuros. Um controle que evita perdas em anos futuros vale menos, em termos de hoje, do que a mesma perda evitada agora, porque o dinheiro tem valor no tempo. Ela aplica um fator de desconto simples a um investimento de três anos em backups. O ajuste é modesto, mas muda qual de duas opções parece melhor. Ela observa que o desconto é padrão na análise de investimentos e que os investimentos em segurança devem ser comparados na mesma base que os demais. Ela declara a taxa usada.

### Exemplo resolvido

Nadia modela a correção dos acessos como decaimento exponencial, deriva intervalos de revisão baseados em risco e desconta as perdas futuras evitadas.

> **Caso sintético.** As taxas de decaimento e os números do investimento são sintéticos.

### Erros e limites

O decaimento real é irregular. As taxas de desconto são escolhas de política.

### Exercícios

- **EX016 — Causa do decaimento.** O que faz a correção dos acessos decair depois de uma revisão? *Rubrica:* 3 = funcionários que mudam de função sem atualização dos acessos;; 2 = mudanças de função;; 1 = nada;; 0 = nenhuma.
- **EX017 — Alta rotatividade.** Que departamentos precisam de revisões mais frequentes? *Rubrica:* 3 = os de alta rotatividade de pessoal;; 2 = rotatividade;; 1 = nada;; 0 = nenhuma.
- **EX018 — Valor no tempo.** Por que uma perda futura evitada vale menos hoje? *Rubrica:* 3 = o dinheiro tem valor no tempo;; 2 = desconto;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) calcular a perda anual esperada a partir da frequência e do impacto; (2) ordenar os riscos pela perda esperada; (3) reconhecer os limites das estimativas de número único.

### 7.1 Frequência e impacto

Nadia aprende a clássica expectativa de perda anualizada (ALE): a taxa anual de ocorrência (ARO) vezes a expectativa de perda única (SLE). Para a Ardwell, ela estima cinco riscos com dados de uma oficina: uma interrupção do faturamento esperada a cada dois anos, custando cento e vinte mil; ransomware uma vez por década, a novecentos mil; quatro notebooks perdidos por ano, a seis mil cada; um vazamento de dados de cartão uma vez em vinte anos, a um milhão e meio; e o mau uso do acesso de fornecedores ao sistema de controle uma vez em cinco anos, a quatrocentos mil.

### 7.2 Ordenar os riscos

O laboratório multiplica cada par e ordena os resultados. O ransomware fica em primeiro, com noventa mil por ano, seguido do mau uso do acesso de fornecedores, com oitenta mil, do vazamento de cartões, com setenta e cinco mil, da interrupção do faturamento, com sessenta mil, e dos notebooks perdidos, com vinte e quatro mil. O total é de trezentos e vinte e nove mil. Nadia percebe que os quatro primeiros estão próximos, então pequenas mudanças nas estimativas poderiam reordená-los. Ela conclui que a ordenação justifica atenção aos quatro, e não a uma única prioridade máxima.

### Laboratório — Perda anual esperada de cinco riscos da Ardwell

```python
"""Annualised loss expectancy (ALE = ARO x SLE) for synthetic Ardwell risks."""
risks = [("billing outage", 0.5, 120_000), ("ransomware", 0.1, 900_000),
         ("lost laptop", 4.0, 6_000), ("payment card breach", 0.05, 1_500_000),
         ("SCADA vendor access misuse", 0.2, 400_000)]
tot = 0
for name, aro, sle in sorted(risks, key=lambda r: -r[1]*r[2]):
    ale = aro*sle; tot += ale
    print(f"{name}: ARO {aro} x SLE {sle:,} = ALE {ale:,.0f}")
print(f"total ALE {tot:,.0f}")
```

Execute com `python3 lab_ale.py`. Saída verificada:

```text
ransomware: ARO 0.1 x SLE 900,000 = ALE 90,000
SCADA vendor access misuse: ARO 0.2 x SLE 400,000 = ALE 80,000
payment card breach: ARO 0.05 x SLE 1,500,000 = ALE 75,000
billing outage: ARO 0.5 x SLE 120,000 = ALE 60,000
lost laptop: ARO 4.0 x SLE 6,000 = ALE 24,000
total ALE 329,000
```

### 7.3 Limites das médias

O Prof. Brenner adverte que a perda esperada esconde a forma dos resultados. O vazamento de cartões tem valor esperado baixo, mas um desfecho único catastrófico que poderia ameaçar a cooperativa, enquanto os notebooks perdidos são frequentes, mas pequenos. Um conselho que vê só médias pode subestimar eventos raros e graves. Nadia aprende a relatar faixas e os piores casos plausíveis ao lado das médias, e lê como Freund e Jones (2015) decompõem frequência e magnitude no modelo FAIR para tornar essas estimativas mais estruturadas e defensáveis.

### Exemplo resolvido

Nadia calcula a ALE de cinco riscos, coloca o ransomware em primeiro com noventa mil, chega a um total de trezentos e vinte e nove mil e observa que as posições estão próximas.

> **Caso sintético.** Todas as estimativas são sintéticas; Freund e Jones (2015) é real.

### Erros e limites

Estimativas únicas escondem a incerteza. As médias subestimam catástrofes raras.

### Exercícios

- **EX019 — Fórmula da ALE.** Como se calcula a expectativa de perda anualizada? *Rubrica:* 3 = taxa de ocorrência vezes expectativa de perda única;; 2 = ARO x SLE;; 1 = nada;; 0 = nenhuma.
- **EX020 — Os dois primeiros.** Que dois riscos ficaram mais altos pela ALE no laboratório? *Rubrica:* 3 = ransomware 90 mil e mau uso por fornecedores 80 mil;; 2 = ransomware primeiro;; 1 = notebooks;; 0 = nenhuma.
- **EX021 — Forma oculta.** Por que o vazamento de cartões pode merecer mais atenção do que sua ALE sugere? *Rubrica:* 3 = é raro, mas tem um desfecho único catastrófico;; 2 = cauda;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) mapear componentes de sistemas como ativos de governança; (2) entender onde os controles atuam no hardware e no firmware; (3) incluir a cadeia de suprimentos no escopo de risco.

### 8.1 Ativos a partir da arquitetura

Nadia estuda como os computadores são feitos de processadores, memória, armazenamento e dispositivos de entrada e saída, todos controlados por firmware e sistemas operacionais. Para a governança, aprende a tratar essas camadas como ativos com responsáveis. Um inventário de ativos, exigido pela ISO/IEC 27001:2022 por meio dos controles do Anexo A, precisa listar não só servidores e notebooks, mas também os dispositivos do sistema de controle nas subestações. Sem saber o que existe, a Ardwell não consegue avaliar riscos nem demonstrar que os controles se aplicam a tudo o que está no escopo. Ela lista cada camada com seu responsável e a equipe que atualiza o registro.

### 8.2 Firmware e confiança

O firmware roda antes do sistema operacional e raramente é atualizado. Nadia aprende que, se o firmware for comprometido, os controles do sistema operacional podem ser contornados. Ela acrescenta o controle das versões de firmware aos registros de ativos da Ardwell e propõe que as compras exijam dos fornecedores atualizações assinadas, redigindo a cláusula. O Prof. Brenner observa que a governança muitas vezes para no sistema operacional porque o firmware é invisível, mas o NIST SP 800-53 Rev. 5 inclui controles de integridade de sistema e de firmware, que dão base para fazer aos fornecedores as perguntas certas.

### 8.3 Cadeia de suprimentos

Todo componente de hardware chega por uma cadeia de suprimentos. Nadia lista os fornecedores da Ardwell para dispositivos do sistema de controle e anota quais oferecem atualizações de segurança e por quanto tempo. Dois dispositivos mais antigos já passaram do período de suporte do fabricante, então novas vulnerabilidades não serão corrigidas. Ela registra isso como risco, com opções: substituir, isolar ou aceitar com monitoramento compensatório, e o acrescenta ao registro de riscos. Aprende que a gestão de riscos da cadeia de suprimentos faz parte da função Govern do NIST CSF 2.0, o que liga o conhecimento de arquitetura à supervisão do conselho.

### Exemplo resolvido

Nadia acrescenta ao inventário os dispositivos do sistema de controle e seu firmware, exige atualizações assinadas e registra os dispositivos sem suporte como risco.

> **Caso sintético.** Os dispositivos e os fornecedores são sintéticos; as normas citadas são reais.

### Erros e limites

Os inventários ficam desatualizados. As datas de suporte dos fornecedores mudam.

### Exercícios

- **EX022 — Escopo do inventário.** O que o inventário de ativos da Ardwell precisa incluir além de servidores e notebooks? *Rubrica:* 3 = os dispositivos do sistema de controle nas subestações;; 2 = dispositivos de OT;; 1 = nada;; 0 = nenhuma.
- **EX023 — Risco do firmware.** Por que um firmware comprometido importa? *Rubrica:* 3 = pode contornar os controles do sistema operacional;; 2 = contornar;; 1 = nada;; 0 = nenhuma.
- **EX024 — Opções sem suporte.** Que opções existem para os dois dispositivos sem suporte? *Rubrica:* 3 = substituir, isolar ou aceitar com monitoramento;; 2 = três opções;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar ferramentas de governança como módulos testados; (2) tratar entradas ruins com segurança; (3) produzir relatórios repetíveis a partir do código.

### 9.1 Módulos e testes

Em Programação II, Nadia reestrutura seu verificador de políticas em módulos: um lê os dados, outro aplica as regras e um terceiro escreve os relatórios. Cada módulo tem testes unitários feitos com o framework de testes da biblioteca padrão. Ela escreve um teste para cada regra, incluindo casos difíceis, como uma política com dois responsáveis ou uma data de revisão no formato errado. Separar a leitura da verificação permite reutilizar as mesmas regras depois em outros registros, como a lista de fornecedores, que também precisa de responsáveis e datas de revisão na Ardwell.

### 9.2 Tratar entradas ruins

Os dados reais de governança são bagunçados. As datas chegam em vários formatos, os responsáveis aparecem como nomes em algumas linhas e como endereços de e-mail em outras, e algumas linhas estão em branco. Nadia aprende a validar a entrada explicitamente e a relatar os problemas, em vez de pular linhas em silêncio. Uma linha pulada poderia esconder um risco sem responsável. Seu programa agora lista cada linha que não conseguiu ler, com o número da linha e o motivo, para que os donos dos dados corrijam a fonte. O Prof. Brenner chama isso de falhar ruidosamente, um hábito vital nas ferramentas de compliance.

### 9.3 Relatórios repetíveis

Nadia torna seus relatórios repetíveis: a mesma entrada sempre produz a mesma saída, com a data da execução, a versão do script e um resumo do arquivo de entrada impressos no topo. Se um auditor perguntar como um número foi produzido, ela pode executar de novo a versão exata sobre a entrada arquivada. Ela aprende que a repetibilidade transforma um script de conveniência pessoal em evidência organizacional, e que um relatório sem suas entradas e sua versão não pode ser conferido por mais ninguém depois.

### Exemplo resolvido

Nadia divide o verificador em módulos testados, relata ruidosamente as linhas ilegíveis e carimba os relatórios com a data da execução, a versão e o resumo da entrada.

> **Caso sintético.** Os registros e os dados são sintéticos.

### Erros e limites

Os testes cobrem só os casos que alguém imaginou. As entradas arquivadas precisam de regras de retenção.

### Exercícios

- **EX025 — Divisão em módulos.** Em que três módulos Nadia dividiu sua ferramenta? *Rubrica:* 3 = leitura, verificação de regras e relatório;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX026 — Linhas puladas.** Por que pular linhas ilegíveis em silêncio é perigoso? *Rubrica:* 3 = pode esconder um risco sem responsável;; 2 = risco oculto;; 1 = nada;; 0 = nenhuma.
- **EX027 — Cabeçalho do relatório.** O que cada relatório imprime no topo? *Rubrica:* 3 = data da execução, versão do script e resumo da entrada;; 2 = cabeçalho;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética da engenharia a decisões de governança; (2) pesar a segurança física das pessoas contra a segurança da informação e o compliance; (3) lidar com pressões para relatar resultados falsos.

### 10.1 Deveres de um engenheiro

Nadia estuda códigos profissionais que colocam a segurança do público em primeiro lugar. Na Ardwell, as decisões de governança afetam o fornecimento de energia a casas, hospitais e empresas, então têm consequências de segurança para as pessoas. Ela aprende que o engenheiro que aprova um controle ou uma avaliação de riscos assume a responsabilidade por sua exatidão. Ética também significa competência: não alegar conhecimento numa área em que não se tem, e pedir ajuda quando um julgamento excede o que se sabe. Esses deveres valem igualmente para o trabalho de compliance, que pode parecer administrativo, mas molda decisões reais sobre infraestrutura pública.

### 10.2 Safety versus security

Alguns controles de segurança da informação podem prejudicar a segurança das pessoas. Bloquear um operador depois de logins malsucedidos poderia impedi-lo de responder a uma emergência na rede elétrica. Nadia aprende que, em ambientes industriais, a disponibilidade e a segurança das pessoas costumam ter prioridade, então os controles precisam ser desenhados com os operadores. Ela propõe monitoramento e alertas para falhas repetidas nos consoles de controle, em vez do bloqueio, com restrição do acesso físico à sala de controle. A decisão é documentada com seu raciocínio, para que os auditores entendam por que um controle padrão foi adaptado em vez de aplicado sem mudanças.

### 10.3 Pressão para relatar resultados falsos

Num estudo de caso, um gestor pede a um analista que marque como aprovado um teste de controle que falhou, para que a auditoria de certificação corra bem. Nadia discute as opções: recusar, registrar o resultado verdadeiro, escalar pelo canal apropriado e proteger a evidência. Ela aprende que falsear resultados de controles mina todo o sistema de gestão e pode violar leis ou contratos. O Prof. Brenner acrescenta que as organizações devem tornar seguro o relato honesto, porque uma cultura que pune más notícias empurra os problemas para fora da vista até que causem danos.

### Exemplo resolvido

Nadia aplica uma ética que põe a segurança das pessoas em primeiro lugar, troca o bloqueio por monitoramento nos consoles de controle e planeja uma resposta honesta à pressão para falsear resultados.

> **Caso sintético.** O estudo de caso e as decisões são sintéticos.

### Erros e limites

Os códigos dão princípios, não respostas. Escalar pode trazer risco pessoal.

### Exercícios

- **EX028 — Dever de aprovação.** O que significa, para um engenheiro, aprovar uma avaliação de riscos? *Rubrica:* 3 = assumir a responsabilidade por sua exatidão;; 2 = responsabilidade;; 1 = nada;; 0 = nenhuma.
- **EX029 — Alternativa nos consoles.** O que Nadia propôs em vez do bloqueio nos consoles de controle? *Rubrica:* 3 = monitoramento e alertas com restrição do acesso físico;; 2 = monitoramento;; 1 = bloqueio;; 0 = nenhuma.
- **EX030 — Cultura honesta.** Por que as organizações devem tornar seguro o relato honesto? *Rubrica:* 3 = punir más notícias esconde os problemas até que causem danos;; 2 = cultura;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) mapear as zonas da rede no escopo da governança; (2) avaliar os caminhos de acesso remoto; (3) relacionar a segmentação aos requisitos de compliance.

### 11.1 Zonas e fronteiras

Nadia mapeia a rede da Ardwell em zonas: a rede corporativa do escritório, o ambiente de pagamento dos clientes, a rede do sistema de controle e uma zona para o acesso remoto de fornecedores. Cada fronteira entre zonas é um ponto onde o tráfego pode ser controlado e registrado. A governança precisa desse mapa porque as decisões de escopo dependem dele. Por exemplo, o PCI DSS v4.0 se aplica ao ambiente de dados do titular do cartão e aos sistemas conectados, então uma boa segmentação mantém pequena a zona de pagamento e reduz o número de sistemas sujeitos a seus requisitos. Uma zona própria para o acesso de fornecedores também permite registrar cada sessão num único ponto.

### 11.2 Caminhos de acesso remoto

Os fornecedores mantêm os equipamentos do sistema de controle por conexões remotas. Nadia rastreia cada caminho: do site do fornecedor, pela internet, até o gateway de acesso remoto da Ardwell, depois até um jump host e, por fim, até o equipamento. Ela anota quais saltos exigem autenticação multifator, quais são registrados e quem aprova cada sessão. Um fornecedor usa uma conexão direta que contorna o jump host. Ela a registra como achado, porque um caminho sem registro nem aprovação quebra as premissas de governança por trás do desenho dos controles. O Prof. Brenner pergunta que evidência a conexão direta deixa, e Nadia não encontra nenhuma: por isso ela não pode ser auditada.

### 11.3 Evidência de segmentação

Afirmar que há segmentação não basta; é preciso demonstrá-la. Nadia aprende que os avaliadores esperam evidências como revisões das regras de firewall e testes que mostrem que o tráfego não atravessa fronteiras que não deveria. Ela escreve um plano de testes para verificar que a rede corporativa não alcança diretamente a rede do sistema de controle. Também observa que a segmentação precisa ser testada de novo depois de mudanças, porque uma única regra nova de firewall pode ligar zonas discretamente. Executar o teste depois de cada mudança de firewall liga a evidência de segmentação à gestão de mudanças, e não a um calendário anual.

### Exemplo resolvido

Nadia mapeia quatro zonas de rede, rastreia os caminhos dos fornecedores, encontra um desvio e planeja testes de segmentação como evidência.

> **Caso sintético.** A rede da Ardwell é sintética; o PCI DSS v4.0 é real.

### Erros e limites

Os diagramas de rede se afastam da realidade. Os testes mostram só o que foi testado.

### Exercícios

- **EX031 — Quatro zonas.** Que quatro zonas Nadia mapeou? *Rubrica:* 3 = corporativa, pagamento, sistema de controle e acesso de fornecedores;; 2 = quatro;; 1 = nada;; 0 = nenhuma.
- **EX032 — Achado do desvio.** Por que a conexão direta do fornecedor foi um achado? *Rubrica:* 3 = contornava o registro e a aprovação;; 2 = desvio;; 1 = nada;; 0 = nenhuma.
- **EX033 — Novo teste.** Quando a segmentação precisa ser testada de novo? *Rubrica:* 3 = depois de mudanças, como novas regras de firewall;; 2 = depois de mudança;; 1 = nunca;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) relacionar os mecanismos do sistema operacional aos objetivos de controle; (2) definir baselines de configuração segura; (3) medir o desvio de configuração.

### 12.1 Mecanismos e objetivos

Nadia estuda como os sistemas operacionais gerenciam usuários, permissões, processos e logs, e liga cada mecanismo a um objetivo de controle. Contas e permissões apoiam o menor privilégio. Os logs de auditoria apoiam a responsabilização e a investigação. Os mecanismos de atualização apoiam a gestão de vulnerabilidades. Entender o mecanismo a ajuda a julgar se uma alegação de controle é crível. Uma política dizendo que os administradores são restritos significa pouco se o sistema operacional não impõe contas de administrador separadas e não registra seu uso em logs que usuários comuns não conseguem alterar. O Prof. Brenner sugere conferir se um usuário comum consegue apagar o log de segurança, porque essa única configuração decide se a alegação se sustenta.

### 12.2 Baselines de configuração

A Ardwell precisa de um baseline de configuração segura para os computadores do escritório e os servidores: que serviços ficam desativados, que configurações são impostas e como as atualizações são aplicadas. Nadia redige um baseline com base nas orientações dos fabricantes e o adapta às necessidades da Ardwell, registrando cada desvio com seu motivo. Um baseline transforma um requisito vago de configuração segura em configurações específicas e testáveis. Ela aprende que os baselines precisam de responsáveis e datas de revisão, como as políticas, porque as versões dos sistemas mudam. Registrar o motivo de cada desvio permite a um revisor futuro ver se ele ainda vale depois de uma atualização do sistema.

### 12.3 Medir o desvio

Os sistemas se afastam do baseline à medida que os administradores fazem mudanças. Nadia escreve um script que compara as configurações reais com o baseline e relata as diferenças. Num teste sintético com quarenta servidores, um quarto mostra pelo menos um desvio, quase sempre um serviço desnecessário ativado para diagnóstico e nunca desligado. Ela aprende que o desvio é normal e que a pergunta de governança é com que rapidez ele é detectado e corrigido. A medição regular transforma o baseline de documento em controle vivo, com resultado observável. Dez servidores em quarenta com desvio, a maioria por serviços de diagnóstico esquecidos, sugerem acrescentar uma etapa de remoção ao procedimento de diagnóstico.

### Exemplo resolvido

Nadia liga os mecanismos do sistema operacional aos objetivos, redige um baseline com desvios registrados e mede o desvio de configuração nos servidores.

> **Caso sintético.** O baseline e os números de desvio são sintéticos.

### Erros e limites

Os baselines ficam atrás das novas versões. Os scripts de desvio não veem as configurações que não verificam.

### Exercícios

- **EX034 — Alegação sobre administradores.** O que torna crível uma política que restringe os administradores? *Rubrica:* 3 = contas de administrador separadas impostas e registradas;; 2 = imposição;; 1 = nada;; 0 = nenhuma.
- **EX035 — Desvios do baseline.** Como os desvios do baseline devem ser tratados? *Rubrica:* 3 = registrados com os motivos;; 2 = documentados;; 1 = ignorados;; 0 = nenhuma.
- **EX036 — Pergunta sobre o desvio.** Qual é a verdadeira pergunta de governança sobre o desvio? *Rubrica:* 3 = com que rapidez é detectado e corrigido;; 2 = rapidez;; 1 = nada;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) modelar um registro de riscos como dados estruturados; (2) validar automaticamente a qualidade do registro; (3) proteger a integridade dos dados de governança.

### 13.1 O registro como dados

O registro de riscos da Ardwell vive numa planilha editada por muitas pessoas. Nadia o modela como uma tabela com campos definidos: identificador, responsável, data da última revisão e uma nota de um a vinte e cinco na escala cinco por cinco da cooperativa. Campos definidos permitem verificações automáticas. Ela aprende com o projeto de bancos de dados que cada campo deve ter um tipo e valores permitidos, para que uma nota trinta ou um responsável em branco possam ser apanhados. Tratar o registro como dados, e não como documento, é o primeiro passo para relatórios de risco confiáveis, e ela documenta cada campo num dicionário de dados.

### 13.2 Validar a qualidade

O laboratório de Nadia confere seis linhas sintéticas do registro contra três regras: todo risco precisa ter responsável, as revisões não podem ter mais de cento e oitenta dias e as notas precisam ficar entre um e vinte e cinco. O laboratório encontra seis problemas em quatro linhas. Dois riscos não têm responsável. Três revisões estão vencidas, uma delas há mais de um ano. Uma nota vinte e seis está fora da escala. Só duas linhas estão limpas. Nadia envia a cada responsável uma lista específica de correções, em vez de um lembrete genérico, para que cada um saiba exatamente o que mudar.

### Laboratório — Validação de um registro de riscos sintético

```python
"""Validate a synthetic risk register: missing owners, overdue reviews, scores out of range."""
from datetime import date
today = date(2026, 10, 1)
reg = [("R01", "IT ops", date(2026, 6, 1), 12), ("R02", "", date(2026, 9, 1), 8),
       ("R03", "Finance", date(2025, 8, 15), 20), ("R04", "OT eng", date(2026, 3, 20), 26),
       ("R05", "HR", date(2026, 8, 30), 6), ("R06", "", date(2025, 11, 2), 15)]
issues = []
for rid, owner, last, score in reg:
    if not owner: issues.append((rid, "no owner"))
    if (today - last).days > 180: issues.append((rid, f"review overdue {(today-last).days} days"))
    if not 1 <= score <= 25: issues.append((rid, f"score {score} outside 1-25"))
for i in issues: print(*i)
print(f"rows {len(reg)}; issues {len(issues)}; clean rows {len(reg) - len({r for r, _ in issues})}")
```

Execute com `python3 lab_register.py`. Saída verificada:

```text
R02 no owner
R03 review overdue 412 days
R04 review overdue 195 days
R04 score 26 outside 1-25
R06 no owner
R06 review overdue 333 days
rows 6; issues 6; clean rows 2
```

### 13.3 Integridade dos dados de governança

Um registro que qualquer pessoa edita sem deixar rastro não serve como evidência. Nadia recomenda levá-lo para um sistema que registre quem mudou cada entrada e quando, com aprovação para mudanças de nota. Ela observa que edições falsificadas ou descuidadas poderiam fazer riscos parecerem menores antes de uma reunião do conselho. O histórico de versões torna essas mudanças visíveis. O Prof. Brenner acrescenta que os mesmos princípios de integridade, controle de acesso e trilha de auditoria que protegem os dados do negócio valem para os dados de governança que descrevem o risco. A aprovação de mudanças de nota também significa que um risco só pode ser rebaixado com uma pessoa identificada assumindo a decisão.

### Exemplo resolvido

Nadia define campos tipados no registro, encontra seis problemas em quatro de seis linhas e recomenda um sistema de registro auditado.

> **Caso sintético.** As linhas do registro são sintéticas.

### Erros e limites

A validação confere a forma, não se os riscos estão certos. As trilhas de auditoria precisam ser revisadas.

### Exercícios

- **EX037 — Regras de validação.** Que três regras o laboratório aplicou? *Rubrica:* 3 = responsável presente, revisão em até 180 dias, nota de 1 a 25;; 2 = três regras;; 1 = nada;; 0 = nenhuma.
- **EX038 — Linhas limpas.** Quantas das seis linhas estavam limpas? *Rubrica:* 3 = duas;; 2 = 2;; 1 = seis;; 0 = nenhuma.
- **EX039 — Risco à integridade.** O que poderia acontecer sem histórico de mudanças? *Rubrica:* 3 = riscos rebaixados para parecer menores antes das reuniões do conselho;; 2 = manipulação;; 1 = nada;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) aplicar práticas de desenvolvimento seguro como controles de governança; (2) gerenciar mudanças com aprovação e rastreabilidade; (3) incluir o código de terceiros no risco.

### 14.1 Desenvolvimento como controle

A Ardwell desenvolve e mantém seu portal de pagamento para clientes. Nadia aprende que as práticas de desenvolvimento seguro, como revisão de código, testes de segurança e gestão de dependências, são controles de governança, além de hábitos de engenharia. A ISO/IEC 27002:2022 inclui controles para ciclos de vida de desenvolvimento seguro e codificação segura, e o PCI DSS v4.0 exige que o software sob medida dos sistemas de pagamento seja desenvolvido com segurança. Ela mapeia cada prática do fluxo de trabalho da equipe do portal a esses requisitos e anota onde já existe evidência nas ferramentas da equipe, como os registros de revisão no repositório, que podem ser reaproveitados nas auditorias.

### 14.2 Gestão de mudanças

Toda mudança no portal passa por um ticket, uma revisão de código e uma aprovação antes da implantação. Nadia confere um mês sintético de mudanças e descobre que a maioria é rastreável do ticket até a implantação, mas algumas correções emergenciais pularam a revisão. Ela recomenda um caminho emergencial documentado, com revisão posterior em até dois dias úteis. A gestão de mudanças rastreável permite que os auditores confirmem que o que roda em produção foi aprovado, e que os engenheiros encontrem a mudança que introduziu um problema quando algo quebra. A revisão em dois dias úteis mantém o caminho emergencial rápido sem perder a rastreabilidade.

### 14.3 Código de terceiros

O portal depende de dezenas de bibliotecas de código aberto. Nadia aprende que cada uma é um fornecedor cujas vulnerabilidades se tornam risco da Ardwell. Ela propõe uma lista de materiais de software (SBOM) com cada componente e sua versão, com alertas automáticos quando uma vulnerabilidade conhecida for publicada. Também anota as obrigações de licenciamento, que são uma questão de compliance por si só. O Prof. Brenner observa que as aplicações modernas são, em sua maior parte, código de outras pessoas, então a governança precisa alcançar os componentes que a equipe nunca escreveu. A SBOM também diz à Ardwell, em poucas horas, que versões do portal são afetadas quando uma vulnerabilidade de biblioteca é anunciada.

### Exemplo resolvido

Nadia mapeia as práticas de desenvolvimento às normas, encontra correções emergenciais sem rastreabilidade e propõe uma lista de materiais de software.

> **Caso sintético.** Os registros de mudanças são sintéticos; as normas citadas são reais.

### Erros e limites

As revisões variam em profundidade. As listas de componentes deixam escapar as dependências transitivas.

### Exercícios

- **EX040 — Normas para o desenvolvimento.** A que duas normas Nadia mapeou o desenvolvimento seguro? *Rubrica:* 3 = ISO/IEC 27002:2022 e PCI DSS v4.0;; 2 = duas;; 1 = nada;; 0 = nenhuma.
- **EX041 — Caminho emergencial.** O que Nadia recomendou para as correções emergenciais? *Rubrica:* 3 = um caminho documentado com revisão em até dois dias úteis;; 2 = revisão posterior;; 1 = nada;; 0 = nenhuma.
- **EX042 — Risco das bibliotecas.** Por que as bibliotecas de código aberto são uma preocupação de governança? *Rubrica:* 3 = suas vulnerabilidades e licenças se tornam risco da Ardwell;; 2 = fornecedor;; 1 = nada;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) definir confidencialidade, integridade e disponibilidade para os ativos da Ardwell; (2) ligar ameaças, vulnerabilidades e impacto ao risco; (3) distinguir os tipos de controle.

### 15.1 Objetivos de segurança

Nadia define o que segurança significa para os principais ativos da Ardwell. Para os dados de pagamento dos clientes, a confidencialidade é o que mais importa. Para as leituras de medidores que geram as contas, a integridade. Para os sistemas de controle que mantêm a energia fluindo, a disponibilidade e a segurança das pessoas. Ela aprende que ordenar os objetivos por ativo orienta a escolha dos controles, porque um controle que reforça a confidencialidade, como um bloqueio rígido, pode enfraquecer a disponibilidade. Um bloqueio rígido nos consoles do sistema de controle, por exemplo, poderia impedir um operador de restabelecer a energia durante um incidente. Explicitar essas prioridades ajuda o conselho a entender por que os controles variam.

### 15.2 Os blocos do risco

Nadia aprende os blocos usados no NIST SP 800-30 Rev. 1: fontes e eventos de ameaça, vulnerabilidades e condições predisponentes, probabilidade e impacto. O risco surge quando uma ameaça pode explorar uma vulnerabilidade para causar um impacto. Ela aplica isso ao acesso remoto dos fornecedores: a ameaça é o mau uso de uma conta de fornecedor, a vulnerabilidade é uma senha compartilhada e o impacto é uma interrupção não planejada. Separar as partes mostra onde um controle pode agir, como trocar a senha compartilhada por contas nominais. As contas nominais tratam a vulnerabilidade, enquanto o registro das sessões ajudaria a detectar o evento de ameaça se a vulnerabilidade voltasse.

### 15.3 Tipos de controle

Os controles podem prevenir, detectar ou corrigir, e podem ser administrativos, técnicos ou físicos. Nadia classifica os controles da Ardwell para o acesso de fornecedores: as contas nominais e a aprovação são preventivas; o registro das sessões é detectivo; um procedimento testado para revogar o acesso durante um incidente é corretivo. Ela aprende que depender de um só tipo é frágil, porque a prevenção acaba falhando. Um conjunto equilibrado permite à Ardwell barrar a maioria dos problemas, perceber o restante e se recuperar, que é a base da defesa em profundidade. O procedimento de revogação só conta se tiver sido testado, porque um procedimento não testado pode falhar justamente no incidente para o qual foi escrito.

### Exemplo resolvido

Nadia ordena os objetivos de segurança por ativo, decompõe o risco do acesso de fornecedores com os termos do SP 800-30 e equilibra controles preventivos, detectivos e corretivos.

> **Caso sintético.** Os ativos e os controles são sintéticos; o SP 800-30 Rev. 1 é real.

### Erros e limites

A ordem dos objetivos pode ser contestada. Na prática, as classificações se confundem.

### Exercícios

- **EX043 — Prioridade dos medidores.** Que objetivo importa mais para as leituras dos medidores? *Rubrica:* 3 = integridade;; 2 = integridade;; 1 = confidencialidade;; 0 = nenhuma.
- **EX044 — Partes do risco.** Que vulnerabilidade Nadia identificou no acesso de fornecedores? *Rubrica:* 3 = uma senha compartilhada;; 2 = senha compartilhada;; 1 = nada;; 0 = nenhuma.
- **EX045 — Exemplo corretivo.** Dê o controle corretivo do acesso de fornecedores. *Rubrica:* 3 = procedimento testado para revogar o acesso durante incidentes;; 2 = revogar;; 1 = nada;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) tratar o programa de governança como um sistema com requisitos e interfaces; (2) rastrear os requisitos até controles e testes; (3) gerenciar o ciclo de vida do sistema.

### 16.1 O programa como sistema

A engenharia de sistemas trata esforços complexos como sistemas com finalidades, componentes, interfaces e ciclos de vida. Nadia aplica essa visão ao programa de governança da Ardwell. Sua finalidade é manter o risco dentro do apetite do conselho e demonstrar compliance. Seus componentes incluem políticas, o registro de riscos, os responsáveis pelos controles, o monitoramento e as auditorias. As interfaces o ligam a finanças, operações e reguladores. Ver a governança como sistema a ajuda a fazer perguntas de engenharia, como o que acontece quando um componente falha ou uma interface muda. Se o conselho muda o apetite, a interface com o monitoramento também precisa mudar, ou os relatórios medirão contra uma meta antiga.

### 16.2 Rastreabilidade

Uma ferramenta central da engenharia de sistemas é a matriz de rastreabilidade. Nadia liga cada requisito de governança, vindo de lei, contrato ou norma, aos controles que o atendem e aos testes que mostram que funcionam. As lacunas aparecem como requisitos sem controle ou controles sem teste. Ela reconhece aí o mesmo problema de cobertura estudado no mapeamento de compliance. A rastreabilidade permite à Ardwell responder depressa à pergunta de um auditor sobre qualquer requisito e mostra aos gestores que controles existem só para atender obrigações que podem ter caducado; um requisito cuja fonte legal caducou aparece na matriz como um controle mantido por hábito.

### 16.3 Ciclo de vida

Os sistemas têm ciclos de vida: concepção, desenvolvimento, operação, manutenção e desativação. Os componentes de governança também. As políticas são redigidas, aprovadas, usadas, revisadas e retiradas. Os controles são desenhados, implementados, testados e, um dia, substituídos. Nadia observa que a desativação costuma ser esquecida; controles e políticas antigos continuam no papel muito depois de deixarem de funcionar. O NIST SP 800-37 Rev. 2 enquadra a gestão de riscos como contínua ao longo do ciclo de vida, e ela adota sua ênfase no monitoramento como a etapa que mantém o sistema honesto. Uma revisão de acessos que ainda lista um sistema de faturamento desativado é um controle além do seu ponto de desativação.

### Exemplo resolvido

Nadia modela a governança como sistema, monta um rastreio de requisito a controle e a teste e planeja a gestão do ciclo de vida, incluindo a desativação.

> **Caso sintético.** O programa da Ardwell é sintético; o SP 800-37 Rev. 2 é real.

### Erros e limites

As visões sistêmicas podem virar burocracia. A rastreabilidade exige manutenção.

### Exercícios

- **EX046 — Finalidade do programa.** Qual é a finalidade do programa de governança da Ardwell visto como sistema? *Rubrica:* 3 = manter o risco dentro do apetite e demonstrar compliance;; 2 = finalidade;; 1 = nada;; 0 = nenhuma.
- **EX047 — Lacunas do rastreio.** Que lacunas uma matriz de rastreabilidade revela? *Rubrica:* 3 = requisitos sem controles e controles sem testes;; 2 = lacunas;; 1 = nada;; 0 = nenhuma.
- **EX048 — Etapa esquecida.** Que etapa do ciclo de vida costuma ser esquecida em controles e políticas? *Rubrica:* 3 = a desativação;; 2 = desativação;; 1 = desenho;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) descrever a governança como uma malha de realimentação; (2) identificar sensores, setpoints e atuadores num sistema de gestão; (3) reconhecer atrasos e oscilações nas respostas de governança.

### 17.1 Governança como realimentação

Na engenharia de controle, um sistema mede sua saída, compara-a com um setpoint e ajusta a entrada para reduzir a diferença. Nadia vê a mesma malha na governança. O conselho da Ardwell fixa o apetite a riscos como setpoint. O monitoramento e os indicadores-chave de risco atuam como sensores. As decisões sobre orçamentos, controles e prioridades atuam como atuadores. A ISO/IEC 27001:2022 incorpora essa malha em seus requisitos de monitoramento, auditoria interna, análise crítica pela direção e melhoria contínua, para que o sistema de gestão se corrija com o tempo. Nessa malha, a auditoria interna e a análise crítica são as etapas que comparam o risco medido com o setpoint do conselho.

### 17.2 Atrasos

Malhas de realimentação com atrasos longos se comportam mal. Se a Ardwell mede o desempenho dos controles uma vez por ano, os problemas crescem por meses antes de alguém reagir, e as ações corretivas chegam tarde. Nadia modela uma malha simples em que um backlog de achados é revisado trimestral ou anualmente e vê que a malha anual deixa o backlog oscilar muito mais longe da meta. Ela aprende que medir mais depressa não garante um controle melhor, mas medir devagar quase garante um controle ruim, sobretudo quando os riscos mudam rápido. O Prof. Brenner acrescenta que a revisão trimestral só ajuda se as decisões também forem trimestrais; um sensor rápido com um atuador lento continua atrasado.

### 17.3 Reação exagerada

Uma resposta forte demais também causa problemas. Depois de uma auditoria ruim, a gestão pode impor controles rígidos em toda parte, provocando contornos e queixas, depois afrouxá-los e depois apertá-los de novo. Os engenheiros chamam isso de oscilação. Nadia sugere respostas proporcionais ao tamanho da lacuna e à importância do ativo. O Prof. Brenner observa que a boa governança busca uma melhoria constante, e não oscilações dramáticas, e que regras de decisão documentadas ajudam os gestores a responder de forma consistente, em vez de reagir à última manchete ou ao último relatório de auditoria. Uma regra como apertar os controles só para ativos acima de uma criticidade definida amorteceria as oscilações.

### Exemplo resolvido

Nadia mapeia o apetite, os indicadores e as decisões numa malha de realimentação e mostra como atrasos e reações exageradas degradam a governança.

> **Caso sintético.** Os modelos são ilustrativos; a ISO/IEC 27001:2022 é real.

### Erros e limites

As organizações não são sistemas lineares. Os indicadores podem ser manipulados.

### Exercícios

- **EX049 — Setpoint.** O que atua como setpoint na malha de governança da Ardwell? *Rubrica:* 3 = o apetite a riscos do conselho;; 2 = apetite;; 1 = nada;; 0 = nenhuma.
- **EX050 — Malha anual.** O que aconteceu com o backlog quando revisado anualmente em vez de trimestralmente? *Rubrica:* 3 = oscilou para mais longe da meta;; 2 = oscilações maiores;; 1 = nada;; 0 = nenhuma.
- **EX051 — Remédio para a oscilação.** O que ajuda os gestores a evitar respostas oscilantes? *Rubrica:* 3 = regras de decisão proporcionais e documentadas;; 2 = regras;; 1 = nada;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) traduzir requisitos de governança em princípios de arquitetura; (2) revisar uma arquitetura contra eles; (3) registrar as decisões de arquitetura para auditoria.

### 18.1 Princípios a partir dos requisitos

Nadia aprende que a arquitetura transforma requisitos em estrutura. Os requisitos de governança da Ardwell incluem manter os dados de pagamento num segmento pequeno, separar os sistemas de controle dos sistemas do escritório e controlar o acesso dos fornecedores. Ela escreve princípios de arquitetura a partir deles: minimizar o escopo dos dados sensíveis, separar as zonas por nível de confiança, intermediar todo acesso externo por pontos monitorados e projetar para a recuperação. Os princípios dão aos arquitetos uma base para as escolhas e aos auditores um modo de conferir se os projetos seguem a política. O princípio de intermediar o acesso externo, por exemplo, exclui diretamente a conexão direta de fornecedor encontrada antes.

### 18.2 Revisão de arquitetura

Nadia participa da revisão de uma nova plataforma proposta para os dados de medição e a confere contra cada princípio. O projeto guarda os nomes dos clientes junto com as leituras dos medidores num serviço em nuvem acessível pelos notebooks do escritório, o que amplia o escopo dos dados pessoais e cria um novo caminho até um repositório sensível. Ela recomenda pseudonimizar as leituras e restringir o acesso a uma zona de análise, o que preserva o valor analítico e tira os nomes do repositório alcançável pelos notebooks. A revisão registra cada preocupação, a resposta do arquiteto e a decisão final, para que o resultado possa ser rastreado depois.

### 18.3 Registros de decisão

A Ardwell adota registros curtos de decisões de arquitetura: o contexto, a decisão, as alternativas consideradas e as consequências, incluindo os riscos aceitos. Nadia escreve um para a plataforma de medição, que lista manter os nomes com as leituras como alternativa rejeitada e a pseudonimização como a escolhida. Ela aprende que os registros de decisão ajudam os auditores a ver que os riscos foram considerados, e não ignorados, e ajudam futuros engenheiros a entender por que algo é como é. Sem eles, as organizações repetem debates antigos ou desfazem boas decisões porque ninguém lembra os motivos por trás delas.

### Exemplo resolvido

Nadia deriva quatro princípios de arquitetura, revisa contra eles o projeto de uma plataforma de medição e registra a decisão com as alternativas.

> **Caso sintético.** A plataforma e as decisões são sintéticas.

### Erros e limites

Os princípios podem entrar em conflito. Registros de decisão longos demais ficam sem leitura.

### Exercícios

- **EX052 — Lista de princípios.** Cite dois princípios de arquitetura de Nadia. *Rubrica:* 3 = minimizar o escopo dos dados sensíveis; intermediar o acesso externo;; 2 = princípios;; 1 = nada;; 0 = nenhuma.
- **EX053 — Problema da plataforma.** O que havia de errado no projeto da plataforma de medição? *Rubrica:* 3 = nomes guardados com as leituras, acessíveis pelos notebooks do escritório;; 2 = escopo;; 1 = nada;; 0 = nenhuma.
- **EX054 — Conteúdo do registro.** O que contém um registro de decisão de arquitetura? *Rubrica:* 3 = contexto, decisão, alternativas e consequências;; 2 = quatro partes;; 1 = nada;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) governar as identidades ao longo do ciclo de vida; (2) relacionar os controles criptográficos à política; (3) gerenciar as chaves como ativos governados.

### 19.1 Ciclo de vida das identidades

Na Ardwell, as identidades são criadas quando os funcionários entram, mudam quando eles trocam de função e precisam terminar quando eles saem. Nadia mapeia esse processo de admissão, movimentação e desligamento e descobre que a movimentação é o ponto fraco: os novos acessos são concedidos depressa, mas os antigos raramente são removidos. Ela propõe que o sistema de recursos humanos dispare automaticamente as mudanças de acesso e que os gestores confirmem os acessos de quem mudou de função em até duas semanas. Governar identidades é, sobretudo, governar essas transições, onde nasce a maior parte do acesso excessivo; quem muda de função e mantém o acesso antigo ao faturamento acumula direitos que nenhum papel concederia.

### 19.2 Criptografia e política

Nadia estuda como a criptografia protege dados em repouso e em trânsito e como as assinaturas digitais protegem a integridade. Ela as liga à política: a classificação de dados da Ardwell exige criptografia para os dados de pagamento dos clientes e para os dados pessoais em notebooks. A ISO/IEC 27002:2022 inclui um controle sobre o uso de criptografia que espera regras para esse uso e para a gestão de chaves. Ela aprende que a criptografia só é tão forte quanto as decisões de política sobre onde usá-la e como gerenciá-la. Para os notebooks, a política decide que a criptografia é obrigatória, e as regras de gestão de chaves decidem quem pode recuperar um aparelho bloqueado.

### 19.3 Chaves como ativos

As chaves precisam ser geradas, guardadas, trocadas e destruídas sob controle. Nadia lista as chaves importantes da Ardwell, incluindo os certificados do portal de pagamento, e encontra um certificado administrado por um único engenheiro, sem backup nem controle de vencimento. Se ele vencesse sem ninguém notar, o portal pararia. Ela registra num inventário o responsável, a data de vencimento e o arranjo de backup de cada chave. Aprende que as falhas de gestão de chaves costumam ser falhas de governança, como a falta de um responsável, e não fraquezas da própria criptografia. Com as datas de vencimento no inventário, o certificado do portal pode ser renovado antes que os clientes vejam uma falha.

### Exemplo resolvido

Nadia fecha a lacuna da movimentação com gatilhos automáticos, liga a criptografia à classificação e inventaria as chaves com responsáveis e datas de vencimento.

> **Caso sintético.** As identidades, as chaves e os processos são sintéticos; a ISO/IEC 27002:2022 é real.

### Erros e limites

A automação falha quando os dados de RH estão errados. Os inventários de chaves ficam desatualizados.

### Exercícios

- **EX055 — Transição frágil.** Que transição de identidade é o ponto fraco da Ardwell? *Rubrica:* 3 = a movimentação;; 2 = quem muda de função;; 1 = desligamento;; 0 = nenhuma.
- **EX056 — Regra de criptografia.** Que dados a classificação da Ardwell exige criptografar? *Rubrica:* 3 = dados de pagamento e dados pessoais em notebooks;; 2 = classificação;; 1 = nada;; 0 = nenhuma.
- **EX057 — Risco do certificado.** Por que o certificado de um único engenheiro era um risco? *Rubrica:* 3 = sem backup nem controle de vencimento, poderia vencer sem ninguém notar;; 2 = responsável;; 1 = nada;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Governança, riscos e compliance de segurança: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) definir governança, gestão de riscos e compliance e como se relacionam; (2) situá-las na organização da Ardwell; (3) identificar as obrigações que moldam o programa.

### 20.1 Três disciplinas relacionadas

Nadia começa agora as disciplinas centrais de GRC. A governança define direção, responsabilização e supervisão: quem decide, qual é o apetite a riscos e como o desempenho é monitorado. A gestão de riscos identifica, analisa, avalia e trata os riscos, seguindo um processo como o descrito na ISO 31000:2018, adotada no Brasil como ABNT NBR ISO 31000:2018. O compliance garante que a organização cumpra as obrigações vindas de leis, regulamentos, contratos e normas adotadas. As três se sobrepõem, mas diferem. O COBIT 2019 separa a governança, que avalia, direciona e monitora, da gestão, que planeja, constrói, executa e monitora. Na Ardwell, a revisão trimestral dos relatórios pelo conselho é governança no sentido do COBIT; o gestor de segurança que conduz o processo de riscos faz gestão.

### 20.2 Lugar na organização

Na Ardwell, o conselho aprova o apetite a riscos e recebe relatórios trimestrais. Um gestor de segurança da informação conduz o processo de riscos e se reporta ao diretor de operações. As obrigações de compliance ficam com uma responsável jurídica e de compliance, enquanto a auditoria interna dá garantia independente ao comitê de auditoria do conselho. Nadia desenha essas relações e observa que linhas de reporte claras evitam conflitos de interesse, como a pessoa que opera os controles também julgar se eles funcionam, o que enfraqueceria a garantia. É o reporte da auditoria interna ao comitê de auditoria, e não ao diretor de operações, que mantém sua garantia independente.

### 20.3 Obrigações

Nadia lista as obrigações da Ardwell. Os pagamentos com cartão trazem o PCI DSS v4.0, por meio dos contratos com o banco. Os dados pessoais dos clientes trazem a legislação de proteção de dados. Como distribuidora de energia, a Ardwell enfrenta regras setoriais de resiliência e de comunicação de incidentes. O conselho também escolheu se alinhar à ISO/IEC 27001:2022 e usar o NIST CSF 2.0 nos relatórios. Ela separa as obrigações compulsórias das escolhas voluntárias, porque as penalidades e a flexibilidade diferem, e registra a fonte e o responsável de cada uma num registro de obrigações. Como o PCI DSS v4.0 chega pelo contrato com o banco, seu responsável precisa ser alguém que administre essa relação contratual.

### Exemplo resolvido

Nadia define governança, gestão de riscos e compliance, mapeia as linhas de reporte da Ardwell e monta um registro de obrigações.

> **Caso sintético.** A estrutura da Ardwell é sintética; a ISO 31000:2018 (ABNT NBR ISO 31000:2018), o COBIT 2019, o PCI DSS v4.0 e o CSF 2.0 são reais.

### Erros e limites

As obrigações legais precisam de revisão jurídica. Os papéis variam entre organizações.

### Exercícios

- **EX058 — Papel da governança.** O que a governança define? *Rubrica:* 3 = direção, responsabilização e supervisão;; 2 = direção;; 1 = nada;; 0 = nenhuma.
- **EX059 — Independência.** Por que quem opera os controles não deve julgar se eles funcionam? *Rubrica:* 3 = cria um conflito de interesses que enfraquece a garantia;; 2 = independência;; 1 = nada;; 0 = nenhuma.
- **EX060 — Compulsório ou voluntário.** O alinhamento da Ardwell à ISO/IEC 27001:2022 é compulsório? *Rubrica:* 3 = não, é uma escolha do conselho;; 2 = voluntário;; 1 = compulsório;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060 (as de EX061–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Nadia Okafor, o Prof. Tomas Brenner, a Kestrel Polytechnic, a Ardwell Power Cooperative e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Se o backlog de achados em aberto está diminuindo, estável ou crescendo.

**EX002.** Porque ali a atenção da gestão diminui e os achados mais difíceis ficam parados.

**EX003.** Como a área sob a curva das fraquezas em aberto ao longo do tempo.

**EX004.** Autenticação multifator obrigatória para sessões remotas e acesso imediato de fornecedores em emergências.

**EX005.** Sete, de funcionários que tinham mudado de função.

**EX006.** Cadastrar fornecedor junto com aprovar pagamento (ou aprovar pagamento com conciliar banco).

**EX007.** Controles físicos, ao lado dos organizacionais, de pessoas e tecnológicos.

**EX008.** Facilities, trabalhando com TI.

**EX009.** Porque as fechaduras só retardam, e é preciso detecção contra um atacante determinado.

**EX010.** Título, responsável, data de aprovação e data da próxima revisão.

**EX011.** Porque um responsável consegue corrigir uma política nomeada, mas não consegue agir sobre um número sem explicação.

**EX012.** Porque, quando os scripts produzem evidências de compliance, o próprio script é evidência que os auditores precisam entender.

**EX013.** Decisões, opções e consequências em linguagem simples.

**EX014.** Para dizer que a perda anual esperada é de cerca de noventa mil sob premissas declaradas, com uma faixa ampla.

**EX015.** Porque as decisões de governança afetam muitas equipes e o memorando registra como a decisão foi tomada.

**EX016.** Funcionários que mudam de função sem que seus acessos sejam atualizados.

**EX017.** Departamentos com alta rotatividade de pessoal, onde o decaimento é mais rápido.

**EX018.** Porque o dinheiro tem valor no tempo, então os valores futuros são descontados.

**EX019.** A taxa anual de ocorrência multiplicada pela expectativa de perda única.

**EX020.** Ransomware, com 90.000, e mau uso do acesso de fornecedores, com 80.000.

**EX021.** Porque é raro, mas uma única ocorrência poderia ser catastrófica, algo que a média esconde.

**EX022.** Os dispositivos do sistema de controle nas subestações, junto com seu firmware.

**EX023.** Porque roda primeiro e pode contornar os controles do sistema operacional.

**EX024.** Substituí-los, isolá-los ou aceitar o risco com monitoramento compensatório.

**EX025.** Um para ler os dados, outro para aplicar as regras e outro para escrever os relatórios.

**EX026.** Porque uma linha pulada poderia esconder um risco sem responsável.

**EX027.** A data da execução, a versão do script e um resumo do arquivo de entrada.

**EX028.** Assumir a responsabilidade por sua exatidão.

**EX029.** Monitoramento e alertas sobre falhas repetidas, com restrição física do acesso à sala de controle.

**EX030.** Porque uma cultura que pune más notícias empurra os problemas para fora da vista até que causem danos.

**EX031.** Zonas do escritório corporativo, de pagamento dos clientes, do sistema de controle e de acesso remoto de fornecedores.

**EX032.** Porque contornava o jump host, então as sessões ficavam sem registro e sem aprovação.

**EX033.** Depois de mudanças, porque uma única regra nova de firewall pode ligar zonas.

**EX034.** Que o sistema operacional imponha contas de administrador separadas e registre seu uso em logs que os usuários não conseguem alterar.

**EX035.** Cada desvio é registrado com seu motivo.

**EX036.** Com que rapidez o desvio é detectado e corrigido.

**EX037.** Todo risco tem responsável, as revisões não têm mais de 180 dias e as notas ficam entre 1 e 25.

**EX038.** Duas.

**EX039.** Edições descuidadas ou falsificadas poderiam fazer riscos parecerem menores sem que ninguém percebesse.

**EX040.** ISO/IEC 27002:2022 e PCI DSS v4.0.

**EX041.** Um caminho emergencial documentado, com revisão posterior em até dois dias úteis.

**EX042.** Porque cada uma é um fornecedor cujas vulnerabilidades e obrigações de licença se tornam risco da Ardwell.

**EX043.** Integridade, porque as leituras geram as contas.

**EX044.** Uma senha compartilhada do fornecedor.

**EX045.** Um procedimento testado para revogar o acesso de fornecedores durante um incidente.

**EX046.** Manter o risco dentro do apetite do conselho e demonstrar compliance.

**EX047.** Requisitos sem controle e controles sem teste.

**EX048.** A desativação.

**EX049.** O apetite a riscos do conselho.

**EX050.** Oscilou muito mais longe da meta, por causa do atraso maior.

**EX051.** Respostas proporcionais, guiadas por regras de decisão documentadas.

**EX052.** Por exemplo, minimizar o escopo dos dados sensíveis e intermediar todo acesso externo por pontos monitorados.

**EX053.** Guardava os nomes dos clientes com as leituras num serviço alcançável pelos notebooks do escritório, ampliando o escopo dos dados sensíveis.

**EX054.** O contexto, a decisão, as alternativas consideradas e as consequências, incluindo os riscos aceitos.

**EX055.** A movimentação, porque os acessos antigos raramente são removidos.

**EX056.** Os dados de pagamento dos clientes e os dados pessoais em notebooks.

**EX057.** Porque não tinha backup nem controle de vencimento e poderia vencer sem ninguém notar, derrubando o portal.

**EX058.** Direção, responsabilização e supervisão, incluindo o apetite a riscos.

**EX059.** Porque isso cria um conflito de interesses e enfraquece a garantia.

**EX060.** Não; é uma escolha voluntária do conselho, ao contrário das obrigações contratuais do PCI DSS.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO 31000:2018 e da ABNT NBR ISO/IEC 27001:2022, citadas nesta edição como referências brasileiras e conferidas em suas fontes oficiais; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Associação Brasileira de Normas Técnicas. (2018). *ABNT NBR ISO 31000:2018 — Gestão de riscos — Diretrizes*. ABNT. <https://www.abntcatalogo.com.br/>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Cox, L. A., Jr. (2008). What's wrong with risk matrices? *Risk Analysis*, 28(2), 497–512. <https://doi.org/10.1111/j.1539-6924.2008.01030.x>
- Freund, J., & Jones, J. (2015). *Measuring and managing information risk: A FAIR approach*. Butterworth-Heinemann. <https://doi.org/10.1016/C2013-0-09966-5>
- Gordon, L. A., & Loeb, M. P. (2002). The economics of information security investment. *ACM Transactions on Information and System Security*, 5(4), 438–457. <https://doi.org/10.1145/581271.581274>
- Hubbard, D. W., & Seiersen, R. (2016). *How to measure anything in cybersecurity risk*. Wiley. <https://doi.org/10.1002/9781119162315>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- International Organization for Standardization. (2022c). *ISO/IEC 27005:2022 Information security, cybersecurity and privacy protection — Guidance on managing information security risks*. <https://www.iso.org/standard/80585.html>
- ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. ISACA. <https://www.isaca.org/resources/cobit>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Joint Task Force. (2018). *Risk management framework for information systems and organizations: A system life cycle approach for security and privacy* (NIST SP 800-37 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-37r2>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
- Spears, J. L., & Barki, H. (2010). User participation in information systems security risk management. *MIS Quarterly*, 34(3), 503–522. <https://doi.org/10.2307/25750689>
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
