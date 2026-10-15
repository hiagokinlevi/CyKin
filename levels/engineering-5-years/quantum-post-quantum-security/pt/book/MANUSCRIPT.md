# Segurança Quântica e Pós-Quântica: Engenharia de Sistemas Resistentes à Computação Quântica

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–50 de 50 têm texto didático escrito; os exercícios EX001–EX100 (dois por capítulo) têm as resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, com saídas verificadas. A revisão independente e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
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
11. [Redes e protocolos](#ch-11)
12. [Sistemas operacionais](#ch-12)
13. [Sistemas de dados](#ch-13)
14. [Engenharia de software](#ch-14)
15. [Fundamentos de segurança](#ch-15)
16. [Engenharia de sistemas](#ch-16)
17. [Fundamentos de controle e realimentação](#ch-17)
18. [Arquitetura de segurança](#ch-18)
19. [Identidade e criptografia](#ch-19)
20. [Segurança quântica e pós-quântica: contexto de engenharia](#ch-20)
21. [Segurança quântica e pós-quântica: requisitos](#ch-21)
22. [Segurança quântica e pós-quântica: modelos de sistema e de dados](#ch-22)
23. [Segurança quântica e pós-quântica: análise de ameaças e de falhas](#ch-23)
24. [Segurança quântica e pós-quântica: métodos I](#ch-24)
25. [Ateliê de projeto I](#ch-25)
26. [Segurança quântica e pós-quântica: alternativas de arquitetura](#ch-26)
27. [Segurança quântica e pós-quântica: projeto de controles](#ch-27)
28. [Segurança quântica e pós-quântica: implementação I](#ch-28)
29. [Segurança quântica e pós-quântica: medição](#ch-29)
30. [Laboratório de verificação I](#ch-30)
31. [Segurança quântica e pós-quântica: implementação II](#ch-31)
32. [Segurança quântica e pós-quântica: confiabilidade](#ch-32)
33. [Segurança quântica e pós-quântica: segurança operacional e resiliência](#ch-33)
34. [Segurança quântica e pós-quântica: integração](#ch-34)
35. [Ateliê de projeto II](#ch-35)
36. [Segurança quântica e pós-quântica: desempenho e escala](#ch-36)
37. [Segurança quântica e pós-quântica: operações](#ch-37)
38. [Segurança quântica e pós-quântica: validação](#ch-38)
39. [Segurança quântica e pós-quântica: manutenibilidade](#ch-39)
40. [Laboratório de verificação II](#ch-40)
41. [Segurança quântica e pós-quântica: otimização de sistemas](#ch-41)
42. [Segurança quântica e pós-quântica: pesquisa aplicada](#ch-42)
43. [Prática na indústria ou no serviço público](#ch-43)
44. [Projeto final de engenharia I](#ch-44)
45. [Revisão independente de projeto](#ch-45)
46. [Projeto final de engenharia II](#ch-46)
47. [Ensaio de falha e recuperação](#ch-47)
48. [Dossiê de evidências](#ch-48)
49. [Trabalho de conclusão de engenharia](#ch-49)
50. [Defesa final](#ch-50)

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

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 50

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 50

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 50

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 50

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 50

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 50

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 50

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 50

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 50

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) acompanhar um handshake do TLS 1.3 e identificar onde acontecem a troca de chaves e a autenticação; (2) explicar como o tamanho dos pacotes, a MTU e a fragmentação interagem com mensagens pós-quânticas maiores; (3) descrever o IKEv2, o SSH e o DNSSEC do ponto de vista da migração; e (4) reconhecer a ossificação dos middleboxes. O capítulo prepara a integração (Capítulo 34) e o desempenho (Capítulo 36).

### 11.1 TLS 1.3

No TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html)), o cliente envia um ClientHello com compartilhamentos de chave para um ou mais grupos; o servidor responde com o seu compartilhamento, e ambos derivam as chaves do segredo compartilhado. Em seguida, o servidor envia, cifrados, a sua cadeia de certificados e uma assinatura CertificateVerify. A troca de chaves protege a confidencialidade contra a gravação; os certificados e as assinaturas fornecem a autenticação no momento da conexão. Grupos híbridos como o X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) mudam apenas a parte do compartilhamento de chave: o compartilhamento do cliente cresce de 32 para 1.216 bytes, o do servidor para 1.120 bytes.

### 11.2 O tamanho e a rede

Um caminho Ethernet normalmente transporta pacotes IP de 1.500 bytes, cerca de 1.460 bytes de carga útil TCP. Um ClientHello com compartilhamento híbrido muitas vezes passa disso e precisa de dois segmentos TCP. O TCP lida com isso de forma transparente, mas alguns middleboxes e servidores inspecionam apenas o primeiro pacote. O Google relatou incompatibilidades desse tipo quando o Chrome passou a oferecer o Kyber híbrido ([Chromium Blog 2023](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)). Sobre UDP (QUIC, DTLS, IKEv2), mensagens maiores levantam problemas de fragmentação e de limite de amplificação que os projetistas de protocolos tratam explicitamente.

Os testes, portanto, cobrem o caminho inteiro, incluindo proxies e balanceadores de carga.

### 11.3 Outros protocolos

As VPNs IKEv2 acrescentam troca de chaves pós-quântica por meio de trocas adicionais (o [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html) define múltiplas trocas de chaves no IKEv2). As implementações de SSH já implantaram métodos híbridos de troca de chaves que combinam um KEM de reticulados com o X25519. O DNSSEC é sobretudo um problema de assinaturas: as assinaturas pós-quânticas são muito maiores do que as assinaturas ECDSA atuais, o que sobrecarrega as respostas UDP.

Cada protocolo precisa do seu próprio plano. A VPN site a site da BPA pode acrescentar uma troca ML-KEM pelo RFC 9370 assim que os dois gateways a suportarem; a administração por SSH pode passar a um método híbrido com uma mudança de configuração em servidores e clientes; o DNSSEC precisa esperar por normas que encaixem assinaturas grandes nas respostas DNS, então permanece no inventário como uma dependência acompanhada.

### 11.4 Ossificação

Quando os middleboxes supõem que os campos de um protocolo nunca mudam, valores novos quebram as conexões. O TLS 1.3 introduziu o GREASE ([RFC 8701](https://www.rfc-editor.org/rfc/rfc8701.html)) — valores reservados aleatórios — para manter as implementações tolerantes. A migração pós-quântica é um teste de ossificação: o protocolo a permite, mas os equipamentos implantados talvez não.

O plano de testes da BPA envia ClientHellos híbridos por todos os dispositivos de inspeção no caminho até os portais dos parceiros antes de ativá-los. Um dispositivo que reinicia a conexão é registrado com a sua versão de firmware, e o fornecedor é chamado a corrigi-lo. Isso transforma a ossificação de uma interrupção surpresa numa lista de itens conhecidos, com responsáveis e datas.

### 11.5 Exemplo resolvido

A equipe do terminal da BPA relata que o portal de uma companhia de navegação falha através do proxy de inspeção antigo depois da ativação de um grupo híbrido. Os traces de pacotes mostram o proxy reiniciando as conexões cujo ClientHello ocupa dois segmentos. Opções: atualizar o firmware do proxy, desviar a inspeção para aquele destino ou desativar temporariamente o grupo híbrido apenas naquele caminho enquanto o fornecedor o corrige — mantendo-o em todos os outros.

A exceção direcionada é a escolha certa, porque a falha do proxy afeta apenas um caminho, enquanto o risco de coleta vale para todo o tráfego. A exceção é registrada com data de expiração e responsável, para que não se torne permanente. Depois de instalado o firmware do fornecedor, o teste do laboratório é refeito antes de o grupo híbrido ser reativado naquele caminho.

### 11.6 Erros comuns e limites

- Supor que a troca de chaves híbrida também migra os certificados.
- Esquecer os limites de tamanho dos protocolos UDP.
- Reverter a PQC globalmente por causa de uma falha local de middlebox.

A troca de chaves híbrida protege o tráfego gravado, mas deixa a autenticação em certificados RSA ou ECDSA, que precisam da sua própria migração. Protocolos UDP como o QUIC e o IKEv2 precisam tratar o tamanho explicitamente, porque não têm a segmentação do TCP. Uma reversão global por causa de um proxy joga fora a proteção de todos os outros caminhos, como mostrou o caso do portal da companhia de navegação; uma exceção com prazo para aquele único caminho mantém todo o resto protegido.

### Exercícios

- **EX021 — Contagem de segmentos.** Um ClientHello tem 540 bytes sem compartilhamentos de chave. Quantos segmentos de 1.460 bytes ele ocupa com um compartilhamento só X25519 (32 B) e com o X25519MLKEM768 (1.216 B), contando ~4 B de sobrecarga por compartilhamento? Rubrica: 3 = 1 e 2 segmentos, com a aritmética.
- **EX022 — Mapa de protocolos.** Para TLS, IKEv2, SSH e DNSSEC, diga se a migração é principalmente de troca de chaves, de assinaturas ou de ambas. Rubrica: 3 = correto, com razões de uma linha.

### Síntese

A troca de chaves híbrida muda o tamanho das mensagens, que redes e middleboxes podem tratar mal; cada protocolo tem a sua própria forma de migração, e o obstáculo muitas vezes é a ossificação, não a criptografia.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 50

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) localizar bibliotecas e configurações criptográficas num sistema operacional; (2) explicar as políticas criptográficas de todo o sistema; (3) entender a inicialização segura e a assinatura de atualizações; e (4) gerenciar a entropia e o armazenamento de chaves. O capítulo parte dos Capítulos 8–9 e prepara o inventário (Capítulo 22) e a manutenibilidade (Capítulo 39).

### 12.1 Onde a criptografia mora

Num servidor Linux, o TLS normalmente vem de uma biblioteca compartilhada (OpenSSL, GnuTLS, NSS, BoringSSL em algumas aplicações), o SSH do OpenSSH, as VPNs do IPsec do kernel mais um daemon IKE em espaço de usuário. As aplicações também podem embutir as próprias bibliotecas — programas Java, Go e Rust muitas vezes o fazem. Um inventário que verifica só a biblioteca do sistema deixa escapar a criptografia ligada estaticamente ou embutida.

Encontrar código embutido exige examinar binários e pacotes de aplicação, não apenas o gerenciador de pacotes. Num binário Go, as informações de build listam os módulos criptográficos compilados; em Java, os provedores de segurança configurados mostram qual biblioteca trata o TLS. Essas verificações pertencem ao script de inventário, para que todos os hosts sejam avaliados da mesma forma.

### 12.2 Políticas de todo o sistema

Algumas distribuições oferecem políticas criptográficas de todo o sistema, que definem os algoritmos padrão para todas as bibliotecas que as respeitam. As políticas são uma alavanca poderosa de agilidade: mudar um perfil pode ativar grupos híbridos ou desativar algoritmos fracos em muitos serviços. O seu limite é a cobertura — aplicações com bibliotecas embutidas as ignoram.

A BPA usa a política para ativar o grupo híbrido, numa única mudança, em todos os serviços que usam a biblioteca do sistema, e depois verifica o handshake de cada serviço para confirmar o efeito. Os serviços que não mostram o grupo híbrido após a mudança são exatamente os que têm bibliotecas embutidas, então a implantação da política funciona também como teste da cobertura do inventário.

### 12.3 Inicialização segura e atualizações

O firmware verifica a assinatura do bootloader, que verifica a do kernel, e assim por diante. Essas assinaturas precisam continuar verificáveis durante toda a vida do dispositivo, que pode passar de uma década. Isso faz das cadeias de inicialização candidatas precoces às assinaturas baseadas em hash (LMS, XMSS, conforme a [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208)), que o CNSA 2.0 também prioriza para a assinatura de software e firmware.

Um dispositivo entregue em 2026 com vida útil de quinze anos ainda estará verificando atualizações em 2041, então a chave de inicialização escolhida agora precisa continuar segura por todo esse período. Trocar a raiz de confiança depois pode exigir acesso físico ou ser impossível, e é por isso que as cadeias de inicialização recebem a primeira prioridade, e não a última.

### 12.4 Entropia e armazenamento de chaves

As chaves precisam de boa aleatoriedade vinda do sistema operacional (`getrandom`), sobretudo no início da inicialização e em máquinas virtuais. As chaves privadas pertencem a armazenamento protegido — HSMs, TPMs ou repositórios de chaves do sistema operacional —, nunca a arquivos legíveis por todos.

Máquinas virtuais clonadas de uma mesma imagem podem começar com estado aleatório idêntico, de modo que chaves geradas na primeira inicialização podem se repetir entre hosts. Esperar que o `getrandom` indique que o pool está pronto e gerar as chaves depois de concluída a inicialização evita isso. Nos servidores do terminal da BPA, as chaves privadas TLS ficam no repositório de chaves apoiado pelo TPM e são auditadas mensalmente quanto a desvios nas permissões de arquivo.

### 12.5 Exemplo resolvido

O inventário de um servidor do terminal da BPA encontra o OpenSSL 3.x como biblioteca do sistema, uma aplicação Java com provedor próprio, um binário Go ligado estaticamente e um daemon IPsec. Ativar o TLS híbrido pela política do sistema afeta apenas o primeiro; os outros dois precisam de mudanças nas aplicações. O plano de migração registra um item de trabalho por provedor criptográfico, não por servidor.

A contagem por provedor dá quatro itens de trabalho para este servidor, com responsáveis diferentes: a equipe de plataforma para o OpenSSL e o IPsec, a equipe da aplicação para o Java e os desenvolvedores do serviço Go, que precisam recompilar com um conjunto de ferramentas mais novo. Um plano contado por servidor teria marcado este host como concluído depois da mudança de política, enquanto dois dos seus quatro provedores continuavam intocados.

### 12.6 Erros comuns e limites

- Supor que uma mudança de política migra o host inteiro.
- Ignorar as assinaturas da cadeia de inicialização porque "não são de rede".
- Guardar chaves em diretórios de configuração.

O exemplo resolvido mostrou uma mudança de política alcançando apenas um de quatro provedores num único host. As assinaturas da cadeia de inicialização importam porque precisam continuar válidas por toda a vida do dispositivo e são difíceis de substituir, então vêm primeiro nas migrações de assinatura. Chaves guardadas em diretórios de configuração são copiadas para backups e imagens, onde podem sobreviver aos sistemas que deveriam proteger.

### Exercícios

- **EX023 — Inventário de provedores.** Liste quatro lugares onde a criptografia pode morar num servidor e como você detectaria cada um. Rubrica: 3 = inclui bibliotecas embutidas/estáticas.
- **EX024 — Cadeia de inicialização.** Explique por que a assinatura de firmware é uma prioridade precoce da PQC. Rubrica: 3 = vida útil do dispositivo e restrição de apenas verificar.

### Síntese

A criptografia mora em muitos provedores num mesmo host; as políticas do sistema ajudam, mas não cobrem o código embutido; as cadeias de inicialização de vida longa precisam de migração precoce; as chaves precisam de armazenamento protegido e boa entropia.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 50

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) classificar os dados pelo tempo de vida da confidencialidade; (2) distinguir a cifragem em repouso, em trânsito e em backups; (3) entender a cifragem em envelope e o encapsulamento de chaves (key wrapping); e (4) identificar onde algoritmos vulneráveis à computação quântica protegem dados armazenados. O capítulo prepara os modelos de sistema e de dados (Capítulo 22).

### 13.1 Tempo de vida da confidencialidade

O insumo principal do risco quântico é por quanto tempo os dados precisam permanecer secretos. Os manifestos de contêineres da BPA importam por semanas; as declarações aduaneiras, por 25 anos; os registros de funcionários, por décadas. Classifique os dados primeiro pelo tempo de vida; a ordem da migração decorre disso.

O tempo de vida é definido pelo negócio e pela lei, não pela TI. Para as declarações aduaneiras, os 25 anos vêm das regras de retenção e de sensibilidade comercial, então o dono dos dados aprova o número. Os manifestos, que perdem valor depois que o navio parte, podem ficar na criptografia atual até a renovação normal, liberando esforço para as classes de vida longa. Registrar a origem de cada tempo de vida facilita responder a contestações posteriores.

### 13.2 Em repouso, em trânsito, em backups

Os dados em massa em repouso costumam ser cifrados com algoritmos simétricos (AES-GCM), que não são seriamente ameaçados por computadores quânticos com chaves de 256 bits. O perigo está em **como as chaves simétricas são protegidas**: se uma chave de dados é encapsulada com RSA ou transmitida por um canal protegido por ECDH que um adversário gravou, os dados herdam essa vulnerabilidade. Backups e arquivos copiados para terceiros ampliam a exposição.

Rastrear cada chave de dados desde a criação até todos os lugares em que é encapsulada ou enviada é a forma de encontrar essas dependências ocultas.

### 13.3 Cifragem em envelope

Os serviços de gestão de chaves em nuvem cifram os dados com uma chave de dados e encapsulam essa chave com uma chave mestra. Se a chave mestra é simétrica e fica dentro do serviço, o risco quântico é baixo; se as chaves são trocadas entre partes usando RSA-OAEP ou ECDH (como em muitos formatos de cifragem de documentos), o encapsulamento é o ponto fraco. KEMs pós-quânticos podem substituir esses encapsulamentos — a norma CMS agora tem um [mecanismo baseado em KEM](https://www.rfc-editor.org/rfc/rfc9629.html) (RFC 9629).

A migração substitui apenas o encapsulamento, então os dados armazenados não precisam ser cifrados de novo.

### 13.4 Banco de dados e enlaces de replicação

A replicação de bancos de dados entre locais muitas vezes roda sobre TLS. Os fluxos de replicação gravados de um banco aduaneiro de 25 anos são um alvo privilegiado de coleta, o que faz dos enlaces de replicação candidatos precoces ao TLS híbrido.

O volume de replicação é grande e constante, o que o torna atraente para um adversário capaz de grampear uma única rota de fibra. Ao contrário do tráfego de navegadores, as duas pontas pertencem à BPA, então o TLS híbrido pode ser ativado assim que as bibliotecas dos dois servidores de banco de dados o suportarem, sem coordenação com parceiros. A mudança é testada verificando o grupo negociado na sessão de replicação e depois acompanhando o atraso da replicação por uma semana, para confirmar que o handshake maior não tem efeito operacional.

### 13.5 Exemplo resolvido

O arquivo aduaneiro da BPA: AES-256-GCM em repouso (aceitável), chaves de dados encapsuladas por um KMS local com chave mestra AES (aceitável), replicação noturna para um local de recuperação de desastres por TLS 1.2 com ECDHE (vulnerável à coleta) e exportações para a agência aduaneira nacional como arquivos cifrados com RSA (vulneráveis). Prioridades: o enlace de replicação e o formato de exportação.

As duas prioridades diferem quanto a quem precisa agir. O enlace de replicação é interno, então a BPA pode passá-lo para TLS híbrido numa única janela de manutenção. O formato de exportação exige que a agência aduaneira aceite um novo formato de arquivo, por exemplo CMS com ML-KEM conforme o RFC 9629, o que significa um plano de testes conjunto e uma data combinada. Começar essa conversa agora importa mais do que qualquer mudança interna.

### 13.6 Erros comuns e limites

- Substituir o AES "por causa da computação quântica" e deixar os encapsulamentos de chave com RSA.
- Ignorar os caminhos de backup e de exportação.
- Não classificar o tempo de vida dos dados antes de priorizar.

O AES-256 já resiste a Grover na prática, então substituí-lo gasta dinheiro onde não há lacuna, enquanto as chaves encapsuladas com RSA deixam a lacuna real aberta. A própria análise do arquivo da BPA encontrou os seus dois caminhos vulneráveis na replicação e nas exportações, não no armazenamento. Classificar primeiro o tempo de vida dos dados evita migrar manifestos de um mês antes dos registros aduaneiros de 25 anos e dá aos donos dos dados um número que eles podem defender na auditoria.

### Exercícios

- **EX025 — Classificar.** Classifique seis conjuntos de dados da BPA pelo tempo de vida da confidencialidade e justifique. Rubrica: 3 = tempos de vida plausíveis e ligados à prioridade.
- **EX026 — Encontrar o encapsulamento fraco.** Num fluxo de cifragem de documentos que usa AES-256 e RSA-OAEP, identifique a etapa vulnerável à computação quântica e um substituto baseado em normas. Rubrica: 3 = o encapsulamento RSA; um KEM (por exemplo, ML-KEM via KEMRecipientInfo do CMS).

### Síntese

O risco quântico para os dados armazenados vem pela troca e pelo encapsulamento de chaves, não pelo AES; classifique os dados pelo tempo de vida e depois corrija os enlaces de replicação, as exportações e os encapsulamentos.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 50

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) gerenciar requisitos, projeto, implementação e testes num projeto de migração; (2) usar controle de versão e revisão de código para mudanças criptográficas; (3) montar uma lista de materiais de software (SBOM) e uma lista de materiais criptográficos (CBOM); e (4) planejar versões escalonadas. O capítulo parte dos Capítulos 4 e 9 e prepara a implementação (Capítulo 28).

### 14.1 Ciclo de vida

Uma migração é um projeto de software: requisitos (quais funções precisam se tornar resistentes à computação quântica, e até quando), projeto (híbrido ou PQC pura, quais bibliotecas), implementação, testes, versão escalonada e manutenção. As mudanças criptográficas têm alto impacto e baixa visibilidade: se estiverem erradas, falham em silêncio ou de forma catastrófica.

A falha silenciosa é a mais perigosa das duas: um serviço que volta discretamente à troca de chaves clássica parece saudável enquanto a gravação continua a expor o seu tráfego. Por isso, os requisitos da BPA declaram resultados mensuráveis, como o grupo negociado registrado por sessão, para que os testes possam mostrar que a mudança realmente fez efeito.

### 14.2 Revisão

Toda mudança criptográfica passa pela revisão de alguém com conhecimento de criptografia, além de testes de interoperabilidade. As listas de verificação perguntam: os identificadores de algoritmo vêm da política? Os comprimentos são validados? As comparações são em tempo constante? A versão da biblioteca está fixada e tem suporte?

A BPA mantém um pequeno grupo de revisores que concluíram o treinamento em criptografia, e toda mudança que toca as interfaces `Signer` ou KEM exige um deles. A lista de verificação fica guardada com o código, e cada item corresponde, quando possível, a um teste automatizado, por exemplo, um teste que falha quando um comprimento de chave é aceito sem validação. Os revisores então dedicam o seu tempo às questões de projeto que os testes não conseguem responder.

### 14.3 SBOM e CBOM

Um SBOM lista componentes e versões. Um CBOM estende isso aos ativos criptográficos: algoritmos, conjuntos de parâmetros, comprimentos de chave, protocolos, certificados e onde as chaves ficam. Formatos como o CycloneDX suportam campos de CBOM. Um CBOM é a base para responder "onde usamos RSA?" em minutos, e não em meses.

A BPA gera o CBOM no pipeline de build, então cada versão leva um inventário atualizado. Uma consulta por RSA em todos os CBOMs, filtrada para chaves com tempo de vida acima de dez anos, produziu os primeiros itens de trabalho da migração de assinaturas.

### 14.4 Versões escalonadas

Use feature flags para as escolhas de algoritmo, implantações canário com taxas de falha medidas (Capítulo 37) e planos de reversão. Mantenha disponíveis os algoritmos antigos e os novos durante a transição.

Uma flag permite à equipe desligar o grupo híbrido para um caminho em minutos, como no caso do portal da companhia de navegação, sem reimplantar código. O tamanho do passo do canário começa pequeno, como 1% do tráfego, e só cresce depois que o limite de falhas dado pela regra de três cai abaixo do orçamento combinado. Os dados de cada passo são guardados, para que um incidente posterior possa ser comparado com a linha de base da implantação.

### 14.5 Exemplo resolvido

A equipe do portal da BPA acrescenta o TLS híbrido atrás de uma flag, executa testes de interoperabilidade contra os 50 principais clientes dos parceiros, implanta em 1% do tráfego, monitora as falhas e promove em passos. O CBOM é atualizado automaticamente a partir dos metadados do build, para que o inventário fique em dia.

Escolher os 50 principais clientes dos parceiros cobre a maior parte do tráfego do portal, de modo que uma falha ali apareceria depressa no canário. Cada passo de promoção exige um número mínimo de conexões sem falha, que a equipe calcula antes da implantação. A atualização automática do CBOM permitiu que o escritório de segurança relatasse a mudança ao conselho na mesma semana em que ela atingiu todo o tráfego.

### 14.6 Erros comuns e limites

- Mudanças criptográficas incorporadas sem revisão especializada.
- CBOMs montados à mão uma vez e nunca atualizados.
- Versões "big bang" sem flags.

Incorporações sem revisão já levaram código Kyber da época dos rascunhos para a produção em outras organizações; a regra da BPA de que mudanças nas interfaces exigem um revisor treinado impede isso. CBOMs feitos à mão ficam desatualizados em um ciclo de versão, então o build os gera. Versões "big bang" eliminam a chance de detectar as falhas de middlebox que os canários encontram com 1% do tráfego e tornam a reversão uma escolha de tudo ou nada.

### Nota de engenharia

Trate o CBOM como um artefato vivo, de propriedade de uma equipe nomeada, gerado a partir dos pipelines de build, da gestão de configuração e da telemetria, e não de planilhas. Cada versão deve comparar o seu CBOM com o anterior: uma nova dependência de RSA introduzida por uma atualização de biblioteca é uma regressão a detectar na revisão, exatamente como um teste que falha. As equipes que ligam essa comparação à integração contínua descobrem acréscimos vulneráveis à computação quântica em dias, e não na próxima auditoria anual, e ainda ganham uma lista precisa para questionários de fornecedores e reguladores.

### Exercícios

- **EX027 — Lista de revisão.** Escreva uma lista de verificação de dez itens para revisar uma mudança de PQC. Rubrica: 3 = cobre identificadores, validação, tempo constante, versões, testes, reversão.
- **EX028 — Campos do CBOM.** Liste os campos mínimos de uma entrada de CBOM para um endpoint TLS. Rubrica: 3 = algoritmo, conjunto de parâmetros, protocolo, localização da chave, responsável, detalhes do certificado.

### Síntese

Trate a migração como engenharia de software: mudanças revisadas, flags, canários, reversão e um CBOM mantido automaticamente.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 50

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) aplicar confidencialidade, integridade e disponibilidade à migração criptográfica; (2) explicar os níveis de segurança e as cinco categorias de PQC do NIST; (3) distinguir modelos de ataque — gravação passiva, intermediário ativo (man-in-the-middle) e falsificação; e (4) entender a defesa em profundidade. O capítulo prepara a arquitetura de segurança (Capítulo 18).

### 15.1 A tríade CID na migração

A confidencialidade é ameaçada pelas trocas de chaves gravadas; a integridade e a autenticidade, pela futura falsificação de assinaturas em documentos e firmware de vida longa; a disponibilidade, pela própria migração — mensagens grandes demais, clientes incompatíveis, certificados expirados. Um plano que melhora a confidencialidade, mas provoca interrupções, falhou na disponibilidade.

O plano da BPA lista, portanto, para cada mudança, qual propriedade ela melhora e qual põe em risco. O TLS híbrido no portal melhora a confidencialidade e arrisca a disponibilidade por causa de handshakes maiores; o ML-DSA nos conhecimentos de embarque melhora a integridade de longo prazo e arrisca a disponibilidade para parceiros cujo software ainda não consegue verificá-lo. Cada risco recebe uma mitigação, como um canário ou um período de assinatura dupla.

### 15.2 Categorias de segurança

O NIST definiu cinco categorias de segurança pós-quântica por comparação com o custo de quebrar primitivas simétricas: a categoria 1 é pelo menos tão difícil quanto a busca de chave no AES-128, a categoria 3 quanto no AES-192, a categoria 5 quanto no AES-256; as categorias 2 e 4 se comparam com colisões do SHA-256 e do SHA-384. O ML-KEM-512/768/1024 visa as categorias 1/3/5 ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)). O CNSA 2.0 exige os conjuntos de categoria 5 (ML-KEM-1024, ML-DSA-87) para sistemas de segurança nacional.

A BPA não opera sistemas de segurança nacional, então a categoria 3 é o seu padrão, com a categoria 5 apenas onde os tempos de vida dos dados são os mais longos. Os bytes extras dos conjuntos maiores só são pagos onde compram alguma coisa.

### 15.3 Modelos de ataque

**Gravação passiva agora, decifração depois** ameaça a confidencialidade de tudo o que é protegido hoje por uma troca de chaves vulnerável. **Ataques ativos com um computador quântico** — personificar um servidor falsificando assinaturas — exigem que o CRQC exista no momento do ataque, então a migração das assinaturas é menos urgente para a autenticação de vida curta, mas urgente para as raízes de confiança de vida longa. **A falsificação de assinaturas arquivadas** ameaça documentos cujas assinaturas precisam continuar significativas por anos.

Associar cada sistema da BPA a esses modelos define as prioridades: a replicação aduaneira cai no primeiro, a autenticação TLS dos parceiros no segundo e os conhecimentos de embarque no terceiro.

### 15.4 Defesa em profundidade

A troca de chaves híbrida é defesa em profundidade entre pressupostos: o atacante precisa quebrar tanto o componente tradicional quanto o pós-quântico ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)). A agilidade é defesa em profundidade ao longo do tempo: se um algoritmo enfraquecer, substitua-o depressa.

As duas formas trabalham juntas. A troca de chaves híbrida protege a BPA se for encontrada uma falha no ML-KEM, porque o X25519 continua resistindo a atacantes clássicos. A agilidade protege a BPA se os dois enfraquecerem com o tempo, já que o arquivo de política pode trocar de algoritmo sem mudanças de código. Nenhuma das duas ajuda se as chaves forem guardadas sem cuidado, então os controles de armazenamento continuam sendo uma camada à parte.

### 15.5 Exemplo resolvido

Os conhecimentos de embarque da BPA são assinados com ECDSA e precisam ser verificáveis por 12 anos. Um CRQC dentro de 12 anos permitiria falsificar um conhecimento com data no passado, a menos que o documento leve uma assinatura pós-quântica ou uma cadeia de carimbos de tempo confiável que também tenha sido migrada. Prioridade: alta — integridade de documentos jurídicos por longos períodos.

Um carimbo de tempo confiável prova que o documento existia antes de uma certa data, então nem uma falsificação posterior pode ser antedatada para antes do carimbo. A escolha da BPA é recarimbar os conhecimentos arquivados com uma autoridade de carimbo de tempo pós-quântica e assinar os novos conhecimentos com ML-DSA-65, cujas assinaturas de 3.309 bytes cabem facilmente nos arquivos dos documentos.

### 15.6 Erros comuns e limites

- Tratar a PQC como uma questão só de confidencialidade.
- Escolher a categoria 5 em toda parte sem considerar tamanho e desempenho.
- Esquecer a disponibilidade.

Tratar a PQC apenas como um problema de confidencialidade deixa os conhecimentos de embarque e o firmware abertos a falsificações futuras. A categoria 5 em toda parte acrescenta bytes e processamento, por exemplo a chave de 1.568 bytes do ML-KEM-1024 contra os 1.184 do 768, sem uma necessidade correspondente para a maior parte dos dados da BPA. Falhas de disponibilidade, como um middlebox que rejeita handshakes grandes, podem desfazer a credibilidade de todo o programa. Um plano que nomeia de antemão os seus riscos de disponibilidade e as mitigações mantém o apoio das equipes de operação quando acontece o primeiro incidente.

### Exercícios

- **EX029 — Escolha de categoria.** Recomende uma categoria para o portal da BPA e para um enlace com um parceiro de segurança nacional; justifique. Rubrica: 3 = categoria 3 (ou 1) para o portal, com raciocínio; categoria 5, conforme o CNSA 2.0, para o parceiro.
- **EX030 — Modelos de ataque.** Para o tráfego de VPN, as assinaturas de firmware e os conhecimentos de embarque, diga qual modelo de ataque domina. Rubrica: 3 = gravação; falsificação de raízes de vida longa; falsificação de assinaturas arquivadas.

### Síntese

A migração toca confidencialidade, integridade e disponibilidade; as categorias ligam a força da PQC a referências simétricas; a urgência difere conforme o modelo de ataque; os híbridos e a agilidade dão profundidade.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 50

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) aplicar um ciclo de vida de sistemas a uma migração de vários anos; (2) gerenciar interfaces e dependências entre organizações; (3) usar estudos de compromisso (trade studies); e (4) planejar a verificação e a validação desde o início. O capítulo parte do Capítulo 14 e prepara os requisitos (Capítulo 21).

### 16.1 Visão de ciclo de vida

Uma migração de todo o porto abrange concepção (por quê e o quê), requisitos, arquitetura, implementação, integração, verificação, validação, operação e desativação. Normas de ciclo de vida como a ISO/IEC/IEEE 15288 descrevem esses processos. A migração criptográfica difere da maioria das mudanças de sistema porque toca todas as interfaces ao mesmo tempo e porque parceiros de fora da organização precisam mudar no mesmo passo.

Para a BPA, a desativação é uma fase real: as chaves e os certificados RSA precisam ser retirados e os algoritmos antigos desativados assim que todos os parceiros tiverem migrado; caso contrário, os caminhos de rebaixamento ficam abertos indefinidamente. Planejar a desativação desde o início, com uma data-alvo por interface, impede que o programa termine com os algoritmos antigos e novos ativados permanentemente.

### 16.2 Interfaces e dependências

A BPA depende das companhias de navegação (pares de VPN), da agência aduaneira (formatos de exportação), dos fornecedores (equipamentos, HSMs, firmware dos guindastes) e dos fabricantes de navegadores (clientes TLS). Um documento de controle de interfaces lista, por interface, os algoritmos atuais, o alvo, quem precisa mudar e até quando. As dependências explicam os cronogramas melhor do que as estimativas de esforço.

Para a exportação aduaneira, o documento de controle registra RSA-OAEP hoje, CMS com ML-KEM-768 como alvo, a agência aduaneira como a parte que precisa mudar primeiro e uma data combinada numa carta conjunta. Uma dependência como essa define o cronograma, independentemente de quão depressa os desenvolvedores da própria BPA terminem a sua parte.

### 16.3 Estudos de compromisso

Um estudo de compromisso compara opções segundo critérios ponderados. Para a VPN da BPA: (a) IKEv2 híbrido com ML-KEM agora, (b) esperar pelo suporte nativo do fornecedor, (c) acrescentar uma camada de chave pré-compartilhada como mitigação provisória. Critérios: ganho de segurança, risco de disponibilidade, custo, prontidão dos parceiros, conformidade com as normas. Os pesos vêm dos requisitos, não de preferências.

Fixar os pesos antes da pontuação impede que uma equipe os ajuste para favorecer a opção que já prefere. A equipe da BPA publica os pesos na revisão de requisitos, pontua cada opção de forma independente e depois verifica se uma mudança moderada em algum peso mudaria a vencedora. Se mudar, o resultado é registrado como apertado, e a decisão cita explicitamente o fator decisivo.

### 16.4 Planejamento de V&V

A verificação pergunta "construímos certo?" (requisitos atendidos); a validação pergunta "construímos a coisa certa?" (necessidades das partes interessadas atendidas). Planeje as duas antes da implementação: por exemplo, verificar que a VPN negocia ML-KEM-768 ou mais forte em todos os túneis e validar que as operações das companhias de navegação continuam sem atraso.

A verificação, aqui, é uma consulta de logs: o algoritmo negociado de cada túnel é registrado, e qualquer túnel sem ML-KEM-768 ou mais forte reprova na verificação. A validação precisa da equipe de operações das companhias de navegação, que confirma que os tempos de troca de documentos e de estabelecimento das conexões não mudaram depois da virada. Escrever as duas verificações antes da implementação garante que o registro necessário para a verificação seja construído desde o início.

### 16.5 Exemplo resolvido

O estudo de compromisso dá à opção (a) a maior nota em segurança e normas, à (b) a maior em disponibilidade e à (c) o papel de solução provisória barata. Decisão: (c) imediatamente para os dois parceiros de maior valor, (a) num piloto com um parceiro, (b) para os demais quando os fornecedores entregarem — documentado com datas de revisão.

Cada opção tem uma data de revisão para que a decisão não congele: o piloto é revisto após três meses para decidir se (a) pode se estender a mais parceiros, e as chaves pré-compartilhadas provisórias são rotacionadas e verificadas ao mesmo tempo. Anotar essas datas transforma um meio-termo num plano que avança.

### 16.6 Erros comuns e limites

- Planejar a migração como um projeto interno quando os parceiros também precisam mudar.
- Estudos de compromisso com pesos escolhidos depois da pontuação.
- V&V inventada depois da implantação.

Os parceiros são donos de metade de cada interface externa, então um plano só com tarefas internas vai travar na primeira VPN ou no primeiro formato de exportação. Pesos escolhidos depois da pontuação fazem do estudo de compromisso um argumento a favor de uma decisão já tomada. A V&V inventada depois da implantação costuma não ter os logs necessários para verificar qualquer coisa, como mostrou a verificação do algoritmo dos túneis.

### Nota de engenharia

A engenharia de sistemas também pergunta quando parar. Uma migração tem um critério de saída por interface — por exemplo, "negociação só clássica abaixo de 0,5% dos túneis por 90 dias e confirmação do parceiro recebida" —, após o qual o caminho antigo é removido, em vez de ficar como alternativa permanente. Sem critérios de saída, as configurações de transição se tornam permanentes, e a organização carrega tanto o risco antigo quanto a nova complexidade. Registre os critérios de saída no documento de controle de interfaces, para que as revisões de progresso possam encerrar os pacotes de trabalho de forma objetiva.

### Exercícios

- **EX031 — Lista de interfaces.** Esboce cinco linhas do documento de controle de interfaces da BPA. Rubrica: 3 = atual, alvo, responsável e data para cada uma.
- **EX032 — Estudo de compromisso.** Pontue as três opções de VPN com pesos explícitos. Rubrica: 3 = pesos justificados antes da pontuação; sensibilidade registrada.

### Síntese

A migração é um problema de sistemas dominado por interfaces e parceiros; estudos de compromisso com pesos prévios e um planejamento precoce de V&V mantêm as decisões defensáveis.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 50

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) modelar um programa de migração como um laço de realimentação; (2) escolher indicadores antecedentes e consequentes; (3) reconhecer a instabilidade causada por correção excessiva; e (4) aplicar ideias de controle aos portões de implantação. O capítulo prepara as operações (Capítulo 37) e a otimização (Capítulo 41).

### 17.1 Programas como laços

Um laço de realimentação mede a saída, compara-a com um valor de referência e ajusta a entrada. Na migração, a "saída" é a parcela protegida do tráfego e dos ativos; o valor de referência é a trajetória-alvo; a entrada é o esforço de engenharia e o ritmo de implantação. Sem medição não há controle — só esperança.

O valor de referência da BPA é uma trajetória, por exemplo 50% das trocas de chaves externas híbridas no fim do primeiro ano e 90% no fim do segundo. A comparação mensal entre a parcela medida e a planejada orienta a alocação de esforço do mês seguinte.

### 17.2 Indicadores

Indicadores **consequentes** mostram resultados: porcentagem de trocas de chaves negociadas com grupos híbridos, parcela de certificados com assinaturas pós-quânticas, parcela de ativos desconhecidos. Indicadores **antecedentes** preveem resultados: fornecedores com roteiros de PQC assumidos, cobertura do CBOM, prontidão do ambiente de testes. Um painel precisa de ambos.

Os indicadores consequentes confirmam o progresso, mas chegam tarde demais para mudar o rumo; os antecedentes avisam cedo. Se a cobertura do CBOM estacionar em 71%, o número da parcela protegida vai parecer bom enquanto os ativos desconhecidos continuam sem medição. Associar cada indicador consequente ao antecedente que o move permite aos gestores agir antes de o resultado aparecer. Cada indicador tem uma definição e uma fonte de dados registradas, para que duas equipes não possam relatá-lo de formas diferentes.

### 17.3 Estabilidade

A correção excessiva causa oscilação: ativar grupos híbridos em toda parte depois de uma boa semana, reverter em toda parte depois de um dia ruim. A teoria de controle sugere amortecimento — passos menores, esperas para a medição e histerese (limiares diferentes para promover e para reverter).

Na prática, a BPA promove um passo de implantação somente após uma semana de dados limpos e reverte somente se o limite de falhas exceder o dobro do orçamento. A distância entre esses limiares é a histerese: um único dia ruim dentro da faixa provoca uma investigação, não uma reversão. As falhas também são delimitadas, então um problema num caminho é tratado apenas naquele caminho.

### 17.4 Portões de implantação como controladores

Um portão de canário é um controlador simples: aumente a exposição quando o limite superior de confiança da taxa de falhas estiver abaixo do orçamento, mantenha caso contrário e reverta só quando um limiar mais alto for ultrapassado. O Capítulo 37 implementa um.

Os limiares vêm do orçamento de falhas. Com um orçamento de 10^-5 e a regra de três, um passo precisa de cerca de 300.000 conexões limpas antes da promoção. Um limiar de reversão mais alto que o de promoção impede que o portão alterne para lá e para cá quando a taxa medida oscila perto do orçamento. Registrar cada decisão com os seus dados permite aos revisores conferir que o controlador se comportou como projetado.

### 17.5 Exemplo resolvido

O painel da BPA mostra negociação híbrida em 62% do tráfego do portal (consequente) e cobertura do CBOM em 71% dos ativos (antecedente). Os ativos desconhecidos somam 18%. A ação de controle: aumentar o esforço de inventário sobre os ativos desconhecidos em vez de empurrar mais o tráfego do portal, porque o risco maior está onde nada é medido.

Os 18% de ativos desconhecidos podem conter sistemas com dados de 25 anos que nenhuma implantação alcança, então encontrá-los reduz mais risco do que levar o tráfego do portal de 62% para 80%. O plano do mês seguinte designa dois engenheiros para o inventário e fixa a meta de reduzir à metade a parcela desconhecida.

### 17.6 Erros comuns e limites

- Painéis só com indicadores consequentes.
- Reverter globalmente por causa de falhas locais (correção excessiva).
- Medir os algoritmos configurados em vez dos negociados.

Um painel só com porcentagens de negociação não consegue avisar que o inventário estacionou. As reversões globais descartam o progresso feito em todos os caminhos saudáveis. Medir os algoritmos configurados conta servidores onde o híbrido está ativado, mas nunca é negociado, por exemplo porque os clientes não o oferecem; a BPA lê o grupo negociado nos logs de sessão, que é o único número que reflete a proteção real do tráfego, e o compara todo mês com a parcela configurada.

### Nota de engenharia

O atraso de medição importa neste laço. A telemetria passiva pode ficar um dia atrás das mudanças de configuração; as mudanças do lado dos parceiros podem atrasar semanas. Um controlador que reage mais depressa do que os seus sensores oscila, então o ritmo de implantação precisa ser mais lento do que a medição relevante mais lenta. Na prática, a BPA define decisões semanais de promoção para os serviços internos e revisões mensais para as interfaces com parceiros, e registra o atraso de medição ao lado de cada indicador, para que ninguém confunda o retrato de ontem com o estado de hoje.

### Exercícios

- **EX033 — Indicadores.** Proponha três indicadores antecedentes e três consequentes para a BPA. Rubrica: 3 = mensuráveis, com responsável nomeado.
- **EX034 — Histerese.** Projete limiares de promover/manter/reverter para a implantação de um grupo híbrido. Rubrica: 3 = limiares distintos, com justificativa.

### Síntese

Uma migração é um processo controlado: meça os resultados negociados, combine indicadores antecedentes e consequentes, amorteça as correções e use portões com histerese.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 50

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) identificar fronteiras de confiança e onde a criptografia as impõe; (2) projetar uma arquitetura criptográfica com zonas e serviços; (3) centralizar a gestão de chaves; e (4) documentar a agilidade criptográfica como propriedade da arquitetura. O capítulo parte dos Capítulos 15–17 e prepara o núcleo de PQC.

### 18.1 Fronteiras de confiança

Desenhe cada fronteira em que os dados passam de um domínio de confiança para outro: da internet para o portal, da BPA para uma companhia de navegação, da rede do terminal para a rede dos guindastes, da BPA para a agência aduaneira. Em cada fronteira, liste as funções criptográficas: estabelecimento de chaves, autenticação, integridade, confidencialidade em repouso. Essa lista é o esqueleto da arquitetura.

Na fronteira da rede dos guindastes, por exemplo, a lista contém a verificação de assinaturas de firmware e a VPN para o serviço de manutenção do fornecedor. Anotá-la revelou que o enlace do fornecedor usava uma chave pré-compartilhada e autenticação RSA, que o inventário original não havia encontrado porque o enlace era gerenciado pelo fornecedor. A lista de cada fronteira se torna um conjunto de linhas no documento de controle de interfaces.

### 18.2 Serviços criptográficos

Centralize onde for possível: uma camada de terminação TLS, uma PKI com uma AC apoiada em HSM, um serviço de gestão de chaves, um serviço de assinatura para firmware e documentos. A centralização transforma a migração de um serviço na migração para muitos consumidores. A criptografia descentralizada — cada aplicação com a sua biblioteca e as suas chaves — multiplica o trabalho.

O proxy de borda da BPA termina o TLS de todos os seus serviços públicos, então ativar o grupo híbrido ali protegeu cada um deles com uma única mudança. Já os serviços internos que embutem cada um a sua biblioteca exigem um projeto separado por serviço. A direção da arquitetura é, portanto, encaminhar os serviços novos pelos componentes compartilhados e registrar qualquer exceção com o motivo e uma data de expiração.

### 18.3 A agilidade criptográfica como arquitetura

O white paper do NIST sobre agilidade criptográfica ([CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1)) descreve a agilidade como a capacidade de substituir algoritmos em protocolos, aplicações, software, hardware e infraestrutura preservando a segurança e as operações. Em termos de arquitetura, isso significa: escolhas de algoritmo na política, não no código; protocolos que negociam algoritmos com segurança; ciclos de vida de certificados e chaves curtos o bastante para a rotação; e um inventário que mostra onde tudo está.

Cada elemento pode ser testado: uma mudança de política deve trocar os algoritmos num ambiente de testes sem mudança de código; o tempo de vida dos certificados deve ser curto o bastante para substituí-los todos dentro de uma janela planejada.

### 18.4 Onde aplicar os híbridos

Decida onde os híbridos se aplicam: primeiro a troca de chaves em todas as fronteiras externas de TLS e VPN; depois as assinaturas das raízes de vida longa e do firmware; o tráfego interno entre serviços conforme o tempo de vida dos dados. Registre a decisão e a sua data de revisão.

A ordem segue a desigualdade de Mosca: a troca de chaves externa primeiro, porque o tráfego gravado está exposto agora; depois as assinaturas de vida longa, porque as raízes e o firmware precisam durar mais que a chegada de um CRQC; e o tráfego interno por último, se carregar dados de vida curta. Um serviço que transporta registros aduaneiros sobe na lista mesmo sendo interno. A data de revisão obriga a um novo olhar à medida que as bibliotecas e os parceiros ficam prontos.

### 18.5 Exemplo resolvido

A arquitetura-alvo da BPA: TLS híbrido no proxy de borda e nas VPNs com parceiros; um novo HSM com suporte a PQC para a AC; firmware dos guindastes assinado com LMS por um serviço central de assinatura com gestão de estado; ML-DSA com carimbo de tempo para os conhecimentos de embarque; seleção de algoritmos guiada por política nos serviços internos.

Cada elemento corresponde a uma decisão anterior: o TLS híbrido vem da implantação no portal, o HSM do plano da AC, o LMS da restrição de 32 KB do controlador do guindaste e o ML-DSA com carimbo de tempo da análise dos conhecimentos de embarque. Escrever a arquitetura assim mostra aos revisores de onde veio cada escolha e qual decisão anterior revisitar se uma restrição mudar.

### 18.6 Erros comuns e limites

- Diagramas de arquitetura sem nenhuma função criptográfica marcada.
- Cada equipe escolhendo algoritmos de forma independente.
- Agilidade alegada, mas com chaves de 20 anos de vida.

Sem as funções criptográficas nos diagramas, a VPN do fornecedor e o formato de exportação ficam invisíveis até um incidente. Escolhas independentes produzem várias bibliotecas e conjuntos de parâmetros pós-quânticos, que precisam ser mantidos um a um. Um tempo de vida de chave de 20 anos significa que a agilidade só existe no papel, porque a rotação levaria mais tempo do que o horizonte da ameaça permite. A BPA limita o tempo de vida das novas chaves para que todas possam ser substituídas em até dois anos.

### Nota de engenharia

As fronteiras de confiança também existem no tempo. Um documento assinado hoje atravessa uma fronteira rumo ao futuro quando um tribunal ou um parceiro o verifica anos depois, então a arquitetura deve mostrar os serviços de validação de longo prazo — carimbo de tempo, reassinatura de arquivos, registros de evidência — como componentes com a sua própria criptografia a migrar. Desenhá-los explicitamente evita o descuido comum em que todos os caminhos online são migrados enquanto as evidências arquivadas continuam protegidas por algoritmos que um adversário futuro poderia falsificar.

### Exercícios

- **EX035 — Tabela de fronteiras.** Crie uma tabela de fronteiras para quatro fronteiras da BPA, com funções e algoritmos atuais. Rubrica: 3 = completa e precisa.
- **EX036 — Centralizar.** Argumente a favor ou contra centralizar a terminação TLS para fins de migração. Rubrica: 3 = benefício de agilidade e risco de ponto único de falha ponderados.

### Síntese

A arquitetura associa as fronteiras de confiança às funções criptográficas, centraliza os serviços para tornar a migração tratável e codifica a agilidade na política, nos protocolos, nos ciclos de vida e no inventário.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 50

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) explicar assinaturas digitais, certificados e hierarquias de PKI; (2) entender as assinaturas baseadas em hash de uso único e de muitos usos; (3) comparar ML-DSA, SLH-DSA, LMS/XMSS e o futuro FN-DSA; e (4) planejar a migração da PKI, incluindo raízes e assinaturas de vida longa. O capítulo fecha a etapa de fundamentos.

### 19.1 Assinaturas e PKI

Uma assinatura liga uma mensagem a uma chave; um certificado liga uma chave a uma identidade e é assinado por uma autoridade certificadora (AC); uma cadeia leva a uma raiz em que as partes confiantes confiam. As raízes muitas vezes vivem mais de 20 anos, então uma chave raiz que um futuro CRQC pudesse falsificar compromete todos os certificados abaixo dela.

Os certificados finais duram cerca de um ano e são substituídos rotineiramente, então o seu algoritmo pode mudar na próxima renovação. A raiz é diferente: as partes confiantes precisam receber uma nova raiz e confiar nela antes que qualquer certificado emitido por ela seja aceito, o que leva anos para parceiros e dispositivos. É por isso que a BPA cria primeiro a sua raiz pós-quântica.

### 19.2 Assinaturas baseadas em hash a partir dos princípios

Uma assinatura de uso único de Lamport publica os hashes de dois segredos aleatórios por bit do resumo da mensagem e revela um segredo por bit ao assinar. A segurança precisa apenas de um hash de mão única. Usar uma chave duas vezes revela os dois segredos em muitas posições, reduzindo bruscamente o trabalho do falsificador; mais alguns usos tornam a falsificação prática. As árvores de Merkle combinam muitas chaves de uso único sob uma só chave pública; o LMS e o XMSS ([RFC 8554](https://www.rfc-editor.org/rfc/rfc8554.html), [RFC 8391](https://www.rfc-editor.org/rfc/rfc8391.html), [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208)) fazem isso com estado; o SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) evita o estado usando uma hiperárvore com assinaturas de poucos usos nas folhas, ao custo de assinaturas maiores.

### 19.3 Atividade prática — Laboratório L

```python
# Lab L (ch 19): Lamport one-time signatures from SHA-256 - the idea under SLH-DSA, LMS and XMSS.
import hashlib, secrets
H = lambda b: hashlib.sha256(b).digest()
def keygen(bits=256):
    sk = [(secrets.token_bytes(32), secrets.token_bytes(32)) for _ in range(bits)]
    pk = [(H(a), H(b)) for a, b in sk]
    return sk, pk
def bits_of(msg):
    d = int.from_bytes(H(msg), "big"); return [(d >> (255 - i)) & 1 for i in range(256)]
def sign(sk, msg): return [sk[i][b] for i, b in enumerate(bits_of(msg))]
def verify(pk, msg, sig): return all(H(s) == pk[i][b] for i, (s, b) in enumerate(zip(sig, bits_of(msg))))
sk, pk = keygen()
s1 = sign(sk, b"firmware v1.0")
print("valid signature verifies:", verify(pk, b"firmware v1.0", s1))
print("tampered message rejected:", not verify(pk, b"firmware v1.1", s1))
s2 = sign(sk, b"firmware v1.1")          # KEY REUSE: never do this
revealed = sum(1 for i in range(256) if bits_of(b"firmware v1.0")[i] != bits_of(b"firmware v1.1")[i])
print(f"after one reuse, both secrets revealed at {revealed}/256 positions -> forging needs ~2^{256 - revealed} hashes, not 2^256")
print("signature size:", 256 * 32, "bytes; public key:", 2 * 256 * 32, "bytes")
```

Saída esperada:

```text
valid signature verifies: True
tampered message rejected: True
after one reuse, both secrets revealed at 118/256 positions -> forging needs ~2^138 hashes, not 2^256
signature size: 8192 bytes; public key: 16384 bytes
```

A saída mostra tanto a força do esquema quanto a sua fragilidade. Uma assinatura válida é verificada e uma mensagem alterada falha, usando apenas o SHA-256. Depois de uma reutilização, os dois resumos diferem em 118 posições, onde os dois segredos agora são públicos; um falsificador precisa de uma mensagem cujo resumo coincida nas 138 posições restantes, cerca de 2^138 hashes. Cada nova reutilização reduz à metade, em média, as posições desconhecidas, então, depois de três assinaturas, restam cerca de 64, ao alcance de grandes computações. Os tamanhos, 8 KB por assinatura, explicam por que os esquemas práticos comprimem as chaves de Lamport com cadeias de Winternitz e árvores de Merkle.

### 19.4 As opções padronizadas

| Esquema | Base | Chave pública / assinatura (bytes) | Notas |
|---|---|---|---|
| ML-DSA-44/65/87 ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) | Reticulados modulares | 1.312/2.420 · 1.952/3.309 · 2.592/4.627 | Uso geral |
| SLH-DSA (FIPS 205) | Hashes, sem estado | 32–64 / 7.856–49.856 | Conservador, grande |
| LMS, XMSS (SP 800-208) | Hashes, com estado | Pequena / ~1–3 kB típico | O estado nunca pode se repetir; firmware |
| FN-DSA (Falcon) | Reticulados NTRU | ~900 / ~666 no nível 1 | Norma (FIPS 206) em desenvolvimento |

Para a BPA, a tabela aponta o ML-DSA para a assinatura geral, o LMS para o firmware onde o estado pode ser gerenciado e o SLH-DSA onde o tamanho da assinatura importa menos do que pressupostos conservadores. O FN-DSA fica anotado para uso futuro, quando a FIPS 206 for final, já que as suas assinaturas pequenas se adequam a enlaces restritos. A escolha para cada uso é registrada com os números de tamanho da tabela, para que revisores posteriores possam conferi-los.

### 19.5 Exemplo resolvido

O plano de PKI da BPA: uma nova raiz ML-DSA-87 (ou uma raiz composta tradicional+PQC, conforme o suporte das partes confiantes) criada agora e distribuída; intermediárias migradas no próximo ciclo de certificados; LMS para a assinatura de firmware, com estado protegido por HSM; SLH-DSA considerado para uma raiz offline raramente usada, por causa do seu pressuposto conservador.

Distribuir a nova raiz leva tempo, então ela é criada antes que as intermediárias precisem dela; uma raiz criada no primeiro ano pode estar nos repositórios de confiança dos parceiros quando os certificados finais migrarem. A raiz offline assina raramente, então as assinaturas grandes do SLH-DSA pouco importam, enquanto a sua dependência exclusiva de hashes dá garantia caso os esquemas de reticulados sejam enfraquecidos.

### 19.6 Erros comuns e limites

- Reutilizar chaves de uso único ou com estado (o retrocesso do estado após a restauração de um backup é uma falha clássica).
- Migrar os certificados finais e deixar uma raiz de vida longa vulnerável.
- Citar o FN-DSA como norma final.

Restaurar um servidor de assinatura a partir de um backup pode reiniciar o contador do LMS, de modo que a mesma chave de uso único assina duas mensagens, exatamente a reutilização que o Laboratório L mostra; o HSM da BPA guarda o estado e se recusa a retroceder. Um certificado final pós-quântico sob uma raiz RSA continua falhando se a raiz puder ser falsificada. O FN-DSA deve ser planejado, não implantado, até que a sua norma seja final.

### Exercícios

- **EX037 — Reutilização no Lamport.** Explique, a partir do Laboratório L, por que assinar duas mensagens com uma chave permite a falsificação. Rubrica: 3 = argumento dos segredos revelados correto.
- **EX038 — Seleção de esquema.** Escolha um esquema de assinatura para (a) certificados de servidores TLS, (b) firmware dos guindastes, (c) uma raiz offline usada duas vezes por ano. Rubrica: 3 = ML-DSA; LMS/XMSS ou ML-DSA, com razões; SLH-DSA ou ML-DSA, com razões.

### Síntese

As assinaturas e a PKI carregam confiança de vida longa; os esquemas baseados em hash são conservadores e ou têm estado ou são grandes; o ML-DSA é a escolha de uso geral; as raízes precisam migrar primeiro.

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 50

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Segurança quântica e pós-quântica: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) explicar com precisão a ameaça quântica à criptografia implantada; (2) aplicar a desigualdade de Mosca para priorizar sistemas; (3) resumir o panorama de normas e políticas, com a sua situação; e (4) enquadrar a migração da BPA como um programa de engenharia. Este capítulo abre o núcleo de PQC e se apoia em todos os fundamentos.

### 20.1 O que quebra e o que não quebra

O algoritmo de Shor quebra RSA, Diffie–Hellman em corpo finito, DSA, ECDSA, EdDSA, ECDH e X25519 — todos os algoritmos de chave pública amplamente implantados. O algoritmo de Grover enfraquece apenas modestamente as cifras simétricas e os hashes; o AES-256 e o SHA-384/SHA-512 continuam sendo escolhas conservadoras. Assim, a migração trata da criptografia de *chave pública*: estabelecimento de chaves e assinaturas digitais.

Isso divide o inventário da BPA em duas listas. Todo uso de RSA, ECDSA, ECDH e X25519 precisa de substituição ou de um híbrido. Os usos de AES-256 e SHA-384 não precisam de mudança, e o AES-128 pode passar ao AES-256 durante a renovação rotineira. Manter as listas separadas impede que o programa passe o primeiro ano em mudanças simétricas que reduzem pouco risco.

### 20.2 Priorizar com Mosca

Para cada sistema, estime *x* (por quanto tempo os seus dados ou assinaturas precisam permanecer seguros), *y* (quanto tempo a migração levará) e trate *z* (o tempo até um CRQC) como uma faixa. Se *x* + *y* > *z* para um *z* plausível, o sistema já está atrasado ([Mosca 2018](https://doi.org/10.1109/MSP.2018.3761723)). Os dados aduaneiros da BPA (*x* = 25) estão atrasados em qualquer faixa plausível; o fluxo de rastreamento de contêineres (*x* ≈ 0,1) pode seguir o ciclo tecnológico normal.

Para os dados aduaneiros, x = 25 e a migração pode levar y = 5 anos, então qualquer CRQC que chegue antes de trinta anos a partir de agora expõe parte dos registros de hoje.

### 20.3 Normas e políticas, com a situação

O NIST publicou o ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)), o ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) e o SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) em agosto de 2024; as assinaturas baseadas em hash com estado estão na [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208); a orientação de uso de KEMs é a [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) (setembro de 2025). O HQC foi selecionado em março de 2025 como KEM de reserva ([IR 8545](https://doi.org/10.6028/NIST.IR.8545)); o FN-DSA está sendo padronizado. O rascunho do [NIST IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) propõe descontinuar os algoritmos vulneráveis à computação quântica de 112 bits após 2030 e proibi-los após 2035. A IETF padronizou os grupos híbridos do TLS ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) e a terminologia dos híbridos ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)). As situações mudam — verifique novamente.

### 20.4 A migração como programa

O [projeto Migration to Post-Quantum Cryptography](https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms) do NCCoE mantém duas frentes de trabalho com colaboradores da indústria — a descoberta criptográfica (ferramentas de inventário que apoiam a priorização baseada em risco) e os testes de interoperabilidade dos algoritmos padronizados em protocolos comuns. Pacotes de trabalho de engenharia para a BPA: inventário (CBOM), requisitos, arquitetura, relação com fornecedores, pilotos, implantação, verificação e agilidade.

Os pacotes de trabalho correm em parte em paralelo: o inventário e a relação com fornecedores começam imediatamente, porque ditam o ritmo de todo o resto. Os pilotos começam assim que uma biblioteca e um parceiro estejam prontos, enquanto a verificação é planejada desde o início.

### 20.5 Exemplo resolvido

A lista inicial de prioridades da BPA: (1) replicação e exportações aduaneiras — confidencialidade, *x* = 25; (2) VPNs com parceiros — o tráfego gravado inclui condições comerciais, *x* = 10; (3) raiz da PKI e assinatura de firmware — confiança de vida longa; (4) portal público — TLS híbrido disponível a baixo custo; (5) telemetria interna de vida curta — depois.

A ordem segue x: primeiro os dados aduaneiros de 25 anos, depois as condições comerciais de 10 anos nas VPNs. A raiz da PKI fica em terceiro, apesar de dados menos sensíveis, porque precisa ser distribuída muito antes do uso. O portal fica em quarto apenas porque o TLS híbrido ali é barato e rápido. A telemetria de vida curta espera pelas atualizações normais das bibliotecas.

### 20.6 Erros comuns e limites

- Migrar primeiro a criptografia simétrica.
- Tratar datas de políticas como previsões quânticas.
- Usar nomes de candidatos ("Kyber") para as normas finais ("ML-KEM").

A migração que começa pelo simétrico gasta esforço onde Grover tem pouco efeito, enquanto a troca de chaves vulnerável a Shor continua vazando tráfego gravado. Datas de políticas, como os prazos do CNSA 2.0, refletem planejamento, não previsões de um CRQC, e não devem ser lidas como previsões. Os nomes de rascunho causam erros de interoperabilidade, porque o Kyber de rascunho e o ML-KEM final diferem, então os inventários registram os nomes finais e a norma a que cada um se refere, como a FIPS 203 para o ML-KEM.

### Exercícios

- **EX039 — Tabela de Mosca.** Monte uma tabela de Mosca (*x*, *y*, veredito ao longo de *z* = 10–30) para cinco sistemas da BPA. Rubrica: 3 = valores justificados, vereditos coerentes.
- **EX040 — Resumo da situação.** Escreva um resumo de 150 palavras da situação das normas de PQC, com citações. Rubrica: 3 = situações e datas corretas.

### Síntese

Os computadores quânticos ameaçam a criptografia de chave pública; a desigualdade de Mosca ordena o trabalho; existem normas para KEMs e assinaturas, e outras estão a caminho; a migração é um programa de vários anos.

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 50

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Segurança quântica e pós-quântica: requisitos

### Objetivos de aprendizagem

Você vai (1) escrever requisitos de PQC verificáveis; (2) derivar requisitos dos tempos de vida dos dados, das políticas e das restrições dos parceiros; (3) incluir requisitos de disponibilidade e de agilidade; e (4) rastrear os requisitos até os métodos de verificação. O capítulo parte do Capítulo 20 e prepara os modelos e a análise de ameaças.

### 21.1 Bons requisitos

Um requisito é necessário, inequívoco, verificável e rastreável. "O sistema deverá ser seguro contra a computação quântica" falha nos quatro. Melhor: "REQ-KE-01: Todas as conexões TLS na borda externa deverão negociar o X25519MLKEM768 ou um grupo híbrido PQ/T mais forte quando o cliente oferecer um. Verificação: a telemetria passiva mostra que ≥ 99% dos clientes que o oferecem o negociam."

O requisito reescrito nomeia uma propriedade, um lugar e um limiar, e a linha de verificação diz que evidência conta. A condição "quando o cliente oferecer um" importa: a BPA não pode obrigar scanners portáteis antigos a suportar o grupo híbrido, então um requisito que os ignorasse nunca poderia ser cumprido.

### 21.2 Fontes

Derive os requisitos de: tempos de vida da confidencialidade dos dados (Capítulo 13), períodos de validade das assinaturas (conhecimentos de embarque: 12 anos), políticas (planos de transição do NIST, reguladores setoriais, CNSA 2.0 para parceiros de segurança nacional), capacidades dos parceiros e restrições operacionais (orçamentos de tamanho de handshake, memória dos dispositivos).

Cada fonte produz números que acabam no texto dos requisitos. O tempo de vida aduaneiro de 25 anos torna urgente o REQ-EXP-03; a validade de 12 anos dos conhecimentos de embarque fixa o prazo da assinatura com ML-DSA; o orçamento de handshake de 1.300 bytes limita o conjunto de parâmetros; os 32 KB de flash dos controladores dos guindastes restringem a escolha da assinatura de firmware. Registrar de qual fonte veio cada requisito permite aos revisores conferi-lo quando essa fonte mudar.

### 21.3 Categorias de requisitos

- **Estabelecimento de chaves**: quais protocolos usam KEMs híbridos ou PQC, com quais conjuntos de parâmetros.
- **Assinaturas**: quais artefatos precisam de assinaturas pós-quânticas, e até quando.
- **Agilidade**: "REQ-AG-02: Substituir o algoritmo KEM no TLS de borda deverá exigir apenas uma mudança de política e poderá ser concluído em até 30 dias, incluindo os testes."
- **Inventário**: "REQ-INV-01: O CBOM deverá cobrir ≥ 95% dos ativos, com a parcela desconhecida relatada mensalmente."
- **Disponibilidade**: "REQ-AV-01: Ativar grupos híbridos não deverá elevar as falhas de handshake acima da linha de base + 0,04 ponto percentual (limite superior de 95%)."

Todo requisito aqui carrega um número, para que os testes possam dizer aprovado ou reprovado.

### 21.4 Rastreabilidade

Cada requisito se liga a uma fonte e a um método de verificação (teste, análise, inspeção, demonstração). Uma matriz de rastreabilidade mostra a cobertura e ajuda os revisores a encontrar requisitos órfãos.

Na matriz da BPA, o REQ-KE-01 remonta ao tempo de vida dos dados aduaneiros e aponta adiante para a consulta da telemetria passiva; o REQ-AG-02 remonta à política de agilidade e aponta adiante para um exercício cronometrado em que a equipe troca o KEM num ambiente de testes. Um requisito sem ligação adiante não tem evidência de que foi cumprido, e um sem ligação para trás pode não ter razão de existir. Os dois tipos são sinalizados na revisão mensal.

### 21.5 Exemplo resolvido

O requisito de exportação aduaneira da BPA: "REQ-EXP-03: Os arquivos exportados para a agência aduaneira deverão ser cifrados para a chave ML-KEM-1024 da agência usando o KEMRecipientInfo do CMS ([RFC 9629](https://www.rfc-editor.org/rfc/rfc9629.html)), com um destinatário RSA-OAEP mantido em paralelo até que a agência confirme o suporte (data-alvo registrada). Verificação: inspeção da estrutura do arquivo exportado; teste de interoperabilidade com o sistema de testes da agência."

Manter o destinatário RSA-OAEP em paralelo significa que a agência consegue ler os arquivos durante a transição, mas também que os arquivos continuam expostos à coleta até que esse destinatário seja removido, por isso a data-alvo importa.

### 21.6 Erros comuns e limites

- Requisitos que nomeiam produtos em vez de propriedades.
- Ausência de requisitos de disponibilidade ou de agilidade.
- Requisitos sem métodos de verificação.

Nomear um produto prende a BPA a um fornecedor e nada diz sobre a propriedade necessária, de modo que um produto substituto não pode ser conferido contra ele. Sem requisitos de disponibilidade e de agilidade, uma implantação que quebra os parceiros ou que não pode ser mudada depois ainda passa na revisão. Um requisito sem método de verificação não pode ser encerrado, como mostra, por contraste, a linha de telemetria do REQ-KE-01. Cada requisito é revisado quanto às três falhas antes de entrar na linha de base.

### Exercícios

- **EX041 — Reescrever.** Reescreva "Usar PQC na VPN" como um requisito verificável. Rubrica: 3 = protocolo, parâmetro, condição e verificação declarados.
- **EX042 — Rastrear.** Monte uma matriz de rastreabilidade de cinco linhas para a BPA. Rubrica: 3 = fontes e métodos de verificação para cada linha.

### Síntese

Os requisitos de PQC são específicos, verificáveis e rastreados até os tempos de vida dos dados, as políticas e as restrições, e incluem agilidade, inventário e disponibilidade, não apenas algoritmos.

<!-- open-cyber-academy:chapter-navigation:start ch-21 -->
### Continue estudando — capítulo 21 de 50

[← Capítulo 20](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Segurança quântica e pós-quântica: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) modelar sistemas como ativos, fluxos e funções criptográficas; (2) construir um modelo de dados para um CBOM; (3) ligar os fluxos de dados aos tempos de vida da confidencialidade; e (4) usar os modelos para calcular a exposição. O capítulo parte dos Capítulos 13, 14 e 21.

### 22.1 Modelos de ativos e de fluxos

Modele cada ativo (serviço, dispositivo, repositório de dados) e cada fluxo entre ativos. Anote nos fluxos o protocolo, o algoritmo de estabelecimento de chaves, o algoritmo de autenticação e as classes de dados transportadas. Anote nos repositórios a cifragem, o método de encapsulamento de chaves e a retenção. O modelo se torna a espinha dorsal do inventário, da análise de ameaças e do planejamento.

A anotação dos fluxos é onde está a maior parte do valor, porque o risco de coleta se prende aos fluxos, não aos ativos. Um servidor pode hospedar tanto um fluxo de telemetria de vida curta quanto um fluxo de replicação aduaneira, e só o segundo é urgente. Registrar as classes de dados por fluxo permite ao modelo separá-los, o que uma lista de ativos sozinha não consegue.

### 22.2 Modelo de dados do CBOM

Um conjunto mínimo de entidades do CBOM: *Asset* (id, responsável, tipo, localização); *CryptoUse* (ativo, função: troca de chaves/assinatura/cifragem/hash, algoritmo, conjunto de parâmetros, protocolo, biblioteca, fonte da evidência, última observação); *Key/Certificate* (algoritmo, tamanho, emissor, validade, armazenamento); *DataClass* (tempo de vida). O campo *fonte da evidência* — código, configuração, observação passiva, declaração do fornecedor — importa porque as fontes diferem em confiabilidade.

O código e a configuração mostram a intenção, a observação passiva mostra o que foi negociado, e uma declaração do fornecedor é uma alegação até ser testada. Os relatórios de planejamento da BPA mostram a parcela de cada fonte, de modo que um retrato construído sobretudo com declarações fica visivelmente mais fraco.

### 22.3 Cálculo da exposição

Exposição de um fluxo = (tempo de vida dos dados > tempo até o CRQC assumido) × (troca de chaves vulnerável) × (gravável pelo adversário). Uma consulta sobre o modelo lista os fluxos expostos; juntá-la ao volume de tráfego os ordena. Campos incertos são *desconhecidos*, nunca presumidos seguros.

O primeiro fator usa a data assumida do CRQC como uma faixa, de modo que um fluxo pode estar exposto apenas no caso pessimista; a consulta informa os dois casos. O terceiro fator capta se um adversário consegue gravar o fluxo, o que é alto para enlaces de internet e mais baixo para tráfego dentro de uma sala de equipamentos trancada. Tratar campos desconhecidos como desconhecidos mantém as lacunas visíveis, e a contagem de desconhecidos se torna um indicador antecedente para a equipe de inventário.

### 22.4 Exemplo resolvido

O modelo da BPA tem 412 ativos e 1.930 fluxos. Consultar os fluxos que transportam dados com tempo de vida ≥ 10 anos sobre troca de chaves só ECDHE devolve 37 fluxos, 29 dos quais passam por quatro gateways — o que faz dos gateways os alvos de migração de maior alavancagem.

Quatro gateways tratando 29 de 37 fluxos expostos significam que uma mudança de configuração em quatro dispositivos remove a maior parte da exposição, com muito mais eficiência do que visitar cada aplicação. Os oito fluxos restantes são tratados um a um. Essa é a alavancagem que um modelo dá: sem ele, a equipe provavelmente começaria pelo dono de aplicação que se oferecesse primeiro.

### 22.5 Atividade prática

Esboce as entidades do CBOM numa tabela ou como dataclasses Python, depois preencha dez registros a partir da descrição da BPA e escreva uma consulta pelos fluxos expostos. O Laboratório I do Capítulo 29 amplia isso.

Escolha registros que incluam pelo menos um campo desconhecido e um fluxo com dados de vida longa sobre ECDHE, para que a consulta devolva algo a discutir. Confira se a sua consulta lista os desconhecidos separadamente, em vez de descartá-los em silêncio. Depois acrescente uma coluna de volume de tráfego e ordene os fluxos expostos por volume para ver quais seriam os primeiros itens de trabalho. Guarde as dataclasses para o laboratório posterior.

### 22.6 Erros comuns e limites

- Modelos que registram algoritmos, mas não a fonte da evidência.
- Tratar o desconhecido como seguro.
- Modelos construídos uma vez e nunca atualizados.

Sem a fonte da evidência, a alegação de um fornecedor de suportar PQC parece igual a um handshake medido, e o planejamento se apoia em dados não verificados. Tratar o desconhecido como seguro faz a consulta de exposição parecer melhor à medida que o inventário piora. Um modelo construído uma vez fica errado na próxima versão; a BPA o atualiza a partir do CBOM em cada build e da observação passiva toda semana.

### Nota de engenharia

Os modelos também precisam registrar o tempo. Um fluxo observado uma vez há dezoito meses pode não existir mais, e uma biblioteca atualizada na semana passada pode ter mudado os padrões. Guarde os registros de primeira e última observação com cada observação e passe os registros envelhecidos para um estado "não verificado", em vez de apagá-los em silêncio. Isso mantém a consulta de exposição honesta: ela distingue os fluxos sabidamente vulneráveis agora daqueles que eram vulneráveis na última observação e precisam ser observados de novo antes que alguém gaste orçamento de migração com eles.

### Exercícios

- **EX043 — Projeto da entidade.** Defina a entidade CryptoUse com tipos de campo e valores permitidos. Rubrica: 3 = inclui a fonte da evidência e o registro de última observação.
- **EX044 — Consulta de exposição.** Escreva pseudocódigo para a consulta de fluxos expostos. Rubrica: 3 = trata explicitamente os valores desconhecidos.

### Síntese

Modelos de ativos e fluxos anotados com funções criptográficas e tempos de vida dos dados transformam as perguntas da migração em consultas; o modelo do CBOM precisa registrar as fontes de evidência e os desconhecidos.

<!-- open-cyber-academy:chapter-navigation:start ch-22 -->
### Continue estudando — capítulo 22 de 50

[← Capítulo 21](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Segurança quântica e pós-quântica: análise de ameaças e de falhas

### Objetivos de aprendizagem

Você vai (1) modelar as ameaças da era quântica com uma análise no estilo STRIDE; (2) analisar os modos de falha introduzidos pela própria migração; (3) incluir ataques de rebaixamento e de implementação; e (4) priorizar com uma pontuação de risco. O capítulo parte dos Capítulos 15 e 22.

### 23.1 Ameaças da era quântica

- **Colete agora, decifre depois**: gravar tráfego protegido por uma troca de chaves vulnerável.
- **Falsificação futura**: falsificar assinaturas em artefatos de vida longa quando existir um CRQC.
- **Rebaixamento**: um atacante ativo remove as opções pós-quânticas para que os pares voltem a uma troca só clássica. O TLS 1.3 protege a transcrição da negociação, então o rebaixamento exige quebrar a autenticação — mas uma lógica de fallback mal configurada nas aplicações pode reintroduzi-lo.
- **Ataques de implementação**: canais laterais e injeção de falhas contra código novo (Capítulo 31).
- **Surpresa criptoanalítica**: uma fraqueza encontrada num esquema novo, como aconteceu com o Rainbow e o SIKE ([Beullens 2022](https://eprint.iacr.org/2022/214); [Castryck e Decru 2022](https://eprint.iacr.org/2022/975)).

### 23.2 Modos de falha da migração

A análise de modos de falha e efeitos (FMEA) se aplica: handshakes grandes demais descartados por middleboxes; clientes que não conseguem interpretar os novos certificados; HSMs que não conseguem guardar as novas chaves; chaves de assinatura com estado reutilizadas após a restauração de um backup; falhas de interoperabilidade entre implementações de rascunho e finais; certificados de transição expirados. Cada um tem causa, efeito, método de detecção e mitigação.

Vários deles já apareceram no caso da BPA: o proxy que reiniciava ClientHellos divididos, a falha de importação de chaves entre HSMs e o risco de reutilização do estado do LMS após uma restauração. Listá-los numa única tabela obriga a definir um método de detecção para cada um, que costuma ser a parte que falta.

### 23.3 Pontuação de risco

Pontue probabilidade e impacto; para as ameaças de coleta, o impacto cresce com o tempo de vida e o volume dos dados. Evite a falsa precisão: três ou cinco níveis com definições claras bastam.

A BPA usa três níveis com definições escritas: impacto alto significa dados com tempo de vida acima de dez anos ou uma função de segurança operacional; médio significa dados comerciais abaixo de dez anos; baixo significa dados operacionais de vida curta. Dois avaliadores que pontuam o mesmo item devem chegar ao mesmo nível e, quando não chegam, as definições são apertadas, em vez de se tirar a média. Uma nota como três vírgula sete numa escala de cinco pontos sugere uma precisão que os insumos não sustentam.

### 23.4 Exemplo resolvido

FMEA da assinatura do firmware dos guindastes da BPA com LMS: falha "contador de estado reiniciado após a restauração do HSM" → efeito "reutilização de chave de uso único permitindo falsificação" → detecção "auditoria do contador monotônico contra o log" → mitigação "HSM com reserva de estado, procedimentos de restauração que proíbem o retrocesso, chave separada por local de assinatura". Severidade alta, probabilidade média → ação prioritária.

A etapa de detecção funciona porque cada assinatura carrega o seu índice: comparar o maior índice visto no firmware publicado com o contador do HSM mostra de imediato um retrocesso. Chaves separadas por local limitam o dano de um erro às assinaturas de um único local.

### 23.5 Erros comuns e limites

- Analisar só ameaças criptoanalíticas, e não as falhas da migração.
- Supor que os híbridos dispensam a análise do rebaixamento.
- Pontuações numéricas de risco apresentadas como medições.

A maioria dos incidentes nas primeiras migrações vem de modos de falha como o reinício do proxy, não da criptoanálise, então uma análise limitada a ataques deixa escapar os problemas prováveis. Os híbridos protegem contra a quebra de um componente, mas um fallback mal configurado ainda pode remover inteiramente a parte pós-quântica, por isso os caminhos de rebaixamento são analisados por aplicação. As pontuações de risco ordenam itens; não são medições e não devem ser somadas.

### Nota de engenharia

Por fim, ordene as ameaças pelo momento em que podem se concretizar. O "colete agora, decifre depois" está acontecendo hoje para qualquer tráfego gravado, embora a decifração precise de uma máquina futura; a falsificação ativa exige que a máquina exista no momento do ataque. Essa divisão temporal explica por que a mesma organização pode, racionalmente, migrar a troca de chaves neste ano e agendar a migração das assinaturas para depois, e dá aos tomadores de decisão uma razão clara para a ordem do trabalho, em vez de uma lista indiferenciada de riscos quânticos.

### Exercícios

- **EX045 — Tabela de ameaças.** Produza uma tabela de ameaças para a VPN dos parceiros da BPA cobrindo as cinco classes de ameaça. Rubrica: 3 = cada uma com mitigação.
- **EX046 — Linha de FMEA.** Escreva uma linha de FMEA para "middlebox descarta ClientHello de dois segmentos". Rubrica: 3 = causa, efeito, detecção, mitigação, prioridade.

### Síntese

A análise de ameaças na era quântica inclui gravação, falsificação futura, rebaixamento, ataques de implementação e surpresa criptoanalítica; a própria migração tem modos de falha que a FMEA torna visíveis.

<!-- open-cyber-academy:chapter-navigation:start ch-23 -->
### Continue estudando — capítulo 23 de 50

[← Capítulo 22](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Segurança quântica e pós-quântica: métodos I

### Objetivos de aprendizagem

Você vai (1) explicar o aprendizado com erros (LWE) e por que o ruído torna difícil a álgebra linear; (2) acompanhar uma cifragem LWE de brinquedo; (3) relacioná-la à estrutura do ML-KEM; e (4) entender o papel da transformação de Fujisaki–Okamoto. O capítulo parte do Capítulo 2 e fundamenta as escolhas de projeto dos Capítulos 25–28.

### 24.1 Aprendizado com erros

Dada uma matriz aleatória *A* e *b* = *A*·*s* + *e* mod *q*, em que *s* é secreto e *e* é um vetor de pequenos erros aleatórios, encontre *s*. Sem *e*, isso é eliminação gaussiana. Com *e*, não se conhece algoritmo eficiente, clássico ou quântico, para parâmetros adequados; [Regev (2009)](https://doi.org/10.1145/1568318.1568324) relacionou o LWE a problemas de reticulados no pior caso. Os melhores ataques usam redução de reticulados, cujo custo cresce exponencialmente com a dimensão.

O papel do ruído aparece na dimensão: no Laboratório W, dezesseis incógnitas com erros pequenos são fáceis de resolver por força bruta sobre os erros, enquanto o ML-KEM-768 trabalha com dimensão 768, em que os melhores ataques de redução de reticulados precisam de muito mais trabalho do que qualquer computador consegue fazer.

### 24.2 Cifrar um bit

Para cifrar um bit, some um subconjunto aleatório de linhas de (*A*, *b*): *u* = Σ*r*ᵢ*A*ᵢ, *v* = Σ*r*ᵢ*b*ᵢ + bit·⌊*q*/2⌋. O detentor da chave calcula *v* − ⟨*u*, *s*⟩ = bit·⌊*q*/2⌋ + ruído pequeno e arredonda. A decifração funciona enquanto o ruído acumulado ficar abaixo de *q*/4.

No Laboratório W, os erros são no máximo 2 em valor absoluto e o subconjunto tem no máximo 64 linhas, então o ruído acumulado é no máximo 128. Isso está muito abaixo de q/4, que é cerca de 832, então todo bit é decifrado corretamente. Erros maiores ou mais linhas empurrariam o ruído rumo a q/4 e causariam falhas, que é o compromisso que os parâmetros do ML-KEM equilibram com a segurança.

### 24.3 Atividade prática — Laboratório W (brinquedo, inseguro)

```python
# Lab W (ch 24): a TOY Regev-style LWE encryption of one bit. Deliberately insecure parameters.
import random
rng = random.Random(5)
n, q, m = 16, 3329, 64
def small(): return rng.choice([-2, -1, 0, 1, 2])
s = [rng.randrange(q) for _ in range(n)]
A = [[rng.randrange(q) for _ in range(n)] for _ in range(m)]
b = [(sum(A[i][j] * s[j] for j in range(n)) + small()) % q for i in range(m)]   # b = A s + e
def enc(bit):
    r = [rng.randrange(2) for _ in range(m)]                                        # random subset
    u = [sum(r[i] * A[i][j] for i in range(m)) % q for j in range(n)]
    v = (sum(r[i] * b[i] for i in range(m)) + bit * (q // 2)) % q
    return u, v
def dec(u, v):
    d = (v - sum(u[j] * s[j] for j in range(n))) % q                                 # = bit*q/2 + small noise
    return 1 if q // 4 < d < 3 * q // 4 else 0
ok = sum(dec(*enc(bit)) == bit for bit in [rng.randrange(2) for _ in range(2000)])
print(f"toy LWE: {ok}/2000 bits decrypted correctly (noise stays below q/4)")
```

Saída esperada:

```text
toy LWE: 2000/2000 bits decrypted correctly (noise stays below q/4)
```

Esses parâmetros são pequenos demais para dar segurança e vazam por muitos caminhos; o laboratório existe só para tornar a álgebra concreta.

O resultado de 2000 em 2000 decorre do limite: um ruído de no máximo 128 nunca pode cruzar o limiar de 832. Mude `small()` para sortear de −20 a 20 e execute de novo; o ruído no pior caso sobe para 1.280, acima do limiar, mas os 2000 bits continuam sendo decifrados, porque uma soma de cerca de 32 erros aleatórios raramente se aproxima do pior caso; as falhas só aparecem com erros muito maiores, como mostra o exercício EX047. Depois faça-a devolver sempre 0 e resolva *s* a partir de dezesseis linhas de A e b por eliminação gaussiana, o que mostra que são os erros que carregam a segurança.

### 24.4 Do brinquedo ao ML-KEM

O ML-KEM substitui os inteiros por polinômios em Z₃₃₂₉[*x*]/(*x*²⁵⁶+1) e usa a estrutura de módulo (*k* = 2, 3 ou 4 vetores de polinômios) para ter chaves compactas, comprime os textos cifrados, sorteia o ruído de uma distribuição binomial centrada e deriva a aleatoriedade com SHAKE. A cifragem de chave pública subjacente só é segura contra atacantes passivos; o ML-KEM aplica uma transformação no estilo Fujisaki–Okamoto — recifrar durante o desencapsulamento e devolver uma chave pseudoaleatória de "rejeição implícita" em caso de divergência — para resistir a ataques de texto cifrado escolhido ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)).

Cada mudança tem um propósito: polinômios e módulos encolhem as chaves, a compressão economiza bytes e a transformação resiste a ataques ativos.

### 24.5 Exemplo resolvido

Um engenheiro da BPA pergunta por que o desencapsulamento do ML-KEM recifra. Resposta: para detectar textos cifrados manipulados. Sem essa verificação, um atacante poderia enviar textos cifrados forjados e aprender sobre a chave secreta a partir do sucesso ou não da decifração. As implementações precisam fazer a comparação em tempo constante, ou o tempo da verificação vaza a mesma informação.

A chave de rejeição implícita também importa: devolver um erro em caso de divergência diria, por si só, ao atacante que o texto cifrado era inválido. Ao devolver uma chave pseudoaleatória derivada de um valor secreto, o ML-KEM faz o caso inválido parecer um sucesso normal para o atacante, e o protocolo falha mais adiante de uma forma que nada revela sobre a chave.

### 24.6 Erros comuns e limites

- Achar que a segurança do LWE vem da matriz, e não do ruído.
- Usar a cifragem segura só contra atacantes passivos sem a transformação FO.
- Tratar o brinquedo como um esquema utilizável.

O Laboratório W mostra o primeiro ponto diretamente: retire os erros e o segredo cai diante da eliminação gaussiana. O esquema seguro só contra passivos, sem a transformação, fica aberto aos ataques de texto cifrado escolhido descritos no exemplo resolvido. O brinquedo usa dimensão dezesseis e nenhuma compressão, então não oferece segurança alguma, e o seu único uso é didático.

### Exercícios

- **EX047 — Orçamento de ruído.** No Laboratório W, mude a escolha dos erros para `rng.randint(-150, 150)` e depois para `rng.randint(-300, 300)` e observe a decifração. Explique. Rubrica: 3 = aparecem falhas; explica o ruído acumulado contra *q*/4.
- **EX048 — Propósito da FO.** Explique a rejeição implícita a um desenvolvedor em 120 palavras. Rubrica: 3 = raciocínio de texto cifrado escolhido e exigência de tempo constante.

### Síntese

O LWE esconde segredos sob ruído; um brinquedo mostra a decifração como arredondamento; o ML-KEM acrescenta estrutura de anel/módulo, compressão e a transformação FO para a segurança contra texto cifrado escolhido.

<!-- open-cyber-academy:chapter-navigation:start ch-24 -->
### Continue estudando — capítulo 24 de 50

[← Capítulo 23](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) conduzir um ateliê de projeto estruturado sobre um problema com forma real; (2) produzir um projeto de troca de chaves híbrida para a borda da BPA; (3) apresentá-lo e defendê-lo com evidências; e (4) incorporar as críticas. O capítulo integra os Capítulos 20–24.

### 25.1 Enunciado

Projete o estabelecimento de chaves resistente à computação quântica para o portal público da BPA e a borda das APIs de parceiros: 2 milhões de conexões por dia, uma população mista de clientes (navegadores, software dos parceiros, scanners portáteis antigos), um proxy de inspeção num dos caminhos e uma CDN à frente do portal. Restrições: nenhuma regressão de disponibilidade além do requisito do Capítulo 21, orçamento para a atualização de um único equipamento, prazo de seis meses.

As restrições puxam em direções diferentes. Dois milhões de conexões diárias significam que até taxas de falha pequenas produzem muitos incidentes; os scanners antigos talvez nunca suportem grupos híbridos; o orçamento de um único equipamento não substitui todos os dispositivos. Bons projetos dizem explicitamente qual restrição relaxam e por quê.

### 25.2 Método do ateliê

As equipes produzem: diagrama de contexto; subconjunto de requisitos; duas alternativas; estudo de compromisso; projeto escolhido com esboço de configuração; plano de testes; riscos. Cada equipe apresenta por dez minutos e recebe as críticas de uma banca que representa operações, segurança, parceiros e finanças.

Apresentar duas alternativas obriga as equipes a justificar a escolha, em vez de defender a primeira ideia. Os papéis da banca refletem os revisores reais que a BPA enfrentaria: operações pergunta sobre monitoramento, finanças sobre custo, parceiros sobre compatibilidade. As equipes que preparam evidências para cada papel, como um plano de testes mostrando que o firmware do proxy foi verificado, costumam lidar melhor com as críticas do que as que se apoiam em argumentos gerais. As críticas são registradas para que as equipes possam revisar o projeto depois.

### 25.3 Esboço da solução de referência

Terminar o TLS na CDN e no proxy de borda com o X25519MLKEM768 oferecido primeiro e o X25519 como alternativa para clientes que não suportam o grupo híbrido ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)); atualizar o firmware do proxy de inspeção ou desviar a inspeção do TLS 1.3 para as APIs de parceiros; deixar os scanners portáteis em grupos clássicos, sob uma exceção de curto prazo com data de substituição; medir os grupos negociados pelos logs; implantação escalonada com portões de canário. Nota: a troca de chaves híbrida protege contra a gravação; os certificados continuam clássicos por enquanto — documentado como lacuna conhecida, com um pacote de trabalho posterior.

### 25.4 Exemplos de crítica

Operações pergunta como o fallback é monitorado; segurança pergunta se o fallback poderia ser forçado (no TLS 1.3, só quebrando a autenticação ou explorando a lógica de novas tentativas no nível da aplicação, que precisa ser verificada); parceiros perguntam sobre as versões das bibliotecas dos seus clientes; finanças pergunta sobre os custos dos equipamentos. Boas equipes respondem com evidências ou acrescentam itens de trabalho.

A pergunta de segurança é a mais sutil: se uma aplicação repete todo handshake malsucedido sem o grupo híbrido, um atacante pode forçar falhas e obter conexões clássicas. Uma boa resposta verifica a lógica de novas tentativas do portal e registra qualquer fallback.

### 25.5 Erros comuns e limites

- Projetos que ignoram a população de clientes antigos.
- Nenhum plano de medição dos grupos negociados.
- Afirmar que o portal é "seguro contra a computação quântica" enquanto os certificados são clássicos.

Os scanners portáteis não podem ser ignorados: precisam de uma exceção com data de substituição, como mostra o esboço de referência. Sem medir os grupos negociados, ninguém sabe se a implantação funcionou. Chamar o portal de "seguro contra a computação quântica" enquanto os certificados continuam clássicos engana as partes interessadas, já que ataques ativos com um futuro CRQC ainda seriam possíveis; em vez disso, o esboço documenta essa lacuna, com um pacote de trabalho posterior.

### Nota de engenharia

Os ateliês também treinam o hábito de anotar o que o projeto não faz. A solução de referência protege as trocas de chaves gravadas, mas não a autenticação, não cobre os scanners portáteis até a substituição e depende do firmware do fornecedor para o proxy de inspeção. Listar isso explicitamente no registro do projeto transforma esses pontos em pacotes de trabalho acompanhados, com responsáveis, em vez de descobertas feitas por um auditor. Um projeto que declara as suas lacunas é mais fácil de aprovar do que um que parece completo, mas não é.

### Exercícios

- **EX049 — Entregável do ateliê.** Produza o diagrama de contexto (com alternativa em texto) e o estudo de compromisso para o enunciado. Rubrica: 3 = duas alternativas reais, pesos antes das notas.
- **EX050 — Resposta à crítica.** Responda em 150 palavras à pergunta da banca de segurança sobre o fallback. Rubrica: 3 = proteção da transcrição no TLS 1.3 e risco das novas tentativas da aplicação, ambos tratados.

### Síntese

Um ateliê de projeto transforma normas num projeto configurado, medido e escalonado, cujas lacunas estão declaradas e cujos críticos foram respondidos.

<!-- open-cyber-academy:chapter-navigation:start ch-25 -->
### Continue estudando — capítulo 25 de 50

[← Capítulo 24](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Segurança quântica e pós-quântica: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar PQC pura, híbrido PQ/T e mitigações provisórias; (2) avaliar certificados compostos versus paralelos; (3) considerar alternativas de chave simétrica, como chaves pré-compartilhadas; e (4) escolher a arquitetura por contexto. O capítulo parte dos Capítulos 18 e 25.

### 26.1 Pura versus híbrida

A **PQC pura** usa apenas algoritmos pós-quânticos: mais simples e menor que o híbrido, mas aposta tudo em pressupostos mais novos. O **híbrido PQ/T** combina os dois ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)): é seguro se qualquer um deles resistir, ao custo extra de bytes e complexidade. Durante a transição, muitos protocolos e documentos de orientação preferem híbridos para a troca de chaves; algumas orientações governamentais, como o CNSA 2.0, aceitam PQC pura com os conjuntos de parâmetros da categoria 5. A escolha depende do apetite de risco frente a uma surpresa criptoanalítica versus a complexidade.

A BPA escolhe híbridos para a troca de chaves externa.

### 26.2 Certificados

Opções para a autenticação pós-quântica: (a) **certificados de PQC pura** (chaves e assinaturas ML-DSA); (b) **certificados compostos**, em que um certificado carrega uma chave tradicional e uma pós-quântica e as duas assinaturas precisam ser verificadas; (c) **cadeias paralelas** — dois certificados, um por algoritmo, com a negociação escolhendo; (d) **migração adiada**, com certificados clássicos de vida curta, aceitável onde ataques quânticos ativos ainda não são viáveis. Cada uma troca compatibilidade, tamanho e complexidade.

Para a BPA, a opção (d) é aceitável por enquanto para os certificados web públicos, porque eles duram cerca de um ano e um ataque quântico ativo precisa de um CRQC no momento da conexão.

### 26.3 Mitigações provisórias

Onde a PQC ainda não está disponível — em equipamentos de VPN antigos, por exemplo —, misturar uma chave simétrica pré-compartilhada na derivação de chaves pode proteger o tráfego gravado, já que as PSKs não são vulneráveis a Shor. O [RFC 8784](https://www.rfc-editor.org/rfc/rfc8784.html) define um mecanismo desse tipo para o IKEv2. As PSKs trazem os ônus da distribuição e da rotação de chaves, então são uma ponte, não um destino.

Para os dois parceiros de maior valor da BPA, a PSK é trocada por um canal fora de banda e rotacionada a cada três meses, com responsável e expiração registrados por parceiro. O tráfego gravado do túnel fica então protegido mesmo enquanto o equipamento oferece apenas troca de chaves clássica.

### 26.4 Tabela de decisão

| Contexto | Troca de chaves | Autenticação |
|---|---|---|
| Portal web público | Híbrido X25519MLKEM768 | Clássica agora, ML-DSA quando os clientes suportarem |
| VPN de parceiro, equipamento antigo | IKEv2 + mistura de PSK (provisório) | Clássica, de vida curta |
| VPN de parceiro, moderna | IKEv2 com troca adicional ML-KEM (RFC 9370) | Conforme a capacidade do parceiro |
| Firmware dos guindastes | — | LMS/XMSS ou ML-DSA |
| Parceiro de segurança nacional | ML-KEM-1024 conforme o CNSA 2.0 | ML-DSA-87 |

A tabela torna explícita a variação: a mesma organização usa cinco combinações diferentes conforme o contexto. Cada linha remonta a uma decisão anterior, por exemplo a linha do firmware dos guindastes à restrição de 32 KB e a linha do equipamento antigo ao estudo de compromisso que escolheu a mistura de PSK como solução provisória. Quando um parceiro se atualiza, a sua linha muda e a tabela mostra o novo alvo. As linhas têm datas de revisão, para que as escolhas provisórias não se tornem permanentes.

### 26.5 Exemplo resolvido

A BPA debate certificados compostos para a sua PKI interna. Prós: uma só cadeia, os dois algoritmos verificados. Contras: suporte limitado nas bibliotecas, certificados maiores, política complexa. Decisão: cadeias paralelas internamente, onde os clientes podem ser atualizados, e adiar a migração dos certificados públicos até que exista suporte no ecossistema dos navegadores; revisão anual.

As cadeias paralelas internas permitem à BPA testar certificados ML-DSA com clientes que ela controla, sem esperar por um suporte mais amplo. A revisão anual verifica as versões dos navegadores e das bibliotecas; quando o ecossistema suportar certificados ML-DSA, o portal público migra, aproveitando a experiência da implantação interna.

### 26.6 Erros comuns e limites

- Uma só arquitetura para todos os contextos.
- PSKs sem planos de rotação.
- Supor que os certificados compostos têm suporte universal.

Uma arquitetura única falha porque os contextos diferem: um controlador de guindaste com 32 KB de flash e um portal público com milhões de navegadores não podem usar o mesmo projeto. PSKs sem rotação acabam vazando ou expirando sem que ninguém perceba, deixando os túneis desprotegidos; cada uma precisa de um responsável e de uma data de rotação trimestral. Os certificados compostos ainda têm suporte limitado nas bibliotecas, então as cadeias paralelas costumam ser a escolha prática por enquanto, como mostrou a decisão da PKI interna da BPA.

### Exercícios

- **EX051 — Argumento pelo híbrido.** Defenda em 150 palavras a troca de chaves híbrida no portal da BPA, citando as quebras de esquemas. Rubrica: 3 = raciocínio de "basta um resistir" e custo reconhecido.
- **EX052 — Ponte com PSK.** Projete uma abordagem provisória com PSK para uma VPN antiga, incluindo a rotação. Rubrica: 3 = distribuição, rotação, data de desativação.

### Síntese

As alternativas de arquitetura diferem conforme o contexto: os híbridos protegem contra surpresas, a PQC pura simplifica, as PSKs fazem a ponte e as estratégias de certificados trocam compatibilidade por garantia.

<!-- open-cyber-academy:chapter-navigation:start ch-26 -->
### Continue estudando — capítulo 26 de 50

[← Capítulo 25](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Segurança quântica e pós-quântica: projeto de controles

### Objetivos de aprendizagem

Você vai (1) projetar os controles que tornam segura a troca de chaves híbrida — combinadores, vínculo com a transcrição e negociação; (2) projetar controles de gestão de chaves para os novos tipos de chave; (3) especificar controles de política para os algoritmos permitidos; e (4) testar um combinador. O capítulo parte dos Capítulos 24–26.

### 27.1 Controles do combinador

Uma troca de chaves híbrida precisa derivar a chave de sessão dos dois segredos compartilhados, para que o comprometimento de um não revele a chave. No X25519MLKEM768, os segredos são concatenados (primeiro o ML-KEM) e entram no escalonamento de chaves do TLS 1.3, que os vincula à transcrição do handshake ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)). Combinadores próprios fora de protocolos padronizados devem seguir os métodos de derivação de chaves da [SP 800-56C](https://doi.org/10.6028/NIST.SP.800-56Cr2), que a FIPS 203 permite para os segredos compartilhados do ML-KEM, e vincular o contexto (identidades, textos cifrados, transcrição).

### 27.2 Atividade prática — Laboratório C

```python
# Lab C (ch 27): a hybrid key combiner. The session key depends on BOTH shared secrets.
import hashlib, hmac
def hkdf_extract(salt, ikm): return hmac.new(salt, ikm, hashlib.sha256).digest()
def combine(ss_pq, ss_trad, context):
    # Concatenate secrets (PQ first, as in X25519MLKEM768), bind the transcript/context, then extract.
    return hkdf_extract(b"\x00" * 32, ss_pq + ss_trad + context).hex()[:16]
pq, trad, ctx = b"P" * 32, b"T" * 32, b"handshake-transcript-hash"
print("baseline              ", combine(pq, trad, ctx))
print("PQ secret changed     ", combine(b"Q" * 32, trad, ctx))
print("traditional changed   ", combine(pq, b"U" * 32, ctx))
print("context changed       ", combine(pq, trad, b"other-transcript"))
```

Saída esperada:

```text
baseline               d48e982e8c06ca60
PQ secret changed      d4c36ea2d90b2e9c
traditional changed    8dcefa12ded3d99c
context changed        af06eca8abcd45a9
```

Mudar qualquer um dos segredos ou o contexto muda a saída: a chave derivada depende dos dois componentes e do que foi negociado.

Note que só os primeiros caracteres da saída hexadecimal são mostrados, para facilitar a leitura; uma derivação real usaria a saída completa e uma etapa adequada de expansão HKDF. Experimente passar um contexto vazio e compare: o resultado ainda depende dos dois segredos, mas não mais da transcrição, que é exatamente a fraqueza que o vínculo com o contexto evita.

### 27.3 Controles de negociação

A negociação dos algoritmos precisa ser autenticada. O TLS 1.3 assina a transcrição, então um atacante que remove os grupos híbridos é detectado, a menos que consiga falsificar a assinatura do servidor. Uma lógica de aplicação que repete a tentativa sem grupos híbridos após qualquer falha reabre o rebaixamento; controles: registrar e alertar sobre fallback e desativar o fallback onde todos os pares suportam híbridos.

O portal da BPA registra todo handshake que termina sem um grupo híbrido quando o cliente ofereceu um. Um aumento desses eventos dispara um alerta, já que pode significar um ataque ou um middlebox com mau comportamento, e os dois precisam de investigação.

### 27.4 Controles de gestão de chaves

Os novos tipos de chave precisam de controles de ciclo de vida: geração em módulos aprovados, armazenamento, rotação, backup e destruição. As chaves de desencapsulamento do ML-KEM podem ser guardadas como uma semente de 64 bytes, conforme a FIPS 203; as chaves de assinatura baseadas em hash com estado exigem proteção do estado contra retrocesso; as chaves ML-DSA precisam de suporte no HSM.

A forma de semente de 64 bytes é compacta e evita incompatibilidades de formato, como mostra o problema de importação no HSM do exemplo do próximo capítulo. A destruição também exige cuidado: uma chave precisa ser removida de todos os backups e partições de HSM, e a entrada do CBOM fechada com a data.

### 27.5 Controles de política

Uma lista de permissões de algoritmos e conjuntos de parâmetros por contexto — por exemplo, "TLS de borda: X25519MLKEM768, SecP256r1MLKEM768; fallback X25519 até 2027-12-31" —, implementada na configuração e verificada pela telemetria.

A entrada de fallback tem uma data de término para que não fique para sempre; depois dessa data, o X25519 sozinho é removido do TLS de borda. A telemetria confirma o que a configuração afirma, contando os grupos negociados por dia. Quando a contagem de conexões só clássicas se aproxima de zero, a equipe tem evidência de que a remoção não vai quebrar os parceiros, e a mudança pode passar sem um longo debate.

### 27.6 Exemplo resolvido

Uma equipe da BPA propõe fazer XOR dos dois segredos compartilhados para economizar uma chamada de KDF. A revisão rejeita: o XOR não oferece vínculo com o contexto e é frágil em algumas provas de segurança; use o combinador padrão do protocolo ou a derivação da SP 800-56C com os dois segredos e o contexto.

Economizar uma chamada de KDF não ganha nada mensurável: calcular o hash de algumas dezenas de bytes custa microssegundos, enquanto um combinador fraco poderia minar a própria razão de usar um híbrido. A revisão registra a decisão nas notas de projeto da equipe, para que a ideia não seja proposta de novo.

### 27.7 Erros comuns e limites

- Combinadores improvisados (XOR, truncamento).
- Fallback silencioso, sem registro.
- Tratar chaves com estado como chaves comuns no backup.

XOR e truncamento parecem inofensivos, mas descartam o vínculo com o contexto e podem enfraquecer as provas de segurança, como explicou o exemplo resolvido. O fallback silencioso esconde o rebaixamento, e é por isso que a BPA registra todo handshake sem o grupo híbrido. Fazer backup de uma chave de assinatura com estado como se fosse uma chave comum convida ao retrocesso do estado e à reutilização de chaves de uso único após uma restauração; a BPA exclui essas chaves dos backups rotineiros e mantém o estado delas no HSM.

### Exercícios

- **EX053 — Revisão de combinador.** Revise uma proposta que calcula o hash apenas do segredo de PQC "porque é mais forte". Rubrica: 3 = explica a perda da proteção dupla e recomenda o combinador padrão.
- **EX054 — Arquivo de política.** Escreva uma lista de permissões de política para a borda e os serviços internos da BPA, com datas de expiração para os fallbacks. Rubrica: 3 = conjuntos de parâmetros explícitos, expiração datada.

### Síntese

A segurança dos híbridos depende de controles: combinadores padronizados com vínculo ao contexto, negociação autenticada sem fallback silencioso, gestão do ciclo de vida dos novos tipos de chave e listas de permissões datadas.

<!-- open-cyber-academy:chapter-navigation:start ch-27 -->
### Continue estudando — capítulo 27 de 50

[← Capítulo 26](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Segurança quântica e pós-quântica: implementação I

### Objetivos de aprendizagem

Você vai (1) selecionar bibliotecas verificadas e módulos validados; (2) integrar o ML-KEM e o ML-DSA por meio de interfaces de provedores; (3) tratar codificações, identificadores e interoperabilidade; e (4) implementar com segurança a gestão de assinaturas com estado. O capítulo parte dos Capítulos 9, 14 e 27.

### 28.1 Seleção de bibliotecas

Use implementações mantidas e revisadas, com código em tempo constante, vetores de teste e, quando exigido, validação no Cryptographic Module Validation Program (CMVP) do NIST. Prefira bibliotecas que implementem as versões finais das FIPS, e não o Kyber/Dilithium de rascunho. Registre no CBOM a biblioteca, a versão e os identificadores de algoritmo.

A validação no CMVP leva tempo, então uma biblioteca pode suportar bem o ML-KEM muito antes de a sua versão validada estar disponível. A política da BPA aceita bibliotecas não validadas em pilotos e exige módulos validados em produção nos sistemas regulados, com as datas acompanhadas no plano.

### 28.2 Integração por provedores

A maioria das plataformas expõe a criptografia por meio de provedores (provedores do OpenSSL, provedores de segurança do Java, PKCS#11 para HSMs). Integre a PQC acrescentando ou atualizando provedores e configurando os nomes dos algoritmos pela política. As aplicações que chamam interfaces genéricas (Capítulo 9) não precisam de mudanças de código; as que chamam funções específicas de algoritmo precisam.

É aqui que a refatoração com `Signer` compensa: o serviço de documentos eletrônicos da BPA precisa apenas de um novo provedor e de uma entrada na política, enquanto os serviços que ainda chamam funções específicas de algoritmo precisam, cada um, de mudanças de código. O CBOM registra o padrão que cada aplicação usa, o que transforma uma estimativa vaga de esforço numa contagem de itens de trabalho.

### 28.3 Identificadores e codificações

A interoperabilidade depende de identificadores exatos: codepoints do TLS (0x11EC para o X25519MLKEM768 no [registro da IANA](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml)), identificadores de objeto X.509 para as chaves ML-DSA e ML-KEM e codificações de chave (semente versus chave expandida). As incompatibilidades causam falhas que parecem defeitos de rede.

Um codepoint errado faz o servidor ignorar o compartilhamento do cliente, de modo que a conexão cai para o fallback ou falha, o que um engenheiro pode diagnosticar erradamente como problema de firewall. Os testes de interoperabilidade, portanto, comparam identificadores e codificações com o registro e as normas antes de verificar qualquer outra coisa.

### 28.4 Assinaturas com estado

A assinatura com LMS/XMSS nunca pode reutilizar um índice de chave de uso único. Controles: assinar num HSM que imponha estado monotônico; reservar faixas de índices por assinante; proibir a restauração do estado a partir de backups; monitorar a capacidade de assinatura restante (a [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) exige geração de chaves e assinatura em módulo de hardware para esses esquemas). Se esses controles forem inviáveis, prefira o SLH-DSA, sem estado, ou o ML-DSA.

Para o firmware dos guindastes da BPA, uma chave de 2^15 assinaturas com algumas versões por ano nunca se esgota, então o monitoramento da capacidade é uma formalidade; o controle real é a recusa do HSM em retroceder o estado.

### 28.5 Exemplo resolvido

A BPA integra o ML-DSA-65 para os conhecimentos de embarque. O serviço de assinatura usa um HSM via PKCS#11; os verificadores nos sistemas dos parceiros usam outra biblioteca. Os testes de interoperabilidade revelam que uma biblioteca esperava um formato de chave privada expandida — irrelevante para os verificadores, mas impedindo a importação da chave num HSM de backup. Solução: padronizar o armazenamento das chaves em forma de semente e testar a importação/exportação nos dois HSMs antes da produção.

O problema só teria aparecido durante uma recuperação de desastre, quando o HSM de backup fosse necessário, que é o pior momento para descobri-lo. Testar a importação e a exportação antes da produção transformou uma interrupção futura numa decisão de configuração.

### 28.6 Erros comuns e limites

- Misturar implementações de rascunho e finais dos algoritmos.
- Assinatura em software para esquemas com estado.
- Supor que os identificadores coincidem entre fornecedores.

O código Kyber ou Dilithium de rascunho não interopera com o ML-KEM ou o ML-DSA finais, então misturá-los causa falhas que parecem aleatórias. A assinatura só em software para LMS ou XMSS não consegue garantir que o estado nunca seja reutilizado, e a SP 800-208 exige um módulo de hardware. Os identificadores e as codificações dos fornecedores precisam ser verificados em testes, como mostrou o problema da chave expandida; um teste que importa cada chave nos dois HSMs detecta isso cedo.

### Nota de engenharia

Planeje os formatos de chaves e certificados pensando na migração. Guarde as chaves privadas ML-KEM e ML-DSA como sementes onde a norma e o módulo permitirem, porque as sementes são compactas e se expandem de forma determinística, o que simplifica o backup e a migração entre HSMs. Registre no CBOM a codificação que cada sistema usa, teste a exportação e a importação entre cada par de módulos antes da produção e mantenha um procedimento escrito para as cerimônias de chaves que nomeie o conjunto de parâmetros, a codificação, a versão do firmware do módulo e as testemunhas.

### Exercícios

- **EX055 — Lista para escolher biblioteca.** Escreva uma lista de verificação para selecionar uma biblioteca de PQC. Rubrica: 3 = versões finais das FIPS, tempo constante, KATs, manutenção, validação.
- **EX056 — Plano de estado.** Projete a gestão de estado do LMS para dois locais de assinatura. Rubrica: 3 = particionamento de índices, sem retrocesso, monitoramento da capacidade.

### Síntese

Implemente a PQC por meio de provedores verificados e validados, identificadores e codificações exatos e uma gestão rigorosa do estado nas assinaturas com estado.

<!-- open-cyber-academy:chapter-navigation:start ch-28 -->
### Continue estudando — capítulo 28 de 50

[← Capítulo 27](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Segurança quântica e pós-quântica: medição

### Objetivos de aprendizagem

Você vai (1) construir e consultar um CBOM; (2) medir os algoritmos negociados versus os configurados; (3) relatar a cobertura e a parcela desconhecida; e (4) projetar métricas resistentes à manipulação. O capítulo parte dos Capítulos 17 e 22.

### 29.1 Fontes de evidência

As evidências de inventário vêm da varredura de código, da análise de configuração, da observação passiva de handshakes na rede, dos logs dos endpoints e das declarações dos fornecedores. Cada fonte vê coisas diferentes: o código mostra a intenção, a configuração mostra o que é oferecido, a observação passiva mostra o que é negociado e os fornecedores declaram o que fazem os produtos fechados. Combine-as e registre a fonte de cada constatação.

Onde as fontes discordam, a discordância é ela própria uma constatação: se a configuração oferece o grupo híbrido, mas a observação passiva nunca o vê negociado, algo no caminho o está removendo ou os clientes não o oferecem.

### 29.2 Atividade prática — Laboratório I

```python
# Lab I (ch 29): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("gateway-1", "key-exchange", "X25519MLKEM768", "passive"), ("gateway-1", "signature", "RSA-2048", "config"),
    ("scada-hmi", "key-exchange", "ECDHE-P256", "passive"), ("scada-hmi", "signature", "ECDSA-P256", "code"),
    ("billing", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("crane-plc", "unknown", "unknown", "none"), ("vpn", "key-exchange", "ECDHE-P384", "config")]
VULN = {"RSA-2048", "ECDHE-P256", "ECDSA-P256", "RSA-kex", "ECDHE-P384"}
assets = {r[0] for r in records}
unknown = {r[0] for r in records if r[2] == "unknown"}
vuln = [r for r in records if r[2] in VULN]
print(f"assets {len(assets)}, unknown {len(unknown)} ({100*len(unknown)/len(assets):.0f}%)")
print(f"quantum-vulnerable uses {len(vuln)}:", ", ".join(f"{a}/{f}" for a, f, _, _ in vuln))
print("hybrid key exchange present on:", [r[0] for r in records if "MLKEM" in r[2]])
```

Saída esperada:

```text
assets 5, unknown 1 (20%)
quantum-vulnerable uses 5: gateway-1/signature, scada-hmi/key-exchange, scada-hmi/signature, billing/key-exchange, vpn/key-exchange
hybrid key exchange present on: ['gateway-1']
```

O estado desconhecido do CLP do guindaste é uma constatação, não uma lacuna a esconder: ele representa 20% deste inventário minúsculo e precisa ser resolvido por declaração do fornecedor ou por análise em bancada.

Note como o script conta usos, e não ativos: o gateway-1 tem troca de chaves híbrida, mas ainda aparece como vulnerável, porque a sua assinatura é RSA-2048, o que coincide com o ponto anterior de que a troca de chaves híbrida deixa a autenticação intocada. O AES-256-GCM do sistema de faturamento fica corretamente fora da lista de vulneráveis. Amplie os registros com um filtro pela coluna de fonte e imprima quantas constatações se apoiam apenas na configuração; depois acrescente um sexto ativo cuja fonte seja uma declaração do fornecedor e decida como relatá-lo.

### 29.3 Métricas

- **Cobertura**: ativos com pelo menos uma determinação criptográfica ÷ todos os ativos.
- **Parcela desconhecida**: relatada separadamente.
- **Parcela híbrida negociada**: conexões que negociam grupos PQ/T ÷ conexões, ponderada pela classe de dados.
- **Contagem de usos vulneráveis**, por função e tempo de vida dos dados.
- **Tempo de substituição**: dias decorridos entre a mudança de política e a negociação completa de um novo algoritmo num serviço (uma métrica de agilidade).

Ponderar a parcela híbrida pela classe de dados impede que um grande volume de telemetria de vida curta faça o progresso parecer melhor do que é para os dados aduaneiros. O tempo de substituição é a única métrica que mede diretamente a agilidade, e o exercício de mesa de quebra de algoritmo, mais adiante no livro, a utiliza. Cada métrica tem uma definição e uma fonte de dados escritas.

### 29.4 Manipulação

A "porcentagem migrada" pode ser inflada redefinindo os ativos ou contando a configuração em vez da negociação. Use denominadores auditáveis e publique as definições.

Uma inflação comum é retirar da lista de ativos os dispositivos difíceis de inventariar, o que eleva a cobertura sem nenhum conhecimento novo. A BPA fixa o denominador no registro de ativos mantido pelas operações, que a equipe de segurança não pode editar, e conta apenas os grupos negociados vistos nos logs de sessão. As definições são publicadas junto com cada número mensal, para que qualquer mudança de definição apareça como uma nota visível, e não como um salto inexplicado na linha de tendência.

### 29.5 Exemplo resolvido

O primeiro relatório do CBOM da BPA: 412 ativos, cobertura de 82%, desconhecidos 18%, 311 usos vulneráveis, negociação híbrida de 0% (antes da implantação). Seis meses depois: cobertura de 94%, desconhecidos 6%, negociação híbrida em 64% das conexões de borda, usos vulneráveis sobre dados de vida longa reduzidos de 37 fluxos para 8.

Os números contam uma história coerente: a cobertura subiu à medida que os desconhecidos caíram, e a redução de 37 fluxos expostos para 8 reflete a mudança nos quatro gateways encontrada pelo modelo, que removeu 29 deles. A negociação híbrida em 64% das conexões de borda, e não em 100%, é esperada, porque os scanners antigos e alguns clientes dos parceiros não oferecem o grupo híbrido; o relatório os lista como exceções conhecidas, com datas de substituição.

### 29.6 Erros comuns e limites

- Esconder os desconhecidos.
- Contar os algoritmos configurados como proteção.
- Inventários de uma só fonte.

Esconder os desconhecidos faz o inventário parecer completo enquanto sistemas como o CLP do guindaste continuam sem avaliação; o Laboratório I os relata como 20% para que não possam ser ignorados. Contar os algoritmos configurados superestima a proteção sempre que clientes ou middleboxes impedem a negociação. Um inventário construído com uma única fonte deixa escapar o que essa fonte não consegue ver, como bibliotecas ligadas estaticamente, invisíveis às varreduras de pacotes de software, ou equipamentos de fornecedores, invisíveis à varredura de código. A BPA exige pelo menos duas fontes para qualquer ativo que guarde dados de vida longa.

### Nota de engenharia

Apresente as medições com os seus pontos cegos. Os sensores passivos no TLS 1.3 veem o grupo de troca de chaves negociado no ServerHello, mas não o certificado, que é cifrado; os logs dos endpoints preenchem essa lacuna, mas só onde o registro está ativado. Um bom painel mostra, portanto, ao lado de cada métrica, qual fonte a produziu e que parcela dos ativos essa fonte consegue observar. Os tomadores de decisão entendem então por que os números da migração de certificados vêm de evidências de configuração, enquanto os números da troca de chaves vêm da rede.

### Exercícios

- **EX057 — Ampliar o Laboratório I.** Acrescente um registro de uma VPN com "IKEv2 ML-KEM-768 + ECDH" e atualize a lógica da lista de híbridos. Rubrica: 3 = o código funciona, a VPN é reconhecida como híbrida.
- **EX058 — Definições de métricas.** Escreva definições precisas para a cobertura e a parcela híbrida negociada. Rubrica: 3 = numerador, denominador, janela de tempo, fonte de dados.

### Síntese

Medir significa um CBOM de várias fontes, métricas do negociado e não do configurado, desconhecidos explícitos e definições que resistem à manipulação.

<!-- open-cyber-academy:chapter-navigation:start ch-29 -->
### Continue estudando — capítulo 29 de 50

[← Capítulo 28](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) verificar implementações com testes de resposta conhecida; (2) escrever testes negativos para entradas malformadas; (3) testar a interoperabilidade entre bibliotecas; e (4) registrar as evidências de verificação. O capítulo parte dos Capítulos 9, 28 e 29.

### 30.1 Testes de resposta conhecida

Os testes de resposta conhecida (KATs) alimentam entradas fixas e comparam as saídas com valores publicados. Os organismos de normalização e o Cryptographic Algorithm Validation Program do NIST publicam vetores; para o ML-KEM, modos de teste determinísticos permitem fixar a aleatoriedade para que as saídas possam ser comparadas byte a byte.

Os modos determinísticos existem apenas para testes; o código de produção precisa usar aleatoriedade nova, e uma verificação de build garante que os ganchos de teste não sejam alcançáveis nas versões de produção. A BPA executa a suíte de vetores a cada atualização de biblioteca e bloqueia a atualização se algum vetor falhar, o que detecta regressões como as mudanças da codificação do ML-KEM entre o rascunho e a versão final.

### 30.2 Atividade prática — Laboratório V

```python
# Lab V (ch 30): known-answer and negative tests - the habit behind validating PQC libraries.
import hashlib
KATS = [  # (function, input, expected hex prefix) - published test values for SHA-3 / SHAKE on empty input
    ("sha3_256", b"", "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"),
    ("shake_128/32", b"", "7f9c2ba4e88f827d616045507605853ed73b8093f6efbc88eb1a6eacfa66ef26"),
]
def run(name, data):
    if name == "sha3_256": return hashlib.sha3_256(data).hexdigest()
    return hashlib.shake_128(data).hexdigest(32)
for name, data, want in KATS:
    print(f"KAT {name:13s}", "PASS" if run(name, data) == want else "FAIL")
SIZES = {"ML-KEM-512": 800, "ML-KEM-768": 1184, "ML-KEM-1024": 1568}   # encapsulation-key bytes, FIPS 203
def validate_ek(param, ek):
    if len(ek) != SIZES[param]: raise ValueError(f"{param}: expected {SIZES[param]} bytes, got {len(ek)}")
    return True
for param, n in [("ML-KEM-768", 1184), ("ML-KEM-768", 1183), ("ML-KEM-512", 1184)]:
    try: validate_ek(param, bytes(n)); print(f"negative/positive test {param} len {n}: accepted")
    except ValueError as e: print(f"negative/positive test {param} len {n}: rejected ({e})")
```

Saída esperada:

```text
KAT sha3_256      PASS
KAT shake_128/32  PASS
negative/positive test ML-KEM-768 len 1184: accepted
negative/positive test ML-KEM-768 len 1183: rejected (ML-KEM-768: expected 1184 bytes, got 1183)
negative/positive test ML-KEM-512 len 1184: rejected (ML-KEM-512: expected 800 bytes, got 1184)
```

O validador de comprimento é só a primeira verificação: a FIPS 203 também exige verificar que os coeficientes codificados de uma chave de encapsulamento estão abaixo de *q* (a verificação de módulo) e uma verificação de hash nas chaves de desencapsulamento. As bibliotecas reais implementam isso; os seus testes devem confirmar que elas rejeitam chaves ruins.

O terceiro caso de teste é o importante: uma chave ML-KEM-768 de tamanho correto apresentada como ML-KEM-512 precisa ser rejeitada, porque um interpretador que confia no comprimento da chave para escolher o conjunto de parâmetros pode ser conduzido por um atacante.

### 30.3 Interoperabilidade

Execute handshakes entre cada par de implementações de cliente e servidor no escopo; encapsule com uma biblioteca e desencapsule com outra; assine com o HSM e verifique no software dos parceiros. Registre a matriz. As falhas de interoperabilidade no início do programa são baratas; em produção, são interrupções.

Testar uma biblioteca apenas contra ela mesma prova pouco, já que um bug de codificação de um lado é espelhado do outro e se anula. Pares de implementações diferentes expõem essas incompatibilidades. A matriz também registra as versões, então, quando uma biblioteca é atualizada, apenas as linhas afetadas são refeitas.

### 30.4 Evidências

Cada execução de teste registra: implementação e versão, vetores de teste usados, resultado, data, operador. As evidências alimentam a coluna de verificação da matriz de rastreabilidade (Capítulo 21).

As evidências precisam ser reprodutíveis: outro engenheiro deve conseguir refazer o mesmo teste com as mesmas versões e vetores e obter o mesmo resultado. A BPA guarda a configuração do teste junto com o resultado, então um auditor que pergunta como o REQ-KE-01 foi verificado recebe a consulta, a sua saída e a data, e não uma afirmação de que os testes foram feitos. Resultados mais antigos que a versão atual da biblioteca são marcados como vencidos e refeitos antes da versão.

### 30.5 Exemplo resolvido

A matriz de interoperabilidade da BPA para o TLS de borda: três pilhas de servidor × cinco famílias de clientes. Duas falhas: uma biblioteca antiga de um parceiro oferecia o codepoint obsoleto de antes da norma e não conseguia concluir handshakes híbridos; um balanceador de carga removia grupos desconhecidos. As duas recebem itens de trabalho; nenhuma bloqueia a implantação, porque o fallback para o X25519 funciona e é registrado.

O codepoint obsoleto pertence a uma implementação de rascunho do Kyber, e é por isso que os pares com o ML-KEM final não conseguem concluir o handshake; o parceiro precisa atualizar a biblioteca. O problema do balanceador de carga é mais sério, porque afeta todo o tráfego que passa por ele, então a sua correção é agendada antes que a implantação avance por esse caminho.

### 30.6 Erros comuns e limites

- Apenas testes positivos.
- Testar uma biblioteca contra ela mesma.
- Resultados não registrados.

Testes positivos sozinhos aprovariam um validador que aceita qualquer chave, enquanto os casos de rejeição do Laboratório V mostram que o validador realmente discrimina. Testar uma biblioteca contra ela mesma esconde incompatibilidades de codificação, que só aparecem quando há uma implementação diferente do outro lado, como mostrou a falha do codepoint obsoleto. Resultados não registrados não podem sustentar a matriz de rastreabilidade, então um teste aprovado que ninguém anotou não vale nada na revisão. O pipeline da BPA guarda cada execução com versões e vetores.

### Nota de engenharia

As evidências de verificação devem poder ser reproduzidas por outra pessoa. Guarde os vetores de teste exatos, as versões das ferramentas e as linhas de comando junto com os resultados e refaça a suíte automaticamente sempre que mudar uma biblioteca, um provedor ou o firmware de um HSM. Quando um fornecedor publicar um alerta de segurança, a equipe poderá então responder em horas se a versão afetada está implantada e se os seus testes ainda passam, em vez de reconstruir a verificação original de memória e por capturas de tela.

### Exercícios

- **EX059 — Testes negativos.** Liste cinco testes negativos para uma função de desencapsulamento ML-KEM. Rubrica: 3 = comprimento errado, texto cifrado modificado, chave errada, chave malformada, coerência de chamadas repetidas.
- **EX060 — Matriz de interoperabilidade.** Projete a matriz de interoperabilidade para as assinaturas dos conhecimentos de embarque da BPA. Rubrica: 3 = assinantes, verificadores, formatos, resultados esperados.

### Síntese

A verificação combina testes de resposta conhecida, testes negativos e interoperabilidade entre implementações, tudo registrado como evidência rastreada até os requisitos.

<!-- open-cyber-academy:chapter-navigation:start ch-30 -->
### Continue estudando — capítulo 30 de 50

[← Capítulo 29](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Segurança quântica e pós-quântica: implementação II

### Objetivos de aprendizagem

Você vai (1) aplicar técnicas de tempo constante ao código baseado em reticulados; (2) entender os ataques por injeção de falhas e as suas contramedidas; (3) lidar com segurança com a aleatoriedade e as sementes; e (4) avaliar implementações embarcadas. O capítulo aprofunda o Capítulo 28 com a segurança da implementação.

### 31.1 Tempo constante

As implementações baseadas em reticulados precisam evitar desvios, acessos à memória e instruções de tempo variável que dependam de segredos. A divisão é uma armadilha conhecida: compiladores e processadores podem implementar a divisão por uma constante com tempo variável, e o KyberSlash mostrou vazamentos reais a partir de divisões dependentes de segredos ([Bernstein et al. 2024](https://eprint.iacr.org/2024/1049)). A correção é uma aritmética que evite a divisão (multiplicação por constantes pré-calculadas e deslocamentos) e a verificação com ferramentas de análise de tempo.

Um código-fonte que parece de tempo constante pode deixar de sê-lo após a compilação, por isso as verificações são executadas sobre o binário de cada plataforma-alvo.

### 31.2 Comparação no desencapsulamento

A rejeição implícita do ML-KEM compara um texto cifrado recifrado com o recebido. A comparação e a seleção entre a chave real e a chave de rejeição precisam ser de tempo constante; caso contrário, o tempo revela se um texto cifrado manipulado foi decifrado "corretamente", reabrindo os ataques de texto cifrado escolhido.

Uma comparação ingênua que para no primeiro byte diferente termina mais cedo para algumas entradas do que para outras, e um atacante que envia muitos textos cifrados forjados consegue medir a diferença. A correção compara todos os bytes e combina as diferenças com operações bit a bit, e depois seleciona a chave com uma máscara em vez de um desvio. As bibliotecas implementam isso; a revisão da BPA verifica que o código da aplicação nunca reimplemente a comparação nem acrescente uma saída antecipada em torno dela.

### 31.3 Ataques por injeção de falhas

Injetar falhas (picos de tensão, falhas de clock, lasers) pode pular verificações ou corromper cálculos. Nas assinaturas, uma falha durante a assinatura ML-DSA pode vazar informações sobre a chave secreta; nos esquemas determinísticos, as falhas podem ser especialmente perigosas. As contramedidas incluem o cálculo redundante, a verificação de uma assinatura antes de liberá-la e hardware reforçado. Elas importam para dispositivos aos quais um atacante tem acesso físico — scanners de portão, cartões inteligentes.

Verificar uma assinatura antes de liberá-la custa uma verificação a mais, o que no ML-DSA é rápido, e detecta falhas que corromperam a assinatura. Para o serviço central de assinatura da BPA, numa sala protegida, o risco de falhas é baixo; para dispositivos em campo, um atacante com acesso físico tem tempo para experimentar, então é ali que as contramedidas importam mais.

### 31.4 Aleatoriedade e sementes

A geração de chaves e o encapsulamento do ML-KEM consomem aleatoriedade nova; o ML-DSA oferece um modo "hedged" que mistura aleatoriedade nova com derivação determinística, o que ajuda contra falhas injetadas e falhas de aleatoriedade ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)). As sementes que geram chaves são tão sensíveis quanto as próprias chaves.

Num esquema hedged, um gerador de números aleatórios com defeito degrada para a assinatura determinística em vez de vazar a chave, e é por isso que a BPA ativa o ML-DSA hedged no seu serviço de assinatura. As sementes de 64 bytes do ML-KEM precisam ser protegidas como chaves privadas: quem obtém uma semente pode regenerar a chave de desencapsulamento. As regras de armazenamento e de backup se aplicam às sementes da mesma forma, inclusive a destruição quando a chave é aposentada.

### 31.5 Exemplo resolvido

O fornecedor dos scanners de portão da BPA fornece um verificador ML-DSA para o firmware. Como o dispositivo apenas verifica, o vazamento da chave secreta não está em jogo no dispositivo; os principais riscos são falhas que pulem o resultado da verificação. Contramedida: verificar duas vezes, por caminhos de código diferentes, e conferir um hash da imagem após o boot.

Usar dois caminhos de código diferentes significa que é improvável que uma única falha injetada pule as duas verificações da mesma forma. A conferência do hash após o boot acrescenta mais uma camada: se uma falha deixou uma imagem não assinada iniciar, a divergência é detectada e o dispositivo a relata. Essas etapas custam milissegundos no boot, o que o scanner pode pagar.

### 31.6 Erros comuns e limites

- Supor que os compiladores preservam a intenção de tempo constante.
- Ignorar ataques físicos contra dispositivos em campo.
- Tratar as sementes como não sensíveis.

Os compiladores otimizam para velocidade e podem introduzir desvios ou consultas a tabelas que vazam tempo, então as alegações de tempo constante precisam ser verificadas no código compilado. Dispositivos em campo, como os scanners de portão, enfrentam atacantes que podem injetar falhas neles à vontade, ao contrário dos servidores numa sala vigiada. As sementes regeneram chaves, então tratá-las como configuração inofensiva expõe todas as chaves derivadas delas. As revisões da BPA verificam esses três pontos em cada nova classe de dispositivo antes da compra.

### Exercícios

- **EX061 — Auditoria de divisão.** Explique por que `coeff // 1665` sobre um valor secreto pode vazar informação e proponha uma alternativa. Rubrica: 3 = risco da divisão de tempo variável e alternativa com multiplicação/deslocamento.
- **EX062 — Ameaça de falhas.** Para um bootloader que apenas verifica, identifique a ameaça de falhas e duas contramedidas. Rubrica: 3 = verificação pulada; verificação redundante e hash após o boot.

### Síntese

A segurança da implementação em PQC significa aritmética e comparações de tempo constante, resistência a falhas onde os atacantes têm acesso físico e cuidado no tratamento da aleatoriedade e das sementes.

<!-- open-cyber-academy:chapter-navigation:start ch-31 -->
### Continue estudando — capítulo 31 de 50

[← Capítulo 30](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Segurança quântica e pós-quântica: confiabilidade

### Objetivos de aprendizagem

Você vai (1) identificar os riscos de confiabilidade trazidos por mensagens maiores e novos caminhos de código; (2) projetar um comportamento de fallback e de novas tentativas que preserve a segurança; (3) planejar a capacidade dos esquemas de assinatura com estado; e (4) monitorar falhas silenciosas. O capítulo parte dos Capítulos 23 e 30.

### 32.1 Riscos de confiabilidade

Riscos novos: fragmentação e descartes por middleboxes; timeouts em dispositivos restritos e lentos; falhas na interpretação de certificados; bugs de biblioteca em código novo; chaves de assinatura com estado esgotadas; limites de desempenho dos HSMs. Cada um precisa de detecção e de resposta.

Cada risco tem um sinal correspondente: os descartes aparecem como falhas de handshake por caminho, os timeouts como caudas de latência em classes de dispositivos, as falhas de interpretação como erros de certificado nos logs dos clientes e as chaves com estado esgotadas como um contador se aproximando do limite. O plano de monitoramento da BPA lista o sinal, o limiar e o responsável por cada risco, para que um alerta chegue a alguém que sabe o que fazer, e não a uma fila genérica.

### 32.2 Fallback seguro

O fallback pode preservar a disponibilidade, mas não pode criar um rebaixamento silencioso. Regras de projeto: fallback apenas para algoritmos aprovados; registrar cada fallback com o motivo; alertar quando as taxas de fallback subirem; definir uma data de expiração para a permissão de fallback; nunca fazer fallback em falhas de autenticação, apenas em incompatibilidade demonstrável.

A última regra é crítica: uma falha de autenticação pode sinalizar um ataque, então tentar de novo com configurações mais fracas daria ao atacante o que ele quer. O portal da BPA, por isso, só faz fallback após um reset de conexão num caminho listado como incompatível, nunca após um erro de certificado ou de assinatura.

### 32.3 Capacidade dos esquemas com estado

Uma chave LMS com árvore de altura 20 suporta cerca de um milhão de assinaturas; uma árvore de altura 10, cerca de mil. A capacidade precisa exceder, com margem, o volume de assinaturas esperado ao longo da vida da chave; alertas de monitoramento em limiares (por exemplo, 70% usados) disparam uma troca de chave planejada.

A altura da árvore troca capacidade por tempo de geração da chave e tamanho da assinatura: cada nível a mais dobra a capacidade e acrescenta um pouco a cada assinatura. Como a troca de chave exige distribuir antecipadamente uma nova chave pública aos dispositivos, o limiar de alerta precisa deixar assinaturas restantes suficientes para cobrir esse período de distribuição.

### 32.4 Falhas silenciosas

A pior falha de confiabilidade é a segurança desativada em silêncio: uma configuração que, por causa de um erro de digitação, faz fallback para apenas o clássico em todo lugar. Monitorar os grupos negociados (Capítulo 29) detecta isso.

A BPA se protege disso com uma verificação diária que compara a parcela híbrida negociada com a da semana anterior; uma queda repentina para perto de zero dispara um alerta mesmo que nenhuma conexão tenha falhado. As mudanças de configuração na política criptográfica também exigem um segundo revisor, o que detecta erros de digitação antes da implantação. Uma falha silenciosa não pode ser vista nos logs de erro, porque nada dá erro; ela só pode ser detectada medindo o que é negociado.

### 32.5 Exemplo resolvido

A BPA assina cerca de 2.000 imagens de firmware por ano, somando todas as famílias de dispositivos. Uma árvore LMS de altura 15 (32.768 assinaturas) por local de assinatura dura mais de uma década no volume atual; a equipe ainda assim define alertas em 50% e 80% e documenta a troca para uma nova chave, com distribuição antecipada da sua chave pública.

A 2.000 assinaturas por ano, uma árvore de 32.768 assinaturas dura cerca de dezesseis anos por local, e é por isso que a capacidade não é a restrição. Os alertas ainda importam, porque o volume pode mudar, por exemplo se uma nova família de dispositivos for acrescentada. Distribuir cedo a próxima chave pública significa que a troca de chave não exige nenhuma atualização de firmware emergencial.

### 32.6 Erros comuns e limites

- Fallback sem registro nem expiração.
- Chaves com estado subdimensionadas.
- Monitorar a configuração em vez da negociação.

Um fallback sem registro e sem expiração transforma uma ferramenta de transição num caminho permanente de rebaixamento. Uma chave LMS pequena demais se esgota antes que os dispositivos possam receber uma nova chave pública, deixando sem nenhuma forma de assinar atualizações. Monitorar a configuração em vez da negociação deixa escapar as falhas silenciosas descritas acima, em que tudo parece ativado, mas nada está protegido. Cada um desses erros foi visto nas primeiras implantações de outras organizações, e é por isso que o plano da BPA nomeia um controle para cada um.

### Nota de engenharia

As revisões de confiabilidade também devem cobrir relógios e expirações. Certificados de transição, PSKs com datas de rotação e permissões de fallback expiram por projeto; se a automação de renovação falhar, o resultado é uma interrupção que parece uma falha criptográfica. Registre as expirações no sistema de monitoramento, com alertas a 30, 14 e 3 dias, e teste os caminhos de renovação no ambiente réplica, porque a primeira renovação do certificado de um algoritmo novo é um lugar clássico para aparecerem incompatibilidades de interpretação ou de política.

### Exercícios

- **EX063 — Política de fallback.** Escreva uma política de fallback para o TLS de borda que satisfaça as regras de 32.2. Rubrica: 3 = as cinco regras incorporadas.
- **EX064 — Capacidade.** Um local assina 15 documentos por minuto, continuamente, com LMS. Uma árvore de altura 20 basta para um ano? Rubrica: 3 = 7,9 milhões de assinaturas/ano > 1.048.576 — não basta; propõe HSS/várias árvores ou ML-DSA.

### Síntese

A engenharia de confiabilidade em PQC antecipa falhas de tamanho e de caminhos de código, projeta um fallback registrado, com expiração e seguro quanto à autenticação, dimensiona as chaves com estado com margem e monitora os resultados negociados.

<!-- open-cyber-academy:chapter-navigation:start ch-32 -->
### Continue estudando — capítulo 32 de 50

[← Capítulo 31](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Segurança quântica e pós-quântica: segurança operacional e resiliência

### Objetivos de aprendizagem

Você vai (1) analisar como a migração criptográfica interage com as operações relacionadas à segurança física (safety); (2) projetar implantações resilientes para a tecnologia operacional do porto; (3) planejar a resposta a incidentes criptográficos, incluindo o comprometimento de um algoritmo; e (4) preparar-se para um cenário de "quebra criptográfica". O capítulo parte dos Capítulos 10, 23 e 32.

### 33.1 Interações com a segurança física

Na BPA, guindastes, sistemas de portão e serviços de tráfego de embarcações precisam continuar operando. Uma verificação de assinatura de firmware que falha pode inutilizar o controlador de um guindaste; um certificado rejeitado por um scanner de portão pode parar caminhões. As etapas de migração nesses sistemas exigem testes em unidades reserva, janelas de manutenção, imagens de reversão verificadas e a aprovação dos operadores.

A aprovação dos operadores importa porque eles conhecem as consequências de um guindaste ou de um portão parado num período de pico melhor do que a equipe de segurança. A BPA agenda as mudanças de assinatura de firmware fora dos picos de chegada de navios e mantém um técnico no local durante a atualização da primeira unidade. Se a verificação falhar na unidade reserva, a implantação para ali, antes que qualquer guindaste em operação seja tocado.

### 33.2 Implantação resiliente

Use anéis: laboratório → unidade reserva → uma unidade de baixo impacto → um local → todos. Cada anel tem um período de espera e critérios de sucesso explícitos. Mantenha a chave de verificação anterior como confiável até que a nova cadeia esteja comprovada, para que a reversão continue possível.

Para os controladores de guindaste, o período de espera é de uma semana de operação normal por anel, e sucesso significa nenhuma falha de verificação e nenhuma reinicialização inexplicada. Manter a chave antiga como confiável custa pouco e preserva um caminho de volta caso a nova cadeia tenha um defeito. Ela só é removida depois que todos os dispositivos tiverem executado a nova cadeia com sucesso.

### 33.3 Resposta a incidentes criptográficos

Planeje para: uma vulnerabilidade numa biblioteca PQC (corrigir e trocar as chaves), um comprometimento de chave (revogar e substituir), uma reutilização de índice de uma chave com estado (tratar como comprometimento) e uma quebra criptoanalítica de um algoritmo (mudar para a alternativa). Os híbridos dão tempo no último caso: se o ML-KEM fosse enfraquecido, o X25519 ainda protegeria contra atacantes clássicos enquanto a agilidade substitui o componente pós-quântico — por exemplo, pelo HQC, quando for padronizado ([IR 8545](https://doi.org/10.6028/NIST.IR.8545)).

Cada cenário tem um responsável, uma primeira ação e um tempo-alvo no plano da BPA.

### 33.4 Exercício de mesa: quebra de algoritmo

Cenário: um artigo confiável relata um ataque prático contra um conjunto de parâmetros de assinatura pós-quântica. Perguntas: onde ele é usado (CBOM)? O que depende dele (raízes, firmware)? Qual é a alternativa (SLH-DSA, outro nível do ML-DSA)? Quanto tempo leva a substituição (métrica de tempo de substituição)? Quem decide? O exercício de mesa mede a agilidade diretamente.

Conduzir o exercício com o CBOM aberto transforma cada pergunta numa consulta, e o tempo gasto para responder mostra onde o inventário é fraco. Se ninguém consegue dizer em uma hora quais dispositivos dependem do conjunto de parâmetros afetado, essa lacuna é a principal constatação.

### 33.5 Exemplo resolvido

O exercício de mesa da BPA descobre que o firmware dos guindastes confia em um único algoritmo de assinatura, sem previsão de uma segunda chave no bootloader. Ação: a próxima versão do bootloader aceita duas chaves de verificação de algoritmos diferentes (por exemplo, LMS e ML-DSA), para que a quebra de um deles não deixe os dispositivos sem saída.

Sem a segunda chave, uma quebra do LMS deixaria dispositivos impossíveis de atualizar, sem caminho confiável para receber uma correção, já que qualquer firmware novo precisaria de uma assinatura que o bootloader não consegue verificar com segurança. Acrescentar a segunda chave agora, enquanto o bootloader ainda pode ser atualizado, preserva opções para o restante da vida do dispositivo.

### 33.6 Erros comuns e limites

- Implantar mudanças criptográficas em sistemas de segurança física sem unidades reserva e sem reversão.
- Nenhum plano para o comprometimento de um algoritmo.
- Âncoras de confiança de um único algoritmo em dispositivos de vida longa.

Implantar uma mudança de assinatura de firmware nos guindastes sem uma unidade reserva testada e sem imagem de reversão arrisca controladores inutilizados e operações paradas. Sem um plano para o comprometimento de um algoritmo, uma quebra força a improvisação sob pressão. Âncoras de confiança de um único algoritmo em dispositivos com vida útil de dez a vinte anos não deixam alternativa se esse algoritmo falhar, como o exercício de mesa da BPA descobriu no firmware dos guindastes antes da próxima versão do bootloader.

### Exercícios

- **EX065 — Anéis.** Defina os anéis de implantação e os critérios para o firmware de guindaste assinado com um algoritmo novo. Rubrica: 3 = unidades reserva, períodos de espera, reversão.
- **EX066 — Exercício de mesa.** Conduza o exercício de mesa de quebra de algoritmo para os conhecimentos de embarque da BPA e registre as ações. Rubrica: 3 = usa o CBOM, esquema alternativo, tempo de substituição.

### Síntese

A segurança física e a resiliência exigem implantações em anéis com reversão, planos de incidente que incluam quebras de algoritmo e âncoras de confiança capazes de aceitar mais de um algoritmo.

<!-- open-cyber-academy:chapter-navigation:start ch-33 -->
### Continue estudando — capítulo 33 de 50

[← Capítulo 32](#ch-32) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Segurança quântica e pós-quântica: integração

### Objetivos de aprendizagem

Você vai (1) integrar a PQC no TLS, na VPN, na PKI, na assinatura de código e nos formatos de dados; (2) gerenciar a integração com parceiros e fornecedores; (3) sequenciar a integração para gerenciar as dependências; e (4) executar testes de integração de ponta a ponta. O capítulo parte dos Capítulos 16, 28 e 30.

### 34.1 Mapa de integração

| Domínio | Ponto de integração | Dependência |
|---|---|---|
| Web/TLS | CDN, proxy de borda, balanceadores de carga internos | Suporte dos clientes, middleboxes |
| VPN | Gateways IKEv2 | Fornecedores dos pares, suporte ao RFC 9370 |
| PKI | Software da AC, HSM, perfis de certificado | Suporte das partes confiantes |
| Assinatura de código | Serviço de assinatura, bootloaders dos dispositivos | Atualizações de firmware dos dispositivos |
| Documentos | Assinaturas de conhecimentos de embarque, exportações CMS | Software dos parceiros e da aduana |

A coluna de dependência explica a maior parte do cronograma: a BPA controla a sua CDN e o seu proxy de borda, então o TLS web anda primeiro, enquanto os documentos dependem de software dos parceiros e da aduana que a BPA não pode mudar. Ler o mapa linha por linha também mostra quais pontos de integração compartilham uma dependência, como o HSM, que atende tanto a PKI quanto a assinatura de código, de modo que um atraso afeta dois domínios.

### 34.2 Integração com parceiros

Os parceiros andam no próprio ritmo. Publique um aviso de migração com prazos, algoritmos suportados e endpoints de teste; ofereça um ambiente de testes de interoperabilidade; mantenha caminhos clássicos disponíveis, com desativação datada. A aduana, por exemplo, pode aceitar exportações envelopadas com ML-KEM apenas depois da sua própria atualização; destinatários paralelos no CMS (clássico e PQC) cobrem a lacuna.

O ambiente de testes é o item mais útil, porque os parceiros podem testar o seu software contra a nova configuração da BPA sem risco para a produção. As desativações datadas dão aos parceiros um prazo para planejar, e a BPA os lembra em intervalos fixos antes de cada data.

### 34.3 Sequenciamento

Sequencie por dependência e valor: primeiro o TLS de borda (independente, de alto valor); em seguida a raiz da PKI e o HSM (prazo de entrega longo, habilitadores das assinaturas); a assinatura de firmware à medida que os dispositivos são renovados; os documentos com os parceiros; os serviços internos conforme o tempo de vida dos dados.

A raiz da PKI e o HSM vêm cedo, apesar do baixo risco imediato, porque os seus prazos de entrega são longos: a compra, a certificação e a distribuição de uma nova raiz podem levar anos. O TLS de borda vai primeiro porque a BPA controla tanto a configuração quanto a medição, e o seu valor contra a coleta é imediato. A assinatura de firmware acompanha os ciclos de renovação dos dispositivos, e não uma data no calendário. Essa ordem segue as dependências, e não a ordem em que as equipes pediram o trabalho.

### 34.4 Testes de ponta a ponta

Os testes de integração exercitam fluxos inteiros: um cliente de parceiro que se conecta pela borda a uma API que assina um documento com ML-DSA, armazenado e replicado sobre TLS híbrido e verificado por um sistema de testes da aduana. As falhas nesses testes revelam incompatibilidades de interface que nenhum teste unitário encontra.

Por exemplo, um cliente de parceiro pode negociar corretamente o grupo híbrido enquanto a API rejeita o documento assinado, maior, por causa de um limite de tamanho num campo de banco de dados. Só um teste que segue o fluxo completo encontra esse tipo de incompatibilidade entre componentes que passaram, cada um, nos seus próprios testes.

### 34.5 Exemplo resolvido

O plano de integração da BPA tem 14 pacotes de trabalho. Um grafo de dependências mostra que a atualização do HSM condiciona cinco deles; a compra é, portanto, iniciada no mês um, embora as assinaturas só se tornem urgentes no mês nove.

O HSM condiciona cinco pacotes de trabalho porque a PKI, a assinatura de código e a assinatura de documentos precisam dos seus novos tipos de chave. Iniciar a compra no mês um dá cerca de oito meses de prazo antes de as assinaturas se tornarem urgentes, o que corresponde aos atrasos típicos de compra e de certificação. Sem o grafo de dependências, o HSM provavelmente teria sido encomendado quando o trabalho de assinaturas começasse, atrasando cinco pacotes de uma só vez.

### 34.6 Erros comuns e limites

- Integrar os domínios isoladamente.
- Esquecer as datas de desativação dos parceiros.
- Nenhum teste de ponta a ponta.

Integrar os domínios isoladamente deixa escapar os fluxos que os atravessam, como um documento assinado que vai da API, pela replicação, até a aduana. Datas de desativação esquecidas deixam caminhos clássicos abertos indefinidamente, desfazendo a proteção da migração. Sem testes de ponta a ponta, as incompatibilidades de interface surgem em produção como interrupções que cada equipe atribui a outra. O plano da BPA, por isso, nomeia um responsável para cada fluxo entre domínios, mantém um registro de desativações revisado mensalmente e executa o teste completo do parceiro à aduana antes de cada mudança importante.

### 34.7 Lista de verificação de prontidão para integração

Antes de a BPA mudar um enlace com um parceiro para troca de chaves híbrida, o responsável pela integração confirma quatro itens: a pilha do parceiro anuncia o mesmo grupo híbrido, os dois lados registram o grupo negociado, um fallback clássico continua permitido apenas onde a lista de exceções acordada o permite, e uma janela de testes conjunta está reservada, com um contato de reversão em cada lado. Um enlace que falha em qualquer item permanece na configuração atual e é reagendado, em vez de forçado.

Reagendar custa alguns dias; forçar um enlace que falhou custa a confiança do parceiro.

### Exercícios

- **EX067 — Grafo de dependências.** Desenhe (ou liste) o grafo de dependências dos 5 domínios da BPA. Rubrica: 3 = dependências do HSM e dos parceiros visíveis.
- **EX068 — Aviso aos parceiros.** Escreva um aviso de migração para os parceiros das companhias de navegação. Rubrica: 3 = algoritmos, endpoints de teste, cronograma, desativação, contato.

### Síntese

A integração abrange protocolos, PKI, assinaturas e documentos; os parceiros precisam de avisos e ambientes de testes; o sequenciamento segue as dependências; os testes de ponta a ponta detectam incompatibilidades de interface.

<!-- open-cyber-academy:chapter-navigation:start ch-34 -->
### Continue estudando — capítulo 34 de 50

[← Capítulo 33](#ch-33) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 35 →](#ch-35)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) projetar a autenticação pós-quântica de um ecossistema de documentos e firmware; (2) escolher entre ML-DSA, SLH-DSA e assinaturas baseadas em hash com estado; (3) projetar a validação de longo prazo com carimbos de tempo; e (4) defender o projeto diante de uma banca. O capítulo integra os Capítulos 26–34.

### 35.1 Enunciado

Projete assinaturas pós-quânticas para (a) os conhecimentos de embarque eletrônicos da BPA, verificáveis por 12 anos por parceiros e tribunais, e (b) o firmware de 3.000 dispositivos de campo, com vida útil de 10–20 anos e bootloaders restritos. Restrições: o software de verificação dos parceiros varia; alguns dispositivos não podem ser atualizados além de mais uma versão do bootloader.

As duas partes diferem na sua restrição principal. Os conhecimentos de embarque precisam ser verificáveis por tribunais e parceiros com software que a BPA não controla, então a compatibilidade e a evidência de longo prazo são o que mais importa. Os dispositivos de firmware podem receber apenas mais uma atualização de bootloader, então o que for escolhido agora precisa durar o restante da vida do dispositivo. As equipes que tratam as duas partes como um único problema costumam escolher um único algoritmo que não serve bem a nenhuma delas.

### 35.2 Esboço da solução de referência

(a) Conhecimentos de embarque: assinar com ML-DSA-65 ao lado da assinatura ECDSA existente durante a transição (assinaturas duplas no formato do documento), acrescentar carimbos de tempo confiáveis e planejar o recarimbo (renovação do carimbo de tempo de arquivo), para que a evidência continue válida se um algoritmo enfraquecer. (b) Firmware: a versão final do bootloader aceita duas chaves de verificação — LMS (SP 800-208, apenas verificação no dispositivo, assinatura no HSM com controle de estado) e ML-DSA-44 —, para que o comprometimento ou a quebra de uma deixe a outra; assinar cada imagem com as duas.

As duas partes usam dois algoritmos pelo mesmo motivo: vida longa sem segunda chance.

### 35.3 Crítica da banca

O jurídico pergunta se as assinaturas duplas confundem os tribunais — resposta: a política do documento declara que qualquer uma das assinaturas válidas basta durante a transição, e que as duas são exigidas após uma data. As operações perguntam pela vazão de assinaturas — a capacidade do LMS é dimensionada conforme o Capítulo 32. A segurança pergunta por que não o SLH-DSA para o firmware — as suas assinaturas maiores (7,8 kB ou mais na variante pequena) podem exceder os orçamentos de tempo de boot e de armazenamento nos menores dispositivos, mas ele continua candidato para os outros.

Cada resposta remete a uma decisão já tomada, que é o que a banca quer ver: evidências, não opiniões novas.

### 35.4 Erros comuns e limites

- Âncoras de confiança de um único algoritmo em dispositivos que não podem ser atualizados de novo.
- Ignorar a validação de longo prazo e a renovação dos carimbos de tempo.
- Escolher assinaturas com estado sem capacidade de gerenciamento de estado.

Dispositivos que não podem receber outra atualização de bootloader precisam de duas âncoras de confiança agora, já que não haverá chance posterior de acrescentar uma. A evidência jurídica precisa continuar válida por doze anos, o que exige a renovação dos carimbos de tempo se um algoritmo enfraquecer. Assinaturas com estado sem estado imposto pelo HSM arriscam a reutilização de índices após uma restauração, então as equipes sem essa capacidade devem preferir o ML-DSA ou o SLH-DSA.

### Nota de engenharia

A validação de longo prazo merece um teste próprio. Simule a verificação de um conhecimento de embarque num ano futuro, configurando a política do verificador para rejeitar o ECDSA e aceitar apenas o ML-DSA e os carimbos de tempo renovados; os documentos assinados no início da transição ainda precisam ser validados pela sua cadeia de carimbos de tempo de arquivo. Executar esse teste agora revela se o formato do documento, a autoridade de carimbo de tempo e o software verificador realmente suportam as regras de transição que o jurídico aprovou no papel.

### Exercícios

- **EX069 — Projeto do documento.** Especifique os campos de assinatura e a política de validação dos conhecimentos de embarque com assinatura dupla. Rubrica: 3 = regras de transição e renovação dos carimbos de tempo.
- **EX070 — Chaves do bootloader.** Justifique o projeto de bootloader com dois algoritmos e o seu custo. Rubrica: 3 = benefício da diversidade vs. tamanho do código e custo de assinatura.

### Síntese

A autenticação de vida longa precisa de diversidade de algoritmos, carimbos de tempo com renovação e escolhas de assinatura adequadas às restrições dos dispositivos e à capacidade de gerenciamento de estado.

<!-- open-cyber-academy:chapter-navigation:start ch-35 -->
### Continue estudando — capítulo 35 de 50

[← Capítulo 34](#ch-34) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 36 →](#ch-36)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-36"></a>

## Capítulo 36 — Segurança quântica e pós-quântica: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) orçar bytes e computação para os handshakes pós-quânticos; (2) medir latência e vazão; (3) avaliar os efeitos do tamanho das cadeias de certificados; e (4) escalar os serviços de assinatura e verificação. O capítulo parte dos Capítulos 8, 11 e 29.

### 36.1 Orçamentos de bytes

O ML-KEM acrescenta cerca de 2,3 kB a um handshake TLS híbrido (compartilhamento de 1.216 bytes do cliente mais compartilhamento de 1.120 bytes do servidor). Os certificados pós-quânticos acrescentam muito mais: cada certificado ML-DSA-44 carrega uma chave de 1.312 bytes e uma assinatura de 2.420 bytes; uma cadeia mais as assinaturas do CertificateVerify e da Certificate Transparency pode passar de 15 kB — além da janela de congestionamento inicial do TCP em muitas configurações, o que custa uma ida e volta a mais.

A troca de chaves cabe em dois segmentos TCP, enquanto uma cadeia de certificados pós-quânticos pode precisar, sozinha, de uma ida e volta a mais. É por isso que a BPA migra primeiro a troca de chaves e trata os certificados como um projeto separado.

### 36.2 Atividade prática — Laboratório B

```python
# Lab B (ch 36): bytes of authentication in a TLS handshake for different signature choices.
# Sizes in bytes: (public key, signature). ML-DSA from FIPS 204; SLH-DSA-128s from FIPS 205.
algs = {"ECDSA P-256": (65, 72), "RSA-2048": (270, 256), "ML-DSA-44": (1312, 2420),
        "ML-DSA-65": (1952, 3309), "SLH-DSA-SHA2-128s": (32, 7856)}
def chain_bytes(alg, depth=2, scts=2):
    pk, sig = algs[alg]
    certs = depth * (pk + sig + 400)          # leaf + intermediate: key + CA signature + ~400 B fields
    return certs + sig + scts * sig           # + CertificateVerify + embedded SCT signatures
for a in algs:
    print(f"{a:20s} ~{chain_bytes(a):6d} bytes of certificates and signatures")
```

Saída esperada:

```text
ECDSA P-256          ~  1290 bytes of certificates and signatures
RSA-2048             ~  2620 bytes of certificates and signatures
ML-DSA-44            ~ 15524 bytes of certificates and signatures
ML-DSA-65            ~ 21249 bytes of certificates and signatures
SLH-DSA-SHA2-128s    ~ 40144 bytes of certificates and signatures
```

O acréscimo de ~400 bytes por certificado e as duas assinaturas SCT embutidas são hipóteses simplificadoras; os tamanhos reais variam. O resultado explica por que a migração da autenticação na web pública é mais difícil do que a da troca de chaves e por que as propostas para reduzir o tamanho das cadeias (como os certificados abreviados ou em árvore de Merkle) são temas ativos de pesquisa.

Lendo a saída, uma cadeia ML-DSA-44 tem cerca de doze vezes o tamanho da cadeia ECDSA, e a variante pequena do SLH-DSA é cerca de trinta vezes maior. Execute de novo com `scts=0` para ver quanto as assinaturas de transparência contribuem.

### 36.3 Computação

As operações do ML-KEM são rápidas — muitas vezes mais rápidas que o X25519 em servidores com instruções vetoriais. A assinatura e a verificação do ML-DSA são rápidas; a assinatura do SLH-DSA é lenta (de milissegundos a segundos, conforme a variante). O planejamento da capacidade dos servidores, portanto, se concentra na largura de banda e nos serviços de assinatura, e não na CPU do KEM.

Para a BPA, isso desloca o planejamento para a largura de banda nos enlaces de satélite com os navios e para a vazão do serviço central de assinatura. A assinatura lenta do SLH-DSA é aceitável para uma raiz offline que assina raramente, mas não para assinar milhares de documentos por hora.

### 36.4 Medição

Meça os percentis da latência de handshake (p50, p95, p99) por tipo de cliente e caminho de rede, antes e depois; a vazão dos serviços de assinatura; as operações por segundo dos HSMs com os novos algoritmos. Relate distribuições, não médias.

As médias escondem a cauda, onde estão os usuários com enlaces ruins; um aumento de alguns milissegundos no p99 pode esconder algumas conexões que expiram por completo. A BPA registra a latência por tipo de cliente e caminho porque os navios em enlaces de satélite se comportam de forma muito diferente dos navegadores de escritório. As medições são feitas durante uma semana antes e outra depois de cada mudança, para que a variação diária normal não engane a comparação.

### 36.5 Exemplo resolvido

A BPA mede os handshakes de borda: latência p50 +0,4 ms e p99 +3 ms após ativar o X25519MLKEM768 (sintético); dentro do orçamento. Um teste de uma cadeia ML-DSA-65 num enlace de satélite com um navio mostra uma ida e volta a mais (+600 ms) — então as conexões dos navios mantêm certificados clássicos por mais tempo e recebem um ajuste da retomada de sessão.

O resultado da borda mostra que o custo do ML-KEM é pequeno em enlaces terrestres. O resultado do navio mostra que é a cadeia grande, e não a troca de chaves, que causa a ida e volta a mais, como o Laboratório B previa: mais de 15 kB de dados de autenticação excedem a janela de congestionamento inicial. A retomada de sessão evita reenviar a cadeia nas conexões repetidas.

### 36.6 Erros comuns e limites

- Medir apenas a CPU.
- Médias em vez da latência de cauda.
- Ignorar os efeitos das cadeias grandes sobre a janela de congestionamento.

Os benchmarks de CPU mostram o ML-KEM mais rápido que o X25519, mas não captam os custos de largura de banda que dominam nos enlaces lentos. As médias escondem as conexões lentas dos navios na cauda do p99. Cadeias grandes que excedem a janela de congestionamento acrescentam uma ida e volta inteira, o que num enlace de satélite de 600 milissegundos custa mais do que toda a computação somada. O plano da BPA mede cada classe de dispositivo e cada caminho de rede separadamente exatamente por esse motivo.

### Nota de engenharia

O planejamento de capacidade deve incluir as pessoas que vão ler os números. Expresse os resultados como mudanças na latência visível ao usuário no percentil 99 por caminho e como bytes por conexão para a equipe de rede, e não apenas como operações por segundo. Uma mudança de dois milissegundos na mediana costuma ser invisível, enquanto uma ida e volta inteira a mais num enlace de alta latência com um navio não é; apresentar as duas lado a lado permite que as partes interessadas aceitem a mudança barata e planejem em torno da cara.

### Exercícios

- **EX071 — Orçamento da cadeia.** Usando o Laboratório B, encontre o tamanho com profundidade 1 (apenas o certificado folha) para o ML-DSA-44 sem SCTs. Rubrica: 3 = valor correto e método.
- **EX072 — Plano de medição.** Escreva um plano de medição de latência para o enlace com os navios. Rubrica: 3 = percentis, caminhos, antes/depois, tamanho da amostra.

### Síntese

O desempenho da PQC é sobretudo uma questão de bytes: a troca de chaves acrescenta kilobytes, os certificados acrescentam muitos mais; meça as caudas e os caminhos e planeje a capacidade de assinatura.

<!-- open-cyber-academy:chapter-navigation:start ch-36 -->
### Continue estudando — capítulo 36 de 50

[← Capítulo 35](#ch-35) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 37 →](#ch-37)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-37"></a>

## Capítulo 37 — Segurança quântica e pós-quântica: operações

### Objetivos de aprendizagem

Você vai (1) operar implantações em estágios com portões estatísticos; (2) monitorar os algoritmos negociados e o fallback; (3) gerenciar certificados e chaves para os novos algoritmos; e (4) conduzir os processos de mudança e de incidentes. O capítulo parte dos Capítulos 17, 32 e 36.

### 37.1 Portões de canário

Promova um estágio da implantação apenas quando o limite superior de confiança da taxa de falhas estiver dentro do orçamento. Canários pequenos não conseguem demonstrar efeitos pequenos — o limite é largo —, então o portão segura até que tráfego suficiente tenha sido observado.

O portão compara o limite superior com a linha de base mais o aumento permitido, e não com zero, porque alguns handshakes falham por motivos comuns, como clientes que caem das redes móveis. Medir a linha de base durante uma semana antes da mudança faz, portanto, parte do portão. Sem isso, a equipe não consegue saber se uma taxa de falhas de uma em duas mil é nova ou sempre existiu.

### 37.2 Atividade prática — Laboratório K

```python
# Lab K (ch 37): canary gate for enabling a hybrid group - promote only if failures stay within budget.
import math
def upper95(k, n):                      # Wilson upper bound
    z = 1.96; p = k / n; d = 1 + z*z/n
    return ((p + z*z/(2*n)) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
baseline, budget = 5e-4, 4e-4            # baseline failure rate, allowed increase
for stage, k, n in [("1% canary", 3, 5000), ("10% canary", 28, 50000), ("10% canary (proxy site)", 96, 50000)]:
    ub = upper95(k, n); ok = ub <= baseline + budget
    print(f"{stage:24s} {k}/{n}  upper95={ub:.5f}  {'PROMOTE' if ok else 'HOLD'}")
```

Saída esperada:

```text
1% canary                3/5000  upper95=0.00176  HOLD
10% canary               28/50000  upper95=0.00081  PROMOTE
10% canary (proxy site)  96/50000  upper95=0.00234  HOLD
```

O canário de 1% segura não porque as falhas sejam altas, mas porque 5.000 conexões não conseguem limitar a taxa com precisão. O local do proxy segura porque a sua taxa é de fato maior — um problema local a corrigir, não um motivo para uma reversão global.

O portão passa quando o limite é no máximo 0,0009, a linha de base de 0,0005 mais o orçamento de 0,0004. Com 3 falhas em 5.000, a estimativa pontual é 0,0006, já dentro do orçamento, mas o limite de Wilson de 0,00176 não está. Experimente 0 e 1 falha em 5.000: zero dá um limite de cerca de 0,00077 e promove, enquanto uma única falha dá 0,00113 e segura. Só com a taxa da linha de base, 5.000 conexões teriam cerca de 2,5 falhas, então um canário tão pequeno quase sempre segura, e o portão simplesmente espera mais tráfego.

### 37.3 Monitoramento

Painéis: grupos negociados por serviço, taxa e motivos de fallback, falhas de handshake por caminho, algoritmos de certificado em uso, capacidade das chaves com estado, versões das bibliotecas. Alertas para picos de fallback e para qualquer negociação inesperada somente clássica onde os híbridos são exigidos.

Cada item do painel responde a uma pergunta operacional: o grupo híbrido está sendo negociado, onde as falhas se concentram, quais bibliotecas precisam de atualização e quantas assinaturas restam nas chaves com estado. Os alertas se concentram nas mudanças, para que o engenheiro de plantão olhe o que mudou desde ontem em vez de ler todos os painéis. A BPA revisa se cada alerta levou a uma ação útil e remove os alertas que nunca levam.

### 37.4 Operações de certificados e chaves

A automação do ciclo de vida dos certificados (por exemplo, o ACME, [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555.html)) torna rotineiras as mudanças de algoritmo: certificados de vida curta podem trocar de algoritmo na renovação. As cerimônias de chaves das novas raízes PQC são planejadas como qualquer cerimônia de raiz, com testemunhas e procedimentos registrados.

Com certificados de noventa dias emitidos via ACME, a BPA pode mover um serviço para um novo algoritmo de assinatura em um único ciclo de renovação, uma vez que os clientes o suportem. Uma cerimônia de raiz leva muito mais tempo para organizar, então a cerimônia da raiz pós-quântica é agendada cedo, com o HSM e as testemunhas reservados com meses de antecedência.

### 37.5 Exemplo resolvido

O runbook de operações da BPA para o TLS híbrido: revisão diária dos painéis durante a implantação; promover pelos portões; quando o portão segura, investigar por caminho; num pico de fallback, verificar as mudanças recentes; em falhas no local do proxy, aplicar uma exceção específica do caminho, com expiração, e abrir um chamado com o fornecedor.

Cada etapa do runbook corresponde a uma lição do caso: os portões vêm do Laboratório K, a investigação por caminho vem do resultado do local do proxy, e as exceções específicas de caminho vêm da falha do portal das companhias de navegação. Escrever essas etapas significa que o turno da noite trata um portão retido da mesma forma que a equipe de implantação trataria. O runbook é revisado após cada incidente e atualizado quando uma etapa se mostrou pouco clara.

### 37.6 Erros comuns e limites

- Promover com base em estimativas pontuais de canários pequenos.
- Reversão global para falhas locais.
- Processos manuais de certificados que tornam lenta a mudança de algoritmo.

Um canário pequeno ainda tem um limite de confiança largo, como o Laboratório K mostrou para 5.000 conexões, em que 3 falhas deram uma estimativa pontual de 0,0006, dentro do orçamento, mas um limite superior de 0,00176, então promover com base na estimativa pontual é adivinhação. Uma reversão global por causa do problema do local do proxy removeria a proteção de todos os caminhos saudáveis. Os processos manuais de certificados fazem de cada mudança de algoritmo um projeto, enquanto a renovação automatizada a transforma numa etapa de rotina que acontece a cada noventa dias.

### Nota de engenharia

As operações também são responsáveis pela comunicação durante a implantação. Publique uma nota curta de status a cada estágio de promoção, listando o estágio, o limite de falhas medido, as exceções conhecidas e a data da próxima decisão, para que a equipe da central de atendimento reconheça os chamados relacionados e os parceiros possam planejar. Uma central de atendimento que sabe que uma implantação híbrida chegou ontem ao proxy de inspeção do portal das companhias de navegação encaminhará corretamente, em minutos, um conjunto de reclamações de conexão, em vez de tratá-las durante dias como falhas sem relação.

### Exercícios

- **EX073 — Aritmética do portão.** Com linha de base de 5e-4 e orçamento de 4e-4, 30 falhas em 50.000 conexões permitem promover? Use a função do Laboratório K. Rubrica: 3 = decisão correta, com o limite superior mostrado.
- **EX074 — Runbook.** Escreva a seção do runbook para "a taxa de fallback dobrou durante a noite". Rubrica: 3 = etapas de triagem, responsáveis, escalonamento.

### Síntese

As operações transformam a implantação em etapas controladas, com portões estatísticos, monitoramento dos resultados negociados, ciclos de vida de certificados automatizados e respostas específicas por caminho.

<!-- open-cyber-academy:chapter-navigation:start ch-37 -->
### Continue estudando — capítulo 37 de 50

[← Capítulo 36](#ch-36) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 38 →](#ch-38)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-38"></a>

## Capítulo 38 — Segurança quântica e pós-quântica: validação

### Objetivos de aprendizagem

Você vai (1) validar que o sistema migrado atende às necessidades das partes interessadas; (2) distinguir as evidências de verificação das evidências de validação; (3) conduzir testes de aceitação com usuários e parceiros; e (4) validar com cuidado as alegações de redução de risco. O capítulo parte dos Capítulos 16, 30 e 37.

### 38.1 Verificação versus validação

A verificação mostra que os requisitos são cumpridos ("o TLS de borda negocia o X25519MLKEM768 com 99,2% dos clientes que o oferecem"). A validação mostra que o sistema cumpre o seu propósito ("as companhias de navegação, a aduana e a equipe operam normalmente, e os fluxos de dados de vida longa estão protegidos contra a gravação"). As duas são necessárias; uma não implica a outra.

Um sistema pode passar na verificação e ainda assim falhar na validação: a borda pode negociar o grupo híbrido com 99,2% dos clientes que o oferecem enquanto um job em lote de um parceiro falha em silêncio porque o seu cliente antigo expira por timeout. A validação detectaria isso pelos testes de aceitação do próprio parceiro. Inversamente, os parceiros podem estar satisfeitos enquanto um requisito não é cumprido, por exemplo se a replicação ainda usa troca de chaves clássica.

### 38.2 Testes de aceitação

Os parceiros executam testes de aceitação nos seus fluxos de trabalho; a equipe de operações confirma que não há incidentes novos; o jurídico confirma que os documentos com assinatura dupla são aceitáveis; as equipes de dispositivos confirmam que as atualizações de firmware funcionam em todos os modelos. Registre a aceitação com datas e signatários.

A aceitação é registrada por parte interessada porque cada uma verifica uma propriedade diferente: os parceiros, os seus fluxos de trabalho; o jurídico, o valor probatório das assinaturas; as equipes de dispositivos, o caminho de atualização. Uma assinatura datada de cada uma torna simples resolver disputas posteriores. Quando uma parte interessada não pode aceitar, o motivo se torna um item de trabalho, em vez de ser anotado e esquecido.

### 38.3 Validar a redução de risco

Afirme com cuidado: "O tráfego de borda gravado e negociado com grupos híbridos está protegido contra a decifração quântica futura se o X25519 ou o ML-KEM-768 continuar seguro" é defensável. "A BPA é segura contra a computação quântica" não é — ainda restam certificados, algumas VPNs, dispositivos e ativos desconhecidos. A validação relata o que está protegido e o que não está.

A afirmação defensável nomeia exatamente o que está protegido, sob qual hipótese e, implicitamente, o que não está. Listar os caminhos clássicos restantes, com datas, transforma a lacuna num plano em vez de uma fraqueza oculta. Os conselhos conseguem tomar decisões com afirmações assim; um slogan como "segura contra a computação quântica" não lhes dá nada sobre o que agir e se torna constrangedor quando uma exceção é descoberta.

### 38.4 Validação independente

Uma equipe independente (auditoria interna ou avaliador externo) amostra fluxos, verifica os algoritmos negociados a partir do seu próprio ponto de observação e revisa os desconhecidos do CBOM. A independência detecta a autoavaliação otimista.

Uma equipe independente que captura tráfego do seu próprio ponto de observação pode descobrir, por exemplo, que um serviço relatado como híbrido na verdade negocia grupos clássicos com uma determinada família de clientes. Amostrar fluxos, em vez de confiar no painel da equipe, é o que torna a verificação independente. Revisar os desconhecidos importa porque uma autoavaliação tende a tratá-los como menores. As constatações do avaliador entram no dossiê com as respostas da equipe.

### 38.5 Exemplo resolvido

O relatório de validação da BPA: 64% das conexões de borda híbridas (verificação); aceitação dos parceiros concluída para 11 de 14 companhias (validação); exportações para a aduana com destinatário duplo (validação pendente do teste da agência); bootloader com chave dupla em 40% dos dispositivos; ativos desconhecidos 6%. A declaração de risco residual lista os caminhos clássicos restantes, com datas.

O relatório separa verificação de validação em cada linha, para que os leitores vejam quais alegações se apoiam na telemetria e quais na confirmação das partes interessadas. O teste pendente da aduana é relatado como pendente, não como concluído, e o número de 40% do firmware declara a cobertura de dispositivos, não a assinatura de imagens. É essa precisão que permite ao conselho confiar no restante do relatório.

### 38.6 Erros comuns e limites

- Tratar as métricas de verificação como validação.
- Alegar em excesso que se é "seguro contra a computação quântica".
- Apenas autovalidação.

Uma parcela híbrida alta é um resultado de verificação; ela não diz nada sobre se os parceiros ainda conseguem trabalhar, o que só a validação confirma. Alegar ser "seguro contra a computação quântica" ignora os certificados clássicos, as VPNs e os ativos desconhecidos que o relatório lista. A autovalidação sozinha tende a deixar escapar o que a equipe não pensou em verificar, e é por isso que uma amostra independente faz parte do processo da BPA. Cada um desses erros aparece nos primeiros relatórios de migração de muitas organizações, geralmente descoberto por um auditor, e não pela equipe.

### Nota de engenharia

A validação deve revisitar, uma a uma, as necessidades originais das partes interessadas do Capítulo 21. Para cada uma, declare se está atendida, parcialmente atendida ou não atendida, com evidências, e registre qualquer necessidade que tenha mudado durante o programa — por exemplo, um parceiro cuja exigência de retenção de dados passou de cinco para dez anos após a renovação de um contrato. As necessidades mudam; uma validação que compara apenas com a lista original pode declarar sucesso num alvo que já não reflete o que as partes interessadas realmente exigem.

### Exercícios

- **EX075 — Risco residual.** Escreva a declaração de risco residual da BPA após o primeiro ano. Rubrica: 3 = lista os caminhos não protegidos, com datas e responsáveis.
- **EX076 — Independência.** Projete uma amostra de validação independente para o TLS de borda. Rubrica: 3 = ponto de observação, tamanho da amostra, comparação com as métricas internas.

### Síntese

A validação confirma que o sistema migrado atende às suas partes interessadas e declara o risco residual com honestidade, idealmente verificado por uma equipe independente.

<!-- open-cyber-academy:chapter-navigation:start ch-38 -->
### Continue estudando — capítulo 38 de 50

[← Capítulo 37](#ch-37) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 39 →](#ch-39)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-39"></a>

## Capítulo 39 — Segurança quântica e pós-quântica: manutenibilidade

### Objetivos de aprendizagem

Você vai (1) projetar para a agilidade criptográfica, para que as mudanças futuras sejam baratas; (2) implementar a seleção de algoritmos orientada por política; (3) gerenciar a aposentadoria de algoritmos; e (4) manter o inventário e a documentação atualizados. O capítulo parte dos Capítulos 9, 18 e 27.

### 39.1 Agilidade como manutenibilidade

A transição pós-quântica não será a última: os conjuntos de parâmetros podem mudar, o HQC e o FN-DSA vão chegar e algum algoritmo pode enfraquecer. O [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) descreve a agilidade em protocolos, aplicações, hardware e infraestrutura. Sistemas manuteníveis fazem da mudança de algoritmo uma operação de rotina, medida em dias.

A meta da BPA é que trocar um algoritmo em qualquer serviço no escopo leve dias, não meses. O Laboratório A mostra o padrão em poucas linhas: um registro de implementações, uma política que escolhe uma delas e uma lista de aceitação que controla o que ainda é confiável. A métrica de tempo de substituição testa se esse projeto se sustenta nos sistemas reais, onde suposições fixas no código costumam se esconder.

### 39.2 Atividade prática — Laboratório A

```python
# Lab A (ch 39): crypto-agility through a policy-driven registry instead of hard-coded algorithms.
import hashlib, hmac
REGISTRY = {"hmac-sha256": lambda k, m: hmac.new(k, m, hashlib.sha256).digest(),
            "hmac-sha3-256": lambda k, m: hmac.new(k, m, hashlib.sha3_256).digest()}
POLICY = {"tag-algorithm": "hmac-sha256", "accept": ["hmac-sha256", "hmac-sha3-256"]}
def protect(key, msg):
    alg = POLICY["tag-algorithm"]; return alg, REGISTRY[alg](key, msg)
def check(key, msg, alg, tag):
    if alg not in POLICY["accept"]: return False            # algorithm identifier is authenticated by policy
    return hmac.compare_digest(REGISTRY[alg](key, msg), tag)
k, m = b"k" * 32, b"meter reading 42"
a1, t1 = protect(k, m)
POLICY["tag-algorithm"] = "hmac-sha3-256"                   # migration = one policy change
a2, t2 = protect(k, m)
print("old tag still verifies during transition:", check(k, m, a1, t1))
print("new tag verifies:", check(k, m, a2, t2), "| algorithms:", a1, "->", a2)
POLICY["accept"] = ["hmac-sha3-256"]                        # retire the old algorithm
print("old tag after retirement:", check(k, m, a1, t1))
```

Saída esperada:

```text
old tag still verifies during transition: True
new tag verifies: True | algorithms: hmac-sha256 -> hmac-sha3-256
old tag after retirement: False
```

O laboratório usa MACs simétricos para manter o código curto; o padrão — registro, política, lista de aceitação, aposentadoria — é idêntico para KEMs e assinaturas.

Observe a ordem das etapas: o novo algoritmo é introduzido enquanto o antigo continua na lista de aceitação, para que as tags existentes ainda sejam verificadas; só então o algoritmo antigo é removido. Inverter a ordem quebraria todas as tags armazenadas de uma só vez. O identificador do algoritmo viaja com a tag, mas é verificado contra a política, então um atacante não consegue escolher um algoritmo fraco trocando o rótulo. Acrescente ao registro um terceiro algoritmo, deliberadamente fraco, e confirme que ele é rejeitado porque a política não o aceita.

### 39.3 Aposentadoria

Aposentar um algoritmo tem fases: parar de gerar novos usos; aceitar os usos antigos durante uma janela de transição; rejeitar após uma data; remover o código. Cada fase é uma mudança de política mais o monitoramento do uso residual.

Monitorar o uso residual diz à BPA quando é seguro passar à fase seguinte: se os handshakes somente clássicos caíram para um punhado de clientes conhecidos, a data de rejeição pode ser definida e esses clientes, contatados. Remover o código por último evita a reativação acidental por um erro de configuração. Cada fase tem uma data publicada com antecedência, para que os parceiros possam planejar.

### 39.4 Documentação e inventário

Mantenha o CBOM, os documentos de controle de interface, as políticas e os runbooks atualizados por meio de automação sempre que possível (geração do CBOM no build, painéis alimentados por telemetria). Uma documentação desatualizada torna a próxima migração tão difícil quanto a primeira.

A BPA trata a documentação como parte do sistema: um build que muda dependências criptográficas regenera o CBOM, e uma mudança de política atualiza o documento de controle de interface pelo mesmo pipeline. Quando a documentação precisa ser escrita à mão, como os runbooks, ela tem um responsável e uma data de revisão. O objetivo é que a próxima migração comece de um retrato preciso, e não de mais um projeto de descoberta.

### 39.5 Exemplo resolvido

A BPA mede o tempo de substituição trocando, por política, o algoritmo de MAC interno num serviço de teste: 2 dias, incluindo os testes. O mesmo exercício num serviço legado com algoritmos fixos no código leva 6 semanas — um argumento quantificado para a refatoração.

Dois dias contra seis semanas dão um fator de cerca de vinte, o que torna concreto o argumento da refatoração para quem detém o orçamento. As seis semanas vêm sobretudo de encontrar cada ponto de chamada fixo no código e testar cada um, o mesmo trabalho de que o serviço de documentos eletrônicos da BPA precisou para as suas 41 chamadas `rsa_sign()`. Refatorar uma vez remove esse custo de todas as mudanças futuras.

### 39.6 Erros comuns e limites

- Tratar a migração PQC como um projeto único.
- Aceitar identificadores de algoritmo vindos de entradas não confiáveis sem verificação de política.
- Aposentar algoritmos sem monitorar o uso residual.

Tratar a migração PQC como um projeto único deixa os sistemas tão rígidos quanto antes, prontos para repetir o esforço quando o HQC ou o FN-DSA chegarem. Aceitar identificadores de algoritmo vindos de entradas não confiáveis permite que um atacante escolha a opção mais fraca, o que o Laboratório A impede com a sua lista de aceitação. Aposentar sem monitorar arrisca quebrar clientes que ainda dependem do algoritmo antigo, o que a BPA evita publicando as datas de rejeição apenas depois que o uso residual está perto de zero.

### Nota de engenharia

A agilidade também é contratual. A linguagem das compras deve exigir que os fornecedores suportem a substituição de algoritmos por configuração, publiquem os inventários criptográficos dos seus produtos, forneçam atualizações de segurança para novos algoritmos dentro de prazos declarados e divulguem as bibliotecas que embutem. A BPA acrescenta essas cláusulas a todo contrato novo de equipamentos e software; ao longo de um ciclo de renovação de hardware, a parcela dos ativos que pode trocar de algoritmo sem substituição cresce, e a próxima migração fica mais barata por projeto.

### Exercícios

- **EX077 — Ampliar o Laboratório A.** Acrescente um terceiro algoritmo e uma verificação de data de aposentadoria. Rubrica: 3 = funciona e falha de forma fechada após a data.
- **EX078 — Tempo de substituição.** Projete uma medição do tempo de substituição para o KEM de borda da BPA. Rubrica: 3 = eventos de início e fim e evidências definidos.

### Síntese

Manutenibilidade significa agilidade: algoritmos orientados por política, aposentadoria em fases, inventário atualizado e um tempo de substituição medido.

<!-- open-cyber-academy:chapter-navigation:start ch-39 -->
### Continue estudando — capítulo 39 de 50

[← Capítulo 38](#ch-38) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 40 →](#ch-40)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem

Você vai (1) verificar as proteções de ponta a ponta, num laboratório, a partir do ponto de observação de um atacante; (2) testar a resistência ao rebaixamento; (3) verificar o tratamento do estado das assinaturas com estado; e (4) produzir um relatório de verificação. O capítulo parte dos Capítulos 30–39.

### 40.1 Verificação do ponto de observação do atacante

Num laboratório isolado que replica a borda da BPA, capture handshakes e confirme o grupo negociado a partir da rede, e não dos logs do servidor. Verifique que as sessões gravadas com grupos híbridos exigiriam quebrar tanto o X25519 quanto o ML-KEM — conferindo que a derivação da chave de sessão inclui os dois compartilhamentos (o princípio do Laboratório C).

Os logs do servidor podem estar errados: uma biblioteca TLS pode registrar o primeiro grupo oferecido em vez do negociado, como o estagiário do Capítulo 43 descobre. Ler o ServerHello na rede dá o grupo real, e compará-lo com os logs verifica os dois de uma só vez.

### 40.2 Testes de rebaixamento

Um man-in-the-middle de laboratório remove os grupos híbridos do ClientHello. Esperado: a assinatura da transcrição do TLS 1.3 provoca a falha, ou o cliente tenta de novo sem o híbrido somente se a lógica da aplicação o permitir — o que o teste deve detectar e a política deve proibir onde possível. Execute apenas no laboratório.

O resultado esperado para um cliente correto é um handshake que falha, sem nova tentativa, já que a verificação da transcrição detecta o grupo removido. Se o cliente tenta de novo sem o grupo híbrido e tem sucesso, o teste encontrou um caminho de rebaixamento no nível da aplicação. Repita o teste para cada biblioteca cliente no escopo, porque o comportamento de nova tentativa difere entre elas.

### 40.3 Testes de tratamento do estado

Para LMS/XMSS: simule a restauração do HSM a partir de um backup e confirme que o HSM se recusa a reutilizar índices; simule pedidos de assinatura simultâneos e confirme que não há índice duplicado; esgote uma pequena árvore de teste e confirme que a assinatura para de forma limpa.

O teste de assinatura simultânea importa porque um serviço de assinatura sob carga pode entregar o mesmo índice a dois pedidos se a atualização do contador não for atômica. Esgotar uma pequena árvore de teste, por exemplo uma de altura cinco com 32 assinaturas, permite à equipe verificar o comportamento de fim de chave em minutos, em vez de esperar anos. Cada resultado de teste entra no dossiê com a versão do firmware do HSM usada, já que uma atualização posterior do firmware pode mudar o comportamento.

### 40.4 Relatório de verificação

Relatório: escopo, ambiente, testes, resultados, desvios, problemas residuais, links para as evidências. Um bom relatório permite que um revisor execute os testes de novo.

Os desvios são a parte mais importante: um teste executado com outra versão de biblioteca ou numa rede simplificada precisa dizê-lo, ou um revisor pode supor que os resultados valem para a produção. Os links para as evidências ligam cada resultado à sua captura ou log bruto. Os relatórios da BPA usam sempre os mesmos títulos, para que os revisores saibam onde procurar e as partes ausentes saltem aos olhos. Um relatório que não pode ser executado de novo é tratado como rascunho.

### 40.5 Exemplo resolvido

O laboratório da BPA descobre que uma biblioteca cliente interna tenta de novo com grupos somente clássicos após qualquer erro de handshake, inclusive os causados por um atacante. Correção: restringir a nova tentativa a erros de incompatibilidade específicos, registrar as novas tentativas e planejar a remoção do fallback para esse cliente até uma data definida.

Restringir a nova tentativa aos erros de incompatibilidade listados mantém a disponibilidade para pares genuinamente antigos, enquanto nega ao atacante a capacidade de disparar o fallback com um erro forjado. Registrar cada nova tentativa fornece os dados necessários para ver quando o fallback pode ser removido. A remoção datada torna a exceção temporária por projeto, e o teste de rebaixamento é executado de novo após a correção para confirmá-la.

### 40.6 Erros comuns e limites

- Verificar apenas pelos logs do servidor.
- Testar o rebaixamento em produção.
- Não testar a restauração do estado das assinaturas com estado.

Os logs do servidor refletem o que o software acredita, o que pode diferir da rede, então a verificação apenas pelos logs pode deixar escapar rebaixamentos reais. Os testes de rebaixamento em produção podem quebrar sessões dos parceiros, então eles ficam no laboratório isolado. Não testar a restauração do estado deixa a falha mais perigosa do LMS, a reutilização de índices após a restauração de um backup, sem exame até acontecer de verdade. Cada um desses testes leva horas no laboratório e evita falhas que levariam semanas para reparar em produção.

### Nota de engenharia

Inclua controles negativos em cada execução do laboratório. Antes de testar a resistência ao rebaixamento, confirme que o arcabouço de testes consegue detectar um rebaixamento bem-sucedido, configurando deliberadamente um cliente que o permita; se mesmo assim o arcabouço não relatar nenhum rebaixamento, ele está quebrado. Os controles negativos são baratos e evitam a falha de verificação mais constrangedora — um relatório verde produzido por um teste que nunca poderia ter falhado.

### Exercícios

- **EX079 — Plano do teste de rebaixamento.** Escreva o plano de laboratório para o teste de rebaixamento. Rubrica: 3 = isolamento, resultados esperados, critérios de aprovação/reprovação.
- **EX080 — Teste de estado.** Escreva três casos de teste de tratamento do estado para um HSM LMS. Rubrica: 3 = restauração, concorrência, esgotamento.

### Síntese

A verificação de segundo estágio confere as proteções a partir do ponto de observação do atacante, testa o rebaixamento e o tratamento do estado em isolamento e produz relatórios que podem ser executados de novo.

<!-- open-cyber-academy:chapter-navigation:start ch-40 -->
### Continue estudando — capítulo 40 de 50

[← Capítulo 39](#ch-39) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 41 →](#ch-41)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-41"></a>

## Capítulo 41 — Segurança quântica e pós-quântica: otimização do sistema

### Objetivos de aprendizagem

Você vai (1) otimizar as escolhas de parâmetros e algoritmos ao longo de um sistema; (2) reduzir o custo adicional dos handshakes com retomada e cache; (3) equilibrar as categorias de segurança com o custo; e (4) priorizar o trabalho de migração restante para a máxima redução de risco. O capítulo parte dos Capítulos 6, 36 e 39.

### 41.1 Escolhas de parâmetros

O ML-KEM-768 (categoria 3) é o padrão comum para o TLS híbrido; o ML-KEM-1024, onde a política exige a categoria 5 (CNSA 2.0). O ML-DSA-44 versus o -65 troca tamanho por margem. Escolha por contexto, com justificativa documentada, e não "o máximo em todo lugar".

Para a BPA, o ML-KEM-768 cabe no orçamento de 1.300 bytes e dá a categoria 3, o que convém aos seus dados. O ML-DSA-65 é usado nos conhecimentos de embarque, onde alguns kilobytes a mais por documento são irrelevantes, enquanto o ML-DSA-44 convém ao bootloader do guindaste, com a sua memória apertada. Cada escolha e o seu motivo são registrados no registro de decisões.

### 41.2 Redução do custo adicional

A retomada de sessão evita handshakes completos repetidos; a reutilização de conexões amortiza o custo dos certificados; a compressão de certificados ([RFC 8879](https://www.rfc-editor.org/rfc/rfc8879.html)) ajuda as cadeias clássicas, mas comprime mal as chaves e assinaturas pós-quânticas, de aparência aleatória; retirar os certificados intermediários onde os clientes os mantêm em cache reduz bytes.

A compressão funciona nos certificados clássicos porque eles contêm estruturas repetidas; as chaves e assinaturas ML-DSA são quase aleatórias, então há pouco a remover. Para os navios da BPA, a retomada é a medida mais eficaz, porque cada navio se reconecta muitas vezes por dia e só precisa da cadeia completa na primeira conexão.

### 41.3 Priorização pela redução de risco

Com orçamento limitado, ordene o trabalho restante pela exposição reduzida por unidade de esforço: fluxos com dados de vida longa × volume ÷ esforço. Uma ordenação gulosa costuma bastar e é transparente.

Por exemplo, um fluxo com dados aduaneiros de 25 anos, em alto volume, que precisa de uma única mudança de configuração pontua muito acima de um fluxo de baixo volume que exige a substituição de um equipamento. Publicar as pontuações permite que as partes interessadas vejam por que o seu sistema não é o primeiro. Refazer a ordenação após cada item concluído mantém a lista atual à medida que as estimativas de esforço mudam e surgem novos fluxos.

### 41.4 Exemplo resolvido

Os itens restantes da BPA: enlaces com navios (alto custo de latência das cadeias grandes; tempo de vida dos dados moderado), VPN legada (tempo de vida longo, custo de substituição do equipamento), telemetria interna (tempo de vida curto). Otimização: os enlaces com navios recebem apenas a troca de chaves híbrida (barata), com certificados clássicos e retomada ajustada; a VPN legada recebe a mistura de PSK agora e a substituição do equipamento no próximo ciclo orçamentário; a telemetria espera.

A decisão sobre os navios decorre das medições de latência: a troca de chaves híbrida acrescenta pouco, enquanto uma cadeia pós-quântica acrescenta uma ida e volta de 600 milissegundos. Dividir a mudança dá proteção contra a coleta agora, sem esse custo.

### 41.5 Erros comuns e limites

- Categoria 5 em todo lugar sem necessidade.
- Esperar que a compressão encolha as assinaturas PQC.
- Priorizar pela facilidade em vez da exposição.

A categoria 5 em todo lugar acrescenta bytes e computação para dados que não precisam dela, como a chave maior de 1.568 bytes do ML-KEM-1024 diante do orçamento de 1.300 bytes. A compressão ajuda as cadeias clássicas, mas não consegue encolher muito o material pós-quântico de aparência aleatória. Escolher o trabalho pela facilidade em vez da exposição deixa os fluxos aduaneiros de 25 anos esperando enquanto itens mais simples e de pouco valor são concluídos. A ordenação da BPA usa a exposição dividida pelo esforço para cada item e publica a lista, para que cada escolha possa ser questionada.

### Nota de engenharia

As decisões de otimização devem ser revisitadas quando as entradas mudam. Uma nova versão de navegador que suporte certificados pós-quânticos, uma atualização de firmware que corrija um middlebox ou uma data de política revista podem reordenar o trabalho restante. Mantenha a ordenação como uma pequena tabela sob controle de versão, com as hipóteses escritas ao lado de cada pontuação, e recalcule-a a cada revisão trimestral, em vez de tratar a primeira ordenação como um plano permanente.

### 41.6 Otimização que não pode enfraquecer a segurança

Reduzir o tamanho do handshake retirando certificados intermediários ou mantendo chaves em cache por mais tempo pode economizar milissegundos, mas cada mudança desse tipo é revisada diante do horizonte de confidencialidade da BPA. Uma otimização que encurta a latência, mas reintroduz um caminho somente clássico para os dados aduaneiros de 25 anos, é rejeitada, por maior que seja o ganho.

Cada proposta de otimização declara, portanto, quais fluxos afeta e os tempos de vida dos seus dados. Os revisores verificam se a mudança poderia remover a parcela pós-quântica de algum desses fluxos, por exemplo ao habilitar um caminho de fallback. As propostas que só mexem em certificados de sessões de vida curta, como o ajuste da retomada para os navios, costumam passar rapidamente.

### Exercícios

- **EX081 — Ordenar.** Ordene cinco itens restantes da BPA por exposição ÷ esforço, com números declarados. Rubrica: 3 = método transparente e sensibilidade indicada.
- **EX082 — Retomada.** Explique como a retomada muda o custo das cadeias PQC grandes para clientes recorrentes. Rubrica: 3 = correto, com a ressalva sobre as configurações de retomada e de sigilo futuro (forward secrecy).

### Síntese

A otimização do sistema escolhe os parâmetros por contexto, reduz o custo adicional repetido e ordena o trabalho restante pela exposição reduzida por unidade de esforço.

<!-- open-cyber-academy:chapter-navigation:start ch-41 -->
### Continue estudando — capítulo 41 de 50

[← Capítulo 40](#ch-40) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 42 →](#ch-42)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-42"></a>

## Capítulo 42 — Segurança quântica e pós-quântica: pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa aplicada a partir do trabalho de engenharia; (2) projetar um pequeno estudo com resultados mensuráveis; (3) ler e avaliar criticamente a pesquisa em PQC; e (4) devolver os resultados à comunidade de forma responsável. O capítulo parte dos Capítulos 29, 36 e 38.

### 42.1 Perguntas vindas da prática

A engenharia levanta perguntas dignas de pesquisa: com que frequência os middleboxes tratam mal ClientHellos grandes num determinado setor? Qual é o tempo de substituição real para diferentes arquiteturas? Quão precisas são as ferramentas de inventário diante de uma verdade de referência adjudicada? Os livros de [mestrado](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) e de [doutorado](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) desta área desenvolvem esses estudos em profundidade.

Perguntas como essas vêm de dados operacionais que a maioria das organizações já tem, como os logs de falhas de handshake e os registros de mudanças, então um estudo muitas vezes pode começar sem uma nova coleta de dados.

### 42.2 Pequenos estudos

Defina a pergunta, a população, as medições, a comparação e a análise antes de coletar os dados; use dados sintéticos ou autorizados; relate intervalos e limites. Uma monografia de engenharia (Capítulo 49) pode incluir um estudo assim.

Fixar a análise de antemão evita escolher, depois de ver os dados, a comparação que dá o resultado mais interessante. Um estudo na BPA poderia perguntar se os handshakes híbridos falham mais num modelo de proxy do que em outro, tendo como população um mês de tráfego sintético reproduzido e relatando o resultado como uma diferença nas taxas de falha, com o seu intervalo de confiança. Os limites escritos declaram o que a reprodução não consegue representar, como a diversidade real dos clientes.

### 42.3 Ler pesquisa

Verifique o que os números de um artigo medem (configurado ou negociado? laboratório ou campo?), se as linhas de base são justas, se o código e os dados estão disponíveis e quão antigos são os resultados — a área anda rápido, e resultados sobre algoritmos em rascunho podem não se aplicar às normas finais.

Um artigo que relata a adoção do híbrido com base nas configurações pode superestimar a proteção real, como a própria experiência da BPA com os números configurados e negociados mostrou. Resultados medidos no Kyber em rascunho podem diferir, em desempenho ou interoperabilidade, do ML-KEM final. Verificar se o código e os dados estão publicados diz ao leitor se o resultado pode ser reproduzido ou precisa ser aceito por confiança. Os engenheiros da BPA anotam esses pontos ao citar um artigo num registro de decisão.

### 42.4 Devolver à comunidade

Relate os bugs de interoperabilidade aos implementadores, publique resultados agregados anonimizados, contribua com vetores de teste e participe das discussões de normalização. Coordene a divulgação de vulnerabilidades.

O relato da BPA sobre o problema do codepoint obsoleto aos mantenedores da biblioteca do parceiro ajudou outros usuários dessa biblioteca, e não só a BPA. As contribuições de vetores de teste melhoram todas as implementações que os executam. Antes de publicar números agregados, a equipe verifica que nenhum parceiro ou sistema possa ser identificado a partir deles. A participação nas discussões de normalização permite que os operadores levantem problemas práticos, como os limites de tamanho dos handshakes, enquanto os projetos ainda podem mudar.

### 42.5 Exemplo resolvido

Os engenheiros da BPA perguntam se a sua telemetria passiva subconta a negociação híbrida por causa das extensões cifradas do TLS 1.3. Um pequeno estudo compara as determinações dos logs do servidor e das capturas da rede em 1.000 sessões sintéticas no laboratório e encontra concordância quanto ao grupo de troca de chaves (visível em claro no ServerHello), mas não quanto aos algoritmos dos certificados (cifrados) — um resultado aplicado que muda o projeto da medição.

O resultado explica por que o painel pode relatar a troca de chaves híbrida a partir de dados passivos, mas precisa usar a configuração para os algoritmos dos certificados, um limite declarado mais adiante nas orientações da monografia.

### 42.6 Erros comuns e limites

- Estudos projetados depois da coleta dos dados.
- Aplicar resultados de algoritmos em rascunho às normas finais.
- Publicar dados organizacionais identificáveis.

Um estudo projetado depois de ver os dados tende a encontrar o que a equipe esperava encontrar, e é por isso que a pergunta e a análise são fixadas primeiro. Os resultados sobre algoritmos em rascunho podem enganar quando aplicados às normas finais, já que detalhes mudaram. Publicar dados identificáveis pode expor parceiros ou fraquezas; a BPA agrega e verifica cada número antes da divulgação, e um segundo engenheiro confirma que nenhum parceiro pode ser reconhecido nas tabelas publicadas.

### Nota de engenharia

Os estudos aplicados precisam respeitar as mesmas regras de autorização e minimização que as operações. Use dados sintéticos ou dados de sistemas que você está autorizado a estudar, minimize os identificadores na coleta, obtenha a aprovação do dono dos dados antes de publicar agregados e encaminhe qualquer fraqueza de produto pela divulgação coordenada. Essas restrições raramente enfraquecem um estudo de engenharia; geralmente elas afiam a sua pergunta para aquilo que a organização realmente precisa saber.

### Exercícios

- **EX083 — Pergunta.** Escreva uma pergunta de pesquisa aplicada a partir do seu próprio contexto de engenharia, com um plano de medição. Rubrica: 3 = mensurável e delimitada.
- **EX084 — Verificação de artigo.** Aplique a lista de verificação de 42.3 a um artigo sobre desempenho de PQC à sua escolha. Rubrica: 3 = cada verificação respondida com evidências.

### Síntese

A pesquisa aplicada nasce de perguntas de engenharia, usa pequenos estudos planejados de antemão, lê a literatura criticamente e devolve resultados de forma responsável.

<!-- open-cyber-academy:chapter-navigation:start ch-42 -->
### Continue estudando — capítulo 42 de 50

[← Capítulo 41](#ch-41) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 43 →](#ch-43)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-43"></a>

## Capítulo 43 — Prática na indústria ou no serviço público

### Objetivos de aprendizagem

Você vai (1) trabalhar, sob supervisão, numa equipe de migração com formato real; (2) aplicar práticas profissionais — controle de mudanças, documentação, comunicação com as partes interessadas; (3) refletir sobre as lacunas entre teoria e prática; e (4) produzir um relatório de estágio sem divulgar informações confidenciais. O capítulo inicia a etapa de prática e de projeto final.

### 43.1 O estágio

Um estágio numa equipe de segurança, num fornecedor, num órgão público ou numa organização de normalização expõe as realidades da migração: ciclos de compras, sistemas legados, política entre parceiros, congelamentos de mudanças. Neste livro, o estágio é simulado na BPA; num programa real, aplicam-se as regras de confidencialidade da instituição anfitriã.

O estágio ensina o que a sala de aula não consegue: um congelamento de mudanças pode atrasar em um mês uma migração pronta, e a resposta de um fornecedor pode levar oito semanas. Os estudantes aprendem a planejar em torno desses atrasos, em vez de tratá-los como exceções.

### 43.2 Prática profissional

Siga o controle de mudanças: toda mudança criptográfica tem um chamado, uma avaliação de risco, evidências de teste, aprovação e um plano de reversão. Documente as decisões com a justificativa. Comunique o progresso na linguagem da instituição anfitriã — risco e impacto no serviço, e não nomes de algoritmos.

Na prática, um chamado para ativar o grupo híbrido na API dos parceiros nomeia o serviço, a mudança, as evidências de teste do laboratório, o plano de canário e o comando de reversão. Relatar o progresso como "a replicação aduaneira agora está protegida contra a gravação" significa mais para os gestores do que "X25519MLKEM768 ativado". O estagiário escreve as duas versões para cada mudança.

### 43.3 Teoria versus prática

Surpresas comuns: o inventário é mais difícil do que a escolha dos algoritmos; as alegações de "pronto para PQC" dos fornecedores vão de roteiros a funcionalidades já entregues; os parceiros ditam o ritmo; os problemas mais difíceis são organizacionais. Registre-as como notas reflexivas.

As notas de estágio da BPA mostram esse padrão: as decisões sobre algoritmos levaram dias, enquanto encontrar todos os usos do RSA levou meses. As alegações dos fornecedores precisaram ser conferidas com as versões efetivamente entregues. As notas reflexivas registram cada surpresa e o que o estudante planejaria de outra forma da próxima vez, que é o principal resultado de aprendizagem do estágio. Os estudantes comparam as suas notas com o plano que escreveram no início para ver onde as suas expectativas estavam erradas.

### 43.4 Confidencialidade

O relatório de estágio descreve métodos e lições sem identificar sistemas, vulnerabilidades ou parceiros. Use exemplos sintéticos onde for necessário e obtenha a aprovação da instituição anfitriã antes da entrega.

Um relatório de estágio pode descrever o método do painel e a lição sobre os grupos "primeiro oferecido" sem nomear a biblioteca nem os sistemas da instituição anfitriã. Onde é preciso um exemplo concreto, o estudante usa o caso sintético da BPA. A aprovação da instituição anfitriã é uma etapa do processo de entrega, com data própria, para que o relatório não seja atrasado no último momento por um pedido inesperado de mudanças.

### 43.5 Exemplo resolvido

Um estagiário na BPA (sintético) constrói o painel de telemetria passiva. Lições registradas: uma biblioteca TLS registrava apenas o grupo "primeiro oferecido", e não o negociado — o painel esteve errado até ser corrigido; as declarações dos fornecedores dos equipamentos levaram oito semanas para serem obtidas; o comitê de mudanças exigiu um ensaio de reversão antes de aprovar o TLS híbrido na API dos parceiros.

O erro de registro é uma constatação típica de estágio: o painel parecia plausível até o estudante compará-lo com as capturas da rede, o método depois formalizado na verificação do ponto de observação do atacante. A exigência do ensaio de reversão mostra que os comitês de mudanças se preocupam tanto com a recuperação quanto com a própria mudança.

### 43.6 Erros comuns e limites

- Contornar o controle de mudanças "porque é só configuração".
- Relatórios que divulgam vulnerabilidades da instituição anfitriã.
- Tratar os roteiros dos fornecedores como capacidade entregue.

As mudanças de configuração podem quebrar a produção tanto quanto as mudanças de código, como mostrou o reset do proxy, então elas seguem o controle de mudanças. Relatórios que divulgam vulnerabilidades da instituição anfitriã podem prejudicá-la e violar o acordo de estágio. Os roteiros dos fornecedores descrevem intenções; só as funcionalidades entregues e testadas contam num plano de migração, e o estagiário registra no CBOM qual é qual, com a data da verificação.

### Nota de engenharia

Os estágios também ensinam como as decisões são realmente tomadas. Observe quem aprova as mudanças criptográficas, que evidências pedem, quais riscos aceitam e quais escalam. Registre essas observações sem nomes. Os estudantes que entendem o caminho das decisões escrevem projetos melhores no Projeto Final I, porque antecipam as perguntas do comitê de mudanças, do setor de compras e dos gestores de parceiros, em vez de descobri-las no fim.

### Exercícios

- **EX085 — Chamado de mudança.** Escreva um chamado de mudança para ativar o TLS híbrido num serviço interno. Rubrica: 3 = risco, testes, aprovação, reversão.
- **EX086 — Reflexão.** Escreva uma reflexão de 300 palavras sobre uma lacuna entre teoria e prática. Rubrica: 3 = específica, analítica, confidencial.

### Síntese

A prática ensina que a migração é tanto organizacional quanto técnica; o controle de mudanças, a documentação e a confidencialidade são obrigações profissionais.

<!-- open-cyber-academy:chapter-navigation:start ch-43 -->
### Continue estudando — capítulo 43 de 50

[← Capítulo 42](#ch-42) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 44 →](#ch-44)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-44"></a>

## Capítulo 44 — Projeto final de engenharia I

### Objetivos de aprendizagem

Você vai (1) delimitar o escopo de um projeto final de migração; (2) produzir os requisitos, a arquitetura e o plano; (3) construir um primeiro incremento; e (4) apresentar o progresso com evidências. O capítulo integra os Capítulos 20–43.

### 44.1 Enunciado do projeto final

Migre o ecossistema da BPA voltado aos parceiros — TLS de borda, VPNs com parceiros, assinaturas dos conhecimentos de embarque e exportações para a aduana — para o estabelecimento de chaves resistente à computação quântica e um caminho definido para as assinaturas, com agilidade criptográfica e medição, num programa de 18 meses. O Projeto Final I cobre do escopo até um primeiro incremento; o Projeto Final II (Capítulo 46) conclui e valida.

A janela de 18 meses é deliberadamente mais curta que uma migração completa, então os estudantes precisam escolher um primeiro incremento significativo e mostrar como o restante decorre dele. Os sistemas voltados aos parceiros são escolhidos porque combinam os dados de vida mais longa com as dependências que ditam o ritmo.

### 44.2 Entregáveis do Projeto Final I

1. Declaração de escopo e mapa das partes interessadas.
2. Requisitos com rastreabilidade (Capítulo 21).
3. Modelo de ativos e fluxos e linha de base do CBOM (Capítulos 22, 29).
4. Análise de ameaças e FMEA (Capítulo 23).
5. Arquitetura com alternativas e decisões (Capítulos 25–27).
6. Primeiro incremento: TLS híbrido na API dos parceiros num ambiente de teste, com medição.
7. Plano para o Projeto Final II, com os riscos.

Os entregáveis seguem a ordem dos capítulos anteriores do livro, então cada um se apoia num método já praticado. O primeiro incremento é o que mais importa, porque transforma planos em evidências: um ambiente de teste de TLS híbrido com medição mostra que a equipe consegue entregar, e os seus resultados alimentam o projeto do canário para a produção. O plano para o Projeto Final II lista explicitamente dependências como a compra do HSM.

### 44.3 Avaliação

Os avaliadores procuram a rastreabilidade dos requisitos ao projeto e aos testes, desconhecidos honestos no CBOM, um incremento funcionando com evidências e um plano cujas dependências estejam visíveis.

Os avaliadores rastreiam pelo menos um requisito de ponta a ponta, da fonte, passando pela decisão de projeto, até o resultado do teste, e verificam que a parcela de desconhecidos do CBOM está relatada, e não escondida. Um plano cujo caminho crítico está visível recebe mais crédito do que um com mais funcionalidades, mas sem dependências mostradas. As entregas que declaram os limites com clareza são mais bem avaliadas do que as que alegam mais do que as suas evidências sustentam.

### 44.4 Exemplo resolvido

Uma entrega-modelo do Projeto Final I identifica 37 fluxos de vida longa expostos, escolhe a troca de chaves híbrida em todo o perímetro externo, adia a migração dos certificados públicos com justificativa, demonstra o incremento da API dos parceiros com 0 falhas em 20.000 conexões de laboratório (limite superior de 95% de 1,5 × 10^-4) e lista a compra do HSM como o caminho crítico.

O limite superior vem da regra de três: três dividido por 20.000 conexões dá uma vez e meia em dez mil, o que fica dentro do orçamento de disponibilidade do REQ-AV-01. Nomear a compra do HSM como o caminho crítico mostra que a equipe entendeu o grafo de dependências do capítulo de integração, em que o HSM condicionava cinco pacotes de trabalho. O adiamento dos certificados públicos é aceito porque a justificativa cita o suporte dos navegadores e o argumento do ataque ativo.

### 44.5 Erros comuns e limites

- Escopo amplo demais para entregar um incremento.
- Nenhuma medição de linha de base.
- Planos sem dependências.

Um escopo que cobre o porto inteiro não consegue entregar um incremento funcionando no tempo disponível, então a entrega vira um plano sem evidências. Sem uma medição de linha de base, o Projeto Final II não consegue mostrar melhora, como deixa claro a linha de base acordada no início. Os planos sem dependências deixam escapar itens de prazo longo, como os HSMs, que então atrasam vários pacotes de trabalho de uma vez. Os avaliadores verificam os três pontos na primeira semana, para que as equipes ainda possam corrigi-los.

### Nota de engenharia

Mantenha um registro de decisões desde o primeiro dia do projeto final. Cada entrada registra a data, a decisão, as alternativas consideradas, as evidências e quem concordou. O registro alimenta o capítulo de arquitetura da monografia, responde rapidamente às perguntas de "por quê" dos revisores e protege a equipe quando uma descoberta posterior faz uma decisão anterior parecer errada — ele mostra o que se sabia na época. Os examinadores avaliam consistentemente melhor os projetos finais com registros de decisões claros do que os que têm projetos polidos, mas sem explicação.

### 44.6 Acordar a linha de base do projeto final

O Projeto Final I começa registrando o estado inicial da BPA: quais enlaces usam troca de chaves híbrida, quais certificados se encadeiam a raízes clássicas e quais entradas do inventário ainda não foram verificadas. O progresso no Projeto Final II é medido contra essa linha de base, para que as alegações posteriores de melhora possam ser conferidas pelo avaliador.

A linha de base é assinada pelo avaliador e guardada no dossiê antes de qualquer mudança. Ela usa os mesmos métodos de medição que o Projeto Final II vai usar, como a telemetria passiva para os grupos negociados, para que as diferenças reflitam mudanças reais, e não um método novo. As entradas desconhecidas são contadas explicitamente, já que reduzi-las é um dos objetivos do projeto final.

### Exercícios

- **EX087 — Escopo.** Escreva a declaração de escopo do projeto final, com o que está dentro e fora do escopo. Rubrica: 3 = incremento entregável, exclusões explícitas.
- **EX088 — Evidências do incremento.** Defina o pacote de evidências do primeiro incremento. Rubrica: 3 = configuração, testes, medições, rastreabilidade.

### Síntese

O Projeto Final I prova que o estudante consegue delimitar, modelar, projetar e entregar um primeiro incremento medido de uma migração com formato real.

<!-- open-cyber-academy:chapter-navigation:start ch-44 -->
### Continue estudando — capítulo 44 de 50

[← Capítulo 43](#ch-43) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 45 →](#ch-45)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-45"></a>

## Capítulo 45 — Revisão independente de projeto

### Objetivos de aprendizagem

Você vai (1) conduzir e receber uma revisão independente de projeto; (2) usar uma lista de verificação estruturada para projetos de PQC; (3) classificar as constatações por severidade; e (4) responder com mudanças ou com uma aceitação justificada. O capítulo examina o Projeto Final I antes do Projeto Final II.

### 45.1 Método de revisão

Revisores independentes da equipe de projeto leem os requisitos, a arquitetura, a análise de ameaças e as evidências e depois entrevistam a equipe. As constatações são escritas, classificadas (crítica, maior, menor, observação) e respondidas.

Independência significa que os revisores não participaram do projeto e não se reportam ao seu líder. As entrevistas testam se a equipe entende os próprios documentos; um projeto que só um membro consegue explicar já é um risco em si. Cada constatação recebe uma resposta escrita: uma mudança ou uma aceitação fundamentada do risco, com um responsável. As constatações e as respostas, juntas, fazem parte do dossiê de evidências.

### 45.2 Lista de verificação da revisão de PQC

- Todos os usos de chave pública estão inventariados, com os desconhecidos relatados?
- Os algoritmos e os conjuntos de parâmetros vêm das normas atuais (FIPS 203/204/205, SP 800-208), e as implementações da era dos rascunhos estão excluídas?
- Os combinadores híbridos são padronizados e vinculados ao contexto?
- A negociação é autenticada, e o fallback é registrado e datado?
- As chaves de assinatura com estado estão protegidas contra a reutilização?
- As âncoras de confiança de vida longa têm diversidade de algoritmos?
- A agilidade é demonstrada (tempo de substituição), e não apenas alegada?
- Os riscos de disponibilidade (tamanho, middleboxes, dispositivos) são testados?
- Os riscos residuais são declarados com honestidade?

Cada pergunta corresponde a um capítulo anterior, então uma constatação pode apontar o método que foi pulado.

### 45.3 Severidade

Crítica: uma falha de projeto que derrota o objetivo de segurança (por exemplo, um combinador XOR sem vínculo, chaves com estado em software com backups). Maior: lacuna significativa (sem monitoramento do fallback). Menor: documentação ou clareza. Observações: sugestões.

A severidade orienta o que precisa ser corrigido antes de prosseguir: as constatações críticas bloqueiam o estágio seguinte, as maiores precisam de um plano com datas, as menores são corrigidas no curso normal. Definições claras mantêm os revisores coerentes, de modo que dois revisores que avaliam o mesmo problema cheguem ao mesmo nível. Uma constatação classificada como crítica precisa explicar como ela derrota o objetivo, o que impede que o rótulo seja usado apenas para dar ênfase.

### 45.4 Exemplo resolvido

Revisão do Projeto Final I modelo: uma constatação maior — as exportações para a aduana usariam apenas ML-KEM, sem componente tradicional e sem evidências de interoperabilidade da agência; resposta: acrescentar um destinatário RSA-OAEP paralelo durante a transição e agendar o teste da agência. Uma menor — fonte de evidência do CBOM ausente em 40 registros; corrigida.

A constatação das exportações é maior, e não crítica, porque o ML-KEM sozinho não é inseguro, mas confiar nele sem um componente tradicional e sem os testes da agência arrisca tanto uma surpresa criptoanalítica quanto uma exportação ilegível. A resposta restaura a abordagem híbrida usada nos outros lugares e acrescenta um teste datado.

### 45.5 Erros comuns e limites

- Revisões feitas pela própria equipe de projeto.
- Constatações sem severidade ou sem resposta.
- Respostas defensivas em vez de mudanças ou de aceitação fundamentada.

Uma equipe de projeto que revisa a si mesma compartilha os próprios pontos cegos, por isso revisores independentes são exigidos. Constatações sem severidade não podem ser priorizadas, e constatações sem resposta tendem a ser esquecidas. As respostas defensivas desperdiçam a revisão: ou se muda o projeto, ou se aceita o risco com motivos declarados e um responsável, como mostrou a constatação das exportações, com o seu teste datado da agência e o responsável nomeado.

### Nota de engenharia

Os revisores também devem confrontar o que a equipe de projeto mediu com o que ela alegou. Amostre três métricas do painel da equipe e recalcule-as a partir das evidências brutas; as divergências revelam desvios de definição ou bugs no pipeline. Uma revisão que só lê documentos pode deixar escapar que a métrica "negociada" é, na verdade, calculada a partir dos grupos oferecidos — exatamente o tipo de erro que faz um programa parecer mais adiantado do que está.

### Exercícios

- **EX089 — Revisão.** Revise o projeto de um colega (ou o modelo) com a lista de verificação e escreva três constatações com severidade. Rubrica: 3 = específicas, acionáveis, corretamente classificadas.
- **EX090 — Resposta.** Escreva uma resposta a uma constatação maior aceitando o risco, com justificativa. Rubrica: 3 = responsável pelo risco, justificativa, data de revisão.

### Síntese

Uma revisão independente com uma lista de verificação específica de PQC e uma classificação de severidade detecta as falhas de projeto antes que se tornem implantações.

<!-- open-cyber-academy:chapter-navigation:start ch-45 -->
### Continue estudando — capítulo 45 de 50

[← Capítulo 44](#ch-44) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 46 →](#ch-46)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-46"></a>

## Capítulo 46 — Projeto final de engenharia II

### Objetivos de aprendizagem

Você vai (1) concluir a implementação do projeto final em todos os domínios; (2) executar a verificação e a validação; (3) demonstrar a agilidade; e (4) preparar as evidências para o dossiê. O capítulo segue a revisão do Capítulo 45.

### 46.1 Escopo do Projeto Final II

Concluir a troca de chaves híbrida na borda e nas VPNs com parceiros (ou PSK provisória onde os equipamentos não têm suporte), os conhecimentos de embarque com assinatura dupla e carimbos de tempo, as exportações para a aduana com destinatário duplo, a cobertura do CBOM ≥ 95% com os desconhecidos relatados e uma demonstração de agilidade.

Cada item continua um trabalho iniciado no Projeto Final I e é medido contra a sua linha de base. A meta de 95% de cobertura do CBOM coincide com o REQ-INV-01, então o projeto final testa o mesmo requisito que a produção. A demonstração de agilidade está incluída porque é o único item que mostra que o sistema pode mudar de novo depois que o projeto final termina.

### 46.2 Verificação e validação

Execute as suítes de testes dos Laboratórios de Verificação I e II contra o sistema concluído; colete a aceitação dos parceiros; produza a declaração de risco residual. Trate cada constatação da revisão com evidências.

As suítes dos dois laboratórios de verificação são executadas sem alterações, para que os resultados possam ser comparados com as execuções anteriores. A aceitação dos parceiros é coletada por parceiro, com datas. A declaração de risco residual lista o que continua clássico e quando vai mudar. Cada constatação da revisão do Projeto Final I precisa de evidências da sua resolução; uma constatação aberta impede a conclusão, a menos que o risco seja aceito explicitamente pelo dono do programa.

### 46.3 Demonstração de agilidade

Demonstre a substituição de um algoritmo por política dentro do tempo-alvo — por exemplo, trocando o grupo híbrido preferido da borda de X25519MLKEM768 para SecP256r1MLKEM768 num cenário de conformidade e depois voltando, medindo o tempo de substituição e confirmando que a telemetria acompanha.

Trocar e depois voltar prova que a mudança é reversível e que a telemetria a acompanha nas duas direções. O cronômetro começa no pedido de mudança de política e para quando a telemetria mostra o novo grupo negociado por todos os clientes que o suportam. Qualquer etapa manual necessária pelo caminho é registrada, porque cada uma é um ponto onde uma mudança real de emergência poderia travar.

### 46.4 Exemplo resolvido

Resultados-modelo: parcela híbrida na borda de 71%; VPNs — 9 de 14 parceiros com a troca de chaves adicional ML-KEM, 5 com mistura de PSK; conhecimentos de embarque com assinatura dupla desde o mês 14; exportações com destinatário duplo, aceitação da agência pendente; cobertura do CBOM de 96%, desconhecidos 4%; demonstração de agilidade: da mudança de política à negociação completa em 3 dias.

Os números são coerentes com os estágios anteriores: a parcela híbrida na borda subiu de 64% para 71%, a cobertura do CBOM de 94% para 96%, e a divisão das VPNs corresponde à opção de PSK provisória da tabela de decisão para os equipamentos mais antigos. A aceitação da agência continua pendente e é relatada como tal.

### 46.5 Erros comuns e limites

- Declarar a conclusão com constatações da revisão não resolvidas.
- Agilidade demonstrada apenas numa bancada de testes.
- Risco residual omitido.

Declarar a conclusão com constatações da revisão em aberto esconde problemas conhecidos das pessoas que vão operar o sistema. Uma demonstração de agilidade apenas numa bancada de testes não prova que o pipeline de produção consegue trocar de algoritmo, então ela é executada no ambiente réplica com a configuração de produção. Omitir o risco residual deixa as operações sem saber o que ainda precisa de atenção após a passagem. A passagem para as operações, mais adiante no projeto final, depende de os três pontos estarem corretos.

### Nota de engenharia

O Projeto Final II também é o momento de ensaiar a passagem. Escreva o runbook de operações, o procedimento de manutenção do CBOM e o procedimento de agilidade como se outra equipe fosse operar o sistema amanhã e depois peça a um colega que não trabalhou no projeto que execute uma tarefa de rotina — renovar a expiração de um fallback, acrescentar um parceiro, trocar o grupo preferido — usando apenas os documentos. Cada pergunta que ele fizer marca uma lacuna a fechar antes de o dossiê ser montado.

### 46.6 Passar o projeto final às operações

O pacote do Projeto Final II vai para a equipe de operações da BPA com as mudanças de configuração, as evidências de teste, as etapas de reversão e uma lista do que continua clássico e por quê. Um engenheiro de operações refaz a demonstração de agilidade sem o estudante presente; só quando essa repetição dá certo o projeto final conta como transferível, e não como um resultado de uma só pessoa, e qualquer etapa que tenha precisado da ajuda do estudante é reescrita.

A repetição também testa as hipóteses do runbook, como direitos de acesso que o estudante tinha, mas que a equipe de operações não tem.

### Exercícios

- **EX091 — Plano da demonstração de agilidade.** Escreva o plano da demonstração de agilidade, com critérios de sucesso. Rubrica: 3 = eventos de início e fim, evidências da telemetria, reversão.
- **EX092 — Fechamento das constatações.** Produza uma tabela de fechamento das constatações da revisão do Capítulo 45. Rubrica: 3 = cada constatação com evidências de fechamento ou risco aceito.

### Síntese

O Projeto Final II conclui a migração incremento a incremento, a verifica e valida, demonstra a agilidade e fecha as constatações da revisão com evidências.

<!-- open-cyber-academy:chapter-navigation:start ch-46 -->
### Continue estudando — capítulo 46 de 50

[← Capítulo 45](#ch-45) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 47 →](#ch-47)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-47"></a>

## Capítulo 47 — Ensaio de falha e recuperação

### Objetivos de aprendizagem

Você vai (1) projetar e conduzir um ensaio de falha controlado; (2) recuperar-se de falhas criptográficas dentro dos objetivos; (3) medir o tempo de recuperação; e (4) melhorar os planos a partir dos resultados. O capítulo testa a resiliência projetada no Capítulo 33.

### 47.1 Cenários do ensaio

Num ambiente réplica isolado: (a) vulnerabilidade numa biblioteca PQC que exige correção emergencial e troca de chaves; (b) HSM de assinatura LMS restaurado a partir de um backup — confirmar a recusa em assinar até que o estado seja reconciliado; (c) quebra de algoritmo simulada: desativar o ML-DSA na política e mudar a assinatura dos conhecimentos de embarque para a alternativa; (d) atualização de um middlebox que descarta ClientHellos grandes num local.

Os quatro cenários cobrem capacidades diferentes: a correção e a troca de chaves testam as operações; a restauração do HSM testa os controles de estado; a quebra de algoritmo testa a agilidade; a mudança no middlebox testa a resposta específica por caminho.

### 47.2 Objetivos

Defina os objetivos de tempo de recuperação: por exemplo, corrigir e trocar as chaves da borda em até 72 horas; trocar o algoritmo de assinatura em até 14 dias; exceção específica de caminho para o middlebox em até 2 horas. Meça os tempos reais.

Os objetivos vêm dos requisitos e do risco: 72 horas para a troca de chaves da borda refletem a exposição de um serviço público, enquanto 14 dias para a troca da assinatura refletem a necessidade de os verificadores dos parceiros se atualizarem. Defini-los antes do ensaio dá sentido aos resultados; os objetivos escolhidos depois tendem a coincidir com o que quer que tenha acontecido e não ensinam nada sobre a prontidão.

### 47.3 Conduzir o ensaio

Instrua os participantes; injete as falhas; observe sem ajudar; registre os tempos, as decisões e os problemas; pare se a segurança física ou a produção estiver em risco (não deveria estar — apenas réplica).

Os observadores não ajudam porque o objetivo é ver o que os runbooks e a equipe conseguem fazer sozinhos. Registrar as decisões, e não só os tempos, mostra onde as pessoas hesitaram ou improvisaram, o que muitas vezes revela uma etapa ausente no runbook. A regra de parada é declarada de antemão, mesmo sendo o ambiente uma réplica, para que os participantes saibam que ela existe e pratiquem o seu uso.

### 47.4 Exemplo resolvido

Resultados de um ensaio-modelo: (a) 41 horas; (b) o HSM recusou, mas o runbook não tinha as etapas de reconciliação — acrescentadas; (c) 19 dias, excedendo o objetivo porque os verificadores dos parceiros precisaram de atualizações — endpoints de teste para os parceiros acrescentados ao plano; (d) 35 minutos.

Três dos quatro cenários cumpriram os objetivos: 41 horas contra 72, 35 minutos contra 2 horas e o HSM recusando corretamente a assinatura. A troca da assinatura levou 19 dias contra 14 porque os verificadores dos parceiros tiveram de ser atualizados, uma dependência que a agilidade dentro da BPA não consegue remover. Acrescentar endpoints de teste para os parceiros encurta esse caminho no próximo exercício.

### 47.5 Erros comuns e limites

- Ensaios em produção.
- Objetivos definidos depois do ensaio.
- Nenhuma ação de acompanhamento.

Os ensaios em produção arriscam causar justamente os incidentes que pretendem ensaiar. Os objetivos definidos depois não conseguem mostrar se o desempenho foi bom o bastante. Sem ações de acompanhamento, o ensaio produz um relatório e nenhuma melhora; na BPA, cada lacuna, como as etapas de reconciliação ausentes, virou uma ação acompanhada e testada de novo. Um ensaio só conta como concluído quando cada ação tem um responsável, uma data e um novo teste planejado.

### Nota de engenharia

Os ensaios devem variar quem está de plantão. Uma recuperação que só funciona quando o projetista do sistema está presente não é uma capacidade de recuperação; conduza pelo menos um cenário só com a equipe de plantão e os projetistas observando em silêncio. Meça não apenas o tempo decorrido, mas também a qualidade das decisões: se a equipe consultou o CBOM, seguiu o runbook e se comunicou com os parceiros nos momentos certos. Essas observações geram as melhorias mais valiosas.

### 47.6 Acompanhar as constatações do ensaio

Cada lacuna encontrada no ensaio vira uma ação acompanhada: as etapas de reconciliação ausentes no runbook, os endpoints de teste para os parceiros e a implantação nos parceiros, mais lenta que o planejado, de 19 dias. O ensaio é repetido para os cenários que não cumpriram o objetivo, e os resultados da repetição são acrescentados ao dossiê de evidências ao lado dos originais, para que os leitores vejam tanto a falha quanto a correção.

Manter os dois resultados também mostra aos avaliadores que a equipe corrigiu o que falhou. A repetição usa o mesmo cenário e o mesmo objetivo que o original, para que a melhora seja medida em pé de igualdade. Se a repetição ainda não cumprir o objetivo, a lacuna é relatada na declaração de risco residual, e não escondida.

### Exercícios

- **EX093 — Projeto do cenário.** Projete o cenário (c) em detalhe, com as injeções e os observadores. Rubrica: 3 = realista, mensurável, isolado.
- **EX094 — Relatório pós-ação.** Escreva o relatório pós-ação do cenário (c). Rubrica: 3 = causa raiz, ações, responsáveis, datas.

### Síntese

Os ensaios de falha medem a capacidade real de recuperação contra os objetivos e transformam surpresas em melhorias do plano.

<!-- open-cyber-academy:chapter-navigation:start ch-47 -->
### Continue estudando — capítulo 47 de 50

[← Capítulo 46](#ch-46) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 48 →](#ch-48)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-48"></a>

## Capítulo 48 — Dossiê de evidências

### Objetivos de aprendizagem

Você vai (1) montar um dossiê de evidências do sistema migrado; (2) ligar as evidências aos requisitos e às alegações; (3) proteger as evidências sensíveis; e (4) tornar o dossiê revisável por auditores e sucessores. O capítulo prepara a monografia e a defesa.

### 48.1 Conteúdo

Requisitos e matriz de rastreabilidade; arquitetura e registros de decisão; instantâneos do CBOM, com o método; análises de ameaças e FMEA; relatórios de teste (KATs, interoperabilidade, rebaixamento, estado); dados de medição (grupos negociados, falhas, latência); registros de validação e de aceitação; relatórios dos ensaios de falha; declaração de risco residual; resultados da demonstração de agilidade.

Cada tipo de item responde a uma pergunta diferente do revisor: a matriz mostra o que foi exigido, os relatórios de teste mostram o que foi verificado, os dados de medição mostram o que aconteceu em operação e a declaração de risco residual mostra o que resta. Um revisor deve poder partir de qualquer alegação do resumo e chegar à sua evidência pelo índice.

### 48.2 Ligar as alegações às evidências

Toda alegação nos resumos tem um identificador de evidência. "Conexões de borda que negociam grupos híbridos: 71% (EV-MEAS-14, janela de 30 dias, telemetria passiva)". As alegações sem ligação são removidas.

O identificador diz ao leitor onde está a evidência, a janela diz quando ela foi medida e a fonte diz como. Remover as alegações sem ligação pode encurtar um resumo, mas cada frase restante pode ser verificada. A amostra de dez alegações do auditor, no exemplo do dossiê, mostra como isso funciona na prática, com cada alegação rastreada em minutos.

### 48.3 Proteger as evidências

As evidências podem revelar fraquezas. Classifique as partes do dossiê; compartilhe as partes sensíveis (detalhes de vulnerabilidades, mapas de rede) apenas com revisores autorizados; publique apenas resumos sanitizados.

Um mapa de rede que mostra quais fluxos ainda usam troca de chaves clássica é útil a um atacante que planeja gravar tráfego, por isso ele é classificado. Os resumos sanitizados substituem os nomes dos sistemas por categorias e dão totais em vez de listas. O acesso às partes classificadas é registrado, e o índice do dossiê mostra quais partes existem sem expor o seu conteúdo. A BPA revisa as classificações quando o dossiê é atualizado, já que uma lacuna fechada pode não precisar mais de proteção.

### 48.4 Revisabilidade

Use uma estrutura, um índice e um controle de versão consistentes. Um sucessor deve encontrar em minutos onde ficam as chaves ML-DSA e como substituí-las.

O dossiê da BPA segue a mesma ordem dos capítulos de verificação deste livro, com um índice que liga cada identificador de evidência ao seu arquivo. O controle de versão mostra quando cada item mudou e quem o mudou. A primeira tarefa de um engenheiro novo é responder a três perguntas a partir do dossiê, como onde ficam as chaves ML-DSA, o que testa se a estrutura funciona.

### 48.5 Exemplo resolvido

O índice do dossiê da BPA lista 126 itens de evidência. Um auditor amostra dez alegações e rastreia cada uma até a evidência em menos de uma hora; uma alegação — "todo o firmware tem assinatura dupla" — se revela válida apenas para os dispositivos com o novo bootloader; a alegação é corrigida para "todas as imagens têm assinatura dupla; 40% dos dispositivos verificam as duas".

A alegação corrigida é mais útil do que a original: ela diz às operações que 60% dos dispositivos ainda verificam apenas uma assinatura, o que é um risco residual real. Amostrar dez alegações em menos de uma hora também mostra que o dossiê é revisável, a propriedade que a parte anterior pedia.

### 48.6 Erros comuns e limites

- Alegações sem identificadores de evidência.
- Dossiês com detalhes sensíveis amplamente compartilhados.
- Evidências espalhadas por pastas pessoais.

As alegações sem identificadores não podem ser verificadas e convidam ao exagero, como mostrou a alegação do firmware. Compartilhar amplamente as partes sensíveis entrega aos atacantes um mapa das fraquezas restantes. As evidências em pastas pessoais desaparecem quando as pessoas saem, e a próxima migração começa sem elas. A BPA mantém todas as evidências no repositório versionado, com controles de acesso, e o índice é verificado quanto a links quebrados e itens ausentes antes de cada auditoria.

### Nota de engenharia

Os dossiês também precisam de um responsável pela manutenção. As evidências envelhecem: as medições ficam desatualizadas, o status das normas muda, os parceiros se atualizam. Atribua um responsável, uma frequência de revisão e uma data de expiração a cada item de evidência, para que o dossiê continue sendo uma descrição verdadeira do sistema, e não um instantâneo da semana em que foi entregue. Os auditores confiam nos dossiês que mostram o próprio histórico de atualizações.

### 48.7 Manter o dossiê atualizado

O dossiê da BPA é versionado: cada atualização declara o que mudou, por que e quem aprovou. Quando uma norma é revista ou um fornecedor lança uma nova opção pós-quântica, as alegações afetadas são verificadas de novo e as suas evidências, renovadas, e os itens desatualizados são marcados em vez de removidos em silêncio.

Um item desatualizado continua visível, com a sua data e o motivo da caducidade, para que um revisor consiga distinguir um sucesso antigo de um atual. Quando a FIPS 206 para o FN-DSA for final, por exemplo, a alegação de que o FN-DSA está excluído enquanto aguarda a normalização é revista, e o registro de decisões registra se a BPA passa a adotá-lo nos enlaces restritos.

### Exercícios

- **EX095 — Índice.** Esboce a estrutura do índice do dossiê. Rubrica: 3 = categorias, identificadores, classificação.
- **EX096 — Auditoria de alegações.** Audite cinco alegações dos resultados do Capítulo 46 diante das necessidades de evidência. Rubrica: 3 = cada uma ligada ou corrigida.

### Síntese

Um dossiê de evidências liga cada alegação a evidências protegidas e indexadas, nas quais auditores e sucessores conseguem navegar.

<!-- open-cyber-academy:chapter-navigation:start ch-48 -->
### Continue estudando — capítulo 48 de 50

[← Capítulo 47](#ch-47) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 49 →](#ch-49)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-49"></a>

## Capítulo 49 — Monografia de engenharia

### Objetivos de aprendizagem

Você vai (1) escrever uma monografia de engenharia que documente o projeto, a implementação e a validação; (2) apresentar os resultados com incerteza e limites; (3) generalizar as lições de forma responsável; e (4) cumprir os padrões de integridade acadêmica. O capítulo sintetiza o projeto final.

### 49.1 Estrutura

Introdução (problema, partes interessadas, contribuição); fundamentação (ameaça quântica, normas, híbridos, agilidade); requisitos; projeto e alternativas; implementação; verificação e validação; operações e ensaio de falha; discussão (lições, generalização, limites); conclusão e trabalhos futuros. Opcionalmente, inclua um estudo aplicado (Capítulo 42).

A estrutura espelha o ciclo de vida da engenharia, para que os leitores encontrem cada parte onde a esperam. Os examinadores muitas vezes leem primeiro a discussão dos limites, então ela precisa declarar o que o trabalho não mostrou, como a migração dos certificados no portal público. O estudo opcional se encaixa naturalmente onde orienta uma escolha de projeto ou de medição, como a comparação da telemetria que mudou o painel da BPA.

### 49.2 Resultados e limites

Relate os resultados medidos com janelas e intervalos; declare os riscos residuais; descreva os limites com a sua direção (por exemplo, "a telemetria passiva não consegue ver os algoritmos dos certificados no TLS 1.3, então o status da migração dos certificados vem apenas da configuração").

Declarar a direção de um limite diz aos leitores para que lado vai o erro: o status dos certificados obtido da configuração pode superestimar a migração, porque um certificado configurado pode não ser servido a todos os clientes. Os intervalos mostram quanto os números medidos poderiam variar. Uma monografia que relata os dois é mais fácil de confiar do que uma só com valores pontuais.

### 49.3 Generalização

Lições que se generalizam: o inventário primeiro; a troca de chaves híbrida cedo; a autenticação conforme a vida útil das âncoras de confiança; a agilidade medida; os parceiros ditam o ritmo. Lições que podem não se generalizar: taxas de falha específicas, comportamentos de fornecedores, a estrutura de dependências da BPA.

Separar as duas listas ajuda os leitores de outras organizações a decidir o que aproveitar. Um hospital ou uma concessionária de serviços públicos pode aplicar diretamente o planejamento que começa pelo inventário e a agilidade medida, mas as suas taxas de falha e os seus problemas com fornecedores serão diferentes dos da BPA. A monografia diz quais lições dependem do contexto e o que precisaria ser verificado em outro lugar.

### 49.4 Integridade

Cite as normas e a pesquisa com precisão; distinga o seu trabalho do trabalho da equipe; rotule os dados sintéticos; não divulgue informações confidenciais da instituição anfitriã.

Rotular os dados sintéticos protege os leitores de tratar os números da BPA como medições de um porto real. Distinguir o trabalho individual do trabalho da equipe importa num programa em que muitas pessoas contribuíram. Citar com precisão significa citar os números da norma, como a chave ML-KEM-768 de 1.184 bytes, e não o arredondamento de uma fonte secundária. As informações confidenciais da instituição anfitriã, como nomes de parceiros ou fraquezas não corrigidas, ficam fora da monografia, mesmo quando tornariam um exemplo mais vívido.

### 49.5 Exemplo resolvido

Um resumo-modelo de monografia: "Esta monografia projeta e valida uma migração resistente à computação quântica para o ecossistema de parceiros de uma autoridade portuária sintética. A troca de chaves híbrida X25519MLKEM768 chegou a 71% das conexões de borda sem exceder o orçamento de falhas; as VPNs com parceiros usaram trocas adicionais ML-KEM ou mistura provisória de chaves pré-compartilhadas; os conhecimentos de embarque receberam assinatura dupla com ML-DSA-65 e ECDSA, com renovação dos carimbos de tempo; um projeto orientado por política trocou o grupo híbrido preferido em três dias. Os certificados do portal público continuam clássicos; os riscos residuais e as lições generalizáveis são discutidos."

O resumo declara um resultado por área.

### 49.6 Erros comuns e limites

- Generalizar em excesso a partir de uma organização.
- Omitir os riscos residuais.
- Dados sintéticos sem rótulo.

A experiência de um porto não consegue estabelecer taxas de falha para todas as organizações, então as alegações precisam se limitar ao caso. Omitir os riscos residuais, como os certificados clássicos do portal, superestima o resultado. Dados sintéticos sem rótulo podem ser confundidos com medições de campo e citados em outros lugares como fatos. Cada um desses pontos é verificado pelo orientador antes da entrega, usando como referências a declaração de risco residual e os rótulos dos dados no dossiê de evidências.

### Nota de engenharia

Escreva a monografia de modo que um profissional de outra organização consiga reutilizá-la. Inclua como apêndices os modelos de requisitos, o esquema do CBOM, o formato da lista de permissões da política e os planos de teste, com exemplos sintéticos. Os artefatos reutilizáveis multiplicam o valor do trabalho e muitas vezes são o que os examinadores e os empregadores lembram. Mantenha fora os detalhes confidenciais e rotule cada número que vem do caso sintético da BPA.

### Exercícios

- **EX097 — Resumo.** Escreva o resumo da sua monografia (200 palavras). Rubrica: 3 = problema, método, resultados com números, limites.
- **EX098 — Tabela de generalização.** Separe dez lições em "provavelmente gerais" e "específicas do contexto". Rubrica: 3 = classificação justificada.

### Síntese

A monografia registra um projeto validado, com resultados e limites honestos, e separa as lições gerais das locais.

<!-- open-cyber-academy:chapter-navigation:start ch-49 -->
### Continue estudando — capítulo 49 de 50

[← Capítulo 48](#ch-48) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 50 →](#ch-50)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-50"></a>

## Capítulo 50 — Defesa final

### Objetivos de aprendizagem

Você vai (1) apresentar e defender a monografia de engenharia; (2) responder a perguntas técnicas, éticas e de gestão; (3) demonstrar o sistema ou as suas evidências; e (4) definir um plano futuro para a próxima mudança criptográfica do sistema. O capítulo conclui o curso.

### 50.1 Apresentação

Vinte minutos: problema e o que está em jogo; requisitos; arquitetura e decisões-chave; resultados com evidências; falhas e recuperação; risco residual; o que você faria de outro modo. Use diagramas com alternativas em texto.

Vinte minutos é pouco, então cada parte recebe cerca de três minutos, com o maior cuidado dado aos resultados e ao risco residual. A pergunta final, o que você faria de outro modo, mostra reflexão e muitas vezes provoca a pergunta de acompanhamento mais útil da banca. As alternativas em texto para os diagramas ajudam os membros da banca que usam leitores de tela e obrigam o apresentador a dizer em palavras o ponto de cada diagrama.

### 50.2 Perguntas prováveis

- Por que híbrido em vez de PQC pura? (Proteção contra surpresas criptoanalíticas; citar Rainbow/SIKE; custo aceito.)
- Por que os certificados do portal ainda são clássicos? (Os ataques quânticos ativos precisam de um CRQC no momento da conexão; suporte do ecossistema e tamanho; plano e gatilho para a mudança.)
- Como você sabe que o fallback não é um caminho de rebaixamento? (Autenticação da transcrição; fallback registrado e datado; teste de rebaixamento no laboratório.)
- O que acontece se o ML-KEM for quebrado? (O X25519 ainda protege contra atacantes clássicos; caminho de agilidade para uma alternativa como o HQC, quando for padronizado; tempo de substituição medido.)
- O que você faria com o dobro do orçamento? (Priorizar por exposição ÷ esforço.)

### 50.3 Demonstração

Mostre o painel, uma mudança de algoritmo orientada por política no ambiente réplica e o rastreamento de uma alegação no dossiê.

Cada parte da demonstração sustenta uma alegação diferente: o painel mostra a medição em operação, a mudança de política mostra a agilidade e o rastreamento no dossiê mostra que os resultados se apoiam em evidências. Executá-la no ambiente réplica evita qualquer risco para os serviços da BPA. O apresentador ensaia cada etapa com um cronômetro e tem capturas de tela prontas caso o ambiente falhe durante a defesa.

### 50.4 Plano futuro

A agilidade é o legado: agende a reverificação das normas (FN-DSA, HQC, IR 8547 revisado), exercícios de mesa anuais de quebra de algoritmo, a automação da atualização do CBOM e revisões com os parceiros.

Cada item tem um responsável e uma data, para que o plano sobreviva ao fim do programa. Reverificar as normas detecta mudanças como uma norma final do FN-DSA ou a publicação do HQC, que acrescentariam opções para a BPA. Os exercícios de mesa anuais mantêm atualizado o número do tempo de substituição, enquanto as revisões com os parceiros acompanham os caminhos clássicos restantes rumo às suas datas de desativação e sinalizam qualquer atraso.

### 50.5 Erros comuns e limites

- Alegar que a organização é "segura contra a computação quântica".
- Nenhuma resposta para o comprometimento de um algoritmo.
- Demonstrações que dependem dos sistemas de produção.

Alegar ser "seguro contra a computação quântica" convida a banca a listar os certificados clássicos e os ativos desconhecidos que restam. Sem uma resposta para o comprometimento de um algoritmo, o trabalho de agilidade não tem propósito visível. Uma demonstração que precisa dos sistemas de produção arrisca uma interrupção durante a defesa e não pode ser repetida depois pelos revisores; o ambiente réplica evita os dois problemas. Os candidatos que preparam respostas honestas sobre esses pontos costumam achar mais fáceis as perguntas da banca.

### Nota de engenharia

Depois da defesa, entregue o sistema aos seus donos com uma carta curta que declare o que foi alcançado, o que resta, as datas das próximas expirações e revisões e como contatar as pessoas que conhecem o projeto. A prontidão quântica depende mais da continuidade do que de qualquer engenheiro individual, então o ato final do curso é garantir que a capacidade sobreviva ao fim do projeto e que a próxima mudança de algoritmo encontre uma equipe preparada.

### Exercícios

- **EX099 — Respostas da defesa.** Escreva respostas às cinco perguntas de 50.2 para o seu próprio projeto final. Rubrica: 3 = baseadas em evidências, delimitadas.
- **EX100 — Plano futuro.** Escreva o plano futuro de dois anos para a criptografia da BPA após o projeto final. Rubrica: 3 = reverificação, exercícios de mesa, inventário, marcos com os parceiros.

### Síntese

A defesa mostra uma migração validada, medida e ágil, responde a perguntas difíceis com evidências e deixa um plano para a próxima mudança — porque a prontidão quântica é uma capacidade, não uma linha de chegada.

<!-- open-cyber-academy:chapter-navigation:start ch-50 -->
### Continue estudando — capítulo 50 de 50

[← Capítulo 49](#ch-49) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre a BPA são sintéticos.

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

**EX021.** 540 + 32 + 4 = 576 B → um segmento; 540 + 1.216 + 4 = 1.760 B → dois segmentos.

**EX022.** TLS: ambos (a troca de chaves primeiro). IKEv2: principalmente troca de chaves (a autenticação depois). SSH: ambos (a troca de chaves implantada primeiro). DNSSEC: assinaturas.

**EX023.** Biblioteca do sistema (consultas ao gerenciador de pacotes), bibliotecas embutidas/ligadas estaticamente (varredura de binários), configuração de provedores em tempo de execução (análise de configuração), chaves guardadas em HSM/TPM (inventário PKCS#11/de dispositivos).

**EX024.** Os dispositivos vivem 10–20 anos e verificam o firmware offline; um esquema de assinatura falsificável dentro desse tempo de vida permite a um atacante instalar firmware malicioso; os bootloaders são difíceis de atualizar, então a âncora de confiança precisa ser escolhida cedo.

**EX025.** Fluxo de status dos contêineres (dias), logs operacionais do terminal (1 ano), conhecimentos de embarque (12 anos de integridade), declarações aduaneiras (25 anos de confidencialidade), registros de RH (décadas), imagens das câmeras de segurança (semanas a meses). Os tempos de vida mais longos primeiro.

**EX026.** O encapsulamento de chave RSA-OAEP; substitua por um destinatário KEM (ML-KEM via KEMRecipientInfo do CMS, RFC 9629), opcionalmente ao lado do RSA durante a transição.

**EX027.** Algoritmo vindo da política; conjunto de parâmetros aprovado; comprimentos validados; comparações em tempo constante; biblioteca fixada e na versão da norma final; KATs passando; testes de interoperabilidade; fallback registrado; plano de reversão; CBOM atualizado.

**EX028.** Id do ativo, endpoint, protocolo/versão, grupos de troca de chaves oferecidos e negociados, algoritmo de assinatura, emissor/validade/algoritmo da chave do certificado, biblioteca e versão, local de armazenamento da chave, responsável, fonte da evidência, última observação.

**EX029.** Portal: categoria 3 (ML-KEM-768 no X25519MLKEM768), equilibrando margem e tamanho; parceiro de segurança nacional: categoria 5 (ML-KEM-1024, ML-DSA-87), como exige o CNSA 2.0.

**EX030.** Tráfego de VPN: colete agora, decifre depois; assinaturas de firmware: falsificação futura contra raízes de vida longa; conhecimentos de embarque: falsificação de assinaturas arquivadas.

**EX031.** Por exemplo, "VPN da companhia de navegação — IKEv2 ECDH P-384 → IKEv2 + ML-KEM-768 (RFC 9370) — responsáveis: rede da BPA + parceiro — meta: 3º trimestre do ano que vem"; linhas semelhantes para a exportação aduaneira, o TLS de borda, a assinatura de firmware e o HSM.

**EX032.** Pesos definidos primeiro (segurança 0,35, disponibilidade 0,25, normas 0,15, prontidão dos parceiros 0,15, custo 0,10); notas por opção; a verificação de sensibilidade mostra se a vencedora muda quando o peso da disponibilidade sobe.

**EX033.** Antecedentes: cobertura do CBOM, compromissos de PQC dos fornecedores, prontidão do ambiente de testes. Consequentes: parcela híbrida negociada, parcela de documentos com assinatura dupla, tendência da parcela de ativos desconhecidos. Cada um com um responsável.

**EX034.** Promover quando o limite superior ≤ linha de base + orçamento; manter quando estiver entre o orçamento e 2× o orçamento; reverter apenas o caminho afetado quando o limite inferior exceder 2× o orçamento — limiares diferentes evitam a oscilação.

**EX035.** Internet→portal: troca de chaves TLS X25519, certificado RSA; BPA→companhia de navegação: IKEv2 ECDH, certificado ECDSA; terminal→guindastes: assinaturas RSA de firmware; BPA→aduana: cifragem de arquivos RSA-OAEP.

**EX036.** A favor: um só lugar para ativar os híbridos e monitorar a negociação, agilidade rápida. Contra: ponto único de falha e concentração de chaves; mitigue com redundância e chaves apoiadas em HSM.

**EX037.** Cada assinatura revela um de dois segredos por bit do resumo; duas mensagens cujos resumos diferem na posição *i* revelam ali os dois segredos; com os dois segredos conhecidos em muitas posições, um atacante pode montar assinaturas para outros resumos que usem apenas valores revelados.

**EX038.** (a) ML-DSA (uso geral, suporte do ecossistema); (b) LMS/XMSS se o HSM de assinatura gerenciar o estado (verificador pequeno), ou ML-DSA caso contrário; (c) SLH-DSA para o máximo de conservadorismo, dada a baixa frequência de assinatura, ou ML-DSA-87 se o tamanho importar.

**EX039.** Aduana (x=25, y=5 como em 20.2 → atrasada para todo z < 30); VPN dos parceiros (x=10, y=1,5 → atrasada se z ≤ 11,5); firmware (x=15, y=3 → atrasado se z ≤ 18); portal (x=1, y=0,5 → não atrasado); telemetria (x≈0,1 → não atrasada).

**EX040.** Precisa informar FIPS 203/204/205 finais (agosto de 2024), SP 800-208, SP 800-227 final (setembro de 2025), HQC selecionado (IR 8545, março de 2025) com a norma pendente, FN-DSA pendente, IR 8547 em rascunho.

**EX041.** "REQ-VPN-01: Todos os túneis IKEv2 com parceiros deverão executar uma troca de chaves adicional ML-KEM-768 (ou mais forte), conforme o RFC 9370, quando o par a suportar; caso contrário, mistura de PSK conforme o RFC 8784 até uma data de desativação definida. Verificação: os logs dos gateways mostram trocas negociadas em 100% dos túneis."

**EX042.** Cinco requisitos, cada um com fonte (tempo de vida dos dados, política, contrato com parceiro) e método (teste, inspeção, demonstração, análise).

**EX043.** CryptoUse{asset_id: str, function: enum[key-exchange, signature, encryption, hash, unknown], algorithm: str, parameter_set: str|None, protocol: str|None, library: str|None, evidence_source: enum[code, config, passive, vendor, endpoint-log], last_observed: datetime}.

**EX044.** `for flow in flows: if flow.lifetime is None or flow.kex is None: report(flow, "unknown"); elif flow.lifetime >= T and flow.kex in VULNERABLE and flow.recordable: report(flow, "exposed")`.

**EX045.** Coleta (mitigar: troca de chaves PQ/PSK), falsificação futura (autenticação de vida curta, migrar depois), rebaixamento (negociação autenticada, sem fallback silencioso), ataques de implementação (bibliotecas verificadas em tempo constante, correções), surpresa criptoanalítica (híbrido, agilidade).

**EX046.** Causa: o middlebox lê só o primeiro segmento; efeito: conexões reiniciadas, interrupções num caminho; detecção: telemetria de falhas por caminho e traces de pacotes; mitigação: atualização de firmware, exceção de caminho com expiração; prioridade: alta.

**EX047.** Com ±150, cerca de 1.880/2.000 bits são decifrados corretamente; com ±300, apenas cerca de 1.272/2.000: a soma de ~32 erros cresce com o tamanho dos erros até muitas vezes passar de *q*/4 ≈ 832, e o arredondamento falha. Os esquemas reais escolhem o ruído de modo que a probabilidade de falha seja desprezível.

**EX048.** "Quando chega um texto cifrado, o ML-KEM o decifra, recifra o resultado e compara. Se forem diferentes, ele devolve uma chave pseudoaleatória derivada de um segredo, em vez de um erro. Um atacante que envia textos cifrados forjados não aprende nada com o sucesso ou a falha — desde que a comparação e a seleção levem o mesmo tempo em qualquer caso."

**EX049.** Diagrama de clientes, CDN, proxy de borda, proxy de inspeção e APIs, com alternativa em texto; alternativas (híbrido agora vs. esperar suporte nativo do fornecedor); pesos fixados antes da pontuação.

**EX050.** O TLS 1.3 assina a transcrição do handshake, então a remoção dos grupos híbridos é detectada, a menos que a autenticação seja quebrada; o risco residual é uma lógica de novas tentativas na aplicação que recorre ao fallback após qualquer erro — registrada, restrita a erros de incompatibilidade conhecidos e com data de remoção.

**EX051.** O híbrido exige quebrar tanto o X25519 quanto o ML-KEM-768; o Rainbow e o SIKE mostram que esquemas novos podem cair inesperadamente; o custo é de ~2,3 kB por handshake e algum risco de middlebox, aceitável para o portal.

**EX052.** Gerar PSKs de 256 bits por par, distribuir fora de banda, misturar conforme o RFC 8784, rotacionar a cada 90 dias com sobreposição, desativar quando o equipamento for substituído (com data).

**EX053.** Calcular o hash só do segredo PQ descarta a proteção clássica: se o ML-KEM fosse quebrado, a sessão cairia junto. Use o combinador padrão por concatenação, com vínculo à transcrição.

**EX054.** Borda: X25519MLKEM768, SecP256r1MLKEM768; fallback X25519 até uma data declarada. Interno: híbrido onde as bibliotecas suportarem; clássico permitido para telemetria até uma data declarada. Enlace de segurança nacional: apenas ML-KEM-1024.

**EX055.** Implementa as FIPS 203/204/205 finais (não os rascunhos); tempo constante, com evidência; passa nos KATs; manutenção ativa e alertas de segurança; validação no CMVP onde exigida; licença clara; histórico de interoperabilidade.

**EX056.** Chaves LMS separadas por local (ou subárvores HSS particionadas), contadores monotônicos impostos pelo HSM, nenhuma restauração de estado a partir de backup, alertas em 50%/80%, troca de chave documentada.

**EX057.** Acrescente `("vpn-2", "key-exchange", "IKEv2 ML-KEM-768 + ECDH", "config")`; mude o teste de híbrido para `"ML-KEM" in alg or "MLKEM" in alg`.

**EX058.** Cobertura = ativos com ≥ 1 determinação ÷ ativos no registro, mensal, todas as fontes. Parcela híbrida negociada = conexões que negociam grupos PQ/T ÷ conexões, janela de 30 dias, telemetria passiva, por serviço e classe de dados.

**EX059.** Texto cifrado de comprimento errado; texto cifrado com um bit invertido (esperar a chave de rejeição implícita, sem vazamento de erro); chave de desencapsulamento que falha na verificação de hash; chave de encapsulamento que falha na verificação de módulo; o desencapsulamento repetido da mesma entrada devolve a mesma chave.

**EX060.** Assinantes (HSM A, HSM B) × verificadores (BPA, três sistemas de parceiros, aduana) × formatos (documento com assinatura dupla), com os resultados de verificação esperados, incluindo casos negativos.

**EX061.** A divisão de um segredo por uma constante pode ser compilada em instruções de tempo variável em algumas plataformas; use multiplicação no estilo de Barrett por um recíproco pré-calculado e deslocamentos.

**EX062.** Uma falha injetada que pula a verificação; contramedidas: verificar duas vezes por caminhos de código diferentes e conferir um hash da imagem carregada após o boot.

**EX063.** Fallback apenas para o X25519; registrar o motivo; alertar acima de um limiar; a permissão expira numa data; nunca fazer fallback em falha de autenticação.

**EX064.** 15 × 60 × 24 × 365 ≈ 7,9 milhões de assinaturas por ano > 1.048.576 — insuficiente; use HSS de vários níveis com mais capacidade, várias chaves ou ML-DSA para esse volume.

**EX065.** Laboratório → unidade reserva (1 semana) → um guindaste de baixo impacto (1 semana) → um terminal (1 semana) → todos; imagem de reversão verificada com a chave antiga em cada anel.

**EX066.** O CBOM identifica o ML-DSA-65 nos conhecimentos de embarque; alternativa: o ECDSA continua válido no curto prazo, mais a mudança para o SLH-DSA ou outro nível do ML-DSA; renovação dos carimbos de tempo; meta de 14 dias; atualizações dos verificadores dos parceiros como dependência.

**EX067.** HSM → PKI → assinatura de documentos e assinatura de firmware; prontidão dos parceiros → VPN e documentos; prontidão da aduana → exportações; TLS de borda em grande parte independente.

**EX068.** O aviso lista os grupos suportados (X25519MLKEM768), o endpoint de teste, o cronograma, a desativação das propostas de VPN somente clássicas e o contato.

**EX069.** Dois campos de assinatura (ECDSA, ML-DSA-65), tokens de carimbo de tempo, política: qualquer uma válida até uma data, as duas exigidas depois; calendário de renovação dos carimbos de tempo de arquivo.

**EX070.** A diversidade significa que o comprometimento de um algoritmo não deixa os dispositivos sem saída; custos: tamanho do código do bootloader e assinatura dupla de cada imagem.

**EX071.** 1 × (1.312 + 2.420 + 400) + 2.420 = 6.552 bytes.

**EX072.** Medir a latência de handshake p50/p95/p99 para certificados clássicos vs. híbrido vs. certificados PQ no caminho por satélite, ≥ 1.000 handshakes por condição, nas mesmas janelas de tempo.

**EX073.** Limite superior para 30/50.000 ≈ 0,00086 ≤ 0,0009 → PROMOVER (por pouco); uma equipe cautelosa poderia estender a observação.

**EX074.** Verificar as mudanças recentes, decompor o fallback por cliente e caminho, comparar com os alertas dos fornecedores, aplicar uma exceção de caminho se for local, escalar para a segurança se o fallback não tiver motivo de incompatibilidade.

**EX075.** Lista os certificados clássicos do portal (revisão anual), 5 VPNs com mistura de PSK (substituição no próximo orçamento), dispositivos com bootloaders de chave única (datas de renovação), ativos desconhecidos 6% (responsáveis nomeados).

**EX076.** Ponto de observação externo capturando uma amostra aleatória de 2.000 handshakes por semana; comparar a parcela negociada com a telemetria interna; investigar diferenças > 2 pontos.

**EX077.** Acrescente `"hmac-sha512"` ao registro e uma verificação `RETIRE = {"hmac-sha256": date(...)}` em `check` que rejeita após a data.

**EX078.** Início: mudança de política incorporada; fim: ≥ 99% dos clientes que oferecem o novo grupo o negociam; evidência: série temporal da telemetria e chamado de mudança.

**EX079.** Laboratório isolado com proxy MITM; remover os grupos híbridos; esperar falha do handshake ou nova tentativa registrada e permitida pela política; reprovar se ocorrer uma conexão silenciosa somente clássica onde a política a proíbe.

**EX080.** Restaurar o backup do HSM → assinatura recusada até a reconciliação; 100 pedidos simultâneos → todos os índices únicos; esgotar a árvore de teste → recusa limpa e alerta.

**EX081.** Por exemplo, VPN legada (exposição 9, esforço 3 → 3,0), exportações para a aduana (8, 2 → 4,0), enlaces com navios (4, 2 → 2,0), replicação do banco de dados interno (6, 1 → 6,0), telemetria (1, 1 → 1,0): ordem replicação, exportações, VPN, navios, telemetria.

**EX082.** A retomada dispensa a transmissão dos certificados para clientes recorrentes, removendo a maior parte dos bytes da cadeia PQ; mantenha a retomada com troca de chaves (EC)DHE/híbrida para preservar o sigilo futuro.

**EX083.** Por exemplo, "Nos nossos 300 serviços, que parcela dos clientes com capacidade híbrida recorre a grupos clássicos, e por quê?", com janela de telemetria e categorias.

**EX084.** Responde a cada verificação: grandeza medida, linha de base, disponibilidade do código/dados, data e versões dos algoritmos.

**EX085.** Chamado: serviço, mudança (ativar X25519MLKEM768), risco (middlebox), testes (matriz de interoperabilidade), aprovação, reversão (reverter a política), monitoramento.

**EX086.** Uma reflexão analítica de 300 palavras sobre, por exemplo, a lacuna entre o marketing de "pronto para PQC" e as funcionalidades entregues.

**EX087.** Dentro do escopo: incremento de TLS híbrido na API dos parceiros, linha de base do CBOM, requisitos, arquitetura; fora: certificados públicos, telemetria interna, renovação de dispositivos.

**EX088.** Arquivos de configuração, resultados de interoperabilidade, medição de laboratório com 20.000 conexões e o seu limite, links de rastreabilidade, teste de reversão.

**EX089.** Constatações como "fallback sem data (maior)", "fonte de evidência do CBOM ausente (menor)", "bootloader de chave única (crítica para dispositivos de vida longa)".

**EX090.** Aceitar os certificados clássicos do portal: responsável pelo risco, o CISO; justificativa (nenhum ataque quântico ativo é possível hoje; ecossistema); revisão anual ou mediante gatilho.

**EX091.** Trocar o grupo preferido por política, medir até 99% de negociação, confirmar a telemetria e a reversão; sucesso se em até 7 dias, sem violar o orçamento de falhas.

**EX092.** Tabela das constatações com evidências de fechamento (exportações com destinatário duplo, fontes do CBOM acrescentadas) ou riscos aceitos, com responsáveis.

**EX093.** Injeção: "ataque prático contra o ML-DSA-65 publicado"; os observadores cronometram a consulta ao CBOM, a decisão, a mudança de política e os avisos aos parceiros; apenas réplica isolada.

**EX094.** Causa raiz da troca em 19 dias: os verificadores dos parceiros; ações: endpoints de teste para os parceiros, algoritmo alternativo previamente acordado, responsáveis e datas.

**EX095.** Seções: requisitos, projeto, inventário, testes, medições, validação, ensaios, risco; IDs EV-REQ-nn etc.; classificação por item.

**EX096.** "71% híbrido" → EV-MEAS; "9 de 14 parceiros" → EV-VAL; "agilidade em 3 dias" → EV-AGIL; "todo o firmware tem assinatura dupla" → corrigida para imagens vs. dispositivos; "CBOM 96%" → EV-INV.

**EX097.** Um resumo de 200 palavras com problema, método, resultados numéricos e limites, por exemplo como em 49.5.

**EX098.** Gerais: o inventário primeiro, híbridos cedo, diversidade das âncoras de confiança, agilidade medida, ritmo ditado pelos parceiros. Específicas: taxas de falha, prazos dos fornecedores, grafo de dependências da BPA, números de latência, escolhas de PSK.

**EX099.** Respostas baseadas em evidências às perguntas de 50.2, citando o dossiê.

**EX100.** Ano 1: reverificar o status do FN-DSA/HQC/IR 8547, automação do CBOM, exercício de mesa; ano 2: decisão sobre os certificados do portal, substituições restantes das VPNs, marcos com os parceiros, segundo exercício de mesa.

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
