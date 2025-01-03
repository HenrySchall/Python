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
# dataset = pd.read_csv('dataset_df.csv')
# dataset

# Preparando Dados
dataset = ['VALE3.SA', 'WEGE3.SA', 'ITUB4.SA', 'BOVA11.SA']

dataset_vector = pd.DataFrame()
for acao in dataset:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02', end='2023-12-31')['Close']
dataset_vector

dataset_df = dataset_vector.rename(columns={'VALE3.SA': 'VALE', 'WEGE3.SA': 'WEGE','ITUB4.SA': 'ITAU', 'BOVA11.SA': 'BOVA'})

dataset_df.isnull().sum()
dataset_df.dropna(inplace=True)
dataset_df.isnull().sum()

dataset_df

dataset_df_normalizado = dataset_df.copy()
for i in dataset_df_normalizado.columns[0:]:
  dataset_df_normalizado[i] = dataset_df_normalizado[i] / dataset_df_normalizado[i][0]
dataset_df_normalizado

dataset_df_normalizado.plot(xlabel='Date', figsize = (15,7), title = 'Histórico do preço das ações (Normalizado)')
plt.show()

########################
### Taxas de Retorno ###
########################

dataset_normalizado = dataset_df_normalizado
dataset_taxa_retorno = (dataset_normalizado / dataset_normalizado.shift(1)) - 1
dataset_taxa_retorno

# Preenchendo NAN como 0 (Necessário para o cálculo)
dataset_taxa_retorno.fillna(0, inplace=True)
dataset_taxa_retorno.head()

# Taxa de Retorno Anual
dataset_taxa_retorno.mean() * 252

#######################
### Calculando Beta ###
#######################

# 1) Regressão Linear

# Visualizando os dados
# fig = px.scatter(dataset_taxa_retorno, x = 'BOVA', y = 'VALE', title = 'BOVA x MGLU')
# fig.show()

# Calculando Beta
# beta, alpha = np.polyfit(x = dataset_taxa_retorno['BOVA'], y = dataset_taxa_retorno['VALE'], deg = 1)
# print('beta:', beta, 'alpha:', alpha)

# figura = px.scatter(dataset_taxa_retorno, x = 'BOVA', y = 'VALE', title = 'BOVA x VALE')
# figura.add_scatter(x = dataset_taxa_retorno['BOVA'], y = beta * dataset_taxa_retorno['BOVA'] + alpha)
# figura.show()

# 2) Variâncias & Covariâncias 

matriz_correlacao = dataset_taxa_retorno.drop(columns = ['ITAU', 'WEGE']).corr()
matriz_correlacao

matriz_covariancia = dataset_taxa_retorno.drop(columns = ['ITAU', 'WEGE']).cov() * 252 # anualizando
matriz_covariancia # -> matriz de covariâncias anualizada

# COV(Vale,BOVA)
covariancia_vale_bova = matriz_covariancia.iloc[0, 1]
covariancia_vale_bova

# σ²(BOVA)
variancia_bova = dataset_taxa_retorno['BOVA'].var() * 252
variancia_bova # -> variância de mercado anualizada

# Resultados:
# COV(Vale,BOVA) -> 0.0661
# σ²(BOVA) -> 0.0642

# Beta
beta_vale = covariancia_vale_bova / variancia_bova
beta_vale # -> 1.02

# Como obtemos um beta de 1.02 e por construção o beta de mercado é igual a 1,
# podemos dizer que a vale é 0,2% mais volátil que o mercado no período análisado.

#######################
### Calculando CAPM ###
#######################

# Calculando o Rm
Rm = dataset_taxa_retorno['BOVA'].mean() * 252
Rm # -> 0.1481

# Calculando o Rf
taxa_selic_historico = np.array([12.75, 14.25, 12.25, 6.5, 5.0, 2.0, 9,25, 13,75, 11,75])
Rf = taxa_selic_historico.mean() / 100
Rf # -> 0.2172

# Taxa Selic
# 2015 = 12,75%
# 2016 = 14.25%
# 2017 = 12.25%
# 2018 = 6.5%
# 2019 = 5.0%
# 2020 = 2.0%
# 2021 = 9,25%
# 2022 = 13,75%
# 2023 = 11,75%

capm_vale = Rf + (beta_vale * (Rm - Rf))
capm_vale # -> 0.1460

# O investimento em Vale irá gerar 14,60% retorno, para compensar o risco de se investir nessa empresa

#################
### Portfolio ###
#################

# Calculando os Betas 
matriz_correlacao_port = dataset_taxa_retorno.cov() * 252
matriz_correlacao_port

# COV(Vale,BOVA)
covariancia_vale_bova = matriz_correlacao_port .iloc[0, 3]
covariancia_vale_bova

# COV(Wege,BOVA)
covariancia_wege_bova = matriz_correlacao_port .iloc[1, 3]
covariancia_wege_bova

# COV(Itau,BOVA)
covariancia_itau_bova = matriz_correlacao_port .iloc[2, 3]
covariancia_itau_bova

# σ²(BOVA) 
variancia_bova = dataset_taxa_retorno['BOVA'].var() * 252
variancia_bova # -> variância de mercado anualizada

# Resultados:
# COV(Vale,BOVA) -> 0.0661
# COV(Wege,BOVA) -> 0.0451
# COV(Itau,BOVA) -> 0.0645 
# σ²(BOVA) -> 0.0642

# Beta Vale
beta_vale = covariancia_vale_bova / variancia_bova
beta_vale # -> 1.02

# Beta wege
beta_wege = covariancia_wege_bova / variancia_bova
beta_wege # -> 0,70

# Beta Itau
beta_itau = covariancia_itau_bova / variancia_bova
beta_itau # -> 1.00

# CAPM Vale
capm_vale = Rf + (beta_vale * (Rm - Rf))
capm_vale # -> 0.1460

# CAPM Vege
capm_wege = Rf + (beta_wege * (Rm - Rf))
capm_wege # -> 0.1687

# CAPM Itau
capm_itau = Rf + (beta_itau * (Rm - Rf))
capm_itau # -> 0.1478

###################
### Alternativa ###
###################

# betas = []
# alphas = []
# for ativo in dataset_taxa_retorno.columns[0:-1]:
  # beta, alpha = np.polyfit(dataset_taxa_retorno['BOVA'], dataset_taxa_retorno[ativo], 1)
  # betas.append(beta)
  # alphas.append(alpha)

# betas
# alphas

# def visualiza_betas_alphas(betas, alphas):
  # for i, ativo in enumerate(dataset_taxa_retorno.columns[0:-1]):
    # print(ativo, 'beta:', betas[i], 'alpha:', alphas[i] * 100)

# visualiza_betas_alphas(betas, alphas)

# np.array(betas).mean() * 100 

# capm_empresas = []
# for i, ativo in enumerate(dataset_taxa_retorno.columns[0:-1]):
  # capm_empresas.append(rf + (betas[i] * (Rm - Rf)))

# def visualiza_capm(capm):
  # for i, ativo in enumerate(dataset_taxa_retorno.columns[0:-1]):
    # print(ativo, 'CAPM:', capm[i] * 100)

# visualiza_capm(capm_empresas)

#############################
### CAPM & Beta Portfolio ###
#############################

pesos = np.array([0.33, 0.33, 0.34])

# Beta 
beta_portfolio = [beta_vale, beta_wege, beta_itau]
beta_portfolio

beta_portfolio = np.sum(beta_portfolio * pesos) 
beta_portfolio # -> 0.91
# CAPM 
capm_empresas = [capm_vale, capm_wege, capm_itau]
capm_empresas

capm_portfolio = np.sum(capm_empresas * pesos) * 100
capm_portfolio # -> 15.41%