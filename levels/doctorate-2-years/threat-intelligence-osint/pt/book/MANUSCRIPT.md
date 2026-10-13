# Inteligência de ameaças e OSINT: um livro de pesquisa para o doutorado

- Idioma: português do Brasil (`pt`); trilha de pesquisa de doutorado, dois anos. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–8 de 8 têm texto didático escrito; os exercícios EX001–EX056 têm resoluções correspondentes com rubricas de 0 a 3; três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas vêm de execuções reais. A revisão independente e a verificação de 300 páginas A4 continuam em aberto.
- Público: doutorandos que desenham uma contribuição original e testável ao método de inteligência de ameaças cibernéticas (CTI) ou de inteligência de fontes abertas (OSINT).
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite ético: nenhuma coleta sobre pessoas privadas reais, nenhuma evasão de termos de uso, nenhuma desanonimização, nenhuma intrusão na infraestrutura de adversários. Todos os conjuntos de dados, pessoas e organizações são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

O capítulo 1 estabelece a integridade da pesquisa; o 2 mapeia a fronteira; o 3 formula uma contribuição; o 4 replica linhas de base; o 5 conduz o estudo principal com validação independente; o 6 lida com a crítica; o 7 monta a tese e o arquivo; o 8 prepara a defesa e a publicação. Cada capítulo tem objetivos, texto didático, um exemplo resolvido, um caso sintético rotulado, erros e limites, sete exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**.

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Larkspur CTI Lab** — grupo de pesquisa universitário com um corpus de 1.200 relatórios sintéticos de CTI | Sede da pesquisa | Inventado |
| **Tomas Ekberg** | Doutorando que estuda em que medida a linguagem de confiança dos relatórios de CTI corresponde aos desfechos | Inventado |
| **Dra. Hana Sato** | Orientadora | Inventada |

### Fontes principais

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) e [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); o [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); o [artigo da kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf) de Hutchins et al.; NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridade e métodos avançados de pesquisa

### Objetivos de aprendizagem

Você vai (1) enunciar as obrigações de integridade que se aplicam à pesquisa em CTI e OSINT; (2) separar os dados que você pode legitimamente coletar dos dados que você apenas consegue coletar; (3) pré-registrar uma pergunta, um método e um plano de análise; (4) montar um dossiê de ética que um comitê de revisão possa aprovar.

### 1.1 Por que a pesquisa em CTI precisa de regras próprias de integridade

A pesquisa em inteligência de ameaças toca ao mesmo tempo três populações sensíveis: as vítimas citadas em relatórios de incidentes, os analistas cujos julgamentos são estudados e as pessoas que aparecem incidentalmente em fontes abertas. Um desenho estatisticamente sólido ainda pode ser antiético se reidentificar uma organização vítima a partir de um relatório sanitizado ou se raspar um fórum contra os termos de uso dele. Por isso, a integridade nesta área combina a ética de pesquisa comum — honestidade, transparência, nenhuma fabricação — com a legislação de proteção de dados, como o Regulamento Geral sobre a Proteção de Dados (GDPR) da União Europeia, e com as restrições de compartilhamento que as próprias fontes carregam, por exemplo os rótulos do FIRST TLP 2.0. No Brasil, o papel equivalente cabe à Lei Geral de Proteção de Dados Pessoais (LGPD, Lei nº 13.709/2018), cujo cumprimento é fiscalizado pela Autoridade Nacional de Proteção de Dados (ANPD).

### 1.2 Poder versus ter permissão

Visibilidade pública não equivale a permissão. Uma página de perfil pode ser acessível sem login e, ainda assim, os termos da plataforma podem proibir a coleta automatizada, e os dados da pessoa podem continuar sendo dados pessoais segundo o GDPR. A regra de Tomas: antes de qualquer coleta, registre por escrito a base legal, os termos aplicáveis, a etapa de minimização e o prazo de retenção. Se qualquer um dos quatro estiver em branco, a coleta espera. O corpus do fórum mostra a regra funcionando: as postagens eram acessíveis sem login, mas os termos do fórum proibiam a raspagem para pesquisa e nenhuma permissão foi concedida, de modo que o campo "termos aplicáveis" não podia ser preenchido com honestidade e o corpus foi descartado antes de qualquer coleta.

### 1.3 Pré-registro

Pré-registrar a pergunta de pesquisa, as hipóteses, o esquema de codificação e o plano de análise antes de ver os dados de desfecho protege contra o ajuste inconsciente. Em CTI, onde as narrativas de atribuição seduzem, isso importa: assim que um nome de grupo como APT29 (ATT&CK G0016) aparece em um relatório, os analistas tendem a ler cada artefato posterior como confirmação. A obra *Psychology of Intelligence Analysis*, de Heuer, documenta essa tendência no julgamento humano. Para Tomas, o pré-registro fixa de antemão o mapeamento de cada expressão estimativa para uma probabilidade e a regra de codificação de um desfecho. Se esses itens fossem escolhidos depois de ver quais afirmações se confirmaram, ele poderia, sem querer, colocar uma expressão como "provável" onde quer que ela melhorasse a curva de calibração.

### 1.4 O dossiê de ética

O dossiê contém: inventário de dados, base legal, tratamento TLP de cada fonte, método de desidentificação, local de armazenamento, lista de acesso, prazo de retenção e um plano para achados incidentais (por exemplo, descobrir em uma amostra um comprometimento ativo não comunicado). Este último item é específico da pesquisa em segurança e costuma faltar. O dossiê de Tomas nomeia um caminho concreto para esse último item: se a codificação revelar indícios de que uma organização citada ainda pode estar comprometida, ele avisa a Dra. Sato, que contata um coordenador adequado por meio da comunidade de compartilhamento, e ele mesmo não sonda a organização. Os 200 relatórios TLP:AMBER+STRICT têm linha própria: análise só dentro do laboratório, nenhuma citação, relato agregado.

### Exemplo resolvido

Tomas planeja estudar 1.200 relatórios de CTI. Duzentos deles têm o rótulo TLP:AMBER+STRICT de uma comunidade de compartilhamento. Seu dossiê de ética registra que esses só podem ser analisados dentro do laboratório, nunca citados, e que os resultados serão relatados de forma agregada. Um corpus adicional de postagens de fórum é descartado porque os termos do fórum proíbem a raspagem para pesquisa e nenhuma permissão foi concedida.

> **Caso sintético.** O Larkspur CTI Lab, seu corpus e o dossiê de ética de Tomas são inventados.

### Erros e limites

Supor que "público significa livre para usar" é a falha de integridade mais comum. O pré-registro não proíbe o trabalho exploratório; exige que ele seja rotulado como exploratório. Este capítulo não é aconselhamento jurídico.

### Exercícios

- **EX001 — Quatro campos em branco.** Liste os quatro itens que Tomas precisa preencher antes de iniciar qualquer coleta. *Rubrica:* 3 = base legal, termos aplicáveis, minimização, retenção; 2 = três; 1 = um ou dois; 0 = nenhum.
- **EX002 — Corpus âmbar.** Como Tomas pode usar os relatórios TLP:AMBER+STRICT na tese? *Rubrica:* 3 = análise apenas dentro da organização, sem citação nem redistribuição, relato agregado; 2 = restringe o compartilhamento de forma vaga; 1 = citar livremente; 0 = nenhuma.
- **EX003 — Recusa do fórum.** Por que descartar o corpus do fórum é correto, embora as postagens sejam visíveis sem login? *Rubrica:* 3 = os termos proíbem a raspagem, não há permissão, há questões de dados pessoais; 2 = um motivo; 1 = visível significa permitido; 0 = nenhum.
- **EX004 — Comprometimento incidental.** Ao codificar um relatório, Tomas nota indícios de que uma organização citada ainda pode estar comprometida. O que o dossiê de ética deveria ter previsto? *Rubrica:* 3 = caminho de escalonamento previamente acordado (orientadora, CERT/coordenador) sem investigação própria; 2 = avisar apenas a orientadora; 1 = investigar por conta própria; 0 = nenhum.
- **EX005 — Armadilha da confirmação.** Que viés o pré-registro ajuda a conter na pesquisa sobre atribuição, e como? *Rubrica:* 3 = viés de confirmação; fixa hipóteses e codificação antes dos desfechos; 2 = nomeia o viés; 1 = viés não relacionado; 0 = nenhum.
- **EX006 — Rótulo exploratório.** Tomas encontra um padrão inesperado que não estava no plano. Como deve relatá-lo? *Rubrica:* 3 = relatar como exploratório, separado do confirmatório, propor acompanhamento; 2 = relatar com rótulo fraco; 1 = apresentar como planejado; 0 = nenhum.
- **EX007 — Lista de acesso.** Quem deve constar na lista de acesso do subconjunto AMBER+STRICT? *Rubrica:* 3 = apenas membros nomeados do laboratório com necessidade de conhecer, sob o acordo de compartilhamento; 2 = membros do laboratório em geral; 1 = qualquer pessoa da universidade; 0 = nenhum.

### Síntese

Registre a base legal, os termos, a minimização e a retenção antes de coletar; respeite o TLP; pré-registre; planeje os achados incidentais.

### Continue estudando — capítulo 01 de 08

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Inteligência de ameaças e OSINT: fronteira da pesquisa

### Objetivos de aprendizagem

Você vai (1) mapear os principais problemas em aberto no método de CTI; (2) distinguir os modelos (kill chain, Diamond, ATT&CK) pelo que cada um afirma; (3) identificar onde a evidência da literatura é escassa; (4) escrever uma declaração de lacuna que um revisor não possa descartar como mero resumo da literatura.

### 2.1 Três modelos, três afirmações

Hutchins, Cloppert e Amin (2011) propuseram a *intrusion kill chain* — reconhecimento, armamento, entrega, exploração, instalação, comando e controle, ações sobre os objetivos — e argumentaram que os defensores vencem ao quebrar qualquer elo e ao analisar campanhas em vez de incidentes isolados. Caltagirone, Pendergast e Betz (2013) propuseram o Diamond Model: todo evento tem adversário, capacidade, infraestrutura e vítima, e os analistas fazem pivôs ao longo das arestas. O MITRE ATT&CK é uma base de conhecimento curada de táticas, técnicas e grupos observados. O primeiro é uma estratégia defensiva, o segundo uma ontologia analítica, o terceiro um catálogo empírico. Uma pesquisa que os trate como intercambiáveis vai confundir as próprias afirmações.

### 2.2 Problemas em aberto

Várias perguntas continuam com pouca evidência: em que medida a linguagem de confiança dos relatórios prevê a confirmação posterior; quanto o compartilhamento de indicadores realmente reduz danos (o NIST SP 800-150 descreve como compartilhar, não quanto benefício resulta); quão reprodutível é a atribuição entre equipes independentes; e como medir o valor da inteligência estratégica para quem decide. Cada uma é pesquisável com um desenho cuidadoso e dados sintéticos ou consentidos. A tese de Tomas assume a primeira pergunta. As demais pedem outros desenhos: a redução de danos pelo compartilhamento exigiria dados de desfecho das organizações, e a reprodutibilidade da atribuição exigiria equipes independentes trabalhando sobre os mesmos artefatos, razão pela qual aparecem como trabalho futuro, e não na proposta dele.

### 2.3 Fronteira do método OSINT

A investigação em fontes abertas cresceu mais depressa do que sua validação. As perguntas incluem as taxas de erro de geolocalização, a confiabilidade das capturas arquivadas da web e os custos de privacidade de agregar fatos públicos individualmente inofensivos. O trabalho de doutorado aqui precisa pesar o valor da pesquisa contra o dano de construir ferramentas de agregação. O corpus de Tomas evita deliberadamente essa fronteira: usa relatórios, não pessoas, e o corpus do fórum foi descartado. Uma tese que geolocalizasse imagens ou vinculasse perfis públicos precisaria de um dossiê de ética muito mais pesado, porque cada etapa de agregação pode criar um perfil de uma pessoa que nenhum fato público isolado revelava.

### 2.4 Escrevendo a lacuna

Uma boa declaração de lacuna tem três partes: o que se sabe (com citações), o que não se sabe (enunciado com precisão) e por que isso importa para uma decisão. "Há pouca pesquisa sobre CTI" não é uma lacuna; "nenhum estudo publicado mede a calibração da linguagem estimativa em relatórios de CTI de fornecedores em relação à confirmação posterior" é. A declaração do próprio Tomas segue as três partes: a norma é conhecida, já que a ICD 203 exige expressar a incerteza e Kent propôs um vocabulário estimativo; nenhuma medição de calibração em CTI comercial apareceu entre os 40 artigos e relatórios que ele revisou; e isso importa porque as equipes de SOC decidem bloquear ou não com base nessas expressões.

### Exemplo resolvido

Tomas revisa 40 artigos e relatórios. Encontra muitas descrições da exigência da ICD 203 de expressar a incerteza e do vocabulário de probabilidade estimativa de Kent, mas nenhuma medição de calibração em CTI comercial. Sua declaração de lacuna nomeia essa ausência, cita Kent e a ICD 203 para a norma e a liga à tomada de decisão do SOC sobre bloqueios.

> **Caso sintético.** O número de itens revisados por Tomas e sua declaração de lacuna são inventados.

### Erros e limites

Blogs de fornecedores são evidência de prática, não resultados revisados por pares; rotule-os. O entusiasmo pela fronteira não justifica construir ferramentas de vigilância.

### Exercícios

- **EX008 — Afirmações dos modelos.** Em uma linha cada, diga que tipo de coisa são a kill chain, o Diamond Model e o ATT&CK. *Rubrica:* 3 = modelo de estratégia/fases; ontologia de eventos; base de conhecimento empírica; 2 = dois certos; 1 = um; 0 = nenhum.
- **EX009 — Lacuna fraca.** Reescreva "não há muita pesquisa sobre compartilhamento de ameaças" como uma lacuna precisa. *Rubrica:* 3 = incógnita específica + população + medida; 2 = mais específica, mas não mensurável; 1 = inalterada; 0 = nenhuma.
- **EX010 — Pivô no Diamond.** Nomeie as quatro características centrais e um pivô que um analista poderia fazer. *Rubrica:* 3 = adversário, capacidade, infraestrutura, vítima + pivô válido (por exemplo, infraestrutura→outras vítimas); 2 = apenas as características; 1 = parcial; 0 = nenhum.
- **EX011 — Dano por agregação.** Por que combinar fatos públicos inofensivos sobre uma pessoa pode criar um problema ético para a pesquisa em OSINT? *Rubrica:* 3 = a agregação permite identificação/perfilamento/dano; deveres de proteção de dados; 2 = menciona privacidade; 1 = não há problema; 0 = nenhum.
- **EX012 — Classificação de fontes.** Como Tomas deve citar um blog de fornecedor na revisão da literatura? *Rubrica:* 3 = citar, mas rotular como literatura cinzenta/evidência de prática, não revisada por pares; 2 = citar com cautela; 1 = tratar como revisado por pares; 0 = nenhum.
- **EX013 — Escopo do SP 800-150.** O que o NIST SP 800-150 oferece e o que ele não mede? *Rubrica:* 3 = orientação sobre relações/práticas de compartilhamento; não mede empiricamente o benefício; 2 = uma metade; 1 = errado; 0 = nenhum.
- **EX014 — Tese da kill chain.** Enuncie em uma frase o argumento defensivo central de Hutchins et al. *Rubrica:* 3 = quebrar qualquer fase + análise de campanhas/defesa orientada por inteligência; 2 = apenas quebrar a cadeia; 1 = não relacionado; 0 = nenhum.

### Síntese

Saiba o que cada modelo afirma, encontre lacunas precisas e ligadas a decisões, e pese o valor da pesquisa em OSINT contra o dano da agregação.

### Continue estudando — capítulo 02 de 08

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Proposta de contribuição original

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa falseável; (2) definir constructos e suas medidas operacionais; (3) escolher um desenho que possa falhar; (4) escrever, antes da coleta de dados, uma seção da proposta sobre ameaças à validade.

### 3.1 Perguntas falseáveis

"A linguagem de confiança importa" não pode falhar. "As afirmações rotuladas como 'altamente provável' no corpus são confirmadas depois a uma taxa pelo menos 20 pontos percentuais acima das afirmações rotuladas como 'possível'" pode falhar. Uma contribuição de doutorado faz jus ao nome quando se arrisca à refutação. O limiar de 20 pontos também dá à banca um número para discutir antes de os dados chegarem. Se os membros acharem que uma diferença de 10 pontos já importaria para as decisões de bloqueio, o momento certo de mudar o limiar é na proposta, registrado no pré-registro, e não depois de traçada a curva de calibração.

### 3.2 Constructos e medidas

Constructo: a confiança analítica tal como comunicada. Medida: a expressão estimativa do julgamento-chave, mapeada para um intervalo numérico em uma escala publicada, por exemplo as *words of estimative probability* de Kent. Constructo: a confirmação. Medida: se uma fonte posterior e autorizada do corpus — um resumo de denúncia judicial, uma retratação de fornecedor ou um alerta conjunto — apoia ou contradiz a afirmação em até 24 meses. Toda decisão de mapeamento é escrita em um livro de códigos. A janela de 24 meses é ela mesma uma escolha de desenho com custo: as afirmações feitas no fim do período do corpus têm menos tempo para se confirmar e, por isso, têm mais chance de ficar sem resolução. Por esse motivo o livro de códigos registra a data do relatório, e a análise pode verificar se a resolubilidade cai nos relatórios recentes.

### 3.3 Um desenho que pode falhar

Tomas escolhe um desenho de coorte retrospectivo: amostrar julgamentos-chave, codificar a probabilidade declarada, codificar os desfechos às cegas em relação à expressão original e calcular a calibração. O desenho falha se os desfechos forem impossíveis de conhecer para a maioria das afirmações; por isso, a proposta fixa um mínimo de 300 julgamentos resolúveis antes de a análise prosseguir. O piso é uma regra de parada pré-registrada, não uma meta. Se apenas 180 julgamentos amostrados se mostrarem resolúveis, Tomas precisa ampliar a amostra ou revisar o desenho conforme a regra escrita de antemão, e relatar o déficit; seguir em silêncio com 180 deixaria as faixas de alta confiança ralas demais para estimar.

### 3.4 Ameaças à validade

Interna: os codificadores podem inferir a expressão pelo contexto e enviesar a codificação do desfecho. De constructo: uma fonte de "desfecho" pode ela mesma depender do relatório original. Externa: os relatórios comerciais podem diferir dos governamentais. Estatística: faixas pequenas produzem calibração instável. Escrever isso agora permite à banca julgar o plano, e não a sorte do resultado. Cada ameaça tem uma resposta planejada. Os codificadores de desfecho veem as afirmações sem a expressão estimativa. A verificação de circularidade pedida pela banca sinaliza as fontes de desfecho que citam o relatório original. Os relatórios comerciais e os governamentais são analisados separadamente. A amostra principal dá peso maior aos julgamentos de alta confiança, para que as faixas do topo não sejam as menores — o ponto fraco que o piloto revelou.

### 3.5 A afirmação de contribuição

A afirmação é estreita: a primeira estimativa medida da calibração da linguagem estimativa em um corpus definido, sintético mais licenciado, com um livro de códigos aberto. Não é "a CTI não é confiável". Manter a afirmação estreita é o que torna publicável um resultado negativo. Se as afirmações de alta confiança se confirmarem tão pouco quanto as possíveis, a tese ainda entrega uma estimativa medida e um livro de códigos aberto que outros podem aplicar aos próprios corpora; uma afirmação ampla não teria para onde recuar. É por isso que o livro de códigos aberto faz parte da afirmação: permite que outras equipes testem a mesma pergunta nos próprios relatórios.

### Exemplo resolvido

A Dra. Sato contesta a primeira versão da pergunta, "Os fornecedores de CTI são confiantes demais?". Tomas a reescreve com um limiar mensurável, um corpus definido, uma etapa de codificação cega dos desfechos e um piso de resolubilidade. A banca aprova a proposta revisada, pedindo que se acrescente uma verificação de circularidade das fontes de desfecho.

> **Caso sintético.** A troca sobre a proposta é inventada.

### Erros e limites

Afirmações amplas demais atraem rejeição; constructos subespecificados não podem ser replicados. Uma proposta é um plano, não um resultado.

### Exercícios

- **EX015 — Torne falseável.** Reescreva "A atribuição costuma estar errada" como uma hipótese falseável. *Rubrica:* 3 = taxa mensurável, população, comparação ou limiar, prazo; 2 = mensurável, mas sem limiar; 1 = inalterada; 0 = nenhuma.
- **EX016 — Medida operacional.** Dê uma medida operacional para a "confirmação" de um julgamento-chave de CTI. *Rubrica:* 3 = fonte posterior autorizada definida + janela de tempo + codificação apoia/contradiz; 2 = fonte posterior vaga; 1 = impressão do analista; 0 = nenhuma.
- **EX017 — Verificação de circularidade.** Por que as fontes de desfecho precisam ser verificadas quanto à dependência do relatório original? *Rubrica:* 3 = a confirmação circular infla a calibração; são necessárias fontes independentes; 2 = parcial; 1 = não é necessário; 0 = nenhum.
- **EX018 — Codificação cega.** O que se ganha ao codificar os desfechos sem ver a expressão estimativa original? *Rubrica:* 3 = impede o viés do codificador/efeito de expectativa sobre o desfecho; 2 = justiça, de forma vaga; 1 = rapidez; 0 = nenhum.
- **EX019 — Piso de resolubilidade.** O que Tomas deve fazer se apenas 180 dos julgamentos amostrados forem resolúveis? *Rubrica:* 3 = não prosseguir como planejado; ampliar a amostra ou revisar o desenho conforme a regra pré-registrada; relatar o déficit; 2 = apenas ampliar; 1 = prosseguir em silêncio; 0 = nenhum.
- **EX020 — Classe de validade.** Classifique "os relatórios comerciais podem diferir dos governamentais" como um tipo de ameaça à validade. *Rubrica:* 3 = validade externa/generalização; 2 = validade, de forma vaga; 1 = interna; 0 = nenhum.
- **EX021 — Afirmação estreita.** Por que "a CTI não é confiável" é uma afirmação de contribuição inadequada para este estudo? *Rubrica:* 3 = generaliza além do corpus/constructo; o estudo mede apenas a calibração; 2 = ampla demais; 1 = está adequada; 0 = nenhum.

### Síntese

Arrisque-se à refutação, defina as medidas em um livro de códigos, desenhe a codificação cega, escreva primeiro as ameaças à validade e mantenha a afirmação exatamente tão ampla quanto a evidência.

### Continue estudando — capítulo 03 de 08

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Replicação da linha de base e piloto

### Objetivos de aprendizagem

Você vai (1) replicar uma linha de base simples, no estilo das publicadas, antes de construir sobre ela; (2) calcular um escore de Brier e faixas de calibração; (3) calcular a sobreposição de conjuntos entre feeds de indicadores; (4) decidir, a partir de um piloto, se o estudo principal é viável.

### 4.1 Por que replicar primeiro

Construir sobre uma linha de base não replicada acumula erros. Um piloto que reproduz uma medição conhecida e simples — como a sobreposição entre dois feeds de indicadores, grandeza muito discutida na literatura sobre compartilhamento — verifica se o seu pipeline, o parsing e as definições se comportam bem antes do estudo caro. O piloto de Tomas usa duas verificações desse tipo: a sobreposição de Jaccard entre dois pequenos feeds sintéticos de indicadores e um escore de Brier sobre doze julgamentos do piloto. As duas grandezas podem ser calculadas à mão, de modo que uma divergência entre o script e o cálculo manual aponta para um defeito no parsing ou nas definições, e não para uma propriedade do corpus.

### Laboratório 1 — sobreposição da linha de base

```python
"""Lab 1 (ch 04): replicate a baseline - Jaccard overlap of synthetic indicator sets from two feeds."""
feed_a = {"203.0.113.7", "203.0.113.9", "198.51.100.44", "bad.example", "c2.example"}
feed_b = {"203.0.113.9", "198.51.100.44", "c2.example", "drop.example"}
inter, union = feed_a & feed_b, feed_a | feed_b
print(f"|A|={len(feed_a)} |B|={len(feed_b)} |A&B|={len(inter)} |A|B|={len(union)}")
print(f"Jaccard={len(inter)/len(union):.3f}")
print("only in A:", sorted(feed_a - feed_b))
print("only in B:", sorted(feed_b - feed_a))
```

Execute com `python3 lab_overlap.py`. Saída verificada:

```text
|A|=5 |B|=4 |A&B|=3 |A|B|=6
Jaccard=0.500
only in A: ['203.0.113.7', 'bad.example']
only in B: ['drop.example']
```

### 4.2 Lendo a sobreposição

Três dos seis indicadores distintos são compartilhados, um Jaccard de 0,500. A sobreposição nada diz sobre qualidade: dois feeds podem concordar em indicadores obsoletos. A Pirâmide da Dor de Bianco lembra aos analistas que hashes e endereços IP são baratos de trocar para o adversário, de modo que uma sobreposição alta em indicadores da base da pirâmide é uma notícia modesta. Para Tomas, o laboratório de sobreposição é uma verificação do pipeline, não um resultado: o 0,500 coincide com o que ele calcula à mão a partir dos seis indicadores, então o código de parsing e de normalização se comporta como pretendido antes que o trabalho de calibração dependa dele.

### Laboratório 2 — piloto de calibração

```python
"""Lab 2 (ch 04): Brier score and calibration bins for synthetic analyst probability judgments."""
judgments = [  # (stated probability that the claim is true, outcome 1=true 0=false)
    (0.9, 1), (0.9, 1), (0.9, 0), (0.7, 1), (0.7, 0), (0.7, 1),
    (0.3, 0), (0.3, 1), (0.3, 0), (0.1, 0), (0.1, 0), (0.1, 0),
]
brier = sum((p - o) ** 2 for p, o in judgments) / len(judgments)
print(f"n={len(judgments)} Brier={brier:.3f}")
for p in sorted({p for p, _ in judgments}, reverse=True):
    outs = [o for q, o in judgments if q == p]
    print(f"stated {p:.1f}  observed {sum(outs)/len(outs):.2f}  (k={len(outs)})")
```

Execute com `python3 lab_calibration.py`. Saída verificada:

```text
n=12 Brier=0.183
stated 0.9  observed 0.67  (k=3)
stated 0.7  observed 0.67  (k=3)
stated 0.3  observed 0.33  (k=3)
stated 0.1  observed 0.00  (k=3)
```

### 4.3 Lendo o piloto

Doze julgamentos do piloto dão um escore de Brier de 0,183 (0 é perfeito; 0,25 é o que se obtém dizendo sempre 0,5 com desfechos equilibrados). A faixa de 0,9 se confirma apenas duas vezes em três, o que sugere excesso de confiança no topo; a faixa de 0,1 se comporta bem. Com três itens por faixa, nada disso é um achado — é um teste de que o código funciona e uma pista sobre onde o tamanho da amostra precisa ser maior. Tomas conferiu à mão os quatro primeiros termos do Brier contra o script, e eles coincidiram. Registrou no caderno de laboratório a pista da faixa de 0,9 como exploratória e pediu que a amostra principal desse peso maior aos julgamentos de alta confiança, transformando uma curiosidade de três itens em uma decisão de desenho registrada antes de os dados principais serem codificados.

### 4.4 Decisão de viabilidade

O piloto passa se o parsing funcionar, se os codificadores conseguirem resolver os desfechos de pelo menos a fração do piso e se o código de pontuação reproduzir os cálculos manuais. Falha se os desfechos forem em sua maioria irresolúveis ou se a codificação levar muito mais tempo do que o orçado. No piloto de Tomas, o terceiro teste passou, porque os quatro termos do Brier calculados à mão coincidiram com o script. O teste de tempo é o que os candidatos costumam pular: se codificar um julgamento leva três vezes o orçado, 300 julgamentos resolúveis viram outro projeto, e o lugar para descobrir isso é o piloto, não o nono mês.

### Exemplo resolvido

Tomas calcula à mão o escore de Brier dos quatro primeiros itens do piloto e confere com o script. Registra no caderno de laboratório a pista da faixa de 0,9 como exploratória, não como resultado, e pede que a amostra principal dê peso maior aos julgamentos de alta confiança, para que essa faixa seja estimada com precisão adequada.

> **Caso sintético.** Os dois feeds e os doze julgamentos do piloto são inventados.

### Erros e limites

Nunca publique números de piloto como achados. Os valores de indicadores aqui usam endereços de documentação e nomes `.example` e não são ameaças reais.

### Exercícios

- **EX022 — Leitura do Jaccard.** Cite o valor de Jaccard e liste os indicadores que estão apenas no feed A. *Rubrica:* 3 = 0,500; 203.0.113.7 e bad.example; 2 = apenas o valor; 1 = errado; 0 = nenhum.
- **EX023 — Sentido da sobreposição.** Por que uma sobreposição alta entre dois feeds baseados em hashes não prova que algum deles tenha valor? *Rubrica:* 3 = ambos podem ser obsoletos/da base da pirâmide; sobreposição ≠ qualidade ou relevância; 2 = parcial; 1 = prova valor; 0 = nenhum.
- **EX024 — Citação do Brier.** Que escore de Brier o piloto relata, e qual é o valor de referência de dizer sempre 0,5? *Rubrica:* 3 = 0,183 e 0,25; 2 = um; 1 = errado; 0 = nenhum.
- **EX025 — Faixa do topo.** O que a faixa de 0,9 sugere, e por que não é um achado? *Rubrica:* 3 = possível excesso de confiança (0,67 observado); k=3 pequeno demais, apenas piloto; 2 = uma metade; 1 = excesso de confiança comprovado; 0 = nenhum.
- **EX026 — Conferência manual.** Calcule (p−o)² para o primeiro item do piloto (0,9; 1). *Rubrica:* 3 = 0,01; 2 = método certo, deslize aritmético; 1 = método errado; 0 = nenhum.
- **EX027 — Mudança na amostragem.** Que mudança na amostragem o piloto motiva? *Rubrica:* 3 = sobreamostrar os julgamentos de alta confiança para ganhar precisão; 2 = amostra maior em geral; 1 = vago; 0 = nenhum.
- **EX028 — O piloto falha.** Cite duas observações que fariam Tomas parar depois do piloto. *Rubrica:* 3 = duas entre: desfechos em sua maioria irresolúveis / tempo de codificação muito acima do orçado / script divergente do cálculo manual; 2 = uma; 1 = Brier baixo; 0 = nenhuma.

### Síntese

Replique o que é simples, confira o código contra o cálculo manual, trate os números do piloto como pistas e decida a viabilidade por regras fixadas de antemão.

### Continue estudando — capítulo 04 de 08

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Estudo principal e validação independente

### Objetivos de aprendizagem

Você vai (1) organizar a dupla codificação cega de um corpus; (2) calcular a concordância entre avaliadores com o kappa de Cohen; (3) arbitrar divergências sem contaminar os dados; (4) providenciar a validação por uma equipe que não construiu o pipeline.

### 5.1 Dupla codificação

Dois codificadores treinados rotulam, de forma independente, cada evento amostrado com a característica central do Diamond a que se refere um julgamento-chave — adversário, capacidade, infraestrutura ou vítima — e com os códigos de desfecho. Nenhum codificador vê o trabalho do outro até que ambos terminem. No laboratório, dez eventos são codificados; na amostra completa de 340 julgamentos, o mesmo procedimento chegou a um kappa de 0,74 depois de uma revisão do livro de códigos. A independência importa porque codificadores que discutem os primeiros itens convergem para os hábitos um do outro, o que infla a concordância sem melhorar o livro de códigos.

### Laboratório 3 — concordância

```python
"""Lab 3 (ch 05): Cohen's kappa for two coders labelling synthetic events with a Diamond core feature."""
from collections import Counter
a = ["infra", "cap", "infra", "victim", "adv", "infra", "cap", "victim", "infra", "cap"]
b = ["infra", "cap", "cap",   "victim", "adv", "infra", "cap", "infra",  "infra", "cap"]
n = len(a)
po = sum(x == y for x, y in zip(a, b)) / n
ca, cb = Counter(a), Counter(b)
pe = sum(ca[k] * cb[k] for k in set(a) | set(b)) / n ** 2
kappa = (po - pe) / (1 - pe)
print(f"observed agreement={po:.2f} expected={pe:.2f} kappa={kappa:.3f}")
print("disagreements:", [i for i, (x, y) in enumerate(zip(a, b)) if x != y])
```

Execute com `python3 lab_kappa.py`. Saída verificada:

```text
observed agreement=0.80 expected=0.31 kappa=0.710
disagreements: [2, 7]
```

### 5.2 Lendo o kappa

Uma concordância bruta de 0,80 parece forte, mas o acaso sozinho produziria 0,31, dada a frequência com que cada rótulo aparece. O kappa remove esse componente de acaso e dá 0,710, convencionalmente descrito como substancial. As divergências nos itens 2 e 7 envolvem ambas a infraestrutura contra outra característica — uma pista de que a definição de infraestrutura no livro de códigos precisa de um exemplo sobre hospedagem compartilhada. A revisão de Tomas acrescentou esse exemplo, e a concordância na amostra completa de 340 julgamentos chegou a um kappa de 0,74. O valor da concordância ao acaso importa para a tese: se um rótulo dominasse, a concordância bruta poderia ser alta enquanto o kappa continuava baixo, e relatar apenas o valor bruto teria exagerado o quanto o livro de códigos funciona.

### 5.3 Arbitragem

Uma terceira pessoa resolve as divergências usando o livro de códigos, e os dois códigos originais são preservados. Mudar o livro de códigos no meio do estudo exige uma nota de versão e, quando possível, a recodificação dos itens anteriores com a nova definição. A única revisão do livro de códigos feita por Tomas, o exemplo de hospedagem compartilhada para a infraestrutura, é o caso que essa regra cobre. Ela traz uma nota de versão no arquivo, e os itens codificados sob a primeira versão foram recodificados, para que o kappa da amostra completa seja calculado sob uma única definição. As decisões do árbitro são registradas com a regra do livro de códigos em que se apoiaram, para que um leitor posterior possa ver se um dos codificadores foi vencido sistematicamente.

### 5.4 Validação independente

Uma equipe separada refaz a análise a partir dos dados e do código arquivados, sem ajuda. A concordância nos números principais é a validação. A divergência não é fracasso; é informação que precisa ser relatada. No estudo de Tomas, o laboratório parceiro reproduziu o escore de Brier com três casas decimais, mas encontrou um arquivo mesclado de forma errada. Ele o corrigiu e documentou a correção na tese, e não em uma nota privada. Esse erro nunca teria aparecido nas reexecuções dele, porque o pipeline mesclava os arquivos do mesmo jeito errado todas as vezes.

### 5.5 Compartilhando resultados em formato padrão

Quando os achados incluem indicadores ou relações estruturados, os objetos STIX 2.1 permitem que outros os interpretem; porém, resultados de pesquisa agregados costumam ser mais bem compartilhados como tabelas e código do que como indicadores. Os resultados de Tomas são uma tabela de calibração, um mapeamento de expressões para probabilidades e código; nenhum deles é um indicador. Embrulhar a tabela de calibração em objetos STIX acrescentaria trabalho de parsing para os leitores sem acrescentar significado; por isso, o arquivo dele publica CSV com um esquema e reserva o STIX para um eventual trabalho futuro que produza objetos de ameaça.

### Exemplo resolvido

Na amostra completa de 340 julgamentos (sintética), os codificadores chegam a um kappa de 0,74 depois de uma revisão do livro de códigos. A equipe de validação de um laboratório parceiro reproduz o escore de Brier com três casas decimais, mas encontra um arquivo mesclado de forma errada; Tomas o corrige e documenta a correção.

> **Caso sintético.** O tamanho da amostra, o kappa e o laboratório parceiro são inventados.

### Erros e limites

O kappa depende da prevalência dos rótulos; relate também a concordância bruta. Uma validação feita por amigos que ajudaram a construir o pipeline não é independente.

### Exercícios

- **EX029 — Citação do kappa.** Cite a concordância observada, a concordância esperada e o kappa do laboratório. *Rubrica:* 3 = 0,80, 0,31, 0,710; 2 = dois; 1 = um; 0 = nenhum.
- **EX030 — Por que o kappa.** Por que relatar o kappa além dos 80% de concordância bruta? *Rubrica:* 3 = corrige a concordância ao acaso dada a frequência dos rótulos; 2 = "mais rigoroso"; 1 = nenhum motivo; 0 = nenhum.
- **EX031 — Sinal do livro de códigos.** O que as duas divergências sugerem sobre o livro de códigos? *Rubrica:* 3 = definição de infraestrutura ambígua; acrescentar exemplo/esclarecer; 2 = livro de códigos pouco claro; 1 = codificadores descuidados; 0 = nenhum.
- **EX032 — Registro da arbitragem.** O que precisa ser preservado quando uma terceira pessoa arbitra? *Rubrica:* 3 = os dois códigos originais + o código arbitrado + a justificativa/versão do livro de códigos; 2 = código final + um original; 1 = apenas o final; 0 = nenhum.
- **EX033 — Teste de independência.** Um validador que coescreveu o script de parsing é independente? Explique. *Rubrica:* 3 = não; compartilha pressupostos/erros; é preciso uma equipe separada; 2 = não; 1 = sim; 0 = nenhum.
- **EX034 — Achado da validação.** O laboratório parceiro encontra um arquivo mesclado de forma errada. O que a tese precisa dizer? *Rubrica:* 3 = relatar o erro, a correção e o efeito nos resultados; 2 = mencionar a correção; 1 = escondê-lo; 0 = nenhum.
- **EX035 — Adequação do STIX.** Quando o STIX 2.1 seria uma escolha ruim para compartilhar os resultados deste estudo? *Rubrica:* 3 = estatísticas agregadas/livros de códigos não são indicadores; tabelas/código servem melhor; 2 = parcial; 1 = usar sempre STIX; 0 = nenhum.

### Síntese

Codifique às cegas e em dobro, corrija o acaso, arbitre com transparência, valide de forma independente e relate cada correção.

### Continue estudando — capítulo 05 de 08

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Crítica por pares e revisão

### Objetivos de aprendizagem

Você vai (1) solicitar uma crítica adversarial do próprio estudo; (2) aplicar os padrões de *tradecraft* da ICD 203 como lente de revisão; (3) responder aos revisores ponto a ponto; (4) distinguir as revisões que mudam conclusões das que melhoram a apresentação.

### 6.1 Convidando o leitor mais duro

Uma banca de tese é amigável por definição. Os doutorandos também devem buscar um leitor de *red cell*: alguém encarregado de encontrar o pressuposto mais fraco. Na pesquisa sobre método de CTI, os pontos fracos clássicos são fontes de desfecho circulares, viés de seleção do corpus em direção a incidentes dramáticos e escalas de confiança mapeadas depois de ver os dados. O leitor de *red cell* de Tomas atacou um ponto que a banca não havia levantado: as afirmações confirmadas têm mais chance de receber acompanhamento público, o que infla a calibração aparente das afirmações prováveis. A resposta, uma análise de sensibilidade sob dois pressupostos sobre as afirmações sem resolução, mudou o resumo.

### 6.2 A ICD 203 como lente

A ICD 203 pede que os produtos analíticos descrevam a qualidade das fontes, expressem a incerteza, separem informação de pressupostos e julgamentos, incorporem alternativas, mostrem relevância, argumentem com clareza, expliquem mudanças de julgamento, busquem exatidão e usem recursos visuais eficazes. Um artigo de pesquisa sobre CTI deveria atingir o mesmo padrão que mede. Tomas confronta seu rascunho com essa lista e descobre que nunca declarou como a própria conclusão mudaria se as fontes de desfecho fossem apenas metade tão independentes quanto o pressuposto.

A correção aplica à própria conclusão o padrão da ICD 203 sobre a incerteza: a tese agora declara como a estimativa de calibração se move se as afirmações sem resolução forem tratadas primeiro como não confirmadas e depois como confirmadas, usando a análise de sensibilidade com dois pressupostos.

### 6.3 Respostas ponto a ponto

Cada comentário de revisor recebe uma resposta numerada: aceito com alteração (cite a página), aceito parcialmente (explique) ou recusado (explique com evidência). O silêncio sobre um comentário soa como evasão. A resposta de Tomas ao comentário do leitor de *red cell* sobre o viés de acompanhamento seria "aceito com alteração": ela nomeia a análise de sensibilidade, os dois pressupostos sobre as afirmações sem resolução e a página em que aparecem os dois intervalos. Um leitor pode conferir a resposta contra a tese sem reler o capítulo inteiro. Quando um parceiro da comunidade lhe pediu que retirasse um resultado negativo, a resposta de Tomas foi "recusado", citando o plano de análise pré-registrado que exigia relatá-lo; a mudança de redação que o mesmo parceiro também pediu foi "aceito com alteração".

### 6.4 Substantivo versus cosmético

Uma análise de sensibilidade que move o Brier principal de 0,17 para 0,21 é substantiva e precisa chegar ao resumo. Corrigir as fontes das figuras é cosmético. Candidatos que enterram mudanças substantivas em um apêndice perdem a confiança dos leitores. A análise de sensibilidade de Tomas é esse tipo de mudança. Tratar as afirmações sem resolução sob dois pressupostos produziu dois intervalos, e ambos foram para o resumo, porque um leitor que visse apenas o mais favorável avaliaria mal o quanto a conclusão depende do comportamento de acompanhamento. A correção das fontes das figuras vai para o registro de alterações e para nenhum outro lugar, enquanto a mudança do Brier aparece na carta de resposta como a primeira mudança substantiva.

### 6.5 Hipóteses alternativas

A análise de hipóteses concorrentes, discutida por Heuer, pergunta que evidência é inconsistente com cada explicação, em vez de qual é consistente com a favorita. Uma rodada de crítica é um bom momento para listar alternativas: por exemplo, que o excesso de confiança aparente reflita um relato seletivo de acompanhamento, e não uma má calibração dos analistas. Tomas lista essa alternativa explicitamente. A evidência inconsistente com ela seriam taxas de acompanhamento semelhantes para afirmações confirmadas e não confirmadas; a análise de sensibilidade é a maneira dele de mostrar quanto a conclusão muda se a alternativa for verdadeira.

### Exemplo resolvido

O leitor de *red cell* argumenta que as afirmações confirmadas têm mais chance de receber acompanhamento público, inflando a calibração aparente das afirmações prováveis. Tomas acrescenta uma análise de sensibilidade que trata as afirmações sem resolução sob dois pressupostos e relata ambos os intervalos no resumo.

> **Caso sintético.** A crítica do *red cell* e os intervalos de sensibilidade são inventados.

### Erros e limites

A crítica não é pessoal; nem todo comentário está correto. Defenda-se com evidência, não com senioridade.

### Exercícios

- **EX036 — Alvo do red cell.** Cite dois pressupostos que um leitor de red cell deveria atacar primeiro no desenho de Tomas. *Rubrica:* 3 = dois entre independência dos desfechos / seleção do corpus / mapeamento da escala a posteriori / viés de acompanhamento; 2 = um; 1 = erros de digitação; 0 = nenhum.
- **EX037 — Padrão ausente.** Que elemento da ICD 203 o rascunho de Tomas não cumpria antes da revisão? *Rubrica:* 3 = expressar a incerteza/sensibilidade da própria conclusão aos pressupostos; 2 = incerteza vaga; 1 = recursos visuais; 0 = nenhum.
- **EX038 — Tipos de resposta.** Liste as três categorias aceitáveis de resposta a um comentário de revisor. *Rubrica:* 3 = aceito com alteração, aceito parcialmente, recusado com motivos; 2 = duas; 1 = ignorar; 0 = nenhuma.
- **EX039 — Teste do substantivo.** Uma reanálise move o Brier de 0,17 para 0,21. Onde isso precisa aparecer? *Rubrica:* 3 = resumo/resultados principais + explicação; 2 = apenas nos resultados; 1 = apenas no apêndice; 0 = nenhum.
- **EX040 — História concorrente.** Enuncie uma explicação alternativa para o excesso de confiança aparente na faixa do topo. *Rubrica:* 3 = alternativa plausível (acompanhamento seletivo, viés das fontes de desfecho, k pequeno); 2 = vaga; 1 = tentativa mínima; 0 = nenhuma.
- **EX041 — Movimento da ACH.** Na análise de hipóteses concorrentes de Heuer, que evidência importa mais? *Rubrica:* 3 = a evidência inconsistente com as hipóteses (que refuta); 2 = evidência diagnóstica, de forma vaga; 1 = evidência consistente; 0 = nenhuma.
- **EX042 — Recuse bem.** Escreva uma recusa de uma frase a um revisor que pede os nomes reais das vítimas. *Rubrica:* 3 = recusa citando ética/TLP/proteção de dados; oferece alternativa agregada; 2 = apenas recusa; 1 = atende ao pedido; 0 = nenhuma.

### Síntese

Convide a leitura hostil, cobre de si mesmo o padrão da ICD 203, responda a todo comentário, leve as mudanças substantivas para a frente e teste as alternativas pela refutação.

### Continue estudando — capítulo 06 de 08

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Síntese da tese e arquivo de reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) estruturar uma tese de modo que cada capítulo carregue uma afirmação; (2) montar um arquivo de reprodutibilidade que exclua legalmente os dados restritos; (3) documentar o ambiente de software e as sementes aleatórias; (4) escrever uma declaração de disponibilidade de dados honesta sobre as restrições.

### 7.1 Uma afirmação por capítulo

Os leitores devem conseguir enunciar em uma frase a afirmação de cada capítulo: desenho de integridade; lacuna; proposta; replicação da linha de base; resultado principal de calibração; robustez sob crítica. Se um capítulo tem três afirmações sem relação entre si, divida-o; se não tem nenhuma, corte-o. Tomas aplicou o teste a cada um dos seus seis capítulos: um capítulo cuja afirmação não podia ser enunciada em uma frase foi dividido ou cortado, e o teste flagrou um capítulo de rascunho que misturava a lacuna com a proposta. No capítulo de calibração, a frase precisa nomear a medida e o escopo do corpus, como pede o EX043.

### 7.2 O que o arquivo contém

Código, versões do livro de códigos, dados sintéticos de teste, tabelas agregadas de resultados, o pré-registro e um script que reconstrói cada figura. As entradas restritas — relatórios TLP:AMBER+STRICT, texto licenciado de fornecedores — são substituídas por um manifesto de identificadores e hashes SHA-256, para que alguém com acesso legítimo possa verificar se tem os mesmos arquivos. O arquivo de Tomas contém 14 scripts, 3 versões do livro de códigos, um manifesto com os hashes de 1.200 relatórios e amostras sintéticas que exercitam todos os caminhos do código. Um colega sem acesso ao laboratório reconstruiu cada figura em menos de uma hora, e esse é o teste que importa.

### 7.3 Ambiente

Registre a versão do Python e confirme que a análise usa apenas a biblioteca padrão, ou fixe cada dependência. Registre toda semente aleatória usada na amostragem. "Rodou no meu notebook" não é reprodutibilidade. Os laboratórios de Tomas usam apenas a biblioteca padrão, o que elimina a maior parte da deriva de dependências; ainda assim, o arquivo registra a versão do Python usada. A seleção da amostra principal usa uma semente registrada, de modo que os 340 julgamentos podem ser sorteados de novo a partir do manifesto por qualquer pessoa com acesso legítimo aos relatórios. O arquivo também registra o sistema operacional em que as figuras foram geradas, porque a reconstrução de uma hora feita pelo colega aconteceu em outra máquina.

### 7.4 Declaração de disponibilidade de dados

Declare o que é aberto, o que é restrito e por quê, e como um pesquisador autorizado pode pedir acesso. Não escreva "disponível mediante solicitação" se, na prática, os pedidos serão recusados. Para Tomas, a parte restrita são os 200 relatórios TLP:AMBER+STRICT e o texto licenciado de fornecedores. Sua declaração nomeia a comunidade de compartilhamento e o titular da licença como caminhos de acesso, e o manifesto de hashes permite que um pesquisador autorizado confirme que tem os mesmos arquivos. Ela também diz o que um pesquisador autorizado não pode obter: os relatórios em si nunca saem do laboratório, de modo que ter acesso significa trabalhar no local, sob as mesmas regras TLP:AMBER+STRICT que vinculavam Tomas.

### 7.5 Saídas legíveis por máquina

Quando a tese produz estruturas reutilizáveis — por exemplo, um mapeamento de expressões estimativas para intervalos de probabilidade —, publique-as como JSON ou CSV simples, com um esquema. Se o trabalho criar objetos de ameaça, o STIX 2.1 e o TAXII 2.1 oferecem formatos padrão de troca, mas uma tese de método raramente precisa deles. O mapeamento de expressões para probabilidades de Tomas é o candidato óbvio: um CSV com uma linha por expressão estimativa, seu intervalo numérico e a versão do livro de códigos, para que outros possam aplicar o mesmo mapeamento aos próprios relatórios.

### Exemplo resolvido

Um colega sem acesso ao laboratório recebe apenas o arquivo, executa o script de reconstrução sobre as amostras sintéticas e as tabelas agregadas e compara cada figura com o rascunho da tese; todas as figuras coincidem, e a reconstrução inteira leva menos de uma hora.

> **Caso sintético.** O conteúdo do arquivo e o teste de reconstrução são inventados.

### Erros e limites

Manifestos de hashes provam a identidade dos arquivos, não a legitimidade do acesso. A hospedagem do arquivo precisa respeitar as mesmas restrições que os dados.

### Exercícios

- **EX043 — Afirmação do capítulo.** Escreva a afirmação de uma frase do capítulo da tese que relata a calibração. *Rubrica:* 3 = afirmação específica com medida e escopo do corpus; 2 = vaga; 1 = apenas o tema; 0 = nenhuma.
- **EX044 — Substituição do restrito.** Como o arquivo representa os relatórios restritos AMBER+STRICT? *Rubrica:* 3 = manifesto com identificador + SHA-256, sem conteúdo; 2 = lista de títulos; 1 = incluir os arquivos; 0 = nenhum.
- **EX045 — Linha do ambiente.** Indique os dois fatos de ambiente que toda reconstrução precisa ter registrados aqui. *Rubrica:* 3 = versão do Python + sementes (ou dependências fixadas); 2 = um; 1 = tema do sistema operacional; 0 = nenhum.
- **EX046 — Disponibilidade honesta.** Reescreva com honestidade "dados disponíveis mediante solicitação" para relatórios licenciados de fornecedores. *Rubrica:* 3 = declara a restrição de licença, quem pode pedir e por qual caminho; 2 = parcial; 1 = inalterada; 0 = nenhuma.
- **EX047 — Teste de reconstrução.** O que a reconstrução de uma hora feita pelo colega demonstra, e o que não demonstra? *Rubrica:* 3 = código/figuras reprodutíveis a partir do arquivo; não que as entradas restritas ou a codificação estivessem corretas; 2 = uma metade; 1 = prova tudo; 0 = nenhum.
- **EX048 — Escolha do formato.** Que formato serve ao mapeamento de expressões para probabilidades, e por que não o STIX? *Rubrica:* 3 = JSON/CSV com esquema; não é um objeto de ameaça; 2 = apenas o formato; 1 = STIX obrigatório; 0 = nenhum.
- **EX049 — Regra de hospedagem.** O arquivo pode ser colocado em um repositório público com os arquivos restritos criptografados dentro dele? *Rubrica:* 3 = não; o conteúdo restrito não pode ser distribuído, nem criptografado, salvo se os termos permitirem; usar o manifesto; 2 = desaconselhado; 1 = sim; 0 = nenhum.

### Síntese

Uma afirmação por capítulo, um arquivo que reconstrói tudo o que é legítimo, disponibilidade honesta e dados restritos representados apenas por hashes.

### Continue estudando — capítulo 07 de 08

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Plano de defesa e publicação

### Objetivos de aprendizagem

Você vai (1) preparar uma defesa que ponha os limites em primeiro plano; (2) escolher com responsabilidade os veículos de publicação e o momento do *pre-print*; (3) conduzir a divulgação quando os achados puderem constranger fornecedores identificados; (4) planejar um trabalho futuro que estenda a tese em vez de repeti-la.

### 8.1 Postura na defesa

Os examinadores testam se você sabe onde o seu resultado para. Abra com a afirmação, a evidência e as três ameaças mais fortes à validade. Um candidato que levanta o problema do viés de acompanhamento antes do examinador controla a conversa. As três ameaças de Tomas seriam o viés de acompanhamento, as fontes de desfecho que dependem do relatório original e um corpus que pode sobrerrepresentar incidentes dramáticos. A análise de sensibilidade responde à primeira, a verificação de circularidade à segunda, e o escopo declarado do corpus limita a terceira.

### 8.2 Veículos

Eventos de segurança com revisão por pares, periódicos de estudos de inteligência e conferências de profissionais alcançam públicos diferentes. Um resultado de método sobre calibração pode precisar dos dois: um periódico para o método e uma palestra para líderes de SOC. Os *pre-prints* aceleram a disseminação, mas devem trazer a mesma seção de limites que o artigo final. Para Tomas, o método de calibração e o livro de códigos cabem em um periódico; a mensagem prática — quanto peso dar a "altamente provável" em um relatório de fornecedor na hora de decidir um bloqueio — cabe em uma conferência de profissionais para líderes de SOC. O *pre-print* traz os mesmos intervalos de sensibilidade que o resumo.

### 8.3 Sensibilidade dos fornecedores

Mesmo com apresentação sintética ou anonimizada, um leitor pode adivinhar a que fornecedor um padrão se refere. Ofereça às partes afetadas uma prévia curta quando os acordos o exigirem, mas não deixe que a prévia vire veto sobre achados honestos. Nunca revele conteúdo restrito por TLP para obter boa vontade. A conduta de Tomas é o modelo: resultados relatados por classe anonimizada de fornecedor, prévias dadas aos dois parceiros da comunidade cujos acordos as exigiam, uma mudança de redação aceita e um pedido de retirar um resultado negativo recusado. A pergunta do examinador na defesa foi respondida com a descrição desse registro.

### 8.4 O TLP nas saídas

Artigos públicos são, na prática, TLP:CLEAR. Tudo o que derivar de entradas restritas precisa estar agregado o bastante para que a fonte não possa ser reconstruída. Em caso de dúvida, consulte a comunidade de compartilhamento. Os resultados de Tomas derivados dos 200 relatórios TLP:AMBER+STRICT aparecem apenas como agregados dentro de classes de fornecedor, e nenhum relatório é citado. Quando uma classe é tão pequena que um único relatório poderia ser identificado a partir da sua linha, a classe é fundida com outra antes da publicação. A regra de fusão está escrita no arquivo, para que um membro da comunidade de compartilhamento possa verificar que nenhum relatório restrito é recuperável a partir de uma linha publicada.

### 8.5 Trabalho futuro

Extensões naturais: um estudo prospectivo em que os analistas registram probabilidades numéricas no momento da escrita; uma comparação entre idiomas; uma intervenção que treine a calibração e meça a mudança. Cada uma precisa do próprio dossiê de ética. O estudo prospectivo responde à maior limitação de Tomas: se os analistas registrarem uma probabilidade numérica ao escrever um julgamento, não é preciso mapear expressões depois, e o pressuposto de mapeamento que os examinadores questionaram desaparece. Uma intervenção de treino de calibração estudaria os analistas como participantes; por isso, precisaria do consentimento informado deles, que o desenho atual, apenas sobre o corpus, nunca exigiu.

### Exemplo resolvido

Na defesa, um examinador pergunta se os fornecedores foram identificados. Tomas explica que os resultados são relatados por classe anonimizada de fornecedor, que dois parceiros da comunidade tiveram uma prévia do artigo, como seus acordos exigiam, e que uma mudança de redação pedida foi aceita, enquanto um pedido de retirar um resultado negativo foi recusado.

> **Caso sintético.** A troca na defesa e a prévia aos fornecedores são inventadas.

### Erros e limites

Publicar um "ranking" da calibração dos fornecedores a partir de dados licenciados pode violar licenças e é metodologicamente frágil com amostras pequenas.

### Exercícios

- **EX050 — Movimento de abertura.** Que três coisas o primeiro slide da defesa deve trazer? *Rubrica:* 3 = afirmação, evidência, ameaças mais fortes à validade; 2 = duas; 1 = biografia; 0 = nenhuma.
- **EX051 — Dois veículos.** Por que o resultado de calibração poderia ir tanto para um periódico quanto para uma conferência de profissionais? *Rubrica:* 3 = rigor do método/revisão por pares + alcançar quem decide no SOC; 2 = um motivo; 1 = mais citações; 0 = nenhum.
- **EX052 — Veto na prévia.** Um fornecedor pede, durante a prévia, que se retire um achado negativo. Qual é a resposta? *Rubrica:* 3 = recusar a retirada; considerar apenas correções factuais; documentar; 2 = recusar; 1 = retirar; 0 = nenhuma.
- **EX053 — TLP de um artigo.** Que nível de TLP um artigo público tem na prática, e o que decorre disso para as entradas restritas? *Rubrica:* 3 = CLEAR; entradas restritas apenas em agregados não reconstruíveis; 2 = apenas CLEAR; 1 = AMBER; 0 = nenhum.
- **EX054 — Risco do ranking.** Dê dois motivos para não publicar um ranking de calibração com fornecedores identificados. *Rubrica:* 3 = violação de licença/acordo + instabilidade por amostra pequena (ou equidade); 2 = um; 1 = vago; 0 = nenhum.
- **EX055 — Desenho prospectivo.** Descreva em uma frase o estudo prospectivo de continuação. *Rubrica:* 3 = analistas registram probabilidade numérica ao escrever; desfechos acompanhados para a frente; 2 = estudo prospectivo vago; 1 = repetir a tese; 0 = nenhum.
- **EX056 — Regra do pre-print.** O que um pre-print precisa incluir que um resumo de conferência poderia omitir? *Rubrica:* 3 = a seção completa de limites/validade; 2 = métodos; 1 = vago; 0 = nenhum.

### Síntese

Comece pelos limites, escolha os veículos pelo público, deixe a prévia corrigir fatos, mas não achados, respeite o TLP em cada saída e estenda em vez de repetir.

### Continue estudando — capítulo 08 de 08

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções ↓](#worked-results) · [Próximo curso pelo índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX056. O Larkspur CTI Lab, Tomas Ekberg, a Dra. Hana Sato, o corpus e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Base legal, os termos de uso ou de compartilhamento aplicáveis, a etapa de minimização e o prazo de retenção.

**EX002.** Apenas dentro do Larkspur CTI Lab, por pessoas cobertas pelo acordo de compartilhamento; sem citações, sem redistribuição, com resultados relatados apenas como agregados que não permitam identificar um relatório.

**EX003.** Os termos do fórum proíbem a raspagem para pesquisa e nenhuma permissão foi obtida; as postagens também contêm dados pessoais que a visibilidade pública não torna livres para tratamento.

**EX004.** Um escalonamento previamente acordado: avisar a orientadora, que contata um coordenador adequado, como um CERT nacional, por meio da comunidade de compartilhamento; Tomas não sonda a organização por conta própria.

**EX005.** Viés de confirmação. Fixar as hipóteses e o esquema de codificação antes de ver os dados de desfecho impede que a evidência posterior seja dobrada para caber em uma atribuição atraente.

**EX006.** Relatá-lo em uma seção exploratória claramente rotulada, separada dos resultados confirmatórios, e propor um estudo de acompanhamento para testá-lo.

**EX007.** Apenas membros nomeados do Larkspur com necessidade de conhecer documentada e vinculados ao acordo de compartilhamento.

**EX008.** Kill chain: um modelo de estratégia defensiva baseado em fases. Diamond Model: uma ontologia do evento de intrusão. ATT&CK: uma base de conhecimento empírica e curada do comportamento observado de adversários.

**EX009.** Exemplo: "Nenhum estudo publicado mede se os indicadores recebidos por meio de uma comunidade setorial de compartilhamento reduzem o tempo até a detecção nos SOCs dos membros em comparação com os de não membros."

**EX010.** Adversário, capacidade, infraestrutura, vítima. Exemplo de pivô: de um domínio de comando e controle compartilhado (infraestrutura) para outras vítimas que contatam esse domínio.

**EX011.** Fatos individualmente inofensivos, combinados, podem identificar, localizar ou traçar o perfil de uma pessoa, possibilitando danos e acionando deveres de proteção de dados, embora cada fato fosse público.

**EX012.** Citá-lo como literatura cinzenta que descreve a prática, claramente separada da evidência revisada por pares, e evitar apoiar uma afirmação central apenas nele.

**EX013.** Oferece orientação para estabelecer relações de compartilhamento, definir o escopo e tratar a informação compartilhada; não mede empiricamente quanto o compartilhamento melhora os resultados de segurança.

**EX014.** Defensores que analisam campanhas inteiras podem interromper uma intrusão ao quebrar qualquer fase isolada da kill chain, transformando a inteligência sobre os adversários em vantagem defensiva.

**EX015.** Exemplo: "Entre as atribuições a um grupo nomeado no corpus, menos de 70% são apoiadas por uma fonte autorizada independente em até 24 meses."

**EX016.** Um julgamento está "confirmado" se uma fonte autorizada independente do corpus (alerta conjunto, documento judicial, correção do fornecedor) o apoia em até 24 meses, codificado como apoia/contradiz/sem resolução.

**EX017.** Se a fonte "confirmadora" apenas repete o relatório original, a concordância é circular e a calibração parece melhor do que é; só as fontes independentes contam.

**EX018.** Impede que as expectativas dos codificadores — "disseram altamente provável, então provavelmente aconteceu" — vazem para o código de desfecho.

**EX019.** Seguir a regra pré-registrada: não analisar como se o piso tivesse sido atingido; ampliar a amostra ou revisar o desenho com aprovação da banca, e relatar o déficit.

**EX020.** Validade externa — se os achados se generalizam para além da população de relatórios amostrada.

**EX021.** O estudo mede a calibração de um constructo em um corpus definido; afirmar a falta de confiabilidade geral da CTI excede o que os dados podem mostrar.

**EX022.** Jaccard=0.500 (0,500); apenas em A: 203.0.113.7 e bad.example.

**EX023.** Os dois feeds podem trazer os mesmos indicadores obsoletos ou fáceis de trocar, da base da pirâmide; a concordância mostra fontes em comum, não qualidade nem relevância para um defensor.

**EX024.** Brier=0.183 (0,183); prever sempre 0,5 com desfechos equilibrados dá 0,25.

**EX025.** O observado 0,67 para o declarado 0,9 sugere excesso de confiança no topo, mas, com apenas três itens, é um sinal de piloto, não um resultado.

**EX026.** (0,9 − 1)² = 0,01.

**EX027.** Sobreamostrar os julgamentos de alta confiança ("altamente provável" e acima), para que as faixas do topo tenham itens suficientes para estimativas de calibração precisas.

**EX028.** Quaisquer duas entre: a maioria dos desfechos irresolúvel; tempo de codificação muito acima do orçado; o script divergindo do cálculo manual.

**EX029.** Concordância observada 0,80, esperada 0,31, kappa 0,710.

**EX030.** Parte da concordância acontece por acaso, dada a frequência de cada rótulo; o kappa remove essa concordância esperada, para que o valor reflita a consistência real dos codificadores.

**EX031.** As duas divergências envolvem a infraestrutura, então sua definição é ambígua; acrescentar ao livro de códigos uma regra de esclarecimento e um exemplo (por exemplo, hospedagem compartilhada).

**EX032.** Os códigos originais dos dois codificadores, o código arbitrado, a justificativa e a versão do livro de códigos usada.

**EX033.** Não. Por ter escrito o parser, ele compartilha os pressupostos do código e pode deixar passar os mesmos erros; a validação precisa de uma equipe que não o construiu.

**EX034.** Descrever a mesclagem errada, como foi corrigida e se algum número relatado mudou, e em quanto.

**EX035.** Quando os resultados são estatísticas agregadas e regras de codificação, e não indicadores ou relações; tabelas, livros de códigos e código servem melhor aos leitores.

**EX036.** Quaisquer dois entre: independência das fontes de desfecho, seleção do corpus em direção a incidentes dramáticos, mapeamento da escala de confiança depois de ver os desfechos, acompanhamento público seletivo.

**EX037.** Expressar a incerteza: o rascunho não mostrava como a conclusão dependia do pressuposto de independência, de modo que não se dava a sensibilidade do julgamento principal.

**EX038.** Aceito com alteração (com a localização), aceito parcialmente (com explicação), recusado (com motivos baseados em evidência).

**EX039.** No resumo e nos resultados principais, com uma explicação de que pressuposto causou a mudança.

**EX040.** Exemplo: as afirmações que se revelaram verdadeiras recebem acompanhamento público com mais frequência, de modo que os itens sem resolução são desproporcionalmente falsos, distorcendo a faixa do topo.

**EX041.** A evidência inconsistente com uma hipótese — a evidência que refuta é a mais diagnóstica.

**EX042.** "Não podemos nomear as vítimas porque as fontes são restritas por TLP e contêm dados pessoais e organizacionais; em vez disso, fornecemos contagens agregadas por setor."

**EX043.** Exemplo: "Em 340 julgamentos-chave resolúveis do corpus definido, as expressões estimativas de alta confiança se confirmaram com menos frequência do que a probabilidade mapeada (Brier 0,21 sob o pressuposto conservador)."

**EX044.** Como um manifesto de identificadores de relatórios e hashes SHA-256, sem conteúdo, para que os detentores legítimos possam verificar a identidade.

**EX045.** A versão do Python (com apenas a biblioteca padrão, ou dependências fixadas) e as sementes aleatórias usadas na amostragem.

**EX046.** "Os relatórios de fornecedores são licenciados e não podem ser redistribuídos; pesquisadores que tenham a mesma licença podem solicitar o manifesto de identificadores ao responsável pelos dados do Larkspur."

**EX047.** Mostra que o código, as amostras sintéticas e as tabelas agregadas reconstroem todas as figuras; não mostra que as entradas restritas foram codificadas corretamente.

**EX048.** JSON ou CSV com um esquema documentado; o mapeamento é uma tabela metodológica, não um objeto de ameaça, então o STIX acrescenta complexidade sem benefício.

**EX049.** Não. Distribuir conteúdo restrito, mesmo criptografado, pode violar a licença ou o TLP; publique apenas o manifesto de hashes.

**EX050.** A afirmação central, a evidência que a sustenta e as ameaças mais fortes à sua validade.

**EX051.** O periódico testa o método sob revisão por pares; a conferência de profissionais alcança os líderes de SOC que tomam decisões de bloqueio com base na linguagem de confiança.

**EX052.** Recusar a retirada do achado; aceitar apenas correções factuais e registrar o pedido e a resposta.

**EX053.** Na prática, TLP:CLEAR; portanto, as entradas restritas só podem aparecer como agregados a partir dos quais nenhuma fonte possa ser reconstruída.

**EX054.** Pode violar acordos de licença ou de compartilhamento, e as amostras por fornecedor são pequenas demais para um ranking confiável.

**EX055.** Os analistas atribuem uma probabilidade numérica a cada julgamento-chave ao escrevê-lo, e os desfechos são acompanhados para a frente por 24 meses, para medir a calibração sem codificação retrospectiva.

**EX056.** A seção completa de limites e validade, para que os primeiros leitores vejam as mesmas ressalvas que os leitores finais.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bianco, D. (2013). The Pyramid of Pain. <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Caltagirone, S., Pendergast, A. and Betz, C. (2013). The Diamond Model of Intrusion Analysis. Technical Report ADA586960, Center for Cyber Intelligence Analysis and Threat Research. <https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf>
- European Union. Regulation (EU) 2016/679 (General Data Protection Regulation). <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- FIRST. Traffic Light Protocol (TLP) version 2.0. <https://www.first.org/tlp/>
- Heuer, R. J. (1999). Psychology of Intelligence Analysis. CIA Center for the Study of Intelligence. <https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/>
- Hutchins, E. M., Cloppert, M. J. and Amin, R. M. (2011). Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains. Lockheed Martin. <https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf>
- Kent, S. (1964). Words of Estimative Probability. CIA Studies in Intelligence. <https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf>
- MITRE ATT&CK Enterprise matrix, groups, software and technique pages. <https://attack.mitre.org/>
- NIST SP 800-150 (2016). Guide to Cyber Threat Information Sharing. <https://doi.org/10.6028/NIST.SP.800-150>
- NIST SP 800-61 Rev. 3 (2025). Incident Response Recommendations and Considerations for Cybersecurity Risk Management. <https://doi.org/10.6028/NIST.SP.800-61r3>
- OASIS. STIX Version 2.1 (Committee Specification / OASIS Standard). <https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html>
- OASIS. TAXII Version 2.1. <https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html>
- ODNI. Intelligence Community Directive 203: Analytic Standards (2015, amended 2022). <https://www.odni.gov/files/documents/ICD/ICD-203.pdf>
