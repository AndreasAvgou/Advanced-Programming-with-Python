# File: sale.py
from product import Product  # Import the Product class

class Sale:
    """Represents a sale transaction containing a Product and Quantity."""

    def __init__(self, product, quantity):
        self.product = product  # This is a Product object
        self.quantity = int(quantity)

    def get_total_cost(self):
        """Calculates total cost based on product price and quantity."""
        return self.product.price * self.quantity

    def __str__(self):
        """Returns a formatted string for the sale details."""
        total = self.get_total_cost()
        # Access attributes via self.product
        return (f"Product: {self.product.name:<15} | "
                f"Category: {self.product.category:<12} | "
                f"Qty: {self.quantity:<3} | "
                f"Price: {self.product.price:<6.2f}€ | "
                f"Total: {total:<8.2f}€")