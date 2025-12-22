# File: config.py
import os

# Configuration Settings
DATA_FILENAME = 'twitter_dataset.csv'
RESULTS_DIR = 'results'
PLOTS_DIR = os.path.join(RESULTS_DIR, 'plots')

# Ensure output directories exist
def setup_directories():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    os.makedirs(PLOTS_DIR, exist_ok=True)
