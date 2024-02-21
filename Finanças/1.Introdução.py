# Instalar Bibliotecas
# pip install yfinance numpy matplotlib plotly-express pandas seaborn radian

# Importando bases
import string as string
import random as random
import radian as rd
import pandas as pd
import numpy as np
import seaborn as sns
import seaborn.objects as so
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

##################
### Introdução ###
##################

###########################
### Importando um ativo ###
###########################

vale = yf.download("VALE3.SA", start='2015-01-02')
vale

# Open: O preço de abertura nas datas especificadas
# High: O preço da alta nas datas especificadas
# Low: O preço da baixa nas datas especificadas
# Close: O preço de fechamento nas datas especificadas
# Volume: O volume nas datas especificadas
# Adj Close: O preço de fechamento ajustado depois de aplicar distribuições de dividendos ou divisão da ação.

vale.info()
vale.describe()

#plt('VALE3.SA')
#plt.show()

###################################
### Importando multiplos ativos ###
###################################

dataset = ['VALE3.SA', 'WEGE3.SA', 'ITUB4.SA', 'BOVA11.SA']

# Criando um vetor de ativos
dataset_vector = pd.DataFrame()
for acao in dataset:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02')['Close']
dataset_vector

# Renomeando Vetores
dataset_df = dataset_vector.rename(columns={'VALE3.SA': 'VALE', 'WEGE3.SA': 'WEGE','ITUB4.SA': 'ITAU', 'BOVA11.SA': 'BOVA'})
dataset_df

#Verificando valores Null
dataset_df.isnull().sum()

# Substituindo valores Null
dataset_df.dropna(inplace=True)
dataset_df.isnull().sum()

# histograma dos preços
sns.histplot(dataset_df['VALE'], kde = True)
plt.show()

sns.histplot(dataset_df['ITAU'], kde = True)
plt.show()

sns.histplot(dataset_df['WEGE'], kde = True)
plt.show()

dataset_df.plot(xlabel='Date', figsize = (10,7), title = 'Histórico do preço das ações')
plt.show()

# Input

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

# Usa-se para comparar ações distintas
dataset = dataset_df

# Verificando Valores
dataset['VALE'][0], dataset['VALE'][len(dataset) - 1], dataset['VALE'][2242]

# Retorno Vale 
((dataset['VALE'][len(dataset) - 1] - dataset['VALE'][0]) / dataset['VALE'][0]) * 100
 
# Retorno Wege 
((dataset['WEGE'][len(dataset) - 1] - dataset['WEGE'][0]) / dataset['WEGE'][0]) * 100

# Retorno Itaú 
((dataset['ITAU'][len(dataset) - 1] - dataset['ITAU'][0]) / dataset['ITAÚ'][0]) * 100

# Verificando Valores 
dataset['WEGE'], dataset['WEGE'].shift(2)

###############
### Semanal ###
###############

# Retorno Wege
retorno_semanal_wege = (dataset['WEGE'] / dataset['WEGE'].shift(1)) - 1
retorno_semanal_wege

# Retorno Itaú
retorno_semanal_itaú = (dataset['ITAÚ'] / dataset['ITAÚ'].shift(1)) - 1
retorno_semanal_itaú

# Retorno Vale
retorno_semanal_vale = (dataset['VALE'] / dataset['VALE'].shift(1)) - 1
retorno_semanal_vale

#############
### Anual ###
#############

# Retorno Wege
(retorno_semanal_wege.mean() * 246) * 100

# Retorno Itaú
(retorno_semanal_itaú.mean() * 246) * 100

# Retorno Anual
(retorno_semanal_vale.mean() * 246) * 100

###################################
### Taxa de Retorno Logaritmica ### 
###################################

# Usa-se para comparar a mesma ação em períodos diferentes

# Retorno Logaritmica Vale
np.log(dataset['VALE'][len(dataset) - 1] / dataset['VALE'][0]) * 100

# Taxa de Retorno Logaritmica Semanal Vale
retornolog_semanal_vale = np.log(dataset['VALE'] / dataset['VALE'].shift(1))
retornolog_semanal_vale

# Taxa de Retorno Anual
(retornolog_semanal_vale.mean() * 246) * 100








