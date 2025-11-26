# File: main.py
import config
import data_fetcher
import data_processor
import visualizer

def main():
    print("=== Crypto Financial Analysis Tool ===")
    
    # 1. Fetch Data
    df_prices = data_fetcher.fetch_crypto_data(config.COINS)
    
    if df_prices is None or df_prices.empty:
        print("No data available. Exiting.")
        return

    # Display raw data preview
    print("\n--- Prices (Head) ---")
    print(df_prices.head())

    # 2. Calculate Daily Returns
    df_returns = data_processor.calculate_daily_returns(df_prices)
    print("\n--- Daily Returns (Head) ---")
    print(df_returns.head())

    # 3. Calculate Volatility (Risk)
    volatility = data_processor.calculate_volatility(df_returns)
    print("\n--- Volatility (Standard Deviation) ---")
    print(volatility.sort_values(ascending=False))

    # 4. Calculate Correlation
    correlation = data_processor.calculate_correlation(df_returns)
    print("\n--- Correlation Matrix ---")
    print(correlation)

    # 5. Visualizations
    print("\nGenerating Plots...")
    visualizer.plot_prices(df_prices)
    visualizer.plot_correlation_heatmap(correlation)

    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()