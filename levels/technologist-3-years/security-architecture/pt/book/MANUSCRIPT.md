# Arquitetura e Engenharia de Segurança: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 076, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–30 de 30 têm texto didático escrito à mão; os exercícios EX001–EX090 têm resoluções correspondentes com rubricas de 0 a 3; os seis laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de tecnólogo que vão construir, verificar e operar a arquitetura de segurança em organizações pequenas e médias.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios sinalizam regras de firewall, calculam indicadores de saúde, conferem manifestos, executam regras de alerta, comparam listas de desligados e comparam taxas de reporte, sempre sobre dados sintéticos; nada toca uma rede real. Projetos de produção usam produtos e normas avaliados; nunca crie sua própria criptografia. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um estudante de tecnólogo em estágio numa transportadora de encomendas: computação, redes, programação, dados, letramento, sistemas operacionais e identidade; fundamentos de arquitetura e medição; a sequência de arquitetura e engenharia de segurança, da orientação à avaliação; métodos de pesquisa, ateliê em equipe, passagem, implantação, prática de campo e o projeto final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Tomás Ferreira** | Estudante de tecnólogo | Inventado |
| **Ruth Adeyemi** | Instrutora | Inventada |
| **Sam Okafor** | Líder de infraestrutura na Brightwater | Inventado |
| **Kestrel Polytechnic** | Instituição politécnica fictícia | Inventada |
| **Brightwater Logistics** | Operadora fictícia de quatro centros de distribuição de encomendas | Inventada |

### Fontes principais

Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Anderson, *Security Engineering* 3e (2020); Shostack, *Threat Modeling* (2014); NIST [SP 800-160 Vol. 1 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1), [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1) e [SP 800-218](https://doi.org/10.6028/NIST.SP.800-218); ISO/IEC 27002:2022. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever as partes de um sistema computacional e como elas interagem; (2) inventariar os sistemas de um centro de distribuição; (3) relacionar as partes do sistema à exposição de segurança.

### 1.1 Partes de um sistema

Tomás Ferreira é estudante de tecnólogo na fictícia Kestrel Polytechnic e faz estágio na fictícia Brightwater Logistics, que opera quatro centros de distribuição de encomendas. Sua instrutora, Ruth Adeyemi, começa pelo básico: um sistema computacional combina hardware, firmware, um sistema operacional, aplicações, dados e as pessoas que o usam. Cada camada depende da camada de baixo. O coletor portátil de um centro de distribuição, por exemplo, tem um processador, o firmware do fabricante, um sistema operacional móvel, um aplicativo de leitura e os dados das encomendas que ele envia ao serviço central de rastreamento.

### 1.2 Inventariar o centro de distribuição

Tomás percorre o centro de distribuição principal com Sam Okafor, líder de infraestrutura da Brightwater, e registra cada sistema: quarenta coletores portáteis, doze impressoras de etiquetas, seis PCs de escritório, um controlador da esteira de triagem, dois switches de rede, um controlador de rede sem fio e um serviço de rastreamento em nuvem. Para cada um, anota o responsável, o sistema operacional, quem faz a manutenção e se ele guarda dados de encomendas ou de clientes. Ele encontra três impressoras de etiquetas que ninguém assume como suas, o que significa que ninguém as atualiza. Um inventário é o primeiro controle de segurança, porque sistemas desconhecidos não podem ser protegidos.

### 1.3 Partes e exposição

Cada camada traz sua própria exposição. O hardware pode ser roubado, o firmware pode conter falhas que raramente recebem patches, os sistemas operacionais precisam de atualizações, as aplicações podem ter configurações fracas e os dados podem vazar. Tomás marca quais camadas a Brightwater consegue alterar e quais só o fornecedor consegue. O firmware dos coletores, por exemplo, só pode ser atualizado pela ferramenta do fornecedor. Anderson (2020) enfatiza que a segurança depende do sistema inteiro, incluindo as pessoas e os arranjos de manutenção, e não apenas da sua camada de software mais visível.

### Exemplo resolvido

Tomás descreve as camadas de um sistema usando um coletor, inventaria os sistemas de um centro de distribuição e mapeia quais camadas a Brightwater e os fornecedores controlam.

> **Caso sintético.** A Brightwater, a Kestrel e todas as pessoas são sintéticas; Anderson (2020) é real.

### Erros e limites

Inventários feitos percorrendo o local deixam de fora sistemas guardados em armários e veículos. A responsabilidade pode ser disputada.

### Exercícios

- **EX001 — Camadas do coletor.** Cite as camadas de um coletor portátil do centro de distribuição. *Rubrica:* 3 = processador, firmware, SO móvel, aplicativo de leitura, dados das encomendas;; 2 = três;; 1 = vago;; 0 = nenhuma.

- **EX002 — Impressoras sem responsável.** Por que as três impressoras de etiquetas sem responsável são um problema? *Rubrica:* 3 = ninguém as atualiza;; 2 = sem atualizações;; 1 = vago;; 0 = nenhuma.

- **EX003 — Camada só do fornecedor.** Que camada do coletor só o fornecedor consegue atualizar? *Rubrica:* 3 = o firmware, pela ferramenta do fornecedor;; 2 = firmware;; 1 = aplicativo;; 0 = nenhuma.

### Síntese

Conhecer cada camada de cada sistema, e quem pode alterá-la, é onde a segurança começa.

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem

Você vai (1) rastrear como os dispositivos do centro de distribuição chegam aos serviços em nuvem; (2) explicar endereços, portas e resolução de nomes; (3) identificar pontos de exposição da rede.

### 2.1 Rastrear uma leitura

Tomás acompanha a leitura de uma encomenda do coletor até a nuvem. O coletor entra na rede sem fio do centro de distribuição, recebe um endereço do roteador, consulta o nome do serviço de rastreamento pelo DNS e abre uma conexão HTTPS criptografada na porta 443. O firewall do centro de distribuição permite o tráfego web de saída, e o serviço em nuvem responde. Rastrear um caminho de ponta a ponta lhe ensina mais do que decorar tabelas de protocolos, porque ele vê onde cada componente poderia falhar ou ser atacado e qual equipe é dona de cada etapa.

### 2.2 Endereços, portas e nomes

Ruth explica três ideias. Um endereço IP identifica um dispositivo numa rede; uma porta identifica um serviço nesse dispositivo; o DNS transforma nomes em endereços. Tomás usa essas ideias para ler as regras do firewall do centro de distribuição. Uma regra permite conexões de entrada na porta 3389, usada pela área de trabalho remota, para um PC do escritório. Sam explica que ela foi aberta anos atrás para que um antigo gerente pudesse trabalhar de casa. A área de trabalho remota de entrada a partir da internet é uma rota frequente de ransomware, então a regra precisa de atenção urgente.

### 2.3 Pontos de exposição

Tomás lista todos os lugares em que a rede do centro de distribuição encontra o mundo externo: a conexão com a internet, a regra de área de trabalho remota, o link de suporte remoto do fornecedor para o controlador da esteira e a rede sem fio de visitantes usada pelos motoristas. Para cada um, anota o que é alcançável e quem o usa. Sam fecha a regra de área de trabalho remota no mesmo dia e oferece ao gerente a VPN da empresa. A rede de visitantes se revela corretamente separada. Conhecer os pontos de exposição permite que uma equipe pequena concentre o esforço onde os atacantes começariam.

### Exemplo resolvido

Tomás rastreia uma leitura até a nuvem, lê regras de firewall com endereços, portas e nomes e lista quatro pontos de exposição, fechando uma antiga regra de área de trabalho remota.

> **Caso sintético.** Os detalhes da rede são sintéticos.

### Erros e limites

As regras de firewall podem não refletir as configurações do lado da nuvem. Os links de fornecedores podem não estar documentados.

### Exercícios

- **EX004 — Porta 443.** Que porta o coletor usou, e por quê? *Rubrica:* 3 = 443, para HTTPS criptografado;; 2 = 443;; 1 = 80;; 0 = nenhuma.

- **EX005 — Risco da área de trabalho remota.** Por que a regra de entrada na porta 3389 era urgente? *Rubrica:* 3 = a área de trabalho remota pela internet é uma rota frequente de ransomware;; 2 = ransomware;; 1 = vago;; 0 = nenhuma.

- **EX006 — Lista de exposição.** Cite dois pontos de exposição que Tomás listou. *Rubrica:* 3 = conexão com a internet, regra de área de trabalho remota, link do fornecedor da esteira, rede sem fio de visitantes;; 2 = um;; 1 = vago;; 0 = nenhuma.

### Síntese

Rastrear o tráfego real e listar os pontos de exposição transforma o conhecimento de redes em ação de segurança.

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem

Você vai (1) escrever pequenos scripts em Python para conferir configurações; (2) validar entradas com segurança; (3) ler código em busca de erros comuns de segurança.

### 3.1 Scripts como ferramentas

Ruth quer tecnólogos capazes de automatizar pequenas verificações. Tomás escreve um script em Python que lê as regras exportadas do firewall do centro de distribuição e lista qualquer regra que permita tráfego de entrada vindo de qualquer lugar. Escrever a verificação uma vez significa que ela pode rodar depois de cada mudança, em vez de depender de alguém lendo as regras a olho. Ele mantém o script curto, comenta cada etapa e o testa num arquivo de exemplo contendo uma regra que ele sabe que deve ser sinalizada. Testar com um caso sabidamente ruim confirma que o script de fato encontra o que diz encontrar.

### Laboratório — Sinalizar regras de entrada abertas para qualquer origem

```python
# Flag inbound firewall rules that allow any source (synthetic export).
rules = [("in", "any", "office-pc3", 3389), ("in", "10.1.0.0/16", "printer2", 9100),
         ("out", "depot", "any", 443), ("in", "any", "switch1", 22), ("in", "vpn", "office-pc1", 3389)]
flagged = [r for r in rules if r[0] == "in" and r[1] == "any"]
for d, src, dst, port in flagged: print(f"FLAG inbound from {src} to {dst} port {port}")
print(f"{len(flagged)} of {len(rules)} rules flagged")
```

Execute com `python3 lab_rules.py`. Saída verificada:

```text
FLAG inbound from any to office-pc3 port 3389
FLAG inbound from any to switch1 port 22
2 of 5 rules flagged
```

### 3.2 Validar a entrada

O script seguinte de Tomás importa pesos de encomendas de um arquivo CSV enviado por um parceiro. Ruth pergunta o que acontece se uma linha contiver texto onde deveria haver um número, ou um peso negativo. Ele acrescenta verificações que rejeitam as linhas ruins e as relatam, em vez de travar ou armazenar bobagens em silêncio. A validação de entrada protege os sistemas tanto de erros quanto de ataques deliberados. Ele segue o princípio de validar contra o que é permitido, como números entre zero e setenta quilos, em vez de tentar listar tudo o que é proibido.

### 3.3 Ler código em busca de erros

Ruth dá à turma pequenos trechos de código para revisar. Tomás encontra uma consulta ao banco de dados montada juntando texto com a entrada do usuário, o que permite injeção; uma senha escrita no código-fonte; e uma mensagem de erro que mostra detalhes internos aos usuários. Para cada um, ele escreve o padrão mais seguro: consultas parametrizadas, segredos carregados de um cofre gerenciado e mensagens de erro genéricas, com os detalhes registrados de forma privada. Ler código em busca de erros comuns é uma habilidade que os tecnólogos usam ao revisar scripts de fornecedores e pequenas ferramentas internas.

### Exemplo resolvido

Tomás escreve e testa um script de verificação de regras, acrescenta validação por lista de permissão (allow-list) a uma importação e revisa trechos de código em busca de três erros comuns.

> **Caso sintético.** As regras e os trechos de código são sintéticos.

### Erros e limites

Scripts pequenos podem crescer sem testes. As allow-lists precisam ser atualizadas quando as regras do negócio mudam.

### Exercícios

- **EX007 — Caso sabidamente ruim.** Por que testar o script com uma regra sabidamente ruim? *Rubrica:* 3 = para confirmar que ele encontra o que diz encontrar;; 2 = confirmação;; 1 = rapidez;; 0 = nenhuma.

- **EX008 — Regras sinalizadas.** Quantas regras o laboratório sinalizou? *Rubrica:* 3 = duas: 3389 para office-pc3 e 22 para switch1;; 2 = duas;; 1 = vago;; 0 = nenhuma.

- **EX009 — Consulta mais segura.** Qual é o padrão mais seguro para consultas ao banco com entrada do usuário? *Rubrica:* 3 = consultas parametrizadas;; 2 = parâmetros;; 1 = juntar strings;; 0 = nenhuma.

### Síntese

Scripts pequenos e testados e uma leitura cuidadosa do código permitem aos tecnólogos verificar sistemas de forma confiável e identificar erros comuns.

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem

Você vai (1) descrever o modelo de dados de encomendas da Brightwater; (2) identificar os dados pessoais nele; (3) aplicar a minimização aos campos de dados.

### 4.1 O registro da encomenda

Tomás estuda o modelo de dados do serviço de rastreamento com o desenvolvedor que o mantém. Um registro de encomenda guarda um identificador, o remetente, o nome do destinatário, o endereço, o número de telefone, o peso, o nível de serviço, os eventos de leitura e uma foto da entrega. Os eventos de leitura se ligam a centros de distribuição, motoristas e horários. Entender o modelo mostra como os dados fluem e onde se acumulam. Ruth pede que a turma esboce primeiro as entidades e os relacionamentos no papel, porque um diagrama claro ajuda todos a discutir quais campos são necessários, para quem e por quanto tempo.

### 4.2 Dados pessoais

Tomás marca os campos que identificam pessoas: o nome, o endereço e o telefone do destinatário, a identidade do motorista nos eventos de leitura e as fotos de entrega que podem mostrar uma pessoa ou uma casa. Alguns campos são pessoais em combinação, como um horário de entrega e um endereço, que revelam quando alguém está em casa. Ele anota quais equipes acessam cada campo. O atendimento ao cliente precisa dos dados de contato do destinatário; os separadores do centro de distribuição precisam apenas do código postal e do nível de serviço. Mapear os dados pessoais por papel mostra onde o acesso é mais amplo do que qualquer função exige.

### 4.3 Minimizar os campos

Tomás propõe mudanças. As telas dos separadores mostram apenas o código postal, o nível de serviço e o peso. Os números de telefone são ocultados depois da entrega. As fotos de entrega são apagadas após noventa dias, a menos que haja uma reclamação aberta. O desenvolvedor estima o trabalho em duas semanas. Sam apoia, porque menos pessoas vendo dados pessoais significa menos chances de uso indevido e um impacto menor se um coletor for perdido. A minimização de dados, exigida pelas leis de proteção de dados em muitos países, é também um dos controles de segurança mais baratos ao alcance de uma pequena empresa.

### Exemplo resolvido

Tomás mapeia o modelo de dados das encomendas, marca os campos pessoais por papel e propõe três mudanças de minimização nas telas e na retenção.

> **Caso sintético.** O modelo de dados é sintético.

### Erros e limites

Campos ocultados ainda podem existir nas exportações. A exclusão por retenção precisa alcançar também os backups ao longo do tempo.

### Exercícios

- **EX010 — Campos combinados.** Como o horário de entrega e o endereço juntos podem ser pessoais? *Rubrica:* 3 = revelam quando alguém está em casa;; 2 = inferência;; 1 = vago;; 0 = nenhuma.

- **EX011 — Necessidades dos separadores.** De que campos os separadores precisam? *Rubrica:* 3 = código postal, nível de serviço e peso;; 2 = código postal;; 1 = endereço completo;; 0 = nenhuma.

- **EX012 — Retenção das fotos.** Por quanto tempo as fotos de entrega são guardadas segundo a proposta? *Rubrica:* 3 = noventa dias, a menos que haja reclamação aberta;; 2 = noventa dias;; 1 = para sempre;; 0 = nenhuma.

### Síntese

Mapear os dados pessoais no modelo de dados por função mostra como minimizar a exposição a baixo custo.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) explicar os termos centrais de segurança; (2) reconhecer ataques comuns contra empresas de logística; (3) comunicar segurança de forma simples à equipe do centro de distribuição.

### 5.1 Termos centrais

Ruth ensina um vocabulário comum. A confidencialidade mantém a informação longe das pessoas erradas; a integridade a mantém correta; a disponibilidade a mantém utilizável quando necessário. Uma vulnerabilidade é uma fraqueza; uma ameaça é algo que poderia explorá-la; o risco combina probabilidade e impacto. Um controle reduz o risco. Tomás usa esses termos ao redigir o relato da visita ao centro de distribuição, para que Sam e o gerente de operações entendam exatamente o que ele quer dizer. Um vocabulário comum evita mal-entendidos, como chamar todo problema de hack. Ele acrescenta um glossário de uma página à pasta compartilhada do centro de distribuição, para que os novos funcionários possam consultar os termos depois.

### 5.2 Ataques comuns

Tomás estuda ataques vistos na logística: falsas mensagens de texto sobre entregas que roubam dados de clientes, fraude de faturas em que criminosos se passam por fornecedores de combustível, ransomware que para a triagem e as entregas, e furto de coletores dos furgões. Ele liga cada um aos sistemas da Brightwater. A fraude de faturas mira o escritório financeiro; o ransomware atingiria o serviço de rastreamento e a esteira. Conhecer os ataques reais contra um setor orienta o treinamento e os controles melhor do que listas genéricas, porque a equipe reconhece ameaças parecidas com seu próprio trabalho. Ele confere cada ataque contra o último ano de chamados do help desk para ver quais já aconteceram localmente.

### 5.3 Falar com a equipe do centro de distribuição

Tomás prepara uma orientação de dez minutos para uma troca de turno. Ele evita jargão e usa três histórias: um motorista que relatou uma mensagem de texto de phishing, um coletor perdido que foi apagado remotamente e um e-mail de fatura com uma conta bancária alterada. Cada uma termina com uma ação: relatar, relatar, ligar para confirmar. A equipe faz perguntas práticas, como se os celulares pessoais são afetados. Ruth lembra a ele que uma boa comunicação de segurança é curta, concreta e respeitosa com o tempo das pessoas, e convida perguntas em vez de culpar os erros.

### Exemplo resolvido

Tomás define os termos centrais, liga quatro ataques do setor de logística à Brightwater e dá à equipe do centro de distribuição uma orientação de dez minutos baseada em histórias.

> **Caso sintético.** As histórias e a equipe são sintéticas.

### Erros e limites

Uma única orientação se apaga rapidamente. As histórias precisam corresponder aos riscos locais reais para continuarem críveis.

### Exercícios

- **EX013 — Definição de risco.** Como o risco é definido no capítulo? *Rubrica:* 3 = probabilidade combinada com impacto;; 2 = os dois;; 1 = só a ameaça;; 0 = nenhuma.

- **EX014 — Alvo financeiro.** Que ataque mira o escritório financeiro da Brightwater? *Rubrica:* 3 = fraude de faturas, passando-se por fornecedor de combustível;; 2 = fraude de faturas;; 1 = ransomware;; 0 = nenhuma.

- **EX015 — Ações da orientação.** Quais foram as três ações da orientação? *Rubrica:* 3 = relatar, relatar, ligar para confirmar;; 2 = duas;; 1 = vago;; 0 = nenhuma.

### Síntese

Termos compartilhados, ataques específicos do setor e briefings práticos curtos constroem o letramento em segurança.

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem

Você vai (1) endurecer a configuração de um sistema operacional; (2) explicar máquinas virtuais e contêineres; (3) gerenciar atualizações nos dispositivos do centro de distribuição.

### 6.1 Fundamentos de hardening

Tomás revisa os PCs do escritório do centro de distribuição. Hardening significa remover o que não é necessário e apertar o que resta: desativar serviços não usados, retirar os direitos de administrador local das contas do dia a dia, ativar a criptografia de disco, habilitar o firewall nativo e configurar o bloqueio de tela. Ele compara cada PC com um checklist baseado na baseline de segurança do fornecedor. Dois PCs têm usuários com direitos de administrador, o que deixaria um malware se instalar livremente. Ele documenta as mudanças e testa se o software de etiquetas do centro de distribuição continua rodando antes de implantar em todos os locais.

### 6.2 Máquinas virtuais e contêineres

A Brightwater roda sua ferramenta de planejamento de rotas numa máquina virtual, numa pequena sala de servidores. Ruth explica que um hypervisor permite que várias máquinas virtuais compartilhem o hardware mantendo-se isoladas umas das outras, e que os contêineres compartilham um único kernel do sistema operacional, mas separam as aplicações. O isolamento é útil, mas não absoluto: uma falha no hypervisor ou no kernel pode rompê-lo. Tomás observa que a máquina virtual do planejador de rotas e o servidor de arquivos compartilham um host, então aplicar patches no host importa para os dois.

### 6.3 Gerenciar as atualizações

Tomás lista as fontes de atualização: o Windows Update para os PCs, ferramentas dos fornecedores para os coletores e as impressoras, firmware para os switches e o hypervisor. Ele descobre que os coletores foram atualizados pela última vez há onze meses, porque a ferramenta do fornecedor exige uma etapa manual. Sam acerta uma janela mensal de atualização por centro de distribuição, fora dos horários de pico da triagem, com um plano de rollback. Tomás escreve um cronograma curto mostrando cada tipo de dispositivo, seu método de atualização e seu responsável. As atualizações só acontecem com confiabilidade quando alguém é dono delas e quando elas se encaixam na operação.

### Exemplo resolvido

Tomás endurece os PCs do escritório segundo uma baseline, explica os limites do isolamento da virtualização e monta um cronograma mensal de atualizações com responsáveis.

> **Caso sintético.** Os dispositivos e os cronogramas são sintéticos.

### Erros e limites

O hardening pode quebrar software legado. Hosts compartilhados concentram o risco.

### Exercícios

- **EX016 — Risco dos direitos de administrador.** Por que retirar os direitos de administrador local das contas do dia a dia? *Rubrica:* 3 = um malware poderia se instalar livremente;; 2 = malware;; 1 = rapidez;; 0 = nenhuma.

- **EX017 — Contêineres versus VMs.** Em que os contêineres diferem das máquinas virtuais? *Rubrica:* 3 = os contêineres compartilham um kernel; cada VM tem seu próprio SO sobre um hypervisor;; 2 = kernel;; 1 = vago;; 0 = nenhuma.

- **EX018 — Atualizações dos coletores.** Por que os coletores estavam onze meses desatualizados? *Rubrica:* 3 = a ferramenta do fornecedor exige uma etapa manual;; 2 = manual;; 1 = não existem atualizações;; 0 = nenhuma.

### Síntese

O hardening, a compreensão do isolamento e cronogramas de atualização com donos mantêm os sistemas operacionais confiáveis.

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem

Você vai (1) explicar autenticação e autorização; (2) desenhar acesso baseado em papéis para os centros de distribuição; (3) tratar admissões, mudanças de função e desligamentos.

### 7.1 Quem e o quê

Ruth separa duas perguntas. A autenticação pergunta quem você é, usando algo que você sabe, tem ou é. A autorização pergunta o que você pode fazer depois de identificado. Os motoristas da Brightwater entram nos coletores com um PIN de quatro dígitos compartilhado por cada equipe de furgão, então a empresa não consegue saber qual motorista fez uma leitura. Tomás recomenda o login individual, com aproximação de crachá e um PIN pessoal. A identidade individual é a base da responsabilização, porque sem ela os logs não conseguem mostrar quem fez o quê e o acesso não pode ser removido para uma única pessoa.

### 7.2 Papéis para os centros de distribuição

Tomás desenha os papéis: motorista, separador, supervisor do centro de distribuição, atendimento ao cliente, financeiro e administrador. Cada papel lista as permissões de que precisa. Os supervisores podem redistribuir encomendas, mas não alterar endereços de clientes; o atendimento ao cliente pode alterar endereços, mas não redistribuir rotas. Ele confere o desenho contra as tarefas reais acompanhando um supervisor durante um turno. O acesso baseado em papéis mantém as permissões compreensíveis, de modo que um novo supervisor recebe os direitos certos em um passo, em vez de copiar a conta de um colega e herdar o histórico dele. Os trabalhadores de agência recebem o papel de separador com uma data de término igual à do contrato.

### 7.3 Admissões, mudanças de função e desligamentos

A Brightwater contrata muitos temporários antes do inverno. Tomás escreve um processo: quem é admitido recebe um papel na data de início, quem muda de função perde os direitos antigos ao ganhar os novos, e quem se desliga é desativado no último dia, por solicitação do RH. Ele observa que as mudanças de função costumam ser esquecidas, então um separador promovido a supervisor mantém os direitos de separador para sempre. Sam acrescenta uma revisão trimestral em que os supervisores confirmam o acesso de suas equipes. Um processo curto e documentado elimina a maior parte da deriva de acessos vista em pequenas empresas.

### Exemplo resolvido

Tomás substitui os PINs compartilhados das equipes por login individual, desenha seis papéis para os centros de distribuição e escreve um processo de admissão, mudança de função e desligamento com revisão trimestral.

> **Caso sintético.** Os papéis e os processos são sintéticos.

### Erros e limites

A perda de crachás gera carga de suporte. As revisões viram carimbo sem orientação.

### Exercícios

- **EX019 — Problema do PIN compartilhado.** Por que um PIN compartilhado pela equipe é um problema? *Rubrica:* 3 = a empresa não consegue saber qual motorista fez uma leitura;; 2 = responsabilização;; 1 = PIN fraco;; 0 = nenhuma.

- **EX020 — Limites do supervisor.** O que os supervisores não podem fazer? *Rubrica:* 3 = alterar endereços de clientes;; 2 = endereços;; 1 = redistribuir encomendas;; 0 = nenhuma.

- **EX021 — Mudanças de função esquecidas.** Por que as mudanças de função são um risco? *Rubrica:* 3 = a pessoa mantém os direitos antigos ao ganhar os novos;; 2 = deriva;; 1 = vago;; 0 = nenhuma.

### Síntese

Identidades individuais, papéis claros e um processo de admissão, movimentação e desligamento são a base do controle de acesso.

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) explicar o que a arquitetura de segurança significa para uma pequena empresa; (2) aplicar os princípios centrais de projeto; (3) desenhar um diagrama simples de zonas.

### 8.1 Arquitetura para uma pequena empresa

Ruth explica que a arquitetura de segurança é o arranjo geral das proteções ao longo dos sistemas, e não um único dispositivo. Para a Brightwater, ela responde a perguntas como quais sistemas podem conversar com quais, onde as identidades são verificadas, onde os dados ficam armazenados e como os serviços se recuperam após uma falha. Mesmo uma empresa com quatro centros de distribuição se beneficia de registrar isso por escrito, porque decisões tomadas uma de cada vez tendem a se contradizer. Uma arquitetura simples dá a Sam uma referência quando fornecedores propõem novas conexões. A versão escrita também ajuda a nova equipe de TI a entender as escolhas passadas sem depender da memória.

### 8.2 Princípios de projeto

Tomás aplica os princípios clássicos de Saltzer e Schroeder (1975). Menor privilégio: cada papel recebe apenas o que precisa. Padrões seguros contra falhas (fail-safe defaults): novos dispositivos entram numa rede de quarentena até serem aprovados. Economia de mecanismo: um único serviço de identidade, em vez de logins separados por aplicação. Mediação completa: o serviço de rastreamento verifica as permissões a cada requisição, e não só no login. Separação de privilégio: as mudanças de dados bancários no financeiro exigem duas pessoas. Ele liga cada princípio a uma decisão específica da Brightwater, para que se torne prático. Ruth pede que ele marque onde dois princípios puxam em direções diferentes.

### 8.3 Um diagrama de zonas

Tomás desenha um diagrama do centro de distribuição principal com quatro zonas: escritório, dispositivos operacionais como coletores e impressoras, o sistema de controle da esteira e a rede sem fio de visitantes. Setas mostram os fluxos permitidos: os dispositivos operacionais alcançam o serviço de rastreamento em nuvem; a esteira aceita conexões apenas do gateway de suporte do fornecedor; os visitantes alcançam apenas a internet. O diagrama cabe numa página. Sam o afixa ao lado do rack de rede, para que qualquer pessoa que faça mudanças possa conferir se uma nova conexão se encaixa no projeto antes de plugar o cabo.

### Exemplo resolvido

Tomás explica a arquitetura para uma pequena empresa, liga cinco princípios a decisões da Brightwater e desenha um diagrama de quatro zonas com os fluxos permitidos.

> **Caso sintético.** As zonas e os fluxos são sintéticos; Saltzer e Schroeder (1975) é real.

### Erros e limites

Diagramas de uma página omitem detalhes. Os princípios podem entrar em conflito na prática.

### Exercícios

- **EX022 — Por que registrar.** Por que uma pequena empresa se beneficia de uma arquitetura escrita? *Rubrica:* 3 = decisões tomadas uma de cada vez se contradizem;; 2 = consistência;; 1 = vago;; 0 = nenhuma.

- **EX023 — Exemplo de fail-safe.** Como a Brightwater aplica os padrões seguros contra falhas? *Rubrica:* 3 = novos dispositivos entram numa rede de quarentena até serem aprovados;; 2 = quarentena;; 1 = rede aberta;; 0 = nenhuma.

- **EX024 — Fluxo da esteira.** O que pode se conectar ao sistema de controle da esteira? *Rubrica:* 3 = apenas o gateway de suporte do fornecedor;; 2 = gateway;; 1 = qualquer coisa;; 0 = nenhuma.

### Síntese

Mesmo empresas pequenas precisam de uma arquitetura escrita, fundamentada em princípios, e de um diagrama de zonas simples.

<a id="ch-09"></a>

## Capítulo 9 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher medidas simples da saúde da segurança; (2) calculá-las a partir de exportações; (3) relatar tendências aos gestores.

### 9.1 Escolher as medidas

Sam pergunta a Tomás como a Brightwater pode saber se está melhorando. Tomás propõe cinco medidas: a parcela de dispositivos atualizados em até trinta dias, a parcela de funcionários que usam login individual, o número de regras de entrada vindas da internet, os dias entre o desligamento e a desativação da conta e o número de dispositivos sem responsável. Cada uma é barata de coletar a partir das exportações existentes. Ele escreve uma definição de uma linha para cada, para que o número signifique a mesma coisa todo mês, e registra de onde vêm os dados e quem os produz.

### Laboratório — Indicadores mensais de saúde da segurança a partir de exportações

```python
# Monthly security health figures from synthetic exports.
import datetime as dt
today = dt.date(2026, 3, 31)
updated = [dt.date(2026, 3, d) for d in range(3, 32)] + [dt.date(2026, 1, 15)] * 31   # 60 devices
owners = ["sam"] * 57 + [None] * 3
leavers = [(dt.date(2026, 3, 2), dt.date(2026, 3, 3)), (dt.date(2026, 3, 9), dt.date(2026, 3, 16)),
           (dt.date(2026, 3, 20), dt.date(2026, 3, 24))]
recent = sum((today - d).days <= 30 for d in updated)
print(f"updated within 30 days: {recent}/{len(updated)} = {recent/len(updated):.0%}")
print(f"unowned devices: {owners.count(None)}")
days = [(off - left).days for left, off in leavers]
print(f"days to disable leavers: {days}, average {sum(days)/len(days):.0f}")
```

Execute com `python3 lab_health.py`. Saída verificada:

```text
updated within 30 days: 29/60 = 48%
unowned devices: 3
days to disable leavers: [1, 7, 4], average 4
```

### 9.2 Calcular a partir das exportações

Tomás escreve um script que lê exportações sintéticas de dispositivos e de contas e calcula as medidas. O laboratório mostra o mês atual: vinte e nove de sessenta dispositivos atualizados em até trinta dias, três dispositivos sem responsável e uma média de quatro dias para desativar quem se desligou. Ele confere à mão uma amostra de registros para garantir que o script lê as datas corretamente. Um pequeno erro na interpretação das datas faria todos os meses parecerem melhores ou piores do que a realidade, minando a confiança no relatório inteiro. Ele também guarda as exportações brutas por um mês, para que os números possam ser reconferidos.

### 9.3 Relatar tendências

Tomás apresenta três meses de números ao gerente de operações numa tabela simples, com setas mostrando a direção. Ele explica o que cada número significa e que ação ele sugere. A parcela de atualizações é o número mais fraco, o que apoia a janela mensal de atualização acertada no capítulo 6. Ele evita notas codificadas por cor que escondem detalhes. O gerente pede o relatório todo mês. As tendências importam mais do que números isolados, porque mostram se as mudanças estão funcionando e dão um aviso antecipado quando algo escorrega.

### Exemplo resolvido

Tomás define cinco medidas de saúde, calcula-as a partir de exportações sintéticas com uma amostra conferida à mão e relata uma tendência de três meses.

> **Caso sintético.** As exportações e os números são sintéticos.

### Erros e limites

As medidas podem ser manipuladas depois que se fixam metas. As exportações podem deixar dispositivos de fora.

### Exercícios

- **EX025 — Definições das medidas.** Por que escrever uma definição de uma linha para cada medida? *Rubrica:* 3 = para que signifique a mesma coisa todo mês;; 2 = consistência;; 1 = vago;; 0 = nenhuma.

- **EX026 — Parcela de atualizações.** Qual foi a parcela de atualizações no laboratório? *Rubrica:* 3 = 29 de 60, 48%;; 2 = 48%;; 1 = vago;; 0 = nenhuma.

- **EX027 — Conferência à mão.** Por que conferir uma amostra de registros à mão? *Rubrica:* 3 = para confirmar que as datas são lidas corretamente;; 2 = interpretação;; 1 = vago;; 0 = nenhuma.

### Síntese

Algumas medidas bem definidas, calculadas a partir de exportações e mostradas como tendências, dizem aos gestores se a segurança está melhorando.

<a id="ch-10"></a>

## Capítulo 10 — Arquitetura e engenharia de segurança: orientação

### Objetivos de aprendizagem

Você vai (1) descrever o ciclo de vida da arquitetura e engenharia de segurança; (2) situar nele o papel do tecnólogo; (3) planejar o restante do estágio.

### 10.1 O ciclo de vida

Ruth apresenta o ciclo de vida descrito no NIST SP 800-160 Vol. 1 Rev. 1: entender as necessidades e o contexto, definir requisitos, projetar, construir ou adquirir, verificar, implantar, operar e desativar. A segurança pertence a todas as etapas, e não só ao final. Tomás mapeia mudanças recentes da Brightwater no ciclo. As novas impressoras de etiquetas foram compradas sem nenhum requisito de segurança, então suas senhas padrão nunca foram trocadas. Se houvesse um requisito na etapa de aquisição, o fornecedor as teria entregado configuradas corretamente. Ele acrescenta esse exemplo ao diário do estágio como uma lição sobre aquisição.

### 10.2 O papel do tecnólogo

Os tecnólogos trabalham sobretudo em construir, verificar, implantar e operar. As tarefas de Tomás vão incluir configurar dispositivos segundo o projeto, testar se os controles funcionam, documentar mudanças e identificar, na operação, problemas que deveriam mudar o projeto. Os arquitetos decidem a forma geral; os tecnólogos a tornam real e relatam onde a realidade difere do desenho. Ruth enfatiza que esse ciclo de retorno é essencial: projetos que ignoram a experiência operacional viram ficção, e os tecnólogos são as pessoas mais bem posicionadas para perceber isso. Sam concorda em fazer uma reunião mensal curta em que Tomás relate essas diferenças.

### 10.3 Planejar o estágio

Tomás acerta com Sam um plano para as semanas restantes: mapear ativos e fluxos de dados, escrever cenários de risco, aplicar dois métodos a uma mudança real, executar um laboratório guiado, construir automações, montar o monitoramento, resolver problemas e, por fim, entregar um projeto final. Cada semana tem um entregável revisado por Sam. Registrar o plano por escrito ajuda os dois lados a gerenciar expectativas e permite que Ruth confira se o estágio cobre os resultados do curso. Também dá a Tomás um registro do que ele conquistou para futuras candidaturas a emprego.

### Exemplo resolvido

Tomás mapeia as mudanças no ciclo de vida, define o papel do tecnólogo nele e acerta um plano semanal de estágio com entregáveis.

> **Caso sintético.** Os planos e os dispositivos são sintéticos; o SP 800-160 Vol. 1 Rev. 1 é real.

### Erros e limites

Os modelos de ciclo de vida parecem lineares; o trabalho real volta atrás. Os planos de estágio mudam com as necessidades do negócio.

### Exercícios

- **EX028 — Lição das impressoras.** O que deu errado com as novas impressoras de etiquetas? *Rubrica:* 3 = nenhum requisito de segurança na compra, então as senhas padrão ficaram;; 2 = requisitos;; 1 = fornecedor;; 0 = nenhuma.

- **EX029 — Etapas do tecnólogo.** Em que etapas os tecnólogos trabalham sobretudo? *Rubrica:* 3 = construir, verificar, implantar e operar;; 2 = três;; 1 = só projeto;; 0 = nenhuma.

- **EX030 — Ciclo de retorno.** Por que o retorno do tecnólogo é essencial? *Rubrica:* 3 = projetos que ignoram a operação viram ficção;; 2 = realidade;; 1 = vago;; 0 = nenhuma.

### Síntese

Os tecnólogos tornam a arquitetura real ao longo do ciclo de vida e devolvem a realidade operacional ao desenho.

<a id="ch-11"></a>

## Capítulo 11 — Arquitetura e engenharia de segurança: ativos e contexto

### Objetivos de aprendizagem

Você vai (1) ordenar os ativos por importância para o negócio; (2) descrever o contexto e as restrições do negócio; (3) ligar os ativos a atributos de segurança.

### 11.1 Ordenar os ativos

Usando o inventário do capítulo 1, Tomás pergunta aos gerentes de operações quais sistemas importam mais. O serviço de rastreamento fica em primeiro, porque sem ele as encomendas não podem ser roteadas nem rastreadas. O controlador da esteira fica em segundo, porque a triagem manual corta em dois terços a vazão do centro de distribuição. Os coletores ficam em terceiro. Os PCs do escritório importam menos, exceto os do financeiro. Ordenar pela consequência para o negócio, e não pela complexidade técnica, diz a Tomás para onde devem ir primeiro os esforços de proteção e recuperação quando o tempo é limitado. Ele registra a ordenação com a data e os nomes dos gerentes consultados, para que possa ser revisitada antes de cada alta temporada.

### 11.2 Contexto do negócio

Tomás registra as restrições que moldam o projeto. Os centros de distribuição funcionam das quatro da manhã às dez da noite, o que deixa janelas de manutenção curtas. A alta temporada no inverno triplica o volume. O fornecedor da esteira exige acesso remoto para o suporte. A rotatividade entre os separadores é alta, e muitos são trabalhadores de agência. As margens são estreitas, então ferramentas caras são difíceis de justificar. Toda recomendação de segurança precisa caber nessas restrições, e registrá-las cedo impede Tomás de propor projetos que nunca seriam aceitos. Ele compartilha a lista com Ruth para que ela possa julgar as propostas posteriores dele contra ela.

### 11.3 Ativos e atributos

Para cada ativo principal, Tomás anota qual atributo de segurança importa mais. O serviço de rastreamento precisa de disponibilidade e integridade, já que um roteamento errado causa entregas perdidas. Os dados dos clientes precisam de confidencialidade. A esteira precisa de disponibilidade e segurança física, já que comandos com defeito poderiam ferir funcionários. O financeiro precisa da integridade dos pagamentos. Ligar os ativos a atributos, no estilo dos atributos de negócio do SABSA (Sherwood, Clark e Lynas, 2005), o ajuda a escolher os controles: backups e redundância para a disponibilidade, controle de acesso e criptografia para a confidencialidade. Ele mantém a lista de atributos ao lado da ordenação dos ativos, para que as duas sejam revisadas juntas a cada ano.

### Exemplo resolvido

Tomás ordena os ativos pela consequência para o negócio, registra as restrições operacionais e liga cada ativo principal ao seu atributo de segurança mais importante.

> **Caso sintético.** As ordenações e as restrições são sintéticas; o SABSA é real.

### Erros e limites

Os gerentes podem superestimar seus próprios sistemas. Os atributos mudam com as temporadas e os contratos.

### Exercícios

- **EX031 — Ativo principal.** Que ativo ficou em primeiro, e por quê? *Rubrica:* 3 = o serviço de rastreamento; sem ele as encomendas não podem ser roteadas;; 2 = rastreamento;; 1 = esteira;; 0 = nenhuma.

- **EX032 — Exemplo de restrição.** Cite duas restrições que Tomás registrou. *Rubrica:* 3 = horário longo de funcionamento, alta temporada, acesso remoto do fornecedor, rotatividade, margens estreitas;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX033 — Atributos da esteira.** Que atributos importam mais para a esteira? *Rubrica:* 3 = disponibilidade e segurança física;; 2 = disponibilidade;; 1 = confidencialidade;; 0 = nenhuma.

### Síntese

Classificar os ativos pela consequência para o negócio, dentro das restrições reais, mostra onde concentrar a proteção.

<a id="ch-12"></a>

## Capítulo 12 — Arquitetura e engenharia de segurança: fluxos de dados

### Objetivos de aprendizagem

Você vai (1) desenhar os fluxos de dados do manuseio de encomendas; (2) marcar as fronteiras de confiança; (3) encontrar fluxos desprotegidos.

### 12.1 Desenhar os fluxos

Tomás desenha como os dados das encomendas se movem: um varejista envia um manifesto ao serviço de rastreamento; os centros de distribuição leem as encomendas; o serviço de rastreamento envia rotas aos coletores dos motoristas; os motoristas capturam fotos da entrega; os clientes recebem atualizações por mensagem de texto por meio de um provedor de mensagens. Ele rotula cada seta com os dados que ela carrega. Sam o corrige num ponto: os manifestos dos pequenos varejistas chegam por e-mail como planilhas e são enviados ao sistema à mão. Os diagramas precisam corresponder à realidade, e não à descrição oficial do processo. Ele redesenha o diagrama duas vezes até que Sam e o desenvolvedor concordem que ele corresponde ao que de fato acontece nos centros de distribuição.

### 12.2 Fronteiras de confiança

Tomás marca as fronteiras onde os dados passam entre organizações ou níveis de privilégio: do varejista para a Brightwater, da Brightwater para o provedor de mensagens, da rede do centro de distribuição para a nuvem e a caixa de e-mail onde os manifestos chegam. Cada cruzamento deveria ter verificações: autenticação do remetente, criptografia em trânsito e validação do conteúdo. Shostack (2014) recomenda examinar com cuidado cada cruzamento, porque os atacantes exploram os lugares em que uma parte supõe que a outra já verificou. Ele numera cada fronteira no diagrama e lista, para cada uma, quais das três verificações já existem e quais faltam, para que as lacunas fiquem visíveis num relance.

### 12.3 Fluxos desprotegidos

O fluxo das planilhas enviadas por e-mail não tem verificação do remetente nem validação do conteúdo, e qualquer pessoa com acesso à caixa compartilhada pode enviá-las ao sistema. Um criminoso poderia enviar um manifesto falso para desviar encomendas. Tomás recomenda passar os pequenos varejistas para um portal simples de upload com contas e validar os manifestos em busca de mudanças incomuns, como muitas atualizações de endereço de uma vez. O fluxo do provedor de mensagens é criptografado e autenticado, então ali não é preciso mudar nada. Os diagramas de fluxo de dados transformam preocupações vagas em correções específicas.

### Exemplo resolvido

Tomás desenha os fluxos de dados das encomendas, corrigido por Sam, marca quatro fronteiras de confiança e encontra um fluxo desprotegido de manifestos enviados por e-mail.

> **Caso sintético.** Os fluxos e os provedores são sintéticos; Shostack (2014) é real.

### Erros e limites

Os diagramas envelhecem rápido. Os portais acrescentam trabalho para os pequenos varejistas.

### Exercícios

- **EX034 — Correção de Sam.** O que Sam corrigiu no diagrama? *Rubrica:* 3 = pequenos varejistas enviam planilhas por e-mail, enviadas ao sistema à mão;; 2 = manifestos por e-mail;; 1 = vago;; 0 = nenhuma.

- **EX035 — Verificações na fronteira.** Que verificações cada cruzamento de fronteira deveria ter? *Rubrica:* 3 = autenticação do remetente, criptografia e validação do conteúdo;; 2 = duas;; 1 = vago;; 0 = nenhuma.

- **EX036 — Manifesto falso.** O que um criminoso poderia fazer com o fluxo por e-mail? *Rubrica:* 3 = enviar um manifesto falso para desviar encomendas;; 2 = desviar;; 1 = nada;; 0 = nenhuma.

### Síntese

Diagramas de fluxo de dados com fronteiras de confiança marcadas expõem travessias específicas sem proteção.

<a id="ch-13"></a>

## Capítulo 13 — Arquitetura e engenharia de segurança: cenários de risco

### Objetivos de aprendizagem

Você vai (1) escrever cenários de risco concretos; (2) classificá-los de forma consistente; (3) escolher tratamentos.

### 13.1 Escrever os cenários

Tomás transforma seus achados em cenários: um manifesto falso desvia encomendas de alto valor; um ransomware criptografa a máquina virtual de planejamento de rotas durante o pico; um coletor perdido expõe os dados dos destinatários; a conta de suporte do fornecedor da esteira é usada indevidamente. Cada cenário nomeia uma ameaça, uma fraqueza, um ativo e uma consequência. Cenários concretos são mais fáceis de julgar pelos gestores do que declarações abstratas de risco, porque eles conseguem imaginar o evento e reconhecê-lo pela própria experiência. Ele limita cada cenário a duas ou três frases e evita jargão técnico, para que o gerente de operações e a equipe financeira possam classificá-los sem precisar de explicação da TI.

### 13.2 Classificar de forma consistente

Tomás usa uma escala simples de três níveis para probabilidade e impacto, com exemplos para cada nível, seguindo a estrutura do NIST SP 800-30 Rev. 1. Ele pede que Sam e o gerente de operações classifiquem de forma independente. Eles concordam em três cenários, mas divergem no do coletor perdido: o gerente de operações o classifica com probabilidade alta, porque coletores somem todo mês. Esse conhecimento local muda a classificação. Comparar classificações independentes traz à tona conhecimentos escondidos e torna as classificações finais mais defensáveis. As classificações acordadas são registradas com a data da discussão.

### 13.3 Escolher os tratamentos

Para cada cenário, o grupo escolhe um tratamento. O manifesto falso é reduzido pelo portal de upload e pela validação. O ransomware é reduzido por backups offline e restaurações testadas da máquina de planejamento de rotas. O coletor perdido é reduzido pelo apagamento remoto e pela minimização dos dados nas telas. O uso indevido pelo fornecedor é reduzido por acesso com prazo limitado, aprovado por sessão. Cada tratamento tem um responsável e uma data. Um cenário de classificação baixa, a falha de uma impressora, é aceito, porque cada centro de distribuição mantém impressoras de reserva. A lista de tratamentos é arquivada com os cenários para a próxima revisão.

### Exemplo resolvido

Tomás escreve quatro cenários concretos, compara classificações independentes usando escalas no estilo do SP 800-30 e registra os tratamentos com responsáveis.

> **Caso sintético.** Os cenários e as classificações são sintéticos; o SP 800-30 Rev. 1 é real.

### Erros e limites

Escalas de três níveis são grosseiras. As listas de cenários deixam surpresas de fora.

### Exercícios

- **EX037 — Partes do cenário.** Que quatro partes cada cenário nomeia? *Rubrica:* 3 = ameaça, fraqueza, ativo e consequência;; 2 = três;; 1 = vago;; 0 = nenhuma.

- **EX038 — Diferença de classificação.** Por que o gerente de operações classificou mais alto o coletor perdido? *Rubrica:* 3 = coletores somem todo mês;; 2 = conhecimento local;; 1 = vago;; 0 = nenhuma.

- **EX039 — Risco aceito.** Que cenário foi aceito, e por quê? *Rubrica:* 3 = falha de impressora; há impressoras de reserva em cada centro;; 2 = impressora;; 1 = ransomware;; 0 = nenhuma.

### Síntese

Cenários concretos, avaliações independentes e tratamentos com donos tornam a gestão de riscos prática.

<a id="ch-14"></a>

## Capítulo 14 — Arquitetura e engenharia de segurança: métodos I

### Objetivos de aprendizagem

Você vai (1) aplicar o STRIDE ao projeto do portal de upload; (2) registrar ameaças e mitigações; (3) revisar o resultado com o desenvolvedor.

### 14.1 STRIDE no portal

A Brightwater constrói o portal de upload de manifestos recomendado no capítulo 12. Tomás aplica ao projeto o STRIDE de Shostack (2014). Spoofing (falsificação de identidade): um criminoso poderia se passar por um varejista, então as contas precisam de login forte. Tampering (adulteração): um manifesto poderia ser alterado em trânsito, então os uploads usam HTTPS. Repudiation (repúdio): um varejista poderia negar ter enviado uma mudança, então os uploads são registrados com a conta. Information disclosure (divulgação de informação): um varejista não pode ver os manifestos de outro. Denial of service (negação de serviço): arquivos enormes poderiam sobrecarregar a importação. Elevation of privilege (elevação de privilégio): uma conta de varejista não pode alcançar funções de administração.

### 14.2 Registrar os resultados

Tomás registra cada ameaça numa tabela com o elemento afetado, a mitigação, o responsável e como a mitigação será testada. Algumas mitigações já existem no framework do portal, como o HTTPS. Outras exigem trabalho: um limite de tamanho de arquivo, a separação dos dados por varejista conferida por um teste e o login multifator para as contas dos varejistas. Ele marca um item, os picos de alteração de endereços, como dependente de informação do negócio sobre o que conta como incomum. Uma tabela torna a revisão rastreável e dá ao desenvolvedor um checklist.

### 14.3 Revisar com o desenvolvedor

Tomás percorre a tabela com o desenvolvedor em trinta minutos. O desenvolvedor aponta uma ameaça que Tomás deixou passar: os e-mails de redefinição de senha do portal poderiam ser interceptados se o e-mail de um varejista estiver comprometido. Eles acrescentam uma mitigação: os links de redefinição expiram em quinze minutos e notificam o segundo contato da conta. O desenvolvedor também contesta uma mitigação como excessiva. A revisão conjunta melhora o resultado, porque os desenvolvedores sabem como o código de fato se comporta, e os tecnólogos trazem uma visão estruturada das ameaças. Eles combinam repetir a revisão sempre que o projeto do portal mudar.

### Exemplo resolvido

Tomás aplica o STRIDE ao portal, registra seis ameaças com mitigações e testes e as revisa com o desenvolvedor, que acrescenta uma ameaça na redefinição de senha.

> **Caso sintético.** O portal é sintético; Shostack (2014) é real.

### Erros e limites

O STRIDE encontra categorias, não todos os ataques. As revisões dependem do tempo disponível.

### Exercícios

- **EX040 — Divulgação de informação.** Que ameaça de divulgação de informação Tomás encontrou? *Rubrica:* 3 = um varejista ver os manifestos de outro;; 2 = entre varejistas;; 1 = vago;; 0 = nenhuma.

- **EX041 — Item que exige o negócio.** Que item precisava de informação do negócio? *Rubrica:* 3 = definir picos incomuns de alteração de endereços;; 2 = picos;; 1 = vago;; 0 = nenhuma.

- **EX042 — Ameaça esquecida.** Que ameaça o desenvolvedor acrescentou? *Rubrica:* 3 = interceptação dos e-mails de redefinição de senha;; 2 = redefinição;; 1 = vago;; 0 = nenhuma.

### Síntese

O STRIDE dá estrutura, e a revisão conjunta com os desenvolvedores detecta ameaças que cada lado, sozinho, deixaria passar.

<a id="ch-15"></a>

## Capítulo 15 — Arquitetura e engenharia de segurança: laboratório guiado

### Objetivos de aprendizagem

Você vai (1) validar manifestos em busca de mudanças suspeitas; (2) definir limiares a partir dos dados; (3) explicar os alertas à equipe de operações.

### 15.1 A tarefa do laboratório

Ruth propõe um laboratório guiado: escrever um script que compare um novo manifesto com o anterior do mesmo varejista e sinalize mudanças suspeitas, como muitas encomendas desviadas para um único endereço novo. O script roda sobre manifestos sintéticos. Tomás começa listando como é o normal: os varejistas raramente mudam mais do que alguns endereços entre um upload e outro, e quase nunca enviam muitas encomendas para um único endereço novo. Definir primeiro o normal mantém a regra ligada ao negócio, e não a palpites sobre os atacantes.

### Laboratório — Sinalizar desvios suspeitos num manifesto

```python
# Flag manifests sending more than three parcels to the same new address (synthetic).
known = {"12 Hill Rd", "4 Mill St", "7 Park Ave", "22 Dock St", "3 Elm Ct"}
manifests = {"R1": ["12 Hill Rd", "4 Mill St", "8 Oak Way", "7 Park Ave"],
             "R2": ["9 Quay Lane"] * 5 + ["22 Dock St", "3 Elm Ct"],
             "R3": ["5 Bay Rd", "5 Bay Rd", "6 Fern Cl", "12 Hill Rd"]}
for r, addrs in manifests.items():
    new = {}
    for a in addrs:
        if a not in known: new[a] = new.get(a, 0) + 1
    hits = {a: n for a, n in new.items() if n > 3}
    print(f"{r}: {len(addrs)} parcels, new addresses {new} -> {'FLAG ' + str(hits) if hits else 'ok'}")
```

Execute com `python3 lab_manifest.py`. Saída verificada:

```text
R1: 4 parcels, new addresses {'8 Oak Way': 1} -> ok
R2: 7 parcels, new addresses {'9 Quay Lane': 5} -> FLAG {'9 Quay Lane': 5}
R3: 4 parcels, new addresses {'5 Bay Rd': 2, '6 Fern Cl': 1} -> ok
```

### 15.2 Definir limiares

O script conta as encomendas cujo endereço mudou e as encomendas enviadas a um endereço que aparece pela primeira vez. Tomás define um limiar: sinalizar se mais de três encomendas forem para o mesmo endereço novo. O laboratório encontra o manifesto de um varejista com cinco encomendas desviadas para um único endereço novo, que ele marca para um telefonema ao varejista antes do despacho. Ele confere o limiar contra três meses de histórico sintético, para garantir que ele não teria sinalizado manifestos normais mais de uma vez por semana.

### 15.3 Explicar os alertas

Tomás escreve uma explicação de um parágrafo para os supervisores dos centros de distribuição: o que o alerta significa, por que importa e o que fazer, que é reter as encomendas e ligar para o varejista num número conhecido, e não num número que esteja no manifesto. Ele acrescenta um exemplo do laboratório. Os supervisores perguntam com que frequência os alertas vão aparecer; ele responde com sua estimativa histórica. Explicações claras importam, porque um alerta que ninguém entende é ignorado, e um alerta que diz o que fazer é atendido. A explicação é impressa e mantida na mesa de cada supervisor.

### Exemplo resolvido

Tomás constrói uma regra de comparação de manifestos, define um limiar conferido contra o histórico e escreve uma instrução clara para os supervisores.

> **Caso sintético.** Os manifestos e o histórico são sintéticos.

### Erros e limites

Os limiares deixam passar ataques abaixo deles. Ligar para os varejistas acrescenta atraso.

### Exercícios

- **EX043 — Normal primeiro.** Por que definir o normal antes de escrever a regra? *Rubrica:* 3 = para ligar a regra ao negócio, e não a palpites;; 2 = negócio;; 1 = vago;; 0 = nenhuma.

- **EX044 — Achado do laboratório.** O que o laboratório sinalizou? *Rubrica:* 3 = varejista R2: 5 encomendas para o novo endereço 9 Quay Lane;; 2 = cinco;; 1 = vago;; 0 = nenhuma.

- **EX045 — Número conhecido.** Por que ligar para o varejista num número conhecido? *Rubrica:* 3 = o número do manifesto pode pertencer ao criminoso;; 2 = fraude;; 1 = é mais rápido;; 0 = nenhuma.

### Síntese

Regras simples construídas a partir do comportamento normal, com instruções claras, detectam fraudes que os controles técnicos deixam passar.

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura e engenharia de segurança: métodos II

### Objetivos de aprendizagem

Você vai (1) usar uma árvore de ataque para a esteira; (2) encontrar o caminho de ataque mais barato; (3) priorizar as defesas.

### 16.1 Uma árvore de ataque

Tomás analisa o objetivo "parar a esteira durante a alta temporada". Os ramos incluem: usar indevidamente a conta de suporte remoto do fornecedor, infectar a estação de trabalho da esteira por um pendrive USB, inundar a rede de controle a partir de um PC de escritório comprometido ou danificar fisicamente o controlador. Cada ramo se divide em etapas. Construir a árvore com o engenheiro de manutenção revela que o ramo do USB é realista: os engenheiros copiam arquivos de configuração usando pendrives pessoais. As árvores de ataque trazem o pensamento do atacante para uma forma estruturada e revisável. A árvore pronta cabe numa página e fica guardada com a documentação da esteira.

### 16.2 O caminho mais barato

Tomás estima o esforço de cada folha como baixo, médio ou alto. O dano físico exige acesso ao local e é percebido rapidamente. A inundação exige um caminho do escritório para a rede de controle, que o projeto de zonas do capítulo 8 bloqueia. A conta do fornecedor exige credenciais roubadas, o que é esforço médio. O caminho do USB é de baixo esforço se um malware chegar a um pendrive pessoal. O caminho mais barato é, portanto, a rota do USB, que nenhum controle anterior tratava. A árvore aponta o esforço defensivo para a opção mais fácil do atacante.

### 16.3 Priorizar as defesas

Tomás recomenda pendrives fornecidos pela empresa e verificados para o trabalho de configuração, desativar o armazenamento USB na estação de trabalho da esteira, exceto para um dispositivo aprovado, e um backup offline da configuração do controlador. Para a conta do fornecedor, ele confirma que o acesso com prazo limitado já está em vigor. Ele apresenta as recomendações na ordem dos caminhos de ataque que elas fecham. O engenheiro de manutenção concorda, observando que o backup offline da configuração também aceleraria a recuperação após falhas comuns de hardware, trazendo um benefício para o negócio além da segurança. Sam agenda as três mudanças para a próxima janela de manutenção antes da alta temporada.

### Exemplo resolvido

Tomás constrói uma árvore de ataque para a parada da esteira, descobre que o caminho do USB é o mais barato e prioriza três defesas.

> **Caso sintético.** A árvore e as estimativas são sintéticas.

### Erros e limites

As estimativas de esforço são julgamentos. As árvores deixam de fora ramos que ninguém imaginou.

### Exercícios

- **EX046 — Ramo realista.** Que ramo o engenheiro de manutenção tornou realista? *Rubrica:* 3 = pendrives USB usados para copiar arquivos de configuração;; 2 = USB;; 1 = fornecedor;; 0 = nenhuma.

- **EX047 — Caminho bloqueado.** Por que a inundação a partir de um PC de escritório é improvável? *Rubrica:* 3 = o projeto de zonas bloqueia caminhos do escritório para o controle;; 2 = zonas;; 1 = vago;; 0 = nenhuma.

- **EX048 — Benefício extra.** Que benefício para o negócio o backup offline da configuração trouxe? *Rubrica:* 3 = recuperação mais rápida de falhas comuns de hardware;; 2 = recuperação;; 1 = vago;; 0 = nenhuma.

### Síntese

Árvores de ataque revelam o caminho mais barato para o atacante, para que as defesas o fechem primeiro.

<a id="ch-17"></a>

## Capítulo 17 — Arquitetura e engenharia de segurança: ferramentas

### Objetivos de aprendizagem

Você vai (1) escolher ferramentas para uma pequena equipe de segurança; (2) avaliar uma ferramenta num teste; (3) evitar a proliferação de ferramentas.

### 17.1 Necessidades antes das ferramentas

Fornecedores procuram a Brightwater com produtos de segurança. Tomás lista primeiro as necessidades: inventário de dispositivos, relatório de atualizações, logs centralizados, varredura de vulnerabilidades dos serviços expostos à internet e monitoramento de backups. Ele confere o que os sistemas existentes já fazem: o serviço de gestão de dispositivos cobre o inventário e as atualizações, e o provedor de nuvem oferece logging básico. Só a varredura de vulnerabilidades e os alertas sobre logs são lacunas de verdade. Partir das necessidades, e não dos produtos, evita comprar ferramentas sobrepostas que ninguém tem tempo de operar. Ele escreve a lista de necessidades numa página e pede a Sam que a ordene, para que qualquer compra posterior possa ser rastreada até uma lacuna específica e acordada.

### 17.2 Um teste

Tomás conduz um teste de duas semanas de um scanner externo de vulnerabilidades contra os endereços públicos da Brightwater, com permissão por escrito de Sam e do provedor de hospedagem. Ele define os critérios do teste: exatidão dos achados, alarmes falsos, esforço de operação e custo. O scanner encontra um banner desatualizado de servidor web no antigo portal de clientes e um certificado prestes a expirar. Também relata dois alarmes falsos sobre serviços que não estão rodando. Ele registra o tempo gasto a cada semana, porque uma ferramenta que exige horas de triagem pode não servir para uma equipe de duas pessoas.

### 17.3 Evitar a proliferação

Tomás recomenda um único scanner e o uso do logging em nuvem existente com três regras de alerta, em vez de comprar uma plataforma de monitoramento completa. Ele registra quem opera cada ferramenta, com que frequência e para onde vão os resultados. Cada ferramenta precisa ter um responsável e um propósito ligado a um cenário de risco do capítulo 13. Ferramentas sem responsável viram shelfware, que dá falso conforto. Sam aprova o plano, observando que o custo total é menor do que a cotação inicial de um único fornecedor para uma plataforma tudo-em-um. A lista de ferramentas é revisada todo ano junto com os cenários de risco.

### Exemplo resolvido

Tomás lista as necessidades antes dos produtos, testa um scanner com permissão por escrito segundo critérios definidos e recomenda um conjunto mínimo de ferramentas com responsáveis.

> **Caso sintético.** As ferramentas e os achados são sintéticos.

### Erros e limites

Os testes são curtos e podem deixar problemas passarem. Os planos gratuitos podem mudar.

### Exercícios

- **EX049 — Lacunas de verdade.** Que necessidades eram lacunas de verdade? *Rubrica:* 3 = varredura de vulnerabilidades e alertas sobre logs;; 2 = uma;; 1 = inventário;; 0 = nenhuma.

- **EX050 — Permissão para o teste.** O que Tomás obteve antes da varredura? *Rubrica:* 3 = permissão por escrito de Sam e do provedor de hospedagem;; 2 = permissão;; 1 = vago;; 0 = nenhuma.

- **EX051 — Shelfware.** O que acontece com as ferramentas sem responsável? *Rubrica:* 3 = viram shelfware que dá falso conforto;; 2 = shelfware;; 1 = vago;; 0 = nenhuma.

### Síntese

Escolha ferramentas a partir das necessidades, teste-as segundo critérios e dê a cada uma um dono e um propósito.

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura e engenharia de segurança: controles

### Objetivos de aprendizagem

Você vai (1) mapear os controles para os cenários de risco; (2) usar um catálogo de controles para conferir a cobertura; (3) registrar evidências para cada controle.

### 18.1 Controles a partir dos cenários

Tomás lista os controles já escolhidos para os cenários de risco da Brightwater: portal de upload com login multifator, validação de manifestos, backups offline, apagamento remoto, acesso do fornecedor com prazo limitado, restrições de USB na estação de trabalho da esteira e atualizações mensais. Ele mapeia cada um para os cenários que reduz. Um controle que reduz vários cenários, como as atualizações mensais, merece atenção extra, porque sua falha enfraqueceria muitas defesas de uma vez. O mapa também mostra que nenhum controle trata ainda a fraude de faturas no financeiro. Ele acrescenta a fraude de faturas à lista de lacunas a fechar em seguida.

### 18.2 Conferir a cobertura

Tomás usa a ISO/IEC 27002:2022 como catálogo para procurar lacunas. Seus controles sobre relacionamento com fornecedores, transferência de informações e descarte seguro levam a três acréscimos: uma cláusula de segurança para o fornecedor da esteira, uma regra de retorno de ligação (call-back) para as mudanças de dados bancários no financeiro e o apagamento dos coletores antes da devolução à empresa de leasing. O catálogo é usado como lista de lembretes, e não como checklist a implementar por inteiro. Tomás registra por que outros controles do catálogo não são necessários no porte da Brightwater. Os motivos ficam num apêndice curto para auditores e clientes.

### 18.3 Evidências

Para cada controle, Tomás registra o que prova que ele funciona: uma captura de tela da configuração multifator do portal, um log de teste de restauração, uma lista de coletores apagados, as aprovações das sessões do fornecedor e o relatório de atualizações. As evidências precisam ser produzidas regularmente, e não uma única vez. Ele configura lembretes para as verificações mensais e trimestrais. Sam observa que a lista de evidências também vai ajudar quando um grande cliente varejista enviar seu questionário de segurança de fornecedores, o que acontece todo ano e antes levava dias de busca. Cada item indica quem o produz e onde ele fica armazenado.

### Exemplo resolvido

Tomás mapeia sete controles para os cenários, usa a ISO/IEC 27002 para acrescentar três e define evidências regulares para cada controle.

> **Caso sintético.** Os controles e as evidências são sintéticos; a ISO/IEC 27002:2022 é real.

### Erros e limites

As evidências podem mostrar a configuração sem provar a eficácia. Os catálogos tentam à implementação excessiva.

### Exercícios

- **EX052 — Controle compartilhado.** Por que as atualizações mensais merecem atenção extra? *Rubrica:* 3 = sua falha enfraquece as defesas contra muitos cenários;; 2 = muitos cenários;; 1 = vago;; 0 = nenhuma.

- **EX053 — Acréscimos do catálogo.** Cite dois controles acrescentados a partir da ISO/IEC 27002. *Rubrica:* 3 = cláusula do fornecedor, call-back de mudança bancária, apagamento dos coletores;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX054 — Benefício nos questionários.** Como a lista de evidências vai ajudar com os clientes? *Rubrica:* 3 = respondendo rapidamente aos questionários de segurança de fornecedores;; 2 = questionários;; 1 = vago;; 0 = nenhuma.

### Síntese

Controles mapeados para cenários, conferidos com um catálogo e sustentados por evidências regulares formam uma defesa coerente.

<a id="ch-19"></a>

## Capítulo 19 — Arquitetura e engenharia de segurança: monitoramento

### Objetivos de aprendizagem

Você vai (1) escolher o que registrar em log e sobre o que alertar; (2) escrever regras de alerta simples; (3) conduzir uma rotina semanal de revisão.

### 19.1 O que registrar

Tomás decide quais eventos importam: logins no serviço de rastreamento e no portal, ações de administradores, sessões de suporte do fornecedor, mudanças de firewall, resultados de backup e sinalizações da validação de manifestos. Ele evita coletar tudo, porque uma equipe pequena não consegue revisar tudo e o armazenamento custa dinheiro. Cada fonte de log é ligada a um cenário de risco. Ele confere se os relógios dos dispositivos estão sincronizados, já que eventos com horários errados são difíceis de correlacionar ao investigar um incidente em vários sistemas. Ele também define prazos de retenção para cada fonte, guardando a maioria dos logs por noventa dias e os resultados de backup por um ano, para que as investigações tenham histórico suficiente sem custos excessivos de armazenamento.

### Laboratório — Regras de alerta simples sobre um dia de eventos

```python
# Three alert rules over a synthetic day of events: (minute, kind, subject, detail)
events = [(480 + i, "signin_fail", "r-07", "") for i in range(0, 7)] + \
         [(600, "signin_fail", "r-02", ""), (605, "signin_fail", "r-02", ""),
          (130, "vendor_session", "conveyor", "unapproved"), (840, "vendor_session", "conveyor", "approved"),
          (180, "backup", "routeplan", "fail"), (185, "backup", "files", "ok")]
alerts = []
fails = {}
for t, k, s, d in sorted(events):
    if k == "signin_fail":
        fails.setdefault(s, []).append(t)
        recent = [x for x in fails[s] if t - x <= 10]
        if len(recent) > 5 and not any(a[1] == s for a in alerts if a[0] == "signin"):
            alerts.append(("signin", s, f"{len(recent)} failures by {t//60:02d}:{t%60:02d}"))
    elif k == "vendor_session" and d != "approved":
        alerts.append(("vendor", s, f"session at {t//60:02d}:{t%60:02d} without approval"))
    elif k == "backup" and d == "fail":
        alerts.append(("backup", s, "backup failed"))
for a in alerts: print("ALERT", *a)
print(f"{len(alerts)} alerts")
```

Execute com `python3 lab_alerts.py`. Saída verificada:

```text
ALERT vendor conveyor session at 02:10 without approval
ALERT backup routeplan backup failed
ALERT signin r-07 6 failures by 08:05
3 alerts
```

### 19.2 Regras de alerta

Tomás escreve três regras: alertar quando houver mais de cinco falhas de login no portal para uma conta em dez minutos; alertar sobre qualquer sessão do fornecedor fora de uma janela aprovada; e alertar sobre um backup que falhou. O laboratório as executa sobre um dia sintético de eventos. Ele gera três alertas: uma rajada de falhas de login numa conta de varejista, uma sessão noturna do fornecedor sem aprovação e um backup que falhou. Ele investiga cada um nos dados sintéticos e escreve o que um respondente real deveria verificar primeiro.

### 19.3 Revisão semanal

Sam e Tomás definem uma revisão semanal de trinta minutos: alertas gerados, como cada um foi tratado, eventuais mudanças de regras e o status dos backups. Eles registram as decisões num log compartilhado. As regras que disparam com frequência demais são ajustadas; as que nunca disparam são testadas com um evento simulado, para garantir que ainda funcionam. Ruth observa que o monitoramento é uma rotina, e não um produto. Uma equipe pequena que revisa alguns bons alertas toda semana enxerga mais do que uma equipe grande soterrada em dashboards que ninguém lê.

### Exemplo resolvido

Tomás escolhe fontes de log ligadas aos cenários, escreve três regras de alerta testadas sobre eventos sintéticos e define uma rotina semanal de revisão.

> **Caso sintético.** Os eventos e as regras são sintéticos.

### Erros e limites

Os limiares deixam passar ataques lentos. Relógios dessincronizados confundem as investigações.

### Exercícios

- **EX055 — Sincronização dos relógios.** Por que conferir os relógios dos dispositivos? *Rubrica:* 3 = eventos com horários errados são difíceis de correlacionar;; 2 = correlação;; 1 = vago;; 0 = nenhuma.

- **EX056 — Alertas do laboratório.** Que três alertas o laboratório gerou? *Rubrica:* 3 = falhas de login de r-07, sessão noturna não aprovada do fornecedor, backup que falhou;; 2 = dois;; 1 = vago;; 0 = nenhuma.

- **EX057 — Regras silenciosas.** O que eles fazem com as regras que nunca disparam? *Rubrica:* 3 = testam-nas com um evento simulado;; 2 = testar;; 1 = apagar;; 0 = nenhuma.

### Síntese

O monitoramento é uma rotina semanal construída sobre alguns logs bem escolhidos e regras ajustadas e testadas.

<a id="ch-20"></a>

## Capítulo 20 — Arquitetura e engenharia de segurança: solução de problemas

### Objetivos de aprendizagem

Você vai (1) solucionar problemas de controles de segurança de forma metódica; (2) distinguir falhas de controle de ataques; (3) corrigir sem enfraquecer a segurança.

### 20.1 Um método

Quando os motoristas do centro de distribuição norte relatam que os coletores não conseguem sincronizar as rotas, Tomás segue um método: descrever o sintoma com precisão, verificar o que mudou recentemente, testar uma camada de cada vez a partir da rede e formular uma hipótese de cada vez. O sintoma começou naquela manhã em todos os coletores do centro norte, mas não nos outros. A mudança recente foi uma atualização do firewall na noite anterior. Uma abordagem metódica evita mudanças aleatórias que tornam os problemas mais difíceis de diagnosticar e podem remover proteções sem que ninguém perceba.

### 20.2 Falha de controle ou ataque

Tomás verifica se a causa é um ataque ou um erro de configuração. Os logs mostram os coletores chegando ao firewall e sendo bloqueados no novo endereço do serviço de rastreamento, que o provedor havia anunciado na semana anterior. A regra do firewall permitia apenas o endereço antigo. Não há sinais de atividade maliciosa. Ruth enfatiza que muitos incidentes aparentes são falhas de controle, e muitas falhas de controle parecem ataques. Conferir os logs antes de supor qualquer uma das duas coisas evita tanto o pânico quanto a complacência. Ele registra na nota do incidente quais linhas de log descartaram um ataque.

### 20.3 Corrigir com segurança

A correção rápida sugerida por um supervisor é permitir todo o tráfego de saída da zona dos coletores. Tomás, em vez disso, atualiza a regra para permitir a faixa de endereços publicada pelo provedor para o serviço e acrescenta uma nota para assinar os anúncios de mudanças do provedor. A sincronização volta em uma hora. Ele registra o incidente, a causa e a correção no log de mudanças. Resolver problemas sob pressão tenta as pessoas a remover controles; um bom tecnólogo restaura o serviço mantendo o projeto intacto. Sam acrescenta os anúncios do provedor à sua leitura semanal.

### Exemplo resolvido

Tomás soluciona uma falha de sincronização camada por camada, descarta um ataque com base nos logs e corrige a regra de firewall sem liberar todo o tráfego.

> **Caso sintético.** O incidente é sintético.

### Erros e limites

Os provedores nem sempre anunciam as mudanças. Correções rápidas viram permanentes se não forem registradas.

### Exercícios

- **EX058 — Mudança recente.** Que mudança recente apontou para a causa? *Rubrica:* 3 = uma atualização do firewall na noite anterior;; 2 = firewall;; 1 = vago;; 0 = nenhuma.

- **EX059 — Causa real.** Qual foi a causa de fato? *Rubrica:* 3 = o serviço de rastreamento mudou para um endereço novo não permitido pela regra;; 2 = endereço novo;; 1 = ataque;; 0 = nenhuma.

- **EX060 — Correção rejeitada.** Por que rejeitar a liberação de todo o tráfego de saída? *Rubrica:* 3 = remove um controle para restaurar o serviço;; 2 = enfraquece;; 1 = lenta;; 0 = nenhuma.

### Síntese

A resolução metódica de problemas restaura o serviço mantendo intactos os controles de segurança.

<a id="ch-21"></a>

## Capítulo 21 — Arquitetura e engenharia de segurança: integração de serviços

### Objetivos de aprendizagem

Você vai (1) integrar com segurança o serviço de um novo parceiro; (2) proteger as credenciais da API; (3) limitar o que um parceiro pode fazer.

### 21.1 Um novo parceiro

A Brightwater assina contrato com uma rede de armários de retirada de encomendas (lockers), para que os clientes possam retirar encomendas nos armários. A empresa dos armários precisa dos eventos de entrega e devolve as confirmações de retirada. Tomás revisa o plano de integração com o desenvolvedor. Os dados trafegam por uma interface de programação de aplicações (API) sobre HTTPS. Ele pergunta de que dados a empresa dos armários realmente precisa: o identificador da encomenda, a localização do armário e um código de retirada, mas não o endereço residencial nem o telefone do cliente. Minimizar os dados compartilhados limita o dano se o parceiro for invadido.

### 21.2 Proteger as credenciais

A API dos armários usa chaves para autenticar cada lado. Tomás insiste em que as chaves fiquem guardadas no gerenciador de segredos do provedor de nuvem, e não no código ou em arquivos de configuração, sejam diferentes para teste e produção e sejam rotacionadas a cada seis meses. As mensagens recebidas da empresa dos armários são assinadas, para que a Brightwater possa verificar sua origem. Ele segue as práticas de desenvolvimento seguro do NIST SP 800-218, que pede a proteção dos segredos e a revisão dos componentes de terceiros. Uma chave vazada permitiria a um atacante marcar encomendas como retiradas.

### 21.3 Limitar o parceiro

A chave da empresa dos armários só consegue relatar eventos de retirada das encomendas atribuídas aos seus armários; ela não consegue consultar outras encomendas nem alterar rotas. Tomás testa isso tentando buscar uma encomenda não relacionada com a chave de teste do parceiro, o que é corretamente recusado. Ele documenta a integração no diagrama de arquitetura como uma nova fronteira de confiança e acrescenta alertas para volumes incomuns de eventos de retirada. Cada integração amplia a superfície de ataque, então os limites e os testes devem ser incorporados desde o primeiro dia.

### Exemplo resolvido

Tomás minimiza os dados compartilhados com um parceiro de armários, protege as chaves da API num gerenciador de segredos e testa que a chave do parceiro não consegue consultar encomendas não relacionadas.

> **Caso sintético.** O parceiro e a API são sintéticos; o SP 800-218 é real.

### Erros e limites

Os parceiros podem mudar seus sistemas sem aviso. Os gerenciadores de segredos criam uma dependência.

### Exercícios

- **EX061 — Dados desnecessários.** De que dados a empresa dos armários não precisa? *Rubrica:* 3 = endereço residencial e telefone;; 2 = dados de contato;; 1 = código de retirada;; 0 = nenhuma.

- **EX062 — Impacto do vazamento da chave.** O que um atacante poderia fazer com uma chave vazada dos armários? *Rubrica:* 3 = marcar encomendas como retiradas;; 2 = falsa retirada;; 1 = vago;; 0 = nenhuma.

- **EX063 — Teste dos limites.** Como Tomás testou os limites do parceiro? *Rubrica:* 3 = tentou buscar uma encomenda não relacionada com a chave de teste; foi recusado;; 2 = teste;; 1 = vago;; 0 = nenhuma.

### Síntese

Integrações seguras compartilham o mínimo de dados, protegem as chaves e impõem limites testados ao que os parceiros podem fazer.

<a id="ch-22"></a>

## Capítulo 22 — Arquitetura e engenharia de segurança: automação

### Objetivos de aprendizagem

Você vai (1) automatizar uma tarefa de segurança repetitiva; (2) tornar a automação segura e revisável; (3) medir o tempo economizado.

### 22.1 Escolher uma tarefa

Tomás procura trabalho repetitivo. Todo mês, Sam compara à mão a lista de contas com a lista de desligados do RH para encontrar contas não desativadas. Isso leva duas horas, e erros se infiltram. Tomás automatiza a tarefa: um script compara as duas exportações e lista as contas de pessoas desligadas que ainda estão ativas. Bons candidatos à automação são tarefas frequentes, baseadas em regras e sujeitas a erro quando feitas à mão. As tarefas que exigem julgamento ficam com as pessoas, com a automação preparando as informações. Ele também confirma que as duas exportações usam o mesmo formato de nome de usuário antes de escrever qualquer código, já que nomes discrepantes produziriam resultados falsos.

### Laboratório — Comparação das contas com a lista de desligados

```python
# Compare active accounts with the HR leaver list (synthetic exports).
active = {"a.silva", "j.mensah", "t.ferreira", "p.kowal", "s.okafor", "l.chen"}
leavers = {"j.mensah", "p.kowal", "r.dubois"}
still_active = sorted(active & leavers)
print(f"leavers still active: {still_active}")
print(f"leavers already disabled: {sorted(leavers - active)}")
```

Execute com `python3 lab_leavers.py`. Saída verificada:

```text
leavers still active: ['j.mensah', 'p.kowal']
leavers already disabled: ['r.dubois']
```

### 22.2 Automação segura

O script apenas relata; ele não desativa contas. Sam revisa a lista e desativa as contas ele mesmo, porque alguns ex-funcionários têm prorrogações curtas aprovadas para a passagem de trabalho. Tomás guarda o script no repositório de código da empresa, acrescenta testes com dados sintéticos e registra o formato de entrada esperado. Se o RH mudar a exportação, o script falha de forma ruidosa, em vez de produzir uma lista vazia e enganosa. Uma automação que age sem revisão pode causar indisponibilidades; uma automação que relata com verificações economiza tempo com segurança.

### 22.3 Tempo economizado

O laboratório encontra duas contas ativas de pessoas desligadas, o que corresponde à última verificação manual de Sam mais uma que ele deixou passar. Rodar o script leva segundos; revisar a saída leva dez minutos. Tomás estima uma economia de quase duas horas por mês e menos contas esquecidas. Ele registra a estimativa no diário do estágio. Ruth aponta que o ganho principal não é o tempo, mas a confiabilidade: a verificação agora acontece todo mês, mesmo quando Sam está de férias, porque qualquer pessoa pode executá-la. Sam acrescenta o script ao calendário mensal de operação.

### Exemplo resolvido

Tomás automatiza uma verificação mensal de desligados como um script que apenas relata, com testes e falha ruidosa, e encontra duas contas ativas de pessoas desligadas.

> **Caso sintético.** As contas e as listas são sintéticas.

### Erros e limites

Nomes discrepantes entre sistemas causam resultados falsos. Scripts que apenas relatam ainda precisam de alguém que aja.

### Exercícios

- **EX064 — Candidatos à automação.** O que faz de uma tarefa uma boa candidata à automação? *Rubrica:* 3 = frequente, baseada em regras e sujeita a erro à mão;; 2 = duas;; 1 = tarefas de julgamento;; 0 = nenhuma.

- **EX065 — Apenas relatar.** Por que o script apenas relata? *Rubrica:* 3 = alguns desligados têm prorrogações aprovadas que exigem julgamento;; 2 = julgamento;; 1 = rapidez;; 0 = nenhuma.

- **EX066 — Resultado do laboratório.** Que contas de desligados ainda estavam ativas no laboratório? *Rubrica:* 3 = j.mensah e p.kowal;; 2 = duas;; 1 = vago;; 0 = nenhuma.

### Síntese

A automação segura reporta com clareza, falha de forma ruidosa e deixa o julgamento para as pessoas, melhorando mais a confiabilidade do que a velocidade.

<a id="ch-23"></a>

## Capítulo 23 — Arquitetura e engenharia de segurança: avaliação

### Objetivos de aprendizagem

Você vai (1) avaliar se os controles atingiram seus objetivos; (2) comparar números de antes e depois; (3) relatar os limites da avaliação.

### 23.1 Funcionou?

Seis meses depois do início do estágio, Sam pergunta se as mudanças fizeram diferença. Tomás volta às medidas de saúde do capítulo 9 e aos cenários de risco do capítulo 13. Para cada controle, ele pergunta: foi implementado, está operando e o risco mudou? Ele usa evidências, e não impressões. O portal de upload agora recebe noventa por cento dos manifestos; as planilhas por e-mail caíram para um punhado, vindo de varejistas muito pequenos. A verificação de manifestos sinalizou dois uploads suspeitos, ambos confirmados pelos varejistas como tentativas de fraude.

### 23.2 Antes e depois

Tomás compara os números. Os dispositivos atualizados em até trinta dias subiram de quarenta e oito para oitenta e cinco por cento. A média de dias para desativar desligados caiu de quatro para um. As regras de entrada vindas da internet caíram de duas para zero. Os dispositivos sem responsável caíram de três para zero. Ele apresenta cada número com sua fonte e observa que parte da melhoria pode vir de outras causas, como o fornecedor ter lançado uma ferramenta de atualização dos coletores mais fácil. Números de antes e depois são persuasivos, mas não provam, por si sós, qual mudança causou a melhoria.

### 23.3 Limites

Tomás lista o que a avaliação não consegue mostrar. A ausência de incidentes graves em seis meses pode refletir tanto a sorte quanto os controles. Duas tentativas de fraude detectadas não revelam quantas passaram. O comportamento da equipe pode escorregar depois que o estágio terminar. Ele recomenda continuar as medições todo mês e repetir a avaliação em um ano. Ruth elogia a honestidade, observando que uma avaliação que admite seus limites é mais útil aos gestores do que uma que alega sucesso completo, porque lhes diz o que continuar observando.

### Exemplo resolvido

Tomás avalia os controles com medidas de antes e depois, registra duas tentativas de fraude detectadas e lista os limites do que a avaliação mostra.

> **Caso sintético.** Os números são sintéticos.

### Erros e limites

A ausência de incidentes é uma evidência fraca. A atribuição da melhoria é incerta.

### Exercícios

- **EX067 — Parcela do portal.** Que parcela dos manifestos usa agora o portal? *Rubrica:* 3 = noventa por cento;; 2 = 90%;; 1 = todos;; 0 = nenhuma.

- **EX068 — Melhoria das atualizações.** Como mudou a parcela de atualizações em trinta dias? *Rubrica:* 3 = de 48 para 85 por cento;; 2 = subiu;; 1 = vago;; 0 = nenhuma.

- **EX069 — Nenhum incidente.** Por que a ausência de incidentes graves é uma evidência fraca? *Rubrica:* 3 = pode refletir tanto a sorte quanto os controles;; 2 = sorte;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma avaliação honesta compara os resultados medidos e declara claramente o que as evidências não conseguem provar.

<a id="ch-24"></a>

## Capítulo 24 — Métodos de pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma pequena pergunta de pesquisa aplicada; (2) coletar dados de forma ética num local de trabalho; (3) analisar e apresentar os resultados de forma simples.

### 24.1 Uma pergunta prática

Ruth pede que cada estudante responda a uma pergunta aplicada com dados. Tomás pergunta: uma mensagem de dois minutos nos coletores no início do turno reduz o número de dispositivos perdidos não relatados? A Brightwater registra os coletores perdidos e quando eles são relatados. Ele planeja comparar as oito semanas antes da mensagem com as oito semanas depois. A pergunta é pequena, respondível e útil. Ele observa a fraqueza de um desenho antes e depois: outras mudanças no mesmo período poderiam explicar qualquer diferença. Ele escreve a pergunta numa única frase e a submete à aprovação de Ruth.

### 24.2 Coleta ética

Tomás usa apenas as contagens semanais de dispositivos perdidos e relatados, sem nomes. Sam e o gerente de operações aprovam, e a equipe é informada pelo aviso de turno de que contagens anônimas serão usadas num projeto de estudante. Ruth confere o plano contra as orientações de ética da instituição. Tomás guarda as contagens no sistema da instituição e vai apagá-las depois da avaliação. Mesmo estudos simples num local de trabalho precisam do consentimento da organização, de transparência com a equipe e de dados mínimos. Ele escreve o plano num formulário de uma página assinado por Sam e arquivado com Ruth, para que a aprovação possa ser mostrada se alguém perguntar depois.

### Laboratório — Taxas de relato antes e depois da mensagem

```python
# Share of lost handhelds reported within one hour, before and after the shift message (synthetic).
before = [1] * 9 + [0] * 11
after = [1] * 17 + [0] * 4
for name, xs in (("before", before), ("after", after)):
    print(f"{name}: {sum(xs)}/{len(xs)} reported within 1 hour = {sum(xs)/len(xs):.0%}")
print(f"difference: {sum(after)/len(after) - sum(before)/len(before):+.0%} points")
```

Execute com `python3 lab_reports.py`. Saída verificada:

```text
before: 9/20 reported within 1 hour = 45%
after: 17/21 reported within 1 hour = 81%
difference: +36% points
```

### 24.3 Análise e apresentação

O laboratório compara a parcela de dispositivos perdidos relatados em até uma hora. Antes da mensagem, nove de vinte coletores perdidos foram relatados prontamente; depois dela, dezessete de vinte e um. Tomás apresenta o resultado numa tabela simples, com uma frase de cautela: a melhoria é grande, mas o desenho não consegue descartar outras causas, como o novo processo de apagamento remoto ter feito o relato parecer valer a pena. Ele recomenda manter a mensagem, já que ela não custa quase nada, e conferir o número de novo depois da alta temporada.

### Exemplo resolvido

Tomás pergunta se uma mensagem no turno melhora o relato rápido de coletores perdidos, coleta contagens anônimas com aprovação e apresenta um resultado cauteloso.

> **Caso sintético.** As contagens são sintéticas.

### Erros e limites

Desenhos antes e depois não conseguem isolar as causas. Contagens pequenas oscilam facilmente.

### Exercícios

- **EX070 — Fraqueza do desenho.** Qual é a fraqueza do desenho antes e depois? *Rubrica:* 3 = outras mudanças no mesmo período poderiam explicar as diferenças;; 2 = confusão;; 1 = vago;; 0 = nenhuma.

- **EX071 — Relato rápido.** Quais foram as taxas de relato rápido antes e depois? *Rubrica:* 3 = 9 de 20 (45%) e 17 de 21 (81%);; 2 = taxas;; 1 = vago;; 0 = nenhuma.

- **EX072 — Causa alternativa.** Que causa alternativa Tomás mencionou? *Rubrica:* 3 = o novo processo de apagamento remoto fez o relato valer a pena;; 2 = apagamento remoto;; 1 = vago;; 0 = nenhuma.

### Síntese

Pequenos estudos aplicados respondem a perguntas úteis quando os dados são coletados de forma ética e os resultados são apresentados com cautela.

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto em equipe

### Objetivos de aprendizagem

Você vai (1) trabalhar numa equipe de estudantes num projeto de segurança compartilhado; (2) dividir papéis e revisar o trabalho uns dos outros; (3) apresentar um resultado da equipe.

### 25.1 O enunciado do ateliê

De volta à instituição, Ruth conduz um ateliê. Equipes de quatro pessoas projetam a segurança de um serviço fictício de entrega de farmácia, com um site, um aplicativo móvel para os entregadores e um pequeno armazém. A equipe de Tomás inclui um desenvolvedor, um estudante de redes e uma estudante interessada em privacidade. Eles têm três semanas. O enunciado exige um diagrama de zonas, fluxos de dados, cenários de risco, controles e um plano de testes. Trabalhar em equipe espelha a prática real, em que nenhuma pessoa sozinha cobre todas as especialidades. Ruth fornece um breve perfil fictício da empresa como ponto de partida.

### 25.2 Papéis e revisão

A equipe designa um líder para cada entregável, mas exige que cada peça seja revisada por outra pessoa. Tomás lidera os cenários de risco e revisa o diagrama de zonas do estudante de redes, descobrindo que os celulares dos entregadores foram colocados na mesma zona que os sistemas do armazém. A estudante de privacidade revisa os cenários dele e acrescenta um sobre os dados das receitas visíveis nas telas dos entregadores. A revisão por pares pega erros e acrescenta perspectivas. A equipe mantém um log simples dos comentários de revisão e de como cada um foi resolvido. Cada revisor assina a entrada do log quando um comentário é resolvido.

### 25.3 Apresentar

A equipe apresenta a Ruth e a dois profissionais convidados. Eles explicam o projeto e os trade-offs, como a escolha de um login mais simples no aplicativo dos entregadores para manter as entregas rápidas, limitando ao mesmo tempo o que o aplicativo mostra. Um dos profissionais pergunta como eles lidariam com o celular roubado de um entregador; a equipe responde com seu projeto de apagamento remoto e expiração de sessão. O retorno de Ruth elogia o log de revisão, que mostra como o projeto melhorou. Os ateliês em equipe ensinam que os projetos de segurança ficam mais fortes quando construídos e questionados por várias pessoas.

### Exemplo resolvido

A equipe de Tomás projeta a segurança de um serviço de entrega de farmácia com líderes e revisão por pares, corrigindo um erro de zona e acrescentando um cenário de privacidade.

> **Caso sintético.** O serviço de farmácia e a equipe são sintéticos.

### Erros e limites

As equipes podem se curvar ao membro mais barulhento. Três semanas limitam a profundidade.

### Exercícios

- **EX073 — Erro de zona.** O que Tomás encontrou no diagrama de zonas? *Rubrica:* 3 = celulares dos entregadores na mesma zona que os sistemas do armazém;; 2 = zona;; 1 = vago;; 0 = nenhuma.

- **EX074 — Acréscimo de privacidade.** Que cenário a estudante de privacidade acrescentou? *Rubrica:* 3 = dados das receitas visíveis nas telas dos entregadores;; 2 = receitas;; 1 = vago;; 0 = nenhuma.

- **EX075 — Valor do log de revisão.** Por que Ruth elogiou o log de revisão? *Rubrica:* 3 = mostrava como o projeto melhorou;; 2 = melhoria;; 1 = extensão;; 0 = nenhuma.

### Síntese

Ateliês em equipe, com líderes claros e revisão mútua, produzem desenhos de segurança mais fortes do que indivíduos trabalhando sozinhos.

<a id="ch-26"></a>

## Capítulo 26 — Arquitetura e engenharia de segurança: passagem operacional

### Objetivos de aprendizagem

Você vai (1) preparar a equipe de operações da Brightwater para operar os novos controles; (2) escrever runbooks; (3) confirmar a prontidão antes da passagem.

### 26.1 Quem opera depois

O estágio de Tomás vai terminar, e a equipe de TI de duas pessoas da Brightwater precisará operar os controles que ele ajudou a introduzir. Ele lista cada controle e rotina: revisão semanal de alertas, atualizações mensais, o script de desligados, as verificações de manifestos, os backups e testes de restauração, as aprovações das sessões do fornecedor e as revisões trimestrais de acesso. Para cada um, nomeia o futuro responsável e o substituto. Sem uma passagem planejada, os controles introduzidos por um trabalhador temporário tendem a se deteriorar em poucos meses, porque ninguém mais sabe por que existem nem como operá-los.

### 26.2 Runbooks

Tomás escreve um runbook para cada rotina: propósito, quando executá-la, instruções passo a passo, como é a saída normal, o que fazer se falhar e para quem ligar. Ele mantém cada um com uma ou duas páginas, com capturas de tela. Ele pede a uma colega de Sam que siga sem ajuda o runbook de restauração de backup. Ela trava numa etapa em que faltava a indicação de onde fica uma senha, e Tomás corrige o runbook. Testar os runbooks com as pessoas que vão usá-los é a única forma de saber se eles funcionam.

### 26.3 Verificação de prontidão

Antes de sair, Tomás e Sam fazem uma verificação de prontidão. Cada responsável executa sua rotina uma vez, enquanto Tomás observa em silêncio. Todas as rotinas são concluídas, embora a aprovação do fornecedor demore mais do que o esperado porque o papel do aprovador não estava claro. Eles o esclarecem por escrito. Sam aprova a passagem. Tomás deixa seus contatos para dúvidas durante o primeiro mês. Ruth observa que uma boa passagem se mede por quão pouco a pessoa que sai é necessária depois. O registro de prontidão, com os tempos e o papel do aprovador esclarecido, é arquivado com o pacote de passagem para referência futura.

### Exemplo resolvido

Tomás lista os controles com responsáveis e substitutos, escreve runbooks testados e faz uma verificação silenciosa de prontidão antes da aprovação.

> **Caso sintético.** As rotinas e as pessoas são sintéticas.

### Erros e limites

Os runbooks envelhecem conforme os sistemas mudam. Equipes de duas pessoas são frágeis durante as férias.

### Exercícios

- **EX076 — Por que a passagem.** Por que os controles se deterioram sem passagem? *Rubrica:* 3 = ninguém mais sabe por que existem nem como operá-los;; 2 = conhecimento;; 1 = vago;; 0 = nenhuma.

- **EX077 — Teste do runbook.** O que o teste do runbook de restauração revelou? *Rubrica:* 3 = uma etapa sem a indicação de onde fica a senha;; 2 = lacuna;; 1 = nada;; 0 = nenhuma.

- **EX078 — Medida da passagem.** Como se mede uma boa passagem? *Rubrica:* 3 = por quão pouco a pessoa que sai é necessária depois;; 2 = independência;; 1 = extensão;; 0 = nenhuma.

### Síntese

O repasse operacional dá certo com donos nomeados, runbooks testados e uma verificação de prontidão antes da saída.

<a id="ch-27"></a>

## Capítulo 27 — Implantação e validação

### Objetivos de aprendizagem

Você vai (1) implantar com segurança uma mudança de configuração nos centros de distribuição; (2) validá-la contra os requisitos; (3) fazer rollback se necessário.

### 27.1 Planejar a implantação

A Brightwater decide impor o login individual por crachá em todos os coletores dos quatro centros de distribuição, substituindo os PINs compartilhados das equipes, conforme projetado no capítulo 7. Tomás planeja uma implantação escalonada: primeiro um centro, depois dois, depois o último. Cada etapa tem critérios de entrada, como crachás emitidos para toda a equipe, e critérios de saída, como menos de cinco chamados de ajuda com login por turno. Ele agenda as mudanças para o início do turno mais tranquilo. A implantação escalonada limita o impacto dos erros a um local de cada vez.

### 27.2 Validar

Em cada centro de distribuição, Tomás confere os requisitos: todo coletor exige crachá e PIN, as leituras registram o motorista individual, os PINs compartilhados deixam de funcionar e as contas bloqueadas podem ser redefinidas pelos supervisores. Ele testa cada requisito com um crachá de teste e registra os resultados. No segundo centro, um modelo de coletor ainda aceita o antigo PIN compartilhado por causa de uma versão de firmware mais antiga. O firmware é atualizado e o teste é repetido. A validação pega lacunas que a tela de configuração, sozinha, nunca mostraria.

### 27.3 Rollback

Tomás prepara um plano de rollback: se mais de dez por cento dos motoristas não conseguirem fazer login no início do turno, o centro volta aos PINs compartilhados naquele dia enquanto os crachás são corrigidos. O plano nunca é usado, mas tê-lo permite que os supervisores concordem com a mudança com confiança. Depois dos quatro centros, os chamados de ajuda com login se estabilizam em dois por turno. Ele registra os resultados da implantação, o problema de firmware e as lições aprendidas. Um plano de rollback claro é sinal de uma implantação profissional, e não de dúvida sobre a mudança.

### Exemplo resolvido

Tomás implanta o login por crachá em três etapas, valida quatro requisitos por centro de distribuição, pega uma lacuna de firmware e prepara um plano de rollback que não chega a ser usado.

> **Caso sintético.** Os centros de distribuição e os números são sintéticos.

### Erros e limites

Implantações escalonadas prolongam estados mistos. O rollback pode reintroduzir temporariamente controles fracos.

### Exercícios

- **EX079 — Critério de saída.** Qual era o critério de saída de cada etapa? *Rubrica:* 3 = menos de cinco chamados de ajuda com login por turno;; 2 = chamados de ajuda;; 1 = vago;; 0 = nenhuma.

- **EX080 — Lacuna de firmware.** O que a validação pegou no segundo centro? *Rubrica:* 3 = um modelo com firmware antigo ainda aceitava o PIN compartilhado;; 2 = firmware;; 1 = vago;; 0 = nenhuma.

- **EX081 — Gatilho do rollback.** O que dispararia o rollback? *Rubrica:* 3 = mais de dez por cento dos motoristas sem conseguir fazer login no início do turno;; 2 = dez por cento;; 1 = vago;; 0 = nenhuma.

### Síntese

Implantação escalonada, validação dos requisitos e um plano de reversão pronto tornam as mudanças seguras.

<a id="ch-28"></a>

## Capítulo 28 — Prática de campo

### Objetivos de aprendizagem

Você vai (1) aplicar suas habilidades numa segunda organização; (2) adaptar-se a um ambiente diferente; (3) refletir sobre a prática transferível.

### 28.1 Um segundo local

Na prática de campo, Tomás passa duas semanas num centro esportivo comunitário fictício que mantém um site de reservas, pagamentos com cartão por meio de um provedor, cartões de acesso às portas e uma pequena rede de escritório. A gerente cuida da TI junto com todo o resto. Tomás repete seu método: inventário, fluxos de dados, pontos de exposição e ganhos rápidos. O ambiente é mais simples do que o da Brightwater, mas tem menos pessoas para operar qualquer coisa. Ele começa perguntando à gerente qual indisponibilidade doeria mais, e a resposta é o site de reservas num sábado de manhã.

### 28.2 Adaptar-se

Tomás descobre que a conta de administrador do site de reservas é compartilhada por quatro funcionários, que o roteador do escritório ainda usa a senha padrão e que os cartões de acesso nunca são cancelados quando os associados saem. Ele troca a senha do roteador com a gerente, cria contas individuais de administrador com login multifator e escreve uma etapa de uma linha no procedimento de cancelamento de associação para desativar os cartões. Ele deixa de lado medidas complexas, como o logging centralizado. Adaptar-se significa escolher as poucas mudanças que mais importam para a capacidade desta organização.

### 28.3 Reflexão

Em seu diário, Tomás registra o que se transferiu: inventários, contas individuais, processos de desligamento e a verificação da exposição. O que não se transferiu: rotinas de monitoramento e automação, que pressupõem alguém com tempo. Ele reflete que os princípios de arquitetura continuam os mesmos, mas a implementação precisa caber nas pessoas disponíveis. A gerente envia um e-mail um mês depois dizendo que a etapa de cancelamento já desativou onze cartões. Ruth comenta que esse resultado prático é uma evidência de aprendizagem melhor do que qualquer prova escrita. Ele acrescenta essas observações ao relatório de estágio, para que Ruth e Sam as leiam.

### Exemplo resolvido

Tomás aplica seu método num centro esportivo, corrige três problemas prioritários adequados à capacidade dele e reflete sobre o que se transfere.

> **Caso sintético.** O centro esportivo é sintético.

### Erros e limites

Estágios curtos deixam as mudanças sem suporte. Locais pequenos podem regredir sob pressão.

### Exercícios

- **EX082 — Indisponibilidade mais dolorosa.** Que indisponibilidade doeria mais no centro esportivo? *Rubrica:* 3 = o site de reservas num sábado de manhã;; 2 = reservas;; 1 = cartões de acesso;; 0 = nenhuma.

- **EX083 — Correção dos cartões.** Como foram tratados os cartões de acesso de quem saiu? *Rubrica:* 3 = uma etapa de desativação acrescentada ao cancelamento de associação;; 2 = procedimento;; 1 = vago;; 0 = nenhuma.

- **EX084 — Evidência de aprendizagem.** Que resultado a gerente relatou um mês depois? *Rubrica:* 3 = onze cartões desativados;; 2 = onze;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática de campo mostra que os princípios se transferem, enquanto a implementação precisa se ajustar às pessoas disponíveis.

<a id="ch-29"></a>

## Capítulo 29 — Construção do projeto final

### Objetivos de aprendizagem

Você vai (1) construir uma melhoria de segurança completa para um centro de distribuição; (2) integrar o trabalho anterior; (3) documentar a construção.

### 29.1 O projeto final

O projeto final de Tomás é um pacote de baseline de segurança para o quinto centro de distribuição planejado pela Brightwater, que abre no ano que vem. Ele precisa permitir que Sam configure um novo centro com segurança sem reinventar as decisões. O pacote inclui o projeto de zonas, um modelo de regras de firewall, baselines de configuração dos dispositivos, as definições de papéis, as regras de monitoramento, os runbooks e um checklist de implantação. Ele se apoia em todos os capítulos anteriores. Ruth aprova o escopo porque ele produz algo reutilizável, e não um relatório avulso, e Sam confirma que o quinto centro vai usá-lo. Ele acerta uma data de entrega dois meses antes da abertura do centro.

### 29.2 Construir e testar

Tomás constrói o pacote num ambiente de teste na instituição: um firewall virtual carregado com o modelo de regras, um coletor de teste registrado com a baseline e um conjunto de contas de teste usando os papéis. Ele roda os scripts anteriores contra a configuração de teste: o verificador de regras não encontra nenhuma regra de entrada aberta para qualquer origem, as regras de alerta disparam com os eventos simulados e o script de desligados funciona com as exportações de teste. Uma configuração da baseline quebra o driver da impressora de etiquetas, então ele a ajusta e registra o motivo.

### 29.3 Documentar

Tomás redige o pacote como um guia curto com um checklist logo no início. Cada item se liga ao motivo por trás dele, como um cenário de risco ou um princípio, para que a equipe futura possa julgar se ele ainda se aplica. Ele inclui um log de mudanças e um número de versão. Sam o revisa e pede um acréscimo: como solicitar o acesso do fornecedor para a nova esteira. Uma documentação que explica os motivos é mais fácil de manter, porque as pessoas conseguem atualizá-la com inteligência, em vez de seguir passos que não entendem.

### Exemplo resolvido

Tomás constrói e testa em laboratório um pacote reutilizável de baseline de segurança para centros de distribuição, corrigindo um conflito com a impressora, e o documenta com motivos e controle de versão.

> **Caso sintético.** O pacote e o ambiente de teste são sintéticos.

### Erros e limites

Os testes em laboratório deixam passar peculiaridades de cada local. Os pacotes envelhecem sem um responsável.

### Exercícios

- **EX085 — Por que reutilizável.** Por que Ruth aprovou o escopo do projeto final? *Rubrica:* 3 = ele produz algo reutilizável;; 2 = reutilização;; 1 = tamanho;; 0 = nenhuma.

- **EX086 — Conflito no teste.** Que problema o teste revelou? *Rubrica:* 3 = uma configuração da baseline quebrou o driver da impressora de etiquetas;; 2 = impressora;; 1 = vago;; 0 = nenhuma.

- **EX087 — Motivos ligados.** Por que ligar cada item do checklist a um motivo? *Rubrica:* 3 = para que a equipe futura possa julgar se ele ainda se aplica;; 2 = julgamento;; 1 = vago;; 0 = nenhuma.

### Síntese

Um projeto final que constrói, testa e explica uma linha de base reutilizável deixa valor duradouro para a organização.

<a id="ch-30"></a>

## Capítulo 30 — Avaliação do projeto final

### Objetivos de aprendizagem

Você vai (1) avaliar o projeto final segundo critérios; (2) receber e aplicar o retorno de profissionais; (3) planejar os próximos passos como tecnólogo.

### 30.1 Critérios de avaliação

Ruth e Sam avaliam o projeto final segundo quatro critérios acordados no início: completude, funcionamento testado, clareza para os futuros usuários e alinhamento com os riscos da Brightwater. Cada um recebe nota de zero a três. Tomás tira três em funcionamento testado e alinhamento, dois em completude, porque a configuração do acesso do fornecedor foi acrescentada tarde, e três em clareza. Ele explica cada nota com evidências, como os logs de teste e os comentários de revisão de Sam. Critérios claros permitem que a avaliação se concentre nas evidências, e não em impressões. Ruth e Sam dão as notas de forma independente antes de acertar as notas finais.

### 30.2 Retorno de um profissional

Um profissional convidado revisa o pacote e sugere acrescentar uma seção sobre o que fazer se o centro de distribuição abrir antes que todos os controles estejam prontos, o que acontece com frequência em projetos reais. Tomás acrescenta uma seção curta de risco provisório: quais controles são essenciais antes da abertura, como o login individual e as regras de firewall, e quais podem vir em até um mês. Ele agradece ao profissional e registra a mudança. O retorno de pessoas experientes muitas vezes aponta pressões do mundo real que o trabalho em sala de aula não antecipa. A seção cabe numa única página.

### 30.3 Próximos passos

Tomás reflete sobre o que agora consegue fazer: inventariar sistemas, rastrear fluxos de dados, escrever cenários, aplicar o STRIDE e árvores de ataque, escrever pequenos scripts, montar o monitoramento, implantar e validar mudanças e passar a operação adiante. A Brightwater lhe oferece uma vaga júnior de infraestrutura e segurança. Ele aceita e planeja estudar identidade e segurança em nuvem em seguida. Sua reflexão final é que o valor de um tecnólogo está em fazer os projetos funcionarem com confiabilidade no mundo real, e em dizer com honestidade aos projetistas quando eles não funcionam.

### Exemplo resolvido

O projeto final de Tomás recebe notas em quatro critérios, ele acrescenta uma seção de risco provisório a partir do retorno de um profissional e planeja seus próximos passos.

> **Caso sintético.** As notas e as pessoas são sintéticas.

### Erros e limites

Avaliadores que conhecem o estudante podem dar notas generosas. Planos provisórios podem se tornar permanentes.

### Exercícios

- **EX088 — Nota menor.** Que critério recebeu dois, e por quê? *Rubrica:* 3 = completude, porque a configuração do acesso do fornecedor foi acrescentada tarde;; 2 = completude;; 1 = clareza;; 0 = nenhuma.

- **EX089 — Seção provisória.** O que o profissional sugeriu acrescentar? *Rubrica:* 3 = o que fazer se o centro abrir antes que todos os controles estejam prontos;; 2 = risco provisório;; 1 = vago;; 0 = nenhuma.

- **EX090 — Valor do tecnólogo.** Onde Tomás vê o valor de um tecnólogo? *Rubrica:* 3 = fazer os projetos funcionarem com confiabilidade e relatar com honestidade quando não funcionam;; 2 = mundo real;; 1 = vago;; 0 = nenhuma.

### Síntese

A avaliação do projeto final segundo critérios acordados, somada ao retorno de profissionais, completa a preparação do tecnólogo para a prática.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX090. Tomás Ferreira, Ruth Adeyemi, Sam Okafor, a Kestrel Polytechnic, a Brightwater Logistics e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O processador (hardware), o firmware do fabricante, um sistema operacional móvel, o aplicativo de leitura e os dados das encomendas que ele trata.

**EX002.** Porque, sem responsável, ninguém as mantém atualizadas.

**EX003.** O firmware, que só é atualizado pela ferramenta do fornecedor.

**EX004.** A porta 443, para uma conexão HTTPS criptografada com o serviço de rastreamento.

**EX005.** Porque a área de trabalho remota aberta para a internet é uma rota frequente de entrada de ransomware.

**EX006.** O link de suporte do fornecedor da esteira e a rede sem fio de visitantes, além da conexão com a internet e da regra de área de trabalho remota.

**EX007.** Para confirmar que o script de fato detecta o problema que deveria encontrar.

**EX008.** Duas: área de trabalho remota para office-pc3 e SSH para switch1, ambas abertas para qualquer origem.

**EX009.** Usar consultas parametrizadas em vez de juntar texto com a entrada do usuário.

**EX010.** Juntos, podem revelar quando uma pessoa costuma estar em casa.

**EX011.** Apenas o código postal, o nível de serviço e o peso.

**EX012.** Noventa dias, a menos que haja uma reclamação aberta.

**EX013.** O risco combina a probabilidade de uma ameaça explorar uma fraqueza e o impacto caso isso aconteça.

**EX014.** A fraude de faturas, com criminosos se passando por um fornecedor de combustível.

**EX015.** Relatar a mensagem de phishing, relatar o dispositivo perdido e ligar para confirmar mudanças bancárias.

**EX016.** Porque um malware executado como administrador pode se instalar livremente.

**EX017.** Os contêineres compartilham um único kernel do sistema operacional; as máquinas virtuais rodam sistemas operacionais separados sobre um hypervisor.

**EX018.** Porque a ferramenta de atualização do fornecedor exige uma etapa manual que não tinha responsável.

**EX019.** Porque ninguém consegue saber qual motorista fez uma leitura, e o acesso não pode ser removido para uma única pessoa.

**EX020.** Os supervisores não podem alterar endereços de clientes.

**EX021.** Porque quem muda de função muitas vezes mantém os direitos antigos ao ganhar os novos.

**EX022.** Porque decisões tomadas uma de cada vez tendem a se contradizer.

**EX023.** Novos dispositivos entram numa rede de quarentena até serem aprovados.

**EX024.** Apenas o gateway de suporte do fornecedor.

**EX025.** Para que cada número signifique a mesma coisa mês após mês.

**EX026.** 29 de 60 dispositivos, ou 48 por cento, foram atualizados em até trinta dias.

**EX027.** Para confirmar que o script lê as datas corretamente, já que erros de interpretação distorcem todos os números.

**EX028.** Foram compradas sem requisitos de segurança, então as senhas padrão nunca foram trocadas.

**EX029.** Construir, verificar, implantar e operar.

**EX030.** Porque projetos que ignoram a experiência operacional se afastam da realidade.

**EX031.** O serviço de rastreamento, porque sem ele as encomendas não podem ser roteadas nem rastreadas.

**EX032.** Janelas de manutenção curtas, por causa do horário longo de funcionamento, e o volume triplicado na alta temporada, entre outras.

**EX033.** Disponibilidade e segurança física, já que comandos com defeito poderiam ferir funcionários.

**EX034.** Que os pequenos varejistas enviam planilhas de manifesto por e-mail, que a equipe envia ao sistema à mão.

**EX035.** Autenticação do remetente, criptografia em trânsito e validação do conteúdo.

**EX036.** Enviar um manifesto falso que desvia encomendas.

**EX037.** Uma ameaça, uma fraqueza, um ativo e uma consequência.

**EX038.** Porque, na prática, coletores somem todo mês.

**EX039.** A falha de uma impressora, porque cada centro de distribuição mantém impressoras de reserva.

**EX040.** Um varejista ver os manifestos de outro varejista.

**EX041.** O que conta como pico incomum de alterações de endereço.

**EX042.** A interceptação dos e-mails de redefinição de senha se o e-mail de um varejista estiver comprometido.

**EX043.** Para que a regra reflita os padrões reais do negócio, e não palpites sobre os atacantes.

**EX044.** Cinco encomendas do varejista R2 desviadas para um único endereço novo, 9 Quay Lane.

**EX045.** Porque um número num manifesto forjado poderia pertencer ao criminoso.

**EX046.** O ramo do USB, porque os engenheiros copiam arquivos de configuração usando pendrives pessoais.

**EX047.** Porque o projeto de zonas do capítulo 8 bloqueia os caminhos do escritório para a rede de controle.

**EX048.** Ele acelera a recuperação após falhas comuns de hardware, e não só após ataques.

**EX049.** A varredura de vulnerabilidades dos serviços expostos à internet e os alertas sobre logs.

**EX050.** Permissão por escrito de Sam e do provedor de hospedagem.

**EX051.** Viram shelfware sem uso, que dá falso conforto.

**EX052.** Porque reduz vários cenários, então sua falha enfraquece muitas defesas de uma vez.

**EX053.** Uma regra de call-back para mudanças de dados bancários e o apagamento dos coletores antes da devolução, além de uma cláusula para o fornecedor.

**EX054.** Ela agiliza as respostas aos questionários anuais de segurança de fornecedores dos grandes clientes.

**EX055.** Porque eventos com horários errados são difíceis de correlacionar entre sistemas.

**EX056.** Uma rajada de falhas de login do varejista r-07, uma sessão não aprovada do fornecedor às 02:10 e um backup que falhou.

**EX057.** Testam-nas com um evento simulado para confirmar que ainda funcionam.

**EX058.** Uma atualização do firewall feita na noite anterior.

**EX059.** O serviço de rastreamento havia mudado para um endereço novo que a regra do firewall não permitia.

**EX060.** Porque removeria uma proteção em vez de corrigir a regra específica.

**EX061.** O endereço residencial e o telefone do cliente.

**EX062.** Marcar encomendas como retiradas.

**EX063.** Tentando buscar uma encomenda não relacionada com a chave de teste do parceiro, o que foi recusado.

**EX064.** Ser frequente, baseada em regras e sujeita a erro quando feita à mão.

**EX065.** Porque alguns desligados têm prorrogações aprovadas para a passagem, que exigem julgamento humano.

**EX066.** j.mensah e p.kowal.

**EX067.** Noventa por cento.

**EX068.** Subiu de 48 para 85 por cento.

**EX069.** Porque pode refletir tanto a sorte quanto o efeito dos controles.

**EX070.** Outras mudanças no mesmo período poderiam explicar qualquer diferença.

**EX071.** 9 de 20, ou 45 por cento, antes, e 17 de 21, ou 81 por cento, depois.

**EX072.** O novo processo de apagamento remoto, que fez o relato parecer valer a pena.

**EX073.** Os celulares dos entregadores foram colocados na mesma zona que os sistemas do armazém.

**EX074.** Os dados das receitas visíveis nas telas dos entregadores.

**EX075.** Porque mostrava como os comentários de revisão melhoraram o projeto.

**EX076.** Porque ninguém mais sabe por que eles existem nem como operá-los.

**EX077.** Uma etapa em que faltava a indicação de onde fica a senha.

**EX078.** Por quão pouco a pessoa que sai é necessária depois.

**EX079.** Menos de cinco chamados de ajuda com login por turno.

**EX080.** Um modelo de coletor com firmware mais antigo ainda aceitava o antigo PIN compartilhado.

**EX081.** Mais de dez por cento dos motoristas sem conseguir fazer login no início do turno.

**EX082.** O site de reservas num sábado de manhã.

**EX083.** Uma etapa de desativação foi acrescentada ao procedimento de cancelamento de associação.

**EX084.** A nova etapa havia desativado onze cartões.

**EX085.** Porque produz um pacote reutilizável, e não um relatório avulso.

**EX086.** Uma configuração da baseline quebrou o driver da impressora de etiquetas.

**EX087.** Para que a equipe futura possa julgar se cada item ainda se aplica e atualizá-lo com bom senso.

**EX088.** Completude, porque a configuração do acesso do fornecedor foi acrescentada tarde.

**EX089.** Uma seção sobre a abertura antes que todos os controles estejam prontos, listando primeiro os controles essenciais.

**EX090.** Em fazer os projetos funcionarem com confiabilidade e dizer com honestidade aos projetistas quando eles não funcionam.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- International Organization for Standardization. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
