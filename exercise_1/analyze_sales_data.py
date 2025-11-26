import pandas as pd
import os

def analyze_sales_data(filename):
    """
    Loads sales data from a CSV file and performs basic analysis.
    """
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return

    print(f"--- Loading data from: {filename} ---\n")

    # 1. Load the data
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Display basic info
    print("Dataset Info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    print("-" * 40)

    # 2. Data Cleaning & Calculations
    # Ensure columns exist (assuming standard names based on the course context)
    # If columns are named differently (e.g., in Greek), we might need to rename them.
    # Here we assume standard names: 'Product', 'Price', 'Quantity'
    
    # Calculate 'Total Sales' for each row (Price * Quantity)
    if 'Price' in df.columns and 'Quantity' in df.columns:
        df['Total Sales'] = df['Price'] * df['Quantity']
        print("\nCalculated 'Total Sales' column:")
        print(df[['Product', 'Price', 'Quantity', 'Total Sales']].head())
    else:
        print("\nWarning: Columns 'Price' or 'Quantity' not found. Cannot calculate totals.")
        return

    print("-" * 40)

    # 3. Basic Analytics
    
    # A. Total Revenue
    total_revenue = df['Total Sales'].sum()
    print(f"\nTotal Revenue: {total_revenue:.2f}€")

    # B. Best Selling Product (by Quantity)
    if 'Product' in df.columns:
        best_selling = df.groupby('Product')['Quantity'].sum().idxmax()
        max_qty = df.groupby('Product')['Quantity'].sum().max()
        print(f"Best Selling Product (Quantity): {best_selling} ({max_qty} units)")

    # C. Most Valuable Product (by Total Sales revenue)
    if 'Product' in df.columns:
        most_valuable = df.groupby('Product')['Total Sales'].sum().idxmax()
        max_val = df.groupby('Product')['Total Sales'].sum().max()
        print(f"Highest Revenue Product: {most_valuable} ({max_val:.2f}€)")

    # 4. Export results (Optional)
    output_file = "sales_analysis_results.csv"
    df.to_csv(output_file, index=False)
    print(f"\nAnalysis saved to '{output_file}'.")

if __name__ == "__main__":
    # Ensure 'products_sales.csv' is in the same directory
    analyze_sales_data("products_sales.csv")