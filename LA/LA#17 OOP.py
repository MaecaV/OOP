class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power= atk_power
    
    def basic_attack(self, target):
        target.health -= self.atk_power
        target.health = max(0, target.health)
        print(f"{self.name} attacked {target.name}. {target.name}'s health is now {target.health}.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount} points. {self.name}'s health is now {self.health}.")

Granger = Player("Granger", 1500, 50)   
Jawhead = Player("Jawhead", 2500, 80)   

while Granger.health > 0 and Jawhead.health > 0:
    Jawhead.basic_attack(Granger)
    if Granger.health > 0:
       Granger.basic_attack(Jawhead)

if Granger.health == 0:
   print(f"{Granger.name} has been defeated. {Jawhead.name} wins!")  

else:
   print(f"{Jawhead.name} has been defeated. {Granger.name} wins!")  
  
Granger.heal(100)   
