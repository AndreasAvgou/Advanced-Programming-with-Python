# File: sentiment_analyzer.py
from textblob import TextBlob
import pandas as pd

def get_polarity(text):
    """
    Calculates sentiment polarity using TextBlob.
    Returns a value between -1.0 (Negative) and 1.0 (Positive).
    """
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0.0

def add_sentiment_score(tweets_df):
    """
    Adds a 'polarity' column to the tweets DataFrame.
    """
    print("[Info] Calculating sentiment polarity for tweets...")
    tweets_df['polarity'] = tweets_df['text'].apply(get_polarity)
    return tweets_df