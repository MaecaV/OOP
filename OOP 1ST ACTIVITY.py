class hero():
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg ):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
        
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"
       
       
hero_mm1 = hero("Miya", "Marksman", "physical attack" , 100, 50)
hero_fighter1 = hero("Jawhead", "Fighter", "physical damage", 100, 30)
hero_tank1 = hero("Johnson", "Tank", "Physical/magic defense", 150, 20)
hero_jungler1 = hero("Karina", "Jungler", "Physical burst",200, 20 )
hero_mage1 = hero("Cecelion", "Mage", "Magic damage",100, 60)

print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health} HP
{hero_fighter1.auto_atk_dmg} basic attack damage
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}

{hero_tank1.name}
{hero_tank1.role}
{hero_tank1.health} HP
{hero_tank1.auto_atk_dmg} basic attack damage
{hero_tank1.dmg_type}
{hero_tank1.describe()}

{hero_jungler1.name}
{hero_jungler1.role}
{hero_jungler1.health} HP
{hero_jungler1.auto_atk_dmg} basic attack damage
{hero_jungler1.dmg_type}
{hero_jungler1.describe()}

{hero_mage1.name}
{hero_mage1.role}
{hero_mage1.health} HP
{hero_mage1.auto_atk_dmg} basic attack damage
{hero_mage1.dmg_type}
{hero_mage1.describe()}
''')