# Governança, Riscos e Compliance de Segurança: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 097, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 40 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3; os capítulos 9–40 (EX025–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Sofia Reyes, o Dr. Malik Haddad, o Brightwater College, a Elmfield Housing Association, o Corbridge Community Trust e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
