import string as string
import random as random
import radian as rd
import pandas as pd
import numpy as np
import scipy.stats as stats
import datetime  
import seaborn as sns
import seaborn.objects as so
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import statsmodels.tsa.stattools as sm
import plotly.express as px
import math as math
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose as decompose
import statsmodels.api as sm

######################
### Série Temporal ###
######################

# Configuração do padrão de medidas do plot dos gráficos
rcParams['figure.figsize'] = 15, 6

# Criando dados aleatórios (Série Anual)
np.random.seed(10) # definir ponto inicial para gerar mesmos valores aleatórios
dados = np.random.normal(0,1,31) # (média,desvio padrão,quantidade de valores [1990 a 2020])
dados

# Criando dados aleatórios (Série Mensal)
# np.random.seed(6)
# dados = np.random.normal(0,1,72)
# dados = pd.DataFrame(dados)
# dados.columns = ['valores']
# dados

# Selecionando o Período 
# data = np.array('2015-01', dtype = np.datetime64())
# data = data + np.arange(72)
# data = pd.DataFrame(data)
# data.columns = ['data']
# data

# Combinando valores
# serie2 = pd.concat([data, dados], axis=1)
# serie2

# serie2 = pd.Series(serie2['valores'].values, index = serie2['data'])
# serie2
# serie2.plot()
# plt.show()

# Criando dados aleatórios (Série Diária)
# np.random.seed(12)
# dados = np.random.normal(0,1,731)
# dados = pd.DataFrame(dados)
# dados.columns = ['valores']
# dados

# Selecionando o Período 
# data = pd.date_range('2019 Jan 1', periods = len(dados3), freq = 'D'
# data

# serie3 = pd.Series(dados['valores'].values, index = data)
# serie3.plot()
# plt.show()

# Tabela 
dados = pd.DataFrame(dados)
dados.columns = ['valores']
dados
dados.shape # verificando valores

# Gráfico 
serie = pd.Series(dados)
serie.plot()
plt.show()

# Selecionando o Período 
periodo = pd.date_range('2000', periods = len(dados), freq = 'Y')
periodo

serie1 = pd.Series(dados['valores'].values, index = periodo)
serie1.plot()
plt.show()

######################
### Autocorrelação ###
######################

np.random.seed(6)
dados1 = np.random.normal(0,1,72)
dados1

serie = pd.Series(dados1)
serie.plot()
plt.show()

## FAC ###
plot_acf(serie, lags=15)
plt.show()

## FACP ###
plot_pacf(serie, lags=30)
plt.show()

### Case Manchas Solares ###

manchas_solares = sm.datasets.sunspots.load_pandas().data
manchas_solares

serie_m = pd.Series(manchas_solares['SUNACTIVITY'].values, index = manchas_solares['YEAR'])
serie_m

serie_m.plot()

plot_acf(serie_m, lags=45)
plt.show()

plot_pacf(serie_m, lags=30)
plt.show()

#########################
### Passeio Aleatório ###
#########################

from random import sample, random

# Série Passeio aleatório 1
# Criando dados
dados_alet = sample(range(100), k=41) # k -> valores retirados de 100
dados_alet

# Criando período
periodo = list(range(1980, 2021))
periodo

serie_alet = pd.Series(dados_alet, index = periodo)
serie_alet
serie_alet.plot()
plt.show()

## Série Passeio aleatório 2
# Criando dados
serie2 = list()
serie2.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movimento = -1 if random() < 0.5 else 1
    valor = serie2[i-1] + movimento
    serie2.append(valor)

serie2 = pd.Series(serie2)
serie2.plot()
plt.show()

##############
### Testes ###
##############

### Testes de Normalidade ###

# - H0: resíduos normalmente distribuídos (p > 0.05)
# - H1: resíduos não são normalmente distribuídos (p <= 0.05)
stats.shapiro(serie1)

# Verificando se segue uma distribuição normal (graficamente)
stats.probplot(serie1, dist="norm", plot=plt)
plt.title("Normal QQ plot")
plt.show()

### Testes de Estacionaridade ###

# Teste pp (Philips-Perron)
# - H0 = é estacionária: p > 0.05
# - H1 = não é estacionária: p <= 0.05
pp_test = sm.phillips_perron(serie1)

# Renomendando saídas 
pp_test_output = {'Estatítica do teste': pp_test[0], 'p-value': pp_test[1], 'Número de lags': pp_test[2], 'Número de Observações': pp_test[3], 'Valores Críticos': pp_test[4]}
pp_test_output

# Teste KPSS (Kwiatkowski-Phillips-Schmidt-Shin)
# - H0 = é estacionária: teste estatístico < valor crítico
# - H1 = não é estacionária: teste estatístico >= valor crítico
kpss_test = sm.kpss(serie1)

kpss_test_output = {'Estatítica do teste': pp_test[0], 'p-value': pp_test[1], 'Número de lags': pp_test[2], 'Valores Críticos': pp_test[3]}
kpss_test_output

# Teste Dickey Fuller
# - H0 = é estacionária:  teste estatístico < valor crítico
# - H1 = não é estacionária: teste estatístico > valor crítico
df_test = sm.adfuller(serie1)

df_test_output = {'Estatítica do teste': pp_test[0], 'p-value': pp_test[1], 'Número de lags': pp_test[2], 'Número de Observações': pp_test[3], 'Valores Críticos': pp_test[4]}
df_test_output

### Testes de Autocorrelação ###

# Teste de Ljung-Box 
# - H0: não autocorrelacionados (p > 0.05)
# - H1: são autocorrelacionados (p <= 0.05)

####################
### Decomposição ###
####################

concentracao = sm.datasets.co2.load_pandas().data
concentracao

serie = pd.Series(concentracao['co2'].values, index = concentracao.index)
serie

serie.plot()
plt.show()

# Valores missing
concentracao.isnull().sum()
concentracao.dropna(inplace=True)

serie2 = pd.Series(concentracao['co2'].values, index = concentracao.index)
serie2.plot()
plt.show()

decomposicao = decompose(serie2, period=15)
decomposicao = decompose(serie2)

decomposicao.plot()
plt.show()

# Renomeando Labels
plt.subplot(411)
plt.plot(serie, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(decomposicao.trend, label='Tendência')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(decomposicao.seasonal,label='Sazonalidade')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(decomposicao.resid, label='Resíduos')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Decomposição multiplicativa
decomp_mult = decompose(serie2,period=7,model='multiplicative')
decomp_mult.plot()

decomp_mult.plot()
plt.show()

####################################
### Tranformação e Diferenciação ###
####################################

##################
### Suavização ###
##################
