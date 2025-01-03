# Investment Risk

### Taxa de Crescimento 
> Reflete o quanto estamos multiplicamos nosso capital sobre o valor da data de compra. Para calcularmos ela usaremos os valores dos ativos normalizados, ou seja, dividindo o preço de fechamento de cada dia, pelo preço inicial de compra.
 
### Taxa de Retorno Simples
> A taxa de retorno simples é uma métrica financeira utilizada para avaliar a rentabilidade de um investimento ao longo de um período de tempo específico, ela é utilizada quando se quer **comparar ações distintas**.

$RS = (pf + div) - pi/(pi) * 100$

- pf = Preço Final
- pi = Preço Inicial
- div = dividendos do período 

#### Exemplo: 

TOTS3
- pi = R$ 27,93
- qi = 100 (quantidade de compra)
- pf = R$ 35,73
- qf = 100 (quantidade de venda)
- div = 0,25 
- Corretagem = 10,0

> $100 * 27,93 = 2.793$ 
> 
> $100 * 35,73 = 3.573$
> 
> $100 * 0,25 = 25,00$
> 
> $Lucro = (3.573 + 25,00) - 2.793 - 10,0 = 795,00$
> 
> $RS = (3.573 + 25 - 10) - (2.793 + 10)/(2.793 + 10) * 100$ -> 28,0% 

### Taxa de Retorno Logaritmica
> Também conhecida como taxa de retorno contínuo. Assim como a taxa de retorno simples, ela avalia a rentabilidade de um investimento ao longo de um período de tempo específico, sendo utilizada quando se quer **comparar a mesma ações em períodos diferentes**.

$RL = log⁡(pf/pi)* 100$

- pf = Preço Final
- pi = Preço Inicial
- div = dividendos do período 

#### Exemplo: 

TOTS3
- pi = R$ 27,93
- qi = 100 (quantidade de compra)
- pf = R$ 35,73
- qf = 100 (quantidade de venda)
- div = 0,25 
- Corretagem = 10,0

> $100 * 27,93 = 2.793$ 
> 
> $100 * 35,73 = 3.573$
> 
> $100 * 0,25 = 25,00$
> 
> $Lucro = (3.573 + 25,00) - 2.793 - 10,0 = 795,00$
> 
> $RS = log(3.573 + 25 - 10)/(2.793 + 10) * 100$ -> 24,69% 

### Taxa de Retorno Carteira

Pesos de cada Ativo:
- TOTS3 = 0,5
- WEGE3 = 0,5

> $27,47 * 0,5$ -> 13,73%
> 
> $11,17 * 0,5$ -> 5,58% 

Retorno da Carteira = 13,73 + 5,58 -> 19,31%

#### Coeficiente de variação (CV) 
> Mede estatisticamente a dispersão relativa, risco por unidade de retorno. Quanto maior o CV, maior o risco. É muito útil na comparação dos riscos de ativos com retornos esperados diferentes

$CV = σ/RS$

- RS -> Retorno Esperado
- σ -> Desvio Padrão

![Captura de tela 2024-09-13 151633](https://github.com/user-attachments/assets/f8157733-2f1c-42e0-aeee-7fb28689b558)

### Risco 
> As decisões financeiras são tomadas em um ambiente de incerteza com relação ao futuro. Toda vez que uma situação de incerteza puder ser quantificada por meio de uma distribuição de probabilidades dos resultados possíveis, diz-se que a decisão está sendo tomada sob uma situação de risco. Aideia de risco está associada às probabilidades de determinado resultado ficar abaixo do valor esperado de uma variável.  Sendo assim, o risco é representado pela variabilidade dos valores observados em torno do valor esperado da distribuição, ou seja, da dispersão dos resultados em relação à média.

#### Comportamento em Relação ao Risco
-  Indiferente ao Risco: o retorno exigido não varia quando o nível de risco aumenta
-  Avesso ao Risco: o retorno exigido aumenta quando o risco se eleva. Exige um retorno mais elevado para compensar a elevação do risco.
-  Propenso ao Risco (risk lover): o retorno exigido cai quando o nível de risco aumenta. Está disposto a abrir mão de algum retorno para assumir maiores riscos.

#### Risco sistemático & Risco não sistemático

- Risco sistemático: É inerente e determinado por eventos externos à empresa, ou seja, mudança diária no preço das ações, devido a eventos como: recessão da economia, comportamento do cliente. **(Não pode ser eliminado e pode afetar todas as empresas)**
- Risco não sistemático: identificado nas características do próprio ativo (intrínseco), ou seja, eventos específicos da estrutura da empresa (depende do tipo de empresa).

#### Variância (σ²)
> Quantifica o quanto os retornos se diferem em relação a média dos retornos (variabilidade). É
obtida pelo somatório dos quadrados dos retornos subtraido pelo retorno médio esperado de cada ativo.

#### Covariância (σ)
> Medida não padronizada do grau de relacionamento de duas variáveis, ou seja, o grau de dispersão dos resultados em relação à média.
- Cov = + -> relação direta / mesma direção.
- Cov = - -> relação inversa / direção contrária.
- Cov = 0 -> nãohárelaçãoentreosdois retornos.

#### Correlação 
> Medida padronizada da relação entre duas séries de valores (retornos). Explica o grau / intensidade de relacionamento dessas séries (coeficiente de correlação).

- Correlação Positiva: duas séries variam na mesma direção.
- Correlação Negativa: duas séries variam em direções opostas

> Quanto menor for o valor da covariância / correlação, menor o grau de dependência das variáveis. A probabilidade de se reduzir o risco é aumentada com a combinação de ativos com covariância / correlação negativa

#### Índice de Treynor (IS)
> Indica o prêmio de risco esperado ou observado por unidade de risco, ou seja, para cada unidade de risco, tem-se x% de prêmio de risco. Sendo assim quanto maior, maior o prêmio de risco (melhor é).

$IS = Rn - Rf / σ$ 

- Rn = Retorno esperado do Ativo n
- Rf = Retorno esperado do Ativo Livre de Risco)
- σ =  Risco do ativo n

### Teoria do Portolio 
> Levando em conta a Hipótese dos Mercados Eficientes (HME), ou seja, aquela em que os preços refletem as informações disponíveis e apresentam grande sensibilidade a novas informações relevantes. O valor de um ativo é reflexo do consenso dos participantes com relação ao seu desempenho esperado, sendo assim, nenhum investidor é capaz de identificar ativos com preço em desequilíbrio e todos os investidores são racionais e, portanto,
têm aversão ao risco, optando sempre por investir em carteiras, e não em ativos individuais (diversificando parte do risco inerente à situação em que se coloca todo o dinheiro em um único ativo).
>  A teoria do Portfolio trata da composição de uma carteira ótimade ativos, tendo por objetivo maximizar a utilidade do investidor pela relação risco/retorno. Um único ativo, sofrerá todas as consequências de um mau
desempenho.Isso não ocorrerá com um investidor que aplicar em uma carteira diversificada de ativos

O objetivo do gestor financeiro é criar uma carteira eficiente,
que maximize o retorno para certo nível de risco ou minimize o
risco para determinado nível de retorno

![image](https://github.com/HenrySchall/Finance/assets/96027335/3af52f76-c600-46f1-9489-544b30fbfa77)


### CAPM (Capital Asset Pricing Model)
> É um modelo que determina uma taxa de retorno esperada, para um ativo ou de um portfólio de ativos, considerando um mercado em equilíbrio (perfeito), com o risco não diversificável (de mercado), via coeficiente beta ($\beta1$).

$Rn = Rf + \beta1 * (Rm - Rf)$

- Rn = Retorno esperado
- Rf = Risk Free (Ativo Livre de Risco)
- $\beta1$ = beta da empresa
- Rm = Risco de Mercado

> $\beta1$ É uma medida do risco sistemático de um ativo, isto é, a reação do retorno do ativo às reações na carteira de mercado. Determinado pela seguinte fórmula: 

$\beta = (Cov (Rn,Rm)/(σ^2 Rm)$

- $(Cov (Rn,Rm)$ -> Covariância dos retornos da ação com os retornos do mercado
- $(σ^2 Rm)$ -> Variância do mercado
  
Interpretação do Beta 
- B > 1 -> Agressivo
- B < 1 -> Defensivo
- B = 1 -> Neutro ou Beta do Mercado
- B < 0 -> Contrário ao Mercado
- B = 0 -> Ativo Livre de Risco
  
![foto_page-0001](https://github.com/HenrySchall/Finance/assets/96027335/6f11e3dd-7199-4cb8-902e-77f3fb7d54fc)

#### Índice de Sharpe (IT)
> Indica o prêmio de risco esperado ou observado por unidade de risco sistemático (medido pelo $\beta1$). Sendo assim quanto maior, maior o prêmio de risco, ou seja, melhor é.

$IS = Rn - Rf / \beta$ 

- Rn = Retorno esperado do Ativo n
- Rf = Retorno esperado do Ativo Livre de Risco)
- &\beta& =  Beta do ativo n

