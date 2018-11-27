# CrawlWordsWebBR - Projeto Final Megadados
Professor Fábio Ayres <br>
Alunos: [Martim José](https://github.com/martimfj), [Sabrina Simão](https://github.com/SabrinaSimao) e [Leonardo Medeiros](https://github.com/Leostayner)

Este é o projeto final da disciplina Megadados (2018.2) do curso de Engenharia da Computação do Insper. O principal objetivo deste projeto era manipular e analisar um grande conjunto de dados, considerados Big Data. Para isso, foi implementado uma Pipeline em um EMR (Elastic Map Reduce) da AWS que utilizou por meio do Zeppelin o Pypark, para manipular os dados do [Common Crawl](http://commoncrawl.org/) do mês de Setembro, que compreende terabytes de dados, da Web mundial. Porém como o professor já havia feito um filtro dos sites brasileiros, esses terabytes de dados se transformaram em 64GB salvos em um bucket S3. A partir dos dados, analisamos estatisticamente a frequência das palavras que são ditas em conjunto com os nomes das capitais dos estados do Brasil. Para assim mapear o vocabulário associado a cada capital dos estados brasileiros.

## Como utilizar
O Pipeline implementado no cluster EMR da AWS rodou o programa desenvolvido em PySpark no Zeppelin, que originou os arquivos pickle *frequencia_palavras_big.pickle* para a contagem de palavras da web brasileira. E o arquivo *frenquencia_palavras_geral_big* para a contagem de palavras para cada capital de Estado brasileiro. 
* obs: Para executar essa etapa, crie um cluester EMR na AWS com Zeppelin, importe o notebook (*crawler_br_code.json*) e rode as células.

Estes arquivos são lidos pelo programa implementado no arquivo python *br-web-crawler* que calcula o *p-value* de das palavras e cria um pickle (*palavras_pvalue.pickle*) com esses dados calculados.
* obs: Para executar esse programa instale as dependências via `$ sudo pip install -r requirements.txt` e dê `python br-web-crawler.py`.
 
Toda a análise de dados foi feita no jupyter notebook *MegaDadosFinal.ipynb* que carrega o arquivo gerado no passo anterior.
* obs: Para re-executar as células do Notebook, instale as dependênias via `$ sudo pip install -r requirements.txt`. É preciso ter instalado o Jupyter Notebook [(instruções)](https://jupyter.readthedocs.io/en/latest/install.html).

## Documentação e resultados
Toda a documentação do projeto se encontra no arquivo *documentação.pdf*.