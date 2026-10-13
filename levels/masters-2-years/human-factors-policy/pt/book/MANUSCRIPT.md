# Fatores Humanos e Política Cibernética: Curso de Mestrado

- Idioma: português do Brasil (`pt`); curso 167, curso de mestrado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–8 de 8 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; os três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: mestrandos que avaliam como uma mudança na política de segurança afeta o comportamento e a carga de trabalho dos funcionários.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios ajustam uma série temporal interrompida, calculam um intervalo bootstrap para uma diferença de questionário e executam uma verificação deixando um mês de fora, sempre sobre dados sintéticos; nenhum funcionário, senha ou conta real está envolvido. Os questionários descritos aqui nunca pedem senhas e são anônimos. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma mestranda que avalia o fim das trocas obrigatórias de senha em um hospital: pergunta e método de revisão, seminário avançado, desenho e ética, explicações concorrentes, proposta e piloto, coleta e análise, redação e limitações, e revisão independente e defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Sofia Lindqvist** | Mestranda | Inventada |
| **Dr. Paul Nakamura** | Orientador | Inventado |
| **Harrowgate Institute** | Universidade fictícia | Inventada |
| **Orchard Lane Hospital Trust** | Hospital fictício | Inventado |

### Fontes principais

Adams e Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff e Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050); Beautement, Sasse e Wonham (2008), [doi:10.1145/1595676.1595684](https://doi.org/10.1145/1595676.1595684); Ajzen (1991), [doi:10.1016/0749-5978(91)90020-T](https://doi.org/10.1016/0749-5978(91)90020-T). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Pergunta de pesquisa e método de revisão da literatura

### Objetivos de aprendizagem

Você vai (1) transformar um problema do ambiente de trabalho em uma pergunta de pesquisa; (2) conduzir uma busca estruturada na literatura; (3) registrar as fontes de modo que a busca possa ser repetida.

### 1.1 Do problema à pergunta

Sofia Lindqvist é mestranda no fictício Harrowgate Institute, sob orientação do Dr. Paul Nakamura. Ela trabalha meio período no departamento de TI do fictício Orchard Lane Hospital Trust, onde os funcionários precisam trocar a senha a cada sessenta dias e o service desk atende centenas de redefinições por mês. A equipe clínica reclama que as regras desperdiçam tempo durante os plantões. Sofia transforma a reclamação em uma pergunta: depois que o hospital deixou de exigir trocas periódicas obrigatórias e passou a oferecer um gerenciador de senhas, os pedidos de redefinição caíram, e os funcionários passaram a relatar menos reutilização de senhas?

### 1.2 Por que a pergunta importa

Sofia explica ao Dr. Nakamura por que a pergunta merece uma dissertação. Adams e Sasse (1999) constataram que regras de senha exigentes levavam os funcionários a anotar e reutilizar senhas, porque as regras ignoravam o modo como as pessoas realmente trabalham. Trocas obrigatórias são um exemplo comum de regra cujos custos aparecem todos os dias, enquanto os benefícios são incertos. Se a mudança feita pelo hospital reduziu o ônus sem criar novos riscos, outros hospitais podem aprender com ela. Se não reduziu, isso também será uma evidência útil para quem formula políticas e precisa decidir sobre regras de senha.

### 1.3 Uma busca estruturada

Sofia pesquisa em duas bases de dados acadêmicas e em uma coleção de normas, usando termos planejados em inglês: "password policy", "password expiration", "password manager", "usable security" e "help desk". Para cada busca, registra a data, a base, a string de busca e o número de resultados. Faz a triagem de títulos e resumos com base em regras de inclusão escritas: estudos empíricos ou orientações oficiais sobre senhas no ambiente de trabalho. Mantém uma tabela dos itens excluídos, com os motivos. O Dr. Nakamura ressalta que uma busca repetível protege a revisão da acusação de que ela só citou estudos favoráveis à sua opinião.

### 1.4 O que a busca encontrou

A busca de Sofia retorna um conjunto administrável de fontes. Entre as obras principais estão Adams e Sasse (1999); Sasse, Brostoff e Weirich (2001), sobre o projeto de segurança utilizável; Herley (2009), sobre usuários que rejeitam racionalmente conselhos custosos; e Beautement, Sasse e Wonham (2008), sobre o orçamento de compliance. Ela também encontra orientações do NIST e de órgãos nacionais que abandonaram as trocas obrigatórias rotineiras, e as registra como contexto, e não como evidência de efeito. Anota as lacunas: poucos estudos medem o que acontece em um hospital depois de uma mudança desse tipo. Guarda o log completo da busca como apêndice da dissertação.

### Exemplo resolvido

Sofia transforma uma reclamação em uma pergunta de pesquisa de antes e depois, justifica-a, conduz uma busca registrada com regras de inclusão e resume as fontes principais e as lacunas.

> **Caso sintético.** O Harrowgate, o Orchard Lane e todas as pessoas são sintéticos; as obras citadas são reais.

### Erros e limites

Buscas em bases de dados deixam de fora a literatura cinzenta. Documentos de orientação declaram posições, e não efeitos medidos.

### Exercícios

- **EX001 — Pergunta de pesquisa.** Que pergunta de pesquisa Sofia formulou? *Rubrica:* 3 = depois do fim das trocas obrigatórias e da oferta de um gerenciador, as redefinições caíram e os relatos de reutilização diminuíram?;; 2 = dois desfechos;; 1 = nada;; 0 = nenhuma.
- **EX002 — Relevância de Adams e Sasse.** Por que Adams e Sasse (1999) é relevante? *Rubrica:* 3 = regras exigentes levavam a anotar e reutilizar senhas;; 2 = contornos;; 1 = nada;; 0 = nenhuma.
- **EX003 — Registro da busca.** O que Sofia registra para cada busca? *Rubrica:* 3 = data, base, string de busca e número de resultados;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX004 — Itens excluídos.** Por que manter uma tabela de itens excluídos? *Rubrica:* 3 = para que a busca possa ser repetida e não pareça seletiva;; 2 = transparência;; 1 = nada;; 0 = nenhuma.
- **EX005 — Orientação como contexto.** Por que tratar orientações oficiais como contexto, e não como evidência? *Rubrica:* 3 = declaram posições, e não efeitos medidos;; 2 = posições;; 1 = evidência;; 0 = nenhuma.
- **EX006 — Lacuna encontrada.** Que lacuna Sofia registrou? *Rubrica:* 3 = poucos estudos medem efeitos em um hospital depois de uma mudança desse tipo;; 2 = hospital;; 1 = nada;; 0 = nenhuma.
- **EX007 — O argumento de Herley.** Que fonte argumenta que os usuários rejeitam racionalmente conselhos custosos? *Rubrica:* 3 = Herley (2009);; 2 = Herley;; 1 = Whitten;; 0 = nenhuma.

### Síntese

Uma pergunta focada e uma busca registrada e repetível dão a uma dissertação um ponto de partida defensável.

<a id="ch-02"></a>

## Capítulo 2 — Fatores humanos e política cibernética: seminário avançado

### Objetivos de aprendizagem

Você vai (1) criticar as principais teorias de fatores humanos; (2) comparar modelos comportamentais aplicados à segurança; (3) aplicá-los à mudança na política de senhas do hospital.

### 2.1 Teorias do comportamento

No seminário, o Dr. Nakamura pede aos alunos que comparem teorias que explicam o comportamento de segurança. A teoria do comportamento planejado (Ajzen, 1991) diz que as intenções dependem de atitudes, normas sociais e controle percebido. O orçamento de compliance (Beautement, Sasse e Wonham, 2008) diz que as pessoas gastam um esforço limitado com segurança e deixam de cumprir as regras quando as exigências o ultrapassam. Sofia observa que a primeira se concentra no que as pessoas acreditam e a segunda no que as exigências custam. As duas oferecem previsões sobre a mudança de política do hospital, que ela pode comparar. Ela resume ambas em uma tabela comparativa curta.

### 2.2 Aplicar os modelos

Usando o comportamento planejado, Sofia prevê que os funcionários que acreditam que o gerenciador de senhas é fácil de usar e veem colegas usando-o vão adotá-lo. Usando o orçamento de compliance, prevê que eliminar as trocas obrigatórias libera esforço, o que pode aumentar o cumprimento de outras regras, como bloquear a tela. Os modelos fazem previsões diferentes sobre quem muda de comportamento: o comportamento planejado aponta para atitudes e normas, enquanto o orçamento aponta para a carga de trabalho. O desenho do estudo pode testar algumas dessas diferenças, levantando crenças em questionário e medindo a carga de trabalho. Ela escreve cada previsão em uma única frase testável.

### 2.3 Crítica

O seminário critica as duas teorias. O comportamento planejado muitas vezes explica melhor as intenções do que as ações, e as ações de segurança frequentemente são hábitos, e não escolhas deliberadas. O orçamento de compliance é persuasivo, mas difícil de medir diretamente. Bada, Sasse e Nurse (2019) argumentam que campanhas de conscientização fracassam quando presumem que a informação, sozinha, muda o comportamento. Sofia conclui que nenhum modelo isolado explicará seus resultados e que ela deve declarar quais previsões vêm de qual modelo, para que os leitores vejam quais teorias seus dados sustentam e quais não. O grupo do seminário concorda com essa abordagem.

### 2.4 Relevância para políticas

Sofia liga a teoria às políticas. Se o modelo do orçamento for válido, quem formula políticas deve contabilizar o custo de cada regra e eliminar as de pouco valor. Se o comportamento planejado for válido, o foco deve ser tornar as opções seguras fáceis e visíveis. A ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) exige conscientização e competência, mas deixa o método a cargo das organizações. Ela observa que a teoria só ajuda as políticas quando leva a previsões mensuráveis, e acrescenta duas previsões desse tipo ao plano do estudo, para testá-las nos dados do hospital. Registra as duas previsões na proposta antes de ver qualquer dado posterior à mudança.

### Exemplo resolvido

Sofia compara o comportamento planejado e o orçamento de compliance, deriva previsões diferentes para a mudança de senhas, critica as duas teorias e as liga às políticas.

> **Caso sintético.** As previsões são sintéticas; Ajzen (1991), Beautement et al. (2008), Bada et al. (2019) e a ISO/IEC 27001:2022 são reais.

### Erros e limites

Modelos simplificam o comportamento. Medidas de atitude por questionário são imperfeitas.

### Exercícios

- **EX008 — Fatores do comportamento planejado.** Que três fatores moldam a intenção no comportamento planejado? *Rubrica:* 3 = atitudes, normas sociais e controle percebido;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX009 — Previsão do orçamento.** O que o orçamento de compliance prevê depois do fim das trocas obrigatórias? *Rubrica:* 3 = o esforço liberado pode aumentar o cumprimento de outras regras;; 2 = esforço liberado;; 1 = nada;; 0 = nenhuma.
- **EX010 — Lacuna entre intenção e ação.** Qual é uma fraqueza conhecida do comportamento planejado? *Rubrica:* 3 = explica melhor as intenções do que as ações;; 2 = intenção-ação;; 1 = nada;; 0 = nenhuma.
- **EX011 — Fracasso das campanhas.** Por que as campanhas fracassam, segundo Bada et al.? *Rubrica:* 3 = presumem que a informação sozinha muda o comportamento;; 2 = informação;; 1 = nada;; 0 = nenhuma.
- **EX012 — Teoria para políticas.** Quando a teoria ajuda as políticas, na visão de Sofia? *Rubrica:* 3 = quando gera previsões mensuráveis;; 2 = previsões;; 1 = sempre;; 0 = nenhuma.
- **EX013 — Duas previsões.** Cite as duas previsões baseadas em modelos que ela acrescenta. *Rubrica:* 3 = adoção do gerenciador por atitudes e normas; mais bloqueio de tela pelo esforço liberado;; 2 = uma;; 1 = nada;; 0 = nenhuma.
- **EX014 — Medir o orçamento.** Por que o orçamento de compliance é difícil de testar? *Rubrica:* 3 = é difícil de medir diretamente;; 2 = medição;; 1 = nada;; 0 = nenhuma.

### Síntese

Teorias comportamentais são úteis quando fazem previsões distintas e testáveis sobre uma mudança real de política.

<a id="ch-03"></a>

## Capítulo 3 — Desenho do estudo, ética e reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) desenhar um estudo de métodos mistos sobre uma mudança de política; (2) obter aprovação ética para pesquisa com funcionários; (3) planejar a reprodutibilidade.

### 3.1 Métodos mistos

Sofia desenha um estudo em três partes. Primeiro, analisa as contagens mensais de redefinições de senha no service desk ao longo de dezoito meses antes e doze meses depois da mudança de política, uma série temporal interrompida que verifica se o nível ou a tendência mudaram. Segundo, aplica aos funcionários um questionário sobre hábitos de senha, incluindo reutilização e anotação de senhas, com perguntas anônimas. Terceiro, entrevista doze funcionários de funções diferentes sobre como a mudança afetou seu trabalho. Combinar contagens, respostas de questionário e entrevistas permite que cada método cubra as fraquezas dos outros.

### 3.2 Aprovação ética

Sofia submete o projeto ao comitê de ética do Harrowgate e ao escritório de pesquisa do hospital. O questionário não coleta nomes nem faz perguntas sobre senhas reais; pergunta apenas sobre hábitos. Os entrevistados dão consentimento por escrito, podem desistir e são citados apenas pela função. Os dados do service desk são fornecidos como contagens mensais, sem nenhum nome. O comitê pede que ela evite recrutar para as entrevistas seus próprios colegas diretos, porque eles poderiam se sentir incapazes de recusar. Ela concorda e recruta por meio de um aviso neutro. Todos os termos de consentimento ficam guardados com segurança no Harrowgate.

### 3.3 Riscos do autorrelato

Perguntar aos funcionários se reutilizam senhas convida a respostas socialmente desejáveis. Sofia usa uma redação que normaliza o comportamento, por exemplo lembrando que muitas pessoas reutilizam senhas por conveniência, e pergunta sobre frequência em vez de pedir sim ou não. Mantém o questionário anônimo e evita qualquer vínculo com contas individuais. Mesmo assim, espera que a reutilização seja sub-relatada e planeja comparar as respostas de antes e depois, em vez de tratar o nível absoluto como exato. Conhecer o viés de uma medida permite interpretá-la com bom senso. Ela explica essa escolha no capítulo de métodos.

### 3.4 Plano de reprodutibilidade

Sofia escreve um plano de análise antes de ver os dados posteriores à mudança. Guarda o código, o questionário, o roteiro de entrevista e os dados anonimizados em um repositório versionado. As transcrições das entrevistas não são compartilhadas, porque poderiam identificar funcionários; em vez delas, ela compartilha seu esquema de codificação e as contagens. O Dr. Nakamura lembra que reprodutibilidade em pesquisa com pessoas significa compartilhar tudo o que pode ser compartilhado com segurança e explicar com clareza o que não pode e por quê, em vez de não compartilhar nada ou de pôr em risco a privacidade dos participantes. Ela lista os itens compartilhados em uma declaração de dados curta.

### Exemplo resolvido

Sofia desenha um estudo com série temporal, questionário e entrevistas, obtém aprovação com salvaguardas, reduz o viés de autorrelato e escreve um plano de reprodutibilidade.

> **Caso sintético.** O estudo e os comitês são sintéticos.

### Erros e limites

Séries temporais interrompidas podem ser confundidas por outras mudanças simultâneas. Questionários sub-relatam hábitos sensíveis.

### Exercícios

- **EX015 — Três partes.** Quais são as três partes do estudo de Sofia? *Rubrica:* 3 = série temporal das redefinições, questionário anônimo e entrevistas;; 2 = duas;; 1 = nada;; 0 = nenhuma.
- **EX016 — Limites do questionário.** O que o questionário não pergunta? *Rubrica:* 3 = nomes ou senhas reais;; 2 = senhas;; 1 = nada;; 0 = nenhuma.
- **EX017 — Recrutar colegas.** Por que evitar recrutar colegas diretos? *Rubrica:* 3 = poderiam se sentir incapazes de recusar;; 2 = pressão;; 1 = nada;; 0 = nenhuma.
- **EX018 — Redação que normaliza.** Como Sofia reduz as respostas socialmente desejáveis? *Rubrica:* 3 = redação que normaliza a reutilização e pergunta a frequência;; 2 = redação;; 1 = nada;; 0 = nenhuma.
- **EX019 — Comparar níveis.** Por que comparar antes e depois em vez de confiar nos níveis absolutos? *Rubrica:* 3 = a reutilização tende a ser sub-relatada de forma consistente;; 2 = relativo;; 1 = absoluto;; 0 = nenhuma.
- **EX020 — Transcrições não compartilhadas.** O que é compartilhado no lugar das transcrições das entrevistas? *Rubrica:* 3 = o esquema de codificação e as contagens;; 2 = esquema de codificação;; 1 = transcrições;; 0 = nenhuma.

### Síntese

Métodos mistos, com ética cuidadosa e um plano de reprodutibilidade honesto, são adequados à pesquisa sobre o comportamento de segurança da equipe.

<a id="ch-04"></a>

## Capítulo 4 — Fatores humanos e política cibernética: explicações concorrentes

### Objetivos de aprendizagem

Você vai (1) listar explicações para uma mudança nas contagens de redefinições; (2) desenhar verificações para cada uma; (3) decidir o que a evidência sustenta.

### 4.1 Explicações possíveis

Os primeiros dados mostram que as redefinições de senha caíram depois da mudança de política. O Dr. Nakamura pede a Sofia que liste todas as explicações plausíveis antes de declarar sucesso. As redefinições podem ter caído porque as trocas obrigatórias acabaram; porque o gerenciador de senhas ajudou as pessoas a lembrar; porque uma nova ferramenta de autoatendimento desviou pedidos do service desk; porque o quadro de pessoal diminuiu no verão; ou porque o service desk mudou a forma de registrar os chamados. Listar explicações impede que ela aceite a primeira história que combina com suas esperanças. Ela escreve cada explicação em uma linha separada de uma tabela, para associar a cada uma delas uma verificação específica e o respectivo resultado.

### 4.2 Verificações para cada uma

Sofia desenha uma verificação para cada explicação. Para o autoatendimento, obtém as contagens de redefinições por autoatendimento e as soma às do service desk. Para o quadro de pessoal, divide as redefinições pelo número de contas ativas. Para as mudanças de registro, lê o log de mudanças do service desk e entrevista o líder do service desk. Para os efeitos sazonais, compara os mesmos meses do ano anterior. Para o gerenciador de senhas, compara departamentos com adoção alta e baixa do gerenciador. Cada verificação mira diretamente uma explicação, em vez de depender de uma impressão geral sobre os dados.

### Laboratório — Série temporal interrompida das redefinições mensais por 1.000 contas

```python
# Interrupted time series on resets per 1,000 accounts: 18 months before, 12 after (synthetic).
import random
random.seed(3)
y = [62 - 0.2 * t + random.gauss(0, 2) for t in range(18)] + [39 - 0.25 * (t - 18) + random.gauss(0, 2) for t in range(18, 30)]
def fit(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    b = sum((x - mx) * (v - my) for x, v in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b
a0, b0 = fit(range(18), y[:18]); a1, b1 = fit(range(18, 30), y[18:])
pred = a0 + b0 * 18; obs = a1 + b1 * 18
print(f"before: level at month 18 predicted {pred:.1f}, slope {b0:+.2f}/month")
print(f"after: level at month 18 fitted {obs:.1f}, slope {b1:+.2f}/month")
print(f"level change {obs - pred:+.1f} per 1,000 accounts; slope change {b1 - b0:+.2f}")
```

Execute com `python3 lab_its.py`. Saída verificada:

```text
before: level at month 18 predicted 56.9, slope -0.37/month
after: level at month 18 fitted 38.1, slope -0.27/month
level change -18.8 per 1,000 accounts; slope change +0.09
```

### 4.3 O que as verificações mostram

As redefinições por autoatendimento respondem por parte da queda, mas não por toda ela: o total de redefinições por mil contas ainda cai depois da mudança. As mudanças no quadro de pessoal são pequenas. A mudança na forma de registro do service desk aconteceu quatro meses depois, então não pode explicar a queda imediata. O laboratório estima uma queda de nível no ponto da mudança, com pouca alteração na tendência. Departamentos com maior adoção do gerenciador mostram quedas um pouco maiores, o que é compatível com um efeito do gerenciador, mas não o prova, já que quem adota pode diferir de outras maneiras.

### 4.4 Decidir o que é sustentado

Sofia escreve sua conclusão em níveis de confiança. Fortemente sustentado: o total de redefinições por mil contas caiu no ponto da mudança. Moderadamente sustentado: o fim das trocas obrigatórias contribuiu, já que o momento coincide e as alternativas foram em grande parte descartadas. Fracamente sustentado: o gerenciador de senhas contribuiu. Não testado: se a segurança melhorou. O Dr. Nakamura elogia a estrutura e observa que ordenar as explicações pela evidência é mais honesto e mais útil para quem formula políticas do que uma única causa afirmada com falsa certeza. Ela apresenta os quatro níveis em uma tabela curta no capítulo de discussão, para que os leitores vejam de relance quão sustentada está cada afirmação.

### Exemplo resolvido

Sofia lista cinco explicações para a queda das redefinições, desenha verificações específicas, executa uma série temporal interrompida e ordena as conclusões por grau de confiança.

> **Caso sintético.** Os dados e os departamentos são sintéticos.

### Erros e limites

Comparações entre departamentos são confundidas pelas escolhas de adoção. Séries temporais precisam de pontos suficientes antes e depois.

### Exercícios

- **EX021 — Lista de explicações.** Cite três explicações para a queda das redefinições. *Rubrica:* 3 = fim das trocas obrigatórias, gerenciador de senhas, autoatendimento, quadro de pessoal, mudança de registro;; 2 = duas;; 1 = nada;; 0 = nenhuma.
- **EX022 — Verificação do autoatendimento.** Como Sofia tratou a ferramenta de autoatendimento? *Rubrica:* 3 = somou as contagens de autoatendimento às do service desk;; 2 = combinar;; 1 = ignorar;; 0 = nenhuma.
- **EX023 — Verificação do quadro de pessoal.** Como ela controlou as mudanças no quadro de pessoal? *Rubrica:* 3 = dividiu as redefinições pelas contas ativas;; 2 = taxa;; 1 = nada;; 0 = nenhuma.
- **EX024 — Mudança de nível no laboratório.** O que o laboratório estimou no ponto da mudança? *Rubrica:* 3 = queda de nível de 18,8 redefinições por 1.000 contas, mudança de inclinação de +0,09;; 2 = queda de nível;; 1 = aumento;; 0 = nenhuma.
- **EX025 — Momento do registro.** Por que a mudança de registro não pode explicar a queda imediata? *Rubrica:* 3 = aconteceu quatro meses depois;; 2 = momento;; 1 = nada;; 0 = nenhuma.
- **EX026 — Afirmação mais fraca.** Que explicação é apenas fracamente sustentada? *Rubrica:* 3 = a de que o gerenciador de senhas contribuiu;; 2 = gerenciador;; 1 = trocas obrigatórias;; 0 = nenhuma.

### Síntese

Listar e verificar explicações concorrentes permite que um estudo ordene as suas conclusões com honestidade pela força das evidências.

<a id="ch-05"></a>

## Capítulo 5 — Proposta e piloto

### Objetivos de aprendizagem

Você vai (1) escrever uma proposta de dissertação; (2) testar em piloto o questionário e o roteiro de entrevista; (3) revisar os instrumentos com base nas evidências do piloto.

### 5.1 A proposta

A proposta de Sofia apresenta a pergunta, a literatura, as teorias com suas previsões, o desenho em três partes, a ética, o plano de análise e um cronograma. Ela declara o que contaria como apoio e o que contaria contra: se as redefinições por mil contas não caírem no ponto da mudança, ou se os relatos de anotação de senhas no questionário aumentarem, ela relatará a mudança como não benéfica. O Dr. Nakamura a aprova depois que ela encurta a seção de literatura e acrescenta um registro de riscos para atrasos no acesso aos dados. A proposta aprovada é arquivada junto com o pedido ao comitê de ética.

### 5.2 Piloto do questionário

Sofia testa o questionário com dez funcionários de um departamento que não faz parte da amostra. Cronometra o preenchimento e pede a cada pessoa que explique o que entendeu de cada pergunta. Surgem dois problemas. Os funcionários interpretam "gerenciador de senhas" de formas diferentes: alguns pensam nas senhas salvas do navegador, outros na ferramenta aprovada pelo hospital. Uma pergunta sobre compartilhar senhas é lida por alguns como compartilhar com a família e por outros como compartilhar com colegas. Ela reescreve as duas perguntas com exemplos e acrescenta uma definição curta no início. O preenchimento leva cerca de oito minutos.

### 5.3 Piloto das entrevistas

Ela conduz duas entrevistas-piloto. A primeira se alonga demais, porque as perguntas convidam a reclamações genéricas sobre a TI. Ela reordena o roteiro para começar por uma experiência recente e específica, como a última vez em que o participante esqueceu uma senha, e só depois passar a opiniões mais amplas. O segundo piloto funciona melhor e produz exemplos concretos. Ela também aprende a fazer pausas e deixar os participantes terminarem, em vez de preencher os silêncios, o que gera relatos mais ricos sobre como as regras de senha interagem com o trabalho clínico. Registra essas lições em seu diário de pesquisa, para reflexão posterior.

### 5.4 Registrar as revisões

Sofia registra cada mudança decorrente do piloto em um log de revisões, com o motivo e a evidência que a motivou. Os dados do piloto não são usados na análise principal, o que ela anota no plano. O Dr. Nakamura explica que os examinadores procuram esse registro porque ele mostra que os instrumentos foram testados, e não apenas presumidos como funcionais. Ele observa também que os pilotos muitas vezes revelam que pesquisadores e participantes usam as mesmas palavras com sentidos diferentes, algo especialmente comum em segurança, em que termos técnicos carregam também significados do dia a dia.

### Exemplo resolvido

Sofia escreve uma proposta com critérios de refutação, testa em piloto o questionário e as entrevistas, corrige perguntas ambíguas, reordena o roteiro e registra as revisões.

> **Caso sintético.** Os pilotos e os funcionários são sintéticos.

### Erros e limites

Pilotos pequenos deixam passar problemas raros. Revisões feitas após o piloto podem introduzir novas ambiguidades.

### Exercícios

- **EX027 — O que conta contra.** Que resultados contariam contra a mudança de política? *Rubrica:* 3 = nenhuma queda nas redefinições por 1.000 ou mais relatos de anotação de senhas;; 2 = qualquer um;; 1 = nada;; 0 = nenhuma.
- **EX028 — Revisão da proposta.** O que o Dr. Nakamura pediu que ela acrescentasse? *Rubrica:* 3 = um registro de riscos para atrasos no acesso aos dados;; 2 = registro de riscos;; 1 = nada;; 0 = nenhuma.
- **EX029 — Termo ambíguo.** Que termo os funcionários interpretaram de formas diferentes? *Rubrica:* 3 = gerenciador de senhas;; 2 = gerenciador;; 1 = nada;; 0 = nenhuma.
- **EX030 — Ajuste da entrevista.** Como o roteiro de entrevista foi reordenado? *Rubrica:* 3 = começar por uma experiência recente e específica, depois opiniões mais amplas;; 2 = específico primeiro;; 1 = nada;; 0 = nenhuma.
- **EX031 — Uso dos dados do piloto.** Os dados do piloto entram na análise principal? *Rubrica:* 3 = não;; 2 = excluídos;; 1 = sim;; 0 = nenhuma.
- **EX032 — Palavras compartilhadas.** Que problema comum os pilotos revelam na pesquisa em segurança? *Rubrica:* 3 = pesquisadores e participantes usam as palavras de modos diferentes;; 2 = significado;; 1 = nada;; 0 = nenhuma.

### Síntese

Os pilotos testam se os instrumentos significam o que o pesquisador pretende, e revisões registradas mostram aos examinadores que eles foram testados.

<a id="ch-06"></a>

## Capítulo 6 — Coleta e análise de dados

### Objetivos de aprendizagem

Você vai (1) coletar dados de questionário e de entrevistas de forma ética; (2) analisar a mudança nas respostas ao questionário; (3) codificar as entrevistas em temas.

### 6.1 Coletar os dados

Sofia aplica o questionário três meses depois da mudança de política, usando as mesmas perguntas que o hospital havia feito em uma pesquisa interna anterior à mudança. A pesquisa de antes foi anônima e teve a mesma redação em duas perguntas, sobre reutilização e sobre anotação de senhas, o que permite a comparação. Quatrocentos e doze funcionários respondem depois da mudança, contra trezentos e noventa antes. Ela conduz doze entrevistas com profissionais de enfermagem, médicos, administrativos e de infraestrutura predial, e para quando novas entrevistas acrescentam poucas ideias novas. Todas as entrevistas são gravadas com consentimento.

### 6.2 Analisar a mudança no questionário

Sofia compara a proporção de funcionários que relatam anotar senhas. O laboratório estima as proporções de antes e depois e um intervalo bootstrap para a diferença, que reamostra as respostas muitas vezes para mostrar quanto a diferença poderia variar por acaso. A proporção caiu alguns pontos percentuais, e o intervalo não cruza o zero, de modo que a queda dificilmente se deve apenas ao acaso. Ela observa que as amostras são de pessoas diferentes, já que as pesquisas foram anônimas; trata-se, portanto, de uma comparação entre grupos, e não entre indivíduos.

### Laboratório — Intervalo bootstrap para a mudança na anotação de senhas

```python
# Bootstrap interval for the change in share reporting writing passwords down (synthetic anonymous surveys).
import random
rng = random.Random(9)
before = [1] * 82 + [0] * 308    # 390 respondents
after = [1] * 62 + [0] * 350     # 412 respondents
pb, pa = sum(before) / len(before), sum(after) / len(after)
diffs = []
for _ in range(4000):
    b = [rng.choice(before) for _ in before]; a = [rng.choice(after) for _ in after]
    diffs.append(sum(a) / len(a) - sum(b) / len(b))
diffs.sort()
print(f"before {pb:.1%}, after {pa:.1%}, difference {pa - pb:+.1%}")
print(f"95% bootstrap interval {diffs[100]:+.1%} to {diffs[3899]:+.1%}")
```

Execute com `python3 lab_boot.py`. Saída verificada:

```text
before 21.0%, after 15.0%, difference -6.0%
95% bootstrap interval -11.3% to -0.8%
```

### 6.3 Codificar as entrevistas

Sofia codifica as transcrições das entrevistas com um esquema construído a partir de suas teorias e refinado pela leitura. Os temas incluem a pressão do tempo no plantão, contornos como anotações compartilhadas, o alívio com menos trocas e a confusão em torno do gerenciador de senhas. Um segundo codificador codifica três transcrições de forma independente; os dois concordam na maioria dos códigos e discutem as diferenças. As entrevistas explicam os números: os funcionários descrevem as trocas obrigatórias como interrupções no cuidado aos pacientes, e vários dizem que o gerenciador de senhas foi introduzido sem treinamento, o que limitou a adoção. Os códigos acordados são registrados em um livro de códigos compartilhado, com definições e uma citação de exemplo para cada um, de modo que o esquema possa ser reutilizado.

### 6.4 Reunir os resultados

Sofia combina os achados. As redefinições caíram no ponto da mudança; menos funcionários relatam anotar senhas; as entrevistas descrevem alívio e menos interrupções. A adoção do gerenciador ficou abaixo do esperado, o que se explica pela falta de treinamento. Ela avalia que a evidência sustenta a previsão do orçamento de compliance sobre a redução do ônus, enquanto o comportamento planejado ajuda a explicar a baixa adoção do gerenciador pela dificuldade percebida. Integrar os métodos mostra um quadro mais completo do que qualquer método isolado, e também onde eles divergem, como quando os funcionários superestimam com que frequência ainda redefinem senhas. Ela mostra essas ligações em uma tabela de apresentação conjunta.

### Exemplo resolvido

Sofia compara pesquisas anônimas de antes e depois com um intervalo bootstrap, codifica doze entrevistas com um segundo codificador e integra os achados à teoria.

> **Caso sintético.** Os questionários, as entrevistas e os números são sintéticos.

### Erros e limites

Pesquisas anônimas repetidas comparam grupos, não indivíduos. Julgamentos de saturação são subjetivos.

### Exercícios

- **EX033 — Perguntas comparáveis.** Por que Sofia pôde comparar as respostas de antes e depois? *Rubrica:* 3 = uma pesquisa anônima anterior usou a mesma redação;; 2 = mesma redação;; 1 = nada;; 0 = nenhuma.
- **EX034 — Números de respostas.** Quantos funcionários responderam antes e depois? *Rubrica:* 3 = 390 antes e 412 depois;; 2 = números;; 1 = nada;; 0 = nenhuma.
- **EX035 — Resultado do bootstrap.** O que o laboratório encontrou sobre a anotação de senhas? *Rubrica:* 3 = 21,0% antes, 15,0% depois; diferença de -6,0 pontos, intervalo abaixo de zero;; 2 = queda;; 1 = aumento;; 0 = nenhuma.
- **EX036 — Comparação entre grupos.** Por que a comparação do questionário é apenas entre grupos? *Rubrica:* 3 = pesquisas anônimas não ligam as mesmas pessoas;; 2 = anonimato;; 1 = nada;; 0 = nenhuma.
- **EX037 — Motivo da baixa adoção.** Por que a adoção do gerenciador de senhas foi baixa, segundo as entrevistas? *Rubrica:* 3 = foi introduzido sem treinamento;; 2 = treinamento;; 1 = nada;; 0 = nenhuma.
- **EX038 — Apoio à teoria.** A previsão sobre o ônus de qual teoria a evidência sustentou? *Rubrica:* 3 = o orçamento de compliance;; 2 = orçamento;; 1 = nada;; 0 = nenhuma.

### Síntese

Combinar contagens, variação em questionários e temas de entrevistas dá um retrato mais completo e mais honesto do que qualquer método isolado.

<a id="ch-07"></a>

## Capítulo 7 — Redação da dissertação e limitações

### Objetivos de aprendizagem

Você vai (1) estruturar uma dissertação capítulo a capítulo; (2) escrever limitações que informem, em vez de servir de desculpa; (3) testar a robustez do resultado principal.

### 7.1 Estrutura

A dissertação de Sofia segue uma estrutura clara: introdução, literatura e teoria, métodos, resultados de cada parte, discussão integrada, limitações, implicações e conclusão. Cada capítulo de resultados abre com a pergunta que responde e termina com um resumo curto. Ela escreve primeiro o capítulo de métodos, enquanto os detalhes estão frescos, e por último a introdução, quando já sabe o que encontrou. O Dr. Nakamura lê os capítulos à medida que são redigidos e pede que ela corte as repetições entre a revisão da literatura e a discussão. Ela mantém uma lista corrente das decisões que precisará explicar no capítulo de métodos.

### 7.2 Robustez

Antes de escrever a conclusão, Sofia verifica se o resultado principal depende de escolhas que ela fez. Executa de novo a análise da série temporal retirando cada mês por vez, para ver se algum mês atípico, sozinho, determina o resultado. O laboratório mostra que a mudança de nível fica dentro de uma faixa estreita, seja qual for o mês retirado. Ela também testa contar as redefinições por funcionário em vez de por conta, com resultados semelhantes. Verificações de robustez mostram aos leitores que a conclusão não desmoronaria se uma escolha analítica razoável tivesse sido feita de outro modo.

### Laboratório — Verificação deixando um mês de fora na mudança de nível

```python
# Leave-one-month-out check on the interrupted time series level change (same synthetic data as lab_its).
import random
random.seed(3)
y = [62 - 0.2 * t + random.gauss(0, 2) for t in range(18)] + [39 - 0.25 * (t - 18) + random.gauss(0, 2) for t in range(18, 30)]
def fit(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    b = sum((x - mx) * (v - my) for x, v in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b
def level(skip):
    pts = [(t, v) for t, v in enumerate(y) if t != skip]
    pre = [p for p in pts if p[0] < 18]; post = [p for p in pts if p[0] >= 18]
    a0, b0 = fit([p[0] for p in pre], [p[1] for p in pre]); a1, b1 = fit([p[0] for p in post], [p[1] for p in post])
    return (a1 + b1 * 18) - (a0 + b0 * 18)
vals = [level(s) for s in range(30)]
print(f"full data level change {level(-1):+.1f}; leave-one-out range {min(vals):+.1f} to {max(vals):+.1f}")
```

Execute com `python3 lab_robust.py`. Saída verificada:

```text
full data level change -18.8; leave-one-out range -19.3 to -17.8
```

### 7.3 Limitações úteis

Sofia escreve limitações que dizem aos leitores como interpretar o trabalho. O estudo abrange um único hospital, de modo que os resultados podem ser diferentes em organizações com outros funcionários ou outros sistemas. Os grupos do questionário não são indivíduos pareados. O efeito do gerenciador de senhas não pode ser separado das falhas de treinamento. O estudo não mediu desfechos de segurança como o comprometimento de contas, porque esses dados não estavam disponíveis. Para cada limitação, ela declara a provável direção do viés e que tipo de estudo poderia tratá-la. Mantém a seção curta e específica, para não diluí-la.

### 7.4 Implicações

Sofia separa as implicações para o hospital, para outros hospitais e para as políticas. Para o hospital: manter a mudança, oferecer treinamento no gerenciador e acompanhar indicadores de comprometimento. Para outros hospitais: a mudança reduziu o ônus aqui e vale a pena experimentá-la com medição. Para as políticas: as orientações contrárias às trocas obrigatórias rotineiras são compatíveis com esses achados, embora um único estudo não possa encerrar a questão. Escrever as implicações em três níveis evita o exagero que ocorre quando achados de um único local são apresentados como verdades universais. Cada implicação cita o resultado específico que a sustenta, para que os leitores possam rastrear cada recomendação até a evidência.

### Exemplo resolvido

Sofia estrutura a dissertação, verifica a robustez deixando cada mês de fora, escreve limitações com direção de viés e declara implicações em três níveis.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

Verificações de robustez cobrem apenas as alternativas escolhidas. As implicações podem ser lidas de forma mais ampla do que o pretendido.

### Exercícios

- **EX039 — Ordem de redação.** Quais capítulos Sofia escreve primeiro e por último? *Rubrica:* 3 = métodos primeiro, introdução por último;; 2 = ordem;; 1 = nada;; 0 = nenhuma.
- **EX040 — Deixar um de fora.** O que testa retirar cada mês por vez? *Rubrica:* 3 = se um mês atípico determina o resultado;; 2 = influência;; 1 = nada;; 0 = nenhuma.
- **EX041 — Faixa robusta.** Que faixa o laboratório mostrou ao deixar um mês de fora? *Rubrica:* 3 = mudança de nível entre -19,3 e -17,8;; 2 = estreita;; 1 = larga;; 0 = nenhuma.
- **EX042 — Desfecho ausente.** Que desfecho de segurança não foi medido? *Rubrica:* 3 = comprometimento de contas;; 2 = comprometimento;; 1 = redefinições;; 0 = nenhuma.
- **EX043 — Implicações para o hospital.** O que Sofia recomendou ao hospital? *Rubrica:* 3 = manter a mudança, treinar no gerenciador e acompanhar comprometimentos;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX044 — Três níveis.** Em quais três níveis as implicações são declaradas? *Rubrica:* 3 = hospital, outros hospitais e políticas;; 2 = dois;; 1 = nada;; 0 = nenhuma.

### Síntese

Verificações de robustez e limitações direcionais tornam as conclusões de uma dissertação críveis e com o escopo correto.

<a id="ch-08"></a>

## Capítulo 8 — Revisão independente e defesa

### Objetivos de aprendizagem

Você vai (1) preparar-se para a avaliação independente; (2) responder a questionamentos sobre métodos e ética; (3) compartilhar os achados com responsabilidade com a organização parceira.

### 8.1 Revisão independente

Antes da entrega, Sofia pede a um pesquisador de outra instituição que leia a dissertação como um examinador leria. O revisor questiona se a amostra da pesquisa anterior era comparável e pede as taxas de resposta por grupo de funcionários. Sofia acrescenta uma tabela mostrando que as duas pesquisas tinham proporções semelhantes de profissionais de enfermagem, médicos e administrativos. O revisor também sugere esclarecer como ela chegou à saturação nas entrevistas. Uma leitura independente encontra lacunas que um orientador que acompanhou o trabalho de perto talvez já não perceba. Ela agradece ao revisor nos agradecimentos.

### 8.2 A defesa

Na defesa, os examinadores perguntam por que ela não fez um ensaio randomizado. Ela explica que a mudança de política valeu para o hospital inteiro de uma só vez, o que tornava a randomização impossível, e que a série temporal interrompida é um desenho reconhecido para esses casos. Perguntam sobre ética: se os entrevistados se sentiam seguros para criticar a TI. Ela descreve o recrutamento por meio de um aviso neutro e as citações feitas apenas pela função. Os examinadores observam que suas respostas mostram que ela entende os tradeoffs do desenho, em vez de defendê-lo como perfeito. São pedidas apenas correções menores.

### 8.3 Compartilhar com o hospital

Sofia apresenta os achados ao grupo de governança da informação do hospital. Mostra apenas resultados agregados, sem citações que possam identificar funcionários, e explica as limitações em termos simples. O grupo decide manter a política e financiar o treinamento no gerenciador de senhas. Perguntam se podem dizer que a segurança melhorou; Sofia os orienta a dizer que o ônus caiu e que os desfechos de segurança não foram medidos. Compartilhar com responsabilidade garante que a pesquisa informe decisões sem ser esticada além do que mostra. Ela deixa com o grupo um resumo de duas páginas para referência futura.

### 8.4 Depois do diploma

Sofia publica um artigo curto com o Dr. Nakamura e compartilha seus dados anonimizados e seu código. O hospital pede que ela lidere a implantação do treinamento e que estruture o monitoramento de indicadores de comprometimento, o que permitiria a um estudo futuro examinar desfechos de segurança. Ela reflete que a habilidade mais importante que aprendeu foi separar o que a evidência mostra daquilo que as pessoas esperam que ela mostre, especialmente quando o resultado sustenta uma mudança que ela própria defendia desde o início. Também mantém contato com o Dr. Nakamura sobre um possível estudo de continuidade comparando vários hospitais, que mostraria se seus achados valem de forma mais ampla.

### Exemplo resolvido

Sofia recorre a um leitor independente, defende as escolhas de desenho e de ética, compartilha achados agregados com redação cuidadosa e segue com o treinamento e o monitoramento.

> **Caso sintético.** As revisões e as decisões são sintéticas.

### Erros e limites

Os parceiros ainda podem exagerar os achados. O desempenho na defesa depende da preparação tanto quanto da qualidade do trabalho.

### Exercícios

- **EX045 — Tabela de comparabilidade.** O que Sofia acrescentou depois da revisão independente? *Rubrica:* 3 = uma tabela das proporções de grupos de funcionários nas duas pesquisas;; 2 = comparabilidade;; 1 = nada;; 0 = nenhuma.
- **EX046 — Sem randomização.** Por que um ensaio randomizado era impossível? *Rubrica:* 3 = a política valeu para o hospital inteiro de uma vez;; 2 = hospital inteiro;; 1 = custo;; 0 = nenhuma.
- **EX047 — Crítica segura.** Como ela ajudou os entrevistados a se sentirem seguros para criticar a TI? *Rubrica:* 3 = recrutamento neutro e citações apenas pela função;; 2 = neutro;; 1 = nada;; 0 = nenhuma.
- **EX048 — Afirmação correta.** O que o hospital deve dizer sobre segurança? *Rubrica:* 3 = o ônus caiu; os desfechos de segurança não foram medidos;; 2 = ônus;; 1 = a segurança melhorou;; 0 = nenhuma.
- **EX049 — Decisão do hospital.** O que o grupo de governança decidiu? *Rubrica:* 3 = manter a política e financiar o treinamento no gerenciador;; 2 = os dois;; 1 = reverter;; 0 = nenhuma.
- **EX050 — Habilidade principal.** Que habilidade Sofia mais valoriza? *Rubrica:* 3 = separar o que a evidência mostra do que as pessoas esperam;; 2 = evidência;; 1 = nada;; 0 = nenhuma.

### Síntese

Revisão independente, uma defesa fundamentada e comunicação cuidadosa levam as descobertas de uma dissertação à prática com responsabilidade.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Sofia Lindqvist, o Dr. Paul Nakamura, o Harrowgate Institute, o Orchard Lane Hospital Trust e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Se os pedidos de redefinição caíram e os relatos de reutilização de senhas diminuíram depois do fim das trocas obrigatórias e da oferta de um gerenciador.

**EX002.** Porque mostrou que regras de senha exigentes levavam os funcionários a anotar e reutilizar senhas.

**EX003.** A data, a base, a string de busca e o número de resultados.

**EX004.** Para mostrar que a busca não foi seletiva e pode ser repetida.

**EX005.** Porque as orientações declaram posições recomendadas, e não efeitos medidos.

**EX006.** Poucos estudos medem o que acontece em um hospital depois de uma mudança na política de senhas.

**EX007.** Herley (2009).

**EX008.** Atitudes, normas sociais e controle comportamental percebido.

**EX009.** Que o esforço liberado pode aumentar o cumprimento de outras regras, como o bloqueio de tela.

**EX010.** Muitas vezes explica melhor as intenções do que as ações reais, que frequentemente são hábitos.

**EX011.** Porque presumem que a informação, sozinha, mudará o comportamento.

**EX012.** Quando leva a previsões mensuráveis.

**EX013.** A adoção do gerenciador ligada a atitudes e normas, e mais bloqueio de tela graças ao esforço liberado.

**EX014.** Porque o próprio orçamento é difícil de medir diretamente.

**EX015.** Uma série temporal interrompida das contagens de redefinições, um questionário anônimo com os funcionários e entrevistas.

**EX016.** Não pede nomes nem senhas reais, apenas hábitos.

**EX017.** Porque os colegas poderiam se sentir incapazes de recusar.

**EX018.** Normalizando o comportamento na redação da pergunta e perguntando com que frequência, em vez de sim ou não.

**EX019.** Porque a reutilização tende a ser sub-relatada, de modo que as mudanças são mais confiáveis do que os níveis.

**EX020.** O esquema de codificação e as contagens, já que as transcrições poderiam identificar funcionários.

**EX021.** O fim das trocas obrigatórias, o gerenciador de senhas e a ferramenta de autoatendimento, entre outras.

**EX022.** Somando as contagens de redefinições por autoatendimento às do service desk.

**EX023.** Usando redefinições por mil contas ativas.

**EX024.** Uma queda de nível de 18,8 redefinições por 1.000 contas (56,9 previstas, 38,1 ajustadas), com mudança de inclinação de apenas +0,09 por mês.

**EX025.** Porque aconteceu quatro meses depois da mudança.

**EX026.** A de que o gerenciador de senhas contribuiu para a queda.

**EX027.** Nenhuma queda nas redefinições por mil contas no ponto da mudança, ou mais relatos de anotação de senhas.

**EX028.** Um registro de riscos para atrasos no acesso aos dados.

**EX029.** "Gerenciador de senhas", que alguns entendiam como as senhas salvas no navegador.

**EX030.** Começar por uma experiência recente e específica, como a última senha esquecida, antes das opiniões mais amplas.

**EX031.** Não; os dados do piloto ficam de fora, e isso está declarado no plano.

**EX032.** Que pesquisadores e participantes usam as mesmas palavras com significados diferentes.

**EX033.** Porque uma pesquisa anônima anterior fez duas perguntas com redação idêntica.

**EX034.** 390 antes da mudança e 412 depois.

**EX035.** Caiu de 21,0% para 15,0%, uma queda de 6 pontos com intervalo bootstrap de -11,3 a -0,8 pontos.

**EX036.** Porque pesquisas anônimas não conseguem ligar respostas das mesmas pessoas.

**EX037.** Porque foi introduzido sem treinamento.

**EX038.** A previsão do orçamento de compliance de que reduzir o ônus ajuda.

**EX039.** O capítulo de métodos primeiro e a introdução por último.

**EX040.** Se um único mês atípico determina o resultado.

**EX041.** A mudança de nível ficou entre -19,3 e -17,8 redefinições por 1.000 contas, contra -18,8 com todos os meses.

**EX042.** O comprometimento de contas, porque os dados não estavam disponíveis.

**EX043.** Manter a mudança, oferecer treinamento no gerenciador de senhas e acompanhar indicadores de comprometimento.

**EX044.** Para o hospital, para outros hospitais e para as políticas.

**EX045.** Uma tabela mostrando proporções semelhantes de grupos de funcionários nas duas pesquisas.

**EX046.** Porque a política mudou para o hospital inteiro de uma só vez.

**EX047.** Recrutando por meio de um aviso neutro e citando apenas pela função.

**EX048.** Que o ônus caiu, enquanto os desfechos de segurança não foram medidos.

**EX049.** Manter a política e financiar o treinamento no gerenciador de senhas.

**EX050.** Separar o que a evidência mostra daquilo que as pessoas esperam que ela mostre.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes*, 50(2), 179–211. <https://doi.org/10.1016/0749-5978(91)90020-T>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Beautement, A., Sasse, M. A., & Wonham, M. (2008). The compliance budget: Managing security behaviour in organisations. *Proceedings of the 2008 New Security Paradigms Workshop*, 47–58. <https://doi.org/10.1145/1595676.1595684>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
