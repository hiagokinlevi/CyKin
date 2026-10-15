# Segurança Quântica e Pós-Quântica: Métodos de Pesquisa e Prática de Dissertação de Mestrado

- Idioma: português do Brasil (`pt`); curso de mestrado, dois anos; aproximadamente 1.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–8 de 8 têm texto didático escrito, os exercícios EX001–EX050 e as resoluções correspondentes. Revisão independente por especialistas, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: pesquisadores iniciantes com sólida base na área e domínio de métodos de pesquisa, que vão formular uma pergunta, avaliar trabalhos anteriores e produzir resultados reprodutíveis em segurança quântica e pós-quântica. Conhecimento de entrada: o conteúdo de [pós-graduação](../../../../postgraduate-2-years/quantum-post-quantum-security/en/book/PLAN.md) ou de [engenharia](../../../../engineering-5-years/quantum-post-quantum-security/en/book/PLAN.md) desta área, ou equivalente: TLS 1.3, criptografia de chave pública, estatística básica.
- Relação com o [curso de doutorado](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md): o doutorado estuda a descoberta da criptografia vulnerável à computação quântica em toda uma organização. **Este livro estuda a fundo uma pergunta de implantação** — o que acontece com as conexões reais quando se ativa uma troca de chaves híbrida pós-quântica/tradicional (PQ/T) — e ensina, em torno dela, o ciclo completo de uma dissertação de mestrado.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto original, de propriedade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos.
- Limite educacional: não é um título credenciado; não concede autorização para testar nenhuma rede ou produto. Toda organização, log, participante e número de um exemplo resolvido é **sintético**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão do livro](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os oito capítulos acompanham uma única dissertação, da pergunta à defesa. Cada capítulo tem objetivos, seções didáticas, um exemplo resolvido, uma atividade prática (Python 3 offline, só com a biblioteca padrão, quando útil), erros comuns, exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo, delimitado e justificado) e um bloco **Continue estudando**. Tente os exercícios antes de abrir as [resoluções](#worked-results).

### A dissertação sintética: o Fragment Study

A *Larkspur University* (sintética: 30.000 usuários, uma rede de campus com dois caminhos de saída — um caminho direto moderno e um proxy legado com inspeção, usado pela ala do hospital universitário) ativou o grupo híbrido do TLS 1.3 X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) nos navegadores gerenciados. Os chamados ao help desk sobre "sites que não carregam" aumentaram. A pergunta do estudante: **quanto do aumento de handshakes TLS com falha após a ativação do grupo híbrido se deve a mensagens ClientHello que já não cabem num único pacote, em comparação com causas concorrentes, e em quais caminhos de rede?** O corpus fictício de logs se chama **LK-HS-1**; um segundo campus, o *Fenwick College*, fornece os dados de validação. Os codificadores **C1–C2** e os entrevistados **I01–I06** são fictícios.

A pergunta se apoia em experiência pública: quando o Chrome passou a oferecer um compartilhamento de chave híbrido com Kyber, o Google relatou que mensagens ClientHello maiores expuseram bugs em alguns middleboxes e servidores ([Chromium Blog, 2023](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)), e a página comunitária [tldr.fail](https://tldr.fail/) documenta servidores que tratam mal um ClientHello dividido em vários pacotes TCP.

## Sumário

1. [Pergunta de pesquisa e método de revisão da literatura](#ch-01)
2. [Segurança quântica e pós-quântica: seminário avançado](#ch-02)
3. [Desenho do estudo, ética e reprodutibilidade](#ch-03)
4. [Segurança quântica e pós-quântica: explicações concorrentes](#ch-04)
5. [Proposta e piloto](#ch-05)
6. [Coleta e análise de dados](#ch-06)
7. [Redação da dissertação e limitações](#ch-07)
8. [Revisão independente e defesa](#ch-08)
- [Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Pergunta de pesquisa e método de revisão da literatura

### Objetivos de aprendizagem e conexão

Você vai (1) transformar uma reclamação operacional numa pergunta pesquisável; (2) aplicar o teste FINER (viável, interessante, nova, ética, relevante — *feasible, interesting, novel, ethical, relevant*); (3) desenhar uma busca documentada na literatura cobrindo fontes normativas, acadêmicas e de profissionais; e (4) montar uma tabela de evidências. O capítulo parte do seu conhecimento de entrada e prepara o seminário do Capítulo 2.

### 1.1 Da reclamação à pergunta

"O pós-quântico quebrou a internet da ala do hospital" é uma reclamação. Ela mistura uma intervenção (oferecer o X25519MLKEM768), um desfecho (usuários não conseguem carregar sites), uma população (usuários da ala do hospital) e uma causa implícita (a criptografia pós-quântica). Uma pergunta de pesquisa separa esses elementos e faz da causa algo a testar, e não a pressupor. Versão um: *as falhas aumentaram?* — respondível, mas descritiva. Versão dois: *as falhas aumentaram mais no caminho do proxy do que no caminho direto?* — comparativa. Versão três, a pergunta do Fragment Study acima: *quanto do aumento se deve ao tratamento de ClientHello em vários pacotes, e onde?* — explicativa e delimitada. A terceira versão é mais difícil, mas é a que uma dissertação deve tentar, porque pode orientar uma decisão (corrigir o proxy ou reverter o grupo) e pode estar errada.

### 1.2 Por que o tamanho é plausível

Um compartilhamento de chave X25519 tradicional tem 32 bytes. A chave de encapsulamento do ML-KEM-768 tem 1.184 bytes ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), Tabela 3), de modo que o compartilhamento do cliente no X25519MLKEM768 tem 1.216 bytes e o compartilhamento de resposta do servidor — o texto cifrado ML-KEM de 1.088 bytes mais 32 — tem 1.120 bytes (RFC 10024). Um ClientHello que antes cabia num segmento TCP agora muitas vezes precisa de dois. O próprio TLS 1.3 lida com isso (no [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html), os registros podem se estender por vários segmentos), mas um software que lê só o primeiro pacote para tomar uma decisão de roteamento ou de inspeção pode falhar. O mecanismo é específico, o que o torna testável.

### 1.3 FINER

Viável: o proxy e a telemetria dos navegadores da Larkspur já registram os resultados dos handshakes (sintético). Interessante: toda organização que ativa grupos híbridos enfrenta a pergunta. Nova: os relatos públicos são, em sua maioria, de fornecedores ou do navegador como um todo; poucos estudos atribuem as falhas dentro de uma organização testando explicações concorrentes. Ética: os logs podem ser reduzidos a metadados (Capítulo 3). Relevante: a resposta decide entre reverter a proteção quântica e reparar a infraestrutura.

Escreva a verificação FINER na proposta com uma frase de evidência para cada letra, e não apenas um visto. Para a viabilidade, nomeie as fontes de logs e confirme com a equipe de rede que elas guardam os resultados dos handshakes por tempo suficiente. Para a novidade, aponte a tabela de evidências, onde a lacuna na atribuição dentro da organização fica visível.

### 1.4 Uma busca documentada

Pesquise três famílias de fontes separadamente. **Normas**: RFC Editor e IETF datatracker, sobre troca de chaves híbrida no TLS, ML-KEM no TLS e tamanho do ClientHello. **Acadêmicas**: IACR ePrint e as bibliotecas digitais da ACM, do IEEE e da USENIX, com os termos "post-quantum TLS performance", "hybrid key exchange deployment", "middlebox ossification". **Profissionais**: blogs de engenharia de navegadores e de CDNs, que guardam a maior parte das evidências de implantação, mas são escritos por partes interessadas. Registre data, base, expressão de busca e número de resultados de cada busca, para que um leitor possa repeti-la — é o equivalente, no mestrado, a um caderno de laboratório.

### 1.5 Exemplo resolvido: a tabela de evidências

| Fonte | Tipo | Alegação relevante para a pergunta | Evidência | Limite |
|---|---|---|---|---|
| RFC 10024 | Norma | Define os tamanhos dos compartilhamentos híbridos | Especificação | Nada diz sobre taxas de falha |
| Chromium Blog 2023 | Profissional | ClientHello maior expôs bugs de middleboxes | Observação de implantação | Visão de todo o navegador; sem atribuição por rede |
| tldr.fail | Comunidade | Alguns servidores tratam mal o ClientHello dividido | Lista curada | Não é amostra; seleção desconhecida |
| FIPS 203 | Norma | Tamanhos do ML-KEM | Especificação | — |

A tabela revela a lacuna: existem mecanismos e relatos episódicos, mas não existe atribuição dentro de uma organização.

Acrescente uma linha para cada nova fonte conforme a busca avança e mantenha honesta a coluna de limite, mesmo para fontes que apoiam a pergunta. O artigo P-7, discutido no seminário, entraria na tabela com sua alegação de 240% e um limite apontando a taxa de base ausente. Um leitor deve conseguir ver, só pela tabela, por que o estudo é necessário.

### 1.6 Erros comuns e limites

- Deixar que a causa implícita na reclamação vire a hipótese, sem rivais.
- Pesquisar apenas bases acadêmicas num campo em que as evidências de implantação estão em blogs de engenharia.
- Tratar uma lista curada (tldr.fail) como amostra aleatória.
- Buscas não registradas, que não podem ser repetidas.

Cada erro tem uma salvaguarda. Escreva os rivais antes de escolher uma hipótese, como o Capítulo 4 faz com cinco deles. Pesquise os blogs de engenharia como uma família separada, com seus próprios limites. Descreva o tldr.fail como curado, não amostrado. Mantenha um registro de buscas com data, base, expressão e número de resultados de cada execução, para que um examinador possa repeti-la.

### Exercícios — capítulo 1

- **EX001 — Decompor uma reclamação.** Divida "a PQC quebrou o Wi-Fi da biblioteca" em intervenção, desfecho, população e causa implícita. Rubrica: 3 = os quatro elementos mais uma causa rival.
- **EX002 — Três versões.** Escreva versões descritiva, comparativa e explicativa de uma pergunta sobre grupos híbridos e VPNs. Rubrica: 3 = versão explicativa delimitada e testável.
- **EX003 — Aritmética de tamanhos.** Calcule os tamanhos dos compartilhamentos de chave do cliente e do servidor para o SecP384r1MLKEM1024 usando os tamanhos do ML-KEM-1024 da FIPS 203 (chave de encapsulamento e texto cifrado de 1.568 bytes) e um ponto P-384 não comprimido de 97 bytes. Rubrica: 3 = os dois tamanhos corretos, com fontes.
- **EX004 — FINER.** Aplique o FINER à sua própria pergunta. Rubrica: 3 = cada critério argumentado, pelo menos uma fraqueza admitida.
- **EX005 — Registro de buscas.** Escreva um registro de buscas com três bases, expressões e datas. Rubrica: 3 = repetível.
- **EX006 — Tabela de evidências.** Acrescente duas linhas a partir de fontes que você mesmo verificou. Rubrica: 3 = fontes primárias ou claramente rotuladas como de profissionais, limites declarados.
- **EX007 — Enunciado da lacuna.** Escreva a lacuna em uma frase. Rubrica: 3 = nomeia com precisão a evidência ausente.

### Síntese do capítulo

Uma pergunta pesquisável separa intervenção, desfecho, população e causa, apoia-se num mecanismo específico e é sustentada por uma busca repetível em fontes normativas, acadêmicas e de profissionais.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 08

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Segurança quântica e pós-quântica: seminário avançado

### Objetivos de aprendizagem e conexão

Você vai (1) explicar por que o estabelecimento de chaves é migrado antes das assinaturas; (2) descrever a estrutura do ML-KEM e de um combinador híbrido PQ/T no nível necessário para raciocinar sobre a implantação; (3) comparar as famílias pós-quânticas por tamanho e pressuposto; e (4) criticar um artigo de seminário. O capítulo aprofunda o contexto do Capítulo 1 e fundamenta o desenho do estudo do Capítulo 3.

### 2.1 Colete agora, decifre depois

Um adversário que grava tráfego cifrado hoje pode decifrá-lo mais tarde se a troca de chaves cair diante de um futuro computador quântico criptograficamente relevante executando o algoritmo de Shor ([Shor 1997](https://doi.org/10.1137/S0097539795293172)). Com as assinaturas é diferente: forjar uma assinatura depois não ajuda o atacante contra uma sessão que já terminou. Essa assimetria explica por que navegadores e CDNs implantaram primeiro a troca de chaves híbrida e por que o Fragment Study trata de compartilhamentos de chave, e não de certificados. A migração das assinaturas importa para âncoras de confiança e firmware de vida longa, e traz seus próprios problemas de tamanho — as assinaturas ML-DSA-65 têm 3.309 bytes ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) —, mas é uma onda posterior.

### 2.2 O ML-KEM em uma página

O ML-KEM é um mecanismo de encapsulamento de chaves construído sobre o problema module learning-with-errors, uma variante estruturada do LWE ([Regev 2009](https://doi.org/10.1145/1568318.1568324)). Informalmente, a chave pública esconde um vetor secreto atrás de um produto de matriz somado a um ruído pequeno; o encapsulamento produz um texto cifrado do qual só quem detém a chave secreta consegue recuperar uma chave compartilhada de 32 bytes, e uma transformação no estilo Fujisaki–Okamoto dá segurança contra ataques de texto cifrado escolhido. O ML-KEM-512, o -768 e o -1024 visam as categorias de segurança 1, 3 e 5 do NIST. Para a pesquisa de implantação, os fatos essenciais são os tamanhos (chave de encapsulamento de 800/1.184/1.568 bytes; texto cifrado de 768/1.088/1.568 bytes), a velocidade (rápido — muitas vezes mais rápido que o X25519 em código otimizado) e o fato de que a falha de desencapsulamento é possível, mas desprezível nos parâmetros padronizados. A [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) traz as recomendações do NIST para o uso de KEMs.

### 2.3 Combinadores híbridos

Um híbrido PQ/T ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) executa uma troca de chaves pós-quântica e uma tradicional e deriva a chave de sessão de ambas, de modo que o atacante precisa quebrar as duas. No X25519MLKEM768, os dois segredos compartilhados são concatenados — primeiro o ML-KEM, depois o X25519 — e entram no escalonamento de chaves do TLS 1.3 (RFC 10024). O híbrido cobre dois riscos ao mesmo tempo: um futuro computador quântico (coberto pelo ML-KEM) e uma fraqueza inesperada no pressuposto de reticulados, mais novo (coberta pelo X25519). As quebras do Rainbow ([Beullens 2022](https://eprint.iacr.org/2022/214)) e do SIKE ([Castryck e Decru 2022](https://eprint.iacr.org/2022/975)) são o motivo de a segunda proteção ser levada a sério.

### 2.4 Famílias comparadas

| Família | Exemplo | Pressuposto | Chave pública / texto cifrado ou assinatura | Nota de implantação |
|---|---|---|---|---|
| KEM de reticulados | ML-KEM-768 | Module-LWE | 1.184 / 1.088 B | Padrão para híbridos no TLS |
| KEM de códigos | HQC (selecionado em 2025, [IR 8545](https://doi.org/10.6028/NIST.IR.8545)) | Códigos quase-cíclicos | Vários kB | Reserva com pressuposto diferente |
| KEM de códigos | Classic McEliece | Códigos de Goppa | Chaves públicas de centenas de kB | Chaves estáticas de longo prazo, não handshakes |
| Assinatura de reticulados | ML-DSA-65 | Module-LWE/SIS | Chave de 1.952 B / assinatura de 3.309 B | Certificados, assinatura de código |
| Assinatura baseada em hash | SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) | Funções de hash | Chaves pequenas / assinaturas de 7,8–49,9 kB | Conservadora; grande |

### 2.5 Exemplo resolvido: crítica de seminário

O artigo do seminário (estudo sintético "P-7") relata que "a troca de chaves híbrida aumenta a falha de handshake em 240%". Crítica: a taxa de base não é informada (240% de quê?); a comparação é feita entre duas semanas diferentes, com uma atualização do navegador entre elas; as falhas são contadas por tentativa, mas as novas tentativas inflam o número de tentativas; e não há estratificação por caminho. A versão defensável relataria taxas absolutas com intervalos, um controle concorrente e resultados por caminho — que é o desenho do Fragment Study.

Escreva a crítica em quatro parágrafos curtos, um por falha, cada um terminando com a mudança de desenho que a corrigiria. Isso transforma uma lista de reclamações num método e torna visível a ligação com o Fragment Study: taxas de base por 10.000 séries, uma coorte de controle concorrente, séries em vez de tentativas e resultados por caminho de saída.

### 2.6 Erros comuns e limites

- Dizer que a troca de chaves híbrida "torna o TLS seguro contra a computação quântica": certificados e dados armazenados são questões separadas.
- Tratar aumentos relativos sem taxas de base como evidência.
- Supor que o ML-KEM é lento; o problema habitual de implantação é o tamanho, não o processamento.
- Esquecer que as normas do HQC e do FN-DSA ainda estavam em desenvolvimento em 12 de outubro de 2026.

Cada erro tem uma correção concreta nesta dissertação. A troca de chaves híbrida protege apenas o estabelecimento de chaves, e os certificados migram depois. As taxas são relatadas por 10.000 séries, com intervalos de Wilson. O custo do ML-KEM no Fragment Study é o tamanho do compartilhamento de chave, que empurra o ClientHello para além do limite de um segmento. A situação das normas é datada e deve ser verificada de novo antes da entrega.

### Exercícios — capítulo 2

- **EX008 — Por que KEMs primeiro.** Explique a assimetria do "colete agora, decifre depois" em 150 palavras. Rubrica: 3 = assimetria correta e um caso em que as assinaturas são urgentes.
- **EX009 — Fatos do ML-KEM.** Liste os três conjuntos de parâmetros com categorias e tamanhos. Rubrica: 3 = tudo correto, com a FIPS 203 citada.
- **EX010 — Raciocínio sobre o combinador.** Explique por que concatenar os dois segredos compartilhados no escalonamento de chaves obriga o atacante a quebrar ambos. Rubrica: 3 = menciona a derivação de chaves e o pressuposto de que a KDF se comporta bem.
- **EX011 — Escolha de família.** Escolha um KEM para um canal de atualização de firmware com chaves estáticas de vida longa e justifique. Rubrica: 3 = compromisso entre tamanho e pressuposto explícito.
- **EX012 — Criticar o P-7.** Escreva uma crítica de 200 palavras. Rubrica: 3 = taxa de base, fator de confusão e problema de unidade nomeados.
- **EX013 — De relativo para absoluto.** Converta o "aumento de 240%" em termos absolutos, se a taxa de base era de 4,5 por 10.000. Rubrica: 3 = correto (para 15,3 por 10.000) e comentário sobre o significado.

### Síntese do capítulo

O estabelecimento de chaves migra primeiro porque o tráfego gravado pode ser decifrado mais tarde. O ML-KEM é rápido, mas grande; os híbridos cobrem tanto surpresas quânticas quanto clássicas; e as alegações de implantação precisam de taxas de base, controles concorrentes e estratificação.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 08

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Desenho do estudo, ética e reprodutibilidade

### Objetivos de aprendizagem e conexão

Você vai (1) escolher entre desenhos observacionais, quase-experimentais e de bancada de testes; (2) definir desfecho, exposição e unidade de análise; (3) minimizar os dados pessoais em logs de rede; (4) estimar taxas com intervalos honestos; e (5) planejar uma análise reprodutível. O capítulo operacionaliza a pergunta dos Capítulos 1–2 e prepara as explicações concorrentes do Capítulo 4.

### 3.1 Desenhos

Um estudo **observacional antes/depois** compara as taxas de falha antes e depois da mudança; é barato, mas confundido por qualquer outra coisa que tenha mudado. Um **quase-experimento** aproveita uma implantação escalonada: se o grupo híbrido foi ativado primeiro para metade dos navegadores gerenciados, a outra metade é um controle concorrente. Uma **bancada de testes** reproduz os handshakes através de uma cópia do proxy, com e sem o compartilhamento híbrido, e isola diretamente o mecanismo de tamanho, mas não diz com que frequência o mecanismo importa no tráfego real. O Fragment Study combina um quase-experimento de implantação escalonada sobre o LK-HS-1 com uma replicação em bancada — cada um cobre a fraqueza do outro.

### 3.2 Definição das variáveis

Unidade de análise: uma *série de tentativas de conexão* — a primeira tentativa mais as novas tentativas automáticas, em até 10 segundos, para o mesmo host —, para que as novas tentativas não inflem os denominadores. Exposição: se o ClientHello ofereceu o X25519MLKEM768. Desfecho: a série termina sem um handshake concluído. Estratificadores: caminho de saída (direto ou proxy legado), versão do navegador, categoria do destino. Escreva essas definições antes de ver os dados de desfecho.

Guarde as definições no dicionário de dados com a data em que foram fixadas. Mais tarde, o piloto mudou uma delas, definindo a série pelo nome do host em vez do endereço, e essa emenda fica registrada ao lado da redação original.

### 3.3 Ética e minimização

Os logs de handshake contêm endereços IP de clientes e nomes de destinos, que podem revelar condições de saúde (uma ala de hospital) ou comportamentos privados. Minimize na coleta: substitua os endereços dos clientes por um hash com chave, rotacionada mensalmente; guarde os nomes de destino apenas como rótulos de categoria mais um hash com sal; não retenha conteúdo (payload); armazene os logs brutos apenas em sistemas da universidade; obtenha a aprovação do comitê de ética ou do escritório de proteção de dados da universidade; e consulte a equipe de rede sobre o que foi informado aos usuários. As entrevistas com a equipe de help desk (I01–I06) exigem consentimento informado e devem evitar nomear usuários.

### 3.4 Taxas e intervalos

As taxas de falha são proporções pequenas, situação em que o intervalo normal dos livros-texto se comporta mal. O intervalo score de Wilson se comporta bem perto de zero e é fácil de calcular com a biblioteca padrão.

```python
# Lab 3 (synthetic): Wilson 95% intervals for handshake failure rates before/after enabling hybrid.
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
for label, k, n in [("before (x25519 only)", 18, 40000), ("after (hybrid offered)", 61, 40000)]:
    lo, hi = wilson(k, n)
    print(f"{label:24s} {k:3d}/{n} = {1e4*k/n:5.1f} per 10k  95% CI [{1e4*lo:4.1f}, {1e4*hi:4.1f}]")
```

Saída esperada:

```text
before (x25519 only)      18/40000 =   4.5 per 10k  95% CI [ 2.8,  7.1]
after (hybrid offered)    61/40000 =  15.2 per 10k  95% CI [11.9, 19.6]
```

O aumento sintético de 4,5 para 15,2 falhas por 10.000 séries é claro — os intervalos não se sobrepõem —, mas ainda não diz nada sobre o *porquê*. Isso é o Capítulo 4.

O laboratório calcula as taxas para o corpus inteiro, antes da estratificação. Como as duas taxas são pequenas, os intervalos são assimétricos, o que o método de Wilson trata corretamente. Informe contagens e denominadores junto com cada taxa, para que o leitor possa recalcular o intervalo; 18 e 61 falhas em 40.000 séries cada são os números que o Laboratório 4 depois divide por caminho.

### 3.5 Plano de reprodutibilidade

Fixe a análise em código versionado e num dicionário de dados; gere cada número da dissertação a partir de scripts; armazene o conjunto de dados minimizado com uma soma de verificação; registre a política exata do navegador que ativou o grupo e a sua data. O Laboratório 3b, abaixo, também documenta os pressupostos de tamanho por trás do mecanismo, para que o leitor possa recalculá-los.

```python
# Lab 3b: key-share sizes in a TLS 1.3 ClientHello (sizes from FIPS 203 and RFC 10024).
# X25519 share = 32 bytes; ML-KEM-768 encapsulation key = 1184 bytes; ciphertext = 1088 bytes.
BASE_HELLO = 520          # synthetic size of the rest of a typical ClientHello (illustrative)
MSS = 1460                # TCP payload per segment on a 1500-byte Ethernet path, no options
shares = {"x25519 only": 32,
          "X25519MLKEM768": 1184 + 32,
          "X25519MLKEM768 + x25519": 1184 + 32 + 32}
for name, size in shares.items():
    hello = BASE_HELLO + size + 4          # 4 bytes: group id + length per share (approx.)
    segs = -(-hello // MSS)
    print(f"{name:26s} ClientHello ~{hello:5d} B -> {segs} TCP segment(s)")
print("server share for X25519MLKEM768:", 1088 + 32, "bytes")
```

Saída esperada:

```text
x25519 only                ClientHello ~  556 B -> 1 TCP segment(s)
X25519MLKEM768             ClientHello ~ 1740 B -> 2 TCP segment(s)
X25519MLKEM768 + x25519    ClientHello ~ 1772 B -> 2 TCP segment(s)
server share for X25519MLKEM768: 1120 bytes
```

O tamanho do restante do ClientHello (520 bytes) é um pressuposto ilustrativo; os tamanhos reais variam com as extensões, o comprimento do nome do servidor e o preenchimento (padding), e é por isso que a bancada os mede diretamente.

### 3.6 Erros comuns e limites

- Contar novas tentativas como tentativas independentes.
- Coletar nomes de destino completos "por via das dúvidas".
- Usar intervalos de aproximação normal para taxas perto de zero.
- Tratar uma diferença antes/depois como efeito causal.

Cada erro tem uma salvaguarda já prevista no desenho: séries em vez de tentativas como unidade, categorias de destino mais hashes com sal em vez de nomes, intervalos de Wilson para taxas pequenas e uma implantação escalonada com controle concorrente para separar o efeito do grupo híbrido de qualquer outra coisa que tenha mudado nas mesmas semanas.

### Exercícios — capítulo 3

- **EX014 — Escolha do desenho.** Compare os três desenhos para o Fragment Study numa tabela de pontos fortes e ameaças. Rubrica: 3 = cada ameaça associada a um desenho que a resolve.
- **EX015 — Unidade de análise.** Explique como as novas tentativas podem inflar o denominador das falhas e enviesar a taxa. Rubrica: 3 = direção do viés declarada.
- **EX016 — Plano de minimização.** Escreva a seção de minimização de dados do pedido ao comitê de ética. Rubrica: 3 = hash com chave, categorias, retenção e acesso cobertos.
- **EX017 — Wilson à mão.** Calcule o intervalo de Wilson para 9 falhas em 20.000 séries com o Laboratório 3. Rubrica: 3 = saída e interpretação corretas.
- **EX018 — Sensibilidade ao tamanho.** Mude o tamanho de base do Laboratório 3b para 300 e para 1.300 bytes; quando o hello só com x25519 precisa de dois segmentos? Rubrica: 3 = execuções corretas e uma conclusão sobre por que a bancada precisa medir.
- **EX019 — Lista de reprodutibilidade.** Liste oito itens de que um leitor precisa para reproduzir os seus números. Rubrica: 3 = inclui a data da política e a soma de verificação dos dados.

### Síntese do capítulo

Um quase-experimento de implantação escalonada mais uma replicação em bancada, com unidades e desfechos definidos de antemão, logs minimizados, intervalos de Wilson e números gerados por scripts, produz um desenho cujos resultados são confiáveis e podem ser refeitos.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 08

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Segurança quântica e pós-quântica: explicações concorrentes

### Objetivos de aprendizagem e conexão

Você vai (1) listar explicações rivais para um efeito observado; (2) prever o que cada rival implica nos dados que você pode coletar; (3) usar a estratificação para discriminar entre os rivais; e (4) reconhecer quando um padrão se inverte na agregação. O capítulo aplica o desenho do Capítulo 3 e molda a proposta do Capítulo 5.

### 4.1 Rivais para o aumento das falhas

1. **Mecanismo de tamanho** — ClientHello em vários pacotes tratado de forma incorreta pelo proxy legado ou por alguns servidores.
2. **Atualização de software** — a atualização dos navegadores gerenciados, lançada na mesma semana, mudou outros comportamentos.
3. **Codepoint desconhecido** — algum middlebox rejeita um valor de grupo suportado que não reconhece (0x11EC para o X25519MLKEM768, no [registro da IANA](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml)), independentemente do tamanho.
4. **Sazonalidade** — o semestre começou; mais usuários, mais destinos incomuns.
5. **Artefato de relato** — uma campanha do help desk incentivou os relatos, aumentando os chamados, mas não as falhas.

Anote cada rival com os dados que o enfraqueceriam antes de olhar os resultados.

### 4.2 Previsões

Cada rival prevê uma impressão digital diferente. O tamanho prevê falhas concentradas no caminho que contém o proxy com inspeção e entre os destinos alcançados por ele, aparecendo apenas quando o hello cruza o limite de um segmento — a bancada pode variar o preenchimento para cruzá-lo ou não. A atualização prevê um aumento nos *dois* caminhos. O codepoint desconhecido prevê falha mesmo quando o compartilhamento híbrido é pequeno o bastante para caber num segmento (testável oferecendo o codepoint com o preenchimento removido, apenas na bancada). A sazonalidade prevê um aumento também no grupo de controle. O artefato de relato prevê chamados subindo sem que as falhas registradas subam. Escrever essas previsões antes da análise impede narrativas construídas a posteriori.

### 4.3 Atividade prática — Laboratório 4: estratificar por caminho

```python
# Lab 4 (synthetic): competing explanations. Is the failure rise caused by ClientHello size,
# or by the client software update shipped the same week? Stratify by path type.
data = {  # (path, hybrid offered): (failures, attempts)
    ("direct", False): (8, 20000), ("direct", True): (9, 20000),
    ("legacy proxy", False): (10, 20000), ("legacy proxy", True): (52, 20000)}
for path in ("direct", "legacy proxy"):
    r0 = 1e4 * data[(path, False)][0] / data[(path, False)][1]
    r1 = 1e4 * data[(path, True)][0] / data[(path, True)][1]
    print(f"{path:13s} before {r0:4.1f}/10k  after {r1:4.1f}/10k  difference {r1-r0:+5.1f}")
```

Saída esperada:

```text
direct        before  4.0/10k  after  4.5/10k  difference  +0.5
legacy proxy  before  5.0/10k  after 26.0/10k  difference +21.0
```

O aumento agregado está quase todo no caminho do proxy legado; o caminho direto mal se move. Uma atualização do navegador teria afetado os dois caminhos, então o rival 2 sai enfraquecido. O padrão é igualmente compatível com o mecanismo de tamanho e com o mecanismo do codepoint desconhecido — só a bancada consegue separar esses dois. Esta é a lição central do capítulo: uma estratificação elimina alguns rivais, não todos.

Os totais de antes e depois do laboratório coincidem com o Laboratório 3: 18 e 61 falhas em 40.000 séries. A divisão por caminho mostra onde a mudança aconteceu. O aumento de meio ponto no caminho direto está dentro do ruído para essas contagens, enquanto o aumento no caminho do proxy é grande. Nenhum dos estratos distingue ainda o tamanho do codepoint; isso exige a bancada com o preenchimento variado.

### 4.4 Inversões na agregação

Comparações estratificadas e agregadas podem discordar. Se o grupo híbrido tivesse sido ativado primeiro para usuários que usam sobretudo o caminho direto, a taxa agregada de falhas poderia cair após a ativação, embora, dentro do caminho do proxy, tivesse subido. Isso é o paradoxo de Simpson; a defesa é relatar as taxas estratificadas por caminho junto com a agregada e explicar qualquer inversão, em vez de escolher o nível conveniente.

No Fragment Study, a implantação escalonada aleatorizada pelo identificador do dispositivo torna essa inversão improvável, porque as duas coortes devem usar os dois caminhos em proporções semelhantes. Verifique esse pressuposto com uma tabela de balanceamento do uso dos caminhos por coorte antes de relatar qualquer um dos níveis. Se as coortes estiverem desbalanceadas, relate os dois níveis e explique a diferença.

### 4.5 Exemplo resolvido: evidência de entrevistas

As entrevistas com o help desk (I01–I06, sintéticas) relatam que as reclamações vieram "principalmente da ala do hospital" e que limpar o cache "às vezes resolvia". O primeiro ponto é compatível com o caminho do proxy. O segundo aponta para mais um rival: alguns clientes tentaram de novo com um hello menor após uma falha (os navegadores podem recorrer a um fallback), de modo que as falhas eram intermitentes. A evidência qualitativa sugeriu um mecanismo que os logs podiam então testar — a unidade de análise por série, do Capítulo 3, mostra se as novas tentativas tiveram sucesso sem o compartilhamento híbrido.

### 4.6 Erros comuns e limites

- Testar apenas a explicação preferida.
- Tratar a compatibilidade com um rival como prova quando outro prevê o mesmo padrão.
- Relatar apenas o agregado (ou apenas o estrato) que conta a história preferida.
- Executar experimentos de codepoint ou de tamanho contra middleboxes de produção; use a bancada.

Cada erro tem uma salvaguarda usada neste capítulo: cinco rivais listados antes da análise, previsões que os distinguem, taxas agregadas e por caminho relatadas e todos os experimentos de tamanho e de codepoint executados numa cópia isolada do proxy. A evidência de entrevistas é usada para sugerir testes, não para decidi-los.

### Exercícios — capítulo 4

- **EX020 — Tabela de rivais.** Monte uma tabela dos cinco rivais com as impressões digitais previstas. Rubrica: 3 = cada previsão observável.
- **EX021 — Acrescentar um rival.** Proponha um sexto rival e a sua previsão. Rubrica: 3 = plausível e discriminável.
- **EX022 — Estender o Laboratório 4.** Acrescente um caminho "Wi-Fi de visitantes" com 6 e 7 falhas por 20.000 antes/depois. Interprete. Rubrica: 3 = diferença e interpretação corretas.
- **EX023 — Construção de Simpson.** Construa números em que a taxa agregada cai enquanto os dois estratos sobem. Rubrica: 3 = aritmética correta e mecanismo explicado.
- **EX024 — Separar tamanho de codepoint.** Desenhe um experimento de bancada que separe os rivais 1 e 3. Rubrica: 3 = varia tamanho e codepoint de forma independente, em ambiente isolado.
- **EX025 — Do qualitativo ao quantitativo.** Transforme a frase de entrevista "limpar o cache resolveu" numa consulta de logs testável. Rubrica: 3 = a consulta usa o desfecho por série.

### Síntese do capítulo

Um efeito tem rivais; cada rival prevê uma impressão digital; a estratificação e a variação em bancada eliminam os rivais um a um; e os resultados agregados e estratificados precisam ser relatados juntos.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 08

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Proposta e piloto

### Objetivos de aprendizagem e conexão

Você vai (1) escrever uma proposta de dissertação com objetivos, hipóteses e plano de análise; (2) fixar critérios de sucesso para o piloto; (3) executar com segurança um pequeno piloto em bancada; e (4) revisar o protocolo com base no piloto. O capítulo transforma os rivais do Capítulo 4 num plano e prepara a coleta de dados do Capítulo 6.

### 5.1 Estrutura da proposta

Uma proposta de mestrado cabe em oito a doze páginas: contexto e lacuna (Capítulos 1–2); objetivos; hipóteses; desenho e dados (Capítulo 3); rivais e como cada um é tratado (Capítulo 4); plano de análise; ética e gestão de dados; cronograma e riscos. Os objetivos do Fragment Study: (A1) estimar, por caminho, a mudança na taxa de falhas atribuível à oferta do X25519MLKEM768; (A2) determinar em bancada se as falhas do proxy legado dependem do tamanho do ClientHello, do codepoint ou de ambos; (A3) recomendar uma correção que preserve a proteção quântica.

### 5.2 Hipóteses

- **H1** — No caminho do proxy legado, as falhas por 10.000 séries sobem pelo menos 10 quando o grupo híbrido é oferecido, em relação à coorte de controle concorrente; no caminho direto, o aumento fica abaixo de 2.
- **H2** — Na bancada, as falhas do proxy ocorrem quando, e somente quando, o ClientHello ocupa mais de um segmento TCP, independentemente do codepoint.
- **H3** — Após a atualização de firmware do proxy ou um desvio (bypass) da inspeção do TLS 1.3, o excesso no caminho do proxy desaparece (diferença abaixo de 2 por 10.000).

A H2 é o teste decisivo do mecanismo; se as falhas também ocorrerem com um hello de um segmento carregando o codepoint, a H2 é rejeitada em favor do rival 3.

### 5.3 Critérios e execução do piloto

Um piloto de duas semanas com 2.000 séries sintéticas por coorte, mais uma cópia de bancada do proxy (uma instância isolada de laboratório, nunca o dispositivo de produção), testa se o pipeline funciona. Critérios: minimização verificada em 100 registros por uma segunda pessoa; construção das séries igual à reconstrução manual em 50 casos; a bancada consegue produzir hellos de um e de dois segmentos com o mesmo codepoint ajustando o preenchimento; os codificadores atingem κ ≥ 0,75 em 40 logs de falha. O piloto sintético cumpre todos os critérios, exceto o das séries: 6 de 50 casos divergiram porque novas tentativas para um endereço IP diferente do mesmo host foram tratadas como séries novas. A regra é emendada para definir a série pelo nome do host em vez do endereço.

### 5.4 Exemplo resolvido: revisão após o piloto

O memorando de revisão declara o problema (séries divididas por endereço), o seu efeito (denominadores inflados em cerca de 4% no caminho do proxy), a emenda (séries por nome do host com janela de 10 segundos) e uma nova verificação (50 casos novos, 50/50 de concordância). Ele também registra uma decisão de *não* mudar: os codificadores pediram para acrescentar um rótulo de "certificate pinning", mas havia apenas dois casos assim, então eles continuam em "cert", com uma nota. Pilotos devem produzir mudanças pequenas e documentadas, não um novo estudo.

Anexe o memorando ao protocolo como uma emenda datada.

### 5.5 Erros comuns e limites

- Hipóteses sem limiar, de modo que qualquer aumento as "apoia".
- Executar experimentos de tamanho ou de codepoint no proxy de produção.
- Tratar o piloto como resultados preliminares a relatar como achados.
- Emendar o protocolo em silêncio.

Cada erro tem uma salvaguarda na proposta do Fragment Study. A H1 e a H3 têm limiares numéricos por 10.000 séries. Todos os experimentos de tamanho e de codepoint usam a instância isolada da bancada. Os dados do piloto aparecem apenas no capítulo de métodos, como verificações do pipeline. Toda emenda, como a regra de séries por nome do host, é registrada com data e motivo.

### Exercícios — capítulo 5

- **EX026 — De objetivos a hipóteses.** Escreva uma hipótese por objetivo, com limiar. Rubrica: 3 = cada uma falseável.
- **EX027 — Teste decisivo.** Explique por que a H2 é o teste decisivo do mecanismo e que resultado a rejeita. Rubrica: 3 = liga ao rival 3.
- **EX028 — Critérios do piloto.** Acrescente dois critérios de piloto seus. Rubrica: 3 = mensuráveis, ligados a um risco.
- **EX029 — Memorando de revisão.** Escreva o memorando para um piloto em que κ foi 0,66. Rubrica: 3 = causa, emenda, novo teste.
- **EX030 — Registro de riscos.** Liste cinco riscos do projeto com probabilidade, impacto e mitigação. Rubrica: 3 = inclui acesso aos dados e atraso do comitê de ética.
- **EX031 — Cronograma.** Esboce uma lista em estilo Gantt de 24 meses para a dissertação. Rubrica: 3 = realista, inclui a validação com os dados de Fenwick.

### Síntese do capítulo

Uma proposta transforma os rivais em hipóteses falseáveis com um teste decisivo do mecanismo; um piloto verifica o pipeline contra critérios declarados e produz emendas mínimas e documentadas.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 08

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Coleta e análise de dados

### Objetivos de aprendizagem e conexão

Você vai (1) coletar dados segundo um protocolo congelado; (2) codificar logs de falha de forma confiável e medir a concordância; (3) estimar um efeito de diferença-em-diferenças; (4) analisar os resultados da bancada; e (5) validar num segundo local. O capítulo executa a proposta do Capítulo 5 e fornece os resultados que o Capítulo 7 vai redigir.

### 6.1 Coleta

Oito semanas de dados do LK-HS-1 são coletadas sob o protocolo emendado: quatro semanas antes e quatro depois da implantação escalonada, com metade dos navegadores gerenciados (aleatorizada pelo identificador do dispositivo) recebendo primeiro a política híbrida. Congele o script de análise e registre o seu hash antes de revelar os rótulos das coortes.

Mantenha um registro de coleta com as interrupções ou lacunas na telemetria do proxy e dos navegadores, com datas, porque um dia faltando numa coorte enviesaria a comparação. Verifique, antes de revelar os rótulos, que a aleatorização pôs números aproximadamente iguais de dispositivos em cada coorte e que ambas usaram o caminho do proxy em proporções semelhantes.

### 6.2 Codificação das falhas

Cada série com falha tem um trecho de log. Dois codificadores (C1, C2) atribuem, de forma independente e com um livro de códigos escrito, um de quatro rótulos — *size* (reset do proxy após o primeiro segmento), *cert* (validação de certificado), *timeout*, *other*.

```python
# Lab 6 (synthetic): agreement between two coders labelling 60 failure logs, then the share of
# failures attributed to "split ClientHello mishandled" after reconciliation.
from collections import Counter
labels = ["size", "cert", "timeout", "other"]
a = ["size"]*30 + ["cert"]*12 + ["timeout"]*10 + ["other"]*8
b = ["size"]*27 + ["timeout"]*3 + ["cert"]*11 + ["other"] + ["timeout"]*9 + ["size"] + ["other"]*8
n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
ca, cb = Counter(a), Counter(b); pe = sum(ca[l]*cb[l] for l in labels) / n**2
print(f"observed agreement {po:.3f}  chance {pe:.3f}  Cohen's kappa {(po-pe)/(1-pe):.3f}")
```

Saída esperada:

```text
observed agreement 0.917  chance 0.323  Cohen's kappa 0.877
```

Um κ de 0,88 indica forte concordância além do acaso; as discordâncias (sobretudo *size* contra *timeout*, porque um segundo segmento descartado pode parecer um timeout) são resolvidas por discussão e registradas.

Mantenha o livro de códigos com um trecho de log de exemplo para cada rótulo, sobretudo para a fronteira difícil entre size e timeout. Os codificadores trabalham com trechos sem os rótulos das coortes, para que saber se o grupo híbrido foi oferecido não influencie o rótulo escolhido.

### 6.3 Diferença-em-diferenças

Com uma coorte de controle concorrente, o efeito é a mudança na coorte tratada menos a mudança na coorte de controle, estimado separadamente por caminho. Resultados sintéticos: caminho do proxy +20,4 por 10.000 (IC 95% 15,1–25,8); caminho direto +0,6 (−1,0 a 2,2). A H1 é apoiada. O pequeno aumento da própria coorte de controle no caminho do proxy (+0,6, exercício EX034) capta a sazonalidade, o rival 4, que o desenho antes/depois, sozinho, teria atribuído ao grupo híbrido.

Relate a estimativa com o seu intervalo e o número de séries por trás de cada célula, para que o cálculo possa ser conferido. O intervalo do caminho direto inclui zero, o que apoia a segunda parte da H1. O aumento da coorte de controle mostra por que o controle concorrente importa: sem ele, a mudança sazonal teria sido contada como efeito do grupo híbrido.

### 6.4 Resultados da bancada

Na cópia isolada do proxy na bancada, 200 handshakes por condição: hello de um segmento sem o codepoint, 0/200 falhas; hello de um segmento *com* o codepoint híbrido, 0/200; hello de dois segmentos sem o codepoint (só preenchimento), 187/200; hello de dois segmentos com o codepoint, 189/200. As falhas acompanham a segmentação, não o codepoint: a H2 é apoiada e o rival 3 é rejeitado para este modelo de proxy. Depois da aplicação da atualização de firmware do fornecedor na bancada, as falhas com dois segmentos caem para 0/200, o que antecipa a H3.

As quatro condições variam tamanho e codepoint de forma independente, e é isso que permite à bancada separar os dois rivais que os logs não conseguiam separar. Informe as versões de firmware da bancada antes e depois da atualização e o preenchimento usado em cada condição, para que outro laboratório possa reproduzir o resultado com o mesmo modelo de proxy.

### 6.5 Validação no Fenwick College

O Fenwick (sintético) tem um fornecedor de proxy diferente. Aplicando a análise congelada: excesso no caminho do proxy de +1,2 por 10.000 (−0,8 a 3,2) — nenhum efeito relevante. O mecanismo é específico do produto; a dissertação deve dizer "o modelo de proxy legado da Larkspur", e não "proxies com inspeção". Um resultado nulo no segundo local é um achado sobre o escopo, não uma falha do estudo.

Congele o script de análise antes de abrir os dados do Fenwick, como na Larkspur, e registre o seu hash. Relate o intervalo do Fenwick junto com a estimativa: ele inclui zero e exclui um efeito tão grande quanto o da Larkspur. Registrar o fornecedor e a versão do proxy no Fenwick permite que os leitores vejam quais produtos o resultado nulo cobre.

### 6.6 Erros comuns e limites

- Revelar os rótulos das coortes antes de congelar o script.
- Tratar o κ como aprovado/reprovado sem examinar quais categorias discordam.
- Generalizar um defeito específico de um produto para uma categoria de produtos.
- Os números sintéticos aqui ilustram métodos; não são medições de nenhum produto.

Cada erro tem uma salvaguarda neste capítulo: um hash do script registrado antes da revelação, um exame de quais rótulos discordaram em vez de apenas um limiar de κ, o resultado nulo do Fenwick usado para limitar a alegação a um modelo de proxy e uma declaração clara de que os números são sintéticos.

### Exercícios — capítulo 6

- **EX032 — Registro de congelamento.** Escreva o registro de congelamento (o quê, hash, testemunha, data). Rubrica: 3 = verificável.
- **EX033 — Interpretação do kappa.** Recalcule o Laboratório 6 depois de trocar três rótulos *size* do codificador B por *timeout*; interprete. Rubrica: 3 = κ correto e comentário sobre qual confusão importa.
- **EX034 — DiD à mão.** Caminho do proxy tratado 5,0→26,0, caminho do proxy de controle 5,1→5,7 por 10.000: calcule a DiD. Rubrica: 3 = 20,4 e explicação.
- **EX035 — Tabela da bancada.** Explique como as quatro condições da bancada discriminam entre os rivais 1 e 3. Rubrica: 3 = lógica correta.
- **EX036 — Escopo a partir da validação.** Escreva a frase de escopo implicada pelo resultado nulo do Fenwick. Rubrica: 3 = alegação específica do produto, sem generalização excessiva.
- **EX037 — Ameaças.** Liste três ameaças ao pressuposto de tendências paralelas da DiD neste contexto. Rubrica: 3 = específicas do cenário.

### Síntese do capítulo

Scripts congelados, codificação dupla com κ, uma estimativa de diferença-em-diferenças por caminho, uma bancada que varia tamanho e codepoint de forma independente e a validação num segundo local transformam uma correlação num relato causal delimitado.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 08

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Redação da dissertação e limitações

### Objetivos de aprendizagem e conexão

Você vai (1) estruturar uma dissertação de modo que cada capítulo responda a uma pergunta; (2) escrever resultados que separem estimativa, incerteza e interpretação; (3) escrever limitações com direção e consequência; e (4) fazer recomendações proporcionais à evidência. O capítulo transforma os resultados do Capítulo 6 no documento examinado no Capítulo 8.

### 7.1 Estrutura

Introdução (pergunta, por que importa, contribuição); contexto (ameaça quântica, ML-KEM, híbridos, ossificação dos middleboxes); método (desenho, dados, minimização, plano de análise com emendas); resultados (taxas, DiD, codificação, bancada, validação); discussão (mecanismo, escopo, recomendações); limitações; conclusão. Cada capítulo deve abrir com a pergunta que responde e fechar com aquilo de que o capítulo seguinte precisa.

Redija primeiro o capítulo de resultados, depois os métodos que os produziram, e escreva a introdução por último, para que ela não prometa mais do que foi entregue. Confira se a pergunta de abertura de cada capítulo é respondida pelo seu último parágrafo. A discussão deve ligar explicitamente as evidências da bancada e dos logs, em vez de apresentá-las separadas.

### 7.2 Redação dos resultados

Separe três camadas em todo parágrafo de resultados. *Estimativa*: "as falhas no caminho do proxy subiram 20,4 por 10.000 séries em relação ao controle." *Incerteza*: "IC 95% 15,1–25,8; κ da codificação = 0,88." *Interpretação*: "compatível com o mecanismo de tamanho, que a bancada isola." Nunca ponha interpretação na frase da estimativa. Relate o resultado nulo do Fenwick no capítulo de resultados, não numa nota de rodapé.

Aplique o mesmo padrão à bancada e ao Fenwick: estimativa, incerteza e interpretação em frases separadas. Gere os números de cada frase a partir dos scripts de análise, para que uma revisão dos dados não deixe números desatualizados no texto.

### 7.3 Limitações com direção

- *Só navegadores gerenciados foram observados* → os dispositivos não gerenciados da rede de visitantes ficam de fora; o efeito para eles é desconhecido.
- *O proxy da bancada é do mesmo modelo, mas é uma instância de laboratório* → diferenças de configuração podem tornar o efeito em produção maior ou menor.
- *Oito semanas* → destinos raros podem estar sub-representados, provavelmente subestimando as falhas com servidores incomuns.
- *Dados sintéticos neste livro didático* → nenhuma alegação sobre produtos reais.

Acrescente uma coluna de magnitude onde ela puder ser estimada e atualize a tabela se evidências posteriores definirem uma direção. Os dispositivos não gerenciados poderiam ser estudados numa continuação, se a equipe de rede concordar, o que transformaria uma incógnita num resultado medido.

### 7.4 Recomendações

Recomendação proporcional: atualizar o firmware do proxy legado (validado em bancada) e monitorar as falhas no caminho do proxy; não reverter o grupo híbrido no caminho direto, onde nenhum efeito foi encontrado; pedir ao fornecedor do proxy que confirme a correção nas notas de versão. Recomendação desproporcional, a evitar: "proxies com inspeção são incompatíveis com a criptografia pós-quântica".

Escreva cada recomendação com o seu responsável e a evidência que a sustenta. A atualização de firmware precisa de monitoramento em produção após a implantação, porque a bancada mostrou a correção apenas numa instância de laboratório. Se as falhas no caminho do proxy não caírem após a atualização, a recomendação é revista.

### 7.5 Exemplo resolvido: resumo

"Ativar o grupo TLS híbrido pós-quântico/tradicional X25519MLKEM768 numa universidade sintética aumentou os handshakes com falha num caminho de proxy legado com inspeção em 20,4 por 10.000 séries de conexão (IC 95% 15,1–25,8) em relação a um controle concorrente, sem mudança relevante no caminho direto. Experimentos em bancada mostraram que as falhas ocorriam apenas quando o ClientHello ocupava dois segmentos TCP, independentemente do novo codepoint, e cessavam após uma atualização de firmware. Um segundo local, com um proxy diferente, não mostrou efeito. Reparar o dispositivo específico preserva a proteção quântica; a reversão é desnecessária."

### 7.6 Erros comuns e limites

- Interpretação misturada às estimativas.
- Limitações listadas sem direção.
- Recomendações mais amplas do que o produto e o local estudados.

Cada erro tem uma salvaguarda nesta dissertação: frases de resultados em três camadas, uma lista de limitações em que cada item nomeia a sua direção e recomendações limitadas ao modelo de proxy legado da Larkspur. Leia o resumo mais uma vez contra as tabelas de resultados antes da entrega. Peça a um colega que marque qualquer frase que misture estimativa e interpretação, qualquer limitação sem direção e qualquer recomendação que nomeie uma categoria de produtos em vez do dispositivo estudado.

### Exercícios — capítulo 7

- **EX038 — Três camadas.** Reescreva um parágrafo que mistura estimativa e interpretação. Rubrica: 3 = camadas separadas.
- **EX039 — Direções das limitações.** Acrescente duas limitações com direções. Rubrica: 3 = direções argumentadas.
- **EX040 — Recomendação proporcional.** Escreva recomendações para um local em que a bancada mostrou, em vez disso, falhas disparadas pelo codepoint. Rubrica: 3 = coerentes com o mecanismo.
- **EX041 — Crítica do resumo.** Identifique qualquer exagero no resumo de 7.5. Rubrica: 3 = aponta o caráter sintético e o escopo de um único modelo.
- **EX042 — Aberturas de capítulo.** Escreva as duas primeiras frases de cada capítulo da dissertação. Rubrica: 3 = cada uma formula a sua pergunta.
- **EX043 — Parágrafo do resultado nulo.** Escreva o parágrafo de resultados do Fenwick. Rubrica: 3 = relata o IC e a implicação para o escopo.

### Síntese do capítulo

Uma dissertação responde à sua pergunta capítulo a capítulo, separa estimativas de interpretação, dá direção às limitações, relata os resultados nulos com destaque e não recomenda mais do que a evidência sustenta.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 08

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Revisão independente e defesa

### Objetivos de aprendizagem e conexão

Você vai (1) preparar um pacote de reprodutibilidade que um revisor independente consiga executar; (2) antecipar as perguntas dos examinadores; (3) tratar com responsabilidade a divulgação de um defeito de produto; e (4) apresentar os achados aos operadores. O capítulo fecha o ciclo da dissertação e leva ao apêndice de resoluções.

### 8.1 Pacote de reprodutibilidade

Inclua o conjunto de dados minimizado (ou um substituto sintético, se a universidade não puder liberá-lo), os scripts congelados com hashes, o livro de códigos e as planilhas de codificação, a configuração da bancada (sem firmware confidencial do fornecedor) e um README explicando como regenerar cada tabela. Peça a um colega que o execute a frio e registre cada ponto em que travou.

Teste o pacote numa máquina limpa, tendo apenas o README como guia da execução. Registre as versões do Python e de cada script e anote quanto tempo leva a execução completa, para que o revisor possa planejar o tempo.

### 8.2 Perguntas dos examinadores

- *Por que confiar na aleatorização pelo identificador do dispositivo?* Mostre as tabelas de balanceamento do uso dos caminhos e da versão do navegador.
- *O navegador poderia recorrer a um hello só clássico após a falha e esconder o efeito?* Sim; o desfecho por série conta uma série como falha somente se nenhuma tentativa teve sucesso, e uma análise secundária relata as falhas na primeira tentativa.
- *O efeito tem a ver com a criptografia pós-quântica?* Só indiretamente: o gatilho é o tamanho da mensagem, que o ML-KEM aumenta; qualquer ClientHello grande faria o mesmo, como mostra a condição só com preenchimento.
- *O que mudaria a sua recomendação?* Evidências de falhas disparadas pelo codepoint em outros lugares, ou uma correção do fornecedor que falhe em produção.

### 8.3 Divulgação

O defeito do proxy foi encontrado numa bancada isolada. Antes da publicação, relate-o ao fornecedor com os detalhes de reprodução (tamanhos de preenchimento, limites de segmento, versão do firmware), dê um prazo razoável e informe a equipe de rede da Larkspur. Publique a classe do defeito — tratamento incorreto de ClientHello em vários segmentos — e não passos para escapar da inspeção do proxy.

Registre a data de cada etapa da divulgação, do primeiro contato com o fornecedor até a publicação. Se o fornecedor confirmar a correção nas notas de versão, cite-as na dissertação. A equipe de rede da Larkspur deve saber do defeito antes de qualquer apresentação pública dos resultados.

### 8.4 Informe aos operadores

Para as operações de rede da Larkspur (sintético): "Ativar a troca de chaves resistente à computação quântica fez falhar algumas conexões que passam pelo proxy de inspeção antigo, porque a primeira mensagem ficou grande demais para um único pacote e o proxy a tratou de forma incorreta. Uma atualização de firmware resolve isso no nosso laboratório. Mantenham a proteção ligada; atualizem o proxy; acompanhem o painel de falhas da ala do hospital."

Teste o informe com um operador que não viu o estudo. Se ele não souber dizer o que fazer na segunda-feira, simplifique. Deixe o detalhe técnico num apêndice para os engenheiros que perguntarem.

### 8.5 Erros comuns e limites

- Pacotes que não rodam sem o autor.
- Responder "a culpa é da PQC?" com sim ou não, em vez de com o mecanismo.
- Publicar um defeito antes de o fornecedor e o dono serem informados.

Cada erro tem uma salvaguarda: um pacote testado a frio por um colega, uma resposta à pergunta sobre a PQC que explique o tamanho da mensagem e o resultado da condição só com preenchimento, e um cronograma de divulgação combinado com o fornecedor e com a equipe de rede da Larkspur antes da publicação. Confira cada um antes da data da defesa. Ensaie as respostas em voz alta uma vez.

### Exercícios — capítulo 8

- **EX044 — README do pacote.** Escreva o README do pacote de reprodutibilidade. Rubrica: 3 = um estranho conseguiria regenerar a Tabela 1.
- **EX045 — Execução a frio.** Liste cinco prováveis pontos de tropeço para um colega que execute o pacote. Rubrica: 3 = específicos.
- **EX046 — Tabela de balanceamento.** Descreva a tabela de balanceamento que responde à pergunta sobre a aleatorização. Rubrica: 3 = variáveis relevantes para os rivais.
- **EX047 — Pergunta do fallback.** Responda à pergunta do fallback em 120 palavras. Rubrica: 3 = distingue desfecho por série e desfecho da primeira tentativa.
- **EX048 — E-mail de divulgação.** Redija a divulgação ao fornecedor (sem passos de exploração). Rubrica: 3 = reprodutível, delimitada, prazo declarado.
- **EX049 — Informe ao operador.** Reescreva o 8.4 para a direção executiva da universidade. Rubrica: 3 = focado na decisão, sem jargão.
- **EX050 — Reflexão sobre a defesa.** Nomeie a parte mais fraca do Fragment Study e como um estudo futuro a corrigiria. Rubrica: 3 = honesta e acionável.

### Síntese do capítulo

Uma defesa tem sucesso quando um estranho consegue refazer o trabalho, as perguntas difíceis são respondidas com mecanismos e não com slogans, os defeitos são divulgados antes da publicação e os operadores recebem uma decisão clara.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 08

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para autoavaliação; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sintéticos vêm dos laboratórios.

**EX001.** Intervenção: grupo híbrido ativado; desfecho: as sessões de Wi-Fi falham; população: usuários da biblioteca; causa implícita: a PQC. Rival: uma mudança no portal cativo ou no firmware dos pontos de acesso na mesma semana.

**EX002.** Descritiva: as falhas de conexão de VPN mudaram após a ativação da troca de chaves híbrida no IKEv2? Comparativa: mudaram mais para usuários remotos do que para os do campus? Explicativa: quanto da mudança se deve ao tratamento da fragmentação do IKE, e em quais gateways?

**EX003.** Compartilhamento do cliente 97 + 1.568 = 1.665 bytes; compartilhamento do servidor 97 + 1.568 = 1.665 bytes (o texto cifrado do ML-KEM-1024 também tem 1.568 bytes; FIPS 203; RFC 10024).

**EX004.** Uma boa resposta argumenta cada elemento do FINER e admite uma fraqueza, por exemplo, que a viabilidade depende do acesso aos logs.

**EX005.** Três bases (RFC Editor, IACR ePrint, ACM DL), expressões exatas, datas e número de resultados.

**EX006.** Por exemplo, RFC 9794 (terminologia; norma; sem dados de implantação) e SP 800-227 (uso de KEMs; norma; não específica do TLS).

**EX007.** "Nenhum estudo publicado atribui as falhas de handshake pós-híbrido dentro de uma organização ao tamanho da mensagem, em comparação com causas concorrentes, usando um controle concorrente."

**EX008.** As trocas de chaves gravadas podem ser decifradas quando existir um CRQC, então a confidencialidade do tráfego de hoje depende da troca de chaves de hoje; assinaturas forjadas depois não alteram sessões passadas. As assinaturas são urgentes para raízes de confiança de vida longa e para firmware que precisa ser verificável por décadas.

**EX009.** ML-KEM-512 (categoria 1; chave de 800 B, texto cifrado de 768 B), -768 (categoria 3; 1.184 / 1.088), -1024 (categoria 5; 1.568 / 1.568). Segredo compartilhado de 32 B.

**EX010.** Os dois segredos entram no escalonamento de chaves do TLS; recuperar a chave de sessão exige as duas entradas, supondo que a KDF (HKDF) se comporte como um bom extrator, de modo que quebrar só um componente não rende nada útil.

**EX011.** Para chaves estáticas de vida longa com transferências pouco frequentes, o pressuposto conservador baseado em códigos do Classic McEliece e os seus textos cifrados pequenos podem justificar a chave pública grande; como alternativa, ML-KEM com o HQC como reserva posterior. A resposta deve pesar o tamanho da chave contra a diversidade de pressupostos.

**EX012.** Os 240% não têm taxa de base; as semanas diferem e há uma atualização do navegador no meio; as novas tentativas inflam as tentativas; não há estratificação por caminho.

**EX013.** 4,5 × 3,4 = 15,3 por 10.000 — um aumento absoluto de cerca de 10,8 por 10.000 séries, pequeno no agregado, mas concentrado por caminho.

**EX014.** Antes/depois: barato, confundido. Quase-experimento: controle concorrente, exige implantação escalonada. Bancada: isola o mecanismo, não mede a prevalência. A combinação dos dois últimos cobre as ameaças de um e de outro.

**EX015.** As novas tentativas acrescentam tentativas; se as falhas disparam novas tentativas, numerador e denominador sobem e as taxas por tentativa podem enganar em qualquer direção; a unidade por série elimina essa dependência.

**EX016.** Hash com chave dos endereços dos clientes, com rotação mensal; categorias de destino mais hash com sal; nenhum conteúdo; armazenamento nas instalações da universidade; retenção limitada; acesso nominal; aprovação do comitê de ética.

**EX017.** 9/20.000 → 4,5 por 10.000, IC 95% de Wilson de cerca de 2,4–8,6 por 10.000.

**EX018.** Base 300: todos cabem ou não como antes (x25519 556→336 B, um segmento). Base 1.300: o hello só com x25519 tem ~1.336 B, ainda um segmento; ele só precisa de dois quando a base passa de cerca de 1.424 B. Os tamanhos reais dependem das extensões, então meça.

**EX019.** Versão e hash do código; dicionário de dados; conjunto de dados minimizado e soma de verificação; política do navegador e data; regra de atribuição das coortes; definição de série; livro de códigos; configuração da bancada.

**EX020.** Tamanho → só o caminho do proxy, dependente do limite de segmento; atualização → os dois caminhos; codepoint → falhas com hello de um segmento; sazonalidade → o controle também sobe; relato → os chamados sobem sem que as falhas registradas subam.

**EX021.** Por exemplo, uma mudança no resolvedor de DNS que faz o tráfego do hospital passar pelo proxy com mais frequência → a composição dos caminhos muda; verifique a participação de cada caminho ao longo do tempo.

**EX022.** Caminho de visitantes 3,0→3,5 por 10.000 (+0,5): nenhuma mudança relevante, compatível com o mecanismo de tamanho ser específico do proxy.

**EX023.** Antes: estrato A (proxy) 10/1.000 e estrato B (direto) 1/1.000 séries, agregado 11/2.000 = 5,5 por 1.000. Depois: A 3/100 (30 por 1.000) e B 4/1.900 (cerca de 2,1 por 1.000), agregado 7/2.000 = 3,5 por 1.000. Os dois estratos sobem, mas o agregado cai porque o tráfego do período híbrido se deslocou para o estrato de poucas falhas.

**EX024.** Um 2×2 na bancada isolada: {um, dois segmentos} × {codepoint presente, ausente}, usando o preenchimento para controlar o tamanho.

**EX025.** "Proporção de primeiras tentativas com falha para um host seguidas, em até 10 s, por uma tentativa bem-sucedida do mesmo cliente sem o compartilhamento híbrido."

**EX026.** Como a H1–H3 em 5.2, cada uma com um limiar numérico.

**EX027.** Ela varia tamanho e codepoint de forma independente; falhas com um hello de um segmento carregando o codepoint rejeitariam a H2 em favor do rival 3.

**EX028.** Por exemplo, capturas de pacotes da bancada confirmam a segmentação em ≥ 95% das tentativas com preenchimento; o pipeline processa um dia de logs em menos de uma hora.

**EX029.** Causa (ambiguidade do livro de códigos entre size e timeout), emenda (regra de decisão: RST do proxy após o primeiro segmento = size), novo teste em 40 logs novos, seguir adiante se κ ≥ 0,75.

**EX030.** Acesso aos dados retirado; atraso do comitê de ética; fornecedor recusa a licença para a bancada; mudança no cronograma de implantação; indisponibilidade de um codificador — cada um com mitigação.

**EX031.** Meses 1–4 busca e proposta; 5–6 ética e piloto; 7–12 coleta; 13–16 análise; 17–18 validação no Fenwick; 19–22 redação; 23–24 revisão e defesa.

**EX032.** Arquivo do script, SHA-256, testemunha (orientador), data, local do registro.

**EX033.** O κ cai para 0,808 (concordância observada 0,867); a confusão entre size e timeout é a que mais importa, porque afeta o mecanismo.

**EX034.** (26,0 − 5,0) − (5,7 − 5,1) = 21,0 − 0,6 = 20,4 por 10.000.

**EX035.** Falhas com dois segmentos independentemente do codepoint, e nenhuma com um segmento mais o codepoint, apoiam o tamanho e rejeitam o codepoint.

**EX036.** "O efeito foi observado num único modelo de proxy legado na Larkspur; o proxy de outro fornecedor no Fenwick não mostrou efeito."

**EX037.** Crescimento do tráfego da ala do hospital no início do semestre; mudanças nas regras do proxy; atualização do navegador em momentos diferentes nas duas coortes.

**EX038.** Frase de estimativa, frase de incerteza, frase de interpretação — separadas.

**EX039.** Exclusão dos dispositivos não gerenciados (direção desconhecida); janela curta (provavelmente subestima as falhas com destinos raros).

**EX040.** Pedir ao fornecedor suporte ao novo codepoint, desviar temporariamente a inspeção do TLS 1.3 para destinos conhecidos e manter o grupo híbrido nos caminhos não afetados.

**EX041.** O resumo deveria declarar que os dados são sintéticos (neste livro) e que o efeito diz respeito a um único modelo de proxy; "a reversão é desnecessária" vale apenas para a Larkspur.

**EX042.** Uma abertura que formule a pergunta em cada capítulo.

**EX043.** "No Fenwick, o excesso no caminho do proxy foi de +1,2 por 10.000 (IC 95% −0,8 a 3,2): nenhum efeito relevante, o que indica que o defeito da Larkspur é específico do produto."

**EX044.** Passos, ambiente, soma de verificação dos dados, um comando por tabela.

**EX045.** Dependências ausentes, chaves de hash não explicadas, rótulos de caminho, licença da bancada, intervalos de datas não documentados.

**EX046.** Participação por coorte de caminho, versão do navegador, tipo de dispositivo, prédio do campus.

**EX047.** Um fallback do navegador poderia fazer uma série ter sucesso após uma falha; o desfecho primário conta as falhas de série, e uma análise secundária relata as falhas na primeira tentativa para expor o fallback oculto.

**EX048.** Produto, versão do firmware, comportamento observado, método da bancada, prazo de 90 dias, contato; nenhum passo de evasão.

**EX049.** Decisão: aprovar a atualização do proxy; manter a proteção ligada; resultado esperado e monitoramento.

**EX050.** Por exemplo, só navegadores gerenciados foram observados — um estudo futuro acrescenta amostragem da rede de visitantes, com consentimento e minimização.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Chromium Blog (2023). Protecting Chrome Traffic with Hybrid Kyber KEM. <https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html>
- Driscoll, F., Parsons, M., and Hale, B. (2025). Terminology for Post-Quantum Traditional Hybrid Schemes. RFC 9794. <https://www.rfc-editor.org/rfc/rfc9794.html>
- IANA. TLS Supported Groups registry. <https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml>
- Kwiatkowski, K., Kampanakis, P., Westerbaan, B., and Stebila, D. (2026). Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3. RFC 10024. <https://www.rfc-editor.org/rfc/rfc10024.html>
- NIST (2024). FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard. <https://doi.org/10.6028/NIST.FIPS.203>
- NIST (2024). FIPS 204, Module-Lattice-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.204>
- NIST (2024). FIPS 205, Stateless Hash-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.205>
- NIST (2025). IR 8545, Status Report on the Fourth Round of the NIST PQC Standardization Process. <https://doi.org/10.6028/NIST.IR.8545>
- NIST (2025). SP 800-227, Recommendations for Key-Encapsulation Mechanisms. <https://doi.org/10.6028/NIST.SP.800-227>
- Regev, O. (2009). On lattices, learning with errors, random linear codes, and cryptography. *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Rescorla, E. (2018). The Transport Layer Security (TLS) Protocol Version 1.3. RFC 8446. <https://www.rfc-editor.org/rfc/rfc8446.html>
- Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM J. Computing* 26(5). <https://doi.org/10.1137/S0097539795293172>
- tldr.fail. Community page on servers that mishandle large or split TLS ClientHello messages. <https://tldr.fail/>
