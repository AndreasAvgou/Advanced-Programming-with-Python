# File: product.py

class Product:
    """Represents a product in the store."""

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = float(price)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price:.2f}€"