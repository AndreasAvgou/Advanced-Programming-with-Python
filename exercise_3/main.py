# File: main.py
from product import Product
from sale import Sale
from store_manager import StoreManager

def main():
    FILENAME = "sales_data.csv"
    manager = StoreManager()

    print("--- Store Management System (Product & Sale Classes) ---")
    manager.load_from_csv(FILENAME)

    while True:
        print("\nMenu:")
        print("1. View Sales Report")
        print("2. Add New Sale")
        print("3. Save & Exit")
        
        choice = input("Select option: ")

        if choice == '1':
            manager.print_report()
            
        elif choice == '2':
            print("\n--- New Transaction ---")
            # 1. Get Product Details
            name = input("Product Name: ")
            category = input("Category: ")
            
            # Validation
            while True:
                try:
                    price = float(input("Price per unit (€): "))
                    qty = int(input("Quantity: "))
                    if price < 0 or qty < 0:
                        print("Values must be positive.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Use numbers.")

            # 2. Create Objects
            # First create the Product
            new_product = Product(name, category, price)
            
            # Then create the Sale using that product
            new_sale = Sale(new_product, qty)
            
            # Add to manager
            manager.add_sale(new_sale)
            
        elif choice == '3':
            manager.save_to_csv(FILENAME)
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()