# Fatores Humanos e Política Cibernética: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 121, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 4 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–50 (EX031–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Aiko Tanabe, a Profa. Joanna Kerr, a Rivenhall Technical University, a Greyford Water e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
