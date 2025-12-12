# File: visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(corr_matrix):
    """
    Generates a heatmap of the correlation matrix.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap of Audio Features')
    plt.tight_layout()
    plt.show()

def plot_feature_means(means):
    """
    Generates a bar chart for the average scores of audio features.
    """
    plt.figure(figsize=(10, 6))
    
    # Create bar plot
    means.plot(kind='bar', color='#1DB954', edgecolor='black') # Spotify Green color
    
    plt.title('Average Score per Audio Feature')
    plt.ylabel('Mean Value')
    plt.xlabel('Feature')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()