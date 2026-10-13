# Segurança Quântica e Pós-Quântica: Operações Práticas para Equipes Técnicas

- Idioma: português do Brasil (`pt`); curso técnico, 18 meses; aproximadamente 1.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–9 de 18 já estão escritos em português, com os exercícios EX001–EX027 e suas resoluções; os capítulos 10–18 (EX028–EX054) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: operadores técnicos — engenheiros de service desk, operadores de sistemas e de redes, administradores júnior — que precisam verificar, configurar, diagnosticar e confirmar configurações pós-quânticas em serviços reais, sob supervisão. Conhecimento de entrada: redes, sistemas operacionais, scripts e prática segura de laboratório.
- Relação com os livros vizinhos: o [livro de tecnólogo](../../../../technologist-3-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) trata de integração e automação com mais profundidade; o [livro profissional](../../../../professional-6-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) trata da governança da migração. **Este livro é prático**: comandos, verificações, logs, mudanças de configuração, verificação e trabalho seguro em laboratório.
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação credenciada. Não concede autorização para testar sistemas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública. Os exemplos de comandos e de configuração são ilustrativos; consulte a documentação atual do seu produto. Sistemas de produção devem usar implementações verificadas da [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), da [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) e da [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205).

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Dezoito capítulos se distribuem por 18 meses: fundamentos técnicos (1–5), operações pós-quânticas (6–11), laboratório I (12), diagnóstico, automação e integração (13–15), documentação e segurança (16), laboratório II (17) e um projeto supervisionado (18). Cada capítulo tem objetivos de aprendizagem, ensino, um caso resolvido, uma atividade prática, erros comuns, três exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com Python 3; a saída impressa é mostrada para que você possa conferir a sua execução.

### O caso contínuo: Halden Hotel Group

O **Halden Hotel Group (HHG)** é uma rede sintética de 12 hotéis. Cada unidade opera um sistema de gestão hoteleira (PMS), terminais de ponto de venda, fechaduras eletrônicas, Wi-Fi para hóspedes e uma VPN de site até o data center central, que hospeda a API de reservas, o portal do hóspede, o banco de dados de reservas e um serviço de troca de arquivos para os canais de agências de viagem. Os registros de hóspedes com dados de passaporte precisam permanecer confidenciais por sete anos. Você trabalha na equipe de operações do HHG. Todos os números sobre o HHG são inventados.

### Política de fontes

As fontes primárias foram verificadas em 12 de outubro de 2026: NIST FIPS 203/204/205 (agosto de 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (rascunho público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) e [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). O FN-DSA (FIPS 206) e a norma do HQC ainda estavam em desenvolvimento. Verifique a situação de novo antes de se apoiar nela.

## Sumário

| Etapa | Capítulos |
|---|---|
| Fundamentos | [1 Arquitetura de computação e de serviços](#ch-01) · [2 Redes e protocolos](#ch-02) · [3 Sistemas operacionais e identidades](#ch-03) · [4 Scripts e formatos de dados](#ch-04) · [5 Escopo de segurança e evidências](#ch-05) |
| Operações PQC | [6 Modelo do sistema](#ch-06) · [7 Dados e telemetria](#ch-07) · [8 Modos de falha](#ch-08) · [9 Ferramentas e métodos](#ch-09) · [10 Configuração de controles](#ch-10) · [11 Verificação](#ch-11) · [12 Laboratório controlado I](#ch-12) |
| Prática de operações | [13 Diagnóstico de problemas](#ch-13) · [14 Automação](#ch-14) · [15 Integração e dependências](#ch-15) · [16 Documentação técnica e segurança](#ch-16) · [17 Laboratório controlado II](#ch-17) · [18 Projeto técnico supervisionado](#ch-18) |

Capítulos 10–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-10), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Arquitetura de computação e de serviços

### Objetivos de aprendizagem

Você vai (1) descrever como os serviços de um hotel se encaixam, do dispositivo ao data center; (2) apontar onde a criptografia e as assinaturas são usadas; (3) explicar em termos simples o que os computadores quânticos ameaçam; e (4) distinguir as mudanças que você pode fazer por conta própria das que precisam de um fornecedor.

### 1.1 O mapa de serviços

Numa unidade do HHG, um PC da recepção roda o cliente do PMS, que fala pela VPN de site com o servidor do PMS no data center. Os pagamentos com cartão vão dos terminais de ponto de venda (POS) para uma processadora de pagamentos. As fechaduras são programadas por um servidor de fechaduras por meio de um hub. Os hóspedes usam o Wi-Fi para chegar à internet e ao portal do hóspede. No data center, um balanceador de carga fica na frente da API de reservas e do portal; os servidores falam com o banco de dados de reservas; um servidor de troca de arquivos envia arquivos de reservas às agências de viagem. Desenhar esse mapa é a primeira tarefa de qualquer operador, porque toda verificação posterior se refere a uma caixa ou a uma seta dele.

### 1.2 Onde a criptografia é usada

A cifragem protege os dados que trafegam entre as caixas (TLS, VPNs, SSH) e os dados armazenados (cifragem de disco e de banco de dados). As assinaturas provam quem é quem (certificados nos servidores, atualizações de software assinadas, firmware de fechadura assinado). Cada uso tem um *responsável* e uma *rota de mudança*: uma configuração que você pode alterar, um pacote que você pode atualizar, uma atualização do fornecedor ou uma troca de hardware.

No HHG, o TLS do portal do hóspede pode ser mudado pelas operações por meio de configuração, enquanto o firmware assinado das fechaduras só pode mudar com o fornecedor das fechaduras ou com hardware novo. Escreva a rota de mudança ao lado de cada uso que encontrar, já que ela decide quem precisa agir e quanto tempo isso vai levar.

### 1.3 O que os computadores quânticos ameaçam

Um computador quântico grande e com correção de erros, executando o algoritmo de Shor (Shor, 1997), poderia quebrar os métodos de chave pública usados hoje para acordar chaves e assinar — RSA e curvas elípticas. Ele não quebraria de forma significativa a cifragem AES-256 nem o hash SHA-256. Nenhuma máquina desse tipo existe ainda. Daí decorrem dois riscos: alguém poderia *gravar* tráfego cifrado agora e decifrá-lo depois ("colher agora, decifrar depois"), e, quando essa máquina existir, alguém poderia *forjar* assinaturas. O NIST publicou algoritmos substitutos: o ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)) para o acordo de chaves e o ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) e o SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) para assinaturas.

### 1.4 Caso resolvido

O operador lista os usos criptográficos na unidade Harbour: cliente do PMS para o servidor pela VPN de site (troca de chaves ECDH; rota de mudança: firmware do appliance de VPN, fornecedor); POS para a processadora de pagamentos (TLS; processadora e fornecedor do POS); firmware das fechaduras assinado com RSA (fornecedor das fechaduras; renovação de hardware); TLS do portal do hóspede no balanceador de carga (operações do HHG; configuração). Só o último é uma mudança que a equipe de operações pode fazer hoje.

A lista deixa a lacuna clara: a maior parte da criptografia da unidade depende de fornecedores ou de hardware. Isso não significa que nada possa ser feito; significa que a outra tarefa do operador é registrar perguntas precisas aos fornecedores sobre os itens de VPN, POS e fechaduras, com modelo e versões de firmware.

### 1.5 Atividade prática

Desenhe o mapa de serviços de uma unidade a partir da descrição acima. Para cada seta, escreva: protocolo, responsável, rota de mudança.

Inclua as caixas menos visíveis: os terminais POS, o hub das fechaduras e o Wi-Fi dos hóspedes. Para cada seta, nomeie o protocolo (TLS, IPsec, SSH ou desconhecido), quem é responsável por cada ponta e se uma mudança é uma configuração, uma atualização, uma atualização do fornecedor ou uma troca de hardware. Marque como desconhecida qualquer seta que você não consiga preencher, em vez de adivinhar. Compare o seu mapa com o de um colega e resolva as diferenças; as divergências costumam revelar uma caixa que um de vocês esqueceu.

### 1.6 Erros comuns e limites

- Esquecer dispositivos como fechaduras e terminais POS.
- Supor que toda mudança é uma configuração.
- Dizer que os computadores quânticos "quebram toda a cifragem".

Cada erro torna o mapa enganoso. Fechaduras e terminais POS são fáceis de esquecer porque ninguém faz login neles, mas o firmware das fechaduras é um dos pontos de confiança mais longevos do HHG. Supor que toda mudança é uma configuração faz os planos parecerem mais rápidos do que são, porque as rotas de firmware e de hardware levam meses ou anos. Dizer que os computadores quânticos quebram toda a cifragem está errado: o AES-256 e o SHA-256 continuam adequados, e dizer o contrário desvia o esforço para os lugares errados.

### Exercícios

- **EX001 — Rotas de mudança.** Para cinco usos criptográficos do HHG, informe a rota de mudança. Rubrica: 3 = cinco rotas corretas.
- **EX002 — Explicação simples.** Explique "colher agora, decifrar depois" a um gerente de hotel em duas frases. Rubrica: 3 = correta e sem jargão.
- **EX003 — Manter ou substituir.** Quais entre RSA, AES-256, ECDH e SHA-256 precisam ser substituídos? Rubrica: 3 = RSA e ECDH substituídos; AES-256 e SHA-256 mantidos, com os motivos.

### Síntese

Um mapa de serviços claro mostra onde a criptografia é usada, quem é responsável por ela e como ela pode mudar. Os computadores quânticos ameaçam o acordo de chaves e as assinaturas de chave pública, não a cifragem simétrica.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 18

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar TLS, SSH e IPsec no nível necessário para verificá-los; (2) identificar as partes de troca de chaves e de autenticação de cada um; (3) ler qual grupo de troca de chaves uma conexão TLS usou; e (4) explicar por que os handshakes pós-quânticos são maiores.

### 2.1 Três canais seguros

O TLS protege o tráfego web e de APIs; o SSH protege os logins de administradores e as transferências de arquivos (SFTP); o IPsec protege as VPNs entre sites. Cada um primeiro acorda uma chave de sessão (troca de chaves) e prova a identidade (certificados, chaves de host ou chaves pré-compartilhadas), e depois cifra os dados com uma cifra simétrica.

Para cada canal, faça duas perguntas: como a chave é acordada e como a identidade é provada? O trabalho pós-quântico muda a primeira parte com a troca de chaves híbrida e, mais tarde, a segunda com novos certificados ou chaves. No HHG, as VPNs de site usam IPsec, a troca de arquivos dos canais usa SFTP e o portal do hóspede usa TLS.

### 2.2 Troca de chaves híbrida

O projeto de transição combina um método pós-quântico e um clássico, de modo que ambos teriam de ser quebrados — o que se chama *híbrido* ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)). No TLS 1.3, o grupo híbrido X25519MLKEM768 é definido na [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). No SSH, o OpenSSH oferece `mlkem768x25519-sha256` ([notas de versão do OpenSSH](https://www.openssh.com/releasenotes.html)). No IPsec, a [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html) acrescenta trocas de chaves extras, como o ML-KEM.

Consulte a documentação do produto para saber o nome que ele usa.

### 2.3 Lendo o grupo negociado

Numa máquina de laboratório com um OpenSSL atual, `openssl s_client -connect lab-server:443 -groups X25519MLKEM768:X25519` imprime detalhes do handshake, incluindo o grupo negociado nas versões recentes. Os logs do servidor podem registrar o grupo, se configurados para isso. No SSH, `ssh -v` imprime o algoritmo de troca de chaves escolhido ("kex: algorithm: …"). Execute esses comandos apenas contra sistemas que você está autorizado a testar.

Salve a saída com a data e a versão do cliente, já que um cliente antigo não consegue mostrar um grupo híbrido mesmo quando o servidor o oferece. No portal do hóspede de homologação do HHG, foi assim que o problema de ordem dos grupos do Capítulo 5 foi visto pela primeira vez.

### 2.4 Handshakes maiores

O compartilhamento de chave TLS do cliente cresce de 32 bytes (X25519) para 1.216 bytes (X25519MLKEM768), de modo que a primeira mensagem muitas vezes já não cabe num único pacote de rede. A maioria das redes lida com isso; alguns firewalls antigos não. As assinaturas pós-quânticas acrescentam mais quando os certificados mudam: uma assinatura ML-DSA-44 tem 2.420 bytes.

Para os operadores, o efeito prático é que um handshake híbrido pode falhar num caminho de rede e funcionar nos outros. Quando você vir timeouts apenas através de um firewall ou proxy, pense no tamanho da mensagem antes de culpar o algoritmo. Anote o modelo e o firmware do dispositivo, como fez o operador do HHG na unidade Summit.

### 2.5 Caso resolvido

Um operador do HHG se conecta do laboratório ao portal do hóspede de homologação com um cliente atual e vê o grupo híbrido negociado. Com um cliente mais antigo, a conexão é bem-sucedida com X25519 — o fallback esperado. Através da cópia de laboratório do firewall antigo da unidade Summit, a conexão expira por timeout; o operador registra o modelo e o firmware do firewall para acompanhamento.

Os três resultados significam coisas diferentes: o resultado híbrido mostra que o servidor funciona, o fallback mostra que os clientes mais antigos continuam sendo atendidos e o timeout aponta para o caminho de rede, não para o servidor. O operador não muda o portal; o firewall vira um item de acompanhamento.

### 2.6 Atividade prática

No seu laboratório, execute um cliente TLS contra um servidor de teste duas vezes — com e sem o grupo híbrido oferecido — e registre o grupo negociado em cada vez. Repita no SSH com `ssh -v`.

Registre, para cada execução, o comando, a versão do cliente, o alvo, o horário e o grupo negociado ou o algoritmo de troca de chaves. Depois explique em uma ou duas frases por que os resultados diferem. Se o seu cliente não conseguir mostrar o grupo, anote isso e use um cliente mais novo. Use apenas os seus próprios servidores de laboratório. Guarde os arquivos de saída com nomes datados, porque os capítulos seguintes pedem que você compare execuções e escreva constatações a partir delas.

### 2.7 Erros comuns e limites

- Achar que a troca de chaves híbrida muda os certificados.
- Testar sistemas sem autorização.
- Culpar o algoritmo por uma falha de firewall.

Cada erro leva a uma conclusão errada ou a um ato inseguro. A troca de chaves híbrida protege as chaves de sessão, mas o servidor continua provando a sua identidade com um certificado clássico. Testar sem autorização pode derrubar um serviço e custar à sua equipe o direito de testar. Um firewall que descarta mensagens grandes, como no Summit, é um problema de rede, e remover o híbrido para resolvê-lo deixaria todo o resto do tráfego desprotegido. Confira as suas anotações contra esses três antes de escrever uma constatação.

### Exercícios

- **EX004 — Duas partes.** Para TLS, SSH e IPsec, nomeie a parte de troca de chaves e a de identidade. Rubrica: 3 = seis entradas corretas.
- **EX005 — Ler a saída.** Uma linha de `ssh -v` diz `kex: algorithm: curve25519-sha256`. A sessão é híbrida? O que você verificaria em seguida? Rubrica: 3 = não é híbrida; verificar as listas de KEX/versões do servidor e do cliente.
- **EX006 — Tamanho.** Quanto maior é o compartilhamento do cliente no X25519MLKEM768 do que no X25519? Rubrica: 3 = 1.184 bytes.

### Síntese

TLS, SSH e IPsec acordam chaves e provam identidade. A troca de chaves híbrida está disponível nos três; os operadores leem os algoritmos negociados na saída dos clientes e nos logs.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 18

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem

Você vai (1) descobrir quais bibliotecas criptográficas um sistema usa; (2) verificar as versões que importam para o suporte pós-quântico; (3) explicar como funcionam os certificados e os repositórios de confiança num servidor; e (4) manusear chaves com segurança.

### 3.1 Bibliotecas e versões

A maioria dos serviços Linux usa o OpenSSL; o OpenSSL 3.5 acrescentou ML-KEM, ML-DSA e SLH-DSA e oferece X25519MLKEM768 por padrão no TLS ([OpenSSL 3.5 NEWS](https://github.com/openssl/openssl/blob/openssl-3.5/NEWS.md)). Verifique com `openssl version`. Os contêineres carregam as suas próprias bibliotecas, então verifique dentro deles também. Aplicações escritas em Go ou Java usam as suas próprias pilhas TLS; registre a versão do runtime. A versão do OpenSSH é mostrada por `ssh -V`.

Registre cada versão encontrada com a data e o comando usado. Anote os contêineres separadamente.

### 3.2 Certificados e repositórios de confiança

Um certificado de servidor é assinado por uma autoridade certificadora (AC). Os clientes confiam em certificados que se encadeiam até uma raiz no seu repositório de confiança. O sistema operacional tem um repositório de confiança; o Java e algumas aplicações têm o seu próprio. Os certificados pós-quânticos vão exigir que novas raízes sejam acrescentadas a todos os repositórios de confiança relevantes antes que os servidores os usem.

No HHG, o runtime Java do servidor do PMS tem o seu próprio repositório de confiança, então uma nova raiz precisaria ser acrescentada ali, além do sistema operacional. Liste todos os repositórios de confiança de um servidor antes de qualquer mudança de certificado e registre quem pode atualizar cada um.

### 3.3 Manuseando chaves

As chaves privadas devem ficar em arquivos protegidos, legíveis apenas pela conta de serviço, ou, melhor ainda, em módulos de hardware ou serviços de gerenciamento de chaves. Nunca cole chaves em tickets, chats ou logs. Se você encontrar uma chave privada exposta, pare e comunique pelo processo da sua organização; não a copie nem a teste.

Ao diagnosticar problemas, verifique permissões e caminhos em vez de ler o conteúdo das chaves. Se uma tarefa parecer exigir a própria chave, pare e pergunte ao seu supervisor, já que isso costuma ser sinal de que a tarefa foi mal formulada. Registre na sua evidência que as chaves não foram copiadas.

### 3.4 Caso resolvido

O operador verifica o servidor de troca de arquivos do HHG: `openssl version` mostra 3.0.x (sem ML-KEM); `ssh -V` mostra uma versão do OpenSSH anterior à que introduziu `mlkem768x25519-sha256`. Conclusão: são necessárias atualizações tanto do TLS quanto do SSH antes que a troca de chaves híbrida seja possível. O servidor do PMS roda uma aplicação Java com a sua própria pilha TLS; a versão do runtime entra no inventário para que o fornecedor confirme o suporte.

Anote a evidência por trás de cada conclusão: a saída dos comandos no servidor de troca de arquivos e a versão do runtime no servidor do PMS. O item do Java não pode ser resolvido apenas pelas operações do HHG, então vira uma pergunta ao fornecedor, com data.

### 3.5 Atividade prática

Numa VM de laboratório, registre as versões do OpenSSL e do OpenSSH, liste os repositórios de confiança presentes e verifique as permissões de um arquivo de chave privada de teste.

Escreva cada resultado com o comando e a sua saída, e anote quais versões suportam algoritmos pós-quânticos. Verifique as permissões com `ls -l` e confirme que apenas a conta de serviço consegue ler o arquivo da chave. Se houver um contêiner em execução, verifique dentro dele também. Não abra nem copie o arquivo da chave. Compare as suas constatações com o servidor de troca de arquivos do caso resolvido e diga quais atualizações a sua VM precisaria.

### 3.6 Erros comuns e limites

- Verificar o host e esquecer os contêineres.
- Acrescentar raízes apenas ao repositório do sistema operacional.
- Copiar chaves durante o diagnóstico.

Cada erro deixa uma lacuna. Os contêineres carregam as suas próprias bibliotecas, então uma atualização do host pode deixar o próprio serviço inalterado. Acrescentar uma nova raiz apenas ao repositório do sistema operacional quebra aplicações como o PMS do HHG, baseado em Java, que usam o seu próprio repositório. Copiar chaves durante o diagnóstico cria cópias que precisam ser encontradas e destruídas, e pode contar como incidente de segurança. Confira as suas anotações em relação a cada um antes de encerrar uma tarefa.

### 3.7 Contas de serviço e permissões

Os serviços devem rodar sob as suas próprias contas, com acesso apenas às suas próprias chaves e configuração. Quando você atualizar uma biblioteca para obter suporte pós-quântico, verifique se a atualização não redefiniu o dono ou as permissões dos arquivos de chave — os scripts dos pacotes às vezes fazem isso. Um `ls -l` rápido no diretório das chaves antes e depois da mudança, salvo com a sua evidência, mostra que nada foi afrouxado.

Guarde as listagens de antes e depois com o ticket de mudança. Se as permissões mudaram, restaure-as antes de fechar o ticket.

### Exercícios

- **EX007 — Verificação de versões.** Liste três comandos para estabelecer a prontidão pós-quântica do TLS e do SSH de um servidor Linux. Rubrica: 3 = `openssl version`, `ssh -V`, verificação de contêiner/runtime.
- **EX008 — Repositórios de confiança.** Nomeie três repositórios de confiança que podem precisar de uma nova raiz. Rubrica: 3 = sistema operacional, Java, pacote da aplicação/contêiner.
- **EX009 — Chave encontrada.** O que você faz se encontrar uma chave privada numa pasta compartilhada? Rubrica: 3 = parar, não copiar, comunicar pelo processo, documentar.

### Síntese

As versões das bibliotecas e dos runtimes determinam se os serviços podem usar algoritmos pós-quânticos; os certificados dependem de repositórios de confiança que precisam ser atualizados primeiro; as chaves são manuseadas com cuidado rigoroso.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 18

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem

Você vai (1) ler e escrever JSON e CSV em Python; (2) resumir exportações de inventário; (3) tratar valores ausentes como desconhecidos; e (4) escrever scripts que outras pessoas possam executar de novo.

### 4.1 Formatos

Os inventários chegam como JSON vindo de APIs e como CSV vindo de planilhas e scanners. Os módulos `json` e `csv` do Python leem ambos. Sempre verifique se os campos de que você precisa estão presentes e têm os tipos esperados.

No HHG, as exportações do scanner vêm em CSV e o inventário de endpoints em JSON. Confira a contagem de registros e os nomes dos campos antes de confiar em qualquer resumo. Se um campo estiver ausente ou tiver o tipo errado, pare e comunique, em vez de adivinhar.

### 4.2 Atividade prática — Laboratório J

```python
# Lab J (ch 4): parse a synthetic JSON export of TLS endpoints and summarise key exchange by property.
import json, collections
export = json.loads("""[
 {"property": "harbour", "host": "pms-01", "group": "X25519MLKEM768"},
 {"property": "harbour", "host": "pos-02", "group": "secp256r1"},
 {"property": "summit",  "host": "pms-01", "group": "X25519"},
 {"property": "summit",  "host": "lock-hub", "group": null},
 {"property": "lakeside","host": "pms-01", "group": "X25519MLKEM768"}]""")
summary = collections.defaultdict(collections.Counter)
for e in export:
    g = e["group"]
    kind = "unknown" if g is None else ("hybrid" if "MLKEM" in g else "classical")
    summary[e["property"]][kind] += 1
for prop, c in sorted(summary.items()):
    print(f"{prop:9s} hybrid={c['hybrid']} classical={c['classical']} unknown={c['unknown']}")
```

Saída esperada:

```text
harbour   hybrid=1 classical=1 unknown=0
lakeside  hybrid=1 classical=0 unknown=0
summit    hybrid=0 classical=1 unknown=1
```

O hub de fechaduras do Summit não tem grupo registrado. O script o conta como *unknown* (desconhecido), não como *classical* (clássico), porque ninguém o observou ainda.

O script lê uma exportação JSON, decide para cada endpoint se o seu grupo é híbrido, clássico ou desconhecido e conta os resultados por unidade. Repare que `null` vira desconhecido, não clássico, e que o híbrido é detectado pela parte `MLKEM` do nome. O PMS de Lakeside negocia híbrido, enquanto o do Summit não, o que dá uma primeira comparação entre unidades. Execute-o, depois acrescente um endpoint seu e verifique se as contagens mudam como esperado.

### 4.3 Desconhecido não é "não"

Tratar valores ausentes como resposta negativa faz os relatórios parecerem completos e esconde trabalho. Um desconhecido significa "descubra" e deve gerar uma tarefa: perguntar ao fornecedor, verificar a configuração ou observar o tráfego.

No HHG, o hub de fechaduras do Summit continua desconhecido até que o fornecedor das fechaduras responda ou o tráfego seja observado. Conte os desconhecidos separadamente em todo relatório, para que os leitores vejam quanto ainda falta descobrir. Dê a cada desconhecido um responsável e uma data, para que ele seja fechado em vez de ser carregado adiante.

### 4.4 Scripts reexecutáveis

Coloque o caminho de entrada e o formato de saída em argumentos, imprima o que foi lido (número de registros) e mantenha os scripts sob controle de versão com um README curto. Um script que outra pessoa consegue executar de novo no mês que vem vale muito mais do que um cálculo avulso.

Escreva o script para que ele falhe de forma ruidosa diante de entradas ruins, em vez de produzir um resumo errado. Inclua uma entrada de exemplo e a saída esperada, como fazem os laboratórios. Imprima os erros com clareza, nomeando o arquivo e a linha que os causaram.

### 4.5 Caso resolvido

Um operador recebe `endpoints.csv` de um scanner. O seu script conta híbridos, clássicos e desconhecidos por unidade, imprime o total de linhas lidas (48) e grava um pequeno CSV para o painel. Quando a saída do scanner ganha uma nova coluna no mês seguinte, o script continua funcionando porque lê as colunas pelo nome.

A contagem de linhas permite ao leitor verificar que nada foi descartado: se o scanner produziu 48 linhas, o resumo precisa dar conta das 48. Ler pelo nome, e não pela posição, foi o que tornou inofensiva a nova coluna.

### 4.6 Atividade prática

Modifique o Laboratório J para imprimir também a proporção de endpoints híbridos em todas as unidades.

Calcule a proporção como endpoints híbridos divididos por todos os endpoints, e também como híbridos divididos pelos endpoints com grupo conhecido, e imprima ambas com rótulos. Com os dados do Laboratório J, as respostas diferem por causa do hub de fechaduras do Summit. Explique em uma frase qual número pertence a um relatório e por quê. Mantenha a contagem de desconhecidos visível ao lado de ambos os números e teste o script com uma exportação vazia para garantir que ele não divide por zero.

### 4.7 Erros comuns e limites

- Ler colunas pela posição.
- Pular silenciosamente linhas com erros.
- Não imprimir quantos registros foram lidos.

Cada erro produz enganos silenciosos. Ler pela posição quebra assim que um scanner acrescenta uma coluna, como aconteceu no caso resolvido. Pular linhas ruins faz os totais parecerem completos quando não são, e as linhas puladas podem ser justamente as interessantes. Sem uma contagem de registros impressa, ninguém consegue verificar se o script leu o arquivo inteiro. Acrescente um teste para cada um aos seus scripts.

### 4.8 Um pequeno exemplo em CSV

A mesma ideia funciona com CSV. Leia com `csv.DictReader`, para que cada linha seja um dicionário indexado pelo nome da coluna; verifique se a coluna `group` existe antes do laço; e, para cada linha, decida entre híbrido, clássico ou desconhecido com a mesma regra do Laboratório J. Imprima as contagens e o número de linhas lidas, e grave cada linha que falhar na validação num arquivo separado para revisão, em vez de descartá-la. As linhas rejeitadas costumam ser as mais interessantes — um scanner que não conseguiu completar um handshake pode estar apontando exatamente para o problema de firewall que o Capítulo 13 ensina você a diagnosticar.

Quando entregar o script a um colega, inclua um arquivo de entrada de exemplo com algumas linhas sintéticas e a saída que ele deve produzir. Esse pequeno teste permite verificar que o script ainda funciona depois de alterado, do mesmo jeito que os laboratórios deste livro mostram a sua saída esperada.

Mantenha a regra de validação num único lugar do script.

### Exercícios

- **EX010 — Proporção.** Que proporção dos endpoints do Laboratório J é híbrida? Rubrica: 3 = 2/5 = 40 %.
- **EX011 — Validação.** Nomeie três verificações que um script deve fazer em cada registro de inventário. Rubrica: 3 = campos obrigatórios, tipo/valores permitidos, duplicatas.
- **EX012 — Tarefa para o desconhecido.** Escreva a tarefa que você abriria para o hub de fechaduras do Summit. Rubrica: 3 = o que descobrir, como, responsável.

### Síntese

Scripts simples, validados e reexecutáveis transformam exportações de inventário em resumos honestos, nos quais os desconhecidos viram tarefas.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 18

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Escopo de segurança e evidências

### Objetivos de aprendizagem

Você vai (1) trabalhar apenas dentro do escopo escrito; (2) coletar evidências que outras pessoas possam verificar; (3) proteger os dados sensíveis que encontrar; e (4) relatar constatações com clareza.

### 5.1 Escopo

Antes de executar qualquer verificação — mesmo uma conexão de cliente TLS a um servidor de produção —, confirme que ela está dentro do seu escopo escrito: quais sistemas, quais métodos, quais horários e a quem ligar se algo der errado. Testes ativos que tentam forçar downgrades ou injetar falhas são feitos apenas num laboratório isolado.

No HHG, o ticket OPS-412 é um exemplo: ele nomeia o jump host do laboratório, o portal de homologação e o método. Se não tiver certeza de que uma verificação está coberta, pergunte antes de executá-la, não depois.

### 5.2 Evidências

Uma boa evidência é específica e reproduzível: o comando, o alvo, o horário, a saída e a versão da ferramenta. Capturas de tela sozinhas são fracas; a saída em texto salva com uma anotação é melhor. Guarde as evidências onde a sua equipe combinou, não no seu notebook.

Na constatação do OPS-412, a saída foi salva numa pasta de evidências com o nome do ticket, com horário e ferramenta. Use sempre a mesma nomenclatura, para que as evidências possam ser encontradas depois, e mantenha a versão da ferramenta junto de cada saída, porque um cliente antigo pode relatar o resultado errado.

### 5.3 Dados sensíveis

Capturas de handshake, logs e arquivos de configuração podem conter nomes de host, endereços de clientes e às vezes credenciais. Colete apenas o que precisa (por exemplo, o grupo negociado), evite payloads completos de pacotes e siga as regras de retenção.

No HHG, os registros de hóspedes incluem dados de passaporte, então capturas de pacotes de sistemas voltados aos hóspedes poderiam contê-los. Prefira a saída das ferramentas de cliente e os campos de log às capturas. Se capturar algo por engano, avise o seu supervisor e apague o arquivo seguindo as regras de retenção. Apague o que não precisar mais quando a tarefa terminar.

### 5.4 Relato

Uma constatação declara o que você observou, onde, quando, como, por que isso importa e o que você recomenda, além de quem é responsável pela correção. Mantenha os fatos separados das opiniões.

Uma boa constatação permite ao responsável agir sem lhe fazer perguntas. Escreva primeiro a observação, depois a evidência, depois a sua interpretação, claramente marcada como provável, e não como certa. Nomeie o responsável e uma etapa de reverificação, para que a constatação possa ser encerrada com evidência. Se a sua interpretação se mostrar errada após a reverificação, atualize a constatação e diga isso.

### 5.5 Caso resolvido

Constatação (sintética): "Em 3 de outubro, às 10:15, a partir do jump host do laboratório (no escopo conforme o ticket OPS-412), `openssl s_client` para guest-portal.staging.hhg.example negociou X25519, embora a configuração do servidor liste X25519MLKEM768. Saída salva em evidence/OPS-412/. Causa provável: ordem dos grupos. Impacto: proteção híbrida não está em uso na homologação. Recomendação: reordenar os grupos; reverificar. Responsável: Web Operations."

Repare como a constatação separa fato de inferência: o grupo negociado e a configuração são observados, enquanto "ordem dos grupos" é marcada como causa provável. A constatação nomeia o escopo, o local da evidência, o impacto e o responsável, de modo que o Web Operations possa agir e verificar o resultado.

### 5.6 Atividade prática

Escreva uma constatação nesse formato para um resultado de laboratório do Capítulo 2.

Use uma das suas execuções do Capítulo 2, por exemplo a conexão que recorreu ao X25519 quando o híbrido não foi oferecido. Inclua o horário, a referência de escopo, o comando e a versão da ferramenta, onde a saída está salva, a causa provável marcada como tal, o impacto, uma recomendação e um responsável. Mantenha fatos e opiniões em frases separadas. Peça a um colega que verifique se um responsável conseguiria agir com base nela sem lhe perguntar nada.

### 5.7 Erros comuns e limites

- Testar fora do escopo "só para conferir".
- Evidência sem horário ou versão da ferramenta.
- Coletar capturas completas de pacotes.

Cada erro abala a confiança. Uma verificação fora do escopo, por menor que seja, pode derrubar um serviço e encerrar a autorização da sua equipe. Uma evidência sem horário ou versão da ferramenta não pode ser reproduzida nem comparada, então o trabalho precisa ser refeito. Capturas completas de pacotes coletam dados de hóspedes, como os de passaporte, de que ninguém precisava. Confira cada constatação e cada pasta de evidências quanto aos três antes de entregá-las. Corrija o que encontrar.

### 5.8 Quando algo dá errado

Se uma verificação que você executar causar um efeito inesperado — um alerta, um serviço lento, uma conta bloqueada —, pare, anote o horário e o que executou e ligue para o contato nomeado no seu escopo. Não tente corrigir em silêncio. É o relato precoce e honesto que mantém a autorização para trabalhos futuros, e a linha do tempo que você registra ajuda o responsável pelo serviço a separar o seu teste de qualquer incidente real que esteja acontecendo ao mesmo tempo.

Depois, acrescente à pasta de evidências uma nota curta descrevendo o que aconteceu e o que você faria diferente; o próximo operador que usar o mesmo escopo vai se beneficiar disso.

### Exercícios

- **EX013 — Verificação de escopo.** Liste as quatro coisas que você confirma antes de executar uma verificação. Rubrica: 3 = sistemas, métodos, horários, contato.
- **EX014 — Campos da evidência.** Liste cinco campos de um bom registro de evidência. Rubrica: 3 = comando, alvo, horário, saída, versão da ferramenta.
- **EX015 — Constatação.** Reescreva "a VPN é ruim para o quântico" como uma constatação adequada. Rubrica: 3 = observação, local, horário, método, impacto, recomendação, responsável.

### Síntese

Os operadores trabalham dentro do escopo escrito, coletam evidências verificáveis minimizando os dados sensíveis e escrevem constatações que separam fatos de opiniões.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 18

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Segurança quântica e pós-quântica: modelo do sistema

### Objetivos de aprendizagem

Você vai (1) construir um modelo simples do sistema que liste os usos criptográficos por serviço; (2) classificar cada uso pela exposição quântica; (3) registrar o responsável e a rota de mudança; e (4) usar o modelo para escolher as primeiras ações.

### 6.1 O modelo

Para cada serviço, liste: função (troca de chaves, autenticação, cifragem de dados armazenados, assinatura de software), algoritmo, biblioteca ou dispositivo, responsável, rota de mudança e tempo de vida dos dados. Mantenha-o numa tabela compartilhada.

Use o mapa de serviços do Capítulo 1 como ponto de partida: cada seta e cada caixa vira uma ou mais linhas. Acrescente o tempo de vida dos dados a partir do responsável pelos dados, não de suposições. No HHG, os registros de hóspedes com dados de passaporte têm tempo de vida de sete anos, o que orienta a maior parte das prioridades. Marque como desconhecido qualquer campo que não conseguir preencher.

### 6.2 Classes de exposição

*Risco de gravar agora*: troca de chaves clássica protegendo dados que precisam permanecer secretos por anos (dados de passaporte de hóspedes, 7 anos). *Risco de forjar depois*: assinaturas clássicas que precisam permanecer confiáveis por anos ou não podem ser trocadas rapidamente (firmware das fechaduras, a AC interna). *Adequado por ora*: AES-256, SHA-256, tokens de vida curta. *Desconhecido*: ainda sem evidência.

Classifique cada uso, não cada serviço: um serviço pode ter uma troca de chaves de gravar agora e um certificado de forjar depois. No HHG, a troca de chaves ECDHE do portal do hóspede é de gravar agora, e a AC interna é de forjar depois.

### 6.3 Escolhendo as primeiras ações

As primeiras ações são os riscos de gravar agora que as operações podem mudar por configuração: no HHG, o portal do hóspede e a API de reservas no balanceador de carga, e o servidor de troca de arquivos após a atualização. Os itens que dependem de fornecedores viram perguntas a fornecedores; os desconhecidos viram tarefas de investigação.

Essa ordem coloca o esforço onde as operações conseguem agir mais rápido sobre os dados mais expostos. Os itens que precisam de um fornecedor não são ignorados; eles começam com uma pergunta. No HHG, a rota de mudança da VPN de site é o firmware do fornecedor, então ela vira uma pergunta ao fornecedor enquanto o portal é alterado. Registre no modelo o motivo de cada primeira ação.

### 6.4 Caso resolvido

Extrato do modelo do HHG: portal do hóspede (TLS, ECDHE → híbrido disponível por configuração, dados de 7 anos, Web Ops) — agir agora; VPN de site (IPsec, ECDH, firmware do fornecedor, dados de 7 anos, Network Ops) — pergunta ao fornecedor; firmware das fechaduras (assinatura RSA, hardware, fornecedor das fechaduras) — forjar depois, nota para compras; banco de dados de reservas em repouso (AES-256) — adequado; sensores dos frigobares (desconhecido) — investigar.

O extrato mostra toda a gama de resultados: um item para agir agora, uma pergunta ao fornecedor, uma nota para compras, um item já adequado e um a investigar. Cada resultado decorre da rota de mudança e da classe de exposição, não de preferência. Os sensores dos frigobares continuam desconhecidos até que alguém os observe ou pergunte ao fornecedor.

### 6.5 Atividade prática

Construa a tabela do modelo para seis serviços do HHG e marque as primeiras ações.

Escolha seis serviços do mapa, incluindo pelo menos um dispositivo, como as fechaduras, e um com criptografia desconhecida. Para cada um, preencha função, algoritmo, biblioteca ou dispositivo, responsável, rota de mudança e tempo de vida, e depois classifique a exposição. Marque as primeiras ações e explique cada uma em uma linha. Compare com o caso resolvido. Onde a sua resposta divergir, diga por quê; uma rota de mudança diferente é um bom motivo, um palpite não é.

### 6.6 Usando a regra de Mosca

Uma regra prática simples (Mosca, 2018): some por quanto tempo os dados precisam permanecer secretos ao tempo que a mudança vai levar; se o total for maior do que o tempo até que possa existir um computador quântico capaz, os dados já estão em risco. Ninguém conhece esse último número, então experimente vários valores (por exemplo, 10, 15 e 20 anos). Os registros de hóspedes (7 anos) mais uma atualização de VPN de dois anos dão 9 anos — em risco somente se esse computador surgir dentro de 9 anos, o que é incerto, mas não impossível, de modo que a VPN entra na lista atrás dos itens com tempos de vida mais longos.

### 6.7 Erros comuns e limites

- Nenhum tempo de vida dos dados no modelo.
- Tratar o desconhecido como adequado.
- Ignorar a rota de mudança ao escolher ações.

Cada erro leva a uma prioridade errada. Sem um tempo de vida dos dados, o risco de gravar agora não pode ser julgado, e o portal não parece mais urgente do que o painel de operações. Tratar o desconhecido como adequado esconde do plano dispositivos como os sensores dos frigobares. Ignorar a rota de mudança coloca itens dependentes de fornecedores na lista da equipe de operações, onde ficam parados. Confira o seu modelo quanto a cada um antes de usá-lo para escolher o trabalho.

### Exercícios

- **EX016 — Classificar.** Classifique o TLS do portal do hóspede, a assinatura do firmware das fechaduras, os backups em AES-256 e um sensor desconhecido. Rubrica: 3 = gravar agora, forjar depois, adequado, desconhecido.
- **EX017 — Primeira ação.** Qual item do HHG as operações podem corrigir primeiro, e por quê? Rubrica: 3 = configuração TLS do balanceador de carga; sob controle das operações, dados de vida longa.
- **EX018 — Mosca.** Para dados mantidos em segredo por 7 anos e uma mudança de 2 anos, sob quais cronogramas quânticos supostos eles estão em risco? Rubrica: 3 = qualquer cronograma abaixo de 9 anos.

### Síntese

Um modelo do sistema com classes de exposição, responsáveis e rotas de mudança mostra aos operadores onde agir primeiro e onde perguntar aos fornecedores.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 18

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Segurança quântica e pós-quântica: dados e telemetria

### Objetivos de aprendizagem

Você vai (1) coletar fatos criptográficos da configuração, dos logs e dos fornecedores; (2) montar uma lista de materiais criptográficos (CBOM); (3) acrescentar aos logs campos com o algoritmo negociado; e (4) relatar a cobertura e os desconhecidos.

### 7.1 Fontes

Os arquivos de configuração dizem o que um serviço *oferece*. Os logs dizem o que foi *negociado*. As declarações dos fornecedores dizem o que um dispositivo fechado *alega*. Cada fato na CBOM deve dizer de que fonte veio e quando.

No HHG, a configuração do balanceador de carga mostrava o portal do hóspede oferecendo híbrido, mas os logs mostravam apenas 3 % de híbrido. Configuração e logs juntos explicaram o problema; qualquer um deles sozinho teria enganado. Classifique cada fato pela sua fonte. Uma declaração de fornecedor continua sendo uma alegação até ser observada em operação.

### 7.2 Atividade prática — Laboratório I

```python
# Lab I (ch 7): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("booking-gateway", "key-exchange", "X25519MLKEM768", "passive"), ("booking-gateway", "signature", "RSA-2048", "config"),
    ("door-lock-hub", "key-exchange", "ECDHE-P256", "passive"), ("door-lock-hub", "signature", "ECDSA-P256", "code"),
    ("reservations-db", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("minibar-sensor", "unknown", "unknown", "none"), ("property-vpn", "key-exchange", "ECDHE-P384", "config")]
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
quantum-vulnerable uses 5: booking-gateway/signature, door-lock-hub/key-exchange, door-lock-hub/signature, reservations-db/key-exchange, property-vpn/key-exchange
hybrid key exchange present on: ['booking-gateway']
```

O sensor do frigobar é desconhecido; até que seja investigado, a CBOM não pode dizer se o seu tráfego está em risco.

O script lista os usos criptográficos de seis ativos do HHG, sinaliza os que dependem de algoritmos vulneráveis ao quântico e mostra onde a troca de chaves híbrida já está presente. Repare que o AES-256-GCM do faturamento não é sinalizado, já que a cifragem simétrica desse tamanho é adequada, e que o sensor do frigobar conta como desconhecido, e não como seguro. O gateway de reservas negocia troca de chaves híbrida, mas ainda tem uma assinatura RSA-2048, então aparece nas duas listas. Acrescente um registro seu e verifique se as contagens mudam.

### 7.3 Registrando os algoritmos negociados

Os servidores web e os balanceadores de carga normalmente conseguem registrar o protocolo TLS, a cifra e o grupo por conexão; acrescente esses campos ao formato do log de acesso primeiro na homologação, verifique o volume de logs e depois promova. Os servidores SSH registram o algoritmo de troca de chaves num nível de log adequado. Os appliances de VPN registram os métodos negociados por túnel. Registre apenas o que precisa: campos de algoritmo, serviço, horário e um identificador grosseiro do cliente.

Teste a mudança primeiro na homologação. No HHG, o log de acesso do balanceador de carga ganhou um campo de grupo na homologação antes da produção. Verifique se os painéis leem o novo campo corretamente.

### 7.4 Cobertura

Relate que proporção dos serviços tem evidência, por fonte. "Híbrido em 40 % das conexões" significa pouco, a menos que você diga quais serviços e sensores foram incluídos. Mostre os desconhecidos ao lado de cada número.

No HHG, o painel mostra cada serviço separadamente, com o seu tipo de evidência: logs para a API de reservas, o portal do hóspede e a troca de arquivos, apenas configuração para as VPNs das unidades e desconhecido para as fechaduras e os sensores dos frigobares. Uma única média entre esses esconderia o problema do portal do hóspede e as lacunas. Informe sempre o denominador.

### 7.5 Caso resolvido

O HHG acrescenta o grupo negociado aos logs do balanceador de carga. Depois de uma semana, o painel mostra: API de reservas 88 % híbrido; portal do hóspede 3 % híbrido (um problema de configuração encontrado no Capítulo 5); troca de arquivos 0 % (OpenSSH antigo); VPNs das unidades — apenas evidência de configuração, 0 de 12 híbridas; fechaduras e sensores dos frigobares — desconhecidos.

O painel mostra como o tipo de evidência muda o que se pode dizer: os números da API de reservas e do portal do hóspede vêm dos logs, o da VPN vem da configuração, e fechaduras e sensores não podem ser relatados de forma alguma. Os 3 % do portal do hóspede são o item sobre o qual agir primeiro.

### 7.6 Atividade prática

No laboratório, acrescente o grupo TLS negociado ao log de acesso de um servidor web e confirme que ele aparece para clientes híbridos e clássicos.

Use um servidor de teste do seu laboratório e acrescente os campos de protocolo, cifra e grupo ao formato do seu log de acesso. Conecte-se uma vez com um cliente que oferece híbrido e outra com um que não oferece, depois encontre as duas linhas no log e salve-as. Verifique o volume de logs antes e depois. Anote a mudança de configuração exata, já que você precisaria dela para um ticket de mudança na homologação.

### 7.7 Mantendo a CBOM atualizada

Atualize a CBOM após cada mudança relevante: atualizações de bibliotecas, novos certificados, novos dispositivos, firmware de fornecedores. Marque as entradas com mais de três meses como "precisa de reverificação". Uma CBOM desatualizada é pior do que nenhuma, se as pessoas confiarem nela.

No HHG, a entrada do servidor de troca de arquivos precisa mudar após a atualização do seu OpenSSH, e a dos sensores dos frigobares quando o fornecedor responder. Atribua um responsável a cada entrada. Revise as entradas vencidas todo mês e reverifique-as ou marque-as como desconhecidas, para que a CBOM mostre a própria idade com honestidade.

### 7.8 Erros comuns e limites

- Tratar a configuração como prova de negociação.
- Log de depuração detalhado em produção.
- Esconder os desconhecidos.

Cada erro faz a CBOM ou o painel enganarem. A configuração mostra o que é oferecido, mas o portal do hóspede do HHG oferecia híbrido e o negociava em apenas 3 % das conexões. O log de depuração detalhado em produção enche discos e pode capturar dados sensíveis, como endereços de clientes. Esconder os desconhecidos, como as fechaduras e os sensores dos frigobares, faz a cobertura parecer completa. Confira a sua CBOM e o seu painel quanto a cada um antes de compartilhá-los. Corrija-os antes de publicar.

### Exercícios

- **EX019 — Fonte.** Qual fonte prova que um grupo foi negociado: configuração, logs ou ficha do fornecedor? Rubrica: 3 = logs (ou saída do cliente), com o motivo.
- **EX020 — Contagem do Laboratório I.** Quantos usos vulneráveis ao quântico o Laboratório I encontra, e em quantos ativos distintos? Rubrica: 3 = cinco usos em quatro ativos.
- **EX021 — Linha de cobertura.** Escreva uma linha de cobertura para o painel do HHG em 7.5. Rubrica: 3 = números delimitados, com fontes e desconhecidos.

### Síntese

Os operadores constroem a CBOM a partir da configuração, dos logs e das declarações dos fornecedores, com datas e fontes, acrescentam o registro do algoritmo negociado e relatam a cobertura com os desconhecidos visíveis.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 18

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Segurança quântica e pós-quântica: modos de falha

### Objetivos de aprendizagem

Você vai (1) listar as formas pelas quais as mudanças pós-quânticas podem falhar; (2) reconhecer cada uma pelos sintomas; (3) conhecer a primeira resposta segura; e (4) evitar correções que removem a proteção em todos os lugares.

### 8.1 Modos de falha comuns

*Handshake grande descartado*: um firewall, proxy ou balanceador de carga antigo não consegue lidar com a primeira mensagem maior; sintoma: timeouts em apenas um caminho. *Nenhum grupo compartilhado*: cliente e servidor não têm algoritmo em comum, muitas vezes depois de as opções clássicas terem sido removidas cedo demais. *Fallback silencioso*: o híbrido é oferecido, mas o clássico é escolhido, por causa da ordem ou de clientes antigos; sintoma: nada quebra, mas os logs mostram clássico. *Falha de certificado*: um cliente não consegue verificar um certificado pós-quântico ou não confia na nova raiz. *Dispositivos lentos*: dispositivos pequenos demoram mais com mensagens maiores.

### 8.2 Primeiras respostas seguras

Colete evidências primeiro (horário, cliente, caminho, erro). Limite o impacto de forma estreita: encaminhe o grupo de clientes afetado para um listener compatível ou reverta a mudança apenas no site afetado. Não desative o híbrido em todos os lugares por causa de um caminho; isso remove a proteção de todo o resto do tráfego.

No HHG, o timeout do Summit foi tratado assim: a sub-rede da recepção foi encaminhada para um listener sem o grupo híbrido enquanto o firewall era corrigido. Todas as outras unidades mantiveram a proteção híbrida. Registre a medida estreita como exceção, com data de término.

### 8.3 O fallback silencioso merece alertas

Como nada quebra, o fallback silencioso pode durar meses. Acrescente um alerta para quando a proporção híbrida de um serviço cair bruscamente e verifique primeiro a última mudança nesse serviço.

No HHG, a queda da API de reservas de 88 % para 2 % não produziu erro algum; apenas a proporção híbrida a mostrou. Defina o limiar do alerta a partir da variação normal de cada serviço e vincule o alerta ao runbook de quedas da proporção híbrida. Garanta que o alerta chegue a alguém que possa agir e que ele nomeie o serviço e o tamanho da queda.

### 8.4 Caso resolvido

Depois de uma atualização do balanceador de carga no data center, a proporção híbrida da API de reservas cai de 88 % para 2 % sem erros. O operador verifica o registro de mudanças: a atualização restaurou um perfil TLS padrão. Restaurar o perfil aprovado faz a proporção voltar a 87 % em dez minutos. Uma nota é acrescentada ao checklist de mudanças: "Reaplicar o perfil TLS após atualizações de firmware."

O operador seguiu a ordem segura: evidências primeiro, depois a última mudança, depois uma correção estreita. A nota no checklist transforma o incidente numa melhoria duradoura.

### 8.5 Atividade prática

Para cada modo de falha listado neste capítulo, escreva o sintoma que você veria no painel ou num ticket e a sua primeira verificação.

Cubra os cinco: handshake grande descartado, nenhum grupo compartilhado, fallback silencioso, falha de certificado e dispositivos lentos. Para cada um, escreva o que um operador realmente veria, como um ticket de uma unidade, uma proporção híbrida em queda ou um erro de certificado no log de um cliente, e a primeira verificação que você executaria. Mantenha cada primeira verificação segura e estreita. Compare com as correções típicas do Capítulo 13 quando chegar a ele.

### 8.6 Regras de reversão

Toda mudança que mexe em configurações criptográficas precisa de uma reversão escrita: a configuração anterior exata, quem pode acionar a reversão e como confirmar o sucesso. Prefira reverter um site ou um listener em vez do parque inteiro. Após a reversão, guarde as evidências e abra um ticket de problema, para que a causa seja corrigida em vez de a mudança ser esquecida.

No HHG, o perfil TLS aprovado é guardado sob controle de versão, o que tornou a reversão da API de reservas rápida e exata. Teste a reversão na homologação também.

### 8.7 Erros comuns e limites

- Desativação global para corrigir uma falha local.
- Nenhum alerta para o fallback silencioso.
- Reversões sem evidências.

Cada erro causa dano. Desativar o híbrido em todos os lugares por causa de um caminho, como o firewall do Summit, remove a proteção de todas as outras unidades. Sem um alerta, o fallback silencioso pode durar meses, como poderia ter acontecido com a redefinição do perfil da API de reservas. Uma reversão sem evidências deixa a causa desconhecida, então a mesma falha volta na mudança seguinte. Confira os seus planos de mudança e runbooks quanto aos três antes da aprovação.

### Exercícios

- **EX022 — Associar sintomas.** Associe os sintomas aos modos de falha: timeouts através de um proxy; erro "no shared group"; queda da proporção híbrida, sem erros. Rubrica: 3 = três associações corretas.
- **EX023 — Primeira resposta.** Um caminho do portal do hóspede através do firewall de uma unidade expira por timeout. Informe três primeiros passos. Rubrica: 3 = evidências, mitigação estreita, escalonamento/responsável.
- **EX024 — Linha do checklist.** Escreva uma linha de checklist de mudanças que teria evitado o incidente de 8.4. Rubrica: 3 = específica e verificável.

### Síntese

As mudanças pós-quânticas falham de algumas formas reconhecíveis; os operadores coletam evidências, limitam o impacto de forma estreita, geram alertas para o fallback silencioso e mantêm as reversões locais.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 18

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Segurança quântica e pós-quântica: ferramentas e métodos

### Objetivos de aprendizagem

Você vai (1) usar ferramentas de cliente para verificar a negociação; (2) estimar os tamanhos de handshake para diferentes escolhas de certificado; (3) validar uma ferramenta antes de confiar nela; e (4) seguir um método de verificação repetível.

### 9.1 Ferramentas de cliente

`openssl s_client` (TLS), `ssh -v` (SSH) e os comandos de status dos appliances de VPN mostram os algoritmos negociados. Use um cliente com suporte pós-quântico; um cliente antigo sempre relatará clássico. Registre a versão do cliente junto de cada resultado.

No HHG, o scanner do caso resolvido abaixo relatava todos os servidores como clássicos porque embutia uma biblioteca antiga. Escreva a versão do cliente ao lado de cada resultado, para que esses erros possam ser encontrados depois. Verifique o cliente primeiro contra um servidor de laboratório conhecido, para saber que ele consegue relatar híbrido quando for usado.

### 9.2 Atividade prática — Laboratório B

```python
# Lab B (ch 9): bytes of authentication in a TLS handshake for different signature choices.
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

Os certificados pós-quânticos tornam os handshakes muito maiores. Os operadores precisam desses números quando uma equipe de rede pergunta por que um firewall de repente vê mensagens maiores depois de uma troca de certificado.

O script estima os bytes de certificados e assinaturas num handshake TLS para cinco escolhas de assinatura, usando os tamanhos de chave pública e de assinatura da FIPS 204 e da FIPS 205. O ECDSA P-256 precisa de cerca de 1,3 KB; o ML-DSA-44, de cerca de 15,5 KB; e o SLH-DSA-SHA2-128s, de cerca de 40 KB. Esses números explicam por que as trocas de certificado exigem testes de rede. Mude a profundidade ou o número de SCTs para ver como as hipóteses afetam os totais.

### 9.3 Validando ferramentas

Antes de usar um scanner em sistemas reais, teste-o contra servidores de laboratório com configurações conhecidas: híbrido preferido, híbrido oferecido mas não preferido, apenas clássico. Se a ferramenta não conseguir distinguir esses casos, não use os seus resultados.

Guarde os resultados da validação com a versão da ferramenta e repita a validação após cada atualização da ferramenta. No HHG, essa etapa revelou o OpenSSL antigo do scanner antes que os seus resultados enganassem alguém. Uma ferramenta que você não consegue validar não deve produzir constatações, por mais conveniente que seja. Guarde o registro.

### 9.4 Um método repetível

1. Confirmar o escopo. 2. Registrar a ferramenta e a versão. 3. Executar a verificação. 4. Salvar a saída. 5. Comparar com o resultado esperado. 6. Registrar a constatação ou "conforme o esperado". Repetir os mesmos passos torna os resultados comparáveis ao longo do tempo.

Escreva o método num checklist curto e siga-o toda vez, mesmo nas verificações rápidas. O passo 5 é onde aparecem as surpresas, e cada surpresa deve levar a uma constatação ou a uma nota explicando por que o resultado é esperado. Registre a referência de escopo com a saída salva. Use os mesmos passos nas verificações automatizadas.

### 9.5 Caso resolvido

O scanner de um operador do HHG relata todos os servidores como clássicos. O teste contra o laboratório mostra que o scanner embute um OpenSSL antigo. Após a atualização, ele identifica corretamente o servidor híbrido do laboratório; só então é usado no parque de homologação, dentro do escopo.

Sem o teste de laboratório, o scanner teria produzido um relatório falso de que todo o parque era clássico, e o esforço teria ido para os serviços errados. A validação levou pouco tempo e economizou muito mais. Registre a validação com a versão do scanner.

### 9.6 Atividade prática

Valide uma ferramenta de cliente TLS contra três configurações de servidor de laboratório e registre os resultados.

Monte três servidores de laboratório ou três configurações num servidor: híbrido preferido, híbrido oferecido mas não preferido e apenas clássico. Execute a ferramenta contra cada um, registre a versão e a saída e diga se ela distinguiu corretamente os três. Se não distinguiu, anote o que relatou e se uma versão mais nova corrige isso. Arquive esses resultados no registro de validação da ferramenta descrito em 9.3.

### 9.7 Lendo tamanhos

Os números do Laboratório B são estimativas sob hipóteses declaradas: dois certificados na cadeia, cerca de 400 bytes de outros campos do certificado, duas assinaturas de transparência de certificados. Cadeias reais podem ser mais longas ou mais curtas. Quando precisar de números exatos para uma regra de firewall ou um ticket, capture um handshake de laboratório e meça-o, depois anote a configuração de onde ele veio.

Guarde os valores medidos com o ticket. No HHG, uma equipe de firewall que perguntasse sobre o portal do hóspede precisaria de valores medidos, não da estimativa do Laboratório B. Trate as estimativas como um guia da ordem de grandeza.

### 9.8 Erros comuns e limites

- Usar ferramentas não validadas.
- Resultados sem versões do cliente.
- Tratar estimativas de tamanho como medições.

Cada erro torna os resultados pouco confiáveis. Uma ferramenta não validada pode relatar errado o parque inteiro, como fez o scanner do HHG com um OpenSSL antigo. Resultados sem versões do cliente não podem ser verificados depois, já que um cliente antigo sempre relata clássico. Os números de tamanho do Laboratório B se apoiam em hipóteses declaradas, então uma regra de firewall construída sobre eles pode estar errada; meça um handshake real de laboratório antes de usar números num ticket. Confira as suas anotações quanto a cada um desses.

### 9.9 Comparando resultados ao longo do tempo

Guarde a saída salva de cada verificação numa pasta datada, para que a execução do mês seguinte possa ser comparada linha a linha. Um `diff` simples entre duas execuções do mesmo script mostra rapidamente quais serviços mudaram de negociação, o que muitas vezes é mais rápido do que ler um painel quando você investiga uma reclamação específica.

Mantenha os nomes das pastas consistentes, para que os scripts encontrem as execuções. No HHG, foi comparando execuções datadas que o job noturno detectou os dois endpoints que passaram a clássico após um patch.

### Exercícios

- **EX025 — Validação da ferramenta.** Descreva as três configurações de laboratório e os resultados esperados para validar um scanner. Rubrica: 3 = três configurações com as saídas esperadas.
- **EX026 — Razão de tamanhos.** Pelo Laboratório B, aproximadamente quantas vezes maior é a autenticação com ML-DSA-44 do que com ECDSA P-256? Rubrica: 3 = cerca de 12 (15.524/1.290).
- **EX027 — Método.** Liste os seis passos de uma verificação repetível. Rubrica: 3 = os seis, em ordem.

### Síntese

Os operadores usam ferramentas de cliente atuais e validadas, registram versões, seguem um método repetível e entendem os efeitos de tamanho dos certificados pós-quânticos.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 18

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (inglês) →](../../en/book/MANUSCRIPT.md#ch-10)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre o HHG são sintéticos. Esta edição parcial traz as resoluções de EX001–EX027; as de EX028–EX054 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

**EX001.** TLS do portal do hóspede: configuração (operações do HHG). SSH da troca de arquivos: atualização do pacote e depois configuração (operações do HHG). VPN de site: firmware do fornecedor (fornecedor de rede). POS para a processadora: atualização do fornecedor/da processadora. Assinatura do firmware das fechaduras: renovação de hardware (fornecedor das fechaduras).

**EX002.** "Alguém poderia gravar em segredo, hoje, os nossos dados cifrados de hóspedes e guardá-los até que computadores quânticos futuros consigam abri-los. Como os dados de passaporte precisam permanecer privados por anos, estamos atualizando agora a forma como os nossos sistemas acordam chaves secretas."

**EX003.** Substituir RSA e ECDH (o algoritmo de Shor os quebra). Manter AES-256 (Grover deixa um trabalho de ~128 bits) e SHA-256 (sem quebra quântica prática).

**EX004.** TLS: (EC)DHE ou grupo híbrido / assinaturas dos certificados. SSH: algoritmo de KEX / chaves de host e de usuário. IPsec (IKEv2): Diffie–Hellman mais trocas de chaves adicionais / certificados ou chaves pré-compartilhadas.

**EX005.** Não é híbrida (`curve25519-sha256` é clássico). Verificar a ordem de `KexAlgorithms` do servidor e as versões do OpenSSH do cliente e do servidor.

**EX006.** 1.216 − 32 = 1.184 bytes (a chave de encapsulamento do ML-KEM-768).

**EX007.** `openssl version` (no host e dentro dos contêineres), `ssh -V` e a versão do runtime da aplicação (Java/Go) ou o SBOM da imagem do contêiner.

**EX008.** Repositório de confiança do sistema operacional; truststore do Java; pacotes de AC da aplicação ou do contêiner (também as listas de confiança dos appliances).

**EX009.** Parar; não abrir, copiar nem testar a chave; comunicar imediatamente pelo processo de segurança; registrar onde e quando a viu.

**EX010.** 2 de 5 = 40 %.

**EX011.** Campos obrigatórios presentes; valores de tipo permitido/nomes de algoritmo conhecidos (ou null → desconhecido); entradas de host duplicadas detectadas.

**EX012.** "Descobrir os algoritmos de TLS/troca de chaves usados pelo hub de fechaduras do Summit (modelo, firmware). Método: pedido de documentação ao fornecedor e exportação da configuração. Responsável: TI da unidade Summit com o fornecedor das fechaduras. Prazo: 30 dias."

**EX013.** Quais sistemas; quais métodos; quais horários; a quem contatar se algo der errado.

**EX014.** Comando exato; alvo; data e horário; saída salva; ferramenta e versão (mais a referência de escopo).

**EX015.** "Em (data/horário), a exportação da configuração da VPN de site de Harbour (ref. do ticket) mostra IKEv2 apenas com o grupo ECDH 19 e nenhuma troca de chaves ML-KEM adicional. Registros de hóspedes (confidencialidade de 7 anos) atravessam esse túnel, então o tráfego gravado poderia ser decifrado por um computador quântico futuro. Recomendação: pedir ao fornecedor suporte híbrido conforme a RFC 9370 e a data. Responsável: Network Ops."

**EX016.** TLS do portal do hóspede: gravar agora. Assinatura do firmware das fechaduras: forjar depois. Backups em AES-256: adequado por ora. Sensor desconhecido: desconhecido.

**EX017.** O TLS do portal do hóspede/da API de reservas no balanceador de carga: as operações controlam a configuração, a mudança é rápida e ele transporta dados de hóspedes de 7 anos.

**EX018.** 7 + 2 = 9 anos: em risco sob qualquer cronograma suposto menor que 9 anos.

**EX019.** Logs (ou a saída de uma ferramenta de cliente): eles registram o que foi de fato negociado; a configuração mostra apenas o que é oferecido; as fichas dos fornecedores são alegações.

**EX020.** Cinco usos em quatro ativos (booking-gateway, door-lock-hub ×2, reservations-db, property-vpn).

**EX021.** "API de reservas 88 % híbrido (logs do balanceador, todos os listeners do data center); portal do hóspede 3 % (logs do balanceador); troca de arquivos 0 % (logs do sshd); VPNs das unidades 0/12 (apenas configuração); fechaduras e sensores dos frigobares desconhecidos (sem fonte)."

**EX022.** Timeouts através de um proxy → handshake grande descartado. "No shared group" → nenhum algoritmo em comum. Queda da proporção, sem erros → fallback silencioso.

**EX023.** Coletar evidências (horário, cliente, caminho, erro, modelo do firewall); encaminhar a sub-rede afetada daquela unidade para um listener compatível, como exceção registrada; escalar ao responsável/fornecedor do firewall.

**EX024.** "Após qualquer atualização de firmware do balanceador de carga, reaplicar o perfil TLS aprovado e confirmar a proporção híbrida no painel em até 30 minutos."

**EX025.** Híbrido preferido → a ferramenta relata híbrido; híbrido oferecido depois do clássico → a ferramenta relata clássico negociado (e, idealmente, a oferta); apenas clássico → a ferramenta relata clássico. A ferramenta precisa distinguir os três.

**EX026.** 15.524 / 1.290 ≈ 12 vezes.

**EX027.** Confirmar o escopo; registrar a ferramenta e a versão; executar a verificação; salvar a saída; comparar com o esperado; registrar a constatação ou "conforme o esperado".

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; a situação das normas muda, então verifique de novo.

- Bernstein, D. J., et al. (2024). KyberSlash. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- IETF RFCs: 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025); IR 8547 initial public draft (2024). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227> · <https://doi.org/10.6028/NIST.IR.8547.ipd>
- OpenSSH release notes. <https://www.openssh.com/releasenotes.html>
- OpenSSL 3.5 NEWS. <https://github.com/openssl/openssl/blob/openssl-3.5/NEWS.md>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
