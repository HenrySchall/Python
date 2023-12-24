## Introdução

### Estatística
A estatística é a ciência que objetiva coletar, organizar, analisar e interpretar dados. Ela é dividida em 3 partes: **Descritiva, Inferencial e Probabilística.**

- Descritiva é aquela relacionada a descrição dos dados, representada pelas medidas de: centralidade (Média, moda e mediana), posição (Amplitude e Quartis), dispersão (Variância e Desvio Padrão).
- Probabilistica é aquela relacionada a conceitos de probabilidades (espaço amostral, eventos) e distribuições de probabilidade discretas e contínuas (Binomial, Poisson, Exponencial e Normal).
- Inferencial é aquela relacionada a estimação de parâmetros, intervalo de confiança e testes de hipóteses.

##### Tipos de Dados

Qualitativos (atributos não numéricos).
- Nominais: Denominações (cores, gênero, raça, títulos…)
- Ordinais: atributos que podem ser classificados (Ex: classificação de filmes mais assistidos, grau de escolaridade, nível de satisfação…).

Quantitativos (atributos numéricas).
- Discreto: valores finitos ou enumeráveis (quantidade de pessoas numa sala, número de carros em um estacionamento…)
- Contínuo: infinitos valores possíveis num intervalo (renda, tempo, altura…).

##### Técnicas de Amostragem
1) Aleatória Simples: Seleção executada por meio de sorteio, sem nenhum filtro.
2) Estratificada: Divisão da população em grupos e seleção aleatória de uma amostra de cada grupo. (Ex: divisão por região, classe social, religião…).
3) Conglomerado (Agrupamento): Divisão da população em grupos com características similares, porém heterogêneas, e seleção aleatória de alguns grupos para analisar todos os elementos destes grupos. (Ex.: Divisão da população de escolas estaduais por região, enfermeiros de uma rede de hospitais… ).  
4) Sistemática: Membros da população são ordenados numericamente e são selecionados aleatoriamente, obedecendo uma sequência numérica. (Ex.: criação de números para cada amostra e seleção obedecendo uma ordem numérica).

##### Outliers 
São dados discrepantes, isto é, são dados muito diferentes dos demais dados pertencentes à variável em análise. A relevância deles deve ser analisada para definir se continuarão no dataset ou se devem ser tratados (corrigidos, excluídos ou substituídos), pois se não forem relevantes, podem interferir significativamente nos resultados das análises.

![Captura de tela 2023-12-23 220326](https://github.com/HenrySchall/R/assets/96027335/d0f92ab2-e51d-4b0e-8113-791683e24083)

##### Testes de hipóteses 
São testes de afirmações sobre um parâmetro. Processo que utiliza estatísticas amostrais para testar uma hipótese (afirmação original) e aceitá-la ou rejeitá-la.

Existem duas hipóteses:
- Hipótese nula (H0)
- Hipótese alternativa (H1):

##### Tipos de erro
- Erro tipo I: hipótese nula rejeitada quando ela for verdadeira
- Erro tipo II: aceita a hipótese nula (não rejeita) sendo ela falsa.

##### Intervalo de confiança
- Intervalo de confiança: Probabilidade de que o parâmetro populacional estimado, esteja no intervalo selecionado.
- Nível de significância: Probabilidade máxima permitida para cometer o erro tipo I.

![Captura de tela 2023-12-23 220736](https://github.com/HenrySchall/R/assets/96027335/fa170bac-c99f-45c1-aa36-5be116073952)

Intervalo de confiança é a área cinza da curva normal padrão. Já os valores críticos (-Zc e Zc) são os níveis de significância do modelo, dado seu intervalo de confiança. 

![Captura de tela 2023-12-23 220817](https://github.com/HenrySchall/R/assets/96027335/2ddf04a2-cfe2-4e9b-b9db-c3fbf3f92db1)

Nível de confiança/significância| Zc 
:---:|:---:|
90%|1,645   
95%|1,96 
99%|2,575

##### Métricas de Desempenho
Erro absoluto médio (MAE – Mean Absolute Error) 

![Captura de tela 2023-12-23 220021](https://github.com/HenrySchall/R/assets/96027335/f5bcb70b-8869-46b5-819c-11266879e2b1)

- Oi = valores observados
- Pi = valores previstos

Raiz do erro quadrático médio (RMSE – Root Mean Squared Error)

![Captura de tela 2023-12-23 220035](https://github.com/HenrySchall/R/assets/96027335/e6ab921d-9983-4256-b3ec-e41c5ae49bb8)

### Teória Econômica & Econometria

Por meio da Econometria é possível avaliar empiricamente a teoria econômica e explicar fatos passados, testar hipóteses, prever resultados de políticas ou eventos futuros e estimar relações entre variáveis econômicas. Isso é viável porque, em geral, há relações de equilíbrio de longo prazo entre variáveis econômicas.

Campos da econometria, como por exemplo:

- Econometria básica (regressão linear múltipla, ...)
- Econometria de séries temporais (AR, MA, ARMA, ARIMA, ARCH, GARCH, VAR, VEC, ...)
- Econometria não-paramétrica (regressão não-paramétrica, ....)
- Microeconometria (dados em painel, ...)
- Macroeconometria (DSGE, DSGE-VAR, VAR, VEC, ...)

##### Estrutura dos dados econômicos

Os dados econômicos apresentam-se em uma variedade de tipos. Embora alguns métodos econométricos possam ser aplicados com pouca ou nenhuma modificação para muitos tipos diferentes de informações, as características especiais de alguns dados devem ser consideradas ou deveriam ser exploradas. Descreveremos a seguir as estruturas de dados mais importantes encontradas nos trabalhos aplicados.

- Corte Transversal: Um conjunto de dados de corte transversal consiste em uma amostra de indivíduos, consumidores, empresas, cidades, estados, países ou uma variedade de outras unidades, tomada em um determinado ponto no tempo, sendo assim 
não podemos considerar que eles foram obtidos por uma amostra aleatória, os dados das unidades não precisam corresponder ao mesmo período e a ordenação dos dados não importa para a análise econométrica.

- Série Temporal: Um conjunto de séries temporais consiste em observações sobre uma variável ou muitas variáveis ao longo do tempo. Exemplos de dados de séries temporais incluem preços de ações, oferda de moeda, índice de preços ao consumidor, produto interno bruto, taxas anuais de homicídios e números de automóveis vendidos. Sendo assim, podemos considerar que eventos passados podem influenciar eventos futuros e a ordenação cronológica das observações transmite informações importantes.

- Dados em Painel: Um conjunto de dados em painel consiste de em uma série temporal para cada registro de corte transversal. Como exemplo, suponha que tenhamos o histórico de salário, educação e emprego para um conjunto de indivíduos ao longo de um período de dez anos. Sendo assim, as mesmas unidades de corte transversal são acompanhadas ao longo de um determinado período e a ordenação no corte transversal de um conjunto de dados em painel não é importante. 
