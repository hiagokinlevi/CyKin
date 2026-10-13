# Arquitetura e Engenharia de Segurança: Trilha de Pesquisa de Doutorado

- Idioma: português do Brasil (`pt`); curso 191, trilha de pesquisa de doutorado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 8 já estão escritos em português, com os exercícios EX001–EX026 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 5–8 (EX027–EX050) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: doutorandos que testam se uma prática de arquitetura muda os resultados de segurança.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios calculam concordância, uma estimativa de diferença em diferenças com um teste de permutação e os digests de um arquivo, sempre sobre dados sintéticos; nada toca uma organização real. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma doutoranda que testa se uma etapa de threat modeling com STRIDE na revisão de design reduz os defeitos de arquitetura após o lançamento: integridade e métodos, a fronteira da pesquisa, a proposta, a replicação da linha de base e o piloto, o estudo principal e a validação, a crítica, a síntese e o arquivo, e a defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Amara Lind** | Doutoranda | Inventada |
| **Prof. Rafael Quintero** | Orientador | Inventado |
| **Halden Institute of Technology** | Universidade fictícia | Inventada |
| **Tessaro Insurance Group** | Parceira fictícia com trinta equipes de produto | Inventada |

### Fontes principais

Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Shostack, *Threat Modeling* (2014); NIST [SP 800-160 Vol. 1 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1) e [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); Herley e van Oorschot (2017), [doi:10.1109/SP.2017.38](https://doi.org/10.1109/SP.2017.38); Wohlin et al. (2012). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–8: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridade e métodos avançados de pesquisa

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa falseável sobre uma prática de arquitetura; (2) escolher métodos capazes de distinguir a resposta de suas explicações rivais; (3) fixar regras de integridade para dados, parceiros e autoria antes de existir qualquer dado; (4) construir um esquema de codificação com concordância medida.

### 1.1 A doutoranda e a pergunta

Amara Lind é doutoranda no fictício Halden Institute of Technology, sob orientação do Prof. Rafael Quintero. Sua organização parceira é o fictício Tessaro Insurance Group, que mantém trinta equipes de produto construindo sistemas de sinistros, de apólices e de corretores. Todas as pessoas, organizações e números deste livro são sintéticos. A pergunta de Amara é se uma etapa estruturada de threat modeling na revisão de design, usando STRIDE como descrito por Shostack (2014), reduz a taxa de defeitos de segurança no nível da arquitetura encontrados após o lançamento, em comparação com a revisão de design sem essa etapa. A pergunta é falseável: um estudo bem conduzido poderia mostrar nenhuma redução, e ela se compromete de antemão a relatar esse resultado.

### 1.2 Por que é difícil testar afirmações sobre arquitetura

Herley e van Oorschot (2017) argumentam que boa parte do que se escreve sobre segurança faz afirmações que não podem ser refutadas, como dizer que uma prática melhora a segurança sem dizer que observação mostraria que ela não melhora. A arquitetura é especialmente exposta a esse problema, porque os resultados chegam tarde, os defeitos são raros e muitas práticas mudam ao mesmo tempo. Amara responde nomeando um desfecho mensurável, defeitos de arquitetura por cem mudanças de design encontrados nos doze meses após o lançamento, e nomeando de antemão as explicações rivais: maturidade da equipe, idade do sistema, regressão à média depois de anos ruins e mudanças na forma de reportar os defeitos.

### 1.3 Métodos que separam as rivais

Amara compara três desenhos. Uma comparação de antes e depois dentro das equipes que adotam a prática não consegue separar a prática da melhora geral ao longo do tempo. Um ensaio aleatorizado entre equipes seria o mais forte, mas a Tessaro não pode sortear quais equipes adotam, porque a adoção segue os ciclos orçamentários. Ela escolhe um desenho de adoção escalonada com equipes de comparação e uma análise de diferença em diferenças, seguindo a lógica de Wohlin et al. (2012) para experimentos em engenharia de software, e pré-registra o desfecho principal, as covariáveis e as regras de parada. Ela escreve que padrões de resultado apoiariam cada explicação rival, para que a análise possa testá-las, em vez de descartá-las com explicações depois.

### 1.4 Regras de integridade antes dos dados

Antes de coletar qualquer coisa, Amara acorda regras de integridade com a Tessaro e com seu comitê de ética. Os registros de defeitos são pseudonimizados, para que nenhum engenheiro possa ser identificado ou culpado. A Tessaro pode revisar os rascunhos em busca de detalhes confidenciais, mas não pode vetar os achados. O código, os manuais de codificação e réplicas sintéticas dos dados serão arquivados, enquanto os registros reais ficam com a Tessaro. A autoria segue a contribuição, e o assistente de codificação que classifica os defeitos será reconhecido. Ela registra essas regras com data e um hash do documento no seu caderno de laboratório, para que os leitores possam ver depois que elas não foram ajustadas quando os resultados já eram conhecidos.

### 1.5 Codificação com concordância medida

Classificar um defeito como de arquitetura ou de implementação é um julgamento, por isso Amara escreve um manual de codificação com definições e exemplos. Um defeito de arquitetura é aquele cuja correção exige mudar uma fronteira de confiança, a responsabilidade de um componente ou um fluxo de dados; um defeito de implementação pode ser corrigido dentro de um único componente. Ela e um segundo codificador classificam de forma independente um conjunto piloto e calculam o kappa de Cohen, interpretando-o com as faixas cautelosas de Landis e Koch (1977). O laboratório abaixo calcula o kappa sobre quarenta defeitos piloto sintéticos. Um valor baixo significaria que a medida de desfecho não é confiável e que o manual precisa de revisão antes que qualquer comparação faça sentido.

### Laboratório — Concordância entre codificadores na classe do defeito

```python
# Cohen's kappa for two coders classifying 40 synthetic defects (A=architecture, I=implementation).
c1 = "AAAAAAAAAAAAAAAAIIIIIIIIIIIIIIIIIIIIIIII"
c2 = "AAAAAAAAAAAAAAIIIIAIIIIIIIIIIIIIIIIIIAII"
n = len(c1); po = sum(a == b for a, b in zip(c1, c2)) / n
pe = sum((c1.count(k) / n) * (c2.count(k) / n) for k in "AI")
print(f"items={n} observed agreement={po:.3f} expected={pe:.3f} kappa={(po - pe) / (1 - pe):.2f}")
```

Execute com `python3 lab_kappa.py`. Saída verificada:

```text
items=40 observed agreement=0.900 expected=0.520 kappa=0.79
```

### Exemplo resolvido

Amara escreve a pergunta falseável com seu desfecho e quatro rivais, escolhe a adoção escalonada com diferença em diferenças, data e calcula o hash das suas regras de integridade e chega a um kappa de 0,79 na codificação piloto.

> **Caso sintético.** O Halden Institute, o Tessaro Insurance Group, Amara, Rafael e todos os dados são inventados; Shostack (2014), Herley e van Oorschot (2017), Wohlin et al. (2012) e Landis e Koch (1977) são reais.

### Erros e limites

O kappa depende da prevalência das classes e pode enganar quando uma classe domina. O pré-registro restringe a análise, mas não garante uma coleta de dados honesta.

### Exercícios

- **EX001 — Teste de falseabilidade.** Que observação refutaria a hipótese de Amara? *Rubrica:* 3 = nenhuma redução, ou um aumento, dos defeitos de arquitetura pós-lançamento por cem mudanças de design nas equipes que adotam, em relação às equipes de comparação;; 2 = nomeia o desfecho sem comparação;; 1 = diz que não pode ser refutada;; 0 = nenhuma.

- **EX002 — Crítica de Herley.** Que problema Herley e van Oorschot identificam nas afirmações de segurança? *Rubrica:* 3 = muitas afirmações não podem ser refutadas porque não nomeiam nenhuma observação que as contradiria;; 2 = afirmações não científicas;; 1 = nada;; 0 = nenhuma.

- **EX003 — Rejeição do antes e depois.** Por que um desenho simples de antes e depois é fraco aqui? *Rubrica:* 3 = não separa a prática da melhora geral ou da regressão à média;; 2 = uma rival;; 1 = desenho forte;; 0 = nenhuma.

- **EX004 — Sem aleatorização.** Por que a Tessaro não podia aleatorizar a adoção? *Rubrica:* 3 = a adoção segue ciclos orçamentários que a pesquisadora não controla;; 2 = orçamento;; 1 = só ética;; 0 = nenhuma.

- **EX005 — Veto da empresa.** Que direito a Tessaro tem sobre os rascunhos? *Rubrica:* 3 = revisar só em busca de detalhes confidenciais, sem veto sobre os achados;; 2 = revisão;; 1 = veto total;; 0 = nenhuma.

- **EX006 — Definição de defeito.** Como o manual define um defeito de arquitetura? *Rubrica:* 3 = a correção exige mudar uma fronteira de confiança, a responsabilidade de um componente ou um fluxo de dados;; 2 = parcial;; 1 = qualquer bug;; 0 = nenhuma.

- **EX007 — Kappa do piloto.** Que kappa o laboratório relatou e como ele é lido? *Rubrica:* 3 = 0,79, concordância substancial nas faixas de Landis e Koch;; 2 = só o valor;; 1 = abaixo de 0,4;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Arquitetura e engenharia de segurança: fronteira da pesquisa

### Objetivos de aprendizagem

Você vai (1) mapear os principais corpos de conhecimento em arquitetura de segurança; (2) separar princípios, frameworks e evidência empírica; (3) localizar a lacuna que o estudo de Amara trata; (4) julgar a qualidade da evidência na literatura de praticantes.

### 2.1 Corpos de conhecimento

O mapa da literatura de Amara tem quatro regiões. Os princípios começam com Saltzer e Schroeder (1975), cujos princípios de design, como menor privilégio, padrões à prova de falha e mediação completa, ainda enquadram as revisões de arquitetura. Os padrões de engenharia incluem o NIST SP 800-160 Vol. 1 Rev. 1, que trata a segurança como uma propriedade construída ao longo do ciclo de vida do sistema. Os frameworks corporativos incluem o SABSA, descrito por Sherwood, Clark e Lynas (2005), e o guia do The Open Group sobre a integração de risco e segurança ao TOGAF. Os livros de prática incluem Shostack (2014), sobre threat modeling, e Anderson (2020), sobre engenharia de segurança, que combina princípios com muitos estudos de caso de falhas.

### 2.2 Princípios, frameworks, evidência

Essas fontes são tipos diferentes de conhecimento. Os princípios são argumentos raciocinados sobre o que tende a tornar os sistemas mais seguros. Frameworks como o SABSA e o TOGAF organizam o trabalho e o vocabulário, o que ajuda as equipes a se comunicar, mas não mostra por si só que os resultados melhoram. Catálogos de controles como o NIST SP 800-53 Rev. 5 e a ISO/IEC 27002:2022 listam salvaguardas. A evidência empírica é uma quarta categoria: observações de que uma prática mudou os resultados em organizações reais. Amara acha essa quarta categoria escassa. Muitos artigos descrevem um método e um único caso, mas poucos comparam os resultados com um contrafactual crível.

### 2.3 Zero trust como caso

A arquitetura zero trust, descrita no NIST SP 800-207, mostra a velocidade com que uma fronteira avança. A publicação define princípios como autenticar e autorizar cada requisição e não conceder confiança com base na localização na rede. Fornecedores e governos adotaram o termo rapidamente, mas Amara encontra pouca evidência revisada por pares que meça como as implantações de zero trust mudam as taxas de incidentes. Isso não é uma crítica à orientação, que é uma referência de design, mas mostra uma lacuna recorrente: as ideias de arquitetura se espalham por padrões e pela prática mais rápido do que a pesquisa consegue testar seus efeitos. O próprio estudo dela fica nessa lacuna, no caso do threat modeling.

### 2.4 A lacuna e a contribuição

Depois da triagem, Amara encontra estudos sobre a usabilidade do threat modeling, estudos que contam as ameaças identificadas em oficinas e relatos de praticantes sobre a adoção. Ela não encontra, na sua busca, nenhum estudo que ligue uma etapa de threat modeling aos defeitos de arquitetura pós-lançamento com equipes de comparação. Essa é a lacuna dela. Ela declara a contribuição de forma estreita: uma estimativa, com incerteza, do efeito numa organização, um manual de codificação reutilizável e um pacote de replicação. Ela evita afirmar que o threat modeling funciona em geral, porque uma organização não sustenta essa afirmação, e lista as condições em que sua estimativa poderia se transferir.

### 2.5 Julgar a evidência de praticantes

Muito do conhecimento de arquitetura aparece em palestras de conferência, relatórios de fornecedores e blogs. Amara classifica cada fonte numa escala simples: relata como os dados foram coletados, inclui uma comparação, relata as falhas além dos sucessos e declara conflitos de interesse. Uma pesquisa de fornecedor que afirma grandes reduções depois da adoção da sua plataforma pontua baixo em comparação e em conflitos. A revisão pós-incidente honesta de uma equipe pontua mais alto em transparência, mesmo com um único caso. Ela usa as fontes de nota baixa apenas para gerar hipóteses, nunca como evidência de efeito, e declara essa regra no capítulo de métodos.

### Exemplo resolvido

Amara monta um mapa da literatura com quatro regiões, classifica vinte fontes como princípio, framework, catálogo ou empírica, dá notas aos relatos de praticantes e escreve uma declaração estreita da contribuição.

> **Caso sintético.** As contagens da triagem e os relatos classificados são sintéticos; as obras citadas são reais.

### Erros e limites

As buscas na literatura deixam passar a literatura cinzenta e os trabalhos fora do inglês. Uma lacuna pode existir porque uma pergunta é difícil de medir, e não porque ninguém pensou nela.

### Exercícios

- **EX008 — Princípios de Saltzer.** Cite três princípios de Saltzer e Schroeder. *Rubrica:* 3 = três entre menor privilégio, padrões à prova de falha, mediação completa, economia de mecanismo, design aberto, separação de privilégios, menor mecanismo comum, aceitabilidade psicológica;; 2 = dois;; 1 = nada;; 0 = nenhuma.

- **EX009 — Evidência dos frameworks.** Adotar o SABSA ou o TOGAF mostra, por si só, resultados melhores? *Rubrica:* 3 = não; os frameworks organizam o trabalho e o vocabulário, e os resultados exigem evidência empírica;; 2 = não;; 1 = sim;; 0 = nenhuma.

- **EX010 — Princípio do SP 800-207.** Enuncie um princípio de zero trust do SP 800-207. *Rubrica:* 3 = nenhuma confiança implícita pela localização na rede ou cada requisição autenticada e autorizada;; 2 = um;; 1 = confiar na rede interna;; 0 = nenhuma.

- **EX011 — Categoria escassa.** Que categoria de conhecimento Amara achou mais escassa? *Rubrica:* 3 = evidência empírica que compara resultados com um contrafactual;; 2 = empírica;; 1 = princípios;; 0 = nenhuma.

- **EX012 — Contribuição estreita.** Por que Amara evita afirmar que o threat modeling funciona em geral? *Rubrica:* 3 = uma organização não sustenta uma afirmação geral; ela lista as condições de transferência;; 2 = um local;; 1 = funciona;; 0 = nenhuma.

- **EX013 — Nota da pesquisa do fornecedor.** Por que a pesquisa de um fornecedor sobre a própria plataforma pontua baixo? *Rubrica:* 3 = não tem comparação e há conflito de interesse;; 2 = um motivo;; 1 = alta;; 0 = nenhuma.

- **EX014 — Uso das fontes de nota baixa.** Como as fontes de nota baixa podem ser usadas? *Rubrica:* 3 = só para gerar hipóteses, nunca como evidência de efeito;; 2 = hipóteses;; 1 = como evidência;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Proposta de contribuição original

### Objetivos de aprendizagem

Você vai (1) escrever uma proposta que declare de antemão hipóteses, medidas e análise; (2) definir a intervenção com precisão suficiente para ser replicada; (3) planejar o tamanho da amostra diante de tamanhos de efeito realistas; (4) antecipar as ameaças à validade.

### 3.1 Hipóteses e medidas

A proposta de Amara declara uma hipótese principal: as equipes que acrescentarem uma etapa de threat modeling com STRIDE à revisão de design apresentarão uma taxa menor de defeitos de arquitetura pós-lançamento por cem mudanças de design do que as equipes de comparação, medida ao longo de doze meses após cada mudança. As hipóteses secundárias tratam da gravidade dos defeitos e do tempo de correção. Cada medida tem uma definição, uma fonte de dados e uma regra de codificação. Ela também declara o que não é medido, como os defeitos nunca descobertos, e explica por quê: eles não podem ser contados, de modo que o estudo só pode estimar efeitos sobre os defeitos descobertos, uma limitação que ela vai repetir em todos os capítulos que relatarem resultados.

### 3.2 Definição da intervenção

Uma intervenção vaga não pode ser replicada. Amara a especifica em detalhe: antes da aprovação do design, a equipe desenha um diagrama de fluxo de dados com as fronteiras de confiança, percorre cada elemento pelas seis categorias do STRIDE, registra as ameaças com responsáveis e mitigações, e um arquiteto de fora da equipe revisa o registro. A sessão tem duração limitada a noventa minutos para uma mudança típica. Ela escreve um checklist de fidelidade, para que cada sessão possa ser pontuada quanto à aderência ao protocolo. Sem dados de fidelidade, um resultado nulo seria impossível de interpretar, porque ninguém saberia se a prática foi de fato aplicada.

### 3.3 Tamanho da amostra e efeito

Os defeitos de arquitetura são raros: o histórico da Tessaro mostra cerca de quatro por cem mudanças de design. Amara pergunta que redução importaria para a Tessaro, e a liderança de segurança diz que um quarto a menos de defeitos justificaria o custo de tempo. Com trinta equipes e cerca de quarenta mudanças de design por equipe por ano, ela simula o estudo muitas vezes sob esse efeito suposto e descobre que detectá-lo de forma confiável exige pelo menos dezoito meses de acompanhamento. Ela registra a simulação, suas premissas e o plano resultante, e observa que um efeito verdadeiro menor poderia facilmente passar despercebido, o que ela vai relatar, e não esconder.

### 3.4 Ameaças à validade

Seguindo Wohlin et al. (2012), Amara lista as ameaças em quatro grupos. Validade de construto: a classificação dos defeitos pode não captar o que os arquitetos entendem por falha de arquitetura. Validade interna: as equipes que adotam a prática podem mudar também outras práticas, como acrescentar security champions. Validade externa: uma seguradora com uma função central de arquitetura pode ser diferente de uma startup. Validade de conclusão: desfechos raros geram incerteza ampla. Para cada ameaça, ela escreve uma mitigação, como registrar a cada trimestre as mudanças de prática simultâneas e relatar intervalos de confiança, e não apenas testes de significância.

### 3.5 Revisão e aprovação

Amara apresenta a proposta à sua banca e ao conselho de arquitetura da Tessaro. A banca pergunta por que ela não mede também as ameaças encontradas nas sessões; ela a acrescenta como medida de processo, não de desfecho, porque encontrar mais ameaças não prova que haja menos defeitos. A Tessaro pede que as equipes não sejam ranqueadas publicamente; ela concorda em relatar apenas agregados. Os dois grupos aprovam, e ela registra a proposta com carimbo de tempo. Ela mantém um log de mudanças: qualquer alteração posterior nas medidas ou na análise será registrada com o motivo e relatada, para que os leitores distingam os resultados planejados dos exploratórios.

### Exemplo resolvido

Amara escreve uma proposta com uma hipótese principal e duas secundárias, um protocolo STRIDE de noventa minutos com checklist de fidelidade, um acompanhamento de dezoito meses baseado em simulação e uma tabela de validade.

> **Caso sintético.** As taxas de defeitos, o número de equipes e as decisões do conselho são sintéticos; Wohlin et al. (2012) e Shostack (2014) são reais.

### Erros e limites

O poder simulado depende da variação suposta entre as equipes. Os checklists de fidelidade podem virar preenchimento burocrático se os revisores não observarem as sessões.

### Exercícios

- **EX015 — Defeitos não descobertos.** Por que o estudo só pode estimar efeitos sobre os defeitos descobertos? *Rubrica:* 3 = os defeitos não descobertos não podem ser contados, então ficam fora da medida;; 2 = não podem ser contados;; 1 = inclui todos;; 0 = nenhuma.

- **EX016 — Propósito da fidelidade.** Por que um checklist de fidelidade é essencial para interpretar um resultado nulo? *Rubrica:* 3 = mostra se a prática foi de fato aplicada; sem ele, o nulo é ambíguo;; 2 = aplicada;; 1 = não é necessário;; 0 = nenhuma.

- **EX017 — Efeito relevante.** Que redução a liderança da Tessaro disse que importaria? *Rubrica:* 3 = um quarto a menos de defeitos de arquitetura;; 2 = um quarto;; 1 = qualquer uma;; 0 = nenhuma.

- **EX018 — Duração do acompanhamento.** Que acompanhamento a simulação sugeriu, e por quê? *Rubrica:* 3 = pelo menos dezoito meses, porque os defeitos são raros;; 2 = dezoito meses;; 1 = seis meses;; 0 = nenhuma.

- **EX019 — Ameaça interna.** Dê uma ameaça à validade interna e sua mitigação. *Rubrica:* 3 = as equipes que adotam mudam também outras práticas; registrar as mudanças simultâneas a cada trimestre;; 2 = só a ameaça;; 1 = ameaça externa;; 0 = nenhuma.

- **EX020 — Medida de ameaças encontradas.** Por que as ameaças encontradas nas sessões são medida de processo, e não de desfecho? *Rubrica:* 3 = encontrar mais ameaças não prova que haja menos defeitos;; 2 = não é desfecho;; 1 = é desfecho;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Replicação da linha de base e piloto

### Objetivos de aprendizagem

Você vai (1) replicar uma linha de base publicada ou anterior antes de estendê-la; (2) conduzir um piloto para testar procedimentos, não efeitos; (3) conferir os pipelines de dados contra valores conhecidos; (4) revisar o protocolo a partir das evidências do piloto.

### 4.1 Por que replicar primeiro

Antes de testar sua intervenção, Amara verifica se consegue reproduzir a linha de base histórica da própria Tessaro: cerca de quatro defeitos de arquitetura por cem mudanças de design. Se sua extração e sua codificação produzirem um número muito diferente dos registros da organização, ou os registros ou o método dela estão errados, e qualquer comparação posterior seria construída sobre areia. Replicar a linha de base é um teste barato de toda a cadeia de medição. Ela extrai dois anos de mudanças e defeitos históricos, codifica-os com o manual do capítulo 1 e compara sua taxa com o número que a liderança de segurança relatou nos documentos de planejamento.

### 4.2 Resultado da linha de base

A codificação dela dá 3,6 defeitos de arquitetura por cem mudanças, um pouco abaixo dos 4,1 relatados. Ao investigar, ela descobre que o número relatado contava chamados duplicados para o mesmo defeito quando várias equipes eram afetadas. Depois de remover as duplicatas, os dois números coincidem dentro do arredondamento. Essa pequena descoberta importa: se ela tivesse comparado suas medições posteriores com o número inflado do planejamento, a intervenção teria parecido funcionar mesmo que nada tivesse mudado. Ela registra a discrepância e a correção no log de mudanças e informa a Tessaro, cuja equipe de planejamento corrige o dashboard para os relatórios futuros.

### 4.3 Objetivos do piloto

O piloto roda com três equipes voluntárias por três meses. Seus objetivos são procedimentais: as equipes conseguem concluir o protocolo em noventa minutos, o checklist de fidelidade pode ser pontuado de forma consistente, o pipeline de dados de defeitos captura todos os chamados relevantes, e os engenheiros acham a sessão aceitável. O piloto explicitamente não serve para estimar o efeito, porque três equipes em três meses produziriam defeitos de menos para qualquer conclusão. Amara declara isso no plano do piloto, para que ninguém, nem ela mesma, se sinta tentado a anunciar um sucesso precoce a partir de um punhado de números.

### 4.4 Teste do pipeline

Amara insere dez chamados de teste sintéticos, com classificações conhecidas, numa cópia do rastreador de defeitos e roda seus scripts de extração. Nove chegam corretamente; um, aberto num projeto renomeado, se perde. Ela corrige o mapeamento de projetos e roda de novo, recuperando os dez. Ela mantém os chamados sintéticos como um teste de regressão permanente, que roda antes de cada extração de dados. Essa prática, tomada emprestada dos testes de software, dá uma verificação de resposta conhecida para o pipeline da pesquisa, da mesma forma que os vetores de teste dão uma verificação de resposta conhecida para o código criptográfico.

### 4.5 Revisão do protocolo

As evidências do piloto levam a três revisões. As sessões das mudanças grandes se estenderam, então o protocolo agora permite dividi-las em duas sessões. A pontuação de fidelidade divergiu sobre se as fronteiras de confiança tinham sido desenhadas, então o checklist ganha um diagrama de exemplo. Os engenheiros acharam útil, mas lenta, a revisão do arquiteto externo, então as revisões agora precisam terminar em até cinco dias úteis. Cada revisão é registrada com o motivo antes do início do estudo principal. Amara relata o piloto na tese como um capítulo separado, incluindo os problemas, porque quem for replicar o estudo vai enfrentar as mesmas dificuldades práticas.

### Exemplo resolvido

Amara replica a linha de base em 3,6 por cem mudanças, atribui o número de 4,1 a chamados duplicados, corrige uma lacuna do pipeline com chamados de teste sintéticos e registra três revisões do protocolo.

> **Caso sintético.** Os números da linha de base, as equipes do piloto e os chamados são sintéticos.

### Erros e limites

Um piloto com equipes voluntárias pode ser mais motivado do que as equipes típicas. Os testes de regressão só detectam os modos de falha conhecidos.

### Exercícios

- **EX021 — Discrepância da linha de base.** O que explicou a diferença entre 3,6 e 4,1? *Rubrica:* 3 = chamados duplicados para o mesmo defeito entre equipes no número relatado;; 2 = duplicatas;; 1 = erro de codificação;; 0 = nenhuma.

- **EX022 — Risco da comparação inflada.** O que teria acontecido se o número inflado fosse usado como linha de base? *Rubrica:* 3 = a intervenção pareceria funcionar mesmo sem mudança real;; 2 = falso sucesso;; 1 = nada;; 0 = nenhuma.

- **EX023 — Piloto não é efeito.** Por que o piloto não foi usado para estimar o efeito? *Rubrica:* 3 = três equipes em três meses geram defeitos de menos;; 2 = poucos demais;; 1 = foi usado;; 0 = nenhuma.

- **EX024 — Chamado perdido.** Por que um chamado sintético se perdeu, e como isso foi corrigido? *Rubrica:* 3 = estava num projeto renomeado; o mapeamento de projetos foi corrigido;; 2 = causa;; 1 = nada;; 0 = nenhuma.

- **EX025 — Analogia dos chamados de teste.** Com o que os chamados sintéticos se parecem na prática criptográfica? *Rubrica:* 3 = vetores de teste de resposta conhecida;; 2 = vetores de teste;; 1 = nada;; 0 = nenhuma.

- **EX026 — Mudanças grandes.** Como o protocolo foi revisado para as mudanças grandes? *Rubrica:* 3 = permitiu dividi-las em duas sessões;; 2 = divisão;; 1 = encurtado;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX026 (as de EX027–EX050 estão na edição em inglês até a tradução dos capítulos correspondentes). Amara Lind, o Prof. Rafael Quintero, o Halden Institute of Technology, o Tessaro Insurance Group e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Equipes que adotam a prática sem taxa menor, ou com taxa maior, de defeitos de arquitetura pós-lançamento por cem mudanças de design do que as equipes de comparação ao longo de doze meses.

**EX002.** Muitas afirmações de segurança são infalseáveis: afirmam um benefício sem dizer que observação mostraria que o benefício não existe.

**EX003.** Não consegue distinguir o efeito do threat modeling da melhora ao longo do tempo ou da regressão à média depois de anos ruins.

**EX004.** Porque as equipes adotam segundo os ciclos orçamentários, que Amara não pode atribuir ao acaso.

**EX005.** Pode revisar os rascunhos para retirar detalhes confidenciais, mas não pode bloquear nem alterar os achados.

**EX006.** Aquele cuja correção exige mudar uma fronteira de confiança, a responsabilidade de um componente ou um fluxo de dados, e não o código dentro de um único componente.

**EX007.** O kappa foi 0,79, com concordância observada de 0,90, o que fica na faixa de concordância substancial de Landis e Koch.

**EX008.** Menor privilégio, padrões à prova de falha e mediação completa.

**EX009.** Não. Eles estruturam o trabalho e a comunicação, mas a melhora dos resultados precisa ser mostrada por evidência empírica.

**EX010.** Nenhuma confiança é concedida apenas com base na localização na rede; cada requisição de acesso é autenticada e autorizada.

**EX011.** Evidência empírica que compara os resultados com um contrafactual crível.

**EX012.** Porque a evidência de uma organização não sustenta uma afirmação geral, então ela declara as condições de transferência.

**EX013.** Não tem grupo de comparação e o fornecedor tem conflito de interesse no resultado.

**EX014.** Apenas para sugerir hipóteses; nunca como evidência de que uma prática tem efeito.

**EX015.** Porque os defeitos nunca descobertos não podem ser observados, de modo que o desfecho cobre apenas os encontrados.

**EX016.** Mostra se as sessões seguiram o protocolo, para que um resultado nulo possa ser distinguido de uma falha na aplicação da prática.

**EX017.** Uma redução de cerca de um quarto nos defeitos de arquitetura pós-lançamento.

**EX018.** Pelo menos dezoito meses, porque, com cerca de quatro defeitos por cem mudanças, um acompanhamento mais curto gera eventos de menos.

**EX019.** As equipes que adotam podem acrescentar outras práticas, como security champions; Amara registra as mudanças simultâneas a cada trimestre.

**EX020.** Porque identificar mais ameaças nas oficinas não mostra, por si só, que menos defeitos chegam à produção.

**EX021.** Os 4,1 relatados contavam chamados duplicados quando um defeito afetava várias equipes; a remoção das duplicatas alinhou os números.

**EX022.** A intervenção teria parecido eficaz mesmo que nada mudasse, porque a linha de base estava superestimada.

**EX023.** Três equipes em três meses produzem defeitos de menos para sustentar qualquer conclusão sobre o efeito.

**EX024.** Estava num projeto renomeado; Amara corrigiu o mapeamento de projetos e os dez foram recuperados.

**EX025.** São como vetores de teste: entradas conhecidas com saídas esperadas que conferem o pipeline.

**EX026.** As mudanças grandes agora podem passar pelo threat modeling em duas sessões separadas.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- The Open Group. (2016, revised 2022). *Integrating risk and security within a TOGAF enterprise architecture* (TOGAF Series Guide G152). The Open Group.
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
