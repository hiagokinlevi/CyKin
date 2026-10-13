# Segurança Ofensiva Autorizada e Red Team: Um Caderno de Trabalho para o Operador Técnico

- Idioma: português do Brasil (`pt`); curso técnico, dezoito meses; aproximadamente 1.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–18 de 18 têm texto didático escrito à mão; os exercícios EX001–EX072 têm resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, e suas saídas foram incorporadas a partir de execuções reais. A revisão independente e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

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

<a id="ch-09"></a>

## Capítulo 9 — Ferramentas e métodos

### Objetivos de aprendizagem

Você vai (1) escolher métodos a partir dos temas do WSTG; (2) configurar ferramentas com limites de taxa; (3) interpretar resultados com o modelo de sistema; (4) manter um cartão de método por verificação.

### 9.1 Cartões de método

Cada cartão traz: propósito, referência às ROE, ferramenta/configurações, condições de parada e evidência esperada. Além desses campos, todo cartão precisa nomear a verificação, o limite de taxa, o modo de dano e a evidência esperada. Essas quatro entradas são o mínimo para o ENG-512: um cartão a que falte qualquer uma delas é rejeitado na revisão por pares e fica fora da pilha de sábado de Sam. A regra mantém verificações improvisadas fora do engajamento, porque um técnico não pode executar um método cuja taxa e cujo dano nunca foram escritos e combinados.

### 9.2 Limites de taxa

As ferramentas de varredura recebem limites de taxa explícitos, abaixo do que a homologação aguenta. Mais rápido não é melhor. Nas verificações de login da homologação, isso significa um teto rígido de tentativas por minuto, definido para que o padrão do laço de 401 não se repita e o orçamento de ruído fique intacto. Quando o teto é atingido, a tarefa falha de forma fechada e termina; ela não desacelera em silêncio para continuar tentando. Os cartões de autenticação do planejador de viagens seguem a mesma regra, de modo que um colega que leia qualquer cartão de autenticação vê a taxa combinada e sabe exatamente o que acontece quando ela é atingida.

### 9.3 Seleção do WSTG

Sam escolhe autenticação, sessão, controle de acesso e tratamento de entradas para a API do planejador de viagens, e não todos os itens do WSTG numa mesma janela. A seleção do WSTG para a homologação da NMT se concentra nas verificações de sessão, autenticação e entradas que correspondem ao risco voltado aos passageiros, com sessão e autenticação no planejador de viagens em primeiro lugar. Cartões que precisam de backends de tarifa não são selecionados para o ENG-512 comum e ficam fora da lista de seleção. Uma seleção estreita bem feita também dá ao relatório uma declaração de cobertura honesta: os temas deixados de fora são nomeados como não testados nesta janela, em vez de sugeridos como limpos.

### 9.4 Interpretação

Associe cada alerta de ferramenta a um elemento do modelo antes de promovê-lo a achado. Um acerto de ferramenta só vira achado depois que uma pessoa traçou um caminho até o impacto. Um banner desatualizado relatado com baixa confiança fica na fase de descoberta até que Sam mostre exposição e impacto com evidências que um colega possa reproduzir na homologação. Isso mantém o ruído de banners fora do relatório e significa que todo achado que chega ao responsável já explica qual parte do modelo de sistema é afetada e por que isso importa.

### 9.5 Fixação de versões

Registre as versões das ferramentas no cartão de método. As versões das ferramentas de varredura e dos scripts são fixadas no caderno, ao lado do ENG-512, antes de a janela abrir. Sem a fixação, um reteste pode virar uma discussão sobre a configuração: o responsável diz FIXED, o testador vê STILL OPEN, e ninguém consegue dizer se a ferramenta mudou no meio do caminho. Com as versões anotadas, a segunda execução usa as mesmas ferramentas da primeira, então qualquer diferença no resultado aponta para a correção, e não para o ferramental.

### 9.6 Métodos proibidos

Password spraying e negação de serviço continuam proibidos na NMT. A lista de proibições também cobre sondagens na rede de tarifas e qualquer coisa que não esteja num cartão de método aprovado. A biblioteca de cartões de Sam imprime essa lista na capa, e a capa é lida em voz alta na abertura, para que todos os colegas ouçam os mesmos limites antes de a primeira verificação rodar. Um método que não está na biblioteca não é uma zona cinzenta a ser discutida durante a janela; ele está fora do escopo até que um novo cartão seja revisado e combinado.

### 9.7 Biblioteca de cartões

Os cartões de método ficam numa biblioteca da equipe, com responsáveis. Copiar um cartão sem ler as condições de parada é um erro comum de iniciante que Sam vigia. A biblioteca fica no repositório de runbooks, com um responsável e uma data de revisão em cada cartão. Um cartão sem revisão há doze meses é aposentado no arquivo antes de poder entrar no ENG-512, e Sam não executa cartões vencidos nos hosts do ENG-512. Um cartão aposentado só volta depois que seu responsável confere de novo a versão da ferramenta, a taxa e as condições de parada contra as ROE vigentes.

### 9.8 Orçamento de ruído

Se um método geraria mais alertas do que o SOC combinou atender, Sam reduz a taxa ou remarca; os parceiros de detecção não são saco de pancadas. O orçamento de ruído combinado com o SOC limita quantas falhas de autenticação o ENG-512 pode gerar, e é escrito como um número na folha de abertura. Ultrapassá-lo é uma condição de parada, tratada como disciplina e não como fraqueza, e não uma medalha de minúcia. Quando o orçamento é apertado, Sam distribui os cartões de autenticação por duas janelas, em vez de comprimi-los numa só.

### 9.9 Disciplina de campo

Cartões de método são inúteis se discordam das ROE. O passo de revisão de Sam é destacar a cláusula das ROE em que cada cartão se apoia; se não consegue destacar uma cláusula, o cartão é reescrito ou descartado. Esse hábito também educa os iniciantes: eles veem que "sempre rodamos a ferramenta X" não é um motivo, ao passo que "a cláusula 4.2 das ROE permite GET/POST autenticado na API de homologação a ≤1 rps" é um motivo. A disciplina de campo para métodos é cartões, taxas, versões fixadas, a lista de proibições e o orçamento de ruído, e Sam não acrescenta uma verificação engenhosa no meio da janela sem um cartão escrito e um aviso ao SOC.

### Exemplo resolvido (NMT sintética)

O cartão de Sam para IDOR nas viagens salvas: WSTG-AUTHZ, curl com dois usuários de teste, taxa de 1 req/s, parar se a taxa de HTTP 5xx passar de 1%, evidência = IDs de requisição + respostas mascaradas.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX033 — Campos do cartão.** Liste cinco campos de um cartão de método. *Rubrica:* 3 = cinco do capítulo; 2 = três; 1 = um; 0 = nada.
- **EX034 — Motivo do limite de taxa.** Por que definir limites de taxa na homologação? *Rubrica:* 3 = evitar queda/bloqueio/tempestade de logs; 2 = parcial; 1 = ir mais rápido; 0 = nada.
- **EX035 — Seletividade.** Por que não executar todas as verificações do WSTG numa só janela? *Rubrica:* 3 = tempo/qualidade; foco nos temas de alto risco; 2 = parcial; 1 = sempre todas; 0 = nada.
- **EX036 — Proibidos.** Nomeie dois métodos proibidos na NMT. *Rubrica:* 3 = password spraying e negação de serviço; 2 = um; 1 = vago; 0 = nada.

### Síntese

Cartões de método amarram propósito, ROE, limites de taxa e evidências — e mantêm os métodos proibidos de fora.

### Continue estudando — capítulo 09 de 18

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Configuração de controles

### Objetivos de aprendizagem

Você vai (1) ler baselines comuns de configuração segura; (2) distinguir um achado de configuração de um achado de código; (3) propor mudanças de configuração seguras; (4) verificar com o responsável.

### 10.1 Achados de configuração

Configurações de TLS, flags de cookie, cabeçalhos de segurança, conjuntos de cifras da VPN e a política de senhas do AD são configuração e muitas vezes se corrigem sem lançamento de código. Achados de configuração, como uma flag de cookie ausente ou um serviço aberto na 8080, nomeiam o arquivo ou o serviço, a baseline esperada e o responsável. Os chamados de configuração citam a linha da baseline e o desvio observado, por exemplo a falta da flag Secure num cookie de sessão, com o responsável pelo planejador de viagens nomeado. Linhas vagas como "endurecer os servidores" são reescritas antes de os chamados serem abertos, porque ninguém consegue verificar a correção de uma frase que não nomeia nenhuma configuração.

### 10.2 Achados de código

Falhas de lógica na autorização exigem mudanças dos desenvolvedores e testes de regressão. Quando as ROE permitem acesso de leitura ao código ou à configuração dos aplicativos da NMT, Sam cita no achado o arquivo e a linha ou a chave, para que o desenvolvedor vá direto ao ponto que precisa mudar. Os binários do fornecedor de tarifas são outra história: descompilá-los continua proibido no ENG-512, seja o que for que uma ferramenta sugira. Os achados nessa área são descritos a partir do comportamento observado na homologação e encaminhados ao responsável pelas tarifas, em vez de serem sustentados por engenharia reversa.

### 10.3 Propostas seguras

Uma proposta segura nomeia a configuração, o sistema, o risco caso esteja errada e uma reversão. Nunca aplique você mesmo uma configuração na produção, a menos que as ROE e o processo de mudanças digam isso. As propostas de Sam preferem mudanças de configuração na homologação, com reversão, e cada uma inclui um caminho de correção na homologação e uma nota de reversão. Ele nunca propõe um ajuste só para a produção que não possa ser testado antes na zona âmbar; ideias só para a produção esperam por janelas de mudança que não pertencem a Sam. Escrever a linha de risco caso esteja errada o obriga a pensar em quais passageiros ou funcionários perceberiam primeiro uma mudança ruim.

### 10.4 Verificação pelo responsável

Os responsáveis aplicam as mudanças pelo próprio pipeline; Sam verifica. A verificação começa pelo responsável. O responsável pelo planejador de viagens precisa confirmar a correção na conversa do chamado e marcar a caixa do responsável antes que Sam reteste qualquer coisa. Sam deixa essa caixa em branco até que o líder tenha escrito a confirmação, e uma correção sem nome de responsável continua aberta. Correções sem dono, portanto, não podem chegar a FIXED na linguagem do lab_retest, o que impede que uma mudança pela qual ninguém responde seja relatada como encerrada. O histórico do chamado mostra então quem confirmou a mudança e quando.

### 10.5 Baselines

A baseline de endurecimento da NMT é a lista de verificação; desvios exigem chamados. As baselines de versões de TLS e de flags de cookie ficam na tag do runbook que as ROE nomeiam. Sam escreve os achados como desvio dessa baseline, citando o valor esperado e o valor observado, e qualquer redação do tipo "parece ruim" é reescrita antes de o relatório sair. A linguagem de desvio dá ao responsável um alvo concreto a restaurar e dá ao reteste uma condição clara de aprovação, coisa que uma opinião sobre a aparência não oferece. A mesma tag é usada de novo no reteste, para que as duas execuções meçam contra uma única baseline.

### 10.6 Desvio

O desvio de configuração depois de mudanças emergenciais é uma fonte recorrente de achados. Depois de uma mudança na CDN, Sam compara a homologação com o modelo datado. Se as flags de cookie regrediram, um chamado é aberto no meio da semana, mesmo sem nova janela de ENG agendada, porque esperar o próximo horário de sábado deixaria uma regressão conhecida sem nome por dias. O chamado cita a baseline e os valores observados, para que o responsável veja exatamente qual mudança introduziu o desvio e onde ele precisa ser revertido.

### 10.7 Reversão testada

Uma proposta de configuração sem uma reversão testada está incompleta. Sam pergunta ao responsável como ele desfaria a mudança em quinze minutos. Sam não aceita que uma mudança de configuração arriscada seja a correção até que sua reversão tenha sido treinada na homologação e o treino esteja anexado ao chamado como evidência. Uma reversão não testada é registrada como nota de risco e mantém o chamado aberto. Ninguém declara prontidão para a produção antes de esse treino existir, porque uma correção que não pode ser desfeita depressa pode transformar um achado menor numa indisponibilidade durante a janela de mudança.

### 10.8 Homologação primeiro

No trabalho de configuração do ENG-512, a homologação primeiro é absoluta. Achados de configuração da produção são reproduzidos na homologação, quando possível, antes de se insistir numa mudança na produção. Sam conclui a verificação na zona âmbar antes de qualquer mudança na produção ser discutida, e as mudanças na produção esperam então pelas janelas de mudança dos responsáveis, que Sam não controla. Até essas janelas acontecerem, os retestes continuam âmbar, e Sam não escreve "pronto para produção" no relatório nem no chamado. O status só muda quando os retestes âmbar passam e o responsável aplicou a mudança na produção.

### 10.9 Disciplina de campo

Sam mantém uma biblioteca pessoal de boas propostas de configuração (HSTS, flags de cookie, cifras da VPN) escritas no estilo dos chamados de mudança da NMT. Reaproveitar a estrutura acelera o trabalho, mas ele ainda preenche o risco e a reversão específicos do sistema a cada vez. Copiar e colar sem mudanças uma proposta feita para a homologação num chamado de produção é o caminho pelo qual se propõem cifras erradas, então ele trata cada proposta como um texto novo. A disciplina de campo para configuração é baseline, responsável, homologação primeiro e reversão testada; uma reversão que nunca rodou na homologação conta como não testada, por mais simples que pareça no papel, e a revisão por pares rejeita chamados a que falte qualquer um dos quatro.

### 10.10 Nota de encerramento

Sam também pergunta se uma mudança de configuração precisa de uma janela de manutenção. Mudanças de cabeçalho no proxy reverso podem ser instantâneas; mudanças de cifras da VPN podem derrubar sessões dos funcionários e exigir um comunicado. O momento faz parte de uma proposta completa. O trabalho de configuração na NMT protege os passageiros ficando longe do equipamento de tarifa e nomeando responsáveis. O sucesso do ENG-512 são baselines verificadas na web e na API, e não uma longa lista de ruído de ferramentas não verificado, e encerrar o trabalho de configuração nunca inclui uma promessa sobre o equipamento de tarifa em que Sam não tocou.

### Exemplo resolvido (NMT sintética)

Sam descobre que a API de homologação não envia o Strict-Transport-Security. Ele registra um achado de configuração com o cabeçalho recomendado e pede à equipe de segurança de aplicações que o aplique pela configuração do proxy reverso.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX037 — Configuração versus código.** Classifique: cabeçalho HSTS ausente; o passageiro A consegue ler as viagens do passageiro B. *Rubrica:* 3 = configuração; código/lógica; 2 = invertidos; 1 = ambos configuração; 0 = nada.
- **EX038 — Conteúdo da proposta.** Quais quatro coisas entram numa proposta de configuração segura? *Rubrica:* 3 = configuração, sistema, risco caso esteja errada, reversão; 2 = três; 1 = uma; 0 = nada.
- **EX039 — Quem aplica.** Quem aplica as mudanças de configuração na produção? *Rubrica:* 3 = o responsável, pelo processo de mudanças; não o testador sozinho; 2 = parcial; 1 = o testador, livremente; 0 = nada.
- **EX040 — Desvio.** Por que mudanças emergenciais geram achados depois? *Rubrica:* 3 = baselines contornadas; não revertidas; 2 = parcial; 1 = sem motivo; 0 = nada.

### Síntese

Achados de configuração precisam de propostas claras e de mudanças aplicadas pelo responsável; os testadores verificam.

### Continue estudando — capítulo 10 de 18

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Verificação

### Objetivos de aprendizagem

Você vai (1) planejar uma janela de reteste; (2) comparar status de antes e depois; (3) lidar com correções parciais; (4) encerrar somente com evidências.

### 11.1 Plano de reteste

Liste os achados, os métodos, as notas de entrada em produção dos responsáveis e a janela. O plano de reteste do ENG-512 usa os mesmos cartões de método e as mesmas versões fixadas das ferramentas. O status no estilo do lab_retest mostra `F1 open->closed FIXED`, `F2 open->open STILL OPEN`, `F3 open->closed FIXED` — `fixed: 2 open: 1`. Usar os mesmos cartões e as mesmas versões é o que dá sentido a essa divisão: se o F2 continua aberto, a causa é a correção, e não uma mudança no modo como Sam olhou. O caderno coloca o resumo de dois corrigidos e um aberto ao lado dos resumos criptográficos das ferramentas fixadas, para que um examinador veja que o reteste e o teste original usaram entradas idênticas.

### 11.2 Antes e depois

Registre as transições de status de forma explícita.

```python
"""Lab 11: compare synthetic before/after findings for a retest window."""
before = {"F1": "open", "F2": "open", "F3": "open"}
after = {"F1": "closed", "F2": "open", "F3": "closed"}
for fid in sorted(before):
    b, a = before[fid], after[fid]
    print(f"{fid} {b}->{a} {'FIXED' if b == 'open' and a == 'closed' else 'STILL OPEN' if a == 'open' else 'CHECK'}")
print("fixed:", sum(1 for f in before if before[f] == "open" and after[f] == "closed"),
      "open:", sum(1 for f in after if after[f] == "open"))
```

Execute com `python3 lab_retest.py`. Saída verificada:

```text
F1 open->closed FIXED
F2 open->open STILL OPEN
F3 open->closed FIXED
fixed: 2 open: 1
```

Os hashes das evidências de antes e de depois ficam no chamado e provam que o artefato mudou com a correção. FIXED sem um hash com MATCH no artefato de depois não é encerramento na NMT.

Cada transição é escrita com sua data e com a evidência que a justificou, por exemplo o F1 passando de open para closed FIXED com um artefato de depois cujo resumo confere com a cópia guardada no cofre. Um status que muda sem motivo registrado não pode ser auditado depois, e os examinadores da NMT amostram exatamente essas linhas quando revisam chamados encerrados.

### 11.3 Correções parciais

O F2 ainda aberto significa que o chamado continua aberto, com novas evidências. Correções parciais que deixam o F2 em STILL OPEN continuam no controle, com responsável e prazo, e Sam não encerra o engajamento como limpo enquanto houver itens abertos. A revisão do supervisor confere se o slide de resumo mostra o F2 como STILL OPEN, com seu responsável e seu prazo, em vez de escondê-lo sob uma manchete de tudo limpo. Expressões como "parcialmente corrigido" não são usadas; o chamado atende à verificação do seu cartão de método ou não atende, e as novas evidências explicam que parte da correção está faltando.

### 11.4 Encerramento

Encerrado significa FIXED com evidências, ou risco aceito com a assinatura do CISO — e não silêncio. O encerramento exige o aceite do responsável e o status verificado FIXED com evidências. Um "pronto" verbal no chat é rejeitado na revisão semanal. A aceitação de risco é a única outra via, e ela exige a assinatura do CISO no chamado, e não um acordo numa reunião. A revisão semanal reabre qualquer item que tenha sido encerrado por entusiasmo, sem evidência guardada no cofre. O par que a revisão aceita é um hash armazenado do artefato de depois mais o aceite do responsável.

### 11.5 Congelamento do escopo

Nada de nova caçada durante o reteste, a menos que autorizada. Durante o reteste, o escopo fica congelado: nenhum host novo é acrescentado ao ENG-512, mesmo quando uma ferramenta sugere outro serviço em escuta. Os status do reteste cobrem, portanto, apenas os serviços da lista original. O texto do congelamento é lido em voz alta na abertura do reteste, e qualquer host novo sugerido é escrito numa lista de estacionamento como candidato para as próximas ROE, onde os responsáveis podem decidir se o autorizam. Retestar um host novo sem essa decisão produziria um resultado que ninguém combinou receber.

### 11.6 Comunicação

Envie um relatório de reteste curto aos responsáveis no mesmo dia. Os resultados do reteste são comunicados ao SOC e aos responsáveis no mesmo dia, e o STILL OPEN do F2 não fica enterrado até o pacote mensal. Sam envia uma única mensagem ao líder do SOC e ao responsável pelo achado juntos, para que os dois saibam do F2 no mesmo momento e nenhum deles fique sabendo de segunda mão. Os horários das mensagens são guardados ao lado do chamado para os pacotes de exame. Esperar pelo pacote mensal deixaria o responsável um mês atrasado sobre uma fraqueza que continua aberta.

### 11.7 Mesmo método

O reteste usa o mesmo cartão de método, e não um mais forte. Trocar de método no meio do reteste confunde a questão de saber se a correção funcionou. Mesmo método no reteste significa que, se o F1 foi uma verificação de flag de cookie, o reteste usa aquele cartão, e não um perfil diferente de varredura que invente uma aprovação nova. Se a verificação original usou o cartão de cookie, um perfil diferente de varredura poderia simplesmente não testar a mesma flag e relatar uma aprovação que não significa nada. Um colega rubrica o chamado para confirmar que o cartão de método do reteste é o mesmo usado no achado. Mudar o método é um teste novo, e ele precisa de cartão e linha de ROE próprios.

### 11.8 Demonstração ao responsável

Quando ajuda, Sam convida o responsável a assistir uma vez ao reteste bem-sucedido — ver o FIXED gera mais confiança do que um comentário no chamado. A demonstração ao responsável na homologação mostra o estado FIXED antes que Sam marque o encerramento. Capturas de tela sozinhas, sem a presença do responsável, são fracas para os pacotes de exame. O responsável vê o estado FIXED na homologação com os próprios olhos, o que torna muito menos prováveis disputas posteriores sobre a correção ter sido real. O convite de calendário da demonstração é arquivado como evidência de quem a testemunhou. As capturas de tela continuam indo para o cofre, mas apoiam a demonstração em vez de substituí-la.

### 11.9 Disciplina de campo

O dia do reteste é emocionalmente mais difícil que o dia da descoberta, porque os responsáveis torcem pelo verde. Sam abre a chamada lembrando que STILL OPEN é um resultado de reteste bem-sucedido quando é verdadeiro. Ele mostra lado a lado as evidências de antes e de depois. Quando o F2 continua aberto, ele ajuda o responsável a agendar a próxima correção em vez de discutir de novo a severidade — a severidade já foi aceita quando o achado foi registrado. A disciplina de campo para a verificação é mesmo método, antes e depois com hash, demonstração ao responsável e contagens honestas de STILL OPEN. Dois corrigidos e um aberto é o resultado didático do ENG-512.

### 11.10 Nota de encerramento

Se todos os achados ficam FIXED no primeiro reteste, Sam ainda registra os métodos e os hashes. Vitórias fáceis merecem a mesma trilha de evidências que as teimosas, especialmente quando os examinadores amostram chamados encerrados. A nota de encerramento do ENG-512 diz o mesmo: a verificação é o modo pelo qual a NMT passa a confiar no programa. A reputação de Sam se apoia em relatar contagens honestas de itens abertos, incluindo o F2, em vez de produzir um slide com zero abertos. Um programa que empurra os testadores para histórias forçadas de zero abertos tem um defeito próprio, e espera-se que os supervisores o nomeiem.

### Exemplo resolvido (NMT sintética)

O reteste de Sam: F1 e F3 FIXED, F2 STILL OPEN. Ele encerra o T-F1 e o T-F3 com evidências, deixa o T-F2 aberto e avisa o responsável.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX041 — Contagens do laboratório.** Quantos foram corrigidos e quantos continuam abertos? *Rubrica:* 3 = fixed 2 open 1; 2 = parcial; 1 = errado; 0 = nada.
- **EX042 — Ação sobre o F2.** O que acontece com o chamado do F2? *Rubrica:* 3 = continua aberto, com novas evidências; 2 = aberto; 1 = encerrar mesmo assim; 0 = nada.
- **EX043 — Risco aceito.** Quem precisa assinar se a NMT aceitar o F2 sem correção? *Rubrica:* 3 = o CISO (dono do risco); 2 = parcial; 1 = Sam; 0 = nada.
- **EX044 — Nada de nova caçada.** Por que congelar o escopo durante o reteste? *Rubrica:* 3 = o reteste mede as correções; nova caçada exige nova autorização; 2 = parcial; 1 = caçar sempre; 0 = nada.

### Síntese

Verificação é evidência de antes e depois, chamados abertos honestos e comunicação no mesmo dia.

### Continue estudando — capítulo 11 de 18

[← Capítulo 10 (rascunho)](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 (rascunho) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Laboratório controlado I

### Objetivos de aprendizagem

Você vai (1) executar os laboratórios 2, 5 e 11 sob supervisão; (2) montar um caderno de laboratório; (3) conferir as classificações de portas de um colega; (4) parar diante de uma falha plantada.

### 12.1 Caderno

Cole as saídas do lab_ports, do lab_hash e do lab_retest com horários e suas iniciais. O caderno do Laboratório I guarda o inventário, os cartões de método usados, os hashes e todas as mensagens de parada. Ele é mantido à caneta ou num arquivo digital só de acréscimo, para que um minuto de pausa continue visível quando a disciplina de parada for avaliada mais tarde. Apagar uma entrada constrangedora reprova na revisão de integridade, porque um pacote de evidências real perderia justamente o registro que um examinador mais quer ver. As correções entram como novas linhas datadas que apontam para a entrada que corrigem.

### 12.2 Conferência por pares

Troquem as listas de portas; pontuem a concordância com o mapa aprovado. A conferência por pares pontua a completude do caderno antes do aceite. A falta do contato de emergência ou da exclusão da tarifa reprova na etapa dos pares. Esses dois campos são conferidos primeiro porque qualquer uma das lacunas teria interrompido uma janela real do ENG-512 na abertura. Completude vale mais que letra bonita. Em seguida, os colegas comparam linha a linha a lista de portas de cada caderno com o mapa aprovado, e todo serviço ausente ou não aprovado é marcado na folha de pontuação. Um caderno que lista uma porta que o mapa nunca aprovou reprova naquela linha, mesmo que a porta tenha de fato respondido na homologação.

### 12.3 Falha plantada

O supervisor planta um arquivo com MISMATCH; o aluno precisa se recusar a anexá-lo. O supervisor também acrescenta um serviço 3389/rdp ao inventário do laboratório sem avisar Sam, de modo que só a saída do lab_ports o revela como NOT APPROVED. O relatório de Sam precisa listar o serviço plantado, senão o laboratório reprova, e também precisa dizer o que Sam faria em seguida: parar, avisar o responsável e registrar o serviço. O arquivo plantado com MISMATCH testa o hábito de evidência do mesmo modo: anexá-lo significaria que um achado se apoia num artefato cujo resumo não confere mais.

### 12.4 Tempo limitado

Noventa minutos, com parada rígida. Os noventa minutos correspondem à duração de uma janela curta do ENG-512 num sábado. Quando o relógio para, Sam guarda os artefatos no cofre e tira as mãos do teclado, e o supervisor pontua esse momento. Digitar depois do sinal conta como hora extra silenciosa, uma falha de disciplina de janela, porque num engajamento real o trabalho depois do fim combinado ficaria fora da autorização. Aprender a parar no meio de uma tarefa, com uma nota do que ficou por fazer, é mais difícil do que aprender a trabalhar depressa, e por isso o sinal é pontuado separadamente dos achados.

### 12.5 Nada de produção

Qualquer tentativa de varrer a produção da NMT reprova no laboratório. O Laboratório I usa apenas inventários sintéticos, e exportações de passageiros valem zero absoluto, mesmo como ilustração ou captura de tela. Manter os dados de produção fora do pacote de aula significa que nenhum dado pessoal de passageiro pode vazar do notebook de um aluno ou de um fórum compartilhado. A regra também mantém o exercício honesto sobre o que ele pode ensinar: hábitos de decisão, e não fatos sobre o ambiente real da NMT. O aluno que precisa de um registro com aparência realista o constrói a partir do inventário sintético.

### 12.6 Aceite

O supervisor assina o caderno se a conferência por pares e a falha plantada foram tratadas corretamente. Sem essa assinatura, o laboratório continua sendo prática e não entra na pasta de portfólio avaliado de Sam. A conferência por pares vem primeiro, para que o supervisor assine um trabalho que outro aluno já conferiu quanto ao contato de emergência e à exclusão da tarifa. Exigir as duas etapas espelha um engajamento real, em que as evidências são revisadas por um colega antes que alguém as aprove. O supervisor também confirma, antes de assinar, que a falha plantada foi encontrada.

### 12.7 Integridade do caderno

Alterar as saídas dos laboratórios para que pareçam melhores reprova no curso. Os supervisores podem executar os laboratórios de novo e comparar os hashes. A integridade também cobre o próprio caderno: as páginas são datadas, e a exportação final recebe um hash. Os colegas verificam esse hash e a data depois do aceite, e qualquer edição feita mais tarde reinicia o ciclo de revisão. Um supervisor que executa de novo um laboratório e encontra um resumo diferente sabe que a saída foi alterada, seja qual for o motivo alegado. O aluno então explica a mudança num novo ciclo de revisão, e não numa correção silenciosa.

### 12.8 Canal silencioso

Durante o laboratório, só mensagens de ROE e de parada vão para o canal compartilhado — nada de spoilers para os colegas que ainda estão trabalhando. As dúvidas do laboratório vão para o fórum do curso, e não para SMS pessoais. Sam nunca cola as credenciais da tst-sam-web em chat algum, porque elas pertencem apenas ao caminho do cofre. Manter as perguntas num só canal também dá ao supervisor um registro do que foi perguntado, o que ajuda a avaliar se os alunos ficaram dentro das ROE. As respostas publicadas ali também ajudam os colegas que chegarem à mesma dúvida mais tarde na sessão.

### 12.9 Disciplina de campo

O Laboratório I é avaliado pela disciplina, e não pela descoberta de problemas exóticos. Alunos que correm na frente para inventar ataques aos dados sintéticos, mas pulam os hashes, reprovam. Alunos lentos que recusam o MISMATCH plantado e classificam as portas corretamente são aprovados. Sam lembra os colegas desse critério no início, para que a competição não empurre ninguém para hábitos inseguros. As cinco etapas de disciplina de campo para entrar no portfólio são o caderno, a conferência por pares, encontrar a falha plantada, respeitar o tempo limitado e usar apenas dados sintéticos. Cada etapa é marcada como aprovada ou reprovada, sem nota parcial. Um aluno que cumpre as cinco, mas não encontra nada incomum, fez exatamente o que o laboratório pede.

### 12.10 Nota de encerramento

Os alunos entregam o caderno como um único pacote em PDF ou markdown, com sumário. A falta de iniciais ou de horários custa pontos, porque pacotes de evidências reais precisam de atribuição. O Laboratório I existe para que os hábitos do ENG-512 se formem antes que qualquer passageiro real seja afetado por um erro. Sam trata a linha plantada da 3389 com a mesma seriedade de um achado real, registrando-a com os mesmos campos e evidências. A parte de reteste do laboratório ensina a mesma honestidade, com ferramentas fixadas e cartões de método idênticos: dois corrigidos, um aberto.

### Exemplo resolvido (NMT sintética)

Sam recusa a captura de tela plantada com divergência, corrige a classificação errada da 8080 feita pelo colega e termina com três minutos de folga.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX045 — Conteúdo do caderno.** Quais três saídas de laboratório entram no caderno? *Rubrica:* 3 = portas, hash, reteste; 2 = duas; 1 = uma; 0 = nada.
- **EX046 — Resposta à falha plantada.** Qual é a resposta correta a um arquivo de evidência divergente? *Rubrica:* 3 = recusar anexá-lo; capturar de novo/recalcular o hash; 2 = recusar; 1 = anexar; 0 = nada.
- **EX047 — Condição de reprovação.** O que reprova o laboratório imediatamente? *Rubrica:* 3 = varrer a produção / a NMT real; 2 = parcial; 1 = terminar cedo; 0 = nada.
- **EX048 — Pontuação dos pares.** O que a conferência por pares pontua? *Rubrica:* 3 = concordância com o mapa de portas aprovado; 2 = parcial; 1 = velocidade; 0 = nada.

### Síntese

O Laboratório I comprova disciplina com portas, integridade das evidências e honestidade no reteste sob uma parada rígida.

### Continue estudando — capítulo 12 de 18

[← Capítulo 11 (rascunho)](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 (rascunho) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Solução de problemas

### Objetivos de aprendizagem

Você vai (1) seguir uma árvore de solução de problemas para verificações que falharam; (2) separar falhas de ferramenta de achados reais; (3) escalar com evidências; (4) documentar contornos com segurança.

### 13.1 Árvore

Sintoma → reproduzir → verificar escopo/conta/ferramenta → verificar a saúde da homologação → escalar. Na prática, a árvore começa pelo escopo, depois a saúde da ferramenta e então o ambiente. A situação de aprovação do serviço em escuta é a primeira pergunta do cartão de solução de problemas, então Sam verifica se a porta 8080 foi alguma vez aprovada antes de depurar por que o lab_ports a relatou. Pôr o escopo em primeiro lugar evita caçadas falsas à ferramenta: uma hora gasta consertando uma ferramenta de varredura que sinalizou corretamente uma porta não aprovada é uma hora tirada da janela para nada. Só depois de o escopo estar resolvido o cartão passa às verificações da ferramenta e do ambiente.

### 13.2 Falha de ferramenta

Erros de certificado no notebook do testador não são achados da API. Uma falha de ferramenta, como uma queda ou uma saída vazia, é registrada junto com a versão fixada da ferramenta. Sam então passa para o script de baseline sabidamente bom, a versão da semana anterior, cujo caminho está escrito no caderno, e não guardado na memória. Improvisar novas flags no meio de um incidente é proibido, porque uma flag não testada pode mudar o padrão de tráfego e romper os limites de taxa combinados no cartão de método.

### 13.3 Pacote de escalonamento

Sintoma, passos, capturas de tela, horário, o que você já descartou. O pacote de escalonamento do ENG-512 de Sam tem quatro campos: o identificador do chamado, o último hash bom, a mensagem de parada exata que foi publicada e os contatos do responsável. O último hash bom diz ao plantão qual arquivo de evidência estava íntegro antes do problema, para que ninguém o colete de novo às cegas. Montar o pacote leva cerca de cinco minutos e poupa ao engenheiro de plantão uma longa história verbal. Listar o que já foi descartado impede que o engenheiro repita verificações que Sam fez uma hora antes.

### 13.4 Contornos

Flags temporárias de ferramenta são registradas e removidas depois; elas não viram configuração permanente silenciosa. Contornos que mudam o escopo são proibidos de saída. Se um contorno sondaria um host que não está na lista do ENG-512, ele espera por um texto de ROE atualizado, e um pedido de atualização das ROE é a única forma legítima de um contorno acrescentar um host. Mudanças de escopo engenhosas feitas no meio de uma sessão travada não são solução de problemas; são testes não aprovados, e são registradas como tal na revisão pós-ação, em vez de desculpadas porque a ferramenta original estava falhando.

### 13.5 Depuração em dupla

Problemas difíceis ganham um segundo técnico depois de quinze minutos. A depuração em dupla põe esse segundo técnico na visão do jump host, onde ele vê a mesma saída e pode cortar um buraco de coelho que já estourou o tempo limitado. As sessões em dupla são marcadas no calendário antes de a janela abrir, para que o horário exista antes de alguém travar. Torcer para que um colega passe por acaso não é trabalhar em dupla, e geralmente significa que o engenheiro travado continua cavando sozinho até que a maior parte da janela tenha passado.

### 13.6 Impacto nos clientes

Se os passageiros podem ser afetados, pare e ligue para o contato de emergência antes de uma depuração profunda. Impacto nos clientes significa passageiros vendo erros no planejador de viagens. Qualquer indício de dano visível aos passageiros interrompe imediatamente todo trabalho de ENG, antes de a análise de causa raiz continuar, e a parada usa o mesmo modelo de mensagem do exercício do laço de autenticação. O impacto vem antes da curiosidade sobre uma causa raiz inacabada: a causa pode ser investigada depois que o contato de emergência confirmar que os passageiros não são mais afetados e que a homologação voltou a ficar estável.

### 13.7 Baseline sabidamente boa

Sam mantém um curl sabidamente bom para o endpoint de saúde da homologação. Se ele falha, o ambiente está quebrado e os achados esperam. Ao lado do curl, a baseline sabidamente boa é o script fixado da semana anterior e as linhas ok que ele imprimiu. Quando surge de repente uma tempestade de NOT APPROVED, Sam abre essa saída fixada e compara a nova execução com ela antes que alguém abra uma conversa culpando a rede. Se o script antigo ainda imprime as linhas esperadas, a mudança está no alvo ou no escopo; se não imprime, o ambiente é o primeiro suspeito.

### 13.8 Tempo limitado para o ego

Depois de quinze minutos sozinho, ele precisa pedir ajuda. O silêncio heroico desperdiça a janela do engajamento. O tempo limitado existe para proteger a janela do ENG-512 do orgulho. Quinze minutos travado numa ferramenta significam escalar para a dupla ou para o líder, e não tentar mais uma flag em silêncio. Quando o ego atrasa a chamada, a revisão pós-ação diz isso claramente e registra quantos minutos foram perdidos, para que o padrão fique visível para toda a equipe. Escalar cedo é recompensado nessa revisão, e não tratado como sinal de fraqueza.

### 13.9 Disciplina de campo

As notas de solução de problemas de Sam usam os mesmos rótulos Fato/Palpite dos casos. "Palpite: o WAF está bloqueando meu IP" só vira Fato depois que o log do WAF mostra o bloqueio. Essa disciplina o impede de "consertar" o WAF com volume para ver o que acontece — um comportamento que parece uma negação de serviço e viola as ROE. A disciplina de campo para a solução de problemas é árvore, baseline, dupla, tempo limitado e parada diante de impacto nos passageiros. A revisão pós-ação de Sam recompensa o escalonamento cedo. Esses hábitos importam mais do que resolver todas as falhas, porque cada um impede que uma sessão travada vire um teste não aprovado ou inseguro.

### 13.10 Nota de encerramento

Quando o escalonamento é necessário, Sam avisa juntos o líder do engajamento e o responsável pelo produto, para que ninguém saiba de segunda mão que a homologação não está saudável. A regra final é que a solução de problemas existe para proteger a janela e os sistemas por trás dela. Encontrar a falha plantada importa menos do que parar quando alertas de tarifa aparecem em qualquer lugar, então um alerta de tarifa encerra a solução de problemas mesmo com a falha plantada ainda sem solução. Uma falha não resolvida pode ser retomada na próxima sessão, mas um teste que continuou durante um alerta de tarifa é uma falha de segurança que nenhuma correção posterior desfaz.

### Exemplo resolvido (NMT sintética)

As verificações de API de Sam falham com erros de TLS; a homologação funciona normalmente no navegador do jump host. Ele atualiza o repositório de certificados raiz do notebook, executa de novo e documenta o problema do notebook separadamente dos achados.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX049 — Primeiros passos.** Ordene: escalar, reproduzir, verificar a ferramenta. *Rubrica:* 3 = reproduzir, verificar a ferramenta, escalar; 2 = quase; 1 = escalar sempre primeiro; 0 = nada.
- **EX050 — Não é achado.** Por que um erro de TLS no notebook não é um achado da API? *Rubrica:* 3 = repositório de confiança do lado do cliente; a homologação funciona em outro lugar; 2 = parcial; 1 = é achado; 0 = nada.
- **EX051 — Pacote de escalonamento.** Liste quatro itens de um pacote de escalonamento. *Rubrica:* 3 = quatro do capítulo; 2 = três; 1 = um; 0 = nada.
- **EX052 — Impacto nos passageiros.** E se a solução de problemas puder afetar os passageiros? *Rubrica:* 3 = parar; contato de emergência; 2 = parar; 1 = continuar; 0 = nada.

### Síntese

Resolva problemas com uma árvore, prove onde a falha está e escale com um pacote limpo.

### Continue estudando — capítulo 13 de 18

[← Capítulo 12 (rascunho)](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 (rascunho) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Automação

### Objetivos de aprendizagem

Você vai (1) decidir o que automatizar; (2) manter pessoas na validação; (3) agendar a automação dentro das janelas; (4) monitorar a automação para detectar laços.

### 14.1 Automatizar

Hashes, comparações de listas de portas, verificações de campos de chamados, esqueletos de relatório. A regra é automatizar apenas as verificações que Sam já faz do mesmo jeito toda semana, como classificar inventários e calcular hashes de evidências. As tarefas podem repetir esses caminhos comprovados, mas não podem inventar novos métodos, e uma automação que introduziria uma nova técnica de ataque é recusada para o ENG-512. A invenção de métodos fica, portanto, inteiramente fora da fila de automação; uma técnica nova precisa ser escrita como cartão de método, revisada e executada à mão primeiro.

### 14.2 Não automatizar

Exploração, decisões de escopo, severidade sem revisão. As decisões de parada e a ampliação do escopo também continuam humanas. Os operadores param diante de alertas de tarifa, e as tarefas nunca decidem sozinhas continuar. No código das tarefas, uma flag de alerta de tarifa é uma parada rígida que congela a execução, e não um aviso brando que um operador possa descartar. Manter essas escolhas fora da automação significa que um script não pode ampliar o ENG-512 nem continuar testando durante um alerta só porque ninguém estava olhando o console naquele momento. As classificações de severidade também esperam por um revisor humano antes de qualquer chamado ser aberto.

### 14.3 Janelas

A automação roda apenas dentro da janela do engajamento, com os mesmos limites de taxa. Os agendamentos das tarefas correspondem exatamente à janela de sábado das ROE. Tarefas livres de madrugada contra a homologação são violações do controle de mudanças, por mais convenientes que fossem, e os controles de acesso do agendador negam os usuários de ENG fora da janela assinada, para que a regra não dependa da memória. Isso mantém o tráfego automatizado dentro do período em que responsáveis e plantonistas o esperam e conseguem distinguir um teste de um problema real. Quando uma tarefa ainda está rodando no fechamento da janela, ela para e o restante espera pelo próximo horário combinado.

### 14.4 Detecção de laços

Limites de novas tentativas e de tempo máximo de execução são obrigatórios. A detecção de laços em cada tarefa encerra a execução quando respostas 401 se repetem além do orçamento de ruído. A parada das 10:12 do exercício sintético é o padrão que a automação deve copiar: a tarefa para, libera suas conexões e emite a mesma frase de interrupção que o exercício ensinou, para que o canal do engajamento receba uma mensagem que a equipe de resposta já reconhece. Uma tarefa sem limite de novas tentativas e sem limite de tempo de execução não está pronta para a janela de sábado, por melhor que tenha se saído num teste rápido.

### 14.5 Revisão da saída

Todo candidato a achado automatizado recebe validação humana. A revisão da saída é obrigatória antes que qualquer achado seja entregue. Linhas NOT APPROVED automatizadas ainda precisam de uma pessoa que verifique divergências de nome DNS, que a tarefa não consegue julgar, então o registro automático às cegas é recusado. As tarefas de abertura automática de chamados ficam desativadas até que essa etapa humana de divergência dê aprovação. A revisão custa alguns minutos por execução e evita que os responsáveis recebam chamados sobre hosts que apenas estavam listados com outro nome. Os revisores também confirmam que cada candidato corresponde a um host aprovado antes de virar chamado.

### 14.6 Controle de mudanças

Os scripts de automação são versionados como código de produção. O controle de mudanças da automação é igual ao controle de mudanças das ROE. Uma tarefa nova não pode entrar na janela de sábado até passar pela revisão por pares e até que o SOC seja avisado, com o mesmo modelo de um anúncio de mudança nas ROE. Acrescentar uma tarefa em silêncio é tratado como defeito, porque o SOC veria tráfego inesperado sem nenhum aviso que o explicasse e poderia responder como se fosse um ataque real. A versão da tarefa e o revisor que a aprovou são registrados com o aviso de mudança.

### 14.7 Tarefas idempotentes

Comparações automatizadas podem rodar duas vezes sem duplicar chamados. Sam usa host+porta+data como chave dos chamados para evitar duplicatas. O projeto idempotente é o que torna seguras essas novas execuções. Os geradores de relatório do ENG-512 de Sam fazem upsert pela chave do serviço em escuta, então executar uma tarefa uma segunda vez atualiza o chamado existente daquela porta, em vez de abrir uma duplicata. O upsert pela chave do serviço é coberto por um teste unitário no repositório de automação, para que uma mudança posterior no gerador de relatórios não reintroduza em silêncio chamados duplicados que os responsáveis teriam de fechar.

### 14.8 Chave de desativação

A automação tem uma flag global de desativação que o SOC pode solicitar. Sam testa essa flag no primeiro dia do engajamento. Com essa única flag, Sam pode desligar toda a automação de ENG se o planejador de viagens se comportar mal. O teste de desativação é um item do Laboratório II, e a chave precisa ser exercitada de ponta a ponta no ensaio; uma chave que existe só no papel mantém a tarefa fora da lista de sábado. Testá-la cedo significa que, se ela um dia for necessária durante uma janela real, ninguém estará descobrindo pela primeira vez se ela funciona de fato.

### 14.9 Disciplina de campo

Pull requests de automação precisam de um bloco de segurança: limites de taxa, interruptor de emergência, dry-run e a cláusula das ROE que permite a tarefa. Sem esse bloco, os revisores rejeitam o PR. Sam acrescentou o modelo depois que um script bem-intencionado rodou fora da janela porque o cron usava UTC e o autor pensava no horário local. A disciplina de campo para a automação é janela respeitada, atenção a laços, revisão e possibilidade de desativação. Esperteza sem supervisão não é um objetivo na NMT. Uma tarefa que falha em qualquer uma dessas quatro propriedades fica fora da lista de sábado até que a lacuna seja corrigida e revisada de novo por um colega.

### 14.10 Nota de encerramento

Sam acompanha num gráfico o tempo de execução da automação a cada noite. Uma tarefa que de repente leva dez vezes mais pode estar presa num laço ou lendo um inventário maior — os dois casos merecem um olhar humano antes da próxima janela. A automação multiplica bons cartões de método e também multiplica erros. Por isso, Sam só automatiza uma tarefa depois que uma execução manual do ENG-512 teve sucesso no mesmo caminho, com o cartão de método, a taxa e as evidências já revisados. Automatizar um caminho não comprovado apenas repete um erro não testado a cada execução agendada.

### 14.11 Extra

Os limites incluem tanto o número de novas tentativas quanto os minutos de relógio. A tarefa de comparação de portas de Sam morre depois de 20 minutos e o aciona; um travamento silencioso é tratado como um interruptor de parada que falhou. Como prática extra, Sam escreve um exercício de desativação no README de cada automação e o executa de fato no jump host antes de a tarefa ser agendada. Se a chave de desativação não foi testada, a tarefa fica fora da lista de sábado, porque uma chave que nunca foi acionada não dá garantia nenhuma. O README registra quando o exercício foi executado pela última vez, para que um revisor veja que a chave foi exercitada recentemente.

### Exemplo resolvido (NMT sintética)

Sam automatiza a comparação de portas toda noite sobre as exportações de inventário da homologação durante a semana do engajamento; ele continua triando à mão as linhas NOT APPROVED.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX053 — Lista do que automatizar.** Nomeie três bons candidatos à automação. *Rubrica:* 3 = três do capítulo; 2 = dois; 1 = um; 0 = nada.
- **EX054 — Nunca automatizar.** Nomeie duas coisas que Sam não deve automatizar. *Rubrica:* 3 = exploração e decisões de escopo; 2 = uma; 1 = hashes; 0 = nada.
- **EX055 — Limite de novas tentativas.** Por que as novas tentativas da automação precisam de limites? *Rubrica:* 3 = evitar bloqueios/tempestades de logs/laços; 2 = parcial; 1 = ilimitado é melhor; 0 = nada.
- **EX056 — Etapa humana.** O que sempre precisa de uma pessoa antes de um achado ser registrado? *Rubrica:* 3 = validação dos candidatos automatizados; 2 = parcial; 1 = nenhuma etapa; 0 = nada.

### Síntese

Automatize o repetitivo; nunca automatize permissão, exploração nem severidade sem revisão.

### Continue estudando — capítulo 14 de 18

[← Capítulo 13 (rascunho)](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 (rascunho) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Integração e dependências

### Objetivos de aprendizagem

Você vai (1) mapear dependências de terceiros; (2) saber quando o teste delas exige autorização separada; (3) testar o lado da NMT nas integrações; (4) registrar a responsabilidade compartilhada.

### 15.1 Dependências

Blocos de mapa, notificador por SMS, links diretos de pagamento, e-mail na nuvem. As dependências também incluem as CDNs de blocos de mapa e os provedores de identidade, e Sam as lista para que o ENG-512 não relate o tempo esgotado de uma CDN como achado contra a API da NMT. Ele compara cada tempo esgotado com os horários de atividade do ENG-512 antes de decidir a quem ele pertence, e guarda essa comparação ao lado do chamado da CDN. O notificador por SMS e os links diretos de pagamento recebem o mesmo tratamento, porque suas falhas aparecem dentro das telas dos passageiros da NMT. Sam registra um contato externo para cada dependência, quando há um conhecido, para que um chamado possa ir direto a quem consegue corrigi-lo.

### 15.2 Autorização separada

Testar o núcleo do fornecedor de SMS exige a autorização do fornecedor. Do mesmo modo, a assinatura da NMT nunca autoriza os sistemas de um processador de tarifas; esses processadores precisam de autorização escrita própria. Sam registra esses terceiros como exclusões explícitas na tabela de escopo, e cada linha de exclusão cita o ID da cláusula contratual ao lado do nome do processador. Uma linha explícita evita discussões posteriores sobre se um endpoint do fornecedor estava coberto implicitamente só porque o tráfego da NMT chega até ele. Quando um fornecedor quer que os próprios sistemas sejam testados, ele combina essa autorização diretamente com a própria equipe de segurança.

### 15.3 O lado da NMT

Sam pode testar como a NMT trata os callbacks dos fornecedores e o armazenamento de segredos quando esses caminhos estão no escopo. O lado da NMT num achado de dependência é a configuração que a NMT controla: redirecionamentos, chaves de API guardadas na NMT e regras do WAF. Os chamados de Sam miram esses itens, porque os responsáveis da NMT podem mudá-los. Os calendários de correção dos fornecedores são registrados como notas no achado, mas não são chamados de Sam e não pertencem a ele. Isso mantém cada item de correção atribuído a alguém que tem de fato a autoridade e o acesso para fazer a correção.

### 15.4 Matriz de responsabilidades

Quem corrige o quê fica escrito, para que os achados cheguem ao responsável certo. A matriz de responsabilidades nomeia um responsável da NMT e um responsável do fornecedor para cada dependência. Cada chamado de dependência precisa preencher as duas colunas antes que a revisão o aceite. Quando uma das células de responsável está vazia, o robô de triagem comenta que a matriz é necessária, e o chamado volta a quem o relatou antes que alguém atribua trabalho. A divisão evita que os achados fiquem pulando entre a NMT e um fornecedor enquanto cada lado supõe que o outro é responsável pela correção.

### 15.5 Quebras

Indisponibilidades de fornecedores durante os testes são paradas, e não oportunidades para insistir. Quando um caminho de CDN quebra durante o ENG-512, Sam não alega causalidade até que a quebra tenha sido correlacionada com os horários do engajamento. Os intervalos de relógio do ENG são colados nas notas do incidente da CDN, e a alegação espera por um aviso do SOC com relógios alinhados que corresponda à janela. Relógios sincronizados e aviso prévio ao SOC protegem os dois lados de culpas falsas, seja porque o teste causou a indisponibilidade, seja porque apenas estava rodando quando ela começou.

### 15.6 Contratos

Cláusulas de contato de segurança nos contratos com fornecedores agilizam a divulgação responsável. Os contratos também podem proibir testes nos sistemas do fornecedor, então Sam lê a cláusula pertinente antes de propor qualquer verificação voltada ao fornecedor. As cláusulas de proibição de teste são coladas na lista de exclusões das ROE, e as iniciais da revisão jurídica aparecem ao lado de cada cláusula colada no apêndice. Sem essas iniciais, a colagem é tratada como texto de ROE incompleto, porque uma cláusula mal lida poderia comprometer a NMT com testes que o contrato do fornecedor não permite. Qualquer dúvida sobre uma cláusula volta ao jurídico antes mesmo de a proposta ser redigida.

### 15.7 Autenticidade dos callbacks

Ao testar como a NMT trata os callbacks dos fornecedores, Sam usa ambientes de teste documentados, e não tráfego forjado contra endpoints de pagamento da produção. A autenticidade dos callbacks dos webhooks dos fornecedores é verificada apenas com segredos da homologação, nunca com segredos da produção. Os testes de Sam nunca reproduzem callbacks reais de passageiros, nem mesmo para uma demonstração. Os IDs dos segredos de homologação usados em cada teste de webhook são listados no índice de evidências, para que um revisor possa confirmar quais credenciais foram exercitadas e que nenhum segredo da produção nem dado de passageiro entrou no teste em momento algum.

### 15.8 Escopo da varredura de segredos

As varreduras de segredos rodam nos repositórios da NMT listados nas ROE, e não em todos os forks públicos da internet. O escopo da varredura de segredos fica dentro dos repositórios da NMT autorizados para o ENG-512, e o texto do escopo nomeia caminhos de repositório, e não a internet inteira. Varrer o GitHub público de um fornecedor sem permissão escrita está fora do escopo, por mais tentadora que seja uma busca rápida. A lista de caminhos permitidos das ferramentas de varredura é revista sempre que surgem novos repositórios da NMT, para que a cobertura só cresça por meio de uma decisão de escopo registrada.

### 15.9 Disciplina de campo

O mapa de dependências de Sam inclui uma coluna de "dados compartilhados": o que a NMT envia a cada fornecedor. Se a NMT não deveria enviar telefones de passageiros ao provedor de blocos de mapa, isso vira ao mesmo tempo um controle de privacidade e uma verificação de teste: inspecionar as requisições de saída em busca de campos inesperados durante os testes autorizados na homologação. A disciplina de campo para dependências é a matriz, a autorização separada e as correções do lado da NMT primeiro. Os fornecedores de tarifa ficam fora das sondagens comuns. A coluna de dados compartilhados amarra tudo isso, porque mostra quais fluxos de fornecedores a NMT pode testar do próprio lado e quais pertencem ao fornecedor.

### 15.10 Nota de encerramento

Se um fornecedor pede a Sam que "teste rapidinho" o portal dele usando credenciais da NMT, ele recusa e o encaminha ao próprio processo de autorização. Credenciais da NMT não viajam. O capítulo de dependências termina onde termina a tabela de escopo: dizendo com clareza quais sistemas de fornecedores a NMT não autorizou para testes. Sam repete essa lista no relatório, para que os leitores não suponham uma cobertura de processadores de tarifa que a Northline Municipal Transit nunca contratou. A mesma lista vai para a nota de passagem, para que o próximo técnico herde as exclusões junto com os achados.

### Exemplo resolvido (NMT sintética)

Sam encontra uma chave de API de SMS num repositório de homologação. Isso é um achado da NMT (armazenamento de segredos). Ele não faz teste de carga no fornecedor de SMS.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX057 — Exemplo de autorização separada.** Dê uma dependência que Sam não pode testar sem a autorização do fornecedor. *Rubrica:* 3 = fornecedor de SMS / blocos de mapa / pagamento; 2 = parcial; 1 = o site da NMT; 0 = nada.
- **EX058 — Achado do lado da NMT.** Por que uma chave de API de SMS vazada na homologação da NMT é um achado da NMT? *Rubrica:* 3 = a NMT armazena/manuseia o segredo; 2 = parcial; 1 = só do fornecedor; 0 = nada.
- **EX059 — Indisponibilidade do fornecedor.** O fornecedor esgota o tempo durante a janela. O que Sam faz? *Rubrica:* 3 = parar as verificações relacionadas; anotar a dependência; não martelar; 2 = parcial; 1 = tempestade de novas tentativas; 0 = nada.
- **EX060 — Matriz.** O que uma matriz de responsabilidades resolve? *Rubrica:* 3 = o responsável certo para cada achado; 2 = parcial; 1 = não resolve nada; 0 = nada.

### Síntese

Conheça o mapa de dependências; teste o lado da NMT; não ataque fornecedores sem a autorização deles.

### Continue estudando — capítulo 15 de 18

[← Capítulo 14 (rascunho)](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 (rascunho) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Documentação técnica e segurança

### Objetivos de aprendizagem

Você vai (1) escrever runbooks para verificações autorizadas; (2) manter visíveis os avisos de segurança; (3) versionar documentos; (4) aposentar métodos obsoletos.

### 16.1 Runbooks

Passo a passo para cada verificação recorrente, com referências às ROE e as condições de parada no topo, em negrito. O runbook do ENG-512 cobre a abertura, os cartões de método, as mensagens de parada e a limpeza. Cada chamado cita o hash git do runbook, e cada colega cola o mesmo hash no próprio caderno na abertura, como recibo. Assim, todos trabalham a partir de uma única versão dos capítulos de abertura e de parada, e uma edição posterior do runbook não pode deixar dois técnicos seguindo regras de parada diferentes na mesma janela de sábado.

### 16.2 Avisos de segurança

"Não execute contra a produção" é a primeira linha do runbook de comparação de portas da homologação. A primeira página de todo runbook traz os avisos de segurança: a rede de tarifas é preta e a varredura livre é proibida. As amostras de auditoria sempre abrem primeiro a página um, e um runbook cujo aviso de tarifa aparece só numa página tardia reprova na amostra e tem o chamado reaberto. Avisos enterrados na página nove não protegem ninguém, porque um técnico sob pressão de tempo lê os passos iniciais e raramente o apêndice.

### 16.3 Versionamento

Os documentos mostram versão, data e responsável; as versões antigas são arquivadas. As versões dos runbooks são acompanhadas por tags do git, e Sam não segue uma cópia impressa mais antiga que a tag nomeada nas ROE. A lista de abertura inclui um git describe contra essa tag; se a saída não confere, a abertura é cancelada até que a cópia seja alinhada. Uma página impressa pode ser conveniente na mesa, mas só a versão com tag vale quando uma regra de parada ou um contato mudou.

### 16.4 Aposentadoria

Métodos que usavam ferramentas aposentadas são marcados como obsoletos, para que os iniciantes não os sigam. A aposentadoria também remove cartões que mencionam hosts desativados. Esses cartões vão para o arquivo na mesma semana em que o host é desativado, para que uma verificação vencida não volte à pilha no sábado seguinte. Deixar páginas aposentadas na biblioteca ativa confundiria a próxima janela, porque um iniciante poderia seguir um método dirigido a um host que não existe mais ou que agora pertence a outra pessoa.

### 16.5 Público

Escreva para um técnico que estava doente durante o último engajamento. Os leitores são técnicos e o SOC, e não o marketing, então cada passo é escrito para que um técnico que perdeu o ENG-512 consiga segui-lo à noite sem ligar para Sam. As condições de parada aparecem em palavras simples, com um exemplo da mensagem de interrupção a publicar. Slogans e elogios a ferramentas são cortados antes de a edição para técnicos ser publicada, porque aumentam o tamanho sem ajudar ninguém a decidir o que fazer.

### 16.6 Ritmo de revisão

Os runbooks são revistos a cada seis meses ou depois de qualquer incidente de parada. Uma mudança de arquitetura também dispara uma revisão, mesmo quando a data de seis meses ainda está longe. Uma revisão perdida abre um chamado de dívida do programa, que tem responsável e prazo como qualquer achado, e o pacote do CISO lista a dívida de documentação em aberto ao lado dos achados técnicos. Tornar a dívida visível impede que runbooks desatualizados derivem em silêncio até que o próximo incidente de parada os exponha. Cada revisão é registrada com a tag de runbook que produziu, para que os leitores vejam quando uma página foi confirmada pela última vez.

### 16.7 Capturas de tela nos runbooks

Os runbooks preferem passos em texto a capturas de tela que envelhecem quando a interface muda. Onde as capturas ajudam, elas são datadas. Todas as capturas de tela dos runbooks são sintéticas e mascaradas; telas reais de passageiros nunca ilustram um procedimento. A mesma integração contínua que monta os materiais do curso rejeita pull requests que acrescentam capturas não sintéticas de passageiros, para que a política não dependa de os revisores perceberem. Figuras sintéticas ainda mostram os passos com clareza e eliminam o risco de que um documento de treinamento vire um depósito acidental de dados pessoais de passageiros.

### 16.8 Tradução

Se um turno de terceirizados fala outra língua, os avisos críticos de parada aparecem nas duas línguas usadas no local. A redação das frases de parada é combinada uma vez com o SOC e depois reaproveitada, em vez de improvisada durante um incidente. Empatia improvisada ou redação atenuada numa mensagem de parada não é um controle. As frases de interrupção combinadas são versionadas ao lado do trecho da carta de ética, então qualquer edição nelas precisa dos mesmos responsáveis que uma edição no texto de ética e não pode entrar despercebida entre as janelas.

### 16.9 Disciplina de campo

Quando acontece um incidente de parada, Sam atualiza o runbook na mesma semana ou registra um chamado explicando por que não. Documentação adiada para "depois do período corrido" é documentação que nunca acontece. Seus gestores aceitam runbooks mais curtos e atualizados em vez de longos que descrevem ferramentas aposentadas. A disciplina de campo para a documentação é versionada, com avisos, aposentadoria limpa e capturas sintéticas. O ENG-512 de Sam depende do runbook com tag, e não da memória. Um runbook que não pode ser seguido sem perguntar a Sam é tratado como inacabado, seja qual for seu tamanho ou acabamento.

### 16.10 Nota de encerramento

Runbooks obsoletos vão para uma pasta /archive, e a integração contínua verifica que nenhum link ativo aponta para ela. Links quebrados para métodos aposentados reprovam o build da documentação. A documentação é o modo pelo qual a NMT sobrevive às férias de Sam. Um substituto precisa encontrar no runbook as frases de parada e a exclusão da tarifa sem perguntar a Sam, então uma frase de parada ausente é tratada como defeito, e não como escolha de estilo. Quando os documentos estão completos e atualizados, o programa pode continuar testando com segurança enquanto o líder habitual está de licença.

### 16.11 Extra

Sam imprime a página de condições de parada do runbook ativo e a mantém na mesa durante as janelas — telas bloqueiam, e o papel continua legível quando os segundos importam. Como extra, Sam mantém uma folha de consulta de uma página do ENG-512 colada ao lado do jump host. Ela traz a data das ROE, os contatos de emergência e a exclusão da tarifa, e é substituída sempre que a data das ROE avança. Uma folha que corresponde às ROE vigentes dá ao técnico os limites essenciais num relance, sem abrir um documento enquanto uma parada está em andamento.

### Exemplo resolvido (NMT sintética)

O runbook v1.3 de Sam abre com `STOP CONDITIONS` e `OUT OF SCOPE: fare network`, e só depois vêm os passos da comparação de portas.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX061 — Topo do runbook.** Quais dois blocos ficam no topo? *Rubrica:* 3 = condições de parada e ROE/fora do escopo; 2 = um; 1 = histórico; 0 = nada.
- **EX062 — Primeira linha.** Qual é a primeira linha do runbook de comparação de portas da homologação? *Rubrica:* 3 = não executar contra a produção; 2 = parcial; 1 = instalar a ferramenta; 0 = nada.
- **EX063 — Obsoleto.** O que deve acontecer com um runbook de uma ferramenta aposentada? *Rubrica:* 3 = marcar como obsoleto/arquivar; 2 = parcial; 1 = deixar como está; 0 = nada.
- **EX064 — Gatilho de revisão.** Quando os runbooks precisam ser revistos fora do ritmo de seis meses? *Rubrica:* 3 = depois de um incidente de parada (ou de uma grande mudança); 2 = parcial; 1 = nunca; 0 = nada.

### Síntese

A documentação põe a segurança em primeiro lugar, continua versionada e se aposenta junto com suas ferramentas.

### Continue estudando — capítulo 16 de 18

[← Capítulo 15 (rascunho)](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 (rascunho) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Laboratório controlado II

### Objetivos de aprendizagem

Você vai (1) combinar cartões de método com laboratórios; (2) produzir um minirrelatório de reteste; (3) lidar com um exercício de parada no meio do laboratório; (4) entregar evidências indexadas por hash.

### 17.1 Construção

Crie um cartão de método; execute o lab_retest; escreva um relatório de reteste de uma página. O Laboratório II monta um miniENG-512 em torno desse cartão: inventário, lab_ports, evidências com hash, um exercício de parada e status de reteste. Os alunos reaproveitam o inventário do Laboratório I com uma nova falha plantada, para que uma resposta lembrada do primeiro laboratório não seja aprovada. Para passar, o aluno precisa encontrar o serviço NOT APPROVED plantado e entregar uma mensagem de parada ensaiada, junto com os hashes e a tabela de reteste que compõem o conjunto de entregas.

### 17.2 Exercício de parada

Num momento aleatório, o supervisor anuncia a parada; o aluno precisa publicar uma mensagem de parada conforme o padrão em até dois minutos. O exercício repete o laço de 401: interromper, publicar a mensagem de parada do ENG-512 com o horário e esperar orientação. Um aluno que continua depois do laço para terminar mais um objetivo reprova no Laboratório II, por mais perto que esse objetivo parecesse. Interromper e publicar vêm primeiro, porque o hábito avaliado é parar quando chamado, e um engajamento real não oferecerá um momento conveniente para concluir a tarefa em andamento.

### 17.3 Índice de evidências

Tabela de arquivo, hash e ID do achado. O índice de evidências do Laboratório II lista todos os arquivos PNG e TXT com seu prefixo de hash. Qualquer linha com MISMATCH precisa mostrar a aprovação de duas pessoas antes que o hash esperado seja atualizado. Os avaliadores abrem primeiro o índice e avaliam sua completude antes de ler qualquer narrativa, e os capítulos narrativos valem zero ponto se o índice estiver incompleto. A ordem reflete o trabalho real com casos, em que uma história bem escrita não salva evidências cuja integridade não pode ser demonstrada. Os prefixos de hash do índice também precisam conferir com os arquivos da cópia do cofre que o avaliador abre.

### 17.4 Desafio do colega

Um colega tenta convencer você a anexar um arquivo divergente; você recusa. O desafio do colega também procura uma exclusão de tarifa ausente ou um contato de emergência vazio. Corrigir uma lacuna com calma rende boa pontuação, enquanto discutir na defensiva perde pontos, mesmo que o artefato seja corrigido depois. A folha de pontuação mantém o tom e a qualidade do artefato em colunas separadas, então um aluno que corrige o caderno com elegância recebe crédito pelas duas coisas, e um artefato correto defendido de mau jeito ainda mostra os pontos perdidos no tom.

### 17.5 Tempo limitado

Duas horas. O tempo limitado do Laboratório II é fixado no calendário do curso. Quando o sinal do calendário toca, a digitação para, e qualquer estouro é registrado numa nota escrita com o título "estouro", que lista o que ficou inacabado. Minutos extras em silêncio não são permitidos, porque o laboratório pratica a disciplina de uma janela de engajamento real, em que o trabalho fora do horário combinado não é autorizado, por mais perto que o aluno estivesse de terminar. A nota de estouro é avaliada com honestidade, e um item inacabado listado ali custa menos que trabalho extra escondido.

### 17.6 Critério de aprovação

Exercício de parada + recusa + relatório coerente. Em detalhe, o critério de aprovação tem quatro partes: a falha plantada relatada, o exercício de parada limpo, todo hash mostrando MATCH ou um MISMATCH explicado e a conferência por pares aprovada. Faltar qualquer uma das quatro reprova no Laboratório II, mesmo com postura perfeita. Simpatia e apresentação confiante não substituem esses artefatos, porque um examinador que revise o portfólio depois vê apenas os arquivos, e não como o aluno soou. Os avaliadores registram qual das quatro falhou, para que o aluno saiba exatamente o que repetir.

### 17.7 Estresse sem dano

O exercício de parada é estressante de propósito; causar dano aos sistemas, não. Os supervisores nunca plantam falhas que afetem a produção. Estresse sem dano significa apenas carga sintética. Nenhum cenário do Laboratório II toca equipamentos de tarifa reais nem sistemas de produção dos passageiros, e a lista de materiais do laboratório proíbe explicitamente hardware de tarifa e dados de produção. A pressão vem do relógio e do anúncio aleatório de parada, e não de qualquer risco para sistemas reais, então um erro do aluno sob estresse custa pontos, e não o serviço aos passageiros.

### 17.8 Revisão pós-ação

Cada Laboratório II termina com três minutos de revisão pós-ação: o que quase deu errado e o que mudar no runbook. A revisão pós-ação produz três melhorias para o próximo ENG-512. Cada melhoria vira chamado e é ligada ao relatório do Laboratório II antes do aceite, e o supervisor não assina o aceite até que os três chamados existam. Sem eles, o Laboratório II continua incompleto na lista da turma. Exigir chamados, e não ideias faladas, significa que as lições de um quase acidente chegam de fato ao runbook, em vez de se apagarem depois da sessão.

### 17.9 Disciplina de campo

O desafio do colega no Laboratório II é uma encenação de pressão: "anexa logo, o hash está quase igual". A resposta correta é sempre recusar. Sam já ouviu pressões parecidas em engajamentos reais sobre saídas de ferramentas de varredura não verificadas. Praticar a recusa com um colega torna mais fácil a recusa real. A disciplina de campo para o Laboratório II é exercício, evidências, desafio do colega e critério de aprovação. O laboratório existe para tornar o ENG-512 tediosamente seguro. Duas partes do critério de aprovação da seção 17.6 nunca são negociáveis: o serviço NOT APPROVED plantado precisa ser encontrado e a mensagem de parada precisa ser ensaiada de forma limpa.

### 17.10 Nota de encerramento

A mensagem de parada de Sam no exercício usa o mesmo modelo dos engajamentos de produção, para que a memória muscular da redação se transfira. Prosa rebuscada é desencorajada; os fatos vencem. O Laboratório II é a última etapa antes do projeto de Sam, e um exercício de parada reprovado bloqueia o crédito de portfólio até ser ensaiado de forma limpa. O bloqueio é aplicado na prática: os repositórios do projeto continuam trancados até que o exercício de parada do aluno mostre uma aprovação limpa dos pares, então a etapa não pode ser pulada começando o projeto mais cedo. O aluno que reprova no exercício simplesmente ensaia de novo até que fique limpo.

### 17.11 Extra

Se a mensagem do exercício de parada atrasa, o laboratório reprova mesmo que o relatório seja perfeito. A velocidade de parar é a habilidade medida. Como extra, Sam guarda o texto da mensagem de parada do Laboratório II como modelo no runbook, e as paradas reais do ENG-512 copiam sua estrutura em vez de prosa livre. Como o modelo agora é o oficial, qualquer pull request que o altere precisa do aceite da turma do Laboratório II. Isso mantém idênticas a redação ensaiada e a redação real, para que o hábito aprendido no exercício seja o hábito usado no sábado.

### Exemplo resolvido (NMT sintética)

Sam publica uma mensagem de parada em 50 segundos durante o exercício, recusa uma captura de tela ruim e registra um relatório de reteste com o F2 ainda aberto.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX065 — Critério de aprovação.** Nomeie três requisitos de aprovação. *Rubrica:* 3 = exercício de parada, recusa, relatório coerente; 2 = dois; 1 = um; 0 = nada.
- **EX066 — Prazo da parada.** Qual é o limite de tempo para a mensagem de parada? *Rubrica:* 3 = dois minutos; 2 = rápido; 1 = fim do dia; 0 = nada.
- **EX067 — Honestidade do relatório.** O relatório pode marcar o F2 como encerrado sem evidências? *Rubrica:* 3 = não; 2 = não, sem explicação; 1 = sim; 0 = nada.
- **EX068 — Campos do índice.** Quais três campos estão no índice de evidências? *Rubrica:* 3 = arquivo, hash, ID do achado; 2 = dois; 1 = um; 0 = nada.

### Síntese

O Laboratório II acrescenta disciplina de parada e relato honesto do reteste sob pressão.

### Continue estudando — capítulo 17 de 18

[← Capítulo 16 (rascunho)](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 (rascunho) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Projeto técnico supervisionado

### Objetivos de aprendizagem

Você vai (1) entregar um pequeno projeto de teste autorizado sobre dados sintéticos da NMT; (2) apresentá-lo a um supervisor; (3) passar adiante os runbooks; (4) declarar os limites que permanecem.

### 18.1 Briefing do projeto

Usando apenas exportações sintéticas, produza: a comparação atualizada de portas aprovadas, dois achados validados com hashes de evidência, um relato de reteste e uma melhoria de runbook. O briefing do projeto pede um pacote com escopo no estilo ENG para a NMT sintética — diagrama, lista de verificação das ROE, resultado do lab_ports, hashes, reteste com FIXED/STILL OPEN e registro do exercício de parada. Nada de sondagens de tarifa, nada de dados de produção. As duas listas descrevem o mesmo pacote por dois ângulos: as entregas acima são o que o supervisor avalia, e o briefing nomeia os artefatos que precisam sustentá-las. Cada item é construído a partir das exportações sintéticas, com a rede de tarifas intocada.

### 18.2 Apresentação

Quinze minutos para o supervisor e um observador do SOC. A apresentação de Sam abre com as exclusões e os itens ainda abertos, como o F2, e só então passa às evidências. Slides que elogiam ferramentas sem hashes por trás reprovam na etapa da apresentação; qualquer elogio a ferramentas vai para um apêndice. O observador do SOC confere se o caminho de parada mostrado nos slides corresponde ao que o SOC de fato recebeu durante a janela. As perguntas do supervisor sobre qualquer item aberto são respondidas a partir das evidências, e não da memória.

### 18.3 Passagem

Runbooks e scripts no repositório da equipe, com versões. A passagem também inclui o caminho do cofre, os itens abertos e os contatos de emergência. O e-mail sozinho é uma transferência incompleta, então uma demonstração no jump host é agendada, e a lista de transferência exige o convite de calendário como anexo para provar que a demonstração foi marcada, e não apenas prometida. A demonstração permite ao técnico que recebe ver as ferramentas funcionando e fazer perguntas antes de assumir o trabalho. Ela também confirma que quem recebe consegue abrir o caminho do cofre antes que Sam se afaste.

### 18.4 Limites

Sam ainda não faz desenvolvimento de exploits nem projeto de cenários guiados por ameaças — temas de cursos mais longos. A página de limites declara que a rede de tarifas está fora do escopo, que todo o trabalho usou dados sintéticos e que Sam não tem autorização para testar sistemas reais. Cada limite aponta para a linha das ROE que o define, para que os examinadores possam verificar que a página não exagera a autoridade. Um colega revisa a redação dos limites antes da entrega, e os examinadores são orientados a ler esse apêndice primeiro, porque limites escondidos inventam uma cobertura que nunca existiu.

### 18.5 Próximo curso

Segurança de IA (066) é o próximo no caminho curricular. Dentro da própria trilha de red team, o próximo livro é o do nível de tecnólogo, que acrescenta profundidade em projeto e integração. Este livro técnico termina na competência procedimental sob ROE, então o trabalho pesado de projeto espera por esse curso. Antes que os concluintes sigam adiante, Sam diz a eles quais hábitos se transferem diretamente, como a disciplina de parada e o cálculo de hashes das evidências, e qual autoridade não se transfere para nenhum engajamento novo. O livro de segurança de IA citado acima continua sendo o próximo título no caminho curricular mais amplo, fora desta trilha.

### 18.6 Folha de rosto de segurança

A capa do projeto declara que ele é apenas sintético e sem varredura real. A folha de rosto de segurança repete as regras centrais: homologação primeiro, rede de tarifas em preto, as condições de parada e o prazo de exclusão da retenção. Ela é a página um do repositório do projeto, antes de qualquer código. Um robô de revisão verifica que ela é o primeiro arquivo que os revisores veem na árvore, e os merges falham se a capa estiver aninhada em outro lugar, para que ninguém leia os scripts sem antes ler os limites que os regem. Os avaliadores conferem a capa antes de qualquer outro arquivo da entrega.

### 18.7 Higiene do repositório

Os scripts do projeto entram no repositório da equipe sem credenciais, com README e cabeçalhos de licença conforme a política da NMT. A higiene do repositório proíbe segredos e inventários reais; só inventários sintéticos podem ser enviados. Um segredo no git reprova o projeto, seja qual for a qualidade dos achados, e o mesmo vale para um clone que contenha dados reais de inventário. O README precisa mostrar logo de início as instruções de desativação e de parada, para que qualquer pessoa que execute os scripts depois saiba como pará-los antes de saber como iniciá-los.

### 18.8 Ciclo de retorno

O retorno do supervisor vira duas edições de runbook em até uma semana — projeto concluído significa processo melhorado. Os comentários do supervisor viram correções de runbook na mesma semana, e Sam nunca arquiva retorno sem ler. Os links dessas correções da mesma semana são colados na nota de passagem do projeto. Uma nota de passagem sem eles é devolvida como incompleta até que os links estejam presentes, o que garante que o retorno mudou visivelmente o processo, em vez de ser reconhecido e esquecido. O supervisor pode então ver cada comentário ligado à mudança que produziu.

### 18.9 Disciplina de campo

A folha de rosto do projeto supervisionado tem uma página: declaração de uso apenas sintético, ID do engajamento do pacote de dados da sala de aula, lista de entregas com hashes, assinatura do supervisor e a declaração de limites de Sam. Sem a folha de rosto, o projeto está incompleto, mesmo que o trabalho técnico seja excelente. A disciplina de campo para o projeto é briefing, limites, folha de rosto de segurança, repositório limpo e STILL OPEN honesto. Esses cinco são o critério de aprovação. Um projeto que cumpre os cinco é aprovado mesmo quando relata itens abertos, enquanto um projeto a que falte um deles reprova, por mais polidos que pareçam seus achados.

### 18.10 Nota de encerramento

Depois da aceitação, Sam marca uma sessão de orientação de trinta minutos sobre os temas de controle de acesso do OWASP WSTG que ele quer aprofundar — o aprendizado contínuo faz parte da nota do projeto na NMT. O projeto prova que Sam consegue manter os hábitos do ENG-512 sem um professor na sala, e o crédito de portfólio exige artefatos que comprovem esses hábitos solo; a intenção não basta. Os artefatos são a evidência de que esses hábitos são reais: um pacote que mostra o exercício de parada, os hashes e os status de reteste honestos ganha a nota, enquanto a promessa de trabalhar assim não ganha.

### 18.11 Extra

A pergunta do observador do SOC costuma ser sobre detecção: Sam prepara uma técnica do ATT&CK e uma fonte de logs que recomendaria para cada achado. Como extra, Sam anexa as saídas do lab_ports e do lab_hash literalmente num apêndice. Assim, os examinadores podem reproduzir por conta própria as linhas NOT APPROVED, MATCH e MISMATCH e compará-las com os achados, sem precisar de uma reunião para perguntar como um resultado foi produzido. A saída literal também impede que um resumo suavize em silêncio um resultado que as ferramentas relataram de forma mais dura.

### Exemplo resolvido (NMT sintética)

O projeto de Sam é aceito com elogios por deixar o F2 aberto e pelo desempenho no exercício de parada do Laboratório II. Ele arquiva a folha de rosto e o plano para o próximo curso.

> **Caso sintético — Northline Municipal Transit (NMT).** A operadora de transporte, Sam Park e todos os números foram inventados para fins didáticos.

### Erros e limites

Sistemas de transporte reais e equipamentos de tarifa nunca são testados sem uma autorização separada e especializada. Este livro usa apenas dados sintéticos e não concede autorização para testar sistemas reais.

### Exercícios

- **EX069 — Entregas.** Liste quatro entregas do projeto. *Rubrica:* 3 = quatro do briefing; 2 = três; 1 = uma; 0 = nada.
- **EX070 — Por que deixar o F2 aberto.** Por que deixar o F2 aberto é um ponto forte? *Rubrica:* 3 = honestidade; integridade da verificação; 2 = parcial; 1 = fraqueza; 0 = nada.
- **EX071 — Limite.** Nomeie uma habilidade que Sam ainda não pode reivindicar. *Rubrica:* 3 = desenvolvimento de exploits ou liderar testes guiados por ameaças; 2 = parcial; 1 = comparação de portas; 0 = nada.
- **EX072 — Próximo curso.** Qual é o curso 066? *Rubrica:* 3 = segurança de IA; 2 = IA; 1 = errado; 0 = nada.

### Síntese

O projeto técnico comprova um ofício de teste disciplinado sobre dados sintéticos e limites honestos.

### Continue estudando — capítulo 18 de 18

[← Capítulo 17 (rascunho)](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções ↓](#worked-results) · [Próximo curso pelo índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX072. A Northline Municipal Transit, Sam Park e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX033.** Propósito, referência às ROE, ferramenta/configurações, condições de parada, evidência esperada (também a versão).

**EX034.** Para evitar derrubar a homologação, bloquear contas ou inundar os logs.

**EX035.** O tempo é limitado e verificações apressadas deixam de validar; concentre-se primeiro nos temas de alto risco.

**EX036.** Password spraying e testes de negação de serviço.

**EX037.** A falta do HSTS é um achado de configuração; o acesso às viagens de outro usuário é um achado de lógica/autorização da aplicação.

**EX038.** A configuração, o sistema, o risco caso seja aplicada de forma errada e um passo de reversão.

**EX039.** O responsável pelo sistema, pelo processo de mudanças da NMT; o testador verifica depois.

**EX040.** Elas muitas vezes contornam as baselines e não são revertidas, deixando um desvio inseguro.

**EX041.** `fixed: 2 open: 1` (dois corrigidos, um ainda aberto).

**EX042.** Ele continua aberto, com evidências do reteste anexadas mostrando que o problema permanece.

**EX043.** O CISO ou o dono do risco nomeado, por escrito.

**EX044.** O reteste mede se as correções combinadas funcionaram; uma nova caçada precisa de autorização própria.

**EX045.** As saídas do lab_ports, do lab_hash e do lab_retest.

**EX046.** Recusar anexá-lo e capturar de novo ou restaurar um arquivo que confira.

**EX047.** Qualquer tentativa de varrer ou tocar os sistemas de produção da NMT.

**EX048.** Se as classificações correspondem à lista de serviços aprovados.

**EX049.** Reproduzir, verificar a ferramenta/conta/escopo e então escalar, se necessário.

**EX050.** A API de homologação funciona no navegador do jump host; a falha está no repositório de confiança do notebook de Sam.

**EX051.** Sintoma, passos tentados, capturas de tela, horário e o que foi descartado.

**EX052.** Parar e acionar o contato de emergência antes de continuar.

**EX053.** Hashes, comparações de portas, verificações de campos de chamados (também esqueletos de relatório).

**EX054.** Exploração e decisões de escopo (e severidade sem revisão humana).

**EX055.** Novas tentativas ilimitadas podem bloquear contas, inundar os logs ou entrar em laço para sempre.

**EX056.** A validação de que o candidato automatizado é um problema real, dentro do escopo e com impacto.

**EX057.** O serviço de produção do fornecedor de SMS (ou os blocos de mapa / o processador de pagamentos).

**EX058.** A NMT responde pelo modo como armazena e expõe a chave em seus sistemas.

**EX059.** Parar as verificações relacionadas, anotar a indisponibilidade e evitar tempestades de novas tentativas.

**EX060.** Ela envia cada achado a quem de fato consegue corrigi-lo.

**EX061.** Condições de parada e avisos de ROE/fora do escopo.

**EX062.** Um aviso claro para não executar o procedimento contra a produção.

**EX063.** Marcá-lo como obsoleto e arquivá-lo, para que não seja seguido.

**EX064.** Depois de qualquer incidente de parada ou de uma grande mudança no sistema.

**EX065.** Exercício de parada bem-sucedido, recusa da evidência ruim e um relatório de reteste coerente.

**EX066.** Dois minutos a partir do anúncio do supervisor.

**EX067.** Não. O F2 continua aberto sem evidência de correção.

**EX068.** Nome do arquivo, hash e ID do achado.

**EX069.** Comparação de portas, dois achados validados com hashes, um relato de reteste e uma melhoria de runbook.

**EX070.** Isso mostra uma verificação honesta, em vez de chamados encerrados sem evidências.

**EX071.** Desenvolvimento de exploits ou liderar um engajamento guiado por ameaças no estilo CBEST/TIBER.

**EX072.** Segurança de IA.

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
