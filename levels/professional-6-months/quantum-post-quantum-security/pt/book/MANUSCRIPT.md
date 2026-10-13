# Segurança Quântica e Pós-Quântica: Um Fluxo de Trabalho de Migração para Profissionais

- Idioma: português do Brasil (`pt`); curso profissional, seis meses; aproximadamente 360 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais em início de carreira — analistas de segurança, equipes de risco e conformidade de TI, coordenadores de projeto — que vão conduzir um fluxo de trabalho repetível de migração pós-quântica e comunicar as constatações a gestores, responsáveis e fornecedores. Conhecimento de entrada: fundamentos de segurança e os fundamentos de sistemas pertinentes.
- Relação com os livros vizinhos: o [livro técnico](../../../../technical-18-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) ensina a configuração prática e o [livro de pós-graduação](../../../../postgraduate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md), a liderança em escala organizacional. **Este livro trata do fluxo de trabalho de gestão da migração**: delimitação do escopo, inventário, priorização, governança, relacionamento com fornecedores, acompanhamento, verificação e relato.
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação credenciada. Não concede autorização para testar sistemas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública. Sistemas de produção devem usar implementações verificadas da [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), da [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) e da [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205).

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Doze capítulos seguem um único fluxo de trabalho ao longo de seis meses: fundamentos e contexto (1–3), métodos centrais e ferramentas (4–5), o fluxo operacional, controles e verificação (6–7), um caso supervisionado (8), comunicação e relato (9), qualidade e diagnóstico de problemas (10), um laboratório supervisionado (11) e uma revisão de portfólio (12). Cada capítulo tem objetivos de aprendizagem, ensino, um caso resolvido, uma tarefa prática, erros comuns, cinco exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com Python 3; a saída impressa é mostrada para que você possa conferir a sua execução.

### O caso contínuo: Marlow & Tide Insurance

A **Marlow & Tide Insurance (MTI)** é uma seguradora sintética com 1.800 funcionários. Ela vende apólices por meio de um portal de corretores e de uma API de cotação, trata os sinistros num aplicativo de sinistros, mantém um arquivo de apólices de vida que precisa permanecer confidencial e verificável por 40 anos, troca arquivos com resseguradoras por SFTP e opera VPNs de escritórios, uma autoridade certificadora interna e mais de 120 fornecedores. Você entrou na equipe de segurança da MTI como coordenador do seu fluxo de trabalho de prontidão pós-quântica. Todos os números sobre a MTI são inventados.

### Política de fontes

As fontes primárias foram verificadas em 12 de outubro de 2026: NIST FIPS 203/204/205 (agosto de 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (rascunho público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) e [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). O FN-DSA (FIPS 206) e a norma do HQC ainda estavam em desenvolvimento. Verifique a situação de novo antes de se apoiar nela.

## Sumário

| Etapa | Capítulos |
|---|---|
| Fundamentos e contexto | [1 Fundamentos de segurança para profissionais](#ch-01) · [2 Contexto de serviços e de partes interessadas](#ch-02) · [3 Prática autorizada e tratamento de evidências](#ch-03) |
| Métodos e fluxo de trabalho | [4 Métodos centrais](#ch-04) · [5 Ferramentas e interpretação](#ch-05) · [6 Fluxo de trabalho operacional](#ch-06) · [7 Controles e verificação](#ch-07) · [8 Análise de caso supervisionada](#ch-08) |
| Comunicação e qualidade | [9 Comunicação, ética e relato](#ch-09) · [10 Qualidade e diagnóstico de problemas](#ch-10) · [11 Laboratório supervisionado](#ch-11) · [12 Portfólio prático e revisão final](#ch-12) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem

Você vai (1) explicar o que os computadores quânticos ameaçam na criptografia e o que não ameaçam; (2) nomear as normas pós-quânticas do NIST e a sua situação; (3) distinguir o risco de colher agora e decifrar depois do risco de forjar depois; (4) explicar a troca de chaves híbrida em termos simples; e (5) evitar afirmações equivocadas comuns em relatórios.

### 1.1 O que muda e o que não muda

Os sistemas atuais dependem de dois tipos de criptografia. A criptografia *simétrica* (como o AES) cifra os dados com uma chave compartilhada e as *funções de hash* (como o SHA-256) geram impressões digitais dos dados; elas continuam fortes contra os ataques quânticos conhecidos, nos tamanhos atuais. A criptografia de *chave pública* (RSA, curvas elípticas) permite que os sistemas acordem chaves e assinem dados sem um segredo compartilhado prévio; um computador quântico grande e com correção de erros, executando o algoritmo de Shor (Shor, 1997), a quebraria. Nenhum computador desse tipo existe hoje e ninguém sabe quando existirá; as estimativas públicas dos recursos necessários caíram ao longo do tempo (por exemplo, Gidney, 2025), e é por isso que as organizações estão se planejando agora.

### 1.2 Os substitutos

Em agosto de 2024, o NIST publicou três normas: a [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) (ML-KEM), para acordar chaves, e a [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) (ML-DSA) e a [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (SLH-DSA), para assinaturas. A [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) trata das assinaturas baseadas em hash com estado, para usos especializados como firmware. O [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) do NIST é um rascunho público inicial que propõe que os algoritmos vulneráveis ao quântico sejam descontinuados após 2030 e proibidos após 2035 — datas propostas, ainda não regras definitivas. O FN-DSA e uma norma baseada no HQC estavam em desenvolvimento.

### 1.3 Dois riscos com relógios diferentes

*Colher agora, decifrar depois*: um adversário grava hoje tráfego cifrado e o decifra quando existir um computador quântico. Isso importa agora para os dados que precisam permanecer confidenciais por muitos anos — na MTI, os registros de apólices de vida (40 anos) e os registros de sinistros (10 anos). *Forjar depois*: quando existir um computador quântico, um adversário poderia forjar assinaturas, certificados e atualizações de software. Isso importa sobretudo para o que é confiável por muito tempo, como certificados raiz, arquivos assinados e dispositivos que não podem ser atualizados.

Pergunte aos responsáveis pelos dados quais registros se enquadram em cada relógio antes de classificar qualquer coisa.

### 1.4 Troca de chaves híbrida

Durante a transição, os sistemas combinam um método pós-quântico com um tradicional, de modo que um atacante precisaria quebrar ambos. Essa abordagem *híbrida* (terminologia na [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) já está disponível em softwares web comuns como o grupo TLS X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)). A troca de chaves híbrida protege a confidencialidade das sessões; ela não torna, por si só, os certificados ou as assinaturas pós-quânticos.

Para a MTI, isso significa que as sessões gravadas do portal de corretores ficam protegidas assim que o híbrido é negociado, mas o certificado RSA-2048 do portal ainda precisa do seu próprio plano.

### 1.5 Caso resolvido

Um relatório de situação em rascunho diz: "Nosso site agora é à prova de quântico porque habilitamos o Kyber." Corrigido: "O portal de corretores agora usa troca de chaves pós-quântica híbrida (X25519MLKEM768, baseada no ML-KEM da NIST FIPS 203) nas conexões de navegadores atualizados. Isso protege o tráfego gravado do portal contra decifração futura. O certificado do portal ainda usa uma assinatura clássica; a migração do certificado está planejada separadamente."

Repare no que a correção faz. Ela nomeia o serviço, o algoritmo e a sua norma, diz quais clientes se beneficiam, declara o que está protegido e diz claramente o que ainda não foi feito. Ela também abandona "Kyber", o nome anterior à norma, em favor de ML-KEM. Use o mesmo padrão sempre que uma equipe lhe relatar progresso.

### 1.6 Tarefa prática

Reescreva três frases de um folheto de fornecedor ou de uma notícia sobre segurança quântica para que fiquem corretas, com fontes e adequadamente cautelosas.

Para cada frase, registre o original, a sua reescrita e a fonte que usou para verificá-la. Procure três falhas típicas: alegações de permanência como "à prova de quântico", datas de rascunho apresentadas como regras e troca de chaves híbrida descrita como se também cobrisse os certificados. Onde uma alegação não puder ser verificada, diga isso em vez de adivinhar. Guarde as reescritas; elas se tornam o seu texto explicativo correto para o portfólio.

### 1.7 Erros comuns e limites

- Alegações de "à prova de quântico" ou "inquebrável".
- Tratar as datas do rascunho do IR 8547 como definitivas.
- Dizer que a troca de chaves híbrida torna o sistema inteiro pós-quântico.

Cada erro custa credibilidade mais tarde. Um relatório da MTI que chamasse o portal de "à prova de quântico" seria contradito pelo primeiro auditor que olhasse o seu certificado clássico. Um plano construído sobre as datas propostas de 2030 e 2035 do IR 8547 como lei fixa precisaria ser reescrito se o texto final mudar. Confira todo relatório de situação quanto a esses três antes que ele saia da sua mesa. Peça também a um colega que o leia.

### Exercícios

- **EX001 — Manter ou substituir.** Classifique AES-256, RSA-2048, SHA-256 e ECDSA P-256. Rubrica: 3 = quatro corretos, com os motivos.
- **EX002 — Normas.** Nomeie as três normas do NIST de 2024 e para que serve cada uma. Rubrica: 3 = FIPS 203 ML-KEM, estabelecimento de chaves; FIPS 204 ML-DSA e FIPS 205 SLH-DSA, assinaturas.
- **EX003 — Dois relógios.** Dê um exemplo da MTI para cada risco: HNDL e forjar depois. Rubrica: 3 = exemplos corretos e explicados.
- **EX004 — Situação de rascunho.** Escreva uma frase correta sobre as datas do IR 8547. Rubrica: 3 = rascunho, proposta, anos.
- **EX005 — Corrija a alegação.** Corrija: "O TLS híbrido torna os nossos certificados seguros contra o quântico." Rubrica: 3 = separa a troca de chaves da autenticação.

### Síntese

Os computadores quânticos ameaçam o acordo de chaves e as assinaturas de chave pública, não a cifragem simétrica. As normas do NIST de 2024 fornecem substitutos; a troca de chaves híbrida trata já do risco de colher agora e decifrar depois, enquanto as assinaturas seguem um caminho planejado.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Segurança quântica e pós-quântica: contexto de serviços e de partes interessadas

### Objetivos de aprendizagem

Você vai (1) mapear os serviços da MTI para os dados que eles transportam e por quanto tempo esses dados precisam permanecer protegidos; (2) aplicar a regra de Mosca sob várias hipóteses de cronograma; (3) identificar as partes interessadas e o que cada uma precisa; (4) definir uma primeira lista de prioridades; e (5) explicar as prioridades a não especialistas.

### 2.1 Serviços e tempos de vida dos dados

Liste cada serviço, os dados que ele trata e por quanto tempo esses dados precisam permanecer confidenciais ou confiáveis. Use contratos, regulamentos e tabelas de retenção como fontes e pergunte aos responsáveis pelos dados quando tiver dúvida. Na MTI: arquivo de apólices de vida, 40 anos; registros de sinistros, 10 anos; as sessões do portal de corretores transportam dados pessoais relevantes por cerca de 7 anos; as solicitações de cotação têm vida curta.

Onde as fontes divergirem, adote o tempo de vida mais longo e registre a divergência. Por exemplo, um contrato de resseguro pode exigir que os dados de sinistros sejam mantidos por mais tempo do que diz a tabela interna. Um tempo de vida sem fonte é um palpite e deve ser classificado como tal.

### 2.2 A regra de Mosca

Mosca (2018): se os dados precisam permanecer seguros por *x* anos, a migração leva *y* anos e um computador quântico capaz pode chegar em *z* anos, então os dados já estão em risco quando *x* + *y* > *z*. Como ninguém conhece *z*, experimente vários valores.

Na MTI, o x de 40 anos do arquivo excede sozinho qualquer z plausível, então a decisão não depende da previsão. As solicitações de cotação, com x próximo de zero, nunca estão em risco, por menor que seja z. Os casos interessantes ficam no meio, como os registros de sinistros, nos quais a resposta muda com z.

### 2.3 Atividade prática — Laboratório M

```python
# Lab M (ch 2): Mosca's inequality x + y > z for synthetic Marlow & Tide Insurance data, sweeping z.
assets = [  # (name, shelf-life x in years, migration time y in years) - synthetic
    ("life-policy archive", 40, 4), ("claims records", 10, 3), ("quote requests", 0.1, 1), ("broker portal traffic", 7, 2)]
for z in (10, 15, 20):  # years until a cryptographically relevant quantum computer: an assumption, not a forecast
    late = [n for n, x, y in assets if x + y > z]
    print(f"z={z:>2}: at risk now -> {', '.join(late) if late else 'none'}")
```

Saída esperada:

```text
z=10: at risk now -> life-policy archive, claims records
z=15: at risk now -> life-policy archive
z=20: at risk now -> life-policy archive
```

O arquivo de apólices de vida está em risco sob todas as hipóteses; os registros de sinistros, apenas se *z* for de dez anos. Esse padrão é a base de uma lista de prioridades que não depende de prever o futuro.

Mude as entradas para ver quão sensível a lista é. Se a migração dos registros de sinistros levasse cinco anos em vez de três, os sinistros estariam em risco também com z = 15. Registre essas sensibilidades ao lado da tabela: elas dizem ao patrocinador quais estimativas merecem evidências melhores.

### 2.4 Partes interessadas

Os responsáveis pelos dados (subscrição, sinistros) definem os tempos de vida; os responsáveis pelos sistemas (equipes de TI) fazem as mudanças; os fornecedores controlam os produtos; compras redige os contratos; o jurídico e a conformidade acompanham as obrigações; os executivos aprovam os orçamentos e aceitam os riscos; os auditores conferem as evidências. Liste o que cada um precisa do fluxo de trabalho e o que você precisa de cada um.

Na MTI, a subscrição é responsável pelo tempo de vida das apólices de vida e a área de sinistros pelo tempo de vida de 10 anos dos sinistros; a equipe de infraestrutura é responsável pelos servidores SFTP das resseguradoras. Escreva cada nome no mapa de partes interessadas com um contato, para que os pedidos cheguem a uma pessoa, e não a um departamento.

### 2.5 Caso resolvido

A primeira lista de prioridades da MTI: 1) transferências de registros de apólices de vida entre os escritórios e o arquivo; 2) trocas SFTP com resseguradoras transportando dados de sinistros; 3) portal de corretores; 4) planejamento da AC interna (forjar depois, validade longa). As solicitações de cotação perdem prioridade. A lista é explicada ao patrocinador executivo como "proteger primeiro o que precisa ficar secreto por mais tempo".

Cada posição na lista tem um motivo que pode ser rastreado até o Laboratório M ou até a classe de exposição. A AC interna aparece, embora não transporte segredos, porque a sua validade longa a torna uma preocupação de forjar depois. Mantenha os motivos junto da lista, para que ela possa ser defendida.

### 2.6 Tarefa prática

Monte uma tabela de cinco linhas com serviços da MTI, os dados, o tempo de vida, a fonte do tempo de vida e o responsável; execute o Laboratório M com os seus próprios valores.

Obtenha cada tempo de vida de uma tabela de retenção, de um contrato ou de uma declaração do responsável, e escreva qual foi. Depois compare a sua saída do Laboratório M com a do livro: se um serviço entrar ou sair da lista de risco, explique por quê em uma frase. Peça a um colega que verifique se cada responsável nomeado de fato controla o serviço, e não apenas o usa. Guarde a tabela no seu portfólio.

### 2.7 Erros comuns e limites

- Tempos de vida adivinhados em vez de obtidos de fontes.
- Uma única data quântica suposta.
- Esquecer compras e o jurídico como partes interessadas.

Cada erro enfraquece a lista de prioridades de uma forma diferente. Um tempo de vida adivinhado não pode ser defendido perante um auditor. Uma única data quântica faz a lista parecer uma previsão e convida à discussão sobre a data, e não sobre os dados. Deixar de fora compras e o jurídico significa que as cláusulas contratuais e as obrigações aparecem tarde, depois que os fornecedores já definiram os seus roteiros. Confira a sua própria tabela quanto a cada um deles.

### 2.8 Revisitando a lista

As prioridades mudam quando os fatos mudam: um novo contrato estende um período de retenção, um fornecedor lança suporte híbrido, um serviço é desativado. Revise a lista de prioridades a cada trimestre com os responsáveis pelos dados e pelos sistemas, registre o que mudou e por quê e guarde as versões antigas. Auditores e executivos confiam mais numa lista que evolui visivelmente com as evidências do que numa que nunca muda.

Na MTI, um gatilho típico seria o fornecedor do arquivo publicar datas para o suporte ao ML-DSA, o que mudaria a forma como o item de forjar depois é planejado.

### Exercícios

- **EX006 — Mosca.** Para os registros de sinistros (*x* = 10, *y* = 3), declare os cronogramas sob os quais eles estão em risco. Rubrica: 3 = *z* < 13.
- **EX007 — Fonte do tempo de vida.** Nomeie duas fontes de tempos de vida dos dados numa seguradora. Rubrica: 3 = contratos/regulamentação/tabela de retenção, com confirmação do responsável.
- **EX008 — Mapa de partes interessadas.** Liste cinco partes interessadas e uma necessidade de cada uma. Rubrica: 3 = cinco pares pertinentes.
- **EX009 — Prioridade.** Por que o arquivo de apólices de vida vem primeiro? Rubrica: 3 = em risco sob todas as hipóteses; tempo de vida mais longo.
- **EX010 — Explicação simples.** Explique a lista de prioridades a um executivo em três frases. Rubrica: 3 = clara, correta, orientada à decisão.

### Síntese

Mapas de serviços com tempos de vida obtidos de fontes, a regra de Mosca sob várias hipóteses e um mapa de partes interessadas produzem uma lista de prioridades robusta e explicável.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e tratamento de evidências

### Objetivos de aprendizagem

Você vai (1) obter e respeitar a autorização por escrito; (2) coletar apenas as evidências necessárias; (3) guardar e rotular as evidências adequadamente; (4) tratar constatações sensíveis; e (5) trabalhar com informações confidenciais de fornecedores.

### 3.1 Autorização

Mesmo as atividades "inofensivas" — ler configurações, executar uma ferramenta de inventário, pedir logs — precisam de autorização por escrito do responsável pelo sistema, declarando sistemas, métodos, janela de tempo, tratamento dos dados e contatos. Os testes ativos que alteram a negociação são feitos apenas em laboratórios isolados, pela equipe técnica.

Na MTI, o ticket SEC-118 é o modelo: ele nomeia os servidores, o método somente leitura, as datas, o repositório e um contato. Guarde uma cópia de cada autorização com as evidências que ela produziu e interrompa o trabalho quando a janela se fechar, mesmo que a tarefa não tenha terminado.

### 3.2 O mínimo necessário de evidências

Colete o que responde à pergunta: nomes de algoritmos, versões, detalhes de certificados, datas. Não colete conteúdo de mensagens nem dados de clientes. Prefira exportações de configuração e resumos a capturas brutas.

Nos servidores SFTP das resseguradoras, isso significa uma exportação da versão do OpenSSH e das configurações de troca de chaves, e não amostras dos arquivos transferidos. Se uma equipe oferecer mais do que você precisa, recuse educadamente e registre que recusou. Menos evidências são mais fáceis de proteger e mais simples de apagar quando o programa terminar. Anote o que você escolheu não coletar.

### 3.3 Armazenamento e rotulagem

Guarde as evidências no repositório combinado, com rótulos: fonte, data, coletor, sistema, classificação. Restrinja o acesso; inventários de fraquezas são sensíveis. Mantenha um registro de quem acessou o quê.

Use os mesmos campos de rótulo em todos os itens, para que as buscas funcionem entre as fontes: uma exportação, um questionário e um resumo de logs devem todos mostrar quem os coletou e quando. Revise o registro de acessos todo mês e remova as pessoas que não precisam mais de acesso. Evidências que não podem ser rastreadas até uma fonte e uma data devem ser classificadas como U até que possam.

### 3.4 Constatações sensíveis

Se encontrar algo grave — uma chave privada exposta, um sistema sem patch com uma vulnerabilidade conhecida —, comunique imediatamente pelo processo de segurança; não investigue mais por conta própria.

Registre o que viu, quando e onde, e repasse ao contato de incidentes nomeado na sua autorização. Não copie uma chave descoberta nem teste se ela funciona; isso estaria fora da sua autorização e poderia danificar as evidências. Depois, anote no rastreador que o item aguarda o processo de segurança.

### 3.5 Informações de fornecedores

Os fornecedores podem compartilhar roteiros sob confidencialidade. Registre-os como declarações do fornecedor, respeite o acordo e não os encaminhe para fora do grupo de pessoas que precisam deles.

Guarde-os com acesso restrito, como a MTI fez com o roteiro sob NDA, e classifique as alegações que eles contêm como D até serem observadas. Ao resumir para os executivos, refira-se a um roteiro pela sua data e situação, sem citar detalhes confidenciais. Se um fornecedor pedir que o seu roteiro seja apagado, siga o acordo e anote a exclusão no registro de evidências.

### 3.6 Caso resolvido

O coordenador da MTI pede exportações de configuração dos servidores SFTP das resseguradoras (nome no inventário: `insurer-sftp`). A autorização (ticket SEC-118) cobre exportação somente leitura, de 1 a 15 de outubro, resultados guardados no repositório de evidências de segurança, contato: o líder de infraestrutura. A exportação mostra a versão do OpenSSH e as configurações de troca de chaves; nenhum conteúdo de arquivo é tocado. O roteiro de um fornecedor recebido sob NDA é guardado com acesso restrito e rotulado como "declaração do fornecedor, confidencial".

Repare no que fez isso funcionar: o escopo era estreito, o método era somente leitura, a janela tinha data de término e o contato foi nomeado com antecedência. O roteiro foi útil, mas permaneceu confidencial. Os dois itens podem ser rastreados depois pelos seus rótulos.

### 3.7 Tarefa prática

Escreva um pedido de autorização e um rótulo de evidência para uma atividade de inventário.

Escolha um tipo real de atividade, como uma exportação de certificados da AC interna da MTI. O pedido deve nomear sistemas, método, janela de tempo, armazenamento, tratamento dos dados e um contato, como o SEC-118. O rótulo deve informar fonte, data, coletor, sistema e classificação. Pergunte a um colega se um responsável pelo sistema conseguiria aprovar o seu pedido sem fazer uma única pergunta de acompanhamento. Depois revise o pedido uma vez e guarde as duas versões para mostrar o que você melhorou.

### 3.8 Erros comuns e limites

- Coletar mais dados do que o necessário.
- Evidências sem rótulos.
- Compartilhar amplamente os roteiros dos fornecedores.

Cada erro tem um custo. O excesso de dados aumenta o que precisa ser protegido e depois apagado. Evidências sem rótulo não sustentam uma classificação nem podem ser rastreadas numa auditoria, então o trabalho precisa ser repetido. Um roteiro compartilhado além do acordo pode violar um NDA e prejudicar a relação com o fornecedor, da qual dependem vários itens do rastreador da MTI. Confira cada evidência quanto aos três antes de arquivá-la. Corrija-os antes de arquivar.

### 3.9 Retenção e exclusão

As evidências têm o seu próprio tempo de vida. Combine por quanto tempo as exportações de inventário, os questionários e os logs são mantidos — normalmente pela duração do programa mais um período de auditoria — e apague-os com segurança depois, mantendo apenas os resultados agregados e os registros de decisão. Registre as exclusões no registro de evidências. Manter as exportações brutas para sempre aumenta o dano se o repositório for comprometido, porque um mapa completo das fraquezas criptográficas de uma organização é valioso para os atacantes.

Quando alguém deixar o fluxo de trabalho, remova prontamente o seu acesso ao repositório de evidências e revise o que a pessoa podia ver; as revisões de acesso fazem parte do tratamento de evidências, não são um detalhe posterior.

### Exercícios

- **EX011 — Elementos da autorização.** Liste cinco elementos de uma autorização por escrito. Rubrica: 3 = sistemas, métodos, janela, tratamento dos dados, contatos.
- **EX012 — Mínimo de evidências.** Para um inventário de SFTP, liste três coisas a coletar e duas a não coletar. Rubrica: 3 = listas justificadas.
- **EX013 — Rótulo.** Escreva um rótulo de evidência para a exportação do SFTP. Rubrica: 3 = fonte, data, coletor, sistema, classificação.
- **EX014 — Constatação grave.** O que você faz quando encontra uma chave privada numa exportação? Rubrica: 3 = parar, comunicar, não usar, documentar.
- **EX015 — Roteiro sob NDA.** Como você registra e compartilha um roteiro de fornecedor sob NDA? Rubrica: 3 = rótulo de declaração do fornecedor, acesso restrito, necessidade de saber.

### Síntese

Um tratamento de evidências autorizado, mínimo e bem rotulado protege a organização, os seus clientes e os seus fornecedores, e mantém o fluxo de trabalho confiável.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Segurança quântica e pós-quântica: métodos centrais

### Objetivos de aprendizagem

Você vai (1) conduzir um inventário usando várias fontes; (2) construir e ler uma lista de materiais criptográficos (CBOM); (3) classificar evidências; (4) classificar a exposição; e (5) acompanhar os desconhecidos como trabalho.

### 4.1 Fontes do inventário

Exportações de configuração, listas de certificados da AC, observações de rede feitas pelas equipes técnicas, documentação das aplicações e questionários a fornecedores. Cada uma responde a perguntas diferentes; combine-as.

Na MTI, a troca de chaves do portal de corretores foi vista em observação passiva, o seu certificado veio da configuração e o algoritmo de assinatura do aplicativo de sinistros só era conhecido pelo código. Nenhuma fonte isolada cobriu os seis ativos. Registre qual fonte forneceu cada linha da CBOM, porque a fonte define a classificação da evidência. Anote onde duas fontes divergem e pergunte ao responsável qual está atualizada.

### 4.2 Atividade prática — Laboratório I

```python
# Lab I (ch 4): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("broker-portal", "key-exchange", "X25519MLKEM768", "passive"), ("broker-portal", "signature", "RSA-2048", "config"),
    ("claims-app", "key-exchange", "ECDHE-P256", "passive"), ("claims-app", "signature", "ECDSA-P256", "code"),
    ("policy-db", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("call-recorder", "unknown", "unknown", "none"), ("office-vpn", "key-exchange", "ECDHE-P384", "config")]
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
assets 6, unknown 1 (17%)
quantum-vulnerable uses 5: broker-portal/signature, claims-app/key-exchange, claims-app/signature, policy-db/key-exchange, office-vpn/key-exchange
hybrid key exchange present on: ['broker-portal']
```

O script conta os ativos, sinaliza os usos vulneráveis ao quântico e lista onde a troca de chaves híbrida já está presente. Repare que o AES-256-GCM do faturamento não é sinalizado, porque a cifragem simétrica desse tamanho continua adequada, e que o gravador de chamadas é contado como desconhecido, e não como seguro. A proporção de 17 % de desconhecidos é a primeira medida de destaque: um ativo em seis ainda não pode ser avaliado. Execute-o com um registro extra seu e verifique se as contagens mudam como você espera.

### 4.3 Graus de evidência

Uma classificação simples: A, observado em operação; B, configuração oficial; C, inferido da documentação ou do código; D, alegação do fornecedor; U, desconhecido. Prioridades baseadas em evidências D ou U precisam de verificação antes de se gastar dinheiro.

Os graus também dizem como melhorar a evidência: um D pode subir pedindo à equipe técnica que observe o produto em operação, e um C, obtendo a configuração. Escreva o grau ao lado de cada registro, e não só de cada ativo, já que um ativo pode ter graus diferentes para funções diferentes.

### 4.4 Classes de exposição

Gravar agora (HNDL): troca de chaves clássica transportando dados de vida longa. Forjar depois: assinaturas clássicas confiáveis por longos períodos ou difíceis de substituir. Adequado: cifragem simétrica e hashes em bons tamanhos. Desconhecido.

No extrato do Laboratório I, a troca de chaves RSA do policy-db é de gravar agora se transportar dados de vida longa, a assinatura RSA-2048 do portal de corretores é de forjar depois, o AES-256-GCM do faturamento é adequado e o gravador de chamadas é desconhecido. Classifique cada uso de criptografia separadamente, já que um ativo pode cair em duas classes. A classe decide quais controles se aplicam.

### 4.5 Os desconhecidos como trabalho

Todo desconhecido vira uma tarefa com responsável e prazo: perguntar ao fornecedor, pedir uma exportação de configuração, pedir à equipe técnica que observe. Acompanhe a proporção de desconhecidos como medida de destaque.

Na MTI, o U do gravador de chamadas virou uma tarefa de questionário ao seu fornecedor, com responsável nomeado e prazo. A proporção de desconhecidos é uma medida melhor do progresso do inventário do que o número de ativos listados, porque não pode ser melhorada contando duas vezes os ativos fáceis. Feche cada tarefa com evidências.

### 4.6 Caso resolvido

O primeiro extrato da CBOM da MTI corresponde ao Laboratório I: seis ativos, cinco usos vulneráveis ao quântico, um desconhecido (o gravador de chamadas). Graus: portal de corretores A na troca de chaves (observada) e B na assinatura (configuração), aplicativo de sinistros A na troca de chaves e C na assinatura (apenas código), policy DB B, gravador de chamadas U, VPN dos escritórios B. Tarefas: questionário ao fornecedor do gravador de chamadas; confirmar com o responsável o algoritmo de assinatura do aplicativo de sinistros.

Os graus decidem o que acontece em seguida. Os itens com A ou B podem ser priorizados com confiança; o gravador de chamadas não pode ser priorizado de forma alguma até que o seu fornecedor responda, e a entrada de assinatura do aplicativo de sinistros precisa da confirmação do responsável, porque o código sozinho pode não refletir o que está implantado.

### 4.7 Tarefa prática

Atribua grau e classe a cada registro do Laboratório I e escreva tarefas para os desconhecidos.

Dê a cada registro um grau de A a U e uma classe de exposição, com uma linha explicando cada escolha. Para o gravador de chamadas, escreva uma tarefa com responsável, prazo e a pergunta a fazer. Depois compare com o caso resolvido e explique qualquer diferença. Um colega deve conseguir reproduzir os seus graus apenas pela coluna de fonte. Anote quais registros você não conseguiu classificar e por quê.

### 4.8 Erros comuns e limites

- Uma única fonte.
- Tratar alegações de fornecedores como observações.
- Desconhecidos sem responsáveis.

Uma única fonte deixa pontos cegos: a configuração sozinha não mostra o que é negociado, e a observação sozinha não vê os certificados cifrados. Uma alegação de fornecedor tratada como observação pode empurrar dinheiro para um ativo que já está protegido, ou afastá-lo de um que não está. Um desconhecido sem responsável simplesmente continua desconhecido, trimestre após trimestre, enquanto a medida de destaque estagna. Confira o extrato da MTI quanto a cada um deles antes de confiar nele e corrija o que encontrar.

### 4.9 Conduzindo o inventário como um ciclo

Um inventário não se faz uma única vez. Conduza-o como um ciclo: coletar (exportações, questionários, observações), consolidar na CBOM, atribuir graus, classificar, abrir tarefas para os desconhecidos e as lacunas e repetir a cada trimestre. Cada ciclo deve mostrar três números à gestão: quantos ativos de nível 1 têm evidências A ou B, quantos são desconhecidos e quantos já estão protegidos. Quando um fornecedor responde a um questionário, o grau dos seus produtos passa de U para D; quando uma equipe técnica confirma a resposta por observação, passa para A. Esse movimento é progresso real, mesmo antes de qualquer algoritmo mudar, porque transforma palpites em fatos sobre os quais os orçamentos podem se basear.

Mantenha o acesso à CBOM restrito a quem precisa dela e compartilhe de forma mais ampla apenas os resumos.

### Exercícios

- **EX016 — Leitura do Laboratório I.** Qual ativo já tem troca de chaves híbrida, e o que continua clássico nele? Rubrica: 3 = broker-portal; a sua assinatura (RSA-2048).
- **EX017 — Graus.** Atribua graus a: handshake observado; e-mail do fornecedor; registro no banco de dados da AC; diagrama de arquitetura. Rubrica: 3 = A, D, B, C.
- **EX018 — Classes.** Classifique os cinco usos vulneráveis do Laboratório I pela classe de exposição. Rubrica: 3 = trocas de chaves HNDL; assinaturas forjar depois.
- **EX019 — Proporção de desconhecidos.** Qual é a proporção de desconhecidos do Laboratório I, e como você a relataria? Rubrica: 3 = 17 % dos ativos, mostrada ao lado de cada número.
- **EX020 — Tarefa.** Escreva a tarefa para o gravador de chamadas. Rubrica: 3 = pergunta, método, responsável, prazo.

### Síntese

Uma CBOM com várias fontes e evidências graduadas classifica a exposição e transforma os desconhecidos em trabalho acompanhado.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Segurança quântica e pós-quântica: ferramentas e interpretação

### Objetivos de aprendizagem

Você vai (1) ler a saída de auditorias de configuração e de ferramentas de inventário; (2) distinguir "oferecido" de "negociado"; (3) reconhecer os pontos cegos das ferramentas; (4) interpretar as respostas dos questionários a fornecedores; e (5) transformar a saída das ferramentas em constatações.

### 5.1 O que as ferramentas mostram

As auditorias de configuração mostram o que um serviço oferece e em que ordem. Os resumos de logs das equipes técnicas mostram o que foi negociado. Os inventários de certificados mostram os algoritmos de assinatura e as datas de expiração. Os questionários a fornecedores mostram alegações. Como profissional, você raramente vai executar ferramentas ativas por conta própria; vai ler e interpretar a saída delas.

Na MTI, a auditoria de configuração do Laboratório T mostrou o que o portal de sinistros oferecia; apenas os resumos de logs podiam mostrar o que ele negociava. Mantenha o tipo de cada saída ao lado da sua constatação, para que os leitores saibam se ela descreve a intenção ou a operação.

### 5.2 Atividade prática — Laboratório T

```python
# Lab T (ch 5): audit synthetic TLS server configurations for post-quantum key exchange and preference order.
configs = {  # service: ordered list of offered groups (server preference) - synthetic
    "quote-api": ["X25519MLKEM768", "X25519", "secp256r1"],
    "claims-portal": ["X25519", "X25519MLKEM768", "secp256r1"],
    "insurer-sftp": ["ecdh-sha2-nistp256"],
    "hr-intranet": ["X25519", "secp384r1"]}
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
quote-api         OK (hybrid preferred)
claims-portal     WARN hybrid offered but not preferred
insurer-sftp      CLASSICAL ONLY
hr-intranet       CLASSICAL ONLY
```

O portal de sinistros "oferece, mas não prefere" o híbrido: uma auditoria de configuração que verificasse apenas a presença o relataria como concluído, mas a maioria das conexões continuará usando troca de chaves clássica. Pergunte sempre se uma ferramenta verifica a preferência e a negociação real.

O script verifica duas coisas em cada serviço: se algum grupo híbrido é oferecido e se ele vem primeiro na ordem de preferência do servidor. A API de cotação passa nas duas verificações. O servidor SFTP e a intranet de RH falham na primeira. Repare que o script trabalha apenas com configurações; ele não consegue mostrar o que os clientes realmente negociam.

### 5.3 Pontos cegos

Um sensor passivo no TLS 1.3 vê o grupo negociado, mas não o certificado, que é cifrado. Um scanner ativo com uma biblioteca antiga relata tudo como clássico. Uma exportação de configuração pode estar desatualizada. Um questionário pode descrever uma versão do produto que a MTI não executa. Escreva o ponto cego ao lado de cada resultado.

No portal de corretores da MTI, um sensor passivo consegue mostrar X25519MLKEM768, mas não o certificado RSA-2048, que veio da configuração. Combine sempre um resultado com a fonte que cobre o seu ponto cego antes de relatá-lo.

### 5.4 Interpretando questionários

As boas respostas nomeiam algoritmos e conjuntos de parâmetros (ML-KEM-768 conforme a FIPS 203), protocolos (grupo híbrido do TLS 1.3 conforme a RFC 10024; IKEv2 conforme a RFC 9370), versões de produto e datas, e oferecem acesso para teste. As respostas fracas dizem "pronto para PQC" ou "roteiro em revisão". Pontue as respostas de forma consistente, por exemplo 0 = sem resposta, 1 = alegação sem data, 2 = roteiro datado que nomeia algoritmos e protocolos, 3 = entregue e verificável.

Aplique a mesma escala a todos os fornecedores e mantenha o texto da resposta junto da pontuação, para que um revisor possa conferi-la. Uma pontuação 2 continua sendo grau D até que o produto seja observado. Onde um fornecedor oferecer acesso para teste, peça à equipe técnica da MTI que o use e eleve o grau com o que ela encontrar.

### 5.5 Da saída à constatação

Uma constatação declara observação, fonte, data, impacto, recomendação e responsável. "Portal de sinistros: grupo híbrido oferecido, mas X25519 preferido (auditoria de configuração, 6 de outubro). Impacto: as sessões de sinistros continuam expostas a HNDL. Recomendação: reordenar os grupos para preferir X25519MLKEM768; verificar com os logs. Responsável: Web Platform."

Cada elemento tem um propósito: a fonte e a data permitem ao leitor julgar a atualidade, o impacto liga o resultado à exposição e o responsável torna alguém encarregado. Uma constatação sem algum deles tende a ser discutida em vez de corrigida. Escreva as constatações de modo que o responsável possa agir sem lhe perguntar o que você quis dizer.

### 5.6 Caso resolvido

A auditoria sinaliza o insurer-sftp como apenas clássico. A equipe de infraestrutura confirma que a versão do OpenSSH é anterior ao suporte híbrido. Constatação aberta: atualizar e habilitar `mlkem768x25519-sha256`; coordenar com as resseguradoras cujos clientes podem ser antigos; responsável: Infraestrutura; prazo de um trimestre.

Repare que a constatação foi aberta apenas depois que a equipe de infraestrutura confirmou a versão; a auditoria sozinha podia estar desatualizada. A coordenação com as resseguradoras faz parte da constatação porque uma atualização do lado da MTI protege apenas os parceiros cujos clientes também suportam o método híbrido.

### 5.7 Tarefa prática

Transforme cada linha do Laboratório T numa constatação ou numa nota de "conforme o esperado".

Para cada linha, escreva observação, fonte, data, impacto, recomendação e responsável, ou uma nota de uma linha explicando por que nenhuma ação é necessária. A API de cotação deve ser uma nota de "conforme o esperado"; o portal de sinistros e os dois serviços clássicos precisam de constatações. Pergunte se a intranet de RH transporta dados de vida longa antes de decidir a sua prioridade. Mantenha cada constatação em poucas linhas e nomeie o responsável. Peça a um colega que as revise.

### 5.8 Fazendo a pergunta de acompanhamento certa

Quando a saída de uma ferramenta o surpreender, faça três perguntas à equipe técnica antes de abrir uma constatação: a ferramenta é atual o bastante para ver algoritmos pós-quânticos; os dados são recentes; e o resultado coincide com outra fonte? Muitas constatações aparentes desaparecem — ou ficam mais graves — depois dessas verificações.

Na MTI, fazer essas perguntas sobre o resultado do insurer-sftp levou à verificação de versão da equipe de infraestrutura, que transformou um resultado de ferramenta numa constatação confirmada. Registre as respostas às três perguntas junto da constatação, para que um revisor veja o que foi verificado e quando.

### 5.9 Erros comuns e limites

- Contar a presença como sucesso.
- Ignorar os pontos cegos.
- Pontuar as respostas dos questionários de forma inconsistente.

Cada erro leva a um relatório errado. Contar a presença teria marcado o portal de sinistros da MTI como concluído enquanto a maioria das sessões continuava clássica. Ignorar os pontos cegos pode esconder um certificado clássico atrás de um resultado híbrido. Pontuações inconsistentes nos questionários tornam os fornecedores impossíveis de comparar e convidam a reclamações dos que foram pontuados com rigor. Confira toda constatação baseada em ferramentas quanto a esses três erros antes que ela entre no rastreador. Corrija o que encontrar antes de relatar.

### Exercícios

- **EX021 — Oferecido versus negociado.** Explique a diferença usando o portal de sinistros. Rubrica: 3 = a ordem/preferência causa negociação clássica.
- **EX022 — Ponto cego.** O que um sensor passivo de TLS 1.3 não consegue ver, e de onde você obtém isso? Rubrica: 3 = o certificado; configuração/inventário de certificados.
- **EX023 — Pontuar respostas.** Pontue: "pronto para PQC"; "ML-KEM-768 híbrido no TLS 1.3 a partir da v8.2, entregue"; "roteiro 2027 para a RFC 9370". Rubrica: 3 = 1, 3 (se verificável) e 2.
- **EX024 — Constatação.** Escreva a constatação para a hr-intranet. Rubrica: 3 = observação, fonte, data, impacto, recomendação, responsável.
- **EX025 — Acompanhamento.** Liste as três perguntas a fazer antes de abrir uma constatação surpreendente. Rubrica: 3 = atualidade da ferramenta, recência dos dados, corroboração.

### Síntese

Os profissionais interpretam a saída das ferramentas e dos questionários atentos à preferência, à negociação e aos pontos cegos, e a transformam em constatações precisas.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Segurança quântica e pós-quântica: fluxo de trabalho operacional

### Objetivos de aprendizagem

Você vai (1) conduzir o fluxo de trabalho da migração como um ciclo repetível; (2) definir papéis, entradas e saídas de cada passo; (3) usar um rastreador com estados claros; (4) gerenciar as dependências de fornecedores e parceiros; e (5) relatar o progresso com medidas de resultado.

### 6.1 O ciclo

1. **Delimitar o escopo** dos serviços e confirmar a autorização. 2. **Inventariar** com evidências graduadas. 3. **Priorizar** pelo tempo de vida, pela exposição e pela rota de mudança. 4. **Planejar** cada item: controle, responsável, data, dependências. 5. **Implementar** por meio do processo de mudanças da equipe responsável. 6. **Verificar** com evidências de negociação. 7. **Registrar** o risco residual e as exceções. 8. **Relatar** e repetir a cada trimestre.

Cada passo produz uma entrada para o seguinte: a autorização para o inventário, as evidências graduadas para a priorização, um plano para a implementação. Na MTI, o ciclo roda trimestralmente, então um passo atrasado aparece no relatório seguinte, e não no fim do programa.

### 6.2 Papéis

Coordenador (você): conduz o ciclo, mantém o rastreador, escreve os relatórios. Responsáveis pelos sistemas: implementam as mudanças. Responsáveis pelos dados: confirmam os tempos de vida. Compras: cláusulas com fornecedores. Arquitetura de segurança: normas. Patrocinador executivo: decisões e aceitação de riscos. Auditoria interna: verificações independentes.

Na MTI, a equipe de infraestrutura é a responsável pelos servidores SFTP das resseguradoras, a subscrição confirma o tempo de vida do arquivo e o patrocinador aprova as exceções. Escreva os papéis no rastreador, para que cada item nomeie uma pessoa, e combine com cada uma o que ela vai fornecer e até quando.

### 6.3 Estados do rastreador

Use estados simples: *Desconhecido* → *Avaliado* → *Planejado* → *Em andamento* → *Implementado* → *Verificado* → *Encerrado* (ou *Exceção*). Um item passa a Verificado apenas com evidência de negociação, e não só com um ticket de mudança.

Cada estado precisa da sua própria evidência: um registro de inventário para Avaliado, um responsável e uma data para Planejado, um ticket de mudança para Implementado e logs de negociação para Verificado. Registre a data de cada mudança de estado, para que o rastreador mostre quanto tempo os itens levam. Um retorno a um estado anterior também é registrado, com um motivo, como aconteceu com o portal de corretores (Capítulo 10).

### 6.4 Dependências

Muitos itens aguardam fornecedores ou parceiros. Registre a dependência, o pedido enviado, a resposta e a data de acompanhamento. Escale os pedidos sem resposta por meio de compras ou da gestão de contas.

Na MTI, o item do SFTP das resseguradoras dependia de os parceiros atualizarem os seus clientes, e o item do arquivo dependia do roteiro de assinaturas do fornecedor. Cada um tinha no rastreador uma data de pedido e uma data de acompanhamento. Quando uma dependência é resolvida, registre a resposta como evidência e atualize juntos o grau e o estado do item. Seja breve.

### 6.5 Medidas de resultado

Relate: a proporção de itens de nível 1 Verificados; a proporção de Desconhecidos; o número de exceções abertas e quantas estão vencidas; as respostas de fornecedores recebidas. Evite contagens de atividade, como "reuniões realizadas".

Cada medida responde a uma pergunta sobre a qual um executivo pode agir: quanto está protegido, quanto ainda é desconhecido, quanto risco foi aceito e se os fornecedores estão se engajando. Defina cada medida uma única vez, por escrito, e mantenha a definição inalterada entre os trimestres, ou anote qualquer mudança no relatório. Mostre cada medida ao lado da do trimestre anterior.

### 6.6 Caso resolvido

O rastreador da MTI após um trimestre (sintético): 64 itens de nível 1 — 6 Verificados, 9 Implementados, 14 Em andamento, 18 Planejados, 11 Avaliados, 6 Desconhecidos; 3 exceções. Destaque do relatório: "9 % dos itens de nível 1 verificados, 9 % desconhecidos; SFTP das resseguradoras e transferências do arquivo em andamento; 3 exceções, nenhuma vencida."

O destaque relata resultados, e não esforço. Ele também torna a lacuna visível: os 9 itens Implementados ainda não são contados como Verificados, porque não existe evidência de negociação para eles. Os números vão parecer modestos; isso é correto. O patrocinador consegue ver quais itens precisam de um empurrão e quais precisam de coleta de evidências, e não de mais mudanças.

### 6.7 Tarefa prática

Monte um rastreador para dez itens da MTI e faça três deles avançarem pelos estados com evidências.

Dê a cada item uma fonte, um responsável e um estado atual. Para os três que avançarem, anexe a evidência que justifica cada transição: um registro de inventário, um responsável e uma data, um ticket de mudança e depois logs de negociação antes de Verificado. Peça a um colega que verifique se nenhum item pula um estado sem evidência e se as dependências têm datas de acompanhamento. Mantenha um registro de qual evidência você usou em cada avanço.

### 6.8 Cadência

Uma reunião de trabalho mensal com os responsáveis pelos sistemas mantém os itens em movimento; um relatório trimestral vai para o patrocinador; uma revisão anual revisita a norma, as prioridades e os tempos de vida. Mantenha cada reunião curta e conduzida pelo rastreador: primeiro os itens bloqueados, depois os itens a vencer, depois os novos desconhecidos.

Na MTI, foi na reunião mensal que se cobrou a dependência do SFTP das resseguradoras, e o relatório trimestral levou o resultado ao patrocinador. Cancele uma reunião em vez de realizá-la sem nada no rastreador para discutir, e envie depois de cada uma uma nota curta com as decisões e os novos prazos.

### 6.9 Erros comuns e limites

- Marcar itens como concluídos apenas com um ticket de mudança.
- Dependências sem datas de acompanhamento.
- Métricas de atividade nos relatórios.

Cada erro infla o progresso ou esconde atrasos. Um ticket de mudança mostra a intenção, mas a regressão do portal de corretores da MTI mostrou que a configuração pode ser revertida. Uma dependência sem data de acompanhamento pode ficar sem resposta por trimestres. Métricas de atividade, como reuniões realizadas, não dizem nada a um executivo sobre a proteção e tomam o lugar das medidas que dizem. Confira o rastreador e o relatório quanto aos três antes de cada relatório trimestral.

### Exercícios

- **EX026 — Ordenar o ciclo.** Ponha os oito passos em ordem e dê uma saída de cada um. Rubrica: 3 = ordem correta, com as saídas.
- **EX027 — Verificado.** Que evidência leva um item de Implementado a Verificado? Rubrica: 3 = logs de negociação/saída de ferramenta, datados.
- **EX028 — Destaque.** Calcule as proporções de Verificados e de Desconhecidos em 6.6. Rubrica: 3 = 6/64 ≈ 9 %, 6/64 ≈ 9 %.
- **EX029 — Registro de dependência.** Liste os campos de uma dependência de fornecedor. Rubrica: 3 = pedido, data, resposta, grau, acompanhamento, escalonamento.
- **EX030 — Pauta da reunião.** Esboce uma pauta mensal de 30 minutos. Rubrica: 3 = bloqueados, a vencer, desconhecidos, decisões.

### Síntese

Um ciclo repetível, com papéis claros, estados no rastreador, dependências gerenciadas e medidas de resultado, transforma a migração em trabalho rotineiro e relatável.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (inglês) →](../../en/book/MANUSCRIPT.md#ch-07)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre a MTI são sintéticos. Esta edição parcial traz as resoluções de EX001–EX030; as de EX031–EX060 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

**EX001.** AES-256: manter (Grover apenas tira a raiz quadrada da busca). RSA-2048: substituir (Shor). SHA-256: manter (sem quebra quântica prática). ECDSA P-256: substituir (Shor).

**EX002.** FIPS 203 ML-KEM: estabelecimento de chaves. FIPS 204 ML-DSA: assinaturas de uso geral. FIPS 205 SLH-DSA: assinaturas baseadas em hash.

**EX003.** HNDL: transferências de registros de apólices de vida por VPNs com troca de chaves clássica. Forjar depois: a AC raiz interna ou os documentos de apólice assinados que precisam permanecer verificáveis por décadas.

**EX004.** "O NIST IR 8547, um rascunho público inicial, propõe descontinuar os algoritmos vulneráveis ao quântico após 2030 e proibi-los após 2035; essas datas ainda não são definitivas."

**EX005.** "O TLS híbrido protege a troca de chaves da sessão contra decifração futura; os nossos certificados ainda usam assinaturas clássicas e precisam de uma migração separada."

**EX006.** Em risco quando 10 + 3 > *z*, ou seja, *z* < 13 anos.

**EX007.** Regras regulatórias de guarda de registros e contratos de apólices/sinistros, confirmados com os responsáveis pelos dados; a tabela de retenção como verificação cruzada.

**EX008.** Responsáveis pelos dados: perguntas sobre o tempo de vida. Responsáveis pelos sistemas: constatações claras e datas. Compras: texto das cláusulas. Jurídico/conformidade: mapeamento das obrigações. Patrocinador executivo: decisões e postura de risco. (Auditores: evidências.)

**EX009.** Ele está em risco sob todos os cronogramas supostos na varredura, porque o seu tempo de vida de 40 anos supera em muito qualquer *z* plausível.

**EX010.** "Registros que precisam permanecer privados por décadas poderiam ser gravados hoje e decifrados depois. Estamos protegendo essas transferências primeiro, depois o tráfego de sinistros e do portal. Essa ordem é correta qualquer que seja o cronograma quântico que se confirmar."

**EX011.** Sistemas; métodos; janela de tempo; tratamento dos dados; contatos (e condições de parada).

**EX012.** Coletar: versão do OpenSSH; `KexAlgorithms` configurados; tipos de chave de host. Não coletar: conteúdo dos arquivos transferidos; credenciais de usuários ou dados de sessão.

**EX013.** "Fonte: exportação de configuração (somente leitura); data 2026-10-06; coletor: coordenador; sistema: insurer-sftp-01/02; classificação: confidencial – inventário de segurança; ticket SEC-118."

**EX014.** Parar; não copiar nem usar a chave; comunicar imediatamente pelo processo de segurança; registrar o quê e onde; seguir as instruções sobre a revogação.

**EX015.** Registrar como "declaração do fornecedor (grau D), confidencial"; guardar com acesso restrito; compartilhar apenas com as pessoas que precisam dela para o programa.

**EX016.** O broker-portal tem troca de chaves híbrida; a sua assinatura continua RSA-2048 (clássica).

**EX017.** Handshake observado A; e-mail do fornecedor D; registro no banco de dados da AC B; diagrama de arquitetura C.

**EX018.** claims-app/key-exchange, policy-db/key-exchange, office-vpn/key-exchange: HNDL (gravar agora). broker-portal/signature e claims-app/signature: forjar depois.

**EX019.** 1 de 6 ativos = 17 %; relatá-la ao lado de cada número de cobertura, por exemplo "5 de 6 ativos avaliados; 1 (17 %) desconhecido".

**EX020.** "Determinar os algoritmos de troca de chaves e de assinatura usados pelo gravador de chamadas (modelo, versão). Método: questionário ao fornecedor e exportação de configuração. Responsável: TI da Central de Atendimento. Prazo: 30 dias."

**EX021.** O portal de sinistros oferece o grupo híbrido, mas lista o X25519 primeiro; a preferência do servidor prevalece, então os clientes negociam clássico, embora o híbrido esteja "presente".

**EX022.** O certificado do servidor (cifrado no TLS 1.3); obtê-lo da configuração ou do inventário de certificados.

**EX023.** "Pronto para PQC": 1. "ML-KEM-768 híbrido no TLS 1.3 a partir da v8.2, entregue": 3 se puder ser verificado, caso contrário 2. "Roteiro 2027 para a RFC 9370": 2.

**EX024.** "A hr-intranet oferece apenas grupos clássicos (auditoria de configuração, 6 de out.). Impacto: sessões com dados de RH expostas a HNDL. Recomendação: habilitar e preferir X25519MLKEM768 após verificar a biblioteca; verificar pelos logs. Responsável: TI Corporativa."

**EX025.** A ferramenta é atual o bastante para ver algoritmos PQ? Os dados são recentes? Outra fonte concorda?

**EX026.** Escopo (declaração de escopo), inventário (CBOM graduada), priorização (lista de prioridades), planejamento (planos dos itens), implementação (registros de mudança), verificação (evidências de negociação), registro (registro de riscos residuais/exceções), relato (relatório trimestral).

**EX027.** Evidência de negociação datada — logs ou saída de ferramenta mostrando o método híbrido no serviço pretendido.

**EX028.** Verificados 6/64 ≈ 9 %; Desconhecidos 6/64 ≈ 9 %.

**EX029.** Fornecedor, produto/versão, pedido enviado (data), resposta (data, conteúdo), grau da evidência, data de acompanhamento, via de escalonamento.

**EX030.** 5 min itens bloqueados e pedidos; 10 min itens a vencer no mês; 5 min novos desconhecidos e responsáveis; 5 min exceções perto do vencimento; 5 min decisões e ações.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; a situação das normas muda, então verifique de novo.

- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- IETF RFCs: 8784 (IKEv2 PSK mixing), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
