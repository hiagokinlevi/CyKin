# Arquitetura e Engenharia de Segurança: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 053, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–18 de 18 têm texto didático escrito à mão; os exercícios EX001–EX072 têm resoluções correspondentes com rubricas de 0 a 3; os cinco laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente e a verificação de 300 páginas A4 continuam em aberto.
- Público: alunos de curso técnico que vão configurar, verificar e manter controles de segurança em organizações pequenas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios conferem resultados de backup, testam regras de firewall, simulam a alcançabilidade, comparam configurações com uma baseline e comparam regras de login, sempre sobre dados sintéticos em modelos isolados; nada toca uma rede real e nenhum malware é usado. Projetos de produção usam produtos e normas avaliados; nunca crie sua própria criptografia. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma aluna de curso técnico em estágio num grupo de cinco clínicas odontológicas: serviços, redes, contas e scripts; escopo e evidências; modelo do sistema, telemetria, modos de falha, métodos, configuração e verificação; um laboratório isolado; solução de problemas, automação e dependências; documentação, um segundo laboratório e uma implantação supervisionada. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Nadia Kowalczyk** | Aluna do curso técnico | Inventada |
| **Daniel Mercer** | Instrutor | Inventado |
| **Grace Mwangi** | Gerente de TI da Linden | Inventada |
| **Harbourside Technical College** | Escola técnica fictícia | Inventada |
| **Linden Dental Group** | Grupo fictício de cinco clínicas odontológicas | Inventado |

### Fontes principais

NIST [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); Shostack, *Threat Modeling* (2014). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Computação e arquitetura de serviços

### Objetivos de aprendizagem

Você vai (1) descrever como os serviços de uma pequena organização se encaixam; (2) mapear os serviços para os sistemas que os hospedam; (3) identificar quais serviços são mais críticos.

### 1.1 Os serviços das clínicas

Nadia Kowalczyk é aluna de curso técnico no fictício Harbourside Technical College e faz estágio no fictício Linden Dental Group, que mantém cinco clínicas odontológicas. Seu instrutor, Daniel Mercer, pede que ela comece listando serviços, e não dispositivos. Os serviços da Linden incluem agendamento de consultas, prontuários dos pacientes, imagens de raio X digitais, pagamentos com cartão, e-mail e a escala da equipe. Cada serviço é algo que as pessoas usam para fazer o trabalho. Pensar primeiro nos serviços ajuda Nadia a ver por que cada dispositivo importa, porque um dispositivo só é importante pelos serviços que sustenta.

### 1.2 Dos serviços aos sistemas

Nadia mapeia cada serviço para os sistemas que o hospedam. Os prontuários rodam num sistema de gestão clínica em nuvem acessado pelo navegador. As imagens usam um servidor de imagens local em cada clínica, conectado aos sensores nos consultórios. Os pagamentos usam maquininhas de cartão de um provedor de pagamentos. O e-mail é um serviço em nuvem. A escala é uma planilha num drive compartilhado. Grace Mwangi, gerente de TI da Linden, confere o mapa e acrescenta um appliance de backup no escritório central que copia o servidor de imagens de cada clínica toda noite.

### 1.3 O que é crítico

Nadia pergunta aos gerentes das clínicas qual indisponibilidade pararia o trabalho. Sem os prontuários, os dentistas não conseguem ver o histórico de tratamento e as consultas emperram. Sem as imagens, muitos tratamentos não podem seguir com segurança. Os pagamentos podem recorrer a anotar os dados do cartão e cobrar depois por telefone com o provedor. A escala pode ser impressa. Ela classifica prontuários e imagens como críticos, pagamentos como importantes e o resto como de apoio. A classificação diz a Grace onde gastar seu tempo limitado em resiliência e proteção, e dá a Nadia uma moldura para todos os capítulos seguintes.

### Exemplo resolvido

Nadia lista seis serviços, mapeia-os para os sistemas que os hospedam com a correção de Grace e classifica prontuários e imagens como críticos.

> **Caso sintético.** A Linden, o Harbourside e todas as pessoas são sintéticos.

### Erros e limites

As listas de serviços deixam de fora ferramentas informais. Os gerentes podem exagerar as próprias necessidades.

### Exercícios

- **EX001 — Serviços primeiro.** Por que listar os serviços antes dos dispositivos? *Rubrica:* 3 = um dispositivo só importa pelos serviços que sustenta;; 2 = propósito;; 1 = nenhuma;; 0 = nenhuma.

- **EX002 — Acréscimo de Grace.** O que Grace acrescentou ao mapa? *Rubrica:* 3 = um appliance de backup no escritório central que copia os servidores de imagens toda noite;; 2 = backup;; 1 = nenhuma;; 0 = nenhuma.

- **EX003 — Contingência dos pagamentos.** Por que os pagamentos não são classificados como críticos? *Rubrica:* 3 = podem recorrer a anotar os dados do cartão e cobrar depois por telefone;; 2 = contingência;; 1 = sem importância;; 0 = nenhuma.

- **EX004 — Serviços críticos.** Que serviços são críticos? *Rubrica:* 3 = prontuários e imagens;; 2 = os dois;; 1 = e-mail;; 0 = nenhuma.

### Síntese

Mapear serviços para sistemas e classificá-los por impacto mostra onde a proteção importa mais.

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) descrever a rede de uma clínica; (2) explicar os principais protocolos em uso; (3) encontrar configurações de rede que enfraquecem a segurança.

### 2.1 A rede da clínica

Nadia esboça uma clínica típica da Linden. Um roteador se conecta à internet e oferece rede sem fio para a equipe e uma rede separada de visitantes para os pacientes. Um switch conecta os PCs da recepção, os PCs dos consultórios, o servidor de imagens, os sensores de raio X e as impressoras. As maquininhas de cartão se conectam pela rede cabeada ao provedor de pagamentos. Cada clínica tem uma VPN site a site com o escritório central para os backups. Desenhar a rede a ajuda a ver que os dispositivos dos consultórios e os PCs da recepção compartilham uma única rede plana, de modo que qualquer PC infectado consegue alcançar diretamente o servidor de imagens.

### 2.2 Protocolos em uso

Daniel pede a Nadia que identifique os protocolos. Os navegadores usam HTTPS para chegar ao sistema de gestão clínica. O servidor de imagens compartilha arquivos usando SMB, um protocolo de compartilhamento de arquivos do Windows. As maquininhas de cartão usam conexões criptografadas definidas pelo provedor de pagamentos. O DHCP distribui os endereços, e o DNS resolve os nomes. Os backups trafegam pela VPN usando IPsec. Conhecer os protocolos permite que ela faça as perguntas certas, como qual versão do SMB o servidor de imagens usa, porque as versões antigas têm fraquezas bem conhecidas exploradas por ransomware. Ela registra cada protocolo e sua porta no esboço da rede.

### 2.3 Configurações fracas

Nadia confere as configurações com a permissão de Grace. O servidor de imagens ainda permite o SMB versão 1, a página de administração do roteador é alcançável a partir da rede sem fio de visitantes e as impressoras têm senhas padrão. Grace desativa o SMB versão 1 depois de confirmar que o software de imagens não precisa mais dele, restringe a administração do roteador à rede da equipe e troca as senhas das impressoras. Nadia registra cada mudança. Ela observa que a rede plana continua sendo o maior problema e precisa de um reprojeto planejado, e não de uma correção rápida, ao qual ela voltará mais tarde.

### Exemplo resolvido

Nadia esboça a rede de uma clínica, lista os protocolos em uso e encontra três configurações fracas que Grace corrige, deixando a rede plana para reprojeto.

> **Caso sintético.** Os detalhes da rede são sintéticos.

### Erros e limites

Software antigo pode precisar de protocolos antigos. Mudanças no roteador podem interromper as maquininhas de cartão se feitas sem cuidado.

### Exercícios

- **EX005 — Risco da rede plana.** Por que a rede plana da clínica é um risco? *Rubrica:* 3 = qualquer PC infectado consegue alcançar o servidor de imagens;; 2 = propagação;; 1 = nenhuma;; 0 = nenhuma.

- **EX006 — Pergunta sobre o SMB.** Por que perguntar qual versão do SMB o servidor de imagens usa? *Rubrica:* 3 = versões antigas têm fraquezas exploradas por ransomware;; 2 = ransomware;; 1 = nenhuma;; 0 = nenhuma.

- **EX007 — Correção do roteador.** Como a administração do roteador foi restringida? *Rubrica:* 3 = à rede da equipe, e não à rede de visitantes;; 2 = só equipe;; 1 = nenhuma;; 0 = nenhuma.

- **EX008 — Problema maior.** Que problema precisa de um reprojeto planejado? *Rubrica:* 3 = a rede plana;; 2 = rede plana;; 1 = impressoras;; 0 = nenhuma.

### Síntese

Entender uma rede e os seus protocolos revela configurações fracas que podem ser corrigidas e questões de desenho que exigem planejamento.

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem

Você vai (1) revisar as contas de usuário dos PCs das clínicas; (2) aplicar o menor privilégio; (3) configurar com segurança o login em dispositivos compartilhados.

### 3.1 Revisar as contas

Nadia revisa as contas dos PCs da recepção e dos consultórios. A maioria dos PCs entra automaticamente numa conta compartilhada da clínica que tem direitos de administrador local. Os dentistas e os auxiliares então entram no sistema de gestão clínica em nuvem com contas pessoais. A conta compartilhada do Windows significa que qualquer coisa baixada roda com direitos totais, e não há registro de quem usou cada PC. Grace explica que isso foi configurado anos atrás para que a equipe ocupada pudesse começar a trabalhar rapidamente. Nadia documenta o risco e o motivo, porque os dois importam para uma correção.

### 3.2 Menor privilégio

Nadia propõe retirar os direitos de administrador da conta compartilhada e manter uma conta de administrador separada, usada apenas por Grace para a manutenção. Ela testa o visualizador de imagens e o software de odontograma com uma conta padrão num PC. Um programa de odontograma mais antigo não consegue salvar as configurações sem direitos de administrador; o fornecedor oferece uma correção de configuração que concede direitos apenas à pasta do próprio programa. O menor privilégio geralmente funciona depois de pequenos ajustes, e testar primeiro num PC evita interromper uma clínica inteira.

### 3.3 Login em dispositivos compartilhados

Os PCs dos consultórios são usados por várias pessoas a cada dia. Nadia sugere contas individuais do Windows com login rápido por PIN ou crachá e bloqueio automático após cinco minutos de inatividade. Grace faz um piloto numa clínica. A equipe reclama no começo e depois se adapta, quando o login passa a levar menos de cinco segundos. Contas individuais significam que, se um PC for usado indevidamente, o registro mostra quem estava conectado. Nadia observa que a conveniência é um requisito de segurança nas clínicas, porque controles lentos são contornados. A clínica do piloto anota os problemas para a implantação mais ampla.

### Exemplo resolvido

Nadia revisa uma conta de administrador compartilhada, retira os direitos de administrador com uma correção do fornecedor para um programa e pilota o login individual rápido.

> **Caso sintético.** As contas e o software são sintéticos.

### Erros e limites

Métodos de login rápido precisam de tratamento para crachás perdidos. As correções dos fornecedores podem mudar com as atualizações.

### Exercícios

- **EX009 — Risco da conta compartilhada.** Por que a conta de administrador compartilhada é arriscada? *Rubrica:* 3 = os downloads rodam com direitos totais e não há registro dos usuários;; 2 = direitos e responsabilização;; 1 = nenhuma;; 0 = nenhuma.

- **EX010 — Correção do odontograma.** Como o programa de odontograma foi corrigido? *Rubrica:* 3 = uma configuração do fornecedor que concede direitos só à própria pasta;; 2 = direitos na pasta;; 1 = direitos de administrador;; 0 = nenhuma.

- **EX011 — Tempo de bloqueio.** Depois de quanto tempo os PCs dos consultórios bloqueiam? *Rubrica:* 3 = cinco minutos de inatividade;; 2 = cinco;; 1 = nenhuma;; 0 = nenhuma.

- **EX012 — Conveniência.** Por que a conveniência é um requisito de segurança nas clínicas? *Rubrica:* 3 = controles lentos são contornados;; 2 = contornar;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Eliminar as contas administrativas compartilhadas e oferecer um login individual rápido melhora tanto a segurança quanto a responsabilização.

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem

Você vai (1) ler exportações em CSV e JSON; (2) escrever um script para conferir os resultados dos backups; (3) tratar dados ruins com segurança.

### 4.1 Formatos de dados

Os sistemas da Linden exportam dados em formatos diferentes. O appliance de backup grava um arquivo CSV toda noite, com uma linha por clínica: data, nome da clínica, arquivos copiados e status. A exportação de auditoria do sistema de gestão clínica é em JSON, um formato de chaves e valores aninhados. Nadia aprende a ler os dois com a biblioteca padrão do Python. Daniel explica que entender os formatos é uma habilidade técnica central, porque a maioria das verificações de segurança começa lendo a exportação de algum sistema e transformando-a numa resposta clara. Ela guarda arquivos de exemplo de cada formato para testar seus scripts.

### Laboratório — Conferência de uma semana de resultados de backup

```python
# Check a week of nightly backup results (synthetic CSV rows: date, practice, files, status).
rows = """2026-03-01,Elmfield,4120,ok
2026-03-02,Elmfield,4133,ok
2026-03-03,Elmfield,0,disk full
2026-03-04,Elmfield,4150,ok
2026-03-05,Elmfield,4161,ok
2026-03-06,Elmfield,0,disk full
2026-03-07,Elmfield,0,disk full
2026-03-01,Norbury,2210,ok
2026-03-02,Norbury,2215,ok
2026-03-03,Norbury,2219,ok
2026-03-04,Norbury,2224,ok
2026-03-05,Norbury,2230,ok
2026-03-06,Norbury,2233,ok
2026-03-07,Norbury,2241,ok
2026-03-07,Westcott,3100""".splitlines()
summary, unreadable = {}, 0
for r in rows:
    f = r.split(",")
    if len(f) != 4: unreadable += 1; continue
    d, p, _, s = f
    ok, n, last = summary.get(p, (0, 0, "never"))
    summary[p] = (ok + (s == "ok"), n + 1, d if s == "ok" else last)
for p, (ok, n, last) in sorted(summary.items()):
    print(f"{p}: {ok}/{n} nights ok, last success {last}" + ("  <-- CHECK" if ok < n else ""))
print(f"unreadable rows: {unreadable}")
```

Execute com `python3 lab_backups.py`. Saída verificada:

```text
Elmfield: 4/7 nights ok, last success 2026-03-05  <-- CHECK
Norbury: 7/7 nights ok, last success 2026-03-07
unreadable rows: 1
```

### 4.2 Uma verificação de backups

Nadia escreve um script que lê uma semana de resultados sintéticos de backup e relata, para cada clínica, quantas noites tiveram sucesso e a data do último sucesso. O laboratório mostra que a clínica de Elmfield falhou em três noites, incluindo as duas últimas. Grace não tinha percebido porque o appliance só envia e-mail quando há sucesso. O script de Nadia transforma uma falha silenciosa numa falha visível. Grace encontra um disco cheio no servidor de imagens de Elmfield e libera espaço, e o backup da noite seguinte tem sucesso.

### 4.3 Dados ruins

Daniel pergunta o que acontece se faltar um campo numa linha ou se um status estiver escrito errado. Nadia acrescenta verificações: as linhas com campos faltando são relatadas como ilegíveis, em vez de ignoradas, e qualquer status diferente de "ok" conta como falha. Tratar valores desconhecidos como falhas é mais seguro do que tratá-los como sucesso, porque um script de monitoramento que esconde problemas é pior do que nenhum. Ela também registra no topo do arquivo o formato esperado pelo script, para que os futuros usuários saibam o que ele pressupõe.

### Exemplo resolvido

Nadia lê exportações em CSV e JSON, escreve uma verificação de backups que encontra três falhas em Elmfield e trata com segurança as linhas ruins.

> **Caso sintético.** As clínicas e os resultados são sintéticos.

### Erros e limites

Os scripts quebram quando os formatos de exportação mudam. Os e-mails de sucesso criam falso conforto.

### Exercícios

- **EX013 — Falha silenciosa.** Por que Grace não tinha percebido as falhas de Elmfield? *Rubrica:* 3 = o appliance só enviava e-mail quando havia sucesso;; 2 = e-mails de sucesso;; 1 = nenhuma;; 0 = nenhuma.

- **EX014 — Resultado do laboratório.** O que o laboratório relatou para Elmfield? *Rubrica:* 3 = 4 de 7 noites ok, último sucesso em 2026-03-05;; 2 = três falhas;; 1 = nenhuma;; 0 = nenhuma.

- **EX015 — Status desconhecido.** Por que tratar valores de status desconhecidos como falhas? *Rubrica:* 3 = esconder problemas é pior do que não monitorar;; 2 = padrão seguro;; 1 = sucesso;; 0 = nenhuma.

- **EX016 — Causa raiz.** O que causou as falhas de Elmfield? *Rubrica:* 3 = um disco cheio no servidor de imagens;; 2 = disco;; 1 = rede;; 0 = nenhuma.

### Síntese

Ler exportações com pequenos scripts torna visíveis as falhas silenciosas, desde que os dados ruins sejam tratados com cautela.

<a id="ch-05"></a>

## Capítulo 5 — Escopo e evidências de segurança

### Objetivos de aprendizagem

Você vai (1) definir o escopo de uma revisão de segurança; (2) coletar evidências de forma adequada; (3) separar achados de opiniões.

### 5.1 Definir o escopo

Grace pede a Nadia que revise a segurança da clínica de Elmfield. Antes de começar, Nadia escreve um escopo: a rede da clínica, os PCs, o servidor de imagens, o roteador e as maquininhas de cartão; ficam excluídos o sistema de gestão clínica em nuvem, que o fornecedor administra, e os sistemas do provedor de pagamentos. Ela lista o que pode fazer: ler configurações, entrevistar a equipe e executar verificações aprovadas, mas não testar ataques. Grace assina o escopo. Um escopo escrito protege quem revisa, alinha as expectativas e impede que o trabalho deslize para sistemas em que ela não tem permissão para mexer.

### 5.2 Coletar evidências

Para cada verificação, Nadia registra o que examinou, quando, como e o que encontrou, com capturas de tela ou configurações exportadas. Ela anota a versão do firmware do roteador, os compartilhamentos abertos do servidor de imagens e o status de atualização dos PCs. Quando uma recepcionista diz que as senhas ficam num post-it, Nadia registra isso como uma declaração e confere ela mesma, pedindo para ver o balcão da recepção. Evidências que outras pessoas podem verificar são a base de uma revisão crível, e registrar as fontes facilita resolver discordâncias posteriores.

### 5.3 Achados e opiniões

O relatório de Nadia separa os achados, que são fatos apoiados em evidências, das opiniões, que são o julgamento dela sobre risco e prioridade. Um achado: o servidor de imagens compartilha uma pasta legível por todos na rede. Uma opinião: essa é a maior prioridade, porque as imagens são críticas e a rede é plana. Mantê-los separados permite que Grace confira os fatos e depois pondere o julgamento por conta própria. Daniel observa que os revisores perdem a confiança quando as opiniões são apresentadas como fatos, mesmo que as opiniões sejam razoáveis.

### Exemplo resolvido

Nadia escreve um escopo assinado para Elmfield, coleta evidências verificáveis e separa achados de opiniões no relatório.

> **Caso sintético.** A revisão é sintética.

### Erros e limites

Os escopos podem excluir justamente onde estão os problemas. As declarações precisam ser conferidas antes de virarem achados.

### Exercícios

- **EX017 — Exclusões.** O que o escopo excluiu? *Rubrica:* 3 = o sistema de gestão clínica em nuvem e os sistemas do provedor de pagamentos;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX018 — Não permitido.** O que Nadia não tinha permissão para fazer? *Rubrica:* 3 = testar ataques;; 2 = ataques;; 1 = entrevistas;; 0 = nenhuma.

- **EX019 — Post-it.** Como Nadia tratou a afirmação sobre o post-it? *Rubrica:* 3 = registrou-a como declaração e conferiu ela mesma;; 2 = verificar;; 1 = ignorou;; 0 = nenhuma.

- **EX020 — Exemplo de achado.** Dê um achado do relatório de Nadia. *Rubrica:* 3 = o servidor de imagens compartilha uma pasta legível por todos;; 2 = compartilhamento;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Um escopo assinado, evidências verificáveis e uma separação clara entre achados e opiniões tornam uma revisão crível.

<a id="ch-06"></a>

## Capítulo 6 — Arquitetura e engenharia de segurança: modelo do sistema

### Objetivos de aprendizagem

Você vai (1) modelar a clínica de Elmfield como zonas e fluxos; (2) marcar as fronteiras de confiança; (3) propor um projeto segmentado.

### 6.1 Zonas e fluxos

Nadia modela Elmfield como componentes e fluxos: PCs da recepção para o sistema clínico em nuvem, PCs dos consultórios para a nuvem e para o servidor de imagens, sensores de raio X para o servidor de imagens, servidor de imagens para os backups do escritório central, maquininhas de cartão para o provedor de pagamentos e visitantes para a internet. Ela desenha cada fluxo como uma seta rotulada com seu protocolo. O modelo mostra que as maquininhas de cartão e os sensores de raio X nunca precisam conversar com os PCs da recepção, mas a rede plana permite isso.

### 6.2 Fronteiras de confiança

Nadia marca as fronteiras: entre a clínica e a internet, entre a clínica e o escritório central, entre a rede de visitantes dos pacientes e as redes da equipe e em torno das maquininhas de pagamento, que o provedor de pagamentos exige que fiquem isoladas. Ela também marca uma fronteira em torno das imagens clínicas, porque a integridade das imagens afeta o diagnóstico. Cada fronteira precisa de um controle que permita apenas os fluxos listados. Marcar as fronteiras transforma a sensação vaga de que a rede é aberta demais em lugares específicos onde a filtragem deve ficar. Ela numera cada fronteira no diagrama, para que os capítulos e as listas de regras posteriores possam se referir a elas com precisão.

### 6.3 Um projeto segmentado

Nadia propõe quatro segmentos: PCs da equipe, imagens clínicas, maquininhas de pagamento e visitantes. O firewall do roteador permite apenas os fluxos modelados entre eles. Os PCs dos consultórios podem alcançar o servidor de imagens na porta do visualizador; nada mais pode. As maquininhas de cartão alcançam apenas o provedor de pagamentos. Grace revisa o projeto e pergunta se o roteador suporta redes separadas; ele suporta, usando LANs virtuais. O projeto de Nadia segue a ideia, descrita no NIST SP 800-207, de limitar a confiança implícita baseada na localização na rede, em escala adequada a um local pequeno.

### Exemplo resolvido

Nadia modela os fluxos de Elmfield, marca cinco fronteiras de confiança e propõe quatro segmentos com fluxos permitidos explícitos.

> **Caso sintético.** O modelo é sintético; o SP 800-207 é real.

### Erros e limites

Os modelos deixam de fora fluxos não documentados. Os recursos dos roteadores variam conforme o modelo.

### Exercícios

- **EX021 — Caminhos desnecessários.** Que dispositivos nunca precisam conversar com os PCs da recepção? *Rubrica:* 3 = maquininhas de cartão e sensores de raio X;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX022 — Fronteira das imagens.** Por que colocar uma fronteira em torno das imagens clínicas? *Rubrica:* 3 = a integridade das imagens afeta o diagnóstico;; 2 = integridade;; 1 = nenhuma;; 0 = nenhuma.

- **EX023 — Quatro segmentos.** Que quatro segmentos Nadia propôs? *Rubrica:* 3 = PCs da equipe, imagens clínicas, maquininhas de pagamento e visitantes;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

- **EX024 — Suporte do roteador.** Como o roteador suporta os segmentos? *Rubrica:* 3 = LANs virtuais;; 2 = VLANs;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Um modelo com fronteiras marcadas leva diretamente a um desenho segmentado com fluxos permitidos explícitos.

<a id="ch-07"></a>

## Capítulo 7 — Arquitetura e engenharia de segurança: dados e telemetria

### Objetivos de aprendizagem

Você vai (1) identificar os dados sensíveis numa clínica; (2) escolher a telemetria que vale a pena coletar; (3) proteger os próprios logs.

### 7.1 Dados sensíveis

Nadia lista onde ficam os dados dos pacientes em Elmfield: o sistema clínico em nuvem, as imagens de raio X no servidor de imagens, os planos de tratamento impressos, as cartas de encaminhamento no e-mail e os lembretes de consulta enviados por mensagem de texto. Os prontuários odontológicos são dados de saúde e precisam de proteção forte segundo as leis de proteção de dados. Ela observa que as imagens de raio X trazem o nome e a data de nascimento dos pacientes nos cabeçalhos dos arquivos. Saber onde ficam os dados sensíveis lhe diz quais sistemas precisam do controle de acesso, da criptografia e do backup mais fortes. Ela registra cada local numa tabela curta, com o responsável pelo sistema e as pessoas que podem acessá-lo.

### 7.2 Telemetria útil

Grace não consegue observar tudo. Nadia propõe coletar um pequeno conjunto de sinais: logins nos PCs e no sistema clínico em nuvem, ações de administradores, bloqueios do firewall entre segmentos, resultados de backup e alertas do antivírus. Cada sinal apoia uma pergunta que Grace pode precisar responder, como quem visualizou um prontuário ou se um malware tentou alcançar o servidor de imagens. Telemetria sem uma pergunta a responder vira ruído. Ela pergunta ao fornecedor da nuvem que logs de auditoria ele oferece e por quanto tempo os guarda.

### 7.3 Proteger os logs

Os logs podem conter informações sensíveis e podem ser alterados por um atacante que queira apagar seus rastros. Nadia recomenda enviar os logs dos PCs e do firewall para um serviço de logs em nuvem que a equipe das clínicas não consiga modificar, mantê-los por um ano e restringir o acesso a Grace e a um substituto. Ela confere se os relógios de todos os dispositivos se sincronizam com um servidor de horário, para que os eventos possam ser ordenados corretamente. Daniel observa que os logs são evidências, e as evidências precisam ser protegidas tanto da perda quanto da adulteração para merecerem confiança depois de um incidente.

### Exemplo resolvido

Nadia mapeia onde ficam os dados dos pacientes, seleciona cinco sinais de telemetria ligados a perguntas e protege os logs com armazenamento central, retenção e acesso restrito.

> **Caso sintético.** Os locais dos dados e os serviços são sintéticos.

### Erros e limites

Os logs de auditoria dos fornecedores podem ser limitados. O logging centralizado acrescenta custo e uma dependência.

### Exercícios

- **EX025 — Cabeçalhos das imagens.** Que dados sensíveis os cabeçalhos dos arquivos de raio X trazem? *Rubrica:* 3 = nome e data de nascimento dos pacientes;; 2 = identificadores;; 1 = nenhuma;; 0 = nenhuma.

- **EX026 — Regra da telemetria.** Por que ligar cada sinal a uma pergunta? *Rubrica:* 3 = telemetria sem pergunta vira ruído;; 2 = propósito;; 1 = nenhuma;; 0 = nenhuma.

- **EX027 — Destino dos logs.** Para onde devem ir os logs dos PCs e do firewall? *Rubrica:* 3 = um serviço de logs em nuvem que a equipe não consegue modificar;; 2 = central;; 1 = PC local;; 0 = nenhuma.

- **EX028 — Sincronização dos relógios.** Por que sincronizar os relógios dos dispositivos? *Rubrica:* 3 = para que os eventos possam ser ordenados corretamente;; 2 = ordenação;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Saber onde ficam os dados sensíveis e coletar telemetria com propósito e protegida prepara uma prática para detectar e investigar.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura e engenharia de segurança: modos de falha

### Objetivos de aprendizagem

Você vai (1) listar as formas como os sistemas da clínica podem falhar; (2) separar falhas acidentais de deliberadas; (3) planejar respostas para as mais danosas.

### 8.1 Listar as falhas

Nadia trabalha com Grace para listar os modos de falha dos serviços críticos. O link de internet pode cair, cortando o acesso ao sistema clínico em nuvem. O disco do servidor de imagens pode encher ou falhar. Um ransomware pode criptografar o servidor de imagens. Um funcionário pode apagar imagens por engano. O fornecedor da nuvem pode ter uma indisponibilidade. Uma queda de energia pode parar tudo. Para cada caso, ela anota como eles perceberiam e por quanto tempo a clínica conseguiria se virar. Listar as falhas antes que aconteçam permite que a equipe se prepare com calma, em vez de improvisar.

### 8.2 Acidente ou ataque

Muitas falhas parecem iguais, sejam acidentais ou deliberadas. Imagens sumidas podem ser uma exclusão por engano ou um ransomware. Nadia anota os sinais que os distinguem: o ransomware costuma alterar muitos arquivos rapidamente e deixar notas de resgate, enquanto a exclusão acidental afeta poucos arquivos. Ela acrescenta os dois ao plano de resposta, já que os primeiros passos diferem: no ransomware, desconectar o servidor da rede; na exclusão, restaurar do backup. Reconhecer a diferença cedo evita que um acidente seja tratado como crise ou que um ataque seja tratado como rotina.

### 8.3 Respostas

Para as falhas mais danosas, Nadia escreve cartões curtos de resposta. Internet fora do ar: mudar para um roteador reserva de dados móveis guardado na recepção e usar listas do dia impressas. Servidor de imagens perdido: restaurar do backup do escritório central para um servidor reserva, o que ela estima levar quatro horas. Ransomware: isolar, ligar para Grace, não pagar e restaurar do backup depois de entender a causa. Cada cartão cabe numa página e nomeia quem age. Os cartões são testados num breve exercício de mesa (tabletop) com o gerente da clínica.

### Exemplo resolvido

Nadia lista seis modos de falha, distingue ransomware de exclusão acidental e escreve cartões de resposta de uma página testados num exercício de mesa.

> **Caso sintético.** As falhas e os tempos são sintéticos.

### Erros e limites

Os cartões de resposta envelhecem conforme os sistemas mudam. Os tempos de restauração são estimativas até serem testados.

### Exercícios

- **EX029 — Sinais de ransomware.** Em que o ransomware costuma diferir da exclusão acidental? *Rubrica:* 3 = muitos arquivos mudam rapidamente e aparecem notas de resgate;; 2 = volume;; 1 = nenhuma;; 0 = nenhuma.

- **EX030 — Primeiro passo no ransomware.** Qual é o primeiro passo diante de um ransomware? *Rubrica:* 3 = desconectar o servidor da rede;; 2 = isolar;; 1 = restaurar;; 0 = nenhuma.

- **EX031 — Contingência da internet.** Qual é a contingência quando a internet cai? *Rubrica:* 3 = um roteador reserva de dados móveis e listas do dia impressas;; 2 = roteador reserva;; 1 = nenhuma;; 0 = nenhuma.

- **EX032 — Estimativa de restauração.** Quanto tempo se estima que leve a restauração das imagens? *Rubrica:* 3 = quatro horas;; 2 = quatro;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Listar modos de falha e redigir respostas de uma página testadas prepara uma prática tanto para acidentes quanto para ataques.

<a id="ch-09"></a>

## Capítulo 9 — Arquitetura e engenharia de segurança: ferramentas e métodos

### Objetivos de aprendizagem

Você vai (1) usar um método de checklist nas revisões de configuração; (2) usar um modelo de ameaças simples; (3) escolher o método certo para a tarefa.

### 9.1 Revisões por checklist

Para o trabalho de rotina, Nadia usa checklists. Ela monta um para os PCs das clínicas com base na baseline de segurança do fornecedor do sistema operacional: atualizações em dia, criptografia de disco ativada, firewall ativado, nenhum administrador local no uso diário, bloqueio de tela configurado e antivírus ativo. Os checklists são rápidos e consistentes, e servem para tarefas repetidas nas cinco clínicas. Daniel alerta que os checklists só encontram o que listam, então servem para configurações conhecidas, e não para projetos novos, em que é preciso um método de modelagem de ameaças para descobrir o que verificar.

### 9.2 Um modelo de ameaças simples

Quando a Linden planeja o agendamento online para os pacientes, Nadia aplica ao projeto o STRIDE de Shostack (2014). Ela pergunta, para cada parte: alguém consegue se passar por um paciente, alterar um agendamento, negar ter feito um, ver os agendamentos de outros pacientes, inundar o sistema ou obter direitos da equipe? O método descobre que o projeto preliminar mostra os nomes de outros pacientes no calendário de agendamento. O fornecedor altera o calendário para mostrar apenas os horários livres. Um método estruturado encontrou um problema que um checklist não teria coberto.

### 9.3 Escolher os métodos

Nadia escreve um guia para Grace: usar checklists para as configurações de rotina em dispositivos conhecidos; usar o STRIDE para sistemas novos e mudanças nos fluxos de dados; usar a lista de modos de falha para o planejamento de resiliência; e usar a revisão de logs para verificar o que de fato aconteceu. Cada método tem um custo em tempo. Usar o certo evita desperdiçar esforço, como modelar ameaças para a troca de uma impressora ou usar um checklist para um novo serviço online. O guia tem uma página e fica na pasta de TI. Grace acrescenta uma coluna com o tempo típico que cada método leva, para poder planejar a semana de forma realista.

### Exemplo resolvido

Nadia monta um checklist para os PCs, usa o STRIDE para pegar nomes de pacientes num calendário de agendamento e escreve um guia para a escolha de métodos.

> **Caso sintético.** O projeto de agendamento é sintético; Shostack (2014) é real.

### Erros e limites

Os checklists ficam desatualizados. Os modelos de ameaças dependem de projetos exatos.

### Exercícios

- **EX033 — Limite do checklist.** Qual é o limite de um checklist? *Rubrica:* 3 = só encontra o que lista;; 2 = cobertura;; 1 = nenhuma;; 0 = nenhuma.

- **EX034 — Achado do STRIDE.** O que o STRIDE encontrou no projeto de agendamento? *Rubrica:* 3 = nomes de outros pacientes exibidos no calendário;; 2 = nomes;; 1 = nenhuma;; 0 = nenhuma.

- **EX035 — Correção do fornecedor.** Como o fornecedor corrigiu o calendário? *Rubrica:* 3 = mostrando apenas os horários livres;; 2 = horários;; 1 = nenhuma;; 0 = nenhuma.

- **EX036 — Método para sistemas novos.** Que método serve para sistemas novos? *Rubrica:* 3 = a modelagem de ameaças com STRIDE;; 2 = STRIDE;; 1 = checklist;; 0 = nenhuma.

### Síntese

Listas de verificação servem para contextos rotineiros, enquanto modelos de ameaças servem para desenhos novos; escolher bem economiza tempo e encontra problemas reais.

<a id="ch-10"></a>

## Capítulo 10 — Arquitetura e engenharia de segurança: configuração de controles

### Objetivos de aprendizagem

Você vai (1) configurar as regras de firewall entre segmentos; (2) documentar o propósito de cada regra; (3) revisar as regras em busca de erros.

### 10.1 Escrever as regras

Nadia transforma o projeto segmentado do capítulo 6 em regras de firewall para o roteador de Elmfield. Cada regra nomeia um segmento de origem, um destino, uma porta e uma ação. Os PCs dos consultórios podem alcançar o servidor de imagens na porta do visualizador. O servidor de imagens pode alcançar os backups do escritório central pela VPN. As maquininhas de cartão podem alcançar apenas os endereços do provedor de pagamentos. Os visitantes podem alcançar apenas a internet. Uma regra final nega todo o resto entre os segmentos. A ordem importa: os roteadores aplicam a primeira regra que corresponde, então as permissões específicas vêm antes da negação geral.

### Laboratório — Teste de fluxos contra a lista de regras

```python
# Test expected and forbidden flows against an ordered rule list (synthetic).
def allowed(rules, src, dst, port):
    for s, d, p, act in rules:
        if s in (src, "*") and d in (dst, "*") and p in (port, "*"): return act == "allow"
    return False
tests = [("surgery", "imaging", 8443, True), ("imaging", "backup", 445, True), ("payment", "provider", 443, True),
         ("guest", "internet", 443, True), ("reception", "imaging", 8443, False), ("guest", "imaging", 8443, False),
         ("reception", "payment", 443, False)]
v1 = [("staff", "imaging", 8443, "allow"), ("imaging", "backup", 445, "allow"), ("payment", "provider", 443, "allow"),
      ("guest", "internet", "*", "allow"), ("*", "*", "*", "deny")]
seg = {"surgery": "staff", "reception": "staff"}
v2 = [("surgery", "imaging", 8443, "allow")] + v1[1:]
for name, rules, mapping in (("first draft", v1, seg), ("split segments", v2, {})):
    fails = [t for t in tests if allowed(rules, mapping.get(t[0], t[0]), t[1], t[2]) != t[3]]
    print(f"{name}: {len(tests) - len(fails)}/{len(tests)} pass; failures {[(f[0], f[1], f[2]) for f in fails]}")
```

Execute com `python3 lab_fw.py`. Saída verificada:

```text
first draft: 6/7 pass; failures [('reception', 'imaging', 8443)]
split segments: 7/7 pass; failures []
```

### 10.2 Documentar o propósito

Ao lado de cada regra, Nadia escreve seu propósito e seu responsável, como "visualização de raio X nos consultórios, responsável Grace". As regras sem propósito documentado são as que se acumulam e nunca são removidas, porque ninguém se atreve a apagá-las. Ela guarda a lista de regras com o diagrama de rede. Quando, mais tarde, um fornecedor pede uma nova regra, Grace consegue conferir se ela se encaixa no projeto e registrar por que foi acrescentada, mantendo o conjunto de regras compreensível por anos. A lista de regras é revisada uma vez por ano junto com o diagrama de rede.

### 10.3 Revisar as regras

Antes de aplicar as regras, Nadia as testa com um pequeno script que confere uma lista de fluxos esperados e proibidos. O laboratório mostra que todos os fluxos esperados são permitidos, mas que um fluxo proibido, dos PCs da recepção para o servidor de imagens, também é permitido, porque ela escreveu a regra dos consultórios para todo o segmento da equipe. Ela divide a equipe em segmentos de recepção e de consultórios e roda o teste de novo, que então passa. Testar as regras antes de aplicá-las evita tanto indisponibilidades quanto lacunas. Ela guarda a lista de testes para reutilizá-la depois da implantação.

### Exemplo resolvido

Nadia escreve regras de segmentos ordenadas, com propósitos e responsáveis, testa fluxos esperados e proibidos e corrige uma regra ampla demais.

> **Caso sintético.** As regras e os segmentos são sintéticos.

### Erros e limites

Os testes cobrem apenas os fluxos listados. A sintaxe do roteador difere do modelo de teste.

### Exercícios

- **EX037 — Ordem das regras.** Por que as permissões específicas precisam vir antes da negação geral? *Rubrica:* 3 = os roteadores aplicam a primeira regra que corresponde;; 2 = primeira correspondência;; 1 = nenhuma;; 0 = nenhuma.

- **EX038 — Regras não documentadas.** Por que as regras não documentadas se acumulam? *Rubrica:* 3 = ninguém se atreve a apagá-las;; 2 = medo;; 1 = nenhuma;; 0 = nenhuma.

- **EX039 — Falha no laboratório.** Que fluxo proibido o primeiro teste permitiu? *Rubrica:* 3 = recepção para imagens na porta 8443;; 2 = recepção;; 1 = nenhuma;; 0 = nenhuma.

- **EX040 — Correção.** Como Nadia corrigiu a regra ampla? *Rubrica:* 3 = dividindo a equipe em segmentos de recepção e de consultórios;; 2 = dividir;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Regras ordenadas, documentadas e testadas transformam um desenho de segmentação em uma configuração funcional.

<a id="ch-11"></a>

## Capítulo 11 — Arquitetura e engenharia de segurança: verificação

### Objetivos de aprendizagem

Você vai (1) verificar os controles depois da implantação; (2) testar a partir de cada segmento; (3) registrar os resultados da verificação.

### 11.1 Depois da implantação

Grace aplica as novas regras em Elmfield num domingo. Na segunda de manhã, Nadia verifica se a configuração implantada corresponde ao projeto. Ela não confia apenas na tela de configuração do roteador, porque o que está configurado e o que de fato acontece podem diferir. Ela planeja testes a partir de cada segmento usando um notebook que pode mudar de porta e de rede, com a aprovação por escrito de Grace. A verificação confere o comportamento real que os pacientes e a equipe vão experimentar, e não apenas a intenção. Ela também reserva uma hora com Grace para revisarem juntas os resultados.

### 11.2 Testar a partir de cada segmento

A partir do segmento dos consultórios, Nadia abre com sucesso o visualizador de raio X e confirma que não consegue alcançar as maquininhas de cartão. A partir da recepção, confirma que o sistema clínico em nuvem funciona e que o servidor de imagens está inalcançável. A partir da rede de visitantes, alcança a internet, mas nenhum dispositivo interno. A partir do segmento de pagamentos, confere com a ferramenta de teste do provedor que as maquininhas continuam processando transações. Um teste falha: a impressora dos consultórios não pode ser alcançada pelos PCs dos consultórios, porque foi colocada no segmento da recepção. Grace a move.

### 11.3 Registrar os resultados

Nadia registra cada teste: data, segmento, alvo, resultado esperado, resultado real e quem testou. O registro mostra a falha da impressora e sua correção, seguidas de um novo teste aprovado. Ela acrescenta a lista de testes ao procedimento de mudanças da Linden, para que os mesmos testes rodem depois de qualquer mudança futura em qualquer clínica. A verificação registrada é evidência para os auditores e para o provedor de pagamentos, e encurta a solução de problemas depois, porque a equipe sabe quais fluxos funcionavam em qual data. Os registros ficam numa pasta compartilhada com a lista de regras e os diagramas, para que qualquer pessoa que investigue um problema posterior possa comparar com eles.

### Exemplo resolvido

Nadia verifica a segmentação de Elmfield testando a partir de quatro segmentos, encontra uma impressora mal posicionada e registra os resultados para reutilização.

> **Caso sintético.** Os testes e os dispositivos são sintéticos.

### Erros e limites

Testes num momento não provam o comportamento futuro. Mover um notebook entre segmentos exige cuidado.

### Exercícios

- **EX041 — Por que não a tela.** Por que não confiar na tela de configuração do roteador? *Rubrica:* 3 = o comportamento configurado e o real podem diferir;; 2 = comportamento;; 1 = nenhuma;; 0 = nenhuma.

- **EX042 — Teste de visitantes.** O que o teste da rede de visitantes confirmou? *Rubrica:* 3 = só internet, nenhum dispositivo interno;; 2 = só internet;; 1 = nenhuma;; 0 = nenhuma.

- **EX043 — Teste que falhou.** Que teste falhou, e por quê? *Rubrica:* 3 = impressora dos consultórios inalcançável; estava no segmento da recepção;; 2 = impressora;; 1 = nenhuma;; 0 = nenhuma.

- **EX044 — Reutilização.** Como os testes serão reutilizados? *Rubrica:* 3 = acrescentados ao procedimento de mudanças para as mudanças futuras;; 2 = procedimento de mudanças;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

A verificação a partir de cada segmento, com resultados registrados, confirma que os controles se comportam como projetados.

<a id="ch-12"></a>

## Capítulo 12 — Laboratório isolado I

### Objetivos de aprendizagem

Você vai (1) construir um laboratório isolado de uma rede de clínica; (2) simular a propagação de um ransomware; (3) comparar os resultados com rede plana e segmentada.

### 12.1 Construir o laboratório

Na escola, Daniel monta um laboratório isolado com máquinas virtuais: três PCs de recepção, três PCs de consultório, um servidor de imagens e um servidor de backup, todos numa rede isolada, sem internet. A tarefa de Nadia é comparar até onde uma infecção simulada se espalha numa rede plana e no seu projeto segmentado. A simulação usa um script inofensivo que apenas registra quais máquinas ele conseguiu alcançar. Daniel enfatiza que nenhum malware real entra no laboratório e que a rede do laboratório continua isolada.

### Laboratório — Propagação simulada em redes plana e segmentada

```python
# Simulated reachability spread from one reception PC (no malware; graph only).
machines = ["rec1", "rec2", "rec3", "sur1", "sur2", "sur3", "imaging", "backup"]
def spread(edges, start):
    seen, todo = {start}, [start]
    while todo:
        m = todo.pop()
        for a, b in edges:
            if a == m and b not in seen: seen.add(b); todo.append(b)
    return sorted(seen)
flat = [(a, b) for a in machines for b in machines if a != b]
rec = ["rec1", "rec2", "rec3"]; sur = ["sur1", "sur2", "sur3"]
seg = [(a, b) for a in rec for b in rec if a != b] + [(a, b) for a in sur for b in sur if a != b] + \
      [(s, "imaging") for s in sur] + [("imaging", "backup")]
for name, edges in (("flat", flat), ("segmented", seg)):
    r = spread(edges, "rec1"); print(f"{name}: {len(r)} machines reached {r}")
```

Execute com `python3 lab_spread.py`. Saída verificada:

```text
flat: 8 machines reached ['backup', 'imaging', 'rec1', 'rec2', 'rec3', 'sur1', 'sur2', 'sur3']
segmented: 3 machines reached ['rec1', 'rec2', 'rec3']
```

### 12.2 Executar a simulação

Nadia modela a alcançabilidade dos dois projetos e inicia a infecção simulada num PC da recepção. Na rede plana, ela alcança todas as máquinas, inclusive o servidor de imagens e o servidor de backup. No projeto segmentado, alcança apenas os outros PCs da recepção, porque a recepção não consegue alcançar o servidor de imagens e o servidor de backup só aceita conexões do servidor de imagens. O laboratório imprime as máquinas alcançáveis em cada caso, dando um retrato claro do que a segmentação limita. Ela guarda as duas saídas para o relatório do laboratório.

### 12.3 Interpretar

Nadia anota os limites da simulação: um ransomware real pode usar credenciais roubadas ou o sistema em nuvem, e um PC de consultório comprometido ainda alcançaria o servidor de imagens. Ela acrescenta que a restrição do servidor de backup é o resultado mais valioso, porque mantém a recuperação possível. Ela recomenda cópias offline como segunda camada. Daniel pede à turma que compare os resultados; a maioria encontra padrões semelhantes. O exercício mostra por que a segmentação e os backups protegidos andam juntos. Ela registra esses limites no relatório do laboratório para que os leitores não exagerem o resultado, e sugere estender a simulação à propagação baseada em credenciais num exercício posterior.

### Exemplo resolvido

Nadia simula a propagação de uma infecção num laboratório isolado e constata que todas as oito máquinas são alcançadas na rede plana e três no projeto segmentado.

> **Caso sintético.** O laboratório é sintético e isolado.

### Erros e limites

As simulações simplificam o comportamento do atacante. Os PCs dos consultórios continuam sendo um caminho até as imagens.

### Exercícios

- **EX045 — Segurança do laboratório.** Que regra protege o laboratório? *Rubrica:* 3 = nenhum malware real e nenhuma conexão com a internet;; 2 = isolado;; 1 = nenhuma;; 0 = nenhuma.

- **EX046 — Resultado plano.** Quantas máquinas a infecção alcançou na rede plana? *Rubrica:* 3 = todas as 8;; 2 = todas;; 1 = nenhuma;; 0 = nenhuma.

- **EX047 — Resultado segmentado.** Quantas máquinas foram afetadas no projeto segmentado? *Rubrica:* 3 = 3 PCs da recepção;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

- **EX048 — Resultado mais valioso.** Por que a restrição do servidor de backup é o resultado mais valioso? *Rubrica:* 3 = mantém a recuperação possível;; 2 = recuperação;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Simulações contidas mostram como a segmentação e os backups protegidos limitam a propagação de uma infecção.

<a id="ch-13"></a>

## Capítulo 13 — Arquitetura e engenharia de segurança: solução de problemas

### Objetivos de aprendizagem

Você vai (1) diagnosticar um problema causado por uma mudança de segurança; (2) usar os logs para encontrar a causa; (3) corrigi-lo mantendo o controle.

### 13.1 O problema

Duas semanas depois da segmentação, a clínica de Norbury relata que as imagens de raio X levam minutos para aparecer nos consultórios. A equipe suspeita do novo firewall. Nadia começa descrevendo o sintoma com exatidão: as imagens carregam, mas devagar, só em dois dos quatro consultórios e só desde terça-feira. Ela pergunta o que mudou na terça e descobre que um novo sensor de raio X foi instalado no consultório três. Sintomas precisos estreitam a busca muito mais depressa do que queixas genéricas de que a rede está lenta. Ela escreve esses detalhes no chamado antes de investigar mais.

### 13.2 Usar os logs

Nadia confere os logs do firewall do roteador, que mostram conexões repetidamente bloqueadas dos PCs dos consultórios para o servidor de imagens numa segunda porta. O software do novo sensor usa uma porta extra para as prévias das imagens, que as regras não permitem. O visualizador tenta de novo antes de recorrer ao método mais lento, o que causa os atrasos. A causa é um fluxo novo e legítimo, e não um defeito do projeto. Os logs transformaram uma queixa vaga numa regra específica que faltava em vinte minutos. Ela salva as linhas de log relevantes como evidência no chamado.

### 13.3 Corrigir do jeito certo

Nadia confirma a porta na documentação do fornecedor do sensor e depois acrescenta uma regra que permite que os PCs dos consultórios alcancem o servidor de imagens apenas nessa porta, com o propósito e o responsável registrados. Ela roda de novo os testes de verificação do capítulo 11 e acrescenta a nova porta à lista de fluxos esperados. As imagens voltam a carregar normalmente. Ela também acrescenta uma etapa ao procedimento de mudanças: os novos dispositivos clínicos precisam ter suas necessidades de rede documentadas antes da instalação, para que o próximo dispositivo não cause o mesmo atraso.

### Exemplo resolvido

Nadia estreita uma queixa de lentidão nas imagens, encontra conexões bloqueadas nos logs, acrescenta uma regra documentada e atualiza o procedimento de mudanças.

> **Caso sintético.** Os dispositivos e as portas são sintéticos.

### Erros e limites

A documentação dos fornecedores pode estar incompleta. O comportamento de nova tentativa esconde os bloqueios dos usuários.

### Exercícios

- **EX049 — Sintoma preciso.** Que sintoma preciso Nadia registrou? *Rubrica:* 3 = carregamento lento das imagens em dois de quatro consultórios desde terça;; 2 = preciso;; 1 = nenhuma;; 0 = nenhuma.

- **EX050 — Evidência nos logs.** O que os logs do firewall mostraram? *Rubrica:* 3 = conexões bloqueadas dos PCs dos consultórios para o servidor de imagens numa segunda porta;; 2 = bloqueios;; 1 = nenhuma;; 0 = nenhuma.

- **EX051 — Correção certa.** Como o problema foi corrigido? *Rubrica:* 3 = uma regra documentada só para aquela porta, seguida de novos testes;; 2 = regra estreita;; 1 = liberar tudo;; 0 = nenhuma.

- **EX052 — Prevenção.** O que evita uma repetição? *Rubrica:* 3 = documentar as necessidades de rede dos novos dispositivos antes da instalação;; 2 = procedimento de mudanças;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Sintomas e logs precisos encontram a causa real, e correções estreitas mantêm os controles intactos.

<a id="ch-14"></a>

## Capítulo 14 — Arquitetura e engenharia de segurança: automação

### Objetivos de aprendizagem

Você vai (1) automatizar uma comparação de configurações entre as clínicas; (2) relatar a deriva; (3) manter a automação segura.

### 14.1 Deriva entre os locais

As cinco clínicas deveriam compartilhar a mesma baseline, mas as configurações derivam à medida que as pessoas fazem mudanças locais. Nadia escreve um script que compara as configurações exportadas do roteador de cada clínica com uma baseline de referência e lista as diferenças. Grace exporta as configurações todo mês. A deriva importa porque uma única mudança esquecida, como uma regra temporária deixada aberta, pode desfazer a proteção que o projeto oferece. A automação permite que uma equipe pequena confira cinco locais de forma consistente em minutos, em vez de ler longos arquivos de configuração a olho. Grace concorda em rodar a comparação na primeira segunda-feira de cada mês.

### Laboratório — Comparação das configurações das clínicas com uma baseline

```python
# Compare practice router settings with a baseline (synthetic exports).
base = {"smb1": "off", "remote_admin_wan": "off", "guest_isolation": "on", "rule_preview_9443": "absent", "ntp": "on"}
sites = {"Elmfield": dict(base), "Ashby": dict(base), "Kingsley": dict(base),
         "Norbury": dict(base, rule_preview_9443="present"), "Westcott": dict(base, remote_admin_wan="on")}
for s, cfg in sites.items():
    diff = {k: (base[k], v) for k, v in cfg.items() if base[k] != v}
    print(f"{s}: " + ("matches baseline" if not diff else f"differs {diff}"))
```

Execute com `python3 lab_drift.py`. Saída verificada:

```text
Elmfield: matches baseline
Ashby: matches baseline
Kingsley: matches baseline
Norbury: differs {'rule_preview_9443': ('absent', 'present')}
Westcott: differs {'remote_admin_wan': ('off', 'on')}
```

### 14.2 Relatar a deriva

O laboratório compara cinco clínicas. Três correspondem à baseline. Norbury tem a regra documentada da porta de prévias do capítulo 13, que Nadia acrescenta à baseline porque todas as clínicas em breve terão os novos sensores. Westcott tem a administração remota habilitada a partir da internet, o que ninguém consegue explicar. Grace a desativa e troca a senha do roteador para o caso de ela ter sido usada. O relatório lista cada diferença com uma ação recomendada, separando as mudanças aprovadas das inexplicadas. Os achados e as ações são registrados, para que o relatório mensal seguinte possa confirmar que continuaram corrigidos.

### 14.3 Automação segura

O script lê as exportações e relata; ele nunca altera as configurações do roteador. As mudanças continuam sendo uma decisão humana depois de revisão. Nadia guarda o script e a baseline no repositório da Linden com histórico de mudanças, para que as atualizações da baseline fiquem visíveis. Ela acrescenta um teste que falha se uma exportação vier vazia, o que de outro modo poderia parecer conformidade perfeita. Daniel observa que a automação somente de leitura é o primeiro passo certo para equipes pequenas, já que acrescenta visibilidade sem acrescentar o risco de erros automatizados.

### Exemplo resolvido

Nadia compara as configurações dos roteadores de cinco clínicas com uma baseline, atualiza a baseline para uma mudança aprovada e encontra uma administração remota inexplicada.

> **Caso sintético.** As configurações e as clínicas são sintéticas.

### Erros e limites

As exportações podem omitir algumas configurações. As baselines precisam de responsáveis para se manterem atualizadas.

### Exercícios

- **EX053 — Por que a deriva importa.** Por que a deriva importa? *Rubrica:* 3 = uma mudança esquecida pode desfazer a proteção do projeto;; 2 = desfazer;; 1 = nenhuma;; 0 = nenhuma.

- **EX054 — Achado em Westcott.** O que o laboratório encontrou em Westcott? *Rubrica:* 3 = administração remota habilitada a partir da internet;; 2 = administração remota;; 1 = nenhuma;; 0 = nenhuma.

- **EX055 — Atualização da baseline.** Por que a diferença de Norbury foi acrescentada à baseline? *Rubrica:* 3 = todas as clínicas em breve terão os novos sensores;; 2 = aprovada;; 1 = ignorada;; 0 = nenhuma.

- **EX056 — Exportação vazia.** Por que testar exportações vazias? *Rubrica:* 3 = uma exportação vazia poderia parecer conformidade perfeita;; 2 = falsa aprovação;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Relatórios de desvio somente leitura dão a equipes pequenas visibilidade consistente entre as unidades, mantendo as mudanças sob controle humano.

<a id="ch-15"></a>

## Capítulo 15 — Arquitetura e engenharia de segurança: integração e dependências

### Objetivos de aprendizagem

Você vai (1) listar as dependências externas da Linden; (2) avaliar o acesso dos fornecedores; (3) planejar para a falha de um fornecedor.

### 15.1 Dependências

Nadia lista os serviços externos dos quais a Linden depende: o fornecedor do sistema de gestão clínica em nuvem, o provedor de e-mail, o provedor de pagamentos, o fornecedor do software de raio X com suporte remoto, os provedores de internet de cada clínica e o serviço de lembretes por mensagem de texto. Para cada um, ela registra que dados ele guarda, quem administra o contrato e o que acontece se ele falhar. O fornecedor do sistema de gestão clínica é a dependência mais profunda, já que toda consulta e todo prontuário vivem ali. As dependências fazem parte da arquitetura, mesmo que a Linden não as opere.

### 15.2 Acesso dos fornecedores

O fornecedor de raio X se conecta remotamente aos servidores de imagens para dar suporte, usando uma ferramenta de acesso remoto sempre ligada. Nadia recomenda que as sessões só sejam habilitadas sob demanda e aprovadas por Grace, com o fornecedor usando contas nominais e login multifator. Ela também pergunta ao serviço de lembretes por mensagem que dados de pacientes ele recebe e descobre que ele recebe o nome completo e o tipo de tratamento, embora só sejam necessários o primeiro nome e o horário. Grace pede ao fornecedor que reduza os dados enviados. Os dois pedidos são registrados na pasta do fornecedor.

### 15.3 Falha de fornecedor

Nadia pede a cada fornecedor crítico seus compromissos de recuperação e verifica o que a Linden consegue fazer sozinha. Se o sistema de gestão clínica falhar, as clínicas podem imprimir toda noite as listas do dia seguinte como contingência. Se o fornecedor de raio X desaparecer, o software de imagens continua rodando localmente, mas não pode ser atualizado. Ela acrescenta isso aos cartões de resposta do capítulo 8. Planejar para a falha de fornecedores faz parte da resiliência, porque a indisponibilidade longa mais provável numa pequena organização muitas vezes é problema de outra pessoa. Cada contingência é praticada uma vez por ano.

### Exemplo resolvido

Nadia lista seis dependências, restringe o acesso sempre ligado do fornecedor, reduz os dados enviados a um serviço de mensagens e acrescenta contingências para a falha de fornecedores.

> **Caso sintético.** Os fornecedores e os dados são sintéticos.

### Erros e limites

Os compromissos dos fornecedores podem não ser cumpridos. As contingências precisam de prática regular.

### Exercícios

- **EX057 — Dependência mais profunda.** Qual é a dependência mais profunda, e por quê? *Rubrica:* 3 = o fornecedor do sistema de gestão clínica; todas as consultas e prontuários vivem ali;; 2 = sistema clínico;; 1 = e-mail;; 0 = nenhuma.

- **EX058 — Mudança no acesso do fornecedor.** Como deve mudar o acesso do fornecedor de raio X? *Rubrica:* 3 = habilitado sob demanda, aprovado, contas nominais com multifator;; 2 = sob demanda;; 1 = sempre ligado;; 0 = nenhuma.

- **EX059 — Dados do serviço de mensagens.** De que dados o serviço de mensagens realmente precisa? *Rubrica:* 3 = primeiro nome e horário da consulta;; 2 = mínimos;; 1 = prontuários completos;; 0 = nenhuma.

- **EX060 — Contingência dos prontuários.** Qual é a contingência se o sistema clínico falhar? *Rubrica:* 3 = imprimir toda noite as listas do dia seguinte;; 2 = imprimir;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

As dependências pertencem à arquitetura, com acesso limitado dos fornecedores, o mínimo de dados compartilhados e alternativas ensaiadas.

<a id="ch-16"></a>

## Capítulo 16 — Documentação técnica e segurança

### Objetivos de aprendizagem

Você vai (1) escrever documentação técnica clara; (2) incluir avisos de segurança e de privacidade; (3) manter os documentos atualizados.

### 16.1 Escrever para o leitor

Nadia reescreve as anotações dispersas da Linden num conjunto curto de documentação: um diagrama de rede por clínica, a lista de regras de firewall com os propósitos, as baselines dos dispositivos, os cartões de resposta e runbooks para as tarefas de rotina. Ela escreve para a pessoa que vai usar cada documento sob pressão, muitas vezes um gerente de clínica durante uma indisponibilidade. Cada documento começa com seu propósito e quem deve usá-lo, usa passos numerados e evita jargão. Daniel lembra a ela que a documentação é julgada por se outra pessoa consegue segui-la corretamente sem ajuda.

### 16.2 Avisos de segurança e de privacidade

Algumas tarefas trazem riscos para os pacientes ou para os dados. Reiniciar o servidor de imagens durante o horário de atendimento poderia interromper um raio X em andamento, então o runbook manda consultar os consultórios primeiro. Exportar logs para uma investigação poderia expor nomes de pacientes, então o runbook manda guardar as exportações apenas na pasta restrita de logs. Nadia coloca os avisos imediatamente antes do passo a que se aplicam, e não numa seção separada, porque as pessoas sob pressão pulam avisos gerais, mas percebem os que estão no lugar onde agem.

### 16.3 Manter os documentos atualizados

Os documentos envelhecem rápido. Nadia acrescenta uma versão, uma data e um responsável a cada um e liga as atualizações ao procedimento de mudanças: qualquer mudança numa rede, regra ou dispositivo precisa atualizar o documento correspondente antes que a mudança seja encerrada. Grace agenda uma verificação trimestral em que um gerente de clínica segue um runbook e relata os problemas. A primeira verificação encontra uma captura de tela de uma interface de roteador mais antiga. Tratar os documentos como parte do sistema, e não como algo secundário, os mantém úteis quando são mais necessários.

### Exemplo resolvido

Nadia escreve documentos focados no leitor, com avisos de segurança e de privacidade junto aos passos, e liga as atualizações ao controle de mudanças e a verificações trimestrais.

> **Caso sintético.** Os documentos e as verificações são sintéticos.

### Erros e limites

Os documentos derivam quando as mudanças pulam o procedimento. Avisos demais diluem a atenção.

### Exercícios

- **EX061 — Teste da documentação.** Como a documentação é julgada? *Rubrica:* 3 = por se outra pessoa consegue segui-la corretamente sem ajuda;; 2 = usabilidade;; 1 = extensão;; 0 = nenhuma.

- **EX062 — Aviso sobre reiniciar o servidor de imagens.** Que aviso se aplica a reiniciar o servidor de imagens? *Rubrica:* 3 = consultar os consultórios primeiro para não interromper um raio X;; 2 = consultar os consultórios;; 1 = nenhuma;; 0 = nenhuma.

- **EX063 — Onde pôr os avisos.** Onde os avisos devem ser colocados? *Rubrica:* 3 = imediatamente antes do passo a que se aplicam;; 2 = junto ao passo;; 1 = apêndice;; 0 = nenhuma.

- **EX064 — Achado da verificação trimestral.** O que a primeira verificação trimestral encontrou? *Rubrica:* 3 = uma captura de tela desatualizada do roteador;; 2 = captura de tela;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Uma boa documentação técnica é escrita para quem a usa, coloca os avisos onde eles atuam e se mantém atualizada por meio do controle de mudanças.

<a id="ch-17"></a>

## Capítulo 17 — Laboratório isolado II

### Objetivos de aprendizagem

Você vai (1) testar num laboratório a detecção de logins suspeitos; (2) medir detecções e alarmes falsos; (3) recomendar configurações para a Linden.

### 17.1 A tarefa do laboratório

O segundo laboratório de Daniel usa registros sintéticos de login de um sistema clínico em nuvem. Cada registro mostra o usuário, a hora, o local e se o login teve sucesso, com alguns logins maliciosos plantados. Nadia precisa desenhar uma regra que alerte sobre logins suspeitos sem inundar Grace de alarmes. A equipe da Linden trabalha em cinco cidades, principalmente entre as sete da manhã e as sete da noite, então ela começa descrevendo, a partir dos dados, o comportamento normal antes de escrever qualquer regra. Ela escreve sua descrição do normal em poucas frases e pede que Daniel a confira antes de começar a programar.

### Laboratório — Detecção de logins suspeitos em registros sintéticos

```python
# Compare two sign-in alert rules on synthetic records: (user, hour, town, attack?)
recs = [("dr.ali", 9, "Elmfield", 0), ("dr.ali", 23, "Elmfield", 0), ("n.ross", 8, "Norbury", 0),
        ("n.ross", 14, "Norbury", 0), ("dr.ali", 3, "Lisbon", 1), ("k.chan", 10, "Ashby", 0),
        ("k.chan", 2, "Unknown", 1), ("m.ojo", 12, "Kingsley", 0), ("m.ojo", 22, "Riga", 1),
        ("p.lee", 18, "Westcott", 0), ("p.lee", 11, "Westcott", 0)]
seen = {}
for u, h, t, _ in recs:
    if 7 <= h < 19: seen.setdefault(u, set()).add(t)
def rule_a(r): return not (7 <= r[1] < 19)
def rule_b(r): return rule_a(r) and r[2] not in seen.get(r[0], set())
for name, rule in (("Rule A", rule_a), ("Rule B", rule_b)):
    hits = [r for r in recs if rule(r)]
    caught = sum(r[3] for r in hits)
    print(f"{name}: {len(hits)} alerts, {caught} attacks caught, {len(hits) - caught} false alarms")
```

Execute com `python3 lab_signin.py`. Saída verificada:

```text
Rule A: 4 alerts, 3 attacks caught, 1 false alarms
Rule B: 3 alerts, 3 attacks caught, 0 false alarms
```

### 17.2 Medir

Nadia testa duas regras. A regra A alerta sobre qualquer login fora do horário de trabalho. A regra B alerta sobre logins fora do horário de trabalho que também venham de um local nunca usado antes por aquele usuário. O laboratório conta, para cada uma, os alertas, os ataques plantados detectados e os alarmes falsos. A regra A detecta todos os ataques plantados, mas também sinaliza um dentista que confere a agenda tarde da noite. A regra B detecta os mesmos ataques com menos alarmes falsos. Medir os dois resultados mostra o trade-off com clareza. Ela guarda as contagens para o relatório.

### 17.3 Recomendar

Nadia recomenda a regra B para a Linden, com alertas enviados a Grace e uma revisão semanal, e anota seus limites: um atacante usando uma senha roubada durante o horário de trabalho, a partir de uma cidade habitual, não seria sinalizado. Ela acrescenta que o login multifator no sistema clínico importa mais do que qualquer regra de alerta, já que ele bloqueia de saída a maioria dos ataques com senhas roubadas. Daniel concorda, observando que a detecção complementa a prevenção, mas não pode substituí-la. Ela escreve a recomendação como uma nota de uma página para Grace, listando a regra, quem recebe os alertas, a revisão semanal e o ponto cego conhecido, para que a decisão possa ser revista se os padrões de trabalho da Linden mudarem.

### Exemplo resolvido

Nadia compara duas regras de alerta de login em dados sintéticos, escolhe a que tem menos alarmes falsos e declara seu ponto cego.

> **Caso sintético.** Os registros e os ataques são sintéticos.

### Erros e limites

Os ataques plantados podem ser mais fáceis que os reais. Os dados de localização podem estar errados.

### Exercícios

- **EX065 — Normal primeiro.** O que Nadia descreveu antes de escrever as regras? *Rubrica:* 3 = o comportamento normal: cinco cidades, das 7h às 19h;; 2 = normal;; 1 = nenhuma;; 0 = nenhuma.

- **EX066 — Resultado da regra A.** Quais foram os resultados da regra A? *Rubrica:* 3 = 4 alertas, 3 ataques detectados, 1 alarme falso;; 2 = números;; 1 = nenhuma;; 0 = nenhuma.

- **EX067 — Resultado da regra B.** Quais foram os resultados da regra B? *Rubrica:* 3 = 3 alertas, 3 ataques detectados, 0 alarme falso;; 2 = números;; 1 = nenhuma;; 0 = nenhuma.

- **EX068 — Ponto cego.** O que a regra B deixaria passar? *Rubrica:* 3 = uma senha roubada usada no horário de trabalho a partir de uma cidade habitual;; 2 = horário de trabalho;; 1 = nada;; 0 = nenhuma.

### Síntese

Medir a detecção e os alarmes falsos em dados rotulados mostra qual regra implantar, enquanto a prevenção continua essencial.

<a id="ch-18"></a>

## Capítulo 18 — Projeto técnico supervisionado

### Objetivos de aprendizagem

Você vai (1) entregar um projeto técnico completo sob supervisão; (2) apresentar os resultados ao cliente; (3) refletir sobre o seu desenvolvimento.

### 18.1 O projeto

O projeto supervisionado de Nadia é implantar o projeto segmentado nas quatro clínicas restantes da Linden. Ela planeja uma clínica por semana, fora do horário de atendimento, usando a lista de regras, a baseline, os testes e os documentos construídos durante o curso. Antes de cada implantação, ela confirma as listas de dispositivos com o gerente da clínica e verifica se há dispositivos novos. Grace supervisiona a primeira implantação e revisa as demais. O projeto reúne modelagem, configuração, verificação, solução de problemas, automação e documentação num único trabalho real. Ela mantém um log curto de cada noite de implantação.

### 18.2 Entrega e resultados

As quatro implantações são concluídas dentro do prazo. Os testes de verificação passam de primeira em três clínicas; em Ashby, uma maquininha de cartão falha no teste porque estava conectada à porta errada do switch, o que Grace corrige. O script de deriva confirma que as cinco clínicas agora correspondem à baseline. Nadia apresenta os resultados ao diretor de operações da Linden: segmentação implantada, backups protegidos, cartões de resposta testados e documentos atualizados. Ela também lista o que falta: login multifator no sistema clínico e treinamento da equipe. O diretor aprova os dois itens para o ano que vem.

### 18.3 Reflexão

Em sua reflexão, Nadia registra o que agora consegue fazer sozinha: ler redes, configurar e verificar regras de firewall, escrever scripts e documentação úteis, resolver problemas a partir dos logs e trabalhar com fornecedores. Ela anota onde ainda precisa de apoio, como na negociação com fornecedores. A Linden lhe oferece uma vaga de meio período enquanto ela termina o curso. O retorno final de Daniel diz que o hábito mais forte dela é testar antes e depois de cada mudança, o que lhe servirá em qualquer função técnica. Ela arquiva a reflexão no portfólio do curso.

### Exemplo resolvido

Nadia implanta a segmentação em quatro clínicas, corrige a porta de uma maquininha, apresenta os resultados com as lacunas restantes e reflete sobre suas habilidades.

> **Caso sintético.** As implantações e as pessoas são sintéticas.

### Erros e limites

A supervisão pode esconder lacunas na habilidade independente. As lacunas restantes precisam de responsáveis depois do projeto.

### Exercícios

- **EX069 — Verificação antes da implantação.** O que Nadia confirmava antes de cada implantação? *Rubrica:* 3 = as listas de dispositivos com o gerente da clínica e eventuais dispositivos novos;; 2 = dispositivos;; 1 = nenhuma;; 0 = nenhuma.

- **EX070 — Problema em Ashby.** Que problema ocorreu em Ashby? *Rubrica:* 3 = uma maquininha de cartão na porta errada do switch;; 2 = porta;; 1 = nenhuma;; 0 = nenhuma.

- **EX071 — Trabalho restante.** O que Nadia listou como restante? *Rubrica:* 3 = login multifator no sistema clínico e treinamento da equipe;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX072 — Hábito mais forte.** Qual Daniel disse ser o hábito mais forte dela? *Rubrica:* 3 = testar antes e depois de cada mudança;; 2 = testar;; 1 = nenhuma;; 0 = nenhuma.

### Síntese

Um projeto supervisionado que combina todas as habilidades, apresenta resultados honestos e lista o trabalho restante completa a preparação técnica.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX072. Nadia Kowalczyk, Daniel Mercer, Grace Mwangi, o Harbourside Technical College, o Linden Dental Group e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Porque um dispositivo só é importante pelos serviços que sustenta.

**EX002.** Um appliance de backup no escritório central que copia o servidor de imagens de cada clínica toda noite.

**EX003.** Porque podem recorrer a anotar os dados do cartão e cobrar depois por telefone com o provedor.

**EX004.** Os prontuários dos pacientes e as imagens de raio X.

**EX005.** Porque qualquer PC infectado consegue alcançar diretamente o servidor de imagens.

**EX006.** Porque as versões antigas do SMB têm fraquezas conhecidas exploradas por ransomware.

**EX007.** Foi restringida à rede da equipe, para não ser alcançável pela rede sem fio de visitantes.

**EX008.** A rede plana compartilhada pelos dispositivos dos consultórios e pelos PCs da recepção.

**EX009.** Os downloads rodam com direitos totais e ninguém consegue saber quem usou cada PC.

**EX010.** Com uma correção de configuração do fornecedor que concede direitos apenas à pasta do próprio programa.

**EX011.** Depois de cinco minutos de inatividade.

**EX012.** Porque controles lentos são contornados pela equipe ocupada.

**EX013.** Porque o appliance só enviava e-mails quando havia sucesso.

**EX014.** Apenas 4 de 7 noites tiveram sucesso, com o último sucesso em 2026-03-05.

**EX015.** Porque um script que esconde problemas é pior do que nenhum.

**EX016.** Um disco cheio no servidor de imagens de Elmfield.

**EX017.** O sistema de gestão clínica administrado pelo fornecedor e os sistemas do provedor de pagamentos.

**EX018.** Testar ataques; ela só podia ler configurações, entrevistar a equipe e executar verificações aprovadas.

**EX019.** Registrou-a como uma declaração e depois a verificou olhando o balcão da recepção.

**EX020.** O servidor de imagens compartilha uma pasta legível por todos na rede.

**EX021.** As maquininhas de cartão e os sensores de raio X.

**EX022.** Porque a integridade das imagens afeta o diagnóstico.

**EX023.** PCs da equipe, imagens clínicas, maquininhas de pagamento e visitantes.

**EX024.** Usando LANs virtuais.

**EX025.** O nome e a data de nascimento dos pacientes.

**EX026.** Porque telemetria sem uma pergunta a responder vira ruído.

**EX027.** Para um serviço de logs em nuvem que a equipe das clínicas não consegue modificar.

**EX028.** Para que os eventos de dispositivos diferentes possam ser ordenados corretamente.

**EX029.** O ransomware altera muitos arquivos rapidamente e deixa notas de resgate, enquanto a exclusão afeta poucos arquivos.

**EX030.** Desconectar o servidor da rede.

**EX031.** Um roteador reserva de dados móveis na recepção e listas do dia impressas.

**EX032.** Cerca de quatro horas, para um servidor reserva.

**EX033.** Ele só encontra os itens que já lista.

**EX034.** Os nomes de outros pacientes ficavam visíveis no calendário de agendamento.

**EX035.** Mostrando apenas os horários livres.

**EX036.** A modelagem de ameaças com STRIDE.

**EX037.** Porque os roteadores aplicam a primeira regra que corresponde.

**EX038.** Porque, sem um propósito conhecido, ninguém se atreve a apagá-las.

**EX039.** PCs da recepção alcançando o servidor de imagens na porta 8443.

**EX040.** Dividindo a equipe em segmentos separados de recepção e de consultórios.

**EX041.** Porque o que está configurado e o que de fato acontece podem diferir.

**EX042.** Os visitantes alcançam a internet, mas nenhum dispositivo interno.

**EX043.** O da impressora dos consultórios, porque ela havia sido colocada no segmento da recepção.

**EX044.** Foram acrescentados ao procedimento de mudanças, para rodar depois das mudanças futuras.

**EX045.** Nenhum malware real entra, e a rede do laboratório não tem internet.

**EX046.** Todas as oito máquinas, inclusive os servidores de imagens e de backup.

**EX047.** Três, apenas os PCs da recepção.

**EX048.** Porque mantém a recuperação possível depois de uma infecção.

**EX049.** Imagens carregando devagar em dois de quatro consultórios, só desde terça-feira.

**EX050.** Conexões repetidamente bloqueadas numa segunda porta, usada para as prévias.

**EX051.** Acrescentando uma regra documentada apenas para aquela porta e rodando de novo os testes de verificação.

**EX052.** Exigir que as necessidades de rede dos novos dispositivos clínicos sejam documentadas antes da instalação.

**EX053.** Porque uma mudança esquecida, como uma regra temporária aberta, pode desfazer a proteção.

**EX054.** Administração remota habilitada a partir da internet, que ninguém conseguia explicar.

**EX055.** Porque a regra documentada da porta de prévias em breve será necessária em todas as clínicas.

**EX056.** Porque uma exportação vazia poderia, de outro modo, parecer conformidade perfeita.

**EX057.** O fornecedor do sistema de gestão clínica em nuvem, porque toda consulta e todo prontuário vivem ali.

**EX058.** Sessões habilitadas apenas sob demanda e aprovadas por Grace, com contas nominais e login multifator.

**EX059.** Apenas o primeiro nome e o horário da consulta.

**EX060.** Imprimir toda noite as listas de consultas do dia seguinte.

**EX061.** Por se outra pessoa consegue segui-la corretamente sem ajuda.

**EX062.** Consultar os consultórios primeiro, para que um raio X em andamento não seja interrompido.

**EX063.** Imediatamente antes do passo a que se aplicam.

**EX064.** Uma captura de tela de uma interface de roteador mais antiga.

**EX065.** O comportamento normal, com a equipe em cinco cidades trabalhando principalmente das 7h às 19h.

**EX066.** Gerou 4 alertas, detectando 3 ataques com 1 alarme falso.

**EX067.** Gerou 3 alertas, detectando os 3 ataques sem nenhum alarme falso.

**EX068.** Um atacante usando uma senha roubada durante o horário de trabalho a partir de uma cidade habitual.

**EX069.** As listas de dispositivos com o gerente da clínica, incluindo eventuais dispositivos novos.

**EX070.** Uma maquininha de cartão estava conectada à porta errada do switch.

**EX071.** Login multifator no sistema clínico e treinamento da equipe.

**EX072.** Testar antes e depois de cada mudança.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
