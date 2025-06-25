# Preparação dos dados

Durante o pré-processamento do dataset, inicialmente foi feita a verificação de valores ausentes, e constatou-se que não havia dados nulos ou vazios, eliminando a necessidade de preenchimento ou remoção de linhas. Em seguida, foi aplicado um tratamento de outliers, removendo registros com valores extremos nas variáveis **price, bedrooms e bathrooms,** restringindo os valores para até 5 milhões de dólares no preço, no máximo 9 quartos e até 7 banheiros. Isso ajudou a evitar que pontos fora do padrão influenciassem negativamente o desempenho dos modelos.

Na etapa de transformação de dados, foi aplicada a transformação logarítmica à variável price, com o objetivo de reduzir a assimetria da distribuição e melhorar a performance de algoritmos lineares. A variável categórica **zipcode** foi convertida para o formato numérico por meio de one-hot encoding, permitindo seu uso por modelos de machine learning.

Foi também realizada engenharia de atributos, criando variáveis derivadas como:

- **house_age**, calculada com base no ano de construção (2015 - yr_built);
- **was_renovated**, indicando com 1 se a casa foi reformada ou 0 caso contrário;
- **total_sqft**, representando a área total utilizável da casa, somando sqft_living e sqft_basement.

Além disso, foram extraídas características polinomiais a partir das coordenadas geográficas **lat e long**, gerando combinações como **lat², long² e lat*long,** o que permite capturar relações espaciais não lineares que influenciam o valor dos imóveis.

Essas transformações contribuíram para tornar os dados mais adequados ao aprendizado de máquina, melhorando a capacidade dos modelos de capturar padrões relevantes e realizar previsões mais precisas.

```python 
  def transform_zipcode_encoding(df):
      encoding_df = df.copy()
      encoding_df = pd.get_dummies(encoding_df, columns=['zipcode'], prefix='zip')
      return encoding_df

  def transform_df_log_price(df):
      log_df = df.copy()
      log_df['price'] = np.log1p(log_df['price'])
      return log_df

    # Prever e reverter para dólares
    y_pred_log = model.predict(X_test)
    y_pred_dollar = np.expm1(y_pred_log)
    y_true_dollar = np.expm1(y_test)

    # Calcular Previsões Reais
    r2 = r2_score(y_true_dollar, y_pred_dollar)
    mse = mean_squared_error(y_true_dollar, y_pred_dollar)
    rmse = np.sqrt(mse)

  from sklearn.preprocessing import PolynomialFeatures

  def transform_df_polynomial(df):
      poly = PolynomialFeatures(degree=2, include_bias=False)
      df_poly = df.copy()
      poly_features = poly.fit_transform(df_poly[['lat', 'long']])
      df_poly[['lat', 'long', 'lat_sq', 'long_sq', 'lat_long']] = poly_features
      return df_poly

```


# Descrição dos modelos

## Random Forest Regressor

Para este projeto, implementamos o algoritmo `RandomForestRegressor` como um dos modelos de aprendizado supervisionado. Esse algoritmo pertence à categoria de ensemble learning e funciona combinando várias árvores de decisão, de forma que cada árvore vote por um valor e a média das predições seja usada como resultado final.

O Random Forest foi escolhido pelas suas principais vantagens:
- Robustez contra overfitting
- Capacidade de modelar relações não lineares
- Importância de variáveis interpretável

Diversas versões do modelo foram treinadas e avaliadas com variações no conjunto de dados, incluindo:
- Remoção da variável `zipcode`
- Engenharia de atributos: `house_age`, `was_renovated`, `total_sqft`
- Transformações em `latitude` e `longitude` (polinômios e bins)
- Aplicação de `log(price)` para suavizar a distribuição de preços

Essas versões foram avaliadas com base em suas métricas de desempenho (RMSE, MSE, R², erro percentual) para identificar o modelo mais eficaz.

## Linear Regression 

A regressão linear é um método estatístico usado para modelar a relação entre uma variável dependente (alvo) e uma ou mais variáveis independentes (preditoras), assumindo que essa relação pode ser aproximada por uma linha reta. Ela estima os coeficientes de uma equação linear que melhor se ajusta aos dados, de forma a minimizar a soma dos erros quadráticos entre os valores previstos e os reais.

A ideia é modelar uma relação linear entre price e um conjunto de variáveis explicativas (features), ajustando uma equação da forma:

y = β0 + β1x1 + β2x2 + ⋯ + βnxn

onde 𝑦 é a estimativa de price, 𝑥1,𝑥2,…,𝑥𝑛 são as features como bedrooms, bathrooms, sqft_living, etc., e os β são os coeficientes aprendidos pelo modelo que indicam a influência de cada variável no preço final.
​

Durante o treinamento, o modelo ajusta os coeficientes de forma a minimizar a soma dos quadrados dos resíduos entre os valores reais de price e os valores previstos 𝑦. Isso resulta em uma função de predição que pode ser usada para estimar o preço de casas com base nas características fornecidas. Essa abordagem é especialmente útil por sua interpretabilidade e simplicidade matemática.

# Avaliação dos modelos criados

Os processos de validação MAE (Erro Absoluto Médio), MSE (Erro Quadrático Médio), RMSE (Raiz do Erro Quadrático Médio) e R² (Coeficiente de Determinação) são métricas fundamentais para avaliar modelos de regressão, como Linear Regression e Random Forest em tarefas de previsão de valores contínuos.

## Métricas utilizadas

O MAE calcula a média das diferenças absolutas entre as previsões e os valores reais, sendo intuitivo e robusto a outliers. O MSE mede a média dos quadrados dos erros, penalizando mais erros grandes, mas sua escala é menos interpretável. O RMSE resolve isso ao extrair a raiz quadrada do MSE, retornando à unidade original dos dados. O R² indica a proporção da variância dos dados que o modelo consegue explicar, variando de 0 (pior) a 1 (melhor).

Ambos os modelos (Linear Regression e Random Forest) podem ser avaliados com essas métricas, mas o Random Forest, por ser baseado em árvores e capturar relações não lineares, tende a ter menor MAE/MSE/RMSE e maior R² em dados complexos, embora com risco de overfitting. Essas métricas permitem comparar a precisão das previsões e a capacidade de generalização dos modelos, independentemente do algoritmo utilizado.

## Discussão dos resultados obtidos

O modelo `RandomForestRegressor` foi testado com cinco variações principais dos dados. A comparação envolveu:

- Conjunto base sem `zipcode`
- Base com atributos derivados (ex: `house_age`)
- Base com polinômios de `lat` e `long`
- Base com `lat/long` convertidos em bins (regiões discretas)
- Transformação logarítmica da variável `price`

A versão com `log(price)` obteve o **menor erro absoluto (RMSE ≈ 0.0015)** e o **menor erro percentual médio (18.37%)**, sendo a mais eficaz para melhorar a precisão. Já a versão sem `zipcode`, com os dados brutos, alcançou o **maior R² (0.8885)**, explicando melhor a variância do preço.

Isso demonstra que o Random Forest é robusto e consistente, mesmo com diferentes representações dos dados. O uso de engenharia de atributos e transformações contribuiu positivamente para o desempenho final.

| Versão                        | RMSE     | MSE          | R²     | Erro percentual |
|-------------------------------|----------|--------------|--------|-----------------|
| Sem zipcode                   | 0.003458 | 0.00001196   | 0.8885 | 0.27%           |
| Variáveis novas + sem zipcode | 0.003497 | 0.00001223   | 0.8860 | 0.27%           |
| Polinômios em lat/long        | 0.003498 | 0.00001224   | 0.8859 | 0.27%           |
| Com bins lat/long             | 0.003484 | 0.00001214   | 0.8868 | 0.27%           |
| Log(price)                    | 0.001524 | 0.00000232   | 0.8860 | 0.18%           |


O modelo de `Linear Regression` foi testado com diversas variações principais dos dados. A comparação envolveu:

- Conjunto base sem nenhuma alteração
- Conjunto base sem `zipcode`
- Conjunto base sem `zipcode, Lat e Long`
- Base com atributos derivados (ex: `house_age`)
- Base com polinômios de `lat` e `long`
- Base com `lat/long` convertidos em bins (regiões discretas)
- Transformação logarítmica da variável `price`
- Transformação one-hot encoding do `zipcode`
- Combinação do one-hot encoding do `zipcode` com polinômios de `lat` e `long`
- Combinação do one-hot encoding do `zipcode` com polinômios de `lat` e `long` e atributos derivados
-  Combinação do one-hot encoding do `zipcode` com polinômios de `lat` e `long` e Transformação logarítmica da variável `price`
-  Combinação do one-hot encoding do `zipcode` com polinômios de `lat` e `long` e Remoção leve de alguns Outliers
-  Combinação do one-hot encoding do `zipcode` com polinômios de `lat` e `long` e Transformação logarítmica da variável `price` e Remoção leve de alguns Outliers

O modelo original apresentou um RMSE de aproximadamente 212 mil e um R² de 0.7005, servindo como base comparativa. A exclusão de atributos geográficos como zipcode, lat e long levou a uma piora considerável no desempenho, indicando que a localização é um fator crucial para a previsão de preços. 

| Modelo                                     | RMSE         | R²     |
|--------------------------------------------|-------------:|-------:|
| Modelo Original                            | 212,008.67   | 0.7005 |
| Modelo Sem Zipcode                         | 213,724.81   | 0.6957 |
| Modelo Sem Zipcode, Lat e Long             | 228,210.44   | 0.6530 |
| Modelo com modificação de colunas          | 216,377.03   | 0.6881 |
| Modelo com transformação polinomial        | 204,099.31   | 0.7225 |
| Modelo com Spatial Binning                 | 211,679.92   | 0.7015 |
| Modelo com logaritmo do Price              | 273,734.13   | 0.5008 |
| Modelo com one-hot encoding do Zipcode     | 169,539.73   | 0.8085 |
| Modelo com encoding e polinomial           | 169,372.19   | 0.8089 |
| Modelo com enc, poly e mod colunas         | 177,853.15   | 0.7892 |
| Modelo com enc, poly e log price           | 220,918.85   | 0.6748 |
| Modelo com enc, poly e outliers            | 151,283.12   | 0.8226 |
| Modelo com enc, poly, log price e outliers | 136,441.85   | 0.8557 |

 A combinação de encoding + polinômios refinou ainda mais os resultados, tornando-se o melhor modelo. Por outro lado, a transformação logarítmica do preço prejudicou drasticamente o modelo, indicando incompatibilidade com a distribuição dos dados ou a métrica utilizada.


# Pipeline de pesquisa e análise de dados

Para a modelagem com Random Forest e LinearRegression, seguimos um pipeline bem definido e replicável:

1. **Pré-processamento**: remoção de colunas irrelevantes e outliers, tratamento de duplicatas, criação de atributos derivados;
2. **Divisão dos dados**: 80% para treino, 20% para teste;
3. **Treinamento**: uso da função `train_random_forest()` com modularidade para testes variados;
4. **Avaliação**: função `evaluate_random_forest_model()` com retorno das métricas principais;
5. **Comparação estruturada**: tabela `df_results` para comparar todas as versões testadas;
6. **Escolha final**: melhor versão identificada com base em RMSE e R², levando em conta o objetivo da predição.

Esse pipeline foi reutilizável e permitiu analisar com clareza o impacto de cada modificação nos dados.

```python 
# Função de treino
def train_random_forest(df, test_size=0.2, random_state=42, drop_columns=[]):
    drop_columns.extend(['id', 'date', 'price'])
    X = df.drop(drop_columns, axis=1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    rf_model = RandomForestRegressor(n_estimators=100, random_state=random_state)
    rf_model.fit(X_train, y_train)

    return {
        'model': rf_model,
        'X_test': X_test,
        'y_test': y_test,
        'X_train': X_train,
        'y_train': y_train,
        'feature_names': X.columns.tolist()
    }

# Função de avaliação
def evaluate_random_forest_model(results):
    model = results['model']
    X_test = results['X_test']
    y_test = results['y_test']
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    erro_percentual = (rmse / y_test.mean()) * 100

    # Importância das features
    importances = pd.DataFrame({
        'Feature': results['feature_names'],
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)

    # Impressão das métricas
    print("Random Forest Performance:")
    print(f"MSE: {mse:,.2f}")
    print(f"RMSE: {rmse:,.2f}")
    print(f"R-squared: {r2:.4f}")
    print(f"Erro percentual médio: {erro_percentual:.2f}%")
    print("\nTop 5 Important Features:")
    print(importances)

   # Gráfico: valores reais vs previstos
    print("\n")
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted Values')
    plt.grid(True)
    plt.show()

    # Gráfico de resíduos
    print("\n")
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residual Analysis')
    plt.grid(True)
    plt.show()
    print("\n")

    return {
        'RMSE': rmse,
        'MSE': mse,
        'R2': r2,
        'Erro percentual': erro_percentual
    }
```

# Análise Comparativa de Modelos de Regressão para Previsão do Dataset 

Realizamos testes com diversos modelos de regressão aplicados ao nosso dataset, removendo colunas irrelevantes (como id, date, price, entre outras) e avaliando o desempenho com base em métricas padronizadas. Os resultados foram organizados de forma a facilitar a interpretação comparativa.

Foram utilizados cinco modelos: **Gradient Boosting, XGBoost, LightGBM, Random Forest e Regressão Linear**. Os quatro primeiros são algoritmos baseados em árvores de decisão, com variações em eficiência, paralelização e estratégias de crescimento. Já a **Regressão Linear** representa uma abordagem mais simples e interpretável, baseada na suposição de relação linear entre as variáveis.

A avaliação foi feita por meio das métricas MAE, MSE, RMSE, R² e erro percentual (RMSE relativo à média dos valores reais). A tabela a seguir resume os resultados:

| Modelo              | MAE        | MSE              | RMSE       | R²     | Erro Percentual |
|---------------------|------------|------------------|------------|--------|-----------------|
| **Gradient Boosting**   | 74.114,61  | 16.167.312.530,00 | 127.150,75 | 0,8747 | 23,48%          |
| **XGBoost**             | 65.467,44  | 12.936.883.614,68 | 113.740,42 | 0,8997 | 21,01%          |
| **LightGBM**            | 64.842,25  | 12.444.102.256,10 | 111.553,14 | 0,9035 | 20,60%          |
| **Random Forest**       | 68.699,67  | 15.160.600.854,06 | 123.128,39 | 0,8825 | 22,74%          |
| **Linear Regression**   | 74.683,45  | 18.616.377.895,61 | 136.441,85 | 0,8557 | 25,20%          |

O **LightGBM** apresentou o melhor desempenho geral, com menor erro e maior coeficiente de determinação, além de ser mais eficiente em termos computacionais. O XGBoost se mostrou uma alternativa sólida, especialmente útil quando interpretabilidade e regularização são relevantes. Random Forest e Gradient Boosting tiveram desempenho intermediário, enquanto a Regressão Linear teve os piores resultados, sendo adequada apenas em cenários onde a simplicidade do modelo é prioritária.

### Limitações identificadas:

- Os erros percentuais, entre **20% e 25%**, ainda são elevados para aplicações sensíveis, como previsões financeiras.
- Os hiperparâmetros não foram otimizados (utilizou-se **n_estimators=100** como padrão).
- A ausência de normalização pode ter prejudicado o desempenho da Regressão Linear.

### Próximos passos recomendados:

- Realizar tuning de hiperparâmetros (ex.: profundidade das árvores, learning rate).
- Investigar a presença de outliers e incluir novas variáveis relevantes.
- Testar pré-processamento adicional, como normalização e transformação de features.
- Explorar combinações de modelos (ensembles híbridos) para maior robustez.

# Vídeo de apresentação da Etapa 03

[video de apresentação Etapa 3](videos/ProjetoHousePricing-Etapa3.mp4)
