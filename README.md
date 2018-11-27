# CrawlWordsWebBR

# Proposta Inicial
<p>O objetivo principal deste projeto é estudar a manipulação de dados em larga escala. Qualquer quantidade de dados que não cabe na RAM pode ser considerada "BigData". Neste projeto, foi usada uma fração do web crawler de setembro (http://commoncrawl.org/) que continha apenas os sites brasileiros, com um total de apenas 65GB de 7T originais.</p>


# Objetivo de Projeto
<p> Este projeto consiste em analisar estatisticamente a frequencia das palavras em cada capital, de forma a obter informações de quais palavras são as mais utilizadas e quais são as menos utilizadas, de modo a mapear o vocabulario associado a cada capital


# Tradução dos Dados em Hipóteses


# Obntenção dos Dados

# Estruturação Dos Dados
Em posse dos arquivos de contagem das palavras, foi realizado a estruturação dos dados necessario para a analise.

Esta estruturação foi dividia em duas etapas, a primeira etapa consiste em calcular o pvalue de cada palavra e armanena-los em um dicionario, no qual cada chave, que representa a capital, possui uma lista de tuplas, cada tupla comtem as informações de uma palavra, ordenada da seguinte forma: "palavra", "porcentagem na capital", "porcentagem no estado", "pvalue"

A etapa de estruturação consiste em carregar o arquivo gerado na primeira etapa, o qual consiste em um dicionario, e transformalo em um dataframe, este é filtrado, mantendo apenas as palavras que comtem valor de pvalue menor que 0.05, condição esta que é statisticamente significante.

# Resultados


#Conclusão


# Como Rodar

# Gerar arquivo com os P-value
O arquivo responsavel por calcular e gerar o arquivo que contem o p-value é o br-web-crawler.py

# Dependencias
É necessario instalar as seguintes dependencias:

math        pip3 install math
numpy       pip3 install numpy
pickle      pip3 install pickle
scipy       pip3 install scipy

# Execução
Este script deve ser iniciado executando o seguinte comando:

python3 br-web-craeler.py

geraldo como resultado o arquivo de pvalues denominado palavras_pvalue.pickle 


#---------------------------------------------------------------------

# Gerar Dataframe e resultados
o arquivo responsavel por gerar os dataframes com visualização de resultados é denominado MegaDadosFinal.ipynb

# Dependencias
É necessario instalar as seguintes dependencias:

pickle      pip3 install pickle


#Execução
Este script deve ser executado na plataforma do jupyter, para acessa-la execute o seguinte comando:

jupyter notebook

Em seguida é necessario acessar este arquivo.