# File: data_loader.py
import pandas as pd
import os

def load_and_clean_data(filename):
    """
    Loads CSV, removes NaN values, filters bad headers, and converts types.
    """
    if not os.path.exists(filename):
        print(f"[Error] File '{filename}' not found.")
        return None

    try:
        df = pd.read_csv(filename)
        
        # Drop rows with NaN
        df = df.dropna(how='all')

        # Filter out repeated header rows
        df = df[df['Order Date'].str[0:2] != 'Or']

        # Convert types
        df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
        df['Price Each'] = pd.to_numeric(df['Price Each'])
        df['Order Date'] = pd.to_datetime(df['Order Date'])

        print("[Success] Data loaded and cleaned.")
        return df
    except Exception as e:
        print(f"[Error] Data loading failed: {e}")
        return None