# File: analysis_city.py
import matplotlib.pyplot as plt

def analyze_best_city(df):
    print("\n--- Analysis 2: Best City ---")
    results = df.groupby('City').sum(numeric_only=True)
    
    best_city = results['Sales'].idxmax()
    max_sales = results['Sales'].max()
    
    print(f"Top City: {best_city} (${max_sales:,.2f})")

    # Plot
    cities = [city for city, _ in df.groupby('City')]
    
    plt.figure(figsize=(10, 5))
    plt.bar(cities, results['Sales'])
    plt.xticks(cities, rotation='vertical', size=8)
    plt.xlabel('City')
    plt.ylabel('Sales ($)')
    plt.title('Sales per City')
    plt.show()