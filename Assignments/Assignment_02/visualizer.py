# File: visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
import os
import config

def plot_genre_distribution(df):
    """
    Task 4.1: Plot number of tracks per genre.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x='genre', data=df, palette='pastel')
    plt.title('Distribution of Tracks per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    
    save_path = os.path.join(config.PLOTS_DIR, 'genre_distribution.png')
    plt.savefig(save_path)
    plt.close()
    print(f"[Info] Saved genre distribution plot to {save_path}")

def plot_energy_vs_popularity(df):
    """
    Task 4.2: Scatter plot of Energy vs Popularity colored by Genre.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='energy', y='popularity', hue='genre', data=df, s=100, alpha=0.7)
    plt.title('Energy vs Popularity by Genre')
    plt.xlabel('Energy')
    plt.ylabel('Popularity')
    plt.grid(True)
    
    save_path = os.path.join(config.PLOTS_DIR, 'energy_vs_popularity.png')
    plt.savefig(save_path)
    plt.close()
    print(f"[Info] Saved energy vs popularity plot to {save_path}")