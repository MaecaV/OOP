class hero:
    def __init__(self, name):
        self.name = name

    def describe(self, role):
        print(f"{self.name} is a {role} hero.")

ml = hero("Miya")
ml.describe("Marksman")
