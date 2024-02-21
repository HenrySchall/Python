######################
### Jarvis Machine ###
######################

# Input dataset = ['VALE3.SA', 'WEGE3.SA', 'ITUB4.SA', 'BOVA11.SA']

#dataset_vector = pd.DataFrame()
#for acao in dataset:
#  dataset_vector[acao] = yf.download(acao, start='2015-01-02')['Close']
# dataset_vector

#Verificando valores Null
#dataset_df.isnull().sum()
#dataset_df.dropna(inplace=True)
#dataset_df.isnull().sum()

# dataset_df.plot(xlabel='Date', figsize = (10,7), title = 'Histórico do preço das ações')
#plt.show()

#dataset_df_normalizado = dataset_df.copy()
#for i in dataset_df_normalizado.columns[0:]:
#  dataset_df_normalizado[i] = dataset_df_normalizado[i] / dataset_df_normalizado[i][0]
#dataset_df_normalizado

#dataset_df_normalizado.plot(xlabel='Date', figsize = (15,7), title = 'Histórico do preço das ações (Normalizado)')
#plt.show()

# Retorno Simples
#Input -> retorno_x
#Input -> retorno_semanal_x
#Input -> retorno_anual_x

