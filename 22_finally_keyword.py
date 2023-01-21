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
finally:
    print("Try Except block run successfuly")    

# if we will simply print any line after try and except block it will always run
# then why we use finally keyword for example the code below:-

def func():
    try:
        inp = int(input("Enter the index: "))
        arr = [1,2,3]
        print(arr[inp])
        return 1  # it will return the value and will move out but after executing finally block
    except ValueError:
        print("Please enter an Integer")
        return 0 # it will return the value and will move out but after executing finally block
    except IndexError:
        print("Index is not Present")
        return -1 # it will return the value and will move out but after executing finally block
    finally:
        print("Try Except block run successfuly")    

f = func()
print(f)