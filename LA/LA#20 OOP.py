class Chicken:
    def __init__(self, chicken, flour, salt):
        self.__chicken = chicken
        self.flour = flour
        self.salt = salt
    def __str__(self):
        return f"Ang ulam ko ay may {self.chicken}, {self.flour}, {self.salt}"
    def getter(self):
        return self.__chicken
nuggets = Chicken("chicken", "flour", "salt")
fried_chicken = Chicken("chicken", "flour", "salt")
chicken_skin = Chicken("joli_chicken", "flour", "salt")

print(chicken_skin.getter())
