import os
os.system('cls')
 
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return f"Name: {self.name}\nId: {self.id}"
    def __repr__(self):
        return f"Employee('{self.name}',{self.id})"
    def __call__(self):
        print(self.__dict__)

e1 = Employee("Piyush",777)
print(repr(e1))
print(len(e1))
print(e1)
e1()
