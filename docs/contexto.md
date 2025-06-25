# Introdução

O mercado imobiliário no Condado de King, Washington, é altamente dinâmico e influenciado por fatores como localização, características dos imóveis e condições econômicas. Prever com precisão os preços dos imóveis é essencial para compradores, vendedores, investidores e instituições financeiras, que buscam minimizar riscos e maximizar retornos.

Este projeto de ciência de dados utiliza um conjunto de dados completo do Kaggle para desenvolver modelos de aprendizado de máquina capazes de prever os preços dos imóveis na região. O objetivo é não apenas criar uma ferramenta preditiva eficaz, mas também fornecer insights sobre os fatores que influenciam o mercado imobiliário local, apoiando decisões mais informadas.

## Problema

O mercado imobiliário no Condado de King, Washington, é altamente dinâmico e complexo, sendo influenciado por uma variedade de fatores relacionados, como localização, características físicas dos imóveis (tamanho, número de quartos, idade da propriedade, etc.), condições econômicas (taxas de juros, inflação, desemprego) e até mesmo tendências sociais e demográficas. Diante dessa complexidade, determinar o valor justo de um imóvel torna-se um desafio significativo, tanto para compradores quanto para vendedores, investidores e instituições financeiras.

Um dos principais problemas enfrentados é a falta de precisão na avaliação dos preços, o que pode levar a decisões ruins. Compradores podem pagar valores acima do mercado, enquanto vendedores podem perder oportunidades de maximizar seus lucros. Investidores, por sua vez, podem enfrentar dificuldades em identificar propriedades com potencial de valorização, e instituições financeiras podem incorrer em riscos ao conceder financiamentos baseados em avaliações imprecisas. Além disso, a volatilidade do mercado e a constante mudança nos fatores que influenciam os preços dificultam a criação de modelos de previsão confiáveis.


## Questão de pesquisa

Quais são os principais fatores que influenciam os preços dos imóveis no Condado de King, Washington, e como modelos de aprendizado de máquina podem ser utilizados para prever esses preços com precisão?


## Objetivos preliminares

O objetivo geral deste projeto de aprendizado de máquina é desenvolver e implementar modelos preditivos robustos capazes de estimar com precisão os preços de imóveis no Condado de King, Washington, contribuindo para uma melhor compreensão do mercado imobiliário local. Para isso, o projeto tem como objetivos preliminares:

1. Explorar e experimentar diferentes algoritmos de aprendizado de máquina, selecionando aqueles mais adequados para resolver o problema de previsão de preços de imóveis, com foco em modelos de regressão.

2. Desenvolver e otimizar modelos de regressão que possam prever os valores das propriedades com base em variáveis como localização, características físicas dos imóveis e condições econômicas.

3. Identificar e analisar os principais fatores que influenciam os preços dos imóveis na região, utilizando técnicas de análise de dados e interpretação dos modelos para fornecer insights valiosos sobre as dinâmicas do mercado.


## Justificativa

O mercado imobiliário no Condado de King, Washington, é vital para a economia local e seus mais de 2,2 milhões de habitantes. Com uma área de 5.976,3 km², que inclui desde áreas urbanas como Seattle até regiões naturais, o condado apresenta uma diversidade única de imóveis, influenciados por fatores como localização e condições econômicas. Essa complexidade torna a avaliação precisa dos preços dos imóveis um desafio necessário.

Esse projeto visa facilitar decisões relacionadas ao mercado imobiliário, garantindo transações justas para compradores e vendedores. Além disso, os resultados podem auxiliar no planejamento urbano, fornecendo dados confiáveis para políticas públicas e desenvolvimento eficaz. Também contribui para a redução de riscos de instituições financeiras e investidores, que podem usar modelos preditivos precisos para tomar decisões mais seguras.

A relevância histórica e econômica do condado, fundado em 1852 e lar de Seattle, reforça a importância de compreender seu mercado imobiliário. Este projeto não só aborda uma necessidade prática, mas também promove o desenvolvimento sustentável e o bem-estar da comunidade local.


## Público-Alvo

O público-alvo deste projeto abrange compradores e vendedores de imóveis, que buscam avaliações precisas para transações justas; investidores, que dependem de dados confiáveis para identificar oportunidades e reduzir riscos; e instituições financeiras, que utilizam previsões para calcular riscos em financiamentos. Também inclui corretores e imobiliárias, que precisam de informações para assessorar clientes e otimizar negócios, além de governos e urbanistas, que utilizam dados para políticas públicas e planejamento urbano eficaz. Acadêmicos e pesquisadores interessados em estudos sobre mercados imobiliários e modelos preditivos, bem como a sociedade em geral, que se beneficia de um mercado mais transparente e políticas informadas, completam o público-alvo. Esses grupos dependem de informações confiáveis para decisões estratégicas, econômicas ou sociais.


## Estado da arte

O uso de técnicas de aprendizado de máquina para previsão de preços de imóveis tem se consolidado como uma abordagem eficaz em diversos contextos geográficos e mercados. Projetos recentes demonstram a aplicação de métodos avançados para melhorar a precisão das previsões e identificar os fatores mais relevantes que influenciam os valores das propriedades.

[Malere et al. (2019)](https://repositorio.ufc.br/bitstream/riufc/48854/3/2019_tcc_ghpsilva.pdf?utm_source=) exploraram a aplicação de técnicas de mineração de dados e aprendizado de máquina para prever preços de imóveis em diferentes regiões do Brasil. O estudo destacou a importância da seleção de variáveis relevantes, como localização, infraestrutura e características físicas dos imóveis, e comparou o desempenho de múltiplos modelos, incluindo regressão linear e métodos baseados em árvores de decisão. Os resultados mostraram que a escolha adequada de variáveis e algoritmos pode melhorar significativamente a precisão das previsões.

[Jha et al. (2020)](https://arxiv.org/abs/2008.09922?utm_source=) desenvolveram um modelo de classificação para prever se o preço de venda de propriedades na Flórida, EUA, seria maior ou menor que o preço listado. Utilizando algoritmos como Regressão Logística, Random Forest e XGBoost, combinados com técnicas de codificação de alvos, o estudo demonstrou a eficácia de métodos ensemble para capturar padrões complexos nos dados. O trabalho destacou a importância de integrar múltiplas abordagens para melhorar a robustez dos modelos.

[Chou (2022)](https://repositorio.pucgoias.edu.br/jspui/bitstream/123456789/7983/1/intelig%C3%AAncia%20artificial%20no%20mercado%20imobili%C3%A1rio.pdf?utm_source) focou na previsão de preços de imóveis em Taipei, Taiwan, utilizando técnicas de aprendizado de máquina para analisar fatores como localização, tamanho do imóvel e condições econômicas. O estudo evidenciou a relevância de modelos como redes neurais e Gradient Boosting para lidar com a complexidade do mercado imobiliário, especialmente em áreas urbanas densamente povoadas.

[Silva (2019)](https://repositorio.ufc.br/handle/riufc/48854?locale=es&utm_source) propôs a aplicação de metodologias de aprendizagem computacional para avaliação de imóveis em Fortaleza, Brasil. O estudo comparou o desempenho de diferentes algoritmos, como Random Forest e Support Vector Machines (SVM), e discutiu a importância de escolher modelos que se adaptem às particularidades do mercado local. Os resultados reforçaram a necessidade de personalizar abordagens para cada contexto geográfico.

[Alencar (2020)](https://bdta.abcd.usp.br/directbitstream/766cd876-04c6-4f3e-ae20-a0314fb58c37/Sergio%20Ricardo%20Ribeiro%20Alencar.pdf?utm_source) explorou a aplicação de modelos de aprendizado de máquina na precificação de imóveis, destacando a importância da qualidade e quantidade dos dados para a precisão das previsões. O estudo enfatizou que a coleta e o pré-processamento de dados são etapas críticas para o sucesso dos modelos, especialmente em mercados com alta variabilidade e dinâmica complexa.


# Descrição do _dataset_ selecionado

O conjunto de dados, disponibilizado no **Kaggle**, inclui os preços de venda de imóveis no Condado de King, nos EUA, os imóveis foram vendidos no período entre maio de 2014 e maio de 2015. Com **21.613 registros** completos, sem dados faltantes. Os dados estão distribuídos em **21 colunas**, detalhadas na tabela abaixo , e estão no formato **CSV**. [kc_house_data.csv](src\kc_house_data.csv)


| Coluna            | Descrição                                                                 |
|-------------------|---------------------------------------------------------------------------|
| id                | Identificação única de um imóvel                                          |
| date              | Data de venda do imóvel                                                   |
| price             | Preço do imóvel (variável alvo para previsão)                             |
| bedrooms          | Número de quartos do imóvel                                               |
| bathrooms         | Número de banheiros do imóvel                                             |
| sqft_living       | Pé quadrado  da área habitável                                       |
| sqft_lot          | Pé quadrado  do terreno                                              |
| floors            | Número total de andares (níveis) do imóvel                                |
| waterfront        | Indica se o imóvel tem vista para alguma fonte de água (1 = sim, 0 = não)               |
| view              | Indica se o imóvel foi visualizado  (1 = sim, 0 = não)                                      |
| condition         | Avaliação da condição geral do imóvel                                     |
| grade             | Nota geral do imóvel, baseada no sistema de classificação do Condado de King |
| sqft_above        | Pé quadrado  da casa, excluindo o porão                              |
| sqft_basement     | Pé quadrado  do porão                                                |
| yr_built          | Ano de construção do imóvel                                               |
| yr_renovated      | Ano de renovação do imóvel (se aplicável)                                 |
| zipcode           | Código postal da localização do imóvel                                    |
| lat               | Coordenada de latitude do imóvel                                          |
| long              | Coordenada de longitude do imóvel                                         |
| sqft_living15     | Pé quadrado  da sala de estar em 2015 (indica possíveis reformas)    |
| sqft_lot15        | Pé quadrado  do terreno em 2015 (indica possíveis reformas)          |

# Canvas analítico

![Canvas Analítico!](/docs/img/canvas-analitico.png "Canvas Analítico")


# Vídeo de apresentação da Etapa 01

[video de apresentação Etapa 1](videos/ProjetoHousePricing-Etapa1.mp4)


# Referências


> **Links**:
> - [King County Demographics](https://kingcounty.gov/en/dept/executive/governance-leadership/performance-strategy-budget/regional-planning/demographics)
> - [Dados do mercado imobiliário de King County.](https://www.kaggle.com/datasets/soylevbeytullah/house-prices-dataset)
> - [Essential Data Cleaning Techniques for Accurate Machine Learning Models](https://www.kdnuggets.com/essential-data-cleaning-techniques-accurate-machine-learning-models)
> - [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
> - [Scikit Learn User Guide](https://scikit-learn.org/stable/user_guide.html)
> - [Software Analytics Canvas](https://www.feststelltaste.de/software-analytics-canvas/)