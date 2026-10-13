# Fatores Humanos e Política Cibernética: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 121, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–50 de 50 têm texto didático escrito à mão; os exercícios EX001–EX150 têm resoluções correspondentes com rubricas de 0 a 3; os dezenove laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de engenharia que projetam, verificam e operam um programa de conscientização e de reporte em segurança como um sistema sociotécnico projetado.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios modelam reportes semanais, esquecimento, taxas, triagem, filas, confiabilidade, orçamentos e testes exatos sobre dados sintéticos; nenhum funcionário, e-mail ou conta real está envolvido. Toda simulação de phishing descrita é anunciada, aprovada com os representantes dos funcionários, evita iscas que explorem sofrimento pessoal e é relatada apenas de forma agregada. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de engenharia ao longo de um curso de cinco anos centrado no programa de reportes de uma companhia de saneamento: fundamentos, medição e modelos, requisitos e arquitetura, controles e implementação, verificação e validação, operações, otimização, o projeto final com terceirizados, o dossiê de evidências, a tese e a defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Aiko Tanabe** | Estudante de engenharia | Inventada |
| **Profa. Joanna Kerr** | Orientadora | Inventada |
| **Rivenhall Technical University** | Universidade fictícia | Inventada |
| **Greyford Water** | Companhia de saneamento fictícia, 600 funcionários | Inventada |

### Fontes principais

Adams e Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff e Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Hansche et al. (2024), NIST SP 800-50r1; Dawkins e Jacobs (2023), [doi:10.6028/NIST.TN.2276](https://doi.org/10.6028/NIST.TN.2276); Lain, Kostiainen e Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766); Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) usar taxas de variação para descrever o comportamento de segurança ao longo do tempo; (2) interpretar derivadas como velocidades de mudança nos reportes; (3) relacionar a acumulação aos totais de exposição.

### 1.1 Taxas em fatores humanos

Aiko Tanabe é estudante de engenharia na fictícia Rivenhall Technical University. Sua orientadora, a Profa. Joanna Kerr, liga cada disciplina básica a um caso contínuo: a fictícia companhia de saneamento Greyford Water, cujos seiscentos funcionários incluem operadores da sala de controle, engenheiros de campo e equipes administrativas. Em cálculo, Aiko aprende que a derivada descreve a velocidade com que algo muda. Na Greyford, o número de funcionários que reportam e-mails suspeitos muda ao longo das semanas após uma campanha. A taxa de variação diz a ela se os reportes ainda estão subindo, se estabilizaram ou se estão recuando, o que importa mais para o planejamento do que qualquer contagem semanal isolada.

### 1.2 Ler uma curva

Aiko modela os reportes semanais após uma campanha como uma curva que sobe depressa no início e depois se estabiliza. A derivada é grande nas primeiras semanas e encolhe em direção a zero. Ela aprende a ler o ponto em que a curva se dobra, porque é quando o efeito da campanha está se esgotando e um lembrete pode ajudar. Também percebe que uma reta enganaria: ela preveria reportes crescendo para sempre. Escolher uma forma que se ajuste ao modo como as pessoas realmente respondem é a primeira decisão de modelagem em qualquer análise de fatores humanos, e o cálculo lhe dá o vocabulário para descrevê-la.

### 1.3 Acumulação e exposição

A integração soma uma taxa ao longo do tempo. Aiko a usa para estimar a exposição total: se um e-mail de phishing fica nas caixas de entrada sem ser reportado, o número de pessoas que poderiam clicar cresce a cada hora, até que alguém o reporte e ele seja removido. A área sob a curva de caixas de entrada com o e-mail não reportado ao longo do tempo mede a exposição. Reportes mais rápidos encolhem essa área. Essa ideia simples liga a disciplina de matemática ao objetivo da Greyford de reduzir o tempo em que e-mails maliciosos continuam disponíveis, uma medida que não depende de culpar quem clicou.

### Exemplo resolvido

Aiko descreve os reportes após uma campanha como uma curva, lê sua taxa de variação para descobrir quando o efeito se esgota e usa a acumulação para definir o tempo de exposição.

> **Caso sintético.** A Rivenhall, a Greyford e todas as pessoas e números são sintéticos.

### Erros e limites

Curvas suaves simplificam dados semanais ruidosos. Modelos de exposição ignoram o quanto cada e-mail é atraente.

### Exercícios

- **EX001 — Significado da taxa.** O que a derivada dos reportes semanais diz à Greyford? *Rubrica:* 3 = se os reportes estão subindo, se estabilizando ou caindo;; 2 = tendência;; 1 = nada;; 0 = nenhuma.
- **EX002 — Falha da reta.** Por que uma reta enganaria para os reportes após uma campanha? *Rubrica:* 3 = prevê reportes crescendo para sempre;; 2 = sem limite;; 1 = nada;; 0 = nenhuma.
- **EX003 — Área de exposição.** Como a integração define a exposição? *Rubrica:* 3 = área sob as caixas de entrada sem reporte ao longo do tempo;; 2 = área;; 1 = contagem;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) usar conjuntos e lógica para enunciar regras de política; (2) encontrar contradições entre regras; (3) contar combinações que afetam a usabilidade.

### 2.1 Política como lógica

Aiko traduz as regras de senha e de acesso da Greyford para a lógica. Uma regra diz que os operadores devem bloquear a tela ao deixar um console. Outra diz que os consoles da sala de controle devem permanecer conectados durante incidentes, para que nenhum alarme seja perdido. Escritas como proposições lógicas, as duas entram em choque durante um incidente em que um operador se afasta por um instante. Adams e Sasse (1999) constataram que funcionários diante de regras conflitantes ou impraticáveis fazem os próprios acordos. Escrever as regras com precisão expõe esses conflitos antes que os funcionários sejam obrigados a escolher qual regra quebrar.

### 2.2 Conjuntos de pessoas e permissões

Usando conjuntos, Aiko lista quais grupos de funcionários têm quais permissões. A interseção entre engenheiros de campo e pessoas com acesso remoto às estações de bombeamento mostra quem poderia alterar configurações de fora da planta. A diferença entre o conjunto de pessoas treinadas em acesso remoto e o de pessoas que o possuem revela onze funcionários com acesso e sem treinamento. Conjuntos transformam preocupações vagas em listas exatas sobre as quais os gestores podem agir, e facilitam verificar se uma mudança proposta amplia ou reduz cada grupo.

### 2.3 Contar o ônus

Aiko conta quantos logins distintos um engenheiro de campo faz em um dia típico: notebook, acesso remoto, sistema de manutenção, e-mail, folha de ponto e dois portais de fornecedores. Cada um tem as próprias regras de senha. Ela calcula que, se cada sistema exigisse trocas em um calendário diferente, o engenheiro enfrentaria uma troca de senha aproximadamente toda semana. Contar torna o ônus visível. Sasse, Brostoff e Weirich (2001) argumentaram que esse ônus provoca os contornos frequentemente atribuídos à culpa dos usuários; por isso, contar é um primeiro passo rumo a mudanças de projeto.

### Exemplo resolvido

Aiko escreve duas regras em lógica para expor um conflito, usa operações de conjuntos para encontrar funcionários sem treinamento com acesso remoto e conta o ônus de logins.

> **Caso sintético.** As regras, os grupos e as contagens são sintéticos; Adams e Sasse (1999) e Sasse et al. (2001) são reais.

### Erros e limites

A lógica captura regras escritas, não a prática informal. As contagens dependem de um dia típico que pode variar.

### Exercícios

- **EX004 — Conflito de regras.** Quais duas regras entram em conflito na sala de controle? *Rubrica:* 3 = bloquear a tela ao sair versus permanecer conectado durante incidentes;; 2 = as duas regras;; 1 = nada;; 0 = nenhuma.
- **EX005 — Uso da diferença de conjuntos.** O que a diferença de conjuntos revelou? *Rubrica:* 3 = onze funcionários com acesso remoto e sem treinamento;; 2 = sem treinamento;; 1 = nada;; 0 = nenhuma.
- **EX006 — Frequência de trocas.** Com que frequência um engenheiro poderia enfrentar uma troca de senha com calendários separados? *Rubrica:* 3 = aproximadamente toda semana;; 2 = semanal;; 1 = anual;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar ambientes físicos ao erro humano; (2) aplicar as ideias de sinal e ruído aos alarmes; (3) considerar a segurança física em termos humanos.

### 3.1 Ambiente e erro

Aiko visita a sala de controle da Greyford. Iluminação, ruído dos equipamentos, duração dos turnos e reflexos nas telas afetam a precisão com que os operadores leem os painéis. A física explica alguns desses efeitos: o reflexo reduz o contraste, e o ruído de fundo mascara alarmes sonoros. Erros humanos nessas condições costumam ser consequências previsíveis do ambiente, e não falhas pessoais. Ela observa que melhorar a iluminação e os tons de alarme pode reduzir erros a um custo menor do que retreinar funcionários que já são competentes. Lista as condições observadas em uma tabela curta e a compartilha com o supervisor da sala de controle para receber comentários.

### 3.2 Sinal e ruído

Na física, a relação sinal-ruído mede com que clareza um sinal se destaca. Aiko a aplica a alarmes e a alertas de segurança. Se os operadores veem centenas de alarmes de pouco valor por turno, os importantes se perdem no ruído, e os funcionários aprendem a reconhecê-los sem ler. O mesmo acontece com avisos de segurança nas telas: avisos frequentes ensinam as pessoas a clicar adiante. Herley (2009) argumentou que avisos com maioria de falsos positivos podem ser ignorados racionalmente. Aumentar o sinal significa remover os alertas de pouco valor, e não pedir às pessoas que se concentrem mais.

### 3.3 Segurança física e pessoas

Aiko examina o acesso físico. As portas da sala de controle usam crachás, mas os funcionários muitas vezes as seguram abertas para colegas que carregam equipamentos. Ela observa que a física das portas importa: uma porta pesada que fecha devagar convida à carona na entrada. Uma mudança de projeto, como uma mola de fechamento mais rápida e uma segunda entrada para entregas, elimina a pressão para segurar a porta. Controles físicos funcionam melhor quando se ajustam às tarefas que as pessoas executam, a mesma lição que vale para os controles digitais. O gerente de instalações da Greyford concorda em testar a mola mais rápida em uma das unidades.

### Exemplo resolvido

Aiko liga as condições da sala de controle a erros previsíveis, usa a relação sinal-ruído para explicar a fadiga de alarmes e redesenha o comportamento das portas para reduzir as caronas.

> **Caso sintético.** A sala de controle é sintética; Herley (2009) é real.

### Erros e limites

Correções ambientais exigem conhecimento de ergonomia. A redução de alarmes não pode eliminar alarmes críticos.

### Exercícios

- **EX007 — Erros previsíveis.** Por que muitos erros na sala de controle são previsíveis? *Rubrica:* 3 = decorrem de iluminação, ruído, reflexo e duração dos turnos;; 2 = ambiente;; 1 = descuido;; 0 = nenhuma.
- **EX008 — Ruído de alarmes.** O que acontece quando os operadores veem centenas de alarmes de pouco valor? *Rubrica:* 3 = reconhecem os alarmes sem ler;; 2 = fadiga;; 1 = nada;; 0 = nenhuma.
- **EX009 — Redesenho da porta.** Como o projeto de uma porta pode reduzir as caronas? *Rubrica:* 3 = mola de fechamento mais rápida e entrada separada para entregas;; 2 = projeto;; 1 = placas;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas simples para analisar dados de comportamento; (2) tratar dados pessoais com cuidado no código; (3) testar programas com casos conhecidos.

### 4.1 Primeiro programa de análise

Aiko escreve seu primeiro programa em Python para resumir contagens semanais sintéticas de reportes feitos pelo botão de reporte da Greyford. O programa lê uma lista de números, calcula o total, a média e a semana com mais reportes e imprime o resultado. Ela o testa com uma lista curta cuja resposta conhece de cabeça. Testar com casos conhecidos é um hábito básico de engenharia, porque um programa que roda sem erros ainda pode dar respostas erradas se um laço pular a última semana ou dividir pela contagem errada.

### Laboratório — Resumo das contagens semanais de reportes

```python
# Summarise weekly report-button counts after a campaign (synthetic).
weeks = [12, 30, 41, 35, 27, 22, 19, 18, 17, 17, 16, 16]
total = sum(weeks); peak = max(weeks); pw = weeks.index(peak) + 1
print(f"weeks {len(weeks)}, total {total}, average {total / len(weeks):.1f}, peak week {pw} ({peak})")
for i, w in enumerate(weeks, 1): print(f"week {i:2d} {'#' * (w // 2)} {w}")
```

Execute com `python3 lab_weekly.py`. Saída verificada:

```text
weeks 12, total 270, average 22.5, peak week 3 (41)
week  1 ###### 12
week  2 ############### 30
week  3 #################### 41
week  4 ################# 35
week  5 ############# 27
week  6 ########### 22
week  7 ######### 19
week  8 ######### 18
week  9 ######## 17
week 10 ######## 17
week 11 ######## 16
week 12 ######## 16
```

### 4.2 Tratar dados pessoais

A Profa. Kerr adverte que dados de comportamento podem ser pessoais. O programa de Aiko trabalha com contagens por semana, e não com nomes. Se algum dia ela precisar de registros individuais, substituirá os nomes por códigos aleatórios e guardará a chave separadamente. Ela escreve essa regra no topo do script. Programas que processam dados de funcionários devem coletar o mínimo necessário, porque, uma vez numa planilha, os dados tendem a ser copiados, e cópias são difíceis de rastrear ou apagar. A Profa. Kerr confere a regra durante a revisão de código.

### 4.3 Ler o resultado

O laboratório mostra doze semanas de reportes, com pico na semana três, depois de uma campanha, e estabilização em um nível mais baixo. Aiko observa que a média esconde esse formato, por isso acrescenta uma barra simples impressa para cada semana. Ver o formato confirma seu modelo de cálculo do capítulo 1. Ela aprende que a saída de um programa deve apoiar a decisão em questão: aqui, quando agendar o próximo lembrete, algo que as barras semanais tornam óbvio. Ela salva a saída com a data, para que campanhas futuras possam ser comparadas com o mesmo padrão semanal e a mesma linha de base.

### Exemplo resolvido

Aiko escreve e testa um programa que resume os reportes semanais, limita-o a contagens em vez de nomes e acrescenta uma exibição simples em barras para revelar o formato.

> **Caso sintético.** As contagens são sintéticas.

### Erros e limites

Médias escondem padrões. Dados pseudonimizados ainda podem identificar pessoas em grupos pequenos.

### Exercícios

- **EX010 — Hábito de teste.** Por que testar com uma lista cuja resposta é conhecida? *Rubrica:* 3 = um programa pode rodar e ainda dar respostas erradas;; 2 = correção;; 1 = nada;; 0 = nenhuma.
- **EX011 — Pico no laboratório.** Que semana teve mais reportes no laboratório, e quantos? *Rubrica:* 3 = semana 3, com 41 reportes;; 2 = semana 3;; 1 = nada;; 0 = nenhuma.
- **EX012 — Regra de dados.** Que regra Aiko escreveu no topo do script? *Rubrica:* 3 = usar contagens; pseudonimizar com chave separada se forem necessários indivíduos;; 2 = dados mínimos;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever com clareza para operadores e gestores; (2) apresentar dados de comportamento sem atribuir culpa; (3) adaptar uma mensagem ao seu público.

### 5.1 Escrever para operadores

Aiko escreve uma nota de uma página para os operadores da sala de controle explicando o botão de reporte. Usa frases curtas, passos numerados e uma captura de tela. Evita termos como vetor de phishing e usa palavras simples, como e-mail suspeito. Testa a nota com dois operadores, que sugerem colocar em primeiro lugar o passo mais importante: o que fazer se já tiverem clicado. A comunicação em engenharia dá certo quando o leitor consegue agir corretamente, depressa e sem medo de parecer tolo. A nota revisada é plastificada e colocada ao lado de cada console.

### 5.2 Apresentar sem culpa

Para os gestores, Aiko apresenta os resultados das simulações como totais e tendências por departamento, nunca com nomes. Ela enquadra o clique como um resultado esperado de boas iscas e se concentra na velocidade dos reportes. Lain, Kostiainen e Čapkun (2022) constataram que os reportes dos funcionários podem ser um sinal forte de detecção nas organizações. Apresentar resultados sem culpa mantém os funcionários dispostos a reportar os próprios erros, que é justamente quando o reporte rápido mais importa. Ela também mostra aos gestores como a abordagem sem culpa aumentou os reportes de erros genuínos na equipe piloto, o que os convence a manter nomes fora de todos os relatórios e a elogiar publicamente os reportes rápidos.

### 5.3 Adaptar a mensagem

Aiko prepara três versões dos mesmos achados: um gráfico e três tópicos para o conselho, uma página de detalhes para a equipe de segurança e a nota para os operadores. Todas usam os mesmos números, mas com ênfases diferentes. O conselho vê o tempo de exposição caindo; a equipe de segurança vê a carga de triagem; os operadores veem o que fazer. A Profa. Kerr observa que adaptar mensagens não é manipulação, desde que os fatos sejam os mesmos e as limitações apareçam em todas as versões. Ela guarda as três versões em uma única pasta.

### Exemplo resolvido

Aiko escreve uma nota para operadores testada com usuários, apresenta resultados aos gestores sem culpa e adapta um mesmo achado para três públicos.

> **Caso sintético.** As notas e os públicos são sintéticos; Lain et al. (2022) é real.

### Erros e limites

Mensagens simplificadas podem perder ressalvas. Totais por departamento ainda podem expor equipes minúsculas.

### Exercícios

- **EX013 — Sugestão dos operadores.** O que os operadores sugeriram colocar em primeiro lugar na nota? *Rubrica:* 3 = o que fazer se já tiver clicado;; 2 = passo do clique;; 1 = nada;; 0 = nenhuma.
- **EX014 — Enquadramento sem culpa.** Como Aiko enquadra o clique para os gestores? *Rubrica:* 3 = como resultado esperado de boas iscas, com foco na velocidade do reporte;; 2 = esperado;; 1 = falha;; 0 = nenhuma.
- **EX015 — Mesmos fatos.** O que mantém honestas as mensagens adaptadas? *Rubrica:* 3 = os mesmos fatos e limitações em todas as versões;; 2 = consistência;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) modelar o decaimento dos efeitos do treinamento; (2) comparar calendários de reciclagem; (3) reconhecer os limites dos modelos suaves de comportamento.

### 6.1 Modelar o decaimento

Aiko lê que habilidades e atenção se desgastam depois do treinamento. Ela modela a proporção de funcionários que identificariam corretamente uma isca típica como alta logo após o treinamento e decaindo exponencialmente em direção a uma linha de base mais baixa. O modelo tem dois parâmetros: a linha de base e a taxa de decaimento. O cálculo lhe permite obter a meia-vida, o tempo para que o benefício extra do treinamento caia pela metade. Ela enfatiza à Profa. Kerr que se trata de um modelo para apoiar o planejamento e que ainda não tem evidência de que os funcionários da Greyford sigam exatamente essa curva.

### 6.2 Comparar calendários

Usando o modelo, Aiko compara um único curso anual com reciclagens curtas a cada três meses. Integrar o benefício ao longo de um ano mostra que reciclagens curtas e frequentes mantêm a média mais alta, mesmo que cada uma seja menos intensa. O laboratório calcula o benefício médio dos dois calendários com a mesma taxa de decaimento. Ela observa que a comparação ignora o tempo que cada calendário custa aos funcionários, que, segundo a ideia de orçamento de compliance de Beautement, Sasse e Wonham (2008), precisa ser contabilizado; por isso, acrescenta os minutos dos funcionários à comparação.

### Laboratório — Benefício médio da reciclagem anual versus trimestral

```python
# Average training benefit over 12 months: annual vs quarterly refreshers (synthetic exponential decay).
import math
base, gain, k = 0.40, 0.45, 0.24          # baseline, boost after training, decay per month
print(f"half-life of benefit: {math.log(2) / k:.1f} months")
def avg(refresh_months):
    total, steps = 0.0, 1200
    for i in range(steps):
        t = 12 * i / steps; since = min(t - r for r in refresh_months if r <= t)
        total += base + gain * math.exp(-k * since)
    return total / steps
print(f"annual (month 0): average {avg([0]):.2f}")
print(f"quarterly (0,3,6,9): average {avg([0, 3, 6, 9]):.2f}")
```

Execute com `python3 lab_decay.py`. Saída verificada:

```text
half-life of benefit: 2.9 months
annual (month 0): average 0.55
quarterly (0,3,6,9): average 0.72
```

### 6.3 Limites dos modelos suaves

O comportamento real é irregular. Um único incidente marcante pode elevar a vigilância mais do que qualquer reciclagem, e um período de muito trabalho pode reduzi-la de repente. Bada, Sasse e Nurse (2019) constataram que campanhas de conscientização muitas vezes fracassam quando se apoiam apenas em informação, de modo que uma curva suave de decaimento pode descrever o conhecimento, e não o comportamento. Aiko escreve esses limites ao lado do modelo e propõe testá-lo contra os dados reais de reportes da Greyford antes de usá-lo para definir o calendário de treinamento. Ela anota esse teste como tarefa para seu capítulo posterior de medição, quando os dados reais estarão disponíveis.

### Exemplo resolvido

Aiko modela o decaimento do treinamento com uma meia-vida, compara calendários anual e trimestral incluindo o tempo dos funcionários e registra os limites do modelo.

> **Caso sintético.** Os parâmetros são sintéticos; Beautement et al. (2008) e Bada et al. (2019) são reais.

### Erros e limites

O decaimento exponencial é uma premissa. Medidas de conhecimento podem não refletir o comportamento.

### Exercícios

- **EX016 — Meia-vida.** Que meia-vida a taxa de decaimento do laboratório implica? *Rubrica:* 3 = cerca de 2,9 meses;; 2 = cerca de 3 meses;; 1 = nada;; 0 = nenhuma.
- **EX017 — Resultado dos calendários.** Que calendário manteve o maior benefício médio no laboratório? *Rubrica:* 3 = o trimestral: 0,72 contra 0,55 do anual;; 2 = trimestral;; 1 = anual;; 0 = nenhuma.
- **EX018 — Custo ausente.** Que custo Aiko acrescentou à comparação? *Rubrica:* 3 = os minutos dos funcionários gastos em treinamento;; 2 = tempo dos funcionários;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar taxas com incerteza; (2) evitar comparações enganosas entre grupos pequenos; (3) relatar resultados sem identificar indivíduos.

### 7.1 Taxas com incerteza

A última simulação da Greyford constatou que nove de sessenta engenheiros de campo reportaram o e-mail em até uma hora. Aiko calcula a taxa, quinze por cento, e um intervalo de confiança para mostrar quão incerta ela é com apenas sessenta pessoas. O intervalo é largo, de modo que um resultado posterior de vinte por cento talvez não seja uma melhora real. Ela aprende que toda taxa de um grupo pequeno deve vir acompanhada de sua incerteza; caso contrário, os gestores vão reagir à variação aleatória como se fosse uma tendência. Ela acrescenta o intervalo a todos os gráficos.

### Laboratório — Taxas de reporte com intervalos de Wilson por equipe

```python
# Report rates with Wilson 95% intervals by team (synthetic simulation results).
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
teams = {"field engineers": (9, 60), "office": (31, 140), "treatment": (12, 45), "lab": (4, 8), "fleet": (6, 30)}
for t, (k, n) in teams.items():
    lo, hi = wilson(k, n); flag = "  (under 20: merge before reporting)" if n < 20 else ""
    print(f"{t:15} {k}/{n} = {k/n:.1%}  95% CI {lo:.1%} to {hi:.1%}{flag}")
```

Execute com `python3 lab_rates.py`. Saída verificada:

```text
field engineers 9/60 = 15.0%  95% CI 8.1% to 26.1%
office          31/140 = 22.1%  95% CI 16.1% to 29.7%
treatment       12/45 = 26.7%  95% CI 16.0% to 41.0%
lab             4/8 = 50.0%  95% CI 21.5% to 78.5%  (under 20: merge before reporting)
fleet           6/30 = 20.0%  95% CI 9.5% to 37.3%
```

### 7.2 Grupos pequenos

Aiko compara as taxas de reporte de cinco equipes. A menor, com oito pessoas, mostra a taxa mais alta, mas seu intervalo é muito largo. Ela adverte contra ranquear equipes publicamente, porque equipes pequenas oscilam ao acaso e os rankings envergonham pessoas por resultados casuais. Observa também que publicar uma taxa para uma equipe de oito pessoas poderia identificar indivíduos. Sua regra é relatar apenas grupos de vinte ou mais pessoas, fundindo equipes pequenas quando necessário. O laboratório marca a equipe de oito pessoas para fusão, e ela explica ao líder da equipe por que o resultado não será mostrado separadamente.

### 7.3 Relato honesto

Aiko redige os resultados para a direção: a taxa geral de reporte com seu intervalo, a mudança desde o último trimestre e uma nota de que as diferenças entre equipes estão, em sua maioria, dentro da incerteza. Ela inclui a dificuldade da isca na Phish Scale, conforme descrita por Dawkins e Jacobs (2023), porque uma isca mais difícil naturalmente reduziria os reportes. A estatística no trabalho com fatores humanos precisa ser honesta sobre incerteza e contexto, para que as pessoas não sejam julgadas pelo ruído. Ela também lista o que os números não podem mostrar, como se os funcionários que não reportaram simplesmente nunca abriram o e-mail, para que os gestores não leiam demais nos números.

### Exemplo resolvido

Aiko estima taxas de reporte com intervalos de Wilson, adverte contra ranquear equipes pequenas, funde grupos com menos de vinte pessoas e relata os resultados junto com a dificuldade da isca.

> **Caso sintético.** As equipes e as contagens são sintéticas; Dawkins e Jacobs (2023) é real.

### Erros e limites

Os intervalos supõem respostas independentes. Fundir grupos esconde diferenças reais.

### Exercícios

- **EX019 — Intervalo dos engenheiros de campo.** Que intervalo o laboratório deu para 9 de 60? *Rubrica:* 3 = 15,0%, intervalo de Wilson de 95% de 8,1% a 26,1%;; 2 = largo;; 1 = nada;; 0 = nenhuma.
- **EX020 — Risco do ranking.** Por que não ranquear equipes publicamente pela taxa de reporte? *Rubrica:* 3 = equipes pequenas oscilam ao acaso e rankings envergonham por resultados casuais;; 2 = ruído;; 1 = nada;; 0 = nenhuma.
- **EX021 — Regra de tamanho de grupo.** Que tamanho mínimo de grupo Aiko relata? *Rubrica:* 3 = vinte;; 2 = 20;; 1 = oito;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) relacionar o projeto de hardware às decisões de segurança dos usuários; (2) entender os recursos de hardware seguro com que os usuários se deparam; (3) avaliar como o projeto afeta a segurança utilizável.

### 8.1 O hardware com que os usuários lidam

Aiko estuda como o hardware molda o que os usuários veem. Notebooks com um trusted platform module (TPM) podem guardar chaves de modo que a criptografia de disco seja destravada automaticamente com um PIN; chaves de segurança contêm pequenos chips seguros que fazem a autenticação sem revelar segredos. Os usuários não veem os chips, mas sentem o resultado: menos senhas e passos mais simples. Projetar o hardware de modo que o caminho seguro seja também o mais fácil é uma ideia central da segurança utilizável, em sintonia com Sasse, Brostoff e Weirich (2001). Ela lista os recursos presentes nos notebooks da Greyford.

### 8.2 Projeto e decisões

Aiko compara duas formas de a Greyford proteger os notebooks de campo. Uma pede aos usuários uma senha de disco longa e separada na inicialização; a outra usa o TPM com um PIN curto. Entrevistas com engenheiros mostram que eles anotariam a senha longa no próprio notebook. A opção apoiada em hardware oferece proteção semelhante contra o roubo do notebook e elimina a tentação. Ela observa que um bom projeto de hardware reduz o número de decisões de segurança que os usuários precisam tomar corretamente. Apresenta as duas opções ao gerente de TI com as evidências das entrevistas, e o desenho apoiado em hardware é escolhido para a próxima renovação de notebooks.

### 8.3 Limites

Recursos de hardware não resolvem tudo. Chaves de segurança podem ser perdidas, e a reposição precisa ser rápida, ou os funcionários ficarão bloqueados durante trabalhos urgentes. O firmware precisa de atualizações, que os usuários podem adiar se elas interromperem o trabalho. Aiko escreve requisitos: chaves reservas nos depósitos, atualizações agendadas fora dos turnos e um processo claro de recuperação. O hardware só apoia a segurança utilizável quando os processos ao redor são desenhados para condições reais de trabalho. Ela observa também que os funcionários precisam de instruções simples para o primeiro uso, porque uma primeira experiência confusa com uma chave de segurança pode criar uma resistência duradoura, e rascunha um guia ilustrado de uma página para os depósitos.

### Exemplo resolvido

Aiko liga o hardware seguro a passos mais simples para o usuário, compara dois desenhos de proteção de notebooks e escreve requisitos de processo de apoio.

> **Caso sintético.** Os desenhos e as entrevistas são sintéticos; Sasse et al. (2001) é real.

### Erros e limites

Os recursos de hardware variam por modelo. Processos de recuperação podem se tornar um caminho de ataque.

### Exercícios

- **EX022 — Chips invisíveis.** Como os usuários sentem o hardware seguro? *Rubrica:* 3 = menos senhas e passos mais simples;; 2 = mais simples;; 1 = nada;; 0 = nenhuma.
- **EX023 — Escolha do notebook.** Por que preferir o PIN apoiado em hardware nos notebooks de campo? *Rubrica:* 3 = proteção semelhante sem engenheiros anotando senhas nos notebooks;; 2 = usabilidade;; 1 = nada;; 0 = nenhuma.
- **EX024 — Requisito para chaves perdidas.** Que requisito de processo trata das chaves de segurança perdidas? *Rubrica:* 3 = chaves reservas nos depósitos e recuperação rápida;; 2 = reservas;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar um programa que processa e-mails reportados; (2) desenhar estruturas de dados para a triagem; (3) proteger a privacidade no processamento automatizado.

### 9.1 Um programa de triagem

A equipe de segurança da Greyford recebe muitos e-mails reportados. Aiko escreve um programa que agrupa os reportes do mesmo e-mail, conta quantos funcionários reportaram cada um e registra o horário do primeiro reporte. Agrupar reduz a carga da equipe, porque vinte reportes de um mesmo e-mail de phishing exigem uma só investigação. Ela estrutura o programa em funções pequenas para leitura, agrupamento e resumo, cada uma testada separadamente, para que mudanças futuras sejam mais seguras. Escreve um teste curto para cada função usando pequenas listas de reportes feitas à mão, de modo que qualquer mudança posterior que quebre o agrupamento ou a contagem de tempo seja notada imediatamente, e não descoberta durante um incidente real.

### Laboratório — Agrupamento de reportes duplicados e tempo até o primeiro reporte

```python
# Group duplicate reported emails and find first-report delay (synthetic; minutes after arrival).
reports = [("payroll@greyf0rd.co", "Update your bank details", m) for m in (9, 11, 12, 14, 15, 18, 20, 22, 25, 30, 33, 40, 41, 45)] + \
          [("it-help@vendorx.io", "Mailbox full", m) for m in (25, 31, 38, 47, 52, 60, 66, 70, 75)] + \
          [("news@supplier.example", "Monthly newsletter", m) for m in (120, 180, 200)] + \
          [("dhl-track@parcel.example", "Missed delivery", m) for m in (16, 19, 27, 29, 35, 44, 48)] + \
          [("ceo.greyford@gmail.example", "Quick favour", m) for m in (14, 17, 26, 39, 55)] + \
          [("hr@greyford.example", "Benefits survey", m) for m in (90, 95)]
groups = {}
for sender, subject, m in reports:
    key = (sender, subject.lower()); c, first = groups.get(key, (0, 10**9)); groups[key] = (c + 1, min(first, m))
print(f"{len(reports)} reports -> {len(groups)} distinct emails")
for (s, subj), (c, first) in sorted(groups.items(), key=lambda x: -x[1][0]):
    print(f"{c:3d} reports, first after {first:3d} min: {subj} <{s}>")
```

Execute com `python3 lab_triage.py`. Saída verificada:

```text
40 reports -> 6 distinct emails
 14 reports, first after   9 min: update your bank details <payroll@greyf0rd.co>
  9 reports, first after  25 min: mailbox full <it-help@vendorx.io>
  7 reports, first after  16 min: missed delivery <dhl-track@parcel.example>
  5 reports, first after  14 min: quick favour <ceo.greyford@gmail.example>
  3 reports, first after 120 min: monthly newsletter <news@supplier.example>
  2 reports, first after  90 min: benefits survey <hr@greyford.example>
```

### 9.2 Estruturas de dados

Aiko usa um dicionário indexado por uma impressão digital do remetente e do assunto de cada e-mail. Cada entrada guarda a contagem e o horário do primeiro reporte. Essa estrutura torna o agrupamento rápido mesmo com milhares de reportes. O laboratório mostra que quarenta reportes se reduzem a seis e-mails distintos e que o e-mail mais reportado teve seu primeiro reporte nove minutos após a chegada. Esse tempo até o primeiro reporte é o número-chave da exposição, que remete ao modelo de cálculo do capítulo 1. Ela observa que um remetente digitado de forma ligeiramente diferente poderia dividir uma campanha em dois grupos, e acrescenta uma opção de fusão manual.

### 9.3 Privacidade no processamento

E-mails reportados podem conter informações pessoais. O programa de Aiko guarda apenas o remetente, a impressão digital do assunto e os horários dos reportes, e não o corpo das mensagens nem os nomes de quem reportou. A equipe de segurança pode abrir o e-mail original em uma ferramenta controlada quando necessário. Ela documenta o que o programa guarda e por quê. Minimizar os dados guardados em ferramentas automatizadas reduz o risco caso o banco de dados da ferramenta seja exposto, e tranquiliza os funcionários de que reportar não expõe a própria caixa de e-mail. Ela compartilha a lista de campos guardados com os representantes dos funcionários, que a recebem bem e concordam em mencioná-la ao divulgar o botão de reporte.

### Exemplo resolvido

Aiko escreve um programa de triagem testado que agrupa reportes duplicados com um dicionário, encontra o tempo até o primeiro reporte e guarda dados mínimos.

> **Caso sintético.** Os reportes são sintéticos.

### Erros e limites

Impressões digitais podem separar variantes de uma mesma campanha. O armazenamento mínimo pode limitar investigações posteriores.

### Exercícios

- **EX025 — Benefício do agrupamento.** Por que agrupar reportes duplicados? *Rubrica:* 3 = muitos reportes de um e-mail exigem uma só investigação;; 2 = carga de trabalho;; 1 = nada;; 0 = nenhuma.
- **EX026 — Agrupamento no laboratório.** A quantos e-mails distintos os quarenta reportes se reduziram no laboratório? *Rubrica:* 3 = seis, o principal com primeiro reporte após 9 minutos;; 2 = seis;; 1 = quarenta;; 0 = nenhuma.
- **EX027 — Campos guardados.** O que o programa de triagem guarda? *Rubrica:* 3 = apenas remetente, impressão digital do assunto e horários dos reportes;; 2 = mínimo;; 1 = corpos;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética da engenharia ao trabalho de conscientização em segurança; (2) desenhar simulações de phishing éticas; (3) equilibrar deveres de segurança operacional com o bem-estar dos funcionários.

### 10.1 Ética no trabalho de conscientização

A Profa. Kerr lembra à turma que os engenheiros têm deveres para com o público, os empregadores e os colegas. Programas de conscientização afetam a dignidade e a confiança das pessoas. As simulações de phishing, em particular, envolvem engano. Aiko aprende que o engano só se justifica quando serve a um propósito claro de segurança, é aprovado pela organização, evita danos e é seguido de uma explicação honesta. Tratar colegas como adversários a serem flagrados mina a cooperação da qual a segurança depende, como argumentaram Adams e Sasse (1999). Ela escreve essas condições no início de suas notas de desenho das simulações.

### 10.2 Um desenho ético de simulação

Aiko rascunha regras para a Greyford: as simulações são aprovadas pela direção e pelos representantes dos funcionários; os funcionários são avisados, de forma geral, de que simulações acontecem; nenhuma isca explora medos sobre salário, saúde, família ou demissão; as páginas de destino nunca pedem senhas reais e registram apenas que um link foi aberto; os resultados são relatados apenas de forma agregada; ninguém é punido por clicar; e todos que clicam veem uma explicação curta e gentil sobre como reportar da próxima vez. Ela cita a NIST Phish Scale para manter a dificuldade consistente.

### 10.3 Segurança operacional e bem-estar

Os operadores da sala de controle da Greyford lidam com alarmes críticos para a segurança. Aiko recomenda que as simulações nunca sejam enviadas aos consoles da sala de controle durante os turnos, porque a distração poderia afetar o tratamento da água. Em vez disso, os operadores recebem as simulações em suas contas administrativas, em horários mais tranquilos. Ela também propõe um canal para que os funcionários manifestem preocupações sobre qualquer simulação. Ética e segurança operacional se alinham aqui: uma simulação que distraísse um operador durante um alarme criaria um risco real para o público que ela pretende proteger. O gerente da planta aprova a regra.

### Exemplo resolvido

Aiko declara as condições para um engano justificado, rascunha sete regras éticas para simulações e mantém as simulações longe dos consoles críticos para a segurança.

> **Caso sintético.** As regras e os ambientes são sintéticos; Adams e Sasse (1999) e a NIST Phish Scale são reais.

### Erros e limites

Mesmo simulações éticas podem incomodar alguns funcionários. As regras precisam de revisão à medida que as ameaças mudam.

### Exercícios

- **EX028 — Engano justificado.** Quando o engano em simulações pode ser justificado? *Rubrica:* 3 = propósito claro de segurança, aprovação, ausência de dano e explicação honesta depois;; 2 = condições;; 1 = sempre;; 0 = nenhuma.
- **EX029 — Iscas proibidas.** Que temas de isca são excluídos? *Rubrica:* 3 = medos sobre salário, saúde, família e demissão;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX030 — Regra da sala de controle.** Por que evitar simulações nos consoles da sala de controle durante os turnos? *Rubrica:* 3 = a distração poderia afetar a segurança do tratamento da água;; 2 = segurança;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar como a autenticação de e-mail ajuda os usuários; (2) relacionar os sinais dos protocolos ao que os usuários veem; (3) desenhar avisos sobre os quais as pessoas consigam agir.

### 11.1 Autenticação de e-mail

Aiko estuda como o e-mail trafega pelas redes e como os domínios publicam registros que permitem aos servidores de destino verificar se uma mensagem realmente veio deles. Quando as verificações falham, o sistema de destino pode marcar ou rejeitar a mensagem. Na Greyford, muitos e-mails de phishing imitam o próprio domínio da companhia. Verificações de domínio robustas barram boa parte deles antes que os funcionários os vejam. Aiko observa que cada ataque barrado por um protocolo é um ataque que nenhuma pessoa precisa julgar, e essa é a forma mais confiável de projeto em fatores humanos.

### 11.2 Os sinais que os usuários veem

Algumas verificações resultam em sinais exibidos aos usuários, como uma faixa dizendo que a mensagem veio de fora da organização. Aiko examina como os funcionários leem essa faixa. Entrevistas mostram que, como quase todo e-mail de fornecedor a exibe, os funcionários a ignoram. O sinal é tecnicamente correto, mas carrega pouca informação. Ela propõe mostrar um aviso mais forte apenas para remetentes externos que usam nomes parecidos com os de funcionários internos, o que é mais raro e mais significativo. Testa a ideia em um mês de logs sintéticos de e-mail e descobre que o aviso mais forte apareceria em cerca de duas mensagens por pessoa por mês, raro o bastante para ser notado.

### 11.3 Avisos acionáveis

Aiko aplica lições da pesquisa em segurança utilizável. Whitten e Tygar (1999) mostraram que interfaces de segurança confundem os usuários quando exigem a compreensão de conceitos que eles não têm. Um bom aviso diz em palavras simples o que está errado e oferece uma única ação clara, como reportar o e-mail. Aiko rascunha um aviso: "Este remetente é de fora da Greyford, mas usa o nome de um colega da Greyford. Se tiver dúvida, pressione Reportar." Ela o testa com dez funcionários, dos quais oito escolhem corretamente reportar. Dois perguntaram o que significava colega da Greyford, então ela acrescenta um exemplo.

### Exemplo resolvido

Aiko explica as verificações de domínio, encontra uma faixa de remetente externo ignorada e desenha um aviso mais raro e acionável, testado com funcionários.

> **Caso sintético.** Os avisos e os testes são sintéticos; Whitten e Tygar (1999) é real.

### Erros e limites

A detecção de nomes parecidos tem falsos positivos. Avisos perdem força quando usados em excesso.

### Exercícios

- **EX031 — Valor dos protocolos.** Por que ataques barrados por protocolos são valiosos para os fatores humanos? *Rubrica:* 3 = nenhuma pessoa precisa julgá-los;; 2 = sem julgamento;; 1 = nada;; 0 = nenhuma.
- **EX032 — Faixa ignorada.** Por que os funcionários ignoram a faixa de remetente externo? *Rubrica:* 3 = quase todo e-mail de fornecedor a exibe;; 2 = frequente demais;; 1 = nada;; 0 = nenhuma.
- **EX033 — Teste do aviso.** Quantos de dez funcionários escolheram reportar com o novo aviso? *Rubrica:* 3 = oito;; 2 = 8;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) examinar como os prompts do sistema operacional afetam o comportamento; (2) reduzir prompts de segurança desnecessários; (3) desenhar padrões de menor privilégio que as pessoas aceitem.

### 12.1 Prompts e hábitos

Aiko conta os prompts de segurança que os notebooks administrativos da Greyford exibem em uma semana: lembretes de atualização, pedidos de permissão, avisos de certificado e prompts de administrador. Os funcionários veem dezenas. A maioria é rotineira, então as pessoas clicam adiante por hábito. Quando aparece um prompt raro e perigoso, o hábito se mantém. Herley (2009) argumentou que pedir aos usuários que avaliem avisos frequentes, em sua maioria inofensivos, é um mau negócio para eles. Reduzir os prompts rotineiros faz os importantes se destacarem. Ela registra a contagem semanal por notebook como linha de base antes de mudar qualquer coisa, para que o efeito das mudanças posteriores possa ser medido.

### 12.2 Remover prompts

Aiko trabalha com a equipe de TI para remover prompts. As atualizações passam a ser instaladas automaticamente fora do horário de trabalho. Softwares comuns são pré-aprovados, de modo que os funcionários não precisam pedir direitos de administrador para instalá-los. Os avisos de certificado dos sistemas internos são eliminados com a correção dos certificados internos. Depois das mudanças, os prompts semanais por notebook caem bruscamente. Os funcionários notam menos interrupções, e a equipe de TI recebe menos chamados sobre prompts. Ela mede a mudança contando os prompts em dez notebooks durante uma semana antes e uma depois, e compartilha os resultados com os funcionários, junto com uma explicação curta de quais prompts ainda importam e por que devem ser lidos.

### 12.3 Menor privilégio aceito

Retirar os direitos de administrador local costuma encontrar resistência. Aiko desenha uma abordagem que os funcionários aceitam: um catálogo de autoatendimento para softwares aprovados, uma via rápida de pedidos para todo o resto, com resposta em até uma hora útil, e direitos temporários para engenheiros que precisem deles em tarefas específicas. O menor privilégio dá certo quando seus custos para os funcionários são baixos. Ela mede a aceitação contando pedidos e reclamações durante um mês após a mudança. Também pede aos representantes dos funcionários que revisem a abordagem antes do lançamento, e eles sugerem incluir no catálogo ferramentas de engenharia de uso comum, o que reduz os pedidos no primeiro mês.

### Exemplo resolvido

Aiko conta os prompts semanais, remove os rotineiros por meio de automação e pré-aprovação e desenha o menor privilégio com um catálogo e pedidos rápidos.

> **Caso sintético.** As contagens e os processos são sintéticos; Herley (2009) é real.

### Erros e limites

Atualizações automáticas podem quebrar softwares. Direitos temporários precisam de verificações de expiração.

### Exercícios

- **EX034 — Risco do hábito.** Por que prompts rotineiros e frequentes são perigosos? *Rubrica:* 3 = o clique por hábito se estende aos prompts raros e perigosos;; 2 = hábito;; 1 = nada;; 0 = nenhuma.
- **EX035 — Correção de certificados.** Como os avisos de certificado internos foram removidos? *Rubrica:* 3 = com a correção dos certificados internos;; 2 = corrigir certificados;; 1 = ignorar;; 0 = nenhuma.
- **EX036 — Desenho da aceitação.** O que torna o menor privilégio aceitável para os funcionários? *Rubrica:* 3 = catálogo de autoatendimento, pedidos em uma hora e direitos temporários;; 2 = custo baixo;; 1 = nada;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) desenhar um modelo de dados para informações de conscientização e de reportes; (2) aplicar minimização e retenção; (3) prevenir o mau uso de dados de comportamento.

### 13.1 Um modelo de dados

Aiko desenha um pequeno banco de dados para o programa de conscientização da Greyford. As tabelas guardam campanhas, classificações de dificuldade das iscas, resultados agregados por grupo e impressões digitais dos e-mails reportados. Ela omite deliberadamente uma tabela que ligue funcionários individuais aos cliques em simulações. A Profa. Kerr pergunta por quê; Aiko explica que registros individuais de cliques convidam ao mau uso, como aparecer em avaliações de desempenho, e não são necessários para avaliar o programa. Escolhas de projeto em sistemas de dados codificam decisões de política sobre como as pessoas serão tratadas. Ela apresenta o esquema ao RH e aos representantes dos funcionários antes de construí-lo.

### 13.2 Minimização e retenção

Quando dados individuais são inevitáveis, como a conclusão de treinamentos exigida por regulação, Aiko guarda apenas as datas de conclusão, e não as notas dos questionários. Os registros são apagados dois anos depois que a pessoa sai da empresa. Os resultados agregados são mantidos por mais tempo para análise de tendências. Ela documenta a finalidade e a retenção de cada campo em um dicionário de dados. A ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) espera que as informações sejam tratadas segundo regras acordadas, e um dicionário de dados é uma forma simples de mostrar quais são as regras. Ela revisa o dicionário com o encarregado de proteção de dados, que o aprova.

### 13.3 Prevenir o mau uso

Aiko acrescenta controles: só dois funcionários da segurança podem consultar o banco; toda consulta é registrada; e resultados de grupos com menos de vinte pessoas são suprimidos. Ela também redige uma declaração de política, aprovada pelo RH e pelos representantes dos funcionários, de que os dados de conscientização não serão usados para fins disciplinares. Controles técnicos e de política, juntos, constroem a confiança que mantém os funcionários reportando os próprios erros, o comportamento de que o programa mais precisa. Ela também agenda uma revisão anual dos logs de consulta por alguém de fora da equipe de segurança, para que qualquer tentativa de buscar indivíduos ou contornar o limite de vinte pessoas seja notada e questionada.

### Exemplo resolvido

Aiko desenha um banco de dados de conscientização sem registros individuais de cliques, define regras de minimização e retenção e acrescenta limites de acesso, de registro e de uso.

> **Caso sintético.** O banco de dados é sintético; a ISO/IEC 27001:2022 é real.

### Erros e limites

Reguladores podem exigir registros individuais. Limites de agregação podem ser contornados com consultas repetidas.

### Exercícios

- **EX037 — Tabela omitida.** Que tabela Aiko omitiu deliberadamente? *Rubrica:* 3 = funcionários individuais ligados aos cliques em simulações;; 2 = tabela de cliques;; 1 = nada;; 0 = nenhuma.
- **EX038 — Registro de conclusão.** O que é guardado para a conclusão obrigatória de treinamentos? *Rubrica:* 3 = apenas datas de conclusão, sem notas de questionários;; 2 = datas;; 1 = notas;; 0 = nenhuma.
- **EX039 — Política de uso.** O que dizia a declaração de política aprovada? *Rubrica:* 3 = os dados de conscientização não serão usados para fins disciplinares;; 2 = sem punição;; 1 = nada;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) aplicar o design centrado no usuário a um recurso de segurança; (2) conduzir testes de usabilidade; (3) acompanhar defeitos de usabilidade como quaisquer outros defeitos.

### 14.1 Design centrado no usuário

A Greyford quer um novo botão de reporte em seu sistema de e-mail. Aiko segue um processo centrado no usuário: entrevistar usuários, esboçar opções, testar protótipos e refinar. As entrevistas mostram que os engenheiros de campo leem e-mails sobretudo no celular, muitas vezes de luvas ou sob luz forte. Um ícone pequeno escondido em um menu não funcionaria para eles. O desenho dela coloca um botão de reporte grande no topo de cada mensagem, tanto no computador quanto no celular. As práticas de engenharia de software se aplicam aos recursos de segurança exatamente como a qualquer outro recurso.

### 14.2 Testes de usabilidade

Aiko testa o protótipo com oito funcionários de funções diferentes. Cada um é convidado a reportar um e-mail suspeito enquanto ela observa sem ajudar. Ela registra o tempo gasto e os erros. Os usuários de computador reportam em menos de cinco segundos; dois usuários de celular têm dificuldade porque o botão sai da tela ao rolar. Ela corrige o botão para que ele permaneça visível. Testes pequenos com usuários reais encontram problemas que os projetistas não conseguem ver, porque já sabem como o recurso funciona. Ela repete o teste no celular depois da correção, e os oito participantes têm sucesso rapidamente.

### 14.3 Acompanhar defeitos de usabilidade

Aiko registra os problemas de usabilidade no mesmo rastreador de defeitos usado para bugs funcionais, com severidade definida por quantos usuários falham e pela importância da tarefa. O botão que some ao rolar é um defeito de alta severidade, porque reportar é a finalidade principal do recurso. Tratar problemas de usabilidade como defeitos garante que sejam corrigidos antes do lançamento, em vez de ficarem como questões de gosto. Sasse, Brostoff e Weirich (2001) argumentaram que uma segurança que as pessoas não conseguem usar de forma eficaz não é uma segurança eficaz. O defeito é corrigido antes do lançamento.

### Exemplo resolvido

Aiko desenha um botão de reporte com entrevistas e protótipos, testa-o com oito usuários, corrige um defeito no celular e acompanha a usabilidade como defeitos.

> **Caso sintético.** Os testes são sintéticos; Sasse et al. (2001) é real.

### Erros e limites

Oito testadores deixam passar problemas raros. Testes em laboratório diferem das condições reais de campo.

### Exercícios

- **EX040 — Condições de campo.** Que condições afetam o uso de e-mail pelos engenheiros de campo? *Rubrica:* 3 = celular, luvas e luz forte;; 2 = condições;; 1 = nada;; 0 = nenhuma.
- **EX041 — Defeito no celular.** Que defeito de usabilidade o teste encontrou? *Rubrica:* 3 = o botão de reporte no celular saía da tela ao rolar;; 2 = rolagem;; 1 = nada;; 0 = nenhuma.
- **EX042 — Severidade do defeito.** Por que o problema de rolagem era de alta severidade? *Rubrica:* 3 = reportar é a finalidade principal do recurso;; 2 = tarefa central;; 1 = cosmético;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) relacionar os conceitos centrais de segurança ao comportamento humano; (2) reconhecer técnicas de engenharia social; (3) mapear as ameaças dirigidas a pessoas na Greyford.

### 15.1 Conceitos e pessoas

Aiko liga confidencialidade, integridade e disponibilidade a ações humanas. Um engenheiro de campo que compartilha uma senha prejudica a confidencialidade; um operador que age com base em uma instrução forjada prejudica a integridade; uma infecção por ransomware iniciada por um anexo malicioso prejudica a disponibilidade. As pessoas aparecem em todas as partes da segurança, como atacantes, alvos e defensores. Ver as pessoas também como defensoras muda as prioridades de projeto, que passam a apoiar o bom comportamento em vez de apenas restringir o mau. Ela escreve um exemplo de pessoa como defensora para cada objetivo, como um engenheiro que reporta uma ligação estranha de um fornecedor antes de agir.

### 15.2 Engenharia social

Aiko estuda como os atacantes manipulam pessoas. Os princípios de influência de Cialdini (2021), como autoridade, urgência, escassez, reciprocidade, afinidade e prova social, explicam por que as iscas funcionam. Hadnagy (2018) descreve como engenheiros sociais combinam pesquisa sobre os alvos com esses princípios. Uma mensagem falsa do diretor-presidente pedindo um pagamento urgente usa autoridade e urgência ao mesmo tempo. Reconhecer os princípios ajuda os funcionários a perceber a pressão e ajuda os projetistas a acrescentar pausas onde a pressão é provável. Ela monta uma tabela de uma página que liga cada princípio a uma isca típica e a uma pausa simples que a interrompe, e a tabela passa a fazer parte do treinamento posterior.

### 15.3 Ameaças na Greyford

Aiko mapeia as ameaças dirigidas a pessoas: phishing de credenciais de acesso remoto, ligações telefônicas de falsos fornecedores pedindo aos operadores que mudem configurações, fraude de faturas contra o setor financeiro e caronas na entrada dos depósitos. Para cada uma, registra o princípio de influência usado e o controle que elimina a dependência do julgamento, como a verificação por retorno de ligação para pedidos de fornecedores. O Verizon Data Breach Investigations Report (2024) é uma fonte anual que acompanha o elemento humano nas violações, e ela o cita como contexto, e não como dado da Greyford. Mantém o mapa curto o bastante para ser revisado a cada trimestre.

### Exemplo resolvido

Aiko liga os objetivos de segurança a ações humanas, aplica os princípios de influência às iscas e mapeia quatro ameaças dirigidas a pessoas, com seus controles.

> **Caso sintético.** As ameaças na Greyford são sintéticas; Cialdini (2021), Hadnagy (2018) e o Verizon DBIR (2024) são reais.

### Erros e limites

Os princípios de influência explicam, mas não preveem, o comportamento individual. Relatórios do setor podem não corresponder aos riscos de uma companhia de saneamento.

### Exercícios

- **EX043 — Pessoas como defensoras.** Por que ver as pessoas também como defensoras? *Rubrica:* 3 = desloca o projeto para apoiar o bom comportamento;; 2 = apoio;; 1 = nada;; 0 = nenhuma.
- **EX044 — Isca do diretor-presidente.** Que princípios um falso pedido urgente de pagamento do diretor-presidente combina? *Rubrica:* 3 = autoridade e urgência;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX045 — Controle para ligações de fornecedores.** Que controle trata das falsas ligações de fornecedores? *Rubrica:* 3 = verificação por retorno de ligação a um número conhecido;; 2 = retorno de ligação;; 1 = nada;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) tratar as pessoas como componentes de um sistema sociotécnico; (2) alocar funções entre pessoas e máquinas; (3) escrever requisitos que incluam o desempenho humano.

### 16.1 Sistemas sociotécnicos

A Profa. Kerr apresenta a engenharia de sistemas: definir necessidades, requisitos, arquitetura, verificação e operação ao longo de todo o ciclo de vida. Aiko aprende que um sistema de segurança na Greyford inclui pessoas, procedimentos e tecnologia trabalhando juntos. Um sistema de acesso remoto não é só software; ele inclui os engenheiros que o usam, o service desk que redefine suas contas e o gestor que aprova o acesso. Tratar as pessoas como parte do sistema, e não como usuários externos, faz com que seus limites e pontos fortes entrem no projeto desde o início, em vez de serem considerados depois.

### 16.2 Alocar funções

Uma pergunta clássica da engenharia de sistemas é quais tarefas cabem às máquinas e quais cabem às pessoas. Aiko a aplica à defesa contra phishing. Filtrar e-mails sabidamente maliciosos, verificar domínios de remetentes e agrupar reportes duplicados são tarefas adequadas às máquinas, que são rápidas e consistentes. Julgar pedidos incomuns, mas plausíveis, como uma instrução inesperada de um fornecedor, é tarefa adequada a pessoas que conhecem o contexto. Ela aloca cada função e observa que não se deve pedir às pessoas que façam o que as máquinas fazem melhor, como conferir cada link manualmente.

### 16.3 Requisitos de desempenho humano

Aiko escreve requisitos que incluem pessoas: um engenheiro de campo deve conseguir reportar um e-mail suspeito em menos de dez segundos pelo celular; um atendente do service desk deve verificar a identidade de quem liga com um procedimento que leve menos de dois minutos; um operador nunca deve ser obrigado a digitar uma senha enquanto reconhece um alarme crítico. Cada requisito é mensurável e testável. A NIST SP 800-160 Vol. 1 Rev. 1 descreve a engenharia de segurança de sistemas ao longo do ciclo de vida, e Aiko observa que o desempenho humano pertence a esses requisitos, ao lado dos técnicos.

### Exemplo resolvido

Aiko trata as pessoas como componentes do sistema, aloca as funções de defesa contra phishing entre máquinas e pessoas e escreve requisitos mensuráveis de desempenho humano.

> **Caso sintético.** Os requisitos são sintéticos; a SP 800-160 Vol. 1 Rev. 1 é real.

### Erros e limites

A alocação de funções muda à medida que as ferramentas melhoram. Limites de tempo podem não servir para todos os funcionários.

### Exercícios

- **EX046 — Pessoas como componentes.** O que muda ao tratar as pessoas como componentes do sistema? *Rubrica:* 3 = seus limites e pontos fortes passam a fazer parte do projeto;; 2 = insumo de projeto;; 1 = nada;; 0 = nenhuma.
- **EX047 — Funções das máquinas.** Que funções de defesa contra phishing cabem às máquinas? *Rubrica:* 3 = filtrar e-mails maliciosos conhecidos, verificar domínios, agrupar reportes;; 2 = duas;; 1 = julgar contexto;; 0 = nenhuma.
- **EX048 — Requisito do alarme.** O que o requisito do operador proíbe? *Rubrica:* 3 = digitar uma senha enquanto reconhece um alarme crítico;; 2 = senha no alarme;; 1 = nada;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) aplicar malhas de realimentação ao comportamento de segurança; (2) desenhar um retorno oportuno para os reportes; (3) evitar realimentações instáveis ou punitivas.

### 17.1 Malhas de realimentação

Na engenharia de controle, uma malha de realimentação mede uma saída e ajusta uma entrada para manter o sistema no alvo. Aiko aplica essa ideia ao comportamento. Quando os funcionários reportam um e-mail suspeito, eles agem; se não recebem nenhuma resposta, a malha fica aberta e eles podem parar de reportar. Se recebem um agradecimento rápido e depois ficam sabendo o que era o e-mail, a malha se fecha e o reporte é reforçado. Ela esboça o processo de reportes da Greyford como uma malha e descobre que, hoje, quem reporta não recebe resposta alguma.

### 17.2 Desenhar um retorno oportuno

Aiko desenha um retorno em três partes: um agradecimento automático em até um minuto, uma mensagem curta quando a equipe de segurança confirma se o e-mail era malicioso ou seguro, e um resumo mensal mostrando como os reportes ajudaram. A rapidez importa: um retorno semanas depois pouco faz para reforçar o comportamento. Ela estima que a automação pode entregar as duas primeiras partes sem tempo extra da equipe. O desenho espelha princípios de controle: medir rápido, responder rápido e manter a malha simples. Ela escreve as três mensagens em linguagem simples e pergunta a cinco funcionários se as achariam úteis, ajustando a redação depois dos comentários.

### Laboratório — Simulação de reportes com e sem retorno

```python
# Illustrative simulation of monthly reporting rate with and without feedback (synthetic dynamics).
def run(feedback, months=12, r=0.30):
    out = []
    for _ in range(months):
        target = 0.60 if feedback else 0.15
        r += 0.35 * (target - r) if feedback else 0.12 * (target - r)
        out.append(r)
    return out
for name, fb in (("no feedback", False), ("quick feedback", True)):
    s = run(fb); print(f"{name:14} month 3 {s[2]:.0%}, month 6 {s[5]:.0%}, month 12 {s[11]:.0%}")
```

Execute com `python3 lab_feedback.py`. Saída verificada:

```text
no feedback    month 3 25%, month 6 22%, month 12 18%
quick feedback month 3 52%, month 6 58%, month 12 60%
```

### 17.3 Malhas instáveis ou punitivas

O retorno também pode causar dano. Se os funcionários que clicam em uma simulação recebem mensagens duras ou são denunciados aos gestores, aprendem a esconder os erros, e a malha conduz ao comportamento errado. Um retorno excessivo, como e-mails diários, faz as pessoas ignorarem todas as mensagens. O laboratório simula os reportes sem retorno e com retorno rápido, mostrando que, com retorno, a taxa de reporte sobe e se estabiliza, enquanto sem ele a taxa vai caindo. Aiko observa que as premissas da simulação são ilustrativas, e não medidas. Recomenda um limite mensal para as mensagens de retorno.

### Exemplo resolvido

Aiko modela o reporte como uma malha de realimentação, desenha um retorno oportuno em três partes e simula seu efeito, advertindo contra malhas punitivas ou excessivas.

> **Caso sintético.** Os parâmetros da simulação são sintéticos.

### Erros e limites

Modelos de malha simples omitem as influências sociais. Agradecimentos automáticos podem parecer pouco sinceros.

### Exercícios

- **EX049 — Malha aberta.** O que acontece quando quem reporta não recebe resposta? *Rubrica:* 3 = a malha fica aberta e os reportes podem diminuir;; 2 = queda;; 1 = nada;; 0 = nenhuma.
- **EX050 — Partes do retorno.** Quais são as três partes do desenho de retorno? *Rubrica:* 3 = agradecimento imediato, confirmação do veredito e resumo mensal;; 2 = duas;; 1 = nada;; 0 = nenhuma.
- **EX051 — Resultado do laboratório.** Como os reportes diferiram no laboratório após 12 meses? *Rubrica:* 3 = 60% com retorno contra 18% sem;; 2 = maior;; 1 = nada;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) situar os fatores humanos na arquitetura de segurança; (2) desenhar defesas em camadas que tolerem o erro humano; (3) usar as ideias de zero trust para reduzir a dependência da vigilância.

### 18.1 Fatores humanos na arquitetura

Aiko estuda como as escolhas de arquitetura moldam o que as pessoas precisam fazer. Se uma única senha roubada dá acesso a tudo, todos os funcionários precisam ser perfeitos o tempo todo. Se o acesso é segmentado e verificado continuamente, um único erro tem impacto limitado. A NIST SP 800-207 descreve o zero trust como a eliminação da confiança implícita baseada na localização na rede e a avaliação de cada pedido de acesso. Aiko o vê como um projeto de fatores humanos: ele reduz o custo dos erros individuais, que são inevitáveis em uma força de trabalho grande. Ela explica essa visão à equipe de TI.

### 18.2 Defesas em camadas

Aiko desenha camadas para o acesso remoto da Greyford: a filtragem de e-mail remove a maior parte do phishing; a autenticação resistente a phishing com chaves de segurança impede que senhas roubadas funcionem; verificações de dispositivo bloqueiam notebooks não gerenciados; o monitoramento detecta acessos incomuns; e os reportes dos funcionários fornecem um alerta precoce. Cada camada captura algumas falhas das outras. Ela enfatiza que os funcionários são uma camada entre muitas, e não a última linha de defesa, um enquadramento que reduz a pressão e a culpa sobre os indivíduos. Desenha as camadas em um diagrama simples para o conselho, mostrando que ameaça cada camada trata e como a falha de uma é capturada por outra, para que ninguém presuma que um único controle basta.

### 18.3 Reduzir a dependência da vigilância

Aiko lista os pontos em que a Greyford depende de que os funcionários percebam algo: conferir nomes de remetentes, identificar páginas de login falsas e verificar mudanças de dados de pagamento. Para cada um, pergunta se a arquitetura pode eliminar essa necessidade. Chaves de segurança tornam ineficazes as páginas de login falsas, porque a chave não se autentica no site errado. Mudanças de pagamento exigem verificação por retorno de ligação feita por uma segunda pessoa. Saltzer e Schroeder (1975) recomendaram projetos que não dependam de usuários constantemente cuidadosos, e Aiko constata que o princípio ainda se ajusta aos sistemas modernos. Ela lista as dependências restantes para revisão.

### Exemplo resolvido

Aiko aplica o zero trust como projeto de fatores humanos, dispõe as defesas em camadas para que os funcionários sejam uma camada entre muitas e elimina várias dependências da vigilância.

> **Caso sintético.** O projeto da Greyford é sintético; a SP 800-207 e Saltzer e Schroeder (1975) são reais.

### Erros e limites

Camadas acrescentam custo e complexidade. Eliminar a necessidade de vigilância pode reduzir o engajamento dos funcionários se for mal explicado.

### Exercícios

- **EX052 — Risco da senha única.** O que acontece se uma única senha roubada dá acesso a tudo? *Rubrica:* 3 = todos os funcionários precisam ser perfeitos o tempo todo;; 2 = perfeição;; 1 = nada;; 0 = nenhuma.
- **EX053 — Funcionários como camada.** Como Aiko posiciona os funcionários no desenho em camadas? *Rubrica:* 3 = como uma camada entre muitas, não a última linha de defesa;; 2 = uma camada;; 1 = última linha;; 0 = nenhuma.
- **EX054 — Benefício da chave de segurança.** Como as chaves de segurança reduzem a dependência da vigilância? *Rubrica:* 3 = não se autenticam em páginas de login falsas;; 2 = resistentes a phishing;; 1 = nada;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) comparar métodos de autenticação por usabilidade e segurança; (2) explicar por que a autenticação resistente a phishing ajuda as pessoas; (3) planejar com os usuários a implantação de um método de autenticação.

### 19.1 Comparar métodos

Aiko compara opções de autenticação para a Greyford: senhas, códigos por SMS, aprovações em aplicativo, códigos em aplicativo e chaves de segurança. Avalia cada uma quanto à resistência a phishing, rapidez, custo e modos de falha. Senhas são fáceis de capturar por phishing e muitas vezes reutilizadas. Códigos por SMS podem ser interceptados ou capturados por phishing em tempo real. Aprovações em aplicativo podem ser abusadas com prompts repetidos até que um usuário cansado aceite. Chaves de segurança resistem ao phishing porque usam criptografia vinculada ao site legítimo e são rápidas depois que os funcionários aprendem a usá-las. Ela resume a comparação em uma tabela.

### 19.2 A criptografia que os usuários nunca veem

Aiko explica aos funcionários que uma chave de segurança guarda uma chave privada que nunca sai do dispositivo. No login, o site envia um desafio, a chave o assina, e o site confere a assinatura com a chave pública correspondente. A chave também verifica a identidade do site, de modo que um site falso não recebe nada de útil. Os funcionários não precisam entender isso para se beneficiar; basta tocar a chave. Um bom projeto criptográfico esconde a complexidade e, ao mesmo tempo, elimina um julgamento que os usuários faziam mal.

### 19.3 Implantar com os usuários

Aiko planeja uma implantação: piloto com vinte voluntários, coleta de problemas, duas chaves por pessoa com uma guardada em local seguro, uma via rápida de recuperação nos depósitos e um treinamento de cinco minutos com um vídeo curto. Ela evita códigos por SMS como alternativa, porque reintroduziriam o risco de phishing. Marca a implantação fora do inverno, quando canos estourados deixam as equipes de campo mais ocupadas. Planejar em torno do trabalho das pessoas é tão importante quanto escolher a tecnologia certa. Ela também combina que os voluntários do piloto atuem como apoio local em cada depósito, já que os colegas muitas vezes preferem perguntar a um par antes de ligar para o service desk.

### Exemplo resolvido

Aiko compara cinco métodos de autenticação, explica as chaves de segurança em termos simples e planeja uma implantação em etapas, com reservas, recuperação e escolha da estação do ano.

> **Caso sintético.** O plano de implantação é sintético.

### Erros e limites

Chaves de segurança exigem logística de reposição. Alguns sistemas talvez ainda não as suportem.

### Exercícios

- **EX055 — Abuso de prompts.** Como as aprovações em aplicativo podem ser abusadas? *Rubrica:* 3 = prompts repetidos até que um usuário cansado aceite;; 2 = fadiga de prompts;; 1 = nada;; 0 = nenhuma.
- **EX056 — Chave e site falso.** Por que um site falso não obtém nada de útil de uma chave de segurança? *Rubrica:* 3 = a chave verifica a identidade do site antes de assinar;; 2 = verificação de origem;; 1 = nada;; 0 = nenhuma.
- **EX057 — Sem SMS como alternativa.** Por que evitar códigos por SMS como alternativa? *Rubrica:* 3 = reintroduziriam o risco de phishing;; 2 = phishing;; 1 = custo;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Fatores humanos e política cibernética: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) definir o campo de fatores humanos e política cibernética; (2) relacionar as políticas às decisões de engenharia; (3) identificar as partes interessadas na Greyford.

### 20.1 Definir o campo

Aiko começa a parte especializada do curso. Fatores humanos e política cibernética estuda como as pessoas interagem com a segurança e como regras, programas e leis moldam essa interação. O campo abrange a usabilidade das ferramentas de segurança, a conscientização e o treinamento, a cultura organizacional, a engenharia social e o desenho de políticas. Sasse, Brostoff e Weirich (2001) defenderam uma abordagem que trata os usuários como parceiros e projeta a segurança em torno deles. Aiko observa que o campo é tanto engenharia quanto psicologia, porque produz requisitos, projetos e medições. Ela escreve uma definição de um parágrafo em seu caderno.

### 20.2 Política e engenharia

As políticas definem requisitos que os engenheiros precisam atender. A política de segurança da informação da Greyford exige treinamento anual de conscientização, autenticação forte para acesso remoto e reporte de incidentes. A NIST SP 800-50 Rev. 1 trata a conscientização e o treinamento como um programa de aprendizagem, com levantamento de necessidades, desenho, execução e avaliação. Aiko percebe que as escolhas de engenharia determinam se a política é viável: um requisito de reporte pouco significa sem um botão de reporte fácil. Ela decide ler as políticas como um conjunto de restrições e objetivos de projeto. Marca cada cláusula da política com o recurso de projeto que a torna alcançável e encontra duas cláusulas sem nenhum recurso de apoio.

### 20.3 Partes interessadas

Aiko lista as partes interessadas: operadores, engenheiros de campo, equipe administrativa, gestores, a equipe de segurança, o RH, os representantes dos funcionários, o regulador dos serviços de água e o público que depende de água segura. Cada uma tem seus interesses. Os operadores querem o mínimo de interrupções; o RH quer tratamento justo; o regulador quer evidências de boas práticas; o público quer água segura e confiável. Ela registra isso em uma tabela de partes interessadas. A Profa. Kerr observa que o trabalho em fatores humanos fracassa quando serve a uma só parte interessada, geralmente a direção, e ignora as demais. Depois de um lembrete, ela acrescenta os terceirizados.

### Exemplo resolvido

Aiko define o campo, lê as políticas como restrições de projeto e mapeia nove grupos de partes interessadas com seus interesses.

> **Caso sintético.** A política da Greyford é sintética; Sasse et al. (2001) e a SP 800-50 Rev. 1 são reais.

### Erros e limites

Listas de partes interessadas podem omitir grupos discretos, como os terceirizados. Resumos de políticas simplificam deveres legais.

### Exercícios

- **EX058 — Escopo do campo.** Cite três temas de fatores humanos e política cibernética. *Rubrica:* 3 = usabilidade, conscientização e treinamento, cultura, engenharia social, desenho de políticas;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX059 — Políticas como restrições.** Como Aiko escolhe ler as políticas? *Rubrica:* 3 = como restrições e objetivos de projeto;; 2 = restrições;; 1 = só regras;; 0 = nenhuma.
- **EX060 — Modo de falha.** Quando o trabalho em fatores humanos fracassa, segundo a Profa. Kerr? *Rubrica:* 3 = quando serve a uma só parte interessada;; 2 = uma parte interessada;; 1 = nada;; 0 = nenhuma.

<a id="ch-21"></a>

## Capítulo 21 — Fatores humanos e política cibernética: requisitos

### Objetivos de aprendizagem

Você vai (1) levantar requisitos de fatores humanos com os funcionários; (2) escrevê-los de forma testável; (3) priorizar os requisitos com as partes interessadas.

### 21.1 Levantar requisitos

Aiko conduz oficinas curtas com operadores, engenheiros de campo e equipe administrativa para entender o que o programa de conscientização e de reportes precisa alcançar para eles. Pergunta sobre e-mails suspeitos recentes, o que os tornou difíceis de julgar e o que os impediu de reportar. Os operadores dizem que não podem deixar os consoles para ler treinamentos longos. Os engenheiros dizem que leem e-mails no celular, dentro das vans. A equipe administrativa diz ter medo de parecer tola se reportar um e-mail legítimo. Cada afirmação se torna um requisito candidato, fundamentado na experiência real, e não em suposições feitas no escritório de segurança.

### 21.2 Requisitos testáveis

Aiko reescreve cada necessidade como um requisito testável. Os módulos de treinamento para operadores devem durar no máximo cinco minutos e poder ser usados em períodos tranquilos. O reporte deve funcionar no celular com um toque. Todo reporte, inclusive os que se revelam inofensivos, deve receber um agradecimento em até um minuto. Nenhum resultado de simulação pode ser compartilhado nominalmente com os gestores diretos. Cada requisito tem uma medida e um teste. Ela evita frases vagas como os funcionários devem estar conscientes, que não podem ser verificadas e, por isso, não conseguem orientar o projeto.

### 21.3 Priorizar

Com vinte requisitos candidatos e orçamento limitado, Aiko conduz uma sessão de priorização com representantes de cada grupo e a equipe de segurança. Eles ordenam os requisitos pelo risco reduzido, pelo benefício para os funcionários e pelo custo. O reporte com um toque no celular e os agradecimentos rápidos ficam no topo, porque são baratos e atacam a barreira mais comum. Uma plataforma completa de simulação fica mais abaixo, porque a ferramenta existente pode ser configurada. Ela registra a ordem e os motivos, para que decisões posteriores possam remeter a eles. A ordem é compartilhada com todos os funcionários em uma nota curta, para que as pessoas vejam que suas preocupações foram ouvidas.

### Exemplo resolvido

Aiko levanta necessidades de três grupos de funcionários, reescreve-as como requisitos testáveis e prioriza vinte deles com as partes interessadas.

> **Caso sintético.** As oficinas e os requisitos são sintéticos.

### Erros e limites

Os participantes das oficinas podem não representar os funcionários mais discretos. As prioridades refletem quem comparece.

### Exercícios

- **EX061 — Medo da equipe administrativa.** Que barreira a equipe administrativa descreveu? *Rubrica:* 3 = medo de parecer tola ao reportar um e-mail legítimo;; 2 = constrangimento;; 1 = nada;; 0 = nenhuma.
- **EX062 — Requisito vago.** Por que evitar "os funcionários devem estar conscientes" como requisito? *Rubrica:* 3 = não pode ser verificado;; 2 = não testável;; 1 = nada;; 0 = nenhuma.
- **EX063 — Prioridades principais.** Que requisitos ficaram no topo? *Rubrica:* 3 = reporte com um toque no celular e agradecimentos rápidos;; 2 = os dois;; 1 = plataforma;; 0 = nenhuma.

<a id="ch-22"></a>

## Capítulo 22 — Fatores humanos e política cibernética: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) modelar o programa de conscientização como um sistema; (2) modelar os fluxos de dados dos reportes e das simulações; (3) identificar onde as pessoas tomam decisões.

### 22.1 O programa como sistema

Aiko modela o programa de conscientização da Greyford como um sistema com entradas, processos e saídas. As entradas incluem inteligência de ameaças, necessidades dos funcionários e requisitos de política. Os processos incluem treinamento, simulações, reportes, triagem e retorno. As saídas incluem reportes mais rápidos, menos ataques bem-sucedidos e evidências para o regulador. Modelar o programa dessa forma mostra que o treinamento é apenas um processo entre vários e que a saída que importa à Greyford depende de reportes e triagem funcionarem bem juntos. Ela desenha o modelo em um diagrama de uma página e o usa para explicar aos gestores por que investir apenas em treinamento deixaria a maior parte do sistema inalterada e pouco afetaria os resultados que eles desejam.

### 22.2 Fluxos de dados

Aiko desenha os fluxos de dados: os funcionários reportam e-mails ao sistema de triagem; a triagem devolve vereditos a quem reportou; os resultados das simulações seguem de forma agregada para um dashboard; a conclusão dos treinamentos segue para os registros do RH. Ela marca onde aparecem dados pessoais e onde eles são agregados. Um fluxo a preocupa: por padrão, a ferramenta de simulação exporta resultados individuais para uma planilha que os gestores podem abrir. Ela recomenda desligar a exportação e configurar apenas relatórios agregados, em coerência com a política do capítulo 13. O fornecedor confirma que a mudança pode ser travada pelos administradores.

### 22.3 Pontos de decisão

Aiko marca cada ponto em que uma pessoa toma uma decisão: um funcionário decidindo se reporta, um analista de triagem decidindo se um e-mail é malicioso, um gestor decidindo se aprova um acesso e um operador decidindo se age com base em um pedido por telefone. Para cada um, anota que informação a pessoa tem, quanto tempo e que pressão. Pontos de decisão com pouca informação e muita pressão, como pedidos urgentes por telefone, são onde a engenharia social tem sucesso, e por isso merecem atenção de projeto em primeiro lugar.

### Exemplo resolvido

Aiko modela o programa como um sistema, mapeia os fluxos de dados e interrompe uma exportação de resultados individuais, e marca os pontos de decisão com suas pressões.

> **Caso sintético.** Os modelos e as ferramentas são sintéticos.

### Erros e limites

Os modelos omitem canais informais, como mensagens de chat. As configurações padrão mudam com as atualizações das ferramentas.

### Exercícios

- **EX064 — Saída do programa.** Que saída mais importa à Greyford? *Rubrica:* 3 = reportes mais rápidos e menos ataques bem-sucedidos;; 2 = resultados;; 1 = conclusão;; 0 = nenhuma.
- **EX065 — Problema da exportação.** Que fluxo de dados preocupou Aiko? *Rubrica:* 3 = resultados individuais de simulação exportados para uma planilha dos gestores;; 2 = exportação;; 1 = nada;; 0 = nenhuma.
- **EX066 — Pontos de decisão arriscados.** Que pontos de decisão merecem atenção primeiro? *Rubrica:* 3 = os com pouca informação e muita pressão, como pedidos urgentes por telefone;; 2 = pressão;; 1 = nada;; 0 = nenhuma.

<a id="ch-23"></a>

## Capítulo 23 — Fatores humanos e política cibernética: análise de ameaças e falhas

### Objetivos de aprendizagem

Você vai (1) analisar como se desenrolam os ataques de engenharia social; (2) classificar erros humanos; (3) desenhar defesas para cada tipo de falha.

### 23.1 Sequências de ataque

Aiko analisa uma sequência realista: um atacante pesquisa os funcionários da Greyford na internet, envia a um engenheiro de campo uma mensagem se passando por um fornecedor de bombas sobre um problema urgente de firmware, faz em seguida uma ligação e pede ao engenheiro que aprove uma sessão remota. Hadnagy (2018) descreve esse tipo de pretexto em várias etapas. Cada etapa oferece uma chance de deter o ataque: limitar o que os funcionários publicam, verificar os contatos de fornecedores, retornar ligações para números conhecidos e exigir a aprovação de uma segunda pessoa para sessões remotas. Ela desenha a sequência como uma linha do tempo, com cada oportunidade de defesa marcada.

### 23.2 Classificar erros

Aiko usa a distinção entre deslizes, lapsos e enganos estabelecida por Reason (1990). Um deslize é uma ação errada, como clicar no botão errado; um lapso é uma falha de memória, como esquecer de bloquear a tela; um engano é um plano errado, como acreditar que um falso fornecedor é legítimo. Cada um exige uma defesa diferente: deslizes pedem interfaces tolerantes, lapsos pedem lembretes ou automação, e enganos pedem informação melhor ou verificação. Classificar os erros interrompe a resposta padrão de mais treinamento para todo problema.

### 23.3 Defesas por tipo

Aiko mapeia as defesas. Para os deslizes, o botão de reporte tem um desfazer e há uma confirmação para o envio de arquivos sensíveis para fora. Para os lapsos, as telas se bloqueiam automaticamente e as chaves de segurança eliminam as senhas esquecidas. Para os enganos, pedidos de fornecedores exigem verificação por retorno de ligação, e os funcionários recebem orientações curtas sobre os pretextos comuns. Ela também registra as violações, a quebra deliberada de regras, que muitas vezes sinalizam regras impraticáveis, e não má intenção, como constataram Adams e Sasse (1999). As violações a levam a revisar as regras antes de reforçá-las. Ela apresenta o mapeamento como uma tabela que a equipe de segurança pode ampliar quando ocorrerem novos incidentes, para que cada falha futura seja classificada antes da escolha da resposta.

### Exemplo resolvido

Aiko analisa um pretexto em várias etapas, classifica os erros em deslizes, lapsos e enganos e associa defesas a cada tipo, tratando as violações como sinais.

> **Caso sintético.** O ataque é sintético; Hadnagy (2018), Reason (1990) e Adams e Sasse (1999) são reais.

### Erros e limites

Na prática, as categorias de erro se sobrepõem. Os atacantes se adaptam às etapas de verificação conhecidas.

### Exercícios

- **EX067 — Etapas do pretexto.** Que etapas compõem o pretexto do fornecedor? *Rubrica:* 3 = pesquisa online, e-mail falsificado, ligação de acompanhamento, pedido de sessão remota;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX068 — Defesa contra lapsos.** O que defende contra os lapsos? *Rubrica:* 3 = lembretes ou automação, como o bloqueio automático;; 2 = automação;; 1 = treinamento;; 0 = nenhuma.
- **EX069 — Violações como sinais.** O que as violações costumam sinalizar? *Rubrica:* 3 = regras impraticáveis, e não má intenção;; 2 = desenho das regras;; 1 = malícia;; 0 = nenhuma.

<a id="ch-24"></a>

## Capítulo 24 — Fatores humanos e política cibernética: métodos I

### Objetivos de aprendizagem

Você vai (1) conduzir um percurso cognitivo de uma tarefa de segurança; (2) aplicar um questionário curto de forma responsável; (3) combinar métodos para entender um problema.

### 24.1 Percurso cognitivo

Aiko aplica um percurso cognitivo ao processo de redefinição de senha da Greyford. Ela percorre cada ação que o usuário precisa executar, perguntando se ele saberá o que fazer, verá como fazer, entenderá o retorno e saberá que teve sucesso. Descobre que a página de redefinição pede um número de matrícula que a maioria dos funcionários de campo não lembra, e que a mensagem de confirmação é ambígua. Percursos são rápidos, dispensam participantes e encontram muitos problemas cedo, embora dependam de o avaliador imaginar com precisão o usuário.

### 24.2 Um questionário responsável

Aiko aplica um questionário aos funcionários sobre as barreiras ao reporte. O questionário é anônimo, curto e voluntário, e pergunta sobre experiências em vez de testar conhecimentos. Ela evita perguntas indutoras e inclui uma pergunta aberta para comentários. Relata os resultados apenas para grupos de vinte pessoas ou mais. Cento e oitenta funcionários respondem. A barreira mais comum é não saber se algo é suspeito o bastante para ser reportado, seguida de não saber como reportar pelo celular. Ela compartilha os principais resultados com todos os funcionários em até duas semanas, agradecendo e explicando o que vai mudar, para que os respondentes vejam que suas respostas tiveram efeito.

### Laboratório — Contagens e proporções de barreiras nas respostas ao questionário

```python
# Count reporting barriers from an anonymous survey (synthetic multi-select, n=180).
n = 180
barriers = {"unsure if suspicious enough": 71, "don't know how to report on phone": 48, "worried about looking foolish": 33,
            "no time": 29, "never get feedback": 41, "didn't know reporting existed": 12}
for b, c in sorted(barriers.items(), key=lambda x: -x[1]): print(f"{b:34} {c:3d}/{n} = {c/n:.0%}")
```

Execute com `python3 lab_survey.py`. Saída verificada:

```text
unsure if suspicious enough         71/180 = 39%
don't know how to report on phone   48/180 = 27%
never get feedback                  41/180 = 23%
worried about looking foolish       33/180 = 18%
no time                             29/180 = 16%
didn't know reporting existed       12/180 = 7%
```

### 24.3 Combinar métodos

O percurso encontrou problemas de usabilidade; o questionário encontrou incerteza sobre quando reportar. Juntos, eles sugerem duas correções: melhorar as interfaces de redefinição e de reporte e dizer claramente aos funcionários que qualquer dúvida é um bom motivo para reportar. Aiko observa que nenhum dos métodos, sozinho, teria mostrado as duas coisas. Ela planeja em seguida testes de usabilidade com usuários reais, já que percursos e questionários descrevem problemas, mas não mostram como as pessoas de fato se comportam ao usar o sistema. Registra como cada achado foi obtido, para que os leitores saibam quais afirmações se apoiam em revisão de especialista e quais em relatos dos funcionários, e marca os testes de usabilidade para o mês seguinte.

### Exemplo resolvido

Aiko faz o percurso de uma tarefa de redefinição e encontra dois problemas, aplica de forma responsável um questionário sobre barreiras ao reporte e combina os dois métodos em duas correções.

> **Caso sintético.** O questionário e os achados são sintéticos.

### Erros e limites

Percursos dependem da imaginação do avaliador. Questionários medem percepções, não comportamentos.

### Exercícios

- **EX070 — Perguntas do percurso.** Que quatro perguntas orientam cada passo do percurso? *Rubrica:* 3 = saber o que fazer, ver como, entender o retorno, saber que teve sucesso;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX071 — Principal barreira.** Qual foi a barreira ao reporte mais comum no laboratório? *Rubrica:* 3 = não saber se é suspeito o bastante: 71 de 180;; 2 = incerteza;; 1 = celular;; 0 = nenhuma.
- **EX072 — Mensagem clara.** Que mensagem trata dessa barreira? *Rubrica:* 3 = qualquer dúvida é um bom motivo para reportar;; 2 = dúvida;; 1 = nada;; 0 = nenhuma.

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) desenhar em equipe um serviço de reporte e retorno; (2) criticar projetos em um ambiente de ateliê; (3) iterar com base no retorno recebido.

### 25.1 O briefing do ateliê

A Profa. Kerr conduz um ateliê de projeto. A equipe de quatro pessoas de Aiko precisa desenhar um serviço de reporte e retorno para uma operadora regional de transporte fictícia, com motoristas, funcionários de garagem e equipes administrativas. Os requisitos incluem reporte com um toque, retorno rápido e nenhuma culpa individual. A equipe inclui um estudante de computação, uma estudante de psicologia e um estudante de design. Trabalhar entre disciplinas traz ideias diferentes: a estudante de psicologia sugere enquadrar os reportes como uma ajuda aos colegas, e não como um dever de segurança. A equipe combina papéis e cronograma na primeira reunião, e cada membro lidera uma parte do projeto.

### 25.2 Crítica no ateliê

Na crítica intermediária, outras equipes e dois profissionais revisam os projetos. Um profissional aponta que os motoristas não podem usar o celular enquanto dirigem, então o reporte também precisa funcionar em terminais da garagem e por uma simples ligação para uma central. Outro revisor questiona se o resumo mensal será lido. A equipe de Aiko ouve sem se defender e registra cada comentário. A crítica funciona quando os projetistas a tratam como informação, e não como ataque. Eles separam os comentários em obrigatórios e desejáveis antes da sessão seguinte e combinam quem vai tratar de cada um.

### 25.3 Iterar

A equipe revisa o projeto. Acrescenta o reporte pelos terminais da garagem e uma central telefônica, reduz o resumo mensal a três itens com uma imagem e testa o novo enquadramento com cinco funcionários de garagem, que o preferem. Documenta o que mudou e por quê. Na crítica final, os profissionais observam que o projeto agora se ajusta à jornada dos motoristas. Aiko aprende que iterar com base em restrições reais produz projetos que as pessoas de fato usam. A equipe também mantém um log de mudanças curto, listando cada revisão, o comentário que a motivou e o resultado do pequeno teste com os funcionários de garagem, que os revisores finais usam para ver como o projeto evoluiu.

### Exemplo resolvido

A equipe de Aiko desenha um serviço de reporte para uma operadora de transporte, recebe críticas do ateliê sobre os motoristas e itera com terminais, uma central telefônica e um resumo mais curto.

> **Caso sintético.** A operadora de transporte e a equipe são sintéticas.

### Erros e limites

Projetos de ateliê não sofrem as pressões de uma implantação real. Testes pequenos podem favorecer a novidade.

### Exercícios

- **EX073 — Enquadramento da psicologia.** Que enquadramento a estudante de psicologia sugeriu? *Rubrica:* 3 = reportar como ajuda aos colegas;; 2 = ajuda;; 1 = dever;; 0 = nenhuma.
- **EX074 — Restrição dos motoristas.** Que restrição o profissional levantou? *Rubrica:* 3 = motoristas não podem usar o celular enquanto dirigem;; 2 = direção;; 1 = nada;; 0 = nenhuma.
- **EX075 — Mudanças no projeto.** Cite duas mudanças feitas após a crítica. *Rubrica:* 3 = reporte por terminais da garagem, central telefônica, resumo mais curto;; 2 = duas;; 1 = nada;; 0 = nenhuma.

<a id="ch-26"></a>

## Capítulo 26 — Fatores humanos e política cibernética: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar arquiteturas alternativas para um programa de conscientização em segurança; (2) ponderar as alternativas com critérios humanos e organizacionais; (3) justificar uma escolha de forma aberta.

### 26.1 Três alternativas

Aiko compara três formas de a Greyford organizar seu programa. A primeira é orientada a compliance: um curso online anual e simulações trimestrais medidos pela conclusão e pela taxa de cliques. A segunda é orientada a reportes: reporte fácil, retorno rápido, reciclagens mensais curtas e simulações medidas pela velocidade dos reportes. A terceira é orientada ao projeto: investir principalmente em mudanças técnicas que retirem decisões dos funcionários, como chaves de segurança e filtragem mais forte, com o mínimo de treinamento. Cada uma reflete uma teoria diferente sobre o que torna as pessoas seguras, e cada uma tem pontos fortes que faltam às outras.

### 26.2 Critérios e pontuação

Aiko pontua as alternativas com critérios acordados com as partes interessadas: redução de risco, ônus para os funcionários, custo, evidências regulatórias e confiança dos funcionários. O laboratório calcula os totais ponderados. A opção orientada ao projeto pontua mais alto em risco e ônus, mas é a mais fraca em evidências regulatórias, porque o regulador espera alguns registros de treinamento. A opção orientada a reportes pontua bem na maioria dos critérios. A opção orientada a compliance só é a melhor na facilidade de produzir evidências, o que corresponde à crítica de Bada, Sasse e Nurse (2019) de que essas campanhas raramente mudam comportamentos. As partes interessadas definem os pesos antes de ver qualquer pontuação, o que impede que os pesos sejam ajustados para favorecer uma opção.

### Laboratório — Comparação ponderada de três desenhos de programa

```python
# Weighted comparison of three awareness programme designs (synthetic 1-5 scores).
w = {"risk": 0.30, "burden": 0.20, "cost": 0.15, "evidence": 0.15, "trust": 0.20}
s = {"compliance": {"risk": 2, "burden": 2, "cost": 4, "evidence": 5, "trust": 2},
     "reporting": {"risk": 4, "burden": 4, "cost": 4, "evidence": 3, "trust": 4},
     "design": {"risk": 5, "burden": 5, "cost": 2, "evidence": 2, "trust": 4}}
def tot(wt): return {o: sum(wt[c] * v for c, v in sc.items()) / sum(wt.values()) for o, sc in s.items()}
print("base:", {o: round(v, 2) for o, v in tot(w).items()})
print("evidence weight doubled:", {o: round(v, 2) for o, v in tot(dict(w, evidence=0.30)).items()})
```

Execute com `python3 lab_options.py`. Saída verificada:

```text
base: {'compliance': 2.75, 'reporting': 3.85, 'design': 3.9}
evidence weight doubled: {'compliance': 3.04, 'reporting': 3.74, 'design': 3.65}
```

### 26.3 Uma escolha aberta

Aiko recomenda um híbrido: mudanças técnicas orientadas ao projeto combinadas com o programa orientado a reportes, mantendo um treinamento curto que também produz os registros de que o regulador precisa. Ela explica abertamente os tradeoffs: o híbrido custa mais no primeiro ano, mas reduz o ônus e o risco. Observa que os pesos refletem julgamentos das partes interessadas e mostra que a recomendação se mantém quando o peso das evidências regulatórias é dobrado: os totais passam a 3,74 para a opção orientada a reportes e 3,65 para a orientada ao projeto, ambas ainda bem acima da orientada a compliance, com 3,04, de modo que os dois componentes do híbrido continuam sendo os mais fortes. O conselho aprova o híbrido e pede uma avaliação após doze meses.

### Exemplo resolvido

Aiko compara programas orientados a compliance, a reportes e ao projeto com cinco critérios ponderados e recomenda um híbrido, com uma verificação de sensibilidade.

> **Caso sintético.** As pontuações e os pesos são sintéticos; Bada et al. (2019) é real.

### Erros e limites

Pontuações são julgamentos. Desenhos híbridos podem perder o foco se não forem bem geridos.

### Exercícios

- **EX076 — Fraqueza da opção de projeto.** Em que a opção orientada ao projeto pontua pior? *Rubrica:* 3 = evidências regulatórias;; 2 = evidências;; 1 = risco;; 0 = nenhuma.
- **EX077 — Totais ponderados.** Quais foram os totais ponderados no laboratório? *Rubrica:* 3 = compliance 2,75, reportes 3,85, projeto 3,90;; 2 = ordem;; 1 = nada;; 0 = nenhuma.
- **EX078 — Robustez do híbrido.** Como Aiko testou a recomendação do híbrido? *Rubrica:* 3 = dobrando o peso das evidências regulatórias;; 2 = sensibilidade;; 1 = nada;; 0 = nenhuma.

<a id="ch-27"></a>

## Capítulo 27 — Fatores humanos e política cibernética: projeto de controles

### Objetivos de aprendizagem

Você vai (1) desenhar controles que apoiem as pessoas em vez de testá-las; (2) aplicar nudges de forma ética; (3) desenhar procedimentos de verificação para pedidos de alto risco.

### 27.1 Controles de apoio

Aiko desenha controles que ajudam os funcionários a fazer a coisa certa. Pedidos de mudança de dados de pagamento disparam um bloqueio automático e um retorno de ligação feito por uma segunda pessoa, usando um número do cadastro do fornecedor, e não o do pedido. Sessões remotas de fornecedores exigem um número de chamado e aprovação no sistema de manutenção. E-mails externos com nomes iguais aos de funcionários exibem um aviso específico. Cada controle elimina a necessidade de um julgamento solitário sob pressão. Saltzer e Schroeder (1975) chamaram isso de aceitabilidade psicológica: controles fáceis de usar corretamente são usados corretamente.

### 27.2 Nudges éticos

Aiko considera os nudges, pequenas mudanças de projeto que tornam a escolha segura mais fácil ou mais visível. Exemplos incluem fazer do botão de reporte a ação mais destacada, definir padrões seguros para o compartilhamento de arquivos e exibir um lembrete curto quando alguém encaminha arquivos internos para fora. Ela estabelece limites éticos: os nudges devem ser transparentes, fáceis de contornar quando houver um bom motivo e nunca manipuladores. Um nudge que engane as pessoas prejudicaria a confiança e contradiria o respeito pelos funcionários do qual o programa depende.

### 27.3 Procedimentos de verificação

Para pedidos de alto risco, como mudanças nas configurações da estação de tratamento solicitadas por telefone, Aiko escreve um procedimento de verificação: registrar o pedido, desligar, retornar a ligação pelo número oficial, confirmar com um segundo engenheiro e registrar o resultado. O procedimento leva cerca de três minutos. Ela o testa com cinco engenheiros em uma dramatização, com um colega fazendo o papel de quem liga, e não em um exercício real de engano. Todos o completam corretamente após uma prática e sugerem um cartão plastificado junto ao telefone. O cartão lista os números oficiais e os passos em palavras simples.

### Exemplo resolvido

Aiko desenha controles para pagamentos, fornecedores e e-mails que eliminam julgamentos solitários, estabelece limites éticos para os nudges e testa um procedimento de retorno de ligação por dramatização.

> **Caso sintético.** Os controles e os testes são sintéticos; Saltzer e Schroeder (1975) é real.

### Erros e limites

Procedimentos de retorno de ligação falham se os cadastros de fornecedores estiverem errados. Os nudges perdem efeito com o tempo.

### Exercícios

- **EX079 — Origem do número de retorno.** De onde deve vir o número para o retorno de ligação? *Rubrica:* 3 = do cadastro do fornecedor, não do pedido;; 2 = fonte conhecida;; 1 = do pedido;; 0 = nenhuma.
- **EX080 — Limites dos nudges.** Que limites éticos se aplicam aos nudges? *Rubrica:* 3 = transparentes, fáceis de contornar e nunca manipuladores;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX081 — Dramatização, não engano.** Como o procedimento de verificação foi testado? *Rubrica:* 3 = dramatização com um colega fazendo o papel de quem liga;; 2 = dramatização;; 1 = engano real;; 0 = nenhuma.

<a id="ch-28"></a>

## Capítulo 28 — Fatores humanos e política cibernética: implementação I

### Objetivos de aprendizagem

Você vai (1) implementar o botão de reporte e o serviço de retorno; (2) gerir a mudança organizacional; (3) fazer o lançamento com apoio aos funcionários.

### 28.1 Implementação

Aiko se junta à equipe de TI da Greyford para implementar o serviço de reportes. Eles configuram o botão de reporte da plataforma de e-mail no computador e no celular, conectam-no à ferramenta de triagem, configuram os agradecimentos automáticos e criam modelos para as mensagens de veredito. Testam cada caminho com e-mails sintéticos antes do lançamento. Também configuram o dashboard agregado e removem a exportação individual, como planejado no capítulo 22. A implementação segue os requisitos do capítulo 21, que servem de checklist de aceitação. Cada resultado de teste é registrado com a data e o responsável, para que mudanças posteriores possam ser conferidas nos mesmos caminhos e nada seja presumido como ainda funcionando.

### 28.2 Gerir a mudança

Aiko sabe que novos processos fracassam quando as pessoas não entendem por que eles existem. Ela escreve uma explicação curta para os funcionários: por que reportar importa, o que acontece com os reportes e a promessa de que ninguém será culpado por clicar. Primeiro, orienta os líderes de equipe, para que possam responder às perguntas. Os representantes dos funcionários assinam o comunicado em conjunto. Ela evita mensagens baseadas no medo, que Bada, Sasse e Nurse (2019) identificaram como um motivo do fracasso das campanhas, e se concentra em como reportar protege os colegas e o público. Os líderes de equipe também recebem uma lista curta de perguntas prováveis, com sugestões de resposta.

### 28.3 Lançamento e apoio

O serviço é lançado numa terça-feira, evitando as segundas, quando o volume de e-mails é maior. Aiko mantém um canal de ajuda nas duas primeiras semanas e registra as perguntas. A maioria trata de reportar ou não newsletters e faturas de fornecedores. Ela atualiza a orientação para dizer que faturas inesperadas devem ser reportadas, enquanto newsletters conhecidas podem ser ignoradas. Os reportes na primeira semana triplicam em relação ao endereço de e-mail usado antes para reportar, e os agradecimentos funcionam no computador e no celular. O log do canal de ajuda se torna a primeira fonte da página de perguntas frequentes publicada um mês depois.

### Exemplo resolvido

Aiko implementa o reporte e o retorno, gere a mudança por meio dos líderes de equipe e de comunicados assinados em conjunto, e faz o lançamento com um canal de ajuda.

> **Caso sintético.** Os detalhes da implementação e os números são sintéticos; Bada et al. (2019) é real.

### Erros e limites

Picos de lançamento podem se dissipar. Canais de ajuda exigem tempo da equipe.

### Exercícios

- **EX082 — Checklist de aceitação.** O que serviu de checklist de aceitação? *Rubrica:* 3 = os requisitos do capítulo 21;; 2 = requisitos;; 1 = nada;; 0 = nenhuma.
- **EX083 — Mensagem evitada.** Que estilo de mensagem Aiko evitou? *Rubrica:* 3 = mensagens baseadas no medo;; 2 = medo;; 1 = nada;; 0 = nenhuma.
- **EX084 — Pergunta comum.** Do que tratava a maioria das primeiras perguntas? *Rubrica:* 3 = se newsletters e faturas de fornecedores deviam ser reportadas;; 2 = newsletters;; 1 = nada;; 0 = nenhuma.

<a id="ch-29"></a>

## Capítulo 29 — Fatores humanos e política cibernética: medição

### Objetivos de aprendizagem

Você vai (1) definir medidas de resultado para o programa; (2) calcular o tempo de exposição a partir dos dados de reportes; (3) evitar incentivos perversos nas métricas.

### 29.1 Medidas de resultado

Aiko define medidas para o programa da Greyford: a mediana do tempo entre a chegada de um e-mail malicioso e o primeiro reporte; a proporção de e-mails maliciosos reportados por pelo menos uma pessoa; a proporção de reportes que são ameaças reais; o ônus para os funcionários, medido por um questionário trimestral de duas perguntas; e, como medida secundária, a taxa de cliques em simulações com dificuldade fixa na Phish Scale. Cada medida tem uma definição, uma fonte de dados e um responsável. Ela põe em primeiro lugar o tempo até o reporte, porque ele se relaciona diretamente com o tempo em que os ataques permanecem ativos. Os responsáveis revisam suas medidas mensalmente com Aiko.

### 29.2 Calcular a exposição

O laboratório calcula, para um mês de e-mails maliciosos sintéticos, o tempo até o primeiro reporte e o número de caixas de entrada expostas até a remoção. A mediana do tempo até o primeiro reporte é de poucos minutos, mas dois e-mails nunca foram reportados e só foram removidos quando o fornecedor do filtro atualizou suas regras, horas depois. Esses dois respondem pela maior parte da exposição. Aiko recomenda investigar por que não foram reportados; os dois imitavam um lembrete interno de folha de ponto que os funcionários esperavam receber. Ela compartilha o achado também com o fornecedor do filtro.

### Laboratório — Tempo até o primeiro reporte e exposição das caixas de entrada

```python
# Time to first report and inbox-minutes of exposure for a month of malicious emails (synthetic).
emails = [("invoice lure", 40, 4, 30), ("mailbox full", 25, 6, 30), ("parcel", 60, 3, 25), ("ceo favour", 8, 11, 20),
          ("bank update", 35, 5, 30), ("timesheet reminder A", 120, None, 360), ("timesheet reminder B", 90, None, 300)]
# (name, recipients, minutes to first report or None, minutes to removal after report or after filter update)
total = 0; parts = []
for name, n, first, rem in emails:
    mins = (first + rem) if first is not None else rem
    exp = n * mins; total += exp; parts.append((name, first, exp))
firsts = sorted(f for _, f, _ in parts if f is not None)
print(f"median time to first report (reported emails): {firsts[len(firsts) // 2]} min; never reported: {sum(f is None for _, f, _ in parts)}")
unrep = sum(e for _, f, e in parts if f is None)
print(f"total inbox-minutes {total}; never-reported share {unrep / total:.0%}")
```

Execute com `python3 lab_exposure.py`. Saída verificada:

```text
median time to first report (reported emails): 5 min; never reported: 2
total inbox-minutes 75613; never-reported share 93%
```

### 29.3 Incentivos perversos

Aiko adverte contra metas que distorcem o comportamento. Uma meta de reduzir a taxa de cliques poderia ser cumprida enviando simulações mais fáceis e com menos frequência. Uma meta de número de reportes poderia ser cumprida incentivando os funcionários a reportar tudo, sobrecarregando a triagem. Ela propõe acompanhar as medidas em pares, como o número de reportes junto com a proporção de ameaças reais, e nunca vincular a elas remuneração ou punição individual. A medição deve ajudar o programa a aprender, e não criar jogos. Ela escreve essas regras no estatuto do programa, para que futuros gestores não possam introduzir discretamente metas individuais, e pede ao conselho que revise as medidas a cada ano para conferir se ainda servem ao aprendizado.

### Exemplo resolvido

Aiko define cinco medidas com responsáveis, calcula o tempo até o reporte e a exposição a partir de dados sintéticos e acompanha as medidas em pares para evitar incentivos perversos.

> **Caso sintético.** Os dados são sintéticos; a Phish Scale é real.

### Erros e limites

E-mails não reportados só são encontrados se forem detectados de outra forma. Medidas em pares ainda exigem julgamento.

### Exercícios

- **EX085 — Medida principal.** Por que pôr em primeiro lugar o tempo até o reporte? *Rubrica:* 3 = relaciona-se diretamente com o tempo em que os ataques ficam ativos;; 2 = exposição;; 1 = nada;; 0 = nenhuma.
- **EX086 — Exposição no laboratório.** Quanta exposição veio dos dois e-mails não reportados? *Rubrica:* 3 = os dois nunca reportados causaram 93% dos minutos-caixa de exposição;; 2 = a maior parte;; 1 = nada;; 0 = nenhuma.
- **EX087 — Medidas em pares.** Por que acompanhar as medidas em pares? *Rubrica:* 3 = para impedir que uma meta seja manipulada à custa de outra;; 2 = manipulação;; 1 = nada;; 0 = nenhuma.

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) verificar o serviço de reportes em relação aos requisitos; (2) conduzir uma verificação de usabilidade com participantes; (3) registrar as evidências da verificação.

### 30.1 Verificação de requisitos

No laboratório de verificação, Aiko confere cada requisito do capítulo 21. Envia e-mails de teste sintéticos e os reporta pelo computador e pelo celular, cronometrando os agradecimentos. Confere que o dashboard mostra apenas grupos de vinte pessoas ou mais e que não existe exportação individual. Confirma que os módulos de treinamento dos operadores levam menos de cinco minutos. Cada verificação produz um aprovado ou reprovado, com evidências como carimbos de tempo ou capturas de tela. A verificação transforma requisitos em prova, e não em suposição. Os testes são executados duas vezes, em dias diferentes, para descartar efeitos casuais de horário, e qualquer resultado próximo de um limite é repetido.

### 30.2 Verificação de usabilidade

Aiko recruta oito funcionários voluntários para executar tarefas: reportar um e-mail pelo celular, encontrar a mensagem de veredito e encontrar a orientação sobre o que reportar. Mede o sucesso e o tempo sem ajudar. Sete têm sucesso em todas as tarefas; um não consegue encontrar a orientação porque ela só está linkada na intranet. Ela acrescenta um link na mensagem de agradecimento. A verificação de usabilidade confere se os requisitos foram atendidos de um jeito que pessoas reais conseguem usar, algo que verificações técnicas sozinhas não podem confirmar. Ela também registra onde os voluntários hesitaram, mesmo quando tiveram sucesso.

### Laboratório — Resultados da verificação de requisitos

```python
# Requirement verification results, before and after fixing a notification setting (synthetic).
reqs = ["one-tap mobile report", "thank-you within 1 minute (desktop)", "thank-you within 1 minute (mobile)",
        "dashboard groups >= 20 only", "no individual export", "operator module <= 5 minutes"]
round1 = [True, True, False, True, True, True]
for r, ok in zip(reqs, round1): print(f"{'PASS' if ok else 'FAIL'} {r}")
print(f"round 1: {sum(round1)}/{len(reqs)}; round 2 after notification fix: {len(reqs)}/{len(reqs)}")
```

Execute com `python3 lab_verify.py`. Saída verificada:

```text
PASS one-tap mobile report
PASS thank-you within 1 minute (desktop)
FAIL thank-you within 1 minute (mobile)
PASS dashboard groups >= 20 only
PASS no individual export
PASS operator module <= 5 minutes
round 1: 5/6; round 2 after notification fix: 6/6
```

### 30.3 Registrar as evidências

Aiko registra os resultados em uma tabela de verificação que liga cada requisito a seu teste, data, resultado e evidência. Um requisito falha no início: no celular, os agradecimentos levam três minutos em um modelo de aparelho, por causa de uma configuração de notificação. A equipe de TI muda a configuração, e o novo teste passa. A tabela se torna evidência para o regulador e linha de base para a reverificação após mudanças futuras. A Profa. Kerr observa que registrar as falhas torna a verificação mais crível. A tabela é guardada com o documento de requisitos e posta sob controle de versão, para que cada versão futura seja verificada com os mesmos testes e qualquer mudança nos resultados possa ser rastreada.

### Exemplo resolvido

Aiko verifica os requisitos com testes cronometrados, verifica a usabilidade com oito voluntários, corrige um link de orientação e um atraso de notificação e registra as evidências.

> **Caso sintético.** Os testes e os resultados são sintéticos.

### Erros e limites

Voluntários podem ser mais confiantes do que os funcionários típicos. Os modelos de celular variam muito.

### Exercícios

- **EX088 — Verificação do dashboard.** O que Aiko verificou no dashboard? *Rubrica:* 3 = apenas grupos de vinte ou mais e nenhuma exportação individual;; 2 = agregação;; 1 = nada;; 0 = nenhuma.
- **EX089 — Correção de usabilidade.** Que problema de usabilidade um voluntário revelou? *Rubrica:* 3 = orientação linkada apenas na intranet;; 2 = link;; 1 = nada;; 0 = nenhuma.
- **EX090 — Verificação no laboratório.** Quantos requisitos passaram em cada rodada de verificação? *Rubrica:* 3 = 5 de 6 passaram, depois 6 de 6 após a correção da notificação;; 2 = 5 e depois 6;; 1 = nada;; 0 = nenhuma.

<a id="ch-31"></a>

## Capítulo 31 — Fatores humanos e política cibernética: implementação II

### Objetivos de aprendizagem

Você vai (1) implementar os controles de verificação de pagamentos e de fornecedores; (2) integrar os controles aos fluxos de trabalho existentes; (3) treinar os funcionários nos novos procedimentos.

### 31.1 Controles de pagamento

Aiko trabalha com a equipe financeira para implementar o controle de verificação de pagamentos. O sistema financeiro passa a aplicar um bloqueio automático a qualquer mudança nos dados bancários de fornecedores e cria uma tarefa para um segundo analista, que precisa ligar para o fornecedor usando o número que consta do cadastro. O bloqueio não pode ser liberado pela pessoa que recebeu o pedido. A equipe financeira testa o fluxo com dez pedidos de mudança sintéticos, incluindo dois com redação urgente, e todos os pedidos são bloqueados e verificados antes da liberação.

### 31.2 Controles de sessões de fornecedores

Para as sessões remotas de fornecedores em tecnologia operacional, a equipe de TI configura o gateway de acesso remoto de modo que uma sessão só possa começar quando for informado um número de chamado válido do sistema de manutenção e um engenheiro tiver aprovado o chamado. Isso elimina a oportunidade de alguém convencer um operador por telefone a abrir uma sessão. Os fornecedores são informados por escrito um mês antes da mudança, e dois deles pedem uma sessão de teste, que a equipe organiza para que a manutenção real não seja interrompida no dia da mudança.

### 31.3 Treinamento nos procedimentos

Aiko escreve guias curtos de procedimento e conduz sessões de quinze minutos para analistas financeiros e operadores da sala de controle. As sessões usam exemplos resolvidos e dramatizações em vez de provas, e os participantes praticam as etapas do retorno de ligação e do chamado. Ela registra as perguntas e revisa os guias duas vezes. Seguindo a orientação da NIST SP 800-50r1 (Hansche et al., 2024), trata o treinamento por função para funcionários com deveres específicos como distinto da conscientização geral, de modo que essas sessões se concentram apenas nas etapas que essas funções precisam executar. A presença é registrada para o regulador.

### Exemplo resolvido

Aiko implementa um bloqueio de pagamento com retorno de ligação por um segundo analista, sessões de fornecedores condicionadas a chamados e um treinamento curto por função.

> **Caso sintético.** Os procedimentos são sintéticos; a NIST SP 800-50r1 é real.

### Erros e limites

Segundos analistas podem aprovar sem ligar quando estão ocupados. Fornecedores podem resistir à exigência de chamados.

### Exercícios

- **EX091 — Liberação do bloqueio.** Quem não pode liberar o bloqueio de pagamento? *Rubrica:* 3 = a pessoa que recebeu o pedido;; 2 = solicitante;; 1 = segundo analista;; 0 = nenhuma.
- **EX092 — Condição para o fornecedor.** O que precisa existir antes de uma sessão de fornecedor começar? *Rubrica:* 3 = um chamado de manutenção válido e aprovado;; 2 = chamado;; 1 = uma ligação;; 0 = nenhuma.
- **EX093 — Treinamento por função.** Em que o treinamento por função difere da conscientização geral? *Rubrica:* 3 = concentra-se nas etapas que funções específicas precisam executar;; 2 = etapas da função;; 1 = nada;; 0 = nenhuma.

<a id="ch-32"></a>

## Capítulo 32 — Fatores humanos e política cibernética: confiabilidade

### Objetivos de aprendizagem

Você vai (1) analisar a confiabilidade de controles que dependem de pessoas; (2) calcular o efeito de verificações independentes; (3) reconhecer falhas de causa comum.

### 32.1 Confiabilidade humana

Todo controle que depende de uma pessoa pode falhar quando ela está cansada, apressada ou distraída. Aiko trata o controle de retorno de ligação como um sistema com uma probabilidade de falha. Se um analista pula o retorno em cinco por cento dos casos sob pressão, um controle com um único analista falha cerca de uma vez em vinte. Uma segunda verificação independente reduz isso, mas só se as verificações forem de fato independentes. A análise de confiabilidade ajuda a Greyford a ver onde acrescentar verificações e onde um controle técnico seria mais confiável do que qualquer procedimento.

### 32.2 Verificações independentes

O laboratório calcula a probabilidade de uma mudança fraudulenta de pagamento passar quando cada uma de uma, duas ou três verificações independentes falha com determinada probabilidade. Com uma taxa de falha de 5%, duas verificações independentes falham juntas em 0,25% dos casos. Em seguida, o laboratório acrescenta uma causa comum, como a pressão de fim de mês afetando os dois analistas ao mesmo tempo, e mostra que a falha conjunta sobe bruscamente. Isso mostra por que a Greyford escala outra equipe para as segundas verificações no fim do mês e não confia apenas na aritmética da independência.

### Laboratório — Falha independente e de causa comum das verificações

```python
# Probability a fraudulent payment change passes all checks (synthetic rates).
p = 0.05
for k in (1, 2, 3): print(f"{k} independent check(s): {p ** k:.4%}")
# Common cause: on 10% of days (month-end), each check fails with 0.35 and failures are shared.
q, pc = 0.10, 0.35
both = (1 - q) * p * p + q * pc * pc
print(f"2 checks with month-end common cause: {both:.2%}")
```

Execute com `python3 lab_reliability.py`. Saída verificada:

```text
1 independent check(s): 5.0000%
2 independent check(s): 0.2500%
3 independent check(s): 0.0125%
2 checks with month-end common cause: 1.45%
```

### 32.3 Falhas de causa comum

Causas comuns incluem pressão compartilhada, informação enganosa compartilhada e confiança compartilhada em um nome conhecido. Se o e-mail fraudulento convence o primeiro analista, o segundo pode ver o mesmo e-mail e ser convencido também. Por isso, Aiko desenha a segunda verificação para usar informação diferente, o número do cadastro do fornecedor em vez do e-mail, e uma equipe diferente. Ela observa que a independência é uma propriedade de projeto que precisa ser construída, e não presumida, e a escreve na descrição do controle para que ela sobreviva às trocas de pessoal.

### Exemplo resolvido

Aiko modela a confiabilidade do retorno de ligação, mostra que verificações independentes reduzem a falha e desenha o controle contra causas comuns.

> **Caso sintético.** As probabilidades são sintéticas.

### Erros e limites

Taxas reais de falha são difíceis de medir. A independência pode se desgastar com o tempo.

### Exercícios

- **EX094 — Duas verificações.** Qual é a taxa de falha conjunta de duas verificações independentes de 5%? *Rubrica:* 3 = 0,25%;; 2 = 0,0025;; 1 = 10%;; 0 = nenhuma.
- **EX095 — Causa comum no laboratório.** Como uma causa comum alterou a falha conjunta? *Rubrica:* 3 = a falha conjunta subiu de 0,25% para 1,45%;; 2 = aumento;; 1 = nada;; 0 = nenhuma.
- **EX096 — Construir a independência.** Como Aiko construiu a independência na segunda verificação? *Rubrica:* 3 = informação diferente e equipe diferente;; 2 = diferente;; 1 = mesmo e-mail;; 0 = nenhuma.

<a id="ch-33"></a>

## Capítulo 33 — Fatores humanos e política cibernética: segurança e resiliência

### Objetivos de aprendizagem

Você vai (1) ligar o comportamento de segurança à segurança operacional em uma companhia de saneamento; (2) desenhar resiliência para quando as pessoas forem enganadas; (3) ensaiar a recuperação sem engano.

### 33.1 Ligações com a segurança operacional

Em uma companhia de saneamento, um operador enganado poderia permitir mudanças nas configurações de tratamento que afetassem a saúde pública. Aiko trabalha com o gerente de segurança operacional para ligar os procedimentos de segurança da informação e de segurança operacional. Qualquer mudança nas configurações de dosagem já exige, por razões de segurança operacional, um segundo engenheiro; ela estende essa regra aos pedidos remotos, de modo que um operador enganado, sozinho, não consiga mudar uma configuração. O caso de segurança passa a listar a engenharia social como possível evento iniciador, com controles e ações de resposta, para que as duas equipes compartilhem uma única visão do perigo.

### 33.2 Projetar para o engano

Aiko parte do princípio de que alguém acabará sendo enganado, porque nenhum programa consegue impedir todo engano. Ela projeta a resiliência: alertas automáticos sobre mudanças incomuns de configuração, uma forma clara de manifestar uma preocupação depois do fato sem culpa e uma via rápida para reverter mudanças. Os funcionários são informados de que reportar rapidamente um erro é a coisa mais valiosa que podem fazer. Isso desloca a pergunta de se as pessoas podem ser enganadas para quão rápido a organização se recupera quando elas são, um objetivo mais alcançável.

### 33.3 Ensaiar a recuperação

A Greyford ensaia a recuperação com exercícios de mesa, nos quais os funcionários discutem um cenário como o de uma falsificação de fornecedor que levou à abertura de uma sessão. Os exercícios são anunciados, conduzidos com participantes voluntários e focados na resposta, e não em flagrar alguém. O primeiro exercício revela que a sala de controle não sabe para quem ligar na equipe de segurança fora do horário de expediente. Uma escala de plantão é publicada na semana seguinte. Ensaiar a recuperação abertamente constrói confiança, e não medo, em coerência com a abordagem ética do programa.

### Exemplo resolvido

Aiko liga a segurança da informação às regras de segurança operacional da dosagem, projeta a recuperação após um engano e conduz exercícios de mesa anunciados.

> **Caso sintético.** Os cenários são sintéticos.

### Erros e limites

Exercícios de mesa podem não revelar problemas práticos. Alertas podem ser ignorados.

### Exercícios

- **EX097 — Extensão da regra de segurança.** Que regra de segurança operacional foi estendida aos pedidos remotos? *Rubrica:* 3 = segundo engenheiro para mudanças de dosagem;; 2 = duas pessoas;; 1 = nada;; 0 = nenhuma.
- **EX098 — Objetivo da resiliência.** Para que pergunta o projeto para o engano desloca o foco? *Rubrica:* 3 = quão rápido a organização se recupera;; 2 = recuperação;; 1 = se as pessoas são enganadas;; 0 = nenhuma.
- **EX099 — Achado do exercício de mesa.** Que lacuna o primeiro exercício de mesa revelou? *Rubrica:* 3 = nenhum contato de segurança conhecido fora do expediente;; 2 = escala;; 1 = nada;; 0 = nenhuma.

<a id="ch-34"></a>

## Capítulo 34 — Fatores humanos e política cibernética: integração

### Objetivos de aprendizagem

Você vai (1) integrar o programa à resposta a incidentes; (2) alinhá-lo à governança e à gestão de riscos; (3) ligar as métricas ao registro de riscos.

### 34.1 Resposta a incidentes

Aiko integra os reportes à resposta a incidentes. Quando a triagem confirma um e-mail malicioso que chegou a muitas caixas de entrada, a ferramenta de triagem abre automaticamente um chamado de incidente, notifica o líder de resposta e remove o e-mail de todas as caixas. Os responsáveis pela resposta podem ver quem reportou primeiro e agradecer. Depois dos incidentes, os líderes de resposta acrescentam uma nota curta sobre fatores humanos, como se um controle ajudou ou atrapalhou. Essa ligação faz com que os reportes tenham um efeito visível na resposta e que as lições voltem para o projeto.

### 34.2 Alinhamento com a governança

Aiko mapeia o programa na governança da Greyford. A função Govern do NIST CSF 2.0 espera papéis, políticas e supervisão para a cibersegurança, e o programa agora tem um responsável nomeado, um estatuto, relatórios trimestrais ao comitê de riscos e uma revisão anual. A ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) exige conscientização e competência das pessoas cujo trabalho afeta a segurança, e o programa fornece registros de ambas. Ela evita tratar esses frameworks como o objetivo; eles dão estrutura, enquanto o objetivo continua sendo menos resultados danosos. O estatuto é revisado pelo comitê de riscos a cada ano.

### 34.3 Ligações com o registro de riscos

Aiko liga as medidas do programa a entradas do registro de riscos, seguindo a abordagem da NIST SP 800-30r1, segundo a qual as estimativas de probabilidade e impacto devem ser atualizadas com evidências. O risco de fraude de pagamento passa a ser informado pelo número de pedidos de mudança bloqueados e de falsificações verificadas; o risco de abuso de acesso à TO, pelas tentativas de sessões sem chamado. Quando as medidas mudam, os responsáveis pelos riscos revisam a entrada. Isso transforma o programa, de atividade separada, em fonte de evidências para as decisões de risco em toda a organização.

### Exemplo resolvido

Aiko liga os reportes a chamados de incidente automáticos, mapeia o programa no CSF 2.0 e na ISO/IEC 27001 e alimenta o registro de riscos com as medidas.

> **Caso sintético.** A integração é sintética; o NIST CSF 2.0, a ISO/IEC 27001:2022 e a SP 800-30r1 são reais.

### Erros e limites

A criação automática de incidentes pode gerar ruído. O mapeamento em frameworks pode virar mero preenchimento de checklist.

### Exercícios

- **EX100 — Ação automática.** O que acontece quando a triagem confirma um e-mail malicioso recebido por muitos? *Rubrica:* 3 = abre-se um chamado de incidente e o e-mail é removido;; 2 = chamado;; 1 = nada;; 0 = nenhuma.
- **EX101 — Função do CSF.** Que função do CSF 2.0 cobre papéis, políticas e supervisão? *Rubrica:* 3 = Govern;; 2 = govern;; 1 = Protect;; 0 = nenhuma.
- **EX102 — Evidência de risco.** Que medida informa o risco de fraude de pagamento? *Rubrica:* 3 = pedidos de mudança bloqueados e falsificações verificadas;; 2 = pedidos bloqueados;; 1 = nada;; 0 = nenhuma.

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) redesenhar um componente a partir de evidências de avaliação; (2) apresentar a justificativa de projeto a um público misto; (3) responder a questionamentos de forma construtiva.

### 35.1 O briefing do ateliê

O segundo ateliê pede às equipes que redesenhem um componente do programa da Greyford usando as evidências de avaliação reunidas até agora. A equipe de Aiko escolhe a orientação sobre o que reportar, porque o log do canal de ajuda e os testes de usabilidade mostraram confusão sobre faturas e newsletters. O briefing exige um guia redesenhado, um teste com pelo menos seis funcionários e uma apresentação a uma banca que inclui um analista financeiro, um operador e um gerente de segurança. As equipes têm três semanas e precisam documentar cada mudança e seu motivo.

### 35.2 Redesenho guiado por evidências

A equipe reescreve a orientação como três perguntas: você esperava esta mensagem, ela pede que você aja depressa, e ela pede dinheiro, credenciais ou acesso? Se alguma resposta for preocupante, reporte. Eles testam o novo guia com oito funcionários usando doze e-mails sintéticos. As decisões de reporte corretas sobem, em média, de nove para onze em doze. Um participante observa que os e-mails de sistemas internos continuam difíceis de julgar, então a equipe acrescenta uma lista curta dos remetentes de sistema legítimos, atualizada mensalmente.

### 35.3 Apresentação e questionamento

A equipe apresenta o redesenho em dez minutos, começando pelas evidências de confusão. O analista financeiro questiona se as três perguntas pegariam uma fraude de pagamento vinda da conta comprometida de um fornecedor conhecido. A equipe reconhece que o guia, sozinho, não pegaria, e aponta o controle de bloqueio de pagamento como a defesa para esse caso. A banca valoriza a resposta honesta. Aiko aprende que uma justificativa de projeto é mais forte quando mostra como as partes do sistema cobrem as fraquezas umas das outras.

### Exemplo resolvido

A equipe de Aiko redesenha a orientação de reporte como três perguntas, eleva as decisões corretas de nove para onze em doze e responde ao questionamento apontando os controles em camadas.

> **Caso sintético.** O ateliê é sintético.

### Erros e limites

Testes pequenos podem não se generalizar. Listas de remetentes legítimos exigem manutenção.

### Exercícios

- **EX103 — Três perguntas.** Quais são as três perguntas do novo guia? *Rubrica:* 3 = esperada, urgente, pede dinheiro, credenciais ou acesso;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX104 — Resultado do teste.** Como mudaram as decisões corretas? *Rubrica:* 3 = de nove para onze em doze;; 2 = aumento;; 1 = nada;; 0 = nenhuma.
- **EX105 — Fornecedor comprometido.** O que respondeu ao questionamento sobre o fornecedor comprometido? *Rubrica:* 3 = o controle de bloqueio de pagamento;; 2 = controle em camadas;; 1 = o guia;; 0 = nenhuma.

<a id="ch-36"></a>

## Capítulo 36 — Fatores humanos e política cibernética: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) estimar a capacidade de triagem à medida que os reportes crescem; (2) modelar os tempos de espera em fila; (3) planejar pessoal e automação para manter o retorno rápido.

### 36.1 Crescimento dos reportes

À medida que o serviço de reportes dá certo, o volume de reportes cresce. A Greyford recebe cerca de quarenta reportes por dia após o lançamento e espera mais à medida que a confiança dos funcionários aumenta e o programa se estende aos terceirizados. Cada reporte precisa de triagem, e a promessa de retorno rápido depende de a triagem acompanhar o ritmo. Aiko estima que um analista de triagem consegue tratar cerca de doze reportes por hora depois do agrupamento. Ela pergunta o que acontece com os tempos de espera quando o volume diário sobe, porque um retorno lento minaria o efeito mostrado no capítulo 17.

### 36.2 Modelagem de filas

O laboratório simula um dia de reportes chegando ao acaso durante o expediente e atendidos por um analista a uma taxa fixa, e registra a espera média até o veredito. Com quarenta reportes por dia, a espera média é de cerca de sete minutos. Com oitenta, dobra para catorze, e com noventa e cinco, quando o analista fica ocupado quase o tempo todo, chega a vinte e cinco minutos, subindo cada vez mais depressa a cada reporte extra, como prevê a teoria das filas quando a utilização se aproxima de um. Aiko usa o resultado para mostrar aos gestores que a capacidade precisa crescer antes que o volume chegue à parte íngreme da curva, e não depois que as reclamações começarem.

### Laboratório — Tempo de espera pelos vereditos à medida que o volume de reportes cresce

```python
# Single analyst triage queue over an 8-hour day (synthetic, seed fixed).
import random
def day(n, rate=12, seed=1):
    r = random.Random(seed); arr = sorted(r.uniform(0, 480) for _ in range(n))
    free = 0.0; waits = []
    for a in arr:
        start = max(a, free); free = start + 60 / rate; waits.append(free - a)
    return sum(waits) / n
for n in (40, 80, 95):
    print(f"{n} reports/day: mean wait to verdict {sum(day(n, seed=s) for s in range(200)) / 200:.0f} min")
```

Execute com `python3 lab_queue.py`. Saída verificada:

```text
40 reports/day: mean wait to verdict 7 min
80 reports/day: mean wait to verdict 14 min
95 reports/day: mean wait to verdict 25 min
```

### 36.3 Pessoal e automação

Aiko propõe três medidas: agrupamento automático, para que reportes idênticos contem como um único item; vereditos automáticos para mensagens já confirmadas como maliciosas; e um segundo analista nos horários de pico. A automação cuida do trabalho repetitivo, enquanto as pessoas tratam os casos novos ou incertos. Ela define um nível de serviço de veredito em até uma hora útil para noventa por cento dos reportes e uma verificação mensal da medida. Se o nível de serviço escorregar por dois meses, o quadro de pessoal é revisto. Isso mantém rápida a malha de retorno à medida que o programa cresce.

### Exemplo resolvido

Aiko modela os tempos de espera pelos vereditos à medida que os reportes crescem e planeja agrupamento, vereditos automáticos e pessoal nos picos para manter o retorno em até uma hora.

> **Caso sintético.** Os volumes e as taxas são sintéticos.

### Erros e limites

Chegadas reais se concentram em torno das campanhas. Vereditos automáticos podem estar errados.

### Exercícios

- **EX106 — Taxa do analista.** Que taxa de triagem Aiko supôs por analista? *Rubrica:* 3 = cerca de doze reportes por hora;; 2 = doze;; 1 = quarenta;; 0 = nenhuma.
- **EX107 — Fila no laboratório.** Quanto duraram as esperas médias com 40, 80 e 95 reportes por dia? *Rubrica:* 3 = 7, 14 e 25 minutos;; 2 = aumento;; 1 = nada;; 0 = nenhuma.
- **EX108 — Nível de serviço.** Que nível de serviço Aiko definiu? *Rubrica:* 3 = veredito em até uma hora útil para 90%;; 2 = uma hora;; 1 = nada;; 0 = nenhuma.

<a id="ch-37"></a>

## Capítulo 37 — Fatores humanos e política cibernética: operações

### Objetivos de aprendizagem

Você vai (1) definir as operações de rotina do programa; (2) conduzir simulações éticas na operação; (3) tratar reclamações e exceções.

### 37.1 Operações de rotina

Aiko escreve um calendário de operações. Toda semana, a equipe de triagem revisa os agrupamentos e envia os retornos. Todo mês, sai uma reciclagem curta e é feita uma simulação com dificuldade planejada. Todo trimestre, o questionário de ônus é enviado e as medidas são relatadas ao comitê de riscos. Todo ano, o programa é revisado em relação ao seu estatuto. Cada tarefa tem um responsável e um substituto. As operações de rotina importam porque o trabalho de conscientização se desgasta sem atenção constante, como mostrou a análise de decaimento do capítulo 6. Os substitutos cobrem férias e licenças.

### 37.2 Simulações éticas na operação

As simulações seguem regras acordadas com os representantes dos funcionários: programa anunciado, nenhuma isca que explore sofrimento pessoal, como cortes salariais, bônus ou sustos de saúde, nenhum uso de resultados individuais para punição, retorno imediato e acolhedor e relatórios apenas agregados. Cada modelo é classificado pela NIST Phish Scale (Dawkins e Jacobs, 2023) e aprovado por uma pequena banca que inclui um representante dos funcionários. Lain, Kostiainen e Čapkun (2022) constataram que as páginas de treinamento exibidas depois do clique não ajudavam, por isso o retorno é curto e gentil, e não uma aula.

### 37.3 Reclamações e exceções

Alguns funcionários reclamam que as simulações dão a sensação de terem sido enganados. Aiko responde pessoalmente a cada reclamação, explica as regras e registra o tema. Quando várias reclamações citam um modelo que imitava uma mensagem do RH sobre férias, a banca o retira, reconhecendo que chegava perto demais de assuntos pessoais. Exceções são permitidas para funcionários em licença médica ou sob estresse, que podem se excluir temporariamente por meio do gestor, sem dar motivos. Tratar bem as reclamações preserva a confiança da qual os reportes dependem. Os temas são relatados trimestralmente.

### Exemplo resolvido

Aiko define um calendário de operações semanal a anual, conduz simulações sob regras éticas acordadas e retira um modelo após reclamações.

> **Caso sintético.** As operações são sintéticas; Dawkins e Jacobs (2023) e Lain et al. (2022) são reais.

### Erros e limites

As exclusões reduzem a cobertura. As bancas podem aprovar iscas limítrofes.

### Exercícios

- **EX109 — Iscas proibidas.** Que iscas são proibidas? *Rubrica:* 3 = as que exploram sofrimento pessoal, como salário ou saúde;; 2 = sofrimento;; 1 = nada;; 0 = nenhuma.
- **EX110 — Treinamento embutido.** Por que o retorno após o clique é curto e gentil? *Rubrica:* 3 = Lain et al. constataram que páginas de treinamento embutidas não ajudavam;; 2 = pesquisa;; 1 = nada;; 0 = nenhuma.
- **EX111 — Modelo retirado.** Por que um modelo foi retirado? *Rubrica:* 3 = imitava uma mensagem do RH sobre férias, perto demais de assuntos pessoais;; 2 = RH;; 1 = nada;; 0 = nenhuma.

<a id="ch-38"></a>

## Capítulo 38 — Fatores humanos e política cibernética: validação

### Objetivos de aprendizagem

Você vai (1) distinguir validação de verificação; (2) validar o programa em relação à sua finalidade; (3) usar evidências mistas para julgar o sucesso.

### 38.1 Validação versus verificação

A verificação pergunta se o sistema foi construído conforme especificado; a validação pergunta se ele cumpre sua finalidade. O serviço de reportes da Greyford passou na verificação do capítulo 30, mas Aiko agora precisa perguntar se ele de fato reduz os danos causados pelo engano. Um serviço pode atender a todos os requisitos e ainda falhar em sua finalidade se, por exemplo, os funcionários reportarem apenas e-mails inofensivos enquanto os ataques passam sem reporte. Por isso, a validação olha para os resultados na operação real, e não em condições de teste, e precisa de evidências coletadas ao longo de meses, e não de dias. As duas são necessárias, nessa ordem.

### 38.2 Validar os resultados

Depois de nove meses, Aiko compara os resultados com o ano anterior ao lançamento. O laboratório calcula a mudança na mediana do tempo até o primeiro reporte e na proporção de e-mails maliciosos reportados. A proporção reportada sobe e a mediana do tempo cai. Ela também confere as tentativas de fraude de pagamento: três falsas mudanças de dados bancários foram barradas pelo controle de bloqueio, contra uma perda no ano anterior. Ela observa que a comparação antes e depois não pode descartar mudanças nos ataques, por isso apresenta os achados como compatíveis com o sucesso, e não como prova dele.

### Laboratório — Resultados de reportes antes e depois

```python
# Before and after reporting outcomes for malicious emails (synthetic).
before = {"reported": 41, "total": 100, "times": [12, 20, 25, 30, 38, 45, 60, 75, 90]}
after = {"reported": 78, "total": 100, "times": [3, 4, 6, 8, 9, 11, 14, 18, 25]}
for name, d in (("before", before), ("after", after)):
    t = sorted(d["times"]); print(f"{name}: reported share {d['reported'] / d['total']:.0%}, median first report {t[len(t) // 2]} min")
```

Execute com `python3 lab_validate.py`. Saída verificada:

```text
before: reported share 41%, median first report 38 min
after: reported share 78%, median first report 9 min
```

### 38.3 Evidências mistas

Aiko acrescenta evidências qualitativas: entrevistas com dez funcionários, o questionário de ônus e o log de reclamações. Os funcionários descrevem o botão de reporte como fácil e o retorno como tranquilizador, embora alguns ainda não gostem das simulações. As pontuações de ônus melhoram ligeiramente. Juntas, as evidências sustentam a continuidade do programa com ajustes. Ela segue a orientação de Beautement, Sasse e Wonham (2008) de observar os efeitos sobre o orçamento de compliance e descobre que o bloqueio de pagamento acrescenta trabalho no fim do mês, o que leva a uma revisão do quadro de pessoal do setor financeiro nesse período. As anotações das entrevistas são anonimizadas antes da análise.

### Exemplo resolvido

Aiko valida o programa com resultados antes e depois, tentativas de fraude barradas e entrevistas, tratando os resultados como compatíveis com o sucesso, e não como prova.

> **Caso sintético.** Os resultados são sintéticos; Beautement et al. (2008) é real.

### Erros e limites

Desenhos antes e depois são fracos. Os padrões de ataque mudam de um ano para outro.

### Exercícios

- **EX112 — Definição.** O que a validação pergunta? *Rubrica:* 3 = se o sistema cumpre sua finalidade;; 2 = finalidade;; 1 = se foi construído conforme especificado;; 0 = nenhuma.
- **EX113 — Resultados no laboratório.** O que o laboratório mostrou para a mediana do tempo de reporte e a proporção reportada? *Rubrica:* 3 = de 38 para 9 minutos; de 41% para 78%;; 2 = melhora;; 1 = nada;; 0 = nenhuma.
- **EX114 — Ônus no fim do mês.** Que efeito sobre o orçamento de compliance Aiko encontrou? *Rubrica:* 3 = o bloqueio de pagamento acrescenta trabalho no fim do mês;; 2 = financeiro;; 1 = nada;; 0 = nenhuma.

<a id="ch-39"></a>

## Capítulo 39 — Fatores humanos e política cibernética: manutenibilidade

### Objetivos de aprendizagem

Você vai (1) desenhar o programa para ser mantido ao longo de anos; (2) gerir o ciclo de vida de conteúdos e modelos; (3) planejar a passagem de bastão e a documentação.

### 39.1 Projeto duradouro

Programas muitas vezes declinam quando seu fundador sai. Aiko desenha o programa da Greyford para ser manutenível: procedimentos documentados, um estatuto com responsáveis, uma biblioteca de conteúdos com datas de revisão e medidas produzidas automaticamente pela ferramenta de triagem. Ela evita software sob medida quando existe um recurso de produto com suporte, porque ferramentas sob medida exigem especialistas para mantê-las. Também reserva no orçamento um tempo fixo da equipe a cada ano para revisão e atualização, de modo que a manutenção não dependa de um tempo livre que talvez nunca apareça em uma companhia de saneamento movimentada.

### 39.2 Ciclo de vida dos conteúdos

Cada guia, reciclagem e modelo de simulação tem um responsável, uma data de criação e uma data de revisão. Conteúdos com mais de um ano são revisados em relação aos relatórios de ataques atuais, como o Verizon DBIR mais recente, e aos e-mails reportados na própria Greyford. Os modelos são aposentados quando deixam de refletir iscas reais ou quando as reclamações mostram que causam dano. O laboratório conta os itens com revisão prevista em cada trimestre, para que o trabalho possa ser planejado. Uma biblioteca pequena e atual é melhor do que uma grande, cheia de exemplos desatualizados.

### Laboratório — Itens de conteúdo com revisão prevista por trimestre

```python
# Content items due for review by quarter (synthetic library of 40 items).
due = {"Q1": 9, "Q2": 11, "Q3": 14, "Q4": 6}
for q, n in due.items(): print(f"{q}: {n} items")
print("busiest:", max(due, key=due.get), "total:", sum(due.values()))
```

Execute com `python3 lab_lifecycle.py`. Saída verificada:

```text
Q1: 9 items
Q2: 11 items
Q3: 14 items
Q4: 6 items
busiest: Q3 total: 40
```

### 39.3 Passagem de bastão

Aiko escreve um pacote de passagem de bastão: o estatuto, o calendário de operações, a tabela de requisitos e verificação, as medidas com suas definições e as regras éticas das simulações. Um substituto acompanha cada tarefa por um ciclo antes de assumi-la. Ela grava vídeos curtos explicando o raciocínio por trás das decisões principais, porque os documentos costumam registrar o que foi feito, mas não por quê. A Profa. Kerr observa que são os motivos que permitem aos sucessores adaptar o projeto com sabedoria, em vez de congelá-lo ou abandoná-lo. O pacote é revisado anualmente.

### Exemplo resolvido

Aiko projeta para a manutenção com responsáveis e datas de revisão, planeja a revisão de conteúdos por trimestre e escreve um pacote de passagem de bastão com os motivos das decisões.

> **Caso sintético.** Os dados de conteúdo são sintéticos; o Verizon DBIR é real.

### Erros e limites

Datas de revisão muitas vezes são perdidas. Pacotes de passagem de bastão ficam desatualizados.

### Exercícios

- **EX115 — Software sob medida.** Por que evitar software sob medida? *Rubrica:* 3 = exige especialistas para mantê-lo;; 2 = manutenção;; 1 = nada;; 0 = nenhuma.
- **EX116 — Carga de revisão no laboratório.** Que trimestre teve mais conteúdos com revisão prevista? *Rubrica:* 3 = o 3º trimestre, com 14 itens;; 2 = 3º trimestre;; 1 = nada;; 0 = nenhuma.
- **EX117 — Registrar os motivos.** Por que registrar os motivos das decisões? *Rubrica:* 3 = para que os sucessores possam adaptar com sabedoria;; 2 = adaptar;; 1 = nada;; 0 = nenhuma.

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem

Você vai (1) reverificar após mudanças; (2) verificar os controles sob carga realista; (3) relatar os resultados da verificação com seus limites.

### 40.1 Verificação de regressão

Depois de um ano de mudanças, incluindo a nova orientação, os vereditos automáticos e a exigência de chamados para fornecedores, Aiko executa de novo a tabela de verificação do capítulo 30 e acrescenta testes para os novos requisitos. A verificação de regressão confere se as mudanças não quebraram algo que funcionava antes. Aparece uma regressão: o recurso de veredito automático envia o retorno sem o link para a orientação acrescentado depois do teste de usabilidade. A equipe de TI restaura o link e o novo teste passa. Sem a tabela, a regressão poderia ter passado despercebida por meses, enquanto os funcionários perdiam uma orientação útil.

### 40.2 Verificação sob carga

Aiko verifica o serviço de triagem sob carga realista, reproduzindo um dia de campanha sintético com trezentos reportes em duas horas. Ela mede o tempo entre o reporte e o veredito com o agrupamento e os vereditos automáticos ativados. O laboratório resume o resultado: a maioria dos reportes recebe veredito em minutos, porque eles se agrupam em poucos e-mails distintos, mas um punhado de reportes únicos espera mais tempo por um analista. O nível de serviço de uma hora para noventa por cento é atendido, e o reporte mais lento espera menos de duas horas.

### Laboratório — Tempos de veredito durante um dia de campanha sintético

```python
# Verdict times for a synthetic campaign day: 300 reports in 2 hours.
import random
r = random.Random(7)
times = []
for i in range(300):
    if i < 270: times.append(r.uniform(1, 12))      # clustered, automatic verdicts
    elif i < 273: times.append(r.uniform(61, 104))  # unique reports waiting for analyst
    else: times.append(r.uniform(15, 58))           # unique reports handled within the hour
times[-1] = 104.0
within = sum(t <= 60 for t in times) / len(times)
print(f"within 60 min: {within:.0%}; slowest {max(times):.0f} min")
```

Execute com `python3 lab_load.py`. Saída verificada:

```text
within 60 min: 99%; slowest 104 min
```

### 40.3 Relatar os limites

Aiko relata os resultados com seus limites. A reprodução usou reportes sintéticos e não pôde incluir a confusão de uma campanha real, como funcionários ligando para o service desk. Os testes de carga foram executados fora do expediente, por isso não competiram com outros sistemas. Ela recomenda uma verificação ao vivo durante a próxima campanha real. O relatório de verificação declara com clareza o que foi testado, o que não foi e o que continua incerto, o que permite ao comitê de riscos julgar quanta confiança depositar no serviço.

### Exemplo resolvido

Aiko executa de novo a verificação e encontra uma regressão de link ausente, testa a triagem sob carga com uma campanha sintética e relata os limites abertamente.

> **Caso sintético.** Os testes são sintéticos.

### Erros e limites

Reproduções sintéticas não capturam a confusão real. Verificações ao vivo são mais difíceis de controlar.

### Exercícios

- **EX118 — Regressão encontrada.** Que regressão foi encontrada? *Rubrica:* 3 = os vereditos automáticos estavam sem o link de orientação;; 2 = link ausente;; 1 = nada;; 0 = nenhuma.
- **EX119 — Carga no laboratório.** Quão rápidos foram os vereditos durante a reprodução da campanha? *Rubrica:* 3 = 99% em até uma hora; o mais lento em 104 minutos;; 2 = atendido;; 1 = nada;; 0 = nenhuma.
- **EX120 — Fator não testado.** O que a reprodução não incluiu? *Rubrica:* 3 = a confusão de uma campanha real;; 2 = efeitos ao vivo;; 1 = nada;; 0 = nenhuma.

<a id="ch-41"></a>

## Capítulo 41 — Fatores humanos e política cibernética: otimização do sistema

### Objetivos de aprendizagem

Você vai (1) otimizar o programa com um orçamento fixo; (2) comparar os benefícios marginais dos investimentos; (3) evitar otimizar uma única medida em detrimento do todo.

### 41.1 Um orçamento fixo

O conselho da Greyford concede ao programa um orçamento fixo para o próximo ano e pergunta a Aiko como gastá-lo para obter a maior redução de risco. As opções incluem mais simulações, um segundo analista de triagem, chaves de segurança para o pessoal do setor financeiro e da sala de controle, uma filtragem de e-mail melhor e mais conteúdo de reciclagem. Cada opção tem um custo e um efeito estimado sobre as perdas esperadas. Otimizar, aqui, significa escolher a combinação que traz o maior benefício dentro do orçamento, respeitando restrições como o ônus para os funcionários e as regras éticas das simulações.

### 41.2 Benefício marginal

O laboratório ordena as opções pela redução estimada de perdas por unidade de custo e as seleciona de forma gulosa até o orçamento acabar. As chaves de segurança para o pessoal do setor financeiro e da sala de controle dão o maior benefício por unidade de custo, porque eliminam o risco de roubo de credenciais nas funções mais visadas. Mais simulações dão o menor benefício por unidade de custo, já que o programa as realiza mensalmente. Aiko apresenta o resultado como orientação, e não como resposta precisa, porque as estimativas de efeito vêm de julgamento informado pelas evidências da avaliação.

### Laboratório — Seleção gulosa de investimentos dentro de um orçamento

```python
# Greedy selection of programme investments by benefit per cost under a budget of 100 units (synthetic).
opts = [("security keys", 40, 120), ("filtering", 30, 60), ("peak analyst", 25, 45), ("refresher content", 15, 18), ("more simulations", 20, 10)]
budget = 100; spent = 0; chosen = []
for name, cost, benefit in sorted(opts, key=lambda o: o[2] / o[1], reverse=True):
    print(f"{name}: benefit/cost {benefit / cost:.2f}")
    if spent + cost <= budget: chosen.append(name); spent += cost
print("chosen:", chosen, "spent:", spent)
```

Execute com `python3 lab_budget.py`. Saída verificada:

```text
security keys: benefit/cost 3.00
filtering: benefit/cost 2.00
peak analyst: benefit/cost 1.80
refresher content: benefit/cost 1.20
more simulations: benefit/cost 0.50
chosen: ['security keys', 'filtering', 'peak analyst'] spent: 95
```

### 41.3 Visão do sistema como um todo

Aiko alerta contra a otimização de uma única medida. Gastar tudo para reduzir as taxas de clique nas simulações poderia produzir um bom gráfico, mas pouca redução nas perdas reais. Herley (2009) argumentou que os conselhos de segurança muitas vezes custam aos usuários mais esforço do que o dano que evitam, e a otimização deve contar o esforço dos funcionários como um custo real. Por isso, ela inclui as horas estimadas de trabalho dos funcionários em cada opção. O plano final compra chaves de segurança, um segundo analista nos horários de pico e melhorias na filtragem, e mantém as simulações no nível mensal atual.

### Exemplo resolvido

Aiko ordena os investimentos por benefício por custo dentro de um orçamento fixo, inclui o esforço dos funcionários como custo e seleciona chaves, um analista e filtragem.

> **Caso sintético.** Os custos e efeitos são sintéticos; Herley (2009) é real.

### Erros e limites

As estimativas de efeito são incertas. A seleção gulosa nem sempre é ótima.

### Exercícios

- **EX121 — Melhor relação.** Que opção teve o maior benefício por custo? *Rubrica:* 3 = chaves de segurança para as funções visadas;; 2 = chaves;; 1 = simulações;; 0 = nenhuma.
- **EX122 — Seleção no laboratório.** O que o laboratório selecionou dentro do orçamento? *Rubrica:* 3 = chaves, filtragem e analista de pico por 95 de 100 unidades;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX123 — O argumento de Herley.** Que custo Aiko incluiu seguindo Herley (2009)? *Rubrica:* 3 = o esforço dos funcionários;; 2 = esforço;; 1 = só dinheiro;; 0 = nenhuma.

<a id="ch-42"></a>

## Capítulo 42 — Fatores humanos e política cibernética: pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa aplicada a partir de dados operacionais; (2) desenhar um estudo ético dentro do programa; (3) compartilhar os achados com responsabilidade.

### 42.1 Formular a pergunta

Os dados da operação levantam uma pergunta de pesquisa: acrescentar à mensagem de veredito uma frase curta sobre por que o e-mail era perigoso melhora a precisão dos reportes posteriores, em comparação com um veredito simples? Aiko formula a pergunta com precisão, define a precisão dos reportes como a proporção dos reportes de uma pessoa que são ameaças genuínas e escolhe um horizonte de seis meses. Ela consulta os trabalhos publicados e descobre que o conteúdo do retorno é pouco estudado em comparação com o conteúdo do treinamento, de modo que a pergunta pode acrescentar conhecimento útil para além da Greyford. A Profa. Kerr aprova a pergunta.

### 42.2 Desenho ético

Aiko desenha um estudo que sorteia equipes, e não indivíduos, para receber o veredito simples ou o explicado, de modo que os colegas compartilhem uma única versão. As duas versões são inofensivas e a mudança é pequena. Ela busca a aprovação do comitê de ética da universidade e a concordância dos representantes dos funcionários, informa aos funcionários que a redação do retorno está sendo comparada e permite que qualquer equipe se exclua. Os dados são analisados apenas no nível da equipe. O desenho segue os mesmos princípios das regras de simulação: respeito, transparência e nenhuma consequência individual.

### 42.3 Compartilhar os achados

Depois de seis meses, as equipes com o veredito explicado mostram uma precisão de reporte um pouco maior, mas a diferença está dentro do esperado pelo acaso, dado o número de equipes. Aiko relata honestamente o resultado como inconclusivo e sugere um estudo maior, com várias organizações. Ela compartilha os achados primeiro com os funcionários, depois com o regulador e, por fim, em um artigo curto com ilustrações sintéticas em vez de dados brutos. A Profa. Kerr lembra que resultados inconclusivos merecem publicação, porque resultados nulos não publicados distorcem o registro da pesquisa.

### Exemplo resolvido

Aiko formula uma pergunta sobre a redação do retorno, sorteia equipes com aprovação ética e relata abertamente um resultado inconclusivo.

> **Caso sintético.** O estudo é sintético.

### Erros e limites

Poucas equipes dão baixo poder estatístico. Pode haver contaminação entre equipes.

### Exercícios

- **EX124 — Unidade de randomização.** Que unidade foi sorteada? *Rubrica:* 3 = equipes;; 2 = equipe;; 1 = indivíduos;; 0 = nenhuma.
- **EX125 — Definição de precisão.** Como a precisão dos reportes foi definida? *Rubrica:* 3 = proporção dos reportes de uma pessoa que são ameaças genuínas;; 2 = proporção genuína;; 1 = nada;; 0 = nenhuma.
- **EX126 — Resultado nulo.** Por que publicar o resultado inconclusivo? *Rubrica:* 3 = nulos não publicados distorcem o registro da pesquisa;; 2 = registro;; 1 = nada;; 0 = nenhuma.

<a id="ch-43"></a>

## Capítulo 43 — Prática na indústria ou no serviço público

### Objetivos de aprendizagem

Você vai (1) trabalhar dentro das restrições de uma organização de serviço público; (2) dialogar com reguladores e com o público; (3) refletir sobre a prática profissional.

### 43.1 Restrições do serviço público

A Greyford é uma concessionária de serviço público com o dever de fornecer água segura e de reportar incidentes aos reguladores. Aiko aprende que as decisões demoram mais do que em empresas privadas, porque os gastos precisam da aprovação do conselho e das regras de compras. Entre os funcionários há operadores de longa data que desconfiam de iniciativas novas. Ela se adapta planejando as mudanças em torno dos ciclos orçamentários, envolvendo os operadores desde cedo e explicando a ligação com a segurança pública. Trabalhar dentro dessas restrições faz parte da prática profissional, e não é um obstáculo a ser lamentado ou contornado por atalhos informais.

### 43.2 Reguladores e o público

O regulador pergunta como a Greyford gere o lado humano do risco cibernético. Aiko prepara um resumo curto das evidências: o estatuto, as medidas, os resultados de verificação e validação e as regras éticas das simulações. O regulador aprecia a honestidade sobre os limites. A Greyford também publica uma breve declaração aos clientes explicando que nunca pedirá dados bancários por e-mail, apoiando os clientes contra golpes de falsificação de identidade. O diálogo para além da organização reconhece que os atacantes miram clientes e fornecedores, além dos funcionários. A declaração também é impressa nas contas.

### 43.3 Prática reflexiva

Aiko mantém um diário reflexivo durante o estágio, registrando decisões, surpresas e o que faria de forma diferente. Ela anota que seus primeiros desenhos subestimavam o tempo de que os operadores precisam para confiar em um processo novo, e que as conversas informais na sala de controle lhe ensinaram mais do que os questionários. As diretrizes de cultura de cibersegurança da ENISA enfatizam entender a cultura existente antes de mudá-la, e o diário mostra quanto desse entendimento veio de ouvir, e não de medir. O diário passa a fazer parte de seu portfólio profissional.

### Exemplo resolvido

Aiko se adapta às restrições do serviço público, prepara evidências para o regulador, apoia os clientes contra golpes e mantém um diário reflexivo.

> **Caso sintético.** O estágio é sintético; as diretrizes da ENISA são reais.

### Erros e limites

Diários reflexivos podem virar autojustificação. Declarações públicas precisam ser atualizadas.

### Exercícios

- **EX127 — Adaptação às restrições.** Como Aiko se adaptou às decisões lentas? *Rubrica:* 3 = planejando em torno dos ciclos orçamentários e envolvendo os operadores desde cedo;; 2 = planejamento;; 1 = contornando as regras;; 0 = nenhuma.
- **EX128 — Declaração aos clientes.** O que a declaração aos clientes prometia? *Rubrica:* 3 = a Greyford nunca pedirá dados bancários por e-mail;; 2 = nunca;; 1 = nada;; 0 = nenhuma.
- **EX129 — Maior lição.** O que o diário mostrou sobre aprender a cultura? *Rubrica:* 3 = a maior parte do entendimento veio de ouvir;; 2 = ouvir;; 1 = questionários;; 0 = nenhuma.

<a id="ch-44"></a>

## Capítulo 44 — Projeto final de engenharia I

### Objetivos de aprendizagem

Você vai (1) definir um problema de projeto final; (2) levantar requisitos e restrições; (3) planejar o projeto e a avaliação.

### 44.1 O problema do projeto final

O projeto final de Aiko enfrenta uma lacuna encontrada durante o estágio: terceirizados e temporários, cerca de um quinto da força de trabalho, estão fora da maior parte do programa. Eles não têm o botão de reporte em dispositivos pessoais, não recebem reciclagens e muitas vezes são alvo de mensagens falsas de fornecedores. O projeto pergunta como estender os reportes, os controles e o retorno aos terceirizados de forma justa e proporcional ao acesso que têm. Ela define o sucesso como terceirizados reportando a uma taxa semelhante à dos funcionários em até seis meses, sem acrescentar ônus significativo.

### 44.2 Requisitos e restrições

Aiko entrevista oito terceirizados e quatro gestores. Os terceirizados querem uma forma simples de reportar a partir de qualquer dispositivo e não querem ser mais monitorados do que os funcionários. Os gestores querem que os terceirizados sigam as mesmas regras de verificação para pagamentos e acessos. As restrições incluem contratos que limitam o tempo de treinamento e dispositivos que a Greyford não controla. Ela escreve os requisitos, incluindo um formulário web e um endereço de encaminhamento para reportes, um módulo de integração de dez minutos e regras de verificação idênticas, e confere cada um com a equipe de compras em relação às restrições.

### 44.3 Plano de projeto e avaliação

Aiko planeja o projeto em duas partes: uma via de reporte independente do dispositivo e uma integração que cubra as três perguntas do capítulo 35 e as etapas de verificação. A avaliação comparará mensalmente as taxas de reporte dos terceirizados com as dos funcionários, usando um teste de significância adequado a grupos pequenos, e medirá o ônus por questionário depois de três meses. Ela escreve um cronograma com marcos para projeto, revisão, piloto e avaliação. A Profa. Kerr pede que ela defina de antemão que resultado a levaria a abandonar o projeto, e ela acrescenta isso ao plano.

### Exemplo resolvido

Aiko define um projeto final sobre reportes de terceirizados, levanta as necessidades de terceirizados e gestores e planeja o projeto e a avaliação com uma regra de parada.

> **Caso sintético.** O projeto final é sintético.

### Erros e limites

A rotatividade dos terceirizados complica a avaliação. Grupos pequenos geram incerteza ampla.

### Exercícios

- **EX130 — Lacuna tratada.** Que grupo o projeto final tratou? *Rubrica:* 3 = terceirizados e temporários;; 2 = terceirizados;; 1 = nada;; 0 = nenhuma.
- **EX131 — Preocupação dos terceirizados.** O que os terceirizados não queriam? *Rubrica:* 3 = mais monitoramento do que os funcionários;; 2 = monitoramento;; 1 = nada;; 0 = nenhuma.
- **EX132 — Regra de parada.** O que a Profa. Kerr pediu a Aiko que definisse de antemão? *Rubrica:* 3 = o resultado que a levaria a abandonar o projeto;; 2 = abandonar;; 1 = nada;; 0 = nenhuma.

<a id="ch-45"></a>

## Capítulo 45 — Revisão independente de projeto

### Objetivos de aprendizagem

Você vai (1) preparar um projeto para revisão independente; (2) responder aos achados dos revisores; (3) registrar decisões e riscos residuais.

### 45.1 Preparar a revisão

Aiko submete o projeto para terceirizados a uma banca de revisão independente: um arquiteto de segurança de outra concessionária, um pesquisador de fatores humanos e um representante dos terceirizados. Ela fornece os requisitos, o projeto, o plano de avaliação e os riscos conhecidos. A revisão independente traz perspectivas que o projetista não consegue oferecer, porque os projetistas tendem a ver o que pretendiam, e não o que construíram. Ela pede aos revisores que se concentrem na usabilidade, na justiça e em saber se os controles deteriam os ataques identificados no capítulo 24. Os revisores recebem o pacote duas semanas antes da reunião.

### 45.2 Achados dos revisores

A banca levanta seis achados. O arquiteto observa que o endereço de encaminhamento poderia ser falsificado (spoofing) para enviar vereditos falsos; o projeto é alterado para que os vereditos cheguem apenas pela conta do formulário web. O pesquisador observa que o módulo de integração testa a memorização, mas não as decisões, e sugere perguntas com cenários. O representante dos terceirizados observa que as agências podem não repassar os materiais, por isso a integração deve ser enviada diretamente. O laboratório totaliza os achados por severidade e as ações tomadas, mostrando quais continuam abertos após a resposta.

### Laboratório — Total de achados da revisão por severidade e situação

```python
# Review findings tally (synthetic).
f = [("high", "closed"), ("high", "closed"), ("medium", "closed"), ("medium", "open"), ("low", "closed"), ("low", "closed")]
for s in ("high", "medium", "low"):
    print(s, "closed", sum(1 for a, b in f if a == s and b == "closed"), "open", sum(1 for a, b in f if a == s and b == "open"))
print("total closed", sum(b == "closed" for _, b in f), "open", sum(b == "open" for _, b in f))
```

Execute com `python3 lab_review.py`. Saída verificada:

```text
high closed 2 open 0
medium closed 1 open 1
low closed 2 open 0
total closed 5 open 1
```

### 45.3 Registrar o risco residual

Aiko registra cada achado, decisão e risco remanescente em um log de revisão. Um achado médio continua aberto: terceirizados que usam dispositivos pessoais podem não receber os vereditos rapidamente. Ela o aceita como risco residual, com revisão depois do piloto, e o dono do risco assina a aceitação. Registrar abertamente os riscos residuais, em linha com a abordagem de gestão de riscos da NIST SP 800-30r1, garante que as decisões de aceitar riscos sejam tomadas pelas pessoas certas e possam ser revistas depois. O log é compartilhado com a banca.

### Exemplo resolvido

Aiko submete seu projeto a revisores independentes, trata os achados sobre spoofing, integração e distribuição, e registra um risco residual aceito.

> **Caso sintético.** A revisão é sintética; a NIST SP 800-30r1 é real.

### Erros e limites

Os revisores podem deixar passar problemas. Riscos aceitos podem ser esquecidos.

### Exercícios

- **EX133 — Achado de spoofing.** O que o arquiteto encontrou? *Rubrica:* 3 = o endereço de encaminhamento poderia ser falsificado para enviar vereditos falsos;; 2 = spoofing;; 1 = nada;; 0 = nenhuma.
- **EX134 — Total no laboratório.** Quantos achados continuaram abertos após a resposta? *Rubrica:* 3 = 5 fechados, 1 médio aberto;; 2 = um aberto;; 1 = nada;; 0 = nenhuma.
- **EX135 — Aceitação do residual.** Quem assinou a aceitação do risco residual? *Rubrica:* 3 = o dono do risco;; 2 = dono;; 1 = o projetista;; 0 = nenhuma.

<a id="ch-46"></a>

## Capítulo 46 — Projeto final de engenharia II

### Objetivos de aprendizagem

Você vai (1) pilotar o projeto final; (2) analisar resultados de grupos pequenos com um teste exato; (3) decidir se o projeto deve ganhar escala.

### 46.1 Conduzir o piloto

Aiko pilota o projeto para terceirizados com sessenta terceirizados ao longo de três meses. Eles recebem a integração diretamente da Greyford, podem reportar pelo formulário web ou pelo endereço de encaminhamento e seguem as mesmas regras de verificação de pagamentos e acessos que os funcionários. Ela acompanha os reportes de e-mails maliciosos reais, os tempos de veredito e as pontuações de ônus. Dois terceirizados saem e três entram durante o piloto, o que ela registra. O piloto inclui um mês de simulações anunciadas sob as regras éticas vigentes, com representantes dos terceirizados na banca de aprovação dos modelos.

### 46.2 Analisar os resultados

No mês de simulação, os terceirizados reportaram 21 de 60 e-mails simulados, e os funcionários em funções comparáveis reportaram 26 de 60. O laboratório calcula o teste exato de Fisher, adequado a grupos pequenos, e não encontra evidência clara de diferença. Aiko relata as duas taxas com o resultado do teste e observa que o piloto era pequeno demais para detectar diferenças modestas. As pontuações de ônus dos terceirizados são semelhantes às dos funcionários, e a mediana do tempo de veredito para os reportes deles fica dentro do nível de serviço de uma hora, atendendo aos principais critérios de sucesso definidos de antemão.

### Laboratório — Teste exato comparando os reportes de terceirizados e funcionários

```python
# Fisher's exact test (two-sided) for contractor vs employee reporting in simulations (synthetic).
from math import comb
a, n1, b, n2 = 21, 60, 26, 60
K, N = a + b, n1 + n2
def p(x): return comb(n1, x) * comb(n2, K - x) / comb(N, K)
p0 = p(a)
pv = sum(p(x) for x in range(max(0, K - n2), min(K, n1) + 1) if p(x) <= p0 * (1 + 1e-9))
print(f"contractors {a}/{n1} = {a / n1:.0%}, employees {b}/{n2} = {b / n2:.0%}, two-sided p = {pv:.2f}")
```

Execute com `python3 lab_fisher.py`. Saída verificada:

```text
contractors 21/60 = 35%, employees 26/60 = 43%, two-sided p = 0.45
```

### 46.3 Decisão de escala

A regra de parada definida no capítulo 44 teria sido acionada se os reportes dos terceirizados caíssem abaixo da metade da taxa dos funcionários; isso não aconteceu. Aiko recomenda estender o programa a todos os terceirizados, com o risco residual dos dispositivos pessoais revisto depois de mais três meses. O conselho aprova. Ela observa que a decisão se apoia no cumprimento de critérios predefinidos, e não em um resultado significativo, o que é adequado porque o objetivo era a paridade, e não a superioridade. Planejar a regra de decisão de antemão a impediu de interpretar os resultados ao sabor de suas esperanças.

### Exemplo resolvido

Aiko pilota os reportes de terceirizados com sessenta terceirizados, não encontra diferença clara em relação aos funcionários com o teste exato de Fisher e amplia a escala com base em critérios predefinidos.

> **Caso sintético.** Os dados do piloto são sintéticos.

### Erros e limites

Pilotos pequenos não demonstram equivalência com precisão. A rotatividade dos terceirizados afeta os resultados.

### Exercícios

- **EX136 — Taxas do piloto.** Quais foram as taxas de reporte na simulação? *Rubrica:* 3 = terceirizados 21/60 e funcionários 26/60;; 2 = 35% contra 43%;; 1 = nada;; 0 = nenhuma.
- **EX137 — Teste no laboratório.** Que valor-p o teste exato de Fisher deu? *Rubrica:* 3 = cerca de 0,45;; 2 = não significativo;; 1 = 0,05;; 0 = nenhuma.
- **EX138 — Base da decisão.** Em que se baseou a decisão de escala? *Rubrica:* 3 = critérios predefinidos, incluindo a regra de parada;; 2 = critérios;; 1 = significância;; 0 = nenhuma.

<a id="ch-47"></a>

## Capítulo 47 — Ensaio de falha e recuperação

### Objetivos de aprendizagem

Você vai (1) planejar um ensaio de falha do sistema de reportes e verificação; (2) conduzi-lo com segurança; (3) aprender com o que falhou.

### 47.1 Planejar o ensaio

Aiko planeja um ensaio para testar como o programa se comporta quando partes dele falham. Os cenários incluem a ferramenta de triagem ficar fora do ar durante uma campanha, o segundo analista financeiro estar ausente no fim do mês e a equipe de segurança estar inacessível à noite. O ensaio é anunciado a todos os participantes, marcado para um horário tranquilo e aprovado pelos gestores de operações e de segurança operacional. Nenhum funcionário é enganado; o ensaio testa sistemas e procedimentos, e não indivíduos. Cada cenário tem início, observador e condição de parada definidos para garantir a segurança.

### 47.2 Conduzir o ensaio

No primeiro cenário, a ferramenta de triagem é tirada do ar por uma hora. Os reportes se acumulam na caixa postal como previsto, mas os funcionários não recebem mensagens de agradecimento e alguns reportam duas vezes. No segundo, o bloqueio financeiro é escalado corretamente para um analista substituto. No terceiro, a sala de controle alcança o contato de segurança fora do expediente em dez minutos usando a escala de plantão. O laboratório resume o tempo de recuperação de cada cenário em relação à sua meta, mostrando que apenas a queda da triagem excedeu a meta. Os observadores cronometram cada etapa.

### Laboratório — Tempos de recuperação em relação às metas em três cenários de falha

```python
# Recovery times against targets (minutes, synthetic).
s = [("triage outage", 60, 30), ("finance backup", 15, 60), ("out-of-hours contact", 10, 15)]
for name, t, target in s: print(f"{name}: {t} min vs target {target} -> {'MISSED' if t > target else 'met'}")
```

Execute com `python3 lab_recovery.py`. Saída verificada:

```text
triage outage: 60 min vs target 30 -> MISSED
finance backup: 15 min vs target 60 -> met
out-of-hours contact: 10 min vs target 15 -> met
```

### 47.3 Aprender com a falha

Aiko conduz uma revisão sem culpados (blameless). A queda da triagem revelou que o mecanismo de contingência não tinha confirmação automática, de modo que os funcionários ficaram em dúvida se os reportes haviam chegado. A equipe acrescenta uma resposta automática simples da própria caixa postal, independente da ferramenta de triagem. Aiko observa que falhas encontradas em ensaios planejados são muito mais baratas do que as encontradas durante ataques reais. Ela atualiza a tabela de verificação com um novo requisito de confirmação durante quedas, fechando o ciclo entre o ensaio e o projeto. A resposta é testada mensalmente.

### Exemplo resolvido

Aiko conduz um ensaio de falha anunciado com cenários de triagem, setor financeiro e fora do expediente, encontra a falta de confirmação durante quedas e acrescenta um requisito.

> **Caso sintético.** O ensaio é sintético.

### Erros e limites

Ensaios planejados são menos estressantes do que falhas reais. Ensaios em horários tranquilos não capturam os efeitos de pico.

### Exercícios

- **EX139 — Ética do ensaio.** O que o ensaio testa? *Rubrica:* 3 = sistemas e procedimentos, e não indivíduos;; 2 = sistemas;; 1 = a vigilância dos funcionários;; 0 = nenhuma.
- **EX140 — Recuperação no laboratório.** Que cenário excedeu sua meta no laboratório? *Rubrica:* 3 = a queda da triagem, 60 minutos contra 30;; 2 = triagem;; 1 = nada;; 0 = nenhuma.
- **EX141 — Correção acrescentada.** Que correção se seguiu à queda da triagem? *Rubrica:* 3 = uma resposta automática da própria caixa postal;; 2 = confirmação;; 1 = nada;; 0 = nenhuma.

<a id="ch-48"></a>

## Capítulo 48 — Dossiê de evidências

### Objetivos de aprendizagem

Você vai (1) montar um dossiê de evidências do programa; (2) ligar afirmações a evidências; (3) declarar limitações e perguntas em aberto.

### 48.1 Montar o dossiê

Aiko monta um dossiê de evidências para sua avaliação de engenharia e para o regulador da Greyford. Ele contém os requisitos, a justificativa do projeto, as tabelas de verificação, os resultados da validação, a análise do piloto, o relatório do ensaio de falha, o log de revisão e as regras éticas. Cada documento é versionado e datado. O dossiê é organizado em torno de afirmações, como a de que o programa encurta a exposição a e-mails maliciosos, com as evidências de cada afirmação listadas logo abaixo. Essa estrutura ajuda os leitores a ver o que se afirma e com que força isso é sustentado. Um índice lista todos os itens.

### 48.2 Afirmações e evidências

Para cada afirmação, Aiko declara a evidência e sua força. A afirmação sobre a exposição se apoia na comparação antes e depois e na análise de filas, que ela classifica como moderada, porque o desenho não descarta mudanças nos ataques. A afirmação sobre fraude de pagamento se apoia nas tentativas barradas e na análise de confiabilidade. A afirmação de justiça para os terceirizados se apoia no piloto e nas entrevistas. O laboratório conta as afirmações por força de evidência. Ela evita afirmar que o programa mudou a cultura, porque suas evidências não medem a cultura diretamente.

### Laboratório — Afirmações por força de evidência

```python
# Claims by evidence strength (synthetic).
claims = {"shorter exposure": "moderate", "payment fraud caught": "strong", "contractor fairness": "moderate", "low staff burden": "moderate", "lasting effect": "weak"}
for s in ("strong", "moderate", "weak"): print(s, sum(v == s for v in claims.values()))
```

Execute com `python3 lab_dossier.py`. Saída verificada:

```text
strong 1
moderate 3
weak 1
```

### 48.3 Limites e perguntas em aberto

O dossiê termina com limitações e perguntas em aberto: se os efeitos duram mais de dois anos, se os resultados se manteriam em uma concessionária maior e se a redação do retorno importa, dado o estudo inconclusivo. Ela lista os dados que responderiam a cada pergunta. A banca elogia a honestidade do dossiê. A Profa. Kerr lembra que um dossiê é um registro vivo e deve ser atualizado à medida que o programa continua, para que as decisões futuras se apoiem em evidências atuais, e não no retrato tirado para a avaliação.

### Exemplo resolvido

Aiko monta um dossiê baseado em afirmações, classifica a força das evidências e lista as perguntas em aberto.

> **Caso sintético.** O dossiê é sintético.

### Erros e limites

As classificações de força são julgamentos. Os dossiês ficam desatualizados.

### Exercícios

- **EX142 — Organização.** Como o dossiê é organizado? *Rubrica:* 3 = em torno de afirmações, com as evidências abaixo de cada uma;; 2 = afirmações;; 1 = por data;; 0 = nenhuma.
- **EX143 — Forças no laboratório.** O que o laboratório contou? *Rubrica:* 3 = 1 afirmação forte, 3 moderadas e 1 fraca;; 2 = contagens;; 1 = nada;; 0 = nenhuma.
- **EX144 — Afirmação evitada.** Que afirmação Aiko evitou? *Rubrica:* 3 = que o programa mudou a cultura;; 2 = cultura;; 1 = nada;; 0 = nenhuma.

<a id="ch-49"></a>

## Capítulo 49 — Tese de engenharia

### Objetivos de aprendizagem

Você vai (1) estruturar uma tese de engenharia sobre um programa de fatores humanos; (2) apresentar projeto, verificação e validação de forma coerente; (3) escrever com citação e cautela adequadas.

### 49.1 Estrutura da tese

A tese de Aiko se intitula "Projetando um programa de segurança centrado em reportes para uma concessionária de água". Seus capítulos cobrem o problema e o contexto, a literatura, os requisitos, as alternativas de projeto e a escolha, a implementação, a verificação, a validação, o projeto final com terceirizados e as conclusões. Cada capítulo termina com um resumo curto que leva ao seguinte. A estrutura segue o ciclo de vida de engenharia, o que ajuda os examinadores a rastrear cada decisão de projeto do requisito à evidência. Os apêndices trazem as tabelas de verificação, o código dos laboratórios e as aprovações éticas, com exemplos sintéticos no lugar de dados sensíveis. A tese tem noventa páginas.

### 49.2 Argumento coerente

A tese argumenta que um programa centrado em reportes, retorno rápido e controles de apoio reduz a exposição com mais eficácia do que um programa guiado pela conformidade, respeitando ao mesmo tempo os funcionários. Aiko sustenta isso com seus resultados de validação e do piloto, e com literatura como Adams e Sasse (1999), Sasse, Brostoff e Weirich (2001) e Bada, Sasse e Nurse (2019). Ela tem o cuidado de separar o que seus dados mostram do que a literatura sugere, e apresenta seus resultados antes e depois como compatíveis com o argumento, e não como prova dele.

### 49.3 Citação e cautela

Aiko confere cada citação com a fonte original e registra DOIs apenas quando os confirmou. Ela usa linguagem cautelosa: os resultados sugerem, em vez de provar, e os efeitos são descritos com sua incerteza. Ela reconhece que seu caso é uma única concessionária e que outras organizações podem diferir. A Profa. Kerr lê uma versão completa e pede uma única mudança: levar as regras éticas das simulações de um apêndice para o texto principal, porque elas são centrais ao projeto, e não um detalhe administrativo.

### Exemplo resolvido

Aiko estrutura sua tese segundo o ciclo de vida de engenharia, separa suas evidências da literatura e declara os resultados com cautela.

> **Caso sintético.** A tese é sintética; as obras citadas são reais.

### Erros e limites

Um único caso limita a generalização. A literatura pode não se ajustar ao contexto da concessionária.

### Exercícios

- **EX145 — Base da estrutura.** O que a estrutura da tese segue? *Rubrica:* 3 = o ciclo de vida de engenharia;; 2 = ciclo de vida;; 1 = nada;; 0 = nenhuma.
- **EX146 — Separação.** O que Aiko mantém separado? *Rubrica:* 3 = o que seus dados mostram e o que a literatura sugere;; 2 = separação;; 1 = nada;; 0 = nenhuma.
- **EX147 — Mudança pedida.** Que mudança a Profa. Kerr pediu? *Rubrica:* 3 = levar as regras éticas das simulações para o texto principal;; 2 = ética;; 1 = nada;; 0 = nenhuma.

<a id="ch-50"></a>

## Capítulo 50 — Defesa final

### Objetivos de aprendizagem

Você vai (1) preparar uma defesa final de engenharia; (2) responder perguntas sobre projeto e ética; (3) refletir sobre a contribuição e os próximos passos.

### 50.1 Preparação

Aiko prepara uma apresentação de vinte minutos que cobre o problema, a escolha de projeto, a verificação, a validação, o projeto final com terceirizados e os limites. Ela ensaia com colegas que fazem perguntas difíceis sobre custo, ética e evidências. Prepara slides de reserva sobre a análise de confiabilidade, o modelo de filas e o ensaio de falha. Também prepara um resumo de uma página das regras éticas das simulações, esperando perguntas sobre o tema. A preparação se concentra em explicar o raciocínio com clareza, já que os examinadores avaliam a compreensão, e não o acabamento dos slides. Ela também cronometra cada ensaio.

### 50.2 Perguntas

Um examinador pergunta se as simulações deveriam sequer ser usadas, dado o risco à confiança. Aiko responde que a Greyford as usa com parcimônia, sob regras anunciadas e acordadas, sem iscas de sofrimento pessoal e sem consequências individuais, e que elas servem de calibração, e não de medida principal. Outro examinador pergunta como o projeto falharia; ela cita a queda da triagem e o risco de causa comum no fim do mês. Um terceiro pergunta sobre custo; ela apresenta a análise orçamentária com as horas dos funcionários incluídas. Os examinadores notam seu foco constante nas evidências.

### 50.3 Contribuição e próximos passos

Aiko resume sua contribuição: um projeto testado de segurança centrada em reportes para uma concessionária, métodos para verificá-lo e validá-lo e uma extensão justa aos terceirizados. Ela lista os próximos passos: um estudo multicêntrico sobre a redação do retorno, um acompanhamento de dois anos e o compartilhamento do projeto com outras concessionárias por meio do fórum do setor. Os examinadores concedem o grau com distinção. A Profa. Kerr reflete que o projeto mostra como a disciplina de engenharia e o respeito pelas pessoas podem trabalhar juntos em segurança, que era o objetivo do curso.

### Exemplo resolvido

Aiko defende sua tese, responde perguntas sobre a ética das simulações, falhas e custo, e resume sua contribuição e os próximos passos.

> **Caso sintético.** A defesa é sintética.

### Erros e limites

As defesas testam a comunicação, além da substância. Os próximos passos precisam de financiamento.

### Exercícios

- **EX148 — Papel das simulações.** Como Aiko descreve o papel das simulações? *Rubrica:* 3 = calibração parcimoniosa sob regras acordadas, e não a medida principal;; 2 = calibração;; 1 = medida principal;; 0 = nenhuma.
- **EX149 — Exemplos de falha.** Que modos de falha Aiko citou? *Rubrica:* 3 = a queda da triagem e a causa comum no fim do mês;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX150 — Próximo passo.** Cite um próximo passo listado por Aiko. *Rubrica:* 3 = estudo multicêntrico sobre a redação do retorno;; 2 = estudo;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX150. Aiko Tanabe, a Profa. Joanna Kerr, a Rivenhall Technical University, a Greyford Water e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Se os reportes ainda estão subindo, se estabilizaram ou estão recuando depois de uma campanha.

**EX002.** Porque preveria reportes crescendo sem limite, em vez de se estabilizarem.

**EX003.** Como a área sob a curva de caixas de entrada com o e-mail não reportado ao longo do tempo, que reportes mais rápidos encolhem.

**EX004.** A regra de bloquear a tela ao sair e a regra de manter os consoles conectados durante incidentes.

**EX005.** Onze funcionários que têm acesso remoto, mas nenhum treinamento em acesso remoto.

**EX006.** Aproximadamente uma vez por semana, somando seus sete sistemas.

**EX007.** Porque decorrem de condições ambientais como reflexo, ruído e turnos longos.

**EX008.** Aprendem a reconhecer os alarmes sem lê-los, e os importantes se perdem.

**EX009.** Com uma mola de fechamento mais rápida e uma entrada separada para entregas.

**EX010.** Porque um programa pode rodar sem erros e ainda assim produzir respostas erradas.

**EX011.** A semana 3, com 41 reportes.

**EX012.** Trabalhar com contagens e, se forem necessários registros individuais, substituir os nomes por códigos e guardar a chave separadamente.

**EX013.** O que fazer se já tiverem clicado em um link.

**EX014.** Como resultado esperado de boas iscas, com foco na rapidez com que os funcionários reportam.

**EX015.** Usar os mesmos números e incluir as limitações em todas as versões.

**EX016.** Cerca de 2,9 meses para que o benefício extra caia pela metade.

**EX017.** As reciclagens trimestrais, com média de 0,72 contra 0,55 de um único curso anual.

**EX018.** Os minutos dos funcionários que cada calendário consome.

**EX019.** 15,0%, com intervalo de Wilson de 95% de 8,1% a 26,1%.

**EX020.** Porque equipes pequenas variam ao acaso, e os rankings envergonham pessoas por resultados aleatórios.

**EX021.** Vinte pessoas, fundindo as equipes menores.

**EX022.** Por meio de menos senhas e passos mais simples, sem ver os chips.

**EX023.** Oferece proteção semelhante e elimina a tentação de anotar uma senha longa no notebook.

**EX024.** Chaves reservas nos depósitos, com um processo de recuperação claro e rápido.

**EX025.** Porque muitos reportes do mesmo e-mail exigem uma só investigação.

**EX026.** Seis e-mails distintos; o mais reportado teve o primeiro reporte nove minutos após a chegada.

**EX027.** Apenas o remetente, uma impressão digital do assunto e os horários dos reportes, e não corpos de mensagens nem nomes de quem reportou.

**EX028.** Somente com um propósito claro de segurança, aprovação da organização, ausência de dano e explicação honesta depois.

**EX029.** Iscas que exploram medos sobre salário, saúde, família ou demissão.

**EX030.** Porque distrair um operador poderia afetar o tratamento da água, que é crítico para a segurança.

**EX031.** Porque nenhuma pessoa precisa reconhecer e julgar essas mensagens.

**EX032.** Porque aparece em quase todo e-mail de fornecedor e, por isso, carrega pouca informação.

**EX033.** Oito dos dez funcionários.

**EX034.** Porque o hábito de clicar adiante se mantém quando aparece um prompt raro e perigoso.

**EX035.** Corrigindo os certificados internos, de modo que os avisos deixaram de aparecer.

**EX036.** Um catálogo de autoatendimento, pedidos respondidos em até uma hora e direitos temporários por tarefa.

**EX037.** Uma tabela que ligasse funcionários individuais aos cliques em simulações.

**EX038.** Apenas as datas de conclusão, sem as notas dos questionários.

**EX039.** Que os dados de conscientização não serão usados para fins disciplinares.

**EX040.** Leitura no celular, muitas vezes de luvas ou sob luz forte.

**EX041.** No celular, o botão de reporte saía da tela ao rolar.

**EX042.** Porque reportar é a finalidade principal do recurso.

**EX043.** Porque desloca o projeto para apoiar o bom comportamento, em vez de apenas restringi-lo.

**EX044.** Autoridade e urgência.

**EX045.** Verificação por retorno de ligação a um número conhecido para pedidos de fornecedores.

**EX046.** Seus limites e pontos fortes passam a fazer parte do projeto, em vez de serem considerados depois.

**EX047.** Filtrar e-mails sabidamente maliciosos, verificar domínios e agrupar reportes duplicados.

**EX048.** Exigir a digitação de uma senha enquanto se reconhece um alarme crítico.

**EX049.** A malha fica aberta, e os funcionários podem parar de reportar.

**EX050.** Um agradecimento automático, a confirmação de se o e-mail era malicioso e um resumo mensal.

**EX051.** Com retorno, a taxa subiu para 60% no mês 12; sem retorno, caiu para 18%.

**EX052.** Todos os funcionários precisariam ser perfeitos o tempo todo.

**EX053.** Como uma camada entre muitas, e não como a última linha de defesa.

**EX054.** Elas se recusam a autenticar no site errado, então as páginas de login falsas fracassam.

**EX055.** Enviando prompts repetidos até que um usuário cansado aceite um deles.

**EX056.** Porque a chave verifica a identidade do site e não assina para o site errado.

**EX057.** Porque trariam de volta ao sistema o risco de phishing.

**EX058.** Usabilidade das ferramentas de segurança, conscientização e treinamento, e cultura organizacional, entre outros.

**EX059.** Como um conjunto de restrições e objetivos de projeto para a engenharia.

**EX060.** Quando serve a uma só parte interessada, geralmente a direção, e ignora as demais.

**EX061.** O medo de parecer tola ao reportar um e-mail que se revela legítimo.

**EX062.** Porque não pode ser verificado e, por isso, não consegue orientar o projeto.

**EX063.** O reporte com um toque no celular e os agradecimentos em até um minuto.

**EX064.** Reportes mais rápidos e menos ataques bem-sucedidos, e não a conclusão de treinamentos.

**EX065.** A exportação padrão de resultados individuais da ferramenta para uma planilha que os gestores podiam abrir.

**EX066.** Pontos com pouca informação e muita pressão, como pedidos urgentes por telefone.

**EX067.** Pesquisa online, um e-mail falsificado, uma ligação de acompanhamento e um pedido de aprovação de sessão remota.

**EX068.** Lembretes ou automação, como o bloqueio automático de tela.

**EX069.** Que as regras são impraticáveis, e não que os funcionários têm má intenção.

**EX070.** Se os usuários sabem o que fazer, veem como fazer, entendem o retorno e sabem que tiveram sucesso.

**EX071.** Não saber se algo é suspeito o bastante para reportar, citado por 71 de 180 respondentes.

**EX072.** Que qualquer dúvida é um bom motivo para reportar.

**EX073.** Enquadrar os reportes como ajuda aos colegas, e não como dever de segurança.

**EX074.** Que os motoristas não podem usar o celular enquanto dirigem, então são necessárias outras vias de reporte.

**EX075.** Reporte pelos terminais da garagem e por uma central telefônica, além de um resumo mais curto.

**EX076.** Em evidências regulatórias, porque o regulador espera alguns registros de treinamento.

**EX077.** Orientado a compliance 2,75, orientado a reportes 3,85 e orientado ao projeto 3,90.

**EX078.** Verificando que ela se mantinha quando o peso das evidências regulatórias era dobrado.

**EX079.** Do cadastro do fornecedor, nunca do próprio pedido.

**EX080.** Devem ser transparentes, fáceis de contornar e nunca manipuladores.

**EX081.** Por dramatização, com um colega fazendo o papel de quem liga, e não com um exercício de engano.

**EX082.** Os requisitos testáveis escritos no capítulo 21.

**EX083.** Mensagens baseadas no medo, que muitas vezes levam as campanhas ao fracasso.

**EX084.** Se newsletters e faturas de fornecedores deviam ser reportadas.

**EX085.** Porque se relaciona diretamente com o tempo em que os e-mails maliciosos permanecem ativos.

**EX086.** Os dois e-mails nunca reportados causaram a maior parte da exposição, 93% dos minutos-caixa.

**EX087.** Para que uma medida não possa ser manipulada sem que a medida pareada o revele.

**EX088.** Que mostrava apenas grupos de vinte pessoas ou mais e não oferecia exportação individual.

**EX089.** A orientação sobre o que reportar só estava linkada na intranet, então foi acrescentado um link na mensagem de agradecimento.

**EX090.** Cinco de seis requisitos passaram no início, e todos os seis depois da mudança na configuração de notificação.

**EX091.** A pessoa que recebeu o pedido de mudança não pode liberar o bloqueio.

**EX092.** Um número de chamado válido do sistema de manutenção, aprovado por um engenheiro.

**EX093.** Concentra-se apenas nos procedimentos que determinadas funções precisam executar.

**EX094.** 0,25%, porque 0,05 multiplicado por 0,05 é 0,0025.

**EX095.** A falha conjunta subiu de 0,25% para cerca de 1,45% quando a pressão de fim de mês afetou as duas verificações.

**EX096.** Usando o número do cadastro do fornecedor e uma equipe diferente, em vez do e-mail original.

**EX097.** A regra de que mudanças de dosagem exigem um segundo engenheiro.

**EX098.** Quão rapidamente a organização se recupera quando alguém é enganado.

**EX099.** A sala de controle não sabia para quem ligar fora do expediente, então foi publicada uma escala de plantão.

**EX100.** Abre-se um chamado de incidente, o líder é notificado e o e-mail é removido de todas as caixas de entrada.

**EX101.** A função Govern.

**EX102.** O número de mudanças de dados bancários bloqueadas e de pedidos falsos verificados.

**EX103.** Você esperava esta mensagem, ela pressiona por rapidez, e ela pede dinheiro, credenciais ou acesso?

**EX104.** Subiram, em média, de nove para onze em doze.

**EX105.** O controle de bloqueio de pagamento, já que o guia sozinho não pegaria esse caso.

**EX106.** Cerca de doze reportes por hora depois do agrupamento.

**EX107.** Cerca de 7 minutos com quarenta, 14 com oitenta e 25 com noventa e cinco reportes por dia.

**EX108.** Um veredito em até uma hora útil para noventa por cento dos reportes.

**EX109.** Iscas que exploram sofrimento pessoal, como cortes salariais, bônus ou sustos de saúde.

**EX110.** Porque Lain, Kostiainen e Čapkun constataram que as páginas de treinamento embutidas não ajudavam.

**EX111.** Porque imitava uma mensagem do RH sobre férias, perto demais de assuntos pessoais.

**EX112.** Se o sistema cumpre sua finalidade na operação real.

**EX113.** A mediana do tempo caiu de 38 para 9 minutos, e a proporção reportada subiu de 41% para 78%.

**EX114.** O bloqueio de pagamento acrescenta trabalho ao setor financeiro no fim do mês.

**EX115.** Porque ferramentas sob medida exigem especialistas para mantê-las, ao contrário dos recursos de produto com suporte.

**EX116.** O terceiro trimestre, com 14 itens com revisão prevista.

**EX117.** Para que os sucessores possam adaptar o projeto com sabedoria, em vez de congelá-lo ou abandoná-lo.

**EX118.** As mensagens de veredito automático tinham perdido o link para a orientação.

**EX119.** 99% dos reportes receberam veredito em até uma hora, e o mais lento esperou 104 minutos.

**EX120.** A confusão de uma campanha real, como as ligações para o service desk.

**EX121.** Chaves de segurança para o pessoal do setor financeiro e da sala de controle.

**EX122.** Chaves de segurança, filtragem e um analista nos horários de pico, custando 95 de 100 unidades do orçamento.

**EX123.** As horas dos funcionários, já que o esforço dos usuários é um custo real dos conselhos de segurança.

**EX124.** Equipes, para que os colegas compartilhem uma única versão.

**EX125.** A proporção dos reportes de uma pessoa que eram ameaças genuínas.

**EX126.** Porque deixar resultados nulos sem publicação distorce o registro da pesquisa.

**EX127.** Planejando em torno dos ciclos orçamentários, envolvendo os operadores desde cedo e ligando o tema à segurança pública.

**EX128.** Que a Greyford nunca pedirá dados bancários aos clientes por e-mail.

**EX129.** Que a maior parte do entendimento veio de ouvir na sala de controle, e não de medir.

**EX130.** Terceirizados e temporários, cerca de um quinto da força de trabalho.

**EX131.** Ser mais monitorados do que os funcionários.

**EX132.** O resultado que a levaria a abandonar o projeto.

**EX133.** Que o endereço de encaminhamento poderia ser falsificado para enviar vereditos falsos.

**EX134.** Cinco achados foram fechados e um achado médio continuou aberto.

**EX135.** O dono do risco.

**EX136.** Terceirizados 21 de 60 (35%) e funcionários 26 de 60 (43%).

**EX137.** Cerca de 0,45, portanto sem evidência clara de diferença.

**EX138.** Em critérios definidos de antemão, incluindo a regra de parada, e não em um resultado significativo.

**EX139.** Sistemas e procedimentos, sem nenhum funcionário enganado.

**EX140.** A queda da triagem, com 60 minutos contra uma meta de 30.

**EX141.** Uma confirmação automática da caixa postal de reportes, independente da ferramenta de triagem.

**EX142.** Em torno de afirmações, com as evidências de apoio listadas abaixo de cada uma.

**EX143.** Uma afirmação forte, três moderadas e uma fraca.

**EX144.** Que o programa mudou a cultura, porque a cultura não foi medida diretamente.

**EX145.** O ciclo de vida de engenharia, do requisito à evidência.

**EX146.** O que seus próprios dados mostram e o que a literatura sugere.

**EX147.** Levar as regras éticas das simulações de um apêndice para o texto principal.

**EX148.** Como calibração parcimoniosa sob regras anunciadas e acordadas, e não como a medida principal.

**EX149.** A queda da triagem e o risco de causa comum no fim do mês.

**EX150.** Um estudo multicêntrico sobre a redação do retorno, um acompanhamento de dois anos ou o compartilhamento pelo fórum do setor.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Beautement, A., Sasse, M. A., & Wonham, M. (2008). The compliance budget: Managing security behaviour in organisations. *Proceedings of the 2008 New Security Paradigms Workshop*, 47–58. <https://doi.org/10.1145/1595676.1595684>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- Dawkins, S., & Jacobs, J. (2023). *NIST Phish Scale user guide* (NIST TN 2276). NIST. <https://doi.org/10.6028/NIST.TN.2276>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hadnagy, C. (2018). *Social engineering: The science of human hacking* (2nd ed.). Wiley.
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Reason, J. (1990). *Human error*. Cambridge University Press. <https://doi.org/10.1017/CBO9781139062367>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Verizon Business. (2024). *2024 Data breach investigations report*. Verizon. <https://www.verizon.com/business/resources/reports/dbir/>
- Whitten, A., & Tygar, J. D. (1999). Why Johnny can't encrypt: A usability evaluation of PGP 5.0. *Proceedings of the 8th USENIX Security Symposium*. USENIX. <https://www.usenix.org/conference/8th-usenix-security-symposium/why-johnny-cant-encrypt-usability-evaluation-pgp-50>
- Wilson, M., de Zafra, D. E., Pitcher, S. I., Tressler, J. D., & Ippolito, J. B. (1998). *Information technology security training requirements: A role- and performance-based model* (NIST SP 800-16). NIST. <https://doi.org/10.6028/NIST.SP.800-16>
