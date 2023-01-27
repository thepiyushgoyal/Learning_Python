import os
os.system('cls')
 
class calc:

    # A Constructor
    def __init__(self,val1,val2):
        self.a = val1
        self.b = val2

    # showVals func to display the values
    def showPossibleCase(self):
        print(f"\tPossible Case: {self.a} and {self.b}")

    def showVals(self):
        print(f"\tValue 1: {self.a}")
        print(f"\tValue 2: {self.b}")

    # a getter which get the sum of vals
    @property
    def add(self):
        return self.a + self.b
    
    # a getter which get the sub of vals
    @property
    def sub(self):
        return self.a - self.b
    
    # a getter which get the mul of vals
    @property
    def mul(self):
        return self.a * self.b
    
    # a getter which get the div of vals
    @property
    def div(self):
        return self.a / self.b

    @add.setter
    def add(self,addVal):
        for i in range(0,addVal):
            for j in range(addVal - i,addVal - i +1):
                self.a = i
                # obj.showVal1()
                self.b = j
                obj.showPossibleCase()

    @div.setter
    def div(self,divVal):
        for i in range(divVal,divVal+1):
            for j in range(1,divVal+1):
                if(i%j == 0):
                    self.a = i
                    self.b = j
                    obj.showPossibleCase()

    @mul.setter
    def mul(self,mulVal):
        for i in range(1,mulVal+1):
            for j in range(mulVal, 0, -1):
                if(i*j == mulVal):
                    self.a = i
                    self.b = j
                    obj.showPossibleCase()
                    break

    # A setter which sets the new val for val1
    @property
    def newVal1(self):
        pass
    @newVal1.setter
    def newVal1(self,new_val1):
        self.a = new_val1
    
    # A setter which sets the new val for val2
    @property
    def newVal2(self):
        pass
    @newVal2.setter
    def newVal2(self,new_val2):
        self.b = new_val2

# calls
obj = calc(20,10)
obj.showVals()
print("Sum: ",obj.add)
print("Sub: ",obj.sub)
print("Mul: ",obj.mul)
print("Div: ",obj.div)

obj.newVal1 = 60
obj.newVal2 = 40
obj.showVals()
print("Sum: ",obj.add)
print("Sub: ",obj.sub)
print("Mul: ",obj.mul)
print("Div: ",obj.div)

obj.add = 3
print("\n")
obj.mul = 100
print("\n")
obj.div = 100