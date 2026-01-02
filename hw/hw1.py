class GameCharacter:
    def __init__(self, name, age, speed):
        self.name = name  
        self.age = age 
        self.speed = speed 
    
    def description(self):
        return f"Character's description: Name: {self.name}, Age: {self.age}, Speed: {self.speed}"
    
    def speedUp(self):
        return f"Speed increased (+200): {self.speed+200}"

GodOfWar = GameCharacter("Kratos", 1000, 400)
AssassinsCreed = GameCharacter("Altair", 25, 200)
print(GodOfWar.description())
print(AssassinsCreed.speedUp())

