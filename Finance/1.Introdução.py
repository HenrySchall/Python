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
import math as math
import yfinance as yf
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
  dataset_vector[acao] = yf.download(acao, start='2015-01-02', end=None)['Close']
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

###########################
### Taxa de Crescimento ### 
###########################

# A Taxa de Crescimento reflete o quanto estamos multiplicamos nosso capital sobre o valor da data de compra. Para calcularmos ela usaremos os valores dos ativos normalizados, 
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

len(dataset) 
dataset['VALE'][0], dataset['VALE'][2338] # contagem começa do zero, por isso volta-se 1 período)
dataset['VALE'][0], dataset['VALE'][len(dataset)-1]

###############
### Período ###
###############

# Retorno Vale 
((dataset['VALE'][2338] - dataset['VALE'][0]) / dataset['VALE'][0]) * 100
((dataset['VALE'][len(dataset)-1] - dataset['VALE'][0]) / dataset['VALE'][0]) * 100
# Retorno Wege 
((dataset['WEGE'][len(dataset)-1] - dataset['WEGE'][0]) / dataset['WEGE'][0]) * 100
# Retorno Itaú 
((dataset['ITAU'][len(dataset)-1] - dataset['ITAU'][0]) / dataset['ITAU'][0]) * 100

# Resultados: (valores considerando end.date 09/07/2024)
# Vale = 196.52%
# Wege = 650.79%
# Itau = 76.34%

######################
### Retorno Diário ###
######################

dataset['WEGE']
dataset['WEGE'].shift(1) # pega a posição anterior

# Retorno Wege
dataset['RS Diário Wege'] = (dataset['WEGE'] / dataset['WEGE'].shift(1)) - 1
dataset['RS Diário Wege']

dataset['RS Diário Wege'].plot()
plt.show()

# Retorno Itaú
dataset['RS Diário Itau'] = (dataset['ITAU'] / dataset['ITAU'].shift(1)) - 1
dataset['RS Diário Itau']

dataset['RS Diário Itau'].plot()
plt.show()

# Retorno Vale
dataset['RS Diário Vale'] = (dataset['VALE'] / dataset['VALE'].shift(1)) - 1
dataset['RS Diário Vale']

dataset['RS Diário Vale'].plot()
plt.show()

dataset

#########################
### Retorno Semestral ###
#########################

# Retorno Wege
(dataset['RS Diário Wege'].mean() * 126) * 100

# Retorno Itaú
(dataset['RS Diário Itau'].mean() * 126) * 100

# Retorno Anual
(dataset['RS Diário Vale'].mean() * 126) * 100

# Resultados:
# Vale = 13.73%
# Wege = 5.58%
# Itau = 10.87%

#####################
### Retorno Anual ###
#####################

# Retorno Wege
(dataset['RS Diário Wege'].mean() * 252) * 100

# Retorno Itaú
(dataset['RS Diário Itau'].mean() * 252) * 100

# Retorno Anual
(dataset['RS Diário Vale'].mean() * 252) * 100

# Resultados:
# Vale = 27.47%
# Wege = 11.17%
# Itau = 21.75%

###################################
### Taxa de Retorno Logaritmica ### 
###################################

# Usa-se para comparar a MESMA ação em períodos diferentes

np.log(dataset['VALE'][len(dataset) - 1]/dataset['VALE'][0]) * 100
dataset['RL Diário Vale'] = np.log(dataset['VALE']/ dataset['VALE'].shift(1))

(dataset['RL Diário Vale'].mean() * 252) * 100

np.log(dataset['WEGE'][len(dataset) - 1]/dataset['WEGE'][0]) * 100
dataset['RL Diário Wege'] = np.log(dataset['WEGE'][len(dataset) - 1] / dataset['WEGE'].shift(1))

(dataset['RL Diário Wege'].mean() * 252) * 100

np.log(dataset['ITAU'][len(dataset) - 1]/dataset['ITAU'][0]) * 100
dataset['RL Diário Itau'] = np.log(dataset['ITAU'][len(dataset) - 1] / dataset['ITAU'].shift(1))

(dataset['RL Diário Itau'].mean() * 252) * 100

dataset

#######################
### Exemplo Prático ###
####################### 

vale = ['VALE3.SA']

#############################
### Retorno Logaritmico 1 ###
#############################

dataset_vector = pd.DataFrame()
for acao in vale:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02', end='2020-01-03')['Close']
dataset_vector 

dataset_log = dataset_vector.rename(columns={'VALE3.SA': 'VALE'})
dataset_log.isnull().sum()
dataset_log

# Retorno do Período 
np.log(dataset_log['VALE'][len(dataset_log)-1]/dataset_log['VALE'][0]) * 100

# Retorno do Diário
dataset_log['RL VALE'] = np.log(dataset_log['VALE'] / dataset_log['VALE'].shift(1))
dataset_log

# Retorno do Anual 
(dataset_log['RL Diário VALE'].mean() * 252) * 100

#############################
### Retorno Logaritmico 2 ###
#############################

dataset_vector = pd.DataFrame()
for acao in vale:
  dataset_vector[acao] = yf.download(acao, start='2020-01-03', end='2024-01-04')['Close']
dataset_vector 

dataset_log2 = dataset_vector.rename(columns={'VALE3.SA': 'VALE'})
dataset_log2.isnull().sum()
dataset_log2

# Retorno do Período 
np.log(dataset['VALE'][len(dataset_log)-1]/dataset['VALE'][0]) * 100

# Retorno do Diário
dataset_log2['RL Diário VALE'] = np.log(dataset_log2['VALE'] / dataset_log2['VALE'].shift(1))
dataset_log2

# Retorno do Anual 
(dataset_log2['RL VALE'].mean() * 252) * 100

# Resultado Período 1:
# Período = 93.73%
# Anual = 19.00%

# Resultado Período 2:
# Período = 85.80%
# Anual = 8.92%

# Observa-se que o Período 1 obteve melhores resultados do que o Período 2

###########################
### Retorno da Carteira ###
###########################

# Reiniciando o dataset (Rodando novamente, sem o calculo dos retornos)
dataset2 = ['VALE3.SA', 'WEGE3.SA', 'ITUB4.SA', 'BOVA11.SA']

dataset_vector = pd.DataFrame()
for acao in dataset2:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02', end=None)['Close']
dataset_vector

dataset_df2 = dataset_vector.rename(columns={'VALE3.SA': 'VALE', 'WEGE3.SA': 'WEGE','ITUB4.SA': 'ITAU', 'BOVA11.SA': 'BOVA'})
dataset_df2

dataset_df2.isnull().sum()
dataset_df2.dropna(inplace=True)
dataset_df2.isnull().sum()

dataset_df_normalizado = dataset_df2.copy()
for i in dataset_df_normalizado.columns[0:]:
  dataset_df_normalizado[i] = dataset_df_normalizado[i] / dataset_df_normalizado[i][0]
dataset_df_normalizado

################################
### Retorno individual Ativo ###
################################

# Retorno do período
retorno_carteira = (dataset_df_normalizado / dataset_df_normalizado.shift(1)) - 1
retorno_carteira.head()

# Retorno anual de cada ativo (%)
retorno_anual = (retorno_carteira.mean() * 252) * 100
retorno_anual # mesmos valores encontrados anteriormente

########################
### Retorno carteira ### 
########################

# Definindo os Pesos de cada Ativo
pesos_carteira = np.array([0.33, 0.33, 0.34, 0.0])
pesos_carteira.sum() # 1.0 = 100%

# Retorno Carteira 
np.dot(retorno_anual, pesos_carteira)

# Retorno da Carteira -> 20,04%
# Retorno do BOVA11 -> 13.40%

#######################
### Carteira X IBOV ###
#######################

dataset_df_normalizado = dataset_df2.copy()
for i in dataset_df_normalizado.columns[0:]:
  dataset_df_normalizado[i] = dataset_df_normalizado[i] / dataset_df_normalizado[i][0]
dataset_df_normalizado

dataset_df_normalizado['CARTEIRA'] = (dataset_df_normalizado['VALE'] + dataset_df_normalizado['ITAU'] + dataset_df_normalizado['WEGE']) / 3
dataset_df_normalizado

dataset_df_normalizado = dataset_df_normalizado.reset_index()

figura = px.line(title = 'Comparativo carteira x BOVA')
for i in dataset_df_normalizado.columns[1:]:
  figura.add_scatter(x = dataset_df_normalizado['Date'], y = dataset_df_normalizado[i], name = i)
figura.show()

# Limpando colunas não necessárias
dataset_df_normalizado.drop(['VALE', 'WEGE', 'ITAU', 'Date'], axis = 1, inplace= True)
dataset_df_normalizado

figura = px.line(title = 'Comparativo carteira x BOVA')
for i in dataset_df_normalizado.columns[1:]:
  figura.add_scatter(x = dataset_df_normalizado['Date'], y = dataset_df_normalizado[i], name = i)
figura.show()

# Exportar Resultados como CSV
dataset_df_normalizado.to_csv('dataset_df.csv')