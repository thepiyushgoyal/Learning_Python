import os
os.system('cls')


def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)


print("Factorial of 4 :", fact(4))


def fab(index):
    if (index == 0):
        return 0
    elif (index == 1 or index == -1):
        return 1
    elif(index > 1):
        return fab(index-1) + fab(index-2)
    else:
        return fab(index + 2) - fab(index + 1)

userfab = int(input("Enter the index to find fabonacci value : "))
print(f"Fabonacci for index {userfab} is : ",fab(userfab))
print("Fabonacci series")
if(userfab>=0):
    for series in range(0,userfab+1):
        print(fab(series),end=" ")
else:
    for series in range(userfab,1):
        print(fab(series),end=" ")