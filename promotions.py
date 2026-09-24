from abc import ABC, abstractmethod


class Promotion(ABC):
    """Represent a base class for product promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    """Apply half price to every second product."""

    def apply_promotion(self, product, quantity):
        total = 0

        for i in range(quantity):
            if i % 2 == 0:
                total += product.price
            else:
                total += product.price / 2

        return total


class ThirdOneFree(Promotion):
    """Make every third product free."""

    def apply_promotion(self, product, quantity):
        total = 0

        for i in range(1, quantity + 1):
            if i % 3 != 0:
                total += product.price

        return total


class PercentDiscount(Promotion):
    """Apply a percentage discount to a product."""

    def __init__(self, name: str, percent: int):
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100 percent")

        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Calculate the total price after applying the promotion."""
        total = product.price * quantity
        discount = total * (self.percent / 100)
        return total - discount
