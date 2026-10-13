# Segurança Quântica e Pós-Quântica: Prática Especializada para Decisões em Escala Organizacional

- Idioma: português do Brasil (`pt`); curso de especialização de pós-graduação, dois anos em tempo parcial; aproximadamente 600 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: especialistas experientes em segurança — arquitetos, líderes de PKI e de redes, gestores de risco e de garantia — que já conhecem a criptografia clássica e as operações corporativas e agora precisam liderar a migração pós-quântica numa grande organização. Conhecimento de entrada: uma graduação anterior ou experiência profissional equivalente em segurança.
- Relação com os livros vizinhos: o [livro de bacharelado](../../../../bachelors-4-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) constrói os fundamentos e o [livro de engenharia](../../../../engineering-5-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) projeta e constrói migrações; o [livro de mestrado](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) as estuda como pesquisa. **Este livro trata da prática especializada: decidir, justificar, integrar e assegurar a migração em escala organizacional.** Ele pressupõe a matemática e se concentra no julgamento sob incerteza, nos padrões de evidência e na liderança.
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação credenciada. Não concede autorização para testar sistemas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública. O código de brinquedo dos laboratórios não é criptografia para uso; sistemas de produção devem usar implementações verificadas da [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), da [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), da [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) e da [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208).

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Doze capítulos se distribuem em quatro etapas: fundamentos de decisão (1–4), projeto e avaliação (5–6), integração, casos difíceis e garantia (7–9) e pesquisa, projeto e transferência (10–12). Cada capítulo tem objetivos de aprendizagem, ensino especializado, um caso resolvido, uma tarefa prática, erros comuns, cinco exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com Python 3; a saída impressa é mostrada para que você possa conferir a sua execução.

### O caso contínuo: Northgate Regional Health Trust

A **Northgate Regional Health Trust (NRHT)** é uma prestadora pública de saúde sintética, com seis hospitais, 40 clínicas e 22.000 funcionários. Ela opera um prontuário eletrônico do paciente (EHR) replicado entre dois data centers, um sistema de arquivamento e comunicação de imagens (PACS) com um leitor radiológico em nuvem, um serviço de genômica cujos dados precisam permanecer confidenciais por 50 anos, dispositivos médicos conectados, uma PKI interna, VPNs entre locais e um ecossistema de mais de 300 fornecedores. O seu conselho executivo nomeou você para liderar o programa pós-quântico. Todos os números sobre a NRHT são inventados.

### Política de fontes

As fontes primárias foram verificadas em 12 de outubro de 2026: NIST FIPS 203/204/205 (agosto de 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (rascunho público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) e [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). O FN-DSA (FIPS 206) e a norma do HQC ainda estavam em desenvolvimento. Verifique a situação de novo antes de se apoiar nela.

## Sumário

| Etapa | Capítulos |
|---|---|
| Fundamentos de decisão | [1 Tomada de decisão avançada em segurança](#ch-01) · [2 Prática atual](#ch-02) · [3 Evidências especializadas](#ch-03) · [4 Risco e ética avançados](#ch-04) |
| Projeto e avaliação | [5 Alternativas de projeto](#ch-05) · [6 Avaliação controlada](#ch-06) |
| Integração e garantia | [7 Integração organizacional](#ch-07) · [8 Casos difíceis](#ch-08) · [9 Liderança e garantia](#ch-09) |
| Pesquisa e transferência | [10 Leitura e crítica de pesquisas](#ch-10) · [11 Projeto aplicado](#ch-11) · [12 Revisão final e transferência](#ch-12) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem

Você vai (1) enquadrar a migração pós-quântica como tomada de decisão sob incerteza profunda; (2) distinguir escolhas robustas, ótimas e de minimização do arrependimento; (3) explicitar os julgamentos de valor dentro de um modelo de priorização; (4) construir um registro de decisão que sobreviva a auditorias e à rotatividade; e (5) reconhecer quando decidir agora e quando comprar informação.

### 1.1 Incerteza profunda

Os especialistas raramente carecem de opiniões sobre quando existirá um computador quântico criptograficamente relevante (CRQC); o que lhes falta é uma forma defensável de agir sem saber. O tempo de chegada *z* da desigualdade de Mosca (Mosca, 2018) não é uma grandeza com uma distribuição de probabilidade acordada. As estimativas públicas de recursos caíram — Gidney e Ekerå (2021) estimaram 20 milhões de qubits ruidosos para o RSA-2048, Gidney (2025) menos de um milhão sob hipóteses declaradas —, mas as estimativas de recursos não são previsões. Isso é *incerteza profunda*: as partes não conseguem concordar sobre as probabilidades, e talvez nem sobre o modelo. Sob incerteza profunda, otimizar o valor esperado com uma única distribuição inventada produz falsa confiança. Prefira decisões *robustas*: opções que têm desempenho aceitável em todos os cenários plausíveis, mesmo que não sejam ótimas em nenhum.

### 1.2 Três regras de decisão

A escolha pelo *valor esperado* pondera os resultados pelas probabilidades dos cenários; ela é adequada quando as probabilidades são críveis. A escolha *robusta* descarta as opções que falham gravemente em algum cenário plausível e depois escolhe entre as restantes pelo custo. O *minimax do arrependimento* compara cada opção com a melhor opção em retrospecto para cada cenário e escolhe aquela cujo pior arrependimento é o menor. Na migração quântica, os enquadramentos robusto e do arrependimento costumam concordar: começar a troca de chaves híbrida nos fluxos de dados de vida longa tem pouco arrependimento se os CRQCs chegarem tarde (o custo é modesto e constrói agilidade) e evita um grande arrependimento se chegarem cedo (os dados gravados ficam protegidos).

### 1.3 Os modelos codificam valores

Uma pontuação de priorização não é neutra. Multiplicar os registros pelo peso do dano favorece o volume; tratar a privacidade de cada pessoa ao longo da vida como primordial favorece os dados de vida longa, qualquer que seja o volume. O Laboratório D torna o ponto concreto.

Na NRHT, a escolha é entre pesos que contam registros e pesos que refletem o tempo de vida do dano a cada paciente. Nenhum deles está errado como aritmética, mas eles levam a primeiros projetos diferentes. O conselho deve ver as duas classificações e escolher, com o motivo registrado no registro de decisão, em vez de herdar uma escolha enterrada numa fórmula de planilha.

### 1.4 Atividade prática — Laboratório D

```python
# Lab D (ch 1): robust prioritisation - rank synthetic NRHT data flows by expected exposure across timeline scenarios.
flows = {  # name: (confidentiality years x, migration years y, records in transit per year, harm weight) - synthetic
    "genomics transfers": (50, 3, 2e4, 5), "EHR site replication": (25, 2, 3e6, 3),
    "imaging to cloud reader": (10, 2, 8e5, 2), "staff rota sync": (1, 1, 5e5, 1)}
scenarios = {"early z=8": (8, 0.25), "mid z=15": (15, 0.5), "late z=25": (25, 0.25)}  # (z, subjective weight)
score = {}
for name, (x, y, vol, harm) in flows.items():
    s = sum(w * (vol * harm if x + y > z else 0) for z, w in scenarios.values())
    score[name] = s
    print(f"{name:24s} late in: {[k for k, (z, _) in scenarios.items() if x + y > z]}")
print("ranking by weighted exposure:", [n for n, _ in sorted(score.items(), key=lambda kv: -kv[1])])
```

Saída esperada:

```text
genomics transfers       late in: ['early z=8', 'mid z=15', 'late z=25']
EHR site replication     late in: ['early z=8', 'mid z=15', 'late z=25']
imaging to cloud reader  late in: ['early z=8']
staff rota sync          late in: []
ranking by weighted exposure: ['EHR site replication', 'imaging to cloud reader', 'genomics transfers', 'staff rota sync']
```

A pontuação ponderada pelo volume classifica as imagens acima da genômica, embora os dados genômicos estejam expostos em todos os cenários e continuem sensíveis por 50 anos. A aritmética está correta; a questão é se o conselho aceita os seus valores. O trabalho de um especialista é mostrar tanto a coluna "late in", que carrega poucos valores, quanto a classificação ponderada, que carrega muitos, e tornar a escolha dos pesos uma decisão de governança explícita.

Mude o peso do dano da genômica de 5 para 50 e rode de novo: a classificação muda, embora nenhum fato sobre os fluxos tenha mudado. É esse o ponto a mostrar ao conselho. Mantenha a coluna "late in" como a evidência principal e apresente a classificação ponderada como uma visão entre várias, rotulada com os pesos usados.

### 1.5 Comprando informação

Parte da incerteza pode ser reduzida a baixo custo: se um fornecedor vai entregar o IKEv2 híbrido no ano que vem, quantos dispositivos são desconhecidos, qual é o período real de retenção de um conjunto de dados. O raciocínio do *valor da informação* pergunta se resolver uma incerteza poderia mudar a decisão; se não, não espere por ela. O momento do CRQC normalmente não pode ser comprado; os fatos do inventário normalmente podem.

Na NRHT, a decisão de agir sobre os dois fluxos de vida longa não dependia de conhecer z com mais precisão, então esperar por estimativas melhores não teria comprado nada. O inventário de dispositivos, por outro lado, era barato de melhorar e poderia mudar quais dispositivos são tratados primeiro. Registre quais incertezas foram reduzidas com compra de informação e quanto custaram.

### 1.6 Caso resolvido

O conselho da NRHT precisa decidir se financia agora um programa de 18 meses de troca de chaves híbrida nos enlaces entre locais ou se espera dois anos por uma renovação de rede planejada. Análise de cenários: se *z* = 8, esperar expõe o tráfego da genômica e da replicação do EHR a dois anos extras de coleta sem remédio; se *z* = 25, agir agora custa talvez 15 % a mais do que incorporar o trabalho à renovação. O pior arrependimento de esperar (divulgação irreversível de dados de 50 anos) domina o pior arrependimento de agir (custo extra moderado). Decisão: agir agora nos dois fluxos de vida longa; adiar o resto para a renovação; comprar imediatamente informação sobre o inventário de dispositivos.

### 1.7 Erros comuns e limites

- Tratar uma única data de CRQC como base do planejamento.
- Esconder julgamentos de valor dentro dos pesos da pontuação.
- Esperar por informações que não podem mudar a decisão.

Cada erro tem uma salvaguarda usada neste capítulo. Varie z ao longo dos cenários e relate quais escolhas se mantêm em todos eles. Mostre os pesos em qualquer pontuação e registre quem os aprovou. Antes de encomendar um estudo, pergunte se algum resultado plausível mudaria a decisão; se não, decida agora e anote por quê. Mantenha a tabela de cenários no registro de decisão.

### Exercícios

- **EX001 — Regras de decisão.** Para a decisão da NRHT entre agir agora e esperar, declare qual opção cada um dos enquadramentos — valor esperado (com *P*(*z* = 8) = 0,1), robusto e minimax do arrependimento — favorece, usando raciocínio qualitativo. Rubrica: 3 = os três enquadramentos aplicados com hipóteses declaradas.
- **EX002 — Valores no modelo.** Proponha uma mudança na pontuação do Laboratório D que classifique a genômica em primeiro lugar e declare o valor que ela codifica. Rubrica: 3 = mudança concreta e valor explícito.
- **EX003 — Valor da informação.** Nomeie duas incertezas que vale a pena resolver antes de a NRHT assinar um contrato de equipamentos de VPN, e uma pela qual não vale a pena esperar. Rubrica: 3 = justificadas pela sensibilidade da decisão.
- **EX004 — Registro de decisão.** Liste os campos de um registro de decisão que permitiriam a um auditor em 2032 entender a decisão de 2026. Rubrica: 3 = contexto, opções, cenários, valores/pesos, decisão, responsável, gatilho de revisão.
- **EX005 — Teste de robustez.** Defina um cenário que tornaria "agir agora nos fluxos de vida longa" uma decisão ruim e diga quão plausível ele é. Rubrica: 3 = cenário coerente com avaliação honesta.

### Síntese

As decisões da migração quântica são tomadas sob incerteza profunda. Os enquadramentos robustos e baseados no arrependimento, os julgamentos de valor explícitos e a compra direcionada de informação produzem decisões que podem ser defendidas quando o futuro chegar.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Segurança quântica e pós-quântica: prática atual

### Objetivos de aprendizagem

Você vai (1) resumir a situação das normas, das orientações e da implantação na data das fontes; (2) distinguir documentos finais, rascunhos e em desenvolvimento; (3) descrever como a troca de chaves híbrida chegou à implantação em larga escala; (4) avaliar a aplicabilidade das orientações nacionais e setoriais; e (5) manter um resumo vivo do "estado da prática" para uma organização.

### 2.1 Normas

As normas finais do NIST são a [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) (ML-KEM), a [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) (ML-DSA) e a [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (SLH-DSA), publicadas em agosto de 2024, junto com a [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) para as assinaturas baseadas em hash com estado LMS e XMSS. A [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) dá recomendações para os KEMs, incluindo a sua composição. O FN-DSA (FIPS 206, derivado do Falcon) e uma norma de KEM baseada no HQC, selecionado em 2025 como reserva baseada em códigos para o ML-KEM, estavam em desenvolvimento na data das fontes. Os especialistas devem manter um registro datado da situação de cada documento, porque a linguagem de compras e de auditoria muitas vezes cita rascunhos como se fossem finais.

### 2.2 Orientações de transição

O rascunho público inicial do [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) do NIST (novembro de 2024) propõe depreciar os algoritmos de chave pública vulneráveis à computação quântica com segurança de 112 bits depois de 2030 e proibir os algoritmos vulneráveis à computação quântica depois de 2035. O [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) discute considerações de agilidade criptográfica. O projeto [Migration to Post-Quantum Cryptography](https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms) do NCCoE publica guias de prática desenvolvidos com a indústria. Agências nacionais de outros países publicam os seus próprios roteiros; as suas datas e preferências de algoritmos diferem nos detalhes. Um especialista resume a mensagem convergente — inventariar agora, priorizar a confidencialidade de longo prazo, adotar híbridos durante a transição, planejar as assinaturas e a PKI — e sinaliza as divergências pertinentes às jurisdições da organização.

### 2.3 Implantação

A troca de chaves híbrida no TLS passou de experimento a padrão em poucos anos. O Chrome anunciou o Kyber híbrido em 2023 ([Chromium Blog](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)); o grupo padronizado X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) veio em seguida nos principais navegadores, CDNs e bibliotecas TLS. A *autenticação* pós-quântica está atrasada: os certificados ML-DSA exigem mudanças nas ACs, nos navegadores e nas políticas, e o seu tamanho (Capítulo 5) é um custo real de engenharia. O IKEv2 suporta trocas de chaves adicionais pela [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html), e o suporte dos fornecedores varia. A terminologia dos híbridos é definida pela [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html).

### 2.4 Caso resolvido

O resumo do estado da prática da NRHT, uma página, datado: normas finais (FIPS 203/204/205, SP 800-208); rascunhos (datas do IR 8547); em desenvolvimento (FN-DSA, HQC); implantação (TLS híbrido amplamente disponível em navegadores e CDNs; o leitor em nuvem do PACS da NRHT já negocia o X25519MLKEM768; equipamentos de VPN: o fornecedor A suporta a RFC 9370 no firmware atual, o fornecedor B "roteiro 2027"); lacunas (nenhuma AC pública emitindo certificados ML-DSA para a PKI da web em escala; fornecedores de dispositivos médicos em geral calados). O resumo é revisado trimestralmente e toda alegação tem um link.

Atribua um responsável a cada linha do resumo e uma data para a sua próxima verificação. Quando uma situação mudar, como um rascunho sendo finalizado, atualize a linha e guarde a versão anterior para que os leitores vejam o que mudou. O resumo se torna então uma evidência por si só para os auditores.

### 2.5 Tarefa prática

Escreva o resumo do estado da prática da sua organização (ou da NRHT). Marque cada item como final, rascunho, em desenvolvimento ou alegação de fornecedor.

Mantenha o resumo em uma página, com uma data no topo e um link ao lado de cada alegação. Inclua pelo menos um item de cada categoria e acrescente uma coluna com o que cada item significa para a organização. Peça a um colega que verifique se nenhum rascunho está descrito como final e se toda alegação de fornecedor está rotulada como alegação. Defina uma data para a próxima revisão trimestral antes de arquivá-lo.

### 2.6 Erros comuns e limites

- Citar datas de rascunhos como obrigações.
- Supor que a situação da implantação na web se aplica às VPNs, aos dispositivos ou à PKI.
- Resumos sem data, que envelhecem em silêncio.

Cada erro tem uma salvaguarda no resumo da NRHT: um rótulo de situação em cada documento, linhas separadas para web, VPN, PKI e dispositivos, e uma data no topo com revisão trimestral. Ao citar o IR 8547, mencione a sua condição de rascunho na mesma frase que as suas datas. Trate qualquer declaração de fornecedor como alegação até que ela seja observada em operação.

### Exercícios

- **EX006 — Registro de situação.** Classifique a FIPS 203, o IR 8547, a FIPS 206, a SP 800-227 e a RFC 10024 pela situação em 12 de outubro de 2026. Rubrica: 3 = cinco corretas, com fontes.
- **EX007 — Mensagem convergente.** Resuma em quatro tópicos o conselho em que as principais orientações convergem. Rubrica: 3 = inventário, priorização, híbridos, planejamento da PKI.
- **EX008 — Análise do atraso.** Explique por que a autenticação pós-quântica está atrasada em relação à troca de chaves na implantação do TLS. Rubrica: 3 = assimetria de urgência do HNDL, coordenação do ecossistema, tamanho.
- **EX009 — Alegação de fornecedor.** O fornecedor B da NRHT diz estar "pronto para PQC". Escreva três perguntas que transformem isso em alegações verificáveis. Rubrica: 3 = algoritmo/parâmetro, protocolo/norma, data/versão.
- **EX010 — Jurisdição.** A NRHT opera sob duas autoridades nacionais cujos roteiros diferem em três anos na depreciação. Como o programa deve definir a sua data interna? Rubrica: 3 = exigência vinculante mais cedo, justificativa documentada, revisão.

### Síntese

A prática atual combina normas finais, orientações de transição em rascunho e uma implantação desigual. Os especialistas mantêm resumos datados e com fontes que separam o que é exigido, proposto, disponível e apenas alegado.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Segurança quântica e pós-quântica: evidências especializadas

### Objetivos de aprendizagem

Você vai (1) projetar um programa de inventário criptográfico em escala organizacional; (2) graduar as evidências por método e confiança; (3) quantificar a cobertura e a parcela de desconhecidos; (4) tratar as evidências dos fornecedores; e (5) apresentar os resultados do inventário como evidência de decisão, e não como planilhas.

### 3.1 O inventário como programa

Em escala organizacional, uma lista de materiais criptográficos (CBOM) não é uma planilha pontual, mas um programa com responsáveis, fontes, calendários e métricas de qualidade. As fontes incluem sensores passivos de rede, bancos de dados de gestão de configuração, sistemas de gestão de certificados, scanners de código e de binários, APIs dos provedores de nuvem, logs de auditoria dos HSMs e atestados dos fornecedores. Cada uma alimenta observações — ativo, função, algoritmo, parâmetro, implementação, método, data — num repositório que pode ser consultado e comparado ao longo do tempo.

Atribua um responsável a cada fonte e um calendário para atualizá-la, e registre quando cada observação foi confirmada pela última vez. As diferenças entre os retratos mostram a mudança ao longo do tempo, incluindo retrocessos, como um grupo híbrido sendo desligado. O Laboratório I mostra a versão mais simples dessa agregação para alguns poucos ativos sintéticos da NRHT.

### 3.2 Graduação das evidências

Nem todas as observações são iguais. Uma graduação prática: **A** — observada em operação (handshake, log de HSM); **B** — lida de uma configuração autorizada; **C** — inferida da análise de código ou de binários; **D** — declaração do fornecedor; **U** — desconhecida. As decisões sobre o trabalho urgente devem se apoiar em evidências A ou B sempre que possível; as evidências D acionam a verificação dos ativos de alta prioridade. A graduação também orienta o investimento: se a maioria dos ativos de alta prioridade tem apenas evidência D, o próximo gasto é a verificação, e não a migração.

Registre o grau com cada observação e deixe-o decair: um handshake de grau A visto há um ano deve ser tratado como mais fraco que um visto na semana passada. Use o grau para escolher a próxima ação. Na NRHT, a grande parcela de ativos do nível 1 apoiada em declarações de fornecedores de grau D foi o que fez da verificação, e não da migração, o primeiro passo financiado.

### 3.3 Atividade prática — Laboratório I

```python
# Lab I (ch 3): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("pacs-gateway", "key-exchange", "X25519MLKEM768", "passive"), ("pacs-gateway", "signature", "RSA-2048", "config"),
    ("infusion-hub", "key-exchange", "ECDHE-P256", "passive"), ("infusion-hub", "signature", "ECDSA-P256", "code"),
    ("ehr-core", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("imaging-modality", "unknown", "unknown", "none"), ("site-vpn", "key-exchange", "ECDHE-P384", "config")]
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
quantum-vulnerable uses 5: pacs-gateway/signature, infusion-hub/key-exchange, infusion-hub/signature, ehr-core/key-exchange, site-vpn/key-exchange
hybrid key exchange present on: ['pacs-gateway']
```

Mesmo neste pequeno conjunto sintético, um ativo em seis é desconhecido, e o híbrido que existe cobre apenas a troca de chaves num único gateway. Na escala da NRHT, uma parcela de 17 % de desconhecidos em 40.000 ativos seria de 6.800 ativos — um programa por si só.

O laboratório trata um ativo como desconhecido quando o seu único registro não tem algoritmo, e conta os usos vulneráveis à computação quântica por função, e não por ativo. O pacs-gateway aparece duas vezes porque tem uma troca de chaves híbrida e uma assinatura clássica, o que mostra por que a troca de chaves e as assinaturas precisam ser acompanhadas separadamente.

### 3.4 Evidências dos fornecedores

Os fornecedores controlam boa parte da criptografia num hospital: plataformas de EHR, PACS, dispositivos, serviços em nuvem. Peça inventários estruturados (algoritmos, bibliotecas, versões), roteiros com datas e versões, e acesso para testes. As cláusulas contratuais devem exigir a divulgação e a notificação das mudanças criptográficas. Trate o silêncio como *desconhecido*, nunca como *conforme*.

Registre a resposta de cada fornecedor com a data, a pessoa que a deu e o grau de evidência que ela sustenta, em geral D até ser verificada. Pergunte primeiro aos fornecedores por trás do maior número de ativos do nível 1; na NRHT, 40 fornecedores respondem por 80 % do nível 1. Repita as perguntas a cada renovação de contrato.

### 3.5 Apresentando as evidências

Os executivos precisam de respostas para três perguntas: que parcela dos fluxos prioritários está protegida, quão confiantes estamos, e o que é desconhecido? Apresente a cobertura por grau de evidência e nível de prioridade, e não contagens brutas. Mostre as tendências ao longo dos trimestres; uma parcela de desconhecidos em queda é progresso mesmo antes de qualquer algoritmo mudar.

Na NRHT, o primeiro relatório ao conselho começou pela parcela confirmada dos ativos do nível 1, 22 %, e não por uma contagem total. Um gráfico que mostra os graus por nível ao longo dos trimestres sucessivos permite ao conselho ver o progresso da verificação mesmo quando nenhum algoritmo ainda mudou. Mantenha os dados subjacentes disponíveis para quem os pedir.

### 3.6 Caso resolvido

O inventário do primeiro trimestre da NRHT (sintético): 41.200 ativos; nível de prioridade 1 (confidencialidade de longo prazo ou confiança de longo prazo) com 1.850 ativos. Do nível 1: 22 % de grau A/B, 31 % de grau C, 29 % de grau D, 18 % desconhecidos. O relatório ao conselho começa com "conseguimos confirmar a criptografia de apenas 22 % dos nossos ativos mais importantes"; a resposta financiada é a cobertura por sensores nos enlaces entre locais e um questionário aos 40 fornecedores por trás de 80 % do nível 1.

O relatório é desconfortável, mas honesto, e leva diretamente a uma ação financiada. Nos trimestres seguintes, a mesma divisão mostra se a verificação está funcionando; na revisão do segundo ano, a parcela de desconhecidos do nível 1 havia caído, que é a medida que o conselho consegue acompanhar.

### 3.7 Erros comuns e limites

- Tratar as declarações dos fornecedores como observações.
- Relatar contagens de ativos sem nível e grau.
- Apagar as observações desatualizadas, em vez de rebaixá-las.

Cada erro tem uma salvaguarda. Gradue as declarações dos fornecedores como D até serem observadas. Relate as contagens por nível e grau, nunca sozinhas. Mantenha as observações desatualizadas, rebaixe-as e registre a data em que foram confirmadas pela última vez, para que o histórico continue visível e um retrocesso possa ser detectado. Na NRHT, os 29 % dos ativos do nível 1 apoiados em declarações de fornecedores foram relatados como grau D, e não como cobertos, e é por isso que o conselho financiou primeiro a verificação. Mantenha o grau junto com cada contagem na mesma tabela.

### Exercícios

- **EX011 — Gradue.** Gradue: captura do handshake TLS do enlace de replicação do EHR; PDF do fornecedor afirmando "AES-256 e RSA-3072"; varredura de binários que encontra o OpenSSL 3.x; campo do CMDB "crypto: standard". Rubrica: 3 = A, D, C, B-ou-U com justificativa para o caso do CMDB.
- **EX012 — Escala dos desconhecidos.** Se a NRHT reduzir os desconhecidos do nível 1 de 18 % para 6 %, quantos ativos do nível 1 saíram da classe desconhecida? Rubrica: 3 = 0,12 × 1.850 = 222.
- **EX013 — Cláusula para fornecedores.** Redija uma cláusula que exija a notificação das mudanças criptográficas. Rubrica: 3 = escopo, prazo, conteúdo, sanção.
- **EX014 — Regra de desatualização.** Proponha uma regra para rebaixar as observações pela idade e justifique os limiares. Rubrica: 3 = decaimento do grau por tempo, ligado às taxas de mudança.
- **EX015 — Métrica para o conselho.** Projete um único gráfico para o conselho que mostre a confiança do inventário no nível 1. Rubrica: 3 = parcelas de grau empilhadas por trimestre, com os desconhecidos destacados.

### Síntese

As evidências especializadas são graduadas, datadas e atentas aos fornecedores. A cobertura e a parcela de desconhecidos são resultados de primeira classe, e o conselho vê confiança, e não planilhas.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Risco e ética avançados

### Objetivos de aprendizagem

Você vai (1) quantificar o risco quântico com medidas de exposição baseadas em cenários; (2) tratar os riscos com longa latência e dano irreversível; (3) analisar as obrigações éticas para com os titulares dos dados cujo dano ultrapassa o horizonte da organização; (4) lidar com as questões de uso dual e de divulgação no nível especializado; e (5) documentar adequadamente a aceitação do risco residual.

### 4.1 Risco latente e irreversível

O risco do harvest-now-decrypt-later (HNDL) é latente: o evento de perda (a coleta) pode já ter acontecido, e o dano (a decifração) acontece depois e não pode ser desfeito. Os registros de riscos padrão, construídos para eventos com detecção e recuperação imediatas, o representam mal. Represente o HNDL como *exposição acumulada por ano*: o volume de dados de vida longa que atravessa enlaces interceptáveis sob troca de chaves clássica a cada ano, ponderado pelo dano, em cada cenário de cronograma. Cada ano de atraso acrescenta um ano de exposição que nenhuma migração posterior remove.

Na NRHT, o enlace da genômica mostra o padrão: 20.000 registros por ano o atravessam sob troca de chaves clássica, e cada ano soma ao que um interceptador pode já ter. Relate essa exposição por ano e por cenário no registro de riscos, e diga claramente que a exposição passada não pode ser reduzida por uma migração posterior.

### 4.2 Falsificação posterior e risco sistêmico

O risco de falsificação posterior depende das âncoras de confiança e dos canais de atualização. Uma chave de assinatura de código falsificada de um dispositivo médico amplamente implantado poderia afetar a segurança dos pacientes em muitos hospitais ao mesmo tempo; o risco é sistêmico, e não local. Os especialistas devem identificar as âncoras de confiança cujo comprometimento tem efeitos correlacionados e priorizar a sua migração ou controles compensatórios, como assinaturas múltiplas ou chaves de verificação vinculadas ao hardware que possam ser rotacionadas.

Na NRHT, a frota de bombas de infusão é o exemplo mais claro: o seu firmware é verificado com uma assinatura RSA por uma ROM de boot que não pode mudar. Uma assinatura falsificada afetaria todas as bombas ao mesmo tempo. Liste essas âncoras de confiança separadamente no registro, com o número de dispositivos e de locais que dependem de cada uma.

### 4.3 Obrigações para com os titulares dos dados

Os dados genômicos de um paciente revelam informações sobre os seus parentes e continuam sensíveis por gerações. O horizonte de planejamento da organização (ciclos orçamentários, contratos) é mais curto que o horizonte do dano. Eticamente, as pessoas que carregam o risco — os pacientes — não são parte da decisão, o que reforça o dever de cuidado. Os especialistas devem insistir para que os horizontes do dano, e não os calendários de retenção da organização, definam o *x* desses dados, e para que a minimização (Capítulo 5) seja considerada antes dos controles criptográficos.

Para os dados genômicos, isso significa definir x em torno de 50 anos, mesmo que o calendário de retenção seja mais curto, porque as cópias mantidas por outros não seguem o calendário da NRHT. Registre esse raciocínio no relatório de impacto à privacidade. Sempre que possível, envolva representantes dos pacientes nas decisões sobre dados que afetam parentes.

### 4.4 Uso dual e divulgação

Os inventários em escala organizacional são mapas de fraquezas. Restrinja o acesso, publique apenas agregados e trate os relatos de vulnerabilidades dos fornecedores sob divulgação coordenada. Os testes ativos de negociação, de downgrade ou de comportamento sob falhas pertencem a ambientes de teste isolados e autorizados; um especialista que dirige outras pessoas é responsável por garantir que esses limites estejam escritos.

Escreva quem pode ver o inventário completo e quem recebe apenas agregados, e revise a lista todo ano. Os testes em ambientes isolados devem ser aprovados por escrito, com um responsável nomeado e uma data de término. O relato de uma fraqueza por um fornecedor é tratado sob a divulgação acordada, com o fornecedor avisado antes de qualquer publicação.

### 4.5 Aceitação do risco residual

Quando um risco não pode ser reduzido a tempo — uma modalidade de imagem legada que não pode ser atualizada —, o executivo responsável o aceita formalmente: escopo, justificativa, controles compensatórios, data de expiração e gatilho de revisão. A aceitação sem expiração se torna permanente por padrão.

Registre cada aceitação no registro de riscos residuais com o nome do executivo responsável e a data. Revise-a antes da expiração; se o risco ainda não puder ser reduzido, o executivo precisa aceitá-lo de novo, com uma nova data. Na revisão do segundo ano da NRHT, seis aceitações haviam passado da expiração sem revisão, o que levou ao escalonamento automático.

### 4.6 Caso resolvido

O serviço de genômica da NRHT envia 20.000 registros por ano a um parceiro de pesquisa externo por um enlace TLS com troca de chaves clássica. Enquadramento da exposição: cada ano acrescenta 20.000 registros sensíveis por toda a vida ao que um interceptador poderia ter. Enquadramento ético: o horizonte do dano é de ~50 anos e inclui os parentes. Decisão: migrar esse enlace para a troca de chaves híbrida em até três meses, reduzir os dados enviados levando a análise para um ambiente de pesquisa confiável, e registrar que as transferências dos anos anteriores continuam expostas — um risco residual que o conselho aceita formalmente, com uma nota no relatório de impacto à privacidade.

### 4.7 Erros comuns e limites

- Pontuar o HNDL como um incidente comum com impacto imediato.
- Deixar os calendários de retenção definirem os horizontes do dano.
- Aceitações de risco sem expiração.

Cada erro tem uma salvaguarda. Represente o harvest-now-decrypt-later como exposição anual que não pode ser removida depois. Defina o x de cada conjunto de dados a partir do horizonte do dano, e não da retenção. Dê a toda aceitação uma data de expiração e um revisor nomeado, e escalone automaticamente quando uma delas passar. Na NRHT, o enlace da genômica foi registrado como exposição anual com um horizonte de 50 anos, e a aceitação das transferências anteriores foi anotada no relatório de impacto à privacidade com uma data de revisão. Use esse registro como modelo para os demais.

### Exercícios

- **EX016 — Acúmulo da exposição.** Se a migração do enlace da genômica atrasar 18 meses, quantos registros adicionais ficam expostos? Rubrica: 3 = 30.000, com raciocínio.
- **EX017 — Âncora sistêmica.** Identifique duas âncoras de confiança da NRHT com efeitos de falha correlacionados. Rubrica: 3 = duas âncoras plausíveis, com explicação.
- **EX018 — Formulário de aceitação.** Escreva uma aceitação de risco residual para um aparelho de ressonância magnética legado com verificação de firmware apenas RSA. Rubrica: 3 = escopo, justificativa, controles compensatórios, expiração, gatilho.
- **EX019 — Argumento ético.** Argumente, em cinco frases, por que o horizonte do dano aos pacientes deve definir *x*. Rubrica: 3 = quem carrega o risco não é parte, irreversibilidade, dever de cuidado.
- **EX020 — Controle de acesso ao inventário.** Defina quem pode ver a CBOM completa e por quê. Rubrica: 3 = menor privilégio, relatórios agregados, auditoria.

### Síntese

O risco quântico é latente, irreversível e às vezes sistêmico. Os especialistas o expressam como exposição acumulada, definem os horizontes pelo dano aos titulares dos dados, protegem os inventários como informação sensível e tornam a aceitação do risco residual explícita e limitada no tempo.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Segurança quântica e pós-quântica: alternativas de projeto

### Objetivos de aprendizagem

Você vai (1) enumerar as alternativas de projeto para o estabelecimento de chaves, a autenticação e a proteção dos dados; (2) comparar os projetos pós-quântico puro, híbrido, aumentado por PSK e de minimização; (3) quantificar os custos em bytes da autenticação; (4) escolher os conjuntos de parâmetros segundo a política; e (5) documentar as alternativas para que os revisores possam questionar a escolha.

### 5.1 Alternativas de estabelecimento de chaves

O *híbrido PQ/T* (no sentido da [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) combina o ML-KEM com o ECDH, de modo que a sessão seja segura se qualquer um deles se mantiver; é o projeto de transição padrão no TLS (X25519MLKEM768) e no IKEv2 (trocas de chaves adicionais da RFC 9370). O *pós-quântico puro* usa apenas o ML-KEM; ele reduz a complexidade e é atraente onde a política o exige ou onde o componente tradicional não acrescenta valor, mas remove a proteção contra uma quebra inesperada ou uma falha de implementação. O *aumento por PSK* mistura uma chave simétrica pré-compartilhada no handshake (como na [RFC 8784](https://www.rfc-editor.org/rfc/rfc8784.html) para o IKEv2); é uma proteção provisória rápida contra o HNDL em alguns enlaces fixos, mas escala mal. A *minimização e a rearquitetura* enviam menos dados de vida longa — um controle independente dos algoritmos. A [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) discute a composição de KEMs e os requisitos dos combinadores.

### 5.2 Alternativas de autenticação

Opções para os certificados: manter os certificados clássicos enquanto se monitora a prontidão do ecossistema (aceitável onde o risco de falsificação posterior é baixo e os certificados têm vida curta); emitir certificados ML-DSA primeiro em ecossistemas fechados, como a PKI interna e as frotas de dispositivos; usar abordagens de certificados duplos ou compostos durante a transição, onde as normas e os produtos as suportarem; e usar assinaturas baseadas em hash (SLH-DSA, LMS, XMSS) onde o conservadorismo ou a simplicidade da verificação importam, notadamente no firmware.

Escolha pelo ecossistema. A PKI interna e as frotas de dispositivos da NRHT são fechadas, então o ML-DSA pode começar por elas. Os certificados públicos da web continuam clássicos até que os navegadores e as autoridades certificadoras suportem a emissão pós-quântica em escala. Para o firmware, as assinaturas baseadas em hash servem ao caso conservador, desde que o estado seja gerenciado corretamente.

### 5.3 Atividade prática — Laboratório B

```python
# Lab B (ch 5): bytes of authentication in a TLS handshake for different signature choices.
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

Para uma malha de serviços interna numa rede de data center, 15 kB por handshake é aceitável. Para dispositivos de clínicas em enlaces restritos, ou protocolos com limites pequenos de mensagem, pode não ser. A resposta de projeto é escolher onde a autenticação pós-quântica entra primeiro, enxugar as cadeias e medir — e não supor.

Os tamanhos do laboratório vêm das normas; os 400 bytes de outros campos do certificado e as duas assinaturas embutidas são hipóteses aproximadas. Mude a profundidade da cadeia ou o número de assinaturas embutidas para ver com que rapidez os totais crescem. Use o resultado para decidir onde medir primeiro e depois meça em handshakes reais num laboratório.

### 5.4 Política de parâmetros

Os conjuntos de parâmetros se associam às categorias do NIST: ML-KEM-512/768/1024 às categorias 1/3/5; ML-DSA-44/65/87 às 2/3/5. Um especialista define a política explicitamente (por exemplo, categoria 3 por padrão, categoria 5 para parceiros ligados à segurança nacional) e registra o porquê. Parâmetros máximos uniformes desperdiçam bytes e ciclos; escolhas improvisadas tornam as auditorias penosas.

Escreva a política na norma criptográfica, com um motivo curto para cada padrão e cada exceção. Na NRHT, o padrão para o novo estabelecimento de chaves é o híbrido com ML-KEM-768. Revise a política quando as normas mudarem, como quando o FN-DSA for finalizado.

### 5.5 Caso resolvido

A replicação do EHR entre locais da NRHT roda sobre IPsec. Alternativas: (a) IKEv2 híbrido com ML-KEM-768 nos equipamentos do fornecedor A (suportado agora); (b) PSKs da RFC 8784 para os dois locais do fornecedor B até 2027; (c) rearquitetar a replicação para enviar apenas os deltas, cortando o volume em 70 %; (d) ML-KEM puro — rejeitado porque a implementação do fornecedor A é nova e a proteção do híbrido é valiosa. Escolhido: (a) + (b) + (c), com (b) expirando quando o fornecedor B entregar o suporte híbrido. A autenticação continua clássica por enquanto; o plano da PKI interna (Capítulo 8) a trata.

Registre a alternativa rejeitada e o seu motivo no registro de projeto, para que ela possa ser reconsiderada quando a implementação do fornecedor A amadurecer.

### 5.6 Erros comuns e limites

- Escolher o pós-quântico puro para "ser moderno" sem considerar a proteção do híbrido.
- Esquemas de PSK sem rotação e sem distribuição segura.
- Ignorar a minimização porque ela não é criptografia.

Cada erro tem uma salvaguarda. Mantenha o híbrido a menos que haja um motivo para abandoná-lo, e registre esse motivo. Para as PSKs, escreva como as chaves são geradas, distribuídas e rotacionadas, e quando expiram. Conte a minimização como um controle de segurança ao lado dos criptográficos. Na NRHT, as PSKs do fornecedor B receberam uma expiração vinculada ao suporte híbrido, e a replicação foi reprojetada para enviar deltas, cortando o volume em 70 %.

### Exercícios

- **EX021 — Tabela de alternativas.** Compare o híbrido, o pós-quântico puro, o aumento por PSK e a minimização quanto à proteção contra o HNDL, à complexidade, à escalabilidade e ao risco residual. Rubrica: 3 = quatro alternativas × quatro critérios, defensável.
- **EX022 — Orçamento de bytes.** A partir do Laboratório B, por que fator o ML-DSA-65 excede o ECDSA P-256 em bytes de autenticação? Rubrica: 3 = 21.249/1.290 ≈ 16,5.
- **EX023 — Política de parâmetros.** Escreva uma política de parâmetros de duas linhas para a NRHT, com justificativa. Rubrica: 3 = categorias por uso, justificativa.
- **EX024 — Expiração das PSKs.** Especifique as condições sob as quais a alternativa (b) de 5.5 precisa terminar. Rubrica: 3 = suporte do fornecedor verificado, migração testada, data-limite.
- **EX025 — Caso do pós-quântico puro.** Descreva um contexto em que o ML-KEM puro é a melhor escolha. Rubrica: 3 = exigência de política ou contexto restrito, com a perda da proteção do híbrido argumentada.

### Síntese

As alternativas de projeto abrangem as abordagens híbrida, pura, aumentada por PSK e de minimização para o estabelecimento de chaves, e as abordagens em estágios, começando pelos ecossistemas fechados, para a autenticação. Uma política de parâmetros explícita e orçamentos de bytes tornam a escolha revisável.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Segurança quântica e pós-quântica: avaliação controlada

### Objetivos de aprendizagem

Você vai (1) projetar avaliações controladas das mudanças da migração; (2) definir os limiares de decisão antes de coletar os dados; (3) usar limites de confiança nas decisões de implantação em estágios; (4) avaliar a interoperabilidade num parque heterogêneo; e (5) relatar os resultados da avaliação com os seus limites de validade.

### 6.1 Perguntas de avaliação

A avaliação especializada responde a perguntas de decisão: ativar um grupo híbrido no gateway do PACS mantém as taxas de falha dentro do orçamento? O ML-DSA na PKI interna quebra alguma aplicação clínica? Quais versões de firmware de VPN negociam os métodos pretendidos? Cada pergunta precisa de uma população, uma medida, um limiar definido com antecedência e uma regra de decisão.

Na NRHT, a pergunta do gateway do PACS foi respondida com uma população de tipos reais de cliente, uma medida de taxa de falhas, um limiar de 0,09 % acordado com antecedência e uma regra para promover, segurar ou excluir. Escreva os mesmos quatro elementos para cada pergunta antes de coletar os dados, e arquive-os com o registro de mudança.

### 6.2 Limiares antes dos dados

Defina os orçamentos de falhas e os limiares de latência antes do experimento, acordados com os responsáveis pelos serviços. Os limiares definidos depois derivam para o que quer que os dados mostrem. Um orçamento típico: a taxa de falhas de handshake pode subir no máximo 0,04 ponto percentual acima da referência, julgada pelo limite superior de confiança de 95 %.

Acorde o orçamento por escrito com o responsável pelo serviço e registre-o antes do primeiro canário. Na NRHT, o orçamento de 0,04 ponto percentual sobre uma referência de 0,05 % produziu o limiar de 0,09 % usado no gateway do PACS. Se o orçamento precisar mudar, mude-o antes do próximo estágio, e não depois de olhar os resultados.

### 6.3 Atividade prática — Laboratório K

```python
# Lab K (ch 6): canary gate for enabling a hybrid group - promote only if failures stay within budget.
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

O primeiro estágio é segurado pela incerteza, e não por evidência de dano; o local com proxy é segurado por evidência de dano. São achados diferentes e merecem ações diferentes — prorrogar o primeiro estágio; investigar o segundo.

O portão usa o limite superior de Wilson porque contagens pequenas de falhas tornam os intervalos mais simples pouco confiáveis. O primeiro estágio é segurado apenas porque 5.000 tentativas são poucas demais para mostrar que a taxa está dentro do orçamento. O local com proxy é segurado porque o seu limite superior fica bem acima do orçamento. Registre as duas decisões com o tamanho do estágio e a data.

### 6.4 Matrizes de interoperabilidade

Os hospitais têm caudas longas de clientes: navegadores antigos em estações clínicas, navegadores embutidos em dispositivos, sistemas de parceiros. Uma matriz de interoperabilidade lista os tipos de cliente × as configurações de servidor, com os resultados observados. Construa-a primeiro num laboratório com clientes representativos e depois confirme com a telemetria de produção. As lacunas da matriz são desconhecidos a resolver antes de uma implantação ampla.

Na NRHT, a matriz de laboratório com 14 tipos de cliente encontrou dois visualizadores embutidos que falhavam com o ClientHello maior antes de qualquer implantação em produção. Mantenha a matriz com datas e versões, e atualize-a à medida que os clientes são atualizados ou aposentados. Uma célula marcada como desconhecida bloqueia a implantação ampla até ser preenchida.

### 6.5 Validade

As avaliações de laboratório têm limites de validade externa: os proxies de inspeção reais, as condições de Wi-Fi e o firmware dos dispositivos diferem. Os canários de produção têm limites de validade interna: mudanças concorrentes e ciclos semanais. Relate os dois e prefira as conclusões sustentadas pelas evidências do laboratório e do canário juntas.

Declare em cada relatório de avaliação quais conclusões se apoiam em evidências de laboratório, quais em evidências de canário e quais em ambas. Na NRHT, o problema do proxy de inspeção apareceu num canário de produção, e não no laboratório, e é por isso que os dois tipos de evidência são necessários. Liste as mudanças concorrentes durante o período do canário.

### 6.6 Caso resolvido

A NRHT avalia a troca de chaves híbrida no gateway do PACS. Limiar pré-definido: limite superior ≤ 0,09 % de falhas. Matriz de laboratório: 14 tipos de cliente; dois visualizadores embutidos falham com o ClientHello maior. Canário de 1 %, prorrogado para duas semanas até o limite superior cair dentro do limiar: promover. Canário de 10 %: um hospital excede o limiar — o seu proxy de inspeção legado. Decisão: excluir esse hospital, atualizar o proxy, continuar nos demais; os dois visualizadores embutidos são encaminhados por um listener apenas clássico, com risco residual documentado e um chamado aberto com o fornecedor.

A decisão trata cada problema separadamente, o que os resultados agregados teriam escondido. Registre o hospital excluído e o listener apenas clássico no registro de exceções, cada um com um responsável e uma data de expiração.

### 6.7 Erros comuns e limites

- Definir os limiares depois de ver os dados.
- Agregar os locais, o que esconde um local com falhas.
- Conclusões apenas de laboratório para decisões de produção.

Cada erro tem uma salvaguarda na avaliação do PACS: um limiar acordado antes de qualquer dado, resultados relatados por local e decisões baseadas tanto na matriz de laboratório quanto nos canários de produção. Um resultado agregado que parece aceitável pode esconder um local como o hospital com o proxy legado. Escreva o limiar, a divisão por local e a fonte das evidências em toda decisão de implantação, para que um revisor possa conferir cada uma.

### Exercícios

- **EX026 — Regra de decisão.** Escreva uma regra de decisão para promover um canário que inclua limiar, estatística e duração mínima. Rubrica: 3 = os três, justificados.
- **EX027 — Interpretar as retenções.** Explique as ações diferentes para a primeira e a terceira retenção do Laboratório K. Rubrica: 3 = ampliar a amostra vs. investigar a causa.
- **EX028 — Projeto da matriz.** Liste seis tipos de cliente que a NRHT precisa incluir na sua matriz de interoperabilidade. Rubrica: 3 = seis tipos realistas e distintos.
- **EX029 — Agregação.** Dê um exemplo numérico em que os resultados agregados passam, mas um local falha. Rubrica: 3 = aritmética correta mostrando o mascaramento.
- **EX030 — Declaração de validade.** Escreva um parágrafo de validade para a avaliação do PACS. Rubrica: 3 = limites internos e externos, com os efeitos.

### Síntese

A avaliação controlada fixa os limiares com antecedência, usa limites de confiança, mapeia a interoperabilidade nas populações reais de clientes e relata os limites de validade, para que as decisões de implantação se apoiem em evidências, e não em esperança.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (inglês) →](../../en/book/MANUSCRIPT.md#ch-07)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre a NRHT são sintéticos. Esta edição parcial traz as resoluções de EX001–EX030; as de EX031–EX060 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

**EX001.** Valor esperado com *P*(*z* = 8) = 0,1: esperar economiza ~15 % do custo do programa em 90 % dos casos, mas arrisca uma divulgação irreversível em 10 %; se o dano for muito valorizado, o valor esperado ainda favorece agir, mas o resultado depende da probabilidade inventada. Robusto: esperar falha gravemente no cenário antecipado, então é descartado; agir agora. Minimax do arrependimento: o pior arrependimento de esperar (divulgação irreversível) excede o pior arrependimento de agir (custo moderado); agir agora.

**EX002.** Pontuar por registros ponderados pelo tempo de vida — por exemplo, multiplicar por (*x* + *y* − *z*) anos de exposição residual, ou pelo peso do dano ao quadrado para os dados genéticos — ou limitar a influência do volume com log(volume). Isso codifica o valor de que o dano ao longo da vida dos indivíduos (e dos parentes) importa mais que as contagens de registros.

**EX003.** Vale a pena resolver: se o firmware do equipamento suporta agora o IKEv2 híbrido da RFC 9370 (muda a escolha do fornecedor); a vida útil de suporte planejada do equipamento (muda o alinhamento com a renovação). Não vale a pena esperar: a data de chegada do CRQC — impossível de resolver, e a decisão é robusta a ela.

**EX004.** Contexto e pergunta; opções consideradas; cenários e hipóteses (incluindo a faixa de *z* e as fontes); valores e pesos; evidências e graus; decisão e justificativa; responsável e aprovador; data; gatilhos de revisão (mudança das orientações, entrega do fornecedor, nova estimativa).

**EX005.** Um cenário em que uma falha grave de implementação nos primeiros equipamentos híbridos cause interrupções ou vazamentos generalizados, ou em que o ML-KEM seja enfraquecido antes da implantação; plausibilidade de baixa a moderada para as falhas de implementação (precedente do KyberSlash), mitigada pelos híbridos, por firmware verificado e pela implantação em estágios.

**EX006.** FIPS 203: final (2024). IR 8547: rascunho público inicial. FIPS 206 (FN-DSA): em desenvolvimento. SP 800-227: recomendações finais (2025). RFC 10024: RFC publicada pela IETF que especifica os grupos TLS híbridos.

**EX007.** Construir e manter um inventário criptográfico; priorizar os dados que precisam de confidencialidade de longo prazo (HNDL); usar híbridos PQ/T durante a transição; planejar a migração da PKI e das assinaturas e a agilidade criptográfica.

**EX008.** O HNDL torna a troca de chaves urgente, enquanto a falsificação precisa de um CRQC no momento do ataque; as mudanças de autenticação exigem mudanças coordenadas nas ACs, nos navegadores, nas políticas e nos repositórios de raízes; os certificados ML-DSA acrescentam muitos kilobytes, aumentando os custos de desempenho e de compatibilidade.

**EX009.** Quais algoritmos e conjuntos de parâmetros (por exemplo, ML-KEM-768 conforme a FIPS 203) em qual mecanismo de protocolo (por exemplo, a RFC 9370 para o IKEv2)? Quais versões do produto o suportam agora, e em que data para as demais? Podemos testá-lo, e é fornecido um inventário criptográfico?

**EX010.** Adotar a data mais cedo que seja vinculante em qualquer jurisdição para os sistemas afetados, ou justificar uma data posterior com aceitação de risco documentada; registrar a justificativa e marcar uma revisão de governança quando qualquer uma das autoridades atualizar as orientações.

**EX011.** Captura do handshake: A (observada). PDF do fornecedor: D (declaração do fornecedor). Varredura de binários: C (inferida do código). CMDB "crypto: standard": na prática U — vem da configuração, mas não informa nada, então não pode sustentar uma decisão.

**EX012.** (0,18 − 0,06) × 1.850 = 222 ativos.

**EX013.** "O fornecedor deverá notificar a NRHT por escrito com pelo menos 90 dias de antecedência sobre qualquer mudança nos algoritmos, parâmetros, bibliotecas ou protocolos criptográficos dos produtos ou serviços entregues, descrevendo a mudança, as versões afetadas e o impacto na interoperabilidade. As mudanças emergenciais para correções de segurança deverão ser notificadas em até 5 dias úteis. A falta de notificação constitui violação material."

**EX014.** O grau decai um nível quando as observações excedem um limiar de idade ligado à taxa de mudança: observações de rede com mais de 30 dias → B; configuração com mais de 90 dias → C; declarações de fornecedores com mais de 12 meses → U. As camadas que mudam rápido decaem mais rápido.

**EX015.** Uma barra empilhada por trimestre para os ativos do nível 1, mostrando as parcelas dos graus A, B, C, D e U, com U numa cor contrastante e a sua porcentagem rotulada; linha de meta para U.

**EX016.** 20.000 registros/ano × 1,5 ano = 30.000 registros adicionais.

**EX017.** A AC raiz interna (ancora as VPNs, as identidades dos dispositivos e o TLS interno em toda parte); a chave de assinatura de firmware de um grande fornecedor de dispositivos (afeta todas as unidades de uma frota em vários hospitais ao mesmo tempo).

**EX018.** Escopo: aparelho de ressonância magnética modelo X, 6 unidades, verificação de firmware RSA-2048. Justificativa: ROM de boot imutável; substituição pelo fornecedor em 2030. Controles compensatórios: VLAN isolada, lista de atualizações permitidas pelo portal do fornecedor com verificação do hash fora de banda, monitoramento. Expiração: 31 de dezembro de 2030 ou a substituição. Gatilho: progresso crível do CRQC, aviso do fornecedor ou incidente.

**EX019.** Os pacientes carregam o dano, mas não participam da decisão. A divulgação genômica é irreversível e afeta os parentes. O dano dura décadas além dos calendários de retenção e dos horizontes orçamentários da NRHT. O dever de cuidado exige proteger as pessoas pelo tempo em que podem ser prejudicadas. Portanto, *x* deve ser o horizonte do dano.

**EX020.** CBOM completa: os membros da Autoridade de Criptografia e os responsáveis pelas plataformas, no seu escopo, com acesso de menor privilégio e logs de auditoria; os executivos e os auditores recebem agregados; os fornecedores veem apenas os seus produtos; nunca publicada.

**EX021.** Híbrido: forte proteção contra o HNDL, complexidade moderada, escala, residual: autenticação. Pós-quântico puro: forte se o ML-KEM se mantiver, complexidade menor, escala, residual: sem proteção do híbrido. PSK: boa se as PSKs forem secretas, complexidade moderada, escala mal, residual: gestão de chaves. Minimização: reduz a exposição de qualquer forma, complexidade variável, escala por projeto, residual: os dados restantes.

**EX022.** 21.249 / 1.290 ≈ 16,5 vezes.

**EX023.** "Padrão: estabelecimento de chaves híbrido com ML-KEM-768 e assinaturas ML-DSA-65 (categoria 3), equilibrando margem e tamanho. Categoria 5 (ML-KEM-1024/ML-DSA-87) para os enlaces em que os parceiros ou a regulação a exijam."

**EX024.** O fornecedor B entrega o suporte ao IKEv2 híbrido; a NRHT verifica a negociação no laboratório e no canário; a migração é concluída e as PSKs são revogadas; data-limite rígida (por exemplo, 31 de dezembro de 2027), com escalonamento se for perdida.

**EX025.** Um sistema fechado cuja política exige o ML-KEM puro (por exemplo, um parceiro que exige o pós-quântico puro no estilo da CNSA) ou um enlace restrito em que os bytes e o código do componente tradicional importam, aceitando a perda da proteção do híbrido depois de uma revisão madura da implementação.

**EX026.** "Promover quando o limite superior de Wilson de 95 % da taxa de falhas de handshake ≤ referência + 0,04 ponto, medido por pelo menos 14 dias cobrindo dois ciclos semanais, sem nenhum local excedendo individualmente o limite."

**EX027.** Primeira retenção: incerteza — prorrogar o canário para reunir mais dados. Terceira retenção: evidência de dano num local — investigar a causa (o proxy), excluir o local, corrigir e depois testar de novo.

**EX028.** Navegadores modernos nas estações clínicas; navegadores legados em quiosques sem atualização; visualizadores embutidos nas modalidades; aplicativos móveis nos dispositivos da equipe; sistemas de parceiros (outros trusts, laboratórios); proxies de inspeção/firewalls no caminho.

**EX029.** Local A: 10/50.000 falhas; local B: 60/10.000. Agregado 70/60.000 = 0,117 %; se o limiar for de 0,15 %, o agregado passa, enquanto o local B, com 0,6 %, falha gravemente.

**EX030.** Interna: mudanças concorrentes (atualizações do sistema operacional) durante os canários poderiam confundir as falhas; os padrões semanais foram tratados com durações de duas semanas. Externa: os clientes do laboratório podem não representar todos os visualizadores embutidos; o proxy de um hospital mostra que as condições dos locais diferem; os resultados se aplicam às configurações testadas.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; a situação das normas muda, então verifique de novo.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Bernstein, D. J., et al. (2024). KyberSlash. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Chromium Blog (2023). Protecting Chrome Traffic with Hybrid Kyber KEM. <https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html>
- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- Gidney, C., and Ekerå, M. (2021). *Quantum* 5, 433. <https://doi.org/10.22331/q-2021-04-15-433>
- IETF RFCs: 8784 (IKEv2 PSK mixing), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NCCoE. Migration to Post-Quantum Cryptography project. <https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
