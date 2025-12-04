# File: main.py
import data_loader
import text_cleaner
import analyzer
import visualizer

def main():
    # Define the file to load
    FILENAME = "energy_tweets.csv" 
    # Use "energy_tweets_100.csv" if you want a smaller test first
    
    print("=== Tweet Analysis System ===")

    # 1. Load Data
    df = data_loader.load_tweets(FILENAME)
    if df is None:
        return

    # 2. Clean Data
    # Note: We check columns in data_loader, usually the text is in 'text'
    df = text_cleaner.process_tweets(df, text_column='text')

    # 3. Analyze Data
    print("\n--- Running Analysis ---")
    
    # A. Get Hashtags
    hashtag_counts = analyzer.extract_hashtags(df)
    print(f"Top 5 Hashtags: {hashtag_counts.most_common(5)}")
    
    # B. Get Word Frequency
    word_counts = analyzer.count_word_frequency(df)
    print(f"Top 5 Words: {word_counts.most_common(5)}")

    # 4. Visualize Results
    print("\n--- Generating Visualizations ---")
    
    # Plot Hashtags
    visualizer.plot_top_items(hashtag_counts, title="Trending Hashtags", color='green')
    
    # Plot Words
    visualizer.plot_top_items(word_counts, title="Most Common Words", color='skyblue')

    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()