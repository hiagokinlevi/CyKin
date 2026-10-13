# Segurança de TO, IoT e Sistemas Ciberfísicos: Guia do Profissional

- Idioma: português do Brasil (`pt`); curso profissional, seis meses; aproximadamente 360 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, e suas saídas vêm de execuções reais. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais de segurança em início de carreira que entram numa organização, aqui um hospital, cujos sistemas prediais e de instalações são ciberfísicos.
- Relação com os livros vizinhos: o [livro do curso rápido](../../../../rapid-1-month/ot-iot-security/en/book/MANUSCRIPT.md) é uma introdução em quatro capítulos; o [livro técnico](../../../../technical-18-months/ot-iot-security/en/book/MANUSCRIPT.md) aprofunda os procedimentos de chão de fábrica. **Este livro é um guia compacto para profissionais, construído sobre sistemas prediais.**
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação credenciada. Não concede autorização para acessar instalações reais. Todas as instalações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–3 explicam os sistemas prediais hospitalares, a segurança do paciente e as redes prediais; os capítulos 4–10 cobrem inventário, contas, exposição à internet, acesso de empreiteiros, segmentação, monitoramento e alertas; o capítulo 11 cobre a resposta a incidentes e o 12, o relatório de risco final. Todo capítulo tem objetivos, texto didático, um exemplo resolvido, um caso sintético identificado, erros e limites, cinco exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios dos Capítulos 4, 6 e 9 leem apenas dados locais (`python3 file.py`).

### Caso sintético contínuo

| Elemento | Papel | Limite |
|---|---|---|
| **Millbrook Hospital Building Systems** — unidades de tratamento de ar dos centros cirúrgicos AHU-OT1/2, CHILLER-1, alarme de gases medicinais MGAS-PANEL, LIFT-CTRL, controle de acesso DOOR-SRV, estação de trabalho BMS-WS | Hospital estudado ao longo do livro | Inventado |
| **Aisha Bello** | Analista de segurança júnior no Millbrook | Inventada |

### Fontes centrais

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [série ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Lista completa nas [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas prediais como sistemas ciberfísicos

### Objetivos de aprendizagem

Você vai (1) listar os sistemas prediais dos quais um hospital depende; (2) explicar como cada um se torna um sistema ciberfísico quando ligado em rede; e (3) descrever as consequências da sua falha para os pacientes.

### 1.1 O que faz funcionar um prédio hospitalar

Por trás das enfermarias ficam as unidades de tratamento de ar que mantêm os centros cirúrgicos com temperatura, umidade e pressão controladas; resfriadores (chillers) e caldeiras; painéis de alarme de gases medicinais que avisam quando a pressão do oxigênio cai; elevadores que levam pacientes entre andares; e o controle de acesso das portas de farmácias e maternidades. Um sistema de gerenciamento predial (BMS) liga muitos deles numa rede com uma estação de trabalho central.

A maioria desses sistemas é invisível para os pacientes e para muitos funcionários até falhar. No Millbrook, eles incluem as duas unidades de tratamento de ar dos centros cirúrgicos, um chiller, um painel de alarme de gases medicinais, o controlador dos elevadores e o servidor de controle de acesso, todos alcançados a partir de uma única estação de trabalho do BMS. Conhecer a lista é o primeiro passo para perguntar quem protege cada item.

### 1.2 Por que são ciberfísicos

Cada sistema lê sensores e aciona equipamentos no mundo físico por meio de controladores. Quando esses controladores são ligados em rede, uma mudança feita numa tela em qualquer ponto da rede pode mover um damper, parar uma bomba ou destrancar uma porta. O NIST SP 800-82r3 cobre explicitamente a automação predial dentro da tecnologia operacional exatamente por esse motivo.

No Millbrook, um valor de referência digitado na BMS-WS pode mudar o ar de um centro cirúrgico, e uma agenda no DOOR-SRV decide quais portas abrem. Nenhuma das mudanças exige que alguém esteja numa casa de máquinas. É isso que torna esses sistemas uma preocupação de segurança: quem alcança a tela alcança o equipamento por trás dela.

### 1.3 Consequência para os pacientes

Falhas de TI de escritório atrasam o trabalho. Falhas de sistemas prediais podem causar dano aos pacientes: um centro cirúrgico que perde a pressão positiva corre risco de infecção cirúrgica; um alarme de gás silenciado esconde uma queda real; um elevador parado atrasa uma transferência de emergência. O planejamento de segurança num hospital começa perguntando qual falha machucaria alguém, e com que rapidez.

Escreva a resposta para cada sistema numa frase que um clínico reconheceria, e anote por quanto tempo o hospital consegue se virar antes que o dano se torne provável. Um centro cirúrgico pode aguentar minutos antes de uma lista de cirurgias ser cancelada; uma enfermaria pode lidar com uma falha de porta por horas, usando chaves. Essas escalas de tempo decidem depois quais riscos vêm primeiro no planejamento e num incidente.

### 1.4 Quem é o dono deles

Os sistemas prediais muitas vezes pertencem às equipes de engenharia de manutenção ou de instalações, são mantidos por empreiteiros e ficam invisíveis para a equipe de segurança de TI do hospital. Fechar essa lacuna — combinar quem é responsável pela segurança de cada sistema — costuma ser a primeira vitória prática.

No Millbrook, a primeira reunião de Aisha é com o gerente de manutenção predial, e não com a equipe de TI, porque a manutenção opera o BMS e detém as relações com os empreiteiros. O resultado que ela quer é uma lista curta, com um responsável nomeado por sistema, aceita pelos dois lados. Sem ela, toda constatação posterior corre o risco de ser passada de uma equipe para outra sem que ninguém aja.

### Exemplo resolvido (Millbrook sintético)

Aisha Bello, recém-contratada como analista de segurança júnior no Millbrook Hospital, reúne-se com o gerente de manutenção predial e lista os sistemas num quadro branco, com uma consequência para cada. "AHU-OT1: o centro cirúrgico 1 perde pressão — cirurgia adiada ou risco de infecção." "MGAS-PANEL: alarme de pressão de oxigênio silencioso — a equipe da enfermaria não fica sabendo da falha no suprimento."

> **Caso sintético — Millbrook Hospital Building Systems.** O hospital, Aisha Bello e todos os números deste livro foram inventados para o ensino.

### Erros e limites

As consequências precisam ser confirmadas com as equipes clínicas e de manutenção; o palpite de um analista é apenas um ponto de partida.

### Exercícios

- **EX001 — Cinco sistemas.** Liste cinco sistemas prediais hospitalares e o que cada um controla. *Rubrica:* 3 = cinco sistemas, cada um com uma função correta; 2 = quatro; 1 = dois; 0 = nenhum.
- **EX002 — Tornar-se ciberfísico.** Explique em duas frases como a ligação em rede transforma uma unidade de tratamento de ar numa preocupação de segurança ciberfísica. *Rubrica:* 3 = controlador em rede permite que uma tela remota altere o equipamento físico; consequência nomeada; 2 = um ponto; 1 = vago; 0 = nenhum.
- **EX003 — Pressão do centro cirúrgico.** Por que a perda de pressão positiva num centro cirúrgico importa? *Rubrica:* 3 = entra ar não filtrado, risco de infecção cirúrgica, cirurgia adiada; 2 = um; 1 = conforto; 0 = nenhum.
- **EX004 — Alarme de gás silencioso.** Descreva o dano se os alarmes do MGAS-PANEL estiverem desabilitados durante uma queda real de pressão. *Rubrica:* 3 = equipe sem saber, pacientes em oxigênio em risco, resposta atrasada; 2 = parcial; 1 = "o barulho para"; 0 = nenhum.
- **EX005 — Lacuna de responsabilidade.** Por que combinar quem é dono da segurança dos sistemas prediais é uma vitória inicial? *Rubrica:* 3 = a lacuna entre manutenção/empreiteiros/TI deixa ninguém corrigindo ou monitorando; um responsável claro viabiliza cada passo seguinte; 2 = parcial; 1 = papelada; 0 = nenhum.

### Síntese

Os sistemas prediais hospitalares movem ar, gases, pessoas e portas; a falha deles pode ferir pacientes, então a sua segurança precisa de um dono.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Segurança do paciente, contingência e autoridade

### Objetivos de aprendizagem

Você vai (1) explicar por que a segurança clínica está acima da conveniência da segurança da informação; (2) descrever os arranjos de contingência hospitalares para os sistemas prediais; e (3) identificar quem pode autorizar mudanças em áreas clínicas.

### 2.1 Segurança clínica em primeiro lugar

Uma correção de segurança que desliga a ventilação de um centro cirúrgico durante uma cirurgia é pior do que o risco que corrige. Toda tarefa de segurança em áreas clínicas é planejada com as pessoas responsáveis pelos pacientes, e programada em função delas.

Na prática, isso significa perguntar ao gerente do centro cirúrgico quando as listas de cirurgias acontecem antes de agendar qualquer trabalho na AHU-OT1 ou na AHU-OT2, e escolher um horário em que nenhum paciente dependa do sistema. Um atraso de alguns dias para chegar a um horário seguro normalmente é aceitável. Uma mudança de segurança feita às pressas durante uma cirurgia não é.

### 2.2 A contingência já existe

Os hospitais se preparam para falhas prediais independentemente de ataques cibernéticos: oxigênio em cilindros quando o suprimento canalizado falha, refrigeração portátil, chaves manuais para as portas, procedimentos de resgate em elevadores. Esses também são o recurso alternativo quando um sistema em rede não é confiável. Conhecê-los permite à equipe de segurança sugerir isolar um sistema sem deixar os pacientes sem suporte.

Pergunte à manutenção quando cada recurso alternativo foi exercitado pela última vez e quem o acionaria à noite. Um suprimento por cilindros que ninguém verificou, ou chaves manuais que não podem ser encontradas, não é um recurso alternativo. Anotar esses arranjos ao lado de cada sistema no inventário permite à equipe de segurança propor o isolamento num incidente sabendo o que manterá os pacientes seguros enquanto isso.

### 2.3 Autoridade

Os gerentes de manutenção predial autorizam trabalho nos equipamentos prediais; os gerentes do centro cirúrgico decidem quando uma sala está disponível; a pessoa autorizada para gases medicinais controla os sistemas de gases; a segurança de TI aconselha. Os empreiteiros trabalham sob uma permissão de trabalho da manutenção. Os analistas nunca instruem um empreiteiro a alterar diretamente um sistema clínico.

Para Aisha, isso significa que toda solicitação passa pela pessoa com autoridade. Se ela encontra uma senha fraca num controlador, relata-a ao gerente de manutenção, que providencia para que o empreiteiro a troque sob uma permissão. Instruir o empreiteiro diretamente, mesmo com boa intenção, contorna as verificações que protegem os pacientes e não deixa registro de quem aprovou a mudança.

### 2.4 Permissões em hospitais

O trabalho em áreas clínicas muitas vezes precisa de aprovação do controle de infecção, além de uma permissão da manutenção: um técnico que abre um painel do forro num centro cirúrgico pode soltar poeira. Mesmo uma verificação não invasiva pode precisar de um horário agendado.

Pergunte cedo quais aprovações uma tarefa exige, porque combinar um horário para uma casa de máquinas de centro cirúrgico pode levar dias. A verificação de firmware de Aisha precisou de uma permissão da manutenção, da confirmação do gerente do centro cirúrgico e do acompanhamento de um empreiteiro. Anote cada aprovação no registro do trabalho e encerre a permissão quando o trabalho terminar, mesmo quando nada foi alterado.

### 2.5 Conversar com os clínicos

Explique o trabalho de segurança na linguagem do risco ao paciente e do tempo de sala cirúrgica. "Precisamos de uma hora no sábado para que ninguém consiga mudar o ar do centro cirúrgico de fora" obtém concordância mais rápido do que uma lista de protocolos.

Pergunte aos clínicos o que os preocuparia, como uma mudança de temperatura não planejada durante uma operação, e ligue o trabalho de segurança a essa preocupação. Mantenha as solicitações curtas e concretas: qual sala, qual hora, o que vai acontecer e como será verificado. Dê um retorno depois do trabalho, para que a próxima solicitação seja mais fácil de aprovar.

### Exemplo resolvido (Millbrook sintético)

Aisha quer ler as etiquetas de firmware dos controladores de tratamento de ar dos centros cirúrgicos na casa de máquinas da cobertura. O gerente de manutenção emite uma permissão para sábado, das 07:00 às 08:00, quando não há listas de cirurgias; o gerente do centro cirúrgico confirma; um empreiteiro a acompanha; nenhuma configuração é tocada. Ela fotografa as etiquetas, e a permissão é encerrada às 07:40.

> **Caso sintético — Millbrook.** A permissão e os horários são inventados.

### Erros e limites

Os cargos locais têm títulos diferentes; aprenda a lista do seu hospital. Os planos de contingência podem não ter sido testados; pergunte quando foram exercitados pela última vez.

### Exercícios

- **EX006 — Correção que causa dano.** Dê um exemplo de correção de segurança que poderia ferir pacientes se feita na hora errada. *Rubrica:* 3 = ação concreta (por exemplo, reiniciar o controlador de uma AHU) com consequência clínica; 2 = genérica; 1 = nenhuma clínica; 0 = nenhum.
- **EX007 — Associar contingências.** Associe cada contingência ao seu sistema: oxigênio em cilindros, chaves manuais, refrigeração portátil. *Rubrica:* 3 = suprimento de gás, controle de acesso, climatização/chillers; 2 = dois; 1 = um; 0 = nenhum.
- **EX008 — Quem autoriza trabalho em gases.** Quem controla o trabalho em sistemas de gases medicinais no Millbrook? *Rubrica:* 3 = a pessoa autorizada para gases medicinais, sob a manutenção; 2 = só a manutenção; 1 = TI; 0 = nenhum.
- **EX009 — Controle de infecção.** Por que uma verificação de etiqueta de firmware num centro cirúrgico pode precisar de aprovação do controle de infecção? *Rubrica:* 3 = abrir painéis/acessos pode soltar poeira ou violar a área limpa; 2 = vago; 1 = sem motivo; 0 = nenhum.
- **EX010 — Sugestão de isolamento.** Como conhecer os planos de contingência ajuda ao propor isolar o BMS durante um incidente? *Rubrica:* 3 = permite mostrar que os pacientes continuam atendidos por recursos manuais/alternativos, então o isolamento é aceitável; 2 = parcial; 1 = irrelevante; 0 = nenhum.

### Síntese

A segurança clínica define o momento; os planos de contingência tornam possíveis as ações de segurança; cargos nomeados as autorizam.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Redes e protocolos nos sistemas prediais

### Objetivos de aprendizagem

Você vai (1) descrever como os controladores do BMS se comunicam; (2) explicar por que os protocolos prediais muitas vezes não têm autenticação; e (3) identificar onde as redes prediais tocam a rede do hospital.

### 3.1 Camadas de campo e de supervisão

Sensores e atuadores ligam-se aos controladores de campo por fios. Os controladores conversam entre si e com o servidor do BMS por uma rede predial. Entre os protocolos comuns estão o BACnet, normalmente transportado sobre UDP na porta 47808 como BACnet/IP, e o Modbus/TCP, em alguns equipamentos como chillers. Muitos dispositivos também oferecem uma interface web para configuração.

No Millbrook, o BMS fica na VLAN 300, e os controladores de tratamento de ar dos centros cirúrgicos reportam a ele por BACnet/IP. O chiller pode usar Modbus/TCP. Registre no inventário qual protocolo cada dispositivo usa, porque isso decide o que uma regra de firewall precisa permitir e o que o monitoramento consegue ver.

### 3.2 Confiança por padrão

Como muitos protocolos industriais, as instalações clássicas de BACnet e Modbus aceitam comandos de qualquer coisa que consiga alcançá-las. Um notebook na mesma rede normalmente consegue ler todos os pontos e muitas vezes escrever valores de referência. Existem variantes seguras, mas ainda não são comuns em prédios já instalados.

Isso significa que o limite da rede é o controle principal. Se um PC corporativo ou o notebook de um empreiteiro consegue alcançar a VLAN 300, provavelmente consegue ler as temperaturas dos centros cirúrgicos e alterar valores de referência sem senha. Trate qualquer caminho para dentro da rede predial como um caminho até o equipamento, e projete as regras com base nessa premissa.

### 3.3 Onde as redes se encontram

A estação de trabalho do BMS pode ficar na rede corporativa do hospital, para que a equipe de manutenção a alcance a partir dos escritórios. Os empreiteiros acrescentam acesso remoto para suporte. Os elevadores podem ter a sua própria conexão celular com o fabricante. Cada ponto de encontro é um lugar por onde um atacante na rede do hospital poderia entrar no controle predial.

No Millbrook, o ponto de encontro mais importante é a BMS-WS, que fica ao mesmo tempo na VLAN predial e na rede corporativa. Cada ponto desses deve ser listado com o seu responsável e a sua finalidade. Os capítulos posteriores sobre acesso remoto e segmentação partem dessa lista, então perder uma rota aqui significa perdê-la lá também.

### 3.4 O que um analista faz

Peça à equipe de manutenção e ao empreiteiro um desenho da rede; compare-o com a configuração dos switches e do firewall mantida pela equipe de redes; nunca faça varreduras nos controladores prediais para descobrir. Alguns controladores antigos travam sob varreduras.

Registre qual fonte forneceu cada fato e marque como não confirmado tudo o que foi visto apenas num desenho, até que seja conferido com dados dos switches ou do firewall. Quando as fontes discordarem, pergunte ao empreiteiro e à equipe de redes juntos. Algumas respostas vão exigir uma visita a uma casa de máquinas, agendada pela manutenção.

### 3.5 Sem fio

Alguns sensores reportam por conexões sem fio a gateways. Pergunte onde cada gateway se conecta e quem gerencia as suas chaves.

Um gateway sem fio pode ser uma entrada não listada na rede predial, e as suas chaves podem nunca ter sido trocadas desde a instalação. Registre cada gateway no inventário com a sua localização, a rede à qual se conecta, quem detém as suas chaves e quando foram trocadas pela última vez. Trate um gateway que alcança a VLAN 300 como parte da zona do BMS. Peça essa lista ao empreiteiro por escrito.

### Exemplo resolvido (Millbrook sintético)

O desenho do empreiteiro mostra o BMS na VLAN 300, com a estação de trabalho BMS-WS em dupla conexão (dual-homed): uma placa de rede na VLAN 300 e outra na VLAN corporativa. Aisha anota que a BMS-WS faz a ponte entre as redes corporativa e predial — quem a comprometer alcança todos os controladores — e a acrescenta à sua lista de riscos.

> **Caso sintético — Millbrook.** As VLANs e os hosts são inventados.

### Erros e limites

Os nomes dos protocolos e as portas variam conforme a instalação; confirme com o integrador. Um desenho não prova o que está cabeado.

### Exercícios

- **EX011 — Duas camadas.** Descreva as camadas de campo e de supervisão de um BMS. *Rubrica:* 3 = sensores/atuadores ligados por fio aos controladores; controladores e servidor na rede predial; 2 = parcial; 1 = uma; 0 = nenhum.
- **EX012 — Confiança do BACnet.** O que um notebook na VLAN 300 normalmente consegue fazer com controladores BACnet/IP? *Rubrica:* 3 = ler pontos e muitas vezes escrever valores de referência sem autenticação; 2 = só ler; 1 = vago; 0 = nenhum.
- **EX013 — Estação em dupla conexão.** Por que a segunda placa de rede da BMS-WS é um risco? *Rubrica:* 3 = faz a ponte da rede corporativa para a predial, contornando o firewall; o comprometimento alcança os controladores; 2 = parcial; 1 = velocidade; 0 = nenhum.
- **EX014 — Pontos de encontro.** Nomeie três lugares onde as redes prediais do Millbrook podem encontrar outras redes. *Rubrica:* 3 = estação em dupla conexão, acesso remoto de empreiteiros, conexão celular do elevador (ou semelhante); 2 = dois; 1 = um; 0 = nenhum.
- **EX015 — Sem varredura.** Dê duas razões pelas quais Aisha não faz varreduras nos controladores prediais para mapeá-los. *Rubrica:* 3 = controladores antigos podem travar; não autorizado/risco para áreas clínicas; existem fontes melhores; 2 = uma; 1 = "lento"; 0 = nenhum.

### Síntese

Os controladores prediais confiam em quem os alcança, então todo ponto onde as redes predial e hospitalar se encontram importa.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Um inventário dos dispositivos prediais

### Objetivos de aprendizagem

Você vai (1) montar um inventário de dispositivos prediais agrupado por sistema; (2) sinalizar os dispositivos sem suporte do fornecedor; e (3) explicar como a situação de suporte muda as decisões de risco.

### 4.1 O que registrar

Sistema, nome do dispositivo, localização, responsável, modelo do controlador, firmware, ano de instalação, endereço de rede, situação de suporte do fornecedor e consequência clínica. Os equipamentos prediais duram vinte anos ou mais, então a situação de suporte importa mais aqui do que na TI de escritório.

Cada campo responde a uma pergunta que alguém vai fazer. O responsável diz a quem ligar; o firmware e a situação de suporte dizem se existem correções; o endereço de rede diz quais regras de firewall se aplicam; a consequência clínica diz quão urgente é uma constatação. Um campo vazio é, ele próprio, uma constatação a preencher, não uma lacuna a ignorar.

### 4.2 Agrupamento

Agrupar por sistema mostra com quem falar: os dispositivos de climatização vão para o líder mecânico da manutenção, o painel de gases para a pessoa autorizada para gases medicinais, o elevador para o seu empreiteiro de manutenção.

```python
"""Lab 4: group a synthetic Millbrook building-device list by system and flag unsupported firmware."""
devices = [("AHU-OT1", "HVAC", "2019", True), ("AHU-OT2", "HVAC", "2019", True),
           ("CHILLER-1", "HVAC", "2015", False), ("MGAS-PANEL", "medical gas alarm", "2021", True),
           ("LIFT-CTRL", "elevator", "2012", False), ("DOOR-SRV", "access control", "2020", True)]
by = {}
for name, system, year, supported in devices:
    by.setdefault(system, []).append(name)
    if not supported:
        print(f"UNSUPPORTED {name:10} system={system} installed={year}")
for system, names in sorted(by.items()):
    print(f"{system:18} {len(names)} device(s): {', '.join(names)}")
```

Execute com `python3 lab_bms.py`. Saída verificada:

```text
UNSUPPORTED CHILLER-1  system=HVAC installed=2015
UNSUPPORTED LIFT-CTRL  system=elevator installed=2012
HVAC               3 device(s): AHU-OT1, AHU-OT2, CHILLER-1
access control     1 device(s): DOOR-SRV
elevator           1 device(s): LIFT-CTRL
medical gas alarm  1 device(s): MGAS-PANEL
```

O agrupamento também mostra onde uma única fraqueza afeta vários dispositivos. Os três dispositivos de climatização podem compartilhar um empreiteiro e uma política de senhas, então um problema encontrado num deles deve ser verificado em todos. O Laboratório 4 agrupa os seis dispositivos do Millbrook por sistema e sinaliza os que não têm suporte do fornecedor.

### 4.3 Ler a saída

Dois dispositivos estão sem suporte: o CHILLER-1, instalado em 2015, e o LIFT-CTRL, de 2012. "Sem suporte" significa que o fornecedor não vai publicar correções para novas fraquezas. Eles não podem simplesmente ser substituídos — um chiller custa uma quantia alta e a substituição exige planejamento —, então precisam de controles compensatórios: isolamento de rede mais rigoroso, nenhum acesso remoto, monitoramento mais próximo.

Escreva os controles compensatórios ao lado de cada dispositivo sem suporte no inventário, com um responsável e uma data, para que não sejam esquecidos. Anote também quando o dispositivo deve ser substituído, porque os controles compensatórios são uma ponte, não uma resposta permanente. Confirme a situação de suporte com o fornecedor antes de tratar a sinalização do laboratório como definitiva.

### 4.4 Usar o inventário

O inventário alimenta a correspondência com alertas (Capítulo 10), a segmentação (Capítulo 8) e o relatório de risco final (Capítulo 12). Mantenha-o sob controle de acesso.

Como o inventário nomeia dispositivos, versões e endereços, ele também é um mapa útil para um atacante. Compartilhe-o com as pessoas que precisam dele, como a manutenção, a equipe de redes e os empreiteiros, para os seus próprios sistemas, e mantenha as cópias antigas fora do e-mail. Registre quem o alterou e quando, para que o leitor possa confiar no seu conteúdo. Revise o acesso a ele a cada trimestre.

### 4.5 De onde vêm os dados

O dossiê de entrega do empreiteiro do BMS, os registros de manutenção predial, os pedidos de compra, as tabelas dos switches da equipe de redes e as vistorias nas casas de máquinas contribuem. Cada fonte deixa algo de fora: os dossiês de entrega são anteriores aos acréscimos posteriores, os registros de compra não incluem itens comprados pelos empreiteiros e as casas de máquinas guardam dispositivos que ninguém listou. Compará-las, e registrar qual fonte forneceu cada campo, torna o inventário confiável.

No Millbrook, o dossiê de entrega do empreiteiro do BMS é o ponto de partida, mas as tabelas dos switches da equipe de redes mostram na VLAN 300 dispositivos que o dossiê omite. As vistorias nas casas de máquinas são agendadas pela manutenção. Quando as fontes discordarem, registre os dois valores e resolva-os com o responsável, em vez de escolher um em silêncio.

### 4.6 Coluna de consequência

Escreva em palavras simples a consequência clínica de cada dispositivo, combinada com os líderes da manutenção e clínicos, para que as prioridades fiquem claras para quem não é especialista.

Por exemplo: AHU-OT1, o centro cirúrgico 1 perde o controle de pressão; MGAS-PANEL, a equipe não é avisada de uma falha no suprimento de oxigênio; LIFT-CTRL, transferências de pacientes entre andares atrasadas. A coluna orienta depois a ordem do trabalho no relatório de risco, então a sua redação deve ser clara para gestores que nunca viram os equipamentos. Revise a redação anualmente.

### Exemplo resolvido (Millbrook sintético)

Aisha leva os dois dispositivos sem suporte ao gerente de manutenção. Eles combinam: o CHILLER-1 passa para trás de uma regra de firewall dedicada que permite apenas a BMS-WS, e a conexão celular do LIFT-CTRL é revisada com o empreiteiro dos elevadores. Ambos entram no plano de substituição de bens de capital, com anos-alvo.

> **Caso sintético — Millbrook.** Os dispositivos e os anos são inventados.

### Erros e limites

A situação de suporte precisa ser confirmada com o fornecedor; o ano de instalação sozinho é um indício. Os inventários envelhecem; revise-os trimestralmente.

### Exercícios

- **EX016 — Campos do inventário.** Liste seis campos de um inventário de dispositivos prediais. *Rubrica:* 3 = seis campos corretos, incluindo situação de suporte e consequência; 2 = quatro; 1 = dois; 0 = nenhum.
- **EX017 — Estender o laboratório.** Acrescente `("BOILER-2", "HVAC", "2010", False)`. Que linhas novas o laboratório imprime? *Rubrica:* 3 = "UNSUPPORTED BOILER-2   system=HVAC installed=2010" e HVAC com 4 dispositivos; 2 = uma linha; 1 = errado; 0 = nenhum.
- **EX018 — O que significa sem suporte.** Explique ao gerente de manutenção o que "sem suporte" significa para o CHILLER-1. *Rubrica:* 3 = nenhuma correção do fornecedor para novas falhas; o risco cresce; compensar e planejar a substituição; 2 = parcial; 1 = "quebrado"; 0 = nenhum.
- **EX019 — Controles compensatórios.** Proponha três controles compensatórios para o LIFT-CTRL. *Rubrica:* 3 = isolamento, remover/restringir a conexão celular, monitoramento, plano de substituição; 2 = dois; 1 = um; 0 = nenhum.
- **EX020 — A quem ligar.** Usando o agrupamento, quem recebe o registro do MGAS-PANEL? *Rubrica:* 3 = a pessoa autorizada para gases medicinais; 2 = manutenção; 1 = TI; 0 = nenhum.

### Síntese

Um inventário agrupado por sistema e com a situação de suporte mostra os responsáveis e onde os controles compensatórios precisam carregar o risco.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Contas, senhas padrão e linhas de base dos dispositivos

### Objetivos de aprendizagem

Você vai (1) encontrar contas padrão e compartilhadas nos sistemas prediais; (2) aplicar ideias da ETSI EN 303 645 e do NIST IR 8259 às compras; e (3) definir regras de senha práticas para a equipe de manutenção.

### 5.1 Senhas padrão nos prédios

Controladores e interfaces web muitas vezes saem de fábrica com nomes de usuário e senhas documentados. Os integradores às vezes mantêm uma única senha em todas as instalações que atendem. Ambas as coisas significam que qualquer pessoa que tenha lido um manual ou trabalhado para aquele integrador consegue entrar.

No Millbrook, a interface web do DOOR-SRV ainda aceitava a senha de fábrica do seu manual público. Uma verificação de senhas padrão deve cobrir cada controlador e interface web do inventário, feita pelo empreiteiro ou com ele durante um horário agendado, sem que você tente senhas contra sistemas ativos por conta própria. Registre cada resultado e a data da verificação.

### 5.2 Contas compartilhadas da manutenção

A estação de trabalho do BMS pode ter um único login usado por todos os engenheiros de turno. Isso torna as mudanças impossíveis de rastrear. Contas individuais, mesmo que só no servidor do BMS, permitem que o registro de tendências nomeie a pessoa que alterou um valor de referência.

As contas nominais também ajudam quando algo dá errado. Se um valor de referência de um centro cirúrgico muda à noite, um login compartilhado não consegue dizer quem fez a mudança, enquanto um nominal consegue, como mostra a revisão de tendências do Capítulo 9. Onde um controlador permite apenas uma conta, guarde a senha no cofre e registre cada uso com o nome do engenheiro.

### 5.3 Uma linha de base para compras

A ETSI EN 303 645 exige, entre outras provisões, ausência de senhas padrão universais, uma política de divulgação de vulnerabilidades, atualizações de software e comunicação segura; o NIST IR 8259 lista atividades fundamentais que os fabricantes devem realizar. O setor de compras do hospital pode transformá-las em perguntas contratuais para novos dispositivos prediais, de modo que o problema diminua com o tempo.

Para cada novo dispositivo predial, pergunte ao fornecedor por escrito: cada unidade tem uma senha única, existe uma forma publicada de relatar vulnerabilidades, por quanto tempo serão fornecidas atualizações e a comunicação é protegida? Guarde as respostas com o registro da compra. Um fornecedor que não consegue responder já é, por si só, uma informação útil para o comprador.

### 5.4 Regras que a manutenção consegue seguir

Senhas únicas por dispositivo, guardadas num cofre de senhas gerenciado; contas nominais no BMS; direitos de administrador apenas para trabalho planejado; senhas trocadas quando funcionários de um empreiteiro saem.

Escreva as regras numa página, combinadas com o gerente de manutenção, e verifique se o cofre está disponível nos turnos que precisam dele. Quando uma regra for difícil de seguir, como trocar as senhas sempre que funcionários de um empreiteiro saem, combine como o hospital ficará sabendo da saída. Revise as regras depois de qualquer incidente que tenha envolvido uma conta.

### 5.5 Verificar se a mudança funcionou

Depois que uma senha for trocada, tente a antiga a partir da estação de trabalho do BMS, no mesmo horário agendado, para confirmar que ela falha, e confirme que os operadores ainda conseguem entrar com o novo arranjo.

Registre os dois resultados no chamado de mudança. Se a senha antiga ainda funcionar, a mudança não teve efeito, talvez porque o dispositivo tem mais de uma conta ou interface. Se os operadores não conseguirem entrar com o novo arranjo, podem voltar a uma senha compartilhada, o que desfaz o trabalho; resolva o problema de acesso no mesmo horário.

### Exemplo resolvido (Millbrook sintético)

Aisha e o empreiteiro do BMS revisam o DOOR-SRV, o servidor de controle de acesso. A sua interface web ainda aceita a senha de fábrica listada no manual público. O empreiteiro a troca durante um horário agendado, registra-a no cofre do hospital e cria contas nominais para os três seguranças que gerenciam as agendas das portas.

> **Caso sintético — Millbrook.** O dispositivo e as contas são inventados.

### Erros e limites

A ETSI EN 303 645 tem como alvo a IoT de consumo; para controladores prediais de nível industrial, os requisitos de componentes da IEC 62443-4-2 são mais adequados. Alguns controladores antigos permitem apenas uma conta.

### Exercícios

- **EX021 — Por que as senhas de integradores importam.** Explique o risco de uma senha de integrador reutilizada em muitos hospitais. *Rubrica:* 3 = um vazamento ou um ex-funcionário abre todas as instalações; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX022 — Mudanças rastreáveis.** Como as contas nominais do BMS ajudam depois de uma mudança inesperada de valor de referência? *Rubrica:* 3 = o registro de tendências/auditoria mostra quem a fez; apoia a investigação; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX023 — Perguntas contratuais.** Transforme três provisões da ETSI EN 303 645 em perguntas para o contrato de compra. *Rubrica:* 3 = três perguntas precisas (senhas padrão, divulgação, atualizações/criptografia); 2 = duas; 1 = uma; 0 = nenhum.
- **EX024 — Saída de um funcionário do empreiteiro.** Um engenheiro do empreiteiro que conhecia senhas do Millbrook sai da empresa. O que acontece? *Rubrica:* 3 = trocar no cofre as senhas afetadas, revisar os acessos, registrar; 2 = parte; 1 = vago; 0 = nenhum.
- **EX025 — A norma certa.** Que norma se encaixa melhor do que a ETSI EN 303 645 num controlador industrial de BMS, e por quê? *Rubrica:* 3 = IEC 62443-4-2; requisitos de componentes para automação industrial; 2 = só o nome; 1 = errada; 0 = nenhum.

### Síntese

Senhas padrão trocadas, contas nominais, senhas em cofre e perguntas contratuais de base fecham as portas mais fáceis.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Exposição dos sistemas prediais à internet

### Objetivos de aprendizagem

Você vai (1) explicar por que interfaces prediais acabam na internet; (2) comparar uma exportação de exposição com uma lista aprovada; e (3) responder a uma exposição não aprovada.

### 6.1 Como acontece

Um empreiteiro abre uma porta para alcançar a página web do BMS de casa; uma empresa de elevadores acrescenta um roteador; uma regra de firewall de um projeto nunca é removida. O MITRE ATT&CK for ICS lista a T0883 Internet Accessible Device exatamente para essa situação, e os alertas da CISA insistem repetidamente em retirar as interfaces de sistemas de controle do acesso direto pela internet.

No Millbrook, uma regra acrescentada em 2023 para o comissionamento do chiller expôs o BACnet e o login web do BMS diretamente à internet, e ninguém a removeu depois do projeto. Toda abertura desse tipo começa com um pedido razoável por conveniência. A tarefa é dar aos empreiteiros uma rota suportada, para que não precisem pedir portas.

### 6.2 Verificar a exposição

A equipe de redes do hospital, ou um serviço autorizado, produz uma lista dos endereços públicos e serviços abertos do hospital. O analista a compara com a lista aprovada — normalmente apenas o gateway de acesso remoto.

```python
"""Lab 6: compare a synthetic external-exposure export with approved internet-facing services."""
approved = {("203.0.113.10", 443)}
found = [("203.0.113.10", 443, "VPN gateway"), ("203.0.113.24", 47808, "BACnet/IP"),
         ("203.0.113.24", 80, "BMS web login")]
for ip, port, svc in found:
    print(f"{ip}:{port:<6} {svc:14} {'approved' if (ip, port) in approved else 'NOT APPROVED - report'}")
print("unapproved:", sum((ip, port) not in approved for ip, port, _ in found))
```

Execute com `python3 lab_exposure.py`. Saída verificada:

```text
203.0.113.10:443    VPN gateway    approved
203.0.113.24:47808  BACnet/IP      NOT APPROVED - report
203.0.113.24:80     BMS web login  NOT APPROVED - report
unapproved: 2
```

Obtenha a exportação com as pessoas que são donas dos endereços e não sonde endereços do hospital você mesmo, a menos que a equipe de redes tenha autorizado. A lista aprovada deve ser curta e nomear um responsável para cada item. O Laboratório 6 compara a exportação do Millbrook com uma lista aprovada que contém apenas o gateway VPN.

### 6.3 Ler o resultado

O gateway VPN em 203.0.113.10, porta 443, está aprovado. O endereço 203.0.113.24 expõe BACnet/IP na 47808 e um login web do BMS na 80. Ambos não estão aprovados: qualquer pessoa na internet poderia tentar ler ou comandar controladores, ou adivinhar a senha web.

A exposição importa mais por causa do que está por trás dela. O BACnet aceita comandos de qualquer um que o alcance, então isso não é apenas um vazamento de dados, mas uma rota até as configurações de ar dos centros cirúrgicos e do chiller. Essa combinação a coloca no topo do relatório do analista para a equipe de redes e a manutenção.

### 6.4 Responder

Relate imediatamente à equipe de redes e à manutenção; peça ao dono da rede que feche a exposição por meio de uma mudança emergencial; verifique nos registros as conexões vindas de fora; descubra quem a abriu e por quê, e dê a essa pessoa uma rota suportada em troca.

Guarde a exportação, os horários e os trechos dos registros com o relatório, porque eles mostram quanto tempo durou a exposição e se alguém a usou. No Millbrook, os registros do firewall mostraram muitas tentativas externas de alcançar a porta 47808 nos últimos meses. Essa constatação é repassada à manutenção para verificar nas configurações dos controladores e nos registros de tendências se houve mudanças no mesmo período.

### 6.5 Evitar a repetição

Acrescente uma verificação mensal de exposição ao calendário da equipe de redes, exija uma data de término em toda regra de firewall aberta para um projeto e faça os empreiteiros solicitarem acesso remoto pelo processo do gateway, em vez de pedirem portas.

Cada medida fecha uma causa. A verificação mensal pega o que escapa; as datas de término fazem as regras de projeto expirarem; o processo do gateway dá aos empreiteiros uma rota que não precisa de portas abertas. Acompanhe a verificação mensal no registro, com a data e o resultado, para que um mês perdido fique visível.

### Exemplo resolvido (Millbrook sintético)

A equipe de redes rastreia o 203.0.113.24 até uma regra de firewall acrescentada em 2023 para um projeto de comissionamento do chiller. Ela a remove em menos de uma hora; os registros do firewall mostram muitas tentativas externas de conexão à porta 47808 nos últimos meses. O empreiteiro recebe contas no gateway em troca.

> **Caso sintético — Millbrook.** Os endereços pertencem à faixa de documentação 203.0.113.0/24, e os eventos são inventados.

### Erros e limites

As listas de exposição são retratos instantâneos; repita mensalmente. Teste apenas endereços que pertencem à sua organização, por meios autorizados.

### Exercícios

- **EX026 — Como a exposição acontece.** Descreva duas formas pelas quais uma interface do BMS se torna alcançável pela internet. *Rubrica:* 3 = duas rotas concretas (porta do empreiteiro, regra esquecida, roteador do fornecedor); 2 = uma; 1 = vago; 0 = nenhum.
- **EX027 — Terceira constatação.** Se a exportação também encontrasse 203.0.113.10 na porta 22, o que o laboratório imprimiria para ela e no total? *Rubrica:* 3 = linha NOT APPROVED e "unapproved: 3"; 2 = um; 1 = aprovado; 0 = nenhum.
- **EX028 — Nome da técnica.** Que técnica do ATT&CK for ICS descreve a situação do 203.0.113.24? *Rubrica:* 3 = T0883 Internet Accessible Device; 2 = só o nome; 1 = errada; 0 = nenhum.
- **EX029 — Passos da resposta.** Liste os passos da resposta depois de encontrar uma exposição não aprovada. *Rubrica:* 3 = relatar, fechamento emergencial pelo dono, verificar registros, achar a causa, oferecer alternativa segura; 2 = três; 1 = um; 0 = nenhum.
- **EX030 — Limite dos testes.** Por que Aisha não testa os endereços de outros hospitais "para comparação"? *Rubrica:* 3 = não autorizado, potencialmente ilegal, pode causar interrupção; 2 = um; 1 = tudo bem; 0 = nenhum.

### Síntese

Só o gateway fica de frente para a internet; qualquer outra coisa encontrada é relatada, fechada e substituída por uma rota suportada.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Acesso remoto de empreiteiros e fornecedores

### Objetivos de aprendizagem

Você vai (1) inventariar todas as rotas remotas para dentro dos sistemas prediais; (2) aplicar as lições do CISA AA21-042A; e (3) projetar um processo controlado de acesso remoto para empreiteiros.

### 7.1 Muitas mãos

Um hospital pode ter empreiteiros separados para BMS, chillers, elevadores, alarmes de incêndio e controle de acesso, cada um querendo suporte remoto. Sem uma política, cada um instala a sua própria rota: uma ferramenta de área de trabalho remota na estação de trabalho, um roteador, um modem celular.

No Millbrook, Aisha encontrou quatro rotas separadas, três delas instaladas por empreiteiros para a própria conveniência. Nenhuma era maliciosa, mas cada uma era uma entrada que o hospital não controlava. A primeira tarefa é listar cada rota, com quem a instalou, o que ela alcança e se alguém ainda a usa.

### 7.2 Lições do AA21-042A

O alerta da CISA sobre o comprometimento, em 2021, de uma estação de tratamento de água nos EUA descreve um software de acesso remoto sendo usado para alcançar um sistema de controle. As suas recomendações incluem autenticação multifator, senhas fortes para a área de trabalho remota, fechamento das portas de área de trabalho remota não usadas e auditoria das conexões remotas. O MITRE ATT&CK for ICS descreve o mau uso dessas rotas como T0886 Remote Services.

Para o Millbrook, as lições se aplicam diretamente às rotas que Aisha encontrou. Uma ferramenta de área de trabalho remota na BMS-WS é o mesmo tipo de rota descrito no alerta. Exigir autenticação multifator, auditar as conexões e fechar o acesso de área de trabalho remota não usado são passos práticos que a manutenção e os empreiteiros podem combinar, sem esperar por um projeto maior.

### 7.3 Um processo controlado

Um único gateway de acesso remoto de propriedade do hospital; uma conta nominal e com fator múltiplo para cada engenheiro de empreiteiro; contas desabilitadas por padrão e habilitadas por chamado; acesso limitado ao sistema específico que o empreiteiro mantém; sessões gravadas sempre que possível; a conta desabilitada quando a sessão termina.

Escreva o processo num documento curto que os empreiteiros assinam, para que saibam como obter acesso numa emergência, além de para o trabalho planejado. Teste-o uma vez com cada empreiteiro antes de as rotas antigas serem removidas. Revise as contas do gateway semanalmente, porque contas deixadas habilitadas depois de uma sessão são, elas próprias, uma constatação, como mostra mais adiante o relatório de risco do Millbrook.

### 7.4 Remover as rotas antigas

Quando o gateway estiver em funcionamento, remova as ferramentas de área de trabalho remota instaladas diretamente nas estações de trabalho prediais e desconecte os modems não gerenciados — de comum acordo com o empreiteiro e a manutenção, num horário planejado, para que o suporte não se perca durante uma emergência.

No Millbrook, a ordem foi combinada com a manutenção: a ferramenta de área de trabalho remota só foi removida depois que a conta do empreiteiro do BMS no gateway funcionou, o roteador do chiller uma semana depois, e a conexão do elevador foi restringida em vez de removida. Registre cada remoção com a data e quem a confirmou, e depois verifique de novo o inventário de rotas para garantir que nada reapareceu.

### Exemplo resolvido (Millbrook sintético)

O inventário de rotas de Aisha encontra quatro entradas: o gateway, uma ferramenta de área de trabalho remota na BMS-WS instalada pelo empreiteiro do BMS, a conexão celular do elevador e o roteador de um fornecedor do chiller. A manutenção aprova um plano: a ferramenta de área de trabalho remota é removida na semana 1, depois que a conta do empreiteiro no gateway funcionar; o roteador do chiller na semana 2; a conexão do elevador é restringida à central de serviços do empreiteiro dos elevadores, com exigência de chamado.

> **Caso sintético — Millbrook.** As rotas e os prazos são inventados.

### Erros e limites

Algumas conexões de elevadores e de alarmes de incêndio são exigidas para o monitoramento de segurança; restrinja-as e registre-as, em vez de removê-las às cegas.

### Exercícios

- **EX031 — Contar as rotas.** Liste as quatro rotas remotas que Aisha encontrou. *Rubrica:* 3 = gateway, área de trabalho remota na BMS-WS, celular do elevador, roteador do chiller; 2 = três; 1 = uma; 0 = nenhum.
- **EX032 — Aplicar o alerta.** Aplique duas recomendações do AA21-042A ao acesso do empreiteiro do BMS. *Rubrica:* 3 = MFA na conta do gateway e auditoria das sessões (ou fechar a porta de RDP/senha forte); 2 = uma; 1 = vago; 0 = nenhum.
- **EX033 — Limites por sistema.** Por que a conta do empreiteiro do chiller não deve alcançar o servidor de controle de acesso? *Rubrica:* 3 = menor privilégio; o comprometimento de um empreiteiro fica limitado ao seu sistema; 2 = parcial; 1 = sem motivo; 0 = nenhum.
- **EX034 — Momento da remoção.** Por que a ferramenta de área de trabalho remota só é removida depois que a conta do gateway funciona? *Rubrica:* 3 = evitar perder suporte durante uma emergência; testar a substituta antes; 2 = parcial; 1 = sem motivo; 0 = nenhum.
- **EX035 — Conexão de segurança.** A conexão de monitoramento do alarme de incêndio usa um modem celular. Ele deve ser desconectado? *Rubrica:* 3 = não; monitoramento de segurança; restringir, documentar e revisar com o responsável; 2 = só "não"; 1 = sim; 0 = nenhum.

### Síntese

Toda ajuda remota passa por um único gateway, com contas nominais, de fator múltiplo e vinculadas a chamados; as rotas legadas são aposentadas com cuidado.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 12

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Segmentação das redes prediais

### Objetivos de aprendizagem

Você vai (1) definir zonas e condutos para os sistemas prediais do Millbrook usando os termos da IEC 62443; (2) escrever um conjunto mínimo de regras; e (3) planejar a migração sem interromper as áreas clínicas.

### 8.1 Zonas

A IEC 62443-3-2 descreve o agrupamento de ativos em zonas com requisitos de segurança semelhantes, ligadas por condutos. No Millbrook, um começo sensato é: uma zona do BMS (controladores e servidor do BMS), uma zona relevante para a segurança física (alarme de gases medicinais e elevador, cada um separadamente), uma zona de controle de acesso, uma DMZ para o gateway e as exportações de dados, e a zona corporativa.

Escreva cada zona com os seus membros, o seu responsável e a consequência caso seja comprometida. Os alarmes de gases medicinais e os elevadores ficam em zonas separadas porque as suas falhas importam para a segurança do paciente e os seus empreiteiros são diferentes. Um diagrama de zonas aceito tanto pela manutenção quanto pela equipe de redes é o ponto de partida para qualquer tabela de regras.

### 8.2 Condutos e regras

Escreva cada conduto como um pequeno conjunto de regras: a BMS-WS (transferida para a zona do BMS) para os controladores via BACnet/IP; o gateway para a BMS-WS nas sessões dos empreiteiros; o servidor do BMS para um servidor de dados na DMZ, para os relatórios de energia. Todo o resto é negado. Os PCs corporativos nunca se conectam diretamente aos controladores.

Escreva cada regra com origem, destino, protocolo e porta, um motivo e um responsável, para que possa ser revisada depois. Confira as regras com o inventário de rotas, para que nada aprovado seja bloqueado e nada não aprovado permaneça. Uma regra sem responsável deve ser tratada como candidata à remoção.

### 8.3 Corrigir a estação em dupla conexão

Remover a placa de rede corporativa da BMS-WS fecha a ponte do Capítulo 3. A equipe de manutenção que precisa ver o BMS a partir dos escritórios usa um painel somente leitura no servidor da DMZ, ou um host de salto alcançado pelo gateway.

Antes de remover a placa, combine com a manutenção quais tarefas de escritório a usavam e teste a rota substituta com as pessoas que vão usá-la. Faça a mudança num horário agendado e confirme depois que a BMS-WS ainda alcança os seus controladores. Registre a mudança no item da lista de riscos que Aisha criou quando encontrou a ponte.

### 8.4 Migrar com segurança

Mude um conduto de cada vez, em horários combinados com a manutenção e os gerentes dos centros cirúrgicos; observe se há pontos perdidos no BMS depois de cada passo; mantenha a configuração anterior pronta para ser restaurada.

Combine antes quais pontos do BMS serão verificados depois de cada passo e quem vai verificá-los. No Millbrook, depois do segundo passo, dois controladores pararam de reportar porque um conduto para um servidor de horário tinha sido esquecido; isso foi descoberto porque os pontos foram verificados imediatamente. Anote essas surpresas na tabela de regras, para que a próxima mudança as evite.

### 8.5 Documentação

Publique o diagrama de zonas e a tabela de regras com números de revisão e responsáveis, para que os empreiteiros possam solicitar mudanças com base neles.

Mantenha o diagrama e a tabela num lugar que a manutenção, a equipe de redes e os empreiteiros possam ler, e faça referência a eles em toda solicitação de mudança. Quando uma mudança for feita, atualize o número da revisão e anote quem a aprovou. A documentação desatualizada leva os empreiteiros a pedir regras que já existem ou que contradizem o projeto. Guarde as revisões substituídas, para que as decisões passadas possam ser rastreadas.

### Exemplo resolvido (Millbrook sintético)

Ao longo de três manhãs de sábado planejadas, a equipe de redes cria as zonas, transfere a BMS-WS inteiramente para a zona do BMS e implanta as regras. Depois do passo 2, dois controladores param de reportar; a causa é um conduto esquecido para um servidor de horário, que é acrescentado sob a mesma mudança. Os relatórios de energia passam a vir do servidor da DMZ.

> **Caso sintético — Millbrook.** Os passos e as constatações são inventados.

### Erros e limites

A segmentação não detém um atacante que já tem credenciais do gateway; ela limita aonde ele pode ir. Os projetos de zonas precisam ser revisados quando sistemas são acrescentados.

### Exercícios

- **EX036 — Lista de zonas.** Proponha cinco zonas para o Millbrook. *Rubrica:* 3 = BMS, relevante para a segurança física (gases/elevador), controle de acesso, DMZ, corporativa; 2 = quatro; 1 = duas; 0 = nenhum.
- **EX037 — Escrever um conduto.** Escreva a regra que permite ao servidor do BMS enviar dados de energia ao servidor da DMZ. *Rubrica:* 3 = origem servidor do BMS, destino servidor de dados da DMZ, porta específica, permitir; mais negação padrão; 2 = sem negação; 1 = qualquer; 0 = nenhum.
- **EX038 — Visualização nos escritórios.** Como a equipe de manutenção vê o BMS a partir dos escritórios depois que a BMS-WS perde a placa corporativa? *Rubrica:* 3 = painel somente leitura na DMZ ou host de salto via gateway; 2 = parcial; 1 = recolocar a placa; 0 = nenhum.
- **EX039 — Pontos perdidos.** Dois controladores param de reportar depois de uma mudança de regra. Qual é a resposta segura? *Rubrica:* 3 = verificar o impacto clínico, restaurar a configuração anterior se necessário, achar o conduto ausente, corrigir sob mudança; 2 = parcial; 1 = ignorar; 0 = nenhum.
- **EX040 — Limite da segmentação.** Contra o que a segmentação não protege? *Rubrica:* 3 = mau uso de credenciais legítimas do gateway/pessoa interna dentro dos condutos permitidos; 2 = vago; 1 = tudo protegido; 0 = nenhum.

### Síntese

Zonas com condutos estreitos impedem que comprometimentos no escritório alcancem os controladores; migre um conduto de cada vez.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 12

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Monitorar tendências e registros

### Objetivos de aprendizagem

Você vai (1) usar os registros de tendências do BMS como evidência de segurança; (2) sinalizar mudanças fora das janelas aprovadas com um script curto; e (3) combinar evidências de tendências, de logins e da rede.

### 9.1 Tendências como evidência

Um BMS registra valores ao longo do tempo — temperaturas, valores de referência, posições de válvulas —, principalmente para os engenheiros. Os mesmos registros mostram quando um valor de referência mudou e, com contas nominais, quem o mudou. Muitas vezes, são a melhor evidência de adulteração num sistema predial.

Para Aisha, o registro de tendências costuma ser o primeiro lugar para olhar quando algo parece errado, porque mostra diretamente o efeito físico. Descubra com que frequência cada ponto é amostrado e por quanto tempo os registros são guardados antes de confiar neles. Onde as contas são compartilhadas, a tendência mostra o que mudou, mas não quem mudou.

### 9.2 Janelas de mudança

A manutenção combina janelas para as mudanças planejadas de valores de referência, por exemplo, nas manhãs dos dias úteis. Uma mudança fora de uma janela não é necessariamente maliciosa, mas precisa de uma explicação.

```python
"""Lab 9: flag operating-theatre temperature setpoint changes outside a synthetic change window."""
trend = [("01:00", 20.0), ("02:00", 20.0), ("03:00", 26.0), ("04:00", 26.0), ("09:00", 21.0)]
window = ("08:00", "10:00")
prev = None
for t, sp in trend:
    if prev is not None and sp != prev:
        inside = window[0] <= t <= window[1]
        print(f"{t} setpoint {prev}->{sp} {'in window' if inside else 'OUTSIDE WINDOW - review'}")
    prev = sp
```

Execute com `python3 lab_trend.py`. Saída verificada:

```text
03:00 setpoint 20.0->26.0 OUTSIDE WINDOW - review
09:00 setpoint 26.0->21.0 in window
```

As janelas devem ser combinadas com a manutenção e escritas, com quaisquer exceções, como reparos emergenciais. Fora da janela, a pergunta é simplesmente o que aconteceu e quem fez. O Laboratório 9 confere a tendência de um valor de referência de centro cirúrgico com uma janela matinal e sinaliza qualquer mudança fora dela. Revise as janelas com a manutenção anualmente.

### 9.3 Ler a saída

Às 03:00, o valor de referência do centro cirúrgico subiu de 20 °C para 26 °C, fora da janela das 08:00 às 10:00; ele voltou para 21 °C às 09:00, dentro da janela. A mudança das 03:00 é a que deve ser revisada.

O retorno para 21 °C às 09:00 está dentro da janela, mas ainda vale anotá-lo, porque sugere que alguém percebeu a mudança anterior e a corrigiu. As duas mudanças entram na revisão, com as perguntas sobre quem fez cada uma e por quê. O laboratório mostra apenas o valor de referência; a tendência da temperatura real do centro cirúrgico mostraria se a mudança teve efeito.

### 9.4 Combinar fontes

Verifique no registro de auditoria do BMS quem estava conectado às 03:00; no registro do gateway, as sessões remotas; no registro do firewall, as conexões com a zona do BMS. A concordância entre as fontes fortalece a conclusão, seja ela qual for.

Registre o que cada fonte mostrou, inclusive as que não mostraram nada. No Millbrook, o registro do gateway não tinha sessões às 03:00, o que tornava improvável uma mudança remota, e o registro de auditoria do BMS nomeava o engenheiro da noite. O registro do firewall também teria sido verificado se as duas primeiras fontes tivessem discordado.

### 9.5 Alertas

Onde o BMS permitir, gere um alarme para mudanças de valores de referência fora das janelas em unidades críticas, enviado ao engenheiro de plantão da manutenção.

Combine com a manutenção quais unidades contam como críticas, como as unidades de tratamento de ar dos centros cirúrgicos, e o que o engenheiro de plantão deve fazer ao receber o alarme. Um alarme que ninguém atende logo passa a ser ignorado. Teste-o uma vez depois de configurá-lo, durante uma mudança planejada, e registre o resultado. Revise a lista de alarmes a cada trimestre com os engenheiros de plantão, retirando as unidades que já não precisam dele.

### 9.6 Guardar as evidências

Quando uma mudança precisar de revisão, exporte no mesmo dia os registros de tendências e de auditoria relevantes, anote a hora da exportação e guarde-os com as notas da revisão; a retenção do BMS muitas vezes é curta.

Guarde as exportações onde apenas as pessoas que revisam a mudança possam lê-las, com uma nota sobre a origem de cada uma. No Millbrook, os registros de tendências eram guardados por apenas 14 dias, o que mais tarde virou uma constatação no relatório de risco de Aisha. Até que a retenção seja ampliada, a exportação no mesmo dia é a única prática segura.

### Exemplo resolvido (Millbrook sintético)

Aisha verifica os registros: nenhuma sessão no gateway às 03:00, mas o registro de auditoria do BMS mostra que o engenheiro da noite elevou o valor de referência durante uma falha do chiller, para reduzir a carga, e esqueceu de registrar. A explicação é documentada, e o procedimento de plantão ganha um passo: registrar no livro do turno qualquer mudança fora da janela.

> **Caso sintético — Millbrook.** A tendência e a explicação são inventadas.

### Erros e limites

Os registros de tendências podem ter amostragem esparsa e perder mudanças curtas; os relógios precisam estar sincronizados. A retenção pode ser de apenas algumas semanas — exporte o que precisar.

### Exercícios

- **EX041 — Lógica da janela.** Por que a mudança das 09:00 não é sinalizada? *Rubrica:* 3 = 09:00 está dentro da janela das 08:00 às 10:00; 2 = "permitida"; 1 = errado; 0 = nenhum.
- **EX042 — Tendência modificada.** Se a janela fosse das 02:00 às 04:00, o que o laboratório imprimiria? *Rubrica:* 3 = 03:00 "in window", 09:00 "OUTSIDE WINDOW - review"; 2 = um; 1 = igual; 0 = nenhum.
- **EX043 — Três fontes.** Quais três registros Aisha combina com a tendência? *Rubrica:* 3 = auditoria do BMS, gateway, firewall; 2 = dois; 1 = um; 0 = nenhum.
- **EX044 — Impacto clínico.** Que impacto clínico um valor de referência de 26 °C num centro cirúrgico poderia ter durante a noite? *Rubrica:* 3 = sala inutilizável/fora da especificação no início da lista, atraso ou preocupação de controle de infecção; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX045 — Melhoria do processo.** Que mudança evita a próxima mudança fora da janela sem explicação? *Rubrica:* 3 = registro obrigatório no livro do turno, alarme para mudança fora da janela; 2 = um; 1 = culpar; 0 = nenhum.

### Síntese

Os registros de tendências mostram o que mudou e quando; combinados com os registros de acesso, explicam a mudança.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 12

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Alertas e correções para sistemas prediais

### Objetivos de aprendizagem

Você vai (1) comparar os alertas com o inventário predial; (2) decidir entre corrigir e mitigar; e (3) acompanhar as decisões ao longo do tempo.

### 10.1 Fontes

O índice de alertas da CISA inclui muitos produtos de automação predial, de controle de acesso e de elevadores, ao lado dos avisos dos fornecedores. Assine os que forem relevantes para os fornecedores do Millbrook.

Use o inventário para escolher quais fornecedores e produtos acompanhar, incluindo os controladores do BMS, o servidor de controle de acesso e o controlador dos elevadores. Consulte regularmente o índice da CISA e as páginas dos fornecedores e registre a data de cada consulta. Um alerta que chega depois de um incidente é muito menos útil do que um lido na semana em que foi publicado.

### 10.2 Correspondência

Para cada alerta: o produto está no nosso inventário, numa versão afetada, alcançável da forma que o alerta descreve? Os dispositivos sem suporte (Capítulo 4) muitas vezes correspondem a alertas antigos que nunca serão corrigidos.

Registre a resposta a cada pergunta no registro de alertas, mesmo quando o produto não estiver presente. Para dispositivos sem suporte, como o CHILLER-1 e o LIFT-CTRL, um alerta sem correção leva diretamente aos controles compensatórios: isolamento mais rigoroso, nenhum acesso remoto e monitoramento mais próximo, como combinado para esses dispositivos no trabalho de inventário.

### 10.3 Escolher

Corrigir um controlador do BMS normalmente exige uma visita do empreiteiro, um horário agendado e a verificação de todos os pontos depois. As mitigações — regras de firewall, desabilitar uma interface web, restringir a conta do gateway — muitas vezes podem ser aplicadas antes. Registre o que você escolheu e por quê.

A escolha depende da consequência e de quão cedo há um horário seguro disponível. Uma mitigação aplicada hoje pode ser melhor do que uma correção no mês que vem, desde que se verifique que ela bloqueia o caminho descrito pelo alerta. Escreva a decisão no registro com a data, o responsável e a data de revisão.

### 10.4 Acompanhamento

Um registro simples: alerta, produtos afetados aqui, decisão, mitigação, data da correção, responsável, data de revisão. Relate mensalmente ao gerente de manutenção os itens abertos de alta consequência.

Mantenha o registro no mesmo lugar que o inventário, para que um novo alerta possa ser comparado depressa. Revise-o com o gerente de manutenção todo mês e encerre os itens apenas quando a conclusão tiver sido demonstrada, como uma verificação de versão depois da correção. Itens deixados abertos por muito tempo precisam de uma nova decisão, em vez de envelhecer em silêncio.

### 10.5 Testar depois da correção

Depois, o empreiteiro confirma que todos os pontos reportam, que os alarmes funcionam e que as agendas estão corretas; a manutenção aprova.

Combine as verificações antes da correção, com uma lista dos pontos e alarmes a testar e da pessoa que vai testá-los. Mantenha um recurso alternativo pronto, como o firmware anterior ou chaves manuais para as portas. Registre os resultados e a aprovação no registro de alertas, para que o item possa ser encerrado com evidência. Corrija uma unidade primeiro, sempre que possível, e verifique-a antes de passar à seguinte.

### 10.6 Contato com o fornecedor

Quando um alerta não for claro sobre as configurações prediais, pergunte diretamente ao fornecedor ou ao integrador: quais modelos e opções são afetados, se a funcionalidade vulnerável vem habilitada por padrão e se uma mitigação foi testada em sistemas como os do Millbrook. Registre a resposta e quem a deu. As equipes de segurança de produto dos fornecedores costumam responder mais rápido quando a pergunta cita o modelo e a versão exatos do inventário.

Guarde as respostas do fornecedor com o alerta no registro e repita a pergunta se a resposta não for clara. Se o fornecedor confirmar que uma mitigação funciona, verifique-a mesmo assim no Millbrook, porque a configuração local pode ser diferente.

### Exemplo resolvido (Millbrook sintético)

Um alerta sintético avisa que a interface web do DOOR-SRV permite contornar a autenticação na versão 4.1; o Millbrook roda a 4.1. Depois do Capítulo 8, a interface só é alcançável a partir da zona de controle de acesso, e a correção do fornecedor, a 4.2, exige uma interrupção de 30 minutos das agendas das portas. A decisão: restringir hoje a interface à estação de trabalho da sala de segurança e corrigir no domingo às 06:00, com chaves manuais entregues aos gerentes das enfermarias durante a interrupção.

> **Caso sintético — Millbrook.** O alerta e as versões são inventados; os alertas reais são listados pela CISA.

### Erros e limites

Os alertas podem omitir detalhes; pergunte aos fornecedores. É preciso verificar se uma mitigação realmente bloqueia o caminho descrito.

### Exercícios

- **EX046 — Três perguntas de correspondência.** Enuncie as três perguntas que decidem se um alerta importa aqui. *Rubrica:* 3 = produto presente, versão afetada, alcançável como descrito; 2 = duas; 1 = uma; 0 = nenhum.
- **EX047 — Correspondência sem suporte.** Um alerta afeta o LIFT-CTRL, sem correção prevista. Qual é a decisão? *Rubrica:* 3 = isolamento/monitoramento compensatório, registrar, acelerar a substituição; 2 = parcial; 1 = ignorar; 0 = nenhum.
- **EX048 — Plano para a interrupção das portas.** Por que entregar chaves manuais durante a correção do DOOR-SRV? *Rubrica:* 3 = agendas das portas indisponíveis, áreas restritas precisam continuar controladas e acessíveis; 2 = parcial; 1 = sem motivo; 0 = nenhum.
- **EX049 — Registro do item.** Escreva o registro de acompanhamento do alerta do DOOR-SRV. *Rubrica:* 3 = alerta, produto/versão, decisão, mitigação, data da correção, responsável, revisão; 2 = a maioria; 1 = pouco; 0 = nenhum.
- **EX050 — Verificar uma mitigação.** Como você confirmaria que a restrição da interface funciona? *Rubrica:* 3 = o dono da rede confirma a regra; teste autorizado a partir de outra zona falha e a partir da sala de segurança funciona; 2 = parcial; 1 = presumir; 0 = nenhum.

### Síntese

Os alertas são comparados, mitigados depressa, corrigidos em horários agendados com recursos alternativos e acompanhados até o encerramento.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 12

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Resposta a incidentes em sistemas prediais hospitalares

### Objetivos de aprendizagem

Você vai (1) adaptar os passos da resposta a incidentes aos sistemas prediais; (2) decidir quando isolar o BMS; e (3) coordenar com as equipes clínicas, de manutenção e de TI.

### 11.1 Planejar antes

O NIST SP 800-82r3 enfatiza a preparação da resposta a incidentes de TO junto com a equipe de operação. Num hospital, isso significa que a manutenção, os gestores clínicos de plantão, a equipe de segurança de TI e os empreiteiros combinam de antemão: quem lidera, qual é o recurso manual de cada sistema e como alcançar os empreiteiros à noite.

Escreva o acordo como um plano curto, com números de telefone, o recurso alternativo de cada sistema crítico e quem pode ordenar o isolamento. Exercite-o pelo menos uma vez com a manutenção e um empreiteiro, talvez num fim de semana tranquilo. O primeiro incidente é a hora errada de descobrir que o empreiteiro do chiller não tem contato noturno.

### 11.2 Detectar e avaliar

Um alarme, um valor de referência fora da janela ou uma nota de resgate na BMS-WS iniciam o processo. A primeira pergunta é clínica: alguma área está insegura agora? O gestor de plantão e a manutenção decidem as medidas de proteção imediatas — remanejar uma lista de cirurgias, passar para os alarmes de oxigênio em cilindros monitorados pela equipe.

Só depois que o quadro clínico estiver claro começa a avaliação de segurança: o que foi afetado, como começou e se está se espalhando. No Millbrook, a primeira ligação na noite do resgate foi para a manutenção, que confirmou que os centros cirúrgicos estavam vazios e as enfermarias normais antes de a equipe de redes agir.

### 11.3 Conter

Se não for possível confiar no BMS, os controladores normalmente conseguem rodar as suas últimas agendas programadas sem o servidor. Isolar a zona do BMS no seu firewall impede novos comandos remotos, enquanto os equipamentos continuam funcionando localmente. A equipe de manutenção faz rondas nas casas de máquinas e confere à mão os valores críticos.

Antes de isolar, verifique como cada controlador crítico se comporta sem o servidor, porque alguns recaem em padrões que diferem da operação normal. No Millbrook, os condutos foram bloqueados às 22:55 e os controladores continuaram com as suas agendas, enquanto os engenheiros da manutenção faziam rondas de hora em hora. Anote a hora de cada passo de contenção para o registro do incidente.

### 11.4 Evidências e recuperação

Preserve os registros e as imagens antes de reconstruir; restaure a BMS-WS e o servidor a partir de cópias verificadas; confira cada ponto crítico com as leituras locais; reconecte os condutos um de cada vez.

Combine de antemão onde as evidências serão guardadas e quem vai coletá-las, para que a reconstrução não atrase. No Millbrook, o líder do incidente mandou copiar a imagem de disco da BMS-WS e o trecho do registro do firewall das 22:00 às 23:00 para o repositório de evidências antes de a reconstrução começar. Guarde as evidências até que o líder do incidente decida que já não são necessárias. Registre cada passo e o seu horário.

### 11.5 Comunicação

O líder do incidente informa a direção do hospital, que decide sobre a notificação externa. Os analistas não contatam a imprensa nem os reguladores por conta própria.

Os analistas apoiam o líder do incidente fornecendo fatos claros, com horários e fontes. Devem evitar mensagens informais a colegas ou empreiteiros que possam espalhar informações imprecisas. Se um regulador ou um jornalista contatar diretamente um analista, encaminhe o pedido ao líder do incidente sem comentários. Guarde uma cópia de cada atualização enviada, com o seu horário, para que o registro do incidente mostre o que foi dito e quando.

### Exemplo resolvido (Millbrook sintético)

Às 22:40, a BMS-WS mostra uma mensagem de resgate. A manutenção confirma que os centros cirúrgicos estão vazios e as enfermarias normais. A equipe de redes bloqueia os condutos da zona do BMS às 22:55; os controladores continuam com as suas agendas. Os engenheiros da manutenção fazem rondas de hora em hora. Na manhã seguinte, a BMS-WS é reconstruída a partir de uma imagem verificada, o servidor é verificado e os condutos são restaurados até as 14:00, depois da verificação dos pontos.

> **Caso sintético — Millbrook.** O incidente é inventado.

### Erros e limites

Alguns controladores falham para padrões seguros que diferem da operação normal; conheça-os antes de isolar. O monitoramento por rondas não pode durar indefinidamente; planeje a escala de pessoal.

### Exercícios

- **EX051 — Primeira pergunta.** Qual é a primeira pergunta depois que a BMS-WS mostra uma mensagem de resgate, e quem a responde? *Rubrica:* 3 = alguma área clínica está insegura; gestor de plantão/manutenção; 2 = só a pergunta; 1 = pergunta de TI; 0 = nenhum.
- **EX052 — Por que o isolamento é aceitável.** Explique por que bloquear os condutos da zona do BMS não parou a ventilação. *Rubrica:* 3 = os controladores rodam as agendas locais sem o servidor; 2 = parcial; 1 = parou sim; 0 = nenhum.
- **EX053 — Monitoramento manual.** O que substitui o monitoramento do BMS enquanto ele está isolado? *Rubrica:* 3 = rondas da manutenção lendo valores locais, verificações de alarmes pela equipe; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX054 — Reconectar.** Descreva como os condutos são restaurados depois da recuperação. *Rubrica:* 3 = um de cada vez, com verificação dos pontos em relação às leituras locais; 2 = parcial; 1 = todos de uma vez; 0 = nenhum.
- **EX055 — Padrões seguros.** Por que Aisha precisa conhecer o comportamento de falha segura dos controladores antes de recomendar o isolamento? *Rubrica:* 3 = alguns padrões mudam a operação (por exemplo, ventiladores desligados/no máximo), podendo afetar pacientes; 2 = parcial; 1 = não precisa; 0 = nenhum.

### Síntese

A segurança clínica lidera, o controle local sustenta os equipamentos, o isolamento detém o dano remoto e as evidências vêm antes da recuperação.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 12

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Projeto final: um relatório de risco dos sistemas prediais

### Objetivos de aprendizagem

Você vai (1) reunir as constatações de inventário, exposição, acesso, segmentação e monitoramento num relatório de risco; (2) priorizar pela consequência clínica e pela probabilidade; e (3) apresentá-lo aos gestores do hospital.

### 12.1 Estrutura

Escopo e método; sistemas no escopo, com os responsáveis; constatações, cada uma com evidência; classificação de risco; ações recomendadas, com responsáveis e datas; risco residual que o hospital aceita. Mantenha-o em poucas páginas, com um apêndice para as evidências.

Escreva primeiro o escopo, nomeando quais sistemas foram revisados e quais não foram, para que os leitores saibam o que o relatório cobre. Cada constatação deve apontar para a sua evidência no apêndice, e cada ação para um responsável. A parte do risco residual deve dizer quem o aceitou, conforme decidido pelos gestores do hospital.

### 12.2 Classificação

Classifique a consequência (dano ao paciente, perda de serviço) e a probabilidade (exposição, facilidade, atividade conhecida) em escalas simples de três níveis, combinadas com a manutenção e os líderes clínicos. Uma probabilidade média com consequência grave para o paciente normalmente fica acima de uma probabilidade alta com consequência menor.

Combine as escalas antes de classificar qualquer constatação e escreva uma frase explicando cada nível, para que leitores diferentes as apliquem da mesma forma. No Millbrook, o controlador dos elevadores teve consequência alta e probabilidade média, o que o colocou no topo da lista. As classificações devem ser revistas quando as evidências mudarem.

### 12.3 Recomendações

Cada uma nomeia uma mudança específica, um responsável, uma data e como a conclusão será demonstrada. Inclua ganhos rápidos (fechar exposições, remover ferramentas remotas antigas) e projetos mais longos (substituir equipamentos sem suporte).

No Millbrook, as recomendações incluíram a substituição do LIFT-CTRL e uma verificação semanal das contas do gateway. Cada uma foi escrita com um responsável, uma data e a evidência que mostraria a conclusão, como um pedido de compra ou um relatório semanal de contas. Recomendações vagas e sem responsáveis raramente levam a mudanças. Separe na lista os ganhos rápidos dos projetos.

### 12.4 Apresentar

Comece pelos três principais riscos em termos de pacientes; mostre o que já melhorou; peça decisões, não admiração.

Mantenha a apresentação curta, com um slide por risco principal e um slide de melhorias. Leve o apêndice de evidências caso os gestores perguntem, mas não o apresente. Termine com as decisões específicas necessárias, como o financiamento para substituir o LIFT-CTRL, e confirme quem vai agir em cada decisão. Envie os slides depois, com o resumo, para que os gestores ausentes vejam as mesmas decisões e responsáveis.

### 12.5 Apêndice de evidências

Para cada constatação, guarde a fotografia, o trecho de registro ou o excerto de configuração que a sustenta, com a data e quem o coletou. Os gestores raramente leem o apêndice, mas os auditores e o próximo analista vão ler, e ele permite a qualquer pessoa verificar que a constatação era real.

Guarde o apêndice com controles de acesso, porque ele contém detalhes sobre dispositivos, endereços e fraquezas. Ligue cada item ao número da sua constatação e registre onde a evidência original está guardada. Uma constatação sem item de apoio deve ser marcada como não confirmada até que a evidência seja coletada.

### 12.6 Depois da reunião

Registre as decisões tomadas, os responsáveis e as datas no registro de acompanhamento, envie um resumo de uma página aos participantes e agende a revisão de seis meses. O progresso das ações vira o slide de abertura da próxima vez, o que mantém a atenção na mudança, e não em novas constatações.

Verifique na revisão de seis meses se cada ação foi concluída e atualize as classificações onde as evidências mudaram. As ações que atrasaram precisam de uma nova data e de um motivo. Mantenha o resumo curto, para que os participantes o leiam, e arquive-o com o relatório.

### Exemplo resolvido (Millbrook sintético)

O relatório de Aisha lista: (1) LIFT-CTRL sem suporte e com conexão celular — consequência alta (transferências de pacientes), probabilidade média; (2) contas residuais de empreiteiros não desabilitadas depois das sessões — consequência alta, probabilidade média; (3) registros de tendências guardados por apenas 14 dias — consequência média, probabilidade alta. Já corrigidos: exposição do BACnet à internet, BMS-WS em dupla conexão, senha padrão do DOOR-SRV. Os gestores aprovam o financiamento para substituir o LIFT-CTRL no próximo ano e uma verificação semanal das contas do gateway.

> **Caso sintético — Millbrook.** O relatório e as classificações são inventados.

### Erros e limites

Um relatório reflete as evidências disponíveis na sua data; agende uma revisão. Ele não é uma avaliação formal segundo a IEC 62443.

### Exercícios

- **EX056 — Seções do relatório.** Liste as seis seções do relatório de risco. *Rubrica:* 3 = escopo/método, sistemas/responsáveis, constatações/evidências, classificação, ações, risco residual; 2 = quatro; 1 = duas; 0 = nenhum.
- **EX057 — Ordenar dois riscos.** Ordene "retenção de tendências do BMS de 14 dias" e "elevador sem suporte com conexão celular" e justifique. *Rubrica:* 3 = elevador primeiro; a consequência para a transferência de pacientes supera a da perda de evidências; 2 = ordem certa; 1 = invertida; 0 = nenhum.
- **EX058 — Escrever uma recomendação.** Escreva uma recomendação completa para as contas residuais de empreiteiros. *Rubrica:* 3 = mudança específica, responsável, data, evidência de conclusão; 2 = três; 1 = vaga; 0 = nenhum.
- **EX059 — Abrir a apresentação.** Escreva a frase de abertura da apresentação de Aisha aos gestores. *Rubrica:* 3 = risco principal em termos de pacientes, com o pedido; 2 = clara, mas técnica; 1 = jargão; 0 = nenhum.
- **EX060 — Risco residual.** Dê um risco residual que o Millbrook precisa aceitar até o próximo ano e explique por que ele é aceitável. *Rubrica:* 3 = LIFT-CTRL até a substituição, com os controles compensatórios nomeados; 2 = só o risco; 1 = nenhum aceito; 0 = nenhum.

### Síntese

Um relatório curto, com evidências, ordenado pela consequência e com ações com dono transforma constatações em mudanças financiadas.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 12

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. O Millbrook Hospital Building Systems, Aisha Bello e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** As unidades de tratamento de ar controlam a temperatura, a umidade e a pressão dos centros cirúrgicos; os chillers fornecem água gelada; os painéis de alarme de gases medicinais avisam de falhas na pressão dos gases; os controladores dos elevadores movem as cabines entre andares; o controle de acesso tranca e destranca as portas restritas.

**EX002.** Quando o controlador da unidade de tratamento de ar entra na rede, qualquer pessoa que o alcance pode alterar velocidades dos ventiladores ou valores de referência a partir de uma tela longe da casa de máquinas. Um centro cirúrgico poderia perder o controle de pressão ou de temperatura sem que ninguém tocasse na unidade.

**EX003.** A pressão positiva mantém o ar não filtrado do corredor fora do campo estéril; perdê-la aumenta o risco de infecção do sítio cirúrgico e pode obrigar a adiar a cirurgia.

**EX004.** A equipe da enfermaria não saberia que a pressão do oxigênio caiu, então pacientes que dependem do oxigênio canalizado poderiam sofrer dano antes que alguém percebesse e passasse para os cilindros.

**EX005.** Os sistemas prediais muitas vezes ficam entre a manutenção, os empreiteiros e a TI, então ninguém corrige, monitora ou revisa os acessos; nomear um responsável torna possível cada controle posterior.

**EX006.** Reiniciar o controlador da AHU-OT1 para carregar uma correção durante uma lista de cirurgias pararia o suprimento de ar e o controle de pressão com um paciente aberto na mesa.

**EX007.** O oxigênio em cilindros substitui o suprimento canalizado de gases medicinais; as chaves manuais substituem o controle de acesso eletrônico; a refrigeração portátil substitui a climatização e os chillers.

**EX008.** A pessoa autorizada para gases medicinais, trabalhando dentro do sistema de permissões da manutenção, controla qualquer trabalho nos sistemas de gases medicinais, incluindo o painel de alarme.

**EX009.** Alcançar alguns controladores significa abrir painéis do forro ou da parede dentro ou perto de uma área limpa, o que pode soltar poeira e contaminar o centro cirúrgico, a menos que o controle de infecção combine o momento e as precauções.

**EX010.** Se os cilindros, as chaves manuais e a refrigeração portátil conseguem manter as enfermarias seguras, Aisha pode mostrar que desconectar a rede do BMS deixa os pacientes atendidos, o que torna a decisão aceitável para os gestores clínicos.

**EX011.** Na camada de campo, sensores e atuadores são ligados por fios aos controladores locais; na camada de supervisão, esses controladores se comunicam entre si e com o servidor e a estação de trabalho do BMS pela rede predial.

**EX012.** Normalmente consegue ler todos os pontos e muitas vezes escrever valores de referência ou comandos, porque as instalações clássicas de BACnet/IP não autenticam o remetente.

**EX013.** A BMS-WS liga a VLAN corporativa diretamente à VLAN 300 sem passar por um firewall, então um malware ou um atacante na estação de trabalho ganha alcance a todos os controladores prediais.

**EX014.** A BMS-WS em dupla conexão, a conexão de acesso remoto do empreiteiro e a conexão celular do fabricante dos elevadores.

**EX015.** Alguns controladores antigos falham quando sofrem varreduras, o que poderia parar a ventilação em áreas clínicas; e os desenhos, somados à configuração dos switches, dão o mesmo quadro sem tocar nos equipamentos em operação.

**EX016.** Sistema, nome do dispositivo, localização, responsável, versão do firmware, situação de suporte do fornecedor, endereço de rede e consequência clínica da falha.

**EX017.** Ele imprime `UNSUPPORTED BOILER-2   system=HVAC installed=2010`, e a linha de HVAC passa a ser `HVAC               4 device(s): AHU-OT1, AHU-OT2, CHILLER-1, BOILER-2`.

**EX018.** O fornecedor do chiller não vai publicar correções para as fraquezas descobertas daqui em diante, então o risco dele cresce com o tempo; precisamos protegê-lo de outras formas e planejar a sua substituição.

**EX019.** Colocar o LIFT-CTRL no seu próprio segmento de rede, alcançável apenas pelo seu gateway de manutenção; restringir ou remover a conexão celular, a menos que usada sob chamado; monitorar as suas conexões; programar a substituição no plano de bens de capital.

**EX020.** A pessoa autorizada para gases medicinais, porque o sistema de alarme de gases medicinais é dela.

**EX021.** Se essa única senha vazar, ou se um engenheiro que a conhecia sair em maus termos, todos os hospitais atendidos pelo integrador ficam abertos de uma vez.

**EX022.** O registro de auditoria ou de tendências do BMS registra qual conta nominal fez a mudança, então o hospital pode perguntar a essa pessoa o motivo e separar depressa um erro de um mau uso.

**EX023.** "Cada dispositivo sai de fábrica com uma senha única ou obriga a definir uma na configuração inicial?" "Vocês publicam uma política e um contato para divulgação de vulnerabilidades?" "Por quantos anos vocês fornecerão atualizações de segurança, e a comunicação é criptografada?"

**EX024.** Trocar todas as senhas que esse engenheiro conhecia, com os novos valores guardados no cofre; revisar quais contas e acessos remotos ele tinha e desabilitá-los; registrar a mudança.

**EX025.** IEC 62443-4-2, porque ela define requisitos de segurança para componentes de sistemas de automação e controle industrial, que é o que os controladores do BMS são.

**EX026.** Um empreiteiro redireciona uma porta para que a página web do BMS funcione de casa; uma regra de firewall de projeto continua ativa depois do fim do comissionamento.

**EX027.** `203.0.113.10:22 ... NOT APPROVED - report` para o novo item, e o total passa a ser `unapproved: 3`, já que apenas a porta 443 desse endereço está aprovada.

**EX028.** T0883 Internet Accessible Device.

**EX029.** Relatar à equipe de redes e à manutenção; fazer o responsável fechá-la por meio de uma mudança emergencial; revisar os registros em busca de conexões externas; descobrir quem a abriu e por quê; dar a essa parte acesso pelo gateway em troca.

**EX030.** Ela não tem autorização para sistemas que não pertencem ao Millbrook; sondá-los poderia violar a lei e perturbar os equipamentos de outro hospital.

**EX031.** O gateway de acesso remoto do hospital; uma ferramenta de área de trabalho remota na BMS-WS; a conexão celular do elevador; o roteador do fornecedor do chiller.

**EX032.** Dar aos engenheiros do empreiteiro do BMS contas individuais no gateway com autenticação multifator e revisar os registros de sessão do gateway depois de cada visita de suporte.

**EX033.** Cada empreiteiro precisa apenas do seu próprio sistema; limitar a conta significa que uma senha roubada do empreiteiro do chiller não consegue abrir as portas da farmácia ou da maternidade.

**EX034.** Se a ferramenta antiga for removida primeiro e a conta do gateway falhar, o empreiteiro não poderia ajudar durante uma falha dos equipamentos; testar antes a substituta mantém o suporte contínuo.

**EX035.** Não — o monitoramento do alarme de incêndio é uma função de segurança da vida; documentar a conexão, confirmar com o responsável pela segurança contra incêndio que ela só alcança a central de monitoramento e revisá-la, em vez de desconectá-la.

**EX036.** Uma zona do BMS; uma zona do alarme de gases medicinais e uma zona dos elevadores (relevantes para a segurança física); uma zona de controle de acesso; uma DMZ; a zona corporativa.

**EX037.** "Servidor do BMS → servidor de dados da DMZ na porta de exportação combinada, permitir", com o "qualquer → qualquer negar" final pegando tudo o que não está listado.

**EX038.** Eles abrem um painel somente leitura no servidor de dados da DMZ ou, para mudanças, conectam-se pelo gateway a um host de salto dentro da zona do BMS.

**EX039.** Confirmar com a manutenção se os pontos perdidos afetam áreas clínicas, restaurar a configuração anterior se afetarem, identificar o conduto ausente (aqui, um servidor de horário) e acrescentá-lo sob o mesmo registro de mudança.

**EX040.** Ela não impede que alguém usando credenciais válidas do gateway, ou uma pessoa interna, cause dano dentro dos condutos permitidos.

**EX041.** O script só sinaliza uma mudança cujo horário cai fora das 08:00–10:00, e 09:00 está dentro dessa janela.

**EX042.** `03:00 setpoint 20.0->26.0 in window` e `09:00 setpoint 26.0->21.0 OUTSIDE WINDOW - review`.

**EX043.** O registro de auditoria do BMS, o registro do gateway de acesso remoto e o registro do firewall da zona do BMS.

**EX044.** O centro cirúrgico estaria fora da sua faixa de temperatura quando a lista da manhã começasse, então a cirurgia poderia ser adiada até as condições se recuperarem, e o conforto da equipe e as condições de esterilidade ficariam comprometidos.

**EX045.** Exigir que toda mudança fora da janela seja escrita no livro do turno com o motivo e configurar um alarme do BMS para o engenheiro de plantão quando um valor de referência crítico mudar fora da janela.

**EX046.** Temos o produto? Estamos rodando uma versão afetada? A fraqueza pode ser alcançada da forma que o alerta descreve?

**EX047.** Registrar que se aplica e não pode ser corrigido, manter o LIFT-CTRL isolado apenas com a sua rota de manutenção, monitorar as suas conexões e aumentar a prioridade da sua substituição no plano de bens de capital.

**EX048.** Durante a interrupção de 30 minutos, as agendas eletrônicas das portas podem não funcionar, então os gerentes das enfermarias precisam de chaves para manter as portas da farmácia e da maternidade ao mesmo tempo seguras e utilizáveis.

**EX049.** "Alerta: contorno de autenticação na web do DOOR-SRV, v4.1 (a nossa). Decisão: mitigar e depois corrigir. Mitigação: interface limitada à estação de trabalho da sala de segurança. Correção 4.2 no domingo às 06:00, com chaves manuais. Responsável: líder de sistemas de segurança da manutenção. Revisar depois da correção."

**EX050.** Pedir ao dono da rede que mostre a regra e, num teste combinado, confirmar que a página web abre a partir da estação de trabalho da sala de segurança e falha a partir de outro host da zona de controle de acesso.

**EX051.** "Alguma área clínica está insegura agora?" — respondida pelo gestor clínico de plantão junto com a manutenção, antes de qualquer ação técnica.

**EX052.** Os controladores de campo guardam os seus próprios programas e agendas e continuam operando as unidades de tratamento de ar sem o servidor ou a estação de trabalho do BMS; o firewall só impediu os comandos vindos de fora da zona.

**EX053.** Rondas da manutenção de hora em hora lendo os mostradores locais nas casas de máquinas, e as equipes das enfermarias e dos centros cirúrgicos observando os alarmes locais, incluindo os painéis de gases medicinais.

**EX054.** Depois da reconstrução, a equipe de redes reabilita um conduto de cada vez, e a manutenção compara cada ponto crítico do BMS com as leituras locais antes de o próximo conduto ser restaurado.

**EX055.** Alguns controladores voltam a padrões como ventiladores em velocidade fixa ou dampers fechados quando perdem o servidor, o que poderia perturbar a pressão do centro cirúrgico, então a recomendação precisa levar esse comportamento em conta.

**EX056.** Escopo e método; sistemas no escopo e responsáveis; constatações com evidências; classificação de risco; ações recomendadas com responsáveis e datas; risco residual aceito.

**EX057.** O elevador vem primeiro: se for mal utilizado ou falhar, as transferências de pacientes entre andares atrasam, um dano clínico direto, enquanto a retenção curta das tendências enfraquece principalmente as investigações.

**EX058.** "As contas do gateway são desabilitadas automaticamente ao fim de cada sessão com chamado; responsável: líder da equipe de redes; até o fim do próximo mês; evidência: relatório semanal mostrando nenhuma conta de empreiteiro habilitada fora de chamados abertos."

**EX059.** "Os nossos elevadores levam pacientes entre os centros cirúrgicos e as enfermarias, e o controlador deles já não pode ser corrigido; pedimos que vocês financiem a sua substituição no próximo ano."

**EX060.** O LIFT-CTRL continua em serviço até a substituição; isso é aceitável porque ele está isolado na sua própria zona, a sua conexão celular está restrita à central de serviços do empreiteiro, sob chamados, e as suas conexões são monitoradas.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; verifique novamente as edições antes de citar.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0883 Internet Accessible Device, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
