from products import Product

class Store:
    """Represents a store with a list of products."""

    def __init__(self, products: list[Product]):
        """Initialize the store with a list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_all_products(self) -> list[Product]:
        """Return all active products in the store."""
        result = []
        for product in self.products:
            if product.active:
                result.append(product)
        return result

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Process an order and return the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        total = 0
        for product in self.products:
            total += product.quantity

        return total
