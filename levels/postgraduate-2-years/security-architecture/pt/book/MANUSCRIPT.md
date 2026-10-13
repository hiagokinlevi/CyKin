# Arquitetura e Engenharia de Segurança: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 145, curso de pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: arquitetos e engenheiros em atividade que lideram decisões de arquitetura de segurança em escala organizacional.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios calculam a alcançabilidade entre zonas, notas ponderadas de opções com uma varredura de sensibilidade, contagens por nível de garantia e comparações de rubricas sobre dados sintéticos; nada toca uma rede real. Projetos de produção usam produtos e normas avaliados; nunca crie sua própria criptografia. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma arquiteta pós-graduanda numa rede regional de clínicas: tomada de decisão, prática atual e evidências especializadas; risco e ética, alternativas de desenho e um piloto controlado; integração organizacional, casos difíceis e garantia; crítica de pesquisas, um projeto aplicado e a transferência final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Priya Ramanathan** | Estudante de pós-graduação e arquiteta de segurança líder | Inventada |
| **Dra. Elena Voss** | Orientadora | Inventada |
| **Brookmere University** | Universidade fictícia | Inventada |
| **Corvane Health Network** | Rede fictícia de 22 clínicas comunitárias | Inventada |
| **Hollin Care** | Grupo fictício de clínicas adquirido | Inventado |

### Fontes principais

NIST [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-160 Vol. 1 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1), [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1), [SP 800-37 Rev. 2](https://doi.org/10.6028/NIST.SP.800-37r2) e [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5); ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); Sherwood, Clark e Lynas, *Enterprise Security Architecture* (SABSA, 2005); Shostack, *Threat Modeling* (2014). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem

Você vai (1) enquadrar uma decisão de arquitetura em escala organizacional; (2) separar fatos, premissas e valores; (3) registrar uma decisão de modo que outros possam contestá-la.

### 1.1 A decisão na Corvane

Priya Ramanathan é estudante de pós-graduação e arquiteta de segurança líder na Corvane Health Network, um grupo fictício de vinte e duas clínicas comunitárias. Sua orientadora, a Dra. Elena Voss, da fictícia Brookmere University, pede que ela traga ao curso uma decisão real em andamento. A Corvane precisa decidir se consolida as redes das clínicas atrás de um único serviço de acesso baseado em nuvem ou se mantém o firewall local e a VPN de cada clínica. A escolha afeta os dados dos pacientes, a disponibilidade das clínicas, o fluxo de trabalho da equipe e o orçamento por cinco anos, então é uma decisão em escala organizacional, e não um detalhe de projeto.

### 1.2 Fatos, premissas e valores

Priya divide seu briefing em três colunas. Fatos são coisas que ela pode verificar: vinte e duas clínicas, quatro modelos de firewall, duas indisponibilidades no ano passado causadas por certificados de VPN expirados. Premissas são crenças que ela ainda não consegue verificar, como a de que o serviço em nuvem atenderá às metas de disponibilidade em áreas rurais com conectividade ruim. Valores são prioridades que o conselho precisa definir, como quanto tempo de indisponibilidade das clínicas é aceitável para economizar dinheiro. Misturar essas três coisas é a causa mais comum de discussões circulares em reuniões de arquitetura, porque as pessoas discutem valores enquanto parecem discutir fatos.

### 1.3 Registrar a decisão

Priya escreve um registro de decisão de arquitetura (architecture decision record): contexto, opções consideradas, critérios, a decisão, as consequências e as condições que fariam a decisão ser revisitada. Ela cita os princípios de zero trust do NIST SP 800-207 como direção de projeto, mas observa que eles não ditam nenhum produto. O registro é curto, datado e assinado pelo diretor de tecnologia da informação. Dois anos depois, um novo arquiteto consegue ler por que a escolha foi feita e julgar se suas condições ainda valem, em vez de adivinhar o raciocínio ou repetir todo o debate.

### Exemplo resolvido

Priya enquadra a decisão sobre a rede das clínicas, organiza seu briefing em fatos, premissas e valores e a registra num registro de decisão com condições de revisão.

> **Caso sintético.** A Corvane, a Brookmere e todas as pessoas são sintéticas; o SP 800-207 é real.

### Erros e limites

Os registros de decisão podem virar burocracia se ninguém os lê. As premissas precisam ser testadas, e não apenas listadas.

### Exercícios

- **EX001 — Teste de escala organizacional.** Por que a escolha da rede das clínicas é uma decisão em escala organizacional? *Rubrica:* 3 = afeta dados dos pacientes, disponibilidade, fluxo de trabalho e orçamento por cinco anos em todas as clínicas;; 2 = vários efeitos;; 1 = é técnica;; 0 = nenhuma.

- **EX002 — Exemplo de premissa.** Dê a premissa que Priya ainda não conseguia verificar. *Rubrica:* 3 = disponibilidade do serviço em nuvem em clínicas rurais com conectividade ruim;; 2 = disponibilidade;; 1 = indisponibilidades por certificados;; 0 = nenhuma.

- **EX003 — Valor para o conselho.** Que valor Priya deixou para o conselho? *Rubrica:* 3 = quanto tempo de indisponibilidade das clínicas é aceitável para economizar dinheiro;; 2 = indisponibilidade;; 1 = modelos de firewall;; 0 = nenhuma.

- **EX004 — Discussões circulares.** Segundo o capítulo, o que causa discussões circulares de arquitetura? *Rubrica:* 3 = misturar fatos, premissas e valores;; 2 = misturar;; 1 = orçamento;; 0 = nenhuma.

- **EX005 — Condições de revisão.** Por que incluir condições de revisão num registro de decisão? *Rubrica:* 3 = para que um arquiteto posterior possa julgar se a decisão ainda vale;; 2 = revisão futura;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Arquitetura e engenharia de segurança: prática atual

### Objetivos de aprendizagem

Você vai (1) levantar a prática atual de arquitetura na área da saúde; (2) compará-la com as orientações publicadas; (3) identificar lacunas na prática da Corvane.

### 2.1 O que os profissionais fazem

Priya entrevista arquitetos de três organizações de saúde pares, todas anonimizadas para o curso. Eles compartilham padrões: acesso da equipe centrado em identidade, segmentação de rede que separa os dispositivos clínicos, acesso remoto de fornecedores por sessões intermediadas (brokered) e comitês de revisão de arquitetura para novos sistemas. Nenhum usa por inteiro métodos formais como o SABSA; todos aproveitam partes, como os perfis de atributos de negócio. Ela observa que a prática é moldada por equipes pequenas, por dispositivos médicos legados que não podem receber patches e por reguladores que esperam decisões de risco documentadas, e não projetos específicos.

### 2.2 Comparar com as orientações

Priya mapeia a prática observada contra o NIST SP 800-160 Vol. 1 Rev. 1, que descreve a engenharia de segurança de sistemas ao longo do ciclo de vida, e contra a ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022), que exige um sistema de gestão da segurança da informação. A prática se alinha bem em controle de acesso e gestão de fornecedores, mas é fraca em verificação: a maioria das organizações revisa os projetos antes da construção, mas raramente testa se os sistemas entregues correspondem a esses projetos. As orientações esperam a verificação como uma atividade do ciclo de vida. A lacuna importa porque a deriva não detectada entre o projeto e a realidade é onde muitos incidentes começam.

### 2.3 As lacunas da Corvane

Aplicando a comparação à Corvane, Priya encontra a mesma fraqueza de verificação e mais duas. Em nove clínicas, os dispositivos clínicos compartilham a rede com notebooks administrativos, e as revisões de arquitetura não têm registro de quais riscos foram aceitos. Ela as ordena por consequência: primeiro a segmentação dos dispositivos, porque uma infecção num notebook poderia alcançar as estações de gerenciamento das bombas de infusão; depois a verificação; depois os registros de riscos aceitos. Ela apresenta a ordenação com as fontes, para que o diretor de tecnologia da informação veja que as lacunas são medidas contra orientações reconhecidas, e não apenas contra a opinião dela.

### Exemplo resolvido

Priya compara a prática anonimizada dos pares com o SP 800-160v1r1 e a ISO/IEC 27001 (no Brasil, ABNT NBR ISO/IEC 27001), encontra uma lacuna comum de verificação e ordena três lacunas na Corvane.

> **Caso sintético.** As entrevistas e os detalhes da Corvane são sintéticos; o SP 800-160 Vol. 1 Rev. 1 e a ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) são reais.

### Erros e limites

Três entrevistas não representam um setor. O alinhamento às orientações não é prova de segurança.

### Exercícios

- **EX006 — Padrão comum.** Cite dois padrões que as três organizações pares compartilham. *Rubrica:* 3 = acesso centrado em identidade, segmentação de dispositivos, acesso intermediado de fornecedores, comitês de revisão;; 2 = um;; 1 = nenhuma;; 0 = nenhuma.

- **EX007 — Uso do SABSA.** Como os pares usam o SABSA? *Rubrica:* 3 = aproveitam partes, como os perfis de atributos, e não o método completo;; 2 = partes;; 1 = método completo;; 0 = nenhuma.

- **EX008 — Lacuna de verificação.** Que lacuna de verificação Priya encontrou na prática? *Rubrica:* 3 = os sistemas entregues raramente são testados contra seus projetos;; 2 = testes;; 1 = revisões de projeto;; 0 = nenhuma.

- **EX009 — Primeira prioridade.** Por que ordenar a segmentação dos dispositivos em primeiro lugar na Corvane? *Rubrica:* 3 = uma infecção num notebook poderia alcançar as estações de gerenciamento das bombas de infusão;; 2 = segurança do paciente;; 1 = custo;; 0 = nenhuma.

- **EX010 — Por que citar fontes.** Por que Priya apresentou as lacunas com fontes? *Rubrica:* 3 = para que sejam vistas como medidas contra orientações, e não como opinião;; 2 = credibilidade;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Arquitetura e engenharia de segurança: evidências especializadas

### Objetivos de aprendizagem

Você vai (1) reunir evidências especializadas sobre o risco dos dispositivos clínicos; (2) modelar a alcançabilidade entre zonas de rede; (3) apresentar evidências proporcionais à decisão.

### 3.1 Fontes especializadas

Para a lacuna de segmentação, Priya precisa de evidências além das orientações gerais. Ela lê a documentação de segurança do fabricante das estações de gerenciamento das bombas de infusão da Corvane, o inventário da equipe de engenharia clínica e as regras de firewall da equipe de redes. Os engenheiros clínicos sabem quais dispositivos não podem receber patches e de quais conexões de fornecedores eles precisam. Esse conhecimento é uma evidência especializada que os arquitetos muitas vezes não têm. Ela registra cada fonte, seu responsável e sua data, porque os inventários de dispositivos na saúde são notoriamente incompletos e ela precisa mostrar quão atual é o seu retrato.

### 3.2 Modelar a alcançabilidade

Priya constrói um pequeno modelo de quais zonas conseguem alcançar quais outras sob as regras atuais e depois o repete sob as regras propostas. O laboratório abaixo calcula a alcançabilidade nos dois casos. Sob as regras atuais, a zona dos notebooks administrativos consegue alcançar a zona dos dispositivos clínicos por meio de um servidor de impressão compartilhado. Sob as regras propostas, apenas o jump host da engenharia clínica consegue alcançar os dispositivos clínicos. O modelo é simples, mas transforma uma longa exportação de firewall numa afirmação clara que um tomador de decisão consegue acompanhar e conferir.

### Laboratório — Alcançabilidade entre zonas antes e depois da segmentação

```python
# Zone reachability before and after segmentation (synthetic rules).
def reach(rules, start):
    seen, todo = {start}, [start]
    while todo:
        z = todo.pop()
        for a, b in rules:
            if a == z and b not in seen: seen.add(b); todo.append(b)
    return sorted(seen - {start})
current = [("admin", "print"), ("print", "clinical"), ("admin", "internet"), ("jump", "clinical"), ("clinical", "print")]
proposed = [("admin", "print"), ("admin", "internet"), ("jump", "clinical")]
for name, rules in [("current", current), ("proposed", proposed)]:
    print(f"{name}: admin reaches {reach(rules, 'admin')}; jump reaches {reach(rules, 'jump')}")
```

Execute com `python3 lab_reach.py`. Saída verificada:

```text
current: admin reaches ['clinical', 'internet', 'print']; jump reaches ['clinical', 'print']
proposed: admin reaches ['internet', 'print']; jump reaches ['clinical']
```

### 3.3 Evidências proporcionais

Priya resiste à vontade de levar todos os detalhes ao conselho. Ela apresenta o resultado da alcançabilidade, a contagem de clínicas afetadas e a visão dos engenheiros clínicos sobre o impacto operacional. As regras detalhadas de firewall vão para um apêndice destinado aos revisores técnicos. As evidências são proporcionais: o bastante para justificar a decisão e mostrar seus limites, e não tanto que a decisão se perca. A Dra. Voss observa que a proporção é uma habilidade profissional, porque sobrecarregar os tomadores de decisão com detalhes é uma forma de evitar a responsabilidade por uma recomendação clara.

### Exemplo resolvido

Priya reúne evidências de dispositivos e de firewall com especialistas, modela a alcançabilidade antes e depois da segmentação e apresenta uma síntese proporcional.

> **Caso sintético.** Os dispositivos, as zonas e as regras são sintéticos.

### Erros e limites

Os inventários deixam dispositivos de fora. Os modelos de alcançabilidade ignoram caminhos na camada de aplicação não capturados nas regras.

### Exercícios

- **EX011 — Conhecimento especializado.** O que os engenheiros clínicos sabiam que os arquitetos muitas vezes não sabem? *Rubrica:* 3 = quais dispositivos não podem receber patches e de quais conexões de fornecedores precisam;; 2 = dispositivos;; 1 = nada;; 0 = nenhuma.

- **EX012 — Caminho atual.** Como os notebooks administrativos conseguiam alcançar os dispositivos clínicos sob as regras atuais? *Rubrica:* 3 = pelo servidor de impressão compartilhado;; 2 = servidor de impressão;; 1 = diretamente;; 0 = nenhuma.

- **EX013 — Caminho proposto.** O que consegue alcançar os dispositivos clínicos sob as regras propostas? *Rubrica:* 3 = apenas o jump host da engenharia clínica;; 2 = jump host;; 1 = tudo;; 0 = nenhuma.

- **EX014 — Registrar datas.** Por que registrar a data de cada fonte? *Rubrica:* 3 = os inventários costumam ser incompletos, então é preciso mostrar a atualidade;; 2 = atualidade;; 1 = nenhuma;; 0 = nenhuma.

- **EX015 — Proporção.** O que significa evidência proporcional aqui? *Rubrica:* 3 = o bastante para justificar a decisão e mostrar os limites, com os detalhes em apêndices;; 2 = o bastante;; 1 = tudo;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Risco avançado e ética

### Objetivos de aprendizagem

Você vai (1) estimar o risco com incerteza explícita; (2) ponderar a segurança do paciente contra outros danos; (3) lidar com um conflito ético no trabalho de arquitetura.

### 4.1 Risco com faixas

Priya estima o risco de um evento de ransomware alcançar os dispositivos clínicos. Em vez de um número único, ela dá faixas: uma probabilidade anual entre dois e oito por cento sob o projeto atual, e um impacto de um a cinco dias de interrupção das clínicas. Ela explica cada faixa por suas fontes, seguindo o NIST SP 800-30 Rev. 1. Um laboratório de Monte Carlo não é necessário para o conselho; um caso simples baixo, provável e alto é mais claro. As faixas mostram aos líderes quanto é desconhecido e impedem que um número de aparência precisa sugira uma confiança que não existe.

### 4.2 Segurança do paciente e outros danos

A saúde acrescenta uma dimensão que a maioria dos métodos de risco trata de forma superficial: o dano aos pacientes. Priya separa três tipos de dano: à segurança do paciente, à privacidade e financeiro. Ela se recusa a converter a segurança do paciente em dinheiro, porque fazer isso esconde um julgamento ético dentro da aritmética. Em vez disso, apresenta o dano à segurança ao lado dos outros e pede ao comitê de governança clínica que o pondere. É esse comitê, e não a equipe de arquitetura, que detém a autoridade sobre o risco clínico. Colocar as decisões no órgão certo faz parte do dever ético do arquiteto.

### 4.3 Um conflito ético

Um fornecedor oferece à Corvane um desconto se ela adiar a segmentação por um ano, para coincidir com o lançamento de um produto do fornecedor. A diretora financeira é favorável a aceitar. Priya acredita que o adiamento expõe os pacientes a um risco evitável. Ela documenta sua opinião, as faixas de risco e a preocupação com a segurança e escala o caso ao comitê de governança clínica, em vez de passar por cima da decisão ou aceitá-la em silêncio. O comitê rejeita o adiamento. Priya reflete que a ética profissional exige tornar o risco visível para quem é responsável, sem decidir sozinha e sem ficar calada.

### Exemplo resolvido

Priya dá faixas de risco com fontes, mantém a segurança do paciente separada do dinheiro e escala ao comitê de governança clínica um adiamento motivado pelo fornecedor.

> **Caso sintético.** Os números, o fornecedor e os comitês são sintéticos; o SP 800-30 Rev. 1 é real.

### Erros e limites

As faixas podem ser largas demais para orientar a ação. Escalar sem evidências pode parecer obstrução.

### Exercícios

- **EX016 — Por que faixas.** Por que expressar o risco em faixas, e não em números únicos? *Rubrica:* 3 = para mostrar a incerteza e evitar falsa confiança;; 2 = incerteza;; 1 = precisão;; 0 = nenhuma.

- **EX017 — Três danos.** Que três tipos de dano Priya separou? *Rubrica:* 3 = segurança do paciente, privacidade e financeiro;; 2 = dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX018 — Não monetizar a segurança.** Por que não converter a segurança do paciente em dinheiro? *Rubrica:* 3 = isso esconde um julgamento ético dentro da aritmética;; 2 = ética;; 1 = é mais fácil;; 0 = nenhuma.

- **EX019 — Autoridade certa.** Quem detém a autoridade sobre o risco clínico na Corvane? *Rubrica:* 3 = o comitê de governança clínica;; 2 = comitê;; 1 = equipe de arquitetura;; 0 = nenhuma.

- **EX020 — Lidar com o desconto.** Como Priya lidou com a oferta de adiamento do fornecedor? *Rubrica:* 3 = documentou e escalou ao comitê de governança clínica;; 2 = escalou;; 1 = aceitou;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Arquitetura e engenharia de segurança: alternativas de desenho

### Objetivos de aprendizagem

Você vai (1) gerar alternativas de projeto realmente diferentes; (2) compará-las por atributos de negócio; (3) escolher com trade-offs explícitos.

### 5.1 Gerar alternativas

Para a decisão de acesso das clínicas, Priya insiste em pelo menos três alternativas reais, e não em um projeto favorito e dois espantalhos. A opção um mantém os firewalls locais e as VPNs, mas automatiza a renovação de certificados. A opção dois leva todas as clínicas a um cloud access broker com políticas cientes de identidade. A opção três é híbrida: um broker em nuvem para as aplicações da equipe, com segmentação local e um caminho local de contingência para os sistemas clínicos. Ela pede a um colega que prefere a opção um que escreva a defesa dela, para que cada opção seja argumentada por alguém que acredita nela.

### 5.2 Atributos como critérios

Priya usa atributos de negócio no estilo do SABSA (Sherwood, Clark e Lynas, 2005) como critérios: disponível, protegido, auditável, operável por uma equipe pequena e acessível em custo. Os líderes clínicos dão o maior peso à disponibilidade, porque as clínicas não podem parar de atender pacientes. O laboratório abaixo pontua as três opções e verifica se a ordenação se mantém quando o peso da disponibilidade muda. A opção híbrida fica em primeiro no caso-base e quando a disponibilidade importa mais; a opção em nuvem só vence se o peso da disponibilidade cair para 0,20 ou menos, o que nenhum líder clínico apoia.

### Laboratório — Notas por atributo e uma varredura de sensibilidade

```python
# Score three access designs on weighted attributes and sweep the availability weight (synthetic).
attrs = ["available", "protected", "auditable", "operable", "affordable"]
score = {"local": [3, 2, 2, 3, 4], "cloud": [3, 5, 5, 4, 3], "hybrid": [5, 4, 4, 3, 3]}
def rank(wa):
    rest = (1 - wa) / 4; w = [wa] + [rest] * 4
    return {o: sum(a * b for a, b in zip(w, s)) for o, s in score.items()}
for wa in (0.40, 0.60, 0.20, 0.05):
    r = rank(wa); best = max(r, key=r.get)
    print(f"availability weight {wa:.2f}: " + ", ".join(f"{o} {v:.2f}" for o, v in r.items()) + f" -> {best}")
```

Execute com `python3 lab_options.py`. Saída verificada:

```text
availability weight 0.40: local 2.85, cloud 3.75, hybrid 4.10 -> hybrid
availability weight 0.60: local 2.90, cloud 3.50, hybrid 4.40 -> hybrid
availability weight 0.20: local 2.80, cloud 4.00, hybrid 3.80 -> cloud
availability weight 0.05: local 2.76, cloud 4.19, hybrid 3.57 -> cloud
```

### 5.3 Trade-offs explícitos

A opção híbrida não sai de graça. Ela mantém dois caminhos de acesso, o que dobra parte do trabalho operacional e cria o risco de o caminho de contingência ser negligenciado até o momento em que for necessário. Priya escreve esses custos no registro de decisão, junto com uma mitigação: testes trimestrais da contingência local em duas clínicas. Ela observa que a escolha híbrida reflete o julgamento de valor do conselho sobre a disponibilidade e que outro conselho poderia, razoavelmente, escolher de outro modo. Explicitar essa dependência mantém a recomendação honesta sobre onde o julgamento entra.

### Exemplo resolvido

Priya desenvolve três alternativas reais com defensores, pontua-as em cinco atributos com uma varredura de sensibilidade e registra os custos e as mitigações da opção híbrida.

> **Caso sintético.** As opções, as notas e os pesos são sintéticos; o SABSA é real.

### Erros e limites

As notas por atributo são julgamentos. Dois caminhos de acesso aumentam a carga operacional.

### Exercícios

- **EX021 — Espantalhos.** Por que insistir em três alternativas reais? *Rubrica:* 3 = para evitar um projeto favorito acompanhado de espantalhos;; 2 = comparação justa;; 1 = rapidez;; 0 = nenhuma.

- **EX022 — Maior peso.** Que atributo os líderes clínicos ponderaram mais, e por quê? *Rubrica:* 3 = disponibilidade, porque as clínicas não podem parar de atender pacientes;; 2 = disponibilidade;; 1 = custo;; 0 = nenhuma.

- **EX023 — Ordenação-base.** Que opção ficou em primeiro no caso-base do laboratório? *Rubrica:* 3 = híbrida, 4,10;; 2 = híbrida;; 1 = nuvem;; 0 = nenhuma.

- **EX024 — Quando a nuvem vence.** Quando a opção em nuvem vence na varredura? *Rubrica:* 3 = com peso de disponibilidade de 0,20 ou menos;; 2 = peso baixo;; 1 = sempre;; 0 = nenhuma.

- **EX025 — Custo da híbrida.** Que custo oculto a opção híbrida carrega? *Rubrica:* 3 = dois caminhos de acesso, com risco de a contingência ser negligenciada;; 2 = contingência;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Arquitetura e engenharia de segurança: avaliação controlada

### Objetivos de aprendizagem

Você vai (1) desenhar um piloto controlado do projeto híbrido; (2) medir os resultados contra um grupo de comparação; (3) interpretar com cuidado resultados limitados.

### 6.1 Desenhar o piloto

Antes de implantar o projeto híbrido nas vinte e duas clínicas, Priya conduz um piloto em seis clínicas, sorteadas entre clínicas de tamanho e conectividade semelhantes, enquanto outras seis continuam como antes. Ela define os resultados de antemão: minutos de indisponibilidade do acesso por clínica por mês, tempo de login da equipe e chamados ao help desk sobre acesso. A escolha aleatória das clínicas do piloto a impede de escolher os locais mais fáceis. Wohlin e colegas (2012) descrevem esse tipo de comparação controlada e as ameaças à validade que ela precisa tratar.

### 6.2 Medir

Ao longo de três meses, as clínicas do piloto registram uma média de onze minutos de indisponibilidade por mês, contra trinta e quatro nas clínicas de comparação, principalmente porque desaparecem as indisponibilidades por expiração de certificados. O tempo de login sobe quatro segundos por causa de uma etapa extra de identidade. Os chamados ao help desk sobem no primeiro mês e depois caem abaixo do nível de comparação. Priya relata cada resultado com o número de clínicas e de meses por trás dele, para que os leitores vejam quão pequena é a amostra. Ela também registra um teste de contingência em cada clínica do piloto.

### 6.3 Interpretar com cuidado

Seis clínicas ao longo de três meses é uma amostra pequena. Priya escreve que os resultados são consistentes com uma disponibilidade melhor e um impacto aceitável sobre a equipe, mas que um único mês ruim poderia mudar o quadro. Ela recomenda uma implantação escalonada com medição contínua, em vez de uma mudança big-bang. O conselho concorda. A Dra. Voss destaca que resultados definidos de antemão, escolha aleatória e relato honesto da amostra são o que tornam um piloto convincente, mais do que o tamanho da melhoria em si. Os números mensais completos são publicados num apêndice para quem quiser conferi-los.

### Exemplo resolvido

Priya pilota o projeto híbrido em seis clínicas sorteadas, mede três resultados definidos de antemão contra seis clínicas de comparação e recomenda uma implantação escalonada.

> **Caso sintético.** As clínicas e os números são sintéticos; Wohlin et al. (2012) é real.

### Erros e limites

Amostras pequenas são frágeis. A equipe pode se comportar de outro modo quando sabe que está num piloto.

### Exercícios

- **EX026 — Escolher por sorteio.** Por que sortear as clínicas do piloto? *Rubrica:* 3 = para impedir a escolha dos locais mais fáceis;; 2 = viés;; 1 = conveniência;; 0 = nenhuma.

- **EX027 — Resultado de indisponibilidade.** Quantos minutos mensais de indisponibilidade tiveram as clínicas do piloto e as de comparação? *Rubrica:* 3 = onze contra trinta e quatro;; 2 = menos;; 1 = nenhuma;; 0 = nenhuma.

- **EX028 — Custo para a equipe.** Que custo para a equipe o piloto mostrou? *Rubrica:* 3 = o login subiu quatro segundos;; 2 = quatro segundos;; 1 = nenhuma;; 0 = nenhuma.

- **EX029 — Padrão dos chamados.** Como mudaram os chamados ao help desk? *Rubrica:* 3 = subiram no primeiro mês e depois caíram abaixo da comparação;; 2 = subida e queda;; 1 = estáveis;; 0 = nenhuma.

- **EX030 — Recomendação.** O que Priya recomendou depois do piloto? *Rubrica:* 3 = uma implantação escalonada com medição contínua;; 2 = escalonada;; 1 = big-bang;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Priya Ramanathan, a Dra. Elena Voss, a Brookmere University, a Corvane Health Network, a Hollin Care e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Porque molda a proteção dos dados dos pacientes, a disponibilidade das clínicas, o fluxo de trabalho da equipe e o orçamento de todas as clínicas por cinco anos.

**EX002.** Que o serviço em nuvem atenderia às metas de disponibilidade em clínicas rurais com conectividade fraca.

**EX003.** Quanto tempo de indisponibilidade das clínicas a organização aceita em troca de economia.

**EX004.** Discutir valores enquanto se parece discutir fatos, misturando as três categorias.

**EX005.** Para que um arquiteto posterior possa ver se as condições por trás da escolha ainda valem.

**EX006.** O acesso da equipe centrado em identidade e a segmentação dos dispositivos clínicos, além do acesso intermediado de fornecedores e dos comitês de revisão.

**EX007.** Eles aproveitam partes, como os perfis de atributos de negócio, em vez de aplicar o método completo.

**EX008.** As organizações revisam os projetos, mas raramente testam se os sistemas entregues correspondem a eles.

**EX009.** Porque um notebook infectado poderia alcançar as estações de gerenciamento das bombas de infusão.

**EX010.** Para que os líderes vejam que as lacunas são julgadas contra orientações reconhecidas, e não contra opinião pessoal.

**EX011.** Quais dispositivos não podem receber patches e de quais conexões de fornecedores eles precisam.

**EX012.** Por meio de um servidor de impressão compartilhado que as duas zonas conseguiam alcançar.

**EX013.** Apenas o jump host da engenharia clínica.

**EX014.** Porque os inventários de dispositivos de saúde costumam ser incompletos e os leitores precisam saber quão atuais são as evidências.

**EX015.** Evidências suficientes para justificar a decisão e seus limites, com os detalhes levados para apêndices.

**EX016.** As faixas mostram quanto é desconhecido e evitam sugerir falsa confiança.

**EX017.** Dano à segurança do paciente, à privacidade e financeiro.

**EX018.** Porque isso esconde um julgamento ético dentro da aritmética.

**EX019.** O comitê de governança clínica.

**EX020.** Ela documentou o risco e a preocupação com a segurança e escalou ao comitê, que rejeitou o adiamento.

**EX021.** Para evitar apresentar um projeto favorito ao lado de opções fracas que servem de espantalho.

**EX022.** A disponibilidade, porque as clínicas precisam continuar atendendo pacientes.

**EX023.** A opção híbrida, com 4,10 contra 3,75 da nuvem.

**EX024.** Apenas quando o peso da disponibilidade cai para 0,20 ou menos, o que nenhum líder clínico apoia.

**EX025.** Dois caminhos de acesso, com o risco de a contingência local ser negligenciada até ser necessária.

**EX026.** Para impedir que a arquiteta selecionasse as clínicas mais fáceis.

**EX027.** Onze minutos nas clínicas do piloto contra trinta e quatro nas clínicas de comparação.

**EX028.** O tempo de login subiu quatro segundos por causa de uma etapa extra de identidade.

**EX029.** Subiram no primeiro mês e depois caíram abaixo do nível de comparação.

**EX030.** Uma implantação escalonada com medição contínua, em vez de uma única grande mudança.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Joint Task Force. (2018). *Risk management framework for information systems and organizations* (NIST SP 800-37 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-37r2>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- Stouffer, K., Pease, M., Tang, C., Zimmerman, T., Pillitteri, V., Lightman, S., Hahn, A., Saravia, S., Sherule, A., & Thompson, M. (2023). *Guide to operational technology (OT) security* (NIST SP 800-82 Rev. 3). NIST. <https://doi.org/10.6028/NIST.SP.800-82r3>
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
