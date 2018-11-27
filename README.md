# Projeto Final MegaDados
--------------
Insper

Prof. Fábio Ayres

Membros: Martim F., Sabrina S., Leonardo M

## Proposta Inicial
-----

O objetivo principal deste projeto foi estudar a manipulação de dados em larga escala. Qualquer quantidade de dados que não cabe na RAM pode ser considerada "BigData".
Neste projeto, foi usada uma fração do web crawler de setembro (http://commoncrawl.org/) que continha apenas os sites brasileiros, com um total de apenas 65GB de 7T originais.

### Tradução dos Dados em Hipóteses
------
Com isso, pensamos em analisar a frequência de palavras em documentos e montar um bag of words (BOW) para a totalidade dos documentos. Sequencialmente, fizemos um filtro que pegava apenas os documentos em que o nome de cada um dos 26 estado do Brasil fosse mencionado, e montamos um BOW individual para cada.

Será que uma palavra (ω) é mais frequênte em textos em que "São Paulo" é mencionado? Por exemplo... "Bras"
Será que as preposições são mencionadas igualmente no BOW total e nos BOWs filtrados? Provavelmente "Tu" para "São Paulo" terá uma frequência bem menor que do total.

Assim, temos:

> Hipótese 0: freq ω (estado) = freq ω (total)

Em contrapartida, é possível que palavras tenham frequências totalmente divergêntes entre um estado e a visão geral dos documentos coletados:

> Hipótese 1: freq ω (estado) ≠  freq ω (total)



### Mecanismos para Cálculo do p-value
------
Foi calculado um pvalue experimental de cada palavra em seu respectivo BOW, usando como parâmetro o teste de hipotese para distribuição binomial.



$$\hat{p} = \frac{n_t p_t + n_e p_e}{n_t + p_e} $$

--------------

$$Z = \frac{p_e - p_t}{\sqrt { \hat{p} (1-\hat{p}) (\frac{1}{n_e} + \frac{1}{n_t}) }}$$


Onde:

$n_t$ é a quantidade da palavras no dicionario total

$n_e$ é a quantidade da palavras no dicionario do estado

$p_t$ é a fracao da palavra por todas as palavras no dic total

$p_e$ é a fracao da palavra por todas as palavras no dic do estado

Usando a biblioteca do scipy, calcula-se a distribuição cumulativa de uma normal passando como parâmetro o valor $Z$ 

Assim, temos:

$$ Pvalue = (1 - norm.cdf(Z))*2 $$
