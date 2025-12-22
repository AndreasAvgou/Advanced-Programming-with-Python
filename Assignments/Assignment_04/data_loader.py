# File: data_loader.py
import pandas as pd

def load_and_clean_data(filepath):
    """
    Task 1: Load and clean the User Behavior dataset.
    """
    print(f"--- Loading data from {filepath} ---")
    try:
        df = pd.read_csv(filepath)
        
        # 1.1 Check for duplicates
        initial_len = len(df)
        df.drop_duplicates(subset=['user_id'], inplace=True)
        
        # 1.2 Handle missing values (if any)
        # For this dataset, we fill numeric NaNs with the median
        df.fillna(df.median(), inplace=True)
        
        # 1.3 Validate Data Types
        df['user_id'] = df['user_id'].astype(int)
        df['churned'] = df['churned'].astype(int)
        
        print(f"[Info] Loaded {len(df)} unique users (Removed {initial_len - len(df)} duplicates).")
        return df
        
    except FileNotFoundError:
        print("[Error] File not found.")
        return None