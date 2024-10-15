class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health = target.health - self.power
        print(f"({target.name}'s {target.health} HP has been damaged by {self.power} attack power.")
    
    def special_move(self, target):
        pass
   
    def defend(self, attacker):
        attacker.power = attacker.power - 50
        print("Shield on.")

class Warrior(Character):
    def special_move(self, target):
        target.health = target.health - self.power
        print(f"Warrior {self.name} uses Shield Bash on {target.name}! \n>> {target.name}'s health reduced by {self.power}. Total {target.name}'s HP: {target.health}")
        self.power = self.power * 2
        
class Mage(Character):
    def special_move(self, target):
        target.health = target.health - self.power
        print(f"Mage {self.name} casts Fireball on {target.name}! \n>> {target.name} HP - {self.power}. Total {target.name}'s HP: {target.health}")
        
class Archer(Character):
    def special_move(self, target):
        target.health = target.health - self.power
        print(f"Archer {self.name} shoots a Piercing Arrow on {target.name}! \n>> {target.name}'s health reduced by {self.power}. Total {target.name}'s HP: {target.health}")

class Monster(Character):
    def __init__(self, name, health, power, heal, target):
        super().__init__(name, health, power)
        self.heal = heal
        self.target = target
    
    def special_move(self, heal, target):
        target.health = target.health - self.power
        self.health += self.heal
        print(f"Monster {self.name} roared to {target.name}")
        print(f">> Monster {self.name} dealt {self.power} damage to {target.name} and gained {self.heal} health! Total {self.name}'s HP: {self.health}")

warriorAtk = Warrior("Colet", 1000, 150)
mageAtk = Mage("Jho", 700, 200)
archerAtk = Archer("Arc", 800, 120)
monsterAtk = Monster("Gwen", 900, 80, 50, 80)

for x in (warriorAtk, mageAtk, archerAtk):
    x.special_move(monsterAtk)
    
for targets in (warriorAtk, mageAtk, archerAtk):
    monsterAtk.special_move(monsterAtk, targets)
