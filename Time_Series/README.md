## Séries Temporais
#### Objetivos:
- Analisar a origem da série
- Previsões futuras
- Descrição do comportamento da série 
- Analisar perodicidade ou tendência 

#### Tipos:
- Univariada = apenas uma variável se altera ao longo do tempo
- Multivariada = mais de uma variável se altera ao longo do tempo

#### Conceitos:
Série Temporal -> é um conjunto de observações ordenadas no tempo ou um corte particular de um processo estocástico desconhecido

#### Matematicamente: Y = Tdt + Szt + et 
- Tendência (Tdt): Mudanças graduais em longo prazo (crescimento populacional).
- Sazonalidade (Szt): oscilações de subida e de queda que sempre ocorrem em um determinado período (maior valor da conta de energia elétrica no inverno).
- Resíduos (et): apresenta movimentos ascendentes e descendentes da série após a retirada do efeito de tendência ou sazonal (sequência de variáveis aleatórias).

![Figura-4-Decomposicao-da-serie-temporal-em-componentes-de-sazonalidade-de-tendencia-e](https://github.com/HenrySchall/Time-Series/assets/96027335/46bf2b49-dcb1-4153-9d66-2e57b4dc57ad)

Processo Estocástico -> é uma coleção de variáveis aleatórias definidas num mesmo espaço de probabilidades (processo gerador de uma série de variáveis). A descrição de um 
processo estocástico é feita através de uma distribuição de probabilidade conjunta (o que é muito complexo de se fazer), então geralmente descrevemos ele por meio das funções:
- $𝜇(𝑡)=𝐸{𝑍(𝑡)}$ -> Média 
- $𝜎^2(𝑡)=𝑉𝑎𝑟{𝑍(𝑡)}$ -> Variância 
- $𝛾(𝑡1,𝑡2)=𝐶𝑜𝑣{𝑍(𝑡1),𝑍(𝑡2)}$ -> Autocovariância

![Captura de tela 2024-07-04 180109](https://github.com/HenrySchall/Time-Series/assets/96027335/7ffc0399-4f35-4e82-ac69-8950c083c8f4)

Estacionaridade -> é quando uma série temporal apresenta todas suas características estatísticas constante ao longo do tempo
- Estacionaridade Fraca = é quando as propriedades estatiaticas, são constantes no tempo, E(x)=U, Var(x) = 𝜎^2, COV(X,X-n) = k (corariância entre observações em diferentes pontos no tempo depende do tempo específico em que elas ocorreram). Na literatura, geralmente estacionalidade significa estacionalidade fraca.

- Estacionaridade Forte = também chamada de estrita, é quando a função de probabilidade conjunta é invariante no tempo, ou seja, as distribuições individuais são iguais para todos "ts". Com isso a covariância depende apenas da distância entre as observações e não do tempo especifico que ocorreram. 

![Imagem-2](https://github.com/HenrySchall/Time-Series/assets/96027335/6c237676-00e5-407f-bcc7-cddf6c1c4a34)

Passeio Aleatório (Random Walk) -> é a soma de pequenas flutuações estocásticas (tendência estocástica)
Matematicamente: $𝑍𝑡 = 𝑍(𝑡−1)+ et$

Autocorrelação -> é a correlação de determinados períodos anteriores com o período atual, ou seja, o grau de dependência serial. Cada período desse tipo de correlação é denominado lag (defasagem) e sua representação é feita pela Função de Autocorrelação (FAC) e a Função de Autocorrelação Parcial (FACP), ambas comparam o valor presente com os valores passados da série, a diferença entre eles é que a FAC analisa tanto a correlação direta como a indireta, já a FACP apenas correlação direta. Então podemos dizer, que a FAC vê a correlação direta do mês de janeiro em março e também a correlação indireta que o mês de janeiro teve em fevereiro que também teve em março, enquanto que a FACP apenas a correlação de janeiro em março. Essa análise é feita, porque é o pressuposto essencial para se criar previsões eficientes de uma série.

Ruído Branco (White Noise) -> é quando o erro de uma série temporal, segue uma distribuição normal, ou seja, um processo puramente aleatório. 
- $E(Xt) = 0$ 
- $Var(Xt) = 𝜎^2$

Transformação e Suavização -> São técnicas que buscam deixar a série o mais próximo possível de uma distribuição normal. Transformando o valor das varáveis ou suavizando a tendência e/ou sazonaliade da série. Dentre todas as técnicas existentes podemos citar:
1) Tranformação Log 
2) Tranformação Expoencial
3) Tranformação Box-Cox
4) Suavização Média Móvel Exponencial (MME) - Curto período 
5) Suavização por Média Móvel Simples (MMS) - Longo período

Diferenciação -> A diferenciação, busca transformar uma série não estacionária em estacionária, por meio da diferença de dois períodos consecutivos

#### Modelos das séries temporais univariados:
Modelos lineares:
 - Modelos autorregressivos (AR)
 - Modelos médias móveis (MA)
 - Modelos autorregressivos e médias móveis (ARMA)
 - Modelos autorregressivos integrados e de médias móveis (ARIMA)
 - Modelos de longas dependências temporais ou memória longa (ARFIMA)
 - Modelos autorregressivos integrados e de médias móveis com sazonalidade (SARIMA)
 
Modelos não lineares:
 - Autorregressivo com limiar (TAR)
 - Autorregressivo com transição suave (STAR)
 - Troca de regime markoviano (MSM)
 - Redes neurais artificiais autorregressivas (AR-ANN)

Estrutura: 
- Autorregressivo (AR): indica que a variável é regressada em seus valores anteriores. 
- Integrado (I): indica que os valores de dados foram substituídos com a diferença entre seus valores e os valores anteriores (diferenciação).
- Média móvel (MA): Indica que o erro de regressão é uma combinação linear dos termos de erro dos valores passados.

Codificação: (p, d, q) Parâmetro d só pode ser inteiro, caso estivessemos trabalhando com um Modelo ARFIMA, o parâmetro d pode ser fracionado

- p = ordem da autorregressão.
- d = grau de diferenciação.
- q = ordem da média móvel.

Quando adicionamos a sazonalidade, além da codificação Arima (p, d, q), incluimos a codificação para a Sazonalidade (P, D, Q). Então um modelo SARIMA é definido por: (p, d, q)(P, D, Q)

Exemplos:
- Modelo ARFIMA: (1, 0.25, 1) 
- Modelo ARIMA: (2, 1, 1)
- Modelo AR: (1, 0, 0)
- Modelo MA (0, 0, 3)
- Modelo I: (0, 2, 0)
- Modelo ARMA: (4, 0, 1)
- Modelo SARIMA: (1, 1, 2)(2, 0, 1)

#### Função de Autocorrelação (FAC) e Função de Autocorrelação Parcial (FACP)

#### Akaike’s Information Criterion (AIC) e o Bayesian Information Criterion (BIC)
Nos modelos mais avançados, as funções de autocorrelação e autocorrelação parcial não são informativas para definir a ordem dos modelos, por isso usasse um critério de informação. Um critério de informação é uma forma de encontrar o número ideal de parâmetros de um modelo, para entendê-lo, tenha em mente que, a cada regressor adicional, a soma dos resíduos não vai aumentar; frequentemente, diminuirá. A redução se dá à custa de mais regressores. Para balancear a redução dos erros e o aumento do número de regressores, o critério de informação associa uma penalidade a esse aumento. Sendo assim, sua equação apresenta duas partes: a primeira mede a qualidade do ajuste do modelo aos dados, enquanto a segunda parte é chamada de função de penalização dado que penaliza modelos com muitos parâmetros, sendo assim, dado todas as combinações de modelos procuramos aquele que apresenta menor AIC.

#### Testes Estatísticos

##### Teste de Kolmogorov-Smirnov
> Qualifica a máxima diferença absoluta entre a função de distribuição da amostra e a função de distribuição acumulada da distribuição de referência (geramente distribuição normal), ou seja, ele qualifica distância entre duas amostras (comparação entre elas).

- *H0: A amostra segue a distribuição de referência*
- *H1: A amostra não segue a distribuição de referência*

##### Teste de Anderson-Darling 
> Testa se uma função de distribuição acumulada f(x), pode ser candidata a ser um função de distribuição acumulada de uma amostra aleatória;

- *H0: A amostra tem distribuição de f(x)*
- *H1: A amostra não tem distribuição f(x)*

##### Teste de Shapiro Wilk 
> O teste Shapiro Wilk segue a seguinte equação descrita abaixo. Sendo que xi são os valores da amostra ordenados, no qual valores menores que W são evidências de que os dados são normais.

![Captura de tela 2024-07-04 191812](https://github.com/HenrySchall/Time-Series/assets/96027335/c9789639-2602-44bb-a9f3-491b92b65310)

> Já o termo b é determinado pela seguinte equação:

![Captura de tela 2024-07-04 192115](https://github.com/HenrySchall/Time-Series/assets/96027335/c2594f21-082f-4f6d-9293-66b45b0125fb)

> onde ai são constantes geradas pelas médias, variâncias e covariâncias das estatísticas de ordem de uma amostra de tamanho n de uma distribuição normal (tabela da normal).

Estatística de teste:
- *H0: A amostra segue uma distribuição normal (W-obtido < W-crítico)*
- *H1: A amostra não segue uma distribuição normal (W-obtido > W-crítico)*

![img46](https://github.com/HenrySchall/Time-Series/assets/96027335/64ca5aa1-d601-44b1-8d21-16ec79400211)

##### Teste de Jarque-Bera
> Verifica se os erros são um Ruído Branco, ou seja, seguem uma distribuição normal. O teste se baseia nos resíduos do método dos mínimos quadrados. Para sua realização o teste necessita dos cálculos da assimetria (skewness) e da curtose (kurtosis) da amostra, dado pela seguinte fórmula:
 
![Captura de tela 2024-07-04 193133](https://github.com/HenrySchall/Time-Series/assets/96027335/fe76cc80-fa40-46c8-8357-7e19e49339a5)

> onde n e o número de observações (ou graus de liberdade geral); S é aassimetria da amostra; e K é a curtose da amostra

![Captura de tela 2024-07-04 193243](https://github.com/HenrySchall/Time-Series/assets/96027335/b24d6ca3-6e20-44ed-a3d6-5004c3646bd6)

$\widehat{u3}$ e $\widehat{u4}$ são as estimativas do terceiro e quarto momentos, respectivamente; $\bar{x}$ a média da amostra, e $𝜎^2$ é a estimativa do segundo momento, a variância.

- *H0: resíduos são normalmente distribuídos*
- *H1: resíduos não são normalmente distribuídos*

#### Resumo:

|Teste|Quando usar|Prós|Contras|Cenários não indicados|
|---|---|---|---|---|
|Shapiro-Wilk|Pequenas amostras (sensível a pequenas desvios da normalidade)|Sensível a pequenas desvios da normalidade (adequado para amostras pequenas|Pode ser menos potente em amostras maiores|Dados com distribuição fortemente bimodal ou multimodal|
|Kolmogorov-Smirov|Amostras grandes (teste não paramétrico)|Não requer suposições sobre os parâmetros da distribuição (adequado para amostras grandes)|Menos sensível a pequenos desvios (menos potente em amostras pequenas)|Sensível a desvios nas caudas da distribuição|
|Anderson Darling|Verificação geral de normalidade|Sensibilidade a desvios em caudas e simetria (fornece estatística de teste e valores críticos)|Menos sensível a desvios pequenos|Não é recomendado para amostras muito pequenas|
|Jaque-Bera|Verificação geral de normalidade em amostras grandes|Combina informações sobre simetria e curtose (adequado para amostras grandes)|Menos sensível a desvios pequenos|Sensível a desvios nas caudas da distribuição| 
  
##### Teste de Aderência
> Este teste é utilizado quando deseja-se validar a hipótese que um conjunto de dados é gerado por uma determinada distribuição de probabilidade.

- *H0: segue o modelo proposto*
- *H1: não segue o modelo proposto*
  
##### Teste de Indepedência
> Este teste é utilizado quando deseja-se validar a hipótese de independência entre duas variáveis aleatórias. Se por exemplo, existe a funlçao de probabilidade conjunta das duas variáveis aleatórias, pode-se verificar se para todos os possíveis valores das variávies, o produto das probabilidades margianis é igual à probabilidade conjunto.

- *H0: as variáveis aleatórias são independentes*
- *H1: as variáveis aleatórias não são independentes*

##### Teste de Homogeneidade
> Esse teste é utilizado quando deseja-se validar a hipótese de que uma variável aleatória apresenta comportamento similar, ou homogêneo, em relação às suas várias subpopulações. Este teste apresenta a mesma mecânica do Teste de Independência, mas uma distinção importante se refere à forma como as amostras são coletadas. No Teste de homogeneidade fixa-se o tamanho da amostra em cada uma das subpopulações e, então, seleciona-se uma amostra de cada uma delas.

- *H0: As subpopulações das variáveis aleatórias são homogêneas*
- *H1: As subpopulações das variáveis aleatórias não são homogêneas*
  

#### Coeficientes de Correlação
> Os coeficientes de correlação verificam a existência e o grau de associação entre dois conjuntos de dados.

##### Coeficiente Pearson 
> Estabelecer o nível de relação linear entre duas variáveis. Em outras palavras, mede em grau e o sentido (crescente/decrescente) da associação linear entre duas variáveis. Ele sempre estará entre −1,00 e +1,00, tendo o sinal a função de indicar a direção do movimento, ou seja, positivo (relação direta) e negativa (relação inversa) e o valor do coeficiente, a função de indicar a força da correlação, onde nos intervalos:
> - (+0,90; +1,00) ou (−1,00; −0,90) = correlação muito forte
> - (+0,60; +0,90) ou (−0,90; −0,60) = correlação forte
> - (+0,30; +0,60) ou (−0,60; −0,30) = correlação moderada
> - (0,00; +0,30) ou (−0,30; 0,00) = correlação fraca
>
> Graficamente:

![3](https://github.com/HenrySchall/Time-Series/assets/96027335/5391579e-90f0-4ed2-92a0-b95c6068591f)

> Sua equação é definida pela seguinte fórmula:

![1](https://github.com/HenrySchall/Time-Series/assets/96027335/8f4dd7f6-e82b-4bf0-a06d-58400ede1060)

> Lembrando que o coeficiente de correlação populacional é dado por:

![2](https://github.com/HenrySchall/Time-Series/assets/96027335/6e39a2b7-4bfd-4d30-987e-bca3e8c5c8d8)

> Exemplo: A tabela abaixo apresenta 15 observações, com o tempo de entrega (em minutos) e a distância de entrega de um TelePizza.

|Tempo|Distância|
|---|---|
|40|688|
|21|215|
|14|255|
|20|462|
|24|448|
|29|776|
|15|200|
|19|132|
|10|36|
|35|770|
|18|140|
|52|810|
|19|450|
|20|635|
|11|150|

> Calculando os valores obtemos o seguinte resultado:

![4](https://github.com/HenrySchall/Time-Series/assets/96027335/a224016f-5d0a-4b84-ac79-6b8f5dae6ae1)

> Conclui-se que existe uma relação linear forte e positiva entre as variáveis. Todavia o coeficiente de correlação de Pearson é apenas uma estimativa do coeficiente de correlação populacional, pois é calculado com base em uma amostra aleatória de 𝑛 pares de dados. Sendo assim a amostra observada pode apresentar correlação, mas a população não, neste caso, tem-se um problema de inferência, pois o fato de r≠0 não é garantia de 𝜌≠0. Para resolver esse problema, utiliza-se da estatística de teste T-student, definido pela equação abaixo, para verificar se realmente existe correlação linear entre as variáveis:

![5](https://github.com/HenrySchall/Time-Series/assets/96027335/84310f44-b3d8-477d-9e71-1ec81dcbb21a)

> Onde 𝑡 segue uma distribuição 𝑡−𝑆𝑡𝑢𝑑𝑒𝑛𝑡 com 𝑛−2 graus de liberdade e regido pelas seguintes hipóteses:

- *H0: A correlação entre as variáveis é zero (𝜌 = 0)*
- *H1: A correlação entre as variáveis não é zero (𝜌 ≠ 0)*

![6](https://github.com/HenrySchall/Time-Series/assets/96027335/ccc5a428-cea3-4a8f-a773-c6b454b87f28)

> A partir da estatística 𝑡 com 13 graus de liberdade, os pontos críticos são ±2,1604. Portanto, rejeita-se 𝐻𝑜 ao nível de significância de 5%. Sendo assim a correlação entre o tempo de entrega e a distância percorrida é diferente de zero, então, existe uma relação linear e positiva entre as variáveis da ordem de 𝑟 = 0,8216.

##### Coeficiente Spearman
> O coeficiente de correlação de Spearman, ou rho de Spearman, é uma medida não paramétrica da correlação (associação) entre duas variáveis ordinais. Ao contrário do coeficiente de correlação de Pearson, que mede a força e a direção da relação linear entre duas variáveis, o coeficiente de Spearman avalia a intensidade (o quão bem) é a relação entre duas variáveis. O coeficiente de correlação de Spearman (𝜌) é calculado utilizando a seguinte fórmula:

![20](https://github.com/HenrySchall/Time-Series/assets/96027335/65f56f8e-31b3-4d4f-a4d0-b7e692b2fd44)

#### Interpretação:
- ρ=1 indica uma perfeita correlação positiva.
- ρ=−1 indica uma perfeita correlação negativa.
- ρ=0 indica ausência de correlação.

> Exemplo: Dados os valores da tabela abaixo:

![9](https://github.com/HenrySchall/Time-Series/assets/96027335/68db17b8-2b31-41c9-b1d1-cf241b30ee55)

> Calculando os valores obtemos o seguinte resultado:

![12](https://github.com/HenrySchall/Time-Series/assets/96027335/1c332788-5570-48e1-8d17-2b3b36c61aff)
 
> Utilizando-se da mesma equação estatística do teste T-student. Teremos as seguintes hipóteses:

- *H0: A correlação entre as variáveis é zero*
- *H1: A correlação entre as variáveis não é zero*

> A partir da estatística 𝑡−𝑆𝑡𝑢𝑑𝑒𝑛𝑡 com 11 graus de liberdade, os pontos críticos são ±2,2010. Portanto, rejeita-se 𝐻𝑜 ao nível de significância de 5%. Sendo assim a correlação entre as variáveis 𝑋 e 𝑌 é diferente 
de zero, então, existe uma relação não-linear e negativa de ordem 𝑟= −0,9698. 

##### Coeficiente Kendall 
> O coeficiente de correlação de Kendall é uma medida estatística utilizada para avaliar a associação entre duas variáveis ordinais, exatamente igual ao coeficiente de correlação de Spearman, a difenreça é que ele mede a correlação de concordância, enquanto Spearman, mede a correlação de postos. Sendo particularmente útil quando as variáveis em questão não assumem necessariamente distribuições normais. O coeficiente de correlação de Kendall (τ) é definido pela seguinte fórmula:

![124](https://github.com/HenrySchall/Time-Series/assets/96027335/ac68ba9a-1c0d-4cab-a892-7d9ab87cc400)

> No qual, 𝑛 é o número de elementos aos quais atribui-se postos, 𝑆 é a soma da variável 𝑌 à direita que são superiores menos o número de postos à direita que são inferiores.

#### Interpretação:
- τ=1 indica uma perfeita concordância.
- τ=−1 indica uma perfeita discordância.
- τ=0 indica ausência de associação entre as variáveis.

> Para o cálculo do coeficiente de correlação por postos de Kendall ordena-se inicialmente uma das variáveis em ordem crescente de postos e o S correspondente a cada elemento será obtido fazendo o número de elementos 
cujo posto é superior ao que se está calculando menos o número de elementos cujo posto é inferior ao mesmo. Para verificar a significância do valor observado do coeficiente 𝜏 de Kendall, para 𝑛≤10 deve-se consultar a tabela abaixo.

![125](https://github.com/HenrySchall/Time-Series/assets/96027335/9a2f16b5-e667-4d3c-a8dd-01d3ed678409)

> Para 𝑛>10, pode utilizar a estatística de teste:

![128](https://github.com/HenrySchall/Time-Series/assets/96027335/275d3eda-ef7e-453a-86d1-a4918ef935ff)

> Exemplo: Dados os valores da tabela abaixo:

![14](https://github.com/HenrySchall/Time-Series/assets/96027335/a886a3c7-1e07-429f-844f-782e88c480c7)

> Calculando os valores obtemos o seguinte resultado:

![17](https://github.com/HenrySchall/Time-Series/assets/96027335/aae35d85-d483-40ad-a41e-6261c2b36b97)

> Tendo as seguintes hipóteses:

- *H0: A correlação entre as variáveis é zero (𝜏=0)*
- *H1: A correlação entre as variáveis não é zero (𝜏≠0)*

>  A partir da estatística 𝑁𝑜𝑟𝑚𝑎𝑙 𝑝𝑎𝑑𝑟ã𝑜, os pontos críticos são ±1,96. Portanto, rejeita-se 𝐻𝑜 ao nível de significância de 5%. Sendo assim a correlação entre as variáveis 𝑋 e 𝑌 é diferente de zero, então, existe uma 
relação não-linear e negativa de ordem 𝜏=−0,7692.

*Observação: Pode-se fazer uma comparação entre coeficiente de correlação de Spearman e o coeficiente de correlação por postos de Kendall. Os valores numéricos não são iguais, quando calculados para os mesmos pares de postos, e não são comparáveis numericamente. Contudo, pelo fato de utilizarem a mesma quantidade de informação contida nos dados, ambos têm o mesmo poder de detectar a existência de associação na população, e rejeitarão a hipótese nula para um mesmo nível de significância.*








