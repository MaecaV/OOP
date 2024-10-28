class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, func):
        def col(*args, **kwards):
            print("Introducing...")
            func(*args, **kwards)
            print("This character is amazing!")
        return col
        
naruto = AnimeCharacter("Naruto", "Shadow Clone Jutsu")

@naruto.introduce
def character_intro():
    print(f"I am {naruto.name} and I can use {naruto.ability}.")
    
character_intro()
