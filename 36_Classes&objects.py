import os
os.system('cls')
 
class Person:
    def getPerson(self):
        self.name = input("Enter your Name: ")
        self.age = int(input("Enter your Age: "))
    def displayPerson(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

a = Person()
b = Person()
a.getPerson()
b.getPerson()
a.displayPerson()
b.displayPerson()