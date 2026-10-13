# Privacidade e Proteção de Dados: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 119, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–50 (EX031–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de engenharia que projetam, verificam e operam a privacidade e a proteção de dados como propriedades de um sistema real.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios executam resposta aleatorizada, consultas de retenção, verificações de fluxos de dados, pontuação de DPIA, contagens de minimização, confiabilidade da eliminação, orçamentos de privacidade, um relógio de incidente e resumos criptográficos de evidências, sempre sobre dados sintéticos. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de engenharia ao longo de um curso de cinco anos centrado em uma prestadora de telemedicina: fundamentos lidos pela ótica da privacidade, sistemas e segurança, requisitos e modelos, ameaças e DPIA, controles e implementação, medição e verificação, confiabilidade, resiliência e escala, operação e validação, o serviço de dados de pesquisa do projeto final, o ensaio de incidente, o dossiê de evidências, o trabalho de conclusão e a defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Zara Mbeki** | Estudante de engenharia | Inventada |
| **Prof. Anders Holm** | Orientador | Inventado |
| **Corwen Polytechnic** | Universidade fictícia | Inventada |
| **Pellmore Telehealth** | Prestadora fictícia de telemedicina, com 300 funcionários e pacientes na União Europeia e no Brasil | Inventada |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR); Lei nº 13.709/2018 (LGPD); Diretrizes 4/2019, 05/2020, 07/2020, 01/2022 e 9/2022 do EDPB; WP248 rev.01 sobre DPIA; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10), NISTIR 8053 e SP 800-188; ISO/IEC 29100:2011 e ISO/IEC 27701:2025; Sweeney (2002); Dwork et al. (2006) e Dwork e Roth (2014); Solove (2006); Nissenbaum (2004); Acquisti et al. (2015). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) interpretar taxas de variação no crescimento dos dados; (2) usar limites para raciocinar sobre o anonimato quando os grupos encolhem; (3) ligar o cálculo à engenharia de privacidade.

### 1.1 Por que uma engenheira encontra a privacidade cedo

Zara Mbeki começa um curso de engenharia de cinco anos na fictícia Corwen Polytechnic, sob orientação do Prof. Anders Holm. A parceira de seu estágio é a fictícia Pellmore Telehealth, uma prestadora de telemedicina com 300 funcionários e pacientes na União Europeia e no Brasil. O aplicativo da Pellmore agenda consultas, conduz teleconsultas por vídeo e guarda prontuários. O Prof. Holm explica que a privacidade e a proteção de dados serão o principal domínio de engenharia de Zara, e que cada disciplina de fundamentos será lida por essa ótica, a começar pelo cálculo, porque os problemas de privacidade costumam envolver quantidades que crescem ou diminuem com o tempo.

### 1.2 Taxas de variação

O volume de vídeo armazenado pela Pellmore cresce cerca de quarenta gigabytes por dia. A derivada do armazenamento em relação ao tempo é essa taxa diária, e integrá-la ao longo de um ano dá o total. Zara vê de imediato uma consequência para a privacidade: se as gravações nunca forem apagadas, a quantidade de dados de saúde sensíveis em risco cresce linearmente para sempre. Uma regra de retenção transforma a curva de crescimento em um patamar, porque os dados entram e saem na mesma taxa. Ela esboça as duas curvas e rotula a diferença entre elas como exposição evitável, que um vazamento poderia revelar.

### 1.3 Limites e grupos pequenos

Um limite descreve o que acontece quando uma quantidade se aproxima de um valor. Zara aplica a ideia às estatísticas publicadas. Se a Pellmore divulga o tempo médio de espera de uma clínica, a média descreve muitos pacientes; quando o tamanho do grupo se aproxima de um, a média passa a ser o tempo exato de espera de uma única pessoa. A proteção de privacidade que funciona para grupos grandes falha, portanto, no limite dos grupos muito pequenos. Essa intuição, ela aprende, está por trás das regras que suprimem células pequenas em tabelas publicadas e das garantias formais que ela encontrará mais tarde na privacidade diferencial.

### 1.4 Otimização como compromisso

O cálculo também encontra máximos e mínimos. O Prof. Holm propõe um exercício: a utilidade de um conjunto de dados cresce com o detalhe, mas o risco à privacidade também cresce. Se os dois forem modelados como curvas suaves, o melhor nível de detalhe é aquele em que o ganho marginal de utilidade iguala o aumento marginal de risco. Zara percebe que o modelo é simplista, porque o risco para as pessoas não se troca livremente por utilidade e a lei fixa limites rígidos, mas o hábito de perguntar pelos efeitos marginais vai ajudá-la a defender projetos proporcionais ao longo de todo o curso.

### Exemplo resolvido

Zara modela o crescimento do armazenamento com e sem retenção, raciocina sobre médias quando o tamanho do grupo diminui e enquadra o detalhe contra o risco como um compromisso marginal limitado pela lei.

> **Caso sintético.** A Corwen, a Pellmore e os números são sintéticos.

### Erros e limites

Curvas suaves simplificam riscos discretos; os limites legais são restrições, não termos de um compromisso.

### Exercícios

- **EX001 — Patamar de retenção.** Por que uma regra de retenção transforma o crescimento do armazenamento em um patamar? *Rubrica:* 3 = os dados entram e saem em taxas iguais, então o total para de subir;; 2 = menciona a eliminação;; 1 = diz que o armazenamento para;; 0 = nenhuma.
- **EX002 — Limite do grupo pequeno.** O que acontece com uma média quando o tamanho do grupo se aproxima de um? *Rubrica:* 3 = ela vira o valor exato de uma pessoa, revelando-o;; 2 = diz que fica menos precisa;; 1 = errado;; 0 = nenhuma.
- **EX003 — Limites do compromisso marginal.** Por que o modelo de compromisso marginal é simplista para a privacidade? *Rubrica:* 3 = o dano às pessoas não é livremente trocável e a lei fixa limites rígidos;; 2 = menciona a lei;; 1 = aceita o modelo;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) contar combinações de atributos; (2) usar conjuntos para descrever categorias de dados; (3) raciocinar sobre a unicidade com o princípio da casa dos pombos.

### 2.1 Contando combinações

Zara conta quantos perfis distintos o formulário de agendamento da Pellmore pode produzir. A data de nascimento tem cerca de 36.500 valores ao longo de um século, o sexo tem dois valores comuns e a Pellmore atende cerca de 3.000 áreas postais. O produto passa de duzentos milhões de combinações possíveis, muito mais do que os 150.000 pacientes da Pellmore. A maioria das combinações fica vazia, e muitos pacientes ficam sozinhos em sua combinação. Esse argumento simples de contagem explica a constatação de Sweeney (2002) de que poucos atributos comuns bastam para singularizar a maioria das pessoas, que Zara estudará em detalhe mais adiante no curso.

### 2.2 Conjuntos e categorias

A legislação de proteção de dados usa categorias que se comportam como conjuntos. O GDPR distingue os dados pessoais das categorias especiais do artigo 9, que incluem os dados relativos à saúde; a LGPD faz a mesma distinção entre dado pessoal (art. 5º, I) e dado pessoal sensível, que inclui o dado referente à saúde (art. 5º, II), com hipóteses de tratamento próprias no art. 11. Zara desenha um diagrama de Venn: todos os dados que a Pellmore guarda, o subconjunto que é dado pessoal e, dentro dele, o subconjunto que é dado de saúde. Ela percebe que quase tudo o que a Pellmore guarda cai no conjunto mais interno, porque até o horário de uma consulta em uma clínica de telemedicina revela que alguém procurou atendimento. Pensar em conjuntos a ajuda a ver por que as decisões de classificação precisam ser tomadas com cuidado.

### 2.3 O princípio da casa dos pombos

Se houver mais pombos do que casas, alguma casa terá pelo menos dois pombos. Zara usa a recíproca: quando há muito mais casas do que pombos, a maioria das casas tem no máximo um. Com duzentos milhões de combinações e 150.000 pacientes, a unicidade é quase garantida, a menos que os atributos sejam tornados mais grosseiros. O Prof. Holm pede que ela calcule quão grosseiros os atributos precisam ser para que cada combinação tenha, em média, pelo menos cinco pacientes. Reduzir a data de nascimento ao ano de nascimento e a área postal à região aproxima o número de combinações da escala necessária.

### 2.4 Grafos de relações

A matemática discreta também trata de grafos. Zara modela os sistemas da Pellmore como nós e os fluxos de dados como arestas. Um prontuário vai do aplicativo para o banco de agendamentos, depois para o fornecedor de vídeo, o sistema de prontuários e o laboratório parceiro. O grafo mostra por onde os dados pessoais circulam e quais nós se ligam a organizações externas. Ela aprende que esse grafo é o ponto de partida de um registro das atividades de tratamento, exigido pelo artigo 30 do GDPR e, no Brasil, pelo art. 37 da LGPD, e que arestas ausentes no diagrama costumam significar fluxos não documentados e, portanto, não gerenciados.

### Exemplo resolvido

Zara conta mais de duzentos milhões de combinações de atributos para 150.000 pacientes, classifica os dados da Pellmore com conjuntos, aplica o princípio da casa dos pombos à unicidade e desenha um grafo de fluxos de dados.

> **Caso sintético.** Os números de pacientes são sintéticos; os artigos 9 e 30 do GDPR, os arts. 5º, 11 e 37 da LGPD e Sweeney (2002) são reais.

### Erros e limites

A contagem uniforme presume valores igualmente prováveis; os atributos reais se concentram.

### Exercícios

- **EX004 — Contagem de combinações.** Por que muitos pacientes ficam sozinhos em sua combinação? *Rubrica:* 3 = as combinações superam em muito o número de pacientes;; 2 = menciona números;; 1 = errado;; 0 = nenhuma.
- **EX005 — Conjunto mais interno.** Por que a maior parte dos dados da Pellmore cai no subconjunto dos dados de saúde? *Rubrica:* 3 = até as consultas agendadas revelam que alguém procurou atendimento médico;; 2 = menciona saúde;; 1 = diz que só os prontuários;; 0 = nenhuma.
- **EX006 — Arestas ausentes.** O que costuma significar uma aresta ausente no grafo de fluxos de dados? *Rubrica:* 3 = um fluxo não documentado que não é gerenciado;; 2 = menciona erro;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) explicar como os dados persistem nos meios físicos; (2) raciocinar sobre a eliminação no nível do hardware; (3) ligar fatos físicos às obrigações de eliminação.

### 3.1 Bits são físicos

Na disciplina de física para computação, Zara aprende que os bits armazenados são estados físicos: carga em células de memória flash, regiões magnetizadas em discos. Apagar um arquivo costuma remover apenas um ponteiro, deixando os estados intactos até serem sobrescritos. Para a Pellmore, isso importa porque o direito ao apagamento do artigo 17 do GDPR exige que os dados sejam apagados sem demora injustificada em certos casos, e a LGPD dá ao titular o direito à eliminação (art. 18, IV e VI), definida como a exclusão de dado armazenado em banco de dados, independentemente do procedimento empregado (art. 5º, XIV). Se os engenheiros igualarem apagar uma linha do banco de dados a eliminar os dados, cópias podem persistir em discos, logs e backups, o que cria uma distância entre o que o sistema informa e o que é fisicamente verdadeiro.

### 3.2 Memória flash e nivelamento de desgaste

As unidades de estado sólido distribuem as gravações entre as células para não desgastar nenhuma área isolada. Uma consequência é que sobrescrever um arquivo pode gravar em células novas e deixar as antigas intactas. Zara lê que a eliminação segura nesses meios depende de comandos de sanitização embutidos ou de criptografia. Com a criptografia, os dados são guardados apenas em forma cifrada, e destruir a chave torna ilegíveis todas as cópias. Essa abordagem, muitas vezes chamada de apagamento criptográfico, é atraente para o arquivo de vídeo da Pellmore, em que sobrescrever fisicamente cada cópia seria impraticável em tantas unidades.

### 3.3 Energia e retenção

A física também ensina que o armazenamento consome energia e espaço. Guardar anos de teleconsultas em vídeo tem um custo em eletricidade e refrigeração, além do custo em risco. Zara escreve uma nota curta para a equipe de instalações da Pellmore ligando a retenção ao consumo de energia. Uma retenção mais curta reduz tanto a pegada ambiental quanto a quantidade de dados de saúde expostos em um vazamento. O argumento não é decisivo sozinho, mas mostra que a engenharia de privacidade costuma se alinhar a outros objetivos de engenharia, o que pode tornar as propostas mais fáceis de aceitar pelos gestores.

### 3.4 Sinais e canais laterais

Por fim, Zara estuda como os sinais físicos vazam informação. As chamadas de vídeo enviam pacotes cujos tamanhos e tempos podem revelar atividade mesmo quando o conteúdo está cifrado, e as telas emitem sinais fracos. Para a Pellmore, a lição prática é modesta: cifrar o vídeo protege o conteúdo, mas metadados como a duração e o horário da chamada ainda revelam que um paciente consultou um médico. Ela anota isso como um tema a retomar quando estudar redes e modelos de ameaça, porque proteger os metadados costuma exigir escolhas de projeto, e não apenas criptografia.

### Exemplo resolvido

Zara explica que apagar uma linha deixa vestígios físicos, propõe o apagamento criptográfico para o arquivo de vídeo, liga a retenção ao consumo de energia e registra o vazamento de metadados das chamadas cifradas.

> **Caso sintético.** O arquivo da Pellmore é sintético; o artigo 17 do GDPR e os arts. 5º e 18 da LGPD são reais.

### Erros e limites

O apagamento criptográfico depende de as chaves nunca serem copiadas em texto claro; a gestão de chaves passa a ser o controle crítico.

### Exercícios

- **EX007 — Eliminação do ponteiro.** Por que apagar um arquivo muitas vezes não elimina os dados? *Rubrica:* 3 = só o ponteiro é removido; os estados físicos permanecem até serem sobrescritos;; 2 = menciona sobrescrita;; 1 = diz que elimina;; 0 = nenhuma.
- **EX008 — Apagamento criptográfico.** Como funciona o apagamento criptográfico? *Rubrica:* 3 = os dados são guardados cifrados; destruir a chave torna ilegível cada cópia;; 2 = menciona chaves;; 1 = descreve sobrescrita;; 0 = nenhuma.
- **EX009 — Vazamento de metadados.** O que ainda vaza de uma chamada de vídeo cifrada? *Rubrica:* 3 = metadados como horário e duração revelam que a consulta ocorreu;; 2 = menciona metadados;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas simples que tratem dados pessoais com segurança; (2) evitar registrar identificadores em logs; (3) validar entradas para reduzir erros de coleta.

### 4.1 Primeiros programas com dados pessoais

A primeira disciplina de programação de Zara usa Python. Seu primeiro trabalho, um script de agendamento, pede o nome e a data de nascimento do paciente e imprime uma confirmação. O Prof. Holm aponta que as mensagens de depuração dela incluem a data de nascimento completa, que acabaria nos logs se o script rodasse em um servidor. Os logs costumam ser guardados por mais tempo e protegidos com menos cuidado do que os bancos de dados. Zara troca a mensagem por outra que contém apenas um código de agendamento, um hábito que as orientações do EDPB sobre proteção de dados desde a concepção descreveriam como proteger os dados por padrão.

### 4.2 Validando a entrada

O formulário de agendamento aceita texto livre para o motivo da consulta. Zara percebe que os pacientes digitam muito mais do que o necessário, incluindo medicamentos e histórico familiar. Ela muda o formulário para oferecer uma lista curta de tipos de consulta e um campo de texto livre limitado, com uma nota clara sobre o que incluir. Validar e limitar a entrada é uma técnica de programação, mas também aplica o princípio da minimização de dados do artigo 5(1)(c) do GDPR, que exige dados adequados, pertinentes e limitados ao necessário, e o princípio da necessidade da LGPD (art. 6º, III).

### 4.3 Funções e responsabilidade

À medida que o script cresce, Zara o divide em funções: uma para coletar a entrada, uma para validar e uma para armazenar. Ela acrescenta uma função que pseudonimiza o identificador do paciente com um hash com chave antes de passá-lo à área de análise. A chave fica guardada separadamente, o que corresponde à definição de pseudonimização do artigo 4(5) do GDPR e à do art. 13, § 4º, da LGPD. Ela aprende que concentrar a lógica de privacidade em uma única função a torna mais fácil de testar e mais difícil de esquecer, e que um nome de função como pseudonymise também documenta a intenção para outros desenvolvedores.

### 4.4 Testando com dados falsos

Os testes de Zara usam pacientes inventados, gerados pelo próprio script, e nunca dados reais copiados da Pellmore. Ela escreve um teste que verifica que nenhuma linha de log contém um padrão de data de nascimento. O Prof. Holm chama isso de teste unitário de privacidade e pede à turma que acrescente um a cada trabalho. O hábito de testar automaticamente as propriedades de privacidade vai se tornar importante mais tarde, nos laboratórios de verificação, em que Zara testará sistemas inteiros, mas começa com poucas linhas em um exercício de programação do primeiro ano e com o compromisso de nunca usar prontuários reais no desenvolvimento.

### Exemplo resolvido

Zara retira as datas de nascimento das mensagens de depuração, limita o texto livre, isola a pseudonimização em uma função e acrescenta um teste unitário de privacidade que procura datas de nascimento nos logs.

> **Caso sintético.** O script e os pacientes são sintéticos; os artigos 4(5) e 5(1)(c) do GDPR, os arts. 6º e 13 da LGPD e as Diretrizes 4/2019 do EDPB são reais.

### Erros e limites

Um hash com chave é pseudonimização, não anonimização; quem tem a chave pode refazer a vinculação.

### Exercícios

- **EX010 — Logs de depuração.** Por que imprimir datas de nascimento nas mensagens de depuração é arriscado? *Rubrica:* 3 = os logs são guardados por mais tempo e protegidos com menos cuidado do que os bancos de dados;; 2 = menciona logs;; 1 = inofensivo;; 0 = nenhuma.
- **EX011 — Limites do texto livre.** Que princípio do GDPR limitar o texto livre aplica? *Rubrica:* 3 = a minimização de dados do artigo 5(1)(c);; 2 = menciona minimização;; 1 = cita outro;; 0 = nenhuma.
- **EX012 — Teste unitário de privacidade.** O que o teste unitário de privacidade de Zara verifica? *Rubrica:* 3 = que nenhuma linha de log contém um padrão de data de nascimento;; 2 = menciona logs;; 1 = omite;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever avisos de privacidade que engenheiros e pacientes entendam; (2) documentar decisões de projeto; (3) explicar o risco sem jargão.

### 5.1 Escrevendo para pacientes

Na disciplina de comunicação em engenharia, Zara reescreve o aviso de privacidade da Pellmore. O original é longo e cheio de linguagem jurídica. Os artigos 12 a 14 do GDPR exigem que a informação seja prestada de forma concisa, transparente, inteligível e de fácil acesso, em linguagem clara e simples; a LGPD exige informações claras, precisas e facilmente acessíveis (art. 6º, VI), disponibilizadas de forma clara, adequada e ostensiva (art. 9º). Zara reorganiza o aviso em torno das perguntas dos pacientes: o que é coletado, por quê, quem vê, por quanto tempo é guardado e como exercer os direitos. Ela testa o rascunho com cinco colegas que não são engenheiros e reescreve cada frase que eles entendem errado. O aviso final é mais curto e mais preciso.

### 5.2 Informação em camadas

Zara aprende que um único documento não serve a todos. Ela desenha um aviso em camadas: um resumo curto no momento do agendamento, um aviso completo acessível a partir dele e explicações específicas no momento em que um recurso usa dados, como quando o aplicativo pede acesso à câmera. Acquisti, Brandimarte e Loewenstein (2015) descrevem como as decisões de privacidade das pessoas dependem do contexto e da forma de apresentação, o que sustenta dar a informação no momento da decisão, e não só em um documento longo lido uma vez, se tanto, quando a conta é criada.

### 5.3 Registros de decisões de projeto

Os engenheiros também precisam se comunicar entre si. Zara começa um registro de decisões para seu trabalho na Pellmore. Cada entrada informa a decisão, as alternativas consideradas, o raciocínio de privacidade e quem a aprovou. Por exemplo, ela registra a escolha de guardar códigos de agendamento, e não nomes, na área de análise. O Prof. Holm explica que esses registros sustentam o princípio da responsabilidade do artigo 5(2) do GDPR, que exige que o controlador consiga demonstrar a conformidade, equivalente ao princípio de responsabilização e prestação de contas da LGPD (art. 6º, X), e que eles ajudam futuros engenheiros a entender por que um sistema tem a forma que tem.

### 5.4 Explicando o risco com clareza

Zara pratica explicar o risco a gestores. Em vez de dizer que um conjunto de dados tem alto risco de reidentificação, ela diz que alguém que conheça o código postal e a data de nascimento de um paciente poderia encontrar nele o histórico de consultas desse paciente. Explicações concretas levam a decisões melhores, porque os gestores conseguem imaginar o dano. Ela também aprende a declarar a incerteza com honestidade, por exemplo que uma estimativa de risco depende do que o atacante sabe, sem se esconder atrás dela. A comunicação, conclui, é uma competência de engenharia que determina se bons projetos chegam a ser adotados.

### Exemplo resolvido

Zara reescreve o aviso de privacidade em torno das perguntas dos pacientes, distribui-o em camadas nos pontos de decisão, começa um registro de decisões para a responsabilização e pratica explicações concretas do risco.

> **Caso sintético.** O aviso e o registro de decisões são sintéticos; os artigos 5(2) e 12–14 do GDPR, os arts. 6º e 9º da LGPD e Acquisti et al. (2015) são reais.

### Erros e limites

A linguagem simples precisa continuar precisa; uma simplificação que descreve mal o tratamento viola a transparência.

### Exercícios

- **EX013 — Padrão de transparência.** Que forma a informação deve ter segundo o GDPR? *Rubrica:* 3 = concisa, transparente, inteligível, de fácil acesso, em linguagem clara e simples;; 2 = lista algumas;; 1 = diz detalhada;; 0 = nenhuma.
- **EX014 — Aviso no momento certo.** Por que informar quando um recurso usa dados? *Rubrica:* 3 = as decisões dependem do contexto, então a informação naquele momento é mais útil;; 2 = menciona o momento;; 1 = diz que uma vez basta;; 0 = nenhuma.
- **EX015 — Papel do registro de decisões.** Que princípio o registro de decisões sustenta? *Rubrica:* 3 = a responsabilidade do artigo 5(2);; 2 = menciona responsabilização;; 1 = cita outro;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) integrar a exposição ao longo do tempo; (2) modelar o decaimento exponencial do risco; (3) usar séries para acumular a perda de privacidade.

### 6.1 Exposição acumulada

Zara modela a exposição da Pellmore como o número de prontuários armazenados multiplicado pelo tempo em que ficam armazenados. Integrar o armazenamento ao longo de um ano dá a exposição em pacientes-dia. Um prazo de retenção de trinta dias para as gravações de vídeo, em vez do armazenamento indefinido, reduz drasticamente a integral, mesmo que a entrada diária não mude. Ela mostra o cálculo ao líder de engenharia da Pellmore como a área sob duas curvas. O gráfico torna imediato o efeito da retenção e fornece um único número que pode ser acompanhado como indicador-chave. Na LGPD, a mesma ideia aparece no término do tratamento quando a finalidade é alcançada (art. 15, I) e na eliminação que se segue (art. 16).

### 6.2 Decaimento e obsolescência

Alguns riscos decaem. Um endereço antigo é menos útil para um atacante do que o atual, e a utilidade dos dados de contato poderia ser modelada como um decaimento exponencial no tempo. Zara adverte contra o uso excessivo do modelo: a informação de saúde não perde sensibilidade com a idade, e um diagnóstico de dez anos atrás ainda pode prejudicar alguém. Ela conclui que os modelos de decaimento podem orientar a retenção de dados de baixa sensibilidade, mas as categorias especiais precisam de regras explícitas, e não da suposição de que o risco desaparece naturalmente com o tempo.

### 6.3 Séries e acumulação

Em trabalhos posteriores, Zara vai publicar estatísticas repetidas. O Cálculo II apresenta as séries, somas de muitos termos. Se cada publicação vazar uma pequena quantidade de informação, o total depois de muitas publicações é a soma. Zara escreve a soma para publicações diárias e vê que ela cresce sem limite. Isso antecipa a propriedade de composição da privacidade diferencial descrita por Dwork e Roth (2014), em que a perda de privacidade se soma entre as consultas, e a deixa cética diante de qualquer afirmação de que publicações frequentes são seguras porque cada uma, isoladamente, é inofensiva.

### 6.4 Aproximação

As aproximações de Taylor permitem aos engenheiros trocar uma função complexa por uma simples perto de um ponto. Zara usa a ideia para estimar como uma pequena mudança na retenção afeta a exposição: perto da política atual, a exposição varia aproximadamente em proporção ao prazo de retenção. Ela usa isso para explicar que reduzir a retenção à metade reduz aproximadamente à metade a exposição daquela categoria. O Prof. Holm lembra que as aproximações só valem perto do ponto em que foram feitas, uma cautela útil sempre que os engenheiros extrapolam de pequenas mudanças para grandes reformulações.

### Exemplo resolvido

Zara integra o armazenamento para obter a exposição em pacientes-dia, limita os modelos de decaimento aos dados de baixa sensibilidade, soma as publicações repetidas para antecipar a composição e usa uma aproximação linear para mudanças de retenção.

> **Caso sintético.** Os números de exposição são sintéticos; Dwork e Roth (2014) e os arts. 15 e 16 da LGPD são reais.

### Erros e limites

A medida em pacientes-dia ignora diferenças de sensibilidade entre registros; pondere as categorias quando necessário.

### Exercícios

- **EX016 — Pacientes-dia.** O que mede a integral do armazenamento ao longo do tempo? *Rubrica:* 3 = a exposição acumulada em pacientes-dia;; 2 = menciona área;; 1 = tamanho do armazenamento;; 0 = nenhuma.
- **EX017 — Cautela com o decaimento.** Por que os modelos de decaimento não servem para dados de saúde? *Rubrica:* 3 = a informação de saúde mantém sua sensibilidade com o tempo;; 2 = menciona sensibilidade;; 1 = aceita o decaimento;; 0 = nenhuma.
- **EX018 — Publicações somadas.** O que mostra a soma dos vazamentos diários? *Rubrica:* 3 = a perda total de privacidade cresce sem limite à medida que as publicações continuam;; 2 = menciona crescimento;; 1 = diz que fica pequena;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) aplicar a resposta aleatorizada a uma pesquisa sensível; (2) estimar uma proporção e sua incerteza; (3) explicar o compromisso entre privacidade e precisão.

### 7.1 Uma pergunta sensível

A Pellmore quer saber quantos pacientes deixam de tomar a medicação prescrita, mas os pacientes podem não responder com honestidade se temerem que o médico veja. Zara propõe a resposta aleatorizada, uma técnica clássica de pesquisa. Cada paciente joga uma moeda em segredo: se der cara, responde a verdade; se der coroa, joga de novo e responde sim se der cara e não se der coroa. Qualquer sim isolado pode ter vindo da moeda, então nenhuma resposta revela a verdade sobre um indivíduo, mas a proporção geral ainda pode ser estimada a partir de muitas respostas, porque o comportamento da moeda é conhecido.

### 7.2 Estimando a parcela

O laboratório simula 2.000 pacientes, dos quais 17,9% de fato deixam de tomar a medicação. Com o desenho da moeda, um quarto de todas as respostas são sins aleatórios, então a parcela observada de sins é 0,344. A estimativa subtrai a parte aleatória e dobra o restante, dando 0,189, com intervalo de 95% de 0,147 a 0,231. O intervalo contém o valor verdadeiro. Zara explica cada passo à líder clínica da Pellmore, enfatizando que a estimativa descreve o grupo e que as respostas individuais continuam negáveis até para a equipe da pesquisa. A líder clínica aceita o método para a pesquisa piloto.

### 7.3 O custo da negabilidade

A privacidade tem um preço em precisão. Uma pesquisa direta com 2.000 respondentes honestos teria erro padrão de 0,009, mas a resposta aleatorizada tem 0,021, mais que o dobro. Zara explica que o ruído que protege os indivíduos também borra a estimativa, então é preciso uma amostra maior para obter a mesma precisão. É o mesmo compromisso que ela encontrará na privacidade diferencial, em que a resposta aleatorizada costuma ser apresentada como um exemplo pioneiro de mecanismo que dá a cada respondente uma negabilidade plausível. O ruído amplia o erro da estimativa.

### 7.4 Respostas honestas como o ganho real

Zara também observa que a comparação com uma pesquisa direta presume que os pacientes responderiam com honestidade, que é exatamente o que a Pellmore duvida. Se o medo fizer muitos pacientes negarem que deixam de tomar a medicação, uma pesquisa direta seria precisa, mas errada. A resposta aleatorizada troca precisão por honestidade. Ela a recomenda para essa pergunta e escreve uma breve explicação para o consentimento, para que os pacientes entendam o mecanismo da moeda. O Prof. Holm acrescenta que a estatística não consiste apenas em calcular intervalos, mas em entender como os dados foram gerados e o que poderia enviesá-los.

### Laboratório — Pesquisa por resposta aleatorizada sobre adesão à medicação

```python
# Randomised response: estimate how many of 2,000 synthetic patients skipped medication, without learning anyone's answer.
import random
r = random.Random(4)
true_p, n = 0.18, 2000
truth = [r.random() < true_p for _ in range(n)]
# each respondent flips a coin: heads answer truthfully, tails answer "yes" with probability 1/2
ans = [t if r.random() < 0.5 else (r.random() < 0.5) for t in truth]
y = sum(ans) / n
est = (y - 0.25) / 0.5
se = (y * (1 - y) / n) ** 0.5 / 0.5
print(f"true share {sum(truth)/n:.3f}; observed yes {y:.3f}; estimate {est:.3f} (95% CI {est-1.96*se:.3f} to {est+1.96*se:.3f})")
print(f"direct-survey standard error would be {(est*(1-est)/n)**0.5:.3f}; randomised response {se:.3f}")
```

Execute com `python3 lab_rr.py`. Saída verificada:

```text
true share 0.179; observed yes 0.344; estimate 0.189 (95% CI 0.147 to 0.231)
direct-survey standard error would be 0.009; randomised response 0.021
```

### Exemplo resolvido

Zara estima a parcela que deixa de tomar a medicação em 0,189 (intervalo de 95% de 0,147 a 0,231) contra um valor verdadeiro de 0,179, e mostra o erro padrão subindo de 0,009 para 0,021 como o preço da negabilidade.

> **Caso sintético.** Os pacientes e as respostas são sintéticos e gerados com semente fixa.

### Erros e limites

O método só protege diante de quem conduz a pesquisa se os pacientes confiarem na moeda; uma explicação ruim o enfraquece.

### Exercícios

- **EX019 — Negabilidade.** Por que um sim isolado não revela o comportamento de um paciente? *Rubrica:* 3 = ele pode vir da moeda, e não da verdade;; 2 = menciona aleatoriedade;; 1 = diz que revela;; 0 = nenhuma.
- **EX020 — Cálculo da estimativa.** Como a estimativa 0,189 é obtida a partir de 0,344? *Rubrica:* 3 = subtrair os 0,25 de sins aleatórios e dividir por 0,5;; 2 = descreve em parte;; 1 = errado;; 0 = nenhuma.
- **EX021 — Razão entre erros.** Quanto maior é o erro padrão da resposta aleatorizada? *Rubrica:* 3 = 0,021 contra 0,009, mais que o dobro;; 2 = menciona que é maior;; 1 = errado;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) rastrear onde os dados ficam na memória e nos caches; (2) entender o isolamento por hardware; (3) avaliar recursos de hardware para proteger dados de saúde.

### 8.1 Dados em muitos lugares

Em arquitetura de computadores, Zara acompanha um prontuário dentro de um servidor. Ele fica no disco, é copiado para a memória, passa pelos caches do processador e pode ser gravado na área de troca (swap). Cada cópia é um lugar onde os dados podem persistir ou vazar. Ela percebe que uma aplicação que elimina os registros com cuidado ainda pode deixar fragmentos em despejos de memória ou em arquivos de troca. Para a Pellmore, ela recomenda swap cifrado e a desativação, nos servidores de produção, dos despejos de falha que incluem a memória, a menos que um despejo seja pedido explicitamente e tratado por um procedimento definido.

### 8.2 Isolamento

A arquitetura oferece isolamento: os processos normalmente não leem a memória uns dos outros, e as máquinas virtuais são separadas por um hipervisor. Zara aprende que falhas de hardware às vezes romperam essas fronteiras, de modo que os clientes de uma nuvem compartilham risco com os vizinhos. Para o sistema de prontuários da Pellmore, ela lê a documentação do provedor de nuvem sobre hosts dedicados e computação confidencial, que cifra a memória em uso. Ela observa que esses recursos reduzem o risco, mas acrescentam custo e complexidade, e que a escolha deve seguir uma avaliação de risco, e não um folheto de fornecedor.

### 8.3 Hardware confiável para as chaves

Os módulos de segurança de hardware (HSM) e os enclaves seguros mantêm as chaves criptográficas longe da memória comum. Zara liga isso ao Capítulo 3: se a Pellmore usar apagamento criptográfico para os vídeos, as chaves são o ativo mais valioso, e guardá-las em um módulo de hardware torna a cópia acidental muito mais difícil. Ela esboça um projeto em que cada mês de gravações tem sua própria chave, guardada no módulo, e apagar a chave de um mês elimina aquele mês. O projeto transforma o cumprimento da retenção em uma operação de chave simples e auditável. Os auditores podem conferir os logs de exclusão de chaves.

### 8.4 Compromissos de desempenho

A criptografia e o isolamento custam tempo de processador. Zara mede que cifrar o vídeo em repouso acrescenta pouca carga em processadores modernos com aceleração por hardware. Ela registra a medição em seu registro de decisões, porque a alegação de que as medidas de privacidade são lentas demais muitas vezes bloqueia bons projetos sem evidência. O Prof. Holm lembra que as medições devem ser repetidas com a carga real da Pellmore, mas seus primeiros números bastam para levar a conversa da opinião para os dados, um objetivo recorrente em sua formação de engenharia. A criptografia acrescenta uma latência mensurável.

### Exemplo resolvido

Zara mapeia as cópias de um prontuário do disco ao cache, recomenda swap cifrado, considera a computação confidencial e projeta chaves mensais em um módulo de hardware para o apagamento criptográfico.

> **Caso sintético.** Os servidores da Pellmore são sintéticos.

### Erros e limites

Os recursos de hardware têm suas próprias falhas; a defesa em profundidade continua importando.

### Exercícios

- **EX022 — Cópias ocultas.** Cite dois lugares onde um registro apagado pode persistir em um servidor. *Rubrica:* 3 = despejos de memória e swap (também caches);; 2 = cita um;; 1 = nenhum;; 0 = nenhuma.
- **EX023 — Chaves mensais.** Como as chaves mensais tornam a retenção auditável? *Rubrica:* 3 = apagar a chave de um mês elimina as gravações daquele mês em uma operação;; 2 = menciona chaves;; 1 = omite;; 0 = nenhuma.
- **EX024 — Evidência acima da opinião.** Por que medir a sobrecarga da criptografia? *Rubrica:* 3 = para substituir por dados as alegações de que a privacidade é lenta demais;; 2 = menciona velocidade;; 1 = pula a medição;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) projetar estruturas de dados que separem os identificadores; (2) aplicar verificações de acesso no código; (3) escrever testes para propriedades de privacidade.

### 9.1 Separando os identificadores

Em Programação II, Zara projeta o prontuário da Pellmore como duas estruturas ligadas: uma tabela de identidade, com nome e dados de contato, e uma tabela clínica indexada por um identificador interno. A maioria dos serviços precisa só da parte clínica ou só da parte de identidade, raramente das duas. Separá-las no código facilita dar a cada serviço apenas o que ele precisa. Ela reconhece nisso uma implementação da proteção de dados desde a concepção, em que a própria estrutura do software limita a exposição, em vez de depender de que cada desenvolvedor se lembre de uma regra; a LGPD pede o mesmo ao exigir que as medidas de segurança sejam observadas desde a fase de concepção do produto ou serviço (art. 46, § 2º).

### 9.2 Verificações de acesso no código

Zara escreve uma função que todo serviço precisa chamar antes de ler um prontuário. Ela confere o papel de quem chama e a finalidade do pedido contra uma tabela de política. Uma recepcionista pode ler os horários das consultas, mas não as anotações clínicas; um médico só pode ler as anotações dos pacientes agendados com ele. A função registra cada acesso com a finalidade. Ela testa que uma chamada sem finalidade falha. O Prof. Holm observa que concentrar as verificações em um só lugar evita regras inconsistentes, que são uma fonte comum de acesso amplo demais em sistemas reais.

### 9.3 Testes baseados em propriedades

Zara aprende os testes baseados em propriedades, em que uma ferramenta gera muitas entradas aleatórias para testar regras gerais. Ela escreve propriedades como nenhuma função devolver um prontuário clínico ao papel de recepcionista, e nenhuma função de exportação incluir a tabela de identidade. A ferramenta encontra um defeito: uma exportação escrita por um colega junta as duas tabelas por conveniência. Corrigi-lo elimina um caminho pelo qual prontuários completos poderiam sair do sistema. Ela percebe que testar propriedades de privacidade de forma geral é mais poderoso do que conferir alguns exemplos escolhidos à mão.

### 9.4 Tratamento de erros

Mensagens de erro podem vazar dados. Zara descobre que um agendamento que falha devolve um erro com o prontuário completo do paciente, para fins de depuração. Ela muda os erros para devolverem um código de referência e registra os detalhes internamente, sob controle de acesso. Também garante que as exceções não mostrem aos usuários pilhas de chamadas com valores de variáveis. Essas pequenas mudanças reduzem a divulgação acidental, que muitas vezes acontece por caminhos comuns do software, como os erros, e não por ataques dramáticos, e deixam o sistema mais profissional aos olhos dos pacientes e dos auditores.

### Exemplo resolvido

Zara separa a identidade dos dados clínicos, centraliza as verificações de acesso por finalidade, encontra um defeito de exportação com testes baseados em propriedades e retira dados das mensagens de erro.

> **Caso sintético.** O código e os pacientes são sintéticos; o art. 46 da LGPD é real.

### Erros e limites

Verificações centrais viram um ponto único de falha; precisam de seus próprios testes e monitoramento.

### Exercícios

- **EX025 — Prontuário dividido.** Por que dividir os dados de identidade e os clínicos em duas estruturas? *Rubrica:* 3 = a maioria dos serviços precisa de uma parte só, então cada um recebe apenas o que precisa;; 2 = menciona separação;; 1 = sem motivo;; 0 = nenhuma.
- **EX026 — Finalidade no acesso.** Por que quem chama precisa declarar uma finalidade para ler um prontuário? *Rubrica:* 3 = o acesso é conferido e registrado contra a finalidade, evitando uso amplo demais;; 2 = menciona registro;; 1 = diz que é opcional;; 0 = nenhuma.
- **EX027 — Achado do teste de propriedades.** Que defeito o teste baseado em propriedades encontrou? *Rubrica:* 3 = uma exportação que juntava as tabelas de identidade e clínica;; 2 = menciona exportação;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética da engenharia às decisões de privacidade; (2) reconhecer danos que vão além da conformidade legal; (3) decidir quando escalar preocupações.

### 10.1 Deveres de uma engenheira

A ética da engenharia pede aos profissionais que coloquem acima de tudo a segurança e o bem-estar do público. Zara aplica isso à Pellmore. A exposição de dados de saúde pode causar discriminação, constrangimento, perda do emprego e sofrimento. Warren e Brandeis (1890) escreveram sobre o dano aos sentimentos; Solove (2006) lista danos como a divulgação, a exposição e o aumento da acessibilidade. Zara escreve que seu dever não é só cumprir a lei, mas prevenir danos previsíveis aos pacientes, mesmo quando nenhum regulador perceberia, porque os pacientes não conseguem ver nem controlar como o sistema é construído.

### 10.2 Além da conformidade

Zara encontra um caso em que a lei e a ética divergem. A equipe de análise da Pellmore quer inferir gravidez a partir dos padrões de consultas para enviar dicas de saúde direcionadas. O tratamento poderia ser enquadrado como lícito com consentimento, mas muitas pacientes o achariam invasivo, e algumas poderiam ser prejudicadas se um familiar visse as mensagens. A integridade contextual de Nissenbaum a ajuda a formular o problema: uma informação compartilhada para o cuidado está fluindo para o marketing, um contexto diferente, com normas diferentes. Ela recomenda não criar o recurso e registra seu raciocínio no registro de decisões.

### 10.3 Segurança dos pacientes

A telemedicina acrescenta preocupações de segurança. Se uma teleconsulta falhar em silêncio, um paciente pode perder um atendimento urgente. Zara aprende que as medidas de privacidade não podem criar riscos à segurança do paciente: um tempo limite de sessão rígido demais poderia interromper uma consulta. Ela trabalha com os médicos para definir tempos limite que protejam aparelhos deixados sem supervisão sem encerrar chamadas ativas. O exercício lhe ensina que segurança e privacidade são deveres para com os mesmos pacientes, e que os engenheiros precisam equilibrá-las abertamente, em vez de maximizar uma em silêncio à custa da outra.

### 10.4 Escalonamento

Zara pergunta o que deveria fazer se um gestor ignorasse uma preocupação séria de privacidade. O Prof. Holm explica que ela deveria primeiro documentar a preocupação e levá-la ao orientador e ao encarregado de proteção de dados, cujo papel nos artigos 38 e 39 do GDPR inclui aconselhar a organização e monitorar a conformidade com independência. Na LGPD, cabe ao encarregado orientar os funcionários e contratados sobre as práticas de proteção de dados (art. 41, § 2º, III), e sua atuação é regulamentada pela Resolução CD/ANPD nº 18/2024. Se a preocupação continuar sem resposta e os pacientes estiverem em risco, códigos profissionais e proteções a denunciantes podem se aplicar. Zara escreve um plano pessoal de escalonamento, esperando nunca usá-lo, mas mais segura de conhecer o caminho.

### Exemplo resolvido

Zara enquadra seu dever em torno do dano previsível, recomenda não inferir gravidez com base na integridade contextual, equilibra os tempos limite com a segurança clínica e escreve um caminho de escalonamento que passa pelo encarregado de proteção de dados.

> **Caso sintético.** A proposta da equipe de análise é sintética; Warren e Brandeis (1890), Solove (2006), Nissenbaum (2004), os artigos 38–39 do GDPR, o art. 41 da LGPD e a Resolução CD/ANPD nº 18/2024 são reais.

### Erros e limites

O julgamento ético varia; registrar o raciocínio permite que outros o contestem.

### Exercícios

- **EX028 — Dever ético.** Que dever vai além da conformidade legal para Zara? *Rubrica:* 3 = prevenir danos previsíveis aos pacientes mesmo quando ninguém perceberia;; 2 = menciona dano;; 1 = só a lei;; 0 = nenhuma.
- **EX029 — Inferência de gravidez.** Por que Zara desaconselha o recurso de inferência de gravidez? *Rubrica:* 3 = a informação de cuidado flui para o marketing, rompendo as normas do contexto e arriscando dano;; 2 = menciona invasão;; 1 = apoia o recurso;; 0 = nenhuma.
- **EX030 — Papel do encarregado.** Por que escalar ao encarregado de proteção de dados? *Rubrica:* 3 = o encarregado aconselha e monitora a conformidade com independência, pelos artigos 38–39;; 2 = menciona o encarregado;; 1 = vai primeiro à imprensa;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Zara Mbeki, o Prof. Anders Holm, a Corwen Polytechnic, a Pellmore Telehealth e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Com a eliminação após um prazo fixo, a entrada iguala a saída, e os dados armazenados se estabilizam.

**EX002.** Ela se transforma no valor de uma única pessoa, então publicá-la divulga os dados dessa pessoa.

**EX003.** O risco para os indivíduos não pode ser trocado livremente por utilidade, e as exigências legais funcionam como restrições.

**EX004.** Há muito mais combinações possíveis do que pacientes, então a maioria das combinações abriga no máximo uma pessoa.

**EX005.** Em uma prestadora de telemedicina, quase qualquer dado pessoal, até os horários de agendamento, indica atendimento de saúde; na LGPD, é dado pessoal sensível (art. 5º, II).

**EX006.** Um fluxo de dados não documentado que ninguém está gerenciando.

**EX007.** O sistema de arquivos descarta sua referência, mas os estados armazenados persistem até serem sobrescritos.

**EX008.** Todas as cópias são cifradas sob uma única chave; destruir a chave as torna ilegíveis.

**EX009.** O horário e a duração revelam que um paciente consultou um profissional de saúde, mesmo que o conteúdo esteja protegido.

**EX010.** Os logs costumam persistir e ser menos protegidos, então identificadores neles criam exposição evitável.

**EX011.** Minimização de dados: os dados devem ser adequados, pertinentes e limitados ao necessário; na LGPD, o princípio da necessidade (art. 6º, III).

**EX012.** Ele varre a saída dos logs e falha se alguma linha contiver uma data de nascimento.

**EX013.** Concisa, transparente, inteligível e de fácil acesso, em linguagem clara e simples.

**EX014.** As pessoas decidem dentro de um contexto, então explicações no momento do uso são mais eficazes do que um único aviso longo.

**EX015.** Responsabilidade: conseguir demonstrar a conformidade; na LGPD, responsabilização e prestação de contas (art. 6º, X).

**EX016.** Mede a exposição acumulada: os dados de quantos pacientes foram guardados e por quanto tempo.

**EX017.** Um diagnóstico antigo ainda pode causar dano, então a sensibilidade não decai com a idade.

**EX018.** Pequenas perdas por publicação se somam, então publicações repetidas acumulam uma perda sem limite.

**EX019.** Qualquer sim pode ter sido produzido pela segunda moeda, então é plausivelmente negável.

**EX020.** (0,344 − 0,25) / 0,5 ≈ 0,189.

**EX021.** Cerca de 0,021 contra 0,009, mais que o dobro.

**EX022.** A área de troca (swap) e os despejos de falha; caches e memória também podem guardar fragmentos.

**EX023.** Os vídeos de cada mês compartilham uma chave; destruí-la elimina aquele mês, e a operação de chave é fácil de verificar.

**EX024.** As medições rebatem alegações sem fundamento de que a proteção custa caro demais.

**EX025.** Permite que cada serviço acesse apenas a parte de que precisa, limitando a exposição desde a concepção.

**EX026.** Verificações por finalidade limitam a leitura a usos legítimos e criam um registro que permite a prestação de contas.

**EX027.** Uma exportação de conveniência que juntava as duas tabelas, permitindo que prontuários completos saíssem.

**EX028.** Prevenir danos previsíveis aos pacientes, quer um regulador perceba ou não.

**EX029.** Leva a informação de cuidado para um contexto de marketing, violando as expectativas das pacientes e arriscando dano.

**EX030.** O papel independente do encarregado inclui aconselhar e monitorar a conformidade, o que o torna o canal adequado; no Brasil, sua atuação é regulamentada pela Resolução CD/ANPD nº 18/2024.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 18, de 16 de julho de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science, 347*(6221), 509–514. <https://doi.org/10.1126/science.aaa1465>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 18, de 16 de julho de 2024 — Aprova o Regulamento sobre a atuação do encarregado pelo tratamento de dados pessoais*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. <https://doi.org/10.1561/0400000042>
- Dwork, C., McSherry, F., Nissim, K., & Smith, A. (2006). Calibrating noise to sensitivity in private data analysis. *Theory of Cryptography (TCC 2006)*, 265–284. <https://doi.org/10.1007/11681878_14>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Data Protection Board. (2020). *Guidelines 4/2019 on Article 25 Data Protection by Design and by Default* (Version 2.0, adopted 20 October 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en>
- European Data Protection Board. (2021). *Guidelines 07/2020 on the concepts of controller and processor in the GDPR* (Version 2.0 adopted 7 July 2021; Version 2.1, 20 September 2022). <https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en>
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- European Data Protection Board. (2023). *Guidelines 9/2022 on personal data breach notification under GDPR* (Version 2.0, adopted 28 March 2023). <https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S. L. (2015). *De-identification of personal information* (NISTIR 8053). NIST. <https://doi.org/10.6028/NIST.IR.8053>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). NIST. <https://doi.org/10.6028/NIST.SP.800-188>
- ISO/IEC. (2011). *ISO/IEC 29100:2011 Information technology — Security techniques — Privacy framework*. <https://www.iso.org/standard/45123.html>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
- Warren, S. D., & Brandeis, L. D. (1890). The right to privacy. *Harvard Law Review, 4*(5), 193–220. <https://doi.org/10.2307/1321160>
