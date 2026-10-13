# Segurança Ofensiva Autorizada e Red Team: Um Caderno de Trabalho para o Operador Técnico

- Idioma: português do Brasil (`pt`); curso técnico, dezoito meses; aproximadamente 1.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 18 já estão escritos em português, com os exercícios EX001–EX016 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 5–18 (EX017–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX016 (as de EX017–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). A Northline Municipal Transit, Sam Park e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
