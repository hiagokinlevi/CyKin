# Segurança Ofensiva Autorizada e Red Team: Um Livro para a Graduação em Engenharia

- Idioma: português do Brasil (`pt`); cinco anos; aproximadamente 4.000 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 50 já estão escritos em português, com os exercícios EX001–EX012 e suas resoluções com rubricas de 0 a 3; os capítulos 5–50 (EX013–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX012 (as de EX013–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). A Riverstone Transit, Sam Ito e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
