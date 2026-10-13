# Governança, Riscos e Compliance de Segurança: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 097, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–28 de 40 já estão escritos em português, com os exercícios EX001–EX084 e suas resoluções com rubricas de 0 a 3 e 6 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 29–40 (EX085–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de bacharelado que aprendem a construir, operar e avaliar um programa de GRC proporcional numa organização pequena.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios consultam um registro de riscos em SQLite e calculam intervalos de Wilson, medianas de patch, níveis de fornecedores, ordenações de matriz contra perda esperada e um resumo de lacunas do CSF, sempre sobre dados sintéticos. Os números de risco são ilustrações, as normas são citadas pela edição e parafraseadas, e nada aqui é auditoria, atestação ou aconselhamento jurídico reais. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de bacharelado ao longo de quatro anos centrados no programa de GRC de uma associação de habitação social: fundamentos e dados, identidade e privacidade, escopo e teoria, modelos e fornecedores, métodos de risco e controles, laboratórios, verificação, análise de falhas e operações, pesquisa e um trabalho de conclusão que redesenha a revisão de acessos. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Sofia Reyes** | Estudante de bacharelado | Inventada |
| **Dr. Malik Haddad** | Tutor | Inventado |
| **Brightwater College** | Faculdade fictícia | Inventada |
| **Elmfield Housing Association** | Associação de habitação social fictícia, 300 funcionários, 4.000 moradias | Inventada |
| **Corbridge Community Trust** | Instituição beneficente fictícia, usada para comparação | Inventada |

### Fontes principais

ISO 31000:2018 (no Brasil, ABNT NBR ISO 31000:2018); ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) e 27002:2022; NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29), o [NIST Privacy Framework](https://doi.org/10.6028/NIST.CSWP.10) e o [SP 800-55v1](https://doi.org/10.6028/NIST.SP.800-55v1); COBIT 2019; PCI DSS v4.0; trust services criteria da AICPA; Cox (2008), [doi:10.1111/j.1539-6924.2008.01030.x](https://doi.org/10.1111/j.1539-6924.2008.01030.x); GAO-21-105263. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) |

Capítulos 29–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-29), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) usar proporções e taxas para descrever fatos de governança; (2) evitar erros comuns com porcentagens; (3) formular afirmações com precisão.

### 1.1 Números na governança

Sofia Reyes é estudante de bacharelado no fictício Brightwater College. Seu tutor, o Dr. Malik Haddad, usa um único caso ao longo do curso: a fictícia Elmfield Housing Association, uma associação de habitação social com trezentos funcionários e quatro mil moradias, que guarda dados pessoais dos inquilinos e recebe pagamentos de aluguel on-line. Os gestores da Elmfield costumam descrever a segurança com números: a maioria dos funcionários fez o treinamento, poucos notebooks estão sem criptografia. Sofia aprende a transformar essas frases em proporções precisas, com numerador e denominador declarados. "Poucos notebooks sem criptografia", por exemplo, vira nove de cento e vinte notebooks quando as duas contagens são conhecidas.

### 1.2 Armadilhas das porcentagens

Sofia estuda as armadilhas comuns. Passar de dois incidentes para quatro é um aumento de cem por cento, mas são só dois incidentes a mais. Uma queda de dez para cinco por cento de revisões vencidas é de cinco pontos percentuais, e não de cinco por cento. Uma proporção sem sua base pode enganar: noventa por cento dos notebooks criptografados significa pouco se o número de notebooks é desconhecido, ou se os dez por cento sem criptografia guardam justamente os dados mais sensíveis. Ela pratica reescrever afirmações enganosas como afirmações honestas, que mostram as contagens e as bases, para que qualquer leitor possa conferir o que está sendo dito.

### 1.3 Afirmações precisas

O Dr. Haddad pede à turma que escreva uma afirmação precisa sobre a Elmfield. Sofia escreve: em primeiro de outubro, duzentas e setenta de trezentas contas de funcionários tinham a autenticação multifator ativada, segundo o relatório do sistema de identidade. A afirmação nomeia a data, a contagem, a base e a fonte. Ela aprende que afirmações precisas podem ser conferidas e contestadas, e as vagas não, e por isso auditores e conselhos as preferem e a escrita de governança deve usá-las desde o início. O Dr. Haddad observa que o relatório do sistema de identidade aparece como fonte, então quem duvidar das duzentas e setenta contas pode executá-lo de novo.

### Exemplo resolvido

Sofia reescreve afirmações vagas como contagens datadas, com bases e fontes, e evita as armadilhas das porcentagens.

> **Caso sintético.** O Brightwater, a Elmfield e todos os números são sintéticos.

### Erros e limites

Números precisos ainda podem estar errados. As fontes podem estar desatualizadas.

### Exercícios

- **EX001 — Pontos ou porcentagem.** Uma queda de dez para cinco por cento é uma mudança de que tamanho? *Rubrica:* 3 = cinco pontos percentuais;; 2 = pontos;; 1 = cinco por cento;; 0 = nenhuma.
- **EX002 — Base ausente.** Por que um número de noventa por cento pode enganar? *Rubrica:* 3 = a base e quais itens faltam são desconhecidos;; 2 = base;; 1 = nada;; 0 = nenhuma.
- **EX003 — Partes da afirmação.** Que quatro partes a afirmação precisa de Sofia incluía? *Rubrica:* 3 = data, contagem, base e fonte;; 2 = quatro;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever os componentes da TI de uma organização; (2) montar um inventário de ativos simples; (3) entender por que os inventários vêm primeiro na governança.

### 2.1 Os sistemas da Elmfield

Sofia visita a Elmfield e lista seus sistemas computacionais: notebooks para o pessoal do escritório, tablets para os operários de manutenção, um servidor de arquivos, um sistema de gestão habitacional hospedado por um fornecedor, e-mail em nuvem, uma página de pagamento de aluguel operada por um provedor de pagamentos e um pequeno portal do conselho. Ela aprende que cada sistema tem hardware, software, dados e pessoas que o usam. Entender essas partes a ajuda a ver onde as coisas podem dar errado e quem precisaria agir. O portal do conselho, por exemplo, guarda os documentos do conselho, então uma falha ali exigiria um responsável capaz de decidir depressa.

### 2.2 O inventário

Sofia monta um inventário de ativos como uma tabela: nome do ativo, tipo, responsável, localização, dados guardados e fornecedor. Descobre que ninguém é responsável pelo portal do conselho e que onze tablets não constam da lista da equipe de manutenção. A ISO/IEC 27002:2022 traz orientações sobre inventários de informações e outros ativos associados, e o NIST CSF 2.0 coloca a gestão de ativos na função Identify. Ela aprende que um inventário não é papelada, mas o mapa do qual depende cada controle posterior. Os onze tablets ausentes importam porque os operários levam neles os endereços dos inquilinos para o campo.

### 2.3 Por que primeiro

O Dr. Haddad explica por que a governança começa pelo inventário. A avaliação de riscos precisa saber o que pode ser prejudicado. O controle de acesso precisa saber que sistemas controlar. A resposta a incidentes precisa saber o que restaurar. Sem inventário, cada uma delas adivinha. Sofia observa que os inventários se degradam quando os funcionários compram novos dispositivos ou adotam novos serviços, então o inventário precisa de responsável e data de revisão. Ela recomenda uma conferência trimestral contra os registros de compras e o sistema de identidade, que teria apanhado os onze tablets da manutenção antes de alguém sair procurando por eles.

### Exemplo resolvido

Sofia lista os sistemas da Elmfield, monta um inventário com responsáveis, encontra um portal sem responsável e tablets ausentes e planeja conferências trimestrais.

> **Caso sintético.** Os sistemas da Elmfield são sintéticos; a ISO/IEC 27002:2022 e o CSF 2.0 são reais.

### Erros e limites

Os inventários deixam escapar a shadow IT. Os responsáveis podem ser só nominais.

### Exercícios

- **EX004 — Campos do inventário.** Que campos o inventário de Sofia contém? *Rubrica:* 3 = nome, tipo, responsável, localização, dados guardados, fornecedor;; 2 = seis campos;; 1 = nada;; 0 = nenhuma.
- **EX005 — Lacunas do inventário.** Que duas lacunas o inventário revelou? *Rubrica:* 3 = portal do conselho sem responsável e onze tablets ausentes;; 2 = duas lacunas;; 1 = nada;; 0 = nenhuma.
- **EX006 — Conferência contra a degradação.** Como Sofia planeja manter o inventário atualizado? *Rubrica:* 3 = conferência trimestral contra compras e registros de identidade;; 2 = trimestral;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) ler dados de governança com programas simples; (2) contar e filtrar registros; (3) escrever saídas sobre as quais as pessoas possam agir.

### 3.1 Primeiro script

Sofia escreve seu primeiro programa em Python para ler o inventário da Elmfield de um arquivo CSV. Ele imprime quantos ativos existem e quantos não têm responsável. Ela aprende as estruturas básicas: listas para guardar registros, laços para visitar cada um e condições para testar os campos. A professora insiste que até uma contagem simples ajuda a governança, porque troca impressões por fatos. O script também roda sempre do mesmo jeito, ao contrário da contagem manual, que pode dar respostas diferentes em dias diferentes. Executado de novo depois da atribuição de responsáveis, o mesmo script mostra se o número de ativos sem responsável realmente caiu.

### 3.2 Filtrar

Em seguida, Sofia filtra o inventário para listar os ativos que guardam dados pessoais de inquilinos e não têm responsável. Aparecem dois: o portal do conselho, que guarda documentos do conselho com reclamações de inquilinos, e uma pasta num drive compartilhado. Ela imprime cada um com sua localização para que alguém possa dar seguimento. Aprende que filtrar pela combinação de sensibilidade e falta de responsável aponta aos gestores primeiro as lacunas mais urgentes, em vez de sobrecarregá-los com uma longa lista indiferenciada de problemas. O portal do conselho vem primeiro porque seus documentos contêm reclamações de inquilinos e ninguém responde por ele.

### 3.3 Saída acionável

O Dr. Haddad revisa a saída. Uma linha dizendo "dois problemas encontrados" não ajuda; uma linha que nomeia o ativo, o problema e um responsável sugerido, sim. Sofia reescreve a saída para incluir esses campos e a data da execução. Ela aprende a pensar na saída do programa como uma mensagem para um gestor ocupado: se a mensagem precisa de explicação, deve ser reescrita. Esse hábito vai importar ao longo de todo o curso, quando os scripts produzirem evidências de governança. Uma linha útil poderia dizer: portal do conselho, sem responsável, responsável sugerido o secretário da associação, executado na data indicada.

### Exemplo resolvido

Sofia conta os registros do inventário, filtra os ativos sensíveis sem responsável e reescreve a saída para nomear o ativo, o problema e o responsável sugerido.

> **Caso sintético.** O arquivo de inventário é sintético.

### Erros e limites

Os scripts confiam em sua entrada. Os responsáveis sugeridos precisam de confirmação.

### Exercícios

- **EX007 — Benefício do script.** Por que uma contagem feita por script ajuda a governança? *Rubrica:* 3 = troca impressões por fatos repetíveis;; 2 = fatos;; 1 = nada;; 0 = nenhuma.
- **EX008 — Combinação do filtro.** Por que combinação Sofia filtrou? *Rubrica:* 3 = dados pessoais de inquilinos e sem responsável;; 2 = sensível sem responsável;; 1 = nada;; 0 = nenhuma.
- **EX009 — Saída reescrita.** O que cada linha de saída passou a incluir? *Rubrica:* 3 = ativo, problema, responsável sugerido e data da execução;; 2 = campos;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) escrever um argumento curto com evidências; (2) citar normas e fontes corretamente; (3) parafrasear em vez de copiar.

### 4.1 Estrutura do argumento

O primeiro ensaio de Sofia pergunta se as organizações pequenas precisam de governança de segurança formal. Ela aprende a estruturar um argumento: uma tese clara, razões, evidências para cada razão, um contra-argumento e uma resposta. Sua tese é que mesmo as organizações pequenas precisam de uma governança básica, porque guardam dados sensíveis e enfrentam as mesmas ameaças que as grandes. Seu contra-argumento é que os frameworks formais custam caro demais para equipes pequenas. Sua resposta propõe uma governança proporcional ao porte e ao risco. Para a Elmfield, isso poderia significar um inventário com responsáveis e um registro de riscos curto, em vez de uma certificação completa.

### 4.2 Citar as fontes

Sofia cita o NIST CSF 2.0 e seus recursos para pequenas empresas, a ISO/IEC 27001:2022 e um artigo de Spears e Barki (2010) sobre a participação dos usuários na gestão de riscos de segurança. O Dr. Haddad a ensina a citar as normas com edição e ano, porque os requisitos mudam entre as edições, e a dar um DOI ou link oficial quando existir. Citar a ISO/IEC 27001:2022, e não uma edição anterior, importa porque a numeração dos controles mudou. Ele adverte que nunca se deve inventar referências ou identificadores, e que cada um deve ser conferido no registro da editora antes da entrega.

### 4.3 Paráfrase

As normas são protegidas por direitos autorais, e copiar trechos longos não é permitido. Sofia aprende a parafrasear com suas próprias palavras e citar a fonte, citando literalmente só expressões curtas quando a redação exata importa. Ela pratica resumindo a ideia de um plano de tratamento de riscos sem copiar nenhuma frase e sem a norma aberta à frente, o que mostra se consegue explicar as opções de tratamento com suas palavras. Parafrasear também testa a compreensão: se ela não consegue explicar uma ideia com simplicidade, ainda não a entendeu. O ensaio recebe boas notas pela estrutura clara e pela citação exata e honesta.

### Exemplo resolvido

Sofia estrutura um ensaio com tese, razões, contra-argumento e resposta, cita as fontes pela edição e parafraseia as normas.

> **Caso sintético.** O ensaio é sintético; o CSF 2.0, a ISO/IEC 27001:2022 e Spears e Barki (2010) são reais.

### Erros e limites

Ensaios curtos simplificam demais. As paráfrases podem distorcer o sentido.

### Exercícios

- **EX010 — Contra-argumento.** Que contra-argumento Sofia tratou? *Rubrica:* 3 = os frameworks formais custam caro demais para equipes pequenas;; 2 = custo;; 1 = nada;; 0 = nenhuma.
- **EX011 — Motivo da edição.** Por que citar as normas com edição e ano? *Rubrica:* 3 = os requisitos mudam entre as edições;; 2 = edições;; 1 = nada;; 0 = nenhuma.
- **EX012 — Teste da paráfrase.** Por que parafrasear testa a compreensão? *Rubrica:* 3 = quem não consegue explicar com simplicidade ainda não entendeu;; 2 = compreensão;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) explicar as ameaças básicas a uma organização pequena; (2) relacioná-las a controles do dia a dia; (3) comunicar segurança sem medo.

### 5.1 Ameaças comuns

Sofia aprende as ameaças que a Elmfield mais enfrenta: e-mails que enganam os funcionários para entregar senhas ou pagar faturas falsas, ransomware que criptografa arquivos, dispositivos perdidos, erros como enviar dados de inquilinos à pessoa errada e o mau uso de acessos por prestadores de serviço. Ela observa que a maioria dos incidentes em organizações pequenas vem de falhas comuns, e não de ataques sofisticados. Saber quais ameaças são comuns ajuda a Elmfield a concentrar recursos limitados onde evitarão mais danos. Para a Elmfield, uma fatura falsa paga ou dados enviados à pessoa errada são muito mais prováveis do que um ataque direcionado.

### 5.2 Controles do dia a dia

Para cada ameaça, ela lista controles do dia a dia. A autenticação multifator limita o dano de senhas roubadas. Backups mantidos offline permitem a recuperação de um ransomware. A criptografia protege os notebooks perdidos. Conferir os destinatários e usar links de compartilhamento seguros reduzem os e-mails mal endereçados. Contas nominais e com acesso limitado para os prestadores reduzem o mau uso. Ela aprende que as orientações de início rápido do NIST CSF 2.0 para pequenas empresas destacam o mesmo básico. Os controles não precisam ser complexos para funcionar, mas precisam ser aplicados de forma consistente: a autenticação multifator só ajuda se cobrir as trezentas contas.

### 5.3 Comunicar bem

Sofia prepara uma palestra curta para os agentes de habitação da Elmfield. Evita linguagem assustadora e culpa. Em vez disso, explica por que cada controle ajuda inquilinos e funcionários, dá instruções simples e convida a perguntas. Aprende que o medo pode causar breves surtos de cautela, mas muitas vezes leva a esconder erros. Incentivar os funcionários a relatar os erros depressa, como um e-mail mal endereçado, permite à Elmfield limitar o dano; quem relata em minutos pode permitir pedir ao destinatário que apague a mensagem antes de qualquer prejuízo. A boa comunicação é ela mesma um controle, porque molda o comportamento das pessoas quando algo dá errado.

### Exemplo resolvido

Sofia identifica as ameaças comuns da Elmfield, liga-as a controles do dia a dia e dá uma palestra sem culpa que incentiva o relato rápido.

> **Caso sintético.** As ameaças e a palestra são sintéticas; as orientações do CSF 2.0 são reais.

### Erros e limites

Controles simples falham se forem inconsistentes. O efeito das palestras dura pouco.

### Exercícios

- **EX013 — Causa comum.** De onde vem a maioria dos incidentes em organizações pequenas? *Rubrica:* 3 = de falhas comuns, não de ataques sofisticados;; 2 = comuns;; 1 = nada;; 0 = nenhuma.
- **EX014 — Controle contra ransomware.** Que controle permite a recuperação de um ransomware? *Rubrica:* 3 = backups offline;; 2 = backups;; 1 = nada;; 0 = nenhuma.
- **EX015 — Efeito do medo.** Por que evitar o medo nas palestras de segurança? *Rubrica:* 3 = leva a esconder erros;; 2 = esconder;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) representar papéis e permissões como conjuntos e relações; (2) encontrar conflitos de segregação de funções; (3) usar grafos para rastrear dependências.

### 6.1 Papéis como conjuntos

Sofia representa os papéis financeiros da Elmfield como conjuntos de permissões. O auxiliar de pagamentos pode lançar faturas de fornecedores e registrar pagamentos. A gerente financeira pode aprovar pagamentos e cadastrar novos fornecedores. Ela lista que funcionários têm que papéis e calcula as permissões combinadas de cada pessoa. Uma pessoa que cobre a ausência de uma colega tem os dois papéis, o que lhe permite cadastrar um fornecedor e aprovar pagamentos a ele. Os conjuntos tornam esse conflito visível na hora, sem depender de alguém notar. Aqui a origem do conflito é o arranjo de cobertura, e não a intenção de alguém.

### 6.2 Segregação de funções

A segregação de funções impede que uma pessoa conclua sozinha um processo sensível. Sofia escreve as regras como pares de permissões proibidos, como cadastrar fornecedor com aprovar pagamento. Ela confere o conjunto de permissões de cada pessoa contra as regras e encontra o único conflito. Recomenda que os arranjos de cobertura usem acesso temporário, com um segundo aprovador e data de término. Aprende que essa lógica simples está por trás de muitos controles antifraude e pode ser conferida automaticamente todo mês; uma conferência mensal automática também apanharia um arranjo de cobertura que deveria ter terminado e nunca terminou.

### 6.3 Grafos de dependência

Sofia desenha um grafo em que os nós são sistemas e as arestas mostram dependências. O sistema de gestão habitacional depende da identidade em nuvem, que depende do e-mail. Se a identidade em nuvem falhar, os funcionários não alcançam os registros habitacionais. O grafo mostra que a identidade é um ponto único de falha para a maioria dos serviços. Ela aprende que os grafos revelam concentrações ocultas de risco que os inventários sozinhos não mostram, e que o planejamento de resiliência deve focar os nós com muitos dependentes. O Dr. Haddad sugere conferir como os funcionários chegariam aos registros habitacionais se a identidade em nuvem caísse.

### Exemplo resolvido

Sofia encontra um conflito de segregação de funções por operações de conjuntos e identifica com um grafo a identidade em nuvem como ponto único de falha.

> **Caso sintético.** Os papéis, os funcionários e os sistemas são sintéticos.

### Erros e limites

Os dados de permissões podem estar incompletos. Os grafos deixam escapar dependências informais.

### Exercícios

- **EX016 — Conflito encontrado.** Que conflito Sofia encontrou? *Rubrica:* 3 = uma pessoa podia cadastrar um fornecedor e aprovar pagamentos a ele;; 2 = SoD;; 1 = nada;; 0 = nenhuma.
- **EX017 — Correção da cobertura.** Como devem funcionar os arranjos de cobertura? *Rubrica:* 3 = acesso temporário com segundo aprovador e data de término;; 2 = temporário;; 1 = nada;; 0 = nenhuma.
- **EX018 — Ponto único.** Que sistema é um ponto único de falha? *Rubrica:* 3 = a identidade em nuvem;; 2 = identidade;; 1 = e-mail;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) descrever a rede da Elmfield e suas conexões externas; (2) identificar onde os dados saem da organização; (3) relacionar o desenho da rede ao risco.

### 7.1 A rede

A rede do escritório da Elmfield liga os notebooks e o servidor de arquivos, com acesso à internet por um firewall. A maioria dos serviços agora roda na nuvem, alcançada pela internet. Os tablets da manutenção se conectam por redes móveis e nunca passam pelo firewall do escritório. Sofia aprende que a velha ideia de uma rede interna confiável já não serve, porque os funcionários e os dados estão espalhados por muitos lugares. A governança precisa, portanto, focar a identidade, os dispositivos e a proteção dos dados onde quer que estejam, e não só o firewall do escritório, que cobre uma parte cada vez menor do trabalho.

### 7.2 Dados que saem

Sofia rastreia por onde os dados dos inquilinos saem da Elmfield: e-mail para prestadores, os servidores do fornecedor do sistema habitacional, o provedor de pagamentos e o escritório de folha de pagamento. Cada fluxo precisa de um motivo, um contrato e proteção em trânsito. Ela descobre que os prestadores de manutenção recebem os registros completos dos inquilinos quando precisam só de nome, endereço e telefone. Recomenda enviar só os campos necessários, aplicando o princípio da minimização de dados, o que reduz o dano se os sistemas de um prestador forem comprometidos e diminui o que a Elmfield teria de comunicar nesse caso.

### 7.3 Risco de rede

Sofia lista os riscos de rede: um serviço de área de trabalho remota exposto no servidor de arquivos, uma rede Wi-Fi de visitantes que compartilha a rede do escritório e a falta de logs no firewall. Ela os ordena pelo dano potencial e pela facilidade de correção. Fechar a exposição da área de trabalho remota fica em primeiro, porque os atacantes fazem varreduras rotineiras em busca dela. O Wi-Fi de visitantes e os logs do firewall vêm depois, baratos de corrigir, mas menos prováveis de serem explorados primeiro. Ela aprende que pequenas correções podem eliminar grandes riscos e que uma revisão de rede é um modo rápido de uma organização pequena achar problemas sérios.

### Exemplo resolvido

Sofia mapeia a rede e os fluxos de dados da Elmfield, aplica a minimização aos dados dos prestadores e ordena três riscos de rede.

> **Caso sintético.** A rede da Elmfield é sintética.

### Erros e limites

Os fluxos de dados mudam. As ordenações dependem de julgamento.

### Exercícios

- **EX019 — Rede confiável.** Por que a ideia de rede interna confiável já não serve? *Rubrica:* 3 = funcionários e dados estão espalhados por muitos lugares;; 2 = nuvem e mobilidade;; 1 = nada;; 0 = nenhuma.
- **EX020 — Correção por minimização.** O que os prestadores devem receber em vez dos registros completos? *Rubrica:* 3 = só nome, endereço e telefone;; 2 = campos mínimos;; 1 = registros completos;; 0 = nenhuma.
- **EX021 — Maior risco de rede.** Que risco de rede ficou em primeiro? *Rubrica:* 3 = área de trabalho remota exposta no servidor de arquivos;; 2 = RDP;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar scripts de governança em funções com testes; (2) ler várias fontes de dados; (3) cruzar as fontes para encontrar divergências.

### 8.1 Funções e testes

Sofia reestrutura os scripts em funções, cada uma com uma tarefa: ler um arquivo, conferir uma regra ou imprimir um relatório. Ela escreve pequenos testes com respostas conhecidas. Por exemplo, um teste entrega à verificação de responsável um registro com o responsável vazio e espera que ele seja sinalizado; se uma mudança posterior quebrar a verificação, o teste falha na hora. Os testes apanham erros quando ela altera o código depois. Ela aprende que os scripts de governança precisam de testes porque sua saída pode ser usada como evidência, e evidência errada pode enganar gestores e auditores.

### 8.2 Várias fontes

As verificações reais combinam fontes. Sofia lê o inventário, a exportação de contas do sistema de identidade e a lista de desligamentos de recursos humanos. Cada uma usa nomes diferentes para a mesma coisa: o sistema de identidade usa endereços de e-mail, e o RH usa números de matrícula. Ela escreve uma tabela de correspondência para juntá-las. Aprende que boa parte do trabalho de governança é conciliar fontes que nunca foram feitas para bater, e que documentar a correspondência é essencial para que outros repitam a verificação. A própria tabela, que liga matrículas a e-mails, é evidência e deve ser guardada com os resultados.

### 8.3 Divergências

O cruzamento revela divergências: quatro contas pertencem a funcionários da lista de desligamentos, dois notebooks do inventário estão atribuídos a desligados e uma conta ativa não corresponde a nenhum funcionário. Sofia imprime cada divergência com os detalhes das duas fontes. O Dr. Haddad observa que as divergências são onde o risco se esconde, porque cada sistema parece correto sozinho. A conciliação transforma registros separados num único quadro, que é a base das revisões de acesso e das auditorias de ativos. A conta ativa sem funcionário correspondente é a mais urgente, porque ninguém sabe dizer quem a usa.

### Exemplo resolvido

Sofia escreve funções testadas, junta três fontes com uma tabela de correspondência e encontra contas e notebooks de desligados e uma conta órfã.

> **Caso sintético.** As fontes e as divergências são sintéticas.

### Erros e limites

Erros de correspondência geram falsos alarmes. As fontes podem compartilhar o mesmo erro.

### Exercícios

- **EX022 — Propósito dos testes.** Por que os scripts de governança precisam de testes? *Rubrica:* 3 = sua saída pode ser usada como evidência;; 2 = evidência;; 1 = nada;; 0 = nenhuma.
- **EX023 — Problema da junção.** Por que Sofia precisou de uma tabela de correspondência? *Rubrica:* 3 = as fontes usam identificadores diferentes;; 2 = identificadores;; 1 = nada;; 0 = nenhuma.
- **EX024 — Conta órfã.** O que é uma conta órfã nesta verificação? *Rubrica:* 3 = uma conta ativa que não corresponde a nenhum funcionário;; 2 = órfã;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) guardar um registro de riscos num banco de dados; (2) consultá-lo em busca de prioridades e lacunas; (3) entender por que a estrutura melhora os dados de governança.

### 9.1 O registro num banco de dados

O registro de riscos da Elmfield é uma planilha com células mescladas e texto livre. Sofia leva uma amostra de seis riscos para um pequeno banco SQLite com colunas definidas: identificador, título, responsável, probabilidade de um a cinco e impacto de um a cinco. Colunas definidas permitem consultas que seriam lentas e sujeitas a erro se feitas à mão. Ela aprende que a estrutura é o que transforma um registro de documento em dados capazes de responder a perguntas. Células mescladas e texto livre, por exemplo, impedem ordenar os riscos pela nota ou listar os que não têm responsável.

### 9.2 Consultas

O laboratório executa duas consultas. A primeira ordena os riscos pela nota, probabilidade vezes impacto. Dados de inquilinos enviados por e-mail à pessoa errada e um notebook perdido com anotações de casos empatam em doze, seguidos de ransomware no servidor de arquivos, com dez. A segunda lista os riscos sem responsável: o de mau uso da conta do prestador de manutenção e o de senhas fracas no portal do conselho. Sofia observa que os empates mostram os limites de uma escala de cinco pontos, incapaz de separar riscos que podem diferir muito nas consequências reais. Os dois riscos sem responsável são uma lacuna de governança mais clara do que o empate, porque ninguém vai agir sobre eles.

### Laboratório — Consultas a um registro de riscos sintético

```python
"""A synthetic Elmfield risk register in SQLite: top risks and unowned entries."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table risk(id text, title text, owner text, likelihood int, impact int)")
db.executemany("insert into risk values (?,?,?,?,?)", [
    ("R1", "tenant data emailed to wrong person", "Housing", 4, 3), ("R2", "ransomware on file server", "IT", 2, 5),
    ("R3", "repairs contractor account misuse", None, 3, 3), ("R4", "rent payment page outage", "Finance", 3, 2),
    ("R5", "lost laptop with case notes", "Housing", 3, 4), ("R6", "weak passwords on board portal", None, 2, 2)])
for row in db.execute("select id, title, likelihood*impact s from risk order by s desc limit 3"):
    print("top", *row)
print("unowned:", [r[0] for r in db.execute("select id from risk where owner is null")])
```

Execute com `python3 lab_sqlite.py`. Saída verificada:

```text
top R1 tenant data emailed to wrong person 12
top R5 lost laptop with case notes 12
top R2 ransomware on file server 10
unowned: ['R3', 'R6']
```

### 9.3 Por que a estrutura ajuda

Com dados estruturados, a Elmfield pode acompanhar como as notas mudam ao longo do tempo, conferir se todo risco tem responsável e produzir automaticamente os relatórios para o conselho. Sofia também acrescenta uma restrição para que probabilidade e impacto fiquem entre um e cinco, evitando erros de digitação; uma probabilidade 33 digitada por engano não vai mais parar silenciosamente no topo da lista. O Dr. Haddad observa que os bancos de dados não melhoram sozinhos os julgamentos de risco, mas os tornam visíveis, consistentes e fáceis de revisar, o que melhora a governança ao expor as lacunas.

### Exemplo resolvido

Sofia carrega seis riscos no SQLite, encontra dois empatados em doze e dois riscos sem responsável e acrescenta restrições de faixa.

> **Caso sintético.** O registro é sintético.

### Erros e limites

Dados estruturados ainda podem conter julgamentos ruins. As escalas causam empates.

### Exercícios

- **EX025 — Fórmula da nota.** Como a nota de risco é calculada? *Rubrica:* 3 = probabilidade vezes impacto;; 2 = produto;; 1 = soma;; 0 = nenhuma.
- **EX026 — Riscos empatados.** Que dois riscos empataram no topo? *Rubrica:* 3 = dados de inquilinos mal endereçados e notebook perdido, ambos 12;; 2 = empate;; 1 = ransomware;; 0 = nenhuma.
- **EX027 — Lista sem responsável.** Que riscos não tinham responsável? *Rubrica:* 3 = R3 mau uso pelo prestador e R6 senhas do portal do conselho;; 2 = dois;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) trabalhar só dentro do escopo autorizado; (2) tratar com ética os dados pessoais durante o trabalho de governança; (3) relatar os achados com responsabilidade.

### 10.1 Autorização

O trabalho de Sofia na Elmfield precisa de autorização por escrito. O Dr. Haddad explica que mesmo verificações bem-intencionadas, como testar se uma senha é fraca, podem violar regras ou leis se feitas sem permissão. A diretora da Elmfield assina uma carta que define o que Sofia pode fazer: ler exportações do inventário e das contas, entrevistar funcionários e revisar documentos. Os testes ativos em sistemas ficam excluídos. Ela aprende que um escopo claro a protege, assim como a organização e as pessoas cujos dados ela pode ver. A carta também avisa os funcionários do que esperar, para que um pedido de entrevista não pareça uma investigação.

### 10.2 Dados pessoais

As exportações de contas e as listas de desligamentos contêm dados pessoais. Sofia as guarda só no notebook criptografado que a Elmfield lhe forneceu para o estágio, remove os nomes ao compartilhar resultados com o tutor e apaga as cópias no fim. Ela aprende que o trabalho de governança precisa seguir os mesmos princípios de proteção de dados que promove: usar o mínimo de dados necessário, mantê-los seguros e guardá-los só pelo tempo preciso. Remover os nomes antes de compartilhar é a minimização aplicada ao próprio trabalho. Fazer diferente minaria sua credibilidade e poderia prejudicar inquilinos e funcionários.

### 10.3 Relato responsável

Quando encontra o serviço de área de trabalho remota exposto, Sofia o relata imediatamente ao líder de TI da Elmfield, em vez de esperar pelo relatório final, porque os atacantes poderiam explorá-lo a qualquer momento. Ela o descreve de forma factual, sem culpar quem o configurou. Relatar em particular, e não numa reunião, também evita chamar atenção para a exposição antes que seja fechada. Ela aprende que os achados urgentes exigem relato rápido e reservado pelos canais combinados, enquanto os riscos menores podem esperar o relatório escrito. O relato responsável equilibra rapidez, exatidão e respeito pelos colegas.

### Exemplo resolvido

Sofia trabalha sob um escopo assinado, protege os dados pessoais no próprio trabalho e relata um achado urgente prontamente e sem culpar ninguém.

> **Caso sintético.** A carta de escopo e os achados são sintéticos.

### Erros e limites

Os escopos podem ser ambíguos. Os julgamentos de urgência variam.

### Exercícios

- **EX028 — Atividade excluída.** Que atividade ficou fora do escopo de Sofia? *Rubrica:* 3 = testes ativos em sistemas;; 2 = testes;; 1 = nada;; 0 = nenhuma.
- **EX029 — Tratamento dos dados.** Como Sofia tratou os dados pessoais das exportações? *Rubrica:* 3 = notebook criptografado, nomes removidos ao compartilhar, apagados no fim;; 2 = minimizar;; 1 = nada;; 0 = nenhuma.
- **EX030 — Relato urgente.** Por que relatar imediatamente a exposição da área de trabalho remota? *Rubrica:* 3 = os atacantes poderiam explorá-la a qualquer momento;; 2 = urgência;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) relacionar as configurações do sistema operacional à política; (2) conferir os notebooks contra um baseline simples; (3) planejar as atualizações como um processo governado.

### 11.1 Configurações e política

A política da Elmfield diz que os notebooks precisam ser criptografados, bloquear a tela depois de alguns minutos ociosos, receber atualizações automaticamente e não dar direitos de administrador aos funcionários. Sofia aprende que cada afirmação corresponde a configurações do sistema operacional. A criptografia é uma configuração do disco, o bloqueio de tela é uma configuração de energia e segurança, as atualizações são geridas pelo serviço de atualização e os direitos de administrador dependem da participação em grupos, que pode ser lida em cada notebook. Ligar as afirmações da política às configurações é o que torna uma política aplicável e conferível, e não um desejo.

### 11.2 Conferência do baseline

Sofia usa o console de gestão de dispositivos para exportar as configurações de cento e vinte notebooks e as compara com o baseline da política. A maioria está conforme, mas nove não têm criptografia, todos notebooks da equipe de manutenção comprados localmente, e catorze usuários ainda têm direitos de administrador concedidos por causa de softwares antigos. Ela lista cada um com seu responsável. Aprende que as conferências de baseline revelam não só lacunas técnicas, mas lacunas de processo, como dispositivos comprados fora do caminho normal. O Dr. Haddad pergunta à turma quem deveria responder pela correção desses nove notebooks.

### 11.3 Atualizações como processo

As atualizações corrigem vulnerabilidades, mas podem quebrar softwares. A Elmfield precisa de um processo governado: testar as atualizações em poucos dispositivos, implantá-las em todos dentro de um prazo definido e acompanhar as exceções. Sofia redige o processo com o líder de TI, fixando trinta dias para as atualizações críticas, meta que ela vai medir no capítulo 15. Ela aprende que a política de atualização é um equilíbrio entre rapidez e estabilidade, e que escrever a meta e medir contra ela permite à Elmfield ver se a prática corresponde à intenção, em vez de apenas supor que corresponde.

### Exemplo resolvido

Sofia liga a política às configurações, encontra nove notebooks sem criptografia e catorze administradores e redige um processo de atualização.

> **Caso sintético.** As contagens de notebooks são sintéticas.

### Erros e limites

As exportações do console deixam de fora os dispositivos não gerenciados. As metas de atualização precisam de exceções.

### Exercícios

- **EX031 — Da política à configuração.** Que configuração impõe a regra de não haver administradores? *Rubrica:* 3 = participação em grupos;; 2 = grupos;; 1 = nada;; 0 = nenhuma.
- **EX032 — Causa raiz.** Por que nove notebooks não tinham criptografia? *Rubrica:* 3 = foram comprados localmente fora do caminho normal;; 2 = compras;; 1 = nada;; 0 = nenhuma.
- **EX033 — Meta de atualização.** Que meta Sofia fixou para as atualizações críticas? *Rubrica:* 3 = trinta dias;; 2 = 30;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar uma proporção com um intervalo; (2) comparar equipes de forma justa apesar dos tamanhos diferentes; (3) evitar ler demais em amostras pequenas.

### 12.1 Proporções com intervalos

A Elmfield pede a cada equipe que confirme ciência da política atualizada de tratamento de informações. Sofia aprende que uma proporção vinda de uma amostra ou de uma equipe pequena deve vir com um intervalo que mostre a incerteza. Ela usa o intervalo de Wilson, que se comporta bem com contagens pequenas e proporções próximas de zero ou de um. O intervalo mostra aos gestores a faixa de valores compatível com os dados, o que é mais honesto do que uma porcentagem única e ajuda a evitar decisões baseadas em diferenças casuais. Para uma equipe de quinze pessoas, o intervalo será muito mais largo do que para uma de sessenta.

### 12.2 Comparar equipes

O laboratório calcula as taxas de ciência. Habitação tem cinquenta e dois de sessenta, oitenta e sete por cento, com intervalo de setenta e seis a noventa e três por cento. Manutenção tem dezoito de trinta, sessenta por cento, com intervalo de quarenta e dois a setenta e cinco. Finanças tem catorze de quinze, noventa e três por cento, mas seu intervalo vai de setenta a noventa e nove, porque a equipe é pequena. A manutenção está claramente abaixo da habitação, já que os intervalos mal se tocam. Finanças e habitação não podem ser distinguidas, e relatar os intervalos impede apresentar os noventa e três por cento de finanças como melhores.

### Laboratório — Intervalos de Wilson para a ciência da política

```python
"""Wilson 95% interval for a proportion (policy acknowledgement), stdlib only."""
from math import sqrt
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n; c = (p + z*z/(2*n))/d; h = z*sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c-h, c+h
for team, k, n in [("housing", 52, 60), ("repairs", 18, 30), ("finance", 14, 15)]:
    lo, hi = wilson(k, n); print(f"{team}: {k}/{n} = {k/n:.0%}, 95% interval {lo:.0%} to {hi:.0%}")
```

Execute com `python3 lab_wilson.py`. Saída verificada:

```text
housing: 52/60 = 87%, 95% interval 76% to 93%
repairs: 18/30 = 60%, 95% interval 42% to 75%
finance: 14/15 = 93%, 95% interval 70% to 99%
```

### 12.3 Amostras pequenas

Sofia observa que a porcentagem alta de finanças impressiona, mas se apoia em quinze pessoas; uma confirmação a mais ou a menos a moveria vários pontos. Ela recomenda que a Elmfield concentre o apoio na manutenção, onde a lacuna é clara, e pergunta por que os funcionários da manutenção acham a confirmação mais difícil. Descobre que eles raramente usam notebooks e que a política foi enviada por e-mail. A estatística revelou a lacuna; conversar com as pessoas revelou a causa e uma correção simples: confirmar a ciência em tablets durante as reuniões de equipe, o que se encaixa no modo como a manutenção já trabalha.

### Exemplo resolvido

Sofia calcula intervalos de Wilson, constata que a manutenção está claramente abaixo da habitação e rastreia a causa até o envio por e-mail.

> **Caso sintético.** As contagens de ciência são sintéticas.

### Erros e limites

Confirmar ciência não significa entender. Os intervalos supõem independência.

### Exercícios

- **EX034 — Motivo do Wilson.** Por que usar o intervalo de Wilson? *Rubrica:* 3 = comporta-se bem com contagens pequenas e proporções extremas;; 2 = amostras pequenas;; 1 = nada;; 0 = nenhuma.
- **EX035 — Intervalo da manutenção.** Qual é o intervalo da equipe de manutenção? *Rubrica:* 3 = 42% a 75%;; 2 = largo;; 1 = nada;; 0 = nenhuma.
- **EX036 — Causa na manutenção.** Por que a equipe de manutenção confirmou menos? *Rubrica:* 3 = raramente usa notebooks e a política chegou por e-mail;; 2 = canal;; 1 = nada;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) gerir as identidades na admissão, na movimentação e no desligamento; (2) aplicar o menor privilégio; (3) conduzir uma revisão de acessos simples.

### 13.1 Ciclo de vida

Sofia mapeia o ciclo de vida das identidades na Elmfield. O RH avisa a TI quando alguém entra, e as contas são criadas. Quando os funcionários mudam de equipe, pedem novos acessos, mas raramente perdem os antigos. Quando saem, as contas deveriam ser desativadas no último dia, mas a lista de desligamentos chega atrasada à TI. Ela encontra quatro contas ativas de desligados. Propõe que o RH envie os avisos de desligamento automaticamente antes do último dia e que a TI confirme cada desativação num ticket. Os acessos antigos de quem mudou de equipe são outra lacuna, que a revisão de acessos da seção 13.3 foi pensada para apanhar.

### 13.2 Menor privilégio

Menor privilégio significa que cada pessoa tem só os acessos de que seu papel precisa. Sofia revisa o sistema de gestão habitacional e descobre que todos os agentes de habitação veem o registro completo de qualquer inquilino, incluindo necessidades de apoio e anotações de proteção (safeguarding). Só a equipe especializada de apoio precisa dessas anotações. Ela recomenda acesso baseado em papéis que restrinja os campos sensíveis. A ISO/IEC 27002:2022 traz orientações sobre controle de acesso e direitos de acesso que apoiam isso, e os inquilinos, cuja situação pode expô-los a riscos se for vista amplamente, têm forte interesse nessa restrição.

### 13.3 Revisão de acessos

Sofia conduz a primeira revisão de acessos da Elmfield, no sistema financeiro. Envia a cada gestor uma lista dos acessos de sua equipe e pede que confirme ou remova cada item. A maioria responde em uma semana; dois precisam de lembretes. Sete direitos de acesso são removidos. Ela registra a data, o revisor e as mudanças como evidência. Aprende que as revisões funcionam melhor quando as listas são curtas, claras e enviadas a quem realmente sabe o que sua equipe faz. Os sete direitos removidos mostram que os acessos tinham se acumulado com o tempo, e por isso a revisão deve ser repetida regularmente.

### Exemplo resolvido

Sofia corrige o processo de desligamento, restringe por papel as anotações sensíveis dos inquilinos e conduz uma revisão de acessos financeiros que remove sete direitos.

> **Caso sintético.** As contas e as revisões são sintéticas; a ISO/IEC 27002:2022 é real.

### Erros e limites

Os gestores podem aprovar sem conferir. O desenho de papéis leva tempo.

### Exercícios

- **EX037 — Correção do desligamento.** Como Sofia corrigiu os avisos de desligamento atrasados? *Rubrica:* 3 = avisos automáticos do RH antes do último dia, com confirmação em ticket;; 2 = automação;; 1 = nada;; 0 = nenhuma.
- **EX038 — Campos sensíveis.** Quem deve ver as anotações de proteção? *Rubrica:* 3 = só a equipe especializada de apoio;; 2 = equipe de apoio;; 1 = todos os agentes;; 0 = nenhuma.
- **EX039 — Resultado da revisão.** Quantos direitos de acesso a revisão removeu? *Rubrica:* 3 = sete;; 2 = 7;; 1 = nada;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem

Você vai (1) aplicar os princípios de proteção de dados aos dados dos inquilinos; (2) mapear o tratamento de dados pessoais; (3) ligar a governança de privacidade à de segurança.

### 14.1 Princípios

Sofia estuda os princípios de proteção de dados comuns às leis de privacidade modernas: tratamento lícito e leal, limitação da finalidade, minimização, exatidão, limitação da conservação, segurança e responsabilização. Ela os aplica à Elmfield. Os dados dos inquilinos são coletados para gerir locações e manutenções, então usá-los para marketing sem relação violaria a limitação da finalidade. Guardar por décadas os registros de antigos inquilinos viola a limitação da conservação. Ela observa que esses princípios se sobrepõem à segurança, mas também cobrem a lealdade e os direitos das pessoas; a lealdade não tem um controle de segurança direto e precisa de atenção própria.

### 14.2 Mapa do tratamento

Sofia monta um registro das atividades de tratamento: que dados pessoais a Elmfield tem, por quê, de onde vêm, quem os recebe e por quanto tempo são guardados. Descobre que os prestadores de manutenção recebem dados demais, que as necessidades de apoio ficam guardadas em dois sistemas e que ninguém sabe por quanto tempo as gravações de chamadas são mantidas, uma lacuna de conservação que precisa de uma decisão de retenção e de um responsável. O NIST Privacy Framework oferece uma estrutura para gerir o risco de privacidade, que ela usa para organizar esses achados ao lado dos de segurança.

### 14.3 Juntar privacidade e segurança

Sofia recomenda que a Elmfield conduza juntas a governança de privacidade e a de segurança, com um único registro de riscos e responsáveis compartilhados. Um e-mail mal endereçado é ao mesmo tempo um incidente de segurança e uma violação de dados pessoais que pode precisar ser comunicada. As regras de retenção reduzem os dados que um atacante poderia roubar. Ela aprende que privacidade e segurança são distintas, mas fortemente ligadas, e que programas separados muitas vezes duplicam esforços e deixam escapar os riscos que ficam entre eles, como o compartilhamento excessivo de dados com prestadores, encontrado tanto no trabalho de rede quanto no de privacidade.

### Exemplo resolvido

Sofia aplica os princípios de privacidade, mapeia o tratamento com três lacunas e recomenda uma governança conjunta de privacidade e segurança.

> **Caso sintético.** O tratamento de dados da Elmfield é sintético; o NIST Privacy Framework é real.

### Erros e limites

As leis variam de país para país. Os mapeamentos ficam desatualizados.

### Exercícios

- **EX040 — Violação de finalidade.** Que uso dos dados dos inquilinos violaria a limitação da finalidade? *Rubrica:* 3 = marketing sem relação;; 2 = marketing;; 1 = manutenção;; 0 = nenhuma.
- **EX041 — Lacunas do tratamento.** Cite duas lacunas encontradas no mapa do tratamento. *Rubrica:* 3 = dados demais para prestadores e retenção das gravações desconhecida;; 2 = lacunas;; 1 = nada;; 0 = nenhuma.
- **EX042 — Exemplo conjunto.** Por que um e-mail mal endereçado é assunto de segurança e de privacidade? *Rubrica:* 3 = é incidente de segurança e violação de dados pessoais;; 2 = ambos;; 1 = nada;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher medidas que reflitam o desempenho dos controles; (2) usar medianas e limiares para dados assimétricos; (3) apresentar as medidas com honestidade.

### 15.1 Escolher as medidas

A Elmfield quer saber se seu processo de atualização funciona. Sofia escolhe duas medidas: a mediana de dias para aplicar as atualizações críticas e a proporção aplicada dentro da meta de trinta dias. Ela aprende que as medidas devem se relacionar ao propósito do controle, que é encurtar o tempo em que as vulnerabilidades ficam abertas. Contar as atualizações instaladas seria uma medida de atividade; o tempo até a instalação é uma medida de desempenho, mais próxima do que importa para o risco. Dez de quinze atualizações em até trinta dias é um número de desempenho; quinze atualizações instaladas mostraria só atividade.

### 15.2 Dados assimétricos

O laboratório examina quinze atualizações críticas. A mediana é de vinte e um dias, e dez de quinze, sessenta e sete por cento, foram aplicadas em até trinta dias. As três mais lentas levaram quarenta e oito, sessenta e dois e noventa dias. Sofia observa que a média seria puxada para cima por esses atrasos longos, então a mediana descreve melhor uma atualização típica, enquanto os casos mais lentos merecem atenção separada. A maioria das atualizações lentas afetava o servidor de arquivos, que os funcionários evitam reiniciar no horário de trabalho, um padrão que liga os números a uma causa que uma janela de manutenção pode resolver.

### Laboratório — Dias até o patch: mediana e proporção dentro da meta

```python
"""Days to patch for 15 synthetic critical updates: median and share within 30 days."""
from statistics import median
days = [3, 5, 7, 8, 12, 14, 15, 21, 25, 29, 33, 41, 48, 62, 90]
print(f"updates {len(days)}; median {median(days)} days")
w = sum(d <= 30 for d in days); print(f"within 30 days {w}/{len(days)} = {w/len(days):.0%}")
print(f"slowest three {days[-3:]}")
```

Execute com `python3 lab_patch.py`. Saída verificada:

```text
updates 15; median 21 days
within 30 days 10/15 = 67%
slowest three [48, 62, 90]
```

### 15.3 Apresentação honesta

Sofia apresenta as duas medidas com a lista das atualizações lentas e sua causa. Evita dizer que a maioria das atualizações está no prazo sem acrescentar que um terço não está. Recomenda uma janela mensal de manutenção para o servidor de arquivos. O Dr. Haddad observa que o NIST SP 800-55v1 discute a seleção e o uso de medidas de segurança da informação, e que boas medidas provocam decisões em vez de enfeitar relatórios; a medida de Sofia leva diretamente à decisão da janela de manutenção. Mostrar as atualizações lentas pelo nome permite ao líder de TI agir sobre o servidor, e não sobre os notebooks em geral.

### Exemplo resolvido

Sofia mede uma mediana de vinte e um dias, com sessenta e sete por cento dentro da meta, e rastreia as atualizações lentas até o servidor de arquivos.

> **Caso sintético.** Os dados de atualização são sintéticos; o NIST SP 800-55v1 é real.

### Erros e limites

Amostras pequenas variam. As medianas escondem os casos mais lentos.

### Exercícios

- **EX043 — Medida de desempenho.** Por que o tempo até a instalação é melhor medida do que as atualizações instaladas? *Rubrica:* 3 = relaciona-se a quanto tempo as vulnerabilidades ficam abertas;; 2 = desempenho;; 1 = atividade;; 0 = nenhuma.
- **EX044 — Resultados de patch.** Que mediana e que proporção na meta o laboratório relatou? *Rubrica:* 3 = 21 dias, 67%;; 2 = mediana 21;; 1 = nada;; 0 = nenhuma.
- **EX045 — Causa da lentidão.** Por que as atualizações mais lentas atrasaram? *Rubrica:* 3 = o servidor de arquivos não era reiniciado no horário de trabalho;; 2 = servidor;; 1 = nada;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever uma arquitetura de segurança simples para uma organização pequena; (2) aplicar a defesa em camadas; (3) documentar as escolhas de projeto.

### 16.1 Uma arquitetura simples

Sofia esboça a arquitetura-alvo da Elmfield. A identidade é central: todos os funcionários entram uma única vez, com autenticação multifator, para chegar ao e-mail em nuvem, ao sistema habitacional e aos arquivos. Os dispositivos são gerenciados e criptografados. Os dados sensíveis ficam em poucos lugares bem controlados. Os backups ficam separados e são testados. A rede do escritório deixa de ser confiável por padrão. Cada elemento responde a uma lacuna encontrada antes, como os notebooks sem criptografia e a área de trabalho remota exposta. Ela aprende que organizações pequenas podem alcançar uma segurança forte com poucas decisões de projeto bem escolhidas, em vez de muitas ferramentas complexas.

### 16.2 Camadas

Sofia aplica a defesa em camadas ao ransomware. A filtragem de e-mail bloqueia muitas mensagens maliciosas. A autenticação multifator limita as senhas roubadas. Os controles de dispositivo bloqueiam programas desconhecidos. Os direitos de administrador limitados reduzem a propagação. Os backups offline permitem a recuperação. Nenhuma camada é perfeita, mas juntas reduzem a chance de uma única falha causar um desastre. Ela observa que camadas com uma fraqueza em comum, como uma única conta de administrador que controla todas, enfraqueceriam muito essa proteção. O Dr. Haddad pergunta que camada falhou num caso real estudado pela turma, para mostrar que o backup offline muitas vezes foi a última a resistir.

### 16.3 Documentar as escolhas

Sofia escreve notas curtas de decisão para cada escolha importante: por que a identidade em nuvem foi escolhida, por que o servidor de arquivos vai migrar para um serviço em nuvem e por que os backups continuam offline. Cada nota registra as alternativas e os riscos aceitos; a dos backups, por exemplo, registra que um backup só em nuvem foi considerado e rejeitado porque o ransomware poderia alcançá-lo. Ela aprende que as decisões documentadas ajudam futuros funcionários a entender a arquitetura e mostram aos auditores que o risco foi considerado. A diretora da Elmfield aprecia as notas porque explicam decisões técnicas numa linguagem que o conselho acompanha.

### Exemplo resolvido

Sofia esboça uma arquitetura centrada na identidade, põe em camadas as defesas contra ransomware e documenta as decisões principais.

> **Caso sintético.** A arquitetura é sintética.

### Erros e limites

As camadas podem compartilhar fraquezas. As migrações para a nuvem trazem risco de fornecedor.

### Exercícios

- **EX046 — Elemento central.** O que é central na arquitetura-alvo da Elmfield? *Rubrica:* 3 = a identidade com autenticação multifator;; 2 = identidade;; 1 = rede;; 0 = nenhuma.
- **EX047 — Fraqueza compartilhada.** O que poderia enfraquecer a defesa em camadas? *Rubrica:* 3 = uma única conta de administrador controlando todas as camadas;; 2 = administrador compartilhado;; 1 = nada;; 0 = nenhuma.
- **EX048 — Notas de decisão.** O que as notas de decisão de Sofia registram? *Rubrica:* 3 = as alternativas e os riscos aceitos;; 2 = alternativas;; 1 = nada;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) explicar o que a criptografia e o hash protegem; (2) relacioná-los a decisões de política; (3) gerenciar chaves e certificados como itens governados.

### 17.1 O que a criptografia protege

Sofia aprende que a criptografia mantém os dados confidenciais diante de quem não tem a chave, enquanto o hash produz uma impressão digital que muda se os dados mudarem, o que apoia as verificações de integridade. As assinaturas digitais combinam as duas ideias para mostrar quem criou algo e que não foi alterado. Na Elmfield, a criptografia dos notebooks protege os dispositivos perdidos, as conexões seguras protegem os dados em trânsito e os hashes podem mostrar que os arquivos de evidência não foram alterados depois da coleta. Mais adiante no curso, o hash das evidências do teste de backup será um uso direto dessa propriedade de integridade.

### 17.2 Decisões de política

A criptografia exige decisões de política: que dados precisam ser criptografados, onde e com que métodos aprovados. Sofia redige um padrão curto de criptografia para a Elmfield que remete à classificação de dados: dados pessoais dos inquilinos criptografados em repouso nos dispositivos e em trânsito; documentos do conselho criptografados quando compartilhados fora do portal. Ela aprende que a ISO/IEC 27002:2022 espera regras sobre o uso da criptografia e sobre a gestão de chaves, e que regras simples e claras funcionam melhor do que longos documentos técnicos que ninguém lê; uma regra de duas linhas para os documentos do conselho tem mais chance de ser seguida do que um capítulo sobre cifras.

### 17.3 Chaves e certificados

Sofia lista os certificados e as chaves de recuperação da Elmfield. O certificado do site se renova automaticamente, mas as chaves de recuperação dos notebooks ficam guardadas só no console de dispositivos, que uma única pessoa administra. Se essa pessoa saísse, a recuperação poderia falhar. Ela recomenda um segundo administrador e um procedimento de recuperação documentado, o que elimina o ponto único de falha sem nenhuma mudança na criptografia em si. Ela aprende que a maioria das falhas criptográficas em organizações pequenas são falhas de gestão, como certificados vencidos ou chaves perdidas, e não algoritmos quebrados.

### Exemplo resolvido

Sofia explica a criptografia e o hash, redige um padrão curto de criptografia e corrige um risco de chave dependente de um único administrador.

> **Caso sintético.** As chaves da Elmfield são sintéticas; a ISO/IEC 27002:2022 é real.

### Erros e limites

A criptografia não impede o mau uso autorizado. Os procedimentos de chaves precisam ser testados.

### Exercícios

- **EX049 — Papel do hash.** O que o hash apoia? *Rubrica:* 3 = verificações de integridade;; 2 = integridade;; 1 = confidencialidade;; 0 = nenhuma.
- **EX050 — Regra dos documentos do conselho.** Quando os documentos do conselho precisam ser criptografados pelo padrão proposto? *Rubrica:* 3 = quando compartilhados fora do portal;; 2 = fora do portal;; 1 = nunca;; 0 = nenhuma.
- **EX051 — Risco das chaves.** Qual era o risco das chaves de recuperação dos notebooks? *Rubrica:* 3 = um único administrador controlava o único repositório;; 2 = administrador único;; 1 = nada;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta pesquisável sobre governança; (2) escolher adequadamente entre entrevistas e questionários; (3) planejar uma coleta de dados ética.

### 18.1 Uma pergunta de pesquisa

O primeiro projeto de pesquisa de Sofia pergunta por que algumas equipes da Elmfield cumprem as tarefas de segurança no prazo e outras não. Ela a reduz à revisão trimestral de acessos: o que ajuda ou atrapalha os gestores a concluí-la? Aprende que boas perguntas são específicas, respondíveis com os dados disponíveis e úteis para alguém. Perguntar se a cultura de segurança é boa seria vago demais; perguntar o que ajuda os gestores a concluir uma tarefa definida pode levar a melhorias práticas. Focar a revisão trimestral também lhe dá uma tarefa com datas e registros de conclusão que ela pode examinar.

### 18.2 Escolher os métodos

Com só doze gestores, um questionário teria pouco poder estatístico. Sofia escolhe entrevistas semiestruturadas, que permitem aos gestores explicar seus motivos com as próprias palavras. Ela escreve um roteiro de entrevista com perguntas abertas e estímulos, pilota-o com um gestor e revisa duas perguntas confusas antes que distorcessem as outras onze entrevistas. Aprende que as entrevistas servem a grupos pequenos e a perguntas do tipo "por quê", enquanto os questionários servem a grupos grandes e a perguntas do tipo "quantos", e que a escolha deve seguir a pergunta, e não o hábito.

### 18.3 Ética

Sofia submete um pedido curto de aprovação ética ao Brightwater College. A participação é voluntária, as entrevistas só são gravadas com consentimento, as transcrições removem os nomes e a diretora da Elmfield verá só os temas, e não quem disse o quê, o que protege os gestores que criticaram o processo de revisão. Ela aprende que mesmo pesquisas de baixo risco sobre locais de trabalho exigem cuidado, porque os gestores podem temer críticas, e proteger sua identidade incentiva respostas honestas. A aprovação ética chega em duas semanas, e ela começa as entrevistas com folhas de informação claras para cada participante.

### Exemplo resolvido

Sofia formula uma pergunta específica sobre a conclusão da revisão de acessos, escolhe entrevistas para doze gestores e obtém a aprovação ética.

> **Caso sintético.** O estudo é sintético.

### Erros e limites

As entrevistas refletem o que as pessoas dizem, nem sempre o que fazem. Grupos pequenos limitam a generalização.

### Exercícios

- **EX052 — Pergunta reduzida.** A que a pergunta de Sofia foi reduzida? *Rubrica:* 3 = o que ajuda ou atrapalha os gestores a concluir a revisão de acessos;; 2 = específica;; 1 = cultura;; 0 = nenhuma.
- **EX053 — Escolha do método.** Por que entrevistas em vez de questionário? *Rubrica:* 3 = só doze gestores e uma pergunta do tipo por quê;; 2 = grupo pequeno;; 1 = nada;; 0 = nenhuma.
- **EX054 — Acesso da diretora.** O que a diretora da Elmfield verá? *Rubrica:* 3 = só os temas, não quem disse o quê;; 2 = temas;; 1 = transcrições;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Governança, riscos e compliance de segurança: escopo e teoria

### Objetivos de aprendizagem

Você vai (1) definir governança, gestão de riscos e compliance; (2) fixar o escopo de um programa de GRC; (3) explicar a teoria central por trás da gestão de riscos.

### 19.1 Definições

Sofia começa agora as disciplinas de GRC. Governança significa direção e supervisão: quem decide que nível de risco é aceitável e como o desempenho é conferido. Gestão de riscos significa identificar, analisar, avaliar e tratar riscos, processo que a ISO 31000:2018, adotada no Brasil como ABNT NBR ISO 31000:2018, descreve em termos gerais para qualquer organização. Compliance significa cumprir as obrigações vindas de leis, contratos e normas adotadas. Ela aprende que as três se apoiam: a governança dá a direção, a gestão de riscos informa as decisões e o compliance confirma que as obrigações são cumpridas. Na Elmfield, o apetite do conselho dá a direção, o registro informa a diretora e, mais tarde, a declaração de aplicabilidade mostra o compliance.

### 19.2 Escopo

A Elmfield precisa decidir o que seu programa cobre. Sofia propõe um escopo que inclui todos os funcionários, dispositivos, serviços em nuvem e fornecedores que tratam dados dos inquilinos, além do portal do conselho. Os itens excluídos, como os dispositivos dos próprios inquilinos, são listados com os motivos. A ISO/IEC 27001:2022 exige um escopo definido para o sistema de gestão, e ela aprende que um escopo claro evita tanto lacunas quanto esforço desperdiçado: estreito demais, deixa riscos de fora; amplo demais, não pode ser gerido com os recursos da Elmfield. Ao Dr. Haddad ela explica que a Elmfield não controla os dispositivos dos inquilinos, mas pode limitar o que o portal dos inquilinos expõe.

### 19.3 Teoria

Sofia lê sobre a teoria do risco. O risco combina a incerteza sobre eventos com suas consequências para os objetivos. As opções de tratamento incluem evitar, reduzir, compartilhar e aceitar o risco. Cox (2008) mostra que matrizes simples podem ordenar mal os riscos, enquanto Hubbard e Seiersen (2016) defendem estimativas quantitativas mesmo com poucos dados. Ela aprende que a teoria adverte tanto contra a falsa precisão quanto contra a falsa simplicidade, e que organizações pequenas devem escolher métodos que consigam aplicar com consistência e explicar ao conselho. Seu laboratório posterior, que compara notas de matriz com perda esperada, testa exatamente essa advertência nos riscos da Elmfield.

### Exemplo resolvido

Sofia define as três disciplinas, propõe o escopo da Elmfield com as exclusões e revisa a teoria central do risco e as opções de tratamento.

> **Caso sintético.** O escopo da Elmfield é sintético; a ISO 31000:2018 (ABNT NBR ISO 31000:2018), a ISO/IEC 27001:2022, Cox (2008) e Hubbard e Seiersen (2016) são reais.

### Erros e limites

As definições variam conforme a fonte. As decisões de escopo precisam de revisão.

### Exercícios

- **EX055 — Papéis das disciplinas.** Como as três disciplinas se apoiam? *Rubrica:* 3 = governança dá direção, risco informa decisões, compliance confirma obrigações;; 2 = papéis;; 1 = nada;; 0 = nenhuma.
- **EX056 — Item excluído.** Que item ficou fora do escopo? *Rubrica:* 3 = os dispositivos dos próprios inquilinos;; 2 = dispositivos dos inquilinos;; 1 = nada;; 0 = nenhuma.
- **EX057 — Opções de tratamento.** Liste as quatro opções de tratamento. *Rubrica:* 3 = evitar, reduzir, compartilhar, aceitar;; 2 = quatro;; 1 = nada;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Governança, riscos e compliance de segurança: casos fundamentais

### Objetivos de aprendizagem

Você vai (1) analisar casos de governança publicados; (2) extrair lições para uma organização pequena; (3) distinguir causas raiz de sintomas.

### 20.1 Ler casos

Sofia estuda lições de governança em relatórios públicos. O GAO-21-105263, um depoimento de 2021 do Government Accountability Office dos Estados Unidos, descreve fraquezas na supervisão federal da segurança de oleodutos depois do ataque de ransomware aos sistemas de negócio da Colonial Pipeline, incluindo avaliações de risco sem informações de cibersegurança e um protocolo de incidentes não atualizado desde 2010. Ela lê esses relatórios em busca de padrões, e não de culpados: informações de risco incompletas, planos de resposta desatualizados e acompanhamento lento das recomendações se repetem. Os relatórios públicos de auditoria são um bom material didático porque se apoiam em evidências, embora seus contextos possam diferir do da Elmfield.

### 20.2 Lições para a Elmfield

Dos casos, Sofia extrai lições na escala da Elmfield: nomear uma pessoa responsável pelo programa de segurança, escrever uma declaração curta de apetite a riscos aprovada pelo conselho, manter um registro revisado trimestralmente e relatar o progresso ao conselho duas vezes por ano, ritmo adequado a um conselho que se reúne poucas vezes no ano. Ela evita copiar estruturas de grandes organizações que a Elmfield não conseguiria sustentar. Aprende que as boas lições tratam de princípios, como a responsabilização clara, e não de comitês ou ferramentas específicos, que dependem do porte e dos recursos de cada organização.

### 20.3 Causas raiz

Sofia pratica separar sintomas de causas. Num incidente sintético na Elmfield, a conta de um prestador foi usada depois do fim do contrato. O sintoma era uma conta ativa. A causa raiz era que ninguém respondia pelo desligamento dos prestadores, já que os contratos eram geridos pela equipe de manutenção e as contas pela TI. Ela recomenda atribuir esse papel e ligar a data de fim dos contratos ao vencimento das contas, o que também fecha a lacuna para qualquer prestador futuro. Corrigir as causas evita repetições; corrigir só os sintomas, não. Desativar a conta resolveria o caso, mas não impediria o próximo.

### Exemplo resolvido

Sofia lê casos de auditoria pública em busca de padrões, extrai lições proporcionais para a Elmfield e rastreia um incidente com a conta de um prestador até a falta de responsável.

> **Caso sintético.** O incidente da Elmfield é sintético; o GAO-21-105263 é real.

### Erros e limites

Os casos de grandes organizações podem não se transferir. A análise de causa raiz pode parar cedo demais.

### Exercícios

- **EX058 — Fraquezas do GAO.** Que duas fraquezas o GAO-21-105263 descreveu? *Rubrica:* 3 = avaliações de risco sem informações de cibersegurança e protocolo de incidentes desatualizado;; 2 = duas;; 1 = nada;; 0 = nenhuma.
- **EX059 — Relatos ao conselho.** Com que frequência o progresso deve ser relatado ao conselho da Elmfield? *Rubrica:* 3 = duas vezes por ano;; 2 = duas vezes;; 1 = nada;; 0 = nenhuma.
- **EX060 — Causa raiz do prestador.** Qual foi a causa raiz do incidente com a conta do prestador? *Rubrica:* 3 = ninguém respondia pelo desligamento dos prestadores;; 2 = responsável;; 1 = conta ativa;; 0 = nenhuma.

<a id="ch-21"></a>

## Capítulo 21 — Governança, riscos e compliance de segurança: modelos de sistema

### Objetivos de aprendizagem

Você vai (1) modelar o sistema de governança da Elmfield como papéis, processos e fluxos de informação; (2) identificar lacunas de responsabilização; (3) usar uma matriz RACI.

### 21.1 Papéis e processos

Sofia modela a governança da Elmfield como um sistema de papéis e processos. O conselho aprova o apetite a riscos e recebe relatórios. A diretora responde pelo programa. O líder de TI opera os controles técnicos. Os gestores das equipes são responsáveis pelos riscos de suas áreas. Uma encarregada de proteção de dados em tempo parcial cuida da privacidade. Os processos os ligam: revisão de riscos, aprovação de políticas, tratamento de incidentes e revisão de acessos. O desenho mostra quem passa informações a quem e onde as decisões são tomadas; mostra, por exemplo, que os gestores são responsáveis por riscos, mas não têm um caminho definido para levá-los ao conselho.

### 21.2 RACI

Sofia monta uma matriz de responsabilidades que lista, para cada processo, quem é responsável pela execução, quem presta contas, quem é consultado e quem é informado (RACI). Na revisão de acessos, os gestores executam, a diretora presta contas, a TI é consultada e o conselho é informado. Ela encontra dois problemas. Ninguém presta contas pela segurança dos fornecedores, e o tratamento de incidentes tem três pessoas marcadas como prestando contas, o que na prática significa ninguém. O COBIT 2019 usa um mapeamento semelhante para esclarecer os papéis de governança e de gestão. O Dr. Haddad aponta que a lacuna dos fornecedores é a mais grave, porque o prestador de manutenção se conecta remotamente ao sistema habitacional.

### 21.3 Corrigir as lacunas

Sofia propõe que a diretora preste contas pela segurança dos fornecedores, com a gerente financeira executando os contratos e o líder de TI consultado. Nos incidentes, o líder de TI passa a prestar contas, com a encarregada de proteção de dados executando as comunicações de violação. O conselho aprova a matriz. Ela aprende que a prestação de contas deve recair sobre um único papel por processo, e que as matrizes só são úteis se as pessoas as conhecerem e se forem revisadas quando os papéis mudam; uma revisão a cada mudança de papel teria apanhado antes os três nomes no tratamento de incidentes.

### Exemplo resolvido

Sofia modela os papéis e processos de governança da Elmfield, encontra duas lacunas de responsabilização com uma matriz RACI e as corrige.

> **Caso sintético.** Os papéis e a matriz são sintéticos; o COBIT 2019 é real.

### Erros e limites

As matrizes descrevem os papéis pretendidos, não o comportamento. Equipes pequenas confundem papéis.

### Exercícios

- **EX061 — Letras do RACI.** O que significam as quatro letras do RACI? *Rubrica:* 3 = responsável pela execução, quem presta contas, consultado, informado;; 2 = quatro;; 1 = nada;; 0 = nenhuma.
- **EX062 — Problema dos incidentes.** O que estava errado no tratamento de incidentes? *Rubrica:* 3 = três pessoas prestando contas significava ninguém;; 2 = gente demais;; 1 = nada;; 0 = nenhuma.
- **EX063 — Regra de prestação de contas.** Quantos papéis devem prestar contas por processo? *Rubrica:* 3 = um;; 2 = único;; 1 = vários;; 0 = nenhuma.

<a id="ch-22"></a>

## Capítulo 22 — Governança, riscos e compliance de segurança: dados e dependências

### Objetivos de aprendizagem

Você vai (1) mapear as dependências de fornecedores; (2) classificar os fornecedores em níveis de risco; (3) fixar controles proporcionais para os fornecedores.

### 22.1 Dependências de fornecedores

A Elmfield depende de fornecedores para o sistema habitacional, o e-mail, a folha de pagamento, a manutenção e a impressão. Sofia mapeia o que cada fornecedor acessa: dados, sistemas ou instalações. Aprende que o NIST CSF 2.0 inclui a gestão de riscos de cibersegurança da cadeia de suprimentos na função Govern, e que a ISO/IEC 27002:2022 cobre a segurança da informação nas relações com fornecedores. Organizações pequenas dependem muito de fornecedores, então sua segurança costuma depender tanto dos controles deles quanto dos próprios. O acesso remoto do prestador de manutenção ao sistema habitacional mostra como os controles de um fornecedor passam a fazer parte da exposição da própria Elmfield.

### 22.2 Níveis

Sofia pontua cinco fornecedores de zero a dois em três fatores: acesso a dados pessoais, criticidade para os serviços e acesso remoto a sistemas. O laboratório soma as notas e atribui os níveis. O prestador de manutenção e o e-mail em nuvem somam cinco, nível alto. O escritório de folha de pagamento soma quatro, também alto, por meio dos dados pessoais e da criticidade, mesmo sem acesso remoto. A gráfica soma um e a empresa de limpeza, zero, ambas de nível baixo. A classificação permite à Elmfield concentrar o escrutínio nos três fornecedores de nível alto, em vez de tratar todos os fornecedores da mesma forma, e as notas explicam a razão de cada nível.

### Laboratório — Níveis de fornecedores por dados, criticidade e acesso remoto

```python
"""Supplier tiering: data access, criticality and remote access scored 0-2 (synthetic)."""
sup = {"repairs contractor": (1, 2, 2), "payroll bureau": (2, 2, 0), "cloud email": (2, 2, 1),
       "printing firm": (1, 0, 0), "cleaning company": (0, 0, 0)}
for s, (d, c, r) in sup.items():
    t = d + c + r; tier = "high" if t >= 4 else "medium" if t >= 2 else "low"
    print(f"{s}: score {t} tier {tier}")
```

Execute com `python3 lab_tier.py`. Saída verificada:

```text
repairs contractor: score 5 tier high
payroll bureau: score 4 tier high
cloud email: score 5 tier high
printing firm: score 1 tier low
cleaning company: score 0 tier low
```

### 22.3 Controles proporcionais

Para os fornecedores de nível alto, Sofia recomenda perguntas de segurança antes dos contratos, cláusulas contratuais de notificação de violações e devolução de dados e uma revisão anual de seus relatórios de garantia ou certificações. Para os de nível baixo, basta uma cláusula curta de confidencialidade. Ela observa que o acesso remoto do prestador de manutenção precisa de atenção especial, porque sua equipe se conecta ao sistema habitacional a partir dos próprios escritórios; exigir contas nominais apoiaria também os controles contra mau uso escolhidos depois. Ela aprende que uma governança de fornecedores proporcional economiza esforço e concentra a atenção no risco real.

### Exemplo resolvido

Sofia mapeia os acessos dos fornecedores, classifica cinco fornecedores, três deles de nível alto, e fixa controles proporcionais.

> **Caso sintético.** Os fornecedores e as notas são sintéticos; o CSF 2.0 e a ISO/IEC 27002:2022 são reais.

### Erros e limites

Notas simples perdem nuances. Os relatórios de garantia dos fornecedores variam de escopo.

### Exercícios

- **EX064 — Fatores dos níveis.** Que três fatores são pontuados? *Rubrica:* 3 = acesso a dados pessoais, criticidade, acesso remoto;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX065 — Nível alto.** Que fornecedores ficam no nível alto? *Rubrica:* 3 = prestador de manutenção, e-mail em nuvem, folha de pagamento;; 2 = três;; 1 = gráfica;; 0 = nenhuma.
- **EX066 — Controles de nível alto.** Cite dois controles para fornecedores de nível alto. *Rubrica:* 3 = perguntas antes do contrato e cláusulas de notificação de violações;; 2 = controles;; 1 = nada;; 0 = nenhuma.

<a id="ch-23"></a>

## Capítulo 23 — Governança, riscos e compliance de segurança: métodos I

### Objetivos de aprendizagem

Você vai (1) pontuar riscos numa matriz 5x5; (2) comparar as notas da matriz com a perda esperada; (3) entender quando as duas discordam.

### 23.1 Pontuação na matriz

A Elmfield pontua os riscos numa matriz cinco por cinco: probabilidade e impacto de um a cinco, multiplicados para dar a nota. Sofia pontua cinco riscos com os gestores. Dados de inquilinos mal endereçados ficam com doze, o notebook perdido com doze, o ransomware com dez, o mau uso pelo prestador com nove e a queda da página de pagamento com seis. A matriz é rápida e familiar, e por isso muitas organizações a usam. Sofia também pede aos gestores uma probabilidade anual e uma perda típica para cada risco, para comparar os métodos; é esse pedido que torna possível a comparação da seção seguinte.

### 23.2 Perda esperada

O laboratório calcula a perda esperada como probabilidade vezes perda. O ransomware, com uma chance em dez e uma perda de duzentos e cinquenta mil, tem a maior perda esperada, vinte e cinco mil. Os dados mal endereçados vêm em seguida, com doze mil, e o notebook perdido com dez mil. A matriz põe os dados mal endereçados em primeiro, empatados com o notebook, enquanto a perda esperada põe o ransomware em primeiro. A discordância surge porque a matriz comprime um impacto muito grande numa nota cinco: como o impacto tem teto em cinco, a perda de duzentos e cinquenta mil do ransomware não aparece como muitas vezes maior do que as perdas menores.

### Laboratório — Notas da matriz contra perda esperada

```python
"""5x5 scores vs expected loss (thousands) for five Elmfield risks."""
risks = [("tenant data misdirected", 4, 3, 0.8, 15), ("ransomware", 2, 5, 0.1, 250),
         ("lost laptop", 3, 4, 0.5, 20), ("payment page outage", 3, 2, 0.6, 8), ("contractor misuse", 3, 3, 0.2, 40)]
for n, l, i, p, loss in risks: print(f"{n}: score {l*i}, expected loss {p*loss:.1f}k")
print("top by score:", max(risks, key=lambda r: r[1]*r[2])[0]); print("top by expected loss:", max(risks, key=lambda r: r[3]*r[4])[0])
```

Execute com `python3 lab_score.py`. Saída verificada:

```text
tenant data misdirected: score 12, expected loss 12.0k
ransomware: score 10, expected loss 25.0k
lost laptop: score 12, expected loss 10.0k
payment page outage: score 6, expected loss 4.8k
contractor misuse: score 9, expected loss 8.0k
top by score: tenant data misdirected
top by expected loss: ransomware
```

### 23.3 Quando discordam

Sofia lê Cox (2008), que mostra que as matrizes de risco podem dar notas maiores a riscos quantitativamente menores e produzir empates entre riscos muito diferentes. Seu laboratório ilustra os dois problemas. Ela não conclui que as matrizes são inúteis: ajudam a iniciar conversas e são fáceis para não especialistas. Recomenda que a Elmfield mantenha a matriz para a triagem inicial, mas acrescente estimativas aproximadas de perda esperada para os principais riscos, para que riscos raros e graves como o ransomware não sejam subestimados. Fazer isso só para os cinco principais mantém pequeno o trabalho extra para uma equipe do porte da Elmfield.

### Exemplo resolvido

Sofia constata que a matriz põe os dados mal endereçados em primeiro, enquanto a perda esperada põe o ransomware em primeiro, e recomenda combinar os dois métodos.

> **Caso sintético.** As notas e as estimativas são sintéticas; Cox (2008) é real.

### Erros e limites

A perda esperada exige entradas incertas. As matrizes comprimem a gravidade.

### Exercícios

- **EX067 — Topo da matriz.** Que risco lidera a ordenação da matriz? *Rubrica:* 3 = dados de inquilinos mal endereçados, empatados com o notebook em 12;; 2 = empate;; 1 = ransomware;; 0 = nenhuma.
- **EX068 — Topo pela perda esperada.** Que risco lidera pela perda esperada? *Rubrica:* 3 = ransomware, com 25 mil;; 2 = ransomware;; 1 = notebook;; 0 = nenhuma.
- **EX069 — Causa da discordância.** Por que os métodos discordam sobre o ransomware? *Rubrica:* 3 = a matriz comprime impactos muito grandes numa nota cinco;; 2 = compressão;; 1 = nada;; 0 = nenhuma.

<a id="ch-24"></a>

## Capítulo 24 — Governança, riscos e compliance de segurança: controles

### Objetivos de aprendizagem

Você vai (1) selecionar controles para os principais riscos da Elmfield; (2) escrever uma declaração de aplicabilidade; (3) atribuir responsáveis aos controles.

### 24.1 Selecionar controles

Para cada risco principal, Sofia seleciona controles da ISO/IEC 27002:2022. Para os dados mal endereçados: links de compartilhamento seguros, conferência de destinatários e treinamento. Para os notebooks perdidos: criptografia e apagamento remoto. Para o ransomware: backups offline, autenticação multifator e direitos de administrador limitados. Para o mau uso pelo prestador: contas nominais e revisões de acesso. Ela aprende que selecionar de um catálogo reconhecido torna as escolhas mais fáceis de explicar e ajuda a garantir que nada óbvio fique de fora. Ligar cada controle a um risco nomeado também permite mostrar aos auditores por que cada um foi escolhido.

### 24.2 Declaração de aplicabilidade

A ISO/IEC 27001:2022, adotada no Brasil como ABNT NBR ISO/IEC 27001:2022, exige uma declaração de aplicabilidade que liste os controles de referência, se cada um está incluído e por quê. Sofia redige uma para a Elmfield. A maioria dos controles é incluída. Alguns são excluídos com motivos: os controles de desenvolvimento seguro ficam de fora porque a Elmfield não desenvolve software, embora os controles de fornecedores cubram seu sistema habitacional. Ela aprende que as exclusões precisam ser justificadas pelo escopo e pelo risco, e não pela conveniência, e que a declaração se torna um documento-chave para os auditores.

### 24.3 Responsáveis

Cada controle precisa de um responsável que garanta sua operação. Sofia atribui os responsáveis: o líder de TI para backups e criptografia, os gestores para as revisões de acesso, a encarregada de proteção de dados para as regras de compartilhamento e a gerente financeira para os contratos com fornecedores. Ela escreve uma descrição de uma linha da operação de cada controle. Aprende que os responsáveis precisam de autoridade e de tempo; atribuir tudo ao líder de TI sobrecarregaria uma pessoa e deixaria controles sem execução quando ela estivesse ausente. Dividir a responsabilidade distribui a carga entre papéis com o conhecimento certo.

### Exemplo resolvido

Sofia seleciona controles para quatro riscos, redige uma declaração de aplicabilidade com exclusões justificadas e distribui a responsabilidade.

> **Caso sintético.** Os controles da Elmfield são sintéticos; a ISO/IEC 27001:2022 (ABNT NBR ISO/IEC 27001:2022) e a 27002:2022 são reais.

### Erros e limites

Os controles de catálogo precisam ser adaptados. Os responsáveis mudam de função.

### Exercícios

- **EX070 — Controles dos notebooks.** Que controles tratam os notebooks perdidos? *Rubrica:* 3 = criptografia e apagamento remoto;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX071 — Exclusão justificada.** Por que os controles de desenvolvimento seguro foram excluídos? *Rubrica:* 3 = a Elmfield não desenvolve software;; 2 = sem desenvolvimento;; 1 = nada;; 0 = nenhuma.
- **EX072 — Distribuição dos responsáveis.** Por que não atribuir todos os controles ao líder de TI? *Rubrica:* 3 = sobrecarregaria uma pessoa;; 2 = sobrecarga;; 1 = nada;; 0 = nenhuma.

<a id="ch-25"></a>

## Capítulo 25 — Laboratório I

### Objetivos de aprendizagem

Você vai (1) testar um controle num ambiente seguro; (2) registrar as evidências corretamente; (3) comparar os resultados com o esperado.

### 25.1 Planejar o teste

No primeiro laboratório, Sofia testa o controle de backup da Elmfield usando uma cópia de teste do compartilhamento de arquivos fornecida pelo líder de TI. O teste confere se existe um backup para cada dia da última semana, se ele fica guardado offline e se uma amostra de arquivos pode ser restaurada. Ela escreve os passos, os resultados esperados e as evidências a coletar antes de começar, para que o teste não possa ser redefinido em silêncio se algo falhar. Testar numa cópia garante que nada em uso real seja perturbado e que o trabalho dos funcionários continue normalmente durante o teste.

### 25.2 Executar e registrar

Sofia restaura vinte arquivos sorteados de pastas e datas diferentes, o que aumenta a chance de uma exclusão oculta aparecer. Dezenove são restaurados corretamente. Um, uma planilha grande, falha porque o backup excluía arquivos acima de um limite de tamanho. Ela registra a data, os passos, os resultados, as capturas de tela e a lista de arquivos. Guarda as evidências numa pasta que só ela e o líder de TI podem alterar. Aprende que a evidência precisa permitir que outra pessoa entenda o que foi testado e veja o resultado por si mesma, sem depender da palavra de quem fez o teste.

### 25.3 Comparar com o esperado

A descrição do controle dizia que todos os arquivos são copiados toda noite; o teste mostra que os arquivos grandes ficam de fora. Sofia relata a lacuna com seu impacto provável: as planilhas grandes incluem os registros de aluguéis atrasados. O líder de TI muda a configuração e pede um novo teste, que passa. Ela aprende que os testes revelam a diferença entre o que se acredita que um controle faz e o que ele faz, muitas vezes por uma escolha de configuração esquecida. O Dr. Haddad pergunta por que ninguém notou antes, e Sofia aponta que o relatório noturno mostrava sucesso porque os arquivos excluídos nunca contavam como falhas.

### Exemplo resolvido

Sofia testa os backups numa cópia, restaura dezenove de vinte arquivos, encontra uma exclusão por tamanho e confirma a correção com um novo teste.

> **Caso sintético.** O teste é sintético.

### Erros e limites

Amostras pequenas deixam escapar falhas raras. As cópias de teste podem diferir dos sistemas reais.

### Exercícios

- **EX073 — Resultado da restauração.** Quantos arquivos amostrados foram restaurados corretamente? *Rubrica:* 3 = dezenove de vinte;; 2 = 19;; 1 = 20;; 0 = nenhuma.
- **EX074 — Causa da falha.** Por que um arquivo não foi restaurado? *Rubrica:* 3 = o backup excluía arquivos acima de um limite de tamanho;; 2 = limite de tamanho;; 1 = nada;; 0 = nenhuma.
- **EX075 — Crença e realidade.** O que o teste revelou sobre o controle? *Rubrica:* 3 = fazia menos do que se acreditava por uma configuração esquecida;; 2 = lacuna;; 1 = nada;; 0 = nenhuma.

<a id="ch-26"></a>

## Capítulo 26 — Governança, riscos e compliance de segurança: métodos II

### Objetivos de aprendizagem

Você vai (1) conduzir uma avaliação de lacunas contra o NIST CSF 2.0; (2) resumir os resultados por função; (3) priorizar as melhorias.

### 26.1 Avaliação de lacunas

Sofia conduz uma avaliação de lacunas com uma amostra de resultados de cada função do NIST CSF 2.0: Govern, Identify, Protect, Detect, Respond e Recover. Com o líder de TI e a diretora, ela classifica cada resultado amostrado como alcançado ou não alcançado, com base em evidências, e não em opiniões. Um resultado sobre backups, por exemplo, só conta como alcançado por causa do teste de laboratório. Ela registra a evidência de cada classificação para que as reavaliações futuras comparem coisas comparáveis; ligar o resultado de backup ao teste permite repetir a classificação depois com a mesma evidência.

### 26.2 Resultados

O laboratório resume vinte e oito resultados classificados. Protect é a mais forte, com cinco de seis, oitenta e três por cento. Identify chega a sessenta por cento. Govern e Respond chegam a cinquenta por cento. Recover chega a trinta e três por cento, e Detect é a mais fraca, com um de quatro, vinte e cinco por cento. No total, quinze de vinte e oito resultados são alcançados, cinquenta e quatro por cento. Sofia observa que a Elmfield investiu em proteção, mas tem pouca capacidade de perceber incidentes ou se recuperar deles, padrão comum em organizações pequenas. Com só quatro resultados de Detect, um a mais moveria esse número em vinte e cinco pontos.

### Laboratório — Resultados alcançados do CSF 2.0 por função

```python
"""Gap assessment: share of sampled CSF 2.0 outcomes achieved per function (synthetic ratings)."""
ratings = {"Govern": [1,0,0,1,0,1], "Identify": [1,1,0,1,0], "Protect": [1,1,1,0,1,1],
           "Detect": [0,1,0,0], "Respond": [1,0,0,1], "Recover": [0,0,1]}
for f, r in ratings.items(): print(f"{f}: {sum(r)}/{len(r)} = {sum(r)/len(r):.0%}")
t = sum(sum(r) for r in ratings.values()); n = sum(len(r) for r in ratings.values())
print(f"overall {t}/{n} = {t/n:.0%}; weakest {min(ratings, key=lambda f: sum(ratings[f])/len(ratings[f]))}")
```

Execute com `python3 lab_gap.py`. Saída verificada:

```text
Govern: 3/6 = 50%
Identify: 3/5 = 60%
Protect: 5/6 = 83%
Detect: 1/4 = 25%
Respond: 2/4 = 50%
Recover: 1/3 = 33%
overall 15/28 = 54%; weakest Detect
```

### 26.3 Prioridades

Sofia propõe prioridades com base nas lacunas e no risco. A detecção vem primeiro, respondendo à função mais fraca: ativar alertas nos serviços de e-mail e de identidade em nuvem e designar alguém para revisá-los. A recuperação vem em segundo: documentar e testar um plano de restauração do sistema habitacional. As melhorias de governança, como aprovar um apetite a riscos, vêm depois. Ela adverte que as porcentagens de amostras pequenas são aproximadas, então devem orientar as prioridades, e não virar metas. O conselho aprova o plano para o ano seguinte, com a detecção à frente.

### Exemplo resolvido

Sofia classifica vinte e oito resultados do CSF, constata que Detect é a função mais fraca, com vinte e cinco por cento, e prioriza a detecção e a recuperação.

> **Caso sintético.** As classificações são sintéticas; o CSF 2.0 é real.

### Erros e limites

Os resultados amostrados não são o framework inteiro. Classificações binárias perdem nuances.

### Exercícios

- **EX076 — Base da classificação.** Com que base os resultados são classificados como alcançados? *Rubrica:* 3 = evidências, e não opiniões;; 2 = evidências;; 1 = opinião;; 0 = nenhuma.
- **EX077 — Função mais fraca.** Que função é a mais fraca, e em que nível? *Rubrica:* 3 = Detect, 1/4 = 25%;; 2 = Detect;; 1 = Protect;; 0 = nenhuma.
- **EX078 — Resultado geral.** Que proporção dos resultados é alcançada no total? *Rubrica:* 3 = 15/28 = 54%;; 2 = 54%;; 1 = nada;; 0 = nenhuma.

<a id="ch-27"></a>

## Capítulo 27 — Governança, riscos e compliance de segurança: verificação

### Objetivos de aprendizagem

Você vai (1) verificar controles por inspeção, observação e reexecução; (2) escolher testes adequados; (3) documentar os resultados da verificação.

### 27.1 Tipos de teste

Sofia aprende três formas de verificar um controle. A inspeção examina documentos ou registros, como as aprovações das revisões de acesso. A observação acompanha a execução de um controle, como um gestor revisando acessos. A reexecução repete o controle de forma independente, como Sofia comparar ela mesma a lista de desligamentos com as contas ativas. A reexecução dá a evidência mais forte porque não depende dos registros do responsável, mas exige mais tempo e acesso. Sua comparação da lista de desligamentos com as contas ativas é reexecução, e é por isso que depois encontra o que a revisão deixou passar.

### 27.2 Escolher os testes

Para cada controle-chave, Sofia escolhe um teste. Nas revisões de acesso, inspeciona as aprovações e reexecuta uma amostra, porque elas protegem os dados dos inquilinos em todos os sistemas. Na criptografia, inspeciona o relatório do console de dispositivos. No tratamento de incidentes, observa um exercício de mesa. Ela aprende que a escolha depende da importância do controle e das evidências disponíveis, e que os controles importantes merecem testes mais fortes. Também observa que depender só da inspeção traz o risco de aceitar registros que parecem completos, mas descrevem controles que ninguém executou de fato.

### 27.3 Documentar os resultados

Sofia documenta cada teste com objetivo, método, amostra, resultados e conclusão. A reexecução da verificação de desligamentos revela uma conta que a revisão de acessos deixou passar, então ela conclui que o controle de revisão opera com exceção e recomenda acrescentar a lista de desligamentos ao material dos revisores. Ela aprende que os resultados da verificação devem dizer com clareza se um controle operou com eficácia, operou com exceções ou falhou, para que a gestão saiba quanto pode confiar nele; aqui, a gestão pode confiar na revisão, mas só depois de acrescentada a lista de desligamentos.

### Exemplo resolvido

Sofia usa inspeção, observação e reexecução, encontra uma exceção na revisão de acessos e declara as conclusões com clareza.

> **Caso sintético.** Os testes e os resultados são sintéticos.

### Erros e limites

A observação pode mudar o comportamento. A reexecução exige acesso.

### Exercícios

- **EX079 — Teste mais forte.** Que tipo de teste dá a evidência mais forte? *Rubrica:* 3 = reexecução;; 2 = reexecutar;; 1 = inspeção;; 0 = nenhuma.
- **EX080 — Risco da inspeção.** Qual é o risco de depender só da inspeção? *Rubrica:* 3 = os registros podem descrever controles que ninguém executou;; 2 = registros falsos;; 1 = nada;; 0 = nenhuma.
- **EX081 — Categorias de conclusão.** Que três conclusões uma verificação pode alcançar? *Rubrica:* 3 = eficaz, eficaz com exceções, falhou;; 2 = três;; 1 = nada;; 0 = nenhuma.

<a id="ch-28"></a>

## Capítulo 28 — Governança, riscos e compliance de segurança: análise de falhas

### Objetivos de aprendizagem

Você vai (1) analisar um incidente em busca de falhas de controle; (2) conduzir uma revisão sem culpados; (3) transformar as lições em mudanças de controles.

### 28.1 O incidente

Ocorre um incidente sintético: um agente de habitação envia por e-mail uma planilha com detalhes de aluguéis atrasados de inquilinos para um endereço externo com nome parecido com o de um contato da prefeitura. O destinatário avisa, e o arquivo é apagado. Sofia ajuda a encarregada de proteção de dados a avaliar se a violação precisa ser comunicada ao regulador e se os inquilinos devem ser avisados, seguindo o procedimento da Elmfield. A avaliação considera a sensibilidade dos dados e a confirmação de exclusão pelo destinatário, que reduz o risco aos inquilinos, mas não dispensa por si só a avaliação.

### 28.2 Revisão sem culpados

Sofia conduz uma revisão sem culpados. O objetivo é entender como o sistema permitiu o erro, e não punir o agente. Eles descobrem que o e-mail completou automaticamente o endereço errado, que planilhas com dados de atraso eram enviadas rotineiramente por e-mail em vez de compartilhadas pelo sistema habitacional e que não aparecia nenhum aviso para destinatários externos. São condições do sistema que pegariam qualquer agente, não só este. Sofia aprende que as revisões sem culpados incentivam relatos honestos, que revelam problemas de projeto, enquanto culpar indivíduos tende a esconder informações e deixa as mesmas condições no lugar.

### 28.3 Mudanças nos controles

A revisão leva a mudanças: um aviso de destinatário externo no e-mail, uma regra de que os dados de atraso são compartilhados por links seguros com prazo de validade e um lembrete curto nas reuniões de equipe. Sofia atualiza o registro de riscos, elevando a estimativa de probabilidade dos dados mal endereçados, já que o incidente mostrou que o risco era mais provável do que a nota anterior, e registrando os novos controles. Ela aprende que os incidentes são evidências sobre a eficácia dos controles e devem realimentar a avaliação de riscos, fechando o ciclo entre operações e governança.

### Exemplo resolvido

Sofia apoia a avaliação da violação, conduz uma revisão sem culpados que encontra três causas sistêmicas e leva as mudanças ao registro.

> **Caso sintético.** O incidente é sintético.

### Erros e limites

As revisões sem culpados ainda precisam responsabilizar a negligência repetida. Os avisos causam fadiga.

### Exercícios

- **EX082 — Objetivo da revisão.** Qual é o objetivo de uma revisão sem culpados? *Rubrica:* 3 = entender como o sistema permitiu o erro;; 2 = sistema;; 1 = punição;; 0 = nenhuma.
- **EX083 — Causas sistêmicas.** Cite duas causas sistêmicas encontradas. *Rubrica:* 3 = preenchimento automático e envio rotineiro das planilhas de atraso por e-mail;; 2 = causas;; 1 = nada;; 0 = nenhuma.
- **EX084 — Atualização do registro.** Como Sofia atualizou o registro? *Rubrica:* 3 = elevou a probabilidade dos dados mal endereçados e registrou os novos controles;; 2 = atualização;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX084 (as de EX085–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Sofia Reyes, o Dr. Malik Haddad, o Brightwater College, a Elmfield Housing Association, o Corbridge Community Trust e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Cinco pontos percentuais (uma redução à metade em termos relativos).

**EX002.** Porque, sem a contagem e sem saber quais itens faltam, a proporção esconde detalhes importantes.

**EX003.** A data, a contagem, a base e a fonte.

**EX004.** Nome do ativo, tipo, responsável, localização, dados guardados e fornecedor.

**EX005.** O portal do conselho não tinha responsável e onze tablets não constavam da lista da manutenção.

**EX006.** Uma conferência trimestral contra os registros de compras e o sistema de identidade.

**EX007.** Troca impressões por fatos e dá a mesma resposta a cada execução.

**EX008.** Ativos com dados pessoais de inquilinos que não tinham responsável.

**EX009.** O ativo, o problema, um responsável sugerido e a data da execução.

**EX010.** Que os frameworks formais custam caro demais para equipes pequenas.

**EX011.** Porque os requisitos mudam entre as edições.

**EX012.** Porque, se você não consegue explicar uma ideia com suas próprias palavras, ainda não a entendeu.

**EX013.** De falhas e erros comuns, e não de ataques sofisticados.

**EX014.** Backups mantidos offline.

**EX015.** Porque o medo muitas vezes leva os funcionários a esconder os erros em vez de relatá-los.

**EX016.** Uma pessoa que cobria uma colega podia tanto cadastrar um fornecedor quanto aprovar pagamentos a ele.

**EX017.** Com acesso temporário, um segundo aprovador e uma data de término.

**EX018.** A identidade em nuvem, da qual depende a maioria dos serviços.

**EX019.** Porque os funcionários e os dados estão espalhados por serviços em nuvem, dispositivos móveis e escritórios.

**EX020.** Só o nome, o endereço e o telefone de que precisam.

**EX021.** O serviço de área de trabalho remota exposto no servidor de arquivos.

**EX022.** Porque sua saída pode ser usada como evidência, e evidência errada engana.

**EX023.** Porque o sistema de identidade usa endereços de e-mail e o RH usa números de matrícula.

**EX024.** Uma conta ativa que não corresponde a nenhum funcionário.

**EX025.** Probabilidade multiplicada pelo impacto.

**EX026.** Dados de inquilinos enviados por e-mail à pessoa errada e o notebook perdido com anotações de casos, ambos com nota 12.

**EX027.** R3, mau uso da conta do prestador de manutenção, e R6, senhas fracas no portal do conselho.

**EX028.** Testes ativos em sistemas.

**EX029.** Guardou-os num notebook criptografado da Elmfield, removeu os nomes ao compartilhar e apagou as cópias no fim.

**EX030.** Porque os atacantes poderiam explorá-la a qualquer momento, então esperar deixaria o dano possível.

**EX031.** A participação no grupo de administradores em cada notebook.

**EX032.** Eram notebooks da manutenção comprados localmente, fora do caminho normal de compras.

**EX033.** Trinta dias.

**EX034.** Porque se comporta bem com contagens pequenas e proporções próximas de zero ou de um.

**EX035.** 42% a 75%.

**EX036.** Porque raramente usam notebooks e a política foi enviada por e-mail.

**EX037.** O RH envia os avisos de desligamento automaticamente antes do último dia e a TI confirma cada desativação num ticket.

**EX038.** Só a equipe especializada de apoio.

**EX039.** Sete.

**EX040.** Usar os dados de locação e manutenção para marketing sem relação.

**EX041.** Os prestadores de manutenção recebem dados demais e a retenção das gravações de chamadas é desconhecida (também as necessidades de apoio guardadas em dois lugares).

**EX042.** Porque é um incidente de segurança e uma violação de dados pessoais que pode precisar ser comunicada.

**EX043.** Porque mede quanto tempo as vulnerabilidades ficam abertas, que é o propósito do controle.

**EX044.** Uma mediana de 21 dias, com 10 de 15 (67%) em até 30 dias.

**EX045.** Afetavam o servidor de arquivos, que os funcionários evitam reiniciar no horário de trabalho.

**EX046.** A identidade, com login único e autenticação multifator.

**EX047.** Uma fraqueza compartilhada, como uma única conta de administrador que controla todas as camadas.

**EX048.** A escolha, suas alternativas e os riscos aceitos.

**EX049.** Verificações de integridade, porque a impressão digital muda se os dados mudarem.

**EX050.** Quando compartilhados fora do portal do conselho.

**EX051.** Só uma pessoa administrava o console que as guardava, então a recuperação poderia falhar se ela saísse.

**EX052.** O que ajuda ou atrapalha os gestores a concluir a revisão trimestral de acessos.

**EX053.** Porque são só doze gestores e a pergunta é do tipo por quê.

**EX054.** Só os temas, não quem disse o quê.

**EX055.** A governança dá a direção, a gestão de riscos informa as decisões e o compliance confirma que as obrigações são cumpridas.

**EX056.** Os dispositivos dos próprios inquilinos, com os motivos registrados.

**EX057.** Evitar, reduzir, compartilhar e aceitar.

**EX058.** Avaliações de risco sem informações de cibersegurança e um protocolo de resposta a incidentes não atualizado desde 2010.

**EX059.** Duas vezes por ano.

**EX060.** Ninguém respondia pelo desligamento dos prestadores entre a equipe de manutenção e a TI.

**EX061.** Responsável pela execução, quem presta contas, consultado e informado.

**EX062.** Três pessoas estavam marcadas como prestando contas, o que na prática significa ninguém.

**EX063.** Um.

**EX064.** Acesso a dados pessoais, criticidade para os serviços e acesso remoto a sistemas.

**EX065.** O prestador de manutenção (5), o e-mail em nuvem (5) e o escritório de folha de pagamento (4).

**EX066.** Por exemplo, perguntas de segurança antes dos contratos e cláusulas de notificação de violações (também revisão anual de garantia).

**EX067.** Dados de inquilinos mal endereçados, empatados com o notebook perdido em 12.

**EX068.** O ransomware, com 25 mil.

**EX069.** Porque a matriz comprime um impacto muito grande numa nota máxima de cinco.

**EX070.** Criptografia e apagamento remoto.

**EX071.** Porque a Elmfield não desenvolve software; os controles de fornecedores cobrem seu sistema habitacional.

**EX072.** Porque sobrecarregaria uma pessoa e deixaria controles sem execução na ausência dela.

**EX073.** Dezenove de vinte.

**EX074.** O backup excluía arquivos acima de um limite de tamanho.

**EX075.** Que ele fazia menos do que a descrição afirmava, por causa de uma escolha de configuração esquecida.

**EX076.** Em evidências, como o resultado de um teste, e não em opiniões.

**EX077.** Detect, com um de quatro resultados (25%).

**EX078.** Quinze de vinte e oito, 54%.

**EX079.** A reexecução, porque não depende dos registros do responsável.

**EX080.** Aceitar registros que parecem completos, mas descrevem controles que ninguém executou.

**EX081.** Operou com eficácia, operou com exceções ou falhou.

**EX082.** Entender como o sistema permitiu o erro, e não punir a pessoa.

**EX083.** Por exemplo, o e-mail completou automaticamente o endereço errado e as planilhas de atraso eram enviadas rotineiramente por e-mail (também a falta de aviso externo).

**EX084.** Elevou a estimativa de probabilidade dos dados mal endereçados e registrou os novos controles.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO 31000:2018 e da ABNT NBR ISO/IEC 27001:2022, citadas nesta edição como referências brasileiras e conferidas em suas fontes oficiais; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Associação Brasileira de Normas Técnicas. (2018). *ABNT NBR ISO 31000:2018 — Gestão de riscos — Diretrizes*. ABNT. <https://www.abntcatalogo.com.br/>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Cox, L. A., Jr. (2008). What's wrong with risk matrices? *Risk Analysis*, 28(2), 497–512. <https://doi.org/10.1111/j.1539-6924.2008.01030.x>
- Hubbard, D. W., & Seiersen, R. (2016). *How to measure anything in cybersecurity risk*. Wiley. <https://doi.org/10.1002/9781119162315>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. ISACA. <https://www.isaca.org/resources/cobit>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
- Schroeder, K., Trinh, H., & Pillitteri, V. (2024). *Measurement guide for information security: Volume 1 — Identifying and selecting measures* (NIST SP 800-55v1). <https://doi.org/10.6028/NIST.SP.800-55v1>
- Spears, J. L., & Barki, H. (2010). User participation in information systems security risk management. *MIS Quarterly*, 34(3), 503–522. <https://doi.org/10.2307/25750689>
- U.S. Government Accountability Office. (2021). *Critical infrastructure protection: TSA is taking steps to address some pipeline security program weaknesses* (GAO-21-105263). <https://www.gao.gov/products/gao-21-105263>
