# Segurança Ofensiva Autorizada e Red Team: Um Livro para o Tecnólogo

- Idioma: português do Brasil (`pt`); curso de tecnólogo, três anos; aproximadamente 2.400 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–30 de 30 têm texto didático escrito à mão; os exercícios EX001–EX090 têm resoluções correspondentes com rubricas de 0 a 3; nove laboratórios offline usam apenas a biblioteca padrão do Python 3, e suas saídas foram incorporadas a partir de execuções reais sobre dados sintéticos. A revisão técnica independente e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

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

<a id="ch-10"></a>

## Capítulo 10 — Segurança ofensiva autorizada e red team: orientação

### Objetivos de aprendizagem

Você vai (1) situar a avaliação de vulnerabilidades, o teste de intrusão e o red team num único ciclo de vida; (2) nomear os documentos que criam a permissão; (3) explicar os papéis das equipes red, blue e purple; (4) enunciar com suas palavras o limite educacional deste livro.

### 10.1 Um ciclo de vida, não uma lista de ferramentas

A prática autorizada passa por governança e definição de escopo, regras de engajamento, execução dentro dessas regras, tratamento de evidências, classificação de risco, relatório, correção e validação. Os nomes das ferramentas mudam; o ciclo de vida, não. O NIST SP 800-115 e o PTES organizam o trabalho dessa forma, ainda que os títulos de suas partes sejam diferentes. Priya ensina o caminho que vai da governança, passando por escopo, ROE, execução, evidência, classificação e relatório, até o reteste. Nos treinamentos, os alunos que pularam direto para os scanners produziram um STOP por interação com o sistema de tarifas. A Northpoint é avaliada pela fidelidade com que seguiu o ciclo de vida antes que alguém olhe para a esperteza de seus achados.

### 10.2 A permissão é escrita

A permissão vem de um acordo assinado que nomeia as partes, os sistemas, os métodos, a janela, as exclusões, as regras de tratamento de dados, o contato de emergência e o público do relatório. Um "pode ir" verbal não basta. O Capítulo 11 transforma esse acordo em objetos de escopo e de ROE verificáveis. O pacote assinado do ENG-712 nomeia as partes, os sistemas, os métodos, a janela, as exclusões, o prazo de retenção, o contato de emergência e o telefone da equipe branca. Um contato de emergência vazio cancela o início de sábado, exatamente como ensinam os laboratórios de ROE. A retenção e o telefone da equipe branca são conferidos na mesma passada, porque cada um deles é necessário antes de qualquer atividade começar.

### 10.3 Red, blue e purple

A equipe red (ou a prestadora de testes) exercita comportamentos adversários sob autorização. A equipe blue (o SOC e os defensores) detecta e responde. O purple teaming é colaboração estruturada: a equipe red anuncia ou revela técnicas de forma controlada para que a blue melhore a detecção, com o aprendizado como objetivo, e não uma simples "pegadinha". O TIBER-EU e o CBEST acrescentam uma camada guiada por inteligência de ameaças, usada na garantia do setor financeiro; os tecnólogos devem reconhecer esses nomes mesmo quando sua organização não é um banco.

A red (Northpoint) exercita comportamentos; a blue (SOC da TRT) detecta; a purple leva o que passou despercebido para as regras DET-19 e DET-20. Priya recusa engajamentos que não prevejam uma equipe branca alcançável. O aprendizado é uma entrega, não um extra opcional.

### 10.4 O que este livro não fará

Ele não fornecerá código de exploit, payloads nem procedimentos de ataque passo a passo. Não autorizará ninguém a testar um sistema real. Ensina governança, evidência, medição e validação de correções sobre dados sintéticos, para que, quando o aluno entrar mais tarde numa equipe real, a disciplina já esteja instalada. Nada de código de exploit, nada de autorização ao vivo, nada de tarifas "só desta vez". O limite do Capítulo 10 é o que Priya cita quando uma banca pede os passos de T1552.001 — ela aponta para o ATT&CK e para por aí. A recusa é praticada em simulações de banca, e não deixada como teoria.

### Exemplo resolvido

O CISO da TRT pergunta se eles "precisam de um red team". Priya pergunta que decisão o resultado vai apoiar. O CISO quer saber se o SOC perceberia um intruso realista. Essa é uma pergunta de red team com capacidade purple, não de varredura de vulnerabilidades. Priya propõe um exercício com escopo definido, com autoridade de parada da equipe branca, ROE escritas e uma revisão de aprendizado — e lembra que o pagamento de tarifas continua excluído.

> **Caso sintético.** A conversa com o CISO foi inventada para a orientação.

### Erros e limites

Comprar um produto de "red team" que na verdade é uma varredura desperdiça dinheiro e cria falsa garantia. Nomes de frameworks num slide não equivalem a seguir suas fases.

### Exercícios

- **EX028 — Decisão primeiro.** Reescreva a necessidade do CISO como um objetivo de avaliação de uma frase. *Rubrica:* 3 = objetivo sobre a detecção, pelo SOC, de um intruso realista num exercício com escopo definido; 2 = objetivo vago; 1 = "rodar ferramentas"; 0 = nada.
- **EX029 — Lista de documentos.** Nomeie cinco campos que um acordo assinado precisa conter antes de os testes começarem. *Rubrica:* 3 = cinco entre escopo/exclusões/métodos/janela/contato de emergência/tratamento de dados/público do relatório/partes; 2 = três; 1 = um; 0 = nada.
- **EX030 — Objetivo purple.** Numa frase, o que torna um exercício "purple" em vez de uma disputa puramente competitiva entre red e blue? *Rubrica:* 3 = colaboração estruturada voltada a melhorar a detecção/resposta, e não apenas a marcar uma invasão; 2 = menciona colaboração; 1 = mais ferramentas; 0 = nada.

### Síntese

Comece pela decisão, escreva a permissão, conheça os papéis e mantenha este currículo do lado defensivo da linha.

### Continue estudando — capítulo 10 de 30

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Segurança ofensiva autorizada e red team: ativos e contexto

### Objetivos de aprendizagem

Você vai (1) transformar um acordo assinado em escopo e ROE verificáveis por máquina; (2) rejeitar atividades planejadas que caiam fora da janela ou na lista de parada; (3) explicar por que o contexto do ativo (responsável, criticidade, fragilidade) muda a escolha do método; (4) manter alcançável um contato da equipe branca.

### 11.1 Do texto aos objetos

Um acordo escrito em parágrafos se torna útil quando também é uma lista: prefixos e nomes em escopo, sistemas excluídos, atividades permitidas, horários de início e fim, atividades proibidas e um contato de emergência. Os verificadores do Capítulo 2 e deste capítulo operam sobre essas listas. Um texto ambíguo como "e sistemas relacionados" é um defeito, não um recurso. Os acordos em texto viram listas carregáveis pelos verificadores lab_scope e lab_roe. Se um campo não puder ser interpretado, o ENG-712 não começa. Priya mantém tanto as ROE narrativas quanto as listas para máquina.

### 11.2 O contexto muda o método

Um ativo de alta criticidade e frágil pode ser examinado apenas por revisão de configuração. Um clone de homologação de baixa criticidade pode aceitar verificações mais ativas. O registro de ativo do Capítulo 1 fornece esse contexto; ignorá-lo produz ou testes imprudentes ou cautela desperdiçada. Na TRT, o portal de produção, frágil, fica na revisão de configuração, enquanto um clone de homologação rotulado pode receber varreduras de inventário. Quem faz essa escolha é o campo de criticidade do registro de ativo, e não a preferência de um testador no dia. Registrar a escolha nas ROE permite que um revisor veja depois por que os dois sistemas foram tratados de forma diferente.

### 11.3 Listas de parada e janelas

Uma lista de parada nomeia atividades que nunca são permitidas, nem dentro da janela — no caso da TRT, interação com o sistema de tarifas e engenharia social contra motoristas. Uma janela nomeia quando as atividades permitidas podem rodar. As duas são controles rígidos. Na saída do laboratório, uma revisão da VPN às 06:10 devolve STOP porque a janela termina às 05:00. No estúdio, os exercícios de lista de parada usam um nome de host de tarifas falso que precisa produzir HOLD ou STOP, e não tráfego curioso. Os dois controles são verificados antes de cada ação, então um método permitido no horário errado continua sendo recusado.

### Laboratório D — verificador de atividades das ROE

```python
"""Lab D (ch 11): check synthetic planned activities against the rules-of-engagement window and stop list."""
from datetime import datetime
WINDOW = (datetime(2026, 11, 3, 22, 0), datetime(2026, 11, 4, 5, 0))
FORBIDDEN = {"denial-of-service", "social engineering of drivers", "fare-system interaction"}
plan = [
    ("2026-11-03 22:30", "external service inventory"),
    ("2026-11-04 04:45", "portal authentication review"),
    ("2026-11-04 06:10", "VPN configuration review"),
    ("2026-11-03 23:00", "fare-system interaction"),
]
for when, act in plan:
    t = datetime.strptime(when, "%Y-%m-%d %H:%M")
    if act in FORBIDDEN:
        status = "STOP: forbidden activity"
    elif not (WINDOW[0] <= t <= WINDOW[1]):
        status = "STOP: outside window"
    else:
        status = "allowed"
    print(f"{when}  {act:32} {status}")
```

Execute com `python3 lab_roe.py`. Saída verificada:

```text
2026-11-03 22:30  external service inventory       allowed
2026-11-04 04:45  portal authentication review     allowed
2026-11-04 06:10  VPN configuration review         STOP: outside window
2026-11-03 23:00  fare-system interaction          STOP: forbidden activity
```

### 11.4 Equipe branca

Alguém com autoridade de parada precisa estar alcançável durante toda a janela. Se essa pessoa não puder ser alcançada, a sessão não começa. Exercícios no estilo TIBER-EU formalizam isso como uma função de controle da equipe branca; engajamentos menores continuam precisando da mesma ideia. Silêncio da equipe branca significa não começar: se o contato de plantão não atende, as ferramentas ficam paradas e a revisão da VPN espera. As funções de controle no estilo TIBER são tomadas emprestadas como ideia, mesmo a TRT não sendo um banco. Durante o ENG-712, apenas o elo de ligação nomeado aciona a equipe branca; conversas paralelas, não.

### Exemplo resolvido

O plano preliminar da Northpoint inclui uma revisão da VPN às 06:10 e uma "interação com o sistema de tarifas" às 23:00. O laboratório imprime STOP para as duas — uma fora da janela, outra proibida. Priya cancela essas linhas antes da abertura e mantém as duas atividades permitidas.

> **Caso sintético.** As linhas do plano e a janela de 22:00–05:00 são objetos fictícios das ROE da TRT.

### Erros e limites

Um verificador não consegue inventar exclusões ausentes. Se o acordo silencia, pergunte; não presuma.

### Exercícios

- **EX031 — Duas paradas.** Cite as duas linhas STOP do laboratório e o motivo de cada uma. *Rubrica:* 3 = revisão da VPN fora da janela; interação com o sistema de tarifas proibida; 2 = uma correta; 1 = as duas permitidas; 0 = nada.
- **EX032 — Contexto frágil.** A API de horários está marcada como frágil. Qual mudança de método deve entrar nas ROE? *Rubrica:* 3 = limitar a taxa/restringir ou passar para revisão de configuração; escrito nas ROE; 2 = cautela vaga; 1 = ignorar; 0 = nada.
- **EX033 — Equipe branca inalcançável.** Na manhã da janela, o contato de plantão da equipe branca não atende. O que acontece? *Rubrica:* 3 = não começar; escalar para o CISO/substituto nomeado; recomeçar só quando o contato for confirmado; 2 = adiar; 1 = começar mesmo assim; 0 = nada.

### Síntese

Escopo e ROE são listas que se podem verificar; o contexto escolhe o método; sem equipe branca alcançável, não há início.

### Continue estudando — capítulo 11 de 30

[← Capítulo 10 (rascunho)](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 (rascunho) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Segurança ofensiva autorizada e red team: fluxos de dados

### Objetivos de aprendizagem

Você vai (1) desenhar um diagrama de fluxo de dados para um serviço da TRT; (2) marcar onde podem aparecer evidências da avaliação e dados pessoais; (3) aplicar regras de minimização e de ocultação de dados; (4) escolher armazenamento e retenção compatíveis com o acordo.

### 12.1 Fluxos, não caixas

Um diagrama de fluxo de dados mostra o que se move: um pedido de passageiro à API de horários, um login de funcionário no portal, uma linha de log para o SIEM, um backup para o armazenamento. Caixas, sozinhas, não revelam onde as cópias de dados sensíveis vão parar. Avaliações que tocam esses caminhos podem criar novas cópias; o acordo precisa dizer o que acontece com elas. Para o ENG-712, Priya desenha os fluxos passageiro→API e funcionário→portal→SIEM antes de o engajamento começar. Qualquer achado que dependa de evidência de log passa então a citar o fluxo de onde ela veio, e cada fluxo é verificado quanto a dados pessoais antes de o desenho das evidências ser aprovado. Um diagrama de caixas sem setas esconderia justamente os deveres de retenção que se aplicam quando uma linha de log é copiada para o cofre de evidências.

### 12.2 Dados pessoais e operacionais

Mesmo uma operadora de transporte guarda dados pessoais — identificadores de funcionários e, às vezes, dados de contas de passageiros em sistemas vizinhos. Dados operacionais como escalas de motoristas e cronogramas de manutenção também podem ser sensíveis. Capture o mínimo que prova um achado; mascare o resto antes de arquivar. No ENG-712, as capturas de tela de login mantêm o domínio do e-mail dos funcionários como prova, mas têm a parte local mascarada antes de entrar no cofre. Os extratos de escala são tratados como sensíveis, mesmo não sendo dados pessoais clássicos, porque revelam quem trabalha onde e quando. Os dois tipos de evidência correm no mesmo relógio de retenção de 90 dias que os banners de serviço.

### 12.3 Caminhos transfronteiriços e de fornecedores

Se os logs forem enviados a um SIEM de fornecedor em outro país, a evidência pode sair da jurisdição que o acordo pressupunha. Registre o caminho antes do engajamento; não o descubra no rascunho do relatório. Priya nomeia no acordo qualquer caminho transfronteiriço de SIEM antes do envio do primeiro log, tratando-o como um host que precisa de escopo. Se o fornecedor anunciar no meio da janela que mudou de região, o envio de logs é pausado e se faz uma reunião de decisão. Ela não inventa consentimento para uma transferência que o acordo assinado nunca previu.

### 12.4 Relógios de retenção

Inicie um relógio de retenção quando a evidência for coletada. Quando terminar o prazo do acordo, apague ou devolva os dados e registre que o fez. Depósitos indefinidos "por via das dúvidas" são um passivo. O ENG-712 corre num relógio de 90 dias que termina com apagamento ou devolução e um registro escrito de destruição que nomeia quem apagou a evidência e quando. O registro tem seu hash incluído no pacote de passagem, ao lado da mudança de controle de acesso no cofre. Guardar cópias para treinamento exigiria um novo acordo; sem ele, a lista de verificação da passagem falha.

### Exemplo resolvido

Priya mapeia o login do portal dos funcionários: navegador → proxy reverso → aplicação do portal → diretório; e um fluxo paralelo aplicação do portal → log da aplicação → SIEM. Uma captura de tela de um login com falha mostra o e-mail de um funcionário. Ela mascara a parte local antes de arquivar, mantém o domínio para provar que era uma conta de funcionário e guarda o arquivo no ENG-712 com uma nota de retenção de 90 dias tirada do acordo.

> **Caso sintético.** O fluxo de login e a captura de tela mascarada são inventados.

### Erros e limites

Uma ocultação que deixa o segredo recuperável (um recorte que ainda mostra a senha nos metadados EXIF, por exemplo) não é ocultação. Este capítulo não trata em detalhe de regimes jurídicos; siga sua assessoria jurídica e o acordo.

### Exercícios

- **EX034 — Cópia extra.** Nomeie um lugar, além do servidor de aplicação, onde um pedido à API de horários pode ser copiado, e por que isso importa para um avaliador. *Rubrica:* 3 = por exemplo, logs do proxy reverso / SIEM / CDN / WAF — cada um é um possível local de evidência e de retenção; 2 = nomeia o lugar; 1 = em lugar nenhum; 0 = nada.
- **EX035 — Escolha da máscara.** Uma captura de tela mostra o e-mail de funcionário `alex.rivera@trt.example`. O que Priya mantém e o que mascara? *Rubrica:* 3 = mascarar a parte local; manter o domínio ou um marcador de papel para provar o contexto de funcionário; 2 = mascarar tudo; 1 = manter o endereço completo; 0 = nada.
- **EX036 — Fim da retenção.** O acordo do ENG-712 fala em 90 dias. Que duas ações encerram o relógio? *Rubrica:* 3 = apagar ou devolver a evidência + registrar a destruição/devolução; 2 = uma ação; 1 = guardar para sempre; 0 = nada.

### Síntese

Siga as cópias, minimize e mascare, e encerre o relógio de retenção por escrito.

### Continue estudando — capítulo 12 de 30

[← Capítulo 11 (rascunho)](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 (rascunho) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Segurança ofensiva autorizada e red team: cenários de risco

### Objetivos de aprendizagem

Você vai (1) classificar achados com uma matriz transparente de probabilidade × impacto; (2) ordenar uma lista de achados para definir a ordem de correção; (3) escrever um cenário de risco curto que ligue ativo, técnica e consequência; (4) separar a severidade de uma fraqueza da urgência de um chamado.

### 13.1 Classificação transparente

Uma escala de probabilidade de 1 a 5 e uma de impacto de 1 a 5, multiplicadas, dão uma pontuação que qualquer pessoa pode recalcular. Faixas como critical ≥ 20, high ≥ 12, medium ≥ 6, low ≥ 0 transformam pontuações numa linguagem que os gestores reconhecem. Documente a escala no relatório para que os leitores não fiquem adivinhando. O F-09 mostra a aritmética: probabilidade 4 vezes impacto 5 dá 20, que cai na faixa crítica. Priya imprime esse cálculo no apêndice do relatório para que um diretor possa recalculá-lo em segundos. Uma pontuação que não pode ser recalculada convida à discussão sobre o julgamento do testador, em vez da discussão sobre o risco, e a revisão a rejeita.

### 13.2 Cenários ligam os pontos

"Conta de administrador compartilhada no portal dos funcionários" é uma fraqueza. O cenário acrescenta: um adversário usando T1078 Valid Accounts poderia alterar os horários públicos (integridade) e bloquear os operadores (disponibilidade). Os cenários tornam as pontuações de impacto defensáveis. No ENG-712, essa frase fica sob o F-01, ligando a conta de administrador compartilhada ao T1078 e à integridade dos horários públicos. Essa ligação explica por que o CISO deve se preocupar antes da mudança de serviço do fim de semana, e não depois dela. Achados altos sem frase de cenário são reescritos antes que o gerador de relatórios produza a tabela executiva.

### 13.3 Severidade versus urgência

Um achado crítico num host de homologação desativado pode ter baixa urgência. Um achado médio num sistema sob ataque ativo pode ter alta urgência. Os chamados levam os dois campos; reduzi-los a um único número perde informação. Priya conduz com os responsáveis uma triagem semanal que ordena os chamados primeiro pela urgência. Um achado médio num sistema que está sendo ativamente abusado pode, assim, passar à frente de um crítico num host de homologação prestes a ser desligado. Os responsáveis veem os dois valores no chamado, então a ordem é explicada, e não misteriosa.

### Laboratório E — pontuador de achados

```python
"""Lab E (ch 13): rate synthetic findings with a 1-5 likelihood x impact matrix and sort them."""
BANDS = [(20, "critical"), (12, "high"), (6, "medium"), (0, "low")]
findings = [
    ("F-01", "shared admin account on staff portal", 4, 4),
    ("F-04", "verbose error page on timetable API", 3, 1),
    ("F-07", "unreviewed VPN accounts of ex-contractors", 3, 5),
    ("F-09", "wiki page with plaintext service password", 4, 5),
]
def band(s):
    return next(name for floor, name in BANDS if s >= floor)
for fid, title, lik, imp in sorted(findings, key=lambda f: -(f[2] * f[3])):
    s = lik * imp
    print(f"{fid} L{lik} x I{imp} = {s:2d} {band(s):8} {title}")
```

Execute com `python3 lab_score.py`. Saída verificada:

```text
F-09 L4 x I5 = 20 critical wiki page with plaintext service password
F-01 L4 x I4 = 16 high     shared admin account on staff portal
F-07 L3 x I5 = 15 high     unreviewed VPN accounts of ex-contractors
F-04 L3 x I1 =  3 low      verbose error page on timetable API
```

### 13.4 A linguagem do NIST

O NIST SP 800-30 Rev. 1 descreve o risco como função de ameaça, vulnerabilidade e impacto (entre outros enquadramentos). A matriz de sala de aula é uma simplificação para ordenar o trabalho, não uma avaliação de risco corporativa completa. Priya coloca a citação do SP 800-30 sob a figura da matriz, rotulando a escala de 1 a 5 como uma simplificação didática de suas ideias. Os examinadores podem então ver de onde vem a abordagem e o que ela deixa de fora, como a análise das fontes de ameaça. Ninguém que leia o relatório deve pensar que a TRT inventou sua própria teoria de risco.

### 13.5 Comunicar as pontuações para cima

Quando Priya apresenta a lista ordenada, ela dedica mais tempo aos dois cenários do topo do que ao achado baixo. Conselhos conseguem absorver um punhado de riscos bem narrados; não conseguem absorver o despejo de uma planilha. Ela mantém a tabela completa num apêndice para os auditores e põe três frases no sumário executivo: o que importa, por quê e que decisão ela precisa nesta semana. No resumo oral do ENG-712, o F-09 e o F-01 vêm primeiro, enquanto o achado baixo de página de erro detalhada ganha uma única linha.

### Exemplo resolvido

Quatro achados da TRT entram no pontuador. A senha em texto claro na wiki (T1552.001 Credentials In Files) encabeça a lista com 20, crítica. A página de erro detalhada da API de horários pontua 3, baixa. Priya apresenta a lista ordenada ao comitê de correção, com cenários de uma frase anexados.

> **Caso sintético.** Os quatro achados e suas pontuações são inventados.

### Erros e limites

Não invente números de probabilidade sem motivo. O CVSS (veja o FIRST CVSS v4.0) pontua vulnerabilidades; o risco organizacional também precisa de um contexto que a matriz deve declarar.

### Exercícios

- **EX037 — Topo da lista.** Qual achado o laboratório classifica em primeiro lugar e qual é sua faixa? *Rubrica:* 3 = F-09, crítica (pontuação 20); 2 = só o F-09; 1 = achado errado; 0 = nada.
- **EX038 — Frase de cenário.** Escreva um cenário de risco de uma frase para o F-07 (contas de VPN de ex-terceirizados). *Rubrica:* 3 = ativo + caminho de técnica/agente + consequência para a CIA; 2 = dois dos três; 1 = repete o título; 0 = nada.
- **EX039 — Separar a urgência.** O F-04 tem severidade baixa numa API de produção que está sendo sondada a partir da internet neste momento. Que urgência você atribui e por quê? *Rubrica:* 3 = urgência elevada apesar da severidade baixa, por causa da sondagem ativa; 2 = eleva sem motivo; 1 = ignora a sondagem; 0 = nada.

### Síntese

Pontue com transparência, narre o cenário e mantenha severidade e urgência como mostradores separados.

### Continue estudando — capítulo 13 de 30

[← Capítulo 12 (rascunho)](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 (rascunho) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Segurança ofensiva autorizada e red team: métodos I

### Objetivos de aprendizagem

Você vai (1) mapear as fases do engajamento para o NIST SP 800-115 e o PTES; (2) escolher entre técnicas de revisão e de validação com base no risco; (3) escrever uma declaração de método que as ROE possam citar; (4) manter as descrições de técnicas no nível de ID do ATT&CK, sem detalhe operacional.

### 14.1 Dois mapas da mesma jornada

O NIST SP 800-115 agrupa as técnicas em revisão, identificação e análise de alvos e validação de vulnerabilidades dos alvos, envolvidas por atividades de planejamento e de pós-teste. O PTES nomeia pré-engajamento, coleta de inteligência, modelagem de ameaças, análise de vulnerabilidades, exploração, pós-exploração e relatório. Um tecnólogo não precisa decorar cada subseção; precisa situar cada atividade planejada numa fase e saber qual documento o cliente prefere. O SP 800-115 e o PTES nomeiam etapas; Priya mapeia as atividades do ENG-712 nos dois, para que a Northpoint e os auditores compartilhem o vocabulário. Os extras guiados por ameaças ficam por cima da disciplina de escopo, e não no lugar dela.

### 14.2 Revisão antes da validação

A revisão de configuração, a revisão de documentos e a revisão de logs muitas vezes respondem à pergunta com menos risco operacional do que a validação ativa. Use a validação quando a decisão realmente precisar da confirmação de que uma fraqueza é alcançável dentro dos limites combinados — e só então. No portal dos funcionários, revisar a configuração de autenticação respondeu à pergunta sobre o MFA com muito menos risco do que qualquer experimento com senhas. A validação ativa fica reservada para os casos em que a decisão do CISO depende da prova de que uma fraqueza pode de fato ser alcançada dentro das ROE. Um pedido de validação desse tipo precisa de uma declaração de decisão de uma linha antes que qualquer verificação ativa rode.

### 14.3 Declarações de método

Uma declaração de método é uma descrição curta e não procedimental: "Inventário de serviços externos dos prefixos em escopo usando scanners aprovados, nas taxas combinadas; revisão da configuração de autenticação do portal dos funcionários; sem negação de serviço, sem interação com o sistema de tarifas, sem engenharia social." Ela pertence às ROE. A declaração do ENG-712 permanece nesse nível: inventário nas taxas combinadas, revisão da autenticação do portal e as três exclusões. Instruções de exploração passo a passo não pertencem nem a este livro nem às entregas do engajamento. Na rubrica de revisão por pares, qualquer detalhe de uso dual numa declaração de método reprova o critério de segurança, por mais completo que seja o restante do pacote.

### 14.4 ATT&CK no nível de ID

Refira-se aos comportamentos como T1595 Active Scanning, T1046 Network Service Discovery, T1078 Valid Accounts. Não os expanda em passos práticos. Os defensores podem abrir as páginas do ATT&CK; os atacantes não precisam deste livro. Toda entrega aponta para as páginas de técnicas do ATT&CK em vez de colar o texto de procedimentos. Expandir esses identificadores em receitas quebraria o limite educacional definido no Capítulo 10. Um defensor que precise de mais detalhe pode seguir o link, e o relatório continua útil para o SOC sem virar um manual para atacantes.

### Exemplo resolvido

Priya redige a declaração de método para a janela de novembro da TRT. O planejamento e as ROE citam os controles de planejamento do SP 800-115. A execução lista o inventário (identificação) e a revisão de autenticação (validação da eficácia de um controle). O relatório e a validação das correções fecham o ciclo. A declaração nunca descreve como contornar a autenticação.

> **Caso sintético.** A declaração de método de novembro foi inventada para a TRT.

### Erros e limites

Copiar uma lista de métodos da ficha técnica de um fornecedor sem compará-la com o escopo produz atividade não autorizada. "Exploração", no PTES, é o nome de uma fase, não uma licença para ataques sem controle.

### Exercícios

- **EX040 — Situar na fase.** Situe "revisão da configuração de autenticação do portal dos funcionários" numa família de técnicas do SP 800-115 e numa fase do PTES. *Rubrica:* 3 = revisão ou validação (SP) + análise de vulnerabilidades ou fase equivalente do PTES, com justificativa breve; 2 = uma correta; 1 = errada; 0 = nada.
- **EX041 — Frase de método.** Escreva uma declaração de método de uma frase para o inventário dos prefixos em escopo da TRT que inclua um limite rígido. *Rubrica:* 3 = inventário + apenas o que está em escopo + limite de taxa/janela/exclusão; 2 = só o inventário; 1 = varredura ilimitada; 0 = nada.
- **EX042 — Só o ID.** Por que o livro cita o T1046 pelo ID em vez de descrever os passos da varredura? *Rubrica:* 3 = mapeamento defensivo sem ensinar procedimentos de ataque; 2 = concisão; 1 = porque os passos são secretos; 0 = nada.

### Síntese

Nomeie a fase, prefira a revisão quando ela responde, escreva o método como limites mais intenção e pare no ID da técnica.

### Continue estudando — capítulo 14 de 30

[← Capítulo 13 (rascunho)](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 (rascunho) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Segurança ofensiva autorizada e red team: laboratório guiado

### Objetivos de aprendizagem

Você vai (1) executar um pipeline de três controles que admite uma ação apenas quando alvo, horário e atividade passam; (2) manter um registro do operador com as ações admitidas; (3) explicar por que um HOLD é um sucesso, e não uma falha; (4) entregar o registro a um revisor como evidência de disciplina.

### 15.1 Três controles

Toda ação planejada tem um endereço de alvo, um carimbo de tempo e um nome de atividade. O alvo precisa estar no prefixo em escopo, o horário dentro da janela e a atividade na lista aprovada. Se qualquer controle falhar, a ação não prossegue. Na saída do Laboratório F, A2 é retida no controle de atividade e A3 no controle de alvo, então nenhuma das duas chega ao registro do operador. Priya registra as duas linhas HOLD em capturas de tela nas notas de treinamento, porque no ENG-712 os controles são o produto e a improvisação é o defeito.

### 15.2 O registro do operador

Apenas as ações que passam pelos três controles são escritas no registro do operador. O registro é a evidência de que a equipe ficou dentro do acordo. Um registro cheio de improvisação é um achado contra a própria equipe de testes. No laboratório, apenas A1 e A4 passam pelos três controles, então são as únicas entradas do registro do operador. Priya revisa o registro antes da sessão com o CISO e o compara com o histórico do chat. Qualquer ação que apareça no chat, mas não no registro, é uma ação nas sombras e vira um achado de processo contra a Northpoint.

### Laboratório F — pipeline guiado

```python
"""Lab F (ch 15): guided pipeline - an action is logged only if target, time and activity all pass."""
import ipaddress
from datetime import datetime
scope = ipaddress.ip_network("192.0.2.0/25")
window = (datetime(2026, 11, 3, 22, 0), datetime(2026, 11, 4, 5, 0))
approved = {"service inventory", "authentication review", "configuration review"}
actions = [
    ("A1", "192.0.2.12", "2026-11-03 22:15", "service inventory"),
    ("A2", "192.0.2.12", "2026-11-03 22:40", "password spraying"),
    ("A3", "192.0.2.140", "2026-11-03 23:05", "configuration review"),
    ("A4", "192.0.2.30", "2026-11-04 01:20", "authentication review"),
]
log = []
for aid, ip, when, act in actions:
    checks = {
        "target": ipaddress.ip_address(ip) in scope,
        "time": window[0] <= datetime.strptime(when, "%Y-%m-%d %H:%M") <= window[1],
        "activity": act in approved,
    }
    failed = [k for k, ok in checks.items() if not ok]
    print(aid, "PROCEED" if not failed else "HOLD (" + ",".join(failed) + ")")
    if not failed:
        log.append(aid)
print("operator log entries:", log)
```

Execute com `python3 lab_pipeline.py`. Saída verificada:

```text
A1 PROCEED
A2 HOLD (activity)
A3 HOLD (target)
A4 PROCEED
operator log entries: ['A1', 'A4']
```

### 15.3 HOLD é um recurso

A2 é retida porque "password spraying" não é uma atividade aprovada. A3 é retida porque o alvo está fora do /25. Esses HOLDs protegem a TRT e a Northpoint. Celebrar um HOLD na reunião de encerramento ensina aos juniores que a contenção é profissional. As reuniões de encerramento dão aos HOLDs e aos STOPs de pagamento de tarifas o mesmo reconhecimento que aos achados. As notas do estúdio concedem pontos por HOLDs documentados que impediram trabalho fora de escopo ou fora da janela. Juniores que escondem um HOLD para parecer produtivos são reprovados na nota do estúdio, porque escondê-lo apaga a evidência de que os controles funcionaram.

### 15.4 Uso pelo revisor

Um revisor deve conseguir repetir os controles sobre o registro. Se aparecer uma entrada que não passaria, o engajamento tem uma falha de processo, independentemente de algo "interessante" ter sido encontrado. A revisão por pares dos pacotes de treinamento do ENG-712 inclui executar de novo as verificações dos controles sobre cada entrada do registro. Se uma entrada teria sido retida, o engajamento registra uma falha de processo mesmo quando o achado relacionado parece impressionante. O processo é avaliado ao lado dos achados, então um resultado forte não consegue esconder um registro que os controles teriam rejeitado.

### Exemplo resolvido

Quatro ações candidatas entram no pipeline. A1 e A4 prosseguem; A2 e A3 ficam retidas. O registro do operador contém apenas `['A1', 'A4']`. Priya anexa essa saída aos registros do engajamento antes do fim do turno da noite.

> **Caso sintético.** As quatro ações e os resultados do pipeline foram inventados para o laboratório guiado.

### Erros e limites

O pipeline não substitui o julgamento humano sobre fragilidade ou incidentes em andamento; ele apenas aplica os três controles rígidos. Preocupações mais sutis continuam precisando de uma pessoa.

### Exercícios

- **EX043 — Motivos da retenção.** Por que A2 e A3 ficam retidas, segundo o laboratório? *Rubrica:* 3 = A2, atividade não aprovada; A3, alvo fora de escopo; 2 = uma correta; 1 = as duas prosseguem; 0 = nada.
- **EX044 — Conteúdo do registro.** O que o registro do operador contém depois da execução e por que essa lista é evidência? *Rubrica:* 3 = ['A1','A4']; prova que só ações aprovadas pelos controles foram executadas; 2 = nomeia a lista; 1 = inclui as retidas; 0 = nada.
- **EX045 — Preocupação sutil.** A API de horários é frágil, mas o alvo e a atividade de A4 são permitidos. Que passo extra uma pessoa deve dar? *Rubrica:* 3 = aplicar a limitação de taxa/nota de fragilidade das ROE ou mudar de método; confirmar com a equipe branca em caso de dúvida; 2 = cautela vaga; 1 = ignorar; 0 = nada.

### Síntese

Três controles rígidos, um registro só com o que passou e o julgamento humano ainda aplicado por cima.

### Continue estudando — capítulo 15 de 30

[← Capítulo 14 (rascunho)](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 (rascunho) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Segurança ofensiva autorizada e red team: métodos II

### Objetivos de aprendizagem

Você vai (1) contrastar o letramento em testes de aplicações web (OWASP WSTG) com métodos centrados em rede; (2) explicar o que os frameworks guiados por ameaças (TIBER-EU, CBEST) acrescentam; (3) escolher uma combinação de métodos para uma operadora de transporte que não é um banco; (4) escrever uma redação de exclusão que resista ao contato com a realidade.

### 16.1 O OWASP WSTG como catálogo

O OWASP Web Security Testing Guide organiza verificações para aplicações web: configuração, identidade, tratamento de entradas, lógica de negócio e mais. Um tecnólogo o usa como lista de verificação de cobertura para o portal dos funcionários e a API de horários, e não como licença para executar todas as verificações. Cada verificação selecionada continua precisando de uma linha nas ROE. No ENG-712, Priya marca quais áreas do WSTG foram executadas contra o portal dos funcionários, quais contra a API de horários e quais foram deixadas de fora de propósito. É esse registro que dá sentido a uma declaração de cobertura para os leitores. Um relatório que diz apenas que a equipe seguiu o WSTG não permite ao leitor saber se as verificações de lógica de negócio na API foram feitas ou puladas.

### 16.2 Garantia guiada por ameaças

O TIBER-EU e o CBEST descrevem exercícios guiados por inteligência, usados especialmente na infraestrutura do mercado financeiro. Eles acrescentam uma fase de inteligência de ameaças, uma função de controle da equipe branca e uma repetição voltada ao aprendizado. A TRT não é um banco, mas tomar emprestadas as ideias de equipe branca e de revisão de aprendizado melhora qualquer exercício de red team. As ideias do TIBER/CBEST — inteligência, equipe branca, repetição para aprendizado — são tomadas emprestadas com cautela pela TRT. Priya não alega conformidade com o CBEST para uma operadora de ônibus. Ela alega alcançabilidade da equipe branca e chamados purple, e seus slides dizem explicitamente que tomar essas ideias emprestadas não permite à TRT alegar conformidade no estilo bancário.

### 16.3 Misturar métodos sem misturar escopos

Um único engajamento pode incluir uma revisão do portal orientada pelo WSTG e um inventário de rede limitado, desde que os dois fiquem dentro do mesmo acordo e das mesmas exclusões. Acrescentar uma "olhada rápida" não declarada nos sistemas de pagamento de tarifas viola o acordo, mesmo que o método seja brando. O acordo do ENG-712 abriga tanto a revisão do portal quanto o inventário de rede, com as mesmas exclusões valendo para os dois. Uma olhada discreta num host de pagamento de tarifas continuaria sendo contato com um sistema excluído, e o verificador de escopo devolveria STOP para ela. O aumento de escopo é tratado como condição de parada, nunca como meta ousada para uma tarde tranquila.

### 16.4 Uma redação de exclusão que funciona

"Os sistemas de pagamento de tarifas, incluindo os hosts em 192.0.2.64/27 e qualquer nome de host sob fare.trt.example, estão excluídos de todas as atividades." Isso é melhor do que "sistemas sensíveis estão fora de escopo", que ninguém consegue verificar. A versão precisa pode ser carregada diretamente no verificador de escopo, que então devolve STOP para qualquer endereço em 192.0.2.64/27 ou qualquer nome sob fare.trt.example. A revisão por pares rejeita redações vagas de exclusão porque nenhuma ferramenta e nenhum revisor conseguem testar contra elas. Na abertura, strings de exclusão verificáveis são um controle tão firme quanto ter um contato de emergência nas ROE.

### Exemplo resolvido

Priya propõe para o próximo trimestre: verificações de configuração e de identidade no portal dos funcionários, orientadas pelo WSTG; inventário dos prefixos em escopo; uma repetição purple de meio dia de T1078 e T1133 com o SOC. O pagamento de tarifas continua excluído por prefixo e por padrão de nome de host. O CISO aceita a combinação porque cada peça corresponde a uma decisão.

> **Caso sintético.** A combinação trimestral é um artefato de planejamento fictício.

### Erros e limites

Citar o TIBER-EU sem um provedor de inteligência de ameaças ou uma equipe branca é teatro. Percentuais de cobertura do WSTG sem contexto de severidade enganam os conselhos.

### Exercícios

- **EX046 — Prática emprestada.** Nomeie duas ideias do TIBER-EU/CBEST que a TRT pode tomar emprestadas sem ser um banco. *Rubrica:* 3 = controle da equipe branca + revisão de aprendizado/repetição (ou desenho de cenários guiado por inteligência de ameaças); 2 = uma; 1 = alegar certificação CBEST completa; 0 = nada.
- **EX047 — Reescrita da exclusão.** Melhore "sistemas sensíveis estão fora de escopo" para o segmento de tarifas da TRT. *Rubrica:* 3 = nomeia o prefixo e/ou o padrão de nome de host e "todas as atividades"; 2 = nomeia os sistemas de forma vaga; 1 = mantém o original; 0 = nada.
- **EX048 — Seleção no WSTG.** Por que Priya poderia escolher verificações de identidade e pular o fuzzing intrusivo de lógica de negócio no primeiro engajamento do portal? *Rubrica:* 3 = limites de risco/fragilidade/ROE / necessidades da decisão; 2 = cautela vaga; 1 = sempre executar tudo; 0 = nada.

### Síntese

Escolha catálogos para a cobertura, tome emprestada dos frameworks guiados por ameaças a disciplina da equipe branca e escreva exclusões que um script consiga verificar.

### Continue estudando — capítulo 16 de 30

[← Capítulo 15 (rascunho)](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 (rascunho) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Segurança ofensiva autorizada e red team: ferramentas

### Objetivos de aprendizagem

Você vai (1) inventariar as ferramentas de avaliação com responsável, finalidade e dados tratados; (2) aplicar uma nota de controle de mudanças antes de atualizar uma ferramenta no meio do engajamento; (3) explicar o risco de cadeia de suprimentos das ferramentas de avaliação; (4) manter os laboratórios de sala de aula na biblioteca padrão do Python.

### 17.1 As ferramentas estão no escopo da governança

Tudo o que toca sistemas ou dados do cliente faz parte da superfície de ataque do engajamento — inclusive o notebook e os scanners do próprio testador. Um inventário lista cada ferramenta, quem a mantém, que dados ela guarda e se pode sair do ambiente aprovado. No ENG-712, cada notebook e cada scanner ganham uma linha no inventário que registra a criptografia de disco e por quanto tempo qualquer cache local de evidências é mantido. A evidência guardada na máquina de um testador corre no mesmo relógio de retenção que a evidência no cofre. Um notebook perdido segue o mesmo caminho de incidente que um crachá perdido, porque qualquer um dos dois pode expor dados do cliente.

### 17.2 Controle de mudanças em pleno voo

Atualizar um scanner no meio de uma janela pode mudar seu comportamento e invalidar comparações. Anote a versão na abertura; adie atualizações, a menos que a equipe branca concorde que uma correção de segurança na própria ferramenta as exige. Versões fixadas protegem as comparações de antes e depois no trabalho purple: se o scanner mudar entre as execuções, uma diferença nos resultados pode vir da ferramenta, e não dos controles do cliente. Quando uma correção de segurança na própria ferramenta não pode esperar, a equipe branca rubrica a atualização, e a rubrica fica guardada no registro ao lado da versão fixada.

### 17.3 Cadeia de suprimentos das ferramentas

O software de avaliação vem de fornecedores e de projetos de código aberto. Prefira versões assinadas, verifique os checksums quando fornecidos e evite scripts aleatórios da internet. O T1195 Supply Chain Compromise do ATT&CK costuma ser discutido como técnica adversária contra o cliente; ele também se aplica à equipe de testes. Priya verifica os checksums antes de a janela abrir, e esse passo é uma linha da lista de verificação da abertura. Um script encontrado na internet que diz apenas interpretar JSON continua sendo recusado se não for assinado nem revisado, porque rodaria numa máquina que guarda evidências do cliente. Uma ferramenta de teste comprometida poderia causar exatamente o dano que o T1195 descreve para os clientes.

### 17.4 Restrição de sala de aula

Todo laboratório deste livro usa apenas a biblioteca padrão do Python 3 e dados sintéticos. Isso é intencional: os alunos praticam a lógica de decisão sem depender de scanners comerciais nem construir ferramentas de ataque. A restrição também mantém cada laboratório reproduzível em qualquer máquina com Python 3, sem licenças nem acesso à rede. Scanners comerciais podem aparecer mais tarde no trabalho, mas chegam pela aquisição e pelo controle de mudanças da TRT, com linhas próprias no inventário e versões fixadas. As decisões praticadas aqui, sobre controles, escopo e evidência, valem sem alteração para essas ferramentas.

### Exemplo resolvido

A lista de kit da Northpoint para a TRT nomeia dois scanners de inventário (com versões fixadas), um cofre para anotações e os verificadores de ROE deste curso. Um júnior sugere acrescentar um novo "verificador de credenciais" encontrado na internet. Priya o rejeita: sem responsável, sem checksum, sem entrada no controle de mudanças, e as ROE não listam atividades de adivinhação de credenciais.

> **Caso sintético.** A lista de kit e a ferramenta rejeitada são inventadas.

### Erros e limites

Uma versão antiga fixada com uma vulnerabilidade conhecida na ferramenta também é um risco; planeje as atualizações entre engajamentos. A sincronização da saída das ferramentas com uma nuvem pessoal pode vazar evidências.

### Exercícios

- **EX049 — Campos do kit.** Nomeie quatro campos que toda entrada de ferramenta na lista de kit deve ter. *Rubrica:* 3 = quatro entre nome/versão/responsável/finalidade/dados tratados/ambiente aprovado; 2 = dois; 1 = só o nome; 0 = nada.
- **EX050 — Atualização no meio da janela.** Um fornecedor de scanner lança uma atualização de funcionalidades no segundo dia da janela. Qual é a ação padrão? *Rubrica:* 3 = adiar; manter a versão fixada; atualizar apenas com concordância da equipe branca se uma correção de segurança exigir; 2 = só adiar; 1 = atualizar imediatamente; 0 = nada.
- **EX051 — Script aleatório.** Por que recusar um script sem controle que "só verifica senhas"? *Rubrica:* 3 = sem responsável/checksum + a atividade pode estar fora das ROE + tratamento de evidências/dados desconhecido; 2 = um motivo; 1 = permitir se funcionar; 0 = nada.

### Síntese

Inventarie o kit, fixe as versões, leve a sério a cadeia de suprimentos das ferramentas e mantenha os laboratórios didáticos entediantes de propósito.

### Continue estudando — capítulo 17 de 30

[← Capítulo 16 (rascunho)](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 (rascunho) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Segurança ofensiva autorizada e red team: controles

### Objetivos de aprendizagem

Você vai (1) mapear achados comuns de avaliação para famílias de controles na linguagem do NIST SP 800-53 e do CSF 2.0; (2) distinguir controles compensatórios de controles ausentes; (3) escrever uma recomendação de correção que nomeie um controle, um responsável e uma verificação; (4) evitar prometer "segurança total".

### 18.1 Controles como respostas aos achados

Um achado é uma lacuna; um controle é a forma como a organização a fecha. O NIST SP 800-53 Rev. 5 traz famílias de controles (controle de acesso, auditoria e responsabilização, identificação e autenticação, e muitas outras). O NIST CSF 2.0 organiza os resultados em Govern, Identify, Protect, Detect, Respond e Recover. Relatórios que recomendam "tenha cuidado" não ajudam ninguém; relatórios que recomendam "aplicar MFA em todos os caminhos da VPN (controle da família IA); responsável: equipe de identidade; verificação: revisão trimestral de contas" criam trabalho.

Na linha de recomendação, os achados são mapeados para as famílias do SP 800-53 e para as funções do CSF. O F-01 aponta para controles de identidade; o T1021 que passou despercebido aponta para trabalho de detecção e resposta. Os responsáveis veem um verbo de controle, e não apenas um problema.

### 18.2 Controles compensatórios

Se o MFA ainda não puder cobrir um caminho legado, um controle compensatório pode ser um jump host com gravação de sessões e um tempo limite de sessão mais curto. Documente a compensação e o plano para removê-la. Os avaliadores devem testar se a compensação realmente funciona, e não apenas se está escrita. Toda compensação leva uma data de término e um gancho de reteste, para que não se torne permanente em silêncio. Os avaliadores verificam se o jump host realmente grava as sessões e se o tempo limite mais curto realmente encerra as sessões ociosas, em vez de aceitar o documento de desenho. Uma compensação nunca revisitada vira um risco aceito sem aprovador nomeado.

### 18.3 Detectar e responder também são controles

O trabalho purple muitas vezes descobre que a prevenção falhou, mas a detecção também. As recomendações então caem nas funções Detect e Respond: um novo alerta, um passo de runbook, um link para um playbook. O D3FEND oferece um vocabulário de técnicas defensivas que pode ficar ao lado dos IDs do ATT&CK num programa maduro. Quando o ENG-712 descobriu que a prevenção e a detecção falharam para uma técnica, o resultado foi um chamado DET e um passo de runbook, e não o conselho de monitorar mais. Os verbos do D3FEND tornam a recomendação específica o bastante para que um engenheiro de detecção aja sobre ela e para que um exercício posterior a reteste. Cada recomendação também nomeia um responsável, para chegar a alguém que possa agir.

### 18.4 Frases de garantia proibidas

"Totalmente seguro", "garantido", "à prova de ataques" e "100% de cobertura" são falsas e proibidas nos relatórios da TRT. Declarações limitadas no tempo e no escopo são a alternativa profissional. A TRT lista essas frases no apêndice das ROE, para que os fornecedores não possam alegar que não sabiam, e os rascunhos que as contêm são devolvidos até serem reescritos. A declaração substituta do ENG-712 é limitada no tempo e no escopo e diz o que foi testado, em qual janela e dentro de quais limites. A revisão confere cada rascunho em busca das frases listadas antes de o pacote chegar ao CISO, e um revisor que encontra uma delas também confere o parágrafo em volta em busca de uma afirmação ilimitada.

### Exemplo resolvido

Para o F-07 (contas de VPN de ex-terceirizados), Priya recomenda: desativar as três contas em 48 horas (Protect / controle de acesso); instituir uma revisão de admissões, mudanças e desligamentos a cada 90 dias (Govern); acrescentar um alerta no SIEM para logins na VPN de contas com contratos encerrados (Detect). Ela recusa um rascunho de fornecedor que chamava a VPN de "totalmente segura após a correção".

> **Caso sintético.** As recomendações de controle foram inventadas para o F-07 da TRT.

### Erros e limites

Os catálogos de controles são grandes; escolha os poucos que correspondem ao achado. Mapear cada achado para vinte controles gera ruído.

### Exercícios

- **EX052 — Trio de controle.** Para o F-09 (senha em texto claro na wiki), escreva controle + responsável + verificação. *Rubrica:* 3 = por exemplo, remover o segredo + cofre de segredos / responsável pela wiki / verificação por varredura ou revisão; 2 = duas partes; 1 = "conserte"; 0 = nada.
- **EX053 — Compensação.** Dê um controle compensatório para um caminho legado de VPN que ainda não suporta MFA. *Rubrica:* 3 = compensação concreta (jump host, gravação, tempo limite curto, lista de permissões) + caráter temporário; 2 = monitoramento extra vago; 1 = ignorar; 0 = nada.
- **EX054 — Frase proibida.** Reescreva "O portal agora está à prova de ataques" como uma frase profissional. *Rubrica:* 3 = garantia limitada no tempo/escopo, sem afirmações absolutas; 2 = mais branda, mas ainda absoluta; 1 = mantém "à prova de ataques"; 0 = nada.

### Síntese

Nomeie o controle, o responsável e a verificação; permita compensações temporárias; nunca venda segurança absoluta.

### Continue estudando — capítulo 18 de 30

[← Capítulo 17 (rascunho)](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 (rascunho) →](#ch-19)

<a id="ch-19"></a>

## Capítulo 19 — Segurança ofensiva autorizada e red team: monitoramento

### Objetivos de aprendizagem

Você vai (1) construir uma matriz de cobertura do ATT&CK a partir do registro de um exercício purple; (2) interpretar os resultados alerted, logged e missed; (3) propor uma melhoria de detecção para cada técnica não detectada; (4) manter a matriz restrita ao exercício.

### 19.1 Cobertura como conversa

Uma matriz de cobertura não afirma que a organização detecta "tudo". Ela mostra, para as técnicas exercitadas numa janela nomeada, se o SOC alertou, apenas registrou em log ou deixou passar. Essa conversa orienta o investimento. Os slides de cobertura da TRT abrem com as datas da janela e a lista de técnicas exercitadas, para que a matriz não possa ser lida como uma declaração sobre tudo. Qualquer alegação de detecção universal é apagada na revisão, porque sete técnicas numa noite não conseguem sustentá-la. As discussões sobre investimento usam então as três palavras alerted, logged e missed, que apontam diretamente para o que precisa ser construído.

### 19.2 Alerted, logged, missed

Alerted significa que uma pessoa ou um playbook foi notificado a tempo de agir. Logged significa que a telemetria existia, mas ninguém foi acordado. Missed significa que o comportamento não deixou telemetria utilizável. Logged não é sucesso se o exercício pressupunha um analista respondendo. Os líderes do SOC às vezes leem logged como "funcionou em parte", então Priya o explica em relação ao objetivo do exercício. Se o exercício pressupunha que um analista responderia, uma técnica apenas registrada em log conta como falha para esse objetivo. Ela ainda abre um chamado DET, mesmo com a telemetria existindo, porque ninguém agiu a tempo.

### Laboratório G — matriz de cobertura

```python
"""Lab F (ch 19): ATT&CK technique coverage matrix from a synthetic purple-team log."""
log = [
    ("T1078", "Initial Access", "alerted"), ("T1133", "Initial Access", "logged"),
    ("T1087", "Discovery", "missed"), ("T1069", "Discovery", "alerted"),
    ("T1021", "Lateral Movement", "missed"), ("T1213", "Collection", "logged"),
    ("T1567", "Exfiltration", "alerted"),
]
order = ["alerted", "logged", "missed"]
for tid, tactic, outcome in log:
    print(f"{tid:6} {tactic:17} " + " ".join("X" if o == outcome else "." for o in order))
n = len(log)
for o in order:
    k = sum(1 for _, _, x in log if x == o)
    print(f"{o:8} {k}/{n} = {100 * k / n:.1f}%")
```

Execute com `python3 lab_coverage.py`. Saída verificada:

```text
T1078  Initial Access    X . .
T1133  Initial Access    . X .
T1087  Discovery         . . X
T1069  Discovery         X . .
T1021  Lateral Movement  . . X
T1213  Collection        . X .
T1567  Exfiltration      X . .
alerted  3/7 = 42.9%
logged   2/7 = 28.6%
missed   2/7 = 28.6%
```

### 19.3 Da falha ao backlog

Cada técnica não detectada vira um item de backlog: qual fonte de log, qual lógica de alerta, qual responsável, qual teste para prová-lo depois. Ligue o item ao ID do ATT&CK para que os exercícios futuros possam retestar a mesma célula. O DET-19 e o DET-20 seguem esse padrão para o T1021 e o T1087: cada um nomeia a fonte de log, a lógica de alerta, um responsável e um plano de reteste. A etiqueta do ATT&CK permite que o próximo ciclo purple encontre a mesma célula. Uma falha registrada sem etiqueta tende a cair na fila errada e nunca é retestada.

### 19.4 Navigator e D3FEND

O ATT&CK Navigator visualiza camadas de cobertura. O D3FEND nomeia técnicas defensivas que podem contrapor uma dada técnica ofensiva. Juntos, ajudam um tecnólogo a falar com as equipes red e blue sem inventar um vocabulário particular. Priya importa para o Navigator o conjunto de técnicas efetivamente exercitadas no ENG-712, em vez de exibir um mapa de calor corporativo genérico. Os links do D3FEND ficam nas células onde uma recomendação é feita. Um mapa de calor que não reflete o conjunto exercitado é rejeitado como decoração, porque sugere uma cobertura que ninguém mediu.

### 19.5 Retestar as mesmas células

Uma matriz de cobertura só se justifica se o exercício seguinte reabrir as mesmas células. Priya etiqueta o DET-19 e o DET-20 com T1021 e T1087 para que o ciclo purple seguinte possa imprimir uma linha de antes e depois. Sem essa disciplina, a organização redescobre as mesmas falhas e as chama de nova descoberta. Exercitar técnicas novas e interessantes não desculpa pular as células que falharam da última vez. Se essas linhas ainda mostrarem uma falha, os itens de backlog são reabertos com seus responsáveis.

### Exemplo resolvido

O registro purple da TRT cobre sete técnicas. Três geraram alerta (42.9%), duas foram registradas em log (28.6%), duas passaram despercebidas (28.6%). As falhas são o T1087 Account Discovery e o T1021 Remote Services. Priya abre dois chamados de backlog: envio dos logs de auditoria do diretório ao SIEM para o T1087 e alertas de sessão no jump host para o T1021.

> **Caso sintético.** O registro de sete técnicas e os percentuais são inventados.

### Erros e limites

Uma matriz de um único exercício não é uma pontuação de maturidade corporativa. Não esconda as falhas para poupar sentimentos; o aprendizado é o produto.

### Exercícios

- **EX055 — Percentuais.** Cite os três percentuais de resultado impressos pelo laboratório. *Rubrica:* 3 = alerted 42.9%, logged 28.6%, missed 28.6%; 2 = dois corretos; 1 = um; 0 = nada.
- **EX056 — Item de backlog.** Escreva o título de um chamado de backlog para a falha do T1021. *Rubrica:* 3 = nomeia o T1021 + objetivo de detecção/alerta + sistema (jump host/serviços remotos); 2 = chamado de detecção vago; 1 = "esforce-se mais"; 0 = nada.
- **EX057 — Logged ≠ concluído.** Por que um resultado "logged" para o T1133 não basta se o exercício esperava um analista respondendo? *Rubrica:* 3 = telemetria sem notificação/resposta não cumpre o objetivo de detectar e responder; 2 = parcial; 1 = logged é sucesso; 0 = nada.

### Síntese

Meça o que este exercício exercitou, diga a verdade sobre as falhas e transforme cada falha numa tarefa de detecção nomeada.

### Continue estudando — capítulo 19 de 30

[← Capítulo 18 (rascunho)](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 (rascunho) →](#ch-20)

<a id="ch-20"></a>

## Capítulo 20 — Segurança ofensiva autorizada e red team: solução de problemas

### Objetivos de aprendizagem

Você vai (1) construir uma árvore de falhas para uma sessão de avaliação que falhou; (2) separar falhas de ferramenta, de escopo e de ambiente; (3) escrever uma nota de go/no-go depois de um incidente no meio da janela; (4) manter as notas de solução de problemas como evidência do engajamento.

### 20.1 Sessões falham por motivos banais

Deriva de DNS, um certificado de testador vencido, um coletor do SIEM fora do ar, o telefone da equipe branca no silencioso, uma planilha de escopo com erro de digitação — isso interrompe o trabalho com mais frequência do que problemas exóticos. Uma árvore de falhas começa com "a sessão não pode prosseguir" e se ramifica em autorização, conectividade, ferramentas e segurança. Priya dedica a essas falhas comuns os primeiros trinta minutos de qualquer sessão travada do ENG-712: confere se os nomes ainda resolvem para os endereços aprovados, se os certificados dos testadores são válidos, se o coletor do SIEM está recebendo e se o telefone da equipe branca toca. Só quando as quatro verificações estão saudáveis a equipe procura algo incomum. A maioria das sessões travadas termina na primeira ou na segunda verificação.

### 20.2 Três classes de falha

Falhas de escopo: o alvo deixou de estar aprovado. Falhas de ferramenta: o verificador ou o scanner se comporta mal. Falhas de ambiente: o sistema do cliente está instável ou já há um incidente em andamento. Classificar uma falha de ambiente como falha de ferramenta leva a "tentar de novo" quando a atitude certa é parar. Cada classe tem um responsável diferente: as falhas de escopo vão para a equipe branca, as de ferramenta para o líder do kit da própria Northpoint e as de ambiente para as operações da TRT. A nota de go/no-go de Priya nomeia a classe para que a pessoa certa seja acionada. Registrar uma falha de ambiente como falha de ferramenta faria a Northpoint insistir contra um sistema que as operações estão tentando estabilizar.

### 20.3 Go / no-go

Depois de qualquer evento inesperado — uma queda, uma reclamação, uma indisponibilidade do SIEM —, a equipe escreve uma nota curta de go/no-go: o que aconteceu, qual a classe da falha, quem foi informado, a decisão, assinatura/horário. No-go é um resultado profissional. Durante uma indisponibilidade do SIEM, por exemplo, a equipe pausa o tráfego e escreve a nota antes de enviar qualquer coisa a mais, porque uma atividade que o SOC não consegue ver produz ruído sem valor de evidência. A nota registra o carimbo de tempo da última técnica observada normalmente. Esse carimbo mantém honestas as contagens do exercício purple quando a sessão é retomada.

### 20.4 Incidente paralelo

Se o SOC da TRT já está tratando um incidente real, a atividade de avaliação que acrescenta ruído costuma ser suspensa. O NIST SP 800-61 Rev. 3 discute a coordenação da resposta a incidentes; as equipes de avaliação precisam saber como recuar. As ROE de Priya para o ENG-712 declaram explicitamente o caminho de suspensão, incluindo quem manda a Northpoint recuar e quem depois diz que ela pode retomar. O caminho é ensaiado no estúdio com um acionamento falso do SOC antes do engajamento real. Acrescentar ruído de avaliação enquanto os analistas trabalham num incidente real disputaria a atenção de que o incidente precisa.

### Exemplo resolvido

Às 23:10, a API de horários começa a dar timeout. A ferramenta de inventário da Northpoint é a primeira a ser culpada. A árvore de falhas de Priya pergunta se algum outro cliente relatou a indisponibilidade — sim, o NOC relatou, antes de a taxa de varredura aumentar. Classificação: falha de ambiente (fragilidade preexistente). Decisão: no-go para verificações ativas; continuar apenas com revisão de documentos, depois da aprovação da equipe branca.

> **Caso sintético.** O timeout das 23:10 e o relato do NOC são inventados.

### Erros e limites

Notas de solução de problemas que culpam pessoas, e não sistemas, envenenam a confiança no trabalho purple. Não esconda um no-go da página de limitações do relatório.

### Exercícios

- **EX058 — Classifique.** O relógio do notebook de um testador está errado, e o verificador de ROE marca todas as ações como fora da janela. Qual é a classe da falha e a primeira correção? *Rubrica:* 3 = ferramenta (ou ambiente local do testador); corrigir o relógio/NTP; executar de novo o verificador; 2 = só a classe; 1 = falha de escopo; 0 = nada.
- **EX059 — Recuar.** O SOC declara uma investigação ativa de ransomware (sintética). O que a equipe de avaliação faz? *Rubrica:* 3 = suspender a atividade ruidosa; avisar a equipe branca; esperar a retomada por escrito; 2 = pausa vaga; 1 = continuar discretamente; 0 = nada.
- **EX060 — Campos do go/no-go.** Liste cinco campos que uma nota de go/no-go deve conter. *Rubrica:* 3 = cinco entre evento/horário/classe/pessoas informadas/decisão/assinatura; 2 = três; 1 = um; 0 = nada.

### Síntese

Primeiro a árvore, depois a classificação, escreva a decisão e recue quando a organização já estiver apagando um incêndio.

### Continue estudando — capítulo 20 de 30

[← Capítulo 19 (rascunho)](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 (rascunho) →](#ch-21)

<a id="ch-21"></a>

## Capítulo 21 — Segurança ofensiva autorizada e red team: integração de serviços

### Objetivos de aprendizagem

Você vai (1) situar o serviço de avaliação entre os serviços de identidade, logs, chamados e gestão de mudanças; (2) definir interfaces de passagem com responsáveis e SLAs; (3) explicar por que os achados da avaliação precisam entrar no mesmo controle que os demais riscos; (4) evitar TI paralela para evidências e chamados.

### 21.1 A avaliação como serviço

Uma capacidade de avaliação autorizada é um serviço com entradas (pedidos, acordos), processos (execução com escopo) e saídas (achados, relatórios, resultados de reteste). Ela depende de identidade (quem pode aprovar), de logs (para onde vai a evidência da atividade), de chamados (onde os achados moram) e de gestão de mudanças (quando as correções entram em produção). Desenhar essas dependências impede que a equipe de avaliação invente ferramentas paralelas que ninguém mais acompanha. Tratar o trabalho como serviço muda o que Priya mede. Ao lado das contagens de críticos, ela acompanha o tempo de fila entre um pedido de parada e a confirmação da equipe branca, e a taxa de achados reabertos depois do reteste. Uma prestadora com muitos críticos, mas confirmações lentas e reaberturas frequentes, pode servir pior à TRT do que uma mais discreta.

### 21.2 Interfaces e SLAs

Cada interface precisa de um responsável e de uma expectativa de resposta: confirmação da equipe branca em até quinze minutos após um pedido de parada; confirmação do chamado de correção em até dois dias úteis; acesso ao repositório de evidências revogado em até um dia após o encerramento do engajamento. SLAs sem responsáveis são enfeites. No ENG-712, essas expectativas estão escritas no acordo, cada uma com um responsável nomeado, e Priya as acompanha durante o engajamento. Uma confirmação perdida aparece como dívida de processo na folha de avaliação assinada. Uma interface sem responsável tende a virar um lugar onde pedidos de parada e chamados ficam sem resposta.

### 21.3 Um único controle de riscos

Achados que vivem só num PDF nunca encontram seus responsáveis. Exporte-os para o controle de riscos ou de vulnerabilidades da organização, com o mesmo vocabulário de severidade exigido no Capítulo 4. Mantenha o PDF como narrativa; mantenha o controle como fila de trabalho. No ENG-712, o F-01 e o F-07 existem como chamados no controle antes de qualquer apresentação de slides ser montada, usando as mesmas palavras de severidade do relatório. Uma apresentação que chega antes dos chamados é devolvida sem publicação. O controle é onde moram os responsáveis e os prazos, então um achado que nunca chega a ele nunca é corrigido.

### 21.4 TI paralela

Drives pessoais, canais de chat não gerenciados e quadros privados "só para este engajamento" viram o lugar onde a evidência vai morrer — ou vazar. Use os serviços aprovados, mesmo quando parecem mais lentos. A regra cobre também os arquivos temporários: uma captura de tela salva numa pasta da área de trabalho chamada evidence_tmp está fora do cofre e de seu relógio de retenção. Auditorias semanais do cofre verificam por amostragem notebooks e drives compartilhados em busca dessas pastas paralelas durante o engajamento. A regra de canal discreto do Capítulo 25 vale da mesma forma, então evidências e detalhes das ROE circulam apenas por serviços aprovados.

### Exemplo resolvido

Priya integra as saídas da Northpoint ao controle da TRT: cada achado vira um chamado com ID do ATT&CK, severidade, responsável e prazo; o relatório em PDF é anexado. O cofre de evidências concede à Northpoint um acesso com prazo, que expira no fim da retenção. O SOC recebe um convite de calendário para a repetição purple antes de a janela abrir, e não depois.

> **Caso sintético.** O padrão de integração foi inventado para o cenário de ferramentas da TRT.

### Erros e limites

Uma integração que inunda o SOC com ruído bruto de scanner ensina as pessoas a ignorar chamados. Filtre e classifique os achados antes que entrem no controle.

### Exercícios

- **EX061 — Responsável pela interface.** Nomeie três interfaces da avaliação e um papel responsável para cada uma. *Rubrica:* 3 = três interfaces distintas com papéis (por exemplo, equipe branca/CISO, controle/gestão de vulnerabilidades, cofre/engenharia de segurança); 2 = duas; 1 = uma; 0 = nada.
- **EX062 — Só o PDF.** Por que um relatório em PDF, sozinho, é uma integração fraca? *Rubrica:* 3 = sem fila de trabalho/responsável/prazo; os achados empacam; 2 = difícil de pesquisar; 1 = o PDF basta; 0 = nada.
- **EX063 — Quadro paralelo.** Um testador cria um Trello privado para os achados da TRT. O que Priya deve exigir em vez disso? *Rubrica:* 3 = usar o controle aprovado da TRT; exportar/migrar; desativar o quadro privado; 2 = só migrar; 1 = permitir o quadro privado; 0 = nada.

### Síntese

Trate a avaliação como um serviço com interfaces nomeadas, um único controle e nenhum depósito paralelo.

### Continue estudando — capítulo 21 de 30

[← Capítulo 20 (rascunho)](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 (rascunho) →](#ch-22)

<a id="ch-22"></a>

## Capítulo 22 — Segurança ofensiva autorizada e red team: automação

### Objetivos de aprendizagem

Você vai (1) automatizar tabelas de relatório e contagens de status a partir de achados estruturados; (2) decidir quais etapas precisam continuar humanas; (3) aplicar limites de taxa e opções de ensaio a seco (dry-run) a qualquer automação que possa tocar sistemas; (4) versionar os scripts de automação junto com o engajamento.

### 22.1 Automatize as partes tediosas e inspecionáveis

Montar uma tabela Markdown a partir de uma lista de achados, contar abertos versus corrigidos, ordenar por severidade — isso é ideal para scripts. Eles reduzem os erros de cópia e produzem artefatos idênticos para o revisor. A regra prática de Priya é que um script pode reorganizar o que uma pessoa já decidiu, mas não pode decidir nada sozinho. Ordenar quatro achados por severidade é seguro porque as severidades foram definidas durante a validação; adivinhar a severidade de um registro que não a tem, não. Quando o gerador e uma tabela feita à mão divergem, a diferença é tratada como defeito num dos dois e rastreada antes de o rascunho sair.

### Laboratório H — gerador de relatório

```python
"""Lab G (ch 22): build a Markdown executive table from synthetic findings."""
from collections import Counter
findings = [
    {"id": "F-01", "sev": "high", "status": "open", "tid": "T1078"},
    {"id": "F-04", "sev": "low", "status": "accepted", "tid": "T1190"},
    {"id": "F-07", "sev": "high", "status": "open", "tid": "T1133"},
    {"id": "F-09", "sev": "critical", "status": "fixed", "tid": "T1552"},
]
rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}
print("| ID | Severity | ATT&CK | Status |")
print("|---|---|---|---|")
for f in sorted(findings, key=lambda f: (rank[f["sev"]], f["id"])):
    print(f"| {f['id']} | {f['sev']} | {f['tid']} | {f['status']} |")
c = Counter(f["status"] for f in findings)
print(f"open={c['open']} fixed={c['fixed']} accepted={c['accepted']}")
```

Execute com `python3 lab_report.py`. Saída verificada:

```text
| ID | Severity | ATT&CK | Status |
|---|---|---|---|
| F-09 | critical | T1552 | fixed |
| F-01 | high | T1078 | open |
| F-07 | high | T1133 | open |
| F-04 | low | T1190 | accepted |
open=2 fixed=1 accepted=1
```

### 22.2 Mantenha pessoas nos controles

Decisões de autorização, acionamentos da equipe branca, disputas de severidade e notas de go/no-go continuam humanos. Automatizar "aprovar escopo" é como as organizações acabam autorizando, sem querer, o prefixo errado. A linha é traçada nas decisões que mudam quem ou o que pode ser tocado. Um script pode avisar a equipe branca de que um cartão planejado mira um endereço fora da lista de escopo assinada, mas só uma pessoa nomeada pode dizer se o cartão para ou se o escopo é emendado. Propostas de automatizar a aprovação de escopo no ENG-712 são encerradas com uma referência a esta regra, em vez de serem debatidas a cada vez.

### 22.3 Ensaio a seco e limites de taxa

Qualquer automação capaz de enviar tráfego precisa de um modo de ensaio a seco que imprima o que ela faria e de um limite de taxa combinado nas ROE. Os laboratórios de sala de aula nunca enviam tráfego; as ferramentas de produção precisam mostrar a mesma disciplina. O ensaio a seco de uma ferramenta do ENG-712 lista cada endereço de alvo, o cartão de método a que pertence e a taxa de envio planejada, para que a equipe branca possa compará-lo com as ROE assinadas antes que qualquer coisa saia do notebook. Quando as ROE pedem prova de que as taxas foram respeitadas, essa lista impressa é arquivada com as demais evidências do engajamento e mantida pelo mesmo prazo de retenção.

### 22.4 Versione com o engajamento

Guarde a versão exata do script (hash do commit ou hash do arquivo) no registro do engajamento, para que um revisor possa regenerar a tabela depois. Arquivos "final_final_v3.py" sem versão não são evidência. Priya registra um SHA-256 do gerador ao lado de cada tabela gerada, do mesmo jeito que faz no exemplo resolvido. Meses depois, um auditor pode executar de novo o script com hash sobre o JSON arquivado e conferir que a tabela do relatório é idêntica. Um arquivo chamado final_v3.py sem hash não pode ser ligado a nenhuma tabela, então a revisão do arquivo o rejeita, por mais arrumada que a saída pareça.

### 22.5 O que não raspar

Uma automação que puxa senhas de produção, cookies de sessão ou dados pessoais para um gerador de relatórios é um incidente de tratamento de dados prestes a acontecer. O gerador deste capítulo lê apenas os campos que uma pessoa já registrou como achados. Se um campo estiver ausente, o script deve falhar ruidosamente em vez de inventar uma severidade padrão. O padrão seguro é um gerador que só aceita os campos de um achado registrado: identificador, título, severidade, status e responsável. Testes de integração contínua o alimentam com fixtures sintéticas, incluindo registros deliberadamente quebrados e sem severidade, para provar que ele para com erro. Um gerador que fosse buscar cookies ou senhas em consoles transformaria uma conveniência de relatório num incidente de tratamento de dados sob o acordo.

### Exemplo resolvido

Priya executa o gerador de relatório sobre quatro achados sintéticos. Ele imprime primeiro o F-09, crítico, depois os dois altos, depois o baixo, e resume open=2 fixed=1 accepted=1. Ela cola a tabela no rascunho do relatório e registra o SHA-256 do script ao lado do anexo.

> **Caso sintético.** Os quatro achados e a tabela impressa são inventados.

### Erros e limites

Uma automação que descarta em silêncio os achados de severidade desconhecida é um defeito; falhe ruidosamente. Não feche chamados automaticamente a partir de um scanner sem revisão humana.

### Exercícios

- **EX064 — Ordem da tabela.** Na saída do laboratório, qual achado aparece primeiro e por quê? *Rubrica:* 3 = F-09; crítico fica acima de alto/baixo; 2 = só o F-09; 1 = lógica de ordenação errada; 0 = nada.
- **EX065 — Controle humano.** Nomeie duas decisões que não devem ser automatizadas no processo da TRT. *Rubrica:* 3 = duas entre autorizar escopo / disputa de severidade / go-no-go / parada pela equipe branca; 2 = uma; 1 = automatizar tudo; 0 = nada.
- **EX066 — Evidência de versão.** Como Priya deve provar qual script gerou a tabela? *Rubrica:* 3 = guardar o commit ou o SHA-256 do script junto com o engajamento; 2 = nota de versão vaga; 1 = lembrar; 0 = nada.

### Síntese

Automatize tabelas e contagens; mantenha a autorização humana; faça ensaio a seco de tudo o que toca sistemas; versione os scripts.

### Continue estudando — capítulo 22 de 30

[← Capítulo 21 (rascunho)](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 (rascunho) →](#ch-23)

<a id="ch-23"></a>

## Capítulo 23 — Segurança ofensiva autorizada e red team: avaliação

### Objetivos de aprendizagem

Você vai (1) definir os critérios de avaliação antes de um engajamento terminar; (2) pontuar a qualidade do processo separadamente da contagem de achados; (3) conduzir uma revisão de lições aprendidas que produza itens de backlog; (4) recusar métricas de vaidade.

### 23.1 Critérios antes do encerramento

A avaliação responde: ficamos no escopo, atendemos à decisão de que o CISO precisava, os defensores aprenderam, a correção começou? Escreva esses critérios nas ROE ou nas notas da abertura, para que o seu eu do futuro não invente critérios mais brandos depois de uma semana bagunçada. No ENG-712, as quatro perguntas foram escritas nas notas da abertura como itens de sim ou não: ficou no escopo, apoiou a decisão do CISO sobre cobertura, deu aos defensores algo a aprender, iniciou a correção. Priya as preenche antes de o CISO ler a folha, e a contagem de achados aparece apenas como linha de apoio, para que um apêndice longo não possa substituir um critério não cumprido.

### 23.2 Qualidade do processo ≠ contagem de troféus

Um engajamento que não encontra nada, mas demonstra controles sólidos, evidências limpas e uma repetição purple útil, pode ser um sucesso. Um engajamento que encontra dezenas de problemas ignorando as exclusões é um fracasso com um apêndice longo. Pontue a disciplina explicitamente. A rubrica de estúdio de Priya põe isso na primeira página, porque os estudantes tendem a se medir pelo tamanho da tabela de achados. No ENG-712, um engajamento discreto, com controles limpos e uma repetição purple útil, ainda teria cumprido os quatro critérios. Uma equipe que produzisse muitos achados atravessando uma linha de STOP seria reprovada no critério de escopo, e nenhuma contagem de achados conserta isso.

### 23.3 Lições aprendidas

Em até duas semanas, as equipes red, blue e branca se reúnem. Cada falha da matriz de cobertura vira um chamado. Cada falha de processo vira uma mudança de procedimento. Registre o que parar, o que começar e o que continuar. O DET-19, da história da cobertura, é o modelo de chamado de falha: nomeia a técnica do ATT&CK não coberta, a célula da matriz de onde veio e o responsável pela detecção. As falhas de processo são escritas como edições de um procedimento, como a verificação de sincronização de relógio antes da abertura que o ENG-712 acrescentou. Fazer a reunião em até duas semanas importa porque as pessoas ainda lembram por que uma escolha foi feita.

### 23.4 Métricas de vaidade

"Hosts varridos", "pacotes enviados" e "críticos encontrados", sem contexto, incentivam o comportamento errado. Prefira "técnicas exercitadas", "percentual com alerta", "achados aceitos no controle dentro do SLA" e "retestes encerrados". Num slide gerencial, Priya substitui uma linha como hosts varridos pelo número de técnicas exercitadas e pela parcela que gerou alerta. O segundo par responde à pergunta que o CISO fez sobre a cobertura do SOC; o primeiro só mede o quanto os testadores estiveram ocupados. Ela remove as linhas de vaidade na mesma passada de revisão que tira do relatório as frases de garantia proibidas.

### 23.5 Compartilhar os resultados sem vergonha

Publique a folha de avaliação para as pessoas que viveram o exercício. Esconder do SOC uma pontuação baixa de processo enquanto se celebra uma contagem alta de achados ensina a lição errada. A regra da TRT é que a mesma folha que o CISO assina é a folha que a equipe lê na retrospectiva. No ENG-712, o SOC viu a folha completa, incluindo a falha de processo da sincronização de relógio, na mesma retrospectiva em que os dois itens de backlog de detecção foram discutidos. Saber de uma pontuação fraca de processo por um resumo semanas depois teria soado como culpa. Vê-la ao lado dos achados a transformou num problema compartilhado, com responsável e data.

### Exemplo resolvido

A folha de avaliação da TRT para o ENG-712: aderência ao escopo de 100% (nenhuma violação de STOP); decisão apoiada (números de cobertura do SOC entregues); dois itens de backlog de detecção abertos; uma mudança de processo (verificação de sincronização de relógio antes da abertura). A contagem de achados é registrada, mas não é usada como pontuação principal. O CISO assina a folha.

> **Caso sintético.** A folha de avaliação é inventada.

### Erros e limites

Culpar indivíduos na reunião de lições aprendidas destrói a confiança no trabalho purple. Mantenha a ata centrada em sistemas e procedimentos.

### Exercícios

- **EX067 — Pontuação principal.** Por que "críticos encontrados" é uma pontuação principal de avaliação fraca? *Rubrica:* 3 = premia volume/abuso de escopo; ignora processo e aprendizado; 2 = um motivo; 1 = é a melhor pontuação; 0 = nada.
- **EX068 — Critério.** Escreva um critério declarado de antemão que meça o aprendizado dos defensores. *Rubrica:* 3 = critério de aprendizado mensurável (por exemplo, itens de backlog abertos por falha, presença na repetição); 2 = aprendizado vago; 1 = contagem de achados; 0 = nada.
- **EX069 — Parar/começar/continuar.** Dê um parar, um começar e um continuar tirados da história do ENG-712 até aqui. *Rubrica:* 3 = três itens concretos apoiados nos capítulos anteriores; 2 = dois; 1 = um; 0 = nada.

### Síntese

Declare os critérios cedo, pontue a disciplina, converta as lições em chamados e ignore os contadores de vaidade.

### Continue estudando — capítulo 23 de 30

[← Capítulo 22 (rascunho)](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 (rascunho) →](#ch-24)

<a id="ch-24"></a>

## Capítulo 24 — Métodos de pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa sobre a prática de avaliação que possa ser respondida com dados sintéticos ou autorizados; (2) escolher um método (estudo de medição, comparação de casos, entrevista estruturada); (3) declarar de início a ética e os limites; (4) escrever uma lista de verificação de resumo que pegue as peças que faltam.

### 24.1 Perguntas que valem a pena

Exemplos: um pipeline de três controles reduz as tentativas fora de escopo nos exercícios de estudantes? Em quais técnicas do ATT&CK o SOC da TRT alerta depois de um ciclo purple? Quanto tempo os chamados de correção de cada severidade ficam abertos? Cada pergunta nomeia uma população, uma medida e um limite. Uma pergunta como "o red team funciona?" não passa nesse teste, porque não nomeia população nem medida. A pergunta de estúdio de Priya sobre tentativas fora de escopo passa: a população são os exercícios de estúdio, a medida são as linhas OUT-OF-SCOPE no log do verificador, e o limite é que o comportamento de estudantes pode diferir do de uma equipe contratada. Perguntas que só poderiam ser respondidas testando usuários reais sem o conhecimento deles são rejeitadas de imediato.

### 24.2 Métodos adequados a tecnólogos

Estudos de medição sobre dados de chamados e de cobertura; comparações de antes e depois quando um controle muda; entrevistas estruturadas com analistas do SOC sobre a qualidade dos alertas. A pesquisa de exploits em laboratório está fora do escopo deste curso. O fio comum são dados com que um tecnólogo já lida: carimbos de tempo de chamados, células da matriz de cobertura e as palavras dos analistas que fazem a triagem dos alertas. Uma comparação de antes e depois em torno do DET-19, por exemplo, pode contar quantas vezes a nova detecção disparou sobre atividade sintética repetida. Propostas que derivam para o desenvolvimento de exploits inéditos são redirecionadas, porque exigem um laboratório e uma autorização que este curso não pode oferecer.

### 24.3 Ética em primeiro lugar

Nada de testes encobertos com usuários reais, nada de coleta de dados pessoais além do acordo, nada de publicação de identificadores de clientes. Rotule os dados sintéticos. Obtenha aprovação antes de entrevistar funcionários. Cada uma dessas regras tem uma verificação concreta que um revisor pode executar antes da submissão. Os logs sintéticos levam um rótulo nos nomes de arquivo e nos cabeçalhos, o consentimento para entrevistas é escrito e arquivado antes de qualquer resumo ser redigido, e todo rascunho público é pesquisado em busca de nomes e identificadores de clientes antes de ser enviado ao seminário. Um rascunho que falha na pesquisa volta ao autor, em vez de ser editado discretamente por um revisor.

### 24.4 Lista de verificação do resumo

Um resumo aceitável declara a pergunta, o método, o tamanho da amostra n, os limites e a postura ética. A falta do n é um modo de falha comum em trabalhos de estudantes. O exemplo resolvido de Priya mostra o mínimo: n = 3 exercícios e 12 ações, declarados no resumo ao lado do limite de que os dados são sintéticos. A avaliação do seminário trata a falta de uma linha de limites com a mesma seriedade que a falta do n, porque as duas permitem que o leitor superestime o que o estudo mostra. A linha de ética nomeia a postura — aqui, nenhum sistema real —, em vez de dizer que a ética foi considerada.

### 24.5 Reprodutibilidade para tecnólogos

Um colega deve conseguir refazer as contagens a partir dos logs sintéticos e obter as mesmas frações. Priya guarda os arquivos de entrada ao lado do resumo e anota a versão do Python. Reprodutibilidade aqui não tem a ver com ambientes exóticos; tem a ver com não acenar para números que ninguém mais consegue reconstruir. No miniestudo da fração de HOLDs, isso significa que os três logs sintéticos de exercícios, o script de contagem e uma nota com a versão do Python ficam numa só pasta, ao lado do resumo. Um colega que execute de novo o script deve chegar à mesma contagem de HOLDs em 12 ações. A captura de tela do total de uma planilha não é aceita, porque ninguém consegue verificar como ele foi produzido.

### Exemplo resolvido

O miniestudo de Priya pergunta: depois da introdução do registro do operador, que fração das ações planejadas foi HOLD em três exercícios sintéticos? Método: contar as saídas do pipeline. n = 3 exercícios, 12 ações. Limite: apenas dados sintéticos. Ética: nenhum sistema real. Ela se recusa a afirmar que o resultado se generaliza para todos os fornecedores.

> **Caso sintético.** O desenho do miniestudo foi inventado para o trabalho do curso.

### Erros e limites

Colher logs de produção para um artigo sem aprovação continua sendo uma violação no tratamento de dados. Um n minúsculo exige afirmações humildes.

### Exercícios

- **EX070 — Forma da pergunta.** Reescreva "Red teams são bons?" como uma pergunta de pesquisa mensurável para a TRT. *Rubrica:* 3 = nomeia medida, população e período; 2 = parcialmente mensurável; 1 = continua vaga; 0 = nada.
- **EX071 — Falta o n.** Um resumo descreve o método e os limites, mas não o tamanho da amostra. O que diz a lista de verificação? *Rubrica:* 3 = n MISSING → revisar; 2 = incompleto; 1 = está bom assim; 0 = nada.
- **EX072 — Linha de ética.** Escreva uma frase de ética que Priya possa pôr em seu resumo. *Rubrica:* 3 = nenhum sistema real / dados sintéticos ou autorizados / nenhum dado pessoal além do acordo; 2 = ética vaga; 1 = não é necessária; 0 = nada.

### Síntese

Faça uma pergunta mensurável, escolha um método humilde, ponha a ética no resumo e nunca pule o n.

### Continue estudando — capítulo 24 de 30

[← Capítulo 23 (rascunho)](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 (rascunho) →](#ch-25)

<a id="ch-25"></a>

## Capítulo 25 — Estúdio de projeto em equipe

### Objetivos de aprendizagem

Você vai (1) formar uma pequena equipe com papéis nomeados (líder, evidências, elo de ligação); (2) executar uma lista de verificação de planejamento antes de qualquer trabalho de laboratório; (3) apresentar uma revisão no meio do estúdio com base nos critérios de avaliação do Capítulo 23; (4) praticar a resolução de conflitos quando as opiniões sobre o escopo divergem.

### 25.1 Papéis valem mais que heroísmo

O líder cuida das ROE e do cronograma. O responsável pelas evidências cuida dos manifestos e da custódia. O elo de ligação fala com a equipe branca (sintética) e com o SOC. Alternar os papéis entre estúdios cria amplitude; deixar tudo com quem escreve melhor cria um ponto único de falha. Cada papel tem um cartão na parede do estúdio, fotografado para a pasta de evidências no início, para que haja registro de quem teve cada função. No exemplo resolvido, Sam é o elo de ligação e, por isso, tem o único número de contato da equipe branca. Alternar os cartões entre estúdios faz com que todos acabem executando um manifesto, cuidando de umas ROE e fazendo uma ligação difícil para a equipe branca.

### 25.2 Lista de verificação de planejamento

Campos do acordo completos; listas de escopo carregáveis pelo verificador; inventário do kit com versões fixadas; critérios de avaliação escritos; canal de comunicação testado. Sem lista de verificação, sem tempo de laboratório. O instrutor pode reprovar na porta um estúdio que não apresente a lista. Cada item é respondido com sim ou não na porta. Um acordo com o campo de exclusão vazio ou uma lista de escopo que o verificador não consegue carregar significa que o relógio do laboratório não começa, por mais perto que a equipe diga estar. Testar o canal de comunicação antes do início do trabalho está na lista porque um elo de ligação que não consegue alcançar a equipe branca durante um HOLD não tem como continuar com segurança.

### 25.3 Revisão no meio do estúdio

Na metade, a equipe apresenta: controles aprovados até ali, HOLDs encontrados, contagem de evidências, riscos para a entrega. Os instrutores pontuam o processo, não o drama. A revisão intermediária da Platform B é um bom exemplo: quatro controles aprovados, um HOLD num nome DNS à deriva e seis itens de evidência com hash. Relatar o HOLD abertamente rende pontos, porque mostra o controle funcionando. Um HOLD escondido e descoberto depois custa mais do que um declarado cedo, já que sugere que a equipe teria seguido em frente sem a decisão da equipe branca.

### 25.4 Conflito sobre o escopo

Quando os membros discordam sobre se um nome de host está no escopo, a regra é: parar, reler o acordo, pedir ao elo de ligação que confirme com a equipe branca. A voz mais alta não vence. A Platform B enfrentou exatamente esse caso com seu nome DNS à deriva: a equipe pausou esse alvo, e Sam pediu à equipe branca uma decisão por escrito. A decisão é arquivada sob o identificador de evidência do nome de host, para que um leitor posterior veja por que o nome foi testado ou deixado de lado. Uma lembrança confiante do que o escopo queria dizer nunca substitui a lista assinada.

### 25.5 Canais discretos

As conversas do estúdio que contêm hashes de evidências, nomes de contas ou detalhes das ROE ficam no canal aprovado, e não em aplicativos de mensagens pessoais. Sam, como elo de ligação, é a única pessoa que aciona a equipe branca. Conversas paralelas criam instruções conflitantes e perda de custódia. Durante o estúdio, os instrutores verificam semanalmente uma amostra de mensagens para conferir que nenhum hash ou detalhe das ROE vazou para SMS ou e-mail pessoais. O log do canal aprovado também serve como parte do registro de custódia, mostrando quando cada hash foi compartilhado e com quem. Quando dois colegas acionam cada um a equipe branca, a equipe acaba com duas respostas e nenhum registro claro de qual delas valeu.

### Exemplo resolvido

A equipe de estúdio "Platform B" designa Priya como líder (para o exercício), Jordan para as evidências e Sam como elo de ligação. A revisão intermediária mostra quatro controles aprovados, um HOLD num nome DNS à deriva e seis itens de evidência com hash. Eles pedem uma decisão por escrito sobre o nome à deriva e pausam esse alvo.

> **Caso sintético.** A Platform B e seus membros, exceto Priya, são colegas inventados.

### Erros e limites

Estúdios que pulam o elo de ligação e "só dão um toque informal no CISO" treinam maus hábitos. Mantenha as comunicações no canal aprovado.

### Exercícios

- **EX073 — Mapa de papéis.** Atribua as responsabilidades de líder, evidências e elo de ligação, numa frase cada. *Rubrica:* 3 = três frases de responsabilidade distintas; 2 = duas; 1 = uma; 0 = nada.
- **EX074 — Conflito da deriva.** Jordan acha que o nome de host à deriva está "perto o bastante". O que a equipe faz? *Rubrica:* 3 = parar; reconferir o acordo; o elo de ligação confirma com a equipe branca; nenhum teste até o aval por escrito; 2 = só parar; 1 = testar mesmo assim; 0 = nada.
- **EX075 — Conteúdo da revisão intermediária.** Liste quatro itens que uma revisão no meio do estúdio deve mostrar. *Rubrica:* 3 = quatro entre controles/HOLDs/contagem de evidências/riscos/progresso nos critérios; 2 = dois; 1 = só achados; 0 = nada.

### Síntese

Nomeie os papéis, cumpra a lista de verificação, revise o processo na metade e resolva disputas de escopo com o acordo — não com o volume da voz.

### Continue estudando — capítulo 25 de 30

[← Capítulo 24 (rascunho)](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 (rascunho) →](#ch-26)

<a id="ch-26"></a>

## Capítulo 26 — Segurança ofensiva autorizada e red team: passagem para operação

### Objetivos de aprendizagem

Você vai (1) escrever um pacote de passagem com o qual as operações possam agir sem a presença da equipe de testes; (2) incluir o risco residual e as incógnitas conhecidas; (3) transferir de forma limpa o acesso às evidências; (4) agendar a janela de reteste antes da desmobilização.

### 26.1 Do que as operações precisam

Os responsáveis precisam de: cada achado com severidade, cenário, ponteiro de evidência, controle recomendado e um prazo sugerido. Não precisam de um diário de viagem de cada ferramenta que os testadores executaram. Corte a narrativa que não muda uma decisão. Priya monta a tabela executiva com o gerador de relatório e deixa de fora qualquer prazo sem responsável, já que uma data que ninguém assume não será cumprida. Cada responsável recebe então uma folha de achado que começa pelo cenário e pelo prazo. As notas sobre quais ferramentas foram executadas vão para um apêndice opcional, para os leitores que precisem reproduzir o trabalho.

### 26.2 Risco residual e incógnitas

Todo engajamento termina com coisas não testadas — segmentos excluídos, técnicas não exercitadas, janelas que foram encurtadas. Liste-as. Os conselhos detestam surpresas mais do que detestam um trabalho incompleto, mas honestamente delimitado. No ENG-712, a página de risco residual nomeia duas lacunas em palavras simples: o segmento de pagamento de tarifas não foi testado, e a técnica T1021 ainda não gerou alerta. A lista de verificação da passagem trata como incompleta uma página residual sem a linha do pagamento de tarifas. Escrever as lacunas agora custa um parágrafo curto, enquanto um conselho que as descubra depois perde a confiança no engajamento inteiro.

### 26.3 Transferência de acesso

Contas de testadores, perfis de VPN e permissões no cofre terminam na data da passagem. As operações recebem acesso de leitura ao pacote de evidências sob seus próprios papéis. Caixas de correio compartilhadas usadas "só para o teste" são fechadas. Na reunião de passagem do ENG-712, Priya lê em voz alta a lista de verificação de revogação com a Northpoint presente, e os perfis de VPN são revogados na mesma tarde. O cofre de evidências passa para controle de acesso exclusivo da TRT, mas só depois que as operações confirmam que conseguem abrir os arquivos. Qualquer acesso da Northpoint que ainda funcione depois da data da passagem é registrado como achado contra o próprio engajamento.

### 26.4 O reteste na agenda

Um prazo de correção sem horário de reteste é um desejo. Reserve a janela de validação (Capítulo 27) antes que a equipe de testes se disperse. Uma passagem sem reteste reservado é marcada como incompleta na folha de avaliação. No ENG-712, o reteste é reservado para 2026-12-08 enquanto os testadores da Northpoint ainda estão contratados, e o convite de calendário é anexado ao pacote de passagem. Reservar cedo significa que as pessoas que conhecem os achados estarão disponíveis para executar as verificações. Um pacote de passagem que chega sem o convite é marcado como incompleto até que o horário seja combinado.

### 26.5 Apresentações calorosas

Uma reunião de passagem em que Priya apresenta pelo nome cada responsável por achado é melhor do que despejar um e-mail. Dez minutos de esclarecimento presencial (ou por vídeo) evitam uma semana de chamados mal encaminhados. Ela registra a presença para que a folha de avaliação mostre que as operações de fato receberam o trabalho. Priya acompanha uma medida simples de como isso funcionou: o número de chamados que chegam à equipe errada na primeira semana depois da passagem. Um responsável que ouviu o cenário explicado pessoalmente tem menos chance de devolver um chamado dizendo que não é dele. A lista de presença da reunião entra na folha de avaliação como prova de entrega.

### Exemplo resolvido

O pacote de passagem de Priya para o ENG-712: tabela executiva do gerador de relatório; quatro folhas de achados; página de risco residual (pagamento de tarifas não testado; T1021 ainda sem detecção); ACL do cofre de evidências trocada para acesso exclusivo da TRT; horário de reteste reservado para 2026-12-08. Os perfis de VPN da Northpoint são revogados na mesma tarde.

> **Caso sintético.** O conteúdo do pacote de passagem é inventado.

### Erros e limites

Passagens que despejam exportações brutas de scanner sem triagem criam enxurradas de chamados. Não revogue o acesso às evidências antes que as operações confirmem que conseguem abrir os arquivos.

### Exercícios

- **EX076 — Conteúdo do pacote.** Nomeie cinco artefatos de um pacote de passagem mínimo. *Rubrica:* 3 = cinco entre tabela executiva/achados/risco residual/ponteiros de evidência/nota de ACL/data de reteste; 2 = três; 1 = só o PDF; 0 = nada.
- **EX077 — Incógnita.** Escreva uma frase de risco residual para a exclusão do pagamento de tarifas da TRT. *Rubrica:* 3 = declara a exclusão + que nenhuma garantia é afirmada ali; 2 = menciona a exclusão; 1 = afirma que as tarifas estão bem; 0 = nada.
- **EX078 — Ordem da revogação.** Em que ordem devem acontecer a troca da ACL do cofre e a revogação da VPN da Northpoint, e por quê? *Rubrica:* 3 = confirmar que a TRT consegue ler as evidências e depois revogar o acesso dos testadores; 2 = qualquer ordem com justificativa fraca; 1 = revogar primeiro, às cegas; 0 = nada.

### Síntese

Entregue decisões e evidências, diga o que você não testou, mova os acessos com cuidado e reserve o reteste antes da despedida.

### Continue estudando — capítulo 26 de 30

[← Capítulo 25 (rascunho)](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 (rascunho) →](#ch-27)

<a id="ch-27"></a>

## Capítulo 27 — Implantação e validação

### Objetivos de aprendizagem

Você vai (1) decidir entre VALIDATED, REOPENED ou NOT RETESTED a partir das observações do reteste; (2) recusar-se a marcar um achado como encerrado com base num "já corrigimos" verbal; (3) registrar a evidência da validação sob as mesmas regras de custódia; (4) devolver as falhas ao controle de riscos.

### 27.1 A validação é um teste da correção

A validação da correção pergunta se a correção combinada eliminou o problema, sob as mesmas restrições de escopo e de método. Não é um engajamento novo nem um carimbo automático. No ENG-712, o reteste usa a mesma lista de escopo e os mesmos cartões de método do engajamento original. Aproveitar a visita para sondar os hosts excluídos de pagamento de tarifas seria uma falha de segurança, por mais conveniente que parecesse. Os três rótulos de status do laboratório mantêm a linguagem honesta, obrigando os testadores a dizer exatamente o que foi verificado e o que não foi.

### Laboratório I — status do reteste

```python
"""Lab H (ch 27): decide remediation-validation status from synthetic retest observations."""
retests = [
    ("F-01", "shared admin account", True, True),
    ("F-07", "ex-contractor VPN accounts", True, False),
    ("F-09", "plaintext password on wiki", False, None),
]
for fid, title, fix_claimed, check_passed in retests:
    if not fix_claimed:
        status = "NOT RETESTED - no fix declared"
    elif check_passed:
        status = "VALIDATED"
    else:
        status = "REOPENED"
    print(f"{fid} {status:30} {title}")
```

Execute com `python3 lab_retest.py`. Saída verificada:

```text
F-01 VALIDATED                      shared admin account
F-07 REOPENED                       ex-contractor VPN accounts
F-09 NOT RETESTED - no fix declared plaintext password on wiki
```

### 27.2 Três status

VALIDATED: correção declarada e verificação aprovada. REOPENED: correção declarada, mas a verificação falhou. NOT RETESTED: nenhuma correção declarada, portanto ainda não há verificação. Fechar um chamado sem um dos dois primeiros (ou sem uma aceitação de risco explícita) é um defeito de processo. A saída do laboratório dá um exemplo de cada: F-01 VALIDATED, F-07 REOPENED e F-09 NOT RETESTED. Palavras como "resolvido" ou "quase corrigido" são reescritas como um dos três rótulos antes de o relatório ir para o CISO. Uma aceitação de risco explícita é a única outra forma de um chamado ser fechado, e ela é registrada separadamente.

### 27.3 A mesma custódia

A evidência do reteste — uma nova exportação de configuração, um novo trecho de log — recebe hash e é arquivada como a original. "Na minha tela parece certo" não é evidência. Para o F-01, a nova evidência é arquivada como E-101, com seu próprio digest, ao lado da evidência original da descoberta, na mesma estrutura do cofre. Um par que abra o achado pode então comparar diretamente os arquivos de antes e depois. Uma concordância num compartilhamento de tela de que a configuração parece certa não deixa nada que possa ser verificado depois.

### 27.4 Aceitação de risco

Às vezes um responsável aceita um risco residual, com um aprovador nomeado e uma data de revisão. Esse é um caminho legítimo de encerramento; o silêncio, não. Uma aceitação no controle precisa de dois campos para valer: o nome da pessoa que aceita o risco e uma data de revisão. A equipe de Priya transforma cada data de revisão num lembrete de calendário duas semanas antes do vencimento. Uma aceitação com qualquer desses campos vazio é reaberta, porque ninguém pode ser cobrado por uma decisão que não tem dono.

### 27.5 Correções parciais

Às vezes um responsável corrige duas de três contas e pede para fechar o chamado. A regra de Priya é validar o que foi declarado, reabrir ou dividir o achado para o que resta e nunca deixar uma correção parcial apagar o problema inteiro. O controle deve mostrar o trabalho residual, e não uma caixa verde que o esconde. O exemplo resolvido mostra por quê: o F-07 foi reaberto porque contas de ex-terceirizados ainda conseguiam se autenticar depois de uma correção declarada, então fechá-lo pela palavra do responsável teria escondido um acesso ativo. Um chamado filho separado para qualquer conta restante mantém o identificador do achado pai, para que um examinador possa seguir o histórico.

### Exemplo resolvido

Três achados entram no reteste. O F-01 é validado. O F-07 é reaberto porque as contas de ex-terceirizados ainda se autenticam. O F-09 nunca foi declarado corrigido. Priya atualiza o controle: F-01 fechado com a evidência E-101; o F-07 continua com severidade alta e o prazo é reiniciado; o F-09 continua aberto, aguardando uma declaração de correção.

> **Caso sintético.** Os três resultados de reteste são inventados.

### Erros e limites

Retestar apenas o caminho feliz e ignorar pontos de entrada alternativos pode validar falsamente. Fique dentro do escopo original, a menos que um novo acordo diga o contrário.

### Exercícios

- **EX079 — Status do laboratório.** Cite os três status que o laboratório imprime. *Rubrica:* 3 = VALIDATED, REOPENED, NOT RETESTED - no fix declared; 2 = dois; 1 = um; 0 = nada.
- **EX080 — Encerramento verbal.** Um responsável diz que o F-07 está corrigido, mas recusa uma janela de reteste. Qual é o status e o próximo passo? *Rubrica:* 3 = continua aberto / não validado; escalar; nada de encerrar sem verificação ou aceitação formal; 2 = manter aberto; 1 = encerrar pela palavra; 0 = nada.
- **EX081 — Campos da aceitação.** Nomeie três campos de que um registro de aceitação de risco precisa. *Rubrica:* 3 = três entre aprovador/motivo/data de revisão/declaração de risco residual/escopo; 2 = dois; 1 = um; 0 = nada.

### Síntese

Sem declaração de correção, sem reteste; sem evidência, sem encerramento; a aceitação é explícita ou não aconteceu.

### Continue estudando — capítulo 27 de 30

[← Capítulo 26 (rascunho)](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 (rascunho) →](#ch-28)

<a id="ch-28"></a>

## Capítulo 28 — Prática de campo

### Objetivos de aprendizagem

Você vai (1) preparar uma lista de verificação do kit de campo para uma sessão supervisionada presencial ou remota; (2) praticar a conduta profissional com a equipe de operações; (3) lidar com um evento inesperado de produção durante uma janela; (4) fazer o encerramento com fatos, não com folclore.

### 28.1 Kit de campo

ROE escritas e contatos de emergência (cópia offline); versões de ferramentas fixadas; verificador de escopo e verificador de ROE; credenciais do cofre de evidências que funcionem; um caminho telefônico fora de banda testado até a equipe branca; um bloco de notas para as linhas de custódia quando os sistemas estiverem fora do ar. Painéis sofisticados são opcionais; a lista de verificação, não. A cópia offline importa mais do que parece durante uma longa noite no local. Um celular pode ser o único dispositivo com as ROE e o número da equipe branca, e uma bateria descarregada numa plataforma de estação deixa então o testador sem como conferir um limite nem ligar para alguém. Priya leva as ROE e a folha de contatos impressas, e a lista de verificação de conduta reprova um kit que não as tenha.

### 28.2 Conduta

A equipe de avaliação é convidada na casa das operações. Explique em linguagem simples o que você está prestes a fazer, respeite a janela e nunca surpreenda um gestor de mudanças com tráfego durante um congelamento. O sucesso do trabalho purple depende da confiança construída nesses pequenos momentos. Na prática, isso significa avisar o controlador de plantão sobre o que a próxima verificação vai tocar antes de começá-la. Se houver uma troca de escala marcada para sexta-feira, uma verificação quase concluída para e passa para a janela seguinte, mesmo com o alvo em escopo. Essa troca pertence ao gestor de mudanças, e os testadores que a ignoram perdem o acesso de que precisam para o resto do engajamento.

### 28.3 Eventos inesperados

O desarme de um disjuntor, uma indisponibilidade da informação aos passageiros, uma emergência médica no local — nada disso aparece nas ROE, e tudo isso significa parar o trabalho ruidoso e dar lugar às operações. Retome apenas por instrução da equipe branca. As ROE não conseguem listar todas as emergências, então o padrão quando algo inesperado acontece é parar. Recomeçar exige um "pode seguir" explícito da equipe branca, e o registro anota o nome de quem o deu e o horário. Esse registro mostra depois que a pausa e a retomada foram decisões, e não deriva.

### 28.4 Encerramento com fatos

"O SOC estava dormindo" é folclore. "O T1021 não gerou alerta por 40 minutos; chamado DET-19 aberto" é um fato. As notas de campo devem sustentar o segundo estilo. Registrar os quarenta minutos de silêncio sobre o T1021 e o chamado DET-19 dá ao SOC algo a corrigir e uma forma de conferir que foi corrigido. Redações ofensivas sobre o SOC são cortadas das notas de campo, e o autor que as usa recebe um achado de conduta levantado pelo elo de ligação. A culpa encerra justamente as conversas de que uma equipe purple precisa.

### 28.5 Prática de campo remota

Quando a sessão é remota, e não presencial, o kit continua valendo: telefone fora de banda, ROE offline, compartilhamento de tela testado que não exponha arquivos não relacionados na área de trabalho. Priya fecha todas as outras janelas antes de entrar na chamada com a equipe branca. A exposição acidental da tela de outro cliente é uma falha de campo, mesmo que nenhum pacote tenha sido enviado. O trabalho remoto acrescenta riscos próprios, como uma notificação de chat que aparece durante o compartilhamento de tela ou um arquivo de outro cliente visível na área de trabalho. Antes de uma chamada com a equipe branca, Priya testa o compartilhamento de tela com um colega e confirma que apenas a janela combinada está visível. As ROE offline e o telefone fora de banda ficam na mesa dela exatamente como ficariam no local.

### Exemplo resolvido

Durante uma janela noturna supervisionada, os painéis de informação aos passageiros falham em toda a cidade por um motivo não relacionado. Priya interrompe o tráfego de inventário, avisa a equipe branca e passa para a rotulagem offline das evidências. Quando o NOC resolve o evento, a equipe branca autoriza uma retomada encurtada. O encerramento cita o horário da interrupção e os chamados DET, e não personalidades.

> **Caso sintético.** A indisponibilidade dos painéis e a interrupção são uma prática de campo inventada.

### Erros e limites

O heroísmo de campo de "terminar a varredura mesmo assim" durante uma indisponibilidade é como as equipes de avaliação acabam banidas. Aceite o no-go.

### Exercícios

- **EX082 — Item do kit.** Por que levar uma cópia offline das ROE? *Rubrica:* 3 = o cofre/a VPN podem estar fora do ar; ainda é preciso ter o escopo/os contatos de emergência; 2 = backup, de forma vaga; 1 = desnecessário; 0 = nada.
- **EX083 — Congelamento.** Um congelamento de mudanças começa duas horas antes do previsto. O que a equipe faz com as verificações ativas planejadas? *Rubrica:* 3 = parar as verificações ativas; confirmar com a equipe branca/o gestor de mudanças; reagendar; 2 = pausar; 1 = espremê-las no tempo que resta; 0 = nada.
- **EX084 — Linha de fato.** Reescreva "O SOC nos ignorou" como uma frase factual de encerramento. *Rubrica:* 3 = nomeia a técnica, o tempo até o alerta ou a falha, o ID do chamado; 2 = fato parcial; 1 = mantém a culpa; 0 = nada.

### Síntese

Leve a lista de verificação, comporte-se como convidado, dê lugar aos eventos reais e faça o encerramento com fatos registrados em chamados.

### Continue estudando — capítulo 28 de 30

[← Capítulo 27 (rascunho)](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 (rascunho) →](#ch-29)

<a id="ch-29"></a>

## Capítulo 29 — Construção do projeto final

### Objetivos de aprendizagem

Você vai (1) montar um pacote completo de avaliação autorizada para um pedido sintético da TRT; (2) incluir objetos de escopo, ROE, declaração de método, plano de evidências, escala de classificação e modelo de relatório; (3) executar todos os verificadores dos laboratórios sobre o pacote; (4) entregar uma construção que um colega consiga operar sem precisar lhe fazer perguntas.

### 29.1 Os artefatos da construção

1. Pedido e declaração de decisão. 2. Listas de escopo (prefixos, nomes, exclusões). 3. ROE (janela, atividades permitidas, lista de parada, contato da equipe branca). 4. Declaração de método mapeada para SP 800-115/PTES/WSTG, conforme o uso. 5. Inventário do kit com versões. 6. Plano de evidências (o quê, onde, retenção). 7. Escala de classificação e faixas. 8. Modelo de relatório com gancho para a tabela executiva. 9. Plano de reteste. 10. Critérios de avaliação.

A falta de qualquer um dos dez reprova a pontuação de completude do projeto final. A ordem segue a vida de um engajamento, então a pontuação de completude percorre os artefatos na mesma sequência na folha de pontuação dos colegas. Um pacote com achados brilhantes, mas sem plano de evidências ou plano de reteste, está incompleto. No exemplo resolvido de Priya, os dez artefatos estão presentes, incluindo a exclusão do pagamento de tarifas tanto por prefixo quanto por nome de host.

### 29.2 Opere o que você construiu

Um colega carrega seu escopo nos padrões do `lab_scope.py`, suas ROE nos padrões do `lab_roe.py` e seus achados no `lab_score.py` e no `lab_report.py`. Se não conseguir, a construção está incompleta. No exemplo resolvido, um colega executa os verificadores sobre o pacote de Priya e obtém os mesmos resultados STOP e IN-SCOPE que ela documentou. Essa reprodução por alguém que não é o autor é o que operabilidade significa aqui. Se o verificador de escopo não conseguir carregar as listas entregues, a operabilidade falha antes que se olhe qualquer slide, porque uma apresentação polida de um pacote inutilizável não ajuda uma equipe de operações.

### 29.3 Nenhum conteúdo de exploração

O pacote contém zero procedimentos de ataque. Quem pedir esse tipo de coisa durante o projeto final é redirecionado ao limite educacional do Capítulo 10. O projeto final testa se os estudantes conseguem desenhar e operar um serviço de avaliação, e não se conseguem atacar algo, então passos de ataque não acrescentam nada à nota. Um estudante que peça detalhes de exploração durante a construção é redirecionado ao Capítulo 10 e recebe um desconto de segurança. A rubrica não tem exceção para pedidos apresentados como sendo para fins didáticos, já que um procedimento escrito funciona do mesmo jeito para quem quer que o leia depois.

### 29.4 Rubrica da revisão por pares

Os colegas pontuam: completude dos dez artefatos, verificabilidade, clareza da linguagem de risco residual e segurança (nenhum detalhe de uso dual). O volume de achados é irrelevante. Detalhes de uso dual reprovam o critério de segurança mesmo num pacote completo em todo o resto. Um colega que dê pontos extras por uma lista longa de achados inventou um critério, e essa folha de pontuação é anulada e refeita. O sentido da rubrica é que um revisor possa entregar o pacote a uma equipe de operações e esperar que ele funcione, com uma redação de risco residual que um gestor consiga repetir com exatidão.

### 29.5 Tempo limitado

A construção do projeto final é pontuada pela completude e pela operabilidade dentro de uma janela fixa de estúdio, e não por um polimento sem fim. Priya congela as listas de escopo quarenta e oito horas antes da revisão por pares, para que os verificadores parem de se mexer. Edições estéticas de última hora que quebram uma coluna do CSV reprovam no teste dos colegas. O líder anuncia o congelamento no canal do estúdio quando faltam 48 horas, e a partir daí as listas de escopo não são editadas. Uma coluna renomeada por capricho depois do congelamento pode impedir o verificador de escopo de carregar o CSV, o que reprovaria no teste dos colegas. Polir os slides continua permitido, desde que os arquivos que os verificadores leem não mudem.

### Exemplo resolvido

O pacote de projeto final de Priya para um pedido sintético de "garantia de identidade do portal dos funcionários" preenche os dez artefatos, exclui o pagamento de tarifas por prefixo e por nome de host, fixa as versões de três ferramentas e inclui o gancho da tabela do Capítulo 22. Um colega executa os verificadores e produz os mesmos resultados STOP/IN-SCOPE que ela documentou.

> **Caso sintético.** O pedido do projeto final e o colega são inventados.

### Erros e limites

Uma prosa bonita que um verificador não consegue carregar não cumpre o objetivo do tecnólogo. Copiar o pacote de outra equipe sem entendê-lo também reprova.

### Exercícios

- **EX085 — Dez artefatos.** Liste quaisquer oito dos dez artefatos da construção. *Rubrica:* 3 = oito corretos da lista do capítulo; 2 = cinco; 1 = três; 0 = nada.
- **EX086 — Teste dos colegas.** Que dois resultados provam que um colega consegue operar o seu pacote? *Rubrica:* 3 = os verificadores rodam + os veredictos batem com os documentados; 2 = um; 1 = o colega gosta da prosa; 0 = nada.
- **EX087 — Falha de segurança.** Um colega de equipe acrescenta uma página com os passos de password spraying "para dar realismo". O que você faz? *Rubrica:* 3 = remover; citar o limite educacional; recusar conteúdo de uso dual; 2 = mover para um apêndice; 1 = manter; 0 = nada.

### Síntese

Construa o serviço inteiro no papel e nos verificadores; deixe um colega operá-lo; mantenha de fora os detalhes de exploração.

### Continue estudando — capítulo 29 de 30

[← Capítulo 28 (rascunho)](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 (rascunho) →](#ch-30)

<a id="ch-30"></a>

## Capítulo 30 — Avaliação do projeto final

### Objetivos de aprendizagem

Você vai (1) apresentar o pacote do projeto final a uma banca; (2) defender as escolhas de escopo, método e risco residual citando frameworks; (3) responder corretamente a "o que você recusaria?"; (4) identificar seu próximo passo no curso sem afirmar que o livro está pronto.

### 30.1 Pauta da banca

Dez minutos: decisão e escopo. Dez minutos: método e controles. Dez minutos: evidência, classificação e relatório. Dez minutos: aprendizado purple e reteste. Dez minutos: perguntas. A banca tem em mãos as ROE e as saídas dos verificadores enquanto você fala. Priya mantém um cronômetro visível na mesa, e a lista de verificação do kit da banca reprova a prontidão se ele faltar. Os blocos de tempo protegem os blocos finais: um candidato que gasta vinte minutos com detalhes técnicos não deixa tempo para mostrar o aprendizado purple nem o plano de reteste. Como a banca tem as ROE e as saídas dos verificadores, cada afirmação pode ser conferida com um artefato no momento em que é feita.

### 30.2 Defesa com citações

Quando perguntarem por que as exclusões vêm primeiro, cite o Capítulo 2 e a prática das ROE. Quando perguntarem por que você tomou emprestada uma equipe branca, cite as ideias do TIBER-EU/CBEST. Quando perguntarem como você classificou o F-09, mostre a matriz. Opiniões sem artefatos pontuam mal. Priya ensaia essas respostas em voz alta e as mantém numa folha-resumo de uma página, que a banca permite sobre a mesa. Para o F-09, ela abre a matriz de classificação e percorre as células de probabilidade e impacto, em vez de defender a classificação de memória. Uma resposta que aponta para um artefato permite que a banca a confira, enquanto uma opinião confiante não deixa nada a verificar.

### 30.3 A pergunta da recusa

As bancas perguntam o que você recusaria. Respostas fortes: testar sem uma equipe branca alcançável; contato com o pagamento de tarifas; ampliação do escopo pelo chat no meio da janela; fornecer passos de exploração; guardar evidências num notebook pessoal. Respostas fracas: "nada, somos flexíveis". Cada resposta forte nomeia uma condição e o motivo pelo qual ela encerra o trabalho, como a falta de uma equipe branca alcançável significar que ninguém pode autorizar uma parada ou uma retomada. A segurança na prova oral reprova se faltar qualquer uma das quatro classes de recusa: ausência da equipe branca, contato com o pagamento de tarifas, ampliação de escopo pelo chat e passos de exploração. Uma resposta flexível sugere que o candidato ainda não pensou em onde ficam os limites.

### 30.4 Depois da banca

Aprovação significa que o pacote cumpre a rubrica do Capítulo 29 e que a defesa oral mostrou julgamento. Não significa que o manuscrito passou pela verificação A4 ou pela revisão independente. O próximo curso no percurso de estudo é o curso 089, segurança de IA e aprendizado de máquina para tecnólogos. Antes do fim das perguntas, Priya diz em voz alta que o pacote usa dados sintéticos e que uma aprovação não confere nenhuma autoridade real. Essa frase está na lista de verificação do roteiro de aprovação, porque os candidatos às vezes descrevem a aprovação num curso como se ela os certificasse para testar sistemas reais. Dizer os limites com clareza faz parte do julgamento que a banca está avaliando.

### 30.5 Registro no portfólio

Depois da banca, Priya arquiva uma nota curta de portfólio: quais artefatos liderou, qual recusa praticou, quais chamados de detecção abriu. A nota cita o ENG-712 e rotula tudo como sintético. Futuros empregadores que leiam um portfólio devem ver julgamento, e não a alegação de que ela "hackeou uma empresa de transporte". A nota de Priya lista a folha de avaliação e o pacote de passagem como artefatos que ela liderou, a recusa do pagamento de tarifas como a que praticou e o DET-19 como um chamado que abriu. Redações como "hackeou uma empresa de transporte" são proibidas na nota, porque são falsas para um exercício sintético e sugerem a atitude errada a um empregador.

### Exemplo resolvido

Priya apresenta o pacote do ENG-712. Pedem a ela que amplie o escopo para o pagamento de tarifas "só desta vez". Ela recusa, cita a redação da exclusão e oferece uma proposta de engajamento separado, caso o responsável pelas tarifas o autorize. Pedem a ela os passos de exploração do T1552.001; ela aponta para a página do ATT&CK e para o limite do livro. A banca registra a segurança e a honestidade sobre o risco residual como pontos fortes.

> **Caso sintético.** A troca com a banca foi inventada para a prática de avaliação.

### Erros e limites

Decorar nomes de frameworks sem ligá-los a uma decisão reprova. Alegar acreditação com base neste rascunho reprova.

### Exercícios

- **EX088 — Lista de recusas.** Dê três recusas distintas que um tecnólogo precisa estar pronto para fazer. *Rubrica:* 3 = três entre sem equipe branca / sistemas excluídos / mudança de escopo pelo chat / passos de exploração / depósitos pessoais de evidências; 2 = duas; 1 = uma; 0 = nada.
- **EX089 — Defesa com citação.** Numa frase, defenda por que logged ≠ alerted usando a linguagem do Capítulo 19. *Rubrica:* 3 = o objetivo de detectar e responder exige notificação/resposta, e não apenas telemetria; 2 = parcial; 1 = logged basta; 0 = nada.
- **EX090 — Próximo passo.** Qual é o próximo curso depois do capítulo 30 deste livro e o que você não pode afirmar sobre este rascunho? *Rubrica:* 3 = curso 089, segurança de IA + nenhuma afirmação de livro pronto/aprovado na A4/acreditado; 2 = uma parte; 1 = curso errado; 0 = nada.

### Síntese

Apresente artefatos, cite frameworks, pratique a recusa e saia com humildade sobre o que é um manuscrito em rascunho.

### Continue estudando — capítulo 30 de 30

[← Capítulo 29 (rascunho)](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções ↓](#worked-results) · [Próximo curso pelo índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX090. A Tidewater Regional Transit, Priya Natarajan, a Northpoint Assurance e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX028.** Exemplo: "Determinar, num exercício autorizado e com prazo definido, sob supervisão da equipe branca, se o SOC da TRT detecta e responde a um intruso realista contra o portal dos funcionários e a VPN, excluindo os sistemas de pagamento de tarifas."

**EX029.** Quaisquer cinco entre: partes, sistemas em escopo, exclusões, métodos permitidos, janela de tempo, contato de emergência, regras de tratamento de dados, público do relatório. Nomear cinco campos obrigatórios distintos recebe 3.

**EX030.** O purple teaming estrutura a colaboração — muitas vezes com revelações planejadas ou revisões conjuntas — para que os defensores melhorem a detecção e a resposta; o produto principal é o aprendizado, e não um placar competitivo.

**EX031.** `2026-11-04 06:10 VPN configuration review STOP: outside window` e `2026-11-03 23:00 fare-system interaction STOP: forbidden activity`.

**EX032.** Escrever um limite rígido: apenas revisão de configuração, ou verificações ativas limitadas a uma taxa combinada dentro da janela, e registrar esse limite nas ROE para que os testadores não improvisem.

**EX033.** Não iniciar a sessão. Escalar para o CISO ou para o substituto nomeado, confirmar uma autoridade de parada alcançável e só então reabrir a janela por escrito.

**EX034.** Exemplo: logs de acesso do proxy reverso, um WAF, uma borda de CDN ou o SIEM. Qualquer um deles pode guardar uma cópia que vira evidência da avaliação e que precisa seguir as regras de retenção do acordo.

**EX035.** Mascarar `alex.rivera` (a parte local) e manter `@trt.example` ou um rótulo como "conta de funcionário", para que o achado ainda prove que uma identidade de funcionário estava envolvida sem expor a pessoa.

**EX036.** Apagar ou devolver todos os itens de evidência do ENG-712 quando chegar o dia 90 e escrever um registro curto de que a destruição ou a devolução aconteceu, de quem a fez e de quando.

**EX037.** O F-09, com pontuação 20 na faixa crítica — a página da wiki com uma senha de serviço em texto claro.

**EX038.** Exemplo: "Contas de VPN de ex-terceirizados (T1078) poderiam permitir que um ex-terceirizado alcançasse o jump host de gerenciamento e perturbasse as operações do portal dos funcionários (disponibilidade/integridade)."

**EX039.** Elevar a urgência (por exemplo, tratar o chamado como devido nesta semana), mesmo com a severidade continuando baixa, porque a sondagem ativa a partir da internet aumenta a chance de a fraqueza ser encontrada antes de um ciclo rotineiro de correção.

**EX040.** SP 800-115: revisão (revisão de configuração) ou, se for para confirmar a aplicação do controle, validação de vulnerabilidades do alvo. PTES: análise de vulnerabilidades (ou uma fase vizinha claramente justificada). Nomear as duas com uma justificativa curta recebe 3.

**EX041.** Exemplo: "Inventariar os serviços em escuta apenas nos prefixos em escopo, na taxa de requisições combinada e dentro da janela das ROE, com os endereços de pagamento de tarifas excluídos."

**EX042.** Os IDs de técnica permitem que defensores e relatórios mapeiem comportamentos de forma consistente sem fornecer procedimentos operacionais de ataque, que este livro educacional deliberadamente não traz.

**EX043.** A2 fica retida porque a atividade ("password spraying") não está na lista aprovada. A3 fica retida porque 192.0.2.140 está fora do /25 em escopo.

**EX044.** `['A1', 'A4']`. A lista é a evidência de que apenas as ações que passaram pelos controles de alvo, horário e atividade foram registradas como executadas.

**EX045.** Respeitar a nota de fragilidade das ROE — limitar a taxa ou passar para revisão de configuração — e, se a nota não estiver clara, perguntar à equipe branca antes de prosseguir, mesmo que os controles rígidos tenham passado.

**EX046.** Uma equipe branca com autoridade de parada e uma revisão estruturada de aprendizado ou de repetição depois do exercício. O desenho de cenários guiado por inteligência de ameaças também é aceito como segunda ideia.

**EX047.** Exemplo: "Todos os sistemas de pagamento de tarifas estão excluídos de todas as atividades, incluindo os hosts em 192.0.2.64/27 e qualquer nome sob fare.trt.example."

**EX048.** A decisão do primeiro engajamento é sobre a eficácia dos controles de identidade; o fuzzing intrusivo aumenta o risco ligado à fragilidade e pode exceder as ROE. Escolha verificações que respondam à decisão dentro dos limites combinados.

**EX049.** Quaisquer quatro entre: nome, versão, responsável/mantenedor, finalidade, dados tratados, ambiente aprovado, referência de checksum/assinatura.

**EX050.** Manter a versão fixada. Adiar a atualização de funcionalidades para depois da janela; só considerar uma mudança no meio da janela se for uma correção de segurança e a equipe branca concordar por escrito.

**EX051.** O script não tem responsável nem verificação de integridade, pode executar atividades que as ROE proíbem e pode guardar ou transmitir evidências fora das regras de tratamento aprovadas.

**EX052.** Exemplo: remover a senha da wiki e guardá-la no cofre de segredos aprovado (Protect); responsável = responsável pela wiki/pelo serviço; verificação = varredura automatizada de segredos no espaço da wiki mais uma revisão por amostragem em 30 dias.

**EX053.** Exemplo: forçar o caminho legado a passar por um jump host com MFA e gravação de sessões, reduzir a duração da sessão para uma hora e acompanhar uma data para aposentar o caminho legado.

**EX054.** Exemplo: "Em 2026-11-10, dentro do escopo do portal dos funcionários do ENG-712, os achados de identidade relatados anteriormente foram corrigidos e retestados; o risco residual fora desse escopo permanece."

**EX055.** alerted 3/7 = 42.9%; logged 2/7 = 28.6%; missed 2/7 = 28.6%.

**EX056.** Exemplo: "Detectar T1021 Remote Services nos jump hosts — alertar o SOC sobre sessões interativas fora das janelas de mudança."

**EX057.** O objetivo do exercício era detecção e resposta. Uma linha de log que ninguém vê não produz resposta, então o resultado não cumpre o objetivo, mesmo com a telemetria existindo.

**EX058.** Ferramenta (ambiente do testador): corrigir o relógio via NTP ou ajuste manual, conferir o horário com o relógio da equipe branca e executar de novo o verificador de ROE antes de qualquer outra ação.

**EX059.** Suspender as atividades que possam acrescentar ruído ou risco, avisar imediatamente a equipe branca e retomar apenas por instrução escrita, depois que o comandante do incidente concordar.

**EX060.** Quaisquer cinco entre: descrição do evento, carimbo de tempo, classe da falha, pessoas informadas, decisão (go/no-go), condições para retomar, assinatura/nome de quem decidiu.

**EX061.** Exemplo: pedidos de parada da equipe branca → CISO/gestor de segurança de plantão; chamados de achados → responsável pela gestão de vulnerabilidades; acesso ao cofre de evidências → engenharia de segurança. Outros trios coerentes recebem 3.

**EX062.** Um PDF não tem campo de responsável, prazo nem estado de fluxo de trabalho, então a correção empaca, a menos que alguém copie à mão cada achado para um controle.

**EX063.** Exigir todos os achados no controle aprovado da TRT, migrar o que já estiver no quadro privado e desativar o quadro, para que evidências e status não possam divergir.

**EX064.** O F-09 aparece primeiro porque sua severidade é crítica, que o gerador classifica acima de alta e baixa.

**EX065.** Exemplo: aprovar mudanças de escopo e emitir um go/no-go depois de um incidente. A autoridade de parada da equipe branca e a decisão final sobre severidade também pontuam.

**EX066.** Registrar o hash do commit ou o digest SHA-256 do script na pasta do engajamento, ao lado da tabela gerada, para que um revisor possa regenerá-la e comparar.

**EX067.** Ela premia encontrar mais problemas, mesmo por métodos inseguros, e ignora se a equipe ficou no escopo, se os defensores aprenderam e se a correção começou.

**EX068.** Exemplo: "Para cada técnica não detectada na matriz de cobertura, um chamado de backlog de detecção, com responsável e ID do ATT&CK, é aberto em até cinco dias úteis."

**EX069.** Exemplo: Parar — atualizações de ferramentas no meio da janela sem o aval da equipe branca. Começar — verificação de sincronização de relógio antes da abertura. Continuar — pipeline de três controles com registro do operador. Outros trios coerentes recebem 3.

**EX070.** Exemplo: "Ao longo de dois ciclos purple trimestrais na TRT, que percentual das técnicas do ATT&CK exercitadas passou de missed para alerted?"

**EX071.** Marcar o n como MISSING e revisar o resumo antes da submissão; sem o tamanho da amostra, os leitores não conseguem julgar a afirmação.

**EX072.** Exemplo: "Este estudo usa apenas logs sintéticos de exercícios e não envolve sistemas reais da TRT nem dados pessoais."

**EX073.** Líder: responde pela aderência às ROE e pelo cronograma. Evidências: custódia, hash e higiene do repositório. Elo de ligação: comunicação com a equipe branca/o SOC e confirmações por escrito.

**EX074.** Parar de testar esse nome, reler a lista aprovada e fazer o elo de ligação obter uma decisão por escrito da equipe branca antes de qualquer outra ação.

**EX075.** Quaisquer quatro entre: controles aprovados, HOLDs e seus motivos, itens de evidência contados/com hash, riscos para a entrega, progresso nos critérios de avaliação declarados de antemão, perguntas em aberto para a equipe branca.

**EX076.** Quaisquer cinco entre: tabela executiva de achados, folhas por achado, página de risco residual/incógnitas, índice de evidências com hashes, nota de ACL/transferência, janela de reteste reservada, cópia do método/das ROE.

**EX077.** Exemplo: "Os sistemas de pagamento de tarifas (192.0.2.64/27 e fare.trt.example) foram excluídos; este engajamento não oferece nenhuma garantia sobre esses sistemas."

**EX078.** Confirmar que os operadores da TRT conseguem abrir o pacote de evidências sob a nova ACL e depois revogar a VPN e as permissões no cofre da Northpoint, para que a correção nunca perca o acesso às provas.

**EX079.** F-01 VALIDATED; F-07 REOPENED; F-09 NOT RETESTED - no fix declared.

**EX080.** Deixar o F-07 aberto (não validado). Escalar para o responsável pela correção e para o CISO; encerrar apenas depois de um reteste bem-sucedido ou de uma aceitação de risco por escrito.

**EX081.** Quaisquer três entre: aprovador nomeado, motivo, declaração de risco residual, data de revisão/vencimento, escopo da aceitação, ID do achado vinculado.

**EX082.** Se o cofre ou a VPN estiverem indisponíveis, ainda é preciso ter o escopo, as exclusões e os números de contato de emergência; o papel ou uma cópia offline criptografada mantém os controles aplicáveis.

**EX083.** Parar imediatamente as verificações ativas, confirmar o congelamento com a equipe branca e com o gestor de mudanças e reagendar dentro de uma janela escrita.

**EX084.** Exemplo: "A atividade de T1021 das 22:10 às 22:50 não gerou alerta no SOC; o chamado de backlog de detecção DET-19 foi aberto."

**EX085.** Quaisquer oito entre: pedido/decisão, listas de escopo, ROE, declaração de método, inventário do kit, plano de evidências, escala de classificação, modelo de relatório, plano de reteste, critérios de avaliação.

**EX086.** O colega consegue executar os verificadores pertinentes sobre as suas listas, e os veredictos impressos batem com o que a sua documentação previa.

**EX087.** Apagar a página, lembrar à equipe o limite educacional do Capítulo 10 e recusar qualquer conteúdo procedimental de uso dual na entrega.

**EX088.** Exemplo: recusar começar sem uma equipe branca alcançável; recusar qualquer atividade no pagamento de tarifas; recusar fornecer procedimentos de exploração. A ampliação de escopo pelo chat e os depósitos de evidências em notebook pessoal também contam.

**EX089.** Um resultado logged significa que a telemetria existia, mas o objetivo de detectar e responder falha se nenhum analista ou playbook foi notificado a tempo de agir.

**EX090.** O próximo é o curso 089, segurança de IA e aprendizado de máquina (tecnólogo). Não afirmar que este rascunho é uma qualificação acreditada nem que passou pelos controles de 300 páginas A4 e de revisão independente.

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
