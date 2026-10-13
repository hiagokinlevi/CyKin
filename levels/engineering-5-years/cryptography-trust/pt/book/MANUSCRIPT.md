# Criptografia e Serviços de Confiança: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 123, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 3 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–50 (EX031–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de engenharia que vão projetar, construir e operar serviços criptográficos de confiança para infraestruturas críticas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios existem para entender e verificar comportamentos em relação a normas e vetores de teste. Sistemas de produção usam bibliotecas avaliadas e módulos de segurança de hardware (HSMs); nunca crie sua própria criptografia. Pessoas, organizações, chaves e dispositivos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de engenharia ao longo de cinco anos enquanto ela ajuda uma companhia de saneamento a autenticar as leituras e o firmware de seus medidores inteligentes: fundamentos de matemática, física e programação; sistemas, redes e segurança; depois requisitos, modelos, ameaças, métodos, ateliês, implementação, verificação, operações, migração pós-quântica, um pipeline de revogação no projeto final, um ensaio de recuperação, um dossiê de evidências, uma tese e uma defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Aiyana Torres** | Estudante de engenharia | Inventada |
| **Marcus Webb** | Engenheiro da companhia e mentor | Inventado |
| **Halden Institute of Engineering** | Instituto fictício | Inventado |
| **Ridgeway Water Utility** | Companhia de saneamento fictícia com 50.000 medidores inteligentes | Inventada |

### Fontes principais

Katz e Lindell (3ª ed.); Boneh e Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); Menezes et al., [*Handbook of Applied Cryptography*](https://cacr.uwaterloo.ca/hac/); [FIPS 197](https://doi.org/10.6028/NIST.FIPS.197-upd1), [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4), [FIPS 186-5](https://doi.org/10.6028/NIST.FIPS.186-5), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204); [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5); [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869), [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) ler taxas de crescimento como a linguagem da força criptográfica; (2) usar logaritmos para comparar quantidades enormes; (3) estimar o tempo de busca exaustiva para diferentes tamanhos de chave.

### 1.1 O caso e por que o crescimento importa

Aiyana Torres é estudante do primeiro ano de engenharia no fictício Halden Institute of Engineering. Ao longo de cinco anos, ela vai ajudar a fictícia Ridgeway Water Utility a projetar como seus 50.000 medidores inteligentes de água autenticam as leituras e aceitam atualizações de firmware, sob a mentoria do engenheiro da companhia Marcus Webb. Todos os medidores, chaves e números deste livro são sintéticos. O cálculo começa com taxas de variação, e a criptografia depende sobretudo de uma delas: a rapidez com que cresce o trabalho de adivinhar uma chave à medida que a chave fica mais longa. O crescimento linear soma uma quantidade fixa a cada passo; o crescimento exponencial multiplica. A busca de chaves é exponencial, e essa diferença explica por que alguns bits a mais protegem tanto.

### 1.2 Logaritmos domam números enormes

Uma chave de 128 bits tem 2^128 valores possíveis, cerca de 3,4 × 10^38, um número grande demais para imaginar. Os logaritmos transformam multiplicação em soma: log10(2^128) = 128 × log10(2), aproximadamente 38,5. Aiyana aprende a comparar níveis de segurança comparando expoentes, e não os números brutos. A derivada de 2^x é ln(2) × 2^x, de modo que a própria taxa de crescimento é proporcional ao tamanho atual, a marca do comportamento exponencial. Quando os engenheiros dizem que um tamanho de chave oferece "segurança de 128 bits", querem dizer que um atacante precisa de trabalho da ordem de 2^128 operações, e Katz e Lindell usam a mesma convenção ao definir a segurança concreta.

### Laboratório — Tempo de busca exaustiva

```python
"""Exhaustive-search time for key lengths at a hypothetical 10^12 guesses per second (synthetic rate)."""
import math
RATE = 10**12
YEAR = 365.25 * 24 * 3600

def main():
    for bits in (40, 56, 80, 128):
        years = 2 ** (bits - 1) / RATE / YEAR  # expected half the space
        print(f"{bits:>3}-bit key: log10(years) = {math.log10(years):6.2f}")
    print(f"each extra bit multiplies work by {2 ** 1}; 10 extra bits by {2 ** 10}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_keyspace.py`. Saída verificada:

```text
 40-bit key: log10(years) =  -7.76
 56-bit key: log10(years) =  -2.94
 80-bit key: log10(years) =   4.28
128-bit key: log10(years) =  18.73
each extra bit multiplies work by 2; 10 extra bits by 1024
```

### 1.3 Ler a estimativa

A uma taxa hipotética de um trilhão de tentativas por segundo, uma chave de 40 bits cai numa fração de segundo (log10 dos anos em torno de -7,8), e uma chave de 56 bits, o tamanho da cifra DES, já aposentada, em cerca de um dia (log10 em torno de -2,9). Uma chave de 80 bits exige por volta de dezenove mil anos, e uma de 128 bits, cerca de 10^18,7 anos, muito mais do que a idade do universo. Cada bit a mais dobra o trabalho, e dez bits a mais o multiplicam por 1.024. Aiyana anota que a taxa é inventada e que os atacantes reais melhoram, e é por isso que normas como o AES do FIPS 197 começam em 128 bits, e não no limite do viável.

### Exemplo resolvido

Aiyana tabula os tempos de busca para 40, 56, 80 e 128 bits, compara-os por seus logaritmos de base 10 e recomenda que a Ridgeway nunca aceite chaves de medidor abaixo de 128 bits.

> **Caso sintético.** A Ridgeway, seus medidores e a taxa de tentativas são inventados; o FIPS 197 é a norma real do AES.

### Erros e limites

A busca exaustiva é apenas um ataque; uma chave longa não ajuda se for mal armazenada ou gerada a partir de uma fonte aleatória fraca. Estimativas logarítmicas são ordens de grandeza, não cronogramas.

### Exercícios

- **EX001 — Exponencial versus linear.** Por que a busca de chaves é descrita como exponencial, e não linear, no tamanho da chave? *Rubrica:* 3 = cada bit a mais dobra o número de chaves, então o trabalho se multiplica;; 2 = "cresce rápido";; 1 = resposta linear;; 0 = nenhuma.

- **EX002 — Logaritmos da busca de chaves.** Usando o laboratório, dê o logaritmo de base 10 dos anos esperados para chaves de 56 e de 128 bits. *Rubrica:* 3 = cerca de -2,94 e 18,73;; 2 = um certo;; 1 = sinal errado;; 0 = nenhuma.

- **EX003 — Por que começar em 128.** Por que Aiyana recomenda chaves de pelo menos 128 bits para os medidores? *Rubrica:* 3 = o trabalho esperado de 2^127 é inviável com margem; coincide com o mínimo do FIPS 197;; 2 = "mais seguro";; 1 = 56 bits bastam;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) calcular com aritmética modular; (2) explicar por que os inversos modulares e o pequeno teorema de Fermat importam para os sistemas de chave pública; (3) reconhecer por que exemplos de brinquedo nunca devem virar chaves reais.

### 2.1 Aritmética do relógio

A aritmética modular funciona como um relógio: os números dão a volta depois de chegar ao módulo. Dezessete horas depois das 9 horas são 2 horas, porque 26 mod 24 é igual a 2. A criptografia de chave pública vive nesse mundo. Aiyana pratica adição, multiplicação e exponenciação módulo n e aprende que o pow(b, e, n) de três argumentos do Python calcula b^e mod n com eficiência, por quadrados sucessivos, sem jamais construir o enorme número intermediário. O Handbook of Applied Cryptography, no capítulo 2, reúne essas ferramentas da teoria dos números e está disponível gratuitamente na internet, o que o torna sua referência para definições como máximo divisor comum e inverso multiplicativo.

### 2.2 Inversos e Fermat

Um número e tem inverso módulo m quando mdc(e, m) = 1; o inverso d satisfaz e × d mod m = 1, e o algoritmo de Euclides estendido o encontra. O pequeno teorema de Fermat diz que, para um primo p e um a não divisível por p, a^(p-1) mod p = 1. Junto com a generalização de Euler, esses fatos explicam por que a construção do RSA de livro-texto consegue reverter uma exponenciação com um segundo expoente. Aiyana trata isso como compreensão, e não como engenharia: a RFC 8017 mostra que o RSA real precisa de esquemas de preenchimento (padding) como o OAEP e o PSS, porque a operação crua de livro-texto vaza estrutura e é insegura.

### Laboratório — Aritmética modular de brinquedo

```python
"""Modular arithmetic facts behind public-key cryptography, on toy numbers (never a real key)."""
from math import gcd
p, q = 61, 53            # textbook-sized primes, far too small for any real use
n, phi = p * q, (p - 1) * (q - 1)
e = 17

def main():
    d = pow(e, -1, phi)  # modular inverse (Python 3.8+)
    print(f"n={n} phi={phi} gcd(e,phi)={gcd(e, phi)} d={d} (e*d mod phi = {e * d % phi})")
    m = 65
    c = pow(m, e, n)
    print(f"toy m={m} -> c={c} -> back {pow(c, d, n)}")
    print(f"Fermat check: 7^(61-1) mod 61 = {pow(7, 60, 61)}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_modular.py`. Saída verificada:

```text
n=3233 phi=3120 gcd(e,phi)=1 d=2753 (e*d mod phi = 1)
toy m=65 -> c=2790 -> back 65
Fermat check: 7^(61-1) mod 61 = 1
```

### 2.3 Ler o brinquedo

Com os primos 61 e 53, o módulo é 3233 e phi é 3120. O expoente 17 não tem fator em comum com 3120, então seu inverso existe e é igual a 2753, e 17 × 2753 mod 3120 é 1. Elevar 65 à 17ª potência dá 2790, e elevar 2790 a 2753 devolve 65. A verificação de Fermat imprime 1 para 7^60 mod 61. Aiyana escreve em vermelho nas suas anotações que esses números podem ser fatorados à mão instantaneamente, que não há preenchimento nem aleatoriedade e que a Ridgeway vai usar, em vez disso, bibliotecas avaliadas que implementam assinaturas do FIPS 186-5 ou da RFC 8032. Os módulos RSA reais têm hoje pelo menos 2048 bits, e a geração de chaves fica a cargo de bibliotecas auditadas.

### Exemplo resolvido

Aiyana calcula o inverso de 17 módulo 3120, verifica o teorema de Fermat para 7 e 61 e explica por que a mesma aritmética com números de tamanho real ainda precisa do preenchimento padronizado.

> **Caso sintético.** Os primos e a mensagem são brinquedos de livro-texto; a RFC 8017 e o FIPS 186-5 são as normas reais.

### Erros e limites

O RSA de brinquedo é um recurso didático. Copiá-lo para um software, mesmo com primos grandes, produz um sistema inseguro, sem preenchimento, sem cuidado com canais laterais e sem geração de chaves avaliada.

### Exercícios

- **EX004 — Condição do inverso.** Quando existe um inverso de e módulo m? *Rubrica:* 3 = quando mdc(e, m) = 1;; 2 = coprimos dito de forma vaga;; 1 = sempre;; 0 = nenhuma.

- **EX005 — Valores do brinquedo.** A partir do laboratório, dê d e o texto cifrado de 65. *Rubrica:* 3 = d = 2753, c = 2790;; 2 = um;; 1 = outros números;; 0 = nenhuma.

- **EX006 — Por que o preenchimento.** Por que o RSA de livro-texto é inseguro mesmo com primos grandes? *Rubrica:* 3 = sem preenchimento nem aleatoriedade, vaza estrutura; a RFC 8017 exige OAEP/PSS;; 2 = "simples demais";; 1 = é seguro;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar sinais físicos ao vazamento de informação; (2) explicar canais laterais, como tempo e consumo de energia; (3) ligar a aleatoriedade física à geração de chaves.

### 3.1 A computação é física

Toda computação consome corrente, leva tempo e emite calor e radiação eletromagnética. A disciplina de física de Aiyana liga isso à segurança: um medidor que processa uma chave secreta pode vazar informação pelo tempo que uma operação leva ou pela energia que consome. Esses vazamentos são chamados de canais laterais. Eles importam porque os medidores da Ridgeway ficam em porões e em caixas na calçada, onde um atacante poderia conectar sondas. Um algoritmo matematicamente forte pode ser quebrado na prática se sua implementação vazar bits da chave pela física, e é por isso que organismos de normalização e fabricantes testam implementações, e não apenas projetos.

### 3.2 Tempo e energia

Um canal lateral de tempo aparece quando o tempo de execução depende de dados secretos, por exemplo numa comparação que para no primeiro byte errado. Medir muitas tentativas pode revelar quantos bytes iniciais estavam certos. A análise de consumo de energia registra a corrente consumida durante operações criptográficas; diferenças entre processar um bit 0 e um bit 1 podem, com estatística, revelar chaves. As defesas incluem código de tempo constante, mascaramento e hardware projetado para resistir à análise. Aiyana aprende que o hmac.compare_digest do Python existe justamente para que a comparação de tags de autenticação leve o mesmo tempo, não importa onde elas difiram.

### 3.3 Aleatoriedade física

As chaves precisam ser imprevisíveis, e a imprevisibilidade vem, em última instância, de ruído físico, como flutuações térmicas ou o jitter de osciladores. Fontes de entropia de hardware alimentam geradores determinísticos de bits aleatórios, especificados no NIST SP 800-90A, que expandem uma semente pequena e bem medida em muitos bits imprevisíveis. Um medidor que inicializa sempre no mesmo estado, sem boa entropia, pode produzir as mesmas chaves que milhares de outros medidores. Aiyana anota que os sistemas operacionais expõem geradores avaliados, e que o módulo secrets do Python os usa, de modo que os engenheiros nunca devem inventar suas próprias rotinas de números aleatórios para chaves.

### Exemplo resolvido

Aiyana lista três vazamentos físicos de um medidor instalado numa caixa na calçada (tempo, energia, emissão eletromagnética) e associa cada um a uma defesa: comparação em tempo constante, hardware mascarado e blindagem, além de entropia avaliada para a geração de chaves.

> **Caso sintético.** A instalação dos medidores é inventada; o SP 800-90A é a recomendação real do NIST.

### Erros e limites

A resistência a canais laterais não pode ser confirmada apenas lendo o código; ela exige medições no dispositivo real. A entropia física pode falhar silenciosamente, então os geradores precisam de testes de saúde.

### Exercícios

- **EX007 — Canal lateral definido.** O que é um canal lateral? *Rubrica:* 3 = informação vazada por efeitos físicos, como tempo ou energia, e não pelas saídas do algoritmo;; 2 = "ataque físico";; 1 = ataque de rede;; 0 = nenhuma.

- **EX008 — Comparação com saída antecipada.** Por que uma comparação byte a byte que para cedo vaza segredos? *Rubrica:* 3 = o tempo revela quantos bytes iniciais coincidiram;; 2 = mais lenta;; 1 = não vaza;; 0 = nenhuma.

- **EX009 — Papel do SP 800-90A.** O que o SP 800-90A especifica, e por que isso importa para os medidores? *Rubrica:* 3 = geradores determinísticos de bits aleatórios semeados por entropia, para que os medidores não produzam chaves idênticas;; 2 = aleatoriedade;; 1 = cifração;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) representar corretamente bytes, texto e hexadecimal; (2) usar as funções de hash da biblioteca padrão; (3) evitar erros comuns de codificação que quebram verificações criptográficas.

### 4.1 Bytes não são texto

As funções criptográficas operam sobre bytes, e não sobre caracteres. Em Python, "litres" é texto e b"litres" são bytes; converter entre os dois exige uma codificação explícita, como UTF-8. O primeiro bug de Aiyana vem de calcular o hash de uma leitura num sistema com uma codificação diferente da de outro, de modo que leituras iguais produziram digests diferentes. Ela aprende a fixar uma codificação canônica na especificação, a converter uma única vez na fronteira e a manter bytes em todo o interior. O hexadecimal é um formato de exibição de bytes: dois caracteres hexadecimais representam um byte, e é por isso que um digest SHA-256 de 32 bytes é impresso com 64 caracteres.

### 4.2 Usar o hashlib

O módulo hashlib oferece o SHA-256 e outras funções do FIPS 180-4. Um hash leva uma entrada de qualquer tamanho a um digest de tamanho fixo; mudar um bit muda cerca de metade dos bits da saída. Aiyana escreve pequenas funções que calculam o hash de uma string de leitura e imprimem o digest hexadecimal e depois confere vetores de teste publicados na norma para confirmar que está chamando a função corretamente. Ela aprende a diferença entre chamar update repetidamente num objeto de hash, o que calcula o hash da concatenação, e calcular o hash de cada pedaço separadamente, o que dá resultados diferentes que confundiram seu primeiro teste.

### 4.3 Formatos canônicos

Dois programas precisam concordar byte a byte antes que hashes ou assinaturas possam coincidir. Aiyana define um formato canônico de leitura para a Ridgeway: ordem fixa dos campos, separadores de ponto e vírgula, litros inteiros e timestamps em UTC com um Z no final. Ela evita litros em ponto flutuante, porque 18342.0 e 18342 teriam hashes diferentes. Ela também evita que a ordem de impressão de um dicionário defina os bytes. Essa disciplina antecipa os capítulos seguintes, em que as leituras são autenticadas com HMAC e o firmware com assinaturas; ambos falham, sem causar dano, mas de modo confuso, se o emissor e o receptor discordarem sobre os bytes exatos.

### Exemplo resolvido

Aiyana corrige um teste que falhava codificando as leituras em UTF-8 uma única vez, usando litros inteiros e timestamps em UTC, e depois confirma suas chamadas ao SHA-256 contra um vetor de teste do FIPS 180-4.

> **Caso sintético.** O formato de leitura foi inventado para a Ridgeway; o FIPS 180-4 é real.

### Erros e limites

Hash não é cifração: qualquer pessoa pode calcular um digest. Misturar texto e bytes muda os resultados silenciosamente, então especifique as codificações explicitamente.

### Exercícios

- **EX010 — Tamanho em hexadecimal.** Por que um digest SHA-256 é impresso com 64 caracteres hexadecimais? *Rubrica:* 3 = 32 bytes, dois caracteres hexadecimais por byte;; 2 = 64 bytes;; 1 = aleatório;; 0 = nenhuma.

- **EX011 — Bug de codificação.** O que causou os primeiros digests divergentes de Aiyana? *Rubrica:* 3 = codificações de texto diferentes em dois sistemas para leituras iguais;; 2 = codificação mencionada;; 1 = algoritmo errado;; 0 = nenhuma.

- **EX012 — Litros inteiros.** Por que o formato canônico usa litros inteiros? *Rubrica:* 3 = 18342.0 e 18342 produzem bytes e digests diferentes;; 2 = floats são imprecisos;; 1 = estilo;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) explicar decisões criptográficas para não especialistas; (2) escrever um registro de decisão para uma escolha de gerenciamento de chaves; (3) evitar linguagem de segurança enganosa.

### 5.1 Escrever para o conselho

O conselho da Ridgeway inclui um agricultor, uma enfermeira aposentada e um contador. Aiyana precisa explicar por que os medidores precisam de leituras autenticadas. Ela começa pela decisão necessária, aprovar um orçamento para as chaves dos medidores, e depois enuncia o risco em palavras simples: sem autenticação, alguém poderia alterar as leituras e as contas. Ela define o jargão uma única vez: um código de autenticação de mensagem é uma tag curta que prova que uma leitura veio do medidor e não foi alterada. Marcus Webb lhe diz que o conselho não precisa da matemática, mas precisa saber o que pode dar errado e quanto custa evitar.

### 5.2 Linguagem de segurança honesta

Aiyana evita palavras como "inquebrável" ou "de nível militar", que prometem mais do que qualquer engenheiro pode entregar. Em vez disso, escreve que o HMAC-SHA256, especificado na RFC 2104 e no FIPS 198-1, é amplamente revisado e não tem ataques práticos conhecidos quando as chaves estão protegidas, e que o principal risco é o manuseio das chaves, e não o algoritmo. Ela lista o que o controle não faz: ele não esconde as leituras de quem escuta a comunicação, o que exigiria cifração. Afirmações precisas protegem a companhia quando auditores ou jornalistas perguntarem, mais tarde, o que foi prometido e por quê.

### 5.3 Registros de decisão

Aiyana escreve um registro de decisão para a primeira grande escolha: uma chave de autenticação única por medidor, derivada de uma chave mestra no serviço de chaves da companhia, em vez de uma chave compartilhada por todos os medidores. O registro informa contexto, opções, decisão, consequências, data e aprovador. Sua consequência principal é explícita: roubar a chave de um medidor permite a um atacante forjar apenas as leituras daquele medidor, e não as da frota inteira. Anos depois, quando um prestador de serviços propõe uma chave compartilhada para simplificar o provisionamento, o registro explica em dois minutos por que essa opção foi rejeitada.

### Exemplo resolvido

A nota de uma página de Aiyana para o conselho pede um orçamento para o serviço de chaves, explica as leituras forjadas em palavras simples, evita "inquebrável" e remete a um registro de decisão que escolhe chaves por medidor.

> **Caso sintético.** O conselho e a decisão são inventados; a RFC 2104 e o FIPS 198-1 são reais.

### Erros e limites

Simplificar demais pode enganar: dizer "cifrado" quando os dados estão apenas autenticados é um erro factual. Registros sem as opções rejeitadas perdem metade do seu valor.

### Exercícios

- **EX013 — Abertura da nota ao conselho.** Como Aiyana abre sua nota ao conselho? *Rubrica:* 3 = com a decisão necessária (orçamento para as chaves dos medidores) e depois o risco em linguagem simples;; 2 = risco primeiro;; 1 = jargão;; 0 = nenhuma.

- **EX014 — O que o HMAC não faz.** O que a nota diz que o HMAC não oferece? *Rubrica:* 3 = confidencialidade; as leituras não ficam ocultas, seria preciso cifração;; 2 = sigilo;; 1 = tudo;; 0 = nenhuma.

- **EX015 — Chaves por medidor.** Que consequência das chaves por medidor o registro destaca? *Rubrica:* 3 = roubar a chave de um medidor só permite forjar aquele medidor, não a frota;; 2 = limita o dano;; 1 = mais barato;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar séries e limites para raciocinar sobre risco acumulado; (2) modelar a probabilidade de falha ao longo de muitas tentativas; (3) aplicar a aproximação 1 - e^-x a eventos de segurança.

### 6.1 Acumular riscos pequenos

Um único evento de probabilidade minúscula torna-se provável quando repetido vezes suficientes. Se cada uma de n tentativas independentes falha com probabilidade p, a chance de nenhuma falhar é (1 - p)^n. O Cálculo II dá a Aiyana a ferramenta para simplificar isso: para p pequeno, (1 - p)^n fica próximo de e^(-np), um limite que ela deduz da série da função exponencial. Essa aproximação aparece o tempo todo em criptografia, das colisões de nonces à reutilização aleatória de chaves, porque os engenheiros repetem operações bilhões de vezes. Um risco de um em um bilhão por operação não é pequeno para uma frota que realiza dez bilhões de operações.

### 6.2 Séries e a exponencial

A função exponencial pode ser escrita como uma série infinita, 1 + x + x²/2 + x³/6 e assim por diante. Para x pequeno, os dois primeiros termos dominam, e é por isso que 1 - e^(-x) é aproximadamente x quando x é minúsculo. O math.expm1 do Python calcula e^x - 1 com precisão mesmo para x muito pequeno, evitando o erro de arredondamento de subtrair números quase iguais. Aiyana descobre isso do jeito difícil quando seu cálculo ingênuo de 1 - exp(-1e-18) imprime zero. Ela passa a usar -expm1(-x) e obtém a probabilidade minúscula correta, uma lição de cuidado numérico.

### 6.3 Aplicar à Ridgeway

Suponha que um firmware defeituoso de medidor escolha um identificador aleatório de 32 bits para cada sessão e que o servidor confunda as sessões se dois identificadores coincidirem. Com muitas sessões, a chance de colisão cresce aproximadamente como o quadrado do número de sessões dividido pelo dobro do espaço, o efeito do aniversário que o Capítulo 7 desenvolve. Aiyana usa a aproximação exponencial para mostrar ao conselho que um projeto aceitável para um piloto com cem medidores falha com cinquenta mil. O cálculo lhe diz quando o "raro" deixa de ser raro, o que orienta quantos bits os identificadores e os nonces precisam ter.

### Exemplo resolvido

Aiyana deduz (1 - p)^n ≈ e^(-np), corrige um bug de arredondamento com math.expm1 e mostra que um identificador por sessão seguro para um piloto é inseguro em escala completa.

> **Caso sintético.** O projeto do identificador é inventado; a matemática é padrão.

### Erros e limites

A aproximação supõe independência e p pequeno; falhas correlacionadas, como uma semente aleatória ruim compartilhada, a quebram gravemente. A subtração em ponto flutuante de números quase iguais perde precisão.

### Exercícios

- **EX016 — Aproximação pelo limite.** Que aproximação Aiyana usa para (1 - p)^n quando p é pequeno? *Rubrica:* 3 = e^(-np);; 2 = exponencial;; 1 = np exatamente;; 0 = nenhuma.

- **EX017 — Correção com expm1.** Por que 1 - exp(-1e-18) imprimiu zero, e o que corrigiu isso? *Rubrica:* 3 = arredondamento ao subtrair números quase iguais; usar -math.expm1(-x);; 2 = arredondamento;; 1 = fórmula errada;; 0 = nenhuma.

- **EX018 — Falha correlacionada.** Quando a hipótese de independência falha gravemente? *Rubrica:* 3 = falhas correlacionadas, como uma semente aleatória ruim compartilhada entre medidores;; 2 = correlação;; 1 = nunca;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) aplicar o limite do aniversário a colisões; (2) escolher tamanhos de tags e identificadores a partir de metas de colisão; (3) interpretar afirmações probabilísticas nas normas.

### 7.1 O problema do aniversário

Numa sala com 23 pessoas, a chance de duas fazerem aniversário no mesmo dia passa de metade, embora o ano tenha 365 dias. O motivo é que o número de pares cresce com o quadrado do número de pessoas. Para valores aleatórios de um espaço de tamanho N, as colisões se tornam prováveis depois de cerca da raiz quadrada de N sorteios. Para um valor de n bits, isso dá cerca de 2^(n/2). Katz e Lindell usam esse limite para explicar por que uma função de hash com saída de n bits oferece apenas cerca de n/2 bits de resistência a colisões, e é por isso que se diz que o SHA-256 dá segurança de 128 bits contra colisões.

### Laboratório — Probabilidade de colisão

```python
"""Birthday bound: chance two of k random n-bit tags collide (approximation)."""
import math

def p(k, bits):
    return -math.expm1(-k * (k - 1) / 2 ** (bits + 1))

def main():
    for bits in (32, 64, 128):
        k = 2 ** (bits // 2)
        print(f"{bits:>3}-bit tags, k=2^{bits // 2}: P(collision) = {p(k, bits):.3f}")
    print(f"meters 50,000 with 32-bit ids: P = {p(50_000, 32):.3f}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_birthday.py`. Saída verificada:

```text
 32-bit tags, k=2^16: P(collision) = 0.393
 64-bit tags, k=2^32: P(collision) = 0.393
128-bit tags, k=2^64: P(collision) = 0.393
meters 50,000 with 32-bit ids: P = 0.253
```

### 7.2 Ler os resultados

Para cada tamanho de tag, sortear 2^(n/2) valores aleatórios dá uma probabilidade de colisão de cerca de 0,393, a mesma para 32, 64 e 128 bits. Essa constante mostra exatamente a regra da raiz quadrada. Na prática, dar identificadores aleatórios de 32 bits a 50.000 medidores produz uma chance de cerca de 25 por cento de dois compartilharem um identificador. Aiyana recomenda que a Ridgeway atribua os identificadores sequencialmente a partir de um registro, e não ao acaso, e que todo valor aleatório cuja unicidade importe, como um nonce, use pelo menos 96 bits, como faz o GCM, com contagem e rotação, como exige o SP 800-38D.

### 7.3 Interpretar afirmações probabilísticas

As normas frequentemente enunciam a segurança como um limite de probabilidade para um atacante que faz certo número de consultas. Aiyana aprende a fazer três perguntas a qualquer afirmação desse tipo: o que o atacante pode fazer, quantas operações são contadas e que evento conta como falha. Uma afirmação de falha 2^-32 depois de 2^32 mensagens é muito diferente de 2^-32 por mensagem. Ela também aprende que as estatísticas de sistemas reais raramente coincidem com a aleatoriedade ideal, de modo que os engenheiros medem, por exemplo verificando nos logs de produção se há nonces duplicados, em vez de confiar apenas no limite teórico.

### Exemplo resolvido

Aiyana calcula uma chance de colisão de 25 por cento para 50.000 identificadores aleatórios de 32 bits e recomenda identificadores atribuídos por registro e nonces contados de 96 bits.

> **Caso sintético.** O tamanho da frota é inventado; o SP 800-38D é real.

### Erros e limites

O limite do aniversário supõe aleatoriedade uniforme; geradores enviesados colidem mais cedo. Os limites de probabilidade dependem da unidade contada, então leia-os com cuidado.

### Exercícios

- **EX019 — Regra da raiz quadrada.** Depois de aproximadamente quantos sorteios valores aleatórios de n bits começam a colidir? *Rubrica:* 3 = cerca de 2^(n/2);; 2 = raiz quadrada mencionada;; 1 = 2^n;; 0 = nenhuma.

- **EX020 — Identificadores dos medidores.** Que chance de colisão o laboratório deu para 50.000 medidores com identificadores de 32 bits, e que correção se seguiu? *Rubrica:* 3 = cerca de 0,253; identificadores atribuídos por registro;; 2 = só o número;; 1 = só a correção;; 0 = nenhuma.

- **EX021 — Ler um limite.** Cite as três perguntas que Aiyana faz a uma afirmação probabilística. *Rubrica:* 3 = capacidades do atacante, operações contadas, evento de falha;; 2 = duas;; 1 = uma;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) descrever como os processadores aceleram a criptografia; (2) explicar os caches como fonte de vazamento; (3) avaliar elementos seguros para armazenar as chaves dos medidores.

### 8.1 Suporte de hardware à criptografia

Os processadores modernos incluem instruções que aceleram o AES e o SHA-2 diretamente no hardware, o que torna a cifração rápida e também ajuda a resistir a vazamentos de tempo, porque o hardware executa em tempo constante, quaisquer que sejam os valores da chave. Aiyana compara os processadores dos servidores da Ridgeway, que têm essas instruções, com os pequenos microcontroladores dos medidores, que podem não ter. Num microcontrolador, o AES em software precisa ser escrito com cuidado para evitar consultas a tabelas que dependam de dados secretos. Esse detalhe de arquitetura afeta quais algoritmos a Ridgeway seleciona para os medidores e por que ela prefere fornecedores cujas bibliotecas documentam o comportamento em tempo constante.

### 8.2 Caches e vazamento

Os caches tornam o acesso à memória mais rápido ao manter os dados usados recentemente perto do processador. Como o tempo de acesso depende de os dados estarem ou não no cache, um programa cujos acessos à memória dependem de segredos pode vazar esses segredos para outro programa que compartilha o cache. As implementações clássicas do AES baseadas em tabelas tinham essa fraqueza. Aiyana aprende que é por isso que os servidores em nuvem isolam cargas de trabalho sensíveis e que as instruções de hardware substituíram as tabelas de consulta. Para os servidores da Ridgeway, ela recomenda executar o serviço de chaves em hosts dedicados, e não em máquinas virtuais compartilhadas, um custo considerado justificável para as chaves mais sensíveis.

### 8.3 Elementos seguros

Um elemento seguro é um pequeno chip resistente a violação que armazena chaves e realiza operações criptográficas internamente, de modo que a chave nunca aparece na memória principal do medidor. Ele resiste a sondagem e a ataques de canal lateral melhor do que um microcontrolador comum. Aiyana compara três projetos de medidor: chave na memória flash, chave numa região protegida do microcontrolador e chave dentro de um elemento seguro. O elemento seguro custa mais por medidor, mas significa que abrir um medidor e extrair sua memória não revela a chave dele. Ela registra o trade-off e o risco residual que permanece mesmo com a resistência a violação.

### Exemplo resolvido

Aiyana recomenda elementos seguros para as chaves dos medidores, AES em hardware nos servidores e hosts dedicados para o serviço de chaves, com os custos e os riscos residuais registrados.

> **Caso sintético.** Os projetos de medidor e os custos são inventados.

### Erros e limites

A resistência a violação aumenta o custo do atacante, mas não é absoluta. A aceleração por hardware não corrige usos indevidos, como a reutilização de nonces.

### Exercícios

- **EX022 — Benefício do AES em hardware.** Cite dois benefícios das instruções de AES em hardware. *Rubrica:* 3 = velocidade e execução em tempo constante, que resiste a vazamentos de tempo;; 2 = um;; 1 = nenhum;; 0 = nenhuma.

- **EX023 — Vazamento pelo cache.** Como um cache pode vazar segredos? *Rubrica:* 3 = o tempo de acesso depende dos dados em cache; acessos dependentes de segredos revelam chaves a um programa que compartilha a máquina;; 2 = tempo mencionado;; 1 = não vaza;; 0 = nenhuma.

- **EX024 — Valor do elemento seguro.** O que um elemento seguro impede, em comparação com chaves na flash? *Rubrica:* 3 = extrair a memória de um medidor aberto não revela sua chave;; 2 = protege a chave;; 1 = cifra os dados;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar código que chama bibliotecas criptográficas com segurança; (2) tratar erros sem vazar informação; (3) testar código criptográfico com testes de resposta conhecida e testes negativos.

### 9.1 Encapsular bibliotecas com segurança

Aiyana escreve um pequeno módulo que o serviço de leitura dos medidores vai chamar para a autenticação. Ele expõe duas funções, gerar a tag de uma leitura e verificar uma leitura, e esconde internamente todo o manuseio de chaves e as escolhas de algoritmos. Quem chama não pode escolher algoritmos nem passar chaves brutas. Esse padrão de encapsulamento (wrapper) reduz o uso indevido: os desenvolvedores não podem usar por acidente um hash fraco nem comparar tags com a igualdade comum. Marcus lembra a ela que o wrapper delega ao hmac e ao hashlib da biblioteca padrão, que implementam a RFC 2104 e o FIPS 180-4, em vez de reimplementar qualquer primitiva.

### 9.2 Erros que não vazam

Quando a verificação falha, o serviço não deve dizer a quem chamou o motivo, por exemplo se o identificador do medidor era desconhecido ou se a tag estava errada, porque erros detalhados ajudam os atacantes a sondar o sistema. A função de verificação de Aiyana devolve a quem chama apenas verdadeiro ou falso e escreve o motivo detalhado num log protegido. Ela também garante que as exceções nunca incluam material de chave nem leituras completas em suas mensagens. Essas regras refletem um princípio mais amplo: em código de segurança, a conveniência para a depuração não pode virar informação para os atacantes.

### 9.3 Testar código criptográfico

Aiyana escreve três tipos de teste. Os testes de resposta conhecida conferem seu wrapper contra vetores publicados, como os valores da RFC 4231 para o HMAC-SHA256, confirmando o uso correto. Os testes negativos conferem que uma leitura alterada, uma chave errada ou uma tag truncada falham. Os testes de propriedade geram muitas leituras aleatórias e confirmam que gerar a tag e depois verificar sempre dá certo. Ela aprende que os testes negativos muitas vezes faltam na prática, de modo que uma função de verificação que sempre devolve verdadeiro poderia passar em todos os testes positivos. Sua suíte de testes roda a cada mudança, na integração contínua.

### Exemplo resolvido

O wrapper de Aiyana expõe apenas a geração de tag e a verificação, devolve apenas verdadeiro ou falso, registra os detalhes de forma privada e passa nos testes de resposta conhecida, negativos e de propriedade.

> **Caso sintético.** O serviço e o wrapper são inventados; a RFC 2104 e o FIPS 180-4 são reais.

### Erros e limites

Wrappers podem esconder bugs tanto quanto complexidade; eles precisam ser revisados e testados. Uma suíte de testes sem casos negativos não consegue pegar um verificador que aceita tudo.

### Exercícios

- **EX025 — Benefício do wrapper.** Como o wrapper reduz o uso indevido? *Rubrica:* 3 = quem chama não pode escolher algoritmos, passar chaves brutas nem comparar tags de forma insegura;; 2 = esconde detalhes;; 1 = mais rápido;; 0 = nenhuma.

- **EX026 — Falha silenciosa.** Por que a verificação devolve apenas verdadeiro ou falso a quem chama? *Rubrica:* 3 = motivos detalhados ajudam atacantes a sondar; os detalhes vão para logs protegidos;; 2 = segurança;; 1 = mais simples;; 0 = nenhuma.

- **EX027 — Testes negativos ausentes.** Contra que perigo os testes negativos protegem? *Rubrica:* 3 = um verificador que sempre devolve verdadeiro passar em todos os testes positivos;; 2 = bugs;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética da engenharia a sistemas criptográficos em infraestruturas críticas; (2) tratar com responsabilidade as fraquezas descobertas; (3) pesar a segurança física e operacional (safety) contra a segurança contra ataques (security).

### 10.1 Dever para com o público

Os códigos de ética da engenharia colocam a segurança do público em primeiro lugar. Para uma companhia de saneamento, essa segurança inclui água confiável e contas corretas e também não cortar o abastecimento porque um controle de segurança falhou. Aiyana considera um projeto em que os medidores se recusam a reportar se a assinatura do firmware não puder ser verificada. Isso protege contra adulteração, mas poderia deixar a companhia cega para vazamentos se um certificado expirar. Ela aprende que os engenheiros precisam pensar nos modos de falha dos próprios controles de segurança, porque um controle que falha de forma perigosa pode prejudicar o público que deveria proteger.

### 10.2 Divulgação responsável

Durante testes numa bancada de laboratório, Aiyana percebe que o medidor de um fornecedor aceita firmware sem verificar a assinatura quando a bateria está fraca. Ela relata o problema a Marcus, que o relata ao fornecedor pelo processo de divulgação coordenada da Ridgeway, dando ao fornecedor tempo para corrigi-lo antes que os detalhes sejam compartilhados. Ela não publica nada sobre isso nem o testa em medidores instalados. A prática ética significa relatar as fraquezas a quem pode corrigi-las, manter os detalhes confidenciais até a correção e nunca explorá-las, nem mesmo para provar um argumento.

### 10.3 Trade-offs entre safety e security

Aiyana escreve uma análise curta do caso da bateria fraca e do caso da expiração. Para cada um, ela lista o que acontece se o controle falhar aberto, aceitando qualquer coisa, e se falhar fechado, recusando tudo. Para as atualizações de firmware, falhar fechado é o certo: um medidor deve manter seu firmware atual em vez de instalar código não verificado. Para o envio das leituras, falhar fechado prejudicaria os clientes, então os medidores continuam reportando enquanto emitem um alerta. Registrar essas escolhas por escrito permite que as equipes de safety e de security da companhia entrem em acordo com antecedência, em vez de discutirem durante um incidente.

### Exemplo resolvido

Aiyana relata, por divulgação coordenada, uma forma de contornar a assinatura com bateria fraca e escreve uma tabela de falha aberta versus falha fechada para as atualizações de firmware e para as leituras.

> **Caso sintético.** A falha do fornecedor é inventada para fins didáticos.

### Erros e limites

Tratar todo controle de segurança como falha fechada pode criar riscos à segurança das pessoas; tratar todos como falha aberta convida ataques. A divulgação sem coordenação pode prejudicar os usuários.

### Exercícios

- **EX028 — Risco da expiração.** Que risco à segurança das pessoas Aiyana viu em recusar o envio quando a assinatura falha? *Rubrica:* 3 = a companhia fica cega para vazamentos se um certificado expirar;; 2 = indisponibilidade;; 1 = nenhum;; 0 = nenhuma.

- **EX029 — Caminho da divulgação.** Como foi tratada a falha da bateria fraca? *Rubrica:* 3 = relatada a Marcus e ao fornecedor por divulgação coordenada, mantida confidencial, não testada em medidores em operação;; 2 = relatada;; 1 = publicada abertamente;; 0 = nenhuma.

- **EX030 — Modo de falha do firmware.** A verificação do firmware deve falhar aberta ou fechada, e por quê? *Rubrica:* 3 = fechada: manter o firmware atual em vez de instalar código não verificado;; 2 = fechada;; 1 = aberta;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Aiyana Torres, Marcus Webb, o Halden Institute of Engineering, a Ridgeway Water Utility e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Cada bit acrescentado dobra o espaço de chaves, então o trabalho se multiplica, em vez de aumentar num passo fixo.

**EX002.** Aproximadamente -2,94 para 56 bits (cerca de um dia) e 18,73 para 128 bits.

**EX003.** Um trabalho esperado de 2^127 tentativas está muito além de qualquer atacante previsível, deixando margem para melhorias, e o AES do FIPS 197 começa em 128 bits.

**EX004.** Exatamente quando e e m não têm fator comum, isto é, mdc(e, m) = 1.

**EX005.** O inverso é 2753, e 65 é cifrado como 2790, que é decifrado de volta para 65.

**EX006.** Sem o preenchimento aleatorizado exigido pela RFC 8017 (OAEP ou PSS), o RSA determinístico de livro-texto vaza estrutura e permite ataques.

**EX007.** Vazamento de informação secreta pelo comportamento físico, como tempo, energia ou emissões, e não pelas saídas previstas.

**EX008.** Seu tempo de execução revela quantos bytes iniciais estavam certos, permitindo que um atacante adivinhe as tags byte a byte.

**EX009.** Geradores determinísticos de bits aleatórios que expandem uma entropia bem semeada, impedindo que os medidores inicializem com chaves idênticas e previsíveis.

**EX010.** O digest tem 32 bytes, e cada byte é escrito como dois caracteres hexadecimais.

**EX011.** Os dois sistemas codificaram o mesmo texto de leitura com codificações diferentes, então os bytes do hash eram diferentes.

**EX012.** Representações em ponto flutuante como 18342.0 e 18342 são sequências de bytes diferentes e nunca teriam o mesmo hash nem passariam na mesma verificação.

**EX013.** Com a decisão de que ela precisa, aprovar um orçamento para as chaves, seguida do risco de leituras alteradas em palavras simples.

**EX014.** Ele não esconde as leituras de quem escuta a comunicação; a confidencialidade exigiria cifração.

**EX015.** Uma chave roubada só permite forjar as leituras daquele medidor, em vez das de todos os medidores.

**EX016.** (1 - p)^n é aproximadamente e^(-np) para p pequeno.

**EX017.** Subtrair dois números em ponto flutuante quase iguais perdeu toda a precisão; -math.expm1(-x) calcula o resultado minúsculo com exatidão.

**EX018.** Quando as falhas são correlacionadas, por exemplo se muitos medidores compartilham a mesma semente aleatória fraca.

**EX019.** Por volta de 2^(n/2) sorteios, a raiz quadrada do espaço.

**EX020.** Cerca de 25,3 por cento; Aiyana recomenda atribuir os identificadores sequencialmente a partir de um registro.

**EX021.** O que o atacante pode fazer, quantas operações são contadas e que evento é definido como falha.

**EX022.** Elas tornam o AES rápido e executam em tempo constante, o que evita um tempo dependente de segredos.

**EX023.** Quando os padrões de acesso à memória dependem de segredos, outro programa que compartilha o cache pode medir diferenças de tempo e deduzi-los.

**EX024.** A chave nunca sai do chip, então abrir um medidor e extrair sua memória não expõe a chave.

**EX025.** Quem chama não pode escolher algoritmos, manusear chaves nem comparar tags por conta própria, o que elimina erros comuns.

**EX026.** Motivos de erro específicos ajudariam os atacantes a sondar o sistema, então os detalhes vão apenas para um log protegido.

**EX027.** Sem testes negativos, um verificador que aceita tudo ainda passaria na suíte de testes.

**EX028.** Se um certificado expirasse, os medidores parariam de reportar, e a companhia poderia deixar de perceber vazamentos.

**EX029.** Foi para Marcus e depois para o fornecedor por divulgação coordenada, ficou confidencial até a correção e nunca foi testada em medidores instalados.

**EX030.** Fechada, porque manter um firmware conhecido é mais seguro do que executar código não verificado.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barker, E., & Roginsky, A. (2019). *Transitioning the use of cryptographic algorithms and key lengths* (NIST SP 800-131A Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-131Ar2>
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
- Nystrom, M. (2005). *Identifiers and test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512* (RFC 4231). IETF. <https://www.rfc-editor.org/rfc/rfc4231>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Shoup, V. (2004). *Sequences of games: A tool for taming complexity in security proofs* (Cryptology ePrint Archive, Paper 2004/332). <https://eprint.iacr.org/2004/332>
