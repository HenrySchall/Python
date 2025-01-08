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
import yfinance as yf
import math as math
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import plotly.express as px 
import statsmodels.api as sm
import statsmodels.formula.api as smf

##########################
### Visualizando Dados ###
##########################

base_credit = pd.read_csv("C:\Users\henri\OneDrive\Repositórios\Python\Datasets\credit_risk_dataset.csv")
base_credit

# default 
# 0 = paga por empréstimo
# 1 = não paga o empréstimo

base_credit.info()
base_credit.describe()
# count  
# mean -> média  
# std -> desvio padrão      
# min -> valor mínimo    
# 25% -> 1 quartil
# 50% -> 2 quartil/mediana
# 75% -> 3 quartil
# max -> valor máximo

# trazendo o cliente com a maior/menor renda
base_credit[base_credit['income'] >= 69995.685578]
base_credit[base_credit['income'] <= 20014.489471]

# visualizando dados default 
np.unique(base_credit['default'], return_counts=True)
# array [1717, 283]
# pagam o empréstimo -> 1717
# não pagam o empréstimo -> 283

sns.countplot(x = base_credit['default'])

# gráfico de correlção das variáveis
grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color = 'default')
grafico.show()

#########################################
### Tratamento Valores Inconsistentes ###
#########################################

# quantidade de registros
base_credit.shape  

# idades menores que zero
base_credit.loc[base_credit['age'] < 0]
# observa-se 3 valores inconsistentes, então:
# 1) Apagar eles
# 2) Apagar a variável
# 3) Substituir pela média

# 1) Apagar eles
base_credit_1 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
base_credit_1

base_credit_1.loc[base_credit['age'] < 0]

# 2) Apagar a variável (coluna)
base_credit_2 = base_credit.drop('age', axis = 1)
base_credit_2

# 3) Substituir pela média
base_credit.mean()
base_credit['age'].mean()
base_credit.loc[base_credit['age'] < 0, 'age'] = 40.92
base_credit.loc[base_credit['age'] < 0]

####################################
### Tratamento Valores Faltantes ###
####################################

# Verificando valores nulos
base_credit.isnull().sum() # quantidade de valores NaN
base_credit.loc[pd.isnull(base_credit['age'])] # quais são os clientes com NaN

# Eliminando valores nulos
base_credit= base_credit.dropna(inplace=True)  
base_credit.isnull().sum()  

# Preenchendo valores nulos com a média
base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)

base_credit.loc[[29]]
base_credit.loc[[31]]
base_credit.loc[[32]]

# Exportar como CSV
base_credit.to_csv('credit_risk_dataset.csv')

#########################################
### Divisão entre previsores e classe ###
#########################################

base_credit

# Criando um vetor com as variáveis explicativas
X_credit = base_credit.iloc[:, 1:4].values
X_credit

# Criando um vetor com a variável dependente
y_credit = base_credit.iloc[:, 4].values
y_credit

# Visualizando dados
X_credit[:,0].min() 
X_credit[:,1].min() 
X_credit[:,2].min()

# Realizando normalização/padronização
scaler_credit = StandardScaler()
X_credit = scaler_credit.fit_transform(X_credit)

X_credit[:,0].min() 
X_credit[:,1].min() 
X_credit[:,2].min()

######################################################
### LabelEncoder (transformar string para numeric) ###
######################################################

base_credit = pd.read_csv("C:/Users/henri/OneDrive/Repositórios/Python/Introdução/Datasets/credit_risk_dataset.csv")
base_credit

label_encoder_teste = LabelEncoder()
X_census[:,1]
teste = label_encoder_teste.fit_transform(X_census[:,1])
teste

label_encoder_workclass = LabelEncoder()
X_census[:,1] = label_encoder_workclass.fit_transform(X_census[:,1])

####################################################
### OneHotEncoder (criação de variáveis dummies) ###
####################################################

onehotencoder_census = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder='passthrough')
X_census = onehotencoder_census.fit_transform(X_census).toarray()
X_census
X_census.shape

# Limpando colunas não necessárias
dataset.drop(labels=['RL Vale'], axis=1, inplace=True)
dataset.drop(labels=['RL Itau'], axis=1, inplace=True)
dataset.drop(labels=['RL Wege'], axis=1, inplace=True)
dataset.drop(labels=['RS Vale'], axis=1, inplace=True)
dataset.drop(labels=['RS Itau'], axis=1, inplace=True)
dataset.drop(labels=['RS Wege'], axis=1, inplace=True)

dataset
dataset.describe()


# Resertar indice 
dados2 = dados2.reset_index(drop=True) # drop é para excluir o índice anterior
dados2