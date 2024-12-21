class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating")

    def info(self):
        print(f"The {self.brand} is a model {self.model}")

class WashingMachine(Appliance):
    def __init__(self, name, model):
        super().__init__(name, model)
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def __init__(self, name, model):
        super().__init__(name, model)
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def __init__(self, name, model):
        Appliance.__init__(self, name, model)
    def operate(self):
        print("Heating food!")

washingmachine = WashingMachine("WashingMachine", "Samsung")
refrigerator = Refrigerator("Refrigerator", "Samsung")
microwave = Microwave("Microwave", "Samsung")

for appliance in [washingmachine, refrigerator, microwave]:
    appliance.operate()

washingmachine.info()
refrigerator.info()
microwave.info()
