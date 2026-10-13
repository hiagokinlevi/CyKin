# Inteligência de ameaças e OSINT: um livro de bacharelado

- Idioma: português do Brasil (`pt`); curso de bacharelado, quatro anos. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 40 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 9–40 (EX025–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de graduação que se preparam para trabalhar como analistas juniores de inteligência de ameaças cibernéticas (CTI) ou para seguir na pesquisa.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite ético: nenhuma coleta sobre pessoas privadas reais, nenhuma evasão de termos de uso, nenhuma desanonimização e nenhum contato com infraestrutura de adversários. Organizações, pessoas e indicadores são **sintéticos**, salvo quando uma frase cita uma fonte pública; os endereços usam as faixas da RFC 5737 e os domínios usam `.example`.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–18 constroem fundamentos de raciocínio, computação, escrita, privacidade, evidência e pesquisa por meio de exemplos de inteligência. Os capítulos 19–32 ensinam teoria de CTI e OSINT, casos, modelos, dados, métodos, controles, verificação, análise de falhas, operações e interfaces, com dois laboratórios. Os capítulos 33–40 tratam de métodos de pesquisa, um projeto comparativo, o projeto final, a prática comunitária, a revisão de evidências e a tese. Cada capítulo tem objetivos, texto didático, um exemplo resolvido, um caso sintético rotulado, erros e limites, três exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**.

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Halden County Health Trust (HCHT)** — três hospitais, um laboratório regional e um portal do paciente | Organização atendida pela CTI | Inventada |
| **Amara Diallo** | Estudante de graduação em estágio de meio período na equipe de segurança do HCHT | Inventada |
| **Health Sector Sharing Circle (HSSC)** | Comunidade regional que troca inteligência sob o TLP 2.0 | Inventada |

### Fontes principais

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) e [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); a [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf) de Hutchins et al.; NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) distinguir dedução, indução e abdução no trabalho de inteligência; (2) identificar falácias comuns em relatórios de ameaças; (3) usar proporções e razões corretamente; (4) explicitar as premissas por trás de uma conclusão.

### 1.1 Três tipos de inferência

A dedução vai de regras a conclusões certas: se todo relatório TLP:RED vai apenas para destinatários nomeados e Amara não está entre eles, ela não pode lê-lo. A indução generaliza a partir de casos: cinco relatórios do setor começaram com phishing, então o phishing é uma via de entrada comum. A abdução propõe a melhor explicação para uma observação: uma rajada de logins com falha durante a noite pode ser adivinhação de senhas. A análise de inteligência depende muito da abdução, e é por isso que suas conclusões precisam ser declaradas com incerteza. Amara rotula cada conclusão com a inferência que a produziu.

### 1.2 Falácias em relatórios

Raciocínio post hoc: uma indisponibilidade veio depois de um e-mail de phishing, então o e-mail a causou. Negligência da taxa-base: um detector com 99% de acerto parece decisivo até você lembrar como ataques reais são raros. Sobrevivência: estudar apenas os incidentes detectados diz pouco sobre os que não foram. Nomear a falácia no rascunho de um colega é uma habilidade útil de revisão. Na primeira revisão que Amara faz de um rascunho do HSSC, ela marca uma frase que atribui um surto de ransomware a um fornecedor porque a atualização do fornecedor chegou na véspera. O rascunho não oferece nenhuma outra ligação. Ela sugere reescrevê-la como hipótese e listar que evidências a confirmariam ou descartariam, o que transforma uma falácia em uma pergunta útil para o próximo analista.

### 1.3 Proporções e razões

"O phishing apareceu em 3 de 5 relatórios" é uma proporção, 60%. Relatar só "60%" esconde que a amostra é de cinco. Sempre dê o numerador e o denominador, especialmente quando o denominador é pequeno. Amara escreve "3 de 5 relatórios" em suas notas e acrescenta o período que eles cobrem. Quando um trimestre posterior traz vinte relatórios, a proporção pode ser comparada de forma justa, e os leitores veem que o primeiro número se apoiava em pouquíssimos casos. Uma porcentagem tirada de cinco itens pode oscilar vinte pontos com um relatório a mais, então apresentá-la sozinha sugere muito mais precisão do que a evidência tem.

### 1.4 Premissas

Toda conclusão se apoia em premissas. Escrevê-las — os relatórios são representativos; os carimbos de tempo estão corretos — permite que os leitores julguem quanto confiar no resultado. Amara mantém uma lista curta de premissas no fim de cada nota que escreve para a equipe de segurança do HCHT. Quando uma delas se revela errada, como um feed cujos carimbos de tempo usam outro fuso horário, ela vê na hora quais conclusões dependiam dela e revisa só essas. Premissas não declaradas são os erros mais difíceis de encontrar, porque ninguém sabe que precisa conferi-las.

### Estimar antes de calcular

Antes de rodar números, Amara escreve uma expectativa grosseira: cerca de metade dos relatórios do setor vai mencionar phishing. Se o valor calculado for muito diferente, ela confere os dados e o código antes de acreditar na surpresa. Estimativas grosseiras pegam cedo erros de planilha, linhas duplicadas e colunas mal lidas.

### Exemplo resolvido

Um blog de fornecedor afirma que "os ataques de ransomware a hospitais subiram 300%". Amara pergunta: 300% sobre qual linha de base, em que período, contados como? O blog conta incidentes relatados publicamente, que podem subir porque as regras de notificação mudaram. Ela registra a alegação como "os incidentes relatados aumentaram; taxa subjacente desconhecida".

> **Caso sintético.** A alegação do blog é inventada; o HCHT é fictício.

### Erros e limites

A lógica organiza o raciocínio, mas não substitui a evidência. Porcentagens de amostras minúsculas enganam mesmo quando a aritmética está certa.

### Exercícios

- **EX001 — Tipo de inferência.** Que tipo de inferência é "logins com falha durante a noite sugerem adivinhação de senhas"? *Rubrica:* 3 = abdução (melhor explicação), com justificativa; 2 = só o nome; 1 = dedução; 0 = nenhuma.
- **EX002 — Encontre a falácia.** "A indisponibilidade aconteceu depois do e-mail de phishing, então o e-mail a causou." Nomeie a falácia. *Rubrica:* 3 = post hoc ergo propter hoc, com o porquê; 2 = só o nome; 1 = falácia errada; 0 = nenhuma.
- **EX003 — Pergunta de linha de base.** Liste três perguntas a fazer sobre "os ataques subiram 300%". *Rubrica:* 3 = linha de base, período, método de contagem (ou mudança nas regras de notificação); 2 = duas; 1 = uma; 0 = nenhuma.

### Síntese

Nomeie o tipo de inferência, pegue as falácias, dê os numeradores junto com as porcentagens e escreva as premissas.

### Continue estudando — capítulo 01 de 40

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever os componentes do parque computacional de um hospital relevantes para a CTI; (2) explicar que logs cada componente produz; (3) identificar onde os indicadores podem ser conferidos; (4) reconhecer os dispositivos médicos como casos especiais.

### 2.1 O parque computacional

O HCHT opera estações de trabalho dos funcionários, aplicações clínicas, um portal do paciente, e-mail, um serviço de diretório, caixas de correio na nuvem, sistemas de laboratório e dispositivos médicos em rede. Cada um tem responsáveis, rotas de atualização e logs. A CTI só é útil se chega ao lugar onde pode ser conferida ou aplicada. A primeira tarefa de Amara é listar, para cada parte do parque, quem é o responsável, como é atualizada e o que registra. A lista mostra onde a inteligência pode ser usada depressa, como na filtragem de e-mail, e onde não pode, como nos sistemas de laboratório operados por um fornecedor sob contrato.

### 2.2 Logs como sensores

Gateways de e-mail registram remetentes e anexos; proxies web registram URLs; resolvedores DNS registram consultas; endpoints registram processos; o diretório registra logons. Quando o HSSC compartilha um domínio malicioso, Amara pode buscar contatos passados nos logs de DNS e de proxy — uma caçada retrospectiva. Uma caçada retrospectiva responde a uma pergunta simples: algo no HCHT contatou este domínio antes de sabermos que era malicioso? Amara confere se a retenção dos logs cobre o período descrito no relatório do HSSC, já que uma caçada não encontra contatos mais antigos que o log mais antigo. Onde a retenção é curta, ela registra a lacuna em vez de relatar um resultado limpo.

### 2.3 Pontos de aplicação

Filtros de e-mail, bloqueio por DNS, categorias de proxy e regras de endpoint podem agir sobre indicadores. Cada um tem um raio de impacto diferente. Bloquear um domínio no DNS afeta todo dispositivo que usa o resolvedor, inclusive os sistemas clínicos. Um bloqueio errado no DNS poderia impedir uma aplicação clínica de alcançar o serviço de um fornecedor e atrasar o atendimento aos pacientes. Por isso Amara registra, para cada ponto de aplicação, quem pode alterá-lo, com que rapidez um bloqueio pode ser revertido e quais sistemas ele afeta. Indicadores de baixa confiança vão primeiro para monitoramento, onde geram alertas sem interromper o tráfego, até que a evidência sustente um bloqueio.

### 2.4 Dispositivos médicos

Bombas de infusão e sistemas de imagem costumam rodar sistemas operacionais antigos e não podem ser corrigidos depressa. Podem não tolerar varreduras nem software de agente. A CTI sobre ameaças a esses dispositivos vai para a equipe de engenharia clínica, que decide pelo isolamento de rede em vez de mudanças no host. Amara aprende que a segurança do paciente vem primeiro: uma mudança de segurança que faz uma bomba parar de funcionar é pior do que a ameaça que ela pretendia tratar. A inteligência sobre esses dispositivos é redigida para engenheiros clínicos, nomeando o modelo do dispositivo e a exposição, e eles decidem que mudança é segura para os pacientes.

### 2.5 Inventário de ativos

Um inventário preciso permite que os analistas respondam "usamos o produto afetado?" em minutos quando chega um alerta. Sem ele, cada alerta dispara um exercício de adivinhação. O inventário do HCHT lista produtos de software e versões para estações de trabalho e servidores, mas os dispositivos médicos são registrados só pelo modelo, então Amara anota que alertas sobre software de dispositivos exigem conferência extra com a engenharia clínica. Manter o inventário atualizado é tarefa de operações; o papel de Amara é relatar onde as lacunas atrasaram uma resposta, para que os responsáveis possam corrigi-las.

### Sistemas na nuvem e de fornecedores

Alguns serviços do HCHT rodam em plataformas de fornecedores: o e-mail na nuvem, o portal de agendamento e o software de patologia. Os logs ficam com o fornecedor. Os contratos devem dizer que logs o HCHT pode obter e com que rapidez, porque uma caçada a indicadores é impossível sem acesso aos registros relevantes.

### Exemplo resolvido

O HSSC compartilha um alerta sobre um produto de servidor de imagem vulnerável. Amara consulta o inventário: dois servidores em um hospital correspondem. Ela envia o alerta à engenharia clínica com os identificadores dos ativos, e não à fila geral de TI, porque os servidores são sistemas médicos certificados.

> **Caso sintético.** O alerta e os servidores são inventados.

### Erros e limites

Inventários envelhecem; confirme com os responsáveis. Não faça varreduras em dispositivos médicos sem aprovação da engenharia clínica.

### Exercícios

- **EX004 — Fonte de log.** Que log mostraria se algum dispositivo do HCHT consultou um domínio malicioso na semana passada? *Rubrica:* 3 = logs do resolvedor DNS (proxy como fonte secundária); 2 = só o proxy; 1 = antivírus do endpoint; 0 = nenhuma.
- **EX005 — Rota do dispositivo.** Por que Amara encaminhou o alerta de imagem à engenharia clínica? *Rubrica:* 3 = sistemas médicos certificados; processo especial de mudança/segurança; responsáveis; 2 = só os responsáveis; 1 = conveniência; 0 = nenhuma.
- **EX006 — Raio de impacto.** Dê um risco de bloquear um domínio no resolvedor DNS de um hospital. *Rubrica:* 3 = pode quebrar sistemas clínicos que dependem dele/dano colateral; 2 = vago; 1 = nenhum risco; 0 = nenhuma.

### Síntese

Conheça o parque, seus logs e pontos de aplicação, trate os dispositivos médicos à parte e mantenha o inventário atualizado.

### Continue estudando — capítulo 02 de 40

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever funções em Python que limpam e classificam indicadores; (2) usar strings, listas, conjuntos e dicionários; (3) tratar entradas ruins de forma explícita; (4) manter os scripts livres de coleta pela rede.

### 3.1 Por que analistas programam

Os analistas recebem indicadores em e-mails, PDFs e planilhas. Scripts pequenos extraem, limpam e comparam esses indicadores mais depressa e com mais precisão do que copiar à mão. Aqui, programar é uma ferramenta de leitura e conferência, não de coleta. Amara escreve seu primeiro script para ler indicadores de uma planilha compartilhada pelo HSSC, remover duplicatas e compará-los com uma lista exportada do gateway de e-mail. Feita à mão, a comparação levava uma hora e deixou passar duas correspondências; o script leva segundos e dá a mesma resposta toda vez que roda.

### 3.2 Tipos para inteligência

Uma string guarda um indicador. Uma lista mantém a ordem, como eventos no tempo. Um conjunto remove duplicatas e permite a interseção — quais indicadores aparecem tanto nos nossos logs quanto no feed? Um dicionário associa um indicador a seus metadados: fonte, TLP, primeira observação. Escolher o tipo certo torna a pergunta fácil de responder. O script de Amara guarda os indicadores do feed em um conjunto, então a sobreposição com os logs do HCHT é uma única interseção, e mantém os metadados em um dicionário, então cada correspondência vem com sua fonte e seu rótulo TLP. Sem o rótulo, ela não saberia quais correspondências podem ser compartilhadas com outras equipes.

### 3.3 Classificar valores

Uma função simples decide se uma string parece um endereço IPv4, um domínio ou um hash. O módulo `ipaddress` da biblioteca padrão valida endereços; verificações de tamanho e de caracteres distinguem hashes SHA-256 (64 caracteres hexadecimais) de outras strings. Amara testa a função com exemplos de cada tipo e com casos traiçoeiros, como um domínio que contém dígitos ou um hash com letras maiúsculas. Um valor mal classificado poderia mandar um domínio para uma lista de bloqueio de endereços, onde não faria nada, enquanto a analista acreditava que ele estava bloqueado.

### 3.4 Falha explícita

Se um valor não se encaixa em nenhum tipo, retorne "unknown" e guarde-o para revisão. Adivinhar cria indicadores falsos que podem depois bloquear serviços legítimos. O script de Amara grava os valores desconhecidos em um arquivo separado, com a linha de onde vieram, para que ela possa conferi-los à mão. Muitos se revelam indicadores desarmados, como domínios com colchetes em volta dos pontos, que o script agora trata de forma explícita. A falha explícita transformou um erro silencioso em uma lista de melhorias e manteve indicadores falsos fora das listas de bloqueio.

### 3.5 Nenhuma coleta oculta

Os scripts deste curso leem apenas arquivos locais. Código que baixa páginas web, consulta serviços externos ou entra em plataformas está fora deste capítulo e exige termos, permissão e supervisão. Amara faz duas perguntas sobre o próprio trabalho: de onde vem cada entrada, e ela tinha permissão para usá-la? Quando uma fonte publica apenas uma página web, ela pede à mesa do HSSC um arquivo exportado em vez de acrescentar uma etapa de download ao script. Qualquer etapa de coleta é uma decisão separada de sua supervisora, com aprovação e registro próprios.

### Código legível

Analistas compartilham scripts com colegas que precisam confiar na saída. Nomes de função claros, docstrings curtas e um pequeno teste com entradas conhecidas tornam um script revisável. Um teste que alimenta um hash válido, um hash truncado e um domínio mostra aos revisores exatamente como os casos de borda se comportam antes de o script tocar dados reais.

### Exemplo resolvido

Amara recebe 40 valores colados de um PDF. Seu classificador rotula 18 domínios, 12 endereços IPv4, 7 hashes SHA-256 e 3 desconhecidos — dois eram hashes truncados e um, um domínio com um colchete perdido do desarmamento. Ela corrige o colchete, devolve os hashes truncados ao remetente e armazena 38.

> **Caso sintético.** Os valores do PDF são inventados.

### Erros e limites

Verificações de padrão confirmam a forma, não a malícia. Um domínio de aparência válida ainda pode ser um erro de digitação.

### Exercícios

- **EX007 — Escolha um tipo.** Que tipo do Python encontra os indicadores presentes tanto no feed quanto nos logs do HCHT, e como? *Rubrica:* 3 = interseção de conjuntos (&); 2 = só conjunto; 1 = laço em lista sem remover duplicatas; 0 = nenhuma.
- **EX008 — Forma do hash.** Que forma tem um hash SHA-256 como texto? *Rubrica:* 3 = 64 caracteres hexadecimais; 2 = 64 caracteres; 1 = 32; 0 = nenhuma.
- **EX009 — Valor truncado.** O que Amara deve fazer com os dois hashes truncados? *Rubrica:* 3 = marcar como desconhecidos, não armazená-los como indicadores, avisar o remetente; 2 = descartar; 1 = completar e armazenar; 0 = nenhuma.

### Síntese

Use o tipo de dado certo, valide a forma, falhe de forma explícita e mantenha os scripts locais.

### Continue estudando — capítulo 03 de 40

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) estruturar um argumento com alegação, evidência e raciocínio; (2) citar fontes corretamente; (3) escrever com a ressalva adequada; (4) adaptar hábitos acadêmicos à escrita de inteligência.

### 4.1 Alegação, evidência, raciocínio

Um parágrafo faz uma alegação, apresenta a evidência e explica por que a evidência sustenta a alegação. "O phishing é a via de entrada mais comum nos relatórios do HSSC (alegação); ele aparece em 3 de 5 relatórios de 2026 (evidência); as outras vias aparecem no máximo duas vezes (raciocínio)." Os leitores podem então contestar a evidência em vez de adivinhar o que você quis dizer. Amara usa esse padrão em todos os parágrafos de seus relatórios. Assim, sua supervisora confere a evidência depressa, e um leitor que discorda sabe exatamente que parte questionar. Quando uma alegação ainda não tem evidência, ela a rotula como hipótese e diz o que a testaria.

### 4.2 Citação

Cite especificações para definições (STIX 2.1 para tipos de objeto), artigos para modelos (Hutchins et al. para a kill chain) e fontes de dados para números. Parafraseie e cite; cite literalmente só quando a redação exata importa. Nunca cite um relatório com restrição TLP em trabalhos acadêmicos públicos. Amara mantém uma lista de referências para cada trabalho e confere se cada marcação TLP permite o uso que ela faz de uma fonte. Para um ensaio sobre phishing na saúde, ela cita apenas relatórios públicos e descreve as tendências do HSSC em termos gerais, sem nomear nenhum relatório restrito, para que o ensaio possa ser compartilhado com a turma.

### 4.3 Ressalvas

"Prova" raramente se justifica. "Sugere", "é compatível com" e palavras calibradas como "provável" sinalizam a incerteza com honestidade. O excesso de ressalvas — "talvez possivelmente quem sabe" — é tão inútil quanto exagerar a alegação. Amara aprende a escolher uma palavra calibrada por julgamento e a dizer em que ela se apoia, como "provável, com base em dois relatórios independentes". Um leitor pode agir com base nisso, ou pedir mais evidência, e esse é o propósito de fazer ressalvas com honestidade. Ela evita empilhar qualificadores, o que esconde o julgamento em vez de expressar sua incerteza.

### 4.4 Estilo acadêmico versus estilo de inteligência

A escrita acadêmica costuma construir o caminho até uma conclusão. A escrita de inteligência declara a conclusão principal primeiro. A ICD 203 pede que os produtos analíticos sejam claros e lógicos; os dois estilos compartilham esse objetivo, mas diferem na ordem. Amara aprende os dois. Na prática, ela escreve os ensaios do curso em estilo acadêmico e suas notas para o HCHT com a conclusão principal na primeira frase, seguida da evidência. Leitores ocupados da equipe de segurança podem ler só essa primeira linha, então ela precisa estar correta por si só. Sua supervisora confere se a evidência abaixo realmente a sustenta.

### 4.5 Revisão

Leia os rascunhos em voz alta, corte palavras que não mudam o sentido e peça a um colega que reformule sua alegação principal. Amara lê em voz alta sua primeira nota para o HCHT e encontra duas frases que dizem a mesma coisa. Um colega reformula sua alegação principal como "bloquear estes domínios" quando ela queria dizer "monitorar estes domínios", então ela reescreve a linha de abertura para deixar a ação clara. É na revisão que surge a maior parte da clareza de um relatório, e ela reserva tempo para isso em vez de tratar a revisão como opcional.

### Escrever para não especialistas

Gestores clínicos também leem as notas de segurança do HCHT. Troque o jargão por palavras simples ou defina-o uma vez: "phishing (e-mail fraudulento que engana as pessoas para que ajam)". Frases curtas, voz ativa e ações concretas — "encaminhe faturas suspeitas à central de atendimento" — tornam a orientação utilizável por funcionários ocupados das enfermarias, que têm minutos, e não horas, para lê-la.

### Exemplo resolvido

O primeiro parágrafo do ensaio de Amara mistura três alegações sobre phishing, ransomware e ameaças internas. Seu orientador pede uma alegação por parágrafo. Ela o divide em três, cada um com sua evidência, e leva a conclusão para a frase de abertura na versão em estilo de inteligência.

> **Caso sintético.** O ensaio é inventado.

### Erros e limites

Citar uma fonte não a torna confiável; avalie-a. As regras de integridade acadêmica proíbem apresentar a análise de outra pessoa como sua.

### Exercícios

- **EX010 — Monte um parágrafo.** Escreva um parágrafo de alegação, evidência e raciocínio sobre uma técnica do ATT&CK em um setor fictício. *Rubrica:* 3 = as três partes claras; 2 = duas; 1 = só a alegação; 0 = nenhuma.
- **EX011 — Fonte restrita.** Amara pode citar um relatório TLP:AMBER do HSSC em um ensaio público? *Rubrica:* 3 = não; usar fontes públicas ou exemplos sintéticos; 2 = não; 1 = sim, com atribuição; 0 = nenhuma.
- **EX012 — Diferença de ordem.** Como a ordem da escrita de inteligência difere da escrita acadêmica típica? *Rubrica:* 3 = conclusão principal primeiro vs construção até a conclusão; 2 = parcial; 1 = nenhuma diferença; 0 = nenhuma.

### Síntese

Uma alegação por parágrafo, cite com precisão e de forma lícita, faça ressalvas honestas e saiba quando começar pela conclusão.

### Continue estudando — capítulo 04 de 40

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) definir ameaça, vulnerabilidade, risco e controle; (2) descrever o ciclo de vida da CTI; (3) distinguir inteligência estratégica, operacional e tática; (4) explicar por que a saúde atrai atacantes.

### 5.1 Termos centrais

Uma ameaça é uma causa potencial de dano — um ator ou um evento. Uma vulnerabilidade é uma fraqueza. O risco combina probabilidade e impacto. Um controle reduz o risco. A CTI informa a parte da ameaça nessa equação, para que os controles vão para onde importam. Para o HCHT, a ameaça é um grupo criminoso que envia phishing aos funcionários clínicos, a vulnerabilidade é um serviço de acesso remoto sem correção e o risco é alto porque uma indisponibilidade afetaria o atendimento aos pacientes. A inteligência sobre os métodos do grupo ajuda a decidir que controles reforçar primeiro.

### 5.2 O ciclo de vida da CTI

Direção (do que os tomadores de decisão precisam?), coleta, processamento, análise, disseminação e feedback. Na prática, a direção muitas vezes falta; os analistas então coletam tudo e não ajudam ninguém. Requisitos prioritários de inteligência resolvem isso. Amara ajuda sua supervisora a redigir os primeiros requisitos do HCHT: que ameaças poderiam interromper os serviços clínicos, quais fornecedores são visados e que técnicas aparecem em ataques ao setor de saúde. Cada requisito nomeia quem precisa da resposta e com que frequência. A coleta então se concentra nas fontes que os respondem, e o feedback mostra se as respostas foram úteis, de modo que o ciclo melhora com o tempo.

### 5.3 Três níveis

Estratégico: tendências e intenções para executivos — por exemplo, grupos criminosos que visam hospitais para extorsão. Operacional: campanhas e momento para os líderes de incidente — uma onda de phishing contra instituições de saúde neste mês. Tático: indicadores e técnicas para analistas — domínios remetentes e T1566 Phishing. Cada nível atinge um público diferente e pede um estilo diferente. Amara pratica escrever o mesmo relatório do HSSC de três formas: um parágrafo curto para o conselho, uma página para os líderes de incidente e uma lista de indicadores com técnicas para os analistas. Misturar níveis, como entregar listas de indicadores ao conselho, desperdiça o tempo do leitor e esconde o que ele precisa decidir.

### 5.4 Por que a saúde

Hospitais guardam dados sensíveis, funcionam 24 horas por dia e não toleram indisponibilidade, o que aumenta a pressão para pagar a extorsão. Sistemas legados e muitos fornecedores ampliam a exposição. A inteligência estratégica ajuda os conselhos a entender esse contexto sem sensacionalismo. O briefing de Amara para o conselho do HCHT usa relatórios do setor para descrever a ameaça com precisão e liga cada ponto a uma decisão que o conselho pode tomar, como financiar uma recuperação mais rápida dos sistemas clínicos. Ela evita linguagem alarmista e usa números só quando a fonte e a amostra estão claras.

### 5.5 Inteligência versus informação

Um feed de domínios é informação. Uma avaliação de que uma campanha visa sistemas de laboratório e de que o HCHT deve bloquear domínios específicos e orientar os funcionários do laboratório é inteligência — analisada e ligada a uma decisão. Amara confere cada produto que escreve com este teste: que decisão ele apoia, e quem a toma? Uma lista que ela não consegue ligar a uma decisão é mantida como informação e guardada para buscas futuras, não enviada como inteligência. Isso reserva a caixa de entrada da equipe de segurança para material que lhe pede algo, e ajuda o HSSC a ver quais dos itens compartilhados foram de fato usados.

### Quem consome inteligência no HCHT

Os consumidores incluem a central de atendimento, a equipe de rede, a engenharia clínica, o encarregado de proteção de dados e o conselho. Cada um precisa de detalhes diferentes em velocidades diferentes. Mapear os consumidores e suas decisões é o primeiro passo prático da direção, porque mostra que perguntas a inteligência precisa responder e em que formato cada público consegue de fato usar a resposta.

### Exemplo resolvido

O diretor executivo do HCHT pergunta se a instituição é "um alvo". A supervisora de Amara responde no nível estratégico: organizações de saúde da região enfrentaram campanhas de extorsão; a exposição do HCHT é típica; as principais prioridades defensivas são a resistência ao phishing e os backups. Os indicadores ficam fora do briefing executivo.

> **Caso sintético.** O briefing é inventado.

### Erros e limites

Briefings movidos pelo medo distorcem o investimento. Os níveis se sobrepõem; rotule o público pretendido.

### Exercícios

- **EX013 — Rótulo de nível.** Classifique "domínios remetentes da onda de phishing desta semana". *Rubrica:* 3 = tático, com o público; 2 = tático; 1 = estratégico; 0 = nenhuma.
- **EX014 — Etapa ausente.** Que etapa do ciclo de vida falta com mais frequência, e o que a corrige? *Rubrica:* 3 = direção; requisitos prioritários de inteligência; 2 = só direção; 1 = coleta; 0 = nenhuma.
- **EX015 — Omissão no briefing executivo.** Por que deixar os indicadores fora do briefing do diretor executivo? *Rubrica:* 3 = nível/público errado; executivos precisam de contexto estratégico e decisões; 2 = parcial; 1 = sigilo; 0 = nenhuma.

### Síntese

Use os termos centrais com precisão, comece o ciclo pela direção, ajuste o nível ao público e transforme informação em inteligência.

### Continue estudando — capítulo 05 de 40

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) usar conjuntos e relações para modelar indicadores e atores; (2) representar inteligência como grafos; (3) raciocinar sobre caminhos e componentes conexos; (4) reconhecer os limites da análise de vínculos.

### 6.1 Conjuntos e relações

Cada feed é um conjunto de indicadores. A união combina feeds; a interseção mostra concordância; a diferença mostra o que só uma fonte tem. Uma relação forma pares de elementos: (domínio, resolve-para, endereço). Os objetos de relacionamento do STIX 2.1 expressam exatamente isso — um objeto de origem, um tipo de relacionamento e um objeto de destino. Amara usa operações de conjuntos para comparar dois feeds do HSSC e descobre que eles se sobrepõem em apenas um terço dos indicadores. A concordância entre fontes independentes aumenta a confiança; os indicadores encontrados em um único feed não estão errados, mas precisam de mais conferência antes de um bloqueio.

### 6.2 Grafos

Trate indicadores, famílias de malware e campanhas como nós, e os relacionamentos como arestas. Os grafos tornam os pivôs visíveis: dois domínios de phishing que resolveram para o mesmo endereço ficam ligados por esse nó de endereço. Os quatro vértices do Diamond Model — adversário, capacidade, infraestrutura, vítima — são, eles mesmos, um pequeno grafo para cada evento. Amara monta um pequeno grafo a partir de um relatório do HSSC e confere cada aresta com sua fonte antes de tirar conclusões. Cada aresta leva a fonte que a relatou e a data, então uma ligação que se apoia em um relatório antigo ou fraco pode ser identificada e, se preciso, removida sem reconstruir o grafo inteiro.

### 6.3 Caminhos e componentes

Um caminho liga dois nós por meio de arestas. Um componente conexo é um grupo em que todo nó alcança todos os outros. Às vezes os analistas tratam um componente como "uma campanha". Isso é uma hipótese, não um fato. Amara escreve "estes indicadores formam um grupo conexo, que pode ser uma campanha", e não "esta é uma campanha". Depois ela procura evidências que os separariam, como técnicas de entrega ou momentos diferentes. Um componente formado por um endereço de hospedagem compartilhada, por exemplo, pode juntar atores sem relação entre si, então a hipótese precisa ser testada antes que alguém aja com base nela.

### 6.4 A armadilha da infraestrutura compartilhada

Hospedagem compartilhada, redes de distribuição de conteúdo e endereços de nuvem ligam clientes sem relação entre si. Um endereço que serve milhares de domínios liga todos eles em um grafo ingênuo. Antes de confiar em uma ligação, pergunte quantas outras coisas compartilham aquele nó; nós de grau alto costumam ser ruído. Amara confere o número de domínios em cada endereço com as informações públicas do provedor de hospedagem ou com um registro de DNS passivo, e descarta as arestas que passam por nós que servem muitos sites sem relação. Ela registra cada aresta removida e o motivo, para que um revisor possa ver a escolha.

### 6.5 Dirigido versus não dirigido

"O domínio resolve para o endereço" tem direção; "apareceu no mesmo relatório" não tem. Mantenha a direção onde ela carrega significado, ou você vai raciocinar de trás para frente. Amara guarda cada relacionamento com seu tipo e sua direção, seguindo os objetos de relacionamento do STIX. Inverter uma aresta, por exemplo lendo "o endereço resolve para o domínio", poderia levar à falsa conclusão de que todo domínio em um endereço compartilhado pertence ao mesmo ator. Ligações não dirigidas, como a coocorrência em um relatório, ficam separadas e são tratadas como evidência mais fraca, já que só mostram que duas coisas foram mencionadas juntas.

### 6.6 O grau como sinal de alerta

O grau de um nó é o número de suas arestas. Um hub repentino em um pequeno grafo de inteligência merece inspeção: pode ser um servidor de comando genuíno, ou um resolvedor público, um provedor de webmail ou um artefato de parsing equivocado. Amara acrescenta ao script do grafo uma verificação de grau que lista, para revisão manual, qualquer nó acima de um limiar escolhido. O limiar é definido a partir da forma normal do grafo, e cada nó marcado é conferido com informações públicas antes de ser mantido. Um resolvedor público ou um provedor de webmail é removido com uma nota; um servidor genuíno é mantido e destacado.

### Exemplo resolvido

Amara liga seis domínios de phishing do HSSC. Cinco se juntam em um componente por meio de um único endereço. Ela confere o endereço: ele pertence a um grande provedor de hospedagem e serve muitos sites sem relação. Ela o remove como pivô; os seis domínios se dividem em três pequenos grupos, dois deles ligados por um padrão comum de e-mail de registro. Sua nota diz "dois domínios podem estar relacionados; evidência fraca".

> **Caso sintético.** Os domínios e os detalhes de hospedagem são inventados.

### Erros e limites

Grafos mostram coocorrência, não intenção. Um desenho com muitas linhas parece convincente; teste cada aresta.

### Exercícios

- **EX016 — Operação de conjuntos.** Que operação de conjuntos lista os indicadores que só o HSSC tem, e não a lista de bloqueio do próprio HCHT? *Rubrica:* 3 = diferença (HSSC − HCHT); 2 = nomeada, mas com a direção errada; 1 = interseção; 0 = nenhuma.
- **EX017 — Grau alto.** Por que Amara descartou o endereço de hospedagem como pivô? *Rubrica:* 3 = nó compartilhado/de grau alto liga sites sem relação; ligação falsa; 2 = parcial; 1 = era malicioso; 0 = nenhuma.
- **EX018 — Vértices do Diamond.** Nomeie os quatro vértices do Diamond Model. *Rubrica:* 3 = adversário, capacidade, infraestrutura, vítima; 2 = três; 1 = um ou dois; 0 = nenhuma.

### Síntese

Conjuntos e grafos organizam a inteligência; confira os nós de grau alto, mantenha a direção e trate os componentes como hipóteses.

### Continue estudando — capítulo 06 de 40

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar DNS, HTTP(S) e SMTP no nível de que a CTI precisa; (2) ler cabeçalhos de e-mail em busca de pistas sobre o remetente; (3) entender por que o tráfego cifrado limita a visibilidade; (4) relacionar protocolos a técnicas do ATT&CK.

### 7.1 DNS

O Domain Name System associa nomes a endereços. Os logs do resolvedor registram qual dispositivo pediu qual nome e quando. Como quase toda conexão começa com uma consulta, o DNS é a fonte mais amplamente útil para conferir indicadores de domínio. Amara verifica por quanto tempo o HCHT guarda os logs do resolvedor e se eles registram o endereço interno do dispositivo ou só o endereço de um servidor de encaminhamento, o que esconderia qual estação de trabalho fez a consulta. Os dois fatos decidem se uma busca retrospectiva por um domínio do HSSC consegue encontrar o dispositivo que o contatou, e ambos ficam escritos em suas notas sobre cada fonte.

### 7.2 HTTP e HTTPS

O tráfego web carrega a maior parte da atividade dos usuários e muito tráfego malicioso de comando. A técnica Application Layer Protocol do ATT&CK (T1071) descreve adversários que se misturam ao tráfego normal de web, e-mail ou DNS. Com HTTPS, um proxy pode ver só o nome do servidor, não o caminho completo, a menos que o tráfego seja inspecionado — uma decisão com implicações jurídicas e de privacidade em um hospital. A equipe jurídica e de privacidade do HCHT decidiu que categorias de tráfego podem ser inspecionadas, e os sites de saúde usados pelos funcionários para cuidados pessoais ficam excluídos. Amara trabalha com o que o proxy registra sob essa decisão, em geral o nome do servidor e o horário, e anota quando um indicador não pode ser conferido porque só o caminho completo o revelaria.

### 7.3 SMTP e cabeçalhos

Os cabeçalhos de e-mail registram o caminho que a mensagem percorreu: as linhas Received, o remetente do envelope e os resultados de autenticação (SPF, DKIM, DMARC). Um nome de exibição dizendo "HCHT Payroll" não significa nada se a autenticação falha e o domínio remetente é um domínio sósia. Amara aprende a ler primeiro os resultados de autenticação, depois o domínio remetente e só então o nome de exibição, que é a parte mais fácil de um atacante falsificar. Ela compara os domínios sósias dos relatórios do HSSC com os domínios do próprio HCHT para ver que truques miram a instituição.

### 7.4 Portas e serviços

Portas ou protocolos incomuns podem sugerir tunelamento, mas muitos sistemas médicos legítimos também usam portas incomuns. O contexto dado pelos responsáveis pelos ativos vale mais que regras práticas. Amara pergunta à equipe de engenharia clínica que portas seus dispositivos usam antes de tratar qualquer porta incomum como suspeita. Uma lista de portas clínicas conhecidas, mantida junto com o inventário de ativos, evita alertas sobre o tráfego normal de imagem e deixa as anomalias reais se destacarem. Cada entrada registra o modelo do dispositivo e o responsável que a confirmou.

### 7.5 Horários e endereços

Os logs de rede registram horários em fusos diferentes e endereços que podem ser traduzidos por firewalls. Normalize os horários para UTC e anote a tradução de endereços antes de correlacionar com indicadores compartilhados. Amara descobriu que o proxy do HCHT registrava a hora local, enquanto os relatórios do HSSC usam UTC, o que fazia um contato parecer ter ocorrido uma hora antes da primeira observação do domínio. Depois da normalização, a ordem fez sentido. Agora ela registra o fuso horário e qualquer tradução de endereços de cada fonte de log em uma tabela curta, para que outros analistas possam correlacionar eventos sem redescobrir os mesmos problemas.

### 7.6 Resultados de autenticação na prática

O SPF verifica se o servidor remetente pode enviar pelo domínio do envelope; o DKIM verifica uma assinatura sobre a mensagem; o DMARC os vincula ao domínio visível no campo From e declara a política do titular. Uma mensagem pode passar no SPF de um domínio sósia que o atacante controla, então passar nas verificações prova apenas quem a enviou, não que o remetente seja benigno. Amara acrescenta isso à sua lista de verificação para relatos de phishing. Para cada mensagem de phishing relatada, ela registra os três resultados e se o domínio visível é do próprio HCHT, de um parceiro conhecido ou um sósia. Isso torna visível, ao longo do tempo, o padrão de falsificação.

### Exemplo resolvido

Uma gerente de enfermaria encaminha um e-mail suspeito de "atualização salarial". Amara lê os cabeçalhos: o domínio no campo From é hcht-payrolI.example (I maiúsculo no lugar de l), o SPF passa para esse domínio sósia e o alinhamento DMARC falha em relação ao domínio real. Ela registra o sósia como indicador de phishing (T1566) e o compartilha com o HSSC em TLP:GREEN depois de remover o endereço da funcionária destinatária.

> **Caso sintético.** O e-mail e os domínios são inventados.

### Erros e limites

Cabeçalhos anteriores ao seu próprio gateway podem ser forjados. A inspeção de tráfego cifrado exige aprovação de política e aviso aos funcionários.

### Exercícios

- **EX019 — Veredito do cabeçalho.** O SPF passa, mas o alinhamento DMARC falha em relação ao domínio real. O que isso diz a Amara? *Rubrica:* 3 = o remetente está autorizado para o sósia, não para o domínio real; falsificação/sósia; 2 = parcial; 1 = o e-mail é seguro; 0 = nenhuma.
- **EX020 — Melhor fonte para domínios.** Por que o DNS é a fonte mais útil para indicadores de domínio? *Rubrica:* 3 = quase todas as conexões começam com consultas; cobertura ampla; 2 = parcial; 1 = criptografia; 0 = nenhuma.
- **EX021 — Limite do HTTPS.** O que um proxy normalmente vê no tráfego HTTPS sem inspeção? *Rubrica:* 3 = nome do servidor (SNI)/destino, não o caminho nem o conteúdo; 2 = só o destino; 1 = tudo; 0 = nenhuma.

### Síntese

Os logs de DNS, web e e-mail são os principais pontos de conferência do analista de CTI; leia os cabeçalhos com senso crítico e respeite os limites da visibilidade sobre o tráfego cifrado.

### Continue estudando — capítulo 07 de 40

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) fazer o parsing de um feed de indicadores em CSV com a biblioteca padrão; (2) validar cada linha e registrar os motivos de rejeição; (3) relatar contagens com honestidade; (4) projetar scripts que possam ser auditados.

### 8.1 Feeds como arquivos

O HSSC distribui um CSV diário com colunas para tipo, valor, data da primeira observação e TLP. Planilhas estragam esses arquivos — transformam números longos em notação científica ou removem zeros à esquerda —, por isso Amara os processa com o módulo `csv` do Python. Ela mantém o arquivo original inalterado e grava a saída processada em um arquivo novo, para que qualquer dúvida sobre o feed possa ser conferida com o que o HSSC realmente enviou. Ela evita abrir o original em uma planilha mesmo para uma olhada rápida, porque salvá-lo por acidente poderia mudar valores sem que ninguém percebesse.

### Laboratório — validar um feed

```python
"""Lab 2 (ch 08): parse a synthetic CSV feed with the csv module and count accepted/rejected rows."""
import csv, io
data = """type,value,first_seen,tlp
domain,portal-login.example,2026-09-01,TLP:GREEN
ipv4,203.0.113.50,2026-09-02,TLP:AMBER
domain,,2026-09-02,TLP:GREEN
sha256,abc123,2026-09-03,TLP:GREEN
url,http://files.example/x,2026-09-04,TLP:CLEAR
"""
ok, bad = [], []
for row in csv.DictReader(io.StringIO(data)):
    if not row["value"]:
        bad.append(("empty value", row)); continue
    if row["type"] == "sha256" and len(row["value"]) != 64:
        bad.append(("sha256 length", row)); continue
    ok.append(row)
print("accepted", len(ok), "rejected", len(bad))
for reason, row in bad:
    print(" reject:", reason, row["type"], row["first_seen"])
```

Execute com `python3 lab_csvfeed.py`. Saída verificada:

```text
accepted 3 rejected 2
 reject: empty value domain 2026-09-02
 reject: sha256 length sha256 2026-09-03
```

### 8.2 Lendo o resultado

Três linhas passam; duas falham. Uma tem o valor de domínio vazio; outra diz ser um hash SHA-256, mas tem o tamanho errado. Cada rejeição é impressa com sua data e seu motivo, para que Amara possa enviar ao HSSC um feedback preciso, em vez de "seu feed está quebrado". O feedback vai para o contato do HSSC com os números das linhas, para que os erros sejam corrigidos na origem para todos os membros. Ela também confere se as mesmas falhas apareceram em arquivos anteriores. Nenhuma tinha aparecido.

### 8.3 Regras de validação

As regras verificam presença (nenhum valor vazio), forma (tamanho do hash, endereço válido), vocabulário permitido (rótulos TLP do FIRST TLP 2.0: CLEAR, GREEN, AMBER, AMBER+STRICT, RED) e formato de data. As regras devem ser poucas, explícitas e testadas. Amara escreve um teste para cada regra usando um pequeno arquivo de linhas boas e ruins, então mudar uma regra mostra na hora que casos ela afeta. Ela mantém a lista de regras na documentação do script e a compartilha com o HSSC, para que a comunidade saiba o que o HCHT confere e possa pegar problemas antes de enviar o feed. Novas regras só são acrescentadas depois que um problema real mostra que são necessárias.

### 8.4 Nunca descarte em silêncio

Um script que pula linhas ruins sem avisar torna as contagens indignas de confiança. Sempre relate os totais aceitos e rejeitados. A importação de Amara imprime os dois totais e grava as linhas rejeitadas em um arquivo, com o motivo de cada uma. Se os totais não somam o número de linhas do feed, o script para com um erro. Um descarte silencioso já escondeu por uma semana uma mudança de coluna em um feed, até que um domínio ausente foi notado por acaso, e é por isso que a regra agora é rígida.

### 8.5 Idempotência

Rodar a importação duas vezes não deve criar duplicatas. Use o valor mais o tipo como chave e atualize os metadados em vez de acrescentar linhas novas. Amara testa isso importando o mesmo feed duas vezes e conferindo que a contagem de linhas não muda, enquanto a data da última observação é atualizada. A idempotência importa porque as importações são executadas de novo depois de falhas, e as duplicatas inflariam as contagens nos relatórios e fariam um indicador parecer vir de duas fontes, aumentando uma confiança que a evidência não sustenta.

### 8.6 Codificação e delimitadores

Os feeds chegam com codificações e separadores diferentes. Abra os arquivos com uma codificação explícita, detecte ou declare o delimitador e remova caracteres invisíveis, como marcas de ordem de bytes, do primeiro cabeçalho. Muitos erros intrigantes de "coluna ausente" são só um caractere escondido no nome do primeiro campo. Amara acrescenta as duas etapas à sua função de importação. A importação imprime a codificação e o delimitador detectados, para que uma mudança na forma como o HSSC produz o arquivo seja notada na hora, em vez de aparecer mais tarde como um erro intrigante. Amara mantém um pequeno conjunto de arquivos de exemplo com codificações diferentes como testes.

### Exemplo resolvido

No dia seguinte, o feed traz uma linha com TLP "AMBER STRICT" (espaço em vez de sinal de mais). O script de Amara a rejeita com o motivo `unknown TLP label`. Ela pede ao HSSC que a corrija em vez de adivinhar, porque tratá-la como AMBER afrouxaria uma restrição.

> **Caso sintético.** As linhas do feed são inventadas.

### Erros e limites

Formato válido não é verdade. Um indicador bem formado pode estar errado ou desatualizado; a validação é só a primeira barreira.

### Exercícios

- **EX022 — Rejeições do laboratório.** Que duas linhas falharam no laboratório, e por quê? *Rubrica:* 3 = domínio vazio (09-02); tamanho de sha256 errado (09-03); 2 = uma; 1 = só as contagens; 0 = nenhuma.
- **EX023 — Erro de digitação no TLP.** Por que "AMBER STRICT" não deve ser mapeado automaticamente para AMBER? *Rubrica:* 3 = afrouxaria a restrição; perguntar ao remetente; 2 = parcial; 1 = inofensivo; 0 = nenhuma.
- **EX024 — Segurança na reexecução.** Como o importador deve evitar duplicatas quando roda duas vezes? *Rubrica:* 3 = chave por tipo+valor; atualizar em vez de inserir; 2 = remover duplicatas de forma vaga; 1 = apagar tudo antes; 0 = nenhuma.

### Síntese

Faça o parsing com código, valide de forma explícita, relate as rejeições e mantenha as importações idempotentes.

### Continue estudando — capítulo 08 de 40

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). O Halden County Health Trust, Amara Diallo, o Health Sector Sharing Circle e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Abdução — ela propõe a explicação mais plausível para uma observação sem prová-la.

**EX002.** Post hoc ergo propter hoc: supor que, porque um evento veio depois de outro, o primeiro causou o segundo.

**EX003.** Qual era o número de linha de base? Em que período a alta foi medida? Como os ataques foram contados — e as regras de notificação mudaram?

**EX004.** Os logs do resolvedor DNS; os logs do proxy web podem corroborar para o tráfego HTTP.

**EX005.** Os servidores de imagem são sistemas médicos certificados, com processo próprio de segurança e de mudança, e pertencem à engenharia clínica.

**EX006.** Se um serviço clínico legítimo compartilha o domínio ou depende dele, o bloqueio pode interromper o atendimento aos pacientes.

**EX007.** Um conjunto: `feed & seen` retorna os valores presentes nas duas coleções.

**EX008.** Exatamente 64 caracteres hexadecimais (0–9, a–f).

**EX009.** Rotulá-los como desconhecidos, mantê-los fora do repositório de indicadores e pedir ao remetente os valores completos.

**EX010.** Exemplo: "O abuso de contas válidas (T1078) é uma via recorrente nos relatórios fictícios do varejo (alegação); ele aparece em quatro de seis incidentes (evidência); como os atacantes usaram credenciais reais, os controles de perímetro não alertaram (raciocínio)."

**EX011.** Não. O TLP:AMBER limita o compartilhamento à organização destinatária; um ensaio público precisa se apoiar em fontes públicas ou em exemplos sintéticos.

**EX012.** A escrita de inteligência põe o julgamento principal primeiro; a escrita acadêmica costuma construir o argumento antes de concluir.

**EX013.** Tático — detalhe operacional para analistas que configuram filtros e fazem caçadas.

**EX014.** A direção; requisitos prioritários de inteligência escritos pelos tomadores de decisão a corrigem.

**EX015.** Os executivos decidem prioridades e investimentos; indicadores são detalhe tático que não ajuda nessa decisão.

**EX016.** A diferença HSSC menos HCHT: os elementos do conjunto do HSSC que não estão no conjunto da lista de bloqueio.

**EX017.** O endereço serve muitos sites sem relação entre si, então ligar por meio dele cria conexões falsas entre domínios sem operador comum.

**EX018.** Adversário, capacidade, infraestrutura e vítima (Caltagirone, Pendergast e Betz, 2013).

**EX019.** O titular do domínio sósia autorizou o servidor remetente, mas a mensagem não está alinhada com o domínio real do HCHT — um phishing clássico com domínio sósia.

**EX020.** Quase toda conexão de rede começa com uma consulta de nome, então os logs do resolvedor cobrem quase todos os dispositivos e aplicações.

**EX021.** Em geral, o endereço de destino e o nome do servidor, não o caminho da URL nem o conteúdo.

**EX022.** A linha de domínio datada de 2026-09-02 tinha o valor vazio; a linha de sha256 datada de 2026-09-03 tinha o tamanho errado. Três linhas foram aceitas.

**EX023.** O AMBER+STRICT limita o compartilhamento apenas à organização destinatária; mapeá-lo para AMBER permitiria um compartilhamento mais amplo do que a fonte pretendia.

**EX024.** Usar tipo mais valor como chave única e atualizar os metadados do registro existente em vez de inserir uma linha nova.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bianco, D. (2013). The Pyramid of Pain. <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
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
