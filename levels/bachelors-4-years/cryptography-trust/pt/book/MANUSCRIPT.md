# Criptografia e Serviços de Confiança: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 100, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 40 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–40 (EX031–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de bacharelado que aprendem criptografia desde os fundamentos matemáticos até a operação de serviços de confiança numa organização real.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios ilustram conceitos (XOR, cifras clássicas, hash com salt, cadeias de hashes) sobre dados sintéticos; as cifras de brinquedo aparecem apenas para explicar por que falham. Sistemas de produção usam bibliotecas avaliadas; nunca crie sua própria criptografia. Pessoas, organizações e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante ao longo de quatro anos enquanto ela ajuda um consórcio de bibliotecas públicas a proteger os dados dos leitores: fundamentos de matemática, sistemas e programação; letramento em segurança, estruturas discretas, protocolos, bancos de dados, ética, privacidade e evidências; depois, serviços de confiança na teoria e na prática, cifração autenticada, assinaturas, verificação, análise de falhas e operações; e, por fim, pesquisa, um projeto comparativo, um inventário de certificados como trabalho de conclusão, oficinas comunitárias e uma tese. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Priya Raman** | Estudante de bacharelado | Inventada |
| **Dr. Tomás Echeverría** | Professor | Inventado |
| **Grace Okafor** | Líder de TI do consórcio | Inventada |
| **Ashford University** | Universidade fictícia | Inventada |
| **Tidewell Public Library Consortium** | Parceiro fictício com doze unidades | Inventado |

### Fontes principais

Katz e Lindell (3ª ed.); Menezes et al., [*Handbook of Applied Cryptography*](https://cacr.uwaterloo.ca/hac/); Boneh e Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4); [SP 800-38D](https://doi.org/10.6028/NIST.SP.800-38D); [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) raciocinar com precisão sobre definições e afirmações em criptografia; (2) usar a operação XOR e suas propriedades algébricas; (3) provar por que reutilizar a chave de um one-time pad falha.

### 1.1 O caso e as afirmações precisas

Priya Raman é estudante do primeiro ano de bacharelado na fictícia Ashford University. Ao longo de quatro anos, ela vai trabalhar com o fictício Tidewell Public Library Consortium, doze bibliotecas que compartilham um portal de leitores, um serviço de e-books e sistemas internos, orientada pelo professor Dr. Tomás Echeverría e pela líder de TI do consórcio, Grace Okafor. Todos os leitores, chaves e números aqui são sintéticos. Sua primeira lição é que a criptografia é uma disciplina matemática: uma afirmação como "esta cifra é segura" não significa nada até que a segurança seja definida, o atacante seja descrito e a afirmação seja provada ou reduzida a uma premissa bem estudada, como insistem Katz e Lindell.

### 1.2 O XOR e sua álgebra

O ou exclusivo, escrito XOR, compara dois bits e devolve 1 quando eles diferem. Ele tem propriedades que Priya prova a partir da tabela-verdade: x XOR x = 0, x XOR 0 = x, e o XOR é associativo e comutativo. Isso torna o XOR reversível: se c = p XOR k, então c XOR k = p. O one-time pad cifra fazendo o XOR de uma mensagem com uma chave verdadeiramente aleatória do mesmo tamanho, usada uma única vez, e Shannon provou que ele tem sigilo perfeito nessas condições. Provar com cuidado pequenos fatos algébricos é um treino para ler as provas das disciplinas posteriores.

### Laboratório — Reutilização do one-time pad

```python
"""Why a one-time pad must never be reused: XOR of two ciphertexts cancels the key (toy data)."""
import secrets
def xor(a, b): return bytes(x ^ y for x, y in zip(a, b))

def main():
    p1, p2 = b"RENEW BOOK 0417", b"FINE PAID  0938"
    key = bytes.fromhex("8f1e2a77c03b5d9e4412ab6f0e7c31")  # fixed demo pad, used twice on purpose
    c1, c2 = xor(p1, key), xor(p2, key)
    print("c1 xor c2 == p1 xor p2:", xor(c1, c2) == xor(p1, p2))
    guess = xor(xor(c1, c2), b"RENEW BOOK 0417")
    print("knowing p1 reveals p2:", guess.decode())
    fresh = secrets.token_bytes(len(p1))
    print("fresh pad length matches message:", len(fresh) == len(p1))

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_xor.py`. Saída verificada:

```text
c1 xor c2 == p1 xor p2: True
knowing p1 reveals p2: FINE PAID  0938
fresh pad length matches message: True
```

### 1.3 Por que a reutilização falha

O laboratório cifra de propósito duas mensagens de leitores com o mesmo pad. Fazer o XOR dos dois textos cifrados cancela a chave, já que (p1 XOR k) XOR (p2 XOR k) = p1 XOR p2, o que o laboratório confirma como True. Se um atacante conhece ou adivinha uma das mensagens, como um aviso padrão "RENEW BOOK", a outra aparece em claro: FINE PAID 0938. A prova cabe em três linhas, e a lição dura uma carreira: um esquema perfeito nas suas condições pode falhar completamente quando uma condição, aqui "usar uma vez", é violada. O pad novo, gerado com o módulo secrets, mostra como as chaves devem ser geradas, embora os sistemas reais usem cifras padronizadas em vez de pads.

### Exemplo resolvido

Priya prova x XOR x = 0 a partir da tabela-verdade, deduz c1 XOR c2 = p1 XOR p2 e usa o laboratório para recuperar uma segunda mensagem a partir de uma primeira mensagem conhecida quando um pad é reutilizado.

> **Caso sintético.** A Tidewell, seus leitores e suas mensagens são inventados.

### Erros e limites

O sigilo perfeito só vale para chaves verdadeiramente aleatórias, nunca reutilizadas e do tamanho da mensagem; sistemas práticos usam AES-GCM ou algo semelhante, de bibliotecas avaliadas, e não pads. Demonstrações de brinquedo não são projetos.

### Exercícios

- **EX001 — Definir seguro.** Por que "esta cifra é segura" não significa nada por si só? *Rubrica:* 3 = a segurança precisa ser definida com um modelo de atacante e provada ou reduzida a uma premissa;; 2 = precisa de definição;; 1 = tem significado;; 0 = nenhuma.

- **EX002 — Identidades do XOR.** Enuncie duas identidades do XOR que fazem a decifração funcionar. *Rubrica:* 3 = x XOR x = 0 e x XOR 0 = x (com a associatividade);; 2 = uma;; 1 = errada;; 0 = nenhuma.

- **EX003 — Resultado da reutilização do pad.** O que o laboratório recuperou, e por quê? *Rubrica:* 3 = FINE PAID 0938, porque c1 XOR c2 = p1 XOR p2 e p1 era conhecida;; 2 = a mensagem;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever onde a criptografia fica num sistema computacional; (2) explicar os dados em repouso, em trânsito e em uso; (3) identificar qual componente protege cada um.

### 2.1 Camadas de um sistema

Priya mapeia os sistemas da Tidewell em camadas: o hardware dos servidores das unidades e dos notebooks dos leitores, os sistemas operacionais, aplicações como o catálogo e o portal dos leitores, as redes que ligam as unidades e os serviços em nuvem que hospedam os e-books. A criptografia aparece em várias camadas: cifração de disco no sistema operacional, TLS nas bibliotecas de rede, hash de senhas na aplicação do portal e assinaturas nas atualizações de software. Ela aprende que uma proteção numa camada não cobre as outras; cifrar um disco não faz nada pelos dados que trafegam entre as unidades, e o TLS não faz nada pelo disco de um notebook roubado.

### 2.2 Três estados dos dados

Os dados existem em três estados. Em repouso, ficam em discos e backups; a cifração de disco completo e a cifração do banco de dados os protegem contra o roubo das mídias. Em trânsito, movem-se pelas redes; o TLS os protege contra escuta e adulteração. Em uso, estão sendo processados na memória, onde costumam estar decifrados e são protegidos principalmente pelo controle de acesso e pelo isolamento do sistema operacional. Priya classifica os registros de leitores da Tidewell em cada estado e anota que o consórcio cifra os notebooks e usa TLS no portal, mas que as fitas de backup enviadas a um depósito externo não são cifradas.

### 2.3 Combinar as proteções

Priya monta uma tabela que associa cada fluxo de dados à sua proteção e ao seu dono. Os logins dos leitores trafegam por TLS e são armazenados como hashes de senha com salt; o histórico de empréstimos fica num banco de dados cifrado; os backups viajam por mensageiro sem cifração. Ela recomenda cifrar os backups com chaves mantidas pelo consórcio, e não pela empresa de mensageiros, e registra que a perda das chaves tornaria os backups ilegíveis, de modo que as chaves precisam de um backup protegido próprio. Grace Okafor aceita a recomendação e pede a Priya que estime o custo da mudança no software de backup.

### Exemplo resolvido

O mapa de camadas e a tabela de estados dos dados de Priya mostram as fitas de backup não cifradas como uma lacuna, e ela recomenda a cifração dos backups com chaves do consórcio e um backup protegido das chaves.

> **Caso sintético.** Os sistemas da Tidewell são inventados.

### Erros e limites

A cifração em repouso não protege os dados em uso por uma aplicação comprometida. Perder as chaves de cifração destrói os dados tão certamente quanto perder as mídias.

### Exercícios

- **EX004 — Limites das camadas.** Por que a cifração de disco não protege os dados que circulam entre as unidades? *Rubrica:* 3 = ela protege apenas dados em repouso; o trânsito precisa de TLS;; 2 = as camadas diferem;; 1 = protege;; 0 = nenhuma.

- **EX005 — Dados em uso.** O que protege principalmente os dados em uso? *Rubrica:* 3 = controle de acesso e isolamento do sistema operacional, já que os dados estão decifrados na memória;; 2 = controle de acesso;; 1 = cifração;; 0 = nenhuma.

- **EX006 — Lacuna dos backups.** Que lacuna Priya encontrou, e o que ela recomendou? *Rubrica:* 3 = fitas de backup não cifradas; cifrar com chaves do consórcio e fazer backup das chaves;; 2 = lacuna;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) lidar com bytes, codificações e hexadecimal em Python; (2) calcular digests SHA-256 com o hashlib; (3) conferir os resultados contra vetores de teste publicados.

### 3.1 Bytes e codificações

Os primeiros programas de Priya mostram que os computadores armazenam texto como bytes, segundo uma codificação. A string "café" vira cinco bytes em UTF-8, porque o é precisa de dois. As funções criptográficas recebem bytes, então ela sempre escreve text.encode("utf-8") antes de calcular o hash. O hexadecimal exibe os bytes de forma legível, dois caracteres por byte. Ela pratica as conversões com bytes.hex() e bytes.fromhex(). Pequenos erros aqui, como calcular o hash de uma string lida de um arquivo com uma quebra de linha no final, produzem digests totalmente diferentes, o que a ensinou a imprimir os tamanhos e as formas hexadecimais ao depurar.

### 3.2 Hash com o hashlib

O hashlib do Python implementa o SHA-256 do FIPS 180-4. Priya calcula o digest da string vazia e de "abc" e os compara com os exemplos publicados com a norma: o digest de "abc" começa com ba7816bf. Coincidir com um vetor publicado prova que ela está chamando a função corretamente. Ela observa o efeito avalanche: trocar "abc" por "abd" muda cerca de metade dos 256 bits da saída. Ela aprende que os hashes são funções públicas, que qualquer pessoa pode calcular; um hash só prova a integridade quando o digest esperado vem de uma fonte confiável.

### 3.3 Uma ferramenta de integridade de arquivos

Priya escreve um pequeno programa que calcula o digest SHA-256 de cada arquivo de uma pasta e salva uma lista e, mais tarde, recalcula e relata as mudanças. Ela usa para os testes os arquivos sintéticos de exportação do catálogo da Tidewell. Os arquivos grandes são lidos em blocos e passados ao método update do objeto de hash, de modo que o uso de memória fica pequeno. Ela documenta um limite: um atacante que consiga modificar tanto os arquivos quanto a lista salva pode esconder as mudanças, então a lista precisa ficar guardada num lugar protegido ou ser assinada. Isso antecipa as assinaturas digitais, que aparecem mais adiante no curso.

### Exemplo resolvido

Priya confirma suas chamadas ao SHA-256 contra o exemplo "abc" do FIPS 180-4, constrói um verificador de integridade de arquivos que lê em blocos e registra que a própria lista de digests precisa de proteção.

> **Caso sintético.** Os arquivos do catálogo são inventados; o FIPS 180-4 é real.

### Erros e limites

Hashes não escondem dados e não autenticam por si sós. Erros de codificação são a causa mais comum de digests que não coincidem.

### Exercícios

- **EX007 — Tamanho em UTF-8.** Por que "café" tem cinco bytes em UTF-8? *Rubrica:* 3 = o é ocupa dois bytes;; 2 = codificação;; 1 = quatro;; 0 = nenhuma.

- **EX008 — Conferência do vetor de teste.** Como Priya confirmou que usou o SHA-256 corretamente? *Rubrica:* 3 = coincidiu com o digest do exemplo "abc" do FIPS 180-4, que começa com ba7816bf;; 2 = vetor coincidiu;; 1 = adivinhou;; 0 = nenhuma.

- **EX009 — Limite da ferramenta de integridade.** Que limite o verificador de integridade tem? *Rubrica:* 3 = um atacante que modifica os arquivos e a lista de digests esconde as mudanças; a lista precisa ser protegida ou assinada;; 2 = proteger a lista;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) escrever explicações claras de ideias criptográficas; (2) citar normas e livros-texto corretamente; (3) evitar exageros na escrita sobre segurança.

### 4.1 Explicar com clareza

O primeiro ensaio de Priya explica a um leitor leigo por que as senhas não devem ser armazenadas em texto claro. Ela usa um exemplo concreto, um banco de dados roubado que expõe a senha de todos os leitores, e depois explica o hash com salt em palavras simples, antes de introduzir os termos. O Dr. Echeverría tira pontos de um parágrafo que usava "hash", "salt" e "derivação de chave" sem defini-los. Ela aprende a definir cada termo uma vez, usá-lo de forma consistente e preferir frases curtas. Escrever com clareza não é simplificar; é uma precisão que os leitores conseguem acompanhar.

### 4.2 Citar corretamente

Para as afirmações criptográficas, Priya cita fontes primárias: o FIPS 180-4 para o SHA-256, a RFC 9106 para o Argon2, Katz e Lindell para as definições e o Handbook of Applied Cryptography de Menezes e colegas para o contexto clássico. Ela cita o documento e a seção exatos sempre que possível e confere se cada link funciona. Ela evita citar posts de blog para fatos que as normas enunciam e nunca inventa uma referência ou um identificador. Quando uma fonte é um rascunho, como o livro-texto online de Boneh e Shoup, ela anota a versão que leu.

### 4.3 Evitar exageros

A escrita sobre segurança costuma exagerar: "inquebrável", "completamente seguro" ou "hackers não conseguem". Priya reescreve essas expressões com afirmações precisas: "O Argon2id torna cada palpite de senha custoso em tempo e memória, desacelerando a adivinhação offline." Ela também declara o que a medida não faz: ela não protege senhas fracas como "library1" contra uma adivinhação determinada. O Dr. Echeverría diz à turma que limites cuidadosos tornam a escrita mais persuasiva para leitores especialistas e protegem os autores quando as afirmações são testadas. Ela mantém ao lado da mesa uma lista de expressões proibidas como lembrete.

### Exemplo resolvido

O ensaio de Priya define os termos uma vez, cita o FIPS 180-4 e a RFC 9106 e substitui "inquebrável" por uma afirmação precisa com o limite declarado.

> **Caso sintético.** O ensaio é inventado; as normas citadas são reais.

### Erros e limites

Citações de fontes secundárias podem carregar erros; confira o documento primário. Uma linguagem precisa ainda precisa de uma base técnica correta.

### Exercícios

- **EX010 — Definir os termos.** O que o Dr. Echeverría penalizou, e por quê? *Rubrica:* 3 = termos como hash e salt usados sem definição;; 2 = jargão indefinido;; 1 = estilo;; 0 = nenhuma.

- **EX011 — Fontes primárias.** Que fontes primárias Priya citou para o SHA-256 e o Argon2? *Rubrica:* 3 = FIPS 180-4 e RFC 9106;; 2 = uma;; 1 = blog;; 0 = nenhuma.

- **EX012 — Reescrita precisa.** Reescreva com precisão "o Argon2 torna as senhas inquebráveis". *Rubrica:* 3 = o Argon2id torna cada palpite custoso em tempo e memória, desacelerando a adivinhação offline; senhas fracas continuam em risco;; 2 = parcial;; 1 = inalterada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) reconhecer os objetivos a que a criptografia serve; (2) distinguir cifração, hash, MACs e assinaturas; (3) identificar equívocos comuns.

### 5.1 Para que serve a criptografia

Priya lista os objetivos a que a criptografia serve: confidencialidade, manter os dados em segredo; integridade, detectar mudanças; autenticação, confirmar quem enviou algo; e irretratabilidade (não repúdio), impedir que um signatário negue uma assinatura. Ela associa exemplos da Tidewell: o histórico de leitura dos leitores precisa de confidencialidade, as exportações do catálogo precisam de integridade, os logins da equipe precisam de autenticação e os contratos assinados com editoras de e-books se beneficiam da irretratabilidade. Cada objetivo precisa de ferramentas diferentes, e confundi-los é a raiz de muitos erros que ela vai encontrar depois. Ela fixa os quatro objetivos acima de cada discussão de projeto posterior, para que cada ferramenta proposta precise nomear o objetivo a que serve.

### 5.2 Quatro ferramentas

A cifração oferece confidencialidade com uma chave; o AES do FIPS 197 é a cifra simétrica padrão. As funções de hash, como o SHA-256, oferecem uma impressão digital de tamanho fixo, sem chave. Os códigos de autenticação de mensagem, como o HMAC da RFC 2104, oferecem integridade e autenticação entre partes que compartilham uma chave. As assinaturas digitais, como o ECDSA do FIPS 186-5 ou o Ed25519 da RFC 8032, oferecem integridade, autenticação e irretratabilidade, usando uma chave privada para assinar e uma chave pública para verificar. Priya desenha uma tabela de qual ferramenta atende a qual objetivo.

### 5.3 Equívocos comuns

Priya coleta equívocos em entrevistas com a equipe da Tidewell: "o site tem um cadeado, então nossos dados estão seguros em toda parte"; "calculamos o hash dos backups, então eles estão cifrados"; "uma senha mais longa é sempre uma senha mais forte"; e "cifração significa que ninguém pode alterar os dados". Ela corrige cada um: o TLS protege apenas a conexão; hash não é cifração; o comprimento só ajuda se a senha não for previsível; e a cifração não autenticada pode permitir adulterações não detectadas, e é por isso que se prefere a cifração autenticada, como o AES-GCM.

### Exemplo resolvido

Priya associa os quatro objetivos a exemplos da Tidewell, monta uma tabela de ferramentas e objetivos e corrige quatro equívocos da equipe.

> **Caso sintético.** As falas da equipe são inventadas.

### Erros e limites

Tabelas simplificadas omitem nuances, como a cifração autenticada, que combina objetivos. A irretratabilidade também depende da proteção das chaves e do contexto jurídico.

### Exercícios

- **EX013 — Associar objetivos.** A que objetivo servem os contratos assinados com as editoras? *Rubrica:* 3 = irretratabilidade (além de integridade e autenticação);; 2 = integridade;; 1 = confidencialidade;; 0 = nenhuma.

- **EX014 — MAC versus assinatura.** Em que um MAC difere de uma assinatura? *Rubrica:* 3 = o MAC usa uma chave compartilhada, sem irretratabilidade; a assinatura usa chaves privada/pública e sustenta a irretratabilidade;; 2 = parcial;; 1 = iguais;; 0 = nenhuma.

- **EX015 — Equívoco do cadeado.** Corrija "o cadeado significa que nossos dados estão seguros em toda parte". *Rubrica:* 3 = o TLS protege apenas a conexão, não os dados armazenados nos servidores;; 2 = parcial;; 1 = concorda;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) usar aritmética modular e grupos; (2) explicar o problema do logaritmo discreto; (3) relacioná-lo ao acordo de chaves Diffie-Hellman.

### 6.1 Aritmética modular e grupos

Priya estuda os inteiros módulo um primo p. A multiplicação módulo p, excluído o zero, forma um grupo: é fechada, associativa, tem um elemento neutro, e todo elemento tem um inverso. Alguns elementos, chamados geradores, produzem todos os elementos não nulos quando elevados a potências sucessivas. Para p = 23 e gerador 5, as potências de 5 módulo 23 percorrem todos os 22 valores não nulos. Essas estruturas, tratadas no capítulo 2 do Handbook of Applied Cryptography, estão na base de muitos sistemas de chave pública e dão um significado preciso a operações que de outra forma pareceriam aritmética arbitrária.

### 6.2 O logaritmo discreto

Calcular 5^x mod 23 é fácil para qualquer x, usando a exponenciação rápida. Ir para trás, encontrar x a partir do resultado, é o problema do logaritmo discreto. Para primos minúsculos, Priya consegue testar todos os valores, mas, para primos de milhares de bits, não se conhece nenhum algoritmo clássico eficiente. Essa assimetria, fácil para a frente e difícil para trás, é o que a criptografia de chave pública precisa. Priya destaca a palavra "conhece": a segurança se apoia na crença de que o problema é difícil, e o algoritmo de Shor o resolveria num computador quântico grande, o que motiva normas pós-quânticas como o FIPS 203.

### 6.3 Diffie-Hellman à mão

Priya resolve uma troca Diffie-Hellman de brinquedo: Alice escolhe o segredo a = 6 e envia 5^6 mod 23 = 8; Bob escolhe b = 15 e envia 5^15 mod 23 = 19. Alice calcula 19^6 mod 23 = 2 e Bob calcula 8^15 mod 23 = 2, um segredo compartilhado que nenhum dos dois enviou. Quem escuta vê 8 e 19, mas precisa resolver um logaritmo discreto. Ela enfatiza que os sistemas reais usam grupos grandes ou curvas elípticas, como o X25519 da RFC 7748, autenticam a troca para deter atacantes ativos e rodam dentro do TLS 1.3, e não como código escrito à mão. Priya repete o cálculo com uma colega para confirmar que os dois lados chegam de fato ao mesmo valor.

### Exemplo resolvido

Priya verifica que 5 gera o grupo módulo 23, calcula um segredo compartilhado de brinquedo igual a 2 num Diffie-Hellman e explica por que as trocas reais usam o X25519 dentro do TLS, com autenticação.

> **Caso sintético.** Apenas números de brinquedo; a RFC 7748 e o FIPS 203 são reais.

### Erros e limites

O Diffie-Hellman não autenticado está aberto a ataques de intermediário (man-in-the-middle). Grupos de brinquedo são trivialmente quebráveis.

### Exercícios

- **EX016 — Propriedades de grupo.** Liste as quatro propriedades de grupo. *Rubrica:* 3 = fechamento, associatividade, elemento neutro, inversos;; 2 = três;; 1 = uma;; 0 = nenhuma.

- **EX017 — Segredo compartilhado de brinquedo.** Que segredo compartilhado a troca de brinquedo produziu, e a partir de quais valores públicos? *Rubrica:* 3 = 2, a partir dos valores públicos 8 e 19;; 2 = só o segredo;; 1 = errado;; 0 = nenhuma.

- **EX018 — Ameaça quântica.** Por que o algoritmo de Shor importa aqui? *Rubrica:* 3 = resolveria logaritmos discretos num computador quântico grande, motivando o FIPS 203;; 2 = quântico;; 1 = nenhum motivo;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar em alto nível o handshake do TLS 1.3; (2) descrever a validação de certificados pelos navegadores; (3) identificar riscos no nível do protocolo, como rebaixamento e má configuração.

### 7.1 O handshake do TLS 1.3

Quando um leitor abre o portal da Tidewell, o navegador e o servidor executam um handshake TLS 1.3 da RFC 8446. O cliente envia os algoritmos suportados e um compartilhamento de chave (key share); o servidor responde com o seu, e os dois derivam as chaves usando o HKDF da RFC 5869. O servidor envia seu certificado e assina a transcrição do handshake para provar que tem a chave privada; depois, os dois confirmam o handshake com códigos de autenticação de mensagem. Todos os dados seguintes são cifrados com uma cifra autenticada, como o AES-GCM. Priya captura o handshake num laboratório com um servidor de teste e identifica cada mensagem.

### 7.2 Validação de certificados

O navegador confere que o certificado do servidor se encadeia até uma raiz em que ele confia, que o nome corresponde a portal.tidewell.example, que está dentro das datas de validade e que não foi revogado. A RFC 5280 define os campos do certificado e a validação do caminho. Se qualquer verificação falhar, o navegador mostra um aviso. Priya explica à equipe da biblioteca por que passar por cima desses avisos é perigoso: o aviso pode ser o único sinal de que alguém no Wi-Fi do café está interceptando a conexão com um certificado forjado.

### 7.3 Riscos do protocolo

As versões mais antigas do TLS permitiam que atacantes empurrassem as conexões para algoritmos mais fracos. O TLS 1.3 remove as opções legadas e protege contra o rebaixamento assinando todo o handshake. A maioria dos problemas práticos vem hoje da configuração: servidores que ainda oferecem TLS 1.0, certificados expirados ou aplicações que desativam a verificação. Priya varre os serviços públicos da Tidewell, com permissão, e descobre que a wiki da equipe ainda aceita TLS 1.0. Ela relata o fato a Grace, que agenda uma mudança de configuração, e registra o escopo e a autorização da varredura nas suas anotações. Ela testa de novo depois da mudança.

### Exemplo resolvido

Priya identifica cada mensagem do handshake do TLS 1.3, explica as verificações de certificado à equipe e relata uma configuração de TLS 1.0 encontrada numa varredura autorizada.

> **Caso sintético.** Os hosts da Tidewell são inventados; a RFC 8446, a RFC 5869 e a RFC 5280 são reais.

### Erros e limites

Varrer sistemas sem permissão é antiético e pode ser ilegal. Um certificado válido mostra quem opera um servidor, e não que o servidor é seguro.

### Exercícios

- **EX019 — Assinatura da transcrição.** Por que o servidor assina a transcrição do handshake? *Rubrica:* 3 = para provar que tem a chave privada do certificado e proteger contra adulteração/rebaixamento;; 2 = provar a chave;; 1 = cifrar;; 0 = nenhuma.

- **EX020 — Verificações do navegador.** Liste três verificações que o navegador faz num certificado. *Rubrica:* 3 = três entre cadeia até raiz confiável, correspondência do nome, datas de validade, revogação;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX021 — Achado da varredura.** O que a varredura autorizada de Priya encontrou? *Rubrica:* 3 = a wiki da equipe aceitando TLS 1.0;; 2 = TLS antigo;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) usar com segurança APIs criptográficas de alto nível; (2) estruturar o código para evitar usos indevidos; (3) escrever testes negativos.

### 8.1 APIs de alto nível

Priya aprende que as bibliotecas criptográficas oferecem primitivas de baixo nível e receitas de alto nível. As APIs de baixo nível exigem escolher modos, nonces e preenchimento, onde é fácil errar. As APIs de alto nível, como uma função de cifração autenticada que gera os nonces e devolve um único token, tornam o uso seguro o padrão. Para a ferramenta de exportação da Tidewell, ela usa a receita de cifração autenticada de uma biblioteca mantida, em vez de montar por conta própria o AES e um modo. A regra do curso é explícita: os estudantes aprendem como as primitivas funcionam, mas o código de produção usa APIs de alto nível avaliadas. Os colegas de equipe concordam em segui-la.

### 8.2 Estruturar com segurança

Priya isola a criptografia num módulo com uma interface pequena: protect(data) e unprotect(token). As chaves são carregadas do cofre de segredos do consórcio, nunca do código-fonte. Os erros em unprotect lançam uma única exceção genérica, para que quem chama não possa saber por que um token falhou. Ela escreve anotações de tipo que marcam os valores secretos e evita registrá-los em log. A revisão de código se concentra nesse módulo, que é pequeno o bastante para ser lido com cuidado. A estrutura faz com que futuras mudanças de algoritmo afetem um arquivo, e não a aplicação inteira.

### 8.3 Testes negativos

Priya escreve testes que devem falhar: tokens adulterados, tokens truncados, tokens protegidos com outra chave e entrada vazia. Cada um precisa ser rejeitado. Ela também testa que duas proteções dos mesmos dados produzem tokens diferentes, confirmando que os nonces são novos. Uma versão anterior de um colega passava em todos os testes positivos, mas devolvia os dados mesmo para tokens adulterados, porque pulava a verificação da tag. Os testes negativos pegaram isso. Ela os acrescenta à integração contínua, para que rodem a cada mudança. Cada teste tem um comentário de uma linha que explica seu propósito.

### Exemplo resolvido

Priya usa uma receita de cifração autenticada de alto nível num pequeno módulo protect/unprotect, carrega as chaves de um cofre de segredos e pega, com testes negativos, uma verificação de tag que era pulada.

> **Caso sintético.** A ferramenta de exportação é inventada.

### Erros e limites

As APIs de alto nível ainda precisam de um gerenciamento de chaves correto. Os testes só provam aquilo que verificam.

### Exercícios

- **EX022 — Vantagem do alto nível.** Por que preferir APIs criptográficas de alto nível? *Rubrica:* 3 = padrões seguros cuidam de nonces, modos e preenchimento, reduzindo o uso indevido;; 2 = mais seguras;; 1 = mais rápidas;; 0 = nenhuma.

- **EX023 — Exceção genérica.** Por que unprotect lança uma única exceção genérica? *Rubrica:* 3 = para que quem chama ou atacantes não saibam por que um token falhou;; 2 = esconder o motivo;; 1 = mais simples;; 0 = nenhuma.

- **EX024 — Teste de nonce novo.** O que proteger os mesmos dados duas vezes testa? *Rubrica:* 3 = os tokens diferem, confirmando nonces novos;; 2 = nonces;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) armazenar senhas com hash lento e com salt; (2) explicar por que os salts e os fatores de trabalho importam; (3) escolher proteções por campo num banco de dados.

### 9.1 Armazenamento de senhas

O portal antigo da Tidewell armazenava as senhas com SHA-256 puro, o que Priya explica ser inseguro: o SHA-256 é rápido, então um atacante com uma tabela roubada pode testar bilhões de palpites por segundo, e senhas idênticas produzem hashes idênticos. Um esquema adequado acrescenta um salt aleatório único por usuário e usa uma função deliberadamente lenta. A RFC 9106 especifica o Argon2id, a escolha preferida; o PBKDF2, disponível no hashlib do Python, é uma alternativa mais antiga que precisa de um número alto de iterações. O laboratório demonstra o uso de salt com o PBKDF2 porque ele está na biblioteca padrão.

### Laboratório — Hash de senhas com salt

```python
"""Salted password hashing with hashlib.pbkdf2_hmac on synthetic passwords (prefer Argon2id, RFC 9106)."""
import hashlib, hmac
def h(pw, salt, n=600_000):
    return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, n).hex()

def main():
    s1, s2 = bytes.fromhex("a1" * 16), bytes.fromhex("b2" * 16)  # fixed demo salts for reproducible output
    a, b = h("correct horse 42", s1), h("correct horse 42", s2)
    print("same password, different salts differ:", a != b)
    print("stored:", a[:24], "...")
    print("login with right password:", hmac.compare_digest(a, h("correct horse 42", s1)))
    print("login with wrong password:", hmac.compare_digest(a, h("correct horse 43", s1)))

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_pbkdf2.py`. Saída verificada:

```text
same password, different salts differ: True
stored: c96866459ba12d6a7bc6285d ...
login with right password: True
login with wrong password: False
```

### 9.2 Ler a execução

A mesma senha com dois salts diferentes produz valores armazenados diferentes, de modo que um atacante não consegue ver quais leitores compartilham uma senha nem usar tabelas pré-calculadas. Entrar com a senha certa recalcula o mesmo valor, e compare_digest devolve True; a mudança de um caractere devolve False. Os salts fixos de demonstração existem apenas para tornar a saída repetível; os salts reais vêm de secrets.token_bytes. As 600.000 iterações desaceleram cada palpite. Priya recomenda migrar para o Argon2id, refazendo o hash de cada senha no próximo login bem-sucedido do leitor.

### 9.3 Escolhas por campo

Além das senhas, Priya classifica os campos do banco de dados: nomes e endereços são cifrados no nível do campo, com chaves do serviço de chaves do consórcio; o histórico de empréstimos com mais de noventa dias é apagado, seguindo o princípio de privacidade de guardar apenas o necessário; e os números dos cartões dos leitores são tokenizados para os sistemas de relatórios. Ela registra que apagar dados antigos costuma ser a proteção mais forte, já que dados que não existem não podem vazar. Grace concorda e agenda a mudança de retenção depois da aprovação do conselho. A política é publicada para os leitores.

### Exemplo resolvido

Priya substitui o SHA-256 puro por um hash lento com salt, planeja a migração para o Argon2id no próximo login, cifra os campos pessoais e apaga o histórico de empréstimos depois de noventa dias.

> **Caso sintético.** O banco de dados da Tidewell é inventado; a RFC 9106 é real.

### Erros e limites

O hash lento não salva senhas muito fracas. Chaves de cifração guardadas ao lado do banco de dados oferecem pouca proteção.

### Exercícios

- **EX025 — Por que o SHA-256 falha.** Por que o SHA-256 puro é inseguro para senhas? *Rubrica:* 3 = é rápido, permitindo bilhões de palpites, e senhas idênticas dão hashes idênticos;; 2 = rápido;; 1 = está bom;; 0 = nenhuma.

- **EX026 — Efeito do salt.** O que o laboratório mostrou sobre os salts? *Rubrica:* 3 = a mesma senha com salts diferentes dá valores armazenados diferentes;; 2 = diferem;; 1 = iguais;; 0 = nenhuma.

- **EX027 — Proteção mais forte.** O que Priya diz ser, muitas vezes, a proteção mais forte? *Rubrica:* 3 = apagar os dados que não são necessários;; 2 = apagar;; 1 = cifração;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) aplicar regras éticas aos testes criptográficos; (2) obter e documentar a autorização; (3) tratar com responsabilidade as fraquezas descobertas.

### 10.1 Autorização primeiro

Priya aprende que testar a criptografia de um sistema, por exemplo varrendo as configurações de TLS ou tentando quebrar hashes de senha, exige autorização por escrito do dono. Antes da varredura do Capítulo 7, Grace assinou um escopo que listava os hosts, as datas e as ferramentas permitidas. Testar fora do escopo, mesmo com boas intenções, pode violar leis e a confiança. O Dr. Echeverría diz à turma que o mesmo ato técnico pode ser pesquisa legítima ou crime, conforme a autorização, e é por isso que os profissionais a documentam todas as vezes. Priya guarda uma cópia com suas anotações.

### 10.2 Lidar com material sensível

Durante um exercício de aula sobre a força das senhas, o grupo de Priya recebe um arquivo sintético de hashes de senhas criado pelo professor. Eles são lembrados de nunca usar bancos de dados reais de senhas vazadas, que contêm segredos de pessoas reais, mesmo que estejam publicamente disponíveis. Os resultados são discutidos apenas de forma agregada. Priya aprende a tratar chaves, hashes e dados pessoais como materiais perigosos: minimizar as cópias, armazená-las cifradas, apagá-las ao terminar e registrar quem teve acesso. Os membros do grupo assinam um breve acordo de manuseio no início do exercício, e o professor apaga o arquivo no fim do semestre.

### 10.3 Divulgação responsável

Mais tarde, usando um aplicativo público de e-books fora das atividades do curso, Priya percebe que ele envia os dados de login por HTTP sem cifração. Ela não testa mais nada. Ela relata o problema ao contato de segurança do fornecedor, com uma descrição curta e um prazo de divulgação de noventa dias, seguindo a prática de divulgação coordenada que seu curso ensina, e informa o Dr. Echeverría. O fornecedor corrige o problema em um mês e lhe agradece. Ela anota que explorar a falha para "prová-la" teria sido antiético e desnecessário.

### Exemplo resolvido

Priya documenta um escopo de varredura assinado, usa apenas arquivos sintéticos de hashes e relata uma falha de login por HTTP por divulgação coordenada, sem testes adicionais.

> **Caso sintético.** O fornecedor e os eventos são inventados.

### Erros e limites

A disponibilidade pública de dados vazados não torna ético o seu uso. Divulgar sem dar tempo ao fornecedor pode prejudicar os usuários.

### Exercícios

- **EX028 — Conteúdo da autorização.** O que o escopo assinado por Grace listava? *Rubrica:* 3 = hosts, datas e ferramentas permitidas;; 2 = dois;; 1 = nenhum;; 0 = nenhuma.

- **EX029 — Bancos de dados vazados.** Por que os estudantes não podem usar bancos de dados reais de senhas vazadas? *Rubrica:* 3 = eles contêm segredos de pessoas reais, mesmo sendo públicos;; 2 = privacidade;; 1 = permitido;; 0 = nenhuma.

- **EX030 — Passos da divulgação.** Como Priya tratou a falha de login por HTTP? *Rubrica:* 3 = parou de testar, relatou ao contato de segurança do fornecedor com prazo de noventa dias, informou o professor;; 2 = relatou;; 1 = explorou;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Priya Raman, o Dr. Tomás Echeverría, Grace Okafor, a Ashford University, o Tidewell Public Library Consortium e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Sem uma definição precisa da segurança e do atacante, a afirmação não pode ser provada nem testada.

**EX002.** x XOR x é igual a 0 e x XOR 0 é igual a x, então fazer de novo o XOR com a chave restaura a mensagem.

**EX003.** Recuperou "FINE PAID 0938", já que o XOR dos textos cifrados cancela a chave e a primeira mensagem era conhecida.

**EX004.** A cifração de disco cobre os dados armazenados, enquanto os dados em trânsito precisam de proteção de rede, como o TLS.

**EX005.** Principalmente o controle de acesso e o isolamento do sistema operacional, porque os dados precisam ser decifrados para serem processados.

**EX006.** As fitas de backup externas não eram cifradas; ela propôs cifrá-las com chaves controladas pelo consórcio, com um backup seguro das chaves.

**EX007.** Porque o é é codificado com dois bytes em UTF-8, mais um byte para cada uma das outras letras.

**EX008.** Comparando seu digest de "abc" com o exemplo publicado no FIPS 180-4, que começa com ba7816bf.

**EX009.** Se um atacante conseguir mudar tanto os arquivos quanto a lista armazenada, as mudanças passam despercebidas, então a lista precisa de proteção ou de uma assinatura.

**EX010.** Um parágrafo que usava hash, salt e derivação de chave sem defini-los para um leitor leigo.

**EX011.** O FIPS 180-4 para o SHA-256 e a RFC 9106 para o Argon2.

**EX012.** O Argon2id torna cada palpite caro em tempo e memória, desacelerando os ataques offline, embora senhas fracas ainda possam ser adivinhadas.

**EX013.** Irretratabilidade, junto com integridade e autenticação.

**EX014.** Um MAC usa uma única chave secreta compartilhada e não consegue provar qual detentor o gerou; uma assinatura usa uma chave privada e verificação pública, sustentando a irretratabilidade.

**EX015.** O cadeado mostra que o TLS protege a conexão em trânsito, e não os dados armazenados em servidores ou dispositivos.

**EX016.** Fechamento, associatividade, um elemento neutro e um inverso para cada elemento.

**EX017.** As duas partes calcularam 2, depois de trocar os valores públicos 8 e 19.

**EX018.** Um computador quântico grande que o executasse resolveria logaritmos discretos com eficiência, e é por isso que existem normas pós-quânticas como o FIPS 203.

**EX019.** Para provar a posse da chave privada do certificado e proteger o handshake contra adulteração.

**EX020.** Confere a cadeia até uma raiz confiável, que o nome corresponde e que a data está dentro da validade.

**EX021.** A wiki da equipe ainda aceitava o protocolo desatualizado TLS 1.0.

**EX022.** Elas fazem escolhas seguras sobre nonces, modos e preenchimento por padrão, de modo que menos erros são possíveis.

**EX023.** Para que nem quem chama nem os atacantes saibam qual verificação falhou.

**EX024.** Que os tokens diferem, o que mostra que um nonce novo é usado a cada vez.

**EX025.** Ele é tão rápido que hashes roubados podem ser adivinhados a taxas enormes, e senhas iguais produzem hashes iguais.

**EX026.** A mesma senha armazenada com dois salts produziu dois valores diferentes.

**EX027.** Apagar os dados que não são mais necessários, já que dados ausentes não podem vazar.

**EX028.** Os hosts no escopo, as datas dos testes e as ferramentas permitidas.

**EX029.** Porque eles guardam senhas e dados pessoais de pessoas reais, qualquer que seja sua disponibilidade pública.

**EX030.** Ela parou de testar, relatou ao contato de segurança do fornecedor com um prazo de noventa dias e avisou seu professor.

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
