# File: main.py
import config
import data_loader
import analytics
import models
import forecasting

def main():
    print("=== Assignment 3: Automated Investment Portfolio Management ===")
    
    config.setup_directories()
    
    # --- TASK 1: Dataset Handling ---
    df = data_loader.load_and_clean_data(config.DATA_FILENAME)
    if df is None: return

    # Detect Volatility
    df = data_loader.detect_high_volatility(df)

    # --- TASK 2: Advanced Analytics ---
    df = analytics.apply_rolling_windows(df, window_size=3) # Short window for small dataset
    df = analytics.detect_trend_changes(df, window_size=3)

    # --- TASK 3: OOP Architecture (Portfolio) ---
    print("\n--- OOP Portfolio Management ---")
    portfolio = models.Portfolio()
    
    # Create Asset objects for each unique ticker
    unique_assets = df['asset'].unique()
    for ticker in unique_assets:
        asset_data = df[df['asset'] == ticker]
        asset_obj = models.Asset(ticker, asset_data)
        portfolio.add_asset(asset_obj)
        print(f"Added {ticker}: Avg Return={asset_obj.get_average_return():.4f}, Risk={asset_obj.get_risk():.4f}")

    # Optimize Weights
    optimal_weights = portfolio.optimize_weights()
    print("\nOptimal Portfolio Weights (Inverse Volatility):")
    for ticker, weight in optimal_weights.items():
        print(f"{ticker}: {weight:.2%}")

    # --- TASK 4: ML Forecasting ---
    print("\n--- ML Forecasting ---")
    # Forecast for the first asset in the list
    if len(unique_assets) > 0:
        forecasting.train_and_forecast(df, unique_assets[0])
    
    print("\n=== Execution Complete ===")

if __name__ == "__main__":
    main()