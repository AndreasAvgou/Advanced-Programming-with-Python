# File: analytics.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import config

def analyze_user_behavior(df):
    """
    Task 2.1: Basic metrics and correlations.
    """
    print("\n--- User Behavior Analytics ---")
    
    # Calculate Conversion Rate (Purchases per Session)
    df['conversion_rate'] = df['purchases'] / df['sessions']
    df['conversion_rate'] = df['conversion_rate'].fillna(0) # Handle division by zero
    
    avg_conv = df['conversion_rate'].mean()
    print(f"Average Conversion Rate: {avg_conv:.4f} purchases/session")
    
    return df

def compare_churn_groups(df):
    """
    Task 2.2: Compare behavioral patterns between Churned (1) and Active (0) users.
    """
    print("\n--- Churned vs Active Users Comparison ---")
    comparison = df.groupby('churned')[['sessions', 'avg_session_time', 'purchases', 'last_active_days']].mean()
    print(comparison)
    
    return comparison

def plot_correlation_matrix(df):
    """
    Visualizes correlations between features.
    """
    plt.figure(figsize=(10, 8))
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Feature Correlation Matrix')
    
    save_path = os.path.join(config.PLOTS_DIR, 'correlation_matrix.png')
    plt.savefig(save_path)
    plt.close()
    print(f"[Info] Saved correlation matrix to {save_path}")