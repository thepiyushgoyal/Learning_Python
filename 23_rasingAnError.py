import os
os.system('cls')
 
inp = input("Enter a number from 1 to 10: ")
if(inp != 'quit'):
    if(int(inp)>10 or int(inp)<1):
        raise ValueError("Enter Number from 1 to 10")
print("Done")