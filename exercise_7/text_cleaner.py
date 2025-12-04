# File: text_cleaner.py
import re

def clean_text(text):
    """
    Cleans a single string:
    1. Removes URLs (http...)
    2. Removes Mentions (@username)
    3. Removes special characters (except hashtags for analysis)
    4. Converts to lowercase
    """
    if not isinstance(text, str):
        return ""

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove mentions (@user)
    text = re.sub(r'@\w+', '', text)
    
    # Remove special characters/numbers (keep letters and # for now)
    text = re.sub(r'[^a-zA-Z#\s]', '', text)
    
    # Convert to lowercase and strip whitespace
    return text.lower().strip()

def process_tweets(df, text_column='text'):
    """
    Applies the cleaning function to the whole DataFrame.
    """
    print("--- Cleaning Data ---")
    if text_column not in df.columns:
        # Fallback: try to find a column that looks like 'text' or 'tweet'
        possible_cols = [c for c in df.columns if 'text' in c.lower() or 'tweet' in c.lower()]
        if possible_cols:
            text_column = possible_cols[0]
        else:
            print("[Error] Could not find a text column.")
            return df

    # Create a new column for clean text
    df['clean_text'] = df[text_column].apply(clean_text)
    print("[Success] Text cleaning complete.")
    return df