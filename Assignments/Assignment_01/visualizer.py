# File: visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
import os
import config

def plot_daily_activity(df):
    """
    Task 4.1: Plot timeline of tweets per day.
    """
    # Group by date (day)
    daily_counts = df.groupby(df['date'].dt.date).size()
    
    plt.figure(figsize=(10, 5))
    daily_counts.plot(kind='line', marker='o', color='b')
    plt.title('Daily Tweet Activity')
    plt.xlabel('Date')
    plt.ylabel('Number of Tweets')
    plt.grid(True)
    
    save_path = os.path.join(config.PLOTS_DIR, 'daily_activity.png')
    plt.savefig(save_path)
    plt.close()
    print(f"[Info] Saved daily activity plot to {save_path}")

def plot_top_hashtags(trending_series):
    """
    Task 4.2: Plot bar chart of top hashtags.
    """
    plt.figure(figsize=(8, 6))
    sns.barplot(x=trending_series.values, y=trending_series.index, palette='viridis')
    plt.title('Top Trending Hashtags')
    plt.xlabel('Count')
    plt.ylabel('Hashtag')
    
    save_path = os.path.join(config.PLOTS_DIR, 'top_hashtags.png')
    plt.savefig(save_path)
    plt.close()
    print(f"[Info] Saved hashtag plot to {save_path}")