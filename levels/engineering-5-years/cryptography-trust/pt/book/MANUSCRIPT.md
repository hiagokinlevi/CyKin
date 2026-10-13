# Criptografia e Serviços de Confiança: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 123, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–50 de 50 têm texto didático escrito à mão; os exercícios EX001–EX150 têm resoluções correspondentes com rubricas de 0 a 3; os oito laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

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

### Síntese

O cálculo dá aos engenheiros o vocabulário do crescimento; espaços de chaves exponenciais, comparados por meio de logaritmos, explicam por que as chaves modernas começam em 128 bits.

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

### Síntese

A aritmética modular, os inversos e o teorema de Fermat explicam a matemática da chave pública, mas os sistemas reais dependem de esquemas padronizados e de bibliotecas avaliadas.

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

### Síntese

A criptografia roda em dispositivos físicos; o tempo, o consumo de energia e a entropia determinam se um algoritmo sólido continua seguro num medidor instalado num porão.

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

### Síntese

A programação criptográfica correta começa com bytes, codificações explícitas, vetores de teste verificados e um formato canônico com que os dois lados concordam.

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

### Síntese

Uma comunicação clara e honesta e registros de decisão tornam as escolhas criptográficas compreensíveis para quem decide e duráveis diante das mudanças na equipe.

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

### Síntese

As séries e os limites explicam como riscos minúsculos por operação se acumulam em escala, e uma numérica cuidadosa mantém essas estimativas honestas.

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

### Síntese

O limite do aniversário transforma o risco de colisão em requisitos de tamanho em bits, e a leitura cuidadosa das afirmações probabilísticas evita um falso conforto.

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

### Síntese

A arquitetura molda a segurança criptográfica: instruções de hardware, o comportamento do cache e os elementos seguros decidem quão bem as chaves sobrevivem em dispositivos reais.

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

### Síntese

A programação criptográfica segura encapsula bibliotecas avaliadas, revela pouco nas falhas e comprova o comportamento com testes positivos e negativos.

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

### Síntese

A engenharia criptográfica ética protege o público ao planejar como os controles falham e ao divulgar as fraquezas de forma responsável.

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) rastrear como os dados dos medidores atravessam as redes; (2) explicar o que o TLS 1.3 protege e o que não protege; (3) escolher onde autenticar e onde cifrar.

### 11.1 O caminho de uma leitura

Uma leitura sai de um medidor por um enlace de rádio de baixa potência até um concentrador do bairro, segue por uma rede celular até o gateway da Ridgeway e depois atravessa a rede interna da companhia até o banco de dados de faturamento. Aiyana desenha cada salto e pergunta quem poderia ler ou modificar os dados ali: alguém escutando o rádio por perto, a operadora celular, um insider na rede interna. Cada salto tem atacantes diferentes. Desenhar o caminho primeiro evita um erro comum, proteger fortemente um enlace e deixar outro aberto, e mostra onde uma proteção fim a fim, do medidor ao banco de dados, eliminaria a dependência dos saltos intermediários.

### 11.2 O que o TLS 1.3 oferece

Entre o concentrador e o gateway, a Ridgeway usa o TLS 1.3, especificado na RFC 8446. O TLS oferece confidencialidade, integridade e autenticação do servidor para a conexão, usando uma troca de chaves efêmera, como o X25519 da RFC 7748, de modo que o tráfego gravado não possa ser decifrado depois, mesmo que as chaves de longo prazo vazem, uma propriedade chamada sigilo futuro (forward secrecy). Aiyana anota o que o TLS não faz: ele protege os dados apenas enquanto estão em trânsito naquela conexão. Depois que o gateway os decifra, as leituras são texto claro dentro da companhia, e o TLS não diz nada sobre se o próprio medidor foi honesto.

### 11.3 Autenticação fim a fim

Como o TLS termina no gateway, Aiyana propõe que cada medidor também anexe uma tag HMAC a cada leitura, usando sua chave por medidor do Capítulo 5. O banco de dados de faturamento verifica a tag diretamente, de modo que um gateway ou concentrador comprometido não consegue alterar as leituras sem ser detectado. Essa estratificação, segurança de transporte somada à autenticação de mensagens, é comum em infraestruturas críticas. Ela documenta qual camada defende contra qual atacante: o TLS contra operadoras e quem escuta naquele enlace, o HMAC contra qualquer sistema intermediário que modifique leituras. A sobreposição é deliberada, para que uma falha não elimine toda a proteção.

### Exemplo resolvido

O diagrama de Aiyana mostra quatro saltos; o TLS 1.3 protege o trecho do concentrador ao gateway, e as tags HMAC por medidor protegem as leituras do medidor até o banco de dados.

> **Caso sintético.** A rede da Ridgeway é inventada; a RFC 8446 e a RFC 7748 são reais.

### Erros e limites

O TLS não autentica a origem dos dados além da ponta da conexão; controles no nível da mensagem são necessários quando os intermediários não são confiáveis. Os enlaces de rádio até os medidores podem precisar de proteção separada.

### Exercícios

- **EX031 — Atacantes por salto.** Cite o atacante que Aiyana associa ao salto celular. *Rubrica:* 3 = a operadora celular ou qualquer pessoa na rede dela;; 2 = rede;; 1 = nenhum;; 0 = nenhuma.

- **EX032 — Sigilo futuro.** O que significa sigilo futuro no TLS 1.3? *Rubrica:* 3 = o tráfego gravado não pode ser decifrado depois, mesmo que chaves de longo prazo vazem, graças à troca de chaves efêmera;; 2 = chaves efêmeras;; 1 = cifração;; 0 = nenhuma.

- **EX033 — Por que também HMAC.** Por que acrescentar tags HMAC quando o TLS já é usado? *Rubrica:* 3 = o TLS termina no gateway; o HMAC permite ao banco de dados detectar leituras alteradas por intermediários comprometidos;; 2 = estratificação;; 1 = redundante;; 0 = nenhuma.

### Síntese

Segurança de redes significa mapear os atacantes de cada salto e sobrepor proteções de transporte e de mensagem, para que nenhum ponto final receba confiança cega.

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) explicar como os sistemas operacionais protegem chaves na memória e no disco; (2) usar corretamente o gerador aleatório do sistema operacional; (3) aplicar o privilégio mínimo a serviços criptográficos.

### 12.1 Processos e memória

Um sistema operacional separa os processos para que um não possa ler a memória do outro. O serviço de chaves da Ridgeway roda como processo próprio, sob uma conta dedicada; a aplicação de faturamento pede a ele que calcule as tags, em vez de guardar as chaves. Aiyana aprende que uma chave na memória de um processo também pode acabar em arquivos de swap ou em despejos de memória após falhas (crash dumps), então o serviço desativa os core dumps e trava as páginas das chaves na memória, onde a plataforma permite. Esses detalhes do sistema operacional importam tanto quanto o algoritmo, porque a maioria dos roubos reais de chaves as lê da memória ou do disco, e não quebrando a criptografia.

### 12.2 O gerador aleatório do sistema operacional

O sistema operacional reúne entropia de eventos de hardware e expõe aos programas um gerador criptograficamente seguro, no Linux pela chamada de sistema getrandom. O módulo secrets do Python o usa. Aiyana compara secrets.token_bytes com o módulo random, que é um gerador rápido e previsível feito para simulações; suas saídas podem ser reconstruídas depois de observados valores suficientes. Ela reescreve o script de geração de chaves de um colega que usava random.getrandbits. A regra que adota é simples: tudo o que é secreto, incluindo chaves, nonces e tokens, vem do secrets ou de uma biblioteca avaliada, nunca do random.

### 12.3 Privilégio mínimo

Aiyana configura o serviço de chaves para rodar com os direitos mínimos de que precisa: acesso de leitura ao seu próprio arquivo de chaves cifrado, um único socket de escuta e nenhum shell. As permissões de arquivo restringem o arquivo de chaves à conta do serviço. Os administradores acessam o serviço por uma interface auditada, em vez de entrar no host. O SP 800-57 Part 1 enfatiza a proteção das chaves ao longo de todo o seu ciclo de vida, e o privilégio mínimo no nível do sistema operacional é uma grande parte dessa proteção. Se a aplicação de faturamento for comprometida, o atacante ainda assim não consegue ler as chaves brutas.

### Exemplo resolvido

Aiyana transfere as chaves para um processo de serviço dedicado, com memória travada, sem core dumps, com permissões de arquivo mínimas e geração baseada no secrets.

> **Caso sintético.** O serviço de chaves é inventado; o SP 800-57 Part 1 é real.

### Erros e limites

O travamento de memória e a supressão de dumps dependem da plataforma e são imperfeitos. Um atacante privilegiado no host ainda pode ler a memória, então o isolamento reduz o risco, mas não o elimina.

### Exercícios

- **EX034 — Swap e dumps.** Por que desativar os core dumps do serviço de chaves? *Rubrica:* 3 = chaves na memória poderiam ser gravadas em dumps ou no swap e roubadas do disco;; 2 = vazamento em disco;; 1 = desempenho;; 0 = nenhuma.

- **EX035 — random versus secrets.** Por que as chaves nunca podem vir do módulo random do Python? *Rubrica:* 3 = ele é previsível e reconstruível; o secrets usa o CSPRNG do sistema operacional;; 2 = previsível;; 1 = mais lento;; 0 = nenhuma.

- **EX036 — Aplicação de faturamento comprometida.** O que um atacante que compromete a aplicação de faturamento não consegue fazer? *Rubrica:* 3 = ler as chaves brutas, já que o serviço de chaves separado as guarda sob privilégio mínimo;; 2 = limitado;; 1 = tudo;; 0 = nenhuma.

### Síntese

O isolamento do sistema operacional, a aleatoriedade segura e o privilégio mínimo protegem as chaves onde acontece a maioria dos roubos reais: na memória e no disco.

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) escolher entre hash, cifração e tokenização para dados armazenados; (2) armazenar senhas com funções que exigem muita memória (memory-hard); (3) planejar a cifração em repouso com chaves separadas.

### 13.1 Três ferramentas para dados armazenados

O banco de dados da Ridgeway guarda nomes, endereços e dados bancários dos clientes, além das leituras dos medidores. Aiyana aprende a escolher a ferramenta certa para cada campo. A cifração esconde dados que precisarão ser lidos depois, como os dados bancários para débito automático. A tokenização substitui os dados por uma referência sem significado guardada em outro lugar, útil quando a maioria dos sistemas precisa apenas de um marcador. O hash, que é de mão única, serve para valores que só precisam ser conferidos, nunca recuperados. Escolher a ferramenta errada, como calcular o hash de dados bancários que precisam ser usados ou cifrar senhas que nunca precisam ser decifradas, cria sistemas quebrados ou riscos desnecessários.

### 13.2 Armazenar senhas

As senhas do portal dos clientes nunca devem ser armazenadas em texto claro nem apenas com um hash rápido como o SHA-256, porque atacantes que roubem a tabela podem testar bilhões de palpites por segundo. Aiyana recomenda uma função de hash de senhas memory-hard, o Argon2id da RFC 9106, que obriga cada palpite a usar memória e tempo significativos, com um salt aleatório único por usuário. Se o Argon2 não estiver disponível, o scrypt da RFC 7914 ou o PBKDF2 com um número alto de iterações são alternativas. O hashlib do Python oferece scrypt e pbkdf2_hmac; o código de produção ainda assim usa uma biblioteca avaliada de hash de senhas, com padrões sensatos.

### 13.3 Cifração em repouso

Para os dados bancários, a Ridgeway usa cifração do banco de dados com uma chave de cifração de dados, ela própria cifrada por uma chave de cifração de chaves guardada no serviço de chaves, um padrão chamado cifração envelopada (envelope encryption). Aiyana explica seu benefício: rotacionar a chave de cifração de chaves exige recifrar apenas as pequenas chaves de dados, e não o banco de dados inteiro. Ela também anota um limite: a cifração em repouso protege contra discos e backups roubados, mas não contra um atacante que consulta a aplicação em execução, que decifra os dados para os usuários legítimos. O controle de acesso e o monitoramento continuam essenciais ao lado da cifração.

### Exemplo resolvido

Aiyana atribui a cifração aos dados bancários, tokens aos sistemas de relatórios e o Argon2id com salts por usuário às senhas do portal, e projeta a cifração envelopada com as chaves no serviço de chaves.

> **Caso sintético.** O banco de dados é inventado; a RFC 9106 e a RFC 7914 são reais.

### Erros e limites

A cifração em repouso não impede o roubo pelo nível da aplicação. Um hash de senha lento ainda falha se os usuários escolherem senhas muito comuns, então limitação de tentativas e verificação de vazamentos ajudam.

### Exercícios

- **EX037 — Escolher uma ferramenta.** Que ferramenta serve para as senhas do portal, e por quê? *Rubrica:* 3 = hash com uma função memory-hard, já que elas precisam ser conferidas, não recuperadas;; 2 = hash;; 1 = cifração;; 0 = nenhuma.

- **EX038 — Escolha do Argon2.** O que Aiyana recomenda para senhas, e que RFC o define? *Rubrica:* 3 = Argon2id com salts por usuário, RFC 9106;; 2 = Argon2;; 1 = SHA-256;; 0 = nenhuma.

- **EX039 — Benefício do envelope.** Que benefício a cifração envelopada oferece? *Rubrica:* 3 = rotacionar a chave de cifração de chaves recifra apenas as pequenas chaves de dados;; 2 = rotação mais fácil;; 1 = consultas mais rápidas;; 0 = nenhuma.

### Síntese

Associar hash, cifração e tokenização a cada campo, com hash de senhas resistente em memória e cifração envelopada, protege os dados armazenados de forma proporcional.

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) integrar requisitos criptográficos ao ciclo de vida de desenvolvimento; (2) gerenciar dependências de bibliotecas criptográficas; (3) revisar código em busca de usos indevidos comuns.

### 14.1 Requisitos no ciclo de vida

Aiyana entra na equipe de software da Ridgeway e descobre que, em projetos anteriores, a criptografia foi acrescentada tarde, o que causou retrabalho. Ela propõe que os requisitos de segurança, como "toda leitura é autenticada com uma chave por medidor" e "o firmware só é aceito com uma assinatura válida", apareçam no backlog desde o início, cada um com um teste de aceitação. Tratar as propriedades criptográficas como requisitos testáveis, e não como uma revisão final, torna-as visíveis no planejamento e nas estimativas e deixa claro qual equipe é dona de cada propriedade.

### 14.2 Gerenciar dependências

A Ridgeway depende de algumas bibliotecas criptográficas. Aiyana registra a versão, a origem e os mantenedores de cada biblioteca e se inscreve nos seus avisos de segurança. Ela fixa as versões para que os builds sejam reproduzíveis, mas agenda atualizações regulares, porque as bibliotecas criptográficas corrigem vulnerabilidades com frequência. Ela também confere se os pacotes baixados coincidem com os hashes ou as assinaturas publicados, para evitar dependências adulteradas. A equipe concorda em nunca copiar código criptográfico de fóruns para a base de código; se faltar uma função, eles procuram uma biblioteca mantida ou levam o assunto à revisão de projeto.

### 14.3 Revisar em busca de uso indevido

Aiyana escreve um checklist curto de revisão: nenhuma chave embutida no código; segredos vindos do módulo secrets; nenhum modo ECB nem cifração não autenticada; nonces nunca reutilizados sob uma mesma chave; tags comparadas com hmac.compare_digest; senhas com hash Argon2id; verificação do TLS nunca desativada. Os revisores marcam cada item nas mudanças que tocam a criptografia. No primeiro mês, o checklist pega um auxiliar de testes que desativava a verificação de certificados e estava prestes a ser reutilizado em código de produção. Checklists não substituem a especialização, mas pegam erros comuns de forma confiável.

### Exemplo resolvido

Aiyana acrescenta requisitos criptográficos testáveis ao backlog, fixa e monitora as bibliotecas e introduz um checklist de revisão com sete itens que pega uma verificação de TLS desativada.

> **Caso sintético.** A equipe e o incidente são inventados.

### Erros e limites

Checklists podem virar mera formalidade; os revisores precisam entender cada item. Fixar versões sem atualizá-las mantém vulnerabilidades conhecidas.

### Exercícios

- **EX040 — Requisito testável.** Dê um exemplo de requisito criptográfico escrito como item de backlog. *Rubrica:* 3 = toda leitura autenticada com uma chave por medidor (ou firmware aceito apenas com assinatura válida), com teste de aceitação;; 2 = exemplo sem teste;; 1 = vago;; 0 = nenhuma.

- **EX041 — Regra de dependências.** O que a equipe combinou sobre código de fóruns? *Rubrica:* 3 = nunca copiar código criptográfico de fóruns; usar uma biblioteca mantida ou levar à revisão de projeto;; 2 = evitar;; 1 = permitido;; 0 = nenhuma.

- **EX042 — O que o checklist pegou.** O que o checklist pegou no primeiro mês? *Rubrica:* 3 = um auxiliar de testes que desativava a verificação de certificados e estava prestes a entrar em produção;; 2 = problema de TLS;; 1 = nada;; 0 = nenhuma.

### Síntese

A criptografia se torna confiável quando é um requisito testado, suas bibliotecas são gerenciadas ativamente e as revisões procuram usos indevidos conhecidos.

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) associar confidencialidade, integridade e disponibilidade a controles criptográficos; (2) definir modelos de ameaça; (3) distinguir autenticação de autorização.

### 15.1 As três propriedades

A segurança costuma ser descrita pela confidencialidade, pela integridade e pela disponibilidade. Aiyana associa cada uma aos medidores da Ridgeway. A confidencialidade das leituras importa porque os padrões de consumo revelam quando as casas estão vazias. A integridade importa porque leituras alteradas mudam as contas. A disponibilidade importa porque a companhia precisa das leituras para detectar vazamentos. A criptografia serve principalmente à confidencialidade e à integridade: a cifração à primeira, os códigos de autenticação e as assinaturas à segunda. Ela pode prejudicar a disponibilidade se chaves forem perdidas ou certificados expirarem, e é por isso que o gerenciamento de chaves e as operações são tão importantes quanto os algoritmos.

### 15.2 Modelos de ameaça

Um modelo de ameaça informa quem são os atacantes, o que querem, o que podem fazer e o que está fora do escopo. Aiyana escreve um para os medidores: um vizinho curioso com um receptor de rádio, um cliente tentando reduzir a conta, um grupo criminoso que busca interromper o abastecimento e um insider malicioso. Ela deixa fora do escopo do piloto os ataques de hardware de Estados-nação e diz isso explicitamente. Katz e Lindell insistem em que toda definição de segurança depende de um modelo explícito de atacante; sem ele, afirmações como "seguro" não têm significado.

### 15.3 Autenticação e autorização

A autenticação estabelece quem ou o que está se comunicando; a autorização decide o que essa parte pode fazer. Um medidor se autentica com sua chave por medidor, mas só está autorizado a enviar as próprias leituras, e não as de outros medidores nem mudanças de configuração. Aiyana encontra um rascunho de projeto em que qualquer medidor autenticado poderia enviar leituras para qualquer identificador, uma confusão clássica entre as duas coisas. Ela acrescenta uma verificação que vincula cada chave a um único identificador de medidor. A criptografia fornece a autenticação; a autorização é uma decisão de política implementada na lógica da aplicação.

### Exemplo resolvido

Aiyana associa as propriedades da tríade CIA aos controles dos medidores, escreve um modelo de ameaça com quatro atacantes e uma exclusão explícita e corrige um projeto em que a autenticação não implicava a autorização correta.

> **Caso sintético.** O modelo de ameaça é inventado.

### Erros e limites

Modelos de ameaça envelhecem; revise-os quando os sistemas mudarem. Uma autenticação forte com uma autorização fraca ainda permite abusos.

### Exercícios

- **EX043 — Por que a confidencialidade.** Por que a confidencialidade das leituras dos medidores importa? *Rubrica:* 3 = os padrões de consumo revelam quando as casas estão vazias;; 2 = privacidade;; 1 = nenhum motivo;; 0 = nenhuma.

- **EX044 — Fora do escopo.** O que Aiyana deixou fora do escopo, e por que declarar isso? *Rubrica:* 3 = ataques de hardware de Estados-nação; um escopo explícito dá significado às afirmações;; 2 = escopo declarado;; 1 = nada;; 0 = nenhuma.

- **EX045 — Correção da autorização.** Que verificação corrigiu a falha de autorização? *Rubrica:* 3 = vincular cada chave a um identificador de medidor, para que os medidores só enviem as próprias leituras;; 2 = vinculação;; 1 = cifração;; 0 = nenhuma.

### Síntese

Os fundamentos de segurança dão o enquadramento da criptografia: associe-a a propriedades explícitas e a modelos de atacante e mantenha a autenticação separada da autorização.

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) tratar o gerenciamento de chaves como um sistema com etapas de ciclo de vida; (2) definir interfaces e responsabilidades; (3) rastrear os requisitos através dos componentes.

### 16.1 Chaves como sistema

Aiyana aprende com o SP 800-57 Part 1 que as chaves têm ciclos de vida: geração, distribuição, uso, armazenamento, rotação, revogação e destruição. Cada etapa envolve pessoas, processos e tecnologia. Ela desenha o sistema de chaves da Ridgeway: um serviço de chaves que gera as chaves dos medidores, um processo na fábrica que as carrega nos elementos seguros, concentradores que encaminham as leituras e um sistema de faturamento que verifica as tags. A engenharia de sistemas a ajuda a ver que uma fraqueza em qualquer ponto, como chaves enviadas por e-mail à fábrica, mina algoritmos fortes em todos os outros. Seu diagrama também mostra as pessoas envolvidas, porque um procedimento descuidado quebra um sistema tão certamente quanto um algoritmo fraco.

### 16.2 Interfaces e responsabilidades

Para cada interface, Aiyana define o que é trocado, como é protegido e quem é o dono. A fábrica recebe as chaves dos medidores cifradas sob uma chave de transporte, e não em claro; o serviço de chaves é dono da geração; as operações são donas da rotação; a segurança é dona das decisões de revogação. Ela usa uma tabela de responsabilidades para que nenhuma etapa do ciclo de vida fique sem dono. Em projetos anteriores, a revogação ficou entre equipes, e chaves comprometidas continuaram ativas por meses. Uma propriedade clara é, por si só, um controle de segurança. A tabela é revisada a cada trimestre, para que reorganizações nunca deixem uma etapa sem dono.

### 16.3 Rastreabilidade de requisitos

Aiyana rastreia cada requisito de alto nível, como "uma chave de medidor roubada afeta apenas aquele medidor", até os requisitos dos componentes: derivação por medidor no serviço de chaves, vinculação das chaves aos identificadores no faturamento, listas de revogação nos concentradores. Cada requisito de componente tem um método de verificação: teste, inspeção ou análise. Quando um fornecedor propõe uma mudança no processo da fábrica, o rastreamento mostra quais requisitos ela toca e quais testes precisam ser executados de novo. A rastreabilidade transforma uma meta de segurança em trabalho de engenharia verificável. Ela também ajuda os auditores, que podem seguir qualquer requisito até a sua evidência.

### Exemplo resolvido

O diagrama do sistema de chaves, a tabela de responsabilidades e a matriz de rastreabilidade de Aiyana mostram cada etapa do ciclo de vida com dono e cada requisito de segurança ligado a um teste.

> **Caso sintético.** Os processos da Ridgeway são inventados; o SP 800-57 Part 1 é real.

### Erros e limites

Diagramas se afastam da realidade; revise-os em relação ao que está implantado. A rastreabilidade só ajuda se os testes realmente rodarem.

### Exercícios

- **EX046 — Etapas do ciclo de vida.** Liste quatro etapas do ciclo de vida das chaves segundo o SP 800-57. *Rubrica:* 3 = quatro entre geração, distribuição, uso, armazenamento, rotação, revogação, destruição;; 2 = três;; 1 = uma;; 0 = nenhuma.

- **EX047 — Interface com a fábrica.** Como as chaves são protegidas a caminho da fábrica? *Rubrica:* 3 = cifradas sob uma chave de transporte, nunca em claro;; 2 = cifradas;; 1 = por e-mail;; 0 = nenhuma.

- **EX048 — Lição sobre a propriedade.** Que falha passada motivou a tabela de responsabilidades? *Rubrica:* 3 = a revogação ficou entre equipes, e chaves comprometidas continuaram ativas por meses;; 2 = etapa sem dono;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Tratar o gerenciamento de chaves como um sistema com interfaces que têm dono e requisitos rastreados impede que algoritmos fortes sejam minados por processos fracos.

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) aplicar laços de realimentação às operações de segurança; (2) projetar alertas sobre sinais de saúde criptográfica; (3) evitar oscilações e a fadiga de alertas.

### 17.1 Realimentação nas operações

A engenharia de controle estuda sistemas que medem a saída e ajustam a entrada. Aiyana aplica a ideia às operações criptográficas: medir sinais como falhas de verificação de tags, dias até a expiração dos certificados e idade das chaves, compará-los com metas e agir. Sem realimentação, os problemas só são percebidos quando os clientes reclamam. Um laço de realimentação para a Ridgeway poderia medir a taxa horária de falhas de verificação por concentrador e alertar se ela subir bruscamente, o que poderia indicar um lote defeituoso de medidores ou uma tentativa de falsificação. Aiyana trata cada sinal como um sensor e cada runbook como o controlador que fecha o laço.

### 17.2 Projetar alertas

Aiyana escolhe os limiares a partir de dados de linha de base. As falhas normais de verificação, por ruído de rádio e deriva de relógio, ficam em torno de 0,1 por cento; ela alerta acima de 1 por cento sustentado por quinze minutos. Os certificados geram alerta trinta dias antes da expiração e escalonam aos sete. A idade das chaves gera alerta no fim do seu criptoperíodo. Cada alerta tem um dono e um runbook com as primeiras verificações. Ela também acrescenta alertas para a ausência de sinais esperados, como nenhuma tentativa de renovação na última semana, porque falhas silenciosas causam muitas indisponibilidades.

### 17.3 Evitar fadiga e oscilação

Alertas demais ensinam as pessoas a ignorá-los, e reações automáticas agressivas demais podem oscilar, por exemplo revogando e reprovisionando repetidamente as chaves de um medidor com um rádio instável. Aiyana acrescenta histerese: um alerta só se encerra quando a taxa cai bem abaixo do gatilho. As ações automáticas se limitam a passos seguros, como sinalizar um medidor para inspeção, enquanto a revogação exige uma decisão humana. Ela revisa mensalmente o volume de alertas e remove os que nunca levaram a uma ação, mantendo o sinal significativo.

### Exemplo resolvido

Aiyana projeta alertas sobre a taxa de falhas de verificação, a expiração de certificados e a idade das chaves, com linhas de base, histerese e aprovação humana para a revogação.

> **Caso sintético.** As linhas de base são inventadas.

### Erros e limites

Limiares definidos sem linha de base criam ruído. A revogação automática sem histerese pode interromper o serviço.

### Exercícios

- **EX049 — Sinais de saúde.** Cite três sinais de saúde criptográfica que Aiyana mede. *Rubrica:* 3 = falhas de verificação, dias até a expiração dos certificados, idade das chaves;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX050 — Alerta de sinal ausente.** Por que alertar sobre a ausência de tentativas de renovação? *Rubrica:* 3 = falhas silenciosas, como clientes de renovação quebrados, causam indisponibilidades;; 2 = silêncio;; 1 = desnecessário;; 0 = nenhuma.

- **EX051 — Uso da histerese.** O que a histerese impede aqui? *Rubrica:* 3 = alertas oscilando ou revogação/reprovisionamento repetidos de medidores instáveis;; 2 = intermitência;; 1 = nada;; 0 = nenhuma.

### Síntese

Laços de realimentação com limiares baseados em linhas de base, histerese e portões humanos mantêm os sistemas criptográficos saudáveis sem afogar os operadores em ruído.

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) posicionar âncoras de confiança criptográficas numa arquitetura; (2) projetar defesa em profundidade para as chaves; (3) comparar serviços de chaves centralizados e distribuídos.

### 18.1 Âncoras de confiança

Toda arquitetura criptográfica se apoia em âncoras de confiança, chaves cuja autenticidade é pressuposta, e não provada, como um certificado raiz ou uma chave pública de assinatura de firmware embutida nos medidores. Aiyana identifica as âncoras da Ridgeway: a chave raiz do firmware, a raiz TLS dos concentradores e a chave mestra no serviço de chaves. O comprometimento de uma âncora é catastrófico, então as âncoras são poucas, mantidas offline sempre que possível e protegidas por procedimentos que exigem várias pessoas. Seu diagrama de arquitetura marca as âncoras em vermelho, para que os revisores vejam imediatamente onde é necessária a maior proteção.

### 18.2 Defesa em profundidade para as chaves

Aiyana organiza a proteção em camadas: a chave raiz do firmware fica num módulo de segurança de hardware offline, usado apenas em cerimônias de assinatura; chaves de assinatura intermediárias assinam as versões do dia a dia e podem ser revogadas; os medidores só aceitam firmware quando a cadeia é verificada e o número de versão aumenta, o que impede a volta (rollback) a versões antigas e vulneráveis. Cada camada limita o dano causado pela falha de outra. Se uma chave intermediária vazar, a raiz pode revogá-la; se uma versão antiga assinada for reenviada, a verificação de versão a rejeita.

### 18.3 Centralizado ou distribuído

Um único serviço central de chaves simplifica a auditoria e a rotação, mas se torna um alvo de alto valor e um ponto único de falha. Distribuir as chaves entre serviços regionais melhora a disponibilidade, mas multiplica os lugares a proteger. Aiyana propõe um serviço central com um standby ativo (hot standby) num segundo data center e caches regionais que guardam apenas chaves derivadas de vida curta. Ela avalia o projeto em relação ao modelo de ameaça do Capítulo 15 e registra que um insider num site regional só consegue afetar as chaves de vida curta daquela região. Ela anota que o site de standby duplica os controles físicos a auditar.

### Exemplo resolvido

A arquitetura de Aiyana marca três âncoras de confiança, coloca a raiz do firmware offline, com intermediárias para as versões e proteção contra rollback, e escolhe um serviço central de chaves com standby e caches regionais de vida curta.

> **Caso sintético.** A arquitetura é inventada.

### Erros e limites

Raízes offline são tão seguras quanto os procedimentos das cerimônias. A proteção contra rollback falha se os contadores de versão puderem ser reiniciados.

### Exercícios

- **EX052 — Âncora de confiança definida.** O que é uma âncora de confiança? *Rubrica:* 3 = uma chave cuja autenticidade é pressuposta, como um certificado raiz ou uma chave de assinatura de firmware embutida;; 2 = chave raiz;; 1 = qualquer chave;; 0 = nenhuma.

- **EX053 — Proteção contra rollback.** Como o projeto impede o rollback do firmware? *Rubrica:* 3 = os medidores exigem que o número de versão aumente, além de uma cadeia válida;; 2 = verificação de versão;; 1 = só a assinatura;; 0 = nenhuma.

- **EX054 — Insider regional.** O que um insider num site regional consegue afetar no projeto escolhido? *Rubrica:* 3 = apenas as chaves derivadas de vida curta daquela região;; 2 = limitado;; 1 = tudo;; 0 = nenhuma.

### Síntese

As arquiteturas devem nomear suas âncoras de confiança, proteger as chaves em camadas e equilibrar o controle central com a disponibilidade, com exposição regional limitada.

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) autenticar dispositivos e pessoas com chaves e certificados; (2) usar o HMAC para a autenticação de mensagens; (3) relacionar identidades a certificados e à revogação.

### 19.1 Identidade dos dispositivos

Cada medidor da Ridgeway precisa de uma identidade que outros possam verificar. Aiyana compara duas abordagens. A identidade simétrica usa uma chave secreta por medidor compartilhada com o serviço de chaves; é barata, mas o serviço precisa proteger todas as chaves. A identidade assimétrica dá a cada medidor um par de chaves e um certificado assinado pela autoridade de dispositivos da Ridgeway, seguindo o perfil X.509 da RFC 5280; os verificadores precisam apenas das chaves públicas. Ela recomenda chaves HMAC simétricas para as leituras, cujo volume é alto, e certificados para os concentradores, que se autenticam no gateway por TLS.

### Laboratório — Autenticação de mensagens

```python
"""Authenticate synthetic meter readings with HMAC-SHA256 (RFC 2104) and constant-time compare."""
import hmac, hashlib
KEY = bytes(range(32))   # demo key; real keys come from the utility's key service
def tag(msg): return hmac.new(KEY, msg, hashlib.sha256).hexdigest()

def main():
    msg = b"meter=M-0417;litres=18342;ts=2026-04-01T06:00Z"
    t = tag(msg)
    print("tag", t[:24], "...")
    print("genuine verifies:", hmac.compare_digest(t, tag(msg)))
    forged = msg.replace(b"18342", b"08342")
    print("edited reading verifies:", hmac.compare_digest(t, tag(forged)))

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_hmac.py`. Saída verificada:

```text
tag bc7de0101afc1c79bfc23747 ...
genuine verifies: True
edited reading verifies: False
```

### 19.2 Ler a execução do HMAC

O laboratório gera a tag de uma leitura canônica com HMAC-SHA256 e a verifica. A leitura genuína é verificada, e a leitura editada, com um dígito alterado, falha, porque sem a chave ninguém consegue calcular uma tag válida para uma mensagem modificada. A verificação usa hmac.compare_digest para evitar vazamentos de tempo. A chave de demonstração é uma sequência fixa de bytes apenas para que a saída seja reproduzível; as chaves reais vêm do serviço de chaves. Aiyana enfatiza que o HMAC dá integridade e autenticação da origem entre as partes que compartilham a chave, mas não irretratabilidade (não repúdio), porque qualquer das partes poderia ter produzido a tag.

### 19.3 Pessoas e revogação

As pessoas da Ridgeway se autenticam com chaves de segurança de hardware e certificados de vida curta para o acesso administrativo. Quando alguém sai, seu acesso precisa terminar rapidamente. Aiyana documenta a revogação para cada tipo de identidade: as chaves dos medidores são desativadas no serviço de chaves; os certificados dos concentradores são acrescentados a uma lista de revogação ou simplesmente deixados expirar, já que têm vida curta; os certificados da equipe são revogados e seus tokens desativados. Ela anota que vidas curtas reduzem a dependência da verificação de revogação, que os clientes fazem de forma desigual. Os passos de revogação são ensaiados duas vezes por ano, para que a equipe os conheça sob pressão.

### Exemplo resolvido

Aiyana escolhe chaves HMAC por medidor para as leituras e certificados para os concentradores e a equipe, demonstra a verificação de tags e documenta a revogação por tipo de identidade.

> **Caso sintético.** As identidades e a chave de demonstração são inventadas; a RFC 5280 e a RFC 2104 são reais.

### Erros e limites

O HMAC não consegue provar a um terceiro qual lado criou uma mensagem. Certificados de vida longa tornam a revogação essencial e difícil.

### Exercícios

- **EX055 — Simétrico ou assimétrico.** Por que usar chaves HMAC para as leituras, mas certificados para os concentradores? *Rubrica:* 3 = leituras em grande volume combinam com tags simétricas baratas; os concentradores usam TLS com verificação pública;; 2 = motivos parciais;; 1 = aleatório;; 0 = nenhuma.

- **EX056 — Leitura editada.** O que o laboratório imprimiu para a leitura editada, e por quê? *Rubrica:* 3 = False, já que uma tag válida não pode ser calculada sem a chave;; 2 = False;; 1 = True;; 0 = nenhuma.

- **EX057 — Irretratabilidade.** Por que o HMAC não oferece irretratabilidade? *Rubrica:* 3 = as duas partes compartilham a chave, então qualquer uma poderia ter feito a tag;; 2 = chave compartilhada;; 1 = ele oferece;; 0 = nenhuma.

### Síntese

A identidade combina chaves, certificados e revogação; o HMAC autentica mensagens de alto volume entre detentores de chaves, enquanto os certificados escalam a verificação.

<a id="ch-20"></a>

## Capítulo 20 — Criptografia e serviços de confiança: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) enquadrar as necessidades criptográficas da Ridgeway como um problema de engenharia; (2) listar as partes interessadas e as restrições; (3) definir medidas de sucesso para o serviço de confiança.

### 20.1 O problema de engenharia

Ao entrar nos anos de especialização, Aiyana escreve uma declaração do problema: a Ridgeway precisa de um serviço de confiança que emita e gerencie chaves e certificados para 50.000 medidores, 400 concentradores e 120 funcionários, autentique cada leitura de ponta a ponta, assine o firmware com proteção contra rollback e continue disponível durante indisponibilidades. As restrições incluem a vida da bateria dos medidores, a largura de banda do rádio e um orçamento fixo. Enquadrar o problema dessa forma desloca a discussão de qual algoritmo é o mais forte para qual sistema atende juntos às necessidades de segurança, custo e confiabilidade. Ela mantém a declaração em uma página, para que todas as partes interessadas possam lê-la e contestá-la.

### 20.2 Partes interessadas

Aiyana lista as partes interessadas e o que elas precisam: os clientes precisam de contas corretas e de privacidade; os técnicos de campo precisam substituir medidores sem passos complexos; as operações precisam de alertas sobre os quais consigam agir; o regulador precisa de evidências dos controles; os fornecedores precisam de interfaces claras. Ela entrevista cada grupo. Os técnicos revelam que os medidores às vezes são trocados entre endereços durante consertos, o que afeta como as chaves são vinculadas às identidades. Fatos operacionais como esse, invisíveis num livro de segurança, moldam o projeto tanto quanto as normas. Aiyana registra cada entrevista numa nota curta, para que as escolhas de projeto posteriores possam citar necessidades reais.

### 20.3 Medidas de sucesso

Aiyana define metas mensuráveis: nenhuma leitura forjada aceita em testes independentes; menos de um incidente de expiração de certificado por ano; atualizações de firmware chegando a 99 por cento dos medidores em até trinta dias; rotação de chaves concluída no prazo para todas as classes de chave; e provisionamento de um medidor substituto em menos de dez minutos. Cada medida tem uma fonte de dados e um dono. As medidas mantêm o projeto honesto, evitam o excesso de sofisticação e dão ao regulador evidências que vão além de garantias verbais. Ela também planeja revisar as medidas anualmente, já que uma meta definida no piloto pode ser frouxa ou rígida demais em escala completa.

### Exemplo resolvido

A declaração do problema de Aiyana nomeia a escala, as restrições, as partes interessadas e cinco medidas de sucesso, incluindo a meta de provisionamento em dez minutos dos técnicos.

> **Caso sintético.** Os números da Ridgeway são inventados.

### Erros e limites

Medidas de sucesso podem ser manipuladas se ignorarem a qualidade; associe cada uma a uma revisão. As entrevistas com as partes interessadas podem deixar de fora grupos silenciosos, como clientes com necessidades de acessibilidade.

### Exercícios

- **EX058 — Restrições do problema.** Cite três restrições da declaração do problema. *Rubrica:* 3 = três entre vida da bateria, largura de banda do rádio, orçamento, disponibilidade durante indisponibilidades;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX059 — Percepção dos técnicos.** O que os técnicos revelaram, e por que isso importa? *Rubrica:* 3 = medidores trocados entre endereços durante consertos, afetando o vínculo entre chave e identidade;; 2 = troca;; 1 = nada;; 0 = nenhuma.

- **EX060 — Medida do firmware.** Enuncie a medida de sucesso do firmware. *Rubrica:* 3 = 99 por cento dos medidores atualizados em até trinta dias;; 2 = 99 por cento;; 1 = sempre;; 0 = nenhuma.

### Síntese

A engenharia criptográfica começa enquadrando a escala, as restrições, as partes interessadas e as metas mensuráveis de todo o serviço de confiança.

<a id="ch-21"></a>

## Capítulo 21 — Criptografia e serviços de confiança: requisitos

### Objetivos de aprendizagem

Você vai (1) escrever requisitos criptográficos verificáveis; (2) derivar das normas os requisitos de algoritmo e de tamanho de chave; (3) separar requisitos funcionais de requisitos de garantia.

### 21.1 Enunciados verificáveis

Aiyana reescreve metas vagas como requisitos verificáveis. "As leituras devem ser seguras" vira "Toda leitura carrega uma tag HMAC-SHA256 calculada com uma chave por medidor de 256 bits; o serviço de faturamento rejeita qualquer leitura cuja tag falhe na verificação." Cada requisito nomeia a propriedade, o mecanismo, o parâmetro e o comportamento observável. Um testador consegue conferi-lo sem adivinhar o que "seguro" queria dizer. Ela evita requisitos que ditam desnecessariamente detalhes de implementação, para que os fornecedores possam atendê-los de formas diferentes, mas é precisa onde a precisão evita usos indevidos, como no tamanho da chave e no comportamento da verificação.

### 21.2 Apoiar-se nas normas

Para as escolhas de algoritmo, Aiyana cita normas, e não preferências: AES-256-GCM segundo o FIPS 197 e o SP 800-38D para cifrar dados de configuração; SHA-256 segundo o FIPS 180-4; ECDSA P-256 segundo o FIPS 186-5 ou Ed25519 segundo a RFC 8032 para as assinaturas de firmware; TLS 1.3 segundo a RFC 8446 para os concentradores. Os tamanhos de chave e os criptoperíodos seguem o SP 800-57 Part 1. Ela acrescenta um requisito voltado ao futuro: o projeto de assinatura do firmware deve permitir a migração para assinaturas pós-quânticas, como o ML-DSA do FIPS 204, sem substituir os medidores. Citar normas também permite aos auditores conferir as escolhas contra critérios públicos, e não contra as preferências da equipe, e simplifica revisões futuras quando as orientações mudarem.

### 21.3 Requisitos de garantia

Os requisitos funcionais dizem o que o sistema faz; os requisitos de garantia dizem como a Ridgeway saberá que isso foi feito corretamente. Aiyana acrescenta itens de garantia: as bibliotecas devem vir de projetos mantidos, com avisos de segurança; os módulos de segurança de hardware devem ter um certificado de validação reconhecido; testadores independentes devem tentar forjar leituras antes da entrada em produção; as cerimônias de chaves devem ter duas testemunhas e ata registrada. Esses requisitos custam dinheiro e tempo, então ela os classifica por risco e registra quais são obrigatórios para o piloto e quais para a implantação completa.

### Exemplo resolvido

O conjunto de requisitos de Aiyana especifica HMAC-SHA256 com chaves de 256 bits, algoritmos apoiados em normas, um caminho de migração pós-quântica e itens de garantia classificados.

> **Caso sintético.** O conjunto de requisitos da Ridgeway é inventado; as normas citadas são reais.

### Erros e limites

Especificar demais a implementação pode bloquear projetos melhores; especificar de menos os parâmetros convida a escolhas fracas. Os requisitos precisam de revisão periódica à medida que as normas mudam.

### Exercícios

- **EX061 — Reescrever uma meta.** Reescreva "as leituras devem ser seguras" como um requisito verificável. *Rubrica:* 3 = nomeia HMAC-SHA256, chave por medidor de 256 bits, rejeição quando a verificação falha;; 2 = mecanismo parcial;; 1 = vago;; 0 = nenhuma.

- **EX062 — Normas de assinatura.** Que normas sustentam as opções de assinatura do firmware? *Rubrica:* 3 = FIPS 186-5 (ECDSA P-256) ou RFC 8032 (Ed25519);; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

- **EX063 — Exemplo de garantia.** Dê dois requisitos de garantia. *Rubrica:* 3 = dois entre bibliotecas mantidas, HSMs validados, testes independentes de falsificação, cerimônias com testemunhas;; 2 = um;; 1 = item funcional;; 0 = nenhuma.

### Síntese

Bons requisitos criptográficos são verificáveis, fundamentados em normas, prontos para a migração e acompanhados de evidências de garantia.

<a id="ch-22"></a>

## Capítulo 22 — Criptografia e serviços de confiança: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) modelar chaves, certificados e identidades como dados; (2) projetar o esquema de um inventário de chaves; (3) modelar os estados e as transições das chaves.

### 22.1 Modelar os objetos de chave

Aiyana modela os dados do serviço de confiança. Um registro de chave tem identificador, finalidade, algoritmo, tamanho, dono, data de criação, data de ativação, data de expiração ou de fim do criptoperíodo, estado e local de armazenamento; ele nunca contém o próprio material de chave. Um registro de certificado liga uma identidade de titular, a impressão digital (fingerprint) da chave pública, o emissor, o número de série e as datas de validade. Os registros de medidor ligam um medidor físico, o identificador da sua chave atual e o endereço de instalação. Separar a identidade da chave permite trocar a chave dos medidores ou movê-los entre endereços sem perder o histórico.

### 22.2 O inventário de chaves

Usando o modelo, Aiyana projeta um inventário de chaves, o lugar único que lista todas as chaves da Ridgeway. O SP 800-57 Part 1 enfatiza que as organizações precisam saber que chaves têm e onde elas são usadas. O inventário responde a perguntas operacionais: quais chaves expiram este mês, quais sistemas usam a chave intermediária do firmware, quais chaves ainda usam um algoritmo com aposentadoria programada. Ela encontra três chaves em scripts antigos que ninguém tinha registrado, o que demonstra por que o inventário importa antes que qualquer mudança criptográfica possa ser planejada com segurança.

### 22.3 Estados das chaves

Aiyana modela os estados de uma chave: pré-ativação, ativa, suspensa, desativada, comprometida e destruída, seguindo o ciclo de vida descrito no SP 800-57 Part 1. Cada transição tem um gatilho e um ator autorizado: ativação depois do provisionamento, desativação no fim do criptoperíodo, comprometida diante de evidência de exposição. Chaves desativadas ainda podem verificar dados antigos, mas não criar novas tags nem assinaturas. O modelo de estados evita erros como assinar um novo firmware com uma chave já marcada para aposentadoria, porque o serviço verifica o estado antes de cada operação. As mudanças de estado são registradas com o ator e o motivo, para auditoria.

### Exemplo resolvido

O modelo de dados de Aiyana separa medidores, identidades e chaves; o inventário encontra três chaves não registradas; e um ciclo de vida com seis estados bloqueia assinaturas com chaves aposentadas.

> **Caso sintético.** O esquema e os achados são inventados; o SP 800-57 Part 1 é real.

### Erros e limites

Inventários se degradam sem descoberta automatizada. Um modelo de estados só é aplicado se toda operação o verificar.

### Exercícios

- **EX064 — Nenhum material de chave.** O que um registro de chave nunca pode conter? *Rubrica:* 3 = o próprio material de chave;; 2 = segredos;; 1 = metadados;; 0 = nenhuma.

- **EX065 — Achado do inventário.** O que a construção do inventário revelou? *Rubrica:* 3 = três chaves em scripts antigos que ninguém tinha registrado;; 2 = chaves não registradas;; 1 = nada;; 0 = nenhuma.

- **EX066 — Chave desativada.** O que uma chave desativada ainda pode fazer, e o que não pode? *Rubrica:* 3 = verificar dados antigos, mas não criar novas tags ou assinaturas;; 2 = só verificar;; 1 = tudo;; 0 = nenhuma.

### Síntese

Modelos de dados claros, um inventário completo e uma máquina de estados de chave imposta tornam as chaves gerenciáveis, em vez de passivos escondidos.

<a id="ch-23"></a>

## Capítulo 23 — Criptografia e serviços de confiança: análise de ameaças e falhas

### Objetivos de aprendizagem

Você vai (1) analisar sistematicamente as ameaças ao serviço de confiança; (2) analisar modos de falha não maliciosos; (3) classificar os riscos para tratamento.

### 23.1 Ameaças sistemáticas

Aiyana usa um método estruturado, percorrendo cada componente e cada fluxo de dados e perguntando como um atacante poderia falsificar uma identidade, adulterar dados, negar ações, divulgar informação, negar o serviço ou obter privilégios. No caminho do firmware, ela descobre que um atacante que comprometesse o servidor de build poderia conseguir que código malicioso fosse assinado legitimamente. Nas leituras, uma chave de medidor roubada permite forjar as leituras daquele medidor. No serviço de chaves, um insider poderia exportar chaves. Cada ameaça é escrita com suas pré-condições, para que a equipe possa julgar a probabilidade, em vez de reagir à história mais dramática.

### 23.2 Modos de falha

Nem todos os problemas são ataques. Aiyana acrescenta a análise de falhas: um certificado de concentrador expirado interrompe as leituras de um distrito; a deriva de relógio nos medidores faz as verificações de timestamp rejeitarem leituras válidas; a perda do módulo de segurança de hardware sem backup torna impossível assinar o firmware; um gerador de números aleatórios defeituoso depois de uma atualização de firmware produz nonces repetidos. Para cada uma, ela registra a detecção e o efeito. Várias falhas têm consequências tão graves quanto as dos ataques, e algumas são mais prováveis, o que remodela as prioridades. Registrar os métodos de detecção também mostra quais falhas passariam despercebidas hoje.

### 23.3 Classificação e tratamento

Aiyana pontua cada ameaça e falha por probabilidade e impacto numa escala simples e escolhe um tratamento: mitigar, transferir, aceitar ou evitar. O comprometimento do servidor de build é mitigado com builds reproduzíveis e aprovação da assinatura por duas pessoas. A perda do HSM é mitigada com um backup cifrado sob custódia dividida. A deriva de relógio dos medidores é mitigada com uma janela de tolerância. Um risco residual, a adulteração física de medidores individuais, é aceito com monitoramento, porque as chaves por medidor limitam seu impacto. As decisões e os donos são registrados. O registro é revisitado depois de cada incidente ou mudança importante.

### Exemplo resolvido

A análise de Aiyana lista o comprometimento do servidor de build, chaves de medidor roubadas, exportação por insider, expiração de certificados, deriva de relógio e perda do HSM, classifica-os e atribui tratamentos com donos.

> **Caso sintético.** As ameaças e as pontuações são inventadas.

### Erros e limites

Pontuações são julgamentos, não medições; registre o raciocínio. Ignorar as falhas não maliciosas deixa de fora muitas indisponibilidades reais.

### Exercícios

- **EX067 — Ameaça ao servidor de build.** Por que o comprometimento do servidor de build é grave para o firmware? *Rubrica:* 3 = código malicioso poderia ser assinado legitimamente e aceito pelos medidores;; 2 = abuso da assinatura;; 1 = menor;; 0 = nenhuma.

- **EX068 — Exemplo de falha.** Dê dois modos de falha não maliciosos. *Rubrica:* 3 = dois entre expiração de certificado, deriva de relógio, perda do HSM, RNG defeituoso;; 2 = um;; 1 = um ataque;; 0 = nenhuma.

- **EX069 — Tratamento da perda do HSM.** Como a perda do HSM é tratada? *Rubrica:* 3 = backup cifrado sob custódia dividida;; 2 = backup;; 1 = aceitar;; 0 = nenhuma.

### Síntese

Combinar a análise de ameaças com a análise de falhas e com tratamentos explícitos dá um quadro de riscos equilibrado e com donos para o serviço de confiança.

<a id="ch-24"></a>

## Capítulo 24 — Criptografia e serviços de confiança: métodos I

### Objetivos de aprendizagem

Você vai (1) derivar muitas chaves de uma chave mestra com o HKDF; (2) verificar uma implementação contra vetores de teste publicados; (3) separar as chaves por finalidade com informações de contexto.

### 24.1 Por que derivar chaves

A Ridgeway precisa de chaves separadas para cada medidor e para cada finalidade. Armazenar 50.000 chaves aleatórias é possível, mas derivá-las de uma chave mestra no serviço de chaves simplifica o backup e o provisionamento. O HKDF, especificado na RFC 5869, faz isso em duas etapas: a extração (extract) concentra a entropia do material de chave de entrada numa chave pseudoaleatória usando HMAC com um salt, e a expansão (expand) produz quantos bytes de saída forem necessários, vinculados a uma string info que descreve a finalidade. Strings info diferentes geram chaves independentes, de modo que uma chave de telemetria não pode ser confundida com uma chave de firmware.

### Laboratório — HKDF contra a RFC 5869

```python
"""Check HKDF-SHA256 against RFC 5869 test case 1 (teaching only: use a vetted library in production)."""
import hmac, hashlib

def hkdf(ikm, salt, info, length):
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()          # extract
    okm, t, i = b"", b"", 1
    while len(okm) < length:                                     # expand
        t = hmac.new(prk, t + info + bytes([i]), hashlib.sha256).digest(); okm += t; i += 1
    return prk, okm[:length]

def main():
    prk, okm = hkdf(bytes([0x0b]) * 22, bytes(range(13)), bytes(range(0xf0, 0xfa)), 42)
    want = "3cb25f25faacd57a90434f64d0362f2a2d2d0a90cf1a5a4c5db02d56ecc4c5bf34007208d5b887185865"
    print("PRK", prk.hex()[:32], "...")
    print("OKM matches RFC 5869 A.1:", okm.hex() == want)
    a = hkdf(b"utility-master-demo", b"salt", b"telemetry-tls", 16)[1].hex()
    b = hkdf(b"utility-master-demo", b"salt", b"firmware-sign", 16)[1].hex()
    print("different info, different keys:", a != b)

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_hkdf.py`. Saída verificada:

```text
PRK 077709362c2e32df0ddc3f0dc47bba63 ...
OKM matches RFC 5869 A.1: True
different info, different keys: True
```

### 24.2 Ler a execução do HKDF

O laboratório implementa o HKDF com hmac apenas para tornar visíveis as duas etapas e o confere contra o caso de teste A.1 da RFC 5869: a saída de 42 bytes coincide exatamente. Em seguida, ele deriva duas chaves da mesma chave mestra de demonstração com strings info diferentes, telemetry-tls e firmware-sign, e confirma que elas diferem. Aiyana escreve ao lado do código que o serviço de chaves de produção da Ridgeway usa o HKDF de uma biblioteca avaliada; o objetivo do exercício é entender e verificar o comportamento, e não implantar uma versão escrita à mão. Um vetor de teste que coincide prova o uso correto, não a segurança contra canais laterais.

### 24.3 Contexto e separação

Aiyana projeta as strings info com cuidado: elas incluem a finalidade, o identificador do medidor e a versão da chave, como "ridgeway/reading-hmac/M-0417/v3". Incluir a versão permite a rotação derivando uma nova chave sem mudar a chave mestra. Incluir o identificador do medidor torna única a chave de cada medidor. Ela alerta contra reutilizar uma chave derivada para duas finalidades, como gerar tags de leituras e cifrar a configuração, porque uma fraqueza ou um uso indevido num uso poderia comprometer o outro. A separação de chaves é um hábito de projeto barato e poderoso. Ela documenta o formato dos rótulos para que todas as equipes derivem as chaves de forma idêntica.

### Exemplo resolvido

Aiyana verifica o comportamento do HKDF contra o caso A.1 da RFC 5869 e depois especifica strings info que codificam a finalidade, o identificador do medidor e a versão, para chaves por medidor e rotacionáveis.

> **Caso sintético.** A chave mestra e os rótulos são inventados; a RFC 5869 e seu vetor de teste são reais.

### Erros e limites

O HKDF não acrescenta entropia; uma chave mestra fraca gera chaves derivadas fracas. Versões escritas à mão servem apenas para aprender.

### Exercícios

- **EX070 — Extração e expansão.** O que fazem as duas etapas do HKDF? *Rubrica:* 3 = a extração gera uma chave pseudoaleatória a partir do material de entrada com um salt; a expansão produz bytes vinculados à info;; 2 = uma etapa;; 1 = cifração;; 0 = nenhuma.

- **EX071 — Resultado do vetor de teste.** O que o laboratório imprimiu na verificação da RFC 5869? *Rubrica:* 3 = OKM matches RFC 5869 A.1: True;; 2 = True;; 1 = False;; 0 = nenhuma.

- **EX072 — Projeto da string info.** O que Aiyana coloca nas strings info, e por que incluir a versão? *Rubrica:* 3 = finalidade, identificador do medidor, versão; a versão permite a rotação sem mudar a chave mestra;; 2 = parcial;; 1 = aleatório;; 0 = nenhuma.

### Síntese

O HKDF deriva muitas chaves separadas e rotacionáveis a partir de uma chave mestra bem protegida, e os vetores de teste confirmam o uso correto.

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) produzir um primeiro projeto integrado para a autenticação das leituras dos medidores; (2) apresentá-lo para crítica; (3) revisá-lo com base no retorno recebido.

### 25.1 O enunciado do ateliê

No primeiro ateliê de projeto, a equipe de Aiyana precisa projetar a autenticação fim a fim das leituras, do medidor ao faturamento, usando o que os capítulos anteriores ensinaram: chaves por medidor derivadas com HKDF, formatos canônicos de leitura, tags HMAC, TLS entre os concentradores e o gateway e verificações do estado das chaves. O enunciado inclui restrições: cada mensagem de leitura pode acrescentar no máximo 32 bytes, os medidores despertam por dois segundos a cada hora, e o sistema precisa tolerar concentradores offline por um dia. A equipe trabalha em quadros brancos antes de escrever qualquer documento.

### 25.2 O primeiro projeto

O projeto da equipe trunca as tags HMAC para 16 bytes, para caber no limite de tamanho, inclui em cada leitura um contador monotonicamente crescente para impedir a repetição (replay) e faz os concentradores guardarem as leituras em buffer durante as indisponibilidades. O faturamento verifica a tag, confere que o contador é maior que o último aceito e confere o estado da chave. Aiyana justifica as tags de 16 bytes: forjar exige adivinhar 128 bits, muito além do viável, e a RFC 2104 permite o truncamento com cuidado. Ela documenta cada decisão de projeto e o requisito que ela atende. O contador também permite ao faturamento perceber lacunas que indicam leituras perdidas.

### 25.3 Crítica e revisão

Os revisores levantam três problemas. Primeiro, se um medidor for substituído, o contador do novo medidor recomeça, e o faturamento rejeitaria suas leituras; a equipe acrescenta uma versão da chave à mensagem, para que os contadores recomecem com as novas chaves. Segundo, as leituras em buffer chegam fora de ordem depois das indisponibilidades; o faturamento passa a aceitar contadores dentro de uma janela e a acompanhar as lacunas. Terceiro, nada registra as verificações que falham; a equipe acrescenta o registro em log e o alerta do Capítulo 17. Aiyana aprende que a crítica encontra problemas operacionais que os documentos de projeto raramente revelam.

### Exemplo resolvido

O projeto da equipe usa tags HMAC truncadas para 16 bytes, com contadores, e depois é revisado para lidar com a substituição de medidores, as leituras em buffer fora de ordem e a falta de logs de falhas.

> **Caso sintético.** O ateliê e os revisores são inventados.

### Erros e limites

O truncamento reduz a resistência à falsificação; nunca trunque abaixo do que o modelo de ameaça permite. Os contadores contra replay exigem tratamento cuidadoso das reinicializações.

### Exercícios

- **EX073 — Truncamento da tag.** Por que uma tag truncada para 16 bytes é aceitável aqui? *Rubrica:* 3 = forjar exige adivinhar 128 bits; a RFC 2104 permite o truncamento cuidadoso;; 2 = 128 bits;; 1 = inseguro;; 0 = nenhuma.

- **EX074 — Defesa contra replay.** Como o projeto impede leituras repetidas? *Rubrica:* 3 = contador monotonicamente crescente verificado pelo faturamento;; 2 = contador;; 1 = só timestamps;; 0 = nenhuma.

- **EX075 — Correção da substituição.** Como a equipe corrigiu a reinicialização dos contadores nos medidores substitutos? *Rubrica:* 3 = acrescentou a versão da chave, para que os contadores recomecem com as novas chaves;; 2 = versão;; 1 = ignorar;; 0 = nenhuma.

### Síntese

A crítica de ateliê transforma um projeto aparentemente correto num projeto operável, ao expor lacunas de substituição, de ordenação e de monitoramento.

<a id="ch-26"></a>

## Capítulo 26 — Criptografia e serviços de confiança: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar arquiteturas simétricas e de chave pública para os medidores; (2) avaliar um serviço gerenciado de chaves em nuvem contra HSMs locais; (3) documentar os trade-offs.

### 26.1 Simétrica versus chave pública

Aiyana compara duas arquiteturas para a autenticação das leituras. O projeto simétrico usa HMAC com chaves derivadas no serviço de chaves: tags pequenas, pouca energia do medidor, mas o serviço guarda todas as chaves. O projeto de chave pública dá a cada medidor um par de chaves de assinatura com o Ed25519 da RFC 8032: o faturamento verifica com chaves públicas e o serviço central não guarda segredos, mas as assinaturas têm 64 bytes e assinar custa mais energia. Ela mede as duas opções contra as restrições e o modelo de ameaça e conclui que o projeto simétrico cabe no limite de 32 bytes, enquanto o de chave pública reduz o risco central.

### 26.2 Gerenciado ou local

Para o próprio serviço de chaves, Aiyana compara um serviço gerenciado de chaves em nuvem com módulos de segurança de hardware locais (on-premises). A opção em nuvem oferece alta disponibilidade e menos manutenção, mas coloca a custódia das chaves com um provedor e depende da conectividade de rede. Os HSMs locais mantêm a custódia dentro da casa, mas exigem pessoal qualificado, cerimônias e ciclos de substituição. Ela lista as restrições regulatórias: o regulador exige que as chaves do faturamento permaneçam sob o controle da companhia. As duas opções podem atender a isso com os contratos e os projetos de empacotamento de chaves (key wrapping) certos, então o custo e a equipe decidem.

### 26.3 Documentar os trade-offs

Aiyana escreve uma análise de alternativas com uma tabela de critérios: segurança, energia, tamanho da mensagem, disponibilidade, custo, competências da equipe e caminho de migração. Ela pontua cada opção e explica as notas em texto corrido. A recomendação é HMAC simétrico para as leituras, Ed25519 ou ECDSA para o firmware e HSMs locais para a raiz do firmware, com um serviço gerenciado para as chaves derivadas das leituras. Ela registra que mudança futura reverteria cada decisão, por exemplo quadros de rádio maiores que tornassem as assinaturas viáveis para as leituras. Os revisores podem então contestar uma nota sem rejeitar a análise inteira.

### Exemplo resolvido

A tabela de alternativas de Aiyana recomenda HMAC para as leituras, assinaturas para o firmware, um HSM local para a raiz do firmware e um serviço gerenciado para as chaves derivadas, com as condições de reversão.

> **Caso sintético.** As opções e as notas são inventadas; a RFC 8032 é real.

### Erros e limites

Notas escondem premissas; explique-as. A custódia em nuvem precisa de controles contratuais e técnicos, e não apenas de confiança.

### Exercícios

- **EX076 — Tamanho da assinatura.** Por que o projeto de chave pública não coube nas leituras? *Rubrica:* 3 = as assinaturas Ed25519 têm 64 bytes, excedendo o limite de 32 bytes;; 2 = tamanho;; 1 = velocidade;; 0 = nenhuma.

- **EX077 — Restrição regulatória.** Que restrição regulatória afeta a escolha do serviço de chaves? *Rubrica:* 3 = as chaves do faturamento precisam permanecer sob o controle da companhia;; 2 = custódia;; 1 = nenhuma;; 0 = nenhuma.

- **EX078 — Condição de reversão.** Dê uma condição que reverteria a decisão sobre as leituras. *Rubrica:* 3 = quadros de rádio maiores, tornando as assinaturas viáveis;; 2 = quadros maiores;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Comparar arquiteturas abertamente, com critérios, pontuações e condições de reversão, leva a uma combinação defensável de projetos simétricos e de chave pública.

<a id="ch-27"></a>

## Capítulo 27 — Criptografia e serviços de confiança: projeto de controles

### Objetivos de aprendizagem

Você vai (1) projetar controles preventivos, detectivos e corretivos para as chaves; (2) especificar uma cerimônia de chaves; (3) associar controles a riscos.

### 27.1 Três tipos de controle

Aiyana projeta controles de três tipos. Os controles preventivos impedem problemas: os HSMs impedem a exportação de chaves, as verificações de estado impedem o uso de chaves aposentadas e a revisão de código impede segredos embutidos. Os controles detectivos percebem problemas: alertas de falhas de verificação, varreduras do inventário em busca de chaves desconhecidas e o monitoramento do Certificate Transparency segundo a RFC 6962. Os controles corretivos recuperam: revogação, procedimentos de troca de chaves e restauração a partir de backups cifrados. Um conjunto equilibrado importa, porque os controles preventivos acabam falhando e a detecção sem correção apenas documenta o dano. Ela confere que todo risco alto tem pelo menos um controle de cada tipo e sinaliza qualquer risco que dependa apenas da prevenção.

### 27.2 A cerimônia de chaves

Para gerar a chave raiz do firmware, Aiyana especifica uma cerimônia: um HSM offline numa sala protegida, três custodiantes, cada um com um smart card, uma testemunha da auditoria, um roteiro escrito, gravação em vídeo da sala, mas não das telas que mostram segredos, e uma ata assinada. A chave é gerada dentro do HSM e guardada em backup em forma cifrada, dividida entre os custodiantes, de modo que dois dos três são necessários para a recuperação. O propósito da cerimônia é produzir evidências, para os reguladores e para os futuros engenheiros, de que nenhuma pessoa sozinha jamais teve a chave raiz.

### 27.3 Associar controles a riscos

Aiyana associa cada risco do Capítulo 23 aos seus controles. O comprometimento do servidor de build é associado a builds reproduzíveis, aprovação das versões por duas pessoas e registro das assinaturas. As chaves de medidor roubadas são associadas à derivação por medidor, aos alertas de verificação e à revogação. A exportação por insider é associada à não exportabilidade do HSM, ao controle duplo e aos logs de auditoria. O mapa revela um risco, a deriva de relógio dos medidores, com apenas um controle corretivo; ela acrescenta um controle detectivo que acompanha o desvio dos timestamps. Lacunas encontradas no papel são mais baratas de corrigir do que lacunas encontradas em incidentes. O mapa é mantido ao lado do registro de riscos e atualizado junto com ele.

### Exemplo resolvido

Aiyana lista controles preventivos, detectivos e corretivos, especifica uma cerimônia da chave raiz com três custodiantes e associa controles a riscos, fechando uma lacuna de detecção da deriva de relógio.

> **Caso sintético.** Os detalhes da cerimônia são inventados; a RFC 6962 é real.

### Erros e limites

Cerimônias falham se os roteiros forem ignorados sob pressão de tempo. Controles mapeados no papel ainda precisam ser testados.

### Exercícios

- **EX079 — Tipos de controle.** Dê um controle preventivo, um detectivo e um corretivo. *Rubrica:* 3 = por exemplo, não exportação pelo HSM, alertas de verificação, revogação;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX080 — Propósito da cerimônia.** Qual é o propósito da cerimônia de chaves? *Rubrica:* 3 = produzir evidências de que nenhuma pessoa sozinha jamais teve a chave raiz;; 2 = evidências;; 1 = velocidade;; 0 = nenhuma.

- **EX081 — Lacuna encontrada.** Que lacuna o mapa de riscos revelou, e como ela foi fechada? *Rubrica:* 3 = a deriva de relógio só tinha controle corretivo; acrescentou-se um controle detectivo que acompanha o desvio;; 2 = lacuna nomeada;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Controles preventivos, detectivos e corretivos equilibrados, evidenciados por cerimônias e associados aos riscos, mantêm o serviço de confiança resiliente.

<a id="ch-28"></a>

## Capítulo 28 — Criptografia e serviços de confiança: implementação I

### Objetivos de aprendizagem

Você vai (1) implementar a verificação do firmware com um manifesto de hashes e uma assinatura; (2) explicar por que o manifesto precisa ser assinado; (3) integrar a verificação ao processo de atualização.

### 28.1 O caminho de atualização do firmware

Aiyana implementa a primeira parte do caminho de atualização do firmware. O sistema de build produz uma imagem e um manifesto que contém a versão e o digest SHA-256 da imagem. O manifesto é assinado com a chave de assinatura intermediária. Os medidores baixam os dois, verificam a assinatura do manifesto contra a cadeia embutida de raiz e intermediária, conferem que a versão é mais nova e depois calculam o hash da imagem e o comparam com o digest do manifesto. Só se todas as verificações passarem o medidor grava a imagem no seu slot inativo e reinicia a partir dele.

### Laboratório — Verificação do manifesto

```python
"""Verify a synthetic firmware image against a SHA-256 manifest before install (FIPS 180-4)."""
import hashlib
IMAGE = b"RIDGEWAY-METER-FW v3.2.1\n" + bytes(range(256)) * 4
MANIFEST = {"version": "3.2.1", "sha256": hashlib.sha256(IMAGE).hexdigest()}

def check(img):
    return hashlib.sha256(img).hexdigest() == MANIFEST["sha256"]

def main():
    print("manifest digest", MANIFEST["sha256"][:20], "...")
    print("intact image accepted:", check(IMAGE))
    bad = bytearray(IMAGE); bad[100] ^= 1
    print("one flipped bit accepted:", check(bytes(bad)))
    print("note: the manifest itself must be signed, or an attacker swaps both")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_manifest.py`. Saída verificada:

```text
manifest digest 29de505e903e58072161 ...
intact image accepted: True
one flipped bit accepted: False
note: the manifest itself must be signed, or an attacker swaps both
```

### 28.2 Ler a verificação do manifesto

O laboratório calcula o digest SHA-256 de uma imagem sintética e o guarda num manifesto. A imagem intacta é aceita; inverter um único bit faz a verificação falhar, ilustrando a propriedade de avalanche dos hashes do FIPS 180-4. A última linha do laboratório enuncia a lição principal: um hash sozinho prova apenas que a imagem coincide com o manifesto. Um atacante que consiga substituir tanto a imagem quanto um manifesto não assinado vence com facilidade. É a assinatura sobre o manifesto, feita com ECDSA ou Ed25519 numa biblioteca avaliada, que vincula o digest à Ridgeway.

### 28.3 Detalhes de integração

Aiyana trata dos detalhes práticos. Os medidores mantêm dois slots de firmware, para que uma atualização que falhe possa voltar à versão anterior sem inutilizar o aparelho. A verificação acontece antes da gravação e de novo na inicialização. Imagens grandes têm o hash calculado em blocos, para caber na memória do medidor, usando o método de atualização incremental do hashlib. Os medidores reportam a versão instalada e o resultado da verificação, alimentando a medida de sucesso do firmware do Capítulo 20. Ela documenta que a verificação de assinaturas usa no medidor a biblioteca certificada do fornecedor, e não o código dela. Os relatos de verificações que falharam vão para o sistema de alertas descrito anteriormente.

### Exemplo resolvido

Aiyana implementa a verificação baseada em manifesto, com assinatura, verificação de versão, dois slots e nova verificação na inicialização, e mostra que um único bit invertido faz o hash falhar.

> **Caso sintético.** A imagem e o manifesto são inventados; o FIPS 180-4 é real.

### Erros e limites

Um hash sem assinatura não autentica nada diante de um atacante ativo. Os dois slots precisam de proteção contra rollback, para que os atacantes não consigam forçar versões antigas.

### Exercícios

- **EX082 — Ordem das verificações.** Liste as verificações que um medidor faz antes de instalar o firmware. *Rubrica:* 3 = cadeia de assinatura do manifesto, versão mais nova, hash da imagem igual ao do manifesto;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX083 — Bit invertido.** O que aconteceu quando um bit foi invertido? *Rubrica:* 3 = a imagem foi rejeitada (accepted: False);; 2 = rejeitada;; 1 = aceita;; 0 = nenhuma.

- **EX084 — Manifesto não assinado.** Por que o manifesto precisa ser assinado? *Rubrica:* 3 = do contrário, um atacante troca a imagem e o manifesto juntos;; 2 = troca;; 1 = não é preciso;; 0 = nenhuma.

### Síntese

A verificação do firmware liga um hash da imagem a um manifesto assinado, conferido antes da instalação e na inicialização, com slots seguros de reversão.

<a id="ch-29"></a>

## Capítulo 29 — Criptografia e serviços de confiança: medição

### Objetivos de aprendizagem

Você vai (1) medir a saúde do gerenciamento de chaves com dados do inventário; (2) relatar as chaves vencidas em relação aos criptoperíodos; (3) construir um painel de medição que leve à ação.

### 29.1 O que medir

Aiyana projeta métricas para o serviço de confiança: a proporção de chaves dentro do criptoperíodo, os dias até a expiração dos certificados, as taxas de falhas de verificação, a dispersão das versões de firmware entre os medidores e o tempo para revogar uma chave comprometida em exercícios. O SP 800-57 Part 1 recomenda criptoperíodos para os tipos de chave; medir a aderência transforma essa orientação em informação gerencial. Cada métrica tem definição, fonte de dados e meta, para que dois analistas obtenham o mesmo número a partir dos mesmos dados. Ela mantém a lista curta, porque um painel com cinquenta métricas esconde as poucas que importam, e combina cada definição com a equipe dona dos dados.

### Laboratório — Auditoria de criptoperíodos

```python
"""Key inventory ages against a 365-day cryptoperiod (synthetic utility keys, fixed audit date)."""
from datetime import date
AUDIT = date(2026, 6, 30); PERIOD = 365
KEYS = [("telemetry-tls", date(2026, 1, 10)), ("fw-signing", date(2024, 2, 1)),
        ("db-at-rest", date(2025, 9, 1)), ("webhook-hmac", date(2025, 5, 20)), ("backup-wrap", date(2023, 11, 5))]

def main():
    over = 0
    for name, made in KEYS:
        age = (AUDIT - made).days; late = age > PERIOD; over += late
        print(f"{name:<14} age {age:>4} d {'OVERDUE' if late else ''}")
    print(f"overdue {over}/{len(KEYS)}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_rotation.py`. Saída verificada:

```text
telemetry-tls  age  171 d 
fw-signing     age  880 d OVERDUE
db-at-rest     age  302 d 
webhook-hmac   age  406 d OVERDUE
backup-wrap    age  968 d OVERDUE
overdue 3/5
```

### 29.2 Ler a auditoria

Na data sintética de auditoria, 30 de junho de 2026, três das cinco chaves amostradas excedem um criptoperíodo de 365 dias: a intermediária de assinatura do firmware, com 880 dias, a chave HMAC dos webhooks, com 406, e a chave de empacotamento dos backups, com 968. Apenas a chave TLS da telemetria e a chave do banco de dados estão dentro do período. Aiyana não entra em pânico: uma chave vencida não está necessariamente comprometida, mas quanto mais tempo uma chave é usada, mais dados ela protege e maior é o impacto de uma exposição não descoberta. Ela agenda as rotações por risco, começando pela intermediária do firmware.

### 29.3 Painéis que levam à ação

O painel de Aiyana mostra cada métrica com sua meta, tendência e dono. As chaves vencidas aparecem como uma lista com donos e datas de rotação planejadas, e não apenas como uma porcentagem. As revisões mensais perguntam por que as métricas mudaram. Ela evita métricas de vaidade, como contar as chaves geradas, que não dizem nada sobre a segurança. Quando a intermediária do firmware é rotacionada, o painel registra a mudança, e a proporção de vencidas cai de três em cinco para duas em cinco, dando à equipe um progresso visível. Os donos precisam explicar qualquer item vermelho na revisão seguinte.

### Exemplo resolvido

A auditoria de Aiyana encontra três de cinco chaves vencidas, agenda a rotação começando pela intermediária do firmware e constrói um painel de métricas com donos e metas.

> **Caso sintético.** As chaves e as datas são inventadas; o SP 800-57 Part 1 é real.

### Erros e limites

Métricas podem estimular manipulação, como renomear chaves para zerar sua idade. Os criptoperíodos são orientações a adaptar ao risco, e não constantes universais.

### Exercícios

- **EX085 — Chaves vencidas.** Quais chaves amostradas estavam vencidas, e com que idade? *Rubrica:* 3 = fw-signing 880, webhook-hmac 406, backup-wrap 968 dias;; 2 = nomes;; 1 = só a contagem;; 0 = nenhuma.

- **EX086 — Significado de vencida.** Vencida significa comprometida? Explique. *Rubrica:* 3 = não; o uso mais longo aumenta os dados protegidos e o impacto de uma exposição não detectada;; 2 = não;; 1 = sim;; 0 = nenhuma.

- **EX087 — Métrica de vaidade.** Dê um exemplo de métrica de vaidade que Aiyana evita. *Rubrica:* 3 = contar as chaves geradas;; 2 = semelhante;; 1 = métrica real;; 0 = nenhuma.

### Síntese

Medir a adesão aos criptoperíodos e outras métricas de saúde das chaves, com donos e metas, transforma as normas em ação.

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) planejar a verificação de controles criptográficos; (2) executar testes negativos contra a autenticação das leituras; (3) registrar evidências para a garantia.

### 30.1 Planejar a verificação

No primeiro laboratório de verificação, a equipe de Aiyana testa o projeto de autenticação das leituras numa bancada com dez medidores de teste, um concentrador e uma cópia do verificador do faturamento. O plano de testes lista cada requisito, o teste, o resultado esperado e a evidência a guardar. Os testes rodam numa rede isolada, com chaves sintéticas, nunca com chaves de produção. O plano também declara o que está fora do escopo, como a adulteração física, que um laboratório posterior cobre, para que os resultados não sejam interpretados além do que mostram. Cada teste é revisado por uma segunda engenheira ou engenheiro antes de rodar.

### 30.2 Testes negativos

A equipe executa testes negativos: leituras alteradas, leituras repetidas com contadores antigos, leituras com tag gerada por uma chave revogada, leituras com tags truncadas e leituras de um identificador de medidor vinculado a outra chave. Cada uma precisa ser rejeitada e registrada. Um teste falha: as leituras com tag de uma chave revogada são aceitas por até uma hora, porque o verificador guarda em cache os estados das chaves. A equipe reduz o tempo do cache para um minuto e acrescenta um envio explícito (push) das revogações. Encontrar isso numa bancada custa muito menos do que encontrá-lo em produção.

### 30.3 Registrar as evidências

Para cada teste, a equipe registra as entradas, as saídas, os logs, as versões de software e o nome do testador e os guarda num arquivo com evidência de adulteração (tamper-evident), com digests SHA-256. Aiyana escreve um resumo: vinte e quatro testes, vinte e três aprovados de início, um reprovado, corrigido e testado de novo. As evidências apoiam a revisão do regulador e os futuros testes de regressão. Ela enfatiza que passar nos testes mostra a ausência de defeitos conhecidos nas condições testadas, e não a ausência de todos os defeitos. O arquivo é somente leitura para os testadores, para que os resultados não possam ser editados discretamente depois, e cada novo teste é acrescentado como uma nova entrada.

### Exemplo resolvido

O laboratório executa vinte e quatro testes; uma falha de revogação em cache é encontrada e corrigida encurtando o cache e enviando as revogações, e as evidências são arquivadas com digests.

> **Caso sintético.** O laboratório e os resultados são inventados.

### Erros e limites

Testes de bancada usam condições idealizadas; o comportamento em campo pode ser diferente. Testes com chaves de produção arriscam uma exposição real.

### Exercícios

- **EX088 — Regra de isolamento.** Que chaves e que rede o laboratório usa? *Rubrica:* 3 = chaves sintéticas numa rede isolada, nunca chaves de produção;; 2 = sintéticas;; 1 = produção;; 0 = nenhuma.

- **EX089 — Falha de revogação.** O que falhou, e como foi corrigido? *Rubrica:* 3 = leituras com chave revogada aceitas por uma hora por causa do cache; cache reduzido a um minuto mais envio das revogações;; 2 = só a falha;; 1 = só a correção;; 0 = nenhuma.

- **EX090 — Limites da aprovação.** O que passar em todos os testes mostra? *Rubrica:* 3 = ausência de defeitos conhecidos nas condições testadas, não de todos os defeitos;; 2 = limitado;; 1 = prova a segurança;; 0 = nenhuma.

### Síntese

Testes negativos planejados, com evidências arquivadas, encontram falhas reais cedo e sustentam afirmações de garantia honestas.

<a id="ch-31"></a>

## Capítulo 31 — Criptografia e serviços de confiança: implementação II

### Objetivos de aprendizagem

Você vai (1) implantar o TLS 1.3 com autenticação mútua para os concentradores; (2) automatizar a emissão e a renovação de certificados; (3) evitar erros comuns de configuração do TLS.

### 31.1 TLS mútuo para os concentradores

Os concentradores se conectam ao gateway da Ridgeway usando o TLS 1.3 da RFC 8446 com autenticação mútua: o gateway apresenta seu certificado, e cada concentrador apresenta um certificado de cliente emitido pela autoridade de dispositivos da Ridgeway. O gateway confere que o certificado se encadeia até a autoridade de dispositivos, não expirou e não foi revogado e associa seu titular a um registro de concentrador. Aiyana configura o gateway para aceitar apenas o TLS 1.3, removendo as versões mais antigas e suas suítes de cifras legadas, o que simplifica a configuração e elimina classes inteiras de problemas de rebaixamento (downgrade).

### 31.2 Automatizar os certificados

Os certificados dos concentradores duram noventa dias e são renovados automaticamente por um serviço ACME interno, usando o protocolo da RFC 8555. Cada concentrador gera seu par de chaves localmente, de modo que a chave privada nunca sai do dispositivo, e solicita um certificado provando o controle da sua identidade. A renovação começa quando resta um terço da validade. Renovações que falham geram alertas, seguindo a lição de que a automação pode falhar silenciosamente. Aiyana testa a renovação adiantando o relógio de um concentrador de teste e confirmando que ele renova e que o gateway aceita o novo certificado.

### 31.3 Armadilhas de configuração

Aiyana lista os erros de TLS que ela verifica: desativar a verificação de certificados nos clientes para contornar um erro; confiar nas raízes públicas do sistema operacional para os certificados de dispositivos, em vez de apenas na autoridade da Ridgeway; pular as verificações de nome de host ou de identidade; e usar uma mesma chave de certificado em muitos concentradores. Ela escreve testes automatizados de configuração que se conectam com um certificado expirado, um certificado de outra autoridade e um certificado revogado e confirma que cada um é rejeitado. Esses testes rodam sempre que a configuração do gateway muda. Um teste que falha bloqueia a implantação até que alguém corrija a causa.

### Exemplo resolvido

Aiyana implanta a autenticação mútua somente com TLS 1.3, com certificados ACME de noventa dias gerados no dispositivo, e acrescenta testes de configuração para certificados expirados, de outras autoridades e revogados.

> **Caso sintético.** A autoridade de dispositivos é inventada; a RFC 8446 e a RFC 8555 são reais.

### Erros e limites

O TLS mútuo aumenta o trabalho de gerenciamento de certificados; a automação precisa ser monitorada. Confiar em raízes públicas para uma identidade privada de dispositivos permite que pessoas de fora se autentiquem.

### Exercícios

- **EX091 — Autenticação mútua.** O que o TLS mútuo acrescenta para os concentradores? *Rubrica:* 3 = os concentradores apresentam certificados de cliente da autoridade de dispositivos da Ridgeway, verificados pelo gateway;; 2 = certificado de cliente;; 1 = cifração;; 0 = nenhuma.

- **EX092 — Local da geração das chaves.** Onde são geradas as chaves privadas dos concentradores, e por quê? *Rubrica:* 3 = no concentrador, para que as chaves nunca saiam do dispositivo;; 2 = localmente;; 1 = centralmente;; 0 = nenhuma.

- **EX093 — Armadilha das raízes.** Por que não confiar em raízes públicas para os certificados de dispositivos? *Rubrica:* 3 = qualquer pessoa com um certificado público poderia se autenticar como dispositivo; confiar apenas na autoridade da Ridgeway;; 2 = pessoas de fora;; 1 = tudo bem;; 0 = nenhuma.

### Síntese

O TLS mútuo com certificados automatizados e gerados nos dispositivos e com configurações testadas protege os enlaces dos coletores sem trabalho manual.

<a id="ch-32"></a>

## Capítulo 32 — Criptografia e serviços de confiança: confiabilidade

### Objetivos de aprendizagem

Você vai (1) modelar a disponibilidade dos custodiantes de chaves e dos serviços; (2) escolher tamanhos de quórum para a recuperação; (3) projetar redundância sem enfraquecer a segurança.

### 32.1 Confiabilidade das pessoas e dos serviços

Uma chave que não pode ser usada quando necessário é uma falha de confiabilidade. Aiyana modela o processo de recuperação da raiz do firmware, que exige custodiantes com smart cards. Se apenas um custodiante guardar o backup da raiz, a raiz ficará indisponível sempre que essa pessoa estiver doente ou viajando, e perdida se ela sair. Se todos os cinco precisarem estar presentes, a disponibilidade cai bruscamente. Esquemas de quórum, em que quaisquer m de n custodiantes bastam, equilibram as duas coisas. Ela usa probabilidade para escolher m e n, dada a disponibilidade de cada custodiante.

### Laboratório — Quórum de custodiantes

```python
"""Probability that at least m of n key custodians are reachable (each independently with prob a)."""
from math import comb

def at_least(m, n, a):
    return sum(comb(n, k) * a ** k * (1 - a) ** (n - k) for k in range(m, n + 1))

def main():
    for m, n in [(1, 1), (2, 3), (3, 5), (5, 5)]:
        print(f"{m}-of-{n}, each 0.90 reachable: P = {at_least(m, n, 0.90):.4f}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_quorum.py`. Saída verificada:

```text
1-of-1, each 0.90 reachable: P = 0.9000
2-of-3, each 0.90 reachable: P = 0.9720
3-of-5, each 0.90 reachable: P = 0.9914
5-of-5, each 0.90 reachable: P = 0.5905
```

### 32.2 Ler os resultados do quórum

Com cada custodiante alcançável 90 por cento do tempo, um único custodiante dá disponibilidade de 0,90, dois de três dão 0,972, três de cinco dão 0,9914, e exigir todos os cinco dá apenas 0,5905. Exigir todo mundo é pior do que depender de uma só pessoa. Aiyana recomenda três de cinco para a raiz: alta disponibilidade, e nenhum par de custodiantes consegue conspirar para recuperar a chave sozinho. O recurso de divisão de chaves do fornecedor do HSM implementa a divisão; ela não implementa por conta própria o compartilhamento de segredos, coerente com a regra contra a criptografia caseira. Sua escolha é registrada na política de gerenciamento de chaves.

### 32.3 Redundância para os serviços

Para o serviço de chaves online, Aiyana projeta réplicas ativo-standby em dois data centers, com as chaves replicadas em forma cifrada entre HSMs do mesmo modelo. A replicação usa o mecanismo seguro de transferência de chaves do fornecedor, de modo que as chaves nunca aparecem em texto claro. O failover é testado a cada trimestre. Ela registra um trade-off: mais réplicas significam mais lugares a proteger e auditar. Ela limita as réplicas a dois sites e exige os mesmos controles físicos em ambos. Confiabilidade e segurança só se reforçam mutuamente quando a redundância é projetada com o mesmo rigor que o sistema primário.

### Exemplo resolvido

Aiyana escolhe um quórum de três de cinco custodiantes (disponibilidade de 0,9914) implementado pelo fornecedor do HSM e réplicas ativo-standby do serviço de chaves em dois sites, com testes trimestrais de failover.

> **Caso sintético.** Os números de disponibilidade são premissas inventadas.

### Erros e limites

As premissas de independência falham se os custodiantes viajarem juntos ou trabalharem no mesmo prédio. Mais réplicas aumentam a superfície de ataque.

### Exercícios

- **EX094 — Quórum de todos os cinco.** Que disponibilidade se obtém exigindo todos os cinco custodiantes, e por que isso é ruim? *Rubrica:* 3 = 0,5905, pior do que um único custodiante;; 2 = número;; 1 = bom;; 0 = nenhuma.

- **EX095 — Quórum recomendado.** Que quórum Aiyana recomenda, e por quê? *Rubrica:* 3 = três de cinco: disponibilidade de 0,9914, e nenhum par consegue conspirar;; 2 = 3 de 5;; 1 = 1 de 1;; 0 = nenhuma.

- **EX096 — Implementação da divisão.** Quem implementa a divisão da chave, e por quê? *Rubrica:* 3 = o recurso do fornecedor do HSM, evitando a criptografia caseira;; 2 = fornecedor;; 1 = Aiyana;; 0 = nenhuma.

### Síntese

Projetos de quórum e de redundância mantêm as chaves disponíveis sem concentrar poder, desde que construídos sobre mecanismos avaliados e testados.

<a id="ch-33"></a>

## Capítulo 33 — Criptografia e serviços de confiança: segurança e resiliência

### Objetivos de aprendizagem

Você vai (1) projetar um comportamento seguro para quando as verificações criptográficas falham; (2) planejar o comprometimento de chaves de assinatura; (3) incorporar resiliência aos medidores e aos serviços.

### 33.1 Falhar com segurança

Partindo do Capítulo 10, Aiyana especifica o comportamento para cada falha criptográfica. Se a tag de uma leitura falha, o faturamento a guarda em quarentena e alerta, em vez de descartá-la, para que a evidência permaneça. Se a assinatura de um firmware falha, o medidor mantém o firmware atual e reporta. Se o certificado de um concentrador expira, o concentrador guarda as leituras em buffer por até sete dias enquanto alerta as operações, de modo que as leituras atrasam, mas não se perdem. Cada comportamento é testado. O objetivo é que as falhas criptográficas causem atrasos visíveis e recuperáveis, e não perda silenciosa de dados ou estados inseguros.

### 33.2 Comprometimento da chave de assinatura

Aiyana planeja para o pior caso: a chave de assinatura intermediária do firmware vaza. O runbook de resposta revoga a intermediária publicando uma revogação assinada pela raiz offline, emite uma nova intermediária numa cerimônia, assina de novo o firmware atual e envia uma atualização que instala a confiança na nova intermediária. Como os medidores verificam a cadeia contra a raiz, a intermediária revogada se torna inútil. Ela estima o tempo para concluir a resposta e a pratica num exercício de mesa (tabletop), identificando passos lentos, como reunir os custodiantes em cima da hora.

### 33.3 Recursos de resiliência

Aiyana acrescenta recursos que ajudam o sistema a sobreviver a surpresas: os medidores guardam duas âncoras de confiança, a raiz atual e uma raiz de reserva pré-provisionada, mantida offline e criada numa cerimônia separada, para que a perda da raiz primária seja contornável; o firmware oferece agilidade de algoritmos, permitindo um futuro esquema de assinatura pós-quântica do FIPS 204 ou do FIPS 205; e os concentradores podem recorrer a um segundo gateway. A resiliência custa dinheiro e complexidade, então cada recurso é ligado a um risco específico da análise. Cada recurso é revisado anualmente para confirmar que seu risco ainda existe.

### Exemplo resolvido

Aiyana especifica a quarentena para leituras que falham, a manutenção do firmware atual quando o novo falha, o buffer de sete dias para certificados de concentradores expirados e um runbook ensaiado para o comprometimento da chave intermediária, com uma raiz de reserva.

> **Caso sintético.** O runbook e os recursos são inventados; o FIPS 204 e o FIPS 205 são reais.

### Erros e limites

As raízes de reserva precisam ser protegidas com tanto cuidado quanto as primárias. Runbooks não testados falham sob pressão.

### Exercícios

- **EX097 — Comportamento com tag inválida.** O que acontece com uma leitura cuja tag falha? *Rubrica:* 3 = fica em quarentena com alerta, não é descartada, preservando a evidência;; 2 = quarentena;; 1 = descartada;; 0 = nenhuma.

- **EX098 — Comprometimento da intermediária.** Resuma a resposta a um vazamento da chave intermediária do firmware. *Rubrica:* 3 = revogação assinada pela raiz, nova intermediária em cerimônia, nova assinatura do firmware, envio da nova confiança;; 2 = parcial;; 1 = ignorar;; 0 = nenhuma.

- **EX099 — Raiz de reserva.** Por que os medidores guardam uma raiz de reserva? *Rubrica:* 3 = a perda ou o comprometimento da raiz primária continua contornável;; 2 = resiliência;; 1 = nenhum motivo;; 0 = nenhuma.

### Síntese

Um comportamento seguro diante de falhas, uma resposta a comprometimentos ensaiada e uma resiliência planejada permitem que os sistemas criptográficos se degradem de forma controlada.

<a id="ch-34"></a>

## Capítulo 34 — Criptografia e serviços de confiança: integração

### Objetivos de aprendizagem

Você vai (1) integrar o serviço de confiança ao faturamento, às operações de campo e ao monitoramento; (2) definir contratos de interface; (3) testar os fluxos de ponta a ponta.

### 34.1 Pontos de integração

O serviço de confiança toca muitos sistemas: o faturamento verifica as leituras, as operações de campo provisionam medidores substitutos, o monitoramento recebe alertas, o sistema de build solicita assinaturas de firmware e o gerenciamento de identidades controla o acesso da equipe. Aiyana lista cada integração com seus dados, protocolo e autenticação. Ela descobre que a ferramenta portátil das operações de campo precisa solicitar uma nova chave de medidor durante a substituição, o que não tinha sido projetado. A análise de integração revela fluxos ausentes como esse antes da implantação, quando mudar as interfaces ainda é barato. Ela registra cada fluxo numa tabela compartilhada que as equipes donas revisam juntas.

### 34.2 Contratos de interface

Para cada integração, Aiyana escreve um contrato: formatos de requisição e de resposta, códigos de erro, limites de taxa, método de autenticação e o que acontece quando o tempo se esgota (timeout). O contrato de assinatura diz que o sistema de build envia o digest do manifesto, e não a imagem inteira, e só recebe uma assinatura se dois aprovadores tiverem autorizado a versão. O contrato de provisionamento de chaves diz que as ferramentas portáteis nunca recebem chaves de medidor; elas recebem um blob cifrado que só o elemento seguro do medidor de destino consegue desembrulhar. Os contratos permitem que as equipes trabalhem de forma independente, preservando as propriedades de segurança.

### 34.3 Testes de ponta a ponta

Aiyana executa testes de ponta a ponta que atravessam todas as integrações: provisionar um medidor substituto, obter uma leitura, verificá-la no faturamento, enviar uma atualização de firmware, revogar o medidor antigo e confirmar que suas leituras são rejeitadas. Os testes rodam num ambiente de homologação (staging) com chaves sintéticas. Um teste revela que o faturamento ainda aceita as leituras do medidor antigo, porque o evento de revogação vai para o monitoramento, mas não para o faturamento. A correção encaminha as revogações por uma fila de mensagens que todos os verificadores assinam. Esses testes rodam antes de cada versão de qualquer sistema conectado.

### Exemplo resolvido

Aiyana mapeia cinco integrações, escreve contratos para a assinatura e o provisionamento e descobre, com testes de ponta a ponta, que os eventos de revogação nunca chegavam ao faturamento.

> **Caso sintético.** Os sistemas são inventados.

### Erros e limites

Os contratos se desviam se não forem testados automaticamente. Os testes de ponta a ponta são lentos, então mantenha-os focados nos fluxos críticos para a segurança.

### Exercícios

- **EX100 — Fluxo ausente.** Que fluxo faltava antes da análise de integração? *Rubrica:* 3 = a ferramenta portátil solicitando uma nova chave de medidor durante a substituição;; 2 = provisionamento;; 1 = nenhum;; 0 = nenhuma.

- **EX101 — Blob da ferramenta portátil.** Por que as ferramentas portáteis recebem um blob cifrado em vez de uma chave? *Rubrica:* 3 = só o elemento seguro do medidor consegue desembrulhá-lo, então as ferramentas nunca guardam chaves;; 2 = proteger a chave;; 1 = velocidade;; 0 = nenhuma.

- **EX102 — Encaminhamento da revogação.** O que os testes de ponta a ponta revelaram sobre a revogação, e o que corrigiu isso? *Rubrica:* 3 = as revogações chegavam ao monitoramento, mas não ao faturamento; encaminhá-las por uma fila que todos os verificadores assinam;; 2 = só o achado;; 1 = só a correção;; 0 = nenhuma.

### Síntese

A integração com contratos explícitos e testes de ponta a ponta faz o serviço de confiança funcionar entre sistemas sem vazar chaves nem perder eventos.

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) reprojetar o sistema para um novo requisito; (2) avaliar a prontidão pós-quântica; (3) apresentar um plano de migração para crítica.

### 35.1 O novo requisito

No segundo ateliê de projeto, o regulador anuncia que as companhias precisam planejar a migração das assinaturas de longa duração para algoritmos pós-quânticos. Os medidores duram quinze anos, então o firmware assinado hoje precisa continuar verificável e seguro até por volta de 2041. A equipe de Aiyana precisa reprojetar a assinatura do firmware para que os medidores aceitem assinaturas pós-quânticas sem substituição de hardware. Eles leem o FIPS 204, do ML-DSA, e o FIPS 205, do SLH-DSA, e anotam que ambos produzem assinaturas e chaves muito maiores que as do Ed25519 ou do ECDSA. A equipe também lê as orientações de transição do NIST, para que o plano acompanhe os prazos esperados, e registra quais gerações de medidores podem ser atualizadas em campo.

### 35.2 Avaliar as opções

A equipe compara as opções. O ML-DSA oferece assinaturas de tamanho moderado, de alguns kilobytes, e verificação rápida; o SLH-DSA depende apenas de funções de hash, oferecendo premissas de segurança conservadoras, com assinaturas maiores. Um esquema híbrido exige que tanto uma assinatura clássica quanto uma pós-quântica sejam verificadas, protegendo contra a falha de qualquer uma delas. Para o firmware, o tamanho importa menos do que para as leituras, porque as atualizações são pouco frequentes. A equipe propõe assinaturas híbridas ECDSA mais ML-DSA nos manifestos, com os medidores aceitando o firmware apenas quando as duas forem verificadas, e uma fase posterior que abandona a assinatura clássica.

### 35.3 Crítica e plano

Os revisores questionam se os medidores têm memória e flash suficientes para verificar assinaturas pós-quânticas. A equipe mede com a biblioteca do fornecedor num medidor de teste e descobre que a verificação cabe, mas exige uma atualização de firmware do bootloader, que por sua vez precisa ser assinada de forma clássica. Eles escrevem um plano de migração: atualizar agora os bootloaders com assinaturas clássicas, introduzir em seguida os manifestos híbridos e aposentar a verificação somente clássica depois que a confiança aumentar. Cada passo tem um rollback. Os revisores aceitam o plano, com o pedido de acompanhar as orientações do NIST sobre os prazos de transição.

### Exemplo resolvido

A equipe propõe assinaturas híbridas ECDSA mais ML-DSA nos manifestos, verifica a viabilidade num medidor de teste e escalona a migração por meio de uma atualização do bootloader assinada de forma clássica.

> **Caso sintético.** A regra do regulador e as medições são inventadas; o FIPS 204 e o FIPS 205 são reais.

### Erros e limites

Esquemas híbridos aumentam a complexidade e o tamanho; precisam ser projetados por especialistas e implementados com bibliotecas avaliadas. Os prazos mudam, então os planos precisam de revisão.

### Exercícios

- **EX103 — Por que planejar agora.** Por que a Ridgeway precisa planejar agora a assinatura pós-quântica do firmware? *Rubrica:* 3 = os medidores duram quinze anos, então as assinaturas precisam continuar seguras até por volta de 2041;; 2 = vida longa;; 1 = não é preciso;; 0 = nenhuma.

- **EX104 — Regra híbrida.** Como o esquema híbrido proposto aceita o firmware? *Rubrica:* 3 = só quando as assinaturas ECDSA e ML-DSA forem ambas verificadas;; 2 = ambas;; 1 = qualquer uma;; 0 = nenhuma.

- **EX105 — Passo do bootloader.** Por que o plano começa com uma atualização do bootloader? *Rubrica:* 3 = verificar assinaturas PQ exige um bootloader atualizado, ele próprio assinado de forma clássica;; 2 = bootloader;; 1 = pular;; 0 = nenhuma.

### Síntese

A prontidão pós-quântica para dispositivos de vida longa exige uma migração antecipada, escalonada e híbrida, fundamentada em medições e em normas.

<a id="ch-36"></a>

## Capítulo 36 — Criptografia e serviços de confiança: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) estimar a carga de trabalho criptográfica na escala da frota; (2) ajustar os custos do hash de senhas e da verificação; (3) planejar a capacidade para os picos.

### 36.1 Carga da frota

Aiyana estima a carga: 50.000 medidores reportando a cada hora produzem cerca de 1,2 milhão de leituras por dia, e cada uma precisa de uma verificação HMAC. O HMAC-SHA256 sobre mensagens curtas leva microssegundos em servidores modernos, então a verificação é barata; o gargalo está nas gravações no banco de dados e nas consultas de chaves. Ela projeta um cache de chaves derivadas na memória protegida do verificador, renovado quando as chaves são rotacionadas. Estimar primeiro evita desperdiçar otimização na criptografia quando o custo real está em outro lugar. Ela confirma a estimativa com um teste de carga em homologação, que mostra o HMAC usando menos de um por cento do processador, enquanto a fila do banco de dados cresce durante as rajadas.

### 36.2 Custos do hash de senhas

O portal dos clientes usa o Argon2id da RFC 9106, que é deliberadamente lento. Aiyana ajusta os parâmetros para que cada login leve cerca de meio segundo no servidor e use memória suficiente para atrasar atacantes com hardware especializado. No pico, quando as contas são emitidas, milhares de clientes entram em uma hora. Ela calcula a capacidade de servidor necessária e acrescenta limitação de taxa por conta e por endereço de rede, para que os atacantes não possam usar os logins para esgotar os recursos. O ajuste equilibra a experiência do usuário, a capacidade e a resistência a palpites offline.

### 36.3 Planejar os picos

As implantações de firmware criam picos: se todos os 50.000 medidores baixassem e verificassem ao mesmo tempo, os concentradores ficariam saturados. Aiyana escalona as atualizações em ondas de cinco por cento, monitora os resultados das verificações e pausa automaticamente se as falhas excederem um limiar. As renovações de certificados também são espalhadas, acrescentando um jitter aleatório aos horários de renovação, o que evita a situação em que todos os concentradores renovam no mesmo minuto. O planejamento de capacidade para a criptografia costuma ser uma questão de agendamento, e não de velocidade bruta. Ela também ensaia uma pausa da implantação, para que os operadores saibam interromper rapidamente uma onda se as falhas de verificação aumentarem durante uma atualização.

### Exemplo resolvido

Aiyana estima 1,2 milhão de verificações diárias, guarda em cache as chaves derivadas, ajusta o Argon2id para cerca de meio segundo com limites de taxa e escalona o firmware e as renovações.

> **Caso sintético.** Os números de carga são inventados; a RFC 9106 é real.

### Erros e limites

Reduzir o custo do hash de senhas para economizar capacidade enfraquece a proteção. Os caches de chaves precisam ser protegidos como o serviço de chaves.

### Exercícios

- **EX106 — Leituras diárias.** Quantas leituras por dia a frota produz? *Rubrica:* 3 = cerca de 1,2 milhão;; 2 = ordem de grandeza certa;; 1 = errado;; 0 = nenhuma.

- **EX107 — Gargalo real.** Onde está o gargalo da verificação das leituras? *Rubrica:* 3 = nas gravações no banco de dados e nas consultas de chaves, não no HMAC;; 2 = banco de dados;; 1 = HMAC;; 0 = nenhuma.

- **EX108 — Jitter da renovação.** Por que acrescentar jitter às renovações de certificados? *Rubrica:* 3 = para evitar que todos os concentradores renovem ao mesmo tempo e sobrecarreguem os serviços;; 2 = espalhar a carga;; 1 = segurança;; 0 = nenhuma.

### Síntese

Em escala, o desempenho criptográfico depende de estimar a carga, ajustar os custos deliberados e programar os picos, mais do que da velocidade bruta dos algoritmos.

<a id="ch-37"></a>

## Capítulo 37 — Criptografia e serviços de confiança: operações

### Objetivos de aprendizagem

Você vai (1) escrever runbooks operacionais para tarefas rotineiras com chaves; (2) rotacionar chaves sem indisponibilidade; (3) tratar incidentes que envolvem chaves.

### 37.1 Runbooks de rotina

Aiyana escreve runbooks para as tarefas de rotina: rotacionar as chaves das leituras, renovar os certificados do gateway, acrescentar um custodiante, substituir um HSM e responder a alertas de falhas de verificação. Cada runbook lista pré-condições, passos, verificações e rollback. Ela testa cada um com um operador que não o escreveu e revisa os passos pouco claros. Os runbooks transformam o conhecimento especializado em operações repetíveis e reduzem os erros às 3 da manhã, quando os incidentes parecem acontecer. Eles também dão aos auditores evidências de que os procedimentos existem e são seguidos. Cada runbook nomeia seu dono e a data em que foi exercitado pela última vez.

### 37.2 Rotação sem indisponibilidade

Rotacionar as chaves das leituras de 50.000 medidores não pode acontecer de uma só vez. Aiyana projeta uma validade sobreposta: o serviço de chaves deriva as chaves da versão 4 e as envia aos medidores em ondas; o faturamento aceita tags das versões 3 e 4 durante a transição; depois que todos os medidores confirmam, a versão 3 é desativada e usada apenas para verificar leituras históricas. A versão da chave em cada mensagem, acrescentada no Ateliê de projeto I, torna isso possível. O monitoramento acompanha a proporção de leituras na nova versão, dando aos operadores uma visão clara do progresso.

### 37.3 Incidentes com chaves

Quando um técnico relata a perda de uma ferramenta portátil, a equipe de Aiyana segue o runbook de incidentes com chaves: confirmar o que a ferramenta podia acessar, que, segundo o Capítulo 34, são apenas blobs cifrados; revogar as credenciais da própria ferramenta; revisar os logs em busca de uso indevido; e registrar o incidente. Como as ferramentas portáteis nunca guardam chaves de medidor, nenhuma rotação nos medidores é necessária. Ela contrasta isso com um incidente hipotético em que vazam as credenciais de um administrador do serviço de chaves, o que exigiria uma rotação mais ampla. Projetos que limitam o que cada componente guarda tornam os incidentes pequenos.

### Exemplo resolvido

Os runbooks de Aiyana são testados por outros operadores, as chaves das leituras da versão 4 são implantadas com aceitação sobreposta e a perda de uma ferramenta portátil é contida sem rotação nos medidores.

> **Caso sintético.** Os incidentes e as versões são inventados.

### Erros e limites

Períodos de sobreposição que nunca terminam deixam chaves antigas ativas. Os runbooks precisam ser atualizados depois de cada uso.

### Exercícios

- **EX109 — Teste dos runbooks.** Como Aiyana testou os runbooks? *Rubrica:* 3 = um operador que não os escreveu os seguiu, e os passos pouco claros foram revisados;; 2 = testados;; 1 = não testados;; 0 = nenhuma.

- **EX110 — Validade sobreposta.** Como as chaves das leituras são rotacionadas sem indisponibilidade? *Rubrica:* 3 = enviar a v4 em ondas, o faturamento aceita v3 e v4, desativar a v3 depois que todos confirmam;; 2 = sobreposição;; 1 = tudo de uma vez;; 0 = nenhuma.

- **EX111 — Ferramenta portátil perdida.** Por que a ferramenta perdida não exigiu rotação nos medidores? *Rubrica:* 3 = as ferramentas guardam apenas blobs cifrados, nunca chaves de medidor;; 2 = sem chaves;; 1 = sorte;; 0 = nenhuma.

### Síntese

Runbooks testados, rotação com sobreposição e projetos que limitam o que os componentes guardam tornam as operações criptográficas tranquilas e os incidentes pequenos.

<a id="ch-38"></a>

## Capítulo 38 — Criptografia e serviços de confiança: validação

### Objetivos de aprendizagem

Você vai (1) validar que o serviço de confiança atende às necessidades das partes interessadas; (2) contratar testes independentes; (3) interpretar com honestidade os resultados da validação.

### 38.1 Verificação versus validação

A verificação pergunta se o sistema foi construído conforme especificado; a validação pergunta se ele atende às necessidades reais. Os laboratórios de Aiyana verificaram os requisitos. A validação pergunta às partes interessadas: os técnicos provisionam medidores em menos de dez minutos? Os operadores entendem os alertas? O regulador aceita as evidências? Ela conduz um piloto de campo com 500 medidores num distrito durante três meses, coletando dados sobre cada medida de sucesso do Capítulo 20. Vários requisitos foram atendidos no laboratório, mas não em campo, como o tempo de provisionamento quando o sinal móvel é fraco.

### 38.2 Testes independentes

A Ridgeway contrata uma empresa de segurança independente para tentar forjar leituras, instalar firmware não assinado e extrair chaves de uma amostra de medidores, com autorização por escrito e num distrito de teste. A empresa não encontra como forjar leituras nem instalar firmware não assinado, mas extrai a chave de um protótipo de medidor sem elemento seguro, confirmando a decisão anterior de exigir elementos seguros. Os testes independentes trazem uma criatividade de atacante que falta à equipe de projeto e fornecem evidências críveis ao regulador.

### 38.3 Interpretação honesta

Aiyana escreve o relatório de validação. O provisionamento atingiu a meta de dez minutos em 91 por cento dos casos; as falhas vieram de sinal fraco, tratadas permitindo o provisionamento offline com sincronização posterior. Nenhuma leitura forjada foi aceita nos testes, mas ela anota que o teste cobriu três meses e um distrito. As atualizações de firmware chegaram a 97 por cento dos medidores do piloto em até trinta dias, abaixo da meta de 99 por cento, porque alguns medidores estavam inalcançáveis em caixas inundadas. Ela relata as metas não atingidas com a mesma clareza que os sucessos, com ações corretivas. As ações corretivas recebem donos e datas para a revisão seguinte.

### Exemplo resolvido

O piloto com 500 medidores e o teste independente não mostram falsificação nem firmware não assinado, confirmam a decisão pelo elemento seguro e relatam, com as correções, as metas não atingidas de provisionamento e de alcance do firmware.

> **Caso sintético.** O piloto, a empresa e os números são inventados.

### Erros e limites

A validação num distrito pode não representar toda a área de atendimento. Os testes independentes são limitados pelo escopo e pelo tempo.

### Exercícios

- **EX112 — Pergunta da validação.** Em que a validação difere da verificação? *Rubrica:* 3 = a validação confere as necessidades reais das partes interessadas; a verificação confere o que foi construído contra a especificação;; 2 = diferença parcial;; 1 = iguais;; 0 = nenhuma.

- **EX113 — Extração de chave.** O que o teste independente extraiu, e o que isso confirmou? *Rubrica:* 3 = uma chave de um protótipo sem elemento seguro, confirmando o requisito de elemento seguro;; 2 = achado;; 1 = nada;; 0 = nenhuma.

- **EX114 — Meta do firmware não atingida.** Que resultado do firmware ficou abaixo da meta, e por quê? *Rubrica:* 3 = 97 por cento em trinta dias contra 99, por causa de medidores inalcançáveis em caixas inundadas;; 2 = número;; 1 = motivo;; 0 = nenhuma.

### Síntese

A validação em campo, os testes independentes e o relato honesto das falhas mostram se o serviço de confiança realmente atende às suas partes interessadas.

<a id="ch-39"></a>

## Capítulo 39 — Criptografia e serviços de confiança: manutenibilidade

### Objetivos de aprendizagem

Você vai (1) projetar para a agilidade criptográfica; (2) gerenciar a obsolescência de algoritmos ao longo do tempo; (3) manter a documentação e o conhecimento atualizados.

### 39.1 Agilidade criptográfica

Os algoritmos envelhecem. O SHA-1 passou de recomendado a obsoleto durante a vida útil de sistemas que ainda estão em uso. Aiyana projeta o serviço de confiança da Ridgeway para a agilidade: as mensagens e os manifestos carregam identificadores de algoritmo; os verificadores aceitam um conjunto configurado de algoritmos; e as chaves são marcadas com seu algoritmo no inventário. Mudar de algoritmo vira então uma tarefa de configuração e implantação, e não um novo projeto. Ela adverte que a agilidade não pode permitir que os atacantes escolham opções fracas, então os verificadores recusam algoritmos removidos da lista de permitidos.

### 39.2 Gerenciar a obsolescência

Aiyana estabelece um processo de obsolescência. A cada ano, a equipe de segurança revisa as orientações do NIST, como o SP 800-131A sobre a transição de algoritmos e tamanhos de chave, e atualiza uma lista de algoritmos aprovados com datas de aposentadoria planejadas. O inventário informa quantas chaves usam cada algoritmo, para que a aposentadoria possa ser planejada. Quando um algoritmo é programado para remoção, a equipe primeiro deixa de criar novas chaves com ele, depois migra os usos existentes e, por fim, remove o suporte à verificação depois de um período de carência. A obsolescência vira rotina, e não emergência.

### 39.3 Documentação e conhecimento

A manutenibilidade também diz respeito às pessoas. Aiyana mantém os documentos de arquitetura, os registros de decisão, os runbooks e o inventário num único repositório com histórico de mudanças. Cada documento tem um dono e uma data de revisão. Os novos engenheiros seguem uma trilha de integração que inclui uma rotação de chaves supervisionada em homologação. Ela anota que muitos incidentes criptográficos em sistemas antigos começaram quando ninguém lembrava por que um projeto tinha sido escolhido, de modo que a gestão do conhecimento é um controle de segurança tão real quanto um HSM. As datas de revisão aparecem no painel, para que documentos desatualizados fiquem visíveis.

### Exemplo resolvido

Aiyana acrescenta identificadores de algoritmo e listas de permitidos, uma revisão anual de obsolescência baseada no SP 800-131A e documentação com donos, com integração por meio de uma rotação supervisionada.

> **Caso sintético.** O processo da Ridgeway é inventado; o SP 800-131A é uma publicação real do NIST.

### Erros e limites

A agilidade pode introduzir ataques de rebaixamento se opções fracas continuarem aceitas. Documentação sem dono se degrada.

### Exercícios

- **EX115 — Mecanismo de agilidade.** Cite dois mecanismos que dão agilidade. *Rubrica:* 3 = identificadores de algoritmo nas mensagens, listas de permitidos configuradas, marcação do algoritmo no inventário;; 2 = um;; 1 = nenhum;; 0 = nenhuma.

- **EX116 — Passos da obsolescência.** Quais são os três passos para aposentar um algoritmo? *Rubrica:* 3 = parar de criar novas chaves, migrar os usos existentes, remover a verificação depois da carência;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX117 — Risco de conhecimento.** Por que a gestão do conhecimento é um controle de segurança? *Rubrica:* 3 = incidentes começam quando ninguém lembra por que os projetos foram escolhidos;; 2 = memória;; 1 = não é;; 0 = nenhuma.

### Síntese

A agilidade, a descontinuação rotineira e o conhecimento mantido conservam um serviço de confiança seguro ao longo de décadas de mudanças de algoritmos e de equipe.

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem

Você vai (1) testar a resistência física e a canais laterais dos medidores; (2) executar um teste de injeção de falhas no serviço de confiança; (3) documentar o risco residual.

### 40.1 Testes físicos

O segundo laboratório testa os medidores fisicamente, com autorização e apenas em amostras de laboratório. A equipe confere que os elementos seguros resistem a sondagens simples e que as portas de depuração estão desativadas nos builds de produção. Um laboratório parceiro especializado faz medições de canal lateral na operação HMAC dentro do elemento seguro, confirmando que não há correlação mensurável com os bits da chave dentro do orçamento do teste. Aiyana registra que os resultados se aplicam à revisão de hardware testada e que uma nova revisão exige novos testes. A equipe anota o número de série de cada amostra, para que os resultados possam ser ligados a uma revisão exata.

### 40.2 Injeção de falhas

A equipe injeta falhas no serviço de confiança de homologação: o HSM primário é desligado, o relógio de um concentrador salta uma semana à frente, a fila de revogação é atrasada e uma imagem de firmware corrompida é oferecida. Cada injeção confere se ocorre o comportamento seguro projetado no Capítulo 33. O HSM de standby assume em quarenta segundos. O salto do relógio faz o concentrador apresentar um certificado como ainda não válido, que o gateway rejeita corretamente, mas a mensagem de alerta do concentrador não é clara; a equipe a reescreve.

### 40.3 Risco residual

Aiyana escreve uma declaração de risco residual: os riscos que permanecem depois dos controles, por que são aceitos e quem os aceitou. Os exemplos incluem um atacante determinado e bem financiado extraindo, com equipamento avançado, as chaves de um único medidor, aceito porque as chaves por medidor limitam o impacto; e a perda simultânea dos dois data centers, aceita com um plano de recuperação offline de vários dias. A direção assina a declaração. Tornar o risco residual explícito evita a falsa impressão de que os testes deixaram o sistema perfeitamente seguro. A declaração é revisada sempre que o modelo de ameaça muda e pelo menos uma vez por ano.

### Exemplo resolvido

O laboratório confirma as proteções do elemento seguro e das portas de depuração, passa nas injeções de falhas com um failover de HSM em quarenta segundos, esclarece um alerta de salto de relógio e registra os riscos residuais assinados.

> **Caso sintético.** Os resultados são inventados.

### Erros e limites

Os testes de canal lateral são limitados pelo orçamento e pela técnica. As declarações de risco residual precisam ser revisitadas quando as ameaças mudam.

### Exercícios

- **EX118 — Escopo do hardware.** Que limite se aplica aos resultados dos testes físicos? *Rubrica:* 3 = valem para a revisão de hardware testada; novas revisões precisam de novos testes;; 2 = revisão;; 1 = universais;; 0 = nenhuma.

- **EX119 — Salto do relógio.** O que a injeção do salto de relógio revelou? *Rubrica:* 3 = certificado rejeitado corretamente como ainda não válido, mas mensagem de alerta pouco clara e reescrita;; 2 = alerta;; 1 = falha;; 0 = nenhuma.

- **EX120 — Exemplo de risco residual.** Dê um risco residual aceito e sua justificativa. *Rubrica:* 3 = extração da chave de um medidor por atacante avançado, limitada pelas chaves por medidor (ou perda dos dois data centers, recuperação offline);; 2 = exemplo;; 1 = nenhum;; 0 = nenhuma.

### Síntese

Testes físicos, injeção de falhas e declarações de risco residual assinadas completam a verificação com um relato honesto do que resta.

<a id="ch-41"></a>

## Capítulo 41 — Criptografia e serviços de confiança: otimização do sistema

### Objetivos de aprendizagem

Você vai (1) otimizar o serviço de confiança em custo e energia sem enfraquecer a segurança; (2) reduzir o trabalho operacional repetitivo por meio da automação; (3) avaliar as otimizações em relação aos requisitos.

### 41.1 Energia nos medidores

As baterias dos medidores precisam durar quinze anos. Aiyana mede a energia por leitura: a transmissão de rádio domina, e o cálculo do HMAC no elemento seguro custa uma pequena fração. Ela otimiza agrupando quatro leituras horárias numa única transmissão, com uma única tag cobrindo o lote, o que reduz os despertares do rádio. A tag do lote cobre cada leitura e seu contador, de modo que nenhuma leitura pode ser removida ou reordenada sem ser detectada. Ela confere que o agrupamento não viola o requisito de que o faturamento receba as leituras em até seis horas e documenta o trade-off na latência.

### 41.2 Reduzir o trabalho repetitivo

A equipe de operações gasta horas por mês em solicitações manuais de certificados para serviços web internos que ficam fora do sistema ACME. Aiyana estende a emissão automatizada a esses serviços e acrescenta um relatório semanal dos certificados descobertos por varredura que não estão no inventário. Os passos manuais caem cerca de dois terços. Ela trata a própria automação como um sistema a proteger: as credenciais do serviço ACME ficam guardadas no serviço de chaves, e seus logs de emissão alimentam o monitoramento, para que a automação não vire um caminho não monitorado até os certificados.

### 41.3 Avaliar as otimizações

Cada otimização é avaliada em relação aos requisitos antes de ser adotada. Uma proposta de encurtar as tags das leituras para 8 bytes, para economizar mais energia, é rejeitada: a resistência à falsificação de 64 bits fica abaixo da meta do modelo de ameaça, e a economia é marginal, já que o custo do rádio é determinado pelos cabeçalhos. Uma proposta de reduzir os parâmetros do Argon2 para cortar custos de servidor também é rejeitada. Aiyana registra as otimizações rejeitadas com os motivos, evitando que as mesmas ideias voltem sem novas evidências. Cada ideia rejeitada é guardada com os dados que a refutaram, para que um futuro proponente veja exatamente que nova evidência seria necessária para reabri-la.

### Exemplo resolvido

Aiyana agrupa quatro leituras sob uma tag para economizar energia, automatiza os certificados internos para cortar dois terços do trabalho repetitivo e rejeita as tags de 8 bytes e os parâmetros mais fracos do Argon2, com os motivos registrados.

> **Caso sintético.** As medições são inventadas.

### Erros e limites

Otimizações que reduzem as margens de segurança costumam parecer atraentes isoladamente. O agrupamento muda a latência e a semântica do replay, o que precisa ser testado de novo.

### Exercícios

- **EX121 — Cobertura da tag do lote.** O que a tag do lote precisa cobrir, e por quê? *Rubrica:* 3 = cada leitura e seu contador, para que nenhuma possa ser removida ou reordenada sem detecção;; 2 = leituras;; 1 = só o cabeçalho;; 0 = nenhuma.

- **EX122 — Segurança da automação.** Como a própria automação é protegida? *Rubrica:* 3 = credenciais do serviço ACME no serviço de chaves e logs de emissão monitorados;; 2 = logs;; 1 = desnecessário;; 0 = nenhuma.

- **EX123 — Corte de tag rejeitado.** Por que encurtar as tags para 8 bytes foi rejeitado? *Rubrica:* 3 = resistência à falsificação de 64 bits abaixo da meta do modelo de ameaça e economia marginal;; 2 = segurança;; 1 = custo;; 0 = nenhuma.

### Síntese

A otimização precisa economizar energia, dinheiro ou trabalho sem sair dos requisitos de segurança, e as ideias rejeitadas também merecem registro.

<a id="ch-42"></a>

## Capítulo 42 — Criptografia e serviços de confiança: pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma questão de pesquisa aplicada a partir de dados operacionais; (2) desenhar um estudo pequeno com dados sintéticos ou autorizados; (3) relatar os achados com seus limites.

### 42.1 Uma questão vinda das operações

Os dados operacionais mostram que as falhas de verificação se concentram em certos concentradores ao amanhecer. Aiyana formula uma questão de pesquisa aplicada: as falhas do amanhecer são causadas pela deriva dos relógios dos medidores além da tolerância de timestamp depois de noites frias, e não por ataques ou ruído de rádio? A questão importa porque ampliar a tolerância enfraquece a proteção contra replay, enquanto apertá-la causa rejeições falsas. A pesquisa aplicada na engenharia responde a questões que melhoram um sistema específico, usando métodos rigorosos numa escala modesta. Respondê-la poderia evitar tanto alertas desnecessários quanto uma proteção mais fraca.

### 42.2 Desenhar o estudo

Aiyana desenha um estudo com dados autorizados do piloto: para cada falha, ela registra o concentrador, o horário, a temperatura de uma fonte meteorológica pública e o desvio de relógio informado pelo medidor. Ela define antecipadamente que a explicação pela deriva é sustentada se as falhas se correlacionarem com temperaturas baixas e desvios grandes, e que a explicação por ataque mostraria tags falhando, e não timestamps. Ela usa apenas identificadores de medidor pseudonimizados. O plano do estudo é curto, mas escrito antes da análise, um hábito dos métodos de pesquisa que evita ajustar histórias aos dados.

### 42.3 Achados e limites

Os dados mostram que a maioria das falhas do amanhecer tem tags válidas, mas timestamps fora da tolerância, e ocorre depois de noites abaixo de zero, com desvios maiores nos medidores mais antigos. A explicação pela deriva é sustentada. Aiyana recomenda uma sincronização periódica de horário a partir dos concentradores, autenticada com a chave do medidor, em vez de ampliar a tolerância. Ela relata os limites: um distrito, um inverno e correlação, e não um experimento controlado. Ela compartilha o método com outras companhias pelo grupo de trabalho do regulador, sem nenhum identificador de medidor. Ela planeja um acompanhamento controlado com medidores de teste deliberadamente resfriados.

### Exemplo resolvido

O estudo de Aiyana liga as falhas do amanhecer à deriva de relógio provocada pelo frio, com tags válidas, e recomenda uma sincronização de horário autenticada, em vez de uma tolerância maior.

> **Caso sintético.** Os dados e os achados são inventados.

### Erros e limites

Correlação não prova causa; um teste controlado a fortaleceria. Compartilhar métodos não pode revelar detalhes da infraestrutura.

### Exercícios

- **EX124 — Questão de pesquisa.** Enuncie a questão de pesquisa aplicada de Aiyana. *Rubrica:* 3 = se as falhas do amanhecer vêm da deriva de relógio provocada pelo frio além da tolerância, e não de ataques ou ruído;; 2 = parcial;; 1 = vaga;; 0 = nenhuma.

- **EX125 — Distinguir um ataque.** Que evidência indicaria ataque, e não deriva? *Rubrica:* 3 = tags falhando, e não timestamps;; 2 = falhas de tag;; 1 = temperatura;; 0 = nenhuma.

- **EX126 — Recomendação.** O que ela recomendou em vez de ampliar a tolerância? *Rubrica:* 3 = sincronização periódica e autenticada do horário a partir dos concentradores;; 2 = sincronização;; 1 = ampliar;; 0 = nenhuma.

### Síntese

A pesquisa aplicada transforma enigmas operacionais em estudos pequenos e planejados de antemão, cujos achados melhoram o sistema sem enfraquecer os controles.

<a id="ch-43"></a>

## Capítulo 43 — Prática na indústria ou no serviço público

### Objetivos de aprendizagem

Você vai (1) aplicar os conhecimentos do curso durante um estágio numa companhia; (2) trabalhar dentro da governança e do controle de mudanças; (3) refletir sobre a prática profissional.

### 43.1 O estágio

Aiyana passa um período de estágio na equipe de operações de segurança da Ridgeway, agora como engenheira júnior supervisionada. Suas tarefas incluem fazer a triagem dos alertas de verificação, ajudar numa rotação trimestral de chaves e atualizar runbooks. Marcus Webb supervisiona e aprova seu trabalho. Ela aprende que a maioria dos dias é rotineira e que o valor de um bom projeto aparece em operações sem incidentes. Ela também aprende quanto contexto os engenheiros precisam antes de agir diante de um alerta, como as mudanças recentes e os medidores sabidamente defeituosos. Ela mantém um registro de cada tarefa e do que aprendeu com ela.

### 43.2 Controle de mudanças

Toda mudança em produção na Ridgeway passa pelo controle de mudanças: um pedido escrito, avaliação de risco, aprovação e um plano de rollback. Aiyana envia sua primeira mudança, o ajuste de um limiar de alerta, e é solicitada a mostrar evidências a partir dos dados de linha de base. De início, ela vê o processo como lento; depois, vê seu valor quando uma mudança não revisada de outra equipe na configuração do gateway desativa brevemente as verificações de certificados de cliente em homologação, o que é pego antes de chegar à produção. As configurações criptográficas são especialmente sensíveis a pequenas mudanças, então um controle de mudanças disciplinado as protege.

### 43.3 Reflexão profissional

No fim do estágio, Aiyana escreve uma reflexão. Ela anota que seus projetos acadêmicos subestimaram o tempo necessário para a coordenação com fornecedores e equipes de campo, que runbooks claros reduziram o estresse durante um incidente menor e que uma vez se sentiu tentada a contornar uma aprovação lenta para corrigir um alerta, mas não o fez. Ela identifica competências a desenvolver: negociar requisitos de segurança com fornecedores e explicar riscos a gestores. A reflexão transforma a experiência em aprendizagem deliberada. Ela compartilha a reflexão com Marcus e combina duas metas para o seu primeiro ano.

### Exemplo resolvido

Aiyana faz a triagem de alertas, ajuda numa rotação e atualiza runbooks sob supervisão, segue o controle de mudanças e escreve uma reflexão que identifica a negociação com fornecedores como lacuna de competência.

> **Caso sintético.** O estágio e os eventos são inventados.

### Erros e limites

Estágios podem virar observação passiva; defina tarefas e revisões concretas. O controle de mudanças pode virar burocracia se ignorar os níveis de risco.

### Exercícios

- **EX127 — Tarefas do estágio.** Cite duas tarefas que Aiyana realizou no estágio. *Rubrica:* 3 = duas entre triagem de alertas, ajuda na rotação, atualização de runbooks;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

- **EX128 — Lição do controle de mudanças.** Que evento mostrou o valor do controle de mudanças? *Rubrica:* 3 = uma mudança não revisada no gateway desativou as verificações de certificados de cliente em homologação, pega antes da produção;; 2 = evento;; 1 = nenhum;; 0 = nenhuma.

- **EX129 — Lacuna de competência.** Que competências ela identificou para desenvolver? *Rubrica:* 3 = negociar requisitos de segurança com fornecedores e explicar riscos a gestores;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

A prática mostra que o controle disciplinado de mudanças, runbooks claros e a reflexão importam tanto quanto o conhecimento de projeto.

<a id="ch-44"></a>

## Capítulo 44 — Projeto final de engenharia I

### Objetivos de aprendizagem

Você vai (1) definir o escopo de um projeto final sobre o serviço de confiança; (2) planejar marcos e evidências; (3) identificar os riscos ao próprio projeto.

### 44.1 Escolher o projeto final

Para o seu projeto final, Aiyana escolhe projetar e prototipar o pipeline automatizado de revogação: quando um medidor é dado como roubado ou há suspeita de que uma chave foi exposta, a revogação precisa chegar a todos os verificadores em até um minuto e ser auditável. O projeto combina temas anteriores: estados das chaves, filas de mensagens, monitoramento e runbooks. Ela escreve uma declaração de escopo que inclui o projeto, um protótipo em homologação, testes e a passagem para as operações, e exclui mudanças no firmware dos medidores, que exigiriam um envolvimento do fornecedor além do tempo do projeto final.

### 44.2 Marcos e evidências

Aiyana planeja os marcos: requisitos e modelo de ameaça até a terceira semana, revisão de projeto até a sexta, protótipo até a décima, testes de verificação até a décima segunda e passagem até a décima quinta. Para cada marco, ela define as evidências: documentos, atas de revisão, resultados de testes e uma gravação da demonstração. Seu orientador e Marcus concordam que as evidências serão avaliadas segundo os critérios do programa de engenharia. Definir as evidências cedo evita a falha comum dos projetos finais: um protótipo que funciona sem raciocínio documentado. A falta de evidências num marco conta como marco não cumprido.

### 44.3 Riscos do projeto

Aiyana lista os riscos ao projeto: a disponibilidade do ambiente de homologação, a dependência do tempo da equipe de operações e a possibilidade de seu projeto conflitar com uma atualização planejada do serviço de chaves. As mitigações incluem reservar horários de homologação cedo, combinar uma hora semanal com as operações e se reunir com a equipe do serviço de chaves na segunda semana. Ela mantém um registro de riscos atualizado semanalmente. Tratar o projeto final como um projeto de engenharia, com seus próprios riscos e controles, pratica os hábitos de que ela vai precisar na vida profissional. Os riscos que crescem são escalados ao orientador na mesma semana.

### Exemplo resolvido

Aiyana define o escopo de um projeto final com um pipeline de revogação auditável em um minuto, estabelece cinco marcos sustentados por evidências e registra três riscos do projeto com mitigações.

> **Caso sintético.** O plano do projeto final é inventado.

### Erros e limites

Projetos finais costumam ter escopo grande demais; exclusões firmes protegem a entrega. Evidências planejadas tarde costumam ficar incompletas.

### Exercícios

- **EX130 — Meta do projeto final.** O que o pipeline de revogação precisa alcançar? *Rubrica:* 3 = a revogação chega a todos os verificadores em até um minuto e é auditável;; 2 = um minuto;; 1 = vago;; 0 = nenhuma.

- **EX131 — Exclusão.** O que Aiyana excluiu do escopo, e por quê? *Rubrica:* 3 = mudanças no firmware dos medidores, que exigiriam envolvimento do fornecedor além do tempo disponível;; 2 = firmware;; 1 = nada;; 0 = nenhuma.

- **EX132 — Risco do projeto.** Cite um risco do projeto e sua mitigação. *Rubrica:* 3 = por exemplo, conflito com a atualização do serviço de chaves, mitigado por uma reunião cedo;; 2 = só o risco;; 1 = nenhum;; 0 = nenhuma.

### Síntese

Um trabalho de conclusão bem delimitado, com marcos sustentados por evidências e seu próprio registro de riscos, pratica a engenharia profissional sobre uma necessidade real de segurança.

<a id="ch-45"></a>

## Capítulo 45 — Revisão independente de projeto

### Objetivos de aprendizagem

Você vai (1) preparar um projeto para revisão independente; (2) responder aos achados da revisão; (3) distinguir achados bloqueantes de achados consultivos.

### 45.1 Preparar a revisão

O projeto de revogação de Aiyana vai para uma banca de revisão independente: um criptógrafo de outra companhia, uma engenheira de confiabilidade e um auditor. Ela envia um pacote com uma semana de antecedência, com os requisitos, o modelo de ameaça, a arquitetura, os contratos de interface, o plano de testes e as questões em aberto. Ela lista as premissas explicitamente, como a de que a fila de mensagens preserva a ordem por medidor. Um bom pacote permite que os revisores gastem seu tempo com julgamento, e não reconstruindo o projeto a partir de anotações dispersas. Ela também inclui uma lista das fraquezas conhecidas, para que os revisores partam de uma base honesta.

### 45.2 Achados da revisão

A banca levanta cinco achados. Dois são bloqueantes: as mensagens de revogação não são autenticadas, de modo que um atacante na rede interna poderia forjar revogações e causar negação de serviço, e não há comportamento definido se um verificador perder mensagens enquanto estiver offline. Três são consultivos: nomenclatura, disposição do painel e uma sugestão de reutilizar um repositório de auditoria existente. Aiyana valoriza especialmente o primeiro achado: ela tinha protegido as leituras com cuidado, mas tratado as mensagens internas de controle como confiáveis. Cada achado é registrado com sua severidade e o revisor que o levantou.

### 45.3 Responder

Para os achados bloqueantes, Aiyana assina as mensagens de revogação com uma chave dedicada guardada no serviço de chaves e verificada por todos os assinantes da fila, e acrescenta uma etapa de reconciliação em que os verificadores, ao se reconectar, baixam a lista completa de revogação e comparam um hash dela com o valor publicado. Dos achados consultivos, ela aceita dois e recusa um, com uma justificativa. Ela reapresenta à banca o projeto alterado, e a banca encerra os achados bloqueantes. A revisão independente pegou uma falha que teria custado caro em produção.

### Exemplo resolvido

A banca encontra mensagens de revogação não autenticadas e falta de comportamento offline; Aiyana acrescenta revogações assinadas e a reconciliação na reconexão e encerra os dois achados bloqueantes.

> **Caso sintético.** A banca e os achados são inventados.

### Erros e limites

Pacotes de revisão que escondem premissas recebem revisões superficiais. Tratar as mensagens internas como confiáveis é uma falha de projeto comum.

### Exercícios

- **EX133 — Pacote de revisão.** Liste quatro itens do pacote de revisão de Aiyana. *Rubrica:* 3 = quatro entre requisitos, modelo de ameaça, arquitetura, contratos, plano de testes, questões em aberto, premissas;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX134 — Revogação forjada.** Por que as mensagens de revogação não autenticadas foram um achado bloqueante? *Rubrica:* 3 = atacantes na rede interna poderiam forjar revogações, causando negação de serviço;; 2 = falsificação;; 1 = menor;; 0 = nenhuma.

- **EX135 — Correção offline.** Como o projeto revisado trata os verificadores que estiveram offline? *Rubrica:* 3 = baixam a lista completa de revogação na reconexão e comparam seu hash com o valor publicado;; 2 = baixar;; 1 = ignorar;; 0 = nenhuma.

### Síntese

Uma revisão independente com um pacote completo encontra falhas que os projetistas deixam passar, especialmente a confiança depositada em mensagens internas.

<a id="ch-46"></a>

## Capítulo 46 — Projeto final de engenharia II

### Objetivos de aprendizagem

Você vai (1) construir e testar o protótipo do projeto final; (2) medi-lo em relação aos requisitos; (3) entregá-lo às operações.

### 46.1 Construir o protótipo

Aiyana constrói o pipeline de revogação em homologação. Um pedido de revogação feito por um operador autorizado cria uma mensagem assinada com o identificador da chave, o motivo, o horário e um número de sequência. A fila de mensagens a entrega ao faturamento, ao serviço de configuração dos concentradores e ao monitoramento. Cada assinante verifica a assinatura com a biblioteca avaliada, confere o número de sequência, atualiza seu cache de estados das chaves e confirma o recebimento. Entregas não confirmadas disparam alertas. O protótipo usa apenas componentes existentes e aprovados, para que possa ir à produção sem novas aprovações de segurança para tecnologias desconhecidas.

### 46.2 Medir os resultados

Aiyana executa 1.000 revogações de teste. O tempo mediano para alcançar todos os verificadores é de quatro segundos, e o mais lento é de trinta e oito segundos, dentro do requisito de um minuto. Revogações forjadas, assinadas com uma chave errada, são rejeitadas por todos os assinantes. Um verificador deixado offline por uma hora se reconcilia corretamente na reconexão. Ela também mede o esforço do operador: emitir uma revogação leva menos de um minuto pela interface aprovada. Ela relata uma lacuna: os painéis de monitoramento mostram as revogações, mas não as confirmações por assinante, o que ela acrescenta. Todas as execuções são roteirizadas, para que outras pessoas possam repeti-las.

### 46.3 Passagem

A passagem inclui o projeto, os registros de decisão, os runbooks para emitir e auditar revogações, os resultados dos testes e uma sessão de treinamento para os operadores. As operações executam elas mesmas um exercício de revogação antes de aceitar o sistema. Aiyana fica disponível por duas semanas de suporte. Ela registra as limitações conhecidas, como a dependência da disponibilidade da fila de mensagens, com um runbook alternativo para a distribuição manual das revogações. Um projeto final que termina com uma passagem que funciona, e não apenas com uma demonstração, mostra completude profissional. As operações assinam uma nota de aceitação que lista as pendências e seus donos.

### Exemplo resolvido

O protótipo atinge a meta de um minuto, com mediana de quatro segundos e máximo de trinta e oito, rejeita falsificações, reconcilia verificadores offline e é entregue depois de um exercício conduzido pelas operações.

> **Caso sintético.** As medições são inventadas.

### Erros e limites

O desempenho em homologação pode diferir do de produção. Uma passagem sem prática dos operadores deixa o conhecimento com quem construiu.

### Exercícios

- **EX136 — Mensagem de revogação.** Que campos uma mensagem de revogação contém? *Rubrica:* 3 = identificador da chave, motivo, horário, número de sequência, assinada;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX137 — Resultados de tempo.** Informe os tempos mediano e máximo de revogação. *Rubrica:* 3 = mediana de quatro segundos, máximo de trinta e oito segundos;; 2 = um;; 1 = errado;; 0 = nenhuma.

- **EX138 — Condição da passagem.** O que as operações fizeram antes de aceitar o sistema? *Rubrica:* 3 = executaram elas mesmas um exercício de revogação;; 2 = exercício;; 1 = nada;; 0 = nenhuma.

### Síntese

Um trabalho de conclusão se comprova pelo desempenho medido em relação aos requisitos e por uma passagem que deixa as operações capazes de executá-lo.

<a id="ch-47"></a>

## Capítulo 47 — Ensaio de falha e recuperação

### Objetivos de aprendizagem

Você vai (1) planejar um exercício de recuperação em grande escala; (2) recuperar a raiz do firmware a partir das partes dos custodiantes; (3) aprender com os achados do exercício.

### 47.1 Planejar o ensaio

A Ridgeway faz um ensaio anual de falha e recuperação, e Aiyana ajuda a planejar o cenário deste ano: o HSM primário de assinatura é destruído num incêndio simulado, e uma correção de segurança precisa ser assinada e publicada em até quarenta e oito horas. O ensaio usa os procedimentos reais de backup, mas uma raiz de teste e medidores de teste, de modo que nenhuma chave de produção é exposta. Os objetivos, os critérios de sucesso, os observadores e uma regra de interrupção são combinados antecipadamente. O planejamento garante que o exercício teste os procedimentos, e não a improvisação. Um responsável pela segurança pode interromper o ensaio a qualquer momento se um passo puser em risco sistemas reais.

### 47.2 Executar a recuperação

Três dos cinco custodiantes são chamados; um está no exterior e outro está inalcançável, mas o quórum de três de cinco do Capítulo 32 permite a recuperação. Eles se reúnem no site de backup, restauram a raiz de teste num HSM sobressalente a partir das partes cifradas, emitem uma nova intermediária numa cerimônia e assinam a correção. Os medidores de teste a aceitam. O tempo total é de trinta e uma horas. Os observadores registram cada passo. Um atraso surge porque o firmware do HSM sobressalente era mais antigo do que o exigido e precisou de uma atualização durante o ensaio.

### 47.3 Aprender com o ensaio

A revisão posterior ao ensaio lista os achados sem buscar culpados: o HSM sobressalente não era mantido com o mesmo firmware da produção; a lista de contatos dos custodiantes tinha um número de telefone desatualizado; e o roteiro da cerimônia não tinha um passo para registrar a nova intermediária no inventário. Cada achado recebe um dono e um prazo. Aiyana atualiza o roteiro da cerimônia e acrescenta verificações do firmware do HSM sobressalente ao checklist mensal das operações. O valor do ensaio está nesses achados, descobertos na prática, e não durante uma emergência real.

### Exemplo resolvido

O ensaio recupera uma raiz de teste a partir das partes de três custodiantes, assina uma correção em trinta e uma horas e produz três achados sem culpados, com donos.

> **Caso sintético.** O cenário e os tempos são inventados.

### Erros e limites

Exercícios com condições irreais dão uma falsa confiança. Usar chaves de produção em ensaios arrisca uma exposição real.

### Exercícios

- **EX139 — Raiz de teste.** Por que o ensaio usa uma raiz de teste e medidores de teste? *Rubrica:* 3 = para exercitar os procedimentos reais sem expor chaves de produção;; 2 = segurança;; 1 = realismo;; 0 = nenhuma.

- **EX140 — Quórum na prática.** Como o projeto de quórum ajudou durante o ensaio? *Rubrica:* 3 = só três de cinco custodiantes estavam disponíveis, o suficiente para a recuperação;; 2 = quórum;; 1 = não ajudou;; 0 = nenhuma.

- **EX141 — Achados do ensaio.** Cite dois achados da revisão posterior ao ensaio. *Rubrica:* 3 = dois entre firmware desatualizado do HSM sobressalente, telefone errado, passo de inventário ausente;; 2 = um;; 1 = nenhum;; 0 = nenhuma.

### Síntese

Testes de recuperação realistas, com revisão sem culpa, revelam as pequenas lacunas operacionais que paralisariam uma emergência real.

<a id="ch-48"></a>

## Capítulo 48 — Dossiê de evidências

### Objetivos de aprendizagem

Você vai (1) montar um dossiê de evidências para reguladores e avaliadores; (2) ligar as evidências aos requisitos e aos riscos; (3) proteger as evidências sensíveis.

### 48.1 Propósito do dossiê

O regulador exige que a Ridgeway demonstre que seu serviço de confiança da medição está adequadamente protegido. Aiyana monta um dossiê de evidências: requisitos, arquitetura, registro de riscos, mapa de controles, relatórios de testes, resumo dos testes independentes, atas das cerimônias, achados do ensaio e declarações de risco residual. O dossiê é organizado por requisito, para que um avaliador possa seguir qualquer requisito até seu projeto, seus testes e suas evidências operacionais. Um dossiê transforma anos de trabalho num argumento auditável, e não numa pilha de documentos. Ele também dá aos futuros engenheiros um mapa único de por que o sistema é como é.

### 48.2 Ligar as evidências

Para cada requisito, o dossiê inclui uma afirmação curta, as evidências que a sustentam e quaisquer limitações. Por exemplo, a afirmação de que as leituras não podem ser forjadas sem uma chave de medidor se liga ao projeto do HMAC, aos testes negativos do laboratório, ao teste independente que não encontrou falsificação e aos dados de monitoramento que mostram as falhas de verificação investigadas. Onde as evidências são mais fracas, como a resistência a canais laterais testada numa única revisão de hardware, o dossiê diz isso. Aiyana usa digests SHA-256 para identificar cada arquivo de evidência, para que os avaliadores possam confirmar que examinaram exatamente as versões referenciadas.

### 48.3 Proteger as evidências sensíveis

Algumas evidências ajudariam os atacantes, como relatórios detalhados de testes de intrusão ou a configuração dos HSMs. Aiyana classifica cada item: resumos públicos, material exclusivo do regulador e material apenas interno, disponível para inspeção no local. Material de chave nunca aparece em nenhum dossiê. As atas das cerimônias incluem identificadores de chave e impressões digitais, mas não as chaves. Ela combina com o regulador as regras de manuseio. As evidências que protegem o público não podem se tornar, elas próprias, um risco para o público. O acesso ao material exclusivo do regulador e ao material interno é registrado, e as cópias são numeradas, para que qualquer vazamento possa ser rastreado até um destinatário específico.

### Exemplo resolvido

O dossiê de Aiyana organiza as evidências por requisito, liga as afirmações aos testes e às operações com digests e classifica os itens sensíveis com regras de manuseio combinadas.

> **Caso sintético.** O dossiê é inventado.

### Erros e limites

Dossiês que escondem evidências fracas perdem credibilidade quando os avaliadores encontram as lacunas. Compartilhar demais relatórios de testes detalhados aumenta o risco.

### Exercícios

- **EX142 — Organização do dossiê.** Como o dossiê é organizado, e por quê? *Rubrica:* 3 = por requisito, para que os avaliadores rastreiem cada um até o projeto, os testes e as operações;; 2 = requisito;; 1 = data;; 0 = nenhuma.

- **EX143 — Evidências fracas.** Como o dossiê trata as evidências mais fracas? *Rubrica:* 3 = declara abertamente seus limites, por exemplo testes de canal lateral numa só revisão;; 2 = honesto;; 1 = esconde;; 0 = nenhuma.

- **EX144 — Atas das cerimônias.** O que as atas das cerimônias incluem e excluem? *Rubrica:* 3 = identificadores de chave e impressões digitais, nunca material de chave;; 2 = impressões digitais;; 1 = chaves;; 0 = nenhuma.

### Síntese

Um dossiê de evidências organizado por requisito, honesto quanto aos limites e cuidadoso com o material sensível torna as afirmações de segurança auditáveis.

<a id="ch-49"></a>

## Capítulo 49 — Tese de engenharia

### Objetivos de aprendizagem

Você vai (1) escrever uma tese de engenharia sobre o serviço de confiança; (2) apresentar o raciocínio de projeto e as evidências; (3) declarar as contribuições e as limitações.

### 49.1 Estrutura da tese

A tese de Aiyana apresenta o projeto e a avaliação do serviço de confiança da medição da Ridgeway, com foco no seu pipeline de revogação e no plano de migração pós-quântica. Os capítulos cobrem o problema e os requisitos, as normas relacionadas, a arquitetura e as alternativas, a implementação, a verificação e a validação, as operações e as conclusões. Cada decisão de projeto cita seu requisito e suas evidências. A tese não é um diário do projeto; é um argumento de que o projeto atende aos seus requisitos sob premissas declaradas. Ela usa o dossiê de evidências como espinha dorsal, para que cada afirmação da tese aponte para um artefato existente.

### 49.2 Evidências e raciocínio

A tese relata os resultados medidos: revogação chegando a todos os verificadores numa mediana de quatro segundos; testes independentes sem leituras forjadas; alcance do firmware de 97 por cento no piloto; e recuperação em trinta e uma horas no ensaio. Ela explica por que as alternativas foram rejeitadas, como as leituras com chave pública que excediam o orçamento das mensagens. Aiyana inclui os programas dos laboratórios como apêndices, todos usando apenas a biblioteca padrão sobre dados sintéticos, e declara claramente que os sistemas de produção usam bibliotecas criptográficas avaliadas e HSMs. Cada número cita o teste ou o log que o produziu.

### 49.3 Contribuições e limites

Ela declara as contribuições: um projeto de pipeline de revogação com mensagens autenticadas e reconciliação, uma abordagem medida da migração pós-quântica para medidores de vida longa e um conjunto de métricas operacionais ligado às etapas do ciclo de vida do SP 800-57. Os limites incluem uma única companhia, um piloto em vez de uma implantação completa e a dependência de implementações de fornecedores que ela não pôde inspecionar. Ela sugere trabalhos futuros sobre o desempenho das assinaturas híbridas nas diferentes gerações de medidores. Limites claros tornam as contribuições mais críveis. Seu orientador lê primeiro a seção de limites, como os examinadores costumam fazer, e pede que ela torne cada limite específico sobre quem poderia ver resultados diferentes.

### Exemplo resolvido

A tese de Aiyana argumenta que o serviço de confiança atende aos seus requisitos, relata os resultados medidos, explica as alternativas rejeitadas e declara três contribuições com seus limites.

> **Caso sintético.** Os resultados são inventados; o SP 800-57 é real.

### Erros e limites

Teses que listam atividades em vez de argumentar afirmações são fracas. Afirmar mais do que as evidências sustentam convida à reprovação.

### Exercícios

- **EX145 — Natureza da tese.** O que é a tese, segundo o capítulo? *Rubrica:* 3 = um argumento de que o projeto atende aos requisitos sob premissas declaradas, não um diário;; 2 = argumento;; 1 = diário;; 0 = nenhuma.

- **EX146 — Declaração sobre os apêndices de laboratório.** O que a tese diz sobre os programas dos laboratórios? *Rubrica:* 3 = só biblioteca padrão sobre dados sintéticos; a produção usa bibliotecas avaliadas e HSMs;; 2 = biblioteca padrão;; 1 = código de produção;; 0 = nenhuma.

- **EX147 — Limites da tese.** Cite dois limites que Aiyana declara. *Rubrica:* 3 = dois entre uma única companhia, piloto e não implantação completa, implementações de fornecedores não inspecionadas;; 2 = um;; 1 = nenhum;; 0 = nenhuma.

### Síntese

Uma tese de engenharia é um argumento fundamentado e sustentado por evidências, com contribuições claras e limites honestos.

<a id="ch-50"></a>

## Capítulo 50 — Defesa final

### Objetivos de aprendizagem

Você vai (1) defender as decisões de projeto diante de uma banca examinadora; (2) responder a perguntas sobre trade-offs de segurança; (3) refletir sobre a responsabilidade contínua da engenheira.

### 50.1 Preparar a defesa

Aiyana prepara uma apresentação de vinte minutos: o problema, as principais escolhas de projeto, as evidências e os limites. Ela antecipa as perguntas: por que chaves simétricas para as leituras, por que três de cinco custodiantes, por que assinaturas pós-quânticas híbridas e o que acontece se o serviço de chaves for comprometido. Para cada uma, prepara uma resposta concisa que aponta para as evidências na tese ou no dossiê. Marcus e seu orientador fazem uma defesa simulada, pressionando-a sobre premissas de custo que ela não tinha justificado plenamente, e ela as reforça. Ela ensaia as respostas em voz alta até que cada uma caiba em menos de dois minutos.

### 50.2 Responder a perguntas sobre trade-offs

Durante a defesa, um examinador pergunta por que a Ridgeway não usou assinaturas de chave pública nas leituras para eliminar o risco central das chaves. Aiyana explica o orçamento de 32 bytes por mensagem e as restrições de energia, as mitigações do risco central (HSMs, derivação por medidor, monitoramento e controle duplo) e a condição sob a qual ela reverteria a decisão. Outro examinador pergunta se o código dos laboratórios poderia ser usado em produção; ela responde com firmeza que não, porque ele existe para verificar a compreensão contra vetores de teste, enquanto a produção depende de bibliotecas avaliadas.

### 50.3 Responsabilidade contínua

Ao concluir, Aiyana reflete que o serviço de confiança vai durar mais do que o envolvimento dela. Algoritmos ficarão obsoletos, a computação quântica pode amadurecer, a equipe vai mudar e as ameaças vão evoluir. Sua responsabilidade como engenheira é deixar um sistema que outras pessoas consigam entender, operar, testar e mudar com segurança, com documentação, runbooks, métricas e uma trilha de evidências. A banca aprova sua tese, destacando a clareza dos seus limites. Ela começa a trabalhar na Ridgeway como engenheira de segurança no mês seguinte. Ela agenda sua própria primeira revisão do sistema para dali a um ano.

### Exemplo resolvido

Aiyana defende o projeto simétrico das leituras, o quórum de custodiantes e a migração híbrida, recusa-se a chamar o código dos laboratórios de pronto para produção e enquadra sua responsabilidade como deixar um sistema manutenível.

> **Caso sintético.** A defesa e o resultado são inventados.

### Erros e limites

Defender todas as decisões como perfeitas mina a credibilidade; reconheça os trade-offs. A responsabilidade da engenharia continua depois da passagem.

### Exercícios

- **EX148 — Lição da defesa simulada.** Que fraqueza a defesa simulada expôs? *Rubrica:* 3 = premissas de custo não totalmente justificadas;; 2 = custos;; 1 = nenhuma;; 0 = nenhuma.

- **EX149 — Mitigações do risco central.** Que mitigações ela citou para o risco central das chaves? *Rubrica:* 3 = HSMs, derivação por medidor, monitoramento, controle duplo;; 2 = três;; 1 = uma;; 0 = nenhuma.

- **EX150 — Responsabilidade da engenheira.** Como Aiyana descreve sua responsabilidade contínua? *Rubrica:* 3 = deixar um sistema que outros consigam entender, operar, testar e mudar com segurança, com documentação e evidências;; 2 = parcial;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Uma defesa demonstra domínio ao explicar os compromissos com honestidade, e a responsabilidade de engenharia continua por toda a vida do sistema.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX150. Aiyana Torres, Marcus Webb, o Halden Institute of Engineering, a Ridgeway Water Utility e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** A operadora celular, ou qualquer pessoa com acesso a essa rede.

**EX032.** A troca de chaves efêmera faz com que chaves de longo prazo roubadas não consigam decifrar sessões passadas que foram gravadas.

**EX033.** O TLS termina no gateway, então o HMAC fim a fim permite ao banco de dados detectar alterações feitas por qualquer sistema intermediário.

**EX034.** Os crash dumps poderiam gravar no disco chaves que estavam na memória, onde outras pessoas poderiam lê-las.

**EX035.** O random é um gerador previsível para simulações, cujo estado pode ser recuperado; o secrets obtém valores do gerador criptográfico do sistema operacional.

**EX036.** Não consegue ler as chaves brutas, porque somente a conta isolada do serviço de chaves tem acesso a elas.

**EX037.** Um hash de mão única e memory-hard, porque as senhas só precisam ser verificadas, nunca decifradas.

**EX038.** Argon2id com um salt aleatório único por usuário, como definido na RFC 9106.

**EX039.** Rotacionar a chave mestra exige apenas reembrulhar as pequenas chaves de dados, em vez de recifrar o banco de dados.

**EX040.** "Toda leitura é autenticada com uma chave por medidor", com um teste de aceitação que rejeita leituras alteradas.

**EX041.** Nunca colar código criptográfico de fóruns; usar uma biblioteca mantida ou levar a lacuna à revisão de projeto.

**EX042.** Um auxiliar de testes que desativava a verificação de certificados TLS e estava prestes a ser reutilizado em produção.

**EX043.** Os padrões de uso mostram quando os moradores estão fora, o que poderia ajudar ladrões.

**EX044.** Ataques de hardware de Estados-nação ao piloto; declarar isso explicitamente mantém as afirmações honestas.

**EX045.** Cada chave é vinculada a um único identificador de medidor, então um medidor autenticado só pode enviar as próprias leituras.

**EX046.** Por exemplo, geração, distribuição, rotação e destruição.

**EX047.** Elas são enviadas cifradas sob uma chave de transporte, nunca em forma clara.

**EX048.** A revogação não pertencia a ninguém, então chaves comprometidas continuaram ativas por meses.

**EX049.** Taxa de falhas de verificação de tags, dias até a expiração dos certificados e idade das chaves.

**EX050.** Porque as ferramentas de renovação podem falhar silenciosamente, e perceber que não houve tentativa evita uma expiração mais tarde.

**EX051.** Alertas que oscilam rapidamente e revogações automáticas repetidas de medidores com falhas intermitentes.

**EX052.** Uma chave em que se confia por pressuposição, e não por prova, como um certificado raiz ou uma chave pública de firmware embutida.

**EX053.** Os medidores só aceitam firmware com uma cadeia válida e um número de versão maior que o instalado.

**EX054.** Apenas as chaves derivadas de vida curta guardadas em cache para aquela região.

**EX055.** As leituras são numerosas e combinam com tags simétricas baratas, enquanto os concentradores se autenticam por TLS, em que os certificados permitem aos verificadores usar chaves públicas.

**EX056.** False, porque mudar a leitura muda a tag exigida, que não pode ser produzida sem a chave.

**EX057.** Tanto o medidor quanto o serviço de chaves têm a chave, então uma tag não pode provar qual dos dois a criou.

**EX058.** Vida da bateria dos medidores, largura de banda de rádio limitada e um orçamento fixo.

**EX059.** Os medidores são movidos entre endereços durante consertos, então os vínculos das chaves com as identidades precisam lidar com as trocas.

**EX060.** As atualizações de firmware devem chegar a 99 por cento dos medidores em até trinta dias após o lançamento.

**EX061.** Toda leitura carrega uma tag HMAC-SHA256 com uma chave por medidor de 256 bits, e o faturamento rejeita as leituras cuja tag falhe.

**EX062.** ECDSA P-256 segundo o FIPS 186-5, ou Ed25519 segundo a RFC 8032.

**EX063.** Testes independentes de falsificação antes da entrada em produção e cerimônias de chaves com testemunhas e ata.

**EX064.** Os bytes reais da chave; apenas metadados sobre a chave.

**EX065.** Três chaves escondidas em scripts antigos que não constavam de nenhum registro.

**EX066.** Ela ainda pode verificar dados produzidos anteriormente, mas não pode criar novas tags nem assinaturas.

**EX067.** Atacantes poderiam conseguir que um firmware malicioso fosse assinado com a chave genuína, de modo que os medidores o aceitariam.

**EX068.** Um certificado de concentrador expirado e a deriva de relógio dos medidores rejeitando leituras válidas.

**EX069.** Com um backup cifrado da chave de assinatura mantido sob custódia dividida.

**EX070.** A extração condensa o material de chave de entrada numa chave pseudoaleatória usando um salt; a expansão a estende em chaves de saída vinculadas a uma string info.

**EX071.** Imprimiu que a saída coincidia com o caso de teste A.1 da RFC 5869: True.

**EX072.** Finalidade, identificador do medidor e versão da chave; a versão permite derivar novas chaves para a rotação sem uma nova chave mestra.

**EX073.** Forjar uma leitura exigiria adivinhar um valor de 128 bits, e a RFC 2104 permite o truncamento dentro desses limites.

**EX074.** Cada leitura carrega um contador crescente, e o faturamento rejeita contadores que não sejam maiores que o último aceito.

**EX075.** Acrescentaram uma versão da chave às mensagens, para que o contador de um novo medidor comece do zero com sua nova chave.

**EX076.** As assinaturas Ed25519 ocupam 64 bytes, grandes demais para o orçamento de 32 bytes por mensagem.

**EX077.** O regulador exige que as chaves do faturamento fiquem sob o controle da Ridgeway.

**EX078.** Se os quadros de rádio crescessem o suficiente para transportar assinaturas, as leituras com chave pública se tornariam viáveis.

**EX079.** Não exportabilidade pelo HSM (preventivo), alertas de falhas de verificação (detectivo) e revogação (corretivo).

**EX080.** Provar que a chave raiz foi gerada e guardada em backup sem que nenhuma pessoa sozinha a controlasse.

**EX081.** A deriva de relógio dos medidores não tinha detecção, então foi acrescentado um monitor do desvio dos timestamps.

**EX082.** Ele verifica a cadeia de assinatura do manifesto, confirma que a versão é mais nova e confere o digest da imagem contra o manifesto.

**EX083.** A verificação falhou, e a imagem foi rejeitada.

**EX084.** Sem assinatura, um atacante poderia substituir a imagem e o manifesto juntos e passar na verificação do hash.

**EX085.** A chave de assinatura do firmware (880 dias), a chave HMAC dos webhooks (406) e a chave de empacotamento dos backups (968).

**EX086.** Não, mas o uso mais longo aumenta a quantidade de dados protegidos e o dano caso uma exposição tenha passado despercebida.

**EX087.** O número de chaves geradas, que não diz nada sobre a segurança.

**EX088.** Chaves sintéticas numa rede isolada, nunca chaves de produção.

**EX089.** Leituras com uma chave revogada foram aceitas por até uma hora; o cache foi reduzido a um minuto, e as revogações passaram a ser enviadas.

**EX090.** Apenas que os defeitos conhecidos estão ausentes nas condições testadas, e não que o sistema está livre de defeitos.

**EX091.** Cada concentrador prova sua identidade com um certificado de cliente emitido pela autoridade de dispositivos da Ridgeway.

**EX092.** No próprio concentrador, de modo que a chave privada nunca precise ser transmitida.

**EX093.** Qualquer parte com um certificado emitido publicamente poderia então se autenticar, então só se deve confiar na autoridade de dispositivos da Ridgeway.

**EX094.** Cerca de 0,59, menos até do que depender de um só custodiante.

**EX095.** Três de cinco, o que dá cerca de 0,99 de disponibilidade e impede que duas pessoas quaisquer recuperem a chave.

**EX096.** A divisão de chaves embutida do fornecedor do HSM, porque implementar ela mesma o compartilhamento de segredos seria criptografia caseira.

**EX097.** Ela é posta em quarentena e um alerta é emitido, preservando a evidência.

**EX098.** Revogá-la com uma declaração assinada pela raiz, criar uma nova intermediária numa cerimônia, assinar de novo o firmware e distribuir a nova confiança.

**EX099.** Para que perder ou comprometer a raiz primária não deixe a frota sem saída.

**EX100.** A solicitação de uma nova chave de medidor pela ferramenta portátil de campo ao substituir um medidor.

**EX101.** Para que só o elemento seguro do medidor de destino consiga desembrulhá-lo e a ferramenta nunca veja a chave.

**EX102.** O faturamento nunca recebia os eventos de revogação; agora uma fila de mensagens compartilhada os entrega a todos os verificadores.

**EX103.** Os medidores ficam em serviço cerca de quinze anos, então o firmware assinado agora precisa continuar confiável até por volta de 2041.

**EX104.** Somente se tanto a assinatura clássica ECDSA quanto a ML-DSA forem verificadas.

**EX105.** A verificação pós-quântica exige um novo bootloader, que precisa primeiro ser implantado usando assinaturas clássicas.

**EX106.** Cerca de 1,2 milhão de leituras por dia.

**EX107.** Nas gravações no banco de dados e nas consultas de chaves; o HMAC em si é barato.

**EX108.** Para que os concentradores não renovem todos no mesmo instante e sobrecarreguem o serviço emissor.

**EX109.** Um operador que não os conhecia os executou, e os passos confusos foram reescritos.

**EX110.** As chaves da nova versão são implantadas em ondas enquanto o faturamento aceita as duas versões, e a versão antiga é desativada quando todos os medidores tiverem migrado.

**EX111.** Ela só guardava blobs cifrados para os elementos seguros dos medidores, nunca as próprias chaves de medidor.

**EX112.** A verificação confirma que o sistema corresponde à especificação; a validação confirma que ele atende às necessidades reais das partes interessadas.

**EX113.** Uma chave de um protótipo de medidor sem elemento seguro, confirmando o requisito de elementos seguros.

**EX114.** Apenas 97 por cento foram atualizados em trinta dias, abaixo dos 99 por cento, porque alguns medidores em caixas inundadas estavam inalcançáveis.

**EX115.** Identificadores de algoritmo nas mensagens e nos manifestos e uma lista configurada de algoritmos aceitos.

**EX116.** Parar de emitir novas chaves com ele, migrar os usos existentes e depois retirar o suporte à verificação após um período de carência.

**EX117.** Porque muitos incidentes começam quando os engenheiros já não sabem por que um projeto foi escolhido e o mudam de forma insegura.

**EX118.** Valem apenas para a revisão de hardware testada, então novas revisões precisam ser testadas de novo.

**EX119.** O gateway rejeitou corretamente o certificado ainda não válido, mas o alerta do concentrador não era claro e foi reescrito.

**EX120.** A extração da chave de um medidor por um atacante bem financiado, aceita porque as chaves por medidor confinam o dano àquele medidor.

**EX121.** As quatro leituras e seus contadores, para que a remoção ou a reordenação seja detectada.

**EX122.** Suas credenciais ficam no serviço de chaves, e seus logs de emissão vão para o monitoramento.

**EX123.** A resistência à falsificação de sessenta e quatro bits fica abaixo da meta do modelo de ameaça, e de qualquer forma os cabeçalhos de rádio dominam o consumo de energia.

**EX124.** As falhas de verificação do amanhecer são causadas pela deriva dos relógios dos medidores além da tolerância de timestamp depois de noites frias, e não por ataques ou ruído de rádio?

**EX125.** Falhas na própria verificação da tag, e não timestamps fora da tolerância.

**EX126.** Sincronização regular do horário a partir dos concentradores, autenticada com a chave de cada medidor.

**EX127.** A triagem de alertas de verificação e a ajuda numa rotação trimestral de chaves.

**EX128.** Uma mudança não revisada de outra equipe desativou as verificações de certificados de cliente em homologação e foi pega antes da produção.

**EX129.** Negociar requisitos de segurança com fornecedores e comunicar riscos a gestores.

**EX130.** As revogações precisam chegar a todos os verificadores em até um minuto, com uma trilha de auditoria.

**EX131.** Mudanças no firmware dos medidores, que exigiriam trabalho do fornecedor além do cronograma do projeto final.

**EX132.** Um conflito com a atualização planejada do serviço de chaves, mitigado por uma reunião com essa equipe na segunda semana.

**EX133.** Requisitos, modelo de ameaça, arquitetura e plano de testes (além dos contratos e das questões em aberto).

**EX134.** Um atacante interno poderia forjar revogações e derrubar medidores legítimos.

**EX135.** Ao se reconectar, os verificadores baixam a lista completa de revogação e conferem seu hash com o valor publicado.

**EX136.** O identificador da chave, o motivo, o timestamp e o número de sequência, tudo assinado.

**EX137.** Uma mediana de quatro segundos e um máximo de trinta e oito segundos.

**EX138.** Executaram o próprio exercício de revogação.

**EX139.** Para que os procedimentos reais sejam praticados sem arriscar as chaves de produção.

**EX140.** Dois custodiantes estavam indisponíveis, mas três de cinco bastaram para a recuperação.

**EX141.** O firmware do HSM sobressalente estava desatualizado, e o número de telefone de um custodiante estava errado.

**EX142.** Por requisito, permitindo que um avaliador rastreie cada um pelo projeto, pelos testes e pelas operações.

**EX143.** Declara a limitação abertamente, como os testes de canal lateral feitos em apenas uma revisão de hardware.

**EX144.** Incluem identificadores de chave e impressões digitais, mas nunca material de chave.

**EX145.** Um argumento de que o projeto satisfaz seus requisitos sob premissas declaradas, e não um registro do projeto.

**EX146.** Eles usam apenas a biblioteca padrão sobre dados sintéticos, enquanto a produção depende de bibliotecas avaliadas e HSMs.

**EX147.** Uma única companhia e um piloto, em vez de uma implantação completa.

**EX148.** Suas premissas de custo não tinham sido justificadas adequadamente.

**EX149.** Módulos de segurança de hardware, derivação de chaves por medidor, monitoramento e controle duplo.

**EX150.** Deixar um sistema que outras pessoas consigam entender, operar, testar e mudar com segurança, apoiado em documentação, runbooks, métricas e evidências.

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
