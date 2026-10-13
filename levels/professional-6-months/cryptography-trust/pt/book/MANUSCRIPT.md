# Criptografia e Serviços de Confiança: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 031, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais em início de carreira.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios sinalizam linhas de inventário, verificam notificações HMAC, comparam o PBKDF2 com salt com um hash rápido e resumem achados; não implementam nenhuma cifra. Sistemas de produção usam bibliotecas avaliadas, clientes ACME e repositórios de chaves gerenciados; nunca crie sua própria criptografia. Pessoas, organizações e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma analista júnior num provedor de serviços gerenciados pelos fundamentos, pelas partes interessadas, pela prática autorizada, pelos métodos centrais, pela interpretação de ferramentas, por um fluxo mensal, pela verificação, por um caso de chave exposta, pelos relatórios, pela qualidade, por um laboratório de ensaio e por um portfólio. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Dana Whitlock** | Analista de segurança júnior | Inventada |
| **Marcus Oyelaran** | Analista líder e mentor | Inventado |
| **Copperleaf Managed Services** | Provedor fictício de serviços gerenciados | Inventado |
| **Bayside Dental Group** | Cliente fictício com quatro clínicas | Inventado |

### Fontes principais

[RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 6962](https://www.rfc-editor.org/rfc/rfc6962); [RFC 4231](https://www.rfc-editor.org/rfc/rfc4231); [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4); NIST [SP 800-52 Rev. 2](https://doi.org/10.6028/NIST.SP.800-52r2) e [SP 800-131A Rev. 2](https://doi.org/10.6028/NIST.SP.800-131Ar2). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem

Você vai (1) descrever as metas de confidencialidade, integridade e autenticidade a que a criptografia serve; (2) situar a criptografia entre os demais controles; (3) conhecer o caso do provedor de serviços gerenciados usado ao longo do livro.

### 1.1 O caso

Dana Whitlock acabou de entrar no fictício provedor de serviços gerenciados Copperleaf Managed Services como analista de segurança júnior, num programa profissional de seis meses. Seu mentor é Marcus Oyelaran, analista líder. O principal cliente da Copperleaf neste livro é o fictício Bayside Dental Group, que mantém quatro clínicas com um site de agendamento para pacientes, um banco de dados de gestão clínica, notebooks da equipe, um serviço de e-mail e pagamentos com cartão por meio de um processador externo. Todas as pessoas, empresas, sistemas e números aqui são sintéticos. O trabalho de Dana é executar verificações repetíveis, registrar evidências e explicar os achados com clareza ao gerente da clínica, e não projetar nova criptografia.

### 1.2 Três metas

Marcus explica a criptografia por meio de três metas. A confidencialidade mantém os prontuários e os dados de agendamento legíveis apenas por pessoas autorizadas. A integridade torna detectáveis as alterações não autorizadas, por exemplo numa fatura ou num laudo de raio X. A autenticidade confirma quem enviou ou assinou algo, como uma notificação de pagamento do processador. A disponibilidade também importa, mas a criptografia pode prejudicá-la, por exemplo quando um certificado expira ou quando se perde uma chave de cifração de disco. Dana aprende a perguntar a que meta um controle serve antes de julgá-lo, porque a cifração sozinha não prova quem enviou uma mensagem e uma assinatura sozinha não esconde seu conteúdo.

### 1.3 Um controle entre muitos

A criptografia protege os dados em trânsito e em repouso, mas não resolve uma senha roubada, um servidor sem correções ou uma recepcionista enganada para enviar arquivos. Na Bayside, o site de agendamento usa TLS, os notebooks usam cifração de disco completo e os backups são cifrados, mas o maior incidente recente foi um e-mail de phishing. Dana aprende a situar os achados criptográficos no contexto: um certificado expirado pode ser urgente porque os pacientes veem avisos, enquanto uma configuração de cifra forte acrescenta pouco se toda a equipe compartilha uma única senha de administrador. Bons profissionais relatam as questões criptográficas com seu peso real, sem inflá-las nem descartá-las.

### Exemplo resolvido

Dana relaciona os cinco principais serviços da Bayside às três metas e anota quais controles existentes são criptográficos e quais não são.

> **Caso sintético.** A Copperleaf, o Bayside Dental Group, Dana e Marcus são inventados.

### Erros e limites

As três metas simplificam; alguns mecanismos servem a várias ao mesmo tempo. O contexto muda a prioridade, então uma lista de verificação sozinha não consegue ordenar os achados.

### Exercícios

- **EX001 — Atribuições da analista.** O que envolve o papel de Dana na Copperleaf? *Rubrica:* 3 = executar verificações repetíveis, registrar evidências e explicar achados, sem projetar criptografia;; 2 = parcial;; 1 = projeta cifras;; 0 = nenhuma.

- **EX002 — Assinatura e sigilo.** Uma assinatura digital numa fatura a mantém confidencial? *Rubrica:* 3 = não; dá integridade e autenticidade, não confidencialidade;; 2 = diz que não;; 1 = diz que sim;; 0 = nenhuma.

- **EX003 — Dano à disponibilidade.** Dê uma forma pela qual a criptografia pode reduzir a disponibilidade. *Rubrica:* 3 = certificado expirado ou chave de cifração perdida;; 2 = um exemplo;; 1 = nada;; 0 = nenhuma.

- **EX004 — Maior incidente.** Qual foi o maior incidente recente da Bayside, e o que ele ensina? *Rubrica:* 3 = phishing; a criptografia é um controle entre muitos;; 2 = cita o phishing;; 1 = cita uma cifra;; 0 = nenhuma.

- **EX005 — Pesando os achados.** Por que um certificado expirado pode ter prioridade sobre uma configuração de cifra? *Rubrica:* 3 = os pacientes veem avisos e o serviço falha; o impacto importa mais que a força teórica;; 2 = impacto;; 1 = sempre iguais;; 0 = nenhuma.

### Síntese

Os profissionais julgam cada controle criptográfico pela meta a que ele serve e pelo seu peso real entre todos os controles de um cliente.

<a id="ch-02"></a>

## Capítulo 2 — Criptografia e serviços de confiança: contexto de serviços e partes interessadas

### Objetivos de aprendizagem

Você vai (1) identificar as partes interessadas afetadas pelos serviços criptográficos de um cliente; (2) registrar os donos e os fornecedores dos serviços; (3) explicar os achados na linguagem das partes interessadas.

### 2.1 Quem se importa com o quê

Marcus pede a Dana que liste as pessoas afetadas pela criptografia da Bayside. Os pacientes se importam com que o site de agendamento seja privado e não mostre avisos. O gerente da clínica se importa com custos, indisponibilidade e deveres regulatórios relativos a dados de saúde. A equipe da recepção se importa com que os notebooks liguem e o e-mail funcione. O processador de pagamentos se importa com que a Bayside verifique suas notificações e proteja os dados de cartão. O desenvolvedor do site, uma pequena agência externa, se importa com as renovações de certificados que configurou anos atrás. Cada parte interessada ouve o mesmo achado de forma diferente, então Dana aprende a escrevê-lo em termos do que cada uma precisa saber ou fazer.

### 2.2 Donos e fornecedores

Para cada serviço, Dana registra o dono de negócio, o dono técnico e o fornecedor. O site de agendamento pertence ao gerente da clínica, é operado tecnicamente pela agência e hospedado por um provedor de nuvem. O serviço de e-mail é uma plataforma gerenciada em que o fornecedor controla as chaves. O banco de dados de gestão clínica roda num servidor da clínica principal, mantido pela Copperleaf. Essa tabela responde a duas perguntas práticas: quem precisa aprovar uma mudança, e quem de fato pode fazê-la. Sem ela, Dana certa vez passou um dia tentando corrigir um certificado que só a agência podia renovar.

### 2.3 A linguagem das partes interessadas

O primeiro rascunho de achado de Dana dizia que o site de agendamento servia uma cadeia de certificados incompleta. O gerente da clínica não entendeu. Marcus a ajuda a reescrevê-lo: alguns pacientes com celulares mais antigos veem um aviso de segurança ao agendar, porque falta no site um arquivo que prova que o certificado é genuíno; a agência pode corrigir isso em menos de uma hora, sem custo extra. O detalhe técnico fica num apêndice para a agência. Traduzir os achados dessa forma não é simplificar a verdade; é escolher que parte da verdade cada leitor precisa para agir.

### Exemplo resolvido

Dana monta uma tabela de partes interessadas para a Bayside e reescreve duas vezes o achado da cadeia, uma para o gerente da clínica e outra para a agência.

> **Caso sintético.** As partes interessadas, os fornecedores e o achado da cadeia são sintéticos.

### Erros e limites

As tabelas de donos ficam desatualizadas quando os fornecedores mudam. A linguagem simples não pode omitir fatos que mudam a decisão.

### Exercícios

- **EX006 — Preocupação dos pacientes.** Com o que os pacientes mais se importam na criptografia do site de agendamento? *Rubrica:* 3 = privacidade e nenhum aviso do navegador;; 2 = um;; 1 = custo;; 0 = nenhuma.

- **EX007 — Duas perguntas práticas.** A que duas perguntas a tabela de donos responde? *Rubrica:* 3 = quem precisa aprovar uma mudança e quem pode fazê-la;; 2 = uma;; 1 = nada;; 0 = nenhuma.

- **EX008 — Dia desperdiçado.** Por que Dana certa vez desperdiçou um dia com um certificado? *Rubrica:* 3 = só a agência podia renová-lo e ela não tinha registrado o fornecedor;; 2 = fornecedor;; 1 = azar;; 0 = nenhuma.

- **EX009 — Redação para o gerente.** Reescreva cadeia de certificados incompleta para o gerente da clínica. *Rubrica:* 3 = alguns pacientes veem avisos porque falta um arquivo de prova; a agência pode corrigir rapidamente;; 2 = efeito do aviso;; 1 = só técnico;; 0 = nenhuma.

- **EX010 — Para onde vão os detalhes.** Para onde vai o detalhe técnico do achado? *Rubrica:* 3 = um apêndice para a agência ou o leitor técnico;; 2 = apêndice;; 1 = apagado;; 0 = nenhuma.

### Síntese

Os achados criptográficos só importam quando o dono certo os entende, então os profissionais mapeiam as partes interessadas e escrevem para cada uma.

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e manuseio de evidências

### Objetivos de aprendizagem

Você vai (1) trabalhar sob uma autorização escrita; (2) manusear evidências e dados do cliente de forma mínima; (3) proteger segredos descobertos durante um trabalho.

### 3.1 Autorização escrita

A Copperleaf nunca testa um sistema de cliente sem uma autorização assinada. Para a Bayside, ela lista os sistemas no escopo, como o site de agendamento, o servidor da clínica e os notebooks da equipe; as verificações permitidas, como leituras de certificados, varreduras de configuração TLS e revisões de permissões de arquivos; as datas; e um contato de emergência. O processador de pagamentos e o provedor de nuvem estão excluídos, porque a Bayside não pode autorizar testes nos sistemas de outra empresa. Dana guarda uma cópia da autorização com suas anotações e para imediatamente se uma verificação for tocar em algo não listado, mesmo quando o alvo extra estiver a apenas um nome de host de distância.

### 3.2 Evidências mínimas

Os dados de saúde aumentam o que está em jogo. Quando Dana verifica a cifração dos backups, ela registra as configurações da rotina de backup e uma restauração de teste de um arquivo sintético, nunca um prontuário de paciente. As evidências incluem o comando ou a tela usada, o horário com fuso, o sistema e o resultado, armazenados na pasta de evidências da Copperleaf com acesso restrito à equipe do trabalho. Ela guarda apenas o que sustenta um achado. Marcus explica que as próprias evidências são sensíveis: uma pasta de exportações de configuração de uma clínica é um alvo, então ela é cifrada em repouso e apagada no prazo acordado em contrato.

### 3.3 Segredos encontrados no trabalho

No servidor da clínica, Dana encontra um arquivo de texto com a senha do administrador do banco de dados e as credenciais de FTP da agência. Ela não os explora, não os copia e não testa se funcionam. Registra o caminho do arquivo, o tipo de segredo e o horário, informa Marcus e o dono técnico do cliente no mesmo dia e recomenda a rotação. Testar uma credencial encontrada, mesmo para provar o risco, iria além da sua autorização e poderia quebrar sistemas. Seu relatório depois mostra o achado com os segredos ocultados, o que basta para justificar a correção.

### Exemplo resolvido

Dana passa um dia de verificações na Bayside sob a autorização assinada, mantém as evidências mínimas e relata um arquivo de senhas apenas pelo caminho.

> **Caso sintético.** A autorização, o servidor e o arquivo de senhas são sintéticos.

### Erros e limites

A autorização não elimina a necessidade de cuidado em produção. As regras de retenção variam conforme o contrato e a jurisdição.

### Exercícios

- **EX011 — Sistemas excluídos.** Por que o processador e o provedor de nuvem estão fora do escopo? *Rubrica:* 3 = a Bayside não pode autorizar testes nos sistemas de outra empresa;; 2 = propriedade;; 1 = razões técnicas;; 0 = nenhuma.

- **EX012 — Evidência da verificação de backup.** Como Dana evidencia a cifração dos backups sem dados de pacientes? *Rubrica:* 3 = registra as configurações da rotina e restaura um arquivo de teste sintético;; 2 = arquivo sintético;; 1 = usa um prontuário;; 0 = nenhuma.

- **EX013 — Evidência como alvo.** Por que a própria pasta de evidências é protegida? *Rubrica:* 3 = contém configurações sensíveis do cliente; é cifrada e apagada no prazo;; 2 = sensível;; 1 = não é sensível;; 0 = nenhuma.

- **EX014 — Credenciais encontradas.** Dana deve testar as credenciais de FTP encontradas para provar que funcionam? *Rubrica:* 3 = não; isso excede a autorização e pode quebrar sistemas; relatar e recomendar rotação;; 2 = não;; 1 = sim;; 0 = nenhuma.

- **EX015 — Ocultação.** Como o relatório mostra o achado do arquivo de senhas? *Rubrica:* 3 = com os segredos ocultados, apenas caminho e tipo;; 2 = ocultados;; 1 = segredos completos;; 0 = nenhuma.

### Síntese

O manuseio de evidências autorizado, mínimo e cuidadoso mantém um trabalho dentro da lei e impede que ele crie nova exposição.

<a id="ch-04"></a>

## Capítulo 4 — Criptografia e serviços de confiança: métodos centrais

### Objetivos de aprendizagem

Você vai (1) explicar cifração simétrica, hashing, MACs e assinaturas em termos práticos; (2) explicar certificados e cadeias; (3) escolher o método certo para uma necessidade do cliente.

### 4.1 Quatro blocos de construção

Marcus resume os blocos de construção. A cifração simétrica, como o AES no modo GCM da NIST SP 800-38D, usa uma chave para cifrar e decifrar e também detecta adulterações. Um hash, como o SHA-256 da FIPS 180-4, dá uma impressão digital de tamanho fixo dos dados que qualquer pessoa pode calcular. Um código de autenticação de mensagem, como o HMAC, exige uma chave compartilhada e prova que uma mensagem veio de alguém que a possui. Uma assinatura digital, como o Ed25519 da RFC 8032 ou o ECDSA da FIPS 186-5, usa uma chave privada para assinar e uma chave pública para verificar, então qualquer pessoa pode conferi-la sem ser capaz de assinar.

### 4.2 Certificados e cadeias

Um certificado, definido na RFC 5280, vincula um nome como book.bayside.example a uma chave pública e é assinado por uma autoridade certificadora. Os navegadores confiam num pequeno conjunto de autoridades raiz; as raízes assinam intermediárias, e as intermediárias assinam certificados de servidor. O navegador verifica a cadeia do certificado do servidor até uma raiz confiável, confere o nome e as datas de validade e só então prossegue. Dana aprende que a maioria dos problemas de certificados que ela verá não é matemática quebrada, mas questões operacionais: datas expiradas, intermediárias ausentes, nomes errados ou uma chave privada guardada onde gente demais pode lê-la.

### 4.3 Ligando o método à necessidade

Dana pratica com necessidades da Bayside. Proteger o formulário de agendamento em trânsito pede TLS. Detectar se um arquivo de exportação noturna foi corrompido pede um hash, com o valor esperado entregue separadamente. Provar que as notificações de pagamento vieram do processador pede um HMAC com um segredo compartilhado, ou uma assinatura se o processador publica uma chave pública. Permitir que os pacientes verifiquem um PDF de plano de tratamento assinado pede uma assinatura. Proteger um backup em repouso pede cifração autenticada, com a chave guardada separada do backup. Acertar essa correspondência é a habilidade central do profissional.

### Exemplo resolvido

Dana preenche uma tabela com seis necessidades da Bayside, escolhendo TLS, hash, HMAC, assinatura ou cifração autenticada para cada uma e indicando quem guarda a chave.

> **Caso sintético.** As necessidades e os nomes de host são sintéticos; as normas citadas são reais.

### Erros e limites

Sistemas reais combinam métodos; o próprio TLS usa os quatro blocos. Um hash sem um valor de referência confiável não prova nada sobre adulteração.

### Exercícios

- **EX016 — MAC versus assinatura.** Por que quem verifica um MAC pode forjar tags e quem verifica uma assinatura não pode? *Rubrica:* 3 = quem verifica assinaturas não pode forjar, porque tem apenas a chave pública; quem verifica MACs tem a mesma chave e poderia criar tags;; 2 = assimetria de chaves;; 1 = nenhuma diferença;; 0 = nenhuma.

- **EX017 — Ordem da cadeia.** Descreva a cadeia que um navegador verifica para o site de agendamento. *Rubrica:* 3 = certificado do servidor assinado pela intermediária, assinada por uma raiz confiável, mais nome e datas;; 2 = cadeia parcial;; 1 = nenhuma cadeia;; 0 = nenhuma.

- **EX018 — Problemas típicos.** Que tipo de problema de certificado Dana vai encontrar com mais frequência? *Rubrica:* 3 = operacionais: expiração, intermediárias ausentes, nomes errados, chaves expostas;; 2 = dois;; 1 = matemática quebrada;; 0 = nenhuma.

- **EX019 — Método para backup.** Que método protege um backup em repouso, e onde deve ficar a chave? *Rubrica:* 3 = cifração autenticada com a chave guardada separada do backup;; 2 = método;; 1 = hash;; 0 = nenhuma.

- **EX020 — Plano de tratamento assinado.** Que método permite aos pacientes verificar que um PDF de plano de tratamento veio da Bayside? *Rubrica:* 3 = assinatura digital verificada com uma chave pública;; 2 = assinatura;; 1 = cifração;; 0 = nenhuma.

### Síntese

Escolher entre cifração, hashes, MACs, assinaturas e certificados conforme a necessidade é a habilidade criptográfica central do profissional.

<a id="ch-05"></a>

## Capítulo 5 — Criptografia e serviços de confiança: ferramentas e interpretação

### Objetivos de aprendizagem

Você vai (1) executar uma verificação de inventário sobre certificados e algoritmos; (2) interpretar a saída das ferramentas sem afirmar além do que ela mostra; (3) distinguir achados de ruído das ferramentas.

### 5.1 Uma verificação de inventário

A Copperleaf mantém um inventário simples por cliente: cada endpoint, a expiração do seu certificado, o tipo e o tamanho da sua chave, seu algoritmo de assinatura e as versões de TLS que aceita. Dana escreve um script curto que lê o inventário sintético da Bayside e sinaliza as linhas que violam a linha de base da Copperleaf: certificados que expiram em até trinta dias, chaves RSA menores que 2048 bits, assinaturas SHA-1 e aceitação de TLS 1.0 ou 1.1. A linha de base segue orientações do NIST como a SP 800-131A Rev. 2 e a SP 800-52 Rev. 2. O laboratório abaixo mostra as sinalizações de cinco endpoints sintéticos e a contagem dos limpos.

### Laboratório — Sinalizações da linha de base

```python
# Flag synthetic endpoints against a simple baseline (NIST SP 800-131A/800-52 inspired).
import datetime
REVIEW = datetime.date(2026, 3, 1)
eps = [("book.bayside.example", "2026-03-18", "RSA", 2048, "sha256", ["1.2", "1.3"]),
       ("clinic-srv.bayside.lan", "2027-01-10", "RSA", 1024, "sha256", ["1.2"]),
       ("printer.bayside.lan", "2028-05-02", "RSA", 2048, "sha1", ["1.0", "1.2"]),
       ("mail-gw.bayside.example", "2026-09-30", "ECDSA", 256, "sha256", ["1.1", "1.2", "1.3"]),
       ("api.bayside.example", "2026-11-20", "ECDSA", 256, "sha256", ["1.3"])]
clean = 0
for host, exp, kt, bits, sig, vers in eps:
    f = []
    d = (datetime.date.fromisoformat(exp) - REVIEW).days
    if d <= 30: f.append(f"expires in {d} d")
    if kt == "RSA" and bits < 2048: f.append(f"RSA-{bits}")
    if sig == "sha1": f.append("SHA-1 signature")
    old = [v for v in vers if v in ("1.0", "1.1")]
    if old: f.append("TLS " + "/".join(old))
    if f: print(f"{host:26} " + "; ".join(f))
    else: clean += 1
print("clean endpoints:", clean)
```

Execute com `python3 lab_inventory.py`. Saída verificada:

```text
book.bayside.example       expires in 17 d
clinic-srv.bayside.lan     RSA-1024
printer.bayside.lan        SHA-1 signature; TLS 1.0
mail-gw.bayside.example    TLS 1.1
clean endpoints: 1
```

### 5.2 Interpretando a saída

Uma sinalização é uma pergunta, não um veredito. O script sinaliza a impressora antiga da clínica por TLS 1.0, mas a impressora fica numa rede isolada e só o servidor fala com ela. A sinalização continua verdadeira, mas o risco é menor que o de um site público. Dana registra a sinalização, acrescenta o contexto e deixa a classificação de risco refletir as duas coisas. Ela também anota de onde vieram os dados e quando, porque um inventário exportado no mês passado pode não conter um certificado renovado ontem. Interpretar a saída significa declarar o que a ferramenta mediu, o que ela não conseguiu ver e o que isso implica para o cliente.

### 5.3 Ruído e falsos positivos

Os scanners muitas vezes relatam itens tecnicamente corretos, mas irrelevantes, como um certificado autoassinado numa página interna de gerenciamento acessível apenas a partir de um notebook de administrador, ou interpretam mal uma configuração. Dana confere manualmente cada sinalização numa amostra antes de relatar: ela se conecta com openssl s_client ou lê o certificado com openssl x509 e confirma o valor. As questões confirmadas viram achados; as leituras erradas são registradas como ruído da ferramenta, com uma breve explicação. Essa prática mantém os relatórios críveis, porque um achado obviamente errado faz o cliente duvidar de todas as outras linhas do relatório.

### Exemplo resolvido

Dana executa o laboratório de inventário, confirma manualmente o certificado de agendamento prestes a expirar, rebaixa com contexto a sinalização de TLS 1.0 da impressora isolada e registra uma leitura errada do scanner como ruído.

> **Caso sintético.** Os endpoints, os tamanhos e as datas são sintéticos; a NIST SP 800-131A Rev. 2 e a SP 800-52 Rev. 2 são reais.

### Erros e limites

As linhas de base ficam atrás das novas orientações; revise-as anualmente. A amostragem manual pode deixar passar leituras erradas raras.

### Exercícios

- **EX021 — Regras da linha de base.** Liste as quatro regras da linha de base no script de Dana. *Rubrica:* 3 = expiração em até 30 dias, RSA abaixo de 2048, assinatura SHA-1, TLS 1.0 ou 1.1 aceito;; 2 = três;; 1 = uma;; 0 = nenhuma.

- **EX022 — Contagem de sinalizações do laboratório.** Quantos endpoints o laboratório sinalizou e quantos estavam limpos? *Rubrica:* 3 = quatro sinalizados, um limpo;; 2 = contagem de um dos lados;; 1 = errado;; 0 = nenhuma.

- **EX023 — Contexto da impressora.** Por que a sinalização de TLS 1.0 da impressora recebe classificação menor? *Rubrica:* 3 = ela está isolada e só o servidor a alcança;; 2 = isolamento;; 1 = sinalização falsa;; 0 = nenhuma.

- **EX024 — Confirmação manual.** Como Dana confirma uma sinalização antes de relatá-la? *Rubrica:* 3 = conecta com openssl s_client ou lê o certificado com openssl x509;; 2 = ferramenta citada;; 1 = confia no scanner;; 0 = nenhuma.

- **EX025 — Credibilidade.** O que um achado obviamente errado faz com um relatório? *Rubrica:* 3 = faz o cliente duvidar de todos os outros achados;; 2 = dúvida;; 1 = nada;; 0 = nenhuma.

### Síntese

As ferramentas produzem sinalizações; os profissionais as transformam em achados confirmando-as, acrescentando contexto e declarando os limites.

<a id="ch-06"></a>

## Capítulo 6 — Criptografia e serviços de confiança: fluxo operacional

### Objetivos de aprendizagem

Você vai (1) executar o fluxo mensal de verificação criptográfica da Copperleaf; (2) acompanhar os achados da descoberta ao encerramento; (3) repassar as correções ao dono certo.

### 6.1 O fluxo mensal

A Copperleaf executa uma verificação criptográfica mensal para cada cliente. A etapa um exporta o inventário e executa o script da linha de base. A etapa dois confirma as sinalizações à mão. A etapa três consulta os logs de transparência de certificados, definidos na RFC 6962, em busca de qualquer certificado emitido para os domínios do cliente que o inventário não liste. A etapa quatro classifica e registra os achados no rastreador. A etapa cinco envia o resumo ao cliente. Dana segue uma lista de verificação para cada etapa e a assina com a data. Uma lista de verificação parece monótona, mas é o que torna o fluxo repetível quando Dana está doente e um colega o executa no lugar dela.

### 6.2 Acompanhando os achados

Cada achado recebe um identificador, uma descrição, o link para a evidência, uma classificação de risco, um dono, um prazo e um status: aberto, em andamento, corrigido aguardando verificação ou encerrado. Um achado só é encerrado depois que Dana verifica a correção, e não quando o dono diz que terminou. No mês passado, a agência relatou que a cadeia do agendamento estava corrigida, mas o novo teste de Dana ainda mostrou a intermediária ausente num dos dois servidores com balanceamento de carga. O acompanhamento com verificação pega essas meias correções, e o histórico mostra ao cliente quanto tempo as questões ficam abertas, o que é útil ao discutir níveis de serviço.

### 6.3 Repassando as correções

Dana raramente corrige as coisas ela mesma. As renovações de certificados do site de agendamento vão para a agência, as questões de cifração dos notebooks vão para a equipe de desktops da Copperleaf, e as configurações da integração de pagamentos vão para o gerente da clínica, que contata o processador. Cada repasse inclui o achado, a evidência, uma sugestão de correção com uma referência, como a RFC ou a página do NIST pertinente, e o prazo. Marcus a ensina a propor em vez de ordenar: um fornecedor que entende por que uma mudança importa costuma agir mais rápido do que um que recebe uma exigência sem explicação.

### Exemplo resolvido

Dana conclui uma execução mensal para a Bayside, encontra uma cadeia corrigida pela metade num dos servidores com balanceamento de carga, mantém o achado aberto e o devolve à agência com evidências.

> **Caso sintético.** As entradas do rastreador e a troca com a agência são sintéticas; a RFC 6962 é real.

### Erros e limites

Ciclos mensais deixam passar problemas de curta duração entre as execuções. Os logs de transparência cobrem apenas ACs públicas.

### Exercícios

- **EX026 — Propósito da etapa três.** Por que consultar os logs de transparência no fluxo mensal? *Rubrica:* 3 = para encontrar certificados emitidos para domínios do cliente que não estão no inventário;; 2 = certificados não listados;; 1 = nada;; 0 = nenhuma.

- **EX027 — Regra de encerramento.** Quando um achado pode passar a encerrado? *Rubrica:* 3 = só depois que Dana verifica a correção ela mesma;; 2 = verificação;; 1 = quando o dono diz;; 0 = nenhuma.

- **EX028 — Meia correção.** Que meia correção o novo teste de Dana pegou? *Rubrica:* 3 = intermediária ainda ausente num dos dois servidores com balanceamento de carga;; 2 = um servidor;; 1 = nada;; 0 = nenhuma.

- **EX029 — Repasse dos notebooks.** Quem recebe um achado de cifração de disco dos notebooks? *Rubrica:* 3 = a equipe de desktops da Copperleaf;; 2 = equipe de desktops;; 1 = agência;; 0 = nenhuma.

- **EX030 — Propor, não ordenar.** Por que Marcus aconselha propor correções em vez de ordená-las? *Rubrica:* 3 = fornecedores que entendem o motivo agem mais rápido;; 2 = entendimento;; 1 = nenhum motivo;; 0 = nenhuma.

### Síntese

Um fluxo repetível, com encerramento verificado e repasses claros, transforma as verificações mensais em melhorias duradouras.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Dana Whitlock, Marcus Oyelaran, a Copperleaf Managed Services, o Bayside Dental Group e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Executar verificações repetíveis, guardar evidências e explicar os achados ao cliente, sem inventar criptografia.

**EX002.** Não. Uma assinatura mostra quem assinou e que o conteúdo não mudou, mas qualquer pessoa ainda pode ler o conteúdo.

**EX003.** Um certificado expirado impede os pacientes de acessar o site de agendamento, e uma chave de cifração de disco perdida torna ilegíveis os dados de um notebook.

**EX004.** Um e-mail de phishing; ele mostra que uma criptografia forte não impede que pessoas sejam enganadas, então os achados precisam de contexto.

**EX005.** Porque um certificado expirado quebra o serviço e alarma os pacientes agora, enquanto uma cifra um pouco mais fraca tem pouco impacto prático.

**EX006.** Que o agendamento seja privado e que o site abra sem avisos de segurança.

**EX007.** Quem tem autoridade para aprovar uma mudança, e quem é tecnicamente capaz de executá-la.

**EX008.** Porque a agência controlava aquele certificado e ela não tinha identificado o fornecedor antes.

**EX009.** Alguns pacientes com celulares mais antigos veem um aviso de segurança ao agendar porque falta um arquivo que prova o certificado; a agência pode corrigir isso rapidamente.

**EX010.** Para um apêndice técnico dirigido à agência, para que o resumo continue legível sem perder fatos.

**EX011.** Porque só os donos deles podem autorizar testes; a assinatura da Bayside não cobre sistemas de terceiros.

**EX012.** Registrando as configurações de cifração da rotina de backup e restaurando um arquivo de teste sintético, em vez de qualquer prontuário.

**EX013.** Porque exportações de uma clínica são valiosas para atacantes, então a pasta é cifrada, tem acesso restrito e é apagada no prazo.

**EX014.** Não. Testá-las vai além da sua autorização; ela relata o caminho e o tipo e recomenda a rotação.

**EX015.** Lista o caminho do arquivo e os tipos de segredo com todos os valores ocultados, o que basta para justificar a rotação.

**EX016.** Uma assinatura pode ser conferida com uma chave pública que não consegue assinar, enquanto qualquer pessoa capaz de verificar um HMAC tem a chave compartilhada e poderia forjar tags.

**EX017.** Do certificado do servidor para sua intermediária e até uma raiz confiável, conferindo o nome e as datas de validade.

**EX018.** Os operacionais: certificados expirados, intermediárias ausentes, nomes errados e chaves privadas guardadas de forma aberta demais.

**EX019.** Cifração autenticada como o AES-GCM, com a chave armazenada separadamente da mídia de backup.

**EX020.** Uma assinatura digital, que os pacientes podem verificar com a chave pública ou o certificado da Bayside.

**EX021.** Expiração em até 30 dias, chaves RSA abaixo de 2048 bits, assinaturas SHA-1 e aceitação de TLS 1.0 ou 1.1.

**EX022.** Quatro endpoints foram sinalizados e um, a API do portal, estava limpo.

**EX023.** Porque a impressora fica num segmento isolado acessível apenas pelo servidor, então a exposição é limitada, embora a sinalização seja verdadeira.

**EX024.** Reproduzindo-a com openssl s_client ou openssl x509 e conferindo ela mesma o valor.

**EX025.** Mina a confiança em todos os outros achados, então o ruído precisa ser filtrado primeiro.

**EX026.** Para identificar qualquer certificado publicamente confiável emitido para os domínios da Bayside que o inventário não conhece.

**EX027.** Só depois que Dana testou de novo e confirmou a correção, e não apenas pela palavra do dono.

**EX028.** A agência tinha corrigido a cadeia num dos servidores com balanceamento de carga, mas o outro ainda omitia a intermediária.

**EX029.** A equipe de desktops da Copperleaf, que gerencia os notebooks da clínica.

**EX030.** Porque um fornecedor que entende por que a mudança importa costuma agir mais cedo e com mais cuidado.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Barker, E., & Roginsky, A. (2019). *Transitioning the use of cryptographic algorithms and key lengths* (NIST SP 800-131A Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-131Ar2>
- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Dworkin, M. (2007). *Recommendation for block cipher modes of operation: Galois/Counter Mode (GCM) and GMAC* (NIST SP 800-38D). NIST. <https://doi.org/10.6028/NIST.SP.800-38D>
- Josefsson, S., & Liusvaara, I. (2017). *Edwards-curve digital signature algorithm (EdDSA)* (RFC 8032). IETF. <https://www.rfc-editor.org/rfc/rfc8032>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate transparency* (RFC 6962). IETF. <https://www.rfc-editor.org/rfc/rfc6962>
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2023). *Digital signature standard (DSS)* (FIPS 186-5). <https://doi.org/10.6028/NIST.FIPS.186-5>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Nystrom, M. (2005). *Identifiers and test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512* (RFC 4231). IETF. <https://www.rfc-editor.org/rfc/rfc4231>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
