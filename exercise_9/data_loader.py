# File: data_loader.py
import pandas as pd
import os

def load_csv(filename):
    """
    Loads a CSV file into a Pandas DataFrame.
    
    Args:
        filename (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded data or None if file not found.
    """
    if not os.path.exists(filename):
        print(f"[Error] File '{filename}' not found.")
        return None

    try:
        df = pd.read_csv(filename)
        print(f"[Success] Loaded {len(df)} rows from '{filename}'.")
        return df
    except Exception as e:
        print(f"[Error] Failed to read CSV: {e}")
        return None