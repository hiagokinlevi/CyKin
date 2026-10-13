# Privacidade e Proteção de Dados: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 050, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–12 de 18 já estão escritos em português, com os exercícios EX001–EX048 e suas resoluções com rubricas de 0 a 3 e 3 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 13–18 (EX049–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

Capítulos 13–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-13), até a chegada dos próximos lotes.

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

- **EX001 — Dados de saúde.** Por que as anotações de tratamento odontológico são dados relativos à saúde? *Rubrica:* 3 = revelam informações sobre o estado de saúde da pessoa;; 2 = menciona saúde;; 1 = nada;; 0 = nenhuma.
- **EX002 — Serviço e componente.** Qual é a diferença entre um serviço e um componente? *Rubrica:* 3 = o serviço é o que os usuários vivenciam; os componentes o entregam;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX003 — As cópias importam.** Por que cada cópia de um registro importa? *Rubrica:* 3 = a proteção, a retenção e os pedidos de acesso precisam cobrir todas as cópias;; 2 = menciona cópias;; 1 = nada;; 0 = nenhuma.
- **EX004 — Conteúdo do SMS.** O que o gateway de SMS fica sabendo sobre os pacientes? *Rubrica:* 3 = nomes, telefones, horários de consulta e que são pacientes odontológicos;; 2 = a maioria;; 1 = um;; 0 = nenhuma.

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

- **EX005 — Risco dos visitantes.** Por que a rede compartilhada com os visitantes era um problema? *Rubrica:* 3 = os pacientes poderiam alcançar o servidor de imagens;; 2 = menciona o servidor;; 1 = nada;; 0 = nenhuma.
- **EX006 — DICOM.** Como Leila tratou o tráfego DICOM sem criptografia? *Rubrica:* 3 = como um risco gerido primeiro pela segmentação;; 2 = menciona segmentação;; 1 = nada;; 0 = nenhuma.
- **EX007 — Três zonas.** Cite as três zonas que Leila propôs. *Rubrica:* 3 = clínica, administrativa e de visitantes;; 2 = todas;; 1 = duas;; 0 = nenhuma.
- **EX008 — Confirmar a mudança.** Como Leila confirmou que a segmentação funcionou? *Rubrica:* 3 = testou a partir do Wi-Fi de visitantes que o servidor ficou inalcançável;; 2 = menciona teste;; 1 = nada;; 0 = nenhuma.

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

- **EX009 — Problema do login compartilhado.** Por que os logins compartilhados são um problema de privacidade? *Rubrica:* 3 = ninguém consegue saber quem abriu um prontuário;; 2 = menciona responsabilização;; 1 = nada;; 0 = nenhuma.
- **EX010 — Acesso da recepção.** De que a recepção precisa no sistema clínico? *Rubrica:* 3 = consultas, contatos, situação de pagamento;; 2 = a maioria;; 1 = anotações;; 0 = nenhuma.
- **EX011 — Contas de administrador.** Quantas contas de administrador restaram? *Rubrica:* 3 = quatro de vinte e três;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX012 — Controle dos substitutos.** Como as contas dos substitutos são controladas agora? *Rubrica:* 3 = datas de término ligadas à escala;; 2 = menciona data de término;; 1 = nada;; 0 = nenhuma.

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

- **EX013 — Campo aninhado.** Que campo desnecessário Leila encontrou na exportação JSON? *Rubrica:* 3 = histórico médico dentro das consultas;; 2 = correta;; 1 = nada;; 0 = nenhuma.
- **EX014 — Saída do script.** Por que os scripts devem evitar imprimir nomes? *Rubrica:* 3 = as saídas acabam em chamados e chats;; 2 = menciona propagação;; 1 = nada;; 0 = nenhuma.
- **EX015 — Ação da validação.** O que o script faz quando a validação falha? *Rubrica:* 3 = para com uma mensagem clara;; 2 = correta;; 1 = adivinha;; 0 = nenhuma.
- **EX016 — Arquivos temporários.** Como os arquivos temporários são tratados? *Rubrica:* 3 = módulo tempfile, removidos no fim;; 2 = menciona remoção;; 1 = mantidos;; 0 = nenhuma.

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
- **EX018 — Pedido recusado.** Por que Leila se recusou a ver um prontuário real? *Rubrica:* 3 = fora do escopo; reproduzir com dados sintéticos;; 2 = menciona escopo;; 1 = nada;; 0 = nenhuma.
- **EX019 — Campos da evidência.** O que cada registro de achado inclui? *Rubrica:* 3 = data, hora, sistema, método, observação, captura de tela;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX020 — Finalidade do hash.** O que o hash das evidências comprova? *Rubrica:* 3 = integridade, não confidencialidade;; 2 = correta;; 1 = confidencialidade;; 0 = nenhuma.

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
- **EX022 — Condição do atendimento.** Que condição do artigo 9 apoia o atendimento? *Rubrica:* 3 = artigo 9(2)(h);; 2 = correta;; 1 = consentimento;; 0 = nenhuma.
- **EX023 — Lacuna das entregas.** Que lacuna Leila encontrou no serviço de entregas? *Rubrica:* 3 = nenhum contrato de operador;; 2 = correta;; 1 = nada;; 0 = nenhuma.
- **EX024 — Possível transferência.** Que possível transferência Leila sinalizou? *Rubrica:* 3 = o suporte do provedor de SMS fora da UE;; 2 = correta;; 1 = nada;; 0 = nenhuma.

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
- **EX026 — Correção na origem.** O que o desenvolvedor mudou? *Rubrica:* 3 = registrar números de reserva e dígitos parciais do telefone;; 2 = menciona números de reserva;; 1 = nada;; 0 = nenhuma.
- **EX027 — Por que os logs viajam.** Por que os logs se espalham mais que os registros? *Rubrica:* 3 = são copiados para o monitoramento e compartilhados em chamados de suporte;; 2 = menciona cópias;; 1 = nada;; 0 = nenhuma.
- **EX028 — Retenção dos logs.** Que retenção Leila propôs para os logs detalhados? *Rubrica:* 3 = trinta dias;; 2 = correta;; 1 = noventa;; 0 = nenhuma.

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
- **EX030 — Detectar o silêncio.** Como as falhas silenciosas são detectadas? *Rubrica:* 3 = rotinas informam o sucesso todo dia; a falta do relatório gera alerta;; 2 = menciona diário;; 1 = nada;; 0 = nenhuma.
- **EX031 — Conteúdo do lembrete.** O que os lembretes devem conter agora? *Rubrica:* 3 = só o nome da clínica e o horário;; 2 = correta;; 1 = todos os detalhes;; 0 = nenhuma.
- **EX032 — Registro da violação.** Por que o caso do número errado foi registrado? *Rubrica:* 3 = era uma violação de dados pessoais, mesmo de baixo risco;; 2 = menciona violação;; 1 = nada;; 0 = nenhuma.

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

- **EX033 — Pergunta sobre as ferramentas.** Que pergunta Leila acrescentou à sua lista de ferramentas? *Rubrica:* 3 = para onde a ferramenta envia os dados que lê;; 2 = correta;; 1 = nenhuma;; 0 = nenhuma.
- **EX034 — Partes do método.** O que cada método define? *Rubrica:* 3 = pergunta, fonte, passos, saída esperada, interpretação;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX035 — Sementes fixas.** Por que usar sementes aleatórias fixas? *Rubrica:* 3 = dados sintéticos idênticos entre execuções;; 2 = menciona repetibilidade;; 1 = nada;; 0 = nenhuma.
- **EX036 — Ferramentas como tratamento.** Por que as próprias ferramentas de privacidade são um risco? *Rubrica:* 3 = também tratam dados pessoais;; 2 = menciona tratamento;; 1 = nada;; 0 = nenhuma.

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

- **EX037 — Antes do consentimento.** Quantos cookies eram gravados antes do consentimento sem isenção? *Rubrica:* 3 = 3 de 7;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX038 — Cookie de idioma.** Por que o cookie de idioma era um problema? *Rubrica:* 3 = era gravado antes de o visitante escolher um idioma;; 2 = menciona escolha;; 1 = nada;; 0 = nenhuma.
- **EX039 — Decisão sobre o pixel.** O que aconteceu com o pixel de publicidade? *Rubrica:* 3 = foi removido; ninguém precisava dele;; 2 = menciona remoção;; 1 = adiado;; 0 = nenhuma.
- **EX040 — Verificação a cada versão.** Por que acrescentar o teste de cookies à lista de cada versão? *Rubrica:* 3 = as mudanças costumam reintroduzir tags precoces;; 2 = menciona regressões;; 1 = nada;; 0 = nenhuma.

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
- **EX042 — Resultado da amostra.** Quantas contas da amostra conferiram? *Rubrica:* 3 = 18 de 20;; 2 = correta;; 1 = errada;; 0 = nenhuma.
- **EX043 — Execuções perdidas.** Por que a rotina de exclusão perdeu dois dias? *Rubrica:* 3 = reinicializações do servidor para atualizações;; 2 = correta;; 1 = nada;; 0 = nenhuma.
- **EX044 — Situação da segmentação.** Como Leila relatou a segmentação da rede? *Rubrica:* 3 = verificada em uma clínica, ainda não nas outras sete;; 2 = correta;; 1 = verificada;; 0 = nenhuma.

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
- **EX048 — Direitos da equipe.** O que a equipe precisa saber sobre os logs de auditoria? *Rubrica:* 3 = os acessos são registrados e revisados;; 2 = correta;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX048 (as de EX049–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). Leila Haddad, o Sr. Daniel Okafor, o Riverside Technical College, o Marlow Dental Group e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
