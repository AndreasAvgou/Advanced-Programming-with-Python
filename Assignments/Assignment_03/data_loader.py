# File: data_loader.py
import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    """
    Task 1.1: Load and clean the Finance dataset.
    """
    print(f"--- Loading data from {filepath} ---")
    try:
        df = pd.read_csv(filepath)
        
        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Sort by date
        df.sort_values(by='date', inplace=True)
        
        # Check for duplicates
        initial_len = len(df)
        df.drop_duplicates(inplace=True)
        
        # Fill missing prices with forward fill (common in finance)
        df['price'] = df['price'].ffill()
        
        print(f"[Info] Loaded {len(df)} records.")
        return df
    except FileNotFoundError:
        print("[Error] File not found.")
        return None

def detect_high_volatility(df, threshold=0.05):
    """
    Task 1.2: Find periods of high volatility.
    Calculates daily returns and checks if they exceed a threshold.
    """
    print("\n--- Volatility Analysis ---")
    # Calculate daily returns per asset
    df['returns'] = df.groupby('asset')['price'].pct_change()
    
    # Identify high volatility days
    high_vol = df[np.abs(df['returns']) > threshold]
    
    if not high_vol.empty:
        print(f"Found {len(high_vol)} high volatility events (Return > {threshold*100}%).")
        print(high_vol[['date', 'asset', 'returns']].head())
    else:
        print("No high volatility periods found.")
        
    return df