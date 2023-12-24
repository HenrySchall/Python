# Python
 






### Estatística
A estatística é a ciência que objetiva coletar, organizar, analisar e interpretar dados. Ela é dividida em 3 partes: **Descritiva, Inferencial e Probabilística.**

- Descritiva é aquela relacionada a descrição dos dados, representada pelas medidas de: centralidade (Média, moda e mediana), posição (Amplitude e Quartis), dispersão (Variância e Desvio Padrão).
- Probabilistica é aquela relacionada a conceitos de probabilidades (espaço amostral, eventos) e distribuições de probabilidade discretas e contínuas (Binomial, Poisson, Exponencial e Normal).
- Inferencial é aquela relacionada a estimação de parâmetros, intervalo de confiança e testes de hipóteses.

#### Tipos de Dados

Qualitativos (atributos não numéricos).
- Nominais: Denominações (cores, gênero, raça, títulos…)
- Ordinais: atributos que podem ser classificados (Ex: classificação de filmes mais assistidos, grau de escolaridade, nível de satisfação…).

Quantitativos (atributos numéricas).
- Discreto: valores finitos ou enumeráveis (quantidade de pessoas numa sala, número de carros em um estacionamento…)
- Contínuo: infinitos valores possíveis num intervalo (renda, tempo, altura…).

#### Técnicas de Amostragem
1) Aleatória Simples: Seleção executada por meio de sorteio, sem nenhum filtro.
2) Estratificada: Divisão da população em grupos e seleção aleatória de uma amostra de cada grupo. (Ex: divisão por região, classe social, religião…).
3) Conglomerado (Agrupamento): Divisão da população em grupos com características similares, porém heterogêneas, e seleção aleatória de alguns grupos para analisar todos os elementos destes grupos. (Ex.: Divisão da população de escolas estaduais por região, enfermeiros de uma rede de hospitais… ).  
4) Sistemática: Membros da população são ordenados numericamente e são selecionados aleatoriamente, obedecendo uma sequência numérica. (Ex.: criação de números para cada amostra e seleção obedecendo uma ordem numérica).

#### Outliers
Outliers são dados discrepantes, isto é, são dados muito diferentes dos demais dados pertencentes à variável em análise. A relevância deles deve ser analisada para definir se continuarão no dataset ou se devem ser tratados (corrigidos, excluídos ou substituídos), pois se não forem relevantes, podem interferir significativamente nos resultados das análises. Eles podem ser identificados por observações diretas no dataset (quando a quantidade for pequena), por gráficos e por funções específicas.

![Captura de tela 2023-12-23 220326](https://github.com/HenrySchall/R/assets/96027335/d0f92ab2-e51d-4b0e-8113-791683e24083)


#### Testes de hipóteses
São testes de afirmações sobre um parâmetro. Processo que utiliza estatísticas amostrais para testar uma hipótese (afirmação original) e aceitá-la ou rejeitá-la.

Existem duas hipóteses:
- Hipótese nula (H0)
- Hipótese alternativa (H1): oposto da hipótese nula.

#### Tipos de erro
- Erro tipo I: hipótese nula rejeitada quando ela for verdadeira
- Erro tipo II: aceita a hipótese nula (não rejeita) sendo ela falsa.

#### Intervalo de confiança
Nível de confiança: Probabilidade de que o intervalo estimado contenha o parâmetro populacional.

Esse nível de confiança (c) é a área sob a curva normal padrão entre os valores críticos (-Zc e Zc).

#### Nível de significância (α)
Probabilidade máxima permitida para cometer o erro tipo I.

#### Métricas de Desempenho do modelo
Erro absoluto médio (MAE – Mean Absolute Error) 

![Captura de tela 2023-12-23 220021](https://github.com/HenrySchall/R/assets/96027335/f5bcb70b-8869-46b5-819c-11266879e2b1)

Raiz do erro quadrático médio (RMSE – Root Mean Squared Error)

![Captura de tela 2023-12-23 220035](https://github.com/HenrySchall/R/assets/96027335/e6ab921d-9983-4256-b3ec-e41c5ae49bb8)

#### Comparação de modelos
- AIC: Critério de informação de Akaike.
- BIC: Critério de informação Bayesiano.

### Álgebra Linear
