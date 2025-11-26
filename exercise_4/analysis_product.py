# File: analysis_product.py
import matplotlib.pyplot as plt

def analyze_top_product(df):
    print("\n--- Analysis 3: Top Product ---")
    group = df.groupby('Product')
    qty_ordered = group['Quantity Ordered'].sum()
    
    best_product = qty_ordered.idxmax()
    print(f"Most Sold Product: {best_product}")

    # Plot
    products = [p for p, _ in group]
    
    plt.figure(figsize=(10, 6))
    plt.bar(products, qty_ordered)
    plt.xticks(products, rotation='vertical', size=8)
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.title('Most Sold Products')
    plt.show()