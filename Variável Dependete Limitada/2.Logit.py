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
from sklearn.linear_model import LogisticRegression

#############
### Logit ###
#############

cases = pd.read_csv("C:/Users/henri/OneDrive/Repositórios/Python/Datasets/casos_covid.csv", sep=';', encoding='utf-8')
cases

# Obtendo informações dos dados
cases.shape
cases.info()
cases.describe()

##################
### Tratamento ### 
##################

cases.head()
cases.isnull().sum()

cases['cs_sexo'].value_counts()
cases["obito"].value_counts()
cases["cardiopatia"].value_counts()

cases2 = cases.loc[cases.cs_sexo != 'IGNORADO']
cases3 = cases2.loc[cases2.cs_sexo != 'INDEFINIDO']

cases3['cs_sexo'].value_counts()

cases3["obito"] = cases3["obito"].replace({0:"nao", 1:"sim"})
fig = px.pie(cases, names="obito") 

cases3.head()
cases3.info()

plt.scatter(cases3.cs_sexo,cases3.obito)
plt.xlabel('cs_sexo')
plt.ylabel('ÓBITO')
plt.grid(False)
plt.show()

################
### Modelo 1 ###
################

modelo1 = smf.glm(formula='obito ~ cs_sexo', data=cases3, family = sm.families.Binomial()).fit()
print(modelo1.summary()) #glm = regressão logistica

# Estatisticamente significativo: p <= 0,05
# Estatisticamente não é significativo: p > 0,05

# -0.512894 -> relação entre sexo masculino e ir à obito

# Razão de chance (Mesmo que pegar o valor encontrado para a variável é jogar na equação com o número de euler)
razao = np.exp(modelo1.params[1])
razao

# 0.598760333313471, em um intervalo de confiança de 95%, os homens tem 59,87% menos chances de sobrevivência do que mulheres.

coef = 1/razao
coef

# Estatisticamente, com intervalo de confiança de 95%, a chance de uma pessoa do sexo masculino ir a óbito é 1,67 vezes maior do que a chance de uma pessoa do sexo feminino.

################
### Modelo 2 ###
################

plt.scatter(cases3.idade,cases3.obito)
plt.xlabel('IDADE')
plt.ylabel('ÓBITO')
plt.grid(False)
plt.show()

modelo3 = smf.glm(formula='obito ~ idade', data=cases3, family = sm.families.Binomial()).fit()
print(modelo3.summary())

# Razão de chance 
razao1 = np.exp(modelo3.params[1])
razao1

# Em um intervalo de confiança de 95%, para cada ano mais velho, o indivíduo tem 91,80% a menos em comparação à um individuo um ano a menos.

coef = 1/razao1
coef

# Estatisticamente, com intervalo de confiança de 95%, a chance de uma pessoa com idade avançada ir a óbito é 1,09 vezes maior do que a chance de uma pessoa mais jovem.