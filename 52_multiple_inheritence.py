import os
os.system('cls')
 
class Subject:
    def __init__(self,sub):
        self.sub = sub
    def show(self):
        print(f"Subject: {self.sub}")
    
 
class Sport:
    def __init__(self,spo):
        self.spo = spo
    def show(self):
        print(f"Sport:   {self.spo}\n")
    
class Student(Subject,Sport):
    def __init__(self,name,sub,spo):
        self.name = name
        self.sub = sub
        self.spo = spo
    def show(self):
        print(f"Name:    {self.name}")
        super().show()
        Sport.show(self)

st1 = Student('Piyush','Python','Pool')
st1.show()
st2 = Student('Jasbir','Javascript','javlien')
st2.show()
