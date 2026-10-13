# Criptografia e Serviços de Confiança: Curso Rápido

- Idioma: português do Brasil (`pt`); curso 008, curso rápido (1 mês). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–4 de 4 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; os três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: iniciantes sem experiência anterior em segurança.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios calculam impressões digitais SHA-256 e chamam o scrypt do hashlib sobre dados sintéticos; não implementam nenhuma cifra. Sistemas reais usam bibliotecas e produtos avaliados; nunca crie sua própria criptografia. Pessoas, organizações e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Quatro capítulos acompanham um iniciante que ajuda uma pequena biblioteca comunitária: o que a criptografia protege, permissão e prática segura, os sistemas e os fornecedores da biblioteca e uma tarefa guiada de conferência da impressão digital de um download. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Leo Fernandes** | Iniciante e voluntário | Inventado |
| **Inês Hartley** | Guia voluntária de TI | Inventada |
| **Willow Lane Community Library** | Pequena biblioteca fictícia | Inventada |

### Fontes principais

[RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 7914](https://www.rfc-editor.org/rfc/rfc7914); [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4); Menezes, van Oorschot e Vanstone, [Handbook of Applied Cryptography](https://cacr.uwaterloo.ca/hac/). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Criptografia e serviços de confiança: fundamentos e decisões

### Objetivos de aprendizagem

Você vai (1) explicar em palavras simples o que a criptografia protege; (2) distinguir codificação, hashing, cifração e assinaturas; (3) entender o que um cadeado e um certificado prometem e o que não prometem; (4) tomar decisões simples e seguras sobre ferramentas criptográficas.

### 1.1 O caso

Leo Fernandes não tem formação em segurança. Ele se inscreve num curso introdutório de um mês e, como prática, ajuda a fictícia Willow Lane Community Library, uma pequena biblioteca com um site público, um sistema de contas de e-books para os associados, dois notebooks da equipe, uma rede Wi-Fi pública e um boletim por e-mail. Sua guia é Inês Hartley, a voluntária que cuida da TI da biblioteca. Todas as pessoas, lugares e números deste livro são sintéticos. O objetivo de Leo é entender os riscos centrais o bastante para explicá-los à equipe da biblioteca e concluir com segurança uma tarefa guiada. Ele vai usar a criptografia, nunca inventá-la.

### 1.2 O que a criptografia protege

Inês explica três promessas. Confidencialidade significa que só as pessoas certas podem ler algo, como o endereço de um associado. Integridade significa que as alterações são percebidas, como um arquivo do site alterado por um invasor. Autenticidade significa que é possível saber quem enviou ou publicou algo, como um e-mail da biblioteca. A criptografia cumpre essas promessas com matemática e chaves, que são valores secretos. Ela não impede que alguém adivinhe uma senha fraca, clique num link falso ou deixe um notebook desbloqueado. Leo escreve as três palavras num cartão e pergunta, para cada ferramenta, que promessa ela cumpre, porque cada ferramenta cumpre promessas diferentes.

### 1.3 Quatro tipos de transformação

Leo conhece quatro coisas que parecem texto embaralhado. A codificação, como o Base64, só muda a forma como os dados são escritos; qualquer pessoa pode revertê-la, então ela não esconde nada. O hashing, como o SHA-256, transforma quaisquer dados numa impressão digital curta que não pode ser revertida, e uma mudança minúscula dá uma impressão digital completamente diferente. A cifração, como o AES, esconde os dados para que só quem tem a chave possa lê-los. Uma assinatura digital permite que qualquer pessoa confira quem assinou algo usando uma chave pública. O laboratório abaixo mostra o comportamento do hash sobre um texto sintético: uma letra alterada produz uma impressão digital sem nenhuma relação com a anterior.

### Laboratório — Uma letra muda a impressão digital

```python
# SHA-256 fingerprints of synthetic text (FIPS 180-4 via hashlib).
import hashlib
a = "Willow Lane opening hours: 9-17"
b = "Willow Lane opening hours: 9-18"
ha, hb = hashlib.sha256(a.encode()).hexdigest(), hashlib.sha256(b.encode()).hexdigest()
print("A:", ha[:32] + "...")
print("B:", hb[:32] + "...")
print("match:", ha == hb)
```

Execute com `python3 lab_fingerprint.py`. Saída verificada:

```text
A: 7a5d91566f93af7abf7fc2c33d868004...
B: c029501271e71ec3fc765840b69dfabd...
match: False
```

### 1.4 O cadeado e o certificado

Quando Leo abre o site da biblioteca, o navegador mostra um cadeado. Inês explica que isso significa que a conexão usa TLS, o protocolo da RFC 8446, então pessoas na mesma rede Wi-Fi não conseguem ler nem alterar o que passa entre Leo e o site. O site prova seu nome com um certificado, definido na RFC 5280, emitido por uma autoridade em que o navegador confia. O cadeado não significa que o site é honesto, livre de bugs ou aquele que Leo pretendia visitar; um site falso com um nome parecido pode ter seu próprio cadeado. Por isso Leo confere o endereço com cuidado, e não apenas o cadeado.

### 1.5 Decisões simples e seguras

Inês dá a Leo quatro regras para as decisões que ele pode tomar sozinho. Use ferramentas e configurações conhecidas, em vez de truques caseiros. Nunca ignore um aviso de certificado do navegador num site que deveria ser confiável; relate-o. Mantenha segredos como senhas e chaves fora de e-mails, chats e documentos compartilhados. Na dúvida, pergunte antes de mudar qualquer coisa. Leo percebe que as regras tratam de comportamento, e não de matemática. A maioria dos problemas reais em pequenas organizações vem de configurações e hábitos, e um iniciante que segue essas regras já evita os erros mais comuns cometidos por pessoas que sabem muito mais teoria.

### Exemplo resolvido

Leo relaciona o site, as contas de e-books e o boletim da biblioteca às três promessas, executa o laboratório da impressão digital e explica a um funcionário por que o cadeado sozinho não basta.

> **Caso sintético.** A Willow Lane Community Library, Leo e Inês são inventados; a RFC 8446 e a RFC 5280 são reais.

### Erros e limites

Estas são primeiras aproximações; sistemas reais combinam vários mecanismos. Um cadeado num site falso continua parecendo um cadeado.

### Exercícios

- **EX001 — O objetivo de Leo.** O que Leo está tentando alcançar neste curso? *Rubrica:* 3 = entender os riscos centrais, explicá-los e concluir com segurança uma tarefa guiada;; 2 = parte;; 1 = projetar criptografia;; 0 = nenhuma.

- **EX002 — Integridade numa biblioteca.** Dê um exemplo de integridade numa biblioteca. *Rubrica:* 3 = perceber que um arquivo do site foi alterado por um invasor;; 2 = exemplo;; 1 = exemplo de confidencialidade;; 0 = nenhuma.

- **EX003 — O que a criptografia não impede.** Cite duas coisas que a criptografia não consegue impedir. *Rubrica:* 3 = adivinhação de senhas fracas, cliques em links falsos, notebooks desbloqueados (duas);; 2 = uma;; 1 = diz que impede tudo;; 0 = nenhuma.

- **EX004 — Sigilo do Base64.** O Base64 esconde uma senha? Explique. *Rubrica:* 3 = não; é codificação que qualquer um pode reverter sem chave;; 2 = não;; 1 = sim;; 0 = nenhuma.

- **EX005 — Mudança de uma letra.** No laboratório, o que aconteceu quando uma letra mudou? *Rubrica:* 3 = a impressão digital SHA-256 mudou completamente, match False;; 2 = mudou;; 1 = igual;; 0 = nenhuma.

- **EX006 — Revertendo um hash.** Uma impressão digital SHA-256 pode ser convertida de volta no texto original? *Rubrica:* 3 = não, o hashing é de mão única;; 2 = não;; 1 = sim;; 0 = nenhuma.

- **EX007 — Quem lê dados cifrados.** Quem pode ler dados cifrados com AES? *Rubrica:* 3 = só quem tem a chave certa;; 2 = quem tem a chave;; 1 = qualquer um;; 0 = nenhuma.

- **EX008 — Conferência da assinatura.** O que uma assinatura digital permite que qualquer pessoa confira? *Rubrica:* 3 = quem assinou e que não houve alteração, usando uma chave pública;; 2 = quem assinou;; 1 = esconde o conteúdo;; 0 = nenhuma.

- **EX009 — A promessa do cadeado.** O que o cadeado do navegador de fato promete? *Rubrica:* 3 = a conexão é protegida por TLS até o site nomeado no certificado;; 2 = conexão TLS;; 1 = o site é honesto;; 0 = nenhuma.

- **EX010 — Cadeado em site falso.** Por que um site falso da biblioteca ainda pode mostrar um cadeado? *Rubrica:* 3 = ele pode obter seu próprio certificado para um nome parecido;; 2 = certificado próprio;; 1 = impossível;; 0 = nenhuma.

- **EX011 — Aviso de certificado.** O que Leo deve fazer se o site da biblioteca mostrar um aviso de certificado? *Rubrica:* 3 = não ignorar o aviso; relatá-lo;; 2 = relatar;; 1 = ignorar o aviso;; 0 = nenhuma.

- **EX012 — Segredos no chat.** Onde senhas e chaves nunca devem ser compartilhadas? *Rubrica:* 3 = e-mail, chat ou documentos compartilhados;; 2 = um lugar;; 1 = qualquer lugar serve;; 0 = nenhuma.

- **EX013 — Foco das regras.** Do que tratam principalmente as quatro regras de Inês? *Rubrica:* 3 = comportamento e configurações, e não matemática;; 2 = comportamento;; 1 = matemática;; 0 = nenhuma.

### Síntese

A criptografia cumpre promessas de confidencialidade, integridade e autenticidade por meio de chaves, e os iniciantes ficam seguros ao ligar as ferramentas às promessas e seguir regras simples.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 04)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Escopo, permissão e prática segura

### Objetivos de aprendizagem

Você vai (1) explicar por que a permissão vem antes de qualquer verificação; (2) definir um escopo pequeno e seguro; (3) manusear dados pessoais e segredos com cuidado; (4) relatar problemas de forma responsável.

### 2.1 Primeiro, a permissão

Leo é curioso e quer varrer a rede da biblioteca para ver o que há nela. Inês o impede: verificar sistemas sem permissão pode ser ilegal, pode quebrar dispositivos frágeis como o velho quiosque de autoatendimento e pode incomodar parceiros cujos sistemas estão na mesma rede. Mesmo com boas intenções, os testes precisam de permissão escrita da pessoa responsável. No caso de Leo, é o gerente da biblioteca, que assina uma breve nota. Leo aprende que pedir antes não é uma formalidade; isso protege a biblioteca, seus associados e o próprio Leo, e constrói a confiança que permite que ele ajude de novo depois.

### 2.2 Um escopo pequeno e seguro

A nota assinada lista exatamente o que Leo pode fazer: ler no navegador os detalhes do certificado do site da biblioteca, conferir se os notebooks da equipe têm a cifração de disco ativada e revisar se a página de contas de e-books usa uma política de senhas forte. Ela lista o que ele não pode fazer: varrer a rede, testar senhas, mexer nos sistemas do fornecedor de livros ou nos equipamentos de Wi-Fi da prefeitura. Ela também indica a semana e Inês como seu contato. Um escopo pequeno mantém a primeira tarefa de um iniciante segura e possível de terminar. Leo escreve o escopo no alto das suas anotações e confere cada passo contra ele antes de começar.

### 2.3 Dados pessoais e segredos

As bibliotecas guardam dados pessoais: nomes, endereços, histórico de empréstimos. Ao verificar um notebook, Leo pode ver registros de associados na tela. Inês o ensina a olhar apenas o que a tarefa exige, fechar todo o resto e nunca copiar dados pessoais para suas anotações. Se ele encontrar uma senha escrita num post-it ou salva num arquivo de texto, registra onde estava e que tipo de segredo é, mas não a própria senha, e avisa Inês no mesmo dia para que ela seja trocada. Escrever um segredo num relatório só espalharia ainda mais o problema.

### 2.4 Relatando com responsabilidade

Quando Leo encontra algo errado, ele relata a Inês e ao gerente, e não a amigos ou às redes sociais. Seu relato diz o que ele viu, onde, quando e por que isso importa, em palavras simples, com uma sugestão de próximo passo. Se algum dia ele notasse uma fraqueza num produto que muitas bibliotecas usam, como a plataforma de e-books, o caminho certo seria avisar o fornecedor em particular, por meio da biblioteca, para que ele a corrija antes que os detalhes se tornem públicos. Isso se chama divulgação coordenada. Relatar com responsabilidade transforma uma descoberta numa correção, e não num novo risco.

### Exemplo resolvido

Leo obtém uma nota de escopo assinada, verifica dentro dela a cifração de disco de dois notebooks, encontra um post-it com uma senha, registra apenas sua localização e relata o caso a Inês.

> **Caso sintético.** A nota de escopo, os notebooks e o post-it são sintéticos.

### Erros e limites

A permissão não torna seguro um trabalho descuidado. As regras sobre dados pessoais variam conforme o país; siga a política da biblioteca.

### Exercícios

- **EX014 — Recusa da varredura.** Por que Inês impediu Leo de varrer a rede? *Rubrica:* 3 = sem permissão; pode ser ilegal, quebrar dispositivos ou afetar parceiros;; 2 = um motivo;; 1 = pode varrer;; 0 = nenhuma.

- **EX015 — Quem concede a permissão.** Quem assina a nota de permissão de Leo? *Rubrica:* 3 = o gerente da biblioteca;; 2 = gerente;; 1 = Leo;; 0 = nenhuma.

- **EX016 — Verificações permitidas.** Liste duas verificações que Leo pode fazer. *Rubrica:* 3 = duas entre: ler o certificado do site, conferir a cifração de disco dos notebooks, revisar a política de senhas;; 2 = uma;; 1 = varrer a rede;; 0 = nenhuma.

- **EX017 — Ações proibidas.** Cite duas ações fora do escopo de Leo. *Rubrica:* 3 = duas entre: varredura, testar senhas, sistemas do fornecedor, equipamentos de Wi-Fi da prefeitura;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX018 — Benefício do escopo pequeno.** O que um escopo pequeno dá a um iniciante? *Rubrica:* 3 = uma primeira tarefa segura e possível de terminar;; 2 = segura;; 1 = vago;; 0 = nenhuma.

- **EX019 — Registro de associado visto.** O que Leo deve fazer se o registro de um associado aparecer na tela? *Rubrica:* 3 = olhar só o que a tarefa exige, fechá-lo e não copiá-lo;; 2 = fechá-lo;; 1 = copiá-lo;; 0 = nenhuma.

- **EX020 — Post-it.** Como Leo deve registrar uma senha encontrada num post-it? *Rubrica:* 3 = apenas localização e tipo, e avisar Inês para trocá-la;; 2 = localização;; 1 = escreve a senha;; 0 = nenhuma.

- **EX021 — Conteúdo do relato.** O que o relato de Leo deve incluir? *Rubrica:* 3 = o quê, onde, quando, por que importa e um próximo passo;; 2 = três;; 1 = vago;; 0 = nenhuma.

- **EX022 — Público errado.** Quem não deve ser o primeiro a saber de uma fraqueza? *Rubrica:* 3 = amigos ou redes sociais;; 2 = cita;; 1 = o gerente;; 0 = nenhuma.

- **EX023 — Fraqueza na plataforma.** Como deve ser tratada uma fraqueza na plataforma de e-books? *Rubrica:* 3 = divulgação coordenada ao fornecedor por meio da biblioteca;; 2 = fornecedor;; 1 = publicar on-line;; 0 = nenhuma.

- **EX024 — Nome da divulgação coordenada.** Como se chama o caminho de relato que começa em particular? *Rubrica:* 3 = divulgação coordenada;; 2 = nomeado;; 1 = vago;; 0 = nenhuma.

- **EX025 — Risco do quiosque.** Que dispositivo frágil uma varredura não aprovada poderia perturbar? *Rubrica:* 3 = o velho quiosque de autoatendimento;; 2 = quiosque;; 1 = vago;; 0 = nenhuma.

- **EX026 — Proteção ao pedir.** A quem protege pedir permissão? *Rubrica:* 3 = a biblioteca, seus associados e Leo;; 2 = dois;; 1 = ninguém;; 0 = nenhuma.

### Síntese

A prática segura significa obter permissão, manter um escopo pequeno, manusear dados pessoais e segredos com cuidado e relatar pelas pessoas certas.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 04)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Criptografia e serviços de confiança: sistemas, dados e dependências

### Objetivos de aprendizagem

Você vai (1) listar os sistemas da biblioteca e onde a criptografia é usada; (2) explicar como as senhas devem ser armazenadas; (3) reconhecer as dependências de fornecedores externos; (4) entender por que chaves e certificados expiram.

### 3.1 Os sistemas e sua criptografia

Com Inês, Leo lista os sistemas da biblioteca. O site usa TLS para que as conexões dos visitantes sejam privadas. O sistema de contas de e-books armazena as senhas dos associados e é operado por um fornecedor externo. Os notebooks da equipe usam a cifração de disco embutida, então um notebook roubado não expõe os arquivos. O Wi-Fi público usa uma senha compartilhada, que mantém afastados os vizinhos ocasionais, mas não protege os usuários uns dos outros. A plataforma do boletim assina os e-mails enviados para que os destinatários possam saber que eles vêm mesmo da biblioteca. Leo se surpreende com quantos lugares usam criptografia silenciosamente, sem que ninguém na biblioteca pense nisso.

### 3.2 Como as senhas devem ser armazenadas

Leo pergunta como um site se lembra da sua senha. Inês explica que um bom sistema nunca armazena a própria senha. Ele armazena o resultado de uma função de hashing de senhas lenta e com salt, como o scrypt, descrito na RFC 7914, ou o Argon2id, descrito na RFC 9106. O salt é um valor aleatório por usuário, então dois associados com a mesma senha recebem resultados armazenados diferentes. Quando você faz login, o sistema repete o cálculo e compara. Se ladrões roubarem o banco de dados, o hashing lento torna caro adivinhar. O laboratório abaixo mostra o armazenamento com salt sobre contas sintéticas usando a biblioteca padrão do Python.

### Laboratório — Armazenamento de senhas com salt

```python
# Salted scrypt storage for synthetic members. Teaching only; real systems use maintained libraries.
import hashlib, hmac, secrets
P = dict(n=2**14, r=8, p=1, dklen=32)
def store(pw):
    s = secrets.token_bytes(16); return s, hashlib.scrypt(pw, salt=s, **P)
def check(pw, rec): return hmac.compare_digest(hashlib.scrypt(pw, salt=rec[0], **P), rec[1])
m1, m2 = store(b"ReadMore2026"), store(b"ReadMore2026")
print("same password, same stored value?", m1[1] == m2[1])
print("member 1 right password:", check(b"ReadMore2026", m1))
print("member 2 right password:", check(b"ReadMore2026", m2))
print("member 1 wrong password:", check(b"ReadLess2026", m1))
```

Execute com `python3 lab_salted.py`. Saída verificada:

```text
same password, same stored value? False
member 1 right password: True
member 2 right password: True
member 1 wrong password: False
```

### 3.3 Dependendo de fornecedores

Muitas das proteções da biblioteca são operadas por outros. O fornecedor de e-books armazena os hashes das senhas dos associados; a plataforma do boletim guarda a chave de assinatura dos e-mails; o provedor de hospedagem renova o certificado do site. A biblioteca não pode mudar essas configurações diretamente, mas depende delas. Inês mostra a Leo como conferir o que o fornecedor promete, por exemplo na sua página de segurança ou no contrato, e a quem contatar se algo der errado. Conhecer a lista de dependências significa que, quando um fornecedor anuncia um problema, a biblioteca sabe na hora se os associados foram afetados e o que dizer a eles.

### 3.4 Por que as coisas expiram

Os certificados e algumas chaves têm data de validade. Um certificado que expira faz os navegadores mostrarem avisos, o que aconteceu com o site da biblioteca no ano passado, quando a renovação automática do provedor de hospedagem falhou silenciosamente. A expiração existe para que uma chave não possa ser usada para sempre caso tenha sido roubada sem que ninguém percebesse, e para que as configurações sejam atualizadas. Inês agora mantém um calendário simples de datas de expiração com lembretes um mês antes, mesmo para itens que os fornecedores renovam automaticamente. Leo aprende que a criptografia não é algo que se configura e se esquece: alguém precisa vigiar datas, renovações e fornecedores, ou a própria proteção pode causar uma indisponibilidade.

### Exemplo resolvido

Leo monta uma tabela de cinco linhas com os sistemas da biblioteca, seu uso de criptografia e quem os controla, executa o laboratório de armazenamento com salt e acrescenta o certificado do site ao calendário de expiração.

> **Caso sintético.** Os sistemas, os fornecedores e a indisponibilidade passada são sintéticos; a RFC 7914 e a RFC 9106 são reais.

### Erros e limites

Uma senha de Wi-Fi compartilhada dá proteção limitada entre os usuários. As promessas dos fornecedores ainda precisam ser conferidas ao longo do tempo.

### Exercícios

- **EX027 — Propósito da cifração dos notebooks.** Contra o que a cifração de disco dos notebooks protege? *Rubrica:* 3 = um notebook roubado expondo seus arquivos;; 2 = roubo;; 1 = ataques de rede;; 0 = nenhuma.

- **EX028 — Limite do Wi-Fi compartilhado.** O que a senha compartilhada do Wi-Fi não faz? *Rubrica:* 3 = proteger os usuários da rede uns dos outros;; 2 = limite;; 1 = protege tudo;; 0 = nenhuma.

- **EX029 — Assinatura do boletim.** Por que a plataforma do boletim assina os e-mails? *Rubrica:* 3 = para que os destinatários possam saber que o e-mail vem mesmo da biblioteca;; 2 = autenticidade;; 1 = sigilo;; 0 = nenhuma.

- **EX030 — Nunca armazenada.** O que um bom sistema de login nunca deve armazenar? *Rubrica:* 3 = a própria senha;; 2 = senha;; 1 = o hash;; 0 = nenhuma.

- **EX031 — Significado de salt.** O que é um salt no armazenamento de senhas? *Rubrica:* 3 = um valor aleatório por usuário para que senhas iguais deem resultados diferentes;; 2 = valor aleatório;; 1 = chave secreta;; 0 = nenhuma.

- **EX032 — Resultado do laboratório.** No laboratório com salt, dois associados com a mesma senha receberam o mesmo valor armazenado? *Rubrica:* 3 = não, diferiram; os dois foram verificados com a senha certa;; 2 = não;; 1 = sim;; 0 = nenhuma.

- **EX033 — Valor do hashing lento.** Por que o hashing lento é útil se um banco de dados for roubado? *Rubrica:* 3 = torna cada palpite caro para os ladrões;; 2 = caro;; 1 = mais rápido;; 0 = nenhuma.

- **EX034 — Chave do fornecedor.** Quem guarda a chave de assinatura dos e-mails? *Rubrica:* 3 = a plataforma do boletim;; 2 = plataforma;; 1 = biblioteca;; 0 = nenhuma.

- **EX035 — Conferindo um fornecedor.** Onde a biblioteca pode conferir as promessas de um fornecedor? *Rubrica:* 3 = na sua página de segurança ou no contrato;; 2 = um lugar;; 1 = em lugar nenhum;; 0 = nenhuma.

- **EX036 — Causa da indisponibilidade passada.** Por que o site da biblioteca mostrou avisos no ano passado? *Rubrica:* 3 = a renovação automática do provedor falhou silenciosamente e o certificado expirou;; 2 = expirou;; 1 = invadido;; 0 = nenhuma.

- **EX037 — Propósito da expiração.** Dê um motivo pelo qual os certificados expiram. *Rubrica:* 3 = limita o uso de uma chave roubada ou força a atualização das configurações;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX038 — Lembretes do calendário.** Com quanta antecedência Inês configura os lembretes de expiração? *Rubrica:* 3 = um mês;; 2 = mês;; 1 = vago;; 0 = nenhuma.

### Síntese

Pequenas organizações dependem da criptografia em muitos sistemas e fornecedores, então precisam saber onde ela é usada e vigiar senhas, chaves e datas de expiração.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 04)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Criptografia e serviços de confiança: laboratório guiado e síntese aplicada

### Objetivos de aprendizagem

Você vai (1) concluir uma tarefa guiada verificando um arquivo baixado com uma impressão digital publicada; (2) interpretar o resultado corretamente; (3) escrever um breve resumo em linguagem simples para a equipe da biblioteca; (4) planejar seus próximos passos de aprendizado.

### 4.1 A tarefa guiada

A biblioteca quer instalar uma ferramenta de catálogo gratuita num notebook da equipe. O site do projeto publica uma impressão digital SHA-256 para cada download. Inês pede a Leo que confira se o arquivo que ele baixou corresponde a ela. A ideia é simples: se mesmo um único byte do arquivo tiver sido danificado ou trocado, a impressão digital será diferente. Leo faz a tarefa de forma segura, usando um arquivo sintético no laboratório abaixo, e depois repete os passos com o download real sob a supervisão de Inês. O laboratório compara um arquivo correto e um arquivo adulterado com o valor publicado e imprime a correspondência ou a divergência de cada um.

### Laboratório — Conferindo a impressão digital de um download

```python
# Compare synthetic downloads with a published SHA-256 fingerprint.
import hashlib
original = b"catalogue-tool v2.1 synthetic installer bytes " * 50
published = hashlib.sha256(original).hexdigest()
tampered = original[:-1] + b"!"
print("published:", published[:24] + "...")
for name, data in [("download_ok.bin", original), ("download_bad.bin", tampered)]:
    print(name, "MATCH" if hashlib.sha256(data).hexdigest() == published else "MISMATCH")
```

Execute com `python3 lab_checkfile.py`. Saída verificada:

```text
published: 215e60edb672063786f8bb92...
download_ok.bin MATCH
download_bad.bin MISMATCH
```

### 4.2 Lendo o resultado

Uma correspondência diz a Leo que o arquivo é idêntico àquele cuja impressão digital foi publicada. Ela não lhe diz que o software é seguro ou livre de bugs e, se um atacante tivesse alterado tanto o arquivo quanto a impressão digital no mesmo site, a verificação ainda daria correspondência. É por isso que alguns projetos também assinam suas versões com uma assinatura digital, que exige a chave privada do projeto para ser forjada. Leo anota os dois pontos. Uma divergência significa parar: não instalar, baixar de novo do site oficial e avisar Inês se ainda falhar.

### 4.3 Resumindo para a equipe

Leo escreve um resumo de cinco frases para a equipe da biblioteca. O download da ferramenta de catálogo foi conferido com a impressão digital publicada pelo projeto e correspondeu. Isso mostra que o arquivo não foi danificado nem trocado no caminho. Isso não prova que o software é seguro, então ele é instalado primeiro em apenas um notebook. Se uma verificação algum dia falhar, o arquivo não deve ser instalado. Leo também lista os três achados dos capítulos anteriores: o post-it com a senha, o calendário de expiração e o alerta sobre ignorar erros de certificado, cada um com quem vai agir.

### 4.4 O que vem a seguir

O curso termina com uma breve reflexão. Leo agora consegue explicar as três promessas, distinguir codificação de cifração, pedir permissão e escopo, não guardar nada secreto nas anotações e conferir a impressão digital de um download. Ele sabe o que não sabe: como o TLS negocia chaves, como os certificados são emitidos e como as organizações gerenciam chaves ao longo dos anos. Inês recomenda os próximos passos: o curso profissional e a leitura de capítulos acessíveis do Handbook of Applied Cryptography, de Menezes, van Oorschot e Vanstone, cujos capítulos estão disponíveis gratuitamente on-line. Leo sai com uma visão clara dos riscos centrais e com uma tarefa segura concluída.

### Exemplo resolvido

Leo executa o laboratório da impressão digital, verifica o download real sob supervisão, escreve um resumo de cinco frases para a equipe e lista três achados anteriores com seus donos.

> **Caso sintético.** A ferramenta de catálogo, os arquivos e as impressões digitais são sintéticos; o Handbook of Applied Cryptography é real.

### Erros e limites

Uma impressão digital vinda do mesmo site que o arquivo prova apenas que os dois correspondem. As assinaturas exigem que a chave de quem assina seja confiada corretamente.

### Exercícios

- **EX039 — Impressão digital publicada.** O que o projeto do catálogo publica para cada download? *Rubrica:* 3 = uma impressão digital SHA-256;; 2 = impressão digital;; 1 = senha;; 0 = nenhuma.

- **EX040 — Resultados do laboratório.** O que o laboratório imprimiu para o arquivo correto e para o adulterado? *Rubrica:* 3 = MATCH para o arquivo correto, MISMATCH para o adulterado;; 2 = um;; 1 = os dois correspondem;; 0 = nenhuma.

- **EX041 — Significado de uma correspondência.** O que uma impressão digital correspondente prova? *Rubrica:* 3 = que o arquivo é idêntico ao publicado;; 2 = idêntico;; 1 = o software é seguro;; 0 = nenhuma.

- **EX042 — Correspondência não é segurança.** O que uma correspondência não prova? *Rubrica:* 3 = que o software é seguro ou livre de bugs;; 2 = segurança;; 1 = prova tudo;; 0 = nenhuma.

- **EX043 — Fraqueza do mesmo site.** Quando uma verificação de impressão digital poderia ser enganada? *Rubrica:* 3 = se um atacante alterasse o arquivo e a impressão digital no mesmo site;; 2 = ambos alterados;; 1 = nunca;; 0 = nenhuma.

- **EX044 — Versões assinadas.** Por que alguns projetos também assinam suas versões? *Rubrica:* 3 = forjar uma assinatura exige a chave privada do projeto;; 2 = chave privada;; 1 = nenhum motivo;; 0 = nenhuma.

- **EX045 — Ação após divergência.** O que Leo deve fazer após uma divergência? *Rubrica:* 3 = parar, não instalar, baixar de novo do site oficial, avisar Inês se falhar de novo;; 2 = parar;; 1 = instalar assim mesmo;; 0 = nenhuma.

- **EX046 — Instalação em etapas.** Por que a ferramenta é instalada primeiro em um notebook? *Rubrica:* 3 = uma correspondência não prova que o software é seguro;; 2 = cautela;; 1 = vago;; 0 = nenhuma.

- **EX047 — Achados anteriores.** Liste os três achados anteriores no resumo de Leo. *Rubrica:* 3 = senha no post-it, calendário de expiração, alerta sobre avisos de certificado;; 2 = dois;; 1 = vago;; 0 = nenhuma.

- **EX048 — Desconhecidos admitidos.** Cite dois temas que Leo sabe que ainda não aprendeu. *Rubrica:* 3 = dois entre: negociação de chaves do TLS, emissão de certificados, gerenciamento de chaves a longo prazo;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX049 — Leitura gratuita.** Que referência com capítulos gratuitos on-line Inês recomenda? *Rubrica:* 3 = Handbook of Applied Cryptography, de Menezes, van Oorschot e Vanstone;; 2 = título;; 1 = vago;; 0 = nenhuma.

- **EX050 — Próximo curso.** Que curso Inês sugere em seguida? *Rubrica:* 3 = o curso profissional;; 2 = nomeado;; 1 = vago;; 0 = nenhuma.

### Síntese

Conferir uma impressão digital publicada é uma tarefa criptográfica pequena e real, e entender o que ela prova e o que não prova é a lição final do curso.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 04)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Leo Fernandes, Inês Hartley, a Willow Lane Community Library e todos os arquivos e números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Entender os riscos centrais, explicá-los à equipe da biblioteca e concluir com segurança uma tarefa guiada.

**EX002.** Perceber que uma página do site da biblioteca foi alterada por alguém que não deveria tê-la alterado.

**EX003.** Ela não impede que uma senha fraca seja adivinhada nem que uma pessoa clique num link falso.

**EX004.** Não. O Base64 é só uma forma de escrever dados, e qualquer pessoa pode revertê-lo sem chave nenhuma.

**EX005.** A impressão digital ficou completamente diferente e a verificação de correspondência imprimiu False.

**EX006.** Não. O hashing é de mão única; só é possível conferir um palpite calculando seu hash e comparando.

**EX007.** Só quem tem a chave secreta correta.

**EX008.** Quem assinou o item e que ele não foi alterado, usando a chave pública de quem assinou.

**EX009.** Que a conexão está protegida por TLS e que o site tem um certificado para o nome mostrado.

**EX010.** Porque ele pode obter um certificado válido para seu próprio nome parecido, e assim o cadeado aparece.

**EX011.** Parar, não ignorar o aviso e relatá-lo a Inês.

**EX012.** Nunca em e-mails, mensagens de chat ou documentos compartilhados.

**EX013.** Tratam de comportamento e configurações, que é de onde vem a maioria dos problemas reais.

**EX014.** Porque, sem permissão, isso poderia ser ilegal, quebrar dispositivos frágeis como o quiosque e afetar os sistemas de parceiros.

**EX015.** O gerente da biblioteca, que é o responsável pelos sistemas da biblioteca.

**EX016.** Ler os detalhes do certificado do site e conferir se os notebooks têm a cifração de disco ativada.

**EX017.** Varrer a rede e testar senhas estão ambos fora do seu escopo.

**EX018.** Torna a primeira tarefa segura e possível de terminar.

**EX019.** Desviar o olhar do que a tarefa não exige, fechar o registro e nunca copiá-lo para as anotações.

**EX020.** Ele anota onde estava e que é uma senha, sem escrevê-la, e avisa Inês para que ela seja trocada.

**EX021.** O que ele viu, onde e quando, por que importa e uma sugestão de próximo passo.

**EX022.** Amigos e redes sociais; os achados vão para Inês e para o gerente.

**EX023.** Avisar o fornecedor em particular, por meio da biblioteca, para que a fraqueza seja corrigida antes que os detalhes sejam públicos.

**EX024.** Divulgação coordenada.

**EX025.** O velho quiosque de autoatendimento da biblioteca, que poderia travar sob uma varredura.

**EX026.** Protege a biblioteca, seus associados e o próprio Leo.

**EX027.** Contra um notebook perdido ou roubado ter seus arquivos lidos.

**EX028.** Não protege as pessoas da rede umas das outras.

**EX029.** Para que os sistemas de e-mail que recebem possam conferir que o boletim vem mesmo da biblioteca.

**EX030.** A senha propriamente dita; ele guarda apenas um hash lento e com salt.

**EX031.** Um valor aleatório armazenado com o hash de cada usuário para que senhas idênticas produzam resultados armazenados diferentes.

**EX032.** Não. Seus valores armazenados eram diferentes, e os dois ainda foram verificados com a senha correta.

**EX033.** Torna caro cada palpite de senha, atrasando os ladrões que tentam recuperar as senhas.

**EX034.** O fornecedor da plataforma do boletim.

**EX035.** Na página de segurança publicada pelo fornecedor ou no contrato.

**EX036.** O certificado expirou porque a renovação automática do provedor de hospedagem falhou sem que ninguém percebesse.

**EX037.** Para que uma chave roubada sem que ninguém percebesse não possa ser usada para sempre.

**EX038.** Um mês antes de cada data de expiração.

**EX039.** Uma impressão digital SHA-256 de cada arquivo.

**EX040.** O arquivo correto imprimiu MATCH e o arquivo adulterado imprimiu MISMATCH.

**EX041.** Que o arquivo baixado é exatamente o arquivo cuja impressão digital foi publicada.

**EX042.** Não prova que o software é seguro ou livre de bugs.

**EX043.** Se um atacante substituísse tanto o arquivo quanto a impressão digital publicada no mesmo site.

**EX044.** Porque forjar uma assinatura digital exige a chave privada do projeto, que um atacante no site não tem.

**EX045.** Parar, não instalar, baixar de novo do site oficial e avisar Inês se ainda falhar.

**EX046.** Porque a correspondência não prova segurança, então testá-la num notebook limita o dano se algo estiver errado.

**EX047.** O post-it com a senha, o calendário de expiração e o conselho de não ignorar avisos de certificado.

**EX048.** Como o TLS negocia chaves e como os certificados são emitidos.

**EX049.** O Handbook of Applied Cryptography, de Menezes, van Oorschot e Vanstone.

**EX050.** O curso profissional de criptografia e serviços de confiança.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
