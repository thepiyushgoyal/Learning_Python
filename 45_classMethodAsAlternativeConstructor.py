import os
os.system('cls')
 
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    
    def showStudent(self):
        print(f"RollNo of {self.name} is {self.rollno}")

    @classmethod
    def CommaNdHyphenSeprator(cls,studentDetails,i):
        return cls(studentDetails.split(",")[i].split("-")[0][1:],studentDetails.split(",")[i].split("-")[1])

studentDetails = '''
jasbir-341,
piyush-409,
revanshu-414,
jaswinder-342,
Mohit-090,
sarbjeet-425
'''

for index in range(0,len(studentDetails.split(","))):
    obje = Student.CommaNdHyphenSeprator(studentDetails,index)
    obje.showStudent()




