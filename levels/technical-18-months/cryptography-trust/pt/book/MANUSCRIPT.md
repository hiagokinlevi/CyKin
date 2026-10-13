# Criptografia e Serviços de Confiança: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 054, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–9 de 18 já estão escritos em português, com os exercícios EX001–EX036 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 10–18 (EX037–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: operadores técnicos.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios calculam hashes de arquivos, calculam expirações, inspecionam os padrões de TLS do Python, conferem o HMAC e o scrypt contra vetores publicados, contam motivos em logs e planejam rotações; não implementam nenhuma cifra. Sistemas de produção usam bibliotecas avaliadas, clientes ACME, cofres e HSMs; nunca crie sua própria criptografia. Pessoas, organizações e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um estudante do curso técnico pelos fundamentos de computação e de redes, por um estágio em operações de TI, por dois laboratórios isolados e por um projeto supervisionado: arquitetura, camadas de protocolo, arquivos de chave, formatos de dados, escopo e evidências, modelos de confiança, telemetria, modos de falha, ferramentas, configuração de TLS, verificação, solução de problemas, automação, integrações, documentação e armazenamento de senhas. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Tomás Reyes** | Estudante do curso técnico em estágio | Inventado |
| **Priya Nandakumar** | Técnica sênior e mentora | Inventada |
| **Eastbrook Technical Institute** | Escola fictícia | Inventada |
| **Lumen Freight Logistics** | Transportadora regional fictícia | Inventada |

### Fontes principais

[RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555); [RFC 4231](https://www.rfc-editor.org/rfc/rfc4231); [RFC 7914](https://www.rfc-editor.org/rfc/rfc7914); [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4); NIST [SP 800-52 Rev. 2](https://doi.org/10.6028/NIST.SP.800-52r2) e [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) |

Capítulos 10–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-10), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Computação e arquitetura de serviços

### Objetivos de aprendizagem

Você vai (1) descrever os serviços de uma empresa de logística e onde a criptografia fica dentro deles; (2) separar clientes, servidores e serviços gerenciados; (3) registrar quem controla cada chave.

### 1.1 O caso

Tomás Reyes é estudante do primeiro ano do curso técnico de dezoito meses do fictício Eastbrook Technical Institute. Seu estágio supervisionado é na equipe de operações de TI da fictícia Lumen Freight Logistics, uma transportadora regional com três depósitos, um portal de rastreamento de encomendas para os clientes, coletores portáteis para os motoristas e trocas noturnas de arquivos com armazéns parceiros. Sua mentora é a técnica sênior Priya Nandakumar. Todas as pessoas, sistemas, endereços e números deste livro são sintéticos. Um técnico diagnostica falhas, configura controles e prova que os controles funcionam, então Tomás vai passar a maior parte do tempo lendo configurações e logs, e não projetando algoritmos, e nunca vai escrever sua própria cifra.

### 1.2 Clientes, servidores e serviços

Priya pede que Tomás separe os sistemas da empresa em três grupos. Os clientes incluem os coletores dos motoristas, os notebooks do escritório e os navegadores que os clientes usam. Os servidores incluem o portal de rastreamento, um banco de dados interno e o host de transferência de arquivos. Os serviços gerenciados incluem a plataforma de e-mail, o processador de pagamentos e o armazenamento de backup em nuvem. A criptografia aparece nos três grupos: os notebooks usam cifração de disco completo, o portal termina o TLS, os backups são cifrados antes do envio e o processador de pagamentos assina os callbacks. Tomás aprende que o mesmo algoritmo, como o AES, pode ser bem configurado num servidor e mal configurado em outro, então o inventário precisa registrar a configuração, e não apenas os nomes.

### 1.3 Quem controla as chaves

Para cada sistema, Tomás acrescenta uma coluna chamada dono da chave. Nos servidores da empresa, a equipe de operações gera e guarda as chaves privadas, então um erro ali é um problema da Lumen a corrigir. Nos serviços gerenciados, o provedor guarda as chaves, e a Lumen só pode escolher as configurações que o provedor expõe e conferir os contratos e os relatórios de auditoria. Os coletores são um caso misto: o fornecedor do dispositivo instala uma lista de certificados raiz, enquanto a Lumen instala um certificado de cliente para o Wi-Fi dos depósitos. Saber quem é o dono diz a Tomás quem chamar quando algo quebra e evita que ele desperdice uma noite mudando uma configuração que só um fornecedor pode mudar.

### Exemplo resolvido

Tomás monta uma tabela de doze linhas com os sistemas da Lumen, com colunas para tipo, função criptográfica e dono da chave, e marca o armazenamento de backup e o processador de pagamentos como controlados pelo provedor.

> **Caso sintético.** A Lumen Freight Logistics, o Eastbrook Technical Institute, Tomás e Priya são inventados.

### Erros e limites

Um inventário é um retrato instantâneo; novos sistemas aparecem sem aviso. As chaves controladas por provedores ainda criam risco para a Lumen, por meio dos contratos e das indisponibilidades.

### Exercícios

- **EX001 — Papel no estágio.** Qual é o trabalho de Tomás na Lumen, em uma frase? *Rubrica:* 3 = diagnosticar falhas, configurar controles e verificar que funcionam; não projetar algoritmos;; 2 = papel parcial;; 1 = diz que ele projeta cifras;; 0 = nenhuma.

- **EX002 — Agrupar os sistemas.** Classifique o coletor do motorista, o portal de rastreamento e o processador de pagamentos como cliente, servidor ou serviço gerenciado. *Rubrica:* 3 = coletor cliente; portal servidor; processador de pagamentos serviço gerenciado;; 2 = dois corretos;; 1 = um correto;; 0 = nenhuma.

- **EX003 — O mesmo algoritmo duas vezes.** Por que registrar a configuração, e não apenas o nome do algoritmo? *Rubrica:* 3 = o mesmo algoritmo pode ser bem configurado num host e mal configurado em outro;; 2 = menciona configurações;; 1 = lista só nomes;; 0 = nenhuma.

- **EX004 — Valor do dono da chave.** Como saber quem é o dono da chave ajuda durante uma indisponibilidade? *Rubrica:* 3 = diz quem pode corrigir; evita mudar configurações que só um fornecedor controla;; 2 = quem chamar;; 1 = nenhum benefício;; 0 = nenhuma.

### Síntese

Um mapa útil da arquitetura de serviços nomeia cada sistema, sua função criptográfica e quem guarda as chaves.

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) rastrear uma requisição ao portal de rastreamento pelo DNS, pelo TCP e pelo TLS; (2) explicar o que cada camada protege; (3) associar os sintomas comuns à camada que falhou.

### 2.1 Uma requisição passo a passo

Quando um cliente abre track.lumen.example, o navegador primeiro pergunta um endereço ao DNS, depois abre uma conexão TCP com a porta 443, depois executa um handshake TLS e só então envia a requisição HTTP com o número da encomenda. Tomás desenha essas etapas como quatro caixas. Ele observa que o DNS simples não é cifrado nem autenticado, de modo que uma resposta forjada poderia mandar o navegador para o host errado. O TLS limita o dano: o impostor não consegue apresentar um certificado válido para o nome da Lumen, então o navegador para. É por isso que a validação de certificados nunca deve ser desligada, nem mesmo durante os testes.

### 2.2 O que cada camada protege

O TCP dá entrega ordenada, mas nenhum sigilo; qualquer um no caminho pode ler e alterar os dados TCP simples. O TLS 1.3, especificado na RFC 8446, acrescenta confidencialidade por meio de cifração autenticada, integridade de cada registro e autenticação do servidor por meio do seu certificado. Ele não esconde o endereço IP do servidor e, na maioria das implantações, o nome solicitado continua visível no handshake. Tomás anota isso porque um gerente certa vez afirmou que o TLS torna o tráfego invisível. Ser preciso sobre o que uma camada protege e o que não protege é o primeiro passo para diagnosticar uma falha corretamente.

### 2.3 Sintomas por camada

Priya entrega a Tomás uma lista de chamados da central de atendimento. Um nome que não resolve é um problema de DNS. Uma conexão que expira por tempo aponta para o roteamento ou para um firewall, na camada TCP. Um aviso do navegador sobre um certificado não confiável ou expirado é um problema de TLS. Uma página que carrega, mas mostra uma mensagem de erro, é um problema da aplicação. Separar os chamados por camada economiza tempo, porque cada camada tem ferramentas diferentes: dig ou nslookup para o DNS, um teste de porta para o TCP, um teste de handshake para o TLS e os logs do servidor para a aplicação.

### Exemplo resolvido

Tomás separa oito chamados sintéticos em DNS, TCP, TLS e aplicação e associa a cada um a primeira ferramenta de diagnóstico correspondente.

> **Caso sintético.** Os textos dos chamados e os nomes de host são inventados; a RFC 8446 é real.

### Erros e limites

Falhas reais podem atravessar camadas, como um firewall que quebra o TLS ao interceptá-lo. Separar por camada é uma hipótese inicial, e não um veredito.

### Exercícios

- **EX005 — Ordem das etapas.** Liste as quatro etapas antes que o número da encomenda chegue ao portal. *Rubrica:* 3 = consulta DNS, conexão TCP, handshake TLS, requisição HTTP;; 2 = três em ordem;; 1 = fora de ordem;; 0 = nenhuma.

- **EX006 — Resposta DNS forjada.** Por que uma resposta DNS forjada normalmente não consegue roubar uma sessão TLS? *Rubrica:* 3 = o impostor não consegue apresentar um certificado válido para o nome, então a validação falha;; 2 = menciona certificado;; 1 = diz que o DNS é cifrado;; 0 = nenhuma.

- **EX007 — Visível no TLS.** Dê duas coisas que o TLS não esconde de um observador no caminho. *Rubrica:* 3 = o endereço IP do servidor e, normalmente, o nome solicitado (SNI), além do tempo e do tamanho do tráfego;; 2 = um item;; 1 = afirma que tudo fica escondido;; 0 = nenhuma.

- **EX008 — Do chamado à camada.** Um chamado diz que o navegador mostra que o certificado expirou. Que camada, e que primeira ferramenta? *Rubrica:* 3 = camada TLS; executar um teste de handshake e ler as datas do certificado;; 2 = só a camada;; 1 = camada errada;; 0 = nenhuma.

### Síntese

Diagnosticar problemas de rede começa por saber qual camada protege o quê e qual ferramenta inspeciona cada camada.

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem

Você vai (1) localizar os repositórios de chaves e certificados em hosts Linux e Windows; (2) aplicar o privilégio mínimo aos arquivos de chave privada; (3) explicar como as contas de serviço usam identidades criptográficas.

### 3.1 Onde as chaves ficam

No host Linux de transferência de arquivos, Tomás encontra o certificado do servidor em /etc/ssl/certs e a chave privada num diretório que só o root e a conta de serviço podem ler. Nos notebooks Windows, os certificados ficam no repositório de certificados, que o sistema operacional protege com as credenciais do usuário ou da máquina. Os coletores guardam o certificado de cliente do Wi-Fi num repositório de chaves do fornecedor apoiado em hardware. Priya explica que a localização importa tanto quanto o algoritmo: uma chave RSA ou ECDSA forte num arquivo legível por todos não dá nenhuma proteção, porque qualquer um que copie o arquivo pode se passar pelo servidor.

### 3.2 Privilégio mínimo para arquivos de chave

Tomás confere as permissões no host de transferência de arquivos com ls -l e descobre que um script de backup tinha copiado a chave privada para /tmp com o modo 644, legível por todas as contas. Ele relata o problema, remove a cópia, e a equipe rotaciona a chave porque não consegue provar que ninguém a leu. A regra que ele escreve no caderno é que uma chave privada deve poder ser lida apenas pelo processo que precisa dela, pertencer a uma conta dedicada e nunca ser copiada para pastas compartilhadas, chamados ou chats. Uma exposição sem evidência de uso indevido ainda exige rotação.

### 3.3 Contas de serviço e identidade

Muitos serviços da Lumen rodam como contas não humanas. O portal de rastreamento roda como svc-portal, que precisa ler sua chave TLS e mais nada; o job noturno de transferência roda como svc-sftp e se autentica junto aos parceiros com uma chave SSH. Essas identidades são tão importantes quanto as senhas da equipe, mas costumam ser esquecidas quando as pessoas saem. Tomás acrescenta cada conta de serviço ao inventário, com sua chave, seu dono e a data em que a chave foi criada, para que os capítulos seguintes possam planejar a rotação. Ele também confirma que nenhuma das contas consegue fazer login interativo.

### Exemplo resolvido

Tomás audita as permissões dos arquivos de chave em dois hosts sintéticos, encontra a cópia 644 em /tmp e registra o chamado de rotação e a conta de serviço afetada.

> **Caso sintético.** Os nomes de host, os caminhos e as contas são exemplos inventados de organizações comuns.

### Erros e limites

As permissões de arquivo não impedem o root nem um serviço comprometido. Os repositórios apoiados em hardware reduzem as cópias, mas não o uso indevido por meio do dispositivo.

### Exercícios

- **EX009 — Chave forte, arquivo fraco.** Por que uma chave forte num arquivo legível por todos ainda é um problema? *Rubrica:* 3 = qualquer um que a copie pode se passar pelo servidor; a força do algoritmo é irrelevante;; 2 = menciona cópia;; 1 = diz que a força basta;; 0 = nenhuma.

- **EX010 — Resposta à cópia exposta.** O que a equipe fez com a cópia da chave em /tmp, e por que rotacionar? *Rubrica:* 3 = removeu a cópia e rotacionou, já que a exposição não pode ser descartada;; 2 = só removeu;; 1 = ignorou;; 0 = nenhuma.

- **EX011 — Escopo da conta do portal.** O que a svc-portal deve poder ler? *Rubrica:* 3 = apenas sua própria chave privada TLS e os arquivos de aplicação necessários; sem login interativo;; 2 = só a chave;; 1 = tudo;; 0 = nenhuma.

- **EX012 — Identidades esquecidas.** Por que acrescentar as contas de serviço e suas chaves ao inventário? *Rubrica:* 3 = costumam ser esquecidas; o inventário sustenta os donos e a rotação;; 2 = menciona acompanhamento;; 1 = nenhuma razão;; 0 = nenhuma.

### Síntese

A identidade criptográfica é tão forte quanto as permissões de arquivo e os limites de conta que protegem cada chave privada.

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem

Você vai (1) distinguir codificação, hash e cifração nos dados que encontra no dia a dia; (2) construir um manifesto de integridade SHA-256 com Python; (3) ler PEM e Base64 com segurança.

### 4.1 Codificação, hash, cifração

Tomás vê com frequência cadeias longas nos arquivos de configuração e precisa distingui-las. Base64 e hexadecimal são codificações: mudam a representação, e qualquer um pode revertê-las sem chave. Um hash como o SHA-256, especificado no FIPS 180-4, mapeia qualquer entrada num resumo fixo de 32 bytes e não pode ser revertido, mas qualquer um pode calculá-lo, então ele só prova integridade quando o próprio resumo esperado é confiável. A cifração precisa de uma chave para ser revertida. Certa vez, um colega chamou de cifrada uma senha em Base64; Tomás hoje explica que decodificá-la leva um comando e nenhum segredo.

### 4.2 Manifestos de integridade

Os arquivos noturnos dos parceiros chegam por SFTP, e de vez em quando uma transferência truncada passa despercebida. Priya sugere um manifesto: o remetente lista cada nome de arquivo com seu resumo SHA-256, e o destinatário recalcula e compara. Tomás escreve um pequeno script que faz isso sobre dados sintéticos. Um manifesto detecta de forma confiável a corrupção acidental. Contra um atacante capaz de alterar tanto o arquivo quanto o manifesto, ele não prova nada, então em produção o próprio manifesto precisa ser assinado ou entregue por um canal autenticado. O laboratório abaixo mostra tanto o caso de sucesso quanto uma alteração detectada.

### Laboratório — Verificação de manifesto SHA-256

```python
# Synthetic SHA-256 manifest check (FIPS 180-4 via hashlib). Teaching only.
import hashlib
files = {"routes_mon.csv": b"depot,route\nN1,12\nN2,7\n",
         "routes_tue.csv": b"depot,route\nN1,13\nN2,7\n"}
manifest = {n: hashlib.sha256(d).hexdigest() for n, d in files.items()}
files["routes_tue.csv"] = b"depot,route\nN1,18\nN2,7\n"   # simulated change in transit
for name, data in files.items():
    ok = hashlib.sha256(data).hexdigest() == manifest[name]
    print(f"{name}: {'OK' if ok else 'CHANGED'} {manifest[name][:16]}...")
```

Execute com `python3 lab_manifest.py`. Saída verificada:

```text
routes_mon.csv: OK 71e12cbcb1238386...
routes_tue.csv: CHANGED 03db2f9cd00a57f9...
```

### 4.3 Ler arquivos PEM

Certificados e chaves normalmente chegam em PEM: texto em Base64 entre linhas BEGIN e END. Tomás aprende a olhar o cabeçalho antes de qualquer outra coisa. BEGIN CERTIFICATE é público e pode ser compartilhado; BEGIN PRIVATE KEY ou BEGIN RSA PRIVATE KEY é secreto e nunca pode ser colado num chamado, num chat ou num decodificador online. Quando precisa inspecionar um certificado, ele usa ferramentas locais, e não sites. Decodificar o PEM mostra os bytes DER, que ferramentas como openssl x509 -text transformam em campos legíveis, como titular, emissor e datas de validade.

### Exemplo resolvido

Tomás executa o laboratório do manifesto, vê um arquivo de parceiro sinalizado como alterado e explica a Priya por que seria necessário um manifesto assinado contra um atacante deliberado.

> **Caso sintético.** Os nomes e os conteúdos dos arquivos no laboratório são sintéticos.

### Erros e limites

Manifestos de hash não autenticam o remetente. Manifestos com SHA-1 e MD5 estão obsoletos para fins de segurança; use SHA-256 ou mais forte.

### Exercícios

- **EX013 — Senha em Base64.** Uma configuração guarda uma cadeia em Base64 rotulada como senha cifrada. O que está errado? *Rubrica:* 3 = Base64 é uma codificação reversível, sem chave; não é cifração;; 2 = diz que não é cifrada;; 1 = concorda que é cifrada;; 0 = nenhuma.

- **EX014 — Resultado do manifesto.** No laboratório, que arquivo foi sinalizado, e por quê? *Rubrica:* 3 = routes_tue.csv, seu resumo deixou de coincidir depois que um caractere mudou;; 2 = nomeia o arquivo;; 1 = nenhum arquivo;; 0 = nenhuma.

- **EX015 — Limite do manifesto.** Que ataque um manifesto não assinado não consegue impedir? *Rubrica:* 3 = um atacante que substitui tanto o arquivo quanto o manifesto;; 2 = menciona atacante;; 1 = diz que nenhum;; 0 = nenhuma.

- **EX016 — Conferência do cabeçalho PEM.** Que cabeçalho PEM nunca pode ser colado num chamado? *Rubrica:* 3 = qualquer cabeçalho PRIVATE KEY, porque é secreto;; 2 = menciona privada;; 1 = cabeçalho de certificado;; 0 = nenhuma.

### Síntese

Saber se os dados estão codificados, passaram por hash ou estão cifrados diz a um técnico o que eles podem provar e quem pode revertê-los.

<a id="ch-05"></a>

## Capítulo 5 — Escopo e evidências de segurança

### Objetivos de aprendizagem

Você vai (1) escrever uma declaração de escopo para verificações criptográficas; (2) coletar evidências que outro técnico consiga reproduzir; (3) tratar os segredos encontrados durante o trabalho.

### 5.1 Escrever um escopo

Antes que Tomás varra qualquer coisa, Priya o faz escrever um escopo. Ele nomeia os sistemas que ele pode testar, como o portal de rastreamento e o host de transferência de arquivos; as verificações que pode executar, como testes de handshake e leituras de certificados; a janela de tempo; e a pessoa que aprovou. Varrer o servidor de um parceiro ou um provedor de pagamentos sem a permissão deles está fora do escopo, mesmo que seja tecnicamente fácil. Um escopo protege a empresa, os parceiros e o próprio Tomás, porque uma varredura não aprovada pode disparar alarmes, quebrar dispositivos frágeis ou violar um contrato.

### 5.2 Evidências reproduzíveis

Quando Tomás encontra uma configuração fraca, uma captura de tela sozinha é uma evidência pobre. Priya o ensina a registrar o comando exato, a data e a hora com o fuso horário, o host de onde o executou, a saída bruta e um resumo SHA-256 de qualquer arquivo salvo. Outro técnico deve conseguir executar o comando de novo e ver o mesmo resultado, ou explicar por que ele mudou. Boas evidências também registram o que não foi verificado, para que os leitores não suponham uma cobertura maior do que a existente. Esse hábito torna muito mais rápidos os relatórios, as auditorias e as solicitações de mudança posteriores, porque ninguém precisa perguntar como uma afirmação foi obtida.

### 5.3 Segredos encontrados durante o trabalho

Durante as revisões, Tomás vai ver senhas, tokens de API ou chaves privadas em lugares onde não deveriam estar. A regra é parar, registrar apenas a localização e o tipo do segredo, nunca copiar o valor para anotações ou chamados e avisar o dono para que o segredo possa ser rotacionado. As evidências devem mostrar que um segredo existe, por exemplo registrando o caminho do arquivo e os primeiros caracteres de um hash do valor, e não o próprio valor. Tratar os segredos dessa forma evita que a investigação espalhe exatamente a exposição que deveria corrigir.

### Exemplo resolvido

Tomás escreve um escopo de uma página para as verificações de TLS do portal e do host de arquivos, registra um achado com comando, carimbo de tempo e resumo da saída e registra um token vazado apenas pelo caminho.

> **Caso sintético.** Os detalhes do escopo, os hosts e o achado do token são inventados.

### Erros e limites

Um escopo não torna seguro um teste arriscado; as verificações em produção ainda exigem cuidado. As evidências podem ficar desatualizadas em horas, à medida que os sistemas mudam.

### Exercícios

- **EX017 — Alvo fora do escopo.** Varrer a API do provedor de pagamentos está no escopo por padrão? *Rubrica:* 3 = não; exige a permissão explícita do provedor e os termos do contrato;; 2 = diz não;; 1 = diz sim;; 0 = nenhuma.

- **EX018 — Campos das evidências.** Liste quatro campos que um achado reproduzível deve incluir. *Rubrica:* 3 = quatro entre comando, carimbo de tempo com fuso, host de origem, saída bruta, resumo do arquivo, o que não foi verificado;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX019 — Token num script.** Você encontra um token de API num script de shell. O que registra? *Rubrica:* 3 = apenas a localização e o tipo, não o valor; avisar o dono para a rotação;; 2 = localização;; 1 = copia o valor;; 0 = nenhuma.

- **EX020 — Declaração de cobertura.** Por que registrar o que não foi verificado? *Rubrica:* 3 = para que os leitores não suponham uma cobertura maior do que a existente;; 2 = menciona leitores;; 1 = nenhuma razão;; 0 = nenhuma.

### Síntese

O escopo limita o que pode ser testado, as evidências tornam os achados reproduzíveis e os segredos são relatados sem ser copiados.

<a id="ch-06"></a>

## Capítulo 6 — Criptografia e serviços de confiança: modelo do sistema

### Objetivos de aprendizagem

Você vai (1) modelar as relações de confiança da Lumen como partes, chaves e verificadores; (2) identificar as âncoras de confiança; (3) explicar por que uma cadeia de confiança falha no seu elo mais fraco.

### 6.1 Partes, chaves e verificadores

Priya desenha o modelo de confiança num quadro branco. Cada seta tem três partes: uma parte que detém uma chave privada, uma chave pública ou certificado que a representa e um verificador que confere a prova. Os clientes verificam o portal por meio do seu certificado TLS. A Lumen verifica os callbacks do processador de pagamentos por meio de um segredo HMAC compartilhado. Os parceiros verificam os arquivos noturnos por meio da chave de host SSH da Lumen. Desenhar o modelo dessa forma faz Tomás fazer as mesmas três perguntas em todo lugar: quem detém o segredo, o que o verificador confere e o que acontece se o segredo vazar ou a verificação for pulada.

### 6.2 Âncoras de confiança

Toda cadeia de verificação termina em algo em que se confia sem mais provas, chamado âncora de confiança. Para o site público, as âncoras são os certificados raiz distribuídos com os navegadores e os sistemas operacionais. Para o Wi-Fi dos depósitos, a âncora é a raiz interna da própria Lumen, instalada nos coletores pelo gerenciamento de dispositivos. Para o SSH, a âncora é a impressão digital da chave de host registrada na primeira vez que um parceiro se conectou. Tomás aprende que acrescentar uma âncora é um ato poderoso: qualquer certificado assinado sob uma nova raiz passa a ser confiável. Por isso, as mudanças de âncoras passam pelo controle de mudanças, e ele nunca instala uma raiz só para fazer um aviso desaparecer.

### 6.3 Elo mais fraco

Uma cadeia é tão forte quanto sua parte mais fraca. Se a chave privada da raiz interna fica num notebook comum, as configurações cuidadosas de TLS em cada ponto de acesso dos depósitos podem ser desfeitas por qualquer um que roube esse notebook. Se o segredo HMAC dos callbacks de pagamento for versionado num repositório público, a verificação de assinatura no servidor perde o sentido. Tomás revisa cada seta do modelo e pergunta onde o material privado está guardado e quem poderia alcançá-lo. Ele marca dois elos fracos: a localização da chave da raiz interna e uma antiga chave SSH compartilhada por dois parceiros.

### Exemplo resolvido

Tomás desenha seis setas de confiança com detentor, artefato e verificador, rotula três âncoras de confiança e sinaliza dois elos fracos para Priya.

> **Caso sintético.** O modelo de confiança, as raízes e as chaves são sintéticos.

### Erros e limites

Os modelos omitem as pessoas que podem contornar as verificações, como funcionários que clicam para passar pelos avisos. As âncoras instaladas pelos fornecedores estão fora do controle da Lumen.

### Exercícios

- **EX021 — Três perguntas.** Que três perguntas Tomás faz sobre cada seta de confiança? *Rubrica:* 3 = quem detém o segredo, o que o verificador confere, e se o segredo vazar ou a verificação for pulada;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX022 — Âncora dos depósitos.** Qual é a âncora de confiança dos certificados do Wi-Fi dos depósitos? *Rubrica:* 3 = a raiz interna da Lumen instalada nos coletores;; 2 = raiz interna;; 1 = AC pública;; 0 = nenhuma.

- **EX023 — Acrescentar uma raiz.** Por que instalar uma nova raiz precisa passar pelo controle de mudanças? *Rubrica:* 3 = todo certificado assinado sob ela passa a ser confiável; é um ato poderoso;; 2 = menciona o alcance da confiança;; 1 = inofensivo;; 0 = nenhuma.

- **EX024 — Chave compartilhada entre parceiros.** Por que uma chave SSH compartilhada por dois parceiros é um elo fraco? *Rubrica:* 3 = o vazamento de um parceiro compromete os dois e o acesso não pode ser revogado separadamente;; 2 = menciona vazamento;; 1 = não é fraco;; 0 = nenhuma.

### Síntese

Os modelos de confiança tornam explícitos cada detentor, âncora e verificador, para que o elo mais fraco fique visível.

<a id="ch-07"></a>

## Capítulo 7 — Criptografia e serviços de confiança: dados e telemetria

### Objetivos de aprendizagem

Você vai (1) escolher fontes de dados para monitorar a saúde criptográfica; (2) calcular a expiração dos certificados a partir de um inventário; (3) evitar registrar segredos em logs.

### 7.1 Fontes de dados úteis

Tomás lista onde os fatos criptográficos podem ser observados. As configurações dos servidores mostram quais versões de TLS e quais certificados estão implantados. Os logs de handshake no balanceador de carga registram as versões negociadas e as falhas. Os logs de transparência de certificados, definidos na RFC 6962, listam publicamente os certificados emitidos para os domínios da Lumen, o que ajuda a detectar emissões inesperadas. A planilha do inventário registra os donos e as datas de expiração. Cada fonte responde a uma pergunta diferente, e nenhuma é completa sozinha: a configuração diz o que deveria acontecer, os logs dizem o que aconteceu e os logs de transparência mostram o que as autoridades certificadoras emitiram para os nomes da Lumen, quer a Lumen tenha pedido, quer não.

### 7.2 Expiração a partir do inventário

Certificados expirados causam a maioria das indisponibilidades que Priya já viu. Ela pede que Tomás calcule os dias restantes de cada certificado do inventário e os ordene por urgência. Ele escreve um script curto que lê um CSV sintético, compara cada data notAfter com uma data de revisão fixa e rotula cada linha como renew now, plan ou fine. Usar uma data de revisão fixa no laboratório mantém a saída reproduzível; em produção, o script usaria a data atual. O laboratório abaixo mostra o resultado para cinco certificados sintéticos, incluindo um que já expirou.

### Laboratório — Relatório de expiração de certificados

```python
# Synthetic certificate inventory; fixed review date for reproducible output.
import csv, io, datetime
REVIEW = datetime.date(2026, 3, 1)
data = """host,not_after,owner
track.lumen.example,2026-03-20,web-team
sftp.lumen.example,2026-07-30,ops
depot-wifi-ca,2031-01-15,ops
staging.lumen.example,2026-02-17,web-team
api.lumen.example,2026-04-10,web-team
"""
rows = []
for r in csv.DictReader(io.StringIO(data)):
    d = (datetime.date.fromisoformat(r["not_after"]) - REVIEW).days
    label = "EXPIRED" if d < 0 else "renew now" if d <= 30 else "plan" if d <= 60 else "fine"
    rows.append((d, r["host"], r["owner"], label))
for d, h, o, l in sorted(rows):
    print(f"{h:24} {d:5d} days  {o:9} {l}")
```

Execute com `python3 lab_expiry.py`. Saída verificada:

```text
staging.lumen.example      -12 days  web-team  EXPIRED
track.lumen.example         19 days  web-team  renew now
api.lumen.example           40 days  web-team  plan
sftp.lumen.example         151 days  ops       fine
depot-wifi-ca             1781 days  ops       fine
```

### 7.3 Manter os segredos fora dos logs

A telemetria pode vazar o que mede. Certa vez, uma configuração de depuração no portal registrou os cabeçalhos HTTP completos, incluindo cookies de sessão e uma chave de API, num arquivo legível por toda a equipe de operações. Tomás aprende a conferir os formatos de log antes de ativá-los, a mascarar os tokens para que restem apenas alguns caracteres e a manter desligados em produção os recursos de registro de chaves do TLS, que gravam segredos de sessão para depuração. Os logs são copiados para muitos lugares, como backups e ferramentas de análise, então um segredo gravado uma vez pode ser muito difícil de remover por completo.

### Exemplo resolvido

Tomás executa o laboratório de expiração, encontra um certificado expirado no antigo host de homologação e abre um chamado que também remove uma opção de depuração que registrava cabeçalhos.

> **Caso sintético.** As linhas do inventário, os hosts e as datas são sintéticos; a RFC 6962 é real.

### Erros e limites

Os inventários se afastam da realidade; confirme a expiração no endpoint em funcionamento. Os logs de transparência cobrem os certificados de confiança pública, e não os internos.

### Exercícios

- **EX025 — Três fontes.** Que fonte mostra os certificados que uma AC emitiu para a Lumen mesmo que a Lumen não os tenha pedido? *Rubrica:* 3 = logs de transparência de certificados;; 2 = nomeia CT;; 1 = nomeia configuração;; 0 = nenhuma.

- **EX026 — Linha expirada.** No laboratório, que certificado já tinha expirado, e há quantos dias? *Rubrica:* 3 = staging.lumen.example, expirado 12 dias antes da data de revisão;; 2 = só o host;; 1 = nenhum;; 0 = nenhuma.

- **EX027 — Data de revisão fixa.** Por que o laboratório usa uma data de revisão fixa? *Rubrica:* 3 = para que a saída seja reproduzível; em produção usa-se a data de hoje;; 2 = reproduzível;; 1 = nenhuma razão;; 0 = nenhuma.

- **EX028 — Registro de cabeçalhos em depuração.** O que deu errado com o registro de depuração do portal? *Rubrica:* 3 = registrou cookies de sessão e uma chave de API num arquivo amplamente legível;; 2 = menciona segredos;; 1 = nada;; 0 = nenhuma.

### Síntese

A telemetria deve revelar a saúde criptográfica, como a expiração e as falhas, sem se tornar ela mesma uma fonte de segredos vazados.

<a id="ch-08"></a>

## Capítulo 8 — Criptografia e serviços de confiança: modos de falha

### Objetivos de aprendizagem

Você vai (1) classificar as falhas criptográficas como expiração, incompatibilidade, má configuração ou comprometimento; (2) explicar em termos simples a reutilização de nonces e a aleatoriedade fraca; (3) escolher uma primeira resposta para cada classe.

### 8.1 Quatro classes de falha

Priya agrupa os incidentes anteriores da Lumen em quatro classes. Expiração: um certificado ou uma chave passou da data final, então os clientes o recusaram. Incompatibilidade: o certificado não cobria o nome do host, ou a cadeia estava incompleta. Má configuração: um servidor permitia versões obsoletas do protocolo, ou um script desativava a verificação. Comprometimento: uma chave privada ou um segredo compartilhado vazou. Tomás nota que as três primeiras são operacionais e normalmente barulhentas, porque os usuários veem erros, enquanto o comprometimento costuma ser silencioso. Essa diferença molda o monitoramento: as falhas barulhentas precisam de reparo rápido, e as silenciosas precisam de controles de detecção, como o monitoramento de transparência e os logs de acesso às chaves.

### 8.2 Nonces e aleatoriedade

Algumas falhas vêm de usos indevidos dentro do software, e não das configurações. O AES-GCM, descrito na NIST SP 800-38D, exige que um nonce nunca se repita sob a mesma chave; uma repetição pode revelar a relação entre duas mensagens e permite que um atacante forje etiquetas de autenticação. As chaves e os nonces precisam vir de um gerador criptograficamente seguro, como a fonte do sistema operacional encapsulada pelo módulo secrets do Python, e não do random, que é previsível. Tomás não vai escrever esse tipo de código para produção, mas precisa reconhecer esses erros nos avisos dos fornecedores e nas revisões de código e saber que eles exigem uma correção do fornecedor, e não um ajuste de configuração.

### 8.3 Primeiras respostas

Para a expiração, renove e implante o certificado e depois acrescente monitoramento. Para a incompatibilidade, emita de novo com os nomes corretos ou corrija a cadeia servida pelo host. Para a má configuração, mude a configuração por meio do controle de mudanças e teste de novo. Para o comprometimento, revogue o certificado ou rotacione o segredo imediatamente, descubra onde a chave foi exposta e revise os logs em busca de uso indevido. Tomás escreve isso num cartão plastificado para o turno da noite. Ele acrescenta que um técnico que não tenha certeza se um caso é má configuração ou comprometimento deve tratá-lo como comprometimento até que um engenheiro sênior decida.

### Exemplo resolvido

Tomás separa seis incidentes sintéticos nas quatro classes e escreve num cartão de uma página a primeira resposta correspondente a cada um.

> **Caso sintético.** Os incidentes são inventados; a SP 800-38D é real.

### Erros e limites

As classes se sobrepõem; um certificado expirado substituído às pressas por um autoassinado vira má configuração. Um comprometimento silencioso pode nunca ser detectado.

### Exercícios

- **EX029 — Barulhentas e silenciosas.** Que classe de falha costuma ser silenciosa, e o que isso implica? *Rubrica:* 3 = comprometimento; exige controles de detecção, como CT e logs de acesso às chaves;; 2 = nomeia comprometimento;; 1 = nomeia expiração;; 0 = nenhuma.

- **EX030 — Regra do nonce do GCM.** Que regra o AES-GCM impõe aos nonces? *Rubrica:* 3 = nunca repetir um nonce sob a mesma chave;; 2 = unicidade;; 1 = nada;; 0 = nenhuma.

- **EX031 — Módulo random.** Por que o módulo random do Python é errado para chaves? *Rubrica:* 3 = é previsível; use o secrets, que encapsula o CSPRNG do sistema operacional;; 2 = previsível;; 1 = tudo bem;; 0 = nenhuma.

- **EX032 — Caso incerto.** O que um técnico deve fazer quando não tem certeza se um caso é comprometimento? *Rubrica:* 3 = tratá-lo como comprometimento até que um engenheiro sênior decida;; 2 = escalar;; 1 = esperar;; 0 = nenhuma.

### Síntese

Classificar uma falha como expiração, incompatibilidade, má configuração ou comprometimento diz ao técnico quão urgente ela é e o que fazer primeiro.

<a id="ch-09"></a>

## Capítulo 9 — Criptografia e serviços de confiança: ferramentas e métodos

### Objetivos de aprendizagem

Você vai (1) usar o openssl, o ssh-keygen e o módulo ssl do Python com segurança para inspeção; (2) ler um teste de handshake; (3) evitar ferramentas que vazam dados para terceiros.

### 9.1 O kit básico

O kit de ferramentas de Tomás é pequeno. O openssl s_client se conecta a um servidor e imprime o protocolo negociado, a suíte de cifras e a cadeia de certificados. O openssl x509 -noout -text lê um arquivo de certificado. O ssh-keygen -l -f imprime a impressão digital de uma chave pública SSH para que possa ser comparada com um valor registrado. O módulo ssl do Python pode abrir uma conexão verificada e informar a versão do protocolo em poucas linhas. Cada ferramenta lê informações públicas ou arquivos locais; nenhuma precisa de chaves privadas. Priya insiste em que ele entenda cada opção que usa, porque comandos copiados de fóruns muitas vezes incluem opções que desativam a verificação.

### 9.2 Ler um teste de handshake

Tomás executa o s_client contra o portal de homologação no laboratório e lê a saída de cima para baixo. Ele confere a linha do protocolo, que deve dizer TLSv1.3 ou TLSv1.2; o resultado da verificação, que deve ser 0 (ok); o titular e os nomes alternativos do certificado; e a data notAfter. Um resultado como unable to get local issuer certificate significa que o servidor não enviou seu intermediário. Ele registra o comando e a saída como evidência. Ele aprende que um erro de verificação num teste é um achado a relatar, e nunca algo a silenciar com uma opção que pula as verificações.

### 9.3 Ferramentas que vazam

Decodificadores de certificados online, sites de colagem de texto e scanners públicos são convenientes, mas enviam os dados a um terceiro. Colar um certificado é de baixo risco, porque ele é público; colar uma chave privada, uma configuração com segredos ou uma lista de nomes de hosts internos não é. Os serviços públicos de varredura também registram resultados que outros podem pesquisar. A regra de Tomás é usar ferramentas locais para tudo o que é interno e usar serviços públicos apenas para endpoints públicos, com aprovação. Ele também confere que seus próprios scripts nunca imprimam segredos no terminal, porque o histórico do terminal e o compartilhamento de tela vazam.

### Exemplo resolvido

Tomás testa o portal de homologação com o s_client, encontra um intermediário ausente, registra a evidência localmente e recusa a sugestão de um colega de colar a chave do servidor num decodificador web.

> **Caso sintético.** Os hosts e as saídas descritos são sintéticos.

### Erros e limites

A saída das ferramentas varia entre versões; registre as versões junto com as evidências. Um teste bem-sucedido a partir de uma rede não diz nada sobre clientes em outros lugares.

### Exercícios

- **EX033 — Conferência da impressão digital.** Que comando imprime a impressão digital de uma chave pública SSH para comparação? *Rubrica:* 3 = ssh-keygen -l -f arquivo_da_chave;; 2 = nomeia o ssh-keygen;; 1 = nomeia o openssl;; 0 = nenhuma.

- **EX034 — Intermediário ausente.** O que unable to get local issuer certificate normalmente significa? *Rubrica:* 3 = o servidor não enviou seu certificado intermediário;; 2 = problema de cadeia;; 1 = expirado;; 0 = nenhuma.

- **EX035 — Silenciar erros.** Um fórum sugere acrescentar uma opção que pula a verificação. Por que recusar? *Rubrica:* 3 = o erro é um achado; pulá-lo o esconde e permite a interceptação;; 2 = esconde o problema;; 1 = aceitar;; 0 = nenhuma.

- **EX036 — Política de colagem.** Qual item pode ir para um decodificador público, um certificado ou uma chave privada? *Rubrica:* 3 = um certificado público de um endpoint público, nunca uma chave privada;; 2 = certificado;; 1 = chave privada;; 0 = nenhuma.

### Síntese

As ferramentas de inspeção são seguras quando leem apenas dados públicos, mantêm a verificação ligada e ficam locais para o material interno.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX036 (as de EX037–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). Tomás Reyes, Priya Nandakumar, o Eastbrook Technical Institute, a Lumen Freight Logistics e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Ele diagnostica falhas criptográficas, configura controles e verifica que eles funcionam, sem inventar algoritmos.

**EX002.** O coletor é um cliente, o portal de rastreamento é um servidor e o processador de pagamentos é um serviço gerenciado.

**EX003.** Porque o AES ou o TLS podem ser configurados corretamente num servidor e de forma fraca em outro, então o nome sozinho diz pouco.

**EX004.** Diz a Tomás se é a Lumen ou um fornecedor que precisa agir, para que ele escale em vez de perder tempo com configurações que não pode mudar.

**EX005.** Resolução DNS, conexão TCP com a porta 443, o handshake TLS e, por fim, a requisição HTTP com o número da encomenda.

**EX006.** Porque o host impostor não consegue mostrar um certificado confiável para track.lumen.example, então o navegador interrompe o handshake.

**EX007.** O endereço IP do servidor e, na maioria das implantações, o nome do servidor no handshake; os tamanhos e o tempo também vazam.

**EX008.** É uma falha na camada TLS; execute um teste de handshake, como o openssl s_client, e leia a data notAfter do certificado.

**EX009.** Porque qualquer conta local pode copiar o arquivo e se passar pelo serviço; a força da chave não ajuda depois que ela vaza.

**EX010.** Eles apagaram a cópia e substituíram a chave, porque não conseguiam provar que ninguém a tinha lido.

**EX011.** Apenas sua própria chave TLS e os arquivos de aplicação de que precisa, sem login interativo.

**EX012.** Porque as identidades não humanas são facilmente esquecidas, e registrar a chave, o dono e a data de criação torna a rotação possível.

**EX013.** Base64 é apenas uma codificação; qualquer um pode decodificá-la sem chave, então a senha está, na prática, em texto claro.

**EX014.** routes_tue.csv foi sinalizado porque seu SHA-256 recalculado diferiu do manifesto depois que o conteúdo mudou.

**EX015.** Um atacante capaz de alterar tanto o arquivo de dados quanto o manifesto pode fazê-los coincidir; o manifesto precisa ser assinado ou autenticado.

**EX016.** Um bloco BEGIN PRIVATE KEY (ou RSA/EC PRIVATE KEY), já que é a metade secreta do par de chaves.

**EX017.** Não. Os sistemas de terceiros exigem a permissão explícita desse terceiro, que um escopo da Lumen não pode conceder.

**EX018.** O comando exato, a data e a hora com fuso, o host de onde foi executado e a saída bruta, além de um resumo dos arquivos salvos.

**EX019.** Apenas o caminho do arquivo e o fato de ser um token de API; depois, avisar o dono para que possa ser rotacionado; nunca copiar o valor.

**EX020.** Para que os leitores não confundam um teste parcial com uma garantia completa.

**EX021.** Quem detém o segredo, o que exatamente o verificador confere e o que acontece se o segredo vazar ou a verificação for pulada.

**EX022.** O próprio certificado raiz interno da Lumen, instalado nos coletores por meio do gerenciamento de dispositivos.

**EX023.** Porque todo certificado emitido sob essa raiz passa a ser confiável, o que pode permitir a interceptação se for mal usado.

**EX024.** Um vazamento de qualquer dos parceiros expõe as duas conexões, e a Lumen não consegue revogar um parceiro sem quebrar o outro.

**EX025.** Os logs de transparência de certificados, que registram publicamente os certificados emitidos para os domínios da Lumen.

**EX026.** staging.lumen.example, que expirou 12 dias antes da data de revisão de 2026-03-01.

**EX027.** Para que a saída seja a mesma em todas as execuções; um script de produção compararia com a data atual.

**EX028.** Gravou os cabeçalhos completos, incluindo cookies de sessão e uma chave de API, num log legível por toda a equipe.

**EX029.** O comprometimento costuma ser silencioso, então exige detecção, como o monitoramento de transparência e o registro dos acessos às chaves.

**EX030.** Um nonce nunca pode se repetir sob a mesma chave; a reutilização pode expor relações entre textos claros e permitir a falsificação de etiquetas.

**EX031.** O random não é criptograficamente seguro e sua saída pode ser prevista; o secrets usa o gerador seguro do sistema operacional.

**EX032.** Tratá-lo como comprometimento, iniciando os passos de revogação ou rotação, até que um engenheiro sênior decida o contrário.

**EX033.** ssh-keygen -l -f seguido do arquivo da chave pública imprime sua impressão digital para comparação com o valor registrado.

**EX034.** O servidor não está enviando o certificado intermediário, então o cliente não consegue montar uma cadeia até uma raiz confiável.

**EX035.** Porque o erro de verificação é o achado; pular as verificações o esconde e permitiria que um impostor passasse.

**EX036.** Apenas um certificado público de um endpoint público, com aprovação; uma chave privada nunca deve sair das ferramentas locais.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barnes, R., Hoffman-Andrews, J., McCarney, D., & Kasten, J. (2019). *Automatic certificate management environment (ACME)* (RFC 8555). IETF. <https://www.rfc-editor.org/rfc/rfc8555>
- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Dworkin, M. (2007). *Recommendation for block cipher modes of operation: Galois/Counter Mode (GCM) and GMAC* (NIST SP 800-38D). NIST. <https://doi.org/10.6028/NIST.SP.800-38D>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate transparency* (RFC 6962). IETF. <https://www.rfc-editor.org/rfc/rfc6962>
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- Nystrom, M. (2005). *Identifiers and test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512* (RFC 4231). IETF. <https://www.rfc-editor.org/rfc/rfc4231>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
