import string as string
import random as random
import radian as rd
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import seaborn.objects as so
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf
import math as math
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

##################
### Introdução ###
##################

# Criando o dataset
dataset = ['VALE3.SA', 'WEGE3.SA', 'ITUB4.SA', 'BOVA11.SA']

# Criando um vetor de ativos
dataset_vector = pd.DataFrame()
for acao in dataset:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02')['Close']
dataset_vector

########################
### Limpeza de Dados ###
########################

# Renomeando Vetores
dataset_df = dataset_vector.rename(columns={'VALE3.SA': 'VALE', 'WEGE3.SA': 'WEGE','ITUB4.SA': 'ITAU', 'BOVA11.SA': 'BOVA'})
dataset_df

#Verificando valores NULL
dataset_df.isnull().sum()

# Substituindo valores NULL
dataset_df.dropna(inplace=True)
dataset_df.isnull().sum()

dataset_df.info()
dataset_df.describe()

# histograma dos preços
sns.histplot(dataset_df['VALE'], kde = True)
plt.show()

sns.histplot(dataset_df['ITAU'], kde = True)
plt.show()

sns.histplot(dataset_df['WEGE'], kde = True)
plt.show()

# gráfico preços comprados 
dataset_df.plot(xlabel='Date', figsize = (10,7), title = 'Histórico do preço das ações')
plt.show()

figura = px.line(title = 'Comparativo carteira x BOVA')

###########################
### Taxa de Crescimento ### 
###########################

# A Taxa de crescimento reflete o quanto estamos multiplicamos nosso capital sobre o valor da data de compra. Sendo assim, para calcularmos ela usaremos os valores dos ativos normalizados, 
# ou seja, dividindo o preço de fechamento de cada dia, pelo preço inicial de compra.

dataset_df_normalizado = dataset_df.copy()
for i in dataset_df_normalizado.columns[0:]:
  dataset_df_normalizado[i] = dataset_df_normalizado[i] / dataset_df_normalizado[i][0]
dataset_df_normalizado

dataset_df_normalizado.plot(xlabel='Date', figsize = (15,7), title = 'Histórico do preço das ações (Normalizado)')
plt.show()

################################
### Taxas de Retorno Simples ###
################################

# Usa-se para comparar ações DISTINTAS

# Verificando Valores
dataset = dataset_df
dataset
dataset['VALE'][0], dataset['VALE'][2289]

###############
### Período ###
###############

# Retorno Vale 
((dataset['VALE'][2289] - dataset['VALE'][0]) / dataset['VALE'][0]) * 100
# Retorno Wege 
((dataset['WEGE'][2289]- dataset['WEGE'][0]) / dataset['WEGE'][0]) * 100
# Retorno Itaú 
((dataset['ITAU'][2289] - dataset['ITAU'][0]) / dataset['ITAU'][0]) * 100

# Resultados:
# Vale = 192.38%
# Wege = 562.15%
# Itau = 72.80%

##############
### Diário ###
##############

dataset['WEGE']
dataset['WEGE'].shift(1)

# Retorno Wege
dataset['RS Wege'] = (dataset['WEGE'] / dataset['WEGE'].shift(1)) - 1
dataset['RS Wege']

dataset['RS Wege'].plot()
plt.show()

# Retorno Itaú
dataset['RS Itau'] = (dataset['ITAU'] / dataset['ITAU'].shift(1)) - 1
dataset['RS Itau']

dataset['RS Itau'].plot()
plt.show()

# Retorno Vale
dataset['RS Vale'] = (dataset['VALE'] / dataset['VALE'].shift(1)) - 1
dataset['RS Vale']

dataset['RS Vale'].plot()
plt.show()

#############
### Anual ###
#############

# Retorno Wege
(dataset['RS Wege'].mean() * 246) * 100

# Retorno Itaú
(dataset['RS Itau'].mean() * 246) * 100

# Retorno Anual
(dataset['RS Vale'].mean() * 246) * 100

# Resultados:
# Vale = 21.51%
# Wege = 26.01%
# Itau = 10.89%

###################################
### Taxa de Retorno Logaritmica ### 
###################################

# Usa-se para comparar a MESMA ação em períodos diferentes

# Fixando datas
dataset
dataset.iloc[[1216]] # 02/01/2020
dataset.iloc[[1217]] # 03/01/2020
dataset.iloc[[2210]] # 03/01/2024

# Criando dataset do período 1
dataset.vale = ['VALE3.SA']

dataset_vector = pd.DataFrame()
for acao in dataset.vale:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02', end='2020-01-03')['Close']
dataset_vector 

dataset_log = dataset_vector.rename(columns={'VALE3.SA': 'VALE'})
dataset_log.isnull().sum()
dataset_log

# Criando dataset do período 2
dataset.vale = ['VALE3.SA']

dataset_vector = pd.DataFrame()
for acao in dataset.vale:
  dataset_vector[acao] = yf.download(acao, start='2020-01-03', end='2024-01-04')['Close']
dataset_vector 

dataset_log2 = dataset_vector.rename(columns={'VALE3.SA': 'VALE'})
dataset_log2.isnull().sum()
dataset_log2

#############################
### Retorno Logaritmico 1 ###
#############################

# Retorno do Período 
np.log(dataset_log['VALE'][1216]/dataset_log['VALE'][0]) * 100

# Retorno do Diário
dataset_log['RL VALE'] = np.log(dataset_log['VALE'] / dataset_log['VALE'].shift(1))
dataset_log

# Retorno do Anual 
(dataset_log['RL VALE'].mean() * 246) * 100

#############################
### Retorno Logaritmico 2 ###
#############################

# Retorno do Período 
np.log(dataset['VALE'][2210]/dataset['VALE'][1218]) * 100

# Retorno do Diário
dataset_log2['RL VALE'] = np.log(dataset_log2['VALE'] / dataset_log2['VALE'].shift(1))
dataset_log2

# Retorno do Anual 
(dataset_log2['RL VALE'].mean() * 246) * 100

# Resultado Período 1:
# Período = 81.69%
# Anual = 18.55%

# Resultado Período 2:
# Período = 35.15%
# Anual = 8.70%

#############################
### Retorno Logaritmico 3 ###
#############################

np.log(dataset['VALE'][2289]/dataset['VALE'][0]) * 100
dataset['RL Vale'] = np.log(dataset['VALE'] / dataset['VALE'].shift(1))
(dataset['RL Vale'].mean() * 246) * 100

np.log(dataset['WEGE'][2289]/dataset['WEGE'][0]) * 100
dataset['RL Wege'] = np.log(dataset['WEGE'] / dataset['WEGE'].shift(1))
(dataset['RL Wege'].mean() * 246) * 100

np.log(dataset['ITAU'][2289]/dataset['ITAU'][0]) * 100
dataset['RL Itau'] = np.log(dataset['ITAU'] / dataset['ITAU'].shift(1))
(dataset['RL Itau'].mean() * 246) * 100

dataset

####################################
### Retorno de carteira de ações ###
####################################

# Relembrando os dados do dataframe normalizado
dataset_df_normalizado
dataset_df_normalizado.plot(xlabel = 'Date', figsize=(15, 7))
plt.show()

# Apagando a coluna date
dataset_df_normalizado = dataset_df_normalizado.reset_index()
dataset_df_normalizado.drop(labels=['Date'], axis=1, inplace=True)
dataset_df_normalizado

###################################
### Retorno carteira individual ###
###################################

# Retorno do período
retorno_carteira = (dataset_df_normalizado / dataset_df_normalizado.shift(1)) - 1
retorno_carteira.head()

# Retorno anual de cada ativo (%)
retorno_anual = (retorno_carteira.mean() * 246 ) * 100
retorno_anual

#################################
### Retorno carteira conjunta ###
#################################

# Calculando os pesos 
pesos_carteira = np.array([0.33, 0.33, 0.34, 0.0])
pesos_carteira.sum()

# Retorno Carteira 
np.dot(retorno_anual, pesos_carteira)
retorno_anual

#######################
### Carteira X IBOV ###
#######################

dataset_normalizado = dataset_df.copy()
for i in dataset_normalizado.columns[0:]:
  dataset_normalizado[i] = (dataset_normalizado[i] / dataset_normalizado[i][0])
dataset_normalizado.head()

# Limpando colunas não necessárias
dataset_normalizado.drop(labels=['RL Vale'], axis=1, inplace=True)
dataset_normalizado.drop(labels=['RL Itau'], axis=1, inplace=True)
dataset_normalizado.drop(labels=['RL Wege'], axis=1, inplace=True)
dataset_normalizado.drop(labels=['RS Vale'], axis=1, inplace=True)
dataset_normalizado.drop(labels=['RS Itau'], axis=1, inplace=True)
dataset_normalizado.drop(labels=['RS Wege'], axis=1, inplace=True)
dataset_normalizado = dataset_normalizado.reset_index()

dataset_normalizado.head()

dataset_normalizado['CARTEIRA'] = (dataset_normalizado['VALE'] + dataset_normalizado['ITAU'] + dataset_normalizado['WEGE']) / 3
dataset_normalizado

figura = px.line(title = 'Comparativo carteira x BOVA')
for i in dataset_normalizado.columns[1:]:
  figura.add_scatter(x = dataset_normalizado['Date'], y = dataset_normalizado[i], name = i)
figura.show()

dataset_normalizado.drop(['VALE', 'WEGE', 'ITAU'], axis = 1, inplace= True)
dataset_normalizado

figura = px.line(title = 'Comparativo carteira x BOVA')
for i in dataset_normalizado.columns[1:]:
  figura.add_scatter(x = dataset_normalizado['Date'], y = dataset_normalizado[i], name = i)
figura.show()

# Exportar como CSV
dataset_df.to_csv('dataset_df.csv')