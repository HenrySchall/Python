########################
### Importando dados ###
########################

#####################
### Yahoo Finance ###
#####################

petro = yf.download("PETR4.SA", start='2015-01-01')
petro

###########
### CSV ###
###########

petro = pd.read_csv('"C:/Users/henri/OneDrive/Repositórios/Python/Impotando_dados/Datasets/petrogol.csv')
petro