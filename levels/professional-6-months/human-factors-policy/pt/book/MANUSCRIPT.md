# Fatores Humanos e Política Cibernética: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 029, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão na edição em inglês; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os cinco laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais em atividade que migram para funções de coordenação de segurança e apoiam o reporte pelos funcionários, os procedimentos de verificação e um relato honesto às lideranças.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam barreiras de um questionário, calculam tempos até o veredito, apuram fatores de quase-incidentes, montam um gráfico de reportes mensais e comparam duas versões de veredito, sempre sobre dados sintéticos; nenhum funcionário, inquilino, e-mail ou conta real está envolvido. Os procedimentos são praticados com encenação anunciada e testados com voluntários que conhecem o propósito. O livro não recomenda phishing simulado no primeiro ano; qualquer simulação posterior deve ser anunciada, acordada com os representantes dos funcionários, evitar iscas sobre salário, moradia ou saúde, dar um retorno gentil, permanecer agregada e ficar fora dos processos de desempenho. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma profissional ao longo de um curso de seis meses enquanto ela se torna coordenadora de segurança numa associação de habitação: fundamentos, contexto, prática autorizada, métodos, ferramentas, fluxo de trabalho, controles, análise de caso, comunicação e ética, qualidade, um laboratório supervisionado e a revisão de um portfólio. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Grace Mwangi** | Coordenadora de segurança e participante do curso | Inventada |
| **Alan Pryce** | Mentor | Inventado |
| **Harlow Professional Academy** | Instituição de formação fictícia | Inventada |
| **Ferngate Housing Association** | Associação de habitação fictícia, 180 funcionários | Inventada |

### Fontes principais

Adams e Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff e Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Cialdini (2021); Bada, Sasse e Nurse (2019), arXiv:1901.02672; Lain, Kostiainen e Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem

Você vai (1) explicar ideias centrais de segurança em termos humanos; (2) descrever o papel do profissional na segurança centrada nas pessoas; (3) definir metas pessoais de aprendizagem.

### 1.1 Ideias centrais

Grace Mwangi, uma gerente administrativa que está migrando para a função de coordenadora de segurança, matricula-se num curso profissional de seis meses na fictícia Harlow Professional Academy. Seu mentor, Alan Pryce, começa pelas ideias centrais: confidencialidade, integridade e disponibilidade; ameaças e vulnerabilidades; e controles que reduzem o risco. Ele explica cada uma com exemplos do empregador dela, a fictícia Ferngate Housing Association, uma associação de habitação que tem 180 funcionários e guarda os cadastros dos inquilinos e os pagamentos de aluguel. Um e-mail falso que altera os dados bancários de um prestador ameaça a integridade e o dinheiro; um notebook perdido ameaça a confidencialidade.

### 1.2 O papel do profissional

Alan explica que a nova função de Grace fica entre os funcionários, os gestores e o fornecedor de TI. Ela vai ajudar os funcionários a reportar mensagens suspeitas, conduzir sessões curtas de aprendizagem, verificar se os procedimentos de verificação são seguidos e prestar contas aos gestores. Adams e Sasse (1999) mostraram que os usuários não são o inimigo, e Sasse, Brostoff e Weirich (2001) defenderam que a visão do elo mais fraco deve ser transformada pelo design. O papel de Grace é tornar o comportamento seguro fácil e bem-vindo, não policiar os colegas, o que combina com sua experiência em apoiar pessoas.

### 1.3 Metas de aprendizagem

Grace define metas de aprendizagem: entender os ataques comuns contra associações de habitação, aprender medição simples, escrever procedimentos claros e lidar com questões éticas como as simulações. Alan sugere que ela mantenha um portfólio de trabalho, com os procedimentos que escrever, os dados que analisar e reflexões sobre casos. O portfólio será revisado no último capítulo. Definir metas cedo a ajuda a se concentrar durante um curso curto e lhe dá uma forma de avaliar o próprio progresso por resultados concretos, e não por impressões vagas. Alan concorda com as metas.

### Exemplo resolvido

Grace aprende as ideias centrais de segurança com exemplos da Ferngate, define sua função de coordenadora como de apoio, e não de policiamento, e estabelece metas de aprendizagem com um portfólio.

> **Caso sintético.** A Ferngate é sintética; Adams e Sasse (1999) e Sasse et al. (2001) são reais.

### Erros e limites

As funções podem derivar para a fiscalização. As metas precisam ser revisitadas.

### Exercícios

- **EX001 — Exemplo de integridade.** Que exemplo da Ferngate ameaça a integridade? *Rubrica:* 3 = um e-mail falso que altera os dados bancários de um prestador;; 2 = alteração bancária;; 1 = notebook perdido;; 0 = nenhuma.

- **EX002 — Posição da função.** Entre quem fica a função de Grace? *Rubrica:* 3 = funcionários, gestores e o fornecedor de TI;; 2 = três grupos;; 1 = vago;; 0 = nenhuma.

- **EX003 — Propósito da função.** Qual é o propósito da função de Grace? *Rubrica:* 3 = tornar o comportamento seguro fácil e bem-vindo;; 2 = apoio;; 1 = policiamento;; 0 = nenhuma.

- **EX004 — Elo mais fraco.** O que Sasse, Brostoff e Weirich (2001) defenderam? *Rubrica:* 3 = a visão do elo mais fraco deve ser transformada pelo design;; 2 = design;; 1 = culpa;; 0 = nenhuma.

- **EX005 — Portfólio.** O que o portfólio de Grace vai conter? *Rubrica:* 3 = procedimentos, análises e reflexões;; 2 = portfólio;; 1 = vago;; 0 = nenhuma.

### Síntese

Os profissionais traduzem as ideias de segurança em termos humanos e capacitam, em vez de policiar.

<a id="ch-02"></a>

## Capítulo 2 — Fatores humanos e política cibernética: contexto de serviços e partes interessadas

### Objetivos de aprendizagem

Você vai (1) mapear os serviços e as partes interessadas da Ferngate; (2) identificar onde as pessoas enfrentam decisões de segurança; (3) entender as preocupações das partes interessadas.

### 2.1 Serviços e pessoas

Grace mapeia os serviços da Ferngate: gestão de locações, reparos, cobrança de aluguel e apoio comunitário. As partes interessadas incluem inquilinos, funcionários, prestadores de reparos, o fornecedor de TI, o conselho e o regulador do setor de habitação. Os funcionários costumam trabalhar fora do escritório, visitando inquilinos com tablets, e usam e-mail e um sistema de gestão habitacional. Os inquilinos contatam a Ferngate por telefone, e-mail e um portal on-line. Cada relação cria oportunidades de personificação, como prestadores falsos pedindo pagamento ou pessoas que ligam fingindo ser inquilinos para obter informações sobre um vizinho. Ela desenha o mapa numa página.

### 2.2 Pontos de decisão

Grace lista os pontos em que os funcionários enfrentam decisões de segurança: atender pedidos telefônicos de informações sobre inquilinos, aprovar faturas de prestadores, abrir anexos enviados por inquilinos e entrar no sistema em tablets compartilhados. Ela conversa com cinco colegas sobre momentos difíceis recentes. Uma agente de habitação descreve alguém que ligou dizendo ser filho de uma inquilina e pediu o novo endereço dela. Uma assistente financeira descreve uma fatura urgente vinda de um endereço parecido com o de um prestador. Essas conversas ancoram seu trabalho em pressões reais, e não em ameaças abstratas. Ela escreve cada história sem nomes.

### 2.3 Preocupações das partes interessadas

Grace entrevista as partes interessadas sobre suas preocupações. Os gestores se preocupam com fraudes e com o escrutínio do regulador. Os funcionários se preocupam em ser culpados por erros e com trabalho extra. Os inquilinos, por meio de um painel de inquilinos, se preocupam com a privacidade e querem ter certeza de que a Ferngate não pedirá dados bancários por e-mail. O fornecedor de TI se preocupa com pedidos pouco claros dos funcionários. Ela registra as preocupações numa tabela simples. Entender as preocupações a ajuda a desenhar mudanças que as respondam, tornando o apoio mais provável entre os grupos. Os gestores revisam a tabela.

### Exemplo resolvido

Grace mapeia os serviços e as partes interessadas, registra pontos de decisão a partir de histórias dos colegas e tabula as preocupações das partes interessadas.

> **Caso sintético.** Todos os detalhes são sintéticos.

### Erros e limites

As entrevistas refletem poucas vozes. As preocupações mudam.

### Exercícios

- **EX006 — Trabalho externo.** Como os agentes de habitação costumam trabalhar? *Rubrica:* 3 = fora do escritório, com tablets, visitando inquilinos;; 2 = móvel;; 1 = vago;; 0 = nenhuma.

- **EX007 — Exemplo da ligação.** O que queria o falso filho que ligou? *Rubrica:* 3 = o novo endereço de uma inquilina;; 2 = endereço;; 1 = vago;; 0 = nenhuma.

- **EX008 — Preocupação dos funcionários.** Com o que os funcionários se preocupam? *Rubrica:* 3 = culpa e trabalho extra;; 2 = duas;; 1 = fraude;; 0 = nenhuma.

- **EX009 — Preocupação dos inquilinos.** Sobre o que os inquilinos querem garantia? *Rubrica:* 3 = a Ferngate nunca pede dados bancários por e-mail;; 2 = e-mail;; 1 = vago;; 0 = nenhuma.

- **EX010 — Tabela de preocupações.** Por que registrar as preocupações das partes interessadas? *Rubrica:* 3 = para desenhar mudanças que as respondam;; 2 = insumo para o design;; 1 = vago;; 0 = nenhuma.

### Síntese

O contexto dos serviços e das partes interessadas mostra onde as pessoas decidem e o que as preocupa.

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e manuseio de evidências

### Objetivos de aprendizagem

Você vai (1) trabalhar dentro de uma autorização por escrito; (2) manusear com segurança as evidências vindas dos reportes; (3) proteger a privacidade no trabalho de segurança.

### 3.1 Autorização

Alan explica que os coordenadores de segurança devem agir dentro de uma autorização por escrito. Grace obtém um mandato curto do diretor executivo da Ferngate que descreve o que ela pode fazer: gerenciar a caixa postal de reporte, revisar as mensagens reportadas com o fornecedor de TI, conduzir sessões de aprendizagem e revisar os logs de verificação. Ele declara o que ela não pode fazer: ler as caixas postais dos funcionários, monitorar pessoas individualmente ou fazer testes enganosos sem aprovação dos gestores e dos representantes dos funcionários. A autorização protege Grace, os colegas e a Ferngate ao deixar os limites claros antes que surja qualquer problema. Ela guarda uma cópia assinada.

### 3.2 Manuseio de evidências

As mensagens reportadas são evidências de ataques. Grace aprende a manuseá-las com segurança: nunca clicar em links nem abrir anexos dos reportes no seu computador normal; encaminhar os itens suspeitos ao fornecedor de TI pelo método combinado; registrar data, tipo e desfecho sem copiar dados pessoais; e guardar os registros numa pasta restrita. Se um reporte sugere um incidente grave, como um vazamento de dados de inquilinos, ela segue o plano de incidentes e preserva as informações conforme a orientação do fornecedor de TI, em vez de investigar sozinha.

### 3.3 Proteção da privacidade

Os reportes às vezes contêm dados de inquilinos ou mensagens pessoais. Grace retira os dados pessoais dos resumos e guarda os reportes originais apenas pelo tempo necessário. Ela não registra quem reportou o quê em nenhum resumo compartilhado com os gestores. Explica aos gestores que isso protege a privacidade dos inquilinos e incentiva os funcionários a reportar sem medo de serem julgados. A proteção da privacidade faz parte da prática autorizada, porque o trabalho de segurança não deve criar novos danos enquanto tenta evitar outros. Os gestores concordam com essa abordagem. Alan concorda.

### Exemplo resolvido

Grace obtém um mandato com limites claros, manuseia com segurança as mensagens reportadas e retira os dados pessoais dos resumos.

> **Caso sintético.** O mandato é sintético.

### Erros e limites

Os mandatos precisam de atualização. O manuseio de evidências precisa do apoio do fornecedor.

### Exercícios

- **EX011 — Limite do mandato.** Cite uma coisa que Grace não pode fazer. *Rubrica:* 3 = ler as caixas postais dos funcionários;; 2 = monitoramento;; 1 = revisar reportes;; 0 = nenhuma.

- **EX012 — Manuseio seguro.** O que Grace nunca deve fazer com os itens reportados? *Rubrica:* 3 = clicar em links ou abrir anexos no seu computador;; 2 = não clicar;; 1 = vago;; 0 = nenhuma.

- **EX013 — Incidente grave.** O que Grace faz se um reporte sugere um incidente grave? *Rubrica:* 3 = segue o plano de incidentes e a orientação do fornecedor;; 2 = plano;; 1 = investiga sozinha;; 0 = nenhuma.

- **EX014 — Regra dos resumos.** O que fica de fora dos resumos para os gestores? *Rubrica:* 3 = quem reportou o quê;; 2 = identidade de quem reporta;; 1 = vago;; 0 = nenhuma.

- **EX015 — Razão da privacidade.** Por que a privacidade incentiva o reporte? *Rubrica:* 3 = os funcionários não temem ser julgados;; 2 = confiança;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática autorizada estabelece limites, trata as evidências com segurança e protege a privacidade.

<a id="ch-04"></a>

## Capítulo 4 — Fatores humanos e política cibernética: métodos centrais

### Objetivos de aprendizagem

Você vai (1) aplicar um questionário anônimo curto; (2) conduzir conversas estruturadas; (3) transformar os achados em prioridades.

### 4.1 Um questionário curto

Grace aplica um questionário anônimo de seis perguntas que pergunta aos funcionários se sabem como reportar, o que os impede, se tiveram retorno depois de reportar, quão confiantes se sentem diante de pedidos por telefone e quanto esforço dedicam à segurança por semana. O painel de inquilinos revisa uma versão separada de duas perguntas para os inquilinos. Ela recebe 126 respostas de funcionários, de 180. O laboratório conta as barreiras que os funcionários escolheram. Ela compartilha os principais resultados com todos os funcionários em duas semanas, explicando o que vai acontecer em seguida. O questionário é anônimo. Os representantes dos funcionários o aprovam.

### Laboratório — Barreiras entre 126 respostas de funcionários

```python
# Barriers among 126 synthetic staff responses (multiple choice).
b = {"unsure if worth reporting": 51, "never heard back": 38, "don't know how": 33, "too busy": 27, "fear of blame": 15}
for k, v in sorted(b.items(), key=lambda x: -x[1]): print(f"{k}: {v}/126 = {v / 126:.0%}")
```

Execute com `python3 lab_barriers.py`. Saída verificada:

```text
unsure if worth reporting: 51/126 = 40%
never heard back: 38/126 = 30%
don't know how: 33/126 = 26%
too busy: 27/126 = 21%
fear of blame: 15/126 = 12%
```

### 4.2 Conversas estruturadas

Grace conduz oito conversas estruturadas de quinze minutos com funcionários de equipes diferentes, usando as mesmas cinco perguntas em todas e tomando notas sem nomes. Os agentes de habitação descrevem a incerteza diante de pedidos telefônicos de parentes. A equipe financeira descreve a pressão de prestadores que exigem pagamento urgente. Várias pessoas contam que reportaram um e-mail suspeito uma vez e nunca tiveram retorno. As conversas estruturadas acrescentam razões e histórias aos números do questionário, e as perguntas uniformes facilitam a comparação das respostas entre as equipes. As notas são conferidas com cada pessoa.

### 4.3 Definição de prioridades

Grace combina os achados em três prioridades: facilitar o reporte com um botão e respostas rápidas; oferecer um procedimento claro para pedidos telefônicos sobre inquilinos; e introduzir a verificação por retorno de ligação nas alterações de dados bancários de prestadores. Cada prioridade responde ao mesmo tempo a uma barreira comum e a uma preocupação das partes interessadas do capítulo 2. Ela apresenta as prioridades aos gestores com as evidências por trás delas. Os gestores as aprovam e destinam um pequeno orçamento, impressionados por as prioridades virem da experiência dos funcionários, e não de conselhos genéricos. O trabalho começa em um mês.

### Exemplo resolvido

Grace aplica o questionário a 126 funcionários, conduz oito conversas estruturadas e define três prioridades baseadas em evidências.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Viés de autodeclaração. Oito conversas são poucas.

### Exercícios

- **EX016 — Taxa de resposta.** Qual foi a taxa de resposta dos funcionários? *Rubrica:* 3 = 70%;; 2 = 126 de 180;; 1 = 126%;; 0 = nenhuma.

- **EX017 — Barreira principal no laboratório.** Qual foi a principal barreira no laboratório? *Rubrica:* 3 = não ter certeza se vale reportar, 51 de 126;; 2 = incerteza;; 1 = vago;; 0 = nenhuma.

- **EX018 — Perguntas uniformes.** Por que usar as mesmas perguntas em todas as conversas? *Rubrica:* 3 = para comparar as respostas entre as equipes;; 2 = comparabilidade;; 1 = vago;; 0 = nenhuma.

- **EX019 — Prioridade do telefone.** Que prioridade trata dos pedidos por telefone? *Rubrica:* 3 = um procedimento claro para pedidos telefônicos sobre inquilinos;; 2 = procedimento;; 1 = vago;; 0 = nenhuma.

- **EX020 — Divulgação dos resultados.** Quando Grace compartilhou os principais resultados com os funcionários? *Rubrica:* 3 = em duas semanas;; 2 = duas semanas;; 1 = nunca;; 0 = nenhuma.

### Síntese

Questionários simples e conversas estruturadas produzem prioridades fundamentadas na experiência da equipe.

<a id="ch-05"></a>

## Capítulo 5 — Fatores humanos e política cibernética: ferramentas e interpretação

### Objetivos de aprendizagem

Você vai (1) usar ferramentas simples para acompanhar reportes e vereditos; (2) interpretar corretamente medidas básicas; (3) evitar comparações enganosas.

### 5.1 Ferramentas simples

Grace usa uma planilha e um script curto em Python fornecido pelo curso para acompanhar os reportes. Cada linha guarda a data, a equipe, a categoria, o veredito e a hora em que o veredito foi enviado, sem nomes de quem reportou. O script calcula as contagens mensais, a proporção de reportes que eram maliciosos e a mediana do tempo até o veredito. Ela aprende a conferir a saída do script com algumas linhas contadas à mão, o que lhe dá confiança de que a ferramenta funciona corretamente antes de compartilhar os números com os gestores.

### 5.2 Interpretação das medidas

Grace aprende a interpretar as medidas com cuidado. Um aumento nos reportes pode significar mais ataques ou mais disposição para reportar; ela confere os logs do filtro do fornecedor de TI para saber qual. Uma proporção baixa de reportes maliciosos pode significar que os funcionários reportam demais, mas Alan explica que o excesso de reportes é um sinal saudável num programa novo, porque mostra que as pessoas se sentem seguras para perguntar. O laboratório calcula a mediana do tempo até o veredito antes e depois de as respostas passarem a usar modelos, mostrando uma grande melhora. Ela registra as duas verificações.

### Laboratório — Mediana do tempo até o veredito antes e depois dos modelos

```python
# Median hours to verdict before and after templated replies (synthetic).
before = [4, 9, 18, 22, 26, 30, 41, 48, 70]; after = [0.5, 1, 1.5, 2, 3, 3.5, 5, 6, 20]
m = lambda x: sorted(x)[len(x) // 2]
print(f"before: median {m(before)} h; after: median {m(after)} h")
```

Execute com `python3 lab_verdict.py`. Saída verificada:

```text
before: median 26 h; after: median 3 h
```

### 5.3 Comparações enganosas

Grace evita comparações que induzem a erro. Ela não ranqueia as equipes pela contagem de reportes, porque o tamanho e a exposição das equipes são diferentes, e os rankings envergonhariam alguns grupos. Ela só divulga números de grupos com pelo menos vinte funcionários. Mostra as mudanças ao longo do tempo com o número de casos por trás de cada número. Quando um gestor pergunta qual equipe é a pior, ela explica por que essa pergunta não pode ser respondida de forma justa com os dados e oferece uma pergunta mais útil: onde as pessoas precisam de mais apoio?

### Exemplo resolvido

Grace acompanha os reportes com uma planilha e um script, interpreta corretamente os aumentos e o excesso de reportes e evita rankings injustos entre equipes.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Números pequenos variam. Os scripts precisam ser conferidos depois de mudanças.

### Exercícios

- **EX021 — Conferência manual.** Por que conferir à mão a saída do script? *Rubrica:* 3 = para confirmar que a ferramenta funciona antes de compartilhar;; 2 = verificação;; 1 = vago;; 0 = nenhuma.

- **EX022 — Aumento dos reportes.** Que duas coisas um aumento nos reportes pode significar? *Rubrica:* 3 = mais ataques ou mais disposição;; 2 = duas causas;; 1 = vago;; 0 = nenhuma.

- **EX023 — Excesso de reportes.** Como Alan vê o excesso de reportes num programa novo? *Rubrica:* 3 = como sinal saudável de que as pessoas se sentem seguras;; 2 = saudável;; 1 = problema;; 0 = nenhuma.

- **EX024 — Tempos de veredito no laboratório.** Como mudou a mediana do tempo até o veredito com os modelos? *Rubrica:* 3 = 26 horas antes e 3 horas depois dos modelos;; 2 = mais rápido;; 1 = vago;; 0 = nenhuma.

- **EX025 — Pergunta melhor.** Que pergunta Grace ofereceu no lugar de qual equipe é a pior? *Rubrica:* 3 = onde as pessoas precisam de mais apoio;; 2 = apoio;; 1 = vago;; 0 = nenhuma.

### Síntese

Ferramentas simples fornecem medidas úteis quando interpretadas com cuidado e de forma justa.

<a id="ch-06"></a>

## Capítulo 6 — Fatores humanos e política cibernética: fluxo operacional

### Objetivos de aprendizagem

Você vai (1) desenhar o fluxo diário de reporte; (2) definir tempos de resposta e responsabilidades; (3) lidar com picos e ausências.

### 6.1 Fluxo diário

Grace desenha o fluxo diário. Os funcionários reportam por um botão que envia as mensagens a uma caixa postal compartilhada e mostra uma nota de agradecimento. Duas vezes por dia, Grace ou sua reserva revisa os novos reportes, agrupa as duplicatas, envia com modelos os vereditos claros de inofensivo ou spam e encaminha ao fornecedor de TI os itens incertos ou maliciosos. O fornecedor de TI confirma os vereditos e remove as mensagens maliciosas de todas as caixas postais. Grace registra os desfechos na planilha. O fluxo leva cerca de vinte minutos por dia nos dias normais.

### 6.2 Tempos e responsabilidades

Grace define metas: agradecimento imediato, veredito em até um dia útil e remoção das mensagens maliciosas confirmadas em até duas horas depois da confirmação. Ela registra por escrito quem faz cada etapa: Grace na triagem, uma reserva nomeada quando ela está fora, o fornecedor de TI na análise e na remoção, e o gerente financeiro em qualquer reporte relacionado a pagamentos. Responsabilidades claras impedem que os reportes caiam entre as pessoas, o que as entrevistas mostraram ter acontecido antes, quando ninguém sabia ao certo quem devia responder. Os gestores aprovam as metas. Cada responsável assina.

### 6.3 Picos e ausências

Durante campanhas de ataque, os reportes podem se multiplicar. Grace se planeja para os picos: quando chegam mais de vinte reportes sobre uma mesma mensagem, ela envia uma mensagem curta a todos os funcionários dizendo que a mensagem é conhecida e está sendo removida, o que reduz os reportes duplicados e tranquiliza as pessoas. Para as ausências, sua reserva tem um runbook curto e acesso à caixa postal. Ela testa o arranjo de reserva tirando uma folga planejada numa semana normal e revisando depois o que aconteceu. O teste corre bem. Nada se perde.

### Exemplo resolvido

Grace desenha um fluxo de triagem duas vezes ao dia com modelos, define metas de resposta e responsabilidades nomeadas e se planeja para picos de campanha e ausências.

> **Caso sintético.** O fluxo é sintético.

### Erros e limites

A revisão duas vezes ao dia pode ser lenta durante campanhas. As reservas precisam de prática.

### Exercícios

- **EX026 — Tempo diário.** Quanto tempo leva o fluxo nos dias normais? *Rubrica:* 3 = cerca de vinte minutos;; 2 = 20 minutos;; 1 = vago;; 0 = nenhuma.

- **EX027 — Meta de veredito.** Qual é a meta de veredito? *Rubrica:* 3 = em até um dia útil;; 2 = um dia;; 1 = vago;; 0 = nenhuma.

- **EX028 — Reportes de pagamento.** Quem cuida dos reportes relacionados a pagamentos? *Rubrica:* 3 = o gerente financeiro;; 2 = financeiro;; 1 = Grace sozinha;; 0 = nenhuma.

- **EX029 — Mensagem de pico.** O que Grace envia durante as campanhas? *Rubrica:* 3 = uma mensagem dizendo que o e-mail é conhecido e está sendo removido;; 2 = aviso a todos;; 1 = vago;; 0 = nenhuma.

- **EX030 — Teste da reserva.** Como Grace testou o arranjo de reserva? *Rubrica:* 3 = tirando uma folga planejada e revisando depois;; 2 = ausência planejada;; 1 = vago;; 0 = nenhuma.

### Síntese

Um fluxo de trabalho claro, com metas, donos e planos para os picos, mantém o reporte confiável.

<a id="ch-07"></a>

## Capítulo 7 — Fatores humanos e política cibernética: controles e verificação

### Objetivos de aprendizagem

Você vai (1) introduzir um procedimento para pedidos por telefone e um controle de retorno de ligação para prestadores; (2) verificar se os controles funcionam na prática; (3) ajustar os controles depois do retorno recebido.

### 7.1 Procedimento para o telefone

Grace escreve um procedimento para pedidos telefônicos sobre inquilinos: os funcionários nunca compartilham por telefone o endereço, os contatos ou a situação de um inquilino com ninguém além do próprio inquilino verificado; pedidos de parentes, órgãos ou autoridades são recebidos por escrito e repassados ao responsável pela proteção de dados. Um roteiro curto ajuda os funcionários a recusar com educação: Não posso passar essa informação por telefone, mas posso encaminhar seu pedido à nossa equipe de dados. O procedimento elimina a necessidade de julgar se quem liga parece genuíno, algo que os atacantes exploram.

### 7.2 Controle de retorno de ligação

Com o gerente financeiro, Grace introduz um controle de retorno de ligação. Qualquer pedido de alteração dos dados bancários de um prestador fica retido até que uma segunda pessoa ligue para o prestador no número que já consta dos registros da Ferngate. O sistema financeiro bloqueia pagamentos para os novos dados até que o retorno de ligação seja registrado. Os prestadores recebem uma carta explicando a regra. Cialdini (2021) descreve como a autoridade e a urgência pressionam as pessoas; o controle faz com que ninguém precise resistir sozinho a essa pressão sob prazo. A maioria dos prestadores responde positivamente. O financeiro concorda.

### 7.3 Verificação e ajuste

Grace verifica os dois controles. Ela confere o log financeiro todo mês e confirma que cada alteração de dados bancários tem um retorno de ligação registrado. Pede a cinco agentes de habitação que pratiquem o roteiro telefônico em encenação anunciada, com um colega fazendo o papel de quem liga. Todos usam o roteiro corretamente depois de um treino, mas dois dizem que ele soa ríspido para os parentes de inquilinos idosos. Grace o ajusta, acrescentando uma frase que explica que a regra protege o familiar deles. A verificação e o retorno melhoram os controles juntos.

### Exemplo resolvido

Grace escreve um procedimento para pedidos telefônicos com roteiro, monta um controle de retorno de ligação para prestadores e verifica os dois, ajustando o roteiro depois do retorno da encenação.

> **Caso sintético.** Os procedimentos são sintéticos; Cialdini (2021) é real.

### Erros e limites

Os roteiros podem soar frios. Os registros dos prestadores podem estar desatualizados.

### Exercícios

- **EX031 — Regra do telefone.** O que os funcionários não podem compartilhar por telefone? *Rubrica:* 3 = endereço, contatos ou situação do inquilino;; 2 = dados do inquilino;; 1 = vago;; 0 = nenhuma.

- **EX032 — Número para retorno.** Que número é usado nos retornos de ligação? *Rubrica:* 3 = o número dos registros da Ferngate;; 2 = registros;; 1 = o do pedido;; 0 = nenhuma.

- **EX033 — Princípios de pressão.** Que pressões o controle de retorno de ligação alivia? *Rubrica:* 3 = autoridade e urgência;; 2 = Cialdini;; 1 = vago;; 0 = nenhuma.

- **EX034 — Encenação.** Como o roteiro telefônico foi testado? *Rubrica:* 3 = encenação anunciada com um colega fazendo o papel de quem liga;; 2 = encenação;; 1 = teste secreto;; 0 = nenhuma.

- **EX035 — Mudança no roteiro.** Por que o roteiro foi ajustado? *Rubrica:* 3 = soava ríspido para os parentes;; 2 = tom;; 1 = vago;; 0 = nenhuma.

### Síntese

Os controles eliminam julgamentos difíceis, e a verificação com retorno os aprimora.

<a id="ch-08"></a>

## Capítulo 8 — Fatores humanos e política cibernética: análise de caso supervisionada

### Objetivos de aprendizagem

Você vai (1) analisar sem culpa um quase-incidente de segurança; (2) identificar os fatores contribuintes; (3) recomendar melhorias sob supervisão.

### 8.1 O quase-incidente

Uma assistente financeira recebeu uma fatura de um endereço parecido com o e-mail de um prestador de serviços de telhado, com novos dados bancários e um pedido de pagamento no mesmo dia por causa de um suposto problema de fluxo de caixa. Ela começou a atualizar os dados, mas o sistema financeiro bloqueou o pagamento até o retorno de ligação. O retorno de ligação revelou que o pedido era falso. Grace analisa o quase-incidente sob a supervisão de Alan. A assistente o reportou imediatamente quando o retorno de ligação não confirmou o pedido, e o gerente financeiro lhe agradece publicamente.

### 8.2 Fatores contribuintes

Grace identifica os fatores sem culpar a assistente. O domínio parecido passou nas verificações de e-mail; a etiqueta de externo estava presente, mas era fácil de não ver numa tela movimentada; o pedido usava urgência e uma história plausível; e a carga de trabalho do fechamento do mês deixava pouco tempo. O controle de retorno de ligação funcionou como projetado. Ela observa que a assistente agiu de forma razoável sob pressão e que o sistema barrou a fraude, que é exatamente como as defesas em camadas devem funcionar. O laboratório apura os fatores deste e de outros três quase-incidentes do ano.

### Laboratório — Fatores contribuintes em quatro quase-incidentes

```python
# Contributing factors across four near misses (synthetic).
nm = [{"urgency", "lookalike domain", "workload"}, {"urgency", "authority"}, {"urgency", "lookalike domain"}, {"urgency", "workload", "authority"}]
for f in ("urgency", "lookalike domain", "workload", "authority"): print(f, sum(f in s for s in nm), "of 4")
```

Execute com `python3 lab_nearmiss.py`. Saída verificada:

```text
urgency 4 of 4
lookalike domain 2 of 4
workload 2 of 4
authority 2 of 4
```

### 8.3 Recomendações

Grace recomenda tornar a etiqueta de externo mais visível na caixa postal do financeiro, enviar aos prestadores um lembrete de que a Ferngate sempre retorna a ligação e compartilhar o caso de forma anônima na próxima sessão de aprendizagem, como uma história de sucesso. Alan revisa a análise e sugere acrescentar uma nota sobre como o log de retornos de ligação ajudou. Compartilhar quase-incidentes como sucessos incentiva o reporte e mostra aos funcionários que o sistema foi desenhado para apoiá-los. O gerente financeiro aprova todas as recomendações. O trabalho começa na semana seguinte. Os funcionários são informados.

### Exemplo resolvido

Grace analisa um quase-incidente de fatura falsa barrado pelo retorno de ligação, encontra os fatores sem culpar ninguém e recomenda etiquetas visíveis, lembretes e a divulgação do sucesso.

> **Caso sintético.** O caso é sintético.

### Erros e limites

Os conjuntos de quase-incidentes são pequenos. Histórias de sucesso podem incentivar a complacência.

### Exercícios

- **EX036 — O que barrou o pagamento.** O que barrou o pagamento falso? *Rubrica:* 3 = o sistema financeiro o bloqueou até o retorno de ligação;; 2 = retorno de ligação;; 1 = a assistente;; 0 = nenhuma.

- **EX037 — História usada.** Que história a fatura falsa contava? *Rubrica:* 3 = um problema de fluxo de caixa que exigia pagamento no mesmo dia;; 2 = urgência;; 1 = vago;; 0 = nenhuma.

- **EX038 — Fator principal no laboratório.** Que fator apareceu nos quatro quase-incidentes do laboratório? *Rubrica:* 3 = urgência;; 2 = urgência, hesitando com carga de trabalho;; 1 = carga de trabalho;; 0 = nenhuma.

- **EX039 — Problema da etiqueta.** Que problema a etiqueta de externo tinha? *Rubrica:* 3 = era fácil de não ver numa tela movimentada;; 2 = visibilidade;; 1 = vago;; 0 = nenhuma.

- **EX040 — Forma de divulgação.** Como o caso será compartilhado? *Rubrica:* 3 = de forma anônima, como história de sucesso;; 2 = sucesso;; 1 = com culpa;; 0 = nenhuma.

### Síntese

A análise sem culpados mostra as defesas em camadas funcionando e transforma quase-incidentes em aprendizado.

<a id="ch-09"></a>

## Capítulo 9 — Comunicação, ética e relatórios

### Objetivos de aprendizagem

Você vai (1) comunicar mensagens de segurança sem medo; (2) decidir com ética sobre as simulações; (3) prestar contas aos gestores e ao conselho.

### 9.1 Comunicar sem medo

Grace escreve mensagens mensais curtas para os funcionários, com um exemplo recente, uma ação simples e um agradecimento pelos reportes. Ela evita imagens assustadoras e ameaças disciplinares. Bada, Sasse e Nurse (2019) constataram que as campanhas baseadas no medo muitas vezes falham. Ela também escreve um aviso curto para os inquilinos no site e nos boletins: a Ferngate nunca pedirá dados bancários por e-mail ou por mensagem de texto, e os inquilinos podem ligar para o número principal para conferir. As mensagens se concentram no que as pessoas podem fazer, o que gera confiança. Os funcionários gostam delas.

### 9.2 Decisão sobre simulações

Os gestores perguntam se a Ferngate deveria fazer phishing simulado. Grace considera as evidências, incluindo Lain, Kostiainen e Čapkun (2022), que constataram que algumas práticas comuns de simulação não ajudavam. Ela recomenda não fazer simulações no primeiro ano, enquanto o reporte e os controles se consolidam. Se forem usadas depois, as simulações devem seguir regras acordadas com os representantes dos funcionários: programa anunciado, nenhuma isca sobre salário, moradia ou saúde, retorno gentil e imediato, resultados agregados e nenhum uso em processos de desempenho. Os gestores aceitam a recomendação. A decisão fica registrada em ata.

### 9.3 Prestar contas para cima

Grace presta contas trimestralmente aos gestores e anualmente ao conselho. Os relatórios incluem medidas de resultado, como a proporção de mensagens suspeitas reportadas e o tempo até o veredito, os controles verificados, os quase-incidentes e o ônus para os funcionários. Ela declara os limites com honestidade e evita afirmar que a Ferngate está totalmente protegida. O conselho faz boas perguntas sobre fraudes de prestadores e a privacidade dos inquilinos, que Grace responde com suas evidências. Relatórios claros constroem confiança entre a coordenadora e as lideranças, o que garante apoio ao programa. O conselho lhe agradece.

### Exemplo resolvido

Grace escreve mensagens sem medo para funcionários e inquilinos, recomenda nenhuma simulação no primeiro ano e regras rígidas depois, e relata com honestidade os resultados aos gestores e ao conselho.

> **Caso sintético.** As comunicações são sintéticas; Bada et al. (2019) e Lain et al. (2022) são reais.

### Erros e limites

As mensagens mensais podem virar rotina. A atenção do conselho varia.

### Exercícios

- **EX041 — Partes da mensagem.** O que cada mensagem mensal contém? *Rubrica:* 3 = um exemplo, uma ação e um agradecimento;; 2 = três;; 1 = avisos;; 0 = nenhuma.

- **EX042 — Aviso aos inquilinos.** O que o aviso aos inquilinos promete? *Rubrica:* 3 = a Ferngate nunca pede dados bancários por e-mail ou mensagem de texto;; 2 = nunca;; 1 = vago;; 0 = nenhuma.

- **EX043 — Recomendação sobre simulações.** O que Grace recomendou para o primeiro ano? *Rubrica:* 3 = nenhuma simulação no primeiro ano;; 2 = nenhuma simulação, sem o limite do primeiro ano;; 1 = mensais;; 0 = sem resposta.

- **EX044 — Temas de isca proibidos.** Que temas de isca são proibidos se houver simulações depois? *Rubrica:* 3 = salário, moradia ou saúde;; 2 = angústia;; 1 = vago;; 0 = nenhuma.

- **EX045 — Conteúdo dos relatórios.** O que os relatórios de Grace incluem? *Rubrica:* 3 = resultados, controles verificados, quase-incidentes e ônus;; 2 = resultados;; 1 = atividades;; 0 = nenhuma.

### Síntese

Uma comunicação sem medo, decisões cuidadosas sobre simulações e um reporte honesto sustentam a confiança.

<a id="ch-10"></a>

## Capítulo 10 — Fatores humanos e política cibernética: qualidade e solução de problemas

### Objetivos de aprendizagem

Você vai (1) verificar a qualidade do serviço de reporte; (2) resolver um problema; (3) melhorar o serviço continuamente.

### 10.1 Verificações de qualidade

Grace verifica a qualidade todo mês: os vereditos são enviados em até um dia útil; os vereditos estão corretos; estão chegando reportes de todas as equipes; e os modelos são claros? Ela sorteia dez vereditos por mês e pede ao fornecedor de TI que os confirme. Também pergunta a duas pessoas que reportaram, escolhidas ao acaso a cada mês, se a resposta foi útil. As verificações de qualidade captam desvios lentos, como modelos que ficam desatualizados ou respostas que ficam secas nos períodos de movimento, antes que os funcionários percam a confiança no serviço. Ela registra cada resultado.

### 10.2 Solução de problemas

No quarto mês, os reportes dos agentes de habitação caem bruscamente. Grace confere os logs do filtro e não encontra queda nas mensagens suspeitas. Ela pergunta a dois agentes e descobre que uma atualização dos tablets removeu o botão de reporte do aplicativo de e-mail. Eles tinham suposto que o reporte não era mais desejado. O fornecedor de TI restaura o botão e acrescenta uma verificação depois das atualizações. Grace envia uma mensagem explicando o problema e agradecendo aos agentes. O laboratório mostra os reportes mensais dos agentes de habitação, com a queda e a recuperação.

### Laboratório — Reportes mensais dos agentes de habitação

```python
# Housing officer reports by month (synthetic).
for m, n in enumerate([11, 14, 16, 2, 15, 17], 1): print(f"month {m}: {n}")
```

Execute com `python3 lab_officers.py`. Saída verificada:

```text
month 1: 11
month 2: 14
month 3: 16
month 4: 2
month 5: 15
month 6: 17
```

### 10.3 Melhoria contínua

Grace mantém um log de melhorias que lista problemas, causas, correções e datas. Ela o revisa a cada trimestre com Alan e o fornecedor de TI, procurando padrões. Dois registros envolvem atualizações que removeram configurações, então o fornecedor acrescenta um checklist padrão pós-atualização. Um envolve um modelo confuso, que ela reescreve. A melhoria contínua transforma correções isoladas em mudanças duradouras, o que é importante numa organização pequena, onde os mesmos problemas voltariam sempre que os sistemas mudassem ou as pessoas saíssem. Alan lê o log a cada trimestre.

### Exemplo resolvido

Grace faz verificações mensais de qualidade, atribui a queda nos reportes dos agentes de habitação a uma atualização dos tablets e mantém um log de melhorias que leva a um checklist pós-atualização.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

As amostras podem deixar passar problemas. Os logs precisam de revisão.

### Exercícios

- **EX046 — Perguntas de qualidade.** Cite duas perguntas mensais de qualidade. *Rubrica:* 3 = rapidez e correção dos vereditos;; 2 = duas;; 1 = vago;; 0 = nenhuma.

- **EX047 — Causa da queda.** O que causou a queda dos agentes de habitação? *Rubrica:* 3 = uma atualização dos tablets removeu o botão de reporte;; 2 = atualização;; 1 = menos ataques;; 0 = nenhuma.

- **EX048 — Queda no laboratório.** Como variaram os reportes dos agentes de habitação ao longo dos seis meses? *Rubrica:* 3 = 14 e 16, depois 2 no mês quatro, depois 15;; 2 = queda e recuperação;; 1 = vago;; 0 = nenhuma.

- **EX049 — Padrão encontrado.** Que padrão o log de melhorias revelou? *Rubrica:* 3 = atualizações que removem configurações;; 2 = atualizações;; 1 = vago;; 0 = nenhuma.

- **EX050 — Correção do fornecedor.** O que o fornecedor acrescentou? *Rubrica:* 3 = um checklist padrão pós-atualização;; 2 = checklist;; 1 = vago;; 0 = nenhuma.

### Síntese

Verificações de qualidade e um registro de melhorias transformam correções em melhorias duradouras do serviço.

<a id="ch-11"></a>

## Capítulo 11 — Laboratório supervisionado

### Objetivos de aprendizagem

Você vai (1) testar com voluntários uma mudança nas mensagens de veredito; (2) comparar a compreensão entre as versões; (3) decidir sobre a adoção.

### 11.1 O teste

No laboratório supervisionado, Grace testa duas versões da mensagem de veredito. A versão A diz apenas se a mensagem era maliciosa. A versão B acrescenta uma frase que explica a pista, como um endereço parecido ou um pedido de pagamento incomum. Vinte voluntários, que conhecem o propósito, leem os vereditos de cinco mensagens sintéticas num ambiente de teste, metade vendo a versão A e metade a versão B. Depois, cada um avalia três novas mensagens sintéticas. Alan supervisiona, e os voluntários podem desistir a qualquer momento. Cada sessão dura vinte minutos.

### 11.2 Comparação dos resultados

O laboratório compara os julgamentos corretos sobre as novas mensagens entre os dois grupos. Os voluntários que leram a versão B julgam corretamente mais mensagens do que os que leram a versão A. Grace observa a amostra pequena e que os voluntários sabiam que seriam convidados a julgar mensagens, o que pode deixá-los mais cuidadosos do que o normal. Ainda assim, o resultado é compatível com a ideia de que explicações breves ajudam as pessoas a aprender com cada reporte. Ela registra as contagens e a diferença sem exagerá-las. Alan revisa a análise.

### Laboratório — Julgamentos corretos depois das versões A e B do veredito

```python
# Correct judgements of three new messages by ten volunteers per version (synthetic).
a = [2, 1, 2, 2, 1, 2, 3, 2, 1, 2]; b = [3, 2, 3, 3, 2, 3, 2, 3, 2, 2]
print(f"version A: {sum(a)}/30 correct; version B: {sum(b)}/30 correct")
```

Execute com `python3 lab_versions.py`. Saída verificada:

```text
version A: 18/30 correct; version B: 25/30 correct
```

### 11.3 Adoção

Grace recomenda adotar a versão B, já que ela custa só uma frase por veredito e pode ajudar os funcionários a aprender. Ela atualiza os modelos com as pistas comuns e treina sua reserva para escrever explicações curtas. Planeja verificar depois de três meses, com dados reais, se o reporte repetido melhora. Alan observa que ela seguiu um processo sólido: uma pergunta clara, um teste pequeno e justo, uma análise honesta e uma mudança barata com acompanhamento, que é como os profissionais devem melhorar os serviços. Os gestores aprovam a mudança.

### Exemplo resolvido

Grace testa duas versões de veredito com vinte voluntários, encontra julgamentos melhores depois das explicações e adota a versão B com acompanhamento.

> **Caso sintético.** O teste é sintético.

### Erros e limites

Amostra pequena. Os voluntários conheciam a tarefa.

### Exercícios

- **EX051 — Versão B.** O que a versão B acrescenta? *Rubrica:* 3 = uma frase que explica a pista;; 2 = explicação;; 1 = vago;; 0 = nenhuma.

- **EX052 — Resultado do laboratório.** O que o laboratório mostrou para os julgamentos corretos? *Rubrica:* 3 = A 18 de 30, B 25 de 30;; 2 = B melhor;; 1 = vago;; 0 = nenhuma.

- **EX053 — Cautela.** Por que os voluntários podem ter sido mais cuidadosos do que o normal? *Rubrica:* 3 = sabiam que julgariam mensagens;; 2 = consciência;; 1 = vago;; 0 = nenhuma.

- **EX054 — Custo.** Quanto custa a versão B? *Rubrica:* 3 = uma frase por veredito;; 2 = pouco;; 1 = vago;; 0 = nenhuma.

- **EX055 — Acompanhamento.** Que acompanhamento Grace planejou? *Rubrica:* 3 = verificar o reporte repetido depois de três meses;; 2 = acompanhamento;; 1 = vago;; 0 = nenhuma.

### Síntese

Testes pequenos e justos sustentam melhorias baratas quando acompanhados de dados reais.

<a id="ch-12"></a>

## Capítulo 12 — Portfólio de prática e revisão final

### Objetivos de aprendizagem

Você vai (1) montar um portfólio de prática; (2) apresentar resultados e limites; (3) planejar o desenvolvimento profissional contínuo.

### 12.1 O portfólio

Grace monta seu portfólio: o mandato, o mapa das partes interessadas, os achados do questionário e das conversas, os procedimentos e roteiros, o fluxo de trabalho e o runbook, a análise do quase-incidente, o log de qualidade, o relatório do laboratório e os relatórios trimestrais. Cada item tem uma nota curta explicando o que ele mostra sobre sua prática. Alan o revisa com ela, conferindo se todos os itens estão livres de dados pessoais e se as afirmações estão apoiadas em evidências. Um portfólio mostra não só o que ela fez, mas como ela raciocinou, o que importa na avaliação profissional. Ele fica guardado com segurança.

### 12.2 Resultados e limites

Grace apresenta os resultados depois de seis meses: a proporção de mensagens suspeitas reportadas subiu; a mediana do tempo até o veredito caiu de cerca de um dia para algumas horas; uma fatura falsa foi barrada pelo retorno de ligação; e o ônus para os funcionários ficou estável. Ela apresenta os limites: seis meses é pouco, os números são pequenos e parte da melhora pode refletir a novidade. Os gestores perguntam o que ela faria em seguida; ela sugere estender as regras de retorno de ligação aos pedidos de reembolso de inquilinos e revisar o procedimento telefônico com o painel de inquilinos. Os gestores concordam.

### 12.3 Desenvolvimento contínuo

Grace planeja seu desenvolvimento contínuo: entrar numa rede regional de coordenadores de segurança do setor de habitação, ler o Verizon DBIR anual e as orientações do NIST SP 800-50r1 e fazer um curso curto de proteção de dados. Alan sugere que ela seja mentora de um colega que atue como sua reserva, o que também fortalece a resiliência da Ferngate. Grace reflete que sua experiência em apoiar pessoas se mostrou mais útil do que ela esperava, porque a segurança centrada nas pessoas depende tanto de confiança, comunicação clara e ajuda prática quanto de conhecimento técnico. Alan aprova a conclusão do curso.

### Exemplo resolvido

Grace monta um portfólio, apresenta os resultados de seis meses com os limites e planeja o desenvolvimento contínuo e a mentoria.

> **Caso sintético.** Os resultados são sintéticos; o DBIR e o SP 800-50r1 são reais.

### Erros e limites

Os portfólios podem ser seletivos. Seis meses é pouco.

### Exercícios

- **EX056 — Conferência do portfólio.** O que Alan conferiu no portfólio? *Rubrica:* 3 = ausência de dados pessoais e afirmações apoiadas;; 2 = qualidade;; 1 = vago;; 0 = nenhuma.

- **EX057 — Resultado do tempo de veredito.** Como mudou a mediana do tempo até o veredito? *Rubrica:* 3 = de cerca de um dia para algumas horas;; 2 = mais rápido;; 1 = vago;; 0 = nenhuma.

- **EX058 — Próximo controle.** Que próximo controle Grace sugeriu? *Rubrica:* 3 = retorno de ligação para pedidos de reembolso de inquilinos;; 2 = reembolsos;; 1 = vago;; 0 = nenhuma.

- **EX059 — Mentoria.** De quem Grace será mentora? *Rubrica:* 3 = de um colega que atua como sua reserva;; 2 = reserva;; 1 = vago;; 0 = nenhuma.

- **EX060 — Lição da experiência.** Por que a experiência de Grace se mostrou útil? *Rubrica:* 3 = a segurança centrada nas pessoas depende de confiança e comunicação;; 2 = habilidades com pessoas;; 1 = vago;; 0 = nenhuma.

### Síntese

Um portfólio mostra raciocínio e resultados, e o desenvolvimento contínuo sustenta a prática.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Grace Mwangi, Alan Pryce, a Harlow Professional Academy, a Ferngate Housing Association e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Um e-mail falso que altera os dados bancários de um prestador.

**EX002.** Entre os funcionários, os gestores e o fornecedor de TI.

**EX003.** Tornar o comportamento seguro fácil e bem-vindo, não policiar os colegas.

**EX004.** Que a visão do elo mais fraco deve ser transformada desenhando a segurança em torno das pessoas.

**EX005.** Os procedimentos que escrever, os dados que analisar e reflexões sobre casos.

**EX006.** Fora do escritório, visitando inquilinos com tablets.

**EX007.** O novo endereço da inquilina.

**EX008.** Ser culpados por erros e trabalho extra.

**EX009.** De que a Ferngate nunca pedirá dados bancários por e-mail.

**EX010.** Para que as mudanças possam ser desenhadas para respondê-las e conquistar apoio.

**EX011.** Ler as caixas postais dos funcionários, monitorar pessoas individualmente ou fazer testes enganosos sem aprovação.

**EX012.** Clicar em links ou abrir anexos dos reportes no seu computador normal.

**EX013.** Segue o plano de incidentes e a orientação do fornecedor de TI.

**EX014.** Quem reportou o quê, junto com os dados pessoais.

**EX015.** Porque os funcionários reportam mais quando não temem ser julgados.

**EX016.** 70%, já que 126 de 180 funcionários responderam.

**EX017.** Não ter certeza se uma mensagem valia o reporte, escolhida por 51 de 126 (40%).

**EX018.** Para tornar as respostas comparáveis entre as equipes.

**EX019.** Um procedimento claro para pedidos telefônicos sobre inquilinos.

**EX020.** Em até duas semanas depois do questionário.

**EX021.** Para confirmar que a ferramenta funciona corretamente antes de compartilhar os números.

**EX022.** Mais ataques ou mais disposição para reportar.

**EX023.** Como um sinal saudável de que as pessoas se sentem seguras para perguntar.

**EX024.** Cerca de 26 horas antes dos modelos e 3 horas depois.

**EX025.** Onde as pessoas precisam de mais apoio?

**EX026.** Cerca de vinte minutos por dia.

**EX027.** Um veredito em até um dia útil.

**EX028.** O gerente financeiro.

**EX029.** Uma mensagem curta a todos os funcionários dizendo que a mensagem é conhecida e está sendo removida.

**EX030.** Tirando uma folga planejada e revisando o que aconteceu.

**EX031.** O endereço, os contatos ou a situação de um inquilino, exceto ao próprio inquilino verificado.

**EX032.** O número que já consta dos registros da Ferngate.

**EX033.** A pressão da autoridade e da urgência, descrita por Cialdini.

**EX034.** Por meio de encenação anunciada, com um colega fazendo o papel de quem liga.

**EX035.** Porque soava ríspido para os parentes, então foi acrescentada uma explicação.

**EX036.** O sistema bloqueou o pagamento até o retorno de ligação, e o retorno revelou a fraude.

**EX037.** Um suposto problema de fluxo de caixa que exigia pagamento naquele mesmo dia.

**EX038.** A urgência, presente nos quatro.

**EX039.** Era fácil de não ver numa tela movimentada.

**EX040.** De forma anônima, como história de sucesso numa sessão de aprendizagem.

**EX041.** Um exemplo recente, uma ação simples e um agradecimento pelos reportes.

**EX042.** Que a Ferngate nunca pedirá dados bancários por e-mail ou por mensagem de texto.

**EX043.** Nenhuma simulação no primeiro ano.

**EX044.** Salário, moradia ou saúde.

**EX045.** Medidas de resultado, controles verificados, quase-incidentes e ônus para os funcionários, com os limites.

**EX046.** Se os vereditos chegam a tempo, se estão corretos, se os reportes chegam de todas as equipes e se os modelos são claros.

**EX047.** Uma atualização dos tablets removeu o botão de reporte do aplicativo de e-mail.

**EX048.** 14 e 16 nos meses dois e três, 2 no mês quatro e 15 no mês cinco, depois da correção.

**EX049.** Dois problemas foram causados por atualizações que removeram configurações.

**EX050.** Um checklist padrão pós-atualização.

**EX051.** Uma frase que explica a pista que revelou a mensagem.

**EX052.** Os leitores da versão A julgaram corretamente 18 de 30 e os da versão B, 25 de 30.

**EX053.** Porque sabiam que estavam sendo convidados a julgar mensagens.

**EX054.** Apenas uma frase a mais por veredito.

**EX055.** Verificar depois de três meses se o reporte repetido melhora.

**EX056.** Se os itens estavam livres de dados pessoais e se as afirmações estavam apoiadas em evidências.

**EX057.** De cerca de um dia para algumas horas.

**EX058.** Estender as regras de retorno de ligação aos pedidos de reembolso de inquilinos.

**EX059.** Um colega que atua como sua reserva.

**EX060.** Porque a segurança centrada nas pessoas depende de confiança, comunicação e ajuda prática.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Verizon Business. (2024). *2024 Data breach investigations report*. Verizon. <https://www.verizon.com/business/resources/reports/dbir/>
