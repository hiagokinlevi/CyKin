# Privacidade e Proteção de Dados: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 142, curso de pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais em pós-graduação que lideram um programa de privacidade numa empresa regulada e com operações em mais de um país.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios simulam a detecção de fraudes com diferentes níveis de detalhe da localização, analisam um teste A/B de banner de consentimento e comparam indicadores de risco de privacidade com os limites do conselho, sempre sobre dados sintéticos. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma gerente de privacidade ao longo de um curso de pós-graduação: tomada de decisão, prática atual, evidências sobre a necessidade, risco e ética, alternativas de design do consentimento, uma avaliação A/B controlada, integração organizacional, casos difíceis, indicadores para o conselho e garantia, leitura crítica de pesquisas, um projeto aplicado de retenção e a revisão final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Priscila Andrade** | Estudante de pós-graduação e gerente de privacidade | Inventada |
| **Dra. Helen Ward** | Orientadora | Inventada |
| **Ashgrove School of Management** | Escola fictícia | Inventada |
| **Corvina Pay** | Empresa fictícia de pagamentos, 900 funcionários, Brasil e Portugal | Inventada |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR); Lei nº 13.709/2018 (LGPD); Resolução CD/ANPD nº 15/2024; Diretiva 2002/58/CE (ePrivacy), artigo 5(3); Diretrizes 05/2020, 07/2020 e 9/2022 do EDPB; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 27701:2025; Acquisti et al. (2015), [doi:10.1126/science.aaa1465](https://doi.org/10.1126/science.aaa1465); Sweeney (2002); Narayanan e Shmatikov (2008); Dwork e Roth (2014); Solove (2006); Nissenbaum (2004). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem

Você vai (1) enquadrar as decisões de privacidade como escolhas sob incerteza; (2) separar as restrições legais dos trade-offs de risco; (3) documentar as decisões para fins de responsabilização.

### 1.1 A profissional e a empresa

Priscila Andrade é gerente de privacidade da fictícia Corvina Pay, uma empresa de pagamentos com 900 funcionários que atende clientes no Brasil e em Portugal. Ela se matricula num curso de pós-graduação de dois anos na fictícia Ashgrove School of Management, orientada pela Dra. Helen Ward. A Corvina precisa cumprir a LGPD no Brasil e o GDPR em Portugal. O dia a dia de Priscila envolve decisões sobre modelos antifraude, consentimento para marketing, fornecedores e pedidos de titulares, muitas vezes tomadas às pressas e com informação incompleta sobre riscos e benefícios. A maioria chega como pedido urgente de produto.

### 1.2 Decisões sob incerteza

A Dra. Ward pede que Priscila descreva uma decisão recente. A equipe antifraude queria a localização GPS precisa de cada pagamento com cartão. Priscila não sabia quanto o GPS melhoraria a detecção, como os clientes reagiriam nem como os reguladores veriam a medida. Ela aprende a enquadrar decisões assim com opções, resultados, probabilidades e valores, mesmo que as estimativas sejam grosseiras. Registrar a incerteza por escrito permite reduzi-la, por exemplo testando se dados menos precisos funcionam tão bem antes de coletar a localização exata de todos os clientes.

### 1.3 Restrições versus trade-offs

Priscila separa as restrições dos trade-offs. Restrições são exigências que não podem ser negociadas, como ter uma base legal pelo artigo 6 do GDPR ou pelo art. 7º da LGPD e respeitar a necessidade. Trade-offs são escolhas entre opções lícitas, como a quantidade de dados a coletar para a prevenção de fraudes. Ela observa que os gestores costumam tratar as exigências legais como custos a ponderar, o que é um erro de categoria. O prazo de 72 horas do GDPR para notificar violações é uma restrição; o nível de detalhe da localização a guardar é um trade-off. Esclarecer a diferença cedo evita debates inúteis.

### 1.4 Registro das decisões

Priscila introduz na Corvina um registro de decisão com sete campos: a pergunta, as opções consideradas, as evidências, as restrições legais, a opção escolhida, o risco residual e o responsável, além de uma data para conferir o resultado esperado. Ela o usa na decisão sobre o GPS. A responsabilização pelo artigo 5(2) do GDPR e pelo art. 6º, X, da LGPD exige demonstrar a conformidade, e os registros de decisão são evidências fortes. A Dra. Ward observa que eles também melhoram as decisões futuras, porque a organização pode comparar o que esperava com o que de fato aconteceu e aprender com a diferença.

### Exemplo resolvido

Priscila enquadra o pedido de GPS como uma decisão sob incerteza, separa as restrições de base legal dos trade-offs de coleta e introduz um registro de decisão.

> **Caso sintético.** A Corvina, a Ashgrove e todas as pessoas são sintéticas; os artigos 5(2) e 6 do GDPR e os arts. 6º e 7º da LGPD são reais.

### Erros e limites

Probabilidades grosseiras podem criar uma falsa precisão; mostre intervalos.

### Exercícios

- **EX001 — Restrição ou trade-off.** Ter uma base legal é um trade-off ou uma restrição? *Rubrica:* 3 = uma restrição que não pode ser negociada;; 2 = restrição sem justificativa;; 1 = trade-off;; 0 = nenhuma.
- **EX002 — Reduzir a incerteza.** Como a Corvina poderia reduzir a incerteza sobre o valor do GPS? *Rubrica:* 3 = testar se dados menos precisos funcionam tão bem antes de coletar a localização exata;; 2 = menciona testes;; 1 = coletar de qualquer forma;; 0 = nenhuma.
- **EX003 — Campos do registro de decisão.** Liste os campos do registro de decisão de Priscila. *Rubrica:* 3 = pergunta, opções, evidências, restrições, escolha, risco residual, responsável;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX004 — Aprender com os registros.** Como os registros de decisão melhoram as decisões futuras? *Rubrica:* 3 = comparar expectativas com resultados ensina a organização;; 2 = menciona aprendizado;; 1 = só conformidade;; 0 = nenhuma.
- **EX005 — Duas leis.** Que leis regem o tratamento da Corvina e onde? *Rubrica:* 3 = a LGPD no Brasil, o GDPR em Portugal;; 2 = uma;; 1 = errada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Privacidade e proteção de dados: prática atual

### Objetivos de aprendizagem

Você vai (1) mapear a prática atual de privacidade numa empresa de pagamentos; (2) comparar as obrigações do GDPR e da LGPD; (3) identificar lacunas em relação às boas práticas.

### 2.1 Mapear a prática

Priscila mapeia o programa de privacidade da Corvina: um encarregado pelo tratamento de dados (o DPO, na terminologia do GDPR), um registro das operações de tratamento, um processo de DPIA, uma equipe de atendimento aos titulares, contratos com fornecedores e treinamento. Ela entrevista os líderes de equipe para ver como cada peça funciona na prática. Descobre que o registro das operações existe, mas não é atualizado há um ano, que dois fornecedores nem constam dele e que as DPIAs só são feitas para produtos novos, e não para mudanças em produtos existentes, como o modelo antifraude.

### 2.2 Comparar as leis

Priscila monta uma comparação das obrigações do GDPR e da LGPD. Ambas exigem bases legais, transparência, segurança e atendimento aos direitos. A LGPD lista dez bases legais no art. 7º, entre elas a proteção do crédito, relevante para a Corvina; o GDPR usa seis bases no artigo 6. Para violações, o GDPR fixa a notificação à autoridade em até 72 horas; no Brasil, o art. 48 da LGPD remete o prazo à ANPD, e a Resolução CD/ANPD nº 15/2024 o fixou em três dias úteis, em seu art. 6º, contados do conhecimento de que dados pessoais foram afetados. Ela desenha processos que atendam à exigência mais rigorosa em cada ponto, e essa passa a ser o padrão do grupo.

### 2.3 Estruturas de referência

Priscila compara o programa da Corvina com o NIST Privacy Framework 1.0 e com a ISO/IEC 27701:2025. As funções do framework do NIST mostram que a Corvina é forte em Protect-P, mas mais fraca em Identify-P, porque o inventário está desatualizado. A ISO/IEC 27701 espera processos documentados de sistema de gestão, que a Corvina tem em parte. Por ora, ela usa as estruturas como listas de verificação organizadas, e não como metas de certificação. O NIST Privacy Framework a ajuda a descrever ao conselho os resultados desejados, e os controles da ISO/IEC 27701 a ajudam a conferir se a gestão de fornecedores e o treinamento funcionam na prática.

### 2.4 Lacunas

Priscila lista as lacunas: um registro das operações desatualizado, DPIAs que não são acionadas por mudanças, contratos com fornecedores sem cláusulas claras de exclusão e um treinamento genérico. Ela as classifica por risco. O inventário desatualizado vem em primeiro lugar, porque os outros processos dependem dele. Ela apresenta a lista ao comitê executivo da Corvina com um plano de doze meses, e cada lacuna recebe um responsável, como o diretor de produto para as mudanças não revisadas. A Dra. Ward comenta que uma lista de lacunas crível é específica, priorizada e com donos, e não um rol de tudo o que poderia melhorar.

### Exemplo resolvido

Priscila mapeia o programa da Corvina, compara as obrigações do GDPR e da LGPD, usa o NIST Privacy Framework e a ISO/IEC 27701 como listas de verificação e prioriza quatro lacunas num plano de doze meses.

> **Caso sintético.** O programa da Corvina é sintético; o artigo 6 do GDPR, os arts. 7º e 48 da LGPD, a Resolução CD/ANPD nº 15/2024, o NIST Privacy Framework 1.0 e a ISO/IEC 27701:2025 são reais.

### Erros e limites

Comparações entre leis simplificam; os regulamentos das autoridades nacionais acrescentam detalhes.

### Exercícios

- **EX006 — Lacuna no acionamento da DPIA.** Que lacuna Priscila encontrou na prática de DPIA? *Rubrica:* 3 = DPIAs só para produtos novos, não para mudanças;; 2 = menciona mudanças;; 1 = nenhuma;; 0 = nenhuma.
- **EX007 — Bases da LGPD.** Quantas bases legais o art. 7º da LGPD lista, e qual serve a pagamentos? *Rubrica:* 3 = dez; a proteção do crédito é relevante;; 2 = só o número;; 1 = errado;; 0 = nenhuma.
- **EX008 — Exigência mais rigorosa.** Como Priscila trata as diferenças entre as leis? *Rubrica:* 3 = desenha processos que atendem à exigência mais rigorosa;; 2 = menciona a mais rigorosa;; 1 = escolhe uma;; 0 = nenhuma.
- **EX009 — Papel das estruturas.** Como Priscila usa as estruturas de referência? *Rubrica:* 3 = como listas de verificação organizadas, não metas de certificação;; 2 = menciona lista;; 1 = certificar;; 0 = nenhuma.
- **EX010 — Primeira lacuna.** Por que o inventário desatualizado vem em primeiro lugar? *Rubrica:* 3 = os outros processos dependem dele;; 2 = menciona dependência;; 1 = aleatório;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Privacidade e proteção de dados: evidências especializadas

### Objetivos de aprendizagem

Você vai (1) testar com evidências se os dados são necessários; (2) comparar o desempenho de um modelo com menos dados; (3) aplicar as evidências a uma decisão de minimização.

### 3.1 A questão da necessidade

A minimização exige que os dados sejam adequados, pertinentes e limitados ao necessário, pelo artigo 5(1)(c) do GDPR e pelo princípio da necessidade do art. 6º, III, da LGPD. A equipe antifraude argumenta que o GPS preciso é necessário. Priscila pede evidências. Com um cientista de dados, ela desenha uma simulação sobre 20.000 transações sintéticas que compara três regras: GPS completo com novidade do dispositivo, localização por cidade com novidade do dispositivo e apenas a novidade do dispositivo. O objetivo é medir o que a localização precisa acrescenta, e as três regras rodam sobre o mesmo histórico.

### 3.2 Resultados

O laboratório mostra que o GPS completo com dispositivo e a localização por cidade com dispositivo detectam os mesmos 43,1% das fraudes, com os mesmos 90 alarmes falsos. Neste cenário sintético, o GPS não acrescenta nada além de saber que o pagamento vem de uma cidade incomum. Usar apenas a novidade do dispositivo detecta mais fraudes, 56,4%, mas produz 1.572 alarmes falsos, que bloqueariam muitos clientes legítimos. A localização por cidade fornece, portanto, o sinal útil sem rastreamento preciso. Como guardar as coordenadas exatas não acrescenta detecção, o rastreamento preciso não pode ser chamado de necessário.

### 3.3 Interpretar as evidências

Priscila é cuidadosa. A simulação é sintética e se apoia em premissas com que a equipe antifraude concordou. Ela mostra que o GPS pode ser desnecessário, e não que nunca ajude. Priscila propõe um piloto controlado com dados reais, porém pseudonimizados, no ambiente seguro da equipe antifraude, comparando por três meses as regras por cidade e por GPS. Até haver resultados, a Corvina usa a localização por cidade. Ela registra isso como uma decisão tomada com base no princípio da necessidade, com as evidências, o plano do piloto e uma revisão prevista para seis meses depois.

### 3.4 Cultura de evidências

A Dra. Ward observa que Priscila trocou a opinião pela evidência na conversa. A equipe antifraude, inicialmente resistente, aceita o piloto porque ele pode lhe dar razão. Priscila nota que os argumentos de necessidade ficam mais fortes quando apoiados em dados e que as equipes de privacidade ganham credibilidade quando ajudam a testar as alegações, em vez de simplesmente rejeitá-las. A equipe antifraude agora propõe seus próprios testes antes de pedir dados novos, e o pedido seguinte, de acesso à lista de contatos, é retirado depois que um pequeno teste não mostra benefício algum.

### Laboratório — Detecção de fraudes com GPS completo, localização por cidade ou só o dispositivo

```python
# Does a fraud rule need precise location? Compare detection with full GPS, city-level and no location (synthetic).
import random
r = random.Random(21)
tx = []
for _ in range(20000):
    fraud = r.random() < 0.01
    far = r.random() < (0.70 if fraud else 0.05)          # far from usual city
    newdev = r.random() < (0.60 if fraud else 0.08)       # new device
    odd_gps = far and r.random() < 0.5                    # GPS adds detail only within 'far' cases
    tx.append((fraud, far, newdev, odd_gps))
def score(rule):
    flagged = [t for t in tx if rule(t)]; tp = sum(t[0] for t in flagged); fr = sum(t[0] for t in tx)
    return tp / fr, len(flagged) - tp
for name, rule in [("full GPS + device", lambda t: (t[1] and t[2]) or t[3] and t[2]),
                   ("city-level + device", lambda t: t[1] and t[2]),
                   ("device only", lambda t: t[2])]:
    rec, fp = score(rule); print(f"{name:20s} detects {rec:5.1%} of fraud; false alarms {fp:5d}")
```

Execute com `python3 lab_fraud.py`. Saída verificada:

```text
full GPS + device    detects 43.1% of fraud; false alarms    90
city-level + device  detects 43.1% of fraud; false alarms    90
device only          detects 56.4% of fraud; false alarms  1572
```

### Exemplo resolvido

Priscila mostra que as regras com GPS e por cidade detectam 43,1% das fraudes sintéticas com 90 alarmes falsos, enquanto a detecção só pelo dispositivo eleva os alarmes falsos a 1.572, e adota a localização por cidade até o fim do piloto.

> **Caso sintético.** As transações são sintéticas; o artigo 5(1)(c) do GDPR e o art. 6º da LGPD são reais.

### Erros e limites

Dados sintéticos refletem premissas; pilotos reais podem mostrar resultados diferentes.

### Exercícios

- **EX011 — Valor do GPS.** O que o GPS preciso acrescentou na simulação? *Rubrica:* 3 = nada além da cidade: os mesmos 43,1% de detecção e 90 alarmes falsos;; 2 = menciona ausência de ganho;; 1 = melhorou;; 0 = nenhuma.
- **EX012 — Custo de usar só o dispositivo.** Por que não usar apenas a novidade do dispositivo? *Rubrica:* 3 = 1.572 alarmes falsos bloqueariam muitos clientes legítimos;; 2 = menciona alarmes falsos;; 1 = é a melhor;; 0 = nenhuma.
- **EX013 — Decisão provisória.** O que a Corvina usa até o fim do piloto? *Rubrica:* 3 = a localização por cidade;; 2 = menciona cidade;; 1 = GPS;; 0 = nenhuma.
- **EX014 — Princípio da necessidade.** Que princípios exigem limitar os dados ao necessário? *Rubrica:* 3 = o artigo 5(1)(c) do GDPR e o art. 6º, III, da LGPD;; 2 = um;; 1 = nenhum;; 0 = nenhuma.
- **EX015 — Equipe resistente.** Por que a equipe antifraude aceitou o piloto? *Rubrica:* 3 = ele poderia lhe dar razão;; 2 = menciona justiça;; 1 = foi forçada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Risco e ética avançados

### Objetivos de aprendizagem

Você vai (1) avaliar o risco de privacidade para as pessoas, e não só para a empresa; (2) aplicar a análise ética ao perfilamento; (3) lidar com conflitos de interesse.

### 4.1 Risco para quem

Os registros de riscos corporativos medem o risco para a empresa: multas, reputação, custos. Priscila observa que a lei de proteção de dados se concentra nos riscos aos direitos e liberdades das pessoas. Uma violação que expusesse históricos de transações poderia revelar compras ligadas à saúde, doações religiosas ou apostas, causando dano aos clientes mesmo que as perdas da Corvina fossem pequenas. Ela acrescenta ao registro de riscos uma coluna separada para o dano às pessoas, de modo que as decisões considerem as duas perspectivas. Na proposta de perfilamento, o risco para a empresa é moderado, mas o dano aos clientes é alto.

### 4.2 Ética do perfilamento

A equipe de marketing da Corvina propõe usar os dados de transações para inferir eventos de vida, como gravidez ou perda de emprego, e oferecer produtos financeiros. Priscila analisa a proposta pela integridade contextual: os clientes compartilham dados de transações para fazer pagamentos, e não para ter eventos íntimos de sua vida inferidos. A taxonomia de Solove dá a isso os nomes de uso secundário e agregação. Ela lembra ainda o direito de oposição ao marketing direto, no artigo 21 do GDPR, e os deveres de transparência. Recomenda não inferir eventos sensíveis e propõe, em seu lugar, ofertas mediante adesão, que respeitam a escolha do cliente.

### 4.3 Conflitos de interesse

O encarregado se reporta ao diretor de operações, que também responde pela receita de marketing. Priscila aponta o risco de conflito, já que o artigo 38(6) do GDPR exige que as outras funções do DPO não resultem em conflito de interesses. Ela recomenda que, nos assuntos de privacidade, o encarregado se reporte ao comitê de riscos do conselho. Depois de discussão, o comitê executivo concorda, e a nova linha de reporte passa a valer no trimestre seguinte. A Dra. Ward observa que as estruturas de governança moldam os resultados tanto quanto as decisões individuais, porque determinam quem pode dizer não sem medo de perder o cargo.

### 4.4 Raciocínio ético

Priscila escreve uma nota de ética para a Corvina: considerar o dano às pessoas, respeitar os contextos em que os dados foram compartilhados, preferir a transparência e a escolha e evitar inferências que os clientes achariam invasivas. Ela testa a nota em três decisões passadas e descobre que uma delas, uma segmentação de marketing por categoria de gasto, teria sido desenhada de outra forma. Com a equipe de marketing, revisa a segmentação para usar categorias mais amplas e personalização mediante adesão. Uma categoria como gastos em farmácia vira varejo em geral, e o modelo deixa de sugerir condições de saúde.

### Exemplo resolvido

Priscila acrescenta o dano às pessoas ao registro de riscos, desaconselha inferir eventos de vida a partir de transações, muda a linha de reporte do encarregado para evitar um conflito e escreve uma nota de ética aplicada a decisões passadas.

> **Caso sintético.** As propostas são sintéticas; Solove (2006), Nissenbaum (2004) e os artigos 21 e 38(6) do GDPR são reais.

### Erros e limites

Notas de ética precisam de exemplos para serem usáveis; princípios abstratos são facilmente ignorados.

### Exercícios

- **EX016 — Duas visões de risco.** Por que acrescentar uma coluna para o dano às pessoas? *Rubrica:* 3 = a lei se concentra nos direitos das pessoas, não só nas perdas da empresa;; 2 = menciona pessoas;; 1 = só a empresa;; 0 = nenhuma.
- **EX017 — Inferência de eventos de vida.** Por que desaconselhar a inferência de eventos de vida a partir de transações? *Rubrica:* 3 = rompe as normas do contexto e equivale a uso secundário;; 2 = menciona invasão;; 1 = apoia;; 0 = nenhuma.
- **EX018 — Conflito do encarregado.** Que conflito Priscila identificou para o encarregado? *Rubrica:* 3 = reportar-se a um executivo responsável pela receita de marketing;; 2 = menciona a linha de reporte;; 1 = nenhum;; 0 = nenhuma.
- **EX019 — Artigo 38(6).** O que exige o artigo 38(6) do GDPR? *Rubrica:* 3 = as outras funções do DPO não podem gerar conflito de interesses;; 2 = aproximado;; 1 = errado;; 0 = nenhuma.
- **EX020 — Segmentação revista.** Como a decisão de segmentação foi revista? *Rubrica:* 3 = categorias mais amplas e personalização mediante adesão;; 2 = uma;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Privacidade e proteção de dados: alternativas de design

### Objetivos de aprendizagem

Você vai (1) gerar alternativas para uma interface de consentimento; (2) avaliar as alternativas diante da lei e do comportamento dos usuários; (3) escolher uma alternativa para testar.

### 5.1 O problema do consentimento

O aplicativo da Corvina pede que os clientes aceitem cookies de marketing e ofertas personalizadas. O banner atual mostra um grande botão Aceitar e um pequeno link para as configurações. O artigo 5(3) da Diretiva ePrivacy exige consentimento para cookies não essenciais, e as Diretrizes 05/2020 do EDPB dizem que o consentimento deve ser livre e tão fácil de recusar quanto de dar. Priscila suspeita que o design empurra os clientes para o aceite, já que esconder a recusa atrás de um link de configurações é um sinal de alerta para o EDPB. Ela decide desenhar alternativas e testá-las direito.

### 5.2 Alternativas

A equipe de Priscila desenha três alternativas: A, o banner atual; B, um banner com os botões Aceitar tudo e Rejeitar tudo do mesmo tamanho e cor, além das configurações; C, uma escolha em camadas, com chaves separadas para análise e marketing, todas desligadas por padrão. Ela avalia cada uma pelos critérios legais e pela experiência esperada do usuário. A provavelmente falha no critério da facilidade igual. B e C parecem conformes; C oferece escolha mais granular, mas leva mais tempo. Ela guarda as capturas de tela e os critérios de cada design no plano de teste, para que os revisores vejam exatamente o que os clientes viram.

### 5.3 Percepção comportamental

Acquisti, Brandimarte e Loewenstein (2015) descrevem como os padrões e o enquadramento influenciam as escolhas de privacidade. Priscila espera que a aceitação caia em B e C, porque o design deixa de empurrar o aceite. Ela observa que uma queda na aceitação não é um fracasso: significa que as escolhas refletem melhor as preferências dos clientes. A equipe de marketing se preocupa com menos consentimentos. Priscila argumenta que consentimentos obtidos por indução são frágeis, tanto juridicamente quanto na confiança dos clientes. Um consentimento de que o cliente se arrepende gera revogações, reclamações e talvez a atenção do regulador.

### 5.4 Escolher o que testar

Priscila decide testar A contra B, porque B é a menor mudança com probabilidade de alcançar a conformidade e é fácil de implementar, enquanto C exige mais trabalho de engenharia e será considerado depois, se B funcionar bem. Ela define os resultados: a taxa de aceitação e as revogações em até noventa dias, como medida de arrependimento. Escreve um plano de teste com tamanhos de amostra e método de análise, para que a decisão se apoie em evidências, e não em opiniões. O plano é revisado pelo encarregado antes do início, e o marketing concorda com os critérios de sucesso.

### Exemplo resolvido

Priscila desenha três banners de consentimento, considera o atual não conforme quanto à facilidade igual de recusa, explica por que uma aceitação menor é aceitável e escolhe um teste A/B do banner atual contra botões iguais.

> **Caso sintético.** Os banners são sintéticos; o artigo 5(3) da Diretiva ePrivacy, as Diretrizes 05/2020 do EDPB e Acquisti et al. (2015) são reais.

### Erros e limites

Testes de banner medem comportamento, e não compreensão; acrescente verificações de compreensão se possível.

### Exercícios

- **EX021 — Problema do banner A.** Por que o banner A provavelmente falha? *Rubrica:* 3 = recusar é mais difícil que aceitar;; 2 = menciona facilidade;; 1 = é conforme;; 0 = nenhuma.
- **EX022 — Aceitação menor.** Por que uma queda na aceitação não é um fracasso? *Rubrica:* 3 = as escolhas refletem preferências reais; consentimentos induzidos são frágeis;; 2 = menciona preferências;; 1 = é fracasso;; 0 = nenhuma.
- **EX023 — Por que testar B.** Por que testar B antes de C? *Rubrica:* 3 = menor mudança provavelmente conforme e fácil de implementar;; 2 = menciona simplicidade;; 1 = aleatório;; 0 = nenhuma.
- **EX024 — Medida de arrependimento.** Que resultado mede o arrependimento? *Rubrica:* 3 = revogações em até noventa dias;; 2 = menciona revogações;; 1 = nenhum;; 0 = nenhuma.
- **EX025 — Lei do consentimento para cookies.** Que dispositivo exige consentimento para cookies não essenciais? *Rubrica:* 3 = o artigo 5(3) da Diretiva ePrivacy;; 2 = menciona a ePrivacy;; 1 = só o GDPR;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Privacidade e proteção de dados: avaliação controlada

### Objetivos de aprendizagem

Você vai (1) conduzir um teste A/B de forma ética; (2) estimar uma diferença entre proporções; (3) interpretar resultados comportamentais para a conformidade.

### 6.1 Conduzir o teste

A Corvina mostra aleatoriamente o banner A ou o B a 8.000 novos usuários do aplicativo, 4.000 para cada um, durante duas semanas. Priscila confere se o próprio teste é lícito: o banner A só aparece durante o teste, e os dois banners registram as escolhas corretamente. Ela também limita a análise às escolhas agregadas, e o encarregado aprova o teste. Priscila observa que testar um design menos conforme deve ser algo breve e justificado pela necessidade de medir a melhoria, e por isso o teste termina na data prevista, sem prorrogação, mesmo que o marketing peça mais tempo.

### 6.2 Resultados

O laboratório calcula os resultados. O banner A tem taxa de aceitação de 79,0%; o B, de 57,0%. A diferença é de 22,0 pontos percentuais, com intervalo de 95% de 20,0 a 24,0 pontos e estatística z de 21,1, muito além do acaso. Em noventa dias, as revogações por mil consentimentos são 41 com A e 12 com B. Os clientes que aceitaram com A tiveram mais de três vezes mais chance de mudar de ideia depois. Como o intervalo de confiança da diferença na aceitação, de 20,0 a 24,0 pontos, exclui o zero, a distância entre os banners não é um resultado casual desta amostra.

### 6.3 Interpretação

Priscila interpreta os resultados. O banner A empurrou cerca de um quinto dos usuários para um aceite que uma escolha equilibrada não teria produzido. As revogações mais altas com A sugerem que muitos desses consentimentos não refletiam preferências reais. Do ponto de vista da conformidade, é questionável que os consentimentos obtidos com A sejam livres. Do ponto de vista do negócio, B produz consentimentos em menor número, mas mais duradouros. Ela recomenda adotar B imediatamente, porque os consentimentos extras de A carregam um custo jurídico e de reputação que a taxa de aceitação, sozinha, esconde.

### 6.4 Comunicar os resultados

Os líderes de marketing ficam decepcionados com a aceitação menor. Priscila apresenta as evidências: B é conforme, A provavelmente não, e os consentimentos de B são mais estáveis. Ela também estima que o alcance do marketing cai menos do que a aceitação sugere, porque menos pessoas revogam. A Dra. Ward observa que a avaliação controlada transforma um debate de valores numa decisão baseada em evidências, mais fácil de aceitar pelos líderes mesmo quando o resultado desagrada. O resumo de uma página mostra as duas taxas de aceitação, as duas de revogação e uma única recomendação.

### Laboratório — Teste A/B do banner de consentimento

```python
# Consent banner A/B test: A has "Accept" prominent; B gives "Reject all" equal prominence. Two-proportion z-test.
import math
na, ka, nb, kb = 4000, 3160, 4000, 2280
pa, pb = ka / na, kb / nb; p = (ka + kb) / (na + nb)
z = (pa - pb) / math.sqrt(p * (1 - p) * (1 / na + 1 / nb))
se = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
print(f"A accept rate {pa:.1%}; B accept rate {pb:.1%}; difference {pa-pb:.1%} (95% CI {pa-pb-1.96*se:.1%} to {pa-pb+1.96*se:.1%}); z = {z:.1f}")
wa, wb = 130, 27  # synthetic 90-day follow-up: withdrawals among consenting users
print(f"withdrawals within 90 days per 1,000 consents: A {1000*wa/ka:.0f} vs B {1000*wb/kb:.0f}")
```

Execute com `python3 lab_ab.py`. Saída verificada:

```text
A accept rate 79.0%; B accept rate 57.0%; difference 22.0% (95% CI 20.0% to 24.0%); z = 21.1
withdrawals within 90 days per 1,000 consents: A 41 vs B 12
```

### Exemplo resolvido

Priscila encontra aceitação de 79,0% com o banner A contra 57,0% com botões iguais (diferença de 22,0 pontos, IC de 95% de 20,0 a 24,0) e revogações de 41 contra 12 por mil, e recomenda o banner B.

> **Caso sintético.** Os usuários e as escolhas são sintéticos.

### Erros e limites

Duas semanas podem não captar o comportamento sazonal; repita o teste mais tarde.

### Exercícios

- **EX026 — Diferença na aceitação.** Qual foi a diferença de aceitação entre A e B? *Rubrica:* 3 = 22,0 pontos (IC de 95% de 20,0 a 24,0);; 2 = aproximadamente;; 1 = errada;; 0 = nenhuma.
- **EX027 — Razão das revogações.** Como as revogações se compararam? *Rubrica:* 3 = 41 contra 12 por mil, mais de três vezes maior com A;; 2 = só os números;; 1 = nada;; 0 = nenhuma.
- **EX028 — Ética do teste.** Por que exibir o banner A durante o teste precisa ser breve? *Rubrica:* 3 = ele é provavelmente menos conforme, justificado só para medir a melhoria;; 2 = menciona conformidade;; 1 = sem limite;; 0 = nenhuma.
- **EX029 — Consentimento duradouro.** Que benefício de negócio o banner B oferece? *Rubrica:* 3 = consentimentos em menor número, mas mais duradouros;; 2 = menciona estabilidade;; 1 = nenhum;; 0 = nenhuma.
- **EX030 — Dúvida sobre a liberdade.** Por que os consentimentos obtidos com A são questionáveis? *Rubrica:* 3 = o design empurrou os usuários, e as revogações maiores sugerem que as escolhas não refletiam preferências;; 2 = menciona indução;; 1 = são válidos;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Priscila Andrade, a Dra. Helen Ward, a Ashgrove School of Management, a Corvina Pay e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Uma restrição: tratar dados sem base legal não é uma opção a ponderar.

**EX002.** Testando se a localização por cidade detecta fraudes tão bem quanto o GPS.

**EX003.** Pergunta, opções, evidências, restrições legais, opção escolhida, risco residual e responsável.

**EX004.** Permitem que a organização compare o que esperava com o que aconteceu.

**EX005.** A LGPD para as operações brasileiras e o GDPR para as operações portuguesas.

**EX006.** As DPIAs não eram acionadas por mudanças significativas no tratamento existente.

**EX007.** Dez, entre elas a proteção do crédito, relevante para uma empresa de pagamentos.

**EX008.** Ela desenha cada processo para atender à mais rigorosa das duas exigências.

**EX009.** Como listas de verificação organizadas para encontrar lacunas.

**EX010.** Porque as DPIAs, o atendimento aos titulares e a gestão de fornecedores dependem de um inventário exato.

**EX011.** Nada; a detecção e os alarmes falsos foram iguais aos da localização por cidade.

**EX012.** Produz 1.572 alarmes falsos, prejudicando muitos clientes legítimos.

**EX013.** A localização por cidade.

**EX014.** A minimização do GDPR, no artigo 5(1)(c), e a necessidade da LGPD, no art. 6º, III.

**EX015.** Porque um teste justo poderia confirmar o ponto de vista dela.

**EX016.** A lei de proteção de dados avalia os riscos às pessoas, que os registros centrados na empresa deixam passar.

**EX017.** Os clientes compartilham dados para pagar, não para ter eventos íntimos inferidos; é uso secundário e agregação.

**EX018.** O encarregado se reportava ao executivo que também respondia pela receita de marketing.

**EX019.** Que as outras funções e deveres do DPO não resultem em conflito de interesses.

**EX020.** Com categorias de gasto mais amplas e personalização mediante adesão.

**EX021.** A recusa é menos visível que o aceite, então o consentimento não é tão fácil de recusar.

**EX022.** Uma aceitação menor indica escolha mais livre; o consentimento induzido é frágil jurídica e reputacionalmente.

**EX023.** B é a menor mudança com probabilidade de atender à lei.

**EX024.** As revogações do consentimento em até noventa dias.

**EX025.** O artigo 5(3) da Diretiva ePrivacy.

**EX026.** 22,0 pontos percentuais, intervalo de 95% de 20,0 a 24,0.

**EX027.** 41 por mil com A contra 12 com B, mais de três vezes mais.

**EX028.** Porque A provavelmente não é conforme, e seu uso deve se limitar ao teste.

**EX029.** Seus consentimentos são em menor número, mas mais estáveis ao longo do tempo.

**EX030.** Porque o design induziu o aceite, e as revogações posteriores mostram que muitas escolhas não eram genuínas.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 15, de 24 de abril de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science, 347*(6221), 509–514. <https://doi.org/10.1126/science.aaa1465>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Aprova o Regulamento de Comunicação de Incidente de Segurança*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. <https://doi.org/10.1561/0400000042>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Data Protection Board. (2021). *Guidelines 07/2020 on the concepts of controller and processor in the GDPR* (Version 2.0 adopted 7 July 2021; Version 2.1, 20 September 2022). <https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en>
- European Data Protection Board. (2023). *Guidelines 9/2022 on personal data breach notification under GDPR* (Version 2.0, adopted 28 March 2023). <https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en>
- European Union. (2002). Directive 2002/58/EC of the European Parliament and of the Council of 12 July 2002 concerning the processing of personal data and the protection of privacy in the electronic communications sector (ePrivacy Directive), as amended by Directive 2009/136/EC. *Official Journal of the European Communities, L 201*, 37–47 (CELEX 32002L0058; ELI dir/2002/58/oj, confirmed via the Publications Office record). <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0058>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. <https://doi.org/10.1109/SP.2008.33>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
