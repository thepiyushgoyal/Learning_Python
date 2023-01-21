import os
os.system('cls')

x = 10   # Global variable
print("Global value: ",x)


def func():
    y = 3    # Local variable
    print("Local value: ",y)
    # x = 5  we can't change the global variable inside the function if we print it now out of this it will print 10 only
    # But there is a method to change the global variable inside the function - Not recomended
    global x
    x = 5

func()
print("Global value after changing in func: ",x)

# print(y)   can't print the local value outside its scope
