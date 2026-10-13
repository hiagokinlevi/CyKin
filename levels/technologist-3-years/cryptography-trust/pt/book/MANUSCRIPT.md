# Criptografia e Serviços de Confiança: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 077, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 30 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 9–30 (EX025–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: implementadores e administradores de tecnologia.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios analisam logs, planejam renovações, verificam HMACs e chamam o scrypt do hashlib contra um vetor publicado; não implementam nenhuma cifra. Sistemas de produção usam bibliotecas avaliadas, clientes ACME, HSMs e produtos de fornecedores; nunca crie sua própria criptografia. Pessoas, organizações e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de tecnólogo pelos fundamentos, por um estágio numa prefeitura e por um projeto final: codificação versus cifração, TLS e certificados, inventários, fluxos de dados, risco, verificação de webhooks, uma autoridade certificadora de laboratório, armazenamento de senhas, ferramentas, controles, monitoramento, solução de problemas, integração, automação, avaliação, pesquisa, trabalho em equipe, passagem, implantação, prática de campo e o projeto final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Rosa Delgado** | Estudante de tecnólogo | Inventada |
| **Owen Pryce** | Mentor do estágio, TI da prefeitura | Inventado |
| **Dr Imogen Hale** | Tutora | Inventada |
| **Pinecrest Polytechnic** | Escola fictícia | Inventada |
| **Harbourview City Council** | Governo local fictício | Inventado |

### Fontes principais

[RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555); [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104); [RFC 7914](https://www.rfc-editor.org/rfc/rfc7914); NIST [SP 800-52 Rev. 2](https://doi.org/10.6028/NIST.SP.800-52r2) e [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever os sistemas que uma cidade opera e onde a criptografia aparece neles; (2) distinguir hardware, software e serviços; (3) identificar dependências criptográficas em serviços do dia a dia.

### 1.1 O caso

Rosa Delgado é estudante do primeiro ano do curso de tecnólogo de três anos da fictícia Pinecrest Polytechnic. Seu estágio, que se estende pelos três anos, é no departamento de TI do fictício Harbourview City Council, sob a supervisão do engenheiro sênior Owen Pryce. A prefeitura opera um portal de licenças de estacionamento, um serviço de documentos para as decisões municipais assinadas, uma VPN para a equipe, um sistema de informação geográfica e integrações de pagamento. Todos os sistemas, pessoas e números deste livro são sintéticos. Um tecnólogo constrói e opera serviços integrados, então o objetivo de Rosa é tornar esses serviços confiáveis na operação diária, e não inventar uma criptografia nova.

### 1.2 Hardware, software e serviços

Rosa classifica os sistemas da prefeitura em hardware, como servidores, notebooks e equipamentos de rede; software, como sistemas operacionais, servidores web e bancos de dados; e serviços contratados de fora, como o provedor de pagamentos e a plataforma de e-mail. A criptografia aparece em cada um: os notebooks cifram os discos, os servidores web terminam o TLS, os bancos de dados cifram os backups e o provedor de pagamentos assina as notificações. Owen pede que ela anote, para cada item, quem controla as chaves. Ela descobre que, nos serviços externos, é o provedor que guarda as chaves, o que significa que a prefeitura precisa confiar nos contratos e nos controles do provedor, e não na sua própria configuração.

### 1.3 Dependências do dia a dia

Rosa acompanha uma ação de um cidadão, a compra de uma licença de estacionamento, do começo ao fim. O navegador se conecta ao portal por TLS; o portal confere a senha do cidadão contra um hash armazenado; ele chama o provedor de pagamentos, que depois envia de volta uma notificação assinada; e o registro da licença é armazenado num banco de dados cifrado, com backups noturnos cifrados. Cinco mecanismos criptográficos distintos sustentam uma tarefa simples. Se qualquer um deles falhar, por exemplo um certificado expirado ou um segredo de webhook errado, os cidadãos veem erros. Esse exercício mostra a Rosa por que a integração de serviços e as operações são centrais na criptografia aplicada.

### Exemplo resolvido

Rosa mapeia a compra da licença pelo TLS, pelo hash de senhas, por uma notificação de pagamento assinada e pelo armazenamento cifrado, e anota quem guarda cada chave.

> **Caso sintético.** Harbourview, Pinecrest e todos os sistemas são inventados.

### Erros e limites

Diagramas de uma única transação deixam passar processos de fundo, como backups e logs. Os serviços externos transferem o controle das chaves aos provedores, então os contratos importam.

### Exercícios

- **EX001 — Local do estágio.** Onde acontece o estágio de Rosa, e em que um tecnólogo se concentra? *Rubrica:* 3 = TI do Harbourview City Council; tornar serviços integrados confiáveis na operação;; 2 = só o local;; 1 = inventar criptografia;; 0 = nenhuma.

- **EX002 — Chaves do provedor.** Quem guarda as chaves dos serviços externos, e o que decorre disso? *Rubrica:* 3 = o provedor; a prefeitura depende dos contratos e dos controles do provedor;; 2 = provedor;; 1 = a prefeitura;; 0 = nenhuma.

- **EX003 — Mecanismos da licença.** Cite quatro mecanismos criptográficos na compra de uma licença. *Rubrica:* 3 = quatro entre TLS, hash de senha, notificação assinada, cifração do banco de dados, cifração dos backups;; 2 = três;; 1 = um;; 0 = nenhuma.

### Síntese

Mesmo serviços públicos simples dependem de vários mecanismos criptográficos cujas chaves e donos precisam ser conhecidos.

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem

Você vai (1) explicar o DNS, o HTTP e o TLS num serviço web municipal; (2) descrever o que os certificados TLS provam; (3) reconhecer falhas comuns no nível da rede.

### 2.1 Como uma requisição viaja

Quando um cidadão digita permits.harbourview.example, o navegador pergunta ao DNS o endereço do servidor, abre uma conexão TCP e inicia um handshake TLS antes de enviar qualquer requisição HTTP. Rosa aprende que a ordem importa: as respostas do DNS não são protegidas pelo TLS, de modo que um atacante que envenene o DNS poderia direcionar o navegador para outro lugar, mas as verificações do certificado TLS falhariam então, porque o atacante não consegue apresentar um certificado válido para o nome da prefeitura. É por isso que a validação de certificados é a âncora da segurança na web: ela detecta redirecionamentos que as camadas inferiores não conseguem impedir. Ela pratica o rastreamento dessas etapas num laboratório com domínios de teste.

### 2.2 O que um certificado prova

Um certificado TLS vincula o nome permits.harbourview.example a uma chave pública, com a assinatura de uma autoridade certificadora em que o navegador confia. A RFC 5280 define os campos, incluindo os nomes alternativos do titular e as datas de validade. O certificado prova que quem conclui o handshake detém a chave privada daquele nome; ele não prova que o site é seguro nem que o código da prefeitura está livre de bugs. Rosa explica isso à equipe de comunicação da prefeitura, que tinha dito aos cidadãos que "o cadeado significa que seus dados estão seguros", e sugere uma redação mais precisa, dizendo que a conexão é privada.

### 2.3 Falhas comuns

Rosa lista as falhas de rede que vai encontrar: certificados expirados, certificados sem um nome necessário, cadeias incompletas em que o servidor não envia o certificado intermediário, relógios errados nos clientes e clientes antigos que não conseguem negociar as versões modernas do TLS definidas na RFC 8446. Cada uma produz um erro diferente no navegador. Ela monta para a central de atendimento um guia de uma página que associa as mensagens de erro às causas prováveis, para que a equipe de primeiro nível possa coletar os detalhes certos antes de escalar. O guia depois reduz o tempo gasto no diagnóstico de problemas simples de certificado.

### Exemplo resolvido

Rosa rastreia o DNS, o TCP e o TLS do site de licenças, corrige a frase "o cadeado significa segurança" e escreve um guia de erros e causas para a central de atendimento.

> **Caso sintético.** Os domínios e as equipes são inventados; a RFC 5280 e a RFC 8446 são reais.

### Erros e limites

O TLS sozinho não protege as consultas DNS. Um certificado válido não diz nada sobre a segurança da aplicação.

### Exercícios

- **EX004 — DNS e TLS.** Por que a validação de certificados ainda protege um cidadão se o DNS for envenenado? *Rubrica:* 3 = o atacante não consegue apresentar um certificado válido para o nome da prefeitura;; 2 = certificado válido;; 1 = não protege;; 0 = nenhuma.

- **EX005 — Redação do cadeado.** O que Rosa sugeriu no lugar de "o cadeado significa que seus dados estão seguros"? *Rubrica:* 3 = uma redação dizendo que a conexão é privada, e não que o site ou os dados estão seguros;; 2 = precisa;; 1 = inalterada;; 0 = nenhuma.

- **EX006 — Cadeia incompleta.** O que é uma falha de cadeia incompleta? *Rubrica:* 3 = o servidor não envia o certificado intermediário;; 2 = intermediário ausente;; 1 = expirado;; 0 = nenhuma.

### Síntese

A segurança na web se apoia na validação de certificados sobre camadas que, de outra forma, ficam desprotegidas; conhecer os padrões de falha acelera o diagnóstico.

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem

Você vai (1) escrever scripts simples em Python para as operações; (2) distinguir codificação de cifração; (3) tratar segredos em scripts com segurança.

### 3.1 Scripts para as operações

Os tecnólogos automatizam o trabalho rotineiro com scripts. Os primeiros scripts de Rosa leem exportações em CSV da lista de certificados da prefeitura e imprimem os que expiram em até trinta dias. Ela aprende a usar a biblioteca padrão: csv para ler arquivos, datetime para a aritmética de datas e argparse para as opções de linha de comando. Ela escreve funções pequenas, com nomes claros, e testa cada uma com dados de exemplo antes de executá-las sobre as exportações reais. Owen revisa o código e pede que ela trate as linhas ruins com elegância, já que as exportações dos sistemas mais antigos às vezes contêm datas em branco que, de outra forma, derrubariam o script.

### Laboratório — Codificação não é cifração

```python
"""Encoding is not encryption: Base64 and hex are reversible by anyone (synthetic permit record)."""
import base64
REC = b"permit=PK-2291;plate=HRV-447;zone=4"

def main():
    b64 = base64.b64encode(REC).decode()
    print("base64:", b64)
    print("decoded without any key:", base64.b64decode(b64).decode())
    print("hex:", REC.hex()[:32], "...")
    print("length grows by", len(b64) - len(REC), "chars; secrecy added: none")

if __name__ == "__main__":
    main()
```

Execute com `python3 lab_encoding.py`. Saída verificada:

```text
base64: cGVybWl0PVBLLTIyOTE7cGxhdGU9SFJWLTQ0Nzt6b25lPTQ=
decoded without any key: permit=PK-2291;plate=HRV-447;zone=4
hex: 7065726d69743d504b2d323239313b70 ...
length grows by 13 chars; secrecy added: none
```

### 3.2 Ler o laboratório de codificação

O laboratório codifica em Base64 um registro sintético de licença. A saída parece embaralhada, mas decodificá-la não exige nenhuma chave e imprime exatamente o registro original. A codificação hexadecimal, da mesma forma, apenas muda a representação. O Base64 deixa o texto treze caracteres mais longo e não acrescenta nenhum sigilo. Rosa encontra uma integração da prefeitura que "protegia" os dados das licenças em trânsito codificando-os em Base64 dentro de uma requisição HTTP não cifrada. Ela a relata, e a integração passa para HTTPS com TLS. A lição é simples, mas importante: a codificação serve a formatos de transporte e armazenamento, enquanto a confidencialidade exige cifração com uma chave.

### 3.3 Segredos em scripts

O script seguinte de Rosa chama uma API interna que exige um token. Sua primeira versão escreve o token diretamente no código, o que Owen rejeita: o código é copiado, compartilhado e versionado em repositórios. Ela move o token para uma variável de ambiente preenchida pelo repositório de segredos da prefeitura e faz o script falhar de forma clara se ele estiver ausente. Ela também evita imprimir tokens nos logs e usa o módulo secrets quando um script precisa gerar um valor aleatório, nunca o módulo random. Esses hábitos se aplicam a todos os scripts que ela escreve depois.

### Exemplo resolvido

Rosa escreve um script de expiração de certificados com leitura tolerante, mostra que o Base64 não acrescenta sigilo, faz uma integração com Base64 sobre HTTP passar para TLS e tira um token de API do código.

> **Caso sintético.** O registro de licença e a integração são inventados.

### Erros e limites

A ofuscação, como o Base64, leva as pessoas a acreditar que os dados estão protegidos. Variáveis de ambiente são melhores que o código, mas ainda precisam de um repositório de segredos por trás.

### Exercícios

- **EX007 — Linhas ruins.** O que Owen pediu que Rosa tratasse no script de expiração? *Rubrica:* 3 = linhas em branco ou ruins das exportações antigas, sem derrubar o script;; 2 = linhas ruins;; 1 = velocidade;; 0 = nenhuma.

- **EX008 — Achado do Base64.** O que Rosa encontrou, e o que resolveu? *Rubrica:* 3 = dados de licenças codificados em Base64 sobre HTTP simples; passaram para HTTPS;; 2 = achado e correção;; 1 = um;; 0 = nenhuma.

- **EX009 — Tratamento do token.** Para onde Rosa moveu o token da API, e por quê? *Rubrica:* 3 = para uma variável de ambiente vinda do repositório de segredos, já que o código é copiado e versionado;; 2 = variável de ambiente;; 1 = deixou no código;; 0 = nenhuma.

### Síntese

Scripts operacionais exigem um tratamento de dados limpo, a compreensão clara de que codificação não é cifração e um manuseio disciplinado dos segredos.

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem

Você vai (1) modelar certificados, chaves e donos como dados; (2) projetar uma tabela de inventário simples; (3) manter valores sensíveis fora dos inventários.

### 4.1 Modelar os objetos de confiança

Rosa projeta um modelo de dados para os certificados e as chaves da prefeitura. Um registro de certificado guarda o nome do host, o emissor, o número de série, a data de expiração, o método de renovação e o dono. Um registro de chave guarda sua finalidade, o algoritmo, a localização, a data de criação e o dono. Cada registro tem um identificador único, e os certificados se ligam à chave que usam. Ela deliberadamente não armazena chaves privadas nem segredos no modelo: o inventário descreve as chaves, nunca as contém. A SP 800-57 Part 1 enfatiza que as organizações precisam conhecer suas chaves, e um modelo bem projetado é o primeiro passo para esse conhecimento.

### 4.2 Projetar a tabela

Usando um banco de dados leve, Rosa cria tabelas para certificados, chaves, donos e serviços, com relacionamentos entre elas. Ela acrescenta restrições: todo certificado precisa ter um dono e uma data de expiração; o método de renovação precisa ser acme, internal-ca ou manual. As restrições capturam os erros no momento da entrada, e não durante uma indisponibilidade. Ela importa as planilhas existentes e encontra trinta linhas sem dono, que sinaliza para acompanhamento. Owen observa que o próprio ato de carregar os dados num modelo mais rigoroso costuma revelar mais do que qualquer relatório.

### 4.3 Manter os segredos de fora

Um colega pergunta se o inventário não poderia também guardar as senhas das contas de serviço, "para manter tudo num lugar só". Rosa explica por que não: o inventário é lido por muitas pessoas, exportado para relatórios e copiado amplamente em backups, de modo que guardar segredos ali os exporia. Os segredos pertencem a um repositório de segredos dedicado, com controle de acesso e logs de auditoria. O inventário pode registrar onde um segredo está guardado e quem é seu dono. Separar a descrição do segredo é um padrão que ela vai reutilizar em todos os sistemas que projetar.

### Exemplo resolvido

O modelo de inventário de Rosa liga certificados, chaves, donos e serviços com restrições, encontra trinta linhas sem dono e se recusa a guardar senhas de serviço.

> **Caso sintético.** O inventário é inventado; a SP 800-57 Part 1 é real.

### Erros e limites

Inventários se degradam sem atualizações vindas da automação. Misturar segredos aos dados descritivos os expõe amplamente.

### Exercícios

- **EX010 — Campos do certificado.** Liste quatro campos de um registro de certificado. *Rubrica:* 3 = quatro entre host, emissor, série, expiração, método de renovação, dono;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX011 — Benefício das restrições.** Por que acrescentar restrições, como exigir um dono? *Rubrica:* 3 = capturar os erros na entrada, e não durante as indisponibilidades;; 2 = erros cedo;; 1 = mais lento;; 0 = nenhuma.

- **EX012 — Pedido das senhas.** Por que as senhas de serviço não podem ir para o inventário? *Rubrica:* 3 = é lido, exportado e copiado amplamente; os segredos pertencem a um repositório de segredos;; 2 = exposição;; 1 = tudo bem;; 0 = nenhuma.

### Síntese

Um modelo de dados claro para os objetos de confiança, imposto com restrições e mantido livre de segredos, torna as chaves e os certificados gerenciáveis.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) explicar os objetivos centrais da criptografia em termos da prefeitura; (2) associar as ferramentas aos objetivos; (3) corrigir mal-entendidos comuns da equipe.

### 5.1 Objetivos em termos da prefeitura

Rosa explica os objetivos criptográficos com exemplos da prefeitura. A confidencialidade mantém privados os endereços dos cidadãos e as referências de pagamento. A integridade garante que uma decisão municipal assinada não foi alterada depois da aprovação. A autenticação confirma que uma notificação de pagamento veio de fato do provedor de pagamentos. A disponibilidade, embora não seja fornecida pela criptografia, pode ser prejudicada por ela quando certificados expiram ou chaves se perdem. Enquadrar os objetivos em torno de serviços reais ajuda os colegas sem formação técnica a ver por que cada controle existe e ajuda Rosa a decidir qual ferramenta convém a cada necessidade, em vez de recorrer à cifração por hábito.

### 5.2 Associar as ferramentas

Rosa monta uma tabela simples. A cifração, como o AES-GCM da SP 800-38D, fornece confidencialidade e, por ser autenticada, integridade para os dados armazenados ou transmitidos. O hash com SHA-256, do FIPS 180-4, fornece impressões digitais para verificações de integridade quando o hash esperado é confiável. O HMAC, da RFC 2104, autentica mensagens entre partes que compartilham um segredo, como os webhooks de pagamento. As assinaturas digitais, como o Ed25519 da RFC 8032, permitem que qualquer pessoa verifique as decisões municipais assinadas com uma chave pública. Ela acrescenta uma coluna indicando quem guarda as chaves em cada caso, ligando as ferramentas às operações.

### 5.3 Corrigir mal-entendidos

Rosa coleta mal-entendidos dos colegas: "Nós ciframos as senhas para poder enviá-las de volta por e-mail se as pessoas esquecerem"; "o PDF é assinado, então é confidencial"; e "nossa VPN significa que os sites internos não precisam de TLS". Ela corrige cada um com delicadeza: as senhas devem passar por hash, e não por uma cifração reversível, para que ninguém consiga recuperá-las; as assinaturas provam a origem e a integridade, mas não escondem o conteúdo; e o tráfego interno ainda se beneficia do TLS, porque existem pessoas internas mal-intencionadas e dispositivos comprometidos. Ela transforma a lista num pequeno questionário para os novos funcionários.

### Exemplo resolvido

Rosa associa quatro objetivos aos serviços da prefeitura, monta uma tabela de ferramentas com quem guarda as chaves e corrige três mal-entendidos da equipe num questionário.

> **Caso sintético.** As falas dos colegas são inventadas.

### Erros e limites

Tabelas simplificam demais; a cifração autenticada, por exemplo, fornece mais de um objetivo. A disponibilidade depende das operações, e não dos algoritmos.

### Exercícios

- **EX013 — Exemplo de integridade.** Que exemplo da prefeitura ilustra a integridade? *Rubrica:* 3 = uma decisão municipal assinada não alterada depois da aprovação;; 2 = exemplo;; 1 = exemplo de confidencialidade;; 0 = nenhuma.

- **EX014 — Ferramenta do webhook.** Que ferramenta convém aos webhooks de pagamento, e por quê? *Rubrica:* 3 = HMAC, já que as duas partes compartilham um segredo e precisam autenticar as mensagens;; 2 = HMAC;; 1 = cifração;; 0 = nenhuma.

- **EX015 — Equívoco das senhas.** Corrija "nós ciframos as senhas para poder enviá-las de volta por e-mail". *Rubrica:* 3 = as senhas devem passar por hash para que ninguém consiga recuperá-las; use a redefinição;; 2 = hash;; 1 = concorda;; 0 = nenhuma.

### Síntese

Letramento em segurança significa associar cada ferramenta criptográfica a um objetivo concreto e corrigir os equívocos em linguagem simples.

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem

Você vai (1) proteger chaves em servidores Linux e máquinas virtuais; (2) entender os riscos da clonagem e dos snapshots; (3) usar a aleatoriedade segura do sistema operacional.

### 6.1 Chaves nos servidores

Os servidores web da prefeitura guardam chaves privadas TLS. Rosa confere como elas são armazenadas: as chaves devem poder ser lidas apenas pela conta do servidor web, nunca por todos os usuários, e não devem ficar em diretórios pessoais nem em pastas compartilhadas. Ela encontra um servidor em que o arquivo da chave pode ser lido por todas as contas, uma sobra de uma sessão de solução de problemas. Ela corrige as permissões, registra a mudança e acrescenta uma verificação semanal que relata os arquivos de chave com permissões frouxas. As permissões do sistema operacional são um controle de chaves básico, mas poderoso.

### 6.2 Clonagem e snapshots

As máquinas virtuais podem ser clonadas e ter snapshots, o que é conveniente, mas arriscado para a criptografia. Um servidor clonado carrega as mesmas chaves privadas do original, então duas máquinas passam a ter uma única identidade. Os snapshots podem capturar as chaves e o estado do gerador aleatório que estão na memória. Rosa descobre que a imagem modelo da prefeitura incluía uma chave de host SSH gerada de antemão, de modo que toda nova máquina virtual tinha a mesma chave. Ela corrige o modelo para gerar as chaves na primeira inicialização e substitui as chaves duplicadas, documentando quantas máquinas foram afetadas.

### 6.3 Aleatoriedade em máquinas virtuais

Máquinas virtuais recém-iniciadas podem ter pouca entropia, e máquinas clonadas podem começar com estados de gerador idênticos. Os sistemas operacionais modernos lidam melhor com isso, alimentando o gerador a partir do hipervisor e de fontes de hardware, e a NIST SP 800-90A descreve os projetos de gerador que eles usam. Rosa confere se as imagens Linux da prefeitura usam a interface getrandom do kernel, que bloqueia até que o gerador esteja alimentado, e se as aplicações a usam, por exemplo por meio do módulo secrets do Python. Ela anota que as aplicações nunca devem manter seus próprios geradores aleatórios caseiros.

### Exemplo resolvido

Rosa corrige uma chave TLS legível por todos, remove uma chave de host SSH duplicada do modelo de máquina virtual e confirma que as imagens usam a aleatoriedade do sistema devidamente alimentada.

> **Caso sintético.** Os servidores e as imagens são inventados; a SP 800-90A é real.

### Erros e limites

Snapshots e backups podem conter chaves; proteja-os como chaves. Corrigir um modelo não corrige as máquinas já clonadas a partir dele.

### Exercícios

- **EX016 — Permissões da chave.** Que problema de permissão Rosa encontrou? *Rubrica:* 3 = um arquivo de chave TLS legível por todas as contas;; 2 = legível;; 1 = nada;; 0 = nenhuma.

- **EX017 — Falha do modelo.** O que havia de errado com o modelo de máquina virtual? *Rubrica:* 3 = continha uma chave de host SSH gerada de antemão, compartilhada por todos os clones;; 2 = chave compartilhada;; 1 = nada;; 0 = nenhuma.

- **EX018 — getrandom.** Por que usar o getrandom nas novas máquinas virtuais? *Rubrica:* 3 = ele bloqueia até que o gerador esteja alimentado, evitando uma aleatoriedade fraca no início;; 2 = alimentado;; 1 = mais rápido;; 0 = nenhuma.

### Síntese

Os sistemas operacionais e a virtualização moldam a segurança das chaves por meio das permissões, dos modelos e da aleatoriedade alimentada.

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem

Você vai (1) explicar como certificados e tokens identificam usuários e dispositivos; (2) configurar a autenticação multifator para a equipe; (3) gerenciar as mudanças de acesso quando funcionários mudam de função ou saem.

### 7.1 Identidades e credenciais

Rosa aprende que as identidades podem ser provadas com senhas, códigos de uso único, chaves de segurança e certificados. A VPN da equipe da prefeitura usa certificados de dispositivo emitidos por uma autoridade certificadora interna, mais a senha do funcionário e um código de uso único. O certificado mostra que o dispositivo é gerenciado pela prefeitura; a senha e o código mostram que a pessoa está autorizada. Rosa explica aos novos funcionários que perder um notebook exige, portanto, tanto revogar o certificado do dispositivo quanto conferir a conta, porque as duas credenciais provam coisas diferentes. Rosa também anota que cada tipo de credencial tem uma validade e um caminho de revogação diferentes, que precisam ser registrados ao lado dele no inventário.

### 7.2 Implantação do multifator

Owen pede que Rosa ajude a implantar chaves de segurança resistentes a phishing para os administradores. As chaves de segurança assinam um desafio que inclui a origem do site, de modo que uma página de login falsa não consegue reutilizar a resposta. Rosa prepara as instruções, registra duas chaves por administrador para que uma chave perdida não deixe ninguém sem acesso e testa a recuperação. Ela mantém os códigos de uso único como alternativa para a equipe sem chaves de segurança. Ela acompanha a adoção semanalmente e alcança todos os administradores em um mês. Ela acompanha o cadastramento semanalmente, cobrando pessoalmente as últimas equipes, porque uma implantação que para em noventa por cento deixa desprotegidas as contas mais fracas.

### 7.3 Entradas, mudanças e saídas

O acesso precisa mudar quando funcionários entram, mudam de função ou saem. Rosa revisa o processo da prefeitura e descobre que os certificados de dispositivo dos que saíam às vezes não eram revogados por semanas. Ela acrescenta à lista de verificação de desligamento um passo que revoga o certificado e desativa os tokens no último dia de trabalho, além de um relatório mensal que compara os certificados ativos com o diretório da equipe. Ela aprende que as credenciais criptográficas são tão boas quanto os processos que as emitem e as retiram. O processamento dos desligamentos é conferido mensalmente contra a lista de recursos humanos, e qualquer certificado ainda válido de uma pessoa que saiu é revogado no mesmo dia.

### Exemplo resolvido

Rosa explica os certificados de dispositivo versus as credenciais pessoais, implanta duas chaves de segurança por administrador e acrescenta a revogação de certificados à lista de desligamento, com uma reconciliação mensal.

> **Caso sintético.** Os processos e os números são inventados.

### Erros e limites

Uma autenticação forte não limita o que um usuário autenticado pode fazer. As chaves de segurança reservas também precisam ser guardadas com segurança.

### Exercícios

- **EX019 — Duas credenciais.** O que o certificado de dispositivo e a senha com código provam, cada um? *Rubrica:* 3 = certificado: dispositivo gerenciado pela prefeitura; senha e código: pessoa autorizada;; 2 = ambos;; 1 = um;; 0 = nenhuma.

- **EX020 — Duas chaves.** Por que registrar duas chaves de segurança por administrador? *Rubrica:* 3 = para que uma chave perdida não deixe o administrador sem acesso;; 2 = reserva;; 1 = segurança;; 0 = nenhuma.

- **EX021 — Lacuna do desligamento.** Que lacuna Rosa encontrou no processo de desligamento? *Rubrica:* 3 = certificados de dispositivo não revogados por semanas;; 2 = atraso;; 1 = nada;; 0 = nenhuma.

### Síntese

Certificados e tokens identificam dispositivos e pessoas, mas são os processos de emissão e de revogação que decidem sua força real.

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) traçar as fronteiras de confiança dos serviços da prefeitura; (2) posicionar o TLS, as assinaturas e a cifração nas fronteiras certas; (3) identificar pontos únicos de falha na infraestrutura de confiança.

### 8.1 Fronteiras de confiança

Rosa desenha a arquitetura do serviço de licenças com as fronteiras de confiança: entre a internet e o gateway web, entre o gateway e os servidores de aplicação, entre as aplicações e o banco de dados e entre a prefeitura e o provedor de pagamentos. Ela marca quais dados atravessam cada fronteira e como são protegidos. O diagrama mostra que o gateway termina o TLS e encaminha o tráfego às aplicações por HTTP simples dentro do data center, um projeto escolhido anos atrás por simplicidade. Ela o registra como uma lacuna.

### 8.2 Posicionar os controles

Rosa propõe controles em cada fronteira: TLS dos cidadãos até o gateway, TLS com autenticação mútua do gateway até as aplicações, conexões com o banco de dados por TLS com verificação de certificado, webhooks do provedor de pagamentos assinados com HMAC e PDFs assinados para as decisões municipais. Owen revisa a proposta e concorda, mas pede que ela estime a carga operacional dos certificados adicionais. Ela responde que a emissão automatizada pela autoridade interna manterá a carga pequena, o que leva ao trabalho de automação dos capítulos posteriores.

### 8.3 Pontos únicos de falha

O diagrama também revela que a autoridade certificadora interna roda numa única máquina virtual, sem backup da sua chave de assinatura, e que a mesma conta de administrador a gerencia e gerencia o gateway. Se a máquina falhasse, nenhum certificado interno novo poderia ser emitido; se a conta fosse comprometida, um atacante poderia emitir certificados e redirecionar o tráfego. Rosa recomenda um backup cifrado da chave da autoridade, mantido sob controle duplo, e contas de administrador separadas. As duas recomendações são acrescentadas ao registro de riscos da prefeitura.

### Exemplo resolvido

O diagrama de arquitetura de Rosa revela HTTP simples atrás do gateway e uma única autoridade certificadora interna sem backup, e ela propõe controles nas fronteiras e backups sob controle duplo.

> **Caso sintético.** A arquitetura é inventada.

### Erros e limites

As redes internas não são automaticamente confiáveis. Mais certificados significam mais operações, a menos que a emissão seja automatizada.

### Exercícios

- **EX022 — Lacuna interna.** Que lacuna o diagrama revelou atrás do gateway? *Rubrica:* 3 = tráfego encaminhado às aplicações por HTTP simples;; 2 = HTTP simples;; 1 = nada;; 0 = nenhuma.

- **EX023 — Controle do webhook.** Que controle protege os webhooks de pagamento? *Rubrica:* 3 = assinaturas HMAC do provedor de pagamentos;; 2 = HMAC;; 1 = só TLS;; 0 = nenhuma.

- **EX024 — Fraqueza da AC.** Por que a autoridade certificadora interna é um ponto único de falha? *Rubrica:* 3 = uma única máquina virtual sem backup da chave, gerenciada pela mesma conta que o gateway;; 2 = ambos;; 1 = um;; 0 = nenhuma.

### Síntese

Traçar as fronteiras de confiança posiciona os controles criptográficos onde eles importam e expõe uma infraestrutura de confiança frágil.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Rosa Delgado, Owen Pryce, a Dr Imogen Hale, a Pinecrest Polytechnic, o Harbourview City Council e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** No departamento de TI da prefeitura, concentrando-se em construir e operar serviços integrados de forma confiável e segura.

**EX002.** O provedor as guarda, então a prefeitura precisa confiar nos contratos e nos controles do próprio provedor.

**EX003.** TLS até o portal, a conferência do hash da senha, uma notificação de pagamento assinada e um banco de dados cifrado.

**EX004.** Porque o servidor impostor não consegue mostrar um certificado confiável para o nome da prefeitura, então o navegador o rejeita.

**EX005.** Uma redação explicando que a conexão é privada, sem afirmar que o site ou os dados estão seguros.

**EX006.** O servidor omite o certificado intermediário, então os clientes não conseguem montar um caminho até uma raiz confiável.

**EX007.** Linhas com datas em branco ou malformadas vindas das exportações antigas, para que o script não falhe.

**EX008.** Uma integração enviava dados de licenças codificados em Base64 por HTTP não cifrado; ela passou para HTTPS.

**EX009.** Para uma variável de ambiente preenchida a partir do repositório de segredos, porque o código-fonte é compartilhado e versionado.

**EX010.** Nome do host, emissor, data de expiração e dono.

**EX011.** Elas barram registros incompletos no momento da entrada, antes que dados ausentes causem uma indisponibilidade.

**EX012.** O inventário é lido, exportado e copiado em backups amplamente, então os segredos ficariam expostos; eles pertencem a um repositório de segredos.

**EX013.** Uma decisão municipal assinada que não pode mudar depois de aprovada.

**EX014.** HMAC, porque o provedor e a prefeitura compartilham um segredo e precisam autenticar as mensagens.

**EX015.** As senhas devem ser armazenadas como hashes de mão única, para que ninguém consiga recuperá-las; senhas esquecidas são redefinidas, e não enviadas por e-mail.

**EX016.** Uma chave privada TLS legível por todas as contas de um servidor.

**EX017.** Ele trazia uma chave de host SSH gerada de antemão, então toda máquina nova tinha a mesma chave.

**EX018.** Porque ele espera até que o gerador do kernel esteja devidamente alimentado antes de devolver bytes aleatórios.

**EX019.** O certificado prova que o dispositivo é gerenciado pela prefeitura; a senha e o código provam que a pessoa está autorizada.

**EX020.** Para que perder uma chave não deixe o administrador sem acesso.

**EX021.** Os certificados de dispositivo de quem saía às vezes continuavam válidos por semanas.

**EX022.** O gateway encaminhava o tráfego aos servidores de aplicação por HTTP não cifrado.

**EX023.** Assinaturas HMAC nas notificações do provedor de pagamentos.

**EX024.** Ela roda numa única máquina sem backup da chave, e a mesma conta controla a autoridade e o gateway.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barker, E., & Roginsky, A. (2019). *Transitioning the use of cryptographic algorithms and key lengths* (NIST SP 800-131A Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-131Ar2>
- Barnes, R., Bhargavan, K., Lipp, B., & Wood, C. (2022). *Hybrid public key encryption* (RFC 9180). IETF. <https://www.rfc-editor.org/rfc/rfc9180>
- Barnes, R., Hoffman-Andrews, J., McCarney, D., & Kasten, J. (2019). *Automatic certificate management environment (ACME)* (RFC 8555). IETF. <https://www.rfc-editor.org/rfc/rfc8555>
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
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- Moriarty, K., Kaliski, B., Jonsson, J., & Rusch, A. (2016). *PKCS #1: RSA cryptography specifications version 2.2* (RFC 8017). IETF. <https://www.rfc-editor.org/rfc/rfc8017>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2008). *The keyed-hash message authentication code (HMAC)* (FIPS 198-1). <https://doi.org/10.6028/NIST.FIPS.198-1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2023). *Digital signature standard (DSS)* (FIPS 186-5). <https://doi.org/10.6028/NIST.FIPS.186-5>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Nystrom, M. (2005). *Identifiers and test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512* (RFC 4231). IETF. <https://www.rfc-editor.org/rfc/rfc4231>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Shoup, V. (2004). *Sequences of games: A tool for taming complexity in security proofs* (Cryptology ePrint Archive, Paper 2004/332). <https://eprint.iacr.org/2004/332>
