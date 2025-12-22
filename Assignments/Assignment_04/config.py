# File: config.py
import os

# Configuration Settings
DATA_FILENAME = 'user_behavior_dataset.csv'
RESULTS_DIR = 'results'
PLOTS_DIR = os.path.join(RESULTS_DIR, 'plots')

# Model Settings
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Ensure output directories exist
def setup_directories():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(PLOTS_DIR, exist_ok=True)