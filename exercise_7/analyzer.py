# File: analyzer.py
import pandas as pd
from collections import Counter

def extract_hashtags(df):
    """
    Extracts all hashtags from the 'clean_text' column.
    """
    all_hashtags = []
    
    for tweet in df['clean_text']:
        words = tweet.split()
        for word in words:
            if word.startswith('#') and len(word) > 1:
                all_hashtags.append(word)
                
    return Counter(all_hashtags)

def count_word_frequency(df):
    """
    Counts the frequency of all words (excluding common stop words).
    """
    all_words = []
    # Basic list of stop words to ignore
    stop_words = {'the', 'to', 'and', 'of', 'a', 'in', 'is', 'for', 'on', 'with', 'rt', 'this', 'http', 'https'}
    
    for tweet in df['clean_text']:
        # Remove hashtags for word count
        words = tweet.replace('#', '').split()
        for word in words:
            if word not in stop_words and len(word) > 2:
                all_words.append(word)
                
    return Counter(all_words)