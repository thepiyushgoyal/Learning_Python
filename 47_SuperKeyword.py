import os
os.system('cls')
 
class Marks:
    def __init__(self):
        self.marks = int(input("Enter your total Marks: "))
    def showDetails(self):
        print(f"Percentage obtained: {self.marks/5}%")
    
class Fees(Marks):
    def __init__(self):
        # We can here use the super keyword to call the parent class methods
        # if the function name is same or we have to call the constructor.
        super().__init__() 
        self.fees = int(input("Enter Your Paid fees: "))
    def showDetails(self):
        super().showDetails()
        print(f"Remaining Fees: ₹{100000 - self.fees}")

f = Fees()
f.showDetails()