class Phone():
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model
    
    def describePhone(self):
        print(f"{self.brand} has {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

cp = Android("Realme", "C67")
cp.describePhone()
