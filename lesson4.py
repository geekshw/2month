# double underscore - dunder
# магические методы

from typing import Any


class ElecrtoCar:
    def __init__(self , power , battery):
        self.power = power
        self.battery = battery
    def info(self , value):
        print(f"Мошность - {self.power}  Vat \nЗаряд батареи - {self.battery }Mah - {value}")
    def __repr__(self):
        return f"Мошность - {self.power}  Vat \nЗаряд батареи - {self.battery} - это метод repr"
    def __str__(self):
        return f"Мошность - {self.power}  Vat \nЗаряд батареи - {self.battery} - это метод str"
    def __call__(self) :
        print("Hello world!")
    def __call__(self , a ,b):
        print(a + b)
car = ElecrtoCar(120 , 20000)
# car.info(12)
# car.add(1,2)
print(car)
print("HEllo World!")
car()

