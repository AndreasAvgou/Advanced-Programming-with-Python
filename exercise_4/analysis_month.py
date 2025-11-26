# File: analysis_month.py
import matplotlib.pyplot as plt

def analyze_best_month(df):
    print("\n--- Analysis 1: Best Month ---")
    results = df.groupby('Month').sum(numeric_only=True)
    
    best_month = results['Sales'].idxmax()
    max_sales = results['Sales'].max()
    
    print(f"Best Month: {best_month}")
    print(f"Revenue: ${max_sales:,.2f}")

    # Plot
    months = range(1, 13)
    plt.figure(figsize=(10, 5))
    plt.bar(months, results['Sales'])
    plt.xticks(months)
    plt.xlabel('Month')
    plt.ylabel('Sales ($)')
    plt.title('Sales per Month')
    plt.show()