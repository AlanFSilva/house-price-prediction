import pickle
import numpy as np
import pandas as pd
import os
import logging
from sklearn.preprocessing import PolynomialFeatures

script_dir = os.getcwd()
models = ['LinearRegression','RandomForest','GradientBoosting','XGBoost','LightGBM'] 

def complete_zipcodes_from_kc(df):
    file_id = "17zHf76n_Z_gXYu-kiRMb1upGRjz6JTpr"
    file_path = f"https://drive.google.com/uc?id={file_id}"
    df_zipcodes = pd.read_csv(file_path, header=None, names=['zipcode'])
    
    df_zipcodes['zipcode'] = df_zipcodes['zipcode'].astype(str).str.zfill(5)
    df_zipcodes['zipcode'] = 'zip_' + df_zipcodes['zipcode']

    for zip_col in df_zipcodes['zipcode'].unique():
      if zip_col not in df.columns:
          df[zip_col] = 0
    return df

def predict_model(payload, model):
    poly = PolynomialFeatures(degree=2, include_bias=False)
   
    if type(payload) == dict:
        arr = [payload]
        df = pd.DataFrame(arr)
    else:
        df = payload
        
    df['living_to_lot_ratio'] = df['sqft_living'] / df['sqft_lot']
    df['bath_per_bed'] = df['bathrooms'] / df['bedrooms']
    
    poly_features = poly.fit_transform(df[['lat', 'long']])
    df[['lat', 'long', 'lat_sq', 'long_sq', 'lat_long']] = poly_features
   
    df["sqft_living"] = np.log1p(df["sqft_living"])
    df["sqft_lot"] = np.log1p(df["sqft_lot"])
    
    df = pd.get_dummies(df, columns=['zipcode'], prefix='zip')
    df = complete_zipcodes_from_kc(df)
    
    df = df[sorted(df.columns)]
    y_pred = model.predict(df)
    return y_pred

def deserialize_model(model_name):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        #base_path = os.path.join(script_dir, 'site', 'wwwroot')

        filename = os.path.join("serializers", f"models-{model_name}.pkl")
        file_path = os.path.join(script_dir, filename)
        logging.error(file_path)
        print(file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Model file not found at {file_path}")
            
        with open(file_path, 'rb') as file:
            return pickle.load(file)
            
    except Exception as e:
        # Log detalhado para diagnóstico no Azure
        error = f"Failed to deserialize model {model_name}: {str(e)}"
        logging.error(error)
        print(error)
        raise

def predict_models_by_request(payload):
    predicts = []

    for model_name in models:
        model = deserialize_model(model_name)
        y_pred = predict_model(payload, model)
        print(model_name)
        predicts.append({
          "model": model_name,
          "value": np.expm1(float(y_pred))})

    return predicts