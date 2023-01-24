import os
os.system('cls')
 
class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
    def showData(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Piyush","Web Developer")
a.showData()