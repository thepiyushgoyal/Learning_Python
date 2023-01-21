import os
os.system('cls')

x = int(input("Enter a number: "))
match x:
    case 0:
        print("Number is 0 and even")
    case _ if x % 2 == 0:
        print("Number is even")
    case _:
        print("Number is Odd")
