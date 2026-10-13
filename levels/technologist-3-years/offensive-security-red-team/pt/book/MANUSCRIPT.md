# Segurança Ofensiva Autorizada e Red Team: Um Livro para o Tecnólogo

- Idioma: português do Brasil (`pt`); curso de tecnólogo, três anos; aproximadamente 2.400 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–15 de 30 já estão escritos em português, com os exercícios EX001–EX045 e suas resoluções com rubricas de 0 a 3 e 6 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 16–30 (EX046–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) |

Capítulos 16–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-16), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX045 (as de EX046–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). A Tidewater Regional Transit, Priya Natarajan, a Northpoint Assurance e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
