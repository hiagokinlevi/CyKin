# Criptografia e Serviços de Confiança: Curso de Mestrado

- Idioma: português do Brasil (`pt`); curso 169, curso de mestrado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–8 de 8 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; os cinco laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

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

### Síntese

Uma pergunta estreita com uma unidade justa, uma busca reproduzível e um registro completo de decisões são a base de um estudo de mestrado crível.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 08)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

### Síntese

Os certificados são afirmações assinadas e limitadas no tempo que o TLS impõe com rigor; são as operações do ciclo de vida, e não a criptografia, que decidem se eles continuam válidos.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 08)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

### Síntese

Um desenho observacional honesto, pseudônimos com chave mantidos pelo parceiro e um pacote de reprodutibilidade testado tornam um estudo de campo ao mesmo tempo ético e verificável.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 08)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX024 — Evidência de confusão.** Que números do inventário tornam a propriedade um fator de confusão? *Rubrica:* 3 = 38 por cento dos manuais vs 21 por cento dos ACME sem dono;; 2 = direção;; 1 = vago;; 0 = nenhuma.

- **EX025 — Colisões com mudanças.** Quantos incidentes ACME vieram depois de mudanças de infraestrutura, e por quê? *Rubrica:* 3 = cinco de sete; o cliente não conseguia completar o desafio, erros sem acompanhamento;; 2 = o número;; 1 = o motivo;; 0 = nenhuma.

- **EX026 — Fator de confusão não medido.** Que fator de confusão os dados não conseguem tratar? *Rubrica:* 3 = a criticidade do serviço, não registrada de forma consistente;; 2 = "não medido";; 1 = propriedade;; 0 = nenhuma.

### Síntese

Explicações rivais preveem padrões diferentes; testá-las exige taxas, estratificação por fatores de confusão medidos e franqueza sobre o que continua sem medida.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 08)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Proposta e piloto

### Objetivos de aprendizagem

Você vai (1) escrever uma proposta que se compromete com desfechos, estratos e análise; (2) pilotar a extração de dados numa pequena fatia; (3) corrigir os erros de extração antes da coleta completa.

### 5.1 A proposta

A proposta de Felipe enuncia o desfecho primário, incidentes de expiração por 100 certificados-ano, comparado entre a renovação manual e a ACME, no geral e dentro dos estratos com dono conhecido e sem dono. O desfecho secundário é a parcela dos incidentes ACME precedidos por uma mudança de infraestrutura nos sete dias anteriores. O plano de análise usa razões de taxas com intervalos por bootstrap, porque os incidentes são poucos e sua distribuição está longe da normal. Ele registra a semente e o número de reamostragens planejados e lista de antemão os campos do inventário que vai usar, para que não possa depois vasculhar o conjunto de dados atrás de uma divisão favorável.

### 5.2 Ligar certificados a incidentes

O passo técnico mais difícil é ligar os chamados aos certificados. Os chamados mencionam nomes de host em texto livre, às vezes com erros de grafia, enquanto o inventário usa nomes totalmente qualificados. Felipe escreve as regras de correspondência de antemão: primeiro, correspondência exata com o nome alternativo do titular; depois, uma lista documentada de apelidos conhecidos; por fim, revisão manual por duas pessoas para o que sobrar. Cada chamado também precisa mencionar a expiração do certificado ou um erro de navegador ou de cliente sobre a validade; chamados que apenas mencionam um certificado durante uma indisponibilidade sem relação são excluídos. As regras vão para o apêndice da proposta.

### 5.3 Conduzir o piloto

O piloto extrai três meses de chamados e a fatia correspondente do inventário: 118 certificados e 11 chamados candidatos. Duas pessoas aplicam as regras de ligação de forma independente. Elas concordam em nove chamados e discordam em dois. Uma discordância envolve um chamado que cita um balanceador de carga que termina o TLS de vários hosts; a outra envolve um certificado intermediário expirado numa cadeia, e não o próprio certificado do servidor. Felipe também descobre que 14 linhas do inventário não têm valor de modo de renovação, porque as planilhas mais antigas nunca o registraram. Ele trata isso como falhas do instrumento a corrigir, e não como resultados a interpretar.

### 5.4 Corrigir os instrumentos

Felipe faz três mudanças nas regras. Os chamados de balanceador de carga são atribuídos ao certificado de fato apresentado aos clientes, conferido contra o campo de endpoint do inventário. Os intermediários expirados são codificados como incidentes de expiração atribuídos ao dono da cadeia, porque a validação de caminho da RFC 5280 falha diante de qualquer certificado expirado no caminho, e não apenas do certificado folha. As linhas sem modo de renovação são preenchidas a partir dos registros de conta do próprio cliente ACME, quando possível, e, caso contrário, marcadas como desconhecidas e relatadas como um grupo separado, e não descartadas em silêncio. Cada mudança é registrada com data antes do início da extração completa.

### 5.5 O que o piloto não diz

O piloto cobre só três meses, então Felipe não calcula nem relata taxas de incidentes a partir dele. Ele o usa para estimar o esforço: a ligação levou cerca de quatro minutos por chamado, então uma extração de dois anos, com cerca de 120 chamados, é viável em um mês. Ele também confirma que a pseudonimização roda na Briarwood antes da exportação e que a chave do HMAC nunca sai do cofre de segredos deles. A Dra. Solberg aprova a proposta revisada, e Felipe agenda a extração completa para um período tranquilo, para que a equipe de infraestrutura possa responder a perguntas sobre chamados ambíguos.

### Exemplo resolvido

Felipe se compromete com taxas por 100 certificados-ano com estratos de propriedade, pilota a ligação com 118 certificados e 11 chamados e corrige as regras para balanceadores de carga, intermediários e modos de renovação ausentes.

> **Caso sintético.** As contagens e os tempos do piloto são inventados; a validação de caminho da RFC 5280 é real.

### Erros e limites

Um piloto curto demais não consegue estimar taxas e não deve tentar. Mudar as regras depois de ver os dados de desfecho, e não durante um piloto, transforma a análise em algo guiado pelo desfecho.

### Exercícios

- **EX027 — Desfecho primário.** Enuncie o desfecho primário e sua comparação. *Rubrica:* 3 = incidentes por 100 certificados-ano, manual vs ACME, no geral e por estrato de propriedade;; 2 = sem estratos;; 1 = contagens;; 0 = nenhuma.

- **EX028 — Ordem da ligação.** Em que ordem os chamados são ligados aos certificados? *Rubrica:* 3 = correspondência exata do SAN, lista de apelidos conhecidos, depois revisão manual por duas pessoas;; 2 = duas etapas;; 1 = só manual;; 0 = nenhuma.

- **EX029 — Discordâncias do piloto.** Sobre o que foram as duas discordâncias do piloto? *Rubrica:* 3 = balanceador de carga que termina vários hosts; certificado intermediário expirado;; 2 = uma;; 1 = erro de digitação;; 0 = nenhuma.

- **EX030 — Regra dos intermediários.** Como os intermediários expirados são codificados, e por quê? *Rubrica:* 3 = como incidentes de expiração do dono da cadeia, pois a validação de caminho da RFC 5280 falha diante de qualquer certificado expirado;; 2 = só a codificação;; 1 = excluídos;; 0 = nenhuma.

- **EX031 — Modo de renovação ausente.** O que acontece com as linhas sem modo de renovação? *Rubrica:* 3 = preencher a partir dos registros da conta ACME; senão, marcar como desconhecido e relatar à parte;; 2 = marcar como desconhecido;; 1 = descartar;; 0 = nenhuma.

- **EX032 — Estimativa de esforço.** Que estimativa de esforço o piloto produziu? *Rubrica:* 3 = cerca de quatro minutos por chamado, cerca de 120 chamados viáveis em um mês;; 2 = só os minutos;; 1 = vaga;; 0 = nenhuma.

### Síntese

Uma proposta específica, somada a um piloto voltado para falhas de extração, torna o conjunto de dados completo consistente antes que qualquer taxa seja calculada.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 08)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Coleta e análise de dados

### Objetivos de aprendizagem

Você vai (1) calcular taxas de incidentes por certificado-ano; (2) expressar a incerteza de uma razão de taxas com bootstrap; (3) comparar as estimativas gerais e estratificadas.

### 6.1 O conjunto de dados montado

A extração completa cobre dois anos. Os certificados manuais contribuem com 540 certificados-ano e 23 incidentes de expiração ligados; os certificados ACME, com 900 certificados-ano e 7 incidentes. Restam quarenta e uma linhas com modo de renovação desconhecido e dois incidentes; Felipe as relata à parte e roda uma conferência que mostra que atribuí-las todas a qualquer um dos grupos não muda nenhuma conclusão. Cada número remonta a uma consulta e a uma entrada do log de codificação. Antes de rodar qualquer comparação, ele relê a proposta para confirmar que a análise corresponde ao que registrou, incluindo a semente e o número de reamostragens.

### 6.2 Taxas e a razão de taxas

Uma taxa divide os eventos pela exposição. A renovação manual apresenta 4,26 incidentes por 100 certificados-ano, e a ACME, 0,78, o que dá uma razão de taxas de 5,48: os certificados manuais falharam cerca de cinco vezes e meia mais por unidade de exposição. Uma razão sozinha esconde a incerteza, e sete incidentes ACME é um número pequeno. O bootstrap estima a incerteza reamostrando os certificados-ano com reposição milhares de vezes e recalculando a razão, e depois lendo os 95 por cento centrais dos valores resultantes. Ele faz poucas suposições, o que se adapta a dados de eventos esparsos.

### Laboratório — Razão de taxas com bootstrap

```python
"""Expiry incidents per 100 certificate-years with a bootstrap interval for the rate ratio (synthetic)."""
import random
MANUAL = [1] * 23 + [0] * 517   # 540 manual certificate-years, 23 incidents
ACME = [1] * 7 + [0] * 893      # 900 ACME certificate-years, 7 incidents

def rate(x): return 100 * sum(x) / len(x)

def main():
    rr = rate(MANUAL) / rate(ACME)
    rng = random.Random(7); boots = []
    for _ in range(5000):
        m = [rng.choice(MANUAL) for _ in MANUAL]; a = [rng.choice(ACME) for _ in ACME]
        if sum(a): boots.append(rate(m) / rate(a))
    boots.sort()
    lo, hi = boots[int(0.025 * len(boots))], boots[int(0.975 * len(boots))]
    print(f"manual {rate(MANUAL):.2f} per 100 cert-years, acme {rate(ACME):.2f}")
    print(f"rate ratio {rr:.2f}, bootstrap 95% interval {lo:.2f}-{hi:.2f} (seed 7, 5000 resamples)")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_rate.py`. Saída verificada:

```text
manual 4.26 per 100 cert-years, acme 0.78
rate ratio 5.48, bootstrap 95% interval 2.50-17.50 (seed 7, 5000 resamples)
```

### 6.3 Ler o intervalo

O intervalo por bootstrap vai de 2,50 a 17,50, com semente 7 e 5.000 reamostragens. O limite inferior bem acima de 1 significa que os dados são difíceis de conciliar com taxas iguais, mas o intervalo é largo e assimétrico, porque um punhado de incidentes ACME domina o denominador da razão. Felipe relata o intervalo no resumo ao lado da estimativa pontual, escrevendo "cerca de 2,5 a 17,5 vezes maior" em vez de "5,48 vezes maior", porque o número único sugeriria mais precisão do que sete eventos conseguem dar. Assim, o leitor pode julgar por si mesmo quanto peso o achado merece.

### 6.4 Estratificar pela propriedade

Entre os certificados com dono conhecido, a renovação manual apresenta 9 incidentes em 335 certificados-ano, 2,69 por 100, e a ACME, 2 em 711, 0,28 por 100, uma razão perto de 9,6. Entre os certificados sem dono, a manual apresenta 14 em 205, 6,83 por 100, e a ACME, 5 em 189, 2,65 por 100, uma razão perto de 2,6. Daí decorrem duas lições. A automação está associada a taxas menores nos dois estratos, então a propriedade não elimina o efeito. E os certificados sem dono falham mais, qualquer que seja o modo: um certificado ACME órfão falha mais ou menos tanto quanto um manual com dono. A propriedade, portanto, importa por si só, e Felipe a assinala como uma segunda alavanca para o capítulo de discussão.

### 6.5 A descrição da colisão com mudanças

Cinco dos sete incidentes ACME vieram depois de uma mudança de infraestrutura nos sete dias anteriores, o que confirma a impressão do piloto. Felipe relata isso de forma descritiva, como a proposta exigia, e acrescenta uma observação concreta dos logs: em quatro desses cinco casos, o cliente ACME registrou erros de renovação por mais de uma semana antes da expiração, mas os logs não eram encaminhados ao monitoramento. Esse achado leva diretamente à ação: alertar sobre falhas de renovação, que o SP 800-57 Part 1 trataria como parte da transição planejada de chaves, fecha uma lacuna que a automação, sozinha, deixa aberta.

### Exemplo resolvido

Felipe relata 4,26 contra 0,78 incidentes por 100 certificados-ano, uma razão de taxas de 5,48 com intervalo por bootstrap de 2,50 a 17,50, uma taxa ACME menor nos dois estratos de propriedade e erros de renovação não monitorados antes da maioria dos incidentes ACME.

> **Caso sintético.** A exposição, os incidentes e os estratos são dados didáticos inventados.

### Erros e limites

Intervalos por bootstrap a partir de pouquíssimos eventos são instáveis; com sete eventos, relate-os como aproximados. A estratificação controla apenas a propriedade.

### Exercícios

- **EX033 — Taxas.** Informe as taxas dos dois modos de renovação por 100 certificados-ano. *Rubrica:* 3 = manual 4,26, ACME 0,78;; 2 = uma;; 1 = contagens;; 0 = nenhuma.

- **EX034 — Intervalo por bootstrap.** Dê a razão de taxas e seu intervalo, com a semente. *Rubrica:* 3 = 5,48, 2,50–17,50, semente 7, 5000 reamostragens;; 2 = razão e intervalo;; 1 = só a razão;; 0 = nenhuma.

- **EX035 — Intervalo largo.** Por que o intervalo é largo e assimétrico? *Rubrica:* 3 = apenas sete incidentes ACME dominam o denominador da razão;; 2 = amostra pequena;; 1 = código ruim;; 0 = nenhuma.

- **EX036 — Razões por estrato.** Dê a razão de taxas dentro de cada estrato de propriedade. *Rubrica:* 3 = cerca de 9,6 com dono conhecido, cerca de 2,6 sem dono;; 2 = uma;; 1 = só as taxas;; 0 = nenhuma.

- **EX037 — Comparação com órfãos.** Como um certificado ACME órfão se compara a um manual com dono? *Rubrica:* 3 = taxa mais ou menos igual (2,65 vs 2,69 por 100);; 2 = semelhante;; 1 = muito menor;; 0 = nenhuma.

- **EX038 — Achado nos logs.** O que os logs mostraram antes dos incidentes ACME, e que correção decorre disso? *Rubrica:* 3 = erros de renovação registrados por mais de uma semana em 4 de 5, sem monitoramento; alertar sobre falhas de renovação;; 2 = só o achado;; 1 = só a correção;; 0 = nenhuma.

### Síntese

Taxas, intervalos e estratos, juntos, mostram uma associação robusta entre a automação e menos expirações, e revelam a propriedade e o monitoramento como alavancas independentes.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 08)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Redação da dissertação e limitações

### Objetivos de aprendizagem

Você vai (1) estruturar uma dissertação para que cada capítulo sirva à afirmação principal; (2) escrever limitações específicas e úteis; (3) transformar os achados em recomendações que respeitem a força das evidências.

### 7.1 Estruturar em torno da afirmação

A dissertação de Felipe abre com uma afirmação: na Briarwood, a renovação ACME esteve associada a substancialmente menos incidentes de expiração por certificado-ano do que a renovação manual, nos dois estratos de propriedade, e a maioria dos incidentes ACME restantes veio de falhas de renovação não monitoradas após mudanças de infraestrutura. O capítulo de literatura explica por que essa questão estava em aberto; o de métodos define as unidades, as regras de ligação e a pseudonimização; o de resultados relata as taxas, os intervalos e os estratos; a discussão os interpreta. O teste da Dra. Solberg para cada parágrafo é se removê-lo enfraqueceria a afirmação. Os parágrafos que não passam no teste vão para os apêndices ou desaparecem.

### 7.2 Escrever os resultados com simplicidade

O capítulo de resultados começa pela análise primária exatamente como registrada, depois a análise estratificada, depois o achado descritivo da colisão com mudanças. Cada tabela declara a unidade, a exposição, o número de eventos e o método do intervalo. Felipe evita adjetivos como "dramático" e escreve números com intervalos. Onde uma análise foi acrescentada depois do piloto, como a conferência de sensibilidade do modo desconhecido, ele a rotula. Ele inclui o inventário de oito certificados do capítulo 2 apenas como ilustração na seção de contexto, explicitamente não como evidência.

### 7.3 Limitações específicas

Seções de limitações fracas listam ressalvas genéricas. Felipe escreve limitações específicas, cada uma com a direção provável do viés. Os chamados sub-registram as indisponibilidades curtas corrigidas antes que alguém abrisse um registro, o que provavelmente subconta mais os incidentes manuais, porque as renovações manuais muitas vezes são corrigidas à mão em minutos. A criticidade dos serviços não foi medida, então os serviços automatizados podem ser os mais bem mantidos, o que exageraria a vantagem do ACME. O estudo cobre uma rede de saúde com um cliente ACME; organizações que usam desafios DNS-01 com outra infraestrutura podem ver outros padrões de falha.

### 7.4 Recomendações proporcionais às evidências

A partir de evidências fortes, Felipe recomenda automatizar a renovação dos certificados que podem usá-la e designar um dono nomeado para cada certificado, porque as duas associações se mantiveram nos estratos. A partir de evidências mais fracas, descritivas, ele recomenda alertar sobre falhas de renovação ACME e revisar as dependências de certificados durante mudanças de firewall, enquadradas como medidas de baixo custo coerentes com os achados, e não como efeitos provados. Ele também recomenda monitorar os logs do Certificate Transparency, definidos na RFC 6962, para descobrir certificados ausentes do inventário, enquadrando isso como hipótese para trabalhos futuros, já que seu estudo nunca o mediu.

### 7.5 Escrever sobre criptografia com responsabilidade

Como os leitores podem ler por alto, Felipe acrescenta um quadro curto que esclarece o que o estudo não diz. Ele não diz que os certificados ou o TLS são fracos; as falhas foram operacionais, e a criptografia se comportou como a RFC 8446 e a RFC 5280 exigem. Ele não recomenda estender as validades para reduzir as renovações, o que trocaria conveniência operacional por uma janela de exposição maior para chaves comprometidas. E não recomenda construir scripts de renovação próprios no lugar de clientes ACME mantidos, porque ferramentas caseiras reintroduziriam exatamente as falhas silenciosas que o estudo observou.

### Exemplo resolvido

Felipe escreve uma dissertação guiada pela afirmação, limitações específicas com as direções do viés e recomendações graduadas pela força das evidências, além de um quadro sobre o que o estudo não implica a respeito da criptografia.

> **Caso sintético.** Os achados da Briarwood são inventados; a RFC 6962, a RFC 8446 e a RFC 5280 são reais.

### Erros e limites

Recomendar mais do que as evidências sustentam é a falha mais comum das dissertações. Limitações sem uma direção de viés ajudam pouco os leitores.

### Exercícios

- **EX039 — Teste do parágrafo.** Que teste a Dra. Solberg aplicou a cada parágrafo? *Rubrica:* 3 = removê-lo enfraqueceria a afirmação principal? Se não, mover ou cortar;; 2 = relevância;; 1 = tamanho;; 0 = nenhuma.

- **EX040 — Conteúdo das tabelas.** O que cada tabela de resultados precisa declarar? *Rubrica:* 3 = unidade, exposição, número de eventos, método do intervalo;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX041 — Viés dos chamados.** Em que direção o sub-registro dos chamados provavelmente enviesa os resultados, e por quê? *Rubrica:* 3 = subconta mais os incidentes manuais, pois as correções à mão acontecem em minutos, sem chamado;; 2 = direção;; 1 = vago;; 0 = nenhuma.

- **EX042 — Recomendações fortes versus fracas.** Que recomendações se apoiam em evidências fortes, e quais em fracas? *Rubrica:* 3 = automatizar a renovação e designar donos: fortes; alertas e revisão de mudanças: mais fracas;; 2 = parcial;; 1 = todas fortes;; 0 = nenhuma.

- **EX043 — Recomendação de CT.** Como o monitoramento do Certificate Transparency é enquadrado, e por quê? *Rubrica:* 3 = como hipótese para trabalhos futuros, porque o estudo não o mediu;; 2 = enquadrado com cautela;; 1 = provado;; 0 = nenhuma.

- **EX044 — O que ele não diz.** Dê duas coisas que o quadro de esclarecimento diz que o estudo não implica. *Rubrica:* 3 = duas entre: o TLS é fraco, estender as validades, escrever scripts de renovação próprios;; 2 = uma;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma estrutura guiada pela afirmação, limitações específicas e recomendações graduadas pelas evidências transformam a análise numa dissertação em que os leitores podem confiar e com base na qual podem agir.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 08)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Revisão independente e defesa

### Objetivos de aprendizagem

Você vai (1) preparar-se para o exame independente de um estudo sobre operações criptográficas; (2) responder aos questionamentos com evidências do pacote; (3) planejar a disseminação para os profissionais.

### 8.1 Exame externo

A Coldwater nomeia uma examinadora externa que trabalha com infraestrutura de chaves públicas em outra universidade. Ela recebe a dissertação, o conjunto de dados pseudonimizado e o pacote de reprodutibilidade e roda de novo a análise antes da defesa. Seu relatório prévio concorda com a razão de taxas e o intervalo, mas questiona duas escolhas: codificar os intermediários expirados como incidentes de expiração e a decisão de relatar à parte os modos de renovação desconhecidos. Felipe prepara uma resposta curta para cada uma, apontando para o log do piloto, para a regra de validação de caminho da RFC 5280 e para a conferência de sensibilidade, em vez de repetir suas conclusões.

### 8.2 Responder à questão dos intermediários

A examinadora argumenta que um intermediário expirado é culpa da autoridade emissora, e não da Briarwood. Felipe responde que os clientes viveram a mesma falha nos dois casos, que a Briarwood escolheu servir aquela cadeia e era responsável por atualizá-la, e que a validação de caminho da RFC 5280 rejeita qualquer certificado expirado no caminho. Em seguida, ele mostra o resultado de sensibilidade: remover os dois casos de intermediários muda a razão de taxas geral de 5,48 para cerca de 5,2, então a conclusão não depende da escolha. Mostrar a alternativa com calma responde à objeção melhor do que defender a regra original.

### 8.3 Perguntas sobre a criptografia

Um membro da banca pergunta se a mudança para certificados pós-quânticos alteraria os achados. Felipe responde que o ML-DSA do FIPS 204 e o SLH-DSA do FIPS 205 trazem chaves e assinaturas maiores e, possivelmente, cadeias híbridas durante a transição, mas que a renovação continua sendo um processo operacional. Se algo muda, a migração acrescenta risco: novas versões de clientes, novos perfis de certificado e mais mudanças, cada uma uma chance para as colisões com mudanças que seu estudo observou. Ele sugere que as recomendações de propriedade e de monitoramento se tornam mais importantes, e não menos, durante a migração. Ele se recusa a prever taxas de incidentes para a migração, já que seus dados não contêm nenhuma.

### 8.4 Disseminação para os profissionais

Depois da defesa, Felipe escreve um resumo de quatro páginas para profissionais da Briarwood e de hospitais semelhantes. Ele dá as taxas e o intervalo em linguagem simples, um checklist com três ações (automatizar onde possível, nomear um dono para cada certificado, alertar sobre falhas de renovação) e o quadro de esclarecimento sobre o que o estudo não implica. O líder de infraestrutura da Briarwood o revisa para garantir que não apareçam nomes de host nem a arquitetura interna. Felipe também oferece o livro de códigos anonimizado e as regras de ligação para reutilização, para que outras organizações possam medir suas próprias taxas de expiração nas mesmas unidades.

### 8.5 Encerrar o estudo

Felipe encerra formalmente o estudo. O comitê de ética recebe um relatório final, e a Briarwood destrói a chave de pseudonimização do HMAC segundo seu próprio procedimento de destruição de chaves, em linha com as fases do ciclo de vida do SP 800-57 Part 1, para que nem mesmo o conjunto de dados de Felipe possa ser ligado de volta aos nomes de host. O pacote de reprodutibilidade continua disponível, com uma nota de que a religação é impossível por projeto. A Dra. Solberg lembra a ele que destruir a chave faz parte da ética do estudo, e não é um incômodo: um pseudônimo é tão forte quanto a proteção da sua chave.

### Exemplo resolvido

Felipe responde à objeção da examinadora sobre os certificados intermediários com um resultado de sensibilidade (de 5,48 para cerca de 5,2), relaciona a migração pós-quântica ao risco de colisão com mudanças e encerra o estudo fazendo a Briarwood destruir a chave de pseudonimização.

> **Caso sintético.** A examinadora, a banca e os números são inventados; o FIPS 204, o FIPS 205 e o SP 800-57 são reais.

### Erros e limites

Respostas defensivas que repetem conclusões não convencem ninguém; mostre as alternativas e seu efeito. Nunca guarde uma chave de pseudonimização além do que o estudo precisa.

### Exercícios

- **EX045 — Preparação da examinadora.** O que a examinadora externa fez antes da defesa? *Rubrica:* 3 = rodou de novo a análise a partir do pacote e escreveu um relatório questionando duas escolhas;; 2 = rodou de novo a análise;; 1 = leu;; 0 = nenhuma.

- **EX046 — Sensibilidade dos intermediários.** Como a remoção dos casos de intermediários afetou o resultado? *Rubrica:* 3 = razão de taxas de 5,48 para cerca de 5,2, conclusão inalterada;; 2 = inalterada;; 1 = invertida;; 0 = nenhuma.

- **EX047 — Argumento de responsabilidade.** Dê dois motivos pelos quais Felipe manteve os intermediários como incidentes da Briarwood. *Rubrica:* 3 = dois entre: mesma falha no cliente, a Briarwood servia a cadeia, a validação de caminho rejeita qualquer certificado expirado;; 2 = um;; 1 = culpa da autoridade;; 0 = nenhuma.

- **EX048 — Efeito pós-quântico.** Como a migração PQ poderia afetar o risco de expiração? *Rubrica:* 3 = FIPS 204/205: chaves maiores, cadeias híbridas, mais mudanças aumentam o risco de colisão; propriedade e monitoramento importam mais;; 2 = parcial;; 1 = nenhum efeito;; 0 = nenhuma.

- **EX049 — Checklist para profissionais.** Liste as três ações do resumo para profissionais. *Rubrica:* 3 = automatizar onde possível, nomear um dono, alertar sobre falhas de renovação;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX050 — Destruição da chave.** Por que a Briarwood destrói a chave do HMAC no encerramento? *Rubrica:* 3 = para que os dados nunca possam ser religados; a força do pseudônimo depende da proteção da chave; ciclo de vida do SP 800-57;; 2 = privacidade;; 1 = espaço em disco;; 0 = nenhuma.

### Síntese

Uma nova execução independente, respostas serenas sobre a sensibilidade, a divulgação aos profissionais e uma destruição deliberada de chaves completam um estudo de mestrado que outros podem verificar e usar.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 08)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Felipe Arantes, a Dra. Ingrid Solberg, a Coldwater Polytechnic, a Briarwood Health Network e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX027.** Incidentes de expiração por 100 certificados-ano, comparando a renovação manual com a ACME no geral e dentro dos grupos com dono conhecido e sem dono.

**EX028.** Primeiro, correspondências exatas do nome alternativo do titular; depois, a lista documentada de apelidos; por fim, revisão independente por duas pessoas.

**EX029.** Um balanceador de carga que termina o TLS de vários hosts e um certificado intermediário, e não folha, expirado.

**EX030.** Como incidentes de expiração do dono da cadeia, porque a validação de caminho segundo a RFC 5280 rejeita qualquer certificado expirado na cadeia.

**EX031.** Preenchidas a partir dos registros de conta do cliente ACME, quando possível; caso contrário, rotuladas como desconhecidas e relatadas como um grupo próprio.

**EX032.** Cerca de quatro minutos por chamado, então ligar cerca de 120 chamados de dois anos cabe em um mês.

**EX033.** Manual 4,26 e ACME 0,78 incidentes por 100 certificados-ano.

**EX034.** Razão de taxas 5,48 com intervalo de 95 por cento por bootstrap de 2,50 a 17,50 (semente 7, 5.000 reamostragens).

**EX035.** O denominador da razão se apoia em apenas sete incidentes ACME, então as reamostragens com pouquíssimos deles inflam a cauda superior.

**EX036.** Cerca de 9,6 entre os certificados com dono conhecido e cerca de 2,6 entre os sem dono.

**EX037.** Mais ou menos igual: os certificados ACME órfãos falham a 2,65 por 100, contra 2,69 dos manuais com dono.

**EX038.** Em quatro de cinco casos, o cliente ACME registrou erros por mais de uma semana sem que ninguém notasse; encaminhar as falhas de renovação ao monitoramento, com alertas.

**EX039.** Se apagar o parágrafo enfraqueceria a afirmação central; os parágrafos que não enfraqueceriam são movidos para os apêndices ou cortados.

**EX040.** A unidade, a exposição medida, quantos eventos ocorreram e como o intervalo foi calculado.

**EX041.** Provavelmente subconta mais os incidentes manuais, porque a equipe muitas vezes corrige as renovações manuais em minutos, sem abrir chamado, o que torna o estudo conservador.

**EX042.** Automatizar a renovação e nomear donos se apoiam em associações vistas nos dois estratos; alertar sobre falhas de renovação e revisar as dependências durante as mudanças se apoiam em evidências descritivas.

**EX043.** Como uma hipótese para pesquisas futuras, já que o estudo nunca mediu se o monitoramento do CT encontra certificados ausentes.

**EX044.** Por exemplo, que o próprio TLS é fraco e que as validades deveriam ser alongadas (e também que scripts próprios deveriam substituir clientes mantidos).

**EX045.** Ela rodou de novo a análise a partir do pacote de reprodutibilidade e enviou um relatório questionando a regra dos intermediários e o tratamento dos modos de renovação desconhecidos.

**EX046.** A razão de taxas geral passou de 5,48 para cerca de 5,2, deixando a conclusão intacta.

**EX047.** Os clientes viram a mesma falha, e a Briarwood escolheu e mantinha a cadeia que servia (além disso, a validação de caminho rejeita qualquer certificado expirado no caminho).

**EX048.** Certificados ML-DSA ou SLH-DSA maiores, cadeias híbridas e muitas mudanças de clientes aumentam as oportunidades de colisões com mudanças, tornando a propriedade e o monitoramento ainda mais importantes.

**EX049.** Automatizar a renovação onde possível, dar a cada certificado um dono nomeado e alertar sobre falhas de renovação.

**EX050.** Destruir a chave torna a religação impossível, já que os pseudônimos são tão seguros quanto sua chave, seguindo as fases do ciclo de vida de chaves do SP 800-57.

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
