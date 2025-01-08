# Instalar Bibliotecas (rodar no Windows terminal/powershell)
# pip install yfinance numpy matplotlib plotly-express seaborn radian install plotly yellowbrick sklearn.preprocessing

# Importando bases
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


#############################
### Tipo Básico do Objeto ###
#############################

# Graficamente
fig = px.pie(relacao, names="cs_sexo")
fig.show()

filmes.dtypes()

# int: Tipo inteiro da biblioteca NumPy. Esse tipo de dado não tem suporte a valores ausentes.
# int64: Numero nulo inteiros do Pandas.
# float64: Numero de ponto flutuante da biblioteca NumPy. Esse tipo de dado suporta valores ausentes.
# object: Com esse tipo de dados você trabalhar com sequencias de caracteres. Esses caracteres podem ser números ou letras.
# category: Tipo categórico da biblioteca Pandas.
# bool: Tipo booleano da biblioteca NumPy. Esse tipo de dado não suporta dados ausentes.
# boolean: Tipo booleano que suporta valor nulo.
# datetime64: Tipos data da biblioteca NumPy. Esse tipo aceita valores ausentes.

base_credit.head(10)
base_credit.tail(8)