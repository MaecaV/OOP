class hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

character_ml = hero("Johnson", "Tank")
print(character_ml.name, character_ml.role)