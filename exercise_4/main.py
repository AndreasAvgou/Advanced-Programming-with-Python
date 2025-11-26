# File: main.py
# Import all our custom modules
import data_loader
import feature_engineering
import analysis_month
import analysis_city
import analysis_product

def main():
    FILENAME = 'sales_data.csv'
    
    print("=== STARTING MODULAR ANALYSIS ===")

    # 1. Load Data
    df = data_loader.load_and_clean_data(FILENAME)
    if df is None: return

    # 2. Add Features
    df = feature_engineering.add_features(df)

    # 3. Run Analyses
    analysis_month.analyze_best_month(df)
    analysis_city.analyze_best_city(df)
    analysis_product.analyze_top_product(df)

    print("\n=== ALL ANALYSES COMPLETE ===")

if __name__ == "__main__":
    main()