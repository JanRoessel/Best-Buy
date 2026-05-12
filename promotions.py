from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        # Every pair: 1 full price + 1 half price = 1.5x
        # Odd item left over pays full price
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * 1.5 + remainder) * product.price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        # Every 3 items: pay for 2
        paid = quantity - (quantity // 3)
        return paid * product.price