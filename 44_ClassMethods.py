import os
os.system('cls')

class person:
    count = 0 # class variable
    gender = 'custom'
    def __init__(self,name):
        self.name = name
        person.count += 1
    def showPerson(self):
        print(f"Person number: {person.count}\nName: {self.name}\nGender: {self.gender}\n")
    # class method - It helps us to change the variable value for all instances not for single object
    # if not applying @classmethod then p1.changeGender('male') will only set the gender for p1 instance
    # but if we apply it will changes for p2 instance too. 
    @classmethod
    def changeGender(cls,setGender):
        cls.gender = setGender

p1 = person('Piyush')
p1.changeGender('male')
p1.showPerson()

p2 = person('Jasbir')
p2.showPerson()

p3 = person('laxmi')
p1.changeGender('female')
p3.showPerson()