import os
os.system('cls')

index = 0
list = ['piyush', 'revanshu', 'jasbir']
for name in list:
    print(name)
    if (index == 2):
        print("No 2")
    index += 1

names = ['piyush', 'revanshu', 'jasbir']
for index, name in enumerate(names,start =1):
    print(name)
    if (index == 2):
        print("No 2")
