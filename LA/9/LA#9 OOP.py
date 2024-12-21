class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"
car1 = Car("Honda")
print(car1)

del car1
#print(car1)
        
