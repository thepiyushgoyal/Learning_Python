import os
os.system('cls')

age = int(input("Enter your age: "))
print("Your age is : ", age)
if (age >= 18):
    print("you can drive")
elif (age > 0 and age < 18):
    print("You can't drive")
else:
    print("Invalid age")
