#Abrindo Arquivos

import pandas as pd

df = pd.read_csv(r'C:\Users\carmo\Documents\Python\Pandas Course\Dados_aula_1.csv', encoding='UTF-8', sep=';')

#Especificando Cabeçalho - parâmetro header = <linha do cabeçalho>
df = pd.read_csv(r'C:\Users\carmo\Documents\Python\Pandas Course\Dados_aula_1.csv', encoding='UTF-8', sep=';', header=0)

#selecionando apenas algumas colunas - usecols= <lista das colunas que vc quer>
df = pd.read_csv(r'C:\Users\carmo\Documents\Python\Pandas Course\Dados_aula_1.csv', encoding='UTF-8', sep=';', usecols=["AddressID", "AddressLine1"])

#lendo x linhas do arquivo - nrows=<num_linhas>
df = pd.read_csv(r'C:\Users\carmo\Documents\Python\Pandas Course\Dados_aula_1.csv', encoding='UTF-8', sep=';', usecols=["AddressID", "AddressLine1"], nrows=200)

#Exibir as primeiras 200 linhas de um df
df.head(200)