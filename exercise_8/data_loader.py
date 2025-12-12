# File: data_loader.py
import pandas as pd
import os

def load_data(filename):
    """
    Loads the Spotify dataset from CSV into a Pandas DataFrame.
    """
    if not os.path.exists(filename):
        print(f"[Error] File '{filename}' not found.")
        return None
        
    try:
        df = pd.read_csv(filename)
        print(f"[Success] Loaded {len(df)} tracks from '{filename}'.")
        # Display the first few rows to verify
        print(df.head())
        return df
    except Exception as e:
        print(f"[Error] Failed to load data: {e}")
        return None