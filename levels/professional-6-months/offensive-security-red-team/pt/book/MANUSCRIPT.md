# Segurança Ofensiva Autorizada e Red Team: Um Guia para o Profissional

- Idioma: português do Brasil (`pt`); curso profissional, seis meses; aproximadamente 360 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–8 de 12 já estão escritos em português, com os exercícios EX001–EX040 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 9–12 (EX041–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais em início de carreira que entram na equipe de segurança de uma organização.
- Relação com os livros vizinhos: o [livro do curso rápido](../../../../rapid-1-month/offensive-security-red-team/pt/book/MANUSCRIPT.md) é uma introdução em quatro capítulos; o [livro do técnico](../../../../technical-18-months/offensive-security-red-team/pt/book/MANUSCRIPT.md) se aprofunda em ferramentas e verificação. **Este livro é um guia compacto para o profissional.**
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação acreditada. **Não concede autorização para testar sistemas reais.** Todas as organizações, pessoas e números são **sintéticos**, salvo quando uma frase cita uma fonte pública. Os laboratórios ensinam escopo, filtragem, gestão de tickets e relatórios — nunca técnicas transformadas em armas.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–3 cobrem fundamentos, contexto e autorização; os capítulos 4–7 cobrem métodos, ferramentas, fluxo de trabalho e verificação; os capítulos 8–10 cobrem análise de casos, comunicação e qualidade; os capítulos 11–12 são o laboratório supervisionado e o portfólio. Cada capítulo traz objetivos, ensino, um exemplo resolvido, um caso sintético rotulado, erros e limites, cinco exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios dos capítulos 3, 5 e 10 leem apenas dados locais (`python3 file.py`).

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Harborline Credit Union (HCU)** — internet banking, VPN da equipe, núcleo AS/400 (fora do escopo), camada web de homologação | Organização estudada ao longo do livro | Inventada |
| **Leo Okonkwo** | Profissional júnior de segurança na HCU | Inventado |

### Fontes principais

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

Capítulos 9–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-09), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de segurança para profissionais

### Objetivos de aprendizagem

Você vai (1) situar a segurança ofensiva autorizada entre as outras práticas de segurança; (2) nomear confidencialidade, integridade e disponibilidade com exemplos de uma cooperativa de crédito; (3) explicar o menor privilégio e a defesa em profundidade; (4) listar os referenciais que este curso usa.

### 1.1 Onde os testes ofensivos se encaixam

O trabalho de segurança inclui arquitetura, monitoramento, resposta a incidentes e testes autorizados. Os testes encontram o que as outras práticas deixaram passar, sob permissão por escrito. Eles não substituem a aplicação de patches, o registro de logs nem o treinamento. Na HCU, o escopo do ENG-440 de Leo cobre a homologação do internet banking e a VPN da equipe, e as revisões dele ficam ao lado da aplicação de patches, dos logs e do treinamento, em vez de substituí-los. Quando aparece uma constatação, Leo ainda pergunta se a aplicação de patches ou o monitoramento deveriam tê-la detectado, para que os testes alimentem o endurecimento do dia a dia em vez de competir com ele. Um relatório limpo do ENG-440 continua deixando o trabalho com os atributos Secure e HttpOnly dos cookies para a equipe de segurança de aplicações e as lacunas de MFA para os responsáveis pela VPN.

### 1.2 CIA em uma cooperativa de crédito

A confidencialidade protege os dados das contas dos associados; a integridade protege saldos e instruções de transferência; a disponibilidade mantém o internet banking utilizável. Uma constatação é julgada pelo que ela ameaça, e, quando Leo classifica uma constatação, ele diz qual das três está em jogo. Um cookie de sessão sem Secure e HttpOnly ameaça a confidencialidade das sessões dos associados; uma senha de administrador compartilhada ameaça a integridade das mudanças; um teste que bloqueia contas ameaça a disponibilidade. O mesmo problema técnico pode atingir mais de uma, e o relatório deve dizer isso. O bloqueio de contas é o motivo pelo qual as ROE proíbem o password spraying: uma única execução descuidada no dia do pagamento poderia impedir os associados de acessar seus salários. A constatação sobre os atributos do cookie no ENG-440 é classificada principalmente pela confidencialidade, porque uma sessão roubada expõe a visão da conta de um associado.

### 1.3 Menor privilégio e profundidade

Contas e caminhos de rede devem permitir apenas o necessário. Várias camadas — rede, aplicação, identidade, monitoramento — fazem com que uma única falha não encerre a história. Os testadores procuram lugares onde faltam camadas. Na VPN da equipe, menor privilégio significa que cada administrador tem uma conta nominal em vez de um login compartilhado, e profundidade significa que uma senha roubada ainda enfrenta o MFA e o monitoramento. Leo procura lugares onde falta uma camada, como um caminho administrativo alcançável sem o jump host, porque é ali que uma única falha encerra a história.

### 1.4 Referenciais que você vai citar

NIST SP 800-115 para planejar avaliações; PTES para as etapas do engajamento; OWASP WSTG para verificações web; MITRE ATT&CK para os nomes de técnicas; TIBER-EU e CBEST para testes guiados por ameaças no setor financeiro. Cada referência responde a uma pergunta diferente, por isso Leo cita a que corresponde à decisão que está sendo registrada. Ele abre primeiro o OWASP WSTG para os testes de aplicação web na homologação do internet banking, o PTES para as etapas do engajamento e o NIST SP 800-115 quando planeja que tipo de avaliação a HCU precisa. O ATT&CK fornece nomes de técnicas como T1078 Valid Accounts para o SOC. TIBER-EU e CBEST só importam se a HCU vier a patrocinar um teste guiado por ameaças.

### 1.5 O que os profissionais produzem

Os profissionais produzem planos com escopo definido, constatações validadas, relatórios claros e correções verificadas — não pilhas de ruído de scanner sem confirmação. A primeira semana de Leo entrega um plano com escopo para o internet banking e a VPN, e não um despejo de scanner. Mais adiante, ele vai produzir constatações validadas, um relatório claro para o CISO e para os engenheiros e correções verificadas com evidências de reteste. Essas quatro entregas são o que o CISO e os examinadores conseguem auditar. O ruído de ferramenta sem confirmação fica fora do relatório, para que os responsáveis atuem sobre o que é real; ruído de scanner sem validação desperdiça o tempo de quem corrige e esconde os problemas que importam para os associados.

### 1.6 Confiança dos associados

Os associados confiam à HCU seus salários e economias. Um teste descuidado que bloqueia contas ou vaza um extrato destrói essa confiança mais rápido do que a maioria das constatações técnicas. Todo método que Leo propõe precisa responder: que dano aos associados isto pode causar se der errado, e como evitamos isso? Essa pergunta molda as ROE: homologação primeiro, nada de password spraying, parar se dados de associados aparecerem inesperadamente. Uma transferência de dia de pagamento bloqueada ou um extrato vazado prejudicariam associados que nunca escolheram fazer parte de um teste, por isso a prevenção é escrita nos métodos e nas condições de parada antes que qualquer pacote saia.

### Exemplo resolvido (HCU sintética)

Leo Okonkwo entra na equipe de segurança da HCU. Sua primeira semana é um mapa: o internet banking e a VPN da equipe estão na próxima revisão autorizada; o núcleo bancário AS/400 está fora do escopo. Ele fixa as perguntas de CIA acima da mesa.

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX001 — Três práticas.** Cite três práticas de segurança além dos testes autorizados. *Rubrica:* 3 = três entre arquitetura, monitoramento, resposta a incidentes, aplicação de patches, treinamento; 2 = duas; 1 = uma; 0 = nada.
- **EX002 — Associação CIA.** Associe: extratos de associados vazados; valor de transferência alterado; internet banking fora do ar. *Rubrica:* 3 = C, I, A; 2 = dois; 1 = um; 0 = nada.
- **EX003 — Menor privilégio.** Dê um exemplo de menor privilégio em uma cooperativa de crédito. *Rubrica:* 3 = conta/caminho concreto limitado ao necessário; 2 = vago; 1 = errado; 0 = nada.
- **EX004 — Defesa em profundidade.** Por que um único firewall não basta? *Rubrica:* 3 = outras camadas podem falhar de forma independente; aplicação/identidade/monitoramento continuam necessários; 2 = parcial; 1 = ele basta; 0 = nada.
- **EX005 — Escolha de referencial.** Qual fonte Leo abriria primeiro para estruturar um teste de aplicação web? *Rubrica:* 3 = OWASP WSTG; 2 = ATT&CK; 1 = só CBEST; 0 = nada.

### Síntese

Os testes autorizados ficam ao lado das outras práticas; CIA, menor privilégio e referenciais públicos moldam todo engajamento.

### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Contexto de serviços e partes interessadas

### Objetivos de aprendizagem

Você vai (1) identificar os serviços da HCU e quem é responsável por eles; (2) explicar por que o núcleo bancário costuma ficar fora do escopo; (3) mapear as partes interessadas de um engajamento; (4) escrever um parágrafo de contexto para um plano de teste.

### 2.1 Serviços que importam

A HCU opera internet banking, uma VPN da equipe, e-mail, um site para associados e um núcleo bancário em um AS/400. O internet banking e a VPN são alcançáveis pela internet e mudam com frequência; são alvos iniciais comuns de revisão autorizada, por isso a próxima revisão autorizada de Leo começa por eles. A VPN da equipe tem prioridade alta porque uma senha de administrador compartilhada ali alcançaria sistemas internos, como a constatação posterior do ENG-440 mostrou. O e-mail e o site público também importam, mas mudam com menos frequência e estão mais abaixo no plano atual. O AS/400 está na lista para que todos saibam que ele existe e que é deixado de lado de propósito. Cada serviço da lista traz o nome do seu responsável, para que Leo saiba a quem perguntar antes que qualquer verificação o toque.

### 2.2 Por que o núcleo bancário é excluído

O AS/400 guarda o sistema de registro dos saldos. Uma indisponibilidade acidental pararia as agências. A menos que um trabalho especializado e fortemente controlado seja financiado, ele fica fora do escopo e é protegido por controles compensatórios. Esses controles — isolamento de rede, caminhos administrativos rigidamente limitados e monitoramento — são o que torna a exclusão defensável diante dos examinadores. O plano de Leo os nomeia, com o responsável de cada um, em vez de fingir que o sistema é invisível, para que os examinadores possam fazer perguntas diretamente à equipe de rede. Um trabalho especializado exigiria financiamento próprio, ROE próprias e operadores treinados nessa plataforma; até que seja financiado, o AS/400 aparece no relatório apenas como uma exclusão com seus controles listados.

### 2.3 Partes interessadas

O CISO autoriza; o responsável de produto do internet banking aceita o risco; a equipe de rede abre regras temporárias; o SOC observa o tráfego de teste; o jurídico revisa o contrato. O trabalho de Leo é saber quem decide o quê, por isso, antes do kickoff, ele consegue nomear cada pessoa e o que ela precisa aprovar. Se o responsável de produto não aceitou o risco residual, ou se o SOC não foi avisado da janela, ele não começa. Ele mantém no ticket do ENG-440 um registro de aprovação datado, de uma linha, para cada parte interessada; a regra temporária de firewall da equipe de rede, por exemplo, precisa estar ativa até as 08:00 de sábado, ou a janela é adiada. Saber quem decide o quê evita um teste que está autorizado no papel, mas bloqueado na prática.

### 2.4 Contexto no plano

Um bom plano declara o propósito de negócio (proteger os associados, atender às expectativas dos examinadores), os serviços dentro e fora do escopo e os horários de pico a evitar (por exemplo, a sexta-feira de pagamento). O rascunho de Leo para a HCU declara o propósito (dados dos associados e o exame anual), lista o internet banking e a VPN no escopo, exclui o AS/400, a rede de caixas eletrônicos e a processadora de cartões e evita a janela de processamento em lote da manhã de sábado. A janela de sábado e a exclusão do dia de pagamento ficam ao lado da lista de hosts, para que um revisor veja julgamento sobre horários, e não apenas endereços. Os revisores também podem conferir os horários com a escala do SOC, já que os analistas de plantão naquela manhã de sábado precisam esperar o tráfego de teste.

### 2.5 Terceiros

Processadoras de cartões e e-mail em nuvem são organizações separadas. Testá-las exige a autorização delas, não apenas a da HCU. O plano de Leo lista a processadora de cartões e o e-mail em nuvem como fora do escopo por esse motivo, para que um testador entusiasmado não invente uma permissão que nunca foi concedida. Se a HCU quiser testá-los, o CISO precisa obter autorização por escrito de cada fornecedor e anexá-la às ROE. A assinatura da HCU sozinha nunca cobre os sistemas de outra organização, por mais conveniente que fosse sondar a processadora de cartões na mesma janela de sábado.

### 2.6 Expectativas dos examinadores

As cooperativas de crédito passam por exames de segurança e solidez que perguntam como os sistemas são testados. O parágrafo de contexto de Leo também é evidência para os examinadores: mostra que a HCU escolhe o escopo deliberadamente, exclui sistemas frágeis e agenda os testes em torno da operação, em vez de testar "tudo o que responde a um ping". O parágrafo é arquivado com as ROE, de modo que os examinadores leem o mesmo raciocínio de escopo que o CISO assinou e devem ver que a HCU testou o que pretendia testar. Nomear a exclusão do AS/400 e a fuga da janela de lote é tão útil quanto listar o que estava no escopo, porque mostra julgamento, e não uma checklist de todos os hosts alcançáveis.

### Exemplo resolvido (HCU sintética)

Leo escreve: "Propósito: reduzir o risco aos dados dos associados e autenticar o internet banking antes do exame anual. No escopo: camada web do internet banking e VPN da equipe. Fora do escopo: núcleo AS/400, rede de caixas eletrônicos, processadora de cartões terceirizada. Evitar: janela de processamento em lote da manhã de sábado."

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX006 — Cinco serviços.** Liste cinco serviços da HCU citados no capítulo. *Rubrica:* 3 = cinco corretos; 2 = quatro; 1 = dois; 0 = nada.
- **EX007 — Motivo da exclusão do AS/400.** Por que o AS/400 costuma ficar fora do escopo? *Rubrica:* 3 = sistema de registro; uma indisponibilidade para as agências; exige controles especializados; 2 = parcial; 1 = "é antigo"; 0 = nada.
- **EX008 — Quem autoriza.** Quem na HCU autoriza o engajamento? *Rubrica:* 3 = o CISO (com a aceitação do responsável de produto); 2 = o CISO; 1 = Leo; 0 = nada.
- **EX009 — Papel do SOC.** O que o SOC precisa saber antes de o teste começar? *Rubrica:* 3 = janela, IPs de origem, métodos ruidosos esperados; para não tratar o teste às cegas como ataque real; 2 = parcial; 1 = vago; 0 = nada.
- **EX010 — Terceiro.** As ROE da HCU podem, sozinhas, autorizar o teste da processadora de cartões? *Rubrica:* 3 = não; é necessária a autorização da própria processadora; 2 = não; 1 = sim; 0 = nada.

### Síntese

Serviços, responsáveis, exclusões e terceiros entram no plano antes de qualquer método ser escolhido.

### Continue estudando — capítulo 02 de 12

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Prática autorizada e tratamento de evidências

### Objetivos de aprendizagem

Você vai (1) preencher uma checklist de regras de engajamento; (2) explicar a retenção e a anonimização de evidências; (3) recusar trabalho que não tenha contato de emergência; (4) descrever a cadeia de custódia dos dados de teste.

### 3.1 Checklist antes do kickoff

Todo campo obrigatório das regras de engajamento precisa estar preenchido: escopo, exclusões, métodos, janela, contato de emergência, tratamento de dados e público do relatório. Um contato de emergência vazio interrompe o teste.

```python
"""Lab 3: validate a synthetic rules-of-engagement checklist before testing starts."""
required = ["in_scope", "out_of_scope", "allowed_methods", "window", "emergency_contact",
            "data_handling", "report_audience"]
draft = {"in_scope": "192.0.2.0/24 web and VPN", "out_of_scope": "core banking AS/400",
         "allowed_methods": "config review, authenticated web tests", "window": "Sat 08:00-12:00",
         "emergency_contact": "", "data_handling": "delete within 30 days", "report_audience": "CISO"}
missing = [k for k in required if not draft.get(k)]
print("complete" if not missing else "MISSING: " + ", ".join(missing))
for k in required:
    print(f"  {k}: {draft.get(k) or '(empty)'}")
```

Execute com `python3 lab_roe.py`. Saída verificada:

```text
MISSING: emergency_contact
  in_scope: 192.0.2.0/24 web and VPN
  out_of_scope: core banking AS/400
  allowed_methods: config review, authenticated web tests
  window: Sat 08:00-12:00
  emergency_contact: (empty)
  data_handling: delete within 30 days
  report_audience: CISO
```

O laboratório imprime MISSING quando `emergency_contact` está vazio e lista os demais campos, para que Leo veja o que já está preenchido. No rascunho do exemplo, todos os campos estão preenchidos, exceto `emergency_contact`, e é por isso que o laboratório imprime uma única linha MISSING. Ele não vai agendar a janela de sábado, das 08:00 às 12:00, até que o CISO nomeie um contato de plantão. Um campo vazio é uma parada, não um convite para improvisar.

### 3.2 Regras de evidências

Capture apenas o que comprova a constatação. Anonimize os identificadores dos associados. Guarde as evidências no repositório aprovado, com acesso limitado à equipe do engajamento. Apague ou devolva as evidências quando o acordo determinar. Na HCU, isso significa capturas de tela sem nomes de associados nem números de conta, guardadas sob o ticket do engajamento no cofre, e não em chat pessoal; a evidência de que falta um atributo no cookie não precisa do token de sessão de um associado real. O acesso à pasta do ENG-440 é limitado à equipe nomeada no acordo. Quando o acordo diz para apagar em até 30 dias, Leo agenda a exclusão e a confirma, e o registro no cofre mostra a data de exclusão ao lado da pasta, para que um revisor confira que a regra foi cumprida.

### 3.3 Cadeia de custódia

Anote quem coletou cada item, quando e cada transferência. Nos laboratórios de aula, o registro é curto; em exames reais, ele pode ser examinado a fundo. A linha de custódia de Leo no ENG-440 anota quem exportou cada arquivo, de qual jump host e quando ele entrou no cofre. Um registro de custódia de duas linhas basta para o engajamento de aula ENG-CLASS-11, mas ele registra exatamente os campos que Leo vai usar no ENG-440, para que a prática se transfira. Se uma evidência muda de mãos na troca de turno, a linha de transferência nomeia as duas pessoas e o identificador do ticket; a falta de custódia é a forma como arquivos se perdem antes de um exame.

### 3.4 Dispositivos pessoais

Não guarde evidências da HCU em notebooks pessoais nem em aplicativos de chat. Use o ambiente fornecido. A HCU fornece um ambiente de jump restrito para os testes. Uma evidência que sai dele — copiada para um celular, colada no WhatsApp ou salva em um drive pessoal — viola o acordo e pode expor dados de associados. Leo trata o ambiente fornecido como o único lugar onde as evidências podem ficar. Se precisar trabalhar remotamente, ele usa a VPN para entrar nesse ambiente, nunca uma pasta sincronizada que copia arquivos para uma máquina de casa. Se uma cópia chegar a sair, Leo informa o CISO no mesmo dia, em vez de apagá-la discretamente.

### 3.5 Sala de aula versus produção

Estes laboratórios validam checklists em rascunhos sintéticos; eles não substituem a revisão jurídica de ROE reais. Passar no `lab_roe` com um rascunho sintético prova que Leo consegue identificar um contato de emergência ausente; não significa que ROE reais estejam prontas. ROE reais também precisam da assinatura do CISO, da verificação do contrato pelo jurídico e da aprovação de firewall pela equipe de rede, e nada disso o laboratório simula. Leo declara esse limite entre sala de aula e produção em todo relatório de laboratório, para que ninguém trate uma aprovação em aula como autorização de produção.

### 3.6 Quando a checklist falha

Se algum campo obrigatório das ROE estiver vazio na manhã do teste, Leo cancela a janela por escrito e informa o CISO e o SOC. Recomeçar depois de uma correria para preencher campos gera erros; um adiamento limpo custa menos do que uma hora não autorizada. Ele publica o cancelamento no canal do engajamento, com o campo ausente nomeado, e o CISO e o líder do SOC recebem o mesmo cancelamento por escrito, para que ninguém mantenha um plano de sábado desatualizado na agenda nem espere tráfego. Uma nova janela só é marcada depois que a checklist imprime `complete` em ROE completas; o cancelamento por escrito o protege se alguém afirmar mais tarde que os testes ocorreram sem elas.

### 3.7 O acordo vence o hábito

Mesmo que Leo tenha testado o mesmo site de homologação no trimestre passado, ele não reutiliza as ROE do trimestre passado. Sistemas, responsáveis e exclusões mudam. Cada engajamento começa com um acordo assinado e atual, e a checklist é executada contra esse acordo, não contra a memória. As exclusões do trimestre passado podem ter omitido um novo host de homologação que agora é adjacente à produção; executar a checklist contra o acordo assinado atual detecta isso, e o novo host também precisaria de um responsável nomeado na lista de partes interessadas antes que Leo pudesse incluí-lo no escopo. Ele data cada execução da checklist e guarda a saída com as novas ROE no cofre, para que a verificação possa ser mostrada depois. Hábito não é autorização.

### Exemplo resolvido (HCU sintética)

Leo executa a checklist no rascunho das ROE. Ela imprime MISSING: emergency_contact. Ele não vai agendar a janela de sábado até que o CISO nomeie um contato de plantão e o campo seja preenchido.

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX011 — Campo ausente.** O que o laboratório imprime como linha de status, e o que Leo precisa fazer? *Rubrica:* 3 = MISSING: emergency_contact; não começar até preencher; 2 = só "ausente"; 1 = começar mesmo assim; 0 = nada.
- **EX012 — Contato preenchido.** Se `emergency_contact` passar a ser "SOC on-call +1-555-0100", qual é a linha de status? *Rubrica:* 3 = complete; 2 = ok; 1 = continua ausente; 0 = nada.
- **EX013 — Anonimização.** Uma captura de tela mostra o número completo da conta de um associado. O que fazer antes de arquivá-la? *Rubrica:* 3 = anonimizar/mascarar; manter só os dígitos necessários para provar o problema; 2 = parcial; 1 = arquivar como está; 0 = nada.
- **EX014 — Chat pessoal.** Leo pode colar evidências em um chat privado de WhatsApp com um colega? *Rubrica:* 3 = não; usar apenas o repositório aprovado; 2 = não; 1 = sim, se for privado; 0 = nada.
- **EX015 — Nota de custódia.** Escreva uma entrada de custódia de uma linha para uma exportação de configuração. *Rubrica:* 3 = quem, o quê, quando, de onde; 2 = dois campos; 1 = vago; 0 = nada.

### Síntese

Sem contato de emergência, não há teste; as evidências são minimizadas, retidas conforme o acordo e nunca deixadas em dispositivos pessoais.

### Continue estudando — capítulo 03 de 12

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Métodos centrais

### Objetivos de aprendizagem

Você vai (1) descrever as etapas do PTES em ordem; (2) separar descoberta de validação; (3) explicar por que a exploração é opcional e restrita; (4) escolher métodos compatíveis com as ROE da HCU.

### 4.1 A espinha dorsal do PTES

As etapas do PTES dão uma ordem comum: pré-engajamento (definição de escopo), coleta de inteligência, modelagem de ameaças, análise de vulnerabilidades, exploração, pós-exploração e relatório. As ROE atuais da HCU permitem análise e testes web autenticados, não exploração ampla. Por isso, a tabela de métodos de Leo para na coleta de inteligência, na análise de vulnerabilidades e nos testes web autenticados na homologação, e marca cada etapa do PTES como permitida, não permitida ou fora do escopo, para que o CISO veja onde o ENG-440 termina. Exploração e pós-exploração ficam fora do plano até que as ROE sejam reescritas e assinadas de novo; avançar porque uma ferramenta facilitou quebraria a confiança do SOC. Usar os nomes do PTES ajuda o CISO e as empresas externas a compartilhar um único vocabulário.

### 4.2 Descoberta versus validação

A descoberta lista problemas possíveis; a validação os confirma com evidências dentro das regras. A saída de uma ferramenta, sozinha, é descoberta. Uma configuração incorreta confirmada, com captura de tela e impacto de negócio, é uma constatação. Um outdated-banner com confiança 0.7 é descoberta até que Leo confirme a versão, a exposição e o impacto com evidências; ele compara o banner com o boletim do fornecedor para aquela versão antes de decidir se aquilo chega a ser uma constatação. Só então ele vira uma constatação, com severidade e recomendação. No laboratório do capítulo 5, um FLOOR de 0.6 mantém open-redirect em 0.9, outdated-banner em 0.7 e cookie-flag em 0.85, mas, sem evidência e sem declaração de impacto, um item continua fora da lista de constatações.

### 4.3 Exploração restrita

Se as ROE vierem a permitir a demonstração de uma falha, use o menor passo que mostre o impacto, em contas acordadas, com parada se algo inesperado acontecer. Este curso continua sem ensinar desenvolvimento de exploits. Se a HCU vier a permitir uma prova de impacto, Leo usa uma conta de teste acordada que contém apenas dados sintéticos, para que uma prova nunca mostre o saldo de um associado real. Ele dá o menor passo que mostra o problema e não inventa passos além das ROE. Um bloqueio de conta, um vazamento de dados ou um host que não seja de homologação provoca parada imediata e uma ligação para o contato de emergência.

### 4.4 Associar métodos às ROE

O plano de Leo associa cada método a uma linha das ROE. O que não estiver associado fica de fora. As verificações autenticadas do WSTG na homologação correspondem aos métodos permitidos e aos sistemas no escopo. O password spraying não tem linha, então fica de fora; ele também correria o risco de bloquear contas reais de associados na semana do pagamento, o que é um dos motivos pelos quais as ROE o omitem. As sondagens ao AS/400 têm uma linha de exclusão, então ficam de fora. Cada linha da tabela de métodos de Leo traz a cláusula das ROE em que se apoia, para que um revisor confira a associação linha por linha. Métodos não associados não ganham uma execução de teste; eles esperam uma atualização por escrito das ROE, e o ENG-440 não ganha pontos extras por criatividade fora da tabela.

### 4.5 Modelagem de ameaças leve

Mesmo sem um cenário completo de red team, nomeie os atores prováveis (senha de associado roubada, phishing contra a equipe), para que as verificações se concentrem no que importa para a HCU. No internet banking, esses são os atores que Leo nomeia. Esse foco direciona as verificações para o tratamento de sessões, a política de senhas e o MFA da VPN, em vez de peculiaridades obscuras de protocolo que nenhum ator provável usaria contra a HCU. O uso indevido por pessoas internas e os ataques ao AS/400 ficam fora deste modelo leve porque o ENG-440 não pode testá-los. Nomear essas exclusões no modelo permite que o relatório explique por que uma verificação estava ou não no escopo quando os examinadores perguntarem.

### 4.6 Limites da coleta de inteligência

O OSINT sobre a HCU fica restrito a páginas públicas e documentos publicados. Raspar fóruns de associados, comprar dados vazados ou se passar por funcionários está fora, a menos que as ROE permitam explicitamente um cenário de engenharia social — o que as ROE atuais da HCU não fazem. A coleta de Leo se limita ao site público da HCU e aos documentos publicados que qualquer pessoa consegue abrir sem entrar no internet banking. Comprar dados vazados ou raspar fóruns de associados reuniria inteligência fora das ROE e poderia expor pessoas reais. Ele não faz coleta em ritmos que pareçam abuso e registra o que coletou. Se algum dia for necessário um cenário de engenharia social, ele terá sua própria aprovação por escrito.

### 4.7 O relatório como etapa do método

O PTES termina com o relatório porque constatações que nunca chegam aos responsáveis não mudam nada. Leo reserva tempo para a redação e a revisão dentro da janela do engajamento, em vez de tratar o relatório como hora extra não paga depois dos testes. No ENG-440, ele bloqueia a última parte da janela de sábado para redação e revisão por pares, e os testes que avançam sobre esse tempo reservado são interrompidos, em vez de espremer a revisão. Se a redação passar do tempo, a validação inacabada vira uma lacuna explícita no relatório, e não uma alegação silenciosa de cobertura total. Constatações que ficam só nas anotações dele até segunda-feira não ajudam ninguém antes do exame; o relatório é uma etapa do método com relógio, não um detalhe posterior.

### Exemplo resolvido (HCU sintética)

A tabela de métodos de Leo: OSINT em páginas públicas da HCU (permitido); verificações autenticadas do WSTG na homologação do internet banking (permitido); password spraying (proibido); sondagens ao AS/400 (fora do escopo).

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX016 — Ordem das etapas.** Coloque em ordem: relatório, análise de vulnerabilidades, pré-engajamento, exploração. *Rubrica:* 3 = pré-engajamento, análise de vulnerabilidades, exploração, relatório; 2 = quase toda; 1 = aleatória; 0 = nada.
- **EX017 — Descoberta ou constatação.** A ferramenta relata outdated-banner com confiança 0.7. Isso já é uma constatação? *Rubrica:* 3 = descoberta até ser validada com evidências e impacto; 2 = parcial; 1 = já é constatação; 0 = nada.
- **EX018 — Por que o spraying é proibido.** Por que a HCU proíbe o password spraying? *Rubrica:* 3 = bloqueios/dano aos associados/ruído; não está entre os métodos permitidos; 2 = parcial; 1 = "é lento"; 0 = nada.
- **EX019 — Prova mínima.** O que significa "menor passo que mostra o impacto"? *Rubrica:* 3 = parar assim que o impacto for mostrado; sem pivotamento extra; 2 = parcial; 1 = sempre tomar o domínio inteiro; 0 = nada.
- **EX020 — Associar um método.** Associe "verificações autenticadas do WSTG na homologação" à linguagem das ROE. *Rubrica:* 3 = cita allowed_methods e in_scope da homologação; 2 = parcial; 1 = não associado; 0 = nada.

### Síntese

Os métodos seguem a ordem do PTES e as ROE; a descoberta só vira constatação depois de evidências validadas.

### Continue estudando — capítulo 04 de 12

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Ferramentas e interpretação

### Objetivos de aprendizagem

Você vai (1) tratar scanners como assistentes, e não como juízes; (2) filtrar constatações por confiança e confirmação; (3) explicar falsos positivos e falsos negativos; (4) registrar as versões das ferramentas nas evidências.

### 5.1 As ferramentas ajudam

Scanners e checklists aceleram a descoberta. Eles rotulam errado, perdem o contexto e não conseguem julgar o impacto de negócio. Leo lê todo item mantido: quando o `lab_severity` mantém três de cinco itens, ele ainda abre cada item mantido e pergunta se a HCU deveria agir. Itens que ele não consegue explicar em palavras simples quanto ao impacto sobre os associados voltam para mais validação ou são descartados. Os dois itens descartados, dir-listing e trace-method, são anotados no apêndice de método, para que ninguém se pergunte se foram ignorados. Os scanners ajudam na descoberta; eles não julgam o impacto sobre os associados nem escrevem a recomendação.

### 5.2 Piso de confiança

A HCU descarta itens não confirmados abaixo de um piso de confiança, para que o relatório não seja inflado com ruído.

```python
"""Lab 5: filter a synthetic tool finding list, dropping noise below a confidence floor."""
findings = [("open-redirect", 0.9, True), ("dir-listing", 0.4, False),
            ("outdated-banner", 0.7, True), ("cookie-flag", 0.85, True), ("trace-method", 0.3, False)]
FLOOR = 0.6
kept = [(n, c) for n, c, confirmed in findings if c >= FLOOR and confirmed]
for n, c in kept:
    print(f"KEEP {n:16} confidence={c}")
print(f"kept {len(kept)} of {len(findings)}; dropped {len(findings)-len(kept)}")
```

Execute com `python3 lab_severity.py`. Saída verificada:

```text
KEEP open-redirect    confidence=0.9
KEEP outdated-banner  confidence=0.7
KEEP cookie-flag      confidence=0.85
kept 3 of 5; dropped 2
```

Com FLOOR em 0.6, o laboratório mantém open-redirect (0.9), outdated-banner (0.7) e cookie-flag (0.85) e descarta o resto. Dir-listing e trace-method ficam abaixo de 0.6, por isso permanecem no apêndice de saída bruta, e não na lista de constatações, e itens não confirmados abaixo do piso nunca aparecem nos slides executivos. Subir o piso para 0.8 descartaria também o banner. Leo declara o piso nas notas de método, para que os leitores saibam o que foi filtrado.

### 5.3 Falsos positivos e negativos

Um falso positivo desperdiça o tempo de quem corrige; um falso negativo deixa o risco. A amostragem e a validação manual reduzem os dois; nenhum chega a zero. Leo planeja o tempo de validação a partir das taxas históricas de falsos positivos e aceita que algum risco ainda possa escapar. Se os falsos positivos da última revisão se concentraram em uma verificação do scanner, essa verificação ganha tempo extra de validação no ENG-440. Na dúvida, ele valida mais em vez de entregar uma lista maior. Ele diz ao CISO que o relatório contém itens validados, e não que todos os problemas possíveis foram encontrados.

### 5.4 Versões e configurações

Registre o nome da ferramenta, a versão e o perfil junto com as evidências, para que um reteste possa usar a mesma configuração. As evidências de Leo para a constatação do cookie-flag nomeiam o scanner, sua versão e o perfil usado, e o nome do perfil fica registrado no ticket T-15, para que o reteste depois da correção da equipe de segurança de aplicações repita a mesma verificação com as mesmas configurações de varredura. Sem versões, um reteste que falha não consegue dizer se a correção falhou ou se a configuração mudou. Configurações que mudam no meio do engajamento são registradas com o horário da mudança, para que as evidências continuem dizendo qual configuração produziu cada resultado.

### 5.5 O OWASP WSTG como ferramenta de raciocínio

Mesmo sem scanner, o WSTG oferece uma lista estruturada de verificações web, para que a cobertura fique visível. Leo usa uma checklist derivada do WSTG para a homologação do internet banking, para mostrar quais verificações foram executadas e quais estavam fora do escopo. As linhas são marcadas como executada, não executada ou fora do escopo, e cada linha executada aponta para seu arquivo de evidência no cofre. A cobertura que existe só na cabeça dele não pode ser revisada nem retestada. Linhas vazias na checklist são lacunas honestas; inventar cobertura não ajuda ninguém quando os examinadores perguntam o que foi realmente testado.

### 5.6 Interpretar banners

Um banner desatualizado é uma pista, não uma crise. Leo verifica se o serviço está exposto à internet, se a versão é realmente vulnerável e se um WAF ou uma regra de acesso já limita a exposição antes de escrever uma constatação de severidade alta. Na camada de homologação da HCU, um banner desatualizado atrás de regras de acesso pode ter baixa prioridade; o mesmo banner em uma porta administrativa exposta à internet não teria. Para o banner do ENG-440, Leo registra que a homologação fica atrás de regras de acesso, e é por isso que ele não é classificado como alto. Ele escreve esse raciocínio na constatação, para que a severidade não seja um rótulo misterioso desligado do impacto sobre os associados; o contexto transforma uma pista em uma constatação proporcional.

### 5.7 Taxas de base

Se um scanner marca quarenta itens e o histórico mostra que trinta foram falsos positivos, Leo planeja o tempo de validação de acordo: quarenta itens brutos com esse histórico sugerem cerca de dez constatações reais. As taxas de base protegem o cronograma. Ele não promete ao CISO "quarenta constatações" antes da validação, porque isso cria a expectativa errada e pressiona a equipe a manter ruído. O tempo de validação faz parte do orçamento do engajamento, não é hora extra opcional, e Leo promete um conjunto validado com um prazo definido para a confirmação.

### 5.8 Verificações manuais por amostragem

A cada cinco itens automatizados mantidos, Leo valida manualmente, de ponta a ponta e com uma conta autorizada, pelo menos o de maior severidade. As verificações por amostragem detectam erros sistemáticos das ferramentas que uma pontuação de confiança não detecta, porque esses erros aparecem quando um humano repete o caminho. No ENG-440, o `lab_severity` mantém três itens e open-redirect, em 0.9, é o mais alto, por isso Leo percorre esse caminho primeiro, com uma conta autorizada, antes de o relatório ser redigido. Se o percurso do open-redirect falhar, os outros itens mantidos passam pelo mesmo caminho humano antes da redação do relatório.

### Exemplo resolvido (HCU sintética)

Leo filtra a lista sintética: open-redirect, outdated-banner e cookie-flag são mantidos; dir-listing e trace-method são descartados. Ele ainda valida manualmente os três itens mantidos antes que entrem no relatório.

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX021 — Contagem do laboratório.** Quantas constatações o laboratório mantém, e quais são descartadas? *Rubrica:* 3 = 3 mantidas; dir-listing e trace-method descartadas; 2 = só a contagem; 1 = errado; 0 = nada.
- **EX022 — Subir o piso.** Se FLOOR passar a 0.8, quais itens permanecem? *Rubrica:* 3 = só open-redirect e cookie-flag; 2 = um; 1 = os três; 0 = nada.
- **EX023 — Falso positivo.** Dê um exemplo de falso positivo na HCU. *Rubrica:* 3 = o scanner aponta um problema que a configuração da homologação mostra estar mitigado; 2 = parcial; 1 = vago; 0 = nada.
- **EX024 — Falso negativo.** Dê um exemplo de falso negativo na HCU. *Rubrica:* 3 = o problema existe, mas a ferramenta não o detecta (por exemplo, falha na lógica de autenticação); 2 = parcial; 1 = vago; 0 = nada.
- **EX025 — Nota de versão.** Escreva a linha sobre a ferramenta que Leo acrescenta às evidências. *Rubrica:* 3 = nome, versão, perfil/configurações; 2 = só o nome; 1 = vago; 0 = nada.

### Síntese

As ferramentas propõem; as pessoas decidem — filtrar, validar, registrar versões e só então relatar.

### Continue estudando — capítulo 05 de 12

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Fluxo de trabalho operacional

### Objetivos de aprendizagem

Você vai (1) descrever o fluxo de trabalho do dia do teste, do kickoff ao debrief; (2) manter um registro de atividades contemporâneo; (3) coordenar com o SOC; (4) lidar com uma dúvida de escopo no meio do teste.

### 6.1 A sequência do dia

A chamada de kickoff confirma as ROE e os contatos; os testadores começam apenas dentro da janela; as notas de progresso vão para o canal do engajamento; há uma verificação intermediária com o responsável de produto se algo sensível aparecer; há um debrief no fim do dia; as evidências vão para o cofre. No ENG-440, a sequência de sábado de Leo segue essa ordem. Nada começa antes que o kickoff confirme que as ROE ainda correspondem à cópia assinada, e as evidências vão para o cofre antes de ele ir embora. Desvios da sequência são registrados com um motivo, para que uma revisão posterior veja por quê.

### 6.2 Registro de atividades

Toda ação recebe horário, sistema, método e resultado. O registro defende a equipe se uma indisponibilidade for atribuída aos testes e alimenta o relatório. A linha de registro de Leo inclui horário, host, método e resultado, como uma pausa quando um nome de host parecia ser de produção. Cada linha usa o relógio do jump host, para que as entradas do registro e os alertas do SOC possam ser alinhados depois, sem adivinhar diferenças de horário. Os registros ficam no cofre com as evidências, e não apenas em um histórico de chat que vai rolando para longe. Se o tráfego do dia de pagamento ficar lento, é o registro que mostra se os testes estavam envolvidos.

### 6.3 Coordenação com o SOC

Envie mensagens de início e de fim. Se o SOC vir alertas relacionados, ele liga para o contato de emergência, em vez de bloquear o acesso de Leo sem aviso. A mensagem de início de Leo no ENG-440 sai às 08:05, menciona apenas a homologação e traz o identificador do ticket, o IP de origem e o horário de término, 12:00. Se o SOC ligar por causa do IP dele, ele confirma o ticket, compartilha a janela e reduz o ritmo ou pausa se pedirem; qualquer mudança de ritmo é escrita no registro de atividades com o horário e o nome do analista. Às 12:00, Leo publica o fim no canal do engajamento, com o identificador do ticket, para que o SOC retire o IP dele da lista de observação. Testar em silêncio diante de um SOC atento cria incidentes evitáveis.

### 6.4 Dúvidas no meio do teste

Descobriu um novo nome de host? Pause e pergunte. Não "inclua só desta vez". Às 09:40, Leo encontra um nome de host que pode ser de produção; ele pausa, pergunta ao responsável de produto, descobre que é de homologação, registra a decisão e continua. A resposta do responsável de produto confirmando que o host pertence à homologação é colada no ticket antes de os testes recomeçarem, para que o ENG-440 mostre julgamento sob pressão de tempo, e não um palpite de sorte. A pergunta custa minutos; uma sondagem não autorizada em um host com cara de produção custaria o engajamento. Adivinhar teria sido sair do escopo.

### 6.5 Estado final

Na hora de parar, pare. Verificações inacabadas viram trabalho para a próxima janela ou notas explícitas de falta de tempo — não extrapolações silenciosas. Às 12:00, Leo para, mesmo que uma verificação do WSTG esteja pela metade. A verificação inacabada é listada no relatório com a etapa a que chegou, para que a próxima janela comece dali. O SOC espera silêncio depois da mensagem de fim das 12:00, então qualquer pacote posterior vindo do IP de Leo pareceria um ataque. Extrapolações silenciosas quebram o acordo em que o SOC e o CISO confiaram, e a parada das 12:00 no ENG-440 é a mesma regra que ele pratica no ENG-CLASS-11.

### 6.6 Passagem entre testadores

Se Leo encerra o turno e um colega continua, o registro de atividades e o cofre de evidências são a passagem de bastão. Notas verbais não bastam; o colega precisa ver o que já foi validado, para não retestar de forma destrutiva nem perder uma condição de parada. O colega que abre o cofre deve ver as constatações validadas, as dúvidas em aberto e as condições de parada já atingidas. As notas de passagem nomeiam a próxima ação segura e o que não pode ser repetido, como uma pausa que Leo já acordou. Quando um colega assume no meio da janela, a nota mais o caminho no cofre bastam; Leo não deixa contexto crítico apenas na própria cabeça.

### 6.7 Disciplina no canal de comunicação

O chat do engajamento serve para escopo, paradas e status — não para piadas sobre "hackear o banco". A linguagem casual vaza para capturas de tela e prejudica a confiança se um examinador ler o canal mais tarde. Leo escreve o status em palavras simples e profissionais, com identificadores de ticket, porque capturas de tela do canal podem aparecer nas evidências ou na revisão dos examinadores. As capturas de tela do ENG-440 são limpas de bagunça da área de trabalho e de abas sem relação antes de entrarem no cofre sob o identificador do ticket. A comunicação fica no canal do engajamento; o chat pessoal não é repositório de evidências do ENG-440.

### 6.8 Extensões de janela

Se o trabalho precisar continuar além da janela, Leo para, pede uma extensão por escrito ao CISO e espera a confirmação antes que qualquer outro pacote saia do notebook dele. Um "claro, pode continuar" verbal não basta, nem mesmo vindo do CISO ao telefone. Uma extensão por escrito nomeia o novo horário de término e é arquivada com as ROE antes de o trabalho recomeçar. Se o sábado se estender, o notebook de Leo não envia mais nenhum pacote até que essa extensão exista, porque o SOC e o contato de emergência precisam ver o mesmo relógio que Leo usa.

### Exemplo resolvido (HCU sintética)

Às 08:05, Leo publica "ENG-440 start — staging only" (início do ENG-440, apenas homologação). Às 09:40, ele encontra um nome de host que pode ser de produção; pausa, pergunta ao responsável de produto, descobre que é de homologação, registra a decisão e continua.

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX026 — Mensagem de início.** Quais quatro fatos pertencem à mensagem de início de Leo? *Rubrica:* 3 = ticket/identificador, lembrete do escopo, janela, contato do testador; 2 = três; 1 = um; 0 = nada.
- **EX027 — Linha de registro.** Escreva uma linha do registro de atividades para uma verificação de sessão do WSTG. *Rubrica:* 3 = horário, sistema, método, resultado; 2 = três; 1 = vago; 0 = nada.
- **EX028 — Alerta do SOC.** O SOC liga por causa de alertas vindos do IP de Leo. O que ele faz? *Rubrica:* 3 = confirma o teste autorizado; compartilha janela/ticket; ajusta o ritmo se pedirem; 2 = parcial; 1 = ignora; 0 = nada.
- **EX029 — Novo nome de host.** Qual é o processo correto quando aparece um novo nome de host? *Rubrica:* 3 = pausar; perguntar ao responsável; atualização de escopo por escrito, se necessário; 2 = parcial; 1 = testá-lo; 0 = nada.
- **EX030 — Hora de parar.** A janela termina com uma verificação inacabada. O que Leo faz? *Rubrica:* 3 = para; anota o item inacabado para a próxima janela; 2 = para; 1 = extrapola; 0 = nada.

### Síntese

O fluxo de trabalho é kickoff, trabalho registrado, visibilidade para o SOC e pausar para perguntar — nunca ampliação silenciosa do escopo.

### Continue estudando — capítulo 06 de 12

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Controles e verificação

### Objetivos de aprendizagem

Você vai (1) sugerir controles compatíveis com as constatações; (2) distinguir controles compensatórios; (3) planejar um reteste; (4) saber quando um controle está verificado.

### 7.1 Associar o controle à constatação

Uma constatação de senha de administrador compartilhada pede contas nominais e cofre de senhas; um open redirect pede destinos em lista de permissões; um atributo ausente no cookie pede o atributo configurado e verificado na CI. Leo escreve cada recomendação de acordo com a constatação: contas nominais na VPN e um cofre para senhas compartilhadas; destinos em lista de permissões para um open redirect; atributos Secure e HttpOnly verificados na CI para o cookie de sessão. A equipe de segurança de aplicações é responsável por Secure e HttpOnly na constatação do cookie-flag, e a linha da recomendação traz esse nome e um prazo. Conselhos genéricos como "endurecer a aplicação" ou "endurecer as sessões" não dizem a um responsável o que mudar.

### 7.2 Controles compensatórios

Quando a correção ideal está a meses de distância, um controle compensatório reduz o risco agora — por exemplo, caminhos administrativos da VPN restritos aos jump hosts enquanto a reutilização de senhas é eliminada. Leo registra o controle compensatório como temporário, com um responsável e uma data para rever a correção ideal, para que ele não se torne permanente por descuido. Restrições temporárias de rede em torno de um banner desatualizado são aceitáveis nos mesmos termos: depois que o banner recebe o patch, as regras de acesso saem do ticket com uma nota de reteste e um registro de horário de retirada. Compensações sem prazo viram dívida esquecida.

### 7.3 Desenho do reteste

Reteste apenas as constatações acordadas, com o mesmo método ou um equivalente, depois que o responsável disser que a correção está no ar. Registre aprovação ou reprovação com evidências. Depois que o responsável diz que os atributos do cookie estão no ar na homologação, Leo repete a mesma verificação com a versão de ferramenta registrada, e a aprovação ou reprovação vai para o ticket com uma captura de tela nova. Ele confere nomes de host, portas e versões de build com a nota de mudança do responsável antes de declarar que um reteste falhou. Um reteste que toque um host fora da lista original do ENG-440 espera uma atualização de escopo por escrito, e retestar constatações sem relação desperdiça a janela.

### 7.4 O que significa verificado

Verificado significa que Leo reproduziu o sintoma original e o viu corrigido (ou confirmou que o controle compensatório funciona), e não que o responsável disse que corrigiu. A confirmação de implantação pelo responsável é necessária, mas não suficiente. Leo ou outro testador precisa ver que o sintoma original sumiu, ou que o controle compensatório funciona, antes de o ticket ser marcado como verificado. As capturas de tela do cookie, de antes e depois, entram no cofre com hash e são vinculadas ao T-15, para que a verificação seja evidência no registro, e não uma garantia verbal de que alguém acha que está corrigido.

### 7.5 Acompanhamento

As constatações viram tickets com responsáveis e datas; a verificação os fecha. Cada constatação da HCU vira um ticket com um responsável e um prazo, e as evidências de verificação o fecham. Tickets sem responsáveis ou datas escondem risco no backlog, e é por isso que o `lab_ticket` do capítulo 10 sinaliza campos incompletos: ele marca o T-15 como incompleto em owner e verified, e o T-18 como incompleto em due date, e esses nunca contam como prontos para fechamento. Toda sexta-feira, Leo abre o rastreador, e campos de responsável ou prazo em branco são escalados na mesma semana, em vez de envelhecerem até virar constatações de exame.

### 7.6 Correções parciais

Às vezes, os responsáveis corrigem um caminho e deixam outro aberto. A checklist de reteste de Leo nomeia cada caminho da constatação original. Um ticket não é fechado até que nenhum dos caminhos listados reproduza o problema ou que um controle compensatório aceito seja verificado. Em um open redirect, Leo lista cada parâmetro e caminho da constatação original; fechar depois de corrigir apenas um deixa os associados expostos nos outros. Se um caminho de redirecionamento continuar aberto depois de uma correção parcial, o CISO o aceita por escrito, com prazo de expiração, ou o ticket permanece aberto no rastreador até que o risco residual tenha responsável ou seja eliminado.

### 7.7 Responsáveis pela verificação

Quem aplica uma correção não deve ser a única pessoa a marcá-la como verificada. Leo ou outro testador retesta; o responsável confirma a implantação. A separação mantém os fechamentos otimistas fora das métricas: "corrigido porque eu implantei" não sobrevive a um reteste separado. A mesma regra vale para Leo, então um colega verifica qualquer controle compensatório que ele tenha aplicado, e o fechamento nunca depende das mesmas mãos que fizeram a mudança. Métricas que contam tickets verificados só depois da assinatura de um testador separado mantêm os números honestos para o CISO e os examinadores.

### 7.8 Vigilância de regressões

Depois de uma correção, Leo pergunta se os caminhos relacionados foram verificados pelo responsável. Um open redirect corrigido que deixa um segundo parâmetro intocado é uma regressão comum; o plano de reteste nomeia os caminhos irmãos quando existem. Quando o responsável corrige um parâmetro de redirecionamento, o plano de reteste de Leo já nomeia os parâmetros irmãos da constatação, e regressões custam menos quando detectadas na mesma janela do que no próximo ciclo de exame. A vigilância de regressões depois do ENG-440 também verifica se os atributos do cookie e as correções de redirecionamento continuam nos builds seguintes. Uma correção que desaparece na próxima implantação da homologação reabre o ticket com o identificador do build anexado.

### Exemplo resolvido (HCU sintética)

Para a senha de administrador compartilhada da VPN, a HCU habilita MFA e contas nominais em duas semanas (ideal) e, enquanto isso, restringe os caminhos administrativos ao jump host (compensatório). Leo retesta os dois.

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX031 — Associação de controle.** Sugira um controle para um open redirect. *Rubrica:* 3 = lista de permissões para os destinos de redirecionamento / remover o parâmetro; 2 = parcial; 1 = "firewall"; 0 = nada.
- **EX032 — Exemplo compensatório.** Dê um controle compensatório para a reutilização de senhas na administração da VPN. *Rubrica:* 3 = restringir a administração ao jump host / MFA / monitoramento; 2 = parcial; 1 = ignorar; 0 = nada.
- **EX033 — Gatilho do reteste.** Quando o reteste começa? *Rubrica:* 3 = depois que o responsável confirma a correção no ar / na janela acordada; 2 = parcial; 1 = sempre imediatamente; 0 = nada.
- **EX034 — Não verificado.** O responsável envia um e-mail dizendo "corrigimos" sem detalhes. Está verificado? *Rubrica:* 3 = não; são necessárias evidências de reteste; 2 = não; 1 = sim; 0 = nada.
- **EX035 — Escopo do reteste.** Leo pode testar URLs novas sem relação durante o reteste? *Rubrica:* 3 = não; só as constatações acordadas, a menos que o escopo seja ampliado; 2 = não; 1 = sim; 0 = nada.

### Síntese

Os controles correspondem às constatações; os controles compensatórios compram tempo; a verificação é um reteste com evidências.

### Continue estudando — capítulo 07 de 12

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Análise supervisionada de casos

### Objetivos de aprendizagem

Você vai (1) analisar um dossiê de caso sintético da HCU; (2) separar fatos de suposições; (3) propor os próximos passos autorizados; (4) escalar quando necessário.

### 8.1 O dossiê do caso

Um pacote sintético contém: um trecho das ROE, três constatações validadas, o registro de atividades e uma nota de que um funcionário reutilizou a senha da VPN em um e-mail pessoal (relatado pelo próprio funcionário). O pacote é rotulado ENG-440 e guardado no cofre, e registra fatos, suposições e ações em linhas rotuladas. A nota sobre a reutilização de senha é marcada como relatada pelo funcionário, e não como algo que Leo descobriu mexendo no e-mail pessoal, que continua fora do escopo. O relatório vai para o CISO como uma questão de conscientização da equipe, porque a reutilização envolve contas fora do engajamento.

### 8.2 Fatos versus suposições

Fato: a reutilização de senha foi relatada. Suposição: um atacante já tem a senha. Leo rotula as suposições com clareza: seu dossiê diz Fato para o relato e Suposição para qualquer afirmação de que um atacante já tem a senha. As suposições podem orientar os próximos passos, mas nunca são escritas como constatações confirmadas. A linha de Suposições da nota do caso diz que ainda não há nenhuma sobre abuso externo, que é tudo o que as evidências sustentam. Se a revisão de logs do SOC mostrar mais tarde sessões incomuns na VPN, a suposição pode passar a Fato, com o trecho do log anexado.

### 8.3 Próximos passos dentro das ROE

Forçar a redefinição da senha da VPN dessa conta; verificar os logs da VPN em busca de sessões incomuns; não tocar no e-mail pessoal (fora do escopo). Leo solicita a redefinição da senha da VPN dessa conta e pede ao SOC que verifique os logs em busca de sessões incomuns. O pedido de redefinição passa por um ticket da central de serviços de TI vinculado ao ENG-440, para que a linha do tempo fique em um só lugar. O e-mail pessoal está fora do escopo, por isso ele não contata o provedor nem pede os logs dessa caixa de entrada. O funcionário que relatou a reutilização troca ele mesmo a senha pessoal; a HCU nunca toca nessa conta.

### 8.4 Escalonamento

O risco de exposição de dados de associados e a reutilização de senhas em serviços pessoais vão para o CISO no mesmo dia. O escalonamento no mesmo dia dá ao CISO tempo para ordenar redefinições de senha da VPN e comunicações antes que o risco se espalhe para além do caso de reutilização relatado pelo funcionário; esperar a reunião semanal de constatações seria lento demais para uma exposição de dados de associados. O CISO recebe a nota por telefone e por e-mail antes do fim do expediente. Leo escala com uma linha do tempo de uma página com os fatos, as suposições rotuladas como suposições e a próxima ação segura, e não apenas com frustração.

### 8.5 Rótulo do ATT&CK

A reutilização de senha que permite acesso à VPN corresponde a T1078 Valid Accounts na busca de detecções do SOC. Leo acrescenta T1078 à nota do caso para que o SOC possa pesquisar com um nome comum. O rótulo descreve o comportamento; ele não prova que um atacante externo esteve envolvido. O SOC usa o nome da técnica para puxar suas detecções de T1078 já existentes para a VPN, em vez de escrever novas às pressas. Se a busca não encontrar nada, o relatório diz que não foram vistas sessões incomuns no período revisado, e não que a conta nunca foi usada indevidamente.

### 8.6 Escrever para o dossiê do caso

As notas de caso usam registros de horário, identificadores de ticket e os rótulos Fato/Suposição/Ação. Uma narrativa livre serve para o resumo, mas são as linhas rotuladas que o CISO e os auditores conseguem percorrer em um minuto durante um incidente. Durante o incidente de reutilização de senha, cada linha rotulada começa com um registro de horário e o identificador do ticket ENG-440, para que o CISO ordene fatos, suposições e ações de relance, sem ler antes uma longa narrativa. Leo ainda escreve um resumo curto para quem precisa da história; ele tem três ou quatro frases e fica acima das linhas rotuladas, nunca no lugar delas.

### 8.7 Hora de escalar

Leo usa uma regra simples: se fundos de associados, dados pessoais em grande escala ou sistemas de segurança física puderem ser afetados, escale em até uma hora. Itens de menor impacto seguem o processo normal de constatações. A reutilização de senha que poderia abrir a VPN entra nessa regra de uma hora, porque dados de associados poderiam vir em seguida. O relógio começa quando Leo lê o relato do funcionário, e a ligação para o CISO é registrada com o horário em relação a esse início. O banner desatualizado de baixo impacto na homologação entra no relatório do ENG-440 com o prazo normal da equipe de segurança de aplicações, e não no telefone do CISO.

### 8.8 Colaboração com o SOC no caso

Leo compartilha a técnica do ATT&CK e o identificador da conta com o SOC, para que ele possa fazer a busca, mas não cola dados pessoais de associados no ticket. As consultas de busca usam o identificador da conta da VPN e o período do ENG-440. O ticket do SOC contém o identificador da conta, o período e T1078, e nada que identifique um associado: nomes, documentos de identidade e números completos de conta ficam fora do ticket do SOC e das capturas de tela de chat. As capturas de tela da busca são recortadas às colunas de sessão antes de entrarem no cofre.

### Exemplo resolvido (HCU sintética)

A nota de caso de Leo: "Fatos: relato de funcionário sobre a senha da VPN reutilizada no e-mail pessoal; constatações F1–F3 validadas. Suposições: ainda nenhuma sobre abuso externo. Ações: redefinição de senha, revisão de logs, briefing ao CISO. Fora do escopo: conteúdo do e-mail pessoal."

> **Caso sintético — Harborline Credit Union (HCU).** A cooperativa de crédito, Leo Okonkwo e todos os números foram inventados para fins didáticos.

### Erros e limites

Políticas e leis locais variam; siga a autorização da HCU e a sua jurisdição. Este livro nunca autoriza testes em sistemas reais.

### Exercícios

- **EX036 — Extrair fatos.** Liste dois fatos do dossiê do caso. *Rubrica:* 3 = dois itens claramente factuais; 2 = um; 1 = suposição tratada como fato; 0 = nada.
- **EX037 — Rótulo de suposição.** Reescreva "os atacantes com certeza têm a senha" como uma suposição rotulada. *Rubrica:* 3 = incerteza rotulada; 2 = parcial; 1 = continua categórica; 0 = nada.
- **EX038 — Ação fora do escopo.** Por que não ler o e-mail pessoal do funcionário? *Rubrica:* 3 = fora do escopo / sem autorização / privacidade; 2 = parcial; 1 = deveria ler; 0 = nada.
- **EX039 — Escalar no mesmo dia.** O que dispara o escalonamento ao CISO no mesmo dia neste caso? *Rubrica:* 3 = risco da reutilização de credenciais para a VPN/serviços dos associados; 2 = parcial; 1 = vago; 0 = nada.
- **EX040 — ATT&CK.** Qual nome de técnica ajuda o SOC a buscar detecções para este caso? *Rubrica:* 3 = T1078 Valid Accounts; 2 = só o nome; 1 = errado; 0 = nada.

### Síntese

O trabalho de caso separa fatos de suposições, age apenas dentro do escopo e escala o risco real no mesmo dia.

### Continue estudando — capítulo 08 de 12

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX040 (as de EX041–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). A Harborline Credit Union, Leo Okonkwo e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Arquitetura, monitoramento de segurança e resposta a incidentes (aplicação de patches e treinamento da equipe também contam).

**EX002.** Confidencialidade; integridade; disponibilidade.

**EX003.** Uma conta de caixa que consegue consultar saldos, mas não consegue aprovar transferências acima de um valor definido.

**EX004.** Atacantes que contornam ou abusam de um caminho permitido ainda enfrentam verificações na aplicação, controles de identidade e monitoramento; a falha de uma camada não deveria expor tudo.

**EX005.** OWASP Web Security Testing Guide — ele é organizado em torno de casos de teste de aplicações web.

**EX006.** Internet banking, VPN da equipe, e-mail, site para associados e o núcleo bancário AS/400.

**EX007.** Ele é o sistema de registro dos saldos; erros de teste poderiam parar as agências, por isso exige um trabalho especializado e cuidadosamente controlado, se chegar a ser testado.

**EX008.** O CISO autoriza; o responsável de produto do internet banking aceita o risco residual desse serviço.

**EX009.** A janela de horário, os endereços de origem e quais métodos podem parecer ataques, para que os analistas distingam o teste autorizado de um incidente real.

**EX010.** Não. A processadora de cartões é uma organização separada; seus sistemas precisam da autorização por escrito dela própria.

**EX011.** `MISSING: emergency_contact` — ele bloqueia o kickoff até que o CISO forneça um contato e a checklist passe.

**EX012.** `complete`

**EX013.** Mascarar o número da conta, para que a constatação continue demonstrável sem expor o identificador do associado.

**EX014.** Não. As evidências ficam no repositório aprovado, sob as regras de acesso do acordo.

**EX015.** "2026-10-18 09:12 Leo Okonkwo exportou a configuração da VPN do jump host JUMP-1 sob o ticket ENG-440; armazenada em evidence/ENG-440/vpn.txt."

**EX016.** Pré-engajamento, análise de vulnerabilidades, exploração, relatório.

**EX017.** É descoberta até que alguém a confirme, registre evidências e explique o impacto dentro das ROE.

**EX018.** Ele pode bloquear contas de associados ou da equipe e interromper o serviço; está fora da lista de métodos permitidos.

**EX019.** Demonstrar o efeito de segurança com a menor ação necessária e parar — sem acessar sistemas ou dados adicionais.

**EX020.** Permitido em "testes web autenticados" contra o sistema de homologação do internet banking, que está no escopo.

**EX021.** Mantém 3 de 5; descarta dir-listing e trace-method.

**EX022.** open-redirect (0.9) e cookie-flag (0.85); outdated-banner (0.7) é descartado.

**EX023.** Um scanner relata listagem de diretório, mas o servidor de homologação devolve uma página de login para esse caminho quando verificado com uma conta autorizada.

**EX024.** Uma falha de controle de acesso em uma página de transferência que nenhum scanner verifica, porque exige uma sessão válida de associado e etapas de negócio.

**EX025.** "OWASP ZAP 2.15, perfil de varredura de API 'HCU-staging-auth', executado em 2026-10-18 por Leo Okonkwo."

**EX026.** Identificador do engajamento, sistemas no escopo, janela de horário e um contato acessível do testador.

**EX027.** "09:12 staging.examplebank.test — verificação de expiração de sessão do WSTG — cookie persistiu após o logout — evidência E14."

**EX028.** Confirmar que se trata do ENG-440, compartilhar a janela das ROE e o ticket e reduzir o ritmo ou pausar se o SOC pedir.

**EX029.** Pausar os testes desse nome, perguntar ao responsável de produto ou ao CISO e continuar só depois de uma decisão de escopo registrada.

**EX030.** Parar no horário, registrar a verificação inacabada e agendá-la apenas dentro de uma nova janela autorizada.

**EX031.** Colocar os destinos de redirecionamento em lista de permissões ou remover os redirecionamentos controlados pelo usuário.

**EX032.** Restringir as interfaces administrativas da VPN à rede do jump host e exigir MFA enquanto as senhas compartilhadas são substituídas por senhas únicas.

**EX033.** Depois que o responsável declara que a correção foi implantada e dentro da janela de reteste registrada no ticket.

**EX034.** Não. A verificação exige as evidências do reteste de Leo, não apenas um e-mail.

**EX035.** Não. O reteste fica nas constatações acordadas, a menos que uma extensão de escopo por escrito diga o contrário.

**EX036.** As ROE excluem o e-mail pessoal; um funcionário relatou ter reutilizado a senha da VPN no e-mail pessoal.

**EX037.** "Suposição (não confirmada): a senha também pode ser conhecida por outras pessoas se o e-mail pessoal tiver sido comprometido; ainda não há evidência nos logs da HCU."

**EX038.** O e-mail pessoal está fora da autorização da HCU e dos limites de privacidade; a HCU pode redefinir as próprias credenciais de VPN sem lê-lo.

**EX039.** Uma senha de VPN exposta fora da HCU poderia permitir que alguém alcançasse serviços da equipe; esse risco precisa de visibilidade imediata do CISO.

**EX040.** T1078 Valid Accounts.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v3.1 Specification Document. <https://www.first.org/cvss/v3.1/specification-document>
- MITRE ATT&CK, including T1078 Valid Accounts. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
