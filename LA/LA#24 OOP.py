from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name
    @abstractmethod
    def attack(self):
        pass
class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")
class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")
class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")
    
        
col = Warrior("Col")
cole = Mage("Cole")
colet = Archer("Colet")

col.attack()
cole.attack()
colet.attack()
