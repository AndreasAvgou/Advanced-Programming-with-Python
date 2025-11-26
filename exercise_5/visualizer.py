# File: visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_prices(df):
    """
    Plots the historical prices of all coins over time.
    """
    plt.figure(figsize=(12, 6))
    for column in df.columns:
        plt.plot(df.index, df[column], label=column.capitalize())
    
    plt.title('Cryptocurrency Prices (Last 30 Days)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(corr_matrix):
    """
    Plots a heatmap of the correlation matrix.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
    plt.title('Correlation Matrix of Daily Returns')
    plt.tight_layout()
    plt.show()