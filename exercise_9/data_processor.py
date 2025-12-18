# File: data_processor.py
import pandas as pd

def merge_datasets(songs_df, tweets_df):
    """
    1. Calculates average sentiment per song_id from tweets.
    2. Merges this data with the songs DataFrame.
    """
    # Group tweets by song_id and calculate mean polarity
    avg_sentiment = tweets_df.groupby('song_id')['polarity'].mean().reset_index()
    avg_sentiment.rename(columns={'polarity': 'avg_sentiment'}, inplace=True)
    
    # Merge with songs data
    # Use 'inner' join to keep only songs that have tweets
    merged_df = pd.merge(songs_df, avg_sentiment, on='song_id', how='inner')
    
    print(f"[Success] Merged datasets. Resulting DataFrame has {len(merged_df)} songs.")
    return merged_df