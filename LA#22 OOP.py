class Party:
    def __init__(self, party_theme, pagkain):
        self.party_theme = party_theme
        self.pagkain = pagkain
    def foods(self):
        print(f"Party Theme: {self.party_theme}")
        print("Chicken, Ice_Cream, Spag")
        self.__special_dish()
    def __special_dish(self):
        print(f"My special dish ({self.pagkain})")
        
col = Party("Y", "Pizyum")
cole = Party("U", "Takoyum")
colet = Party("M", "Chocoyum")

col.foods()
print()
cole.foods()
print()
colet.foods()
