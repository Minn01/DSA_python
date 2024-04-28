import math


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle[radius={self.radius}])"

    def __str__(self):
        return f"Circle({self.radius})"


c1 = Circle(20)
print(c1)
print(c1.get_area())
print(c1.get_perimeter())

class Account:
    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id
        self.balance: int = 0

    def getBalance(self) -> int:
        return self.balance

    def setBalance(self, balance) -> None:
        self.balance = balance
    # -- other getters/setters/ methods --


