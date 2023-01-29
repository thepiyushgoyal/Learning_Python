import os
os.system('cls')
 
class A:
    def __init__(self):
        self.a = int(input("Enter a number: "))
    def showA(self):
        print(f"public var a = {self.a}")
 
class B:
    def __init__(self):
        self._b = int(input("Enter a number: "))
    def _showB(self):
        print(f"protected var b = {self._b}")
 
class C:
    def __init__(self):
        self.__c = int(input("Enter a number: "))
    def __showC(self):
        print(f"private var c = {self.__c}")

a1 = A()
b1 = B()
c1 = C()
print(a1.a)
print(b1._b)
print(c1._C__c)
a1.showA()
b1._showB()
c1._C__showC()