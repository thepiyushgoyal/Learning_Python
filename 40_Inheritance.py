import os
os.system('cls')
 
class Marks:
    def getMarks(self):
        self.marks = int(input("Enter your total Marks: "))
    def showMarks(self):
        print(f"Percentage obtained: {self.marks/5}%")
    
class Fees(Marks):
    def __init__(self):
        self.fees = int(input("Enter Your Paid fees: "))
    def showFees(self):
        print(f"Remaining Fees: ₹{100000 - self.fees}")

f = Fees()
f.getMarks()
f.showFees()
f.showMarks()