# File: analytics.py
import pandas as pd
import numpy as np

def apply_rolling_windows(df, window_size=7):
    """
    Task 2.1: Calculate Rolling Averages.
    """
    print(f"\n--- Calculating {window_size}-Day Rolling Averages ---")
    
    # Calculate rolling mean per asset
    df[f'ma_{window_size}'] = df.groupby('asset')['price'].transform(
        lambda x: x.rolling(window=window_size).mean()
    )
    return df

def detect_trend_changes(df, window_size=7):
    """
    Task 2.2: Feature Engineering - Trend Change Detection.
    A simple crossover strategy: Price > MA -> Uptrend, Price < MA -> Downtrend.
    """
    print("\n--- Detecting Trend Changes ---")
    
    # Create a signal: 1 if Price > MA, -1 if Price < MA
    df['trend_signal'] = np.where(df['price'] > df[f'ma_{window_size}'], 1, -1)
    
    # Detect where the signal changes
    df['trend_change'] = df.groupby('asset')['trend_signal'].diff().fillna(0)
    
    changes = df[df['trend_change'] != 0]
    print(f"Identified {len(changes)} potential trend change points.")
    return df