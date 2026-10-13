# Segurança Ofensiva Autorizada e Red Team: Um Livro para a Graduação em Engenharia

- Idioma: português do Brasil (`pt`); cinco anos; aproximadamente 4.000 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–12 de 50 já estão escritos em português, com os exercícios EX001–EX036 e suas resoluções com rubricas de 0 a 3; os capítulos 13–50 (EX037–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: futuros engenheiros de sistemas de segurança que vão projetar ferramentas de avaliação autorizada e plataformas de medição e relato.
- Relação com os livros vizinhos: o [livro de bacharelado](../../../../bachelors-4-years/offensive-security-red-team/en/book/MANUSCRIPT.md) é mais amplo; o [livro de tecnólogo](../../../../technologist-3-years/offensive-security-red-team/en/book/MANUSCRIPT.md) é mais voltado à implementação. **Este livro é centrado no projeto**: requisitos, arquitetura, controles, verificação e evidências de projeto final para plataformas autorizadas de red team.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação e **não concede autorização para testar sistemas reais**. Todas as organizações, pessoas, achados e números são **sintéticos**, salvo quando uma frase cita uma fonte pública. Os laboratórios ensinam escopo, medição e relato — nunca técnicas transformadas em arma.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Cada capítulo tem objetivos de aprendizagem, texto didático, um exemplo resolvido, erros e limites, exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios são determinísticos, rodam offline com `python3 arquivo.py` sobre dados sintéticos e imprimem os resultados mostrados como saída verificada.

### O exemplo contínuo (sintético): Riverstone Transit

> **Caso sintético — ficção.** A **Riverstone Transit** é inventada. Ela opera o TrackScope (verificador de escopo e de regras de engajamento), o FindingsDesk (ferramenta de tickets e severidade) e o PulseMap (relatório de cobertura ATT&CK). *Sam Ito*, estagiário de engenharia na equipe da plataforma de avaliação autorizada, acompanha esses sistemas ao longo do curso. Todos os números são inventados; todos os testes acontecem em cópias isoladas, com dados sintéticos e autorização por escrito.

### Política de fontes

As fontes foram conferidas em 12 de outubro de 2026: [NIST SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); [MITRE ATT&CK](https://attack.mitre.org/); [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide) (guia de implementação de 2024). Albrecht e Jensen (arXiv:2010.06377) criticam pontuações de segurança vazias. O conteúdo jurídico é orientação, não aconselhamento.

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

Capítulos 13–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-13), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) modelar uma quantidade acumulada numa avaliação como a integral de uma taxa; (2) usar uma derivada para descobrir quando uma taxa atinge o pico; (3) transformar as duas num limite de taxa que Sam Ito consiga defender nas regras de engajamento (ROE).

### 1.1 Taxas e acúmulos num engajamento

Todo teste autorizado produz tráfego, e o cliente se importa com duas coisas: a velocidade com que ele chega e quanto se acumula. Se uma tarefa de enumeração envia requisições à taxa r(t) requisições por segundo, o total enviado entre os instantes a e b é a integral ∫ r(t) dt de a até b. Uma ROE que diz "no máximo 5 requisições por segundo" limita r(t); uma que diz "no máximo 20.000 requisições por dia contra a API de tickets" limita a integral. São restrições diferentes, e um cronograma pode satisfazer uma enquanto viola a outra.

### 1.2 Encontrando o pico

Suponha que o TrackScope acelere uma varredura e depois a desacelere, com r(t) = 6t − t² requisições por segundo para 0 ≤ t ≤ 6 minutos (t em minutos, sintético). A derivada r′(t) = 6 − 2t se anula em t = 3, onde r(3) = 9 requisições por segundo. Se o teto da ROE é 5 por segundo, esse cronograma o viola entre as duas raízes de 6t − t² = 5, isto é, t = 1 e t = 5 minutos. O cálculo diz não apenas *se* um plano quebra o limite, mas *por quanto tempo*, que é a primeira pergunta da equipe de operações do cliente.

### 1.3 Do total ao cronograma

O total dessa rampa é ∫₀⁶ (6t − t²) dt = [3t² − t³/3]₀⁶ = 108 − 72 = 36 requisição-minutos por segundo, ou seja, 36 × 60 = 2.160 requisições. Um cronograma plano a 5 por segundo precisaria de 2.160 / 5 = 432 segundos, 7,2 minutos, para enviar o mesmo volume sem nenhuma violação. Engenheiros preferem o cronograma plano porque seu pico é igual à sua média e é trivial de verificar a partir dos logs. > **Caso sintético — Riverstone Transit.** A rampa que Sam esboçou para o teste do gateway de tarifas atingia 9 req/s; a ROE permitia 5. Sam a substituiu por um token bucket de 5 req/s (veja o Capítulo 36) e anexou o cálculo da integral à solicitação de mudança.

### 1.4 Erros e limites

O tráfego real é feito de rajadas, não é suave; um modelo contínuo dá uma visão de caso médio, e o limite da ROE precisa ser imposto por um mecanismo, não pelo cálculo. As unidades causam a maior parte dos erros: mantenha segundos e minutos separados. A imposição pertence à configuração do scanner e a um limitador de taxa de rede que o cliente consiga ver, para que um erro no cronograma não ultrapasse silenciosamente o limite acordado. Ao converter entre minutos e segundos, escreva as unidades ao lado de cada número e confira o valor final com uma estimativa grosseira. As rajadas significam que um pico curto pode quebrar um limite por segundo mesmo quando a média horária está boa; por isso, Sam Ito define na ROE um teto de janela curta e outro de janela longa e os testa antes do início do engajamento.

### Exercícios

- **EX001 — Janela de violação.** Para r(t) = 8t − t² req/s (t em minutos, de 0 a 8) e um teto de 7 req/s, encontre o pico e o intervalo durante o qual o teto é violado. Rubrica: 3 = pico 16 em t=4 e violação entre t=1 e t=7 (6 minutos); 2 = um deslize; 1 = apenas o pico; 0 = nada.
- **EX002 — Dois tipos de limite.** Dê uma cláusula de ROE que limite uma taxa e outra que limite um total, para a mesma API, e diga qual delas uma verificação baseada em logs confere com mais facilidade. Rubrica: 3 = as duas cláusulas com unidades e resposta justificada; 2 = cláusulas sem justificativa; 1 = uma cláusula; 0 = nada.
- **EX003 — Equivalente plano.** Quanto tempo um cronograma plano de 4 req/s leva para enviar as 2.160 requisições do §1.3? Rubrica: 3 = 540 s (9 minutos) com o cálculo; 2 = número certo, sem unidades; 1 = apenas o método; 0 = nada.

### Síntese

Um limite de taxa e um limite de volume são a derivada e a integral da mesma curva. Conferir os dois transforma uma promessa vaga de "baixo impacto" em números que o cliente pode auditar.

### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) expressar o escopo como conjuntos e predicados; (2) provar uma propriedade simples de uma regra de escopo; (3) contar o tamanho de um escopo para que as alegações de cobertura tenham um denominador.

### 2.1 Escopo é um conjunto

O escopo escrito lista o que pode ser testado: redes em escopo I, portas em escopo P e uma lista de exclusão D. O conjunto de alvos permitidos é T = {(h, p) : h ∈ I, h ∉ D, p ∈ P}. Escrever o escopo dessa forma expõe ambiguidades que uma ROE em prosa esconde. "A rede 10.20.0.0/16, exceto o gateway" é a diferença de conjuntos I \ D com D = {10.20.0.1}. "Serviços web" não é um conjunto até que alguém liste as portas. Quando os alvos são pares de host e porta, toda ação proposta pode ser conferida contra o mesmo predicado. Frases ambíguas como "serviços web" desaparecem, porque o conjunto contém uma porta ou não contém. A lista de exclusão fica dentro da definição de T, de modo que esquecer de aplicá-la é um erro de código, e não uma decisão de julgamento durante o teste. Sam mantém a ROE escrita e o conjunto legível por máquina na mesma mudança, para que não possam divergir.

### 2.2 Predicados e provas

O TrackScope implementa o predicado allowed(h, p) = inCIDR(h, I) ∧ ¬(h ∈ D) ∧ (p ∈ P). Como toda cláusula é uma conjunção, acrescentar um host a D só pode encolher T: se (h, p) ∈ T depois da mudança, então já estava em T antes. Vale a pena provar e testar essa monotonicidade, porque o oposto (uma mudança que amplia o escopo silenciosamente) é o incidente que os engenheiros mais querem evitar. Um teste unitário confere a propriedade em todos os pares tirados de um pequeno universo sintético.

```python
"""Check proposed engagement targets against a written scope (synthetic)."""
SCOPE_CIDRS = [("10.20.0.0", 16), ("192.168.50.0", 24)]  # inclusive synthetic ranges
SCOPE_PORTS = {22, 80, 443, 8080}
DENY_HOSTS = {"10.20.0.1", "192.168.50.1"}  # out-of-scope infra

def ip_int(s):
    a,b,c,d = map(int, s.split("."))
    return (a<<24)|(b<<16)|(c<<8)|d

def in_cidr(ip, net, bits):
    mask = (0xFFFFFFFF << (32-bits)) & 0xFFFFFFFF
    return (ip_int(ip) & mask) == (ip_int(net) & mask)

def check(host, port):
    reasons = []
    if host in DENY_HOSTS:
        reasons.append("deny-list")
    if not any(in_cidr(host, n, b) for n,b in SCOPE_CIDRS):
        reasons.append("outside-cidr")
    if port not in SCOPE_PORTS:
        reasons.append("port-not-in-scope")
    return ("ALLOW" if not reasons else "DENY"), reasons

tests = [
    ("10.20.1.10", 443),
    ("10.20.0.1", 443),
    ("192.168.50.20", 22),
    ("192.168.50.20", 3389),
    ("8.8.8.8", 80),
    ("192.168.1.10", 80),
]
for h,p in tests:
    v, r = check(h,p)
    print(f"target={h}:{p} decision={v} reasons={','.join(r) or '-'}")
```

Saída esperada:

```text
target=10.20.1.10:443 decision=ALLOW reasons=-
target=10.20.0.1:443 decision=DENY reasons=deny-list
target=192.168.50.20:22 decision=ALLOW reasons=-
target=192.168.50.20:3389 decision=DENY reasons=port-not-in-scope
target=8.8.8.8:80 decision=DENY reasons=outside-cidr
target=192.168.1.10:80 decision=DENY reasons=outside-cidr
```

### 2.3 Contando o denominador

Um /16 contém 2¹⁶ = 65.536 endereços; um /24 contém 256. Com quatro portas permitidas e um host excluído, |T| = (65.536 − 1 + 256) × 4 = 263.164 pares host–porta. Ninguém testa todos os pares, então a cobertura precisa ser declarada como "pares examinados / |T|" ou como uma fração amostrada, nunca como "a rede foi coberta". > **Caso sintético — Riverstone Transit.** O primeiro rascunho da ROE dizia "todos os sistemas das garagens". Sam o reescreveu como dois CIDRs, um conjunto de portas e uma lista de exclusão de um host, e o líder de rede do cliente descobriu que um CIDR de garagem também continha um quiosque de um fornecedor, que foi acrescentado a D antes da assinatura.

### 2.4 Erros e limites

Conjuntos descrevem a intenção, não a realidade: o DHCP pode mover um host para dentro ou para fora de uma faixa durante o teste, então o predicado precisa ser reavaliado a cada ação. CIDRs sobrepostos são contados em dobro se você somar os tamanhos de forma ingênua; use inclusão–exclusão. Reavaliar o predicado antes de cada ação custa pouco e pega um host que mudou de lugar durante o dia. Quando duas faixas se sobrepõem, somar seus tamanhos duas vezes é o erro comum; calcule a união. Um arquivo de escopo correto no kickoff pode estar errado na hora do almoço se o cliente renumerar uma sub-rede, e é por isso que o TrackScope registra a versão do arquivo de escopo em cada decisão.

### Exercícios

- **EX004 — Notação de conjuntos.** Escreva o conjunto de alvos permitidos para as redes 192.168.50.0/24, portas {22, 443} e lista de exclusão {192.168.50.1, 192.168.50.254}. Rubrica: 3 = expressão de conjunto correta e |T| = 508; 2 = expressão sem a contagem; 1 = parcial; 0 = nada.
- **EX005 — Monotonicidade.** Prove que acrescentar uma porta a P só pode ampliar T e diga qual regra de revisão isso implica. Rubrica: 3 = prova mais "acréscimos de porta precisam de um segundo aprovador"; 2 = apenas a prova; 1 = afirmação; 0 = nada.
- **EX006 — Leitura do laboratório.** Na saída do laboratório, por que 192.168.50.20:3389 é negado enquanto 192.168.50.20:22 é permitido? Rubrica: 3 = porta 3389 fora de P, host em I e fora de D; 2 = motivo sem as outras cláusulas; 1 = vago; 0 = errado.

### Síntese

Trate o escopo como um predicado sobre um conjunto contável. Assim ele pode ser testado e contado, e é possível mostrar que uma mudança nele não o amplia.

### Continue estudando — capítulo 02 de 50

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar propagação de sinal, largura de banda e latência ao que um teste consegue observar; (2) estimar os efeitos colaterais físicos do tráfego de teste; (3) explicar por que testes de rádio e de acesso físico precisam de autorização separada.

### 3.1 A latência tem um piso

Os sinais na fibra viajam a cerca de dois terços da velocidade da luz, aproximadamente 200.000 km/s, então 1.000 km de fibra acrescentam cerca de 5 ms em cada sentido. Quando o TrackScope relata um tempo de ida e volta de 40 ms até um servidor de garagem a 300 km de distância, cerca de 3 ms são propagação, e o resto é enfileiramento, comutação e processamento. Engenheiros usam esse piso para conferir a plausibilidade de evidências de tempo: um tempo de ida e volta *abaixo* do piso de propagação significa que a medição ou a suposição de localização está errada.

Se um tempo de ida e volta medido é menor do que a luz levaria para percorrer a distância alegada, ou o servidor está mais perto do que se pensava ou o relógio está errado. Sam usa o piso como verificação de evidências, não como localizador: muitos caminhos fazem rotas mais longas, então uma latência alta não prova nada sobre a distância. Em links de garagem de algumas centenas de quilômetros, alguns milissegundos de propagação são normais; dezenas de milissegundos de processamento num sistema de tarifas ocupado também são normais e não devem ser lidos como prova de um host distante.

### 3.2 Largura de banda e serialização

O tempo de serialização é o tamanho dividido pela taxa do link. Um quadro de 1.500 bytes num uplink de garagem de 10 Mb/s leva 1.500 × 8 / 10⁷ = 1,2 ms para ser colocado no meio. Se uma varredura autorizada envia 2.000 sondas pequenas por segundo, com 100 bytes cada, ela consome 1,6 Mb/s, 16% desse uplink, e é por isso que links de OT e de filiais com pouca banda recebem limites de ROE mais rígidos que as redes de data center. O tempo de serialização se soma a cada pacote antes de qualquer atraso de processamento. Num uplink lento, muitas sondas pequenas se acumulam mais depressa do que os engenheiros esperam, porque cada sonda ainda carrega cabeçalhos. Dezesseis por cento de um link de garagem já bastam para incomodar as operações e disparar alarmes de capacidade. Por isso, Sam dimensiona as varreduras pelo menor link em escopo, não pelo núcleo do data center, e escreve na ROE a taxa de link assumida, para que o cliente possa corrigi-la.

### 3.3 Calor, energia e meios físicos

A computação dissipa energia na forma de calor. Um teste de estresse que mantém a CPU de um validador de tarifas embarcado a 100% pode levá-lo além do seu envelope térmico num quiosque vedado; isso é uma questão de segurança operacional (*safety*), não um achado de segurança da informação. O rádio é um meio físico compartilhado com pessoas que nunca assinaram a ROE: avaliações de Wi-Fi e Bluetooth transmitem para o espaço público e são reguladas, então precisam de autorização explícita por escrito que nomeie frequências, locais e horários.

> **Caso sintético — Riverstone Transit.** Um teste de vazão proposto para o uplink da garagem teria usado 70% de um link de 10 Mb/s durante a janela de despacho da manhã. Sam o transferiu para 02:00–04:00 e o limitou a 1 Mb/s depois de calcular a carga de serialização.

### 3.4 Erros e limites

A física de guardanapo dá ordens de grandeza; links reais têm sobrecargas (cabeçalhos, retransmissões) que acrescentam de 5% a 20%. Não deduza a localização geográfica apenas pela latência; os caminhos de roteamento raramente são linhas retas. A sobrecarga de cabeçalhos e retransmissões faz com que um cálculo que a ignora subestime a carga. Usar a latência para adivinhar a localização falha quando o tráfego é roteado por um hub distante ou por uma VPN. Sam declara as suposições ao lado de cada estimativa e trata uma divergência em relação aos valores medidos como sinal para revisar o modelo, não como um achado sobre o alvo.

### Exercícios

- **EX007 — Piso de propagação.** Um relatório alega um tempo de ida e volta de 2 ms entre locais a 800 km de distância, por fibra. É plausível? Rubrica: 3 = piso ≈ 8 ms de ida e volta, portanto implausível, com uma causa provável (cache, local errado, proxy local); 2 = apenas o cálculo; 1 = palpite; 0 = nada.
- **EX008 — Fatia do link.** Que fração de um link de 2 Mb/s 500 sondas por segundo de 120 bytes usam? Rubrica: 3 = 0,48 Mb/s = 24%; 2 = um deslize de unidade; 1 = apenas o método; 0 = nada.
- **EX009 — Autorização de rádio.** Liste quatro campos que uma autorização escrita para uma avaliação de Wi-Fi precisa conter além de uma ROE de rede comum. Rubrica: 3 = frequências/bandas, locais físicos, horários e uma regra para dispositivos/dados de terceiros; 2 = três; 1 = um ou dois; 0 = nada.

### Síntese

A física define pisos e orçamentos. Usá-los pega evidências impossíveis e mantém o tráfego de teste dentro do que links e dispositivos frágeis aguentam.

### Continue estudando — capítulo 03 de 50

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever funções pequenas e testáveis para a contabilidade de uma avaliação; (2) escolher estruturas de dados que dificultem representar estados errados; (3) escrever um teste unitário antes de confiar na saída de uma ferramenta.

### 4.1 Funções que retornam decisões

As ferramentas de avaliação são, em grande parte, contabilidade: este alvo é permitido, qual achado é duplicado, qual a idade deste ticket. Cada pergunta deve ser uma função pura, com entradas explícitas e um valor de retorno, como `allowed(host, port, scope) -> (bool, reason)`. Retornar o *motivo* junto com a decisão torna os logs úteis: "DENY outside-cidr" diz ao revisor qual regra disparou. Evite estado global; uma função que lê um arquivo de escopo global escondido não pode ser testada contra um escopo sintético.

Uma função pura pode ser chamada por um teste unitário com um escopo falso e pela ferramenta em produção com o escopo real, e os dois caminhos compartilham a mesma lógica. Retornar uma string de motivo transforma cada negação numa explicação que o log do engajamento pode guardar. O estado global é inimigo desse padrão: se o escopo é lido de um arquivo dentro da função, um teste não consegue injetar um escopo sintético sem mexer no sistema de arquivos. Sam mantém o escopo como argumento em todos os pontos em que o TrackScope decide permitir ou negar.

### 4.2 Estruturas de dados que resistem a erros

Guarde as portas como um `set` de inteiros, não como uma string separada por vírgulas: a pertinência é exata, e "443" não pode casar com "4430". Guarde os CIDRs como objetos de rede já interpretados (o módulo padrão `ipaddress`), e não como strings, porque a comparação por prefixo de string acha que 10.200.0.5 está dentro de "10.20". Guarde os achados como dicionários com um esquema fixo e valide as chaves obrigatórias na criação. Tipos errados criam bugs silenciosos que parecem erros de escopo. Uma string de portas convida a uma comparação de substring; um conjunto de inteiros, não. Verificações de prefixo de string sobre endereços são uma armadilha clássica, e é por isso que existem os objetos de rede da biblioteca padrão. Validar os registros de achados na criação pega uma referência de ticket ausente antes de o relatório ser escrito, quando corrigi-la ainda custa segundos, e não uma correção constrangedora junto ao cliente.

### 4.3 Teste primeiro

Antes de usar um verificador de escopo numa rede de cliente, escreva cinco testes sobre dados sintéticos: um de permissão, um de negação para cada regra e um caso de fronteira (o primeiro e o último endereço de uma faixa). O laboratório do Capítulo 2 é exatamente uma tabela de decisões desse tipo; reproduzi-lo num teste unitário significa que uma refatoração posterior que quebre a lista de exclusão será pega antes de chegar a um engajamento real.

```python
import ipaddress
def in_scope(h, nets):
    a = ipaddress.ip_address(h)
    return any(a in ipaddress.ip_network(n) for n in nets)
assert in_scope("10.20.255.255", ["10.20.0.0/16"])
assert not in_scope("10.2.0.5", ["10.20.0.0/16"])
print("scope tests passed")
```

> **Caso sintético — Riverstone Transit.** Um script de estagiário comparava o escopo com `host.startswith("10.2")`. O teste de fronteira de Sam mostrou que ele aceitava 10.200.0.0/16, uma rede de parceiro. A correção usou `ipaddress`, e o teste agora roda na CI.

### 4.4 Erros e limites

Os testes provam o comportamento nos casos que você escreveu, não em todas as entradas. Mantenha os dados de teste sintéticos; nunca cole a lista real de hosts de um cliente num repositório público. Uma suíte que passa significa que os casos escritos se comportam; uma fronteira não testada ainda pode estar errada. Hosts sintéticos mantêm as redes dos clientes fora do histórico do git e fora das máquinas dos estudantes. Quando uma nova regra é acrescentada ao verificador de escopo, Sam acrescenta um teste para ela na mesma mudança, para que a suíte e as regras fiquem alinhadas.

### Exercícios

- **EX010 — Caça ao bug.** Explique por que `"443" in "8443,22"` é verdadeiro em Python e como corrigir a verificação de porta. Rubrica: 3 = semântica de substring explicada e correção com conjunto de inteiros; 2 = apenas a correção; 1 = vago; 0 = nada.
- **EX011 — Testes de fronteira.** Dê os dois endereços de fronteira a testar para 192.168.50.0/24 e o resultado esperado para 192.168.51.0. Rubrica: 3 = .0 e .255 dentro, 192.168.51.0 fora; 2 = um faltando; 1 = parcial; 0 = nada.
- **EX012 — Códigos de motivo.** Por que uma função de escopo deve retornar uma string de motivo, e não apenas um booleano? Rubrica: 3 = valor para auditoria/log e precisão dos testes, com um exemplo; 2 = um motivo; 1 = vago; 0 = nada.

### Síntese

Funções puras pequenas, tipos de dados exatos e testes escritos sobre dados sintéticos são o mecanismo de segurança de escopo mais barato que um engenheiro tem.

### Continue estudando — capítulo 04 de 50

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Comunicação de engenharia

### Objetivos de aprendizagem

Você vai (1) escrever um achado com o qual um não especialista consiga agir, sem detalhes de exploração; (2) estruturar um relatório curto de engenharia; (3) declarar a incerteza com clareza.

### 5.1 Quem lê decide

Um relatório de red team é lido por um engenheiro que precisa corrigir algo e por um gestor que precisa financiar a correção. Nenhum dos dois precisa de uma receita. Um achado precisa de: um título que declare a fraqueza e o ativo; o escopo afetado; a evidência (o que foi observado, com horário e referência de ticket); o impacto em termos de negócio; a correção recomendada; e como a correção será verificada. O NIST SP 800-115 trata o relatório como parte da avaliação, não como um detalhe posterior.

Colocar a correção e sua verificação ao lado da evidência significa que o engenheiro que precisa agir tem tudo numa única página. O impacto de negócio responde à pergunta de financiamento do gestor sem jargão técnico: trens atrasados, dados de passageiros expostos ou um risco de falsificação de bilhetes pesam de maneiras diferentes. Deixar de fora uma receita funcional não é imprecisão; é uma escolha deliberada para que o relatório possa ser repassado dentro do cliente sem virar um manual. O lugar que o NIST SP 800-115 dá ao relatório lembra às equipes que um achado não relatado não ajuda ninguém.

### 5.2 Escreva a alegação na força certa

"Comprometemos o domínio" é uma manchete. "Dentro da janela autorizada, uma conta de serviço no diretório do laboratório tinha direitos de administrador de domínio; confirmamos a participação no grupo apenas com leitura e não a usamos" é um achado. A segunda frase diz o que foi feito, o que não foi feito e em qual escopo, e o leitor pode verificá-la. A alegação mais fraca e cuidadosa é mais forte como engenharia, porque outra equipe pode conferi-la de novo. Declarar o que não foi feito fecha a brecha em que o leitor imagina um cenário pior do que o ocorrido. Nomear o escopo, como o diretório do laboratório e não a produção, impede que um achado seja aplicado ao sistema errado. Sam lê cada rascunho em voz alta e pergunta se cada substantivo aponta para algo no repositório de evidências.

### 5.3 Estrutura do relatório

Um relatório curto de engenharia tem: um sumário executivo (três frases: o que foi testado, o resultado mais importante e a única decisão necessária); escopo e método, com a versão da ROE; achados ordenados por prioridade; limitações (o que ficou fora do escopo ou não foi alcançado); e um apêndice com os hashes das evidências. Use tabelas para os achados e prosa para o raciocínio.

```python
"""Score synthetic findings for report priority (no exploit details)."""
# impact 0-3, exploitability 0-3, exposure 0-3  -> priority
findings = [
    ("SYN-001", "default admin password on staging web UI", 3, 3, 2),
    ("SYN-002", "missing security headers on public site", 1, 1, 3),
    ("SYN-003", "outdated TLS on internal admin port", 2, 2, 1),
    ("SYN-004", "verbose error messages disclose paths", 1, 2, 2),
    ("SYN-005", "service account with domain admin in lab AD", 3, 2, 1),
]

def priority(impact, exploitability, exposure):
    score = impact*4 + exploitability*2 + exposure
    if score >= 16: return "critical", score
    if score >= 11: return "high", score
    if score >= 7: return "medium", score
    return "low", score

for fid, title, i, e, x in findings:
    p, s = priority(i, e, x)
    print(f"{fid} priority={p:8} score={s:2} impact={i} exploitability={e} exposure={x} :: {title}")
```

Saída esperada:

```text
SYN-001 priority=critical score=20 impact=3 exploitability=3 exposure=2 :: default admin password on staging web UI
SYN-002 priority=medium   score= 9 impact=1 exploitability=1 exposure=3 :: missing security headers on public site
SYN-003 priority=high     score=13 impact=2 exploitability=2 exposure=1 :: outdated TLS on internal admin port
SYN-004 priority=medium   score=10 impact=1 exploitability=2 exposure=2 :: verbose error messages disclose paths
SYN-005 priority=critical score=17 impact=3 exploitability=2 exposure=1 :: service account with domain admin in lab AD
```

> **Caso sintético — Riverstone Transit.** O primeiro rascunho de Sam para o SYN-001 dizia "a UI de staging está totalmente dominada". O achado revisado diz: "A UI de administração de staging (10.20.1.10:443) aceita a senha padrão do fornecedor; observado às 10:45, ticket FD-118; um atacante na rede corporativa poderia alterar as tabelas de tarifas em staging; correção: trocar e exigir credenciais únicas; verificar por uma falha de login num reteste."

### 5.4 Erros e limites

Evite adjetivos que não possam ser verificados ("trivial", "catastrófico"). Não inclua payloads funcionais, credenciais ou instruções passo a passo nos relatórios; faça referência ao repositório de evidências. Adjetivos não verificáveis convidam à discussão e escondem a evidência real. Payloads funcionais e credenciais pertencem a um repositório controlado com logs de acesso, não a um PDF que vai circular por e-mail. Quando um leitor precisa de mais detalhes para verificar uma correção, Sam o direciona para o ticket e o hash da evidência, em vez de colar segredos no corpo do relatório.

### Exercícios

- **EX013 — Reescrita.** Reescreva "A VPN está escancarada kkk" como título de achado e uma linha de evidência de uma frase. Rubrica: 3 = ativo, fraqueza, horário/referência da observação, sem detalhes de exploração; 2 = falta um elemento; 1 = ainda vago; 0 = inalterado.
- **EX014 — Sumário executivo.** Escreva um sumário de três frases para os cinco achados do laboratório. Rubrica: 3 = escopo, os dois itens críticos, uma decisão solicitada; 2 = falta a decisão; 1 = só uma lista; 0 = nada.
- **EX015 — Limitações.** Cite duas limitações que um relatório deste engajamento precisa declarar. Rubrica: 3 = dois limites específicos (por exemplo, hosts não alcançados, janela de tempo, sem engenharia social) com efeito nas conclusões; 2 = dois sem efeito; 1 = um; 0 = nenhum.

### Síntese

Um bom achado é específico, verificável e seguro para circular. Escrevê-lo assim faz parte da engenharia, não é decoração.

### Continue estudando — capítulo 05 de 50

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar séries e acumulação para raciocinar sobre sondagens repetidas; (2) aplicar um modelo diferencial simples a um backlog de remediação; (3) decidir quando um modelo contínuo basta para um debate sobre a ROE.

### 6.1 Séries geométricas e novas tentativas

Se cada tentativa de enviar evidências tem sucesso com probabilidade p = 0,8, de forma independente, a chance de ter sucesso em até k tentativas é 1 − (1 − p)^k. Isso é uma série geométrica finita. Com k = 3, 1 − 0,2³ = 0,992. As novas tentativas elevam a taxa de sucesso, mas também multiplicam o tráfego: o número esperado de tentativas até o sucesso é 1/p = 1,25, então um lote de 1.000 envios espera 1.250 requisições. A ROE precisa contar as novas tentativas, não só os envios lógicos.

```python
"""Reliability of a synthetic evidence-upload step with retries (deterministic)."""
import random
random.seed(7)
P_FAIL = 0.2
def upload_attempts(max_tries):
    for t in range(1, max_tries + 1):
        if random.random() > P_FAIL:
            return True, t
    return False, max_tries
for tries in (1, 2, 3, 5):
    random.seed(7)
    ok = sum(upload_attempts(tries)[0] for _ in range(1000))
    print(f"max_tries={tries} success={ok}/1000 theory={1-P_FAIL**tries:.4f}")
```

Saída esperada:

```text
max_tries=1 success=784/1000 theory=0.8000
max_tries=2 success=949/1000 theory=0.9600
max_tries=3 success=988/1000 theory=0.9920
max_tries=5 success=1000/1000 theory=0.9997
```

Contar apenas os envios lógicos subestima a carga pelo fator de novas tentativas. Com p igual a 0,8, cada mil envios lógicos significam, em média, cerca de mil duzentas e cinquenta tentativas, e é isso que o limitador de taxa do cliente vai ver. A semente do laboratório mantém a demonstração estável entre máquinas; em produção, usa-se a mesma fórmula com taxas de falha medidas. Sam escreve o número esperado de tentativas no orçamento de volume da ROE antes do engajamento.

### 6.2 Modelo diferencial de um backlog

Seja B(t) o número de achados abertos. Os achados chegam à taxa a e são fechados à taxa c quando há equipe. Então B′(t) ≈ a − c. Se a = 4/dia e c = 6/dia, o backlog cai cerca de 2 por dia; partindo de 30, chega a zero em 15 dias. Se as chegadas saltam para 8/dia (uma semana de campanha) enquanto a equipe continua em 6, o backlog cresce. O modelo é grosseiro — ignora a prioridade —, mas torna quantitativa a decisão sobre a equipe. O sinal de a menos c conta a história num relance: negativo, a pilha encolhe; positivo, ela cresce. A prioridade continua importando nas filas reais, então Sam usa o modelo para pedir equipe, não para prometer uma data no calendário. Quando uma semana de campanha dobra as chegadas, o mesmo modelo mostra quantas pessoas a mais são necessárias para fechar tickets e manter o nível. Plotar B(t) ao longo de um mês torna o efeito visível para gestores que não vão ler a equação.

### 6.3 Quando o contínuo basta

Debates sobre a ROE costumam precisar de uma ordem de grandeza, não de uma forma fechada. "Uma varredura a 5 req/s por 30 minutos vai produzir cerca de 9.000 requisições?" Sim: 5 × 1.800 = 9.000. Reserve o cálculo exato para agendas com picos (§1) e para modelos que o cliente vai auditar. A aritmética de ordem de grandeza resolve a maioria dos debates sobre a ROE em minutos. Agendas exatas com picos precisam do tratamento mais completo do primeiro capítulo de cálculo, e são essas que Sam leva a um cliente que vai auditar os números. Para uma varredura plana, multiplicar a taxa pela duração basta, e escrever o produto ao lado do limite de volume mostra a conformidade num relance. Se o produto fica perto do limite, ele passa para a verificação da agenda exata em vez de torcer para que as rajadas fiquem pequenas.

> **Caso sintético — Riverstone Transit.** O FindingsDesk mostrava um backlog de 28 achados médios, com duas remediações por dia. O modelo B′ de Sam previu 14 dias para zerar se não houvesse novas chegadas; o gestor financiou um terceiro engenheiro para aquela quinzena.

### 6.4 Erros e limites

A independência das novas tentativas falha quando a falha é sistemática (um endpoint quebrado). Modelos de backlog ignoram prioridade e SLA; use-os para iniciar uma conversa, não como uma previsão que o conselho vai citar. Um endpoint quebrado falha em todas as tentativas, então multiplicá-las não eleva a taxa de sucesso e só acrescenta carga. Modelos de equipe que ignoram a severidade vão fechar os tickets fáceis enquanto os críticos envelhecem. Sam rotula cada modelo com suas premissas e não deixa que um gráfico de backlog seja citado como data de entrega.

### 6.3b Escolhendo um limite de tentativas a partir da série

A série geométrica dá a chance de todas as tentativas falharem como p elevado a n. Sam a usa de trás para frente: o envio de evidências do TrackScope precisa ter sucesso 99% das vezes, e execuções sintéticas mostram uma taxa de falha de 20% por tentativa; então três tentativas (0,8%) atingem a meta, enquanto duas (4%) não. Ele escreve a derivação na nota de design para que um revisor possa conferir o limite sem repetir os experimentos. Trabalhar de trás para frente a partir de uma meta de confiabilidade transforma uma questão de gosto numa derivação curta. Três tentativas deixam menos de um por cento de falha quando cada tentativa falha uma vez em cinco, o que bate com o laboratório. Pôr a derivação na nota de design significa que um engenheiro, mais tarde, pode mudar a taxa de falha e recalcular o limite sem adivinhar por que três foi o número escolhido. Sam repete a verificação sintética sempre que o caminho de envio muda.

### Exercícios

- **EX016 — Tráfego de novas tentativas.** Com p = 0,7 e um lote de 500 envios, quantas tentativas são esperadas até que cada um tenha sucesso uma vez? Rubrica: 3 = 500/0,7 ≈ 714 com o raciocínio; 2 = um deslize; 1 = só a fórmula; 0 = nada.
- **EX017 — Backlog.** B(0) = 40, a = 3/dia, c = 5/dia. Quando B chega a 0? Rubrica: 3 = 20 dias; 2 = método certo, aritmética errada; 1 = qualitativo; 0 = nada.
- **EX018 — Leitura do laboratório.** Pelo laboratório, em quantos pontos percentuais k = 3 melhora em relação a k = 1 com p = 0,8? Rubrica: 3 = 99,2 − 80,0 = 19,2 pontos (teoria) ou a diferença empírica 98,8 − 78,4 = 20,4 pontos; 2 = um número; 1 = vago; 0 = errado.

### Síntese

Séries e taxas transformam "tente de novo" e "contrate alguém" em números que cabem numa ROE ou num pedido de equipe.

### Continue estudando — capítulo 06 de 50

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) relatar uma taxa com um intervalo, não como uma porcentagem solta; (2) aplicar a regra de Bayes à precisão de alarmes; (3) recusar uma classificação que a amostra não sustenta.

### 7.1 Taxas e intervalos de Wilson

Três sucessos em vinte tentativas são 15%. Um intervalo de Wilson de 95% para isso vai de cerca de 5% a 36%. Você pode dizer que a taxa provavelmente não é zero e provavelmente fica abaixo de 40%; não pode dizer que ela é melhor que uma defesa que marcou 20/100 (20%). Um n maior estreita o intervalo: 300/2.000 continua sendo 15%, mas fica entre cerca de 13,5% e 16,6%. Albrecht e Jensen alertam contra pontuações únicas vazias; um intervalo é a honestidade mais barata.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Saída esperada:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

Os mesmos quinze por cento significam coisas muito diferentes com n igual a vinte e com n igual a dois mil. Um intervalo torna isso visível sem uma aula de estatística. Sam relata o intervalo ao lado de cada taxa de sucesso de ataque, para que nenhuma defesa seja coroada com base numa amostra minúscula. A variação de sementes e o bootstrap pareado do laboratório oferecem mais duas verificações: estabilidade entre sementes e uma diferença que pode incluir zero.

### 7.2 Taxas de base e precisão

Um detector com 95% de taxa de verdadeiros positivos e 5% de taxa de falsos positivos parece excelente até que a taxa de base da classe ruim seja 0,1%. Então quase todo alerta é um falso positivo (precisão ≈ 1,9%). Regra de Bayes: precisão = TPR·π / (TPR·π + FPR·(1−π)). O PulseMap precisa mostrar a precisão na taxa de base do cliente, não só a TPR.

```python
"""Lab B: base rates and alarm precision (Bayes' rule).
A detector for malicious prompts with given true- and false-positive rates
is applied to traffic with different shares of malicious prompts."""
for tpr, fpr in ((0.95, 0.05), (0.95, 0.01), (0.80, 0.001)):
    for prev in (0.10, 0.01, 0.001):
        tp = tpr * prev; fp = fpr * (1 - prev)
        prec = tp / (tp + fp)
        per_10k = round(10000 * (tp + fp))
        print(f"tpr={tpr:.2f} fpr={fpr:.3f} prevalence={prev:.3f} precision={prec:.3f} alerts_per_10k={per_10k}")
```

Saída esperada:

```text
tpr=0.95 fpr=0.050 prevalence=0.100 precision=0.679 alerts_per_10k=1400
tpr=0.95 fpr=0.050 prevalence=0.010 precision=0.161 alerts_per_10k=590
tpr=0.95 fpr=0.050 prevalence=0.001 precision=0.019 alerts_per_10k=509
tpr=0.95 fpr=0.010 prevalence=0.100 precision=0.913 alerts_per_10k=1040
tpr=0.95 fpr=0.010 prevalence=0.010 precision=0.490 alerts_per_10k=194
tpr=0.95 fpr=0.010 prevalence=0.001 precision=0.087 alerts_per_10k=109
tpr=0.80 fpr=0.001 prevalence=0.100 precision=0.989 alerts_per_10k=809
tpr=0.80 fpr=0.001 prevalence=0.010 precision=0.890 alerts_per_10k=90
tpr=0.80 fpr=0.001 prevalence=0.001 precision=0.445 alerts_per_10k=18
```

A precisão despenca quando a classe ruim é rara, que é exatamente o cenário do PulseMap. Um painel que mostra só a taxa de verdadeiros positivos parecerá excelente enquanto inunda os analistas de alarmes falsos. Calcular a precisão na prevalência medida do cliente, como faz a tabela do laboratório, é o que Sam coloca no relatório. Se a prevalência é desconhecida, ele mostra uma pequena tabela com uma faixa de valores em vez de escolher um número lisonjeiro.

### 7.3 Classificando defesas

Duas defesas com intervalos sobrepostos não são classificadas. Prefira um desenho pareado, com os mesmos prompts, e um bootstrap da diferença, como mostra o laboratório. Se o intervalo da diferença incluir zero, relate "nenhuma diferença significativa nesta amostra", não um vencedor.

> **Caso sintético — Riverstone Transit.** Um fornecedor afirmou que "nosso filtro é 99% eficaz". Sam pediu a taxa de base e o tamanho da amostra; nenhum dos dois estava no folheto. O piloto usou 200 prompts sintéticos com 1% de ataques e mediu precisão ≈ 16%.

### 7.4 Erros e limites

A independência das tentativas falha quando os prompts compartilham um modelo de texto. Os intervalos pressupõem um processo fixo; trocar o modelo no meio do teste os invalida. Nunca invente um valor-p para uma tabela que você não testou. Modelos de texto compartilhados tornam as tentativas dependentes, então intervalos que pressupõem independência ficam estreitos demais. Trocar o modelo no meio do teste mistura dois processos e invalida a amostra. Sam nunca anexa uma alegação de significância a uma tabela que não foi testada para isso, e reinicia a amostra quando a defesa sob teste muda.

### 7.3b Comunicando incerteza a quem não é estatístico

Uma taxa de detecção de 7 em 10 e uma de 700 em 1.000 imprimem a mesma porcentagem, mas merecem confianças muito diferentes. Quando Sam relata a cobertura do PulseMap ao gestor de segurança da Riverstone Transit, ele informa a contagem, o intervalo e uma frase simples: "vimos sete de dez eventos de teste; a taxa real poderia plausivelmente estar em qualquer ponto entre cerca de 40% e 90%". Os gestores então pedem mais tentativas, em vez de tratar uma amostra pequena como um fato, e a classificação das defesas espera até que os intervalos deixem de se sobrepor.

### Exercícios

- **EX019 — Intervalo.** Diga o que você pode afirmar a partir de 8/40 sucessos com 95%. Rubrica: 3 = Wilson ≈ 10,5%–34,5% (ou Clopper–Pearson), não é possível classificar contra 25%; 2 = só o intervalo; 1 = estimativa pontual; 0 = errado.
- **EX020 — Precisão.** Detector com TPR 0,9, FPR 0,02, π = 0,005. Qual a precisão? Rubrica: 3 ≈ 0,184 com o raciocínio; 2 = um deslize; 1 = fórmula; 0 = nada.
- **EX021 — Recusa de classificação.** Dois filtros marcam 12/100 e 18/100. Escreva a frase que recusa uma classificação. Rubrica: 3 = cita incerteza sobreposta / necessidade de desenho pareado; 2 = cautela vaga; 1 = escolhe um vencedor; 0 = nada.

### Síntese

A estatística é a linguagem para não exagerar nas alegações. Taxas com intervalos e precisão na taxa de base real mantêm o PulseMap honesto.

### Continue estudando — capítulo 07 de 50

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) mapear os níveis de privilégio para o que um teste autorizado pode observar; (2) explicar por que canais laterais de tempo e de cache precisam de cláusulas especiais na ROE; (3) desenhar um caminho de evidências que não exija privilégios de kernel.

### 8.1 Privilégio e observabilidade

O modo usuário vê a memória do processo e as chamadas de sistema que lhe são permitidas; o modo kernel vê dispositivos e tabelas de páginas; um hipervisor vê os convidados. Um engajamento autorizado que permanece em modo usuário não pode afirmar que "descartamos um rootkit de kernel". Declare o nível de privilégio de cada observação no pacote de evidências. O TrackScope deve registrar a conta e o papel usados em cada ação. Um achado é tão forte quanto o ponto de observação que o produziu. Evidências em modo usuário não conseguem descartar ameaças que vivem abaixo dele, e afirmar o contrário vende o engajamento por mais do que ele é. Registrar a conta e o papel ao lado de cada ação permite que um revisor veja se uma alegação posterior corresponde ao acesso usado. O TrackScope se recusa a guardar uma observação sem esse campo.

### 8.2 Canais laterais são físicos

Canais laterais de cache e de tempo medem o estado microarquitetural. São técnicas de pesquisa, ruidosas e muitas vezes fora do escopo de avaliações comerciais. Se estiverem no escopo, a ROE precisa nomear as plataformas, proibir tráfego de produção e exigir uma condição de parada caso a latência para os usuários suba. Não trate um laboratório de estudante num notebook como evidência sobre um servidor. Essas técnicas medem o estado de hardware compartilhado e podem perturbar a latência de produção, e é por isso que precisam de cláusulas próprias na ROE. Um laboratório num notebook não diz nada sobre o comportamento de cache de um servidor sob carga. Quando os canais laterais estão fora do escopo, Sam declara esse limite no relatório para que os leitores não presumam que foram tentados. As condições de parada protegem usuários que nunca concordaram em fazer parte do experimento.

### 8.3 Evidência sem root

A maior parte das evidências duráveis de uma avaliação autorizada são logs, leituras de configuração e respostas de aplicação — tudo disponível para uma conta de usuário devidamente autorizada. Prefira esse caminho: é mais seguro, mais fácil de revogar depois do engajamento e suficiente para achados sobre autenticação, autorização e exposição.

> **Caso sintético — Riverstone Transit.** Uma proposta de "imagem completa de disco" de um validador de tarifas precisava de root e tiraria o dispositivo do ar. Sam a substituiu por uma exportação de configuração e uma leitura, no nível da aplicação, da lista de contas, ambas autorizadas pela ROE existente.

### 8.4 Erros e limites

Diagramas de arquitetura em apresentações de marketing omitem caches compartilhados e planos de gerenciamento. Verifique a plataforma real antes de prometer um nível de privilégio na ROE. Diagramas de marketing muitas vezes escondem interfaces de gerenciamento e hardware compartilhado. Sam confirma a plataforma real com o cliente antes que a ROE prometa um nível de privilégio. Se a plataforma não puder ser confirmada, o engajamento fica no menor privilégio cuja existência é conhecida, e o relatório declara esse limite para que os leitores não inventem um ponto de observação mais forte.

### 8.3b Privilégio nos tickets

O FindingsDesk deve guardar `privilege_used` como um enum (user, admin-local, admin-domain, hypervisor, out-of-band). A ordenação e a lógica de SLA podem então tratar achados de hipervisor de forma diferente de leituras de configuração em modo usuário. Sem o campo, dois achados com títulos parecidos podem ter sido obtidos sob autorizações radicalmente diferentes, e o plano de reteste estará errado. Um enum impede a deriva do texto livre, como 'admin' significar local num ticket e domínio em outro. Os relógios de SLA podem então dar aos achados de hipervisor um caminho diferente, porque verificá-los exige outro acesso e outras condições de parada. Os planos de reteste leem o campo para que quem faz o reteste leve a autorização certa. O FindingsDesk rejeita um ticket que o omita.

### Exercícios

- **EX022 — Mapa de privilégios.** Liste três observações possíveis como usuário comum e três que exigem privilégios elevados. Rubrica: 3 = seis itens concretos mapeados corretamente; 2 = quatro; 1 = vago; 0 = nada.
- **EX023 — ROE de canal lateral.** Escreva duas cláusulas de ROE para um estudo autorizado de tempo de cache num host de laboratório reserva. Rubrica: 3 = plataforma nomeada, produção excluída, condição de parada; 2 = dois de três; 1 = um; 0 = nada.
- **EX024 — Caminho de evidência.** Proponha um caminho de evidência para "senha de administrador padrão na UI de staging" que não precise de root. Rubrica: 3 = tentativa de login sob a ROE, captura de tela/log, ticket, nenhuma credencial deixada para trás; 2 = falta um; 1 = vago; 0 = exige root.

### Síntese

Diga qual privilégio você usou. Prefira evidências de nível de usuário. Trate canais laterais como algo especial, não como uma ferramenta padrão.

### Continue estudando — capítulo 08 de 50

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) desenhar um esquema de achados que proíba receitas de exploração; (2) implementar atualizações idempotentes; (3) usar testes de propriedade para regras de escopo.

### 9.1 Esquemas sem payloads

O FindingsDesk guarda título, ativo, classe de fraqueza, referência de evidência, impacto, status e carimbos de tempo. Ele não pode guardar um exploit funcional, uma credencial ativa nem um ataque passo a passo. A validação do esquema rejeita campos chamados `payload`, `password` ou `shell`. As evidências ficam num repositório lacrado, referenciado por hash (Capítulo 48). Rejeitar esses nomes de campo na entrada impede que um engenheiro bem-intencionado cole uma senha num ticket durante um encerramento corrido. Evidência por hash significa que o ticket continua compartilhável enquanto o repositório lacrado continua trancado. Sam avalia cada proposta de nova coluna pela mesma regra: se ela puder conter uma receita ou um segredo, não pertence ao FindingsDesk.

### 9.2 Atualizações idempotentes

Fechar um achado duas vezes precisa deixá-lo fechado; anexar o mesmo hash de evidência duas vezes precisa deixar um único anexo. A idempotência torna seguras as novas tentativas (Capítulo 6). Use um id de achado estável e trate criar-ou-atualizar como uma única operação indexada por esse id.

```python
"""Deduplicate synthetic findings by a stable fingerprint (asset, weakness class, location)."""
import hashlib
raw = [
    ("web-01", "missing-header", "/login"),
    ("web-01", "missing-header", "/login"),
    ("web-01", "missing-header", "/account"),
    ("web-02", "default-credential", "admin-ui"),
    ("web-02", "default-credential", "admin-ui"),
    ("db-01", "weak-tls", "5432"),
]
seen = {}
for asset, cls, loc in raw:
    fp = hashlib.sha256(f"{asset}|{cls}|{loc}".encode()).hexdigest()[:10]
    seen.setdefault(fp, [asset, cls, loc, 0])[3] += 1
print(f"raw={len(raw)} unique={len(seen)}")
for fp, (a, c, l, n) in sorted(seen.items(), key=lambda x: x[1]):
    print(f"{fp} {a:7} {c:19} {l:9} occurrences={n}")
```

Saída esperada:

```text
raw=6 unique=4
f9bb6de442 db-01   weak-tls            5432      occurrences=1
66fb6f1d56 web-01  missing-header      /account  occurrences=1
c4bfba3b72 web-01  missing-header      /login    occurrences=2
296a3331f0 web-02  default-credential  admin-ui  occurrences=2
```

Novas tentativas são normais quando os envios falham e, sem idempotência, cada uma reabriria trabalho ou criaria tickets duplicados. Um id estável transforma criação e atualização no mesmo caminho, de modo que a segunda chamada encontra a linha existente. A impressão digital do laboratório reduz seis linhas brutas a quatro achados únicos, que é o que os responsáveis pela remediação querem ver.

### 9.3 Testes de propriedade

Além dos testes por exemplo, declare uma propriedade: "para todo host na lista de exclusão e toda porta, allowed é False". Gere dezenas de hosts sintéticos e afirme a propriedade. Testes de propriedade pegam o bug em que uma entrada da lista de exclusão é ignorada para portas fora de uma lista fixa no código.

> **Caso sintético — Riverstone Transit.** A deduplicação de seis linhas brutas deixou quatro achados únicos; as duas duplicatas eram o mesmo cabeçalho ausente em /login, relatado por dois scanners. Sam fez da impressão digital (ativo, fraqueza, local) a chave de idempotência.

### 9.4 Erros e limites

Esquemas derivam; versione-os. Testes de propriedade são tão bons quanto o gerador; inclua à mão os casos de borda conhecidos. Um esquema sem campo de versão obriga os clientes a adivinhar quais campos existem. Geradores que nunca emitem o último endereço de uma faixa nunca vão pegar um bug ali. Sam mantém uma pequena tabela, escrita à mão, de casos traiçoeiros ao lado da suíte de propriedades e roda as duas a cada mudança. Um bug no gerador é tratado como um bug de produto: corrija-o antes do próximo engajamento.

### 9.2b Migração sem indisponibilidade

Quando o esquema de achados ganha um campo obrigatório, implante uma mudança em duas fases: primeiro aceite e persista o campo como opcional enquanto preenche os registros antigos; depois mude o validador para obrigatório. Engajamentos no meio da janela não podem quebrar porque um cliente móvel está uma versão atrás. Publique a versão do esquema nas respostas da API para que os clientes possam se recusar a escrever quando forem incompatíveis. Mudanças em duas fases mantêm a escrita segura para clientes no meio de um engajamento. O preenchimento retroativo completa as linhas antigas antes de o campo se tornar obrigatório, para que os validadores não rejeitem tickets históricos. Publicar a versão do esquema permite que um cliente móvel recuse uma escrita incompatível em vez de corromper um achado. Sam ensaia a virada numa cópia de staging, com um fixture de engajamento ativo, antes de tocar a produção.

### 9.1b Chaves de idempotência a partir de impressões digitais

Quando dois scanners relatam a mesma fraqueza, calcule primeiro a impressão digital e use-a para gerar ou localizar o id do achado antes da inserção. Pessoas ainda confirmam as fusões quando as impressões digitais colidem entre causas-raiz diferentes (o mesmo cabeçalho ausente em duas aplicações sem relação). Registre os ids dos scanners como referências de evidência, não como achados separados, para que a remediação acompanhe um único ticket. Os scanners discordam na redação, mas costumam concordar em ativo, classe e local, o que basta para uma impressão digital. Colisões entre aplicações sem relação são raras e exigem uma fusão humana, que sai mais barata que dezenas de tickets duplicados. Guardar os ids dos scanners como evidência preserva a proveniência sem multiplicar o backlog. Sam mostra a impressão digital no ticket para que os responsáveis vejam por que dois alertas viraram um.

### Exercícios

- **EX025 — Rejeição pelo esquema.** Escreva uma regra de validação que rejeite um achado contendo um campo cujo nome case com `(?i)payload|password|passwd|shell`. Rubrica: 3 = regra mais um exemplo que falha; 2 = só a regra; 1 = ideia; 0 = nada.
- **EX026 — Impressão digital.** Pelo laboratório, por que duas linhas de /login se fundem e duas de /account não? Rubrica: 3 = mesma impressão digital vs. local diferente; 2 = "mesmo achado"; 1 = vago; 0 = errado.
- **EX027 — Propriedade.** Declare uma propriedade de `allowed` que precisa valer depois de qualquer acréscimo à lista de exclusão. Rubrica: 3 = encolhimento monotônico / todo host excluído sempre negado; 2 = informal; 1 = propriedade errada; 0 = nada.

### Síntese

Esquemas, idempotência e propriedades tornam o software de avaliação entediante no bom sentido: previsível sob novas tentativas e revisões.

### Continue estudando — capítulo 09 de 50

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) recusar pedidos de uso dual e fora do escopo; (2) aplicar condições de parada sem esperar por uma reunião; (3) documentar consentimento e autorização para que uma revisão possa reconstruí-los.

### 10.1 Autorização não é entusiasmo

Um gestor dizendo "pode ir" no chat não é autorização por escrito. O NIST SP 800-115 e o PTES esperam um escopo assinado, com métodos, datas, limites, contatos e condições de parada. Sem esse documento, o engenheiro para. O entusiasmo de uma única parte interessada que não é dona do ativo é um caminho comum para testes não autorizados. Mensagens de chat desaparecem, carecem de detalhes de escopo e raramente nomeiam condições de parada. Um documento assinado pode ser mostrado meses depois, quando alguém perguntar por que um host foi tocado. Parar sem esse documento não é teimosia; é a única atitude que mantém o engenheiro e o cliente dentro da lei. Sam guarda o hash da ROE assinada no TrackScope, ao lado de cada execução.

### 10.2 Uso dual e ensino

Este livro ensina escopo, medição e relatório. Não ensina desenvolvimento de exploits, payloads transformados em armas nem receitas de evasão. Quando um colega pede "só a PoC", a resposta é a descrição do achado e a referência da evidência, não um ataque funcional. Publicar trabalhos de estudantes que contenham técnicas ativas contra produtos reais é uma decisão de divulgação que envolve fornecedores e a lei, não o envio de uma lição de casa. A recusa protege colegas, futuros empregadores e fornecedores que nunca concordaram em ser alvo de lição de casa. Uma descrição do achado com uma referência de evidência permite que um colega aprenda o que estava errado sem receber um ataque pronto. Quando um trabalho do curso pode tocar um produto real, Sam o encaminha pelo mesmo caminho de divulgação que um engajamento profissional usaria. Os laboratórios do curso ficam em sistemas sintéticos por esse motivo.

### 10.3 Condições de parada

Condições de parada são gatilhos combinados de antemão: sondar um host da lista de exclusão, latência acima de um limiar, um alarme de segurança ou um pedido do contato do cliente. Quando um gatilho dispara, primeiro pare, depois notifique. O TrackScope deve impor as negações rígidas em software, para que "eu esqueci" não seja um modo de falha.

```python
"""Evaluate proposed actions against synthetic rules of engagement."""
ROE = {
    "hours": ("09:00", "17:00"),
    "deny_actions": {"denial-of-service", "phishing-staff", "exfiltrate-real-data"},
    "require_approval": {"password-spray-lab", "privilege-escalation-lab"},
    "max_concurrency": 5,
}
proposals = [
    ("service-enum", "10:30", 3, False),
    ("denial-of-service", "10:30", 1, False),
    ("password-spray-lab", "10:30", 2, False),
    ("password-spray-lab", "10:30", 2, True),
    ("service-enum", "18:00", 2, False),
    ("service-enum", "11:00", 20, False),
]

def ok_time(t):
    return ROE["hours"][0] <= t <= ROE["hours"][1]

for action, when, conc, approved in proposals:
    reasons=[]
    if action in ROE["deny_actions"]: reasons.append("deny-action")
    if action in ROE["require_approval"] and not approved: reasons.append("needs-approval")
    if not ok_time(when): reasons.append("outside-hours")
    if conc > ROE["max_concurrency"]: reasons.append("concurrency")
    print(f"action={action:20} when={when} conc={conc:2} approved={approved} -> {'ALLOW' if not reasons else 'DENY'} {','.join(reasons) or '-'}")
```

Saída esperada:

```text
action=service-enum         when=10:30 conc= 3 approved=False -> ALLOW -
action=denial-of-service    when=10:30 conc= 1 approved=False -> DENY deny-action
action=password-spray-lab   when=10:30 conc= 2 approved=False -> DENY needs-approval
action=password-spray-lab   when=10:30 conc= 2 approved=True -> ALLOW -
action=service-enum         when=18:00 conc= 2 approved=False -> DENY outside-hours
action=service-enum         when=11:00 conc=20 approved=False -> DENY concurrency
```

> **Caso sintético — Riverstone Transit.** Às 11:10 a varredura tocou 10.20.0.1 (na lista de exclusão). O TrackScope negou as ações seguintes; Sam escalou; o cliente confirmou. A retomada exigiu uma linha atualizada na ROE, não um "tudo bem" verbal.

O laboratório mostra negações para ações proibidas, aprovação ausente, horário errado e concorrência excessiva. A imposição em software significa que a parada acontece mesmo que a pessoa esteja cansada ou distraída. Notifique depois de parar, não antes, para que a ação danosa não continue enquanto alguém procura um horário para reunião. Sam testa o caminho de negação em staging com uma ação proibida deliberada antes de cada engajamento.

### 10.4 Erros e limites

Ética não é um capítulo que se termina; é uma restrição sobre todos os capítulos seguintes. O texto jurídico aqui é orientação, não aconselhamento — consulte a assessoria jurídica em engajamentos reais. Os capítulos posteriores sobre ferramentas e métodos herdam esses limites; nenhum deles se sobrepõe a uma ROE ausente. Um texto de orientação não substitui a assessoria jurídica quando há um contrato real na mesa. Sam escala as questões jurídicas em vez de inventar respostas a partir de um parágrafo de livro, e revisita o consentimento quando o escopo muda no meio do engajamento, antes de qualquer nova ação rodar.

### 10.3b Controle duplo para verbos perigosos

Ações que mudam a autorização — publicar uma nova ScopeVersion, desativar uma condição de parada, exportar um dossiê lacrado — exigem duas pessoas autenticadas ou um controle individual com atraso e janela de cancelamento. A conveniência de engenharia não é argumento contra o controle duplo quando o raio de impacto é o patrimônio do cliente. Um único engenheiro cansado não deveria conseguir ampliar o escopo de um ambiente inteiro. Uma segunda pessoa, ou um atraso que permita cancelar, transforma um erro num evento recuperável. Publicar uma nova ScopeVersion e exportar um dossiê lacrado mudam quem pode ver o quê, e é por isso que ambos estão na lista de controle duplo. Sam registra os dois aprovadores em cada uma dessas ações.

### Exercícios

- **EX028 — Recuse.** Escreva uma recusa de duas frases a um pedido de exploit funcional contra um produto de fornecedor para um trabalho avaliado. Rubrica: 3 = recusa, oferece alternativa permitida (texto do achado / laboratório sintético), cita segurança; 2 = recusa sem alternativa; 1 = vago; 0 = fornece o exploit.
- **EX029 — Pare.** Pelo laboratório, quais ações são negadas e por quê? Rubrica: 3 = DoS sempre; password spraying sem aprovação; fora do horário; concorrência; 2 = três; 1 = um; 0 = errado.
- **EX030 — Campos de autorização.** Liste seis campos que uma ROE assinada precisa conter. Rubrica: 3 = sistemas, métodos, datas, limites de taxa/dados, contatos, condições de parada (ou seis equivalentes); 2 = quatro; 1 = dois; 0 = nada.

### Síntese

Permissão por escrito, condições de parada e o hábito de recusar são engenharia de segurança, não burocracia.

### Continue estudando — capítulo 10 de 50

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) descrever o que um observador autorizado pode aprender em cada camada OSI sem atacá-la; (2) definir com precisão o escopo de portas e protocolos; (3) interpretar uma negação como um controle bem-sucedido, não como um teste fracassado.

### 11.1 Camadas como pontos de observação

Capturas na camada de enlace exigem acesso a um segmento; dados de roteamento da camada de rede exigem um ponto de observação; evidências da camada de aplicação muitas vezes exigem credenciais. Uma avaliação que só tem credenciais de aplicação não deve alegar visibilidade da camada de enlace. Declare o ponto de observação na seção de método. Credenciais de uma aplicação não dizem nada sobre os quadros que passam no fio. Alegar um ponto de observação mais amplo do que o que você tinha é inventar cobertura. Nomear a camada na descrição do método permite que um revisor associe cada achado ao que de fato podia ser visto. Sam se recusa a registrar alegações sobre a camada de enlace quando o engajamento só tinha uma conta de aplicação.

### 11.2 Portas não são serviços

A porta 443 costuma significar TLS e HTTPS, mas pode transportar outros protocolos. Um escopo que diz "portas web" precisa listar números e, se necessário, os protocolos de aplicação esperados. Um achado de que "o HTTPS estava aberto" fica incompleto sem o titular do certificado, o método de autenticação e a confirmação de que o serviço era o esperado. Listar os números das portas tira da ROE a expressão nebulosa "portas web". Confirmar o titular do certificado e o método de autenticação evita um achado que confunda outro serviço na 443 com o portal esperado. As anotações de Sam sempre incluem qual protocolo foi observado, não só que a porta respondeu.

### 11.3 Negações são dados

Uma porta fechada, um handshake TCP recusado ou um bloqueio de WAF é evidência de que um controle funcionou para aquela sondagem. Relate isso como cobertura de uma verificação planejada, não como uma falha em "entrar". A distinção entre coberto e planejado-mas-não-visto do PulseMap (Capítulo 29) depende disso.

```python
"""Rank synthetic assets for authorized engagement scoping."""
assets = [
    ("public-web-portal", 3, 3, 3),      # exposure, data_sensitivity, blast_radius 1-3
    ("staging-admin-ui", 2, 3, 2),
    ("corp-vpn-edge", 3, 2, 3),
    ("internal-wiki", 1, 2, 1),
    ("printer-fleet", 2, 1, 1),
    ("lab-jump-host", 1, 1, 2),
]
print(f"{'asset':20} score exposure data blast")
for name, e, d, b in sorted(assets, key=lambda x: -(x[1]+x[2]+x[3])):
    print(f"{name:20} {e+d+b:5} {e:8} {d:4} {b:5}")
```

Saída esperada:

```text
asset                score exposure data blast
public-web-portal        9        3    3     3
corp-vpn-edge            8        3    2     3
staging-admin-ui         7        2    3     2
internal-wiki            4        1    2     1
printer-fleet            4        2    1     1
lab-jump-host            4        1    1     2
```

> **Caso sintético — Riverstone Transit.** O inventário classificou public-web-portal no topo (pontuação 9). Sam o agendou primeiro, conforme a ROE, e adiou printer-fleet, que teve pontuação 4 e estava fora da janela da semana.

As métricas de cobertura ficam honestas quando um bloqueio conta como uma verificação concluída. Perseguir só os caminhos abertos enviesa o relatório para a falha e esconde controles que funcionaram. O balde planejado-mas-não-visto do PulseMap existe para que uma negação silenciosa ainda seja registrada. Sam lista as sondagens bloqueadas ao lado das bem-sucedidas no resumo diário.

### 11.4 Erros e limites

Scanners identificam produtos pelos banners; banners mentem. Confirme com uma verificação no nível da aplicação antes de escrever um achado. Não faça varreduras na Internet pública a partir do ambiente do curso. Um banner que declara a versão de um produto pode ter sido copiado de um modelo ou ter ficado desatualizado depois de uma atualização. Uma verificação no nível da aplicação, como ler uma página de saúde mediante autorização, confirma o que de fato está lá. Os ambientes do curso ficam fora da Internet pública para que os estudantes nunca se tornem um scanner indesejado na rede de outra pessoa. As máquinas de laboratório de Sam não têm rota para lá.

### 11.3b Famílias de protocolos no escopo

Documentos de escopo devem nomear explicitamente as famílias de protocolos: "TCP 443 com dados de aplicação HTTPS" é mais claro que "443". Se a interceptação de TLS for proibida, diga isso. Se apenas TLS 1.2+ puder ser testado, diga isso. A ambiguidade aqui vira discussão durante o engajamento, quando alguém quer tentar uma porta legada em texto claro "só para ver". Nomear HTTPS na TCP 443 não deixa espaço para um experimento em texto claro no mesmo número. Proibir de antemão a interceptação de TLS evita uma discussão no meio do teste com as equipes de privacidade e jurídica. Portas legadas em texto claro ficam fechadas, a menos que a ROE as liste. Sam lê o parágrafo de protocolos em voz alta com o contato do cliente antes do kickoff.

### 11.4b Capturando só o que a ROE permite

Capturas de pacotes feitas durante um teste autorizado muitas vezes contêm dados fora do propósito do engajamento, como credenciais de funcionários ou registros de passageiros, no caso da Riverstone Transit. O plano de captura de Sam nomeia as interfaces, um filtro limitado aos hosts em escopo, um período de retenção e quem pode abrir os arquivos, e a captura é apagada no prazo. Filtros e retenção curta reduzem quantos dados de funcionários ou passageiros podem permanecer depois do teste. Nomear quem pode abrir os arquivos impede a navegação casual por uma captura que por acaso incluiu um login. A exclusão no prazo é verificada, não presumida. O encerramento de Sam inclui um ticket mostrando que a captura foi apagada.

### Exercícios

- **EX031 — Ponto de observação.** Associe três tipos de evidência ao ponto de observação mínimo necessário. Rubrica: 3 = associação correta (por exemplo, tabela ARP → acesso ao enlace; certificado TLS → TCP até a porta; campo de API → sessão autenticada); 2 = dois; 1 = um; 0 = nada.
- **EX032 — Portas do escopo.** Reescreva "todas as coisas web" como um conjunto de portas e uma nota de aplicação para a Riverstone. Rubrica: 3 = {80,443,8080} mais "só HTTP(S) para as aplicações de tarifas e de funcionários"; 2 = só as portas; 1 = vago; 0 = nada.
- **EX033 — Inventário.** Quais dois ativos do laboratório você agendaria primeiro, e por quê? Rubrica: 3 = public-web-portal e corp-vpn-edge, com motivos de pontuação/exposição; 2 = corretos sem motivos; 1 = um; 0 = errado.

### Síntese

As redes dão a você um ponto de observação e um conjunto de portas. Delimite-os no escopo; trate os bloqueios como resultados.

### Continue estudando — capítulo 11 de 50

[← Capítulo 10 (rascunho)](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 (rascunho) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) separar a revisão de configuração do abuso em tempo de execução; (2) coletar evidências do sistema operacional com privilégio mínimo; (3) registrar o uso de contas para que a revogação seja possível.

### 12.1 Configuração geralmente basta

Política de senhas, nível de patches, serviços em escuta e participação no grupo de administradores locais respondem à maioria das perguntas sobre o sistema operacional numa avaliação autorizada. Ler esses dados com uma conta de administrador concedida para o engajamento é diferente de explorar um serviço para obter essa conta. Prefira a primeira opção; uma descoberta no estilo do PTES fica dentro dos métodos combinados. Leituras com uma conta de administrador concedida respondem ao nível de patches e à participação em grupos locais sem transformar o engajamento numa caça a um ponto de apoio. Essa distinção importa para a ética e para a clareza da remediação: um achado obtido com uma conta concedida trata de exposição e política, não de um caminho de invasão. Sam registra que a conta foi emitida para o teste, para que os leitores não deduzam um acesso furtivo.

### 12.2 Privilégio mínimo para quem testa

Emita uma conta de avaliação nominal, com um papel limitado no tempo. Registre toda elevação. Ao fim do engajamento, desative a conta e troque quaisquer segredos compartilhados que ela tenha tocado. O FindingsDesk deve guardar o id da conta usada em cada achado, para que a revogação possa ser verificada. Uma conta nominal e limitada no tempo pode ser desativada sem caçar senhas compartilhadas. Registrar as elevações torna direitos incomuns visíveis durante o engajamento, não só depois. Guardar o id da conta em cada achado torna mecânica a lista de verificação da revogação. O encerramento de Sam falha se algum achado ainda apontar para uma conta de teste ativa.

### 12.3 Local vs. domínio

Um administrador local num host não é administrador de domínio. Os achados precisam nomear o repositório de identidades (SAM local, LDAP, IdP de nuvem). Confundi-los infla a severidade e direciona mal a remediação. A remediação para um administrador local é o endurecimento do host; a remediação para um administrador de domínio é trabalho no repositório de identidades. Misturar os rótulos manda a equipe errada, com a urgência errada. Provedores de identidade na nuvem acrescentam um terceiro repositório, que precisa ser nomeado explicitamente. O modelo de achado de Sam exige o campo de repositório de identidades antes que um ticket saia do rascunho.

> **Caso sintético — Riverstone Transit.** O SYN-005 era uma conta de serviço do laboratório com direitos de administrador de domínio — um achado de diretório, não um achado de "o Windows está quebrado". A remediação significou remover a participação no grupo e trocar a senha, verificando depois com uma leitura do grupo.

### 12.4 Erros e limites

Os fornecedores de sistemas operacionais mudam os padrões; cite a versão que você observou. Não desative ferramentas de segurança para "fazer o teste funcionar"; se uma ferramenta bloqueia você, isso é um resultado sob a ROE. Os padrões do guia de endurecimento do ano passado podem não corresponder à build que você viu. Citar a versão observada mantém o achado verificável. Uma ferramenta de segurança que bloqueia uma sondagem fez seu trabalho sob a ROE; desligá-la seria inventar um sistema diferente do que o cliente roda. Sam relata o bloqueio e passa para a próxima verificação planejada.

### 12.3b Imagens e análise offline

Imagens completas de disco têm alto impacto: tiram sistemas do ar, contêm dados pessoais e convidam à navegação fora do escopo. Prefira leituras ao vivo, com privilégio mínimo. Se uma imagem for de fato necessária, a ROE precisa nomear a cadeia de custódia, a criptografia em repouso, quem pode montá-la e uma data de destruição — e os laboratórios do curso continuam sem praticar a geração de imagens de hosts reais. Imagens são o último recurso por causa da indisponibilidade e da privacidade. Leituras ao vivo com privilégio mínimo respondem à maioria das perguntas sem copiar discos inteiros. Quando uma imagem é inevitável, a cadeia de custódia e a data de destruição são exigências da ROE, não gentilezas. Os laboratórios do curso nunca geram imagens de hosts reais, então os estudantes praticam a decisão de evitar a imagem, e não a geração da imagem em si.

### 12.4b Registrando mudanças nos hosts

Qualquer configuração que quem testa muda num host, mesmo um nível de log temporário, é escrita no log do engajamento com horário, motivo e o comando usado para revertê-la. No encerramento, Sam percorre essa lista com o dono do sistema, para que nenhum host da Riverstone Transit fique num estado que ninguém se lembra de ter criado. Mudanças temporárias de nível de log continuam sendo mudanças. Um comando de reversão escrito na hora sobrevive à rotatividade da equipe e aos plantões de fim de semana. Percorrer a lista com o dono transforma o encerramento numa lista de verificação compartilhada, em vez de um teste de memória. Sam se recusa a marcar um engajamento como concluído enquanto restar na lista qualquer mudança não revertida.

### Exercícios

- **EX034 — Desenho de conta.** Especifique uma conta de avaliação com privilégio mínimo para ler a participação no grupo de administradores locais em três hosts Windows. Rubrica: 3 = conta nominal, grupo/papel, limite de tempo, registro, revogação; 2 = três de cinco; 1 = "admin"; 0 = nada.
- **EX035 — Redação da severidade.** Reescreva "pegamos SYSTEM em tudo" como uma frase de achado com escopo. Rubrica: 3 = identidade, hosts, método (configuração/autorização), sem exploit; 2 = falta o escopo; 1 = ainda vago; 0 = linguagem de exploit.
- **EX036 — Verificação de revogação.** Liste três verificações pós-engajamento de que a conta de avaliação deixou de existir. Rubrica: 3 = desativada no diretório, resquício local, revisão de ticket/log; 2 = duas; 1 = uma; 0 = nada.

### Síntese

Leia a configuração com uma conta temporária; nomeie o repositório de identidades; revogue ao terminar.

### Continue estudando — capítulo 12 de 50

[← Capítulo 11 (rascunho)](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 (rascunho) →](#ch-13)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX036 (as de EX037–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). A Riverstone Transit, Sam Ito e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** r′(t) = 8 − 2t = 0 em t = 4, então o pico é r(4) = 32 − 16 = 16 req/s. Resolver 8t − t² = 7 dá t² − 8t + 7 = 0, t = 1 ou t = 7. O teto é violado do minuto 1 ao minuto 7, seis minutos. A nota 3 exige o pico e a janela.

**EX002.** Taxa: "No máximo 5 requisições por segundo para /api/tickets a partir do endereço de origem da avaliação." Total: "No máximo 20.000 requisições por dia corrido para /api/tickets." O total é mais fácil de verificar pelos logs (uma única contagem por dia); a taxa exige agrupamento por segundo e uma tolerância para a defasagem de relógio.

**EX003.** 2.160 / 4 = 540 segundos = 9 minutos. O cronograma plano é mais longo que a rampa de 6 minutos, mas nunca ultrapassa o teto.

**EX004.** T = {(h, p) : h ∈ 192.168.50.0/24, h ∉ {192.168.50.1, 192.168.50.254}, p ∈ {22, 443}}. |T| = (256 − 2) × 2 = 508. (Contar apenas os hosts utilizáveis, 254 − 2 = 252 hosts e 504 pares, também é aceito se for declarado.)

**EX005.** Seja P′ = P ∪ {q}. Qualquer (h, p) ∈ T tem p ∈ P ⊆ P′, e as outras cláusulas não mudam, então (h, p) ∈ T′. Logo, T ⊆ T′. Como acréscimos de porta só podem ampliar o escopo, eles precisam de aprovação escrita do cliente e de um segundo revisor, ao contrário dos acréscimos à lista de exclusão.

**EX006.** Os dois usam o host 192.168.50.20, que está na faixa 192.168.50.0/24 e fora da lista de exclusão. A porta 22 está em P = {22, 80, 443, 8080}; a porta 3389 não está, então essa cláusula falha e a decisão é DENY com o motivo port-not-in-scope.

**EX007.** 800 km em cada sentido a ~200.000 km/s dão ~4 ms, então ~8 ms de ida e volta é o piso. 2 ms não é plausível; provavelmente a resposta veio de um cache local, de um proxy ou de um local diferente do suposto. Peça o método de medição e o caminho.

**EX008.** 500 × 120 × 8 = 480.000 b/s = 0,48 Mb/s, ou seja, 24% de 2 Mb/s. Acrescente a sobrecarga de cabeçalhos para um valor realista.

**EX009.** Bandas e canais permitidos; locais físicos exatos (prédios/andares); datas e horários; limites de potência de transmissão ou de teste ativo; e uma regra de que dispositivos de terceiros e seu tráfego estão fora do escopo, não são registrados ou são descartados imediatamente. Quaisquer quatro, com um signatário autorizador nomeado.

**EX010.** `in` sobre strings testa uma substring, e "8443,22" contém "443". Interprete o campo como um conjunto de inteiros, `ports = {int(x) for x in s.split(",")}`, e teste `443 in ports`, que aqui é False.

**EX011.** Teste 192.168.50.0 e 192.168.50.255 (ambos dentro do objeto de rede /24) e 192.168.51.0, que precisa ficar fora. Uma implementação por prefixo de string costuma falhar no último caso.

**EX012.** O motivo identifica qual regra disparou, então os logs mostram por que uma ação foi bloqueada ("deny-list" ou "outside-cidr"), e os revisores podem conferir a regra certa. Os testes podem então afirmar o motivo específico, pegando um caso em que a resposta certa é alcançada pelo motivo errado.

**EX013.** Título: "O edge da VPN corporativa permite uma versão legada de protocolo sem autenticação multifator." Evidência: "Em 14 de março, às 10:20 (sintético), a revisão de configuração autorizada de corp-vpn-edge mostrou o perfil legado ativo, com login só por senha; ref. FD-131." Sem comandos, sem credenciais.

**EX014.** "Entre 09:00 e 17:00 do dia autorizado, avaliamos 12 hosts da Riverstone em escopo, sob a ROE v1.3. Dois achados são críticos: uma senha de administrador padrão na UI web de staging e uma conta de serviço do laboratório com direitos de administrador de domínio. Pedimos ao dono da plataforma que aprove a troca de credenciais dentro do SLA crítico de 7 dias."

**EX015.** Por exemplo: (1) o gateway da lista de exclusão e dois hosts que estavam fora do ar não foram avaliados, então seu estado é desconhecido; (2) engenharia social e acesso físico estavam fora do escopo, então o relatório não diz nada sobre a resiliência a phishing. Cada limite estreita o que as conclusões cobrem.

**EX016.** Tentativas esperadas por envio = 1/0,7 ≈ 1,429; para 500 envios, cerca de 714 tentativas. A ROE e o limite de taxa precisam cobrir 714, não 500.

**EX017.** B′ = 3 − 5 = −2/dia, então B(t) = 40 − 2t = 0 em t = 20 dias, supondo taxas constantes e sem prioridade.

**EX018.** Teoria: 1 − 0,2³ = 0,992 contra 0,8, um ganho de 0,192 (19,2 pontos). O empírico do laboratório, 988/1000 contra 784/1000, dá cerca de 20,4 pontos; qualquer um dos números, com a comparação, vale 3.

**EX019.** Estimativa pontual de 20%. Um intervalo de Wilson de 95% vai de aproximadamente 10,5% a 34,5%. Você pode dizer que a taxa provavelmente fica entre a casa dos dez e o início dos trinta por cento; não pode alegar superioridade sobre outro método com 25% sem uma amostra maior ou pareada.

**EX020.** Precisão = (0,9·0,005) / (0,9·0,005 + 0,02·0,995) = 0,0045 / (0,0045 + 0,0199) ≈ 0,184 (18,4%).

**EX021.** "Com 12/100 e 18/100, os intervalos se sobrepõem bastante; esta amostra não justifica classificar os filtros. Precisamos de um n maior ou de um teste pareado com os mesmos prompts antes de escolher um."

**EX022.** Usuário: respostas HTTP, leituras autenticadas de API, a própria lista de processos, logs de aplicação que a conta pode ver, o certificado TLS apresentado. Elevado: disco bruto, memória de outros usuários, módulos de kernel, tabelas de firewall, console do hipervisor. Quaisquer seis corretos, com a divisão clara.

**EX023.** "Somente o host lab-cache-01 (nenhum tráfego de produção roteado para ele)." "Pare e notifique o contato se a latência mediana da requisição canário passar de 50 ms por cinco minutos." Mais: "nenhum resultado publicado com chaves de produção ou dados de clientes."

**EX024.** Sob a ROE, tente um login com a senha padrão do fornecedor na URL de staging; capture o status HTTP e uma captura de tela com dados ocultados; abra um ticket no FindingsDesk com horário e URL; faça logout; não guarde a senha no corpo do ticket (referencie o repositório de evidências lacrado). Nenhum acesso ao sistema operacional é necessário.

**EX025.** Na ingestão, se alguma chave casar com a regex, rejeite com 400 e o motivo "forbidden field". Exemplo de corpo que falha: `{"title":"x","payload":"..."}`. Os testes afirmam a rejeição.

**EX026.** A impressão digital é (ativo, fraqueza, local). As duas linhas de /login compartilham (web-01, missing-header, /login); /account é outro local, então tem outra impressão digital e é um achado separado.

**EX027.** Depois de acrescentar o host h à lista de exclusão, para toda porta p, allowed(h, p) é False. De forma equivalente, o conjunto permitido depois da mudança é um subconjunto do conjunto de antes.

**EX028.** "Não posso fornecer um exploit funcional nem uma PoC contra um produto real — isso é uso dual e fica fora das regras de segurança deste curso. Posso ajudar você a escrever a descrição de um achado a partir de evidências sintéticas ou indicar o processo público de comunicados do fornecedor."

**EX029.** denial-of-service → deny-action; password-spray-lab sem aprovação → needs-approval; service-enum às 18:00 → outside-hours; service-enum com concorrência 20 → concurrency. O password spraying aprovado e a enumeração dentro do horário com concorrência 3 são ALLOW.

**EX030.** Sistemas e endpoints em escopo; métodos permitidos; datas e horários; limites de taxa, de dados e de privacidade; contatos nomeados e escalonamento; condições de parada e regras de retomada. Assinada por alguém com autoridade sobre os ativos.

**EX031.** Exemplo: a observação de MAC/ARP exige acesso ao segmento de enlace; o certificado TLS apresentado exige uma conexão TCP até a porta; um campo privado de API exige uma sessão autenticada. As triplas exatas podem variar, se justificadas.

**EX032.** P = {80, 443, 8080}; nota: "Só HTTP e HTTPS para o portal de tarifas e as aplicações de funcionários listados no Apêndice A; sem MITM de TLS, sem outros protocolos nessas portas."

**EX033.** public-web-portal (9) e corp-vpn-edge (8): maior exposição e raio de impacto, ambos voltados para a Internet. staging-admin-ui (7) vem em seguida, se sobrar tempo.

**EX034.** Conta `svc-assess-sam` num papel personalizado "Local group readers" nos três hosts (ou uma gMSA com esse direito); válida das 09:00 às 17:00 nas datas da ROE; todos os logons auditados; desativada automaticamente ao fim do dia, mais uma verificação manual.

**EX035.** "Nos hosts de laboratório HV-01 e HV-02, a conta de avaliação recebeu participação no grupo local Administrators pela GPO Lab-Admins; confirmado por leitura do grupo em 14 de março; nenhum exploit usado; remova o vínculo da GPO e verifique de novo."

**EX036.** (1) O IdP/diretório mostra a conta desativada ou excluída; (2) não há administradores locais remanescentes com esse nome nos hosts amostrados; (3) o último logon e a trilha de tickets foram revisados, sem atividade depois do horário de término.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Albrecht, M. R., Jensen, R. B. (2020). The Vacuity of the Open Source Security Testing Methodology Manual. arXiv:2010.06377.
- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide (2024 update). <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- MITRE ATT&CK. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
