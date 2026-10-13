# Segurança Quântica e Pós-Quântica: Fundamentos para Decisões Defensáveis

- Idioma: português do Brasil (`pt`); curso de bacharelado, quatro anos; aproximadamente 3.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 40 já estão escritos em português, com os exercícios EX001–EX040 e suas resoluções; os capítulos 21–40 (EX041–EX080) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de segurança e computação em sentido amplo que precisam de fundamentos duradouros — matemática, sistemas, redes, conceitos criptográficos, evidências e ética — e, depois, de um primeiro estudo cuidadoso da ameaça quântica e da criptografia pós-quântica (PQC). Conhecimento de entrada: matemática do ensino médio, computação básica e comunicação escrita.
- Relação com os livros vizinhos: o [livro de engenharia](../../../../engineering-5-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) projeta e constrói migrações; os livros de [mestrado](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) e de [doutorado](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) as estudam empiricamente. **Este livro constrói os fundamentos e o hábito de comparar alternativas com hipóteses e evidências explícitas.**
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é um título credenciado. Não concede autorização para testar sistemas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública. A criptografia de brinquedo dos laboratórios é deliberadamente insegura; sistemas reais devem usar implementações verificadas da [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), da [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), da [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) e da [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208).

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Quarenta capítulos se distribuem ao longo de quatro anos: fundamentos gerais (1–18), o núcleo quântico e pós-quântico (19–32) e pesquisa, projeto e trabalho final (33–40). Cada capítulo tem objetivos de aprendizagem, ensino, um exemplo resolvido, uma atividade prática, erros comuns, dois exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com Python 3; a saída impressa é mostrada para que você possa conferir a sua execução.

### O caso contínuo: Harbourline Credit Union

A **Harbourline Credit Union (HCU)** é uma cooperativa financeira sintética, pertencente aos seus associados, com 40 agências. Ela opera um sistema bancário central, um aplicativo móvel, terminais de cartão e caixas eletrônicos, VPNs entre as agências e o data center, uma autoridade certificadora interna e um arquivo de documentos de financiamento imobiliário que precisam permanecer confidenciais e verificáveis por 30 anos. O seu conselho faz uma pergunta simples — "o que a computação quântica significa para nós?" — e o livro a responde passo a passo. Todos os números sobre a HCU são inventados.

### Política de fontes

As fontes primárias foram verificadas em 12 de outubro de 2026: NIST FIPS 203/204/205 (agosto de 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (rascunho público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) e [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). O FN-DSA (FIPS 206) e a norma do HQC ainda estavam em desenvolvimento. Verifique a situação de novo antes de se apoiar nela.

## Sumário

1. [Raciocínio matemático](#ch-01)
2. [Sistemas computacionais](#ch-02)
3. [Programação I](#ch-03)
4. [Escrita acadêmica](#ch-04)
5. [Letramento em segurança](#ch-05)
6. [Estruturas discretas](#ch-06)
7. [Redes e protocolos](#ch-07)
8. [Programação II](#ch-08)
9. [Dados e bancos de dados](#ch-09)
10. [Ética e prática autorizada](#ch-10)
11. [Sistemas operacionais](#ch-11)
12. [Probabilidade e estatística](#ch-12)
13. [Identidade e acesso](#ch-13)
14. [Fundamentos de privacidade](#ch-14)
15. [Evidências e medição](#ch-15)
16. [Arquitetura de segurança](#ch-16)
17. [Conceitos de criptografia](#ch-17)
18. [Métodos de pesquisa I](#ch-18)
19. [Segurança quântica e pós-quântica: escopo e teoria](#ch-19)
20. [Segurança quântica e pós-quântica: casos fundamentais](#ch-20)

Capítulos 21–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) ler e escrever uma demonstração curta por argumento direto, por contradição e por indução; (2) comparar taxas de crescimento usando logaritmos e a notação O grande; (3) explicar por que "com que rapidez cresce o custo do ataque?" é a pergunta central da criptografia; e (4) distinguir uma afirmação matemática de uma estimativa empírica. O capítulo prepara as estruturas discretas (Capítulo 6) e a probabilidade (Capítulo 12).

### 1.1 Por que estudantes de segurança precisam de demonstrações

Uma afirmação de segurança é um enunciado sobre *todo* atacante dentro de um modelo, e não sobre os atacantes que por acaso testamos. Testar uma fechadura com dez gazuas mostra que ela resistiu a dez gazuas; não mostra que resiste à décima primeira. A matemática é a única ferramenta que nos permite fazer afirmações do tipo "para todo", e ela o faz enunciando as hipóteses com precisão. Quando uma norma diz que um esquema é seguro "se o problema Module-LWE for difícil", essa frase é um teorema condicional: a conclusão é tão forte quanto a hipótese, e a hipótese se apoia em décadas de ataques fracassados, e não numa demonstração. Aprender a separar a parte demonstrada da parte suposta é o hábito matemático mais útil deste livro.

Três formas de demonstração se repetem. Uma *demonstração direta* encadeia afirmações verdadeiras até a conclusão. Uma *demonstração por contradição* supõe o contrário e deriva algo impossível; a demonstração de Euclides de que existem infinitos primos é o exemplo clássico e sustenta por que os módulos RSA podem ser escolhidos livremente. A *indução* demonstra um caso base e um passo de *n* para *n*+1; é assim que raciocinamos sobre laços, cadeias de hash e os contadores dentro das assinaturas com estado.

### 1.2 Taxas de crescimento

Os criptógrafos medem a segurança em bits: um problema de "128 bits" exige cerca de 2^128 operações básicas. Os logaritmos convertem entre escalas: log₂(10^30) ≈ 100, então 10^30 operações são cerca de 2^100. A notação O grande mantém apenas o termo dominante: um algoritmo que executa 3*n*³ + 50*n* passos é O(*n*³). A ameaça quântica é, no fundo, uma mudança na taxa de crescimento. Classicamente, o melhor algoritmo de fatoração conhecido cresce de forma *subexponencial* no comprimento em bits do número; o algoritmo de Shor (Shor, 1997) cresce de forma *polinomial*, aproximadamente como *n*³ operações lógicas. Para a busca de chaves por força bruta, o algoritmo de Grover (Grover, 1996) apenas reduz 2^*k* tentativas a cerca de 2^(*k*/2) iterações sequenciais. Uma das mudanças é um colapso; a outra é uma raiz quadrada que chaves mais longas absorvem.

### 1.3 Exemplo resolvido

O gerente de TI da HCU lê uma manchete dizendo que os computadores quânticos vão "quebrar toda a criptografia". Usando as taxas de crescimento, classificamos a criptografia da HCU. O RSA-2048 e as chaves de curvas elípticas protegem os logins e a troca de chaves da VPN: existe um ataque de tempo polinomial num grande computador quântico tolerante a falhas, então eles precisam ser substituídos. O AES-256 cifra o banco de dados: o Grover deixa cerca de 2^128 de trabalho sequencial, ainda muito além do alcance, então ele fica. A manchete erra no seu alcance, e a correção vem de uma comparação de crescimento, e não de uma opinião.

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

Leia a saída como uma tabela de taxas de crescimento, e não como tempos de execução previstos: os números ignoram constantes, correção de erros e velocidade do hardware, que o Capítulo 19 trata como hipóteses explícitas.

Dois contrastes se destacam. Para as chaves simétricas, a busca de Grover reduz o expoente à metade, então uma chave de 256 bits ainda deixa um problema muito grande. Para o RSA, a distância é bem maior: o custo clássico cresce mais rápido que qualquer polinômio no tamanho da chave, enquanto o custo de Shor cresce apenas como o seu cubo. Dobrar a chave de 1024 para 2048 bits acrescenta muito trabalho clássico, mas apenas alguns bits de trabalho quântico. Essa diferença é a razão pela qual o RSA precisa ser substituído, e não alongado.

### 1.5 Erros comuns e limites

- Tratar "seguro se o problema X for difícil" como uma demonstração incondicional.
- Comparar contagens de operações entre máquinas como se uma porta quântica e uma instrução clássica custassem o mesmo.
- Ler as estimativas heurísticas de fatoração como exatas; elas são guias de ordem de grandeza.

Cada erro vem de esquecer o que o cálculo deixa de fora. As demonstrações de segurança são condicionais, então a condição precisa ser declarada ao lado do resultado. As contagens de operações comparam crescimento, e não tempo de relógio, já que uma única operação quântica com correção de erros pode levar muito mais tempo que uma clássica. As estimativas heurísticas são úteis para decidir quais algoritmos estão em perigo, não para prever uma data. Um estudante cuidadoso escreve a hipótese ao lado de cada número.

### Exercícios

- **EX001 — Bits de trabalho.** Expresse 10^24 operações e 10^24 × 2^20 operações em bits de trabalho. Rubrica: 3 = os dois corretos, com o logaritmo mostrado.
- **EX002 — Forma da demonstração.** Demonstre por indução que uma cadeia de hash de comprimento *n*, construída como h₁ = H(s), h_{k+1} = H(h_k), exige exatamente *n* avaliações de hash. Rubrica: 3 = caso base, passo e conclusão enunciados.

### Síntese

Os argumentos de segurança combinam implicações demonstradas com problemas difíceis supostos. A ameaça quântica é uma mudança na taxa de crescimento: o Shor, de tempo polinomial, derruba a fatoração e os logaritmos discretos, enquanto o Grover apenas reduz à metade o expoente da busca de chaves.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 40

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever as camadas de um sistema computacional, do hardware à aplicação; (2) explicar onde o código criptográfico e as chaves ficam em cada camada; (3) contrastar, no nível conceitual, os bits clássicos com os qubits; e (4) mapear um serviço da HCU nessas camadas.

### 2.1 Camadas e onde fica a criptografia

Um serviço moderno é uma pilha. Na base ficam os processadores, a memória, o armazenamento e as interfaces de rede; acima deles, o firmware inicializa a máquina, um sistema operacional gerencia os recursos, as bibliotecas oferecem funções compartilhadas e as aplicações entregam as funcionalidades. A criptografia aparece em quase todas as camadas. O firmware verifica as assinaturas do estágio seguinte do boot. O sistema operacional guarda chaves e oferece um provedor criptográfico. Bibliotecas como as pilhas TLS negociam algoritmos com pares remotos. As aplicações assinam documentos ou cifram campos. Os módulos de segurança de hardware (HSMs) e os cartões inteligentes são pequenos computadores cujo único propósito é manter as chaves dentro de uma fronteira.

Essa divisão em camadas importa para a migração. Substituir um algoritmo numa aplicação é uma nova versão de software; substituí-lo na ROM de boot de um terminal de cartão pode exigir a troca do dispositivo. Os estudantes que conseguem localizar cada uso criptográfico na pilha conseguem estimar quão difícil será mudá-lo, e essa estimativa orienta todos os planos posteriores deste livro.

### 2.2 Bits, qubits e o que são os computadores quânticos

Um bit clássico é 0 ou 1. O estado de um qubit é descrito por duas amplitudes complexas; medi-lo produz 0 ou 1 com probabilidades dadas por essas amplitudes. Vários qubits podem estar *emaranhados*, de modo que o seu estado conjunto não é uma lista de bits independentes. Os algoritmos quânticos organizam a interferência para que as respostas erradas se cancelem e as certas se reforcem. É uma capacidade estreita: os computadores quânticos não são máquinas de uso geral mais rápidas e, para a maioria das cargas de trabalho — bancos de dados, servidores web, planilhas —, não oferecem nada. A sua relevância para a segurança vem de poucos algoritmos, acima de todos a busca de períodos de Shor.

Os dispositivos atuais são ruidosos. Executar o Shor contra o RSA-2048 exige *qubits lógicos com correção de erros*, cada um construído a partir de muitos qubits físicos. As estimativas públicas caíram com o tempo — Gidney (2025) estimou menos de um milhão de qubits ruidosos, funcionando por menos de uma semana sob hipóteses de hardware declaradas —, mas nenhuma máquina assim existe, e a data da sua chegada é incerta.

### 2.3 Exemplo resolvido

Mapeie o login do aplicativo bancário da HCU. O enclave seguro do celular guarda uma chave do dispositivo (hardware); o sistema operacional do celular oferece um repositório de chaves (sistema operacional); a biblioteca TLS do aplicativo negocia a troca de chaves com o servidor (biblioteca); o balanceador de carga do servidor encerra o TLS usando um certificado da AC da HCU (infraestrutura); a aplicação bancária central confere um token de sessão assinado (aplicação). Cinco camadas, pelo menos quatro algoritmos relevantes para a ameaça quântica, três donos diferentes.

Cada uma das cinco camadas guarda uma chave ou uma verificação, e cada uma pode precisar de uma mudança diferente numa migração. A chave do dispositivo e a troca de chaves TLS são ambas vulneráveis à computação quântica se usarem curvas elípticas. A assinatura do token de sessão pode ser conferida apenas no servidor, o que é mais fácil de mudar. Mapear o login dessa forma mostra à equipe da HCU que o aplicativo não é uma decisão criptográfica, mas várias, com donos diferentes.

### 2.4 Atividade prática

Escolha um dispositivo que você possui. Liste as suas camadas e, para cada uma, uma função criptográfica que você acredita que ela execute. Marque cada crença como *observada* (você viu a configuração ou a documentação) ou *suposta*. Guarde a lista; o Capítulo 22 transforma listas assim num inventário.

A maioria dos estudantes encontra mais entradas supostas do que observadas, sobretudo no firmware e no hardware. Essa lacuna é o objetivo do exercício: o conhecimento de uma organização sobre a própria criptografia costuma ser incompleto, e a primeira tarefa de uma migração é descobrir o que realmente existe. Anote onde você procuraria para confirmar cada suposição, como uma tela de configurações ou a documentação de um fornecedor.

### 2.5 Erros comuns e limites

- Supor que "computador quântico" significa um laptop mais rápido.
- Esquecer o firmware e o hardware ao listar a criptografia.
- Citar um número de qubits sem a taxa de erro e o tempo de execução que ele pressupõe.

Um computador quântico é um tipo diferente de máquina, mais rápida apenas para certos problemas; para a maioria das tarefas, não oferece vantagem. O firmware e o hardware costumam ser esquecidos porque ninguém os configura no dia a dia, mas eles verificam assinaturas e guardam chaves. Um número de qubits sozinho diz pouco, já que os algoritmos úteis precisam de qubits com correção de erros e de longos tempos de execução, e as estimativas publicadas tornam essas hipóteses explícitas.

### Exercícios

- **EX003 — Mapa de camadas.** Mapeie um saque no caixa eletrônico da HCU em pelo menos quatro camadas e nomeie uma função criptográfica em cada uma. Rubrica: 3 = quatro camadas corretas, com funções e donos plausíveis.
- **EX004 — Verificação de mito.** Explique em três frases por que um computador quântico não aceleraria o processamento mensal em lote dos extratos da HCU. Rubrica: 3 = menciona a vantagem algorítmica estreita e o tipo de carga de trabalho.

### Síntese

A criptografia está espalhada por todas as camadas de um sistema, e a camada determina quão difícil é mudá-la. Os computadores quânticos são máquinas especializadas cujo impacto na segurança vem de poucos algoritmos, e a sua chegada depende da correção de erros em escala.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 40

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever pequenos programas em Python com funções, laços e condicionais; (2) tratar corretamente texto e bytes; (3) usar os módulos `hashlib` e `secrets` da biblioteca padrão; e (4) testar uma função com asserções.

### 3.1 Programas como enunciados precisos

Um programa é um argumento que uma máquina consegue conferir executando-o. O trabalho de segurança usa programas para reproduzir afirmações: se um relatório diz que "esta configuração oferece apenas troca de chaves clássica", um script curto que interpreta a configuração e imprime os grupos torna a afirmação repetível. Ao longo deste livro, os laboratórios são programas curtos em Python que usam apenas a biblioteca padrão, para que todo leitor possa executá-los offline e comparar a saída.

Comece pelas construções básicas: as variáveis guardam valores; as funções dão nome a um cálculo reutilizável; os laços `for` repetem; os comandos `if` escolhem. Programas legíveis usam nomes descritivos, funções pequenas e comentários que explicam *por quê*, e não *o quê*.

### 3.2 Texto versus bytes

As funções criptográficas operam sobre bytes, não sobre texto. Em Python, `"abc"` é texto (uma sequência de caracteres Unicode) e `b"abc"` são bytes. Converter texto em bytes exige uma codificação, normalmente UTF-8: `"abc".encode("utf-8")`. Um bug clássico é calcular o hash de `str(b"abc")`, que é o texto de seis caracteres `b'abc'`, e não os três bytes. O resumo fica errado em silêncio, e dois sistemas que discordam quanto à codificação não conseguirão verificar as assinaturas um do outro. Os problemas de interoperabilidade nas implantações pós-quânticas costumam ser desse tipo: ordem de bytes errada, codificação errada, comprimento errado.

### 3.3 Aleatoriedade e hashing na biblioteca padrão

`secrets.token_bytes(32)` devolve 32 bytes do gerador criptograficamente seguro do sistema operacional; o módulo `random` *não* é adequado para chaves, porque a sua saída é previsível a partir da semente. `hashlib.sha256(data).hexdigest()` calcula um resumo SHA-256; `hashlib.sha3_256` e `hashlib.shake_128` calculam membros da família SHA-3 usados dentro do ML-KEM e do ML-DSA. Para comparar valores secretos, use `hmac.compare_digest`, que leva um tempo independente de onde as entradas diferem.

Os testes de resposta conhecida usam entradas e saídas publicadas, então uma implementação errada falha de imediato. A família SHA-3 é útil neste livro porque o ML-KEM e o ML-DSA a usam internamente. Nunca imprima bytes secretos durante a depuração; imprima o seu comprimento ou um resumo.

### 3.4 Exemplo resolvido

Um estagiário da HCU escreve uma função para calcular a impressão digital de certificados:

```python
import hashlib
def fingerprint(der: bytes) -> str:
    return hashlib.sha256(der).hexdigest()
assert fingerprint(b"") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
print("fingerprint test passed")
```

A asserção usa como resposta conhecida o resumo publicado da cadeia vazia. Se alguém depois mudar a função para calcular o hash de texto, o teste falha imediatamente.

O teste confere a função contra um fato externo, e não contra a sua própria saída, o que é o que lhe permite falhar. Um segundo teste, com os bytes de um certificado real e a sua impressão digital publicada, detectaria um erro diferente, como calcular o hash de uma codificação em texto do certificado em vez dos seus bytes brutos. O estagiário acrescenta os dois testes ao repositório da HCU, para que cada mudança posterior seja conferida automaticamente.

### 3.5 Atividade prática

Escreva `is_valid_length(alg, data)`, que devolve `True` apenas se `data` tiver o comprimento esperado para aquele algoritmo, usando um dicionário como `{"ML-KEM-768-ek": 1184}` (o tamanho da chave de encapsulamento na FIPS 203). Teste uma entrada correta e duas incorretas.

Uma verificação de comprimento não é uma verificação de segurança; ela só detecta erros grosseiros, como valores truncados ou concatenados. Ainda assim vale a pena tê-la, porque muitos bugs de integração nas migrações pós-quânticas vêm de buffers dimensionados para chaves clássicas. Tire os tamanhos esperados da própria norma, e não de um post de blog, e anote o documento e a tabela que você usou, para que um revisor possa conferir cada número.

### 3.6 Erros comuns e limites

- Usar `random` para chaves ou nonces.
- Misturar texto e bytes, ou imprimir segredos nos logs durante a depuração.
- Escrever testes que não podem falhar (comparar um valor com ele mesmo).

Cada erro produz um código que parece funcionar. Uma chave do módulo random parece aleatória, mas pode ser prevista por qualquer um que descubra a semente. O resumo dos bytes errados parece um resumo e só falha quando comparado com outro sistema. Um teste que compara um valor com ele mesmo sempre passa, então dá uma falsa confiança. Registrar segredos nos logs os deixa em arquivos que mais pessoas podem ler do que o próprio programa.

### Exercícios

- **EX005 — Bug de codificação.** Explique por que `hashlib.sha256(str(b"abc").encode())` difere de `hashlib.sha256(b"abc")` e nomeie a classe do bug. Rubrica: 3 = explicação correta e classe do bug.
- **EX006 — Teste de resposta conhecida.** Escreva uma função que devolva o resumo hexadecimal SHA3-256 da sua entrada e um teste usando o resumo da cadeia vazia `a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a`. Rubrica: 3 = executa, e o teste pode falhar se a função estiver errada.

### Síntese

Programas pequenos e testados tornam as afirmações de segurança reproduzíveis. Os bytes, as codificações e a aleatoriedade segura são onde o código criptográfico dos iniciantes mais costuma errar.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 40

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) estruturar um argumento como afirmação, evidência e raciocínio; (2) citar as fontes primárias com precisão, incluindo a sua situação; (3) escrever sobre a incerteza sem exagerá-la nem escondê-la; e (4) adaptar um resultado para um leitor técnico e para um não técnico.

### 4.1 Afirmação, evidência, raciocínio

Todo parágrafo de um relatório de segurança deve permitir que o leitor encontre três coisas: o que você afirma, que evidência sustenta a afirmação e por que a evidência a sustenta. "A VPN da HCU é vulnerável à computação quântica" é uma afirmação. "A configuração da VPN exportada em 3 de março negocia apenas o grupo ECDH 19" é uma evidência. "O ECDH é quebrado pelo algoritmo de Shor num computador quântico criptograficamente relevante, então o tráfego gravado da VPN poderia ser decifrado depois" é o raciocínio. Quando falta um dos três, os leitores ou desconfiam de um resultado correto, ou aceitam um sem sustentação.

### 4.2 Citar as normas e a sua situação

A escrita criptográfica depende de normas cuja situação muda. Cite o documento com precisão — "NIST FIPS 203, *Module-Lattice-Based Key-Encapsulation Mechanism Standard*, agosto de 2024" — com um link persistente, como o seu DOI. Declare a situação quando ela importar: as FIPS 203, 204 e 205 são normas finais; o [NIST IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) era um rascunho público inicial em 12 de outubro de 2026, então as suas datas de transição propostas são propostas, e não regras; o FN-DSA ainda estava em desenvolvimento. Prefira as fontes primárias às notícias e confira se a fonte realmente diz o que você lhe atribui. Muitos erros nos relatórios de migração vêm de citar o resumo secundário de um rascunho como se fosse uma exigência final.

### 4.3 Escrever sobre a incerteza

Ninguém sabe quando existirá um computador quântico criptograficamente relevante. A boa escrita transforma essa incerteza em hipóteses explícitas: "Se uma máquina assim existir dentro de 15 anos, os registros com uma exigência de confidencialidade de 30 anos já estão expostos à coleta do tipo 'colete agora, decifre depois'." Evite tanto a falsa precisão ("em 2031") quanto o descaso ("faltam décadas, ignore"). Use faixas, declare quem fez uma estimativa e quando, e mostre como a sua recomendação muda ao longo da faixa.

Enunciados em duas partes como esse permitem que o leitor substitua a sua hipótese pela dele e ainda use o seu raciocínio. Diga quem fez cada estimativa que você cita e quando.

### 4.4 Exemplo resolvido

Uma frase de rascunho diz: "Os computadores quânticos vão quebrar a nossa criptografia até 2030, então o NIST nos obriga a mudar para o Kyber imediatamente." Reescrita: "As estimativas públicas de quando um computador quântico poderia quebrar o RSA-2048 variam muito, e nenhuma tem autoridade. O NIST publicou o ML-KEM, derivado do CRYSTALS-Kyber, como FIPS 203 em 2024, e o seu rascunho IR 8547 propõe tornar obsoletos os algoritmos vulneráveis à computação quântica depois de 2030 e proibi-los depois de 2035. Como o nosso arquivo de financiamentos imobiliários precisa permanecer confidencial por 30 anos, recomendamos iniciar neste ano a migração da troca de chaves das transferências do arquivo." Cada afirmação agora tem fonte, data e ressalvas.

### 4.5 Atividade prática

Pegue uma notícia de uma página sobre computação quântica. Marque cada afirmação factual, encontre a sua fonte primária, se houver, e reescreva a conclusão principal da notícia em três frases que respeitem as evidências.

A maioria das notícias mistura fatos corretos com afirmações sem fonte ou que exageram uma fonte. Escrever as suas três frases obriga você a decidir o que as evidências realmente sustentam. Compare a sua versão com a de um colega: se forem diferentes, verifique se um de vocês se apoiou numa afirmação que o outro não conseguiu encontrar na fonte. Guarde as fontes primárias que você encontrou, pois vai reutilizá-las em capítulos posteriores.

### 4.6 Erros comuns e limites

- Citar o blog de um fornecedor para o conteúdo de uma norma.
- Apresentar as datas propostas por um rascunho como obrigatórias.
- Escrever "à prova de computação quântica" ou "inquebrável"; prefira "projetado para resistir aos ataques quânticos conhecidos".

O blog de um fornecedor pode descrever uma norma com precisão, mas também pode misturar afirmações de produto ou um rascunho anterior. Cite a própria norma. Os documentos em rascunho propõem datas para comentários; eles não são exigências até serem publicados na forma final. Palavras absolutas como inquebrável prometem mais do que qualquer criptógrafo pode cumprir, e os leitores que depois souberem de um ataque desconfiarão de todo o resto do relatório.

### Exercícios

- **EX007 — Afirmação, evidência, raciocínio.** Escreva um resultado em três frases de que a AC interna da HCU usa RSA-2048 e por que isso importa. Rotule cada frase como A, E ou R. Rubrica: 3 = as três presentes e precisas.
- **EX008 — Disciplina quanto à situação.** Corrija esta frase: "A FIPS 206 exige o Falcon para todas as assinaturas a partir de 2025." Rubrica: 3 = observa que a FIPS 206 estava em desenvolvimento, nomeia o FN-DSA, remove a exigência falsa.

### Síntese

Uma escrita de segurança clara separa afirmação, evidência e raciocínio, cita as fontes primárias com a sua situação e transforma a incerteza em hipóteses declaradas.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 40

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) definir confidencialidade, integridade, disponibilidade e autenticidade; (2) relacionar ativos, ameaças, vulnerabilidades e controles; (3) explicar "colete agora, decifre depois" e "falsifique depois" como padrões de ameaça; e (4) ler criticamente uma declaração de risco simples.

### 5.1 Propriedades centrais

*Confidencialidade* significa que apenas as partes autorizadas podem ler a informação; *integridade* significa que as mudanças não autorizadas são detectadas ou impedidas; *disponibilidade* significa que os usuários autorizados podem usar o serviço quando precisam; *autenticidade* significa que conseguimos saber quem produziu uma mensagem. A criptografia serve principalmente à confidencialidade (cifração, troca de chaves), à integridade e à autenticidade (códigos de autenticação de mensagem e assinaturas). A disponibilidade é fácil de esquecer nas mudanças criptográficas: uma migração que faz os handshakes falharem é um incidente de disponibilidade, mesmo que melhore a confidencialidade.

No caso da HCU, um gateway que rejeitasse os celulares mais antigos dos associados após uma mudança de algoritmo seria uma falha de segurança, mesmo que nenhum dado vazasse.

### 5.2 Ativos, ameaças, vulnerabilidades, controles

Um *ativo* é algo de valor — os dados dos associados, a capacidade de aprovar pagamentos. Uma *ameaça* é uma causa potencial de dano, geralmente um agente com uma capacidade e um motivo. Uma *vulnerabilidade* é uma fraqueza que a ameaça pode explorar. Um *controle* reduz a probabilidade ou o impacto. O risco é a combinação de probabilidade e impacto de um cenário que liga esses elementos. Na segurança quântica, a vulnerabilidade muitas vezes não é um bug, mas uma propriedade matemática de um algoritmo que se torna explorável quando passa a existir uma nova capacidade.

### 5.3 Dois padrões de ameaça quântica

*Colete agora, decifre depois* (HNDL, na sigla em inglês): um adversário grava hoje o tráfego cifrado e o guarda até que um computador quântico consiga recuperar a troca de chaves. O dano acontece no futuro, mas a coleta — e, portanto, a necessidade de agir — é agora, para quaisquer dados cuja confidencialidade precise durar mais do que a chegada de uma máquina assim. *Falsifique depois*: quando existir um computador quântico, um adversário poderá derivar chaves privadas de assinatura a partir das chaves públicas e falsificar assinaturas, atualizações de firmware ou certificados. Ao contrário do HNDL, a falsificação precisa da máquina no momento do ataque, então a migração das assinaturas pode seguir outro cronograma — exceto onde as assinaturas precisam continuar confiáveis por muitos anos, como nos documentos de financiamento imobiliário ou em dispositivos que não podem ser atualizados.

### 5.4 Exemplo resolvido

Declaração de risco da HCU, rascunho: "Risco de ataque quântico: alto." Melhorada: "Ativo: transferências do arquivo de financiamentos imobiliários entre as agências e o data center (confidencialidade exigida por 30 anos). Ameaça: um adversário com muitos recursos gravando o tráfego da WAN. Vulnerabilidade: a troca de chaves da VPN usa apenas ECDH. Impacto, se concretizado: divulgação do histórico financeiro dos associados. Probabilidade: a coleta é plausível agora; a decifração depende de uma capacidade futura incerta. Opções de controle: troca de chaves híbrida pós-quântica, redução dos dados em trânsito." A declaração melhorada sustenta uma decisão; o rascunho não.

A versão melhorada nomeia separadamente cada elemento do risco, para que os leitores possam discordar de uma parte sem rejeitar o todo. Ela também mostra por que o risco é urgente apesar da data incerta: a coleta pode acontecer hoje. Um revisor pode conferir cada parte contra as evidências, como a configuração da VPN ou a política de retenção do arquivo.

### 5.5 Atividade prática

Escreva declarações de risco no formato melhorado para dois ativos da HCU: as mensagens de autorização de cartão e a chave de assinatura de código do aplicativo móvel. Observe como os seus horizontes de tempo diferem.

As mensagens de autorização de cartão precisam de confidencialidade apenas por pouco tempo, então o "colete agora, decifre depois" importa pouco ali; a preocupação é a autenticação. A chave de assinatura de código importa enquanto as versões antigas do aplicativo forem confiáveis, o que faz do "falsifique depois" a principal preocupação. Escrever as duas declarações no mesmo formato torna essas diferenças visíveis, e a comparação ajuda a decidir qual ativo migrar primeiro.

### 5.6 Erros comuns e limites

- Tratar todo uso criptográfico como igualmente urgente.
- Ignorar a disponibilidade ao trocar algoritmos.
- Confundir uma ameaça (agente) com uma vulnerabilidade (fraqueza).

A urgência depende de quanto tempo os dados precisam continuar confidenciais e de quanto tempo as assinaturas precisam ser confiáveis. Tratar todo uso como igualmente urgente dilui o esforço e atrasa os casos que mais importam. Ignorar a disponibilidade pode transformar uma melhoria de segurança numa interrupção que os associados percebem. Confundir ameaças com vulnerabilidades leva a controles mirados na coisa errada, como tentar deter um adversário em vez de remover a fraqueza que ele exploraria.

### Exercícios

- **EX009 — Classificação de padrões.** Classifique cada item como HNDL, falsificação posterior ou nenhum: tráfego de VPN arquivado, assinatura de firmware dos caixas eletrônicos, cifração AES-256 do banco de dados, sessão TLS com o aplicativo móvel. Rubrica: 3 = os quatro corretos, com motivos de uma linha.
- **EX010 — Declaração de risco.** Reescreva "A PKI está sob risco quântico" como uma declaração de risco completa para a AC interna da HCU. Rubrica: 3 = ativo, ameaça, vulnerabilidade, impacto, probabilidade e controles presentes.

### Síntese

As propriedades de segurança, os elementos do risco e dois padrões de ameaça definidos pelo tempo — colete agora, decifre depois e falsifique depois — dão um vocabulário preciso o bastante para ordenar os riscos quânticos.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 40

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) calcular com aritmética modular; (2) explicar os grupos e por que os períodos ocultos importam; (3) multiplicar polinômios no anel Z_q[x]/(x^n+1); e (4) ligar essas estruturas ao RSA, às curvas elípticas e ao ML-KEM.

### 6.1 Aritmética modular e grupos

Trabalhar módulo *q* mantém os números em {0, …, *q*−1}: 15 mod 7 = 1. Um *grupo* é um conjunto com uma operação associativa, que tem elemento neutro e inversos. Os números não nulos módulo um primo *p* formam um grupo sob a multiplicação; os pontos de uma curva elíptica formam um grupo sob a adição de pontos. Repetir a operação a partir de um elemento inicial *g* acaba gerando um ciclo: *g*, *g*², *g*³, … volta a 1 depois de *r* passos, em que *r* é a *ordem* de *g*. Encontrar *r* — um período oculto — é difícil classicamente para grupos grandes, e o RSA, o Diffie–Hellman e a criptografia de curvas elípticas se apoiam todos em problemas equivalentes ou redutíveis a encontrar esses períodos ou logaritmos discretos. O algoritmo de Shor encontra períodos de forma eficiente num computador quântico, e é por isso que todos eles caem juntos.

### 6.2 Anéis de polinômios

Um anel de polinômios Z_q[*x*]/(*x*^*n*+1) contém os polinômios de grau menor que *n* com coeficientes módulo *q*. Para multiplicar, multiplique normalmente e depois substitua *x*^*n* por −1. O ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)) usa *n* = 256 e *q* = 3329; o ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) usa *n* = 256 e *q* = 8380417. Vetores desses polinômios formam *módulos*, daí "reticulado de módulos". O anel é escolhido pela compacidade e pela multiplicação rápida; a segurança vem do acréscimo de um pequeno ruído aleatório, tema do Capítulo 23. Não se conhece nenhum ataque quântico eficiente por busca de períodos contra esses problemas com ruído.

### 6.3 Atividade prática — Laboratório R

```python
# Lab R (ch 6): multiplication in R_q = Z_q[x]/(x^n + 1), the ring behind ML-KEM (there n=256, q=3329).
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

Confira à mão: (1 + 2*x* + 3*x*³)·*x* = *x* + 2*x*² + 3*x*⁴ = −3 + *x* + 2*x*² ≡ 14 + *x* + 2*x*² (mod 17).

O laboratório multiplica dois polinômios pequenos num anel com parâmetros de brinquedo e imprime o resultado. Fazer um produto à mão, como mostrado, é a melhor forma de ver onde acontece a troca de sinal. Os parâmetros reais são muito maiores, mas a regra é a mesma, e as bibliotecas que você vai usar a aplicam com algoritmos muito mais rápidos. O anel de brinquedo não é seguro; ele existe apenas para tornar a aritmética visível.

### 6.4 Exemplo resolvido

Um desenvolvedor da HCU pergunta por que a sua biblioteca pós-quântica "multiplica polinômios" quando o RSA "eleva números a potências". O RSA trabalha no grupo multiplicativo módulo *N*, onde existe um período oculto e o Shor consegue encontrá-lo. O ML-KEM trabalha com álgebra linear com ruído sobre anéis de polinômios, onde não se conhece nenhuma estrutura de períodos assim que ajude. A aritmética parece diferente porque o problema difícil é diferente.

Vale a pena responder à pergunta do desenvolvedor antes de qualquer trabalho de migração, porque ela explica por que os novos algoritmos exigem novas habilidades de revisão. O código que lida com polinômios e ruído tem modos de falha diferentes do código que lida com inteiros grandes, como erros na redução ou na amostragem do ruído.

### 6.5 Erros comuns e limites

- Esquecer a troca de sinal ao reduzir *x*^*n* a −1.
- Acreditar que a estrutura do anel sozinha dá segurança; sem ruído, as equações são fáceis de resolver.
- Supor que "nenhum ataque conhecido" significa "demonstradamente seguro".

A troca de sinal é o erro mais comum no cálculo à mão, e os testes com respostas conhecidas o detectam. O segundo erro importa mais: o anel torna a aritmética conveniente, mas a segurança vem do ruído acrescentado. Sem ele, as equações são álgebra linear comum e fáceis de resolver. "Nenhum ataque conhecido" é uma afirmação sobre o conhecimento atual, então as normas incluem margens de segurança e são revistas à medida que a pesquisa continua.

### Exercícios

- **EX011 — Ordem de um elemento.** Encontre a ordem de 3 módulo 7 listando as potências. Rubrica: 3 = ordem correta, com a lista.
- **EX012 — Produto no anel.** Calcule (2 + *x*)(3 + *x*³) em Z_17[*x*]/(*x*⁴+1) e confira com o Laboratório R. Rubrica: 3 = coeficientes corretos, com a redução mostrada.

### Síntese

A criptografia de chave pública clássica esconde períodos em grupos, que o algoritmo de Shor encontra. A PQC baseada em reticulados calcula em anéis de polinômios e esconde os segredos sob ruído, uma estrutura sem atalho quântico conhecido.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 40

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) descrever as camadas do TCP/IP e onde operam o TLS, o IPsec e o SSH; (2) acompanhar um handshake TLS 1.3 e identificar a troca de chaves e a autenticação; (3) explicar por que as chaves e assinaturas pós-quânticas pressionam o tamanho das mensagens; e (4) nomear os documentos da IETF que definem a troca de chaves híbrida.

### 7.1 Camadas e canais seguros

Os dados atravessam as redes em camadas: enlace, internet (IP), transporte (TCP, UDP, QUIC) e aplicação. Os canais seguros inserem a criptografia em pontos diferentes. O TLS protege fluxos de aplicação como o HTTPS; o IPsec com IKEv2 protege pacotes IP entre locais, como nas VPNs das agências da HCU; o SSH protege as sessões dos administradores. Cada um tem duas tarefas criptográficas: o *estabelecimento de chaves*, que acorda um segredo de sessão novo, e a *autenticação*, que prova quem é o par, geralmente com certificados e assinaturas.

As duas tarefas enfrentam ameaças quânticas diferentes. O estabelecimento de chaves importa para o "colete agora, decifre depois", porque o tráfego gravado pode ser aberto quando o segredo de sessão for recuperado. A autenticação importa apenas no momento da conexão, já que uma assinatura falsificada depois não consegue mudar um handshake passado.

### 7.2 O handshake TLS 1.3

No TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html)), o cliente envia um ClientHello listando os grupos suportados e um compartilhamento de chave; o servidor responde com um ServerHello contendo o seu compartilhamento de chave e, depois, mensagens cifradas que levam a sua cadeia de certificados e uma assinatura CertificateVerify. O estabelecimento de chaves e a autenticação são separados: um grupo híbrido como o X25519MLKEM768, especificado para o TLS no [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html), substitui apenas a parte da troca de chaves. O seu compartilhamento de chave do cliente tem 1.216 bytes e o do servidor, 1.120 bytes, contra 32 bytes do X25519 sozinho. A cadeia de certificados permanece inalterada até que sejam implantados certificados pós-quânticos.

### 7.3 Tamanho e middleboxes

Mensagens maiores importam. Um ClientHello acima de cerca de 1.500 bytes pode ocupar dois segmentos TCP; alguns firewalls e dispositivos de inspeção antigos tratam mal essas mensagens ou identificadores de grupo desconhecidos. As assinaturas pós-quânticas são ainda maiores: uma assinatura ML-DSA-44 tem 2.420 bytes ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)), contra cerca de 72 do ECDSA P-256. O Capítulo 30 mede o que isso causa às cadeias de certificados.

Antes de culpar o novo algoritmo por uma falha, verifique para onde foram os bytes. Uma captura de pacotes em laboratório mostra se uma mensagem foi dividida, descartada ou rejeitada, e por qual dispositivo.

### 7.4 Exemplo resolvido

A equipe de rede da HCU vê um aumento de conexões que falham depois de ativar um grupo híbrido num gateway web de teste. Uma captura de pacotes no laboratório mostra que o ClientHello agora ocupa dois segmentos, e um proxy de inspeção legado numa agência derruba a conexão. A correção não é desativar a troca de chaves pós-quântica em todo lugar, mas atualizar ou contornar esse proxy, registrando o problema no log da migração. O diagnóstico exigiu conhecer as duas camadas: o tamanho veio da criptografia, a falha veio do tratamento no transporte.

### 7.5 Atividade prática

Usando um navegador de laboratório e o seu próprio servidor de teste, ou traces de handshake publicados, identifique a lista de grupos suportados num ClientHello e o grupo selecionado no ServerHello. Registre quais mensagens são cifradas no TLS 1.3. Não capture o tráfego de outras pessoas.

A maior parte do handshake depois do ServerHello é cifrada no TLS 1.3, inclusive o certificado, então um observador passivo vê menos do que nas versões mais antigas. Compare uma conexão que oferece um grupo híbrido com uma que oferece apenas grupos clássicos e anote a diferença no tamanho do ClientHello. Os traces publicados são uma alternativa segura se você não tiver um servidor de teste próprio. Anote a ferramenta que usou e a sua versão, para que outro estudante possa repetir a observação.

### 7.6 Erros comuns e limites

- Acreditar que a troca de chaves híbrida também torna a autenticação pós-quântica.
- Culpar o algoritmo por falhas causadas por middleboxes.
- Capturar tráfego em redes que você não está autorizado a monitorar.

A troca de chaves híbrida protege os segredos de sessão contra a decifração posterior, mas o certificado e a sua assinatura continuam clássicos até que os certificados mudem, o que é uma migração separada e mais lenta. As falhas por middleboxes são comuns nas primeiras implantações, e diagnosticá-las exige evidências da rede, e não suposições sobre o algoritmo. Capturar tráfego sem autorização é ilegal em muitos lugares e quebra a confiança de que o trabalho de segurança depende, por melhor que seja a intenção.

### Exercícios

- **EX013 — Separe as tarefas.** Para o TLS 1.3, o IKEv2 e o SSH, nomeie o mecanismo de estabelecimento de chaves e o de autenticação numa implantação clássica típica. Rubrica: 3 = seis entradas corretas.
- **EX014 — Orçamento de tamanho.** Quantos bytes a mais um cliente envia no seu compartilhamento de chave com o X25519MLKEM768 do que com o X25519 sozinho? Rubrica: 3 = 1.184 bytes, com os tamanhos citados.

### Síntese

Os protocolos seguros separam o estabelecimento de chaves da autenticação. A troca de chaves híbrida pós-quântica muda o primeiro, aumenta os handshakes e pode expor middleboxes antigos; a autenticação muda depois, com os certificados pós-quânticos.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 40

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar programas maiores com módulos, data classes e tratamento de erros; (2) interpretar entradas estruturadas, como CSV e JSON; (3) escrever testes tanto para entradas válidas quanto para inválidas; e (4) evitar erros de segurança comuns em código que lida com chaves.

### 8.1 Estrutura e dados

À medida que os programas crescem, a estrutura os mantém corretos. Agrupe as funções relacionadas em módulos, represente os registros com `dataclasses` para que os campos tenham nome e lance exceções para estados inválidos, em vez de devolver em silêncio valores errados. Os módulos `csv` e `json` da biblioteca padrão interpretam formatos comuns; validar cada campo ao lê-lo — tipo, faixa, valores permitidos — impede que dados ruins se propaguem. No trabalho de migração, os inventários chegam como exportações CSV de scanners e de bancos de dados de configuração, e a maioria dos erros de análise começa numa coluna não validada.

### 8.2 Testes negativos

Um teste positivo confere que uma entrada válida funciona; um *teste negativo* confere que uma entrada inválida é rejeitada. O código criptográfico precisa dos dois. Um decodificador de chaves de encapsulamento ML-KEM precisa aceitar exatamente 800, 1.184 ou 1.568 bytes para os três conjuntos de parâmetros da FIPS 203 e rejeitar qualquer outra coisa, e a FIPS 203 também especifica verificações de entrada sobre os coeficientes da chave. Bibliotecas que pularam essas verificações já aceitaram, historicamente, entradas malformadas que vazaram informações ou derrubaram serviços. Escreva os testes negativos antes de escrever o decodificador.

Os testes da HCU incluem chaves com um byte a menos e com um byte a mais.

### 8.3 Lidar com segredos no código

Mantenha os segredos fora dos logs, das mensagens de exceção e do controle de versão. Prefira passar *handles* de chaves (referências mantidas por um HSM ou pelo repositório de chaves do sistema operacional) em vez dos bytes brutos da chave. Compare segredos com funções de tempo constante. Nunca escreva a sua própria implementação de produção de um algoritmo pós-quântico; use uma biblioteca verificada e trate com desconfiança até um pequeno código de encapsulamento, porque os canais laterais e os bugs de interpretação vivem na cola tanto quanto no núcleo.

Para a HCU, isso significa chamar a biblioteca aprovada por uma pequena interface e revisar essa interface com o mesmo cuidado que todo o resto.

### 8.4 Exemplo resolvido

Um analista da HCU recebe `inventory.csv` com as colunas `host, protocol, group`. Um script descuidado conta as linhas em que `group == "x25519"` e relata "a maioria dos hosts é clássica". Uma versão cuidadosa normaliza as maiúsculas e minúsculas, rejeita as linhas com grupo vazio como *desconhecidas* em vez de *clássicas* e imprime três números: clássicos, híbridos e desconhecidos. O script cuidadoso revela que 18% das linhas sintéticas são desconhecidas — um fato que o primeiro script escondia.

Tratar o desconhecido como clássico teria feito o inventário parecer mais completo e mais uniformemente clássico do que era, escondendo os hosts cuja criptografia ninguém conhecia. Os desconhecidos se tornam uma lista de trabalho própria: alguém precisa verificar esses hosts diretamente antes que o inventário possa ser confiável. O script cuidadoso também registra a data do arquivo de entrada, para que os leitores posteriores saibam quão recentes são as contagens.

### 8.5 Atividade prática

Escreva uma função que leia linhas `host,group`, valide que `group` pertence a um conjunto permitido e devolva as contagens de híbridos, clássicos e desconhecidos. Inclua um teste negativo com uma cadeia de grupo desconhecida.

Normalize as maiúsculas e minúsculas e os espaços antes de comparar e decida de antemão o que conta como híbrido. Um nome de grupo que você nunca viu deve cair em desconhecido, nunca em clássico por padrão. O seu teste negativo deve mostrar que um nome de grupo escrito errado ou inventado é contado como desconhecido e que a função não quebra diante de uma linha vazia. Imprima as três contagens numa ordem fixa, para que as saídas de execuções diferentes possam ser comparadas.

### 8.6 Erros comuns e limites

- Tratar dados ausentes como um resultado negativo.
- Capturar todas as exceções e continuar em silêncio.
- Escrever criptografia própria em vez de chamar uma implementação verificada.

Os dados ausentes são um resultado sobre o inventário, e não sobre os sistemas. Engolir exceções esconde as linhas que falharam, então os totais parecem completos quando não estão; registre cada falha com o número da linha. A criptografia própria falha de maneiras que os testes raramente detectam, como diferenças de tempo, e as bibliotecas verificadas tiveram anos de revisão que uma implementação nova não consegue igualar.

### Exercícios

- **EX015 — Testes negativos.** Liste quatro testes negativos para uma função que carrega uma chave pública ML-DSA-65 (1.952 bytes na FIPS 204). Rubrica: 3 = quatro casos de falha distintos e significativos.
- **EX016 — Desconhecido não é não.** Explique em duas frases por que contar campos vazios como "clássicos" enviesa um inventário. Rubrica: 3 = identifica a direção do viés e a consequência para a decisão.

### Síntese

Código estruturado, entradas validadas e testes negativos tornam a análise confiável; no código criptográfico, rejeitar uma entrada ruim é tão importante quanto tratar uma entrada boa.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 40

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) modelar dados com entidades, atributos e relacionamentos; (2) escrever consultas SQL simples; (3) associar aos dados tempos de retenção e de confidencialidade; e (4) explicar como o tempo de vida dos dados determina a urgência quântica.

### 9.1 Modelar dados

Um banco de dados relacional guarda tabelas de linhas. Uma *entidade* (associado, conta, documento) se torna uma tabela; os *atributos* se tornam colunas; os *relacionamentos* se tornam chaves que ligam as tabelas. As consultas SQL selecionam, filtram e juntam: `SELECT host FROM services WHERE kex_group = 'ECDHE-P256'` devolve os hosts que usam um determinado grupo. Modelos bem feitos tornam a análise possível: se uma equipe de migração guarda cada observação criptográfica com a sua fonte e a sua data, ela pode depois perguntar quais observações estão desatualizadas.

A tabela de inventário da HCU registra, para cada linha, o host, o protocolo, o grupo, a fonte e a data da observação. A coluna de fonte distingue uma exportação de configuração de uma captura passiva, que têm confiabilidades diferentes.

### 9.2 Tempos de vida dos dados

Toda classe de dados tem um *período de retenção* (quanto tempo é guardada) e um *tempo de confidencialidade* (por quanto tempo a sua divulgação causaria dano). Eles diferem: as mensagens de autorização de cartão são guardadas por sete anos para disputas, mas são quase inofensivas depois que o cartão expira; os documentos de financiamento imobiliário são guardados e continuam sensíveis por 30 anos. Michele Mosca (2018) formulou a consequência quântica: se *x* é o tempo durante o qual os dados precisam continuar seguros, *y* o tempo para migrar e *z* o tempo até um computador quântico capaz, então *x* + *y* > *z* significa que os dados já estão em risco. Os bancos de dados são onde *x* é registrado, então um modelo de dados com atributos de tempo de vida é a primeira ferramenta quantitativa do planejamento da migração.

### 9.3 Cifração em repouso

Os bancos de dados cifram os dados em repouso com algoritmos simétricos como o AES-256, cujas chaves são envelopadas por chaves de cifração de chaves. A camada simétrica não é o problema quântico. O problema é como as chaves viajam: se as chaves do banco de dados são copiadas para outro local por um canal que usa transporte de chaves RSA ou ECDH, os backups gravados podem expô-las depois. O inventário, portanto, segue as chaves, e não apenas os dados.

Os jobs de backup da HCU, por exemplo, copiam chaves envelopadas entre os data centers pela mesma VPN que transporta o arquivo de financiamentos imobiliários.

### 9.4 Exemplo resolvido

A HCU modela `data_class(name, retention_years, confidentiality_years, transfer_channel)`. Uma consulta encontra as classes com `confidentiality_years >= 15 AND transfer_channel = 'vpn-ecdh'`: os documentos de financiamento imobiliário e os registros de identidade dos associados. Essas duas classes se tornam as primeiras candidatas à troca de chaves híbrida, antes do tráfego de cartões, de alto volume mas de vida curta.

O tráfego de cartões é alto em volume, mas perde o seu valor em poucos dias, então o "colete agora, decifre depois" importa pouco para ele. Os registros de financiamento imobiliário e de identidade mantêm o seu valor por décadas. Ordenar a migração pelo tempo de confidencialidade, e não pelo volume de tráfego ou pela facilidade, põe o esforço onde a exposição futura é maior. O resultado da consulta é uma lista inicial para a discussão com os donos dos dados, que podem conhecer outras classes de vida longa que a tabela ainda não contém.

### 9.5 Atividade prática

Crie uma tabela de cinco linhas com classes de dados sintéticas da HCU, com retenção, tempo de confidencialidade e canal. Escreva a consulta acima e justifique a ordem de migração que ela sugere.

Inclua pelo menos uma classe cuja retenção seja longa, mas cujo tempo de confidencialidade seja curto, como os relatórios anuais publicados, para que a diferença fique visível. A sua justificativa deve explicar por que cada classe cai onde cai e qual hipótese mudaria a sua posição. Compare a sua ordenação com a de um colega e anote qualquer classe que vocês posicionaram de forma diferente, com o motivo. Guarde a tabela; capítulos posteriores a ampliam.

### 9.6 Erros comuns e limites

- Confundir retenção com tempo de confidencialidade.
- Supor que a cifração em repouso resolve a exposição em trânsito.
- Registrar os tempos de vida uma vez e nunca mais revisá-los após mudanças de contratos ou de leis.

A retenção é quanto tempo um registro é guardado; o tempo de confidencialidade é por quanto tempo a sua divulgação causaria dano. Eles muitas vezes diferem. A cifração em repouso protege as cópias armazenadas, mas não diz nada sobre as cópias enviadas por uma rede. Os tempos de vida mudam quando mudam as leis, os contratos ou as práticas de negócio, então cada um precisa de um responsável e de uma data de revisão; caso contrário, as prioridades da migração se afastam lentamente da realidade.

### Exercícios

- **EX017 — SQL.** Escreva uma consulta que devolva as classes de dados cujo tempo de confidencialidade exceda 10 anos e cujo canal use uma troca de chaves vulnerável à computação quântica. Rubrica: 3 = sintaxe e condições corretas.
- **EX018 — Tempos de vida.** Dê tempos de retenção e de confidencialidade plausíveis para as autorizações de cartão e os arquivos de financiamento imobiliário e explique a diferença. Rubrica: 3 = valores razoáveis e diferença justificada.

### Síntese

Modelos de dados com atributos de tempo de vida transformam a pergunta quântica numa consulta. É preciso seguir as chaves, e não apenas os dados, para encontrar a exposição.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 40

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) explicar por que a autorização define o trabalho de segurança legítimo; (2) escrever uma declaração de escopo para uma avaliação criptográfica; (3) lidar com responsabilidade com o conhecimento de uso dual; e (4) encaminhar as fraquezas descobertas pela divulgação coordenada.

### 10.1 A autorização é a fronteira

A mesma ação — varrer um servidor em busca dos grupos TLS que ele suporta, capturar um handshake, testar se um dispositivo aceita um algoritmo rebaixado — é trabalho profissional quando o dono do sistema a autoriza por escrito, e um crime ou uma quebra de confiança quando não autoriza. A autorização precisa nomear os sistemas, a janela de tempo, as técnicas permitidas, os dados que você pode coletar e a pessoa a contatar se algo quebrar. A aprovação verbal de um engenheiro amigo não é autorização; tampouco o fato de um serviço ser alcançável pela internet.

### 10.2 Escopo do trabalho criptográfico

As avaliações criptográficas podem parecer inofensivas, mas tocam coisas sensíveis: os certificados revelam nomes de hosts internos, as capturas de handshake podem conter metadados e os testes de rebaixamento podem quebrar sessões de produção. Um bom escopo diz, por exemplo: "Observação passiva dos handshakes TLS na porta espelho do gateway de teste da HCU, de 1º a 14 de maio; nenhuma retenção de payload; nenhum teste ativo de rebaixamento fora do laboratório isolado; resultados compartilhados apenas com o escritório de segurança da HCU." Os experimentos ativos que modificam a negociação ou injetam falhas pertencem a bancadas de teste isoladas.

Um escopo escrito também protege o estudante: se algo quebrar, o registro mostra o que era permitido.

### 10.3 Uso dual e divulgação

Saber encontrar sistemas vulneráveis à computação quântica também diz a um adversário onde procurar. Publique resultados agregados, e não listas de hosts vulneráveis nomeados. Se você encontrar uma fraqueza no produto de um fornecedor — por exemplo, uma biblioteca que aceita chaves ML-KEM malformadas —, relate-a em particular ao fornecedor, combine um prazo e publique apenas depois de uma correção ou do prazo combinado. Rotule claramente todos os dados sintéticos, para que os exemplos de ensino nunca sejam confundidos com resultados reais sobre organizações reais.

Os relatórios da HCU sobre a sua própria migração seguem a mesma regra e descrevem o progresso por contagens.

### 10.4 Exemplo resolvido

Um estagiário da HCU percebe que o site público de um banco parceiro ainda oferece apenas troca de chaves clássica e propõe "varrer todos os bancos parceiros" para um projeto de aula. A resposta ética: observar um único handshake público feito numa visita normal pelo navegador é algo comum, mas varrer sistematicamente os parceiros está fora da autoridade da HCU. Em vez disso, o estagiário estuda medições agregadas publicadas e pede à equipe de gestão de fornecedores da HCU que inclua perguntas sobre prontidão pós-quântica nos questionários aos parceiros.

A resposta mantém o objetivo útil, saber quão preparados estão os parceiros, enquanto o leva para um canal em que a HCU tem legitimidade para perguntar.

### 10.5 Atividade prática

Redija um pedido de autorização de uma página para um inventário TLS passivo de uma rede de teste sintética da HCU. Inclua os sistemas, as datas, as técnicas, o tratamento dos dados, as condições de parada e os contatos.

As condições de parada dizem quando interromper: por exemplo, se a rede de teste mostrar tráfego de produção inesperado ou se um serviço se degradar. Os contatos devem incluir alguém que possa autorizar uma parada a qualquer hora. O tratamento dos dados declara o que é capturado, onde é guardado e quando é apagado. Peça a um colega que leia o seu pedido como se fosse o dono do sistema e liste tudo o que ele se recusaria a assinar.

### 10.6 Erros comuns e limites

- Tratar a possibilidade de alcançar um sistema pela internet como permissão.
- Reter os payloads dos pacotes "por precaução".
- Publicar listas nomeadas de sistemas vulneráveis.

Conseguir alcançar um sistema não é o mesmo que ter permissão para testá-lo; a permissão vem do seu dono, por escrito. Os payloads podem conter dados pessoais de que a avaliação nunca precisou, e guardá-los cria risco sem benefício. As listas nomeadas ajudam os atacantes a escolher alvos, então compartilhe-as apenas com as pessoas que vão corrigir os sistemas. Cada erro prejudica a confiança que permite às equipes de segurança fazer o seu trabalho.

### Exercícios

- **EX019 — Lacunas de escopo.** Identifique três elementos ausentes em: "Você pode testar a nossa criptografia na semana que vem." Rubrica: 3 = três entre sistemas, técnicas, tratamento dos dados, janela, contatos, condições de parada.
- **EX020 — Divulgação.** Descreva as etapas depois de descobrir que o equipamento de VPN de um fornecedor recorre em silêncio à troca de chaves clássica quando o híbrido está configurado. Rubrica: 3 = relato privado, evidências, prazo, publicação coordenada.

### Síntese

A autorização, o tratamento dos dados dentro do escopo e a divulgação coordenada são o que torna profissional a avaliação criptográfica. Os experimentos ativos de rebaixamento ou de injeção de falhas pertencem apenas a bancadas de teste isoladas e autorizadas.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 40

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) descrever processos, isolamento de memória, permissões de arquivos e serviços do sistema; (2) explicar como os sistemas operacionais oferecem serviços criptográficos e armazenamento de chaves; (3) identificar as dependências no nível do sistema operacional que controlam uma migração; e (4) raciocinar sobre os canais de atualização e as suas assinaturas.

### 11.1 Isolamento e privilégio

Um sistema operacional isola os processos em espaços de endereçamento separados, impõe permissões de arquivos e concede privilégios a usuários e serviços. Chaves guardadas num arquivo que todos podem ler anulam tudo isso; chaves mantidas por um serviço privilegiado, ou por hardware como um TPM, só são alcançáveis por interfaces definidas. O menor privilégio — dar a cada componente apenas o acesso de que ele precisa — se aplica ao material criptográfico tanto quanto aos arquivos.

O inventário da HCU registra, portanto, onde cada chave fica, além do algoritmo que ela usa.

### 11.2 Provedores criptográficos

As aplicações raramente implementam a criptografia elas mesmas. Elas chamam um *provedor*: os provedores do OpenSSL no Linux, o framework CNG no Windows, os repositórios de chaves da plataforma nos sistemas móveis. O provedor e a sua versão decidem quais algoritmos uma aplicação pode usar, então uma migração pós-quântica muitas vezes começa como uma atualização do sistema operacional ou de uma biblioteca. As políticas criptográficas de todo o sistema, em algumas distribuições Linux, definem os algoritmos permitidos num só lugar; isso é valioso para a agilidade, porque uma única mudança de política pode ativar um grupo híbrido em muitos serviços, e perigoso se for mudado sem testes.

### 11.3 Atualizações e boot

Os sistemas operacionais confiam em atualizações assinadas e, pelo boot seguro, em componentes de boot assinados. Hoje essas assinaturas usam tipicamente RSA ou ECDSA. Como os ataques de falsificação posterior visam âncoras de confiança de vida longa, os fornecedores estão planejando assinaturas pós-quânticas ou baseadas em hash para o firmware e as cadeias de boot; a [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) aprova os esquemas baseados em hash com estado LMS e XMSS, adequados à assinatura de firmware quando o signatário consegue gerenciar o estado com cuidado. Os dispositivos cuja ROM de boot só consegue verificar RSA não podem ser atualizados apenas por software.

Esses dispositivos precisam de um plano de substituição.

### 11.4 Exemplo resolvido

Os servidores das agências da HCU rodam uma distribuição Linux cuja versão atual do OpenSSL suporta o grupo híbrido X25519MLKEM768 no TLS. A equipe descobre que o middleware bancário central traz a sua própria biblioteca TLS, mais antiga e ligada estaticamente, e ignora o provedor do sistema operacional. Atualizar o sistema operacional não muda nada para esse middleware; o fornecedor precisa entregar uma nova versão. A visão no nível do sistema operacional revelou uma dependência oculta que uma lista de verificação servidor a servidor teria deixado escapar.

A equipe acrescenta ao inventário uma coluna que registra se cada aplicação usa a biblioteca do sistema ou a sua própria e pede a cada fornecedor um roteiro.

### 11.5 Atividade prática

Numa máquina virtual de laboratório que você controla, liste as bibliotecas criptográficas instaladas e as suas versões e encontre onde está configurada a política criptográfica do sistema (se houver). Registre quais aplicações ligam as suas próprias cópias.

Procure aplicações que trazem a sua própria biblioteca TLS, como alguns bancos de dados, ambientes de execução de linguagens e agentes de fornecedores. As suas versões podem estar anos atrás da biblioteca do sistema. Faça isso apenas numa máquina que você controla e não mude a política criptográfica durante o exercício. O seu registro se torna uma pequena versão do inventário de dependências que a HCU constrói para os seus servidores, e as mesmas perguntas valem em escala.

### 11.6 Erros comuns e limites

- Supor que uma atualização do sistema operacional migra todas as aplicações.
- Editar uma política criptográfica de todo o sistema diretamente na produção.
- Deixar de lado as assinaturas da cadeia de boot e das atualizações.

As aplicações que trazem as suas próprias bibliotecas não mudam quando o sistema operacional muda. As mudanças de política de todo o sistema podem quebrar serviços de maneiras difíceis de rastrear, então teste-as num laboratório e implante-as gradualmente. As assinaturas de boot e de atualização são fáceis de esquecer porque funcionam em silêncio, mas protegem o código mais confiável da máquina e muitas vezes têm os prazos de migração mais longos.

### Exercícios

- **EX021 — Dependência de provedor.** Explique por que uma aplicação que liga estaticamente a sua biblioteca TLS é um item de migração separado. Rubrica: 3 = consequências de dependência, de responsabilidade e de testes.
- **EX022 — Cadeia de boot.** Por que as assinaturas baseadas em hash com estado são adequadas à assinatura de firmware, mas arriscadas para um servidor web? Rubrica: 3 = menciona o gerenciamento do estado, o volume de assinaturas e a recuperação.

### Síntese

Os sistemas operacionais fornecem os provedores criptográficos, o armazenamento de chaves e as cadeias de atualização assinadas de que as aplicações dependem. A migração, portanto, passa pelas camadas do sistema operacional e das bibliotecas — e por todo componente que as contorna.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 40

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) calcular probabilidades de eventos independentes e contagens esperadas; (2) raciocinar sobre probabilidades de falha muito pequenas; (3) usar intervalos de confiança para taxas medidas; e (4) interpretar os números de falha de decifração dos esquemas pós-quânticos.

### 12.1 Eventos raros em escala

Se um evento tem probabilidade *p* por tentativa e há *N* tentativas independentes, o número esperado de ocorrências é *Np*, e a probabilidade de pelo menos uma é 1 − (1 − *p*)^*N* ≈ *Np* quando *Np* é pequeno. Essa fórmula simples explica por que os criptógrafos exigem probabilidades de falha astronomicamente pequenas. Uma taxa de falha de 2^−20 parece minúscula, mas em 10^9 handshakes ela prevê cerca de 950 falhas. O ML-KEM é projetado para que o desencapsulamento honesto falhe com probabilidade de cerca de 2^−139 no ML-KEM-512 e de cerca de 2^−165 no ML-KEM-768, segundo a análise da FIPS 203, então as falhas são desprezíveis em qualquer escala realista.

### 12.2 Atividade prática — Laboratório P

```python
# Lab P (ch 12): how small must a failure probability be? Binomial reasoning for rare events.
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

Observe como cada mudança de 20 bits no expoente desloca a contagem esperada por um fator de cerca de um milhão.

As linhas do meio mostram por que as probabilidades de falha nas normas são tão pequenas. Uma taxa que parece desprezível para um bilhão de operações pode produzir centenas de falhas em um milhão de bilhões, que os grandes serviços alcançam ao longo da sua vida. As últimas linhas mostram uma probabilidade tão pequena que não se esperam falhas em nenhuma escala realista. Quando um projeto cita uma taxa de falha, multiplique-a pelo número de operações que você espera antes de decidir se ela importa.

### 12.3 Taxas medidas e intervalos

Os dados operacionais dão contagens, não probabilidades. Se 3 de 5.000 conexões de teste falham, a estimativa pontual é 0,06%, mas a taxa verdadeira pode ser maior. Um intervalo de confiança de 95% — por exemplo, o intervalo de Wilson usado no Capítulo 29 — expressa essa incerteza. Com amostras pequenas, o limite superior é o que importa para uma decisão de seguir ou não: "estamos razoavelmente confiantes de que a taxa de falha está abaixo de *u*" é a afirmação defensável.

Relate o intervalo junto com a contagem e o tamanho da amostra, para que o leitor possa julgá-lo.

### 12.4 Taxas de base

A probabilidade também protege contra alarmes enganosos. Se um detector sinaliza os handshakes que "parecem tentativas de rebaixamento" com 99% de sensibilidade e 1% de falsos positivos, mas as tentativas reais de rebaixamento ocorrem em um handshake por milhão, então quase todos os alertas são falsos. Pergunte sempre pela taxa de base antes de interpretar uma contagem de alertas.

Neste exemplo, um milhão de handshakes daria cerca de dez mil alertas falsos e aproximadamente um verdadeiro. Uma equipe que recebesse esse fluxo aprenderia a ignorar o alerta, o que anula o seu propósito. Detectores melhores, ou a aplicação da regra apenas onde os rebaixamentos são mais prováveis, aumentam a parcela de alertas verdadeiros. A HCU pede esses números antes de adotar qualquer nova regra de detecção.

### 12.5 Exemplo resolvido

O aplicativo móvel da HCU realiza 2 × 10^8 estabelecimentos de chave por ano. Se um esquema hipotético falhasse com probabilidade 2^−40, as falhas esperadas seriam 2 × 10^8 × 9,1 × 10^−13 ≈ 1,8 × 10^−4 por ano — desprezíveis. Se um bug de implementação elevasse a taxa para 1 em 10^5, a contagem esperada seria de 2.000 por ano, visível nos chamados de suporte. As taxas de falha medidas testam, portanto, a implementação, e não a matemática.

Pediu-se à equipe de suporte da HCU que observasse esse padrão durante o piloto híbrido. Um aumento repentino dos erros de conexão após a atualização de uma biblioteca apontaria para o código, já que a própria taxa de falha do esquema não consegue produzir esses números.

### 12.6 Erros comuns e limites

- Ler a estimativa pontual de uma amostra pequena como a taxa verdadeira.
- Ignorar as taxas de base ao interpretar alertas.
- Supor independência onde as falhas são correlacionadas (um middlebox ruim afeta todas as conexões que passam por ele).

Amostras pequenas podem produzir uma estimativa pontual muito distante da taxa verdadeira, sobretudo para eventos raros; relate o intervalo. As taxas de base decidem se um alerta provavelmente é real. As falhas correlacionadas, como muitas conexões passando por um único dispositivo defeituoso, quebram a independência que os modelos simples supõem, então as falhas se agrupam e as médias enganam. Verifique onde as falhas ocorrem antes de tratá-las como independentes.

### Exercícios

- **EX023 — Falhas esperadas.** Com *p* = 2^−30 e 10^12 operações, calcule o número esperado de falhas. Rubrica: 3 = ≈ 931, com o método mostrado.
- **EX024 — Taxa de base.** Para o detector de rebaixamento de 12.4, estime a fração de alertas verdadeiros entre 10^8 handshakes. Rubrica: 3 = cerca de 100 verdadeiros em cerca de 10^6 alertas (≈ 0,01%), com o método mostrado.

### Síntese

Contagens esperadas, limites de confiança e taxas de base transformam probabilidades minúsculas e dados operacionais ruidosos em decisões defensáveis.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 40

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) distinguir identificação, autenticação e autorização; (2) explicar como os certificados e a infraestrutura de chaves públicas (PKI) ligam identidades a chaves; (3) identificar os elementos vulneráveis à computação quântica nos fluxos de autenticação comuns; e (4) planejar onde as assinaturas pós-quânticas serão necessárias primeiro.

### 13.1 Três etapas

A *identificação* alega uma identidade; a *autenticação* a prova; a *autorização* decide o que a parte autenticada pode fazer. Senhas, códigos de uso único e passkeys autenticam usuários; certificados e assinaturas autenticam máquinas e software. A autorização é geralmente uma contabilidade simétrica — listas de controle de acesso e papéis — e não é ameaçada diretamente pelos computadores quânticos. A autenticação baseada em assinaturas de chave pública é.

Manter as três etapas separadas ajuda uma equipe de migração a manter o foco. As tabelas de papéis e as listas de acesso da HCU não precisam de mudança por motivos quânticos. Todo lugar onde uma assinatura ou um login por chave pública prova a identidade precisa, e esses lugares estão espalhados por celulares, servidores, a autoridade certificadora e as versões de software. Listá-los por etapa torna o escopo do trabalho mais claro.

### 13.2 A PKI em resumo

Um certificado é uma declaração assinada por uma autoridade certificadora (AC): "esta chave pública pertence a este nome, válida até esta data". Os verificadores confiam num pequeno conjunto de ACs raiz e seguem as cadeias até elas. Se um adversário consegue calcular a chave privada de uma AC a partir da sua chave pública — como o algoritmo de Shor permitiria para o RSA e o ECDSA —, ele pode emitir certificados para qualquer nome. Como as chaves raiz têm vida longa e estão amplamente embutidas, a PKI é o alvo arquetípico da falsificação posterior. As normas de assinatura pós-quântica oferecem substitutos: o ML-DSA, na [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), para uso geral, e o SLH-DSA, na [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205), como opção conservadora baseada em hash.

### 13.3 Fluxos de autenticação

As passkeys e os autenticadores FIDO usam assinaturas de chave pública (muitas vezes ECDSA) dentro de um elemento seguro. Os tokens de login único são assinados com RSA ou ECDSA. Os certificados de assinatura de código protegem as atualizações de software. Cada fluxo tem um caminho de migração diferente: os tokens de vida curta podem mudar rapidamente quando as bibliotecas suportarem o ML-DSA; os autenticadores de hardware precisam de dispositivos novos; as ACs raiz precisam de um longo planejamento, porque as partes confiantes precisam primeiro confiar nas novas raízes.

A HCU agrupa os seus fluxos pelo caminho de que cada um precisa. Os tokens de vida curta vêm primeiro; a AC, por último.

### 13.4 Exemplo resolvido

A HCU lista os seus usos de autenticação: as passkeys dos associados (ECDSA no hardware do celular), os tokens de SSO dos funcionários (RSA-2048, vida de 10 minutos), a AC interna (raiz RSA-4096, validade de 20 anos), a assinatura de código do aplicativo móvel (ECDSA, controlada pela plataforma). O risco de falsificação posterior é maior para a raiz de vida longa e para a assinatura de código, em que uma assinatura falsificada permitiria a um adversário distribuir software malicioso. Os tokens de SSO de vida curta têm prioridade menor: falsificar um exige um computador quântico no momento do ataque, e a chave pode ser trocada rapidamente assim que existir um.

A lista também mostra quem controla cada mudança. A HCU pode mudar os seus próprios tokens e a sua AC; para as passkeys e a assinatura de código, depende dos fabricantes de celulares e das plataformas de aplicativos.

### 13.5 Atividade prática

Desenhe a hierarquia de certificados da HCU: raiz, duas intermediárias, folhas de servidor e de cliente. Anote em cada uma o algoritmo, a validade e quem precisa confiar nela. Marque quais mudanças exigem que as partes confiantes atualizem os seus repositórios de confiança.

As partes confiantes incluem os celulares dos associados, os servidores das agências, os caixas eletrônicos e os bancos parceiros, cada um com uma forma diferente de atualizar a confiança. Alguns podem receber uma nova raiz numa atualização de rotina; outros, como os caixas eletrônicos, podem precisar da visita de um fornecedor. Marque esses com cuidado, porque eles ditam o ritmo de toda a migração dos certificados. Compare o seu diagrama com o de um colega e confira se os dois puseram os mesmos períodos de validade nos mesmos certificados.

### 13.6 Erros comuns e limites

- Tratar as listas de autorização como vulneráveis à computação quântica.
- Planejar migrar os certificados folha antes que as partes confiantes confiem numa raiz pós-quântica.
- Esquecer os autenticadores de hardware que não podem ser atualizados.

As listas de acesso e as tabelas de papéis não usam matemática de chave pública, então os computadores quânticos não as ameaçam. Emitir certificados folha pós-quânticos antes que as partes confiantes confiem numa raiz correspondente faz as conexões falharem. Os autenticadores de hardware com algoritmos fixos só podem ser substituídos, o que exige orçamento e anos. Um plano que os ignora parecerá completo no papel e travará na prática, quando se descobrir que os dispositivos estão nos bolsos dos associados.

### Exercícios

- **EX025 — Classificar.** Para senhas, passkeys, tokens de SSO e uma AC raiz interna, declare se um computador quântico ameaça o mecanismo e por quê. Rubrica: 3 = quatro entradas corretas e fundamentadas.
- **EX026 — Ordem do trabalho.** Explique por que uma raiz pós-quântica precisa ser distribuída às partes confiantes antes que os certificados folha pós-quânticos sejam úteis. Rubrica: 3 = lógica de validação da cadeia enunciada.

### Síntese

Os computadores quânticos ameaçam a autenticação de chave pública, e não a lógica de autorização. As raízes da PKI e a assinatura de código são os alvos de vida longa; os tokens de vida curta podem vir depois.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 40

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem

Você vai (1) enunciar princípios centrais de privacidade, como a limitação da finalidade e a minimização; (2) relacionar o dano à privacidade com o tempo de confidencialidade; (3) explicar por que o "colete agora, decifre depois" é um problema de privacidade; e (4) projetar uma medição que minimize os dados para o trabalho de migração.

### 14.1 Princípios

A legislação e a prática de privacidade compartilham princípios comuns: coletar dados pessoais para uma finalidade declarada, coletar apenas o necessário (*minimização*), guardá-los apenas pelo tempo necessário (*limitação do armazenamento*), protegê-los adequadamente e ser transparente. Esses princípios dizem respeito às pessoas, e não aos sistemas; um dano à privacidade é um dano a um associado cujos dados são expostos, mesmo que a organização não sofra perda alguma.

Numa migração quântica, esses princípios moldam duas coisas: quais dados mais precisam de proteção e como o próprio trabalho de migração trata as informações pessoais encontradas pelo caminho.

### 14.2 Tempo de vida do dano

Alguns dados pessoais deixam de importar rapidamente; outros continuam sensíveis por toda a vida — condições de saúde, dificuldades financeiras, documentos de identidade. O "colete agora, decifre depois" transforma a sensibilidade de vida longa em risco presente: o tráfego gravado hoje pode revelar amanhã o que um associado contou em confiança décadas antes. Para a privacidade, o *x* relevante na desigualdade de Mosca é o tempo de vida do dano à pessoa, que pode exceder o período de retenção da organização. Apagar um registro do banco de dados da HCU não apaga uma cópia que um adversário gravou em trânsito.

### 14.3 A minimização como controle quântico

A proteção mais barata para os dados é não enviá-los. Reduzir o que atravessa as redes — tokenizar números de conta, manter os campos sensíveis no data center e enviar apenas resultados derivados — diminui a exposição ao HNDL, qualquer que seja o algoritmo. A minimização também se aplica à própria medição da migração: um inventário precisa de nomes de algoritmos e identificadores de hosts, e não do conteúdo das mensagens.

A primeira revisão do tráfego das agências da HCU encontrou nomes de associados viajando junto com transações que precisavam apenas de um token de conta. Substituir os nomes por tokens reduziu a exposição de imediato, antes que qualquer algoritmo mudasse.

### 14.4 Exemplo resolvido

O fluxo de pedidos de empréstimo da HCU envia os perfis completos dos solicitantes das agências para a sede, incluindo anotações médicas nos casos de dificuldade financeira. Uma revisão de privacidade descobre que os analistas de crédito da sede precisam apenas de um indicador de dificuldade e de um valor. Mudar o formulário para que as anotações médicas fiquem no processo da agência reduz tanto a pegada de privacidade quanto os dados expostos à decifração futura, antes que qualquer algoritmo pós-quântico seja implantado. A troca de chaves híbrida na VPN das agências é então agendada para os fluxos restantes.

### 14.5 Atividade prática

Para três fluxos de dados sintéticos da HCU, liste os campos de dados pessoais, a finalidade e quais campos poderiam ser removidos, tokenizados ou agregados antes da transmissão.

Os candidatos típicos são nomes completos enviados onde um identificador bastaria, datas de nascimento enviadas para verificações que só precisam de uma faixa etária e números de conta enviados onde um token funciona. Para cada campo que você remover, diga quem perceberia e se algum processo quebra. Depois, estime quanto a mudança reduz os dados de vida longa que atravessam a rede, que é a exposição da qual o "colete agora, decifre depois" depende.

### 14.6 Erros comuns e limites

- Igualar o período de retenção ao tempo de vida do dano.
- Coletar capturas completas de pacotes para um inventário.
- Tratar a PQC como substituta da minimização, e não como complemento.

O dano da divulgação pode durar muito mais do que o registro é guardado: um arquivo de financiamento imobiliário apagado que foi gravado em trânsito ainda pode ser decifrado depois. As capturas completas coletam dados pessoais de que o inventário nunca precisou e criam um novo repositório a proteger. Os algoritmos pós-quânticos protegem o que é enviado; a minimização reduz o que é enviado. Os dois funcionam juntos, e nenhum substitui o outro.

### Exercícios

- **EX027 — Tempo de vida do dano.** Dê dois tipos de dados cujo dano à privacidade dure mais do que o período de retenção da HCU e explique a consequência para o HNDL. Rubrica: 3 = dois exemplos, com raciocínio ligado ao tráfego gravado.
- **EX028 — Minimize o inventário.** Especifique os campos mínimos de que um inventário TLS passivo precisa e dois campos que ele não deve coletar. Rubrica: 3 = listas justificadas.

### Síntese

O dano à privacidade pode durar mais do que qualquer cronograma de retenção, o que faz do "colete agora, decifre depois" uma questão de privacidade. A minimização reduz a exposição sob qualquer algoritmo e deve preceder e acompanhar a PQC.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 40

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) definir validade, confiabilidade e cobertura para as medições de segurança; (2) escolher indicadores de prontidão criptográfica; (3) registrar a proveniência de cada observação; e (4) apresentar as medições com os seus pontos cegos.

### 15.1 O que torna uma medição útil

Uma medição é *válida* se mede o que afirma medir, *confiável* se dá o mesmo resultado quando repetida, e tem *cobertura* conhecida se sabemos que parcela da população ela observa. A "porcentagem de conexões TLS que usam troca de chaves híbrida" é válida se contada a partir das mensagens ServerHello, confiável se o sensor for estável, e a sua cobertura é a parcela do tráfego que passa pelo sensor. Sem a cobertura, um número de 90% pode descrever apenas o décimo fácil do parque.

A cobertura é a propriedade que mais falta nos painéis de segurança.

### 15.2 Indicadores de prontidão

Indicadores úteis para uma migração quântica incluem: a parcela de ativos com um inventário criptográfico conhecido; a parcela de fluxos de dados de vida longa protegidos por troca de chaves híbrida; a parcela de certificados emitidos por ACs capazes de emitir certificados pós-quânticos; o número de fornecedores com um roteiro de PQC publicado; e o tempo médio para mudar um algoritmo por configuração. Cada indicador deve ter um responsável, uma fonte e uma frequência de atualização.

A HCU começou com três desses e acrescentou os outros quando os responsáveis foram acordados. Cada um tem uma fonte.

### 15.3 Proveniência

Registre para cada observação: o que foi observado, por qual método (rede passiva, configuração, varredura de código, declaração do fornecedor), quando e por quem. Os métodos diferem em confiança: um handshake observado é uma evidência mais forte do que a ficha técnica de um fornecedor. No TLS 1.3, um sensor passivo vê o grupo selecionado, mas não o certificado do servidor, que é cifrado, então os algoritmos dos certificados precisam vir de evidências dos endpoints ou da configuração. Misturar métodos sem rótulos faz os painéis parecerem mais certos do que são.

O inventário da HCU tem uma coluna para o método e outra para a data, e os painéis mostram as duas.

### 15.4 Exemplo resolvido

O primeiro painel da HCU relata "92% das conexões híbridas". Ao inspecioná-lo, descobre-se que o único sensor fica diante do novo gateway web, que já usa o X25519MLKEM768; as VPNs das agências e a rede de caixas eletrônicos são invisíveis para ele. O painel corrigido mostra "tráfego web: 92% híbrido (cobertura do sensor: 100% do gateway web); VPN: 0% (evidência de configuração, 40/40 agências); caixas eletrônicos: desconhecido (sem sensor)". O número de destaque caiu, e a qualidade das decisões subiu.

A correção não mudou nenhum sistema, apenas o que o painel afirmava. Os gestores passaram a ver onde restava trabalho e onde a equipe simplesmente não tinha visibilidade. A linha dos caixas eletrônicos levou a um pedido ao fornecedor dos caixas eletrônicos por evidências de configuração, já que acrescentar um sensor de rede ali não era possível.

### 15.5 Atividade prática

Projete três indicadores de prontidão para a HCU. Para cada um, dê a definição, a fonte, a cobertura, o responsável e a frequência de atualização, e nomeie uma forma como ele poderia enganar.

Uma boa definição diz exatamente o que é contado e o que não é. A cobertura deve declarar que parte do parque a fonte consegue ver. Um responsável é uma pessoa ou um papel que vai perceber quando o número parecer errado. A forma como um indicador poderia enganar é muitas vezes a sua linha mais útil: por exemplo, uma contagem de fornecedores com roteiros não diz nada sobre se os roteiros são realistas ou têm datas.

### 15.6 Erros comuns e limites

- Relatar uma porcentagem sem o seu denominador e a sua cobertura.
- Tratar as alegações dos fornecedores como observações.
- Contar conexões quando a decisão diz respeito a ativos ou classes de dados.

Uma porcentagem sem a sua base pode esconder uma amostra minúscula ou enviesada. As declarações dos fornecedores são úteis, mas não testadas; rotule-as como alegações até que alguém observe o comportamento. Contar conexões favorece os sistemas movimentados, enquanto as decisões de migração geralmente dizem respeito a quais ativos ou classes de dados estão protegidos. Um único serviço web movimentado pode fazer o número parecer bom enquanto um enlace de arquivo, pouco movimentado mas sensível, continua clássico. Escolha a unidade que corresponde à decisão.

### Exercícios

- **EX029 — Cobertura.** Reescreva "95% dos nossos certificados estão prontos para PQC" de modo que declare o método, a cobertura e o denominador. Rubrica: 3 = os três presentes e plausíveis.
- **EX030 — Projeto de indicador.** Proponha um indicador para "capacidade de mudar algoritmos rapidamente" e explique como medi-lo. Rubrica: 3 = definição, método de medição, limitação.

### Síntese

Medições válidas e confiáveis, com cobertura e proveniência declaradas, permitem que os tomadores de decisão vejam tanto o progresso quanto os pontos cegos.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 40

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever fronteiras de confiança, zonas e defesa em profundidade; (2) desenhar um diagrama de fluxo de dados que mostre as proteções criptográficas; (3) explicar a agilidade criptográfica como uma propriedade da arquitetura; e (4) identificar as fronteiras de confiança de vida longa que atravessam o tempo.

### 16.1 Fronteiras e zonas

Uma *fronteira de confiança* separa componentes com níveis de confiança diferentes — a internet e a camada web da HCU, a camada web e a zona bancária central, uma agência e o data center. Os dados que atravessam uma fronteira precisam de uma proteção adequada à sua sensibilidade: cifração, autenticação, validação. A *defesa em profundidade* sobrepõe controles independentes, para que uma falha não exponha tudo.

Para a migração quântica, as fronteiras que mais importam são aquelas em que dados de vida longa saem de uma zona protegida por uma rede que outra pessoa poderia gravar.

### 16.2 Diagramas de fluxo de dados

Um diagrama de fluxo de dados mostra entidades externas, processos, repositórios de dados e os fluxos entre eles, com as fronteiras de confiança desenhadas como linhas tracejadas. Anotar cada fluxo com o protocolo, o algoritmo de troca de chaves, o algoritmo de autenticação e o tempo de vida dos dados transforma o diagrama num mapa de exposição quântica: qualquer fluxo que atravessa uma fronteira não confiável com dados de vida longa e troca de chaves clássica é candidato ao "colete agora, decifre depois".

O primeiro diagrama da HCU levou uma semana para ser anotado, sobretudo porque ninguém sabia qual algoritmo vários fluxos usavam. Essas lacunas foram tão úteis quanto as respostas: cada uma virou uma pergunta para um responsável ou um fornecedor. Desenhar o diagrama antes de escolher qualquer algoritmo novo fez o plano partir do que os sistemas realmente fazem.

### 16.3 Agilidade criptográfica

A *agilidade criptográfica* é a capacidade de trocar algoritmos criptográficos com esforço e risco limitados. Na arquitetura, ela significa política centralizada, identificadores de algoritmo que viajam com os dados, bibliotecas que suportam vários algoritmos e interfaces que toleram chaves e assinaturas maiores. O [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) do NIST discute as considerações sobre a agilidade criptográfica. Uma arquitetura sem agilidade trata a migração PQC como uma reconstrução única; uma arquitetura ágil a trata como a primeira de várias mudanças planejadas.

Para a HCU, a agilidade é testada perguntando quanto tempo levaria para trocar um algoritmo na VPN das agências.

### 16.4 Fronteiras no tempo

Algumas fronteiras não são atravessadas no espaço, mas no tempo. Um financiamento imobiliário assinado hoje será verificado por um tribunal ou um comprador anos depois; um arquivo cifrado hoje será decifrado durante uma auditoria futura. A arquitetura deve mostrar os serviços de longo prazo — carimbo de tempo, recifração de arquivos, renovação de evidências — como componentes cuja própria criptografia precisa ser migrada.

O arquivo de financiamentos imobiliários da HCU é o caso mais claro: a sua cifração e as suas assinaturas precisam continuar funcionando, e seguras, décadas depois da criação dos documentos. Cada uma precisa de um responsável.

### 16.5 Exemplo resolvido

O diagrama da HCU mostra aplicativo móvel → gateway web (fronteira com a internet, TLS híbrido), gateway web → sistema bancário central (interno, TLS clássico), sistema bancário central → arquivo (interno, AES-256 em repouso, chaves envelopadas com RSA-OAEP), agência → data center (fronteira da WAN, IPsec ECDH). A anotação revela duas prioridades: a WAN das agências, pelo HNDL, e as chaves do arquivo envelopadas com RSA, que ficam expostas se as chaves envelopadas forem algum dia copiadas para fora do local.

O enlace TLS interno entre o gateway e o sistema bancário central é clássico, mas fica dentro do data center, o que reduz a sua prioridade. O diagrama tornou essas escolhas visíveis numa só página, e o escritório de segurança da HCU o usou para acordar o plano de migração do primeiro ano.

### 16.6 Erros comuns e limites

- Desenhar diagramas sem algoritmos e tempos de vida.
- Considerar apenas as fronteiras de rede, e não as fronteiras no tempo.
- Fixar as escolhas de algoritmo no código da aplicação.

Um diagrama sem algoritmos e tempos de vida não consegue mostrar a exposição quântica, por mais organizado que pareça. As fronteiras no tempo são fáceis de deixar passar porque não aparecem nos mapas de rede; os arquivos, os carimbos de tempo e os registros assinados as atravessam em silêncio. As escolhas de algoritmo fixadas no código da aplicação transformam cada mudança futura num projeto de software, o oposto da agilidade criptográfica. Registre cada escolha na configuração ou na política, para que possa ser encontrada e mudada depois.

### Exercícios

- **EX031 — Mapa de exposição.** Para o diagrama da HCU em 16.5, ordene os quatro fluxos pela prioridade de HNDL e justifique a ordem. Rubrica: 3 = ordem coerente com a fronteira, o tempo de vida e o algoritmo.
- **EX032 — Recursos de agilidade.** Liste três recursos de arquitetura que permitiriam à HCU trocar o ML-KEM-768 por outro KEM, se necessário. Rubrica: 3 = três recursos concretos e distintos.

### Síntese

As fronteiras de confiança, os fluxos de dados anotados e a agilidade criptográfica permitem que os arquitetos localizem a exposição quântica e projetem para trocas repetidas de algoritmo, inclusive nas fronteiras atravessadas no tempo.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 40

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) distinguir cifração simétrica, funções de hash, MACs, troca de chaves, KEMs e assinaturas; (2) explicar os níveis de segurança e as categorias pós-quânticas do NIST; (3) construir e quebrar uma assinatura de uso único de Lamport; e (4) nomear as três normas pós-quânticas finais do NIST.

### 17.1 A caixa de ferramentas

A *cifração simétrica* (AES) usa uma única chave compartilhada; as *funções de hash* (SHA-2, SHA-3) comprimem os dados numa impressão digital; os *MACs* (HMAC) provam a integridade com uma chave compartilhada; a *troca de chaves* (Diffie–Hellman) permite que duas partes derivem um segredo compartilhado por um canal público; um *mecanismo de encapsulamento de chaves* (KEM) permite que uma parte encapsule um segredo novo para a chave pública da outra; as *assinaturas* permitem que qualquer um verifique que o detentor de uma chave privada aprovou uma mensagem. Os computadores quânticos ameaçam a troca de chaves, a cifração de chave pública e as assinaturas baseadas em fatoração e logaritmos discretos; as primitivas simétricas e os hashes precisam, no máximo, de parâmetros maiores.

### 17.2 As normas do NIST

Em agosto de 2024, o NIST publicou três normas pós-quânticas: a [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), ML-KEM, um KEM baseado em reticulados com os conjuntos de parâmetros ML-KEM-512, -768 e -1024; a [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), ML-DSA, uma assinatura baseada em reticulados; e a [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205), SLH-DSA, uma assinatura baseada em hash sem estado. Antes disso, a [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) havia aprovado as assinaturas baseadas em hash com estado LMS e XMSS. O NIST define as *categorias* de segurança 1–5 por comparação com a quebra do AES-128, do SHA-256, do AES-192, do SHA-384 e do AES-256; o ML-KEM-768 visa a categoria 3.

Para a HCU, os conjuntos de parâmetros da categoria três são o ponto de partida comum, já que oferecem uma margem confortável com tamanho moderado.

### 17.3 Atividade prática — Laboratório L

O esquema de Lamport assina uma mensagem revelando, para cada bit do seu hash, um de dois valores secretos cujos hashes formam a chave pública.

```python
# Lab L (ch 17): Lamport one-time signatures from SHA-256 - the idea under SLH-DSA, LMS and XMSS.
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

A segurança se apoia apenas na função de hash, e é por isso que as assinaturas baseadas em hash são consideradas conservadoras. A reutilização é fatal: duas assinaturas revelam os dois segredos em muitas posições. O SLH-DSA constrói árvores de assinaturas de uso único e de poucos usos, para que uma única chave possa assinar muitas mensagens sem estado; o LMS e o XMSS o fazem com um estado que o signatário nunca pode repetir.

### 17.4 Exemplo resolvido

O arquiteto da HCU pergunta qual primitiva atende a cada necessidade: a cifração do arquivo (AES-256, manter), o transporte de chaves para o arquivo (KEM: ML-KEM-768 num híbrido), a assinatura dos extratos (ML-DSA-65 quando houver suporte, ou híbrido com ECDSA durante a transição), a assinatura do firmware dos caixas eletrônicos (LMS pela SP 800-208 ou SLH-DSA, porque o volume de assinaturas é baixo e o conservadorismo é valorizado).

Cada escolha decorre da necessidade, e não do algoritmo mais novo. A cifração simétrica fica porque a busca de Grover deixa o AES-256 forte. O transporte de chaves precisa de um KEM. As assinaturas precisam ser verificáveis enquanto a declaração assinada importar. A assinatura de firmware favorece os esquemas baseados em hash porque a sua segurança se apoia apenas nas funções de hash, e o baixo volume de assinaturas torna prático o gerenciamento do estado.

### 17.5 Erros comuns e limites

- Chamar o ML-KEM de "cifração"; ele é um KEM que produz um segredo compartilhado.
- Reutilizar chaves de assinatura de uso único ou com estado.
- Tratar o laboratório de Lamport de brinquedo como código utilizável.

Um KEM dá aos dois lados um segredo compartilhado; os próprios dados são então cifrados com um algoritmo simétrico. As chaves de assinatura com estado nunca podem assinar duas vezes com a mesma chave de uso único, o que significa que o signatário precisa acompanhar o estado de forma confiável, inclusive entre backups e falhas. O esquema de Lamport do laboratório existe para mostrar a ideia das assinaturas baseadas em hash; ele é inseguro na prática e nunca deve ser usado fora da sala de aula.

### Exercícios

- **EX033 — Escolha a primitiva.** Para o armazenamento de senhas, a integridade das mensagens entre dois servidores da HCU, o acordo de chave de sessão e a aprovação de documentos, nomeie a primitiva e um algoritmo padronizado. Rubrica: 3 = quatro escolhas corretas.
- **EX034 — Reutilização.** Usando a saída do Laboratório L, explique por que a segunda assinatura de Lamport permite a falsificação. Rubrica: 3 = os dois segredos em muitas posições, combinados para assinar novas mensagens.

### Síntese

Os computadores quânticos quebram a troca de chaves e as assinaturas de chave pública baseadas em fatoração e logaritmos discretos. As FIPS 203, 204 e 205 e a SP 800-208 do NIST fornecem os substitutos; as primitivas simétricas e de hash permanecem, com tamanhos adequados.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 40

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta pesquisável; (2) escolher entre revisão de literatura, medição, experimento e estudo de caso; (3) projetar um estudo de medição simples com população e amostra declaradas; e (4) identificar as ameaças à validade.

### 18.1 Perguntas

Uma boa pergunta de pesquisa é específica, respondível com as evidências disponíveis e relevante para uma decisão. "A PQC é boa?" não é pesquisável. "Que parcela dos fluxos entre as agências da HCU e o data center leva dados com um tempo de confidencialidade acima de 15 anos?" é. As perguntas nesta área costumam ter as formas *quanto* (medição), *o que acontece se* (experimento), *como foi* (estudo de caso) ou *o que se sabe* (revisão de literatura).

O escritório de segurança da HCU pede à equipe de estudantes perguntas do segundo tipo, porque cada resposta muda uma prioridade da migração ou uma linha do orçamento.

### 18.2 Métodos

Uma *revisão de literatura* resume sistematicamente as fontes primárias, registrando os termos de busca e as regras de inclusão. Um *estudo de medição* conta propriedades de uma população, como os grupos TLS oferecidos por um conjunto de servidores. Um *experimento* muda um fator e observa o efeito, como a latência do handshake com e sem um grupo híbrido num laboratório. Um *estudo de caso* examina uma migração em profundidade. Cada método responde a perguntas diferentes; combiná-los fortalece as conclusões.

Os estudos da própria HCU combinam uma medição do seu parque com experimentos de laboratório nos enlaces mais lentos das agências.

### 18.3 Populações, amostras e validade

Declare a população (todos os serviços web da HCU), o quadro de amostragem (os serviços no registro de ativos) e a amostra (os alcançáveis a partir da rede de teste). A *validade interna* pergunta se o efeito observado é causado pelo fator estudado; a *validade externa* pergunta se os resultados se generalizam. Um experimento de latência numa rede de laboratório rápida pode não prever os resultados nos enlaces das agências rurais; isso é um limite de validade externa, e não uma falha, desde que seja declarado.

O próprio registro de ativos da HCU pode estar incompleto, o que é um problema de quadro a ser declarado.

### 18.4 Exemplo resolvido

Pergunta: "Ativar o X25519MLKEM768 no gateway de teste da HCU aumenta o tempo mediano de handshake dos clientes das agências?" Método: experimento de laboratório com latência de agência emulada de 40 ms e 1% de perda; 1.000 handshakes por condição, alternando a ordem para controlar a deriva. Resultado (sintético): a mediana aumenta 0,9 ms; o percentil 99 aumenta 3 ms porque alguns ClientHellos precisam de um segundo segmento. Nota de validade: a perda emulada não reproduz o comportamento do proxy de inspeção real da agência.

O relatório declara tanto a mediana quanto a cauda e o limite da emulação. A equipe de rede da HCU então testou numa agência com o proxy real antes da implantação ampla, que é onde a lacuna de validade externa apareceria.

### 18.5 Atividade prática

Escreva um protocolo de estudo de uma página para medir quantos serviços internos da HCU suportam o TLS 1.3, incluindo a população, o quadro, a amostra, o método, o tratamento dos dados e as ameaças à validade.

Um protocolo escrito antes da coleta dos dados impede que as escolhas posteriores sejam moldadas pelos resultados. Diga como você vai contar um serviço que não responde, como vai tratar os serviços fora do registro e por quanto tempo os dados serão guardados. As ameaças à validade podem incluir serviços alcançáveis apenas a partir de algumas redes ou uma rede de teste diferente da produção. Peça a um colega que leia o protocolo e tente encontrar uma escolha que você deixou sem declarar.

### 18.6 Erros comuns e limites

- Perguntas amplas demais para serem respondidas.
- Quadros de amostragem não declarados que escondem o viés de seleção.
- Generalizar a latência do laboratório para as redes de produção.

Uma pergunta ampla produz respostas vagas sobre as quais ninguém consegue agir. Um quadro não declarado esconde quais sistemas nunca estiveram na amostra, e os ausentes muitas vezes são os mais antigos e frágeis. As redes de laboratório são mais limpas que a produção, então os resultados de latência e de falhas devem ser apresentados como limites inferiores até serem confirmados em campo. Escreva cada limite ao lado do resultado que ele afeta, e não num lugar separado que os leitores podem pular.

### Exercícios

- **EX035 — Afie a pergunta.** Transforme "Os nossos fornecedores estão prontos para a computação quântica?" numa pergunta pesquisável, com um método. Rubrica: 3 = específica, mensurável, relevante para a decisão.
- **EX036 — Validade.** Nomeie uma ameaça à validade interna e uma à validade externa no experimento de 18.4. Rubrica: 3 = as duas corretas e explicadas.

### Síntese

Perguntas pesquisáveis, populações explícitas e limites de validade declarados transformam opiniões sobre a prontidão quântica em evidências.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 40

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Segurança quântica e pós-quântica: escopo e teoria

### Objetivos de aprendizagem

Você vai (1) definir o escopo da segurança quântica e pós-quântica; (2) enunciar a desigualdade de Mosca e aplicá-la variando as hipóteses; (3) distinguir a criptografia pós-quântica da distribuição quântica de chaves; e (4) resumir a situação das normas do NIST e das orientações de transição.

### 19.1 Escopo

A área cobre quatro perguntas. O que os computadores quânticos podem fazer com a criptografia? (O Shor quebra o RSA, o Diffie–Hellman e as curvas elípticas; o Grover enfraquece quadraticamente a busca simétrica.) O que substitui os algoritmos vulneráveis? (A criptografia pós-quântica: algoritmos clássicos que se acredita resistirem ao ataque quântico.) Como as organizações migram? (Inventário, priorização, implantação híbrida, agilidade.) E que papel, se algum, cabe às tecnologias de comunicação quântica, como a distribuição quântica de chaves (QKD)? Este livro se concentra nas três primeiras, porque a PQC roda nos computadores e redes de hoje.

A QKD é discutida brevemente abaixo.

### 19.2 PQC versus QKD

Os algoritmos PQC, como o ML-KEM, são implementações em software e hardware de esquemas matemáticos; eles funcionam em qualquer rede. A QKD usa estados quânticos da luz para estabelecer chaves e precisa de enlaces dedicados e nós confiáveis, e ainda precisa de autenticação clássica. A [NSA](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/) declarou que não apoia a QKD para os sistemas de segurança nacional e recomenda, em vez disso, os algoritmos resistentes à computação quântica. Para uma organização como a HCU, a PQC é o caminho prático.

Os enlaces da HCU passam por linhas dedicadas alugadas e pela internet, onde a QKD exigiria uma infraestrutura nova.

### 19.3 A desigualdade de Mosca

Mosca (2018) deu à área a sua regra de planejamento. Seja *x* o tempo durante o qual os dados precisam continuar seguros, *y* o tempo que a migração leva e *z* o tempo até que exista um computador quântico criptograficamente relevante (CRQC). Se *x* + *y* > *z*, você já está atrasado para esses dados. Como *z* é desconhecido, varie-o: as decisões corretas em toda uma faixa plausível de *z* são robustas.

Para a HCU, os trinta anos do arquivo tornam grande o lado esquerdo, qualquer que seja o tempo de migração escolhido. Mesmo que um CRQC estivesse a quarenta anos de distância, uma migração que levasse mais de dez anos deixaria parte dos dados do arquivo exposta. A desigualdade transforma uma pergunta irrespondível, quando a máquina vai chegar, numa pergunta utilizável: para quais dados a resposta não importa?

### 19.4 Atividade prática — Laboratório M

```python
# Lab M (ch 19): Mosca's inequality x + y > z for synthetic Harbourline Credit Union data, sweeping z.
assets = [  # (name, shelf-life x in years, migration time y in years) - synthetic
    ("mortgage archive", 30, 4), ("member records", 10, 3), ("card authorisation", 0.01, 5), ("branch VPN traffic", 7, 2)]
for z in (10, 15, 20):  # years until a cryptographically relevant quantum computer: an assumption, not a forecast
    late = [n for n, x, y in assets if x + y > z]
    print(f"z={z:>2}: at risk now -> {', '.join(late) if late else 'none'}")
```

Saída esperada:

```text
z=10: at risk now -> mortgage archive, member records
z=15: at risk now -> mortgage archive
z=20: at risk now -> mortgage archive
```

As mensagens de autorização de cartão têm vida curta, então saem da lista; o arquivo de financiamentos imobiliários está em risco sob todas as hipóteses da variação. Essa é a conclusão robusta.

O laboratório varia o tempo de chegada desconhecido em três valores e, para cada um, imprime as classes de dados da HCU cujo tempo de confidencialidade mais o tempo de migração o excede. Os registros dos associados aparecem apenas sob a hipótese mais curta, então a sua situação depende da data incerta; o arquivo de financiamentos imobiliários aparece nas três. As classes que mudam de situação dentro da variação são onde a data realmente importa, e elas precisam de um julgamento mais cuidadoso e de revisão regular à medida que as estimativas mudam. As classes que nunca aparecem, como as mensagens de cartão, podem esperar as atualizações de rotina.

### 19.5 Normas e situação da transição

As FIPS 203, 204 e 205 são finais (agosto de 2024). A [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) dá recomendações para o uso de KEMs. O rascunho [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) do NIST propõe tornar obsoletos, depois de 2030, os algoritmos vulneráveis à computação quântica com segurança de 112 bits e proibir, depois de 2035, os algoritmos de chave pública vulneráveis à computação quântica; como rascunho, ele sinaliza uma direção, e não datas vinculantes. O FN-DSA (FIPS 206) e uma norma baseada no HQC estavam em desenvolvimento em 12 de outubro de 2026. O [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) define a terminologia dos esquemas híbridos pós-quânticos/tradicionais (PQ/T).

A HCU acompanha esses documentos com a sua situação e a data da verificação.

### 19.6 Exemplo resolvido

O conselho da HCU pede uma resposta num único slide. "Os computadores quânticos capazes de quebrar a nossa criptografia de chave pública não existem hoje, e a sua data é incerta. O nosso arquivo de financiamentos imobiliários precisa permanecer confidencial por 30 anos, então as transferências gravadas estão em risco sob qualquer cronograma plausível; vamos proteger esses fluxos primeiro, com troca de chaves híbrida pós-quântica, seguindo as normas de 2024 do NIST. As assinaturas e os dispositivos seguem um cronograma planejado, alinhado ao rascunho das orientações de transição do NIST."

O slide evita uma data prevista, declara a exigência que gera a urgência e nomeia a primeira ação. Os membros do conselho podem contestar qualquer parte, e cada parte aponta para evidências no plano. Um slide seguinte lista o que o conselho vai ouvir a cada trimestre.

### 19.7 Erros comuns e limites

- Citar uma única data de CRQC como fato.
- Apresentar a QKD como substituta direta da PQC.
- Tratar as datas do rascunho IR 8547 como finais.

As estimativas publicadas de quando um CRQC poderia existir variam muito e mudam à medida que a pesquisa avança, então uma única data dá uma falsa confiança. A QKD precisa de hardware especial e de enlaces dedicados, resolve apenas a distribuição de chaves e ainda precisa de autenticação clássica. As orientações em rascunho estão abertas a comentários e podem mudar antes da publicação. Cada erro faz um plano parecer mais firme do que as evidências permitem, e o plano quebra quando a hipótese quebra.

### Exercícios

- **EX037 — Mosca.** Para os registros dos associados, com *x* = 10 e *y* = 3, para quais valores de *z* a HCU já está atrasada? Rubrica: 3 = *z* < 13, com raciocínio.
- **EX038 — PQC ou QKD.** Dê dois motivos pelos quais a HCU deve priorizar a PQC em vez da QKD nos enlaces das agências. Rubrica: 3 = motivos de infraestrutura e de autenticação/orientações.

### Síntese

A segurança quântica e pós-quântica pergunta o que os computadores quânticos quebram, o que os substitui e como migrar. A desigualdade de Mosca, variada sobre cronogramas incertos, ordena os dados; as FIPS 203/204/205 fornecem os substitutos.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 40

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Segurança quântica e pós-quântica: casos fundamentais

### Objetivos de aprendizagem

Você vai (1) resumir os casos públicos que moldaram a prática pós-quântica; (2) explicar o que cada caso ensina sobre evidências e hipóteses; (3) relacionar os casos com a implantação híbrida; e (4) aplicar as suas lições às decisões da HCU.

### 20.1 O Shor e as estimativas de recursos

O algoritmo de Shor de 1994 (versão em periódico de 1997) mostrou que a fatoração e os logaritmos discretos são resolvíveis de forma eficiente num computador quântico. Por décadas, a questão foram os recursos. Gidney e Ekerå (2021) estimaram 20 milhões de qubits ruidosos funcionando por oito horas para fatorar o RSA-2048; Gidney (2025) baixou isso para menos de um milhão de qubits ruidosos em menos de uma semana, sob hipóteses declaradas sobre as taxas de erro e a conectividade. A lição: as estimativas de recursos caem à medida que os algoritmos e a correção de erros melhoram, então os planos não podem depender de que a estimativa de hoje permaneça fixa.

O plano da HCU usa, portanto, uma faixa de datas de chegada, e não um único número.

### 20.2 Candidatos quebrados

O processo do NIST eliminou candidatos publicamente. O Rainbow, uma assinatura multivariada, foi quebrado por Beullens (2022) com um ataque de recuperação de chave que rodava "num fim de semana num laptop". O SIKE, um KEM baseado em isogenias, foi quebrado por Castryck e Decru (2022) com um ataque clássico. Os dois haviam sobrevivido a anos de análise. A lição: os esquemas novos carregam o risco de quebras clássicas, o que é um argumento central para a implantação híbrida — combinar um algoritmo pós-quântico e um tradicional, para que um atacante precise quebrar os dois.

Nenhuma das quebras precisou de um computador quântico.

### 20.3 Falhas de implementação

O KyberSlash (Bernstein et al., 2024) mostrou que várias implementações do Kyber vazavam informações secretas pelo tempo das operações de divisão, embora a matemática fosse sólida. A lição: uma norma correta não é uma implementação correta; use bibliotecas verificadas e mantenha-as atualizadas.

Para a HCU, a lição virou uma pergunta de compras: qual biblioteca e qual versão cada equipamento usa, e com que rapidez o fornecedor entrega as correções? Um fornecedor que não consegue responder é um risco, qualquer que seja o algoritmo que ele alega suportar.

### 20.4 Implantação inicial

A equipe do Chrome, do Google, anunciou em 2023 a troca de chaves híbrida pós-quântica ([Chromium Blog](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)), e alguns servidores e middleboxes falharam diante do ClientHello maior. A lição: a implantação expõe bugs do ecossistema que nenhuma revisão de especificação encontra; a implantação em estágios e o monitoramento são essenciais.

A maioria das falhas veio de software que supunha que as mensagens de handshake continuariam pequenas. Os navegadores implantaram gradualmente, mediram as falhas e trabalharam com os operadores de servidores para corrigi-las. A HCU segue o mesmo padrão em escala menor, com as suas agências piloto.

### 20.5 Exemplo resolvido

O fornecedor da HCU propõe ativar imediatamente o ML-KEM puro nas VPNs das agências. Aplicando os casos: o SIKE mostra que um esquema novo pode falhar de repente, então um híbrido com ECDH é o projeto de transição prudente; o KyberSlash mostra que a versão da implementação do fornecedor importa, então a HCU pergunta qual biblioteca e qual versão o equipamento usa; a experiência do Chrome mostra que uma agência com um dispositivo legado pode quebrar, então a HCU começa com três agências piloto.

Cada agência piloto é monitorada quanto a fallbacks e falhas de handshake antes que qualquer implantação mais ampla seja aprovada.

### 20.6 Atividade prática

Escreva um cartão de lição de meia página para um dos quatro casos: o que aconteceu, a fonte primária, o que ele mudou na prática e uma pergunta que ele levanta para a HCU.

Um bom cartão é curto o bastante para ser lido em um minuto e aponta para a fonte primária, e não para um resumo dela. A mudança prática deve ser específica, como a passagem para projetos híbridos ou testes de tempo mais rigorosos. A sua pergunta para a HCU deve ser uma que a equipe realmente consiga responder, por exemplo quais produtos dos seus fornecedores ainda usam uma versão vulnerável de biblioteca.

### 20.7 Erros comuns e limites

- Concluir a partir do SIKE que toda a PQC é frágil; o ML-KEM se apoia numa família de problemas diferente e bem estudada.
- Tratar as estimativas de recursos como previsões de datas.
- Supor que uma norma final implica implementações seguras.

O SIKE e o Rainbow foram quebrados pelas suas próprias estruturas; os problemas de reticulados do ML-KEM têm uma longa história de pesquisa e resistiram à análise. Isso é evidência, e não demonstração, e é por isso que se usam híbridos durante a transição. As estimativas de recursos mostram do que um algoritmo precisaria, e não quando alguém vai construí-lo. As implementações precisam de revisão e testes próprios, como o KyberSlash mostrou para um projeto sólido.

### Exercícios

- **EX039 — Do caso ao controle.** Associe cada um dos quatro casos a um controle que a HCU deveria adotar. Rubrica: 3 = quatro associações plausíveis e distintas.
- **EX040 — Tendência das estimativas.** Explique por que a queda das estimativas de recursos deve mudar o planejamento de *y* (tempo de migração) na desigualdade de Mosca, e não apenas o de *z*. Rubrica: 3 = defende começar mais cedo e construir agilidade.

### Síntese

A queda das estimativas de recursos, os candidatos quebrados, as falhas de implementação e os bugs de implantação ensinam, cada um, um controle: planejar para a incerteza, implantar híbridos, usar bibliotecas verificadas e implantar em estágios.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 40

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 (inglês) →](../../en/book/MANUSCRIPT.md#ch-21)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre a HCU são sintéticos. Esta edição parcial traz as resoluções de EX001–EX040; as de EX041–EX080 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

**EX001.** log₂(10^24) = 24 × 3,32 ≈ 79,7 → cerca de 80 bits; acrescentar 2^20 dá cerca de 100 bits.

**EX002.** Base: *n* = 1 exige uma avaliação, h₁ = H(s). Passo: se h_k exige *k* avaliações, h_{k+1} = H(h_k) exige exatamente mais uma, *k* + 1. Conclusão: por indução, h_n exige *n* avaliações para todo *n* ≥ 1.

**EX003.** Hardware: o chip do cartão e o teclado de PIN cifrador do caixa eletrônico guardam chaves (fornecedor/emissor do cartão). Firmware: o software assinado do caixa eletrônico, verificado no boot (fornecedor do caixa eletrônico). Sistema operacional/biblioteca: TLS ou IPsec do caixa eletrônico até o switch (equipe de rede da HCU/fornecedor). Aplicação: o MAC da mensagem de autorização e a verificação da resposta do host (operador do switch de pagamentos).

**EX004.** A vantagem quântica existe apenas para problemas estruturados específicos, como a busca de períodos e a busca não estruturada. O processamento em lote dos extratos é um processamento de dados comum — ler, formatar e gravar registros —, dominado por E/S e aritmética simples. Nenhum algoritmo quântico conhecido oferece uma aceleração significativa, e o hardware quântico atual seria muito mais lento.

**EX005.** `str(b"abc")` produz o texto de seis caracteres `b'abc'`, cujos bytes UTF-8 diferem dos três bytes `abc`, então os resumos diferem. Classe do bug: confusão de tipos entre texto e bytes (erro de codificação), que quebra a interoperabilidade em silêncio.

**EX006.** `def h(b): return hashlib.sha3_256(b).hexdigest()` com `assert h(b"") == "a7ffc6f8…8434a"`. O teste falha se a função calcular o hash de texto, usar SHA-256 no lugar ou truncar.

**EX007.** A: "A autoridade certificadora interna da HCU está exposta à futura falsificação de assinaturas." E: "O seu certificado raiz, exportado em (data), usa RSA-2048 com validade até 2044." R: "Um computador quântico criptograficamente relevante poderia derivar a chave privada RSA com o algoritmo de Shor e emitir certificados confiáveis, e a validade da raiz vai além das datas de chegada plausíveis, então o planejamento da migração deve começar agora."

**EX008.** "A FIPS 206, que vai especificar o FN-DSA (derivado do Falcon), ainda estava em desenvolvimento em 12 de outubro de 2026; ela ainda não impõe nenhuma exigência. As normas finais de assinatura do NIST são a FIPS 204 (ML-DSA) e a FIPS 205 (SLH-DSA)."

**EX009.** Tráfego de VPN arquivado: HNDL (gravado agora, decifrado depois). Assinatura de firmware dos caixas eletrônicos: falsificação posterior (atualizações falsificadas precisam de um CRQC no momento do ataque, mas os dispositivos têm vida longa). Cifração AES-256 do banco de dados: nenhum (adequada diante do Grover). Sessão TLS com o aplicativo móvel: HNDL se os dados da sessão continuarem sensíveis além de *z*; também falsificação posterior para o seu certificado.

**EX010.** Ativo: a raiz da AC interna da HCU e os certificados emitidos. Ameaça: um adversário futuro com um CRQC. Vulnerabilidade: a chave raiz RSA-2048. Impacto: certificados falsificados para serviços internos e VPNs, permitindo a personificação. Probabilidade: baixa hoje, crescendo com o progresso quântico; a validade da raiz até 2044 se sobrepõe às chegadas plausíveis. Controles: planejar uma raiz pós-quântica (ML-DSA), encurtar a validade, distribuir cedo a nova raiz às partes confiantes, inventariar os dependentes.

**EX011.** 3¹ = 3, 3² = 2, 3³ = 6, 3⁴ = 4, 3⁵ = 5, 3⁶ = 1 (mod 7): ordem 6.

**EX012.** (2 + *x*)(3 + *x*³) = 6 + 3*x* + 2*x*³ + *x*⁴ = 6 + 3*x* + 2*x*³ − 1 = 5 + 3*x* + 2*x*³ → [5, 3, 0, 2].

**EX013.** TLS 1.3: troca de chaves (EC)DHE; assinaturas de certificado (RSA/ECDSA) com CertificateVerify. IKEv2: Diffie–Hellman (muitas vezes grupos ECP); certificados ou chaves pré-compartilhadas com assinaturas/MACs. SSH: troca de chaves ECDH/curve25519; assinaturas da chave do host (Ed25519, ECDSA, RSA) e chaves de usuário.

**EX014.** 1.216 − 32 = 1.184 bytes a mais (a chave de encapsulamento ML-KEM-768, FIPS 203; tamanhos dos compartilhamentos conforme o RFC 10024).

**EX015.** Rejeitar: 1.951 bytes (curta); 1.953 bytes (longa); uma chave ML-DSA-44 (1.312 bytes) apresentada como ML-DSA-65; uma chave com identificador de algoritmo/envelope de codificação errado; entrada vazia. Quaisquer quatro casos distintos.

**EX016.** Contar campos vazios como clássicos faz o inventário parecer mais completo e mais uniformemente clássico do que é, escondendo os ativos cuja criptografia ninguém conhece. Os tomadores de decisão então subfinanciam a investigação dos itens desconhecidos, que muitas vezes incluem os dispositivos mais difíceis.

**EX017.** `SELECT name FROM data_class WHERE confidentiality_years > 10 AND transfer_channel IN ('vpn-ecdh', 'tls-ecdhe', 'rsa-kex');`

**EX018.** Autorizações de cartão: retenção de ~7 anos (disputas), confidencialidade de ~2–3 anos (até a expiração do cartão). Arquivos de financiamento imobiliário: retenção de ~30 anos, confidencialidade de ~30 anos ou mais (dados financeiros pessoais). A diferença existe porque o dano da divulgação termina quando as credenciais expiram, no caso dos cartões, mas não no caso dos dados de histórico de vida.

**EX019.** Faltam: quais sistemas; quais técnicas (passivas/ativas); a janela de tempo; o tratamento dos dados; os contatos e as condições de parada. Quaisquer três.

**EX020.** Reproduzir num laboratório isolado; registrar as versões e as evidências; relatar em particular ao contato de segurança do fornecedor; combinar um prazo de divulgação (por exemplo, 90 dias); informar o escritório de segurança da HCU e aplicar mitigações (monitoramento do fallback); publicar um alerta em conjunto após uma correção ou o prazo.

**EX021.** Ela ignora o provedor do sistema operacional, então as atualizações do sistema operacional e as políticas criptográficas do sistema não a mudam; o seu fornecedor ou desenvolvedor é responsável pela mudança; ela precisa ser testada e lançada separadamente, e a sua versão precisa constar do inventário.

**EX022.** O firmware é assinado raramente, por um signatário controlado que pode manter o estado num HSM, e a verificação só precisa de um código pequeno. Um servidor web assina constantemente, pode rodar em muitas réplicas e ser restaurado a partir de backups, então a reutilização do estado — fatal para o LMS/XMSS — se torna provável.

**EX023.** 2^−30 ≈ 9,31 × 10^−10; × 10^12 ≈ 931 falhas.

**EX024.** Tentativas verdadeiras: 10^8/10^6 = 100, detectadas ≈ 99. Alertas falsos: 1% de ~10^8 ≈ 10^6. Fração verdadeira ≈ 99/1.000.099 ≈ 0,01%.

**EX025.** Senhas: não diretamente (armazenamento simétrico/por hash; adequado diante do Grover). Passkeys: sim, assinaturas ECDSA (falsificação posterior). Tokens de SSO: sim, assinaturas RSA/ECDSA, mas de vida curta, prioridade menor. AC raiz interna: sim, chave de assinatura de vida longa, prioridade alta.

**EX026.** Os verificadores constroem cadeias até uma raiz confiável. Uma folha pós-quântica assinada por uma intermediária pós-quântica se encadeia a uma raiz pós-quântica; se as partes confiantes não confiam nessa raiz, a validação falha, então a raiz precisa ser distribuída primeiro aos repositórios de confiança.

**EX027.** As informações de saúde nos casos de dificuldade financeira e os documentos de identidade; os dois continuam danosos por toda a vida. O tráfego gravado que os leva pode ser decifrado depois que a HCU apaga a sua cópia, então a exposição ao HNDL é determinada pelo tempo de vida do dano, e não pela retenção.

**EX028.** Necessários: identificador do host/serviço, protocolo, grupos oferecidos e selecionado, algoritmo de assinatura, validade do certificado, data da observação, método. Não coletados: payloads; endereços IP dos clientes associados (ou apenas truncados); identificadores de sessão.

**EX029.** "A revisão de configuração do inventário de certificados da HCU (1.240 certificados do banco de dados da AC, 15 de março) mostra 95% emitidos por ACs cujo software suporta a emissão ML-DSA; os certificados de ACs externas (fora do banco de dados) estão excluídos."

**EX030.** Indicador: tempo mediano entre a aprovação de uma mudança de algoritmo e a produção, para uma classe de serviços. Medir a partir dos chamados de mudança (registros de data da aprovação à implantação) para mudanças de teste, como ativar um grupo novo. Limitação: as mudanças de teste podem ser mais fáceis que as reais; amostras pequenas.

**EX031.** 1) Agência → data center (WAN, fronteira não confiável, dados de 30 anos, ECDH). 2) Envelopamento das chaves do sistema bancário central → arquivo (RSA-OAEP, chaves de vida longa; expostas se copiadas). 3) Gateway → sistema central (interno, clássico; menor probabilidade de interceptação). 4) Aplicativo móvel → gateway (já híbrido; a autenticação continua clássica).

**EX032.** Configuração central da política criptográfica; identificadores de algoritmo guardados com os textos cifrados/chaves; bibliotecas/provedores que suportam vários KEMs por trás de uma única interface; formatos de mensagem com campos de comprimento que toleram chaves maiores; testes executáveis para qualquer algoritmo configurado.

**EX033.** Armazenamento de senhas: função de hash de senhas (por exemplo, PBKDF2 ou uma função que exige muita memória). Integridade entre servidores: HMAC-SHA-256. Acordo de chave de sessão: X25519MLKEM768 híbrido (FIPS 203 + RFC 10024). Aprovação de documentos: ML-DSA-65 (FIPS 204) ou híbrido com ECDSA durante a transição.

**EX034.** Cada assinatura revela um segredo por posição de bit. Os hashes de duas mensagens diferentes diferem em ~metade das posições, revelando ali os dois segredos (118/256 no Laboratório L). Um atacante pode assinar qualquer mensagem nova cujos bits de hash nas 138 posições restantes coincidam com o que foi revelado, o que exige cerca de 2^138 tentativas de hash; cada reutilização adicional reduz aproximadamente à metade as posições não coincidentes, então, depois de algumas reutilizações, as falsificações se tornam fáceis.

**EX035.** "Que parcela dos 25 fornecedores críticos da HCU publicou um roteiro de PQC com datas para a troca de chaves híbrida, medida pela revisão dos seus documentos públicos e das respostas aos questionários até 30 de junho?"

**EX036.** Interna: a deriva das condições do laboratório ao longo do tempo (mitigada pela alternância da ordem) ou efeitos de cache. Externa: a perda e a latência emuladas não reproduzem os proxies reais das agências nem as condições de rádio.

**EX037.** Atrasada quando *x* + *y* > *z*: 13 > *z*, então para *z* < 13 anos.

**EX038.** A PQC roda nas redes e nos dispositivos existentes, enquanto a QKD precisa de enlaces ópticos dedicados e de nós confiáveis em 40 agências; a QKD ainda exige autenticação clássica e não é apoiada pelas orientações da NSA para os sistemas de segurança nacional, enquanto a PQC está padronizada nas FIPS 203/204/205.

**EX039.** Queda das estimativas → planejar com cronogramas variados e começar cedo. Rainbow/SIKE → implantação híbrida. KyberSlash → bibliotecas verificadas e atualizadas e acompanhamento das versões. Implantação do Chrome → implantação em estágios com monitoramento.

**EX040.** Se *z* puder ser menor que o esperado, a única variável que a HCU controla é *y*. Começar mais cedo e construir agilidade reduz *y* nesta migração e nas futuras, mantendo *x* + *y* abaixo de uma faixa mais ampla de *z*.

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
- IETF RFCs: 8446 (TLS 1.3), 8784 (IKEv2 PSK mixing), 8879 (certificate compression), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025); SP 800-56C Rev. 2. <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227> · <https://doi.org/10.6028/NIST.SP.800-56Cr2>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- NSA. Quantum Key Distribution (QKD) and Quantum Cryptography (QC). <https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/>
- Regev, O. (2009). On lattices, learning with errors, random linear codes, and cryptography. *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
