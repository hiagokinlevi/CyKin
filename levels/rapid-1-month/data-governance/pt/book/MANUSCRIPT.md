# Governança de Dados: Curso Rápido

- Idioma: português do Brasil (`pt`); curso 003, curso rápido (1 mês). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–4 de 4 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; o laboratório offline usa apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e sua saída foi incorporada de uma execução real, idêntica à da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: iniciantes que precisam de um começo rápido e prático em governança de dados para um pequeno negócio.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: o laboratório confere uma lista sintética de doze linhas de inscrições de um café em busca de e-mails em branco, endereços malformados, duplicatas e marcações de consentimento. A legislação é citada pela edição e parafraseada; nada aqui é aconselhamento jurídico. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os quatro capítulos acompanham um supervisor de turno ao longo de um curso de um mês: fundamentos e primeiras decisões, responsabilidade e práticas seguras, qualidade, sistemas e fornecedores, e um laboratório guiado que se transforma em um plano de ação curto. Execute o laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Kwame Boateng** | Estudante do curso rápido, supervisor de turno em um café | Inventado |
| **Sra. Lena Fischer** | Mentora, gerente de dados de uma prefeitura | Inventada |
| **Riverside Adult Learning Centre** | Centro de educação de adultos fictício | Inventado |
| **Copperleaf Café** | Negócio fictício, com dois cafés e doze funcionários | Inventado |

### Fontes principais

GDPR; LGPD. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Governança de dados: fundamentos e primeiras decisões

### Objetivos de aprendizagem

Você vai (1) explicar a governança de dados em palavras simples; (2) listar os dados que um pequeno café mantém; (3) tomar três primeiras decisões sobre responsabilidades e regras.

### 1.1 O aprendiz e o café

Kwame Boateng trabalha como supervisor de turno no Copperleaf Café, um negócio fictício com dois cafés, doze funcionários e um boletim por e-mail para os clientes frequentes. A dona, a Sra. Adeyemi, pede a ele que organize a forma como o café cuida de seus dados. Ele entra em um curso rápido de um mês no fictício Riverside Adult Learning Centre, orientado pela mentora Sra. Lena Fischer, que trabalha como gerente de dados de uma prefeitura. Todos os exercícios usam dados sintéticos inventados para o ensino, nunca dados reais de clientes. Kwame começa o curso animado e com muitas perguntas.

### 1.2 O que significa governança de dados

A Sra. Fischer explica a governança de dados em uma frase: combinar quem é responsável por cada tipo de dado, que regras ele deve seguir e como todos conferem se as regras funcionam. Kwame anota que se trata de decisões e hábitos, e não de software caro. Um pequeno café consegue governar seus dados com uma lista curta de responsáveis, uma página de regras e algumas verificações regulares. O objetivo são dados exatos o bastante para serem usados, seguros e guardados só pelo tempo necessário. Kwame gosta da ideia de começar pequeno e escreve a frase da mentora na primeira página do caderno.

### 1.3 Os dados da Copperleaf

Kwame lista os dados da Copperleaf: a folha de inscrição no boletim com os e-mails dos clientes, os nomes, telefones e escalas dos funcionários, os contatos e as notas fiscais dos fornecedores, os relatórios de pagamento com cartão do fornecedor do caixa, anotações de alergia de alguns clientes frequentes e fotos de um evento recente. Ele marca quais contêm dados pessoais sobre pessoas identificáveis. A maioria contém. Observa que as anotações de alergia são informações de saúde, que o GDPR trata como categoria especial e a LGPD como dado pessoal sensível (art. 5º, II), com cuidados adicionais. Ele escreve cada item em uma lista, com o local onde fica guardado.

### 1.4 Por que isso importa

A Sra. Fischer pergunta a Kwame o que poderia dar errado. Ele lista: mandar e-mails a clientes que nunca concordaram, perder as anotações de alergia e servir a comida errada, passar os telefones dos funcionários para a pessoa errada, guardar escalas antigas para sempre e pagar duas vezes a um fornecedor porque existem duas cópias da mesma nota. Cada problema afeta clientes, funcionários ou dinheiro. Ele percebe que a governança protege as pessoas e o negócio ao mesmo tempo, e que os pequenos negócios enfrentam os mesmos tipos de risco que os grandes. A Sra. Adeyemi concorda com a lista e pede que ele siga adiante.

### 1.5 Três primeiras decisões

A Sra. Fischer pede a Kwame que tome três decisões naquela semana. Primeira: a Sra. Adeyemi responde por todos os dados, e Kwame cuida deles no dia a dia. Segunda: cada tipo de dado ganha um responsável nomeado: Kwame para o boletim e as anotações de alergia, o subgerente para as escalas e a Sra. Adeyemi para os registros de fornecedores e pagamentos. Terceira: nenhum dado de cliente ou de funcionário sai dos sistemas aprovados do café. A Sra. Adeyemi concorda com as três, e Kwame as escreve em uma única página. A equipe é informada naquela mesma semana, durante a troca de turno.

### Exemplo resolvido

Kwame define a governança como responsabilidades, regras e verificações, lista os dados da Copperleaf, incluindo as anotações de alergia como informação de saúde, identifica riscos para as pessoas e para o dinheiro e registra três primeiras decisões aprovadas pela Sra. Adeyemi.

> **Caso sintético.** A Copperleaf, o Riverside e todas as pessoas são sintéticos; o GDPR e a LGPD são reais.

### Erros e limites

Achar que a governança exige ferramentas caras atrasa decisões simples que ajudam de imediato.

### Exercícios

- **EX001 — Tamanho do negócio.** Quantos cafés a Copperleaf tem? *Rubrica:* 3 = dois;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX002 — Trabalho da mentora.** Qual é o trabalho da Sra. Fischer? *Rubrica:* 3 = gerente de dados de uma prefeitura;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX003 — Definição em uma frase.** Como a Sra. Fischer define governança? *Rubrica:* 3 = quem é responsável, que regras, como as regras são conferidas;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX004 — Necessidade de software.** Um pequeno café precisa de software caro para governar seus dados? *Rubrica:* 3 = não;; 2 = correto;; 1 = sim;; 0 = nenhuma.
- **EX005 — Situação das alergias.** Por que as anotações de alergia exigem cuidado adicional? *Rubrica:* 3 = são informações de saúde, dados de categoria especial;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX006 — Exemplo de dado de funcionário.** Cite um tipo de dado de funcionário que a Copperleaf mantém. *Rubrica:* 3 = nomes, telefones ou escalas;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX007 — Risco com fornecedores.** Que risco financeiro Kwame listou? *Rubrica:* 3 = pagar duas vezes a um fornecedor por notas duplicadas;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX008 — Risco das alergias.** O que a perda das anotações de alergia poderia causar? *Rubrica:* 3 = servir a comida errada;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX009 — Quem responde.** Quem responde por todos os dados da Copperleaf? *Rubrica:* 3 = a Sra. Adeyemi;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX010 — Responsável pelo boletim.** Quem cuida da lista do boletim? *Rubrica:* 3 = Kwame;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX011 — Responsável pelas escalas.** Quem cuida das escalas? *Rubrica:* 3 = o subgerente;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX012 — Regra dos sistemas aprovados.** Qual é a terceira decisão? *Rubrica:* 3 = nenhum dado de cliente ou funcionário sai dos sistemas aprovados;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX013 — Registro das decisões.** Onde as três decisões estão escritas? *Rubrica:* 3 = em uma única página;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Responsabilidade, regras e práticas seguras

### Objetivos de aprendizagem

Você vai (1) escrever regras simples para cada tipo de dado; (2) aplicar hábitos básicos de segurança; (3) decidir por quanto tempo guardar os registros.

### 2.1 Regras simples

Kwame escreve uma página de regras com a ajuda da Sra. Fischer. Os e-mails do boletim são usados apenas para o boletim. As anotações de alergia ficam em uma pasta trancada atrás do balcão e só são mostradas a quem prepara o pedido daquele cliente. As escalas são compartilhadas pelo grupo de mensagens da equipe pago pelo café, e não por redes sociais pessoais. As notas fiscais são arquivadas por fornecedor e data em uma única pasta compartilhada. Cada regra nomeia o responsável, para que a equipe saiba a quem perguntar. A página cabe em um só lado da folha e fica fácil de ler em poucos minutos.

### 2.2 Pedindo só o necessário

A antiga folha de inscrição pedia nome, e-mail, telefone, data de aniversário e endereço residencial. Kwame pergunta por quê. A Sra. Adeyemi responde que só o e-mail é necessário para o boletim, e que o primeiro nome deixa os e-mails mais simpáticos. Kwame retira telefone, aniversário e endereço da nova folha. A Sra. Fischer explica que coletar menos dados significa menos a proteger, menos a perder e menos perguntas dos clientes sobre por que o café quer seus dados; é o princípio da necessidade da LGPD (art. 6º, III). A nova folha é mais rápida de preencher, e mais clientes se inscrevem na primeira semana.

### 2.3 Hábitos de segurança

Kwame lista hábitos para a equipe: bloquear a tela do computador do caixa ao se afastar, usar logins separados no sistema do caixa em vez de um código compartilhado, manter a folha de inscrição fora do alcance dos clientes, nunca fotografar dados de clientes com celulares pessoais e relatar a Kwame no mesmo dia papéis ou aparelhos perdidos. Ele explica cada hábito na reunião seguinte da equipe com um exemplo real do que poderia acontecer, como um cliente lendo a folha de inscrição deixada no balcão. A equipe concorda prontamente e sugere afixar a lista perto do caixa.

### 2.4 Guardar e eliminar

Kwame define os prazos de guarda. Os e-mails do boletim são guardados enquanto o cliente continuar inscrito e eliminados logo depois do cancelamento. As escalas antigas são guardadas pelo período exigido pelas regras trabalhistas e depois eliminadas. As notas fiscais são guardadas pelo período exigido pelas regras fiscais. As anotações de alergia são revistas com o cliente a cada seis meses. As fotos de eventos são eliminadas após um ano, salvo se as pessoas concordaram com um uso mais longo. Ele escreve cada prazo ao lado da regra correspondente. A Sra. Adeyemi confere os prazos fiscais e trabalhistas com seu contador.

### 2.5 Obtendo a concordância

Kwame mostra as regras à Sra. Adeyemi e ao subgerente. O subgerente pergunta se a equipe ainda pode trocar turnos por mensagem de texto. Eles combinam que as trocas passam pelo grupo de mensagens pago, que mantém os números em sigilo. A Sra. Adeyemi assina a página e pede a Kwame que a afixe na sala da equipe. A Sra. Fischer lembra que as regras funcionam quando as pessoas as entendem, por isso ele deve explicar as mudanças em vez de apenas anunciá-las. Kwame explica cada mudança na reunião seguinte da equipe e responde às dúvidas de quem chegou depois.

### Exemplo resolvido

Kwame escreve regras que nomeiam os responsáveis, reduz a folha de inscrição ao primeiro nome e ao e-mail, lista hábitos de segurança explicados com exemplos, define prazos de guarda e obtém a assinatura das regras, que ficam afixadas na sala da equipe.

> **Caso sintético.** As regras são sintéticas.

### Erros e limites

Copiar a política longa de uma grande empresa para um café produz regras que ninguém lê.

### Exercícios

- **EX014 — Uso do boletim.** Para que podem ser usados os e-mails do boletim? *Rubrica:* 3 = apenas para o boletim;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX015 — Acesso às alergias.** Quem pode ver as anotações de alergia? *Rubrica:* 3 = quem prepara o pedido daquele cliente;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX016 — Canal das escalas.** Como as escalas são compartilhadas? *Rubrica:* 3 = pelo grupo de mensagens pago da equipe;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX017 — Campos mantidos.** Que campos continuam na nova folha de inscrição? *Rubrica:* 3 = primeiro nome e e-mail;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX018 — Benefício de coletar menos.** Por que coletar menos dados? *Rubrica:* 3 = menos a proteger, perder ou explicar;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX019 — Login do caixa.** O que substitui o código compartilhado do caixa? *Rubrica:* 3 = logins separados;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX020 — Relato de perdas.** Quando papéis perdidos devem ser relatados? *Rubrica:* 3 = no mesmo dia;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX021 — Após o cancelamento.** O que acontece com os e-mails após o cancelamento da inscrição? *Rubrica:* 3 = são eliminados logo depois;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX022 — Revisão das alergias.** Com que frequência as anotações de alergia são revistas? *Rubrica:* 3 = a cada seis meses;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX023 — Prazo das fotos.** Por quanto tempo as fotos de eventos são guardadas por padrão? *Rubrica:* 3 = um ano;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX024 — Troca de turnos.** Como a equipe troca turnos agora? *Rubrica:* 3 = pelo grupo de mensagens pago;; 2 = correto;; 1 = por mensagem de texto;; 0 = nenhuma.
- **EX025 — Local das regras.** Onde as regras assinadas ficam expostas? *Rubrica:* 3 = na sala da equipe;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX026 — Explicando as mudanças.** O que, segundo a Sra. Fischer, faz as regras funcionarem? *Rubrica:* 3 = as pessoas entenderem as regras;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Qualidade, sistemas e fornecedores

### Objetivos de aprendizagem

Você vai (1) conferir a qualidade dos dados em um pequeno negócio; (2) mapear onde os dados ficam guardados; (3) avaliar os fornecedores que lidam com os dados do café.

### 3.1 Qualidade em palavras simples

A Sra. Fischer explica a qualidade com três perguntas: o dado está completo, é válido e é exato? Na lista do boletim, completo significa que toda linha tem um e-mail, válido significa que cada e-mail parece um endereço real e exato significa que ele pertence à pessoa que se inscreveu. Kwame acrescenta uma quarta pergunta, sobre duplicatas: a mesma pessoa aparece duas vezes? Ele observa que a má qualidade desperdiça esforço e irrita os clientes que recebem duas cópias de cada e-mail. Kwame escreve as quatro perguntas no caderno, para usá-las nas verificações que vai montar mais adiante.

### 3.2 Onde os dados ficam

Kwame desenha um mapa simples de onde ficam os dados da Copperleaf: a folha de inscrição em papel, o serviço de boletins, o sistema do fornecedor do caixa, o grupo de mensagens da equipe, uma pasta compartilhada para as notas fiscais e a pasta trancada das alergias. Para cada lugar, anota quem pode ver e se está protegido. Ele encontra no notebook do café uma planilha antiga com e-mails de clientes que ninguém usa. A Sra. Adeyemi concorda que ele a elimine depois de conferir que ela não contém nada necessário. Kwame guarda o mapa junto com as regras, para atualizá-lo quando algo mudar.

### 3.3 Fornecedores

Três fornecedores lidam com os dados da Copperleaf: o serviço de boletins, o fornecedor do caixa e dos pagamentos com cartão e o aplicativo de mensagens. Kwame confere os termos de cada um em busca de compromissos de proteção de dados, como manter os dados seguros, usá-los só para a Copperleaf e eliminá-los no fim do contrato; na LGPD, quem trata dados em nome do controlador é o operador (art. 39). O serviço de boletins e o fornecedor do caixa incluem esses termos. O aplicativo de mensagens é uma versão pessoal gratuita, sem termos empresariais, então a Sra. Adeyemi passa para a versão empresarial paga.

### 3.4 Pagamentos e notas fiscais

Kwame examina as notas fiscais e encontra duas cópias da mesma nota de um fornecedor, uma por e-mail e outra em papel, com datas ligeiramente diferentes. O café quase pagou duas vezes. Ele sugere que as notas sejam lançadas uma única vez, a partir da cópia recebida por e-mail, com a cópia em papel marcada como recebida. A Sra. Adeyemi concorda. A Sra. Fischer observa que registros duplicados também são um problema de qualidade nos dados financeiros, e que um único ponto de entrada evita a maioria deles. O contador também aprova a mudança, porque ela torna os registros mensais mais fáceis de conferir.

### 3.5 Verificações simples

Kwame define três verificações mensais: procurar e-mails duplicados ou malformados na lista do boletim, confirmar que só funcionários atuais estão no grupo de mensagens e comparar as notas lançadas com os pagamentos feitos. Cada verificação leva poucos minutos. Ele registra a data e o que encontrou em um caderno guardado com as regras. A Sra. Fischer explica que verificações curtas e regulares pegam os problemas cedo e mostram que as regras estão sendo seguidas. Depois do primeiro mês, o caderno já mostra um e-mail duplicado removido e um ex-funcionário retirado do grupo de mensagens.

### Exemplo resolvido

Kwame define a qualidade com completude, validade, exatidão e duplicatas, mapeia onde os dados ficam e elimina uma planilha de e-mails sem uso, passa as mensagens da equipe para uma versão empresarial, impede notas duplicadas no lançamento e define três verificações mensais.

> **Caso sintético.** Os sistemas e fornecedores são sintéticos.

### Erros e limites

Aplicativos pessoais gratuitos usados para dados do negócio muitas vezes não têm os termos de que uma empresa precisa.

### Exercícios

- **EX027 — Perguntas de qualidade.** Que três perguntas de qualidade a Sra. Fischer usa? *Rubrica:* 3 = completo, válido, exato;; 2 = todas;; 1 = algumas;; 0 = nenhuma.
- **EX028 — Pergunta acrescentada.** Que quarta pergunta Kwame acrescentou? *Rubrica:* 3 = se a mesma pessoa aparece duas vezes;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX029 — Planilha esquecida.** Que arquivo esquecido estava no notebook do café? *Rubrica:* 3 = uma planilha antiga de e-mails de clientes;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX030 — Condição para eliminar.** O que foi conferido antes de eliminá-la? *Rubrica:* 3 = que não continha nada necessário;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX031 — Número de fornecedores.** Quantos fornecedores lidam com os dados da Copperleaf? *Rubrica:* 3 = três;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX032 — Termos dos fornecedores.** Com o que os termos dos fornecedores devem se comprometer? *Rubrica:* 3 = segurança, uso só para a Copperleaf e eliminação no fim;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX033 — Correção das mensagens.** O que mudou no aplicativo de mensagens? *Rubrica:* 3 = passou para a versão empresarial paga;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX034 — Nota duplicada.** Por que o café quase pagou duas vezes? *Rubrica:* 3 = cópias por e-mail e em papel da mesma nota;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX035 — Regra de lançamento.** Que cópia da nota é lançada? *Rubrica:* 3 = a cópia recebida por e-mail;; 2 = correto;; 1 = a de papel;; 0 = nenhuma.
- **EX036 — Verificação das mensagens.** O que a verificação do grupo de mensagens confirma? *Rubrica:* 3 = que só funcionários atuais são membros;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX037 — Registro das verificações.** Onde os resultados das verificações são registrados? *Rubrica:* 3 = em um caderno guardado com as regras;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX038 — Tempo das verificações.** Quanto tempo leva cada verificação mensal? *Rubrica:* 3 = poucos minutos;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Laboratório guiado e plano de ação

### Objetivos de aprendizagem

Você vai (1) conferir uma lista sintética de inscrições com um script curto; (2) decidir quem pode receber o boletim; (3) escrever um plano de ação de um mês.

### 4.1 A lista de inscrições

A lista do boletim da Copperleaf foi digitada a partir das folhas de papel por funcionários diferentes. Algumas linhas têm e-mail em branco, algumas têm o mesmo endereço digitado duas vezes com maiúsculas ou espaços diferentes e algumas não têm marcação na caixa de consentimento. Kwame quer saber para quantos endereços o café pode de fato enviar e-mails. A Sra. Fischer o ajuda a escrever um script curto em Python usando só a biblioteca padrão, executado sobre uma lista sintética de doze linhas que reproduz esses problemas sem usar nenhum dado real de cliente. Kwame o executa.

```python
"""Check a synthetic cafe newsletter sign-up list: blanks, duplicates and consent ticks (stdlib only)."""
rows = [("ana@example.org", "yes"), ("Ana@Example.org ", "yes"), ("", "yes"), ("ben@example.org", ""),
        ("cai@example.org", "yes"), ("dee@example", "yes"), ("eli@example.org", "no"), ("fay@example.org", "yes"),
        ("cai@example.org", "yes"), ("gus@example.org", "yes"), ("", ""), ("hal@example.org", "yes")]
clean = [(e.strip().lower(), c) for e, c in rows]
blank = sum(1 for e, _ in clean if not e)
bad = sum(1 for e, _ in clean if e and ("@" not in e or "." not in e.split("@")[-1]))
seen, dup = set(), 0
for e, _ in clean:
    if e and e in seen: dup += 1
    seen.add(e)
ok = {e for e, c in clean if e and c == "yes" and "." in e.split("@")[-1]}
print(f"rows {len(rows)}; blank email {blank}; malformed {bad}; duplicates {dup}")
print(f"unique valid addresses with a yes tick: {len(ok)}")
```

Execute com `python3 lab_signups.py`. Saída verificada:

```text
rows 12; blank email 2; malformed 1; duplicates 2
unique valid addresses with a yes tick: 5
```

### 4.2 O que o laboratório encontra

O script remove os espaços e converte cada endereço para minúsculas antes de conferi-lo. Das doze linhas, duas têm e-mail em branco, um endereço está malformado porque não tem uma terminação adequada depois da arroba e duas linhas duplicam endereços já listados. Depois de retirados os problemas, só cinco endereços únicos e válidos têm um sim na caixa de consentimento. Kwame se surpreende: doze linhas no papel viram cinco pessoas a quem o café pode mandar e-mails com segurança. Ele mostra o resultado à Sra. Adeyemi, que esperava uma lista muito maior e pede que ele explique cada problema encontrado.

### 4.3 Decidindo para quem enviar

A Sra. Fischer explica que os e-mails de marketing exigem o consentimento do cliente, e que o café precisa conseguir demonstrá-lo; na LGPD, o consentimento deve ser livre, informado e inequívoco (art. 5º, XII), e cabe ao controlador provar que o obteve (art. 8º, § 2º). As linhas com marcação em branco ou com não ficam de fora. O endereço malformado não pode ser usado de qualquer forma. Kwame e a Sra. Adeyemi decidem enviar e-mails aos cinco endereços confirmados e convidar pessoalmente os outros clientes a assinar a nova folha, se quiserem o boletim. Ele registra a decisão e a data no caderno.

### 4.4 O plano de ação

Kwame escreve um plano de um mês com cinco ações: trocar a folha de inscrição pela versão mais curta, com uma caixa de consentimento clara e a data; executar a verificação do laboratório todo mês na lista digitada; eliminar a planilha esquecida; concluir a mudança para o aplicativo de mensagens pago; e explicar as regras na reunião seguinte da equipe. Cada ação tem um responsável e uma data. A Sra. Adeyemi o aprova, e Kwame o afixa ao lado das regras. Ele mantém o plano curto para que possa de fato ser concluído em um mês, sem competir com o trabalho do café.

### 4.5 Depois do curso

No fim do mês, Kwame revisa o andamento. Quatro ações estão concluídas; a reunião da equipe foi adiada para a semana seguinte. Ele reflete que decisões pequenas e claras mudaram mais do que esperava, e que conferir os dados com um script curto tornou o problema visível para todos. A Sra. Fischer sugere que ele continue com privacidade e proteção de dados, já que os dados de clientes e funcionários são centrais para o café. O próximo curso desta área faz exatamente isso. Kwame agradece à Sra. Fischer e se inscreve no mês seguinte, levando o caderno do curso.

### Exemplo resolvido

Kwame confere doze linhas sintéticas de inscrição e encontra dois e-mails em branco, um endereço malformado e duas duplicatas, restando cinco endereços únicos e válidos com consentimento; ele decide enviar e-mails só a esses e conclui quatro das cinco ações de seu plano de um mês.

> **Caso sintético.** A lista é sintética; as saídas vêm de lab_signups.py; o GDPR e a LGPD são reais. Isto não é aconselhamento jurídico.

### Erros e limites

Contar linhas em vez de endereços únicos, válidos e com consentimento superestima quem pode receber e-mails.

### Exercícios

- **EX039 — Linhas do laboratório.** Quantas linhas tem a lista sintética? *Rubrica:* 3 = doze;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX040 — E-mails em branco.** Quantas linhas têm e-mail em branco? *Rubrica:* 3 = duas;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX041 — Malformados.** Quantos endereços estão malformados? *Rubrica:* 3 = um;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX042 — Linhas duplicadas.** Quantas linhas duplicadas o script encontra? *Rubrica:* 3 = duas;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX043 — Total que pode receber.** Quantos endereços únicos e válidos têm um sim? *Rubrica:* 3 = cinco;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX044 — Etapas de normalização.** O que o script faz antes de conferir cada endereço? *Rubrica:* 3 = remove espaços e converte para minúsculas;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX045 — Marcação em branco.** As linhas com marcação em branco recebem e-mails? *Rubrica:* 3 = não;; 2 = correto;; 1 = sim;; 0 = nenhuma.
- **EX046 — Outros clientes.** Como os outros clientes vão entrar no boletim? *Rubrica:* 3 = assinando pessoalmente a nova folha;; 2 = correto;; 1 = vago;; 0 = nenhuma.
- **EX047 — Ações do plano.** Quantas ações tem o plano de um mês? *Rubrica:* 3 = cinco;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX048 — Itens da nova folha.** O que a nova folha inclui? *Rubrica:* 3 = uma caixa de consentimento clara e a data;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX049 — Ação atrasada.** Que ação atrasou? *Rubrica:* 3 = a explicação das regras na reunião da equipe;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX050 — Próximo tema.** O que a Sra. Fischer sugere em seguida? *Rubrica:* 3 = privacidade e proteção de dados;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Kwame Boateng, a Sra. Lena Fischer, o Riverside Adult Learning Centre, o Copperleaf Café e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Dois.

**EX002.** Gerente de dados de uma prefeitura.

**EX003.** Combinar quem é responsável, que regras valem e como elas são conferidas.

**EX004.** Não; responsáveis, regras e verificações bastam para começar.

**EX005.** São informações de saúde, uma categoria especial no GDPR e dado sensível na LGPD.

**EX006.** As escalas da equipe.

**EX007.** Pagar duas vezes a um fornecedor porque existem duas cópias da nota.

**EX008.** Servir a um cliente uma comida que lhe faz mal.

**EX009.** A Sra. Adeyemi, a dona.

**EX010.** Kwame.

**EX011.** O subgerente.

**EX012.** Os dados de clientes e funcionários ficam dentro dos sistemas aprovados.

**EX013.** Em uma única página aprovada pela Sra. Adeyemi.

**EX014.** Apenas o boletim.

**EX015.** Apenas quem prepara o pedido daquele cliente.

**EX016.** Pelo grupo de mensagens pago da equipe do café.

**EX017.** Primeiro nome e e-mail.

**EX018.** Há menos a proteger, perder ou explicar.

**EX019.** Logins separados para cada pessoa.

**EX020.** No mesmo dia, a Kwame.

**EX021.** São eliminados logo depois.

**EX022.** A cada seis meses, com o cliente.

**EX023.** Um ano, salvo se as pessoas concordaram com um uso mais longo.

**EX024.** Pelo grupo de mensagens pago, que mantém os números em sigilo.

**EX025.** Afixadas na sala da equipe.

**EX026.** As pessoas entenderem por que as regras existem.

**EX027.** Está completo, é válido e é exato?

**EX028.** Se a mesma pessoa aparece duas vezes.

**EX029.** Uma planilha antiga de e-mails de clientes.

**EX030.** Que não continha nada de que o café ainda precisasse.

**EX031.** Três.

**EX032.** Segurança, uso apenas para a Copperleaf e eliminação no fim.

**EX033.** A Copperleaf passou para a versão empresarial paga.

**EX034.** A mesma nota existia como cópia por e-mail e em papel.

**EX035.** A cópia recebida por e-mail, com a de papel marcada como recebida.

**EX036.** Que só funcionários atuais estão no grupo.

**EX037.** Em um caderno guardado com as regras.

**EX038.** Poucos minutos.

**EX039.** Doze.

**EX040.** Dois e-mails em branco.

**EX041.** Um endereço malformado.

**EX042.** Duas linhas duplicadas.

**EX043.** Cinco.

**EX044.** Remove os espaços e converte para minúsculas.

**EX045.** Não; marcações em branco não valem como consentimento.

**EX046.** Assinando pessoalmente a nova folha, se quiserem.

**EX047.** Cinco ações.

**EX048.** Uma caixa de consentimento clara e a data.

**EX049.** A explicação das regras na reunião da equipe, adiada em uma semana.

**EX050.** Privacidade e proteção de dados.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
