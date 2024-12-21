class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describeSpiderman(self):
        print(f"Name: {self.name} Age: {self.age}")
        
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle  
        
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
man1 = Tobey("tobey maguire", 49, "Spiderman(July 2000)")
man2 = Andrew("andrew grafield", 41, "Spiderman(June 2012)")
man3 = Tom("tom holland", 28, "Spiderman(2017)")

print(f"{man1.name.upper()} {man1.movieTitle}")
print(f"{man2.name.upper()} {man2.movieTitle}")       
print(f"{man3.name.upper()} {man3.movieTitle}") 
