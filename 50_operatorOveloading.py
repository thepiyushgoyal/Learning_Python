import os
os.system('cls')
 
class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a} + {self.b}i"
    def __add__(self,obj):
        return complex(self.a+obj.a,self.b+obj.b)

c1 = complex(3,4)
print(f"  {c1}")
c2 = complex(5,2)
print(f"+ {c2}")
print(f"= {c1+c2}")