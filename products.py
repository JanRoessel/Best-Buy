class Product:
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return bool(self.active)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if not self.is_active():
            raise Exception(f"{self.name} is not available for purchase.")
        if quantity > self.quantity:
            raise Exception(f"Not enough stock. Only {self.quantity} items available.")

        self.set_quantity(self.quantity - quantity)
        return self.price * quantity


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        pass  # Quantity must always stay 0 — ignore any changes

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        return self.price * quantity

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: Unlimited")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        if quantity > self.maximum:
            raise Exception(f"Cannot purchase more than {self.maximum} of '{self.name}' per order.")
        return super().buy(quantity)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}")

if __name__ == "__main__":
    main()