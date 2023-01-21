import os
os.system('cls')

cube = lambda x:  x*x*x

def sum(cube, value, res=0):
    for digit in value:
        res = res + cube(int(digit))
    return res

x = input("Enter a Number: ")
print("Sum of cube of Numbers: ",sum(cube,x,0))