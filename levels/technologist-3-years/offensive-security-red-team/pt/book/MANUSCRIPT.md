# Segurança Ofensiva Autorizada e Red Team: Um Livro para o Tecnólogo

- Idioma: português do Brasil (`pt`); curso de tecnólogo, três anos; aproximadamente 2.400 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–9 de 30 já estão escritos em português, com os exercícios EX001–EX027 e suas resoluções com rubricas de 0 a 3 e 3 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 10–30 (EX028–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: implementadores e administradores de tecnologia que vão construir, operar e medir a capacidade de avaliação autorizada de uma organização, trabalhando ao lado de seus defensores.
- Relação com os livros vizinhos: o [livro técnico](../../../../technical-18-months/offensive-security-red-team/en/book/MANUSCRIPT.md) enfatiza a disciplina no uso de ferramentas e a verificação; o [livro de bacharelado](../../../../bachelors-4-years/offensive-security-red-team/pt/book/MANUSCRIPT.md) acrescenta teoria mais ampla. **Este livro trata da integração de serviços, controles, operações e medição em torno de testes autorizados.**
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação acreditada e **não concede autorização para testar nenhum sistema real**. O livro não contém código de exploit, payloads nem procedimentos de ataque passo a passo. Os laboratórios verificam escopo, registros, evidências, classificações, cobertura e relatórios sobre dados inventados.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–9 constroem o letramento em computação, identidade, arquitetura e medição de que um tecnólogo precisa antes de participar de um engajamento. Os capítulos 10–23 cobrem o ciclo de vida da avaliação autorizada: governança, escopo, fluxos de dados, risco, metodologia, um laboratório guiado, higiene de ferramentas, controles, monitoramento, solução de problemas, integração, automação e avaliação. Os capítulos 24–30 tratam de método de pesquisa, estúdio em equipe, passagem para operação, implantação e validação, prática de campo e o projeto final. Cada capítulo traz objetivos, seções didáticas, um exemplo resolvido, um caso sintético rotulado, erros e limites, três exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Execute cada laboratório com `python3 arquivo.py`; nenhum abre conexão de rede.

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Tidewater Regional Transit (TRT)** — operadora de ônibus e veículo leve sobre trilhos, com portal dos funcionários, API de horários, wiki interna, VPN dos funcionários e um segmento de pagamento de tarifas sempre excluído | Organização estudada ao longo do livro | Inventada |
| **Priya Natarajan** | Tecnóloga de segurança na equipe de engenharia da TRT | Inventada |
| **Northpoint Assurance** | Prestadora externa de testes contratada pela TRT | Inventada |

Todos os endereços vêm das faixas de documentação reservadas pela RFC 5737 (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24).

### Fontes principais

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide); MITRE [ATT&CK](https://attack.mitre.org/). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) |

Capítulos 10–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-10), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever as camadas de hardware, firmware, sistema operacional e aplicação de um computador nos termos de que um avaliador precisa; (2) explicar por que sistemas frágeis ou compartilhados mudam o planejamento de um teste; (3) escrever um registro de ativo que uma reunião de escopo possa usar; (4) reconhecer quando um sistema pertence a alguém que não autorizou testes.

### 1.1 Camadas que um avaliador precisa nomear

Um sistema computacional é uma pilha. Na base ficam processador, memória, armazenamento e interface de rede. Firmwares como o UEFI ou um controlador de gerenciamento da placa-mãe (BMC) dão a partida na máquina e muitas vezes continuam rodando ao lado dela. O sistema operacional agenda processos, aplica permissões de arquivo e expõe serviços. As aplicações ficam no topo e guardam os dados que interessam ao negócio. Quando um relatório de teste diz "o host", o leitor não consegue saber qual camada foi examinada; um tecnólogo nomeia a camada, porque o responsável, o caminho de correção e o risco são diferentes em cada uma.

### 1.2 Por que capacidade e fragilidade importam

O tráfego de avaliação consome recursos. Um serviço que responde a cinquenta requisições por minuto em uso normal pode se degradar quando uma ferramenta de inventário envia milhares. O NIST SP 800-115 adverte que os testes podem perturbar as operações e pede que os planejadores pesem esse risco antes de escolher as técnicas. Controladores embarcados antigos, daemons legados de thread única e storages perto do limite são as vítimas habituais. A resposta não é pulá-los em silêncio, e sim registrar a restrição e combinar com o responsável um método mais brando, como a revisão de configuração.

O primeiro diagrama de Priya para o ENG-712 separa os caminhos de internet dos passageiros dos caminhos da VPN dos funcionários antes que qualquer lista de prefixos seja montada. As premissas de confiança diferem em cada caminho, então um inventário único e plano esconderia onde a autorização precisa mudar.

### 1.3 Infraestrutura compartilhada e virtual

Muitos sistemas rodam em hardware de outra pessoa: um provedor de hospedagem, um parceiro de serviços gerenciados, uma plataforma de nuvem. O cliente pode ser dono da máquina virtual, mas não do hipervisor nem da malha de armazenamento por baixo dela. A autorização do cliente, portanto, cobre apenas o que o cliente controla. Os termos do provedor, que às vezes exigem aviso prévio e às vezes proíbem certos tipos de teste, precisam ser lidos antes do planejamento. Hospedagem compartilhada significa que a TRT pode não enxergar o hipervisor subjacente. Por isso o escopo do ENG-712 elaborado por Priya nomeia as máquinas virtuais e as URLs que a TRT controla, e não o plano de gerenciamento do provedor. Quando um achado toca a infraestrutura compartilhada, ela escala para o responsável pela nuvem em vez de sondar lateralmente. As regras de engajamento (ROE) da Northpoint repetem esse limite para que os testadores não inventem permissão.

### 1.4 O registro de ativo

Um registro útil contém: identificador, função de negócio, responsável, localização (física ou lógica), sistema operacional e versão, criticidade, fragilidade conhecida e o status de autorização para testes. Todos os capítulos seguintes se apoiam nesses campos: as verificações de escopo leem o endereço, as classificações de risco leem a criticidade, os relatórios leem o responsável. A linha de ativo de Priya para o portal dos funcionários traz responsável, criticidade e a nota de fragilidade "congelamento de mudanças às sextas". Sem esse registro, as decisões do lab_scope parecem arbitrárias. Ela atualiza a linha quando o DNS muda, porque um identificador desatualizado é o caminho pelo qual hosts OUT-OF-SCOPE acabam testados por engano.

### Exemplo resolvido

Priya inventaria o servidor de horários da TRT. Hardware: um servidor de rack com três anos de uso. Firmware: BMC do fabricante com porta de rede própria. Sistema operacional: uma versão de Linux com suporte. Aplicação: a API de horários. Ela registra o BMC como um ativo separado, porque sua porta de rede fica numa VLAN de gerenciamento que o escopo da Northpoint não menciona. A reunião de escopo terá de decidir se ele está dentro ou fora.

> **Caso sintético.** A Tidewater Regional Transit e seu servidor de horários foram inventados para este capítulo.

### Erros e limites

Tratar "o servidor" como uma coisa só esconde o firmware e as interfaces de gerenciamento. Supor que ser locatário na nuvem concede permissão sobre as camadas do provedor é um erro comum e grave. Este capítulo descreve apenas arquitetura; não explica como atacar nenhuma camada.

### Exercícios

- **EX001 — Interface oculta.** Por que um controlador de gerenciamento da placa-mãe com porta de rede própria deve aparecer como um registro de ativo próprio? *Rubrica:* 3 = interface separada, responsável/caminho de correção separados, o escopo precisa decidir explicitamente; 2 = só a interface separada; 1 = "faz parte do servidor"; 0 = nada.
- **EX002 — Daemon frágil.** Um daemon legado de planejamento de rotas cai sob carga pesada. Proponha como o plano deve tratá-lo. *Rubrica:* 3 = registrar a fragilidade, combinar com o responsável um método de menor impacto (revisão de configuração ou verificação com limitação de taxa), documentar nas ROE; 2 = excluir sem discussão; 1 = testar normalmente; 0 = nada.
- **EX003 — Limite da hospedagem.** A TRT aluga máquinas virtuais de uma empresa de hospedagem. Quais camadas a TRT pode autorizar e o que precisa ser verificado para o restante? *Rubrica:* 3 = a TRT autoriza suas VMs/aplicações; hipervisor e malha exigem termos/aviso ao provedor; 2 = em parte; 1 = a TRT autoriza tudo; 0 = nada.

### Síntese

Nomeie a camada, registre o responsável e a fragilidade, e nunca deixe a condição de locatário se passar por autoridade sobre o hardware de outra pessoa.

### Continue estudando — capítulo 01 de 30

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem

Você vai (1) ler faixas de endereços em notação CIDR; (2) separar endereços em escopo, excluídos e fora de escopo com um pequeno script; (3) explicar por que nomes DNS e endereços IP podem se descolar durante um engajamento; (4) listar os serviços de internet que uma operadora de transporte costuma expor.

### 2.1 Endereços, prefixos e propriedade

Uma rede IPv4 como 192.0.2.0/25 cobre 128 endereços, de .0 a .127. O comprimento do prefixo indica quantos bits iniciais são fixos. Documentos de escopo quase sempre listam prefixos, e não hosts isolados, então um tecnólogo precisa conseguir testar a pertinência com rapidez e sem erros de aritmética mental. Propriedade é outra questão: um prefixo anunciado por um provedor de nuvem pode conter endereços que pertencem a milhares de clientes. O lab_scope imprime 192.0.2.10 e 198.51.100.20 como IN-SCOPE dentro das faixas didáticas /25 documentadas da TRT. Priya ensina comprimento de prefixo com esses endereços da RFC 5737 para que os alunos nunca apontem ferramentas para redes de transporte reais. O responsável por cada prefixo é escrito ao lado do CIDR antes de a Northpoint receber a lista.

### 2.2 Exclusões dentro das faixas

Escopos reais costumam abrir buracos. O segmento de pagamento de tarifas da TRT, 192.0.2.64/27, fica dentro do bloco maior em escopo por causa de como a rede foi numerada historicamente. Um verificador precisa avaliar as exclusões primeiro; caso contrário, a inclusão mais ampla vence e um sistema proibido é tocado. A exceção de tarifas 192.0.2.70 EXCLUDED fica dentro de um bloco maior de propósito. O verificador de Priya precisa respeitar os buracos, e não só os prefixos externos; do contrário, o ENG-712 liberaria hosts de pagamento de tarifas. Ela demonstra a linha EXCLUDED na reunião de abertura para que a Northpoint veja que o buraco é intencional, e reprova qualquer planilha de escopo que liste apenas os CIDRs externos sem a exceção de tarifas escrita ao lado.

### 2.3 Nomes versus números

Registros DNS mudam. Um nome de host aprovado na segunda-feira pode resolver para outro endereço na quinta, depois de uma migração, talvez para um endereço compartilhado de rede de distribuição de conteúdo (CDN). A boa prática é aprovar o nome e o endereço, resolver de novo antes de cada sessão e parar se eles divergirem. Depois de uma migração para a CDN, o nome do portal dos funcionários passou a resolver fora dos endereços aprovados. Priya pausou o ENG-712, executou de novo o lab_scope e esperou uma atualização por escrito da equipe branca. Nomes, sozinhos, nunca autorizam; os números na lista assinada, sim. Enquanto a sessão fica suspensa, Priya registra capturas de tela das resoluções antiga e nova como evidência, com uma nota de HOLD, e não um palpite.

### 2.4 Serviços expostos típicos

Uma operadora de transporte costuma publicar um site para passageiros, uma API de horários ou de tempo real, um gateway de acesso remoto dos funcionários, e-mail e, às vezes, um portal de suporte de fornecedor. O ATT&CK cataloga o uso adversário de gateways de acesso remoto como T1133 External Remote Services, e é por isso que esses gateways costumam ser priorizados nas discussões de escopo. A face exposta comum da TRT é o site dos passageiros, a API de horários, a VPN dos funcionários e o e-mail — não os validadores de tarifa. As declarações de método do ENG-712 listam esses serviços explicitamente. Qualquer coisa que se pareça com fare.trt.example é recusada, mesmo que responda numa porta interessante.

### Laboratório A — verificador de escopo

```python
"""Lab A (ch 02): classify synthetic targets against a written scope. Documentation ranges only."""
import ipaddress
IN_SCOPE = [ipaddress.ip_network(n) for n in ("192.0.2.0/25", "198.51.100.16/28")]
EXCLUDED = [ipaddress.ip_network("192.0.2.64/27")]  # fare-payment segment, carved out by the client
targets = ["192.0.2.10", "192.0.2.70", "192.0.2.200", "198.51.100.20", "203.0.113.5"]
def verdict(addr):
    ip = ipaddress.ip_address(addr)
    if any(ip in n for n in EXCLUDED):
        return "EXCLUDED"
    if any(ip in n for n in IN_SCOPE):
        return "IN-SCOPE"
    return "OUT-OF-SCOPE"
for t in targets:
    print(f"{t:15} {verdict(t)}")
print("testable:", sum(verdict(t) == "IN-SCOPE" for t in targets), "of", len(targets))
```

Execute com `python3 lab_scope.py`. Saída verificada:

```text
192.0.2.10      IN-SCOPE
192.0.2.70      EXCLUDED
192.0.2.200     OUT-OF-SCOPE
198.51.100.20   IN-SCOPE
203.0.113.5     OUT-OF-SCOPE
testable: 2 of 5
```

### Exemplo resolvido

Cinco endereços candidatos chegam a Priya pela planilha de planejamento da Northpoint. O script marca 192.0.2.70 como EXCLUDED porque ele cai na exceção de pagamento de tarifas, e 192.0.2.200 como OUT-OF-SCOPE porque um /25 termina em .127. Apenas dois dos cinco são testáveis. Ela devolve a planilha com esses veredictos antes de qualquer sessão ser agendada.

> **Caso sintético.** Os endereços usam faixas de documentação da RFC 5737; o desenho da rede da TRT é fictício.

### Erros e limites

Verificar inclusões antes das exclusões, confiar na resposta DNS de ontem e confundir "o cliente usa este endereço" com "o cliente é dono dele" são as falhas clássicas. O script verifica aritmética, não autoridade legal.

### Exercícios

- **EX004 — Limite da faixa.** Usando a saída do laboratório, por que 192.0.2.200 está fora de escopo, mesmo começando com 192.0.2? *Rubrica:* 3 = o /25 cobre .0–.127, então .200 fica fora; 2 = diz que está fora sem justificar; 1 = diz que está em escopo; 0 = nada.
- **EX005 — Erro de ordem.** Suponha que um colega reescreva a função para testar IN_SCOPE antes de EXCLUDED. O que 192.0.2.70 retornaria e por que isso é perigoso? *Rubrica:* 3 = IN-SCOPE; o sistema de pagamento de tarifas seria testado; 2 = aponta o veredicto errado; 1 = nada muda; 0 = nada.
- **EX006 — Nome de host à deriva.** O nome aprovado portal.trt.example agora resolve para 203.0.113.5. O que Priya deve fazer? *Rubrica:* 3 = parar, o endereço está fora de escopo, confirmar com o responsável e reaprovar antes de testar; 2 = só parar; 1 = testar o nome mesmo assim; 0 = nada.

### Síntese

Pertinência é aritmética, as exclusões vêm primeiro, e todo nome é resolvido e verificado de novo antes do início de uma sessão.

### Continue estudando — capítulo 02 de 30

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem

Você vai (1) escrever funções Python pequenas e legíveis, cada uma tomando uma decisão; (2) usar apenas a biblioteca padrão, para que um laboratório rode em qualquer estação de trabalho aprovada; (3) testar uma função com entradas conhecidas antes de confiar nela; (4) explicar por que as ferramentas de avaliação devem falhar fechadas.

### 3.1 Por que tecnólogos programam

O trabalho de avaliação produz listas: hosts, contas, achados, itens de evidência, datas de reteste. Scripts que verificam, ordenam e resumem essas listas eliminam erros de cópia e tornam as decisões repetíveis. Não são ferramentas de ataque. Neste livro, todo script lê dados inventados guardados no próprio arquivo e imprime um veredicto. Priya automatiza as listas de hosts e de achados para que as pessoas gastem tempo com os HOLDs e a severidade, e não copiando linhas. Scripts que classificam escopo e calculam hashes de evidência estão dentro dos limites; scripts que inventam caminhos de ataque, não. O registro do operador do ENG-712 é gerado apenas a partir de ações que passaram pelo controle.

### 3.2 Uma função, uma decisão

Uma função como `verdict(addr)`, do Capítulo 2, responde a uma pergunta e devolve um pequeno conjunto de rótulos. Esse desenho a torna testável: alimente-a com um endereço cuja resposta você já conhece e compare. Quando uma função decide, imprime e grava arquivos ao mesmo tempo, um defeito numa parte se esconde nas outras. verdict(addr) devolve IN-SCOPE, EXCLUDED ou OUT-OF-SCOPE e nada mais. Essa decisão única passa por testes unitários com 192.0.2.10, 192.0.2.70 e 192.0.2.200 antes de toda janela. Uma função auxiliar que também edita o inventário que lê é reprovada na revisão de código da TRT, porque deixa de responder a uma única decisão e um defeito na edição se esconderia no veredicto.

### 3.3 Biblioteca padrão primeiro

A biblioteca padrão do Python inclui `ipaddress`, `datetime`, `hashlib`, `json`, `csv` e `collections`. Eles cobrem aritmética de escopo, janelas de tempo, hash de evidências, registros estruturados e contagens. Evitar pacotes de terceiros significa não ter revisão de dependências, não ter surpresas na cadeia de suprimentos e ter comportamento idêntico na máquina do revisor. ipaddress, datetime, hashlib e json cobrem os laboratórios didáticos do ENG-712 sem scanners de terceiros. Priya fixa a escolha da biblioteca padrão no inventário do kit, para que as discussões sobre cadeia de suprimentos tratem das ferramentas da TRT, e não de pacotes aleatórios do PyPI baixados no meio da janela. Se a Northpoint trouxer depois um scanner comercial, essa ferramenta ganha linha própria, responsável e nota de tratamento de dados.

### 3.4 Falhar fechado

Se um arquivo de escopo estiver ausente ou uma data não puder ser interpretada, o padrão seguro é "não prosseguir". Um verificador que devolve "permitido" ao encontrar uma exceção é pior do que nenhum, porque cria falsa confiança. Escreva primeiro o caminho de negação e depois acrescente as condições de permissão. Arquivos de escopo ausentes fazem o verificador falhar fechado em "não prosseguir". Devolver permitido numa exceção teria liberado 192.0.2.200 numa leitura quebrada. Os testes de Priya verificam o caminho fechado com uma fixture de arquivo apagado: remover o arquivo de escopo na integração contínua (CI) precisa resultar em não prosseguir, nunca em permitido. A fixture fica ao lado da tabela de testes do ENG-712 para que os auditores possam executar de novo o caminho fechado.

### 3.5 Testes como evidência

Uma tabela curta de entradas e saídas esperadas, executada antes de cada engajamento, é evidência de que as ferramentas se comportam. Guarde-a junto dos registros do engajamento para que um revisor possa executá-la de novo. A tabela de testes pré-engajamento de verdict() é arquivada no ENG-712 ao lado das ROE. Quando a Northpoint pergunta se a ferramenta mudou, Priya mostra a tabela executada na abertura, e não a lembrança de uma saída verde. Como a execução é anexada ao chamado antes de as ferramentas começarem, ninguém pode alegar depois que o verificador "provavelmente estava bem" sem apresentar esse artefato.

### Exemplo resolvido

Priya escreve uma função auxiliar que devolve "allowed" apenas quando uma string de data é interpretada e cai dentro da janela. Seu primeiro rascunho capturava `ValueError` e devolvia "allowed". Ela a reescreve para que a exceção devolva "STOP: unreadable time" e acrescenta três casos conhecidos — dentro, fora, malformado — a uma lista de testes executada antes do trabalho de cada noite.

> **Caso sintético.** A função auxiliar de Priya e suas entradas de teste foram inventadas para fins didáticos.

### Erros e limites

Trechos copiados de fóruns podem esconder chamadas de rede ou padrões inseguros; leia cada linha. Habilidade em programação não cria permissão para testar nada.

### Exercícios

- **EX007 — Padrão na exceção.** Um parser recebe "2026-11-31 23:00" (uma data inválida). O que um verificador de janela que falha fechado deve devolver? *Rubrica:* 3 = um rótulo de parada/negação e o motivo, nunca "allowed"; 2 = nega sem motivo; 1 = allowed; 0 = nada.
- **EX008 — Escolha da biblioteca.** Nomeie o módulo da biblioteca padrão que você usaria para calcular digests SHA-256 e um motivo para preferi-lo a um pacote de terceiros. *Rubrica:* 3 = hashlib + nenhuma dependência extra/revisão de cadeia de suprimentos/mesmo comportamento para o revisor; 2 = só o módulo; 1 = terceiros; 0 = nada.
- **EX009 — Tabela de respostas conhecidas.** Dê três entradas de teste, com as saídas esperadas, para a função `verdict` do Capítulo 2. *Rubrica:* 3 = três pares corretos cobrindo IN-SCOPE, EXCLUDED e OUT-OF-SCOPE; 2 = dois corretos; 1 = um; 0 = nada.

### Síntese

Funções pequenas, biblioteca padrão, negar por padrão e uma tabela de respostas conhecidas guardada como evidência.

### Continue estudando — capítulo 03 de 30

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem

Você vai (1) desenhar um registro mínimo para um achado; (2) validar registros quanto a campos ausentes, tipos errados e valores ilegais; (3) explicar por que vocabulários controlados tornam os relatórios comparáveis; (4) ligar achados a evidências por identificadores, e não por texto corrido.

### 4.1 Do que um registro de achado precisa

Um achado é uma afirmação: neste ativo existe esta fraqueza, demonstrada por esta evidência, com esta severidade. Os campos mínimos são, portanto, um identificador, o ativo, um ID de técnica do ATT&CK ou outra referência de fraqueza, uma severidade tirada de uma lista combinada e um ponteiro para a evidência. Responsável pela correção, prazo e status vêm mais tarde no ciclo de vida. O achado F-01 precisa de id, ativo, id de evidência, severidade e cenário antes de entrar no gerador de relatórios. O lab_records rejeita linhas incompletas. Priya não discute severidade num registro que ainda acusa evidência ausente.

### 4.2 Vocabulários controlados

Se um testador escreve "urgente", outro "P1" e um terceiro "muito ruim", ninguém consegue contar os críticos. Um conjunto fixo — `low`, `medium`, `high`, `critical` — permite que os painéis somem e comparem. IDs do ATT&CK como T1078 fazem o mesmo trabalho para o comportamento adversário: "contas válidas" escrito de cinco jeitos continua sendo uma técnica. O vocabulário da TRT é `low`, `medium`, `high`, `critical` — nunca `urgent`. O lab_records sinaliza o F-02 pela severidade urgent para que os painéis continuem contáveis. Os redatores da Northpoint recebem as mesmas quatro palavras no apêndice das ROE, para que os painéis da TRT continuem comparáveis entre prestadores e entre engajamentos.

### 4.3 Identificadores em vez de texto corrido

A evidência é ligada por um ID como E-001, e não por "veja a captura de tela de terça". IDs sobrevivem a renomeação, tradução e cópia para um sistema de chamados. Cada ID precisa ser único dentro do engajamento. No ENG-712, o F-09 aponta para o E-002 pelo identificador, então renomear o PNG ou exportar a wiki para outro formato não quebra a ligação. Os sistemas de chamados recebem os identificadores inalterados quando os achados são copiados. Antes de o gerador de relatórios rodar, referências de chat como a captura de tela da wiki são reescritas como identificadores de evidência, para que cada afirmação do rascunho aponte para um arquivo específico.

### 4.4 Validação como controle de passagem

Os registros são validados antes de entrar no relatório. Um validador que lista todos os problemas, em vez de parar no primeiro, economiza idas e vindas com o testador. O validador lista todos os problemas de um registro numa única passada. Evidência ausente no F-03 e uma severidade inválida em outra linha aparecem juntas antes que o autor reescreva. As idas e vindas diminuem quando o controle é completo: no primeiro ensaio do ENG-712, um validador que parava no primeiro problema custou um dia de vaivém com os autores da Northpoint.

### Laboratório B — validador de registros

```python
"""Lab B (ch 04): validate synthetic finding records against a minimal schema."""
REQUIRED = {"id": str, "asset": str, "technique": str, "severity": str, "evidence": str}
SEVERITIES = {"low", "medium", "high", "critical"}
records = [
    {"id": "F-01", "asset": "trt-portal", "technique": "T1078", "severity": "high", "evidence": "E-001"},
    {"id": "F-02", "asset": "trt-wiki", "technique": "T1213", "severity": "urgent", "evidence": "E-002"},
    {"id": "F-03", "asset": "trt-vpn", "technique": "T1133", "severity": "medium"},
]
for r in records:
    problems = [f"missing {k}" for k in REQUIRED if k not in r]
    problems += [f"{k} not {t.__name__}" for k, t in REQUIRED.items() if k in r and not isinstance(r[k], t)]
    if r.get("severity") and r["severity"] not in SEVERITIES:
        problems.append(f"bad severity '{r['severity']}'")
    print(r["id"], "OK" if not problems else "; ".join(problems))
```

Execute com `python3 lab_records.py`. Saída verificada:

```text
F-01 OK
F-02 bad severity 'urgent'
F-03 missing evidence
```

### Exemplo resolvido

A Northpoint entrega três achados em rascunho. O F-01 passa. O F-02 usa "urgent", que não está na lista combinada de severidades. O F-03 não tem ponteiro de evidência, então nada sustenta a afirmação. Priya devolve o F-02 e o F-03 com as mensagens do validador e aceita o F-01 no controle de achados.

> **Caso sintético.** Esses três achados e seus ativos são exemplos fictícios da TRT.

### Erros e limites

Um esquema garante forma, não verdade: um registro bem formado ainda pode descrever algo que nunca aconteceu. Mantenha o vocabulário curto; graus demais de severidade produzem discussão em vez de ação.

### Exercícios

- **EX010 — Afirmação sem sustentação.** Segundo o laboratório, o que há de errado com o F-03 e por que isso o impede de entrar no relatório? *Rubrica:* 3 = falta evidência; um achado sem evidência não pode ser verificado; 2 = só nomeia o problema; 1 = diz OK; 0 = nada.
- **EX011 — Conserto do vocabulário.** Como a severidade do F-02 deve ser corrigida e quem decide o valor? *Rubrica:* 3 = mapear para um nível combinado (por exemplo, high/critical), pelo testador com concordância do revisor, usando o método de classificação; 2 = só escolhe um valor; 1 = acrescentar "urgent" à lista; 0 = nada.
- **EX012 — Campo extra.** Proponha um campo adicional para a fase de correção e justifique-o numa frase. *Rubrica:* 3 = campo sensato (responsável, prazo, status, data de reteste) com justificativa; 2 = só o campo; 1 = campo irrelevante; 0 = nada.

### Síntese

Um achado é uma afirmação estruturada, com vocabulário fixo e um ponteiro de evidência; valide antes de relatar.

### Continue estudando — capítulo 04 de 30

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) distinguir avaliação de vulnerabilidades, teste de intrusão e red team; (2) enunciar em palavras simples os objetivos de confidencialidade, integridade e disponibilidade; (3) explicar a diferença entre a existência de um controle e sua eficácia; (4) explicar por que é a autorização, e não a habilidade, que separa o teste do crime.

### 5.1 Três tipos de avaliação

Uma avaliação de vulnerabilidades enumera fraquezas conhecidas de forma ampla e costuma parar na identificação. Um teste de intrusão tenta, dentro de limites combinados, confirmar se as fraquezas podem de fato ser usadas e aonde elas levam. Um exercício de red team emula um agente de ameaça específico por um período mais longo para testar a detecção e a resposta como um todo, muitas vezes com apenas uma pequena "equipe branca" ciente dele. O NIST SP 800-115 descreve revisão, identificação e análise de alvos e validação de vulnerabilidades dos alvos como famílias de técnicas; o PTES descreve fases que vão do pré-engajamento ao relatório.

### 5.2 CIA em palavras operacionais

Confidencialidade: só as pessoas certas leem os rascunhos de horários e os registros dos funcionários. Integridade: ninguém altera a escala de motoristas da semana seguinte sem deixar rastro. Disponibilidade: os passageiros recebem as chegadas em tempo real quando precisam delas. Todo achado deve dizer qual dessas propriedades ameaça, porque isso orienta quem se importa e com que urgência. Para a TRT, a confidencialidade cobre os rascunhos da escala de funcionários; a integridade cobre a veracidade dos horários; a disponibilidade cobre a informação aos passageiros no horário de pico. Priya classifica o F-01, de administrador compartilhado, como risco de integridade e disponibilidade, e não como uma caça a troféus de confidencialidade.

Falhas de integridade dos horários no pico prejudicam os passageiros mesmo quando nenhum dado pessoal vaza. O texto de Priya sobre o F-01 começa por esse enquadramento operacional de CIA para o CISO.

### 5.3 Existência versus eficácia

Uma política que exige autenticação multifator existe no papel. A eficácia só se demonstra quando um avaliador observa que as contas de fato não conseguem entrar sem o segundo fator. Avaliações medem eficácia; auditorias muitas vezes param na existência. As duas importam, mas um relatório precisa dizer qual delas mediu. O ENG-712 não usa o PDF da política como prova de nada. Ele inclui um caminho de login observado no portal dos funcionários que ainda aceitava senha sem segundo fator, registrado como evidência antes de ser classificado. O relatório declara que se tratou de uma verificação de eficácia, para que o leitor não confunda a citação de uma política com prova de que o MFA funciona.

### 5.4 A autorização é a linha

A mesma atividade — verificar se uma conta está protegida — é um serviço quando existe permissão por escrito e um crime em muitas jurisdições quando não existe. A habilidade não muda isso. O Capítulo 10 trata dos documentos que criam a permissão. Priya só abre o ENG-712 depois que o fluxo de aprovação do CISO foi assinado, e o carimbo de tempo da assinatura é a primeira linha do pacote do engajamento. A Northpoint não pode começar discretamente em clones de homologação antes que essa linha exista, por mais ansiosos que estejam seus testadores. Qualquer atividade anterior à assinatura é tratada como não autorizada, mesmo que a mesma verificação viesse a ser permitida depois.

### Exemplo resolvido

Um gerente da TRT pede a Priya "um pen test rápido da VPN antes de sexta". Ela pergunta que decisão o resultado vai apoiar. A necessidade real é confirmar que as contas de ex-terceirizados foram desativadas — uma pergunta de eficácia sobre um controle. Ela propõe uma revisão direcionada de contas em vez de um teste de intrusão, que exige escopo, acordo e uma janela que a sexta-feira não pode oferecer.

> **Caso sintético.** O pedido do gerente e a VPN da TRT são fictícios.

### Erros e limites

Chamar toda varredura de "pen test" infla a garantia. Os rótulos variam entre fornecedores; leia o que foi efetivamente feito.

### Exercícios

- **EX013 — Nomeie o serviço.** Um conselho quer saber se o SOC perceberia um intruso realista ao longo de seis semanas. Qual tipo de avaliação serve e por quê? *Rubrica:* 3 = exercício de red team; testa detecção/resposta ao longo do tempo contra um perfil de ameaça; 2 = só o tipo; 1 = varredura de vulnerabilidades; 0 = nada.
- **EX014 — Controle de papel.** A política da TRT diz que todos os logins na VPN exigem MFA. Que evidência mostraria eficácia, e não apenas existência? *Rubrica:* 3 = registros de login observados/amostrados ou contas de teste mostrando o segundo fator aplicado em todos os caminhos; 2 = observação vaga; 1 = o documento da política; 0 = nada.
- **EX015 — Mudança na escala.** Qual propriedade da CIA é ameaçada se a escala de motoristas puder ser alterada sem rastro, e quem deve ser avisado primeiro? *Rubrica:* 3 = integridade; o responsável pelas operações/pela escala e o líder de segurança; 2 = só integridade; 1 = disponibilidade; 0 = nada.

### Síntese

Escolha o tipo de avaliação pela decisão que ela precisa apoiar, meça a eficácia e lembre que a permissão é a única linha entre a prática e o dano.

### Continue estudando — capítulo 05 de 30

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem

Você vai (1) nomear os artefatos de sistema operacional que um avaliador costuma pedir; (2) explicar como a virtualização muda as premissas de isolamento; (3) descrever por que snapshots e imagens de referência importam para a correção; (4) recusar pedidos que impliquem intrusão ao vivo num hipervisor de produção sem permissão do provedor.

### 6.1 O que um sistema operacional expõe

Um sistema operacional guarda contas, listas de processos, serviços em escuta, inventários de pacotes, logs e arquivos de configuração. Na avaliação autorizada, essas são fontes de evidência quando o acordo permite o acesso. Um tecnólogo que entende onde cada fonte fica pode pedir exportações em vez de sessões interativas, o que reduz o risco operacional e ainda produz artefatos verificáveis. Para as máquinas convidadas da TRT, a evidência de sistema operacional consiste em listas de pacotes, serviços em escuta e logs de autenticação coletados sob as ROE. Priya não extrai a memória de processos por curiosidade. Os equipamentos de tarifa continuam intocados, mesmo quando aparecem na mesma VLAN de um desenho.

### 6.2 Estado de correções e de configuração

Um sistema operacional com suporte e com as correções em dia é diferente de uma versão sem suporte que não recebe mais atualizações de segurança. A configuração também importa: um serviço que escuta em todas as interfaces, uma senha guardada num arquivo em texto claro, um host protegido por firewall com uma porta de gerenciamento sem uso deixada aberta. Esses são fatos de configuração, não receitas de exploração, e aparecem nos achados como evidência de lacunas de controle. Máquinas convidadas sem suporte na VLAN dos funcionários viram achados com responsáveis; as que estão corrigidas e atualizadas, não. A deriva de configuração — um RDP aberto que o lab_ports marcaria como NOT APPROVED em outro lugar — é registrada junto com o estado dos pacotes, e não numa lista folclórica separada.

### 6.3 Virtualização e destino compartilhado

As máquinas convidadas compartilham um hipervisor, o armazenamento e às vezes uma malha de rede. O isolamento é uma propriedade do desenho da plataforma e do cuidado com que ela foi configurada. Um achado de que uma máquina convidada alcança a interface de gerenciamento de outra é uma questão da plataforma, e não apenas do sistema operacional convidado. Os termos dos provedores costumam proibir testar o hipervisor de dentro de uma máquina convidada; esse limite precisa ser escrito em todo engajamento de nuvem ou hospedagem.

Hipervisores compartilhados significam que um teste ruidoso pode afetar os vizinhos. Os limites de taxa e os ensaios a seco do ENG-712 existem em parte porque os hosts da TRT ficam numa malha compartilhada. Priya registra o destino compartilhado na página de risco residual.

### 6.4 Snapshots para a correção

Quando uma correção é aplicada, um snapshot do estado conhecido e bom permite que os operadores revertam se a mudança quebrar algo. Snapshots também congelam um momento para revisão posterior, mas podem conter segredos. Guarde-os sob as mesmas regras de acesso das demais evidências e apague-os quando o acordo mandar. No ENG-712, o plano de reteste de 2026-12-08 nomeia os snapshots pós-correção da máquina convidada do portal, para que o reteste compare a mesma build que foi corrigida. Sem eles, uma disputa sobre se o F-01 está VALIDATED pode virar uma discussão sobre qual build foi examinada. Os snapshots são guardados e apagados sob as mesmas regras de acesso e retenção das demais evidências.

### Exemplo resolvido

Priya pede à equipe de sistemas operacionais uma exportação do inventário de pacotes das VMs do portal dos funcionários, e não um shell. O inventário mostra uma biblioteca sem suporte usada por uma ferramenta auxiliar. O achado cita a exportação do inventário como evidência, lista a técnica T1195 Supply Chain Compromise do ATT&CK como padrão adversário relacionado para discussão posterior e recomenda um caminho de atualização. Nenhuma sessão interativa foi necessária.

> **Caso sintético.** O inventário de pacotes e a biblioteca sem suporte foram inventados para a TRT.

### Erros e limites

Uma lista de pacotes é um artefato de um momento; pode estar desatualizada no dia seguinte. Acesso à máquina convidada nunca implica acesso ao hipervisor. Este capítulo não descreve como escapar de uma máquina virtual.

### Exercícios

- **EX016 — Exportação em vez de shell.** Dê dois motivos para preferir uma exportação do inventário de pacotes a um shell interativo numa VM de produção. *Rubrica:* 3 = menor risco operacional + evidência reproduzível; 2 = um motivo; 1 = o shell é sempre melhor; 0 = nada.
- **EX017 — Linha do hipervisor.** A Northpoint pede para "verificar o hipervisor em busca de falhas de isolamento" de dentro de uma máquina convidada. O que Priya responde? *Rubrica:* 3 = recusa; está fora da autoridade da TRT; exige autorização e termos do provedor; 2 = só recusa; 1 = permite; 0 = nada.
- **EX018 — Segredo no snapshot.** Um snapshot de correção de uma VM do portal contém uma senha de serviço em texto claro. Como ele deve ser tratado? *Rubrica:* 3 = tratar como evidência/segredo; restringir o acesso; trocar a senha; apagar/devolver conforme o acordo; 2 = restringir o acesso; 1 = deixar no armazenamento comum; 0 = nada.

### Síntese

Prefira exportações, respeite o limite do hipervisor e trate os snapshots ao mesmo tempo como ferramentas de recuperação e como possíveis depósitos de segredos.

### Continue estudando — capítulo 06 de 30

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem

Você vai (1) descrever autenticação, autorização e registro de atividades (accounting) como decisões separadas; (2) explicar por que contas compartilhadas e remanescentes aparecem com tanta frequência nas avaliações; (3) mapear fraquezas comuns de identidade para IDs de técnica do ATT&CK; (4) desenhar uma lista de verificação de privilégio mínimo para um portal dos funcionários.

### 7.1 Três decisões

A autenticação responde "quem é este?". A autorização responde "o que pode fazer?". O registro de atividades responde "o que fez?". Um sistema que autentica com rigor, mas autoriza todo mundo como administrador, resolveu apenas a primeira pergunta. Os achados devem dizer qual decisão falhou. No portal da TRT, as três podem falhar de forma independente: uma senha correta usada com um papel remanescente de terceirizado continua sendo um achado. Os papéis de VPN remanescentes do F-07 mostram deriva de autorização enquanto a autenticação ainda funciona, e a falta de trilha de registro pertence à mesma família de achados. Priya pontua cada decisão separadamente no texto, para que os responsáveis saibam qual controle corrigir.

### 7.2 Contas compartilhadas e remanescentes

Senhas compartilhadas para "a conta de operações" destroem a responsabilização: ninguém sabe quem a usou. Contas remanescentes de terceirizados e ex-funcionários são uma fonte clássica de acesso inesperado. O ATT&CK cataloga o uso adversário de credenciais legítimas como T1078 Valid Accounts e a criação de novas contas como T1136 Create Account. Mapear um achado para esses IDs permite que os defensores procurem os mesmos padrões em seus próprios logs. Senhas de operações compartilhadas destroem a perna do registro de atividades; o F-07 acompanha as contas de VPN de ex-terceirizados pelo mesmo motivo. O ENG-712 recomenda contas nominais e datas de revogação, e não mais um segredo compartilhado.

### 7.3 Multifator e caminhos de recuperação

Um segundo fator aumenta o custo de senhas roubadas. Os caminhos de recuperação — redefinição por SMS, liberação pelo service desk, códigos de backup — precisam ser protegidos no mesmo nível, ou viram a porta fraca. A geração de pedidos de MFA (ATT&CK T1621) é uma técnica adversária contra fatores por notificação push; isso é uma questão de desenho para exercícios de purple team, não uma deixa para desativar o MFA. Quando as ROE permitem, a declaração de método de Priya inclui uma revisão dos caminhos de recuperação do portal dos funcionários, incluindo a redefinição por SMS e a liberação pelo service desk. Um desenho forte de MFA com um processo fraco de redefinição é registrado como achado, e não ignorado. A revisão fica no nível de configuração e de processo e não envolve disparar pedidos push para funcionários reais.

### 7.4 Privilégio mínimo como lista de verificação

Para cada papel no portal dos funcionários: liste as ações de que ele precisa, remova o resto e registre quem pode conceder exceções. A lista de verificação é evidência de que a autorização foi desenhada, e não herdada. O privilégio mínimo dos papéis do portal é uma lista de verificação escrita e assinada pelo responsável pela aplicação. As exceções registram quem as concedeu e quando expiram. A lista é anexada como evidência ao lado do F-01; uma lista sem assinatura não conta como evidência de privilégio mínimo. A cada reteste, Priya relê a lista de exceções, porque uma exceção vencida que ainda concede direitos é, ela mesma, um achado.

### Exemplo resolvido

Priya revisa a lista de contas de VPN da TRT. Três contas pertencem a terceirizados cujos contratos terminaram há meses. Ela registra um achado sob T1078, com a evidência E-010 (a exportação das contas com as datas do último login), e recomenda a desativação mais uma revisão trimestral. Ela não tenta usar as contas.

> **Caso sintético.** As contas remanescentes de terceirizados são exemplos fictícios da TRT.

### Erros e limites

Listar contas não é o mesmo que provar que elas podem ser usadas; essa etapa exige autorização explícita. Não guarde senhas recuperadas em chamados.

### Exercícios

- **EX019 — Qual decisão?** Um portal permite que qualquer funcionário autenticado edite o horário público. Qual dos três (AAA) falhou e qual é a direção da correção? *Rubrica:* 3 = autorização; restringir a edição a um papel de publicador; 2 = só autorização; 1 = autenticação; 0 = nada.
- **EX020 — Mapeamento no ATT&CK.** Mapeie "contas de VPN de ex-terceirizados ainda ativas" para um ID e um nome de técnica. *Rubrica:* 3 = T1078 Valid Accounts; 2 = só T1078 ou só Valid Accounts; 1 = ID errado; 0 = nada.
- **EX021 — Caminho de recuperação.** Nomeie uma fraqueza de caminho de recuperação capaz de anular o MFA e uma mitigação. *Rubrica:* 3 = por exemplo, redefinição fraca pelo service desk / interceptação de SMS / códigos de backup desprotegidos + a mitigação correspondente; 2 = nomeia a fraqueza; 1 = desativar o MFA; 0 = nada.

### Síntese

Separe quem, o quê e o que foi feito; aposente as contas remanescentes; mapeie os achados de identidade para o ATT&CK, para que os defensores possam caçá-los.

### Continue estudando — capítulo 07 de 30

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) desenhar um diagrama de fronteiras de confiança para um serviço pequeno; (2) explicar a defesa em profundidade sem tratá-la como slogan; (3) posicionar controles de rede, de identidade e de aplicação nesse diagrama; (4) identificar onde a evidência da avaliação deve ser coletada.

### 8.1 Fronteiras de confiança

Uma fronteira de confiança é um lugar onde as premissas mudam: da internet para a DMZ, da DMZ para a rede interna, da aplicação para o banco de dados, do dispositivo do funcionário para a VPN. Atravessar uma fronteira deve exigir um controle — autenticação, criptografia, um gateway, um filtro. Diagramas que omitem as fronteiras escondem os lugares onde os achados mais importam. O diagrama de Priya mostra internet, DMZ, portal e diretório como mudanças distintas de premissa, cada uma com seu próprio controle. O pagamento de tarifas fica atrás de outro gateway e é um domínio de confiança diferente, então nunca herda permissões do portal por aparecer perto dele num slide. O escopo segue essas fronteiras, e não uma lista plana de endereços que por acaso respondem.

### 8.2 Defesa em profundidade como camadas com propósito

Profundidade significa camadas independentes que falham de maneiras diferentes. Uma VPN, um login de aplicação e uma permissão de banco de dados são três camadas. Se todas dependem do mesmo repositório de senhas, são uma camada usando três chapéus. Um avaliador procura pontos únicos de falha compartilhados com o mesmo cuidado com que procura camadas ausentes. Uma repetição purple no ENG-712 mostrou a VPN e o portal falhando juntos no mesmo modo de indisponibilidade do diretório. Se as três camadas desabam quando o diretório cai, a profundidade é apenas aparente. Por isso as recomendações incluem controles de sessão independentes, e não mais uma camada que dependa do mesmo repositório de senhas.

### 8.3 Onde a evidência mora

A evidência de rede mora nos logs dos gateways e, quando autorizado, em capturas de pacotes. A evidência de identidade mora nos logs de autenticação. A evidência de aplicação mora nos logs de acesso e nas exportações de configuração. Saber onde pedir poupa acessos interativos de que ninguém precisa. No ENG-712, o plano de evidências nomeia os logs dos gateways, os logs de autenticação do diretório e os logs de acesso do portal antes de a janela abrir, junto com quem vai exportar cada um. Capturas de pacotes precisam de uma linha própria e explícita nas ROE, porque podem coletar muito mais dados pessoais do que um achado exige. Priya não inicia capturas em enlaces compartilhados por iniciativa própria, mesmo quando um log parece incompleto.

### 8.4 Arquitetura e escopo

O escopo deve seguir a arquitetura. Se o segmento de pagamento de tarifas fica atrás de um gateway diferente, com responsáveis diferentes, ele é outro domínio de confiança e, em geral, outro engajamento. Misturar domínios num só relatório confunde a correção. Como o pagamento de tarifas é um domínio de confiança separado, as exclusões do ENG-712 nomeiam 192.0.2.64/27 e fare.trt.example. O parágrafo de exclusão é lido em voz alta na abertura e rubricado pelos responsáveis pela arquitetura, e qualquer divergência sobre onde fica a fronteira é resolvida por escrito antes de as ferramentas rodarem. Um parágrafo de exclusão que ninguém rubricou é tratado como não lido.

### Exemplo resolvido

Priya esboça o portal dos funcionários da TRT: internet → proxy reverso → servidores de aplicação → banco de dados; um caminho paralelo para VPN dos funcionários → jump host de gerenciamento → a mesma camada de aplicação. Ela marca o proxy e o jump host como controles de fronteira de confiança. O segmento de pagamento de tarifas é desenhado numa página separada com a nota "fora de escopo". Os testadores da Northpoint usam o esboço para planejar quais logs vão pedir.

> **Caso sintético.** O esboço de arquitetura e seus componentes são inventados.

### Erros e limites

Diagramas bonitos que inventam sistemas que a organização não tem desperdiçam tempo. Profundidade não é "mais ferramentas"; são modos de falha independentes.

### Exercícios

- **EX022 — Marcação de fronteira.** No esboço de Priya, nomeie duas fronteiras de confiança e um controle em cada. *Rubrica:* 3 = duas fronteiras distintas com controles correspondentes (por exemplo, internet→proxy com TLS/autenticação; VPN→jump host com MFA); 2 = uma completa; 1 = vago; 0 = nada.
- **EX023 — Falha compartilhada.** A VPN, o portal e o banco de dados aceitam a mesma senha do Active Directory, sem MFA. Por que isso não são três camadas? *Rubrica:* 3 = um repositório de credenciais/um segredo; comprometer esse segredo derrota as três; 2 = aponta a senha compartilhada; 1 = continuam sendo três camadas; 0 = nada.
- **EX024 — Lugar da evidência.** Onde Priya procuraria primeiro a evidência de que um login na VPN dos funcionários ocorreu às 02:00? *Rubrica:* 3 = logs da VPN/de autenticação (evidência de identidade); 2 = logs vagos; 1 = banco de dados; 0 = nada.

### Síntese

Desenhe as fronteiras, confira se as camadas falham de forma independente e colete a evidência no lugar onde o controle realmente mora.

### Continue estudando — capítulo 08 de 30

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Evidência e medição

### Objetivos de aprendizagem

Você vai (1) escrever uma nota de cadeia de custódia para um artefato digital; (2) calcular e verificar um manifesto SHA-256; (3) explicar por que a medição precisa de uma unidade e de uma janela de tempo definidas; (4) recusar-se a guardar evidências do engajamento em dispositivos pessoais.

### 9.1 A evidência sustenta uma afirmação

Um achado sem evidência é uma opinião. A evidência pode ser uma exportação de configuração, uma captura de tela com dados ocultados, um trecho de log ou o hash de um arquivo. Capture apenas o que prova o ponto; mais dados significam mais risco de retenção e mais trabalho de ocultação. No ENG-712, a afirmação sobre o banner do portal entra no relatório porque o E-001 tem um digest correspondente. Uma opinião sobre o banner sem esse arquivo é apagada na revisão por pares. Priya captura evidências apenas em sistemas autorizados e mascara a parte local dos e-mails dos funcionários antes de arquivar, para que a evidência prove o ponto sem acrescentar risco de retenção.

### 9.2 Cadeia de custódia

Para cada item, registre quem o coletou, quando, de onde e cada repasse. O NIST SP 800-86 descreve a integração de técnicas forenses à resposta a incidentes; a mesma disciplina de rotulagem e verificação de integridade vale para a evidência de avaliação, mesmo quando o que está em jogo juridicamente é menor. As linhas de custódia do ENG-712 nomeiam quem exportou o E-001, quando e de qual host. Os repasses para Jordan, como responsável pelas evidências, são registrados. Os hábitos do NIST SP 800-86 se transferem mesmo quando o caso é sintético. Uma linha de custódia ausente bloqueia a exportação para o pacote do conselho, mesmo quando o hash confere.

### 9.3 Hash como verificação de adulteração

Um digest SHA-256 de um artefato, guardado separadamente do artefato, permite que um leitor posterior detecte edições silenciosas. Se o digest não confere mais, o arquivo mudou — de propósito ou não — e a afirmação que dependia dele precisa ser revista. O laboratório mostra E-001 MATCH e E-002 MISMATCH. A divergência suspendeu uma afirmação sobre uma senha na wiki até que a exportação fosse refeita sob revisão de duas pessoas. Os digests ficam guardados ao lado dos arquivos de evidência, e não apenas numa conversa de chamado que qualquer um pode editar, para que um leitor posterior ainda consiga conferi-los.

### Laboratório C — manifesto de evidências

```python
"""Lab C (ch 09): build a SHA-256 evidence manifest for synthetic artefacts and detect tampering."""
import hashlib
artefacts = {
    "E-001_portal_login_banner.txt": b"TRT staff portal - authorised users only\n",
    "E-002_wiki_page_export.txt": b"Runbook draft v3 (synthetic)\n",
}
manifest = {name: hashlib.sha256(data).hexdigest() for name, data in artefacts.items()}
for name, h in manifest.items():
    print(f"{h[:16]}...  {name}")
artefacts["E-002_wiki_page_export.txt"] = b"Runbook draft v4 (synthetic)\n"  # simulated later edit
for name, data in artefacts.items():
    ok = hashlib.sha256(data).hexdigest() == manifest[name]
    print(name, "MATCH" if ok else "MISMATCH")
```

Execute com `python3 lab_hash.py`. Saída verificada:

```text
3b5ca57a4755e156...  E-001_portal_login_banner.txt
ce711fb5a92e12ef...  E-002_wiki_page_export.txt
E-001_portal_login_banner.txt MATCH
E-002_wiki_page_export.txt MISMATCH
```

### 9.4 Medir exige unidades

"Varremos muita coisa" não é uma medida. "Sete técnicas do ATT&CK exercitadas entre 22:00 e 05:00; três geraram alerta, duas foram registradas em log, duas passaram despercebidas" é uma medida. O Capítulo 19 constrói uma matriz de cobertura; este capítulo apenas insiste em que os números tenham unidades e janelas. O slide purple do ENG-712 usa exatamente essas contagens para as sete técnicas. Um percentual de cobertura sem unidades ou janela levaria o CISO a comparar números que significam coisas diferentes. Com contagens por categoria, a conversa sobre investimento pode partir das duas técnicas não detectadas e perguntar que fonte de log ou alerta fecharia cada lacuna.

### Exemplo resolvido

Priya calcula o hash de duas exportações sintéticas antes de arquivá-las. Mais tarde, alguém "atualiza" a exportação da wiki. A verificação do manifesto imprime MISMATCH para esse arquivo e MATCH para o banner intocado. Ela trata a exportação da wiki como não confiável até que uma cópia nova seja obtida sob custódia.

> **Caso sintético.** Os dois artefatos e a edição posterior foram inventados para o laboratório.

### Erros e limites

Hashes detectam mudança; não provam que o original era verdadeiro. Aplicativos de chat pessoais e notebooks pessoais não são repositórios de evidência.

### Exercícios

- **EX025 — Resultado do manifesto.** Usando a saída do laboratório, qual arquivo divergiu e o que isso significa para um achado que o citava? *Rubrica:* 3 = a exportação da wiki E-002; a evidência do achado precisa ser coletada de novo ou o achado suspenso; 2 = nomeia o arquivo; 1 = ignorar a divergência; 0 = nada.
- **EX026 — Linha de custódia.** Escreva uma entrada de custódia de uma linha para a exportação do banner do portal. *Rubrica:* 3 = quem, o quê, quando, de onde; 2 = dois campos; 1 = vago; 0 = nada.
- **EX027 — Notebook pessoal.** Priya pode guardar durante a noite uma cópia da evidência da TRT no notebook de casa? *Rubrica:* 3 = não; apenas no repositório aprovado, conforme o acordo; 2 = não; 1 = sim, se estiver criptografado; 0 = nada.

### Síntese

Minimize, rotule, calcule o hash, meça com unidades e nunca estacione evidências em dispositivos pessoais.

### Continue estudando — capítulo 09 de 30

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX027 (as de EX028–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). A Tidewater Regional Transit, Priya Natarajan, a Northpoint Assurance e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O BMC é acessível por uma porta de rede própria, recebe correções pelo firmware do fabricante e não pelo sistema operacional, e pode ficar numa VLAN de gerenciamento fora do escopo escrito. Um registro separado obriga a reunião de escopo a incluí-lo ou excluí-lo explicitamente.

**EX002.** Registrar no registro de ativo a fragilidade de cair sob carga, combinar com o responsável um método de menor impacto, como a revisão de configuração ou uma verificação com forte limitação de taxa numa janela supervisionada, e escrever esse limite nas regras de engajamento.

**EX003.** A TRT pode autorizar testes nas próprias máquinas virtuais, sistemas operacionais e aplicações. O hipervisor, o armazenamento e a malha de rede pertencem à empresa de hospedagem, então seus termos de serviço precisam ser lidos e qualquer aviso exigido precisa ser dado antes do planejamento.

**EX004.** Um /25 fixa os primeiros 25 bits, então 192.0.2.0/25 vai de .0 a .127. O endereço .200 fica na metade superior do /24, que não está listada, por isso o laboratório imprime OUT-OF-SCOPE.

**EX005.** Devolveria IN-SCOPE, porque 192.0.2.70 também está dentro de 192.0.2.0/25. O segmento de pagamento de tarifas que o cliente excluiu seria então testado, violando o acordo.

**EX006.** Parar de testar esse nome. 203.0.113.5 está fora de todos os prefixos aprovados; Priya confirma com o responsável pelo sistema o que mudou e obtém reaprovação por escrito para o novo endereço antes de qualquer trabalho adicional.

**EX007.** Deve devolver um rótulo de parada como "STOP: unreadable time". Novembro tem 30 dias, então a string não pode ser interpretada; um horário ilegível nunca deve ser tratado como dentro da janela.

**EX008.** `hashlib`. Ele vem com o Python, então não exige revisão de dependências, não introduz risco de cadeia de suprimentos e dá resultados idênticos ao revisor.

**EX009.** 192.0.2.10 → IN-SCOPE; 192.0.2.70 → EXCLUDED; 203.0.113.5 → OUT-OF-SCOPE (qualquer trio equivalente que cubra os três rótulos recebe 3).

**EX010.** O validador imprime `missing evidence`. Sem um identificador de evidência, nenhum revisor consegue verificar a afirmação, então ela não pode aparecer como achado até que a evidência seja anexada.

**EX011.** Substituir "urgent" por um de low/medium/high/critical. O testador propõe o nível usando o método de classificação combinado (Capítulo 13) e o revisor o confirma; o vocabulário em si não é ampliado.

**EX012.** Exemplo: `owner` — a pessoa ou equipe nomeada e responsável pela correção, para que o controle de correções possa encaminhar e cobrar o achado. Prazo, status ou data de reteste com justificativa também recebem 3.

**EX013.** Um exercício de red team. Ele emula um agente de ameaça definido ao longo de semanas, com pouca ciência por parte dos defensores, então mede a detecção e a resposta como um todo em vez de listar fraquezas.

**EX014.** Registros de login amostrados em todos os caminhos de entrada da VPN, ou contas de teste autorizadas, mostrando que nenhuma sessão foi estabelecida sem o segundo fator. A política escrita prova apenas que o controle existe.

**EX015.** Integridade. A equipe de operações responsável pela escala e o líder de segurança da TRT devem ser avisados primeiro, porque uma alteração silenciosa poderia colocar o motorista errado numa linha.

**EX016.** Uma exportação evita o acesso interativo que poderia perturbar uma VM de produção e produz um artefato reproduzível que um revisor pode reexaminar sem reabrir um shell.

**EX017.** Ela recusa. Testar o hipervisor está fora da condição de locatária da TRT; exige autorização por escrito do provedor de hospedagem, sob seus termos, o que o engajamento atual não inclui.

**EX018.** Guardar o snapshot sob as regras de acesso às evidências, trocar imediatamente a senha exposta e apagar ou devolver o snapshot quando terminar o prazo de retenção do acordo.

**EX019.** Falhou a autorização: a autenticação funcionou para muitas pessoas, mas o privilégio de edição era amplo demais. Restringir a edição de horários a um papel nomeado de publicador e registrar cada mudança.

**EX020.** T1078 Valid Accounts — credenciais legítimas que não deveriam mais funcionar continuam utilizáveis.

**EX021.** Exemplo: um procedimento de redefinição de senha no service desk que aceita nome e número de matrícula por telefone, sem retorno de ligação. Mitigar com comprovação de identidade mais forte e um segundo canal. Interceptação na redefinição por SMS ou códigos de backup desprotegidos, com as mitigações correspondentes, também recebem 3.

**EX022.** Exemplo: (1) internet → proxy reverso — terminação TLS e autenticação no proxy reverso; (2) VPN dos funcionários → jump host — MFA e acesso de gerenciamento por lista de permissões. Pares distintos equivalentes recebem 3.

**EX023.** As três dependem do mesmo segredo no mesmo diretório. Roubar ou adivinhar essa senha atravessa todas as camadas de uma vez, então a profundidade é ilusória.

**EX024.** O gateway da VPN ou o log central de autenticação — a evidência de identidade para esse caminho. Logs de aplicação ou de banco de dados podem mostrar atividade posterior, mas não provam o login na VPN em si.

**EX025.** `E-002_wiki_page_export.txt` imprime MISMATCH. Qualquer achado que citava essa exportação precisa ficar suspenso até que uma cópia nova seja coletada sob custódia e tenha o hash recalculado; o arquivo alterado deixou de ser evidência confiável.

**EX026.** Exemplo: "2026-11-03 21:40 Priya Natarajan exportou o banner de login do portal a partir de trt-portal, no chamado ENG-712; guardado em evidence/ENG-712/E-001_portal_login_banner.txt."

**EX027.** Não. A evidência fica no repositório aprovado do engajamento, sob as regras de acesso e retenção do acordo, e não em equipamento pessoal.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v4.0 Specification Document. <https://www.first.org/cvss/v4.0/specification-document>
- IETF RFC 5737. IPv4 Address Blocks Reserved for Documentation. <https://www.rfc-editor.org/rfc/rfc5737>
- IETF RFC 9116. A File Format to Aid in Security Vulnerability Disclosure (security.txt). <https://www.rfc-editor.org/rfc/rfc9116>
- MITRE ATT&CK Enterprise matrix and technique pages (e.g. T1078 Valid Accounts, T1133 External Remote Services, T1552.001 Credentials In Files). <https://attack.mitre.org/>
- MITRE ATT&CK Navigator. <https://mitre-attack.github.io/attack-navigator/>
- MITRE D3FEND. <https://d3fend.mitre.org/>
- NIST CSWP 29 (2024). The NIST Cybersecurity Framework (CSF) 2.0. <https://doi.org/10.6028/NIST.CSWP.29>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- NIST SP 800-30 Rev. 1 (2012). Guide for Conducting Risk Assessments. <https://doi.org/10.6028/NIST.SP.800-30r1>
- NIST SP 800-53 Rev. 5 (2020). Security and Privacy Controls for Information Systems and Organizations. <https://doi.org/10.6028/NIST.SP.800-53r5>
- NIST SP 800-61 Rev. 3 (2025). Incident Response Recommendations and Considerations for Cybersecurity Risk Management. <https://doi.org/10.6028/NIST.SP.800-61r3>
- NIST SP 800-86 (2006). Guide to Integrating Forensic Techniques into Incident Response. <https://doi.org/10.6028/NIST.SP.800-86>
- OWASP Application Security Verification Standard (ASVS). <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
