https://rpubs.com/alberto-martuscelli/aula4_econometria2


### Modelo de Probabilidade Linear
O modelo de regressão linear

Yi=β0+β1X1i+β2X2i+⋯+βkXki+ui

com uma variável dependente binária Yi
 é chamado de modelo de probabilidade linear. No modelo de probabilidade linear temos

E(Y|X1,X2,…,Xk)=P(Y=1|X1,X2,…,X3)

onde,

PP(Y=1|X1,X2,…,Xk)=β0+β1+X1i+β2X2i+⋯+βkXki.

Assim, βj
 pode ser interpretado como a mudança na probabilidade tal que Yi=1
, mantendo constantes os outros k−1
 regressores constantes. Assim como na regressão múltipla comum, βj
pode ser estimado usando OLS e as fórmulas robustas de erro padrão podem ser usadas para testes de hipóteses e cálculo de intervalos de confiança.

Na maioria dos modelos de probabilidade linear, R2
 não tem interpretação significativa, uma veque a linha de regressão nunca pode ajustar os dados perfeitamente se a variável dependente for binária e os regressores forem contínuos. Isso pode ser visto no aplicativo abaixo.

É essencial usar erros padrão robustos, uma vez que em um modelo de probabilidade linear ui
 são sempre heterocedásticos.

Modelos de probabilidade linear são facilmente estimados em R usando a função lm()


O modelo de probabilidade linear tem uma grande falha: ele assume que a função de probabilidade condicional é linear. Isso não restringe P(Y=1|X1,…,Xk)
 a ficar entre 0
 e 1
. Podemos ver isso facilmente em nossa reprodução feita anteriormente: para P/I ratio≥1.75
, (1.2) prevê que a probabilidade de negação de um pedido de hipoteca seja maior que 1
. Para aplicações com Razão P/I
 próxima de 0
, a probabilidade prevista de negação é ainda negativa, de modo que o modelo não tem interpretação significativa aqui.

Esta circunstância exige uma abordagem que utilize uma função não linear para modelar a função de probabilidade condicional de uma variável dependente binária. Os métodos comumente usados são regressão Probit e Logit.

Probit
Na regressão Probit, a função de distribuição normal padrão cumulativa Φ(⋅)
 é usada para modelar a função de regressão quando a variável dependente é binária, ou seja, assumimos

E(Y|X)=P(Y=1|X)=Φ(β0+β1X).(11.4)

β0+β1X
 desempenha o papel de um quantil z
.

Lembre-se que

Φ(z)=P(Z≤z) , Z∼N(0,1)

tal que o coeficiente Probit β1
 em (11.4) é a mudança em z
 associada a uma mudança de uma unidade em X
 . Embora o efeito sobre z
 de uma mudança em X
 seja linear, a ligação entre z
 e a variável dependente Y
 é não linear, uma vez que Φ
 é uma função não linear de X
.

Como a variável dependente é uma função não linear dos regressores, o coeficiente em X
 não tem interpretação simples. De acordo com o Conceito Chave 8.1, a mudança esperada na probabilidade de Y=1
 devido a uma mudança na razão P/I pode ser calculada da seguinte forma:

Calcule a probabilidade prevista de que Y=1
 para o valor original de X
 .
Calcule a probabilidade prevista de que Y=1
 para X+ΔX
x’.
Calcule a diferença entre as duas probabilidades previstas.
É claro que podemos generalizar (11.4) para a regressão Probit com regressores múltiplos para mitigar o risco de enfrentar vieses de variáveisomitidas. Os fundamentos da regressão Probit estão resumidos no Conceito 2.

Conceito 2: Modelo Probit, Probabilidades Previstas e Efeitos Estimados
Suponha que Y seja uma variável binária. O modelo

Y=β0+β1+X1+β2X2+⋯+βkXk+u

com

P(Y=1|X1,X2,…,Xk)=Φ(β0+β1+X1+β2X2+⋯+βkXk)

é o modelo Probit populacional com múltiplos regressores X1,X2,…,XkeΦ(⋅)
 é a função de distribuição normal padrão cumulativa.

A probabilidade prevista de que Y=1
 dado X1,X2,…,Xk
 pode ser calculada em duas etapas:

Calcule z=β0+β1X1+β2X2+⋯+βkXk

Procure Φ(z)
 chamando pnorm() .

βj

Logit
O Conceito 3 resume a função de regressão Logit.

Definição 3: Regressão Logística
A função de regressão Logit populacional é

P(Y=1|X1,X2,…,Xk)==F(β0+β1X1+β2X2+⋯+βkXk)11+e−(β0+β1X1+β2X2+⋯+βkXk).

A ideia é semelhante à regressão Probit, exceto que um CDF diferente é usado:

F(x)=11+e−x

é o CDF de uma variável aleatória padrão distribuída logisticamente.

Quanto à regressão Probit, não existe uma interpretação simples dos coeficientes do modelo e é melhor considerar as probabilidades previstas ou diferenças nas probabilidades previstas. Aqui, novamente, estatísticas t e intervalos de confiança baseados em aproximações normais de grandes amostras podem ser calculados como de costume.

É bastante fácil estimar um modelo de regressão Logit usando R .
 é o efeito sobre $z$ de uma mudança de uma unidade no regressor Xj
 , mantendo constantes todos os outros k−1
 regressores.

O efeito na probabilidade prevista de uma mudança num regressor pode ser calculado como no Conceito Chave 8.1.

Em R , os modelos Probit podem ser estimados usando a função glm() do pacote stats . Usando a família de argumentos , especificamos que queremos usar uma função de ligação Probit.