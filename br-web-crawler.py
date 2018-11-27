import math
import numpy as np
import pickle
from scipy.stats import norm

#Nt = quantidade da palavra no dicionario total
#Ne = quantidade da palavra no dicionario do estado
#Pt = fracao da palavra/todas as palavras no dic total
#Pe = fracao da palavra/todas as palavras no dic do estado
def calcula_pvalue(nt, ne, pt, pe):
    P = ((nt*pt)+(ne*pe))/(nt+ne)
    if pe > pt:
        Z = (pe-pt)/math.sqrt(P*(1-P)*((1/ne)+(1/nt)))
    else:
        Z = (pt-pe)/math.sqrt(P*(1-P)*((1/ne)+(1/nt)))
    p_value = (1 - norm.cdf(Z))*2
    return p_value

def get_total(dic_label):
    return sum(contagem+1000 for contagem in dic_label.values())

def save(data, name):	
    with open(name, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

## MAIN ##
with open('./Pickle/frequencia_palavras_big.pickle', 'rb') as handle:
    dic_load = pickle.load(handle)
    for estado, lista_palavras in dic_load.items():
        dic_load[estado] = dict(lista_palavras)

with open('./Pickle/frequencia_palavras_geral_big.pickle', 'rb') as handle:
    lista_geral_load = pickle.load(handle)
    dic_geral_load = dict(lista_geral_load)

total = get_total(dic_geral_load)
dic_final = {}

for estado, dic_estado in dic_load.items():
    
    dic_final[estado] = [] 
    total_capital  = get_total(dic_estado)

    for palavra, Ne in dic_estado.items():
        if Ne < 1000:
            continue
        Nt = dic_geral_load[palavra] if palavra in dic_geral_load else 0.0
        Pt = Nt / total
        Pe = Ne / total_capital
        pvalue  = calcula_pvalue(Nt, Ne, Pt, Pe)
        dic_final[estado].append((palavra, Pt, Pe, pvalue, Nt, Ne))

save(dic_final, "./Pickle/palavras_pvalue.pickle")
