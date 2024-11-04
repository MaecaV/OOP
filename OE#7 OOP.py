class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def col():
           print("Introducing...")
           func()
           print("This character is amazing!")
        return col   
    
nina = TekkenCharacter("Nina", "Fatal Judgement")

@nina.introduce
def character_intro():
    print(f"I am {nina.name} and I can use {nina.ability}.")

character_intro()
