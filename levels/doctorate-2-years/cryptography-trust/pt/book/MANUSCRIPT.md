# Criptografia e Serviços de Confiança: Trilha de Pesquisa de Doutorado

- Idioma: português do Brasil (`pt`); curso 192, trilha de pesquisa de doutorado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 8 já estão escritos em português, com os exercícios EX001–EX026 e suas resoluções com rubricas de 0 a 3 e 3 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 5–8 (EX027–EX050) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: doutorandos que estudam como o uso indevido de criptografia em software pode ser medido e reduzido como controle de engenharia.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: este livro estuda o *uso* de bibliotecas criptográficas avaliadas. Ele nunca ensina a projetar nem a implementar à mão primitivas para produção; os pequenos laboratórios com a biblioteca padrão apenas medem, contam e calculam hashes de dados sintéticos. Pessoas, organizações, chaves e achados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma doutoranda que testa se um checklist de uso indevido de criptografia somado a uma etapa automatizada de lint na revisão de código reduz o uso indevido confirmado (reutilização de nonce, manuseio fraco de chaves, primitivas obsoletas) nas mudanças integradas, passando pela concordância entre codificadores, a fronteira da pesquisa, uma proposta registrada, uma auditoria de linha de base e um piloto, um estudo principal randomizado, a crítica por pares, um arquivo de reprodutibilidade com hashes e a defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Nadia Haddad** | Doutoranda | Inventada |
| **Prof. Oskar Brandt** | Orientador | Inventado |
| **Larkspur University** | Universidade fictícia | Inventada |
| **Meridian Payments Cooperative** | Parceira fictícia com 24 equipes de engenharia | Inventada |

### Fontes principais

Katz e Lindell, *Introduction to Modern Cryptography* (3ª ed.); Boneh e Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); Menezes et al., [*Handbook of Applied Cryptography*](https://cacr.uwaterloo.ca/hac/); NIST [SP 800-38D](https://doi.org/10.6028/NIST.SP.800-38D), [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5), [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203); [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–8: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridade e métodos avançados de pesquisa

### Objetivos de aprendizagem

Você vai (1) enquadrar uma questão de doutorado sobre o uso indevido de criptografia na revisão de código; (2) construir e testar um esquema de codificação confiável para os achados de uso indevido; (3) definir regras de integridade e de divulgação para lidar com fraquezas em sistemas de pagamento em produção.

### 1.1 O caso

Nadia Haddad é doutoranda na fictícia Larkspur University, sob orientação do Prof. Oskar Brandt. Sua parceira, a fictícia Meridian Payments Cooperative, tem 24 equipes de engenharia que chamam bibliotecas criptográficas avaliadas para a tokenização de cartões, a assinatura de webhooks e a cifração de dados em repouso. Todas as equipes, mudanças e números deste livro são sintéticos. A pergunta de Nadia é se acrescentar um checklist de uso indevido de criptografia e uma etapa automatizada de lint à revisão de código reduz o número de achados confirmados de uso indevido a cada dez mudanças integradas, em comparação com a revisão habitual da Meridian. A unidade de interesse é o uso indevido de bibliotecas corretas, e não algoritmos quebrados, o que corresponde ao que os profissionais mais erram.

### 1.2 O que conta como uso indevido

Uso indevido significa uma primitiva correta usada de um modo que anula sua garantia de segurança. Katz e Lindell mostram que a cifração autenticada só é segura sob condições declaradas, e o SP 800-38D torna uma delas explícita: um nonce do GCM nunca pode se repetir sob a mesma chave. O livro de códigos de Nadia tem quatro categorias. Nonce-iv cobre nonces e vetores de inicialização repetidos, previsíveis ou truncados. Key-handling cobre chaves embutidas no código, registradas em log, compartilhadas em excesso ou nunca rotacionadas. Primitive-choice cobre algoritmos obsoletos ou inadequados, como hashes rápidos sem salt para senhas. Other captura os problemas residuais. Cada categoria traz uma definição, dois exemplos, dois quase acertos e uma regra de sobreposição.

### Laboratório — Concordância entre codificadores

```python
"""Cohen's kappa for two coders labelling synthetic cryptographic-misuse findings (read-only)."""
from collections import Counter
CATS = ["nonce-iv", "key-handling", "primitive-choice", "other"]
# 48 synthetic findings: (coder A label, coder B label)
PAIRS = ([("nonce-iv", "nonce-iv")] * 12 + [("key-handling", "key-handling")] * 13 +
         [("primitive-choice", "primitive-choice")] * 10 + [("other", "other")] * 6 +
         [("key-handling", "primitive-choice")] * 3 + [("nonce-iv", "primitive-choice")] * 2 +
         [("other", "key-handling")] * 2)

def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in CATS) / n ** 2
    return po, pe, (po - pe) / (1 - pe)

def main():
    po, pe, k = kappa(PAIRS)
    print(f"items {len(PAIRS)}, agreed {sum(a == b for a, b in PAIRS)}")
    print(f"observed {po:.3f}, chance {pe:.3f}, kappa {k:.3f}")
    for (a, b), n in sorted(Counter(p for p in PAIRS if p[0] != p[1]).items()):
        print(f"disagree {a} -> {b}: {n}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_kappa.py`. Saída verificada:

```text
items 48, agreed 41
observed 0.854, chance 0.263, kappa 0.802
disagree key-handling -> primitive-choice: 3
disagree nonce-iv -> primitive-choice: 2
disagree other -> key-handling: 2
```

### 1.3 Ler a concordância

Dois codificadores treinados rotulam de forma independente 48 achados sintéticos e concordam em 41, uma concordância observada de 0,854. A concordância ao acaso, calculada a partir das frequências de categoria de cada codificador, é 0,263, então o kappa de Cohen é 0,802; Landis e Koch chamariam isso de substancial a quase perfeito, mas Nadia trata esses rótulos como orientação aproximada. As discordâncias são informativas. Cinco das sete levam um achado para primitive-choice, três vindas de key-handling e duas de nonce-iv. O codificador B lê "uma chave derivada com um hash rápido" como uma escolha de algoritmo, enquanto o codificador A a lê como manuseio de chave. Nadia acrescenta uma regra de sobreposição: a derivação de uma chave é key-handling, a menos que o próprio algoritmo esteja obsoleto (deprecated).

### 1.4 Integridade e divulgação

Os achados sobre código de pagamento em produção são perigosos, porque a descrição de uma fraqueza não corrigida poderia ajudar um atacante a forjar webhooks ou a decifrar tokens armazenados. O acordo de dados de Nadia diz que a Meridian só compartilha um achado depois que a correção foi implantada ou o código foi desativado, que os nomes de repositórios e os identificadores de chaves são substituídos por pseudônimos e que nenhum material de chave, amostra de texto cifrado ou procedimento de exploração jamais sai da Meridian. Os achados ficam num servidor cifrado da universidade, com os acessos registrados. O comitê de ética também exige uma regra de escalonamento: qualquer uso indevido de alta severidade não corrigido que Nadia perceber durante o estudo vai para o líder de segurança da Meridian em até um dia útil, qualquer que seja o braço do estudo.

### 1.5 Validade desde o início

Nadia separa três questões de validade antes de coletar dados reais. A validade de construto pergunta se "uso indevido confirmado a cada dez mudanças integradas" captura o que os criptógrafos entendem por segurança enfraquecida; ela confere o livro de códigos com dois engenheiros de segurança da Meridian e contra os modos de falha listados no SP 800-57 Part 1 para o gerenciamento de chaves. A validade interna pergunta se qualquer diferença vem do checklist, e não da habilidade das equipes, o que motiva a atribuição aleatória das equipes mais adiante. A validade externa pergunta se os resultados de uma empresa de pagamentos com bibliotecas maduras se transferem para pequenas startups, o que ela vai argumentar com cautela, em vez de pressupor.

### Exemplo resolvido

Nadia escreve a pergunta, o livro de códigos com quatro categorias e o acordo de divulgação e depois executa o exercício de concordância com 48 itens. Um kappa de 0,802 e uma deriva clara para primitive-choice levam a uma nova regra de sobreposição antes da codificação real.

> **Caso sintético.** A Larkspur, a Meridian e todos os achados são inventados; o SP 800-38D, o SP 800-57 e Landis e Koch são reais.

### Erros e limites

O kappa resume a concordância, mas esconde onde está a discordância; sempre tabule as células fora da diagonal. Uma concordância alta também não prova que as categorias são as certas, apenas que duas pessoas as aplicam da mesma forma.

### Exercícios

- **EX001 — Pergunta de pesquisa.** Enuncie numa frase a pergunta de pesquisa de Nadia. *Rubrica:* 3 = se checklist mais lint reduz o uso indevido confirmado a cada dez mudanças integradas em relação à revisão habitual;; 2 = checklist versus habitual sem a medida;; 1 = "criptografia melhor" vago;; 0 = nenhuma.

- **EX002 — Definir o uso indevido.** Como o livro define o uso indevido de criptografia, e por que a regra do nonce do GCM é um exemplo? *Rubrica:* 3 = primitiva correta usada de modo que sua garantia falha; reutilizar o nonce sob uma chave anula a segurança do GCM segundo o SP 800-38D;; 2 = só a definição;; 1 = "algoritmo fraco";; 0 = nenhuma.

- **EX003 — Números da concordância.** Informe a concordância observada, a concordância ao acaso e o kappa do laboratório. *Rubrica:* 3 = 0,854, 0,263, 0,802;; 2 = só o kappa;; 1 = errado mas plausível;; 0 = nenhuma.

- **EX004 — Padrão de deriva.** Que categoria absorveu a maioria das discordâncias, e que regra Nadia acrescentou? *Rubrica:* 3 = primitive-choice (5 de 7); derivação de chave é key-handling, a menos que o algoritmo esteja obsoleto;; 2 = só a categoria;; 1 = só a regra;; 0 = nenhuma.

- **EX005 — Condição de compartilhamento.** Sob que condição a Meridian pode compartilhar um achado com Nadia? *Rubrica:* 3 = só depois que a correção for implantada ou o código desativado, com pseudônimos;; 2 = após a correção;; 1 = a qualquer momento;; 0 = nenhuma.

- **EX006 — Dever de escalonamento.** O que Nadia deve fazer se vir um uso indevido de alta severidade não corrigido? *Rubrica:* 3 = avisar o líder de segurança da Meridian em até um dia útil, qualquer que seja o braço;; 2 = relatar;; 1 = anotar nos dados;; 0 = nenhuma.

- **EX007 — Ameaça à validade interna.** Cite a ameaça à validade interna e o remédio planejado. *Rubrica:* 3 = a habilidade das equipes confunde o efeito; randomizar as equipes;; 2 = só a ameaça;; 1 = viés genérico;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Criptografia e serviços de confiança: fronteira da pesquisa

### Objetivos de aprendizagem

Você vai (1) mapear a fronteira da pesquisa sobre criptografia usável e resistente a uso indevido; (2) quantificar um risco de uso indevido a partir do limite declarado numa norma; (3) posicionar uma questão original em relação ao que as normas já resolvem.

### 2.1 O que está resolvido

A segurança das primitivas, em grande parte, não é a questão de Nadia. O AES é especificado no FIPS 197, o SHA-2 no FIPS 180-4, o HMAC no FIPS 198-1 e as assinaturas digitais no FIPS 186-5 e na RFC 8032. Boneh e Shoup apresentam as provas por redução que tornam essas escolhas defensáveis, e Katz e Lindell mostram como a cifração autenticada compõe confidencialidade e integridade. Uma tese que voltasse a litigar esses resultados acrescentaria pouco. O que continua em aberto é a distância entre uma primitiva provada e o código que a chama: parâmetros, nonces, armazenamento de chaves e a cola dos protocolos. É nessa distância que as auditorias da Meridian continuam encontrando problemas, e é ali que Nadia situa sua contribuição.

### 2.2 Limites de nonce como risco mensurável

As normas muitas vezes expressam o risco de uso indevido como um limite de uso. O SP 800-38D exige que, quando nonces de 96 bits do GCM são gerados aleatoriamente, uma única chave cifre no máximo 2^32 mensagens, porque nonces aleatórios acabam colidindo, e uma colisão expõe o XOR de dois textos claros e permite a falsificação da tag de autenticação. A aproximação do aniversário dá a chance de pelo menos uma repetição entre q sorteios aleatórios de 2^96 valores como aproximadamente q²/2^97. O laboratório calcula essa probabilidade para três volumes sintéticos, para mostrar por que a política de rotação, e não a cifra, é a variável controlável.

### Laboratório — Risco de colisão de nonces aleatórios

```python
"""Birthday-bound estimate for random 96-bit AES-GCM nonces under one key (synthetic volumes)."""
import math

def p_collision(q, bits=96):
    # P(at least one repeat among q uniform draws from 2**bits values) ~ 1 - exp(-q(q-1)/2^(bits+1))
    return -math.expm1(-q * (q - 1) / 2 ** (bits + 1))

def main():
    for label, q in [("pilot service, 1e6 msgs", 10**6), ("busy queue, 2^32 msgs", 2**32),
                     ("unrotated key, 2^40 msgs", 2**40)]:
        print(f"{label:<26} P(repeat) = {p_collision(q):.3e}")
    q = 2**32
    print(f"2^32 limit -> about 1 in {1 / p_collision(q):,.0f}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_nonce.py`. Saída verificada:

```text
pilot service, 1e6 msgs    P(repeat) = 6.311e-18
busy queue, 2^32 msgs      P(repeat) = 1.164e-10
unrotated key, 2^40 msgs   P(repeat) = 7.629e-06
2^32 limit -> about 1 in 8,589,934,594
```

### 2.3 Ler a curva

Com um milhão de mensagens, a probabilidade de repetição é de cerca de 6 × 10^-18, desprezível. No limite de 2^32, é de cerca de 1,2 × 10^-10, aproximadamente uma chance em 8,6 bilhões, que a norma trata como o teto aceitável. Uma fila sintética que nunca rotaciona sua chave e chega a 2^40 mensagens sobe para cerca de 7,6 × 10^-6, um risco que nenhum regulador de pagamentos aceitaria para uma única chave. Nadia tira a lição para a pesquisa: a cifra era a mesma nas três linhas. A diferença veio da disciplina operacional, isto é, contar as invocações e rotacionar as chaves, que é exatamente o comportamento que um checklist e uma etapa de lint poderiam plausivelmente mudar.

### 2.4 Trabalhos sobre resistência a uso indevido e usabilidade

A fronteira inclui duas respostas ao uso indevido. Uma projeta primitivas que falham de forma mais suave, como os modos resistentes ao uso indevido de nonce (nonce-misuse-resistant), de modo que um nonce repetido vaze apenas a igualdade das mensagens, em vez de quebrar a autenticidade. A outra estuda os desenvolvedores e as ferramentas, perguntando se as interfaces das bibliotecas, a documentação ou os auxílios à revisão mudam o comportamento. O estudo de Nadia pertence à segunda linha. Na revisão de literatura, ela tem o cuidado de citar apenas trabalhos que leu e verificou, e de registrar para cada artigo sua população, sua medida de uso indevido e se mediu código entregue ou tarefas de laboratório, porque essas escolhas limitam a comparação.

### 2.5 Posicionar a contribuição

A partir da revisão da fronteira, Nadia escreve um parágrafo de posicionamento. Estudos de laboratório mostram que os desenvolvedores usam mal as bibliotecas sob pressão de tempo, mas poucos medem o uso indevido confirmado em mudanças de produção entregues, com atribuição aleatória. Sua contribuição é um estudo de campo randomizado dentro de uma organização, medido por uma contagem auditada a cada dez mudanças integradas, com um livro de códigos e um arquivo de análise públicos. Ela também declara o que não vai afirmar: não vai afirmar que o checklist impede todo uso indevido, nem que os resultados se transferem para empresas sem bibliotecas avaliadas. Dizer o que está fora do escopo mantém os examinadores concentrados nas evidências que ela consegue produzir.

### Exemplo resolvido

Nadia tabula as três linhas de volume de nonces, liga o limite de 2^32 ao SP 800-38D e argumenta que a disciplina de rotação é o comportamento que sua intervenção visa.

> **Caso sintético.** Os volumes de mensagens pertencem a uma fila inventada; o limite de 2^32 é a regra real do SP 800-38D.

### Erros e limites

A fórmula do aniversário é uma aproximação válida apenas para nonces aleatórios; nonces baseados em contador têm outros modos de falha, principalmente a perda de estado após reinicializações. Nunca trate uma probabilidade minúscula como permissão para pular a rotação.

### Exercícios

- **EX008 — Terreno resolvido.** Que questões Nadia trata como resolvidas, e que lacuna aberta ela estuda? *Rubrica:* 3 = segurança das primitivas (FIPS 197, 180-4, 186-5) resolvida; a distância entre a primitiva e o código que a chama, aberta;; 2 = só a lacuna;; 1 = "nova cifra";; 0 = nenhuma.

- **EX009 — Teto de uso do GCM.** Que limite de uso o SP 800-38D fixa para nonces aleatórios de 96 bits, e por quê? *Rubrica:* 3 = no máximo 2^32 mensagens por chave, porque colisões vazam o XOR dos textos claros e permitem falsificação;; 2 = só o limite;; 1 = "rotacionar sempre";; 0 = nenhuma.

- **EX010 — Probabilidade no teto.** Que probabilidade de repetição o laboratório relatou em 2^32 mensagens? *Rubrica:* 3 = cerca de 1,164e-10, cerca de 1 em 8,6 bilhões;; 2 = ordem de grandeza;; 1 = outra linha;; 0 = nenhuma.

- **EX011 — Fila sem rotação.** O que a linha de 2^40 mostrou, e que lição decorre dela? *Rubrica:* 3 = cerca de 7,6e-6; a rotação operacional, e não a cifra, determina o risco;; 2 = só o número;; 1 = só a lição;; 0 = nenhuma.

- **EX012 — Duas respostas da fronteira.** Cite as duas respostas da pesquisa ao uso indevido e diga a qual Nadia se junta. *Rubrica:* 3 = primitivas resistentes a uso indevido vs estudos de desenvolvedores/ferramentas; ela se junta às ferramentas;; 2 = as duas citadas;; 1 = uma;; 0 = nenhuma.

- **EX013 — Registro da literatura.** Que três fatos Nadia registra para cada artigo que revisa? *Rubrica:* 3 = população, medida de uso indevido, código entregue vs tarefa de laboratório;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX014 — Afirmação de escopo.** Dê uma afirmação que Nadia explicitamente se recusa a fazer. *Rubrica:* 3 = que o checklist impede todo uso indevido, ou que os resultados se transferem para empresas sem bibliotecas avaliadas;; 2 = limite vago;; 1 = sem relação;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Proposta de contribuição original

### Objetivos de aprendizagem

Você vai (1) escrever hipóteses falseáveis para um estudo de redução do uso indevido; (2) escolher um desfecho primário e a análise antes de ver os dados; (3) registrar o plano para que mudanças posteriores fiquem visíveis.

### 3.1 Da pergunta às hipóteses

Nadia transforma sua pergunta numa hipótese primária e numa secundária. A H1 afirma que as equipes que usam o checklist e a etapa de lint terão, ao longo de um trimestre, uma média menor de achados confirmados de uso indevido a cada dez mudanças integradas do que as equipes que usam a revisão habitual. A H2 afirma que uma parcela maior das equipes com checklist registrará zero uso indevido naquele trimestre. As duas são direcionais e falseáveis: uma diferença nula ou invertida conta contra elas. Ela também escreve uma expectativa nula para a ferramenta de lint sozinha, porque os examinadores vão perguntar se uma ferramenta barata, e não a atenção humana, explica algum efeito.

### 3.2 Escolher o desfecho

O desfecho primário é o uso indevido confirmado a cada dez mudanças integradas que tocam código criptográfico, medido por equipe. Confirmação significa que um auditor cego, que não sabe o braço, concorda que a mudança viola uma regra do livro de códigos. Nadia rejeita duas alternativas tentadoras. Os avisos do lint recompensariam a ferramenta por sinalizar seus próprios padrões, e os incidentes seriam raros demais para medir num trimestre. Ela define "toca código criptográfico" de forma mecânica, como qualquer mudança que importe o wrapper criptográfico aprovado da Meridian ou os módulos da biblioteca padrão hashlib, hmac ou secrets, para que a inclusão não dependa de julgamento.

### 3.3 Desenho e poder estatístico

Há vinte e quatro equipes disponíveis, então Nadia planeja um desenho randomizado por conglomerados com doze equipes por braço, estratificado por linha de produto, para que as equipes de tokenização, de webhooks e de armazenamento apareçam nos dois braços. A randomização no nível da equipe evita a contaminação, já que os engenheiros de uma equipe compartilham hábitos de revisão. Ela estima o poder a partir da linha de base que vai medir no capítulo 4 e declara a limitação honesta: com doze conglomerados por braço, só efeitos grandes são detectáveis com confiabilidade. Por isso, ela se compromete de antemão com um teste de permutação, que não pressupõe normalidade e se adapta a poucos conglomerados.

### 3.4 Registro e plano de análise

Antes que exista qualquer dado de desfecho, Nadia deposita um plano com carimbo de tempo no escritório de pesquisa da universidade. Ele lista as hipóteses, os desfechos primário e secundário, a regra de inclusão, a política de semente da randomização, o teste de permutação com 20.000 embaralhamentos e a regra para tratar equipes que saiam da Meridian. Também lista o que contaria como desvio. O registro não é burocracia por si mesma: permite que os examinadores distingam os resultados confirmatórios dos exploratórios e protege Nadia da tentação de trocar de desfecho quando o primeiro decepcionar.

### 3.5 Riscos para a parceira

A proposta também protege a Meridian. O checklist nunca pede que os revisores testem explorações; ele faz perguntas como se cada chave do GCM tem um contador de invocações e um gatilho de rotação, se as chaves vêm de um serviço gerenciado de chaves, e não do código-fonte, e se o armazenamento de senhas usa uma função com alto custo de memória (memory-hard), como o Argon2 da RFC 9106. As equipes de controle mantêm sua revisão habitual, então nenhuma equipe recebe proteção mais fraca do que antes. O dever de escalonamento do capítulo 1 continua valendo nos dois braços, e o líder de segurança pode interromper o estudo se algum braço causar dano.

### Exemplo resolvido

O registro de uma página de Nadia enuncia H1 e H2, o desfecho a cada dez mudanças que tocam criptografia, o desenho estratificado por conglomerados de 12 contra 12 e o teste de permutação, e depois é depositado com carimbo de tempo antes que os dados da linha de base sejam revelados.

> **Caso sintético.** O escritório de registro e o checklist são inventados para fins didáticos; a RFC 9106 e o SP 800-38D são referências reais para os itens do checklist.

### Erros e limites

O registro não conserta uma medida de desfecho fraca, e um número pequeno de conglomerados limita o poder, qualquer que seja o teste. Relate os desvios abertamente, em vez de emendar o plano em silêncio.

### Exercícios

- **EX015 — Hipótese primária.** Escreva a H1 com precisão. *Rubrica:* 3 = as equipes com checklist+lint têm média menor de uso indevido confirmado a cada dez mudanças integradas que tocam criptografia ao longo de um trimestre;; 2 = direção sem unidade;; 1 = sem direção;; 0 = nenhuma.

- **EX016 — Desfechos rejeitados.** Por que Nadia rejeitou os avisos do lint e os incidentes como desfechos? *Rubrica:* 3 = os avisos recompensam os próprios padrões da ferramenta; os incidentes são raros demais num trimestre;; 2 = um motivo;; 1 = vago;; 0 = nenhuma.

- **EX017 — Regra de inclusão.** Como é definido "toca código criptográfico"? *Rubrica:* 3 = a mudança importa o wrapper criptográfico aprovado, hashlib, hmac ou secrets;; 2 = importa criptografia;; 1 = julgamento do revisor;; 0 = nenhuma.

- **EX018 — Escolha dos conglomerados.** Por que randomizar equipes, e não mudanças individuais? *Rubrica:* 3 = os engenheiros de uma equipe compartilham hábitos, então a atribuição por mudança contamina os braços;; 2 = contaminação citada;; 1 = conveniência;; 0 = nenhuma.

- **EX019 — Conteúdo registrado.** Liste quatro itens do plano registrado. *Rubrica:* 3 = quatro entre hipóteses, desfechos, regra de inclusão, política de semente, teste de permutação, regra de atrito, definição de desvio;; 2 = três;; 1 = um ou dois;; 0 = nenhuma.

- **EX020 — Item de senhas do checklist.** O que o checklist pergunta sobre o armazenamento de senhas, e que fonte o apoia? *Rubrica:* 3 = função memory-hard como o Argon2, RFC 9106;; 2 = Argon2 sem fonte;; 1 = "fazer hash das senhas";; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Replicação da linha de base e piloto

### Objetivos de aprendizagem

Você vai (1) medir uma taxa de uso indevido de linha de base a partir de uma auditoria histórica; (2) conduzir um piloto que testa procedimentos, e não efeitos; (3) revisar os instrumentos antes do estudo principal.

### 4.1 Por que primeiro uma linha de base

Uma linha de base diz a Nadia quão comum já é o uso indevido, o que molda o poder estatístico, e replica uma afirmação em que a Meridian acredita, mas nunca conferiu: a de que sua biblioteca wrapper tornou o uso indevido raro. Dois auditores, cegos em relação ao estudo que virá, revisam uma amostra aleatória de 80 mudanças integradas no ano anterior que tocam criptografia, usando o livro de códigos do capítulo 1 com sua nova regra de sobreposição. Cada achado confirmado é ligado a um identificador pseudonimizado da mudança. Nada da amostra é compartilhado fora da Meridian até que as correções de eventuais problemas em aberto tenham sido implantadas.

### Laboratório — Auditoria de linha de base

```python
"""Baseline count of confirmed crypto-misuse in 80 synthetic merged changes (read-only)."""
from collections import Counter
# (change id, confirmed misuse category or None) -- synthetic audit of last year's merges
CHANGES = ([("nonce-iv")] * 7 + [("key-handling")] * 9 + [("primitive-choice")] * 5 +
           [("other")] * 2 + [None] * 57)

def main():
    c = Counter(x for x in CHANGES if x)
    n = len(CHANGES); m = sum(c.values())
    print(f"changes {n}, with confirmed misuse {m} ({100 * m / n:.1f}%)")
    for k, v in c.most_common():
        print(f"  {k:<17} {v}")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_baseline.py`. Saída verificada:

```text
changes 80, with confirmed misuse 23 (28.8%)
  key-handling      9
  nonce-iv          7
  primitive-choice  5
  other             2
```

### 4.2 Ler a linha de base

Vinte e três de oitenta mudanças, 28,8 por cento, contêm pelo menos um uso indevido confirmado. Key-handling lidera com nove, seguido por nonce-iv com sete, primitive-choice com cinco e other com dois. A replicação, portanto, derruba a crença da Meridian: o wrapper reduziu alguns erros de algoritmo, mas as chaves ainda acabam em arquivos de configuração, e os nonces ainda às vezes são derivados de carimbos de tempo. Nadia registra a taxa como cerca de 2,9 achados a cada dez mudanças para fins de planejamento, observando que uma mudança pode conter vários achados e que seu desfecho primário conta achados, e não mudanças.

### 4.3 Planejar a partir da linha de base

Com uma média de controle perto de 1,5 a 2 achados a cada dez mudanças, por equipe, por trimestre, Nadia julga que uma redução pela metade seria detectável com doze equipes por braço, mas uma redução de 20 por cento não. Ela escreve isso num adendo ao registro, com carimbo de tempo anterior ao início do estudo principal, para que os examinadores vejam que a aritmética do planejamento não foi ajustada depois. Ela também observa que a distribuição é assimétrica, com muitos zeros, outro motivo pelo qual o teste de permutação pré-registrado se ajusta melhor aos dados do que um teste t.

### 4.4 O piloto

Duas equipes voluntárias, excluídas do estudo principal, usam o checklist e a etapa de lint por quatro semanas. O piloto faz apenas perguntas de procedimento. Os revisores preenchem o checklist? A regra de lint para nonces constantes dispara nas chamadas ao wrapper? O auditor cego consegue confirmar os achados sem ver qual braço os produziu? Os revisores preenchem 31 de 34 checklists. A regra de nonce produz falsos positivos nos fixtures de teste, que usam nonces fixos de propósito, com chaves descartáveis. Um auditor adivinha o braço pelos comentários do checklist deixados nas descrições de merge, um vazamento do cegamento.

### 4.5 Revisões antes do estudo principal

Nadia faz três mudanças e registra cada uma como revisão anterior ao estudo. A regra de lint ignora os arquivos sob diretórios de teste, o que fica documentado para que os examinadores possam julgar o trade-off. As respostas do checklist saem das descrições de merge para um formulário separado que o auditor nunca vê, fechando o vazamento do cegamento. Uma pergunta do checklist sobre a rotação de chaves é reescrita depois que os revisores leram "rotação" como rotação de logs do sistema de arquivos. Ela deliberadamente não calcula um efeito a partir do piloto, porque duas equipes não aleatórias ao longo de quatro semanas não conseguem estimá-lo, e um número tentador poderia enviesar as escolhas posteriores.

### Exemplo resolvido

A partir da linha de base, Nadia relata 23 de 80 mudanças com uso indevido, key-handling em primeiro, e planeja para uma redução pela metade; a partir do piloto, corrige o falso positivo dos fixtures de teste, o vazamento do cegamento e uma pergunta ambígua.

> **Caso sintético.** As 80 mudanças auditadas e as duas equipes do piloto são inventadas para fins didáticos.

### Erros e limites

Uma amostra histórica de um ano pode subcontar o uso indevido que os auditores não conseguiam ver, como chaves definidas nos ambientes de implantação. Os pilotos testam a viabilidade; relatar efeitos de piloto como evidência é um erro comum.

### Exercícios

- **EX021 — Taxa de linha de base.** Que parcela das mudanças auditadas continha uso indevido? *Rubrica:* 3 = 23 de 80, 28,8 por cento;; 2 = só a porcentagem;; 1 = contagem de achados por categoria;; 0 = nenhuma.

- **EX022 — Categoria líder.** Que categoria liderou a linha de base, e com quantos achados? *Rubrica:* 3 = key-handling, 9;; 2 = só a categoria;; 1 = nonce-iv;; 0 = nenhuma.

- **EX023 — Crença testada.** Que crença da Meridian a linha de base não conseguiu replicar? *Rubrica:* 3 = que a biblioteca wrapper tornou o uso indevido raro;; 2 = wrapper eficaz;; 1 = genérica;; 0 = nenhuma.

- **EX024 — Efeito detectável.** Que tamanho de efeito Nadia julgou detectável, e qual não? *Rubrica:* 3 = redução pela metade detectável, redução de 20 por cento não, com 12 equipes por braço;; 2 = um;; 1 = "grande";; 0 = nenhuma.

- **EX025 — Achados do piloto.** Cite os três problemas que o piloto expôs. *Rubrica:* 3 = falsos positivos de nonce nos fixtures de teste, vazamento do cegamento pelos comentários de merge, pergunta ambígua sobre rotação;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX026 — Nenhum efeito de piloto.** Por que Nadia se recusa a estimar um efeito a partir do piloto? *Rubrica:* 3 = duas equipes não aleatórias em quatro semanas não conseguem estimá-lo, e um número poderia enviesar as escolhas;; 2 = pequeno demais;; 1 = esqueceu;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX026 (as de EX027–EX050 estão na edição em inglês até a tradução dos capítulos correspondentes). Nadia Haddad, o Prof. Oskar Brandt, a Larkspur University, a Meridian Payments Cooperative e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Acrescentar um checklist de uso indevido de criptografia e lint automatizado à revisão reduz os achados confirmados de uso indevido a cada dez mudanças integradas, em comparação com a revisão habitual da Meridian?

**EX002.** Uso indevido é uma primitiva correta usada de modo que sua garantia deixa de valer; reutilizar um nonce do GCM sob uma mesma chave quebra a confidencialidade e a autenticidade que o SP 800-38D promete.

**EX003.** Observada 0,854 (41 de 48), ao acaso 0,263, kappa 0,802.

**EX004.** Primitive-choice recebeu cinco das sete discordâncias; a nova regra codifica a derivação de chave como key-handling, a menos que o próprio algoritmo esteja obsoleto.

**EX005.** Só depois que a correção for implantada ou o código desativado, e com os nomes de repositórios e os identificadores de chaves pseudonimizados.

**EX006.** Escalá-lo ao líder de segurança da Meridian em até um dia útil, independentemente do braço do estudo em que a equipe está.

**EX007.** Diferenças de habilidade entre as equipes poderiam explicar os resultados; a atribuição aleatória das equipes aos braços controla isso.

**EX008.** A segurança das primitivas padrão, como o AES, o SHA-2 e as assinaturas digitais do FIPS 186-5, está resolvida; a lacuna aberta é como o código das aplicações escolhe parâmetros, nonces e armazenamento de chaves ao chamá-las.

**EX009.** No máximo 2^32 invocações por chave, porque nonces aleatórios podem colidir, e uma colisão de nonce no GCM revela o XOR dos textos claros e permite que um atacante forje tags.

**EX010.** Cerca de 1,164 × 10^-10, aproximadamente uma chance em 8,6 bilhões.

**EX011.** Cerca de 7,6 × 10^-6 para uma chave usada 2^40 vezes; o risco é determinado pela contagem e pela rotação das chaves, e não pela cifra em si.

**EX012.** Projetar primitivas resistentes a uso indevido, e estudar desenvolvedores, interfaces e ferramentas; o estudo de Nadia está na linha das ferramentas.

**EX013.** A população estudada, como o uso indevido foi medido e se foi observado código entregue ou tarefas de laboratório.

**EX014.** Ela não afirma que o checklist impede todo uso indevido, nem que os achados se generalizam para organizações sem bibliotecas avaliadas.

**EX015.** Ao longo de um trimestre, as equipes que usam o checklist e a etapa de lint terão uma média menor de achados de uso indevido confirmados pelo auditor a cada dez mudanças integradas que tocam criptografia do que as equipes que usam a revisão habitual.

**EX016.** Os avisos do lint mediriam as próprias regras da ferramenta e inflariam seu efeito aparente, enquanto os incidentes reais são infrequentes demais para contar num único trimestre.

**EX017.** Qualquer mudança integrada que importe o wrapper criptográfico aprovado da Meridian ou os módulos hashlib, hmac ou secrets.

**EX018.** Os engenheiros de uma equipe compartilham hábitos de revisão, então atribuir mudanças individuais deixaria a intervenção vazar para as mudanças de controle.

**EX019.** Por exemplo: H1 e H2, o desfecho primário, a regra de inclusão e o teste de permutação com 20.000 embaralhamentos (além da política de semente e das regras de atrito e de desvio).

**EX020.** Se as senhas são armazenadas com uma função memory-hard como o Argon2, conforme especificado na RFC 9106.

**EX021.** Vinte e três de oitenta mudanças amostradas, ou 28,8 por cento.

**EX022.** Key-handling, com nove achados confirmados.

**EX023.** A suposição da Meridian de que sua biblioteca wrapper já tinha tornado raro o uso indevido de criptografia.

**EX024.** Uma redução pela metade da média de controle poderia ser detectada com doze equipes por braço; uma queda de 20 por cento não.

**EX025.** Avisos falsos positivos de nonce nos fixtures de teste, auditores adivinhando o braço pelos comentários do checklist nas descrições de merge e revisores lendo "rotação" de forma errada.

**EX026.** Duas equipes voluntárias ao longo de quatro semanas não são nem aleatórias nem grandes o bastante, e um número precoce poderia direcionar as decisões posteriores.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barnes, R., Bhargavan, K., Lipp, B., & Wood, C. (2022). *Hybrid public key encryption* (RFC 9180). IETF. <https://www.rfc-editor.org/rfc/rfc9180>
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
