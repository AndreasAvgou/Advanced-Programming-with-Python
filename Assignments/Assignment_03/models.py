# File: models.py
import pandas as pd
import numpy as np

class Asset:
    """
    Task 3.1: Asset Class representing a single financial instrument.
    """
    def __init__(self, ticker, data):
        self.ticker = ticker
        self.data = data.sort_values('date') # Ensure sorted history
        self.prices = self.data['price'].values
        
    def get_average_return(self):
        # Calculate daily percentage change
        returns = self.data['price'].pct_change().dropna()
        return returns.mean()
    
    def get_risk(self):
        # Risk is standard deviation of returns
        returns = self.data['price'].pct_change().dropna()
        return returns.std()

    def __str__(self):
        return f"Asset({self.ticker})"

class Portfolio:
    """
    Task 3.1: Portfolio Class to manage multiple assets.
    """
    def __init__(self):
        self.assets = {} # Dict of ticker -> Asset object

    def add_asset(self, asset):
        self.assets[asset.ticker] = asset

    def calculate_portfolio_risk(self, weights=None):
        """
        Calculates portfolio risk assuming equal weights if not provided.
        (Simplified version assuming zero correlation for this exercise level, 
         or just weighted avg of std dev for simplicity).
        """
        if not weights:
            # Equal weights
            n = len(self.assets)
            weights = {ticker: 1.0/n for ticker in self.assets}
        
        total_risk = 0
        for ticker, asset in self.assets.items():
            total_risk += weights[ticker] * asset.get_risk()
            
        return total_risk

    def optimize_weights(self):
        """
        Task 3.2: Find optimal investment weights.
        Simple Heuristic: Inverse Volatility Weighting (Low risk -> High weight).
        """
        risks = {t: a.get_risk() for t, a in self.assets.items()}
        total_inverse_risk = sum(1/r for r in risks.values() if r > 0)
        
        weights = {}
        for ticker, r in risks.items():
            if r > 0 and total_inverse_risk > 0:
                weights[ticker] = (1/r) / total_inverse_risk
            else:
                weights[ticker] = 0
                
        return weights