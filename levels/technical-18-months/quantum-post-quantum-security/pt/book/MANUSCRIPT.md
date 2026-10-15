# Segurança Quântica e Pós-Quântica: Operações Práticas para Equipes Técnicas

- Idioma: português do Brasil (`pt`); curso técnico, 18 meses; aproximadamente 1.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–18 de 18 têm texto didático escrito; os exercícios EX001–EX054 (três por capítulo) têm as resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, com saídas verificadas. A revisão independente e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
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

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 18

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 18

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 18

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 18

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 18

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 18

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 18

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 18

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 18

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Segurança quântica e pós-quântica: configuração de controles

### Objetivos de aprendizagem

Você vai (1) configurar a troca de chaves híbrida em servidores TLS e SSH num laboratório; (2) auditar configurações quanto à presença e à preferência; (3) manter o fallback clássico durante a transição; e (4) aplicar as mudanças por meio do controle de mudanças.

### 10.1 Configuração do TLS

Em servidores baseados em OpenSSL, defina a lista de grupos com o híbrido primeiro, por exemplo `X25519MLKEM768:X25519:secp256r1`. Os servidores web e os balanceadores de carga expõem isso por meio de uma diretiva ou de um perfil; consulte a documentação do seu produto para os nomes exatos. A ordem importa quando é o servidor que decide.

No HHG, o balanceador de carga do portal do hóspede listava o X25519 primeiro, então a maioria dos clientes negociava clássico. Mantenha os grupos clássicos depois do híbrido, e não no lugar dele, e salve a string exata de grupos na linha de base, para que todos os listeners usem a mesma ordem.

### 10.2 Configuração do SSH

Na configuração do servidor OpenSSH, coloque `mlkem768x25519-sha256` primeiro em `KexAlgorithms`, seguido de `sntrup761x25519-sha512@openssh.com` e `curve25519-sha256` por compatibilidade. Recarregue o serviço e teste com `ssh -v` a partir de um cliente que suporte o híbrido.

No HHG, essa é a mudança de que o servidor de troca de arquivos precisa após a atualização do seu OpenSSH. Salve a linha `KexAlgorithms` antes e depois da edição, verifique a sintaxe da configuração antes de recarregar e mantenha uma sessão existente aberta enquanto testa, para que um erro não o deixe trancado do lado de fora.

### 10.3 Atividade prática — Laboratório T

```python
# Lab T (ch 10): audit synthetic TLS and SSH server configurations for post-quantum key exchange and preference order.
configs = {  # service: ordered list of offered groups (server preference) - synthetic
    "booking-api": ["X25519MLKEM768", "X25519", "secp256r1"],
    "guest-portal": ["X25519", "X25519MLKEM768", "secp256r1"],
    "channel-sftp": ["ecdh-sha2-nistp256"],
    "ops-grafana": ["X25519", "secp384r1"]}
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
booking-api       OK (hybrid preferred)
guest-portal      WARN hybrid offered but not preferred
channel-sftp      CLASSICAL ONLY
ops-grafana       CLASSICAL ONLY
```

O portal do hóspede oferece híbrido, mas prefere o X25519 — o problema encontrado no Capítulo 5. O SFTP dos canais e o painel de operações são apenas clássicos.

O script audita a lista ordenada de cada serviço quanto a duas propriedades: se algum método híbrido é oferecido e se um deles vem primeiro. A API de reservas passa nas duas verificações, enquanto o portal do hóspede falha na preferência e os outros dois falham na presença. Repare que a entrada de channel-sftp é um método SSH, que a lista TLS do script não conhece; uma auditoria de SSH precisa da sua própria lista de nomes híbridos, como `mlkem768x25519-sha256`. Estenda o script para tratar esse caso.

### 10.4 Controle de mudanças

Toda mudança em produção passa por um ticket de mudança: o quê, por quê, quando, risco, evidência de teste, reversão, aprovador. Faça a mudança na homologação, verifique, depois aplique em produção numa janela de baixo tráfego, verifique de novo e feche o ticket com evidências.

No HHG, o ticket OPS-430 é um exemplo de registro completo. Anexe a evidência da homologação antes de pedir a aprovação e feche o ticket somente após a verificação em produção. No HHG, a mudança em produção do OPS-430 foi feita às 06:00 de uma terça-feira, um horário de baixo tráfego para o portal do hóspede. Registre o nome do aprovador.

### 10.5 Caso resolvido

Ticket OPS-430: reordenar os grupos no balanceador de carga do portal do hóspede para `X25519MLKEM768:X25519:secp256r1`. Teste na homologação: híbrido negociado pelos clientes atuais, X25519 por um cliente antigo. Mudança em produção na terça-feira às 06:00; a verificação às 06:10 mostra híbrido negociado; a proporção híbrida no painel sobe de 3 % para 85 % até o meio-dia. Plano de reversão (restaurar a ordem anterior) não necessário.

O ticket segue todos os passos: teste na homologação com os dois tipos de cliente, uma janela de baixo tráfego, verificação imediata e um resultado mensurável. A reversão foi escrita com antecedência, embora não tenha sido usada. A subida da proporção híbrida também confirma a constatação do Capítulo 5.

### 10.6 Atividade prática

No laboratório, configure um servidor TLS e um servidor SSH com o híbrido primeiro; verifique com clientes; escreva o ticket de mudança que você abriria para a produção.

Coloque o método híbrido primeiro e mantenha os métodos clássicos depois dele nos dois servidores. Verifique do lado do cliente com `openssl s_client` e `ssh -v`, e do lado do servidor com os logs. Teste também com um cliente antigo, para confirmar o fallback. Depois escreva o ticket de produção com o quê, por quê, quando, risco, evidência de teste, reversão e aprovador, usando o OPS-430 como modelo.

### 10.7 Mantenha o fallback por ora

Durante a transição, mantenha as opções clássicas depois do híbrido, para que os clientes mais antigos continuem se conectando. Removê-las é uma decisão separada e posterior, baseada num monitoramento que mostre poucos clientes clássicos restantes e no acordo com os responsáveis pelos serviços e com os parceiros.

No HHG, quatro agências de viagem ainda usavam clientes SFTP antigos após a atualização, então remover os métodos clássicos as teria desconectado. Monitore a proporção clássica por serviço e por parceiro antes de propor a remoção, e registre a decisão e quem concordou com ela. A remoção não é uma decisão apenas do operador.

### 10.8 Erros comuns e limites

- Híbrido listado depois do clássico.
- Remover o fallback cedo demais.
- Mudanças sem tickets ou sem verificação.

Cada erro enfraquece a proteção ou o controle. Listar o híbrido depois do clássico significa que a maioria dos clientes negocia clássico, como no portal do hóspede do HHG. Remover o fallback cedo demais desconecta clientes mais antigos, como as quatro agências com clientes SFTP antigos. Uma mudança sem ticket ou sem verificação não pode ser revisada, revertida de forma confiável nem comprovada. Confira cada mudança de configuração quanto aos três antes da aprovação. Corrija o que encontrar.

### Exercícios

- **EX028 — Linha do TLS.** Escreva uma lista de grupos com o híbrido primeiro e dois fallbacks clássicos. Rubrica: 3 = híbrido primeiro, nomes válidos.
- **EX029 — Linha do SSH.** Escreva uma linha `KexAlgorithms` com o híbrido primeiro e fallbacks compatíveis. Rubrica: 3 = lista ordenada válida.
- **EX030 — Ticket.** Escreva o ticket de mudança para habilitar o SSH híbrido no servidor SFTP dos canais. Rubrica: 3 = o quê, por quê, quando, risco, evidência de teste, reversão, aprovador.

### Síntese

Os operadores configuram o híbrido primeiro, com fallback clássico, no TLS e no SSH, auditam a preferência além da presença e fazem as mudanças por meio de tickets testados e verificados.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 18

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Segurança quântica e pós-quântica: verificação

### Objetivos de aprendizagem

Você vai (1) verificar se as mudanças atingiram o seu objetivo; (2) executar testes de resposta conhecida e testes negativos no laboratório; (3) usar controles negativos; e (4) encerrar o trabalho com evidências.

### 11.1 Verifique a negociação, não a configuração

Uma configuração pode dizer híbrido enquanto as conexões negociam clássico. Verifique do lado do cliente (saída das ferramentas) e do lado do servidor (logs). No SSH, confira o algoritmo de KEX no `ssh -v`; nas VPNs, confira o status do túnel.

Use os dois lados: a saída da ferramenta de cliente mostra o que um cliente obteve, e os logs do servidor mostram o que todos os clientes obtiveram. No HHG, a configuração do portal do hóspede listava o híbrido, mas os logs mostravam apenas 3 % de híbrido. Verifique com mais de um tipo de cliente, incluindo um cliente antigo, para confirmar que o fallback continua funcionando como pretendido.

### 11.2 Atividade prática — Laboratório V

```python
# Lab V (ch 11): known-answer and negative tests - the habit behind validating PQC libraries.
import hashlib
KATS = [  # (function, input, expected hex prefix) - published test values for SHA-3 / SHAKE on empty input
    ("sha3_256", b"", "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"),
    ("shake_128/32", b"", "7f9c2ba4e88f827d616045507605853ed73b8093f6efbc88eb1a6eacfa66ef26"),
]
def run(name, data):
    if name == "sha3_256": return hashlib.sha3_256(data).hexdigest()
    return hashlib.shake_128(data).hexdigest(32)
for name, data, want in KATS:
    print(f"KAT {name:13s}", "PASS" if run(name, data) == want else "FAIL")
SIZES = {"ML-KEM-512": 800, "ML-KEM-768": 1184, "ML-KEM-1024": 1568}   # encapsulation-key bytes, FIPS 203
def validate_ek(param, ek):
    if len(ek) != SIZES[param]: raise ValueError(f"{param}: expected {SIZES[param]} bytes, got {len(ek)}")
    return True
for param, n in [("ML-KEM-768", 1184), ("ML-KEM-768", 1183), ("ML-KEM-512", 1184)]:
    try: validate_ek(param, bytes(n)); print(f"negative/positive test {param} len {n}: accepted")
    except ValueError as e: print(f"negative/positive test {param} len {n}: rejected ({e})")
```

Saída esperada:

```text
KAT sha3_256      PASS
KAT shake_128/32  PASS
negative/positive test ML-KEM-768 len 1184: accepted
negative/positive test ML-KEM-768 len 1183: rejected (ML-KEM-768: expected 1184 bytes, got 1183)
negative/positive test ML-KEM-512 len 1184: rejected (ML-KEM-512: expected 800 bytes, got 1184)
```

Os testes de resposta conhecida verificam se as funções produzem as saídas publicadas; os testes negativos verificam se entradas com comprimento errado são rejeitadas.

A primeira parte confere duas funções de hash contra as saídas publicadas para a entrada vazia; a segunda verifica se chaves de encapsulamento com comprimento errado para cada conjunto de parâmetros do ML-KEM são rejeitadas. Um PASS nas respostas conhecidas e as rejeições corretas mostram que as verificações funcionam. São os mesmos hábitos usados ao validar bibliotecas pós-quânticas reais: confirmar as saídas corretas e confirmar que entradas ruins são recusadas. Altere um byte de um valor esperado e confirme que o teste agora relata FAIL.

### 11.3 Controles negativos

Para confiar numa verificação, mostre que ela pode falhar: execute-a contra um servidor com o híbrido removido e confirme que ela relata clássico. Uma verificação que sempre diz "passou" é inútil.

No HHG, após o OPS-430, o controle negativo na homologação mostrou 0 % de híbrido com o híbrido removido, provando que o painel mostraria uma falha se ela ocorresse. Execute o controle negativo na homologação ou no laboratório, nunca removendo a proteção em produção. Registre o resultado do controle negativo no ticket, com o horário e a configuração usada.

### 11.4 Encerrando com evidências

Anexe ao ticket as saídas, capturas de tela do painel com horários e a versão da configuração. Anote qualquer coisa inesperada, mesmo que a mudança tenha funcionado.

No HHG, o ticket OPS-430 foi fechado com os resultados dos clientes, o número de 85 % dos logs do balanceador de carga e o controle negativo da homologação. Quem ler o ticket meses depois consegue ver o que foi verificado e quando. Evidência ausente significa que a mudança não está verificada, por melhor que ela pareça funcionar. Guarde as evidências na pasta combinada e vincule-as a partir do ticket, em vez de colar saídas grandes.

### 11.5 Caso resolvido

Após o OPS-430, o operador verifica: três tipos de cliente contra o portal de produção (dois híbridos, um cliente mais antigo clássico, como esperado); os logs do balanceador de carga mostram 85 % de híbrido; o controle negativo na homologação (híbrido removido) mostra corretamente 0 %. Evidências anexadas; ticket fechado.

A verificação cobre os dois lados, inclui clientes antigos como o fallback esperado e acrescenta um controle negativo que prova que a verificação pode falhar. Cada resultado é anexado ao ticket. Um auditor conseguiria verificar o trabalho apenas pelo ticket, sem perguntar ao operador. Use-o como modelo.

### 11.6 Atividade prática

Verifique uma mudança de laboratório dos lados do cliente e do servidor e inclua um controle negativo.

Use uma mudança do Capítulo 10, como a reordenação dos grupos. Registre os resultados dos clientes com as versões, as linhas de log do servidor e a versão da configuração. Para o controle negativo, remova o híbrido no laboratório, confirme que a verificação relata clássico e depois restaure-o. Anexe todas as saídas a um ticket de prática, como se fosse fechar uma mudança de produção, e anote qualquer coisa inesperada. Peça a um colega que o revise. Guarde o ticket com as suas anotações de laboratório.

### 11.7 Verificando após outras mudanças

A verificação não serve apenas para as suas próprias mudanças. Reverifique a negociação híbrida após qualquer atualização que mexa na pilha TLS ou SSH — patches do sistema operacional, firmware do balanceador de carga, reconstrução de imagens de contêiner —, porque essas atualizações podem redefinir a configuração. Uma verificação curta, em script, executada após cada janela de patches detecta regressões em poucas horas.

No HHG, uma atualização de firmware do balanceador de carga redefiniu o perfil TLS da API de reservas; uma verificação em script após a janela de patches a teria encontrado no mesmo dia. Acrescente a verificação ao procedimento de patches.

### 11.8 Erros comuns e limites

- Verificar apenas a configuração.
- Nenhum controle negativo.
- Fechar tickets sem evidências.

Cada erro deixa uma mudança sem comprovação. A configuração sozinha pode dizer híbrido enquanto os clientes negociam clássico, como no portal do hóspede do HHG antes do OPS-430. Uma verificação sem controle negativo pode relatar sucesso aconteça o que acontecer. Um ticket fechado sem evidências não pode ser auditado e não dá ao próximo operador nada com que comparar após uma atualização. Confira cada ticket fechado quanto aos três. Corrija o que encontrar antes que o ticket seja revisado. Anote o que você mudou.

### 11.9 O que a verificação não mostra

Uma negociação híbrida bem-sucedida mostra que a chave de sessão foi acordada com ML-KEM e X25519 juntos. Ela não mostra que o certificado do servidor é pós-quântico (provavelmente ainda é ECDSA ou RSA), que todos os outros saltos do caminho estão protegidos nem que a biblioteca está livre de falhas de implementação. Escreva esses limites no ticket, para que ninguém leia "verificado" como "o serviço inteiro é seguro contra o quântico". A qualidade da implementação vem do uso de bibliotecas avaliadas e atualizadas; falhas passadas, como o problema de tempo KyberSlash (Bernstein et al., 2024), foram corrigidas por atualizações de bibliotecas, não por configuração.

Anote esses limites em todo ticket de verificação.

### Exercícios

- **EX031 — Dois lados.** Nomeie a evidência do lado do cliente e a do lado do servidor para a negociação híbrida no TLS. Rubrica: 3 = saída da ferramenta e logs do servidor.
- **EX032 — Controle negativo.** Projete um controle negativo para a verificação do SSH híbrido. Rubrica: 3 = remover o híbrido, esperar clássico.
- **EX033 — Verificação pós-patch.** Escreva três passos de uma verificação pós-patch. Rubrica: 3 = executar os clientes, conferir logs/painel, comparar com a linha de base.

### Síntese

A verificação confere a negociação real dos dois lados, inclui controles negativos, é repetida após outras atualizações e encerra o trabalho com evidências.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 18

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Laboratório controlado I

### Objetivos de aprendizagem

Você vai (1) montar um laboratório isolado com TLS e SSH capazes de híbrido; (2) reproduzir uma implantação híbrida de ponta a ponta; (3) reproduzir uma falha comum; e (4) escrever um relatório de laboratório.

### 12.1 Montagem do laboratório

Use duas ou três máquinas virtuais ou contêineres numa rede isolada: um servidor com OpenSSL e OpenSSH atuais, um cliente com ferramentas atuais e, opcionalmente, um cliente antigo. Nada de dados de produção, nenhuma conexão com redes de produção, nenhuma credencial real.

Registre as versões do OpenSSL, do OpenSSH e dos clientes, já que os resultados dependem delas. Use chaves de teste geradas e nomes de host de laboratório. No HHG, os trainees montam esse laboratório antes de mexer em qualquer serviço de homologação. Tire um snapshot assim que o laboratório funcionar.

### 12.2 Exercícios no laboratório

Configure o servidor com o híbrido primeiro; conecte com o cliente atual (espere híbrido) e com o cliente antigo (espere fallback clássico). Depois reordene os grupos para pôr o clássico primeiro e observe que o cliente atual agora negocia clássico — o fallback silencioso do Capítulo 8. Restaure a ordem correta.

Salve a saída de cada execução com a configuração vigente no momento. O passo do fallback silencioso é o que mais importa: ele mostra que uma única edição pode remover a proteção híbrida sem que nada quebre, e é por isso que a ordem de preferência é verificada após cada mudança.

### 12.3 Reproduzindo uma falha de tamanho

Alguns laboratórios conseguem emular um dispositivo que descarta primeiras mensagens grandes, por exemplo um proxy configurado com um buffer pequeno. Observe timeouts com híbrido e sucesso sem ele. Isso mostra por que a correção está no dispositivo de rede, e não na remoção da proteção.

No laboratório, registre o tamanho da primeira mensagem com e sem híbrido, para poder ligar os timeouts ao tamanho. No HHG, isso reproduziu o problema do firewall do Summit e embasou o pedido de uma correção de firmware em vez da remoção do híbrido do portal.

### 12.4 Relatório de laboratório

Declare o propósito, o ambiente (versões), os passos, os resultados, a interpretação e as lições. Inclua as saídas.

Escreva-o de modo que outro operador possa repetir o laboratório apenas a partir do seu relatório. Mantenha a interpretação separada dos resultados e registre qualquer passo que não saiu como esperado, com o que você fez em seguida. Inclua a data e o snapshot de laboratório usado. Um relatório curto com versões e saídas completas é melhor do que um longo sem elas. Peça a um colega que repita um passo a partir dele antes de entregá-lo.

### 12.5 Caso resolvido

O relatório de laboratório de um trainee do HHG: servidor com OpenSSL 3.5.x e OpenSSH atual; o cliente atual negociou X25519MLKEM768 e `mlkem768x25519-sha256`; o cliente antigo recorreu ao clássico; os grupos reordenados causaram fallback silencioso; restaurado. Lição: sempre verificar a ordem de preferência após edições.

O relatório é curto, mas completo: versões, resultados, a falha reproduzida e uma lição que muda a prática. Outro trainee conseguiria repeti-lo apenas a partir do relatório. A lição sobre a ordem de preferência é a mesma que o HHG aprendeu no portal do hóspede, então o laboratório confirma com segurança uma constatação de produção.

### 12.6 Atividade prática

Monte o laboratório e complete os passos; escreva o seu relatório.

Siga os passos em ordem: monte o laboratório isolado, configure o híbrido primeiro, teste com clientes atuais e antigos, reproduza o fallback silencioso reordenando os grupos, restaure a ordem e, se o seu laboratório permitir, reproduza uma falha de tamanho. Salve todas as saídas. Depois escreva o relatório com propósito, ambiente e versões, passos, resultados, interpretação e lições, e peça a um colega que repita um passo apenas a partir do seu relatório. Guarde o relatório. Anote o que o colega achou pouco claro.

### 12.7 Segurança do laboratório

Mantenha a rede do laboratório separada das redes de casa ou do escritório; use chaves de teste geradas; destrua o laboratório ao terminar ou faça um snapshot dele com anotações. Nunca aponte ferramentas de laboratório para hosts de produção por engano: use nomes de host que não possam ser resolvidos fora do laboratório e confira duas vezes os alvos antes de executar comandos.

Registre no relatório onde o laboratório rodou, o seu layout de rede e os nomes dos alvos, para que outras pessoas possam verificar que o laboratório ficou isolado. Se suspeitar que um comando atingiu um host real, pare e comunique.

### 12.8 Erros comuns e limites

- Laboratórios conectados à produção.
- Pular o teste com o cliente antigo.
- Relatórios sem versões.

Cada erro enfraquece o laboratório ou o seu relatório. Um laboratório conectado à produção pode afetar serviços reais ou vazar tráfego de teste. Pular o teste com o cliente antigo esconde se o fallback funciona, e é exatamente disso que dependem os parceiros do HHG com clientes mais antigos. Um relatório sem versões não pode ser repetido nem comparado, porque os resultados dependem das versões das bibliotecas e dos clientes. Confira o seu laboratório e o seu relatório quanto aos três. Corrija-os antes de entregar.

### 12.9 Ampliando o laboratório

Quando o básico funcionar, amplie o laboratório um passo de cada vez: acrescente um segundo servidor atrás de um proxy reverso para mostrar que cada salto negocia separadamente; acrescente um parser de logs que conte as sessões híbridas e clássicas; ou acrescente um bastion SSH para praticar a configuração de SFTP do Capítulo 10. Cada ampliação deve terminar com uma nota curta no relatório, para que o laboratório se torne um ambiente de treinamento reutilizável pela equipe.

Registre o propósito de cada ampliação. Anote também as suas versões.

### Exercícios

- **EX034 — Projeto do laboratório.** Liste as máquinas e as versões de software do laboratório. Rubrica: 3 = servidor, cliente atual, cliente antigo, versões.
- **EX035 — Fallback silencioso.** Descreva como reproduzir o fallback silencioso no laboratório. Rubrica: 3 = reordenar os grupos, observar clássico com o cliente atual.
- **EX036 — Relatório.** Liste as seis seções do relatório de laboratório. Rubrica: 3 = propósito, ambiente, passos, resultados, interpretação, lições.

### Síntese

Um laboratório controlado permite aos operadores reproduzir com segurança a implantação híbrida, o fallback silencioso e as falhas de tamanho, e documentar as lições.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 18

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Segurança quântica e pós-quântica: diagnóstico de problemas

### Objetivos de aprendizagem

Você vai (1) seguir um método de diagnóstico passo a passo; (2) fazer a triagem de logs de falha em causas prováveis; (3) corrigir problemas comuns sem remover a proteção de forma ampla; e (4) registrar a causa e a correção.

### 13.1 Método

Reproduzir → isolar → formular hipótese → testar → corrigir → verificar → registrar. Reproduza com o mesmo cliente e o mesmo caminho no laboratório, se possível. Isole tentando um caminho direto, um cliente diferente ou o híbrido desligado numa única conexão de teste. Mude uma coisa de cada vez.

No HHG, o timeout do Summit foi reproduzido no laboratório com o mesmo firmware de firewall antes que qualquer correção fosse escolhida. Anote cada hipótese e o teste que a confirmou ou descartou, para que o registro mostre como a causa foi encontrada.

### 13.2 Atividade prática — Laboratório H

```python
# Lab H (ch 13): triage synthetic handshake failure logs into likely causes.
import re, collections
logs = """2026-10-01T10:00Z client=10.0.4.7 err=handshake_timeout size_clienthello=1530 path=proxy-b
2026-10-01T10:01Z client=10.0.4.9 err=handshake_timeout size_clienthello=1530 path=proxy-b
2026-10-01T10:02Z client=10.0.7.2 err=no_shared_group offered=x25519mlkem768
2026-10-01T10:03Z client=10.0.4.8 err=handshake_timeout size_clienthello=1530 path=proxy-b
2026-10-01T10:04Z client=10.0.9.1 err=bad_certificate alg=mldsa65
2026-10-01T10:05Z client=10.0.4.3 err=handshake_timeout size_clienthello=300 path=direct""".splitlines()
causes = collections.Counter()
for line in logs:
    f = dict(re.findall(r"(\w+)=(\S+)", line))
    if f["err"] == "handshake_timeout" and int(f.get("size_clienthello", 0)) > 1400: c = "large ClientHello dropped (" + f["path"] + ")"
    elif f["err"] == "no_shared_group": c = "client/server group mismatch"
    elif f["err"] == "bad_certificate": c = "client cannot verify PQ certificate"
    else: c = "other / investigate"
    causes[c] += 1
for c, n in causes.most_common(): print(f"{n}  {c}")
```

Saída esperada:

```text
3  large ClientHello dropped (proxy-b)
1  client/server group mismatch
1  client cannot verify PQ certificate
1  other / investigate
```

Três timeouts compartilham um proxy e uma primeira mensagem grande: o proxy é a causa provável. A incompatibilidade de grupos e o erro de certificado precisam de tickets separados.

O script lê seis linhas de log sintéticas e atribui cada uma a uma causa provável usando regras simples: um timeout com primeira mensagem acima de 1.400 bytes aponta para uma mensagem grande sendo descartada, enquanto os erros de grupo e de certificado se associam diretamente. O último timeout teve uma mensagem pequena num caminho direto, então fica para investigação. Repare como agrupar pelo caminho mostra que o proxy-b é o fator comum. Acrescente uma linha sua e confira o resultado.

### 13.3 Correções típicas

Proxy ou firewall descarta mensagens grandes → atualização de firmware ou correção de configuração nesse dispositivo; enquanto isso, encaminhe os usuários afetados para um listener compatível. Nenhum grupo compartilhado → restaure o fallback clássico no servidor ou atualize o cliente. Falha na verificação do certificado → acrescente a nova raiz ao repositório de confiança do cliente ou mantenha o certificado clássico para esse grupo de clientes. Fallback silencioso → corrija a ordem dos grupos e acrescente um alerta.

Escolha a correção mais estreita que restaure o serviço e registre qualquer passo provisório como exceção com data de término. No HHG, o encaminhamento do Summit para um listener sem híbrido foi removido assim que o firmware do firewall foi atualizado.

### 13.4 Registro

Escreva os sintomas, as evidências, a causa, a correção, a verificação e o que ficar pendente. Vincule os tickets relacionados, para que os padrões fiquem visíveis: três unidades com o mesmo modelo de firewall devem virar um único caso com o fornecedor.

No HHG, o ticket do Summit registrou os timeouts, a reprodução no laboratório, o encaminhamento provisório, a correção de firmware e a confirmação. Se outra unidade relatar os mesmos sintomas, os tickets vinculados mostram o padrão de imediato, e o caso com o fornecedor pode cobrir todos os sites afetados. Feche-o somente após a verificação.

### 13.5 Caso resolvido

Ticket: "A recepção do Summit não consegue carregar o portal do hóspede desde segunda-feira." Evidências: timeouts apenas a partir do Summit; uma triagem no estilo do Laboratório H mostra ClientHello grande através do firewall da unidade. Um teste de laboratório com o mesmo firmware de firewall a reproduz. Provisório: uma política encaminha a sub-rede da recepção do Summit para um listener sem o grupo híbrido, registrada como exceção. Correção: atualização do firmware do firewall na quinta-feira; exceção removida; negociações híbridas a partir do Summit confirmadas.

O operador reproduziu a falha antes de corrigi-la e manteve a medida provisória estreita e registrada.

### 13.6 Atividade prática

Usando a saída do Laboratório H, escreva três tickets — um por causa distinta — com as primeiras verificações.

Escreva um ticket para os timeouts do proxy-b, um para a incompatibilidade de grupos e um para o erro de certificado. Para cada um, informe os sintomas com as linhas de log, uma causa provável marcada como tal, as primeiras verificações para confirmá-la, a medida provisória estreita, se necessária, e o responsável. Anote separadamente o único timeout de caminho direto como item a investigar. Vincule os tickets se suspeitar de uma causa comum.

### 13.7 Pedindo ajuda

Escale quando a causa estiver fora do seu controle ou a correção exigir uma mudança que você não está autorizado a fazer. Inclua as evidências, o que você tentou e o que precisa. Bons escalonamentos são curtos, específicos e reproduzíveis; eles são respondidos mais rápido.

No HHG, a correção do firewall do Summit precisava do Network Ops e do fornecedor do firewall, então o operador escalou com a reprodução de laboratório e a versão do firmware anexadas. Diga o que você já descartou, para que quem ajuda não repita as suas verificações. Combine quando você terá retorno.

### 13.8 Erros comuns e limites

- Desligar o híbrido em todos os lugares.
- Mudar várias configurações de uma vez.
- Correções sem verificação.

Cada erro piora o diagnóstico. Desligar o híbrido em todos os lugares por causa de um caminho, como o firewall do Summit, remove a proteção de todas as outras unidades. Mudar várias configurações de uma vez significa que ninguém sabe qual mudança resolveu o problema ou causou um novo. Uma correção sem verificação pode não funcionar, e o ticket será reaberto. Confira todo ticket de diagnóstico quanto aos três antes de fechá-lo. Corrija o que encontrar.

### Exercícios

- **EX037 — Triagem.** No Laboratório H, qual causa você investigaria primeiro, e por quê? Rubrica: 3 = os timeouts do proxy, mais frequentes e com padrão comum.
- **EX038 — Correção provisória.** Descreva uma correção provisória estreita para o problema do Summit. Rubrica: 3 = encaminhar a sub-rede para um listener compatível, com exceção e expiração.
- **EX039 — Escalonamento.** Escreva um escalonamento de três linhas para o fornecedor do firewall. Rubrica: 3 = produto/versão, evidências, pedido.

### Síntese

O diagnóstico metódico, a triagem de logs e as correções provisórias estreitas resolvem problemas pós-quânticos mantendo a proteção para todos os demais.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 18

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Segurança quântica e pós-quântica: automação

### Objetivos de aprendizagem

Você vai (1) automatizar verificações rotineiras da negociação e da configuração; (2) usar limites de confiança para decidir quando uma etapa de implantação é segura; (3) agendar verificações após patches; e (4) manter os scripts fáceis de manter.

### 14.1 Verificações rotineiras

Agende scripts para: executar diariamente uma verificação de cliente contra cada serviço no escopo; analisar os logs quanto à proporção híbrida; auditar as exportações de configuração quanto à presença e à preferência. Envie os resultados ao painel e gere alertas quando houver mudanças.

No HHG, o job noturno contra 14 endpoints é um exemplo. Guarde os resultados com datas, para que cada execução possa ser comparada com a anterior, e garanta que todo alvo esteja no escopo. Gere alertas apenas para mudanças que exijam ação. Mantenha os scripts sob controle de versão junto com a sua lista de alvos e revise os dois juntos.

### 14.2 Atividade prática — Laboratório K

```python
# Lab K (ch 14): canary gate for enabling a hybrid group - promote only if failures stay within budget.
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

Quando uma mudança é implantada em etapas, a decisão de passar à etapa seguinte deve usar o limite superior de confiança da taxa de falhas, e não apenas a taxa observada. Uma amostra pequena pode parecer boa por sorte.

O script calcula um limite superior de Wilson da taxa de falhas em cada etapa e promove apenas se ele ficar dentro da linha de base mais a margem. A primeira etapa fica retida porque 5.000 conexões são poucas para haver confiança, mesmo que a taxa observada esteja boa. A etapa de 10 % é promovida. O site com proxy fica retido porque a sua taxa de falhas está claramente acima da margem, o que aponta para uma falha. Mude as contagens e veja quando cada decisão muda.

### 14.3 Após as janelas de patches

Execute automaticamente o conjunto completo de verificações após cada janela de patches e compare com a execução anterior. As diferenças vão para o operador de plantão.

No HHG, essa comparação encontrou dois endpoints que tinham passado de híbrido a clássico após um patch do balanceador de carga. Escreva a comparação de modo que uma diferença nomeie o endpoint, o resultado anterior e o novo, e inclua um link para o runbook. Guarde a saída completa de cada execução. Confira a saída antes da próxima janela de patches. Registre quem revisou cada diferença.

### 14.4 Scripts fáceis de manter

Controle de versão, um README, entradas e saídas claras, mensagens de erro que digam o que deu errado e um pequeno teste com entrada conhecida. Evite senhas embutidas no código; use o cofre de segredos aprovado.

No HHG, o script de verificação noturna é mantido sob controle de versão junto com a sua lista de alvos e uma entrada de teste. Revise as mudanças nos scripts da mesma forma que as mudanças de configuração e registre quem mantém cada script. Escreva mensagens de erro que digam o que deu errado e onde, para que o operador de plantão possa agir sem ler o código.

### 14.5 Caso resolvido

O HHG agenda um job noturno que executa verificações com `openssl s_client` contra 14 endpoints de homologação e de produção no escopo, extrai o grupo negociado e grava um CSV. Um diff com a noite anterior sinaliza dois endpoints que passaram de híbrido a clássico após um patch do balanceador de carga; o operador da manhã restaura o perfil.

O job encontrou uma regressão que não causou erros, e o operador da manhã pôde agir antes que hóspedes ou parceiros percebessem. O diff tornou a mudança óbvia sem que ninguém precisasse ler 14 conjuntos de saída.

### 14.6 Atividade prática

Escreva um script que leia uma lista de hosts de laboratório, execute uma verificação TLS em cada um e imprima o host e o grupo negociado.

Leia os hosts de um arquivo, um por linha, e execute `openssl s_client` contra cada um com um timeout. Extraia o grupo negociado da saída, imprima o host e o grupo e marque o host como desconhecido se a verificação falhar. Imprima o número de hosts lidos. Teste-o apenas nos seus hosts de laboratório. Acrescente um pequeno arquivo de teste com a saída esperada, para que um colega possa verificar o script depois de alterá-lo.

### 14.7 Automação e escopo

Verificações automatizadas continuam sendo verificações: precisam estar dentro do escopo escrito, rodar em horários combinados e parar se um alvo se comportar de forma inesperada. Mantenha a lista de alvos no repositório, revisada como código, para que ninguém acrescente por acidente um host fora do escopo.

No HHG, os 14 endpoints do job noturno estão na lista de alvos revisada, cada um com a sua referência de escopo. Revise a lista de alvos sempre que o escopo mudar e remova os hosts que não estiverem mais no escopo. Faça o job parar e alertar se um alvo responder de forma inesperada.

### 14.8 Erros comuns e limites

- Promover uma etapa com base numa amostra pequena e afortunada.
- Scripts com segredos embutidos.
- Listas de alvos não revisadas.

Cada erro cria risco. Promover uma etapa com base numa amostra pequena pode deixar uma falha chegar a todos os usuários, e é por isso que o Laboratório K usa um limite superior. Segredos embutidos em scripts vazam pelo controle de versão e pelos logs. Uma lista de alvos não revisada pode acrescentar um host fora do escopo, e o job então o testará todas as noites. Confira a sua automação quanto aos três antes de agendá-la. Corrija-os primeiro.

### 14.9 Qualidade dos alertas

Um alerta que dispara todas as noites por uma exceção conhecida e aceita ensina os operadores a ignorar alertas. Suprima explicitamente as exceções conhecidas, com uma data de expiração que coincida com o registro da exceção, e revise as supressões todo mês. Cada alerta deve ter um link para o seu runbook, para que a pessoa acordada às 03:00 saiba o que fazer primeiro.

No HHG, o listener provisório do Summit deve ser suprimido apenas até a sua exceção expirar. Registre cada supressão com o motivo e o responsável, e remova-a quando a exceção for encerrada. Conte a cada mês os alertas que não exigiram ação.

### Exercícios

- **EX040 — Decisão de etapa.** Usando o Laboratório K, explique por que o primeiro canário fica retido. Rubrica: 3 = limite superior acima da margem por causa da amostra pequena.
- **EX041 — Alerta por diff.** Descreva como um diff noturno detecta o fallback silencioso. Rubrica: 3 = comparar o grupo negociado por host, alertar em híbrido→clássico.
- **EX042 — Higiene de scripts.** Liste quatro características de um script de verificação fácil de manter. Rubrica: 3 = controle de versão, README, erros claros, teste.

### Síntese

A automação executa as verificações rotineiras, controla as etapas de implantação com limites de confiança, reverifica após patches e permanece dentro do escopo e fácil de manter.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 18

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Segurança quântica e pós-quântica: integração e dependências

### Objetivos de aprendizagem

Você vai (1) rastrear um fluxo por todos os saltos; (2) identificar quem controla cada salto; (3) preparar pedidos a fornecedores e parceiros; e (4) entender a agilidade por meio de política, e não de código.

### 15.1 Todo salto conta

Uma reserva de uma agência de viagem chega ao HHG pelo sistema da agência, pelo servidor de troca de arquivos, por um processador interno e pelo banco de dados de reservas. Cada salto negocia separadamente. Uma conexão híbrida num salto não diz nada sobre o seguinte.

No fluxo de reservas das agências, verifique cada salto e registre a sua evidência separadamente. Um número do painel para o servidor SFTP não cobre o processador interno nem a conexão com o banco de dados. Desenhe o fluxo com todos os saltos e marque quais têm evidência de troca de chaves híbrida e quais não têm.

### 15.2 Controladores

Escreva quem controla cada salto: as operações do HHG, um fornecedor, um provedor de nuvem ou um parceiro. O HHG pode mudar os seus próprios servidores; para o resto, só pode pedir, exigir em contrato ou contornar.

No fluxo de reservas dos canais, os clientes das agências são controlados pelos parceiros, o servidor SFTP e o processador interno pertencem ao HHG, e o banco de dados de reservas é um serviço gerenciado. Registre cada controlador com um contato e a via que o HHG pode usar para influenciá-lo. Mantenha a lista atualizada.

### 15.3 Pedidos

Um bom pedido a fornecedor ou parceiro nomeia o produto e a versão, pergunta quais algoritmos e protocolos pós-quânticos são suportados, a partir de qual versão e data, e pede um sistema de teste. Registre as respostas como evidência do fornecedor até que sejam verificadas.

No HHG, o pedido ao provedor do banco de dados gerenciado nomearia o nível de serviço, perguntaria sobre a troca de chaves híbrida nas conexões de clientes e pediria datas e um endpoint de teste. Guarde uma cópia de cada pedido e defina uma data de acompanhamento. Classifique as respostas como evidência do fornecedor.

### 15.4 Atividade prática — Laboratório A

```python
# Lab A (ch 15): crypto-agility through a policy-driven registry instead of hard-coded algorithms.
import hashlib, hmac
REGISTRY = {"hmac-sha256": lambda k, m: hmac.new(k, m, hashlib.sha256).digest(),
            "hmac-sha3-256": lambda k, m: hmac.new(k, m, hashlib.sha3_256).digest()}
POLICY = {"tag-algorithm": "hmac-sha256", "accept": ["hmac-sha256", "hmac-sha3-256"]}
def protect(key, msg):
    alg = POLICY["tag-algorithm"]; return alg, REGISTRY[alg](key, msg)
def check(key, msg, alg, tag):
    if alg not in POLICY["accept"]: return False            # algorithm identifier is authenticated by policy
    return hmac.compare_digest(REGISTRY[alg](key, msg), tag)
k, m = b"k" * 32, b"guest folio 42"
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

Sistemas que leem as escolhas de algoritmo de uma política conseguem mudá-las sem alterar o código. Quando perguntar aos fornecedores sobre a prontidão, pergunte se os algoritmos são configuráveis.

O script guarda o nome do algoritmo junto de cada tag e escolhe os algoritmos a partir de uma política, e não do código. Mudar a política faz as novas tags passarem a SHA3-256 enquanto as tags antigas continuam sendo verificadas, e remover o algoritmo antigo da lista de aceitos o aposenta de forma limpa. É isso que significa criptoagilidade na prática. Pergunte se o produto de um fornecedor funciona assim antes de comprá-lo.

### 15.5 Caso resolvido

O fluxo de SFTP dos canais: cliente da agência de viagem (parceiro) → servidor SFTP do HHG (HHG) → processador interno (HHG) → banco de dados de reservas (provedor do serviço gerenciado). Após atualizar o OpenSSH e habilitar o KEX híbrido, 5 de 9 agências negociam híbrido; quatro usam clientes antigos. O HHG envia a elas um aviso com um endpoint de teste e um prazo de doze meses.

O fluxo mostra que uma atualização no HHG protege apenas parte do caminho. Cinco agências se beneficiam agora; as outras quatro dependem das atualizações dos seus próprios clientes. Cada salto e a sua evidência entram na lista de dependências.

### 15.6 Atividade prática

Rastreie um fluxo do HHG com todos os saltos e controladores e redija um pedido a fornecedor.

Escolha um fluxo, como as reservas das agências ou os logins no portal do hóspede. Liste cada salto com o seu protocolo, controlador e evidência. Depois redija um pedido a fornecedor para um salto que o HHG não controla: nomeie o produto e a versão, pergunte quais algoritmos e protocolos pós-quânticos são suportados, a partir de qual versão e data, e peça um sistema de teste. Registre o tipo de resposta esperado. Confira-o com um colega.

### 15.7 Acompanhando as dependências

Mantenha uma lista de dependências simples: salto, controlador, pedido enviado, resposta, grau da evidência, próxima data de acompanhamento. Revise-a todo mês. Dependências que nunca recebem resposta são riscos a levar ao seu gestor, não tarefas a esquecer.

Quando chegar uma resposta, atualize o grau da evidência e a CBOM juntos. No HHG, a lista inclui as quatro agências com clientes SFTP antigos, com as datas dos avisos e o prazo de doze meses, e o pedido ao provedor do banco de dados gerenciado. Remova uma entrada somente quando o salto estiver verificado ou a dependência for formalmente aceita.

### 15.8 Erros comuns e limites

- Julgar um fluxo por um único salto.
- Tratar as alegações dos fornecedores como fatos.
- Nenhum acompanhamento de pedidos sem resposta.

Cada erro deixa riscos sem ser vistos. Julgar o fluxo das agências apenas pelo salto SFTP deixaria de fora o banco de dados gerenciado. A alegação de um fornecedor não é evidência até ser testada. Um pedido sem data de acompanhamento tende a ser esquecido, deixando o salto desprotegido sem que ninguém tenha decidido isso. Confira a sua lista de dependências quanto aos três todo mês. Corrija o que encontrar. Anote qualquer pedido que espere há mais de um mês.

### 15.9 Contornando uma dependência

Quando um controlador não puder ou não quiser mudar em breve, às vezes o HHG consegue proteger os dados de outra forma: mover a parte sensível de uma transferência para um canal que o HHG controla, reduzir o que é enviado ou terminar uma conexão híbrida num gateway do HHG próximo ao parceiro. Cada contorno precisa de aprovação e de uma entrada no registro de exceções, porque muda o desenho do serviço.

Registre a data de término de cada contorno. No HHG, o listener provisório do Summit foi uma mudança desse tipo e ficou registrado como exceção até que o firewall fosse corrigido.

### Exercícios

- **EX043 — Lista de saltos.** Liste os saltos e controladores do fluxo do portal do hóspede. Rubrica: 3 = cliente, CDN/balanceador, aplicação, banco de dados, com os controladores.
- **EX044 — Pedido a fornecedor.** Escreva um pedido de quatro perguntas ao fornecedor sobre o hub das fechaduras. Rubrica: 3 = algoritmos, protocolos, versão/data, sistema de teste.
- **EX045 — Pergunta de agilidade.** Por que perguntar aos fornecedores se os algoritmos são configuráveis? Rubrica: 3 = mudança futura sem substituição.

### Síntese

Integração significa cada salto e o seu controlador; os operadores enviam pedidos precisos, acompanham as respostas e dão preferência a produtos configuráveis.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 18

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Documentação técnica e segurança

### Objetivos de aprendizagem

Você vai (1) escrever runbooks para as operações pós-quânticas; (2) documentar linhas de base de configuração; (3) seguir as regras de segurança e de autorização; e (4) manter a documentação atualizada.

### 16.1 Runbooks

Um runbook diz: quando usá-lo (sintomas), o que verificar, as ações seguras, a reversão, como confirmar, a quem ligar. Escreva runbooks para quedas da proporção híbrida, timeouts de handshakes grandes, ausência de grupo compartilhado e erros de verificação de certificado.

No HHG, o runbook de queda da proporção híbrida é um exemplo. Mantenha cada runbook curto o bastante para ser seguido durante uma indisponibilidade e teste-o no laboratório antes de confiar nele. Nomeie um responsável por cada runbook e a data da última revisão. Vincule cada um aos alertas que devem acioná-lo.

### 16.2 Linhas de base

Uma linha de base de configuração lista as configurações aprovadas para cada tipo de serviço: versões do TLS, grupos e ordem, `KexAlgorithms` do SSH, tipos de certificado, campos de log. Guarde-a sob controle de versão; as mudanças passam por revisão.

No HHG, a linha de base contém a ordem de grupos aprovada `X25519MLKEM768:X25519:secp256r1` para o TLS e o `KexAlgorithms` com o híbrido primeiro para o SSH. A reversão da API de reservas a usou. Compare regularmente as configurações em execução com a linha de base e trate qualquer diferença como constatação. Registre cada mudança na linha de base com o seu motivo.

### 16.3 Segurança e autorização

Nunca execute testes ativos em produção sem aprovação por escrito; nunca tente forçar downgrades fora do laboratório isolado; nunca manuseie chaves fora das ferramentas aprovadas; comunique imediatamente chaves expostas. Rotule os dados sintéticos como tal em todos os documentos e materiais de treinamento.

No HHG, os testes de falha de tamanho foram feitos no laboratório isolado, não no firewall de produção do Summit. Se uma tarefa parecer exigir um teste ativo em produção, pare e peça primeiro a aprovação por escrito, e guarde a aprovação com as evidências. Comunique abertamente as violações dessas regras.

### 16.4 Mantendo os documentos atualizados

Revise os runbooks após cada incidente e cada mudança importante. Coloque no topo a data da "última revisão" e o responsável. Remova os passos que não se aplicam mais.

No HHG, o incidente do Summit deve levar a uma revisão do runbook de handshakes grandes. Registre cada mudança com um motivo, para que os leitores saibam por que um passo existe. Um documento que ninguém revisou por um ano deve ser tratado como pouco confiável até ser verificado. Atribua cada revisão a um responsável nomeado e registre a data em que foi feita.

### 16.5 Caso resolvido

Runbook do HHG "Queda da proporção híbrida num serviço TLS": sintomas — alerta do painel, proporção híbrida abaixo de 50 %; verificações — última mudança no serviço, perfil TLS atual versus a linha de base; ações — reaplicar o perfil da linha de base no listener afetado; reversão — perfil anterior do controle de versão; confirmação — a proporção híbrida se recupera em até 30 minutos; contatos — plantão do Web Ops, depois o líder de plataforma. Última revisão em 2 de outubro; responsável: Web Ops.

O runbook está completo: cada parte responde, em ordem, a uma pergunta que o operador de plantão terá. A confirmação em 30 minutos dá um ponto de parada claro.

### 16.6 Atividade prática

Escreva um runbook para "Nenhum grupo compartilhado no SFTP" usando o formato acima.

Use os mesmos títulos: sintomas, verificações, ações, reversão, confirmação e a quem ligar. Baseie as verificações no que você aprendeu: o `KexAlgorithms` do servidor contra a linha de base, a versão do cliente e a última mudança. Mantenha a ação estreita, por exemplo restaurar o fallback clássico apenas no servidor SFTP. Acrescente um responsável e uma data de revisão, e teste o runbook no laboratório antes de entregá-lo. Peça a um colega que o siga.

### 16.7 Escrevendo para o turno da noite

Os runbooks são lidos sob pressão, muitas vezes à noite. Use passos curtos e numerados, comandos exatos, saídas esperadas e pontos de parada claros ("se a proporção não tiver se recuperado após o passo 4, ligue para o líder de plataforma"). Evite explicações longas nos passos; vincule o contexto em outro lugar.

No HHG, o runbook de queda da proporção híbrida informa o ponto de confirmação de 30 minutos e nomeia a quem ligar em seguida. Teste cada runbook com alguém que não o escreveu, de preferência no laboratório ao fim de um turno, e corrija qualquer passo que tenha feito a pessoa hesitar.

### 16.8 Erros comuns e limites

- Runbooks sem reversão.
- Linhas de base guardadas apenas na cabeça de alguém.
- Documentos desatualizados.

Cada erro deixa a equipe exposta. Um runbook sem reversão deixa o operador de plantão sem saída quando uma correção falha. Uma linha de base guardada na cabeça de alguém desaparece quando a pessoa está ausente, e as configurações se desviam. Um documento desatualizado pode levar as pessoas a passos que não funcionam mais ou são inseguros. Confira cada runbook e cada linha de base quanto aos três a cada revisão. Corrija o que encontrar. Registre quando cada um foi verificado pela última vez e por quem.

### 16.9 Compartilhando a documentação

Guarde os runbooks e as linhas de base onde a equipe de plantão consiga alcançá-los durante uma indisponibilidade — não apenas num sistema que possa ele mesmo estar fora do ar. Muitas equipes mantêm uma cópia somente leitura num segundo local. Marque os documentos que contêm detalhes sensíveis de configuração e restrinja-os de acordo, mantendo os procedimentos gerais amplamente legíveis.

Revise o acesso aos documentos restritos quando as pessoas mudarem de função. No HHG, o runbook de queda da proporção híbrida seria necessário durante uma indisponibilidade do balanceador de carga, então uma cópia precisa ser alcançável sem ele. Teste o acesso ao segundo local duas vezes por ano.

### Exercícios

- **EX046 — Runbook.** Escreva o runbook de "nenhum grupo compartilhado". Rubrica: 3 = sintomas, verificações, ações, reversão, confirmação, contatos.
- **EX047 — Linha de base.** Liste cinco itens de uma linha de base de TLS. Rubrica: 3 = versões, grupos/ordem, tipos de certificado, log, suítes de cifras.
- **EX048 — Regra de segurança.** Explique por que os testes de downgrade pertencem apenas ao laboratório. Rubrica: 3 = risco para as sessões de produção, autorização.

### Síntese

Runbooks, linhas de base e regras de segurança transformam a habilidade individual em operações confiáveis da equipe; os documentos só continuam úteis quando têm responsável e são revisados.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 18

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Laboratório controlado II

### Objetivos de aprendizagem

Você vai (1) executar um laboratório de múltiplos saltos com monitoramento; (2) injetar e diagnosticar falhas; (3) praticar runbooks sob pressão de tempo; e (4) fazer o debriefing e melhorar os documentos.

### 17.1 Layout do laboratório

Cliente → proxy reverso → servidor web, mais um servidor SSH, todos capazes de híbrido; um parser de logs alimentando um painel simples; um cliente "legado"; e um proxy que pode ser configurado para descartar primeiras mensagens grandes.

Monte-o a partir do laboratório do Capítulo 12, acrescentando o proxy, o parser de logs e o painel. Registre todas as versões. O proxy que descarta mensagens grandes reproduz com segurança o problema do Summit do HHG. Tire um snapshot do laboratório funcionando, para poder restaurá-lo entre os cenários. Rotule claramente cada host de laboratório como laboratório.

### 17.2 Cenários

O instrutor (ou um colega de equipe) injeta uma falha de cada vez: reordenar os grupos no proxy; restringir o buffer do proxy; remover o fallback clássico no SSH; substituir o certificado do servidor por um emitido por uma raiz de laboratório não confiável. Você diagnostica com logs e ferramentas e corrige usando os runbooks.

Cada cenário corresponde a um modo de falha do Capítulo 8: fallback silencioso, mensagem grande descartada, nenhum grupo compartilhado e falha de certificado. Registre os sintomas que você vê, o runbook que usou e se ele funcionou. Restaure o laboratório à sua linha de base antes do cenário seguinte.

### 17.3 Tempos

Registre o tempo para detectar, o tempo para diagnosticar e o tempo para corrigir. O objetivo não é a velocidade em si, mas descobrir quais passos do runbook o atrasaram.

Meça desde o momento em que a falha foi injetada até quando você a percebeu, depois até quando você soube a causa, depois até quando o serviço foi restaurado e verificado. Um tempo de diagnóstico longo costuma significar uma verificação ausente ou um passo confuso no runbook. Compare os tempos entre as sessões. Anote qual passo levou mais tempo.

### 17.4 Debriefing

Após cada cenário: o que aconteceu, o que você fez, o que ajudou, o que mudar no runbook ou no painel. Atualize os documentos imediatamente.

No HHG, o debriefing após o cenário do buffer do proxy acrescentou um passo e um painel de visualização. Mantenha os debriefings curtos e sem culpados, com foco nos documentos e nas ferramentas, e não em quem foi lento. Registre cada mudança com o cenário que a causou. Teste cada runbook atualizado na sessão seguinte para confirmar que ele ajuda. Compartilhe as mudanças com a equipe.

### 17.5 Caso resolvido

Cenário 2 (buffer do proxy): detecção em 3 minutos (timeouts nos logs), diagnóstico em 11 minutos (o operador suspeitou primeiro do servidor), correção em 2 minutos (configuração do proxy restaurada). Debriefing: acrescentar ao runbook "verificar o proxy antes do servidor quando aparecerem timeouts num único caminho"; acrescentar ao painel visualizações por caminho.

O debriefing transformou um diagnóstico de 11 minutos em duas melhorias concretas. O operador suspeitou primeiro do servidor, o que custou tempo; o novo passo do runbook e as visualizações por caminho fazem do proxy a primeira coisa verificada. Registre os tempos, para que as sessões seguintes possam mostrar se as mudanças ajudaram.

### 17.6 Atividade prática

Execute os quatro cenários; registre os tempos e as notas do debriefing.

Execute os quatro cenários em sequência: grupos reordenados no proxy, buffer do proxy restrito, fallback clássico removido no SSH e uma raiz de laboratório não confiável no servidor. Para cada um, registre os tempos para detectar, diagnosticar e corrigir, o runbook usado e o que o atrasou. Restaure o laboratório entre os cenários. Termine com uma lista de mudanças nos runbooks ou no painel e faça-as antes da sessão seguinte. Compartilhe a lista com o seu instrutor.

### 17.7 Trabalhando em dupla

Pratique em duplas: um operador conduz, o outro lê o runbook e registra os tempos e as observações. Troquem os papéis a cada cenário. O trabalho em dupla expõe rapidamente os passos pouco claros e espelha a forma como os incidentes são tratados nas escalas reais de plantão.

Registre no debriefing as observações dos dois papéis. Quem lê deve seguir o runbook exatamente como está escrito, para que os passos pouco claros ou ausentes fiquem visíveis, em vez de serem completados de memória. Combinem antes de cada cenário quem conduz e quem lê, e registrem qualquer passo que o leitor teve de explicar.

### 17.8 Erros comuns e limites

- Pular os debriefings.
- Corrigir sem diagnosticar.
- Não atualizar os documentos após as lições.

Cada erro desperdiça o exercício. Pular os debriefings significa que os mesmos passos vão atrasá-lo da próxima vez. Corrigir sem diagnosticar, por exemplo restaurar a configuração do proxy sem conferir os logs, não ensina nada e pode esconder uma segunda falha. Não atualizar os documentos deixa a lição na sua cabeça em vez de no runbook, onde o turno da noite precisa dela. Confira cada sessão quanto aos três. Corrija o que encontrar. Anote o que você mudou em cada runbook após a sessão.

### 17.9 Registrando o exercício

Mantenha um registro curto de cada sessão de laboratório — data, cenários, tempos, ações do debriefing e quem participou — no repositório da equipe. Ao longo de várias sessões, o registro mostra se os tempos de detecção e de correção estão melhorando e quais runbooks mudaram em consequência. Ele também é evidência, para supervisores e auditores, de que a equipe pratica os seus procedimentos em vez de apenas escrevê-los.

Mantenha o registro factual e breve. Revise-o a cada trimestre. Compartilhe um resumo com a equipe após cada sessão, para que as lições cheguem aos operadores que não participaram.

### Exercícios

- **EX049 — Plano de cenário.** Projete um quinto cenário para o laboratório. Rubrica: 3 = injeção realista, sintoma esperado, correção.
- **EX050 — Análise dos tempos.** No caso resolvido, qual fase levou mais tempo e como você a encurtaria? Rubrica: 3 = diagnóstico; ordem do runbook/visualizações.
- **EX051 — Cenário de certificado.** Que sintoma e que correção você espera no cenário da raiz de laboratório não confiável? Rubrica: 3 = erro de verificação; acrescentar a raiz ou restaurar o certificado confiável.

### Síntese

Laboratórios de múltiplos saltos com falhas injetadas e prática de runbooks cronometrada e com debriefing formam operadores capazes de encontrar e corrigir problemas rapidamente e de melhorar as suas ferramentas.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 18

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Projeto técnico supervisionado

### Objetivos de aprendizagem

Você vai (1) planejar e concluir um projeto de operações supervisionado; (2) aplicar verificações, configuração, verificação e documentação de ponta a ponta; (3) relatar os resultados com evidências; e (4) fazer a passagem para a equipe.

### 18.1 Escolhas de projeto

Exemplos: habilitar e verificar a troca de chaves híbrida num serviço, na homologação e na produção, sob supervisão; construir o painel de grupos negociados para um conjunto de serviços; escrever e testar runbooks para os modos de falha pós-quânticos; construir a CBOM de uma unidade.

No HHG, o projeto do SFTP dos canais, no caso resolvido abaixo, é uma escolha típica. Escolha um projeto pequeno o bastante para terminar sob supervisão, com uma forma clara de verificar o seu resultado, e combine-o com o seu supervisor antes de começar. Anote o resultado esperado.

### 18.2 Plano

Escopo e autorização; passos com evidências para cada um; riscos e reversão; cronograma; pontos de controle com o supervisor.

Escreva o plano em uma página. Nomeie a referência de escopo, liste os passos com a evidência que cada um vai produzir, declare os riscos e a reversão de cada mudança e defina datas para os pontos de controle com o supervisor. No projeto do SFTP dos canais, isso inclui a atualização na homologação, os testes de clientes, o ticket de produção e o aviso aos parceiros. Obtenha a aprovação por escrito antes de começar. Revise o plano se o escopo mudar. Guarde o plano aprovado com as suas evidências.

### 18.3 Execução

Siga o controle de mudanças; salve as evidências; verifique dos dois lados; atualize os documentos. Peça ajuda cedo quando estiver bloqueado.

Mantenha um registro datado do que você fez e de quais evidências foram salvas. No HHG, o projeto do SFTP dos canais seguiu o controle de mudanças para a mudança em produção e verificou dos lados do cliente e do servidor. Atualize os runbooks e o painel à medida que avança, não no final. Se um passo falhar, pare e registre-o antes de tentar de novo. Registre qualquer desvio do plano.

### 18.4 Relatório e passagem

Relatório: objetivo, o que foi feito, evidências, resultados, questões pendentes e recomendações. Passagem: runbooks, scripts, painéis e a lista de itens em aberto, cada um com um responsável.

No HHG, a passagem do SFTP dos canais para o Network Ops listou as quatro agências como itens em aberto. Verifique se todo item em aberto tem um responsável e uma data antes da passagem e peça à equipe que recebe que confirme que aceita cada um. Mantenha o relatório factual e inclua a evidência por trás de cada resultado. Guarde uma cópia com as evidências do seu projeto.

### 18.5 Caso resolvido

Projeto (sintético): "SSH híbrido para o SFTP dos canais." Passos: atualizar o OpenSSH na homologação; configurar `KexAlgorithms`; testar seis tipos de cliente das agências; mudança em produção sob ticket; verificar; visualização no painel para a proporção de KEX; runbook de "nenhum grupo compartilhado"; aviso aos parceiros. Resultados: 5 de 9 agências em híbrido após um mês; quatro sob aviso. Passagem para o Network Ops com itens em aberto para as quatro agências.

O projeto produziu resultados duradouros: configuração, uma visualização no painel, um runbook e um aviso aos parceiros. A passagem deixa claro quem acompanha as quatro agências.

### 18.6 Atividade prática

Escreva o plano do seu projeto e obtenha a aprovação do seu supervisor.

Use o formato do plano: referência de escopo, passos com evidências, riscos e reversão, cronograma e pontos de controle com o supervisor. Escolha um projeto entre os exemplos ou proponha um de tamanho semelhante. Mantenha-o em uma página. Peça ao seu supervisor que o revise, registre os comentários e como você os tratou, e guarde a versão aprovada com as evidências do seu projeto. Revise-o uma vez após o retorno. Anote qual projeto você escolheu e por que ele cabe no tempo disponível.

### 18.7 Refletindo sobre o projeto

Termine com uma reflexão curta: o que saiu conforme o planejado, o que o surpreendeu, qual habilidade você mais usou e o que faria diferente. Compartilhe-a com o seu supervisor; muitas vezes ela é a contribuição mais útil para o projeto do próximo trainee.

Mantenha-a curta e honesta, com exemplos. No HHG, uma reflexão sobre o projeto do SFTP dos canais poderia notar que quatro agências precisaram de mais tempo do que o esperado e que um contato mais cedo com os parceiros teria ajudado. Escreva-a logo depois de terminar, enquanto os detalhes estão frescos.

### 18.8 Erros comuns e limites

- Começar sem aprovação.
- Relatórios sem evidências.
- Passagens sem responsáveis.

Cada erro compromete o projeto. Começar sem aprovação coloca as mudanças fora do escopo e pode encerrar a sua autorização. Um relatório sem evidências não consegue mostrar o que foi alcançado, por melhor que o trabalho tenha ido. Uma passagem sem responsáveis deixa itens em aberto, como as quatro agências com clientes antigos, sem ninguém para acompanhá-los. Confira o seu projeto quanto aos três antes de apresentá-lo. Corrija o que encontrar. Anote qualquer correção no relatório.

### 18.9 Avaliação

O seu supervisor vai avaliar o projeto quanto a: permanência dentro do escopo; qualidade das evidências; correção da configuração (híbrido preferido com fallback controlado); verificação dos dois lados com um controle negativo; utilidade da documentação; e a passagem. Antes da avaliação, confira cada item você mesmo e vincule as evidências. Saber mostrar onde está cada evidência faz parte da habilidade avaliada.

Por fim, apresente o projeto à sua equipe em dez minutos: o problema, o que você mudou, as evidências, o que falta e quem é responsável. Apresentações curtas e factuais de trabalhos concluídos são a forma como os operadores constroem confiança com as equipes cujos sistemas eles alteram.

### Exercícios

- **EX052 — Plano.** Escreva um plano de uma página para o projeto do painel. Rubrica: 3 = escopo, passos com evidências, riscos, cronograma, pontos de controle.
- **EX053 — Resultados.** Expresse "5 de 9 agências" como porcentagem e declare o que falta. Rubrica: 3 = 56 %, quatro agências sob aviso.
- **EX054 — Lista de passagem.** Liste cinco itens de passagem. Rubrica: 3 = runbooks, scripts, painéis, itens em aberto, responsáveis.

### Síntese

Um projeto supervisionado reúne todas as habilidades práticas — escopo, configuração, verificação, documentação e passagem — e deixa a equipe mais bem equipada.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 18

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. Os números sobre o HHG são sintéticos.

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

**EX028.** `X25519MLKEM768:X25519:secp256r1`

**EX029.** `KexAlgorithms mlkem768x25519-sha256,sntrup761x25519-sha512@openssh.com,curve25519-sha256`

**EX030.** O quê: habilitar o KEX híbrido no channel-sftp. Por quê: dados de reservas de 7 anos, risco de gravar agora. Quando: terça-feira às 06:00. Risco: clientes antigos das agências — fallback mantido. Evidência de teste: saídas de `ssh -v` da homologação para seis clientes. Reversão: restaurar o sshd_config anterior do controle de versão e recarregar. Aprovador: líder do Network Ops.

**EX031.** Cliente: saída da ferramenta mostrando o grupo negociado. Servidor: logs de acesso/TLS com o campo do grupo.

**EX032.** Na homologação, remover `mlkem768x25519-sha256` de `KexAlgorithms`; a verificação precisa relatar clássico; restaurar e reverificar.

**EX033.** Executar a verificação de cliente contra os serviços no escopo; conferir o painel/os logs quanto à proporção híbrida; comparar com a linha de base anterior ao patch e alertar sobre as diferenças.

**EX034.** VM servidor (OpenSSL atual ≥ 3.5, OpenSSH atual); VM do cliente atual (idem); VM do cliente antigo (OpenSSL/OpenSSH mais antigos); rede isolada; versões registradas.

**EX035.** Colocar o grupo clássico primeiro na lista do servidor (`X25519:X25519MLKEM768`); conectar com o cliente atual e observar o X25519 negociado, embora o híbrido seja oferecido.

**EX036.** Propósito; ambiente; passos; resultados; interpretação; lições.

**EX037.** Os timeouts do proxy: três das seis falhas, um caminho comum e um padrão claro (ClientHello grande), afetando um site inteiro.

**EX038.** Encaminhar a sub-rede da recepção do Summit para um listener sem o grupo híbrido, registrado como exceção com responsável e expiração vinculada à atualização do firewall.

**EX039.** "Produto: firewall modelo X, firmware 5.2.1 no Summit. Evidência: ClientHello TLS de 1.530 bytes descartado (reprodução de laboratório anexada). Pedido: correção ou orientação de configuração e data prevista de versão."

**EX040.** 3/5.000 tem um limite superior de Wilson de cerca de 0,18 %, acima do limite de 0,09 % (linha de base mais margem); a amostra é pequena demais para mostrar segurança.

**EX041.** Guardar o grupo negociado de cada noite por host; fazer o diff com a noite anterior; alertar quando algum host passar de híbrido a clássico.

**EX042.** Controle de versão; README; mensagens de erro claras; um teste com entrada conhecida (também: nenhum segredo embutido).

**EX043.** Dispositivo do hóspede (hóspede) → CDN ou balanceador de carga (HHG ou provedor de CDN) → aplicação do portal (HHG) → banco de dados de reservas (HHG/provedor gerenciado).

**EX044.** Quais algoritmos o hub usa para a troca de chaves e para a assinatura do firmware? Ele suporta troca de chaves pós-quântica ou híbrida, e em qual protocolo? A partir de qual versão de firmware e data? Podemos obter uma unidade ou um sistema de teste?

**EX045.** Produtos configuráveis podem trocar de algoritmo por política mais tarde (inclusive em mudanças futuras), evitando a troca de hardware ou mudanças de código.

**EX046.** Sintomas: o parceiro relata "no shared group". Verificações: versão do cliente do parceiro; `KexAlgorithms` atual do sshd; mudanças recentes. Ações: restaurar a lista aprovada com fallback clássico. Reversão: configuração anterior. Confirmação: o parceiro se conecta; KEX nos logs. Contatos: plantão do Network Ops, contato do parceiro.

**EX047.** Versões do TLS (1.3, 1.2 se necessário); grupos e ordem; tipo de certificado; campos de log (protocolo, cifra, grupo); suítes de cifras.

**EX048.** Os testes de downgrade podem quebrar ou enfraquecer sessões reais de hóspedes e parceiros e exigem autorização explícita; um laboratório isolado evita danos.

**EX049.** Exemplo: configurar o servidor como somente híbrido e conectar com o cliente legado — sintoma "no shared group"; correção: restaurar o fallback clássico.

**EX050.** Diagnóstico (11 minutos); encurtar ordenando as verificações do runbook (proxy antes do servidor em timeouts de caminho único) e acrescentando visualizações por caminho ao painel.

**EX051.** Sintoma: erro de verificação de certificado nos clientes; correção: acrescentar a raiz de laboratório ao repositório de confiança do cliente (se for o pretendido) ou restaurar o certificado confiável.

**EX052.** Escopo: lista de serviços e fontes de log, aprovação. Passos: acrescentar os campos de log (evidência da homologação), parser, visualizações do painel, alertas. Riscos: volume de logs — implantação em etapas. Cronograma: quatro semanas. Pontos de controle: semanais com o supervisor.

**EX053.** 5/9 ≈ 56 %; quatro agências continuam no clássico, sob aviso com prazo de doze meses.

**EX054.** Runbooks; scripts; painéis; lista de itens em aberto; responsáveis nomeados para cada um.

## Rota de ensino de dezoito disciplinas

Este é o curso **técnico** para operadores práticos, que acompanha o **Halden Hotel Group (HHG)** sintético por verificações, configuração, verificação, diagnóstico de problemas, automação, documentação e laboratórios controlados.

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
