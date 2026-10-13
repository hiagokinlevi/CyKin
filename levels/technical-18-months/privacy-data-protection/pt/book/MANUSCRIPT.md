# Privacidade e Proteção de Dados: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 050, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 18 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3; os capítulos 7–18 (EX025–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). Leila Haddad, o Sr. Daniel Okafor, o Riverside Technical College, o Marlow Dental Group e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
