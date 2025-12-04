# File: data_loader.py
import pandas as pd
import os

def load_tweets(filename):
    """
    Loads the CSV file into a Pandas DataFrame.
    """
    if not os.path.exists(filename):
        print(f"[Error] File '{filename}' not found.")
        return None

    try:
        # Load CSV (assuming standard encoding)
        df = pd.read_csv(filename)
        print(f"[Success] Loaded {len(df)} tweets from '{filename}'.")
        
        # Display columns to help identify the text column
        print(f"[Info] Columns found: {list(df.columns)}")
        
        return df
    except Exception as e:
        print(f"[Error] Failed to read CSV: {e}")
        return None