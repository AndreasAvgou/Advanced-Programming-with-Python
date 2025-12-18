# File: data_cleaner.py
import pandas as pd

def clean_tweets_data(df):
    """
    Removes tweets with empty or missing text.
    """
    initial_count = len(df)
    
    # Drop rows where 'text' is NaN or empty
    df = df.dropna(subset=['text'])
    df = df[df['text'].str.strip() != ""]
    
    print(f"[Info] Cleaned Tweets: Removed {initial_count - len(df)} empty rows.")
    return df

def clean_songs_data(df):
    """
    Fills missing numeric values in songs (e.g., energy) with the column mean.
    """
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Fill NaN values with the mean of the column
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    print("[Info] Cleaned Songs: Filled missing values with column means.")
    return df