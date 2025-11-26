# File: data_processor.py
import pandas as pd

def calculate_daily_returns(df):
    """
    Calculates the percentage daily returns.
    Formula: (Price_t - Price_t-1) / Price_t-1
    """
    # pct_change() computes the percentage change from the immediately previous row
    returns = df.pct_change().dropna()
    return returns

def calculate_volatility(returns_df):
    """
    Calculates the volatility (Standard Deviation) for each coin.
    """
    volatility = returns_df.std()
    return volatility

def calculate_correlation(returns_df):
    """
    Calculates the Pearson correlation matrix between the coins.
    """
    correlation_matrix = returns_df.corr(method='pearson')
    return correlation_matrix