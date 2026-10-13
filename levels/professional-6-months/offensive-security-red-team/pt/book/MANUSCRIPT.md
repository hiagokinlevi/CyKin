# Segurança Ofensiva Autorizada e Red Team: Um Guia para o Profissional

- Idioma: português do Brasil (`pt`); curso profissional, seis meses; aproximadamente 360 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 12 já estão escritos em português, com os exercícios EX001–EX020 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 5–12 (EX021–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX020 (as de EX021–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). A Harborline Credit Union, Leo Okonkwo e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
