import os
os.system('cls')
 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('Piyush',19)
print(p.__dict__)  # Dict method - it gives all the variables with their value in a dictinory

print("\n\n")

print(p.__dir__()) # Prints all the functions / methods that can be apply to a particular object

print("\n\n")

print(help(Person)) # print the details of that method