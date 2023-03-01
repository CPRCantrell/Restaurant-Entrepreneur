class Order:
    def __init__(self, dish_name, price) -> None:
        self.dish_name = dish_name
        self.price = price

class Pizza(Order):
    def __init__(self) -> None:
        super().__init__('Pizza', 10)

class Pasta(Order):
    def __init__(self) -> None:
        super().__init__('Pasta', 12)

class Salad(Order):
    def __init__(self) -> None:
        super().__init__('Salad', 6)