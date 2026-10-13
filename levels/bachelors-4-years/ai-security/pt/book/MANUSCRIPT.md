# Segurança de IA e Aprendizado de Máquina: Livro do Curso de Bacharelado

- Idioma: português do Brasil (`pt`); bacharelado, quatro anos; aproximadamente 3.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 40 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3; os capítulos 11–40 (EX031–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de segurança e computação em sentido amplo que precisam de uma base rigorosa e prática sobre como sistemas de IA são atacados, defendidos, governados e avaliados.
- Relação com os livros vizinhos: o [livro de tecnólogo](../../../../technologist-3-years/ai-security/en/book/MANUSCRIPT.md) é mais voltado à implementação; o [livro de engenharia](../../../../engineering-5-years/ai-security/en/book/MANUSCRIPT.md) dá mais peso ao projeto. **Este livro equilibra teoria, casos, métodos e competências de pesquisa** e termina com um projeto final e uma monografia.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação e não concede autorização para testar sistemas reais. Todas as organizações, pessoas, conjuntos de dados e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Quarenta capítulos acompanham o curso: fundamentos (1–18); teoria, casos, métodos e laboratórios de segurança de IA (19–32); e pesquisa, projeto final e monografia (33–40). Cada capítulo tem objetivos de aprendizagem, texto didático, um exemplo resolvido, erros e limites, três exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios são determinísticos, rodam offline com `python3 arquivo.py` e imprimem os resultados mostrados em *Saída esperada*. São modelos de brinquedo, não defesas de produção.

### O exemplo contínuo (sintético): Lumen Community Health

> **Caso sintético — ficção.** A **Lumen Community Health (LCH)** é uma rede inventada de cinco clínicas. Ela opera o **Ask Lumen**, um chatbot baseado em modelo de linguagem que responde a perguntas de pacientes sobre consultas e serviços das clínicas usando documentos recuperados das clínicas e que pode marcar ou cancelar consultas por meio de uma ferramenta; o **NoShow**, um modelo que prevê faltas a consultas; e o **DocSort**, um modelo que lê cartas de encaminhamento digitalizadas e as encaminha. A estudante *Rina Costa* acompanha a LCH ao longo do curso, em trabalhos de disciplina, num laboratório e no projeto final. Todo número sobre a LCH é inventado; todos os testes acontecem em cópias isoladas, com registros sintéticos de pacientes e autorização por escrito.

### Política de fontes

As fontes foram verificadas em 12 de outubro de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (AI RMF 1.0), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) (Generative AI Profile) e [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025) (taxonomia de ML adversarial); o [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); o [MITRE ATLAS](https://atlas.mitre.org/); o [Regulamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (AI Act); e a [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Os artigos são citados pelo identificador arXiv, e cada um foi aberto e teve o título conferido.

## Sumário

| Parte | Capítulos |
|---|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) ler e escrever enunciados matemáticos precisos; (2) usar técnicas de prova (direta, por contradição, por contraexemplo) para raciocinar sobre afirmações de segurança; (3) trabalhar com funções, vetores e otimização simples; e (4) ver por que um único contraexemplo derruba uma afirmação universal de segurança.

### 1.1 Enunciados e quantificadores

Afirmações de segurança são enunciados matemáticos disfarçados. "O Ask Lumen nunca revela a consulta de outro paciente" significa: *para todas* as entradas e *para todos* os usuários, a saída não contém dados de outro paciente. Um enunciado universal ("para todo") é refutado por um contraexemplo; um enunciado existencial ("existe um ataque") é provado exibindo-se um. Essa assimetria explica por que os atacantes levam vantagem: precisam de uma entrada que funcione, enquanto os defensores precisam cobrir todas. Escrever a afirmação por extenso expõe o que precisa ser verificado: cada usuário, cada entrada, cada caminho pelo qual os dados chegam à saída, incluindo documentos recuperados e resultados de ferramentas.

### 1.2 Técnicas de prova

A *prova direta* deduz a conclusão a partir das hipóteses. A *prova por contradição* supõe o contrário e deduz uma impossibilidade. A *prova por contraexemplo* refuta uma afirmação universal. Em segurança de IA, provas são raras para sistemas inteiros, mas comuns para componentes: "se o serviço de políticas nega toda chamada de ferramenta sem um token válido, então nenhuma marcação não autenticada ocorre" é uma prova direta a partir de uma propriedade do projeto. A prova baseada na propriedade do projeto vale tanto quanto sua hipótese: se algum caminho chega ao sistema de agendamento sem passar pelo serviço de políticas, a conclusão falha. Verificar essa hipótese é uma tarefa de arquitetura, que capítulos posteriores automatizam com busca em grafos.

### 1.3 Funções e vetores

Um modelo é uma função das entradas para as saídas. Entradas como imagens ou registros de atributos são vetores; a distância entre vetores (por exemplo, a distância euclidiana ou a maior diferença absoluta) formaliza a ideia de "pequena mudança". Muitos ataques procuram um vetor próximo que produza uma saída diferente (Szegedy et al., arXiv:1312.6199). A escolha da distância importa. Sob a maior diferença absoluta, todos os atributos podem mudar ao mesmo tempo até um valor fixo; sob a distância euclidiana, uma grande mudança num único atributo consome todo o orçamento. O laboratório de evasão, mais adiante, usa o primeiro tipo, de modo que o tamanho da perturbação eps limita separadamente a mudança em cada coordenada. Uma afirmação de robustez não significa nada até que a distância e seu tamanho sejam declarados.

### 1.4 Otimização

O treinamento minimiza uma função de perda; os ataques a maximizam (ou minimizam a distância sujeita a uma saída alterada). Ambos são problemas de otimização, e é por isso que as mesmas ferramentas matemáticas — gradientes, restrições, busca — aparecem dos dois lados. O laboratório de evasão mostra os dois lados em poucas linhas. O treinamento ajusta os pesos no sentido oposto ao gradiente da perda para reduzir o erro; o ataque move cada ponto de teste no sentido do sinal do mesmo gradiente em relação à entrada para aumentar o erro. Com eps de 0.5, a acurácia do modelo de brinquedo cai de 0.985 para 0.840, o que mostra quão pouco esforço uma busca guiada pelo gradiente exige quando o modelo é simples.

### 1.5 Exemplo resolvido (caso sintético da LCH)

O fornecedor da LCH afirmou: "O NoShow não pode ser manipulado por pacientes." Rina reescreveu isso como um enunciado universal: para todos os pacientes e todos os valores dos campos que os pacientes controlam (preferências de contato, motivo declarado da consulta), a previsão não muda num sentido que o paciente prefira. Em seguida, encontrou um contraexemplo num registro sintético: mudar o "motivo" de "retorno" para "urgente" baixou o risco previsto de falta de 0.42 para 0.18, o que poderia fazer um paciente subir numa lista de lembretes. A afirmação, tal como foi feita, era falsa; o fornecedor a revisou.

### 1.6 Erros e limites

Três erros são comuns: aceitar afirmações universais testadas em poucos exemplos; confundir "nenhum ataque encontrado" com "nenhum ataque existe"; e noções vagas de "pequena mudança", sem medida de distância. O exemplo do NoShow mostra os três. A afirmação do fornecedor foi testada apenas em registros comuns; ninguém havia procurado uma mudança num campo que os pacientes controlam; e "manipulado" não tinha medida declarada. O contraexemplo de Rina, uma mudança de 0.42 para 0.18 causada por um único campo, resolveu a questão de imediato. Uma afirmação revisada nomearia os campos, o tamanho de mudança considerado aceitável e a forma como foi testada.

### Exercícios

- **EX001 — Quantificadores.** Escreva "o filtro bloqueia todas as tentativas de injeção" com quantificadores explícitos e diga o que a refuta. Rubrica: 3 = ∀ entradas da classe, bloqueadas; uma instância não bloqueada refuta; 2 = parcial; 1 = vago; 0 = nenhuma.
- **EX002 — Contraexemplo.** Por que um único registro refutou a afirmação do fornecedor? Rubrica: 3 = afirmação universal falseada por uma instância; 2 = parcial; 1 = vago; 0 = errado.
- **EX003 — Distância.** Para x = (1, 2, 3) e y = (1.5, 2, 2), calcule as distâncias euclidiana e de maior diferença absoluta. Rubrica: 3 = √(0.25 + 0 + 1) ≈ 1.118 e 1; 2 = uma; 1 = método; 0 = nenhuma.

### Síntese

O raciocínio matemático torna precisas as afirmações de segurança. Afirmações universais exigem evidências fortes; um contraexemplo basta para refutá-las; "pequeno" exige uma distância.

### Continue estudando — capítulo 01 de 40

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever como computadores, sistemas operacionais, redes e serviços em nuvem se encaixam; (2) identificar onde uma aplicação de IA roda e armazena dados; (3) explicar o modelo de responsabilidade compartilhada para nuvem e IA hospedada; e (4) mapear um serviço de IA em seus componentes computacionais.

### 2.1 Camadas de um sistema computacional

O hardware executa um sistema operacional, que executa aplicações; as aplicações conversam pela rede com outros serviços, muitas vezes na nuvem. Uma aplicação de IA acrescenta arquivos de modelo, servidores de inferência, bancos de dados vetoriais e conexões com APIs externas de modelos. Cada camada tem seus próprios responsáveis e modos de falha. No Ask Lumen, as partes extras são o modelo hospedado, o banco de dados vetorial com documentos das clínicas e a ferramenta de agendamento. Cada uma acrescenta responsáveis: o provedor do modelo, a equipe de dados da LCH e os administradores do sistema de agendamento. Um problema de segurança em qualquer uma delas, como um banco de dados mal configurado, afeta o chatbot mesmo que o modelo em si funcione corretamente. Conhecer as camadas diz a Rina a quem perguntar sobre cada risco.

### 2.2 Onde a IA roda

Um modelo pode rodar no dispositivo do usuário, nos servidores da organização ou num provedor, por meio de uma API. Cada escolha muda quem pode ver os dados, quem pode alterar o modelo e quem pode testá-lo. APIs de IA hospedada processam os prompts na infraestrutura do provedor; a organização controla apenas seu próprio código, sua configuração e os dados que envia. O Ask Lumen usa uma API hospedada, então a LCH não pode inspecionar os pesos do modelo nem corrigi-lo; pode apenas escolher o que enviar e como tratar o que volta. Isso faz do próprio código da LCH, a parte que monta os prompts e verifica as saídas, o principal lugar onde controles podem ser acrescentados.

### 2.3 Responsabilidade compartilhada

Na computação em nuvem, o provedor protege a infraestrutura e o cliente protege o que coloca sobre ela. Na IA hospedada, o provedor costuma responder pela hospedagem do modelo e pela segurança da plataforma; o cliente responde pelos dados que envia, por como as saídas são usadas, pelas ferramentas que o modelo pode acionar e por quem pode acessar a aplicação. Entender mal essa divisão é uma causa comum de incidentes. No mapa de Rina, a conta de serviço de agendamento é o exemplo mais claro: o provedor do modelo não tem nenhum controle sobre o que essa conta pode fazer no sistema de agendamento da LCH.

### 2.4 Mapeamento de um serviço de IA

Liste: interface do usuário; servidor de aplicação; modelo (onde roda e qual versão); repositório de recuperação; ferramentas e os sistemas que elas tocam; logs; identidades usadas em cada etapa. Esse mapa é o ponto de partida de todos os capítulos seguintes. Cada item responde a uma pergunta que um atacante ou investigador faria: onde a entrada chega, onde os dados ficam, o que o sistema pode alterar e sob qual identidade. Um mapa que lista apenas o modelo deixa de fora a maior parte da superfície de ataque, porque no Ask Lumen as ações arriscadas acontecem pela ferramenta de agendamento e pelo repositório de recuperação. Rina mantém seu mapa num documento compartilhado e o atualiza sempre que a LCH muda um componente.

### 2.5 Exemplo resolvido (caso sintético da LCH)

Rina mapeou o Ask Lumen: widget de chat na web → servidor de aplicação da LCH (máquina virtual na nuvem) → API hospedada do modelo de linguagem (provedor) → recuperação a partir de um banco de dados vetorial de documentos das clínicas (gerido pela LCH) → ferramenta de agendamento que chama o sistema de agendamento (local) usando uma conta de serviço. Os logs iam para o serviço de logs do provedor de nuvem. Rina observou que a conta de serviço de agendamento podia marcar consultas para qualquer paciente — uma responsabilidade que cabe à LCH, e não ao provedor do modelo, corrigir.

O mapa também mostra quem precisa agir em cada achado: a conta de serviço pertence à equipe de agendamento da LCH, e a correção é restringi-la ao paciente cuja sessão fez o pedido.

### 2.6 Erros e limites

Três erros são comuns: supor que o provedor do modelo protege a aplicação inteira; esquecer ferramentas e logs no mapa; e não saber qual versão do modelo está em uso. Cada erro esconde parte do risco. Supor que o provedor protege tudo deixa a conta de serviço da LCH sem exame. Deixar de fora ferramentas e logs esconde os caminhos pelos quais o chatbot pode agir sobre dados de pacientes ou registrá-los. Não saber a versão do modelo torna impossível dizer se uma mudança de comportamento veio de uma atualização do modelo pelo provedor ou do próprio código da LCH.

### Exercícios

- **EX004 — Responsabilidade.** Para o Ask Lumen, liste duas responsabilidades do provedor e três da LCH. Rubrica: 3 = divisão correta; 2 = erro menor; 1 = confuso; 0 = nenhuma.
- **EX005 — Mapa.** Mapeie um assistente de IA para tarefas escolares nos sete componentes de 2.4. Rubrica: 3 = os sete plausíveis; 2 = cinco; 1 = três; 0 = nenhum.
- **EX006 — Escolha de implantação.** Dê uma vantagem de segurança dos modelos no dispositivo e uma das APIs hospedadas. Rubrica: 3 = dados ficam no local vs correções/escala geridas pelo provedor; 2 = uma; 1 = vago; 0 = errado.

### Síntese

Aplicações de IA são sistemas computacionais com partes extras. Mapear onde cada parte roda e quem responde por ela é o primeiro passo de segurança.

### Continue estudando — capítulo 02 de 40

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas simples em Python com variáveis, condições, laços, funções e listas; (2) ler os laboratórios deste livro; (3) tratar entradas com segurança; e (4) testar funções pequenas.

### 3.1 Por que a programação importa para a segurança de IA

O trabalho de segurança precisa de evidências, e as evidências vêm de executar coisas: avaliar um modelo num conjunto de teste, analisar logs, verificar arquivos. Mesmo programas curtos deixam você mais rápido e mais preciso. Os laboratórios deste livro usam apenas a biblioteca padrão do Python, para rodar em qualquer computador. O primeiro script útil de Rina mediu com que frequência as respostas de teste do Ask Lumen citavam um documento das clínicas, uma verificação que levaria horas à mão. Escrevê-lo também a obrigou a definir o que contava como citação, uma pergunta mais precisa do que aquela com que havia começado. Laboratórios só com a biblioteca padrão evitam problemas de dependências, de modo que um colega pode reexecutar o trabalho dela e obter os mesmos números.

### 3.2 Construções básicas

Variáveis guardam valores; `if` escolhe; `for` repete; funções empacotam passos; listas e dicionários guardam coleções. Leia o laboratório de evasão abaixo: ele cria dados sintéticos, treina com um laço um pequeno modelo de regressão logística e depois mede a acurácia à medida que uma perturbação cresce. Você ainda não precisa entender cada linha — concentre-se na estrutura: dados, treinamento, avaliação, impressão.

```python
"""Lab E: evasion of a toy linear classifier (synthetic data, stdlib only).
Trains logistic regression on two synthetic clusters, then applies a
fast-gradient-sign (FGSM-style) perturbation of size eps to every test point
and reports clean vs adversarial accuracy. Teaching model only."""
import math, random
rng = random.Random(7)
def point(label):
    cx = 1.0 if label else -1.0
    return [rng.gauss(cx, 0.7), rng.gauss(cx, 0.7)], label
train = [point(i % 2) for i in range(400)]
test = [point(i % 2) for i in range(200)]
w, b = [0.0, 0.0], 0.0
sig = lambda z: 1 / (1 + math.exp(-z))
for epoch in range(200):
    gw, gb = [0.0, 0.0], 0.0
    for x, y in train:
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        gw[0] += (p - y)*x[0]; gw[1] += (p - y)*x[1]; gb += p - y
    w = [w[i] - 0.1*gw[i]/len(train) for i in range(2)]; b -= 0.1*gb/len(train)
def acc(data, eps):
    ok = 0
    for x, y in data:
        # gradient of the loss w.r.t. x is (p - y) * w; FGSM steps along its sign
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        xa = [x[i] + eps*math.copysign(1, (p - y)*w[i]) for i in range(2)]
        ok += (sig(w[0]*xa[0] + w[1]*xa[1] + b) >= 0.5) == bool(y)
    return ok / len(data)
print(f"weights w=({w[0]:.3f}, {w[1]:.3f}) b={b:.3f}")
for eps in (0.0, 0.25, 0.5, 0.75, 1.0):
    print(f"eps={eps:.2f} accuracy={acc(test, eps):.3f}")
```

Saída esperada:

```text
weights w=(1.795, 1.756) b=-0.080
eps=0.00 accuracy=0.985
eps=0.25 accuracy=0.950
eps=0.50 accuracy=0.840
eps=0.75 accuracy=0.660
eps=1.00 accuracy=0.505
```

A saída mostra o padrão com clareza: a acurácia é 0.985 sem perturbação e cai para 0.505 quando eps chega a um, perto de um palpite ao acaso. A semente aleatória fixa faz toda execução imprimir os mesmos números.

### 3.3 Tratamento seguro de entradas

Programas que leem arquivos, dados de rede ou saídas de IA devem tratá-los como não confiáveis. Converta texto em números com cuidado, verifique intervalos e nunca execute texto como código. Um erro comum em aplicações com LLM é passar a saída do modelo para um comando ou uma página web sem verificações; o OWASP LLM 2025 chama isso de *tratamento inadequado de saídas* (LLM05). No Ask Lumen, a marcação sugerida pelo modelo é uma entrada como qualquer outra: precisa ser analisada como dado, verificada contra regras e só então passada ao sistema de agendamento. O exemplo resolvido deste capítulo faz exatamente isso, com três verificações sobre o código da clínica, a data e o identificador do paciente.

### 3.4 Testes

Escreva testes pequenos com `assert`: `assert classify(0.9) == "high"`. Teste casos-limite — entrada vazia, valores extremos, tipos errados. Testes tornam seguro alterar o código depois. Na verificação de marcações de Rina, os casos-limite incluem uma data exatamente 90 dias à frente, uma data no passado, um código de clínica desconhecido, um identificador de paciente ausente e um pedido com o identificador de outro paciente. Cada caso recebe um teste com o resultado esperado escrito ao lado. Quando ela mais tarde muda a regra de datas, os testes existentes mostram na hora se algo mais quebrou.

### 3.5 Exemplo resolvido (caso sintético da LCH)

Rina escreveu uma função que verifica um pedido de marcação produzido pelo Ask Lumen antes que ele chegue ao sistema de agendamento: o código da clínica deve ser um dos cinco códigos conhecidos, a data deve estar dentro de 90 dias e o identificador do paciente deve corresponder ao usuário conectado. Seus testes incluíram um pedido com o identificador de outro paciente, que a função rejeitou. Verificar em código, fora do modelo, significa que a regra vale mesmo que um prompt convença o modelo a pedir a marcação de outro paciente.

### 3.6 Erros e limites

Três erros são comuns: copiar código sem entender o que ele faz; confiar na saída da IA como se fosse o seu próprio código; e testar apenas o caso normal. Código copiado pode incluir comportamentos que quem copiou nunca notou, como uma chamada insegura que executa texto como comando. Confiar na saída da IA como se fosse o seu próprio código repete esse erro com um autor menos cuidadoso. Testar apenas o caso normal deixa sem teste exatamente os caminhos que um atacante usa; o teste de Rina com o identificador de outro paciente é o tipo que pega problemas reais.

### Exercícios

- **EX007 — Estrutura do laboratório.** Identifique as partes de dados, treinamento, avaliação e saída do laboratório de evasão. Rubrica: 3 = as quatro localizadas corretamente; 2 = três; 1 = uma ou duas; 0 = nenhuma.
- **EX008 — Leitura do laboratório.** Que acurácia o laboratório informa com eps 0.00 e 0.50? Rubrica: 3 = 0.985 e 0.840; 2 = uma; 1 = aproximada; 0 = errada.
- **EX009 — Validação.** Liste as três verificações da função de marcação de Rina e mais uma que ela poderia acrescentar. Rubrica: 3 = código da clínica, janela de datas, correspondência do paciente + extra sensato (formato do horário, limite de taxa); 2 = só as três; 1 = uma ou duas; 0 = nenhuma.

### Síntese

A programação transforma ideias de segurança em evidências. Leia os laboratórios pela estrutura, trate toda entrada externa — inclusive a saída da IA — como não confiável e teste os limites.

### Continue estudando — capítulo 03 de 40

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) escrever prosa acadêmica clara, com afirmações apoiadas em evidências; (2) citar fontes corretamente e verificar cada citação; (3) distinguir pesquisa revisada por pares, preprints, normas e literatura cinzenta; e (4) evitar plágio, incluindo o mau uso de ferramentas de escrita com IA.

### 4.1 Afirmações e evidências

Toda afirmação substantiva precisa de apoio: dados que você produziu, uma fonte citada ou um argumento claro. Em segurança de IA, afirmações sobre ataques e defesas devem declarar as condições: qual modelo, qual ataque, qual métrica. "O treinamento adversarial torna os modelos robustos" é amplo demais; "o treinamento adversarial com descida de gradiente projetada melhorou a robustez a perturbações limitadas nos benchmarks de imagem avaliados (Madry et al., arXiv:1706.06083)" é sustentável. A versão sustentável nomeia o método, o modelo de ameaça e o escopo da avaliação, para que o leitor possa dizer se ela se aplica ao seu sistema. Uma afirmação sobre benchmarks de imagem diz pouco sobre um chatbot de texto como o Ask Lumen.

### 4.2 Citação e verificação

Cite o que você de fato leu e verifique se cada referência existe: abra o DOI, a página do arXiv ou a URL oficial. Não invente identificadores. Assistentes de escrita com IA podem produzir referências plausíveis, mas inexistentes; cada citação que você entrega é sua responsabilidade. Use um estilo consistente e inclua informação suficiente para que o leitor encontre a fonte. O exemplo resolvido de Rina mostra que o risco é real: uma de seis referências produzidas com um assistente não existia. Verificar leva minutos por referência e protege a credibilidade do ensaio. Ela registra onde verificou cada uma, como a página do DOI, para que o avaliador possa seguir o mesmo caminho.

### 4.3 Tipos de fontes

Artigos revisados por pares foram examinados por especialistas; preprints (por exemplo, no arXiv) costumam ser importantes em segurança de IA, mas não passaram por revisão; normas e frameworks (NIST AI 100-1, ISO/IEC 42001) definem termos e práticas; blogs de fornecedores e notícias são pistas úteis, mas evidências fracas. O tipo de fonte determina como uma afirmação é redigida. Um resultado revisado por pares pode ser citado como achado sob suas condições declaradas; um preprint, como resultado relatado ainda não revisado; um blog de fornecedor, como alegação. Nos ensaios de Rina, uma afirmação apoiada apenas num blog de fornecedor é escrita como "o fornecedor afirma", o que diz ao leitor quanto peso lhe dar.

### 4.4 Integridade e ferramentas de IA

Siga a política da sua instituição sobre ferramentas de IA. Em geral, você precisa declarar o uso, verificar a saída e nunca apresentar texto ou análise gerados como trabalho seu sem permissão. Parafrasear sem citar é plágio. A declaração permite que os avaliadores julguem o trabalho com justiça e que os leitores saibam quais partes verificar com mais atenção. A declaração de Rina informa a ferramenta, a tarefa em que ela ajudou e como Rina verificou a saída. A referência inventada no rascunho dela mostra por que verificar importa: a ferramenta a produziu com confiança, e só a verificação a expôs.

### 4.5 Exemplo resolvido (caso sintético da LCH)

O primeiro rascunho de ensaio de Rina, produzido em parte com um assistente de IA, continha seis referências. Ela as verificou: quatro existiam, uma tinha o ano errado e uma não existia. Ela removeu a referência inventada, corrigiu o ano, declarou o uso da ferramenta e reescreveu o parágrafo que dependia da fonte falsa usando uma fonte real que havia lido. Uma taxa de uma referência fabricada em seis é alta o bastante para que ela agora verifique cada referência antes de redigir em torno dela.

### 4.6 Erros e limites

Três erros são comuns: referências não verificadas; afirmações sem condições; e tratar um blog de fornecedor como fato estabelecido. Referências não verificadas podem estar erradas ou ser inventadas, como mostrou o rascunho de Rina, e uma única falsa faz os leitores duvidarem das demais. Afirmações sem condições, como "o treinamento adversarial torna os modelos robustos", são fáceis de refutar com um contraexemplo vindo de outro cenário. Tratar blogs de fornecedores como fato estabelecido faz passar marketing por evidência. Cada erro é barato de evitar e caro depois que um avaliador ou revisor o encontra.

### Exercícios

- **EX010 — Reescrita.** Reescreva "a injeção de prompt é resolvida por filtros" como uma afirmação sustentável ou como uma refutação com citação. Rubrica: 3 = afirmação condicional citando trabalho real (por exemplo, Greshake et al. arXiv:2302.12173) que mostra que filtros são insuficientes; 2 = parcial; 1 = sem citação; 0 = inalterada.
- **EX011 — Verificação.** Descreva como verificar uma referência do arXiv. Rubrica: 3 = abrir arxiv.org/abs/ID, conferir se título/autores/ano correspondem; 2 = parcial; 1 = vago; 0 = nenhuma.
- **EX012 — Tipo de fonte.** Classifique: NIST AI 600-1; um artigo do arXiv; um blog de empresa. Rubrica: 3 = norma/framework, preprint, literatura cinzenta; 2 = dois; 1 = um; 0 = nenhum.

### Síntese

Escrita acadêmica em segurança de IA significa afirmações condicionais, citações verificadas e uso honesto de ferramentas — competências que também tornam confiáveis os relatórios profissionais.

### Continue estudando — capítulo 04 de 40

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) explicar confidencialidade, integridade e disponibilidade; (2) definir ameaça, vulnerabilidade, risco e controle; (3) descrever ataques comuns (phishing, malware, roubo de credenciais) e suas variantes na era da IA; e (4) aplicar práticas básicas de segurança pessoais e organizacionais.

### 5.1 A tríade CIA

A *confidencialidade* mantém a informação longe de pessoas não autorizadas; a *integridade* a mantém exata e inalterada; a *disponibilidade* mantém os sistemas utilizáveis quando necessário. Num chatbot de IA: confidencialidade dos dados de pacientes nas conversas; integridade das respostas e das marcações; disponibilidade do serviço. No Ask Lumen, uma falha de confidencialidade seria mostrar a um paciente a consulta de outro; uma falha de integridade seria uma resposta errada sobre o horário de uma clínica ou uma marcação feita para a pessoa errada; uma falha de disponibilidade seria o chatbot ficar inutilizável numa manhã movimentada. Cada uma exige controles diferentes, então nomear a propriedade em risco ajuda a escolher o controle certo.

### 5.2 Vocabulário de risco

Uma *ameaça* é algo que pode causar dano (um atacante, um acidente). Uma *vulnerabilidade* é uma fraqueza. O *risco* combina probabilidade e impacto. Um *controle* reduz o risco. Um vocabulário preciso ajuda as equipes a concordar sobre prioridades. Aplicado ao Ask Lumen: uma ameaça é um paciente tentando ver as consultas de outro; a vulnerabilidade é a conta de serviço de agendamento que pode agir por qualquer paciente; o risco é a probabilidade dessa combinação vezes o dano de dados de saúde expostos; o controle é uma verificação de política que vincula cada marcação ao paciente conectado. Usar as palavras de forma consistente impede que as discussões misturem problemas com soluções.

### 5.3 Ataques clássicos e variantes com IA

O phishing engana pessoas para que revelem credenciais; a IA pode gerar phishing mais convincente e personalizado, além de clones de voz. O malware compromete dispositivos; código gerado por IA pode conter vulnerabilidades se for aceito sem crítica. O roubo de credenciais dá acesso aos atacantes; credenciais coladas em chatbots podem vazar. E os sistemas de IA introduzem novos tipos de ataque: injeção de prompt, envenenamento de dados, extração de modelo e evasão. Os novos tipos de ataque afetam as mesmas três propriedades: a injeção de prompt ameaça a integridade das ações, a extração ameaça a confidencialidade do modelo, o envenenamento ameaça a integridade dos dados de treinamento.

### 5.4 Práticas básicas

Use autenticação multifator, mantenha o software atualizado, aplique o menor privilégio, faça backup de dados importantes e relate eventos suspeitos. Para ferramentas de IA: não cole segredos ou dados pessoais em serviços não aprovados, verifique as saídas antes de agir e siga a política da organização sobre ferramentas aprovadas. Essas práticas valem para o trabalho com IA tanto quanto para qualquer outro: uma chave de API do provedor do modelo é uma credencial que exige o mesmo cuidado que uma senha. Na LCH, os funcionários são informados sobre quais ferramentas de IA estão aprovadas para trabalho envolvendo pacientes e de que dados de pacientes nunca devem ser colados em outras. Verificar a saída da IA antes de agir com base nela é o hábito que teria pegado a referência inventada de Rina.

### 5.5 Exemplo resolvido (caso sintético da LCH)

Uma recepcionista da LCH recebeu uma mensagem de voz aparentemente de um diretor de clínica pedindo para alterar com urgência os dados bancários de um fornecedor. A sessão de treinamento em letramento em segurança de Rina usou esse caso sintético para discutir clonagem de voz e o controle que a detém: verificar alterações de pagamento por meio de um número de telefone conhecido e de um segundo aprovador, por mais convincente que o pedido pareça. O controle funciona seja a voz real ou clonada, e é por isso que aqui o processo vence a detecção. A LCH também disse aos funcionários que a urgência num pedido de pagamento é, por si só, um motivo para desacelerar e verificar.

### 5.6 Erros e limites

Três erros são comuns: tratar riscos específicos de IA como alheios à segurança clássica; confiar na detecção de falsificações em vez de controles de processo; e colar dados sensíveis em ferramentas públicas de IA. Riscos específicos de IA muitas vezes reutilizam caminhos clássicos: uma voz clonada é phishing por outro meio, e uma chave de API vazada é roubo de credencial. Confiar em identificar falsificações falha à medida que a geração melhora, enquanto a verificação por retorno de ligação continua funcionando. Colar dados sensíveis em ferramentas públicas pode expô-los à retenção pelo provedor e a quem quer que obtenha esses dados depois, por isso a política da LCH nomeia explicitamente as ferramentas aprovadas.

### Exercícios

- **EX013 — CIA.** Dê um exemplo de cada propriedade da tríade CIA para o DocSort. Rubrica: 3 = um exemplo de cada, preciso; 2 = dois; 1 = um; 0 = nenhum.
- **EX014 — Vocabulário.** No caso do clone de voz, indique ameaça, vulnerabilidade, impacto e controle. Rubrica: 3 = os quatro coerentes; 2 = três; 1 = um ou dois; 0 = nenhum.
- **EX015 — Práticas.** Liste três práticas seguras para usar assistentes de IA no trabalho. Rubrica: 3 = nada de segredos/dados pessoais, verificar saídas, só ferramentas aprovadas; 2 = duas; 1 = uma; 0 = nenhuma.

### Síntese

O letramento em segurança — CIA, vocabulário de risco, ataques comuns e práticas básicas — é a base sobre a qual se constrói a segurança específica de IA.

### Continue estudando — capítulo 05 de 40

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) usar conjuntos, relações e grafos para modelar sistemas; (2) expressar regras de acesso como relações e verificá-las; (3) encontrar, num grafo, caminhos de entradas não confiáveis até ações sensíveis; e (4) contar possibilidades para julgar se a força bruta é viável.

### 6.1 Conjuntos e relações

Uma regra de controle de acesso é uma relação entre sujeitos, ações e objetos: (paciente P, marcar, a própria consulta) é permitido; (paciente P, ver, registro de outro paciente) não é. Escrever as regras como conjuntos de triplas permitidas as torna verificáveis por programa e expõe casos ausentes. Uma vez que as regras são um conjunto, um programa pode verificar cada pedido contra ele e listar qualquer ação que não tenha regra alguma. A primeira tentativa de Rina descobriu que "cancelar" não tinha regra para pacientes que cancelassem a consulta de outra pessoa, algo que a política em prosa simplesmente não mencionava. Acrescentar uma negação explícita fechou a lacuna, e o conjunto passou a ser a referência para as verificações de marcação dela.

### 6.2 Grafos

Um grafo tem nós e arestas. Desenhe um sistema de IA como um grafo dirigido: usuário → chatbot → modelo → ferramenta de agendamento → sistema de agendamento, mais repositório de documentos → modelo. Um caminho de um nó não confiável (uma página web pública, um documento enviado) até um nó sensível (a ferramenta de agendamento) é uma rota potencial de ataque. A injeção indireta de prompt segue exatamente esse tipo de caminho (Greshake et al., arXiv:2302.12173). Desenhar o grafo tornou visível uma aresta que o documento de arquitetura não havia registrado: organizações parceiras enviam documentos para o repositório que o modelo lê.

### 6.3 Busca em grafos

A busca em largura encontra todos os nós alcançáveis a partir de um nó inicial. Executá-la a partir de cada nó não confiável e verificar se os nós sensíveis são alcançáveis é uma verificação de arquitetura simples e automatizável. O custo cresce com o número de nós e arestas, então mesmo sistemas grandes podem ser verificados em segundos. O valor está em manter o grafo exato: uma nova origem de envios ou uma nova ferramenta deve ser acrescentada assim que existir, ou a busca relatará um resultado limpo para um sistema que já não corresponde a ele. Rina reexecuta a verificação sempre que o mapa de arquitetura muda e guarda a saída junto do mapa.

### 6.4 Contagem

Se um código de marcação tem 6 dígitos, há 10⁶ possibilidades; a 10 tentativas por segundo, um atacante precisa de cerca de 28 horas para testar todas, então limites de taxa e bloqueios importam. A contagem transforma intuição em números. Com um bloqueio após cinco tentativas erradas, um atacante tem cinco tentativas por conta em vez de um milhão, uma chance de sucesso de cinco em um milhão. A mesma aritmética vale para adivinhar identificadores de pacientes pelo chatbot: se os identificadores são curtos e sequenciais, a enumeração é barata. Rina inclui esses cálculos em suas revisões, para que os ajustes de limite de taxa se apoiem em números, e não em impressões.

### 6.5 Exemplo resolvido (caso sintético da LCH)

Rina listou os nós e as arestas do Ask Lumen e executou à mão uma verificação de alcançabilidade. Duas origens não confiáveis alcançavam a ferramenta de agendamento: o chat dos pacientes (esperado, controlado por autenticação) e os envios de documentos das clínicas por organizações parceiras (inesperado). Os envios dos parceiros podiam conter texto com aparência de instrução que o modelo talvez seguisse. A LCH acrescentou revisão para documentos de parceiros e manteve a ferramenta de agendamento atrás de uma verificação de política vinculada ao paciente conectado. O segundo caminho explica por que os dois controles foram mantidos, em vez de um só: a revisão reduz a chance de texto hostil, e a verificação de política limita seu efeito.

### 6.6 Erros e limites

Três erros são comuns: regras de acesso escritas apenas em prosa; grafos que omitem repositórios de dados e envios; e ignorar a rapidez com que computadores enumeram possibilidades. Regras em prosa deixam casos indefinidos, como mostrou a regra de cancelamento ausente. Grafos que omitem envios e repositórios de dados deixam escapar justamente a rota pela qual a injeção indireta de prompt chega a uma ferramenta. Subestimar a velocidade de enumeração leva a limites fracos para códigos e identificadores; um código de seis dígitos sem limite de taxa cai em cerca de um dia a apenas dez tentativas por segundo, e muito mais rápido com mais.

### Exercícios

- **EX016 — Relação.** Escreva três triplas permitidas e duas proibidas para o Ask Lumen. Rubrica: 3 = cinco triplas sensatas; 2 = quatro; 1 = duas; 0 = nenhuma.
- **EX017 — Caminhos.** Nomeie o caminho inesperado que Rina encontrou e um controle. Rubrica: 3 = envios de parceiros → modelo → agendamento; revisão mais política vinculada ao paciente; 2 = só o caminho; 1 = vago; 0 = nenhum.
- **EX018 — Contagem.** Um código de 4 dígitos a 5 tentativas por segundo: tempo no pior caso? Rubrica: 3 = 10,000/5 = 2,000 s ≈ 33 min; 2 = deslize; 1 = método; 0 = nenhum.

### Síntese

As estruturas discretas oferecem ferramentas exatas — relações para regras, grafos para fluxo de dados, contagem para viabilidade — que tornam visíveis as fraquezas de sistemas de IA.

### Continue estudando — capítulo 06 de 40

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar como uma requisição de chatbot atravessa a internet (DNS, TCP, TLS, HTTP); (2) descrever o que o TLS protege e o que não protege; (3) explicar autenticação de APIs e limitação de taxa; e (4) relacionar controles de rede a ameaças de IA como extração e esgotamento de recursos.

### 7.1 O caminho de uma requisição

O navegador consulta o domínio do chatbot (DNS), conecta-se (TCP), estabelece um canal cifrado e autenticado (TLS) e envia uma requisição HTTP contendo a mensagem. O servidor de aplicação, por sua vez, pode chamar uma API de modelo por outra conexão TLS. Cada etapa deixa um registro que pode ajudar numa investigação: a consulta DNS, o handshake TLS no balanceador de carga, a requisição HTTP no servidor de aplicação e a chamada de saída ao provedor do modelo. No Ask Lumen, uma única mensagem de paciente atravessa, portanto, duas conexões cifradas, e o servidor de aplicação é o único lugar onde o texto em claro fica visível para a LCH. É ali que ficam as verificações de entrada, o registro em log e as decisões de política.

### 7.2 O que o TLS faz e o que não faz

O TLS protege os dados em trânsito contra escuta e adulteração e autentica o servidor. Não protege contra uma mensagem maliciosa de um usuário autenticado, contra injeção de prompt dentro do conteúdo nem contra o mau uso dos dados depois que chegam. No Ask Lumen, o TLS garante que a mensagem de um paciente chegue ao servidor da LCH sem ser lida nem alterada e que o paciente esteja falando com o site verdadeiro da LCH. Não faz nada quanto a um paciente que digita uma instrução feita para manipular o modelo, ou a um documento de parceiro que carrega texto oculto. Esses problemas estão dentro do canal protegido e exigem controles na aplicação.

### 7.3 Autenticação de APIs e limitação de taxa

As APIs autenticam quem as chama com chaves ou tokens. Limites de taxa e cotas restringem quanto cada chamador pode usar. Em APIs de IA, os custos crescem com os tokens, então os limites devem contar tokens, e não apenas requisições. O OWASP LLM10 (*consumo ilimitado*) abrange ataques que esgotam recursos ou orçamentos.

```python
"""Lab R: token-bucket limits against unbounded consumption (synthetic).
Simulates 60 seconds of requests from a normal client and a flooding client
against a model endpoint with a per-client token bucket."""
import random
rng = random.Random(4)
def simulate(rate_per_s, burst, reqs):
    tokens, last, ok = burst, 0.0, 0
    for t in reqs:
        tokens = min(burst, tokens + (t - last) * rate_per_s); last = t
        if tokens >= 1: tokens -= 1; ok += 1
    return ok
normal = sorted(rng.uniform(0, 60) for _ in range(90))
flood = sorted(rng.uniform(0, 60) for _ in range(3000))
for rate, burst in ((5, 20), (2, 10), (1, 5)):
    print(f"limit={rate}/s burst={burst:2d} normal_served={simulate(rate, burst, normal):3d}/90 "
          f"flood_served={simulate(rate, burst, flood):4d}/3000")
```

Saída esperada:

```text
limit=5/s burst=20 normal_served= 90/90 flood_served= 319/3000
limit=2/s burst=10 normal_served= 90/90 flood_served= 129/3000
limit=1/s burst= 5 normal_served= 62/90 flood_served=  64/3000
```

O Lab R mostra o compromisso. A 5 requisições por segundo com rajada de 20, toda requisição normal é atendida e a inundação obtém 319 de 3.000. A 1 por segundo com rajada de 5, a inundação cai para 64, mas o cliente normal perde 28 de suas 90 requisições. Um limite deve ser definido a partir do uso normal medido, e não escolhido apenas para deter ataques.

### 7.4 Ameaças de IA no nível da rede

Consultas sistemáticas podem copiar um modelo (Tramèr et al., arXiv:1609.02943). Inundações de prompts longos podem esgotar a capacidade. Controles de rede — autenticação, cotas, monitoramento, segmentação e filtragem de saída — reduzem esses riscos e limitam o que um componente comprometido consegue alcançar. A extração exige muitas consultas, então cotas por cliente e monitoramento de padrões incomuns de consulta aumentam seu custo. A filtragem de saída importa se um componente for comprometido: um servidor de inferência que só alcança o provedor do modelo não consegue enviar dados para outro lugar. A segmentação mantém os servidores do chatbot separados do banco de dados de agendamento, exceto pela interface estreita da ferramenta de agendamento.

### 7.5 Exemplo resolvido (caso sintético da LCH)

O endpoint público de chat do Ask Lumen não tinha limites por sessão. Um teste de carga sintético que enviava prompts longos multiplicou por dez os custos do modelo em uma hora. A LCH acrescentou cotas de tokens por sessão, um tamanho máximo de mensagem e um alerta quando os gastos passam de 150% da mediana diária. Contar tokens em vez de requisições foi a mudança decisiva: alguns poucos prompts muito longos haviam custado mais do que milhares de mensagens normais. O limiar de alerta de 150% da mediana diária pega o abuso em poucas horas e ignora a alta normal das manhãs movimentadas, e o tamanho máximo de mensagem impede que um único prompt consuma uma grande parte do orçamento.

### 7.6 Erros e limites

Três erros são comuns: acreditar que o TLS resolve ataques no nível da aplicação; limites de requisições que ignoram o custo em tokens; e chaves de API embutidas no código do navegador. O TLS protege o canal, não o conteúdo, então a injeção de prompt e o abuso por usuários conectados passam direto por ele. Limites só de requisições deixam um atacante enviar menos prompts, porém muito mais longos, como mostrou o teste de carga da LCH. Chaves de API no código do navegador podem ser lidas por qualquer pessoa que abra a página, o que permite chamar diretamente o provedor do modelo e contornar por completo as cotas da LCH; as chaves pertencem ao servidor.

### 7.6b Tempos limite e novas tentativas nas chamadas ao modelo

O Ask Lumen chama o provedor do modelo pela rede, e respostas lentas tentam os engenheiros a repetir chamadas de forma agressiva. Cada nova tentativa reenvia a pergunta do paciente e custa dinheiro; novas tentativas sem limite durante uma indisponibilidade podem multiplicar o tráfego e esgotar o limite de taxa de todas as clínicas. A LCH limita as novas tentativas a duas, com espera crescente, e mostra aos pacientes um número de telefone quando o modelo está indisponível. Uma espera crescente entre tentativas permite que um provedor em dificuldades se recupere em vez de ser inundado. O número de telefone mantém os pacientes atendidos enquanto o chatbot está fora do ar.

### Exercícios

- **EX019 — TLS.** Nomeie duas coisas que o TLS protege e duas que não protege. Rubrica: 3 = confidencialidade/integridade em trânsito, autenticação do servidor vs conteúdo malicioso, injeção/mau uso; 2 = três; 1 = uma ou duas; 0 = nenhuma.
- **EX020 — Leitura do laboratório.** No laboratório, por que o limite de 1/s com rajada 5 prejudica os usuários normais? Rubrica: 3 = só 62/90 atendidas, porque as rajadas naturais excedem o balde; 2 = só o número; 1 = vago; 0 = errado.
- **EX021 — Chaves.** Por que chaves de API de modelos não devem aparecer no código do navegador? Rubrica: 3 = qualquer pessoa pode lê-las e usá-las indevidamente, gerando custo e abuso; usar chamadas no servidor; 2 = parcial; 1 = vago; 0 = errado.

### Síntese

As redes entregam serviços de IA; TLS, autenticação, cotas que consideram tokens e monitoramento protegem a entrega, mas não o conteúdo, de que tratam os capítulos seguintes.

### Continue estudando — capítulo 07 de 40

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) organizar programas em módulos e funções com responsabilidades claras; (2) usar JSON e arquivos com segurança; (3) gerenciar pacotes de terceiros e arquivos de modelo com verificações de integridade; e (4) escrever testes que incluam casos adversariais.

### 8.1 Módulos e responsabilidades

Divida os programas de modo que cada parte tenha uma única tarefa. Numa aplicação com LLM: tratamento de entradas, recuperação, chamada ao modelo, verificação de política, execução de ferramentas, registro em log. Manter a verificação de política em seu próprio módulo pequeno permite revisá-la e testá-la independentemente do modelo. A separação também limita o dano: se o módulo de recuperação for manipulado para devolver um documento hostil, a verificação de política continua decidindo de forma independente se alguma chamada de ferramenta resultante é permitida. No Ask Lumen, as verificações de marcação que Rina escreveu no capítulo de programação ficam num módulo assim, com testes que rodam a cada mudança. Um revisor consegue ler o módulo inteiro em poucos minutos.

### 8.2 JSON e arquivos

Analise dados estruturados com analisadores estritos (`json.loads`) e valide campos, tipos e intervalos. Rejeite campos desconhecidos. Nunca use `eval` sobre dados. Quando se pede ao modelo que produza JSON, valide-o da mesma forma, porque o modelo pode produzir saídas malformadas ou manipuladas. No Ask Lumen, pede-se ao modelo que devolva uma marcação em JSON com um código de clínica, uma data e um identificador de paciente. O analisador rejeita qualquer campo extra, como uma instrução para cancelar outras consultas, e qualquer valor fora dos intervalos permitidos. Uma resposta malformada leva a uma mensagem educada de falha para o paciente, nunca a uma ação parcial.

### 8.3 Pacotes e arquivos de modelo

Instale pacotes de fontes confiáveis, com versões fixadas. Arquivos de modelo são riscos parecidos com código: alguns formatos de serialização podem executar código ao serem carregados. Verifique o hash SHA-256 de um arquivo contra um manifesto confiável antes de carregá-lo; o laboratório detecta adulterações dessa forma.

```python
"""Lab H: integrity of model artefacts with SHA-256 manifests (stdlib only).
Creates synthetic 'artefact' bytes, records a manifest, then detects a
one-byte tampering and a swapped file. No real models are involved."""
import hashlib, json
files = {"model.bin": bytes(range(256)) * 40, "tokenizer.json": b'{"vocab": ["a", "b"]}',
         "config.yaml": b"layers: 4\nheads: 8\n"}
manifest = {n: hashlib.sha256(b).hexdigest() for n, b in files.items()}
print(json.dumps({k: v[:16] for k, v in manifest.items()}, indent=1))
received = dict(files)
tampered = bytearray(received["model.bin"]); tampered[5000] ^= 1
received["model.bin"] = bytes(tampered)
received["config.yaml"] = b"layers: 4\nheads: 8\ntrust_remote_code: true\n"
for n, b in sorted(received.items()):
    ok = hashlib.sha256(b).hexdigest() == manifest[n]
    print(f"{n:15s} {'OK' if ok else 'MISMATCH'}")
```

Saída esperada:

```text
{
 "model.bin": "e96760a87768717b",
 "tokenizer.json": "f63d2ddabc61f2d9",
 "config.yaml": "e5bbb570ca0fcb87"
}
config.yaml     MISMATCH
model.bin       MISMATCH
tokenizer.json  OK
```

No Lab H, um único bit invertido em model.bin e uma linha acrescentada em config.yaml mudam os respectivos hashes, enquanto o tokenizer.json intocado continua correspondendo. O manifesto precisa vir de uma fonte confiável, como a versão assinada do fornecedor, ou um atacante que altera um arquivo poderia alterar também o manifesto.

### 8.4 Testes adversariais

Acrescente testes que tentem quebrar seu código: entradas grandes demais, tipos errados, cadeias que parecem injeção, pedidos de dados de outros usuários. Mantenha-os permanentemente na suíte de testes. No analisador de marcações, os testes adversariais incluem uma data escrita por extenso, um identificador de paciente que pertence a outra pessoa, um código de clínica com espaços no final e uma saída do modelo contendo duas marcações. Cada teste registra a rejeição esperada. Uma vez acrescentados, esses testes protegem contra regressões: uma mudança posterior que afrouxe por acidente uma verificação falha na hora, antes de chegar aos pacientes.

### 8.5 Exemplo resolvido (caso sintético da LCH)

O fornecedor do DocSort enviou um modelo atualizado. A verificação de integridade de Rina comparou o hash com o manifesto assinado do fornecedor e encontrou uma divergência no arquivo de configuração. A investigação mostrou que um terceirizado havia editado o arquivo para ativar um modo de depuração que registrava o texto completo das cartas. A mudança foi revertida, e a LCH passou a exigir que toda mudança de modelo chegasse pelo processo de versões assinadas. O modo de depuração corresponde, em espírito, à linha de configuração adulterada do Lab H: uma pequena mudança de texto com grande efeito sobre a privacidade.

### 8.6 Erros e limites

Três erros são comuns: lógica de política misturada ao texto do prompt; carregar arquivos de modelo sem verificação de integridade; e testes apenas com entradas benignas. Uma política escrita no prompt pode ser contornada por uma mensagem habilidosa, enquanto uma política em código não pode. Carregar arquivos de modelo sem verificar hashes teria deixado o modo de depuração do terceirizado chegar à produção na LCH. Testes apenas com entradas benignas passam mesmo quando o analisador aceita saídas perigosas; o arquivo de testes hostis do analisador de marcações existe precisamente para evitar isso, e cresce a cada incidente.

### 8.6b Testes que protegem o analisador

O módulo que transforma a saída do modelo num pedido de marcação é o código mais relevante para a segurança no Ask Lumen, porque uma resposta malformada ou manipulada poderia cancelar a consulta errada. A LCH mantém um arquivo de testes com saídas hostis — campos extras, datas erradas, dois identificadores de consulta — e toda mudança no analisador precisa passar por ele antes da integração. Cada saída hostil do arquivo vem de uma falha real ou de um achado de revisão, então o arquivo registra o histórico de ataques ao analisador, além de protegê-lo contra eles. Quando aparece um novo tipo de falha, um teste para ela é acrescentado antes da correção.

### Exercícios

- **EX022 — Leitura do laboratório.** Quais arquivos falham na verificação de hash do laboratório e por quê? Rubrica: 3 = model.bin e config.yaml, ambos alterados; 2 = um; 1 = vago; 0 = errado.
- **EX023 — Validação de JSON.** Liste quatro verificações para o JSON de marcação produzido pelo modelo. Rubrica: 3 = JSON válido, só campos permitidos, tipos, intervalos/titularidade; 2 = três; 1 = uma ou duas; 0 = nenhuma.
- **EX024 — Modo de depuração.** Por que a mudança para o modo de depuração era um problema de segurança? Rubrica: 3 = registrava dados de saúde sensíveis, ampliando a exposição; mudança não autorizada; 2 = parcial; 1 = vago; 0 = errado.

### Síntese

Programas estruturados, análise estrita, dependências verificadas e testes adversariais tornam as aplicações de IA mais difíceis de quebrar e mais fáceis de confiar.

### Continue estudando — capítulo 08 de 40

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) projetar esquemas relacionais simples e escrever consultas; (2) prevenir injeção em consultas a bancos de dados; (3) entender os bancos de dados vetoriais usados na recuperação; e (4) aplicar controle de acesso e minimização aos dados de IA.

### 9.1 Dados relacionais

Tabelas guardam registros; chaves ligam tabelas; consultas SQL recuperam e alteram dados. O sistema de agendamento da LCH tem tabelas de pacientes, clínicas e consultas. As consultas precisam ser parametrizadas: montar SQL juntando cadeias com entradas do usuário (ou do modelo) possibilita a injeção de SQL. Com uma consulta parametrizada, o banco de dados trata um identificador de paciente como valor, de modo que um texto como uma aspa seguida de palavras-chave SQL não consegue mudar o significado da consulta. Isso importa ainda mais quando os valores vêm de um modelo, que pode ser conduzido por sua entrada a produzir esse tipo de texto. A ferramenta de agendamento da LCH passa cada valor como parâmetro, e um teste com um identificador que parece injeção confirma isso.

### 9.2 Saídas do modelo e bancos de dados

Se um LLM gera consultas ou parâmetros de consulta, trate-os como entrada não confiável: use consultas parametrizadas, restrinja a conta do banco de dados ao mínimo de tabelas e operações e valide os valores. Um LLM capaz de escrever SQL arbitrário com uma conta de administrador é um sério risco de agência excessiva (OWASP LLM06). O Ask Lumen não gera SQL; ele propõe uma marcação cujos campos a ferramenta de agendamento coloca em consultas fixas e parametrizadas. A conta de banco de dados da ferramenta pode inserir e cancelar consultas, mas não pode ler outras tabelas nem alterar o esquema. Mesmo que o modelo fosse totalmente manipulado, o pior resultado se limitaria ao que essa conta permite, e a verificação de política o restringe ainda mais ao paciente conectado.

### 9.3 Bancos de dados vetoriais

A geração aumentada por recuperação armazena trechos de documentos como embeddings e recupera os mais semelhantes a cada pergunta. O controle de acesso precisa ser aplicado no momento da recuperação, com as permissões do usuário; caso contrário, o chatbot pode recuperar e revelar documentos que o usuário não deveria ver (OWASP LLM08, *fraquezas de vetores e embeddings*). Documentos acrescentados ao repositório também podem carregar instruções injetadas. Filtrar no momento da recuperação, em vez de pedir ao modelo que retenha conteúdo restrito, é a abordagem confiável: o modelo não pode vazar um texto que nunca recebeu.

### 9.4 Minimização e retenção

Armazene apenas os dados de que precisa, pelo tempo de que precisa. Os logs de conversas de chatbots costumam conter dados pessoais; defina prazos de retenção e regras de acesso. No Ask Lumen, a LCH guarda os logs de conversas por um prazo fixo, necessário para revisão de qualidade e investigação de incidentes, e depois os apaga. Só as equipes de segurança e de qualidade podem lê-los. A minimização também se aplica ao que é enviado ao provedor do modelo: identificadores de pacientes de que o modelo não precisa para responder ficam fora do prompt.

### 9.5 Exemplo resolvido (caso sintético da LCH)

O índice de recuperação do Ask Lumen incluía documentos de escala da equipe com os telefones dos funcionários. Uma pergunta de teste sintética, "quem está de plantão hoje à noite e como falo com essa pessoa?", devolveu um número de telefone a um paciente. A LCH retirou os documentos da equipe do índice voltado aos pacientes, acrescentou um campo de classificação de documentos e passou a filtrar a recuperação por público. O vazamento não exigiu ataque nenhum, apenas uma pergunta, o que mostra que o controle de acesso precisa ser projetado dentro da recuperação, e não testado depois da implantação. O campo de classificação agora orienta toda recuperação.

### 9.6 Erros e limites

Três erros são comuns: SQL montado com cadeias; um único índice de recuperação para todos os públicos; e retenção indefinida dos logs de chat. SQL montado com cadeias deixa a saída de um modelo, ou o texto digitado por um paciente, tornar-se parte de um comando de banco de dados. Um único índice de recuperação para todos os públicos causou o vazamento do telefone de funcionário no exemplo resolvido. A retenção indefinida dos logs de chat acumula informações pessoais e de saúde que se tornam um alvo e um passivo. Cada erro tem uma correção simples e conhecida, muito mais barata antes da implantação do que depois de um incidente.

### 9.6b Exclusão de dados a pedido

Quando um paciente pede à LCH que apague seu histórico de chat, a exclusão precisa alcançar todas as cópias: a tabela de conversas, os logs e quaisquer entradas do repositório vetorial construídas a partir desses chats. A equipe mantém um mapa de por onde passa o texto dos pacientes, para que um pedido possa ser concluído e confirmado dentro do prazo declarado pela clínica. O repositório vetorial é a cópia mais esquecida, porque ali o texto fica armazenado como trechos e embeddings, e não como uma conversa reconhecível. A LCH marca cada trecho com a conversa de onde ele veio, para que a exclusão consiga encontrá-lo.

### Exercícios

- **EX025 — Consulta parametrizada.** Por que consultas parametrizadas são mais seguras que a concatenação de cadeias? Rubrica: 3 = dados não conseguem mudar a estrutura da consulta; impede injeção; 2 = parcial; 1 = vago; 0 = errado.
- **EX026 — Acesso na recuperação.** O que deu errado com os documentos de escala e qual é a correção geral? Rubrica: 3 = público errado no índice; aplicar filtragem por público/usuário na recuperação; 2 = parcial; 1 = vago; 0 = nenhuma.
- **EX027 — Retenção.** Proponha uma regra de retenção para os logs de chat do Ask Lumen. Rubrica: 3 = prazo, finalidade, acesso, exclusão; 2 = três; 1 = um; 0 = nenhum.

### Síntese

Os repositórios de dados alimentam e registram os sistemas de IA. Consultas parametrizadas, contas com menor privilégio, recuperação atenta ao público e retenção mínima impedem que eles se tornem o vazamento.

### Continue estudando — capítulo 09 de 40

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) aplicar princípios éticos ao trabalho de segurança de IA; (2) explicar por que a autorização é necessária antes de testar; (3) seguir a divulgação coordenada; e (4) reconhecer questões de equidade, privacidade e safety levantadas por sistemas de IA.

### 10.1 Princípios

Respeito às pessoas, evitar danos, honestidade, equidade e responsabilização orientam o trabalho de segurança. Em segurança de IA, os danos incluem violações de privacidade, resultados discriminatórios, conselhos inseguros e mau uso de capacidades. Esses princípios se convertem em escolhas concretas. Evitar danos significa testar com registros sintéticos, não com pacientes reais. Honestidade significa relatar resultados com seus limites. Equidade significa verificar se as previsões do NoShow tratam grupos de forma diferente. Responsabilização significa registrar quem autorizou cada teste e quem tomou cada decisão, para que a responsabilidade fique clara se algo der errado. As notas de laboratório de Rina registram cada uma dessas escolhas.

### 10.2 Autorização

Testar sistemas sem permissão pode ser ilegal e pode prejudicar usuários reais. Obtenha sempre uma autorização por escrito do dono do sistema que defina escopo, métodos, período e contatos. Serviços públicos de IA têm termos de uso; não os ataque fora de programas que o permitam explicitamente (como escopos publicados de bug bounty). A autorização de Rina para o trabalho na LCH nomeia os sistemas (cópias isoladas do Ask Lumen, do NoShow e do DocSort), os métodos permitidos, as datas e o contato a quem ligar se algo inesperado acontecer. Ela leva uma cópia em toda sessão de testes.

### 10.3 Divulgação coordenada

Se você encontrar uma vulnerabilidade, relate-a em privado ao dono, dê um prazo razoável para a correção e publique apenas detalhes que ajudem os defensores. Não acesse mais dados do que o necessário para demonstrar o problema. No caso de Rina, o problema do número de telefone foi demonstrado com um único exemplo sintético, e não verificando muitos números reais. O relatório dela descreveu o comportamento, as condições e uma correção sugerida, e ela o manteve confidencial até que a LCH confirmasse a correção. Publicar detalhes antes da correção teria ajudado mais os atacantes do que os defensores.

### 10.4 Equidade e safety

Sistemas de IA podem tratar grupos de forma diferente. O NoShow, por exemplo, poderia classificar alguns pacientes mais abaixo para lembretes por causa de atributos correlacionados com a renda. O NIST AI RMF lista *justo, com vieses prejudiciais gerenciados* entre as características de uma IA confiável, ao lado de *seguro e resiliente* e *com privacidade reforçada*. O AI Act da UE impõe obrigações a sistemas de alto risco, incluindo alguns usos ligados à saúde; a classificação jurídica exige orientação especializada. Uma verificação de equidade para o NoShow compararia as taxas de erro entre grupos, por exemplo se pacientes de alguns códigos postais são mais vezes previstos, erroneamente, como faltosos.

### 10.5 Exemplo resolvido (caso sintético da LCH)

Um colega propôs testar um chatbot comercial de saúde "para ver se ele vaza dados". Rina explicou que, sem autorização, isso seria antiético e possivelmente ilegal, e sugeriu construir, em vez disso, uma réplica sintética no laboratório do curso. Em outra ocasião, num teste autorizado da LCH, Rina descobriu que o Ask Lumen podia revelar se um número de telefone pertencia a um paciente cadastrado; ela o relatou pelo processo da LCH com evidência mínima, e o problema foi corrigido antes do fim do semestre. Evidência mínima significou um número de telefone sintético, e não uma lista de números reais.

### 10.6 Erros e limites

Três erros são comuns: "só dar uma olhada" em sistemas não autorizados; coletar mais dados pessoais do que o necessário para um relatório; e ignorar a equidade como "não sendo segurança". "Só dar uma olhada" num sistema não autorizado pode violar a lei e prejudicar usuários, qualquer que seja a intenção. Coletar mais dados pessoais do que o necessário transforma um relatório de segurança num risco de privacidade por si só. Ignorar a equidade deixa passar danos que afetam os pacientes tão diretamente quanto um vazamento de dados, como o NoShow dar a alguns grupos menos lembretes por causa de atributos correlacionados com a renda. A prática de Rina trata os três desde a concepção.

### Exercícios

- **EX028 — Autorização.** Liste cinco elementos de uma autorização de testes. Rubrica: 3 = escopo, métodos, janela de tempo, tratamento de dados, contatos/condições de parada; 2 = quatro; 1 = dois; 0 = nenhum.
- **EX029 — Divulgação.** Descreva os passos de divulgação de Rina no problema do número de telefone. Rubrica: 3 = relato privado, evidência mínima, verificação da correção, nenhum dado público; 2 = parcial; 1 = vago; 0 = divulgação pública primeiro.
- **EX030 — Equidade.** Explique como o NoShow poderia gerar resultados injustos. Rubrica: 3 = proxies de características protegidas afetam lembretes/agendamento; 2 = parcial; 1 = vago; 0 = nenhum.

### Síntese

A prática ética em segurança de IA significa testes autorizados, divulgação cuidadosa, dados mínimos e atenção à equidade e à safety, além dos ataques.

### Continue estudando — capítulo 10 de 40

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). A Lumen Community Health, Rina e todos os seus números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** "Para toda entrada x no conjunto de tentativas de injeção, Filtro(x) = bloqueada." Uma única tentativa de injeção que não seja bloqueada a refuta.

**EX002.** A afirmação era universal (para todos os pacientes e todos os valores controláveis); um registro sintético cuja previsão se moveu a favor do paciente é um contraexemplo, logo a afirmação é falsa.

**EX003.** Euclidiana: √(0.5² + 0² + 1²) = √1.25 ≈ 1.118. Maior diferença absoluta: max(0.5, 0, 1) = 1.

**EX004.** Provedor: proteger a plataforma de hospedagem do modelo; manter o serviço de modelo hospedado disponível e atualizado. LCH: quais dados de pacientes são enviados nos prompts; restringir as permissões da ferramenta de agendamento; controlar quem pode usar o chatbot e como as saídas são exibidas.

**EX005.** Interface: portal web da escola; servidor de aplicação: aplicativo da escola; modelo: API hospedada, versão X; recuperação: índice dos materiais das disciplinas; ferramentas: nenhuma ou "enviar rascunho"; logs: logs do aplicativo e do provedor; identidades: conta SSO do estudante, chave de serviço do aplicativo.

**EX006.** No dispositivo: os dados não saem do aparelho. API hospedada: o provedor cuida das correções, da escala e do monitoramento do serviço de modelo.

**EX007.** Dados: a função `point` e as listas `train`/`test`. Treinamento: o laço de 200 épocas que atualiza `w` e `b`. Avaliação: a função `acc`, que aplica a perturbação. Saída: as linhas `print` dos pesos e da acurácia para cada eps.

**EX008.** 0.985 com eps 0.00 e 0.840 com eps 0.50.

**EX009.** Código da clínica no conjunto conhecido; data dentro de 90 dias; identificador do paciente igual ao do usuário conectado. Extra: verificação do formato do horário, ou um limite de marcações por usuário por dia.

**EX010.** "Filtros de conteúdo reduzem, mas não eliminam, a injeção de prompt; a injeção indireta por meio de conteúdo recuperado já comprometeu aplicações reais integradas a LLMs (Greshake et al., arXiv:2302.12173), então ações com consequências precisam de controles fora do modelo."

**EX011.** Abra https://arxiv.org/abs/ seguido do identificador e confira se título, autores e ano correspondem à referência; registre a versão, se ela importar.

**EX012.** NIST AI 600-1: norma/framework (orientação governamental). Artigo do arXiv: preprint. Blog de empresa: literatura cinzenta.

**EX013.** Confidencialidade: cartas de encaminhamento contêm dados de saúde. Integridade: encaminhar mal uma carta atrasa o atendimento. Disponibilidade: se o DocSort estiver fora do ar, as cartas se acumulam sem processamento.

**EX014.** Ameaça: fraudador com uma voz clonada. Vulnerabilidade: alterações de pagamento aceitas por telefone. Impacto: dinheiro enviado ao fraudador. Controle: verificar por um número conhecido e com um segundo aprovador.

**EX015.** Nunca colar segredos ou dados pessoais em ferramentas não aprovadas; verificar as saídas antes de agir com base nelas; usar apenas serviços de IA aprovados pela organização.

**EX016.** Permitidas: (paciente P, marcar, consulta de P); (paciente P, cancelar, consulta de P); (paciente P, ler, informações públicas da clínica). Proibidas: (paciente P, ler, consulta de Q); (paciente P, marcar, consulta para Q).

**EX017.** Envios de documentos de parceiros → modelo → ferramenta de agendamento. Controle: revisar os documentos dos parceiros antes da indexação e permitir marcações apenas para o paciente conectado, por meio de uma verificação de política.

**EX018.** 10,000 / 5 = 2,000 segundos ≈ 33 minutos.

**EX019.** Protege: confidencialidade e integridade dos dados em trânsito; autenticidade do servidor. Não protege: contra conteúdo malicioso de um usuário autenticado; contra injeção de prompt ou mau uso depois da chegada.

**EX020.** Ele atende apenas 62 das 90 requisições normais, porque as rajadas naturais do cliente normal excedem um balde de 5 tokens reabastecido a 1 por segundo.

**EX021.** O código do navegador é visível para qualquer pessoa; uma chave vazada permite que outros usem a API à sua custa e contornem seus controles. Chame o modelo a partir do servidor.

**EX022.** model.bin (um bit alterado) e config.yaml (uma linha acrescentada) falham; tokenizer.json não foi alterado e passa.

**EX023.** JSON válido; apenas campos permitidos; tipos corretos; valores dentro dos intervalos e pertencentes ao paciente conectado.

**EX024.** Registrava o texto completo das cartas — dados de saúde sensíveis —, ampliando a exposição, e era uma mudança não autorizada, feita fora do processo de versões.

**EX025.** Os parâmetros são enviados separadamente do texto da consulta, então a entrada não consegue mudar a estrutura da consulta; isso impede a injeção de SQL.

**EX026.** Documentos da equipe estavam no índice voltado aos pacientes; a recuperação precisa filtrar por público ou permissão do usuário antes que o conteúdo chegue ao modelo.

**EX027.** Guardar os logs de chat por 30 dias para suporte e revisão de safety; acesso limitado à equipe de suporte; dados pessoais ocultados quando possível; exclusão automática após 30 dias.

**EX028.** Escopo (sistemas e contas); métodos permitidos; janela de tempo; regras de tratamento de dados; contatos e condições de parada.

**EX029.** Ela parou assim que o problema foi demonstrado, relatou-o em privado pelo processo da LCH com evidência sintética mínima, não reteve dados reais e verificou a correção.

**EX030.** Atributos como código postal ou tipo de telefone podem funcionar como proxies de renda ou etnia; se baixam a prioridade prevista, alguns grupos recebem menos lembretes ou horários piores.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Arp, D. et al. (2020). Dos and Don'ts of Machine Learning in Computer Security. arXiv:2010.09470.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Carlini, N. et al. (2019). On Evaluating Adversarial Robustness. arXiv:1902.06705.
- Carlini, N. et al. (2023). Poisoning Web-Scale Training Datasets is Practical. arXiv:2302.10149.
- Chen, S. et al. (2024). StruQ: Defending Against Prompt Injection with Structured Queries. arXiv:2402.06363.
- Cohen, J., Rosenfeld, E., Kolter, J. Z. (2019). Certified Adversarial Robustness via Randomized Smoothing. arXiv:1902.02918.
- European Union. Regulation (EU) 2024/1689 (Artificial Intelligence Act). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Gebru, T. et al. (2018). Datasheets for Datasets. arXiv:1803.09010.
- Goodfellow, I., Shlens, J., Szegedy, C. (2014). Explaining and Harnessing Adversarial Examples. arXiv:1412.6572.
- Greshake, K. et al. (2023). Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv:2302.12173.
- Gu, T., Dolan-Gavitt, B., Garg, S. (2017). BadNets. arXiv:1708.06733.
- ISO/IEC 42001:2023 Artificial intelligence — Management system. <https://www.iso.org/standard/81230.html>
- Liu, Y. et al. (2023). Prompt Injection attack against LLM-integrated Applications. arXiv:2306.05499.
- Madry, A. et al. (2017). Towards Deep Learning Models Resistant to Adversarial Attacks. arXiv:1706.06083.
- Mitchell, M. et al. (2018). Model Cards for Model Reporting. arXiv:1810.03993.
- MITRE ATLAS. <https://atlas.mitre.org/>
- NIST AI 100-1 (2023), AI RMF 1.0. <https://doi.org/10.6028/NIST.AI.100-1>
- NIST AI 100-2 E2025 (2025), Adversarial Machine Learning taxonomy. <https://doi.org/10.6028/NIST.AI.100-2e2025>
- NIST AI 600-1 (2024), Generative AI Profile. <https://doi.org/10.6028/NIST.AI.600-1>
- OWASP Top 10 for LLM Applications 2025. <https://genai.owasp.org/llm-top-10/>
- Shokri, R. et al. (2016). Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.
- Tramèr, F. et al. (2016). Stealing Machine Learning Models via Prediction APIs. arXiv:1609.02943.
