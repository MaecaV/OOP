class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    
    def describeAnimal(self):
        print(f"{self.name} has {self.type}")
    
class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim
        
fish = Fish("Goldfish", "Freshwater", True)
print(fish.can_swim)
