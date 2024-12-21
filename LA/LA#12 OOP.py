class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def describeToy(self):
        print(f"{self.name} has {self.price}")
        
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
        
car = Car("sonny_angels", "549")
car.describeToy()
