import os
os.system('cls')

i = 1
while (i <= 10):
    
    print(i)
    i = i+1

j = int(input("Enter the Number 1-100: "))
while (j >= 0):
    print(j)
    j = j-1
else:
    print("Printed upto 0")

k = 0
while True:
    print(k)
    k = k+1
    if(k%10 == 0):
        break  #  Break statement....
