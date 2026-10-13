# Governança, Riscos e Compliance de Segurança: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 051, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–9 de 18 já estão escritos em português, com os exercícios EX001–EX036 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 10–18 (EX037–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de curso técnico que configuram, verificam e documentam os controles por trás do programa de GRC de uma pequena empresa.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios verificam exportações de configuração em JSON contra uma linha de base, contam logins com falha, conferem regras de firewall contra uma lista aprovada e verificam a validade de certificados, sempre sobre dados sintéticos. Qualquer teste acontece só em laboratórios virtuais isolados; as normas são citadas pela edição e parafraseadas, e nada aqui é auditoria, atestação ou aconselhamento jurídico reais. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de curso técnico ao longo de dezoito meses, em torno de uma loja de materiais de construção: serviços, redes, identidades e scripts, escopo e evidências, o modelo de GRC, logs, modos de falha, métodos, configuração, verificação, laboratórios, solução de problemas, automação, dependências de provedores, documentação e um projeto supervisionado. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Amina Yusuf** | Estudante de curso técnico | Inventada |
| **Sra. Clara Bell** | Instrutora | Inventada |
| **Dunmore Technical College** | Escola fictícia | Inventada |
| **Fenwick Building Supplies** | Varejista fictícia, 6 filiais, 180 funcionários, loja on-line | Inventada |

### Fontes principais

NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29) e seus recursos para pequenas empresas; PCI DSS v4.0; trust services criteria da AICPA (SOC 2). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) |

Capítulos 10–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-10), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Computação e arquitetura de serviços

### Objetivos de aprendizagem

Você vai (1) descrever os serviços que uma empresa de varejo opera; (2) identificar os componentes que sustentam cada serviço; (3) registrar os donos para a governança.

### 1.1 Os serviços da Fenwick

Amina Yusuf é aluna do curso técnico no fictício Dunmore Technical College. Sua instrutora, a Sra. Clara Bell, usa um único caso ao longo do curso: a fictícia Fenwick Building Supplies, uma loja de materiais de construção com seis filiais, cento e oitenta funcionários, uma loja on-line e maquininhas de cartão em todos os caixas. Amina lista os serviços da Fenwick: vendas nas filiais, a loja on-line, as entregas, os pedidos a fornecedores e a folha de pagamento. Cada serviço depende de computadores, software, redes e pessoas, e a governança precisa conhecer essas ligações para proteger o que importa. A folha de pagamento, por exemplo, não tem clientes olhando, mas uma falha nela afetaria os cento e oitenta funcionários de uma vez.

### 1.2 Componentes

Para cada serviço, Amina lista os componentes. As vendas nas filiais dependem dos computadores dos caixas, das maquininhas de cartão, do software de frente de caixa (PDV) e da rede da filial. A loja on-line depende de uma plataforma web hospedada, de um gateway de pagamento e do banco de dados de estoque. As entregas dependem de tablets e de um serviço de roteirização. Ela aprende que desenhar essas ligações mostra qual componente sozinho poderia parar vários serviços, como o banco de dados de estoque, de que a loja e as filiais precisam. A Sra. Bell pede que ela destaque o banco de estoque no diagrama, já que uma queda nele pararia a loja on-line e todos os caixas das filiais.

### 1.3 Donos

Amina registra um dono para cada serviço e componente. O diretor de vendas é dono das vendas nas filiais; a gerente de e-commerce, da loja on-line; a equipe de técnicos de TI, dos caixas, das redes e do banco de dados de estoque. Dois componentes, o serviço de roteirização e o Wi-Fi das filiais, não têm dono claro. Ela aprende que os componentes sem dono costumam ser onde os problemas passam despercebidos, então atribuir donos é uma das primeiras e mais simples tarefas de governança. Ela inclui o serviço de roteirização e o Wi-Fi das filiais na pauta do líder de TI, para que os donos sejam acordados.

### Exemplo resolvido

Amina mapeia cinco serviços da Fenwick para seus componentes, identifica o banco de dados de estoque como compartilhado e encontra dois componentes sem dono.

> **Caso sintético.** O Dunmore, a Fenwick e todos os detalhes são sintéticos.

### Erros e limites

Os mapas omitem ferramentas informais. Os donos podem não aceitar a responsabilidade.

### Exercícios

- **EX001 — Componente compartilhado.** Que componente sustenta tanto a loja on-line quanto as filiais? *Rubrica:* 3 = o banco de dados de estoque;; 2 = banco de estoque;; 1 = nada;; 0 = nenhuma.
- **EX002 — Itens sem dono.** Que dois componentes não tinham dono? *Rubrica:* 3 = o serviço de roteirização e o Wi-Fi das filiais;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX003 — Por que donos.** Por que atribuir donos cedo? *Rubrica:* 3 = componentes sem dono são onde os problemas passam despercebidos;; 2 = visibilidade;; 1 = nada;; 0 = nenhuma.
- **EX004 — Lista de serviços.** Cite três serviços da Fenwick. *Rubrica:* 3 = vendas nas filiais, loja on-line, entregas;; 2 = serviços;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) descrever o desenho de rede de uma filial; (2) identificar os requisitos de rede para pagamentos com cartão; (3) documentar as mudanças de rede.

### 2.1 As redes das filiais

Cada filial da Fenwick tem uma rede para os caixas e as maquininhas de cartão, os computadores do escritório e um Wi-Fi de visitantes para os clientes profissionais. Amina aprende que essas redes devem ser separadas, para que um problema numa não se espalhe facilmente para outra. Ela verifica duas filiais: uma tem segmentos separados; a outra liga tudo a um único switch. Ela registra a diferença e aprende que filiais construídas em épocas diferentes costumam variar, o que a governança precisa encontrar e corrigir. A filial com um único switch deixa um aparelho de visitante comprometido alcançar os caixas, por isso ela a registra como a prioridade mais alta das duas.

### 2.2 Requisitos de pagamento com cartão

As maquininhas de cartão e o software dos caixas lidam com dados de cartões de pagamento, o que traz os requisitos do PCI DSS v4.0. Amina aprende que manter os sistemas de pagamento num segmento próprio, permitindo só as conexões necessárias, reduz o número de sistemas no escopo. Ela lista as conexões de que o segmento de pagamento precisa: com o gateway de pagamento, para a autorização, e com a gestão de TI, para as atualizações. Todo o resto deve ser bloqueado, e a própria lista vira evidência para as avaliações. Uma conexão dos computadores do escritório com o segmento de pagamento, por exemplo, traria também esses computadores para o escopo do PCI DSS.

### 2.3 Documentar as mudanças

Quando um técnico de filial acrescenta um aparelho ou uma regra, a mudança deve ser registrada: o quê, por quê, quem aprovou e quando. Amina descobre que as mudanças nas filiais muitas vezes são feitas por telefone, sem registro. Ela redige um formulário simples de mudança e explica que, sem registros, ninguém consegue dizer se a rede ainda corresponde ao seu desenho. Aprende que a documentação das mudanças é um controle básico, que apoia tanto a segurança quanto a solução de problemas. Um formulário com campos para o quê, o porquê, o aprovador e a data toma do técnico só um minuto durante a própria ligação.

### Exemplo resolvido

Amina compara as redes de duas filiais, lista as conexões de pagamento necessárias e redige um formulário de registro de mudanças.

> **Caso sintético.** As redes das filiais são sintéticas; o PCI DSS v4.0 é real.

### Erros e limites

Os diagramas se desatualizam. Os formulários de mudança são pulados nas emergências.

### Exercícios

- **EX005 — Filial sem segmentação.** Que problema tinha a segunda filial? *Rubrica:* 3 = tudo num único switch, sem segmentos;; 2 = rede plana;; 1 = nada;; 0 = nenhuma.
- **EX006 — Conexões de pagamento.** De que conexões o segmento de pagamento precisa? *Rubrica:* 3 = gateway de pagamento e gestão de TI;; 2 = duas;; 1 = internet;; 0 = nenhuma.
- **EX007 — Registro de mudança.** O que um registro de mudança deve capturar? *Rubrica:* 3 = o quê, por quê, quem aprovou e quando;; 2 = quatro;; 1 = nada;; 0 = nenhuma.
- **EX008 — Redução de escopo.** Como a segmentação ajuda no PCI DSS? *Rubrica:* 3 = reduz os sistemas no escopo;; 2 = escopo;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem

Você vai (1) gerir as contas de usuários nos sistemas da empresa; (2) aplicar o menor privilégio nos computadores; (3) controlar o acesso de administrador.

### 3.1 Contas de usuários

Amina aprende como a Fenwick cria contas para os funcionários nos computadores do escritório, nos caixas e nos serviços em nuvem. Cada pessoa deve ter a própria conta, para que as ações possam ser rastreadas. Nos caixas, a equipe compartilha um login, o que torna impossível saber quem fez um estorno. Ela recomenda logins individuais nos caixas, com acesso rápido por cartão. Aprende que as contas individuais são a base da responsabilização, e que as contas compartilhadas costumam existir porque as individuais eram incômodas. Logins individuais também permitiriam ao gerente da filial ver que funcionário fez cada estorno quando o fechamento do caixa não bate.

### 3.2 Menor privilégio

Os computadores do escritório dão a todos os usuários direitos de administrador local, para que possam instalar software. Amina explica que isso permite que um malware se instale com controle total. Ela propõe retirar os direitos de administrador local e criar um processo de solicitação de software. Testa a mudança primeiro em três computadores e descobre que um programa de contabilidade precisa de um ajuste de configuração. Aprende que o menor privilégio deve ser introduzido com cuidado e com testes, para que o trabalho continue sem tropeços. O piloto em três computadores encontrou o problema do programa de contabilidade antes que ele parasse um escritório inteiro.

### 3.3 Acesso de administrador

Os técnicos de TI usam contas de administrador para a manutenção. Amina recomenda contas de administrador separadas, usadas só para tarefas administrativas, com autenticação multifator e registro em log. Ela observa que, se a conta do dia a dia de um técnico for comprometida, os atacantes não devem ganhar direitos de administrador automaticamente. Aprende que controlar o acesso de administrador é uma das medidas de segurança mais eficazes, porque a maioria dos ataques graves depende de obter esses direitos. Registrar as sessões administrativas também dá ao líder de TI um histórico para conferir quando uma configuração muda de forma inesperada, e assim cada ação administrativa tem um nome.

### Exemplo resolvido

Amina substitui os logins compartilhados dos caixas, retira os direitos de administrador local após testes e separa as contas de administrador, com MFA.

> **Caso sintético.** As contas e os sistemas são sintéticos.

### Erros e limites

Retirar direitos pode quebrar softwares. O acesso por cartão exige hardware.

### Exercícios

- **EX009 — Problema do caixa compartilhado.** Por que um login compartilhado no caixa é um problema? *Rubrica:* 3 = não dá para rastrear quem fez um estorno;; 2 = responsabilização;; 1 = nada;; 0 = nenhuma.
- **EX010 — Risco dos direitos de administrador.** Por que retirar os direitos de administrador local? *Rubrica:* 3 = um malware poderia se instalar com controle total;; 2 = malware;; 1 = nada;; 0 = nenhuma.
- **EX011 — Administrador separado.** Por que usar contas de administrador separadas? *Rubrica:* 3 = o comprometimento de uma conta do dia a dia não deve dar direitos de administrador;; 2 = separação;; 1 = nada;; 0 = nenhuma.
- **EX012 — Testar primeiro.** Por que testar a retirada dos direitos primeiro em três computadores? *Rubrica:* 3 = para achar softwares que quebram;; 2 = piloto;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem

Você vai (1) ler formatos de dados estruturados, como JSON; (2) verificar configurações contra uma linha de base com um script; (3) relatar os desvios com clareza.

### 4.1 Formatos de dados

Amina aprende que os sistemas exportam dados de configuração e de status em formatos como CSV e JSON. O JSON representa os registros como campos nomeados, o que facilita lê-los em Python com o módulo json da biblioteca padrão. A ferramenta de gerenciamento de dispositivos da Fenwick exporta as configurações dos notebooks em JSON. Ela aprende que entender os formatos de dados permite aos técnicos verificar muitos aparelhos depressa, em vez de clicar em cada um, o que economiza tempo e reduz erros. No laboratório a seguir, a exportação em JSON permite que um script curto verifique os quatro notebooks contra a linha de base de uma só vez.

### 4.2 Verificação da linha de base

A linha de base da Fenwick exige criptografia de disco, bloqueio de tela em até dez minutos, atualizações automáticas e nenhum direito de administrador local. O laboratório verifica quatro notebooks. O FW-LT01 atende à linha de base. O FW-LT02 não tem criptografia de disco. O FW-LT03 tem bloqueio de tela de trinta minutos e direitos de administrador local. O FW-LT04 está com as atualizações automáticas desligadas. Um bloqueio de tela mais curto, como cinco minutos, é aceito, porque é mais rigoroso que a linha de base. A Sra. Bell pergunta à turma por que o FW-LT03 falha duas vezes, e Amina aponta o bloqueio de trinta minutos e os direitos de administrador local.

### Laboratório — Verificar as configurações dos notebooks contra uma linha de base

```python
"""Check laptop configuration exports (JSON) against a baseline (synthetic Fenwick data)."""
import json
baseline = {"disk_encryption": True, "screen_lock_minutes": 10, "auto_update": True, "local_admin": False}
export = json.loads("""[
 {"host": "FW-LT01", "disk_encryption": true, "screen_lock_minutes": 10, "auto_update": true, "local_admin": false},
 {"host": "FW-LT02", "disk_encryption": false, "screen_lock_minutes": 10, "auto_update": true, "local_admin": false},
 {"host": "FW-LT03", "disk_encryption": true, "screen_lock_minutes": 30, "auto_update": true, "local_admin": true},
 {"host": "FW-LT04", "disk_encryption": true, "screen_lock_minutes": 5, "auto_update": false, "local_admin": false}]""")
for h in export:
    bad = []
    for k, v in baseline.items():
        if k == "screen_lock_minutes":
            if h[k] > v: bad.append(f"{k}={h[k]}")
        elif h[k] != v: bad.append(f"{k}={h[k]}")
    print(h["host"], "OK" if not bad else "DEVIATION " + ", ".join(bad))
```

Execute com `python3 lab_config.py`. Saída verificada:

```text
FW-LT01 OK
FW-LT02 DEVIATION disk_encryption=False
FW-LT03 DEVIATION screen_lock_minutes=30, local_admin=True
FW-LT04 DEVIATION auto_update=False
```

### 4.3 Relatar os desvios

Amina relata cada desvio com o nome do notebook e a configuração que falhou, e depois pergunta aos donos o porquê. O FW-LT02 foi configurado antes de a criptografia virar padrão. O FW-LT03 pertence a um gerente que pediu direitos de administrador meses atrás. O FW-LT04 teve as atualizações pausadas durante um problema de software, e elas nunca foram retomadas. Ela aprende que cada desvio tem uma história, e que registrar a causa ajuda a evitar que o mesmo desvio se repita em outros aparelhos. As atualizações pausadas do FW-LT04, por exemplo, sugerem acrescentar uma data de revisão sempre que as atualizações forem pausadas por um problema de software.

### Exemplo resolvido

Amina lê uma exportação em JSON, encontra três de quatro notebooks fora da linha de base e registra a causa de cada desvio.

> **Caso sintético.** Os dados dos notebooks são sintéticos.

### Erros e limites

As exportações podem estar desatualizadas. As linhas de base precisam de revisão.

### Exercícios

- **EX013 — Vantagem do JSON.** Por que as exportações em JSON são úteis nas verificações? *Rubrica:* 3 = os campos nomeados são fáceis de ler em scripts;; 2 = estrutura;; 1 = nada;; 0 = nenhuma.
- **EX014 — Notebook conforme.** Que notebook atendeu à linha de base? *Rubrica:* 3 = FW-LT01;; 2 = LT01;; 1 = LT03;; 0 = nenhuma.
- **EX015 — Dois desvios.** Que notebook teve dois desvios? *Rubrica:* 3 = FW-LT03, bloqueio de 30 minutos e administrador local;; 2 = LT03;; 1 = nada;; 0 = nenhuma.
- **EX016 — Configuração mais rigorosa.** Por que o bloqueio de cinco minutos do FW-LT04 é aceitável? *Rubrica:* 3 = é mais rigoroso que a linha de base de dez minutos;; 2 = mais rigoroso;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Escopo e evidências de segurança

### Objetivos de aprendizagem

Você vai (1) definir o escopo de uma tarefa de segurança; (2) coletar evidências da forma correta; (3) respeitar os limites da autorização.

### 5.1 Escopo

Antes de qualquer trabalho técnico de segurança, Amina aprende a acordar o escopo por escrito: que sistemas, que atividades e que horários são permitidos. No estágio na Fenwick, o escopo permite ler exportações de configuração, revisar logs e verificar regras de firewall, mas não testar vulnerabilidades em sistemas em produção. A Sra. Bell insiste que trabalhar fora do escopo, mesmo com boas intenções, pode violar regras ou leis e abalar a confiança. O escopo escrito também permite a Amina responder depressa quando alguém na Fenwick lhe pede para testar algo que não está na lista.

### 5.2 Evidências

Amina aprende a coletar evidências: registrar o que foi verificado, quando, por quem e como, e guardar a saída original, como um arquivo exportado ou uma captura de tela. Ela nomeia os arquivos de forma consistente e os guarda numa pasta onde não podem ser alterados depois da coleta. Aprende que a evidência deve permitir que outra pessoa veja exatamente o que ela viu, o que importa nas auditorias e para corrigir problemas depois. Uma exportação mantida sem alteração numa pasta somente leitura pode ser comparada mais tarde com uma exportação nova, para ver o que mudou.

### 5.3 Limites da autorização

Durante o trabalho, Amina nota um servidor que parece permitir área de trabalho remota a partir da internet. Testá-lo estaria fora do escopo. Ela o relata ao líder de TI com a evidência que já tem: a regra de firewall que mostra a conexão. O líder de TI investiga e a fecha. Ela aprende que a resposta correta diante de algo fora do escopo é relatar, e não investigar por conta própria sem permissão. A regra de firewall que ela já tinha em mãos foi evidência suficiente para o líder de TI agir sem que ela sondasse o servidor.

### Exemplo resolvido

Amina trabalha sob um escopo escrito, coleta evidências rastreáveis e relata uma preocupação fora do escopo, em vez de testá-la.

> **Caso sintético.** O escopo e os achados são sintéticos.

### Erros e limites

Os escopos podem ser pouco claros. As pastas de evidências precisam de controle de acesso.

### Exercícios

- **EX017 — Atividade excluída.** Que atividade estava fora do escopo de Amina? *Rubrica:* 3 = teste de vulnerabilidades em sistemas em produção;; 2 = teste;; 1 = nada;; 0 = nenhuma.
- **EX018 — Registro de evidência.** O que um registro de evidência deve incluir? *Rubrica:* 3 = o quê, quando, quem, como e a saída original;; 2 = registro;; 1 = nada;; 0 = nenhuma.
- **EX019 — Resposta fora do escopo.** O que fazer ao notar algo fora do escopo? *Rubrica:* 3 = relatar com a evidência já existente;; 2 = relatar;; 1 = testar;; 0 = nenhuma.
- **EX020 — Armazenamento inalterável.** Por que guardar as evidências onde não podem ser alteradas? *Rubrica:* 3 = para que outros confiem que mostram exatamente o que foi visto;; 2 = integridade;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Governança, riscos e compliance de segurança: modelo do sistema

### Objetivos de aprendizagem

Você vai (1) explicar como a GRC se encaixa no trabalho técnico; (2) modelar os papéis de governança da Fenwick; (3) ligar as tarefas técnicas às políticas e aos riscos.

### 6.1 A GRC e os técnicos

Amina aprende que a governança define regras e prioridades, a gestão de riscos decide o que mais importa e o compliance verifica se as obrigações são cumpridas. Os técnicos fazem tudo isso funcionar: configuram sistemas, coletam evidências e corrigem problemas. A Sra. Bell explica que entender a GRC ajuda os técnicos a ver por que as tarefas importam. Uma verificação da linha de base não é trabalho inútil; ela apoia uma política, reduz um risco e produz evidências que um avaliador pode pedir. Ela dá um exemplo: a verificação de criptografia reduz o risco de notebook perdido e responde a uma pergunta que o avaliador de pagamentos com cartão pode fazer.

### 6.2 Os papéis na Fenwick

O diretor financeiro da Fenwick responde pela segurança. Um líder de TI gerencia uma equipe de três técnicos. Os gerentes das filiais são donos de tarefas locais, como confirmar os desligamentos da equipe. Um avaliador externo verifica todo ano a conformidade dos pagamentos com cartão. Amina desenha esses papéis e o fluxo de informação entre eles, observando que os técnicos relatam os problemas ao líder de TI, que relata os riscos ao diretor financeiro. O desenho também mostra que o avaliador externo depende de evidências produzidas pelos técnicos, como as listas de regras de firewall.

### 6.3 Ligar as tarefas

Amina monta uma tabela que liga as tarefas técnicas às políticas, aos riscos e às obrigações. A criptografia dos notebooks se liga à política de proteção de dados e ao risco de aparelho perdido. As revisões das regras de firewall se ligam à política de rede e às obrigações de pagamento com cartão. As revisões de logs se ligam à política de monitoramento e ao risco de uso indevido de contas. Ela aprende que essa tabela ajuda os técnicos a priorizar quando o tempo é curto e explica aos gestores por que o trabalho técnico merece recursos. Com pouco tempo, por exemplo, a revisão do firewall passa à frente de uma revisão de logs, porque também carrega obrigações de pagamento com cartão.

### Exemplo resolvido

Amina explica a ligação da GRC com o trabalho técnico, modela os papéis da Fenwick e mapeia as tarefas técnicas para políticas, riscos e obrigações.

> **Caso sintético.** Os papéis da Fenwick são sintéticos.

### Erros e limites

As tabelas simplificam ligações complexas. Os papéis mudam.

### Exercícios

- **EX021 — Finalidade da linha de base.** Por que uma verificação da linha de base não é trabalho inútil? *Rubrica:* 3 = apoia uma política, reduz um risco e produz evidências;; 2 = finalidade;; 1 = nada;; 0 = nenhuma.
- **EX022 — Responsável.** Quem responde pela segurança na Fenwick? *Rubrica:* 3 = o diretor financeiro;; 2 = diretor financeiro;; 1 = líder de TI;; 0 = nenhuma.
- **EX023 — Ligações do firewall.** Que política e que obrigação as revisões de firewall apoiam? *Rubrica:* 3 = a política de rede e as obrigações de pagamento com cartão;; 2 = ligações;; 1 = nada;; 0 = nenhuma.
- **EX024 — Uso da tabela.** Como a tabela de tarefas ajuda os técnicos? *Rubrica:* 3 = a priorizar quando o tempo é curto;; 2 = prioridades;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Governança, riscos e compliance de segurança: dados e telemetria

### Objetivos de aprendizagem

Você vai (1) usar os logs como dados de governança; (2) contar e sinalizar eventos incomuns; (3) decidir o que fazer com os alertas.

### 7.1 Logs como dados

Os sistemas registram eventos como logins, mudanças e erros. Amina aprende que os logs são dados de governança: mostram se os controles funcionam e se algo incomum aconteceu. Os serviços em nuvem da Fenwick produzem logs de login com horário, resultado e conta. Ela aprende a lê-los com um script, e que guardar os logs por um período definido costuma ser exigido pela política e pelas regras de cartões de pagamento, então a retenção precisa ser planejada. A Sra. Bell observa que um prazo de retenção escolhido sem conferir as regras de cartão pode apagar logs que um avaliador depois venha a pedir.

### 7.2 Contar as falhas

O laboratório lê doze linhas de log de login e conta as falhas por conta. A conta admin tem sete falhas em poucos minutos e é sinalizada, porque passa de cinco. A j.park tem duas falhas seguidas de um sucesso, provavelmente uma senha digitada errado. A s.ali tem uma falha. No total, três contas tiveram falhas. Amina observa que falhas repetidas numa conta de administrador podem indicar alguém tentando adivinhar a senha. O sucesso da j.park logo depois de duas falhas combina muito mais com um erro de digitação do que com um ataque a essa conta.

### Laboratório — Contar os logins com falha por conta

```python
"""Count failed sign-ins per account from synthetic log lines; flag accounts above 5."""
from collections import Counter
log = """2026-09-14T08:01 FAIL j.park
2026-09-14T08:02 FAIL j.park
2026-09-14T08:02 OK j.park
2026-09-14T09:10 FAIL admin
2026-09-14T09:10 FAIL admin
2026-09-14T09:11 FAIL admin
2026-09-14T09:11 FAIL admin
2026-09-14T09:12 FAIL admin
2026-09-14T09:12 FAIL admin
2026-09-14T09:13 FAIL admin
2026-09-14T10:30 FAIL s.ali
2026-09-14T10:31 OK s.ali"""
c = Counter(l.split()[2] for l in log.splitlines() if " FAIL " in l)
for a, n in c.most_common(): print(f"{a}: {n} failures{'  ALERT' if n > 5 else ''}")
print(f"lines {len(log.splitlines())}; accounts with failures {len(c)}")
```

Execute com `python3 lab_logs.py`. Saída verificada:

```text
admin: 7 failures  ALERT
j.park: 2 failures
s.ali: 1 failures
lines 12; accounts with failures 3
```

### 7.3 Agir sobre os alertas

Amina relata o alerta da conta admin ao líder de TI. Eles verificam e descobrem que as falhas vieram de um endereço desconhecido na internet. A conta já tinha autenticação multifator, então as tentativas falharam. O líder de TI bloqueia o endereço e renomeia a conta admin genérica. Amina aprende que os alertas precisam de um procedimento de resposta e que o contexto, como o endereço de origem e se os outros controles seguraram, determina a gravidade de um alerta. Renomear a conta admin genérica também a torna um alvo menos óbvio para as mesmas tentativas de adivinhação.

### Exemplo resolvido

Amina conta as falhas de login, sinaliza sete na conta admin e apoia uma resposta que bloqueia a origem e renomeia a conta.

> **Caso sintético.** As linhas de log são sintéticas.

### Erros e limites

Limiares simples deixam passar ataques lentos. Os logs podem estar incompletos.

### Exercícios

- **EX025 — Retenção de logs.** Por que a retenção de logs precisa ser planejada? *Rubrica:* 3 = a política e as regras de cartão costumam exigi-la;; 2 = requisitos;; 1 = nada;; 0 = nenhuma.
- **EX026 — Conta sinalizada.** Que conta foi sinalizada, e por quê? *Rubrica:* 3 = admin, 7 falhas acima de 5;; 2 = admin;; 1 = j.park;; 0 = nenhuma.
- **EX027 — Leitura da j.park.** Como Amina interpretou as falhas da j.park? *Rubrica:* 3 = provável senha digitada errado, seguida de sucesso;; 2 = erro de digitação;; 1 = nada;; 0 = nenhuma.
- **EX028 — Ações de resposta.** Que ações se seguiram ao alerta? *Rubrica:* 3 = bloquear o endereço e renomear a conta admin;; 2 = duas;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Governança, riscos e compliance de segurança: modos de falha

### Objetivos de aprendizagem

Você vai (1) identificar como os controles técnicos falham; (2) planejar a detecção de cada falha; (3) registrar os modos de falha no registro de riscos.

### 8.1 Como os controles falham

Amina aprende que os controles podem falhar de muitas formas. Os backups podem rodar e deixar arquivos de fora. As atualizações podem ser pausadas e esquecidas. Regras de firewall podem ser acrescentadas e nunca removidas. Contas podem continuar ativas depois que as pessoas saem. Certificados podem expirar. Ela escreve cada caso como um modo de falha: o que dá errado, como isso apareceria e qual seria o impacto. Aprende que pensar na falha com antecedência torna os controles mais confiáveis. Para os backups, o modo de falha diz: a rotina roda, deixa arquivos de fora e a lacuna só aparece numa restauração.

### 8.2 Detectar a falha

Para cada modo de falha, Amina pergunta como a Fenwick perceberia. Os arquivos que ficaram de fora só apareceriam nos testes de restauração. As atualizações pausadas apareceriam nos relatórios de conformidade. As regras de firewall obsoletas apareceriam nas revisões de regras. As contas ativas de desligados apareceriam na conciliação. Os certificados perto de expirar apareceriam nas verificações de validade. Ela aprende que algumas falhas ficam silenciosas até algo quebrar, então verificações regulares precisam ser agendadas para encontrá-las antes que clientes ou atacantes o façam. Os arquivos que ficaram fora do backup, por exemplo, só aparecem num teste de restauração, e por isso esses testes entram depois no seu cronograma.

### 8.3 Entradas no registro

Amina registra os principais modos de falha no registro de riscos da Fenwick, com donos e verificações de detecção. Por exemplo, o modo de falha da expiração de certificados tem como dono o líder de TI, com uma verificação mensal de validade. Ela aprende que registrar os modos de falha os torna parte da governança, de modo que as verificações sejam agendadas e revisadas, em vez de depender da memória de alguém. Uma verificação mensal com dono transforma o modo de falha dos certificados numa tarefa recorrente, e não numa surpresa. Ligar cada modo de falha a uma verificação nomeada também diz ao avaliador que evidência pedir.

### Exemplo resolvido

Amina lista cinco modos de falha de controles, planeja a detecção de cada um e os registra no registro de riscos, com donos.

> **Caso sintético.** Os modos de falha são sintéticos.

### Erros e limites

As listas deixam escapar falhas novas. As verificações também podem falhar.

### Exercícios

- **EX029 — Falha de backup.** Como os arquivos que ficaram fora do backup seriam detectados? *Rubrica:* 3 = por testes de restauração;; 2 = restauração;; 1 = nada;; 0 = nenhuma.
- **EX030 — Falhas silenciosas.** Por que as verificações precisam ser agendadas? *Rubrica:* 3 = algumas falhas ficam silenciosas até algo quebrar;; 2 = silenciosas;; 1 = nada;; 0 = nenhuma.
- **EX031 — Dono dos certificados.** Quem é dono do modo de falha da expiração de certificados? *Rubrica:* 3 = o líder de TI;; 2 = líder de TI;; 1 = nada;; 0 = nenhuma.
- **EX032 — Partes do modo de falha.** Que três coisas cada modo de falha descreve? *Rubrica:* 3 = o que dá errado, como aparece, impacto;; 2 = três;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Governança, riscos e compliance de segurança: ferramentas e métodos

### Objetivos de aprendizagem

Você vai (1) usar um método simples de riscos; (2) aplicar um checklist de controles; (3) escolher ferramentas adequadas a uma equipe pequena.

### 9.1 Método de riscos

A Fenwick usa um método simples: listar os riscos, dar notas de um a cinco para probabilidade e impacto, multiplicá-las para obter uma pontuação e tratar primeiro os mais altos. Amina ajuda a pontuar os riscos da loja on-line. Ela aprende que o método é rápido, mas tem limites: riscos muito diferentes podem ter a mesma pontuação, e um evento raro mas grave pode parecer baixo. Ela anota esses limites e sugere discutir em mais detalhe os riscos do topo, em vez de depender só das pontuações. Uma chance em vinte de violação no gateway de pagamento, por exemplo, pode pontuar menos que lentidões frequentes da loja, apesar de um impacto muito pior.

### 9.2 Checklists

Amina usa um checklist de controles baseado nos recursos para pequenas empresas do NIST CSF 2.0 para revisar o básico da Fenwick: inventário, contas, atualizações, backups, logs e resposta a incidentes. Cada item é marcado como implantado, parcialmente implantado ou ausente, com evidência. O checklist revela que falta um plano escrito de resposta a incidentes. Ela aprende que os checklists ajudam as equipes pequenas a cobrir o essencial sem precisar de conhecimento profundo em todas as áreas. O plano de resposta a incidentes ausente vira uma entrada do registro com dono, e não uma anotação esquecida no checklist.

### 9.3 Escolher ferramentas

A pequena equipe de TI da Fenwick não consegue operar um software de governança complexo. Amina recomenda usar as ferramentas que eles já têm: o sistema de chamados para as tarefas, planilhas com validação para o registro e scripts curtos para as verificações. Ela aprende que a melhor ferramenta é aquela que a equipe vai de fato usar e manter, e que acrescentar software sem gente para operá-lo muitas vezes aumenta o risco em vez de reduzi-lo. A Sra. Bell observa que uma planilha com validação, mantida em dia por três técnicos, entrega à Fenwick mais do que uma plataforma de governança sem uso.

### Exemplo resolvido

Amina pontua os riscos da loja com um método simples, revisa o básico com um checklist baseado no CSF e recomenda as ferramentas já existentes.

> **Caso sintético.** As notas e os resultados do checklist são sintéticos; os recursos do CSF 2.0 são reais.

### Erros e limites

As pontuações escondem a gravidade. Os checklists deixam o contexto de fora.

### Exercícios

- **EX033 — Limite do método.** Qual é um limite do método de multiplicar notas? *Rubrica:* 3 = eventos raros e graves podem parecer baixos;; 2 = gravidade;; 1 = nada;; 0 = nenhuma.
- **EX034 — Item ausente.** O que o checklist revelou como ausente? *Rubrica:* 3 = um plano escrito de resposta a incidentes;; 2 = plano de incidentes;; 1 = nada;; 0 = nenhuma.
- **EX035 — Escolha de ferramentas.** Que ferramentas Amina recomendou? *Rubrica:* 3 = chamados, planilhas com validação e scripts curtos;; 2 = ferramentas existentes;; 1 = nada;; 0 = nenhuma.
- **EX036 — Marcação do checklist.** Como cada item do checklist é marcado? *Rubrica:* 3 = implantado, parcialmente implantado ou ausente, com evidência;; 2 = três estados;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX036 (as de EX037–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). Amina Yusuf, a Sra. Clara Bell, o Dunmore Technical College, a Fenwick Building Supplies e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O banco de dados de estoque.

**EX002.** O serviço de roteirização e o Wi-Fi das filiais.

**EX003.** Porque os problemas em componentes sem dono muitas vezes passam despercebidos.

**EX004.** Por exemplo, vendas nas filiais, a loja on-line e as entregas (também os pedidos a fornecedores e a folha de pagamento).

**EX005.** Tudo estava ligado a um único switch, sem separação.

**EX006.** As conexões com o gateway de pagamento e com a gestão de TI, para as atualizações.

**EX007.** O que mudou, por quê, quem aprovou e quando.

**EX008.** Reduz o número de sistemas no escopo dos requisitos de dados de cartão.

**EX009.** Porque ninguém consegue dizer quem fez um estorno ou uma venda.

**EX010.** Porque um malware poderia se instalar com controle total.

**EX011.** Para que o comprometimento de uma conta do dia a dia não dê direitos de administrador aos atacantes.

**EX012.** Para encontrar problemas, como um programa de contabilidade que precisa de ajuste, antes da implantação geral.

**EX013.** Porque os campos nomeados tornam os registros fáceis de ler e de verificar com scripts.

**EX014.** FW-LT01.

**EX015.** FW-LT03, com bloqueio de tela de 30 minutos e direitos de administrador local.

**EX016.** Porque um bloqueio de cinco minutos é mais rigoroso que o requisito de dez minutos.

**EX017.** Testar vulnerabilidades em sistemas em produção.

**EX018.** O que foi verificado, quando, por quem, como, e a saída original.

**EX019.** Relatar com a evidência que você já tem, sem investigar além disso.

**EX020.** Para que outros confiem que ela mostra exatamente o que foi observado.

**EX021.** Porque apoia uma política, reduz um risco e produz evidências.

**EX022.** O diretor financeiro.

**EX023.** A política de rede e as obrigações de pagamento com cartão.

**EX024.** Ajuda a priorizar quando o tempo é curto e a justificar os recursos.

**EX025.** Porque a política e as regras de cartões de pagamento costumam exigir que os logs sejam guardados por um período definido.

**EX026.** A conta admin, com sete falhas, acima do limiar de cinco.

**EX027.** Como uma provável senha digitada errado, já que veio um sucesso em seguida.

**EX028.** Bloquear o endereço de origem e renomear a conta admin genérica.

**EX029.** Por testes de restauração.

**EX030.** Porque algumas falhas ficam silenciosas até algo quebrar.

**EX031.** O líder de TI, com uma verificação mensal de validade.

**EX032.** O que dá errado, como isso apareceria e qual seria o impacto.

**EX033.** Eventos raros mas graves podem parecer baixos, e riscos diferentes podem empatar.

**EX034.** Um plano escrito de resposta a incidentes.

**EX035.** O sistema de chamados, planilhas com validação e scripts curtos.

**EX036.** Como implantado, parcialmente implantado ou ausente, com evidência.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO 31000:2018 e da ABNT NBR ISO/IEC 27001:2022, citadas nesta edição como referências brasileiras e conferidas em suas fontes oficiais; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Associação Brasileira de Normas Técnicas. (2018). *ABNT NBR ISO 31000:2018 — Gestão de riscos — Diretrizes*. ABNT. <https://www.abntcatalogo.com.br/>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
