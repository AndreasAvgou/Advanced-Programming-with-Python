# File: main.py
import config
import data_loader
import analytics
import models
import ml_prediction

def main():
    print("=== Assignment 4: User Behavior Analysis & Churn Prediction ===")
    
    config.setup_directories()
    
    # --- TASK 1: Dataset Handling ---
    df = data_loader.load_and_clean_data(config.DATA_FILENAME)
    if df is None: return

    # --- TASK 2: Advanced Analytics ---
    df = analytics.analyze_user_behavior(df)
    analytics.compare_churn_groups(df)
    analytics.plot_correlation_matrix(df)

    # --- TASK 3: OOP Architecture (User Profiling) ---
    print("\n--- OOP User Profiling ---")
    user_base = models.UserBase()
    user_base.load_users(df)
    
    # Calculate statistics via OOP
    churn_rate = user_base.get_churn_rate()
    print(f"Overall Churn Rate (OOP): {churn_rate:.2f}%")
    
    high_value = user_base.get_high_value_users(min_purchases=15)
    print(f"High Value Users (>15 purchases): {len(high_value)}")
    if high_value:
        print(f"Sample High Value User: {high_value[0]}")

    # --- TASK 4: Machine Learning (Churn Prediction) ---
    ml_prediction.train_churn_model(df)
    
    print("\n=== Execution Complete ===")

if __name__ == "__main__":
    main()