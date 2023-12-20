#################################
###### Machine Learning #########
#################################

""" Modelos:
1)Classificação
    - Naive Bayes
    - Árovre de decisão
    - Random Forest
    - KNN
    - SVM (Support Vector Machine)
    - Redes Neurais Artifíciais
    - Regressão Logística
2)Regressão
    - Regressão Linear Simples
    - Regressão Linear Múltipla
    - Regressão Polinomial
    - Regressão SVM
    - Regressão Redes Neurais
    - Regressão Árvore de decisão
3)Associação & Agrupamento
    - Algoritmo Apriori
    - Algoritmo ECLAT
    - Algoritmo K-Means
    - Agrupamento hierárquico
    - DBSCAN """

#pacotes:https://pypi.org/
#trocar atalhos do teclado: crtl K + crtl S

#Instalar pacotes (rodar no terminal/powershell)
pip install radian
pip install pandas
pip install numpy
pip install seaborn
pip install matplotlib
pip install plotly-express

#Importando bases
import radian as rd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#Upload CSV
#Visual Studio
#inverter \ por /
base_credit = pd.read_csv("C:/Users/henri/OneDrive/Códigos/Python/Biblioteca de modelos/Bases de dados/credit_data.csv")
base_credit

#Google Collab
#Área de Trabalho
from google.colab import files
import io
uploaded = files.upload()
uploaded

#Drive
from google.colab import drive
drive.mount("")

base_credit.head(10) # 10 primeiros registros
base_credit.tail(8) # 10 últimos registros
base_credit.describe() # descreve os dados
base_credit[base_credit['income'] >= 69995.685578]
base_credit[base_credit['loan'] <= 1.377630]

#Gráficos
np.unique(base_credit['default'], return_counts=True)

sns.countplot(x = base_credit['default']);
plt.show() #para mostrar o gráfico

plt.hist(x = base_credit['age']);
plt.show()

plt.hist(x = base_credit['income']);
plt.show()

plt.hist(x = base_credit['loan']);
plt.show()

grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color = 'default')
grafico.show()
plt.show()

#Tratando Valores Inconsistentes
base_credit.loc[base_credit['age'] < 0] #

base_credit[base_credit['age'] < 0] #

base_credit2 = base_credit.drop('age', axis = 1) #Apagar a coluna inteira (de todos os registros da base de dados)

base_credit2

base_credit.index

base_credit[base_credit['age'] < 0].index

base_credit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index) # Apagar somente os registros com valores inconsistentes
base_credit3

base_credit3.loc[base_credit3['age'] < 0]

#Preencher os valores inconsistente manualmente
base_credit.mean() # Prencher a média
base_credit['age'].mean()
base_credit['age'][base_credit['age'] > 0].mean()
base_credit.loc[base_credit['age'] < 0, 'age'] = 40.92
base_credit.loc[base_credit['age'] < 0]
base_credit.head(27)

#Tratando Valores Faltantes
base_credit.isnull()
base_credit.isnull().sum()
base_credit.loc[pd.isnull(base_credit['age'])]
base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)
base_credit.loc[pd.isnull(base_credit['age'])]
base_credit.loc[(base_credit['clientid'] == 29) | (base_credit['clientid'] == 31) | (base_credit['clientid'] == 32)]

#Divisão entre previsores e classe
type(base_credit)
X_credit = base_credit.iloc[:, 1:4].values
X_credit
type(X_credit)
y_credit = base_credit.iloc[:, 4].values
y_credit
type(y_credit)

#Escalonamento dos valores
X_credit
X_credit[:,0].min(), X_credit[:,1].min(), X_credit[:,2].min()
X_credit[:,0].max(), X_credit[:,1].max(), X_credit[:,2].max()
from sklearn.preprocessing import StandardScaler
scaler_credit = StandardScaler() 
X_credit = scaler_credit.fit_transform(X_credit)
X_credit[:,0].min(), X_credit[:,1].min(), X_credit[:,2].min()
X_credit[:,0].max(), X_credit[:,1].max(), X_credit[:,2].max()
X_credit

#bases census
base_census = pd.read_csv("C:/Users/henri/OneDrive/Códigos/Python/Biblioteca de modelos/Bases de dados/census.csv")
base_census

#Análise Base
base_census.describe()
base_census.isnull().sum()

#Tipo gráfico 1
grafico = px.treemap(base_census, path=["workclass", "age"])
grafico.show()

#Tipo gráfico 2
grafico = px.parallel_categories(base_census, dimensions=['occupation', 'relationship'])
grafico.show()

#Tratando de Valores Categóricos

#LabelEncoder
from sklearn.preprocessing import LabelEncoder
label_encoder_teste = LabelEncoder()
X_census[:,1]
teste = label_encoder_teste.fit_transform(X_census[:,1]) #convertendo strings para números
teste
X_census[0]

label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

X_census[:,1] = label_encoder_workclass.fit_transform(X_census[:,1])
X_census[:,3] = label_encoder_education.fit_transform(X_census[:,3])
X_census[:,5] = label_encoder_marital.fit_transform(X_census[:,5])
X_census[:,6] = label_encoder_occupation.fit_transform(X_census[:,6])
X_census[:,7] = label_encoder_relationship.fit_transform(X_census[:,7])
X_census[:,8] = label_encoder_race.fit_transform(X_census[:,8])
X_census[:,9] = label_encoder_sex.fit_transform(X_census[:,9])
X_census[:,13] = label_encoder_country.fit_transform(X_census[:,13])

X_census

#OneHotEncoder questão matematica, pode dar peso errado aos fatores

https://scikit-learn.org/stable/modules/preprocessing.html