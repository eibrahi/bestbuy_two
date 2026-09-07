from promotions import Promotion


class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, quantity, and active status."""
        self.promotion = None
        if name == "":
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Product price cannot be negative")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set the product quantity and deactivate it when quantity reaches zero."""
        self.quantity = quantity
        self.active = quantity > 0

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
        print(
            f"Name: {self.name}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )
        if self.promotion:
            print(f"Promotion: {self.promotion.name}")
    
    def set_promotion(self, promotion: Promotion) -> None:
        """Set the promotion for the product."""
        self.promotion = promotion

    def get_promotion(self) -> Promotion:
        """Return the promotion for the product."""
        return self.promotion

    def buy(self, quantity: int) -> float:
        """Buy a given quantity of the product and return the total price."""
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than the product's quantity")

        if not self.active:
            raise ValueError("Product is not active")

        self.set_quantity(self.quantity - quantity)

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        return total_price

class NonStockedProduct(Product):
    """Represents a non-stored product in the store."""
    def __init__(self, name, price):
        """Initialize a non-stored product with name, price, and 0 Stock."""
        super().__init__(name, price, 0)
        self.active = True

    def show(self) -> None:
        """Display the non-stored product name, price, and quantity."""
        print(
            f"Name: {self.name}, "
            f"Price: {self.price}"
        )
        if self.promotion:
            print(f"Promotion: {self.promotion.name}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        return total_price

class LimitedProduct(Product):
    """Represents a limited product in the store."""
    def __init__(self, name, price, quantity, maximum):
        """Initialize a limited product with name, price, quantity, and maximum quantity."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> None:
        """Display the limited product name, price, and quantity."""
        print(
            f"Name: {self.name}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}, "
            f"Maximum order: {self.maximum}"
        )
        if self.promotion:
            print(f"Promotion: {self.promotion.name}")

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise ValueError("Product is not active")

        if quantity > self.maximum:
            raise ValueError(f"Quantity {self.name} cannot be greater than the product's maximum quantity")

        if quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than the product's quantity")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.set_quantity(self.quantity - quantity)

        return total_price
