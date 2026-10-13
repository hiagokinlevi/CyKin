# Arquitetura e Engenharia de Segurança: Curso Rápido

- Idioma: português do Brasil (`pt`); curso 007, curso rápido (1 mês). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–4 de 4 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; os dois laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente e a verificação de 300 páginas A4 continuam em aberto.
- Público: equipes de organizações pequenas que precisam de um começo rápido e prático em arquitetura de segurança.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam dependências de fornecedores e conferem configurações contra uma baseline, ambos sobre dados sintéticos; nada toca um sistema real. Projetos de produção usam produtos e normas avaliados; nunca crie sua própria criptografia. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os quatro capítulos acompanham uma coordenadora de operações numa pequena cooperativa de crédito: fundamentos e decisões; escopo, permissão e prática segura; sistemas, dados e dependências; e um laboratório guiado com um plano de encerramento. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Leah Brennan** | Coordenadora de operações e aluna do curso rápido | Inventada |
| **Felix Ortega** | Tutor | Inventado |
| **Northgate Learning Centre** | Provedora fictícia de formação | Inventada |
| **Saltmarsh Community Credit Union** | Cooperativa de crédito fictícia com duas agências | Inventada |

### Fontes principais

Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Anderson, *Security Engineering* 3e (2020); Shostack, *Threat Modeling* (2014). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Arquitetura e engenharia de segurança: fundamentos e decisões

### Objetivos de aprendizagem

Você vai (1) explicar a arquitetura de segurança em termos simples; (2) aplicar cinco princípios de projeto a uma pequena cooperativa de crédito; (3) registrar corretamente uma decisão.

### 1.1 O que significa arquitetura

Leah Brennan coordena as operações da fictícia Saltmarsh Community Credit Union, uma cooperativa de crédito que atende seis mil associados em duas agências e num site. Ela entra num curso rápido de um mês no fictício Northgate Learning Centre, ministrado por Felix Ortega. Felix define a arquitetura de segurança como o arranjo geral das proteções entre pessoas, processos e tecnologia, projetado para que elas funcionem juntas. Ela responde a perguntas práticas: quem pode alcançar quais sistemas, onde as identidades são verificadas, onde ficam os dados dos associados e como os serviços se recuperam. É um plano para o todo, e não uma lista de produtos.

### 1.2 Por que importa para uma organização pequena

Leah pergunta se uma pequena cooperativa de crédito precisa mesmo de arquitetura. Felix explica que as organizações pequenas tomam decisões de segurança o tempo todo, como comprar um novo sistema de empréstimos ou permitir que um fornecedor se conecte remotamente. Sem um plano geral, cada decisão é tomada isoladamente, e elas muitas vezes se contradizem. Uma arquitetura curta e escrita permite que Leah confira cada nova proposta contra princípios acordados. Anderson (2020) observa que muitas falhas de segurança vêm de sistemas que eram razoáveis cada um sozinho, mas inseguros em combinação. Leah concorda em redigir uma para a Saltmarsh.

### 1.3 Cinco princípios

Felix ensina cinco princípios de Saltzer e Schroeder (1975), em termos simples. Menor privilégio: dar a cada pessoa apenas o acesso de que sua função precisa. Padrões seguros contra falhas (fail-safe defaults): partir de nenhum acesso e conceder o que for necessário. Mediação completa: verificar a permissão a cada requisição, e não só no login. Separação de privilégio: exigir duas pessoas ou duas condições para as ações mais sensíveis. Aceitabilidade psicológica: tornar os controles fáceis o bastante para que as pessoas os usem corretamente. Leah observa que esses princípios têm décadas e ainda assim descrevem a maior parte dos problemas que ela vê no trabalho.

### 1.4 Aplicá-los na Saltmarsh

Leah aplica os princípios. Os caixas podem ver as contas dos associados, mas não alterar as taxas de juros, o que é menor privilégio. As contas de novos funcionários começam vazias e recebem papéis mediante aprovação, o que é padrão seguro contra falhas. As transferências grandes exigem a aprovação de um segundo funcionário, o que é separação de privilégio. Ela encontra uma lacuna: a conta de e-mail compartilhada da agência é usada por todos os caixas, então ninguém consegue saber quem enviou o quê. Ela também descobre que o login do internet banking já usa um segundo fator por aplicativo, que os associados acham fácil, um exemplo de aceitabilidade.

### 1.5 Registrar uma decisão

A primeira decisão de arquitetura de Leah é se deve substituir a conta de e-mail compartilhada da agência por caixas postais individuais e uma caixa compartilhada que cada pessoa acessa com sua própria conta. Ela escreve um registro de decisão curto: contexto, opções, a escolha, os motivos, as consequências e quando revisitar. A escolha são contas individuais com acesso à caixa compartilhada. O motivo é a responsabilização, já que as consultas dos associados precisam ser rastreáveis até a pessoa que respondeu. Felix enfatiza que registrar as decisões por escrito permite que outros as entendam e as questionem depois, mesmo quando o autor já tiver saído.

### Exemplo resolvido

Leah define a arquitetura em termos simples, aplica cinco princípios à Saltmarsh, encontra uma lacuna no e-mail compartilhado e registra a decisão de substituí-lo.

> **Caso sintético.** A Saltmarsh, o Northgate e todas as pessoas são sintéticos; Anderson (2020) e Saltzer e Schroeder (1975) são reais.

### Erros e limites

Os princípios podem entrar em conflito, como a aceitabilidade contra a separação de privilégio. Cursos curtos dão fundamentos, e não domínio.

### Exercícios

- **EX001 — Definição simples.** Como Felix define a arquitetura de segurança? *Rubrica:* 3 = o arranjo geral das proteções entre pessoas, processos e tecnologia;; 2 = plano geral;; 1 = lista de produtos;; 0 = nenhuma.

- **EX002 — Organizações pequenas.** Por que uma pequena cooperativa de crédito precisa de arquitetura? *Rubrica:* 3 = decisões tomadas isoladamente muitas vezes se contradizem;; 2 = consistência;; 1 = nenhuma;; 0 = nenhuma.

- **EX003 — Menor privilégio na Saltmarsh.** Dê o exemplo de menor privilégio da Saltmarsh. *Rubrica:* 3 = os caixas veem as contas, mas não podem alterar as taxas de juros;; 2 = caixas;; 1 = nenhuma;; 0 = nenhuma.

- **EX004 — Exemplo de fail-safe.** Que prática mostra os padrões seguros contra falhas? *Rubrica:* 3 = contas de novos funcionários começam vazias e recebem papéis mediante aprovação;; 2 = começo vazio;; 1 = nenhuma;; 0 = nenhuma.

- **EX005 — Regra das duas pessoas.** Onde a Saltmarsh usa a separação de privilégio? *Rubrica:* 3 = transferências grandes precisam de um segundo aprovador;; 2 = transferências;; 1 = nenhuma;; 0 = nenhuma.

- **EX006 — Lacuna da caixa compartilhada.** Por que a conta de e-mail compartilhada da agência é uma lacuna? *Rubrica:* 3 = ninguém consegue saber quem enviou o quê;; 2 = responsabilização;; 1 = nenhuma;; 0 = nenhuma.

- **EX007 — Exemplo de aceitabilidade.** Que controle mostra a aceitabilidade psicológica? *Rubrica:* 3 = o segundo fator por aplicativo que os associados acham fácil;; 2 = fator por aplicativo;; 1 = nenhuma;; 0 = nenhuma.

- **EX008 — Partes do registro de decisão.** Liste as partes do registro de decisão de Leah. *Rubrica:* 3 = contexto, opções, escolha, motivos, consequências, data de revisão;; 2 = quatro;; 1 = nenhuma;; 0 = nenhuma.

- **EX009 — Opção escolhida.** Que opção a decisão sobre o e-mail escolheu? *Rubrica:* 3 = contas individuais com acesso à caixa compartilhada;; 2 = individual;; 1 = manter compartilhada;; 0 = nenhuma.

- **EX010 — Motivo da escolha.** Por que a responsabilização orientou a escolha do e-mail? *Rubrica:* 3 = as consultas dos associados precisam ser rastreáveis até quem respondeu;; 2 = rastreável;; 1 = custo;; 0 = nenhuma.

- **EX011 — Falhas combinadas.** Segundo Anderson, de onde vêm muitas falhas? *Rubrica:* 3 = de sistemas razoáveis sozinhos, mas inseguros juntos;; 2 = combinação;; 1 = bugs isolados;; 0 = nenhuma.

- **EX012 — Conflito de princípios.** Cite dois princípios que podem entrar em conflito. *Rubrica:* 3 = aceitabilidade e separação de privilégio;; 2 = par;; 1 = nenhuma;; 0 = nenhuma.

- **EX013 — Valor de registrar.** Segundo Felix, por que registrar as decisões por escrito? *Rubrica:* 3 = para que outros possam entendê-las e questioná-las depois;; 2 = questionar;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

A arquitetura de segurança é um plano escrito, fundamentado em alguns princípios duradouros e em decisões registradas.

<a id="ch-02"></a>

## Capítulo 2 — Escopo, permissão e prática segura

### Objetivos de aprendizagem

Você vai (1) definir o escopo de uma pequena revisão de segurança; (2) obter permissão por escrito; (3) trabalhar com segurança com os dados dos associados.

### 2.1 Definir o escopo

A gerente de Leah lhe pede que revise a segurança em torno do novo sistema de solicitação de empréstimos da Saltmarsh. Felix lhe ensina a escrever primeiro um escopo: que sistemas estão incluídos, quais estão excluídos, o que ela vai fazer e o que não vai fazer. Estão incluídos o sistema de empréstimos, os PCs da equipe que o usam e o recurso de envio de documentos pelos associados. Estão excluídos o sistema bancário central, operado por um bureau de serviços, e o processador de cartões. Ela vai ler configurações e entrevistar a equipe; não vai tentar ataques nem acessar os arquivos dos associados.

### 2.2 Permissão por escrito

Leah obtém a aprovação por escrito do diretor executivo e do responsável pelo sistema de empréstimos. A aprovação a nomeia e indica os sistemas no escopo, as datas e as atividades permitidas. Felix explica que até funcionários que revisam os sistemas do próprio empregador precisam de permissão, porque as revisões podem tocar dados sensíveis, interromper serviços ou violar contratos com fornecedores. A aprovação também protege Leah se alguém questionar suas ações. Ela pede ao fornecedor do sistema de empréstimos que confirme que ler as telas de configuração não viola o contrato de suporte. Ela arquiva a aprovação com suas anotações.

### 2.3 Manuseio seguro dos dados dos associados

As solicitações de empréstimo incluem contracheques, extratos bancários e documentos de identidade. A revisão de Leah não precisa de nenhum deles. Onde as telas mostram dados de associados, ela usa uma solicitação de teste criada pelo fornecedor com dados fictícios. Ao fazer capturas de tela das configurações, confere que nenhuma informação de associado apareça. Suas anotações ficam numa pasta restrita e serão apagadas depois que a revisão for aceita. Felix enfatiza que uma revisão de segurança nunca deve se tornar uma nova fonte de exposição de dados. Ela confirma essa abordagem primeiro com o responsável pelo sistema.

### 2.4 Condições de parada

Felix pede a Leah que defina quando ela vai parar e relatar imediatamente. Ela lista três condições: encontrar sinais de que outra pessoa já invadiu, encontrar documentos de associados expostos à internet e causar qualquer interrupção no serviço de empréstimos. Em cada caso, ela vai parar, avisar o responsável pelo sistema e o diretor executivo e não investigar mais sozinha. Condições de parada claras protegem os associados e impedem que quem revisa entre num trabalho de resposta a incidentes que exige outras habilidades e outra autoridade.

### 2.5 Um achado dentro do escopo

Durante a revisão, Leah descobre que os documentos enviados ficam guardados numa pasta em nuvem cuja configuração de compartilhamento permite que qualquer pessoa com o link veja os arquivos. Isso atende a uma de suas condições de parada. Ela para, informa o responsável e o diretor executivo, e o fornecedor muda a configuração em menos de uma hora. O fornecedor confere os logs de acesso e não encontra acesso de terceiros desconhecidos. Leah registra o evento, a resposta e as evidências. Seu escopo, sua permissão e suas condições de parada tornaram a resposta rápida, calma e devidamente documentada.

### Exemplo resolvido

Leah define o escopo de uma revisão do sistema de empréstimos, obtém permissão por escrito, usa dados de teste fictícios, define três condições de parada e trata corretamente um achado de compartilhamento por link.

> **Caso sintético.** O sistema de empréstimos e os eventos são sintéticos.

### Erros e limites

Os escopos podem excluir justamente onde estão os problemas. Os logs do fornecedor podem não mostrar todos os acessos.

### Exercícios

- **EX014 — Sistemas excluídos.** Que sistemas o escopo excluiu? *Rubrica:* 3 = o sistema bancário central operado por um bureau de serviços e o processador de cartões;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX015 — Não permitido.** Que atividades ficavam fora da permissão de Leah? *Rubrica:* 3 = tentar ataques ou acessar arquivos de associados;; 2 = ataques;; 1 = entrevistas;; 0 = nenhuma.

- **EX016 — Aprovadores.** Quem aprovou por escrito a revisão de Leah? *Rubrica:* 3 = o diretor executivo e o responsável pelo sistema de empréstimos;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX017 — Conferência com o fornecedor.** O que Leah confirmou com o fornecedor? *Rubrica:* 3 = que ler as telas de configuração não viola o contrato de suporte;; 2 = contrato;; 1 = nenhuma;; 0 = nenhuma.

- **EX018 — Solicitação de teste.** Como Leah evitou ver dados reais de associados? *Rubrica:* 3 = usou uma solicitação de teste do fornecedor com dados fictícios;; 2 = dados de teste;; 1 = nenhuma;; 0 = nenhuma.

- **EX019 — Cuidado com as capturas.** O que Leah conferia antes de salvar as capturas de tela? *Rubrica:* 3 = que nenhuma informação de associado aparecesse;; 2 = sem dados;; 1 = nenhuma;; 0 = nenhuma.

- **EX020 — Três gatilhos de parada.** Que três condições fazem Leah parar? *Rubrica:* 3 = sinais de invasão, documentos de associados expostos online, interrupção do serviço;; 2 = duas;; 1 = nenhuma;; 0 = nenhuma.

- **EX021 — Por que parar.** Por que quem revisa deve parar em vez de investigar sozinho? *Rubrica:* 3 = a resposta a incidentes exige outras habilidades e outra autoridade;; 2 = autoridade;; 1 = nenhuma;; 0 = nenhuma.

- **EX022 — Achado nos envios.** Que exposição a revisão encontrou? *Rubrica:* 3 = documentos numa pasta em nuvem visível a qualquer pessoa com o link;; 2 = compartilhamento por link;; 1 = nenhuma;; 0 = nenhuma.

- **EX023 — Resultado dos logs do fornecedor.** O que os logs de acesso do fornecedor mostraram? *Rubrica:* 3 = nenhum acesso de terceiros desconhecidos;; 2 = nada encontrado;; 1 = invasão;; 0 = nenhuma.

- **EX024 — Retenção das anotações.** Quando as anotações da revisão de Leah são apagadas? *Rubrica:* 3 = depois que a revisão for aceita;; 2 = após aceitação;; 1 = nunca;; 0 = nenhuma.

- **EX025 — Rapidez da resposta.** Com que rapidez o fornecedor corrigiu a configuração de compartilhamento? *Rubrica:* 3 = em menos de uma hora;; 2 = hora;; 1 = nenhuma;; 0 = nenhuma.

- **EX026 — Exposição pela revisão.** O que uma revisão de segurança nunca deve se tornar? *Rubrica:* 3 = uma nova fonte de exposição de dados;; 2 = exposição;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Escopo, permissão, manuseio seguro dos dados e condições de parada tornam as revisões úteis e seguras.

<a id="ch-03"></a>

## Capítulo 3 — Arquitetura e engenharia de segurança: sistemas, dados e dependências

### Objetivos de aprendizagem

Você vai (1) mapear os sistemas e os fluxos de dados da Saltmarsh; (2) identificar fornecedores e dependências; (3) encontrar onde uma única falha pararia muitos serviços.

### 3.1 Mapear os sistemas

Leah lista os principais sistemas da Saltmarsh com seus responsáveis: o sistema bancário central no bureau de serviços, o internet banking, o novo sistema de empréstimos, o e-mail e as ferramentas de escritório em nuvem, os PCs das agências, o processador de cartões e o sistema telefônico. Para cada um, ela registra que dados ele guarda e quem o usa. Os saldos e as transações das contas dos associados ficam no sistema bancário central; os documentos de empréstimo ficam no sistema de empréstimos; a correspondência com os associados fica no e-mail. Saber onde os dados vivem lhe diz quais sistemas precisam da proteção mais forte.

### 3.2 Desenhar os fluxos de dados

Leah desenha como se move uma solicitação de empréstimo: um associado envia documentos pelo site; o sistema de empréstimos os armazena; um agente de crédito os revisa num PC da agência; a aprovação dispara um pagamento pelo sistema bancário central; o associado recebe um e-mail. Ela rotula cada fluxo com os dados que ele carrega e marca onde ele passa para um fornecedor. Shostack (2014) recomenda atenção cuidadosa a esses cruzamentos, porque cada um depende dos controles de outra parte e de suposições sobre o que o outro lado já verificou.

### 3.3 Fornecedores e dependências

A Saltmarsh depende muito de fornecedores: o bureau de serviços, o fornecedor do sistema de empréstimos, o provedor de e-mail em nuvem, o processador de cartões, o provedor de identidade usado no login da equipe e dois provedores de internet. Leah registra o papel de cada fornecedor, os dados que ele guarda, o responsável pelo contrato e o que acontece se ele falhar. Ela observa que o provedor de identidade é usado por quase todos os sistemas, então sua falha ou seu comprometimento afetaria quase tudo. As dependências fazem parte da arquitetura, mesmo que a Saltmarsh não as opere.

### Laboratório — Contagem dos serviços que dependem de cada fornecedor

```python
# Count services depending on each supplier (synthetic map).
services = {"online banking": ["identity", "bureau", "internet"], "loan system": ["identity", "loan vendor", "bureau"],
            "email": ["identity", "cloud email"], "branch PCs": ["identity", "internet"],
            "card services": ["card processor", "bureau"], "staff intranet": ["identity", "cloud email"],
            "member payments": ["identity", "bureau"]}
count = {}
for s, deps in services.items():
    for d in deps: count[d] = count.get(d, 0) + 1
for d, n in sorted(count.items(), key=lambda x: (-x[1], x[0])): print(f"{d:14} {n} service(s)")
```

Execute com `python3 lab_deps.py`. Saída verificada:

```text
identity       6 service(s)
bureau         4 service(s)
cloud email    2 service(s)
internet       2 service(s)
card processor 1 service(s)
loan vendor    1 service(s)
```

### 3.4 Pontos únicos de falha

O laboratório conta quantos serviços dependem de cada fornecedor. O provedor de identidade sustenta seis serviços, e o bureau de serviços, quatro; a maioria dos outros sustenta um ou dois. Leah discute os resultados com a gerente. Para o provedor de identidade, eles acordam uma conta de administrador de emergência (break-glass) guardada com segurança offline e um procedimento testado para fazer login se o provedor falhar. Para o bureau de serviços, eles contam com os compromissos contratuais de recuperação e mantêm um procedimento manual para saques urgentes de associados nas agências.

### 3.5 Usar o mapa

Leah guarda juntos a lista de sistemas, o diagrama de fluxos de dados e a tabela de dependências como a primeira visão geral de arquitetura da Saltmarsh. Quando, mais tarde, o conselho avalia um novo aplicativo de orçamento doméstico para os associados, a visão geral mostra que ele acrescentaria um novo fornecedor com dados de transações e mais uma dependência do provedor de identidade. O conselho faz perguntas de segurança ao fornecedor antes de assinar. Felix observa que um mapa simples se paga na primeira vez em que molda uma decisão antes que o dinheiro seja gasto. Leah fixa uma data anual para atualizar a visão geral.

### Exemplo resolvido

Leah mapeia os sistemas e os fluxos de dados dos empréstimos, lista seis fornecedores, conta as dependências para identificar o provedor de identidade como principal ponto único de falha e usa o mapa numa decisão do conselho.

> **Caso sintético.** Os sistemas, os fornecedores e as contagens são sintéticos; Shostack (2014) é real.

### Erros e limites

Os mapas ficam desatualizados sem atualizações. As falhas de fornecedores podem se propagar por quartas partes.

### Exercícios

- **EX027 — Onde ficam os saldos.** Que sistema guarda os saldos e as transações das contas? *Rubrica:* 3 = o sistema bancário central no bureau de serviços;; 2 = sistema central;; 1 = sistema de empréstimos;; 0 = nenhuma.

- **EX028 — Etapas do fluxo de empréstimo.** Descreva o fluxo da solicitação de empréstimo. *Rubrica:* 3 = envio, sistema de empréstimos, revisão do agente, pagamento pelo sistema central, e-mail;; 2 = a maioria das etapas;; 1 = nenhuma;; 0 = nenhuma.

- **EX029 — Atenção aos cruzamentos.** Por que os cruzamentos com fornecedores exigem atenção? *Rubrica:* 3 = cada um depende dos controles e das suposições de outra parte;; 2 = suposições;; 1 = nenhuma;; 0 = nenhuma.

- **EX030 — Registro do fornecedor.** O que Leah registra para cada fornecedor? *Rubrica:* 3 = papel, dados guardados, responsável pelo contrato e impacto da falha;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

- **EX031 — Contagem da identidade.** Quantos serviços dependem do provedor de identidade no laboratório? *Rubrica:* 3 = seis;; 2 = 6;; 1 = um;; 0 = nenhuma.

- **EX032 — Contagem do bureau.** Quantos serviços dependem do bureau de serviços? *Rubrica:* 3 = quatro;; 2 = 4;; 1 = nenhuma;; 0 = nenhuma.

- **EX033 — Break-glass.** Que contingência foi acordada para o provedor de identidade? *Rubrica:* 3 = uma conta break-glass offline e um procedimento de login testado;; 2 = break-glass;; 1 = nenhuma;; 0 = nenhuma.

- **EX034 — Contingência do bureau.** Que contingência existe para o bureau de serviços? *Rubrica:* 3 = recuperação contratual e um procedimento manual de saque nas agências;; 2 = manual;; 1 = nenhuma;; 0 = nenhuma.

- **EX035 — Aplicativo de orçamento.** O que o mapa revelou sobre o aplicativo de orçamento? *Rubrica:* 3 = um novo fornecedor com dados de transações e mais dependência da identidade;; 2 = novo fornecedor;; 1 = nada;; 0 = nenhuma.

- **EX036 — Ação do conselho.** Como o conselho reagiu ao aplicativo de orçamento? *Rubrica:* 3 = fez perguntas de segurança ao fornecedor antes de assinar;; 2 = perguntas;; 1 = assinou;; 0 = nenhuma.

- **EX037 — Retorno do mapa.** Quando um mapa simples se paga? *Rubrica:* 3 = na primeira vez em que molda uma decisão antes de o dinheiro ser gasto;; 2 = primeira decisão;; 1 = nunca;; 0 = nenhuma.

- **EX038 — Mapas desatualizados.** O que limita a utilidade do mapa ao longo do tempo? *Rubrica:* 3 = fica desatualizado sem atualizações;; 2 = desatualização;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Mapear sistemas, fluxos de dados e dependências mostra onde a proteção e os planos alternativos importam mais.

<a id="ch-04"></a>

## Capítulo 4 — Arquitetura e engenharia de segurança: laboratório guiado e síntese aplicada

### Objetivos de aprendizagem

Você vai (1) conferir as configurações de um sistema contra uma baseline num laboratório guiado; (2) transformar os resultados em ações priorizadas; (3) sintetizar o aprendizado do mês num plano curto.

### 4.1 O laboratório guiado

Felix propõe um laboratório guiado com configurações sintéticas exportadas de um sistema de empréstimos parecido com o da Saltmarsh. O laboratório compara cada configuração com uma baseline curta tirada dos princípios do mês: login multifator para a equipe, sessões que expiram, nenhuma conta compartilhada, links de envio que expiram, logs de auditoria ativados e direitos de administrador limitados a duas pessoas. Leah roda o script e lê a saída linha por linha. O laboratório roda offline sobre dados fictícios, então nada toca um sistema real. Felix conduz a turma pelas duas primeiras verificações.

### Laboratório — Conferência das configurações do sistema de empréstimos contra uma baseline

```python
# Check loan system settings against a baseline (synthetic exports before and after fixes).
rules = {"staff_mfa": lambda v: v == "on", "session_timeout_min": lambda v: v <= 30,
         "shared_accounts": lambda v: v == 0, "upload_link_expiry_days": lambda v: v is not None and v <= 14,
         "audit_logging": lambda v: v == "on", "admin_count": lambda v: v <= 2, "public_links": lambda v: v == "off"}
after = {"staff_mfa": "on", "session_timeout_min": 30, "shared_accounts": 0, "upload_link_expiry_days": 14,
         "audit_logging": "on", "admin_count": 2, "public_links": "off"}
before = dict(after, session_timeout_min=480, admin_count=5, upload_link_expiry_days=None)
for label, cfg in (("before", before), ("after", after)):
    fails = [f"{k}={cfg[k]}" for k, ok in rules.items() if not ok(cfg[k])]
    print(f"{label}: {len(rules) - len(fails)}/{len(rules)} settings meet baseline; fails {fails}")
```

Execute com `python3 lab_baseline.py`. Saída verificada:

```text
before: 4/7 settings meet baseline; fails ['session_timeout_min=480', 'upload_link_expiry_days=None', 'admin_count=5']
after: 7/7 settings meet baseline; fails []
```

### 4.2 Ler os resultados

O laboratório relata quatro de sete configurações atendendo à baseline. Três não atendem: as sessões ficam abertas por oito horas em vez de trinta minutos, cinco pessoas têm direitos de administrador em vez de duas e os links de envio nunca expiram. Leah observa que a correção anterior do compartilhamento por link fechou o acesso público, mas não definiu uma expiração. Ler os resultados com cuidado importa, porque a aprovação numa configuração pode esconder uma fraqueza relacionada que a baseline descreve separadamente. Ela anota cada lacuna com o nome da configuração, o valor atual e o valor da baseline, para que o fornecedor possa agir.

### 4.3 Priorizar as ações

Leah ordena as três lacunas. Os direitos de administrador vêm primeiro, porque qualquer uma das cinco contas poderia alterar as configurações de segurança ou exportar todos os documentos de empréstimo. A expiração dos links vem em segundo, já que links antigos poderiam vazar se fossem encaminhados. O tempo de expiração das sessões vem em terceiro, já que os PCs das agências já bloqueiam após cinco minutos. Para cada ação, ela nomeia um responsável e uma data e pergunta ao fornecedor quais mudanças podem ser feitas por configuração. Todas as três podem, e o fornecedor confirma que elas não vão atrapalhar o processamento dos empréstimos.

### 4.4 Verificar a correção

Depois das mudanças, Leah roda de novo o laboratório com uma exportação atualizada. Todas as sete configurações agora atendem à baseline. Ela guarda as duas saídas como evidência, datadas, na pasta da revisão. Felix enfatiza que a verificação fecha o ciclo: uma mudança solicitada não é uma mudança feita até que uma verificação a confirme. Ele também sugere rodar de novo a verificação a cada trimestre, porque as atualizações do fornecedor e as mudanças na equipe podem desfazer as configurações sem alarde ao longo do tempo. Leah registra a data de cada execução e o arquivo de exportação usado, para que as evidências possam ser rastreadas. Ela acrescenta a verificação trimestral ao calendário de operações, com o próprio nome como responsável.

### 4.5 Síntese e plano

Para encerrar o curso, Leah escreve um plano de uma página para os próximos seis meses da Saltmarsh: contas de e-mail individuais, como decidido no capítulo 1; uma verificação trimestral do sistema de empréstimos contra a baseline; um procedimento break-glass testado para o provedor de identidade; uma atualização anual da visão geral de arquitetura; e perguntas de segurança para todo novo fornecedor. Cada item se liga a um princípio ou achado do curso. A gerente aprova o plano. Felix observa que o objetivo do curso não era a especialização, e sim um hábito de trabalho de mapear, verificar e registrar que Leah pode continuar usando.

### Exemplo resolvido

Leah executa um laboratório de baseline sobre configurações sintéticas de empréstimos, encontra três lacunas, prioriza-as e as corrige, verifica com uma nova execução e escreve um plano de seis meses.

> **Caso sintético.** As configurações, o fornecedor e o plano são sintéticos.

### Erros e limites

As baselines cobrem apenas as configurações listadas. As verificações trimestrais caducam sem um responsável.

### Exercícios

- **EX039 — Itens da baseline.** Cite três itens da baseline do laboratório. *Rubrica:* 3 = login multifator, expiração de sessão, nenhuma conta compartilhada, expiração de links, logs de auditoria, dois administradores;; 2 = dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX040 — Primeiro resultado.** Quantas configurações atendiam à baseline no início? *Rubrica:* 3 = 4 de 7;; 2 = quatro;; 1 = nenhuma;; 0 = nenhuma.

- **EX041 — Lacuna de sessão.** Que configuração de sessão falhou? *Rubrica:* 3 = as sessões ficavam abertas oito horas em vez de trinta minutos;; 2 = oito horas;; 1 = nenhuma;; 0 = nenhuma.

- **EX042 — Lacuna de administradores.** Quantas pessoas tinham direitos de administrador? *Rubrica:* 3 = cinco em vez de duas;; 2 = cinco;; 1 = duas;; 0 = nenhuma.

- **EX043 — Fraqueza escondida.** O que a correção anterior do link não cobriu? *Rubrica:* 3 = a expiração dos links;; 2 = expiração;; 1 = nenhuma;; 0 = nenhuma.

- **EX044 — Prioridade máxima.** Por que os direitos de administrador são a prioridade máxima? *Rubrica:* 3 = qualquer uma das cinco contas poderia alterar configurações ou exportar todos os documentos;; 2 = poder amplo;; 1 = nenhuma;; 0 = nenhuma.

- **EX045 — Posição da expiração de sessão.** Por que a expiração de sessão ficou em terceiro? *Rubrica:* 3 = os PCs das agências já bloqueiam após cinco minutos;; 2 = bloqueio do PC;; 1 = nenhuma;; 0 = nenhuma.

- **EX046 — Segunda execução.** Quantas configurações passaram depois das mudanças? *Rubrica:* 3 = 7 de 7;; 2 = todas;; 1 = nenhuma;; 0 = nenhuma.

- **EX047 — Mudança feita.** Segundo Felix, quando uma mudança solicitada está de fato feita? *Rubrica:* 3 = quando uma verificação a confirma;; 2 = verificada;; 1 = quando solicitada;; 0 = nenhuma.

- **EX048 — Nova execução trimestral.** Por que rodar de novo a verificação a cada trimestre? *Rubrica:* 3 = atualizações e mudanças na equipe podem desfazer configurações;; 2 = deriva;; 1 = nenhuma;; 0 = nenhuma.

- **EX049 — Itens do plano.** Cite dois itens do plano de seis meses de Leah. *Rubrica:* 3 = e-mail individual, baseline trimestral, teste de break-glass, atualização da visão geral, perguntas aos fornecedores;; 2 = um;; 1 = nenhuma;; 0 = nenhuma.

- **EX050 — Objetivo do curso.** Segundo Felix, qual era o objetivo do curso? *Rubrica:* 3 = um hábito de trabalho de mapear, verificar e registrar;; 2 = hábito;; 1 = especialização;; 0 = nenhuma.

### Síntese

Uma verificação de linha de base guiada, correções priorizadas, verificação e um plano curto transformam um mês de aprendizado em prática duradoura.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Leah Brennan, Felix Ortega, o Northgate Learning Centre, a Saltmarsh Community Credit Union e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O arranjo geral das proteções entre pessoas, processos e tecnologia, projetado para que funcionem juntas.

**EX002.** Porque decisões tomadas uma de cada vez, sem um plano, muitas vezes se contradizem.

**EX003.** Os caixas podem ver as contas dos associados, mas não podem alterar as taxas de juros.

**EX004.** As contas de novos funcionários começam sem acesso e só recebem papéis mediante aprovação.

**EX005.** As transferências grandes precisam da aprovação de um segundo funcionário.

**EX006.** Porque ninguém consegue saber qual caixa enviou qual mensagem.

**EX007.** O segundo fator por aplicativo do internet banking, que os associados acham fácil.

**EX008.** Contexto, opções, a escolha, os motivos, as consequências e quando revisitar.

**EX009.** Contas individuais com acesso a uma caixa compartilhada.

**EX010.** Porque as consultas dos associados precisam ser rastreáveis até a pessoa que as respondeu.

**EX011.** De sistemas que são razoáveis cada um sozinho, mas inseguros em combinação.

**EX012.** A aceitabilidade psicológica e a separação de privilégio, já que aprovações extras acrescentam atrito.

**EX013.** Para que outros possam entender e questionar o raciocínio depois, mesmo após a saída do autor.

**EX014.** O sistema bancário central operado por um bureau de serviços e o processador de cartões.

**EX015.** Tentar ataques ou acessar os arquivos dos associados.

**EX016.** O diretor executivo e o responsável pelo sistema de empréstimos.

**EX017.** Que ler as telas de configuração não violaria o contrato de suporte.

**EX018.** Ela usou uma solicitação de teste do fornecedor com dados fictícios.

**EX019.** Que nenhuma informação de associado aparecia nelas.

**EX020.** Sinais de uma invasão já existente, documentos de associados expostos à internet e qualquer interrupção do serviço.

**EX021.** Porque a resposta a incidentes exige habilidades e autoridade diferentes das de uma revisão.

**EX022.** Os documentos enviados estavam numa pasta em nuvem visível a qualquer pessoa com o link.

**EX023.** Nenhum acesso de terceiros desconhecidos.

**EX024.** Depois que a revisão for aceita.

**EX025.** Em menos de uma hora depois que Leah o relatou.

**EX026.** Uma nova fonte de exposição de dados.

**EX027.** O sistema bancário central operado pelo bureau de serviços.

**EX028.** Um associado envia documentos, o sistema de empréstimos os armazena, um agente os revisa, o sistema central paga e o associado recebe um e-mail.

**EX029.** Porque cada um depende dos controles de outra parte e de suposições sobre o que foi verificado.

**EX030.** Seu papel, os dados que guarda, o responsável pelo contrato e o que acontece se ele falhar.

**EX031.** Seis serviços.

**EX032.** Quatro serviços.

**EX033.** Uma conta de administrador break-glass guardada com segurança offline, com um procedimento testado.

**EX034.** Seus compromissos contratuais de recuperação, mais um procedimento manual para saques urgentes nas agências.

**EX035.** Que ele acrescentaria um fornecedor com dados de transações e mais uma dependência do provedor de identidade.

**EX036.** Fez perguntas de segurança ao fornecedor antes de assinar.

**EX037.** Na primeira vez em que molda uma decisão antes que o dinheiro seja gasto.

**EX038.** Ele fica desatualizado, a menos que seja atualizado conforme os sistemas mudam.

**EX039.** Login multifator da equipe, expiração de sessões e links de envio que expiram, entre outros.

**EX040.** Quatro de sete.

**EX041.** As sessões ficavam abertas por oito horas em vez de trinta minutos.

**EX042.** Cinco pessoas, em vez das duas da baseline.

**EX043.** Ela removeu o acesso público, mas não definiu a expiração dos links.

**EX044.** Porque qualquer uma das cinco contas poderia alterar as configurações de segurança ou exportar todos os documentos de empréstimo.

**EX045.** Porque os PCs das agências já bloqueiam após cinco minutos.

**EX046.** Todas as sete configurações atenderam à baseline.

**EX047.** Somente quando uma verificação a confirma.

**EX048.** Porque as atualizações do fornecedor e as mudanças na equipe podem desfazer as configurações sem alarde.

**EX049.** Uma verificação trimestral do sistema de empréstimos contra a baseline e um procedimento break-glass testado, entre outros.

**EX050.** Um hábito de trabalho de mapear, verificar e registrar, e não a especialização.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
