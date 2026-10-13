# Segurança Quântica e Pós-Quântica: Implementando Serviços Resistentes ao Quântico

- Idioma: português do Brasil (`pt`); curso de tecnólogo, três anos; aproximadamente 2.400 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 30 já estão escritos em português, com os exercícios EX001–EX020 e suas resoluções; os capítulos 11–30 (EX021–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: implementadores e administradores de tecnologia — equipes de sistemas, redes, plataforma e DevOps — que vão configurar, integrar, automatizar, monitorar e passar para as operações serviços pós-quânticos. Conhecimento de entrada: fundamentos de computação e operações de segurança introdutórias.
- Relação com os livros vizinhos: o [livro de bacharelado](../../../../bachelors-4-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) desenvolve a teoria e as habilidades de pesquisa, e o [livro de engenharia](../../../../engineering-5-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) projeta sistemas. **Este livro trata da implementação**: encontrar a criptografia em serviços reais, configurar a troca de chaves híbrida, integrar a PKI e as ferramentas, automatizar verificações, monitorar, diagnosticar problemas e passar o serviço para as operações.
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação credenciada. Não concede autorização para testar sistemas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública. A criptografia de brinquedo dos laboratórios é propositalmente insegura; sistemas de produção devem usar implementações verificadas da [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), da [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), da [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) e da [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208).

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Trinta capítulos se distribuem por três anos: fundamentos de tecnologia (1–9), núcleo de implementação pós-quântica (10–23) e prática de projeto, implantação e projeto final (24–30). Cada capítulo tem objetivos de aprendizagem, ensino, um caso resolvido, uma atividade prática, erros comuns, dois exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com Python 3; a saída impressa é mostrada para que você possa conferir a sua execução. Os trechos de configuração são ilustrativos; consulte a documentação atual do seu produto.

### O caso contínuo: Kestrel Logistics Software

A **Kestrel Logistics Software (KLS)** é uma empresa sintética de 600 funcionários que opera uma plataforma SaaS de logística multi-inquilino para clientes de frete: um gateway de API público, um portal do cliente, um serviço SFTP para troca de arquivos com parceiros, um banco de dados de faturamento, frotas de leitores nos armazéns, VPNs de escritório, uma autoridade certificadora interna e um pipeline de CI/CD. Os contratos com os clientes exigem que os registros de embarque permaneçam confidenciais por dez anos. A equipe de plataforma da KLS recebeu a tarefa de tornar a plataforma resistente ao quântico. Todos os números sobre a KLS são inventados.

### Política de fontes

As fontes primárias foram verificadas em 12 de outubro de 2026: NIST FIPS 203/204/205 (agosto de 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (rascunho público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) e [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). O FN-DSA (FIPS 206) e a norma do HQC ainda estavam em desenvolvimento. Verifique a situação de novo antes de se apoiar nela.

## Sumário

| Etapa | Capítulos |
|---|---|
| Fundamentos | [1 Sistemas computacionais](#ch-01) · [2 Redes e serviços de internet](#ch-02) · [3 Fundamentos de programação](#ch-03) · [4 Modelos de dados](#ch-04) · [5 Letramento em segurança](#ch-05) · [6 Sistemas operacionais e virtualização](#ch-06) · [7 Fundamentos de identidade e acesso](#ch-07) · [8 Fundamentos de arquitetura de segurança](#ch-08) · [9 Evidências e medição](#ch-09) |
| Núcleo de implementação | [10 Orientação](#ch-10) · [11 Ativos e contexto](#ch-11) · [12 Fluxos de dados](#ch-12) · [13 Cenários de risco](#ch-13) · [14 Métodos I](#ch-14) · [15 Laboratório guiado](#ch-15) · [16 Métodos II](#ch-16) · [17 Ferramentas](#ch-17) · [18 Controles](#ch-18) · [19 Monitoramento](#ch-19) · [20 Diagnóstico de problemas](#ch-20) · [21 Integração de serviços](#ch-21) · [22 Automação](#ch-22) · [23 Avaliação](#ch-23) |
| Prática e projeto final | [24 Métodos de pesquisa aplicada](#ch-24) · [25 Ateliê de projeto em equipe](#ch-25) · [26 Passagem para as operações](#ch-26) · [27 Implantação e validação](#ch-27) · [28 Prática de campo](#ch-28) · [29 Construção do projeto final](#ch-29) · [30 Avaliação do projeto final](#ch-30) |

Capítulos 11–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever as camadas de hardware, firmware, sistema operacional, biblioteca e aplicação de um serviço; (2) localizar as funções criptográficas e as chaves em cada camada; (3) explicar o que um computador quântico é e o que não é; e (4) estimar o quão difícil é uma mudança criptográfica a partir da camada em que ela vive.

### 1.1 As camadas em que um implementador mexe

Todo serviço da KLS fica sobre uma pilha. Servidores e leitores têm processadores, memória, TPMs e placas de rede; o firmware os inicializa e verifica as assinaturas do estágio seguinte; um sistema operacional ou hipervisor isola as cargas de trabalho; bibliotecas como OpenSSL, BoringSSL, os pacotes de criptografia do Go ou os provedores do Java implementam os protocolos; as aplicações chamam essas bibliotecas; e os serviços gerenciados (balanceadores de carga, CDNs, serviços de gerenciamento de chaves na nuvem) envolvem tudo isso. Os implementadores mudam a criptografia sobretudo nas camadas do meio — versões de bibliotecas, configuração, certificados —, mas precisam conhecer as camadas de cima e de baixo, porque elas limitam o que é possível.

### 1.2 Onde vive a criptografia

A criptografia aparece em todas as camadas: assinaturas de inicialização segura no firmware; cifragem de disco e repositórios de chaves no sistema operacional; TLS, SSH e IPsec em bibliotecas e daemons; assinaturas de JSON Web Token e cifragem de campos nas aplicações; HSMs ou KMS na nuvem guardando as chaves raiz. Cada local tem um *mecanismo de mudança*: configuração (minutos), atualização de pacote (dias), versão do fornecedor (meses), substituição de hardware (anos). Anotar o mecanismo ao lado de cada uso criptográfico é o hábito mais útil para planejar o trabalho.

Na KLS, o hábito se paga de imediato: os grupos TLS do gateway de API são uma mudança de configuração, a biblioteca do ingress é uma reconstrução de imagem, o bootloader dos leitores é uma renovação de hardware.

### 1.3 Computadores quânticos em uma página

Os computadores quânticos manipulam qubits cujos estados conjuntos interferem entre si; algoritmos específicos exploram isso. O algoritmo de Shor (Shor, 1997) encontra períodos ocultos e, assim, quebra o RSA, o Diffie–Hellman e a criptografia de curvas elípticas; o algoritmo de Grover (Grover, 1996) dá apenas uma aceleração de raiz quadrada para a busca por força bruta, então o AES-256 e o SHA-256 continuam adequados ao uso. Quebrar o RSA-2048 exige uma máquina grande *com correção de erros*; Gidney (2025) estimou menos de um milhão de qubits ruidosos rodando por menos de uma semana, sob premissas declaradas, e essa máquina não existe. Para os implementadores, a mensagem prática é simples: substituir a troca de chaves e as assinaturas de chave pública; manter a cifragem simétrica e os hashes em tamanhos adequados.

### 1.4 Caso resolvido

O leitor de armazém da KLS: placa ARM sem TPM (hardware), bootloader do fornecedor que verifica assinaturas RSA (firmware, mudança por renovação de hardware), Linux embarcado (sistema operacional, imagem do fornecedor), libcurl com uma biblioteca TLS antiga (biblioteca, versão do fornecedor) e um aplicativo de leitura que envia manifestos por HTTPS (aplicação, código da KLS). Das cinco camadas, a KLS controla diretamente uma. A troca de chaves TLS do leitor só pode se tornar híbrida quando o fornecedor entregar uma nova imagem.

A tabela também mostra onde a KLS pode agir agora. O caminho de envio pode ser encurtado para que os manifestos saiam do leitor só uma vez por dia, e o contrato com o fornecedor pode ser alterado para exigir uma imagem com TLS híbrido até uma data definida. Os dois são registrados na linha do leitor, para que o risco residual tenha um dono, em vez de ser esquecido enquanto a renovação está pendente.

### 1.5 Atividade prática

Para um serviço que você administra em laboratório, liste cada camada, uma função criptográfica nela e o mecanismo de mudança. Marque as que você controla.

Uma linha resolvida para um servidor web de laboratório poderia ser: camada de biblioteca, OpenSSL 3.5 fornecendo a troca de chaves TLS, mudada por atualização de pacote, controlada por você; camada de firmware, inicialização segura UEFI com um shim assinado com RSA, mudada pelo fabricante da placa, não controlada. Procure ter pelo menos cinco linhas. Onde não conseguir nomear o mecanismo, escreva "desconhecido" em vez de chutar e anote qual documento ou pessoa poderia responder. Guarde a tabela; o esquema de inventário construído no Capítulo 4 importa exatamente estas colunas.

### 1.6 Erros comuns e limites

- Supor que uma mudança na aplicação pode corrigir a criptografia do firmware.
- Tratar os computadores quânticos como aceleradores de uso geral.
- Esquecer os serviços gerenciados que terminam o TLS em seu nome.

Cada erro tem um exemplo na KLS. Um desenvolvedor que propõe "corrigir" o bootloader RSA dos leitores no aplicativo de envio está mudando a camada errada; só a renovação do fornecedor chega ao firmware. Esperar que um computador quântico acelere o processamento de logs confunde uma capacidade criptoanalítica estreita com computação geral. E é a CDN, não a KLS, que termina o TLS dos navegadores: esquecê-la significa que o inventário mostra as configurações da origem, enquanto os clientes na verdade negociam com a borda do provedor. O limite deste capítulo é a amplitude: ele mapeia as camadas, mas ainda não as mede.

### Exercícios

- **EX001 — Tabela de camadas.** Monte uma tabela de cinco camadas para o portal do cliente da KLS, com função, mecanismo de mudança e dono. Rubrica: 3 = cinco linhas plausíveis.
- **EX002 — Manter ou substituir.** Classifique as assinaturas RSA-2048, o AES-256-GCM, o SHA-256 e o ECDHE P-256 como manter ou substituir, com um motivo para cada. Rubrica: 3 = quatro corretas, com motivos.

### Síntese

A criptografia vive em todas as camadas, e a camada determina quem pode mudá-la e com que rapidez. Os computadores quânticos ameaçam a troca de chaves e as assinaturas de chave pública, não a cifragem simétrica nem os hashes.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 30

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem

Você vai (1) explicar DNS, HTTP, TLS, SSH e IPsec no nível de implementação; (2) identificar o estabelecimento de chaves e a autenticação em cada um; (3) reconhecer como as mensagens pós-quânticas mudam de tamanho; e (4) nomear as normas que definem a troca de chaves híbrida no TLS, no SSH e no IKEv2.

### 2.1 Os serviços e os seus canais seguros

Os clientes da KLS chegam à API por DNS e HTTPS; os parceiros trocam arquivos por SFTP (SSH); os escritórios se conectam por VPNs IPsec. Cada canal seguro faz dois trabalhos: o *estabelecimento de chaves* (combinar as chaves de sessão) e a *autenticação* (provar a identidade com certificados, chaves de host ou chaves pré-compartilhadas). O risco quântico para o primeiro é colher agora, decifrar depois; para o segundo, a falsificação futura.

A distinção decide a ordem do trabalho da KLS. Sessões SFTP gravadas que transportam documentos aduaneiros de dez anos podem ser decifradas depois se a troca de chaves for clássica, então o estabelecimento de chaves vem primeiro. Uma chave de host ou um certificado falsificados só ajudam um atacante quando existir um computador quântico e enquanto essa chave ainda for confiável, então a autenticação pode vir depois, quando as bibliotecas e os repositórios de confiança estiverem prontos.

### 2.2 Troca de chaves híbrida por protocolo

No TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html)), o grupo híbrido X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) combina o ML-KEM-768 com o X25519; o key share do cliente cresce de 32 para 1.216 bytes e o do servidor para 1.120 bytes. No SSH, o OpenSSH acrescentou uma troca de chaves híbrida ML-KEM/X25519, `mlkem768x25519-sha256`, e depois a tornou o padrão ([notas de versão do OpenSSH](https://www.openssh.com/releasenotes.html)), depois de ter oferecido antes um híbrido baseado no sntrup761. No IKEv2, a [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html) permite até sete trocas de chaves adicionais, usadas para acrescentar o ML-KEM ao lado do Diffie–Hellman clássico; a [RFC 8784](https://www.rfc-editor.org/rfc/rfc8784.html) mistura chaves pré-compartilhadas pós-quânticas como medida provisória. A terminologia dessas combinações está na [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html).

### 2.3 Efeitos de tamanho

Um ClientHello que transporta um key share ML-KEM geralmente ultrapassa um pacote de 1.500 bytes. A maioria das pilhas lida com isso; alguns middleboxes e balanceadores de carga antigos, não. As assinaturas pós-quânticas são ainda maiores (ML-DSA-44: 2.420 bytes por assinatura na [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)), o que importa quando os certificados mudarem. O DNSSEC, que roda sobre UDP com limites de tamanho apertados, é especialmente sensível ao tamanho das assinaturas.

Na KLS, o efeito de tamanho é medido, não suposto: o key share híbrido do cliente acrescenta 1.184 bytes, o que empurra um ClientHello típico para além de um segmento. O Laboratório H, no Capítulo 20, mostra a assinatura da falha: ClientHellos de 1.530 bytes expirando num caminho de proxy. Os certificados ainda não foram alterados, então a assinatura de 2.420 bytes do ML-DSA-44 é uma preocupação posterior; a zona DNS continua clássica até que os tamanhos de assinatura e o comportamento dos resolvedores sejam entendidos.

### 2.4 Caso resolvido

A KLS habilita o X25519MLKEM768 num gateway de API de homologação. Os navegadores modernos e o SDK do cliente baseado em Go o negociam de imediato; o cliente Java legado de um cliente oferece apenas grupos clássicos e recua para o X25519, como previsto. Uma sonda de monitoramento de terceiros expira — o seu appliance descarta o ClientHello de dois segmentos. A correção é atualizar a sonda, não desabilitar o grupo.

A execução em homologação também deu à KLS a sua primeira regra de implantação. O recuo do cliente Java é aceitável e é acompanhado como uma fração das sessões; um timeout não é aceitável e precisa ser rastreado até um dispositivo. O fornecedor do monitoramento recebeu um chamado com o tamanho do ClientHello capturado no laboratório, e a lista de grupos da homologação ficou inalterada enquanto a sonda era atualizada.

### 2.5 Atividade prática

Em laboratório, conecte-se a um servidor de teste com um cliente TLS que imprima o grupo negociado, uma vez com o híbrido oferecido e outra sem ele. Registre os tamanhos do ClientHello a partir de uma captura do tráfego do seu próprio laboratório.

Use dois clientes se uma biblioteca não conseguir desabilitar o key share híbrido: por exemplo, um cliente OpenSSL 3.5 com os grupos padrão e o mesmo cliente forçado a usar apenas `X25519`. Registre, para cada execução, o grupo negociado, o comprimento do ClientHello na sua própria captura e se o hello ocupa um ou dois segmentos TCP. Espere cerca de 1.200 bytes a mais com o híbrido. Escreva uma frase explicando o que um middlebox que remonta apenas o primeiro segmento faria com cada execução.

### 2.6 Erros comuns e limites

- Acreditar que a troca de chaves híbrida muda os algoritmos dos certificados.
- Tratar as migrações de SSH e de TLS como uma única tarefa.
- Capturar tráfego que você não tem autorização para capturar.

A troca de chaves híbrida muda apenas a extensão do key share; o certificado e a sua assinatura RSA ou ECDSA ficam intactos, e é por isso que a KLS acompanha os certificados separadamente. SSH e TLS compartilham a ideia, mas não o software: a lista `KexAlgorithms` do OpenSSH nos hosts SFTP e a lista de grupos TLS do gateway são configuradas, testadas e revertidas de forma independente. As capturas se restringem ao tráfego de laboratório ou a escopos autorizados, porque os pacotes dos clientes contêm os dados deles.

### Exercícios

- **EX003 — Mapa de protocolos.** Para o TLS 1.3, o SSH e o IKEv2, nomeie o mecanismo híbrido e o documento que o define. Rubrica: 3 = três corretos, com fontes.
- **EX004 — Diferença em bytes.** Quantos bytes o key share do servidor no X25519MLKEM768 tem a mais do que um key share X25519? Rubrica: 3 = 1.088 bytes (1.120 − 32), observando que isso é igual ao texto cifrado do ML-KEM-768.

### Síntese

Cada canal seguro separa o estabelecimento de chaves da autenticação. A troca de chaves híbrida é padronizada para o TLS, está disponível no SSH e é especificada para o IKEv2; ela aumenta os handshakes e pode expor middleboxes antigos.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 30

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem

Você vai (1) escrever pequenos scripts em Python com funções, dicionários e laços; (2) tratar bytes, codificações e comprimentos com precisão; (3) usar corretamente `hashlib`, `hmac` e `secrets`; e (4) escrever testes que possam falhar.

### 3.1 Scripts para implementadores

Os implementadores escrevem scripts para inventariar, verificar e automatizar. Um script de trinta linhas que analisa exportações de configuração e sinaliza serviços apenas clássicos vale mais do que uma checklist manual, porque pode rodar toda noite. Os laboratórios deste livro usam apenas a biblioteca padrão do Python, para que rodem em qualquer lugar.

O primeiro script desse tipo da KLS lê as configurações exportadas do ingress e dos balanceadores de carga, lista os grupos configurados por listener e imprime qualquer listener de nível 1 sem `X25519MLKEM768`. Rodando toda noite, ele encontrou a lista mal ordenada do portal do cliente muito antes do que o alerta de monitoramento do Capítulo 19 teria encontrado. Manter o script com menos de 50 linhas o manteve revisável.

### 3.2 Bytes e comprimentos

Chaves, textos cifrados e assinaturas são bytes com comprimentos exatos: as chaves de encapsulamento do ML-KEM-768 têm 1.184 bytes e os textos cifrados, 1.088 bytes ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)); as chaves públicas do ML-DSA-65 têm 1.952 bytes e as assinaturas, 3.309 bytes (FIPS 204). Um código que os guarda em colunas de banco de dados de tamanho fixo, campos base64 ou protocol buffers dimensionados para o ECDSA vai truncá-los ou rejeitá-los. Verifique sempre os comprimentos explicitamente e falhe de forma fechada.

Os comprimentos também são a validação mais barata que um implementador pode acrescentar. Uma função que rejeita uma chave ML-KEM-768 de 1.183 bytes, como faz o Laboratório V no Capítulo 15, apanha truncamentos, conjuntos de parâmetros errados e confusões de codificação antes de qualquer chamada à biblioteca. A KLS guarda o conjunto de parâmetros ao lado de cada chave, para que o comprimento esperado possa ser consultado em vez de adivinhado.

### 3.3 Criptografia da biblioteca padrão

`secrets.token_bytes(n)` fornece bytes aleatórios seguros; `random`, não. `hashlib.sha256`, `hashlib.sha3_256` e `hashlib.shake_256` calculam hashes; `hmac.new(key, msg, hashlib.sha256)` calcula MACs; `hmac.compare_digest` compara segredos em tempo constante. A biblioteca padrão do Python não implementa o ML-KEM nem o ML-DSA; o código de produção chama uma biblioteca verificada ou o provedor da plataforma.

Vale a pena conhecer o `hashlib.shake_256`, porque o ML-KEM e o ML-DSA usam SHAKE internamente; os implementadores o encontram nos testes de resposta conhecida, mesmo que nunca implementem os esquemas. O módulo `secrets` tira os seus valores do gerador do sistema operacional, que é o que os scripts da KLS usam para chaves de laboratório e vetores de teste.

### 3.4 Caso resolvido

Um desenvolvedor da KLS guarda chaves públicas numa coluna `VARCHAR(512)` com texto base64. O base64 expande os bytes em 4/3, então uma chave ML-DSA-65 de 1.952 bytes precisa de 2.604 caracteres e é truncada silenciosamente por um modo permissivo do banco de dados. Um teste que fizesse um valor aleatório de 1.952 bytes ir e voltar pela camada de armazenamento teria apanhado o problema:

```python
import base64, secrets
key = secrets.token_bytes(1952)
enc = base64.b64encode(key).decode()
assert len(enc) == 2604 and base64.b64decode(enc) == key
print("round trip ok,", len(enc), "chars")
```

A correção teve duas partes: a coluna passou a um tipo binário dimensionado a partir da maior chave que a KLS planeja guardar, os 2.592 bytes do ML-DSA-87, e o banco de dados passou ao modo estrito, para que um valor grande demais gere um erro em vez de ser cortado. O teste de ida e volta agora roda para cada tipo de chave da tabela de comprimentos do inventário.

### 3.5 Atividade prática

Escreva `check_len(kind, data)` usando um dicionário com os comprimentos esperados das chaves de encapsulamento do ML-KEM-512/768/1024, e teste entradas válidas e inválidas.

Um bom arquivo de testes tem pelo menos seis casos: os três comprimentos corretos (800, 1.184 e 1.568 bytes), um valor com um byte a menos, um valor com um byte a mais e um comprimento correto passado com o rótulo de tipo errado, como 1.184 bytes rotulados ML-KEM-512. A função deve gerar um erro que nomeie o tipo, o comprimento esperado e o comprimento real. Rode os testes uma vez com um defeito proposital, um número errado no dicionário, para mostrar que eles podem falhar.

### 3.6 Erros comuns e limites

- Campos de tamanho fixo dimensionados para chaves clássicas.
- `random` para segredos.
- Testes que só exercitam os caminhos de sucesso.

Na KLS, cada erro teve um custo. A coluna `VARCHAR(512)` truncou silenciosamente chaves ML-DSA num modo permissivo. Um script de teste de carga que montava tokens de sessão com `random` produziu valores previsíveis que um revisor conseguiu reproduzir a partir da semente. Um teste de armazenamento que só gravava chaves válidas passou por meses, enquanto o defeito de truncamento ficava escondido atrás dele. Os scripts são pequenos, mas cada um desses erros sobrevive justamente porque ninguém acha que um script pequeno precisa de testes de falha.

### 3.7 Lendo a documentação das bibliotecas

Antes de chamar qualquer API criptográfica, leia o que ela promete: qual conjunto de parâmetros uma função usa por padrão, se ela devolve erros ou lança exceções, se as chaves são expandidas ou guardadas como sementes e quais codificações ela aceita. A FIPS 203 e a FIPS 204 permitem que as chaves privadas sejam guardadas como sementes curtas que se expandem de forma determinística; duas bibliotecas podem discordar sobre qual forma exportam. Escreva no seu repositório uma nota curta para cada biblioteca que usar, com versão, padrões e codificações, e crie um link para ela no inventário, para que o próximo implementador não precise redescobrir tudo.

### Exercícios

- **EX005 — Dimensionamento em base64.** Quantos caracteres base64 uma assinatura ML-DSA-65 de 3.309 bytes exige? Rubrica: 3 = 4.412, com o método (ceil(3309/3) × 4).
- **EX006 — Tempo constante.** Explique por que `a == b` é arriscado para comparar tags de MAC e o que usar no lugar. Rubrica: 3 = vazamento de tempo por saída antecipada, `hmac.compare_digest`.

### Síntese

Os scripts de implementação precisam tratar bytes e comprimentos com exatidão, usar aleatoriedade segura e comparação em tempo constante, e ser testados tanto na falha quanto no sucesso.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 30

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem

Você vai (1) modelar serviços, endpoints, certificados e algoritmos como registros relacionados; (2) projetar um esquema de inventário com proveniência; (3) associar atributos de tempo de vida dos dados; e (4) consultar o modelo em busca de candidatos à migração.

### 4.1 Um esquema de inventário

Um esquema prático tem tabelas para `service` (nome, dono, nível), `endpoint` (host, porta, protocolo), `crypto_use` (endpoint, função, algoritmo, parâmetro, biblioteca, versão), `observation` (crypto_use, método, data e hora, observador) e `data_class` (nome, confidentiality_years) ligadas aos serviços. Separar a observação do uso permite registrar que o mesmo uso foi visto por um scanner na segunda-feira e confirmado na configuração na quarta-feira.

A KLS acrescenta duas colunas práticas: `change_mechanism` em `crypto_use`, com configuração, pacote, versão do fornecedor ou hardware, e `controller` em `endpoint`. Com elas, uma única consulta lista todas as trocas de chaves clássicas que a KLS pode corrigir por configuração neste mês.

### 4.2 Proveniência e atualidade

Toda linha precisa de um método (captura passiva, configuração, varredura de código, declaração do fornecedor) e de uma data e hora. As observações antigas são rebaixadas para "não verificadas" em vez de apagadas. Sem proveniência, um painel mistura fatos com palpites, e ninguém sabe quais são quais.

A KLS usa três graus: confirmado (dois métodos independentes concordam), observado (um método nos últimos 30 dias) e não verificado (mais antigo, ou uma única declaração do fornecedor). O painel de 71 % do Capítulo 9 deu errado em parte porque linhas da época do scanner, sem rótulo de método, foram contadas como atuais. O grau é calculado a partir da tabela de observações, nunca digitado à mão, para que não possa se afastar das evidências.

### 4.3 Tempos de vida

Associe `confidentiality_years` às classes de dados. Os registros de embarque da KLS precisam permanecer confidenciais por dez anos, por contrato; os dados de faturamento, sete; a telemetria, um. Uma consulta que cruza os tempos de vida com os algoritmos de troca de chaves produz automaticamente a lista de candidatos a colher agora, decifrar depois.

O texto do contrato vale mais do que as tabelas de retenção: os dados de faturamento da KLS são retidos por sete anos por razões fiscais, mas o contrato de um cliente de frete exige confidencialidade de dez anos para as tarifas, então as linhas de faturamento desse cliente herdam dez. Por isso, a coluna de tempo de vida fica na classe de dados e pode ser sobrescrita por cliente, e a consulta usa o maior tempo de vida entre as classes que um fluxo transporta.

### 4.4 Caso resolvido

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE use(service TEXT, function TEXT, algorithm TEXT, data_years INT);
INSERT INTO use VALUES ('api-gateway','kex','X25519MLKEM768',10),('partner-sftp','kex','ecdh-sha2-nistp256',10),
                       ('billing-db','kex','ECDHE-P256',7),('telemetry','kex','ECDHE-P256',1);""")
rows = db.execute("SELECT service FROM use WHERE function='kex' AND algorithm NOT LIKE '%MLKEM%' AND data_years>=5").fetchall()
print("HNDL candidates:", [r[0] for r in rows])
```

A consulta devolve o SFTP dos parceiros e o banco de dados de faturamento; a telemetria fica de fora porque os seus dados têm vida curta, e o gateway já é híbrido.

A consulta codifica três decisões que vale a pena ler em voz alta. A condição `function='kex'` a limita à exposição a colher agora, decifrar depois, porque as assinaturas seguem outro calendário. O teste `NOT LIKE '%MLKEM%'` trata qualquer grupo híbrido como aceitável. O limite `data_years>=5` é uma política da KLS, não uma norma; com três anos, o banco de dados de faturamento continuaria listado e a telemetria continuaria fora. Executada de novo após cada alimentação do inventário, a lista se torna uma fila de trabalho viva para a equipe de plataforma.

### 4.5 Atividade prática

Estenda o exemplo com uma tabela `observation` e uma consulta que liste os usos cuja observação mais recente tem mais de 90 dias.

Dê à tabela `observation` uma chave estrangeira para `use`, uma coluna `method` e uma data e hora `observed_at` guardada como texto ISO. Insira duas observações para o gateway, uma de 10 dias e outra de 200 dias, e uma observação de 120 dias para o SFTP dos parceiros. A consulta correta agrupa por uso e compara a data e hora máxima com o limite, de modo que o gateway é atual porque a sua linha mais recente é recente. Uma consulta que compara todas as linhas listaria o gateway por engano; inclua esse erro como teste negativo.

### 4.6 Erros comuns e limites

- Planilhas planas sem proveniência.
- Apagar dados antigos em vez de marcá-los.
- Tempos de vida copiados das tabelas de retenção sem conferir os contratos.

Na KLS, a planilha plana tinha uma coluna "algoritmo" com valores digitados por quatro pessoas; ninguém sabia dizer se o "ECDHE" do faturamento tinha vindo de uma varredura, de um arquivo de configuração ou da memória. Apagar as linhas antigas removeu por completo a telemetria das empilhadeiras, o que escondeu que ninguém conhecia a sua criptografia. E a primeira lista de tempos de vida copiou a retenção fiscal de sete anos para o faturamento, deixando de lado a cláusula contratual de dez anos. Cada erro torna a lista de migração mais curta do que deveria ser, o que parece progresso, mas não é.

### 4.7 Mantendo o modelo atualizado

Um modelo de inventário começa a envelhecer no momento em que é preenchido. Alimente-o automaticamente: exportações noturnas de configuração dos balanceadores de carga, listas de certificados do banco de dados da AC, manifestos de imagens do registro e resumos de handshakes tirados dos logs. Cada alimentação grava observações com o seu próprio rótulo de método, para que o modelo sempre mostre o que foi visto, como e quando. As linhas digitadas à mão devem ser a exceção e devem trazer o nome de quem as digitou. Quando duas fontes discordam — a configuração diz que o híbrido está habilitado, os logs não mostram nenhuma negociação híbrida —, registre as duas e abra uma tarefa; a discordância costuma ser o fato mais útil do modelo.

O acesso ao modelo também importa. Um mapa completo de quais serviços ainda usam troca de chaves clássica é útil para um atacante, então restrinja o acesso de escrita às alimentações e o de leitura às equipes que precisam dele, e publique apenas agregados fora do grupo de plataforma.

### Exercícios

- **EX007 — Esquema.** Liste as colunas de uma tabela `observation` e explique cada uma. Rubrica: 3 = referência ao uso, método, data e hora, observador, ponteiro para a evidência bruta.
- **EX008 — Consulta.** Escreva um SQL que devolva os serviços com assinaturas clássicas em certificados válidos além de 2030. Rubrica: 3 = condições corretas sobre função, algoritmo e validade.

### Síntese

Um inventário relacional com proveniência e tempos de vida transforma o planejamento da migração em consultas que podem ser executadas de novo sempre que o parque mudar.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 30

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) aplicar confidencialidade, integridade, disponibilidade e autenticidade às mudanças em serviços; (2) relacionar ativos, ameaças, vulnerabilidades e controles; (3) explicar colher agora, decifrar depois e forjar depois; e (4) reconhecer o risco de disponibilidade numa mudança criptográfica.

### 5.1 Propriedades e mudanças

Os implementadores mudam a criptografia para melhorar a confidencialidade e a autenticidade, mas toda mudança arrisca a disponibilidade. Um grupo híbrido que um balanceador de carga não consegue interpretar é uma indisponibilidade. A boa prática trata a disponibilidade como um requisito de mesmo peso: implantação em etapas, reversão, monitoramento.

A regra aparece nos próprios registros da KLS: a sonda de monitoramento que expirou no gateway de homologação teria sido uma tempestade de alertas em produção se o grupo tivesse entrado no ar em todos os lugares ao mesmo tempo. Por isso, cada mudança híbrida traz no seu plano uma reversão, um painel e uma etapa canário.

### 5.2 Vocabulário de risco

Um *ativo* (os registros de embarque), uma *ameaça* (um adversário gravando o tráfego), uma *vulnerabilidade* (a troca de chaves clássica) e um *controle* (a troca de chaves híbrida) se combinam num cenário de risco. As vulnerabilidades quânticas são propriedades dos algoritmos, não defeitos, e se tornam exploráveis quando surge uma capacidade.

Escrever as quatro partes separadamente também mostra onde um controle atua. A troca de chaves híbrida remove a vulnerabilidade apenas para as sessões futuras; ela não faz nada pelo tráfego já gravado. Encurtar a retenção, por sua vez, reduz o valor do ativo. Para o SFTP dos parceiros da KLS, o cenário completo é: documentos aduaneiros, gravados por um adversário numa rede de trânsito, legíveis por causa da troca de chaves ECDH, mitigados pelo `mlkem768x25519-sha256` a partir da data da atualização.

### 5.3 Dois padrões

*Colher agora, decifrar depois*: o tráfego gravado é decifrado quando existir um computador quântico; é urgente para dados cuja confidencialidade dura além desse momento. *Forjar depois*: quando existir um computador quântico, as assinaturas podem ser forjadas; é urgente para a confiança de longa duração (ACs raiz, assinatura de firmware, documentos verificados por anos) e para dispositivos que não podem ser atualizados.

A urgência de cada um é uma questão de datas. A exposição a HNDL começa no dia em que o tráfego é gravado, então, para os dados de embarque de dez anos da KLS, cada sessão clássica de hoje importa. A exposição a forjar depois só começa quando a falsificação se torna possível e dura enquanto a chave for confiável, então a raiz interna de 15 anos é urgente e uma chave de JWT semanal não é.

### 5.4 Caso resolvido

O serviço SFTP dos parceiros da KLS transporta documentos aduaneiros mantidos confidenciais por dez anos; ele usa troca de chaves ECDH: exposto a HNDL agora. A sua chave de host é Ed25519: exposição a forjar depois, de menor urgência, porque as chaves de host podem ser rotacionadas rapidamente quando os clientes SSH suportarem algoritmos de chave de host pós-quânticos. As chaves de assinatura de JWT da API são rotacionadas semanalmente: a exposição a forjar depois é mínima até que exista um computador quântico.

Os três casos dão à KLS três respostas diferentes. A troca de chaves do SFTP é agendada para a próxima janela de manutenção. A chave de host é registrada como risco residual com um gatilho: quando o OpenSSH lançar um algoritmo de chave de host pós-quântico que os clientes da KLS suportem, rotacionar. As chaves de JWT não precisam de nada além de manter a rotação automatizada.

### 5.5 Atividade prática

Escreva três cenários de risco para serviços da KLS usando o padrão ativo–ameaça–vulnerabilidade–controle; rotule cada um como HNDL, forjar depois ou nenhum.

Um cenário completo nomeia as quatro partes e o rótulo. Exemplo: ativo, a replicação do banco de dados de faturamento transportando faturas de sete anos; ameaça, gravação na rede entre zonas do provedor; vulnerabilidade, ECDHE-P256 no TLS da replicação; controle, híbrido suportado pelo provedor ou cifragem de campos na camada de aplicação; rótulo HNDL. Inclua um cenário rotulado nenhum, como os backups em AES-256, e explique por quê: a aceleração de Grover deixa uma chave de 256 bits com ampla margem, então nenhuma ação motivada pelo quântico é necessária.

### 5.6 Erros comuns e limites

- Esquecer a disponibilidade nos planos de mudança.
- Tratar todo risco quântico como igualmente urgente.
- Chamar os algoritmos de "defeitos".

Cada erro leva a uma falha reconhecível. Um plano sem trabalho de disponibilidade habilita o híbrido no portal e descobre o proxy antigo num cliente por meio de um chamado de suporte. Tratar toda exposição como urgente coloca as chaves de JWT semanais na mesma fila do tráfego SFTP de dez anos e atrasa as duas. Chamar o RSA de "defeito" convida a uma mentalidade de correção; não há correção, só substituição, e o cronograma depende de uma capacidade que ainda não existe.

### 5.7 Transformando o risco em tarefas

Os implementadores traduzem cada cenário de risco em itens de trabalho com uma definição clara de pronto. "Exposição a HNDL do SFTP dos parceiros" se torna: confirmar que a versão do OpenSSH nos hosts SFTP suporta `mlkem768x25519-sha256`; habilitá-lo em primeiro lugar na lista de troca de chaves do servidor em homologação; verificar quais clientes dos parceiros o negociam; publicar um aviso aos parceiros; promover para produção; monitorar a fração de sessões que o usam. Cada item tem um dono e uma evidência que prova que está concluído. Declarações de risco que nunca viram tarefas são a forma mais comum de o trabalho de segurança empacar entre o registro de riscos e o backlog da plataforma.

Mantenha a disponibilidade em toda definição de pronto: uma tarefa não está concluída até que a reversão tenha sido testada e o monitoramento não mostre aumento de falhas.

### Exercícios

- **EX009 — Classificar.** Rotule como HNDL, forjar depois ou nenhum: o tráfego da VPN do escritório, a chave de assinatura de código do CI, os backups em AES-256, o TLS para o portal do cliente. Rubrica: 3 = quatro corretos, com motivos.
- **EX010 — Disponibilidade.** Nomeie duas formas pelas quais habilitar a troca de chaves híbrida poderia causar uma indisponibilidade e um controle para cada uma. Rubrica: 3 = dois modos de falha, com controles.

### Síntese

Os implementadores precisam pesar os ganhos de confidencialidade e de autenticidade contra o risco de disponibilidade, e distinguir os padrões ligados ao tempo de colher agora, decifrar depois e de forjar depois.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 30

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem

Você vai (1) explicar o isolamento de processos, os privilégios e os repositórios de chaves; (2) identificar os provedores e as políticas criptográficas do sistema; (3) reconhecer bibliotecas ligadas estaticamente e empacotadas em contêineres; e (4) planejar atualizações de sistema operacional e de imagem que habilitem algoritmos pós-quânticos.

### 6.1 Provedores e políticas

No Linux, a maioria dos serviços se liga a uma biblioteca TLS do sistema; o OpenSSL 3.5 acrescentou suporte ao ML-KEM, ao ML-DSA e ao SLH-DSA e grupos TLS híbridos ([notas de versão do OpenSSL 3.5](https://github.com/openssl/openssl/blob/openssl-3.5/NEWS.md)). Algumas distribuições centralizam os algoritmos permitidos numa política criptográfica de todo o sistema. O Windows usa o CNG; as plataformas móveis fornecem repositórios de chaves e o TLS da plataforma. A versão do provedor no host determina em grande parte o que os serviços podem negociar — a menos que o serviço traga a sua própria biblioteca.

Nos nós da KLS, a primeira verificação é, portanto, `openssl version` mais a política criptográfica da distribuição, que pode remover um grupo que a biblioteca suporta.

### 6.2 Contêineres e ligação estática

Os contêineres empacotam as suas próprias bibliotecas de espaço de usuário; atualizar o sistema operacional do host não muda a biblioteca TLS dentro de uma imagem. Os binários Go e Rust frequentemente ligam a sua criptografia de forma estática. Os implementadores precisam inventariar imagens e binários, não só hosts, e reconstruir as imagens sobre camadas base atualizadas.

A varredura do registro da KLS encontrou o padrão com clareza: a imagem do ingress NGINX trazia um OpenSSL duas versões menores atrás dos hosts, e três serviços Go foram compilados com um toolchain anterior ao TLS híbrido. Nenhum deles mudou quando a frota de nós foi atualizada. O inventário agora lista as versões de biblioteca e de toolchain por digest de imagem, não por host, e a reconstrução é o mecanismo de mudança registrado para cada um.

### 6.3 Virtualização e chaves

Hipervisores, TPMs virtuais e KMS na nuvem guardam chaves de discos e cargas de trabalho. As suas APIs e o suporte a algoritmos mudam no calendário do provedor de nuvem. Registre quais tipos de chave e algoritmos de KMS cada carga de trabalho usa.

Na KLS, isso abrange as chaves do KMS na nuvem que envolvem os discos dos bancos de dados, os TPMs virtuais dos runners de CI e o cluster de HSMs por trás da AC interna. As chaves de envolvimento de disco são simétricas e continuam adequadas ao uso; as chaves assimétricas usadas na importação para o KMS e na assinatura da AC são as que devem ser acompanhadas. A lista de algoritmos publicada por cada provedor e a data da última verificação vão para a coluna de evidências de fornecedores do inventário.

### 6.4 Caso resolvido

A KLS atualiza os seus nós Kubernetes para uma distribuição com OpenSSL 3.5. O contêiner do ingress NGINX ainda roda uma imagem base antiga e continua oferecendo apenas grupos clássicos. Uma reconstrução sobre uma nova imagem base habilita o X25519MLKEM768. O serviço de faturamento, escrito em Go, só ganha suporte ao híbrido depois de uma atualização do toolchain, porque a pilha TLS do Go é compilada junto.

O caso resolvido dá três mecanismos de mudança para um único cluster: uma atualização de nós (feita), uma reconstrução de imagem (um pull request, testado em homologação) e uma atualização de toolchain (uma versão do serviço com testes de regressão). A KLS os agendou separadamente e registrou qual deles ativou a fração híbrida, para que as regressões posteriores pudessem ser rastreadas até o artefato certo.

### 6.5 Atividade prática

Num host de laboratório, liste a versão do OpenSSL no host e dentro de dois contêineres; liste os binários Go ou Rust e as versões dos seus toolchains.

Rode `openssl version` no host e depois `docker run --rm IMAGE openssl version` para cada contêiner, ou inspecione a lista de pacotes da imagem quando não houver shell. Para binários Go, `go version -m BINARY` imprime o toolchain; para Rust, verifique os metadados de compilação ou o `Cargo.lock`. Coloque os resultados numa tabela com host, digest da imagem, biblioteca, versão e se essa versão suporta o ML-KEM. Uma divergência entre o host e o contêiner é a constatação esperada, não uma anomalia.

### 6.6 Erros comuns e limites

- Supor que as atualizações do host mudam os contêineres.
- Editar as políticas criptográficas do sistema em produção sem homologação.
- Ignorar as pilhas TLS compiladas junto.

Cada erro apareceu na KLS. O anúncio da atualização dos nós dizia "TLS híbrido disponível", enquanto o contêiner do ingress continuava negociando X25519. Uma edição de teste da política criptográfica do sistema num host de produção desabilitou um grupo de que um agente de monitoramento precisava, e o agente parou de reportar até que a mudança fosse revertida. E o serviço de faturamento em Go, invisível às varreduras de pacotes, manteve a sua pilha TLS antiga até que alguém lesse os seus metadados de compilação.

### 6.7 Cadência de patches

O suporte pós-quântico chega por meio dos patches comuns, então a cadência de patches da equipe se torna uma alavanca da migração. Acompanhe, para cada imagem base e toolchain, quantos dias ela está atrasada em relação à versão suportada atual. Os serviços atrasados em um ano não conseguem adotar a troca de chaves híbrida sem uma grande atualização de recuperação, que é mais arriscada do que as pequenas atualizações regulares que os teriam mantido em dia.

A KLS mediu o atraso no seu registro: idade mediana das imagens base de 140 dias, pior caso de 410 dias para um serviço legado de relatórios. Esse serviço agora tem uma reconstrução agendada a cada 30 dias, e o seu atraso é uma métrica de painel sob a responsabilidade da sua equipe.

### Exercícios

- **EX011 — Onde mudar.** Para um contêiner NGINX, um serviço Go e um daemon SSH do host, diga o que precisa mudar para habilitar a troca de chaves híbrida. Rubrica: 3 = reconstrução da imagem, toolchain/reconstrução, pacote/configuração do host.
- **EX012 — Política de imagens.** Proponha uma regra de CI que impeça a implantação de imagens com bibliotecas TLS desatualizadas. Rubrica: 3 = verificação concreta, limite, caminho de exceção.

### Síntese

Os sistemas operacionais fornecem provedores criptográficos, mas os contêineres e os binários compilados trazem os seus próprios; o trabalho de implementação segue as bibliotecas até as imagens e os toolchains.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 30

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem

Você vai (1) distinguir autenticação de autorização nos serviços; (2) explicar certificados, cadeias e repositórios de confiança; (3) identificar as assinaturas relevantes para o quântico em SSO, mTLS, SSH e assinatura de código; e (4) planejar a ordem das mudanças de identidade pós-quânticas.

### 7.1 Onde as assinaturas autenticam

Os usuários entram por um SSO cujos tokens são assinados (RSA ou ECDSA); os serviços se autenticam entre si com certificados de TLS mútuo; os administradores usam chaves SSH; os pipelines de CI assinam artefatos; os dispositivos guardam certificados para o registro. A autorização (papéis, políticas) não é ameaçada pelos computadores quânticos; as assinaturas por trás da autenticação, sim.

Na KLS, essa lista corresponde a chaves concretas: a chave de token RS256 do provedor de SSO, a chave emissora ECDSA P-256 da AC interna, as chaves SSH Ed25519 dos administradores, a chave de assinatura de versões RSA-3072 e os certificados de registro de dispositivos nos leitores. Cada uma ganha uma linha com algoritmo, tempo de vida e o sistema que a verifica, porque é o verificador, mais do que o signatário, que costuma limitar a migração.

### 7.2 Cadeias e repositórios de confiança

Um certificado é confiável se encadeia até uma raiz no repositório de confiança do verificador. Introduzir uma raiz pós-quântica significa atualizar primeiro todos os repositórios de confiança — sistemas operacionais, runtimes de linguagens, appliances, sistemas de parceiros. A PKI interna é o melhor lugar para começar com certificados pós-quânticos, porque a KLS controla tanto os emissores quanto os verificadores.

Os sistemas dos parceiros são os repositórios mais lentos de mudar, porque a KLS não pode enviar atualizações para eles; qualquer ligação mTLS com um parceiro precisa que a nova raiz seja entregue e confirmada com meses de antecedência. Dentro da KLS, o pacote de ACs da imagem base dos contêineres e os truststores Java dos serviços são os repositórios mais esquecidos, já que são embutidos nos artefatos em vez de gerenciados nos hosts.

### 7.3 Ordem das mudanças

Comece pelos itens em que o risco de forjar depois é alto e o controle também: a raiz e as intermediárias internas, a assinatura de código de artefatos de vida longa. Deixe os tokens de vida curta para depois; as suas chaves podem ser rotacionadas rapidamente quando as bibliotecas suportarem o ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)). Os certificados web públicos seguem o suporte das ACs públicas e dos navegadores.

A ordem também tem uma vantagem prática. As raízes internas e as chaves de assinatura são poucas, pertencem a uma única equipe e mudam em cerimônias planejadas, então são bons primeiros projetos. Os milhares de certificados finais e de tokens seguem automaticamente quando os emissores e os verificadores suportarem o ML-DSA, então o esforço gasto neles cedo é, na maior parte, desperdiçado esperando pelas bibliotecas.

### 7.4 Caso resolvido

O inventário de identidade da KLS: tokens de SSO RS256 (tempo de vida de 1 hora); mTLS dos serviços pela AC interna (ECDSA P-256, certificados finais de 90 dias, raiz de 15 anos); chaves SSH de usuário Ed25519; assinatura de versões RSA-3072. Prioridade: a raiz interna (vida longa, controlada), a assinatura de versões (artefatos verificados por anos), depois os certificados finais de mTLS, o SSH e os tokens.

A lista também mostra onde a KLS pode se preparar sem algoritmos novos. A assinatura de versões pode acrescentar desde já um segundo campo de assinatura ao formato dos artefatos, de modo que acrescentar o ML-DSA depois seja uma mudança de pipeline. O SSH pode passar a usar certificados de uma autoridade central, para que as chaves de usuário sejam rotacionadas de forma central. Nenhum dos dois passos exige suporte pós-quântico, e ambos encurtam o tempo de migração mais tarde.

### 7.5 Atividade prática

Desenhe a PKI interna da KLS com a raiz, as intermediárias e os tipos de certificados finais, e liste todos os repositórios de confiança que precisam aceitar uma nova raiz.

O desenho deve mostrar a raiz de 15 anos offline, pelo menos uma intermediária emissora e os tipos de certificados finais para os serviços da malha, o ingress, os agentes de monitoramento e os dispositivos. Depois, liste os repositórios de confiança por parte confiante: pacotes do sistema operacional do host, pacotes das imagens de contêiner, truststores Java, pacotes de confiança dos sidecars da malha, agentes de monitoramento, runners de CI e qualquer parceiro que verifique certificados da KLS em mTLS. Marque quais repositórios a KLS atualiza por configuração e quais só por reconstrução ou pedindo ao parceiro. O mais longo desses caminhos define a data segura mais cedo para emitir certificados finais pós-quânticos.

### 7.6 Erros comuns e limites

- Emitir certificados finais pós-quânticos antes que os repositórios de confiança aceitem a raiz.
- Tratar os dados de autorização como vulneráveis ao quântico.
- Esquecer os repositórios de confiança dos parceiros.

No laboratório da KLS, o primeiro erro produziu exatamente o resultado esperado: um certificado final de teste assinado por uma intermediária ML-DSA falhou na validação em todos os serviços Java, porque os seus truststores não tinham recebido a nova raiz. Gastar esforço com mapeamentos de papéis ou políticas de autorização é o segundo erro, já que eles não são criptográficos. O terceiro é o mais lento de corrigir: um parceiro que fixa a raiz atual da KLS vai rejeitar uma nova cadeia até que os seus próprios operadores a atualizem.

### 7.7 Chaves SSH de host e de usuário

O SSH ilustra a separação entre a troca de chaves e a identidade. A troca de chaves híbrida no OpenSSH protege desde já a confidencialidade da sessão, enquanto as chaves de host e de usuário continuam sendo assinaturas clássicas. Rotacionar as chaves de host é barato do ponto de vista operacional se os clientes usam certificados ou arquivos known-hosts gerenciados, e caro se cada usuário fixou chaves individuais. Por isso, passar os administradores para certificados SSH emitidos por uma autoridade central é um passo útil de agilidade, mesmo antes de implantar qualquer algoritmo de chave de host pós-quântico.

Os administradores da KLS hoje confiam nas chaves de host por meio de entradas individuais em `known_hosts`, então uma mudança de chave de host produz avisos em toda a equipe. Passar para certificados de host significa uma única chave de AC na configuração de cada cliente, e uma futura mudança para um algoritmo de chave de host pós-quântico se torna uma mudança de AC.

### Exercícios

- **EX013 — Priorizar.** Ordene os cinco itens de identidade da KLS do caso resolvido deste capítulo por prioridade de migração e justifique. Rubrica: 3 = ordem coerente com o tempo de vida e o controle.
- **EX014 — Repositórios de confiança.** Liste cinco repositórios de confiança que a KLS precisa atualizar para uma nova raiz interna. Rubrica: 3 = cinco repositórios plausíveis.

### Síntese

As assinaturas sustentam a autenticação no SSO, no mTLS, no SSH e na assinatura de código. A identidade pós-quântica começa pelas raízes internas e pela assinatura de longa duração, depois que os repositórios de confiança estiverem preparados.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 30

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) desenhar diagramas de serviços com fronteiras de confiança; (2) anotar os fluxos com algoritmos e tempos de vida dos dados; (3) explicar os pontos de terminação TLS e as suas consequências; e (4) descrever os recursos de agilidade criptográfica que um implementador pode construir.

### 8.1 Fronteiras e terminação

O tráfego atravessa fronteiras — da internet para a borda, da borda para a malha de serviços, do serviço para o banco de dados, do escritório para a nuvem. O TLS muitas vezes é terminado e restabelecido a cada salto: CDN, balanceador de carga, ingress, sidecar. Cada terminação é uma negociação separada, com a sua própria escolha de algoritmo; um grupo híbrido na CDN não diz nada sobre o salto da CDN até a origem.

A KLS conta cinco terminações TLS só no caminho do cliente, e cada uma tem um dono diferente. Por isso, o diagrama precisa mostrar cada terminação com o seu controlador, porque cada dono configura e muda o seu próprio salto no seu próprio calendário.

### 8.2 Diagramas anotados

Anote cada fluxo com protocolo, troca de chaves, autenticação, tempo de vida dos dados e quem controla cada ponta. O diagrama anotado é o mapa do implementador: os fluxos com dados de vida longa, troca de chaves clássica e um caminho não confiável são os primeiros a mudar.

A KLS usa uma linha por fluxo: `CDN→origin LB | TLS 1.3 | ECDHE X25519 | ECDSA P-256 | 10 y | KLS+CDN`. É listar o tempo de vida dos dados na linha que faz o salto da CDN até a origem se destacar: o mesmo protocolo do salto do navegador, mas clássico, e transportando os mesmos dados de embarque de dez anos por redes que a KLS não controla.

### 8.3 Recursos de agilidade

Os implementadores constroem agilidade: configurando os algoritmos num só lugar (perfis TLS centrais, anotações do ingress, políticas criptográficas); mantendo os identificadores de algoritmo nos dados armazenados; usando bibliotecas que suportam vários algoritmos; deixando espaço nos campos e buffers para chaves maiores; e testando no CI cada algoritmo configurado. O [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) do NIST discute essas considerações.

Na KLS, cada recurso tem um teste. O perfil central é renderizado no CI e comparado com o aprovado. As assinaturas armazenadas trazem um identificador de algoritmo, para que os verificadores possam aceitar dois algoritmos durante a transição. As colunas de chaves do banco de dados são dimensionadas para o ML-DSA-87. Um job do pipeline tenta um handshake com cada grupo configurado contra a homologação, para que um grupo listado mas não suportado falhe antes da implantação, e não depois.

### 8.4 Caso resolvido

O caminho do cliente da KLS: navegador → CDN (híbrido) → balanceador de carga da origem (clássico) → ingress (clássico) → pods da API (texto claro dentro da malha, com sidecars mTLS, ECDHE). O salto da internet está protegido; o salto da CDN até a origem atravessa a rede do provedor e a internet e transporta dados de dez anos. Prioridade: habilitar o híbrido no balanceador de carga da origem e no ingress; depois, avaliar a malha.

O plano coloca as primeiras mudanças onde a KLS controla as duas pontas e os dados têm vida longa. O balanceador de carga da origem e o ingress são configuração da KLS; as configurações de origem da CDN são uma opção do provedor que a KLS pode habilitar. A malha fica para avaliação porque os seus saltos permanecem dentro da rede de um único provedor e os seus sidecars são atualizados no calendário de versões da plataforma.

### 8.5 Atividade prática

Desenhe e anote o caminho dos fluxos do SFTP dos parceiros e da VPN do escritório da KLS; marque os pontos de terminação.

Para o SFTP dos parceiros, o caminho é curto: cliente do parceiro → internet → bastion da KLS → host SFTP, com o SSH terminando uma única vez, no bastion ou no host, dependendo do projeto. Para a VPN do escritório, mostre o appliance do escritório, a internet, o gateway de VPN na nuvem e o salto interno até os serviços, observando que o IPsec termina no gateway e o tráfego continua pela malha. Dê a cada salto as mesmas cinco anotações da regra de diagramas acima. Marque como desconhecido qualquer salto em que você não tenha encontrado o algoritmo.

### 8.6 Erros comuns e limites

- Julgar o caminho inteiro pelo primeiro salto.
- Fixar suítes de cifras no código em muitos lugares.
- Diagramas sem tempos de vida dos dados.

A KLS cometeu os três. O relatório inicial "o caminho do cliente é híbrido" julgou o caminho pelo salto do navegador até a CDN. As listas de cifras estavam fixadas no ingress, em dois balanceadores de carga e num modelo de sidecar, então mudá-las exigia quatro revisões e um local esquecido. E os primeiros diagramas mostravam os algoritmos, mas não os tempos de vida, o que fazia os fluxos de telemetria e de embarque parecerem igualmente urgentes. O limite dos diagramas é que eles são desenhados à mão; os traces do Capítulo 12 os transformam em dados.

### 8.7 Checklist de revisão

Ao revisar o projeto de um novo serviço, pergunte: quais saltos terminam o TLS, e quem configura cada um; quais grupos e algoritmos de assinatura cada salto oferece e prefere; onde as escolhas de algoritmo são configuradas; quais dados armazenados trazem identificadores de algoritmo; e se algum campo, buffer ou limite de mensagem supõe tamanhos clássicos. Cinco perguntas feitas no momento do projeto evitam a maior parte do retrabalho que os inventários descobrem depois.

A KLS acrescenta as cinco perguntas ao seu modelo de revisão de projeto. No primeiro trimestre, elas sinalizaram um novo serviço de relatórios que guardava assinaturas numa coluna de 256 bytes e uma nova fila cuja biblioteca cliente fixava grupos clássicos.

### Exercícios

- **EX015 — Terminação.** Explique por que uma borda de CDN híbrida não protege o salto da CDN até a origem. Rubrica: 3 = sessões TLS e negociações separadas.
- **EX016 — Recurso de agilidade.** Descreva um recurso de agilidade que você poderia acrescentar à configuração do ingress da KLS. Rubrica: 3 = perfil central ou anotação, com teste.

### Síntese

Os diagramas anotados revelam cada ponto de terminação como uma negociação separada; os recursos de agilidade permitem que os implementadores mudem todos eles a partir de um só lugar.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 30

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher fontes válidas para cada fato criptográfico; (2) declarar a cobertura e os denominadores; (3) projetar métricas de prontidão para as equipes de implementação; e (4) apresentar as medições com os pontos cegos.

### 9.1 Fontes por fato

O grupo TLS negociado é visível no ServerHello e nos logs do servidor; no TLS 1.3, o certificado é cifrado, então os algoritmos dos certificados vêm da configuração ou da inspeção do endpoint. A troca de chaves do SSH aparece nos logs do daemon em níveis detalhados. A negociação da VPN aparece nos logs do appliance. Associe cada fato à fonte que consegue de fato vê-lo.

A KLS aprendeu isso quando um sensor passivo reportou ECDSA para um serviço cujo certificado ele não conseguia ver; o valor tinha sido inferido, não observado. Cada fato agora traz a classe de fonte que pode legitimamente vê-lo, e os valores inferidos são rotulados.

### 9.2 Cobertura e denominadores

"80 % híbrido" precisa de um denominador (conexões? serviços? serviços de nível 1?) e de uma cobertura (quais sensores, quais locais). Os implementadores devem reportar: os serviços com o híbrido habilitado (configuração), a fração de conexões que negociam o híbrido (logs) e a fração de serviços sem nenhuma evidência.

O painel da KLS usa três números por fluxo: listeners com o híbrido configurado, divididos pelos listeners do inventário; handshakes que negociam o híbrido, divididos pelos handshakes registrados; e serviços sem fonte, divididos pelos serviços de nível 1. Cada número nomeia os seus sensores e a janela de tempo. Um leitor pode então ver que 96 % dos handshakes de navegadores e 0 % das sessões SFTP são híbridos, em vez de um único número misturado que esconde a lacuna do SFTP.

### 9.3 Métricas da equipe

Métricas úteis para os implementadores: a fração dos serviços de nível 1 que oferecem e preferem o híbrido; a fração das imagens construídas sobre camadas base aprovadas; o tempo entre a mudança aprovada e a implantação; o número de listeners apenas clássicos em endereços voltados para a internet; a taxa de handshakes com falha, por causa.

Cada métrica dispara uma ação específica na KLS. Um serviço de nível 1 que oferece mas não prefere o híbrido recebe um chamado de configuração; uma imagem fora da base aprovada recebe uma reconstrução; um tempo de implantação crescente leva a examinar o processo de mudança; qualquer novo listener apenas clássico na internet é revisado em uma semana; e um aumento das falhas por uma causa, como ClientHellos grandes, abre um caso com o fornecedor.

### 9.4 Caso resolvido

O primeiro painel da KLS mostrava "conexões híbridas: 71 %". Detalhamento: tráfego de navegadores para a CDN 96 % híbrido (logs da CDN, cobertura total); tráfego do SDK da API 40 % (logs do gateway); SFTP dos parceiros 0 % (logs do daemon); VPN do escritório 0 % (configuração); leitores desconhecido. O número único media sobretudo os navegadores.

O detalhamento também mostrou o que cada equipe precisava fazer. O tráfego da CDN não precisava de nada. O tráfego do SDK precisava que os clientes atualizassem, então a KLS publicou versões do SDK que enviam o key share híbrido por padrão. O SFTP e a VPN precisavam de trabalho de configuração e de appliance. Os leitores precisavam de uma fonte de dados antes que qualquer meta pudesse ser definida. O número único não tinha sugerido nada disso; o detalhamento produziu quatro chamados e um pedido ao fornecedor.

### 9.5 Atividade prática

Projete três métricas com definição, fonte, denominador, cobertura e dono.

Para cada métrica, escreva a definição numa frase, a fonte dos dados e a sua consulta, o denominador, a cobertura (quais locais, sensores e janela de tempo), o dono e a ação tomada quando o valor se move. Exemplo: "Fração das sessões SFTP dos parceiros que negociam `mlkem768x25519-sha256`, a partir dos logs do sshd nos dois hosts SFTP, denominador todas as sessões concluídas nos últimos 7 dias, dono Platform Team; abaixo de 50 % depois da data do aviso, dispara um contato com os parceiros." Acrescente ao lado uma métrica de "desconhecidos", contando os parceiros sem nenhuma sessão na janela.

### 9.6 Erros comuns e limites

- Percentuais únicos de manchete.
- Afirmar fatos sobre certificados a partir de capturas passivas de TLS 1.3.
- Métricas sem dono.

Na KLS, os 71 % da manchete vieram da mistura de tipos de tráfego; o rótulo "ECDSA" do sensor passivo veio de uma captura TLS 1.3 em que o certificado estava cifrado, então não podia ter sido observado; e a métrica de cobertura do scanner não tinha dono, então, quando o scanner quebrou, ninguém percebeu que o número congelou. O limite dos métodos deste capítulo é que eles medem a configuração e a negociação, não se o tráfego gravado já existe no arquivo de um adversário.

### 9.7 Medição como código

Mantenha as definições das métricas no controle de versão, ao lado dos scripts que as calculam. Quando alguém perguntar por que a fração híbrida mudou de 62 % para 58 %, você pode mostrar se mudou o parque ou a definição — por exemplo, um novo sensor que acrescentou ao denominador o tráfego do escritório antes invisível. Uma mudança de cobertura deve ser anotada no painel, porque um número que cai por causa de uma visibilidade melhor é progresso, não regressão.

Publique também uma métrica de "desconhecidos" ao lado de cada métrica de cobertura: o número de serviços de nível 1 para os quais nenhuma fonte reporta hoje o fato relevante. As equipes que veem a sua contagem de desconhecidos toda semana tendem a corrigir as alimentações que a reduziriam, e é assim que a cobertura da medição melhora sem um projeto separado.

### Exercícios

- **EX017 — Reescrever.** Reescreva "71 % híbrido" como três afirmações com escopo. Rubrica: 3 = escopo por fluxo, com fontes.
- **EX018 — Associar fontes.** Nomeie a melhor fonte para: o grupo TLS negociado, o algoritmo do certificado do servidor, a KEX do SSH, a troca de chaves da VPN. Rubrica: 3 = quatro fontes corretas.

### Síntese

As medições são tão boas quanto as suas fontes, os seus denominadores e a sua cobertura; os implementadores reportam números com escopo e com os pontos cegos visíveis.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 30

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Segurança quântica e pós-quântica: orientação

### Objetivos de aprendizagem

Você vai (1) resumir as normas pós-quânticas do NIST e a sua situação; (2) explicar o LWE com um laboratório de brinquedo; (3) descrever a interface e os conjuntos de parâmetros do ML-KEM; e (4) dizer o que os implementadores devem e não devem fazer com a PQC.

### 10.1 Normas

O NIST publicou a [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) (ML-KEM), a [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) (ML-DSA) e a [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (SLH-DSA) em agosto de 2024; a [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) trata do LMS e do XMSS; a [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) dá recomendações sobre KEMs. O rascunho [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) do NIST propõe tornar obsoletos os algoritmos vulneráveis ao quântico após 2030 e proibi-los após 2035. O FN-DSA e um KEM baseado no HQC estavam em desenvolvimento.

Para os implementadores da KLS, a leitura prática é: ML-KEM para o estabelecimento de chaves desde já, ML-DSA para as assinaturas conforme as ferramentas permitirem, assinaturas baseadas em hash para o firmware, e as datas do rascunho IR 8547 como premissas de planejamento até a versão final.

### 10.2 A ideia por baixo do ML-KEM

O Learning With Errors (Regev, 2009) esconde um segredo em equações lineares com ruído.

```python
# Lab W (ch 10): a TOY Regev-style LWE encryption of one bit. Deliberately insecure parameters.
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

O brinquedo usa 16 dimensões e é trivialmente quebrável; o ML-KEM usa reticulados de módulo estruturados, com polinômios de 256 coeficientes, e uma transformação que protege contra ataques de texto cifrado escolhido.

O desenho do laboratório torna visível a regra de decifragem. O valor `v` do texto cifrado transporta o bit como 0 ou q/2, cerca de 1.664, mais o ruído acumulado da soma de até 64 pequenos erros escolhidos em {−2,…,2}. A decifragem subtrai `u·s` e pergunta se o resto está mais perto de 0 ou de q/2. Como o ruído fica muito abaixo de q/4, todos os 2.000 bits são decifrados corretamente. Faixas de erro maiores ou mais linhas somadas empurrariam o ruído para além desse limite e a decifragem começaria a falhar, o mesmo compromisso que os parâmetros do ML-KEM são escolhidos para administrar.

### 10.3 Interface e parâmetros

O ML-KEM é um KEM: KeyGen → (chave de encapsulamento, chave de desencapsulamento); Encaps(ek) → (texto cifrado, segredo compartilhado de 32 bytes); Decaps(dk, ct) → segredo compartilhado. O ML-KEM-512/768/1024 visa as categorias 1/3/5 do NIST, com chaves de encapsulamento de 800/1.184/1.568 bytes e textos cifrados de 768/1.088/1.568 bytes. O X25519MLKEM768 no TLS usa o ML-KEM-768.

Para os implementadores, a interface importa mais do que a matemática. O cliente gera um par de chaves e envia a chave de encapsulamento; o servidor encapsula e devolve o texto cifrado; os dois obtêm o mesmo segredo de 32 bytes. Não há etapa de cifragem de mensagens, então o ML-KEM é sempre combinado com uma cifra simétrica.

### 10.4 Regras para implementadores

Use bibliotecas verificadas e provedores da plataforma; nunca escreva a sua própria. Mantenha as bibliotecas atualizadas (o KyberSlash mostrou vazamentos de tempo em algumas implementações; Bernstein et al., 2024). Prefira híbridos durante a transição. Verifique os comprimentos e trate os erros sem vazar detalhes. Registre o algoritmo e as versões das bibliotecas no inventário.

Na KLS, essas regras viram perguntas de revisão em todo pull request que mexe com criptografia: qual biblioteca e versão, se ela está na lista aprovada, se o conjunto de parâmetros é explícito e o que acontece com entradas malformadas. Um pull request que responde "nós mesmos escrevemos" é fechado sem mais revisão.

### 10.5 Caso resolvido

Um desenvolvedor da KLS propõe um ML-KEM caseiro em Python "para os leitores". Resposta: rejeitado — a biblioteca padrão não tem o ML-KEM, o código de brinquedo é inseguro, e a imagem do fornecedor ou uma biblioteca verificada é o único caminho aceitável; enquanto isso, os fluxos de dados dos leitores são minimizados.

A etapa de minimização é concreta: os leitores enviam os manifestos num único lote diário, em vez de a cada leitura, o que reduz o volume de sessões que podem ser colhidas enquanto a imagem do fornecedor está pendente. A rejeição e o controle provisório são ambos registrados na linha do leitor no inventário, com o número do chamado do fornecedor.

### 10.6 Erros comuns e limites

- Tratar o laboratório de brinquedo como utilizável.
- Usar o ML-KEM como se ele cifrasse mensagens arbitrárias.
- Ignorar os avisos de atualização das bibliotecas.

Cada erro tem um sintoma reconhecível. Alguém que cola o código de 16 dimensões do Laboratório W num serviço, acreditando que é "criptografia de reticulados", entregou algo que se quebra em segundos. Alguém que chama o ML-KEM para "cifrar o manifesto" leu errado a interface: ele só produz um segredo compartilhado para uma cifra simétrica. E uma equipe que ignora avisos como o KyberSlash mantém um vazamento de tempo que uma atualização de biblioteca teria removido. A orientação aqui é propositalmente rasa; a autoridade são as próprias normas.

### 10.7 Assinaturas em um parágrafo

O ML-DSA (FIPS 204) é a assinatura de reticulados de uso geral, com assinaturas ML-DSA-44/65/87 de 2.420/3.309/4.627 bytes. O SLH-DSA (FIPS 205) depende apenas de funções de hash; as suas chaves públicas são minúsculas, mas as suas assinaturas vão de 7.856 a 49.856 bytes. O LMS e o XMSS (SP 800-208) são assinaturas compactas baseadas em hash que exigem que o signatário acompanhe o estado e nunca reutilize um índice. Os implementadores vão encontrar o ML-DSA primeiro nos certificados e na assinatura de código, e os esquemas baseados em hash na assinatura de firmware.

Para a KLS, isso significa ML-DSA para a AC interna e a assinatura de versões, e LMS para o firmware dos leitores somente se o HSM do fornecedor gerenciar o estado.

### Exercícios

- **EX019 — Tamanhos.** Dê os tamanhos da chave de encapsulamento e do texto cifrado do ML-KEM-768 e o comprimento do segredo compartilhado. Rubrica: 3 = 1.184, 1.088 e 32 bytes.
- **EX020 — Regras.** Liste quatro regras para implementadores de PQC. Rubrica: 3 = bibliotecas verificadas, atualizações, híbridos, tratamento de comprimentos/erros.

### Síntese

As normas do NIST definem as substituições; o ML-KEM é um KEM sobre reticulados de módulo, com três conjuntos de parâmetros. Os implementadores configuram implementações verificadas, nunca constroem as suas próprias.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 30

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (inglês) →](../../en/book/MANUSCRIPT.md#ch-11)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre a KLS são sintéticos. Esta edição parcial traz as resoluções de EX001–EX020; as de EX021–EX060 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

**EX001.** Hardware: appliances de balanceamento de carga/hosts na nuvem (provedor). Firmware: inicialização assinada dos hosts (provedor/fornecedor; troca de hardware). Sistema operacional: distribuição dos nós com OpenSSL (equipe de plataforma; atualização de pacote). Biblioteca: TLS da imagem do ingress/NGINX (equipe de plataforma; reconstrução da imagem). Aplicação: cookies de sessão do portal assinados/cifrados (equipe da aplicação; versão). Gerenciado: TLS da borda da CDN (provedor da CDN; configuração).

**EX002.** Assinaturas RSA-2048: substituir (Shor). AES-256-GCM: manter (Grover deixa um trabalho de ~128 bits). SHA-256: manter (adequado para colisão/pré-imagem nos tamanhos atuais). ECDHE P-256: substituir (Shor; HNDL).

**EX003.** TLS 1.3: grupo X25519MLKEM768, RFC 10024. SSH: troca de chaves `mlkem768x25519-sha256`, notas de versão do OpenSSH. IKEv2: trocas de chaves adicionais, RFC 9370 (mistura provisória de PSK, RFC 8784).

**EX004.** 1.120 − 32 = 1.088 bytes, que é exatamente o texto cifrado do ML-KEM-768 (FIPS 203).

**EX005.** ceil(3.309 / 3) = 1.103 grupos × 4 = 4.412 caracteres.

**EX006.** O `==` pode retornar assim que um byte difere, então o tempo de resposta vaza quantos bytes iniciais coincidem, o que permite adivinhar a tag; use `hmac.compare_digest`.

**EX007.** `use_id` (qual uso criptográfico); `method` (passivo, configuração, código, fornecedor); `observed_at` (data e hora); `observer` (ferramenta ou pessoa); `evidence_ref` (ponteiro para o log bruto/hash da configuração); opcionalmente `grade`.

**EX008.** `SELECT service FROM certs WHERE function='signature' AND algorithm IN ('RSA','ECDSA') AND not_after > '2030-12-31';`

**EX009.** Tráfego da VPN do escritório: HNDL (se os dados forem de vida longa). Chave de assinatura de código do CI: forjar depois (artefatos confiáveis por anos). Backups em AES-256: nenhum (adequado frente a Grover). TLS para o portal do cliente: HNDL para os dados da sessão; forjar depois para o seu certificado.

**EX010.** Um middlebox descarta o ClientHello de vários segmentos → implantação em etapas e atualização/contorno do proxy. Um servidor apenas híbrido rejeita os clientes clássicos → manter o recuo clássico durante a transição. (Também: latência do HRR, CPU em clientes com recursos limitados.)

**EX011.** Contêiner NGINX: reconstruir a imagem sobre uma base com um OpenSSL com suporte a PQ e definir os grupos. Serviço Go: atualizar o toolchain do Go e recompilar, configurando as preferências de curvas se necessário. Daemon SSH do host: atualizar o pacote do OpenSSH e definir o `KexAlgorithms`.

**EX012.** Uma etapa de CI lê o SBOM da imagem e reprova se o OpenSSL for anterior ao mínimo aprovado (por exemplo, 3.5) nos serviços de nível 1; as exceções exigem um chamado com dono e data de expiração.

**EX013.** 1) AC raiz interna (confiança de 15 anos, controlada pela KLS). 2) Assinatura de versões (artefatos verificados por anos). 3) Certificados finais de mTLS dos serviços (depois da raiz). 4) Chaves SSH de usuário (rotacionáveis; adotar certificados). 5) Tokens de SSO (tempo de vida de 1 hora, rotação rápida).

**EX014.** Repositórios de confiança do sistema operacional dos hosts; pacotes de ACs das imagens base dos contêineres; truststores Java nos serviços; pacotes de confiança dos sidecars da malha; agentes de monitoramento; sistemas dos parceiros que usam mTLS; runners de CI.

**EX015.** A CDN termina o TLS do cliente e abre uma nova sessão TLS até a origem; cada negociação é independente, então os algoritmos do salto até a origem dependem das configurações de origem da CDN e da configuração da origem.

**EX016.** Referenciar um perfil nomeado (por exemplo, a anotação `tls-profile: kls-modern`) resolvido de forma central, com um teste de CI que confirme que os grupos renderizados coincidem com o perfil.

**EX017.** "Tráfego de navegadores para a CDN: 96 % híbrido (logs da CDN, todas as bordas)." "Tráfego do SDK da API no gateway: 40 % híbrido (logs do gateway)." "SFTP dos parceiros e VPN do escritório: 0 % (logs do daemon, configuração); leitores: desconhecido (sem fonte)."

**EX018.** Grupo TLS: ServerHello/logs do servidor. Algoritmo do certificado do servidor: configuração do servidor ou inventário de certificados. KEX do SSH: logs do sshd (com o nível de log adequado). Troca de chaves da VPN: logs/configuração do appliance.

**EX019.** Chave de encapsulamento de 1.184 bytes, texto cifrado de 1.088 bytes, segredo compartilhado de 32 bytes.

**EX020.** Usar bibliotecas/provedores verificados; mantê-los atualizados; preferir híbridos durante a transição; validar os comprimentos e tratar os erros sem vazar detalhes.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; a situação das normas muda, então verifique de novo.

- Bernstein, D. J., et al. (2024). KyberSlash. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *STOC '96*. <https://doi.org/10.1145/237814.237866>
- IETF RFCs: 8446 (TLS 1.3), 8555 (ACME), 8784 (IKEv2 PSK mixing), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- OpenSSH release notes. <https://www.openssh.com/releasenotes.html>
- OpenSSL 3.5 NEWS. <https://github.com/openssl/openssl/blob/openssl-3.5/NEWS.md>
- Regev, O. (2009). *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
