# Fatores Humanos e Política Cibernética: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 121, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 50 já estão escritos em português, com os exercícios EX001–EX060 e suas resoluções com rubricas de 0 a 3 e 5 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 21–50 (EX061–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

Capítulos 21–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060 (as de EX061–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Aiko Tanabe, a Profa. Joanna Kerr, a Rivenhall Technical University, a Greyford Water e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
