# Privacidade e Proteção de Dados: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 027, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais em transição de carreira que aprendem a conduzir o trabalho de privacidade numa pequena empresa de serviços.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios conferem currículos de candidatos diante de uma regra de retenção, acompanham os prazos dos pedidos de acesso e procuram nomes de terceiros não ocultados numa resposta de acesso, sempre sobre dados sintéticos. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma profissional ao longo de seis meses numa agência de recrutamento: fundamentos de segurança, partes interessadas e papéis, prática autorizada, métodos centrais, ferramentas, fluxo de trabalho, controles e verificação, um caso de violação, comunicação e ética, qualidade e solução de problemas, um laboratório supervisionado de ocultação e um portfólio final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Marta Silva** | Estudante do curso profissional, ex-gerente administrativa | Inventada |
| **Sra. Grace Lin** | Mentora | Inventada |
| **Northgate Professional Academy** | Academia fictícia | Inventada |
| **Halden Recruitment** | Agência fictícia, 40 consultores, cerca de 25.000 perfis de candidatos | Inventada |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR), artigos 5, 6(1)(b), 10, 12(3), 14, 15, 32, 33 e 34; Diretrizes 07/2020, 9/2022 e 01/2022 do EDPB; Lei nº 13.709/2018 (LGPD); Resolução CD/ANPD nº 15/2024; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 27701:2025. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem

Você vai (1) explicar confidencialidade, integridade e disponibilidade aplicadas a dados pessoais; (2) relacionar a segurança aos deveres de proteção de dados; (3) identificar o básico de segurança de que uma agência de recrutamento precisa.

### 1.1 O curso e o caso

Marta Silva, uma gerente administrativa em transição de carreira, entra num curso profissional de seis meses na fictícia Northgate Professional Academy. Sua mentora é a Sra. Grace Lin, profissional experiente de privacidade. O estágio de Marta é na fictícia Halden Recruitment, uma agência com quarenta consultores que guarda cerca de 25.000 perfis de candidatos, currículos, anotações de entrevistas, referências e, para algumas vagas, resultados de verificações de antecedentes. Os candidatos confiam à Halden sua trajetória, suas pretensões salariais e, às vezes, informações de saúde ou deficiência necessárias para adaptar entrevistas, então o cuidado importa desde o primeiro dia.

### 1.2 Três propriedades de segurança

A Sra. Lin começa pela confidencialidade, pela integridade e pela disponibilidade. Confidencialidade significa que só pessoas autorizadas veem o currículo e as anotações de um candidato. Integridade significa que os registros são exatos e não são alterados sem autorização, para que um candidato não seja rejeitado por causa de uma anotação errada. Disponibilidade significa que os consultores alcançam os registros quando um cliente está esperando uma lista de finalistas. Marta observa que o artigo 32 do GDPR, como o art. 46 da LGPD, pede medidas adequadas ao risco para garantir essas propriedades, e que cada uma protege os candidatos de um jeito.

### 1.3 Segurança e proteção de dados

Marta aprende que a proteção de dados é mais ampla que a segurança. A segurança protege os dados contra perda e uso indevido, enquanto a proteção de dados também pergunta se a Halden deveria coletar aqueles dados, para que finalidade, por quanto tempo e o que os candidatos sabem a respeito. Um banco de currículos perfeitamente protegido, guardado por dez anos sem motivo, ainda viola o princípio da limitação da conservação do artigo 5(1)(e). A Sra. Lin resume a relação: a segurança é necessária para a proteção de dados, mas nunca é suficiente sozinha; as duas precisam andar juntas o tempo todo.

### 1.4 O básico na Halden

Marta lista o básico de segurança e o confere na Halden: contas individuais com autenticação multifator no sistema de recrutamento, notebooks criptografados, um gerenciador de senhas, atualizações automáticas, backups testados e um jeito de a equipe comunicar erros rapidamente. Ela descobre que a autenticação multifator está ativa para apenas metade dos consultores e que os notebooks são criptografados, exceto duas máquinas antigas. Ela registra esses achados iniciais, sob responsabilidade do prestador de TI, com datas de correção para cada um. O prestador aceita os dois achados e concorda com as datas.

### Exemplo resolvido

Marta explica a confidencialidade, a integridade e a disponibilidade dos registros de candidatos, distingue segurança de proteção de dados e encontra lacunas na autenticação multifator e na criptografia dos notebooks.

> **Caso sintético.** A Northgate, a Halden e todas as pessoas são sintéticas; os artigos 5(1)(e) e 32 do GDPR e o art. 46 da LGPD são reais.

### Erros e limites

Listas de verificação do básico não mostram se os controles de fato funcionam; verifique depois.

### Exercícios

- **EX001 — Exemplo de integridade.** Dê um exemplo de falha de integridade na Halden. *Rubrica:* 3 = uma anotação errada leva à rejeição;; 2 = menciona exatidão;; 1 = nada;; 0 = nenhuma.
- **EX002 — Mais ampla que a segurança.** Por que a proteção de dados é mais ampla que a segurança? *Rubrica:* 3 = também trata de se, por que e por quanto tempo os dados são guardados;; 2 = menciona finalidade;; 1 = nada;; 0 = nenhuma.
- **EX003 — Protegido, mas ilícito.** Como um banco de currículos bem protegido ainda pode violar a lei? *Rubrica:* 3 = guardado por tempo demais, violando a limitação da conservação;; 2 = menciona retenção;; 1 = nada;; 0 = nenhuma.
- **EX004 — Cobertura da autenticação multifator.** Que parcela dos consultores tinha autenticação multifator? *Rubrica:* 3 = cerca de metade;; 2 = correta;; 1 = todos;; 0 = nenhuma.
- **EX005 — Lacuna dos notebooks.** O que se descobriu sobre a criptografia dos notebooks? *Rubrica:* 3 = duas máquinas antigas sem criptografia;; 2 = correta;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Privacidade e proteção de dados: contexto do serviço e das partes interessadas

### Objetivos de aprendizagem

Você vai (1) descrever o tratamento e as partes interessadas da Halden; (2) identificar os papéis de controlador e operador; (3) entender as expectativas dos candidatos.

### 2.1 Como o recrutamento funciona

A Halden anuncia vagas, recebe candidaturas, faz a triagem dos currículos, entrevista candidatos, coleta referências, às vezes contrata verificações de antecedentes e envia listas de finalistas aos empregadores clientes. Cada etapa trata dados pessoais. Marta mapeia as etapas com uma consultora sênior e anota de onde vêm os dados: dos próprios candidatos, de sites de vagas, de redes profissionais e de referências. Os perfis em sites de vagas são uma fonte comum para buscar candidatos passivos. Ela aprende que os dados obtidos de outras fontes acionam o dever de informação do artigo 14 do GDPR, então a Halden precisa dizer aos candidatos de onde vieram seus dados.

### 2.2 Partes interessadas

As partes interessadas incluem os candidatos, os empregadores clientes, as referências, os sites de vagas, o fornecedor de verificação de antecedentes, os consultores e a direção da Halden e a autoridade de proteção de dados. Cada uma tem interesses diferentes. Os candidatos querem tratamento justo e discrição, sobretudo quando ainda estão empregados em outro lugar. Os clientes querem candidatos adequados, e rápido. Os consultores querem ferramentas eficientes. Marta observa que as referências também são titulares, porque seus nomes e opiniões ficam registrados, e que uma referência que dá uma opinião franca espera discrição; uma divulgação descuidada pode prejudicar relações de trabalho.

### 2.3 Papéis

A Sra. Lin ajuda Marta a raciocinar sobre os papéis. A Halden é controladora do seu banco de candidatos, porque decide por que e como os dados são tratados. Quando a Halden envia uma lista de finalistas a um cliente, o cliente se torna um controlador separado para a sua decisão de contratação. O fornecedor de verificação de antecedentes atua como operador em algumas verificações e como controlador em outras, conforme o contrato. Marta usa as Diretrizes 07/2020 do EDPB sobre os conceitos de controlador e operador para analisar cada relação, em vez de deduzir os papéis pelos cargos ou pelo nome dos serviços contratados.

### 2.4 Expectativas dos candidatos

Marta revisa vinte reclamações sintéticas e anonimizadas de uma pesquisa setorial. Os temas comuns incluem currículos enviados a empregadores sem o conhecimento do candidato, perfis guardados por anos depois de um pedido de remoção e ligações inesperadas sobre vagas sem relação com o candidato. Ela conclui que os candidatos esperam ser consultados antes de seu currículo ir para um cliente específico e saber por quanto tempo ficam no cadastro. A discrição importa sobretudo para quem está empregado e procurando em silêncio. Essas expectativas orientam seu trabalho posterior sobre consentimento, retenção e transparência na Halden.

### Exemplo resolvido

Marta mapeia as etapas e as fontes do recrutamento, lista as partes interessadas, incluindo as referências, define os papéis de controlador e operador com as Diretrizes 07/2020 do EDPB e identifica as expectativas dos candidatos a partir de reclamações sintéticas.

> **Caso sintético.** As reclamações são sintéticas; o artigo 14 do GDPR e as Diretrizes 07/2020 do EDPB são reais.

### Erros e limites

Os papéis dependem dos fatos e dos contratos; registre o raciocínio de cada um.

### Exercícios

- **EX006 — Gatilho do artigo 14.** Quando o artigo 14 se aplica na Halden? *Rubrica:* 3 = dados obtidos de sites de vagas ou redes profissionais;; 2 = menciona outras fontes;; 1 = nada;; 0 = nenhuma.
- **EX007 — Titulares esquecidos.** Que titulares costumam ser esquecidos? *Rubrica:* 3 = as referências;; 2 = correta;; 1 = clientes;; 0 = nenhuma.
- **EX008 — Papel do cliente.** Que papel o empregador cliente tem na sua decisão de contratação? *Rubrica:* 3 = controlador separado;; 2 = correta;; 1 = operador;; 0 = nenhuma.
- **EX009 — Orientação sobre papéis.** Que diretrizes ajudam a definir os papéis? *Rubrica:* 3 = Diretrizes 07/2020 do EDPB;; 2 = correta;; 1 = outra;; 0 = nenhuma.
- **EX010 — Expectativa.** O que os candidatos esperam antes de o currículo ir para um cliente? *Rubrica:* 3 = ser consultados;; 2 = correta;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e tratamento de evidências

### Objetivos de aprendizagem

Você vai (1) trabalhar dentro de um escopo autorizado; (2) tratar evidências que contêm dados pessoais; (3) respeitar a confidencialidade durante as revisões.

### 3.1 Trabalhar dentro da autorização

A Sra. Lin explica que um profissional de privacidade costuma ver dados sensíveis e só deve agir dentro da autorização recebida. O termo de estágio de Marta permite revisar processos, configurações e amostras de registros escolhidas com a responsável pela proteção de dados, usando dados sintéticos ou ocultados sempre que possível. Não permite contatar candidatos, mudar configurações por conta própria nem pesquisar registros por curiosidade. Quando um consultor lhe pede para consultar a situação da candidatura de um amigo, ela recusa e registra o pedido, deixando claro que a recusa não é pessoal, e sim um limite do seu escopo.

### 3.2 Tratamento das evidências

Durante as revisões, Marta coleta evidências como capturas de tela das configurações de retenção, contagens exportadas e cópias dos avisos de privacidade. Ela guarda as evidências numa pasta restrita, nomeia os arquivos com um padrão de data e tema e registra como cada item foi obtido. Quando uma captura de tela mostraria nomes de candidatos, ela pede um exemplo sintético ou recorta a imagem para mostrar só a configuração. Ela observa que as evidências também são dados pessoais quando contêm nomes, então precisam de prazo de retenção próprio; aqui, elas expiram ao fim do estágio.

### 3.3 Confidencialidade nas conversas

As entrevistas com os consultores às vezes revelam preocupações sobre colegas, como um gerente que compartilha currículos pelo e-mail pessoal. Marta registra os fatos relevantes para os processos e evita fofocas ou julgamentos pessoais nas anotações. Ela só discute os achados sensíveis com a responsável pela proteção de dados e com a Sra. Lin. Aprende que as pessoas compartilham problemas mais abertamente quando confiam que a informação será usada para corrigir processos, e não para culpar indivíduos, o que torna o tratamento justo uma questão prática, além de ética, para quem precisa ouvir a verdade.

### 3.4 Registrar as decisões

Marta mantém um diário de decisões do estágio: o que lhe pediram, o que ela decidiu e por quê, e quem aprovou. O diário inclui a recusa da consulta pedida pelo consultor, a decisão de usar uma exportação sintética na revisão da retenção e um acordo com a responsável pela proteção de dados sobre quais caixas de e-mail ela pode examinar por amostragem. A Sra. Lin revisa o diário toda semana. Ela explica que um registro claro protege tanto o profissional quanto a organização se as decisões forem questionadas depois pela direção ou por um regulador.

### Exemplo resolvido

Marta trabalha dentro de um escopo de estágio escrito, recusa a consulta da candidatura de um amigo, guarda as evidências numa pasta restrita com recortes ou exemplos sintéticos, mantém as conversas confidenciais e conserva um diário de decisões.

> **Caso sintético.** O escopo e o diário são sintéticos.

### Erros e limites

A autorização pode ser pouco clara em empresas pequenas; peça por escrito antes de agir.

### Exercícios

- **EX011 — Pedido fora do escopo.** Que pedido Marta recusou? *Rubrica:* 3 = consultar a situação da candidatura de um amigo;; 2 = correta;; 1 = nada;; 0 = nenhuma.
- **EX012 — Limites do estágio.** Cite algo que Marta não pode fazer. *Rubrica:* 3 = contatar candidatos, mudar configurações, pesquisar por curiosidade;; 2 = um;; 1 = nada;; 0 = nenhuma.
- **EX013 — Nomes nas capturas.** Como Marta evita capturar nomes nas telas? *Rubrica:* 3 = exemplos sintéticos ou recorte;; 2 = um;; 1 = nada;; 0 = nenhuma.
- **EX014 — Benefício da confiança.** Por que o tratamento justo ajuda na prática? *Rubrica:* 3 = as pessoas compartilham problemas mais abertamente;; 2 = menciona abertura;; 1 = nada;; 0 = nenhuma.
- **EX015 — Diário de decisões.** O que o diário de decisões de Marta registra? *Rubrica:* 3 = pedido, decisão, razão, quem aprovou;; 2 = a maioria;; 1 = um;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Privacidade e proteção de dados: métodos centrais

### Objetivos de aprendizagem

Você vai (1) aplicar o mapeamento de dados, a revisão da retenção e a análise da base legal; (2) analisar a retenção de currículos num laboratório; (3) recomendar mudanças.

### 4.1 Mapeamento de dados

Marta monta um mapa de dados da Halden com cada categoria de dados, sua fonte, finalidade, sistema, destinatários e retenção. As categorias incluem contatos, currículos, anotações de entrevistas, referências, documentos de autorização de trabalho, resultados de verificação de antecedentes e respostas de monitoramento de diversidade. O mapa mostra que as respostas de diversidade ficam guardadas com os nomes no sistema de recrutamento, embora só sejam usadas em estatísticas anônimas. Ela recomenda guardá-las separadas e sem nomes, o que apoia a minimização e reduz o impacto de uma violação no banco principal. O prestador de TI confirma que é viável.

### 4.2 Revisão da retenção

A política da Halden diz que os currículos dos candidatos não aprovados são excluídos seis meses depois do último contato, salvo se o candidato aceitar ficar no banco de talentos. Marta confere a prática com uma cópia sintética do banco de candidatos. O laboratório mostra que 1.792 de 2.500 candidatos, 71,7%, passaram dos seis meses sem aceite do banco de talentos, então a política não vem sendo aplicada; a maioria desses perfis tem anos. Também encontra 216 candidatos do banco de talentos sem contato há mais de dois anos, cujo aceite provavelmente está desatualizado e deveria ser renovado ou encerrado.

### 4.3 Análise da base legal

Com a responsável pela proteção de dados, Marta revisa as bases legais. Tratar candidaturas para uma vaga específica se apoia em diligências pré-contratuais a pedido do candidato, pelo artigo 6(1)(b) do GDPR e pelo art. 7º, V, da LGPD. Manter candidatos no banco de talentos para vagas futuras se apoia no consentimento, que precisa ser específico e revogável. As verificações de autorização de trabalho se apoiam em obrigação legal. As verificações de antecedentes exigem análise cuidadosa, sobretudo de registros criminais, que o artigo 10 do GDPR restringe. Ela documenta cada base, e os consultores recebem um resumo do que podem usar para cada finalidade.

### 4.4 Recomendações

Marta recomenda três mudanças: rodar uma rotina automática de exclusão dos currículos vencidos depois de um teste em modo somente relatório; enviar um pedido de renovação aos candidatos do banco de talentos sem contato há dois anos e excluir os que não responderem; e separar os dados de diversidade dos nomes. Ela estima que só a primeira mudança remove mais de dois terços dos perfis guardados. O diretor-geral aprova, e o prestador de TI agenda o trabalho, com Marta preparando o plano de teste. Cada mudança tem responsável e data, e a primeira execução real da exclusão fica marcada para depois do teste.

### Laboratório — Currículos de candidatos além do prazo de retenção

```python
"""Check candidate CVs against a retention rule in a synthetic recruitment database (stdlib only)."""
import random, datetime
random.seed(21)
today = datetime.date(2026, 10, 1)
cands = []
for i in range(2500):
    last = today - datetime.timedelta(days=random.randint(0, 1500))
    pool = random.random() < 0.18          # candidate agreed to stay in talent pool
    cands.append((i, last, pool))
rule = 183                                  # six months after last contact
expired = [c for c in cands if (today - c[1]).days > rule and not c[2]]
pool_old = [c for c in cands if c[2] and (today - c[1]).days > 730]
print(f"candidates {len(cands)}; past six months without pool consent {len(expired)} ({100*len(expired)/len(cands):.1f}%)")
print(f"talent-pool candidates with no contact for over two years {len(pool_old)}")
```

Execute com `python3 lab_cvs.py`. Saída verificada:

```text
candidates 2500; past six months without pool consent 1792 (71.7%)
talent-pool candidates with no contact for over two years 216
```

### Exemplo resolvido

Marta mapeia as categorias de dados, encontra 1.792 de 2.500 candidatos (71,7%) além da retenção e 216 entradas desatualizadas no banco de talentos, documenta as bases legais e recomenda a exclusão, a renovação do consentimento e a separação dos dados de diversidade.

> **Caso sintético.** Os registros são sintéticos; os artigos 6(1)(b) e 10 do GDPR e o art. 7º da LGPD são reais.

### Erros e limites

Alguns registros podem ser necessários para ações judiciais; combine as exceções antes de excluir.

### Exercícios

- **EX016 — Dados de diversidade.** O que o mapa mostrou sobre as respostas de diversidade? *Rubrica:* 3 = guardadas com nomes, embora usadas de forma anônima;; 2 = menciona nomes;; 1 = nada;; 0 = nenhuma.
- **EX017 — Currículos vencidos.** Quantos candidatos passaram dos seis meses sem aceite do banco de talentos? *Rubrica:* 3 = 1.792 de 2.500, 71,7%;; 2 = aproximada;; 1 = errada;; 0 = nenhuma.
- **EX018 — Banco desatualizado.** Quantos candidatos do banco de talentos estavam sem contato há mais de dois anos? *Rubrica:* 3 = 216;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX019 — Base do banco de talentos.** Que base legal apoia o banco de talentos? *Rubrica:* 3 = consentimento;; 2 = correta;; 1 = contrato;; 0 = nenhuma.
- **EX020 — Dados criminais.** Que artigo restringe os dados de registros criminais? *Rubrica:* 3 = artigo 10;; 2 = correta;; 1 = outro;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Privacidade e proteção de dados: ferramentas e interpretação

### Objetivos de aprendizagem

Você vai (1) usar ferramentas simples para examinar dados e configurações; (2) interpretar os resultados com cuidado; (3) evitar exagerar os achados.

### 5.1 Ferramentas práticas

Marta usa os relatórios nativos do sistema de recrutamento, filtros de planilha sobre exportações sintéticas, a busca do sistema de e-mail por anexos enviados para fora e scripts curtos em Python escritos com a ajuda da Sra. Lin. Ela aprende a começar pelos relatórios do próprio sistema antes de exportar dados, porque cada exportação cria uma nova cópia que precisa ser protegida e excluída. Quando precisa de uma exportação, pede só os campos necessários à sua pergunta, como a data do último contato e a situação no banco de talentos, e não os perfis completos. Menos campos significam menos risco.

### 5.2 Ler os resultados

Um relatório mostra que 340 e-mails com currículos anexados foram enviados para endereços externos no mês anterior. Marta resiste à conclusão de que 340 currículos foram compartilhados indevidamente. A maioria foi para empregadores clientes, como parte normal da seleção. Ela examina uma amostra de vinte e confere se cada candidato aceitou ser apresentado àquele cliente. Dezessete aceitaram, dois não puderam ser confirmados e um foi para o e-mail pessoal de um consultor. Sua interpretação é que o problema principal é a falta de registro do aceite do candidato, além de um caso grave de e-mail pessoal.

### 5.3 Incerteza

A Sra. Lin ensina Marta a dizer o que um resultado mostra e o que não mostra. A amostra de vinte sugere que a falta de registro do aceite afeta uma minoria dos casos, mas não permite calcular uma taxa precisa para o mês inteiro. O caso do e-mail pessoal mostra que isso acontece, e não com que frequência. Marta escreve seus achados com expressões como na amostra e não foi possível confirmar, que ajudam os gerentes a entender a força das evidências e a evitar tanto o pânico quanto a complacência. A precisão na linguagem constrói a confiança de quem lê o relatório.

### 5.4 Evitar o exagero

O primeiro rascunho de Marta diz que a Halden compartilha currículos rotineiramente sem consentimento. A Sra. Lin pergunta se as evidências sustentam a palavra rotineiramente. Marta reescreve: numa amostra de vinte e-mails externos com currículos, dois não tinham aceite registrado e um foi para um endereço pessoal. A nova redação é menos dramática, mas mais crível, e o diretor-geral age imediatamente. Marta observa que o exagero corrói a confiança nas orientações de privacidade, sobretudo quando os gerentes conferem as evidências por conta própria. Os fatos já eram graves o bastante sem exagero.

### Exemplo resolvido

Marta usa relatórios nativos e exportações mínimas, examina vinte de 340 e-mails externos com currículos, encontra dois aceites não confirmados e um envio a endereço pessoal e reescreve os achados para que correspondam às evidências.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

Amostras mostram padrões, não taxas exatas; diga isso.

### Exercícios

- **EX021 — Começar pelos relatórios.** Por que começar pelos relatórios nativos? *Rubrica:* 3 = as exportações criam novas cópias;; 2 = menciona cópias;; 1 = nada;; 0 = nenhuma.
- **EX022 — Resultado da amostra.** O que a amostra de vinte mostrou? *Rubrica:* 3 = 17 aceitaram, 2 não confirmados, 1 e-mail pessoal;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX023 — Problema principal.** Qual foi o problema principal identificado? *Rubrica:* 3 = falta de registro do aceite do candidato;; 2 = correta;; 1 = nada;; 0 = nenhuma.
- **EX024 — Expressão cuidadosa.** Dê uma expressão que indique incerteza. *Rubrica:* 3 = na amostra; não foi possível confirmar;; 2 = uma;; 1 = nada;; 0 = nenhuma.
- **EX025 — Exagero.** Que palavra a Sra. Lin questionou? *Rubrica:* 3 = rotineiramente;; 2 = correta;; 1 = outra;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Privacidade e proteção de dados: fluxo operacional

### Objetivos de aprendizagem

Você vai (1) conduzir o fluxo de pedidos de acesso; (2) acompanhar prazos num laboratório; (3) melhorar o fluxo.

### 6.1 Pedidos de acesso na Halden

Os candidatos às vezes pedem à Halden uma cópia dos seus dados, muitas vezes depois de serem rejeitados para uma vaga. O artigo 15 do GDPR lhes dá o direito de acesso, e o artigo 12(3) exige resposta sem demora injustificada e no prazo de um mês, prorrogável por mais dois meses nos pedidos complexos; na LGPD, o art. 19, II, fixa quinze dias para a declaração completa. Marta mapeia o fluxo da Halden: os pedidos chegam por e-mail a qualquer consultor, são encaminhados à gerente administrativa e são respondidos com buscas no sistema de recrutamento e nas caixas de e-mail. Os repasses entre pessoas acrescentavam vários dias a cada pedido.

### 6.2 Laboratório dos prazos

Marta revisa um trimestre sintético com trinta e seis pedidos de acesso. O laboratório mostra que 7 de 36, 19,4%, foram respondidos depois de um mês, e que a mediana do tempo de resposta foi de 21 dias. Os atrasos envolviam, em geral, buscas nas caixas de vários consultores e a espera por verificações de referências. Ninguém acompanhava os prazos de forma central, então os pedidos só eram notados quando os candidatos cobravam, e o padrão se repetiu em todos os meses. Marta observa que o laboratório usa um cálculo simplificado do mês, suficiente para mostrar o padrão, mas não para julgar os prazos legais de cada pedido.

### 6.3 Melhorar o fluxo

Marta desenha um registro central de pedidos com a data de recebimento, a verificação de identidade, os sistemas pesquisados, a decisão de prorrogação e a data da resposta. Os consultores encaminham os pedidos no mesmo dia a uma única caixa de privacidade. Uma lista de verificação traz todos os sistemas e caixas compartilhadas a pesquisar. Ela usa as Diretrizes 01/2022 do EDPB para decidir o que a resposta deve incluir, como finalidades, destinatários, prazos de retenção e a fonte dos dados obtidos em sites de vagas. Os lembretes ficam nos dias vinte e vinte e cinco, e a verificação de identidade é proporcional.

### 6.4 Resultados

No trimestre sintético seguinte, o registro documenta todos os pedidos, e nenhum é respondido com atraso. A mediana do tempo de resposta cai, porque as buscas são planejadas desde o primeiro dia. Marta acrescenta duas lições ao procedimento: as prorrogações precisam ser decididas e comunicadas dentro do primeiro mês, e não depois que ele passou; e os documentos de referência podem conter informações de terceiros que exigem revisão cuidadosa antes da entrega. A Sra. Lin observa que os fluxos operacionais dão certo quando tornam o passo certo também o passo fácil para consultores ocupados.

### Laboratório — Prazos dos pedidos de acesso

```python
"""Track access-request deadlines for a synthetic quarter (stdlib only)."""
import random, datetime
random.seed(4)
start = datetime.date(2026, 4, 1)
reqs = []
for i in range(36):
    recv = start + datetime.timedelta(days=random.randint(0, 80))
    took = random.choice([9, 12, 15, 18, 21, 24, 27, 33, 38, 45])
    reqs.append((recv, took))
def deadline(d):  # one month: same day next month (simplified, clamp to 28)
    m = d.month % 12 + 1; y = d.year + (d.month == 12)
    return datetime.date(y, m, min(d.day, 28))
late = [(r, t) for r, t in reqs if r + datetime.timedelta(days=t) > deadline(r)]
print(f"requests {len(reqs)}; answered after one month {len(late)} ({100*len(late)/len(reqs):.1f}%)")
print(f"median days to answer {sorted(t for _, t in reqs)[len(reqs)//2]}")
```

Execute com `python3 lab_deadlines.py`. Saída verificada:

```text
requests 36; answered after one month 7 (19.4%)
median days to answer 21
```

### Exemplo resolvido

Marta encontra 7 de 36 pedidos sintéticos (19,4%) respondidos depois de um mês, com mediana de 21 dias, cria um registro central, uma lista de verificação e lembretes, e não vê nenhuma resposta atrasada no trimestre seguinte.

> **Caso sintético.** Os pedidos são sintéticos; os artigos 12(3) e 15 do GDPR, o art. 19 da LGPD e as Diretrizes 01/2022 do EDPB são reais.

### Erros e limites

O laboratório simplifica o cálculo do mês; confira os prazos legais caso a caso.

### Exercícios

- **EX026 — Parcela atrasada.** Que parcela dos pedidos foi respondida com atraso? *Rubrica:* 3 = 7 de 36, 19,4%;; 2 = aproximada;; 1 = errada;; 0 = nenhuma.
- **EX027 — Mediana.** Qual foi a mediana do tempo de resposta? *Rubrica:* 3 = 21 dias;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX028 — Causa do atraso.** O que costumava causar o atraso? *Rubrica:* 3 = buscas em várias caixas de e-mail e espera pelas referências;; 2 = menciona caixas;; 1 = nada;; 0 = nenhuma.
- **EX029 — Conteúdo da resposta.** Cite duas coisas que a resposta deve incluir. *Rubrica:* 3 = finalidades, destinatários, retenção, fonte;; 2 = duas;; 1 = uma;; 0 = nenhuma.
- **EX030 — Momento da prorrogação.** Quando as prorrogações precisam ser decididas? *Rubrica:* 3 = dentro do primeiro mês;; 2 = correta;; 1 = depois;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Privacidade e proteção de dados: controles e verificação

### Objetivos de aprendizagem

Você vai (1) selecionar controles para os riscos do recrutamento; (2) verificar se os controles operam; (3) registrar os resultados da verificação.

### 7.1 Selecionar controles

A partir dos achados, Marta propõe seis controles: autenticação multifator para todos os consultores, bloqueio do envio de currículos para domínios de e-mail pessoal, aceite registrado do candidato antes de cada apresentação a um cliente, a rotina automática de exclusão de currículos, o registro central de pedidos de acesso e o armazenamento separado dos dados de diversidade. Cada controle é ligado a um risco e a um princípio. O bloqueio do e-mail pessoal atende à confidencialidade, e o aceite registrado atende à transparência e à lealdade, porque o candidato deve saber para onde vai o currículo antes do envio.

### 7.2 Testar os controles

Marta testa cada controle com dados sintéticos e contas de teste. Ela tenta enviar um currículo sintético para um endereço pessoal e confirma que o bloqueio aparece, com uma mensagem clara. Confere que o sistema de recrutamento recusa uma apresentação ao cliente quando o campo do aceite está vazio. Confirma que a rotina de exclusão, em modo somente relatório, lista o número esperado de perfis vencidos. Um teste falha: os dados de diversidade ainda são copiados para o sistema principal por um script antigo de importação, que o prestador de TI então remove, e Marta repete o teste até ele passar.

### 7.3 Operação ao longo do tempo

Testar uma vez mostra que um controle consegue funcionar; verificar ao longo do tempo mostra que ele continua funcionando. Marta define uma rotina trimestral: conferir a cobertura da autenticação multifator no relatório de identidades, examinar dez apresentações a clientes em busca do aceite registrado, confirmar as mensagens de sucesso da rotina de exclusão e revisar o registro de pedidos de acesso em busca de casos vencidos. Cada verificação tem responsável e resultado esperado. Ela explica que os controles em empresas pequenas costumam se deteriorar quando quem os montou vai embora, e as verificações de rotina protegem contra essa perda de atenção.

### 7.4 Registrar os resultados

Os resultados ficam num registro de verificação, revisto todo trimestre, com a data, o controle, o método de teste, o resultado e o acompanhamento. O primeiro trimestre mostra cobertura completa da autenticação multifator, dez de dez apresentações com aceite registrado e nenhum pedido vencido. O registro dá ao diretor-geral um retrato factual dos controles e dá à responsável pela proteção de dados evidências de responsabilização pelo artigo 5(2) do GDPR e pelo art. 6º, X, da LGPD. A Sra. Lin aconselha Marta a registrar as falhas com a mesma clareza dos sucessos, porque ninguém acredita num registro que nunca mostra problemas.

### Exemplo resolvido

Marta seleciona seis controles ligados a riscos, testa-os com dados sintéticos, encontra um script antigo de importação que copiava dados de diversidade, define uma verificação trimestral e registra os resultados.

> **Caso sintético.** Os controles e os resultados são sintéticos; o artigo 5(2) do GDPR e o art. 6º, X, da LGPD são reais.

### Erros e limites

Um teste aprovado pode esconder lacunas se for estreito demais; varie os casos de teste.

### Exercícios

- **EX031 — Controle do aceite.** Que princípio o aceite registrado apoia? *Rubrica:* 3 = transparência e lealdade;; 2 = um;; 1 = nenhum;; 0 = nenhuma.
- **EX032 — Teste que falhou.** Que teste falhou? *Rubrica:* 3 = dados de diversidade copiados por um script antigo de importação;; 2 = correta;; 1 = nenhum;; 0 = nenhuma.
- **EX033 — Verificações trimestrais.** Cite duas verificações trimestrais. *Rubrica:* 3 = cobertura da autenticação multifator, amostra de apresentações, sucesso da exclusão, pedidos vencidos;; 2 = duas;; 1 = uma;; 0 = nenhuma.
- **EX034 — Resultado da amostra.** Quantas apresentações da amostra tinham aceite registrado? *Rubrica:* 3 = 10 de 10;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX035 — Registrar as falhas.** Por que registrar as falhas com clareza? *Rubrica:* 3 = ninguém acredita num registro sem problemas;; 2 = menciona credibilidade;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Privacidade e proteção de dados: análise supervisionada de caso

### Objetivos de aprendizagem

Você vai (1) analisar, sob supervisão, um incidente de privacidade realista; (2) avaliar o risco aos candidatos; (3) recomendar ações proporcionais.

### 8.1 O caso

A bolsa de notebook de uma consultora é furtada de dentro de um carro. O notebook é criptografado, mas a bolsa também tem anotações impressas de entrevistas de seis candidatos, incluindo o pedido de uma candidata por adaptações na entrevista por causa de uma deficiência. Marta analisa o caso com a Sra. Lin e a responsável pela proteção de dados. Lista os fatos: o que foi perdido, quando, onde, que proteções existiam, quem foi afetado e o que já foi feito. O furto é registrado na polícia naquela mesma noite. Ela observa que o papel costuma escapar dos controles desenhados para os sistemas.

### 8.2 Avaliação de risco

Marta avalia o risco com as Diretrizes 9/2022 do EDPB. O notebook criptografado apresenta risco baixo, porque os dados são ininteligíveis sem a chave. As anotações impressas apresentam risco maior: trazem nomes, empregadores atuais, pretensões salariais e, para uma candidata, informação de saúde. A divulgação poderia prejudicar candidatos ainda empregados e revelar uma deficiência. Ela conclui que a violação é suscetível de gerar risco aos candidatos, então a autoridade de controle precisa ser notificada em até 72 horas, pelo artigo 33 do GDPR; se a Halden operasse no Brasil, a Resolução CD/ANPD nº 15/2024 daria três dias úteis. A decisão é registrada com as razões.

### 8.3 Comunicar os candidatos

Como a informação sobre a deficiência cria um risco elevado para aquela candidata, o artigo 34 exige informá-la diretamente. Marta redige comunicações para os seis candidatos explicando o que aconteceu, que informações estavam envolvidas, o que a Halden está fazendo e com quem falar. O rascunho evita jargão técnico e não minimiza o ocorrido. A Sra. Lin revisa a redação e sugere oferecer um telefonema direto à candidata com informação de saúde, porque uma conversa pessoal é mais respeitosa para uma notícia sensível. As cartas saem em até dois dias depois do furto, e o telefonema acontece no mesmo dia.

### 8.4 Ações proporcionais

Marta recomenda ações proporcionais às causas: nenhuma anotação impressa de entrevista sai do escritório, as anotações são registradas diretamente no sistema de recrutamento, os pedidos de adaptação ficam só num campo restrito e a equipe recebe uma orientação curta sobre o transporte de documentos. Ela evita recomendar medida disciplinar, porque a consultora seguia a prática que todos usavam. A responsável pela proteção de dados registra a violação, a notificação e as decisões. A Sra. Lin observa que a análise é útil porque mudou a prática, e não porque atribuiu culpa: o foco são as causas, e não as pessoas.

### Exemplo resolvido

Marta analisa o furto de uma bolsa com um notebook criptografado e anotações impressas, avalia o risco maior vindo do papel, apoia a notificação em até 72 horas, redige as comunicações aos candidatos e recomenda o fim das anotações impressas.

> **Caso sintético.** O caso é sintético; os artigos 33 e 34 do GDPR, a Resolução CD/ANPD nº 15/2024 e as Diretrizes 9/2022 do EDPB são reais.

### Erros e limites

A avaliação de risco depende de fatos que podem mudar; atualize-a à medida que a informação chega.

### Exercícios

- **EX036 — Item de baixo risco.** Por que o notebook era de baixo risco? *Rubrica:* 3 = criptografado, dados ininteligíveis sem a chave;; 2 = menciona criptografia;; 1 = nada;; 0 = nenhuma.
- **EX037 — Conteúdo de alto risco.** O que tornava as anotações impressas de maior risco? *Rubrica:* 3 = nomes, empregadores, salários e informação de saúde;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX038 — Notificação.** Em que prazo a autoridade precisa ser notificada? *Rubrica:* 3 = 72 horas;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX039 — Artigo 34.** Por que uma candidata precisa ser informada diretamente? *Rubrica:* 3 = risco elevado pela informação sobre deficiência;; 2 = menciona saúde;; 1 = nada;; 0 = nenhuma.
- **EX040 — Sem culpa.** Por que não se recomendou medida disciplinar? *Rubrica:* 3 = a consultora seguia a prática comum;; 2 = correta;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Comunicação, ética e relatórios

### Objetivos de aprendizagem

Você vai (1) escrever achados de privacidade para gestores; (2) lidar com tensões éticas; (3) relatar com clareza e justiça.

### 9.1 Escrever para gestores

Marta prepara um relatório para o diretor-geral da Halden. A Sra. Lin a aconselha a começar pelas decisões necessárias, e não pelo contexto. A primeira página lista três decisões: aprovar a rotina de exclusão, financiar a troca das duas máquinas sem criptografia e adotar a regra de nenhuma anotação impressa. Cada decisão tem uma razão curta, uma estimativa de custo e o risco de não agir. As evidências detalhadas vêm num anexo. O diretor-geral lê a primeira página em cinco minutos e aprova as três decisões, sabendo que o anexo guarda as evidências se alguém precisar conferi-las.

### 9.2 Tensões éticas

Um empregador cliente pede à Halden que informe quais candidatos têm deficiência, para planejar as adaptações com antecedência. Marta reconhece uma tensão: o objetivo do cliente parece útil, mas compartilhar informação de saúde sem a escolha do candidato não é necessário nem justo. Ela recomenda que a Halden pergunte a cada candidato se quer que as adaptações sejam comunicadas, e que compartilhe só a adaptação necessária, e não a condição. A Sra. Lin observa que o raciocínio ético costuma encontrar um jeito de atender ao objetivo legítimo protegendo a pessoa, e aqui é o consentimento que destrava a solução.

### 9.3 Relatar com justiça

Os achados de Marta envolvem consultores específicos, como o que enviou um currículo para um endereço pessoal. No relatório, ela descreve o evento e a lacuna do processo sem nomear o consultor e observa que não havia bloqueio técnico na época. A responsável pela proteção de dados conhece os detalhes e cuida separadamente de qualquer acompanhamento individual. Marta explica que relatórios feitos para melhorar sistemas devem se concentrar nas causas, e que nomear pessoas em relatórios amplos desencoraja os outros de comunicar problemas. Os sistemas mudam; as pessoas aprendem.

### 9.4 Informar os candidatos

Marta também melhora a forma como a Halden explica a privacidade aos candidatos. O aviso de privacidade é reescrito em linguagem simples, com seções sobre candidatar-se a uma vaga, ficar no banco de talentos, referências e verificações de antecedentes. Ele informa os prazos de retenção em meses, e não com expressões vagas. Uma versão curta aparece no formulário de candidatura, com um link para o aviso completo. Ela testa a versão curta com cinco personas sintéticas que representam candidatos diferentes e ajusta as frases que poderiam confundir candidatos que não têm o inglês como língua materna.

### Exemplo resolvido

Marta escreve um relatório que começa pelas decisões e é aprovado numa só leitura, resolve o pedido de um cliente sobre deficiências compartilhando, com consentimento, só as adaptações necessárias, relata as causas sem nomear funcionários e reescreve o aviso aos candidatos.

> **Caso sintético.** O relatório e o aviso são sintéticos.

### Erros e limites

A linguagem simples precisa continuar exata; confira os pontos jurídicos com a responsável pela proteção de dados.

### Exercícios

- **EX041 — Estrutura do relatório.** O que aparece na primeira página do relatório de Marta? *Rubrica:* 3 = as decisões necessárias, com razões, custos e riscos;; 2 = menciona decisões;; 1 = contexto;; 0 = nenhuma.
- **EX042 — Pedido sobre deficiência.** O que Marta recomendou diante do pedido do cliente? *Rubrica:* 3 = perguntar aos candidatos; compartilhar só as adaptações;; 2 = menciona consentimento;; 1 = compartilhar;; 0 = nenhuma.
- **EX043 — Nomear a equipe.** Por que não nomear consultores no relatório? *Rubrica:* 3 = foco nas causas; nomear desencoraja as comunicações;; 2 = menciona comunicações;; 1 = nada;; 0 = nenhuma.
- **EX044 — Redação da retenção.** Como o novo aviso informa a retenção? *Rubrica:* 3 = em meses;; 2 = correta;; 1 = vaga;; 0 = nenhuma.
- **EX045 — Teste do aviso.** Como o aviso curto foi testado? *Rubrica:* 3 = com cinco personas sintéticas;; 2 = correta;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Privacidade e proteção de dados: qualidade e solução de problemas

### Objetivos de aprendizagem

Você vai (1) diagnosticar um problema de privacidade recorrente; (2) melhorar a qualidade do processo; (3) medir a melhoria.

### 10.1 Um problema recorrente

Depois que a rotina de exclusão começa, dois candidatos reclamam que foram excluídos enquanto ainda participavam de processos seletivos. Marta investiga. Descobre que a rotina usa a data do último contato, que só é atualizada quando um consultor registra uma ligação ou um e-mail. Os consultores muitas vezes se comunicam por mensagens em redes profissionais que não ficam registradas no sistema de recrutamento. Os dados eram, portanto, inexatos: candidatos ativos pareciam inativos. O problema é uma falha de qualidade dos dados que faz um controle de privacidade agir sobre as pessoas erradas.

### 10.2 Causa raiz e correção

A causa raiz é que a noção de contato do sistema não corresponde à prática real. Marta trabalha com os consultores para acrescentar um botão simples, marcar como ativo, que atualiza a data sem registrar detalhes, e a rotina de exclusão passa a avisar o consultor responsável sete dias antes de excluir um perfil. O consultor pode confirmar ou prorrogar, informando um motivo. Ela observa que o artigo 5(1)(d) do GDPR, como o princípio da qualidade dos dados do art. 6º, V, da LGPD, exige dados exatos, e que a exatidão importa tanto para as decisões automáticas de retenção quanto para o conteúdo.

### 10.3 Verificações de qualidade

Marta acrescenta verificações de qualidade: um relatório mensal dos perfis com candidatura ativa, mas com o último contato há mais de três meses, e uma revisão por amostragem de cinco perfis por consultor a cada trimestre. O primeiro relatório encontra trinta e um perfis nessa situação, que os consultores atualizam a partir das próprias listas. Ela explica que as verificações de qualidade pegam os problemas antes que causem danos, como uma exclusão indevida ou, no sentido oposto, a guarda de candidatos que deveriam ter sido excluídos porque alguém atualizou a data sem contato real.

### 10.4 Medir a melhoria

No trimestre seguinte, nenhum candidato é excluído indevidamente, e os perfis sinalizados pelo relatório mensal caem de trinta e um para seis. Os consultores dizem que os e-mails de aviso são úteis. Marta também monitora o mau uso do botão marcar como ativo, examinando por amostragem se os perfis prorrogados têm um motivo registrado. A Sra. Lin observa que bons controles de privacidade dependem de bons dados e de bons processos, e que a solução de problemas costuma revelar uma distância entre como um sistema supõe que o trabalho acontece e como as pessoas de fato trabalham.

### Exemplo resolvido

Marta liga as exclusões indevidas a datas de último contato inexatas, acrescenta um botão para marcar como ativo e avisos com sete dias de antecedência, introduz verificações de qualidade mensais e trimestrais e vê os perfis sinalizados caírem de trinta e um para seis.

> **Caso sintético.** O problema é sintético; o artigo 5(1)(d) do GDPR e o art. 6º, V, da LGPD são reais.

### Erros e limites

Botões novos podem ser mal usados para guardar dados indefinidamente; examine seu uso por amostragem.

### Exercícios

- **EX046 — Causa das exclusões.** Por que candidatos ativos foram excluídos? *Rubrica:* 3 = a data do último contato não era atualizada para mensagens em redes profissionais;; 2 = menciona a data;; 1 = nada;; 0 = nenhuma.
- **EX047 — Prazo do aviso.** Com quanto tempo de antecedência o consultor é avisado? *Rubrica:* 3 = sete dias;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX048 — Princípio da exatidão.** Que artigo exige dados exatos? *Rubrica:* 3 = artigo 5(1)(d);; 2 = correta;; 1 = outro;; 0 = nenhuma.
- **EX049 — Perfis sinalizados.** Como mudaram os perfis sinalizados? *Rubrica:* 3 = de trinta e um para seis;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX050 — Mau uso do botão.** Como o mau uso de marcar como ativo é conferido? *Rubrica:* 3 = amostragem dos perfis prorrogados em busca de motivos;; 2 = menciona amostragem;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Laboratório supervisionado

### Objetivos de aprendizagem

Você vai (1) revisar a resposta a um pedido de acesso em busca de dados de terceiros; (2) aplicar a ocultação corretamente; (3) explicar as decisões de ponderação.

### 11.1 A tarefa do laboratório

O laboratório supervisionado de Marta usa uma resposta sintética a um pedido de acesso preparada para uma candidata rejeitada, Rosa Lindqvist. A resposta inclui anotações de entrevista, e-mails, um trecho de chat interno, uma lista de finalistas e uma referência. O artigo 15(4) do GDPR diz que o direito de obter uma cópia não pode prejudicar os direitos e as liberdades de terceiros, então a Halden precisa considerar as informações de terceiros antes de entregar os documentos. O laboratório confere que ocultações foram feitas e se nomes de outras pessoas continuam visíveis; além disso, Marta lê cada linha por inteiro em busca de pistas indiretas.

### 11.2 Resultados do laboratório

O laboratório encontra seis linhas, com quatro ocultações já feitas e três nomes de terceiros ainda visíveis: um membro da banca, Tom Becker, nas anotações da entrevista; uma referência, Ana Ruiz; e um colega, Jon Patel, que reuniu o retorno. Marta não oculta simplesmente os três. A Sra. Lin pede que ela considere o papel de cada pessoa. Funcionários que agiram na sua função profissional, como o membro da banca e o colega, muitas vezes podem ser nomeados, porque a candidata tem interesse legítimo em saber quem a avaliou. É o contexto que decide cada caso, e não uma regra única.

### 11.3 Ponderar a referência

A referência é diferente. Ana Ruiz deu uma opinião em confiança, como ex-gestora. Marta considera se a referência foi dada na expectativa de continuar confidencial, se a candidata já sabe quem é a referência e se o conteúdo pode ser compartilhado sem o nome. Ela recomenda divulgar o conteúdo da referência e perguntar à referência se ela se opõe a que seu nome seja compartilhado, seguindo a abordagem das Diretrizes 01/2022 do EDPB para ponderar os direitos de terceiros. A resposta da referência é registrada, e a decisão final sobre o nome espera por ela.

### 11.4 Documentar as decisões

Marta registra cada decisão de ocultação com o motivo: os nomes dos outros candidatos da lista de finalistas são ocultados porque são terceiros sem relação com o pedido; os nomes dos funcionários ficam visíveis porque eles agiram em funções profissionais; e o nome da referência aguarda a resposta dela. Ela observa que a ocultação indiscriminada pode tornar a resposta inútil e injusta com a candidata, enquanto a falta de ocultação pode prejudicar terceiros. A Sra. Lin aprova o raciocínio e observa que documentar as decisões permite defender a resposta se a candidata ou a autoridade a questionarem.

### Laboratório — Nomes de terceiros numa resposta de acesso

```python
"""Check a synthetic access-request export for unredacted third-party names (stdlib only)."""
import re
candidate = "Rosa Lindqvist"
third = ["Tom Becker", "Ana Ruiz", "Jon Patel"]
doc = [
    "Interview notes: Rosa Lindqvist strong on scheduling; panel member Tom Becker agreed.",
    "Email from [REDACTED] to Rosa Lindqvist confirming second interview.",
    "Reference received from Ana Ruiz, former manager, positive.",
    "Internal chat: [REDACTED] asked whether Rosa Lindqvist could start in May.",
    "Shortlist: Rosa Lindqvist, [REDACTED], [REDACTED].",
    "Feedback compiled by Jon Patel for the hiring manager.",
]
left = [(i + 1, n) for i, line in enumerate(doc) for n in third if n in line]
red = sum(line.count("[REDACTED]") for line in doc)
print(f"lines {len(doc)}; redactions made {red}; third-party names still visible {len(left)}")
for i, n in left: print(f"  line {i}: {n}")
```

Execute com `python3 lab_redact.py`. Saída verificada:

```text
lines 6; redactions made 4; third-party names still visible 3
  line 1: Tom Becker
  line 3: Ana Ruiz
  line 6: Jon Patel
```

### Exemplo resolvido

Marta encontra três nomes de terceiros ainda visíveis numa resposta sintética de seis linhas, mantém os nomes dos funcionários que agiram profissionalmente, oculta os outros candidatos, consulta a referência e documenta cada decisão.

> **Caso sintético.** A resposta é sintética; o artigo 15(4) do GDPR e as Diretrizes 01/2022 do EDPB são reais.

### Erros e limites

Uma busca por nomes deixa passar identificadores indiretos, como cargos; leia os documentos por inteiro.

### Exercícios

- **EX051 — Nomes visíveis.** Quantos nomes de terceiros continuavam visíveis? *Rubrica:* 3 = três;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX052 — Nomes dos funcionários.** Por que os nomes dos funcionários muitas vezes podem ficar? *Rubrica:* 3 = agiram em funções profissionais;; 2 = menciona função;; 1 = nada;; 0 = nenhuma.
- **EX053 — Abordagem da referência.** O que Marta recomendou quanto à referência? *Rubrica:* 3 = divulgar o conteúdo; perguntar sobre o nome;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX054 — Nomes da lista de finalistas.** Por que os outros candidatos foram ocultados? *Rubrica:* 3 = são terceiros sem relação com o pedido;; 2 = correta;; 1 = nada;; 0 = nenhuma.
- **EX055 — Ocultação indiscriminada.** Por que evitar a ocultação indiscriminada? *Rubrica:* 3 = torna as respostas inúteis e injustas;; 2 = menciona justiça;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Portfólio de prática e revisão final

### Objetivos de aprendizagem

Você vai (1) montar um portfólio de prática; (2) refletir sobre as evidências de competência; (3) planejar o desenvolvimento contínuo.

### 12.1 Montar o portfólio

Marta monta seu portfólio a partir dos seis meses na Halden: o mapa de dados, a análise da retenção, o fluxo e o desenho do registro de pedidos de acesso, o registro de verificação, a análise da violação, o caso do cliente sobre deficiências, a solução do problema de qualidade e o laboratório de ocultação. Cada item tem uma nota de capa que explica o problema, o que ela fez, as evidências e o resultado. Ela retira todos os nomes reais e usa exemplos sintéticos do começo ao fim, conferindo que nenhum item permitiria identificar um candidato ou funcionário da Halden; a Sra. Lin confere a anonimização.

### 12.2 Evidências de competência

A Sra. Lin revisa o portfólio diante dos resultados esperados do curso. Marta mostra que sabe mapear o tratamento, analisar a retenção, conduzir os fluxos de direitos, verificar controles, avaliar violações, lidar com tensões éticas e se comunicar com gestores. A Sra. Lin aponta duas áreas de crescimento: o raciocínio jurídico de Marta sobre verificações de antecedentes ainda é hesitante, e seus scripts dependem de ajuda. Marta aceita o retorno e observa que conhecer os limites da própria competência faz parte da prática profissional, sobretudo numa área em que os erros afetam pessoas.

### 12.3 Revisão final

Na reunião de revisão final, o diretor-geral da Halden confirma que as mudanças continuam em vigor: a exclusão de currículos roda toda noite, com avisos; o banco de talentos foi renovado; os pedidos de acesso são registrados de forma central; as anotações impressas de entrevistas acabaram; e os dados de diversidade ficam guardados à parte. A responsável pela proteção de dados apresenta o registro de verificação com dois trimestres de resultados. Marta apresenta as lacunas restantes, cada uma com responsável: contratos de verificação de antecedentes que precisam de revisão e uma integração com uma rede profissional ainda não avaliada quanto aos avisos do artigo 14.

### 12.4 Desenvolvimento contínuo

Marta planeja os próximos passos: estudar as regras sobre registros criminais nas verificações de antecedentes, praticar scripts simples e entrar numa rede regional de profissionais de privacidade. Ela também se oferece para revisar a integração com a rede profissional, aplicando o raciocínio sobre o artigo 14 que aprendeu no segundo capítulo do curso. A Halden lhe oferece um cargo de meio período como coordenadora de privacidade. A Sra. Lin encerra o curso lembrando que os hábitos profissionais mais valiosos que Marta mostrou foram conferir a prática diante da política, declarar as evidências com honestidade e encontrar soluções que respeitam os candidatos.

### Exemplo resolvido

Marta reúne um portfólio sintético de oito itens com notas de capa, aceita o retorno sobre raciocínio jurídico e scripts, confirma que as mudanças continuam em vigor na Halden e planeja seu desenvolvimento contínuo.

> **Caso sintético.** O portfólio é sintético.

### Erros e limites

Portfólios podem exagerar a contribuição individual; dê o crédito correto aos colegas.

### Exercícios

- **EX056 — Itens do portfólio.** Cite três itens do portfólio. *Rubrica:* 3 = mapa de dados, análise da retenção, fluxo de acesso, registro, violação, caso ético, solução de problemas, ocultação;; 2 = três;; 1 = um;; 0 = nenhuma.
- **EX057 — Nota de capa.** O que cada nota de capa explica? *Rubrica:* 3 = o problema, as ações, as evidências e o resultado;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX058 — Áreas de crescimento.** Que duas áreas de crescimento a Sra. Lin identificou? *Rubrica:* 3 = raciocínio jurídico sobre antecedentes e scripts;; 2 = as duas;; 1 = uma;; 0 = nenhuma.
- **EX059 — Lacunas restantes.** Cite uma lacuna restante na Halden. *Rubrica:* 3 = contratos de verificação de antecedentes; avisos do artigo 14 da rede profissional;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX060 — Próximo cargo.** Que cargo a Halden oferece a Marta? *Rubrica:* 3 = coordenadora de privacidade em meio período;; 2 = correta;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Marta Silva, a Sra. Grace Lin, a Northgate Professional Academy, a Halden Recruitment e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Uma anotação de entrevista alterada ou errada que leva à rejeição de um candidato.

**EX002.** Também pergunta se os dados devem ser coletados, para que finalidade e por quanto tempo.

**EX003.** Guardando currículos por anos sem motivo, contra a limitação da conservação.

**EX004.** Cerca de metade.

**EX005.** Todos os notebooks eram criptografados, exceto duas máquinas antigas.

**EX006.** Quando os dados do candidato vêm de outras fontes, como sites de vagas.

**EX007.** As referências, cujos nomes e opiniões são registrados.

**EX008.** Um controlador separado.

**EX009.** As Diretrizes 07/2020 do EDPB sobre os conceitos de controlador e operador.

**EX010.** Ser consultados antes de o currículo ir para um cliente específico.

**EX011.** O pedido de um consultor para consultar a situação da candidatura de um amigo.

**EX012.** Ela não pode mudar configurações do sistema por conta própria.

**EX013.** Usando exemplos sintéticos ou recortando a imagem até a configuração.

**EX014.** A equipe relata problemas mais abertamente quando confia que os achados não serão usados para culpá-la.

**EX015.** O que lhe pediram, o que ela decidiu, por quê e quem aprovou.

**EX016.** Ficavam guardadas com os nomes, embora só as estatísticas anônimas as usem.

**EX017.** 1.792 de 2.500 (71,7%).

**EX018.** 216.

**EX019.** Consentimento, específico e revogável.

**EX020.** Artigo 10.

**EX021.** Cada exportação cria uma nova cópia que precisa ser protegida e excluída.

**EX022.** Dezessete aceitaram, dois não puderam ser confirmados e um foi para um endereço pessoal.

**EX023.** A falta de registro do aceite do candidato para ser apresentado.

**EX024.** Na amostra.

**EX025.** Rotineiramente.

**EX026.** 7 de 36 (19,4%).

**EX027.** 21 dias.

**EX028.** Buscas nas caixas de e-mail de vários consultores e espera pelas verificações de referências.

**EX029.** Finalidades e prazos de retenção (também destinatários e fonte).

**EX030.** Dentro do primeiro mês, com comunicação ao candidato.

**EX031.** Transparência e lealdade.

**EX032.** Os dados de diversidade ainda eram copiados por um script antigo de importação.

**EX033.** A cobertura da autenticação multifator e uma amostra das apresentações a clientes.

**EX034.** Dez de dez.

**EX035.** Um registro que nunca mostra problemas perde a credibilidade.

**EX036.** Era criptografado, então os dados eram ininteligíveis sem a chave.

**EX037.** Nomes, empregadores atuais, pretensões salariais e a informação de saúde de uma candidata.

**EX038.** Em até 72 horas, pelo artigo 33.

**EX039.** A informação sobre a deficiência cria um risco elevado para ela.

**EX040.** A consultora seguia a prática que todos usavam.

**EX041.** As decisões necessárias, cada uma com razão, custo e risco de não agir.

**EX042.** Perguntar a cada candidato e compartilhar só a adaptação necessária, não a condição.

**EX043.** Nomear pessoas desencoraja os outros de comunicar problemas.

**EX044.** Em meses, não com expressões vagas.

**EX045.** Com cinco personas sintéticas de candidatos.

**EX046.** A data do último contato não era atualizada para mensagens fora do sistema.

**EX047.** Sete dias.

**EX048.** Artigo 5(1)(d).

**EX049.** De trinta e um para seis.

**EX050.** Examinando por amostragem se os perfis prorrogados têm um motivo registrado.

**EX051.** Três.

**EX052.** Agiram na sua função profissional.

**EX053.** Compartilhar o conteúdo e perguntar à referência sobre a divulgação do seu nome.

**EX054.** São terceiros sem relação com o pedido.

**EX055.** Pode tornar a resposta inútil e injusta com a candidata.

**EX056.** O mapa de dados, a análise da retenção e o laboratório de ocultação.

**EX057.** O problema, o que ela fez, as evidências e o resultado.

**EX058.** O raciocínio jurídico sobre verificações de antecedentes e a escrita autônoma de scripts.

**EX059.** Contratos de verificação de antecedentes que precisam de revisão.

**EX060.** Um cargo de meio período como coordenadora de privacidade.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 15, de 24 de abril de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Aprova o Regulamento de Comunicação de Incidente de Segurança*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Data Protection Board. (2021). *Guidelines 07/2020 on the concepts of controller and processor in the GDPR* (Version 2.0 adopted 7 July 2021; Version 2.1, 20 September 2022). <https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en>
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- European Data Protection Board. (2023). *Guidelines 9/2022 on personal data breach notification under GDPR* (Version 2.0, adopted 28 March 2023). <https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
