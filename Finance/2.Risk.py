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

# Preparando Dados
dataset_df = ['VALE3.SA', 'WEGE3.SA', 'ITUB4.SA', 'BOVA11.SA']

dataset_vector = pd.DataFrame()
for acao in dataset_df:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02', end='2023-12-31')['Close']
dataset_vector

dataset = dataset_vector.rename(columns={'VALE3.SA': 'VALE', 'WEGE3.SA': 'WEGE','ITUB4.SA': 'ITAU', 'BOVA11.SA': 'BOVA'})

dataset.isnull().sum()
dataset.dropna(inplace=True)
dataset.isnull().sum()

dataset

dataset.to_csv('dataset_df.csv')
dataset = pd.read_csv('dataset_df.csv')
dataset

############################
### Retornos Anuais Vale ###
############################

# dataset.loc[dataset['Date'] == "None"]

# 2021
dataset['VALE'][dataset['Date'] == '2021-01-04']
dataset['VALE'][dataset['Date'] == '2021-12-30']

np.log(77.95/91.45)*100

# 2022
dataset['VALE'][dataset['Date'] == '2022-01-03']
dataset['VALE'][dataset['Date'] == '2022-12-29']

np.log(88.87/78.0)*100

# 2023
dataset['VALE'][dataset['Date'] == '2023-01-02']
dataset['VALE'][dataset['Date'] == '2023-12-28'] 

np.log(77.1/89.40)*100

# Resultados: 
# 2021 -> -15.97%
# 2022 -> 13.04%
# 2023 -> -14.80%

############################
### Retornos Anuais Wege ###
############################

# dataset.loc[dataset['Date'] == "None"]

# 2021
dataset['WEGE'][dataset['Date'] == '2021-01-04']
dataset['WEGE'][dataset['Date'] == '2021-12-30']

np.log(32.98/37.31)*100 

# 2022
dataset['WEGE'][dataset['Date'] == '2022-01-03']
dataset['WEGE'][dataset['Date'] == '2022-12-28']

np.log(38.70/32.02)*100

# 2023
dataset['WEGE'][dataset['Date'] == '2023-01-02']
dataset['WEGE'][dataset['Date'] == '2023-12-27']

np.log(36.84/38.09)*100

# Resultados: 
# 2021 -> -12.33%
# 2022 -> 18.94%
# 2023 -> -3.33%

#############
### Média ###
#############

# Vetor de retornos
retorno_vale = np.array([-15.97, 13.04, 14.80])
retorno_wege = np.array([-12.33, 18.94, -3.33])

media_vale = retorno_vale.mean()
media_vale # -> 3.95

media_wege = retorno_wege.mean()
media_wege # -> 1.09

#################
### Variância ###
#################

variancia_vale = retorno_vale.var()
variancia_vale # -> 199.05

variancia_wege = retorno_wege.var()
variancia_wege # -> 172.75

# dataset['VALE'].tail(30).var()

#####################
### Desvio Padrão ###
#####################

# Quanto maior o desvio padrão, maior é o risco (maior variação)

desvio_padrao_vale = retorno_vale.std()
# 14.10% -> Varição do preço 

desvio_padrao_wege = retorno_wege.std()
# 5.65% -> Varição do preço

# dataset['VALE'].tail(30).std()

###############################
### Coeficiente de variação ###
###############################

stats.variation(retorno_vale)*100
stats.variation(retorno_wege)*100

#########################
### Índice de Treynor ###
#########################

########################
### Índice de Sharpe ###
########################

###################
### Risco Médio ###
###################

# Eliminando Coluna Date
dataset.drop(labels = ['Date'], axis=1, inplace=True)
dataset

# Retorno Simples
taxas_retorno = (dataset / dataset.shift(1)) - 1
taxas_retorno

# Desvio Padrão do Período
taxas_retorno.std()*100

# VALE    2.88% -> maior risco
# WEGE    2.17%
# ITAU    2.03%
# BOVA    1.59% -> menor risco

# Desvio Padrão Médio Anual 
taxas_retorno.std()*252

# VALE    7.26%
# WEGE    5.46%
# ITAU    5.13%
# BOVA    4.02%

# Valores anualizados
taxas_retorno.std()*math.sqrt(252)

################################
### Correlação & Covariância ###
################################

# Matriz de Correlações
taxas_retorno.corr()

# Matriz de Covariâncias
taxas_retorno.cov()

#          VALE      WEGE      ITAU      BOVA
# VALE  0.000832  0.000132  0.000193  0.000263
# WEGE  0.000132  0.000471  0.000152  0.000179
# ITAU  0.000193  0.000152  0.000415  0.000256
# BOVA  0.000263  0.000179  0.000256  0.000255

# Gráfico
plt.figure(figsize=(8,8)) 
sns.heatmap(taxas_retorno.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação')
plt.show()

#######################
### Risco Portfolio ###
#######################

dataset.columns

# Carteira
pesos = np.array([0.33, 0.33, 0.34, 0.0])
pesos.sum()

taxas_retorno.cov()
taxas_retorno.cov() * 252

# Variância do Portfolio
np.dot(taxas_retorno.cov() * 252, pesos)
np.dot(pesos, np.dot(taxas_retorno.cov() * 252, pesos))

# Desvio Padrão do Portfolio
math.sqrt(np.dot(pesos, np.dot(taxas_retorno.cov() * 252, pesos))) * 100 # -> 27.31%

# BOVA (Mercado)
pesos2 = np.array([0.0, 0.0, 0.0, 1.0])

# Variância do BOVA
np.dot(taxas_retorno.cov() * 252, pesos2)
np.dot(pesos2, np.dot(taxas_retorno.cov() * 252, pesos2))

# Desvio Padrão do BOVA
math.sqrt(np.dot(pesos2, np.dot(taxas_retorno.cov() * 252, pesos))) * 100 # -> 24.22%

#########################
### Risco Sistemático ###
#########################

taxas_retorno

# Carteira 
variancia_pesos = (taxas_retorno.var() * 252) * pesos
variancia_pesos

# Subtraindo as variâncias
sub = variancia_pesos[0] - variancia_pesos[1] - variancia_pesos[2] - variancia_pesos[3]
sub

# Variância do Portfolio
variancia_portfolio = np.dot(pesos, np.dot(taxas_retorno.cov() * 252, pesos))
variancia_portfolio

# Risco Sistemático Portfolio
risco_nao_sistematico = (variancia_portfolio - sub) * 100
risco_nao_sistematico # -> 8.01%

# Observa-se que do Risco do portfolio foi de 27.31%. Sendo assim desses 27,31%, 
# podemos dizer que 8.01% são de risco não sistemático.