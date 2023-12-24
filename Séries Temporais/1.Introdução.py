# Configurar figuras
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# Série Anual
np.random.seed(10)
dt = np.random.normal(0,1,41)
# 0 = média
# 1 = desvio padrão
# 41 = quantidade de valores
print(dt)

# Montando a tabela
dt = pd.DataFrame(dt)
dt

# Renomeando coluna
dt.columns = ['valores']
dt.head()

# Analisando dados
dt.shape
dt.describe()

# Criando Série
indice = pd.date_range('1980', periods = len(dt), freq = 'Y')
indice

serie1 = pd.Series(dt['valores'].values, index = indice)

serie1.plot()
plt.show()

# Verificando se é uma distribuição normal
stats.probplot(serie1, dist="norm", plot=plt)
plt.title("Normal QQ plot")
plt.show()

## Teste Shapiro-Wilk ## 
e, p = stats.shapiro(serie1)
print('Estatística de teste: {}'.format(e))
print('p-valor: {}'.format(p))
# não rejeita a hipótese nula, os valores são normalmente distribuídos (p-valor>0,05)

# Série Mensal
np.random.seed(6)
dtm = np.random.normal(0,1,72)
dtm

# Montando a tabela
dtm = pd.DataFrame(dtm)
dtm

# Renomeando coluna
dtm.columns = ['valores']
dtm.head()

# Criando Série
data = pd.date_range('2015-01', periods = len(dtm), freq = 'M')
data

serie2 = pd.Series(dtm['valores'].values, index = data)

serie2.plot()
plt.show()