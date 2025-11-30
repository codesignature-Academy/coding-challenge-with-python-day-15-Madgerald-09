# Inherintance and Polymorphism
# Inheritance allows us to define a class that inherits all the methods of another class

# parent class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# # child class
# class Student(Person):
#     ...

# s1 = Student("john", 35)
# print(s1)

# Polymorphism refers to methods, functions, operators with the same name but can be executed in on so many objects or classes
# class Dog:
#     def __init__(self):
#         pass
    
#     def sound(self):
#         print("Whoof Whoof")
        
# class Cat:
#     def __init__(self):
#         pass
    
#     def sound(self):
#         print("Meow Meow")

# class Lion:
#     def __init__(self):
        
#         pass
    
#     def sound(self):
#         print("Roar")
        
# dog = Dog()
# cat = Cat()
# lion = Lion()

# for animal in [dog, cat, lion]:
#     animal.sound()

class User:
    def __init__(self, firstname,lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        
        
    def user_detail(self):
        print(
            self.firstname,
            self.lastname,
            self.email
        )
    
    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.email}"
    

user1 = User("john", "Mike", "admin@gmail.com")
print(user1)

user2 = User("Joel", "Abram", "admin@yahoo.com")
print(user2)

user3 = User("Smith", "Anderson", "admin@mail.com)
print(user3)
"""