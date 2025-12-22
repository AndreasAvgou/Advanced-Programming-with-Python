# File: main.py
import config
import data_loader
import analytics
import models
import visualizer

def main():
    print("=== Assignment 1: Twitter Trend Analysis Platform ===")
    
    # Setup directories
    config.setup_directories()
    
    # --- TASK 1: Dataset Handling ---
    df = data_loader.load_and_clean_data(config.DATA_FILENAME)
    if df is None:
        return

    # --- TASK 2: Feature Extraction (Analytics) ---
    analytics.get_basic_stats(df)
    trending_hashtags = analytics.get_trending_hashtags(df)

    # --- TASK 3: OOP Architecture (User Profiling) ---
    print("\n--- OOP User Analysis ---")
    user_manager = models.UserManager(df)
    
    # Get top 3 active users
    top_users = user_manager.get_most_active_users(3)
    print("Most Active Users (User ID -> Tweet Count):")
    print(top_users)
    
    # Demonstrate Tweet Class creation for the first row
    first_row = df.iloc[0]
    tweet_obj = models.Tweet(first_row['tweet_id'], first_row['user_id'], first_row['text'], first_row['likes'])
    print(f"\nSample Object: {tweet_obj}")

    # --- TASK 4: Visualization ---
    print("\n--- Generating Plots ---")
    visualizer.plot_daily_activity(df)
    visualizer.plot_top_hashtags(trending_hashtags)
    
    print("\n=== Execution Complete ===")

if __name__ == "__main__":
    main()