# Segurança Quântica e Pós-Quântica: Prática Especializada para Decisões em Escala Organizacional

- Idioma: português do Brasil (`pt`); curso de especialização de pós-graduação, dois anos em tempo parcial; aproximadamente 600 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–12 de 12 têm texto didático escrito; os exercícios EX001–EX060 (cinco por capítulo) têm as resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, com saídas verificadas. A revisão independente e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
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

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Segurança quântica e pós-quântica: integração organizacional

### Objetivos de aprendizagem

Você vai (1) integrar a migração para PQC aos processos de arquitetura, de mudança, de compras e de risco; (2) construir agilidade criptográfica nas plataformas por meio de políticas; (3) projetar os papéis de governança e os direitos de decisão; (4) alinhar a migração aos ciclos de renovação e aos orçamentos; e (5) medir o progresso do programa de forma significativa.

### 7.1 Não um projeto, uma capacidade

Uma migração conduzida como um projeto separado termina com um relatório e deixa a organização tão rígida quanto antes. Integrada aos processos normais, ela deixa uma capacidade: as revisões de arquitetura perguntam sobre algoritmos e agilidade; a gestão de mudanças registra as mudanças criptográficas; as compras exigem inventários e suporte a algoritmos; a gestão de riscos acompanha a exposição quântica. O [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) enquadra isso como agilidade criptográfica tanto no nível organizacional quanto no técnico.

Na NRHT, a Autoridade de Criptografia é o mecanismo para isso: ela é responsável pela norma criptográfica e revisa as decisões de arquitetura, enquanto as compras acrescentam cláusulas aos contratos. Meça a integração por se os processos normais agora fazem perguntas criptográficas sem que a equipe do programa os provoque.

### 7.2 Plataformas orientadas por política

As plataformas que leem as escolhas criptográficas de uma política permitem à organização mudar os algoritmos por configuração. O identificador do algoritmo precisa viajar com os dados e ser autenticado, para que um verificador possa recusar um algoritmo aposentado.

O Laboratório A mostra o padrão com códigos de autenticação de mensagens, mas o mesmo projeto se aplica aos KEMs e às assinaturas. Uma plataforma construída assim consegue passar do clássico ao híbrido, e depois a um novo algoritmo, com uma mudança de política e um período de transição. Os algoritmos fixos no código exigem novas versões de código a cada mudança.

### 7.3 Atividade prática — Laboratório A

```python
# Lab A (ch 7): crypto-agility through a policy-driven registry instead of hard-coded algorithms.
import hashlib, hmac
REGISTRY = {"hmac-sha256": lambda k, m: hmac.new(k, m, hashlib.sha256).digest(),
            "hmac-sha3-256": lambda k, m: hmac.new(k, m, hashlib.sha3_256).digest()}
POLICY = {"tag-algorithm": "hmac-sha256", "accept": ["hmac-sha256", "hmac-sha3-256"]}
def protect(key, msg):
    alg = POLICY["tag-algorithm"]; return alg, REGISTRY[alg](key, msg)
def check(key, msg, alg, tag):
    if alg not in POLICY["accept"]: return False            # algorithm identifier is authenticated by policy
    return hmac.compare_digest(REGISTRY[alg](key, msg), tag)
k, m = b"k" * 32, b"discharge summary 42"
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

O mesmo padrão — registro, política, lista de aceitos, aposentadoria — se aplica aos KEMs e às assinaturas nas plataformas reais.

O laboratório registra o identificador do algoritmo com cada tag e o confere com a lista de aceitos, para que um algoritmo aposentado possa ser recusado. Durante a transição, os dois algoritmos verificam; depois da aposentadoria, a tag antiga falha. Numa plataforma real, o identificador precisa ser protegido pela própria tag ou assinatura, para que um atacante não consiga mudá-lo. Tente aposentar o algoritmo antigo antes de trocar o padrão e anote o que quebra.

### 7.4 Governança e direitos de decisão

Defina quem decide a política criptográfica (uma autoridade ou um conselho de criptografia), quem é responsável pela implementação de cada plataforma, quem aprova as exceções e quem aceita o risco residual. Publique uma norma criptográfica que liste os algoritmos e parâmetros aprovados, as datas de transição e o processo de exceção.

Escreva os direitos de decisão na norma e publique-os, para que os responsáveis pelas plataformas saibam a quem perguntar. As exceções devem ser limitadas no tempo e registradas num registro que a Autoridade de Criptografia revisa. Na NRHT, o CISO preside a autoridade e o executivo responsável assina as aceitações de risco residual.

### 7.5 Ciclos de renovação e orçamento

A maior parte do hardware é substituída em ciclos de cinco a dez anos. Alinhar os requisitos de PQC a esses ciclos evita a substituição prematura; isso exige cláusulas de compras agora, para que o equipamento comprado em 2027 não precise ser substituído em 2031. As assinaturas de software são mais rápidas; exija roteiros com datas.

Associe cada plataforma do nível 1 à sua próxima data de renovação e à cláusula que vai se aplicar à sua substituição. Onde uma renovação cair depois da data em que a migração é necessária, planeje uma medida provisória, como um gateway ou uma PSK. Na NRHT, a substituição da frota de bombas de infusão em 2031 está planejada dessa forma.

### 7.6 Medindo o progresso

Conte resultados, e não atividades: a parcela dos fluxos do nível 1 com troca de chaves híbrida (evidência de grau A/B); a parcela dos novos contratos com cláusulas de PQC; o tempo mediano para mudar um algoritmo nas plataformas orientadas por política; a parcela de desconhecidos do nível 1. Evite métricas de vaidade, como "número de reuniões realizadas".

Relate cada métrica com a sua fonte e o seu grau de evidência, e mostre as tendências ao longo dos trimestres. Na revisão do segundo ano da NRHT, a cobertura híbrida do nível 1 era de 64 % com evidência de grau A ou B, e a parcela de desconhecidos era de 7 %. Métricas sem denominador ou sem fonte não devem aparecer nos relatórios ao conselho.

### 7.7 Caso resolvido

A NRHT cria uma Autoridade de Criptografia presidida pelo CISO, com membros de arquitetura, PKI, engenharia clínica e compras. A sua norma (sintética) define o híbrido com ML-KEM-768 como padrão para o novo estabelecimento de chaves, exige identificadores de algoritmo nos novos formatos de dados e acrescenta cláusulas de PQC a todos os contratos acima de um limiar. As métricas de progresso são revisadas trimestralmente pelo comitê de auditoria.

As primeiras decisões da autoridade são registradas com os seus motivos e datas de revisão, para que os membros posteriores vejam por que os padrões foram escolhidos. A sua norma é curta o bastante para que os responsáveis pelas plataformas a leiam e inclui o processo de exceção. A composição abrange as equipes cujos sistemas vão mudar.

### 7.8 Erros comuns e limites

- Tratar a migração como um projeto pontual.
- Nenhum processo de exceção, o que leva à não conformidade silenciosa.
- Métricas de atividade em vez de métricas de resultado.

Cada erro tem uma salvaguarda. Integre as perguntas criptográficas aos processos de arquitetura, de mudança e de compras. Publique um processo de exceção com expirações. Relate resultados como a cobertura com graus de evidência, e não contagens de reuniões ou de documentos produzidos. Na NRHT, a norma da Autoridade de Criptografia inclui um processo de exceção com datas de expiração, e as suas métricas de progresso são revisadas trimestralmente pelo comitê de auditoria. Confira se cada nova métrica tem denominador e fonte antes de acrescentá-la ao relatório ao conselho.

### Exercícios

- **EX031 — Pontos de integração.** Nomeie quatro processos existentes nos quais os requisitos de PQC devem ser integrados, com um requisito para cada. Rubrica: 3 = quatro processos, requisitos concretos.
- **EX032 — Direitos de decisão.** Esboce uma matriz RACI para "aprovar uma exceção à troca de chaves híbrida". Rubrica: 3 = responsável, aprovador, consultado e informado atribuídos com sensatez.
- **EX033 — Alinhamento com a renovação.** A substituição de um PACS está programada para 2029. O que a licitação de 2026 precisa incluir? Rubrica: 3 = suporte a algoritmos, agilidade, inventário, compromissos de atualização.
- **EX034 — Métrica de resultado.** Converta "sessões de conscientização sobre PQC realizadas" numa métrica de resultado. Rubrica: 3 = mudança mensurável de comportamento ou de estado.
- **EX035 — Teste de agilidade.** Projete um teste trimestral que mostre que uma plataforma consegue trocar de algoritmo por política. Rubrica: 3 = procedimento, evidência, critério de aprovação.

### Síntese

A integração transforma a migração numa capacidade organizacional: plataformas orientadas por política, direitos de decisão claros, compras alinhadas aos ciclos de renovação e métricas de resultado.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 12

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Segurança quântica e pós-quântica: casos difíceis

### Objetivos de aprendizagem

Você vai (1) analisar migrações que envolvem dispositivos médicos e embarcados, a PKI interna, arquivos de longo prazo e terceiros; (2) aplicar controles compensatórios onde a migração é impossível; (3) gerenciar as assinaturas baseadas em hash com estado; (4) planejar a validade das assinaturas de longo prazo; e (5) raciocinar sobre a resposta à quebra de um algoritmo.

### 8.1 Dispositivos médicos e embarcados

Os dispositivos têm aprovações regulatórias, vidas longas e firmware controlado pelo fornecedor. Mudar a criptografia pode exigir uma nova certificação. Opções: firmware do fornecedor com troca de chaves híbrida, onde oferecido; segmentação da rede e gateways que terminam os protocolos pós-quânticos na frente dos dispositivos; fluxos de dados minimizados; e requisitos de compras para as substituições. A segurança dos pacientes governa as janelas de mudança.

Na NRHT, a frota de bombas de infusão ilustra as escolhas: a troca de chaves híbrida chega com uma versão de firmware do fornecedor depois de testes clínicos, enquanto a verificação de boot não pode mudar e é tratada com controles compensatórios até a substituição. Acorde as janelas de mudança com a engenharia clínica e registre os testes de segurança feitos antes de cada atualização.

### 8.2 PKI interna

A PKI interna ancora as VPNs, as identidades dos dispositivos e o TLS entre serviços. Um plano de PKI pós-quântica: montar uma raiz e intermediárias ML-DSA em HSMs que suportem a FIPS 204; distribuir a nova raiz às partes confiantes; emitir certificados pós-quânticos primeiro nos ecossistemas fechados; manter a hierarquia clássica em paralelo; e definir datas de término para a emissão clássica alinhadas à norma interna.

Planeje a distribuição da nova raiz a todas as partes confiantes antes de emitir a partir dela; uma raiz em que os clientes não confiam quebra os serviços. Teste primeiro a emissão e a validação num laboratório com clientes representativos. Registre no plano quais ecossistemas mudam primeiro e a data em que a emissão clássica termina para cada um.

### 8.3 Assinaturas baseadas em hash com estado

A [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) aprova o LMS e o XMSS com o requisito de que as chaves e o estado sejam gerenciados em módulos de hardware e não sejam exportados. Elas servem para a assinatura de firmware. Planeje a capacidade de assinaturas, proteja o estado contra o retrocesso durante o failover dos HSMs e teste a recuperação de desastres para que a recuperação nunca reutilize um índice.

Registre o número de assinaturas que cada chave consegue produzir e acompanhe o uso em relação a ele. Teste o failover dos HSMs de um modo que prove que o estado não pode retroceder, porque reutilizar um índice quebra a segurança. Mantenha o plano junto com o procedimento de assinatura de firmware e revise-o depois de cada mudança nos HSMs.

### 8.4 Assinaturas e arquivos de longo prazo

Os documentos clínicos assinados e os formulários de consentimento precisam continuar verificáveis por décadas. Os carimbos de tempo de arquivo e a renovação dos registros de evidência podem preservar a validade ao longo das transições de algoritmo, desde que a renovação aconteça enquanto o algoritmo mais antigo ainda for confiável. Os arquivos cifrados já expostos em trânsito não podem ser reparados pela recifração.

Agende a renovação bem antes que o algoritmo mais antigo deixe de ser confiável, e registre cada renovação. Nos arquivos cifrados, distinga os dados em repouso, que podem ser recifrados, das cópias que atravessaram redes sob troca de chaves clássica, que não podem ser reparadas. Relate as duas no registro de riscos.

### 8.5 Resposta à quebra de um algoritmo

O Rainbow (Beullens, 2022) e o SIKE (Castryck e Decru, 2022) mostram que esquemas candidatos podem cair rapidamente; o KyberSlash (Bernstein et al., 2024) mostra que as implementações podem vazar. Um plano de resposta nomeia o fórum de decisão, os caminhos de configuração para desativar um algoritmo, os sistemas que precisam de novas versões ou de hardware, o fallback (os híbridos ajudam) e as comunicações aos fornecedores e aos reguladores. A seleção do HQC como KEM de reserva oferece uma alternativa futura com uma base matemática diferente.

Ensaie o plano uma vez por ano com um exercício de mesa, usando um caso realista, como uma fraqueza encontrada numa implementação do ML-KEM. Registre quanto tempo leva para desativar o algoritmo em cada plataforma; as plataformas que levam mais tempo são as primeiras candidatas à agilidade orientada por política.

### 8.6 Caso resolvido

A frota de bombas de infusão da NRHT (sintética, 4.000 unidades) usa firmware assinado com RSA, verificado por uma ROM de boot, e ECDH com um hub de gestão. O fornecedor oferece a troca de chaves híbrida numa versão de firmware de 2027; a verificação de boot não pode mudar. Plano: segmentar as bombas numa VLAN dedicada; adotar o firmware de 2027 depois dos testes de segurança clínica; aceitar o risco residual de falsificação posterior no firmware até a substituição da frota em 2031, com controles compensatórios (lista de atualizações assinadas permitidas no hub, monitoramento de anomalias); exigir a verificação de boot com ML-DSA ou LMS na licitação da substituição.

Registre o risco residual no registro com a sua expiração vinculada à substituição de 2031, e revise-o se a data da substituição atrasar. Garanta que o requisito de verificação de boot pós-quântica da licitação da substituição seja escrito nas compras agora.

### 8.7 Erros comuns e limites

- Aplicar as janelas de mudança de TI aos dispositivos clínicos.
- Construir uma raiz pós-quântica sem um plano de distribuição às partes confiantes.
- Assinatura LMS apenas em software.

Cada erro tem uma salvaguarda neste capítulo. Acorde as janelas de mudança clínicas com a engenharia clínica. Escreva o plano de distribuição às partes confiantes antes de montar uma raiz pós-quântica. Mantenha as chaves e o estado do LMS e do XMSS em módulos de hardware, como a SP 800-208 exige, e teste o failover. Na NRHT, o plano de firmware das bombas foi acordado com a engenharia clínica, a raiz ML-DSA interna tem um plano de distribuição às partes confiantes, e as chaves de assinatura de firmware ficam em módulos de hardware, com o failover testado para que nenhum índice seja reutilizado.

### Exercícios

- **EX036 — Controles compensatórios.** Liste quatro controles compensatórios para os dispositivos que não podem migrar. Rubrica: 3 = quatro controles distintos e eficazes.
- **EX037 — Sequência da PKI.** Ordene os passos do plano da PKI e justifique a ordem. Rubrica: 3 = raiz, distribuição, ecossistemas fechados, emissão ampla, encerramento do clássico.
- **EX038 — Capacidade do LMS.** Uma árvore LMS com 2^15 assinaturas assina 40 imagens de firmware por ano. Quantos anos de capacidade? Rubrica: 3 = 819 anos, com comentário sobre várias árvores/failover dos HSMs.
- **EX039 — Momento da renovação do arquivo.** Quando a NRHT deve renovar os registros de evidência do arquivo baseados em carimbos de tempo assinados com RSA? Rubrica: 3 = bem antes de uma fraqueza crível do RSA, calendário definido por política.
- **EX040 — Simulação de quebra.** Projete um exercício de mesa para "fraqueza anunciada no ML-KEM-768". Rubrica: 3 = cenário, participantes, decisões, critérios de sucesso.

### Síntese

Os casos difíceis — dispositivos, PKI, assinaturas com estado, arquivos e quebras de algoritmos — precisam de controles compensatórios, sequenciamento cuidadoso, estado guardado em hardware, renovação no tempo certo e resposta ensaiada.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 12

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Segurança quântica e pós-quântica: liderança e garantia

### Objetivos de aprendizagem

Você vai (1) liderar um programa de migração plurianual com objetivos claros; (2) projetar um modelo de garantia com verificação independente; (3) preparar evidências para auditores e reguladores; (4) comunicar-se com conselhos, clínicos e fornecedores; e (5) sustentar o programa diante da rotatividade da equipe e das mudanças nas orientações.

### 9.1 Liderança do programa

Um programa plurianual precisa de uma missão ("proteger a confidencialidade e a confiança de longo prazo contra ataques quânticos sem prejudicar os serviços clínicos"), objetivos com datas, um roteiro por nível, um envelope orçamentário com faixas e governança. O trabalho do líder é manter as prioridades alinhadas às evidências à medida que as orientações e a tecnologia mudam, e proteger o programa de ser reduzido a um checklist de conformidade.

Escreva a missão e os objetivos num documento curto que o conselho aprova, e revisite-os em cada revisão anual. Mantenha o roteiro por nível, para que ele mostre o que é protegido primeiro e por quê. Quando as orientações ou a tecnologia mudarem, registre a mudança e o seu efeito sobre as prioridades.

### 9.2 Três linhas de garantia

A primeira linha (os responsáveis pelas plataformas) implementa e faz autotestes; a segunda linha (segurança e risco) define as normas e monitora; a terceira linha (auditoria interna) testa de forma independente. Na PQC, a verificação independente significa observar de novo os algoritmos negociados, amostrar certificados, revisar os registros de exceções e testar as alegações de agilidade, e não ler relatórios de status.

Na NRHT, a auditoria interna observou de novo os fluxos do nível 1 e encontrou três com fallback clássico, que os relatórios de status não haviam mostrado. A primeira e a segunda linhas devem esperar esses achados e tratá-los como informação. Acorde com antecedência como os achados são relatados e quem age sobre eles.

### 9.3 Evidências para auditores e reguladores

Prepare um pacote de evidências: a norma criptográfica e a sua aprovação; o inventário com a cobertura e os graus; o método de priorização e as decisões; as métricas de progresso com as fontes; o registro de exceções e de riscos residuais com as expirações; os relatórios de testes; a garantia dos fornecedores. Cada item deve ser gerado pela operação normal, para que o pacote seja barato de atualizar.

Mantenha o pacote num único local, com um índice curto e a data em que cada item foi gerado. Quando um auditor pedir algo que não está no pacote, acrescente-o ao processo normal, para que esteja lá na próxima vez. Evite criar documentos apenas para as auditorias; eles envelhecem imediatamente e não são confiáveis.

### 9.4 Comunicação

Os conselhos precisam de decisões e da postura de risco; os clínicos precisam da garantia de que as mudanças não vão interromper o atendimento e de janelas de mudança claras; os fornecedores precisam de requisitos e prazos claros; a equipe precisa saber o que muda para ela. As mensagens devem ser calmas e específicas; evite tanto o alarme quanto a complacência.

Use os mesmos fatos para todos os públicos, mas mude a ênfase. Um documento para o conselho começa pela postura e pelas decisões necessárias; um informe clínico começa pelas janelas de mudança e pelos fallbacks; uma carta aos fornecedores começa pelos requisitos e pelas datas. Guarde cópias datadas, para que as mensagens possam ser conferidas com o que aconteceu depois.

### 9.5 Sustentação

As orientações vão mudar: o IR 8547 pode ser finalizado com datas diferentes; as normas do FN-DSA e do HQC vão aparecer. Incorpore ciclos de revisão à governança, mantenha registros de decisão, treine sucessores e mantenha o inventário vivo. Um programa que depende de um único especialista é frágil.

Nomeie um substituto para cada papel-chave e mantenha os registros de decisão atualizados, para que uma saída não interrompa o programa. Rode o ciclo de revisão num calendário, em vez de esperar pelas notícias. Quando uma norma mudar, atualize o resumo, a norma interna e quaisquer decisões afetadas na mesma revisão.

### 9.6 Caso resolvido

A revisão de garantia do segundo ano da NRHT (sintética): a auditoria interna amostra 60 fluxos do nível 1 e observa de novo 57 (95 %) com o algoritmo relatado; três mostram fallback clássico por causa de uma configuração revertida — um achado que leva ao monitoramento da deriva de configuração. O registro de exceções tem 41 entradas; seis passaram da expiração sem revisão — um achado que leva ao escalonamento automático. O conselho recebe uma postura de uma página: cobertura híbrida do nível 1 de 64 % (evidência A/B), 7 % de desconhecidos, plano da PKI no prazo, dois riscos residuais altos aceitos com expiração.

Cada achado leva a uma mudança de processo, e não a uma correção pontual, e a postura apresentada ao conselho mostra tanto o progresso quanto o risco residual. Registre o tamanho da amostra e o método da auditoria, para que a próxima revisão possa comparar os resultados.

### 9.7 Erros comuns e limites

- Garantia por relatório de status.
- Pacotes de evidências montados especialmente antes das auditorias.
- Programas dependentes de um único especialista.

Cada erro tem uma salvaguarda. Observe de novo os algoritmos negociados em vez de ler relatórios. Gere as evidências a partir das operações normais. Treine sucessores e mantenha os registros de decisão, para que o programa continue se o seu líder sair. Na NRHT, a amostra de 60 fluxos do nível 1 da auditoria do segundo ano (9.6) é o modelo: a nova observação encontrou o que os relatórios de status não haviam mostrado. O pacote de evidências é gerado pela operação normal e atualizado a cada trimestre. Um substituto nomeado consegue conduzir cada revisão se o líder estiver ausente, e os registros de decisão explicam por que cada escolha foi feita, para que um recém-chegado consiga continuar o trabalho.

### Exercícios

- **EX041 — Objetivos.** Escreva três objetivos de programa datados e mensuráveis para a NRHT. Rubrica: 3 = específicos, mensuráveis, com prazo, ligados aos níveis.
- **EX042 — Teste de auditoria.** Projete um teste independente da alegação "todos os enlaces entre locais do nível 1 usam troca de chaves híbrida". Rubrica: 3 = amostragem, método de nova observação, critério de aprovação.
- **EX043 — Pacote de evidências.** Liste sete itens do pacote de evidências e as suas fontes. Rubrica: 3 = sete itens com fontes operacionais.
- **EX044 — Mensagem aos clínicos.** Escreva uma mensagem de 100 palavras às lideranças clínicas sobre uma janela de mudança do PACS. Rubrica: 3 = o quê, quando, impacto, contato, tranquilização.
- **EX045 — Continuidade.** Proponha três medidas que mantenham o programa vivo diante de uma troca de liderança. Rubrica: 3 = documentação, ciclos de governança, conhecimento distribuído.

### Síntese

A liderança mantém um programa plurianual alinhado às evidências; a garantia observa de novo, em vez de ler; os pacotes de evidências surgem das operações normais; e a continuidade é projetada desde o início.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 12

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Leitura e crítica de pesquisas

### Objetivos de aprendizagem

Você vai (1) ler criticamente artigos de criptoanálise, de estimativa de recursos e de implantação; (2) extrair as hipóteses e avaliar o seu realismo; (3) julgar adequadamente os preprints e as pesquisas de fornecedores; (4) traduzir a pesquisa em implicações para a prática; e (5) escrever uma crítica estruturada.

### 10.1 Lendo criptoanálise

Os artigos de criptoanálise declaram os modelos de ataque, a complexidade e os experimentos. Pergunte: o ataque se aplica ao conjunto de parâmetros padronizado ou a uma variante? É clássico ou quântico? A complexidade é assintótica ou concreta? Foi reproduzido? A quebra do Rainbow por Beullens (2022) se aplicava aos parâmetros submetidos, com experimentos concretos na escala de um laptop — decisiva. Muitos ataques a reticulados anunciados melhoram ligeiramente as constantes sem mudar as categorias de segurança — importantes, mas não urgentes.

Registre a sua leitura numa tabela curta: esquema e conjunto de parâmetros, clássico ou quântico, concreto ou assintótico, reproduzido ou não, e a implicação prática. Compartilhe-a com a Autoridade de Criptografia quando um artigo afetar um algoritmo em uso. A maioria dos artigos não vai exigir ação; alguns vão, e a tabela mostra quais.

### 10.2 Lendo estimativas de recursos

Os artigos de estimativa de recursos, como Gidney e Ekerå (2021) e Gidney (2025), supõem taxas de erro físico, conectividade, distância do código, tempo de ciclo e escolhas algorítmicas. Extraia-as numa tabela. Pergunte quais hipóteses o hardware atual atende e quais não atende. Uma estimativa em queda sob hipóteses otimistas é um sinal sobre a direção do movimento, e não uma data.

Mantenha a tabela de hipóteses de cada artigo e acrescente uma coluna indicando se o hardware atual atende cada uma. Compare as tabelas entre os artigos para ver quais hipóteses mudaram. Apresente o resultado ao conselho como direção do movimento, como faz a crítica da NRHT a Gidney (2025).

### 10.3 Lendo estudos de implantação

Os artigos de implantação relatam grupos negociados, taxas de falha e desempenho a partir de medições. Pergunte: que população, qual ponto de observação, qual período, que vieses (por exemplo, varrer apenas sites populares)? Os resultados se transferem para ambientes corporativos ou clínicos?

Escreva as respostas a essas perguntas na sua crítica, e diga explicitamente se os resultados se aplicam às redes clínicas da NRHT. As medições em toda a internet podem deixar escapar os proxies de inspeção legados e os clientes embutidos, que a própria avaliação da NRHT mostrou serem importantes. Trate um artigo de implantação como uma hipótese prévia a testar localmente.

### 10.4 Preprints e pesquisas de fornecedores

Os preprints (arXiv, IACR ePrint) costumam ser a primeira fonte crível e são citados rotineiramente nesta área; pondere-os pelo histórico dos autores, pela reprodutibilidade e pela revisão subsequente. As pesquisas de fornecedores podem ser cuidadosas, mas têm interesses; verifique se os dados e os métodos são publicados.

Anote a situação de cada fonte na sua crítica, e verifique depois se um preprint foi revisado ou publicado. Nas pesquisas de fornecedores, pergunte se os resultados podem ser reproduzidos sem o produto do fornecedor. Pondere as fontes de forma consistente, para que um resultado conveniente não receba mais crédito que um inconveniente.

### 10.5 Crítica estruturada

Uma crítica resume a alegação, avalia as evidências e as hipóteses, identifica o que mudaria a conclusão e declara as implicações para a prática. Mantenha-a em uma página para os profissionais.

Use os mesmos títulos em todas as críticas, para que os leitores possam compará-las. Termine com uma frase sobre o que a NRHT deveria fazer de diferente, se houver algo. Guarde a crítica, datada, junto com os registros de decisão que ela informa, para que possa ser revista quando surgir um trabalho novo. Peça a um colega que verifique se o resumo da alegação é justo.

### 10.6 Caso resolvido

Crítica de Gidney (2025) para o conselho da NRHT, uma página: alegação — o RSA-2048 poderia ser fatorado com menos de um milhão de qubits ruidosos em menos de uma semana; hipóteses principais — taxa de erro físico em torno de 10^−3, correção de erros no estilo do código de superfície, conectividade e tempos de ciclo específicos; situação — preprint de um autor estabelecido, que se apoia em predecessores revisados por pares; implicação — a distância de recursos está diminuindo, o que apoia a decisão robusta do conselho de "agir agora nos fluxos de vida longa"; ele não dá uma data e não deve ser citado como tal.

A crítica é curta, cita as hipóteses do artigo e evita convertê-las numa data. Ela também liga o artigo a uma decisão existente, em vez de propor uma nova. Arquive-a com o registro de decisão e revisite-a quando surgir uma estimativa revisada.

### 10.7 Erros comuns e limites

- Tratar todo novo artigo de ataque como urgente.
- Citar estimativas de recursos como previsões.
- Descartar os preprints em bloco.

Cada erro tem uma salvaguarda. Pergunte se um novo ataque se aplica aos parâmetros padronizados antes de chamá-lo de urgente. Apresente as estimativas de recursos com as suas hipóteses e nunca como datas. Pondere os preprints pelo autor, pelo método e pela reprodução, em vez de descartá-los. Na NRHT, a crítica de Gidney (2025) foi apresentada como direção do movimento e ligada a uma decisão existente, e não como uma data. Aplique a mesma disciplina à criptoanálise: confira primeiro o conjunto de parâmetros e depois pergunte se o ataque foi reproduzido antes de elevar a urgência.

### Exercícios

- **EX046 — Tabela de hipóteses.** Construa uma tabela de hipóteses de cinco linhas para um artigo de estimativa de recursos. Rubrica: 3 = taxa de erro, número de qubits, tempo de execução, código, conectividade, com as fontes.
- **EX047 — Teste de urgência.** Dê três perguntas que decidam se um novo artigo de ataque a reticulados muda os planos da NRHT. Rubrica: 3 = aplicabilidade aos parâmetros, impacto na categoria, reprodução.
- **EX048 — Viés de implantação.** Nomeie dois vieses dos estudos de varredura de toda a internet quando aplicados a hospitais. Rubrica: 3 = vieses de população e de ponto de observação explicados.
- **EX049 — Whitepaper de fornecedor.** Liste o que você precisaria para confiar no benchmark de um fornecedor sobre a vazão de uma VPN híbrida. Rubrica: 3 = método, configuração, disponibilidade dos dados, independência.
- **EX050 — Crítica de uma página.** Esboce os cinco títulos do seu modelo de crítica. Rubrica: 3 = alegação, evidências, hipóteses, sensibilidades, implicações.

### Síntese

Os especialistas leem as pesquisas pelas suas hipóteses e pela sua aplicabilidade, ponderam as fontes por tipo e reprodutibilidade, e traduzem os achados em implicações calmas e específicas para a prática.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 12

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Projeto aplicado

### Objetivos de aprendizagem

Você vai (1) delimitar um projeto especializado aplicado com um patrocinador organizacional; (2) produzir entregas prontas para a decisão; (3) aplicar os métodos de evidência, avaliação e governança deste livro; (4) gerenciar a autorização e a proteção dos dados; e (5) avaliar o impacto.

### 11.1 Tipos de projeto

Projetos adequados: projetar e pilotar um programa de inventário para uma divisão; produzir uma norma criptográfica interna com um plano de transição; liderar um piloto avaliado de troca de chaves híbrida numa plataforma; projetar um roteiro de PKI pós-quântica; ou construir um processo de garantia dos fornecedores. Cada um produz artefatos que a organização vai usar.

Escolha um projeto que o patrocinador vá usar qualquer que seja o resultado. Um piloto que descobre que a troca de chaves híbrida não pode ser ativada numa plataforma ainda é útil, se for avaliado segundo critérios definidos com antecedência. Evite projetos que apenas descrevem o problema.

### 11.2 Delimitando com um patrocinador

Acorde com um patrocinador: a decisão que o projeto apoia, o escopo, as entregas, o acesso, a autorização, os critérios de sucesso e como os resultados serão usados. A autorização escrita precisa cobrir qualquer observação ou teste; prefira laboratórios isolados para os testes ativos.

Escreva o acordo e peça ao patrocinador que o assine antes de qualquer coleta de dados. Inclua o que acontece com os dados do projeto no fim e quem pode ver os resultados. Revise o escopo com o patrocinador no meio do caminho, e registre quaisquer mudanças. Guarde uma cópia com os registros do projeto.

### 11.3 Entregas

As entregas prontas para a decisão incluem um documento de decisão curto, as evidências por trás dele (extratos do inventário, resultados de avaliação, tabelas de hipóteses), artefatos de implementação (texto de política, linhas de base de configuração, cláusulas de compras) e um plano de transição para a operação.

Cada entrega deve ter um responsável que vai usá-la depois do projeto. Na NRHT, o projeto da radiologia produziu um questionário, uma rubrica de pontuação e cláusulas contratuais, além de um documento de decisão. Teste os artefatos utilizáveis com as pessoas que vão aplicá-los antes da transição. Acorde a data da transição com cada responsável.

### 11.4 Proteção dos dados

Os projetos na saúde tocam sistemas sensíveis. Colete metadados, e não conteúdo; minimize os identificadores; guarde os dados do projeto com segurança; e apague-os conforme o acordo.

Registre no plano do projeto quais dados serão coletados, quem pode acessá-los, onde serão guardados e quando serão apagados. Verifique se o encarregado de proteção de dados concorda antes do início da coleta. No fim, confirme a exclusão por escrito. Pseudonimize os nomes dos ativos em qualquer extrato do projeto que saia dos sistemas da NRHT, e mantenha o mapeamento apenas nos sistemas da NRHT. Relate imediatamente ao patrocinador qualquer coleta acidental de conteúdo.

### 11.5 Avaliação do impacto

Defina o impacto antes de começar: por exemplo, "parcela de desconhecidos do nível 1 na divisão de radiologia reduzida de 31 % para menos de 10 %" ou "questionário aos fornecedores adotado para todos os novos contratos da radiologia". Meça depois de um período definido.

Defina uma medida de referência antes de começar e acorde a meta e a data para medi-la. No projeto da radiologia da NRHT, a parcela de desconhecidos começou em 31 % e foi medida de novo depois de seis meses. Relate o resultado, quer ele atinja a meta, quer não. Escolha, sempre que possível, medidas que a organização já coleta.

### 11.6 Caso resolvido

Projeto (sintético): "Garantia dos fornecedores quanto à prontidão pós-quântica na radiologia da NRHT." Patrocinador: diretor de TI da radiologia. Entregas: questionário, rubrica de pontuação, cláusulas contratuais, resultados para 18 fornecedores, documento de decisão. Resultados: 5 fornecedores com roteiros datados e acesso para testes; 7 com alegações sem data; 6 calados. Decisão: cláusulas de PQC obrigatórias em todas as renovações; fornecedores calados escalonados às compras; dois fornecedores convidados para pilotos conjuntos no laboratório. Impacto depois de seis meses: a parcela de desconhecidos na radiologia caiu de 31 % para 12 %.

O resultado é relatado com a sua referência e a data da medição, e o documento de decisão transformou os achados em ações de compras. Guarde o questionário e a rubrica para que outras divisões possam reutilizá-los.

### 11.7 Erros comuns e limites

- Projetos sem uma decisão a apoiar.
- Entregas que são apenas relatórios, sem artefatos utilizáveis.
- Medidas de impacto definidas depois do fato.

Cada erro tem uma salvaguarda. Acorde a decisão que o projeto apoia antes de começar. Entregue artefatos como texto de política, cláusulas e linhas de base de configuração junto com o relatório. Defina as medidas de impacto e as referências antes de o trabalho começar, e relate o resultado mesmo quando ficar aquém. Na NRHT, o projeto da radiologia foi ligado a uma decisão de compras, entregou um questionário, uma rubrica e cláusulas, e mediu a parcela de desconhecidos em relação a uma referência de 31 % depois de seis meses. Use essa estrutura como modelo para outras divisões.

### 11.8 Lidando com a resistência

Os projetos aplicados encontram resistência: responsáveis por serviços preocupados com interrupções, fornecedores relutantes em divulgar, detentores de orçamento céticos quanto a um risco que ainda não se materializou. Trate a resistência como informação. O medo de interrupção de um responsável é um requisito de implantação em estágios e de rollback; a relutância de um fornecedor é uma alavanca de compras; o ceticismo é um pedido pelo argumento da decisão robusta do Capítulo 1. Registre as objeções e como o projeto as tratou no documento de decisão, porque as mesmas objeções vão voltar quando o trabalho for ampliado para além do piloto.

### Exercícios

- **EX051 — Acordo com o patrocinador.** Liste oito itens do acordo com o patrocinador. Rubrica: 3 = decisão, escopo, entregas, acesso, autorização, sucesso, uso, tratamento dos dados.
- **EX052 — Rubrica de pontuação.** Projete uma rubrica de 0 a 3 para a prontidão dos fornecedores em PQC. Rubrica: 3 = níveis claramente distinguidos pelas evidências.
- **EX053 — Impacto.** Calcule a redução da parcela de desconhecidos de 11.6 em pontos percentuais e em termos relativos. Rubrica: 3 = 19 pontos, ≈ 61 % relativos.
- **EX054 — Proteção dos dados.** Especifique a retenção e a exclusão dos dados do projeto. Rubrica: 3 = escopo, período, método, verificação.
- **EX055 — Transição.** Liste o que o responsável operacional precisa na transição. Rubrica: 3 = artefatos, procedimentos, contatos, questões em aberto.

### Síntese

Os projetos aplicados apoiam decisões reais, entregam artefatos utilizáveis sob a autorização e a proteção de dados adequadas e medem o impacto segundo critérios definidos com antecedência.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 12

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Revisão final e transferência

### Objetivos de aprendizagem

Você vai (1) revisar o seu portfólio em relação aos objetivos do curso; (2) apresentar e defender escolhas em escala organizacional; (3) transferir os métodos para outros domínios e para futuras mudanças de algoritmo; (4) planejar o desenvolvimento profissional contínuo; e (5) deixar um legado sustentável.

### 12.1 Revisão do portfólio

Reúna: os registros de decisão do Capítulo 1; o resumo do estado da prática (2); o projeto e as métricas do inventário (3); a análise de risco e de ética (4); as alternativas de projeto (5); a avaliação (6); o modelo de governança (7); os planos para os casos difíceis (8); o projeto da garantia (9); as críticas de pesquisas (10); as entregas do projeto (11). Para cada um, anote que evidência mostra que o objetivo foi atingido.

Apresente o portfólio na mesma ordem do curso, para que os examinadores consigam acompanhá-lo. Para cada item, inclua uma nota curta sobre o que você mudaria agora. As evidências ausentes devem ser nomeadas, e não escondidas. Peça a um colega que o leia antes da entrega.

### 12.2 Defesa

Espere questionamentos sobre as hipóteses (cronogramas, horizontes do dano), os valores (pesos da pontuação), os graus de evidência, a aceitação do risco residual e a situação das orientações. Defenda-se com evidências e reconheça a incerteza.

Prepare uma resposta curta para cada questionamento, com uma indicação da evidência no portfólio, como o registro de decisão das datas internas ou os pesos da pontuação aprovados pelo conselho. Onde você estiver incerto, diga que evidência resolveria a questão. Ensaie com alguém que discorde das suas escolhas. Mantenha as respostas curtas e específicas. Anote qualquer pergunta que você não conseguiu responder.

### 12.3 Transferência

Os métodos se transferem: as decisões robustas sob incerteza, a graduação das evidências, a avaliação controlada, a agilidade orientada por política e a garantia por nova observação se aplicam a qualquer transição criptográfica futura — a quebra de um algoritmo implantado, uma nova norma como o FN-DSA ou a eventual aposentadoria dos híbridos atuais. Eles também se transferem para outros riscos de longa latência.

Para mostrar a transferência, aplique um método a um caso novo no portfólio, como usar o portão de canário numa mudança planejada de algoritmo de assinatura. Anote quais partes do método precisaram de adaptação e quais não.

### 12.4 Desenvolvimento contínuo

Acompanhe as normas (NIST, IETF), as orientações setoriais, a criptoanálise e as pesquisas de implantação. Mantenha o seu resumo do estado da prática trimestralmente. Participe de comunidades profissionais e compartilhe lições anonimizadas.

Escreva um plano com fontes específicas e um calendário, e revise-o todo ano. Mantenha um registro curto do que você leu e do que mudou na sua prática por causa disso. Compartilhe uma lição anonimizada por ano com uma comunidade profissional, e peça comentários de colegas que trabalham em outros setores, já que as transições deles podem enfrentar problemas semelhantes e oferecer comparações úteis.

### 12.5 Legado

Deixe a organização com um inventário vivo, uma norma criptográfica com ciclo de revisão, registros de decisão, um registro de exceções com expirações e sucessores treinados. O sucesso é um programa que continua sem você.

Confira o legado pedindo a um sucessor que conduza a revisão trimestral sem você, e corrija qualquer passo que ele não tenha conseguido concluir. Registre onde cada documento-chave fica e quem é o seu responsável. Um teste conduzido pelo sucessor antes da sua saída é a melhor evidência de que o legado funciona, então agende um e registre o que precisou ser corrigido.

### 12.6 Caso resolvido

Na revisão final da NRHT, o líder do programa apresenta: cobertura híbrida do nível 1 de 78 % com evidência A/B; 5 % de desconhecidos; raiz interna ML-DSA em operação, com 40 % dos certificados dos serviços internos migrados; 12 riscos residuais aceitos, todos com expiração; teste de agilidade aprovado em quatro plataformas. Um examinador pergunta o que acontece se o IR 8547 for finalizado com datas mais cedo; o líder mostra o registro de decisão da definição das datas internas e o gatilho de governança para a revisão.

A revisão final mostra o progresso com graus de evidência e nomeia os riscos residuais, cada um com uma expiração. A pergunta do examinador é respondida com um mecanismo de governança, e não com uma previsão, que é o tipo de resposta que um programa robusto deve ser capaz de dar.

### 12.7 Erros comuns e limites

- Portfólios sem evidências dos resultados.
- Defesas que alegam certeza demais.
- Um legado que depende do líder que está saindo.

Cada erro tem uma salvaguarda. Anexe as evidências dos resultados a cada item do portfólio. Na defesa, declare as hipóteses e as incertezas com clareza. Treine sucessores e documente os processos, para que o programa continue depois da sua saída. Na NRHT, a revisão final apresentou a cobertura com graus de evidência, os riscos residuais com expirações e um teste de agilidade em quatro plataformas. A pergunta do examinador sobre o IR 8547 foi respondida com um gatilho de governança. Use essa estrutura: resultado, evidência, risco residual e o mecanismo que vai responder às mudanças depois da sua saída.

### 12.8 Refletindo sobre o julgamento

Encerre o portfólio com uma nota reflexiva sobre o seu próprio julgamento: uma decisão que você tomaria de novo, uma que mudaria com o que sabe agora e uma hipótese da qual tem menos certeza. Os especialistas merecem confiança não porque sempre acertam, mas porque mostram como raciocinam e se atualizam. A nota também ajuda os sucessores a entender quais partes do programa se apoiam em evidências firmes e quais em apostas ponderadas. Na NRHT, por exemplo, o plano das bombas de infusão supõe que a versão de firmware híbrido de 2027 do fornecedor chegue no prazo e passe nos testes clínicos, e dizer isso claramente mostra ao próximo líder onde olhar primeiro.

### Exercícios

- **EX056 — Evidência dos resultados.** Para três objetivos do curso, nomeie a evidência do portfólio que demonstra cada um. Rubrica: 3 = artefatos específicos.
- **EX057 — Transferência.** Explique como o programa trataria um novo requisito de adotar o FN-DSA. Rubrica: 3 = política, inventário, avaliação, implantação pela agilidade.
- **EX058 — Resposta na defesa.** Responda: "Por que você aceitou o risco residual das bombas de infusão?" Rubrica: 3 = restrições, controles compensatórios, expiração, justificativa de segurança.
- **EX059 — Plano de desenvolvimento.** Esboce um plano de desenvolvimento contínuo de um ano. Rubrica: 3 = fontes, cadência, produtos.
- **EX060 — Checklist do legado.** Liste seis itens que precisam existir para que o programa continue sem você. Rubrica: 3 = seis itens concretos.

### Síntese

A revisão final demonstra os resultados com evidências, defende as escolhas com honestidade e transfere os métodos e a capacidade, para que as futuras mudanças criptográficas encontrem uma organização preparada.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 12

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre a NRHT são sintéticos.

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

**EX031.** Revisão de arquitetura: os novos projetos precisam declarar os algoritmos e a agilidade. Gestão de mudanças: registrar as mudanças criptográficas e o rollback. Compras: cláusulas de PQC e divulgação do inventário. Gestão de riscos: exposição quântica acompanhada por nível.

**EX032.** Responsável pela execução: o responsável pela plataforma prepara o pedido. Aprovador: o presidente da Autoridade de Criptografia. Consultados: arquitetura de segurança, segurança clínica (se clínico), risco. Informados: auditoria interna, central de serviços.

**EX033.** Suporte aos algoritmos das FIPS 203/204 em protocolos nomeados na entrega ou com roteiro datado; configuração de algoritmos orientada por política; divulgação do inventário criptográfico; compromissos de atualização e de suporte ao longo da vida do produto; acesso para testes.

**EX034.** "Parcela das equipes de plataforma cujos serviços passam no teste trimestral de agilidade" ou "parcela das solicitações de mudança do nível 1 que registram os detalhes dos algoritmos".

**EX035.** Trimestralmente, trocar o algoritmo configurado de um serviço de teste (por exemplo, a ordem dos grupos preferidos ou o algoritmo de assinatura) apenas por política; verificar a negociação com clientes de teste; restaurar. Evidência: chamado de mudança, logs de negociação antes/depois. Aprovação: mudança e rollback em até um dia, sem nova versão de código.

**EX036.** Segmentação em VLANs dedicadas; gateways que terminam os protocolos pós-quânticos; minimização dos dados enviados pelos dispositivos; lista de permissões e verificação fora de banda das atualizações; monitoramento reforçado.

**EX037.** 1) Criar a raiz e as intermediárias ML-DSA em HSMs; 2) distribuir a raiz às partes confiantes; 3) emitir certificados pós-quânticos nos ecossistemas fechados; 4) ampliar a emissão; 5) encerrar a emissão clássica. A ordem segue as dependências da validação da cadeia.

**EX038.** 2^15 = 32.768 / 40 ≈ 819 anos; a capacidade é ampla, mas planeje árvores separadas ou faixas de índices reservadas para o failover dos HSMs, para que o estado nunca seja duplicado.

**EX039.** Num calendário fixo definido por política, bem antes de qualquer enfraquecimento crível do RSA — por exemplo, migrar a renovação dos carimbos de tempo para ML-DSA ou SLH-DSA assim que a TSA o suportar, e renovar os registros de evidência existentes logo em seguida.

**EX040.** Cenário: um artigo crível reduz a segurança do ML-KEM-768 abaixo da categoria 3. Participantes: Autoridade de Criptografia, responsáveis pelas plataformas, contatos dos fornecedores, comunicação. Decisões: passar ao ML-KEM-1024 ou contar temporariamente com a parte clássica do híbrido; agendar as novas versões. Sucesso: decisões em até 48 horas, caminhos de configuração identificados para todas as plataformas do nível 1.

**EX041.** "Até 31 de dez. de 2027, 90 % dos fluxos entre locais do nível 1 usam troca de chaves híbrida (evidência A/B)." "Até 30 de jun. de 2027, parcela de desconhecidos do nível 1 abaixo de 5 %." "Até 31 de dez. de 2028, raiz interna ML-DSA distribuída a 100 % das partes confiantes gerenciadas."

**EX042.** Amostra aleatória dos enlaces do nível 1; nova observação independente dos métodos negociados, a partir dos logs dos equipamentos ou de sensores passivos, ao longo de uma semana; aprovado se ≥ 95 % confirmarem o híbrido e toda falha tiver uma exceção aprovada.

**EX043.** Norma criptográfica (registros de governança); inventário com graus (repositório da CBOM); método de priorização e decisões (registros de decisão); métricas de progresso (painéis com fontes); registro de exceções (ferramenta de GRC); relatórios de testes (registros de laboratório/canário); garantia dos fornecedores (questionários e contratos).

**EX044.** "Em 14 de nov., das 22h às 2h, vamos atualizar a forma como as conexões do PACS estabelecem a cifração, para proteger as imagens a longo prazo. A visualização pode pausar brevemente durante a janela; nenhuma mudança nos fluxos de trabalho. As leituras de emergência continuam no visualizador de backup. Em caso de problema, contate a central de serviços de TI pelo ramal 4444; um engenheiro de TI da radiologia estará no local."

**EX045.** Registros de decisão e runbooks mantidos atualizados; ciclos de governança incorporados aos comitês (revisões trimestrais); substitutos e sucessores treinados, com responsabilidades compartilhadas.

**EX046.** Taxa de erro físico (por exemplo, 10^−3); número de qubits físicos; tempo de execução; código corretor de erros e distância; conectividade e tempo de ciclo — cada um com a fonte e se o hardware atual o atende.

**EX047.** O ataque se aplica aos conjuntos de parâmetros padronizados? Ele reduz a segurança abaixo da categoria do NIST visada? Foi reproduzido ou revisado por pares?

**EX048.** Viés de população: as varreduras cobrem sites públicos, e não sistemas clínicos internos ou dispositivos. Viés de ponto de observação: os scanners externos não veem as redes internas, os proxies nem as VPNs.

**EX049.** Configuração e hardware do teste; algoritmos e conjuntos de parâmetros; perfil do tráfego; dados e scripts publicados; reprodução independente ou teste por terceiros.

**EX050.** Alegação; qualidade das evidências; hipóteses principais; o que mudaria a conclusão; implicações para a prática.

**EX051.** Decisão apoiada; escopo; entregas; acesso; autorização escrita; critérios de sucesso; como os resultados serão usados; tratamento e exclusão dos dados.

**EX052.** 0 = nenhuma informação; 1 = alegação sem data; 2 = roteiro datado com algoritmos/protocolos nomeados; 3 = suporte entregue e verificado em teste, mais a divulgação do inventário.

**EX053.** 31 % − 12 % = 19 pontos; 19/31 ≈ 61 % de redução relativa.

**EX054.** Dados do projeto limitados a metadados; retidos pela duração do projeto mais 3 meses para revisão; exclusão segura com registro de verificação assinado pelo patrocinador; resultados agregados retidos.

**EX055.** Artefatos (questionário, rubrica, cláusulas, resultados), procedimentos para conduzir o processo, contatos nos fornecedores e nas compras, questões em aberto e datas.

**EX056.** Decisões robustas → registros de decisão (Cap. 1); padrões de evidência → projeto da graduação do inventário (Cap. 3); avaliação controlada → relatório de canário/avaliação (Cap. 6).

**EX057.** Atualizar a norma criptográfica depois que a FIPS 206 for finalizada; inventariar os usos de assinaturas em que a compacidade do FN-DSA ajuda; avaliar no laboratório e no canário; implantar pelas plataformas orientadas por política, com testes de agilidade.

**EX058.** A ROM de boot não consegue verificar assinaturas pós-quânticas; a substituição está programada; os controles compensatórios reduzem a exposição; a aceitação expira na substituição; a segurança dos pacientes exige firmware validado, e não mudanças provisórias arriscadas.

**EX059.** Fontes: NIST, IETF, orientações setoriais, IACR ePrint; cadência: leitura mensal, atualização trimestral do resumo; produtos: resumo atualizado, duas críticas por trimestre, uma palestra.

**EX060.** CBOM viva com responsáveis; norma criptográfica com ciclo de revisão; registros de decisão; registro de exceções com expirações; runbooks de agilidade e de resposta a quebras; sucessores treinados.

## Rota de ensino de doze disciplinas

Este é o curso de **especialização de pós-graduação**. Ele acompanha a sintética **Northgate Regional Health Trust (NRHT)** pelas decisões em escala organizacional: escolha robusta, prática atual, graduação das evidências, ética do risco, alternativas de projeto, avaliação controlada, integração, casos difíceis, garantia, crítica de pesquisas, projeto aplicado e transferência.

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
