# class Car:
#     def __init__(self, wheels, sideMirror, doors):
#         self.wheels = wheels
#         self.sideMirror = sideMirror
#         self.doors = doors
    
#     def details(self):
#         print(f"Wheels = {self.wheels}\nSide Mirror = {self.sideMirror}\nDoors = {self.doors}")
        
    
# car1 = Car(4, 2, 6)
# car1.details()

# car2 = Car(5, 3, 4)
# car2.details()


"""
create a Dog class
using the constructor accept name, age,strength=10
create a method play - 1, sleep + 1, eat + 3
if strength is < 5 print(weak) elif strength >= 7 tired else strong
"""
class Dog:
    def __init__(self, name, age, strength=10):
        self.name = name
        self.age = age
        self.strength = strength
        
    def play(self):
        if self.strength > 1:
            self.strength -= 1
    
    def sleep(self):
        if self.strength != 10:
            self.strength += 1
    
    def eat(self):
        if self.strength <= 7:
            self.strength += 3
            
    def check_strength(self):
        if self.strength < 5:
            print(f"{self.name} is Weak \nStrength {self.strength}")
        elif self.strength <= 7:
            print(f"{self.name} is Tired\nStrength {self.strength}")
        else:
            print(f"{self.name} is Strong\nStrength {self.strength}")
            
dog1 = Dog("Bruno", 3)
dog1.play()
dog1.play()
dog1.play()

dog1.eat()
dog1.check_strength()

dog2 = Dog("Rocky", 5)
dog2.play()
dog2.play()
dog2.play()
dog2.play()

