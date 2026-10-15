# Segurança Quântica e Pós-Quântica: Uma Primeira Introdução

- Idioma: português do Brasil (`pt`); curso rápido, um mês; aproximadamente 80 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–4 de 4 têm texto didático escrito; os exercícios EX001–EX052 (treze por capítulo) têm as resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, com saídas verificadas. A revisão independente e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: iniciantes sem função de segurança e com letramento digital básico, que querem entender o que a computação quântica significa para a segurança do dia a dia e concluir com segurança uma tarefa guiada.
- Relação com os livros vizinhos: o [livro profissional](../../../../professional-6-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) ensina o fluxo de trabalho completo da migração; o [livro técnico](../../../../technical-18-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) ensina a configuração prática. **Este livro é uma introdução curta e cuidadosa**: as ideias centrais, a prática segura, como mapear aquilo de que uma pequena organização depende e um laboratório guiado.
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação. Não concede autorização para testar sistemas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Quatro capítulos, aproximadamente um por semana: fundamentos e decisões (1), escopo, permissão e prática segura (2), sistemas, dados e dependências (3) e um laboratório guiado com uma breve síntese final (4). Cada capítulo tem objetivos de aprendizagem, ensino em linguagem simples, casos resolvidos, atividades práticas, erros comuns, treze exercícios curtos pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com Python 3 e imprimem os seus resultados para que você possa conferir a sua execução; não é preciso experiência em programação para lê-los.

### O exemplo contínuo: Bluebird Bakery Online

A **Bluebird Bakery Online (BBO)** é uma padaria familiar sintética, com duas lojas, um escritório e uma loja online onde os clientes encomendam bolos. Ela usa uma loja virtual hospedada por um provedor, pagamentos com cartão por meio de uma empresa de pagamentos, um portal dos funcionários, um serviço de transferência de arquivos para receber as listas de preços dos fornecedores, e-mail na nuvem e uma rede Wi-Fi no escritório. A dona, Priya, leu uma notícia sobre computadores quânticos e pergunta a você, o sobrinho dela que está aprendendo sobre segurança, o que isso significa para a padaria. Todos os números sobre a BBO são inventados.

### Política de fontes

As fontes primárias foram verificadas em 12 de outubro de 2026: NIST [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) e [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (agosto de 2024), [NIST IR 8547 (rascunho público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) e [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). As normas mudam; verifique de novo antes de se apoiar nelas.

## Sumário

| Semana | Capítulo |
|---|---|
| 1 | [1 Fundamentos e decisões](#ch-01) |
| 2 | [2 Escopo, permissão e prática segura](#ch-02) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Segurança quântica e pós-quântica: fundamentos e decisões

### Objetivos de aprendizagem

Você vai (1) explicar em palavras simples o que fazem a cifragem e as assinaturas digitais; (2) descrever o que é um computador quântico e o que ele poderia quebrar; (3) explicar "colher agora, decifrar depois" e "forjar depois"; (4) nomear as novas normas pós-quânticas; (5) explicar a proteção híbrida; e (6) tomar uma primeira decisão sensata para uma pequena organização.

### 1.1 Cadeados e selos

Quando você visita uma loja virtual, o seu navegador e a loja combinam uma chave secreta que ninguém mais conhece e depois a usam para embaralhar (cifrar) tudo o que você envia. É como duas pessoas combinarem o segredo de um cofre enquanto estranhos escutam — e ainda assim mantê-lo secreto. O método que lhes permite fazer isso se chama *criptografia de chave pública*. A mesma família de métodos também produz *assinaturas digitais*: selos que provam que uma mensagem, um site ou uma atualização de software veio realmente de quem diz ter vindo. Os métodos de chave pública atuais têm nomes como RSA e curvas elípticas. Uma família diferente, a cifragem *simétrica*, como o AES, faz o grosso do embaralhamento depois que a chave foi combinada.

### 1.2 O que é um computador quântico

Os computadores comuns usam bits que valem 0 ou 1. Os computadores quânticos usam *qubits*, que seguem as regras da física quântica e podem ser combinados de formas que fazem certos cálculos funcionarem de maneira muito diferente. Eles não são simplesmente computadores mais rápidos; para a maioria das tarefas — planilhas, sites, jogos — não trazem benefício algum. Mas, para alguns problemas matemáticos especiais, poderiam ser dramaticamente mais rápidos. Um desses problemas é exatamente aquele em que o RSA e as curvas elípticas se apoiam. Em 1994, Peter Shor descreveu um método quântico (publicado numa revista em 1997) que os quebraria num computador quântico confiável e grande o bastante. Essa máquina ainda não existe, e os especialistas discordam sobre quando, ou se, ela vai existir.

### 1.3 O que quebraria e o que não quebraria

Se fosse construído um computador quântico grande e confiável, ele conseguiria descobrir as chaves secretas por trás da criptografia RSA e de curvas elípticas. Isso permitiria a um atacante ler o tráfego protegido por esses métodos e forjar assinaturas. A cifragem simétrica, como o AES-256, e as impressões digitais (hashes), como o SHA-256, continuariam fortes. Então o problema é específico: as partes de "combinar um segredo" e de "assinar" dos sistemas atuais precisam ser substituídas; a cifragem do grosso dos dados, não.

Para a Bluebird Bakery Online, isso significa que os pagamentos com cartão, as conexões da loja online e os logins no portal dos funcionários poderiam ser afetados um dia, porque dependem da combinação de chaves e de assinaturas. Os próprios arquivos, uma vez cifrados com AES, continuariam seguros. É por isso que as ações posteriores da padaria se concentram nos planos dos provedores para a combinação de chaves e as assinaturas, e não nos seus arquivos armazenados.

### 1.4 Dois tipos de risco com momentos diferentes

*Colher agora, decifrar depois*: alguém grava hoje tráfego embaralhado, guarda-o e o destrava anos depois, quando existir um computador quântico. Isso só importa para informações que precisam permanecer privadas por muitos anos — dados médicos, contratos, documentos de identidade, folha de pagamento. *Forjar depois*: quando existir um computador quântico, alguém poderia falsificar selos digitais — por exemplo, uma atualização de software falsa. Isso importa sobretudo para o que precisa ser confiável por muito tempo.

Na padaria, os arquivos da folha de pagamento e as contas dos clientes são as informações mais expostas ao primeiro risco, porque precisam permanecer privadas por muitos anos. O segundo risco importa para coisas como as atualizações de software dos caixas ou do controlador do forno, que dependem de assinaturas para provar que são genuínas. As confirmações de pedido são úteis apenas por meses, então nenhum dos dois riscos importa muito para elas.

### 1.5 As novas normas

Em agosto de 2024, o National Institute of Standards and Technology (NIST) dos EUA publicou três novas normas projetadas para resistir a computadores quânticos: a [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) (ML-KEM, para combinar chaves secretas), a [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) (ML-DSA, para assinaturas) e a [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (SLH-DSA, também para assinaturas). Elas se chamam *criptografia pós-quântica*: software comum projetado para resistir a ataques quânticos futuros. O NIST também publicou um plano em *rascunho*, o [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd), propondo que os métodos antigos sejam eliminados gradualmente após 2030 e interrompidos após 2035; como é um rascunho, essas datas podem mudar.

### 1.6 Proteção híbrida

Durante a transição, muitos sistemas usam *ao mesmo tempo* um método antigo e um novo, de modo que um atacante teria de quebrar os dois. Isso se chama proteção *híbrida* (a [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) define os termos). Os navegadores modernos e muitos sites já usam um método híbrido chamado X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) para combinar chaves. Se você usa um navegador atualizado, algumas das suas conexões provavelmente já estão protegidas dessa forma.

### 1.7 Decidindo o quanto isso importa: Laboratório M

Uma regra simples de Michele Mosca (2018) ajuda a decidir com o que se preocupar. Some quantos anos uma informação precisa permanecer privada (*x*) a quantos anos leva para mudar os sistemas (*y*). Se esse total for maior que o número de anos até que exista um computador quântico capaz (*z*), a informação já está em risco. Ninguém conhece *z*, então experimente vários palpites.

```python
# Lab M (ch 1): Mosca's inequality x + y > z for synthetic Bluebird Bakery Online data, sweeping z.
assets = [  # (name, shelf-life x in years, migration time y in years) - synthetic
    ("customer accounts", 10, 2), ("supplier contracts", 7, 1), ("order confirmations", 0.5, 1), ("staff payroll files", 12, 2)]
for z in (10, 15, 20):  # years until a cryptographically relevant quantum computer: an assumption, not a forecast
    late = [n for n, x, y in assets if x + y > z]
    print(f"z={z:>2}: at risk now -> {', '.join(late) if late else 'none'}")
```

Saída esperada:

```text
z=10: at risk now -> customer accounts, staff payroll files
z=15: at risk now -> none
z=20: at risk now -> none
```

Com um palpite de dez anos, as contas dos clientes e os arquivos da folha de pagamento estariam em risco; com quinze ou vinte, nada na padaria estaria. A conclusão sensata não é o pânico, e sim: manter o software e os serviços atualizados, para que a padaria se beneficie das novas proteções à medida que os provedores as adotam, e perguntar aos provedores que guardam dados de vida longa quais são os seus planos.

### 1.8 Caso resolvido

Priya pergunta: "Devo comprar uma caixa de segurança 'à prova de quântico' que vi anunciada?" Resposta: "Não. Não existe isso de 'à prova de quântico', e a proteção que importa para nós vem do software que os nossos provedores executam. As novas normas já estão aparecendo nos navegadores e nos serviços web. A nossa tarefa é manter os dispositivos atualizados, usar provedores de boa reputação e perguntar aos que guardam os dados dos clientes e da folha de pagamento quais são os seus planos pós-quânticos."

Repare no que a resposta evita: ela não promete que a padaria está segura e não sugere gastar dinheiro agora. Ela nomeia os dois tipos de dados que mais importam e as pessoas que os controlam. Uma boa primeira decisão para uma pequena organização costuma ser fazer as perguntas certas aos provedores, e não comprar equipamentos.

### 1.9 Atividades práticas

1. Escreva uma explicação de três frases sobre o risco quântico para um amigo que não é da área técnica. 2. Encontre uma notícia sobre computadores quânticos e sublinhe qualquer afirmação que pareça exagerada. 3. Refaça o Laboratório M de cabeça com *z* = 8: quais itens estariam em risco?

Na primeira atividade, teste a sua explicação com o amigo e anote qualquer palavra que ele não tenha entendido. Na segunda, compare as afirmações da notícia com o que você aprendeu aqui: ela diz que toda a cifragem quebra ou dá uma data firme? Na terceira, verifique cada item somando os seus dois números e comparando o total com 8.

### 1.10 Erros comuns

- Dizer que os computadores quânticos "quebram toda a cifragem" — a cifragem simétrica e os hashes continuam fortes.
- Citar uma única data para a chegada dos computadores quânticos.
- Comprar produtos anunciados como "à prova de quântico".
- Tratar datas de rascunho como regras definitivas.

Cada erro tem uma correção curta. Diga quais métodos estão em risco: a combinação de chaves e as assinaturas, não a cifragem do grosso dos dados. Dê faixas para os prazos e diga que são palpites. Pergunte o que um produto realmente faz, em vez de confiar num rótulo. E, quando mencionar as datas de 2030 e 2035, diga que elas vêm de um rascunho.

### Exercícios

- **EX001 — Cadeado e selo.** Em uma frase cada, explique o que fazem a cifragem e uma assinatura digital. Rubrica: 3 = ambas corretas e simples.
- **EX002 — Não é um notebook mais rápido.** Explique por que um computador quântico não deixaria mais rápida a planilha de uma padaria. Rubrica: 3 = só problemas especiais se beneficiam.
- **EX003 — O que quebra.** Quais entre RSA, AES-256, curvas elípticas e SHA-256 um computador quântico grande quebraria? Rubrica: 3 = apenas RSA e curvas elípticas.
- **EX004 — Colher agora.** Descreva "colher agora, decifrar depois" com as suas próprias palavras. Rubrica: 3 = gravar agora, destravar depois, importa para segredos de vida longa.
- **EX005 — Forjar depois.** Dê um exemplo do risco de forjar depois. Rubrica: 3 = atualização ou site assinado falso, explicado.
- **EX006 — Quais dados.** Que dados da padaria precisam de proteção por muitos anos: confirmações de pedido, arquivos da folha de pagamento, o cardápio do dia? Rubrica: 3 = arquivos da folha de pagamento, com o motivo.
- **EX007 — Normas.** Nomeie as três normas pós-quânticas do NIST de 2024 e para que serve cada uma. Rubrica: 3 = FIPS 203, combinação de chaves; 204 e 205, assinaturas.
- **EX008 — Rascunho.** O IR 8547 é uma regra definitiva? Explique em uma frase. Rubrica: 3 = rascunho que propõe datas.
- **EX009 — Híbrido.** Explique a proteção híbrida em uma frase. Rubrica: 3 = antigo e novo juntos, os dois precisam ser quebrados.
- **EX010 — Mosca.** Com *x* = 7 e *y* = 1 (contratos com fornecedores), com quais palpites de *z* eles estariam em risco? Rubrica: 3 = *z* abaixo de 8 anos.
- **EX011 — Mito.** Corrija: "Os computadores quânticos já conseguem ler todo o tráfego da internet." Rubrica: 3 = essa máquina ainda não existe; só alguns métodos são vulneráveis.
- **EX012 — Conselho.** Dê a Priya duas ações sensatas. Rubrica: 3 = atualizações, perguntar aos provedores (ou semelhante).
- **EX013 — À prova de quântico.** Por que alegações de "à prova de quântico" devem deixá-lo cauteloso? Rubrica: 3 = alegação indefinida, sem garantias, marketing.

### Síntese

Os computadores quânticos, se construídos em escala, quebrariam os métodos atuais de combinar chaves e de assinar, mas não a cifragem do grosso dos dados. As novas normas do NIST e a proteção híbrida já estão sendo adotadas. Para a maioria das organizações, a decisão sensata é calma: proteger primeiro as informações de vida longa, manter os sistemas atualizados e perguntar aos provedores sobre os seus planos.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 04

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Escopo, permissão e prática segura

### Objetivos de aprendizagem

Você vai (1) explicar por que a permissão é essencial antes de verificar qualquer sistema; (2) escrever um escopo simples; (3) coletar apenas as informações de que precisa; (4) tratar com responsabilidade o que encontrar; (5) evitar "experimentos" inseguros; e (6) relatar com clareza.

### 2.1 Por que a permissão importa

Olhar como um site ou serviço protege as suas conexões pode parecer inofensivo, e o uso comum — visitar um site no seu navegador — não tem problema. Mas sondar sistemas deliberadamente, executar ferramentas de varredura ou tentar fazer uma conexão usar configurações mais fracas é diferente: sem a permissão do dono, isso pode ser ilegal, pode atrapalhar o serviço e quebra a confiança. Os profissionais sempre têm uma permissão por escrito que diz o que podem fazer. Neste curso, você só vai trabalhar com os seus próprios dispositivos, com os sistemas da padaria mediante o acordo por escrito de Priya e com exemplos de laboratório no seu próprio computador.

### 2.2 Um escopo simples

Um escopo responde a cinco perguntas: *Quais* sistemas posso olhar? *Como* posso olhar (por exemplo, ler configurações, ler documentos, usar o meu navegador normalmente)? *Quando*? *O que* vou fazer com as informações? *A quem* ligo se algo parecer errado? Exemplo: "Com o acordo de Priya em 1º de outubro, posso revisar as páginas de configuração das contas da padaria, a documentação dos provedores e os detalhes de conexão do meu próprio navegador com a loja online entre 1º e 31 de outubro. Vou manter as anotações numa pasta compartilhada que só Priya e eu podemos acessar. Não vou executar ferramentas de varredura nem testar nada no sistema de pagamentos. Se algo parecer errado, vou avisar Priya e a equipe de suporte do provedor."

### 2.3 Coletando apenas o necessário

Para entender a prontidão quântica, você precisa de fatos como qual provedor opera um serviço, quais configurações de segurança ou versões ele usa e por quanto tempo os dados precisam ser guardados. Você não precisa de nomes de clientes, números de cartão, senhas nem do conteúdo das mensagens. Anotar menos é mais seguro: se as suas anotações se perderem, nada sensível vaza.

Na padaria, uma anotação útil poderia dizer: loja online, operada pelo provedor da loja virtual, contas de clientes guardadas por cerca de dez anos. Ela não incluiria o nome nem o endereço de nenhum cliente. Se precisar de um exemplo para explicar algo, invente um, em vez de copiar dados reais.

### 2.4 Tratamento responsável

Se você se deparar com algo sensível ou preocupante — uma senha escrita num post-it, uma pasta compartilhada aberta a todos, um alerta de um provedor —, não explore mais. Avise o dono (Priya) imediatamente e sugira contatar o provedor. Nunca tente "testar" se uma senha encontrada funciona. Se achar que encontrou uma fraqueza no produto de uma empresa, avise a empresa em particular; não publique nada sobre isso.

Anote o que viu, onde e quando, sem copiar o próprio item sensível. Uma anotação como post-it com uma senha no monitor do escritório, 9 de outubro, comunicado a Priya é suficiente. O dono e o provedor decidem o que acontece em seguida; a sua tarefa é avisá-los rapidamente e parar por aí.

### 2.5 Experimentos inseguros

Alguns guias online mostram como forçar uma conexão a usar configurações mais antigas e mais fracas ("downgrade") ou como capturar o tráfego de rede de outras pessoas. Isso só é apropriado em laboratórios isolados, conduzidos por profissionais treinados e com permissão. Neste curso, os laboratórios rodam inteiramente no seu próprio computador, com dados inventados.

Se vir um guia desses, você ainda pode aprender lendo-o, mas não siga os passos em nenhuma rede que use, incluindo o Wi-Fi da padaria. Se um colega ou amigo sugerir tentar um deles, explique que isso poderia derrubar as conexões de outras pessoas e que é preciso primeiro a permissão do dono da rede.

### 2.6 Relatando com clareza

Uma boa anotação diz: o que você olhou, quando, como, o que encontrou, por que isso importa e o que sugere. Exemplo: "8 de outubro, página da conta da padaria no provedor de e-mail (somente leitura): a página de ajuda do provedor diz que as conexões usam TLS moderno e lista a troca de chaves pós-quântica como 'em implantação'. Importa porque os e-mails dos funcionários incluem anexos da folha de pagamento. Sugestão: pedir uma data ao provedor."

Anotações curtas são mais fáceis de usar do que as longas. Escreva cada anotação no dia em que fizer a observação e mantenha a data e a fonte junto dela. Se depois descobrir algo que muda a anotação, acrescente uma correção datada em vez de editar a original, para que Priya possa ver o que se sabia e quando.

### 2.7 Caso resolvido

Um colega diz: "Vamos varrer o Wi-Fi do shopping para ver os dispositivos de quem são vulneráveis ao quântico." A resposta segura: "Não temos permissão, e isso poderia expor dados de outras pessoas. Em vez disso, vamos olhar as configurações dos nossos próprios celulares e ler a documentação pública do provedor do Wi-Fi."

A resposta recusa com educação e oferece uma alternativa segura que ainda ensina algo. Ela também explica o porquê: os dados de outras pessoas e a falta de permissão. Se o colega insistir, o certo é parar e conversar com um professor ou com o dono do local, em vez de discutir.

### 2.8 Atividades práticas

1. Escreva um escopo para revisar as configurações do roteador da sua casa. 2. Liste três informações que você *não* anotaria durante uma revisão. 3. Reescreva uma anotação vaga ("o e-mail está ok, acho") como uma anotação clara.

Na primeira atividade, use as cinco perguntas de escopo vistas antes neste capítulo. Na segunda, pense nas coisas que causariam dano se as suas anotações se perdessem. Na terceira, acrescente à anotação vaga o quê, quando, como e a fonte, e remova a palavra acho.

### 2.9 Erros comuns

- Pensar "é público, então posso testar".
- Anotar senhas ou dados de clientes.
- Investigar mais depois de encontrar algo sensível.
- Publicar fraquezas antes que o dono possa corrigi-las.

Cada erro tem uma correção simples. Público significa que qualquer pessoa pode visitar, não que qualquer pessoa pode testar. As anotações devem conter fatos sobre configurações e provedores, nunca segredos. Encontrar algo sensível é o sinal para parar e avisar o dono. E as fraquezas são comunicadas em particular, para que o dono possa corrigi-las primeiro.

### Exercícios

- **EX014 — Permissão.** Por que é preciso permissão antes de executar uma ferramenta de varredura num site? Rubrica: 3 = legalidade, interrupção, confiança.
- **EX015 — Uso comum.** É aceitável visitar um site no seu navegador e olhar os detalhes do cadeado? Explique. Rubrica: 3 = sim, uso comum; contraste com a sondagem.
- **EX016 — Cinco perguntas.** Liste as cinco perguntas a que um escopo responde. Rubrica: 3 = o quê, como, quando, uso dos dados, a quem ligar.
- **EX017 — Escrever um escopo.** Escreva um escopo para revisar as configurações do portal dos funcionários da BBO. Rubrica: 3 = os cinco elementos.
- **EX018 — Não coletar.** Nomeie três coisas a não coletar. Rubrica: 3 = números de cartão, senhas, conteúdo das mensagens (ou semelhante).
- **EX019 — Senha encontrada.** O que você faz se encontrar uma senha num post-it? Rubrica: 3 = não usar, avisar o dono, sugerir a troca.
- **EX020 — Fraqueza num produto.** Como você deve comunicar uma fraqueza no produto de uma empresa? Rubrica: 3 = em particular à empresa, sem publicação.
- **EX021 — Downgrade.** Por que os experimentos de downgrade não são para este curso? Rubrica: 3 = risco, exigem laboratório isolado e permissão.
- **EX022 — Anotação clara.** Reescreva "loja virtual ok" como uma anotação clara. Rubrica: 3 = o quê, quando, como, constatação, porquê, sugestão.
- **EX023 — Colega.** Responda a um colega que quer varrer um Wi-Fi público. Rubrica: 3 = recusar, motivo, alternativa segura.
- **EX024 — Armazenamento.** Onde devem ser guardadas as anotações da revisão? Rubrica: 3 = pasta compartilhada privada com o dono, não pública.
- **EX025 — Algo errado.** O que você faz se, durante a revisão, um serviço parar de funcionar? Rubrica: 3 = parar, avisar o dono/provedor, anotar o horário.
- **EX026 — Exemplos rotulados.** Por que este livro rotula os exemplos como "sintéticos"? Rubrica: 3 = evitar confusão com organizações reais.

### Síntese

A prática segura começa com a permissão e um escopo claro, coleta apenas o necessário, trata com responsabilidade as descobertas sensíveis, evita experimentos arriscados e relata com clareza.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 04

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Segurança quântica e pós-quântica: sistemas, dados e dependências

### Objetivos de aprendizagem

Você vai (1) listar os serviços de que uma pequena organização depende; (2) anotar que dados cada um guarda e por quanto tempo; (3) identificar quem controla a segurança de cada serviço; (4) registrar os fatos com a sua fonte; (5) tratar as incógnitas como perguntas; e (6) escolher prioridades.

### 3.1 Listando os serviços

Comece pelo que o negócio usa todos os dias: a loja online, os pagamentos com cartão, o e-mail, o portal dos funcionários, as transferências de arquivos com fornecedores, o Wi-Fi do escritório, os caixas da loja e qualquer equipamento conectado, como um controlador de forno. Anote cada um com uma descrição de uma linha.

Inclua coisas fáceis de esquecer porque simplesmente funcionam: o roteador do escritório, as maquininhas de cartão nos caixas e o drive na nuvem onde Priya guarda os recibos. Para cada serviço, anote quem o fornece e para que serve. Uma lista feita em dez minutos com Priya é um bom começo; ela pode ser corrigida depois.

### 3.2 Dados e tempos de vida

Para cada serviço, anote o tipo de dado que ele trata e por quanto tempo esse dado precisa permanecer privado. Na BBO: contas dos clientes (nomes, endereços, histórico de pedidos; guardados por cerca de dez anos para registros fiscais e de fidelidade); arquivos da folha de pagamento (doze anos); contratos com fornecedores (sete anos); confirmações de pedido (úteis por meses). Tempos de vida longos fazem com que "colher agora, decifrar depois" importe mais.

Pergunte a Priya ou ao contador dela por quanto tempo cada tipo de registro precisa ser guardado, em vez de chutar. Anote o tempo de vida em anos ao lado de cada serviço, como o Laboratório M os usa. Esses números determinam as prioridades mais adiante neste capítulo, então um tempo de vida errado pode empurrar um serviço importante para baixo na lista.

### 3.3 Quem controla a segurança

As pequenas organizações raramente operam os seus próprios servidores. O provedor da loja virtual controla as conexões da loja; a empresa de pagamentos controla a segurança dos cartões; o provedor de e-mail controla o e-mail; o fabricante do roteador controla as atualizações do equipamento de Wi-Fi. A BBO controla escolhas como quais provedores usar, manter os dispositivos atualizados e fazer perguntas. Anotar o controlador diz a você a quem perguntar.

Para cada serviço da lista, acrescente uma linha: quem controla a sua segurança e como contatá-lo. Na padaria, a maioria das entradas nomeia um provedor, o que significa que a ação principal é fazer perguntas a ele. Onde Priya controla algo, como atualizar o roteador do escritório, anote isso também.

### 3.4 Registrando os fatos com a sua fonte

Cada fato deve dizer de onde veio: "Página de ajuda do provedor, 8 de outubro", "Página de configurações do roteador, versão 2.1", "Perguntei a Priya". Os fatos tirados da documentação são menos certos do que os que você observou diretamente, como o seu navegador mostrando os detalhes da conexão.

Na padaria, a troca de chaves híbrida da loja online foi vista nos detalhes de conexão do seu próprio navegador, o que é uma evidência mais forte do que uma página de ajuda. A afirmação do provedor de e-mail de que a troca de chaves pós-quântica está em implantação é uma alegação da documentação e deve ser verificada de novo mais tarde. Anote a data ao lado de cada fonte, porque as páginas mudam.

### 3.5 Incógnitas são perguntas

Se você não sabe algo — quais configurações de segurança o controlador do forno usa —, escreva "desconhecido" e transforme isso numa pergunta para a pessoa certa. Desconhecido não é o mesmo que seguro.

Dirija cada pergunta à pessoa que pode respondê-la: o fabricante do controlador do forno, sobre as conexões dele; o provedor da folha de pagamento, sobre os seus planos pós-quânticos. Anote quando enviou a pergunta e quando espera uma resposta. Quando a resposta chegar, substitua o desconhecido pelo fato e pela sua fonte.

### 3.6 Atividade prática — Laboratório J

```python
# Lab J (ch 3): parse a synthetic JSON export of TLS endpoints and summarise key exchange by site.
import json, collections
export = json.loads("""[
 {"site": "shop", "host": "web-01", "group": "X25519MLKEM768"},
 {"site": "shop", "host": "till-02", "group": "secp256r1"},
 {"site": "bakery",  "host": "web-01", "group": "X25519"},
 {"site": "bakery",  "host": "oven-ctl", "group": null},
 {"site": "office","host": "web-01", "group": "X25519MLKEM768"}]""")
summary = collections.defaultdict(collections.Counter)
for e in export:
    g = e["group"]
    kind = "unknown" if g is None else ("hybrid" if "MLKEM" in g else "classical")
    summary[e["site"]][kind] += 1
for prop, c in sorted(summary.items()):
    print(f"{prop:9s} hybrid={c['hybrid']} classical={c['classical']} unknown={c['unknown']}")
```

Saída esperada:

```text
bakery    hybrid=0 classical=1 unknown=1
office    hybrid=1 classical=0 unknown=0
shop      hybrid=1 classical=1 unknown=0
```

O controlador do forno da padaria não tem nenhuma informação registrada, então aparece como desconhecido. O caixa da loja e o servidor web da padaria usam métodos clássicos mais antigos. Os servidores web da loja e do escritório já usam proteção híbrida, provavelmente porque o provedor deles os atualizou.

O Laboratório J agrupa registros de conexão inventados por local e conta cada tipo. Um registro sem grupo é contado como desconhecido, não como seguro. Execute-o e confira se a sua saída coincide; depois altere uma entrada para ver como as contagens mudam.

### 3.7 Escolhendo prioridades

Combine tempos de vida e controle. Primeiro: os serviços que guardam dados de vida longa e sobre os quais a BBO pode influir — pergunte aos provedores da folha de pagamento e do e-mail sobre os seus planos pós-quânticos e mantenha as contas atualizadas. Em seguida: os serviços com incógnitas — pergunte ao fabricante do controlador do forno. Por último: os dados de vida curta, como as confirmações de pedido.

Escreva as prioridades como uma lista numerada curta, com um responsável para cada item, geralmente Priya, e uma data para voltar a verificar. A folha de pagamento e o e-mail vêm primeiro porque os seus dados duram mais e a padaria pode perguntar diretamente aos provedores. A lista deve caber numa página.

### 3.8 Caso resolvido

A lista da BBO (sintético): loja online (provedor; contas dos clientes 10 anos; troca de chaves híbrida vista nos detalhes de conexão do seu navegador, 8 de outubro); serviço de folha de pagamento (provedor; 12 anos; desconhecido — perguntar); e-mail (provedor; anexos da folha de pagamento; "em implantação" — pedir a data); transferência de arquivos com fornecedores (provedor; contratos 7 anos; clássico — perguntar); controlador do forno (fabricante; sem dados pessoais; desconhecido — perguntar sobre atualizações). Prioridades: primeiro as perguntas sobre a folha de pagamento e o e-mail.

A lista mistura fatos e incógnitas, e cada incógnita termina com perguntar, o que a transforma numa tarefa. Ela também registra de onde veio cada fato, como os detalhes de conexão do seu navegador para a loja online. Priya consegue lê-la em dois minutos e ver o que fazer primeiro.

### 3.9 Atividades práticas

1. Liste os serviços de que a sua casa ou um clube do qual você participa depende. 2. Para cada um, anote os dados guardados, o tempo de vida e o controlador. 3. Transforme duas incógnitas em perguntas.

Use as mesmas colunas da lista da padaria: serviço, dados guardados, tempo de vida, quem o controla. Para as incógnitas, escreva uma pergunta dirigida a uma pessoa ou empresa nomeada. Mantenha o resultado privado se ele incluir informações sobre outras pessoas. Peça a alguém da casa ou do clube que confira os seus tempos de vida, já que essa pessoa pode conhecer regras que você não conhece.

### 3.10 Erros comuns

- Esquecer equipamentos como caixas e controladores.
- Tratar desconhecido como seguro.
- Anotar fatos sem fontes.
- Supor que o provedor já resolveu, sem perguntar.

Cada erro tem uma solução simples. Percorra o local para encontrar equipamentos como caixas e controladores. Escreva desconhecido e acrescente uma pergunta. Coloque uma fonte e uma data ao lado de cada fato. E pergunte diretamente aos provedores; um e-mail curto custa pouco e a resposta é útil. Revise a lista com o dono uma vez por ano, ou quando um provedor mudar.

### Exercícios

- **EX027 — Lista de serviços.** Liste seis serviços da BBO. Rubrica: 3 = seis serviços plausíveis.
- **EX028 — Tempos de vida.** Dê os dados e o tempo de vida de três serviços. Rubrica: 3 = pares plausíveis.
- **EX029 — Controlador.** Quem controla a segurança das conexões da loja online? Rubrica: 3 = o provedor da loja virtual.
- **EX030 — Fonte.** Reescreva "o e-mail é seguro contra o quântico" com uma fonte e uma data. Rubrica: 3 = com fonte, datado, redação precisa.
- **EX031 — Desconhecido.** Transforme "controlador do forno: desconhecido" numa pergunta para o fabricante. Rubrica: 3 = pergunta clara e respondível.
- **EX032 — Contagens do Laboratório J.** No Laboratório J, quantos endpoints são híbridos, clássicos e desconhecidos no total? Rubrica: 3 = 2, 2, 1.
- **EX033 — Leitura do Laboratório J.** Qual local precisa de acompanhamento primeiro e por quê? Rubrica: 3 = bakery: servidor web clássico e controlador desconhecido.
- **EX034 — Prioridade.** Por que perguntar primeiro ao provedor da folha de pagamento? Rubrica: 3 = tempo de vida mais longo, controlado pelo provedor.
- **EX035 — Observado vs. documentado.** O que é evidência mais forte: os detalhes de conexão do seu navegador ou uma página de ajuda? Rubrica: 3 = o observado, com justificativa.
- **EX036 — Baixa prioridade.** Por que as confirmações de pedido têm baixa prioridade? Rubrica: 3 = tempo de vida curto.
- **EX037 — Equipamentos.** Por que incluir o caixa e o controlador do forno? Rubrica: 3 = dispositivos conectados podem guardar ou transportar dados, precisam de atualizações.
- **EX038 — Lista de perguntas.** Escreva duas perguntas para o provedor de e-mail. Rubrica: 3 = planos/datas pós-quânticos e o que os clientes devem fazer.
- **EX039 — Casa.** Nomeie um tipo de dado doméstico de vida longa e o seu serviço. Rubrica: 3 = p. ex., registros fiscais num armazenamento na nuvem.

### Síntese

Mapear os serviços, os tempos de vida dos dados e quem controla cada serviço, com fatos acompanhados das fontes e incógnitas transformadas em perguntas, mostra a uma pequena organização onde concentrar os esforços.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 04

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Segurança quântica e pós-quântica: laboratório guiado e síntese aplicada

### Objetivos de aprendizagem

Você vai (1) ler uma auditoria de configuração simples; (2) explicar "oferecido" versus "usado"; (3) verificar, com permissão, se o seu próprio navegador usa proteção híbrida; (4) escrever uma nota de prontidão curta para um dono; (5) listar perguntas para os provedores; e (6) planejar os seus próximos passos de aprendizagem.

### 4.1 O laboratório guiado — Laboratório T

Este laboratório verifica configurações inventadas de quatro serviços da BBO. Ele faz duas perguntas: o serviço oferece o novo método híbrido, e ele o prefere?

```python
# Lab T (ch 4): audit synthetic TLS server configurations for post-quantum key exchange and preference order.
configs = {  # service: ordered list of offered groups (server preference) - synthetic
    "online-shop": ["X25519MLKEM768", "X25519", "secp256r1"],
    "staff-portal": ["X25519", "X25519MLKEM768", "secp256r1"],
    "supplier-sftp": ["ecdh-sha2-nistp256"],
    "till-dashboard": ["X25519", "secp384r1"]}
HYBRID = {"X25519MLKEM768", "SecP256r1MLKEM768", "SecP384r1MLKEM1024"}
for svc, groups in configs.items():
    offered = [g for g in groups if g in HYBRID]
    if not offered: verdict = "CLASSICAL ONLY"
    elif groups[0] in HYBRID: verdict = "OK (hybrid preferred)"
    else: verdict = "WARN hybrid offered but not preferred"
    print(f"{svc:17s} {verdict}")
```

Saída esperada:

```text
online-shop       OK (hybrid preferred)
staff-portal      WARN hybrid offered but not preferred
supplier-sftp     CLASSICAL ONLY
till-dashboard    CLASSICAL ONLY
```

A loja online oferece e prefere o híbrido. O portal dos funcionários oferece o híbrido, mas prefere o método mais antigo, então a maioria das conexões ainda vai usar o mais antigo — como mandar instalar uma fechadura nova e continuar usando a velha por hábito. A transferência de arquivos com fornecedores e o painel dos caixas usam apenas métodos mais antigos.

O laboratório olha apenas a ordem dos grupos em cada configuração inventada. Ele não se conecta a nada, então é seguro executá-lo no seu próprio computador. Experimente mover X25519MLKEM768 para o início da lista do portal dos funcionários e execute-o de novo para ver o veredito mudar.

### 4.2 Oferecido versus usado

Uma configuração que *oferece* o novo método não é o mesmo que conexões que o *usam*. O que importa é o que acontece quando uma conexão é feita. A equipe técnica verifica isso com logs de conexão ou ferramentas; como aprendiz, você pode ver isso no seu próprio navegador.

Na padaria, o portal dos funcionários é o exemplo claro: ele oferece o método híbrido, mas lista o mais antigo primeiro, então a maioria das conexões vai usar o método mais antigo. A sua nota para Priya deve dizer oferecido, mas não preferido, e não protegido.

### 4.3 Verificando o seu próprio navegador (com permissão)

No seu próprio computador, usando um site que você visita normalmente, você pode olhar os detalhes da conexão. Em alguns navegadores, o painel de segurança ou as ferramentas de desenvolvedor mostram a "troca de chaves" usada, e você pode ver X25519MLKEM768 nos sites que usam proteção híbrida. Isso é uso comum do seu próprio navegador — você não está sondando o site. Não use ferramentas de varredura contra sites.

Registre o que viu com a data, o site e onde no navegador você encontrou a informação, e guarde a anotação na pasta compartilhada. Uma captura de tela dos detalhes da sua própria conexão serve. Se o painel mostrar uma troca de chaves mais antiga, simplesmente anote isso; não tente outras ferramentas para descobrir mais.

### 4.4 Escrevendo uma nota de prontidão

Uma nota de prontidão para um dono deve ser curta e calma: o que você olhou, o que encontrou, o que isso significa e o que fazer. Exemplo para Priya:

"Nota de prontidão quântica — Bluebird Bakery Online (sintético), 30 de outubro. O que revisei: a nossa lista de serviços, a documentação dos provedores e a conexão do meu próprio navegador com a nossa loja online. Constatações: a loja online usa a nova proteção híbrida; o nosso portal dos funcionários a oferece, mas não a prefere; as transferências de arquivos com fornecedores e o painel dos caixas usam métodos mais antigos; o provedor da folha de pagamento e o controlador do forno são desconhecidos. O que isso significa: nenhum perigo imediato, mas a folha de pagamento e o e-mail guardam informações que precisam permanecer privadas por muitos anos. Ações sugeridas: pedir aos provedores do portal dos funcionários e da transferência de arquivos que prefiram o novo método; pedir aos provedores da folha de pagamento e do e-mail os seus planos e datas pós-quânticos; manter todos os dispositivos e contas atualizados; revisar de novo em seis meses."

### 4.5 Perguntas para os provedores

Boas perguntas são específicas e respondíveis: "As suas conexões usam troca de chaves pós-quântica ou híbrida (por exemplo, X25519MLKEM768)? Se não, quando vão usar? Quais dos nossos dados vocês guardam, e por quanto tempo? Como vão nos informar sobre mudanças?"

Envie as perguntas por e-mail, para que a resposta fique por escrito, e guarde a resposta com a data. Se um provedor não responder, pergunte de novo depois de algumas semanas. Mantenha as perguntas curtas, para que uma equipe de suporte possa respondê-las sem escalar.

### 4.6 Síntese aplicada

Juntando o mês: agora você consegue explicar o que os computadores quânticos ameaçam e o que não ameaçam (Capítulo 1), trabalhar com segurança e com permissão (Capítulo 2), mapear os serviços, os dados e os controladores de uma pequena organização (Capítulo 3), ler uma auditoria simples e escrever uma nota para o dono (este capítulo). Essa é uma primeira tarefa completa e útil.

O trabalho do mês produz três coisas que a padaria pode guardar: uma lista de serviços com tempos de vida e controladores, uma nota de prontidão e um conjunto de perguntas para os provedores. Juntas, elas permitem que Priya aja sem precisar entender a matemática.

### 4.7 Próximos passos

Se quiser ir além: o curso profissional ensina o fluxo de migração completo; o curso técnico ensina a configuração e a verificação na prática. Acompanhe as notícias de fontes confiáveis, como o NIST, e desconfie das manchetes.

Antes de seguir, verifique se consegue explicar a outra pessoa o que significa colher agora, decifrar depois e por que o AES-256 continua forte. Revise os exercícios em que tirou menos de 3. Guarde a nota de prontidão como exemplo para os próximos cursos. Anote a data em que terminou.

### 4.8 Caso resolvido

Priya lê a nota e pergunta: "Então precisamos gastar dinheiro?" Resposta: "Agora não. As nossas ações principais são e-mails aos provedores e manter tudo atualizado. Se o provedor da folha de pagamento não tiver um plano, podemos considerar trocar de provedor na próxima renovação do contrato."

A resposta mantém a decisão pequena e específica: enviar e-mails, continuar atualizando e rever na renovação do contrato. Se a resposta de um provedor mostrar depois um problema real, a próxima nota de prontidão vai dizer isso, e os gastos poderão ser discutidos então.

### 4.9 Atividades práticas

1. Reescreva a nota de prontidão para a sua casa ou clube. 2. Redija um e-mail a um provedor a partir das perguntas acima. 3. Explique "oferecido versus usado" a um amigo usando uma analogia do dia a dia.

Na primeira atividade, use as mesmas quatro partes da nota da padaria: o que revisou, constatações, o que significa e ações sugeridas. Na segunda, escolha uma pergunta da lista para os provedores e dirija-a a um serviço real que você usa. Na terceira, teste a sua analogia com um amigo. Compartilhe o seu trabalho apenas com pessoas de confiança.

### 4.10 Erros comuns

- Relatar "oferecido" como "usado".
- Varrer sites em vez de olhar o seu próprio navegador.
- Notas alarmistas que pedem gastos sem necessidade.
- Esquecer de definir uma data de revisão.

Cada erro tem uma correção simples. Escreva oferecido, mas não preferido quando é isso que a configuração mostra. Use o seu próprio navegador, nunca ferramentas de varredura. Mantenha o tom calmo e as sugestões de gasto pequenas. Coloque uma data de revisão em cada nota. Pergunte ao dono se a nota ficou clara e melhore a próxima com base na resposta dele.

### Exercícios

- **EX040 — Leitura do Laboratório T.** Qual serviço do Laboratório T oferece o híbrido, mas não o prefere? Rubrica: 3 = staff-portal.
- **EX041 — Apenas clássico.** Quais serviços do Laboratório T usam apenas métodos mais antigos? Rubrica: 3 = supplier-sftp e till-dashboard.
- **EX042 — Analogia.** Dê uma analogia do dia a dia para "oferecido versus usado". Rubrica: 3 = clara e precisa.
- **EX043 — O próprio navegador.** Por que verificar os detalhes de conexão do seu próprio navegador é aceitável, mas varrer um site não é? Rubrica: 3 = uso comum vs. sondagem sem permissão.
- **EX044 — Partes da nota.** Liste as quatro partes de uma nota de prontidão. Rubrica: 3 = revisado, constatações, significado, ações.
- **EX045 — Tom calmo.** Reescreva: "Estamos em enorme perigo por causa dos hackers quânticos!" Rubrica: 3 = calmo, preciso.
- **EX046 — Pergunta ao provedor.** Escreva uma pergunta específica para o provedor do portal dos funcionários. Rubrica: 3 = pede para preferir o híbrido/data.
- **EX047 — Data de revisão.** Por que incluir uma data de revisão? Rubrica: 3 = as normas e os serviços mudam.
- **EX048 — Gastos.** Quando a padaria poderia precisar gastar dinheiro? Rubrica: 3 = o provedor não tem plano → trocar na renovação, ou substituição de dispositivo.
- **EX049 — Nome do híbrido.** Qual é o nome do método híbrido comumente usado nos navegadores? Rubrica: 3 = X25519MLKEM768.
- **EX050 — O que ele não resolve.** Nomeie uma coisa que a troca de chaves híbrida não resolve. Rubrica: 3 = assinaturas/certificados ainda clássicos (ou dados gravados antes).
- **EX051 — Próximo curso.** Qual curso você faria em seguida para aprender configuração, e qual para o fluxo de trabalho? Rubrica: 3 = técnico; profissional.
- **EX052 — Resumo final.** Resuma o mês em três frases. Rubrica: 3 = ameaça, prática segura, mapeamento e ação.

### Síntese

O laboratório guiado mostra a diferença entre oferecer e usar a nova proteção; uma nota de prontidão curta e calma e perguntas específicas aos provedores transformam o aprendizado do mês numa primeira tarefa útil para um dono real.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 04

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. A Bluebird Bakery Online é sintética.

**EX001.** A cifragem embaralha as informações para que só quem tem a chave consiga lê-las. Uma assinatura digital é um selo que prova quem criou uma mensagem ou atualização e que ela não foi alterada.

**EX002.** Os computadores quânticos só ajudam em alguns problemas matemáticos especiais; somar colunas numa planilha não é um deles.

**EX003.** RSA e curvas elípticas. O AES-256 e o SHA-256 continuam fortes.

**EX004.** Alguém grava agora o tráfego embaralhado e o guarda até que um futuro computador quântico consiga destravá-lo; isso importa para informações que precisam permanecer privadas por muitos anos.

**EX005.** Quando existir um computador quântico, um atacante poderia falsificar a assinatura de uma atualização de software para que um dispositivo instale software malicioso.

**EX006.** Os arquivos da folha de pagamento: precisam permanecer privados por muitos anos. As confirmações de pedido e o cardápio do dia, não.

**EX007.** FIPS 203 (ML-KEM) para combinar chaves secretas; FIPS 204 (ML-DSA) e FIPS 205 (SLH-DSA) para assinaturas.

**EX008.** Não: é um rascunho que propõe eliminar gradualmente os métodos antigos após 2030 e interrompê-los após 2035; as datas podem mudar.

**EX009.** A proteção híbrida usa um método antigo e um novo ao mesmo tempo, de modo que um atacante teria de quebrar os dois.

**EX010.** 7 + 1 = 8, então há risco para palpites de *z* abaixo de 8 anos.

**EX011.** Esse computador quântico ainda não existe, e mesmo um futuro só quebraria alguns métodos (combinação de chaves e assinaturas), não toda a cifragem.

**EX012.** Manter os dispositivos e as contas atualizados; perguntar aos provedores que guardam dados de vida longa (folha de pagamento, e-mail) quais são os seus planos pós-quânticos.

**EX013.** "À prova de quântico" não tem um significado acordado, nada é garantido contra todos os ataques futuros, e o termo é muitas vezes marketing.

**EX014.** Varrer sem permissão pode ser ilegal, pode atrapalhar o serviço e quebra a confiança do dono.

**EX015.** Sim: visitar um site e ler os detalhes do cadeado ou da conexão é uso comum; sondar ou varrer o site não é.

**EX016.** Quais sistemas; como; quando; o que você vai fazer com as informações; a quem ligar.

**EX017.** "Com o acordo por escrito de Priya (data), posso ver as páginas de configuração do portal dos funcionários e a documentação do provedor, de 1º a 31 de outubro, somente leitura. As anotações vão para a nossa pasta compartilhada privada. Não vou alterar configurações nem executar ferramentas. Contato: Priya, depois o suporte do provedor."

**EX018.** Números de cartão, senhas, conteúdo das mensagens (ou dados pessoais dos clientes).

**EX019.** Não testá-la; avisar Priya imediatamente; sugerir trocá-la e remover o post-it.

**EX020.** Em particular, ao contato de segurança da empresa, com detalhes; não publicar nada enquanto ela corrige.

**EX021.** Eles podem enfraquecer ou derrubar conexões reais e exigem um laboratório isolado, treinamento e permissão.

**EX022.** "8 de outubro, o meu navegador na loja online da padaria (visita normal): os detalhes da conexão mostram a troca de chaves híbrida X25519MLKEM768. Importa porque as contas dos clientes são guardadas por dez anos. Sugestão: nenhuma ação; verificar de novo em seis meses."

**EX023.** "Não — não temos permissão, e isso poderia expor dados de desconhecidos. Vamos verificar os nossos próprios celulares e ler as informações públicas do provedor."

**EX024.** Numa pasta compartilhada privada que só o dono e você podem acessar, não em contas públicas ou pessoais.

**EX025.** Parar, anotar o horário e o que estava fazendo, e avisar Priya e o provedor.

**EX026.** Para que ninguém confunda exemplos didáticos com fatos sobre organizações reais.

**EX027.** Loja online, pagamentos com cartão, e-mail, portal dos funcionários, transferência de arquivos com fornecedores, Wi-Fi do escritório (também os caixas e o controlador do forno).

**EX028.** Loja online: contas dos clientes, 10 anos. Folha de pagamento: arquivos da folha, 12 anos. Transferência com fornecedores: contratos, 7 anos.

**EX029.** O provedor da loja virtual.

**EX030.** "Segundo a página de ajuda do provedor de e-mail (lida em 8 de outubro), a troca de chaves pós-quântica está 'em implantação'; nenhuma data informada."

**EX031.** "Quais métodos de segurança o controlador do forno usa nas suas conexões e atualizações, e vocês vão fornecer atualizações compatíveis com as novas normas pós-quânticas do NIST?"

**EX032.** Híbridos 2, clássicos 2, desconhecido 1.

**EX033.** O local bakery: o seu servidor web usa apenas um método clássico e o seu controlador do forno é desconhecido.

**EX034.** Os dados da folha de pagamento têm o tempo de vida mais longo (12 anos) e são controlados pelo provedor, então perguntar é a ação principal.

**EX035.** Os detalhes de conexão do seu navegador (observados), porque uma página de ajuda pode estar desatualizada ou ser genérica.

**EX036.** Elas só são úteis por alguns meses, então cópias gravadas não importariam anos depois.

**EX037.** Os dispositivos conectados podem transportar dados e precisam de atualizações de segurança; são fáceis de esquecer.

**EX038.** "Vocês usam troca de chaves pós-quântica ou híbrida nas conexões de e-mail, e a partir de quando?" "Há algo que precisamos fazer do nosso lado?"

**EX039.** Registros fiscais guardados num drive na nuvem (mantidos por muitos anos).

**EX040.** staff-portal.

**EX041.** supplier-sftp e till-dashboard.

**EX042.** Uma fechadura nova e mais forte instalada na porta, mas a família continua trancando só a velha, por hábito.

**EX043.** Olhar o seu próprio navegador é uso comum do seu próprio dispositivo; varrer um site sonda o sistema de outra pessoa sem permissão.

**EX044.** O que revisei; constatações; o que significa; ações sugeridas (mais uma data de revisão).

**EX045.** "Os computadores quânticos do futuro poderiam enfraquecer algumas das proteções atuais. Estamos verificando os planos dos nossos provedores e mantendo os sistemas atualizados."

**EX046.** "Vocês podem configurar o portal dos funcionários para preferir a troca de chaves pós-quântica híbrida (X25519MLKEM768) que ele já oferece, e quando?"

**EX047.** As normas, os provedores e os serviços mudam, então a nota precisa ser atualizada.

**EX048.** Se um provedor que guarda dados de vida longa não tiver plano, considerar trocá-lo na renovação do contrato; ou quando um equipamento antigo precisar ser substituído.

**EX049.** X25519MLKEM768.

**EX050.** Os certificados e as assinaturas dos sites ainda usam métodos mais antigos (e os dados gravados antes da mudança continuam expostos).

**EX051.** O curso técnico para a configuração; o curso profissional para o fluxo de trabalho.

**EX052.** "Os computadores quânticos poderiam um dia quebrar os métodos atuais de combinação de chaves e de assinatura, então os segredos de vida longa importam agora. Trabalhamos apenas com permissão e coletamos pouco. Mapear os serviços, os dados e os provedores da padaria mostrou onde fazer perguntas, e uma nota curta deu a Priya ações calmas e práticas."

## Rota de ensino de quatro disciplinas

Este é o curso introdutório **rápido** para novos aprendizes, acompanhando a sintética **Bluebird Bakery Online (BBO)**: fundamentos e decisões, prática segura, mapeamento de serviços e dependências, e um laboratório guiado com uma nota de prontidão para o dono.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; a situação das normas muda, então verifique de novo.

- IETF RFCs: 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST IR 8547 initial public draft (2024). <https://doi.org/10.6028/NIST.IR.8547.ipd>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
