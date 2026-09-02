class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, quantity, and active status."""
        if name == "":
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Product price cannot be negative")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set the product quantity and deactivate it when quantity reaches zero."""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Return whether the product is currently active."""
        return self.active

    def activate(self) -> None:
        """Activate the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the product."""
        self.active = False

    def show(self) -> None:
        """Display the product name, price, and quantity."""
        print("Name: " + self.name)
        print("Price: " + str(self.price))
        print("Quantity: " + str(self.quantity))

    def buy(self, quantity: int) -> float:
        """Buy a given quantity of the product and return the total price."""
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than the product's quantity")

        if not self.active:
            raise ValueError("Product is not active")

        self.quantity -= quantity
        return quantity * self.price
