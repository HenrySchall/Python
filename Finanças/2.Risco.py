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


# Trazendo Dados Exportados
dataset = pd.read_csv('dataset_df.csv')
dataset

# Limpando colunas não necessárias
dataset.drop(labels=['RL Vale'], axis=1, inplace=True)
dataset.drop(labels=['RL Itau'], axis=1, inplace=True)
dataset.drop(labels=['RL Wege'], axis=1, inplace=True)
dataset.drop(labels=['RS Vale'], axis=1, inplace=True)
dataset.drop(labels=['RS Itau'], axis=1, inplace=True)
dataset.drop(labels=['RS Wege'], axis=1, inplace=True)

dataset
dataset.describe()

############################
### Retornos Anuais Vale ###
############################

# 2021
dataset['VALE'][dataset['Date'] == '2021-12-30']
dataset['VALE'][dataset['Date'] == '2021-01-04']

np.log(77.95/91.45)*100

# 2022
dataset['VALE'][dataset['Date'] == '2022-12-29']
dataset['VALE'][dataset['Date'] == '2022-01-03']

np.log(88.87/78.0)*100

# 2023
dataset['VALE'][dataset['Date'] == '2023-12-28'] 
dataset['VALE'][dataset['Date'] == '2023-01-02']

np.log(77.1/89.40)*100

# Resultados: 
# 2021 -> -15.97%
# 2022 -> 13.04%
# 2023 -> -14.80%

############################
### Retornos Anuais Wege ###
############################

# 2021
dataset['WEGE'][dataset['Date'] == '2021-12-30']
dataset['WEGE'][dataset['Date'] == '2021-01-04']

np.log(32.98/37.31)*100 

# 2022
dataset['WEGE'][dataset['Date'] == '2022-12-28']
dataset['WEGE'][dataset['Date'] == '2022-01-03']

np.log(38.70/32.02)*100

# 2023
dataset['WEGE'][dataset['Date'] == '2023-12-27']
dataset['WEGE'][dataset['Date'] == '2023-01-02']

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
media_vale
#3.95

media_wege = retorno_wege.mean()
media_wege
#1.09

#################
### Variância ###
#################

var_vale = retorno_vale.var()
var_vale
#199.05

var_wege = retorno_wege.var()
var_wege 
#172.75

#####################
### Desvio Padrão ###
#####################

# Quanto maior o desvio padrão, maior é o risco (maior variação)

desvio_padrao_vale = retorno_vale.std()
#14.10% -> Varição do preço 

desvio_padrao_wege = retorno_wege.std()
#5.65% -> Varição do preço

# Volatilidade do preço
dataset['VALE'].tail(30).std(), dataset['WEGE'].tail(30).std()

###############################
### Coeficiente de variação ###
###############################

# Mede estatisticamente a dispersão relativa, risco por unidade de retorno. Quanto maior o CV, maior o risco. É muito útil na
# comparação dos riscos de ativos com retornos esperados diferentes

# oeficiente_variacao_vale = (desvio_padrao_vale / media_vale) * 100
#coeficiente_variacao_vale

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

# Retorno 
taxas_retorno = (dataset / dataset.shift(1)) - 1
taxas_retorno

# Desvio Padrão do Período(%)
taxas_retorno.std()*100

# VALE    7.050217 -> maior risco
# WEGE    5.320871
# ITAU    4.991104
# BOVA    3.904960 -> menor risco

# Desvio Padrão Médio Anual 
taxas_retorno.std()*246

# Valores anualizados
taxas_retorno.std()*math.sqrt(246)

################################
### Correlação & Covariância ###
################################

taxas_retorno
taxas_retorno.cov()
taxas_retorno.corr()
plt.figure(figsize=(8,8))
sns.heatmap(taxas_retorno.corr(), annot=True);