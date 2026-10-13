# Governança de Dados: Curso de Mestrado

- Idioma: português do Brasil (`pt`); curso 164, mestrado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–8 de 8 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; dois laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: mestrandos que avaliam se a curadoria de dados (*data stewardship*) melhora a qualidade dos dados em um órgão público.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam endereços duplicados antes e depois da normalização em um cadastro sintético e estimam um efeito de diferenças em diferenças sobre tempos sintéticos de correção, com intervalo por *bootstrap*. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública. O código dos laboratórios e suas saídas são mantidos exatamente como na edição em inglês.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um mestrando desde uma busca estruturada na literatura e um seminário, passando por um desenho quase experimental, explicações concorrentes, um piloto de medição, a análise e a redação da dissertação, até uma defesa com revisão independente. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Tomás Ferreira** | Mestrando | Inventado |
| **Dra. Ingrid Solberg** | Orientadora | Inventada |
| **Instituto de Tecnologia Kestrel** | Instituto fictício | Inventado |
| **Prefeitura do Condado de Arden** | Órgão local fictício, com cinco departamentos que mantêm cópias de endereços | Inventado |

### Fontes principais

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-1:2022; Khatri e Brown (2010), [doi:10.1145/1629175.1629210](https://doi.org/10.1145/1629175.1629210); Wang e Strong (1996); Shadish, Cook e Campbell (2002). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Pergunta de pesquisa e método de revisão da literatura

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa de mestrado sobre curadoria de dados; (2) conduzir uma busca estruturada na literatura; (3) registrar as decisões de busca com transparência.

### 1.1 O estudante e o contexto

Tomás Ferreira inicia um mestrado de dois anos no fictício Instituto de Tecnologia Kestrel, sob orientação da Dra. Ingrid Solberg. A organização parceira é a fictícia Prefeitura do Condado de Arden, onde cinco departamentos mantêm suas próprias cópias dos endereços dos moradores: tributação imobiliária, coleta de lixo, bibliotecas, licenças de estacionamento e assistência social. Os endereços são digitados de formas diferentes em cada sistema, de modo que o mesmo domicílio aparece várias vezes, cartas vão para endereços antigos e os erros levam semanas para ser corrigidos. A prefeitura planeja nomear curadores de dados (*data stewards*) em dois departamentos, como piloto.

### 1.2 Formulando a pergunta

Tomás rascunha uma pergunta: nomear curadores de dados reduz o tempo de correção de erros de endereço? A Dra. Solberg pede que ele a torne respondível. Ele especifica o desfecho como os dias entre a notificação de um erro e sua correção no sistema; a intervenção como curadores nomeados, com responsabilidades definidas; a comparação como os departamentos sem curadores; e o período como seis meses antes e seis meses depois do piloto. O DAMA-DMBOK2 descreve a curadoria como a responsabilização pelos dados em nome de outras pessoas, o que lhe dá uma definição a testar, e não um slogan.

### 1.3 Buscando na literatura

Tomás pesquisa em duas bases acadêmicas e nas publicações da DAMA e da ISO com termos fixos: *data stewardship*, *data governance*, *master data* e *data quality improvement*. Para cada busca, registra a data, a base, os termos e o número de resultados, e faz a triagem de títulos e resumos com critérios escritos. Os estudos precisam relatar um desfecho medido antes e depois de uma mudança de governança. Ele encontra muitos arcabouços e descrições de casos, mas poucos estudos que medem desfechos, o que coincide com a lacuna relatada por outros revisores. A literatura cinzenta é registrada à parte.

### 1.4 Registrando as decisões

Cada inclusão e exclusão é registrada com um motivo, como ausência de medida de desfecho ou tema fora da governança. A Dra. Solberg confere uma décima parte aleatória das decisões e concorda com todas, menos uma, que os dois discutem e resolvem. Tomás aprende que uma busca transparente permite aos leitores julgar se alguma evidência ficou de fora e lhe permite atualizar a revisão mais tarde sem recomeçar. Ele guarda o registro junto com os materiais da dissertação, para que a banca veja como a base de evidências foi montada, em vez de ter de confiar nela.

### Exemplo resolvido

Tomás formula uma pergunta sobre curadoria com desfecho, intervenção, comparação e período, pesquisa com termos fixos, faz a triagem com critérios escritos e registra cada decisão, com conferência da orientadora.

> **Caso sintético.** Kestrel, Arden e todas as pessoas são sintéticos; o DAMA-DMBOK2 é real.

### Erros e limites

Os termos de busca determinam o que é encontrado; teste termos alternativos antes de fechar a busca.

### Exercícios

- **EX001 — Problema do parceiro.** Que problema a Prefeitura do Condado de Arden enfrenta? *Rubrica:* 3 = endereços duplicados em cinco departamentos, causando erros;; 2 = menciona duplicatas;; 1 = vago;; 0 = nenhuma.
- **EX002 — Medida de desfecho.** Qual é a medida de desfecho de Tomás? *Rubrica:* 3 = dias entre a notificação do erro e a correção;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX003 — Grupo de comparação.** Qual é a comparação na pergunta dele? *Rubrica:* 3 = departamentos sem curadores;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX004 — Definição de curadoria.** Como o DAMA-DMBOK2 descreve a curadoria? *Rubrica:* 3 = responsabilização pelos dados em nome de outros;; 2 = menciona responsabilização;; 1 = vago;; 0 = nenhuma.
- **EX005 — Critério de inclusão.** O que os estudos incluídos precisam relatar? *Rubrica:* 3 = um desfecho medido antes e depois de uma mudança de governança;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX006 — Conferência da orientadora.** Que parcela das decisões a Dra. Solberg conferiu? *Rubrica:* 3 = uma décima parte aleatória;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX007 — Lacuna na literatura.** O que a busca mostrou estar faltando? *Rubrica:* 3 = estudos que medem desfechos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Governança de dados: seminário avançado

### Objetivos de aprendizagem

Você vai (1) comparar modelos de governança de forma crítica; (2) relacionar a curadoria com direitos de decisão e normas; (3) apresentar um argumento em seminário.

### 2.1 Modelos de governança

No seminário avançado, Tomás compara três visões. O DAMA-DMBOK2 apresenta a governança como uma função que define políticas, papéis e padrões para as demais áreas de gestão de dados. Khatri e Brown organizam a governança em domínios de decisão — entre eles princípios de dados, qualidade, metadados, acesso e ciclo de vida — e perguntam quem detém os direitos de decisão em cada um. A ISO/IEC 38505-1 atribui a responsabilização ao órgão de governança, que dirige, avalia e monitora o uso dos dados. Ele observa que as três visões enfatizam níveis diferentes: a função, as decisões e a responsabilização do conselho. Cada visão acrescenta algo.

### 2.2 Onde entram os curadores

Tomás posiciona a curadoria em cada visão. Nos termos da DAMA, os curadores executam a governança no trabalho diário, por exemplo definindo padrões de endereço e resolvendo conflitos. Nos termos de Khatri e Brown, os curadores podem deter direitos de decisão sobre a qualidade em um domínio, ou apenas direitos de contribuição, enquanto um servidor da prefeitura decide. Nos termos da ISO, os curadores atuam sob a direção do órgão de governança e prestam contas a ele. Ele argumenta que o efeito do piloto dependerá de quais direitos de decisão os curadores realmente recebem, e não apenas do nome do cargo.

### 2.3 Normas de qualidade

O seminário também trata de normas de qualidade. A ISO 8000-1 apresenta uma visão geral da série ISO 8000 e de seus princípios, entre eles o de que a qualidade é julgada em relação a requisitos declarados. As dimensões de Wang e Strong mostram que os usuários se importam com acessibilidade e atualidade, e não só com acurácia. Para Arden, atualidade significa a rapidez com que um endereço corrigido chega a todos os departamentos. Tomás argumenta que seu desfecho, os dias até a correção, é uma medida de atualidade ancorada em requisitos que os usuários de fato declaram, como a expectativa dos moradores de que o lixo seja recolhido no novo endereço em até um mês.

### 2.4 O argumento do seminário

Tomás apresenta seu argumento: a curadoria só vai encurtar os tempos de correção onde os curadores tiverem direitos de decisão sobre padrões de endereço comuns aos departamentos e um canal para propagar as correções. Os colegas contestam que a cultura da prefeitura pode pesar mais do que a estrutura. Ele aceita o ponto e acrescenta a cultura como explicação concorrente, a ser examinada depois. A Dra. Solberg elogia a passagem da descrição de modelos para a derivação de uma condição testável, que transforma uma discussão de seminário em uma hipótese de pesquisa que o piloto pode confirmar ou refutar. A cultura entra no desenho.

### Exemplo resolvido

Tomás compara DAMA, Khatri e Brown e a ISO/IEC 38505-1, relaciona os curadores aos direitos de decisão, enquadra o tempo de correção como medida de atualidade e deriva uma condição testável para que a curadoria funcione.

> **Caso sintético.** O seminário é sintético; DAMA-DMBOK2, Khatri e Brown (2010), ISO/IEC 38505-1:2017, ISO 8000-1:2022 e Wang e Strong (1996) são reais.

### Erros e limites

Modelos descrevem ideais; prefeituras reais os misturam.

### Exercícios

- **EX008 — Três níveis.** Que níveis as três visões enfatizam? *Rubrica:* 3 = função, decisões e responsabilização do conselho;; 2 = todos;; 1 = um;; 0 = nenhuma.
- **EX009 — Verbos da ISO.** O que faz o órgão de governança segundo a ISO/IEC 38505-1? *Rubrica:* 3 = dirige, avalia e monitora;; 2 = todos;; 1 = um;; 0 = nenhuma.
- **EX010 — O cargo não basta.** Por que o cargo de curador pode não ter efeito? *Rubrica:* 3 = os curadores podem não ter direitos de decisão;; 2 = menciona direitos;; 1 = vago;; 0 = nenhuma.
- **EX011 — Atualidade.** Que dimensão de qualidade são os dias até a correção? *Rubrica:* 3 = atualidade;; 2 = parcialmente correto;; 1 = acurácia;; 0 = nenhuma.
- **EX012 — Princípio da ISO 8000.** Em relação a que a qualidade é julgada na ISO 8000? *Rubrica:* 3 = requisitos declarados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX013 — Contestação dos colegas.** Que explicação concorrente os colegas levantaram? *Rubrica:* 3 = a cultura da prefeitura;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX014 — Condição testável.** Que condição Tomás derivou? *Rubrica:* 3 = curadores precisam de direitos de decisão e de um canal de propagação;; 2 = ambos;; 1 = um;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Desenho do estudo, ética e reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) desenhar uma avaliação quase experimental; (2) tratar da ética na pesquisa em ambiente de trabalho; (3) planejar uma análise reproduzível.

### 3.1 Escolhendo o desenho

A prefeitura não vai sortear quais departamentos recebem curadores; ela já escolheu tributação imobiliária e coleta de lixo. Por isso, Tomás usa um desenho de diferenças em diferenças. Ele compara a variação dos tempos de correção nos dois departamentos com curadores com a variação nos três departamentos de comparação no mesmo período. O desenho elimina diferenças estáveis entre departamentos e tendências comuns, como uma atualização de software em toda a prefeitura, desde que os departamentos tivessem seguido tendências paralelas sem o piloto. Ele não elimina mudanças que afetam apenas um grupo, como a chegada de um novo gerente na tributação.

### 3.2 Verificando as suposições

Tomás examina doze meses de tempos de correção anteriores ao piloto em uma réplica sintética construída a partir dos números agregados que a prefeitura publica. As tendências dos dois grupos parecem semelhantes, o que apoia a suposição de tendências paralelas, embora não a prove. Ele também lista ameaças: os departamentos com curadores podem receber atenção extra, a rotatividade de pessoal pode ser diferente e uma mudança na forma de notificar pode alterar quais erros são registrados. Ele planeja verificar cada ameaça com registros da prefeitura e entrevistas, em vez de simplesmente descartá-la. Cada ameaça ganha uma verificação.

### 3.3 Ética

O estudo envolve servidores da prefeitura, cujo desempenho pode parecer estar sendo julgado. O protocolo ético de Tomás declara que ele analisa apenas tempos no nível do departamento, nunca o desempenho individual, e que os entrevistados são anônimos e podem desistir. Os endereços dos moradores não são usados; a réplica contém endereços sintéticos com os mesmos padrões de erro. O encarregado de proteção de dados da prefeitura confirma que nenhum dado pessoal sai do órgão. A Dra. Solberg observa que a pesquisa em ambiente de trabalho exige cuidado especial, porque as diferenças de poder tornam difícil recusar. A participação é voluntária.

### 3.4 Análise reproduzível

Tomás escreve o plano de análise antes de coletar dados: o estimador, o método do intervalo de confiança, o número de reamostragens do *bootstrap* e o limiar de relevância prática, que ele fixa em cinco dias. Todo o código usa a biblioteca padrão do Python, sementes aleatórias fixas e controle de versão. Ele registra o plano com data, para não poder mudar depois o desfecho ou o limiar ao ver os resultados. A reprodutibilidade, observa ele, é especialmente importante em estudos de governança que prefeituras podem usar para justificar gastos com novos cargos.

### Exemplo resolvido

Tomás escolhe diferenças em diferenças, verifica as tendências anteriores ao piloto em uma réplica sintética, lista ameaças, limita a análise ao nível do departamento por razões éticas e fixa um plano de análise com limiar de relevância de cinco dias.

> **Caso sintético.** O desenho é sintético.

### Erros e limites

Tendências paralelas podem valer antes e falhar depois; fique atento a novos eventos.

### Exercícios

- **EX015 — Por que não sortear.** Por que Tomás não pode sortear? *Rubrica:* 3 = a prefeitura escolheu os departamentos do piloto;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX016 — Nome do desenho.** Que desenho Tomás usa? *Rubrica:* 3 = diferenças em diferenças;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.
- **EX017 — Suposição-chave.** De que suposição o desenho depende? *Rubrica:* 3 = tendências paralelas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX018 — Exemplo de ameaça.** Cite uma ameaça ao desenho. *Rubrica:* 3 = atenção extra, diferença de rotatividade, mudança na notificação;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX019 — Nível ético.** Em que nível o desempenho é analisado? *Rubrica:* 3 = somente no nível do departamento;; 2 = parcialmente correto;; 1 = individual;; 0 = nenhuma.
- **EX020 — Limiar de relevância.** Que limiar de relevância prática foi fixado? *Rubrica:* 3 = cinco dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Governança de dados: explicações concorrentes

### Objetivos de aprendizagem

Você vai (1) listar explicações rivais para um efeito esperado; (2) desenhar verificações para cada uma; (3) decidir que evidências enfraqueceriam a hipótese principal.

### 4.1 Por que as rivais importam

Tomás espera que os departamentos com curadores corrijam erros mais depressa. A Dra. Solberg pergunta o que mais poderia produzir esse resultado. Ele lista rivais: uma nova ferramenta de consulta de endereços introduzida ao mesmo tempo; uma queda no número de erros notificados, que daria aos servidores mais tempo por erro; a transferência de servidores mais experientes para os departamentos com curadores; e um efeito Hawthorne, em que as pessoas trabalham mais porque sabem que estão sendo observadas. Shadish, Cook e Campbell descrevem essas ameaças à validade interna, e nomeá-las com antecedência impede interpretações convenientes depois.

### 4.2 Desenhando verificações

Para cada rival, Tomás desenha uma verificação. A ferramenta de consulta foi implantada nos cinco departamentos, então afeta os dois grupos e é eliminada pelo desenho, mas ele confirma as datas de implantação. O volume de erros é medido por departamento e por mês. A experiência dos servidores é verificada com dados anonimizados de tempo de casa, fornecidos pelo setor de recursos humanos no nível do departamento. O efeito Hawthorne é mais difícil de testar, então ele planeja entrevistas perguntando como o trabalho mudou e compara os dois primeiros meses com os seguintes, esperando que qualquer efeito de novidade se dissipe.

### 4.3 A explicação cultural

Os colegas haviam sugerido que a cultura pesa mais do que a curadoria. Tomás operacionaliza a cultura de forma modesta: se os departamentos já compartilhavam correções informalmente antes do piloto. Entrevistas e resumos escritos dos gerentes indicam que a coleta de lixo já telefonava para a tributação para avisar de mudanças, enquanto as bibliotecas não faziam isso. Ele percebe que isso poderia inflar a melhora aparente da coleta de lixo, se o compartilhamento informal aumentasse. Acrescenta então uma comparação entre os dois departamentos do grupo com curadores, para ver se ambos melhoram de forma parecida ou só o que já colaborava. Os dois são comparados.

### 4.4 Evidências que enfraqueceriam a hipótese

Tomás anota quais resultados contariam contra a curadoria: melhora concentrada em meses de baixo volume de erros, melhora igual nos dois grupos ou melhora apenas no departamento que já compartilhava informalmente. Ele se compromete a relatar esses resultados com honestidade. A Dra. Solberg explica que uma hipótese só é útil se alguma evidência puder contradizê-la, e que registrar essas condições protege o pesquisador da tentação de justificar achados incômodos depois de meses investidos no projeto. Essas condições entram no plano de análise.

### Exemplo resolvido

Tomás lista quatro rivais, desenha verificações para cada uma, operacionaliza a cultura como compartilhamento informal prévio e declara de antemão quais resultados enfraqueceriam a hipótese da curadoria.

> **Caso sintético.** As rivais e as verificações são sintéticas; Shadish, Cook e Campbell (2002) é uma fonte real sobre ameaças à validade.

### Erros e limites

Algumas rivais não podem ser totalmente descartadas; relate-as como limitações.

### Exercícios

- **EX021 — Quatro rivais.** Cite duas explicações rivais. *Rubrica:* 3 = nova ferramenta, menor volume de erros, servidores experientes, efeito Hawthorne;; 2 = duas;; 1 = uma;; 0 = nenhuma.
- **EX022 — Rival da ferramenta.** Por que o desenho elimina a rival da ferramenta de consulta? *Rubrica:* 3 = foi implantada em todos os departamentos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX023 — Verificação Hawthorne.** Como Tomás vai verificar o efeito Hawthorne? *Rubrica:* 3 = entrevistas e comparação dos primeiros meses com os seguintes;; 2 = menciona meses;; 1 = vago;; 0 = nenhuma.
- **EX024 — Medida de cultura.** Como a cultura é operacionalizada? *Rubrica:* 3 = compartilhamento informal prévio de correções;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX025 — Evidência contrária.** Cite um resultado que enfraqueceria a hipótese. *Rubrica:* 3 = melhora só em meses de baixo volume, igual nos dois grupos ou só onde havia compartilhamento;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX026 — Falseabilidade.** Por que registrar as condições contrárias com antecedência? *Rubrica:* 3 = para não justificar resultados incômodos depois;; 2 = menciona viés;; 1 = vago;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Projeto e piloto

### Objetivos de aprendizagem

Você vai (1) testar em piloto a medição de duplicatas e de tempos de correção; (2) normalizar dados de endereço; (3) refinar o projeto com as lições do piloto.

### 5.1 Finalidade do piloto

Antes da coleta principal, Tomás testa suas medições em uma réplica sintética dos cadastros de endereços. Ele quer saber se as duplicatas podem ser contadas de forma confiável, se os tempos de correção podem ser extraídos dos registros de chamados e quanto tempo leva cada etapa. Um piloto não serve para responder à pergunta de pesquisa; ele testa se os métodos funcionam. A Dra. Solberg lembra que problemas encontrados em um piloto custam pouco, enquanto os mesmos problemas encontrados durante o estudo principal podem custar meses.

### 5.2 O laboratório de duplicatas

O laboratório do piloto gera 3.305 registros sintéticos de endereço, nos quais um segundo departamento às vezes digita o mesmo endereço com abreviações, espaços extras e letras maiúsculas diferentes. A correspondência exata não encontra nenhuma duplicata, porque não há duas cadeias de texto idênticas. Depois da normalização — que converte o texto para minúsculas, expande abreviações como St e Rd e reduz espaços repetidos —, aparecem 384 duplicatas, 11,6% dos registros. O resultado mostra que qualquer medida de duplicidade depende fortemente das regras de normalização escolhidas, que são, elas mesmas, uma decisão de governança. As regras de abreviação decidem o que conta como o mesmo endereço.

### 5.3 Tempos de correção

Os registros de chamados indicam quando um erro foi notificado e quando o chamado foi encerrado, mas o encerramento nem sempre significa que o endereço mudou em todos os sistemas. Na réplica, alguns chamados são encerrados quando o departamento que notificou corrige a própria cópia, enquanto os outros departamentos continuam com o dado errado. Tomás redefine o desfecho como os dias até que o endereço corrigido apareça nos cinco sistemas, o que corresponde à experiência dos moradores. A ênfase da ISO 8000-1 em requisitos o ajuda a justificar a mudança: o requisito é um endereço correto em toda parte, não um chamado encerrado.

### 5.4 Refinando o projeto

Com base no piloto, Tomás atualiza o projeto: a contagem de duplicatas usará regras de normalização documentadas e acordadas com os curadores, o tempo de correção será medido até o último sistema atualizado e a extração de dados levará duas semanas, e não uma. Ele registra as mudanças e seus motivos no diário de decisões antes de coletar os dados reais de desfecho, para que as mudanças não possam ser acusadas de perseguir resultados. A Dra. Solberg aprova e observa que o piloto já produziu um achado sobre como as definições moldam a qualidade medida.

### Laboratório — Endereços duplicados antes e depois da normalização


```python
"""Find duplicate address records before and after normalisation in a synthetic council register (stdlib only)."""
import random, re, collections
random.seed(12)
streets = ["High Street", "Mill Lane", "Church Road", "Station Road", "Park Avenue", "Kings Way"]
base = [(random.randint(1, 120), random.choice(streets), f"AR{random.randint(1,9)} {random.randint(1,9)}QX") for _ in range(3000)]
base = list(dict.fromkeys(base))
recs = []
for n, s, p in base:
    recs.append(f"{n} {s}, {p}")
    if random.random() < 0.12:   # a second department keys the same address differently
        v = s.replace("Street", "St").replace("Road", "Rd").replace("Avenue", "Ave")
        recs.append(f"{n}  {v.upper()},{p.lower()}")
def norm(a):
    a = a.lower().replace(",", " ")
    for k, v in {" st ": " street ", " rd ": " road ", " ave ": " avenue "}.items():
        a = (" " + a + " ").replace(k, v).strip()
    return re.sub(r"\s+", " ", a)
exact = len(recs) - len(set(recs))
normd = len(recs) - len({norm(r) for r in recs})
print(f"records {len(recs)}; exact duplicates {exact}; duplicates after normalisation {normd} ({100*normd/len(recs):.1f}%)")
```

Execute com `python3 lab_dupes.py`. Saída verificada:

```text
records 3305; exact duplicates 0; duplicates after normalisation 384 (11.6%)
```

### Exemplo resolvido

Tomás não encontra duplicatas exatas, mas encontra 384 (11,6%) depois da normalização entre 3.305 registros sintéticos, redefine o tempo de correção até o último sistema atualizado e registra as mudanças no projeto antes da coleta principal.

> **Caso sintético.** Os registros são sintéticos; a ISO 8000-1:2022 é real.

### Erros e limites

Uma normalização agressiva pode fundir endereços diferentes; confira uma amostra manualmente.

### Exercícios

- **EX027 — Objetivo do piloto.** O que um piloto deve testar? *Rubrica:* 3 = se os métodos funcionam;; 2 = parcialmente correto;; 1 = responder à pergunta;; 0 = nenhuma.
- **EX028 — Correspondências exatas.** Quantas duplicatas exatas foram encontradas? *Rubrica:* 3 = nenhuma;; 2 = hesitante (poucas ou nenhuma);; 1 = errado;; 0 = sem resposta.
- **EX029 — Duplicatas normalizadas.** Quantas duplicatas apareceram depois da normalização? *Rubrica:* 3 = 384, 11,6%;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX030 — Etapas da normalização.** Cite duas etapas da normalização. *Rubrica:* 3 = minúsculas, expansão de abreviações, redução de espaços;; 2 = duas;; 1 = uma;; 0 = nenhuma.
- **EX031 — Novo desfecho.** Como o tempo de correção foi redefinido? *Rubrica:* 3 = dias até ficar correto nos cinco sistemas;; 2 = parcialmente correto;; 1 = encerramento do chamado;; 0 = nenhuma.
- **EX032 — Mudanças registradas.** Quando as mudanças no projeto foram registradas? *Rubrica:* 3 = antes de coletar os dados reais de desfecho;; 2 = parcialmente correto;; 1 = depois;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Coleta e análise de dados

### Objetivos de aprendizagem

Você vai (1) coletar dados de desfecho no nível do departamento; (2) estimar um efeito de diferenças em diferenças com intervalo por *bootstrap*; (3) verificar as explicações rivais.

### 6.1 Coletando os dados

Tomás extrai os tempos de correção de seis meses antes e seis meses depois do piloto, 120 correções por grupo em cada período, usando a definição do piloto. A extração segue um script escrito e revisado pela equipe de dados da prefeitura, que o executa dentro dos sistemas do órgão e devolve apenas tabelas no nível do departamento. A análise deste livro reproduz essas tabelas com dados sintéticos gerados a partir dos mesmos números agregados, para que qualquer leitor possa executá-la sem acesso aos sistemas da prefeitura nem aos dados dos moradores. Nada identificável sai do órgão.

### 6.2 A estimativa

O laboratório mostra o tempo médio de correção nos departamentos com curadores caindo de 24,1 para 14,8 dias, enquanto os departamentos de comparação passam de 21,9 para 19,6 dias. A estimativa de diferenças em diferenças é de -7,0 dias, com intervalo de 95% por *bootstrap* de -9,1 a -4,8 dias, com base em 2.000 reamostragens. Todo o intervalo fica além do limiar de cinco dias fixado de antemão, de modo que o efeito do piloto é estatisticamente claro e relevante na prática, segundo o critério que Tomás definiu antes de ver os dados. Os departamentos de comparação também melhoraram um pouco, cerca de dois dias, talvez por causa da ferramenta de consulta comum, e o desenho subtrai essa mudança comum do ganho dos departamentos com curadores.

### 6.3 Verificando as rivais

Os volumes de erros são estáveis nos dois grupos, então uma carga de trabalho menor não explica a mudança. Os dados de tempo de casa não mostram deslocamento de servidores experientes. Os resultados mensais mostram melhora ao longo dos seis meses, sem se dissipar, o que pesa contra um puro efeito de novidade. No grupo com curadores, os dois departamentos melhoram, inclusive a tributação, que não tinha compartilhamento informal prévio, o que enfraquece a rival cultural. Tomás relata cada verificação em uma tabela ao lado da estimativa principal, para que os leitores julguem até que ponto as rivais foram tratadas.

### 6.4 O que a estimativa significa

Tomás interpreta o resultado com cuidado: nesta reprodução sintética do piloto de uma prefeitura, nomear curadores com direitos de decisão sobre padrões de endereço esteve associado a correções que chegaram a todos os sistemas cerca de uma semana antes. As entrevistas sugerem o mecanismo: os curadores acordaram um padrão único de endereço e uma rotina semanal de propagação. Ele evita afirmar que a curadoria funciona em qualquer lugar. A Dra. Solberg observa que essa redação cuidadosa respeita tanto a evidência quanto os limites de um piloto com dois departamentos. Outras prefeituras podem diferir em pessoal, sistemas e número de departamentos que mantêm endereços.

### Laboratório — Diferenças em diferenças dos tempos de correção com intervalo por bootstrap


```python
"""Difference-in-differences of days to fix address errors, stewarded vs comparison departments, with bootstrap CI (stdlib only)."""
import random, statistics as st
random.seed(30)
def sample(mu, n): return [max(1, random.gauss(mu, 6)) for _ in range(n)]
treat_pre, treat_post = sample(24, 120), sample(15, 120)
comp_pre, comp_post = sample(22, 120), sample(19, 120)
def did(a, b, c, d): return (st.mean(b) - st.mean(a)) - (st.mean(d) - st.mean(c))
est = did(treat_pre, treat_post, comp_pre, comp_post)
boots = sorted(did(*(random.choices(x, k=len(x)) for x in (treat_pre, treat_post, comp_pre, comp_post))) for _ in range(2000))
print(f"mean days: stewarded {st.mean(treat_pre):.1f} -> {st.mean(treat_post):.1f}; comparison {st.mean(comp_pre):.1f} -> {st.mean(comp_post):.1f}")
print(f"difference-in-differences {est:.1f} days (95% CI {boots[50]:.1f} to {boots[1949]:.1f})")
```

Execute com `python3 lab_did.py`. Saída verificada:

```text
mean days: stewarded 24.1 -> 14.8; comparison 21.9 -> 19.6
difference-in-differences -7.0 days (95% CI -9.1 to -4.8)
```

### Exemplo resolvido

Tomás estima uma diferença em diferenças de -7,0 dias (IC 95% de -9,1 a -4,8), além do limiar de cinco dias, verifica as rivais de volume, tempo de casa, novidade e cultura e identifica como mecanismo um padrão único e uma propagação semanal.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Um intervalo por *bootstrap* reflete a variação amostral, não o viés do desenho.

### Exercícios

- **EX033 — Mudança com curadores.** Como mudaram os tempos de correção com curadores? *Rubrica:* 3 = de 24,1 para 14,8 dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX034 — Estimativa DiD.** Qual foi a estimativa de diferenças em diferenças? *Rubrica:* 3 = -7,0 dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX035 — Intervalo.** Qual foi o intervalo de 95%? *Rubrica:* 3 = de -9,1 a -4,8 dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX036 — Limiar atingido.** O intervalo ultrapassa o limiar de cinco dias? *Rubrica:* 3 = sim, inteiramente;; 2 = parcialmente correto;; 1 = não;; 0 = nenhuma.
- **EX037 — Rival cultural.** Por que a rival cultural fica enfraquecida? *Rubrica:* 3 = a tributação melhorou sem compartilhamento prévio;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX038 — Mecanismo.** Que mecanismo as entrevistas sugeriram? *Rubrica:* 3 = padrão único de endereço e propagação semanal;; 2 = ambos;; 1 = um;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Redação da dissertação e limitações

### Objetivos de aprendizagem

Você vai (1) estruturar uma dissertação de mestrado; (2) escrever limitações que informem o leitor; (3) separar achados de recomendações.

### 7.1 Estrutura

Tomás organiza a dissertação em torno da pergunta: introdução e pergunta, literatura e modelos de governança, desenho e ética, achados do piloto sobre medição, resultados principais, verificação das rivais, discussão, limitações e recomendações. Ele escreve o resumo por último, informando o efeito, o intervalo, o desenho e a principal limitação em quatro frases. A Dra. Solberg o aconselha a dar ao achado do piloto sobre normalização uma seção própria, porque é uma contribuição separada: as taxas de duplicidade medidas dependem de regras, de modo que as organizações precisam governar suas regras de qualidade. Cada capítulo responde a uma parte da pergunta.

### 7.2 Limitações

A seção de limitações de Tomás aponta cinco questões: apenas dois departamentos tratados, seleção não aleatória, uma reprodução sintética dos números em vez da análise direta de todos os registros, um acompanhamento de seis meses que não mostra se os ganhos se mantêm e possíveis diferenças não medidas, como a qualidade da gerência. Para cada uma, ele explica a direção provável do viés e o que trabalhos futuros poderiam fazer a respeito. Ele evita afirmações genéricas como mais pesquisas são necessárias, que não dizem ao leitor qual pesquisa nem por quê. A maioria dessas limitações enviesaria a estimativa para cima.

### 7.3 Achados versus recomendações

Tomás separa o que a evidência mostra do que ele recomenda. O achado é o efeito estimado e seu mecanismo nas condições do piloto. As recomendações são estender a curadoria aos outros três departamentos com os mesmos direitos de decisão, continuar medindo o tempo de correção até o último sistema e publicar as regras de normalização de endereços. Ele sinaliza as recomendações como julgamentos informados pela evidência, para que leitores que discordem de sua ponderação ainda possam usar os achados de forma independente. Julgamento e evidência ficam claramente identificados.

### 7.4 Escrevendo para dois públicos

A dissertação atende à banca e à prefeitura. Tomás escreve um resumo de duas páginas para os servidores, com o resultado principal em linguagem simples, um gráfico dos tempos de correção e as recomendações. A dissertação completa mantém o detalhe técnico para a banca. Ele confere se as duas versões concordam nos números e nas afirmações. A Dra. Solberg observa que a inconsistência entre a versão técnica e o resumo é uma forma comum de a pesquisa perder credibilidade quando chega a tomadores de decisão que comparam as duas. Ambas as versões citam a mesma tabela de resultados.

### Exemplo resolvido

Tomás estrutura a dissertação, aponta cinco limitações específicas com a direção do viés, separa achados de recomendações e escreve um resumo de duas páginas coerente para a prefeitura.

> **Caso sintético.** A dissertação é sintética.

### Erros e limites

Resumos tendem a perder ressalvas; mantenha a principal limitação no resumo.

### Exercícios

- **EX039 — Contribuição separada.** Que contribuição separada ganha seção própria? *Rubrica:* 3 = taxas de duplicidade dependem das regras de normalização;; 2 = menciona regras;; 1 = vago;; 0 = nenhuma.
- **EX040 — Número de limitações.** Quantas limitações Tomás aponta? *Rubrica:* 3 = cinco;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX041 — Limite do acompanhamento.** Por que seis meses são uma limitação? *Rubrica:* 3 = não mostram se os ganhos se mantêm;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX042 — Frase genérica.** Que frase genérica Tomás evita? *Rubrica:* 3 = mais pesquisas são necessárias;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX043 — Exemplo de recomendação.** Cite uma recomendação. *Rubrica:* 3 = estender a curadoria, medir até o último sistema, publicar as regras;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX044 — Consistência.** Por que o resumo e a dissertação precisam concordar? *Rubrica:* 3 = a inconsistência prejudica a credibilidade;; 2 = menciona credibilidade;; 1 = vago;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Revisão independente e defesa

### Objetivos de aprendizagem

Você vai (1) obter uma revisão independente da análise; (2) defender uma dissertação de mestrado; (3) entregar os achados à organização parceira.

### 8.1 Revisão independente

Antes do depósito, uma estatística de outro departamento do Kestrel revisa o código e os dados de Tomás sem a ajuda dele. Ela executa novamente a análise a partir do arquivo e obtém a mesma estimativa e o mesmo intervalo. Questiona se 2.000 reamostragens são suficientes; Tomás roda com 10.000, e o intervalo muda menos de um décimo de dia. Ela também pede um teste placebo, usando um período anterior ao piloto como se fosse o piloto, que não mostra efeito algum e assim apoia o desenho. O resultado do placebo é relatado em um apêndice.

### 8.2 A defesa

Na defesa, a banca pergunta por que a prefeitura deveria confiar em um resultado obtido com dois departamentos. Tomás responde que o resultado é consistente mês a mês, resiste às verificações relatadas e tem um mecanismo plausível, mas que a extensão deve ser avaliada por sua vez. Um examinador pergunta sobre a reprodução sintética; ele explica que a equipe de dados da prefeitura fez a extração internamente e que os dados sintéticos batem com os resumos que ela publicou. A banca o aprova e elogia o tratamento das explicações rivais. Seguem-se pequenos ajustes.

### 8.3 A entrega

Tomás apresenta os achados ao comitê de governança de dados de Arden. O comitê decide estender a curadoria às bibliotecas e às licenças de estacionamento, enquanto a assistência social aguarda uma revisão de suas obrigações legais. Adota as regras de normalização como padrão da prefeitura e pede à equipe de dados que continue a relatar o tempo de correção até o último sistema. Tomás entrega os scripts de análise e um guia para que os servidores possam refazer a avaliação da extensão sem ele. O guia inclui o teste placebo e as regras de normalização.

### 8.4 Reflexão

Tomás reflete que a parte mais útil do seu trabalho talvez sejam as definições de medida, que a prefeitura continuará usando, e não a estimativa isolada. Observa que a pesquisa em governança precisa respeitar as pessoas cujo trabalho é estudado: os curadores estavam ansiosos com a avaliação, e os relatórios no nível do departamento preservaram a confiança deles. A Dra. Solberg encerra a orientação lembrando que boas avaliações facilitam que as organizações aprendam tanto com o sucesso quanto com o fracasso. Mais tarde, Tomás passa a integrar a equipe de dados de Arden.

### Exemplo resolvido

Uma estatística independente reproduz a estimativa, verifica o número de reamostragens e roda um teste placebo; Tomás é aprovado na defesa, e a prefeitura estende a curadoria e adota suas definições.

> **Caso sintético.** A revisão e o comitê são sintéticos.

### Erros e limites

Extensões a novos departamentos podem não reproduzir os efeitos do piloto; avalie-as.

### Exercícios

- **EX045 — Verificação da revisora.** O que a revisora mudou no *bootstrap*? *Rubrica:* 3 = reamostragens de 2.000 para 10.000;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX046 — Placebo.** O que o teste placebo mostrou? *Rubrica:* 3 = nenhum efeito em um período anterior ao piloto;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX047 — Preocupação da banca.** O que a banca questionou? *Rubrica:* 3 = confiar em um resultado de dois departamentos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX048 — Decisão do comitê.** Para quais departamentos a curadoria se estende em seguida? *Rubrica:* 3 = bibliotecas e estacionamento;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX049 — Assistência social.** Por que a assistência social aguarda? *Rubrica:* 3 = revisão de suas obrigações legais;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX050 — Valor duradouro.** Qual pode ser a parte mais útil do trabalho de Tomás? *Rubrica:* 3 = as definições de medida;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Tomás Ferreira, a Dra. Ingrid Solberg, o Instituto de Tecnologia Kestrel, a Prefeitura do Condado de Arden e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Cinco departamentos mantêm suas próprias cópias de endereços, o que gera duplicatas e correções lentas.

**EX002.** Os dias entre a notificação de um erro e sua correção.

**EX003.** Os departamentos sem curadores de dados.

**EX004.** A responsabilização pelos dados em nome de outras pessoas.

**EX005.** Um desfecho medido antes e depois de uma mudança de governança.

**EX006.** Uma décima parte aleatória.

**EX007.** Estudos que medem os desfechos de mudanças de governança.

**EX008.** Função (DAMA), decisões (Khatri e Brown) e responsabilização do conselho (ISO).

**EX009.** Dirige, avalia e monitora o uso dos dados.

**EX010.** Sem direitos de decisão, o cargo muda pouco.

**EX011.** Atualidade.

**EX012.** Em relação a requisitos declarados.

**EX013.** A cultura da prefeitura, e não a estrutura.

**EX014.** A curadoria funciona onde os curadores detêm direitos de decisão e podem propagar correções.

**EX015.** A prefeitura já tinha escolhido os departamentos com curadores.

**EX016.** Diferenças em diferenças.

**EX017.** Tendências paralelas na ausência do piloto.

**EX018.** Departamentos com curadores recebendo atenção extra.

**EX019.** Somente no nível do departamento, nunca individual.

**EX020.** Cinco dias.

**EX021.** Uma nova ferramenta de consulta e um volume menor de erros.

**EX022.** Ela afetou igualmente os dois grupos.

**EX023.** Entrevistas e a comparação dos dois primeiros meses com os seguintes.

**EX024.** Se os departamentos já compartilhavam correções informalmente.

**EX025.** Melhora igual nos dois grupos.

**EX026.** Para que achados incômodos não possam ser justificados depois.

**EX027.** Se os métodos de medição funcionam, não a pergunta de pesquisa.

**EX028.** Nenhuma.

**EX029.** 384 (11,6%).

**EX030.** Converter para minúsculas e expandir abreviações.

**EX031.** Dias até o endereço corrigido aparecer nos cinco sistemas.

**EX032.** Antes da coleta dos dados principais de desfecho.

**EX033.** De 24,1 para 14,8 dias.

**EX034.** -7,0 dias.

**EX035.** De -9,1 a -4,8 dias.

**EX036.** Sim, todo o intervalo fica além de cinco dias.

**EX037.** A tributação também melhorou, apesar de não ter compartilhamento informal prévio.

**EX038.** Um padrão único de endereço e uma rotina semanal de propagação.

**EX039.** O achado de que as taxas de duplicidade medidas dependem das regras de normalização.

**EX040.** Cinco.

**EX041.** Não mostra se os ganhos se mantêm.

**EX042.** Mais pesquisas são necessárias.

**EX043.** Estender a curadoria aos outros três departamentos.

**EX044.** Inconsistências custam credibilidade diante de tomadores de decisão.

**EX045.** Ela pediu 10.000 reamostragens em vez de 2.000.

**EX046.** Nenhum efeito quando um período anterior ao piloto foi tratado como piloto.

**EX047.** Se dois departamentos justificam confiança no resultado.

**EX048.** Bibliotecas e estacionamento.

**EX049.** Suas obrigações legais precisam ser revistas antes.

**EX050.** As definições de medida que a prefeitura continua usando.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. As referências são mantidas idênticas às da edição em inglês; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- ISO. (2022). *ISO 8000-1:2022 Data quality — Part 1: Overview*. International Organization for Standardization. <https://www.iso.org/standard/81745.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- Khatri, V., & Brown, C. V. (2010). Designing data governance. *Communications of the ACM, 53*(1), 148–152. https://doi.org/10.1145/1629175.1629210
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.
