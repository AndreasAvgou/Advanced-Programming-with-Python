# File: data_loader.py
import pandas as pd

def load_and_clean_data(filepath):
    """
    Task 1: Load and clean the Music dataset.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    print(f"--- Loading data from {filepath} ---")
    try:
        # 1.1 Load data
        df = pd.read_csv(filepath)
        
        # 1.2 Data Cleaning
        initial_count = len(df)
        
        # Drop duplicates based on track_id
        df.drop_duplicates(subset=['track_id'], inplace=True)
        
        # Ensure numerical consistency (e.g., energy should be between 0 and 1)
        # We clip values just in case there are outliers
        df['energy'] = df['energy'].clip(0.0, 1.0)
        
        # Filter out invalid release years (e.g., future years or too old)
        df = df[(df['release_year'] >= 1900) & (df['release_year'] <= 2025)]
        
        print(f"[Info] Loaded {len(df)} tracks (Removed {initial_count - len(df)} duplicates/invalid).")
        return df
        
    except FileNotFoundError:
        print("[Error] File not found.")
        return None