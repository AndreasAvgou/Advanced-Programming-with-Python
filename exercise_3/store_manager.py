# File: store_manager.py
import csv
import os
from product import Product
from sale import Sale

class StoreManager:
    """Manages the collection of sales and file I/O."""

    def __init__(self):
        self.sales = []  # List of Sale objects

    def add_sale(self, sale):
        """Adds a sale to the list."""
        self.sales.append(sale)
        print(f"[Info] Sale for '{sale.product.name}' added successfully.")

    def get_grand_total(self):
        """Calculates the total revenue of the store."""
        return sum(s.get_total_cost() for s in self.sales)

    def load_from_csv(self, filename):
        """Loads data from CSV, recreating Product and Sale objects."""
        if not os.path.exists(filename):
            print(f"[Warning] File '{filename}' not found. Starting fresh.")
            return

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                count = 0
                for row in reader:
                    # CSV Format assumed: Name, Category, Price, Quantity
                    if len(row) < 4: continue
                    
                    name = row[0]
                    category = row[1]
                    price = row[2]
                    quantity = row[3]

                    # 1. Create the Product object first
                    prod = Product(name, category, price)
                    
                    # 2. Create the Sale object using the Product
                    sale = Sale(prod, quantity)
                    
                    self.sales.append(sale)
                    count += 1
            
            print(f"[Success] Loaded {count} sales from '{filename}'.")

        except Exception as e:
            print(f"[Error] Failed to load CSV: {e}")

    def save_to_csv(self, filename):
        """Saves the sales data back to CSV."""
        try:
            with open(filename, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Product", "Category", "Price", "Quantity"])
                
                for s in self.sales:
                    # Access data through the product object inside sale
                    writer.writerow([
                        s.product.name, 
                        s.product.category, 
                        s.product.price, 
                        s.quantity
                    ])
            
            print(f"[Success] Data saved to '{filename}'.")
        except Exception as e:
            print(f"[Error] Failed to save CSV: {e}")

    def print_report(self):
        """Prints the full sales report."""
        print("\n" + "="*75)
        print(f"{'STORE SALES REPORT':^75}")
        print("="*75)
        
        if not self.sales:
            print("No sales recorded.")
        else:
            for s in self.sales:
                print(s)  # Calls Sale.__str__
            
            print("-" * 75)
            print(f"GRAND TOTAL REVENUE: {self.get_grand_total():.2f}€")
        
        print("="*75 + "\n")