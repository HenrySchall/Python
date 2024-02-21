########################
### Importando dados ###
########################

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

#####################
### Yahoo Finance ###
#####################

petro = yf.download("PETR4.SA", start='2015-01-01')
petro

###########
### CSV ###
###########

petro = pd.read_csv('"C:/Users/henri/OneDrive/Repositórios/Python/Impotando_dados /Datasets/petrogol.csv')
petro