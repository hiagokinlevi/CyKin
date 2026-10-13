# Segurança Ofensiva Autorizada e Red Team: Um Caderno de Trabalho para o Operador Técnico

- Idioma: português do Brasil (`pt`); curso técnico, dezoito meses; aproximadamente 1.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 18 já estão escritos em português, com os exercícios EX001–EX032 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 9–18 (EX033–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: operadores técnicos que configuram verificações, confirmam correções e mantêm seguros os testes autorizados.
- Relação com os livros vizinhos: o [livro do curso profissional](../../../../professional-6-months/offensive-security-red-team/en/book/MANUSCRIPT.md) é mais curto; o [livro de tecnólogo](../../../../technologist-3-years/offensive-security-red-team/pt/book/MANUSCRIPT.md) acrescenta projeto e integração. **Este livro é procedimental e voltado a laboratórios.**
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação acreditada. **Não concede autorização para testar sistemas reais.** Todas as organizações, pessoas e números são **sintéticos**, salvo quando uma frase cita uma fonte pública. Os laboratórios classificam inventários, calculam hashes de evidências e comparam status de reteste — nunca técnicas transformadas em armas.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–5 constroem arquitetura, redes, identidades, scripts e evidências; os capítulos 6–11 cobrem modelagem, telemetria, modos de falha, métodos, configuração e verificação; os capítulos 12–18 são laboratórios, solução de problemas, automação, dependências, documentação, o Laboratório II e o projeto. Cada capítulo traz objetivos, seções didáticas, um exemplo resolvido, um caso sintético rotulado, erros e limites, quatro exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios dos capítulos 2, 5 e 11 leem apenas dados locais (`python3 arquivo.py`).

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Northline Municipal Transit (NMT)** — site, API do planejador de viagens, AD/VPN dos funcionários, rede de tarifas (fora do escopo) | Organização estudada ao longo do livro | Inventada |
| **Sam Park** | Técnico de segurança na NMT | Inventado |

### Fontes principais

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Arquitetura de computação e de serviços

### Objetivos de aprendizagem

Você vai (1) esboçar os principais serviços da NMT; (2) explicar camadas e limites de confiança; (3) localizar onde os testes autorizados costumam começar; (4) identificar dependências frágeis.

### 1.1 Serviços

A NMT opera um site público, uma API de planejamento de viagens, uma intranet dos funcionários, um Active Directory para os empregados, uma VPN e uma rede de cobrança de tarifas que fica fora do escopo dos testes comuns. O trabalho autorizado comum de Sam Park na Northline Municipal Transit cobre o site público, a API do planejador de viagens, a intranet dos funcionários, o Active Directory e a VPN. A rede de cobrança de tarifas aparece em vermelho em todo diagrama e fica fora do ENG-512, a menos que se assinem regras de engajamento (ROE) especializadas. Confundir esses serviços com as catracas de tarifa é o caminho pelo qual operadores pedem sondagens que não podem executar.

### 1.2 Camadas

As camadas de web e de API voltadas para a internet ficam atrás de um balanceador de carga; os servidores de aplicação conversam com os bancos de dados; a identidade dos funcionários fica no AD. Limites de confiança são os pontos em que pacotes ou credenciais passam de zonas menos confiáveis para zonas mais confiáveis. Na NMT, o balanceador de carga atende tanto o site público quanto a API do planejador de viagens, então um único conjunto de regras do WAF cobre os dois. O limite do AD importa porque uma senha de funcionário obtida por phishing atravessa da VPN para a zona dos funcionários. As verificações do ENG-512 feitas por Sam começam do lado de fora do WAF e param antes da rede de tarifas, porque cruzar essa linha sem autorização especializada está fora do escopo.

### 1.3 Onde os testes começam

Testes técnicos autorizados costumam começar pelas camadas de web e de API voltadas para a internet e pelo acesso remoto dos funcionários, porque é isso que estranhos e funcionários vítimas de phishing alcançam primeiro. Estranhos alcançam o site e a API do planejador de viagens, enquanto credenciais de funcionários obtidas por phishing alcançam a VPN; por isso esses três vêm primeiro. Validadores de tarifa e equipamentos de rádio não são pontos de partida para janelas comuns. A folha de abertura do ENG-512 lista, portanto, o site, a API do planejador de viagens e a VPN dos funcionários nessa ordem, com os validadores de tarifa na lista de itens intocáveis, e nenhuma ferramenta roda antes de ela ser lida. Começar por outro lugar é um erro de escopo, mesmo que uma ferramenta facilite.

### 1.4 Dependências frágeis

Catracas de tarifa e sistemas de rádio podem prejudicar a operação se forem perturbados. Eles ficam excluídos, a menos que um engajamento especializado diga o contrário. Um validador travado numa estação movimentada no pico da manhã transformaria um teste num incidente visível para os passageiros. A folha de abertura de Sam lista validadores de tarifa e rádio entre os itens intocáveis, ao lado do nome do contato de operações, e as ROE do ENG-512 repetem a exclusão na mesma frase que define a janela de sábado, para que ninguém trate a tarifa como um desvio interessante. Um trabalho especializado em tarifas exigiria verba separada, outras ROE e operadores treinados em validadores; as janelas comuns de sábado nunca herdam esses direitos. Sam repete esse limite quando gestores pedem só uma olhadinha.

### 1.5 Disciplina do diagrama de arquitetura

Sam mantém um diagrama datado, com responsáveis em cada caixa. A data fica no carimbo do diagrama, ao lado das iniciais do responsável pela rede na última confirmação. Testar contra um diagrama desatualizado causa erros de escopo, como sondar um host de homologação aposentado que agora compartilha o nome com a produção. Antes do ENG-512, Sam pede ao responsável pela rede que confirme por escrito a data do diagrama e arquiva essa confirmação no chamado do ENG-512 antes de o lab_ports rodar. Um diagrama sem essa confirmação é tratado como não confiável, mesmo que pareça familiar.

### 1.6 Janelas de mudança

Mudanças de arquitetura, como um novo gateway de API ou uma atualização do AD, disparam uma revisão das ROE antes do próximo teste. A lista de gatilhos fica no topo das ROE, para que o responsável pela rede saiba quais mudanças exigem uma nova assinatura. Sam não reaproveita a janela de ENG do trimestre anterior se o planejador de viagens passou para trás de um novo conjunto de regras do WAF sem uma atualização assinada. Depois de uma atualização do AD, ele confere de novo os grupos da tst-sam-web e o MFA antes da próxima janela. Reaproveitar as ROE do trimestre anterior sem essa verificação é o caminho pelo qual direitos vencidos sobrevivem.

### 1.7 Contatos dos responsáveis no diagrama

Cada caixa do diagrama de Sam nomeia uma pessoa, e não apenas uma equipe. Quando surge um achado na API do planejador de viagens, ele sabe a quem ligar sem procurar num diretório. A caixa da API do planejador de viagens, por exemplo, traz o nome do responsável pela API e um número para fora do horário comercial. Isso economiza minutos durante uma parada, quando o SOC precisa de uma decisão do responsável, e não de uma busca no diretório. Os contatos do diagrama são copiados para a nota de abertura do ENG-512 e para a mensagem de início ao SOC, para que a equipe de plantão da madrugada chegue ao responsável pela API sem ligar para o telefone pessoal de Sam. Um rótulo só com o nome da equipe não basta.

### 1.8 Por que os diagramas envelhecem

Um terceirizado acrescenta uma CDN de homologação e ninguém redesenha a figura. As mudanças de terceirizados só chegam ao diagrama quando alguém registra o redesenho, por isso Sam pergunta ao líder do terceirizado o que mudou desde o último engajamento. Sua primeira tarefa em cada engajamento é confirmar o diagrama por escrito com o responsável pela rede; uma caixa desatualizada é o caminho pelo qual uma lista de serviços aprovados fica errada antes mesmo de o lab_ports rodar. Quando uma CDN de homologação aparece sem redesenho, Sam abre um chamado de atualização do modelo antes de confiar em qualquer serviço novo. Figuras desatualizadas são a causa raiz de muitas surpresas NOT APPROVED.

### Exemplo resolvido (NMT sintética)

Sam desenha a NMT: Internet → WAF → web/API → aplicação → BD; um caminho separado VPN → jump → intranet/AD; a rede de tarifas desenhada em vermelho, fora do escopo.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX001 — Caixas.** Liste cinco serviços da NMT. *Rubrica:* 3 = cinco corretos; 2 = quatro; 1 = dois; 0 = nada.
- **EX002 — Limite de confiança.** Dê um limite de confiança do desenho de Sam. *Rubrica:* 3 = por exemplo, Internet para WAF/web, ou VPN para jump; 2 = vago; 1 = tentativa mínima; 0 = nada.
- **EX003 — Por que a tarifa está em vermelho.** Por que a cobrança de tarifas fica fora do escopo comum? *Rubrica:* 3 = impacto na operação/segurança se perturbada; exige autorização especializada; 2 = parcial; 1 = "antiga"; 0 = nada.
- **EX004 — Ponto de partida.** Onde começam os testes autorizados comuns na NMT? *Rubrica:* 3 = web/API voltadas para a internet e acesso remoto dos funcionários; 2 = parcial; 1 = catracas de tarifa; 0 = nada.

### Síntese

A arquitetura mostra camadas, limites de confiança e exclusões antes que qualquer ferramenta rode.

### Continue estudando — capítulo 01 de 18

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) ler portas comuns numa lista aprovada; (2) sinalizar serviços em escuta não aprovados a partir de uma lista sintética; (3) explicar por que a escolha de protocolo importa para os testes; (4) evitar varreduras sem autorização.

### 2.1 Serviços em escuta aprovados

A NMT publica uma lista aprovada para a VLAN web de homologação: 80/http, 443/https, 22/ssh-jump. Qualquer outra coisa é relatada, e não tratada como "interessante para cutucar".

```python
"""Lab 2: classify synthetic listening ports against an approved service list (no scanning)."""
approved = {80: "http", 443: "https", 22: "ssh-jump"}
observed = [(80, "http"), (443, "https"), (22, "ssh"), (3389, "rdp"), (8080, "http-alt")]
for port, name in observed:
    if port not in approved:
        print(f"{port:5}/{name:8} NOT APPROVED - report")
    elif name.split("-")[0] != approved[port].split("-")[0]:
        print(f"{port:5}/{name:8} unexpected name (expected {approved[port]})")
    else:
        print(f"{port:5}/{name:8} ok")
```

Execute com `python3 lab_ports.py`. Saída verificada:

```text
   80/http     ok
  443/https    ok
   22/ssh      ok
 3389/rdp      NOT APPROVED - report
 8080/http-alt NOT APPROVED - report
```

O bloco verificado do lab_ports é colado no caderno do ENG-512: 80, 443 e 22 com ok; 3389/rdp e 8080/http-alt com NOT APPROVED - report. Os serviços em escuta aprovados de Sam são apenas os da lista assinada; qualquer outro vira achado, e não um alvo bônus de varredura. Essas duas linhas viram chamados no mesmo dia. Como o laboratório lê uma lista fixa, executá-lo de novo imprime as mesmas cinco linhas até que o próprio inventário mude.

### 2.2 Noções de protocolo

HTTP/HTTPS transportam o site e a API; o SSH alcança os jump hosts; RDP numa VLAN web é inesperado. Os testadores descrevem o que veem sem enviar tráfego de exploração. As notas de método de Sam nomeiam as noções de protocolo do ENG-512: HTTPS para as verificações do planejador de viagens, SSH apenas para jump hosts nomeados e RDP como serviço em escuta não aprovado a ser relatado. Ele não inventa verificações de protocolos exóticos fora das ROE, e a identidade do protocolo ainda depende do mapa de portas do lab_ports. A curiosidade sobre protocolos além dessa lista espera por uma mudança nas ROE.

### 2.3 Nada de varredura livre

Até listar portas em produção exige autorização; o laboratório deste capítulo apenas classifica offline uma lista sintética. Nada de varredura livre significa que Sam não acrescenta portas porque uma ferramenta as sugeriu. Se 3389 ou 8080 aparecem como NOT APPROVED, ele as relata e para; a expansão livre do ENG-512 é o caminho pelo qual hosts vizinhos da rede de tarifas são tocados por acidente. A abertura inclui a leitura em voz alta da linha que proíbe a varredura livre. Portas sugeridas por ferramentas vão para um chamado de estacionamento, nunca para o inventário ativo no meio da janela. O chamado é revisto com o responsável pela rede depois da janela, e só uma mudança assinada nas ROE pode promover uma porta estacionada à lista aprovada.

### 2.4 Nomes divergentes

A porta 22 rotulada apenas como "ssh" ainda corresponde, no laboratório, à família aprovada ssh-jump, mas Sam anota o nome no inventário para limpeza. Divergências de nome de outro tipo, um rótulo de DNS que aponta para um IP diferente da lista de hosts das ROE, são condições de pausa. Sam consulta o responsável pela rede antes de continuar; supor que api-staging é seguro porque o nome diz homologação já causou erros de escopo na NMT. Uma pausa por divergência de DNS registra o nome consultado, a resposta, o endereço das ROE e a resposta do responsável. Retomar sem essa resposta por escrito reprova na revisão por pares.

### 2.5 Caminhos de saída

Notebooks de funcionários que alcançam a homologação e a internet podem servir de ponte entre ambientes; as ROE dizem quais redes de origem são permitidas. Os caminhos de saída a partir dos jump hosts de homologação são listados para que Sam saiba quais destinos externos suas verificações podem atingir. Se um jump host de homologação passa de repente a alcançar um prefixo ou uma nuvem de um fornecedor de tarifas, Sam interrompe a janela e pede à equipe de rede que classifique o caminho por escrito. Perseguir esse caminho como descoberta no meio da janela está fora do escopo, por mais interessante que pareça.

### 2.6 Registro

As equipes de rede podem espelhar as origens de teste autorizadas; Sam coordena para que seu tráfego seja atribuível. O registro de início, parada e pausas do ENG-512 vai para o canal do engajamento, e cada linha traz o ID do chamado e o horário, para que o SOC possa filtrar o ruído dos testes. O SOC usa essas linhas quando os aplicativos dos passageiros ficam lentos; o silêncio os deixa adivinhando se as verificações de Sam estão envolvidas. O texto do exercício do laço das 10:12, do Capítulo 8, é reaproveitado quando acontece uma parada real, para que a equipe de resposta reconheça o formato na hora.

### 2.7 Identidade TCP versus identidade da aplicação

Uma porta aberta não é o mesmo que um serviço seguro. Sam registra tanto a porta quanto o banner da aplicação ou o nome do certificado, quando o inventário permite. A porta 443 aberta em TCP não prova que a API do planejador de viagens está saudável; a identidade da aplicação ainda exige um cartão de método. Depois que as portas são classificadas sem problemas, Sam executa o cartão de método de aplicação no planejador de viagens e registra os dois resultados, para que os achados não sejam um teatro só de portas. Uma porta TCP verde, sozinha, nunca vira atestado de saúde.

### 2.8 Relato de serviços em escuta não aprovados

Não aprovado não significa "explorar agora". Significa abrir um chamado, anexar a observação sintética e esperar que o responsável confirme se o serviço deveria existir. Por isso, 3389/rdp e 8080/http-alt saem do ENG-512 como achados com responsáveis, e não como notas silenciosas. Sam os registra no mesmo dia, citando literalmente as linhas NOT APPROVED do lab_ports, para que a equipe de rede possa desativá-los ou autorizá-los antes do próximo sábado, em vez de deixá-los como folclore de chat que os examinadores nunca veem. O encerramento é a desativação ou uma autorização futura deliberada, e não um silêncio conveniente.

### Exemplo resolvido (NMT sintética)

Sam classifica a lista sintética: 80, 443 e 22 estão ok; 3389/rdp e 8080/http-alt estão NOT APPROVED. Ele abre um chamado para os dois serviços em escuta não aprovados na homologação.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX005 — Não aprovados.** Quais dois serviços em escuta o laboratório marca como NOT APPROVED? *Rubrica:* 3 = 3389/rdp e 8080/http-alt; 2 = um; 1 = errado; 0 = nada.
- **EX006 — Por que o RDP importa.** Por que RDP na VLAN web é uma preocupação? *Rubrica:* 3 = exposição inesperada de área de trabalho remota; ampla superfície de ataque; 2 = parcial; 1 = tudo bem; 0 = nada.
- **EX007 — Autorização.** Sam pode fazer varredura de portas na produção para montar a própria lista? *Rubrica:* 3 = não sem autorização por escrito; 2 = não; 1 = sim; 0 = nada.
- **EX008 — Acompanhamento do inventário.** O que Sam faz, depois do laboratório, a respeito do nome ssh? *Rubrica:* 3 = anotar a limpeza do nome no inventário; continuar usando o processo de jump; 2 = parcial; 1 = ignorar; 0 = nada.

### Síntese

Listas aprovadas transformam portas cruas em chamados; a varredura livre continua proibida.

### Continue estudando — capítulo 02 de 18

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem

Você vai (1) separar identidades locais, de domínio e de aplicação; (2) explicar o menor privilégio para contas de teste; (3) tratar contas compartilhadas como achados; (4) proteger credenciais de teste.

### 3.1 Camadas de identidade

Estações de trabalho têm contas locais; os funcionários usam contas de domínio do AD; o planejador de viagens tem usuários de aplicação. Um achado pode envolver qualquer camada. Na NMT, as camadas incluem contas voltadas aos passageiros, contas de funcionários no AD, certificados de VPN e contas de serviço do planejador de viagens. A identidade de teste de Sam, a tst-sam-web, fica apenas na camada de funcionários/homologação e é barrada, por construção, dos grupos do AD da rede de tarifas. Sam confere os grupos dela na abertura, antes da retirada no cofre, para que as camadas de identidade continuem separadas sob pressão. Uma mudança de grupo encontrada na abertura é corrigida pela equipe de identidade antes de a janela abrir, e nunca contornada.

### 3.2 Contas de teste

Testes autorizados usam contas de teste nominais com o menor privilégio necessário, emitidas para a janela e revogadas depois dela. Contas "deus" compartilhadas de pentest são, elas mesmas, um achado. A conta de teste tst-sam-web tem acesso de leitura apenas à homologação, fica guardada no cofre para o ENG-512 e expira automaticamente no domingo à noite. Sam não compartilha essa senha no chat; a retirada no cofre é o único caminho, e os registros de retirada ficam no pacote do ENG-512. A expiração de domingo é comprovada por uma tentativa de login na segunda-feira que precisa falhar; um sucesso seria um achado.

### 3.3 Contas de serviço

Contas de API e de automação costumam ter direitos amplos e monitoramento fraco. São alvos de revisão de alto valor quando estão no escopo. As contas de serviço da API ficam fora do conjunto comum de testes de Sam, a menos que as ROE as nomeiem. Usar uma senha de serviço compartilhada porque ela foi colada num chamado antigo viola as regras de manuseio de credenciais e confunde as notas de ATT&CK T1078 para o SOC. Senhas de contas de serviço encontradas em wikis são trocadas pela equipe de identidade, e não emprestadas para testes. Sam registra a exposição e usa apenas identidades de teste guardadas no cofre.

### 3.4 Manuseio de credenciais

Senhas de teste ficam no cofre, e não no chat, em capturas de tela ou em scripts enviados ao git. Sam remove tokens das evidências antes de calcular o hash; um token num PNG reprova na regra de evidência por duas pessoas, mesmo que o achado seja real. Por isso, os PNGs de evidência são recortados no jump host antes de o lab_hash rodar. Calcular o hash de uma imagem que contém um segredo e apagá-la depois ainda deixa o segredo no histórico de backup, que dura mais que o engajamento. Se um segredo chega a um arquivo de evidência, Sam relata o fato, a equipe de identidade troca a credencial e o recorte limpo substitui o original no índice de evidências.

### 3.5 Estações administrativas

Os jump hosts devem ser o único caminho para tarefas administrativas; testes que encontram RDP administrativo direto a partir de VLANs de e-mail importam. As estações administrativas que Sam usa nos testes são jump hosts fornecidos pela NMT. Notebooks pessoais não guardam evidências, e Sam não copia nada do jump host para um celular ou disco doméstico durante o ENG-512; a política de jump da NMT bloqueia clientes pessoais de sincronização em nuvem. Sua lista de limpeza confirma que nenhum arquivo de ENG ficou na pasta Downloads do jump host depois da janela, e a verificação é marcada no pacote do ENG-512 antes de ele ser fechado.

### 3.6 Ligação com o ATT&CK

O abuso de contas legítimas corresponde ao T1078 Valid Accounts, o que é útil ao escrever recomendações de detecção. Sam acrescenta esse rótulo quando um achado trata de credenciais de funcionários roubadas ou reutilizadas, para que o SOC possa buscar por um nome comum; o rótulo não prova a existência de um atacante externo. Quando achados de autenticação são entregues, o assunto do chamado do SOC inclui o T1078 e a janela de tempo. Identificadores de passageiros nunca são colados nesse assunto, porque os assuntos dos chamados do SOC são copiados para painéis e resumos por e-mail que muitos leitores veem. Os detalhes ficam no pacote de evidências restrito, onde o acesso é registrado.

### 3.7 Dia da revogação

No domingo à noite, Sam verifica se a tst-sam-web foi desativada. Contas de teste esquecidas estão entre os achados mais comuns que ele escreve sobre outras equipes, e ele não vai virar um deles. Se o ENG-512 se estender até a segunda-feira, Sam pede uma nova conta com prazo definido, em vez de pedir a alguém que prorrogue a antiga em silêncio. Se tarefas de segunda-feira ainda se autenticam como tst-sam-web, ele abre um chamado com severidade antes de qualquer outro trabalho do dia. O dia da revogação é um controle, não uma sugestão, e seu resultado é registrado no pacote do ENG-512 como qualquer outra verificação.

### 3.8 MFA nas contas de teste

Onde a NMT exige MFA, as contas de teste também recebem MFA. Dispensar o MFA "porque é homologação" ensina maus hábitos e enfraquece a homologação como campo de prova. O MFA nas contas de teste é exigido da mesma forma que na VPN dos funcionários. Uma conta de teste sem MFA é, ela própria, um achado; Sam não defende uma exceção de MFA para facilitar os scripts. Um desafio de MFA ao vivo na abertura é obrigatório, e uma conta de teste com MFA cadastrado, mas com falha na entrega por SMS ou aplicativo, interrompe o ENG-512 até que a equipe de identidade a conserte.

### 3.9 Disciplina de campo

Quando Sam recebe uma nova conta de teste, ele percorre uma lista de quatro passos: confirmar que a conta está em seu nome, confirmar que os grupos correspondem às ROE, guardar o segredo no cofre sob o ID do engajamento e marcar no calendário um lembrete para o dia da revogação. Pular qualquer passo já custou caro à NMT: uma conta compartilhada ficou em Domain Admins depois que um terceirizado saiu. A disciplina de campo para identidades se resume, portanto, a contas de teste no cofre, expiração no domingo, MFA ativo e nenhum grupo da rede de tarifas na tst-sam-web. Antes da janela, os colegas conferem esses quatro pontos num teste rápido, e respostas erradas adiam a janela. Sam trata a higiene de contas como parte do ofício de testar, e não como papelada de outra pessoa.

### Exemplo resolvido (NMT sintética)

Sam recebe a conta tst-sam-web com acesso de leitura apenas à homologação, guardada no cofre para o ENG-512 e com expiração automática no domingo à noite.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX009 — Camadas.** Nomeie as três camadas de identidade do capítulo. *Rubrica:* 3 = local, domínio/AD, aplicação; 2 = duas; 1 = uma; 0 = nada.
- **EX010 — Conta de teste com menor privilégio.** Que direitos a tst-sam-web deve ter? *Rubrica:* 3 = apenas os direitos de homologação necessários às verificações das ROE; 2 = parcial; 1 = administrador do domínio; 0 = nada.
- **EX011 — Conta "deus" compartilhada.** Por que uma conta administrativa de pentest compartilhada é um achado? *Rubrica:* 3 = sem responsabilização; excesso de privilégio; acesso remanescente; 2 = parcial; 1 = conveniente, tudo bem; 0 = nada.
- **EX012 — Cofre.** Onde ficam as senhas de teste? *Rubrica:* 3 = cofre aprovado; não no chat/git; 2 = cofre; 1 = post-it; 0 = nada.

### Síntese

Contas nominais, de menor privilégio, guardadas no cofre e com prazo definido tornam os testes responsabilizáveis.

### Continue estudando — capítulo 03 de 18

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem

Você vai (1) analisar com segurança evidências simples em JSON/CSV; (2) evitar executar artefatos não confiáveis; (3) manter os scripts reproduzíveis; (4) registrar as versões do interpretador.

### 4.1 Por que scripts

Técnicos automatizam comparações de inventário, verificações de hash e a formatação de chamados, e os scripts precisam ser legíveis pela próxima pessoa. Os scripts existem para que Sam possa repetir verificações no estilo do lab_ports e calcular hashes de evidências do mesmo jeito todo sábado. Eles não existem para inventar novos caminhos de ataque; todo script do ENG-512 corresponde a um cartão de método da lista assinada. Os cabeçalhos dos scripts citam os IDs dos cartões de método, para que a automação não se afaste dessa lista, e scripts órfãos, sem citação, são apagados da pasta de tarefas de sábado.

### 4.2 Dados não confiáveis

Arquivos vindos dos alvos são dados, e não código. Não execute binários ou macros desconhecidos de um alvo de teste numa estação administrativa. Dados não confiáveis incluem o JSON da API de homologação e qualquer arquivo que uma ferramenta grave. Sam valida as estruturas antes de analisá-las, e a validação de esquema descarta chaves JSON desconhecidas antes do registro. Um campo inesperado que parece um ID de transação de tarifa é mascarado e escalado, e não registrado por inteiro; campos com cara de pagamento nas respostas da homologação são tratados como sensíveis mesmo fora da produção, porque os dados de homologação às vezes são copiados de sistemas em operação.

### 4.3 Reprodutibilidade

Fixe as versões do Python, defina a semente de qualquer aleatoriedade e guarde os arquivos de entrada ao lado do script no pacote de evidências. Reprodutibilidade significa que outro técnico pode executar o mesmo script sobre o mesmo inventário e obter as mesmas linhas ok e NOT APPROVED. Sam fixa as versões dos scripts no caderno, ao lado do ID do chamado do ENG-512. Os colegas reproduzem usando o hash do script registrado no caderno, e hashes divergentes abortam a comparação. A maioria das disputas sobre reprodutibilidade acaba sendo uma disputa de versões, e ela termina quando as versões fixadas coincidem.

### 4.4 Formatos

JSON e CSV são comuns nas exportações de ferramentas, e Sam valida o esquema antes de confiar em campos para um achado. Os formatos de inventários e de índices de evidências são CSV ou texto simples, combinados no runbook. Dumps binários e blobs JSON sem documentação reprovam na conferência por pares, porque o próximo operador não consegue lê-los sob pressão de tempo. As colunas do CSV de inventário são name, ip, port, proto, approved. Reordená-las quebra o lab_ports, por isso Sam valida a linha de cabeçalho antes de a tarefa rodar; um arquivo com uma coluna ausente ou renomeada interrompe a tarefa, em vez de ser classificado em silêncio.

### 4.5 Segredos em scripts

Nada de senhas fixas no código: os scripts leem do cofre ou de um ambiente injetado pelo jump host. Esses são os únicos padrões que Sam aceita na revisão de código da automação do ENG-512. A varredura de segredos antes do merge no repositório de automação reprova o build quando encontra tokens. Sam troca qualquer token que um dia tenha aparecido no diff de um pull request, porque apagar a linha não apaga o histórico que revisores, espelhos e backups já guardam. A troca é registrada no chamado do ENG-512, com o commit que expôs o token, para que um revisor posterior possa confirmar que o valor antigo está morto.

### 4.6 Revisão de código

Outro técnico lê o script de Sam antes que ele rode numa janela de engajamento. A revisão de código pega listas de portas livres e senhas fixas no código antes de uma janela. Uma nota de revisão abaixo do mínimo significa que o script fica fora da lista de tarefas de sábado. Os revisores procuram padrões de host que parecem sub-redes de tarifa e rejeitam esses laços. A revisão de código é um controle de escopo, e não apenas um clube de estilo. O nome do revisor e o hash do script vão para o caderno do ENG-512, para que a tarefa que roda no sábado seja comprovadamente a que foi lida. Um script alterado depois da revisão volta para a fila, mesmo que a correção tenha uma linha só.

### 4.7 Limites de tamanho da entrada

Scripts que leem exportações de ferramentas limitam o tamanho do arquivo, para que um dump enorme não esgote o jump host. Limites são recursos de segurança, e não pessimismo. Limites de tamanho da entrada impedem que um inventário descontrolado trave o jump host. Sam limita as linhas processadas por execução e falha de forma fechada quando o limite é atingido: a tarefa imprime `ERROR: inventory exceeds cap` e sai com código 2. Truncar sem erro esconderia o 8080/http-alt depois da linha de corte. Quando o limite é atingido, Sam confere a exportação com o responsável antes de aumentar o limite numa mudança revisada, em vez de editar o valor no jump host.

### 4.8 Códigos de saída

Os scripts de Sam saem com código diferente de zero em MISMATCH ou NOT APPROVED, para que a integração contínua e as pessoas percebam as falhas em vez de passar os olhos por logs que parecem verdes. Os códigos de saída distinguem serviços em escuta ok de achados NOT APPROVED, para que a integração contínua e as pessoas concordem; tarefas no estilo do lab_ports que sempre saem com zero escondem o 3389/rdp até alguém ler a saída padrão com cuidado. O SOC monitora saídas diferentes de zero dos usuários de tarefas de ENG. Scripts que saem com 0 enquanto imprimem NOT APPROVED são defeitos corrigidos antes do próximo sábado. A lista de revisão de Sam inclui executar cada tarefa sobre uma lista com uma porta não aprovada e confirmar a saída diferente de zero.

### 4.9 Disciplina de campo

O padrão de scripts de Sam é curto o bastante para ser lembrado: um propósito por script, argparse ou constantes explícitas no topo, nenhuma chamada de rede a menos que o caminho do arquivo de ROE seja passado, e um modo --dry-run que imprime o que aconteceria. O dry-run o salvou quando um erro de digitação num caminho teria apontado uma tarefa de hash para a listagem de um compartilhamento de produção. Os revisores procuram o dry-run e a ausência de hosts fixos no código mais do que código engenhoso. A disciplina de campo para scripts acrescenta versões fixadas, árvores sem segredos, limites de tamanho e códigos de saída que batem com o relatório, e o índice do caderno do ENG-512 liga o hash de cada script ao cartão de método que ele implementa.

### Exemplo resolvido (NMT sintética)

O script de verificação de hash de Sam (laboratório do Capítulo 5) recebe uma pasta de evidências e imprime MATCH/MISMATCH; ele nunca abre imagens além de calcular o hash dos bytes.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX013 — Dados, não código.** Por que não dar um duplo clique num .doc vindo do servidor web alvo? *Rubrica:* 3 = pode executar macros/malware no PC administrativo; tratar como não confiável; 2 = parcial; 1 = tudo bem; 0 = nada.
- **EX014 — Itens de reprodução.** Nomeie três coisas que tornam um script reproduzível. *Rubrica:* 3 = versão, entradas, semente/configurações; 2 = duas; 1 = uma; 0 = nada.
- **EX015 — Segredos.** Como um script deve obter uma senha de homologação? *Rubrica:* 3 = cofre/injeção pelo ambiente; não fixa no código; 2 = parcial; 1 = fixar no código; 0 = nada.
- **EX016 — Leitura por um colega.** Por que outro técnico lê o script primeiro? *Rubrica:* 3 = pegar defeitos de escopo/segurança; entendimento compartilhado; 2 = parcial; 1 = burocracia; 0 = nada.

### Síntese

Scripts são ferramentas controladas: reproduzíveis, sem segredos e revisadas.

### Continue estudando — capítulo 04 de 18

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Escopo de segurança e evidências

### Objetivos de aprendizagem

Você vai (1) reformular as verificações das ROE para técnicos; (2) calcular hashes de arquivos de evidência; (3) rejeitar evidências divergentes; (4) minimizar dados pessoais nas capturas.

### 5.1 ROE do técnico

Antes de qualquer comando, Sam confere o host alvo, o método e a janela contra a folha de ROE apoiada no joelho. As ROE do técnico para o ENG-512 indicam as verificações de web/API de homologação e de VPN, a janela de sábado, o contato de emergência e a rede de tarifas como excluída. Sam não começa se o emergency_contact estiver vazio; a lista de verificação é o mesmo hábito ensinado nos laboratórios do curso profissional. Um emergency_contact vazio cancela o ENG-512 antes de as ferramentas começarem, e Sam publica o cancelamento nomeando o campo ausente, para que o SOC não espere tráfego naquela manhã. A janela só é remarcada depois que o responsável pelas ROE preenche o campo e assina a folha de novo.

### 5.2 Hashes

Calcular o hash das evidências detecta edições acidentais. Uma divergência significa não anexar o arquivo até que sua origem esteja clara.

```python
"""Lab 5: verify synthetic evidence file hashes before attaching to a finding."""
import hashlib
files = {"shot1.png": b"fake-png-bytes-v1", "shot1-edited.png": b"fake-png-bytes-v2",
         "config.txt": b"PermitRootLogin no\n"}
recorded = {k: hashlib.sha256(v).hexdigest() for k, v in files.items() if k != "shot1-edited.png"}
recorded["shot1.png"] = hashlib.sha256(b"fake-png-bytes-v1").hexdigest()
# simulate tampering record for edited shot still labeled shot1
check = {"shot1.png": files["shot1-edited.png"], "config.txt": files["config.txt"]}
for name, data in check.items():
    h = hashlib.sha256(data).hexdigest()
    print(f"{name:12} {h[:12]} {'MATCH' if h == recorded.get(name) else 'MISMATCH'}")
```

Execute com `python3 lab_hash.py`. Saída verificada:

```text
shot1.png    b81db4df801a MISMATCH
config.txt   44c91857f34b MATCH
```

O lab_hash imprime `shot1.png b81db4df801a MISMATCH` e `config.txt 44c91857f34b MATCH`. Sam trata o MISMATCH como uma parada para aquele artefato: o shot1.png fica fora do achado até que duas pessoas concordem com uma nova exportação ou com um hash esperado atualizado. O MATCH no config.txt é o padrão que os chamados devem mostrar depois das correções.

### 5.3 Minimização

Desfoque rostos de passageiros e números de crachá nas capturas de tela; mantenha os pixels que provam o problema. Minimização significa que nomes de passageiros e números de cartão nunca aparecem nas capturas de tela do ENG-512. Uma evidência que prova uma flag de cookie ou uma porta aberta não precisa de um histórico de viagens real, então Sam prova esses problemas apenas com sessões sintéticas e com a moldura recortada da interface, e recorta antes de calcular o hash. Chaves JSON desconhecidas com cara de pagamento são removidas antes que qualquer linha de log saia do jump host para o cofre.

### 5.4 Índice de evidências

Cada arquivo tem um ID, um hash, um horário, um coletor e o ID do achado relacionado. No ENG-512, as linhas do índice trazem o nome do arquivo, um prefixo SHA-256 de doze caracteres hexadecimais, o ID do chamado do ENG-512 e o responsável. Um artefato que não está no índice não faz parte do ENG-512; links de chats pessoais não contam, e artefatos ausentes do índice são apagados como cópias não verificadas. O índice é o que permite a um revisor ligar cada achado do relatório ao arquivo e ao hash exatos que o sustentam.

### 5.5 Integridade versus verdade

Um hash que confere prova que o arquivo não mudou desde o cálculo do hash, e não que o achado no sistema continua verdadeiro. Um MATCH numa captura de tela errada ainda reprova na verificação de verdade. Por isso, Sam valida o caminho do achado e seu impacto com o cartão de método antes de dar a evidência por completa e antes de o relatório sair. Integridade e verdade são registradas como duas marcações separadas no pacote do ENG-512, para que o leitor veja que as duas foram verificadas e por quem. Um achado só com a marcação de integridade continua em rascunho.

### 5.6 Retenção

Siga o calendário de retenção de engajamentos da NMT e apague os caches locais depois de guardar tudo no cofre. A retenção do ENG-512 segue a regra de exclusão em prazo das ROE. Sam agenda a exclusão das evidências do ENG-512 e a confirma; cada registro de exclusão traz a data, o caminho e uma testemunha. PNGs esquecidos no jump host reprovam na verificação de limpeza exigida para o crédito de portfólio. A retenção corta dos dois lados: a evidência é guardada pelo tempo necessário para reteste e contestação, e nem um dia além do que as ROE permitem. A testemunha assina o registro de exclusão, e não apenas Sam.

### 5.7 Fotografar telas

Quando uma captura de tela é necessária, Sam usa as ferramentas do jump host, nomeia o arquivo com o ID do achado e o horário e calcula o hash antes de editar qualquer coisa; o mascaramento é feito numa cópia. Fotografar telas com o celular é recusado quando o jump host pode capturar um PNG mascarado, porque o celular sai do controle da NMT, enquanto as capturas guardadas no cofre ficam no caminho do engajamento. Fotos de tela feitas com celular são rejeitadas na revisão por pares, e a captura no jump host com mascaramento é o único caminho aceito para capturas de tela.

### 5.8 Regra de evidência por duas pessoas

Para achados de alto impacto, um segundo técnico confirma o hash e a observação, e a discordância suspende o registro. Por essa regra, um colega acompanha o cálculo dos hashes dos itens de alto impacto. O MISMATCH no shot1.png é revisto pelas duas pessoas antes que alguém atualize o hash esperado, e o colega fica ao teclado durante o novo cálculo. Atualizações de hash do shot1.png feitas por uma pessoa sozinha são recusadas. O nome do colega é escrito ao lado do novo hash no índice de evidências, para que a aprovação possa ser rastreada depois.

### 5.9 Disciplina de campo

Disputas sobre evidências custam caro. Por isso, Sam calcula o hash logo depois da captura, escreve o hash na linha do registro de atividades e só então mascara uma cópia para o apêndice do relatório. Se o jurídico perguntar mais tarde se uma captura de tela foi alterada, ele pode mostrar o resumo original e o derivado mascarado. O resultado MISMATCH do laboratório é a versão de sala de aula dessa disciplina: bytes editados nunca devem substituir os originais em silêncio, e um MISMATCH é o sinal para chamar uma segunda pessoa, e não para recalcular o hash até que confira. A disciplina de campo para evidências é hash, minimização, índice, retenção e duas pessoas nas divergências; o pacote do ENG-512 de Sam reprova na conferência por pares se faltar qualquer um desses cinco.

### Exemplo resolvido (NMT sintética)

Sam calcula os hashes das evidências: config.txt dá MATCH; shot1.png dá MISMATCH porque os bytes foram editados depois do hash registrado. Ele captura a tela de novo e registra um novo hash.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX017 — Ação diante da divergência.** O que Sam faz com o MISMATCH do shot1.png? *Rubrica:* 3 = não anexar; capturar de novo; novo hash; 2 = parcial; 1 = anexar mesmo assim; 0 = nada.
- **EX018 — Significado do MATCH.** O que o MATCH prova sobre o config.txt? *Rubrica:* 3 = inalterado desde o registro do hash; 2 = parcial; 1 = o sistema está seguro; 0 = nada.
- **EX019 — Minimização.** Dê um exemplo de minimização na NMT. *Rubrica:* 3 = desfocar rostos/crachás/números de cartão; 2 = parcial; 1 = guardar tudo; 0 = nada.
- **EX020 — Folha do joelho.** Quais três fatos estão na folha de ROE que Sam apoia no joelho? *Rubrica:* 3 = host, método, janela (mais o contato de emergência); 2 = dois; 1 = um; 0 = nada.

### Síntese

Escopo na folha do joelho; evidências com hash, minimizadas e indexadas.

### Continue estudando — capítulo 05 de 18

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Modelo de sistema para testes autorizados

### Objetivos de aprendizagem

Você vai (1) construir um modelo de sistema simples para o planejador de viagens; (2) marcar pontos de entrada e repositórios de dados; (3) mapear os temas do OWASP WSTG para o modelo; (4) listar premissas.

### 6.1 Elementos do modelo

Um modelo de sistema nomeia atores (passageiro, funcionário), pontos de entrada (web, API), zonas de confiança, repositórios de dados (BD de viagens, logs) e dependências externas (blocos de mapa). Para a NMT, o modelo diz: passageiro → HTTPS → API → BD de viagens; funcionário → VPN → interface administrativa; blocos de mapa como externos; nuvem de tarifas riscada. O modelo de uma página de Sam é a imagem do escopo antes de as ferramentas rodarem: a nuvem de tarifas e as caixas do fornecedor de blocos de mapa estão riscadas, e há responsáveis nomeados apenas na web, na API e na VPN. As ferramentas ficam fechadas até que essa página esteja atualizada.

### 6.2 Pontos de entrada

Cada ponto de entrada recebe uma lista curta de temas do WSTG: autenticação, sessão, controle de acesso, tratamento de entradas. Na NMT, os pontos de entrada são o site público, a API do planejador de viagens e a VPN dos funcionários. Validadores de tarifa não são pontos de entrada do ENG-512; listá-los como interessantes é um erro de modelo corrigido antes da abertura. Cada um dos três recebe sua própria lista de temas do WSTG, para que as verificações da VPN nunca tomem emprestados os testes de tratamento de entradas da web. Para a VPN dos funcionários, os temas param em autenticação e tratamento de sessão, porque o tratamento de entradas pertence ao site e à API do planejador de viagens. Manter as listas separadas também torna precisa a declaração de cobertura: o relatório pode dizer quais temas foram exercitados em qual ponto de entrada e quais ficaram de fora.

### 6.3 Premissas

"A homologação espelha a autenticação da produção" é uma premissa a validar, e não um fato. Premissas como "a homologação tem a mesma configuração da produção" são escritas no registro de premissas com um responsável, porque premissas não escritas viram brigas de escopo no meio da janela. Cada linha do registro de premissas nomeia quem acreditou nela e a data da última verificação. Uma linha de "a homologação espelha a produção" sem data de verificação é marcada como inválida até que o responsável compare as duas configurações e date a entrada. Achados que dependem de uma premissa inválida ficam fora do relatório até a comparação ser feita.

### 6.4 Fluxos de dados

Anote por onde passam os dados pessoais, como as viagens salvas, para que os testes minimizem a exposição. Os fluxos de dados da NMT mostram consultas de viagem e ações administrativas dos funcionários, e as setas param no BD de viagens e na interface administrativa dos funcionários. Eles não mostram a liquidação de tarifas. Sam se recusa a desenhar fluxos de tarifa no modelo comum, porque desenhar convida a sondar; uma seta de liquidação de tarifas no modelo comum é um defeito de documentação que ele corrige antes do ENG-512. A seta das viagens salvas é a que ele marca para minimização, de modo que as verificações sobre ela usam apenas contas sintéticas.

### 6.5 Fora do modelo

Os validadores de tarifa são omitidos porque estão fora do escopo. Fora do modelo significa a rede de tarifas, o rádio e os processadores de cartão. Essas caixas ficam pretas no mapa de cores e trazem a legenda "somente com ROE especializadas", e os achados do ENG-512 nunca reivindicam cobertura nelas. Deixá-las visíveis, mas pretas, importa: o leitor vê que os sistemas existem e foram excluídos de propósito, em vez de supor que foram esquecidos ou cobertos em silêncio pelos testes comuns. Qualquer pedido de teste dentro de uma caixa preta volta ao responsável pelas ROE como um engajamento separado.

### 6.6 Modelo vivo

Atualize o modelo quando a API ganhar um novo callback de pagamento, mesmo que o pagamento seja de terceiros. O modelo também é atualizado quando uma CDN ou um gateway muda. Sam data cada revisão e guarda a data ao lado do hash das ROE; um modelo mais antigo que a última mudança de arquitetura é inválido para a próxima janela, então, se a arquitetura mudou depois da data do modelo, ele atualiza a figura antes da janela. O histórico de revisões mostra aos revisores contra qual versão do modelo cada janela foi planejada.

### 6.7 Cores das zonas de confiança

Sam pinta a internet de vermelho, a homologação de âmbar, os funcionários de verde e a tarifa de preto (não entrar). O preto é reservado à tarifa para que não possa ser confundido com nenhuma zona onde testar é permitido. A cor torna o escopo visível nas revisões quando os gestores passam os olhos depressa demais para ler as exclusões. O mapa de cores é impresso para a reunião rápida de abertura, para que os gestores que só passam os olhos pelo texto ainda vejam a exclusão. Um mapa impresso em preto e branco perde o sentido, por isso a cópia da abertura também rotula cada zona por escrito.

### 6.8 Registro de premissas

Uma lista corrente de premissas fica embaixo do modelo, e cada uma é marcada como confirmada, rejeitada ou aberta antes de o relatório ser emitido. As entradas nomeiam quem acreditou, por exemplo, que a homologação espelhava a produção e quando isso foi verificado. Premissas que falham viram texto das ROE ou achados; Sam não deixa uma crença quebrada de que a homologação espelha a produção como nota de rodapé não dita. As entradas ainda abertas na hora do relatório são listadas na seção de limitações, para que os leitores saibam quais conclusões dependem de crenças não confirmadas e quem precisa fechá-las.

### 6.9 Disciplina de campo

Construir o modelo de sistema com o responsável pelo produto leva uma hora e evita dias de confusão. Sam projeta um diagrama em branco, pede ao responsável que posicione as caixas e só então acrescenta as próprias setas. Os responsáveis corrigem premissas equivocadas sobre qual banco de dados guarda as viagens salvas e se a interface administrativa compartilha a autenticação com a API dos passageiros, e essas correções mudam quais temas do WSTG importam mais. O registro de premissas anota cada correção com a data em que foi confirmada. A disciplina de campo para a modelagem é um diagrama datado, zonas coloridas, o registro de premissas e a tarifa em preto; Sam não abre as ferramentas do ENG-512 até que esses quatro estejam atualizados, e qualquer lacuna atrasa o início.

### Exemplo resolvido (NMT sintética)

O modelo de uma página de Sam mostra passageiro → HTTPS → API → BD de viagens; funcionário → VPN → interface administrativa; blocos de mapa como externos; nuvem de tarifas riscada.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX021 — Atores.** Nomeie dois atores do modelo. *Rubrica:* 3 = passageiro e funcionário; 2 = um; 1 = vago; 0 = nada.
- **EX022 — Tema do WSTG.** Escolha um ponto de entrada e um tema do WSTG a aplicar. *Rubrica:* 3 = par concreto, por exemplo API + controle de acesso; 2 = parcial; 1 = vago; 0 = nada.
- **EX023 — Verificação de premissa.** Como Sam validaria a premissa de que a homologação espelha a autenticação da produção? *Rubrica:* 3 = comparar configurações/confirmação dos responsáveis; não supor; 2 = parcial; 1 = supor verdadeira; 0 = nada.
- **EX024 — Por que omitir a tarifa.** Por que omitir os validadores de tarifa deste modelo? *Rubrica:* 3 = fora do escopo; 2 = parcial; 1 = sem importância; 0 = nada.

### Síntese

Um modelo de sistema claro concentra o esforço do WSTG e registra as premissas de forma explícita.

### Continue estudando — capítulo 06 de 18

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Dados e telemetria

### Objetivos de aprendizagem

Você vai (1) identificar logs úteis nos testes e na detecção; (2) pedir acesso do jeito certo; (3) evitar despejar dados de produção; (4) usar a telemetria para confirmar achados.

### 7.1 Logs úteis

Os logs úteis nos testes e na detecção incluem logs de acesso web, falhas de autenticação da API, autenticações na VPN, bloqueios do WAF e logins no AD. Para o ENG-512, os logs úteis são as permissões e negações do WAF, as falhas de autenticação da API, os inícios de sessão na VPN e os comandos no jump host. Despejos completos da produção são recusados; Sam pede amostras do WAF e da autenticação da API apenas para o horário da janela do ENG-512. Logs úteis são esses recortes, e não despejos de vários dias. Pedir o recorte com antecedência, com os horários da janela escritos no pedido, permite ao SOC prepará-lo antes do sábado, em vez de procurá-lo durante o teste.

### 7.2 Caminho de acesso

Sam pede acesso somente leitura aos logs durante a janela por meio das ROE, e não usando a senha do SIEM de outra pessoa. O caminho de acesso aos logs é somente leitura, pelo chamado do SOC, e não um papel administrativo pessoal na produção, e o acesso somente leitura basta. Elevar a tst-sam-web a administradora de logs da produção é recusado, mesmo quando o SOC demora a responder ao chamado; a conta de teste de Sam nunca vira um atalho para administrar logs. A disciplina do caminho de acesso limita o raio de impacto se a conta de teste um dia for mal usada.

### 7.3 Nada de despejos da produção

Exportar tabelas inteiras de usuários para análise está fora dos limites; use amostras sintéticas ou minimizadas. Nada de despejos da produção significa nenhuma exportação completa da tabela de histórico de viagens para provar um achado, e despejos da tabela de viagens da produção nunca servem de material didático. Uma amostra mascarada que mostre a classe do problema basta para o trabalho do ENG-512, focado na homologação, e é o máximo que Sam anexa. Se um responsável insistir numa exportação maior, o pedido volta ao responsável pelas ROE e ao contato de privacidade, em vez de ser resolvido no canal do engajamento.

### 7.4 Confirmação de achados

Um achado de controle de acesso fica mais forte quando os logs mostram que a requisição não autorizada teve sucesso. Confirmar achados com logs significa casar os horários depois de sincronizar os relógios. No exercício sintético, o laço de 401 das 10:12 é confirmado quando os logs da API mostram o mesmo minuto e o relógio do jump host concorda com os hosts da API em até dois minutos. Sem essa concordância, o horário da mensagem de parada não tem qualidade de evidência. O exemplo resolvido abaixo usa a mesma ideia com um ID de requisição, que liga a linha de log a uma requisição de teste específica.

### 7.5 Sincronização de relógios

Anote os fusos horários e o estado do NTP ao correlacionar logs com as notas de atividade. A sincronização de relógios entre o jump host de Sam e os hosts da API é verificada na abertura, com uma checagem de NTP contra o VIP da API. Uma diferença maior que dois minutos é corrigida antes de se confiar nos horários das evidências, nos hashes e nas comparações de logs. Sam escreve a diferença medida no registro de atividades, para que um revisor veja que a verificação foi feita e qual era o tamanho da diferença. Um fuso horário escrito ao lado de cada horário evita uma segunda classe de erros quando se comparam logs de sistemas diferentes.

### 7.6 Retorno para a detecção

Compartilhe os nomes das técnicas com o SOC para que ele possa construir detecções depois do teste. O retorno de detecção do ENG-512 lista quais cartões de método rodaram e a que horas pararam. O silêncio depois do início do ENG-512 é uma falha de coordenação, e não um objetivo de furtividade; o SOC nunca deve descobrir que o ENG-512 terminou apenas pelo silêncio. A nota de retorno também diz quais verificações o SOC viu e quais deixou passar, para que as lacunas virem trabalho de detecção, e não surpresas na próxima janela. Ela é enviada no mesmo dia em que a janela se fecha.

### 7.7 Amostra, e não exportação completa

Quando uma consulta de logs devolve milhares de linhas, Sam exporta uma amostra limitada no tempo em torno de sua atividade de teste, e não o dia inteiro, a menos que as ROE peçam mais. Para um achado, ele pede cinco minutos de logs de autenticação da API em torno dele, e não o despejo de um dia. Amostras menores protegem os passageiros e ainda confirmam o problema, e também economizam tempo de revisão, já que um colega consegue ler cinco minutos de linhas de uma só vez. A consulta que produziu a amostra é salva ao lado dela, para que o mesmo recorte possa ser extraído de novo no reteste.

### 7.8 Dados pessoais nos logs

Os logs podem conter nomes, telefones, e-mails, números de cartão e posições de GPS precisas de passageiros. Se um log que Sam precisa guardar contém telefones de passageiros, ele o armazena no caminho restrito do cofre e anota a presença de dados pessoais no índice de evidências. O mascaramento de logs remove e-mails, PANs de cartão e GPS preciso antes que capturas de tela ou extratos entrem no cofre. Uma linha de log com o e-mail de um passageiro reprova na minimização mesmo que o achado seja sobre autenticação, e dados pessoais deixados numa captura de tela didática também reprovam.

### 7.9 Disciplina de campo

Sam reserva o acesso ao SIEM no mesmo chamado das ROE, com data de término. Quando o engajamento termina, ele confirma que seu acesso foi removido; um acesso de leitura esquecido é, ele próprio, um achado que ele escreveria sobre qualquer outra pessoa. Durante a janela, ele salva consultas, e não despejos brutos, para que outro técnico possa refazer a investigação sem guardar dados excessivos de passageiros. A disciplina de campo para a telemetria é amostrar, mascarar, sincronizar os relógios e avisar o SOC. A mensagem de parada do ENG-512 que Sam enviou depois do laço de 401 nomeou o horário e o sistema, para que a detecção pudesse correlacionar.

### Exemplo resolvido (NMT sintética)

Sam correlaciona uma resposta 200 da API de homologação sobre o recurso de outro usuário com o horário do seu registro de atividades; o log da aplicação mostra o mesmo ID de requisição.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX025 — Tipos de log.** Liste quatro tipos de log úteis na NMT. *Rubrica:* 3 = quatro do capítulo; 2 = três; 1 = um; 0 = nada.
- **EX026 — Senha emprestada.** Sam pode usar o login do SIEM do analista do SOC? *Rubrica:* 3 = não; pedir acesso nominal somente leitura; 2 = não; 1 = sim; 0 = nada.
- **EX027 — Despejo.** Por que não exportar o BD de viagens inteiro? *Rubrica:* 3 = privacidade/escopo/minimização; 2 = parcial; 1 = tudo bem; 0 = nada.
- **EX028 — Evidência mais forte.** Que detalhe de log fortalece um achado de controle de acesso? *Rubrica:* 3 = ID/horário/usuário da requisição não autorizada bem-sucedida; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

A telemetria é pedida do jeito certo, minimizada e usada para fortalecer achados — e não para acumular dados.

### Continue estudando — capítulo 07 de 18

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Modos de falha

### Objetivos de aprendizagem

Você vai (1) listar como os testes podem prejudicar a TI de transporte; (2) mapear condições de parada; (3) descrever a falha segura de ferramentas; (4) praticar a comunicação de uma parada.

### 8.1 Modos de dano

Os testes podem prejudicar a TI de transporte por bloqueio de contas, quedas da homologação, um acerto acidental na produção, tempestades de logs e caches envenenados. Para o ENG-512, os modos de dano incluem o bloqueio da API, a saturação da VPN e qualquer toque nos validadores de tarifa. Cada cartão de método de Sam lista que dano sua verificação poderia causar, para que as condições de parada não sejam inventadas sob estresse. Cartões sem modos de dano estão incompletos para o ENG-512 e ficam fora da lista de sábado até que o autor os acrescente. A linha de dano de um cartão também nomeia quem deve ser avisado primeiro se aquele dano ocorrer, por exemplo o responsável pela API num bloqueio.

### 8.2 Condições de parada

As condições de parada são: o responsável pede para parar; uma indisponibilidade sem explicação; alertas do sistema de tarifas em qualquer lugar; dados pessoais expostos num chamado; uma ferramenta em laço. Cada condição tem uma mensagem de parada de uma linha preparada no cartão das ROE, para que Sam a publique sem redigir sob estresse. Qualquer uma basta; Sam não termina "só mais um objetivo" antes. Alertas do sistema de tarifas em qualquer lugar, mesmo os aparentemente sem relação, interrompem o ENG-512 até que a operação libere a linha, e Sam não discute correlação no momento. Dados pessoais aparecendo num chamado são uma parada mesmo que nada esteja quebrado, porque o sistema de chamados pode ser lido por pessoas que o acordo nunca cobriu. Uma ferramenta presa num laço é uma parada por outro motivo: ela pode empurrar o tráfego além da taxa combinada antes que alguém perceba.

### 8.3 Falha segura de ferramentas

Prefira ferramentas que falham de forma fechada (param no erro) a ferramentas que tentam de novo até criar uma tempestade. Falha segura significa que um script sai e libera seus hosts quando os erros se repetem, em vez de tentar para sempre contra a homologação. O exercício do laço de 401 ensina exatamente isso: quando as verificações de autenticação entram em laço, o script de Sam fecha seus sockets e imprime um motivo de parada que nomeia a causa. Uma ferramenta que continua tentando até criar uma tempestade é tratada como defeituosa, por mais completa que pareça, porque o tráfego extra consome o orçamento de ruído e esconde o erro original das pessoas que precisam ler os logs.

### 8.4 Comunicação da parada

Diga o que você estava fazendo, o que observou, o que interrompeu e peça orientação — de forma curta e factual. A mensagem de parada vai para o canal do engajamento num formato fixo: `ENG-512 stop`, causa, `halted HH:MM`, `need guidance`. No exercício, ela diz `ENG-512 stop — looping auth checks on staging API — halted 10:12 — need guidance`. Palavras de atenuação e pedidos de desculpa são apagados antes do envio, porque quem está de plantão precisa agir a partir da primeira linha. Um cabeçalho factual permite ver o que parou, quando parou e que decisão está agora esperando por essa pessoa.

### 8.5 Ensaio

Uma vez por trimestre, Sam ensaia uma mensagem de parada no canal do engajamento com o SOC, e a mensagem de parada também é ensaiada no Laboratório II antes de uma janela real. Sam pratica a publicação do padrão das 10:12 para que a primeira parada real não seja a primeira vez que ele escreve uma, e o Laboratório II avalia a publicação de parada do ensaio antes de qualquer janela real. Uma primeira parada sem ensaio é uma falha do programa esperando para acontecer. O SOC também ensaia a sua parte: confirmar o recebimento da publicação e nomear quem decide.

### 8.6 Sem culpa no momento

Pare primeiro; investigue a causa depois que os sistemas estiverem estáveis. A culpa não tem lugar no momento da parada. Durante o ENG-512, o canal ao vivo traz apenas os fatos da interrupção e o pedido de orientação, e qualquer linguagem de culpa que apareça na conversa da parada é moderada. A discussão sobre por que as verificações de autenticação entraram em laço espera pela revisão pós-ação, que é dona do aprendizado. Separar as duas coisas mantém a equipe de resposta concentrada em estabilizar a homologação e dá à revisão posterior uma linha do tempo limpa, em vez de uma discussão registrada no meio do incidente.

### 8.7 Contato secundário

Se o contato de emergência principal não atender em cinco minutos, Sam liga para o secundário nomeado nas ROE; esperar em silêncio não é um plano. A marca de cinco minutos é contada a partir da primeira ligação não atendida, e os horários das duas ligações vão para o registro de atividades. As ROE de Sam listam os dois contatos, e ligar apenas para o principal não é um caminho de parada completo. Ele disca os dois números a partir do cartão das ROE, e não de memória. Se nenhum dos dois atender, a interrupção continua e Sam segue ligando; a janela não é retomada por padrão.

### 8.8 Interruptor de emergência das ferramentas

Todo script de longa duração que Sam inicia tem uma forma conhecida de ser encerrado, como um grupo de processos ou a parada de um contêiner, e ele testa esse interruptor uma vez antes da janela. No ENG-512, o interruptor é a flag de desativação do script mais o comando de encerramento no jump host praticado no ensaio, de modo que Sam pode parar as próprias tarefas sem esperar a linha de suporte de um fornecedor. O ensaio do interruptor é um item da lista do Laboratório II, e uma flag de desativação não testada mantém a automação fora da lista de sábado.

### 8.9 Disciplina de campo

Depois de qualquer parada real, Sam registra uma nota curta e sem culpa: gatilho, tempo até a interrupção, quem foi chamado, se os passageiros foram afetados e uma mudança de processo. A NMT revisa as notas de parada a cada trimestre. Equipes que escondem paradas acabam causando indisponibilidades maiores; equipes que as registram ganham interruptores melhores e ROE mais claras. O exercício do laço de autenticação existe para que a primeira parada não seja também a primeira vez que Sam escreve essa nota. A disciplina de campo para modos de falha é ter condições de parada escritas, mensagens ensaiadas, um contato secundário e um interruptor de emergência, cada um verificado antes de a janela de sábado se abrir, para que o ENG-512 não dependa de heroísmo nem de improviso quando um laço começar.

### Exemplo resolvido (NMT sintética)

Durante um exercício sintético, o script de Sam entra em laço com respostas 401. Ele para o script, publica `ENG-512 stop — looping auth checks on staging API — halted 10:12 — need guidance` e espera.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX029 — Lista de danos.** Nomeie três modos de dano dos testes. *Rubrica:* 3 = três do capítulo; 2 = dois; 1 = um; 0 = nada.
- **EX030 — Alerta de tarifa.** Um alerta de tarifa aparece durante um teste web. O que Sam faz? *Rubrica:* 3 = parar; acionar o contato de emergência; não tocar na tarifa; 2 = parar; 1 = continuar na web; 0 = nada.
- **EX031 — Mensagem de parada.** Quais quatro fatos entram numa mensagem de parada? *Rubrica:* 3 = ação, observação, interrupção, pedido; 2 = três; 1 = um; 0 = nada.
- **EX032 — Falhar de forma fechada.** O que significa falhar de forma fechada para uma ferramenta de teste? *Rubrica:* 3 = para no erro em vez de tentar de novo de forma agressiva; 2 = parcial; 1 = continua; 0 = nada.

### Síntese

Paradas são ensaiadas, rápidas e factuais; as ferramentas devem falhar de forma fechada.

### Continue estudando — capítulo 08 de 18

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX032 (as de EX033–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). A Northline Municipal Transit, Sam Park e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Site público, API do planejador de viagens, intranet dos funcionários, Active Directory, VPN (a cobrança de tarifas é o sexto, fora do escopo).

**EX002.** O caminho da internet, passando pelo WAF, até a camada web (ou da VPN até o jump host).

**EX003.** Perturbar o equipamento de tarifa pode impedir que os passageiros entrem nas estações; ele exige uma autorização especializada, se for testado.

**EX004.** As camadas de web e de API voltadas para a internet e o acesso remoto dos funcionários.

**EX005.** 3389/rdp e 8080/http-alt.

**EX006.** O RDP não está na lista aprovada e expõe um serviço de área de trabalho remota numa VLAN destinada ao tráfego web.

**EX007.** Não. A varredura em produção exige autorização por escrito; o laboratório usa uma lista sintética.

**EX008.** Ele anota que o inventário deve dizer ssh-jump de forma consistente, enquanto continua usando o processo do jump host.

**EX009.** Contas locais do sistema operacional, contas de domínio do AD e usuários de aplicação.

**EX010.** Apenas as permissões de homologação exigidas pelas verificações autorizadas, nada na produção nem nos sistemas de tarifa.

**EX011.** Ela elimina a responsabilização, costuma ter privilégios em excesso e muitas vezes continua ativa depois do teste.

**EX012.** No cofre de senhas aprovado, nunca no chat nem em repositórios de código.

**EX013.** Documentos vindos dos alvos podem carregar macros ou exploits; trate-os como dados não confiáveis e, se for abri-los, use apenas um visualizador seguro.

**EX014.** Versão do interpretador, arquivos de entrada e quaisquer sementes ou flags de configuração.

**EX015.** Do cofre ou de uma variável de ambiente injetada no jump host — nunca fixa no código do script.

**EX016.** Para pegar erros que poderiam tocar sistemas fora do escopo ou vazar segredos, e para que outra pessoa possa executá-lo se Sam estiver ausente.

**EX017.** Ele o deixa fora do achado, captura a tela de novo e guarda um novo hash.

**EX018.** Os bytes do arquivo conferem com o resumo registrado — integridade desde o cálculo do hash —, e não que o sistema em operação continua configurado daquele jeito.

**EX019.** Desfocar rostos de passageiros ou números de crachá de funcionários numa captura de tela, deixando legível o texto da configuração incorreta.

**EX020.** Host dentro do escopo, método permitido e janela de tempo (o contato de emergência é o quarto).

**EX021.** Passageiro e funcionário.

**EX022.** API do planejador de viagens — controle de acesso, para que os passageiros não leiam as viagens salvas de outras pessoas.

**EX023.** Comparar a configuração de autenticação com a documentação dos responsáveis pela produção ou com uma revisão de configuração permitida — sem supor.

**EX024.** Eles estão fora do escopo deste engajamento, então modelá-los convidaria a testes acidentais.

**EX025.** Acesso web, falhas de autenticação da API, autenticações na VPN, bloqueios do WAF (também logins no AD).

**EX026.** Não. Ele precisa de acesso nominal somente leitura sob as ROE.

**EX027.** Isso expõe dados pessoais de passageiros além do que o achado exige e provavelmente viola as ROE.

**EX028.** Uma linha de log mostrando que sua conta de teste recebeu HTTP 200 para o recurso de outro usuário num horário registrado.

**EX029.** Bloqueios de conta, quedas da homologação, acertos acidentais na produção (também tempestades de logs e envenenamento de cache).

**EX030.** Parar os testes, acionar o contato de emergência e deixar os sistemas de tarifa intocados.

**EX031.** O que ele estava fazendo, o que viu, que interrompeu e um pedido de orientação.

**EX032.** No erro, ela para, em vez de tentar de novo de formas que poderiam bloquear contas ou inundar os logs.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v3.1 Specification Document. <https://www.first.org/cvss/v3.1/specification-document>
- MITRE ATT&CK, including T1078 Valid Accounts. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
