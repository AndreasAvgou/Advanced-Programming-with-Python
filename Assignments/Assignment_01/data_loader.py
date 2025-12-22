# File: data_loader.py
import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    """
    Task 1: Load and clean the Twitter dataset.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    print(f"--- Loading data from {filepath} ---")
    try:
        # 1.1 Load large file
        df = pd.read_csv(filepath)
        
        # 1.2 Data Cleaning
        initial_count = len(df)
        
        # Drop duplicates based on tweet_id
        df.drop_duplicates(subset=['tweet_id'], inplace=True)
        
        # Handle missing values (e.g., fill NaNs in hashtags with 'unknown')
        df['hashtag'] = df['hashtag'].fillna('unknown')
        
        # Convert date column to datetime objects
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Drop rows with invalid dates
        df.dropna(subset=['date'], inplace=True)
        
        print(f"[Info] Loaded {len(df)} rows (Removed {initial_count - len(df)} duplicates/invalid).")
        return df
        
    except FileNotFoundError:
        print("[Error] File not found.")
        return None