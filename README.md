# Crawl Words WebBR - Projeto Final Megadados
Professor Fábio Ayres <br>
Alunos: [Martim José](https://github.com/martimfj), [Sabrina Simão](https://github.com/SabrinaSimao) e [Leonardo Medeiros](https://github.com/Leostayner)

Este é o projeto final da disciplina Megadados (2018.2) do curso de Engenharia da Computação do Insper. O principal objetivo deste projeto era manipular e analisar um grande conjunto de dados, considerados Big Data. Para isso, foi implementado uma Pipeline em um EMR (Elastic Map Reduce) da AWS que utilizou por meio do Zeppelin o Pypark, para manipular os dados do [Common Crawl](http://commoncrawl.org/) do mês de Setembro, que compreende terabytes de dados, da Web mundial. Porém como o professor já havia feito um filtro dos sites brasileiros, esses terabytes de dados se transformaram em 64GB salvos em um bucket S3. A partir dos dados, analisamos estatisticamente a frequência das palavras que são ditas em conjunto com os nomes das capitais dos estados do Brasil. Para assim mapear o vocabulário associado a cada capital dos estados brasileiros.

## Como utilizar
### Pipeline (Extract)
O Pipeline implementado no cluster EMR da AWS rodou o programa desenvolvido em PySpark no Zeppelin, que originou os arquivos pickle *frenquencia_palavras_geral_big* para a contagem de palavras da web brasileira. E o arquivo *frequencia_palavras_big.pickle* para a contagem de palavras para cada capital de Estado brasileiro. Para executar essa etapa, crie um cluester EMR na AWS com Zeppelin, importe o notebook (*crawler_br_code.json*) e rode as células.

Caso queira apenas visualizar a pipeline criada, isso pode ser feito [aqui](https://www.zepl.com/viewer/notebooks/bm90ZTovL21hcnRpbWZqLzdjNDIyMTgyY2U3ZDQyZjk4NWNkZWU5ODQ1NDk0ZDEzL25vdGUuanNvbg) por meio da plataforma Zepl. 

### Calcula P-value (Transform and Load)
Estes arquivos são lidos pelo programa implementado no arquivo python *br-web-crawler* que calcula o *p-value* de das palavras e cria um pickle (*palavras_pvalue.pickle*) com esses dados calculados.

Para executar esse programa instale as dependências via:

```$ sudo pip install -r requirements.txt``` 

E rode com:

```$ python br-web-crawler.py```

### Análise
Toda a análise de dados foi feita no jupyter notebook *MegaDadosFinal.ipynb* que carrega o arquivo gerado no passo anterior. Para re-executar as células do Notebook é preciso instalar as dependências descritas anteriormente e também ter o Jupyter Notebook instalado em seu computador [(instruções)](https://jupyter.readthedocs.io/en/latest/install.html).

## Documentação e resultados
Toda a documentação do projeto se encontra no arquivo *documentação.pdf*.
