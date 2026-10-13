# Criptografia e Serviços de Confiança: Curso de Mestrado

- Idioma: português do Brasil (`pt`); curso 169, curso de mestrado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 8 já estão escritos em português, com os exercícios EX001–EX026 e suas resoluções com rubricas de 0 a 3 e 4 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 5–8 (EX027–EX050) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: mestrandos que vão conduzir um estudo reprodutível sobre como as organizações operam certificados e a confiança em chaves públicas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: o livro estuda como são operadas ferramentas avaliadas de TLS, X.509 e ACME. Ele nunca ensina a construir primitivas criptográficas para produção; os laboratórios calculam datas, contagens, taxas e pseudônimos com chave sobre dados sintéticos. Pessoas, organizações e hosts são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um mestrando que pergunta por que certificados TLS expiram sem que ninguém perceba numa rede hospitalar, e se a renovação automatizada com ACME (RFC 8555) reduz os incidentes de expiração em comparação com a renovação manual. O percurso vai do método de revisão da literatura a um seminário sobre X.509 e TLS 1.3, um desenho de estudo ético, explicações concorrentes, um piloto, a análise dos dados, a redação e uma revisão independente. Tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Felipe Arantes** | Mestrando | Inventado |
| **Dra. Ingrid Solberg** | Orientadora | Inventada |
| **Coldwater Polytechnic** | Universidade fictícia | Inventada |
| **Briarwood Health Network** | Parceira fictícia com cerca de 1.400 certificados | Inventada |

### Fontes principais

[RFC 5280](https://www.rfc-editor.org/rfc/rfc5280) (perfil X.509); [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) (TLS 1.3); [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555) (ACME); [RFC 6962](https://www.rfc-editor.org/rfc/rfc6962) (Certificate Transparency); NIST [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5); Boneh e Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); Katz e Lindell (3ª ed.). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–8: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Pergunta de pesquisa e método de revisão da literatura

### Objetivos de aprendizagem

Você vai (1) transformar uma dor operacional numa questão pesquisável sobre o ciclo de vida dos certificados; (2) conduzir uma busca documentada na literatura com um funil de triagem; (3) registrar por que cada fonte foi mantida ou descartada.

### 1.1 O caso

Felipe Arantes é mestrando na fictícia Coldwater Polytechnic, sob orientação da Dra. Ingrid Solberg. A fictícia Briarwood Health Network mantém cerca de 1.400 certificados TLS em portais de pacientes, sistemas de laboratório e APIs internas. No ano passado, vários expiraram sem que ninguém percebesse, e os profissionais de saúde perderam brevemente o acesso aos resultados de exames. Alguns certificados se renovam automaticamente por meio de um cliente ACME, conforme definido na RFC 8555, enquanto outros são renovados à mão a partir de uma planilha. A pergunta de trabalho de Felipe é se a renovação automatizada está associada a menos incidentes de expiração por certificado-ano do que a renovação manual, e o que mais explica os incidentes que ainda acontecem. Todos os hosts e números deste livro são sintéticos.

### 1.2 Afinar a pergunta

Uma boa pergunta de mestrado é estreita o bastante para ser respondida em um ano e clara quanto à sua unidade. Felipe define um incidente de expiração como uma falha visível ao usuário causada por um certificado que passou da data notAfter, o campo de validade definido na RFC 5280. Sua unidade é o certificado-ano, para que um serviço com muitos certificados de vida curta não seja contado de forma injusta. Ele escreve uma pergunta primária sobre o modo de renovação e uma secundária sobre outras causas, e exclui explicitamente as falhas de revogação e as fraquezas de algoritmos, que são problemas reais, mas exigiriam outros dados. A Dra. Solberg pede que ele escreva os temas excluídos, para que o escopo não se expanda depois.

### 1.3 Uma busca documentada

Felipe faz buscas em três bases acadêmicas, além do índice de RFCs e das publicações do NIST, usando uma string escrita que combina termos de certificados (certificate, X.509, TLS, PKI) com termos de ciclo de vida (expiry, renewal, ACME, outage). Ele guarda as strings exatas, as datas e os números de resultados num log, para que outro estudante possa repetir a busca. As normas são buscadas separadamente, porque raramente aparecem nos índices acadêmicos, mas definem o vocabulário. As etapas de triagem seguem um padrão comum de revisão sistemática: remover duplicatas, triar títulos e resumos contra as regras de inclusão, ler os textos completos e manter apenas os estudos que relatam um desfecho de indisponibilidade ou de expiração.

### Laboratório — Funil de triagem

```python
"""Literature screening funnel for a synthetic review of certificate-lifecycle studies."""
STAGES = [("records found (3 databases + RFC/NIST search)", 412), ("after duplicate removal", 297),
          ("after title/abstract screen", 64), ("after full-text eligibility", 21),
          ("included with outage or expiry outcome", 9)]

def main():
    prev = None
    for name, n in STAGES:
        drop = "" if prev is None else f"  (-{prev - n})"
        print(f"{n:>4}  {name}{drop}")
        prev = n
    print(f"inclusion rate from deduplicated pool: {100 * STAGES[-1][1] / STAGES[1][1]:.1f}%")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_screen.py`. Saída verificada:

```text
 412  records found (3 databases + RFC/NIST search)
 297  after duplicate removal  (-115)
  64  after title/abstract screen  (-233)
  21  after full-text eligibility  (-43)
   9  included with outage or expiry outcome  (-12)
inclusion rate from deduplicated pool: 3.0%
```

### 1.4 Ler o funil

A busca encontra 412 registros; restam 297 depois da remoção das duplicatas, 64 passam pela triagem de títulos e resumos, 21 passam pela elegibilidade do texto completo e 9 relatam um desfecho de expiração ou de indisponibilidade. Só 3,0 por cento do conjunto sem duplicatas acaba incluído, o que é normal para uma pergunta estreita. A maior queda, 233 registros, acontece na triagem de títulos e resumos, sobretudo artigos sobre bugs de validação de certificados, e não sobre o gerenciamento do ciclo de vida. Felipe relata cada número, porque um leitor que vê apenas os nove estudos incluídos não consegue julgar se trabalhos relevantes foram perdidos ou excluídos por motivos fracos.

### 1.5 Registrar as decisões

Para cada artigo lido na íntegra, Felipe escreve uma linha: citação, população, medida de desfecho, se a renovação era automatizada e o motivo da inclusão ou exclusão. Doze artigos são descartados na leitura completa, a maioria porque mediu a emissão indevida de certificados pelas autoridades certificadoras, e não a expiração nos operadores. Ele registra separadamente a literatura cinzenta, como relatórios de indisponibilidade de fornecedores, marcada como não revisada por pares, porque descreve falhas reais, mas raramente declara seus métodos. Esse log se torna um apêndice da dissertação e permite que os examinadores testem se suas conclusões decorrem das evidências que ele de fato leu.

### Exemplo resolvido

Felipe escreve a pergunta com a unidade certificado-ano, registra as strings de busca e relata um funil de 412 para 9, com os motivos de cada exclusão na leitura completa.

> **Caso sintético.** A Coldwater, a Briarwood e todos os hosts são inventados; a RFC 5280 e a RFC 8555 são reais.

### Erros e limites

As buscas perdem trabalhos indexados com outras palavras, e a literatura cinzenta é irregular. Um funil mostra diligência, e não completude, então declare a data e os limites da busca.

### Exercícios

- **EX001 — Pergunta de trabalho.** Enuncie a pergunta primária de Felipe com sua unidade. *Rubrica:* 3 = a renovação automatizada com ACME está associada a menos incidentes de expiração por certificado-ano do que a renovação manual;; 2 = sem unidade;; 1 = "resolver a expiração";; 0 = nenhuma.

- **EX002 — Definição de incidente.** Como é definido um incidente de expiração, e que campo marca a expiração? *Rubrica:* 3 = falha visível ao usuário causada por um certificado após o notAfter (RFC 5280);; 2 = definição sem o campo;; 1 = qualquer aviso;; 0 = nenhuma.

- **EX003 — Temas excluídos.** Que dois temas Felipe excluiu, e por quê? *Rubrica:* 3 = falhas de revogação e fraquezas de algoritmos; exigem outros dados;; 2 = só os temas;; 1 = um;; 0 = nenhuma.

- **EX004 — Números do funil.** Dê as contagens em cada uma das cinco etapas. *Rubrica:* 3 = 412, 297, 64, 21, 9;; 2 = quatro certas;; 1 = só as pontas;; 0 = nenhuma.

- **EX005 — Maior queda.** Onde ocorreu a maior queda, e o que causou a maior parte dela? *Rubrica:* 3 = títulos/resumos, 233 registros, sobretudo artigos sobre bugs de validação;; 2 = só a etapa;; 1 = duplicatas;; 0 = nenhuma.

- **EX006 — Exclusões na leitura completa.** Por que a maioria dos artigos lidos na íntegra foi excluída? *Rubrica:* 3 = estudavam a emissão indevida por ACs, e não a expiração nos operadores;; 2 = fora do tema;; 1 = qualidade;; 0 = nenhuma.

- **EX007 — Literatura cinzenta.** Como Felipe trata os relatórios de indisponibilidade de fornecedores? *Rubrica:* 3 = registra-os separadamente, marcados como não revisados por pares, pois os métodos raramente são declarados;; 2 = marca-os;; 1 = ignora;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Criptografia e serviços de confiança: seminário avançado

### Objetivos de aprendizagem

Você vai (1) explicar como um certificado X.509 vincula uma chave pública a um nome; (2) descrever onde os certificados entram no handshake do TLS 1.3; (3) ler um inventário de certificados e identificar riscos de ciclo de vida.

### 2.1 O que um certificado afirma

Um certificado é uma declaração assinada por uma autoridade emissora de que uma chave pública pertence a um titular, válida entre notBefore e notAfter. A RFC 5280 define o perfil dos campos: titular e nomes alternativos do titular, emissor, número de série, validade, uso da chave e extensões. A assinatura digital, feita com um algoritmo como o ECDSA ou o RSA do FIPS 186-5, permite que um cliente confira a declaração usando a chave pública do emissor, subindo por uma cadeia até uma raiz em que já confia. Katz e Lindell descrevem isso como transferir a confiança de muitas chaves para poucas raízes. A janela de validade faz parte da declaração assinada, então um certificado expirado não pode ser estendido sem uma nova assinatura.

### 2.2 Certificados no TLS 1.3

Num handshake do TLS 1.3, definido na RFC 8446, cliente e servidor primeiro combinam os compartilhamentos de chave, em geral usando o X25519 da RFC 7748, e derivam as chaves do handshake com o HKDF da RFC 5869. Em seguida, o servidor envia sua cadeia de certificados e uma mensagem CertificateVerify, uma assinatura sobre a transcrição do handshake feita com a chave privada do certificado. O cliente valida a cadeia, os nomes e o período de validade. Se o certificado expirou, um cliente configurado corretamente aborta o handshake. Foi esse o comportamento que os profissionais da Briarwood viveram: a criptografia funcionou exatamente como projetada e recusou uma afirmação vencida.

### 2.3 Por que as validades continuam encolhendo

Validades curtas limitam por quanto tempo uma chave roubada ou um certificado emitido por engano continua útil e reduzem a dependência da revogação, que os clientes conferem de forma irregular. O custo é operacional: mais renovações, cada uma uma chance de falhar. O Certificate Transparency, especificado na RFC 6962, acrescenta logs públicos para que os donos de domínios possam ver todo certificado emitido para os seus nomes. O SP 800-57 Part 1 enquadra a mesma tensão para todas as chaves: os criptoperíodos devem ser limitados, mas toda rotação precisa ser planejada. O artigo de seminário de Felipe argumenta que a automação é a única resposta escalável para validades cada vez mais curtas, o que seu estudo vai testar, em vez de pressupor.

### Laboratório — Leitura do inventário

```python
"""Days to expiry for a synthetic certificate inventory, as of a fixed audit date."""
from datetime import date
AUDIT = date(2026, 3, 1)
CERTS = [("h-portal", "acme", date(2026, 4, 20)), ("h-labres", "manual", date(2026, 3, 9)),
         ("h-pacs", "manual", date(2026, 2, 25)), ("h-api", "acme", date(2026, 4, 2)),
         ("h-vpn", "manual", date(2027, 1, 15)), ("h-mail", "manual", date(2026, 3, 20)),
         ("h-sched", "acme", date(2026, 5, 1)), ("h-hr", "manual", date(2026, 3, 27))]

def main():
    for name, how, exp in sorted(CERTS, key=lambda c: c[2]):
        d = (exp - AUDIT).days
        flag = "EXPIRED" if d < 0 else ("<30d" if d < 30 else "")
        print(f"{name:<9} {how:<7} {exp}  {d:>4} d  {flag}")
    urgent = [c for c in CERTS if (c[2] - AUDIT).days < 30]
    print(f"urgent {len(urgent)}/{len(CERTS)}, all manual: {all(c[1] == 'manual' for c in urgent)}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_inventory.py`. Saída verificada:

```text
h-pacs    manual  2026-02-25    -4 d  EXPIRED
h-labres  manual  2026-03-09     8 d  <30d
h-mail    manual  2026-03-20    19 d  <30d
h-hr      manual  2026-03-27    26 d  <30d
h-api     acme    2026-04-02    32 d  
h-portal  acme    2026-04-20    50 d  
h-sched   acme    2026-05-01    61 d  
h-vpn     manual  2027-01-15   320 d  
urgent 4/8, all manual: True
```

### 2.4 Ler o inventário

Na data sintética da auditoria, 1º de março de 2026, um dos oito certificados amostrados, h-pacs, já expirou há quatro dias, e mais três expiram em até trinta dias: h-labres em 8 dias, h-mail em 19 e h-hr em 26. Os quatro certificados urgentes são renovados manualmente, enquanto os três certificados ACME estão entre 32 e 61 dias, o que é coerente com clientes que renovam por volta de um terço da validade antes da expiração. Um certificado manual, h-vpn, tem 320 dias restantes. Felipe observa que um certificado manual de vida longa também não é seguro: ele vai expirar muito depois que a pessoa que o instalou tiver mudado de função.

### 2.5 Do seminário ao estudo

O seminário deixa Felipe com três hipóteses operacionais. Os certificados manuais se concentram perto da expiração porque a renovação depende de uma pessoa se lembrar. Os certificados automatizados ainda podem falhar quando o cliente ACME quebra em silêncio, por exemplo depois que uma mudança de firewall bloqueia o desafio de validação. E os certificados sem um dono registrado falham qualquer que seja o método de renovação, porque ninguém recebe os avisos nem age sobre eles. A terceira hipótese concorre com sua pergunta principal e voltará no capítulo 4. Ele as escreve agora para que a análise posterior teste ideias que ele tinha antes de ver os dados de desfecho.

### Exemplo resolvido

Felipe explica como um certificado expirado faz um cliente TLS 1.3 abortar e depois lê uma amostra de oito certificados em que os quatro itens urgentes são manuais.

> **Caso sintético.** Os oito hosts e as datas são inventados; a RFC 5280, a RFC 8446 e a RFC 6962 são reais.

### Erros e limites

Uma amostra de oito linhas ilustra; ela não estima uma taxa. As datas de validade, sozinhas, não conseguem mostrar se um cliente ACME está de fato saudável.

### Exercícios

- **EX008 — Afirmação do certificado.** O que um certificado X.509 afirma, e o que o torna verificável? *Rubrica:* 3 = vínculo, assinado pelo emissor, entre a chave pública e o titular dentro da janela de validade; verificado com a chave do emissor subindo pela cadeia até uma raiz confiável;; 2 = só o vínculo;; 1 = "cifra o tráfego";; 0 = nenhuma.

- **EX009 — Papel no handshake.** Em que ponto do TLS 1.3 o servidor prova que possui a chave do certificado? *Rubrica:* 3 = CertificateVerify, uma assinatura sobre a transcrição;; 2 = "durante a mensagem de certificado";; 1 = compartilhamento de chave;; 0 = nenhuma.

- **EX010 — Validades curtas.** Dê um benefício e um custo de validades de certificado mais curtas. *Rubrica:* 3 = limita a janela de uma chave roubada/menos dependência da revogação; mais renovações que podem falhar;; 2 = um lado;; 1 = vago;; 0 = nenhuma.

- **EX011 — Certificados urgentes.** Que certificados amostrados estavam expirados ou com menos de 30 dias, e como eram renovados? *Rubrica:* 3 = h-pacs expirado; h-labres, h-mail, h-hr com menos de 30 dias, todos manuais;; 2 = contagem e modo;; 1 = só a contagem;; 0 = nenhuma.

- **EX012 — Certificado manual longo.** Por que h-vpn, com 320 dias, ainda é um risco? *Rubrica:* 3 = expira depois que quem o instalou talvez tenha saído, então ninguém se lembra;; 2 = continua manual;; 1 = seguro;; 0 = nenhuma.

- **EX013 — Falha silenciosa do ACME.** Como um certificado automatizado ainda pode expirar? *Rubrica:* 3 = o cliente ACME quebra em silêncio, p. ex. o firewall bloqueia o desafio de validação;; 2 = falha do cliente;; 1 = nunca;; 0 = nenhuma.

- **EX014 — Hipótese concorrente.** Que hipótese do seminário concorre com a pergunta principal? *Rubrica:* 3 = certificados sem dono registrado falham qualquer que seja o modo de renovação;; 2 = propriedade;; 1 = algoritmo;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Desenho do estudo, ética e reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) escolher um desenho observacional adequado aos registros de certificados existentes; (2) pseudonimizar nomes de host com uma função com chave; (3) planejar um estudo que outras pessoas possam reproduzir.

### 3.1 Escolher um desenho observacional

Felipe não pode randomizar os certificados entre os modos de renovação; a Briarwood decidiu isso anos atrás. Ele escolhe um desenho de coorte retrospectiva: todo certificado ativo nos últimos dois anos é membro, seu modo de renovação é a exposição, e os incidentes de expiração do sistema de chamados são o desfecho. Ele mede o tempo de exposição em certificados-ano, de modo que um certificado que existiu por seis meses contribui com meio ano. Ele aceita abertamente a principal fraqueza: os serviços escolhidos para automação podem diferir dos manuais em idade, equipe ou importância, então as diferenças podem refletir essas características, e não o modo de renovação.

### 3.2 Ética e aprovação

O estudo não toca em dados de pacientes, mas o comitê de ética ainda o revisa, porque os nomes de host e os chamados podem revelar a arquitetura interna da Briarwood e nomes de funcionários. O protocolo de Felipe diz que o texto dos chamados só é lido nas instalações da Briarwood, que os nomes dos funcionários são removidos antes da exportação e que o conjunto de dados exportado contém apenas identificadores pseudonimizados dos hosts, o modo de renovação, as datas e as contagens de incidentes. Qualquer certificado já expirado ou prestes a expirar que ele perceba é comunicado ao líder de infraestrutura da Briarwood no mesmo dia, porque um estudo sobre indisponibilidades não pode deixar uma acontecer sabendo dela.

### 3.3 Pseudônimos com chave

Felipe precisa de pseudônimos estáveis: o mesmo nome de host precisa corresponder ao mesmo identificador em todos os arquivos, mas pessoas de fora não podem conseguir revertê-lo. Um hash simples falha, porque qualquer um pode calcular o hash de um nome de host adivinhado, como portal.briarwood.example, e comparar. Um hash com chave, o HMAC da RFC 2104 com SHA-256, resolve isso: só quem detém a chave secreta consegue calcular o mapeamento. A Briarwood gera e guarda a chave; Felipe recebe apenas dados pseudonimizados. O laboratório usa uma chave de demonstração fixa apenas para que a saída seja reproduzível e mostra que uma chave aleatória nova, gerada pelo módulo secrets, produz pseudônimos sem relação.

### Laboratório — Pseudônimos com chave

```python
"""Keyed pseudonyms for hostnames with HMAC-SHA256 (RFC 2104); synthetic names, demo key only."""
import hmac, hashlib, secrets
HOSTS = ["portal.briarwood.example", "lab-results.briarwood.example", "portal.briarwood.example"]

def pseud(key, host):
    return "h-" + hmac.new(key, host.encode(), hashlib.sha256).hexdigest()[:10]

def main():
    fixed = b"study-demo-key-not-for-production"  # fixed so output is reproducible
    for h in HOSTS:
        print(f"{h:<33} -> {pseud(fixed, h)}")
    plain = "h-" + hashlib.sha256(HOSTS[0].encode()).hexdigest()[:10]
    print(f"unkeyed SHA-256 of first host -> {plain} (anyone can recompute)")
    fresh = secrets.token_bytes(32)
    print(f"fresh random key gives same pseudonym as demo key: {pseud(fresh, HOSTS[0]) == pseud(fixed, HOSTS[0])}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_pseudo.py`. Saída verificada:

```text
portal.briarwood.example          -> h-6f292159ff
lab-results.briarwood.example     -> h-915f39cfa2
portal.briarwood.example          -> h-6f292159ff
unkeyed SHA-256 of first host -> h-80926435c3 (anyone can recompute)
fresh random key gives same pseudonym as demo key: False
```

### 3.4 Ler os pseudônimos

As duas ocorrências de portal.briarwood.example correspondem a h-6f292159ff, então os registros se juntam corretamente, enquanto lab-results corresponde a h-915f39cfa2. O SHA-256 sem chave do primeiro host dá h-80926435c3, que qualquer pessoa de fora que adivinhe o nome pode recalcular; é por isso que o hash simples não é pseudonimização. Com uma chave nova de 32 bytes, o pseudônimo é diferente, o que confirma que o mapeamento depende do segredo. Felipe observa que truncar para dez caracteres hexadecimais é aceitável para 1.400 hosts, pois dá cerca de um trilhão de valores possíveis, mas que é preciso conferir colisões antes de juntar as tabelas.

### 3.5 Plano de reprodutibilidade

O plano de Felipe lista o que outro pesquisador precisaria: o dicionário de dados, as consultas de extração rodadas contra os sistemas de inventário e de chamados da Briarwood, os scripts de análise com as sementes aleatórias, o conjunto de dados pseudonimizado e um log de cada decisão de codificação manual. A Briarwood não pode publicar as consultas de extração, então ele as documenta em prosa com detalhe suficiente para adaptá-las em outro lugar. Ele fixa o ambiente de software na biblioteca padrão do Python, para evitar a deriva de dependências. A Dra. Solberg pede um ensaio: um colega repete a análise apenas a partir do pacote e reproduz todas as tabelas.

### Exemplo resolvido

Felipe registra um desenho de coorte retrospectiva medido em certificados-ano, obtém a aprovação ética com comunicação no mesmo dia de expirações ativas e exporta os dados com pseudônimos HMAC-SHA256 cuja chave fica na Briarwood.

> **Caso sintético.** Os hosts e a chave de demonstração são inventados; o HMAC (RFC 2104) é real, e chaves reais precisam vir de um cofre de segredos gerenciado.

### Erros e limites

Coortes observacionais não conseguem descartar a confusão; só conseguem medir e ajustar pelo que foi registrado. Os pseudônimos protegem contra pessoas de fora, e não contra quem obtiver a chave.

### Exercícios

- **EX015 — Escolha do desenho.** Por que uma coorte retrospectiva em vez de um experimento? *Rubrica:* 3 = o modo de renovação já está atribuído e não pode ser randomizado; a coorte usa registros existentes;; 2 = sem randomização;; 1 = mais barato;; 0 = nenhuma.

- **EX016 — Tempo de exposição.** Como um certificado de seis meses contribui para o denominador? *Rubrica:* 3 = meio certificado-ano;; 2 = parcial;; 1 = um;; 0 = nenhuma.

- **EX017 — Dever diante de risco ativo.** O que Felipe deve fazer ao perceber um certificado prestes a expirar? *Rubrica:* 3 = comunicá-lo ao líder de infraestrutura no mesmo dia;; 2 = comunicar;; 1 = registrá-lo;; 0 = nenhuma.

- **EX018 — Fraqueza do hash simples.** Por que o SHA-256 sem chave não serve para pseudônimos de nomes de host? *Rubrica:* 3 = qualquer um pode calcular o hash de nomes adivinhados e comparar;; 2 = quase reversível;; 1 = lento demais;; 0 = nenhuma.

- **EX019 — Pseudônimos do laboratório.** Que pseudônimo portal.briarwood.example recebeu, e o que o teste com chave nova imprimiu? *Rubrica:* 3 = h-6f292159ff nas duas vezes; False;; 2 = um;; 1 = o valor sem chave;; 0 = nenhuma.

- **EX020 — Ensaio.** O que o ensaio da Dra. Solberg conferiu? *Rubrica:* 3 = um colega reproduziu todas as tabelas só com o pacote;; 2 = reprodutibilidade;; 1 = estilo do código;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Criptografia e serviços de confiança: explicações concorrentes

### Objetivos de aprendizagem

Você vai (1) confrontar explicações rivais para a expiração de certificados; (2) ler uma tabulação cruzada em busca de confusão; (3) decidir quais explicações os dados conseguem e não conseguem distinguir.

### 4.1 Três explicações rivais

Felipe enuncia três explicações para os incidentes de expiração. A explicação do modo de renovação diz que a renovação manual falha porque as pessoas esquecem. A explicação da propriedade diz que os certificados sem um dono nomeado falham porque os avisos não chegam a ninguém, qualquer que seja o método de renovação. A explicação da colisão com mudanças diz que as renovações falham quando mudanças de rede ou de firewall quebram a validação ou a implantação, afetando em especial as renovações automatizadas. Cada uma prevê um padrão diferente. Se o modo de renovação domina, os incidentes manuais devem superar os automatizados mesmo entre os certificados com dono. Se a propriedade domina, os incidentes sem dono devem ser comuns nos dois modos.

### Laboratório — Tabulação cruzada das explicações

```python
"""Cross-tab of 30 synthetic expiry incidents against two competing explanations."""
from collections import Counter
# (renewal mode, owner recorded?) for each incident
INC = ([("manual", False)] * 14 + [("manual", True)] * 9 + [("acme", False)] * 5 + [("acme", True)] * 2)

def main():
    c = Counter(INC)
    print("            owner-missing  owner-known")
    for mode in ("manual", "acme"):
        print(f"{mode:<10} {c[(mode, False)]:>10} {c[(mode, True)]:>12}")
    for mode in ("manual", "acme"):
        tot = c[(mode, False)] + c[(mode, True)]
        print(f"{mode}: {tot} incidents, owner missing in {100 * c[(mode, False)] / tot:.0f}%")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_explain.py`. Saída verificada:

```text
            owner-missing  owner-known
manual             14            9
acme                5            2
manual: 23 incidents, owner missing in 61%
acme: 7 incidents, owner missing in 71%
```

### 4.2 Ler a tabulação cruzada

Entre trinta incidentes sintéticos, vinte e três envolvem certificados manuais e sete, certificados ACME. Os certificados sem dono respondem por 61 por cento dos incidentes manuais e por 71 por cento dos incidentes ACME. Felipe vê duas coisas. A renovação manual está claramente super-representada, o que apoia a explicação do modo de renovação. Mas a parcela sem dono é alta nos dois modos, o que também apoia a explicação da propriedade. As contagens brutas, sozinhas, não conseguem separá-las, porque ele ainda não dividiu pelo número de certificados em cada célula; uma contagem alta pode apenas refletir muitos certificados sem dono.

### 4.3 Confusão em termos simples

Um fator de confusão é um fator ligado tanto à exposição quanto ao desfecho. Se a Briarwood automatizou sobretudo serviços modernos e com dono bem definido e deixou na renovação manual os hosts legados órfãos, a propriedade faria a automação parecer melhor do que é. Felipe confere o inventário e descobre que 38 por cento dos certificados manuais não têm dono, contra 21 por cento dos certificados ACME. A propriedade é, portanto, um fator de confusão plausível, e sua análise precisa comparar iguais com iguais: certificados manuais e ACME dentro do grupo com dono conhecido e, separadamente, dentro do grupo sem dono.

### 4.4 Onde entra a colisão com mudanças

A explicação da colisão com mudanças precisa de outras evidências: chamados de mudança ligados às datas de renovação. Felipe descobre que cinco dos sete incidentes ACME vieram depois de uma mudança de firewall ou de proxy na semana anterior, quando o cliente ACME não conseguia mais completar seu desafio e registrava erros que ninguém acompanhava. A RFC 8555 define tipos de desafio como o HTTP-01 e o DNS-01, e cada um depende de infraestrutura fora do cliente. Essa explicação não concorre tanto com a automação quanto a qualifica: a automação elimina o esquecimento, mas acrescenta uma dependência que precisa ser monitorada.

### 4.5 O que os dados conseguem decidir

Felipe escreve uma tabela de decisão. Os dados conseguem estimar as taxas de incidentes por modo de renovação dentro dos estratos de propriedade, o que trata a confusão pela propriedade. Os dados conseguem descrever com que frequência as falhas automatizadas vêm depois de mudanças, mas, com sete incidentes, só de forma descritiva. Os dados não conseguem descartar fatores de confusão não medidos, como a criticidade do serviço, porque a Briarwood não a registra de forma consistente. Ele declara que sua conclusão será sobre associação, ajustada pela propriedade, e que qualquer linguagem causal precisa ser qualificada. Nomear os limites agora evita um exagero depois.

### Exemplo resolvido

A tabulação cruzada de Felipe mostra a renovação manual super-representada, mas parcelas sem dono altas nos dois modos; ele adota a estratificação pela propriedade e trata a colisão com mudanças como uma qualificação da automação.

> **Caso sintético.** Os trinta incidentes e as porcentagens de propriedade são inventados; os tipos de desafio da RFC 8555 são reais.

### Erros e limites

Contagens sem denominadores enganam; sempre converta em taxas. Estratificar por um fator de confusão deixa os outros sem controle.

### Exercícios

- **EX021 — Três explicações.** Cite as três explicações rivais. *Rubrica:* 3 = modo de renovação, propriedade, colisão com mudanças;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX022 — Parcelas da tabulação.** Que parcelas sem dono o laboratório relatou para cada modo? *Rubrica:* 3 = 61 por cento manual, 71 por cento ACME;; 2 = uma;; 1 = só as contagens;; 0 = nenhuma.

- **EX023 — Por que as contagens falham.** Por que as contagens brutas de incidentes não conseguem separar as explicações? *Rubrica:* 3 = não há denominadores; as contagens podem refletir quantos certificados cada célula contém;; 2 = precisa de taxas;; 1 = amostra pequena;; 0 = nenhuma.

- **EX024 — Evidência de confusão.** Que números do inventário tornam a propriedade um fator de confusão? *Rubrica:* 3 = 38 por cento dos manuais vs 21 por cento dos ACME sem dono;; 2 = direção;; 1 = nenhum;; 0 = nenhuma.

- **EX025 — Colisões com mudanças.** Quantos incidentes ACME vieram depois de mudanças de infraestrutura, e por quê? *Rubrica:* 3 = cinco de sete; o cliente não conseguia completar o desafio, erros sem acompanhamento;; 2 = o número;; 1 = o motivo;; 0 = nenhuma.

- **EX026 — Fator de confusão não medido.** Que fator de confusão os dados não conseguem tratar? *Rubrica:* 3 = a criticidade do serviço, não registrada de forma consistente;; 2 = "não medido";; 1 = propriedade;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX026 (as de EX027–EX050 estão na edição em inglês até a tradução dos capítulos correspondentes). Felipe Arantes, a Dra. Ingrid Solberg, a Coldwater Polytechnic, a Briarwood Health Network e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** A renovação automatizada com ACME está associada a menos incidentes de expiração por certificado-ano do que a renovação manual na Briarwood?

**EX002.** Uma falha visível ao usuário causada por um certificado usado depois da sua data notAfter, o campo de validade da RFC 5280.

**EX003.** As falhas de revogação e os algoritmos fracos, porque respondê-las exigiria dados diferentes dos registros de ciclo de vida.

**EX004.** 412 encontrados, 297 sem duplicatas, 64 após a triagem, 21 elegíveis, 9 incluídos.

**EX005.** A triagem de títulos e resumos removeu 233 registros, em grande parte artigos sobre bugs de validação de certificados.

**EX006.** A maioria mediu a emissão indevida pelas autoridades certificadoras, e não a expiração nas organizações operadoras.

**EX007.** Mantidos numa lista separada e marcados como não revisados por pares, porque esses relatórios descrevem falhas sem métodos claros.

**EX008.** Que o emissor atesta que uma chave pública pertence ao titular nomeado entre notBefore e notAfter; os clientes verificam a assinatura do emissor ao longo de uma cadeia até uma raiz em que confiam.

**EX009.** Na mensagem CertificateVerify, em que o servidor assina a transcrição do handshake com a chave privada do certificado.

**EX010.** Benefício: uma chave comprometida ou um certificado errado continua útil por menos tempo, e a revogação importa menos. Custo: muito mais renovações, cada uma das quais pode falhar.

**EX011.** h-pacs tinha expirado quatro dias antes, e h-labres, h-mail e h-hr expiravam em até 30 dias; os quatro eram manuais.

**EX012.** A renovação dele fica muito no futuro, provavelmente depois que a pessoa que o instalou tiver mudado de função, então ninguém se lembra dele.

**EX013.** Se o cliente ACME parar de funcionar sem ninguém notar, por exemplo porque uma mudança de firewall bloqueia o desafio de validação.

**EX014.** Que os certificados sem um dono registrado falham independentemente de serem renovados manual ou automaticamente.

**EX015.** A Briarwood já tinha escolhido o modo de renovação de cada certificado, então ele não pode ser randomizado; uma coorte usa o histórico existente.

**EX016.** Acrescenta 0,5 certificado-ano de exposição.

**EX017.** Avisar o líder de infraestrutura da Briarwood no mesmo dia.

**EX018.** Uma pessoa de fora pode calcular o hash de nomes de host prováveis e comparar os resultados, recuperando os nomes reais.

**EX019.** h-6f292159ff nas duas linhas, e a comparação com chave nova imprimiu False.

**EX020.** Se um colega, usando apenas o pacote, conseguiria regenerar todas as tabelas da dissertação.

**EX021.** Esquecimento causado pela renovação manual, ausência de dono, de modo que os avisos não chegam a ninguém, e mudanças de infraestrutura que quebram a renovação.

**EX022.** Sem dono em 61 por cento dos incidentes manuais e em 71 por cento dos incidentes ACME.

**EX023.** Faltam denominadores, então uma contagem grande pode apenas refletir muitos certificados naquele grupo, e não um risco maior.

**EX024.** Trinta e oito por cento dos certificados manuais não têm dono, contra vinte e um por cento dos certificados ACME.

**EX025.** Cinco de sete, porque uma mudança de firewall ou de proxy bloqueou o desafio ACME e os logs de erro do cliente não eram acompanhados.

**EX026.** O quão crítico é cada serviço, o que a Briarwood não registra de forma consistente.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barnes, R., Bhargavan, K., Lipp, B., & Wood, C. (2022). *Hybrid public key encryption* (RFC 9180). IETF. <https://www.rfc-editor.org/rfc/rfc9180>
- Barnes, R., Hoffman-Andrews, J., McCarney, D., & Kasten, J. (2019). *Automatic certificate management environment (ACME)* (RFC 8555). IETF. <https://www.rfc-editor.org/rfc/rfc8555>
- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Boneh, D., & Shoup, V. (2023). *A graduate course in applied cryptography* (version 0.6, draft). <https://toc.cryptobook.us/>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Dworkin, M. (2007). *Recommendation for block cipher modes of operation: Galois/Counter Mode (GCM) and GMAC* (NIST SP 800-38D). NIST. <https://doi.org/10.6028/NIST.SP.800-38D>
- Josefsson, S., & Liusvaara, I. (2017). *Edwards-curve digital signature algorithm (EdDSA)* (RFC 8032). IETF. <https://www.rfc-editor.org/rfc/rfc8032>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Krawczyk, H., & Eronen, P. (2010). *HMAC-based extract-and-expand key derivation function (HKDF)* (RFC 5869). IETF. <https://www.rfc-editor.org/rfc/rfc5869>
- Krawczyk, H., Bellare, M., & Canetti, R. (1997). *HMAC: Keyed-hashing for message authentication* (RFC 2104). IETF. <https://www.rfc-editor.org/rfc/rfc2104>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Langley, A., Hamburg, M., & Turner, S. (2016). *Elliptic curves for security* (RFC 7748). IETF. <https://www.rfc-editor.org/rfc/rfc7748>
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate transparency* (RFC 6962). IETF. <https://www.rfc-editor.org/rfc/rfc6962>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- Moriarty, K., Kaliski, B., Jonsson, J., & Rusch, A. (2016). *PKCS #1: RSA cryptography specifications version 2.2* (RFC 8017). IETF. <https://www.rfc-editor.org/rfc/rfc8017>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2008). *The keyed-hash message authentication code (HMAC)* (FIPS 198-1). <https://doi.org/10.6028/NIST.FIPS.198-1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2023). *Digital signature standard (DSS)* (FIPS 186-5). <https://doi.org/10.6028/NIST.FIPS.186-5>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Shoup, V. (2004). *Sequences of games: A tool for taming complexity in security proofs* (Cryptology ePrint Archive, Paper 2004/332). <https://eprint.iacr.org/2004/332>
