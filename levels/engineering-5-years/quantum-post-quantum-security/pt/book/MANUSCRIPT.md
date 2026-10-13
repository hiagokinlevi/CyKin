# Segurança Quântica e Pós-Quântica: Engenharia de Sistemas Resistentes à Computação Quântica

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX020 e suas resoluções; os capítulos 11–50 (EX021–EX100) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: futuros projetistas de sistemas de segurança que vão projetar, construir e validar sistemas que continuem seguros quando existirem grandes computadores quânticos. Conhecimento de entrada: cálculo, computação, redes e engenharia de sistemas no nível de conclusão do ensino médio ou do primeiro ano.
- Relação com os livros vizinhos: os livros de [mestrado](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) e de [doutorado](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) desta área estudam empiricamente a implantação da PQC. **Este livro trata da engenharia da migração**: a matemática por trás dos esquemas de reticulados, de hash e de códigos, o inventário, os requisitos, a arquitetura híbrida PQ/T, a agilidade criptográfica, a implementação, a verificação, as operações e um projeto final.
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é um título credenciado nem uma habilitação profissional. Não concede autorização para testar sistemas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública. A criptografia de brinquedo dos laboratórios é deliberadamente insegura; sistemas de produção devem usar implementações verificadas da [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), da [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), da [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) e da [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208).

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Cinquenta capítulos se distribuem em dez etapas ao longo de cinco anos: fundamentos (1–19), o núcleo de engenharia de PQC (20–42) e prática, projeto final e defesa (43–50). Cada capítulo tem objetivos de aprendizagem, ensino, um exemplo resolvido, uma atividade prática, erros comuns, dois exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com Python 3; a saída impressa é mostrada para que você possa conferir a sua execução.

### O caso contínuo: Brightwater Port Authority

A **Brightwater Port Authority (BPA)** é um porto de contêineres sintético. Ela opera um sistema operacional de terminal, uma troca de dados aduaneiros cujos registros precisam permanecer confidenciais por 25 anos, VPNs site a site com as companhias de navegação, uma PKI interna que assina conhecimentos de embarque eletrônicos (que precisam continuar verificáveis por pelo menos 12 anos), firmware assinado para scanners de portão e guindastes e um portal web público. O conselho da BPA pediu à engenharia que tornasse a criptografia do porto resistente à computação quântica sem interromper as operações. Todos os números sobre a BPA são inventados.

### Política de fontes

As fontes primárias foram verificadas em 12 de outubro de 2026: NIST FIPS 203/204/205 (agosto de 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (rascunho público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd), [NIST IR 8545](https://doi.org/10.6028/NIST.IR.8545), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) e [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). O FN-DSA (FIPS 206) e a norma do HQC ainda estavam em desenvolvimento. Verifique a situação de novo antes de se apoiar nela.

## Sumário

1. [Cálculo I](#ch-01)
2. [Matemática discreta](#ch-02)
3. [Física para computação](#ch-03)
4. [Programação I](#ch-04)
5. [Comunicação em engenharia](#ch-05)
6. [Cálculo II](#ch-06)
7. [Probabilidade e estatística](#ch-07)
8. [Arquitetura de computadores](#ch-08)
9. [Programação II](#ch-09)
10. [Ética e segurança operacional em engenharia](#ch-10)

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) comparar taxas de crescimento — polinomial, subexponencial e exponencial — e explicar por que elas decidem o que um computador quântico ameaça; (2) usar logaritmos para converter fatores de trabalho em "bits de segurança"; e (3) ler criticamente uma afirmação assintótica. Este capítulo abre a etapa de fundamentos e prepara a matemática discreta do Capítulo 2.

### 1.1 Por que um engenheiro precisa de taxas de crescimento

Toda afirmação de segurança deste livro é uma afirmação sobre a velocidade com que algum custo cresce. Encontrar por força bruta uma chave de *k* bits exige cerca de 2^*k* tentativas: o custo dobra a cada bit extra, o que é crescimento **exponencial**. O melhor algoritmo clássico de fatoração, o crivo geral de corpo de números (GNFS), roda em tempo **subexponencial**, aproximadamente exp(c·(ln N)^(1/3)·(ln ln N)^(2/3)) para um módulo *N*. O algoritmo de Shor fatora em tempo **polinomial** no número de bits — da ordem de *n*³ portas quânticas elementares para um módulo de *n* bits, ignorando o custo adicional da correção de erros ([Shor 1997](https://doi.org/10.1137/S0097539795293172)). A busca de Grover encontra uma chave entre 2^*k* candidatas em cerca de 2^(*k*/2) iterações sequenciais ([Grover 1996](https://doi.org/10.1145/237814.237866)). Toda a história da PQC decorre dessas quatro funções: Shor transforma um problema subexponencial num polinomial, o que é catastrófico para o RSA e as curvas elípticas; Grover apenas reduz o expoente pela metade, e é por isso que o AES-256 continua aceitável.

### 1.2 Logaritmos e bits de segurança

Aplicar log₂ a um fator de trabalho dá os "bits de segurança". Um custo de 2^128 operações é "segurança de 128 bits". Os logaritmos transformam produtos em somas, de modo que dobrar o trabalho acrescenta um bit, e multiplicá-lo por um milhão (≈2^20) acrescenta cerca de vinte bits. É por isso que os engenheiros dizem que uma aceleração de 2^20 trazida por hardware melhor "custa" vinte bits. A derivada ajuda a intuição: a curva de custo do GNFS, medida em bits, se achata à medida que as chaves crescem, de modo que cada bit extra de RSA compra menos segurança do que cada bit extra de AES — um dos motivos de as chaves RSA terem milhares de bits.

### 1.3 Limites e notação assintótica

As afirmações "O grande" descrevem o comportamento quando o tamanho da entrada tende ao infinito e escondem constantes. O *n*³ de Shor esconde uma constante grande e, mais importante, o custo adicional da correção quântica de erros, que pode multiplicar por mil ou mais o número de qubits físicos. Estimativas de recursos como a de [Gidney (2025)](https://arxiv.org/abs/2505.15917) — menos de um milhão de qubits ruidosos para o RSA-2048, sob pressupostos de hardware declarados — preenchem essas constantes. Um engenheiro nunca deve ler um limite assintótico como um tempo.

Dois algoritmos com o mesmo O grande podem diferir por fatores que decidem se um ataque leva uma hora ou uma década. A queda de vinte milhões de qubits ruidosos para menos de um milhão veio de constantes e códigos melhores, não de uma mudança no n³ de Shor. Quando um fornecedor cita um limite assintótico, o engenheiro pede os pressupostos de hardware por trás da constante.

### 1.4 Atividade prática — Laboratório G

```python
# Lab G (ch 1): growth rates that decide what quantum computers threaten.
import math
print("Symmetric key search: classical 2^k trials vs Grover ~2^(k/2) sequential iterations")
for k in (128, 192, 256):
    print(f"  k={k}: classical 2^{k}, Grover ~2^{k//2}")
def gnfs_bits(n_bits):            # heuristic L_N[1/3, (64/9)^(1/3)] work, expressed in bits
    ln_n = n_bits * math.log(2)
    work = (64/9) ** (1/3) * ln_n ** (1/3) * math.log(ln_n) ** (2/3)
    return work / math.log(2)
print("Factoring an n-bit RSA modulus: classical GNFS (heuristic) vs Shor gate count ~n^3")
for n in (1024, 2048, 3072):
    print(f"  n={n}: GNFS ~2^{gnfs_bits(n):.0f} operations; Shor ~n^3 = 2^{math.log2(n**3):.0f} logical gates")
```

Saída esperada:

```text
Symmetric key search: classical 2^k trials vs Grover ~2^(k/2) sequential iterations
  k=128: classical 2^128, Grover ~2^64
  k=192: classical 2^192, Grover ~2^96
  k=256: classical 2^256, Grover ~2^128
Factoring an n-bit RSA modulus: classical GNFS (heuristic) vs Shor gate count ~n^3
  n=1024: GNFS ~2^87 operations; Shor ~n^3 = 2^30 logical gates
  n=2048: GNFS ~2^117 operations; Shor ~n^3 = 2^33 logical gates
  n=3072: GNFS ~2^139 operations; Shor ~n^3 = 2^35 logical gates
```

A fórmula do GNFS é heurística (o seu termo *o*(1) é descartado), então os valores em bits se aproximam da força de 112 bits comumente citada para o RSA-2048, sem coincidir com ela. As "contagens de portas" de Shor são portas lógicas antes da correção de erros.

A comparação do laboratório existe para tornar as formas visíveis lado a lado: a força bruta dobra a cada bit, o GNFS se curva mais devagar e a contagem de portas lógicas de Shor cresce apenas polinomialmente. Executá-lo para módulos de 1024, 2048 e 3072 bits mostra por que chaves RSA mais longas compram pouco contra um adversário quântico. Os estudantes devem anotar na tabela o aviso de que a coluna de Shor omite o custo da correção de erros, de modo que nenhuma linha deve ser lida como tempo para quebrar.

### 1.5 Exemplo resolvido: a primeira pergunta da BPA

O conselho da BPA pergunta se deve dobrar o tamanho das chaves AES "por causa da computação quântica". Usando a seção 1.1: sob Grover, o AES-128 cai para cerca de 2^64 iterações sequenciais no modelo idealizado, mas Grover se paraleliza mal, então muitos documentos de orientação ainda aceitam o AES-128; migrar a cifragem em massa para o AES-256 é barato e encerra o debate. O item urgente não é o AES, e sim toda troca de chaves RSA e de curva elíptica, que Shor quebra por completo.

O memorando ao conselho da BPA separa, portanto, duas decisões. As chaves simétricas passam para o AES-256 durante a renovação normal, quase sem custo. A troca de chaves e as assinaturas precisam de uma migração planejada para o ML-KEM e o ML-DSA, porque nenhum tamanho de chave salva o RSA ou as curvas elípticas de Shor. Misturar as duas perguntas é a forma como conselhos gastam dinheiro na correção barata e adiam a importante.

### 1.6 Erros comuns e limites

- Tratar Grover como fatal para a criptografia simétrica.
- Ler *O*(*n*³) como "rápido" sem o custo da correção de erros.
- Comparar bits entre curvas exponenciais e subexponenciais como se crescessem da mesma forma.

Cada erro leva a uma decisão errada. Tratar Grover como fatal manda orçamento para atualizações simétricas que já eram adequadas. Ler n³ como rápido ignora os qubits físicos necessários para cada qubit lógico. Comparar números de bits entre curvas de crescimento diferentes faz o RSA-3072 parecer mais forte contra ataques quânticos do que é. Os modelos deste capítulo comparam opções; não são cronogramas.

### Exercícios

- **EX001 — Bits a partir do trabalho.** Converta 10^30 e 2^100 × 10^6 operações em bits de segurança. Rubrica: 3 = os dois corretos, com o método.
- **EX002 — Explicar a assimetria.** Em 150 palavras, explique ao conselho da BPA por que o RSA precisa ser substituído, mas o AES-256 não. Rubrica: 3 = argumento de taxa de crescimento correto e não técnico.

### Síntese

As taxas de crescimento decidem tudo: Shor torna polinomiais a fatoração e os logaritmos discretos; Grover apenas tira a raiz quadrada da busca. Bits de segurança são logaritmos do trabalho, e os limites assintóticos precisam de estimativas de recursos antes de significarem tempo.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) calcular em aritmética modular e em anéis de polinômios; (2) explicar o anel Z_q[x]/(x^n+1) usado pelo ML-KEM e pelo ML-DSA; (3) enunciar as propriedades de segurança de uma função de hash; e (4) ligar a estrutura de grupo ao motivo pelo qual o algoritmo de Shor funciona. O capítulo parte do Capítulo 1 e prepara a probabilidade (Capítulo 7) e os métodos de reticulados do Capítulo 24.

### 2.1 Aritmética modular

A aritmética módulo *q* mantém os números em {0, …, *q*−1}. O RSA usa um módulo composto; a criptografia de curvas elípticas usa grupos de pontos sobre um corpo primo. Ambos dependem da dificuldade de encontrar um *período* oculto — a ordem de um elemento ou um logaritmo discreto. A percepção de Shor é que um computador quântico consegue encontrar períodos com eficiência usando a transformada quântica de Fourier; é por isso que todos os esquemas cuja segurança se reduz a um período oculto num grupo abeliano caem juntos.

Essa fraqueza comum explica por que a migração não pode ser feita um algoritmo de cada vez, trocando o RSA por curvas elípticas: os dois caem diante da mesma ideia. Os esquemas pós-quânticos são escolhidos justamente porque os seus problemas difíceis, como equações lineares com ruído ou a inversão de hashes, não têm nenhum período oculto conhecido que um computador quântico possa encontrar.

### 2.2 Anéis de polinômios

O ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)) calcula com polinômios de grau menor que 256 cujos coeficientes são inteiros módulo *q* = 3329, reduzidos módulo *x*^256 + 1. Nesse anel, multiplicar por *x* desloca os coeficientes uma posição para cima, e o coeficiente que sai pelo topo volta para a base com o sinal trocado, porque *x*^*n* = −1. Vetores e matrizes desses polinômios formam um *módulo*, daí "reticulado modular" (module-lattice). A estrutura dá chaves compactas e multiplicação rápida (pela transformada de teoria dos números, NTT), enquanto a dificuldade vem do acréscimo de um pequeno ruído — o assunto do Capítulo 24.

### 2.3 Atividade prática — Laboratório R

```python
# Lab R (ch 2): multiplication in R_q = Z_q[x]/(x^n + 1), the ring behind ML-KEM (there n=256, q=3329).
q, n = 17, 4
def mul(a, b):
    c = [0] * n
    for i in range(n):
        for j in range(n):
            k = i + j
            if k < n:
                c[k] = (c[k] + a[i] * b[j]) % q
            else:                       # x^n = -1, so wrap around with a sign flip
                c[k - n] = (c[k - n] - a[i] * b[j]) % q
    return c
a = [1, 2, 0, 3]      # 1 + 2x + 3x^3
b = [0, 1, 0, 0]      # x
print("a*x  =", mul(a, b), " (coefficients shift; x^3 * x = x^4 = -1 -> 17-3 = 14)")
print("a*a  =", mul(a, a))
```

Saída esperada:

```text
a*x  = [14, 1, 2, 0]  (coefficients shift; x^3 * x = x^4 = -1 -> 17-3 = 14)
a*a  = [6, 4, 12, 6]
```

Verificação à mão: (1 + 2*x* + 3*x*³)·*x* = *x* + 2*x*² + 3*x*⁴ = *x* + 2*x*² − 3 ≡ 14 + *x* + 2*x*² (mod 17).

A verificação à mão mostra a regra de volta em ação: o termo x⁴ ultrapassa o limite de grau para n igual a quatro, então vira menos três, e menos três módulo dezessete é quatorze. O ML-KEM usa a mesma regra com n igual a 256 e q igual a 3329. Estudantes que erram o sinal calculam um polinômio diferente, e numa implementação real esse erro quebraria todo desencapsulamento, e é por isso que os testes de resposta conhecida (KAT) o detectam de imediato.

### 2.4 Funções de hash

Um hash criptográfico mapeia qualquer entrada num resumo de tamanho fixo. As propriedades exigidas são *resistência à pré-imagem* (dado um resumo, não encontrar nenhuma entrada), *resistência à segunda pré-imagem* e *resistência a colisões*. As assinaturas baseadas em hash (SLH-DSA na [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205); LMS e XMSS na [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208)) precisam apenas dessas propriedades, e é por isso que são as assinaturas pós-quânticas mais conservadoras: não se sabe de computadores quânticos que façam muito melhor do que acelerações no estilo de Grover contra boas funções de hash.

Grover consegue buscar pré-imagens mais depressa, tirando aproximadamente a raiz quadrada do trabalho, então um hash de 256 bits ainda oferece cerca de 128 bits contra a busca de pré-imagem. A busca de colisões com algoritmos quânticos ganha, na prática, menos do que os limites idealizados sugerem. O preço das assinaturas baseadas em hash é tamanho e velocidade, não pressupostos de segurança.

### 2.5 Exemplo resolvido

Um desenvolvedor da BPA pergunta por que a biblioteca pós-quântica "multiplica polinômios" quando o RSA "só exponencia". A resposta: a segurança do RSA está no grupo multiplicativo módulo *N*, onde Shor encontra períodos. A do ML-KEM está na álgebra linear com ruído sobre um anel de polinômios, onde não se conhece atalho de busca de períodos; o anel serve à eficiência, o ruído serve à segurança.

A pergunta seguinte do desenvolvedor costuma ser sobre custo: a multiplicação de polinômios com a transformada de teoria dos números é rápida, e a geração de chaves do ML-KEM costuma ser mais rápida do que a do RSA. O que muda para o sistema é o tamanho: chaves e textos cifrados são maiores que os de curvas elípticas. Isso desloca o problema de engenharia do tempo de CPU para os bytes na rede.

### 2.6 Erros comuns e limites

- Esquecer a troca de sinal ao reduzir por *x*^*n* + 1.
- Achar que a estrutura de anel sozinha dá segurança (sem ruído, o sistema linear é fácil).
- Confundir resistência a colisões com resistência à pré-imagem.

Uma troca de sinal esquecida produz saídas que parecem plausíveis, mas falham nos testes de interoperabilidade contra a norma. Supor que o anel sozinho dá segurança ignora o papel do ruído: sem erros pequenos, a eliminação gaussiana recupera o segredo. Confundir resistência a colisões e à pré-imagem leva a afirmações erradas sobre parâmetros, por exemplo, reduzir à metade o tamanho de um hash para um uso que só precisa de resistência à pré-imagem.

### Exercícios

- **EX003 — Multiplicação no anel.** Calcule à mão (2 + *x*)(3 + *x*³) em Z_17[*x*]/(*x*⁴ + 1) e confira com o Laboratório R. Rubrica: 3 = correto, com os passos de redução.
- **EX004 — Propriedades do hash.** Para o SLH-DSA, um manifesto de integridade de arquivos e o armazenamento de senhas, diga qual propriedade do hash mais importa. Rubrica: 3 = correto e justificado.

### Síntese

A criptografia de chave pública tradicional esconde um período que o algoritmo de Shor encontra; os esquemas de reticulados calculam num anel de polinômios e escondem os segredos sob ruído; os esquemas baseados em hash dependem apenas das propriedades do hash.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 50

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) descrever em termos de engenharia um qubit, a superposição, a medição e o emaranhamento; (2) explicar a decoerência e por que a correção de erros domina o custo de um computador quântico; (3) distinguir qubits físicos de lógicos; e (4) separar a computação quântica da distribuição quântica de chaves. O capítulo parte dos Capítulos 1–2 e enquadra a ameaça usada ao longo do livro.

### 3.1 Qubits e medição

Um bit clássico é 0 ou 1. O estado de um qubit é uma combinação α|0⟩ + β|1⟩ com amplitudes complexas cujos módulos ao quadrado somam um; a medição devolve 0 com probabilidade |α|² e 1 com probabilidade |β|², e destrói a superposição. *n* qubits são descritos por 2^*n* amplitudes, mas a medição rende apenas *n* bits, de modo que um algoritmo quântico precisa arranjar a interferência para que as respostas erradas se cancelem e as certas se reforcem. O algoritmo de Shor faz isso para períodos; para a maioria dos problemas não se conhece arranjo assim, e é por isso que computadores quânticos não são aceleradores de uso geral.

### 3.2 Emaranhamento e portas

Qubits emaranhados têm resultados de medição correlacionados que não podem ser explicados por estados independentes. Portas — rotações de qubits isolados e operações controladas sobre pares — formam circuitos. Os algoritmos são medidos em contagem de portas lógicas e em *profundidade* do circuito, o número de camadas sequenciais, que importa porque os erros se acumulam com o tempo.

A profundidade importa porque os qubits perdem coerência enquanto esperam: um circuito com muitas camadas sequenciais precisa terminar antes que os erros o dominem, ou a correção de erros precisa acompanhar o ritmo. É por isso que as estimativas de recursos informam tanto os qubits lógicos quanto um tempo de execução. O emaranhamento é um recurso que os algoritmos usam, não uma aceleração por si só; a maioria dos problemas não ganha nada com ele.

### 3.3 Decoerência e correção de erros

Os qubits físicos perdem o estado pela interação com o ambiente (decoerência) e por portas imperfeitas. A correção quântica de erros codifica um qubit *lógico* em muitos qubits *físicos* — em projetos de código de superfície, de centenas a milhares — e mede continuamente as síndromes para corrigir erros. Esse custo adicional explica por que as estimativas para quebrar o RSA-2048 passaram de vinte milhões de qubits ruidosos ([Gidney e Ekerå 2021](https://doi.org/10.22331/q-2021-04-15-433)) para menos de um milhão ([Gidney 2025](https://arxiv.org/abs/2505.15917)) à medida que algoritmos e códigos melhoraram — e por que as contagens de qubits físicos em comunicados de imprensa dizem pouco sobre relevância criptográfica sem as taxas de erro.

### 3.4 A distribuição quântica de chaves é outra coisa

A distribuição quântica de chaves (QKD) usa estados quânticos da luz para acordar chaves, com segurança fundamentada na física, mas precisa de hardware especial, enlaces ponto a ponto e canais clássicos autenticados, e não oferece assinaturas. Várias agências, incluindo a [NSA](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/), recomendam a PQC, e não a QKD, para a maioria dos usos. Este livro trata a QKD como uma tecnologia de nicho e a PQC como o caminho da migração.

A QKD também deixa a autenticação para a criptografia clássica, então um enlace QKD continua precisando de assinaturas ou de chaves pré-compartilhadas, o que traz a PQC de volta ao projeto. Os seus limites de distância e os relés de nós confiáveis acrescentam problemas de segurança física. Para a troca de dados aduaneiros da BPA pela internet pública, a QKD não é opção, enquanto o TLS híbrido com ML-KEM pode ser implantado nos servidores existentes.

### 3.5 Exemplo resolvido

Um fornecedor diz à BPA que "foi anunciada uma máquina de 1.000 qubits, então o RSA logo estará quebrado". A resposta de engenharia: pedir taxas de erro, contagem de qubits lógicos e profundidade do circuito; comparar com as estimativas de recursos publicadas; notar que mil qubits físicos ruidosos estão ordens de grandeza abaixo das estimativas; e migrar mesmo assim, porque o tráfego gravado precisa continuar secreto por décadas (Capítulo 20).

O número do fornecedor não responde a nenhuma das perguntas que importam para o RSA-2048. Os qubits físicos precisam ser convertidos em lógicos numa razão de centenas ou milhares, e o circuito precisa rodar tempo suficiente sem falhar. Ainda assim, a conclusão é continuar migrando: o argumento para agir se apoia em quanto tempo os dados aduaneiros precisam continuar secretos, não na data do próximo anúncio.

### 3.6 Erros comuns e limites

- Dizer que os computadores quânticos "testam todas as respostas ao mesmo tempo".
- Igualar qubits físicos e lógicos.
- Apresentar a QKD como substituta da PQC.

A superposição não permite que um computador quântico leia todas as respostas; a medição devolve um resultado, e só ajuda a interferência projetada para uma estrutura específica. Qubits físicos e lógicos diferem pelo custo da correção de erros, então manchetes sobre contagens de qubits dizem pouco sobre o risco criptográfico. A QKD precisa de enlaces dedicados e deixa as assinaturas sem solução, então não pode substituir a PQC em redes comuns como os enlaces de internet usados pelos parceiros da BPA.

### Exercícios

- **EX005 — Aritmética do custo adicional.** Se um qubit lógico precisa de 1.000 qubits físicos e um algoritmo precisa de 1.400 qubits lógicos mais 30% de custo adicional de qubits auxiliares (ancilla), quantos qubits físicos são necessários? Rubrica: 3 = correto (1,82 milhão) e comentário sobre os pressupostos.
- **EX006 — Alegação do fornecedor.** Escreva três perguntas que transformem um anúncio de contagem de qubits em evidência. Rubrica: 3 = taxa de erro, contagem lógica, profundidade/tempo.

### Síntese

Os algoritmos quânticos exploram a interferência para problemas especiais; a correção de erros torna enormes as máquinas úteis; os anúncios precisam ser traduzidos em recursos lógicos; a QKD não é o caminho da migração.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 50

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas Python pequenos e testáveis com a biblioteca padrão; (2) tratar corretamente bytes, codificações e inteiros; (3) usar com segurança `hashlib`, `hmac` e `secrets`; e (4) reconhecer por que você não deve implementar criptografia de produção por conta própria. O capítulo prepara os laboratórios usados ao longo do livro.

### 4.1 Bytes, não strings

As funções criptográficas operam sobre bytes. O `str` do Python é texto; converta com uma codificação explícita (`"text".encode("utf-8")`). Misturar os dois causa bugs sutis, como calcular o hash da representação textual de um objeto bytes (`"b'...'"`) em vez dos próprios bytes. Os inteiros se convertem com `int.from_bytes(b, "big")` e `n.to_bytes(length, "big")`; declare sempre a ordem dos bytes e o comprimento, porque especificações de protocolo como a FIPS 203 definem codificações exatas.

Um sintoma comum da mistura de tipos são dois sistemas calculando hashes diferentes para a mesma mensagem porque um codificou o texto como UTF-8 e o outro como Latin-1. Fixar a codificação na fronteira e passar bytes em todo o interior elimina essa classe de bug. Comprimento e ordem dos bytes também importam: a FIPS 203 codifica os coeficientes num leiaute de bits preciso, e um teste contra os vetores da norma é a única verificação confiável.

### 4.2 Aleatoriedade

Use `secrets.token_bytes()` para chaves e nonces; nunca `random`, que é um gerador pseudoaleatório previsível, feito para simulações. Os laboratórios deste livro usam `random` apenas para gerar dados sintéticos e parâmetros de brinquedo, e dizem isso.

O `random` do Python parte de um estado que pode ser recuperado depois de observadas saídas suficientes, de modo que qualquer chave produzida por ele pode ser prevista. O `secrets` obtém os dados do gerador criptográfico do sistema operacional. Manter os dois visivelmente separados no código, por exemplo nunca importando `random` em módulos de produção, facilita as revisões e impede que código de brinquedo escorregue para sistemas reais.

### 4.3 Hashes e MACs

Estão disponíveis `hashlib.sha256`, `hashlib.sha3_256` e `hashlib.shake_256`; o SHA-3 e o SHAKE são usados dentro do ML-KEM e do ML-DSA. `hmac.new(key, msg, hashlib.sha256)` calcula um código de autenticação de mensagem, e `hmac.compare_digest` compara tags em tempo constante — um `==` comum pode vazar, pelo tempo, onde dois valores começam a diferir.

O SHAKE é uma função de saída extensível: pode produzir quantos bytes de saída forem necessários, o que o ML-KEM usa para expandir sementes em matrizes. Um MAC difere de um hash porque precisa de uma chave secreta; sem ela, qualquer um pode recalcular o hash de uma mensagem modificada. A comparação em tempo constante importa sobretudo quando o atacante pode enviar muitos palpites e medir os tempos de resposta.

### 4.4 Testes

Toda função recebe um teste com resposta conhecida. Em criptografia, os *testes de resposta conhecida* (KATs) publicados com as normas permitem confirmar que uma implementação produz exatamente os bytes esperados. O Cryptographic Algorithm Validation Program do NIST publica vetores de teste para os algoritmos aprovados.

Um KAT fixa as entradas, inclusive o que normalmente seria aleatório, de modo que a saída esperada é uma única sequência exata de bytes. Passar nos KATs prova que a implementação coincide com a norma nessas entradas; não prova resistência a canais laterais nem a mau uso. Os engenheiros executam os KATs na integração contínua, para que uma atualização de biblioteca que mude as saídas seja detectada antes da implantação.

### 4.5 Exemplo resolvido: um log de auditoria em cadeia de hashes

A BPA quer logs que evidenciem adulteração. Cada entrada guarda `h_i = SHA-256(h_{i-1} || entry_i)`. Um programa curto calcula a cadeia, e um teste verifica que alterar qualquer entrada muda todos os hashes posteriores. O programa usa bytes do começo ao fim, codificações fixas e `compare_digest`. Esse é um uso sólido de primitivas padronizadas; projetar um novo esquema de assinatura não seria.

A cadeia detecta modificação, remoção e reordenação, porque cada mudança altera todos os hashes posteriores. Ela não impede que alguém com acesso de escrita reconstrua a cadeia inteira, por isso a BPA publica o hash mais recente diariamente num sistema separado. O programa é curto o bastante para ser revisado por completo, e toda primitiva que ele usa já é padronizada.

### 4.6 Atividade prática

Escreva a função da cadeia de hashes com um teste, depois acrescente um bug deliberado (calcular o hash de `str(entry)` em vez de `entry`) e veja o teste detectá-lo.

O bug deliberado mostra por que os testes precisam comparar bytes exatos: o hash de `str(entry)` é calculado sobre o texto "b'...'", com aspas e um prefixo, então todos os hashes posteriores mudam, embora o conteúdo do log pareça idêntico. Escreva primeiro o teste que falha, confirme que ele falha com o bug, depois corrija o código e confirme que ele passa. Mantenha o teste na suíte para que o erro não volte.

### 4.7 Erros comuns e limites

- Usar `random` para chaves.
- Comparar segredos com `==`.
- Implementar você mesmo o ML-KEM ou o ML-DSA para produção: a segurança da implementação (Capítulo 31) é mais difícil do que a correção.

Cada erro já causou falhas reais. Números aleatórios previsíveis expuseram chaves, comparações simples vazaram tags de autenticação pelo tempo e implementações caseiras de algoritmos padronizados passaram nos testes de correção enquanto vazavam segredos pelo tempo ou pelo consumo de energia. A BPA usa bibliotecas verificadas para o ML-KEM e o ML-DSA e reserva o próprio código para a cola em volta delas, que testa com KATs.

### Exercícios

- **EX007 — Bug de codificação.** Explique por que `hashlib.sha256(str(b"abc").encode())` difere de `hashlib.sha256(b"abc")` e que classe de bug isso representa. Rubrica: 3 = correto e generalizado.
- **EX008 — Cadeia de hashes.** Escreva a função da cadeia de hashes e um teste que detecte adulteração. Rubrica: 3 = executa, os testes passam, usa bytes e `compare_digest`.

### Síntese

O código criptográfico é exato em bytes, usa aleatoriedade segura, compara segredos em tempo constante e é testado contra respostas conhecidas; os engenheiros compõem primitivas verificadas em vez de inventá-las.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 50

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever um memorando de decisão que separe fatos, pressupostos e recomendações; (2) apresentar com honestidade a incerteza sobre os prazos quânticos; (3) desenhar diagramas de arquitetura com alternativas em texto; e (4) adaptar uma mensagem para públicos técnicos e executivos. O capítulo parte dos Capítulos 1–4 e é usado em todas as revisões de projeto posteriores.

### 5.1 O memorando de decisão

Um memorando abre com a decisão solicitada e depois apresenta contexto, opções, recomendação, riscos e o que mudaria a recomendação. No trabalho com PQC, rotule quatro tipos de afirmação: **fato** ("a FIPS 203 foi publicada em agosto de 2024"), **pressuposto** ("planejamos como se um computador quântico criptograficamente relevante pudesse existir dentro de 15 anos"), **estimativa** ("a migração da VPN levará nove meses") e **recomendação**. Misturá-los é a forma como os prazos viram mitos.

Rotular cada afirmação permite que os leitores contestem a coisa certa. Um fato pode ser conferido na fonte; um pressuposto pode ser variado para ver se a recomendação se mantém; uma estimativa pode ser comparada depois com o progresso real. Quando uma frase os mistura, como uma data de migração apresentada como certa, ninguém consegue saber qual parte questionar.

### 5.2 Comunicar a incerteza

Nunca dê um único "Q-Day". Declare uma faixa de pressupostos e mostre quais decisões são robustas ao longo dela. A desigualdade de Mosca — se o tempo de vida dos dados mais o tempo de migração excede o tempo até a computação quântica, aja agora ([Mosca 2018](https://doi.org/10.1109/MSP.2018.3761723)) — é útil justamente porque pode ser avaliada ao longo de uma faixa. Uma recomendação que vale para todas as faixas plausíveis é fácil de defender.

Na prática, o memorando mostra uma pequena tabela: linhas para o tempo até a computação quântica assumido, colunas para o tempo de vida dos dados e o tempo de migração, e células que marcam onde é preciso agir. Se todas as células disserem "aja", o debate sobre o ano exato se torna irrelevante. Se a resposta mudar dentro da faixa plausível, o memorando diz isso e explica que nova evidência resolveria a questão.

### 5.3 Diagramas

Os diagramas de arquitetura mostram componentes, fronteiras de confiança e onde acontece cada função criptográfica: troca de chaves, assinatura, dados em repouso. Todo diagrama precisa de uma alternativa em texto que descreva o mesmo conteúdo, por acessibilidade e para a revisão; os revisores muitas vezes encontram erros quando são obrigados a ler a versão em texto.

Marcar onde acontece cada função criptográfica mostra num relance o escopo da migração: toda seta de troca de chaves e de assinatura é candidata a mudança, enquanto a cifragem simétrica em repouso talvez só precise de chaves maiores. A versão em texto lista cada seta com o seu algoritmo e responsável. Os revisores que leem essa lista muitas vezes encontram uma dependência oculta, como uma assinatura usada num caminho de atualização de firmware que o diagrama desenhou como uma única caixa.

### 5.4 Públicos

Para engenheiros: algoritmos, conjuntos de parâmetros, protocolos, evidências de testes. Para executivos: risco, custo, cronograma, o que está protegido e o que não está. Para auditores: rastreabilidade dos requisitos e evidências. Os mesmos fatos, em outra ordem.

Um engenheiro que lê a versão executiva pode achar que falta detalhe, e um executivo que lê a versão de engenharia pode não encontrar a decisão. Escrever versões separadas a partir de uma única fonte de fatos as mantém coerentes. Os auditores precisam de uma terceira ordem: cada requisito, a evidência de que é atendido e onde essa evidência está guardada. A BPA mantém as três versões num único repositório, para que um fato alterado atualize todos os públicos ao mesmo tempo.

### 5.5 Exemplo resolvido: o memorando de uma página da BPA

Decisão solicitada: financiar um inventário criptográfico de 12 meses e um piloto de TLS híbrido. Fatos: as normas existem; os registros aduaneiros precisam permanecer confidenciais por 25 anos. Pressuposto: tempo até a computação quântica variado de 10 a 30 anos. Constatação: para registros de 25 anos, qualquer tempo até a computação quântica abaixo de cerca de 26 anos (25 anos de confidencialidade mais cerca de 9 meses de migração) significa que o tráfego gravado hoje está em risco — então a decisão é robusta em toda a faixa de 10–30 anos, exceto na sua cauda otimista, e a cauda não muda a ação. Não se afirma: nenhuma data. Riscos: incompatibilidade de middleboxes, atraso dos fornecedores.

### 5.6 Erros comuns e limites

- Slides executivos com uma única data para os computadores quânticos.
- Diagramas sem alternativas em texto.
- Memorandos que enterram a decisão na página três.

Uma única data convida à discussão sobre a data em vez da decisão, e fica errada assim que as estimativas mudam. Um diagrama sem texto exclui leitores que usam leitores de tela e esconde erros que a escrita exporia. Uma decisão enterrada faz os executivos saírem da reunião sem tomá-la. Cada um desses problemas é fácil de corrigir antes de enviar o memorando.

### Exercícios

- **EX009 — Rotular afirmações.** Rotule dez frases de um folheto de fornecedor como fato, pressuposto, estimativa ou recomendação. Rubrica: 3 = todas corretas, com justificativa para os casos de fronteira.
- **EX010 — Reescrita executiva.** Reescreva em 100 palavras, para o conselho da BPA, um parágrafo técnico sobre a escolha de parâmetros do ML-KEM. Rubrica: 3 = preciso, sem jargão, decisão clara.

### Síntese

Uma boa comunicação de engenharia rotula fatos, pressupostos, estimativas e recomendações, expressa os prazos como faixas, dá aos diagramas alternativas em texto e ordena os mesmos fatos para cada público.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 50

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar modelos exponenciais e logarítmicos de crescimento e decaimento; (2) calcular somas e integrais que aparecem em modelos de custo e de risco; (3) aplicar otimização para escolher parâmetros sob restrições; e (4) modelar a janela de exposição do "colete agora, decifre depois". O capítulo parte do Capítulo 1 e apoia o desempenho (Capítulo 36) e a otimização (Capítulo 41).

### 6.1 Modelos exponenciais

Muitas grandezas deste campo são modeladas exponencialmente: o volume de tráfego gravado, a queda do custo por qubit, a perda de utilidade de um certificado. Um modelo *f*(*t*) = *f*₀·*e*^(*rt*) tem tempo de duplicação ln 2 / *r*. Os engenheiros devem tratar esses modelos como cenários: um tempo de duplicação assumido para a qualidade dos qubits é um pressuposto, não uma lei.

O tempo de duplicação é a forma mais intuitiva de enunciar um modelo exponencial: se o tráfego gravado dobra a cada 3,8 anos, o leitor consegue imaginar o crescimento sem logaritmos. Mostrar os resultados num cenário rápido e num lento mantém o modelo honesto. Se a recomendação mudar entre os cenários, o memorando precisa dizer qual pressuposto provoca a mudança.

### 6.2 Somas e integrais para a exposição

Suponha que a BPA grave tráfego a uma taxa de *v*(*t*) GB por ano e que todo tráfego gravado antes da data de migração *T* fique exposto se um CRQC aparecer no instante *Z*. O volume exposto é a integral de *v* de 0 a *T*. Se *v* cresce exponencialmente, ∫₀^*T* *v*₀*e*^(*rt*) d*t* = (*v*₀/*r*)(*e*^(*rT*) − 1): adiar a migração faz a exposição crescer mais que linearmente. A lição de engenharia é que um atraso de um ano no fim do programa custa mais exposição do que um atraso de um ano no começo.

### 6.3 Otimização

A escolha de parâmetros é otimização com restrições. Exemplo: escolher um conjunto de parâmetros do ML-KEM que maximize a segurança dentro de um orçamento de bytes do handshake. O ML-KEM-512, o -768 e o -1024 oferecem as categorias 1, 3 e 5 do NIST, com chaves de encapsulamento de 800, 1.184 e 1.568 bytes ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)). Se o orçamento para o compartilhamento de chave do cliente for de 1.300 bytes, o ML-KEM-768 é o maior que cabe. Os multiplicadores de Lagrange formalizam esses compromissos para variáveis contínuas; em conjuntos discretos de parâmetros, basta enumerar.

O orçamento de bytes vem de limites reais: algumas redes fragmentam ou descartam mensagens de handshake acima de certos tamanhos, e middleboxes podem rejeitar registros incomuns. Escolher o ML-KEM-768 dentro de um orçamento de 1.300 bytes dá segurança de categoria 3 com folga. Se o orçamento fosse de 1.000 bytes, só o ML-KEM-512 caberia, e o memorando teria de discutir se a categoria 1 é aceitável.

### 6.4 Exemplo resolvido

A troca de dados aduaneiros da BPA envia hoje 2 TB/ano, com crescimento de 20% ao ano (*r* ≈ 0,182). Volume exposto se a migração terminar após 3 anos: (2/0,182)(*e*^0,547 − 1) ≈ 8,0 TB; após 5 anos: ≈ 16,3 TB. Dois anos a mais praticamente dobram o arquivo exposto.

Com r igual a 0,182, os termos exponenciais valem cerca de 1,73 após três anos e 2,49 após cinco. Multiplicar o excesso sobre um por cerca de onze, o fator dois dividido por r, dá os dois números. A duplicação mostra por que o plano do programa antecipa a troca de dados aduaneiros: ela tem o volume que cresce mais depressa e o requisito de confidencialidade mais longo.

### 6.5 Atividade prática

Calcule o volume exposto para migrações concluídas após 1–8 anos e faça um gráfico (ou uma tabela). Identifique o ano em que a exposição passa de 10 TB.

Use a fórmula do exemplo resolvido em vez de somar volumes anuais: somar 2, 2,4, 2,88 e assim por diante trata o tráfego de cada ano como se chegasse no primeiro dia e dá totais um pouco menores, cerca de 7,3 TB após três anos em vez de 8,0. Os dois métodos concordam sobre o primeiro ano que passa de 10 TB, mas só a integral coincide com os números do exemplo resolvido e dos exercícios. Tabular cada ano mostra as diferenças entre anos consecutivos crescendo, que é o efeito não linear que torna caros os atrasos tardios. Os estudantes devem declarar o pressuposto de crescimento ao lado da tabela e refazê-la com 10% e 30%.

### 6.6 Erros comuns e limites

- Tratar pressupostos de crescimento como previsões.
- Pensar linearmente sobre o atraso sob crescimento exponencial.
- Ignorar que a exposição também depende de quanto tempo os dados permanecem sensíveis (Capítulo 20).

As taxas de crescimento são pressupostos; uma taxa de 20% pode cair se um serviço for desativado ou subir se novos parceiros entrarem. O raciocínio linear subestima o custo do atraso, porque cada ano posterior acrescenta mais volume do que o anterior. A exposição também depende do tempo de vida: um tráfego que perde valor após um ano importa menos do que registros aduaneiros que precisam permanecer confidenciais por vinte e cinco anos.

### Exercícios

- **EX011 — Integral da exposição.** Calcule o volume exposto da BPA para *T* = 4 anos. Rubrica: 3 = correto (≈ 11,8 TB), com o cálculo.
- **EX012 — Escolha com orçamento.** Com um orçamento de 900 bytes para o compartilhamento do cliente, qual conjunto do ML-KEM cabe, e o que o engenheiro deve fazer se a categoria 3 for exigida? Rubrica: 3 = cabe o ML-KEM-512; propõe mudar o orçamento ou o transporte em vez de rebaixar em silêncio.

### Síntese

O cálculo transforma o momento da migração em exposição: sob crescimento, o atraso custa mais que linearmente; a escolha de parâmetros é otimização com restrições sobre conjuntos de parâmetros publicados.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 50

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) raciocinar sobre eventos raros, como falhas de decifração; (2) estimar taxas com intervalos de confiança; (3) distinguir níveis de segurança estatísticos de criptográficos; e (4) desenhar uma medição com amostras suficientes. O capítulo parte dos Capítulos 1 e 6 e apoia a medição (Capítulo 29) e a validação (Capítulo 38).

### 7.1 Eventos raros

Os KEMs de reticulados têm uma probabilidade minúscula de que o desencapsulamento produza a chave errada. Os conjuntos de parâmetros da FIPS 203 a mantêm extremamente pequena — cerca de 2^-139 para o ML-KEM-512 e menor para os conjuntos maiores —, muito abaixo de qualquer taxa que um engenheiro vá observar. O número esperado de falhas em *N* operações é *N*·*p*. O Laboratório P mostra por que uma probabilidade como 2^-20, aceitável para muitos fins de engenharia, seria inaceitável para um KEM usado bilhões de vezes, enquanto 2^-139 é desprezível em qualquer escala.

A regra de decisão é simples: multiplique pelo maior número de operações que o sistema jamais fará e confira que o produto fica muito abaixo de um.

### 7.2 Atividade prática — Laboratório P

```python
# Lab P (ch 7): how small must a failure probability be? Binomial reasoning for rare events.
import math
for p_exp in (-20, -40, -139):
    p = 10.0 ** (p_exp * math.log10(2))       # p = 2^p_exp
    for n_ops in (1e9, 1e15):
        exp_fail = n_ops * p
        print(f"p = 2^{p_exp:5d}, {n_ops:.0e} operations -> expected failures {exp_fail:.3e}")
```

Saída esperada:

```text
p = 2^  -20, 1e+09 operations -> expected failures 9.537e+02
p = 2^  -20, 1e+15 operations -> expected failures 9.537e+08
p = 2^  -40, 1e+09 operations -> expected failures 9.095e-04
p = 2^  -40, 1e+15 operations -> expected failures 9.095e+02
p = 2^ -139, 1e+09 operations -> expected failures 1.435e-33
p = 2^ -139, 1e+15 operations -> expected failures 1.435e-27
```

Leia as seis linhas aos pares. Com 2^-20, um bilhão de operações já produz quase mil falhas esperadas, então um esquema assim falharia visivelmente todos os dias na escala da BPA. Com 2^-40, um bilhão de operações parece seguro, mas um quatrilhão, aproximadamente o volume global de um protocolo amplamente implantado ao longo de alguns anos, dá cerca de 900. Com 2^-139, mesmo a contagem maior deixa uma expectativa de 1,4 × 10^-27, e é por isso que a falha de decifração não é, de modo algum, uma preocupação de projeto para o ML-KEM. Estenda o laço com 1e18 operações e confirme que a conclusão não muda.

### 7.3 Intervalos de confiança

Ao medir as taxas de falha de handshake depois de ativar um grupo híbrido, informe um intervalo, não apenas um ponto. Para proporções pequenas, use o intervalo de Wilson (o laboratório de canário do Capítulo 37 o usa). A *regra de três* dá um limite rápido: se ocorrerem zero falhas em *n* tentativas, o limite superior de 95% para a taxa é cerca de 3/*n*.

A regra decorre de exigir que zero falhas em n tentativas tenham no máximo 5% de chance: (1 − p)^n = 0,05 dá p ≈ 3/n. Ela só vale quando as tentativas são independentes; as falhas causadas por um proxy defeituoso se concentram num local, então um canário espalhado por vários locais dá um limite mais honesto do que a mesma contagem vinda de um só.

### 7.4 Segurança estatística versus criptográfica

Um teste estatístico que não encontra falhas em um milhão de execuções diz apenas que a taxa provavelmente está abaixo de 3 × 10^-6. Níveis de segurança criptográfica como 2^-128 não podem ser estabelecidos por testes; eles vêm da análise. Os engenheiros testam para encontrar bugs, não para provar segurança.

Para mostrar por testes uma taxa abaixo de 2^-128, seriam necessárias cerca de 10^39 tentativas, muito além de qualquer computador. Ainda assim vale a pena executar os testes, porque um bug de implementação costuma produzir falhas numa taxa de uma em algumas centenas ou milhares, que uma campanha de testes modesta detecta depressa. Uma execução limpa dos testes descarta, portanto, os bugs grosseiros e deixa a alegação de segurança para a análise publicada.

### 7.5 Exemplo resolvido

O piloto da BPA observa 0 falhas de handshake em 12.000 conexões híbridas num local. A regra de três limita a taxa de falhas abaixo de 2,5 × 10^-4 (95%). Isso basta para implantar em 2 milhões de conexões diárias? No limite, ainda poderiam ocorrer até 500 falhas por dia — então o portão de decisão exige um canário maior antes da implantação completa.

Para baixar o limite a cerca de uma falha por dia com 2 milhões de conexões, é preciso mostrar uma taxa abaixo de 5 × 10^-7, o que, pela regra de três, exige cerca de 6 milhões de conexões limpas. A BPA pode chegar lá ampliando o canário para vários locais durante alguns dias, o que também testa middleboxes diferentes.

### 7.6 Erros comuns e limites

- Interpretar "nenhuma falha observada" como "a taxa é zero".
- Confundir uma probabilidade de falha de decifração com um nível de segurança.
- Ignorar que as operações se multiplicam: raro por evento não é raro por ano.

O primeiro erro leva as equipes a declarar sucesso após um piloto pequeno, como no exemplo resolvido, em que zero falhas em 12.000 ainda permitiam 500 por dia. O segundo confunde dois números: a probabilidade de falha de 2^-139 do ML-KEM é um número de confiabilidade, enquanto a categoria 3 descreve o trabalho de que um atacante precisa. O terceiro se corrige multiplicando as taxas por evento pelo volume anual antes de julgá-las.

### Exercícios

- **EX013 — Regra de três.** Quantas tentativas sem falha são necessárias para limitar uma taxa abaixo de 10^-5? Rubrica: 3 = 300.000, com o raciocínio.
- **EX014 — Escala.** Se um componente falha com probabilidade 2^-30 por operação e a BPA executa 10^10 operações por ano, quantas falhas são esperadas? Rubrica: 3 = ≈ 9,3 e interpretação.

### Síntese

Eventos raros se tornam comuns em escala; os testes limitam taxas, mas não estabelecem segurança criptográfica; informe intervalos e dimensione as amostras para a decisão a tomar.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 50

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) relacionar o desempenho dos algoritmos a recursos do processador, como unidades vetoriais e caches; (2) explicar os canais laterais de tempo e de consumo de energia; (3) avaliar memória e tamanho de código em dispositivos restritos; e (4) entender os módulos de segurança de hardware (HSMs) e as suas restrições de migração. O capítulo prepara a implementação (Capítulos 28 e 31) e o desempenho (Capítulo 36).

### 8.1 Recursos de desempenho

Os esquemas de reticulados passam a maior parte do tempo na multiplicação de polinômios pela transformada de teoria dos números e no cálculo de hashes com SHAKE. As instruções vetoriais (AVX2 em x86, NEON em ARM) paralelizam as operações sobre coeficientes, tornando o ML-KEM muito rápido em servidores. Microcontroladores restritos sem unidades vetoriais são mais lentos, mas muitas vezes ainda aceitáveis; ali, o limite costuma ser a memória, não a velocidade.

Para a BPA, isso significa que os servidores TLS gastarão mais tempo enviando bytes do que calculando; resultados de benchmark que mostram a geração de chaves do ML-KEM mais rápida que a do X25519 num servidor não se transferem para um controlador de guindaste.

### 8.2 Canais laterais

O tempo de execução, os padrões de acesso à cache e o consumo de energia podem revelar segredos se dependerem de valores secretos. As descobertas do "KyberSlash" mostraram que uma divisão por uma constante cujo dividendo dependia de dados secretos vazava tempo em várias implementações do Kyber ([Bernstein et al. 2024](https://eprint.iacr.org/2024/1049)). Código em tempo constante — sem desvios, índices de memória ou instruções de tempo variável que dependam de segredos — é um requisito, não uma otimização.

A correção, nesse caso, foi substituir a divisão por uma multiplicação e um deslocamento que levam o mesmo tempo para qualquer entrada. As revisões procuram o mesmo padrão em outros lugares: qualquer desvio, consulta a tabela ou divisão cuja entrada dependa de uma chave ou de um valor decifrado. Ferramentas que executam o código com entradas marcadas como secretas e apontam essas dependências ajudam, mas precisam rodar sobre o binário compilado, porque os compiladores podem reintroduzir desvios que o código-fonte não tinha.

### 8.3 Memória e tamanho de código

A assinatura com ML-DSA precisa de vários kilobytes de memória de trabalho; as assinaturas SLH-DSA são grandes, mas as chaves são minúsculas; os esquemas baseados em hash com estado precisam de um estado não volátil que nunca pode retroceder. Num scanner de portão com 64 KB de RAM, a escolha do algoritmo de verificação de assinaturas é uma decisão de arquitetura.

Um verificador ML-DSA-44 precisa da chave pública de 1.312 bytes, da assinatura de 2.420 bytes e de uma área de trabalho para a expansão da matriz, que algumas implementações mantêm pequena gerando as linhas sob demanda. Um verificador que cabe porque recalcula dados troca velocidade por memória, o que um scanner que verifica uma atualização por mês pode facilmente pagar. A revisão de arquitetura registra qual compromisso foi escolhido e por quê.

### 8.4 HSMs e elementos seguros

As chaves privadas da autoridade certificadora da BPA ficam num HSM. A migração precisa de um firmware de HSM que suporte o ML-DSA e, possivelmente, o LMS/XMSS com proteção de estado, validado no programa de certificação pertinente. Os ciclos de atualização de HSMs costumam durar anos — uma restrição clássica dos cronogramas de migração.

O plano da BPA faz, portanto, três perguntas ao fornecedor do HSM desde já: quais algoritmos pós-quânticos o firmware atual suporta, quando haverá firmware certificado e se o hardware existente pode ser atualizado ou precisa ser substituído. As respostas fixam a data mais cedo possível para emitir certificados ML-DSA, o que, por sua vez, restringe cada etapa posterior da migração da autenticação.

### 8.5 Exemplo resolvido

Os controladores de guindaste da BPA verificam assinaturas de firmware num bootloader com 32 KB de flash disponíveis. O código de verificação do ML-DSA-44 e uma chave pública de 1.312 bytes podem caber; um verificador LMS é menor e precisa apenas de hashing, e, como só a verificação acontece no dispositivo, o problema de estado do LMS fica no servidor de assinatura. A revisão de arquitetura registra as duas opções e os seus orçamentos de memória.

A decisão também depende da frequência com que o firmware é assinado. As chaves LMS só podem assinar um número fixo de mensagens, por exemplo 2^10 ou 2^15, e perder o estado do assinante pode causar reutilização de chave. Com algumas versões por ano, uma chave de 2^15 assinaturas dura indefinidamente, então o risco está no procedimento de backup do servidor de assinatura, não na capacidade.

### 8.6 Erros comuns e limites

- Fazer benchmarks só em servidores.
- Supor que uma implementação correta roda em tempo constante.
- Esquecer os prazos de compra de HSMs.

Os benchmarks em servidores escondem os limites de memória que decidem o que cabe num scanner de portão ou num controlador de guindaste, então cada classe de dispositivo precisa da sua própria medição. Uma implementação correta ainda pode vazar tempo, como mostrou o caso KyberSlash, e é por isso que o comportamento em tempo constante é testado separadamente das respostas conhecidas. As atualizações de HSM podem levar anos, então o pedido sai antes de o trabalho de software começar, como a BPA fez com a sua autoridade certificadora.

### Exercícios

- **EX015 — Revisão de canal lateral.** Identifique o risco de tempo em `if secret_coeff > q//2: x = slow_path()` e proponha uma correção. Rubrica: 3 = identifica o desvio e dá uma alternativa sem desvio.
- **EX016 — Adequação ao dispositivo.** Compare a verificação ML-DSA-44 e LMS para um bootloader de 32 KB. Rubrica: 3 = memória, localização do estado e normas (FIPS 204, SP 800-208) considerados.

### Síntese

A arquitetura determina velocidade, adequação à memória e vazamento: os esquemas de reticulados são rápidos com unidades vetoriais, o código em tempo constante é obrigatório, os dispositivos restritos moldam a escolha do algoritmo e os ciclos dos HSMs moldam os cronogramas.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 50

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar o código de modo que os algoritmos sejam substituíveis; (2) interpretar e validar entradas não confiáveis, como certificados e compartilhamentos de chave; (3) escrever testes baseados em propriedades e de resposta conhecida; e (4) gerenciar dependências de bibliotecas criptográficas. O capítulo parte do Capítulo 4 e prepara a agilidade (Capítulo 39).

### 9.1 Interfaces acima de implementações

Escreva o código contra interfaces — `kem.encapsulate(public_key)`, `signer.sign(message)` —, e não contra funções específicas de um algoritmo. Um identificador de algoritmo, escolhido pela política, seleciona a implementação. Essa é a base de programação da agilidade criptográfica ([CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1)): a migração passa a ser uma mudança de configuração mais testes, e não uma reescrita.

O arquivo de política nomeia um algoritmo por uso, como ML-DSA-65 para assinaturas de documentos eletrônicos, e o código nunca o menciona. Quando a BPA passar mais tarde de uma configuração híbrida para uma puramente pós-quântica, a mudança será uma linha na política mais a execução dos testes. A revisão de código verifica que nenhum módulo contorna a interface importando diretamente uma biblioteca de algoritmo.

### 9.2 Validação de entradas

As chaves e os textos cifrados pós-quânticos têm comprimentos fixos por conjunto de parâmetros. A FIPS 203 exige verificações nas chaves de encapsulamento (uma verificação de módulo de que os coeficientes codificados estão abaixo de *q*) e nas chaves de desencapsulamento antes do uso. O código deve rejeitar comprimentos errados antes de chamar uma biblioteca e nunca "preencher" ou "truncar" para fazer as entradas caberem.

Uma chave de encapsulamento ML-KEM-768 precisa ter exatamente 1.184 bytes, e um texto cifrado exatamente 1.088. Verificar esses comprimentos primeiro dá uma mensagem de erro clara e evita passar dados malformados para um código que poderia se comportar de forma imprevisível. A verificação de módulo detecta chaves cujos coeficientes foram codificados com valores de 3329 ou mais, que um par malicioso poderia enviar para sondar fraquezas de implementação.

### 9.3 Testes além dos exemplos

Os testes de resposta conhecida confirmam saídas exatas. Os testes baseados em propriedades verificam invariantes sobre muitas entradas aleatórias: decapsulate(encapsulate(pk)) produz a mesma chave; uma assinatura é válida para a mensagem assinada e falha para qualquer mudança de um bit. Os testes negativos importam tanto quanto os positivos.

Um teste de propriedade para o assinador da BPA executa mil mensagens aleatórias, assina cada uma, verifica cada uma e depois inverte um bit aleatório da mensagem e da assinatura, esperando que as duas verificações falhem. Um teste que só verificasse a verificação bem-sucedida passaria mesmo que `verify` sempre retornasse verdadeiro, que é exatamente o bug que os testes negativos existem para detectar.

### 9.4 Dependências

Fixe as versões das bibliotecas criptográficas, acompanhe os seus alertas de segurança e registre quais algoritmos e conjuntos de parâmetros cada uma expõe. Nomes da época dos rascunhos (por exemplo, "Kyber768") e nomes finais (ML-KEM-768) não são intercambiáveis: a norma final mudou detalhes, então as implementações dos rascunhos não interoperam com a FIPS 203.

O arquivo de dependências da BPA registra o nome da biblioteca, a versão exata e os algoritmos que essa versão oferece sob os nomes finais. Quando uma versão da biblioteca renomeia ou remove um algoritmo de rascunho, o build falha no momento da atualização, e não no handshake de um parceiro. O acompanhamento dos alertas importa porque as bibliotecas pós-quânticas são mais novas e tiveram mais correções de segurança por ano do que o código RSA maduro.

### 9.5 Exemplo resolvido

O serviço de documentos eletrônicos da BPA chama `rsa_sign()` em 41 lugares. A refatoração introduz `Signer`, com as implementações `RSA-PSS-3072` e `ML-DSA-65`, selecionadas por um arquivo de política. Uma suíte de testes percorre cada caminho de chamada com as duas. O diff é grande uma vez; a próxima migração será pequena.

Os 41 pontos de chamada são encontrados primeiro com uma busca por `rsa_sign`, e depois cada um é examinado em busca de pressupostos como um comprimento fixo de assinatura de 384 bytes numa coluna do banco de dados. As assinaturas ML-DSA-65 têm 3.309 bytes, então a mudança de esquema faz parte do mesmo item de trabalho. O arquivo de política começa com RSA-PSS-3072, para que nada mude para os usuários até a troca.

### 9.6 Erros comuns e limites

- Fixar no código nomes de algoritmos e comprimentos de chave.
- Tratar as versões de rascunho e final dos algoritmos como iguais.
- Testar apenas os caminhos de sucesso.

Nomes fixos no código transformam cada migração futura numa mudança de código em todos os pontos de chamada, que é exatamente o que a refatoração com `Signer` eliminou. As versões de rascunho e final diferem em detalhes, então uma biblioteca que ainda oferece o Kyber768 não interopera com o ML-KEM-768. Testar só os caminhos de sucesso deixa a validação e o tratamento de erros sem verificação, e os atacantes miram justamente esses caminhos com chaves e textos cifrados malformados.

### Nota de engenharia

As interfaces também precisam de identificadores de algoritmo versionados que viajem com os dados. Uma assinatura guardada hoje precisa carregar um identificador que nomeie o seu algoritmo e conjunto de parâmetros, para que um verificador daqui a dez anos selecione a implementação certa e possa recusar as aposentadas. Sem identificadores, os sistemas adivinham pelo comprimento, o que quebra assim que dois algoritmos compartilham um tamanho. Trate o identificador como parte do conteúdo assinado ou autenticado sempre que o formato permitir, para que um atacante não possa rotular de novo uma assinatura fraca como forte. É esse pequeno hábito de projeto que depois torna segura, e não apenas conveniente, a migração guiada por política do Capítulo 39.

### Exercícios

- **EX017 — Projeto de interface.** Escreva uma interface `KEM` (nomes de métodos e tipos) adequada ao ML-KEM e a um futuro HQC. Rubrica: 3 = nenhum pressuposto específico de algoritmo, como tamanhos.
- **EX018 — Verificação de comprimento.** Escreva um validador que rejeite uma chave de encapsulamento ML-KEM-768 de comprimento errado (correto: 1.184 bytes). Rubrica: 3 = rejeita, nunca preenche.

### Síntese

Algoritmos substituíveis começam no código: interfaces, identificadores escolhidos pela política, validação estrita, testes de propriedade e negativos e um acompanhamento de dependências que distingue rascunho de final.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 50

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança operacional em engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética profissional às decisões de migração criptográfica; (2) identificar quem arca com o risco do "colete agora, decifre depois"; (3) tratar com responsabilidade as descobertas de vulnerabilidades; e (4) evitar exagerar o risco quântico para vender produtos. O capítulo fecha o primeiro bloco de fundamentos e orienta todas as decisões de projeto posteriores.

### 10.1 Deveres

Os códigos de ética da engenharia põem o bem-estar público em primeiro lugar. No trabalho com PQC, isso significa proteger pessoas cujos dados continuarão sensíveis por décadas — registros médicos, jurídicos, aduaneiros e pessoais —, mesmo que o dano, se vier, venha anos depois da decisão do engenheiro. Significa também honestidade: nem minimizar o risco ("computação quântica é ficção científica") nem inflá-lo para vender ("o RSA será quebrado no ano que vem").

Para um engenheiro da BPA, honestidade significa apresentar lado a lado a faixa das estimativas de especialistas e o tempo de vida de 25 anos dos registros, sem escolher a data que convém ao orçamento.

### 10.2 Quem arca com o risco

Os titulares dos dados arcam com o risco do "colete agora, decifre depois", mas raramente decidem os orçamentos de migração. Um engenheiro ético torna essa assimetria visível nos memorandos de decisão: "Se adiarmos, os dados comerciais dos declarantes aduaneiros gravados de agora até a migração poderão se tornar legíveis para um adversário futuro."

O memorando então nomeia quem decide e quem seria prejudicado, para que o conselho veja que adiar transfere o risco para pessoas que não estão na sala. Quantificar a exposição, como na comparação entre 8,0 e 16,3 TB, torna a transferência concreta. Também dá aos representantes dos declarantes algo a perguntar quando a BPA prestar contas sobre a proteção de dados.

### 10.3 Interações com a segurança operacional

As mudanças criptográficas podem quebrar a disponibilidade: um handshake grande demais que um middlebox descarta, uma assinatura de firmware que um bootloader não consegue verificar, um certificado que um dispositivo médico rejeita. Em sistemas relacionados à segurança operacional — guindastes, controle de tráfego do porto —, uma atualização malsucedida pode parar as operações ou criar perigos. A gestão de mudanças com planos de reversão, testes em ambientes isolados e implantações escalonadas é um dever ético, não burocracia.

Na prática, a mudança de firmware dos guindastes da BPA é testada num controlador reserva, implantada num guindaste e mantida assim por uma semana antes dos demais.

### 10.4 Divulgação responsável e limites dos testes

Se os testes revelarem uma vulnerabilidade num produto, relate-a ao fornecedor e dê tempo para a correção antes de publicar. Nunca teste sistemas que você não está autorizado a testar e nunca execute experimentos de rebaixamento (downgrade) sobre tráfego de produção.

Para as equipes da BPA, autorização significa um escopo escrito que nomeia sistemas, datas e técnicas permitidas. Um teste de rebaixamento que remove o grupo híbrido de um ClientHello pertence a uma cópia de laboratório do portal, não ao serviço em produção, onde poderia quebrar as sessões dos parceiros. As descobertas em produtos de fornecedores vão primeiro ao fornecedor, com uma data de divulgação combinada de antemão.

### 10.5 Exemplo resolvido

Um fornecedor oferece à BPA um equipamento "à prova de computação quântica" que usa um algoritmo não publicado. Avaliação ética: um algoritmo não verificado não oferece garantia (o Rainbow e o SIKE foram quebrados apesar de anos de escrutínio público — [Beullens 2022](https://eprint.iacr.org/2022/214), [Castryck e Decru 2022](https://eprint.iacr.org/2022/975)); o marketing exagera; o dever do engenheiro é recomendar algoritmos padronizados e dizer por quê, mesmo que o fornecedor seja amigo da direção.

A avaliação escrita vai para o conselho, e não só para o fornecedor, para que as razões sobrevivam a qualquer pressão posterior para revertê-la.

### 10.6 Erros comuns e limites

- Adiar a migração porque o dano está longe.
- Aceitar termos de marketing como "à prova de computação quântica".
- Implantar mudanças criptográficas em sistemas de segurança operacional sem reversão.

Adiar parece seguro porque ninguém é prejudicado neste ano, mas o tráfego aduaneiro gravado acumula exposição a cada mês que a decisão espera. Alegações de "à prova de computação quântica" devem levar a pedir o algoritmo, a sua norma e o seu histórico de revisão. Sistemas de segurança operacional como os controladores de guindaste precisam de uma reversão testada antes de qualquer mudança na assinatura de firmware, já que um dispositivo que rejeita a própria atualização pode parar as operações.

### Exercícios

- **EX019 — Quem arca com o risco.** Para a BPA, liste três grupos que arcam com o risco quântico e como cada um é representado nas decisões. Rubrica: 3 = grupos distintos, lacuna de representação identificada.
- **EX020 — Carta ao fornecedor.** Escreva uma carta cordial recusando um algoritmo "à prova de computação quântica" não verificado. Rubrica: 3 = cita as normas e as quebras, oferece um caminho adiante.

### Síntese

A engenharia ética de PQC protege dados de vida longa em nome de pessoas que não conseguem ver o risco, comunica com honestidade, trata disponibilidade e segurança operacional como parte da segurança e rejeita criptografia não verificada.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 50

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (inglês) →](../../en/book/MANUSCRIPT.md#ch-11)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre a BPA são sintéticos. Esta edição parcial traz as resoluções de EX001–EX020; as de EX021–EX100 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

**EX001.** log₂(10^30) = 30 × 3,32 ≈ 99,7 → cerca de 100 bits. log₂(2^100 × 10^6) = 100 + 19,9 ≈ 120 bits.

**EX002.** O algoritmo de Shor reduziria a quebra do RSA de um esforço subexponencial inviável para um polinomial — um colapso qualitativo —, então o RSA precisa ser substituído. Grover apenas tira a raiz quadrada da busca por uma chave AES: o AES-256 ainda exigiria cerca de 2^128 passos sequenciais, o que continua muito fora de alcance. Substitua o RSA e as curvas elípticas; mantenha o AES-256.

**EX003.** (2 + *x*)(3 + *x*³) = 6 + 3*x* + 2*x*³ + *x*⁴ = 6 + 3*x* + 2*x*³ − 1 = 5 + 3*x* + 2*x*³ → [5, 3, 0, 2], o que coincide com o `mul` do Laboratório R.

**EX004.** SLH-DSA: resistência do tipo segunda pré-imagem/colisão dos seus hashes internos (a norma depende de propriedades específicas de hashes ajustáveis, *tweakable*); manifesto de arquivos: resistência à segunda pré-imagem (o atacante substitui um arquivo); armazenamento de senhas: resistência à pré-imagem mais lentidão deliberada (use uma função de hash de senhas, não um hash puro).

**EX005.** 1.400 × 1,3 = 1.820 qubits lógicos × 1.000 = 1,82 milhão de qubits físicos — sob taxas de erro e distância de código assumidas; outros pressupostos mudam o custo adicional por fatores grandes.

**EX006.** Quais são as taxas de erro das portas de dois qubits? Quantos qubits lógicos (com correção de erros) conseguem operar, e por quanto tempo? Que profundidade de circuito ou tempo de execução é alcançável para um algoritmo-alvo?

**EX007.** `str(b"abc")` é o texto "b'abc'", então a sua codificação UTF-8 são seis bytes, diferentes dos três bytes `abc`; a classe de bug é a confusão de tipos entre texto e bytes, que produz em silêncio resumos errados e falhas de interoperabilidade.

**EX008.** Uma função que itera `h = sha256(h + entry).digest()` a partir de um início fixo de 32 bytes zero; o teste modifica uma entrada e afirma, com `hmac.compare_digest`, que o hash final é diferente.

**EX009.** "A FIPS 203 foi publicada em 2024" = fato; "os computadores quânticos quebrarão o RSA até 2030" = pressuposto apresentado como fato; "o nosso equipamento migra em um dia" = estimativa; "compre agora" = recomendação. Os casos de fronteira exigem verificação das fontes.

**EX010.** "Vamos usar a versão de força intermediária do novo método padronizado de cifragem. Ela dá uma margem de segurança sólida por décadas, mantém as mensagens pequenas o bastante para a nossa rede e é o que os navegadores já usam. A versão mais forte fica reservada aos enlaces em que as regras de segurança nacional a exigem."

**EX011.** (2/0,1823)(*e*^(0,1823×4) − 1) = 10,97 × (2,074 − 1) ≈ 11,8 TB.

**EX012.** O ML-KEM-512 (800 B) cabe em 900 B; se a categoria 3 for exigida, mude o orçamento (por exemplo, aceite dois segmentos, ajuste o transporte) em vez de rebaixar em silêncio para a categoria 1.

**EX013.** 3/*n* ≤ 10^-5 → *n* ≥ 300.000 tentativas sem falha.

**EX014.** 10^10 × 2^-30 ≈ 9,3 falhas esperadas por ano — raras por operação, rotineiras por ano; projete para detecção e recuperação.

**EX015.** O tempo do desvio revela se o coeficiente secreto excede *q*/2; substitua por um cálculo de máscara em tempo constante (por exemplo, calcule uma máscara a partir do sinal de `q//2 - x` por deslocamento aritmético e selecione com operações bit a bit).

**EX016.** Verificação ML-DSA-44: código maior, chave de 1.312 bytes, sem estado; verificação LMS: só hashing, código muito pequeno, chave pequena; o estado de assinatura fica no HSM de assinatura (SP 800-208). Ambos podem caber; o LMS é menor, o ML-DSA evita a gestão de estado no assinante.

**EX017.** `generate_keypair() -> (public, secret)`, `encapsulate(public) -> (ciphertext, shared_secret)`, `decapsulate(secret, ciphertext) -> shared_secret`, mais `algorithm_id` e `sizes()` consultados na implementação, nunca fixados no código pelos chamadores.

**EX018.** `if len(ek) != 1184: raise ValueError(...)`; nunca preencher nem truncar; depois chamar a biblioteca, que também faz a verificação de módulo da FIPS 203.

**EX019.** Declarantes aduaneiros (segredos comerciais; representados indiretamente pela agência aduaneira), funcionários (dados de RH; representados pela comissão de trabalhadores/RH), parceiros de navegação (condições comerciais; representados pelos contratos). Lacuna: os titulares dos dados raramente estão na sala quando os orçamentos são definidos.

**EX020.** A carta agradece ao fornecedor, explica que a BPA usa apenas algoritmos padronizados após revisão pública (FIPS 203/204/205, SP 800-208), cita as quebras do Rainbow e do SIKE como motivos pelos quais projetos não verificados não podem ser aceitos e convida a uma proposta de um produto baseado em normas.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; a situação das normas muda, então verifique novamente.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Bernstein, D. J., et al. (2024). KyberSlash. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Chromium Blog (2023). Protecting Chrome Traffic with Hybrid Kyber KEM. <https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html>
- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- Gidney, C., and Ekerå, M. (2021). *Quantum* 5, 433. <https://doi.org/10.22331/q-2021-04-15-433>
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *STOC '96*. <https://doi.org/10.1145/237814.237866>
- IANA. TLS Supported Groups registry. <https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml>
- IETF RFCs: 8446 (TLS 1.3), 8554 (LMS), 8391 (XMSS), 8555 (ACME), 8701 (GREASE), 8784 (IKEv2 PSK mixing), 8879 (certificate compression), 9370 (multiple key exchanges in IKEv2), 9629 (KEMs in CMS), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NCCoE. Migration to Post-Quantum Cryptography project. <https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025); SP 800-56C Rev. 2. <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227> · <https://doi.org/10.6028/NIST.SP.800-56Cr2>
- NIST IR 8545 (2025); IR 8547 initial public draft (2024); CSWP 39 upd1 (2026). <https://doi.org/10.6028/NIST.IR.8545> · <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- NSA. Quantum Key Distribution (QKD) and Quantum Cryptography (QC). <https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/>
- Regev, O. (2009). *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
