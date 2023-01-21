import os
os.system('cls')

def Sum():
    pass
 
def SumWithoutReturn(a,b):
    print("SumWithoutReturn :",a+b)
SumWithoutReturn(1,2)


def SumWithReturn(a=0,b=0):
    return a+b
s = SumWithReturn()
print("SumWithReturnDefault :",s)
s = SumWithReturn(2,3)
print("SumWithReturn :",s)
s = SumWithReturn(a=9)
print("SumWithReturnByPassingSingleValue :",s)


def SumUniversal(*nums):
    sum = 0
    for i in nums:
        sum = sum + i
    return sum
s = SumUniversal(1,2,3)
print("SumUniversal :",s)
