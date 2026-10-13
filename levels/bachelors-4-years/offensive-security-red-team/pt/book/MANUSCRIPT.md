# Segurança Ofensiva Autorizada e Red Team: Um Livro para o Bacharelado

- Idioma: português do Brasil (`pt`); bacharelado, quatro anos; aproximadamente 3.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 40 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3; os capítulos 9–40 (EX025–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

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

### 1.7 1.7 Nota aplicada

Sam pratica a tradução de parágrafos das ROE em testes de pertinência no papel antes de abrir o TrackScope. Quando uma frase diz "VLAN web, exceto gateways de pagamento", ele escreve a expressão de conjuntos e lista todos os endereços de gateway conhecidos a partir do registro de ativos. Só então ele carrega o arquivo de escopo. Terceirizados que pulam a etapa do papel propõem com frequência hosts que ficam ao lado do SWIFT "porque o ping funcionou". A etapa do papel é mais lenta e evita incidentes de jornal. A lista do registro de ativos serve também como evidência depois. Os auditores podem casar cada carga do arquivo de escopo com a lista assinada do registro, de modo que qualquer host acrescentado depois se destaca.

### 1.8 1.8 Aritmética de conjuntos resolvida

Dada a VLAN V e as exclusões E, Sam calcula V\E e depois faz a interseção com a lista proposta do dia, P. Só P∩(V\E) pode ser carregado. Ele testa a calculadora com o SWIFT dentro de V e confirma que ele nunca aparece na saída. Um segundo teste coloca em P um endereço fora de V e confirma que ele também é rejeitado. Juntos, os dois testes cobrem as duas formas pelas quais o escopo falha: hosts excluídos vazando de volta e hosts fora da faixa chegando numa planilha amigável. A saída da calculadora é salva com a data, para que a lista carregada no dia possa ser reproduzida depois.

### 1.9 1.11 Cena

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

### 2.7 2.7 Nota aplicada

A regra de falha fechada do PulseMap é testada na CI apagando o arquivo de escopo e verificando que toda API retorna negação. Sam acrescentou esse teste depois que uma configuração errada em staging serviu brevemente listas de permissão vazias. Painéis que não conseguem negar são piores que nenhum painel. Ele demonstra o caminho de negação a todo estagiário novo na primeira semana. O teste de CI também cobre um arquivo corrompido, não só um ausente. Os dois caminhos precisam retornar negação em todos os endpoints, incluindo o health check, antes que o build possa passar.

### 2.8 2.8 Zoneamento da plataforma

TrackScope, FindingsDesk e PulseMap ficam numa zona de avaliação com conduítes controlados apenas para staging. Sam revisa esses conduítes a cada trimestre da mesma forma que revisa os fluxos de negócio do TRB — porque a plataforma pode ferir o banco se estiver mal ligada. Um conduíte da zona de avaliação para a produção deixaria um job mal configurado enviar tráfego a sistemas vivos; por isso, sua ausência é verificada, não presumida. Cada revisão registra quais conduítes existem, quem os aprovou e quando foram usados pela última vez. Conduítes sem uso são removidos em vez de ficarem abertos por conveniência.

### 2.9 2.9 Bug do denominador

Um bug do PulseMap certa vez fazia n assumir 1 por padrão. O teste de regressão de Sam define n=0 e espera um bloco de erro, não 100%. Com n igual a 1 por padrão, um único host tocado teria aparecido como 100% de cobertura, exatamente a porcentagem enganosa contra a qual o Capítulo 1 alerta. O teste de regressão agora roda em todo build, e o PulseMap se recusa a desenhar um bloco de cobertura sem um denominador explícito vindo do arquivo de escopo. Um bloco de erro é honesto; um número confiante construído sobre um valor padrão não é. A correção saiu com uma entrada no changelog que nomeia o bug.

### 2.10 2.11 Cena

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

### 3.7 3.7 Nota aplicada

A saída do dry-run é colada no canal do engajamento antes que qualquer modo de escrita rode. Os colegas têm dois minutos para objetar. Sam certa vez pegou um path traversal para dentro de um arquivo de evidências porque um colega leu o dry-run com cuidado. A revisão social vence a esperteza solitária em scripts operacionais. Dois minutos é curto o bastante para não atrasar uma janela e longo o bastante para um leitor cuidadoso. A saída colada lista todo endereço-alvo, o cartão de método e os caminhos de escrita que o script vai tocar, para que o leitor possa comparar cada linha com a /26 assinada e com a exclusão do SWIFT. A objeção de qualquer leitor pausa a execução até ser resolvida e anotada no log da janela.

### 3.8 3.8 Política de dados de teste

Clientes sintéticos nos fixtures usam documentos de identidade obviamente falsos. Sam rejeita fixtures que reutilizam números pessoais com aparência real, mesmo quando não são usados em produção. A transferência de hábito importa. Um fixture parecido com um número de identidade real pode ser copiado para um teste contra a produção por alguém com pressa. Valores obviamente falsos não podem ser confundidos com dados de clientes, e o hábito se estende a todo engajamento posterior. Um revisor que vê num fixture um número de identidade plausível pergunta de onde ele veio; um valor como FAKE-000-001 encerra a pergunta imediatamente e não pode ser confundido com um cliente durante um incidente.

### 3.9 3.9 Varredura de segredos na CI

Os repositórios da plataforma falham na CI se strings de alta entropia parecem chaves. Sam coloca na lista de permissão apenas fixtures de teste claramente marcados como FAKE. Uma chave de aparência real num arquivo de teste ainda treina as pessoas a ignorar o aviso; por isso, a marcação é obrigatória. Cada fixture permitido é listado com seu dono e o motivo pelo qual é seguro, e a lista é revisada sempre que as regras de CI mudam. Permitir pelo marcador, e não pelo caminho do arquivo, significa que uma chave real colada numa pasta de fixtures continua sendo pega. Quando a CI bloqueia um commit, o desenvolvedor rotaciona a string mesmo que ela só tenha existido localmente.

### 3.10 3.11 Cena

O quadro de revisão de scripts de Sam exibe três trechos rejeitados: uma chamada requests com verify=False, um subprocess com shell=True sobre um nome de host e um laço de novas tentativas sem jitter. Estagiários novos rubricam o quadro depois de lê-lo. O quadro é bobo e eficaz. Quando Sam quase cola verify=False "só em staging", ele vê as próprias iniciais e para. Cada trecho fica ao lado da versão segura: verify ligado com a CA interna do TRB, um subprocess chamado com uma lista de argumentos e um laço de novas tentativas com limite e backoff.

### 3.11 3.20 Extra

O quadro de trechos rejeitados ganha um quarto exemplo sempre que a CI pega um novo antipadrão. Sam data cada trecho. O quadro é um museu vivo de quase-erros. Cada trecho novo traz uma nota de uma linha sobre o que a CI pegou e por que era perigoso, como uma nova tentativa sem limite contra um host lento. Pede-se aos estagiários que expliquem um trecho com as próprias palavras durante a primeira semana. A nota nomeia a regra, não a pessoa que escreveu o código. A equipe de Sam revisa o quadro todo ano e aposenta os trechos cuja regra de CI se tornou rotina.

### Exemplo resolvido (TRB sintético)

O lab_scope.py de Sam usa apenas o módulo ipaddress da biblioteca padrão e faixas de documentação; ele nunca abre um socket.

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX007 — Regra do socket.** Por que o lab_scope não pode abrir sockets? *Rubrica:* 3 = apenas offline/sintético; nenhuma varredura acidental; 2 = parcial; 1 = sockets não têm problema; 0 = nada.
- **EX008 — Dois padrões inseguros.** Nomeie dois padrões de script proibidos na equipe da plataforma. *Rubrica:* 3 = dois entre segredos, TLS desligado, shell não sanitizado, novas tentativas sem limite; 2 = um; 1 = nenhum; 0 = nada.
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

### 4.7 4.7 Nota aplicada

Os exercícios de citação exigem abrir a página viva do NIST ou do PTES, não o resumo de um blog. Sam reprovou um rascunho inicial por citar uma paráfrase de segunda mão do SP 800-115 que inventava uma cláusula. Só fontes primárias — a mesma regra de nunca inventar DOIs. A página do NIST também mostra o status e a data do documento. Sam agora registra, ao lado de cada citação no rascunho, a data em que abriu a página primária e a seção em que se apoiou. Os revisores podem então conferir uma afirmação contra a mesma página, em vez de confiar na memória dele.

### 4.8 4.8 Passagem pelo público

Antes de enviar, Sam lê o sumário executivo em voz alta para alguém de fora da segurança. Se a pessoa não consegue reformular a decisão pedida, ele reescreve. Jargão que sobrevive a essa passagem é um defeito. A reformulação do ouvinte é anotada no histórico do rascunho para comparação posterior. No relatório da conta de administrador compartilhada, um ouvinte de finanças reformulou o pedido como "pagar por contas nominais no sistema de empréstimos", o que bateu. Um rascunho anterior tinha produzido "alguma coisa sobre senhas", o que o mandou de volta para reescrita. O ouvinte de finanças foi escolhido de propósito.

### 4.9 4.9 Auditoria da voz passiva

Achados que escondem os agentes na voz passiva são reescritos. "Senhas foram reutilizadas" vira "A conta de administrador de empréstimos usava a mesma senha da VPN", quando isso é conhecido. Nomear o sistema torna o achado acionável e testável. Quando o agente não é conhecido, a frase diz isso claramente, por exemplo "os logs não mostram qual administrador mudou a configuração". Isso mantém o achado honesto sem inventar um culpado e aponta direto para a lacuna de logs como uma segunda questão a corrigir. Corrigir o rascunho "os desenvolvedores ignoraram a segurança" exigiu apenas uma frase reescrita que nomeava o sistema e o log ausente.

### 4.10 4.11 Cena

Um rascunho de achado certa vez dizia "os desenvolvedores ignoraram a segurança". O jurídico pediu reescrita antes do material do conselho. Sam produziu: "O serviço de empréstimos aceitava uma senha privilegiada compartilhada; os logs não conseguem atribuir mudanças a uma pessoa." Os mesmos fatos, num tom financiável. Ele guarda as duas versões nas notas de ensino para mostrar a diferença. As duas versões descrevem a mesma lacuna de logs. A reescrita remove a acusação, mas mantém todos os fatos: uma senha privilegiada compartilhada e nenhuma atribuição nos logs. É por isso que ela sobreviveu à revisão jurídica e ainda disse aos donos do serviço de empréstimos exatamente o que mudar.

### 4.11 4.20 Extra

Os troféus de tom são adesivos bobos em achados impressos que os desenvolvedores elogiaram como claros. Sam prefere adesivos a métricas que ninguém lê. Cada adesivo registra qual achado foi elogiado e por quê, para que o próximo relatório possa copiar a clareza, e não apenas o adesivo. Clareza que os desenvolvedores notam é clareza que gera correções. Sam guarda os achados elogiados numa pasta como exemplos para estagiários, ao lado do rascunho reescrito "os desenvolvedores ignoraram a segurança", para que os bons e os maus modelos fiquem visíveis. A contagem de achados fica em segundo plano nos relatórios de Sam, porque um achado claro que é corrigido importa mais que uma lista longa.

### Exemplo resolvido (TRB sintético)

Sam reescreve "a equipe web é incompetente" como "a camada web alcança o ledger-db por um fluxo não aprovado; controle: impor a matriz aprovada".

> **Caso sintético — Riverstone Transit Bank (TRB).** O banco, Sam Ito, TrackScope/FindingsDesk/PulseMap e todos os números são inventados para fins didáticos.

### Erros e limites

Este livro não concede nenhuma autoridade para testar bancos ou sistemas de pagamento reais. Os laboratórios usam apenas endereços de faixas de documentação e dados sintéticos; código de exploit nunca é fornecido.

### Exercícios

- **EX010 — Reescrita.** Transforme "reutilização estúpida de senhas" em linguagem profissional de achado. *Rubrica:* 3 = condição do sistema + impacto + nenhum insulto; 2 = parcial; 1 = mantém o insulto; 0 = nada.
- **EX011 — Afirmação especulativa.** Como Sam deve rotular "atacantes já roubaram fundos"? *Rubrica:* 3 = especulativa/não confirmada; separada dos fatos; 2 = parcial; 1 = como fato; 0 = nada.
- **EX012 — Regra de citação.** O que Sam nunca pode inventar ao citar? *Rubrica:* 3 = DOIs / referências falsas; 2 = parcial; 1 = nada; 0 = nada.

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

### 5.7 5.7 Nota aplicada

O roteiro de recusa é ensaiado numa encenação em que um funcionário faz o papel de um diretor impaciente. Sam precisa manter o tom respeitoso sem ceder. As revisões em vídeo mostram se ele sorri nervosamente até concordar; esses clipes são apagados depois da orientação, mas a lição fica. Na encenação, o diretor pede a Sam que "só dê uma olhada rápida" num host fora da /26. O roteiro de Sam nomeia a cláusula das ROE, oferece levar uma mudança de escopo ao dono e dá um prazo realista para a aprovação. Praticar as palavras exatas as torna disponíveis sob pressão real.

### 5.8 5.8 Flashcards de frameworks

O baralho de Sam tem um cartão por framework: SP 800-115, PTES, WSTG, ATT&CK, TIBER-EU, CBEST — propósito e o que ele não é. Usar o CBEST como lista de verificação web é uma resposta comum no verso dos cartões. O cartão do TIBER-EU, por exemplo, diz que ele enquadra red teaming orientado por inteligência de ameaças para entidades financeiras e não é um padrão de varredura de vulnerabilidades. Escrever o lado "o que não é" obriga Sam a entender o propósito de cada framework, e não o seu nome, e o baralho é revisado sempre que um framework publica uma nova versão.

### 5.9 5.9 Fronteira do laboratório doméstico

O laboratório doméstico de Sam usa RFC1918 e nunca o DNS do TRB. Misturar a VPN com o dever de casa é um quase-acidente relatado, se acontecer. As faixas privadas RFC1918 em casa não podem colidir com o endereçamento do TRB se Sam nunca conectar a VPN do banco enquanto experimenta. Usar o DNS do TRB em casa vazaria nomes internos e poderia mandar tráfego do laboratório para o banco. Se houver uma confusão, ele a relata como quase-acidente, para que a regra de fronteira possa ser melhorada, em vez de torcer em silêncio para que ninguém tenha notado.

### 5.10 5.11 Cena

Sam recusa um convite de meetup para demonstrar "como hackeamos nosso banco", embora o trabalho tenha sido autorizado. Capturas de tela viajam. Em vez disso, ele oferece uma palestra sobre desenho de ROE com exemplos sintéticos. Os organizadores aceitam. A contenção diante do uso dual inclui o que você se recusa a apresentar. Uma captura de tela de um achado autorizado do TRB ainda mostra nomes de host reais, versões e fraquezas que talvez ainda não tenham sido corrigidas. Depois de exibida na tela de um meetup, ela não pode ser retirada. A palestra sobre ROE compartilha a lição reutilizável sem os detalhes do banco.

### 5.11 5.20 Extra

As palestras alternativas para meetups usam apenas demonstrações com faixas de documentação. Os slides de Sam são públicos; suas capturas de tela do TRB não são. Faixas de documentação como 198.51.100.0/24 tornam impossível que uma demonstração aponte para um host real, e achados sintéticos não carregam nenhuma informação sobre os sistemas do TRB. Antes de publicar, Sam confere cada slide em busca de nomes internos, IDs de tickets e endereços reais. Suas capturas de tela do TRB ficam dentro do FindingsDesk, onde o acesso é controlado e registrado, e são apagadas quando termina o período de retenção do engajamento. O deck público é revisado uma vez pelo dono das ROE antes da publicação.

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

### 6.7 6.7 Nota aplicada

Os grafos de alcançabilidade anotam as arestas com "autenticada" ou "só de rede". Uma aresta só de rede para hosts vizinhos do razão eleva a severidade mesmo sem credenciais, porque um roubo de credenciais em outro lugar completa o caminho. Os primeiros grafos de Sam não tinham essa anotação e subclassificaram um achado. Depois da correção, toda aresta para um nó vizinho dos pagamentos traz sua anotação, e o lab_rank dá mais peso às arestas só de rede para a camada do razão. O achado antes subclassificado foi repontuado e reenviado com uma nota explicando a mudança, para que os leitores da primeira versão não ficassem com a classificação mais baixa.

### 6.8 6.8 Conjuntos de corte

Para os nós vizinhos dos pagamentos, Sam procura conjuntos de corte de arestas cuja remoção os isolaria da Internet. Essas arestas se tornam prioridades de monitoramento e controle mesmo quando não são "vulneráveis" no sentido de um scanner. Para o ledger-db, o conjunto de corte acabou sendo de duas arestas: a conexão direta da camada web e o acesso administrativo que contornava o jump host. Remover essas duas isola o razão dos caminhos voltados para a internet. Monitorá-las custa muito menos do que vigiar todo host. Essas duas arestas são também as que o F3 e a regra do jump host tratam.

### 6.9 6.9 Evidência das arestas

Cada aresta crítica do grafo cita a fonte de inventário ou de varredura sob as ROE. Arestas sem fonte são removidas. Uma fonte pode ser uma entrada do registro de ativos, uma exportação de regras de firewall ou um resultado de varredura autorizada com sua data. Uma aresta desenhada de memória ou por suposição não pode ser verificada; por isso, não pode sustentar um achado, e deixá-la faria o grafo inteiro parecer mais certo do que é. Quando falta uma fonte, Sam pergunta ao dono e só devolve a aresta ao grafo com evidência.

### 6.10 6.11 Cena

Ao traçar um caminho de um modelo de PC de agência comprometido até o ledger-db, Sam encontra quatro arestas. Remover a aresta web→razão (F3) e exigir o jump host para a administração corta os caminhos perigosos restantes. O grafo não precisava de cinquenta nós — precisava do conjunto de corte. Ele apaga as arestas decorativas do slide. Mostrar quatro arestas e o conjunto de corte fez a discussão da correção levar minutos em vez de uma hora, porque os donos podiam ver exatamente quais duas mudanças importavam. O slide agora mostra apenas as quatro arestas do caminho.

### 6.11 6.20 Extra

Os slides de conjunto de corte usam no máximo seis arestas. Sam apaga o resto na frente do público para ensinar foco. Um slide com cinquenta arestas esconde as duas que importam; um slide com seis torna o conjunto de corte visível para um executivo em segundos. Apagar as arestas ao vivo também mostra que as removidas eram contexto, não evidência. Sam mantém o grafo completo no apêndice, com fontes para cada aresta, para que os engenheiros ainda possam conferir seu raciocínio e nada fique escondido da revisão.

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

### 7.7 7.7 Nota aplicada

As cláusulas de captura das ROE especificam as horas de retenção e quem pode rodar o wireshark. O pedido padrão de Sam é "configurações e logs primeiro; pacotes só se esses falharem". A maioria dos achados web do TRB nunca precisa de pacotes; quando precisa, a cláusula já está escrita. Escrever a cláusula com antecedência significa que um pedido urgente de captura durante uma janela não leva a uma decisão improvisada sobre dados de clientes. A cláusula também nomeia quem apaga os arquivos quando as horas de retenção expiram. A pessoa nomeada confirma a exclusão no ticket da captura quando as horas de retenção expiram, para que ninguém presuma que os arquivos sumiram.

### 7.8 7.8 Humildade diante dos banners

Banners alimentam o inventário, não o teatro de severidade. Sam registra a exposição de versão como baixa, a menos que esteja associada a um caminho vulnerável alcançável sob as ROE — que este curso, ainda assim, não vai explorar no mundo real. Um banner que mostra uma versão antiga pode ter sido corrigido por um backport do fornecedor; por isso, a versão sozinha não prova uma fraqueza. Registrá-la como inventário permite aos donos planejar atualizações sem inflar um relatório com achados alarmantes, mas não verificados. Se uma fraqueza alcançável for confirmada depois sob as ROE, a severidade é repontuada com essa evidência.

### 7.9 7.9 Lint de faixas de documentação

Os exemplos na documentação passam por um lint que garante que os IPs sejam de faixas de documentação. O lint de Sam reprovou o rascunho de um post de blog que usava um endereço real do TRB; boa captura. O endereço real teria revelado parte do layout de rede do TRB e poderia ter convidado os leitores a sondá-lo. O lint roda em toda mudança de documentação e bloqueia a publicação até que o endereço seja substituído por um exemplo de faixa de documentação, como um da 198.51.100.0/24. O rascunho do blog foi corrigido e o endereço original foi relatado ao dono da rede.

### 7.10 7.11 Cena

Um aluno pede para tentar uma varredura TCP FIN em staging "para o trabalho do curso". Sam mostra a lista de métodos proibidos das ROE e a página de fronteira do curso. Em vez disso, eles fazem um quiz offline de PCAP. A curiosidade é redirecionada, não envergonhada — e não é satisfeita em redes bancárias. O quiz usa capturas sintéticas, então o aluno ainda vê como os pacotes se parecem sem que nenhum tráfego toque uma rede do TRB. Sam também registra o pedido como nota de ensino, sem o nome do aluno, porque ele mostra onde a fronteira do curso precisa ser explicada mais cedo.

### 7.11 7.20 Extra

As respostas do quiz de PCAP nunca incluem bytes de payload de clientes reais. Só PCAPs sintéticos. As capturas sintéticas são geradas com endereços de faixas de documentação e payloads inventados, de modo que nenhum dado de cliente pode vazar pelo material didático. As respostas descrevem cabeçalhos, tempos e padrões de fluxo, que é do que os alunos precisam para raciocinar sobre detecção. Sam regenera os arquivos do quiz quando o curso muda, em vez de editar capturas à mão, para que sua procedência fique clara. Cada arquivo regenerado recebe hash, e o hash é publicado com o quiz. Como todo arquivo do quiz é gerado, os alunos nunca manuseiam capturas que contenham tráfego real de clientes do TRB.

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

### 8.7 8.7 Nota aplicada

A importação em lote tem teto de 500 linhas e exige um segundo aprovador acima de 100. Sam viu um analista quase importar um dump de scanner que incluía hosts fora do escopo como "informativos". Tetos e aprovadores são chatos de propósito. Um host fora do escopo "informativo" ainda é evidência de que alguém testou fora das ROE; por isso, ele precisa de revisão, não de armazenamento silencioso. O segundo aprovador confere o resumo do dry-run contra o escopo assinado antes que importações maiores prossigam. O aprovador nunca é a pessoa que rodou a varredura, para que a verificação seja independente.

### 8.8 8.8 Exercícios de migração

As migrações de esquema rodam numa cópia, com checksums antes e depois. Sam registra a contagem de linhas. Uma migração que muda as contagens silenciosamente reprova no exercício. Checksums e contagens de linhas na cópia mostram se uma migração preservou todo achado e toda referência de evidência. Se as contagens diferem, a migração é corrigida e rodada de novo numa cópia nova; a produção nunca é usada como teste. Sam guarda os números de antes e depois com o script de migração, para que um revisor possa confirmar que o exercício passou.

### 8.9 8.9 Escritas idempotentes

As atualizações de tickets são idempotentes por id do achado. Entregas duplicadas vindas de redes instáveis não conseguem criar F1s duplicados. Como cada atualização é indexada pelo ID do achado, aplicar a mesma requisição duas vezes deixa o ticket no mesmo estado que aplicá-la uma vez. Uma criação repetida do F1 atualiza o F1 em vez de inserir um segundo registro. Isso importa no TRB, onde os links de VPN para a zona de avaliação caem com frequência, e achados duplicados inflariam as contagens nos relatórios ao conselho. Por isso, as contagens para o conselho continuam verdadeiras mesmo nos dias de rede ruim.

### 8.10 8.11 Cena

O dry-run da importação em lote do FindingsDesk certa vez revelou 40 hosts fora das ROE embutidos num CSV de scanner. A importação foi bloqueada. Na retrospectiva, Sam agradece mais ao dry-run do que a qualquer funcionalidade nova lançada naquele mês. Quarenta hosts fora do escopo num banco de dados de avaliação teriam parecido resultados de testes autorizados e poderiam ter motivado trabalho de acompanhamento contra sistemas que ninguém havia aprovado. O dry-run transformou um problema silencioso de dados numa decisão visível, e a configuração do scanner que produziu o CSV foi corrigida antes da janela seguinte.

### 8.11 8.12 Extensão

As atualizações idempotentes de tickets salvaram o TRB quando uma VPN instável reenviou doze vezes a mesma chamada de criação de achado. O FindingsDesk mostrou um F1, não doze. Sam acrescenta essa história ao onboarding para que os engenheiros parem de temer o "exatamente uma vez" como algo acadêmico. Doze tickets F1 duplicados teriam mostrado ao conselho doze achados críticos abertos e acionado o dono doze vezes. A idempotência tornou a falha de rede inofensiva, que é exatamente o que os engenheiros precisam ver antes de confiar no desenho. Os engenheiros novos agora testam as novas tentativas na primeira semana.

### 8.12 8.16 Complemento

O limiar de aprovação de 100 linhas do FindingsDesk existe porque um dump de 2.000 linhas certa vez ficou na fila durante a noite e disparou uma tempestade de alertas para os donos. Sam documenta o id do incidente ao lado da constante no código. Ligar a constante ao registro do incidente diz aos futuros engenheiros por que o limiar existe antes que decidam aumentá-lo. Sem o comentário, 100 parece arbitrário e convida à remoção. Com ele, qualquer pessoa que mude o valor pode ler o que aconteceu quando importações grandes rodaram sem revisão e acionaram os donos a noite inteira. O comentário nomeia o ENG-441 e a data da mudança.

### 8.13 8.20 Extra

O id do incidente da tempestade de alertas noturna é ENG-441 no arquivo do curso. Sam o referencia no comentário da constante. A entrada do arquivo descreve a fila noturna, quantos donos foram acionados e a mudança que introduziu o limiar de aprovação. Um revisor que encontra a constante pode seguir o link e julgar o histórico diretamente. A mesma prática vale para o teto de 500 linhas: todo limite de segurança do FindingsDesk aponta para o motivo pelo qual foi definido, de modo que os limites são mudados de forma deliberada, e não por alguém arrumando o código.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). O Riverstone Transit Bank, Sam Ito e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
