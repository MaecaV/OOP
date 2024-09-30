class Cat:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Meow!")
        
class Bird:
    def __init__(self, name):
        self.name = name
      
    def speak(self):
        print("Chirp!")
        
class Fish:
    def __init__(self, name):
        self.name = name
      
    def speak(self):
        print("...")


dog = Dog("Chichi")
cat = Cat("Colet")
bird = Bird("Jho")
fish = Fish("Gwen")

for animal in [dog, cat, bird, fish]:
    animal.speak()
