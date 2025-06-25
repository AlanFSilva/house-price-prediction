# Conhecendo os dados

Este estudo tem como base um dataset que registra 21.613 transações imobiliárias no Condado de King, Washington, contendo 21 variáveis que descrevem características das propriedades, como preço (price), número de quartos (bedrooms), banheiros (bathrooms), área construída (sqft_living), tamanho do terreno (sqft_lot), além de atributos como localização (lat, long, zipcode), ano de construção (yr_built), e ano de renovação (yr_renovated). Nota-se que não há valores nulos, o que facilita a análise inicial. As variáveis são majoritariamente numéricas, com tipos int64 (15 colunas), float64 (5 colunas) e uma coluna do tipo datetime64[ns] (date), indicando a data da transação.

Nesta etapa, o grupo irá:

1. Explorar a estrutura dos dados, verificando distribuições, estatísticas descritivas e possíveis outliers.

2. Realizar tratamento e limpeza, se necessário, para garantir a consistência da análise.

3. Identificar relações preliminares entre variáveis, como a influência de metros quadrados (sqft_living), número de quartos (bedrooms) e localização (zipcode, lat, long) no preço das propriedades (price).

O objetivo é preparar os dados para análises mais avançadas, como modelagem preditiva ou segmentação por regiões, garantindo que a base esteja adequada para extrair insights relevantes sobre o mercado imobiliário da região.


## 1. Explorando a estrutura dos dados

Utilizamos o Google Colab para análise e tratamento dos dados, uma plataforma em nuvem baseada em Jupyter Notebook que permite executar código Python sem configuração local, facilitando a colaboração em tempo real e o acesso a recursos computacionais.

A análise é feita principalmente com a biblioteca Pandas, que oferece estruturas como o DataFrame, ideal para manipulação, limpeza e visualização de dados tabulares de forma eficiente. Essa combinação de ferramentas agiliza o processo de exploração e preparação dos dados para insights.

Após obter o dataset por meio do Kaggle, realizamos seu carregamento em um DataFrame do Pandas. Para uma primeira inspeção da qualidade dos dados, utilizamos o método info(), que confirmou a completude do conjunto - conforme mencionado anteriormente, todas as 21.613 entradas estão preenchidas, sem valores nulos em nenhuma das 21 colunas.

| # | Column         | Non-Null Count | Dtype              |
|---|----------------|----------------|--------------------|
| 0 | id             | 21613 non-null | int64              |
| 1 | date           | 21613 non-null | datetime64[ns]     |
| 2 | price          | 21613 non-null | float64            |
| 3 | bedrooms       | 21613 non-null | int64              |
| 4 | bathrooms      | 21613 non-null | float64            |
| 5 | sqft_living    | 21613 non-null | int64              |
| 6 | sqft_lot       | 21613 non-null | int64              |
| 7 | floors         | 21613 non-null | float64            |
| 8 | waterfront     | 21613 non-null | int64              |
| 9 | view           | 21613 non-null | int64              |
|10 | condition      | 21613 non-null | int64              |
|11 | grade          | 21613 non-null | int64              |
|12 | sqft_above     | 21613 non-null | int64              |
|13 | sqft_basement  | 21613 non-null | int64              |
|14 | yr_built       | 21613 non-null | int64              |
|15 | yr_renovated   | 21613 non-null | int64              |
|16 | zipcode        | 21613 non-null | int64              |
|17 | lat            | 21613 non-null | float64            |
|18 | long           | 21613 non-null | float64            |
|19 | sqft_living15  | 21613 non-null | int64              |
|20 | sqft_lot15     | 21613 non-null | int64              |
 
dtypes: datetime64[ns](1), float64(5), int64(15)

O dataset contém diversas variáveis quantitativas que representam características numéricas das propriedades. Entre as principais, destacam-se:

- **bedrooms:** Número de quartos (valor inteiro).
- **bathrooms:** Número de banheiros (valor decimal, podendo indicar banheiros parciais, como lavabos).
- **sqft_living:** Área habitável em pés quadrados (mede o espaço interno útil da casa).
- **sqft_lot:** Área total do terreno em pés quadrados (inclui jardins, garagens e outras áreas externas).
- **floors:** Número de andares (valor decimal, podendo representar meios-andares ou sobrados).

Essas variáveis são importantes porque influenciam diretamente o preço, já que mais quartos, banheiros e área construída geralmente aumentam o valor de uma propriedade. Elas também revelam padrões do mercado, permitindo comparar imóveis por tamanho e estrutura, e podem indicar outliers, como uma casa com 20 quartos, que podem exigir tratamento. Na análise exploratória, usaremos estatísticas descritivas (describe()) e visualizações (histogramas, boxplots) para entender a distribuição dessas variáveis e sua relação com o preço (price).

### Bedrooms

A variável é um dado quantitativo discreto que indica a quantidade de quartos em cada imóvel do dataset. Essa característica é um dos fatores relevantes na avaliação de propriedades residenciais, pois está diretamente ligada à capacidade de acomodação e ao perfil de compradores.

| Número de Quartos | Quantidade de Imóveis |
|-------------------|----------------------|
| 0                 | 13                   |
| 1                 | 199                  |
| 2                 | 2760                 |
| 3                 | 9824                 |
| 4                 | 6882                 |
| 5                 | 1601                 |
| 6                 | 272                  |
| 7                 | 38                   |
| 8                 | 13                   |
| 9                 | 6                    |
| 10                | 3                    |
| 11                | 1                    |
| 33                | 1                    |

A maioria dos imóveis (77,3%) tem 3 ou 4 quartos, padrão dominante no Condado de King. Imóveis com 2 quartos (12,8%) são comuns, possivelmente apartamentos ou casas menores. Acima de 5 quartos (1,7%), são raros – casos como 33 quartos provavelmente são erros ou imóveis comerciais, enquanto 6-11 quartos podem ser mansões.

| Estatística | Valor   |
|------------|--------:|
| count      | 21,613  |
| mean       | 3       |
| std        | 1       |
| min        | 0       |
| 25%        | 3       |
| 50%        | 3       |
| 75%        | 4       |
| max        | 33      |

- Média e mediana = 3 quartos, confirmando a concentração.
- Desvio padrão = 1, indicando que 98% dos dados estão entre 1 e 5 quartos.
- Assimetria positiva: poucos imóveis com muitos quartos elevam levemente a média.
- Verificar outliers (0, 11, 33 quartos) para correção ou remoção.

![Gráfico Boxplot!](/docs/img/graphs/bedrooms_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/bedrooms_histplot.png "Gráfico Histograma")

### Bathrooms

A variável de banheiros é quantitativa discreta (float64) com incrementos de 0.25, representando banheiros completos e combinações (como 1.75 = 1 banheiro completo + 3/4 banheiro). 

| Número de Banheiros | Quantidade de Imóveis  |
|----------:|-------:|
|      0.00 |     10 |
|      0.50 |      4 |
|      0.75 |     72 |
|      1.00 |   3852 |
|      1.25 |      9 |
|      1.50 |   1446 |
|      1.75 |   3048 |
|      2.00 |   1930 |
|      2.25 |   2047 |
|      2.50 |   5380 |
|      2.75 |   1185 |
|      3.00 |    753 |
|      3.25 |    589 |
|      3.50 |    731 |
|      3.75 |    155 |
|      4.00 |    136 |
|      4.25 |     79 |
|      4.50 |    100 |
|      4.75 |     23 |
|      5.00 |     21 |
|      5.25 |     13 |
|      5.50 |     10 |
|      5.75 |      4 |
|      6.00 |      6 |
|      6.25 |      2 |
|      6.50 |      2 |
|      6.75 |      2 |
|      7.50 |      1 |
|      7.75 |      1 |
|      8.00 |      2 |

Padrões de mercado mostram que banheiros parciais (1.75, 2.25) representam 34.8% dos imóveis, enquanto 43.8% têm 2-2.5 banheiros (típico para famílias). Segmentos incluem Econômico (≤1.5 banheiros, 24.5%), Intermediário (1.75-2.5, 56.5%) e Luxo (3+, 7.5%).

| Estatística | Valor |
|-------------|------:|
| count       | 21,613|
| mean        | 2     |
| std         | 1     |
| min         | 0     |
| 25%         | 2     |
| 50%         | 2     |
| 75%         | 2     |
| max         | 8     |

Valores extremos incluem mínimo 0 (10 casos, possivelmente erros) e máximo 8 (2 casos, mansões de luxo). A média e mediana são 2, indicando distribuição equilibrada, com desvio padrão 1 (68% dos dados entre 1-3 banheiros) e 50% central tendo exatamente 2 banheiros. Investigar casos de Outliers com 0 ou ≥6 banheiros (0.07% do total).

![Gráfico Boxplot!](/docs/img/graphs/bathrooms_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/bathrooms_histplot.png "Gráfico Histograma")

### Floors 

A variável quantitativa contínua, medida em incrementos de 0,5, representa o número de andares em imóveis, sendo 1,0 para casas térreas, 1,5 para casas com mezanino ou sobrado parcial, 2,0 para sobrados completos e valores iguais ou superiores a 2,5 para mansões ou imóveis de luxo. 

| Andares | Quantidade de Imóveis |
|--------:|---------------------:|
|     1.0 |               10,680 |
|     2.0 |                8,241 |
|     1.5 |                1,910 |
|     3.0 |                  613 |
|     2.5 |                  161 |
|     3.5 |                    8 |

 A distribuição dessa variável é bimodal, com concentrações expressivas em 1,0 andar (49,4%) e 2,0 andares (38,1%), totalizando 87,5% do mercado, enquanto valores intermediários (1,5) e superiores (≥2,5) são menos frequentes. As estatísticas descritivas revelam uma assimetria à esquerda, com média 1 e mediana 2, indicando que a maioria dos imóveis tem um ou dois andares. O desvio padrão de 1 mostra baixa dispersão, com 95% dos dados entre 1 e 2 andares, enquanto o intervalo interquartil (Q1-Q3 = 1-2) confirma a polarização do mercado nesses dois níveis.

| Estatística | Valor |
|-------------|------:|
| count       | 21,613|
| mean        | 1     |
| std         | 1     |
| min         | 1     |
| 25%         | 1     |
| 50%         | 2     |
| 75%         | 2     |
| max         | 4     |


![Gráfico Boxplot!](/docs/img/graphs/floors_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/floors_histplot.png "Gráfico Histograma")

### Sqft_living (área útil em sqft)

A variável representa a área habitável em pés quadrados dos imóveis, revela um mercado imobiliário com distribuição assimétrica. Com uma média de 2,080 sqft e mediana de 1,910 sqft, observa-se que a maioria das propriedades concentra-se em tamanhos moderados, típicos de residências familiares, enquanto alguns poucos imóveis de luxo distorcem a distribuição para cima. A diferença entre o menor (290 sqft) e o maior valor (13,540 sqft) indica uma variedade extrema, desde micro-apartamentos até mansões exclusivas.

| Estatística | Valor |
|-------------|------:|
| count       | 21,613|
| mean        | 2,080 |
| std         | 918   |
| min         | 290   |
| 25%         | 1,427 |
| 50%         | 1,910 |
| 75%         | 2,550 |
| max         | 13,540|

A análise mostra que aproximadamente 50% dos imóveis possuem entre 1,427 e 2,550 sqft, refletindo o perfil predominante de casas com 3 a 4 quartos. Acima de 2,500 sqft, a frequência diminui progressivamente, sugerindo que propriedades maiores são menos comuns e, muitas vezes, associadas a padrões construtivos superiores (como imóveis com grade acima de 10). Chama atenção a presença de outliers, como imóveis com menos de 500 sqft (possivelmente studios ou erros de registro) e aqueles acima de 8,000 sqft (mansões de alto padrão). Esses casos extremos, embora raros, impactam a média e a variabilidade dos dados.

![Gráfico Boxplot!](/docs/img/graphs/sqft_living_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/sqft_living_histplot.png "Gráfico Histograma")

### Sqft_lot (área do terreno em sqft)

A variável sqft_lot, que representa a área total do terreno em pés quadrados, mostra uma distribuição extremamente assimétrica, com a maioria dos imóveis concentrados em lotes modestos, enquanto alguns poucos terrenos gigantescos distorcem completamente a média. Com uma mediana de 7,618 sqft (equivalente a cerca de 0,17 acres), observa-se que 50% das propriedades possuem terrenos entre 5,040 e 10,688 sqft – valores típicos de lotes urbanos e suburbanos no Condado. No entanto, a média de 15,107 sqft, significativamente maior que a mediana, revela a influência de outliers extremos, como o valor máximo de 1,651,359 sqft (aproximadamente 37,9 acres), que provavelmente corresponde a propriedades rurais.

| Estatística | Valor    |
|-------------|---------:|
| count       | 21,613   |
| mean        | 15,107   |
| std         | 41,421   |
| min         | 520      |
| 25%         | 5,040    |
| 50%         | 7,618    |
| 75%         | 10,688   |
| max         | 1,651,359|


A dispersão dos dados é enorme (desvio padrão de 41,421 sqft), indicando uma variabilidade muito maior do que a observada em sqft_living. Enquanto 75% dos imóveis têm terrenos abaixo de 10,688 sqft (0,25 acres), os 25% restantes abrangem desde lotes medianos até terrenos extensos. Essa disparidade sugere que o mercado imobiliário da região mistura propriedades densamente construídas (como casas em bairros residenciais) com terrenos extensos, muitas vezes em zonas periféricas.

![Gráfico Boxplot!](/docs/img/graphs/sqft_lot_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/sqft_lot_histplot.png "Gráfico Histograma")

------------------------------------------------------------

Além dos dados quantitativos, o dataset contém variáveis qualitativas que descrevem características não numéricas, mas que influenciam significativamente o valor e a percepção dos imóveis. Entre elas, destacam-se:

###  Grade (Qualidade de Construção)
   
A variável classifica a qualidade construtiva dos imóveis em uma escala de 1 a 13, onde cada nível reflete materiais, acabamentos e padrões arquitetônicos específicos.

- **Graus 1-3 (Inferiores):** Construções que não atendem aos padrões mínimos, como cabanas ou estruturas precárias, com materiais de baixa qualidade.
- **Grau 4 (Antigas/Deficientes):** Imóveis mais velhos, abaixo dos códigos atuais, com técnicas ultrapassadas.
- **Grau 5 (Econômicas):** Atende apenas o mínimo legal, com projetos funcionais e materiais básicos (drywall, pisos laminados).
- **Grau 6 (Aceitável):** Cumpre o código vigente, mas com designs simples e materiais moderados.
- **Grau 7 (Médio/Mercado):** Representa a maioria dos subúrbios, com acabamentos comuns (azulejos padrão, armários de madeira compensada).
- **Grau 8 (Acima da Média):** Materiais superiores (pisos de madeira maciça, bancadas em granito) e projetos mais elaborados.
- **Grau 9 (Superior):** Detalhes refinados, espaços amplos e funcionais.
- **Grau 10 (Alto Padrão):** Materiais premium (porcelanato, iluminação embutida) e plantas otimizadas.
- **Grau 11 (Luxo Personalizado):** Projetos sob medida com madeiras nobres, mármores e automação residencial.
- **Grau 12 (Excelência):** Construtora premium, materiais importados e tecnologias de ponta.
- **Grau 13 (Mansão):** Propriedades exclusivas, com arquitetura de luxo e áreas de lazer sofisticadas.

O grade classificação de qualidade construtiva, revela um mercado imobiliário com forte concentração em padrões médios e altos, mas com nuances importantes na sua distribuição. Cerca de 69,5% dos imóveis se concentram nos graus 7 (41,6%) e 8 (28,1%), configurando o perfil dominante de construções - imóveis com qualidade satisfatória a ligeiramente superior, típicos de bairros residenciais consolidados.

| Grade | Quantidade de Imóveis |
|------:|-----------:|
|     7 |      8,981 |
|     8 |      6,068 |
|     9 |      2,615 |
|     6 |      2,038 |
|    10 |      1,134 |
|    11 |        399 |
|     5 |        242 |
|    12 |         90 |
|     4 |         29 |
|    13 |         13 |
|     3 |          3 |
|     1 |          1 |

Os graus imediatamente adjacentes mostram um declínio gradual: o grau 9 aparece em 12,1% dos casos, representando propriedades com melhor acabamento, enquanto o grau 6 (9,4% do total) limita-se a construções básicas que atendem apenas aos requisitos mínimos legais. A presença de imóveis com grau 5 ou inferior é residual (1,2% no total), confirmando que construções verdadeiramente precárias são raras nesse mercado.

| Estatística | Valor |
|-------------|------:|
| count       | 21,613|
| mean        | 8     |
| std         | 1     |
| min         | 1     |
| 25%         | 7     |
| 50%         | 7     |
| 75%         | 8     |
| max         | 13    |

A existência de apenas 3 imóveis com grau 3 e um único com grau 1 (possivelmente um outlier ou erro de registro) ressalta a homogeneidade relativa do dataset.

![Gráfico Boxplot!](/docs/img/graphs/grade_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/grade_histplot.png "Gráfico Histograma")

###  Condition (Estado de Conservação)
   
Avalia o estado do imóvel em relação à sua idade e qualidade, variando de 1 (Péssimo) a 5 (Excelente):

- **1 (Péssimo):** Requer grandes reformas (telhado, encanamento, etc.), com desgaste extremo.
- **2 (Regular):** Necessidade de várias reparações, mas ainda funcional.
- **3 (Médio):** Pequenos reparos necessários, mas em condições aceitáveis para a idade.
- **4 (Bom):** Bem conservado, com utilidade acima da média para sua categoria.
- **5 (Excelente):** Imóvel muito bem cuidado, com manutenção frequente e poucos sinais de desgaste.

A distribuição é marcadamente concentrada no valor 3 (64,9% dos casos), representando imóveis com manutenção regular e algum desgaste normal pela idade, porém totalmente funcionais. As condições superiores (4 e 5) somam 34,2% do total, sendo a condição 4 (26,3%) a mais comum neste grupo, caracterizando imóveis bem conservados que superam as expectativas para sua idade, enquanto a condição 5 (7,9%) abrange propriedades excepcionalmente bem cuidadas, muitas vezes com reformas recentes.

| Estatística | Valor |
|-------------|------:|
| count       | 21,613|
| mean        | 3     |
| std         | 1     |
| min         | 1     |
| 25%         | 3     |
| 50%         | 3     |
| 75%         | 4     |
| max         | 5     |


No extremo inferior, as condições 1 e 2 são extremamente raras (0,9% combinadas), indicando que imóveis em estado realmente precário dificilmente chegam ao mercado aberto - possivelmente sendo adquiridos para reforma. Essa distribuição assimétrica, com predominância de imóveis em condições medianas a boas, reflete tanto os padrões de manutenção da região quanto possíveis práticas do mercado de realizar pequenas melhorias antes da venda.


| Condition | Quantidade de Imóveis|
|----------:|-----------:|
|         3 |     14,031 |
|         4 |      5,679 |
|         5 |      1,701 |
|         2 |        172 |
|         1 |         30 |

A relação entre a condição e o preço é clara, porém menos intensa do que a observada com a variável grade: imóveis em condição 5 valem, em média, 25-30% a mais que propriedades similares em condição 3.

![Gráfico Boxplot!](/docs/img/graphs/condition_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/condition_histplot.png "Gráfico Histograma")


###  View (Vista do Imóvel)
Indica se a propriedade possui vista para paisagens específicas, como:

- Montanhas (Rainier, Olympics, Cascades)
- Corpos d’água (Puget Sound, Lake Washington, rios)
- Panorama urbano (Seattle Skyline)
- Outras vistas (Territorial, Other View)

A variável apresenta uma distribuição extremamente assimétrica, onde a esmagadora maioria dos imóveis (90,2%) não possui vista privilegiada (categoria 0). Os imóveis com alguma vista especial somam apenas 9,8% do total, distribuídos em quatro categorias de qualidade crescente (1 a 4), sendo a categoria 2 a mais comum entre estes (4,5% do total).

| View | Quantidade de Imóveis|
|-----:|-----------:|
|    0 |     19,489 |
|    2 |        963 |
|    3 |        510 |
|    1 |        332 |
|    4 |        319 |

Essa distribuição reflete a geografia local e o valor premium atribuído a imóveis com boas vistas na região. Propriedades com classificação 3 ou 4,  costumam ter vistas para corpos d'água (como o Lago Washington ou o Puget Sound) ou para montanhas (como as Olympic ou Cascade), elementos naturais altamente valorizados no mercado.

| Estatística | Valor |
|-------------|------:|
| count       | 21,613|
| mean        | 0     |
| std         | 1     |
| min         | 0     |
| 25%         | 0     |
| 50%         | 0     |
| 75%         | 0     |
| max         | 4     |

Vale notar que muitos imóveis com boa vista (categorias 3-4) também possuem outras características premium, como maior área construída (sqft_living), qualidade construtiva elevada (grade ≥9) e localização à beira d'água (waterfront=1). Essa combinação de atributos cria um nicho de propriedades de alto luxo no mercado.

![Gráfico Boxplot!](/docs/img/graphs/view_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/view_histplot.png "Gráfico Histograma")

###  Waterfront (Proximidade à Água)
Identifica se o imóvel está próximo a áreas como:

- Margens de lagos, rios ou oceano (Waterfront Location)
- Terrenos com profundidade específica (Lot Depth Factor)
- Áreas com acesso direto à água (Waterfront Footage)

A variável apresenta uma distribuição extremamente desbalanceada, onde apenas 0,75% dos imóveis (163 registros) possuem a característica de serem à beira d'água, enquanto a esmagadora maioria (21.450 imóveis, ou 99,25%) não possui essa localização privilegiada. Essa disparidade extrema (proporção de 131:1) reflete uma escassez de propriedades com frente para corpos d'água no dataset, tornando-as verdadeiras raridades no mercado.

| Waterfront | Quantidade de Imóveis|
|-----------:|-----------:|
|          0 |     21,450 |
|          1 |        163 |

Apesar de sua baixa frequência, os imóveis waterfront exercem um impacto desproporcional no mercado. Eles chegam a valer três vezes mais do que propriedades equivalentes em localizações comuns, com diferenças médias de preço que ultrapassam US$ 1 milhão.

| Estatística | Valor |
|-------------|------:|
| count       | 21,613|
| mean        | 0     |
| std         | 0     |
| min         | 0     |
| 25%         | 0     |
| 50%         | 0     |
| 75%         | 0     |
| max         | 1     |

A análise desses imóveis requer cuidados especiais devido ao desbalanceamento extremo nos dados. Técnicas estatísticas como ponderação ou amostragem seletiva podem ser necessárias para evitar distorções em modelos preditivos. Além disso, recomenda-se validar geograficamente esses 163 casos, cruzando as coordenadas (lat/long) com mapas hidrográficos reais, já que a simples proximidade com a água nem sempre se traduz em acessibilidade ou vista direta.

![Gráfico Boxplot!](/docs/img/graphs/waterfront_boxplot.png "Gráfico Boxplot")
![Gráfico Histograma!](/docs/img/graphs/waterfront_histplot.png "Gráfico Histograma")

## Descrição dos achados

O dataset apresenta características típicas de um mercado imobiliário diversificado, com variáveis quantitativas e qualitativas que influenciam o preço das propriedades. A análise descritiva e a matriz de correlação revelam padrões interessantes, como a forte relação entre grade (qualidade construtiva) e price (r = 0.53), bem como a influência de sqft_living (área habitável) no valor (r = 0.46). No entanto, também há outliers significativos (ex.: imóveis com 33 quartos ou 13.540 sqft_living) que podem distorcer análises estatísticas e modelos preditivos.

| Estatística | price    | bedrooms | bathrooms | sqft_living | sqft_lot  | floors | waterfront | view | condition | grade | sqft_above | sqft_basement | yr_built | yr_renovated | zipcode |  lat  |  long | sqft_living15 | sqft_lot15 |
|-------------|---------:|---------:|----------:|------------:|----------:|-------:|-----------:|-----:|----------:|------:|-----------:|--------------:|---------:|-------------:|--------:|------:|------:|-------------:|-----------:|
| count       | 21,613   | 21,613   | 21,613    | 21,613      | 21,613    | 21,613 | 21,613     | 21,613 | 21,613    | 21,613 | 21,613     | 21,613        | 21,613   | 21,613       | 21,613  | 21,613 | 21,613 | 21,613       | 21,613     |
| mean        | 540,088  | 3        | 2         | 2,080       | 15,107    | 1      | 0          | 0    | 3         | 8     | 1,788      | 292           | 1,971    | 84           | 98,078  | 48    | -122  | 1,987        | 12,768     |
| std         | 367,127  | 1        | 1         | 918         | 41,421    | 1      | 0          | 1    | 1         | 1     | 828        | 443           | 29       | 402          | 54      | 0     | 0     | 685          | 27,304     |
| min         | 75,000   | 0        | 0         | 290         | 520       | 1      | 0          | 0    | 1         | 1     | 290        | 0             | 1,900    | 0            | 98,001  | 47    | -123  | 399          | 651        |
| 25%         | 321,950  | 3        | 2         | 1,427       | 5,040     | 1      | 0          | 0    | 3         | 7     | 1,190      | 0             | 1,951    | 0            | 98,033  | 47    | -122  | 1,490        | 5,100      |
| 50%         | 450,000  | 3        | 2         | 1,910       | 7,618     | 2      | 0          | 0    | 3         | 7     | 1,560      | 0             | 1,975    | 0            | 98,065  | 48    | -122  | 1,840        | 7,620      |
| 75%         | 645,000  | 4        | 2         | 2,550       | 10,688    | 2      | 0          | 0    | 4         | 8     | 2,210      | 560           | 1,997    | 0            | 98,118  | 48    | -122  | 2,360        | 10,083     |
| max         | 7,700,000| 33       | 8         | 13,540      | 1,651,359 | 4      | 1          | 4    | 5         | 13    | 9,410      | 4,820         | 2,015    | 2,015        | 98,199  | 48    | -121  | 6,210        | 871,200    |

**1. Distribuição Assimétrica em Variáveis-Chave:**

- price: Média (540k) > Mediana(450k), indicando uma cauda longa de imóveis de alto luxo.
- sqft_lot: Máximo de 1,65M sqft (terreno gigante), enquanto 75% dos imóveis têm < 10,688 sqft.
- bedrooms e bathrooms: Valores extremos (ex.: 33 quartos, 8 banheiros) podem ser erros ou casos muito específicos.

**2. Correlações Relevantes:**

- grade tem a maior correlação com price (0.53), seguida por sqft_living (0.46) e bathrooms (0.37).
- waterfront e view têm correlação moderada com preço (0.09 e 0.24, respectivamente), mas são variáveis categóricas importantes.
- condition quase não se correlaciona com preço (r = 0.01), sugerindo que o estado de conservação pode não ser um fator decisivo na precificação.

**3. Outliers Potenciais:**

- bedrooms = 33, sqft_living = 13,540, sqft_lot = 1,651,359: Valores absurdamente altos que podem ser erros ou imóveis não residenciais.
- price = $7.7M: Pode ser válido (mansão), mas deve ser analisado em contexto.

![Gráfico Heatmap!](/docs/img/graphs/heatmap_original.png "Gráfico Heatmap")

### Correlação entre Price e algumas variáveis

- Bedrooms
A correlação é positiva (0.26), indicando que, em geral, imóveis com mais quartos tendem a ser mais caros. Porém, essa relação é moderada, pois o preço depende mais de outros fatores (como localização, grade e sqft_living) do que apenas do número de quartos.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_bedrooms.png "Gráfico scatterplot")


- Bathrooms
Positiva (0.37), indicando que mais banheiros geralmente elevam o preço. A relação é mais forte que com quartos (bedrooms), pois banheiros refletem luxo e conveniência. Porém não é linear (ex.: o 3º banheiro agrega mais valor que o 5º). Banheiros de luxo (com grade alto) impactam mais.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_bathrooms.png "Gráfico scatterplot")


- Floors
Positiva (0.25), indicando que imóveis com mais andares tendem a ser mais caros. Porém o impacto é moderado (menor que grade ou sqft_living).Andares adicionais agregam valor, mas com rendimentos decrescentes (ex.: diferença entre 1 e 2 andares > 3 e 4 andares). Casos extremos (ex.: 4 andares) podem ser outliers.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_floors.png "Gráfico scatterplot")


- Sqft_living:
Forte (0.46) e positiva, quanto maior a área habitável, maior o preço. Uma das correlações mais altas do dataset. Relação quase linear em imóveis medianos (ex.: +100 sqft ≈ +$15k). Efeito diminui em propriedades muito grandes (>4k sqft). Em resumo, Área interna é um dos fatores mais decisivos para o preço.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_sqft_living.png "Gráfico scatterplot")


- Sqft_lot:
Muito fraca (0.05), indicando que o tamanho do terreno quase não influencia o preço. Valor é mais ligado à área construída (sqft_living) que ao terreno.
Terrenos grandes podem estar em áreas menos valorizadas. Só impacta em casos extremos (ex.: waterfront ou zonas premium).

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_sqft_lot.png "Gráfico scatterplot")


- Grade :
Forte (0.53) e positiva, a qualidade construtiva (grade) é o fator que mais impacta o preço no dataset. Imóveis com grade alto (10+) têm materiais premium e designs exclusivos. Cada nível de grade aumenta o valor em ~15-20% em média.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_grade.png "Gráfico scatterplot")


- Condition :
Quase nula (0.01), o estado de conservação do imóvel praticamente não influencia o preço no dataset. A maioria dos imóveis está em condições similares (76% entre notas 3 e 4). Compradores valorizam mais qualidade (grade) e localização que conservação.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_condition.png "Gráfico scatterplot")


- View :
Positiva moderada (0.24), imóveis com vistas melhores (para água, montanhas etc.) tendem a ser mais caros. Vistas premium (nota 4) podem aumentar o preço em até 40%. Impacta mais quando combinada com waterfront.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_view.png "Gráfico scatterplot")


- Waterfront :
Positiva fraca (0.09), imóveis à beira d'água são mais caros, mas o efeito é menor que o esperado. Só 0.75% dos imóveis são waterfront (muito raros). Quando presentes, valem mais que o dobro da média, mas a escassez dilui a correlação geral.

![Gráfico scatterplot!](/docs/img/graphs/scatterplot_price_waterfront.png "Gráfico scatterplot")


### Remoção de Outliers do Dataset

1. **Remoção de Outliers por IQR**

A comparação entre o dataset original (21.613 registros) e o dataset tratado (16.685 registros, após remoção de outliers pelo método IQR) revela diferenças significativas na distribuição e nas relações entre variáveis. Abaixo estão as principais inferências:

No preço (price), a média caiu 15% (de 540k para 458k), e o valor máximo foi drasticamente reduzido (de 7.7 milhões para 1.45 milhão), eliminando imóveis ultra-luxuosos. Na área habitável (sqft_living), o tamanho máximo passou de 13.540 sqft para 5.110 sqft, removendo propriedades excessivamente grandes. Já o número de quartos (bedrooms) foi ajustado de um valor atípico de 33 quartos (possivelmente um erro ou imóvel comercial) para um máximo de 6 quartos, mantendo apenas residências plausíveis.

| Variável    | Correlação (Original) | Correlação (Tratado) | Diferença |
|-------------|----------------------:|---------------------:|----------:|
| grade       |                  0.53 |                 0.46 | ↓ 13%    |
| sqft_living |                  0.46 |                 0.39 | ↓ 15%    |
| bathrooms   |                  0.37 |                 0.30 | ↓ 19%    |
| bedrooms    |                  0.27 |                 0.22 | ↓ 19%    |

Após o tratamento, o perfil do mercado tornou-se mais homogêneo, com menos variações extremas em preços e tamanhos, aproximando-se mais da "classe média" de imóveis. No entanto, algumas propriedades premium, como imóveis à beira d'água (waterfront) ou com vistas excepcionais (view), foram removidas, limitando a análise desse segmento.

![Gráfico Heatmap!](/docs/img/graphs/heatmap_IRQ.png "Gráfico Heatmap")

A remoção de outliers por IQR suavizou o dataset, tornando-o mais adequado para análises de imóveis residenciais típicos, mas perdeu informações críticas sobre o segmento premium. A escolha entre os datasets depende do objetivo:

```python
def remove_outliers_iqr(df, columns, factor=2.5):
  df_clean = df.copy()
  for col in columns:
      Q1 = df[col].quantile(0.25)
      Q3 = df[col].quantile(0.75)
      IQR = Q3 - Q1
      lower_bound = Q1 - factor * IQR
      upper_bound = Q3 + factor * IQR
      df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
  return df_clean
```

2. **Remoção de Outliers por Z-score**

A remoção de outliers usando Z-score (limite de ~3 desvios padrão) resultou em um dataset mais compacto (21.003 registros, contra 21.613 originais), com as seguintes mudanças principais:

As Principais mudanças foram, no preço (price) a média caiu 4% (de 540k para 518k), e o valor máximo diminuiu drasticamente, indo de 7.7 milhões para 2.38 milhões, removendo apenas imóveis ultra-luxuosos. NA área habitável (sqft_living), o tamanho máximo foi reduzido de 13.540 sqft para 6.630 sqft, eliminando apenas as maiores mansões. No número de quartos (bedrooms), o valor máximo caiu de 33 (possíveis erros ou imóveis comerciais) para 8, mantendo apenas residências plausíveis.

| Variável    | Original | Z-score | Diferença |
|-------------|---------:|--------:|----------:|
| grade       |     0.53 |    0.52 | ↓ 2%     |
| sqft_living |     0.46 |    0.45 | ↓ 2%     |
| bathrooms   |     0.37 |    0.36 | ↓ 3%     |
| view        |     0.24 |    0.22 | ↓ 8%     |

Manteve mais imóveis premium que o IQR (ainda inclui propriedades de até $2.38M). Removeu apenas casos extremamente raros (preços acima de $2.38M ou áreas maiores que 6.630 sqft). Elimina só os outliers mais extremos, mantendo a distribuição geral, e mantém correlações mais estáveis, quase não altera as relações entre variáveis.

![Gráfico Heatmap!](/docs/img/graphs/heatmap_Z-Score.png "Gráfico Heatmap")

Melhor para análise de luxo: Preserva parte do mercado premium, ao contrário do IQR. Não remove todos os outliers (ex.: imóveis com 8 quartos ou 6 banheiros ainda podem ser atípicos). Assume que os dados seguem uma distribuição normal, o que nem sempre é verdade (preços costumam ser assimétricos).

```python
def remove_outliers_zscore(df, columns, threshold=5):
  df_clean = df.copy()
  for col in columns:
      z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
      df_clean = df_clean[z_scores < threshold]
  return df_clean
```

3. **Remoção de Outliers por Isolation Forest**

O método Isolation Forest identificou e removeu 2.162 registros (10% do dataset original), resultando em um conjunto de dados mais limpo (19.451 imóveis). As principais mudanças foram:

Essa abordagem trouxe mudanças significativas na distribuição dos dados. O preço médio dos imóveis caiu 9.8%, passando de 
540k para 487k, enquanto o valor máximo reduziu de 7.7 milhões para2.72 milhões, mantendo apenas imóveis considerados plausíveis. Na área habitável, o tamanho máximo diminuiu de 13.540 sqft para 5.400 sqft, eliminando as propriedades extremamente grandes. Curiosamente, o método manteve um outlier específico de 33 quartos, possivelmente por não identificá-lo como anomalia.

| Variável    | Original | Isolation Forest | Diferença   |
|-------------|---------:|-----------------:|------------:|
| grade       |     0.53 |             0.49 | ↓ 7.5%     |
| sqft_living |     0.46 |             0.42 | ↓ 8.7%     |
| bathrooms   |     0.37 |             0.32 | ↓ 13.5%    |
| view        |     0.24 |             0.16 | ↓ 33%      |

O dataset tratado apresentou características interessantes: as distribuições de preço e área habitável ficaram mais próximas da normalidade, a condição dos imóveis manteve a mesma média (3) mas eliminou casos extremos, e o ano médio de renovação caiu drasticamente de 84 para 5, indicando que muitas propriedades reformadas foram consideradas outliers. Entre as principais vantagens do Isolation Forest está sua capacidade de detectar outliers multidimensionais, como imóveis com preço alto e área pequena, ou propriedades com muitos quartos mas poucos banheiros, além de preservar melhor a média geral que o método IQR.

![Gráfico Heatmap!](/docs/img/graphs/heatmap_Isolation_Forest.png "Gráfico Heatmap")

No entanto, o método apresentou algumas limitações: manteve certos outliers óbvios (como o caso dos 33 quartos), pois se concentra em anomalias multidimensionais em vez de regras simples, e causou reduções mais significativas nas correlações, possivelmente eliminando alguns dados válidos porém raros. Em comparação com outros métodos, o Isolation Forest mostrou um equilíbrio: foi mais seletivo que o Z-score (preservando menos registros - 19.451 contra 21.003), mas menos agressivo que o IQR (que reduziu o dataset para 16.685 registros).

```python
from sklearn.ensemble import IsolationForest

def isolation_forest_outliers(df, contamination=0.1):
  clf = IsolationForest(contamination=contamination, random_state=42)
  preds = clf.fit_predict(df)
  return df[preds == 1]
```

4. **Remoção de Outliers por Local Outlier Factor**

O método Local Outlier Factor (LOF) identificou e removeu 2.162 registros (10% do original), resultando em um dataset com 19.451 imóveis. A análise comparativa revela:

Diferente de outros métodos, o LOF mostrou um comportamento único na limpeza dos dados. O preço médio praticamente não mudou (de 540k para 536k, apenas 0.7% de redução), enquanto o valor máximo caiu 31% (de 7.7milhões para 5.3 milhões), mantendo assim boa parte dos imóveis de luxo. Curiosamente, o método não removeu os valores extremos de área habitável (manteve o máximo de 13.540 sqft) nem o caso atípico de 33 quartos, mostrando que o LFO prioriza a análise contextual em vez de regras simples baseadas em valores isolados.

| Variável    | Original | LOF   | Diferença |
|-------------|---------:|------:|----------:|
| grade       |     0.53 |  0.52 | ↓ 2%     |
| sqft_living |     0.46 |  0.46 | 0%       |
| bathrooms   |     0.37 |  0.37 | 0%       |
| view        |     0.24 |  0.23 | ↓ 4%     |

O LOF focou principalmente em remover imóveis com combinações incomuns de características, como propriedades muito caras para poucos quartos ou com área pequena mas alta qualidade de construção. Também eliminou casos isolados geograficamente, como imóveis em zonas com poucas propriedades similares. Entre suas principais vantagens está a capacidade de preservar outliers unidimensionais quando fazem sentido no contexto local, além de manter estáveis as correlações entre variáveis - característica crucial para modelos que dependem dessas relações. 
 
![Gráfico Heatmap!](/docs/img/graphs/heatmap_LOF.png "Gráfico Heatmap")

No entanto, o método apresenta algumas limitações: manteve valores extremos óbvios (como os 33 quartos ou a área máxima) quando considerados normais em seu contexto, e exige maior poder computacional por precisar calcular proximidades entre todos os pontos. Comparado a outros métodos, o LOF se mostrou o mais conservador: reduziu apenas 31% do preço máximo (contra 81% do IQR e 69% do Z-score) e praticamente não alterou as correlações (variação de 0-4%, contra até 33% no Isolation Forest).

```python
from sklearn.neighbors import LocalOutlierFactor

def lof_outliers(df, n_neighbors=20, contamination=0.1):
  lof = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination)
  preds = lof.fit_predict(df)
  return df[preds == 1]
```


## Ferramentas utilizadas

No desenvolvimento do projeto utilizamos um conjunto de ferramentas essenciais que formam a base de qualquer pipeline de análise de dados em Python. O processo começa com a importação dos dados brutos através da biblioteca kagglehub, que permite o acesso direto aos datasets públicos disponíveis na plataforma Kaggle, incluindo nosso conjunto de dados sobre os imóveis.

```python 
dataset_dir = kagglehub.dataset_download("soylevbeytullah/house-prices-dataset")
plt.style.use('ggplot')

for filename in os.listdir(dataset_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(dataset_dir, filename)
        break

csv_file = pd.read_csv(file_path)
data_frame = pd.DataFrame(csv_file)
```

Uma vez importados, os dados são processados e manipulados utilizando duas bibliotecas fundamentais: numpy (np) e pandas (pd). O numpy, especializado em cálculos numéricos, foi empregado para operações matemáticas e cálculos estatísticos. Já o pandas, a ferramenta mais importante para análise de dados tabulares, foi utilizado em todas as etapas - desde a carga inicial dos dados com pd.read_csv() até operações avançadas de limpeza (remoção de valores nulos, filtragem de colunas) e análises estatísticas descritivas através de métodos como describe().

```python 
def show_column_values(df, column):
    print(f"Distribuição de")
    print(df[column].value_counts())
    print("-------------------------------------------")

def show_df_describe(df, title):
    print(title)
    print(df.iloc[:,2:].describe().apply(lambda s: s.apply('{:,.0f}'.format)))
    print("-------------------------------------------")
```

A etapa de visualização dos dados foi realizada com o poderoso combo seaborn (sns) e matplotlib.pyplot (plt). O seaborn, construído sobre o matplotlib, foi usado para criar visualizações sofisticadas como boxplots (sns.boxplot()) e heatmaps (sns.heatmap()), essenciais para identificar padrões e outliers nos dados. Já o matplotlib.pyplot complementou essas visualizações, permitindo personalizações como adição de títulos (plt.title()), rótulos de eixos (plt.xlabel()) e o salvamento das figuras geradas (plt.savefig()) para uso em relatórios.

```python 
def show_histplot(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=50)
    plt.title(f"Distribuição de {column}")
    plt.xlabel(column)
    plt.ylabel("Contagem")
    plt.show()

def show_boxplot(df, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot de {column}")
    plt.xlabel(column)
    plt.show()

def show_scatterplot(df, column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=column, y="price", data=df)
    plt.title(f"price vs {column}")
    plt.xlabel(column)
    plt.ylabel("price")
    plt.show()

def plot_heatmap(df, title, ignore_col):
    correlations = df[df.iloc[:,ignore_col:].columns].corr(method='kendall')
    fig, ax = plt.subplots(figsize=(30,30))
    ax = sns.heatmap(correlations, annot=True, cmap='coolwarm', linewidths=.5)
    ax.set_yticklabels(rotation=0, labels=correlations.columns, fontsize=10)
    ax.set_xticklabels(rotation=0, labels=correlations.columns, fontsize=10)
    ax.set_title(title)
    plt.show()
```

O fluxo completo de trabalho no Google Colab segue uma lógica clara: primeiro baixamos os dados, depois os manipulamos e limpamos, e finalmente os visualizamos para extrair insights. Cada uma dessas bibliotecas desempenha um papel específico e complementar nesse processo.


# Referências

> - [Glossário de termos para lotes residenciais](https://blue.kingcounty.com/Assessor/eRealProperty/ResidentialGlossary.aspx?idx=viewall&Parcel=3225069065&AreaReport=https://kingcounty.gov/en/dept/assessor/buildings-and-property/property-value-and-information/reports/area-reports/2024/residential-westcentral)
> - [Página de Detalhes de uma residência do Condado de King](https://blue.kingcounty.com/Assessor/eRealProperty/Detail.aspx?ParcelNbr=3225069065)
> - [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
> - [Seaborn API](https://seaborn.pydata.org/api.html)
> - [Scikit Learn User Guide](https://scikit-learn.org/stable/user_guide.html)

# Vídeo de apresentação da Etapa 02

[video de apresentação Etapa 2](videos/ProjetoHousePricing-Etapa2.mp4)


