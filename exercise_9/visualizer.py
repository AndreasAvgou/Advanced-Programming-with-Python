# File: visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_analysis(df):
    """
    Generates visualizations to analyze the relationship between 
    audio features and sentiment.
    """
    sns.set(style="whitegrid")
    
    # 1. Bar Chart: Average Sentiment per Song
    plt.figure(figsize=(10, 6))
    sns.barplot(x='title', y='avg_sentiment', data=df, palette='coolwarm')
    plt.title('Average Sentiment per Song')
    plt.xticks(rotation=45)
    plt.ylabel('Sentiment Polarity (-1 to 1)')
    plt.tight_layout()
    plt.show()

    # 2. Scatter Plot: Energy vs Sentiment
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='energy', y='avg_sentiment', data=df, s=100, color='red')
    plt.title('Correlation: Energy vs Sentiment')
    plt.xlabel('Energy')
    plt.ylabel('Average Sentiment')
    plt.grid(True)
    plt.show()

    # 3. Scatter Plot: Danceability vs Sentiment
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='danceability', y='avg_sentiment', data=df, s=100, color='blue')
    plt.title('Correlation: Danceability vs Sentiment')
    plt.xlabel('Danceability')
    plt.ylabel('Average Sentiment')
    plt.grid(True)
    plt.show()