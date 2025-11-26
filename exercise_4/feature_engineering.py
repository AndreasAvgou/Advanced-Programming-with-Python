# File: feature_engineering.py
import pandas as pd

def add_features(df):
    """
    Adds 'Sales', 'Month', and 'City' columns to the DataFrame.
    """
    # 1. Total Sales
    df['Sales'] = df['Quantity Ordered'] * df['Price Each']
    
    # 2. Month
    df['Month'] = df['Order Date'].dt.month
    
    # 3. City Extraction Helper
    def get_city(address):
        return address.split(',')[1].strip()
    
    def get_state(address):
        return address.split(',')[2].split(' ')[1]

    # Apply City extraction
    df['City'] = df['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")
    
    print("[Success] Features added: Sales, Month, City.")
    return df