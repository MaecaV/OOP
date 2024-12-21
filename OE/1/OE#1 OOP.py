class ml:
    def __init__(self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
    
    def describe(self):
        print(f"{self.name} is a {self.role} hero with {self.dmg_type}")
        
    def __str__(self):
        return F"{self.name} is a {self.role} hero with {self.dmg_type}" 
    
marksman = ml("Hanabi", "marksman", "physical")
tank = ml("Johnson", "tank", "physical")
mage = ml("Cecelion", "mage", "magic")
fighter = ml("Alpha", "fighter", "physical")
support = ml("Angela", "mage", "magic")

marksman.describe()
tank.describe()
mage.describe()
fighter.describe()
support.describe()
        