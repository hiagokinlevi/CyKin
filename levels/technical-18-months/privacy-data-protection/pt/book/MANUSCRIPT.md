# Privacidade e Proteção de Dados: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 050, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–18 de 18 têm texto didático escrito à mão; os exercícios EX001–EX072 têm resoluções correspondentes com rubricas de 0 a 3; os quatro laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de curso técnico que configuram, verificam e documentam os sistemas que guardam dados pessoais numa pequena empresa de saúde.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios encontram dados pessoais em linhas de log sintéticas, conferem que cookies um site sintético grava antes do consentimento, sinalizam visualizações de prontuários fora da clínica do funcionário num log de auditoria sintético e aplicam uma regra de retenção a registros sintéticos de lembretes. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de curso técnico ao longo de dezoito meses centrados num grupo odontológico: serviços, redes, identidades e scripts, escopo e evidências, o modelo de tratamento, telemetria, modos de falha, métodos, configuração, verificação, dois laboratórios controlados, solução de problemas, automação, integração, documentação e um projeto supervisionado. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Leila Haddad** | Estudante de curso técnico | Inventada |
| **Sr. Daniel Okafor** | Instrutor | Inventado |
| **Riverside Technical College** | Escola técnica fictícia | Inventada |
| **Marlow Dental Group** | Grupo odontológico fictício, 8 clínicas, cerca de 45.000 pacientes, agendamento online e lembretes por SMS | Inventado |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR), artigos 4(15), 5, 9(2)(h), 15, 17, 28, 30, 32 e 33; Diretiva 2002/58/CE (ePrivacy), artigo 5(3); Diretrizes 05/2020 do EDPB (consentimento); Lei nº 13.709/2018 (LGPD); Resolução CD/ANPD nº 15/2024; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 27701:2025. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Computação e arquitetura de serviços

### Objetivos de aprendizagem

Você vai (1) descrever os serviços que uma pequena empresa de saúde opera; (2) identificar onde os dados dos pacientes são armazenados e tratados; (3) desenhar um mapa simples de serviços.

### 1.1 O curso e o caso

Leila Haddad começa um curso técnico de dezoito meses no fictício Riverside Technical College. Seu instrutor, o Sr. Daniel Okafor, associa cada tema a um estágio no fictício Marlow Dental Group, que tem oito clínicas, atende cerca de 45.000 pacientes e oferece agendamento online com lembretes por SMS. Os prontuários odontológicos incluem anotações de tratamento, radiografias e históricos médicos, que são dados relativos à saúde pelo artigo 4(15) do GDPR e dados pessoais sensíveis pelo art. 5º, II, da LGPD. O papel de Leila é técnico: configurar, verificar e documentar os sistemas que guardam essas informações, sempre sob supervisão e com dados de teste sintéticos.

### 1.2 Serviços e componentes

Os principais serviços da Marlow são um sistema de gestão clínica em nuvem com os prontuários, um servidor de imagens em cada clínica para as radiografias, um site de agendamento, um gateway de SMS para os lembretes, o e-mail e um serviço de folha de pagamento. Leila aprende a separar um serviço, que é o que os usuários vivenciam, dos componentes que o entregam: servidores, bancos de dados, links de rede e plataformas de fornecedores. O agendamento, por exemplo, depende do site, da interface do sistema de gestão clínica e do gateway de SMS, então um problema de privacidade em qualquer um deles afeta os pacientes que agendam online.

### 1.3 Onde os dados ficam

Para cada serviço, Leila faz três perguntas: que dados de pacientes ele guarda, onde está hospedado, física ou logicamente, e quem consegue alcançá-lo. Ela encontra radiografias em servidores locais em todas as clínicas, cópias de cartas de encaminhamento numa caixa de e-mail compartilhada e listas de consultas exportadas para uma planilha por uma recepcionista. Esses locais importam porque a proteção, a retenção e os pedidos de acesso precisam cobrir todas as cópias, e não só o sistema principal. Um registro que existe em quatro lugares tem quatro chances de ser perdido, guardado demais ou esquecido.

### 1.4 Um primeiro mapa de serviços

Leila desenha um mapa de serviços com caixas para os serviços, cilindros para os repositórios de dados e setas para os fluxos, rotulando cada seta com os dados que carrega. O Sr. Okafor pede que ela marque os fornecedores com outra cor, porque a Marlow não controla diretamente seus sistemas. O mapa mostra que o gateway de SMS recebe nomes, telefones e horários de consulta dos pacientes, o que revela que a pessoa é paciente de uma clínica odontológica. O mapa vira a referência dos capítulos seguintes, e Leila o data para que as mudanças possam ser acompanhadas ao longo do curso.

### Exemplo resolvido

Leila lista os serviços da Marlow, separa serviços de componentes, encontra dados de pacientes em servidores locais de imagens, numa caixa de e-mail compartilhada e numa planilha exportada, e desenha um mapa de serviços datado, com os fornecedores marcados.

> **Caso sintético.** O Riverside, a Marlow e todas as pessoas são sintéticos; o artigo 4(15) do GDPR e o art. 5º, II, da LGPD são reais.

### Erros e limites

Um primeiro mapa deixa escapar as cópias informais; entreviste a equipe além de ler as listas de sistemas.

### Exercícios

- **EX001 — Dados de saúde.** Por que as anotações de tratamento odontológico são dados relativos à saúde? *Rubrica:* 3 = revelam informações sobre o estado de saúde da pessoa;; 2 = menciona saúde;; 1 = vago;; 0 = nenhuma.
- **EX002 — Serviço e componente.** Qual é a diferença entre um serviço e um componente? *Rubrica:* 3 = o serviço é o que os usuários vivenciam; os componentes o entregam;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX003 — As cópias importam.** Por que cada cópia de um registro importa? *Rubrica:* 3 = a proteção, a retenção e os pedidos de acesso precisam cobrir todas as cópias;; 2 = menciona cópias;; 1 = vago;; 0 = nenhuma.
- **EX004 — Conteúdo do SMS.** O que o gateway de SMS fica sabendo sobre os pacientes? *Rubrica:* 3 = nomes, telefones, horários de consulta e que são pacientes odontológicos;; 2 = a maioria;; 1 = um;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 18)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) rastrear os dados dos pacientes pelas redes das clínicas; (2) conferir a criptografia dos protocolos; (3) recomendar a segmentação da rede.

### 2.1 Redes das clínicas

Cada clínica da Marlow tem uma pequena rede que liga os computadores da recepção, as cadeiras odontológicas com câmeras intraorais, o servidor de imagens, uma impressora e um ponto de acesso de Wi-Fi para visitantes. Leila mapeia a rede com o prestador de TI da clínica e descobre que, em três clínicas, o Wi-Fi de visitantes e o servidor de imagens compartilham uma única rede plana. Um paciente na sala de espera poderia, portanto, alcançar os compartilhamentos de arquivos do servidor. Ela explica que separar as redes em zonas é uma medida básica pelo artigo 32, porque limita quem pode sequer tentar acessar os sistemas sensíveis.

### 2.2 Protocolos em uso

Leila lista, com as respectivas portas, os protocolos que carregam dados de pacientes: HTTPS entre os navegadores e o sistema de gestão clínica, DICOM para as radiografias entre as câmeras e o servidor de imagens, compartilhamentos SMB para as cartas digitalizadas e SMTP para o e-mail. Ela aprende que o tráfego DICOM dentro da clínica não é criptografado por padrão, o que é comum em imagens médicas. Registra isso como um risco, e não como uma falha, porque mudar os protocolos de imagem exige apoio e testes do fornecedor, e propõe protegê-lo primeiro com a segmentação da rede.

### 2.3 Conferir a criptografia

Com uma estação de teste e registros sintéticos, Leila confere quais conexões são criptografadas. O site de agendamento e o sistema de gestão clínica usam TLS, e a interface do gateway de SMS também. Mas a impressora da clínica recebe as cartas de encaminhamento em texto claro, e a estação de digitalização salva arquivos num compartilhamento sem criptografia. Ela documenta cada achado com o protocolo, os dados transportados e a mudança recomendada, para que o prestador de TI planeje o trabalho e o Sr. Okafor confira o raciocínio dela antes de qualquer alteração ser feita nos sistemas.

### 2.4 Recomendar a segmentação

Leila propõe três zonas por clínica: uma zona clínica para cadeiras, câmeras e servidor de imagens; uma zona administrativa para a recepção e as impressoras; e uma zona de visitantes, só com acesso à internet. O tráfego entre zonas fica limitado ao que cada fluxo de trabalho precisa, como a recepção ver as imagens pelo sistema de gestão clínica, em vez de navegar diretamente no servidor de imagens. O prestador implementa o desenho primeiro numa clínica. Leila testa a partir do Wi-Fi de visitantes com um notebook e confirma que o servidor de imagens deixou de ser alcançável.

### Exemplo resolvido

Leila mapeia as redes das clínicas, descobre o Wi-Fi de visitantes na mesma rede do servidor de imagens, lista os protocolos, incluindo o DICOM e a impressão sem criptografia, e recomenda três zonas, testadas numa clínica.

> **Caso sintético.** As redes são sintéticas; o artigo 32 do GDPR é real.

### Erros e limites

A segmentação pode quebrar fluxos de trabalho; teste com a equipe da clínica antes de expandir.

### Exercícios

- **EX005 — Risco dos visitantes.** Por que a rede compartilhada com os visitantes era um problema? *Rubrica:* 3 = os pacientes poderiam alcançar o servidor de imagens;; 2 = menciona o servidor;; 1 = vago;; 0 = nenhuma.
- **EX006 — DICOM.** Como Leila tratou o tráfego DICOM sem criptografia? *Rubrica:* 3 = como um risco gerido primeiro pela segmentação;; 2 = menciona segmentação;; 1 = vago;; 0 = nenhuma.
- **EX007 — Três zonas.** Cite as três zonas que Leila propôs. *Rubrica:* 3 = clínica, administrativa e de visitantes;; 2 = todas;; 1 = duas;; 0 = nenhuma.
- **EX008 — Confirmar a mudança.** Como Leila confirmou que a segmentação funcionou? *Rubrica:* 3 = testou a partir do Wi-Fi de visitantes que o servidor ficou inalcançável;; 2 = menciona teste;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 18)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem

Você vai (1) configurar contas nos computadores das clínicas; (2) aplicar o menor privilégio; (3) gerir contas compartilhadas e de quem sai.

### 3.1 Contas nos computadores das clínicas

Os computadores da recepção da Marlow foram configurados anos atrás com um único login compartilhado por clínica. Leila explica aos gerentes das clínicas que as contas compartilhadas tornam impossível saber quem abriu um prontuário, o que prejudica tanto a segurança quanto a responsabilização do artigo 5(2) do GDPR e do art. 6º, X, da LGPD. Com o prestador de TI, ela planeja contas individuais para cada funcionário, ligadas ao diretório central, com bloqueio automático da tela depois de cinco minutos. Ela testa a mudança com pacientes sintéticos numa clínica antes que o prestador a estenda às demais.

### 3.2 Menor privilégio

Leila revisa os perfis do sistema de gestão clínica. As recepcionistas precisam de consultas, contatos e situação de pagamento, mas não das anotações de tratamento. As auxiliares de saúde bucal precisam das anotações dos pacientes que atendem, apenas da própria clínica. Os dentistas precisam do prontuário clínico completo dos seus pacientes. Os gerentes precisam de relatórios. Ela descobre que todas as recepcionistas têm acesso clínico, porque um perfil padrão foi copiado anos antes. Propõe perfis mais estreitos, e o gerente aprova depois que Leila mostra, com registros sintéticos, que as tarefas da recepção continuam funcionando.

### 3.3 Direitos de administrador

Nos computadores das clínicas, as contas da equipe tinham direitos de administrador local para que os funcionários instalassem drivers de impressora. Leila explica que esses direitos deixam o malware se espalhar e permitem instalar software não aprovado que pode enviar dados para outros lugares. Ela retira os direitos na clínica piloto e cria um procedimento curto para que o prestador instale as impressoras, agora remotamente. A mudança reduz as contas de administrador de vinte e três para quatro, e ela registra cada conta restante com seu responsável e sua justificativa, para que a próxima revisão possa conferi-las.

### 3.4 Entradas e saídas

As clínicas odontológicas usam profissionais substitutos por períodos curtos. Leila encontra ativas contas de substitutos que saíram meses antes; o primeiro relatório acha seis contas vencidas. Ela liga a criação e a remoção das contas à escala de trabalho, de modo que cada conta de substituto tem data de término e é desativada automaticamente. Para os funcionários permanentes, a remoção é acionada pelo formulário de desligamento do RH. Ela roda um relatório mensal que compara as contas ativas com a equipe atual, envia as diferenças aos gerentes e guarda os relatórios como evidência de que o controle funciona.

### Exemplo resolvido

Leila substitui os logins compartilhados por contas individuais, tira das recepcionistas o acesso às anotações clínicas, remove os direitos de administrador local e liga as contas dos substitutos às datas de término da escala.

> **Caso sintético.** As contas e os perfis são sintéticos; o artigo 5(2) do GDPR e o art. 6º, X, da LGPD são reais.

### Erros e limites

Perfis estreitos podem bloquear tarefas urgentes; defina um caminho de acesso de emergência registrado.

### Exercícios

- **EX009 — Problema do login compartilhado.** Por que os logins compartilhados são um problema de privacidade? *Rubrica:* 3 = ninguém consegue saber quem abriu um prontuário;; 2 = menciona responsabilização;; 1 = vago;; 0 = nenhuma.
- **EX010 — Acesso da recepção.** De que a recepção precisa no sistema clínico? *Rubrica:* 3 = consultas, contatos, situação de pagamento;; 2 = a maioria;; 1 = anotações;; 0 = nenhuma.
- **EX011 — Contas de administrador.** Quantas contas de administrador restaram? *Rubrica:* 3 = quatro de vinte e três;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX012 — Controle dos substitutos.** Como as contas dos substitutos são controladas agora? *Rubrica:* 3 = datas de término ligadas à escala;; 2 = menciona data de término;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 18)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem

Você vai (1) ler exportações CSV e JSON com segurança; (2) escrever scripts que minimizem a saída; (3) validar os dados antes de tratá-los.

### 4.1 Formatos comuns

Os sistemas da Marlow exportam dados em CSV, para planilhas, e em JSON, para as interfaces entre sistemas. Leila pratica a leitura dos dois com os módulos csv e json da biblioteca padrão do Python, usando prontuários sintéticos. Ela observa que os arquivos CSV abrem facilmente em planilhas e são enviados por e-mail, então se espalham depressa, enquanto as exportações JSON costumam ter mais campos do que alguém examina. Numa exportação JSON sintética, ela encontra um campo de histórico médico aninhado dentro do objeto de consulta, embora o relatório de agendamento só precise de horários e códigos de clínica.

### 4.2 Saída mínima

Leila escreve um script que conta as consultas por clínica e por dia, para o planejamento da capacidade. A primeira versão imprime as linhas completas das consultas durante a depuração. Ela o reescreve para produzir apenas contagens e gravar os detalhes de depuração num arquivo temporário apagado no fim; só contagens agregadas saem do script. O Sr. Okafor explica que as saídas dos scripts costumam acabar em chamados, mensagens de chat e e-mails, então um script que imprime nomes de pacientes pode causar uma divulgação mesmo sem que ninguém tenha a intenção de compartilhar nada.

### 4.3 Validar a entrada

Antes de tratar uma exportação, o script de Leila confere se o arquivo tem as colunas esperadas e rejeita arquivos com colunas inesperadas, como medical_history ou date_of_birth. Também confere se as datas são interpretadas corretamente e se os códigos de clínica ficam entre um e oito. Quando a validação falha, o script para com uma mensagem clara, em vez de tentar adivinhar. Ela explica que a validação aplica a minimização no ponto em que os dados entram numa ferramenta, e que também pega erros de exportação antes que eles produzam relatórios enganosos para os gerentes.

### 4.4 Tratar os arquivos

Os scripts de Leila leem as exportações de uma pasta restrita e nunca as copiam para a área de trabalho ou para drives pessoais. Os arquivos temporários usam o módulo tempfile do Python e são removidos quando o script termina. No topo de cada script, ela acrescenta uma nota explicando que dados ele lê, por quê e o que produz. O Sr. Okafor revisa os scripts e pede que ela retire uma importação não usada de uma biblioteca externa de gráficos, mantendo as ferramentas dependentes só da biblioteca padrão, o que simplifica a revisão e a manutenção.

### Exemplo resolvido

Leila lê exportações CSV e JSON, encontra um campo desnecessário de histórico médico aninhado, escreve um script de capacidade que só conta, valida colunas e valores e trata os arquivos apenas numa pasta restrita.

> **Caso sintético.** As exportações são sintéticas.

### Erros e limites

As regras de validação precisam de atualização quando os sistemas mudam o formato das exportações.

### Exercícios

- **EX013 — Campo aninhado.** Que campo desnecessário Leila encontrou na exportação JSON? *Rubrica:* 3 = histórico médico dentro das consultas;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX014 — Saída do script.** Por que os scripts devem evitar imprimir nomes? *Rubrica:* 3 = as saídas acabam em chamados e chats;; 2 = menciona propagação;; 1 = vago;; 0 = nenhuma.
- **EX015 — Ação da validação.** O que o script faz quando a validação falha? *Rubrica:* 3 = para com uma mensagem clara;; 2 = parcialmente correta;; 1 = adivinha;; 0 = nenhuma.
- **EX016 — Arquivos temporários.** Como os arquivos temporários são tratados? *Rubrica:* 3 = módulo tempfile, removidos no fim;; 2 = menciona remoção;; 1 = mantidos;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 18)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Escopo e evidências de segurança

### Objetivos de aprendizagem

Você vai (1) definir o escopo de uma verificação técnica; (2) obter autorização; (3) coletar e guardar as evidências corretamente.

### 5.1 Definir o escopo

Antes de Leila verificar qualquer sistema da Marlow, o Sr. Okafor exige um escopo por escrito: quais sistemas, quais clínicas, quais datas, que métodos e o que fica de fora. Na primeira verificação, o escopo cobre as configurações de contas e as zonas de rede da clínica piloto, usando prontuários sintéticos numa cópia de teste do sistema de gestão clínica. Os prontuários reais e a infraestrutura em nuvem do fornecedor ficam de fora. Ele explica que um escopo claro protege os pacientes, a Marlow e a própria Leila, porque um trabalho fora do escopo pode causar danos ou violar contratos.

### 5.2 Autorização

O escopo é assinado pelo diretor de operações da Marlow e pelo encarregado. O fornecedor do sistema de gestão clínica é avisado, porque seus termos proíbem testes sem aviso prévio. Leila guarda o escopo assinado com suas anotações e leva uma cópia nas visitas às clínicas. Quando um gerente lhe pede para olhar um prontuário real para explicar um problema, ela recusa e pede que o problema seja reproduzido com dados sintéticos, registrando o pedido e a resposta no seu diário de trabalho. O diário também registra quem aprovou cada etapa, para que o trabalho possa ser reconstituído depois.

### 5.3 Coleta de evidências

Leila registra cada achado com data, hora, sistema, método, o que observou e uma captura de tela ou saída de comando tirada do ambiente de teste. Ela evita capturar dados reais de pacientes nas imagens usando registros sintéticos e recortando as partes irrelevantes. As evidências ficam numa pasta restrita, acessível a ela, ao Sr. Okafor e ao encarregado, com nomes de arquivo num padrão fixo de data, clínica e nome da verificação, para serem achadas depressa. Ela explica que a evidência precisa permitir que outra pessoa repita a verificação e chegue ao mesmo resultado.

### 5.4 Integridade das evidências

Para mostrar que as evidências não foram alteradas, Leila calcula um hash SHA-256 de cada arquivo com o hashlib do Python e registra os hashes num log, que também fica guardado como somente leitura. Quando o encarregado revisa os achados, recalcula dois hashes, e eles conferem. O Sr. Okafor observa que o hash não protege a confidencialidade, só a integridade, e que as evidências que contêm dados pessoais ainda precisam ser protegidas e excluídas quando deixarem de ser necessárias, seguindo as mesmas regras de retenção dos outros registros da Marlow.

### Exemplo resolvido

Leila escreve um escopo assinado que exclui os prontuários reais, avisa o fornecedor, recusa um pedido fora do escopo, registra os achados com método e hora e calcula o hash dos arquivos de evidência.

> **Caso sintético.** O escopo e as evidências são sintéticos.

### Erros e limites

O escopo se alarga aos poucos; confira-o de novo antes de cada nova tarefa.

### Exercícios

- **EX017 — Exclusões do escopo.** O que o primeiro escopo de Leila excluía? *Rubrica:* 3 = prontuários reais e infraestrutura do fornecedor;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX018 — Pedido recusado.** Por que Leila se recusou a ver um prontuário real? *Rubrica:* 3 = fora do escopo; reproduzir com dados sintéticos;; 2 = menciona escopo;; 1 = vago;; 0 = nenhuma.
- **EX019 — Campos da evidência.** O que cada registro de achado inclui? *Rubrica:* 3 = data, hora, sistema, método, observação, captura de tela;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX020 — Finalidade do hash.** O que o hash das evidências comprova? *Rubrica:* 3 = integridade, não confidencialidade;; 2 = parcialmente correta;; 1 = confidencialidade;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 18)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Privacidade e proteção de dados: modelo do sistema

### Objetivos de aprendizagem

Você vai (1) modelar tecnicamente as atividades de tratamento; (2) ligar os sistemas às finalidades e às bases legais; (3) identificar destinatários e transferências.

### 6.1 Finalidades e sistemas

Leila transforma o mapa de serviços num modelo de tratamento. Cada finalidade, como prestar atendimento odontológico, agendar consultas, enviar lembretes, faturar e pagar a equipe, é ligada aos sistemas que a apoiam. O atendimento usa o sistema de gestão clínica e os servidores de imagens. Os lembretes usam o sistema de gestão clínica e o gateway de SMS. A folha de pagamento usa só o serviço externo. Ela observa que o registro das atividades de tratamento do artigo 30 do GDPR, como o registro das operações do art. 37 da LGPD, é organizado por finalidade, então um modelo técnico construído assim pode alimentá-lo diretamente.

### 6.2 Bases legais e condições

Com o encarregado, Leila anota a base legal de cada finalidade. O atendimento se apoia na prestação de cuidados de saúde, com o artigo 9(2)(h) do GDPR como condição para os dados de saúde; na LGPD, a hipótese correspondente é a tutela da saúde do art. 11, II, "f". O faturamento se apoia no contrato e na obrigação legal. Os lembretes se apoiam no legítimo interesse, com uma forma fácil de recusa. O marketing de clareamento exige consentimento. Não cabe a Leila decidir essas bases, mas seu modelo mostra que sistemas tratam dados para cada uma, para que uma mudança num lugar não altere outro em silêncio.

### 6.3 Destinatários

O modelo lista os destinatários: o fornecedor do sistema de gestão clínica e o gateway de SMS, como operadores; o laboratório de prótese, que recebe moldagens e prescrições; as clínicas especializadas de encaminhamento; e o provedor da folha de pagamento. Cada operador precisa de contrato pelo artigo 28. Leila confere que os contratos existem e não encontra nenhum com uma pequena empresa de motoboys que leva as prescrições impressas, com nomes de pacientes, ao laboratório. Ela leva o caso ao diretor de operações, observando que os fluxos em papel fazem parte do modelo do sistema, mesmo sem nenhum software envolvido.

### 6.4 Transferências

Leila pergunta a cada fornecedor onde os dados ficam armazenados. O sistema de gestão clínica hospeda os dados na UE. O gateway de SMS encaminha as mensagens por um provedor cuja equipe de suporte fica num país fora da UE. Ela registra isso como uma possível transferência que exige salvaguardas pelo capítulo V do GDPR, como exigiriam os arts. 33 a 36 da LGPD, e a passa ao encarregado, com a localização do suporte do fornecedor anotada. O Sr. Okafor lembra que a equipe técnica costuma descobrir as transferências primeiro, porque enxerga os destinos de rede e os arranjos de suporte.

### Exemplo resolvido

Leila liga as finalidades aos sistemas, registra as bases legais com o encarregado, lista os destinatários, encontra um serviço de entregas sem contrato e sinaliza uma transferência para o suporte do SMS fora da UE.

> **Caso sintético.** O modelo é sintético; os artigos 9(2)(h), 28 e 30 e o capítulo V do GDPR e os arts. 11, 33 a 36 e 37 da LGPD são reais.

### Erros e limites

As bases legais são decididas pelo controlador, com aconselhamento; a equipe técnica as documenta.

### Exercícios

- **EX021 — Estrutura do modelo.** Como o modelo de tratamento de Leila é organizado? *Rubrica:* 3 = por finalidade, como o registro do artigo 30;; 2 = menciona finalidade;; 1 = só sistemas;; 0 = nenhuma.
- **EX022 — Condição do atendimento.** Que condição do artigo 9 apoia o atendimento? *Rubrica:* 3 = artigo 9(2)(h);; 2 = parcialmente correta;; 1 = consentimento;; 0 = nenhuma.
- **EX023 — Lacuna das entregas.** Que lacuna Leila encontrou no serviço de entregas? *Rubrica:* 3 = nenhum contrato de operador;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX024 — Possível transferência.** Que possível transferência Leila sinalizou? *Rubrica:* 3 = o suporte do provedor de SMS fora da UE;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 18)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Privacidade e proteção de dados: dados e telemetria

### Objetivos de aprendizagem

Você vai (1) encontrar dados pessoais em logs e telemetria; (2) mascará-los com segurança; (3) definir a retenção dos logs.

### 7.1 Telemetria por toda parte

Os sistemas da Marlow produzem logs, relatórios de erro e estatísticas de uso. O servidor de agendamento registra cada requisição, o gateway de SMS registra os resultados de entrega e o site envia dados de desempenho a um serviço de monitoramento. Leila aprende que a telemetria costuma ser desenhada pelos desenvolvedores para depuração, com pouca atenção à privacidade. Os logs são copiados para ferramentas de monitoramento, compartilhados com fornecedores em chamados de suporte e guardados por mais tempo do que os dados que descrevem. Uma linha de log com um e-mail pode, portanto, viajar mais longe do que o próprio registro de agendamento.

### 7.2 O laboratório dos logs

Leila analisa uma amostra sintética dos logs do servidor de agendamento. O laboratório mostra que 95 de 400 linhas, 23,8%, contêm dados pessoais: 75 trazem e-mails de pacientes e 20 trazem telefones de mensagens que falharam. Cada uma dessas linhas liga uma pessoa a uma consulta odontológica. Depois de uma etapa de mascaramento que troca os e-mails por um marcador e oculta os dígitos dos telefones, nenhuma linha com dados pessoais permanece. O número da reserva continua permitindo que a equipe de suporte rastreie um problema pelo sistema de gestão clínica, quando autorizada a fazê-lo.

### 7.3 Corrigir na origem

Mascarar depois é útil, mas Leila argumenta que a correção melhor é deixar de registrar dados pessoais nos logs. Ela pede ao desenvolvedor que registre os números das reservas em vez dos e-mails e apenas os três últimos dígitos dos telefones nas mensagens que falharam. O desenvolvedor concorda e muda as chamadas de log na versão seguinte. Leila repete a análise com tráfego sintético da nova versão e confirma que nenhuma linha nova contém e-mails ou telefones completos. Ela registra a mudança e o resultado do novo teste, para que a correção possa ser conferida de novo em cada versão futura.

### 7.4 Retenção dos logs

Por padrão, os logs ficam noventa dias no serviço de monitoramento, e os logs antigos do servidor de agendamento nunca tinham sido apagados. Leila propõe trinta dias para os logs detalhados, o que cobre a maior parte da solução de problemas, e doze meses para as estatísticas agregadas sem dados pessoais. Ela documenta a decisão com o encarregado, ligando-a à limitação da conservação do artigo 5(1)(e) do GDPR. O prestador de TI configura a exclusão automática, e Leila acrescenta uma verificação trimestral de que o arquivo de log mais antigo está dentro do limite. A primeira verificação passa.

### Laboratório — Dados pessoais nos logs do servidor de agendamento

```python
"""Find and mask personal data in synthetic booking-server log lines (stdlib only)."""
import random, re
random.seed(7)
names = ["ana", "ben", "chloe", "dev", "erin", "farid", "gita", "hugo"]
lines = []
for i in range(400):
    kind = random.random()
    if kind < 0.15:
        lines.append(f"INFO booking created for {random.choice(names)}@example.org slot={i}")
    elif kind < 0.22:
        lines.append(f"WARN sms failed to +44 7700 900{random.randint(100,999)} ref={i}")
    else:
        lines.append(f"INFO booking created ref=B{i:05d} clinic={random.randint(1,8)}")
EMAIL = re.compile(r"[\w.]+@[\w.]+"); PHONE = re.compile(r"\+44 \d{4} \d{6}")
hit = [l for l in lines if EMAIL.search(l) or PHONE.search(l)]
masked = [PHONE.sub("+44 **** ******", EMAIL.sub("<email>", l)) for l in lines]
left = sum(1 for l in masked if EMAIL.search(l) or PHONE.search(l))
print(f"log lines {len(lines)}; with personal data {len(hit)} ({100*len(hit)/len(lines):.1f}%)")
print(f"emails {sum(1 for l in lines if EMAIL.search(l))}; phones {sum(1 for l in lines if PHONE.search(l))}; after masking {left}")
```

Execute com `python3 lab_logs.py`. Saída verificada:

```text
log lines 400; with personal data 95 (23.8%)
emails 75; phones 20; after masking 0
```

### Exemplo resolvido

Leila encontra dados pessoais em 95 de 400 linhas sintéticas de log (23,8%), mascara-os até zero, faz o desenvolvedor deixar de registrar e-mails e telefones completos e define a retenção de trinta dias para os logs.

> **Caso sintético.** Os logs são sintéticos; o artigo 5(1)(e) do GDPR é real.

### Erros e limites

As expressões regulares deixam passar formatos incomuns; revise amostras à mão também.

### Exercícios

- **EX025 — Parcela dos logs.** Que parcela das linhas de log tinha dados pessoais? *Rubrica:* 3 = 95 de 400, 23,8%;; 2 = aproximada;; 1 = errada;; 0 = nenhuma.
- **EX026 — Correção na origem.** O que o desenvolvedor mudou? *Rubrica:* 3 = registrar números de reserva e dígitos parciais do telefone;; 2 = menciona números de reserva;; 1 = vago;; 0 = nenhuma.
- **EX027 — Por que os logs viajam.** Por que os logs se espalham mais que os registros? *Rubrica:* 3 = são copiados para o monitoramento e compartilhados em chamados de suporte;; 2 = menciona cópias;; 1 = vago;; 0 = nenhuma.
- **EX028 — Retenção dos logs.** Que retenção Leila propôs para os logs detalhados? *Rubrica:* 3 = trinta dias;; 2 = parcialmente correta;; 1 = noventa;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 18)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Privacidade e proteção de dados: modos de falha

### Objetivos de aprendizagem

Você vai (1) identificar como os controles de privacidade falham; (2) classificar as falhas; (3) desenhar a detecção de cada uma.

### 8.1 Como os controles falham

Leila lista as formas como os controles de privacidade podem falhar na Marlow: um lembrete por SMS enviado a um número antigo, agora de outra pessoa; uma carta de encaminhamento enviada por e-mail à clínica errada; uma radiografia exportada para um pendrive e perdida; a conta de um ex-substituto ainda ativa; e uma rotina automática de exclusão que para de rodar. Ela observa que a maioria das falhas não são ataques, mas erros comuns ou panes silenciosas, e que cada uma pode expor informações de saúde de um paciente a alguém que não deveria vê-las.

### 8.2 Classificar as falhas

Leila classifica as falhas em quatro tipos. As de destinatário errado enviam dados à pessoa errada. As de retenção excessiva guardam dados por tempo demais. As de acesso excessivo deixam as pessoas verem mais do que precisam. As falhas silenciosas acontecem quando uma rotina ou configuração de proteção para de funcionar sem que ninguém perceba. A classificação orienta os controles: destinatário errado pede conferência antes do envio; retenção excessiva, rotinas de exclusão; acesso excessivo, desenho de perfis; e falhas silenciosas, um monitoramento que alguém de fato leia. Nos incidentes passados da Marlow, o destinatário errado é o tipo mais comum.

### 8.3 Desenho da detecção

Para cada tipo de falha, Leila desenha uma forma de percebê-la. Os e-mails ao destinatário errado são detectados pelas comunicações da equipe e por um aviso automático para endereços externos. A retenção excessiva é detectada por uma consulta mensal dos registros mais antigos. O acesso excessivo é detectado pela revisão dos logs de auditoria em busca de visualizações fora da clínica do funcionário. As falhas silenciosas são detectadas por rotinas que informam o sucesso todo dia, de modo que a falta de um relatório dispara um alerta. Ela observa que um controle sem detecção pode falhar por meses antes de alguém notar.

### 8.4 O caso do lembrete

Leila estuda em detalhe o caso do número antigo. Um paciente trocou de número sem avisar a clínica, e o novo dono do número recebeu lembretes com o nome do paciente e da clínica. Leila recomenda que os lembretes tragam só o nome da clínica e o horário, sem o nome completo do paciente nem o tipo de tratamento, e que a recepção confirme o telefone em cada visita. O encarregado trata o evento original como uma violação de dados pessoais e o registra, mesmo com o risco avaliado como baixo, porque o artigo 33(5) do GDPR exige documentar todas as violações.

### Exemplo resolvido

Leila lista as falhas, classifica-as em destinatário errado, retenção excessiva, acesso excessivo e falha silenciosa, desenha a detecção de cada uma e reduz o conteúdo dos lembretes depois de um caso de número errado.

> **Caso sintético.** As falhas são sintéticas; o registro de violações do artigo 33 do GDPR é real.

### Erros e limites

A detecção depende de pessoas agirem diante dos alertas; atribua responsáveis.

### Exercícios

- **EX029 — Quatro tipos.** Cite os quatro tipos de falha. *Rubrica:* 3 = destinatário errado, retenção excessiva, acesso excessivo, falha silenciosa;; 2 = todos;; 1 = dois;; 0 = nenhuma.
- **EX030 — Detectar o silêncio.** Como as falhas silenciosas são detectadas? *Rubrica:* 3 = rotinas informam o sucesso todo dia; a falta do relatório gera alerta;; 2 = menciona diário;; 1 = vago;; 0 = nenhuma.
- **EX031 — Conteúdo do lembrete.** O que os lembretes devem conter agora? *Rubrica:* 3 = só o nome da clínica e o horário;; 2 = parcialmente correta;; 1 = todos os detalhes;; 0 = nenhuma.
- **EX032 — Registro da violação.** Por que o caso do número errado foi registrado? *Rubrica:* 3 = era uma violação de dados pessoais, mesmo de baixo risco;; 2 = menciona violação;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 18)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Privacidade e proteção de dados: ferramentas e métodos

### Objetivos de aprendizagem

Você vai (1) escolher ferramentas para as verificações de privacidade; (2) usar scripts da biblioteca padrão com responsabilidade; (3) documentar os métodos para que possam ser repetidos.

### 9.1 Escolher as ferramentas

Leila precisa de ferramentas para buscar em exportações, analisar logs, conferir cookies e revisar trilhas de auditoria. O Sr. Okafor define uma regra para o curso: usar os recursos nativos dos sistemas e a biblioteca padrão do Python antes de acrescentar software novo, porque cada ferramenta nova exige aprovação, atualizações e a verificação dos dados que ela envia para fora. Alguns varredores comerciais enviam os arquivos à nuvem do fornecedor para análise, o que já seria uma divulgação de dados de pacientes. Leila acrescenta uma pergunta à sua lista de ferramentas: para onde esta ferramenta envia os dados que lê?

### 9.2 Métodos antes das ferramentas

Leila escreve um método para cada verificação antes de escolher a ferramenta: a pergunta, a fonte dos dados, os passos, a saída esperada e como interpretá-la. O método para conferir a retenção dos logs, por exemplo, pergunta: qual é o arquivo de log mais antigo em cada local, e ele está dentro dos trinta dias? A ferramenta, então, é um script curto ou um comando do sistema que responde a essa pergunta. Ela aprende que um método claro facilita explicar os resultados e trocar de ferramenta depois sem mudar a conclusão, porque a pergunta continua a mesma.

### 9.3 Repetibilidade

Cada método é guardado com seu script, os dados sintéticos de teste e os resultados esperados, sob controle de versão. Outro estudante pode executar o mesmo método e comparar as saídas. Leila usa sementes aleatórias fixas nos geradores de dados sintéticos, para que os resultados sejam idênticos entre execuções. Quando um resultado muda inesperadamente, a saída esperada guardada mostra na hora que algo mudou no sistema ou no script. O Sr. Okafor explica que verificações repetíveis transformam os controles de privacidade em algo que pode ser testado como qualquer outro requisito técnico.

### 9.4 Uso responsável

As ferramentas que leem dados pessoais também são tratamento. Os scripts de Leila rodam só no computador de análise restrito, leem apenas as exportações citadas no escopo e produzem contagens ou saídas mascaradas. Ela registra cada execução num log com a data, o método, o nome do arquivo de entrada e o resumo do resultado. Ao terminar uma verificação, apaga as cópias de trabalho das exportações. Ela explica que as ferramentas de privacidade devem seguir os mesmos padrões dos sistemas que examinam, senão viram uma nova fonte de risco para os próprios pacientes que deveriam proteger.

### Exemplo resolvido

Leila prefere os recursos nativos e a biblioteca padrão, pergunta para onde cada ferramenta envia os dados, escreve os métodos antes de escolher as ferramentas, guarda as saídas esperadas com sementes fixas e registra cada execução.

> **Caso sintético.** As ferramentas e os métodos são sintéticos.

### Erros e limites

As ferramentas nativas têm limites; documente o que um método não consegue detectar.

### Exercícios

- **EX033 — Pergunta sobre as ferramentas.** Que pergunta Leila acrescentou à sua lista de ferramentas? *Rubrica:* 3 = para onde a ferramenta envia os dados que lê;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX034 — Partes do método.** O que cada método define? *Rubrica:* 3 = pergunta, fonte, passos, saída esperada, interpretação;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX035 — Sementes fixas.** Por que usar sementes aleatórias fixas? *Rubrica:* 3 = dados sintéticos idênticos entre execuções;; 2 = menciona repetibilidade;; 1 = vago;; 0 = nenhuma.
- **EX036 — Ferramentas como tratamento.** Por que as próprias ferramentas de privacidade são um risco? *Rubrica:* 3 = também tratam dados pessoais;; 2 = menciona tratamento;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — aula 09 (capítulo 09 de 18)

[← Capítulo 08](#ch-08) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Privacidade e proteção de dados: configuração de controles

### Objetivos de aprendizagem

Você vai (1) conferir o comportamento dos cookies num site; (2) configurar o consentimento corretamente; (3) verificar as mudanças de configuração.

### 10.1 Cookies e consentimento

O site de agendamento da Marlow grava cookies e tecnologias semelhantes. O artigo 5(3) da Diretiva ePrivacy exige consentimento antes de armazenar ou ler informações no aparelho do usuário, salvo quando isso é estritamente necessário para um serviço que ele pediu. As Diretrizes 05/2020 do EDPB explicam que o consentimento deve ser livre, específico, informado e inequívoco. A tarefa de Leila é técnica: conferir que cookies o site de fato grava, quando, e se o banner os controla como o aviso diz. Cookies que só lembram as configurações escolhidas pelo visitante podem ser isentos, mas apenas depois que ele fez a escolha.

### 10.2 O laboratório dos cookies

Leila abre o site num perfil de navegador limpo, registra os cookies antes de interagir com o banner e repete depois de aceitar. O laboratório resume seus resultados sintéticos: sete cookies, dos quais três são gravados antes do consentimento sem isenção. O cookie de análise de uso e um pixel de publicidade carregam imediatamente. Um cookie de idioma também é gravado automaticamente antes de o visitante escolher um idioma, então não é claramente necessário para um serviço pedido. Os cookies de sessão e de token de segurança são estritamente necessários e carregam imediatamente, de forma correta.

### 10.3 Corrigir a configuração

O site usa um gerenciador de tags para carregar os scripts. Leila trabalha com o desenvolvedor web para que as tags de análise e de publicidade só disparem depois que o consentimento for registrado, e para que o cookie de idioma só seja gravado quando o visitante escolher um idioma. O banner muda para que recusar seja tão fácil quanto aceitar, com botões do mesmo tamanho na primeira camada. O pixel de publicidade é removido por completo, porque a Marlow não faz campanhas que precisem dele e ninguém soube explicar por que tinha sido instalado.

### 10.4 Verificar a mudança

Leila repete o teste num perfil limpo depois da mudança. Antes do consentimento, só aparecem os cookies de sessão e de segurança. Depois de recusar, nenhum cookie de análise aparece, mesmo navegando por várias páginas. Depois de aceitar, a análise carrega como esperado. Ela registra os resultados com datas, versões do navegador e capturas de tela de cada lista de cookies. Também acrescenta o teste à lista de verificação de cada versão do site, porque mudanças e plugins novos costumam trazer de volta tags que carregam antes do consentimento, e um teste rápido pega isso antes que os pacientes sejam afetados.

### Laboratório — Cookies gravados antes do consentimento

```python
"""Check which cookies a synthetic booking site sets before consent (stdlib only)."""
cookies = [
    ("session_id", "strictly necessary", "before"),
    ("csrf_token", "strictly necessary", "before"),
    ("lang", "functional", "before"),
    ("_ga", "analytics", "before"),
    ("_fbp", "advertising", "before"),
    ("chat_widget", "functional", "after"),
    ("ab_test", "analytics", "after"),
]
bad = [c for c in cookies if c[2] == "before" and c[1] not in ("strictly necessary",)]
for n, cat, when in cookies:
    flag = "PROBLEM" if (n, cat, when) in bad else "ok"
    print(f"{n:12s} {cat:19s} set {when:6s} consent  {flag}")
print(f"cookies set before consent without exemption: {len(bad)} of {len(cookies)}")
```

Execute com `python3 lab_cookies.py`. Saída verificada:

```text
session_id   strictly necessary  set before consent  ok
csrf_token   strictly necessary  set before consent  ok
lang         functional          set before consent  PROBLEM
_ga          analytics           set before consent  PROBLEM
_fbp         advertising         set before consent  PROBLEM
chat_widget  functional          set after  consent  ok
ab_test      analytics           set after  consent  ok
cookies set before consent without exemption: 3 of 7
```

### Exemplo resolvido

Leila encontra três de sete cookies gravados antes do consentimento sem isenção, faz as tags dispararem só depois do consentimento, remove um pixel de publicidade sem uso, iguala os botões do banner e verifica num perfil limpo.

> **Caso sintético.** O site é sintético; o artigo 5(3) da Diretiva 2002/58/CE e as Diretrizes 05/2020 do EDPB são reais.

### Erros e limites

O nome do cookie não prova a finalidade; confira o que cada script de fato faz.

### Exercícios

- **EX037 — Antes do consentimento.** Quantos cookies eram gravados antes do consentimento sem isenção? *Rubrica:* 3 = 3 de 7;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX038 — Cookie de idioma.** Por que o cookie de idioma era um problema? *Rubrica:* 3 = era gravado antes de o visitante escolher um idioma;; 2 = menciona escolha;; 1 = vago;; 0 = nenhuma.
- **EX039 — Decisão sobre o pixel.** O que aconteceu com o pixel de publicidade? *Rubrica:* 3 = foi removido; ninguém precisava dele;; 2 = menciona remoção;; 1 = adiado;; 0 = nenhuma.
- **EX040 — Verificação a cada versão.** Por que acrescentar o teste de cookies à lista de cada versão? *Rubrica:* 3 = as mudanças costumam reintroduzir tags precoces;; 2 = menciona regressões;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — aula 10 (capítulo 10 de 18)

[← Capítulo 09](#ch-09) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Privacidade e proteção de dados: verificação

### Objetivos de aprendizagem

Você vai (1) verificar se os controles de privacidade funcionam como desenhados; (2) usar amostragem; (3) relatar a verificação com honestidade.

### 11.1 O que significa verificar

Leila distingue três perguntas: o controle foi desenhado corretamente, foi implementado como desenhado e opera de forma consistente ao longo do tempo? Um desenho de perfis pode estar certo no papel, ser implementado com um erro e depois ser alterado por um administrador. A verificação precisa de evidências para cada pergunta, e a operação é a mais difícil de comprovar. O Sr. Okafor dá um exemplo do trabalho dela: o desenho da segmentação estava correto e a implementação na clínica piloto foi testada, mas ninguém conferiu ainda se as outras clínicas foram configuradas do mesmo jeito.

### 11.2 Amostragem de contas

Leila verifica os perfis de acesso por amostragem. Ela sorteia vinte contas da equipe nas oito clínicas e compara o perfil de cada uma com o cargo e o vínculo atual da pessoa. Dezoito conferem. Uma recepcionista ainda tem acesso clínico de um perfil antigo, e uma auxiliar transferida para outra clínica ainda acessa os pacientes da clínica anterior. Ela relata os dois casos e pede aos gerentes que os corrijam. Também anota que uma amostra estima a taxa de erro, mas não consegue provar que todas as outras contas estão corretas, o que precisa ficar claro no relatório.

### 11.3 Testar a operação

Para a rotina que exclui os registros antigos de lembretes, Leila confere o log de sucesso dos últimos três meses e encontra dois dias faltando. Ela pergunta ao prestador de TI, que explica que o servidor foi reiniciado para atualizações naqueles dias e a rotina não rodou. A execução do dia seguinte compensou, então nenhum dado ficou guardado por tempo demais. Leila registra isso como uma pequena lacuna operacional e recomenda que a rotina informe o horário em que rodou, para que um dia perdido fique visível na hora, e não meses depois numa revisão.

### 11.4 Relatar com honestidade

O relatório de verificação de Leila lista cada controle, a evidência, o resultado e os limites, começando pelas lacunas. Ela marca os controles como verificados, parcialmente verificados ou ainda não verificados, e evita descrever uma amostra como verificação completa. Sobre a segmentação da rede, escreve: verificada em uma clínica, ainda não verificada nas outras sete. O encarregado gosta da clareza, porque ela mostra exatamente onde falta trabalho. O Sr. Okafor observa que relatórios de verificação inflados criam uma falsa confiança, o que é pior do que uma lacuna declarada com honestidade.

### Exemplo resolvido

Leila separa desenho, implementação e operação, verifica vinte contas por amostragem e encontra dois erros, confere o histórico da rotina de exclusão e relata os controles como verificados, parcialmente verificados e ainda não verificados.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

As amostras estimam taxas; não certificam cada conta.

### Exercícios

- **EX041 — Três perguntas.** Que três perguntas a verificação responde? *Rubrica:* 3 = desenhado corretamente, implementado como desenhado, operando ao longo do tempo;; 2 = todas;; 1 = uma;; 0 = nenhuma.
- **EX042 — Resultado da amostra.** Quantas contas da amostra conferiram? *Rubrica:* 3 = 18 de 20;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX043 — Execuções perdidas.** Por que a rotina de exclusão perdeu dois dias? *Rubrica:* 3 = reinicializações do servidor para atualizações;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX044 — Situação da segmentação.** Como Leila relatou a segmentação da rede? *Rubrica:* 3 = verificada em uma clínica, ainda não nas outras sete;; 2 = parcialmente correta;; 1 = verificada;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — aula 11 (capítulo 11 de 18)

[← Capítulo 10](#ch-10) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Laboratório controlado I

### Objetivos de aprendizagem

Você vai (1) conduzir uma análise controlada de log de auditoria; (2) interpretar acessos incomuns; (3) tratar os achados com justiça.

### 12.1 O laboratório controlado

O primeiro laboratório controlado de Leila usa uma cópia sintética do log de auditoria do sistema de gestão clínica, preparada com as ferramentas de teste do fornecedor e aprovada dentro do seu escopo. O log registra que conta da equipe viu qual prontuário e em que clínica. Nenhum paciente ou funcionário real aparece. O Sr. Okafor define as regras: o laboratório roda num computador isolado, os resultados nunca saem dele e só são compartilhados com o encarregado e o instrutor, e qualquer nome nas conclusões se refere apenas a contas sintéticas.

### 12.2 Resultados do laboratório

O laboratório analisa 5.060 visualizações de prontuários e encontra 179, 3,5%, de pacientes registrados numa clínica diferente da do funcionário. A maioria tem poucas visualizações assim, o que é esperado, porque os pacientes às vezes vão a outra clínica. Uma conta sintética, S07, tem 53 visualizações externas espalhadas por várias clínicas, muito mais que qualquer outra; as seguintes são S13, com 9, e S27, com 7. O padrão é incomum o bastante para justificar um olhar mais atento, mas não prova uso indevido. É o contexto que decide o que vem depois.

### 12.3 Interpretar o padrão

Leila lista explicações possíveis para S07: um cargo que cobre várias clínicas, como uma auxiliar regional ou um gerente, uma designação temporária, uma conta compartilhada ou curiosidade sem motivo sobre os pacientes. Ela confere a lista sintética da equipe e descobre que S07 é recepcionista de uma única clínica. Mesmo assim, não conclui que houve irregularidade. Em vez disso, prepara um resumo factual para o encarregado, que num caso real seguiria o procedimento de investigação da Marlow, incluindo conversar com a pessoa e com o gerente dela antes de qualquer decisão.

### 12.4 Justiça e limites

O Sr. Okafor ressalta que a análise de logs de auditoria afeta os funcionários, que também têm direito à privacidade e a um tratamento justo. A equipe precisa ser informada, no aviso de privacidade dos funcionários, de que os acessos são registrados e revisados. Os limites devem ser aplicados de forma consistente, e os achados devem ser conferidos antes de qualquer ação. Leila anota os limites do laboratório: o log sintético não tem informações sobre tarefas legítimas entre clínicas, então uma revisão real combinaria o log com a escala e os cargos antes de tirar conclusões, protegendo a equipe de suspeitas injustas.

### Laboratório — Visualizações de prontuários fora da clínica do funcionário

```python
"""Flag record views outside a staff member's own clinic in a synthetic audit log (stdlib only)."""
import random, collections
random.seed(5)
staff = {f"S{i:02d}": random.randint(1, 8) for i in range(40)}
log = []
for _ in range(5000):
    s = random.choice(list(staff)); home = staff[s]
    clinic = home if random.random() < 0.97 else random.randint(1, 8)
    log.append((s, clinic))
log += [("S07", c) for c in (2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6) * 5]
out = [(s, c) for s, c in log if c != staff[s]]
per = collections.Counter(s for s, _ in out)
print(f"record views {len(log)}; outside own clinic {len(out)} ({100*len(out)/len(log):.1f}%)")
top = per.most_common(3)
print("top staff by outside views:", ", ".join(f"{s} {n}" for s, n in top))
```

Execute com `python3 lab_access.py`. Saída verificada:

```text
record views 5060; outside own clinic 179 (3.5%)
top staff by outside views: S07 53, S13 9, S27 7
```

### Exemplo resolvido

Leila encontra 179 de 5.060 visualizações (3,5%) fora da clínica dos funcionários, identifica S07 com 53 visualizações externas, lista explicações e prepara um resumo factual sem concluir que houve uso indevido.

> **Caso sintético.** O log de auditoria é sintético.

### Erros e limites

Um acesso incomum é um sinal, não uma prova; siga um procedimento justo.

### Exercícios

- **EX045 — Visualizações externas.** Que parcela das visualizações foi fora da clínica do funcionário? *Rubrica:* 3 = 179 de 5.060, 3,5%;; 2 = aproximada;; 1 = errada;; 0 = nenhuma.
- **EX046 — Ponto fora da curva.** Que conta se destacou e com quantas visualizações externas? *Rubrica:* 3 = S07, com 53;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX047 — Explicações.** Cite duas explicações possíveis para o padrão de S07. *Rubrica:* 3 = cargo regional, designação temporária, conta compartilhada, curiosidade;; 2 = duas;; 1 = uma;; 0 = nenhuma.
- **EX048 — Direitos da equipe.** O que a equipe precisa saber sobre os logs de auditoria? *Rubrica:* 3 = os acessos são registrados e revisados;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — aula 12 (capítulo 12 de 18)

[← Capítulo 11](#ch-11) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Privacidade e proteção de dados: solução de problemas

### Objetivos de aprendizagem

Você vai (1) diagnosticar uma falha de privacidade com método; (2) encontrar a causa raiz; (3) evitar a recorrência.

### 13.1 O sintoma

Uma paciente reclama que recebeu por e-mail uma oferta de clareamento, embora nunca tenha aceitado receber marketing. O encarregado pede a Leila que investigue tecnicamente. Ela começa anotando exatamente o que se sabe: o equivalente sintético da paciente para teste, a data do e-mail, o nome da campanha e a configuração atual de marketing da paciente, que está desligada. Ela resiste a adivinhar as causas antes de reunir os fatos, porque os palpites iniciais tendem a concentrar a atenção no sistema errado e a desperdiçar tempo. Primeiro os fatos, depois as teorias.

### 13.2 Seguir os dados

Leila rastreia como a lista da campanha foi montada. A plataforma de marketing recebe toda noite uma exportação do sistema de gestão clínica com os pacientes que consentiram em receber marketing. Ela compara a exportação da data da campanha com a tabela de consentimentos e descobre que a consulta de exportação usou o campo dos lembretes de consulta, e não o do consentimento para marketing. Todos os pacientes que aceitaram lembretes, cerca de quatro vezes mais pessoas do que as que aceitaram marketing, entraram na lista da campanha naquela noite. A lista afetada é reconstruída para identificar todos os pacientes atingidos.

### 13.3 Causa raiz

A consulta tinha sido editada duas semanas antes, quando o fornecedor do sistema de gestão clínica renomeou vários campos numa atualização que não foi documentada. Quem atualizou a consulta escolheu o campo errado, porque os dois tinham nomes parecidos: contact_ok e marketing_ok. Não havia nenhum teste que conferisse se a exportação continha só pacientes que consentiram. Leila identifica três causas: nomes de campos confusos, nenhuma revisão da mudança na consulta e nenhuma verificação automática. Ela observa que culpar a pessoa deixaria as três causas no lugar, prontas para gerar o próximo erro parecido.

### 13.4 Evitar a recorrência

Leila acrescenta uma verificação automática que compara cada exportação com a tabela de consentimentos antes do envio e interrompe a exportação se algum paciente não tiver consentido; a verificação vale também para as listas de SMS. As mudanças nas consultas passam a exigir revisão por uma segunda pessoa, e o fornecedor é solicitado a documentar com clareza o significado dos campos. A Marlow suprime o marketing para todos os pacientes afetados, envia um pedido de desculpas e registra o evento, cabendo ao encarregado decidir se a notificação é exigida pelo artigo 33 do GDPR, em até 72 horas, ou pela Resolução CD/ANPD nº 15/2024, em três dias úteis.

### Exemplo resolvido

Leila liga um e-mail de marketing indesejado a uma consulta de exportação que usou o campo dos lembretes depois que o fornecedor renomeou os campos, e acrescenta uma verificação automática do consentimento e a revisão por uma segunda pessoa.

> **Caso sintético.** A falha é sintética; o artigo 33 do GDPR e a Resolução CD/ANPD nº 15/2024 são reais.

### Erros e limites

Uma correção rápida só na consulta não impediria o próximo erro parecido.

### Exercícios

- **EX049 — Primeiro passo.** O que Leila fez antes de adivinhar as causas? *Rubrica:* 3 = anotou os fatos conhecidos;; 2 = menciona fatos;; 1 = adivinhou;; 0 = nenhuma.
- **EX050 — Campo errado.** Que campo a exportação usou por engano? *Rubrica:* 3 = o campo dos lembretes, contact_ok;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX051 — Três causas.** Cite as três causas que Leila encontrou. *Rubrica:* 3 = nomes confusos, nenhuma revisão, nenhuma verificação automática;; 2 = todas;; 1 = uma;; 0 = nenhuma.
- **EX052 — Verificação automática.** O que faz a nova verificação? *Rubrica:* 3 = interrompe exportações com pacientes que não consentiram;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — aula 13 (capítulo 13 de 18)

[← Capítulo 12](#ch-12) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Privacidade e proteção de dados: automação

### Objetivos de aprendizagem

Você vai (1) automatizar uma regra de retenção; (2) tratar as exceções; (3) monitorar a automação.

### 14.1 A regra de retenção

Os registros de lembretes de consulta, que guardam o telefone, o horário da consulta e a situação da entrega, são necessários por cerca de um ano para resolver reclamações e conferir problemas de entrega. A tabela de retenção da Marlow fixa 365 dias. Os prontuários clínicos seguem regras profissionais mais longas e não fazem parte desta rotina. Leila escreve a regra com precisão: excluir os registros de lembrete cuja data de consulta seja mais de 365 dias anterior à data da execução, exceto os ligados a uma reclamação em aberto. Uma regra precisa é mais fácil de automatizar e de explicar aos auditores.

### 14.2 O laboratório da retenção

O laboratório aplica a regra a 1.200 registros sintéticos de lembretes. Encontra 712, 59,3%, com mais de 365 dias, e o registro mais antigo tem 900 dias. O resultado mostra que os lembretes nunca foram excluídos desde o início do serviço de SMS, então a maioria já ultrapassou sua finalidade. Leila aponta que cada registro em excesso contém um telefone ligado a uma consulta odontológica, que ficaria exposto se o banco de lembretes sofresse uma violação; a exclusão, portanto, reduz o risco diretamente. Apagar os 712 registros vencidos remove a maior parte dos telefones do banco sem afetar nenhuma consulta atual.

### 14.3 Exceções e segurança

Antes de ativar a exclusão, Leila acrescenta uma marcação de exceção para os registros ligados a reclamações em aberto, definida pela equipe de reclamações. Ela roda a rotina primeiro em modo somente relatório, listando o que seria excluído sem excluir nada, e o diretor de operações revisa as contagens. Só então a exclusão é ligada. Toda noite, a rotina grava num log um resumo das contagens excluídas e retidas, sem listar telefones. Ela explica que as execuções somente relatório são uma forma simples de pegar erros nas regras antes que os dados se percam de forma irreversível.

### 14.4 Monitorar a rotina

A rotina envia uma mensagem diária de sucesso com as contagens. Se nenhuma mensagem chegar, o prestador de TI recebe um alerta. A cada trimestre, Leila confere se o registro de lembrete mais antigo tem menos de 366 dias e se os registros retidos têm uma referência de reclamação vigente; as duas verificações levam minutos. Esse monitoramento enfrenta a falha silenciosa do capítulo 8. O Sr. Okafor observa que a automação aplica a limitação da conservação com confiabilidade, mas só se alguém perceber quando ela para, e é por isso que a mensagem de sucesso importa tanto quanto a própria rotina.

### Laboratório — Registros de lembretes além do prazo de retenção

```python
"""Apply a retention rule to synthetic appointment-reminder records (stdlib only)."""
import random, datetime
random.seed(11)
today = datetime.date(2026, 10, 1)
recs = [(i, today - datetime.timedelta(days=random.randint(0, 900))) for i in range(1200)]
keep_days = 365
expired = [r for r in recs if (today - r[1]).days > keep_days]
oldest = max((today - d).days for _, d in recs)
print(f"reminder records {len(recs)}; older than {keep_days} days {len(expired)} ({100*len(expired)/len(recs):.1f}%)")
print(f"oldest record {oldest} days")
```

Execute com `python3 lab_retention.py`. Saída verificada:

```text
reminder records 1200; older than 365 days 712 (59.3%)
oldest record 900 days
```

### Exemplo resolvido

Leila encontra 712 de 1.200 registros de lembretes (59,3%) com mais de 365 dias, acrescenta uma exceção para reclamações, roda primeiro em modo somente relatório e depois ativa a exclusão, com mensagens diárias de sucesso e verificações trimestrais.

> **Caso sintético.** Os registros são sintéticos.

### Erros e limites

Os backups ainda podem guardar registros excluídos até expirarem; documente a retenção dos backups.

### Exercícios

- **EX053 — Além da retenção.** Quantos registros de lembretes estavam além do prazo? *Rubrica:* 3 = 712 de 1.200, 59,3%;; 2 = aproximada;; 1 = errada;; 0 = nenhuma.
- **EX054 — Registro mais antigo.** Qual era a idade do registro mais antigo? *Rubrica:* 3 = 900 dias;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX055 — Somente relatório.** Por que rodar primeiro em modo somente relatório? *Rubrica:* 3 = pegar erros na regra antes de perder dados;; 2 = menciona erros;; 1 = vago;; 0 = nenhuma.
- **EX056 — Exceção.** Que registros ficam retidos? *Rubrica:* 3 = os ligados a reclamações em aberto;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — aula 14 (capítulo 14 de 18)

[← Capítulo 13](#ch-13) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Privacidade e proteção de dados: integração e dependências

### Objetivos de aprendizagem

Você vai (1) avaliar uma nova integração; (2) mapear as dependências; (3) limitar os dados compartilhados.

### 15.1 A nova integração

A Marlow quer ligar o sistema de gestão clínica a um serviço de avaliações online que envia e-mails aos pacientes depois das consultas pedindo uma nota. Leila avalia tecnicamente a integração antes de qualquer conexão. Pergunta de que dados o serviço precisa, o que guarda, onde, por quanto tempo, quem são seus suboperadores e como os pacientes podem recusar. A integração padrão do fornecedor pede nomes, e-mails, tipos de consulta e nomes dos dentistas, e publica por padrão as avaliações com o primeiro nome e o tipo de consulta. Leila registra cada resposta por escrito.

### 15.2 Dependências

Leila mapeia as dependências: o serviço de avaliações depende de um provedor de envio de e-mails e de uma empresa de hospedagem em nuvem, ambos suboperadores listados no contrato. A integração depende da interface do sistema de gestão clínica, que muda quando o fornecedor faz atualizações. Uma falha em qualquer parte poderia enviar e-mails a pacientes que recusaram ou publicar detalhes que eles não esperavam. Ela observa que cada dependência acrescenta uma parte que pode tratar dados de pacientes e um ponto onde a configuração pode se desviar, então as dependências pertencem ao modelo de tratamento.

### 15.3 Limitar os dados

Leila recomenda enviar só o primeiro nome, o e-mail e a clínica, sem o tipo de consulta nem o dentista, porque um pedido de avaliação não precisa deles, e tipos de consulta como implantes ou ortodontia revelam informações de saúde. A publicação dos tipos de consulta é desligada. Os pacientes que recusaram mensagens não essenciais são excluídos na origem, por um filtro na exportação, e não pelo serviço de avaliações. O encarregado pede uma avaliação de legítimo interesse e um contrato de operador antes de a integração entrar em produção, para que a base legal e as obrigações do fornecedor fiquem documentadas.

### 15.4 Testar a integração

Leila testa com pacientes sintéticos, incluindo um que recusou mensagens e outro com consulta de implante. O que recusou não recebe nada. O pedido do paciente do implante não traz o tipo de consulta, e uma avaliação de teste é publicada sem detalhes do tratamento. Ela também confere que excluir um paciente no sistema clínico leva à exclusão no serviço de avaliações dentro dos trinta dias combinados. Os três testes passam. A integração entra em produção numa clínica, e Leila agenda um novo teste para depois da próxima atualização do fornecedor, porque as atualizações costumam mudar os padrões.

### Exemplo resolvido

Leila avalia uma integração de avaliações, mapeia os suboperadores e as dependências da interface, limita os campos compartilhados a primeiro nome, e-mail e clínica, filtra as recusas na origem e testa com pacientes sintéticos.

> **Caso sintético.** A integração é sintética; os contratos do artigo 28 do GDPR e as avaliações de legítimo interesse são exigências reais.

### Erros e limites

Os fornecedores mudam os padrões nas atualizações; teste de novo depois de cada uma.

### Exercícios

- **EX057 — Campos padrão.** O que a integração padrão do fornecedor pedia? *Rubrica:* 3 = nomes, e-mails, tipos de consulta, nomes dos dentistas;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX058 — Tipo de consulta.** Por que retirar o tipo de consulta? *Rubrica:* 3 = revela informações de saúde e é desnecessário;; 2 = menciona saúde;; 1 = vago;; 0 = nenhuma.
- **EX059 — Filtro das recusas.** Onde os pacientes que recusaram são filtrados? *Rubrica:* 3 = na exportação de origem;; 2 = parcialmente correta;; 1 = no fornecedor;; 0 = nenhuma.
- **EX060 — Teste de exclusão.** Que comportamento de exclusão foi testado? *Rubrica:* 3 = a exclusão chega ao serviço de avaliações em até trinta dias;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — aula 15 (capítulo 15 de 18)

[← Capítulo 14](#ch-14) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Documentação técnica e segurança

### Objetivos de aprendizagem

Você vai (1) escrever documentação técnica clara para os controles de privacidade; (2) incluir segurança e reversão; (3) manter a documentação atualizada.

### 16.1 Por que a documentação importa

O prestador de TI da Marlow troca de equipe a cada poucos anos, e os gerentes mudam de clínica. Leila descobre que várias configurações de privacidade, como as zonas de rede e a rotina de exclusão dos lembretes, são entendidas por uma única pessoa; hoje, um único técnico do prestador concentra a maior parte desse conhecimento. Se essa pessoa sair, ninguém saberá por que uma configuração existe nem como conferi-la. O artigo 5(2) exige que a Marlow demonstre a conformidade, o que é impossível se ninguém consegue explicar os controles. A documentação transforma conhecimento pessoal em conhecimento da organização.

### 16.2 Estrutura de um documento de controle

Leila escreve um documento curto por controle, com estrutura fixa: finalidade, risco enfrentado, onde está configurado, como conferir que funciona, como são os resultados normais, o que fazer diante de resultados anormais, quem é o responsável e quando foi revisto pela última vez. O documento da rotina de exclusão, por exemplo, mostra onde ela roda, a mensagem diária esperada e a verificação trimestral. Ela mantém os documentos com menos de duas páginas e usa capturas de tela do ambiente de teste, nunca de telas com pacientes reais, para que os próprios documentos não exponham dados.

### 16.3 Segurança e reversão

Todo procedimento de mudança inclui passos de segurança. Antes de mudar as regras de rede, o prestador registra a configuração atual para poder restaurá-la. Antes de ativar a exclusão, a rotina roda em modo somente relatório. Antes de mudar perfis, uma conta de teste confirma que as tarefas diárias continuam funcionando. Cada procedimento diz como reverter e quando a reversão não é possível, como depois que os dados foram excluídos, e os passos de reversão também são testados. Leila explica que os passos irreversíveis merecem verificações extras, porque um erro não pode ser desfeito depois que os dados dos pacientes se foram.

### 16.4 Manter atualizada

Os documentos se afastam da realidade à medida que os sistemas mudam. Leila acrescenta uma data de revisão a cada documento e liga as revisões aos chamados de mudança: qualquer chamado que mexa num controle documentado precisa atualizar o documento antes de ser fechado. A cada seis meses, o encarregado recebe a lista dos documentos com a revisão vencida. O Sr. Okafor revisa os documentos de Leila e pede que ela retire dois parágrafos de teoria, porque a equipe operacional precisa de instruções e razões, e não de aulas, quando algo dá errado numa clínica movimentada.

### Exemplo resolvido

Leila escreve documentos de controle de duas páginas com finalidade, risco, local, verificações, resultados normais, ações diante de anomalias, responsável e data de revisão, acrescenta passos de reversão e liga as atualizações aos chamados de mudança.

> **Caso sintético.** Os documentos são sintéticos; o artigo 5(2) do GDPR é real.

### Erros e limites

Documentos escritos uma vez e nunca revistos acabam enganando.

### Exercícios

- **EX061 — Conhecimento concentrado.** Por que o conhecimento de uma só pessoa era um risco? *Rubrica:* 3 = ninguém conseguiria explicar os controles se essa pessoa saísse;; 2 = menciona a saída;; 1 = vago;; 0 = nenhuma.
- **EX062 — Partes do documento.** Cite quatro partes de um documento de controle. *Rubrica:* 3 = finalidade, risco, local, verificações, resultados, ações, responsável, data de revisão;; 2 = quatro;; 1 = duas;; 0 = nenhuma.
- **EX063 — Passos irreversíveis.** Por que os passos irreversíveis exigem verificações extras? *Rubrica:* 3 = os erros não podem ser desfeitos depois da exclusão;; 2 = menciona exclusão;; 1 = vago;; 0 = nenhuma.
- **EX064 — Manter atualizado.** Como os documentos são mantidos atualizados? *Rubrica:* 3 = datas de revisão e chamados de mudança que precisam atualizá-los;; 2 = menciona chamados;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — aula 16 (capítulo 16 de 18)

[← Capítulo 15](#ch-15) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Laboratório controlado II

### Objetivos de aprendizagem

Você vai (1) conduzir um teste de ponta a ponta com um paciente sintético; (2) verificar o atendimento aos direitos; (3) relatar as lacunas.

### 17.1 O paciente sintético

No segundo laboratório controlado, Leila cria no ambiente de teste da Marlow um paciente sintético que agenda online, recebe um lembrete, comparece a uma consulta com radiografia, paga, é encaminhado a um especialista e deixa uma avaliação. Depois, o paciente exerce dois direitos: o acesso, pelo artigo 15 do GDPR, e a eliminação dos dados não clínicos, pelo artigo 17, quando cabível; na LGPD, os incisos II e VI do art. 18. O laboratório segue os dados do paciente por todos os sistemas do modelo de tratamento, testando se o modelo e os controles se sustentam na prática. Nenhum paciente real é envolvido.

### 17.2 Pedido de acesso

Leila envia um pedido de acesso como o paciente sintético. A resposta inclui o registro do sistema de gestão clínica, a radiografia e a fatura, mas deixa de fora o histórico de lembretes, o registro no serviço de avaliações e a carta de encaminhamento na caixa de e-mail compartilhada. Leila observa que os itens esquecidos ficam todos em sistemas acrescentados ou alterados recentemente, que a lista de verificação não acompanhou. Ela os acrescenta à lista e recomenda que toda nova integração, como o serviço de avaliações, atualize a lista antes de entrar em produção, para que as respostas continuem completas.

### 17.3 Eliminação

O paciente então pede a exclusão dos dados de marketing e de avaliações, enquanto os prontuários clínicos ficam guardados por exigência das regras profissionais. Leila confere cada sistema: a plataforma de marketing remove o paciente, o serviço de avaliações remove a avaliação depois de nove dias, mas o banco de lembretes guarda o telefone até a regra anual removê-lo. Ela recomenda que os pedidos de eliminação acionem a exclusão imediata dos lembretes. Confirma também que os prontuários clínicos permanecem e que a carta de resposta, que lista cada sistema, explica com clareza por que eles são mantidos.

### 17.4 Relatar as lacunas

O relatório do laboratório lista cada sistema, o resultado esperado, o resultado observado e uma correção recomendada. São encontradas três lacunas: itens faltando na resposta de acesso, exclusão lenta dos lembretes e nenhum registro da cópia da carta de encaminhamento. Todas recebem responsáveis. O encarregado pede que o laboratório se repita todo ano. O Sr. Okafor observa que um único paciente sintético exercitou mais controles de privacidade da Marlow numa tarde do que meses de revisão de documentos, porque o teste seguiu de ponta a ponta os caminhos reais dos dados.

### Exemplo resolvido

Leila acompanha um paciente sintético pelo agendamento, tratamento, encaminhamento e avaliação, descobre respostas de acesso sem três fontes, encontra a exclusão lenta dos lembretes e relata correções com responsáveis.

> **Caso sintético.** O paciente é sintético; os artigos 15 e 17 do GDPR e o art. 18 da LGPD são reais.

### Erros e limites

A eliminação não se aplica aos registros que a Marlow é obrigada a guardar por lei; explique isso com clareza.

### Exercícios

- **EX065 — Itens faltantes.** Que itens faltaram na resposta de acesso? *Rubrica:* 3 = histórico de lembretes, registro de avaliações, carta de encaminhamento;; 2 = dois;; 1 = um;; 0 = nenhuma.
- **EX066 — Sistemas novos.** Por que os itens faltantes estavam em sistemas recentes? *Rubrica:* 3 = a lista não foi atualizada quando os sistemas mudaram;; 2 = menciona a lista;; 1 = vago;; 0 = nenhuma.
- **EX067 — Eliminação dos lembretes.** O que Leila recomendou para os lembretes na eliminação? *Rubrica:* 3 = excluí-los imediatamente a pedido;; 2 = parcialmente correta;; 1 = anualmente;; 0 = nenhuma.
- **EX068 — Prontuários clínicos.** Por que os prontuários clínicos são mantidos depois dos pedidos de eliminação? *Rubrica:* 3 = as regras profissionais exigem a guarda;; 2 = menciona regras;; 1 = vago;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — aula 17 (capítulo 17 de 18)

[← Capítulo 16](#ch-16) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Projeto técnico supervisionado

### Objetivos de aprendizagem

Você vai (1) planejar e entregar um projeto de privacidade supervisionado; (2) medir o resultado; (3) passar o trabalho à equipe de operações.

### 18.1 Escolher o projeto

No projeto final, Leila escolhe estender a segmentação da rede às sete clínicas ainda não cobertas, porque seu relatório de verificação a apontava como o maior controle não verificado e a exposição pelo Wi-Fi de visitantes afetava as imagens dos pacientes. Ela escreve um plano com escopo, cronograma, testes, passos de reversão e responsáveis. O diretor de operações aprova o plano, e o prestador de TI aceita fazer as mudanças de configuração fora do horário das clínicas, enquanto Leila prepara os testes e a documentação de cada clínica, com uma folha de teste própria para cada uma.

### 18.2 Entrega

O projeto avança uma clínica por semana. Em cada uma, o prestador registra a configuração atual, aplica o desenho de três zonas, e Leila testa a partir da rede de visitantes, da zona administrativa e da zona clínica. Na quarta clínica, as câmeras intraorais param de enviar imagens, porque usavam um endereço fora da zona clínica. O plano de reversão restabelece o serviço em vinte minutos, os endereços das câmeras são corrigidos, e a mudança é reaplicada na semana seguinte, com um teste a mais para a transferência das imagens das câmeras, que passa a fazer parte da folha de teste.

### 18.3 Medir o resultado

Depois de oito semanas, as oito clínicas têm três zonas, e, nos testes de Leila, o Wi-Fi de visitantes não alcança nenhum servidor de imagens. O relatório de verificação agora marca a segmentação como verificada em todas as clínicas. Ela também mede os efeitos colaterais: nenhum aumento nas chamadas de suporte depois da primeira semana e tempos de transferência das imagens inalterados. Apresenta os resultados com o registro das evidências, que acompanham cada afirmação, e anota o risco que resta: o tráfego DICOM dentro da zona clínica continua sem criptografia, o que exige um futuro projeto com o fornecedor.

### 18.4 Entrega e reflexão

Leila entrega o documento de controle, os scripts de teste e as evidências ao prestador de TI e ao encarregado, que combinam um novo teste anual. Na reflexão, ela observa que o trabalho técnico de privacidade é sobretudo configuração, teste e documentação cuidadosos, e não descobertas dramáticas. O Sr. Okafor encerra o curso lembrando que cada mudança técnica que ela fez, do conteúdo dos lembretes às zonas de rede, reduziu a chance de as informações de saúde de um paciente chegarem a quem não deveria vê-las. Leila é contratada pela Marlow como técnica.

### Exemplo resolvido

Leila estende a segmentação da rede a mais sete clínicas, recupera-se de uma falha das câmeras com a reversão, verifica as oito clínicas e entrega documentos e testes.

> **Caso sintético.** O projeto é sintético.

### Erros e limites

Projetos que terminam sem entrega à operação perdem seus controles; combine os responsáveis antes de encerrar.

### Exercícios

- **EX069 — Escolha do projeto.** Por que Leila escolheu a segmentação da rede? *Rubrica:* 3 = maior controle não verificado, com exposição das imagens dos pacientes;; 2 = menciona exposição;; 1 = vago;; 0 = nenhuma.
- **EX070 — Falha das câmeras.** O que falhou na quarta clínica? *Rubrica:* 3 = as câmeras intraorais não conseguiam enviar imagens;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX071 — Risco restante.** Que risco resta depois do projeto? *Rubrica:* 3 = DICOM sem criptografia dentro da zona clínica;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX072 — Entrega.** Quem recebe a entrega? *Rubrica:* 3 = o prestador de TI e o encarregado;; 2 = os dois;; 1 = um;; 0 = nenhuma.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — aula 18 (capítulo 18 de 18)

[← Capítulo 17](#ch-17) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX072. Leila Haddad, o Sr. Daniel Okafor, o Riverside Technical College, o Marlow Dental Group e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Revelam informações sobre a saúde do paciente, que o artigo 4(15) abrange.

**EX002.** O serviço é o que os usuários vivenciam; componentes como servidores e bancos de dados o entregam.

**EX003.** Cada cópia precisa ser protegida, excluída no prazo e incluída nos pedidos de acesso.

**EX004.** Nomes, telefones e horários de consulta, que revelam que são pacientes odontológicos.

**EX005.** Qualquer pessoa no Wi-Fi de visitantes poderia alcançar os compartilhamentos de arquivos do servidor de imagens.

**EX006.** Como um risco a reduzir pela segmentação da rede enquanto as mudanças do fornecedor são planejadas.

**EX007.** Zonas clínica, administrativa e de visitantes.

**EX008.** Testou a partir do Wi-Fi de visitantes e viu que o servidor de imagens ficou inalcançável.

**EX009.** Tornam impossível saber quem acessou qual prontuário.

**EX010.** Consultas, contatos e situação de pagamento, não as anotações de tratamento.

**EX011.** Quatro, de vinte e três.

**EX012.** Cada conta de substituto tem data de término vinda da escala e é desativada automaticamente.

**EX013.** Um campo de histórico médico aninhado em cada objeto de consulta.

**EX014.** As saídas são copiadas para chamados, chats e e-mails, criando divulgações.

**EX015.** Para com uma mensagem clara, em vez de adivinhar.

**EX016.** Criados com tempfile e removidos quando o script termina.

**EX017.** Os prontuários reais e a infraestrutura em nuvem do fornecedor.

**EX018.** Estava fora do escopo assinado, então ela pediu uma reprodução sintética.

**EX019.** Data, hora, sistema, método, observação e a saída que a comprova.

**EX020.** Que os arquivos não mudaram; não os mantém confidenciais.

**EX021.** Por finalidade, correspondendo ao registro das atividades de tratamento do artigo 30.

**EX022.** O artigo 9(2)(h), a prestação de cuidados de saúde.

**EX023.** O serviço de entregas que levava prescrições com nomes não tinha contrato.

**EX024.** A equipe de suporte do provedor de SMS fora da UE.

**EX025.** 95 de 400 linhas (23,8%).

**EX026.** Os logs agora usam números de reserva e só os três últimos dígitos do telefone.

**EX027.** São copiados para ferramentas de monitoramento e compartilhados com fornecedores em chamados de suporte.

**EX028.** Trinta dias para os logs detalhados.

**EX029.** Destinatário errado, retenção excessiva, acesso excessivo e falha silenciosa do controle.

**EX030.** As rotinas informam o sucesso todo dia, e a falta de um relatório dispara um alerta.

**EX031.** Só o nome da clínica e o horário da consulta.

**EX032.** Era uma violação de dados pessoais, que precisa ser documentada mesmo com baixo risco.

**EX033.** Para onde esta ferramenta envia os dados que lê?

**EX034.** A pergunta, a fonte dos dados, os passos, a saída esperada e a interpretação.

**EX035.** Para que os dados sintéticos, e portanto os resultados, sejam idênticos entre execuções.

**EX036.** Leem dados pessoais, então precisam das mesmas proteções que os outros sistemas.

**EX037.** Três de sete.

**EX038.** Era gravado automaticamente, antes de qualquer idioma ser escolhido.

**EX039.** Foi removido, porque a Marlow não precisava dele.

**EX040.** Mudanças no site e plugins costumam trazer de volta tags que carregam antes do consentimento.

**EX041.** Está desenhado corretamente, implementado como desenhado e operando de forma consistente?

**EX042.** Dezoito de vinte.

**EX043.** O servidor foi reiniciado para atualizações e a rotina não rodou.

**EX044.** Verificada em uma clínica, ainda não verificada nas outras sete.

**EX045.** 179 de 5.060 (3,5%).

**EX046.** S07, com 53 visualizações externas.

**EX047.** Uma designação temporária ou uma conta compartilhada (também um cargo regional ou curiosidade).

**EX048.** Que seus acessos aos prontuários são registrados e revisados.

**EX049.** Anotou primeiro os fatos conhecidos.

**EX050.** O campo dos lembretes (contact_ok) em vez de marketing_ok.

**EX051.** Nomes de campos confusos, nenhuma revisão da mudança e nenhuma verificação automática.

**EX052.** Interrompe qualquer exportação que inclua um paciente sem consentimento para marketing.

**EX053.** 712 de 1.200 (59,3%).

**EX054.** 900 dias.

**EX055.** Para conferir o que seria excluído antes de excluir qualquer coisa.

**EX056.** Os registros ligados a uma reclamação em aberto.

**EX057.** Nomes, e-mails, tipos de consulta e nomes dos dentistas.

**EX058.** Revela informações de saúde, e um pedido de avaliação não precisa dele.

**EX059.** Na exportação da Marlow, antes de os dados chegarem ao fornecedor.

**EX060.** Que excluir um paciente o remove do serviço de avaliações em até trinta dias.

**EX061.** Se essa pessoa saísse, ninguém saberia por que as configurações existem nem como conferi-las.

**EX062.** Finalidade, risco, onde está configurado e responsável (além de verificações, resultados, ações e data de revisão).

**EX063.** Depois que os dados dos pacientes são excluídos, um erro não pode ser desfeito.

**EX064.** Cada um tem data de revisão, e os chamados de mudança precisam atualizar os documentos afetados.

**EX065.** O histórico de lembretes, o registro no serviço de avaliações e a carta de encaminhamento.

**EX066.** A lista de verificação não foi atualizada quando os sistemas foram acrescentados ou alterados.

**EX067.** Os pedidos de eliminação devem acionar a exclusão imediata dos lembretes.

**EX068.** As regras profissionais obrigam a Marlow a guardá-los, o que a carta explica.

**EX069.** Era o maior controle não verificado e expunha as imagens dos pacientes ao Wi-Fi de visitantes.

**EX070.** As câmeras intraorais pararam de enviar imagens por causa dos seus endereços.

**EX071.** O tráfego DICOM dentro da zona clínica continua sem criptografia.

**EX072.** O prestador de TI e o encarregado.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 15, de 24 de abril de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Aprova o Regulamento de Comunicação de Incidente de Segurança*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Union. (2002). Directive 2002/58/EC of the European Parliament and of the Council of 12 July 2002 concerning the processing of personal data and the protection of privacy in the electronic communications sector (ePrivacy Directive), as amended by Directive 2009/136/EC. *Official Journal of the European Communities, L 201*, 37–47 (CELEX 32002L0058; ELI dir/2002/58/oj, confirmed via the Publications Office record). <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0058>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
