# CrawlWordsWebBR
# Projeto Final MegaDados
-------------

Insper

Prof. Fábio Ayres

Membros: Martim F., Sabrina S., Leonardo M

## Como Usar

Para utilizar este programa é necessario rodar primeiramente o script br-web-crawler.py, para gerar o arquivo para analise, e em seguida rodar o script MegaDadosFinal.ipynb, que consome esse arquivo. 

Caso o script br-web-crawler ja tenha sido executado anteriormente ou você já possua o arquivo "palavras_pvalue.pickle", não é necessário rodá-lo novamente.


## Gerar Arquivo Para Analise (br-web-crawler.py)
O arquivo responsavel por calcular e gerar o arquivo que contem o p-value é o br-web-crawler.py, este arquivo é necessario para rodar os script de análise.

## Dependencias
É necessario instalar as seguintes dependencias:

math:

$pip3 install math

numpy:

$pip3 install numpy

pickle:

$pip3 install pickle

scipy:

$pip3 install scipy

## Execução
Este script deve ser iniciado executando o seguinte comando:

python3 br-web-craeler.py

gerado como resultado o arquivo de pvalues denominado palavras_pvalue.pickle 


## Gerar Formato de Ánalise (MegaDadosFinal.ipynb)
o script responsavel por gerar os dataframes para analise dos dados é o MegaDadosFinal.ipynb

## Dependencias
É necessario instalar as seguintes dependencias:

pickle:

$pip3 install pickle

jupyter notebook:

$pip3 install jupyter-notebook

## Execução
Este script pode ser executado na plataforma do jupyter, para acessa-la execute o seguinte comando:

jupyter-notebook
