import os
os.system('cls')
 
name =  "piyush"
for i in name:
    print(i) # Printing words of string

colors = ["red","green","blue","yellow"]
for color in colors:
    print(color) # Printing strings in List
    for i in color:
        print(i)

for n in range(0,11,2):
    if(n == 4):
        continue # Continue statement....
    print(n) # Printing numbers
