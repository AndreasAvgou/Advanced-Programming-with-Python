# File: analytics.py
import pandas as pd

def get_basic_stats(df):
    """
    Task 2.1: Calculate basic user metrics.
    """
    stats = {
        'total_tweets': len(df),
        'unique_users': df['user_id'].nunique(),
        'total_likes': df['likes'].sum(),
        'total_retweets': df['retweets'].sum()
    }
    
    print("\n--- Basic Statistics ---")
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    return stats

def get_trending_hashtags(df, top_n=5):
    """
    Task 2.2: Identify trending behavioral patterns (hashtags).
    """
    trending = df['hashtag'].value_counts().head(top_n)
    
    print(f"\n--- Top {top_n} Trending Hashtags ---")
    print(trending)
    
    return trending