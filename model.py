from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def train_model(df):
    #Split the data into features and target
    features = ['SMA10', 'SMA50', 'Prev_Close']
    target = 'Close'

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, shuffle=False)
    model = LinearRegression
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"Model Performance: MAE={mae:.2f}, RMSE={rmse:.2f}")

    return model, y_test, y_pred



