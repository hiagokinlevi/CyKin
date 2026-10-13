# Segurança Ofensiva Autorizada e Red Team: Um Livro para o Bacharelado

- Idioma: português do Brasil (`pt`); bacharelado, quatro anos; aproximadamente 3.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–40 de 40 têm texto didático escrito à mão; os exercícios EX001–EX120 têm resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, e suas saídas foram incorporadas a partir de execuções reais. A revisão independente e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de segurança e de computação em geral.
- Relação com os livros vizinhos: o [livro de engenharia](../../../../engineering-5-years/offensive-security-red-team/en/book/MANUSCRIPT.md) enfatiza a construção de plataformas de avaliação; o [livro de tecnólogo](../../../../technologist-3-years/offensive-security-red-team/en/book/MANUSCRIPT.md) enfatiza a implementação. **Este livro une teoria, casos, laboratórios e um projeto final.**
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação acreditada. **Não concede autorização para testar sistemas reais.** Todas as organizações, pessoas e números são **sintéticos**, salvo quando uma frase cita uma fonte pública. Os laboratórios ensinam escopo, medição e relato — nunca técnicas transformadas em arma.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–18 constroem os fundamentos de matemática, computação, escrita, ética e segurança; os 19–30 são o núcleo de testes autorizados, com laboratórios; os 31–40 cobrem casos avançados, pesquisa, trabalho comparativo, prática de campo, seminários e a tese do projeto final. Cada capítulo tem objetivos de aprendizagem, texto didático, um exemplo resolvido, um caso sintético rotulado, erros e limites, três exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios leem apenas dados locais (`python3 arquivo.py`).

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Riverstone Transit Bank (TRB)** — internet banking, razão contábil, gateway SWIFT (excluído), plataforma de avaliação TrackScope / FindingsDesk / PulseMap | Organização estudada ao longo do livro | Inventada |
| **Sam Ito** | Estagiário de engenharia na equipe da plataforma de avaliação autorizada | Inventado |

### Fontes principais

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) usar conjuntos e lógica para descrever o escopo; (2) aplicar contagem à cobertura; (3) identificar inferências inválidas num argumento de segurança.

### 1.1 Conjuntos para o escopo

Uma autorização escrita é um conjunto de sistemas. A pertinência é binária para cada alvo: dentro do escopo ou fora dele. Uniões de faixas e exclusões (conjuntos subtraídos) são a forma como o Riverstone Transit Bank (TRB) escreve suas ROE. Se o SWIFT fica na mesma /26 que um host web, a exclusão é uma diferença de conjuntos, não uma nota vaga. Escrever o escopo dessa forma também o torna testável: Sam pode passar qualquer endereço proposto a uma função de pertinência e obter um sim ou um não. Uma nota dizendo "evite o SWIFT" não pode ser testada; o conjunto {/26} menos {host SWIFT} pode.

### 1.2 Lógica da autorização

A permissão é necessária para testar; ela não é suficiente para todo método. "Dentro do escopo" e "método permitido" precisam ser ambos verdadeiros. Confundir os dois leva a técnicas não autorizadas em hosts autorizados. No TRB, um host pode estar dentro da /26 assinada enquanto as ROE ainda proíbem password spraying ou verificações de negação de serviço contra ele. Por isso, Sam mantém duas listas no TrackScope, uma de hosts e outra de métodos permitidos, e um teste só roda quando o par aparece nas duas. Um pedido para fazer spraying de credenciais contra um host web dentro do escopo falha na segunda lista, e a mensagem de rejeição nomeia a cláusula que o proíbe.

### 1.3 Contando a cobertura

Se 40 hosts estão no escopo e 28 foram tocados por cartões de método, a cobertura é 28/40. Porcentagens sem denominadores enganam examinadores e conselhos. Escrito como 28/40, o número diz ao leitor que doze hosts dentro do escopo não receberam nenhum cartão de método. Escrito como 70%, ele convida a pergunta "de quê?", e um membro do conselho pode lê-lo como 70% seguro. Por isso, os relatórios de Sam sempre mostram o numerador e o denominador juntos e listam os doze hosts não tocados por dono, para que possam ser agendados para a próxima janela autorizada em vez de sumirem silenciosamente da história.

### 1.4 Saltos inválidos

"O scanner não encontrou nada, então estamos seguros" confunde ausência de evidência com evidência de ausência. Os intervalos de Wilson do Capítulo 12 tornam numérica a humildade diante de amostras pequenas. Uma varredura limpa sobre 28 de 40 hosts não diz nada sobre os doze que nunca foram tocados, e pouco sobre técnicas que o scanner não consegue ver. Sam reescreve essas afirmações como enunciados delimitados: "nenhum achado dos tipos verificados nos 28 hosts testados nesta janela". A versão delimitada é menos reconfortante, mas é a única que a evidência sustenta, e diz ao leitor exatamente onde o próximo teste deve olhar.

### 1.5 Prática

Sam Ito, estagiário de engenharia na equipe da plataforma de avaliação autorizada do TRB, traduz cada frase das ROE em conjuntos antes que qualquer ferramenta rode. Na prática, isso significa que cada frase das ROE vira uma linha no seu caderno: o conjunto que ela nomeia, as exclusões que subtrai e os métodos que permite. A /26 menos o host SWIFT em .20 é uma dessas linhas. Só quando todas as frases foram traduzidas, e a tradução foi conferida com o documento assinado por uma segunda pessoa, ele carrega alguma coisa no TrackScope. Frases ambíguas voltam ao dono das ROE como perguntas, não como palpites.

### 1.6 Por que matemática aqui

Os capítulos posteriores sobre probabilidade, arquitetura e avaliação reutilizam a mesma linguagem cuidadosa. Uma linguagem de escopo descuidada produz testes descuidados. A fração de cobertura de 1.3 volta como uma proporção com intervalo no Capítulo 12, e a expressão de conjuntos de 1.1 vira a função de pertinência do TrackScope nos laboratórios. Aprender o vocabulário uma vez, com cuidado, significa que cada ferramenta posterior tem uma especificação precisa por trás, em vez de um hábito. O caderno de Sam deste capítulo é o primeiro artefato que seu mentor revisa. Uma definição vaga custa pouco para corrigir no caderno, mas a mesma imprecisão no TrackScope poderia colocar um host SWIFT no escopo.

### 1.7 Nota aplicada

Sam pratica a tradução de parágrafos das ROE em testes de pertinência no papel antes de abrir o TrackScope. Quando uma frase diz "VLAN web, exceto gateways de pagamento", ele escreve a expressão de conjuntos e lista todos os endereços de gateway conhecidos a partir do registro de ativos. Só então ele carrega o arquivo de escopo. Terceirizados que pulam a etapa do papel propõem com frequência hosts que ficam ao lado do SWIFT "porque o ping funcionou". A etapa do papel é mais lenta e evita incidentes de jornal. A lista do registro de ativos serve também como evidência depois. Os auditores podem casar cada carga do arquivo de escopo com a lista assinada do registro, de modo que qualquer host acrescentado depois se destaca.

### 1.8 Aritmética de conjuntos resolvida

Dada a VLAN V e as exclusões E, Sam calcula V\E e depois faz a interseção com a lista proposta do dia, P. Só P∩(V\E) pode ser carregado. Ele testa a calculadora com o SWIFT dentro de V e confirma que ele nunca aparece na saída. Um segundo teste coloca em P um endereço fora de V e confirma que ele também é rejeitado. Juntos, os dois testes cobrem as duas formas pelas quais o escopo falha: hosts excluídos vazando de volta e hosts fora da faixa chegando numa planilha amigável. A saída da calculadora é salva com a data, para que a lista carregada no dia possa ser reproduzida depois.

### 1.9 Filtrando uma planilha de agência

Na segunda-feira, Sam recebe de um líder de TI de agência uma planilha de "hosts interessantes". Ele não a importa. Ele reconstrói o escopo a partir das ROE assinadas: a /26, menos o SWIFT em .20, em interseção com os hosts que têm dono no registro de ativos. Três linhas da planilha somem por estarem fora do escopo; uma some por estar excluída. Ele devolve a lista filtrada com a expressão de conjuntos no e-mail. O líder da agência fica irritado por dez minutos e agradecido quando uma quarta linha é reconhecida como um console de pagamento digitado errado. A aritmética de conjuntos no papel escala melhor que a confiança.

### Exemplo resolvido (TRB sintético)

Sam escreve ESCOPO = 198.51.100.0/26 menos {198.51.100.20}. Um host proposto, 198.51.100.70, falha no teste de pertinência; ele o rejeita antes da reunião de abertura.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX001 — Diferença de conjuntos.** Expresse como operação de conjuntos o escopo da VLAN web do TRB com o SWIFT excluído. *Rubrica:* 3 = conjunto da VLAN menos {SWIFT}; 2 = parcial; 1 = união; 0 = nada.
- **EX002 — Necessário vs suficiente.** Por que "host dentro do escopo" não basta para rodar password spraying? *Rubrica:* 3 = o método também precisa ser permitido; o spraying pode ser proibido; 2 = parcial; 1 = basta; 0 = nada.
- **EX003 — Fração de cobertura.** 28 de 40 hosts tocados — escreva a cobertura e um mau uso de "70%". *Rubrica:* 3 = 28/40=0,7; mau uso, p. ex., sugerir segurança; 2 = só a fração; 1 = errado; 0 = nada.

### Síntese

Escopo é pertinência a um conjunto; métodos precisam de sua própria verdade; cobertura precisa de denominadores.

### Continue estudando — capítulo 01 de 40

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) mapear as camadas computacionais do TRB; (2) posicionar a plataforma de avaliação; (3) explicar por que os hosts do razão contábil diferem dos hosts web.

### 2.1 Camadas

As agências usam thin clients; os funcionários usam PCs gerenciados; as aplicações rodam em VMs; o razão contábil fica em hosts endurecidos, com controle de mudanças medido em semanas. Testadores que tratam todo host como uma VM de laboratório causam indisponibilidades. Uma taxa de varredura inofensiva contra uma VM de teste pode esgotar um host do razão cuja janela de mudança está a semanas de distância. Por isso, Sam registra a camada de cada host no arquivo de escopo, e o TrackScope aplica limites mais rígidos à camada do razão do que aos hosts web. Os thin clients acrescentam pouca superfície de ataque, mas muita dependência.

### 2.2 Plataforma de avaliação

TrackScope (verificador de escopo), FindingsDesk (tickets) e PulseMap (cobertura ATT&CK) são a plataforma sintética do TRB que Sam ajuda a construir. Elas rodam em infraestrutura isolada e precisam falhar fechadas quanto ao escopo. Falhar fechada significa que, quando o TrackScope não consegue carregar seu arquivo de escopo, ele nega todas as requisições em vez de permitir todas. Sam trata isso como a propriedade mais importante da plataforma: uma queda do painel é um incômodo, mas um verificador de escopo que permite por padrão poderia enviar tráfego de teste a hosts vizinhos do SWIFT. O FindingsDesk e o PulseMap herdam a mesma regra.

### 2.3 Fronteiras de confiança

Internet para a camada web, camada web para a API central, jump hosts para a administração vizinha do razão — cada travessia é um lugar onde aparecem achados. Em cada travessia, Sam pergunta em que a camada seguinte confia a respeito da anterior. A camada web confia que as requisições da internet são anônimas; a API central confia que as chamadas da camada web já estão autenticadas; a administração vizinha do razão confia que o jump host verificou o operador. Um achado costuma ficar onde uma dessas premissas é falsa; por isso, os cartões de método de Sam são organizados por fronteira, e não por ferramenta, e cada cartão nomeia a premissa de confiança que testa.

### 2.4 Fragilidade

Os sistemas do razão e os vizinhos do SWIFT geralmente ficam fora do escopo de pentest comum ou são condicionados a controles extremos. O NIST SP 800-115 continua valendo para o planejamento mesmo quando a intensidade técnica é baixa. Para o TRB, isso significa que as ROE podem permitir perto do razão apenas revisão de documentos e leitura de configuração, sem nenhuma varredura ativa. O planejamento ainda cobre quem aprova, que evidências são coletadas e como uma parada é acionada. Baixa intensidade não significa baixo rigor; significa que o rigor se desloca para a preparação e a revisão.

### 2.5 Deriva do inventário

Projetos de nuvem acrescentam tenants mais depressa do que os diagramas são atualizados. Testes autorizados contra diagramas desatualizados são um achado de processo. Quando um novo tenant de nuvem aparece nos dados de faturamento, mas não no diagrama usado para escrever as ROE, o escopo já está desatualizado. Sam relata isso como um achado de processo por si só: o banco não pode proteger, nem autorizar testes de, sistemas que não registrou. Ele compara o registro de ativos com as exportações de faturamento todo mês e envia as diferenças ao dono das ROE antes que a próxima janela se abra.

### 2.6 Regra prática

Sam nunca presume a camada de um host só pelo nome; ele confere o registro de ativos. Um host chamado web-test-03 pode, na verdade, estar na camada do razão depois de uma migração, e um host chamado ledger-legacy pode ter sido desativado. Só o registro, com o dono e a camada nomeados, decide como o TrackScope trata um host. Quando o registro e o nome discordam, Sam pergunta ao dono e registra a resposta antes de testar. Palpites baseados no nome são registrados como quase-acidentes quando detectados. A resposta do dono é copiada para os comentários do arquivo de escopo.

### 2.7 Nota aplicada

A regra de falha fechada do PulseMap é testada na CI apagando o arquivo de escopo e verificando que toda API retorna negação. Sam acrescentou esse teste depois que uma configuração errada em staging serviu brevemente listas de permissão vazias. Painéis que não conseguem negar são piores que nenhum painel. Ele demonstra o caminho de negação a todo estagiário novo na primeira semana. O teste de CI também cobre um arquivo corrompido, não só um ausente. Os dois caminhos precisam retornar negação em todos os endpoints, incluindo o health check, antes que o build possa passar.

### 2.8 Zoneamento da plataforma

TrackScope, FindingsDesk e PulseMap ficam numa zona de avaliação com conduítes controlados apenas para staging. Sam revisa esses conduítes a cada trimestre da mesma forma que revisa os fluxos de negócio do TRB — porque a plataforma pode ferir o banco se estiver mal ligada. Um conduíte da zona de avaliação para a produção deixaria um job mal configurado enviar tráfego a sistemas vivos; por isso, sua ausência é verificada, não presumida. Cada revisão registra quais conduítes existem, quem os aprovou e quando foram usados pela última vez. Conduítes sem uso são removidos em vez de ficarem abertos por conveniência.

### 2.9 Bug do denominador

Um bug do PulseMap certa vez fazia n assumir 1 por padrão. O teste de regressão de Sam define n=0 e espera um bloco de erro, não 100%. Com n igual a 1 por padrão, um único host tocado teria aparecido como 100% de cobertura, exatamente a porcentagem enganosa contra a qual o Capítulo 1 alerta. O teste de regressão agora roda em todo build, e o PulseMap se recusa a desenhar um bloco de cobertura sem um denominador explícito vindo do arquivo de escopo. Um bloco de erro é honesto; um número confiante construído sobre um valor padrão não é. A correção saiu com uma entrada no changelog que nomeia o bug.

### 2.10 Game day com o banco de dados fora do ar

Durante um game day da plataforma, Sam derruba o banco de dados do FindingsDesk. O TrackScope continua negando requisições fora do escopo usando seu cache local, enquanto enfileira rascunhos em disco. O PulseMap mostra um aviso de modo degradado. Nenhum tráfego de teste pode "falhar aberto" só porque um sistema de tickets caiu. A nota do game day vira um slide de vendas sobre por que ferramentas de avaliação são ferramentas de segurança. O próprio cache tem um limite de tempo, de modo que uma queda longa acaba negando tudo. Depois do exercício, a equipe anota por quanto tempo o cache pode ser confiável e quem decide quando ele expira.

### Exemplo resolvido (TRB sintético)

Sam coloca o PulseMap na VLAN de avaliação, e não numa imagem de PC de agência, para que um painel comprometido não consiga emitir arquivos de escopo.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX004 — Sistemas frágeis.** Nomeie duas classes de sistemas do TRB que geralmente ficam fora do escopo de testes comum. *Rubrica:* 3 = razão contábil e vizinhos do SWIFT (ou similar); 2 = uma; 1 = site; 0 = nada.
- **EX005 — Falhar fechado.** O que o TrackScope deve fazer se o arquivo de escopo não carregar? *Rubrica:* 3 = negar testes / falhar fechado; 2 = parcial; 1 = permitir tudo; 0 = nada.
- **EX006 — Verificação de camada.** Como Sam confirma a camada de um host? *Rubrica:* 3 = registro de ativos / dono, não palpite pelo nome; 2 = parcial; 1 = palpite pelo nome; 0 = nada.

### Síntese

Camadas e um desenho de plataforma que falha fechado impedem que testes autorizados se tornem mudanças acidentais em produção.

### Continue estudando — capítulo 02 de 40

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever pequenas ferramentas em Python para evidências offline; (2) recusar padrões inseguros; (3) testar ferramentas com dados sintéticos.

### 3.1 Propósito

Sam automatiza verificações de pertinência ao escopo, verificação de hashes e classificação de achados — nunca exploração. Cada verificação automatizada substitui uma etapa manual que as pessoas pulam quando estão cansadas: este endereço está na /26 assinada, este arquivo de evidência ainda corresponde ao hash registrado, quais achados abertos ficam mais alto por severidade e ativo? Nenhum desses scripts envia tráfego a um alvo. Manter a automação do lado seguro dessa linha significa que um bug no código de Sam pode rotular errado um relatório, mas não consegue alcançar o razão contábil nem o SWIFT.

### 3.2 Padrões inseguros

Sem segredos fixos no código, sem verificação TLS desativada, sem chamadas de shell não sanitizadas a scanners, sem novas tentativas sem limite. Cada regra corresponde a uma falha real: uma chave fixa no código acaba num repositório, a verificação TLS desativada esconde uma interceptação, um nome de host passado a um shell pode carregar comandos extras, e um laço de novas tentativas sem limite pode transformar uma verificação educada numa inundação contra um host frágil. A lista de revisão de Sam nomeia esses quatro, para que os revisores os procurem primeiro, e a CI rejeita os dois que podem ser detectados automaticamente antes que qualquer humano leia o código.

### 3.3 Sintético primeiro

Toda ferramenta roda em endereços de faixas de documentação e em arquivos falsos antes de qualquer janela de engajamento. Faixas de documentação como 198.51.100.0/24 não roteiam para hosts reais, então um erro durante o desenvolvimento não alcança nada. Sam roda toda ferramenta nova primeiro contra o escopo sintético do TRB, incluindo a exclusão do SWIFT em .20, e guarda as saídas como resultados esperados. Só quando essas saídas batem com as respostas calculadas à mão a ferramenta se torna elegível para uma janela de engajamento, e a aprovação cita a execução sintética pela data. Um pedido de aprovação sem uma execução sintética datada anexada é recusado, por mais urgente que seja a janela.

### 3.4 Revisão

Um segundo engenheiro lê os scripts de Sam em busca de erros no caminho do escopo. A primeira tarefa do revisor é rastrear todo caminho pelo qual um endereço entra no script e confirmar que ele passa pela verificação de pertinência do TrackScope antes do uso. Erros comuns incluem uma flag de depuração que pula a verificação, um segundo arquivo de entrada lido sem filtragem e uma lista de exclusões carregada depois dos alvos. O revisor assina a revisão no FindingsDesk, de modo que o registro mostra quem verificou qual versão e quando. Scripts não assinados não podem rodar numa janela.

### 3.5 Determinismo

Fixe a semente da aleatoriedade e as versões do interpretador para que as demonstrações do PulseMap sejam reproduzíveis. Uma demonstração do PulseMap que mostra números de cobertura diferentes em duas execuções não pode merecer a confiança de ninguém que esteja assistindo. Com uma semente fixa e uma versão de Python fixada, a mesma entrada sintética sempre produz os mesmos blocos, e um número alterado significa dados ou código alterados, não acaso. Sam registra a semente e a versão nas notas de cada demonstração, para que um revisor possa reproduzir depois exatamente a mesma tela e compará-la com a saída salva.

### 3.6 Laboratórios do curso

Os laboratórios deste livro seguem essas regras e incorporam saídas reais. Cada laboratório deste livro roda offline com a biblioteca padrão do Python 3, usa endereços de faixas de documentação e arquivos sintéticos e imprime uma saída capturada de uma execução real. Se a sua saída diferir da impressa, a diferença é informação: uma entrada alterada, um interpretador diferente ou um bug. Trate-a como Sam trata uma regressão do PulseMap, encontrando a causa antes de confiar em qualquer um dos resultados. Nenhum dos laboratórios precisa de acesso à rede, então eles podem rodar num notebook com a rede desligada.

### 3.7 Nota aplicada

A saída do dry-run é colada no canal do engajamento antes que qualquer modo de escrita rode. Os colegas têm dois minutos para objetar. Sam certa vez pegou um path traversal para dentro de um arquivo de evidências porque um colega leu o dry-run com cuidado. A revisão social vence a esperteza solitária em scripts operacionais. Dois minutos é curto o bastante para não atrasar uma janela e longo o bastante para um leitor cuidadoso. A saída colada lista todo endereço-alvo, o cartão de método e os caminhos de escrita que o script vai tocar, para que o leitor possa comparar cada linha com a /26 assinada e com a exclusão do SWIFT. A objeção de qualquer leitor pausa a execução até ser resolvida e anotada no log da janela.

### 3.8 Política de dados de teste

Clientes sintéticos nos fixtures usam documentos de identidade obviamente falsos. Sam rejeita fixtures que reutilizam números pessoais com aparência real, mesmo quando não são usados em produção. A transferência de hábito importa. Um fixture parecido com um número de identidade real pode ser copiado para um teste contra a produção por alguém com pressa. Valores obviamente falsos não podem ser confundidos com dados de clientes, e o hábito se estende a todo engajamento posterior. Um revisor que vê num fixture um número de identidade plausível pergunta de onde ele veio; um valor como FAKE-000-001 encerra a pergunta imediatamente e não pode ser confundido com um cliente durante um incidente.

### 3.9 Varredura de segredos na CI

Os repositórios da plataforma falham na CI se strings de alta entropia parecem chaves. Sam coloca na lista de permissão apenas fixtures de teste claramente marcados como FAKE. Uma chave de aparência real num arquivo de teste ainda treina as pessoas a ignorar o aviso; por isso, a marcação é obrigatória. Cada fixture permitido é listado com seu dono e o motivo pelo qual é seguro, e a lista é revisada sempre que as regras de CI mudam. Permitir pelo marcador, e não pelo caminho do arquivo, significa que uma chave real colada numa pasta de fixtures continua sendo pega. Quando a CI bloqueia um commit, o desenvolvedor rotaciona a string mesmo que ela só tenha existido localmente.

### 3.10 Quadro de trechos rejeitados

O quadro de revisão de scripts de Sam exibe três trechos rejeitados: uma chamada requests com verify=False, um subprocess com shell=True sobre um nome de host e um laço de novas tentativas sem jitter. Estagiários novos rubricam o quadro depois de lê-lo. O quadro é bobo e eficaz. Quando Sam quase cola verify=False "só em staging", ele vê as próprias iniciais e para. Cada trecho fica ao lado da versão segura: verify ligado com a CA interna do TRB, um subprocess chamado com uma lista de argumentos e um laço de novas tentativas com limite e backoff.

O quadro ganha um quarto exemplo sempre que a CI pega um novo antipadrão. Sam data cada trecho. Cada trecho novo traz uma nota de uma linha sobre o que a CI pegou e por que era perigoso, como uma nova tentativa sem limite contra um host lento. Pede-se aos estagiários que expliquem um trecho com as próprias palavras durante a primeira semana. A nota nomeia a regra, não a pessoa que escreveu o código. A equipe de Sam revisa o quadro todo ano e aposenta os trechos cuja regra de CI se tornou rotina.

### Exemplo resolvido (TRB sintético)

O lab_scope.py de Sam usa apenas o módulo ipaddress da biblioteca padrão e faixas de documentação; ele nunca abre um socket.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX007 — Regra do socket.** Por que o lab_scope não pode abrir sockets? *Rubrica:* 3 = apenas offline/sintético; nenhuma varredura acidental; 2 = parcial; 1 = sockets não têm problema; 0 = nada.
- **EX008 — Dois padrões inseguros.** Nomeie dois padrões de script proibidos na equipe da plataforma. *Rubrica:* 3 = dois entre segredos, TLS desligado, shell não sanitizado, novas tentativas sem limite; 2 = um; 1 = vago; 0 = nada.
- **EX009 — Segundo leitor.** O que o segundo leitor procura? *Rubrica:* 3 = erros no caminho do escopo e segredos; 2 = um; 1 = só estilo; 0 = nada.

### Síntese

Programar, aqui, significa automação segura, revisada e sintética primeiro.

### Continue estudando — capítulo 03 de 40

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) escrever achados sem culpabilização; (2) separar fatos de afirmações; (3) citar frameworks corretamente.

### 4.1 Achados sem culpa

"Conta de administrador compartilhada no sistema de empréstimos" é melhor que "administradores preguiçosos". Conselhos financiam correções; insultos criam inimigos. Um achado que nomeia uma fraqueza, sua localização e sua consequência dá ao dono algo para corrigir. Um achado que nomeia um grupo de pessoas dá a elas algo para defender. Sam escreve o achado da conta de administrador compartilhada com o sistema, a conta, o que os logs conseguem e não conseguem atribuir e uma mudança recomendada, e deixa os julgamentos de caráter totalmente de fora, porque o mesmo relatório será lido pelas pessoas que precisam fazer o trabalho.

### 4.2 Fato vs afirmação

Fato: a camada web abriu uma sessão TCP com o ledger-db. Afirmação: "atacantes podem movimentar dinheiro" precisa de mais evidência ou é rotulada como especulativa. A conexão em si é observada e registrada em log; a afirmação sobre movimentar dinheiro depende do que o ledger-db aceitaria dessa sessão, o que o teste não explorou. Sam escreve o fato no achado e, ou rotula a afirmação maior como especulativa, ou lista a evidência que seria necessária para sustentá-la. Os leitores podem então pesar cada frase pela sua evidência, e não pelo seu tom.

### 4.3 Citações

NIST SP 800-115, PTES, ATT&CK, OWASP WSTG, TIBER-EU e CBEST são citados com os títulos corretos. Nunca invente DOIs. Cada citação é conferida na página do editor antes que o relatório saia, e a edição ou versão importa: o SP 800-115 é citado como o guia técnico do NIST para testes e avaliações, não como uma regulação. Se Sam não consegue encontrar o identificador oficial de uma fonte, ele cita o título e a URL e não diz mais nada. Um DOI inventado minaria toda frase verdadeira perto dele.

### 4.4 Camadas de público

Executivos precisam de decisões; engenheiros precisam de reprodução; ambos precisam de honestidade sobre a incerteza. Para o achado da conta de administrador compartilhada, o CISO precisa da decisão (financiar contas nominais para o sistema de empréstimos), o engenheiro precisa do nome do sistema, da conta e da lacuna de logs, e ambos precisam do mesmo enunciado sobre o que não foi testado. Sam escreve o sumário executivo e o apêndice técnico a partir do mesmo registro de achado, para que eles não possam se distanciar. A incerteza, como os hosts não testados, entra nas duas partes com as mesmas palavras.

### 4.5 Estrutura

Sumário, escopo/métodos, achados, pontos positivos, limitações, apêndices. A ordem é deliberada. Um leitor que para depois do sumário ainda sabe qual decisão foi pedida; escopo e métodos dizem a todos o que foi e o que não foi testado antes que qualquer achado seja lido; os pontos positivos registram o que se manteve, como o SWIFT continuar inalcançável; as limitações impedem que o relatório seja lido como uma garantia. Os apêndices trazem os hashes, os IDs de tickets e os cartões de método que permitem a um engenheiro reproduzir cada etapa. Sam usa essa estrutura em todo relatório do TRB.

### 4.6 Revisão

A revisão por pares pega jargão e afirmações exageradas antes que o CISO veja o rascunho. O revisor de Sam lê procurando duas coisas: palavras que um não especialista não entenderia e frases que afirmam mais do que a evidência mostra, como "atacantes podem movimentar dinheiro" no lugar da conexão observada com o ledger-db. Cada comentário é respondido no histórico do rascunho, de modo que o relatório final mostra o que mudou e por quê antes que o CISO o receba. Comentários não resolvidos bloqueiam a liberação; os resolvidos continuam visíveis. O CISO recebe apenas a versão revisada, então rascunhos exagerados como "atacantes podem movimentar dinheiro" nunca chegam ao CISO.

### 4.7 Nota aplicada

Os exercícios de citação exigem abrir a página viva do NIST ou do PTES, não o resumo de um blog. Sam reprovou um rascunho inicial por citar uma paráfrase de segunda mão do SP 800-115 que inventava uma cláusula. Só fontes primárias — a mesma regra de nunca inventar DOIs. A página do NIST também mostra o status e a data do documento. Sam agora registra, ao lado de cada citação no rascunho, a data em que abriu a página primária e a seção em que se apoiou. Os revisores podem então conferir uma afirmação contra a mesma página, em vez de confiar na memória dele.

### 4.8 Passagem pelo público

Antes de enviar, Sam lê o sumário executivo em voz alta para alguém de fora da segurança. Se a pessoa não consegue reformular a decisão pedida, ele reescreve. Jargão que sobrevive a essa passagem é um defeito. A reformulação do ouvinte é anotada no histórico do rascunho para comparação posterior. No relatório da conta de administrador compartilhada, um ouvinte de finanças reformulou o pedido como "pagar por contas nominais no sistema de empréstimos", o que bateu. Um rascunho anterior tinha produzido "alguma coisa sobre senhas", o que o mandou de volta para reescrita. O ouvinte de finanças foi escolhido de propósito.

### 4.9 Auditoria da voz passiva

Achados que escondem os agentes na voz passiva são reescritos. "Senhas foram reutilizadas" vira "A conta de administrador de empréstimos usava a mesma senha da VPN", quando isso é conhecido. Nomear o sistema torna o achado acionável e testável. Quando o agente não é conhecido, a frase diz isso claramente, por exemplo "os logs não mostram qual administrador mudou a configuração". Isso mantém o achado honesto sem inventar um culpado e aponta direto para a lacuna de logs como uma segunda questão a corrigir. Corrigir o rascunho "os desenvolvedores ignoraram a segurança" exigiu apenas uma frase reescrita que nomeava o sistema e o log ausente.

### 4.10 Reescrevendo um achado acusatório

Um rascunho de achado certa vez dizia "os desenvolvedores ignoraram a segurança". O jurídico pediu reescrita antes do material do conselho. Sam produziu: "O serviço de empréstimos aceitava uma senha privilegiada compartilhada; os logs não conseguem atribuir mudanças a uma pessoa." Os mesmos fatos, num tom financiável. Ele guarda as duas versões nas notas de ensino para mostrar a diferença. A reescrita remove a acusação, mas mantém todos os fatos: uma senha privilegiada compartilhada e nenhuma atribuição nos logs. É por isso que ela sobreviveu à revisão jurídica e ainda disse aos donos do serviço de empréstimos exatamente o que mudar.

Os troféus de tom são adesivos bobos em achados impressos que os desenvolvedores elogiaram como claros. Sam prefere adesivos a métricas que ninguém lê. Cada adesivo registra qual achado foi elogiado e por quê, para que o próximo relatório possa copiar a clareza, e não apenas o adesivo. Clareza que os desenvolvedores notam é clareza que gera correções. Sam guarda os achados elogiados numa pasta como exemplos para estagiários. A contagem de achados fica em segundo plano nos relatórios de Sam, porque um achado claro que é corrigido importa mais que uma lista longa.

### Exemplo resolvido (TRB sintético)

Sam reescreve "a equipe web é incompetente" como "a camada web alcança o ledger-db por um fluxo não aprovado; controle: impor a matriz aprovada".

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX010 — Reescrita.** Transforme "reutilização estúpida de senhas" em linguagem profissional de achado. *Rubrica:* 3 = condição do sistema + impacto + nenhum insulto; 2 = parcial; 1 = mantém o insulto; 0 = nada.
- **EX011 — Afirmação especulativa.** Como Sam deve rotular "atacantes já roubaram fundos"? *Rubrica:* 3 = especulativa/não confirmada; separada dos fatos; 2 = parcial; 1 = como fato; 0 = nada.
- **EX012 — Regra de citação.** O que Sam nunca pode inventar ao citar? *Rubrica:* 3 = DOIs / referências falsas; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Uma escrita clara, citada e atenta ao público faz parte do ofício dos testes autorizados.

### Continue estudando — capítulo 04 de 40

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) situar os testes autorizados entre as práticas de segurança; (2) nomear a tríade CIA com exemplos do TRB; (3) recusar trabalho não autorizado.

### 5.1 Práticas vizinhas

Arquitetura, monitoramento, resposta a incidentes (IR) e testes autorizados se reforçam mutuamente. Testar sem logs é teatro; ter logs sem testar deixa passar o que nem se sabe que se desconhece. No TRB, um teste que alcança o ledger-db a partir da camada web só ajuda se a equipe de monitoramento puder mostrar se o viu e se os responsáveis por incidentes souberem o que fariam em seguida. Por isso, Sam envia cada achado à arquitetura para a correção de desenho, ao monitoramento como uma pergunta de detecção e à IR para uma verificação do playbook. Um achado que melhora as três vale muito mais do que um que só acrescenta uma linha a um relatório.

### 5.2 CIA no TRB

Confidencialidade dos dados de clientes; integridade dos razões e dos pagamentos; disponibilidade do internet banking. Os achados são julgados por qual delas ameaçam. A conexão da camada web com o ledger-db ameaça primeiro a integridade, porque o razão registra saldos e pagamentos; um modelo de extrato vazado ameaça a confidencialidade; uma varredura que deixa o internet banking lento ameaça a disponibilidade. Nomear a propriedade torna concretos os argumentos de severidade. Sam acrescenta a propriedade ameaçada como um campo em todo ticket do FindingsDesk, para que os donos vejam de relance qual promessa aos clientes está em risco e os conselhos possam contar os achados por propriedade, e não por ferramenta.

### 5.3 Permissão

ROE escritas pelos donos. Bug bounties cobrem apenas o escopo publicado. Bancos de amigos nunca são alvos de prática. No TRB, as ROE são assinadas pelos donos dos sistemas da /26 e nomeiam exclusões como o SWIFT. Um bug bounty que cobre o site público não cobre a API interna por trás dele, e a oferta de um amigo para "deixar você tentar" no sistema de outro banco não concede nada, porque o amigo não é dono desse sistema. Sam mantém uma cópia das ROE assinadas aberta durante toda janela e para se um alvo não puder ser rastreado até elas.

### 5.4 Uso dual

Este currículo ensina escopo, medição e relato — não código de exploit para produtos reais. O mesmo conhecimento que ajuda os defensores pode ajudar os atacantes; por isso, o curso traça sua linha nos artefatos: ensina a planejar, medir e relatar testes autorizados e como as técnicas são nomeadas para detecção, mas nunca fornece código de exploit funcional para produtos reais. Os laboratórios de Sam seguem a mesma regra. Quem termina o curso consegue definir o escopo de um engajamento no TRB e classificar seus achados, mas não tem nada que possa ser apontado para o banco de outra pessoa.

### 5.5 Mapa de frameworks

SP 800-115 (planejamento), PTES (etapas), WSTG (web), ATT&CK (técnicas), TIBER-EU/CBEST (setor financeiro orientado por ameaças). Cada framework responde a uma pergunta diferente. O SP 800-115 diz a Sam como planejar e conduzir uma avaliação; o PTES descreve as etapas, do pré-engajamento ao relatório; o WSTG traz casos de teste para aplicações web como o internet banking; o ATT&CK nomeia técnicas para que os achados possam ser ligados à detecção; TIBER-EU e CBEST descrevem red teaming orientado por inteligência para instituições financeiras sob supervisão regulatória. Usar um framework onde cabe outro, como tratar o CBEST como uma lista de verificação web, produz planos confusos.

### 5.6 Ética

O dano ao cliente e a integridade dos pagamentos estão acima da curiosidade e das capturas de tela para o currículo. Na prática, essa ordem decide escolhas reais. Se um teste puder corromper um registro de pagamento, ele para, por mais interessante que fosse o resultado. Se uma captura de tela mostrar dados de clientes, ela não é feita, nem para um portfólio. Sam escreve o impacto esperado no cliente de cada cartão de método antes de uma janela, e qualquer cartão com possível impacto na integridade dos pagamentos precisa da aprovação nominal do dono do razão. A curiosidade é satisfeita no laboratório sintético, onde nada real pode ser prejudicado.

### 5.7 Nota aplicada

O roteiro de recusa é ensaiado numa encenação em que um funcionário faz o papel de um diretor impaciente. Sam precisa manter o tom respeitoso sem ceder. As revisões em vídeo mostram se ele sorri nervosamente até concordar; esses clipes são apagados depois da orientação, mas a lição fica. Na encenação, o diretor pede a Sam que "só dê uma olhada rápida" num host fora da /26. O roteiro de Sam nomeia a cláusula das ROE, oferece levar uma mudança de escopo ao dono e dá um prazo realista para a aprovação. Praticar as palavras exatas as torna disponíveis sob pressão real.

### 5.8 Flashcards de frameworks

O baralho de Sam tem um cartão por framework: SP 800-115, PTES, WSTG, ATT&CK, TIBER-EU, CBEST — propósito e o que ele não é. Usar o CBEST como lista de verificação web é uma resposta comum no verso dos cartões. O cartão do TIBER-EU, por exemplo, diz que ele enquadra red teaming orientado por inteligência de ameaças para entidades financeiras e não é um padrão de varredura de vulnerabilidades. Escrever o lado "o que não é" obriga Sam a entender o propósito de cada framework, e não o seu nome, e o baralho é revisado sempre que um framework publica uma nova versão.

### 5.9 Fronteira do laboratório doméstico

O laboratório doméstico de Sam usa RFC1918 e nunca o DNS do TRB. Misturar a VPN com o dever de casa é um quase-acidente relatado, se acontecer. As faixas privadas RFC1918 em casa não podem colidir com o endereçamento do TRB se Sam nunca conectar a VPN do banco enquanto experimenta. Usar o DNS do TRB em casa vazaria nomes internos e poderia mandar tráfego do laboratório para o banco. Se houver uma confusão, ele a relata como quase-acidente, para que a regra de fronteira possa ser melhorada, em vez de torcer em silêncio para que ninguém tenha notado.

### 5.10 Recusando uma demonstração de invasão

Sam recusa um convite de meetup para demonstrar "como hackeamos nosso banco", embora o trabalho tenha sido autorizado. Capturas de tela viajam. Em vez disso, ele oferece uma palestra sobre desenho de ROE com exemplos sintéticos. Os organizadores aceitam. A contenção diante do uso dual inclui o que você se recusa a apresentar. Uma captura de tela de um achado autorizado do TRB ainda mostra nomes de host reais, versões e fraquezas que talvez ainda não tenham sido corrigidas. Depois de exibida na tela de um meetup, ela não pode ser retirada. A palestra sobre ROE compartilha a lição reutilizável sem os detalhes do banco.

A palestra sobre ROE usa apenas demonstrações com faixas de documentação. Os slides de Sam são públicos; suas capturas de tela do TRB não são. Faixas de documentação como 198.51.100.0/24 tornam impossível que uma demonstração aponte para um host real, e achados sintéticos não carregam nenhuma informação sobre os sistemas do TRB. Antes de publicar, Sam confere cada slide em busca de nomes internos, IDs de tickets e endereços reais. Suas capturas de tela do TRB ficam dentro do FindingsDesk, onde o acesso é controlado e registrado, e são apagadas quando termina o período de retenção do engajamento. O deck público é revisado uma vez pelo dono das ROE antes da publicação.

### Exemplo resolvido (TRB sintético)

Um colega pede a Sam que "teste o login do banco de casa". Sam recusa e aponta para a fronteira do curso.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX013 — Correspondência CIA.** Associe: extratos vazados; transferência alterada; banco fora do ar. *Rubrica:* 3 = C, I, A; 2 = duas; 1 = uma; 0 = nada.
- **EX014 — Recusar.** Por que recusar testar o login do banco de um amigo? *Rubrica:* 3 = não há autorização; ilegal/danoso; 2 = parcial; 1 = tudo bem se tiver cuidado; 0 = nada.
- **EX015 — Uso dual.** O que este curso se recusa a fornecer? *Rubrica:* 3 = código de exploit / procedimentos de ataque para sistemas reais; 2 = parcial; 1 = ajuda com escopo; 0 = nada.

### Síntese

Letramento é CIA, permissão, frameworks e recusa ética.

### Continue estudando — capítulo 05 de 40

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) modelar o acesso como grafos; (2) usar relações para matrizes de fluxo; (3) aplicar árvores às decisões de parada.

### 6.1 Grafos de acesso

Os nós são principais e sistemas; as arestas são "pode autenticar" ou "pode alcançar". Um caminho da Internet até o ledger-db que contorna os jump hosts é um candidato a achado. No TRB, o grafo pode mostrar a internet alcançando a camada web, a camada web alcançando a API central e o jump host alcançando a administração vizinha do razão. Uma aresta extra da camada web diretamente para o ledger-db cria um caminho que pula o jump host, e esse caminho é o achado, tenha ou não algum host isolado uma vulnerabilidade conhecida. Sam desenha apenas arestas sustentadas pelo inventário ou por evidência de varredura autorizada, para que cada caminho possa ser defendido.

### 6.2 Relações de fluxo

Os fluxos aprovados são uma relação R ⊆ Src × Dst. Os fluxos observados devem ser subconjuntos de R quando a matriz é imposta. Para o TRB, R pode incluir (camada web, API central) e (jump host, administração do razão), mas não (camada web, ledger-db). Se os fluxos observados incluem um par fora de R, ou a matriz não está sendo imposta, ou R está incompleta. O laboratório de Sam compara os dois conjuntos e lista as diferenças, e cada diferença vira uma pergunta para o dono da rede, e não um achado automático, porque um fluxo aprovado, mas não documentado, é uma correção de documentação.

### 6.3 Árvores de decisão

Árvores de parada: se o dono pede parada → interromper; senão, se houver indisponibilidade inexplicada → interromper; senão, continuar sob as ROE. Escrever a árvore antes de uma janela elimina a discussão durante ela. Se o dono do sistema de empréstimos diz pare, Sam interrompe na hora, sem perguntar por quê. Se uma indisponibilidade inexplicada aparece em qualquer host dentro do escopo, ele interrompe e relata, mesmo que a indisponibilidade talvez não tenha relação. Só quando nenhuma das condições vale o teste continua, e continuar ainda exige que o método seja permitido pelas ROE. Cada passagem pela árvore de parada é registrada com o horário e o resultado, para que o log da janela mostre por que o teste continuou ou parou.

### 6.4 Equivalência

Hosts da mesma classe de endurecimento podem compartilhar cartões de método — mas só se as ROE os agruparem. Se as ROE do TRB agrupam dez servidores web numa única classe de endurecimento, Sam pode aplicar os mesmos cartões de método aos dez e relatar os resultados por classe. Se as ROE os listam separadamente, talvez porque dois hospedam páginas de pagamento, ele precisa tratar cada um como distinto. A equivalência é uma decisão que o dono toma por escrito, não um atalho que o testador presume porque dois hosts parecem iguais vistos de fora.

### 6.5 Ordenação

A classificação de severidade usa pontuações ordenadas; os empates são desfeitos pelo id do achado, para haver determinismo (lab_rank). Sem um critério de desempate fixo, dois achados com a mesma pontuação poderiam trocar de lugar entre execuções, e o material do conselho mostraria um item diferente no topo a cada vez que fosse regenerado. Desempatar pelo ID do achado faz o lab_rank produzir a mesma ordem a partir dos mesmos dados, de modo que uma mudança na classificação sempre significa uma mudança nas pontuações. Sam registra o esquema de pontuação no relatório para que os leitores saibam o que a ordem significa.

### 6.6 Limites

Os grafos omitem a engenharia social, a menos que as ROE a incluam. Um grafo de arestas de rede e de autenticação não diz nada sobre um funcionário de agência que poderia ser convencido por telefone a aprovar um pagamento. Se as ROE excluem a engenharia social, Sam declara que o grafo cobre apenas caminhos técnicos, para que o conselho não leia "nenhum caminho encontrado" como "nenhuma forma de entrar". A limitação fica no mesmo slide do grafo, em palavras simples. A engenharia social, se autorizada depois, acrescentaria novas arestas ao mesmo grafo.

### 6.7 Nota aplicada

Os grafos de alcançabilidade anotam as arestas com "autenticada" ou "só de rede". Uma aresta só de rede para hosts vizinhos do razão eleva a severidade mesmo sem credenciais, porque um roubo de credenciais em outro lugar completa o caminho. Os primeiros grafos de Sam não tinham essa anotação e subclassificaram um achado. Depois da correção, toda aresta para um nó vizinho dos pagamentos traz sua anotação, e o lab_rank dá mais peso às arestas só de rede para a camada do razão. O achado antes subclassificado foi repontuado e reenviado com uma nota explicando a mudança, para que os leitores da primeira versão não ficassem com a classificação mais baixa.

### 6.8 Conjuntos de corte

Para os nós vizinhos dos pagamentos, Sam procura conjuntos de corte de arestas cuja remoção os isolaria da Internet. Essas arestas se tornam prioridades de monitoramento e controle mesmo quando não são "vulneráveis" no sentido de um scanner. Para o ledger-db, o conjunto de corte acabou sendo de duas arestas: a conexão direta da camada web e o acesso administrativo que contornava o jump host. Remover essas duas isola o razão dos caminhos voltados para a internet. Monitorá-las custa muito menos do que vigiar todo host. Essas duas arestas são também as que o F3 e a regra do jump host tratam.

### 6.9 Evidência das arestas

Cada aresta crítica do grafo cita a fonte de inventário ou de varredura sob as ROE. Arestas sem fonte são removidas. Uma fonte pode ser uma entrada do registro de ativos, uma exportação de regras de firewall ou um resultado de varredura autorizada com sua data. Uma aresta desenhada de memória ou por suposição não pode ser verificada; por isso, não pode sustentar um achado, e deixá-la faria o grafo inteiro parecer mais certo do que é. Quando falta uma fonte, Sam pergunta ao dono e só devolve a aresta ao grafo com evidência.

### 6.10 Encontrando o conjunto de corte

Ao traçar um caminho de um modelo de PC de agência comprometido até o ledger-db, Sam encontra quatro arestas. Remover a aresta web→razão (F3) e exigir o jump host para a administração corta os caminhos perigosos restantes. O grafo não precisava de cinquenta nós — precisava do conjunto de corte. Mostrar quatro arestas e o conjunto de corte fez a discussão da correção levar minutos em vez de uma hora, porque os donos podiam ver exatamente quais duas mudanças importavam.

Os slides de conjunto de corte de Sam usam no máximo seis arestas. Ele apaga o resto na frente do público para ensinar foco. Um slide com cinquenta arestas esconde as duas que importam; um slide com seis torna o conjunto de corte visível para um executivo em segundos. Apagar as arestas ao vivo também mostra que as removidas eram contexto, não evidência. Sam mantém o grafo completo no apêndice, com fontes para cada aresta, para que os engenheiros ainda possam conferir seu raciocínio e nada fique escondido da revisão.

### Exemplo resolvido (TRB sintético)

Sam desenha web → ledger-db como uma aresta que não está em R; o lab_flows depois marca o mesmo par como UNAPPROVED.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX016 — Visão de relação.** O que um fluxo UNAPPROVED significa em termos de relação? *Rubrica:* 3 = par observado que não está na relação aprovada R; 2 = parcial; 1 = aprovado; 0 = nada.
- **EX017 — Encontrar caminhos.** Por que um caminho Internet→web→razão importa? *Rubrica:* 3 = travessias de fronteiras de confiança / alcançabilidade além da intenção; 2 = parcial; 1 = irrelevante; 0 = nada.
- **EX018 — Desempate.** Como o lab_rank desempata pontuações iguais? *Rubrica:* 3 = pelo id do achado; 2 = aleatório; 1 = tamanho do título; 0 = nada.

### Síntese

Grafos e relações tornam precisos os achados de arquitetura e de fluxo.

### Continue estudando — capítulo 06 de 40

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) ler portas e serviços com cuidado; (2) explicar os papéis do TLS; (3) evitar experimentos de protocolo em sistemas vivos do TRB.

### 7.1 Portas não são serviços

A porta 443 frequentemente significa HTTPS, mas pode não significar. Nomes do inventário e certificados importam. Um serviço na 443 do TRB pode ser o front-end do internet banking, um console administrativo ou uma API interna exposta por engano. Sam o identifica pelo registro de ativos, pelos nomes de sujeito do certificado e pela descrição do dono antes de escolher qualquer cartão de método. Tratar toda 443 como "o site" leva a decisões de escopo erradas, como testar um console administrativo sob regras escritas para o site público. A resposta do dono é registrada no arquivo de escopo ao lado da porta.

### 7.2 TLS

Protege a confidencialidade e a integridade em trânsito; não corrige uma autorização quebrada na aplicação. Uma sessão cifrada com o internet banking ainda permite que um cliente logado peça o extrato de outro cliente se a aplicação não verificar a titularidade. Por isso, Sam relata as fraquezas de TLS e as fraquezas de autorização como achados separados, com donos separados: a equipe de plataforma para certificados e configurações de protocolo, a equipe de aplicação para as verificações de acesso. Um bom TLS é necessário, mas não diz nada sobre o que o servidor faz depois que a requisição chega.

### 7.3 Experimentos perigosos

Enviar pacotes malformados à VLAN do razão para "ver o que acontece" está fora dos limites. Os hosts do razão são frágeis, estão sob controle de mudanças e ficam fora do escopo comum; por isso, uma reação não planejada, como uma queda ou uma transação travada, poderia afetar pagamentos reais. Mesmo onde as ROE permitem algum teste de rede, experimentos com pacotes malformados precisam de um cartão de método nomeado, de uma janela de manutenção e da aprovação explícita do dono. Sem isso, a ação certa é registrar a pergunta e levá-la ao dono do razão.

### 7.4 Faixas de documentação

Os laboratórios usam 198.51.100.0/24 e 203.0.113.0/24 para que os exemplos não possam atingir a Internet real. Essas faixas, reservadas para documentação, não são roteadas na internet pública; assim, um erro de digitação ou um exemplo copiado não envia nada a lugar real algum. O escopo sintético do TRB, 198.51.100.0/26 com o SWIFT em .20, as usa pelo mesmo motivo. Usar endereços de aparência real no material do curso cria o risco de um aluno colá-los numa ferramenta numa rede viva. A faixa 203.0.113.0/24 faz o papel do lado do atacante ou do parceiro nos exemplos. Se a impressão de um laboratório algum dia mostrar um endereço fora dessas faixas, trate isso como um defeito do material e relate-o.

### 7.5 Ética da captura

Capturas de pacotes precisam de cláusulas nas ROE; elas frequentemente contêm dados de clientes. Uma captura na camada web do TRB pode conter dados de sessão, números de conta ou conteúdos de extratos. As ROE precisam dizer quem pode capturar, em quais segmentos, por quanto tempo os arquivos são mantidos e como são apagados. Sem essa cláusula, Sam não captura nada, e ele prefere configurações e logs, porque respondem à maioria das perguntas com muito menos dados de clientes. Toda captura feita recebe hash, é armazenada no FindingsDesk e apagada no prazo.

### 7.6 ATT&CK

A T1190 Exploit Public-Facing Application descreve o abuso de serviços voltados para a internet — nomeada para o desenho de detecções, não como um tutorial. Ligar um achado à T1190 diz à equipe de monitoramento quais detecções verificar, como erros ou requisições incomuns no front-end do internet banking, sem descrever como a fraqueza foi acionada. Sam acrescenta o ID da técnica no FindingsDesk para que o PulseMap possa mostrar a cobertura por técnica, e o relatório nunca inclui passos. Os donos das detecções podem então testar suas regras contra requisições sintéticas em staging.

### 7.7 Nota aplicada

As cláusulas de captura das ROE especificam as horas de retenção e quem pode rodar o wireshark. O pedido padrão de Sam é "configurações e logs primeiro; pacotes só se esses falharem". A maioria dos achados web do TRB nunca precisa de pacotes; quando precisa, a cláusula já está escrita. Escrever a cláusula com antecedência significa que um pedido urgente de captura durante uma janela não leva a uma decisão improvisada sobre dados de clientes. A cláusula também nomeia quem apaga os arquivos quando as horas de retenção expiram. A pessoa nomeada confirma a exclusão no ticket da captura quando as horas de retenção expiram, para que ninguém presuma que os arquivos sumiram.

### 7.8 Humildade diante dos banners

Banners alimentam o inventário, não o teatro de severidade. Sam registra a exposição de versão como baixa, a menos que esteja associada a um caminho vulnerável alcançável sob as ROE — que este curso, ainda assim, não vai explorar no mundo real. Um banner que mostra uma versão antiga pode ter sido corrigido por um backport do fornecedor; por isso, a versão sozinha não prova uma fraqueza. Registrá-la como inventário permite aos donos planejar atualizações sem inflar um relatório com achados alarmantes, mas não verificados. Se uma fraqueza alcançável for confirmada depois sob as ROE, a severidade é repontuada com essa evidência.

### 7.9 Lint de faixas de documentação

Os exemplos na documentação passam por um lint que garante que os IPs sejam de faixas de documentação. O lint de Sam reprovou o rascunho de um post de blog que usava um endereço real do TRB; boa captura. O endereço real teria revelado parte do layout de rede do TRB e poderia ter convidado os leitores a sondá-lo. O lint roda em toda mudança de documentação e bloqueia a publicação até que o endereço seja substituído por um exemplo de faixa de documentação, como um da 198.51.100.0/24. O rascunho do blog foi corrigido e o endereço original foi relatado ao dono da rede.

### 7.10 Redirecionando um pedido de FIN scan

Um aluno pede para tentar uma varredura TCP FIN em staging "para o trabalho do curso". Sam mostra a lista de métodos proibidos das ROE e a página de fronteira do curso. Em vez disso, eles fazem um quiz offline de PCAP. A curiosidade é redirecionada, não envergonhada — e não é satisfeita em redes bancárias. O quiz usa capturas sintéticas, então o aluno ainda vê como os pacotes se parecem sem que nenhum tráfego toque uma rede do TRB. Sam também registra o pedido como nota de ensino, sem o nome do aluno, porque ele mostra onde a fronteira do curso precisa ser explicada mais cedo.

As respostas do quiz de PCAP nunca incluem bytes de payload de clientes reais. As capturas sintéticas são geradas com endereços de faixas de documentação e payloads inventados, de modo que nenhum dado de cliente pode vazar pelo material didático. As respostas descrevem cabeçalhos, tempos e padrões de fluxo, que é do que os alunos precisam para raciocinar sobre detecção. Sam regenera os arquivos do quiz quando o curso muda, em vez de editar capturas à mão, para que sua procedência fique clara. Cada arquivo regenerado recebe hash, e o hash é publicado com o quiz.

### Exemplo resolvido (TRB sintético)

O laboratório de escopo de Sam rejeita 203.0.113.9 como OUT OF SCOPE usando apenas aritmética local de IPs.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX019 — Limite do TLS.** O que o TLS não corrige? *Rubrica:* 3 = autorização / lógica da aplicação quebradas; 2 = parcial; 1 = tudo; 0 = nada.
- **EX020 — Faixas de documentação.** Por que usar 198.51.100.0/24 nos laboratórios? *Rubrica:* 3 = faixas reservadas/de documentação; exemplos seguros; 2 = parcial; 1 = TRB real; 0 = nada.
- **EX021 — Regra de captura.** Quando Sam pode fazer uma captura de pacotes? *Rubrica:* 3 = quando as ROE permitem; minimizar os dados; 2 = parcial; 1 = a qualquer momento; 0 = nada.

### Síntese

Letramento em protocolos sem experimentação ao vivo; capturas apenas sob as ROE.

### Continue estudando — capítulo 07 de 40

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar módulos para a plataforma; (2) validar entradas; (3) versionar APIs com cuidado.

### 8.1 Módulos

Carregador de escopo, esquema de achados, exportador de relatórios — cada um com testes e um README. Dividir a plataforma dessa forma permite que cada parte falhe e seja testada por conta própria. Os testes do carregador de escopo o alimentam com a /26 sintética com o SWIFT em .20 e verificam que a exclusão sobrevive a todo formato de entrada. Os testes do esquema de achados rejeitam registros sem campos obrigatórios. Os testes do exportador comparam os relatórios gerados com arquivos esperados salvos. Cada README declara o que o módulo faz, o que ele se recusa a fazer e quem revisa as mudanças nele.

### 8.2 Validar na escrita

O FindingsDesk rejeita tickets sem dono ou sem hash de evidência. Rejeitar tickets incompletos no momento da escrita é mais barato do que persegui-los depois. Um achado sem dono não tem ninguém para corrigi-lo, e um achado sem hash de evidência não pode ser conferido contra o arquivo que afirma descrever. A validação de Sam retorna uma mensagem que nomeia o campo ausente, para que um analista possa corrigir o ticket imediatamente em vez de adivinhar por que ele falhou. O FindingsDesk aplica a mesma regra de campos obrigatórios às importações em lote e às chamadas de API, de modo que nenhuma das vias pode criar um achado sem dono.

### 8.3 Versionamento de API

O PulseMap v2 acrescenta campos sem quebrar os consumidores da v1. Os consumidores existentes do PulseMap, como a exportação mensal para o conselho, leem campos da v1 e precisam continuar funcionando quando aparecem campos novos, como IDs de técnica por cartão de método. Acrescentar campos é seguro; renomeá-los ou removê-los é uma mudança incompatível que exige uma nova versão e um período de migração. Os testes de contrato de Sam rodam o consumidor da v1 contra o servidor da v2 em todo build, para que uma quebra acidental falhe na CI, e não no próximo material do conselho.

### 8.4 Atualizações parciais

Um PATCH não pode limpar campos obrigatórios por acidente. Um cliente que envia apenas uma severidade alterada não pode apagar o dono ou o hash de evidência por omissão. O FindingsDesk trata o PATCH como "alterar apenas estes campos" e roda novamente a validação sobre o registro mesclado, de modo que uma atualização parcial não consegue produzir um ticket que teria sido rejeitado na criação. Os testes de Sam enviam requisições PATCH com um campo de cada vez e confirmam que todos os outros campos obrigatórios sobrevivem inalterados. A mesma regra protege o hash de evidência durante edições em lote.

### 8.5 Importação em lote

A importação de achados por CSV faz primeiro um dry-run e limita o número de linhas. Um dry-run mostra o que a importação criaria, atualizaria ou rejeitaria, incluindo qualquer host fora do escopo do TRB, antes que qualquer coisa seja escrita. O limite de linhas restringe o dano que um arquivo errado pode causar, e a próxima nota aplicada mostra por que os dois limites existem. Só depois que um analista revisa o resumo do dry-run a importação real roda, e o resumo é anexado ao registro da importação. O resumo do dry-run lista cada linha rejeitada com seu motivo, como um host fora do escopo do TRB, para que o analista possa corrigir o arquivo.

### 8.6 Concorrência

O bloqueio otimista impede que dois analistas sobrescrevam silenciosamente o mesmo ticket. Cada ticket carrega um número de versão. Quando um analista salva, o FindingsDesk confere que a versão não mudou desde que o ticket foi aberto; se um colega salvou primeiro, o segundo salvamento é recusado e o analista vê as duas versões. Sem isso, a mudança de severidade de um analista poderia apagar silenciosamente a nova evidência de outro, e ninguém saberia qual visão do achado era a atual. O analista recusado mescla as duas versões à mão, e a mesclagem é registrada.

### 8.7 Nota aplicada

A importação em lote tem teto de 500 linhas e exige um segundo aprovador acima de 100. Sam viu um analista quase importar um dump de scanner que incluía hosts fora do escopo como "informativos". Tetos e aprovadores são chatos de propósito. Um host fora do escopo "informativo" ainda é evidência de que alguém testou fora das ROE; por isso, ele precisa de revisão, não de armazenamento silencioso. O segundo aprovador confere o resumo do dry-run contra o escopo assinado antes que importações maiores prossigam. O aprovador nunca é a pessoa que rodou a varredura, para que a verificação seja independente.

### 8.8 Exercícios de migração

As migrações de esquema rodam numa cópia, com checksums antes e depois. Sam registra a contagem de linhas. Uma migração que muda as contagens silenciosamente reprova no exercício. Checksums e contagens de linhas na cópia mostram se uma migração preservou todo achado e toda referência de evidência. Se as contagens diferem, a migração é corrigida e rodada de novo numa cópia nova; a produção nunca é usada como teste. Sam guarda os números de antes e depois com o script de migração, para que um revisor possa confirmar que o exercício passou.

### 8.9 Escritas idempotentes

As atualizações de tickets são idempotentes por id do achado. Entregas duplicadas vindas de redes instáveis não conseguem criar F1s duplicados. Como cada atualização é indexada pelo ID do achado, aplicar a mesma requisição duas vezes deixa o ticket no mesmo estado que aplicá-la uma vez. Isso importa no TRB, onde os links de VPN para a zona de avaliação caem com frequência, e achados duplicados inflariam as contagens nos relatórios ao conselho.

As atualizações idempotentes de tickets salvaram o TRB quando uma VPN instável reenviou doze vezes a mesma chamada de criação de achado. O FindingsDesk mostrou um F1, não doze. Sam acrescenta essa história ao onboarding para que os engenheiros parem de temer o "exatamente uma vez" como algo acadêmico. Doze tickets F1 duplicados teriam mostrado ao conselho doze achados críticos abertos e acionado o dono doze vezes. A idempotência tornou a falha de rede inofensiva, que é exatamente o que os engenheiros precisam ver antes de confiar no desenho. Os engenheiros novos agora testam as novas tentativas na primeira semana.

### 8.10 Dry-run da importação em lote

O dry-run da importação em lote do FindingsDesk certa vez revelou 40 hosts fora das ROE embutidos num CSV de scanner. A importação foi bloqueada. Na retrospectiva, Sam agradece mais ao dry-run do que a qualquer funcionalidade nova lançada naquele mês. Quarenta hosts fora do escopo num banco de dados de avaliação teriam parecido resultados de testes autorizados e poderiam ter motivado trabalho de acompanhamento contra sistemas que ninguém havia aprovado. O dry-run transformou um problema silencioso de dados numa decisão visível, e a configuração do scanner que produziu o CSV foi corrigida antes da janela seguinte.

### 8.11 Limiar de aprovação de 100 linhas

O limiar de aprovação de 100 linhas do FindingsDesk existe porque um dump de 2.000 linhas certa vez ficou na fila durante a noite e disparou uma tempestade de alertas para os donos. Sam documenta o id do incidente ao lado da constante no código. Ligar a constante ao registro do incidente diz aos futuros engenheiros por que o limiar existe antes que decidam aumentá-lo. Sem o comentário, 100 parece arbitrário e convida à remoção. Com ele, qualquer pessoa que mude o valor pode ler o que aconteceu quando importações grandes rodaram sem revisão e acionaram os donos a noite inteira. O comentário nomeia o ENG-441 e a data da mudança.

O id do incidente é ENG-441 no arquivo do curso. A entrada do arquivo descreve a fila noturna, quantos donos foram acionados e a mudança que introduziu o limiar de aprovação. Um revisor que encontra a constante pode seguir o link e julgar o histórico diretamente. A mesma prática vale para o teto de 500 linhas: todo limite de segurança do FindingsDesk aponta para o motivo pelo qual foi definido, de modo que os limites são mudados de forma deliberada, e não por alguém arrumando o código.

### Exemplo resolvido (TRB sintético)

Sam acrescenta uma verificação ao FindingsDesk: um emergency_contact vazio nos metadados das ROE bloqueia o início do engajamento.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX022 — Regra de rejeição.** Nomeie dois campos que devem bloquear a criação do ticket se estiverem vazios. *Rubrica:* 3 = dois entre dono, hash de evidência, severidade; 2 = um; 1 = cor do título; 0 = nada.
- **EX023 — Importação com dry-run.** Por que fazer dry-run de uma importação em lote? *Rubrica:* 3 = pegar erros de esquema antes da escrita; 2 = parcial; 1 = não precisa; 0 = nada.
- **EX024 — Bloqueio otimista.** Que problema o bloqueio otimista evita? *Rubrica:* 3 = sobrescrita silenciosa de edições concorrentes; 2 = parcial; 1 = interface lenta; 0 = nada.

### Síntese

O código da plataforma valida, versiona e se recusa a iniciar engajamentos inseguros.

### Continue estudando — capítulo 08 de 40

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) projetar esquemas mínimos para achados; (2) proteger dados de clientes em bancos de evidências; (3) reter e apagar no prazo.

### 9.1 Esquema mínimo

Armazene o que os retestes precisam, não tabelas inteiras de clientes. Um registro de achado no TRB precisa apenas do suficiente para reproduzir e verificar a fraqueza: o identificador do ativo afetado, a requisição ou a configuração que a demonstrou, um carimbo de tempo, o testador, o id do engajamento e um ponteiro para o arquivo de evidência. Quando Sam provou que um endpoint de download de extratos devolvia o PDF de outro cliente, o registro guardou os dois ids de conta sintéticos envolvidos e um hash da resposta, não o extrato em si. Um reteste no trimestre seguinte repete a mesma requisição e compara o resultado. Cada coluna extra copiada de uma tabela de clientes vira um dado que a equipe de testes agora precisa proteger, reter e, um dia, apagar.

### 9.2 Controle de acesso

Os bancos de evidências usam acesso baseado em papéis; o papel de estagiário de Sam tem leitura/escrita apenas nos esquemas do engajamento. Os papéis são concedidos por engajamento, não por pessoa, de modo que a permissão desaparece quando o engajamento é encerrado, e não quando alguém se lembra de revogá-la. O FindingsDesk tem três: testador (escreve achados e evidências de um engajamento), revisor (lê os engajamentos que aprova) e custodiante (roda as rotinas de retenção e restauração, nunca edita achados). Separar o custodiante do testador significa que quem apaga as evidências no prazo não é a pessoa cujo trabalho elas documentam. Quando um testador passa para um novo engajamento, seu papel antigo expira e o revisor mantém acesso de leitura até que o relatório seja aceito.

### 9.3 Retenção

Exclusões dirigidas pelo contrato; "guardar para sempre" não é uma política. A declaração de trabalho fixa um período de retenção para as evidências brutas, comumente noventa dias após o relatório final, e outro mais longo para o relatório e o status da remediação. O FindingsDesk armazena essa data na linha do engajamento no dia em que o contrato é assinado, e uma rotina noturna apaga os blobs de evidência cuja data já passou, gravando um recibo de exclusão com contagens e hashes. A retenção também protege o testador: evidência guardada além da data combinada são dados de clientes mantidos sem motivo, e um auditor vai perguntar por quê. Se um cliente pede uma retenção legal, ela é um campo datado com dono, não uma promessa informal.

### 9.4 Backups

Cifrados, com acesso registrado, com restaurações testadas — os backups estão no escopo da revisão de abuso. Um backup é uma segunda cópia de toda captura de tela, todo log de requisições e toda string com cara de credencial que a equipe já capturou; por isso, ele atrai as mesmas ameaças que o banco de dados vivo e costuma ser vigiado com menos cuidado. Os backups de evidências do TRB são cifrados com uma chave mantida pelo papel de custodiante, armazenados numa conta separada, e toda leitura é registrada. A retenção também se aplica aos backups: uma rotina de exclusão que limpa o armazenamento vivo, mas deixa intactos snapshots de noventa dias, não apagou nada. A revisão trimestral de Sam compara a data do snapshot mais antigo com o menor período de retenção de qualquer engajamento ativo.

### 9.5 Higiene de consultas

Nada de SELECT * para notebooks; exporte CSVs minimizados. Os analistas geralmente querem uma contagem, uma tendência ou um único exemplo, e a consulta deve devolver exatamente isso. Puxar tabelas inteiras para um notebook leva a evidência para fora dos controles que a protegem: sem log de acesso, sem rotina de retenção e com um disco que pode viajar. Por isso, o FindingsDesk expõe consultas salvas, como achados abertos por severidade ou dias até a correção por unidade de negócio, que devolvem agregados e colunas redigidas. Quando alguém precisa de uma linha bruta, abre-a dentro do visualizador de evidências, onde a leitura é registrada. Sam reescreveu uma consulta popular de painel que selecionava todas as colunas e reduziu a exportação de quarenta campos para seis.

### 9.6 Integridade

Chaves estrangeiras dos achados para os blobs de evidência. Um achado que aponta para um arquivo ausente ou alterado não pode ser defendido quando o cliente o contesta. Cada blob de evidência no FindingsDesk é armazenado com um hash SHA-256 calculado no upload, e a linha do achado referencia o blob por id com uma restrição de chave estrangeira, de modo que o banco de dados se recusa a apagar evidências que um achado vivo ainda cita. Quando um relatório sai, a exportação lista cada achado com os hashes de suas evidências. Se o TRB depois perguntar se uma captura de tela foi editada, Sam recalcula o hash e compara. Uma divergência é, ela mesma, um incidente a investigar, não um motivo para reenviar o arquivo em silêncio.

### 9.7 Revisão de acessos contra os registros de RH

Os papéis do banco de evidências são revisados trimestralmente contra as listas de RH. A consulta de Sam procura papéis ativos no cofre sem funcionários ativos. A primeira execução encontrou dois terceirizados; o acesso foi removido na mesma tarde. A junção é simples: papéis sem registro ativo correspondente na exportação do RH estão órfãos. Os casos interessantes são os quase-acertos. Um testador em licença parental está inativo no RH, mas deve manter uma conta dormente, e um terceirizado renovado sob uma nova ordem de compra pode aparecer com um id diferente. Por isso, a consulta de Sam produz uma lista de revisão, em vez de revogar o acesso automaticamente, e o líder de segurança assina cada decisão. A execução do segundo trimestre encontrou zero órfãos, que é o resultado que o controle existe para produzir.

### 9.8 Marcas d'água nas exportações

As exportações CSV embutem o id do engajamento e o nome de quem exportou num comentário de cabeçalho. Arquivos vazados podem ser rastreados. Sam verifica a existência da marca d'água numa checagem trimestral por amostragem. Uma marca d'água não impede um vazamento; ela encurta a investigação que vem depois de um. Quando um arquivo aparece num drive compartilhado, o cabeçalho nomeia o engajamento e a pessoa que o exportou, para que o custodiante possa verificar se aquela exportação foi autorizada e qual data de retenção se aplica. Comentários de cabeçalho são fáceis de remover; por isso, o log de exportações do FindingsDesk registra os mesmos campos junto com um hash do arquivo. Comparar o hash de um arquivo perdido com esse log identifica sua origem mesmo quando alguém apagou a linha de comentário.

### 9.9 Jogo de restauração de backup

A cada trimestre, Sam restaura um backup de evidências num host isolado e abre um arquivo. Backups não testados são presumidos quebrados. O exercício tem uma condição de aprovação escrita com antecedência: restaurar em até duas horas, abrir um arquivo de evidência escolhido ao acaso, recalcular seu hash e compará-lo com o registro do achado. O host isolado não tem rota de rede para a produção e é apagado depois, porque um backup restaurado está cheio de evidências sensíveis. O tempo importa tanto quanto o sucesso. Se o TRB contestar um achado durante a revisão de um relatório, a equipe precisa apresentar a evidência original naquela semana, não depois de um dia procurando a chave de decifração. Cada jogo termina com uma nota curta que registra a duração, os problemas e as correções.

### 9.10 Recusar uma exportação em massa

Um analista pede "todas as evidências do ano" para uma tese. Sam recusa a exportação em massa e oferece um extrato só de estatísticas, com contagens por severidade. A tese segue em frente. A minimização vale também para pedidos amigáveis. A recusa funciona porque Sam perguntou a que pergunta a tese tentava responder. O analista queria mostrar por quanto tempo os achados web de alta severidade ficavam abertos, o que exige datas e severidades, não capturas de tela nem ids de conta. Uma consulta agrupada por trimestre e severidade respondeu a isso, e o resultado não continha nenhum dado de cliente. O propósito vem primeiro: um pedido formulado como "todas as evidências" geralmente esconde uma necessidade mais estreita, e nomear essa necessidade transforma um conflito de privacidade numa tarefa de relatório.

### 9.11 Restauração sem manifesto

Durante o game day de restauração, o backup abriu, mas o manifesto de hashes estava ausente. Sam reprovou o jogo e restabeleceu a rotina do manifesto antes do engajamento seguinte. Backups sem manifestos são boatos. O arquivo abriu; por isso, um revisor menos cuidadoso teria aprovado o jogo. Sem o manifesto, porém, ninguém conseguiria provar que o arquivo restaurado correspondia ao que foi capturado durante os testes, e essa prova é a razão de ser da evidência. A causa foi banal: uma migração de armazenamento tinha descartado a rotina agendada que grava os manifestos ao lado de cada snapshot. Sam acrescentou uma verificação que faz o próprio backup falhar quando não há manifesto, de modo que a lacuna agora aparece na noite em que ocorre, em vez de no próximo jogo trimestral.

### 9.12 Um endereço de contato em toda exportação

Os cabeçalhos de marca d'água incluem um mailto de contato para achados e perdidos de exportações extraviadas. Alguém o usou uma vez; Sam lhe pagou um café. O endereço dá a quem encontra um arquivo, de boa-fé, uma forma de relatar uma exportação extraviada em vez de adivinhar quem é o dono. Ele vai para uma caixa compartilhada de custodiantes, não para uma pessoa, de modo que continua funcionando depois de trocas de equipe. Os relatos são tratados como um pequeno incidente. O custodiante confirma a origem do arquivo pelo log de exportações, pede a quem o encontrou que apague sua cópia ou a devolva e registra se a data de retenção já havia passado. Agradecer publicamente a quem relatou aumenta a chance de que o próximo arquivo extraviado também seja relatado.

### 9.13 Um pen drive devolvido

O mailto de achados e perdidos certa vez trouxe de volta um pen drive etiquetado com um id de engajamento. O processo funciona. O pen drive também mostrou onde o processo havia falhado antes: alguém tinha copiado evidências para mídia removível apesar das regras de exportação. O custodiante não simplesmente apagou o pen drive. Ele conferiu o conteúdo contra o log de exportações, encontrou uma cópia não registrada de capturas de tela de um engajamento encerrado meses antes e a rastreou até um testador que queria trabalhar offline num trem. A resposta foi uma conversa curta, a exclusão com recibo e uma nova opção no FindingsDesk para espaços de trabalho offline cifrados que expiram na data de retenção.

### Exemplo resolvido (TRB sintético)

A rotina de exportação de Sam redige os números de conta para os quatro últimos dígitos antes que os analistas baixem o CSV.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX025 — Minimalismo.** Por que não armazenar linhas completas de clientes com cada achado? *Rubrica:* 3 = privacidade/minimização/ROE; 2 = parcial; 1 = precisamos delas; 0 = nada.
- **EX026 — Retenção.** O que dispara a exclusão das evidências de um engajamento? *Rubrica:* 3 = cronograma do contrato / data de retenção; 2 = parcial; 1 = nunca; 0 = nada.
- **EX027 — Papel.** O que um papel de estagiário não deve acessar por padrão? *Rubrica:* 3 = engajamentos não relacionados / banco de clientes de produção; 2 = parcial; 1 = tudo; 0 = nada.

### Síntese

Os bancos de dados guardam o mínimo de dados pessoais necessário, com retenção e papéis impostos.

### Continue estudando — capítulo 09 de 40

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) listar o essencial das ROE; (2) verificar os alvos offline; (3) lidar com a pressão para exceder o escopo.

### 10.1 O essencial das ROE

Escopo, exclusões, métodos, janela, contatos de emergência, tratamento de dados, público do relatório — o NIST SP 800-115 e o PTES põem, ambos, a autorização em primeiro lugar. As regras de engajamento transformam uma permissão geral em instruções que um testador pode conferir antes de cada ação. No TRB, elas listam as redes e os nomes de host no escopo, nomeiam o gateway SWIFT e o razão contábil de produção como excluídos, permitem testes web autenticados, mas proíbem negação de serviço e engenharia social, e fixam os testes nas noites de dias úteis, entre 20:00 e 02:00. Elas também nomeiam quem atende o telefone se algo quebrar, como os dados capturados são armazenados e quem recebe o relatório. Uma regra que não está escrita não existe quando é necessária às 23:40.

### 10.2 Verificação offline

O lab_scope classifica os alvos propostos antes de qualquer pacote.

```python
"""Lab 10: check a synthetic TRB target list against written scope and exclusions (no traffic sent)."""
import ipaddress
scope = [ipaddress.ip_network("198.51.100.0/26")]
excluded = {ipaddress.ip_address("198.51.100.20")}  # SWIFT gateway, owner excluded
for t in ["198.51.100.5", "198.51.100.20", "198.51.100.70", "203.0.113.9"]:
    ip = ipaddress.ip_address(t)
    v = "EXCLUDED" if ip in excluded else "in scope" if any(ip in n for n in scope) else "OUT OF SCOPE"
    print(f"{t:15} {v}")
```

Execute com `python3 lab_scope.py`. Saída verificada:

```text
198.51.100.5    in scope
198.51.100.20   EXCLUDED
198.51.100.70   OUT OF SCOPE
203.0.113.9     OUT OF SCOPE
```

Rodar o classificador antes de qualquer tráfego transforma o escopo de algo de que o testador se lembra em algo que o testador pode mostrar. A lista de alvos propostos, a versão do arquivo de escopo e a saída são salvas juntas na pasta do engajamento. Se uma disputa posterior perguntar por que um host foi testado, a resposta é a saída salva, não uma lembrança. A verificação é estrita de propósito: um endereço fora de todas as faixas listadas é recusado, mesmo quando parece fazer parte do mesmo serviço, até que o arquivo de escopo seja alterado e assinado.

### 10.3 Pressão

"Só acrescente a caixa do SWIFT" é recusado até que a exclusão escrita mude — o que não acontecerá para testes comuns. A pressão raramente chega como uma ordem para quebrar regras. Ela vem como um atalho de aparência razoável, de alguém mais graduado, tarde numa janela, quando o host extra faria o relatório parecer mais completo. A resposta de Sam segue um roteiro: agradecer, explicar que o gateway está excluído nas regras assinadas e oferecer levar uma mudança de escopo ao dono dele para uma janela futura. A exclusão existe porque o dono do gateway não aceitou o risco operacional, e ninguém numa chamada de teste pode aceitá-lo por ele. Recusar com educação e por escrito protege tanto o testador quanto a pessoa que pediu.

### 10.4 Divulgação responsável

Bugs de fornecedores encontrados em software de terceiros seguem os canais do fornecedor apenas com aprovação do CISO. Uma falha num produto comercial que o TRB usa pertence em parte ao TRB e em parte a todos os outros clientes desse produto. Sam a registra no FindingsDesk como um achado do TRB com um controle compensatório e depois passa o detalhe técnico ao CISO, que decide se contata o fornecedor e sob qual prazo de divulgação. Contatar o fornecedor diretamente, ou publicar algo a respeito, poderia expor o TRB como um cliente sem correção antes que exista uma. O relato ao fornecedor traz detalhe suficiente para reproduzir o bug com segurança e nada sobre o ambiente mais amplo do TRB.

### 10.5 Conflitos

Sam não testa sistemas de empresas da família no horário nem com as ferramentas do TRB. Um conflito de interesses não precisa de má intenção para prejudicar um engajamento. Quem testa a empresa de um parente com o scanner do banco usa recursos do TRB fora da autoridade do TRB, e qualquer achado que produza fica exposto à acusação de ter sido distorcido por um motivo pessoal. O mesmo raciocínio vale dentro do banco: um testador cujo amigo é dono da aplicação em revisão deve declarar isso antes da definição do escopo. Declarar um conflito cedo custa um e-mail e, talvez, uma redesignação. Declará-lo depois que o relatório saiu pode custar a credibilidade de todos os achados nele.

### 10.6 Ensino de uso dual

Detalhes de exploit para produtos de pagamento reais estão fora do escopo do currículo. As habilidades deste livro podem ser mal usadas; por isso, o livro traça uma linha no que ensina em detalhe. Ele explica classes de fraquezas, como testadores autorizados as confirmam com segurança e como relatá-las, usando sistemas sintéticos. Ele não dá cadeias de exploit funcionais para terminais de cartão, switches de pagamento ou plataformas bancárias reais, porque esse material ajuda mais um atacante do que um aluno. Um estudante que queira ir além o faz num laboratório sancionado, sob supervisão. O teste de qualquer exemplo didático é se um defensor aprende mais com ele do que um atacante ganha.

### 10.7 Nenhum código de exploit no sistema de achados

Os exemplos da política de uso dual incluem recusar colar PoCs de exploit no FindingsDesk mesmo quando um fornecedor pede "para reprodução". A reprodução no TRB usa evidências de configuração e contas autorizadas, não trechos transformados em arma. O FindingsDesk é lido por desenvolvedores, auditores e gestores, e suas exportações chegam aos fornecedores. Uma prova de conceito funcional armazenada ali se espalharia para todos esses leitores. Em vez disso, os achados de Sam mostram as condições: a configuração errada, a requisição que uma conta de teste autorizada enviou e a resposta que provou a fraqueza. Um desenvolvedor pode confirmar o problema num ambiente de teste a partir dessa descrição. Quando um fornecedor insiste em mais, o CISO decide o que compartilhar e por qual canal seguro.

### 10.8 Registro de brindes e conflitos

Sam registra quaisquer brindes de fornecedores ou contas em outros bancos que possam enviesar decisões de escopo. A transparência é mais barata que brigas por impedimento no meio de um engajamento. O registro é uma tabela curta e datada: o que foi recebido ou mantido, de quem e quais engajamentos isso pode tocar. Coisas pequenas contam porque mostram um padrão. Um ingresso de conferência dado por um fornecedor de scanner importa se Sam depois recomendar o produto desse fornecedor num relatório. O líder de segurança revisa o registro antes de designar os testadores, o que resolve os impedimentos na fase de planejamento, quando trocar um testador é fácil. Uma entrada não é uma acusação; um brinde não registrado descoberto depois é tratado como uma.

### 10.9 Simulação de mesa sobre as regras de engajamento

Uma simulação de mesa anual percorre um cenário de contato de emergência ausente. A equipe de Sam pratica adiar em vez de improvisar. Uma simulação de mesa custa uma hora e nenhum pacote. O facilitador lê uma situação em voz alta: um teste está para começar e o contato de emergência nomeado não atende. Cada participante diz o que faria e qual regra lhe diz isso. O resultado útil são as lacunas que ela expõe. Num ano, a equipe descobriu que as regras nomeavam um contato que tinha mudado de função três meses antes. Atualizar esse nome antes da janela seguinte foi o resultado mais valioso da sessão.

### 10.10 Adiar quando o contato está inalcançável

Simulação de mesa: contato de emergência inalcançável. A equipe de Sam adia a janela por escrito em até cinco minutos. Uma aprovação verbal improvisada de um gestor qualquer é pontuada como condição de reprovação na simulação. Adiar é sucesso. O instinto de seguir em frente vem do custo de reagendar, mas continuar sem um contato alcançável significa que, se um serviço se degradar, ninguém com autoridade poderá dizer aos testadores que parem. Um gestor que por acaso está online pode ter boa intenção, mas não está nomeado nas regras e não pode aceitar o risco. O adiamento escrito registra o horário, as tentativas de alcançar o contato e a próxima janela proposta, de modo que o atraso fica documentado, e não atribuído como culpa.

### 10.11 Impedimento diante do fornecedor de um parente

O registro de conflitos de Sam certa vez listava um irmão que trabalhava num fornecedor fintech. Ele se declarou impedido num teste que envolvia a biblioteca desse fornecedor. O impedimento é mais silencioso que o escândalo. A biblioteca era uma parte pequena do engajamento, o que tornava tentador ficar e apenas pular aquele componente. O líder de segurança preferiu uma separação limpa. Outro testador assumiu todos os achados que tocavam a biblioteca, e o nome de Sam ficou fora desses registros. Se o teste tivesse encontrado uma falha grave, o fornecedor não poderia alegar que um parente a havia exagerado ou suavizado. A entrada no registro, escrita meses antes, fez da decisão uma tarefa de dois minutos, e não uma discussão.

### 10.12 Modelos de adiamento

Os modelos de adiamento incluem os aliases do SOC e do CISO já preenchidos. Sam envia adiamentos em menos de três minutos durante os exercícios. Um modelo remove decisões de um momento estressante. Ele já lista o id do engajamento, os destinatários que precisam saber (o SOC, para que não saia à caça de testadores que já não estão testando, e o gabinete do CISO) e campos para o motivo, as tentativas feitas e uma nova janela proposta. O testador preenche fatos, não redação. Aliases preenchidos importam porque nomes individuais ficam desatualizados, enquanto os endereços de função são mantidos pelas equipes que são donas deles.

### 10.13 Cronometrar o exercício de adiamento

O exercício de adiamento de três minutos é cronometrado com um relógio visível. Passar de três minutos reprova no exercício. O limite não é arbitrário. O SOC do TRB escala varreduras inexplicadas depois de cinco minutos; assim, um adiamento enviado em até três chega aos analistas antes que eles abram um incidente por uma atividade que já parou. Um relógio visível também mostra para onde vai o tempo. Nos primeiros exercícios, a maior parte dele ia em encontrar o modelo, o que levou a um link fixado no canal do engajamento. Os exercícios são pontuados por a mensagem ter chegado, ter ido para as funções certas e estar correta, não só pela velocidade.

### Exemplo resolvido (TRB sintético)

O lab_scope marca 198.51.100.20 como EXCLUDED e 198.51.100.70 como OUT OF SCOPE; Sam remove os dois do plano.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX028 — Linha excluída.** O que o laboratório imprime para 198.51.100.20? *Rubrica:* 3 = EXCLUDED; 2 = fora do escopo; 1 = dentro do escopo; 0 = nada.
- **EX029 — Resposta à pressão.** Como Sam responde a "acrescente o SWIFT só desta vez"? *Rubrica:* 3 = recusa até uma mudança escrita nas ROE; o SWIFT continua excluído; 2 = recusa; 1 = concorda; 0 = nada.
- **EX030 — Lista das ROE.** Nomeie cinco itens essenciais das ROE. *Rubrica:* 3 = cinco entre escopo, exclusões, métodos, janela, contatos, dados, público; 2 = três; 1 = um; 0 = nada.

### Síntese

A ética é operacionalizada como listas de verificação, recusas e matemática de escopo offline.

### Continue estudando — capítulo 10 de 40

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) comparar superfícies administrativas; (2) exigir jump hosts; (3) tratar imagens como parte do escopo quando acordado.

### 11.1 Superfícies

Níveis de correção, administradores locais e serviços remotos diferem entre Windows e Linux. Os achados nomeiam o sistema operacional e o controle que falhou. Num servidor Windows, as superfícies habituais são atualizações cumulativas ausentes, membros do grupo local Administrators e serviços remotos como RDP, SMB e WinRM. No Linux, são pacotes desatualizados, contas com direitos de sudo e daemons escutando, como SSH ou uma porta de banco de dados exposta. Um achado que só diz que o servidor é inseguro não dá ao dono nada para fazer. Um achado que diz que um host Linux de staging aceita logins SSH por senha a partir da VLAN de usuários, ao contrário da baseline de endurecimento, nomeia o sistema operacional, o controle que falhou e como é a correção.

### 11.2 Jump hosts

Os caminhos administrativos passam pelo jump host; RDP da VLAN de e-mail para servidores é um achado. Um jump host concentra o acesso administrativo num único lugar que pode ser endurecido, monitorado e protegido com autenticação multifator. Se os administradores também conseguem alcançar os servidores diretamente a partir da rede em que leem e-mail, o comprometimento de suas estações por phishing vira uma rota para os servidores que contorna todos esses controles. Sam testa o caminho a partir de um host sintético da VLAN de usuários com uma conta autorizada. Se uma sessão RDP com um servidor de staging abre sem passar pelo jump host, o achado registra a rede de origem, o destino e a regra de firewall que deveria tê-la bloqueado.

### 11.3 Imagens

Golden images com agentes antigos reintroduzem risco quando há reconstrução. Uma golden image é o modelo a partir do qual novos hosts são construídos; portanto, o que ela contiver é copiado para todo host construído com ela. Se a imagem traz um agente de endpoint duas versões atrás, ou uma conta local criada para uma sessão de depuração, cada reconstrução traz essa fraqueza de volta, muitas vezes depois de o host original ter sido corrigido à mão. A reconstrução deveria remover a deriva, mas uma imagem desatualizada a acrescenta. É por isso que Sam trata uma fraqueza que reaparece depois de uma reconstrução primeiro como um problema de imagem e confere a data de build e o conteúdo da imagem antes de escrever um achado de host.

### 11.4 Logs

Os logs do sistema operacional sustentam recomendações de detecção ligadas ao ATT&CK. Um teste pode mostrar mais do que se um ataque funciona. Ele também pode mostrar se os defensores o teriam visto. Depois de uma ação autorizada, como criar uma tarefa agendada com uma conta de teste, Sam pergunta ao SOC se o evento do Windows de criação de tarefa chegou ao SIEM e se alguma regra disparou. Mapear a ação para sua técnica do ATT&CK dá às duas equipes um nome comum para ela. A recomendação passa então a ser uma melhoria de detecção, por exemplo encaminhar o evento de criação de tarefa dos servidores de staging e alertar quando um não administrador cria uma tarefa, em vez de um pedido vago por mais logs.

### 11.5 Privilégios

A administração do hipervisor é uma camada de escopo separada. Quem administra o hipervisor controla toda máquina virtual nele: pode tirar snapshots, anexar discos e abrir consoles sem que o sistema operacional convidado registre grande coisa. A permissão para testar os servidores convidados, portanto, não cobre a camada de virtualização, que geralmente tem outro dono e outro risco. No TRB, a equipe de virtualização precisa assinar sua própria entrada de escopo antes que alguém teste o console de gerenciamento. Se Sam encontra credenciais do hipervisor enquanto testa um convidado, ele registra isso como achado e para ali, porque usá-las levaria o teste a uma camada que ninguém autorizou.

### 11.6 Baselines de endurecimento

Desvios precisam de tickets, não de folclore. Uma baseline é a lista escrita das configurações que todo host de determinado tipo deve ter, como protocolos legados desativados, uma política mínima de senhas e log de auditoria ligado. Sistemas reais se desviam por motivos reais, por exemplo uma aplicação antiga que precisa de um protocolo legado. O desvio só é aceitável se estiver registrado com um dono, um motivo e uma data de expiração. Sem esse registro, um testador não consegue distinguir uma exceção aprovada de negligência, e o próximo administrador herda uma configuração que ninguém sabe explicar. Sam confere cada desvio que encontra contra o registro de exceções antes de decidir se escreve um achado.

### 11.7 Fixar versões no pipeline de imagens

Os tickets do pipeline de imagens precisam nomear as versões dos agentes embutidos. Sam rejeita "latest" como string de versão. Builds reproduzíveis de golden images são tratados como lançamentos de aplicação. A tag latest descreve um momento, não uma versão. Uma imagem construída na segunda-feira com o agente mais recente e reconstruída na sexta pode conter código diferente, e nenhum dos tickets mostra qual. Números de versão exatos permitem a um testador comparar um host em execução com a imagem da qual ele diz vir, e permitem ao dono do pipeline voltar a um estado conhecido. Tratar imagens como lançamentos também significa que cada uma tem um changelog, um revisor e uma data de aposentadoria.

### 11.8 Censo de administradores locais

Uma consulta trimestral lista os administradores locais em staging. Nomes inesperados viram tickets. Sam faz a correlação com as listas de desligados. Os direitos de administrador local se acumulam em silêncio. Alguém é adicionado para consertar um driver de impressora e nunca é removido, ou uma conta de serviço recebe direitos de administrador porque isso foi mais rápido do que descobrir de que ela precisava. O censo compara o grupo local Administrators de cada host com a lista esperada para a função desse host. Nomes ausentes da lista esperada são conferidos primeiro contra a lista de desligados, porque uma conta de administrador de alguém que saiu é o caso mais urgente. Cada censo é salvo, para que o seguinte mostre se a contagem está caindo.

### 11.9 Deriva de agentes

Hosts cuja versão do agente difere do catálogo de imagens por mais de uma versão menor abrem tickets automaticamente. O agente de endpoint é a forma como os defensores enxergam um host; por isso, um agente desatualizado pode deixar de ver técnicas que versões mais novas detectam, ou pode falhar em silêncio. A tolerância de uma versão menor permite implantações escalonadas, nas quais alguns hosts atualizam uma semana antes de outros, sem abrir tickets por um atraso normal. Qualquer coisa mais atrasada geralmente significa que o host parou de receber atualizações, muitas vezes porque foi movido para um segmento de rede que o servidor de atualizações não alcança. O ticket automático nomeia o host, os dois números de versão e a data em que o host se comunicou pela última vez.

### 11.10 Uma reconstrução que reintroduziu o RDP

Um host de staging reconstruído volta com uma postura antiga de RDP. O catálogo de imagens dizia que isso não deveria acontecer. Sam registra tanto um achado de host quanto um achado de pipeline de imagens. Dois donos, dois tickets, uma classe de causa raiz. O dono do host pode corrigir seu servidor no mesmo dia, desativando o RDP a partir da VLAN de usuários. Isso não faz nada pelo próximo servidor construído pelo mesmo pipeline. O ticket do dono da imagem pergunta por que o catálogo e o build discordaram. Neste caso, uma etapa de configuração tinha sido movida para um estágio opcional que a reconstrução pulou. Ligar os dois tickets permite ao revisor fechar o achado de host só depois que o achado de imagem tiver uma correção implantada.

### 11.11 Um administrador temporário esquecido

O censo de administradores locais encontrou um administrador "temp" dormente criado durante uma indisponibilidade. Ticket, remoção, verificação. Temporários dormentes são permanentes até serem caçados. A conta tinha sido criada às 02:00, durante uma indisponibilidade de armazenamento, para que um terceirizado pudesse reiniciar serviços, e o registro do incidente dizia que ela seria removida na manhã seguinte. Não foi. Sua senha nunca tinha sido trocada e ela não fazia login havia sete meses, o que a tornava ao mesmo tempo inútil e perigosa. Depois de removê-la, Sam verificou a remoção no host e acrescentou ao modelo de indisponibilidade um campo para contas de emergência, cada uma com um horário de expiração que a revisão de encerramento precisa conferir.

### 11.12 Copiar os donos de imagens nos achados

Os achados de imagem sempre põem em cópia o dono do pipeline, não só o dono do host. Os donos de hosts muitas vezes não enxergam o pipeline que construiu seus servidores, e os donos de pipelines raramente olham tickets de hosts individuais. Uma fraqueza herdada de uma imagem cai entre os dois. O dono do host corrige sua máquina e fecha o ticket, e o pipeline continua produzindo a mesma fraqueza. Pôr o dono do pipeline em cópia coloca o achado diante da pessoa que pode impedir que ele se repita. O FindingsDesk faz isso automaticamente quando a causa raiz de um achado é definida como imagem, de modo que o roteamento não depende de o testador se lembrar.

### 11.13 Ponderar os achados de imagem pela recorrência

Os achados de pipeline usam uma rubrica de severidade separada, ponderada pela recorrência. Uma imagem ruim pode cunhar cem hosts ruins. Num único host, uma configuração fraca pode ser classificada como média porque poucas pessoas conseguem alcançá-lo. A mesma configuração numa imagem que constrói todos os servidores web de staging e de produção é um risco diferente, porque seu alcance cresce a cada build e ela volta depois de cada correção local. A rubrica de imagens, portanto, pergunta quantos hosts são construídos a partir da imagem, com que frequência são reconstruídos e se algum deles está voltado para a internet. Um achado de host médio pode se tornar um achado de pipeline alto sem nenhuma mudança na fraqueza técnica.

### 11.14 Publicar as duas escalas de severidade

A rubrica ponderada pela recorrência para imagens é publicada ao lado da severidade de hosts. Bichos diferentes, escalas diferentes. Publicar as duas escalas evita uma discussão previsível. Um dono de pipeline que vê uma classificação alta para uma configuração que a equipe de hosts classificou como média vai suspeitar de inconsistência, a menos que o motivo esteja escrito. A página publicada mostra as duas rubricas lado a lado, com um exemplo resolvido de uma fraqueza classificada em cada uma. Os revisores conferem que todo achado de imagem declara qual escala usou. Ter uma escala separada também permite ao TRB acompanhar a dívida de pipeline por conta própria, o que fundamentou o pedido de financiamento para testes automatizados de imagens.

### Exemplo resolvido (TRB sintético)

Sam registra o RDP de staging a partir da VLAN de e-mail, contornando o jump host, como um achado com o hash da captura de tela.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX031 — Contorno do jump host.** Por que o RDP da VLAN de e-mail para servidores é um achado? *Rubrica:* 3 = contorna o caminho controlado/registrado do jump host; 2 = parcial; 1 = tudo bem; 0 = nada.
- **EX032 — Risco das imagens.** Como imagens desatualizadas criam fraquezas? *Rubrica:* 3 = reimplantam agentes/configurações antigos; 2 = parcial; 1 = sem risco; 0 = nada.
- **EX033 — Hipervisor.** A administração do hipervisor está implícita no escopo web? *Rubrica:* 3 = não; camada separada; 2 = não; 1 = sim; 0 = nada.

### Síntese

Os achados de sistema operacional nomeiam a camada; a administração passa por jump hosts.

### Continue estudando — capítulo 11 de 40

[← Capítulo 10 (rascunho)](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 (rascunho) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) calcular um intervalo de Wilson; (2) explicar taxas-base; (3) evitar afirmações exageradas a partir de um n pequeno.

### 12.1 Taxas

A taxa de detecção k/n precisa de incerteza. Sete de dez não é o mesmo que setenta de cem. As duas dão setenta por cento, mas sustentam afirmações muito diferentes. Com dez tentativas, uma única falha ou detecção a mais move a taxa em dez pontos; assim, a taxa verdadeira poderia plausivelmente estar em qualquer lugar entre cerca de quarenta e quase noventa por cento. Com cem tentativas, a faixa plausível se estreita para aproximadamente sessenta a setenta e oito. Quando o SOC relata que sua nova regra pegou sete das dez técnicas que Sam rodou numa sessão de purple team, o resumo honesto é que a regra provavelmente funciona mais vezes do que não, e que uma afirmação mais forte precisa de mais tentativas.

### 12.2 Intervalo de Wilson

O lab_wilson imprime intervalos de 95% para contagens sintéticas de detecção de purple team.

```python
"""Lab 12: Wilson 95% interval for a synthetic detection rate in a purple-team exercise."""
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
for k, n in [(7, 10), (70, 100)]:
    lo, hi = wilson(k, n)
    print(f"detected {k}/{n} rate={k/n:.2f} 95% CI=({lo:.2f}, {hi:.2f})")
```

Execute com `python3 lab_wilson.py`. Saída verificada:

```text
detected 7/10 rate=0.70 95% CI=(0.40, 0.89)
detected 70/100 rate=0.70 95% CI=(0.60, 0.78)
```

O intervalo de Wilson é preferido à fórmula de livro-texto de p mais ou menos 1,96 erros-padrão porque essa fórmula se comporta mal com amostras pequenas e com taxas perto de zero ou de um. Ela pode produzir intervalos abaixo de zero ou acima de cem por cento e afirma certeza demais quando poucas tentativas foram feitas. A versão de Wilson puxa ligeiramente o centro em direção a um meio e mantém os limites dentro da faixa possível. Exercícios de purple team são exatamente o cenário de amostra pequena e taxa alta em que isso importa. Comparar as duas linhas impressas mostra o ponto prático: os mesmos setenta por cento carregam uma faixa mais de duas vezes mais larga com dez tentativas.

### 12.3 Taxas-base

Problemas verdadeiros raros, afogados em scanners ruidosos, desperdiçam o tempo de quem corrige. Suponha que um scanner aponte uma fraqueza corretamente em noventa por cento dos hosts vulneráveis e erroneamente em cinco por cento dos corrigidos, e que apenas dois por cento dos mil hosts de staging do TRB sejam de fato vulneráveis. Ele vai encontrar cerca de dezoito dos vinte casos reais e levantar cerca de quarenta e nove alarmes falsos; assim, aproximadamente sete em cada dez alertas estão errados. Desenvolvedores que perseguem esses alarmes falsos aprendem a ignorar o scanner. A taxa-base, a parcela de hosts que realmente têm o problema, decide quão útil é um resultado positivo, e é por isso que Sam confirma à mão a saída do scanner antes de transformá-la em achados.

### 12.4 Classificar defesas

Prefira intervalos que não se sobrepõem ao afirmar que A vence B. Se um controle deteve catorze de vinte cliques simulados de phishing e outro deteve onze de vinte, o primeiro parece melhor, setenta contra cinquenta e cinco por cento. Seus intervalos de Wilson vão de cerca de quarenta e oito a oitenta e cinco e de cerca de trinta e quatro a setenta e quatro, que se sobrepõem amplamente; portanto, os dados não conseguem separar os dois. A sobreposição não prova que os controles são iguais. Ela mostra que o experimento era pequeno demais para dizer. A não sobreposição é uma regra grosseira e conservadora: um teste formal para a diferença entre duas proporções é melhor, mas a verificação de sobreposição barra a afirmação exagerada mais comum antes que ela chegue a um slide.

### 12.5 Relato

Os gestores ouvem contagens e intervalos em linguagem simples. Uma frase como "a detecção foi 0,7, com IC de Wilson de 95% de 0,40 a 0,89" está correta e é quase inútil para um leitor que precisa decidir alguma coisa. Sam a reescreve assim: o SOC detectou sete das dez técnicas que tentamos. Com tão poucas tentativas, a taxa real poderia ser tão baixa quanto quatro em dez ou tão alta quanto nove em dez; por isso, recomendamos outra rodada antes de mudar o orçamento. As contagens vêm primeiro porque as pessoas conseguem visualizá-las, a faixa vem a seguir em palavras, e a frase termina com o que a incerteza significa para a decisão.

### 12.6 Limites

As premissas de independência falham quando os testes compartilham falhas do ambiente. Os cálculos de intervalo presumem que cada tentativa é um sorteio separado, de modo que um resultado não influencia outro. Exercícios reais quebram essa premissa. Se um encaminhador de logs ficou fora do ar por uma hora, toda técnica que Sam rodou naquela hora passou sem detecção pelo mesmo motivo, e dez falhas equivalem, na verdade, a uma única falha contada dez vezes. O intervalo então parece mais estreito do que a evidência justifica. Sam registra o horário e o host-alvo de cada tentativa, verifica se as falhas se agrupam e relata uma falha agrupada como um único achado de infraestrutura, e não como uma taxa de detecção baixa.

### 12.7 Retirar um slide de classificação

Quando os intervalos se sobrepõem, Sam proíbe classificar defesas como vencedoras. Um slide certa vez afirmava que o MFA vencia o treinamento contra phishing com base em intervalos de Wilson sobrepostos; ele retirou o slide e pediu mais tentativas em vez de uma fonte maior. O autor do slide não estava errado em achar que o MFA provavelmente ajuda mais; o conhecimento prévio sugere que sim. O problema era que o slide apresentava os dados do exercício como prova, e os dados não aguentavam esse peso. Sam sugeriu uma redação que mantinha separados o conhecimento prévio e a evidência: a experiência do setor favorece o MFA, e este exercício foi pequeno demais para confirmar ou contradizer isso. Ele também propôs o número de tentativas necessário para uma resposta mais clara no trimestre seguinte.

### 12.8 Todo intervalo em palavras

Sam exige que todo intervalo de uma apresentação apareça uma vez em palavras: "entre cerca de X e Y". Gráficos sozinhos não bastam para o material do conselho. Barras de erro num gráfico são fáceis de ignorar e difíceis de ler quando os slides são impressos em tons de cinza ou percorridos rapidamente num celular. Uma frase sobrevive às duas situações. A regra também pega erros, porque escrever que a taxa ficou entre cerca de quarenta e noventa por cento faz o revisor notar quão larga ela é, coisa que uma barra elegante com um bigode fino não faz. Os membros do conselho que leem as palavras fazem perguntas melhores com consistência, geralmente sobre como estreitar a faixa.

### 12.9 Planejar o número de tentativas

Uma pequena ferramenta sugere n para uma largura-alvo do IC. Sam a usa antes de prometer taxas de detecção a executivos. O planejador inverte o intervalo: dê a ele a taxa que você espera e a largura de faixa que pode aceitar, e ele devolve aproximadamente quantas tentativas você precisa. Para uma taxa perto de um meio e uma faixa de dez pontos para cada lado, a resposta é perto de noventa e seis tentativas. Rodá-lo antes de um exercício muda a conversa. A promessa de medir a detecção com precisão de dez pontos vira ou um compromisso com cerca de cem tentativas, ou uma decisão honesta de relatar uma faixa mais larga a partir das vinte tentativas que a janela permite.

### 12.10 O financeiro pede um único número

O financeiro pede uma única porcentagem de detecção para o relatório anual. Em vez disso, Sam dá duas frases com intervalos. O jurídico prefere a versão dele, porque ela não pode ser lida como uma garantia. A linguagem da incerteza protege o banco. Um único número impresso num relatório anual se torna uma declaração pública sobre as defesas do banco. Se o TRB publicasse que detecta setenta por cento dos ataques, um regulador ou um litigante, depois de uma violação, poderia tratar isso como uma declaração que o banco não cumpriu. As frases de Sam descrevem o que foi medido, em qual exercício e com que incerteza, o que é preciso e muito mais difícil de ler errado. O financeiro ganha um número para citar, e o banco não promete mais do que sua evidência mostra.

### 12.11 Encolher a afirmação

O planejador de tamanho de amostra disse a Sam que ele precisava de n≈96 para um intervalo apertado. Ele encolheu a afirmação em vez de inventar dados. Planejadores existem para encolher promessas. A janela do exercício permitia cerca de trinta tentativas. Sam poderia ter rodado as mesmas técnicas três vezes cada para chegar a noventa e seis, mas execuções repetidas contra os mesmos hosts não são independentes; portanto, o intervalo mais estreito teria sido falso. Em vez disso, o relatório afirmou o que trinta tentativas independentes sustentavam: a detecção provavelmente estava acima de um meio, e comparações mais finas exigiriam um exercício maior. O principal valor do planejador foi tornar esse limite visível antes que alguém tivesse prometido mais.

### 12.12 Um apêndice que explica a recusa

O material do conselho que insiste num único número recebe o apêndice de Sam com a justificativa da recusa. O jurídico endossou o apêndice. O apêndice tem uma página. Ele mostra as contagens, o intervalo e dois parágrafos curtos. O primeiro explica por que uma única porcentagem exageraria o que o exercício mediu. O segundo diz o que o banco pode afirmar com segurança. Escrevê-lo uma vez poupa discutir o mesmo ponto a cada trimestre, e anexá-lo sempre que alguém pede um único número leva a discussão da opinião de Sam para uma posição acordada do banco. O endosso do jurídico importa porque o risco que o apêndice trata é tanto jurídico quanto estatístico.

### 12.13 Registrar o endosso do jurídico

O apêndice de recusa tem anexado o hash do e-mail de endosso do jurídico. Sam adora a integridade chata. O hash permite a qualquer pessoa confirmar depois que o apêndice num material do conselho é a versão que o jurídico aprovou, não uma cópia editada. O e-mail de endosso é armazenado no arquivo de governança, e seu valor SHA-256 é impresso no rodapé do apêndice. Se a redação muda, o hash deixa de bater e a mudança precisa de um novo endosso. Isso usa o mesmo hábito de integridade do manuseio de evidências: um documento cuja autoridade importa deve poder ser conferido sem confiar em quem o encaminhou.

### Exemplo resolvido (TRB sintético)

Sam mostra 7/10, IC (0,40; 0,89), contra 70/100, IC (0,60; 0,78), para explicar por que o TRB financia mais tentativas antes de declarar uma vitória de detecção.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX034 — Leitura do intervalo.** Que IC o laboratório imprime para 7/10? *Rubrica:* 3 = (0.40, 0.89); 2 = aproximado; 1 = errado; 0 = nada.
- **EX035 — Por que mais largo.** Por que o intervalo de 7/10 é mais largo que o de 70/100 com a mesma taxa? *Rubrica:* 3 = amostra menor / mais incerteza; 2 = parcial; 1 = bug; 0 = nada.
- **EX036 — Frase para o gestor.** Escreva uma frase simples que Sam poderia dizer sobre 7/10. *Rubrica:* 3 = contagem + incerteza + não definitivo; 2 = parcial; 1 = "estamos 70% seguros"; 0 = nada.

### Síntese

Amostras pequenas precisam de intervalos; confiança não é uma porcentagem de segurança.

### Continue estudando — capítulo 12 de 40

[← Capítulo 11 (rascunho)](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 (rascunho) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) separar AuthN e AuthZ; (2) aplicar o menor privilégio às contas de teste; (3) mapear contas compartilhadas para a T1078.

### 13.1 AuthN/AuthZ

Provar identidade versus permitir ações. O IDOR é uma falha de AuthZ depois da AuthN. A autenticação responde quem está fazendo a requisição, por meio de uma senha, passkey ou token. A autorização responde se essa pessoa pode fazer esta coisa específica com este objeto específico. Uma referência direta insegura a objeto acontece quando uma aplicação verifica a primeira e pula a segunda. Um cliente faz login corretamente, depois troca um número de conta na URL de um extrato e recebe o extrato de outra pessoa. No TRB, Sam testa a autorização fazendo login como um cliente sintético e pedindo objetos que pertencem a um segundo cliente sintético; assim, um sucesso prova a falha sem tocar nos dados de nenhuma pessoa real.

### 13.2 Contas de teste

Nominais, temporárias, guardadas no cofre, com menor privilégio. Cada propriedade evita uma falha específica. Uma conta nominal, como rt-sam-cust01, liga toda ação nos logs a um único testador, o que uma conta compartilhada não consegue fazer. Uma conta temporária expira quando a janela fecha; assim, uma credencial esquecida se torna inútil em vez de virar uma porta dos fundos. Guardar as credenciais no cofre as mantém fora de mensagens de chat e de arquivos de anotações. Menor privilégio significa que a conta tem apenas os direitos de que os testes planejados precisam. Testar uma falha voltada ao cliente com uma conta de administrador não provaria nada sobre o que um cliente pode fazer e acrescentaria risco se a sessão fosse sequestrada.

### 13.3 Administradores compartilhados

Perda de responsabilização; ATT&CK T1078 Valid Accounts. Quando cinco administradores compartilham uma conta, o log mostra que o admin fez uma mudança, mas não qual pessoa a fez. Isso atrapalha as investigações e deixa os erros sem dono. Credenciais compartilhadas também viajam. Elas são escritas em scripts, documentos de integração e arquivos de configuração, de modo que sobrevivem às pessoas que as conheciam. O ATT&CK lista o abuso de credenciais legítimas como Valid Accounts porque um atacante usando uma senha real de administrador parece administração normal. O achado de Sam para uma conta de administrador compartilhada recomenda contas nominais que possam elevar direitos e registra onde a senha compartilhada foi encontrada armazenada.

### 13.4 MFA

Verificar pela revisão de configuração, não fazendo phishing com funcionários. A pergunta é se a autenticação multifator está imposta em toda rota que importa, e a configuração do provedor de identidade responde a isso diretamente: quais aplicações a exigem, quais grupos estão isentos e se protocolos legados que a contornam ainda estão habilitados. Enviar e-mails de phishing a funcionários reais para descobrir envolveria pessoas que não consentiram em ser testadas neste engajamento e mediria o comportamento delas, e não o controle. Sam exporta as políticas de acesso condicional e confirma uma isenção com uma conta de teste autorizada. O achado nomeia a lacuna com precisão, por exemplo que um endpoint IMAP aceita senhas sem um segundo fator.

### 13.5 Contas de serviço

Donos e datas de rotação obrigatórios. As contas de serviço permitem que aplicações falem com bancos de dados e APIs sem uma pessoa presente, o que também significa que ninguém percebe quando são mal usadas. Uma conta sem dono nomeado não pode ser rotacionada com segurança, porque ninguém sabe quais sistemas vão quebrar quando a senha mudar; por isso, ela geralmente nunca muda. A revisão de Sam lista toda conta de serviço com seu dono, a data da última rotação e os direitos que ela detém e, em seguida, sinaliza as que não têm dono, as rotacionadas há mais de um ano e as que têm direitos de logon interativo de que não deveriam precisar. A correção mais comum é tornar a conta não interativa.

### 13.6 Desligados

Acesso que persiste depois do desligamento no RH é um achado clássico. A lacuna geralmente vem de um processo com várias passagens de bastão. O RH registra a data de saída, a TI desativa a conta do diretório e ninguém remove as contas locais, os logins de SaaS criados fora do single sign-on ou o certificado de VPN. Sam testa isso pegando um registro sintético de desligado e verificando cada sistema a que a função tinha acesso. Encontrar um único login sobrevivente basta para um achado. A recomendação trata do processo, por exemplo dirigir o desprovisionamento a partir do evento do RH e listar todo sistema que fica fora do single sign-on, não só a conta que por acaso foi encontrada.

### 13.7 Expirar as contas de teste automaticamente

A expiração das contas de teste é imposta por uma rotina que desativa as contas no fim da janela e aciona Sam se a desativação falhar. Os lembretes manuais falharam duas vezes no passado; a rotina agora é um controle, não uma conveniência. O acionamento em caso de falha é a parte importante. Uma rotina que falha em silêncio é pior que nenhuma rotina, porque todos acreditam que as contas estão desativadas. A desativação pode falhar quando o serviço de identidade está em manutenção ou quando uma conta foi renomeada, e cada falha deixa uma credencial funcionando por aí. O acionamento vai para o testador e para o líder de segurança juntos. Nenhum dos dois pode encerrar o engajamento até que ambos confirmem que a conta está desativada.

### 13.8 Contas break-glass

Os administradores break-glass são monitorados e raros. A revisão de Sam confere que a conta break-glass não foi usada como conta do dia a dia durante a janela. Uma conta break-glass existe para o dia em que o sistema de identidade normal falha. Ela contorna o single sign-on e geralmente a autenticação multifator, o que a torna poderosa e perigosa. Suas credenciais ficam lacradas, e qualquer uso deve produzir um alerta e uma justificativa escrita. O teste é simples: contar seus logins no último trimestre e compará-los com as emergências registradas. Se os logins superam as emergências, alguém está usando a conta por conveniência. O achado então recomenda corrigir o problema de acesso normal que levou as pessoas a ela.

### 13.9 Confirmar que o cofre nega acesso sem MFA

O acesso ao cofre de credenciais exige MFA. Sam testou a negação sem MFA e registrou a negação como demonstração de um controle positivo. Os controles merecem evidência quando funcionam, não só quando falham. O teste usou uma conta de teste com a senha correta e sem segundo fator e registrou a recusa do cofre junto com sua entrada de log. Registrar essa recusa como um controle positivo significa que a próxima auditoria pode se apoiar em evidência datada, em vez de numa captura de tela da configuração. Isso também define uma referência. Se um teste posterior com a mesma conta tiver sucesso, algo mudou, e o registro anterior mostra exatamente quando se sabia que o controle funcionava pela última vez.

### 13.10 Uma senha rotacionada encontrada numa impressora

Uma senha de administrador compartilhada no sistema de empréstimos é rotacionada, mas a mesma senha é encontrada depois na configuração de uma impressora. A lista de verificação de desligados e segredos de Sam agora inclui "procurar artefatos de reutilização de senha" depois de qualquer achado de administrador compartilhado. A rotação corrigiu um sistema e deixou o segredo antigo funcionando onde quer que ele tivesse sido reutilizado. Anos antes, alguém tinha configurado na impressora a digitalização para pasta com as credenciais do administrador de empréstimos, e a interface web da impressora mostrava a senha a qualquer pessoa na rede. Uma senha compartilhada geralmente tem uma história; por isso, a busca cobre scripts, tarefas agendadas, configurações de dispositivos e documentação, não só o sistema em que ela foi encontrada primeiro.

### 13.11 Testar o alerta de break-glass

O uso de break-glass durante uma janela aciona automaticamente o canal do CISO. Sam testou o acionamento com uma conta break-glass de staging e recebeu um telefonema severo, mas correto. O telefonema foi a evidência de que o alerta funciona, porque mostrou que uma pessoa respondeu, e não apenas que uma mensagem foi enviada. Antes do teste, Sam combinou o horário com o líder de segurança e o registrou no log do engajamento, para que a ligação pudesse ser resolvida rapidamente. Quem atendeu ainda seguiu o procedimento completo e perguntou quem estava usando a conta, por que e sob qual autoridade. Esse é o comportamento certo, já que um atacante também poderia alegar estar fazendo um teste.

### 13.12 Auditar a automação de desligados

Os tickets de desligados se abrem automaticamente a partir dos eventos do RH em até uma hora; Sam audita a automação toda semana. A automação desloca o risco em vez de removê-lo. Se o elo entre o sistema de RH e a ferramenta de tickets quebrar, os desligados param de gerar tickets em silêncio e ninguém vê um ticket ausente. A auditoria semanal compara os desligamentos da semana no RH com os tickets abertos e confere que cada ticket foi fechado com todos os sistemas listados confirmados. Numa semana, as contagens diferiram em três. Uma mudança de esquema na exportação do RH tinha renomeado o campo da data de saída, e a integração pulou esses registros sem relatar erro.

### 13.13 Procurar segredos nas configurações de dispositivos

As configurações de impressoras agora estão no caminho da busca de segredos, depois do incidente de reutilização. Lugares estranhos escondem senhas. Impressoras, armazenamento em rede, controladores de porta e sistemas de salas de reunião frequentemente se autenticam em servidores, e suas páginas de configuração podem guardar essas credenciais de forma legível. Poucas equipes pensam neles como lugares onde vivem segredos; por isso, raramente são rotacionados ou revisados. A busca ampliada usa exportações de configuração coletadas pelos donos dos dispositivos com permissão, e não logins em cada dispositivo durante o teste. As credenciais encontradas são relatadas aos donos e rotacionadas. O testador não as usa, porque usar uma credencial encontrada num dispositivo testaria um sistema fora dos métodos acordados.

### 13.14 Manter a busca de segredos dentro do escopo

As ampliações do caminho da busca de segredos são registradas; a expansão de escopo na busca continua sendo escopo. Cada novo local acrescentado à busca, como exportações de impressoras, um espaço da wiki ou um compartilhamento de arquivos, é registrado com a data, o aprovador e o motivo. Uma busca por senhas lê dados que podem conter informações pessoais e segredos de outras equipes; por isso, precisa da mesma autorização que qualquer outro método de teste. O registro também explica os resultados. Um salto repentino nos segredos encontrados num trimestre só tem significado se os leitores souberem se o banco piorou ou se a busca simplesmente olhou em mais lugares.

### Exemplo resolvido (TRB sintético)

O administrador compartilhado no sistema de empréstimos vira F1, com pontuação 6 no lab_rank.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX037 — T1078.** Que técnica corresponde a senhas válidas de administrador compartilhadas? *Rubrica:* 3 = T1078 Valid Accounts; 2 = o nome; 1 = errado; 0 = nada.
- **EX038 — Método para o MFA.** Como verificar o MFA sem phishing? *Rubrica:* 3 = revisão de configuração/política sob as ROE; 2 = parcial; 1 = phishing; 0 = nada.
- **EX039 — Características da conta de teste.** Liste três características de uma boa conta de teste. *Rubrica:* 3 = nominal, menor privilégio, temporária/no cofre; 2 = duas; 1 = uma; 0 = nada.

### Síntese

Os achados de identidade são precisos quanto a AuthN vs AuthZ e nunca exigem fazer phishing com colegas.

### Continue estudando — capítulo 13 de 40

[← Capítulo 12 (rascunho)](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 (rascunho) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem

Você vai (1) minimizar os dados de clientes nas evidências; (2) redigir; (3) respeitar a retenção.

### 14.1 Minimização

A prova vale mais que extrações em massa de tabelas de clientes. Um testador precisa mostrar que uma fraqueza existe, não coletar o que ela expõe. Se uma API devolve os saldos de outros clientes, uma resposta contendo o saldo de uma conta sintética prova a falha tão bem quanto dez mil reais, e não cria nenhuma nova cópia de dados reais de clientes. Cada registro extra capturado precisa ser armazenado, protegido, relatado e apagado, e pode ele mesmo se tornar uma violação a ser notificada. Sam para um teste assim que tem a primeira resposta que prova o problema. Ele registra quantos registros o endpoint poderia ter devolvido, em vez de obtê-los para provar isso.

### 14.2 Redação

Mascare os números de conta; mantenha os dígitos que provam o problema, se necessário. A redação deve remover a identidade enquanto preserva a prova. Uma captura de tela mostrando que a sessão do cliente A exibiu o extrato do cliente B só precisa dos quatro últimos dígitos de cada número de conta para mostrar que os dois diferem. Os números completos acrescentam risco e nenhuma evidência. Nomes, endereços e saldos são cobertos com caixas sólidas. O desfoque às vezes pode ser revertido, e o recorte pode deixar texto nos metadados da imagem. Sam redige numa cópia, mantém o original não redigido no cofre sob sua data de retenção e calcula o hash dos dois, para que um revisor possa confirmar que a imagem redigida veio da evidência original.

### 14.3 Limitação de finalidade

As evidências do engajamento não são uma fonte de análise de marketing. Os dados dos clientes chegaram à equipe de testes por um único motivo, que era verificar a segurança do banco sob um contrato assinado. Usar as mesmas capturas de tela para estudar como os clientes usam o aplicativo, ou para ilustrar uma apresentação de vendas, é uma nova finalidade que os clientes nunca esperaram e que o contrato nunca cobriu. As leis de privacidade de muitas jurisdições tratam essa mudança de finalidade como algo que precisa de sua própria base legal. A regra prática no TRB é simples. As evidências respondem a perguntas sobre o engajamento de onde vieram, e qualquer outra pergunta precisa de dados separados, coletados para essa finalidade.

### 14.4 Acesso

Necessidade de saber nos cofres de evidências. As evidências de um engajamento são lidas por seus testadores, seu revisor e o custodiante, e por mais ninguém por padrão. Um desenvolvedor que corrige um achado vê a descrição do achado e a prova redigida, não a captura bruta. Um gestor vê o status e a severidade. Pedidos de acesso fora desses papéis vão ao líder do engajamento com um motivo e uma data de término. A necessidade de saber também limita os danos. Se a conta de um testador for comprometida, o atacante alcança as evidências de um engajamento, não toda captura de tela que a equipe fez em cinco anos.

### 14.5 Transferências internacionais

Regiões de nuvem podem envolver regras; o jurídico orienta. As evidências armazenadas num serviço de nuvem ficam numa região específica, e backups ou acessos de suporte podem alcançar outras. Se as evidências contêm dados pessoais de clientes de um país e o armazenamento ou a equipe de suporte do fornecedor estão em outro, podem se aplicar regras de transferência de dados, além dos compromissos do próprio banco com seu regulador. Não se espera que os testadores interpretem essas regras por conta própria. Espera-se que percebam quando as evidências estão prestes a cruzar uma fronteira, por exemplo ao enviá-las a uma ferramenta nova ou compartilhá-las com um fornecedor no exterior, e que consultem o jurídico antes de fazê-lo.

### 14.6 Risco de violação

Os cofres de evidências são alvos de alto valor; proteja-os. O cofre de uma equipe de testes guarda as fraquezas do banco, a prova de como alcançá-las e amostras dos dados por trás delas, o que, junto, forma um roteiro para o atacante. Por isso, o cofre recebe controles pelo menos tão fortes quanto os dos sistemas que ele descreve: autenticação multifator, acesso registrado, criptografia em repouso, retenção curta e seu próprio lugar no plano de incidentes. Se o cofre fosse comprometido, o banco teria de tratar todo achado não corrigido nele como potencialmente conhecido por um atacante. É por isso que o TRB prioriza a correção das fraquezas registradas num cofre exposto, qualquer que seja sua severidade original.

### 14.7 Exercícios de reidentificação

Os exercícios de reidentificação juntam uma captura de tela redigida a organogramas públicos. Se um colega consegue nomear a pessoa, a redação é reprovada no portão. Sam agora prefere personas sintéticas na maioria das capturas de tela didáticas. O exercício testa o que um leitor consegue deduzir, não só o que foi coberto. A captura de tela de uma página administrativa interna pode esconder um nome, mas deixar um cargo, um código de agência e um carimbo de tempo, e, junto com um organograma público, isso identifica uma pessoa. Os colegas têm dez minutos e apenas fontes públicas. Uma identificação bem-sucedida não conta como erro de quem redigiu. Ela mostra que a regra de redação deixou passar um tipo de campo, e a regra é atualizada.

### 14.8 Uma biblioteca de evidências sintéticas

Uma biblioteca de capturas de tela sintéticas cobre os achados comuns, para que os alunos não precisem manusear pixels de clientes reais. Sam contribui com uma nova imagem sintética a cada período letivo. Cada entrada recria um achado típico numa maquete das interfaces do TRB, como uma página de extrato mostrando o cliente errado, uma mensagem de erro vazando um stack trace ou um painel administrativo alcançável sem login, usando dados inventados do começo ao fim. Treinamentos, modelos de relatório e palestras em conferências usam a biblioteca em vez das pastas de engajamento. Construir uma entrada leva algumas horas e remove para sempre a tentação de redigir uma captura de tela real para um slide.

### 14.9 Etiquetas de finalidade nas evidências

Os arquivos de evidência recebem uma etiqueta de finalidade; o uso secundário exige uma nova etiqueta e aprovação. O marketing não pode "só pegar emprestadas" as capturas de tela do engajamento. A etiqueta é definida no upload. Na maioria dos casos, ela é "evidência do engajamento" e, para alguns arquivos, "evidência do engajamento mais uso aprovado em treinamento". O FindingsDesk confere a etiqueta sempre que um arquivo é copiado para outro espaço de trabalho ou anexado a qualquer coisa que não seja um achado, e bloqueia a ação se as finalidades não coincidirem. Acrescentar uma finalidade exige a aprovação do líder do engajamento e uma verificação de privacidade. A etiqueta transforma uma frase de política numa verificação que roda toda vez que um arquivo se move.

### 14.10 Os alunos escolhem o exemplo sintético

O item SS-17 da biblioteca de capturas sintéticas mostra uma cliente falsa, "Ada Example", com a conta ••••4242. Os alunos o preferem a redigir telas reais. Sam mede essa preferência e financia mais arte sintética. A preferência é prática, além de ética. Redigir corretamente uma captura de tela real toma vinte minutos do aluno e uma verificação do revisor, enquanto a sintética está pronta para uso e não traz risco se acabar no lugar errado. Sam acompanha com que frequência cada item da biblioteca é usado. Os itens mais usados mostram sobre quais achados os alunos mais escrevem, e esses são os próximos a ganhar versões sintéticas.

### 14.11 Uma cópia bloqueada para uma pasta de design

As etiquetas de finalidade impediram que um trainee bem-intencionado colocasse capturas de tela do engajamento numa pasta de redesenho de UX. A recusa pareceu mesquinha e protegeu cem clientes. A ideia do trainee era razoável à primeira vista. As capturas de tela mostravam telas reais e confusas que a equipe de design queria melhorar. Também mostravam nomes reais de clientes e saldos parciais, e a pasta de design era compartilhada com uma agência externa. A correção levou uma tarde. O trainee descreveu cada tela confusa em palavras, e a equipe de design a reconstruiu com dados sintéticos. A agência obteve o que precisava e nenhum dado de cliente saiu do banco.

### 14.12 Manter as personas sintéticas obviamente falsas

A sintética Ada Example tem um guia de estilo para que os artistas a mantenham obviamente falsa. Uma persona sintética real demais causa os problemas que deveria evitar. Os leitores podem presumir que é uma cliente real redigida, ou os detalhes podem coincidir por acaso com uma pessoa real. O guia de estilo fixa os sinais reveladores: nomes de uma lista inventada acordada, números de conta terminados em dígitos de teste bem conhecidos, endereços em ruas que não existem na região do TRB e datas num ano de teste reservado. Quem vê esses marcadores reconhece o material didático num relance.

### 14.13 Acordos com ilustradores

Os artistas assinam um CLA segundo o qual Ada Example não pode se parecer com clientes reais. O jurídico insistiu; Sam concordou com prazer. Os ilustradores às vezes baseiam rostos e caligrafias em pessoas que conhecem ou em fotografias de banco de imagens de pessoas reais. No material de treinamento de um banco, uma persona parecida com um cliente real poderia sugerir que a conta desse cliente esteve envolvida num achado de segurança. O acordo de contribuição faz o artista confirmar que toda semelhança é inventada e dá ao TRB os direitos de reutilizar e alterar a arte. Essa segunda parte importa tanto quanto a primeira, porque os exemplos sintéticos precisam ser atualizados quando as interfaces reais mudam.

### 14.14 Visitas à mesa para analistas novos

Os coaches de privacidade do TRB incluem uma visita de cinco minutos à mesa quando um analista novo abre o cofre de evidências pela primeira vez. Sam roteiriza a visita: mostrar as datas de retenção, mostrar a lista de acesso, mostrar um exemplo de falha de redação, pedir ao analista que repita a regra da minimização com as próprias palavras. As visitas à mesa pegam a bravata melhor que os módulos do LMS. Os analistas assinam um pequeno cartão que fica no saguão do cofre.

Uma regra aprendida num documento é facilmente esquecida. Uma regra mostrada à mesa, na tela do próprio analista, com a data de retenção do seu próprio engajamento, tende a ficar. O exemplo de falha de redação é escolhido para ser desconfortável: uma captura de tela que parecia limpa até que um colega nomeou a pessoa nela. Pedir ao analista que reformule a regra mostra se ele a entendeu ou apenas concordou com a cabeça.

### Exemplo resolvido (TRB sintético)

Sam redige tudo, exceto os quatro últimos dígitos, antes de anexar uma captura de tela ao F4.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX040 — Minimização.** Por que não exportar a tabela completa de clientes para um achado? *Rubrica:* 3 = privacidade/finalidade/ROE; 2 = parcial; 1 = precisamos dela; 0 = nada.
- **EX041 — Redação.** O que Sam redige no exemplo da captura de tela? *Rubrica:* 3 = números de conta, exceto os quatro últimos dígitos / identificadores pessoais; 2 = parcial; 1 = vago; 0 = nada.
- **EX042 — Cofre.** Por que proteger fortemente os cofres de evidências? *Rubrica:* 3 = concentram dados sensíveis de prova; 2 = parcial; 1 = não precisa; 0 = nada.

### Síntese

Privacidade é minimização, redação, limites de finalidade e higiene do cofre.

### Continue estudando — capítulo 14 de 40

[← Capítulo 13 (rascunho)](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 (rascunho) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Evidência e medição

### Objetivos de aprendizagem

Você vai (1) calcular hashes de evidências; (2) escolher métricas que não sejam de vaidade; (3) manter a cadeia de custódia.

### 15.1 Hashes

Detectar edições acidentais antes do registro. Um hash criptográfico como o SHA-256 transforma um arquivo numa impressão digital curta que muda completamente se até um único byte mudar. Sam calcula o hash de cada arquivo de evidência quando o captura e de novo quando o anexa a um achado. Se os valores diferem, algo tocou o arquivo nesse meio-tempo, talvez um editor de imagens que o salvou de novo, uma ferramenta de sincronização que converteu as quebras de linha ou uma redação descuidada sobre o original. Pegar isso antes de o relatório sair é fácil. Explicar isso depois que um cliente contesta o achado é muito mais difícil, porque um arquivo alterado parece igual a um adulterado.

### 15.2 Métricas

Ativos tocados, cartões executados, donos designados — não contagens brutas de achados. Uma contagem de achados mede sobretudo o quanto os testadores procuraram e como dividiram os problemas em registros separados. Um aumento de quarenta para sessenta poderia significar que o banco piorou, que o escopo cresceu ou que uma fraqueza foi registrada por host em vez de uma única vez. Medidas mais úteis descrevem o trabalho e seu efeito: quantos ativos do escopo foram de fato testados, quantos métodos de teste planejados foram concluídos, quantos achados têm um dono nomeado e uma data-limite e quanto tempo as correções levam. O PulseMap relata essas medidas, para que um gestor possa saber se um trimestre calmo significa segurança ou pouco teste.

### 15.3 Custódia

Quem/quando/onde para cada artefato. Um registro de cadeia de custódia lista todo ponto em que a evidência mudou de mãos ou de lugar: capturada por Sam num notebook de testes às 21:14, enviada ao FindingsDesk às 21:20, lida pelo revisor na manhã seguinte, exportada em forma redigida para o relatório. Cada entrada tem uma pessoa, um horário e um lugar. Se um achado for contestado meses depois, o registro mostra que a evidência apresentada é a evidência capturada e quem poderia tê-la alterado. Lacunas são registradas como lacunas. Uma nota honesta de que um arquivo ficou num notebook por dois dias é melhor que um registro que esconde isso.

### 15.4 Integridade vs verdade

Hash coincidente ≠ sistema vivo ainda vulnerável. Um hash coincidente prova apenas que o arquivo de evidência não mudou desde que foi capturado. Ele não diz nada sobre se a fraqueza ainda existe, se a evidência foi corretamente entendida ou se o teste era válido. Uma captura de tela pode estar perfeitamente preservada e ainda assim mostrar uma leitura errada. Um servidor vulnerável em março pode ter sido corrigido em abril. É por isso que o TRB separa a integridade da evidência, verificada com hashes, do status do achado, verificado por um reteste. As afirmações do relatório são datadas no momento do teste, por exemplo que o endpoint devolveu dados de outro cliente em 4 de março, e não que ele faz isso agora.

### 15.5 Amostragem

Amostre tickets fechados em busca de evidência de verificação. Conferir todo ticket fechado raramente é viável, e conferir só os que alguém sinaliza deixa passar falhas silenciosas. Uma amostra aleatória evita os dois problemas. Como a amostra é escolhida ao acaso, as equipes não conseguem prever quais tickets serão conferidos; por isso, todo ticket precisa de evidência de que a correção funciona, como um resultado de reteste, um diff de configuração ou uma varredura. Se a amostra revelar evidência ausente, a parcela ausente na amostra estima a parcela ausente no total, e os métodos de intervalo usados para taxas de detecção também se aplicam a essa proporção.

### 15.6 PulseMap

As visões de cobertura precisam mostrar denominadores. Um bloco verde que diz noventa por cento de cobertura esconde a pergunta que importa: noventa por cento de quê. Se o PulseMap conta apenas os hosts do inventário de ativos, e o inventário não tem uma conta de nuvem criada no trimestre passado, a cobertura real é menor do que o bloco sugere. Por isso, cada visão de cobertura mostra a contagem por trás da porcentagem, como quarenta e cinco de cinquenta aplicações web registradas, e nomeia a fonte do total. Os leitores podem então ver quando o próprio denominador parece pequeno demais, o que muitas vezes é o achado mais importante do painel.

### 15.7 Amostragem aleatória de tickets fechados

A amostragem de tickets fechados é de cinco tickets por mês, escolhidos por um gerador de números aleatórios. A ausência de evidência de verificação reabre o ticket automaticamente. Sam publica a contagem de reaberturas para que a manipulação da métrica fique visível. O sorteio é registrado com sua semente, para que qualquer pessoa possa confirmar que os cinco tickets não foram escolhidos a dedo. A reabertura automática mantém a consequência impessoal. Não é Sam acusando uma equipe; é a regra se aplicando sozinha. Publicar a contagem de reaberturas também torna a melhoria visível. Quando as reaberturas de uma unidade de negócio caíram de três por mês para zero, a contagem em queda mostrou que suas correções agora estavam sendo verificadas, e não apenas fechadas.

### 15.8 Um dicionário para os termos das métricas

Um dicionário compartilhado define "tocado", "validado" e "fechado". Sam recusa blocos do PulseMap que usam palavras não definidas. A mesma palavra pode significar coisas diferentes para equipes diferentes. Para um desenvolvedor, fechado pode significar que o código foi mesclado; para as operações, que foi implantado; e, para os testadores, que um reteste passou. Um bloco que conta achados fechados não tem sentido até que a palavra seja fixada. Cada entrada do dicionário dá uma definição, o campo de dados ao qual ela corresponde, um exemplo e um contraexemplo. Quando um bloco novo é proposto, seus rótulos são conferidos contra o dicionário antes da publicação.

### 15.9 O que conta como tocado

"Tocado" significa um cartão de método concluído com evidência, não um ping. A briga de Sam no dicionário por essa palavra valeu uma semana. Pela definição frouxa, um host respondia a uma varredura de rede e por isso contava como coberto. Pela estrita, um método de teste planejado era concluído contra ele e deixava evidência. A diferença foi grande. A cobertura medida por varreduras ficava perto de cem por cento, enquanto a cobertura medida por métodos concluídos ficava em cerca de sessenta. A definição estrita era menos lisonjeira e muito mais útil, porque mostrava quais ativos nunca tinham sido realmente testados.

### 15.10 Um bloco verde com dois pontos de dados

O subtítulo "n=2" ao lado de um visto verde num bloco do PulseMap ensina mais que uma aula sobre tamanho de amostra. Sam deixa de propósito um bloco verde de n pequeno no ambiente de treinamento para provocar perguntas. O bloco mostra que os dois tickets amostrados tinham evidência de verificação, o que dá cem por cento com quase nenhuma informação. Os alunos que o veem geralmente começam dizendo que o controle está funcionando, e então alguém nota o n. A discussão que se segue cobre o que duas observações conseguem sustentar, quão largo é o intervalo e que desenho de bloco evitaria a leitura errada. Essa última pergunta levou à regra de que blocos com amostras muito pequenas não podem ficar verdes.

### 15.11 Aprovar as definições

A briga do dicionário terminou quando o CISO assinou as definições. Sam emoldura o PDF assinado na wiki da equipe. Palavras são controles. A assinatura encerrou a discussão ao fazer das definições uma política do banco, e não uma preferência da equipe de testes. As equipes que discordavam ainda podiam propor mudanças, mas por uma revisão com número de versão, não usando em silêncio o seu próprio significado num painel. Cada bloco do PulseMap agora cita a versão do dicionário que usa. Quando uma definição muda, os números antigos e novos não são plotados na mesma linha sem um marcador, para que um salto causado pela redefinição não seja confundido com uma mudança real.

### 15.12 Definições no papel

As definições de métricas assinadas ficam penduradas ao lado da máquina de café da equipe — o papel ainda funciona. Uma página impressa na parede é vista por pessoas que nunca abririam a wiki, incluindo visitantes de outras equipes que vêm perguntar o que um número significa. Seu uso principal é nas conversas rápidas. Quando alguém diz que um achado está fechado, um colega pode apontar para a definição e perguntar se o reteste passou. A página traz seu número de versão e sua data, de modo que uma impressão desatualizada é fácil de notar e substituir quando a versão assinada muda.

### 15.13 Um estado amarelo para termos não definidos

Blocos com palavras não definidas mostram um estado amarelo, "defina-me", em vez de verde. O amarelo é mais difícil de ignorar. Um bloco que usa um termo ausente do dicionário ainda mostra seu número, mas não pode ficar verde, porque ninguém sabe dizer o que o verde significaria. O estado amarelo nomeia a palavra não definida e leva ao formulário para propor uma definição. Isso evita duas opções piores. Esconder o bloco perde informação, e mostrá-lo verde dá uma falsa tranquilidade. Na prática, a maioria dos blocos amarelos é corrigida em uma semana, geralmente mapeando o rótulo para um termo existente.

### 15.14 Plantão de medição

O plantão de medição acontece às quintas-feiras. Qualquer pessoa pode trazer um bloco que pareça enganoso. A correção mais comum de Sam é acrescentar n ao subtítulo ou trocar o verde por amarelo. Ele acompanha quantos blocos mudam de cor a cada mês, como uma métrica de qualidade das métricas. O plantão dá às pessoas uma forma de baixo risco de questionar um número sem acusar quem construiu o bloco. Muitas queixas acabam sendo sobre rótulos, e não sobre dados. Um bloco que diz "incidentes" pode, na verdade, estar contando alertas, e a correção é um título melhor. Acompanhar as mudanças de cor mostra se o painel está ficando mais honesto com o tempo. Um mês sem mudanças significa ou que os blocos estão bons, ou que as pessoas pararam de vir.

### Exemplo resolvido (TRB sintético)

Sam recusa uma captura de tela com hash divergente e a captura de novo.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX043 — Vaidade.** Por que rejeitar a contagem bruta de achados como KPI? *Rubrica:* 3 = recompensa o ruído; 2 = parcial; 1 = o melhor KPI; 0 = nada.
- **EX044 — Significado do hash.** O que um hash coincidente prova? *Rubrica:* 3 = inalterado desde o cálculo do hash; 2 = parcial; 1 = sistema seguro; 0 = nada.
- **EX045 — Campos de custódia.** Nomeie quatro campos de custódia. *Rubrica:* 3 = quem, o quê, quando, onde; 2 = três; 1 = um; 0 = nada.

### Síntese

A evidência recebe hash e atribuição; as métricas trazem denominadores.

### Continue estudando — capítulo 15 de 40

[← Capítulo 14 (rascunho)](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 (rascunho) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) desenhar as zonas do TRB; (2) impor matrizes de fluxo; (3) falhar fechado.

### 16.1 Zonas

Internet, DMZ, corporativa, vizinha dos pagamentos (restrita), avaliação. Uma zona agrupa sistemas que compartilham um nível de confiança e as mesmas regras sobre o que pode alcançá-los. A zona de internet do TRB não é confiável. A DMZ abriga o front-end público do banco, que precisa falar tanto com a internet quanto com o núcleo. A zona corporativa abriga os notebooks dos funcionários e o e-mail. A zona vizinha dos pagamentos é restrita porque faz fronteira com o gateway SWIFT e com o razão, e a zona de avaliação abriga a plataforma de testes. Os testadores leem um achado pelas zonas que ele atravessa. Um caminho da zona corporativa direto para a zona vizinha dos pagamentos é grave mesmo quando o sistema na outra ponta é apenas moderadamente sensível.

### 16.2 Fluxos

A matriz aprovada é a referência; o lab_flows sinaliza web→ledger-db.

```python
"""Lab 22: flag synthetic TRB data flows missing from the approved flow register."""
approved = {("branch-pc","core-api"), ("web","core-api"), ("core-api","ledger-db"), ("jump","ledger-db")}
seen = [("branch-pc","core-api"), ("web","core-api"), ("core-api","ledger-db"), ("web","ledger-db"), ("jump","ledger-db")]
for s, d in seen:
    print(f"{s:10} -> {d:10} {'approved' if (s,d) in approved else 'UNAPPROVED'}")
```

Execute com `python3 lab_flows.py`. Saída verificada:

```text
branch-pc  -> core-api   approved
web        -> core-api   approved
core-api   -> ledger-db  approved
web        -> ledger-db  UNAPPROVED
jump       -> ledger-db  approved
```

O registro é a declaração de intenção do banco, e o tráfego observado é a evidência do que de fato acontece. O laboratório compara os dois e relata os fluxos vistos, mas nunca aprovados. Um caminho direto da camada web para o banco de dados do razão contorna a API central, onde ficam a autorização e as verificações de entrada; assim, qualquer coisa que comprometa o servidor web poderia alcançar o razão sem essas verificações. O achado registra quando o fluxo foi observado, sua origem e seu destino e o fato de que nenhuma entrada do registro nem ticket de mudança o cobre.

### 16.3 Falhar fechado

Proxies e o TrackScope negam quando a política está ausente. Um controle que falha fechado bloqueia tráfego ou ações quando não consegue decidir, por exemplo porque seu arquivo de política está ausente, seu banco de dados está inalcançável ou uma regra está malformada. Um controle que falha aberto deixa tudo passar nesses casos, o que é conveniente durante uma indisponibilidade e desastroso se um atacante conseguir provocar a falha. Sam testa esse comportamento com segurança em staging. Ele renomeia o arquivo de política do TrackScope e confirma que a plataforma se recusa a iniciar um teste, em vez de rodar sem verificações de escopo. O teste do proxy funciona da mesma forma: com seu conjunto de regras indisponível, as requisições de saída precisam ser recusadas.

### 16.4 Conduítes

Regras de firewall com dono. Um conduíte é o caminho aprovado entre duas zonas, formado pelas regras de firewall, portas e protocolos que deixam uma zona falar com outra. Todo conduíte precisa de um dono, a pessoa que consegue explicar por que o caminho existe, aprovar mudanças e decidir se ele ainda é necessário. Regras sem dono se acumulam: uma porta aberta para uma migração anos atrás permanece porque ninguém sabe se removê-la vai quebrar algo. Quando Sam encontra tráfego usando um conduíte, a primeira pergunta não é se a regra o permite, mas quem é o dono da regra, porque só essa pessoa pode dizer se o tráfego é intencional.

### 16.5 Terceiros

Os processadores precisam de sua própria autorização. O TRB usa empresas externas para códigos únicos por SMS, processamento de cartões e hospedagem em nuvem. Os sistemas delas aparecem nos diagramas de arquitetura do TRB, mas o TRB não é dono deles e não pode autorizar ninguém a testá-los. Testar o serviço de um fornecedor geralmente exige a permissão escrita do fornecedor, sob seus próprios termos, e alguns provedores de nuvem publicam regras sobre o que os clientes podem testar em seu próprio tenant. Sam pode testar como os sistemas do TRB usam um serviço de terceiro, por exemplo se o banco valida as respostas do fornecedor, deixando em paz a infraestrutura do fornecedor, a menos que ele tenha dado seu aval.

### 16.6 Diagramas

Datados e com dono. Um diagrama de arquitetura é uma afirmação sobre como os sistemas estão conectados num momento específico, e um diagrama sem data convida testadores e auditores a confiar numa imagem que pode ter anos. Todo diagrama do TRB traz uma data, um dono e a versão do registro de fluxos que reflete. Antes de um engajamento, Sam confere que a data do diagrama é posterior à última mudança importante nos sistemas do escopo. Se não for, a primeira tarefa é confirmar o layout atual com o dono. Testar contra um diagrama desatualizado pode significar deixar passar caminhos novos ou, pior, sondar endereços que agora pertencem a algo fora do escopo.

### 16.7 Detectar mudanças de regras durante um engajamento

Os trechos da matriz recebem hash e são armazenados ao lado das ROE. Se a rede mudar no meio do engajamento, Sam compara as regras vivas com o hash e pausa se divergirem sem um ticket de mudança. O hash fixa o ambiente para o qual a autorização foi escrita. Se as regras mudam durante a janela, o teste pode agora alcançar lugares que o escopo presumia inalcançáveis, ou os resultados podem refletir uma configuração temporária em vez da normal. Pausar dá ao dono do conduíte tempo para confirmar que a mudança foi intencional. Se foi, o escopo é reconferido contra as novas regras. Se não foi, uma mudança inesperada é, ela mesma, algo que o banco precisa saber.

### 16.8 Contatar os donos dos conduítes

Cada conduíte lista um plantonista. Durante os testes, Sam manda mensagem ao plantonista do conduíte, e não a uma caixa geral de TI, quando as regras se comportam mal. Uma caixa geral é lida por quem estiver livre, talvez horas depois, e essa pessoa pode não conhecer o conduíte nem ter autoridade para mudá-lo. Durante uma janela de testes, os dois atrasos importam. Se uma regra de firewall bloqueia inesperadamente o teste, ou permite inesperadamente algo que não deveria, a pessoa dona desse conduíte pode decidir depressa se pausa, corrige a regra ou continua. O contato do plantão está listado no registro de fluxos ao lado do conduíte, para que os testadores não tenham de descobrir para quem ligar enquanto algo está dando errado.

### 16.9 Marcar os fluxos que precisam de autorização de terceiros

As matrizes de fluxo incluem uma coluna "precisa de autorização de terceiro?". Linhas com "sim" não podem ser testadas apenas sob as ROE do TRB. A coluna torna visível uma fronteira jurídica no lugar onde os testadores planejam seu trabalho. Um fluxo da API central do TRB para o endpoint do fornecedor de SMS é marcado com "sim". Sam pode observar o que o TRB envia e recebe, mas não pode sondar o endpoint do fornecedor em busca de fraquezas. A coluna é preenchida por quem registra o fluxo, e não pelos testadores, de modo que a decisão é tomada por pessoas que conhecem os contratos. Quando uma linha com "sim" importa para um engajamento, o plano inclui pedir a permissão do fornecedor ou registrar a lacuna no relatório.

### 16.10 Uma regra temporária sem expiração

Quando o lab_flows mostra web→ledger-db, a equipe de redes alega que a regra é temporária. Sam pede o ticket de mudança e a data de desativação. Nenhum dos dois existe. Temporário sem expiração vira o achado de processo gêmeo do F3. O achado técnico é o caminho aberto. O achado de processo é que uma regra pôde ser acrescentada como temporária sem nenhum mecanismo para removê-la. Corrigir só o primeiro fecharia esta regra e deixaria a próxima regra temporária com a mesma chance de persistir. O achado de processo recomenda que o fluxo de mudanças de firewall exija uma data de expiração para regras temporárias e alerte o dono uma semana antes dela.

### 16.11 Encaminhar um testador curioso ao programa do fornecedor

A coluna de terceiros com "sim" barrou uma varredura curiosa do fornecedor de SMS. Em vez disso, Sam enviou o link do bug bounty do fornecedor. Fronteiras ainda podem ser úteis. A curiosidade do colega era razoável, já que o endpoint do fornecedor parecia antigo e provavelmente tinha problemas. Varrê-lo a partir da rede do TRB sob as regras do TRB teria sido um teste não autorizado de outra empresa. O bug bounty do fornecedor define o que os pesquisadores podem testar, como e com que proteção jurídica. Segui-lo, com equipamento pessoal e em tempo pessoal, onde o programa permite, manteve o interesse legítimo e deixou o TRB de fora.

### 16.12 Tornar visíveis as datas de expiração

Os convites de calendário para as datas de desativação incluem o alias do CISO como participante opcional, para dar visibilidade. O convite é criado quando uma regra temporária é aprovada e cai na sua data de expiração. O dono é o participante obrigatório. O gabinete do CISO é opcional, o que significa que não se espera que aja, mas pode ver a lista completa de regras temporárias simplesmente abrindo o calendário. No dia, o dono remove a regra ou a prorroga com uma nova aprovação e uma nova data. Um convite sobre o qual ninguém age fica no calendário compartilhado como um evento passado sem ticket de mudança, o que torna a falha fácil de encontrar.

### 16.13 Ligar achados técnicos e de processo

Os achados de processo gêmeos se ligam ao F3 por um campo de id relacionado. Os conselhos veem juntas a dívida técnica e a de processo. Sem a ligação, os dois achados viajam separados. O técnico é corrigido rapidamente e some dos relatórios, enquanto o de processo espera num backlog de governança sem conexão visível com nenhuma exposição real. O campo de id relacionado os mantém juntos, de modo que um relatório ao conselho mostra que existiu um caminho aberto grave e por que ele pôde existir. Os revisores não fecham o achado técnico como resolvido na raiz enquanto seu gêmeo de processo ainda está aberto.

### 16.14 Plantão de arquitetura

O plantão de arquitetura usa um projetor e uma caneta vermelha. Conduítes sem dono são circulados até que um dono apareça no registro. Sam se recusa a agendar testes por conduítes sem dono, mesmo que a regra de firewall exista. A titularidade faz parte da autorização. Um conduíte circulado permanece no diagrama projetado de semana em semana, o que põe uma pressão pública e gentil sobre a equipe dona daquela regra de firewall. Recusar testar por conduítes sem dono não é obstrução. Sem um dono, não há ninguém que possa aceitar o risco do teste, pausá-lo ou explicar resultados inesperados; portanto, falta a precondição para o teste autorizado.

### Exemplo resolvido (TRB sintético)

O lab_flows imprime web -> ledger-db UNAPPROVED; Sam abre o F3.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX046 — Par não aprovado.** Qual fluxo está UNAPPROVED no laboratório? *Rubrica:* 3 = web→ledger-db; 2 = parcial; 1 = branch-pc→core-api; 0 = nada.
- **EX047 — Falhar fechado.** Com a política ausente, o TrackScope deve… *Rubrica:* 3 = negar os testes; 2 = parcial; 1 = permitir; 0 = nada.
- **EX048 — Terceiro.** As ROE do TRB sozinhas podem autorizar o teste de um processador de cartões? *Rubrica:* 3 = não; é preciso a autorização do processador; 2 = não; 1 = sim; 0 = nada.

### Síntese

Arquitetura é zonas, fluxos com dono e padrões que falham fechados.

### Continue estudando — capítulo 16 de 40

[← Capítulo 15 (rascunho)](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 (rascunho) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) dizer o que o TLS faz; (2) proteger evidências em repouso; (3) evitar inventar esquemas.

### 17.1 TLS em trânsito

Confidencialidade e integridade das sessões — não a AuthZ da aplicação. O TLS impede que alguém no caminho da rede leia ou altere silenciosamente o tráfego entre o navegador de um cliente e os servidores do TRB, e permite ao navegador verificar que está falando com o domínio real do banco. Ele não faz nada quanto ao que acontece depois que a requisição chega. Se a aplicação entrega ao cliente A o extrato do cliente B, ela o faz por uma conexão perfeitamente cifrada. Os achados mantêm as duas coisas separadas. Uma versão de protocolo desatualizada ou uma suíte de cifras fraca é um achado de transporte. Uma verificação de titularidade ausente é um achado de aplicação, e corrigir as configurações de TLS o deixaria intocado.

### 17.2 Em repouso

Cifragem do cofre de evidências e logs de acesso à chave. Cifrar o armazenamento do cofre protege contra alguém que obtenha os discos, os backups ou os snapshots sem passar pela aplicação, por exemplo um bucket de armazenamento mal configurado ou um disco descartado. Isso não protege contra quem consegue fazer login normalmente no cofre, porque a aplicação decifra os dados para essa pessoa. A chave que destrava o armazenamento é o verdadeiro ativo, e é por isso que seu uso é registrado separadamente do acesso aos arquivos. Uma rajada de eventos de uso da chave sem logins correspondentes no cofre sugeriria que alguém está lendo o armazenamento diretamente, que é o cenário que a cifragem em repouso existe para impedir.

### 17.3 Hashes

SHA-256 para a integridade das evidências, não para aulas sobre o desenho do armazenamento de senhas aqui. Um hash de uso geral como o SHA-256 é projetado para ser rápido, o que serve para tirar a impressão digital de arquivos de evidência: calcular o hash de um grande arquivo de capturas de tela leva segundos, e qualquer mudança aparece. A mesma velocidade o torna uma má escolha para armazenar senhas, onde a lentidão é uma defesa deliberada contra a adivinhação. O armazenamento de senhas precisa de funções dedicadas, como Argon2 ou bcrypt, um tema dos capítulos de identidade. Neste livro, o SHA-256 responde a uma pergunta, se este é o mesmo arquivo que foi capturado, e os testadores não devem presumir que um sistema é seguro porque ele usa um hash em algum lugar.

### 17.4 Antipadrões

Criptografia caseira para os tokens do TrackScope é proibida. Um dos primeiros protótipos do TrackScope construía tokens de sessão codificando em base64 o nome do testador e um carimbo de tempo e, depois, aplicando XOR do resultado com uma string fixa. Parecia ilegível e não oferecia proteção nenhuma. Quem visse dois tokens conseguiria recuperar a string fixa e forjar tokens novos. A regra desde então é usar a biblioteca de tokens assinados do framework ou um padrão consolidado, como JWTs assinados com uma chave mantida no cofre, e nunca inventar um algoritmo ou uma codificação. Quando Sam vê tokens opacos num sistema em teste, ele confere se mudam de forma previsível entre requisições, um sinal comum de esquemas caseiros.

### 17.5 Custódia de chaves

Chaves da plataforma em HSM ou cofre, com controle dual onde exigido. Quem detém uma chave de assinatura pode se passar pelo sistema que a usa. As chaves mais importantes do TRB, como a que assina os arquivos de escopo do TrackScope e a chave mestra do cofre, ficam num módulo de segurança de hardware. O HSM executa operações com a chave, mas não a entrega. Controle dual significa que operações sensíveis, como exportar uma chave ou mudar quem pode usá-la, precisam de duas pessoas autorizadas agindo juntas, para que nenhuma conta comprometida ou descuidada consiga fazê-las sozinha. Chaves menos críticas ficam no cofre de software, ainda com acesso registrado e donos nomeados.

### 17.6 Limites

A criptografia não detém administradores mal-intencionados autorizados com chaves válidas. Cifragem, assinatura e hashes protegem contra pessoas sem as chaves. Um administrador que detém legitimamente uma chave pode decifrar, assinar ou alterar dados, e a criptografia vai confirmar fielmente suas ações como válidas. Os controles contra pessoas de dentro são, portanto, procedimentais e detectivos: segregação de funções, controle dual para as operações mais sensíveis, logs que o administrador não consegue apagar e revisões do uso das chaves. Quando um relatório diz que os dados estão protegidos por cifragem, Sam acrescenta quem pode decifrá-los, porque é nessa lista que está o risco remanescente.

### 17.7 Testar a negação da exportação de chaves

As cerimônias de exportação no HSM para chaves da plataforma exigem duas pessoas e um código de motivo. O papel de estagiário de Sam não pode exportar. Ele testou a negação tentando uma exportação em staging e registrou o log de negação como evidência de que o controle funciona. O teste foi combinado com antecedência com o dono do HSM e rodado contra uma chave de staging que não protege nada real; assim, uma falha não teria tido consequências. O log de negação registra a conta, a operação pedida, o horário e o motivo da recusa. Um auditor pode se apoiar nesse registro em vez de numa declaração de que a política existe. Ele também dá um ponto de referência se o comportamento do controle algum dia mudar.

### 17.8 Tokens de plataforma de vida curta

Os tokens da plataforma expiram dentro da janela mais uma hora. Sam testa que tokens expirados não conseguem registrar achados. Tokens que persistem são achados contra a plataforma. Um token que sobrevive ao seu propósito é uma credencial esperando para ser roubada. A hora extra permite aos testadores terminar a redação depois que a janela fecha, e qualquer coisa mais longa só acrescenta exposição. O teste é direto. Sam guarda um token de uma janela encerrada, espera passar sua expiração e tenta criar um achado com ele. A plataforma precisa recusar, e a recusa precisa aparecer no log. Se a tentativa tiver sucesso, o achado nomeia o componente da plataforma que deixou de verificar a expiração.

### 17.9 Registrar as cerimônias de chaves

As notas das cerimônias listam os participantes e os ids das chaves, nunca material secreto. Sam arquiva as notas no cofre com a mesma retenção das evidências. Uma cerimônia de chaves é o evento formal em que uma chave é criada, rotacionada ou exportada sob controle dual. Suas notas mostram que o evento seguiu o procedimento, cobrindo quem estava presente, qual chave estava envolvida, qual código de motivo se aplicava e o que cada pessoa conferiu. Valores secretos nunca aparecem, nem parcialmente, porque as notas são lidas por auditores e revisores que não devem conseguir reconstruir uma chave. Manter as notas sob o cronograma de retenção das evidências significa que elas ficam disponíveis enquanto qualquer coisa assinada com aquela chave puder ser questionada.

### 17.10 Uma string com cara de chave bloqueada na CI

Sam tenta fazer commit de um blob base64 "temporário" que parece uma chave. A CI falha. Ele fica contente. A mensagem de falha leva ao documento da cerimônia de chaves. As salvaguardas devem ensinar, não só bloquear. O blob era um fixture de teste copiado de staging, e Sam pretendia removê-lo antes do merge. Um scanner de segredos no pipeline não confia em intenções. Uma vez que uma chave está no histórico de versões, ela está em todo clone do repositório, e apagá-la num commit posterior não a remove. O link da mensagem explicava como pedir uma chave de teste adequada, o que resolveu o problema imediato e mostrou o caminho correto para a próxima vez.

### 17.11 Quando tokens de vida curta incomodam as pessoas

A validade do token mais uma hora certa vez pegou um analista que escrevia tarde. Melhor uma nova autenticação do que um token num notebook roubado semanas depois. O analista perdeu alguns minutos de texto não salvo quando o token expirou no meio de uma frase. A resposta razoável foi corrigir o incômodo sem alongar a validade. O FindingsDesk agora salva os rascunhos localmente de forma cifrada e pede ao usuário que faça login de novo antes de enviar, em vez de descartar o trabalho. Controles de segurança que custam esforço às pessoas tendem a ser contornados; por isso, reduzir o custo sem enfraquecer o controle faz parte de projetá-lo.

### 17.12 Guardar as negações como evidência

Os logs de negação das cerimônias são retidos como evidência positiva para os examinadores que perguntam se os papéis de estagiário são impostos. Os examinadores frequentemente perguntam como o banco sabe que uma restrição é imposta, e não apenas escrita. Uma exportação de configuração mostra a configuração pretendida. Um registro datado de uma tentativa real sendo recusada mostra a configuração em vigor. Os logs de negação são arquivados com o controle a que se referem e renovados sempre que o software do HSM ou as definições de papéis mudam, para que a evidência nunca descreva uma versão do sistema mais antiga que a examinada.

### 17.13 Usar os registros de negação na integração

Os pacotes de evidência positiva de negação são reutilizados na primeira semana de integração. Os funcionários novos aprendem mais vendo um controle real recusar uma requisição real do que lendo que as chaves estão protegidas. Cada pacote junta a requisição, a recusa e a política que a causou e mostra como ler o log. Ele também define expectativas. Os estagiários novos veem no primeiro dia que seu papel não pode exportar chaves e que tentar deixa um registro, o que torna a regra concreta. Os pacotes contêm apenas dados de staging e são revisados antes de serem reutilizados.

### Exemplo resolvido (TRB sintético)

Sam rejeita um PR que cifra os arquivos de escopo com uma chave AES fixa no código-fonte.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX049 — TLS vs AuthZ.** O TLS corrige um IDOR? *Rubrica:* 3 = não, porque o TLS não corrige bugs de autorização; 2 = não, sem justificativa; 1 = sim; 0 = nada.
- **EX050 — Chave fixa no código.** Por que rejeitar chaves AES fixas no código-fonte? *Rubrica:* 3 = exposição da chave no repositório; sem controle dual; 2 = parcial; 1 = tudo bem; 0 = nada.
- **EX051 — Uso do hash aqui.** Para que servem os digests SHA-256 neste curso? *Rubrica:* 3 = integridade das evidências; 2 = parcial; 1 = cifrar o tráfego; 0 = nada.

### Síntese

Use criptografia padrão corretamente; nunca crie a sua própria para os segredos do engajamento.

### Continue estudando — capítulo 17 de 40

[← Capítulo 16 (rascunho)](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 (rascunho) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) formular perguntas respondíveis; (2) desenhar pequenos ensaios de purple team; (3) pré-registrar métricas.

### 18.1 Perguntas

"O controle X aumenta a detecção da T1566 em staging?" é melhor que "a segurança é boa?". Uma pergunta de pesquisa precisa nomear o que será medido, em que condições e contra qual comparação. Perguntar se a segurança é boa convida opiniões que não podem estar erradas e não podem guiar uma decisão. Perguntar se um novo filtro de e-mail aumenta a detecção da técnica de phishing T1566 no ambiente de staging, comparado com o filtro atual, nomeia o controle, a técnica, o lugar e a linha de base. Essa pergunta decide o desenho: um conjunto fixo de amostras de phishing, uma caixa de staging sob cada filtro e uma detecção ou falha registrada para cada amostra. Perguntas vagas produzem trabalho vago.

### 18.2 Desenho

Conjunto de teste fixo, ambiente registrado, plano de tamanho de amostra. Três escolhas decidem se um leitor posterior pode confiar no resultado. O conjunto de teste é escrito antes de qualquer ensaio rodar, para que ninguém possa descartar as amostras que fazem um controle parecer ruim. O ambiente é registrado: qual versão do filtro, qual configuração da caixa de correio, qual data. Sem esse registro, uma mudança posterior pode tornar o resultado irreproduzível. O tamanho da amostra é planejado para a precisão de que a decisão precisa, usando os mesmos métodos de intervalo do relato de detecção. Um desenho que pula qualquer um desses pontos ainda pode produzir um número, mas esse número não vai encerrar uma discussão.

### 18.3 Pré-registro

Escreva a métrica e o limiar antes de ver os resultados. As pessoas ajustam naturalmente o que conta como sucesso depois de ver os dados. Uma taxa de detecção de sessenta por cento pode ser chamada de sucesso ou de fracasso, dependendo do que a equipe esperava. O pré-registro escreve a métrica e o limiar numa nota datada antes do primeiro ensaio, por exemplo que o novo filtro tem sucesso se o limite inferior do seu intervalo de Wilson superar a taxa observada do filtro atual. Mudar o limiar depois é permitido, mas isso precisa ser rotulado como exploratório. A nota datada é o que impede que uma reinterpretação esperançosa seja apresentada como o plano original.

### 18.4 Ética

Dados de clientes estão fora de alcance; phishing sintético para funcionários precisa de aprovação do RH e do CISO. Pesquisas que usam mensagens ou contas reais de clientes estão fora dos métodos deste livro e dos contratos de teste do TRB. Phishing sintético enviado a funcionários reais também não é um teste técnico comum. Ele envolve pessoas que podem se sentir enganadas e pode afetar a confiança nas mensagens de segurança. Qualquer ensaio desse tipo precisa, portanto, de aprovação do RH e do CISO que declare a finalidade, a população, as mensagens, a possibilidade de recusa quando viável e como os resultados serão relatados sem nomear indivíduos. Curiosidade técnica não é aprovação.

### 18.5 Resultados negativos

Publique internamente; eles evitam ideias fracassadas repetidas. Um ensaio que mostra que um controle não fez diferença mensurável é tão útil quanto um que mostra que fez, porque impede a próxima equipe de gastar mais um trimestre na mesma ideia. Resultados negativos também calibram as expectativas. Se três campanhas de conscientização falharam, cada uma, em mover as taxas de clique nos exercícios de staging, a próxima proposta de uma quarta campanha enfrenta uma barra mais alta. Publicação interna significa um relato curto no quadro de ensaios, com a métrica pré-registrada, o resultado e uma frase sobre o que não tentar de novo. Esconder resultados negativos faz a organização reaprender a mesma lição.

### 18.6 Limites

Staging ≠ produção; declare as ameaças à validade. O staging é mais silencioso, mais limpo e monitorado de forma diferente da produção. Uma taxa de detecção medida ali pode ser mais alta porque o tráfego é mais leve, ou mais baixa porque a produção tem sensores extras. Ameaças à validade são os motivos pelos quais um resultado pode não se transferir: a amostra era pequena demais, o kit de phishing estava desatualizado, o filtro estava mal configurado, o SOC foi avisado de que um ensaio estava rodando. Nomeá-las não enfraquece o relatório. Isso diz a quem decide o quanto pode se apoiar no achado. Um resultado sem limites declarados é aquele de que se deve desconfiar.

### 18.7 Relatar um resultado negativo

Os resultados negativos usam o mesmo modelo que os positivos. A nota de Sam "a fadiga de prompts de MFA não melhorou a detecção da T1566 com n=40" impediu um segundo ensaio idêntico no trimestre seguinte. O modelo obriga aos mesmos campos: pergunta, desenho, limiar pré-registrado, resultado, limites. Usar um formato diferente e apologético para resultados negativos os faz parecer falhas da equipe, e não achados sobre um controle. O ensaio de fadiga mostrou que acrescentar mais prompts de MFA não aumentou a detecção do conjunto de phishing, o que redirecionou a proposta seguinte para autenticadores resistentes a phishing. Sem o relato, a mesma ideia da fadiga teria voltado com um novo patrocinador.

### 18.8 Um quadro interno de ensaios

Um quadro público (interno) mostra os ensaios pré-registrados e seu status. Ensaios duplicados são rejeitados num relance. O quadro lista a pergunta, o dono, o tamanho de amostra planejado e se o ensaio está planejado, em andamento ou relatado. Quem propõe um novo ensaio pesquisa nele primeiro. Duplicatas são comuns quando as equipes trabalham em paralelo e cada uma acredita que sua ideia é original. Rejeitar uma duplicata cedo poupa uma turma de funcionários ou um bloco de tempo de staging e, muitas vezes, leva o proponente a se juntar ao ensaio existente. O quadro é chato de propósito. Sua tarefa é tornar a repetição visível.

### 18.9 Preferir intervalos a uma falsa significância

Sam evita declarar significância sem um plano. A maioria dos ensaios de purple team no TRB é descritiva, com intervalos, e não pseudoensaios clínicos. Um p-valor calculado depois do fato a partir de uma pequena amostra de conveniência não significa o que as pessoas pensam. Ele pode parecer decisivo quando a incerteza real é grande. O padrão do TRB é, portanto, relatar contagens e intervalos de Wilson e reservar as afirmações formais de significância para os raros ensaios desenhados para elas, com um plano de tamanho de amostra. O relato descritivo não é uma forma menor de evidência. Ele é honesto sobre o que um exercício de purple team de quarenta ensaios consegue sustentar.

### 18.10 Um ensaio de conscientização fracassado ainda merece um relato

Um ensaio pré-registrado sobre e-mails de conscientização não atinge seu limiar. Sam o relata mesmo assim. A reunião de orçamento do trimestre seguinte cita o resultado negativo para evitar comprar de novo o mesmo pacote de conteúdo. O fornecedor do pacote de conteúdo tinha estudos de caso promissores de outros setores. O ensaio do TRB, com um conjunto fixo de phishing e um limiar de detecção pré-registrado, não atingiu esse limiar. Relatá-lo evitou tanto um enterro silencioso quanto uma discussão acalorada baseada em anedotas. As reuniões de orçamento preferem um resultado datado à sensação de que o treinamento "pareceu útil". O fornecedor foi convidado a propor um pacote diferente para um novo ensaio, em vez de revender o mesmo.

### 18.11 Juntar-se a um ensaio existente em vez de duplicá-lo

O quadro de registro rejeitou em um minuto o título de um ensaio duplicado. O autor se juntou ao ensaio existente como colaborador, em vez de desperdiçar uma turma. A duplicata tinha uma redação ligeiramente diferente, mas o mesmo controle, a mesma técnica e a mesma população de staging. Rodar os dois teria dividido os voluntários disponíveis e deixado cada ensaio com poder estatístico insuficiente. Entrar como colaborador significou que o segundo autor contribuiu com amostras e tempo de revisão, ganhou a coautoria do relato e ainda respondeu à sua pergunta de fundo. O valor do quadro não é rejeitar por rejeitar. É redirecionar o esforço para um resultado capaz de decidir alguma coisa.

### 18.12 Celebrar resultados negativos

Os resultados negativos ganham um ícone de rolha de champanhe no quadro — celebração do aprendizado, não do fracasso. A cultura decide se as pessoas registram resultados negativos ou os escondem. Uma pequena recompensa visível, mesmo um ícone bobo, sinaliza que a organização quer o aprendizado. O ícone só aparece quando o relato está completo, de modo que não pode ser ganho deixando de terminar. As equipes que publicam resultados negativos são agradecidas no resumo trimestral de pesquisa ao lado das que publicam positivos. Ao longo de um ano, a mistura de rolhas e vistos comuns no quadro mostra se a cultura está funcionando.

### 18.13 Ícones não substituem relatos

Os ícones de rolha de champanhe são opcionais; o relato não é. Sam rejeita ícones sem texto. Um ícone sem um relato vinculado deixaria uma equipe reivindicar crédito por um resultado negativo com o qual ninguém consegue aprender. A regra do quadro é que o ícone só é exibido quando os campos do relato estão preenchidos: pergunta, desenho, limiar, resultado, limites. Rejeitar um ícone solto é ocasional e um pouco constrangedor, e mantém o quadro útil. Uma celebração que não deixa um registro reutilizável é só decoração.

### 18.14 Um linter para celebrações vazias

Ícones sem texto são removidos pelo linter de markdown do quadro. O linter é uma verificação curta que roda quando uma entrada do quadro é salva. Se encontra um ícone de rolha e campos de relato vazios, ele remove o ícone e deixa um comentário pedindo o texto. A automação importa aqui porque Sam não consegue revisar toda edição. O linter também impede que colegas bem-intencionados acrescentem ícones a entradas antigas que nunca tiveram relatos, o que inventaria uma história que o quadro não tem.

### Exemplo resolvido (TRB sintético)

Sam pré-registra: sucesso se a detecção for ≥80% em 50 e-mails sintéticos no estilo T1566, com limite inferior de Wilson ≥0,7.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX052 — Pergunta ruim.** Por que "a segurança é boa?" é uma pergunta de pesquisa ruim? *Rubrica:* 3 = não é mensurável/específica; 2 = parcial; 1 = tudo bem; 0 = nada.
- **EX053 — Pré-registro.** O que deve ser escrito antes dos resultados? *Rubrica:* 3 = métrica e limiar (e desenho); 2 = parcial; 1 = vago; 0 = nada.
- **EX054 — Phishing com funcionários.** Que aprovações são necessárias antes de um phishing simulado? *Rubrica:* 3 = CISO/RH (e ROE); 2 = uma; 1 = vago; 0 = nada.

### Síntese

Perguntas respondíveis, métricas pré-registradas e ética antes dos ensaios de purple team.

### Continue estudando — capítulo 18 de 40

[← Capítulo 17 (rascunho)](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 (rascunho) →](#ch-19)

<a id="ch-19"></a>

## Capítulo 19 — Escopo e teoria da segurança ofensiva autorizada

### Objetivos de aprendizagem

Você vai (1) comparar os tipos de avaliação do SP 800-115; (2) mapear as etapas do PTES; (3) situar os testes orientados por ameaças.

### 19.1 Tipos do SP 800-115

Revisões, avaliações de vulnerabilidades, red teaming — profundidades e modelos de permissão diferentes. O NIST SP 800-115 distingue vários tipos de teste de segurança. Uma revisão examina desenhos, configurações ou código sem atacar um sistema vivo. Uma avaliação de vulnerabilidades procura fraquezas conhecidas com ferramentas e verificações manuais leves, geralmente com permissão ampla e pouca furtividade. O red teaming emula um adversário com objetivos específicos, muitas vezes sob regras mais rígidas quanto à detecção e ao impacto. Confundir os nomes leva a expectativas erradas. Uma avaliação web trimestral não consegue responder se um atacante determinado alcançaria o razão sem ser notado, e um exercício orientado por ameaças não consegue substituir as verificações regulares de regressão no portal do cliente.

### 19.2 PTES

Do pré-engajamento ao relatório, como nomes de etapas compartilhados. O Penetration Testing Execution Standard nomeia as etapas que a maioria dos testes autorizados compartilha: pré-engajamento, coleta de inteligência, modelagem de ameaças, análise de vulnerabilidades, exploração, pós-exploração e relatório. O TRB usa esses nomes para que planejadores, testadores e clientes queiram dizer a mesma coisa com cada etapa. O pré-engajamento é onde o escopo e as regras são assinados. O relatório é onde os achados são escritos para os donos, não onde acontecem testes novos. Usar nomes de etapas compartilhados também torna as lacunas óbvias. Um engajamento que salta da coleta de inteligência para o relatório sem análise pulou o trabalho que transforma observações em achados.

### 19.3 Orientados por ameaças

O TIBER-EU e o CBEST usam inteligência para moldar cenários para entidades financeiras; o TRB os estuda mesmo quando faz testes mais leves. Os exercícios orientados por ameaças partem de quem provavelmente atacaria esse tipo de instituição e do que essas pessoas geralmente querem e, então, constroem cenários em torno desse quadro. TIBER-EU e CBEST são frameworks que os bancos usam para esses exercícios sob supervisão regulatória. Os testes web comuns do TRB são mais leves e mais frequentes, mas a ideia orientada por ameaças ainda os molda. As reuniões de escopo perguntam quais técnicas os relatórios atuais de ameaças destacam para bancos de varejo, e os cartões de método do trimestre favorecem essas técnicas. Estudar os frameworks também mantém a equipe honesta sobre o que um teste leve não pode afirmar.

### 19.4 Teoria da mudança

Os testes informam decisões de risco; eles não criam segurança por si sós. Um engajamento bem-sucedido produz evidências que um dono de risco pode usar: uma fraqueza existe, ela é alcançável sob condições declaradas, e corrigi-la removeria esse caminho. A segurança só melhora se alguém então decidir corrigi-la, aceitá-la com um controle compensatório ou mudar o sistema para que o caminho deixe de importar. Testes que produzem achados sem dono são jornalismo caro. Por isso, o TrackScope exige um dono e uma data-limite antes que um achado saia de rascunho, e o PulseMap acompanha a idade dos achados, para que os riscos conhecidos, mas ignorados, continuem visíveis.

### 19.5 Limites da garantia

Um teste limpo é uma garantia limitada no tempo, não um certificado de garantia. Um teste que não encontra nada grave mostra que, com os métodos usados, contra os sistemas do escopo, durante aquela janela, os testadores não demonstraram uma fraqueza grave. Ele não mostra que não existe fraqueza, que nenhuma vai aparecer na semana seguinte quando uma nova funcionalidade for lançada, nem que um adversário diferente, com métodos diferentes, falharia. Os relatórios declaram esse limite explicitamente. O TRB proíbe frases que transformam um teste limpo numa garantia, porque essas frases viram passivos quando o próximo incidente acontece.

### 19.6 Papel da plataforma

O TrackScope codifica a teoria como regras de negação executáveis. As ideias sobre autorização, escopo e falha fechada só protegem o banco quando rodam como código. O TrackScope se recusa a iniciar um teste sem um arquivo de escopo assinado, recusa alvos fora desse arquivo, recusa métodos que as regras marcam como proibidos e para quando sua política não pode ser carregada. Codificar a teoria significa que um testador cansado à meia-noite recebe a mesma recusa que um cuidadoso ao meio-dia. Significa também que as melhorias na teoria, como uma nova exclusão, se tornam melhorias em todo engajamento no momento em que o arquivo de escopo é atualizado.

### 19.7 Declarar o que cada tipo de teste não pode afirmar

O catálogo de avaliações inclui o que cada tipo não pode afirmar. Testes web anuais não podem afirmar cobertura orientada por ameaças; exercícios orientados por ameaças não podem afirmar cobertura de regressão trimestral. Sam cita a linha do que não se pode afirmar nas reuniões de abertura. Clientes e patrocinadores internos naturalmente esticam o que compraram. Depois de um teste web limpo, alguém pergunta se o banco está a salvo de atores estatais. Depois de um exercício orientado por ameaças, alguém pergunta por que um simples bug de regressão chegou à produção. A linha do que não se pode afirmar, lida em voz alta na abertura e impressa no relatório, responde às duas perguntas antes que virem discussões. Ela também define o valor do catálogo. Os compradores sabem o que estão e o que não estão adquirindo.

### 19.8 Frases aprovadas para relatórios

As frases aprovadas para relatórios incluem "garantia limitada no tempo" e proíbem "seguro com garantia". O linter de Sam sinaliza as frases proibidas. Quem escreve sob prazo busca uma linguagem forte. Uma biblioteca de frases aprovadas lhes dá uma linguagem forte o suficiente que o jurídico e o CISO já aceitaram. As frases proibidas são bloqueadas no pipeline de relatórios com uma mensagem que sugere uma substituição. O linter é rude de propósito. É mais fácil discutir com uma substituição sugerida do que notar uma frase perigosa num rascunho longo à meia-noite.

### 19.9 Responder a questionários a partir do catálogo

As respostas a questionários citam o catálogo. Sam impede que colegas respondam "fazemos pentest em tudo" quando o SWIFT está excluído. Questionários de seguradoras e de fornecedores fazem perguntas amplas de sim ou não que não correspondem a como os testes de fato funcionam. Responder de memória produz afirmações exageradas. Responder a partir do catálogo produz frases como: avaliações web autorizadas trimestrais das aplicações voltadas para a internet, exercício orientado por ameaças concluído pela última vez no ano declarado, gateway de pagamentos excluído dos testes comuns. Essas frases se sustentam numa disputa de sinistro. "Fazemos pentest em tudo" não se sustenta.

### 19.10 Uma resposta honesta a uma seguradora

Um questionário de seguradora pergunta "Vocês fazem red teaming?". Sam responde com o catálogo: testes web trimestrais, sim; o último exercício completo orientado por ameaças foi feito em 20XX; o SWIFT é excluído dos testes comuns. A honestidade na caixa de seleção vence a bravata. O formulário queria um sim ou um não. A resposta honesta é um parágrafo curto, que a seguradora aceitou depois de uma ligação de esclarecimento. Um sim na caixa de seleção teria sugerido um programa de red team atual e abrangente que o TRB não tinha naquele ano. Quando um incidente depois envolveu um sistema vizinho dos pagamentos, a resposta escrita mostrou que os testes comuns nunca tinham afirmado cobri-lo, o que importou mais do que parecer assertivo no formulário.

### 19.11 Substituir uma frase proibida

O linter de garantia reprovou um relatório por "totalmente seguro após a remediação". A substituição de Sam: "risco residual aceito para o F3 até 1º de dezembro, com administração compensatória apenas via jump host". A frase proibida prometia um estado que nenhum teste pode provar. A substituição nomeia o achado, a decisão, a data e o controle compensatório. Um dono pode agir com base nela, um auditor pode conferi-la e um incidente posterior pode ser comparado com ela. Escrever a frase específica levou mais tempo que o slogan, e esse é o ponto. A precisão é o produto.

### 19.12 Ler em voz alta as linhas do que não se pode afirmar

As linhas do catálogo sobre o que não se pode afirmar são lidas em voz alta na abertura; murmurar é corrigido. Ler em voz alta obriga cada pessoa na sala a ouvir o limite, incluindo os patrocinadores que pulam o material escrito. Murmurar é corrigido porque um limite ouvido pela metade é como começam as afirmações exageradas. A prática parece um pouco formal nas primeiras vezes e depois se torna normal. Aberturas que a pulam tendem a produzir as mesmas discussões de esclarecimento uma semana depois; por isso, a equipe trata a leitura como parte do início do engajamento, não como um teatro opcional.

### 19.13 Recomeçar uma leitura murmurada

Murmurar na abertura faz a leitura do que não se pode afirmar recomeçar. Clareza acima do conforto. Um recomeço é levemente constrangedor e, por isso, eficaz. Quem lê desacelera, a sala presta atenção e o limite é de fato ouvido. Sam mantém o tom leve. O objetivo é o entendimento compartilhado, não a punição. Depois de alguns recomeços no início do ano, as leituras murmuradas ficaram raras, que é o resultado que a regra existe para produzir. O recomeço também dá a quem chegou atrasado uma segunda chance de ouvir o limite. As aberturas frequentemente começam enquanto alguém ainda está entrando na chamada, e a primeira leitura murmurada é justamente a que essa pessoa teria ouvido. Esperar por uma leitura clara custa menos do que explicar a mesma fronteira de novo no meio do engajamento.

### 19.14 Acompanhar as aberturas murmuradas

Os recomeços da leitura do que não se pode afirmar são registrados como uma métrica divertida de murmúrio. O registro é uma contagem bem-humorada na wiki da equipe, não uma nota de desempenho. Uma contagem em alta sugeriria que as aberturas estão apressadas ou que funcionários novos não viram a prática. Uma contagem em queda sugere que o hábito pegou. Tratar a métrica como diversão impede que ela vire algo que as pessoas manipulam lendo depressa demais para evitar um recomeço. O sinal útil é a tendência ao longo dos trimestres, não uma abertura isolada.

### Exemplo resolvido (TRB sintético)

A nota de aula de Sam: "Cenários no estilo CBEST precisam de inteligência + ROE + objetivos de detecção; nosso teste web trimestral é mais estreito e ainda assim valioso."

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX055 — Etapa.** Onde o PTES coloca o relatório? *Rubrica:* 3 = etapa final, depois do trabalho técnico; 2 = cedo; 1 = nunca; 0 = nada.
- **EX056 — Par orientado por ameaças.** Nomeie os frameworks orientados por ameaças da UE e do Reino Unido citados. *Rubrica:* 3 = TIBER-EU e CBEST; 2 = um; 1 = errado; 0 = nada.
- **EX057 — Certificado de garantia.** Por que um teste limpo não é um certificado de garantia? *Rubrica:* 3 = limitado no tempo / limites de cobertura / mudanças; 2 = parcial; 1 = é sim; 0 = nada.

### Síntese

A teoria liga os tipos de avaliação às permissões, às etapas e a afirmações de garantia humildes.

### Continue estudando — capítulo 19 de 40

[← Capítulo 18 (rascunho)](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 (rascunho) →](#ch-20)

<a id="ch-20"></a>

## Capítulo 20 — Casos fundamentais

### Objetivos de aprendizagem

Você vai (1) analisar casos sintéticos do TRB; (2) separar fato de palpite; (3) escalar riscos aos pagamentos.

### 20.1 Pacote do caso

Trecho das ROE, logs, rascunho de achados, relato de um funcionário sobre reutilização de senha. Um caso fundamental dá aos alunos um mundo fechado sobre o qual podem raciocinar sem inventar fatos. O pacote contém apenas o que a equipe realmente teria: uma página das regras de engajamento, um recorte de logs da VPN e da aplicação, um rascunho de achado e um relato curto de um funcionário de que uma senha foi reutilizada. Nada além disso vale. Os alunos precisam rotular o que sabem, o que supõem e o que fariam em seguida, o que treina o hábito de não preencher lacunas com ficção confiante. O mesmo pacote é reutilizado entre turmas, para que os facilitadores possam comparar como grupos diferentes lidam com a mesma evidência.

### 20.2 Rótulos

Linhas de Fato / Palpite / Ação. Toda afirmação numa discussão de caso é rotulada como um Fato tirado do pacote, um Palpite que vai além dele ou uma Ação que a equipe tomaria em seguida. Os Fatos podem ser conferidos contra o pacote. Os Palpites são permitidos, mas limitados, porque uma lista ilimitada de palpites vira uma história de atribuição. As Ações precisam ser permitidas pelas regras de engajamento. Os rótulos desaceleram a conversa o suficiente para impedir que uma sala deslize para uma narrativa não verificada. Quando duas pessoas discordam, elas primeiro conferem se estão discutindo um Fato ou um Palpite.

### 20.3 Escalonamento

Possível impacto na integridade dos pagamentos → CISO no mesmo dia. Os critérios de escalonamento são escritos antes de o caso começar, para que a urgência não seja negociada no calor da discussão. No TRB, qualquer coisa que possa afetar a integridade dos pagamentos, a movimentação de fundos de clientes ou a disponibilidade do internet banking é escalada ao CISO no mesmo dia, mesmo que a evidência ainda esteja incompleta. O pacote do caso inclui o relato de um funcionário sobre reutilização de senha num jump host vizinho dos pagamentos, o que atinge essa barra. Os alunos praticam a escrita da nota de escalonamento: o que foi observado, o que ainda é desconhecido, o que foi interrompido e que decisão é necessária. Praticar a nota num caso sintético torna a real mais rápida.

### 20.4 Fora do escopo

O conteúdo do e-mail pessoal permanece intocado. O relato do funcionário menciona que a senha reutilizada também era usada numa caixa de e-mail pessoal. Esse detalhe é uma tentação. Ler a caixa pessoal poderia revelar mais sobre a pessoa, e isso está fora de toda fronteira profissional e jurídica do engajamento. O caso ensina a recusa explicitamente. Os alunos podem recomendar que o funcionário troque suas senhas pessoais e podem oferecer orientação, mas não podem pedir nem aceitar acesso a contas pessoais. Escrever essa recusa nas linhas de Ação faz parte de um relato de caso aprovado.

### 20.5 ATT&CK

Etiquete as técnicas para a caça do SOC. Quando o caso produz um achado, os alunos o etiquetam com as técnicas do ATT&CK que ele demonstra, como Valid Accounts para a senha reutilizada no jump host. As etiquetas dão ao SOC um ponto de partida para caçadas: procurar outros logins com aquela conta, ou movimento lateral a partir daquele host depois do login. As etiquetas não são decoração. Um achado sem etiqueta de técnica é mais difícil de transformar em trabalho de detecção. Os facilitadores conferem que as etiquetas correspondem à evidência, e não a uma técnica favorita que o aluno queria mencionar.

### 20.6 Sem culpa

Foco nos sistemas e nos processos. O funcionário que reutilizou uma senha cometeu um erro, e as perguntas úteis são sobre o sistema que permitiu que esse erro importasse: uma senha de administrador compartilhada ainda estava em uso, o jump host aceitava autenticação por senha, os processos de desligamento e de rotação a deixaram passar? Um relato sem culpa nomeia a pessoa apenas na medida em que o pacote exige e gasta sua energia nos controles. Relatos centrados na culpa produzem colegas na defensiva e sistemas inalterados. Os facilitadores redirecionam qualquer linha de Ação que comece punindo alguém para uma Ação que mude um controle.

### 20.7 Proibir o drama sem horário

Os facilitadores proíbem adjetivos de linha do tempo como "de repente", a menos que exista um carimbo de tempo. As notas de caso de Sam agora começam com os horários UTC dos logs e só depois trazem a narrativa. As linhas de Palpite não podem trazer carimbos de tempo fingindo ser fatos. Palavras como de repente, imediatamente e por fim contrabandeiam uma linha do tempo para a história sem evidência. Uma linha de log às 21:14 e outra às 21:47 sustentam um intervalo de trinta e três minutos. "De repente" sustenta o que quer que o falante sinta. Começar pelos carimbos de tempo obriga a narrativa a se ajustar à evidência. Um Palpite sobre o que aconteceu no intervalo continua sendo um Palpite, sem um relógio falso preso a ele.

### 20.8 Declarar o fuso horário dos logs na primeira página

Todo pacote de caso declara o fuso horário das linhas de log na primeira página. Sam certa vez perdeu uma hora por causa de um UTC silencioso; a linha de capa evita isso. Linhas de log que parecem locais e na verdade são UTC, ou o contrário, criam lacunas fantasmas e eventos sobrepostos que mandam a equipe pelo caminho errado. A linha de capa é chata e inegociável: todos os carimbos de tempo deste pacote estão em UTC, ou todos estão em America/New_York. Quando duas fontes de log usam fusos diferentes, os dois são declarados e um deles é convertido numa nota de trabalho, nunca em silêncio na cabeça de alguém.

### 20.9 Um orçamento de três palpites

Cada caso pode trazer no máximo três linhas de Palpite. Os palpites excedentes viram dever de casa para reunir fatos. Palpites ilimitados transformam um caso em escrita criativa. Três palpites bastam para capturar as incertezas mais importantes sem deixar a discussão morar nelas. Quando aparece um quarto palpite, o facilitador pergunta que Fato o resolveria e o atribui como dever de casa: qual log, qual dono, qual consulta. O orçamento treina as pessoas a perceber quando estão inventando e a preferir uma pequena investigação a uma grande história.

### 20.10 Remover uma atribuição não merecida

Noite de caso: uma linha de Palpite sobre "APT29" é removida por falta de evidência. A sala resmunga e depois escreve linhas de Fato melhores sobre os logs da VPN. O teatro da atribuição vicia; o sino ajuda. Nomear um ator conhecido parece expertise. Sem ferramentas, infraestrutura ou relatórios de inteligência correspondentes no pacote, é um Palpite que rouba a atenção do que os logs de fato mostram. Removê-lo é impopular por um minuto e produtivo depois. Os Fatos da VPN que o substituem geralmente importam mais para a próxima ação do banco do que qualquer nome de ator importaria.

### 20.11 Dois fatos em vez de um palpite de APT

O orçamento de palpites obrigou uma equipe a substituir um palpite de APT por dois fatos dos logs da VPN. O caso ficou menos cinematográfico e mais verdadeiro. Os dois Fatos eram que a conta fez login a partir de uma nova impressão digital de dispositivo e que a mesma conta alcançou o jump host em quatro minutos. Esses Fatos sustentam Ações: desativar a conta, revisar outros logins a partir daquele dispositivo, verificar se o MFA foi satisfeito. O Palpite de APT sustentava apenas uma sensação de importância. Menos cinematográfico é o padrão de que o banco precisa quando há dinheiro real e clientes reais envolvidos.

### 20.12 ISO 8601 na capa

As linhas de capa dos carimbos de tempo usam ISO 8601 com deslocamento; "manhã" é proibido. Manhã significa horas diferentes para leitores diferentes e desaparece sob os fusos horários. Um carimbo de tempo ISO 8601 com deslocamento, como 2026-03-04T21:14:00Z, significa um único momento. A proibição de palavras de tempo vagas vale tanto para as linhas de Palpite e de Ação quanto para os Fatos. Se um aluno não sabe o horário, ele escreve que não sabe, o que é em si uma informação útil.

Se um aluno sabe apenas que algo aconteceu de manhã, a linha de Fato diz que o horário é desconhecido, e a linha de Palpite, se houver, fica claramente separada. Fingir precisão é pior do que admitir uma lacuna.

### 20.13 Conferir as linhas de capa na CI

As linhas de capa em ISO 8601 são validadas por uma regex na CI dos pacotes de caso. Os pacotes ficam num pequeno repositório. Uma verificação de integração contínua faz o build falhar quando a primeira página não tem uma linha correspondente ao padrão de carimbo de tempo, ou quando palavras proibidas como manhã aparecem nas linhas de Fato. A verificação é mesquinha de propósito. Os facilitadores devem gastar sua atenção na qualidade do raciocínio, não em pegar desvios de formatação. A automação cuida da correção chata.

Quando a verificação falha, a mensagem de erro mostra o padrão esperado da linha de capa e a lista de palavras proibidas, para que os autores possam corrigir o pacote sem perguntar a um facilitador.

### 20.14 Oficinas de linhas de Fato

As oficinas de linhas de Fato proíbem adjetivos por vinte minutos. Só substantivos, verbos, números e carimbos de tempo. A restrição parece artificial e produz os pacotes de caso mais limpos do período. Sam guarda um pacote-troféu do ano passado como padrão. A restrição tem jeito de jogo e reinicia hábitos formados por livros de suspense e filmes de incidentes. Depois de vinte minutos, o grupo geralmente produz um pacote com base no qual um analista do turno da noite poderia agir sem perguntar o que os adjetivos significavam. O pacote-troféu é reutilizado como a barra para as turmas seguintes.

### Exemplo resolvido (TRB sintético)

Sam escala a senha da VPN reutilizada no e-mail pessoal; redefine as credenciais do TRB; não lê o e-mail pessoal.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX058 — Fato vs palpite.** Rotule: "um funcionário relatou reutilização" vs "um Estado-nação tem o hash". *Rubrica:* 3 = fato vs palpite; 2 = parcial; 1 = ambos fatos; 0 = nada.
- **EX059 — E-mail pessoal.** Por que não ler o e-mail pessoal do funcionário? *Rubrica:* 3 = fora do escopo/privacidade; 2 = parcial; 1 = deveria ler; 0 = nada.
- **EX060 — Gatilho de escalonamento.** O que dispara aqui o escalonamento ao CISO no mesmo dia? *Rubrica:* 3 = reutilização de credencial que arrisca acesso ao banco/pagamentos; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Os casos recompensam o raciocínio rotulado e o escalonamento rápido dos riscos vizinhos dos pagamentos.

### Continue estudando — capítulo 20 de 40

[← Capítulo 19 (rascunho)](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 (rascunho) →](#ch-21)

<a id="ch-21"></a>

## Capítulo 21 — Modelos de sistemas

### Objetivos de aprendizagem

Você vai (1) modelar o internet banking; (2) listar os pontos de entrada; (3) registrar as premissas.

### 21.1 Elementos

Atores, pontos de entrada, armazenamentos, zonas de confiança, processadores externos. Um modelo de sistema para testes autorizados é um mapa do que pode ser alcançado e do que precisa ser protegido, não uma arquitetura corporativa completa. Atores são pessoas ou serviços que iniciam ações: clientes, funcionários, rotinas em lote, testadores. Pontos de entrada são onde esses atores encontram o sistema: a aplicação web, a API móvel, a VPN dos funcionários. Armazenamentos guardam dados que importam: o banco de dados de clientes, o cofre de evidências. Zonas de confiança agrupam componentes que compartilham um nível de exposição. Processadores externos ficam fora do controle do TRB. Nomear cada elemento antes de testar evita que a equipe descubra no meio do engajamento que um par de lote esquecido consegue alcançar o razão.

### 21.2 Pontos de entrada

Web, API móvel, VPN dos funcionários, pares de lote. Cada ponto de entrada tem usuários diferentes, autenticação diferente e formas diferentes de dar errado. A aplicação web pública fica de frente para qualquer pessoa na internet. A API móvel pode compartilhar backends com a aplicação web, mas usar tokens diferentes. A VPN dos funcionários aproxima os administradores dos sistemas internos. Os pares de lote são sistemas de outras instituições que trocam arquivos num cronograma. Um modelo que lista apenas a aplicação web vai deixar passar achados que só aparecem na API móvel ou só depois do login na VPN. Sam confere o log de tickets de mudança em busca de novos pontos de entrada antes de cada engajamento.

### 21.3 Premissas

"O staging espelha a AuthZ da produção" precisa ser validado. Os modelos estão cheios de premissas, e as não validadas são onde os achados se escondem. As equipes frequentemente presumem que o staging usa as mesmas regras de autorização que a produção, que um deep link móvel reutiliza as verificações de sessão da web ou que um callback de um processador de pagamentos é autenticado. Cada premissa é escrita num post-it e marcada como Aberta até que alguém a confira. Uma premissa Aberta na abertura vira uma frase de risco residual no plano: o teste pode deixar passar fraquezas que só existem onde a premissa falha. Fechar premissas faz parte da preparação, não é uma tarefa paralela.

### 21.4 Fluxos de dados

Os caminhos de dados pessoais de clientes dirigem a minimização. O modelo marca todo caminho que transporta dados pessoais de clientes: do navegador para a camada web, da camada web para o armazenamento de clientes, do armazenamento para uma extração de relatórios. Esses caminhos decidem onde as regras de minimização se aplicam durante os testes. Um caminho que nunca transporta dados pessoais pode ser exercitado com mais liberdade, com tráfego sintético. Um caminho que os transporta exige a regra de prova, e não de volume, e um manuseio cuidadoso das evidências. Desenhar os caminhos também revela surpresas, como um site de marketing que posta na API central e, portanto, num armazenamento de dados pessoais.

### 21.5 Exclusões

O gateway SWIFT é omitido quando está fora do escopo. As exclusões precisam aparecer no modelo com a mesma clareza das inclusões. Deixar o gateway SWIFT totalmente fora do diagrama o faz parecer esquecido. Desenhá-lo e marcá-lo como fora do escopo torna a fronteira visível para todos que usam o modelo. Testadores que veem um caminho interessante em direção ao gateway sabem imediatamente que não lhes cabe segui-lo. A mesma disciplina se aplica aos processadores terceiros e aos bancos de dados de clientes de produção quando o engajamento se limita ao staging.

### 21.6 Modelos vivos

Atualize ao surgirem novas rotas de callback de pagamento. Um modelo que não é atualizado vira um perigo, porque as pessoas confiam nele. A regra do TRB é que todo ticket de mudança que acrescente ou altere um ponto de entrada, um armazenamento ou um callback externo precisa atualizar o modelo em até uma semana. A revisão semanal de Sam compara os tickets de mudança abertos com as arestas do modelo e lista os retardatários. A revisão é curta e um pouco irritante, e é por isso que funciona. As equipes atualizam o modelo para não aparecer na lista, e o modelo fica perto o bastante da realidade para planejar testes com base nele.

### 21.7 Fichas físicas para premissas abertas

As oficinas com os donos usam fichas físicas para as premissas. Uma ficha deixada em Aberta no fim bloqueia a abertura. A regra tátil parece infantil e funciona melhor que uma coluna de planilha que ninguém atualiza. Cada premissa Aberta ganha uma ficha na mesa. Fechá-la move a ficha para uma tigela de Fechadas, com uma nota de quem conferiu e como. As fichas ainda em Aberta no fim da oficina são fotografadas para o plano como riscos residuais, e a abertura não pode ser marcada como pronta até que o líder do engajamento as aceite. Colunas de planilha convidam a uma negligência educada. Uma ficha na mesa convida a uma decisão.

### 21.8 Manter os callbacks de pagamento no modelo

Novos callbacks de pagamento precisam aparecer no modelo em até uma semana após os tickets de mudança. A comparação semanal de Sam entre tickets de mudança e arestas do modelo pega os retardatários. Os callbacks de pagamento são fáceis de deixar passar porque chegam de fora e muitas vezes são acrescentados por equipes de produto sob pressão de entrega. Um callback que não está no modelo também não está no registro de fluxos, o que significa que pode não ter dono nem uma verificação de autenticação acordada. A comparação semanal é uma junção simples: tickets de mudança que mencionam callback, webhook ou notify, versus as arestas do modelo. Tudo o que não casa vira uma tarefa para o dono do ticket antes do próximo engajamento.

### 21.9 Desenhar os processadores como caixas-pretas

Os processadores aparecem como caixas-pretas, com os tipos de dados que cruzam a fronteira, e não como falsos hosts internos. Desenhar os servidores internos de um fornecedor convida os testadores a pensar em atacá-los. Desenhar uma caixa-preta rotulada "fornecedor de SMS", com códigos únicos saindo e recibos de entrega chegando, mantém a atenção no lado do TRB da fronteira: os recibos são validados, as falhas são tratadas, o fornecedor é autenticado? Os tipos de dados nas setas importam mais do que qualquer coisa dentro da caixa. Eles dizem aos testadores quais dados pessoais saem do TRB e o que volta que pode receber confiança demais.

### 21.10 Um deep link vira uma premissa aberta

Um novo deep link móvel aparece num ticket de mudança. Em três dias, o modelo de Sam ganha um ponto de entrada e um post-it de premissa: "AuthZ igual à da web?". O post-it continua Aberto na abertura e vira uma frase de risco residual. O deep link poderia reutilizar as verificações de autorização da web ou poderia ter sido ligado às pressas, com uma verificação mais fraca. Ninguém tinha validado qual. Deixar a premissa Aberta foi correto. A frase de risco residual disse a todos que a autorização do deep link móvel não estava coberta pelos testes web planejados, o que impediu que um relatório web limpo fosse lido erroneamente como uma cobertura móvel limpa.

### 21.11 Uma rota silenciosa a partir do site de marketing

A comparação do inventário de callbacks encontrou uma rota silenciosa do site de marketing para a core-api. Ela virou uma revisão de conduíte, e não uma surpresa de marketing em produção. O site de marketing tinha recebido um endpoint de conveniência para preencher previamente formulários de proposta. O endpoint alcançava a core-api e, portanto, o armazenamento de clientes, e nunca tinha aparecido no diagrama de arquitetura. Encontrá-lo numa comparação semanal significou que o conduíte pôde ser revisado, autenticado e ter sua taxa limitada antes que um engajamento ou um atacante o encontrasse. Surpresas são mais baratas em revisões de inventário do que em incidentes de produção.

### 21.12 Fotografar as premissas abertas para o plano

Os post-its de premissas abertas são fotografados para o pacote das ROE antes da abertura. Uma fotografia congela o estado da oficina sem depender de alguém digitá-lo depois. A imagem vai para o pacote das regras de engajamento, ao lado das frases de risco residual, para que qualquer pessoa que leia a autorização possa ver o que ainda era desconhecido. Depois da abertura, os post-its podem ir para o lixo. A fotografia permanece. Se um achado depois depender de uma premissa que estava Aberta, o pacote mostra que a equipe conhecia a lacuna.

A fotografia também resolve disputas sobre o que foi dito na oficina. A memória diverge; uma foto dos post-its não.

### 21.13 Premissas abertas no sumário executivo

As frases de risco residual vindas dos post-its Abertos são coladas automaticamente no rascunho do sumário executivo. Os executivos raramente leem registros de premissas. Eles leem o sumário executivo. Colar ali as premissas Abertas, numa frase simples cada uma, significa que as pessoas que aceitam o risco residual o veem antes de aceitar o relatório. A automação importa porque colar à mão é a etapa que é pulada sob prazo. As frases são curtas de propósito: a autorização do deep link móvel não foi validada contra as regras de produção.

Se a automação falhar, o líder do engajamento cola as frases à mão e abre um ticket contra o pipeline. O sumário ainda precisa trazer os riscos.

### 21.14 Do quadro branco para o registro de premissas

O plantão de modelos termina com uma fotografia do quadro branco e uma passagem de OCR para o registro de premissas. Post-its que o OCR não consegue ler são reescritos. Premissas ilegíveis são premissas negadas. Os erros de OCR são tratados como premissas Abertas até serem corrigidos, o que motiva uma letra caprichada. O caminho de fotografia mais OCR também significa que a oficina pode continuar analógica e colaborativa enquanto o registro duradouro continua pesquisável. Notas ilegíveis não podem virar Fechadas em silêncio. Uma premissa negada não pode ser tratada como Fechada no plano, o que mantém a pressão sobre quem é dono da nota ilegível para reescrevê-la.

### Exemplo resolvido (TRB sintético)

O modelo de Sam mostra web→ledger-db tracejado em vermelho como não intencional.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX061 — Premissa.** Como validar que o staging espelha a AuthZ da produção? *Rubrica:* 3 = comparar configurações/testes com os donos; 2 = parcial; 1 = presumir; 0 = nada.
- **EX062 — Por que omitir o SWIFT.** Por que omitir o SWIFT deste modelo? *Rubrica:* 3 = fora do escopo; 2 = parcial; 1 = sem importância; 0 = nada.
- **EX063 — Pontos de entrada.** Nomeie três pontos de entrada do internet banking. *Rubrica:* 3 = três entre web, API móvel, VPN dos funcionários, lote; 2 = dois; 1 = um; 0 = nada.

### Síntese

Os modelos tornam visíveis os fluxos não intencionais e explícitas as premissas.

### Continue estudando — capítulo 21 de 40

[← Capítulo 20 (rascunho)](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 (rascunho) →](#ch-22)

<a id="ch-22"></a>

## Capítulo 22 — Dados e dependências

### Objetivos de aprendizagem

Você vai (1) mapear as dependências; (2) sinalizar fluxos não aprovados; (3) designar donos.

### 22.1 Dependências

API central, banco de dados do razão, serviço antifraude, SMS, processador de cartões. Uma lista de dependências para testes é o conjunto de sistemas de que o alvo precisa para se comportar normalmente. O internet banking do TRB precisa da API central, do banco de dados do razão, de um serviço de pontuação antifraude, de um provedor de SMS para códigos únicos e de um processador de cartões para as etapas de pagamento. Se algum deles estiver fora do ar ou fora do escopo, partes da aplicação não podem ser testadas com honestidade. A lista também mostra onde os achados podem de fato pertencer. Uma falha que parece um bug do aplicativo bancário pode ser um serviço antifraude mal configurado. Sam confirma o dono e o status de autorização de cada dependência antes da abertura.

### 22.2 Laboratório de fluxos

O lab_flows marca web→ledger-db como UNAPPROVED. O laboratório compara o tráfego observado com o registro de fluxos aprovados e imprime qualquer caminho que não tenha uma entrada. Um caminho direto da web para o razão é o exemplo clássico: ele pula as verificações de autorização da API central e dá a um host web comprometido uma rota para dentro do banco de dados. Rodar o laboratório não é o achado. O achado é o caminho não aprovado mais o ticket de mudança e o dono ausentes. Os testadores salvam a saída do laboratório ao lado do registro do engajamento, para que uma disputa posterior sobre se o caminho existia possa ser respondida com um artefato datado.

### 22.3 Titularidade

Cada fluxo tem um dono de controle. A titularidade responde quem pode aprovar uma mudança, quem recebe um achado e quem pode parar um teste que usa o fluxo. Um fluxo sem dono não pode ser testado com segurança, porque ninguém pode aceitar o risco nem corrigir o que quebrar. O registro do TRB rejeita fluxos novos sem campo de dono, e a verificação pré-engajamento de Sam lista todos os fluxos do escopo cujo dono saiu do banco. Substituir um dono que saiu é uma tarefa de planejamento, não uma surpresa no meio da janela. Achados registrados contra fluxos sem dono tendem a ficar intocados, o que é mais um motivo para exigir a titularidade de antemão.

### 22.4 Terceiros

Autorização separada. As dependências que pertencem a outras empresas precisam da permissão dessas empresas antes que alguém as sonde. A autorização do TRB cobre os sistemas do TRB. O fornecedor de SMS, o processador de cartões e o provedor de nuvem têm, cada um, suas próprias regras. Sam pode observar como o TRB os chama e se o TRB valida as respostas deles, o que testa o código do TRB. Ele não pode rodar varreduras de vulnerabilidades contra os endpoints deles, a menos que seus programas digam que pode. A distinção está escrita nos cartões de método, para que um testador curioso não improvise.

### 22.5 Interrupções

Indisponibilidades de fornecedores são paradas, não oportunidades de martelar. Quando uma dependência está falhando, continuar a enviar tráfego raramente produz evidência de segurança útil e muitas vezes piora a indisponibilidade. As regras de engajamento tratam uma indisponibilidade confirmada de fornecedor como condição de parada para os métodos que precisam desse fornecedor. Sam registra a indisponibilidade, avisa o líder do engajamento e passa para métodos que não dependem do caminho quebrado. Martelar um serviço fora do ar para ver como ele falha é um teste de negação de serviço disfarçado e é proibido, a menos que as ROE o permitam explicitamente numa janela dedicada.

### 22.6 Segredos

Chaves de API em repositórios são achados do TRB. Uma chave de API incluída num commit de um repositório de código-fonte é uma credencial em todo clone, todo backup e, muitas vezes, todo log de integração contínua. Mesmo depois que a chave é removida do commit mais recente, o histórico ainda a guarda. Os achados de Sam para chaves em repositórios recomendam rotacionar a chave, removê-la do histórico quando viável, acrescentar um scanner de segredos ao pipeline e registrar um dono para o novo segredo no cofre. A severidade do achado depende do que a chave destrava. Uma chave de analytics somente leitura é diferente de uma chave que pode movimentar dinheiro.

### 22.7 Expirar os fluxos temporários

As datas de desativação dos fluxos temporários acionam o dono e Sam três dias antes. Se ninguém responde, o TrackScope marca o fluxo como expirado e nega os testes que dependiam dele até que seja renovado por escrito. Fluxos temporários sem expiração se tornam permanentes. O acionamento e a expiração automática transformam o temporário num limite de tempo real. Negar os testes que usavam o fluxo expirado é deliberado. Isso impede que um engajamento passe a depender em silêncio de um caminho que o banco já não pretendia manter e força uma renovação escrita que reafirme o motivo de negócio.

### 22.8 Varrer os repositórios do TRB

As varreduras de segredos em repositórios rodam sobre o código do TRB listado nas ROE. Sam abre achados para chaves sem dono no modelo de ativos. A varredura cobre apenas os repositórios que o engajamento está autorizado a examinar. Os achados distinguem as chaves que já têm donos no cofre das chaves que parecem órfãs. Uma chave órfã é urgente porque ninguém a está rotacionando. Ligar cada achado ao modelo de ativos também mostra quando uma chave pertence a um sistema fora do escopo; nesse caso, Sam a relata ao dono do sistema sem testar mais nada.

### 22.9 Renovações precisam de um motivo

Os acionamentos das datas de desativação incluem o motivo de negócio original. Renovações sem motivo são negadas. Uma renovação que diz "prorrogar por três meses" não ensina nada e convida a regras temporárias eternas. Exigir o motivo original, e uma frase sobre por que ele ainda se aplica, faz o dono perceber quando o projeto que precisava do fluxo já terminou. As renovações negadas aparecem numa lista semanal que Sam revisa com o dono da arquitetura. Padrões de negação muitas vezes apontam para um projeto que deveria terminar ou aceitar um conduíte permanente e revisado.

### 22.10 Quando o dono principal está de licença

Os acionamentos da data de desativação disparam; o dono está de licença. O dono substituto renova com um motivo. Sam passa a tratar como obrigatório o campo de dono substituto — acionamentos de expiração com um único dono são frágeis. Um controle que depende de uma pessoa estar à sua mesa falha durante férias e doenças. O dono substituto já tinha sido informado sobre a finalidade do fluxo, de modo que a renovação levou minutos. Tornar obrigatório o campo de substituto significa que o próximo fluxo temporário não pode ser criado até que duas pessoas possam responder por ele. Uma fragilidade removida no momento do registro não precisa ser descoberta durante uma tempestade de acionamentos.

### 22.11 Uma renovação que tornou o risco visível

Uma expiração sem motivo foi negada; o dono escreveu "atraso no projeto de segmentação PCI". Agora o risco está visível, não eterno. A frase fez dois trabalhos. Ela renovou o fluxo por um tempo limitado e disse a qualquer pessoa que lesse o registro por que um caminho arriscado ainda existia. Atrasos de projeto são reais; atrasos não ditos viram folclore. Quando o projeto de segmentação depois terminou, a mesma entrada do registro tornou óbvio que o motivo do fluxo tinha acabado e que a data de desativação não deveria ser renovada de novo.

### 22.12 Os donos substitutos precisam confirmar

Os donos substitutos precisam confirmar na interface do ticket; silêncio não é aceitação. Listar alguém como substituto sem a sua confirmação cria uma falsa sensação de cobertura. A interface exige um clique que registra a pessoa, o horário e o fluxo. Até que esse clique aconteça, o fluxo temporário não pode ser aprovado. A regra atrasou alguns registros e evitou várias lacunas silenciosas em que o substituto nomeado nunca tinha ouvido falar do fluxo. Nomes de substitutos escritos num ticket sem um clique desaparecem quando essa pessoa muda de equipe. O clique de confirmação é o que transforma um nome num dever.

### 22.13 Bloquear o encerramento sem um substituto

Campos obrigatórios de dono substituto bloqueiam o encerramento do ticket. Sam adora bloquear encerramentos. Os tickets de mudança que abrem fluxos temporários não podem ser encerrados até que exista a confirmação do substituto. Bloquear o encerramento é mais confiável do que enviar lembretes, porque a pressão de entrega já se concentra em fechar tickets. O bloqueio fica visível no mesmo lugar para onde os gerentes de projeto já olham. A preferência de Sam por bloqueios em vez de lembretes vem de ter visto processos baseados em lembretes falharem sempre que a equipe está ocupada.

A pressão de entrega dissolve os acordos de corredor. O bloqueio obriga o dono substituto nomeado a confirmar o fluxo antes que o ticket de mudança possa ser encerrado, e é isso que constitui o controle.

### 22.14 Post-mortems de fluxos expirados

Os post-mortems de expiração de fluxos perguntam se o motivo de negócio original ainda existe. Se o projeto terminou, o fluxo morre. Se o projeto continua, uma nova data de desativação é obrigatória. Regras temporárias eternas são rebatizadas como achados nas notas do post-mortem. O post-mortem é curto: motivo, resultado, próxima data de desativação ou exclusão. Rebatizar as regras temporárias eternas como achados torna o padrão visível para as mesmas pessoas que veem os outros riscos. Um fluxo que sobrevive a todo post-mortem sem um motivo vivo é uma falha de processo, não uma necessidade de rede. Escrever o post-mortem na semana em que o fluxo expira, e não meses depois, mantém honesto o motivo de negócio.

### Exemplo resolvido (TRB sintético)

Sam abre um ticket conjunto para os donos da rede e da aplicação sobre o UNAPPROVED web→ledger-db.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX064 — Linha do laboratório.** Cite a linha UNAPPROVED do laboratório. *Rubrica:* 3 = web -> ledger-db UNAPPROVED; 2 = parcial; 1 = errado; 0 = nada.
- **EX065 — Ticket conjunto.** Por que abrir o ticket para a rede e a aplicação juntas? *Rubrica:* 3 = o fluxo exige mudanças tanto no roteamento quanto no comportamento da aplicação; 2 = parcial; 1 = só uma; 0 = nada.
- **EX066 — Martelar o fornecedor.** E se o fornecedor de SMS der timeout? *Rubrica:* 3 = parar as verificações relacionadas; nenhuma tempestade de novas tentativas; 2 = parcial; 1 = inundar de novas tentativas; 0 = nada.

### Síntese

Dependências e fluxos têm donos; arestas não aprovadas viram tickets.

### Continue estudando — capítulo 22 de 40

[← Capítulo 21 (rascunho)](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 (rascunho) →](#ch-23)

<a id="ch-23"></a>

## Capítulo 23 — Métodos I

### Objetivos de aprendizagem

Você vai (1) construir cartões de método; (2) vincular os métodos às ROE; (3) definir limites de taxa.

### 23.1 Cartões

Finalidade, cláusula das ROE, ferramenta/configurações, paradas, evidência. Um cartão de método é a unidade de trabalho dos testes autorizados. Ele declara por que o método está sendo executado, qual cláusula das regras de engajamento o permite, qual ferramenta e quais configurações serão usadas, que condições param o método e que evidência ele precisa produzir. Os cartões impedem a improvisação. Um testador que quer tentar algo que não está num cartão precisa propor um novo cartão e incluí-lo no conjunto congelado, ou esperar uma alteração das regras. O TrackScope agenda cartões, não atividades livres.

### 23.2 WSTG

Selecione os temas de autenticação, sessão e controle de acesso para o staging do internet banking. O Web Security Testing Guide da OWASP cataloga muitas ideias de teste. O TRB não roda todas em cada engajamento. Para o staging do internet banking, os temas prioritários são autenticação, gerenciamento de sessão e controle de acesso, porque as falhas ali movimentam dados de clientes ou dinheiro. Outros temas aparecem quando os relatórios de ameaças ou mudanças recentes os justificam. Selecionar os temas no plano torna honesta a profundidade do engajamento. Um relatório que afirmasse ampla cobertura web depois de rodar apenas três temas enganaria.

### 23.3 Taxas

Os tetos protegem a disponibilidade. Mesmo testes autorizados podem derrubar um serviço se enviarem tráfego demais. Os cartões de método incluem tetos de taxa: requisições por segundo, sessões concorrentes, total de identidades tentadas. Os tetos são definidos com o dono do serviço e com o SOC, que sabem como é o normal. Exceder um teto é uma condição de parada, não uma sugestão. Sam prefere terminar um método devagar ao longo de duas noites a explicar uma indisponibilidade causada por um teste que deveria ser cuidadoso.

### 23.4 Proibidos

Spraying e DoS continuam proibidos. O password spraying contra muitas contas e os testes de negação de serviço são excluídos das janelas comuns do TRB porque seu impacto é difícil de conter e sua barra de autorização é mais alta. Um testador que descobre que o spraying seria interessante ainda assim não o faz. Ele escreve uma nota de que o método foi considerado e excluído, que pode virar uma recomendação de um exercício separado e cuidadosamente delimitado, se o risco o justificar. Proibido significa proibido, não proibido a menos que se tenha curiosidade.

### 23.5 Silenciosos vs ruidosos

Prefira métodos silenciosos quando a detecção também está em teste. Alguns métodos produzem pouco ruído nos logs; outros inundam o SOC de alertas. Quando o engajamento também está medindo a detecção, métodos ruidosos afogam o sinal que o SOC precisa mostrar. Métodos silenciosos primeiro deixam o SOC demonstrar o que pega em condições realistas. Raspagens ruidosas de inventário ficam em dias separados, com um orçamento de ruído assinado pelo SOC. Misturá-los uma vez produziu uma nevasca de alertas que não ensinou nada nem sobre a detecção nem sobre o inventário.

### 23.6 Congelamento

O conjunto de métodos congela depois da abertura, a menos que as ROE sejam alteradas. Depois da abertura, os cartões agendados ficam fixos. Acrescentar um método no meio da janela contornaria a revisão que conferiu o escopo, os limites de taxa e as condições de parada. Se um método novo se tornar necessário, as regras de engajamento são alteradas por escrito e o congelamento é suspenso apenas para essa alteração. O congelamento frustra os improvisadores e protege todos os demais. Os clientes não podem alegar que foram surpreendidos por um método que não estava na lista da abertura, e os testadores não podem alegar que achavam que um método improvisado era permitido.

### 23.7 Separar os dias silenciosos dos ruidosos

Os métodos silenciosos são preferidos nas janelas de purple team, para que o sinal do SOC seja interpretável. Sam agenda raspagens ruidosas de inventário em dias separados. Misturá-los produziu uma vez uma nevasca de alertas inútil; o calendário agora impede isso. O bloco do calendário é compartilhado com o SOC. Um dia de purple team mostra apenas cartões silenciosos. Um dia de inventário mostra cartões ruidosos e um orçamento de ruído maior. Verificações automáticas se recusam a agendar um cartão ruidoso num dia de purple team. A nevasca ensinou à equipe que o desenho do calendário faz parte do desenho dos métodos.

### 23.8 Todo cartão precisa de um dono

Cada cartão de método tem um engenheiro dono. Cartões sem dono não podem ser agendados. Sam assume a titularidade antes de propor um cartão na abertura. Titularidade significa que alguém mantém atualizados a cláusula das ROE, as versões das ferramentas e as condições de parada do cartão. Cartões sem dono apodrecem: citam cláusulas aposentadas ou configurações que já não correspondem à plataforma. Recusar-se a agendá-los faz da titularidade um requisito prático, e não um campo de cortesia. Assumir a titularidade antes da abertura também significa que quem propõe está se oferecendo para manter o cartão, o que reduz as sugestões de passagem.

### 23.9 Orçamentos de ruído do SOC

O SOC assina um orçamento de ruído por janela. Excedê-lo é uma condição de parada que Sam respeita imediatamente. O orçamento é um número de alertas por hora, geralmente, mais uma lista dos tipos de alerta que contam. O SOC o assina porque conhece sua escala e seu outro trabalho naquela noite. Quando o TrackScope ou o SOC dizem que o orçamento se esgotou, Sam para os cartões ruidosos mesmo que a janela ainda tenha horas pela frente. O respeito imediato à parada constrói confiança. Um testador que negocia para passar de uma parada do SOC uma vez vai achar a próxima conversa sobre orçamento muito mais difícil.

### 23.10 Dividir um cartão para caber no orçamento

O orçamento de ruído do SOC é de 30 alertas por hora. O cartão de método de Sam geraria cerca de 80. Ele divide o cartão em dois dias. O líder do SOC lhe paga um café; a janela fica verde. A divisão preservou o objetivo do teste e a capacidade de resposta do SOC. Os requisitos de evidência do cartão foram cumpridos ao longo dos dois dias, com rótulos claros para que ninguém pensasse que o método tinha sido abandonado. O café é opcional. Uma janela verde, isto é, sem nenhuma emergência causada pelos testes, é a verdadeira recompensa e o motivo pelo qual os orçamentos existem.

### 23.11 Tratar as assinaturas do SOC como as do CISO

A folha do orçamento de ruído é assinada como uma mini-ROE. Sam trata as assinaturas do SOC com o mesmo respeito que as do CISO. O SOC não é dono da autorização geral, mas é dono do ambiente de detecção que o teste vai perturbar. Sua assinatura no orçamento de ruído é a autorização para essa perturbação. Ignorá-la seria ignorar uma fronteira tão real quanto um host excluído. O hábito de Sam de respeito igual também incentiva o SOC a assinar prontamente, porque sabe que a assinatura será honrada, e não barganhada.

### 23.12 Pausa automática quando o orçamento estoura

Estouros do orçamento de ruído disparam uma flag automática de pausa do cartão de método no TrackScope. A automação elimina a conversa constrangedora em que um testador argumenta que só mais algumas requisições terminariam o cartão. A plataforma conta os alertas atribuídos ao engajamento e, quando o orçamento é atingido, pausa os cartões ruidosos e avisa Sam e o SOC. Terminar então exige uma contra-assinatura do SOC para uma prorrogação, não uma decisão unilateral. A flag já deteve vários estouros educados que teriam virado indisponibilidades nada educadas.

### 23.13 Os testadores não podem liberar a própria pausa

As flags de pausa só são liberadas com a contra-assinatura do SOC. Sam não pode liberar o próprio estouro de ruído. A autoliberação faria da pausa automática um teatro. A contra-assinatura do SOC é uma segunda pessoa afirmando que o ambiente aguenta mais carga. Às vezes, ela recusa e pede uma continuação mais silenciosa no dia seguinte. Essa recusa é um controle bem-sucedido. Registrar quem liberou uma pausa, e quando, também ajuda as revisões posteriores a entender por que um cartão ruidoso continuou depois de um estouro.

Quando o analista do SOC libera uma flag, o TrackScope registra no próprio cartão o nome dele, a contagem de alertas no momento da liberação e o novo orçamento. A auditoria seguinte do cartão pode então comparar essa extensão com os alertas que o PulseMap atribuiu ao engajamento depois disso.

### 23.14 Auditorias rotativas dos cartões

A curadoria dos cartões de método é uma função rotativa. A cada mês, um engenheiro diferente audita cinco cartões em busca de deriva nas cláusulas das ROE. A auditoria de Sam encontrou um cartão que citava uma seção aposentada das ROE; ele foi suspenso em uma hora. Uma cláusula aposentada das ROE num cartão ativo é um bug silencioso de autorização. A auditoria mensal pega alguns por ano, geralmente depois de uma reescrita das regras. Suspender o cartão imediatamente impede que alguém agende trabalho sob uma cláusula que já não existe. A função rotativa espalha pela equipe a familiaridade com a biblioteca. Publicar quais cinco cartões foram auditados a cada mês torna a rotação visível e mais difícil de pular.

### Exemplo resolvido (TRB sintético)

O cartão de IDOR de Sam: 1 req/s, dois usuários de teste, parada em rajada de 5xx.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX067 — Campos do cartão.** Liste cinco campos do cartão de método. *Rubrica:* 3 = cinco do capítulo; 2 = três; 1 = um; 0 = nada.
- **EX068 — Par proibido.** Nomeie dois métodos proibidos. *Rubrica:* 3 = spraying e DoS; 2 = um; 1 = autenticação do WSTG; 0 = nada.
- **EX069 — Congelamento.** Por que congelar os métodos depois da abertura? *Rubrica:* 3 = evitar a expansão silenciosa de escopo/métodos; 2 = parcial; 1 = sem motivo; 0 = nada.

### Síntese

Os métodos são cartões vinculados às ROE, com taxas e congelamentos.

### Continue estudando — capítulo 23 de 40

[← Capítulo 22 (rascunho)](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 (rascunho) →](#ch-24)

<a id="ch-24"></a>

## Capítulo 24 — Controles

### Objetivos de aprendizagem

Você vai (1) associar controles a achados; (2) classificar achados; (3) propor controles compensatórios.

### 24.1 Associação

Administrador compartilhado → contas nominais + cofre; fluxo não aprovado → firewall + negação na aplicação; cadastro fraco de MFA → correção do cadastro. Uma recomendação de controle precisa corresponder à fraqueza que responde. Senhas de administrador compartilhadas se corrigem com contas nominais e um cofre, não com uma política de senhas mais longas. Um caminho de rede não aprovado se corrige removendo a regra de firewall e negando o caminho na aplicação, não apenas acrescentando monitoramento. Um cadastro fraco de MFA se corrige no fluxo de cadastro. Recomendações desencontradas desperdiçam o tempo de quem corrige e deixam o caminho original aberto. A revisão de Sam dos rascunhos de achados confere que cada controle recomendado de fato fecharia o caminho demonstrado.

### 24.2 Laboratório de classificação

O lab_rank ordena F1, F3 e F4, com pontuação 6, antes de F2, com 3.

```python
"""Lab 24: rank synthetic TRB findings by likelihood x impact, ties by id."""
f = [("F1","Shared admin on loan system",2,3),("F2","Verbose error pages",3,1),
     ("F3","Web tier reaches ledger DB directly",2,3),("F4","Weak MFA enrolment check",3,2)]
for i,t,l,m in sorted(f, key=lambda x:(-x[2]*x[3], x[0])):
    s=l*m; print(f"{i} {s} {'high' if s>=6 else 'medium' if s>=3 else 'low':6} {t}")
```

Execute com `python3 lab_rank.py`. Saída verificada:

```text
F1 6 high   Shared admin on loan system
F3 6 high   Web tier reaches ledger DB directly
F4 6 high   Weak MFA enrolment check
F2 3 medium Verbose error pages
```

O produto de probabilidade e impacto é um auxílio simples de classificação, não uma lei da natureza. Os empates são desfeitos pelo id do achado, para que a ordem seja reproduzível. F1, F3 e F4 pontuam seis e superam os três de F2, o que corresponde à intuição de que uma senha de administrador compartilhada, um caminho direto da web para o razão e uma verificação fraca no cadastro de MFA importam mais que páginas de erro verbosas. A tarefa do laboratório é tornar a classificação visível antes que as personalidades entrem na discussão. Uma vez que as pontuações estão na mesa, argumentar para rebaixar um achado vira uma decisão visível de aceitação de risco, e não uma reordenação silenciosa.

### 24.3 Compensatórios

Administração apenas via jump host enquanto as senhas se tornam únicas. Um controle compensatório reduz o risco enquanto a correção definitiva não está pronta. Se ainda existem senhas de administrador compartilhadas, restringir a administração ao jump host com autenticação multifator reduz quem pode usar essas senhas e torna seu uso auditável. A compensação tem data. O achado continua aberto, com uma data-limite para as senhas únicas, e o controle compensatório é listado ao lado dele, para que ninguém confunda a regra do jump host com a correção completa. Quando a correção definitiva chega, a compensação pode ser aposentada ou mantida como defesa em profundidade.

### 24.4 Titularidade

Todo controle tem um dono nomeado e uma data. Um controle sem dono é uma frase num relatório. O dono é a pessoa que vai implementá-lo ou operá-lo, e a data é quando ele estará implantado ou será revisado de novo. O TrackScope se recusa a marcar um achado como aceito-com-controle a menos que os dois campos estejam preenchidos. A titularidade também evita compensações órfãs. Quando a pessoa que configurou a administração apenas via jump host sai, o campo datado de dono mostra quem precisa assumir o controle, ou o achado é reaberto.

### 24.5 Verificar depois

O Capítulo 30 trata dos retestes. Declarar um controle implementado não é o mesmo que mostrar que ele funciona. Os retestes fecham essa lacuna. Depois que o dono diz que as contas nominais substituíram a senha de administrador compartilhada, Sam agenda um reteste que tenta a senha antiga e confere que a administração ainda exige o jump host. Retestes reprovados reabrem o achado automaticamente. A data do reteste faz parte do registro do controle, de modo que um controle que nunca foi retestado aparece no PulseMap como não verificado. Um reteste é planejado com a mesma conta, a mesma rede de origem e a mesma requisição que provaram a fraqueza, para que uma aprovação signifique que o caminho está fechado, e não que o testador tentou algo mais fácil.

### 24.6 Afirmação exagerada

Não chame um controle de "previne todo APT". Os controles reduzem caminhos específicos. Nomear um ator sofisticado ou prometer prevenção total transforma um achado preciso em marketing. A linguagem dos relatórios de Sam nomeia o caminho fechado, as condições do teste e o risco residual. Uma frase como "a administração a partir da VLAN de usuários para os servidores de staging está bloqueada enquanto as senhas não se tornam únicas" é utilizável. Uma frase como "isto previne ameaças persistentes avançadas" não é. O linter de garantia sinaliza o segundo tipo de frase antes que o relatório saia de rascunho.

### 24.7 Congelar as pontuações antes da discussão

As reuniões de classificação congelam as pontuações antes da discussão de personalidades. Sam coleta as pontuações em silêncio e depois as revela. O lobby para rebaixar um achado porque uma equipe está "ocupada" acontece depois das pontuações, onde fica visível como aceitação de risco. A pontuação silenciosa impede que a primeira voz alta ancore todas as outras. Revelar depois permite discutir honestamente a ocupação como motivo para aceitar o risco por um tempo, com assinatura e expiração, em vez de como motivo para fingir que o achado pontuou menos. A diferença é se o registro do banco mostra o trade-off.

### 24.8 Aceitação de risco por escrito

A aceitação de risco usa um formulário com o montante, a expiração e a assinatura do CISO. Um "a gente convive com isso" verbal não fecha o F3. A aceitação verbal evapora quando a equipe muda ou quando um incidente faz todos esquecerem quem concordou. O formulário registra o que é aceito, até quando e por quem. O PulseMap mostra os achados aceitos com expiração em âmbar, e não em verde, para que não sumam da atenção. Quando a expiração chega sem correção nem renovação, o achado é reaberto. Esse mecanismo é o motivo pelo qual o F3 não pode ser fechado com uma conversa de corredor.

### 24.9 Revelar as pontuações só depois que todos enviarem

As pontuações só aparecem depois que todos os avaliadores enviam as suas. O roteiro de facilitação de Sam bloqueia revelações antecipadas. Revelações antecipadas deixam os avaliadores posteriores se ajustarem ao grupo, o que anula o julgamento independente. O roteiro de facilitação é uma lista de verificação que Sam lê: confirmar que todo avaliador enviou e, então, mostrar a tabela. O TrackScope impõe a mesma regra em reuniões remotas, escondendo o agregado até que chegue a última cédula. Bloquear revelações antecipadas atrasou ocasionalmente uma reunião em cinco minutos e regularmente impediu que uma voz sênior definisse a pontuação.

### 24.10 Uma trilha de higiene para correções fáceis

A revelação da classificação mostra o F2 por último. A equipe web ainda quer corrigir o F2 primeiro porque é fácil. Sam registra o que é fácil, mas baixo, numa trilha separada de "higiene", para que isso não desloque o financiamento do F3. Correções fáceis valem a pena. Não valem a pena a ponto de deixar sem recursos o trabalho mais bem classificado. A trilha de higiene tem sua própria pequena capacidade e seu próprio limite de WIP, para que a equipe web possa eliminar as páginas de erro verbosas sem tirar engenheiros da correção do caminho para o razão. Manter as trilhas separadas também mantém os relatórios honestos: a vazão da higiene não é apresentada como progresso nos achados de alto risco.

### 24.11 Trilhas paralelas protegem o trabalho difícil

A trilha de higiene corrigiu o F2 em três dias sem roubar a reunião de orçamento do F3. Trilhas paralelas impedem que o trabalho fácil deixe o difícil sem recursos. Antes da divisão, todo achado fácil competia pelo mesmo espaço na reunião que o F3, e o fácil geralmente vencia porque prometia uma vitória rápida. Depois da divisão, o F3 manteve sua conversa de financiamento e o F2 ainda foi corrigido. O padrão se generaliza. Sempre que o trabalho de baixa severidade desloca de forma consistente o de alta severidade, a correção é uma alocação de capacidade separada, não um sermão sobre prioridades.

### 24.12 Limites de WIP na higiene

Os limites de WIP da trilha de higiene a impedem de virar um depósito de riscos ignorados. Sem um limite, todo achado desconfortável é rerrotulado como higiene e a trilha vira um segundo backlog de riscos ignorados. O limite força uma escolha: terminar algo antes de começar mais. Os achados que não cabem precisam esperar, conquistar um lugar na lista classificada principal ou ser aceitos com expiração. O limite de WIP é um controle sobre o processo que alega ajudar. Um achado movido para a higiene ainda precisa levar sua pontuação original, para que qualquer pessoa que revise a trilha possa ver se um item de alto risco foi disfarçado de arrumação.

### 24.13 Um WIP rígido de três

O limite de WIP da higiene é três. A quarta correção fácil espera. Foco é um controle. Três é pouco o bastante para que a equipe sinta a restrição e muito o bastante para que o trabalho real de higiene continue. Quando aparece uma quarta correção fácil, ela espera visivelmente no quadro. Esperar é desconfortável e útil. Isso impede o acúmulo silencioso de arrumações pela metade e evita que a promessa de rapidez da trilha de higiene vire mais uma fila infinita. O limite é revisado a cada trimestre. Se os itens esperam mais de um mês, a equipe ou aumenta a capacidade, ou admite que parte do trabalho de higiene não será feita e registra essa decisão.

### 24.14 Capas de noventa segundos para os conselhos de financiamento

Os conselhos de financiamento recebem listas classificadas com uma capa de uma página em linguagem simples. Sam pratica a capa em voz alta até conseguir apresentá-la em noventa segundos. Os conselhos se lembram da capa por mais tempo que do apêndice. Praticar em voz alta pega o jargão que o apêndice pode manter e a capa não. Conselhos que se lembram da capa fazem perguntas melhores sobre a lista classificada. Conselhos que recebem apenas o apêndice muitas vezes não se lembram de nada além da contagem total de achados, que é o número menos útil do material. O apêndice ainda importa para os engenheiros que vão fazer o trabalho; por isso, a capa sempre termina com uma indicação da tabela classificada e de sua rubrica de pontuação.

### Exemplo resolvido (TRB sintético)

Sam apresenta a lista classificada; o conselho financia F1/F3/F4 primeiro.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX070 — Ordem da classificação.** Qual achado fica em último no laboratório? *Rubrica:* 3 = F2; 2 = F1; 1 = F4; 0 = nada.
- **EX071 — Compensatório.** Dê um controle compensatório para o administrador compartilhado. *Rubrica:* 3 = apenas via jump host/MFA/monitoramento enquanto as senhas se tornam únicas; 2 = parcial; 1 = ignorar; 0 = nada.
- **EX072 — Pontuação.** Qual é a pontuação e a faixa do F4? *Rubrica:* 3 = 6, high; 2 = 6; 1 = 3; 0 = nada.

### Síntese

Os controles correspondem aos achados; a classificação dirige o financiamento; os controles compensatórios ganham tempo.

### Continue estudando — capítulo 24 de 40

[← Capítulo 23 (rascunho)](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 (rascunho) →](#ch-25)

<a id="ch-25"></a>

## Capítulo 25 — Laboratório I

### Objetivos de aprendizagem

Você vai (1) executar os laboratórios de escopo, Wilson e fluxos sob supervisão; (2) fazer a verificação por pares; (3) recusar evidências ruins.

### 25.1 Caderno

Saídas de lab_scope, lab_wilson e lab_flows com as iniciais.

O caderno de laboratório é a evidência de que o estudante executou as ferramentas, e não de que leu sobre elas. Cada saída exigida é colada ou anexada com as iniciais do estudante e o horário. As iniciais importam porque capturas de tela compartilhadas circulam. Um caderno sem saídas é reprovado, por mais polido que seja o texto. Os supervisores conferem se os números colados correspondem ao que as versões fixadas dos scripts produzem, e é por isso que os hashes dos scripts aparecem mais adiante no capítulo.

### 25.2 Verificação por pares

Comparar as classificações de escopo. Depois de executar o lab_scope, os estudantes trocam os cadernos e reclassificam a mesma lista de alvos sem olhar as respostas um do outro. As divergências são discutidas com base no arquivo de escopo escrito, e não na memória. A verificação por pares pega leituras erradas sistemáticas, como tratar a exclusão do SWIFT como opcional, e treina o hábito de ter uma segunda pessoa confirmando as decisões de escopo antes de uma janela real. Uma verificação por pares limpa faz parte dos critérios de aprovação do laboratório. Quando os pares continuam discordando depois de ler o arquivo, o supervisor decide e a linha ambígua é enviada ao autor do escopo como correção de redação.

### 25.3 Falha plantada

Recusar evidência com hash divergente. Um arquivo de evidência no pacote do laboratório tem um hash que não corresponde à nota que o acompanha. Os estudantes que o arquivam mesmo assim são reprovados nessa estação. A questão é emocional, além de técnica. Recusar uma evidência dá a sensação de desacelerar, e num laboratório cronometrado essa pressão é proposital. A ação correta é parar, registrar a divergência e solicitar uma nova captura. Levar essa recusa para os engajamentos reais é o hábito que a estação existe para construir.

### 25.4 Tempo limitado

Duas horas, com parada obrigatória. Janelas reais terminam. O laboratório também termina, mesmo que uma estação esteja inacabada. Os estudantes praticam escrever o que concluíram, o que não concluíram e o que fariam em seguida, que é a mesma disciplina que Sam usa quando uma noite de testes fica sem tempo. Estender o laboratório para os estudantes com dificuldade ensinaria a lição errada. O tempo limitado também mantém justas as verificações por pares: todos têm o mesmo relógio. Os supervisores avaliam a nota de passagem com a mesma seriedade das estações concluídas, porque uma lista honesta do trabalho inacabado é o que permite a um colega retomar com segurança na noite seguinte.

### 25.5 Sem produção

Varrer o TRB em produção reprova no laboratório. O ambiente do laboratório usa endereços de faixas de documentação e dados sintéticos. Qualquer tentativa de apontar ferramentas para sistemas reais do TRB, mesmo por entusiasmo, é reprovação automática e uma conversa com o supervisor. A regra protege o banco e o estudante. A autorização para o laboratório é autorização para o laboratório. A curiosidade sobre a produção pertence a um engajamento planejado com escopo assinado, e não a um exercício de sala de aula. A rede do laboratório não tem rota para as faixas do TRB, então a regra também é imposta tecnicamente, e qualquer tentativa bloqueada aparece no log do firewall do laboratório que o supervisor revisa.

### 25.6 Aprovação

O supervisor aprova pela disciplina, não pela novidade. Um laboratório aprovado mostra verificações de escopo cuidadosas, hashing honesto, cadernos completos e respeito às paradas. Técnicas extras sofisticadas que não foram pedidas não aumentam a nota, e podem reduzi-la se violarem uma regra. Os supervisores assinam uma rubrica curta: escopo correto, recusa por hash demonstrada, saídas presentes, nenhum contato com a produção. A novidade é bem-vinda nos capítulos posteriores de pesquisa. O Laboratório I recompensa a disciplina. Um estudante que terminou todas as estações, mas arquivou a evidência divergente, não é aprovado, enquanto um que a recusou e ficou sem tempo numa estação posterior normalmente é.

### 25.7 A exclusão do SWIFT que sumiu

Entre as falhas plantadas do Laboratório I há um arquivo de escopo com o SWIFT removido das exclusões. Os estudantes que não percebem são reprovados. Sam foi reprovado nessa variante uma vez, quando era estudante, e hoje escreve as exclusões primeiro, todas as vezes. A variante funciona porque os estudantes costumam conferir se as faixas em escopo parecem corretas e esquecem de conferir se as exclusões continuam presentes. O hábito duradouro que Sam tirou dessa reprovação é ler a lista de exclusões antes da lista de inclusões. O laboratório mantém a variante porque a falha é barata numa sala de aula e cara numa janela real.

### 25.8 Fixando as versões dos scripts do laboratório

Os cadernos de laboratório incluem os hashes dos scripts usados. A divergência de versões é uma desculpa comum que Sam elimina fixando os hashes. Sem hashes, um estudante cujos números diferem do gabarito pode alegar que executou outra versão do script, e o supervisor não consegue verificar com facilidade. Com hashes, o caderno mostra exatamente quais bytes foram executados. Fixar versões também protege os estudantes. Se os mantenedores do laboratório mudarem um script no meio do período, a divergência de hash explica um resultado surpreendente, em vez de parecer erro do estudante. A lista de hashes fica no topo do caderno, e a primeira verificação do supervisor é recalcular um hash antes de ler qualquer resultado.

### 25.9 Rodízio das variantes plantadas

A variante de escopo plantada passa por rodízio para que a notícia não se espalhe entre as turmas. Sam mantém três variantes. Se todas as turmas vissem a mesma linha do SWIFT faltando, a turma da tarde ficaria sabendo no almoço. Três variantes mantêm honesta a verificação por pares: exclusão ausente, exclusão renomeada e exclusão apenas num apêndice. Os estudantes são avisados de que existem variantes, então decorar uma resposta é obviamente inútil. Os facilitadores sorteiam a variante de um envelope lacrado no início de cada turma. As variantes diferem apenas em onde o problema da exclusão se esconde, de modo que todos os estudantes enfrentam a mesma habilidade sob um disfarce diferente e as notas continuam comparáveis.

### 25.10 Exclusões pelo id do ativo

A variante B do Laboratório I esconde uma exclusão renomeando o SWIFT para "pay-gw-01". Os estudantes que só buscam a string "SWIFT" são reprovados. Sam ensina a exclusão pelo id do ativo, não pelo nome comercial. Inventários reais renomeiam as coisas. Um gateway que a equipe chama de SWIFT pode aparecer no registro de ativos com um hostname. Conferir as exclusões pelos nomes que as pessoas usam na conversa deixa essas linhas passarem. A variante renomeada do laboratório torna esse modo de falha pessoal. Os estudantes que passam por ela saem com o hábito de casar identificadores de ativos, e não slogans.

### 25.11 Exclusões escondidas em apêndices

A variante C usa uma exclusão listada apenas numa tabela de apêndice. Os estudantes que pulam os apêndices são reprovados. Sam adora a disciplina com apêndices. Documentos de escopo enterram linhas importantes em apêndices com mais frequência do que qualquer um admite. A variante C é um pouco cruel e muito realista. A correção é uma ordem de leitura: folha de rosto, apêndice de exclusões e, depois, faixas de inclusão. Os estudantes que adotam essa ordem deixam de ser reprovados na C e deixam de perder exclusões em regras de engajamento reais. A variante do apêndice também ensina que a estrutura de um documento de escopo faz parte do seu significado; uma tabela no fim pode ter tanta autoridade quanto a folha de rosto.

### 25.12 Lembretes plastificados de ids de ativos

As exclusões por id de ativo estão impressas no cartão plastificado da bancada do laboratório. O cartão lista os três identificadores que precisam aparecer em toda verificação de escopo do banco fictício do laboratório. É um apoio para o hábito, não um substituto para a leitura do arquivo de escopo. Os estudantes podem usá-lo durante o Laboratório I e espera-se que trabalhem sem ele nos laboratórios seguintes. A plastificação sobrevive a café derramado, um risco de laboratório mais comum do que os instrutores admitem. Os estudantes registram no caderno se usaram o cartão, o que permite aos supervisores ver quem está pronto para dispensar o apoio.

### 25.13 Invalidando cartões plastificados antigos

Os cartões plastificados têm versão; os antigos são furados para marcar que estão invalidados. Um cartão desatualizado é pior do que nenhum cartão, porque os estudantes confiam nele. Quando os identificadores de ativos mudam, novos cartões são emitidos e os antigos são furados para que não possam ser reutilizados por descuido. O número de versão do cartão corresponde à versão do pacote do laboratório. Os facilitadores conferem essa correspondência antes de cada turma, como parte da abertura da sala. Os cartões invalidados vão para uma caixa na mesa do facilitador, que serve também como um histórico rápido de quantas vezes os identificadores do laboratório mudaram.

### 25.14 Mostrando um caderno reprovado de verdade

As instruções iniciais do Laboratório I mostram um caderno reprovado de um ano anterior (com permissão) em que o hashing foi pulado. Ver uma reprovação real convence mais do que um item da rubrica. Sam agradece ao ex-aluno que permitiu o compartilhamento anonimizado. A permissão e a anonimização são obrigatórias; o que importa é o hash ausente, não a pessoa. Os estudantes que veem a reprovação fazem perguntas melhores sobre os próprios cadernos. Os itens da rubrica descrevem o padrão. Uma falha real faz o padrão ser sentido. Sempre que possível, cada nova turma vê uma reprovação anonimizada diferente, para que o exemplo não vire uma história conhecida que todos ignoram.

### Exemplo resolvido (TRB sintético)

Sam recusa a evidência ruim plantada e pega um colega marcando o SWIFT como em escopo.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX073 — Laboratórios usados.** Quais três laboratórios estão no caderno? *Rubrica:* 3 = scope, wilson, flows; 2 = dois; 1 = um; 0 = nenhum.
- **EX074 — Condição de reprovação.** O que reprova no Laboratório I imediatamente? *Rubrica:* 3 = varredura ao vivo/em produção; 2 = parcial; 1 = terminar cedo; 0 = nada.
- **EX075 — Erro do SWIFT.** O que se deve dizer a um colega que marca o SWIFT como em escopo? *Rubrica:* 3 = EXCLUDED; remover; 2 = parcial; 1 = ok; 0 = nada.

### Síntese

O Laboratório I avalia a disciplina de autorização e a integridade da evidência.

### Continue estudando — capítulo 25 de 40

[← Capítulo 24 (rascunho)](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 (rascunho) →](#ch-26)

<a id="ch-26"></a>

## Capítulo 26 — Métodos II

### Objetivos de aprendizagem

Você vai (1) encadear achados de forma ética; (2) parar na prova mínima; (3) documentar as cadeias.

### 26.1 Encadeamento

Somente dentro das ROE; parar na prova de impacto. Uma cadeia é uma sequência de passos permitidos que, juntos, mostram como um ponto de apoio de baixo privilégio pode chegar a um ativo de maior valor. No Riverstone Transit Bank, cada elo já precisa estar permitido pelas regras de engajamento; inventar um novo salto no meio do engajamento está fora dos limites. O operador para no momento em que um impacto é provado, porque pivôs adicionais acrescentam risco sem acrescentar evidência ao achado. Sam Ito mantém uma lista curta de transições aprovadas no cartão de método, para que uma sessão de madrugada não invente um atalho criativo que ninguém assinou. Cadeias que parecem impressionantes, mas se apoiam num passo não aprovado, são descartadas, e não celebradas.

### 26.2 Prova mínima

Nada de pivôs extras "por diversão". Prova mínima significa o menor conjunto de passos que demonstra a fraqueza com detalhe suficiente para que o responsável a reproduza. Pivôs extras depois desse ponto são curiosidade disfarçada de rigor e, muitas vezes, ampliam o raio de impacto sem mudar o achado. O TrackScope registra os passos da prova; qualquer coisa além deles exige um novo ticket e uma nova aprovação. Sam certa vez deteve um júnior que queria "só ver" se o domain admin era alcançável depois que uma leitura entre usuários já estava registrada em vídeo. A contenção do júnior entrou na nota de orientação, o que é mais útil do que mais uma captura de tela de um shell.

### 26.3 Documentação

Diagrama da cadeia no apêndice, com horários. Toda cadeia aceita é entregue com um diagrama que nomeia cada salto, os identificadores de ativos do FindingsDesk e o horário de relógio de cada transição. Hostnames escritos à mão já quebraram um link de apêndice e custaram um dia de conserto; ids compartilhados mantêm o apêndice verificável mecanicamente. Os horários importam porque as metas de detecção perguntam se o SOC viu as etapas, e um diagrama sem relógios não consegue responder a isso. Sam cola o diagrama no apêndice do engajamento antes de registrar o achado, e não depois do debrief, para que os revisores nunca precisem correr atrás de uma figura ausente. O diagrama é evidência, não decoração.

### 26.4 Metas de detecção

Anotar se o SOC viu as etapas — sinergia purple. As metas de detecção transformam uma cadeia de red team em retorno para o purple team. Para cada etapa, Sam registra se o PulseMap ou o console do SOC mostrou um acerto, uma falha ou um desconhecido. Desconhecido só é permitido quando nenhum sensor cobre aquele salto, e essa lacuna vira, ela própria, um item do backlog. A nota é curta: id da técnica, nome da etapa, visto ou não, e um ponteiro para a fonte de log que deveria tê-la capturado. Aqui, sinergia purple não é uma reunião conjunta; é o hábito de deixar para a equipe de detecção algo acionável, em vez de uma volta olímpica.

### 26.5 Proximidade de pagamentos

Aprovações extras antes de qualquer coisa perto de pagamentos. Qualquer coisa que toque sistemas adjacentes a pagamentos no TRB precisa de uma segunda assinatura antes de a cadeia continuar. A proximidade de pagamentos inclui o perímetro do gateway SWIFT, as filas de liquidação e os jump hosts que conseguem alcançá-las, mesmo quando o próprio gateway continua fora do escopo. Sam trata "perto" como uma propriedade do caminho de rede e das credenciais compartilhadas, e não do título do achado. Se um salto cairia num host capaz de falar com essas filas, ele pausa, registra o pedido e espera. Pular a pausa uma única vez bastaria para encerrar o engajamento e o estágio.

### 26.6 Sem kit de exploit

O curso continua sem oferecer desenvolvimento de exploits. O curso ensina encadeamento com fraquezas publicadas e ferramentas aprovadas; não ensina a escrever novos exploits. Os estudantes que pedem um kit são remetidos de volta aos cartões de método e ao catálogo de impactos. Esse limite mantém a sala de aula honesta sobre o que um banco autorizará e o que um programa universitário consegue supervisionar com segurança. Os próprios kits de Sam se limitam aos scripts fixados cujos hashes ficam no caderno de laboratório. Construir um payload personalizado para uma cadeia avaliada é reprovação, mesmo que o payload tivesse funcionado.

### 26.7 Ids de ativos nos diagramas

Os diagramas de cadeia usam os mesmos ids de ativos do FindingsDesk. Hostnames escritos à mão já causaram um link quebrado num apêndice; os ids tornaram o apêndice verificável mecanicamente. O FindingsDesk atribui um identificador estável a cada host e serviço em escopo. Diagramas que reutilizam esses ids podem ser validados por um script que percorre o apêndice e confirma que cada caixa ainda existe no inventário. Quando Sam usou um apelido para um jump host, o verificador do apêndice falhou e o achado ficou parado em revisão até o diagrama ser refeito. A lição ficou: rótulos bonitos pertencem à legenda em prosa, não aos nós do grafo. Os juniores agora copiam os ids do painel de inventário em vez de digitá-los de memória.

### 26.8 Catálogo de impactos

As provas de impacto permitidas para cadeias estão catalogadas (leitura entre usuários, mudança de configuração). "Domain admin" não é um impacto permitido em sala de aula no TRB. O catálogo de impactos é uma lista curta e assinada das provas que a sala de aula aceita. A leitura entre usuários de um registro não sensível e uma mudança de configuração reversível estão nela; tomar o domain admin, criptografar arquivos ou tocar pagamentos reais, não. O catálogo existe para que Sam não precise inventar o limite sob pressão. Quando uma cadeia poderia continuar rumo a um impacto proibido, o operador para e registra o que já está provado. A ambição que excede o catálogo é redirecionada para uma meta de detecção ou uma nota de remediação, e não para um salto mais arriscado.

### 26.9 Banner de parar no impacto

Os cartões de método mostram um banner "pare quando o impacto estiver provado". Sam mede a média de passos depois do impacto; quanto menos, melhor. O banner fica no topo de cada cartão de método, para ser a primeira linha que o operador vê ao abrir o cartão. Sam acompanha quantas ações as pessoas executam depois que a captura de tela do impacto já foi salva. Uma média em queda significa que a cultura está funcionando; uma média em alta dispara uma conversa rápida de orientação. A métrica é deliberadamente simples, porque painéis complicados convidam à manipulação. Os operadores que param de forma limpa recebem crédito no resumo do engajamento, o que torna a contenção visível para quem escreve as notas de desempenho.

### 26.10 Parar depois da leitura entre usuários

Depois da prova de impacto por leitura entre usuários, a próxima ação de Sam é parar, e não pivotar para admin. A última caixa do apêndice da cadeia dele é verde: "STOP — impacto demonstrado". Os juniores copiam a caixa nos próprios cartões. A cena é o momento de que todos se lembram: a leitura entre usuários está na tela, o rascunho do achado já nomeia o caminho e a tentação de continuar fala alto. Sam encerra a sessão, cola a caixa verde STOP como nó final e arquiva o caderno. Os juniores que o viram fazer isso uma vez começam a colar a mesma caixa nos próprios cartões. O ritual é pequeno, mas transforma uma regra abstrata num hábito que as pessoas conseguem imitar quando estão cansadas.

### 26.11 Sem simulações de ransomware

O catálogo de impactos proíbe simulação de ransomware em redes bancárias no curso. Alguém sempre pergunta; o catálogo responde antes que Sam precise. Estudantes vindos da cultura de capture-the-flag costumam supor que demonstrações de criptografia são permitidas. No TRB elas não são, nem nas faixas do laboratório que espelham os nomes da produção. O catálogo declara a proibição numa linha, para que Sam possa apontar para o papel em vez de discutir gosto. Perguntas como "e se criptografarmos só um compartilhamento de teste" continuam recebendo um não, porque a sala de aula não pode se dar ao luxo de uma história que soe como ransomware para um auditor. Provas de impacto mais seguras já ensinam as mesmas questões de privilégio sem esse teatro.

### 26.12 Verde significa contenção

As caixas STOP são verdes de propósito — a contenção é sucesso, não fracasso. O vermelho costuma marcar perigo; aqui, o verde marca o fim bem-sucedido de uma cadeia. A escolha da cor é pedagogia deliberada: parar é o resultado que o programa recompensa. Sam explica isso uma vez a cada turma e depois deixa os adesivos falarem. Quando um visitante pergunta por que a última caixa não é vermelha, um operador consegue responder sem chamar o supervisor. Códigos de cor que brigam com a cultura fracassam; códigos de cor que combinam com a cultura pegam.

### 26.13 Adesivos STOP

As caixas verdes STOP são adesivos que os juniores colam nos cartões impressos. A cultura é tátil. Cartões de método impressos ainda circulam na sala dos jump hosts, porque telas se apagam e o papel não. Os juniores colam um adesivo verde STOP no cartão na primeira vez que concluem uma cadeia sob supervisão. O adesivo é um pouco ridículo, e é justamente essa a ideia: torna a regra memorável e dá aos colegas algo para notar durante as revisões. Sam guarda uma folha extra na gaveta ao lado da impressora de crachás. Quando a folha acaba, alguém andou praticando, o que é um bom problema.

### 26.14 Pôsteres de impacto e parada

Pôsteres de ética de encadeamento ficam pendurados na sala dos jump hosts: "Impacto, depois pare". Os visitantes às vezes riem; os operadores, não. Sam observa os novos terceirizados lerem o pôster antes da primeira cadeia. O pôster não é decoração irônica. Os terceirizados que passam os olhos por ele e fazem piada ainda recebem uma orientação verbal, mas Sam anota quem parou o suficiente para ler. Quem trata o slogan como piada tende a ser quem pede mais um salto depois da prova. A sala dos jump hosts é onde os hábitos se formam, então a parede carrega a mesma mensagem dos cartões de método e do catálogo. A coerência entre papel, tela e conversa é o que faz a regra sobreviver às trocas de turno.

### Exemplo resolvido (TRB sintético)

Sam encadeia um fluxo não aprovado e um controle de sessão fraco para mostrar o risco de leitura entre usuários e, então, para.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX076 — Prova mínima.** O que significa prova mínima? *Rubrica:* 3 = parar assim que o impacto é demonstrado; nenhum pivô extra; 2 = parcial; 1 = tomada completa sempre; 0 = nada.
- **EX077 — Perto de pagamentos.** Que passo extra vem antes de testes adjacentes a pagamentos? *Rubrica:* 3 = aprovações extras/verificação das ROE; 2 = parcial; 1 = vago; 0 = nada.
- **EX078 — Documentação da cadeia.** O que pertence ao apêndice da cadeia? *Rubrica:* 3 = passos/horários/links de evidência; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

As cadeias ficam dentro das ROE, provam o impacto de forma mínima e são documentadas com clareza.

### Continue estudando — capítulo 26 de 40

[← Capítulo 25 (rascunho)](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 (rascunho) →](#ch-27)

<a id="ch-27"></a>

## Capítulo 27 — Verificação

### Objetivos de aprendizagem

Você vai (1) planejar retestes; (2) ler os laboratórios de cobertura; (3) encerrar somente com evidência.

### 27.1 Reteste

Mesmos métodos, janela acordada. Um reteste repete os passos originais da prova dentro de uma janela que o responsável e o testador aceitaram quando o achado foi registrado. Mudar o método no meio do reteste torna desonesta uma alegação de FIXED, porque o responsável pode ter corrigido apenas o caminho que foi demonstrado. Sam reserva a janela quando o achado chega, normalmente para cerca de duas semanas depois, para que a agenda não espere o pânico. Se o build testado tiver mudado, o reteste registra essa mudança em vez de inventar uma aprovação. O objetivo do exercício é a verdade sobre o encerramento, não uma caixa de seleção verde.

### 27.2 Laboratório de cobertura

O lab_coverage marca a T1190 como GAP.

```python
"""Lab 27: summarise synthetic purple-team results per ATT&CK technique."""
runs = [("T1078",True),("T1078",True),("T1078",False),("T1566",True),("T1566",False),("T1190",False),("T1190",False)]
from collections import defaultdict
d = defaultdict(lambda:[0,0])
for t, hit in runs: d[t][1]+=1; d[t][0]+=hit
for t in sorted(d): k,n=d[t]; print(f"{t} detected {k}/{n} {'GAP' if k/n<0.5 else 'ok'}")
```

Execute com `python3 lab_coverage.py`. Saída verificada:

```text
T1078 detected 2/3 ok
T1190 detected 0/2 GAP
T1566 detected 1/2 ok
```

O laboratório percorre uma lista curta de execuções sintéticas de purple team e imprime com que frequência cada técnica foi detectada. Os estudantes leem as proporções impressas antes de discutir ferramentas. Uma técnica que nunca é detectada é uma história de lacuna, e não um motivo para declarar que o SOC está quebrado. A orientação de Sam se concentra no enquadramento: amostras pequenas ainda podem justificar instrumentação quando a fonte de log já existe. Os estudantes que só celebram taxas altas de detecção perdem o valor de engenharia de uma falha honesta.

### 27.3 Encerramento

FIXED com evidência ou risco aceito assinado. O encerramento é um status FIXED sustentado pela transcrição de um reteste ou uma assinatura de risco aceito de alguém com autoridade para assumir o risco residual. Qualquer outra coisa deixa o ticket aberto. Sam se recusa a marcar FIXED a partir de um "corrigimos" verbal sem a mesma requisição que provou o problema. Risco aceito não é uma reprovação branda; é uma decisão documentada, com prazo de validade e um responsável. O FindingsDesk não deixa um ticket desaparecer num vago estado de "monitoramento" sem um desses dois finais.

### 27.4 Parcial

STILL OPEN mantém o ticket vivo. Quando um reteste mostra que o caminho foi estreitado, mas não fechado, o status continua STILL OPEN e o ticket permanece na fila do responsável. O progresso parcial é registrado nas notas, para que ninguém finja que o trabalho não aconteceu, mas progresso não é encerramento. Sam certa vez viu uma equipe comemorar uma regra de WAF que bloqueava o payload antigo dele enquanto uma variante com um caractere diferente ainda funcionava; o ticket continuou aberto e a comemoração passou para a correção seguinte. A honestidade sobre estados parciais impede que a liderança declare vitória num painel que mente.

### 27.5 Congelamento do escopo

Nenhuma nova caçada no dia do reteste. O dia do reteste serve para verificar achados conhecidos, e não para abrir uma nova caçada. Novas pistas vão para uma nota de estacionamento destinada à próxima janela de engajamento. O congelamento protege a janela de mudanças do responsável e mantém coerente o arquivo de evidências. Sam já viu retestes virarem dias de descoberta espalhados que não produziram nem um FIXED limpo nem um STILL OPEN limpo. A regra é publicada no convite de agenda do reteste, para que ninguém alegue surpresa. Se mesmo assim surgir uma pista nova crítica, ela vira um ticket de emergência separado, com as próprias aprovações, em vez de pegar carona no reteste.

### 27.6 Comunicar

Nota ao responsável no mesmo dia. Depois de um reteste, o responsável recebe no mesmo dia uma nota que declara FIXED, STILL OPEN ou risco aceito pendente, com um link para a transcrição. Esperar o relatório semanal cria boatos e trabalho duplicado. Sam escreve a nota antes de fechar o notebook, mesmo quando a notícia é decepcionante. A nota nomeia o hash do cartão de método, para que o responsável confirme que o mesmo build foi testado. Rapidez, aqui, é cortesia, não pressão. Uma nota atrasada obriga o responsável a perguntar aos colegas o que aconteceu, e é assim que começam as histórias erradas sobre status.

### 27.7 Histórias de GAP para o SOC

As histórias de GAP oferecidas ao SOC incluem fonte de log, técnica e uma ideia de detecção de exemplo — e não uma exigência de "comprar uma ferramenta". A nota de Sam sobre a T1190 apontava para os logs do WAF e da origem, já licenciados. Uma história de lacuna útil diz ao SOC o que observar com o que ele já possui. O texto de Sam sobre a T1190 nomeava os logs de bypass do WAF e os logs de acesso da origem, ambos já licenciados, e esboçava uma ideia de detecção que usava esses campos. Exigir um novo produto numa nota de lacuna costuma travar a conversa. Os engenheiros de detecção respondem mais rápido quando o pedido é concreto e barato. O item de backlog que veio em seguida citou a nota de Sam literalmente.

### 27.8 Agenda de retestes

As janelas de reteste são reservadas quando os achados são registrados, e não depois que os responsáveis entram em pânico. O modelo de Sam sugere uma data 14 dias depois. Reservar cedo transforma o reteste de uma crise numa rotina. O modelo propõe um intervalo de catorze dias, que dá aos responsáveis tempo para corrigir sem inventar um teatro de urgência. Se o responsável precisar de mais tempo, ele diz isso no ticket e a agenda muda com um motivo anexado. O administrador de Sam certa vez tentou empilhar cinco retestes numa só sexta-feira; a visão da agenda deixou a sobrecarga evidente antes que alguém se esgotasse. Janelas previsíveis são a forma de a verificação continuar gentil.

### 27.9 Do GAP ao backlog

As linhas GAP criam itens no backlog de detecção com ids de técnica. O PulseMap aponta para esses itens. Toda linha GAP no PulseMap precisa apontar para um item do backlog de detecção que carregue o mesmo identificador de técnica. O link é bidirecional, para que o refinamento encontre órfãos em qualquer direção. Sam registra um defeito de plataforma quando um GAP passa uma sprint sem id de backlog. O defeito é sobre o processo, e não sobre culpar o analista que registrou a lacuna. Os links impedem que o resultado do purple team vire um cemitério de capturas de tela.

### 27.10 A lacuna da T1190 vira um spike

O GAP da T1190 com n=2 vira uma história de spike de detecção: "instrumentar os logs de bypass do WAF". Duas semanas depois, o SOC tem uma regra em homologação. Um n pequeno ainda pode impulsionar a engenharia se for enquadrado como lacuna, e não como profecia de desastre. Duas falhas pareceriam fracas num slide sobre porcentagens de cobertura. Enquadradas como uma lacuna com uma fonte de log nomeada, elas viraram um spike de instrumentação de duas semanas que levou uma regra para homologação. O texto de Sam evitou palavras como "cego" e "falha crítica" e se ateve ao que estava faltando. O líder do SOC disse depois que o tom foi o motivo de a história ter andado. O tamanho da evidência e a utilidade da evidência são perguntas diferentes.

### 27.11 Hash do método nos convites

Os convites de agenda de reteste incluem o hash do cartão de método, para que os responsáveis preparem o mesmo build. A divergência de versões é inimiga de um FIXED honesto. Os responsáveis às vezes corrigem um build diferente daquele que Sam testou. Colocar um prefixo de oito caracteres do SHA-256 no convite força a divergência a aparecer antes de a sessão começar. Se os hashes diferirem, o reteste ou muda de alvo ou registra a divergência explicitamente. Sam prefere remarcar a carimbar FIXED num primo do build vulnerável. A honestidade sobre versões faz parte da ética da verificação.

### 27.12 Links bidirecionais de GAP

Os itens do backlog de detecção apontam nos dois sentidos para as linhas GAP do PulseMap. Um link de mão única morre em silêncio quando alguém renomeia um ticket. Links bidirecionais permitem que qualquer um dos lados perceba uma quebra durante o refinamento. A verificação semanal de Sam é uma consulta de cinco minutos por linhas GAP sem id de backlog e por itens de backlog cujo link para o PulseMap dá 404. Consertar essas quebras é tedioso e necessário. O valor do purple team está, em grande parte, no encanamento que mantém os sinais ligados ao trabalho. Quando os dois sentidos resolvem, um engenheiro de detecção consegue ir de uma falha até um ticket sem perguntar a Sam para onde foi a captura de tela.

### 27.13 Prefixos de hash nos convites

Os hashes dos cartões de método nos convites são prefixos SHA-256 de oito caracteres hexadecimais — o suficiente para perceber divergências. Oito caracteres hexadecimais são curtos o bastante para colar num campo de agenda e longos o bastante para tornar improváveis colisões acidentais dentro de um engajamento. Os digests completos ficam no caderno para quem quiser recalculá-los. Sam certa vez pegou uma divergência porque o prefixo no convite já não correspondia ao cartão no compartilhamento. O responsável tinha refeito o build durante a noite e esquecido de avisar. Prefixos curtos se pagam quando evitam um falso FIXED.

### 27.14 Refinamento do backlog com o PulseMap

O refinamento do backlog de detecção inclui o PulseMap uma vez por sprint. Linhas GAP sem ids de backlog são defeitos do refinamento, e não do SOC. Sam registra esses defeitos contra o processo da plataforma. Um refinamento que ignora o PulseMap vai inventando aos poucos um backlog paralelo de capturas de tela. Incluir a visão de GAP uma vez por sprint mantém honestas as duas listas. Quando Sam encontra um GAP órfão, ele registra o defeito contra o processo que deveria tê-lo vinculado, e não contra o analista que estava ocupado naquela semana. Defeitos de processo são mais baratos de corrigir do que a culpa cultural. A sprint termina com todo GAP aberto apontando para algum lugar real.

### Exemplo resolvido (TRB sintético)

O laboratório no estilo PulseMap mostra a T1190 com 0/2, GAP; o SOC prioriza a engenharia de detecção voltada ao público.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX079 — Linha de GAP.** O que o laboratório imprime para a T1190? *Rubrica:* 3 = detected 0/2 GAP; 2 = parcial; 1 = ok; 0 = nada.
- **EX080 — T1078.** A T1078 é GAP ou ok no laboratório? *Rubrica:* 3 = ok (2/3); 2 = GAP; 1 = ausente; 0 = nada.
- **EX081 — Regra de encerramento.** Quando um achado pode ser encerrado como FIXED? *Rubrica:* 3 = a evidência do reteste mostra que está fechado; 2 = parcial; 1 = apenas e-mail do responsável; 0 = nada.

### Síntese

A verificação combina a honestidade do reteste com as lacunas de cobertura de detecção.

### Continue estudando — capítulo 27 de 40

[← Capítulo 26 (rascunho)](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 (rascunho) →](#ch-28)

<a id="ch-28"></a>

## Capítulo 28 — Análise de falhas

### Objetivos de aprendizagem

Você vai (1) classificar causas de ferramenta, de processo e de pessoas; (2) conduzir revisões sem culpa; (3) transformar causas em correções.

### 28.1 Causas

Má configuração de ferramenta, lacunas de processo, ROE pouco claras, lacunas de habilidade — raramente "pessoas ruins". A análise de falhas no TRB começa separando as causas em má configuração de ferramenta, lacunas de processo, regras de engajamento pouco claras e lacunas de habilidade. A culpa pessoal é a última hipótese, não a primeira. Sam já viu revisões desperdiçarem uma hora discutindo quem clicou em quê enquanto o valor padrão de um menu suspenso continuava convidando ao mesmo erro. Nomear cedo a categoria sistêmica mantém a sala útil. Quando uma causa realmente é negligência individual, o relatório ainda separa isso das correções de plataforma e de processo que teriam tornado o erro mais difícil.

### 28.2 Linha do tempo

Fatos primeiro. Uma linha do tempo de falha lista fatos observáveis com horários antes que alguém ofereça motivações. Logs, carimbos de horário do chat e eventos do TrackScope vêm primeiro; as interpretações esperam. Sam se recusa a deixar uma revisão começar com uma história sobre quem foi descuidado. Depois que os fatos estão ordenados, as divergências sobre a causa viram divergências sobre a evidência, e não sobre o caráter. A linha do tempo é colada nas notas da revisão, para que leitores posteriores possam reconstruir o argumento. Se um fato não puder ter horário, ele é marcado como incerto em vez de ser arredondado numa narrativa arrumada.

### 28.3 Sem culpa

Buscar correções sistêmicas. Revisão sem culpa significa que o principal resultado é uma mudança em ferramentas, valores padrão, checklists ou materiais de treinamento, e não uma nota de desempenho. Sam continua orientando indivíduos, mas o ticket da revisão não pode ser encerrado só com orientação, a menos que a caixa de justificativa do modelo esteja preenchida. Equipes que pulam as correções sistêmicas repetem o mesmo incidente com outro nome. A prática vem emprestada da cultura de operações e é adaptada a engajamentos ofensivos, em que a vergonha viaja rápido. As pessoas dizem a verdade mais depressa quando a sala está caçando sistemas quebrados.

### 28.4 Deriva ou ataque

Decidir com evidência. Alguns resultados confusos parecem ataques quando são deriva de configuração, e o inverso também acontece. A revisão pergunta que evidência distinguiria os dois antes de escolher um rótulo. Sam certa vez perseguiu uma "intrusão" que era uma importação noturna de hosts desatualizados na CMDB. O PulseMap e os tickets de mudança costumam resolver a questão mais rápido do que a intuição. Rotular deriva como ataque desperdiça o tempo do SOC; rotular ataque como deriva atrasa a contenção. A decisão é escrita junto com a evidência que a definiu.

### 28.5 Ações

Responsável e data para cada causa. Toda causa aceita sai da revisão com um responsável nomeado e uma data de vencimento. Ações sem responsável são desejos. O modelo de Sam bloqueia "a equipe vai melhorar" como responsável; ele quer uma pessoa ou uma fila. As datas são curtas o bastante para importar e longas o bastante para serem reais. Quando uma ação atrasa, o atraso fica visível no mesmo quadro dos achados do engajamento. O encerramento da revisão de falha espera até que cada ação esteja concluída ou explicitamente adiada com assinatura.

### 28.6 Plataforma

Bugs do TrackScope também geram tickets de engenharia. Se a plataforma convidou ao erro, a engenharia recebe um ticket com a mesma seriedade de um achado. Sam registra esses tickets com a captura de tela do controle confuso e o id da revisão. O plantão da plataforma é convidado para as revisões de falha mesmo quando a sala acha que o erro foi humano, porque a interface muitas vezes induziu o clique. Corrigir o TrackScope uma vez evita uma geração de retreinamentos. Os operadores aprendem a tratar defeitos de ferramenta como resultados de primeira classe de uma revisão. Uma correção silenciosa de bug continua sendo uma correção de bug.

### 28.7 O plantão da plataforma nas revisões

As revisões de falha convidam o plantão da plataforma mesmo quando o erro parece humano. Muitas vezes, a interface convidou ao erro. Convidar o plantão muda a conversa de "quem errou o disparo" para "o que a tela sugeriu". No mês seguinte, o plantão mediu a queda dos cliques errados no mesmo controle e trouxe o gráfico para a retrospectiva da plataforma. O engenheiro de plantão não teria ouvido falar do padrão só por um ticket de treinamento. Revisões que excluem a equipe da plataforma tendem a produzir apresentações que ninguém coloca em produção. O convite é automático no modelo de agenda da revisão.

### 28.8 Affordances da interface

Se três analistas cometem o mesmo erro no TrackScope, a UX muda antes de mais treinamento. Sam registra tickets de UX com capturas de tela do controle confuso. Erros idênticos repetidos são um sinal de problema de design. Treinar a quarta pessoa é mais lento e menos confiável do que mudar o controle. Os tickets de UX de Sam sempre incluem uma captura de tela do antes e um estado proposto para o depois, para que os designers não fiquem adivinhando. O limite de três é uma heurística, não mágica; dois podem bastar quando o raio de impacto é alto. As affordances vencem os sermões quando o relógio é curto e a interface fala alto.

### 28.9 Limite de cinco porquês

As revisões param em cinco porquês ou na primeira correção sistêmica acionável. O teatro interminável de porquês é cortado. Os cinco porquês são uma ferramenta, não um ritual. Sam interrompe a cadeia quando a sala chega a uma correção que alguém pode assumir nesta sprint, mesmo que seja no terceiro porquê. O questionamento interminável vira um teatro que esgota as pessoas sem entregar mudança. O facilitador fica atento à primeira resposta sistêmica acionável e estaciona a filosofia mais profunda para uma revisão de design separada. Os limites mantêm a análise de falha mais curta do que o incidente que ela estuda.

### 28.10 Cinco porquês do inventário desatualizado

Os cinco porquês do inventário desatualizado param em "a API da CMDB não tinha campo de versão de schema". Ação: adicionar a versão de schema e um checksum no TrackScope. Treinar o estagiário que importou o arquivo desatualizado não é a ação principal. A sala poderia ter culpado o estagiário que clicou em importar. Em vez disso, o quinto porquê caiu num campo de versão de schema ausente e num checksum que o TrackScope nunca verificava. Essas duas ações de engenharia se tornaram o principal resultado da revisão; o estagiário recebeu uma nota de orientação tranquila como item secundário. Sam mantém essa cena no guia do facilitador porque ela mostra como é a ausência de culpa quando um júnior está no raio de impacto. Sistemas que não conseguem detectar importações desatualizadas vão continuar contratando bodes expiatórios.

### 28.11 Valor padrão do menu em negar

Um ticket de UX saído de uma revisão de falha mudou o valor padrão de um menu suspenso de "allow" para "deny". Os cliques errados caíram no mês seguinte. Os valores padrão são o destino. O controle parecia idêntico depois da mudança; só a opção padrão mudou. Os cliques errados que atormentavam a seleção de escopo caíram bruscamente no mês seguinte, sem um novo módulo de treinamento. Sam cita esse caso quando alguém argumenta que o trabalho de UX é cosmético. Os valores padrão autorizam ou bloqueiam silenciosamente milhares de cliques futuros. Revisões de falha que nunca tocam nos valores padrão deixam a mesma armadilha armada.

### 28.12 Capturas de tela de antes e depois

Os tickets de UX exigem uma captura de tela de antes e depois do controle que confundiu as pessoas. Frases como "o menu suspenso é confuso" não sobrevivem à passagem para um designer que não estava na sala. Capturas de tela de antes e depois tornam o pedido concreto e revisável. Sam as guarda com o prefixo ux- no mesmo caminho do cofre usado para a evidência dos engajamentos, para que o controle de acesso continue familiar. Tickets sem o par voltam da triagem. A disciplina também obriga quem reporta a propor um estado mais claro, em vez de apenas reclamar.

### 28.13 Caminho da evidência de UX

As capturas de tela de UX de antes e depois ficam no mesmo caminho do cofre da evidência dos engajamentos, com o prefixo ux-. Uma pasta extraoficial separada vira uma gaveta de bagunça que ninguém audita. Usar o cofre do engajamento com um prefixo claro mantém coerentes a retenção, as revisões de acesso e as retenções legais. Sam pode apontar uma única árvore ao jurídico quando surgem perguntas sobre o que foi capturado durante uma semana confusa. O prefixo também permite que a automação pule as imagens de UX ao montar os pacotes de evidência destinados ao cliente. Pequenas regras de nomenclatura evitam grandes dores de cabeça na fase de descoberta.

### 28.14 Caixa de seleção de plataforma ou processo

Os modelos de revisão de falha obrigam uma caixa de seleção "mudança de plataforma ou de processo?". Se nenhuma estiver marcada, a revisão está incompleta. Resultados apenas de treinamento precisam de justificativa explícita. A caixa de seleção é um quebra-molas contra o final preguiçoso em que todos concordam em se esforçar mais. Deixar as duas caixas desmarcadas reprova na validação do modelo que Sam integrou ao TrackScope. Resultados apenas de treinamento são permitidos quando justificados por escrito, por exemplo, uma violação deliberada de política sem lacuna de ferramenta. A maioria das revisões deveria entregar pelo menos uma mudança de plataforma ou de processo. A escolha forçada torna a cultura visível nos dados.

### Exemplo resolvido (TRB sintético)

O rastreamento de um falso acerto em produção mostra um feed de inventário desatualizado; Sam registra ações para a plataforma e para a CMDB.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX082 — Sem culpa.** O que uma revisão sem culpa busca? *Rubrica:* 3 = correções sistêmicas, não punição; 2 = parcial; 1 = bode expiatório; 0 = nada.
- **EX083 — Formato da ação.** Quais dois campos toda ação corretiva precisa ter? *Rubrica:* 3 = responsável e data; 2 = um; 1 = vago; 0 = nada.
- **EX084 — Feed desatualizado.** Por que um inventário desatualizado pode causar um acerto em produção? *Rubrica:* 3 = host errado classificado como em escopo; 2 = parcial; 1 = não pode; 0 = nada.

### Síntese

A análise de falhas produz correções sistêmicas com responsáveis, inclusive na plataforma.

### Continue estudando — capítulo 28 de 40

[← Capítulo 27 (rascunho)](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 (rascunho) →](#ch-29)

<a id="ch-29"></a>

## Capítulo 29 — Operações

### Objetivos de aprendizagem

Você vai (1) conduzir o fluxo de trabalho do dia; (2) coordenar com o SOC; (3) fazer a passagem entre turnos.

### 29.1 Abertura

Confirmar ROE, contatos e janela. A abertura é uma reunião curta e tediosa que confirma as regras de engajamento, os contatos nomeados e a janela exata de tempo antes que alguém toque num teclado. Sam trata o tédio como uma qualidade: surpresas pertencem aos achados, não à autorização. Cada participante diz em voz alta as condições de parada e o canal do SOC que vai usar. Se um contato estiver de folga, o substituto é nomeado antes de a janela abrir. Uma abertura que pula a confirmação é como começam as discussões sobre hora extra e os saltos fora do escopo.

### 29.2 Registro

Log de atividades contemporâneo. Os operadores escrevem o que fizeram enquanto faziam, e não de memória na manhã seguinte. O log de atividades fica ao lado do cartão de método e usa os horários do mesmo relógio que o SOC usa. Sam já viu logs reconstruídos inventarem uma confiança que a sessão bruta nunca conquistou. As notas contemporâneas também protegem o operador quando um alerta parece pior do que a ação executada. O log faz parte do pacote de evidências, então gírias e piadas ficam de fora.

### 29.3 SOC

Mensagens de início e de fim; esperar coordenação do ruído de alertas. O SOC recebe uma mensagem de início quando a janela abre e uma mensagem de fim quando ela fecha, mesmo que a sessão tenha sido silenciosa. O ruído de alertas é esperado; a coordenação é o que faz a confiança sobreviver a uma noite barulhenta. Sam cola o id do engajamento nas duas mensagens, para que os analistas possam filtrar sem adivinhar. Surpresas no meio da janela ainda recebem um aviso, e não a esperança silenciosa de que ninguém perceba. Equipes que pulam a mensagem de fim deixam o SOC vigiando fantasmas depois que o trabalho acabou.

### 29.4 Passagem de turno

Log e cofre valem mais que notas verbais. As passagens de turno usam o log de atividades escrito e os caminhos do cofre, e não um resumo no corredor. Notas verbais evaporam e se transformam. O modelo de colagem de cinco linhas de Sam obriga o operador que sai a nomear os cartões inacabados, as aprovações em aberto e a próxima ação segura. O operador que entra deve estar produtivo em poucos minutos. Passagens que precisam de um romance normalmente escondiam uma bagunça que deveria ter sido uma parada. No TRB, o operador que entra abre o caminho do cofre indicado na passagem antes de tocar em qualquer cartão, para que um caminho errado ou vazio apareça antes de o trabalho recomeçar, e não no reteste seguinte.

### 29.5 Fim

Parada obrigatória no fim da janela. Quando a janela termina, o trabalho termina. Os cartões inacabados passam para a próxima janela autorizada; não ganham mais cinco minutos. Sam pratica um exercício de puxar o cabo no jump host, para que a memória muscular vença a negociação. As discussões sobre a necessidade de hora extra pertencem à próxima conversa sobre as ROE, e não aos últimos minutos desta. As paradas obrigatórias mantêm a agenda honesta para o SOC e para as pessoas que vão dormir depois do turno. O SOC nunca deveria precisar adivinhar se a sessão barulhenta ainda está autorizada.

### 29.6 Higiene do plantão

Sono e credenciais reserva importam em testes de vários dias. Engajamentos de vários dias falham de jeitos comuns: operadores exaustos, tokens expirados e um notebook que não desbloqueia. Sam guarda credenciais reserva no cofre, e não em post-its, e protege o sono como um controle operacional. Um operador cansado que continua é um amplificador de risco, não um herói. A higiene do plantão também significa saber quem cobre se alguém adoecer no meio da janela. O programa avalia a sustentabilidade junto com a habilidade técnica. Operadores esgotados produzem achados que depois precisam de correções constrangedoras.

### 29.7 Parada obrigatória com o cabo puxado

Os exercícios de parada obrigatória incluem puxar o cabo de rede do jump host no instante zero. A memória muscular de Sam é parar de digitar antes de argumentar por mais cinco minutos. As discussões acontecem nas próximas ROE, não na hora extra. O exercício parece teatral até a primeira vez em que alguém tenta "só mais uma requisição" e o cabo já está fora. Sam quer que as mãos parem antes de o debate começar. As negociações de hora extra são registradas como pedidos de mudança das ROE, com assinaturas, o que mata as extensões casuais. Os operadores que odeiam o exercício normalmente admitem depois que ele os salvou de um relatório matinal confuso. Um teatro que impõe um limite real continua sendo um teatro útil.

### 29.8 Etiqueta do canal

O chat do engajamento proíbe capturas de tela de dados de clientes como piada. Sam modera com uma regra fixada e um único aviso. O humor vaza para o chat quando as pessoas estão cansadas, e dados de clientes não pertencem a piadas. A regra fixada é direta e o primeiro aviso é o último. Sam remove as postagens problemáticas e registra uma nota, se necessário. A regra protege o banco, o programa e o operador que, de outro modo, viraria um caso de advertência. Canais que toleram capturas de tela "inofensivas" acabam produzindo uma captura que não é inofensiva.

### 29.9 Contador de horas

Um bot anuncia as horas trabalhadas na janela. Ultrapassar o máximo publica um lembrete de parada. O bot de horas é um contador entediante que não liga para o embalo. No máximo configurado, ele publica um lembrete de parada no canal do engajamento, onde todos podem vê-lo. Sam trata o lembrete como determinante, e não como sugestão. A hora extra escondida se torna impossível quando o relógio fala em público. Quem desativa o bot perde o privilégio de conduzir janelas sem supervisão. Relógios públicos vencem promessas privadas quando o cansaço começa a editar o julgamento.

### 29.10 Cartão inacabado às 16:55

Às 16:55, o cartão inacabado de Sam é registrado como "próxima janela". Às 17:00, começa o exercício de puxar o cabo. Ele já salvou. O exercício é entediante quando a preparação é boa. A parte interessante da cena são os cinco minutos antes do exercício, quando Sam escolhe registrar o cartão inacabado em vez de correr contra o relógio. Exercícios entediantes são o objetivo; drama significa que alguém esperou demais. Os juniores que observam aprendem que salvar e parar é uma habilidade. A próxima janela herda um cartão claro, e não um mistério. A preparação transforma uma parada obrigatória de um precipício num meio-fio.

### 29.11 Avisos de desaceleração

Com 9,5 horas, o contador publica "desacelere". Com 10, publica "parada obrigatória se aproximando". Sam desacelera. Machismo está fora da política. O aviso antecipado de desaceleração existe para que as pessoas terminem as notas e fechem as sessões sem uma parada em pânico. Sam usa essa meia hora para estacionar o trabalho de forma limpa. Os operadores que ignoram a desaceleração e disparam até a parada obrigatória criam passagens de turno confusas. O machismo de quem aguenta mais tempo é eliminado da cultura por meio de orientação. O programa prefere perder meia hora de testes a ganhar uma hora de limpeza e desconfiança.

### 29.12 Link do modelo nos avisos de desaceleração

Os avisos de desaceleração incluem um link para o modelo de cartão inacabado. Um lembrete sem uma ferramenta ainda deixa as pessoas improvisando sob pressão de tempo. O modelo de cartão inacabado fica a um clique da mensagem do bot, então o caminho de menor resistência é o caminho correto. Sam revisa se os operadores realmente usaram o modelo quando as passagens de turno parecem magras. Links em alertas operacionais fazem parte de projetar para humanos cansados. Se o link quebrar, consertá-lo é um ticket de operações, e não um dar de ombros. Pessoas cansadas seguem o link mais próximo; coloque o certo mais perto.

### 29.13 Id das ROE nos cartões inacabados

O modelo de cartão inacabado inclui o id das ROE, para que a próxima janela herde o contexto de autorização. Um cartão inacabado sem o identificador das ROE é um quebra-cabeça para o próximo operador e um risco se a janela errada o pegar. O campo do modelo é obrigatório e validado. Sam já rejeitou cartões que diziam "continuar aquilo de ontem" sem id. O contexto de autorização precisa viajar com o trabalho. Herança sem identidade é como a deriva de escopo volta pela porta lateral. Uma linhagem clara das ROE até o cartão é o que mantém defensáveis os testes de vários dias.

### 29.14 Colagem de passagem em cinco linhas

As passagens de turno usam um modelo de colagem de cinco linhas. Sam rejeita romances em texto livre. O próximo operador deve estar produtivo em três minutos, não em trinta. Passagens longas em prosa escondem a incerteza dentro de parágrafos. Cinco linhas forçam escolhas: o que está aberto, o que está bloqueado, o que vem em seguida, onde está o cofre, para quem ligar. Sam devolve os romances com um pedido educado para usar o modelo. Novos terceirizados às vezes acham o modelo frio; eles se afeiçoam a ele depois da primeira assunção limpa. A brevidade, aqui, é respeito pelo turno que entra.

### 29.15 Agradecer as paradas antecipadas

A cultura da parada obrigatória inclui agradecer a quem para cedo com trabalho inacabado. Os reconhecimentos de Sam nas retrospectivas nomeiam os cartões inacabados que respeitaram o relógio. Os heróis da hora extra recebem orientação, não elogios. A diferença aparece em menos tickets de mudança emergencial depois das semanas de teste e em analistas do SOC que continuam confiando na agenda dos engajamentos. O elogio ensina à sala o que repetir. Agradecer as paradas limpas torna o trabalho inacabado socialmente seguro. Elogiar os heróis da hora extra ensina as pessoas a esconder o relógio. As retrospectivas de Sam tornam a distinção audível todas as vezes. A confiança do SOC é um indicador defasado de que a cultura está funcionando, e vale a pena protegê-la com agradecimentos constrangedores.

### 29.16 Reconhecimentos no boletim

Os reconhecimentos pelas paradas antecipadas aparecem no boletim mensal de operações. O reconhecimento público fora do canal da equipe mostra à liderança que a contenção é valorizada. Sam envia um ou dois nomes com os títulos dos cartões inacabados, nunca com detalhes de clientes. Pessoas que só ouvem falar de salvamentos dramáticos de última hora passam a acreditar que o drama é o trabalho. O item do boletim é curto de propósito. Uma cultura que nunca sai da sala dos jump hosts morre quando a sala muda. O profissionalismo discreto merece tinta tanto quanto os salvamentos barulhentos.

### Exemplo resolvido (TRB sintético)

A parada de Sam às 17:00 deixa um cartão inacabado agendado somente para a próxima janela autorizada.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX085 — Mensagem de início.** Cite quatro fatos de uma mensagem de início. *Rubrica:* 3 = id, escopo, janela, contato; 2 = três; 1 = um; 0 = nada.
- **EX086 — Parada obrigatória.** E se restar trabalho no fim da janela? *Rubrica:* 3 = parar; reagendar uma janela autorizada; 2 = parar; 1 = estourar o horário; 0 = nada.
- **EX087 — Meio da passagem.** Quais dois artefatos tornam segura uma passagem de turno? *Rubrica:* 3 = log de atividades e evidência no cofre; 2 = um; 1 = apenas verbal; 0 = nada.

### Síntese

Operações são abertura, trabalho registrado, visibilidade para o SOC e paradas obrigatórias.

### Continue estudando — capítulo 29 de 40

[← Capítulo 28 (rascunho)](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 (rascunho) →](#ch-30)

<a id="ch-30"></a>

## Capítulo 30 — Laboratório II

### Objetivos de aprendizagem

Você vai (1) executar os laboratórios de classificação e de reteste; (2) passar num exercício de parada; (3) entregar um minirrelatório.

### 30.1 Montagem

lab_rank + lab_retest + relatório de uma página. O Laboratório II pede aos estudantes que classifiquem achados com o lab_rank, os retestem com o lab_retest e escrevam um relatório de uma página com base no qual um responsável ocupado consiga agir. A montagem é intencionalmente pequena, para que a honestidade e a disciplina de parada continuem visíveis. Sam reprova relatórios vistosos que escondem um item STILL OPEN atrás de uma prosa confiante. Os scripts são fixados; os estudantes não trazem forks particulares. O laboratório recompensa uma linguagem de encerramento coerente mais do que pivôs engenhosos. Os responsáveis devem terminar a página sabendo o que corrigir primeiro e o que continua aberto.

### 30.2 Exercício de parada

Mensagem conforme em até dois minutos.

```python
"""Lab 30: compare synthetic before/after statuses for a TRB retest."""
before={"F1":"open","F3":"open","F4":"open"}; after={"F1":"closed","F3":"open","F4":"closed"}
for k in sorted(before): print(k, before[k], "->", after[k], "FIXED" if after[k]=="closed" else "STILL OPEN")
print("fixed", sum(after[k]=="closed" for k in before), "of", len(before))
```

Execute com `python3 lab_retest.py`. Saída verificada:

```text
F1 open -> closed FIXED
F3 open -> open STILL OPEN
F4 open -> closed FIXED
fixed 2 of 3
```

O exercício de parada cronometra a rapidez com que um estudante consegue enviar a mensagem de parada conforme quando o facilitador anuncia o fim do tempo. Dois minutos é a meta; procurar o modelo atrapalhado reprova no exercício, mesmo que o trabalho técnico tenha sido forte. Sam quer que a mensagem seja memória muscular antes de começarem as janelas reais. Os estudantes que discutem durante o exercício praticam a habilidade errada. A rapidez, aqui, é respeito pelo relógio, e não um concurso de digitação.

### 30.3 Honestidade

Deixar aberto o que está STILL OPEN. Se o lab_retest ainda mostrar um caminho aberto, o relatório precisa dizer STILL OPEN e explicar o que resta. Encerrar com base na esperança ou na garantia verbal de um responsável reprova no laboratório. A verificação automatizada de Sam procura as palavras de status quando o estado posterior sintético está aberto. Os estudantes às vezes sentem que a honestidade lhes custa nota; neste curso, a honestidade é a nota. O hábito se transfere para tickets reais, em que alegações falsas de FIXED saem caras. Um STILL OPEN doloroso hoje evita um falso FIXED no pacote de auditoria da semana que vem.

### 30.4 Pressão dos colegas

Recusar evidência divergente. Os colegas podem oferecer uma captura de tela cujo hash está "errado só em um caractere" ou um log de outro build. O movimento correto é recusar e capturar de novo. Sam roteiriza essa pressão no laboratório para que a recusa seja praticada em voz alta. Evidência quase certa é como a confiança morre diante de auditores e reguladores. Os estudantes que aceitam arquivos divergentes são reprovados, mesmo que a prosa esteja polida. Dizer não diante dos colegas é a habilidade que o roteiro de fato avalia.

### 30.5 Tempo limitado

Duas horas. O laboratório cabe em duas horas, incluindo o exercício de parada e o relatório. A expansão de escopo dentro do exercício é uma reprovação autoinfligida. Sam observa os estudantes que correm atrás de um quarto achado em vez de terminar a página. O tempo limitado ensina a priorizar da mesma forma que as janelas de engajamento. Terminar de forma limpa dentro do prazo vale mais do que um rascunho brilhante que perde o relógio. Os estudantes que terminam cedo ajudam os colegas com a redação, e não com caçadas extras. Sair com uma página coerente vale mais do que sair com um brilho inacabado.

### 30.6 Critério de aprovação

Parada + honestidade + relatório coerente. A aprovação exige uma parada no tempo certo, status honestos e um relatório que um responsável consiga usar sem ligar para o estudante. Cadeias engenhosas que falham em qualquer um dos três continuam reprovadas. Sam publica o critério antes do laboratório, para que ninguém o descubra no debrief. O critério espelha em miniatura as expectativas da produção no TRB. Teatro técnico sem disciplina operacional não aprova no curso. Os facilitadores pontuam os três pilares separadamente, para que uma cadeia deslumbrante não esconda uma parada frouxa.

### 30.7 Recusa por divergência de hash

Os roteiros de pressão dos colegas do Laboratório II incluem "o hash está errado só em um caractere". A resposta de recusa de Sam é sempre capturar de novo. Hashes quase certos são como a evidência perde a confiança de tribunais e reguladores. A fala roteirizada soa razoável sob pressão de tempo, e é por isso que ela é ensinada. A resposta modelo de Sam é curta: capturar de novo, não remendar o hash. Os estudantes ensaiam a frase até ela parecer comum. A integridade da evidência não é uma impressão; é um digest que confere. Cursos que nunca praticam a recusa produzem pessoas educadas que aceitam arquivos ruins.

### 30.8 Esqueleto do relatório

Os relatórios do Laboratório II usam um esqueleto com marcadores REQUIRED. A falta da explicação do STILL OPEN reprova na verificação automatizada que Sam escreveu. O esqueleto elimina os debates sobre formatação, para que a atenção fique no conteúdo. Os marcadores REQUIRED tornam as omissões evidentes tanto para humanos quanto para a CI. O verificador de Sam reprova seções vazias em vez de adivinhar a intenção. Os estudantes que apagam um marcador para esconder uma lacuna aprendem que o pipeline percebe. A estrutura é um auxílio à honestidade, e não burocracia por si mesma. Blocos REQUIRED vazios falham ruidosamente antes de um humano abrir o arquivo.

### 30.9 CI do esqueleto

Os PRs dos relatórios do Laboratório II falham na CI se as seções REQUIRED estiverem vazias. Sam gosta de honestidade mecânica. Integração contínua sobre prosa parece estranha até a primeira vez em que pega um status ausente. Sam prefere que um bot rejeite o pull request a depender só de um facilitador cansado. A honestidade mecânica escala entre turmas sem perder a paciência. Os estudantes podem iterar até a verificação passar, o que ensina a revisar sob uma regra clara. Os facilitadores continuam lendo pela qualidade; a CI só impõe a presença. O pipeline é um tutor paciente que repete o mesmo padrão todas as vezes.

### 30.10 A CI rejeita o "o responsável disse"

A CI do Laboratório II rejeita um relatório que marca F3 como encerrado com o comentário "owner said so". A mensagem de erro de Sam cita a regra do curso. A imposição mecânica vence o sermão. A cena é engraçada na primeira vez e séria na segunda. A garantia verbal não é evidência de reteste, e o verificador conhece a diferença. O texto de erro de Sam cita a regra do manual, para que as contestações sejam sobre a regra, e não sobre o humor do bot. Os estudantes atualizam o status para STILL OPEN e escrevem o que resta. Os sermões se apagam; as verificações que falham ensinam.

### 30.11 STILL OPEN quando o reteste está aberto

A CI do esqueleto procura a string STILL OPEN quando o lab_retest mostraria itens abertos. Os estudantes não conseguem esconder o que está aberto por omissão. A omissão é a forma mais branda de falso encerramento. O verificador compara o estado posterior sintético com o texto do relatório e exige as palavras desconfortáveis quando restam caminhos. Sam ajustou a verificação depois que uma turma retirou discretamente da página os itens abertos. Esconder trabalho não corrige sistemas. Tornar mecanicamente obrigatório o registro do que está aberto mantém o laboratório alinhado com a ética da produção. Palavras forçadas na página viram honestidade forçada no próximo ticket real do estudante.

### 30.12 Números de regra na CI

A mensagem da CI cita o número da regra do manual do curso. Mensagens de erro que só dizem "relatório inválido" convidam a discutir com a ferramenta. Citar a regra do manual permite ao estudante consultar a expectativa e corrigir o trabalho. Sam mantém os números de regra estáveis entre os períodos, para que as discussões antigas continuem fazendo sentido. As contestações citam a regra; não pedem ao facilitador que passe por cima de uma falha clara. A automação transparente conquista um respeito relutante. Citações claras transformam um X vermelho num guia de estudo, e não num beco sem saída.

### 30.13 As contestações citam a regra

Os números de regra do manual na CI facilitam as contestações: cite a regra, não discuta com o bot. Um caminho de contestação limpo reduz a temperatura na sala. Os estudantes que discordam precisam mostrar como a regra foi mal aplicada, o que é mais raro do que eles esperam. Sam prefere debater a redação do manual numa reunião de currículo a debater cada verificação reprovada caso a caso. O bot não é o vilão; regras pouco claras seriam. Expectativas numeradas mantêm os dois lados honestos. A justiça do processo importa tanto quanto a correção técnica num laboratório avaliado.

### 30.14 A melhor recusa do dia

Os debriefs do Laboratório II votam na melhor recusa do dia. O vencedor explica a redação que usou. Celebrar a recusa facilita a próxima. A recusa é socialmente constrangedora, então o curso a celebra de propósito. O estudante vencedor lê a frase exata que usou quando a evidência não conferia. Os colegas roubam boas formulações do jeito que, em outras culturas, roubam bons payloads. Sam quer que a recusa pareça um ofício. Uma sala que aplaude um não limpo vai produzir pacotes de evidência mais limpos.

### 30.15 Cartão de exemplo de recusa

Os vencedores da votação da melhor recusa podem atualizar o cartão de exemplo de recusa. O cartão de exemplo no pacote do laboratório é um documento vivo, mantido pelos vencedores recentes. Atualizá-lo mantém a linguagem atual e dá reconhecimento sem inflar as notas. Sam revisa as edições quanto ao tom e à exatidão antes de publicá-las. Os estudantes levam o cartão mais a sério quando foram colegas que escreveram as frases. Ser dono de pequenos artefatos constrói a cultura mais rápido do que só os pôsteres. Exemplos escritos pelos colegas vão mais longe do que as aulas do facilitador depois que o período termina.

### Exemplo resolvido (TRB sintético)

O lab_retest mostra F1/F4 FIXED e F3 STILL OPEN; o relatório de Sam mantém o F3 aberto.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX088 — Contagens do reteste.** Quantos FIXED e quantos STILL OPEN? *Rubrica:* 3 = 2 FIXED, 1 STILL OPEN; 2 = parcial; 1 = todos corrigidos; 0 = nada.
- **EX089 — Limite da parada.** Qual é o limite de tempo da mensagem de parada? *Rubrica:* 3 = dois minutos; 2 = rápido; 1 = no dia seguinte; 0 = nada.
- **EX090 — Tratamento do F3.** O relatório pode encerrar o F3 sem evidência? *Rubrica:* 3 = não; o F3 permanece aberto; 2 = não, sem dizer que o F3 permanece aberto; 1 = sim; 0 = nada.

### Síntese

O Laboratório II enfatiza parar rápido e relatar com honestidade os resultados do reteste.

### Continue estudando — capítulo 30 de 40

[← Capítulo 29 (rascunho)](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 (rascunho) →](#ch-31)

<a id="ch-31"></a>

## Capítulo 31 — Casos avançados

### Objetivos de aprendizagem

Você vai (1) analisar casos com vários achados; (2) priorizar sob pressão do conselho; (3) manter a ética quando a imagem e a integridade colidem.

### 31.1 Pacote

Achados classificados, reteste inacabado e o conselho pedindo para enterrar o F3 antes da divulgação de resultados. O pacote do caso avançado acumula pressão de propósito: uma lista classificada de achados, um reteste ainda aberto e um pedido do conselho para enterrar o F3 antes da teleconferência de resultados. Os estudantes precisam manter o achado visível enquanto redigem respostas da gestão que ficam ao lado dele, e não por cima. Sam recusa qualquer edição que apague o F3 da tabela classificada. O pacote treina a resistência com artefatos, e não com slogans. Os estudantes saem sabendo como é, no papel, um pedido para enterrar um achado.

### 31.2 Ética

Os achados ficam; respostas da gestão são permitidas ao lado deles. A ética, aqui, é concreta: o achado permanece no arquivo do engajamento, e a liderança pode anexar uma resposta explicando o prazo ou os controles compensatórios. Apagar não é responder. Sam ensina a diferença entre contextualizar o risco e escondê-lo. Trabalhos avaliados que apagam discretamente o F3 são reprovados, por mais eloquentes que sejam. A regra protege o banco do autoengano mais do que protege o ego do testador. Uma resposta que defende adiar a correção ainda pode ser honesta se a linha do próprio achado nunca se mover. Os estudantes marcam onde a resposta começa, para que ela não seja confundida com uma edição do achado.

### 31.3 Priorização

Primeiro, os fluxos adjacentes a pagamentos e os fluxos não aprovados do razão. Quando tudo parece urgente, a ordem ainda começa pelo dinheiro em movimento e pela integridade dos livros, não pelo volume de e-mails. A rubrica de classificação de Sam pondera o raio de impacto na direção da movimentação de dinheiro e da integridade dos livros contábeis. Achados cosméticos esperam, mesmo que um vice-presidente mande e-mail duas vezes. Os estudantes praticam dizer qual item vem primeiro e por quê, numa linguagem que um executivo consiga ouvir. Priorizar sem a lente do dinheiro é teatro num banco. Os empates se resolvem a favor do item que ainda não tem um controle compensatório em produção. A classificação falada é registrada nas notas do caso para o debrief.

### 31.4 Comunicação

Preparar versões para executivos e para engenheiros. Um achado precisa de duas leituras: uma versão executiva que declara a decisão, a data e o risco residual, e uma versão para engenheiros que traz os detalhes de reprodução e de correção. Sam gera as duas a partir dos mesmos campos do FindingsDesk, para que as palavras de severidade não possam derivar. Os estudantes que inventam uma pontuação executiva mais branda reprovam na verificação de coerência. Traduzir não é maquiar. Versões duplas claras impedem que resumos de corredor reescrevam o risco. As duas versões carregam o mesmo identificador de achado, para que ninguém possa alegar que descreviam problemas diferentes. A revisão por pares compara as duas páginas lado a lado antes de qualquer envio.

### 31.5 Jurídico

Envolver o jurídico se puder haver dever de divulgação — Sam escala, não decide sozinho. Quando um achado pode disparar deveres de divulgação, Sam escala para o jurídico com os fatos e não inventa uma conclusão jurídica. Estagiários e juniores, em especial, não podem negociar em particular com gerentes de produto sobre silêncio. O caminho de escalonamento está escrito no quadro de métodos. Os cenários avaliados punem a negociação solitária. O jurídico ainda pode dizer que nenhum dever se aplica; a questão é que não é Sam quem decide. As notas de escalonamento se atêm a horários, sistemas tocados e classes de dados envolvidas. Se o jurídico pedir mais detalhes, Sam acrescenta caminhos de evidência, e não opiniões.

### 31.6 Registro

Manter o pedido para enterrar o achado no arquivo do engajamento. Os e-mails de pressão pertencem ao arquivo, com um cabeçalho factual, mesmo quando a resposta é um não firme. Apagar o pedido protege sentimentos e destrói a história. Sam encaminha as tentativas de enterrar achados para o alias do CISO, para que a resposta vire memória institucional. Os estudantes praticam arquivar sem editorializar. As futuras aulas de ética precisam de artefatos, não de lendas. A redação de trechos sensíveis para as cópias de ensino acontece depois; o próprio arquivo do engajamento continua completo. Os cabeçalhos incluem o id do achado e o horário em que a mensagem chegou.

### 31.7 Encaminhar a pressão ao CISO

Os e-mails de pressão são encaminhados ao alias do CISO com um cabeçalho factual curto. Sam não discute calendários de divulgação de resultados sozinho com gerentes de produto. A resposta do alias vira o registro. Discutir sozinho convida a um meio-termo que nunca chega à governança. O alias força a conversa para um canal com retenção e testemunhas. O cabeçalho de Sam declara o que foi pedido e qual achado é o alvo, sem adjetivos. Os gerentes de produto aprendem que calendários de resultados não editam tabelas classificadas. A resposta, seja ela qual for, é o artefato com que o programa depois ensina.

### 31.8 SLA de escalonamento

Os e-mails com pressão para enterrar achados recebem uma confirmação no mesmo dia do alias do CISO, mesmo que a resposta completa espere. O silêncio parece consentimento. Confirmação não é concordância; é a prova de que a mensagem foi vista. Sam acompanha a mediana do tempo de confirmação nos slides de ética, porque o silêncio lento ensina a lição errada. As respostas no mesmo dia podem ser curtas: recebido, em análise, não alterem o achado enquanto isso. A análise completa pode levar mais tempo. A cultura morre no intervalo em que ninguém responde. A cobertura reserva do alias é escalada sempre que o titular está viajando. O modelo de confirmação fica ao lado das outras macros do engajamento.

### 31.9 Imagem versus integridade

Os slides de treinamento incluem um pedido anterior, anonimizado, para enterrar um achado e a resposta do CISO apoiando o testador. A cultura se ensina com artefatos. Slides que só dizem "aja com integridade" perdem para uma troca de e-mails real com trechos ocultados. A apresentação de Sam mostra o pedido, o encaminhamento e a resposta de apoio. Os estudantes veem que a recusa pode ser respaldada de cima. A pressão pela imagem passa a ser discutível, em vez de mítica. Os artefatos duram mais que os slogans quando chega a próxima temporada de resultados. A cada período, Sam confere se as ocultações ainda escondem pessoas vivas e tickers reais. Ocultações quebradas tiram o slide da apresentação até serem corrigidas.

### 31.10 A troca de e-mails impressa

O e-mail com o pedido para enterrar o achado e a resposta do CISO são impressos (com ocultações) na aula de ética. Os estudantes veem que a recusa tem apoio. Cultura é evidência, não slogans. Passar o papel de mão em mão muda a sala. Pessoas que supunham que os testadores ficam sozinhos leem uma frase do CISO que respalda o arquivo. Sam observa a mudança de postura mais do que escuta os pontos da discussão. A evidência de apoio é, ela própria, um controle contra pressões futuras. Aulas que só falam sobre coragem produzem uma coragem mais tímida. As cópias impressas são recolhidas no fim, para que digitalizações descontroladas não circulem. Uma folha de retirada registra qual mesa ficou com qual cópia durante o exercício.

### 31.11 Votar e depois ler a resposta

A aula de ética vota se teria recusado; depois, lê a resposta do CISO. A maioria muda o voto. Os artefatos ensinam. A votação vem primeiro para que seja possível ser honesto sobre o medo. Depois que a resposta é lida, muitos que votaram por atender ao pedido mudam de lado, e essa é a lição: o apoio se tornou imaginável quando o viram. Sam não envergonha ninguém pelo primeiro voto. Ele quer que as pessoas percebam como os artefatos reescrevem o que parece possível. Ensinar sem o segundo momento mediria apenas a ansiedade de base.

### 31.12 Logs de acesso da pasta de ética

Os artefatos de pressão com ocultações ficam na pasta de ética, com logs de acesso. Material de ensino sensível ainda precisa de responsabilização. Os logs de acesso mostram quem abriu a troca de e-mails ocultada e quando. Sam revisa os leitores inesperados a cada período com o líder do programa. Os logs desestimulam a fofoca empacotada e apoiam investigações se algo vazar. A transparência sobre o acesso faz parte de tratar os artefatos com respeito. Contas que só precisam dos slides da aula nunca recebem direitos sobre a pasta. As contas de serviço usadas para backup ficam listadas, para que não pareçam bisbilhoteiras.

### 31.13 Revisão de acesso a cada período

Os logs de acesso da pasta de ética são revisados a cada período em busca de leitores inesperados. Uma pasta sem revisão vira uma fábrica de boatos com senha. As verificações a cada período pegam credenciais compartilhadas e curiosidade ociosa de contas que não deveriam navegar por casos de pressão. Sam registra as esquisitices como notas de processo, e não como acusações públicas. A maioria das anomalias são erros banais; a revisão importa mesmo assim. A governança dos materiais de ensino espelha a governança da evidência dos engajamentos. As constatações da revisão alimentam o checklist de controle de acesso do período seguinte. O checklist é curto o bastante para que líderes ocupados de fato o concluam.

### 31.14 Medir o tempo de resposta do CISO

O tempo de resposta do alias do CISO é medido. Os slides de ética de Sam incluem a mediana do tempo de resposta aos e-mails de pressão. O silêncio lento é acompanhado como um risco para a cultura. O que é medido ganha equipe. Publicar a mediana mantém a liderança ciente de que o silêncio tem um custo além de um e-mail constrangedor. Sam toma o cuidado de nunca publicar conteúdo, apenas tempos. Quando a mediana piora, o programa pede cobertura reserva para o alias. O risco cultural pertence a um painel ao lado do risco técnico. Uma mediana em alta dispara uma conversa sobre equipe antes da próxima janela de resultados. A métrica é zerada a cada trimestre, para que crises antigas não escondam atrasos novos.

### Exemplo resolvido (TRB sintético)

Sam se recusa a retirar o F3, oferece um parágrafo de resposta da gestão e informa o supervisor e o CISO.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX091 — Pedido para enterrar.** Qual é a resposta correta a "retirem o F3 até a divulgação de resultados"? *Rubrica:* 3 = recusar; oferecer resposta da gestão; escalar; 2 = recusar; 1 = retirar; 0 = nada.
- **EX092 — Primeira prioridade.** Que classe de achado fica acima das mensagens de erro verbosas antes da divulgação de resultados? *Rubrica:* 3 = problemas adjacentes a pagamentos / de fluxo do razão; 2 = parcial; 1 = banners; 0 = nada.
- **EX093 — Registro.** Por que registrar o pedido para enterrar o achado? *Rubrica:* 3 = trilha de ética/auditoria; 2 = parcial; 1 = não é necessário; 0 = nada.

### Síntese

Os casos avançados testam a ética sob pressão da imagem tanto quanto a habilidade técnica.

### Continue estudando — capítulo 31 de 40

[← Capítulo 30 (rascunho)](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 (rascunho) →](#ch-32)

<a id="ch-32"></a>

## Capítulo 32 — Interfaces interdisciplinares

### Objetivos de aprendizagem

Você vai (1) trabalhar com jurídico, RH, SOC e desenvolvedores; (2) traduzir achados; (3) respeitar as restrições das outras profissões.

### 32.1 Jurídico

Contratos, divulgação, privacidade — Sam leva fatos, não conclusões jurídicas. Os parceiros do jurídico precisam de um pacote factual limpo: sistemas tocados, classes de dados, horários e se dados de clientes saíram do banco. Sam se recusa a redigir conclusões sobre estatutos de notificação de incidentes; essa é a faixa do advogado. A interface funciona quando os red teamers falam com precisão e ficam dentro da evidência. Adjetivos vagos obrigam os advogados a reinvestigar o que o testador já sabia. Uma folha de fatos de uma página anexada ao ticket vale mais do que um longo e-mail narrativo. Folhas de fatos viajam melhor entre as rotações do jurídico do que a memória heroica.

### 32.2 RH

Simulações que afetam a equipe precisam de caminhos pelo RH. Exercícios de phishing ou sociais que podem tocar registros de funcionários ou percepções de desempenho exigem um caminho pelo RH antes do lançamento. O checklist de Sam pergunta quem verá os nomes, quanto tempo os identificadores vivem e como as reclamações serão tratadas. Pular o RH uma vez criou uma queixa que durou mais do que o achado. O caminho é um contato nomeado e um limite de consentimento escrito, e não um aceno amigável no corredor. Achados que implicam a conduta de uma pessoa passam por revisão de linguagem do RH antes da distribuição ampla. Trabalho que impacta pessoas sem um caminho pelo RH é tratado como um defeito de escopo.

### 32.3 SOC

A engenharia de detecção consome tags ATT&CK e linhas do tempo. Os engenheiros do SOC só conseguem usar a saída do red team quando as tags de técnica e os horários das etapas estão presentes. Os diagramas de cadeia de Sam alimentam itens do backlog de detecção com esses campos já preenchidos. Uma captura de tela sem id de técnica é uma história; uma linha do tempo etiquetada é uma ordem de serviço. A sinergia purple falha quando os red teamers despejam lore e esperam que os analistas inventem a estrutura. As importações do PulseMap são rejeitadas se as tags obrigatórias estiverem em branco. Linhas do tempo etiquetadas são como o trabalho de detecção começa, e não como as discussões começam.

### 32.4 Desenvolvedores

Querem reprodução e padrões seguros de correção. Os desenvolvedores pedem passos exatos de reprodução e um padrão de correção que não derrube os pagamentos. Sam inclui uma requisição mínima, a resposta esperada e uma guarda sugerida que fica dentro das regras de mudança do serviço. Relatórios heroicos de exploit sem um formato seguro de correção desperdiçam sprints de engenharia. Os modelos do FindingsDesk obrigam um bloco de reprodução antes que um achado possa sair do rascunho. Quando a correção não está clara, Sam agenda uma conversa rápida de quinze minutos em vez de adivinhar na prosa. Passos reproduzíveis são a cortesia de que os desenvolvedores se lembram no trimestre seguinte.

### 32.5 Executivos

Querem decisões e datas. Os executivos precisam da decisão exigida, da data em que ela é necessária e do residual se esperarem. Sam mantém as notas executivas com menos de meia página e aponta para o detalhe mais profundo em vez de colá-lo. Briefings cheios de metáforas perdem para uma tabela com três linhas. A interface falha quando os testadores encenam expertise em vez de habilitar uma escolha. Toda nota executiva termina com uma única decisão pedida em texto simples, e as datas são datas de calendário. Um pedido claro é mais gentil do que uma digressão brilhante quando as agendas estão cheias.

### 32.6 Atrito

Compras e janelas de mudança são reais; planeje para elas. Achados brilhantes morrem quando a correção precisa de uma mudança de fornecedor durante um congelamento. Sam pergunta cedo quais remédios exigem compras ou uma janela de mudança e registra essas restrições ao lado do achado. Planejar para o atrito não é baixar a severidade; é sequenciar o trabalho que o banco realmente consegue fazer. As aberturas de engajamento incluem uma varredura de cinco minutos das restrições com o responsável. Congelamentos surpresa ainda acontecem; restrições documentadas tornam a remarcação mais calma. Alfabetização de calendário faz parte da maturidade técnica em empresas reguladas.

### 32.7 Pacotes de tradução gerados

Os pacotes de tradução são gerados a partir dos campos do FindingsDesk, para que os textos para executivos e para engenheiros não possam discordar sobre pontuações no estilo CVSS ou ids de ativos. Sam certa vez encontrou uma deriva nas palavras de severidade entre e-mails; os modelos a removeram. Os pacotes gerados puxam severidade, ids de ativos e títulos das mesmas linhas que o ticket usa. A reformulação manual é permitida para clareza, mas não para mudanças de pontuação. O incidente de deriva de Sam ensinou à equipe que o copia-e-cola entre públicos inventa duas verdades. Os modelos tornaram as versões duplas entediantes e coerentes. Os revisores conferem por amostragem se os números gerados batem com o ticket antes do envio. Uma fonte de números de severidade vale mais do que duas paráfrases inteligentes.

### 32.8 Glossário para leitores do jurídico

Um miniglossário mapeia "conduit", "control" e "finding" para leitores do jurídico. Sam o anexa quando o jurídico entra tarde. Palavras compartilhadas escondem significados diferentes entre as profissões. O miniglossário cabe numa tela e viaja como anexo, e não como palestra. Sam o atualiza quando um novo mal-entendido aparece numa conversa. O jurídico que entra tarde recebe o glossário no primeiro pacote, para que a segunda reunião seja mais curta. Discutir definições no meio de uma crise é como os prazos escorregam. Definições compartilhadas encurtam cada reunião seguinte em minutos que se acumulam ao longo de um trimestre.

### 32.9 Campos RACI do achado

Cada achado importante carrega um RACI minúsculo: quem corrige, quem verifica, quem aceita. Sam o preenche nos campos do FindingsDesk. Achados sem dono envelhecem e viram folclore. O RACI minúsculo fica no ticket, para que a responsabilização fique visível sem um ritual separado de gestão de programa. Sam não move um achado importante para em andamento sem os três nomes. Quem aceita precisa ter autoridade para assumir o risco residual; amigos da equipe não se qualificam. Campos RACI vazios bloqueiam as transições de status no fluxo de trabalho. Papéis nomeados transformam achados em trabalho agendado, em vez de culpa ambiente.

### 32.10 Confirmar a sugestão automática do RACI

Os campos RACI sugerem automaticamente os responsáveis a partir do registro de ativos. Sam ainda confirma com um humano. A sugestão automática sem confirmação certa vez enviou um achado a um ex-funcionário. A sugestão automática é uma conveniência que pode virar um incidente de confidencialidade. A ligação de confirmação de Sam é curta e registrada com um horário no ticket. O e-mail ao ex-funcionário virou um caso de ensino sobre confiar em diretórios depois de eventos de RH. Os humanos ainda vencem grafos desatualizados quando o que está em jogo inclui detalhes privados de vulnerabilidade. A confirmação é obrigatória mesmo quando a sugestão parece obviamente correta. A confirmação humana é um seguro barato contra o apodrecimento do diretório.

### 32.11 Quase incidente do responsável desativado

A sugestão automática do RACI certa vez escolheu um usuário desativado; a ligação de confirmação pegou o erro. Sam mantém a ligação mesmo quando está ocupado. Usuários desativados que ficam no registro de ativos são um modo de falha silencioso. A ligação de confirmação pegou o erro antes de o e-mail ser mesclado. Sam se recusa a pular a ligação em dias cheios, porque dias cheios são quando os atalhos se concentram. Uma verificação ao vivo de dois minutos vale mais do que um dia de recall. Os tickets da plataforma agora marcam em vermelho os responsáveis desativados ao lado da sugestão. Quase incidentes que mudam tanto a interface quanto o hábito são as revisões que valem a pena manter.

### 32.12 Horários de confirmação do responsável

As ligações de confirmação são registradas como "owner confirmed 15:04" no ticket. Uma caixa de seleção nua dizendo "confirmado" envelhece mal quando os auditores perguntam quem falou. A linha do log nomeia o ato e o relógio, para que leitores posteriores possam reconstruir a diligência. Sam cola a linha imediatamente depois da ligação, enquanto a memória está fresca. Tickets sem a linha voltam da revisão por pares. O formato é entediante de propósito, para que as pessoas de fato o usem. A diligência com horário sobrevive de forma limpa às trocas de equipe e impede que os auditores fiquem adivinhando. A disciplina parece pequena até a primeira vez em que evita um recall confuso.

### 32.13 Regra de confirmação em horário comercial

Os horários de "owner confirmed" precisam estar dentro do horário comercial, a menos que o plantão seja anotado. Confirmações noturnas acontecem, mas precisam de uma nota de plantão, para que ninguém assuma um sim acidental e sonolento. O validador de Sam avisa quando o horário cai fora do horário comercial sem a nota. A regra protege os responsáveis tanto quanto protege o processo. As notas de plantão nomeiam a rotação e o ticket que autorizou o contato fora do horário. A falsa urgência fica mais fácil de perceber quando o relógio é disciplinado. Regras de relógio tornam as alegações de urgência mais fáceis de auditar depois, quando as memórias discordam.

### 32.14 Plantão mensal com o jurídico

O plantão interdisciplinar convida o jurídico mensalmente. Sam leva um achado e pergunta como eles formulariam os deveres de divulgação. A tradução mútua se acumula. O plantão mensal vence o contato só em emergência. Sam leva um único achado ao vivo, sem drama, e pergunta ao jurídico como enquadrariam os deveres. O jurídico traz perguntas sobre a evidência que gostaria que os testadores capturassem mais cedo. Os dois lados saem com modelos mais afiados. A presença é curta e recorrente, para que a confiança se acumule. A prática recorrente de baixo risco vence a tradução rara de alto risco sob o calor do prazo.

### Exemplo resolvido (TRB sintético)

O pacote do F3 de Sam inclui uma proposta de regra de firewall para a rede e um checklist de negação no lado do código para a segurança da aplicação.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.
### Exercícios

- **EX094 — Papel do jurídico.** O que Sam leva ao jurídico? *Rubrica:* 3 = fatos/evidência/linha do tempo, não conclusões jurídicas; 2 = parcial; 1 = aconselhamento jurídico; 0 = nada.
- **EX095 — Pacote duplo.** Por que tanto a regra de firewall quanto o checklist da aplicação para o F3? *Rubrica:* 3 = precisa de controles de rede e de aplicação; 2 = parcial; 1 = só um é necessário; 0 = nada.
- **EX096 — Caminho do RH.** Quando o RH precisa ser envolvido? *Rubrica:* 3 = simulações/exercícios de phishing que afetam a equipe; 2 = parcial; 1 = nunca; 0 = nada.

### Síntese

O trabalho interdisciplinar traduz um achado nos artefatos de cada profissão.

### Continue estudando — capítulo 32 de 40

[← Capítulo 31 (rascunho)](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 (rascunho) →](#ch-33)

<a id="ch-33"></a>

## Capítulo 33 — Métodos de pesquisa II

### Objetivos de aprendizagem

Você vai (1) analisar resultados de purple team; (2) respeitar as ameaças à validade; (3) relatar a incerteza.

### 33.1 Análise

Usar intervalos; evitar p-hacking trocando métricas a posteriori. Os planos de análise nomeiam a métrica e o intervalo antes de a coleta de dados começar. Sam rejeita rascunhos de estudo que guardam três métricas reserva na gaveta para um slide mais bonito. Os intervalos comunicam a incerteza; as estimativas pontuais sozinhas convidam a uma precisão falsa. Trocas a posteriori só são permitidas como notas exploratórias claramente rotuladas como tal. O modelo de relatório do laboratório tem uma caixa de métricas travada que não pode ser editada depois que os dados chegam. O pré-compromisso é o que mantém honestos os estudos de sala de aula quando os resultados decepcionam.

### 33.2 Validade

Homologação, fadiga de alertas e contas compartilhadas ameaçam a generalização. As seções de validade precisam nomear ameaças que de fato se aplicam a ambientes no estilo do TRB. Homologação sem o ruído da produção, analistas afogados em alertas e contas de administrador compartilhadas distorcem o que uma pontuação de detecção significa. A rubrica de Sam desconta relatórios que só mencionam o tamanho da amostra. As ameaças vêm acompanhadas de uma mitigação ou de um limite explícito às alegações. O leitor deve saber até onde o resultado pode viajar. Alegar demais a partir de um laboratório arrumado é uma falha de validade, e não uma vitória de marketing.

### 33.3 Avaliação adaptativa

Os adversários se adaptam; conjuntos estáticos de testes envelhecem. Uma avaliação que nunca se renova vira um museu dos truques do ano passado. Sam registra quando atacantes ou sistemas internos mudam o suficiente para envelhecer um teste estático. A avaliação adaptativa agenda gatilhos de renovação, e não apenas revisões anuais. Uma pontuação perfeita num conjunto congelado pode esconder um ponto cego que se abriu no mês passado. O grupo de pesquisa trata o envelhecimento como um risco de primeira classe. Oponentes vivos exigem testes vivos se a linguagem de asseguração for significar alguma coisa. Os gatilhos de renovação pertencem ao plano, e não a um remorso culpado.

### 33.4 Divulgação dos limites

Todo estudo lista os limites no resumo. Limites enterrados na página doze é quase como se não existissem para leitores ocupados. Sam exige pelo menos três limites no resumo: ambiente, amostra e adaptação do adversário. A geração do PDF falha se a lista for mais curta. Nomear os limites cedo é uma qualidade que constrói confiança com revisores céticos. Estudantes que escondem limites para parecer fortes perdem pontos por educação científica. Resumos que admitem fraqueza ensinam melhor julgamento do que resumos que se gabam. Colocar os limites na frente treina o leitor a confiar no restante da página.

### 33.5 Compartilhamento de dados

Conjuntos sintéticos são preferidos para compartilhar. Logs brutos do TRB não saem do banco para um artigo de sala de aula. O padrão de Sam é um conjunto sintético com geradores documentados e verdade de referência conhecida. Quando traços reais forem essenciais, o jurídico e a privacidade aprovam uma versão fortemente sanitizada com um prazo de retenção. Compartilhar o gerador costuma ensinar mais do que compartilhar um dump. Os estudantes aprendem a publicar o suficiente para a reprodução sem exportar a vida do cliente. Conjuntos sintéticos também permitem plantar falhas conhecidas que os logs reais raramente rotulam com limpeza.

### 33.6 Revisita à ética

Reconferir as aprovações se os métodos se expandirem no meio do estudo. A expansão de escopo nos métodos pode ultrapassar a aprovação ética original. Sam pausa a coleta quando aparece uma técnica nova e registra uma emenda antes de continuar. Estudantes ansiosos para "só mais um salto" são o motivo de a regra existir. A emenda nomeia o que mudou e quem aprovou a expansão. Continuar sem ela transforma um estudo cuidadoso numa coleta fora do escopo. Revisitar a ética não é burocracia; é como a autorização acompanha a curiosidade. Uma pausa curta evita um projeto longo que ninguém pode defender.

### 33.7 Três ameaças à validade

As seções de validade listam pelo menos três ameaças todas as vezes: ambiente, tamanho da amostra e adaptação do adversário. O modelo de Sam não gera o PDF do relatório se a lista tiver menos de três. O mínimo de três ameaças impede o teatro vazio de validade. Ambiente cobre as diferenças entre homologação e produção que os estudantes adoram ignorar. Tamanho da amostra cobre a tentação de tratar n=2 como destino. Adaptação do adversário cobre o envelhecimento que os conjuntos estáticos sofrem. O travamento do modelo torna a lista um hábito, e não um item opcional. Relatórios que passam na verificação ainda precisam de prosa que ligue cada ameaça a um limite de alegação.

### 33.8 Log de adaptação

Quando atacantes ou sistemas mudam, Sam registra quais testes estáticos envelheceram. O log alimenta o desenho do próximo ensaio. O log de adaptação é uma lista datada do que mudou e de quais testes isso fere. Sam o revisa antes de propor um novo ensaio, para que o desenho não finja que o mundo parou. Entradas citam tickets de mudança ou notas de inteligência quando existem. Um log vazio num trimestre movimentado é, ele próprio, um sinal de alerta. O desenho do próximo ensaio começa perguntando o que o log tornou obsoleto. Renovações sem um log viram adivinhação vestida de metodologia.

### 33.9 Data de envelhecimento do teste

Os testes carregam uma data de revisão. Testes vencidos não podem sustentar alegações de asseguração até serem renovados. Todo teste empacotado tem uma data de revisão ao lado do nome. Testes vencidos ainda podem rodar para treinamento, mas não podem ser citados na linguagem de asseguração. O verificador de asseguração de Sam recusa citações cujos ids estão vencidos. A data força uma conversa sobre renovação antes que alguém cole um resultado antigo num slide do conselho. Treinamento e asseguração usam os mesmos artefatos sob regras diferentes. Separar esses usos evita que a prática de sala de aula se apresente como cobertura.

### 33.10 Idades dos testes no semáforo

As datas de envelhecimento dos testes ficam laranja aos trinta dias e vermelhas aos noventa. Testes vermelhos não podem ser citados em declarações de asseguração até serem reexecutados. Sam gosta mais de semáforos do que de parágrafos de política. A cor no painel vence um PDF de política que ninguém abre. Laranja significa agendar uma renovação; vermelho significa que a citação está bloqueada. Sam mostrou as luzes à liderança uma vez e a discussão sobre política encurtou. Os operadores entendem o vermelho sem um memorando. O código de cores torna o envelhecimento impossível de ignorar educadamente. As cores mudam automaticamente a partir das datas de revisão, para que ninguém precise lembrar de pintar o risco à mão.

### 33.11 Laranja agenda, vermelho bloqueia

Testes laranja são agendados; testes vermelhos bloqueiam citações. O checklist de asseguração de Sam pergunta literalmente "algum teste vermelho citado?" com uma caixa de não obrigatória. Agendar é a resposta construtiva ao laranja; bloquear é a resposta dura ao vermelho. A caixa de não do checklist é uma pausa forçada antes que alguém cole uma pontuação antiga. Sam trata uma caixa de não desmarcada como uma falha de construção, e não como um detalhe de formatação. O bloqueio protege o conselho de asseguração vintage. Agendar mantém o trabalho de renovação visível ao lado dos engajamentos. As duas respostas juntas transformam o envelhecimento de um sermão num fluxo de trabalho.

### 33.12 API do semáforo nas gerações

A API do semáforo é consultada pela geração do relatório; citações vermelhas fazem a geração falhar. As gerações de relatório chamam o serviço do semáforo e falham fechadas em citações vermelhas. Os autores veem qual id de teste derrubou a geração e precisam renovar ou remover a alegação. Sam prefere uma geração vermelha a um PDF polido com evidência podre. A verificação da API remove debates sobre se alguém "realmente citou" um teste velho. A falha mecânica ensina mais rápido do que a orientação depois do fato. Os autores aprendem a consultar as luzes antes de escrever a frase de asseguração.

### 33.13 Gerações offline falham fechadas

As gerações de relatório chamam a API do semáforo; as gerações offline falham fechadas. Gerações de conveniência em notebooks sem rede costumavam pular a verificação. Essa omissão era um buraco grande o bastante para uma alegação envelhecida passar. Sam mudou o padrão para falhar fechado offline, para que o caminho conveniente não seja o perigoso. Autores que precisam trabalhar em trânsito pré-buscam o estado do semáforo enquanto ainda estão online. A regra chateia as pessoas uma vez e depois evita surpresas constrangedoras. Falhar fechado offline alinha o laptop com o mesmo hábito da plataforma.

### 33.14 Proibição de "provar" sem limiar

O plantão de pesquisa proíbe a palavra "provar" a menos que um limiar pré-registrado seja citado. Sam toca um pequeno sino. A sala se autocorrige na terceira semana. O discurso casual de prova infla o que um estudo de sala de aula consegue carregar. O sino é um pouco ridículo e extremamente eficaz para interromper o hábito. Os palestrantes precisam citar o limiar pré-registrado ou reformular como suporte, sugestão ou lacuna. Na terceira semana, os colegas tocam o sino uns para os outros. Sam quer precisão linguística antes que os slides cheguem a patrocinadores que ouvem "provado" como certeza. Hábitos pequenos e barulhentos vencem memorandos silenciosos sobre modestia.

### Exemplo resolvido (TRB sintético)

Sam relata o GAP da T1190 com n=2 e se recusa a alegar "detecção zero para sempre".

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX097 — A posteriori.** Por que não mudar a métrica de sucesso depois de ver os dados? *Rubrica:* 3 = p-hacking / alegação viesada; 2 = parcial; 1 = tudo bem; 0 = nada.
- **EX098 — n=2.** Como Sam deveria falar de um GAP com n=2? *Rubrica:* 3 = incerteza honesta de amostra pequena; 2 = parcial; 1 = prova de zero para sempre; 0 = nada.
- **EX099 — Adaptativo.** Por que conjuntos estáticos de testes envelhecem? *Rubrica:* 3 = adversários e sistemas mudam; 2 = parcial; 1 = não envelhecem; 0 = nada.

### Síntese

A pesquisa une análise com intervalos, ameaças à validade nomeadas e limites honestos.
### Continue estudando — capítulo 33 de 40

[← Capítulo 32 (rascunho)](#ch-32) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 34 (rascunho) →](#ch-34)

<a id="ch-34"></a>

## Capítulo 34 — Projeto comparativo

### Objetivos de aprendizagem

Você vai (1) comparar duas abordagens de avaliação; (2) usar os critérios do TRB; (3) recomendar uma combinação.

### 34.1 Opções

Teste web trimestral no estilo WSTG versus exercício anual de cenário guiado por ameaças. O projeto comparativo coloca duas opções reais uma contra a outra, e não contra a fantasia de orçamento infinito. Os testes web trimestrais que seguem um método no estilo WSTG enfatizam a cobertura de regressão nas aplicações. Os exercícios anuais de cenário guiado por ameaças enfatizam caminhos realistas e o aprendizado do SOC. Sam proíbe uma terceira opção mágica que faz as duas coisas sem custo. A comparação só é honesta quando as opções cabem no calendário e na equipe que o banco realmente tem. Escolher entre alternativas concretas treina o julgamento que os slides de marketing evitam.

### 34.2 Critérios

Custo, cobertura, aprendizado de detecção, risco operacional e expectativas dos examinadores. Os critérios são fixados antes de as pontuações serem preenchidas, para que a resposta não possa dirigir a rubrica. O custo inclui horas da equipe e faturas de fornecedores; a cobertura pergunta quais classes de ativos são tocadas; o aprendizado de detecção pergunta o que o SOC leva embora; o risco operacional pergunta o quanto a produção é agitada; as expectativas dos examinadores perguntam o que os revisores externos já pediram. Sam trava a lista de critérios no apêndice. Critérios que mudam depois das pontuações são só teatro. Uma rubrica pré-registrada é o que transforma preferência em argumento.

### 34.3 Evidência

Usar resultados sintéticos do passado e intervalos de Wilson. A evidência da comparação vem de resultados sintéticos do passado, com intervalos de Wilson em torno das taxas de detecção e de cobertura. Estimativas pontuais sem intervalos fazem opções fracas parecerem certezas. Sam exige o mesmo tratamento de intervalo nas duas linhas, para que uma opção não ganhe por formato. Os dados sintéticos são rotulados como sintéticos em cada slide. Leitores que querem precisão falsa são remetidos de volta aos intervalos. Intervalos são como opções honestas sobrevivem ao contato com patrocinadores ansiosos.

### 34.4 Recomendação

A combinação recomendada mantém os testes web trimestrais para uma cobertura estável e financia um cenário guiado por ameaças a cada dois anos. O exercício anual guiado por ameaças pontuou bem em aprendizado e mal em capacidade de execução. Sam mostra a linha de capacidade antes da linha de aprendizado, para que o charme não vença a aritmética. A recomendação nomeia o que é cortado quando o orçamento aperta. Combinações sem um plano de corte são desejos. Uma recomendação que sobrevive a um corte de orçamento é uma recomendação que a finança consegue financiar. Sam anexa a tabela de opções pontuadas como apêndice, para que o comitê confira cada linha por trás da recomendação antes de votar.

### 34.5 Não objetivos

Não recomendar zero testes. Um não objetivo explícito é recomendar zero testes como medida de economia. Outro é fingir que slides de marketing de fornecedores são evidência. Sam imprime os não objetivos ao lado da recomendação, para que o atalho barato fique visível. Patrocinadores às vezes pedem a opção zero em particular; o slide responde em público. Nomear o que a análise se recusa a concluir é parte do desenho. Não objetivos mantêm a comparação longe de conclusões que o briefing nunca deveria alcançar.

### 34.6 Apresentação

Dez slides, decisões por último. A apresentação é limitada a dez slides, com a decisão no último. Colocar o teatro na frente e esconder o pedido é avaliado como falha. A orientação de Sam é declarar a combinação pedida no slide um numa frase e passar o restante justificando. Executivos que precisam caçar o pedido em metáforas perdem a paciência. O limite de slides também bloqueia apêndices disfarçados de narrativa. Clareza sobre a decisão é o produto; os slides são só o veículo.

### 34.7 Linha de capacidade de execução

As tabelas de comparação incluem uma linha de "capacidade de execução". O exercício guiado por ameaças todo ano pontua alto em aprendizado e baixo em capacidade — a menos que a equipe cresça. As pontuações de aprendizado seduzem os patrocinadores; as de capacidade mantêm os programas reais. A tabela de Sam fez a opção anual guiada por ameaças parecer excelente até a linha de capacidade ficar vermelha. Capacidade pergunta se as mesmas pessoas conseguem entregar sem abandonar os testes web. Sam se recusa a fingir que o heroísmo cobre um déficit de horas. A linha força uma conversa de contratação ou uma cadência mais lenta. Aprendizado sem capacidade é um programa que existe só nos slides.

### 34.8 Honestidade sobre o custo

As tabelas de comparação incluem horas da equipe, não só faturas de fornecedores. O trabalho web trimestral interno não é de graça só porque nenhum fornecedor enviou boleto. Custeamento só por fatura faz o trabalho interno parecer gratuito e enviesa a tabela na direção de ocupação que a equipe já não consegue terminar. Sam converte horas em custo com uma taxa publicada acordada com a finança. Horas internas aparecem na mesma coluna que as faturas. A honestidade evita a ilusão de que "fazer internamente" remove o custo. Patrocinadores merecem ver o preço completo. Custos ocultos de pessoal voltam como burnout e como janelas perdidas.

### 34.9 Dados da linha de capacidade

A linha de capacidade usa horas exportadas do controle de ponto, não palpites. Palpites comprimem projetos dolorosos e inflam os arrumados. O export encerra discussões sobre se o ano passado foi mesmo tão pesado. Sam mantém a história da subcontagem à mão para lembrar a sala por que a memória não é uma planilha. Os exports são hasheados no apêndice ao lado das pontuações. Capacidade sem um arquivo de horas é opinião. Dados que sobrevivem a um desafio da finança precisam de um arquivo, não de uma lembrança.

### 34.10 Cena da aritmética das horas

Linha de capacidade: no ano passado, o exercício guiado por ameaças consumiu 1.200 horas. Os testes web trimestrais consumiram 400. A opção a cada dois anos cabe; a anual não cabe sem contratação. A cena é um momento quieto de planilha, e não um discurso dramático. Mil e duzentas horas ao lado de quatrocentas fazem a escolha bienal guiada por ameaças parecer inevitável. Sam deixa a aritmética falar antes da retórica. Quem ainda quer a cadência anual precisa apontar para novas contratações, e não para entusiasmo. Aritmética é como as recomendações evitam o teatro do heroísmo. Números que cabem num slide ainda precisam caber num calendário.

### 34.11 Export do controle de ponto

O arquivo de horas é exportado do controle de ponto, não lembrado. A primeira estimativa feita à mão por Sam ficou 30% abaixo e quase aprovou uma cadência impossível. A memória comprime projetos dolorosos e infla os arrumados. O export encerra discussões sobre se o ano passado foi mesmo tão pesado. Sam mantém a história da subcontagem porque ela quase aprovou um plano que teria quebrado a equipe. Estimativas feitas à mão voltam pela porta lateral quando as pessoas estão com pressa. O export é chato e decisivo. Um arquivo chato venceu um plano carismático e impossível.

### 34.12 Export de horas no apêndice

O export hasheado de horas fica no apêndice comparativo. Pontuações sem o arquivo convidam a refazer a aritmética a partir de anedotas. O hash prova qual export sustentou a tabela. Sam aponta o apêndice quando alguém alega um total de horas diferente na sala. Transparência aqui é uma defesa, e não uma performance. A finança consegue refazer a linha de capacidade sem ligar para Sam à meia-noite. Apêndices que carregam os arquivos transformam discussões em verificações. O apêndice também declara quais códigos de controle de ponto foram contados como teste, porque as horas de relatório e de reteste são fáceis de deixar de fora por acidente.

### 34.13 Recusar estimativas de horas feitas à mão

Os apêndices comparativos se recusam a aceitar estimativas de horas feitas à mão sem um export do controle de ponto. A recusa é mecânica: sem hash, sem alegação de capacidade. Sam prefere atrasar uma data do conselho a abençoar uma linha chutada. Números feitos à mão voltam pela porta lateral quando as agendas apertam. A regra protege tanto os estudantes quanto os patrocinadores. Capacidade é um fato de arquivo ou não é um fato. Recusas mecânicas economizam discussões que a memória sempre perde.

### 34.14 O que você cortaria primeiro

As defesas do projeto comparativo perguntam "o que você cortaria primeiro se o orçamento cair pela metade?". Sam responde com qual trimestre de testes web encolhe e qual ano guiado por ameaças desliza. A pergunta do corte revela se o estudante entendeu a capacidade ou só decorou o slogan da combinação. A resposta nomeia o trimestre web que encolhe e o ano guiado por ameaças que desliza, com horas ao lado. Respostas que dizem "cortaríamos a qualidade um pouco em tudo" falham. Cortes nomeados são como as recomendações sobrevivem ao contato com a finança. Um plano de corte é parte da recomendação, e não uma pergunta surpresa. Estudantes que conseguem cortar com honestidade conseguem defender a combinação sob pressão.

### 34.15 Visual do calendário de dois anos

Ao apresentar a recomendação da combinação, Sam leva um calendário de uma página para dois anos, com o trimestre guiado por ameaças sombreado. Um calendário torna óbvias as colisões com congelamentos e visitas de examinadores. Sombrear o trimestre guiado por ameaças evita a reserva silenciosa em dobro das mesmas pessoas. Linguagem abstrata de combinação esconde essas colisões. Sam treina os estudantes a apontar para o sombreado quando alguém pede "só mais um exercício este ano". Calendários são evidência de capacidade. Uma página que mostra quando as pessoas estão ocupadas vence um slide que só afirma ambição.

### 34.16 PDF do calendário para a finança

O PDF do calendário de dois anos é o artefato que os conselhos encaminham à finança. A finança raramente encaminha apresentações com as metáforas intactas. O PDF do calendário de uma página sobrevive às cadeias de encaminhamento e ainda mostra quando dinheiro e pessoas são necessários. Sam gera o PDF a partir da mesma planilha da linha de capacidade. Artefatos que viajam sem o apresentador precisam carregar a aritmética sozinhos. O calendário é a combinação em forma de agenda. Se a finança só puder guardar um arquivo, que seja esse.

### Exemplo resolvido (TRB sintético)

Sam recomenda testes web trimestrais mais um exercício guiado por ameaças a cada dois anos, citando a linha de capacidade.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX100 — Maior regressão.** Qual abordagem captura melhor as regressões web a cada trimestre? *Rubrica:* 3 = trimestral no estilo WSTG; 2 = só guiado por ameaças; 1 = nenhuma; 0 = nada.
- **EX101 — Aprendizado de detecção.** Qual tende a ensinar mais ao SOC sobre caminhos realistas? *Rubrica:* 3 = exercícios de cenário guiados por ameaças; 2 = varreduras de banner; 1 = nenhuma; 0 = nada.
- **EX102 — Combinação.** Que combinação Sam recomenda? *Rubrica:* 3 = web trimestral + guiado por ameaças a cada dois anos; 2 = parcial; 1 = zero testes; 0 = nada.

### Síntese

A comparação pré-registrada critérios, evidencia com intervalos e recomenda uma combinação executável.
### Continue estudando — capítulo 34 de 40

[← Capítulo 33 (rascunho)](#ch-33) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 35 (rascunho) →](#ch-35)

<a id="ch-35"></a>

## Capítulo 35 — Proposta do projeto final

### Objetivos de aprendizagem

Você vai (1) delimitar um projeto final de ferramenta de escopo; (2) declarar não objetivos e métricas; (3) planejar riscos e ética.

### 35.1 Escopo

Construir uma ferramenta de diff de escopo para o TrackScope, com testes e uma avaliação curta em inventários sintéticos. O projeto final constrói uma ferramenta de diff de escopo que compara inventários do TrackScope ao longo do tempo e sinaliza deriva. Os entregáveis são a ferramenta, testes automatizados e uma avaliação curta em inventários sintéticos com falhas plantadas. Sam delimita o escopo para que um estudante consiga terminar em um período. Ambição sem limite vira uma coleção de conectores pela metade. A proposta nomeia o usuário — operadores que carregam inventários — e o trabalho que eles precisam fazer mais rápido. Um escopo estreito com propriedades de controle claras vence um sonho amplo sem testes.

### 35.2 Não objetivos

Os não objetivos impedem que a construção vire uma carreira em conectores. Sem integração com todo sistema de tickets, sem módulos de exploit e sem sumarizador de LLM na versão um. Sam imprime os não objetivos em negrito na capa. Amigos vão sugerir recursos na semana de construção; a capa responde sem um novo debate. Não objetivos são parte do desenho, e não uma desculpa. Uma proposta que não consegue dizer não ainda não está pronta para construção.

### 35.3 Métricas

As métricas de avaliação são precision e recall nas derivas de inventário plantadas, mais um resultado duro de falhar fechado em arquivos corrompidos. Painéis bonitos que engolem arquivos ruins não passam. Sam pré-registra as métricas na proposta, para que resultados decepcionantes não possam trocar o critério. Precision sem recall esconde perdas; recall sem precision esconde ruído. Falhar fechado é uma propriedade binária, e não uma média. Métricas que medem controle e precisão mantêm o projeto final honesto.

### 35.4 Riscos

Tempo, acesso a dados e disponibilidade de revisores. Os riscos principais são o tempo de calendário, o acesso a geradores sintéticos realistas e a disponibilidade de revisores para os checkpoints. Sam lista mitigações: um corte vertical cedo, geradores versionados no repositório do curso e horários de checkpoint pré-reservados. Riscos sem mitigações são preocupações, não um plano. A proposta trata a agenda do orientador como uma dependência. Esperar que a sorte resolva a fila de revisão é um plano de falha. Riscos nomeados com donos sobrevivem à primeira semana movimentada.

### 35.5 Orientador

Checkpoints a cada duas semanas. Checkpoints com o orientador a cada duas semanas mantêm a construção honesta. Cada checkpoint demonstra uma propriedade de controle, como falhar fechado, e não só telas novas. Sam reserva os horários na proposta, para que não sejam aspiracionais. Checkpoints perdidos disparam uma nota de risco, e não um silêncio educado. O orientador está ali para julgar propriedades, não para aplaudir o cromado. Cadência sem propriedades é só teatro de status. Cada demonstração abre com um arquivo corrompido antes de qualquer caminho feliz, e checkpoints perdidos disparam uma nota de risco em vez de um silêncio educado.

### 35.6 Ética

Somente inventários sintéticos. O projeto final usa somente inventários sintéticos; exportações reais do TRB ficam fora dos notebooks dos estudantes. Os geradores documentam como o realismo foi aproximado, para que os avaliadores não sejam enganados. Sam trata um CSV vivo colado "só para testar" como uma falha ética. A proposta cita o limite em inventário sintético na seção de ética e de novo nos não objetivos. Fronteiras repetidas são mais difíceis de "esquecer" na semana de construção. Ética aqui é escolha de dados, e não um parágrafo genérico.

### 35.7 Não objetivos em negrito na capa

Os não objetivos são impressos na capa da proposta em negrito. O orientador de Sam avalia se o estudante consegue apontar para eles sob pressão. O constrangimento é um controle subestimado. Quando um amigo sugere um sumarizador de LLM, Sam aponta para a linha em negrito em vez de inventar um argumento novo. Os orientadores perguntam pelos não objetivos de propósito nos checkpoints. Uma capa que esconde os não objetivos ensina a pessoa errada. Visibilidade é o que faz os limites funcionarem quando o entusiasmo sobe. Negrito na capa é barato; debates na semana de construção são caros.

### 35.8 Demonstrações nos checkpoints

A cada duas semanas, Sam demonstra falhar fechado, não cromado novo de interface. Os orientadores avaliam propriedades de controle. O cromado é sedutor; as propriedades de controle são a nota. O roteiro de demonstração de Sam abre com um arquivo corrompido e mostra a recusa antes de qualquer caminho feliz. Orientadores que só veem telas novas perdem regressões. Sam quer que a primeira impressão de cada checkpoint seja uma propriedade. Demonstrações que começam com o caminho feliz enterram as falhas. Controlar a ordem da demonstração é parte de controlar o produto.

### 35.9 Pôsteres de não objetivos na mesa

As impressoras do laboratório reimprimem pôsteres de não objetivos para a mesa de Sam durante a semana de construção. Um pôster na altura dos olhos vence um PDF enterrado numa pasta. A semana de construção é quando as ideias tentadoras batem o pico, então a impressora roda nessa hora de propósito. Visitantes que fazem piada do pôster ainda o leram. Sam aponta para ele sem precisar abrir o laptop. Artefatos físicos alcançam momentos que os arquivos perdem. Uma mesa que mostra os limites precisa de menos palestras.

### 35.10 Sugestão de LLM recusada

No meio da construção, um amigo sugere acrescentar sumarização de achados por LLM. Sam aponta para a capa e estaciona a ideia. A cena é comum, e é por isso que importa. Em vez de discutir a qualidade do modelo, ele deixa a capa da proposta falar e anota a ideia na lista da v2. O amigo não está errado sobre a utilidade em geral; está errado sobre o escopo desta versão. Estacionar com um ponteiro vence um debate longo que atrasa os testes. A proposta ganha quando diz não sem drama. Recusas calmas protegem o calendário melhor do que discussões brilhantes.

### 35.11 Sem LLM na v1 no pôster

O pôster de não objetivos inclui "nenhum recurso de LLM na v1". Os visitantes riem; Sam aponta para a proposta assinada. O riso costuma saudar proibições explícitas de ferramentas na moda. Sam trata o riso como prova de que o limite está visível. A proposta assinada respalda o pôster quando alguém alega que a regra era só informal. Versão um é permitida ser estreita. Moda que espera a versão dois ainda pode ser boa engenharia. Um pôster que sobrevive ao riso está fazendo o trabalho.

### 35.12 Foto do pôster no README

O README inclui uma foto do pôster de não objetivos na mesa. Examinadores remotos não veem a mesa física. A foto torna o limite auditável no repositório. Sam tira a foto na semana de construção, não num dia arrumado de antes. O README que só alega disciplina sem evidência é fraco. Uma imagem datada fecha o espaço entre o pôster e o arquivo. Documentação que mostra o ambiente de construção ajuda quem não esteve na sala. Leitores futuros que clonam o repositório veem o que a v1 recusou sem caçar e-mail, e Sam rejeita edições do README que cortam os não objetivos da imagem.

### 35.13 Fotografia datada do pôster

A fotografia do README dos não objetivos precisa estar datada dentro da semana de construção. Uma foto sem data poderia ser teatro de outro período. Sam exige a data da câmera ou um papel datado visível no enquadramento. Datar na semana de construção liga o limite ao tempo em que as tentações estavam altas. Orientadores conferem a data nos checkpoints. Teatro de outro período não conta. Evidência que carrega sua própria data resiste a desafios educados. Fotos antigas de outro período não contam, e os orientadores conferem a data nos checkpoints para que teatro de outro termo não passe.

### 35.14 Quiz de não objetivos nos checkpoints

Os checkpoints da proposta incluem um quiz de não objetivos: o orientador nomeia um recurso tentador; Sam deve recusar apontando para a capa. O quiz é curto e um pouco constrangedor de propósito. Dizer não em voz alta sob os olhos do orientador prepara Sam para amigos e patrocinadores. Atrasos de merge soam duros até alguém lembrar o custo de um desvio. O quiz transforma os não objetivos de texto em músculo. Orientadores que pulam o quiz perdem um ensaio barato. Praticar a recusa é parte de avaliar a proposta.

### Exemplo resolvido (TRB sintético)

Sam propõe uma ferramenta de diff de escopo com métricas de precision/recall e falhar fechado, e não objetivos em negrito na capa.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX103 — Não objetivo.** Cite um não objetivo válido da proposta. *Rubrica:* 3 = sem módulos de exploit (ou sem varredura ao vivo do TRB; ou sem integração com todo sistema de tickets); 2 = parcial; 1 = construir tudo; 0 = nada.
- **EX104 — Métrica.** Cite uma métrica de avaliação. *Rubrica:* 3 = precision e recall em derivas plantadas, ou comportamento de falhar fechado em arquivos de escopo corrompidos; 2 = parcial; 1 = "parece bom"; 0 = nada.
- **EX105 — Ética dos dados.** Que inventários o projeto final pode usar? *Rubrica:* 3 = somente inventários sintéticos; 2 = parcial; 1 = exportações reais do TRB; 0 = nada.

### Síntese

A proposta trava escopo, não objetivos, métricas, riscos e ética antes da construção.
### Continue estudando — capítulo 35 de 40

[← Capítulo 34 (rascunho)](#ch-34) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 36 (rascunho) →](#ch-36)

<a id="ch-36"></a>

## Capítulo 36 — Prática de campo ou comunitária

### Objetivos de aprendizagem

Você vai (1) concluir uma reflexão no estilo de estágio; (2) sanitizar relatórios; (3) traduzir métodos acadêmicos para operações.

### 36.1 Estágio

Acompanhar as operações de avaliação do TRB (sintéticas neste curso). A prática de campo neste curso usa um estágio sintético nas operações de avaliação do TRB, para que os estudantes nunca toquem sistemas reais de clientes. Acompanhar significa observar a entrada, o escopo, as janelas de teste e as passagens de turno com um caderno de perguntas. O diário de estágio de Sam proíbe inventar histórias de guerra que não aconteceram na faixa sintética. O objetivo são os modos operacionais, não técnicas secretas. Sintético não significa casual; as mesmas regras de sanitização e de brindes ainda valem. Cada dia de acompanhamento termina com Sam registrando qual decisão ele viu sendo tomada e quem tinha autoridade para tomá-la.

### 36.2 Sanitizar

Nenhum identificador de cliente nos textos acadêmicos. Os textos acadêmicos não podem conter identificadores de clientes, números de conta, IPs brutos nem hostnames que embutam nomes pessoais. Sam executa um checklist e um colega o rubrica com as iniciais antes de qualquer script de upload aceitar o arquivo. Um único sobrenome num hostname quase escapou uma vez; a captura do colega virou almoço e um slide de ensino. A sanitização é avaliada com o mesmo rigor do conteúdo técnico. Dados de cidadãos não têm lugar em espelhos acadêmicos, mesmo quando a história parece educativa. Capturas de tela são o artefato mais arriscado: o título de uma aba do navegador ou um prompt de terminal podem carregar o nome de um cliente mesmo quando o painel principal parece limpo.

### 36.3 Tradução

Intervalos de Wilson viram frases utilizáveis pelo conselho. O trabalho de estágio inclui traduzir intervalos de Wilson em frases que um conselho possa financiar sem perder a incerteza. Sam pratica formulações que mantêm a faixa visível em vez de colapsar num percentual heroico. Diretores que só ouvem estimativas pontuais aprovam programas frágeis. Os exercícios de tradução usam os mesmos resultados sintéticos do projeto comparativo. A cautela estatística que não consegue ser dita em voz alta não vai sobreviver à sala do conselho. Um exercício típico transforma "detectado 4 de 7, intervalo aproximadamente 25 a 84 por cento" em "pegamos cerca da metade, e a taxa verdadeira pode estar em qualquer ponto entre um quarto e a maior parte". Os diretores então perguntam quantas execuções a mais estreitaríam a faixa, que é a pergunta certa.

### 36.4 Conflitos

Políticas de brindes e jantares de fornecedores — seguir as regras do TRB. Eventos comunitários e de fornecedores seguem as políticas de brindes do TRB, sem exceções especiais para estudantes. Sam recusa jantares que pareceriam errados numa revisão posterior, mesmo quando parecem normais em blogs do setor. As regras de conflito fazem parte da prática de campo, e não de um apêndice de RH que ninguém lê. Quando tem dúvida, ele pergunta ao supervisor do estágio antes de aceitar qualquer coisa de valor. A aparência de influência é tratada com a mesma seriedade da influência real. Sam registra no diário de estágio qualquer hospitalidade de fornecedor que recusa, para que uma revisão posterior veja que o limite foi aplicado, e não assumido. Itens pequenos com marca seguem o mesmo limiar das refeições.

### 36.5 Diário

Semanal: aprendizado, premissa quebrada, pergunta. O diário semanal tem três linhas obrigatórias: o que foi aprendido, qual premissa quebrou e que pergunta resta. Diários só de vitórias ensinam vaidade; premissas quebradas ensinam operações. O supervisor de Sam lê a linha da pergunta e, muitas vezes, atribui a partir dela o próximo horário de acompanhamento. As entradas ficam livres de identificadores de clientes como qualquer outro artefato acadêmico. Um diário curto e honesto vale mais do que um diário longo e polido que esconde a confusão. Uma linha típica de premissa quebrada diz: "Eu assumi que o SOC viu nossa mensagem de início; ela foi para um alias sem monitoramento." Essa linha virou uma correção de runbook na semana seguinte, que é exatamente para o que o diário serve.

### 36.6 Saída útil

Deixar para trás uma melhoria de runbook. Todo estágio precisa deixar uma melhoria concreta de runbook que o anfitrião possa manter. O que Sam deixou foi um modelo esclarecido de mensagem de parada que os técnicos de fato colavam. Turismo com crachá termina quando a árvore de arquivos do anfitrião permanece inalterada. As melhorias são pequenas de propósito, para que possam ser revisadas e mescladas. A utilidade se mede pelo que permanece depois que o crachá do estudante deixa de funcionar. A mudança de Sam tinha três linhas: o id do engajamento, o horário de fim da janela e o alias do SOC, colocadas no topo do modelo, onde mãos cansadas olham primeiro. O anfitrião a mesclou depois de uma revisão e ainda a usa, que é a evidência de que o estágio importou.

### 36.7 Cronômetro do que se deixa

O teste do que se deixa usa um cronômetro: o técnico anfitrião ganha quinze minutos sozinho. Sam pode responder perguntas de esclarecimento, mas não tocar no teclado. Tocar no teclado significa que o que se deixou falhou. O cronômetro é duro e esclarecedor. Se o técnico não consegue terminar sem as mãos de Sam, a documentação falhou mesmo que a ferramenta funcione. Respostas de esclarecimento são permitidas; assunção silenciosa do controle, não. Sam observa o relógio mais do que a tela durante o teste. O sucesso sem as mãos é a única nota do que se deixa que conta. As falhas são registradas como defeitos de documentação, com o passo exato em que o técnico travou.

### 36.8 Checklist de sanitização

Antes do upload acadêmico, Sam executa um checklist: nomes, números de conta, IPs, hostnames. Um colega o rubrica com as iniciais. O checklist é entediante de propósito, para que seja concluído. As iniciais do colega criam responsabilização sem uma segunda reunião completa de revisão. Sam nunca rubrica o próprio formulário. A automação de upload procura o campo das iniciais antes de aceitar o PDF. Dois humanos e um script vencem um autor apressado com boas intenções. A ordem do checklist importa: nomes primeiro, porque se escondem nos lugares mais variados; depois números de conta; depois identificadores de rede. Hostnames vêm por último porque precisam da leitura mais lenta, letra por letra, contra a lista de clientes.

### 36.9 Caixa de iniciais do colega

Formulários de sanitização sem as iniciais do colega são rejeitados pelo script de upload acadêmico. A rejeição mecânica elimina discussões sobre se um amigo vai rubricar depois. Sam aprendeu a reservar o tempo do colega antes do prazo de upload, e não depois. Caixas de iniciais em branco são tratadas como assinaturas ausentes em achados. A grosseria do script é um controle de privacidade. Se a caixa estiver vazia, o arquivo simplesmente não sai da estação de trabalho. O script confere se as iniciais diferem das do autor e se o colega está na lista da turma atual, então uma caixa emprestada ou autoassinada ainda falha.

### 36.10 Captura do sobrenome no hostname

As iniciais do colega na sanitização certa vez pegaram um hostname contendo o sobrenome de um cliente. Sam paga o almoço do colega. Checklists com dentes tornam a gentileza fácil. A captura foi pequena e enorme. Um hostname que parecia técnico ainda carregava uma pessoa. O almoço foi agradecimento e um sinal público de que capturas são bem-vindas. Checklists sem dentes produzem heróis solitários; checklists com dentes produzem almoço. Celebrar a captura ensina o próximo colega a olhar com atenção. O hostname seguia um hábito antigo de nomenclatura em que servidores de agência carregavam o sobrenome do gerente de conta. Depois da captura, Sam acrescentou uma linha de padrão de hostname ao checklist, e a equipe anfitriã abriu um ticket para aposentar essa convenção.

### 36.11 Escolher colegas rigorosos

O colega de sanitização certa vez foi o crítico mais rigoroso de Sam. Ele escolhe colegas rigorosos de propósito. Colegas gentis perdem sobrenomes em hostnames. Gentileza e rigor são serviços diferentes. Sam agenda o crítico quando o arquivo mais importa. Revisões de amizade ainda acontecem para o tom; a sanitização quer olhos afiados. Colegas rigorosos são agradecidos de forma específica, para que continuem dizendo sim. Selecionar pela severidade na revisão é uma escolha profissional, não uma falha social. Sam mantém uma lista curta de quem pegou o quê em revisões anteriores e reserva a pessoa cujas capturas combinam com o risco do artefato: hostnames vão para o colega que achou o sobrenome, e tabelas vão para quem enxerga dígitos de conta soltos.

### 36.12 Juramento de privacidade e portões do formulário

As iniciais do colega na sanitização são um campo obrigatório do formulário PDF; em branco, o upload falha. Sam escolhe colegas que já pegaram erros dele, não amigos que passam os olhos. O script de upload rejeita formulários com menos de 10 KB como provavelmente em branco. A pedanteria de processo protege cidadãos cujos nomes nunca devem entrar em espelhos acadêmicos. Essa frase é o juramento de privacidade do capítulo. Existem vários portões porque qualquer portão sozinho acaba falhando. Quem já capturou erros tem prioridade quando Sam escolhe um colega. Arquivos minúsculos são suspeitos mesmo quando os campos parecem preenchidos numa captura de tela. A frase do juramento é assinada de novo no cartão do foyer do cofre. A pedanteria, aqui, é lealdade a pessoas que nunca vão ler a tese.

### 36.13 Portão de tamanho de formulário em branco

O portão de tamanho de formulário em branco certa vez pegou um colega que enviou a foto de uma tabela vazia. A pedanteria vence. A fotografia de uma tabela vazia é um truque antigo contra validadores fracos. O portão de tamanho mais a validação dos campos o impediu. Sam documentou a tentativa para que o próximo autor do validador não removesse a verificação como paranoia. Histórias de processo pertencem ao guia do facilitador ao lado do caminho feliz. A preguiça adversária dentro do curso ainda é útil para endurecer os uploads. O limiar foi definido medindo formulários genuinamente preenchidos, que nunca caíam abaixo do limite.

### 36.14 Cartão do juramento de privacidade no foyer

A frase do juramento de privacidade é assinada no cartão do foyer do cofre. O cartão do foyer fica visível para quem recolhe um crachá para trabalho no cofre. Assinar é rápido e um pouco solene, o que ajuda a memória. Sam observa os novos estagiários assinarem antes do primeiro dia de acompanhamento. Os cartões são arquivados por período, para que o ritual tenha um registro. A assinatura pública liga os modos de privacidade à entrada, e não a uma página não lida do manual. Quem se recusa a assinar não recebe acesso ao cofre naquele período; na prática, a pergunta que isso levanta é uma conversa, e não um confronto.

### Exemplo resolvido (TRB sintético)

A reflexão sanitizada de Sam descreve um exercício de parada sem nomear clientes ou funcionários reais.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX106 — Sanitizar.** O que os textos acadêmicos precisam remover? *Rubrica:* 3 = identificadores de clientes / especificidades sensíveis; 2 = parcial; 1 = vago; 0 = nada.
- **EX107 — Trio do diário.** Quais três linhas vão no diário semanal? *Rubrica:* 3 = aprendizado, premissa quebrada, pergunta; 2 = duas; 1 = uma; 0 = nada.
- **EX108 — O que se deixa.** Cite algo útil para deixar. *Rubrica:* 3 = melhoria de runbook / checklist; 2 = parcial; 1 = malware; 0 = nada.

### Síntese

A prática de campo é reflexão sanitizada mais algo que o anfitrião conserva.
### Continue estudando — capítulo 36 de 40

[← Capítulo 35 (rascunho)](#ch-35) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 37 (rascunho) →](#ch-37)

<a id="ch-37"></a>

## Capítulo 37 — Seminário de revisão de evidências

### Objetivos de aprendizagem

Você vai (1) apresentar evidência sob cronômetro; (2) criticar com checklist; (3) capturar ações datadas.

### 37.1 Formato

20 minutos de apresentação, 20 de crítica, 10 de ações. O relógio do seminário é rígido: vinte minutos para apresentar a evidência, vinte para criticar e dez para capturar ações datadas. Aplausos que comem a faixa das ações são uma falha de facilitação. Sam cronometra com um timer visível, para que ninguém discuta o limite. Apresentações que estouram o tempo perdem a faixa de crítica, e não ganham minutos extras. A disciplina do relógio é parte do que o seminário ensina sobre engajamentos reais. Uma sala que respeita o relógio produz notas que os examinadores conseguem ler.

### 37.2 Checklist

Os revisores trabalham a partir de um checklist que cobre clareza de escopo, hashes de evidência, racional da severidade, privacidade e overclaim. Revisões de vibe em texto livre perdem os mesmos buracos todas as vezes. Sam imprime o checklist nas mesas. Itens sem marca viram a primeira onda de feedback. Checklists tornam a crítica comparável entre apresentadores. Um checklist compartilhado também ensina os apresentadores o que preparar antes de subir ao palco.

### 37.3 Feedback

Referências específicas a linhas; sugerir correções. Feedback útil cita números de linha ou ids de figura e sugere um formato de correção. Comentários como "aperte isso" não ensinam nada acionável antes do próximo rascunho. Sam modela o hábito apontando para a linha e propondo uma frase substituta. Elogios sem âncora são gentis e inúteis para a revisão. A crítica específica é um presente disfarçado de desconforto. Apresentadores que pedem exemplos de redação avançam mais rápido do que os que só defendem o texto atual.

### 37.4 Receber

Escrever ações; evitar debater cada ponto ao vivo. Receber crítica significa escrever ações, e não vencer a sala. Debater ao vivo cada ponto queima a janela de dez minutos das ações. A orientação de Sam é marcar concordo, discordo ou preciso pensar, e seguir em frente. Debates pertencem a threads depois do seminário, com links profundos. Uma lista de ações no fim é o produto; um debate vitorioso não é. Apresentadores que escutam com a caneta na mão terminam com um quadro mais limpo.

### 37.5 Comparar

Opcionalmente comparar com um checklist de metodologia publicado (PTES/WSTG), não com o Instagram. Comparações opcionais usam checklists de metodologia publicados, como trechos de PTES ou WSTG fornecidos no pacote do curso. Lore do Instagram e mitos de corredor estão fora dos limites. Sam traz a página do checklist quando alguém alega que "todo mundo pula hashes". Metodologia publicada ancora a crítica em algo que sobrevive ao semestre. Comparar com a moda ensina o hábito errado. Fontes que os examinadores reconhecem mantêm o seminário auditável.

### 37.6 Registro

Nota do seminário arquivada com o projeto final. A nota do seminário é arquivada ao lado dos materiais do projeto final, para que os examinadores vejam a trilha de crítica. As notas incluem marcas do checklist, ações com responsáveis e quaisquer recusas. Sam trata uma nota ausente como um buraco no pacote de evidência do projeto final. Memória não é um arquivo de seminário. Examinadores que perguntam o que mudou depois da crítica merecem um artefato. Notas curtas e datadas vencem paráfrases longas escritas uma semana depois.

### 37.7 Recusar com motivo

Feedback recusado no seminário exige um motivo escrito que o apresentador aceita. "Não gostei" não fecha o item. Recusar é permitido; recusar sem explicação não é encerramento. Escrever o motivo muitas vezes revela se o comentário estava certo. A história de Sam das seis abertas é contada para mostrar o custo de limbos educados. Recusas entram na máquina de estados ao lado de corrigido e risco aceito. Motivos tornam as recusas revisáveis pelo orientador. Um motivo fraco costuma virar uma correção dois dias depois.

### 37.8 Validade das ações

Ações do seminário com mais de catorze dias sem mudança de estado acionam um aviso a Sam. Ações envelhecidas não são progresso. A validade transforma o limbo educado num aviso que exige mudança de estado. Sam prefere recusar de forma limpa a fingir que uma ação ainda está viva. Catorze dias combinam com a cadência dos checkpoints do projeto final. Avisos incluem o link profundo, para que a ação possa recomeçar em segundos. Progresso é mudança de estado, não intenção. Quadros que envelhecem em silêncio ensinam que a crítica era só teatro.

### 37.9 Máquina de estados dos comentários

Os estados dos comentários são aberto, corrigido, recusado, risco aceito. O rastreador de Sam proíbe outros. Status em texto livre inventam mentiras reconfortantes como "meio pronto". Os quatro estados permitidos cobrem resultados honestos sem poesia. Risco aceito exige uma autoridade, não um colega. Sam agradece ao software pedante quando ele rejeita criatividade à meia-noite. Máquinas de estado pequenas mantêm os seminários honestos em escala. Estados que não existem não podem esconder trabalho. Risco aceito exige uma nota de autoridade do mesmo jeito que os achados, e a validação da API rejeita outras strings na criação.

### 37.10 Cena do aviso no dia dez

Comentários abertos do seminário avisam Sam no dia 10. Ele recusa um com o motivo "fora do escopo do projeto final" e corrige dois no mesmo dia. A cena é operação comum num quadro de comentários. O dia dez é cedo o bastante para agir e tarde o bastante para sentir a pressão. A recusa fora de escopo de Sam é específica, para que o crítico não precise adivinhar. Corrigir dois no mesmo dia mostra que o aviso funciona. Limbo educado termina quando o relógio fala. Apresentadores aprendem a limpar o quadro antes que o aviso se torne um hábito.

### 37.11 Sem status "meio pronto"

A API da máquina de estados rejeita "kinda done". Sam agradece ao software pedante quando está cansado. "Meio pronto" é como o trabalho se esconde parecendo progressista. A rejeição na API significa que a interface nunca oferece a mentira. Sam já tentou digitá-lo à meia-noite e foi salvo pela grosseria. Cansaço é quando status dishonestos parecem razoáveis. Pedanteria protege o eu futuro que terá de explicar o quadro. APIs que se recusam a mentir ensinam melhor do que cartazes sobre honestidade.

### 37.12 Links profundos nas mensagens de aviso

As mensagens de aviso incluem links profundos para a thread do comentário. Um aviso sem link cria uma caça ao tesouro por canais antigos. Links profundos abrem o comentário exato, para que a ação possa começar em segundos. Sam proíbe "veja a thread" sem links. Fadiga mais ambiguidade produz comentários esquecidos. O caminho de menor resistência deve ser o comentário certo. Avisos que carregam o URL respeitam pessoas cansadas. Sam proíbe o atalho "veja a thread" no texto do aviso, e links quebrados são tratados como defeitos de ferramentas que precisam de ticket.

### 37.13 Links profundos do comentário exato

Os links profundos abrem o comentário exato; Sam proíbe "veja a thread" sem links. "Veja a thread" é ambíguo quando um canal mudou ou foi renomeado. Links exatos removem discussões sobre qual observação era a pretendida. O modelo de Sam cola a URL automaticamente a partir do rastreador. Facilidade de uso aqui é ética de evidência. Críticos merecem saber que sua observação foi a que recebeu a ação. Ambiguidade é como o trabalho bom se perde entre as mensagens. O modelo de Sam cola a URL automaticamente a partir do rastreador, e revisores que omitem o link veem a mensagem rejeitada antes do envio.

### 37.14 Semana de higiene dos comentários

A semana de higiene dos comentários a cada período fecha threads envelhecidas. Sam curte o quadro limpo. A semana de higiene é agendada como um lançamento, e não improvisada por culpa. As equipes encerram, recusam ou aceitam o risco do que resta. Sam trata um quadro limpo como um resultado de produto. Higiene que depende de vergonha falha no meio do período. Ritual torna a limpeza comum em vez de heroica. Períodos que pulam a higiene herdam fantasmas que assustam os examinadores.

### 37.15 Pressão da CSV de abertos

O rastreador de seminário de Sam exporta uma CSV semanal de comentários abertos por apresentador. Contagens públicas sem humilhação mantêm a pressão gentil. Visibilidade sem humilhação é um desenho delicado. As contagens são por itens abertos do apresentador, não ataques pessoais no chat. Notas de agradecimento fazem do zero um estado celebrado. Sam revisa o tom da CSV antes de publicar. Pressão que parece placar envenena a sala. Contagens que parecem higiene mantêm o seminário gentil e honesto. Lembretes raivosos já tinham sido tentados e aumentavam a vergonha sem limpar o quadro, então Sam revisa o tom da CSV antes de publicar.

### 37.16 Notas pessoais de agradecimento

As notas de agradecimento por zero abertos são modeladas, mas enviadas pessoalmente. Os modelos mantêm a barra coerente; o envio pessoal mantém o agradecimento humano. Sam escreve uma frase específica sobre uma thread fechada, para que não pareça automatizado. Agradecimentos genéricos ensinam as pessoas a ignorar o elogio. Específicos ensinam o que repetir. Cultura que agradece o encerramento produz mais encerramentos. Uma frase verdadeira vence um parágrafo de modelo que poderia ter ido para qualquer um. As pessoas encaminham essas notas para si mesmas como prova de que o encerramento importa, e agradecimentos genéricos ensinam a ignorar o elogio.

### Exemplo resolvido (TRB sintético)

Sam apresenta o pacote do F3, aceita uma crítica sobre o denominador ausente e registra uma ação para acrescentá-lo.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX109 — Checklist.** Cite itens do checklist do seminário. *Rubrica:* 3 = clareza de escopo, hashes de evidência, racional da severidade e privacidade (overclaim também); 2 = parcial; 1 = um; 0 = nada.
- **EX110 — Bom feedback.** O que torna o feedback útil? *Rubrica:* 3 = aponta linhas específicas e sugere uma correção concreta; 2 = parcial; 1 = "aperte isso"; 0 = nada.
- **EX111 — Overclaim.** Por que porcentagens sem denominadores são um problema? *Rubrica:* 3 = enganam quem decide; 2 = parcial; 1 = são boas; 0 = nada.

### Síntese

O seminário transforma crítica em ações com estado, prazo e links profundos.
### Continue estudando — capítulo 37 de 40

[← Capítulo 36 (rascunho)](#ch-36) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 38 (rascunho) →](#ch-38)

<a id="ch-38"></a>

## Capítulo 38 — Implementação do projeto final

### Objetivos de aprendizagem

Você vai (1) implementar o diff de inventário; (2) falhar fechado; (3) entregar testes, docs e passagem.

### 38.1 Construção

Fazer o diff de dois inventários sintéticos; sinalizar only-in-docs / only-on-network / conflito de tipo. A implementação faz o diff de dois inventários sintéticos e sinaliza hosts só nos documentos, só na rede, ou presentes nos dois com tipos conflitantes. Sam mantém a lógica do diff pequena o bastante para testar. Relatórios vistosos sem classes de conflito falham na avaliação. A ferramenta imprime ids de ativos, não apelidos. Construção aqui significa propriedades, e não um dashboard. Operadores deveriam terminar uma execução sabendo o que investigar a seguir.

### 38.2 Falhar fechado

YAML corrompido → negar com motivo. YAML corrompido precisa negar com uma string de motivo na qual um humano consiga agir. Devolver uma lista vazia de allow na falha de parse é tratado como um bug crítico. O teste de propriedade de Sam procura esse caminho vazio de propósito. Motivos citam o caminho do arquivo e a classe do erro de parse. Falhar fechado é a primeira demonstração em todo checkpoint. Uma negação educada é melhor engenharia do que um silêncio educado. Os testes de propriedade de Sam invertem bits até a negação disparar em cada mutação, e motivos citam o caminho do arquivo e a classe do erro de parse.

### 38.3 Testes

Fixtures douradas; sem rede. Os testes usam fixtures douradas e nunca tocam a rede. As fixtures incluem inventários felizes, quase-correspondências, arquivos truncados e encodings errados. Sam nomeia as fixtures corrompidas de forma que os testes de propriedade as encontrem. Testes que precisam de rede falham na CI de propósito. Fixtures douradas tornam as regressões óbvias. Avaliação sem rede mantém o projeto final alinhado com a disciplina do laboratório. Sam nomeia as fixtures corrompidas com o prefixo corrupt- para que a CI as descubra, e testes que precisam de rede falham na CI de propósito.

### 38.4 Docs

README do operador com exemplos. O README do operador mostra exemplos que se pode copiar e colar para os casos comuns de conflito. Sam escreve o README como se o leitor nunca tivesse visto seus aliases de shell. Exemplos incluem a negação em arquivo corrompido e o caminho de reconhecimento fuzzy. Documentação que só funciona na cabeça de Sam falha no dia do operador. Exemplos são testes para humanos. Um README que um estranho consegue executar é parte da nota. Os exemplos incluem o caminho de negação para que os operadores pratiquem a falha, e um README que um estranho consegue executar é parte da nota.

### 38.5 Congelamento

Congelamento de recursos antes da semana de avaliação. Congelar a construção também mantém as derivas plantadas e os casos de falhar fechado medindo o mesmo código que o orientador aprovou na nota de pré-registro. Sam estaciona ideias na versão dois. Congelamentos quebrados invalidam as métricas. A semana de avaliação não é para recursos heroicos de última hora. Congelar é como a honestidade da avaliação sobrevive ao entusiasmo. Ideias estacionadas ainda podem ser boas; só não são desta nota. Sam estaciona ideias numa lista da v2 em vez de mesclar cromado, e congelamentos quebrados invalidam as métricas da semana de avaliação.

### 38.6 Passagem

Acompanhar um operador executando sozinho. Passagem significa acompanhar um operador que executa a ferramenta sozinho numa conta nova. Sam pode responder perguntas, mas não pode digitar. Se o operador precisar do histórico do shell de Sam, o README falhou. A passagem é cronometrada e anotada. Sucesso sem as mãos é o critério. Uma ferramenta que só o autor consegue operar ainda não foi entregue. Se o operador precisar do histórico do shell cheio de aliases de Sam, a documentação falhou, e sucesso sem as mãos é o critério da passagem.

### 38.7 Fixtures douradas difíceis

As fixtures douradas incluem um escopo deliberadamente corrompido e um inventário de quase-correspondência que não deve ser mesclado por padrão. Mesclas prestativas são como hosts distintos viram um registro confuso. A fixture de quase-correspondência existe para punir a fuzzy padrão. Os testes de Sam falham se os conflitos desaparecerem sem um reconhecimento. Padrões que mesclam em silêncio são bugs de produto. Fixtures que parecem chatas pegam falhas caras. Quase-correspondências são onde inventários mentem com educação. Os testes de Sam falham se os conflitos desaparecerem sem --ack-fuzzy, e escopo corrompido precisa negar em vez de ser "consertado" em silêncio.

### 38.8 Flag de correspondência fuzzy

Nomes de inventário quase correspondentes exigem --ack-fuzzy para mesclar. O padrão é listá-los como conflitos. A flag força uma escolha intencional antes de os inventários colapsarem. A listagem padrão de conflitos impede que gêmeos de homologação e de produção se mesclem em silêncio. Sam registra os reconhecimentos fuzzy no log de auditoria. Conveniência que esconde risco não é conveniência. O padrão protege operadores cansados de si mesmos. Mesclar continua possível; só deixa de ser o caminho de menor resistência. Sam registra o uso da flag com o nome de usuário para perguntas posteriores de auditoria, e mesclar continua possível sem ser o caminho de menor resistência.

### 38.9 Nomes das fixtures corrompidas

Fixtures nomeadas corrupt-*.yaml precisam negar. Um teste de propriedade na CI gera corrupção aleatória além das fixtures nomeadas. Convenções de nomenclatura permitem que os testes de propriedade descubram fixtures sem um manifesto frágil. A corrupção aleatória cresce a cada período conforme os parsers endurecem. Sam exige que cada mutação nova tenha nome e intenção. Fixtures sem o padrão de nome são invisíveis para a propriedade. Descoberta por convenção escala melhor do que listas feitas à mão. Parsers endurecem quando a corrupção se recusa a ficar previsível.

### 38.10 Teste de propriedade com bit-flip

O teste de propriedade de corrupção aleatória inverte bits no YAML até a negação disparar. Sam assiste para o caminho vazio de allow nunca voltar. O caminho vazio de allow teria parecido um escopo vazio limpo na produção. Grosseria nos testes é bem-vinda quando a alternativa é cegueira educada. Sam acrescentou o teste depois de um quase incidente em homologação. Bit-flips encontram classes de bugs que fixtures felizes perdem. Propriedades que caçam o silêncio protegem falhar fechado. Uma suite educada demais deixa passar o pior bug.

### 38.11 Fixtures de truncamento e encoding

As fixtures corrompidas incluem arquivos truncados e encodings errados. A negação precisa disparar nos dois. Truncamento no meio do documento e encodings surpresa são comuns em exportações reais. A negação não pode depender de um único estilo de corrupção. A mutação nova de cada período é registrada com nome. Sam se recusa a tratar UTF-16 inesperado como um caminho feliz. Robustez significa negar estranheza sem travar. Exportações do mundo real não respeitam os exemplos do tutorial. A mutação nova de cada período é registrada com uma intenção de uma linha para legibilidade na CI, e Sam se recusa a tratar UTF-16 inesperado como caminho feliz.

### 38.12 Mutações nomeadas

Cada mutação nova no teste de propriedade ganha um nome e uma intenção de uma linha. Nomes como trunc-mid-yaml tornam as falhas legíveis nos logs da CI. Linhas de intenção impedem que estudantes futuros apaguem uma mutação que não entendem. Sam revisa os nomes nos checkpoints. Mutações anônimas viram dívida. Clareza nos testes é parte da clareza do produto. Uma falha que nomeia a mutação ensina o conserto. Sam revisa os nomes quanto à clareza do mesmo jeito que revisa achados, e uma falha que nomeia a mutação ensina o conserto na semana de avaliação.

### 38.13 Nomes legíveis de mutação

Os nomes das mutações parecem "trunc-mid-yaml", para que as falhas se leiam com clareza na CI. Hashes opacos como ids de mutação desperdiçam minutos na semana de avaliação. O guia de estilo de testes de Sam proíbe nomes engraçados que escondem a intenção. Nomes claros também ajudam os orientadores a auditar a cobertura. Legibilidade é uma propriedade de controle para humanos. Testes que explicam a si mesmos sobrevivem às trocas de turma. Avaliação anda mais rápido quando os logs já contam a história.

### 38.14 Dia do operador com conta nova

O dia do operador usa uma conta nova, sem aliases de Sam no histórico do shell. Se o operador precisar dos aliases, o README falhou. Shells tribais compartilhados mentem sobre a prontidão. Contas novas retiram o conforto de docs incompletos. Sam observa sem digitar e toma notas para consertos no README. Aliases são dívida disfarçada de velocidade. Passagem que depende da memória muscular do autor não é passagem. O dia do operador é onde a documentação encontra a verdade. Aliases que voltam pelos dotfiles são tratados como falhas da passagem, e contas novas retiram o conforto de documentação incompleta de propósito.

### 38.15 Reconhecimento digitado da mescla

Reconhecimentos de correspondência fuzzy exigem digitar a frase "I accept merge risk" exatamente. Diálogos de um clique treinam a cegueira; frases digitadas criam uma pausa. Copiar e colar da wiki ainda força os olhos a passar pelas palavras. Os logs de auditoria guardam quem digitou a frase. Sam quer atrito antes de inventários colapsarem. Uma frase que as pessoas precisam digitar é um controle, não um ornamento. Atrito no momento certo evita recalls caros depois. Os logs de auditoria guardam quem digitou a frase e quando, e remover a frase por conveniência é tratado como um defeito de produto.

### 38.16 Log de auditoria do reconhecimento

A frase de reconhecimento digitada é registrada no log de auditoria com o nome de usuário. Os logs apoiam perguntas posteriores quando uma mescla ruim é descoberta. Os nomes de usuário vêm do contexto autenticado do operador, e não de uma caixa de texto livre. Os runbooks de Sam ensinam a consultar o log antes de culpar a ferramenta. Auditoria sem identidade é teatro. Registros que nomeiam a pessoa tornam o risco aceito real. Mesclas ruins merecem uma trilha, não uma lenda.

### Exemplo resolvido (TRB sintético)

A ferramenta de Sam sinaliza only-in-docs, only-on-network e type-conflict, e nega YAML corrompido com motivo.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX112 — Flags.** Quais classes o diff sinaliza? *Rubrica:* 3 = only-in-docs, only-on-network e type-conflict (e match); 2 = parcial; 1 = uma; 0 = nada.
- **EX113 — Falhar fechado.** O que acontece com YAML corrompido? *Rubrica:* 3 = falhar fechado com motivo claro e código de saída diferente de zero; 2 = parcial; 1 = lista vazia de allow; 0 = nada.
- **EX114 — Rede.** A ferramenta pode exigir rede? *Rubrica:* 3 = não; precisa rodar offline em arquivos locais; 2 = não, sem justificativa; 1 = sim; 0 = nada.

### Síntese

A implementação entrega propriedades de controle, fixtures douradas e uma passagem sem as mãos do autor.
### Continue estudando — capítulo 38 de 40

[← Capítulo 37 (rascunho)](#ch-37) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 39 (rascunho) →](#ch-39)

<a id="ch-39"></a>

## Capítulo 39 — Avaliação do projeto final

### Objetivos de aprendizagem

Você vai (1) avaliar contra métricas pré-registradas; (2) executar testes independentes; (3) declarar o risco residual.

### 39.1 Plano

Precision/recall em derivas plantadas; casos de falhar fechado. O plano de avaliação trava precision e recall nas derivas plantadas mais os casos de falhar fechado antes de qualquer execução começar. Sam congela as definições das métricas numa nota curta de pré-registro que o orientador assina. Inclusões, remoções e conflitos de tipo plantados fornecem a verdade de referência que o script consegue pontuar. Casos de falhar fechado são pontuados como passa ou falha, nunca como crédito parcial brando. Planos que inventam métricas depois de ver as pontuações reprovam no padrão do curso. Sam planta vinte derivas no par de inventários (oito inclusões, sete remoções e cinco conflitos de tipo), para que cada classe tenha casos suficientes para um intervalo significar alguma coisa.

### 39.2 Independência

Outro estudante executa o script de avaliação. Outro estudante executa o script de avaliação enquanto Sam fica longe do teclado. Independência é um protocolo social tanto quanto técnico. O executor assina uma declaração de uma linha de que Sam não editou os logs da execução. As declarações ficam no apêndice ao lado das saídas brutas. Execuções treinadas são tratadas como má conduta acadêmica, e não como colaboração prestativa. O executor recebe apenas o README, o script congelado e o pacote de fixtures; se travar, registra a pergunta por escrito, e a própria pergunta vira dado de avaliação sobre a documentação.

### 39.3 Efeitos colaterais

Tempo de usabilidade; carga de falsos alarmes. As medidas de efeitos colaterais incluem o tempo de usabilidade e a carga de falsos alarmes para os operadores. Uma ferramenta precisa que inundar os operadores de ruído não será adotada. Sam cronometra a triagem de conflitos na primeira vez num par fixo de inventários. Falsos alarmes são contados e discutidos mesmo quando a precision parece lisonjeira. Os efeitos colaterais pertencem ao relatório ao lado das pontuações de destaque. A primeira medição de Sam mostrou operadores gastando a maior parte do tempo em conflitos de tipo que eram variantes inofensivas de nomenclatura. Ele relatou esse custo com honestidade em vez de ajustá-lo para longe antes de a avaliação fechar, e a constatação entrou na lista da v2.

### 39.4 Risco residual

As declarações de risco residual dizem com clareza que a ferramenta ajuda a higiene do inventário e não substitui a disciplina das ROE. Sam recusa linguagem de marketing que implica que o teste autorizado pode ser automatizado. Leitores que pulam este parágrafo são os mais propensos a usar mal a ferramenta. A declaração é obrigatória tanto no resumo do relatório quanto no slide final. Auxílios de higiene continuam subordinados aos limites humanos de autorização. Um exemplo concreto ajuda: a ferramenta pode dizer que um host falta no escopo documentado, mas não pode dizer se testar esse host está autorizado. Esse julgamento permanece com o responsável pelas ROE.

### 39.5 Relatório

O relatório compara os resultados ao pré-registro e proíbe trocas de métrica a posteriori. Análises exploratórias só são permitidas num apêndice claramente rotulado. O modelo de Sam destaca qualquer métrica que não foi pré-registrada. Trocas de volta olímpica são reprovação mesmo que a métrica nova pareça mais gentil. A honestidade sobre falhas faz parte da ciência avaliada. Onde uma classe de deriva plantada pontuou mal, o relatório mostra as falhas pelo nome da fixture, para que os leitores possam inspecioná-las. O resultado mais baixo de Sam, nos conflitos de tipo, aparece no resumo, e não na última página.

### 39.6 Recomendação

Adotar primeiro em homologação. A recomendação é adoção em homologação primeiro, com responsáveis nomeados e um checklist de trinta dias. Ferramentas sem planos de adoção são hobbies, por mais engenhosas que sejam. Sam escreve como é o sucesso em homologação antes de alguém falar de produção. A promoção para produção espera evidência de execuções solo de operadores. Recomendações que pulam a homologação são rejeitadas pelo orientador. No plano de Sam, sucesso em homologação significa duas execuções solo de operadores sem ajuda do autor, sem regressões de falhar fechado e falsos alarmes abaixo do nível que os operadores disseram tolerar no estudo de tempo. Só então começa uma discussão de produção, com o responsável pelo serviço a presidindo.

### 39.7 Declaração de independência

Avaliadores independentes assinam uma declaração de uma linha de que Sam não editou os logs da execução. A declaração fica no apêndice. Avaliação confiável é um protocolo social tanto quanto um script. Scripts sozinhos não conseguem provar independência quando os autores ficam por perto. A linha assinada torna a regra social visível para os examinadores. Sam mantém distância durante as execuções mesmo quando a curiosidade coça. Declarações ausentes bloqueiam o encerramento do capítulo de avaliação. Ciência confiável é, em parte, papelada feita sem ressentimento. A redação é fixa, para que os executores não possam amaciá-la para "quase sem edição".

### 39.8 Plano de adoção em homologação

Os relatórios de avaliação incluem um plano de homologação de trinta dias com responsáveis. Ferramentas sem planos de adoção são hobbies. O plano de trinta dias nomeia datas, responsáveis e a evidência esperada em cada portão. Sam rejeita planos que só dizem monitorar em homologação. Checklists viram tickets, para que o trabalho não se esconda em marcadores de e-mail. Energia de hobby é bem-vinda nos laboratórios e indesejada nas alegações de adoção. Planos com equipe são como as ferramentas saem da tese e entram nas operações. O plano de Sam tem três portões: uma primeira execução solo até o dia dez, uma segunda até o dia vinte e uma revisão dos relatórios de quebra e das contagens de falsos alarmes no dia trinta. Cada portão nomeia o arquivo de evidência que prova que ele passou.

### 39.9 Responsáveis pela adoção

A adoção em homologação nomeia um responsável pelo serviço e um pela plataforma. Um nome só é insuficiente. Responsáveis pelo serviço sentem a dor operacional; responsáveis pela plataforma sentem a dor da ferramenta. Um nome só costuma significar que o estudante ainda é dono de tudo oficiosamente. Sam exige os dois papéis antes de o plano de homologação poder ser aprovado. A propriedade dividida evita o abandono silencioso quando o período termina. Nomenclatura insuficiente é tratada como uma recomendação incompleta. Na prática, o responsável pelo serviço decide se uma lista de conflitos é boa o bastante para agir, enquanto o da plataforma corrige problemas de parser e de empacotamento. Quando esses dois trabalhos compartilham um nome, reclamações operacionais tendem a ficar sem resposta porque a mesma pessoa também está ocupada corrigindo código.

### 39.10 Mira e Sam na adoção

O plano de adoção nomeia Mira para a propriedade do serviço e Sam para o suporte da plataforma. O checklist de trinta dias inclui duas execuções solo de operadores. Sem o nome de Mira, o plano seria ficção. O nome de Mira torna o plano real porque ela pode recusar trabalho que não está pronto. Duas execuções solo pegam lacunas de documentação que os testes unitários perdem. O papel de plataforma de Sam permanece de apoio, e não possessivo. Planos de ficção só com nomes de estudantes são um modo de falha conhecido. A cena é usada no treinamento de orientadores como um exemplo positivo.

### 39.11 Execução solo encontra lacuna de DNS

A segunda execução solo falhou porque o DNS diferia no perfil do operador. O README ganhou um preâmbulo de DNS. Execuções solo encontram bugs de documentação que as ferramentas perdem. Diferenças de perfil são entediantes até quebrarem um operador cuidadoso. Sam agradeceu a falha na retrospectiva em vez de culpar o operador. O texto do preâmbulo de DNS agora faz parte dos exemplos dourados do README. Execuções solo são testes de documentação vestidos de roupa operacional. Ferramentas podem passar nos testes unitários e ainda assim falhar com humanos no primeiro dia. O resolvedor do operador devolvia nomes curtos onde a fixture esperava nomes totalmente qualificados.

### 39.12 Itens do checklist como tickets

Os itens do checklist de trinta dias são tickets, não marcadores num e-mail. Tickets carregam responsáveis, datas de vencimento e anexos de evidência. Marcadores de e-mail evaporam quando as caixas de entrada rotacionam. O modelo de adoção de Sam abre tickets automaticamente a partir do checklist. Tickets encerrados sem evidência são reabertos por política. Tickets são como trinta dias se tornam responsabilizáveis em vez de aspiracionais. O checklist de Sam produz seis tickets: duas execuções solo, a revisão de falsos alarmes, uma revisão das mensagens de negação, a atualização do README e a retrospectiva do dia trinta. Cada um tem um responsável do plano de adoção e uma data de vencimento dentro dos trinta dias, para que o atraso fique visível no quadro antes de a janela fechar.

### 39.13 Evidência para autoencerramento

Tickets dos itens do checklist só se autoencerram quando a evidência da execução solo está anexada. Autoencerrar sem evidência recria o teatro de conclusão no papel. Sam configura a regra para que a conveniência não apague a exigência de prova. Os operadores aprendem a anexar as saídas enquanto a execução está fresca. Anexos ausentes mantêm o ticket barulhento de propósito. Encerramento com portão de evidência é higiene de adoção. A evidência aceitável é específica: o arquivo de saída de conflitos, a linha de comando do operador e o hash da versão da ferramenta. Uma captura de tela sozinha não conta, porque não consegue mostrar qual build rodou. Quando a evidência falta, o ticket continua aberto e avisa o responsável todas as manhãs.

### 39.14 Reescrever partes ignoradas do README

As retrospectivas de adoção no dia 30 perguntam aos operadores o que ignoraram no README. Seções ignoradas são apagadas ou reescritas, não defendidas. Defender parágrafos não lidos desperdiça a única atenção que os operadores ofereceram. Sam prefere encolher a documentação a dar palestra por quem passa os olhos. Ignorado significa que a escrita falhou no ambiente em que entrou. Retrospectivas que reescrevem são mais gentis do que retrospectivas que culpam. Atenção é o recurso escasso que a adoção precisa orçar. Na primeira retrospectiva, os operadores admitiram pular por completo a longa visão geral de arquitetura. Sam a cortou para três frases e moveu o exemplo do caminho de negação para o topo, já que era a parte de que as pessoas realmente precisavam na primeira execução.

### 39.15 Relatórios intencionais de quebra

A verificação de adoção do dia dez pede aos operadores que quebrem a ferramenta de propósito e registrem a quebra. Sam prefere ouvir a dor cedo a um silêncio educado. Dois relatórios intencionais de quebra na primeira turma melhoraram as mensagens de negação mais do que um mês de polimento especulativo teria. O silêncio educado é um antipadrão de adoção. Convidar quebras legitima más notícias cedo. Melhorias nas mensagens de negação a partir de confusão real vencem o polimento imaginado de UX. Sam trata os relatórios de quebra como entrada valorizada, e não como reclamações. Dor cedo é mais barata do que abandono quieto.

### 39.16 Tipo de ticket BREAK-ADOPT

Os relatórios intencionais de quebra têm o próprio tipo de ticket: BREAK-ADOPT. Um tipo distinto mantém a dor da adoção pesquisável depois. Sam revisa os tickets BREAK-ADOPT semanalmente durante a janela de homologação. Misturar quebras com bugs comuns as esconde sob o ruído do backlog. Tipagem torna o convito para quebrar operacionalmente real. Dor pesquisável vira melhoria; dor misturada vira lenda. Cada relatório registra o que o operador tentou, o que a ferramenta fez e o que ele esperava; a primeira turma achou mensagem vaga em inventário vazio, o que virou um conserto específico.

### Exemplo resolvido (TRB sintético)

A avaliação independente mostra precision e recall nas derivas plantadas; Sam recomenda adoção primeiro em homologação, com Mira como responsável pelo serviço.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX115 — Independência.** Quem executa o script de avaliação? *Rubrica:* 3 = outro estudante ou testador independente; 2 = parcial; 1 = só Sam; 0 = nada.
- **EX116 — Risco residual.** O que a ferramenta não substitui? *Rubrica:* 3 = a disciplina das ROE ou as verificações de autorização; 2 = parcial; 1 = tudo; 0 = nada.
- **EX117 — Pré-registro.** As métricas podem mudar depois das pontuações? *Rubrica:* 3 = não; as métricas ficam como pré-registradas; 2 = não, sem justificativa; 1 = sim; 0 = nada.

### Síntese

A avaliação trava métricas, exige independência e declara o risco residual sem substituir a disciplina das ROE.
### Continue estudando — capítulo 39 de 40

[← Capítulo 38 (rascunho)](#ch-38) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 40 (rascunho) →](#ch-40)

<a id="ch-40"></a>

## Capítulo 40 — Tese e apresentação

### Objetivos de aprendizagem

Você vai (1) afirmar só o que a avaliação mostrou; (2) ensaiar perguntas difíceis; (3) posicionar o trabalho com ética.

### 40.1 Afirmação

A ferramenta offline de diff de escopo atinge precision/recall definidos em inventários sintéticos e falha fechada em entradas corrompidas. A afirmação da tese nomeia a ferramenta, as métricas, os dados e a propriedade de falhar fechado sem enfeites. Sam recusa adjetivos que a avaliação não mediu. Afirmações que prometem proteção à produção excedem a evidência. O orientador aplica o teste do resumo: um leitor deve saber exatamente o que foi mostrado. Modéstia aqui é precisão científica. Uma afirmação estreita e verdadeira vence uma ampla que a banca precisa desmontar.

### 40.2 Posicionamento

Não é um framework de red-team exploit. O posicionamento declara o que o trabalho não é, tão alto quanto o que ele é. Leituras do trabalho como framework de exploit são tratadas como falhas de comunicação a corrigir, e não como hype lisonjeiro. Os slides repetem a frase de posicionamento perto da afirmação. Posicionamento claro protege os limites legais e éticos do programa. A frase de posicionamento também governa o vocabulário: a tese diz deriva de inventário, conflito e negar, e evita palavras de ataque que convidariam à leitura errada.

### 40.3 Apresentação

12 minutos + perguntas; disciplina de tempo. A apresentação tem doze minutos mais perguntas, com disciplina rígida de tempo. Sam ensaia com um timer visível e para no meio da frase no ensaio, se precisar. Estourar o tempo rouba a faixa de perguntas, onde acontece o exame de verdade. As bancas notam quem respeita o relógio. Brevidade sob observação faz parte da habilidade profissional avaliada. Os doze minutos de Sam se dividem em dois na afirmação e no posicionamento, quatro no método, três nos resultados com intervalos, dois nos limites e na ética, e um na decisão que ele pede à banca que aceite. O tempo de demonstração ao vivo sai do bloco do método, e não das perguntas.

### 40.4 Perguntas prováveis

Demonstrações de falhar fechado; ética; por que não varredura ao vivo; ameaças à validade. Ele mantém cada resposta ensaiada com menos de três frases e a liga a uma página da tese, para que os membros da banca possam conferir em vez de confiar. Sam publica seu banco de perguntas depois da defesa, para que a próxima turma ensaie melhor. A recusa da demonstração em site público está no banco de propósito. Respostas de ensaio são curtas, citadas e calmas. Perguntas surpresa ainda acontecem; bancos reduzem o pânico evitável. Para "por que não varredura ao vivo", a resposta de Sam é que a afirmação diz respeito à comparação de inventários, dados sintéticos bastaram para testá-la, e uma varredura ao vivo teria precisado de autorização que o curso não pode conceder.

### 40.5 Próximos passos

Integrar tickets do FindingsDesk; estudar métricas de detecção guiadas por ameaças. Os próximos passos mencionam a integração de tickets do FindingsDesk e estudos de métricas de detecção guiadas por ameaças. Permanecem claramente rotulados como trabalho futuro, e não como alegações avaliadas incompletas. Sam resiste a enfiar nos próximos passos recursos banidos pelos não objetivos. Ambição só pertence aqui quando não reescreve a afirmação da tese. Os examinadores não deveriam precisar adivinhar o que foi entregue versus sonhado. A integração de tickets é listada com o próprio risco, que é que conflitos poderiam inundar o FindingsDesk com itens de baixo valor, então um estudo futuro precisaria primeiro de um limiar de triagem. Métricas guiadas por ameaças são enquadradas como uma pergunta de pesquisa separada, não como um recurso da ferramenta.

### 40.6 Reprodutibilidade

Apêndice com dados sintéticos e scripts. O apêndice de reprodutibilidade inclui dados sintéticos e scripts suficientes para regenerar as pontuações. Sam fixa os hashes dos scripts e as versões dos geradores ao lado das tabelas de resultados. Alegações sem apêndices executáveis são avaliadas como ciência incompleta. Dados sintéticos mantêm a reprodução dentro da política do curso. Estudantes futuros deveriam conseguir reexecutar sem pedir arquivos privados a Sam. Uma execução de reprodução numa máquina nova do laboratório faz parte da verificação de submissão: um assistente do orientador segue as instruções do apêndice e confirma que as figuras de precision e recall batem com o relatório até a casa decimal declarada. Qualquer divergência bloqueia a submissão até o apêndice ser corrigido.

### 40.7 Recusa de demonstração hostil

O ensaio com examinador hostil inclui um pedido de demonstração ao vivo contra o site público de um banco. A recusa de Sam cita a lei e os limites do currículo. Os colegas avaliam a clareza da recusa sob estresse. O ensaio é desconfortável de propósito. Clareza sob estresse é a habilidade, não agressão. Sam cita a lei e o currículo em vez de preferência pessoal. Os colegas pontuam a redação para que o feedback seja específico. Recusas que divagam ensinam às bancas a lição errada sobre limites. A frase ensaiada de Sam é curta: "Não estou autorizado a testar esse site, e o currículo proíbe; aqui está o mesmo comportamento na fixture sintética." Depois ele segue em frente.

### 40.8 Banco de perguntas depois da defesa

Sam publica sua lista de perguntas prováveis depois da defesa, para que a turma do ano seguinte ensaie melhor. O banco inclui a recusa da demonstração em site público. Publicar depois da defesa evita vazar respostas para o evento avaliado. Incluir a recusa normaliza o limite para os novatos. Sam atualiza o banco quando novos padrões hostis aparecem. Turmas que ensaiam a partir de bancos reais ficam mais calmas sob o calor da banca. Generosidade com perguntas faz parte da administração do programa. Cada entrada emparelha a pergunta com a resposta que Sam deu e uma nota sobre o que ele diria melhor agora. A nota costuma ser a parte mais útil para os estudantes do ano seguinte.

### 40.9 Autorrevisão em áudio da recusa

As recusas de ensaio são gravadas em áudio para autorrevisão e depois apagadas em até 24 horas. Sam confere a voz em busca de hesitação. A retenção curta equilibra a melhoria com o armazenamento desnecessário de áudio de estresse. Sam ouve em busca de hesitação, empilhamento de desculpas e citações perdidas. A exclusão é registrada, para que a prática não vire vigilância. A autorrevisão pega hábitos que os colegas são educados demais para nomear. A voz sob pressão é um instrumento treinável. A primeira gravação de Sam tinha três desculpas antes da recusa de fato. No terceiro ensaio, não tinha nenhuma, e os colegas avaliaram a versão posterior como mais calma e mais firme. Ele guarda uma nota escrita dessa mudança depois que o áudio é apagado.

### 40.10 Fechando o laptop hostil

No ensaio, o examinador hostil abre um laptop numa página de login pública de banco. Sam fecha a tampa com gentileza, cita o limite e continua com a demonstração de falhar fechado. Os colegas pontuam a gentileza e a firmeza separadamente. Gentileza sem firmeza é rendição; firmeza sem gentileza é teatro. Fechar a tampa com gentileza mantém a sala aprendendo o limite, e não o susto. Sam continua na demonstração de falhar fechado, para que a fala não trave na recusa. Pontuações separadas impedem que o carisma esconda nãos trêmulos. A cena é o momento de ensaio mais recontado do curso.

### 40.11 Calma e firmeza ambas obrigatórias

A pontuação de gentileza importa: bater o laptop assustaria a sala na lição errada. Firme e calmo é a habilidade sob exame. Bater ensina medo; o medo ensina a imitação errada. Firme e calmo é mais difícil e mais profissional. Sam pratica o movimento da tampa até ele ficar entediante. Colegas que recompensam a energia de bater são corrigidos no debrief. A habilidade sob exame é estabelecer limites, não exibir domínio. Firme significa que o limite não se move quando o examinador empurra uma segunda vez. Calmo significa que voz, ritmo e mãos permanecem firmes enquanto ele se mantém. Examinadores de ensaio empurram de propósito duas vezes, porque o segundo empurrão é onde a maioria dos estudantes ou cede ou fica cortante.

### 40.12 Pontuações da rubrica calma/firme

Os colegas pontuam calma e firmeza numa rubrica de 0–3; Sam mira 3/3 nas duas. Rubricas numéricas tornam comparável o feedback barulhento do ensaio. Metas de três e três mantêm o padrão visível. Sam aceita dois como sinais de orientação, e não como ataques pessoais. As âncoras da rubrica incluem descrições breves de cada pontuação. Pontuações comparáveis ajudam os facilitadores a acompanhar a melhoria ao longo das noites. Na escala de firmeza, zero significa que o estudante concordou com a demonstração, um significa que hesitou, dois significa que recusou mas convidou mais negociação, e três significa um não claro com o limite citado. A escala de calma usa voz, ritmo, desculpas e postura como âncoras.

### 40.13 Clipes âncora da rubrica

As âncoras da rubrica calma/firme incluem clipes de vídeo de exemplo de boas recusas (somente internos). Clipes internos mantêm os exemplos concretos sem publicar performances de estresse. Sam revisa os clipes quanto a consentimento e ocultação antes de entrarem no pacote. Adjetivos abstratos derivam; clipes seguram o padrão. O acesso aos clipes segue os mesmos modos da pasta de ética dos artefatos de pressão. Âncoras são ferramentas de ensino, não entretenimento. Cada clipe tem menos de um minuto e vem emparelhado com sua pontuação e um motivo de uma linha, para que um facilitador novo possa se calibrar em poucos minutos antes da noite de ensaio. Clipes de recusas fracas são reencenados pela equipe em vez de tirados de estudantes reais, para poupar alguém do constrangimento.

### 40.14 Lista do que eu ainda recuso

Depois da defesa, Sam publica uma lista de uma página "o que eu ainda recusaria" ao lado do PDF da tese. A lista inclui demonstrações ao vivo em bancos públicos, kits de exploit e dumps não verificados de scanners como evidência. Estudantes futuros veem que o limite sobrevive à formatura. Os orientadores citam a lista quando novos estudantes pedem atalhos. Fantasias de formatura não aposentam limites. Listar recusas ao lado do PDF as torna difíceis de perder. Os orientadores ganham um artefato durável para conversas sobre atalhos. Dumps não verificados de scanners como evidência permanecem na lista de recusa por motivos de integridade. Limites que sobrevivem são a sequência quieta de uma defesa bem-sucedida.

### 40.15 Lista de recusa no caminho de estudo

A lista do que eu ainda recuso é linkada a partir do STUDY_PATH perto do curso 111. A descobribilidade importa quando novos estudantes caçam atalhos em chats privados. Sam confere o link a cada período, para que a podridão não esconda a lista. A colocação no caminho de estudo trata as recusas como currículo, e não como folclore. Leitores do curso 111 encontram o limite antes de a pressão do projeto final bater o pico. Recusas linkadas duram mais do que avisos de corredor. Colocar o link perto do curso 111 é deliberado: esse curso apresenta a proposta do projeto final, que é quando os estudantes sentem pela primeira vez a tentação de prometer uma demonstração ao vivo. Ver a lista de recusa de um formado nesse momento faz o limite parecer uma norma profissional, e não uma regra da equipe.

### Exemplo resolvido (TRB sintético)

O resumo de Sam declara exatamente o que foi mostrado: acurácia offline do diff de escopo em inventários sintéticos e comportamento de falhar fechado — nada mais.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX118 — Posicionamento.** O que a tese não é? *Rubrica:* 3 = não é um framework de exploit; 2 = parcial; 1 = um kit de malware; 0 = nada.
- **EX119 — Teste do resumo.** Qual é o teste do resumo do orientador? *Rubrica:* 3 = o leitor sabe exatamente o que foi mostrado; 2 = parcial; 1 = palavras da moda; 0 = nada.
- **EX120 — Próxima área.** Cite um tema de próximo passo que Sam lista. *Rubrica:* 3 = integração com o FindingsDesk ou métricas de detecção guiadas por ameaças; 2 = vago; 1 = kits de exploit; 0 = nada.

### Síntese

A tese alega apenas o que a avaliação mostrou e ensaia as perguntas difíceis.
### Continue estudando — capítulo 40 de 40

[← Capítulo 39 (rascunho)](#ch-39) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções ↓](#worked-results) · [Próximo curso pelo índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX120. O Riverstone Transit Bank, Sam Ito e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O conjunto dentro do escopo é o conjunto de endereços da VLAN menos o conjunto unitário que contém o gateway SWIFT.

**EX002.** O escopo cobre hosts; métodos precisam de permissão separada. Password spraying costuma ser proibido mesmo em hosts dentro do escopo.

**EX003.** A cobertura é 28/40 (70% dos hosts tocados). Mau uso: tratar 70% como "70% seguro".

**EX004.** Os hosts do razão contábil e os gateways vizinhos do SWIFT.

**EX005.** Falhar fechado: negar testes até que um arquivo de escopo válido seja carregado.

**EX006.** Ele confere o registro de ativos e o dono, não apenas o padrão do nome do host.

**EX007.** Ele precisa continuar sendo uma verificação offline, para não varrer acidentalmente redes reais.

**EX008.** Segredos fixos no código e desativação da verificação TLS (também chamadas de shell não sanitizadas ou novas tentativas sem limite).

**EX009.** Erros que ampliam o escopo ou vazam segredos.

**EX010.** "Vários sistemas aceitam a mesma senha privilegiada, então o comprometimento de um concede acesso amplo; a responsabilização individual fica indisponível."

**EX011.** Rotulá-la como especulativa ou omiti-la até que exista evidência; mantê-la fora da lista de fatos.

**EX012.** Ele nunca pode inventar DOIs nem referências fabricadas.

**EX013.** Confidencialidade; integridade; disponibilidade.

**EX014.** Não há autorização escrita; tentativas de acesso podem ser ilegais e danosas.

**EX015.** Código de exploit e procedimentos de ataque passo a passo para produtos reais.

**EX016.** O par (origem, destino) observado não pertence à relação de fluxos aprovados.

**EX017.** Ele mostra uma alcançabilidade que atravessa fronteiras de confiança além da arquitetura pretendida.

**EX018.** Ele ordena por pontuação decrescente e depois pelo id do achado.

**EX019.** Ele não corrige uma autorização ou uma lógica de negócio quebradas na aplicação.

**EX020.** São endereços de documentação reservados, seguros para exemplos.

**EX021.** Apenas quando as ROE permitem, com minimização dos dados de clientes.

**EX022.** Dono e hash de evidência (severidade também é razoável).

**EX023.** Para pegar erros de esquema e de escopo antes que qualquer ticket seja escrito.

**EX024.** Dois analistas sobrescrevendo silenciosamente as atualizações de ticket um do outro.

**EX025.** Privacidade e minimização prevista nas ROE — os achados precisam de prova, não de dados pessoais em massa.

**EX026.** O cronograma de retenção do contrato do engajamento.

**EX027.** Evidências de outros engajamentos e bancos de dados de clientes de produção.

**EX028.** `198.51.100.20 EXCLUDED`

**EX029.** Recusar; o SWIFT continua excluído, salvo uma mudança escrita nas ROE — que testes comuns não vão conceder.

**EX030.** Escopo, exclusões, métodos, janela, contatos de emergência (também tratamento de dados e público).

**EX031.** Ele contorna o caminho controlado e registrado do jump host.

**EX032.** Elas reimplantam agentes desatualizados ou configurações fracas em hosts novos.

**EX033.** Não; o acesso ao hipervisor precisa de escopo explícito.

**EX034.** `95% CI=(0.40, 0.89)`

**EX035.** Um n menor significa mais incerteza e, portanto, um intervalo de confiança mais largo.

**EX036.** "Detectamos sete de dez eventos de teste; a taxa verdadeira poderia razoavelmente estar em qualquer ponto entre cerca de 40% e 90%, então devemos fazer mais tentativas."

**EX037.** T1078 Valid Accounts.

**EX038.** Revisar a configuração e a política sob as ROE.

**EX039.** Nominal, com o menor privilégio para o método, com prazo definido e guardada no cofre.

**EX040.** Isso excede a finalidade e a minimização prevista nas ROE; a prova precisa de amostras, não de dados em massa.

**EX041.** Números de conta (deixando os quatro últimos dígitos, se necessário) e outros identificadores pessoais.

**EX042.** Eles concentram dados sensíveis de prova, atraentes para atacantes e para pessoas de dentro.

**EX043.** Ela recompensa o ruído e pune a validação cuidadosa.

**EX044.** O arquivo não mudou desde que o digest foi registrado.

**EX045.** Quem coletou, descrição, carimbo de tempo e local de armazenamento (também o hash).

**EX046.** `web -> ledger-db UNAPPROVED`

**EX047.** Negar os testes até que a política seja carregada.

**EX048.** Não; o processador precisa autorizar os seus próprios sistemas.

**EX049.** Não. O TLS não corrige bugs de autorização.

**EX050.** A chave vaza junto com o repositório e contorna a custódia adequada de chaves.

**EX051.** Verificações de integridade nos arquivos de evidência.

**EX052.** Ela não é específica nem mensurável.

**EX053.** A métrica, o limiar e o desenho do ensaio.

**EX054.** Aprovação do CISO e do RH sob ROE escritas.

**EX055.** Como uma etapa tardia/final, depois das etapas técnicas.

**EX056.** TIBER-EU e CBEST.

**EX057.** Ele é limitado no tempo, limitado na cobertura e invalidado por mudanças posteriores.

**EX058.** O relato é um fato; a posse por um Estado-nação é um palpite sem evidência.

**EX059.** Isso está fora do escopo e é uma violação de privacidade; o TRB pode redefinir as próprias credenciais sem lê-lo.

**EX060.** Uma senha de VPN do banco exposta fora do TRB cria risco de acesso não autorizado aos sistemas bancários.

**EX061.** Comparar as configurações e rodar os testes acordados com os donos — não presumir.

**EX062.** Ele está fora do escopo do engajamento; por isso, modelá-lo convida a testes acidentais.

**EX063.** Web, API móvel e VPN dos funcionários (também os pares de lote).

**EX064.** `web -> ledger-db UNAPPROVED` (ênfase do capítulo 22).

**EX065.** Corrigir um fluxo não aprovado pode exigir mudanças tanto no firewall/roteamento quanto na aplicação.

**EX066.** Parar as verificações relacionadas e evitar tempestades de novas tentativas.

**EX067.** Finalidade, cláusula das ROE, ferramenta/configurações, condições de parada, evidência esperada.

**EX068.** Password spraying e testes de negação de serviço.

**EX069.** Para evitar a expansão silenciosa das técnicas além do que foi autorizado.

**EX070.** F2 (páginas de erro verbosas), com pontuação 3.

**EX071.** Restringir a administração aos jump hosts e exigir MFA enquanto as senhas se tornam únicas.

**EX072.** Pontuação 6, faixa high.

**EX073.** lab_scope, lab_wilson e lab_flows.

**EX074.** Tentar varrer sistemas reais do TRB.

**EX075.** O SWIFT está EXCLUDED e precisa ser removido do plano.

**EX076.** Demonstrar o impacto com a menor ação e, então, parar.

**EX077.** Aprovações extras explícitas e confirmação das ROE.

**EX078.** Passos ordenados com horários e links de evidência.

**EX079.** `T1190 detected 0/2 GAP`

**EX080.** ok — detected 2/3.

**EX081.** Quando a evidência do reteste mostra que o problema está fechado.

**EX082.** Correções sistêmicas em vez de culpa individual.

**EX083.** Responsável e data de vencimento.

**EX084.** Um host de produção pode ser marcado erroneamente como em escopo se o inventário estiver desatualizado.

**EX085.** Id do engajamento, lembrete de escopo, janela e contato do testador.

**EX086.** Parar e reagendar para uma nova janela autorizada.

**EX087.** O log de atividades e o índice de evidência no cofre.

**EX088.** F1 e F4 FIXED; F3 STILL OPEN (corrigidos 2 de 3).

**EX089.** Dois minutos.

**EX090.** Não. O F3 permanece aberto.

**EX091.** Recusar removê-lo, oferecer uma resposta da gestão ao lado e escalar o pedido.

**EX092.** Achados adjacentes a pagamentos e de fluxo não aprovado do razão.

**EX093.** Cria uma trilha de auditoria se a pressão voltar e protege a integridade do processo de asseguração.

**EX094.** Fatos, evidência e linha do tempo — não conclusões jurídicas.

**EX095.** O acesso web→razão não aprovado pode precisar tanto de imposição na rede quanto de negação na camada da aplicação.

**EX096.** Quando as simulações afetam a equipe (por exemplo, exercícios de phishing).

**EX097.** Enviesa as alegações (p-hacking) e viola o pré-registro.

**EX098.** Como uma lacuna de amostra pequena que precisa de mais ensaios, não como prova de detecção zero permanente.

**EX099.** Adversários e sistemas mudam, então testes antigos perdem comportamentos novos.

**EX100.** Testes web trimestrais no estilo WSTG.

**EX101.** Exercícios de cenário guiados por ameaças.

**EX102.** Manter os testes web trimestrais e financiar exercícios guiados por ameaças a cada dois anos.

**EX103.** Sem módulos de exploit (ou sem varredura ao vivo do TRB; ou sem integração com todo sistema de tickets).

**EX104.** Precision e recall em derivas de inventário plantadas, ou comportamento de falhar fechado em arquivos de escopo corrompidos.

**EX105.** Somente inventários sintéticos.

**EX106.** Identificadores de clientes e outras especificidades sensíveis.

**EX107.** Um aprendizado, uma premissa quebrada e uma pergunta para o supervisor.

**EX108.** Uma melhoria de runbook ou um checklist que a equipe possa usar sem Sam.

**EX109.** Clareza de escopo, hashes de evidência, racional da severidade e privacidade (overclaim também).

**EX110.** Aponta linhas específicas e sugere uma correção concreta.

**EX111.** Porcentagens sem denominadores enganam quem decide.

**EX112.** only-in-docs, only-on-network e type-conflict (e match).

**EX113.** Falhar fechado com um motivo claro e um código de saída diferente de zero.

**EX114.** Não. Precisa rodar offline em arquivos locais.

**EX115.** Outro estudante ou testador independente.

**EX116.** A ferramenta não substitui a disciplina das ROE nem as verificações de autorização.

**EX117.** Não. As métricas permanecem como pré-registradas.

**EX118.** Não é um framework de exploit de red team.

**EX119.** Um leitor deve saber exatamente o que foi mostrado e o que não foi.

**EX120.** Integrar tickets do FindingsDesk ou estudar métricas de detecção guiadas por ameaças.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v3.1 Specification Document. <https://www.first.org/cvss/v3.1/specification-document>
- MITRE ATT&CK, including T1078 Valid Accounts. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
