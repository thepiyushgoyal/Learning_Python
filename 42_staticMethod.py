import os
os.system('cls')
 
class calc:
    def __init__(self):
        self.num1 = int(input("Enter 1st Number: "))
        self.num2 = int(input("Enter 2nd Number: "))
    @staticmethod
    def sum(num1,num2):
        return num1 + num2

    def sub(self):
        return (self.num1 - self.num2)
    
r = calc()
print(f"sub: {r.sub()}")
print(f"Sum of 2 and 3: {r.sum(2,3)}")