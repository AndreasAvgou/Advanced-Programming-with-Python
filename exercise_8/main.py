# File: main.py
import data_loader
import analyzer
import visualizer

def main():
    # Ensure this matches your uploaded file name
    FILENAME = "data.csv"
    
    print("=== Spotify Data Analysis Tool ===")

    # 1. Load Data
    df = data_loader.load_data(FILENAME)
    if df is None:
        return

    # 2. Analyze Data
    # A. Basic Description
    analyzer.perform_descriptive_analysis(df)
    
    # B. Correlations
    corr_matrix = analyzer.analyze_correlations(df)
    
    # C. Specific check for 'energy'
    analyzer.find_energy_correlations(corr_matrix)
    
    # D. Calculate Means
    means = analyzer.calculate_average_scores(df)

    # 3. Visualize Data
    print("\n[Info] Generating Visualizations...")
    
    # Heatmap
    visualizer.plot_correlation_heatmap(corr_matrix)
    
    # Bar Chart
    visualizer.plot_feature_means(means)

    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()