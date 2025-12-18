# File: main.py
import data_loader
import data_cleaner
import sentiment_analyzer
import data_processor
import visualizer

def main():
    print("=== Music & Social Media Sentiment Analyzer ===")
    
    # 1. Load Data
    songs_df = data_loader.load_csv('songs.csv')
    tweets_df = data_loader.load_csv('tweets.csv')
    
    if songs_df is None or tweets_df is None:
        print("Exiting due to missing files.")
        return

    # 2. Clean Data
    songs_df = data_cleaner.clean_songs_data(songs_df)
    tweets_df = data_cleaner.clean_tweets_data(tweets_df)
    
    # 3. Sentiment Analysis
    tweets_df = sentiment_analyzer.add_sentiment_score(tweets_df)
    
    # Preview sentiment results
    print("\n--- Tweets with Sentiment (First 5) ---")
    print(tweets_df[['text', 'polarity']].head())

    # 4. Merge Data (Calculate Avg Sentiment per Song)
    final_df = data_processor.merge_datasets(songs_df, tweets_df)
    
    print("\n--- Final Merged Data (First 5) ---")
    print(final_df[['title', 'energy', 'danceability', 'avg_sentiment']].head())
    
    # 5. Check Correlations (Numeric output)
    print("\n--- Correlations ---")
    print(final_df[['energy', 'danceability', 'avg_sentiment']].corr())

    # 6. Visualize
    print("\n[Info] Generating plots...")
    visualizer.plot_sentiment_analysis(final_df)

if __name__ == "__main__":
    main()