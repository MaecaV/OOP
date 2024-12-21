class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Ford", "Black")
print(car1.brand, car1.color)

car2 = Car("Honda", "White")
print(car2.brand, car2.color)

car1.color = "Green"
print(car1.brand, car1.color)

car2.color = "Blue"
print(car2.brand, car2.color)

