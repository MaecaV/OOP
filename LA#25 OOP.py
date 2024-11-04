from abc import ABC, abstractmethod

class Ibon(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def lumilipad(self):
        pass

class Kalapati(Ibon):
    @property
    def lumilipad(self):
        return f"Ang {self.name} ay marunong lumipad!"
    
barako = Kalapati("Asul")
print(barako.lumilipad)

