# Governança de Dados: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 026, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais em atividade que receberam a responsabilidade pela governança de dados em uma organização pequena.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios normalizam e-mails sintéticos de doadores para revelar duplicatas e classificam registros sintéticos de consentimento para marketing conforme mostrem ou não quando o consentimento foi dado. Normas e leis são citadas pela edição e parafraseadas; nada aqui é aconselhamento jurídico. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma profissional desde o mapeamento dos dados e dos riscos de uma pequena organização beneficente, passando por papéis, inventário, política, qualidade dos dados, consentimento, segurança, fornecedores, retenção e direitos, até o tratamento de incidentes, os relatórios ao conselho e um plano de um ano. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Grace Mwangi** | Gerente de operações e participante do curso | Inventada |
| **Sr. Tomasz Nowak** | Tutor do curso | Inventado |
| **Kingsford Professional Academy** | Academia fictícia | Inventada |
| **Northbank Food Bank Network** | Organização beneficente fictícia, com seis bancos de alimentos, cerca de 400 voluntários e 4.000 doadores | Inventada |

### Fontes principais

DAMA-DMBOK2 (2017); GDPR; LGPD. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — O papel e a organização

### Objetivos de aprendizagem

Você vai (1) descrever o curso profissional e seu caso; (2) delinear os dados de uma pequena organização beneficente; (3) definir metas para quem lidera a governança.

### 1.1 A participante

Grace Mwangi é a nova gerente de operações da Northbank Food Bank Network, uma organização beneficente fictícia que mantém seis bancos de alimentos, com cerca de quatrocentos voluntários, quatro mil doadores e registros de encaminhamento das famílias que recebem cestas de alimentos. O conselho pediu a ela que assumisse a responsabilidade pela governança de dados. Ela se inscreve em um curso profissional de seis meses na fictícia Kingsford Professional Academy, conduzido pelo Sr. Tomasz Nowak, com encontros uma noite por semana e dados sintéticos em todos os exercícios. Grace está ansiosa para começar.

### 1.2 Os dados da Northbank

Grace lista os dados da organização: nomes, endereços, e-mails e históricos de doação dos doadores; contatos, disponibilidade e verificações de salvaguarda dos voluntários; encaminhamentos de clientes feitos por assistentes sociais e médicos, com tamanho da família, motivos da necessidade e, às vezes, informações de saúde; registros de estoque dos alimentos recebidos e distribuídos; e registros financeiros. Ela observa que os encaminhamentos são os dados mais sensíveis, porque revelam dificuldades e, às vezes, condições de saúde, que o GDPR trata como categoria especial e a LGPD como dado pessoal sensível (art. 5º, II), com proteção adicional.

### 1.3 Situação atual

Grace encontra os dados espalhados por um banco de dados de doadores, planilhas mantidas por cada banco de alimentos, formulários de encaminhamento em papel guardados em arquivos, uma caixa de e-mail compartilhada e os celulares pessoais dos voluntários. Ninguém escreveu regras sobre quem pode ver os encaminhamentos nem por quanto tempo eles são guardados. Um conselheiro perguntou recentemente quantas famílias foram atendidas no ano anterior, e três bancos de alimentos deram números com definições diferentes de família. O Sr. Nowak observa que esse é um ponto de partida típico de uma organização pequena. Grace registra essa situação no caderno do curso.

### 1.4 Metas

Grace define metas para o curso: saber que dados a Northbank tem e onde estão, acordar quem é responsável por cada tipo, proteger adequadamente os dados dos clientes, melhorar os dados dos doadores para a captação de recursos e apresentar números confiáveis ao conselho. O Sr. Nowak pede que cada meta seja mensurável, como todos os seis bancos de alimentos usando uma única definição de família até o fim do curso. Ela escreve as metas no caderno e as compartilha com a presidente do conselho, que as recebe bem e pede atualizações periódicas sobre o andamento de cada uma.

### Exemplo resolvido

Grace, nova gerente de operações da Northbank, lista os dados de doadores, voluntários, clientes, estoque e finanças, encontra registros espalhados e contagens de famílias inconsistentes e define metas mensuráveis de governança, compartilhadas com a presidente do conselho.

> **Caso sintético.** A Northbank, a Kingsford e todas as pessoas são sintéticas; o GDPR e a LGPD são reais.

### Erros e limites

Tratar os dados de uma organização pequena como simples demais para serem governados deixa registros sensíveis desprotegidos.

### Exercícios

- **EX001 — Duração do curso.** Quanto dura o curso de Grace? *Rubrica:* 3 = seis meses;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX002 — Dados mais sensíveis.** Quais são os dados mais sensíveis da Northbank? *Rubrica:* 3 = os encaminhamentos de clientes;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX003 — Categoria especial.** Por que os encaminhamentos podem ser dados de categoria especial? *Rubrica:* 3 = às vezes contêm informações de saúde;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX004 — Números de famílias.** O que deu errado quando o conselho perguntou sobre as famílias atendidas? *Rubrica:* 3 = os bancos usavam definições diferentes;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX005 — Meta mensurável.** Dê o exemplo de meta mensurável do curso. *Rubrica:* 3 = os seis bancos usando uma única definição de família;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Por que a governança importa para uma organização beneficente

### Objetivos de aprendizagem

Você vai (1) explicar ao conselho os benefícios da governança de dados; (2) ligar a governança à missão da organização; (3) descrever os riscos de não fazer nada.

### 2.1 Missão e confiança

O Sr. Nowak explica que as organizações beneficentes dependem da confiança de doadores, clientes, voluntários e financiadores. Os doadores contribuem porque confiam que seu dinheiro e seus dados serão bem tratados. Os clientes compartilham dificuldades pessoais porque confiam que elas ficarão em sigilo. Grace escreve que a governança protege essa confiança ao garantir que os dados sejam exatos, usados só como prometido e mantidos em segurança. Ela observa que um vazamento de encaminhamentos poderia levar famílias a deixar de pedir ajuda. Grace coloca esse ponto no topo de seu informe ao conselho, porque ele liga os dados às pessoas que a organização existe para ajudar.

### 2.2 Decisões melhores

Bons dados ajudam a Northbank a decidir onde abrir um novo ponto de distribuição, que alimentos pedir e quando os voluntários são mais necessários. Com definições inconsistentes, a organização não consegue comparar os bancos de alimentos nem mostrar seu impacto aos financiadores. Grace explica ao conselho que definições e verificações acordadas permitiriam ver tendências confiáveis. O DAMA-DMBOK2 descreve a governança como o exercício de autoridade e controle sobre os dados para que sirvam aos objetivos da organização. Grace dá um exemplo ao conselho: com uma única definição de família, seria possível comparar pela primeira vez a demanda dos seis bancos de alimentos.

### 2.3 Deveres legais

A Northbank precisa seguir a legislação de proteção de dados. O GDPR exige uma base legal para cada uso de dados pessoais, condições adicionais para os dados de categoria especial, segurança, limites ao tempo de guarda e respostas aos pedidos das pessoas; a LGPD traz exigências equivalentes, com as bases legais nos arts. 7º e 11. Os e-mails de captação de recursos exigem consentimento segundo as regras de marketing eletrônico. Grace lista os deveres aplicáveis e observa que descumpri-los pode gerar reclamações, ações da autoridade e danos à reputação, o que pesa muito nas doações. Ela compartilha a lista com o conselho e pede à presidente que defina quem vai conferir cada dever.

### 2.4 Os riscos de não fazer nada

Grace lista os riscos: formulários de encaminhamento perdidos de um arquivo destrancado, o celular de um voluntário com números de clientes roubado, doadores recebendo e-mails depois de pedirem para não receber, financiadores recebendo números inconsistentes e registros guardados por anos sem motivo. Para cada risco, ela estima a probabilidade e o impacto com a escala simples do Sr. Nowak. Os maiores riscos envolvem dados de clientes em papel e em celulares. Ela usa essa lista para explicar ao conselho por que a governança precisa de tempo e atenção. O conselho concorda em dar a Grace dois dias por mês para esse trabalho e revisar o andamento a cada trimestre.

### Exemplo resolvido

Grace liga a governança à confiança, a decisões melhores e aos deveres legais, lista os riscos de não fazer nada e aponta ao conselho os dados de clientes em papel e em celulares como os maiores riscos.

> **Caso sintético.** Os riscos são sintéticos; o DAMA-DMBOK2, o GDPR e a LGPD são reais.

### Erros e limites

Apresentar a governança apenas como conformidade ignora seu valor para as decisões e a confiança.

### Exercícios

- **EX006 — Efeito de um vazamento.** Como um vazamento de encaminhamentos poderia afetar os clientes? *Rubrica:* 3 = famílias poderiam deixar de pedir ajuda;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX007 — Regra de marketing.** O que os e-mails de captação de recursos exigem? *Rubrica:* 3 = consentimento;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX008 — Exemplo de decisão.** Cite uma decisão apoiada por bons dados. *Rubrica:* 3 = onde abrir um ponto de distribuição;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.
- **EX009 — Maiores riscos.** Que riscos ficaram no topo? *Rubrica:* 3 = dados de clientes em papel e em celulares;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX010 — Argumento ao conselho.** O que Grace usou para explicar a necessidade de governança? *Rubrica:* 3 = sua lista ordenada de riscos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Papéis e responsabilidades

### Objetivos de aprendizagem

Você vai (1) definir papéis de governança para uma pequena organização beneficente; (2) atribuí-los de forma realista; (3) escrever descrições simples de papéis.

### 3.1 Papéis simples

O Sr. Nowak explica que as organizações pequenas precisam de papéis simples. Um conselheiro assume a supervisão dos dados em nome do conselho. Uma líder de dados, Grace, coordena a governança no dia a dia. Os donos são os gestores responsáveis por cada tipo de dado: a gerente de captação de recursos pelos doadores, o coordenador de voluntários pelos voluntários e os líderes dos bancos de alimentos pelos encaminhamentos de clientes. Voluntários e funcionários seguem as regras. Grace observa que nomes claros importam mais que títulos imponentes. Ela escreve os papéis em uma tabela curta, com uma linha por pessoa e os dados de que ela cuida.

### 3.2 Atribuindo os papéis

Grace propõe os papéis ao conselho. Uma conselheira com experiência jurídica aceita supervisionar os dados. A gerente de captação aceita ser dona dos dados de doadores. Os líderes dos bancos de alimentos aceitam ser donos dos encaminhamentos, com Grace definindo regras comuns. Grace verifica se a Northbank precisa nomear um encarregado pelo tratamento de dados pessoais e conclui que o tratamento em larga escala de dados de categoria especial pode exigi-lo; no Brasil, o encarregado está previsto no art. 41 da LGPD. Ela leva a questão à conselheira, que providencia orientação externa, e o conselho decide contratar um encarregado externo em tempo parcial.

### 3.3 Descrições dos papéis

Grace escreve uma descrição curta para cada papel: que decisões toma, o que precisa conferir e a quem presta contas. A descrição do líder de banco de alimentos inclui decidir quais voluntários podem ver os encaminhamentos, conferir se os formulários em papel estão trancados e relatar problemas a Grace em até um dia. Ela limita cada descrição a meia página. O Sr. Nowak observa que descrições curtas têm mais chance de ser lidas e seguidas. Cada dono lê e assina sua descrição, e Grace guarda as cópias assinadas junto com a política de dados, para consulta sempre que surgir uma dúvida sobre quem decide.

### 3.4 Fazendo os papéis pegarem

Grace inclui as responsabilidades sobre dados na integração dos voluntários, para que os novatos saibam a quem perguntar. Acrescenta um item fixo sobre dados na reunião mensal dos líderes. Também pede à conselheira que informe sobre os dados em cada reunião do conselho. O Sr. Nowak explica que os papéis se tornam reais quando aparecem nas rotinas, como integrações e reuniões, e não apenas em um documento que ninguém relê. Depois de três meses, Grace percebe que os líderes levantam questões sobre dados na maioria das reuniões mensais, sinal de que a rotina funciona e de que eles já veem os dados como parte do trabalho.

### Exemplo resolvido

Grace define os papéis de conselheira, líder de dados, donos e voluntários, atribui a supervisão a uma conselheira com experiência jurídica, levanta a possível necessidade de um encarregado pelo tratamento de dados e incorpora os papéis às integrações e reuniões.

> **Caso sintético.** Os papéis são sintéticos; o GDPR e a LGPD são reais.

### Erros e limites

Copiar a estrutura de papéis de grandes empresas para uma pequena organização cria cargos vagos.

### Exercícios

- **EX011 — Dona dos doadores.** Quem é dono dos dados de doadores? *Rubrica:* 3 = a gerente de captação de recursos;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX012 — Conselheira supervisora.** Qual conselheira supervisiona os dados? *Rubrica:* 3 = a que tem experiência jurídica;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX013 — Questão do encarregado.** Por que a Northbank pode precisar de um encarregado pelo tratamento de dados? *Rubrica:* 3 = tratamento em larga escala de dados de categoria especial;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX014 — Prazo dos líderes.** Em quanto tempo os líderes devem relatar problemas? *Rubrica:* 3 = em até um dia;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX015 — Incorporando os papéis.** Cite uma rotina que incorpora os papéis. *Rubrica:* 3 = a integração dos voluntários ou as reuniões mensais;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Um inventário de dados

### Objetivos de aprendizagem

Você vai (1) montar um inventário de dados; (2) registrar finalidade, local e acesso; (3) usar o inventário para encontrar lacunas.

### 4.1 Montando o inventário

Grace monta um inventário em uma planilha. Cada linha é um conjunto de dados, como o banco de dados de doadores ou os formulários de encaminhamento do banco de alimentos da beira do rio. As colunas registram que dados pessoais ele contém, a finalidade, a base legal, onde está armazenado, quem pode acessá-lo, por quanto tempo é guardado e o dono. Ela visita cada banco de alimentos e pede aos líderes que lhe mostrem onde os dados ficam, em vez de confiar em descrições, e encontra itens que ninguém tinha mencionado. Ela visita os seis bancos em duas semanas e completa o inventário logo depois.

### 4.2 Surpresas

Em dois bancos de alimentos, os voluntários guardam os telefones dos clientes nos celulares pessoais para combinar as retiradas. Um banco guarda em um armário formulários de encaminhamento de cinco anos atrás. A caixa de e-mail compartilhada contém encaminhamentos de assistentes sociais com todos os detalhes dos casos. Grace registra cada item no inventário. O Sr. Nowak observa que as visitas presenciais revelam práticas informais que as pessoas nem pensam em mencionar, porque lhes parecem normais. Grace agradece aos líderes por mostrarem essas práticas abertamente e explica que o objetivo é corrigir os problemas, e não culpar ninguém.

### 4.3 Encontrando lacunas

Com o inventário completo, Grace procura lacunas: dados sem finalidade clara, dados sem base legal registrada, dados guardados por tempo demais e dados acessíveis a gente demais. Ela descobre que os formulários de cinco anos já não têm finalidade, que os celulares pessoais dos voluntários estão fora de controle e que a caixa compartilhada está aberta a todos os funcionários. Ela lista ações com donos e datas para cada lacuna. A conselheira que supervisiona os dados revisa a lista e acorda as datas com cada dono, para que as lacunas mais graves, que envolvem dados de clientes, sejam tratadas primeiro.

### 4.4 Mantendo-o atualizado

Grace pede aos donos que a avisem quando começarem a coletar dados novos ou mudarem a forma de armazená-los. Ela agenda uma revisão do inventário a cada seis meses. Também usa o inventário para escrever o aviso de privacidade da Northbank, porque ele lista que dados são mantidos e por quê. O Sr. Nowak explica que o GDPR espera que as organizações mantenham registros das operações de tratamento, e que a LGPD tem exigência semelhante no art. 37; um bom inventário atende a essa finalidade e a muitas outras. Grace inclui a revisão do inventário no calendário de governança, para que não seja esquecida nos períodos movimentados.

### Exemplo resolvido

Grace monta um inventário visitando cada banco de alimentos, encontra números de clientes em celulares pessoais, formulários de cinco anos e uma caixa de e-mail aberta, lista ações para as lacunas e mantém o inventário atualizado para o aviso de privacidade.

> **Caso sintético.** As constatações são sintéticas; o GDPR e a LGPD são reais.

### Erros e limites

Montar inventários só a partir de descrições deixa escapar as práticas informais.

### Exercícios

- **EX016 — Motivo das visitas.** Por que Grace visitou pessoalmente os bancos de alimentos? *Rubrica:* 3 = para encontrar dados que as pessoas não mencionam;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX017 — Formulários antigos.** Quantos anos tinham os formulários esquecidos? *Rubrica:* 3 = cinco anos;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX018 — Lacuna da caixa de e-mail.** O que havia de errado com a caixa compartilhada? *Rubrica:* 3 = aberta a todos os funcionários, com detalhes dos casos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX019 — Ciclo de revisão.** Com que frequência o inventário é revisado? *Rubrica:* 3 = a cada seis meses;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX020 — Uso no aviso.** Que documento o inventário ajuda a escrever? *Rubrica:* 3 = o aviso de privacidade;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — O essencial da política

### Objetivos de aprendizagem

Você vai (1) escrever uma política de dados curta; (2) transformá-la em regras práticas para os voluntários; (3) obter a aprovação e comunicá-la.

### 5.1 Uma política curta

Grace redige uma política de dados de duas páginas para a Northbank: por que os dados importam para a missão, os papéis, os princípios para o tratamento de dados pessoais, as regras para os dados dos clientes, o básico de segurança, a retenção e como relatar problemas. Ela evita a linguagem jurídica sempre que possível. A política estabelece que os encaminhamentos só podem ser vistos por voluntários nomeados do banco de alimentos correspondente e nunca podem ser guardados em dispositivos pessoais. Os donos comentam, e ela revisa o rascunho. A versão final fica mais clara e mais curta que a primeira, sem perder nenhuma regra importante.

### 5.2 Regras práticas

A maioria dos voluntários não vai ler uma política. Grace a transforma em um guia de uma página chamado Cuidando das informações das pessoas, com dez regras simples, como trancar os formulários de encaminhamento no fim de cada turno, nunca fotografar formulários e relatar papéis ou celulares perdidos ao líder no mesmo dia. Ela testa o guia com cinco voluntários, que sugerem palavras mais simples para duas regras. O guia final é impresso para todos os bancos de alimentos. Grace acrescenta ilustrações simples para ajudar os voluntários a lembrar das regras durante os turnos mais corridos.

### 5.3 Aprovação

A conselheira que supervisiona os dados apresenta a política ao conselho, explicando os riscos e os benefícios. O conselho a aprova e pede um relatório de andamento em três meses. Grace observa que a aprovação do conselho dá autoridade à política, o que ajuda quando líderes ou voluntários resistem a mudanças, como deixar de usar os celulares pessoais. O Sr. Nowak explica que políticas sem apoio da alta liderança são facilmente ignoradas. A conselheira também pede a Grace que traga exemplos de como a política mudou a prática em cada banco de alimentos, para que o conselho veja efeitos reais, e não apenas um documento.

### 5.4 Comunicação

Grace apresenta o guia em cada banco de alimentos com uma fala curta durante um turno, explicando por que cada regra protege os clientes. Ela responde a perguntas, como a de saber como os voluntários devem combinar as retiradas sem os celulares pessoais. Para isso, providencia um celular da organização em cada banco de alimentos. Ela observa que as regras são seguidas com mais boa vontade quando as pessoas entendem o motivo e têm uma alternativa prática aos velhos hábitos. Depois das falas, Grace confere com cada líder se o guia está afixado e se o celular da organização está em uso nas retiradas.

### Exemplo resolvido

Grace redige uma política de duas páginas, transforma-a em um guia de dez regras testado com voluntários, obtém a aprovação do conselho com um retorno em três meses e a apresenta com falas presenciais e celulares da organização.

> **Caso sintético.** Os documentos são sintéticos.

### Erros e limites

Proibir uma prática sem oferecer alternativa leva as pessoas a continuar com ela às escondidas.

### Exercícios

- **EX021 — Regra dos dados de clientes.** Quem pode ver os encaminhamentos de clientes? *Rubrica:* 3 = voluntários nomeados do banco de alimentos correspondente;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX022 — Título do guia.** Como se chama o guia dos voluntários? *Rubrica:* 3 = Cuidando das informações das pessoas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX023 — Número de regras.** Quantas regras o guia tem? *Rubrica:* 3 = dez;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX024 — Alternativa aos celulares.** O que substituiu os celulares pessoais nas retiradas? *Rubrica:* 3 = um celular da organização em cada banco de alimentos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX025 — Pedido do conselho.** O que o conselho pediu após a aprovação? *Rubrica:* 3 = um relatório de andamento em três meses;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Qualidade de dados na prática

### Objetivos de aprendizagem

Você vai (1) encontrar registros duplicados de doadores; (2) normalizar campos simples; (3) criar hábitos de qualidade para uma equipe pequena.

### 6.1 Doadores duplicados

A gerente de captação conta que alguns doadores recebem duas cópias de cada boletim e reclamam. Grace suspeita de endereços de e-mail duplicados, digitados de maneiras diferentes. Ela exporta e-mails sintéticos de doadores e verifica quantos são, na verdade, o mesmo endereço escrito de outro jeito, com letras maiúsculas ou espaços a mais. Explica que as duplicatas desperdiçam dinheiro, irritam os doadores e fazem parecer que a Northbank tem mais apoiadores do que realmente tem. A gerente de captação concorda em exportar a lista de e-mails dos doadores e conferi-la com a ajuda de Grace.

```python
"""Count duplicate synthetic donor emails before and after normalising case and spaces (stdlib only)."""
import random
random.seed(2)
base = [f"donor{i}@example.org" for i in range(1500)]
emails = []
for e in base:
    emails.append(e)
    if random.random() < 0.08: emails.append(e.upper())
    if random.random() < 0.05: emails.append(" " + e + " ")
print(f"records {len(emails)}; distinct as written {len(set(emails))}; distinct normalised {len({e.strip().lower() for e in emails})}")
print(f"duplicate records found by normalising {len(emails) - len({e.strip().lower() for e in emails})}")
```

Execute com `python3 lab_emails.py`. Saída verificada:

```text
records 1684; distinct as written 1684; distinct normalised 1500
duplicate records found by normalising 184
```

### 6.2 Resultados

O laboratório confere 1.684 registros sintéticos de e-mail. Como foram escritos, os 1.684 são todos distintos, de modo que uma verificação simples de duplicatas não encontra nada. Depois de converter para minúsculas e remover os espaços das pontas, restam apenas 1.500 endereços distintos. A normalização revela 184 registros duplicados. Grace observa que as duplicatas eram invisíveis até a normalização, e por isso os boletins saíam em dobro sem que ninguém entendesse o motivo. Ela explica a constatação à gerente de captação com três exemplos do mesmo endereço escrito de formas diferentes, o que torna o problema fácil de entender sem conhecimento técnico.

### 6.3 Corrigindo e prevenindo

A gerente de captação funde os doadores duplicados no banco de dados, mantendo o histórico completo de doações em um único registro. Grace pergunta ao fornecedor do banco de dados se os e-mails podem ser guardados automaticamente em minúsculas, e ele confirma que sim. Ela também pede à equipe que procure o doador antes de cadastrar um novo. O Sr. Nowak observa que é preciso corrigir as duplicatas existentes e também prevenir as novas, senão o problema volta. Depois das mudanças, as reclamações sobre boletins em dobro param, e a gerente de captação apresenta ao conselho uma contagem mais exata de apoiadores.

### 6.4 Hábitos de qualidade

Grace cria hábitos simples: uma verificação mensal de duplicatas, uma verificação trimestral de CEPs ausentes e uma verificação anual de que a definição de família é usada de forma consistente. Cada verificação tem um dono e leva menos de uma hora. Ela registra os resultados em um log curto. Observa que verificações pequenas e regulares combinam melhor com uma organização de equipe reduzida do que grandes mutirões de limpeza que competem com o trabalho diário. O log é revisado em cada reunião mensal dos líderes, para que os problemas sejam percebidos cedo e os donos vejam que suas verificações fazem diferença.

### Exemplo resolvido

Grace encontra 184 e-mails de doadores duplicados, invisíveis até que 1.684 registros fossem normalizados em 1.500 endereços, funde-os mantendo o histórico de doações, ativa o armazenamento em minúsculas e a busca antes do cadastro e cria verificações mensais.

> **Caso sintético.** Os e-mails são sintéticos; as saídas vêm de lab_emails.py.

### Erros e limites

Verificações de duplicatas por correspondência exata deixam passar diferenças de maiúsculas e espaços.

### Exercícios

- **EX026 — Distintos após normalizar.** Quantos endereços distintos restam após a normalização? *Rubrica:* 3 = 1.500;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX027 — Duplicatas reveladas.** Quantos registros duplicados a normalização revelou? *Rubrica:* 3 = 184;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX028 — Resultado da verificação exata.** O que uma verificação exata de duplicatas encontrou? *Rubrica:* 3 = nada; todos os 1.684 eram distintos;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX029 — Mudança do fornecedor.** O que o fornecedor ativou? *Rubrica:* 3 = o armazenamento automático dos e-mails em minúsculas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX030 — Duração das verificações.** Quanto tempo cada verificação deve levar? *Rubrica:* 3 = menos de uma hora;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Grace Mwangi, o Sr. Tomasz Nowak, a Kingsford Professional Academy, a Northbank Food Bank Network e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Seis meses.

**EX002.** Os encaminhamentos de clientes.

**EX003.** Às vezes incluem informações de saúde.

**EX004.** Os bancos de alimentos usavam definições diferentes de família.

**EX005.** Os seis bancos de alimentos usando uma única definição de família.

**EX006.** As famílias poderiam deixar de pedir ajuda.

**EX007.** Consentimento, segundo as regras de marketing eletrônico.

**EX008.** Onde abrir um novo ponto de distribuição.

**EX009.** Dados de clientes guardados em papel e em celulares.

**EX010.** Sua lista ordenada de riscos.

**EX011.** A gerente de captação de recursos.

**EX012.** Uma conselheira com experiência jurídica.

**EX013.** O tratamento em larga escala de dados de categoria especial.

**EX014.** Em até um dia.

**EX015.** A integração dos voluntários.

**EX016.** Para encontrar práticas informais que as pessoas não mencionariam.

**EX017.** Cinco anos.

**EX018.** Continha detalhes dos casos e estava aberta a todos os funcionários.

**EX019.** A cada seis meses.

**EX020.** O aviso de privacidade.

**EX021.** Apenas voluntários nomeados do banco de alimentos correspondente.

**EX022.** Cuidando das informações das pessoas.

**EX023.** Dez.

**EX024.** Um celular compartilhado da organização em cada banco de alimentos.

**EX025.** Um relatório de andamento em três meses.

**EX026.** 1.500.

**EX027.** 184.

**EX028.** Nada, porque os 1.684 eram distintos como foram escritos.

**EX029.** O armazenamento automático dos e-mails em minúsculas.

**EX030.** Menos de uma hora.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
