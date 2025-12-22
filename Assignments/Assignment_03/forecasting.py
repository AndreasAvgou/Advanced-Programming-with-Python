# File: forecasting.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import os
import config

def train_and_forecast(df, asset_name):
    """
    Task 4.1: Time-series forecasting using Linear Regression.
    Predicts Price based on 'Day Index' (Simple Trend Line).
    """
    print(f"\n--- Forecasting for {asset_name} ---")
    
    asset_data = df[df['asset'] == asset_name].copy()
    if len(asset_data) < 5:
        print("Not enough data for forecasting.")
        return

    # Feature Engineering for ML: Use integer index as time feature
    asset_data['day_index'] = np.arange(len(asset_data))
    
    X = asset_data[['day_index']]
    y = asset_data['price']
    
    # Split Train/Test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model MSE: {mse:.4f}")
    
    # Forecast Future (Next 5 days)
    last_day = asset_data['day_index'].max()
    future_X = np.array([[last_day + i] for i in range(1, config.FORECAST_DAYS + 1)])
    future_pred = model.predict(future_X)
    
    print(f"Next {config.FORECAST_DAYS} Days Prediction: {future_pred}")
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(asset_data['day_index'], y, label='Actual Price')
    plt.plot(X_test, predictions, label='Predicted (Test)', linestyle='--')
    plt.plot(future_X, future_pred, label='Forecast', color='red', marker='o')
    plt.title(f'{asset_name} Price Forecast')
    plt.legend()
    
    save_path = os.path.join(config.PLOTS_DIR, f'forecast_{asset_name}.png')
    plt.savefig(save_path)
    plt.close()
    print(f"Forecast plot saved to {save_path}")