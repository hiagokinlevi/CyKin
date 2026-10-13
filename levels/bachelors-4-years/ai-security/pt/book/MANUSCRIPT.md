# Segurança de IA e Aprendizado de Máquina: Livro do Curso de Bacharelado

- Idioma: português do Brasil (`pt`); bacharelado, quatro anos; aproximadamente 3.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–19 de 40 já estão escritos em português, com os exercícios EX001–EX057 e suas resoluções com rubricas de 0 a 3; os capítulos 20–40 (EX058–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) |

Capítulos 20–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-20), até a chegada dos próximos lotes.

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

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) explicar processos, usuários, permissões de arquivos e isolamento; (2) executar serviços de IA com menor privilégio; (3) isolar em sandbox o código produzido ou acionado por IA; e (4) usar logs do sistema em investigações.

### 11.1 Processos e permissões

Todo programa roda como um processo pertencente a uma conta de usuário. O sistema operacional verifica as permissões dessa conta antes de permitir acesso a arquivos, conexões de rede ou uso de dispositivos. Um servidor de modelo deve rodar sob sua própria conta sem privilégios, que pode ler os arquivos do modelo, mas não pode alterar código, ler dados não relacionados nem administrar a máquina. Se um atacante encontrasse uma falha no servidor de modelo, obteria apenas os direitos dessa conta. É por isso que o worker de OCR do DocSort rodando como administrador, no exemplo resolvido, era um achado grave antes mesmo de algo dar errado.

### 11.2 Isolamento

Contêineres e máquinas virtuais isolam cargas de trabalho. O isolamento é essencial quando um sistema de IA pode executar código (por exemplo, uma ferramenta de análise de dados num chatbot): o código pode ser influenciado por injeção de prompt, então precisa rodar sem acesso à rede, com CPU e memória limitadas, um tempo limite curto e um sistema de arquivos temporário. O Ask Lumen não executa código, mas o DocSort processa digitalizações enviadas, que são arquivos não confiáveis. Rodar seu worker de OCR num contêiner com acesso somente leitura à pasta de entrada significa que um arquivo malicioso só consegue afetar esse contêiner. Cada restrição responde a um risco específico: sem rede, os dados não saem; o tempo limite detém laços sem fim; e o sistema de arquivos temporário desaparece após cada tarefa.

### 11.3 Controle de recursos

Sem limites, uma requisição pesada pode deixar as outras sem recursos. Os control groups (no Linux) e os limites de contêineres restringem o uso de CPU, memória e GPU por carga de trabalho, favorecendo a disponibilidade. No DocSort, uma única digitalização malformada que consumisse toda a memória poderia bloquear todas as cartas de encaminhamento da fila. Um teto de memória no contêiner do worker faz esse arquivo falhar sozinho, enquanto a tarefa seguinte prossegue. Os limites são definidos a partir do uso normal medido mais uma margem, e uma tarefa que atinge um limite é registrada em log para que a causa possa ser investigada, em vez de ser repetida silenciosamente.

### 11.4 Logs

Logs de autenticação, de processos e de acesso a arquivos ajudam a reconstruir o que aconteceu. Correlacioná-los com os identificadores de requisição da aplicação liga uma conversa do chatbot aos seus efeitos no sistema. No Ask Lumen, cada conversa recebe um identificador de requisição que aparece no log da aplicação, no log das chamadas ao modelo e no log da ferramenta de agendamento. Com esse identificador, Rina consegue seguir uma mensagem de paciente desde o chat até qualquer consulta que ela tenha alterado. Sem ele, casar entradas apenas pelo horário é lento e propenso a erros quando muitas conversas acontecem ao mesmo tempo.

### 11.4b Correções e configuração

Sistemas operacionais e software de serviço de IA recebem atualizações de segurança; aplique-as segundo um calendário e acompanhe as versões. Configurações padrão muitas vezes ativam recursos de depuração, páginas de erro detalhadas e contas de exemplo que devem ser desativados em produção. Os despejos de memória do DocSort, no exemplo resolvido, são um caso desse tipo de padrão: úteis no desenvolvimento, nocivos em produção. A LCH agora mantém, para cada serviço de IA, uma lista de verificação de configuração revisada antes de cada versão, com as opções de depuração, páginas de erro e contas de exemplo que precisam estar desligadas. As correções seguem um calendário mensal, e as urgentes são aplicadas antes quando uma vulnerabilidade grave é anunciada.

### 11.5 Exemplo resolvido (caso sintético da LCH)

O worker de OCR do DocSort rodava com uma conta de administrador "por conveniência". Um arquivo digitalizado malformado o derrubou, e o despejo de memória foi gravado numa pasta compartilhada legível por todos os funcionários, expondo o texto das cartas. A correção de Rina: uma conta dedicada sem privilégios, despejos de memória desativados em produção, o worker num contêiner com acesso somente leitura à pasta de entrada e alertas para quedas. Cada correção responde a uma causa: a conta sem privilégios limita o que um worker comprometido pode fazer, os despejos desativados impedem que texto chegue a uma pasta compartilhada, a entrada somente leitura impede o worker de alterar cartas, e os alertas tornam as quedas visíveis.

### 11.6 Erros e limites

Três erros são comuns: serviços rodando como administrador; ferramentas de IA que executam código com acesso à rede; e logs que não podem ser ligados às requisições. Rodar como administrador transforma qualquer bug em controle total da máquina, como quase aconteceu no caso do DocSort. Ferramentas de IA que executam código com acesso à rede podem ser conduzidas por injeção de prompt a enviar dados para fora. Logs que não podem ser ligados às requisições tornam impossível dizer qual conversa causou qual efeito, e as investigações empacam. Cada um desses pontos é uma escolha de configuração, barata de acertar desde o início.

### Exercícios

- **EX031 — Menor privilégio.** Liste três permissões de que o worker do DocSort precisa e três que ele não deveria ter. Rubrica: 3 = os dois lados sensatos; 2 = um lado fraco; 1 = vago; 0 = nenhuma.
- **EX032 — Sandbox.** Especifique uma sandbox para a ferramenta "analisar planilha" de um chatbot. Rubrica: 3 = sem rede, limites de CPU/memória/tempo, sistema de arquivos temporário, usuário sem privilégios; 2 = três; 1 = um ou dois; 0 = nenhum.
- **EX033 — Despejo de memória.** Por que o despejo de memória era um problema de confidencialidade? Rubrica: 3 = continha texto sensível gravado num local amplamente legível; 2 = parcial; 1 = vago; 0 = errado.

### Síntese

O sistema operacional impõe quem pode fazer o quê. Menor privilégio, isolamento, limites de recursos e logs rastreáveis tornam os serviços de IA mais seguros quando algo dá errado.

### Continue estudando — capítulo 11 de 40

[← Capítulo 10 (rascunho)](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 (rascunho) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) usar probabilidade condicional e a regra de Bayes; (2) explicar taxas de base e a precisão de alertas; (3) calcular e interpretar intervalos de confiança para taxas; e (4) comparar dois sistemas de forma justa.

### 12.1 Probabilidade condicional

P(A | B) é a probabilidade de A dado B. A taxa de verdadeiros positivos de um detector é P(alerta | ataque); o que os operadores precisam é P(ataque | alerta), que a regra de Bayes fornece a partir das taxas de verdadeiros e falsos positivos e da taxa de base dos ataques. As duas são facilmente confundidas, e os fornecedores costumam citar a primeira. Um detector que pega 95% dos ataques ainda produz sobretudo alarmes falsos se os ataques forem raros, porque a maioria limpa gera muitos falsos positivos. A regra de Bayes torna o cálculo explícito, e o Lab B mostra quão fortemente a resposta depende da taxa de base.

### 12.2 Taxas de base

Quando os ataques são raros, mesmo bons detectores produzem sobretudo alarmes falsos. O laboratório mostra um detector com TPR de 95% e FPR de 5% que alcança precisão abaixo de 2% com uma taxa de base de 1 em 1.000.

```python
"""Lab B: base rates and alarm precision (Bayes' rule).
A detector for malicious prompts with given true- and false-positive rates
is applied to traffic with different shares of malicious prompts."""
for tpr, fpr in ((0.95, 0.05), (0.95, 0.01), (0.80, 0.001)):
    for prev in (0.10, 0.01, 0.001):
        tp = tpr * prev; fp = fpr * (1 - prev)
        prec = tp / (tp + fp)
        per_10k = round(10000 * (tp + fp))
        print(f"tpr={tpr:.2f} fpr={fpr:.3f} prevalence={prev:.3f} precision={prec:.3f} alerts_per_10k={per_10k}")
```

Saída esperada:

```text
tpr=0.95 fpr=0.050 prevalence=0.100 precision=0.679 alerts_per_10k=1400
tpr=0.95 fpr=0.050 prevalence=0.010 precision=0.161 alerts_per_10k=590
tpr=0.95 fpr=0.050 prevalence=0.001 precision=0.019 alerts_per_10k=509
tpr=0.95 fpr=0.010 prevalence=0.100 precision=0.913 alerts_per_10k=1040
tpr=0.95 fpr=0.010 prevalence=0.010 precision=0.490 alerts_per_10k=194
tpr=0.95 fpr=0.010 prevalence=0.001 precision=0.087 alerts_per_10k=109
tpr=0.80 fpr=0.001 prevalence=0.100 precision=0.989 alerts_per_10k=809
tpr=0.80 fpr=0.001 prevalence=0.010 precision=0.890 alerts_per_10k=90
tpr=0.80 fpr=0.001 prevalence=0.001 precision=0.445 alerts_per_10k=18
```

Lendo o Lab B ao longo das linhas: com uma taxa de base de um em mil, baixar a taxa de falsos positivos de 5% para 1% eleva a precisão de 0.019 para 0.087, e o detector de 0.001 chega a 0.445. Os alertas por 10.000 conversas mostram a carga de trabalho: 509 para o primeiro detector contra 18 para o último. Revisores conseguem lidar com dezoito alertas; quinhentos seriam ignorados.

### 12.3 Intervalos de confiança

Uma taxa observada numa amostra é incerta. O intervalo de Wilson funciona bem com amostras pequenas e taxas extremas. Três sucessos em vinte são compatíveis com taxas reais de cerca de 5% a 36%.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Saída esperada:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

O laboratório mostra como o intervalo se estreita com o tamanho da amostra: a mesma taxa de 15% dá um intervalo de cerca de 11% a 21% com 200 tentativas e de 0.135 a 0.166 com 2.000. Uma demonstração com 20 prompts não consegue distinguir uma defesa fraca de uma forte. A linha por semente acrescenta outra fonte de dispersão: cinco execuções da mesma avaliação variam de 0.105 a 0.145.

### 12.4 Comparação de sistemas

Para comparar duas defesas, teste ambas nos mesmos itens e examine a diferença pareada com um intervalo bootstrap. Se o intervalo incluir zero, você não pode afirmar que uma é melhor. Testar nos mesmos itens remove a variação causada por alguns prompts serem mais difíceis que outros. No Lab S, a defesa reduz o sucesso dos ataques de 0.350 para 0.190, e o intervalo bootstrap da redução vai de 0.120 a 0.203. Como ele exclui o zero, a melhora é real para este conjunto de teste; se ela se mantém em outros prompts é outra questão.

### 12.4b Variação e tamanho da amostra

Os resultados também variam com as sementes aleatórias, as divisões dos dados e a redação dos prompts. Execute várias sementes e relate sua dispersão, como mostra a linha por semente do laboratório. Para planejar quantos casos de teste são necessários para uma taxa perto de p com semiamplitude h do intervalo a 95% de confiança, use n ≈ 1.96² × p(1 − p) / h². Para p = 0.1 e h = 0.02, isso dá cerca de 864 casos — muito mais do que a maioria das demonstrações rápidas usa, e é por isso que muitas "taxas de sucesso" publicadas são menos certas do que parecem. A fórmula também mostra o custo da precisão: reduzir h à metade, para 0.01, exige quatro vezes mais casos, cerca de 3.457.

### 12.5 Exemplo resolvido (caso sintético da LCH)

Um fornecedor ofereceu um "detector de ataques por prompt" com 98% de acurácia. Rina pediu a TPR e a FPR: 90% e 2%. Com uma estimativa de 1 conversa maliciosa a cada 2.000, a precisão seria de cerca de 2% — a maioria dos alertas, falsos. A LCH usou o detector apenas para sinalizar conversas para revisão semanal, e não para bloquear pacientes. O número de 98% de acurácia quase não significava nada aqui, já que um detector que nunca disparasse marcaria cerca de 99.95% no mesmo tráfego. Usá-lo para revisão semanal, em vez de bloqueio, significa que os alertas falsos custam tempo de revisores, e não o acesso dos pacientes.

### 12.6 Erros e limites

Três erros são comuns: acurácia sem taxas de base; números isolados sem intervalos; e comparar sistemas em conjuntos de teste diferentes. A acurácia esconde o compromisso entre ataques perdidos e alarmes falsos e pode parecer alta para um detector inútil quando os ataques são raros. Um número isolado sem intervalo convida ao excesso de confiança, sobretudo em testes pequenos, como três sucessos em vinte. Comparar sistemas em conjuntos de teste diferentes confunde diferenças entre os sistemas com diferenças entre os prompts. O Lab S mostra a correção de cada um, usando os mesmos prompts sintéticos.

### Exercícios

- **EX034 — Precisão.** Calcule a precisão para TPR 0.90, FPR 0.02 e taxa de base 0.0005. Rubrica: 3 = 0.00045/(0.00045 + 0.01999) ≈ 0.022; 2 = deslize; 1 = método; 0 = nenhum.
- **EX035 — Leitura do laboratório.** Qual é o intervalo de Wilson para 300/2000 no Lab S? Rubrica: 3 = [0.135, 0.166]; 2 = aproximado; 1 = só o ponto; 0 = errado.
- **EX036 — Comparação pareada.** Por que testar duas defesas nos mesmos itens? Rubrica: 3 = remove a variação de dificuldade dos itens; inferência pareada válida; 2 = parcial; 1 = vago; 0 = errado.

### Síntese

A probabilidade diz o que um alerta significa e quão seguro você pode estar. Taxas de base, intervalos e comparações pareadas são o mínimo para afirmações honestas em segurança de IA.

### Continue estudando — capítulo 12 de 40

[← Capítulo 11 (rascunho)](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 (rascunho) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) explicar autenticação, autorização e registro de responsabilidade (accounting); (2) projetar acesso baseado em papéis e em atributos para aplicações de IA; (3) aplicar a delegação para que agentes de IA ajam com os direitos limitados do usuário; e (4) evitar problemas de confused deputy.

### 13.1 Autenticação, autorização, accounting

A autenticação prova quem alguém é; a autorização decide o que a pessoa pode fazer; o accounting registra o que ela fez. Uma autenticação forte (multifator) protege as contas; uma autorização precisa limita o dano; o accounting possibilita a investigação. No Ask Lumen, a autenticação é o login do paciente no portal da clínica; a autorização é a regra de que uma marcação só pode ser para esse paciente ou para alguém de quem ele é cuidador cadastrado; o accounting é o log que liga cada marcação à conversa e à sessão que a produziram. Uma fraqueza em qualquer um deles enfraquece os outros: logs perfeitos não ajudam se a ferramenta de agendamento nunca verificou quem estava pedindo.

### 13.2 Acesso baseado em papéis e em atributos

Papéis (paciente, recepcionista, clínico) agrupam permissões. Atributos (clínica, relação com o paciente, horário) as refinam. A ferramenta de agendamento do Ask Lumen deve verificar "quem pede é o paciente ou seu cuidador cadastrado, para esta clínica?", e não "o serviço do chatbot tem permissão para marcar?". A segunda pergunta é a errada porque o serviço do chatbot sempre tem permissão; fazê-la transforma os direitos amplos do serviço em direitos de todo mundo. Atributos como a clínica e a relação de cuidador permitem que a regra acompanhe situações reais sem criar um papel novo para cada uma.

### 13.3 Delegação para agentes de IA

Quando um agente de IA age, ele deve usar um token delegado pelo usuário, com escopo e validade limitados, para que nunca possa fazer mais do que esse usuário. Uma conta de serviço poderosa transforma qualquer manipulação do modelo numa escalada de privilégios — o problema do *confused deputy*, em que um componente confiável é enganado e usa mal sua autoridade. Um token delegado carrega a identidade do paciente, então o sistema de agendamento pode aplicar diretamente os direitos do paciente. Sua validade curta limita o dano se ele vazar por um log ou por uma chamada de ferramenta manipulada.

### 13.4 Accounting das ações de IA

Registre qual usuário, qual conversa, qual proposta do modelo e qual aprovação levaram a cada ação. Sem essa cadeia, os incidentes não podem ser explicados. A cadeia de uma marcação poderia ser: sessão do paciente 7f2, conversa c-118, proposta do modelo às 10:14:03 para marcar na clínica C3 numa certa data, verificação de política aprovada, paciente confirmou às 10:14:20, identificador da marcação gravado. Se um paciente contestar uma marcação mais tarde, cada passo pode ser mostrado. Se o modelo propôs algo que a política bloqueou, isso também fica registrado, o que ajuda a detectar tentativas de manipulação.

### 13.5 Exemplo resolvido (caso sintético da LCH)

O Ask Lumen marcava consultas por meio de uma conta de serviço autorizada a marcar para qualquer paciente. Rina mostrou, no ambiente de teste, que uma mensagem elaborada com o identificador de outro paciente sintético levava o modelo a propor uma marcação para esse paciente, que a conta de serviço executava. A correção usou um token delegado por sessão, vinculado ao paciente conectado (e aos cuidadores cadastrados), e uma verificação de política que compara o paciente da marcação com o titular do token. O teste mostra o confused deputy diretamente: o modelo não fez nada de errado segundo sua própria lógica, e a conta de serviço fez o que tinha permissão para fazer.

### 13.6 Erros e limites

Três erros são comuns: ferramentas de IA rodando sob contas de serviço amplas; autorização decidida pelo modelo; e falta, nos logs, de ligação entre conversas e ações. Contas de serviço amplas fazem de toda injeção de prompt uma possível escalada de privilégios, como mostrou o exemplo resolvido. Deixar o modelo decidir a autorização coloca a regra onde um texto pode discutir com ela. A falta de ligação entre conversas e ações deixa os investigadores sem conseguir dizer qual mensagem causou qual marcação. Tokens delegados, uma verificação de política externa e identificadores de requisição tratam os três, um a um.

### 13.6b Revisão das permissões de agentes

A cada trimestre, a LCH lista o que a ferramenta de agendamento do Ask Lumen realmente pode fazer e compara com aquilo de que o chatbot precisa. Uma revisão descobriu que a conta da ferramenta também podia editar as agendas dos clínicos; esse direito foi removido, e o registro da revisão anota quem aprovou as permissões restantes. As permissões tendem a crescer à medida que funcionalidades são acrescentadas, e ninguém as remove a menos que uma revisão o peça. O direito de editar agendas havia sido acrescentado para um piloto já encerrado, e ninguém tinha notado que continuava concedido.

### Exercícios

- **EX037 — AAA.** Defina autenticação, autorização e accounting com um exemplo do Ask Lumen para cada. Rubrica: 3 = três corretas com exemplos; 2 = duas; 1 = uma; 0 = nenhuma.
- **EX038 — Confused deputy.** Explique o problema do confused deputy usando o achado de Rina. Rubrica: 3 = conta de serviço confiável usada indevidamente por meio de um modelo manipulado; 2 = parcial; 1 = vago; 0 = errado.
- **EX039 — Política.** Escreva a verificação de política para marcações. Rubrica: 3 = booking.patient ∈ {token.subject} ∪ carers(token.subject) e clínica permitida; 2 = parcial; 1 = vago; 0 = nenhuma.

### Síntese

Os controles de identidade decidem o que um agente de IA pode fazer e em nome de quem. Tokens delegados com escopo e verificações de política externas impedem que o modelo se torne um confused deputy.

### Continue estudando — capítulo 13 de 40

[← Capítulo 12 (rascunho)](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 (rascunho) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem

Você vai (1) explicar os princípios de proteção de dados e o conceito de dado pessoal; (2) descrever ataques de privacidade contra o aprendizado de máquina (inferência de pertencimento, extração de dados, inferência de atributos); (3) aplicar técnicas de reforço da privacidade; e (4) avaliar os riscos de privacidade de um sistema de IA.

### 14.1 Princípios

Leis de proteção de dados como o RGPD da UE (no Brasil, a LGPD, Lei nº 13.709/2018) exigem base legal, limitação da finalidade, minimização dos dados, exatidão, limitação da conservação, segurança e responsabilização. Dados de saúde são uma categoria especial, com regras mais rígidas. No Ask Lumen, limitação da finalidade significa que os logs de conversas guardados para revisão de qualidade não são reaproveitados para treinar modelos de marketing; minimização significa que o prompt inclui apenas o necessário para responder; limitação da conservação significa que os logs são apagados ao fim do prazo de retenção. Como dados de saúde são uma categoria especial, a base legal e as salvaguardas da LCH ficam documentadas em sua avaliação de impacto antes de qualquer novo uso.

### 14.2 Ataques de privacidade contra o aprendizado de máquina

A *inferência de pertencimento* decide se um registro estava nos dados de treinamento (Shokri et al., arXiv:1610.05820). A *extração de dados de treinamento* recupera texto memorizado por modelos generativos (Carlini et al., arXiv:2012.07805). A *inferência de atributos* adivinha atributos sensíveis a partir das saídas do modelo. O sobreajuste aumenta esses riscos; o laboratório mostra o pertencimento vazando de um modelo que memoriza e diminuindo à medida que ele generaliza.

```python
"""Lab M: membership inference against an overfit 1-nearest-neighbour 'model'
that returns a confidence score. Synthetic records only; teaching model."""
import random, math
rng = random.Random(5)
def rec(): 
    y = rng.random() < 0.5
    return [rng.gauss(0.6 if y else -0.6, 1.0) for _ in range(4)], int(y)
members = [rec() for _ in range(150)]; nonmembers = [rec() for _ in range(150)]
def confidence(x, y, k):
    # k-NN vote share for the true label, computed over the training set
    d = sorted((sum((a-b)**2 for a, b in zip(x, m)), my) for m, my in members)
    return sum(1 for _, my in d[:k] if my == y)/k
def auc(pos, neg):
    s = sum((p > n) + 0.5*(p == n) for p in pos for n in neg)
    return s/(len(pos)*len(neg))
for k in (1, 5, 25):
    pos = [confidence(x, y, k) for x, y in members]
    neg = [confidence(x, y, k) for x, y in nonmembers]
    best = max(sum(p >= t for p in pos)/len(pos) - sum(n >= t for n in neg)/len(neg)
               for t in sorted(set(pos + neg)))
    print(f"k={k:2d} attack_auc={auc(pos, neg):.3f} best_advantage={best:.3f}")
```

Saída esperada:

```text
k= 1 attack_auc=0.600 best_advantage=0.200
k= 5 attack_auc=0.521 best_advantage=0.073
k=25 attack_auc=0.520 best_advantage=0.060
```

O Lab M torna o efeito mensurável: com k igual a 1, o ataque atinge uma AUC de 0.600, enquanto com k igual a 25 ela cai para 0.520, perto do acaso. Calcular a média sobre mais vizinhos, como faz um modelo que generaliza, reduz o que a saída revela sobre pacientes individuais.

### 14.3 Técnicas de reforço da privacidade

Minimize e pseudonimize os dados; elimine registros de treinamento duplicados; limite o detalhe das saídas (rótulos em vez de confianças); aplique privacidade diferencial durante o treinamento (Abadi et al., arXiv:1607.00133); controle quem pode consultar os modelos; e nunca coloque dados pessoais em prompts sem necessidade. Cada técnica ataca uma parte do risco. A eliminação de duplicatas remove registros repetidos, que os modelos tendem a memorizar. Devolver rótulos em vez de confianças remove o sinal que o ataque do Lab M usa. A privacidade diferencial limita quanto um único registro pode afetar o modelo treinado, com algum custo em acurácia. Os controles de consulta limitam quem pode sondar o modelo. A mudança da LCH no NoShow usou quatro dessas técnicas juntas.

### 14.4 Avaliação de riscos de privacidade

Pergunte: quais dados pessoais entram no treinamento, na recuperação, nos prompts e nos logs? Quem pode consultar o modelo, e o que as saídas revelam? O que acontece se os logs vazarem? Uma avaliação de impacto sobre a proteção de dados documenta as respostas e os controles. No NoShow, as respostas mostraram que dados pessoais entravam no treinamento, que qualquer funcionário podia consultar qualquer identificador de paciente e que as saídas davam probabilidades precisas. Cada achado levou a um controle: consultas restritas, saídas por categoria e atributos minimizados. A avaliação é atualizada quando o sistema muda, e não arquivada uma vez e esquecida.

### 14.4b Prompts e logs

Dados pessoais também passam por prompts e logs. Se funcionários colam dados de pacientes num assistente de IA, esses dados podem ser armazenados pelo provedor ou aparecer em logs. Configure a retenção e a recusa ao uso para treinamento quando o provedor oferecer essas opções, oculte identificadores antes do envio sempre que possível e treine os funcionários sobre o que pode ser compartilhado. A ocultação pode ser automatizada para identificadores estruturados, como números de pacientes, mas o texto livre exige cuidado: um paciente pode digitar um diagnóstico ou o nome de um parente em qualquer ponto de uma mensagem.

### 14.5 Exemplo resolvido (caso sintético da LCH)

A API do NoShow devolvia uma probabilidade precisa para qualquer identificador de paciente. Rina mostrou, com dados sintéticos, que a confiança diferia entre pacientes do conjunto de treinamento e pacientes novos, o que permitia a inferência de pertencimento ("esta pessoa foi atendida na LCH no ano passado?"). A LCH mudou a API para devolver apenas uma categoria de lembrete a funcionários autorizados e retreinou o modelo com atributos minimizados e sem duplicatas. Devolver uma categoria em vez de uma probabilidade removeu a maior parte do sinal, e limitar o acesso a funcionários autorizados reduziu quem podia sequer fazer a pergunta.

### 14.6 Erros e limites

Três erros são comuns: tratar modelos como se não contivessem dados pessoais; saídas de confiança detalhadas para públicos amplos; e logs cheios de dados pessoais sem limite de retenção. Modelos treinados com registros de pacientes carregam informações sobre esses registros, como mostra a inferência de pertencimento. Escores de confiança detalhados para públicos amplos dão aos atacantes o sinal de que precisam. Logs cheios de dados pessoais sem limite de retenção tornam-se um depósito de informações sensíveis que cresce a cada dia. As mudanças da LCH no NoShow e suas regras de retenção de logs tratam os três, e a avaliação de impacto registra por quê.

### Exercícios

- **EX040 — Leitura do laboratório.** Que AUC e que vantagem o laboratório informa com k = 1, e o que isso significa? Rubrica: 3 = 0.600 e 0.200; a memorização vaza o pertencimento; 2 = os números; 1 = vago; 0 = errado.
- **EX041 — Pertencimento sensível.** Por que o pertencimento aos dados de treinamento do NoShow é sensível? Rubrica: 3 = revela que a pessoa foi paciente (informação de saúde); 2 = parcial; 1 = vago; 0 = errado.
- **EX042 — Técnicas.** Liste quatro técnicas de reforço da privacidade para o NoShow. Rubrica: 3 = quatro pertinentes; 2 = três; 1 = uma ou duas; 0 = nenhuma.

### Síntese

Modelos podem revelar seus dados de treinamento. Princípios de proteção de dados, saídas atentas à privacidade e técnicas como a minimização e a privacidade diferencial reduzem o risco.

### Continue estudando — capítulo 14 de 40

[← Capítulo 13 (rascunho)](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 (rascunho) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher métricas que correspondam às perguntas de segurança; (2) projetar conjuntos de teste que evitem vazamento; (3) coletar e preservar evidências corretamente; e (4) redigir resultados de medição com condições e incerteza.

### 15.1 Métricas que correspondem às perguntas

"O chatbot vaza dados de outros pacientes?" exige uma taxa de vazamento numa suíte de testes de tentativas. "O filtro pega injeções?" exige a TPR com uma FPR fixa. "A defesa prejudica a utilidade?" exige o sucesso das tarefas em pedidos normais. Use várias métricas; um único número raramente responde a uma pergunta de segurança. Fixar a taxa de falsos positivos antes de comparar filtros garante que um filtro não pareça melhor simplesmente por sinalizar mais conversas. O tempo dos funcionários gasto revisando alarmes falsos é um custo real para as clínicas.

### 15.2 Conjuntos de teste e vazamento

Mantenha os dados de teste separados de tudo o que foi usado para construir ou ajustar o sistema. Quase-duplicatas entre conjuntos inflam os resultados (Kapoor e Narayanan, arXiv:2207.07048). Para ataques por prompt, construa os casos de teste a partir de modelos que você não usou ao desenvolver as defesas. Se Rina ajustasse uma defesa com os mesmos modelos de injeção com que depois a testasse, sua taxa de sucesso mediria a memorização desses modelos, e não a força geral da defesa. Ela mantém um conjunto separado de modelos de ataque escritos por um colega e só o abre na avaliação final. Procurar quase-duplicatas entre os conjuntos, como o mesmo ataque com um nome trocado, faz parte de construí-los.

### 15.3 Tratamento de evidências

Registre entradas, saídas, versões (modelo, prompt, código) e carimbos de tempo. Armazene as evidências com hashes de integridade e controle de acesso. No trabalho com incidentes, preserve os logs originais antes da análise. As versões importam porque o mesmo prompt pode dar resultados diferentes depois de uma atualização do modelo pelo provedor. Rina registra o identificador de modelo devolvido pela API, o hash do prompt de sistema e o commit do código de cada execução de teste. Calcular o hash das transcrições permite que ela mostre depois que elas não foram editadas. Os logs originais são copiados e têm seu hash calculado antes de qualquer análise, e a análise é feita na cópia.

### 15.4 Relato

Declare a pergunta, o método, a amostra, os resultados com intervalos, as condições e as limitações. Arp et al. (arXiv:2010.09470) listam armadilhas como viés de amostragem e linhas de base inadequadas; confira as suas contra essa lista. O relatório de vazamento de Rina segue esta ordem: pergunta, 400 tentativas sintéticas, resultados de duas versões com intervalos de Wilson, condições como prompts apenas em inglês, e limitações. Ao conferir com a lista de Arp et al., ela encontrou uma armadilha no rascunho: havia comparado a versão 2 com a versão 1 testada meses antes, com outra versão do modelo, e por isso repetiu o teste na mesma versão.

### 15.4b Linhas de base e comparações

Um número significa pouco sem uma linha de base. Relate o resultado do sistema sem defesa ao lado do sistema defendido, e uma alternativa simples e forte (por exemplo, uma lista de ferramentas permitidas) ao lado da sua defesa elaborada. Se a alternativa simples obtiver a maior parte do benefício, diga isso: é um conhecimento útil para os profissionais e protege você contra afirmar demais. No Ask Lumen, uma linha de base simples e forte é remover por completo a ferramenta de cancelamento, que então nenhuma injeção consegue usar indevidamente. Qualquer defesa proposta deve ser comparada com essa opção.

### 15.5 Exemplo resolvido (caso sintético da LCH)

Rina mediu o vazamento do Ask Lumen com 400 tentativas sintéticas de obter a consulta de outro paciente. A versão 1 vazou em 14 casos (3.5%, intervalo de Wilson de 95% de 2.1–5.8%). Depois da correção com token delegado, a versão 2 vazou em 0 de 400 (limite superior de cerca de 0.95%). Ela armazenou as transcrições com hashes e anotou que as tentativas foram apenas em inglês. O intervalo importa: 14 de 400 é compatível com uma taxa real entre cerca de 2.1% e 5.8%, então o efeito da correção é claro mesmo levando o acaso em conta. Zero vazamentos em 400 não significa risco zero; o limite superior de cerca de 0.95% é o que o teste consegue sustentar. Anotar a limitação ao inglês diz aos leitores que outros idiomas continuam sem teste.

### 15.6 Erros e limites

Três erros são comuns: ajustar no conjunto de teste; relatar sem versões; e ignorar os limites de idioma ou formato de uma suíte de testes. Ajustar no conjunto de teste infla os resultados sem melhorar o sistema. Relatar sem versões torna os resultados impossíveis de reproduzir depois que o modelo ou o prompt mudam. Ignorar limites de idioma ou de formato leva os leitores a supor uma cobertura que nunca foi testada, por exemplo ataques escritos em outro idioma ou escondidos num formato de documento que a suíte de testes não incluía, como um PDF digitalizado.

### Exercícios

- **EX043 — Escolha de métricas.** Escolha métricas para avaliar o DocSort contra ataques de encaminhamento errado. Rubrica: 3 = taxa de sucesso de ataques com cartas elaboradas, acurácia do encaminhamento normal, intervalos; 2 = duas; 1 = uma; 0 = nenhuma.
- **EX044 — Zero falhas.** Que limite superior se aplica a 0/400, e por que não afirmar 0%? Rubrica: 3 = ≈ 3/400 ≈ 0.75% (regra de três; Wilson ≈ 0.95%); amostra finita; 2 = parcial; 1 = afirma 0%; 0 = nenhum.
- **EX045 — Registro de evidências.** Liste cinco itens a registrar por caso de teste. Rubrica: 3 = entrada, saída, versões de modelo/prompt/código, carimbo de tempo, hash; 2 = quatro; 1 = dois; 0 = nenhum.

### Síntese

Uma boa medição faz a pergunta certa, usa dados de teste limpos, preserva as evidências e relata os resultados com condições e incerteza.

### Continue estudando — capítulo 15 de 40

[← Capítulo 14 (rascunho)](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 (rascunho) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) aplicar menor privilégio, defesa em profundidade, mediação completa e padrões à prova de falhas a sistemas de IA; (2) traçar fronteiras de confiança em aplicações com LLM; (3) posicionar um ponto de aplicação de políticas fora do modelo; e (4) comparar opções de arquitetura pelo risco residual.

### 16.1 Princípios aplicados à IA

*Menor privilégio*: dê ao modelo e às suas ferramentas apenas as permissões necessárias. *Defesa em profundidade*: combine rotulagem das entradas, validação das saídas, verificações de política, monitoramento e revisão humana. *Mediação completa*: verifique toda ação, todas as vezes. *Padrões à prova de falhas*: negue na dúvida. No Ask Lumen, menor privilégio é o token delegado; defesa em profundidade combina a rotulagem do texto recuperado, a análise das saídas, a verificação de política e o registro em log; mediação completa significa que toda marcação passa pela verificação de política, inclusive as propostas no fim de uma conversa longa; padrões à prova de falhas significam que uma proposta impossível de analisar ou duvidosa é recusada, e o paciente é informado de como marcar por telefone.

### 16.2 Fronteiras de confiança em aplicações com LLM

Um modelo de linguagem recebe instruções confiáveis (dos desenvolvedores), entradas parcialmente confiáveis (dos usuários) e conteúdo não confiável (documentos recuperados, páginas web, resultados de ferramentas) numa única sequência de tokens. Ele não consegue distingui-los de forma confiável, e é por isso que a injeção indireta de prompt funciona (Greshake et al., arXiv:2302.12173). A arquitetura precisa, portanto, impor as consequências fora do modelo. No Ask Lumen, o prompt de sistema é confiável, a mensagem do paciente é parcialmente confiável, e os documentos recuperados das clínicas, especialmente os enviados por parceiros, não são confiáveis. Rotulá-los ajuda o modelo, mas não garante que ele ignore instruções dentro de um documento, então são as próprias verificações da ferramenta de agendamento que limitam o resultado.

### 16.3 O ponto de aplicação de políticas

O modelo *propõe* ações; um componente separado, pequeno e testado *decide* se elas serão executadas, com base na identidade do usuário, na ação, em seus parâmetros e em se conteúdo não confiável a influenciou. Ações de alto impacto exigem confirmação humana. É aqui que se trata o OWASP LLM06 (*agência excessiva*). Manter esse componente pequeno é deliberado: algumas centenas de linhas de código podem ser revisadas e testadas a fundo, ao contrário do modelo. No Ask Lumen, o ponto de política compara o paciente da marcação com o titular do token, verifica as regras de clínica e data e exige confirmação para cancelamentos. Toda decisão, permitida ou recusada, é registrada com o identificador da requisição.

### 16.4 Comparação de opções

As opções para um chatbot de agendamento vão de nenhuma ferramenta (apenas respostas) até o uso livre de ferramentas. Entre elas: ferramentas com verificações de política e confirmações. Compare por risco residual, utilidade e custo, e registre a decisão com seu raciocínio. Risco residual é o que resta depois dos controles; utilidade é quantos pacientes conseguem concluir sua tarefa; custo inclui construir e operar cada opção. Uma tabela com essas três colunas torna o compromisso visível. Registrar o raciocínio permite que uma equipe posterior entenda por que a escolha foi feita e a reveja se as condições mudarem, como no acréscimo de uma nova ferramenta.

### 16.5 Exemplo resolvido (caso sintético da LCH)

A nota de arquitetura de Rina para o Ask Lumen v2 listou três opções: (a) o modelo marca diretamente; (b) o modelo propõe, a política verifica a identidade do paciente e a clínica, e o paciente confirma na interface; (c) o chatbot dá instruções e os pacientes marcam sozinhos. A LCH escolheu (b): a confirmação acrescenta um clique, mas um texto injetado já não consegue marcar nem cancelar sem uma ação do paciente. A opção (a) foi rejeitada porque um único documento injetado poderia agir; a opção (c), porque eliminava a maior parte do valor do chatbot. O estudo do capítulo de métodos de pesquisa mediu depois o custo do clique extra de (b).

### 16.6 Erros e limites

Três erros são comuns: regras de segurança escritas apenas no prompt de sistema; ferramentas com permissões mais amplas que as dos usuários; e nenhum registro de por que uma arquitetura foi escolhida. Regras escritas apenas no prompt de sistema podem ser anuladas por um texto persuasivo, já que o modelo trata ambos como linguagem. Ferramentas com permissões mais amplas que as dos usuários deixam um modelo manipulado ir além do que qualquer usuário poderia fazer. Sem um registro de por que uma arquitetura foi escolhida, mudanças posteriores podem remover um controle sem perceber contra o que ele protegia, como a etapa de confirmação que impede marcações injetadas.

### Exercícios

- **EX046 — Princípios.** Aplique três princípios ao DocSort. Rubrica: 3 = três aplicações concretas; 2 = duas; 1 = só os nomes; 0 = nenhuma.
- **EX047 — Fronteira.** Por que o modelo não consegue impor sozinho a fronteira de confiança? Rubrica: 3 = fluxo único de tokens, seguimento estatístico de instruções; 2 = parcial; 1 = vago; 0 = errado.
- **EX048 — Escolha de opção.** Defenda a opção (b) em vez da (a) em duas frases. Rubrica: 3 = impacto limitado da injeção com atrito modesto; 2 = parcial; 1 = vago; 0 = nenhuma.

### Síntese

A arquitetura de segurança tira a imposição de regras de dentro do modelo: fronteiras de confiança, um ponto de política externo e a confirmação humana limitam o que um modelo manipulado consegue fazer.

### Continue estudando — capítulo 16 de 40

[← Capítulo 15 (rascunho)](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 (rascunho) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) explicar hashing, criptografia simétrica e de chave pública e assinaturas digitais; (2) aplicá-los para proteger artefatos e dados de IA; (3) explicar o que a criptografia não pode fazer pela segurança de IA; e (4) verificar a integridade de modelos com manifestos assinados.

### 17.1 Primitivas básicas

*Funções de hash* (como a SHA-256) mapeiam dados para um resumo curto; mudar um bit muda o resumo. A *criptografia simétrica* (como o AES) protege dados com uma chave compartilhada. A *criptografia de chave pública* permite que qualquer pessoa cifre para o detentor de uma chave, ou verifique assinaturas dele. *Assinaturas digitais* provam quem criou os dados e que eles não foram alterados. Nos sistemas da LCH, hashes verificam os arquivos de modelo, a criptografia simétrica protege os logs de conversas armazenados, a criptografia de chave pública protege o TLS até o provedor do modelo, e assinaturas provam que as versões do DocSort vêm do fornecedor. Cada primitiva responde a uma pergunta diferente, e usar a errada deixa uma lacuna: um hash sozinho mostra que um arquivo não mudou, mas não quem o produziu.

### 17.2 Proteção de artefatos de IA

Cifre dados de treinamento e pesos de modelos em repouso; use TLS em trânsito. Publique os resumos SHA-256 dos arquivos de modelo num manifesto e assine o manifesto, para que os destinatários possam verificar a integridade e a origem antes de carregar. Isso trata riscos da cadeia de suprimentos (OWASP LLM03), como modelos adulterados ou com backdoor (Gu et al., arXiv:1708.06733).

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

O Lab H verifica a integridade, mas não a origem, porque um atacante capaz de alterar os arquivos também poderia alterar um manifesto não assinado. A assinatura fecha essa lacuna, já que a chave não está no servidor.

### 17.3 O que a criptografia não pode fazer

A cifragem não impede que uma consulta autorizada extraia informação de um modelo, não previne a injeção de prompt e não torna limpo um conjunto de dados envenenado — apenas prova que os dados envenenados são os dados que você assinou. A criptografia protege dados e artefatos; o comportamento precisa de outros controles. No Ask Lumen, toda mensagem trafega cifrada e todo arquivo de modelo é verificado, e ainda assim um paciente pode digitar uma injeção e um documento de parceiro pode carregar texto hostil. Esses riscos exigem o ponto de política, a rotulagem e o monitoramento. A nota de arquitetura de Rina lista quais ameaças cada camada trata, para que ninguém suponha que a cifragem cobre mais do que cobre.

### 17.4 Chaves

A segurança depende das chaves: guarde-as em serviços de gerenciamento de chaves, restrinja o acesso, faça sua rotação e nunca as coloque em prompts ou em repositórios de código. A chave de API do provedor de modelo da LCH é um exemplo claro: quem a possui pode executar consultas cobradas da LCH e possivelmente ler logs. A LCH a guarda no serviço de gerenciamento de chaves da nuvem, dá acesso apenas ao servidor de aplicação, faz sua rotação a cada trimestre e varre os repositórios em busca de commits acidentais. Uma chave vazada é primeiro revogada, depois investigada, e os logs são revisados.

### 17.5 Exemplo resolvido (caso sintético da LCH)

O fornecedor do DocSort passou a assinar suas versões. Rina configurou o script de implantação para buscar a chave pública do fornecedor no repositório confiável da própria LCH (e não no servidor de versões), verificar a assinatura do manifesto e depois verificar o resumo de cada arquivo. Uma versão de teste com um arquivo modificado foi rejeitada. Buscar a chave no repositório da própria LCH importa porque, do contrário, um atacante que controlasse o servidor de versões poderia fornecer tanto um arquivo malicioso quanto uma chave correspondente. A versão de teste rejeitada confirma que a verificação funciona de ponta a ponta.

### 17.6 Erros e limites

Três erros são comuns: buscar resumos e chaves no mesmo lugar que os arquivos; supor que a cifragem impede o vazamento pelo modelo; e chaves no código-fonte. Buscar resumos e chaves no mesmo lugar que os arquivos significa que um único comprometimento derrota a verificação, e é por isso que a LCH guarda a chave do DocSort em seu próprio repositório. A cifragem não impede que um modelo revele dados de treinamento por meio de suas respostas. Chaves no código-fonte acabam em repositórios e backups que muitas pessoas podem ler, por isso são procuradas e trocadas quando encontradas.

### 17.6b Verificação de assinaturas na prática

Assinar o arquivo de modelo do DocSort só ajuda se o carregador verificar a assinatura toda vez e se recusar a iniciar em caso de falha. A LCH testou isso carregando uma cópia com um byte alterado: o serviço recusou, registrou o evento e continuou executando a versão verificada anterior. Manter a versão verificada anterior em execução evitou uma indisponibilidade enquanto o problema era investigado, o que tornou a recusa segura. O fornecedor então reemitiu uma versão corretamente assinada. Os funcionários não notaram nenhuma mudança no DocSort enquanto a versão antiga continuava classificando os documentos.

### Exercícios

- **EX049 — Primitivas.** Associe: integridade de um arquivo; origem de um manifesto; confidencialidade de dados armazenados. Rubrica: 3 = hash, assinatura, cifragem; 2 = duas; 1 = uma; 0 = nenhuma.
- **EX050 — Origem da chave.** Por que buscar a chave pública do fornecedor no repositório da própria LCH? Rubrica: 3 = um atacante que controlasse o servidor de versões poderia substituir arquivos e chave; 2 = parcial; 1 = vago; 0 = errado.
- **EX051 — Limites.** Nomeie dois riscos de IA que a criptografia não trata. Rubrica: 3 = injeção de prompt, extração por consultas, envenenamento de dados assinados, evasão; 2 = um; 1 = vago; 0 = errado.

### Síntese

A criptografia torna os artefatos e dados de IA verificáveis e confidenciais, mas não consegue fazer um modelo se comportar; é uma camada entre muitas.

### Continue estudando — capítulo 17 de 40

[← Capítulo 16 (rascunho)](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 (rascunho) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) formular perguntas de pesquisa em segurança de IA; (2) encontrar e avaliar literatura; (3) projetar experimentos simples com controles; e (4) relatar resultados com honestidade e com suas limitações.

### 18.1 Perguntas

Uma boa pergunta é específica, respondível e útil: "Exigir a confirmação do paciente reduz as marcações não autorizadas pelo Ask Lumen sob documentos injetados, e quanto isso custa em marcações concluídas?" Ela nomeia o sistema, a intervenção, o resultado e a comparação. A comparação é a parte que mais costuma faltar: sem ela, um resultado como "nenhuma marcação não autorizada" não pode ser atribuído à confirmação, e não ao fato de os casos de teste serem fáceis. Nomear o custo, as marcações concluídas, torna o estudo útil para a LCH, que precisa pesar segurança contra atendimento.

### 18.2 Literatura

Comece por visões gerais — NIST AI 100-2 E2025 para a terminologia de ML adversarial, OWASP LLM 2025 para riscos de aplicações com LLM, MITRE ATLAS para técnicas do mundo real — e depois leia artigos-chave anotando modelo de ameaça, método, métricas e limitações. Verifique cada referência. Para seu estudo sobre confirmação, Rina lê trabalhos sobre injeção indireta de prompt e sobre confirmação humana em sistemas automatizados, anotando para cada artigo qual ataque ele supõe e como o sucesso foi medido. Ela registra onde os artigos discordam e por quê, muitas vezes por causa de modelos de ameaça diferentes. Verificar referências é o hábito do capítulo de escrita, agora aplicado a uma revisão de literatura completa.

### 18.3 Experimentos

Mude uma coisa de cada vez; mantenha uma condição de controle; use dados de teste reservados; repita com várias sementes; registre as versões. Decida métricas e limiares antes de executar, para que os resultados não conduzam a análise. No estudo de Rina, a única mudança é a confirmação ligada ou desligada; o controle é o mesmo chatbot sem ela; os documentos de teste são escritos separadamente do desenvolvimento; e as métricas, marcações causadas por documentos injetados e marcações normais concluídas, são fixadas de antemão, com um plano de intervalos escrito antes de qualquer execução.

### 18.4 Relato honesto

Relate todas as condições, não só a melhor; dê intervalos; descreva o que não foi testado. Lipton e Steinhardt (arXiv:1807.03341) descrevem "tendências preocupantes", como fontes de ganho pouco claras; evite-as explicando qual mudança causou qual efeito. O relatório de Rina inclui a queda nas marcações concluídas, que alguns leitores poderiam ver como enfraquecendo a defesa da confirmação. Omiti-la enganaria a LCH quanto ao custo. Ela também explica que foi a confirmação, e não outra mudança, que causou o efeito, porque só essa configuração diferia entre as condições. O que ela não testou, como outros idiomas, fica listado.

### 18.4b Ética no desenho da pesquisa

Experimentos de segurança de IA podem causar danos: payloads que funcionam em produtos reais, conjuntos de dados com dados pessoais ou testes em sistemas que não são seus. Use dados sintéticos e sistemas isolados, mantenha os payloads inofensivos (por exemplo, apontados para domínios reservados `.invalid`), obtenha aprovação ética quando houver participação de pessoas e planeje a divulgação caso descubra uma vulnerabilidade real. Os documentos injetados de Rina tentam marcar consultas para um identificador de paciente sintético na cópia isolada, de modo que nada afeta pacientes reais ou sistemas reais. Nenhum funcionário das clínicas é enganado.

### 18.5 Exemplo resolvido (caso sintético da LCH)

O primeiro estudo de Rina comparou o Ask Lumen com e sem confirmação em 300 documentos injetados sintéticos e 300 conversas normais de marcação. Sem confirmação, 21 documentos injetados causaram marcações (7.0%); com confirmação, 0 (limite superior ≈ 1%). As marcações normais concluídas caíram de 97% para 94%, porque alguns usuários de teste desistiram na etapa de confirmação. Ela relatou os dois efeitos e anotou que os usuários de teste eram colegas, não pacientes. A taxa de 7.0% tem um intervalo de Wilson de cerca de 4.6% a 10.5%, claramente acima da condição com confirmação, então a diferença não é resultado do acaso. A queda de três pontos nas marcações normais é o custo.

### 18.6 Erros e limites

Três erros são comuns: perguntas amplas demais; nenhuma condição de controle; e relatar apenas resultados favoráveis. Uma pergunta ampla demais, como "o Ask Lumen é seguro?", não pode ser respondida por nenhum estudo isolado. Sem uma condição de controle, um resultado observado não pode ser atribuído à intervenção. Relatar apenas resultados favoráveis, por exemplo o ganho de segurança sem a queda de 97% para 94% nas marcações concluídas, engana quem decide sobre os compromissos. O desenho do estudo de Rina evita cada um deles ao nomear de antemão a comparação, o custo e os limites.

### Exercícios

- **EX052 — Pergunta.** Escreva uma pergunta de pesquisa sobre o DocSort usando os quatro elementos. Rubrica: 3 = sistema, intervenção, resultado, comparação; 2 = três; 1 = vaga; 0 = nenhuma.
- **EX053 — Controles.** Por que uma condição de controle é necessária no estudo de Rina? Rubrica: 3 = mostra o efeito da confirmação em relação à linha de base; 2 = parcial; 1 = vago; 0 = errado.
- **EX054 — Limitação.** Indique uma limitação do estudo de Rina e seu efeito sobre as conclusões. Rubrica: 3 = colegas, não pacientes → o custo na conclusão pode ser diferente; ou documentos sintéticos; 2 = só a limitação; 1 = genérica; 0 = nenhuma.

### Síntese

Os métodos de pesquisa transformam perguntas em respostas confiáveis: perguntas claras, literatura sólida, experimentos controlados e relatos honestos, com limitações.

### Continue estudando — capítulo 18 de 40

[← Capítulo 17 (rascunho)](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 (rascunho) →](#ch-19)

<a id="ch-19"></a>

## Capítulo 19 — Segurança de IA e aprendizado de máquina: escopo e teoria

### Objetivos de aprendizagem

Você vai (1) definir segurança de IA e distingui-la de safety de IA e de IA responsável; (2) descrever as classes de ataque da taxonomia NIST AI 100-2 E2025; (3) explicar por que o aprendizado de máquina é vulnerável em princípio; e (4) situar os principais frameworks.

### 19.1 Definições

A *segurança de IA* protege os sistemas de IA e os processos ao seu redor contra ataques deliberados e mau uso, e protege terceiros de ataques viabilizados por IA. A *safety de IA* trata de comportamentos nocivos mesmo sem atacante. A *IA responsável* abrange equidade, transparência e responsabilização. As áreas se sobrepõem: uma injeção de prompt é um ataque de segurança que pode causar resultados inseguros ou injustos. Na LCH, as três se encontram num único sistema. Um documento de parceiro que faz o Ask Lumen anunciar o falso fechamento de uma clínica é um ataque, então pertence à segurança; os pacientes que em seguida deixam de ser atendidos são um resultado de safety. Rina mantém os termos separados em seus relatórios para que cada equipe saiba quais problemas são seus.

### 19.2 A taxonomia

O NIST AI 100-2 E2025 classifica os ataques a IA preditiva pelo objetivo — quebra de disponibilidade, violação de integridade, comprometimento da privacidade — e acrescenta o mau uso para a IA generativa. As classes de ataque incluem evasão (entradas em tempo de teste), envenenamento (dados de treinamento ou modelo), ataques de privacidade (inferência de pertencimento, reconstrução de dados, extração de modelo) e, para sistemas generativos, injeção de prompt direta e indireta. Os atacantes são caracterizados pelo conhecimento (caixa-branca, caixa-cinza, caixa-preta) e pelas capacidades (controle dos dados de treinamento, controle do modelo, acesso por consulta). Rina situa cada sistema da LCH nela. O Ask Lumen é generativo, então se aplicam injeção de prompt e mau uso; o NoShow e o DocSort são preditivos. Um atacante externo costuma ter apenas acesso por consulta em caixa-preta, enquanto um terceirizado que rotula as cartas do DocSort tem controle dos dados de treinamento, uma capacidade mais forte.

### 19.3 Por que o aprendizado de máquina é vulnerável

Os modelos aprendem padrões estatísticos a partir de dados, não regras; generalizam de forma imperfeita e são sensíveis a mudanças pequenas e cuidadosamente escolhidas na entrada (Szegedy et al., arXiv:1312.6199; Goodfellow et al., arXiv:1412.6572). Herdam tudo o que seus dados contêm, inclusive veneno. Grandes modelos de linguagem seguem instruções encontradas em qualquer parte de sua entrada. Essas propriedades são inerentes, então a segurança se apoia em controles em camadas, e não numa correção única. O laboratório de evasão mostra isso concretamente: o mesmo classificador de brinquedo que marca 0.985 com entradas limpas cai para cerca do acaso quando o orçamento de perturbação chega a um, sem nenhuma mudança no modelo em si.

### 19.4 Frameworks

O NIST AI RMF (AI 100-1) e seu Generative AI Profile (AI 600-1) organizam a gestão de riscos; o OWASP LLM 2025 lista riscos de aplicações; o MITRE ATLAS cataloga técnicas de adversários com estudos de caso; a ISO/IEC 42001 especifica um sistema de gestão de IA; o AI Act da UE estabelece deveres legais para alguns sistemas. Eles respondem a perguntas diferentes. Rina usa o OWASP para verificar os riscos de aplicação do Ask Lumen, o ATLAS para encontrar exemplos reais de ataques para sua apresentação aos funcionários e o AI RMF para estruturar o processo geral de riscos da LCH. Se o AI Act da UE se aplica depende do uso de cada sistema, então ela registra essa avaliação separadamente, em vez de supor que uma resposta cobre os três sistemas.

### 19.5 Exemplo resolvido (caso sintético da LCH)

Rina classificou os riscos da LCH: Ask Lumen — injeção indireta de prompt por documentos (integridade), divulgação de informações sensíveis (privacidade); NoShow — inferência de pertencimento (privacidade), manipulação de campos controlados pelo paciente (integridade, evasão); DocSort — cartas elaboradas para encaminhar errado (evasão), envenenamento por cartas de treinamento rerrotuladas (integridade). A classificação mostrou que cada sistema tinha riscos de privacidade e de integridade, mas por caminhos diferentes. A principal exposição do Ask Lumen era o que ele lê; a do NoShow, o que ele revela; a do DocSort, quem moldou seus dados de treinamento. Essa diferença levou Rina a designar responsáveis diferentes: a equipe do chatbot, o encarregado de proteção de dados e a equipe de prontuários.

### 19.6 Erros e limites

Três erros são comuns: tratar a segurança de IA apenas como jailbreaks de chatbots; esperar que um único controle corrija vulnerabilidades inerentes; e misturar os termos safety e segurança. Concentrar-se em jailbreaks teria deixado de lado por completo o risco de envenenamento do DocSort, já que ninguém conversa com o DocSort. Nenhum controle isolado cobre evasão, envenenamento e injeção, então a LCH precisa de várias camadas. Usar "safety" quando se quer dizer "segurança" deixa incerto se um atacante é suposto, o que muda os testes que devem ser feitos e quem é responsável por corrigir o problema.

### Exercícios

- **EX055 — Definições.** Classifique: um chatbot dá um conselho errado sobre medicação sem nenhum atacante; um atacante o faz revelar dados de outro paciente. Rubrica: 3 = safety vs segurança, com razões; 2 = só os rótulos; 1 = um; 0 = errado.
- **EX056 — Taxonomia.** Classifique a elaboração de cartas contra o DocSort por objetivo, etapa e conhecimento. Rubrica: 3 = integridade, implantação/evasão, caixa-preta ou caixa-cinza; 2 = dois; 1 = um; 0 = nenhum.
- **EX057 — Inerente.** Dê duas razões pelas quais o aprendizado de máquina é vulnerável em princípio. Rubrica: 3 = generalização estatística/sensibilidade, dependência dos dados, seguimento de instruções na entrada; 2 = uma; 1 = vago; 0 = errado.

### Síntese

A segurança de IA tem um escopo preciso e um vocabulário compartilhado. Suas vulnerabilidades são estruturais, e é por isso que o resto do livro constrói defesas em camadas e medidas.

### Continue estudando — capítulo 19 de 40

[← Capítulo 18 (rascunho)](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 (rascunho) →](#ch-20)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX057 (as de EX058–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). A Lumen Community Health, Rina e todos os seus números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** Precisa: ler sua pasta de entrada; gravar os resultados de encaminhamento na fila; ler seus arquivos de modelo. Não deveria ter: direitos de administrador; acesso de escrita ao código ou aos arquivos de modelo; acesso de leitura a compartilhamentos não relacionados ou acesso a toda a rede.

**EX032.** Executar o código da ferramenta num contêiner sem rede, com limites de CPU, memória e tempo, um sistema de arquivos temporário contendo apenas o arquivo enviado e um usuário sem privilégios.

**EX033.** O despejo continha o texto das cartas (dados de saúde) e foi gravado numa pasta que todos os funcionários podiam ler, expondo-o além das pessoas autorizadas.

**EX034.** TP = 0.90 × 0.0005 = 0.00045; FP = 0.02 × 0.9995 ≈ 0.01999; precisão ≈ 0.00045 / 0.02044 ≈ 0.022.

**EX035.** [0.135, 0.166].

**EX036.** Os itens diferem em dificuldade; usar os mesmos itens faz essa variação se cancelar na diferença pareada, o que dá uma comparação justa e mais precisa.

**EX037.** Autenticação: o paciente entra com senha e código de uso único. Autorização: a ferramenta de agendamento só permite marcar para esse paciente. Accounting: os logs registram quem marcou o quê, por qual conversa.

**EX038.** A conta de serviço de agendamento era confiável para marcar para qualquer pessoa; o modelo, manipulado por uma mensagem, pediu-lhe que marcasse para outro paciente, e ela obedeceu — um intermediário confiável enganado e levado a usar mal sua autoridade.

**EX039.** Permitir somente se booking.patient_id ∈ {token.subject} ∪ registered_carers_of(token.subject) e booking.clinic for uma clínica em que esse paciente esteja cadastrado; caso contrário, negar.

**EX040.** AUC 0.600 e vantagem 0.200: o modelo que memoriza dá maior confiança aos membros, então o pertencimento vaza.

**EX041.** Estar nos dados de treinamento do NoShow revela que a pessoa foi paciente da LCH — uma informação relacionada à saúde.

**EX042.** Minimizar e pseudonimizar os atributos; eliminar registros duplicados; devolver categorias em vez de probabilidades a um grupo limitado de funcionários; treinar com privacidade diferencial (também: restringir consultas, limitar a retenção).

**EX043.** Taxa de sucesso de ataques com cartas elaboradas para encaminhar errado e acurácia do encaminhamento normal com cartas genuínas, ambas com intervalos de confiança.

**EX044.** Com zero falhas em 400 tentativas, o limite superior de 95% é de cerca de 3/400 ≈ 0.75% (Wilson ≈ 0.95%); a taxa real pode ser maior que zero, e outros tipos de ataque não foram testados.

**EX045.** Entrada; saída; versões de modelo, prompt e código; carimbo de tempo; hash de integridade.

**EX046.** Menor privilégio: o DocSort pode encaminhar cartas, mas não ler prontuários de pacientes. Defesa em profundidade: saída do OCR validada, encaminhamentos de baixa confiança enviados aos funcionários, monitoramento das taxas de encaminhamento. Padrão à prova de falhas: cartas ilegíveis ou ambíguas vão para revisão manual.

**EX047.** As instruções e o conteúdo não confiável chegam num único fluxo de tokens, e o seguimento de instruções pelo modelo é estatístico, então ele pode seguir um texto injetado apesar das instruções em contrário.

**EX048.** Em (a), qualquer texto injetado que convença o modelo pode marcar ou cancelar consultas; em (b), são exigidas uma verificação de política e a confirmação do paciente, o que limita o impacto ao custo de um clique.

**EX049.** Integridade de um arquivo: hash. Origem de um manifesto: assinatura digital. Confidencialidade de dados armazenados: cifragem.

**EX050.** Se a chave viesse do servidor de versões, um atacante que controlasse esse servidor poderia substituir juntos arquivos, manifesto e chave; uma chave vinda do repositório confiável da própria LCH não pode ser trocada dessa forma.

**EX051.** Injeção de prompt; extração de modelo ou inferência de pertencimento por meio de consultas legítimas (também: envenenamento de dados que depois foram assinados; evasão).

**EX052.** "No DocSort (sistema), acrescentar uma etapa de revisão humana para encaminhamentos de baixa confiança (intervenção), em comparação com o encaminhamento totalmente automático (comparação), reduz as cartas encaminhadas errado em 500 encaminhamentos sintéticos, incluindo 100 elaborados (resultado)?"

**EX053.** Sem a condição sem confirmação, não há linha de base, então as 0 marcações poderiam se dever ao conjunto de teste, e não à etapa de confirmação.

**EX054.** Os usuários de teste eram colegas; pacientes reais podem desistir mais ou menos vezes na confirmação, então o custo de 3 pontos na conclusão pode não se transferir.

**EX055.** Um conselho errado sem atacante é uma falha de safety (ou de confiabilidade); revelar a um atacante dados de outro paciente é uma falha de segurança (confidencialidade).

**EX056.** Objetivo: violação de integridade; etapa: implantação (evasão no momento da inferência); conhecimento: caixa-preta (ou caixa-cinza, se o atacante conhece o tipo de modelo).

**EX057.** Os modelos aprendem padrões estatísticos sensíveis a pequenas mudanças elaboradas na entrada; dependem inteiramente de seus dados (então o veneno se propaga); LLMs seguem instruções em qualquer parte de sua entrada.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Arp, D. et al. (2020). Dos and Don'ts of Machine Learning in Computer Security. arXiv:2010.09470.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
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
