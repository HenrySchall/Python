###########################
### Tratamento de dados ###
###########################

# Instalar Bibliotecas (rodar no Windows terminal/powershell)
# pip install yfinance numpy matplotlib plotly-express seaborn radian 

# Importando bases
import radian as rd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

petro = yf.download("PETR4.SA", start='2015-01-01')
petro

petro.info()

# Non-Null Count -> informar se há valores nulos
# Dtype -> Tipagem dos atributos

petro.describe()

# count  
# mean -> média  
# std -> desvio padrão      
# min -> valor mínimo    
# 25% -> 1 quartil
# 50% -> 2 quartil/mediana
# 75% -> 3 quartil
# max -> valor máximo

# Data com o valor mais alto de fechamento
petro[petro['Close'] >= 42.68]

# Quantidade de registros
petro.shape  

# Verificando e eliminando valores nulos
petro.isnull().sum()
petro.dropna(inplace=True)  
petro.isnull().sum()  

# Exportar como CSV
petro.to_csv('gol.csv')

# apagando coluna
dataset_df_normalizado.drop(labels=['Date'], axis=1, inplace=True)