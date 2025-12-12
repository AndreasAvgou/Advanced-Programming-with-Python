# File: analyzer.py
import pandas as pd

def perform_descriptive_analysis(df):
    """
    Prints basic descriptive statistics and checks for correlations.
    """
    print("\n--- Descriptive Statistics ---")
    description = df.describe()
    print(description)
    return description

def analyze_correlations(df):
    """
    Calculates the correlation matrix for numeric audio features.
    """
    # Select only numeric columns (float/int)
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Drop 'track_id' if it exists as it's not an audio feature
    if 'track_id' in numeric_df.columns:
        numeric_df = numeric_df.drop(columns=['track_id'])
        
    corr_matrix = numeric_df.corr()
    return corr_matrix

def find_energy_correlations(corr_matrix):
    """
    Identifies which features are most strongly correlated with 'energy'.
    """
    print("\n--- Correlation with 'Energy' ---")
    if 'energy' in corr_matrix.columns:
        # Sort correlations descending
        energy_corr = corr_matrix['energy'].sort_values(ascending=False)
        print(energy_corr)
    else:
        print("[Warning] 'Energy' column not found.")

def calculate_average_scores(df):
    """
    Calculates the mean value for specific audio features.
    """
    # List of features to analyze
    features = ['danceability', 'energy', 'valence', 'tempo', 'liveness', 'acousticness', 'instrumentalness']
    
    # Filter only existing columns
    existing_features = [f for f in features if f in df.columns]
    
    means = df[existing_features].mean()
    print("\n--- Average Feature Scores ---")
    print(means)
    return means