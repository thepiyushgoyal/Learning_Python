import os
os.system('cls')
 
try:
    inp = int(input("Enter the index: "))
    arr = [1,2,3]
    print(arr[inp])
except ValueError:
    print("Please enter an Integer")
except IndexError:
    print("Index is not Present")
    
