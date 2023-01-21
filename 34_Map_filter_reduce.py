import os
os.system('cls')
 
n = [i for i in range(1,51)]
print(n,"\n")

# Map....
nSquare = list(map(lambda x:x*x , n))
print(nSquare,"\n") # map will take all value from list and apply the func and return

# Filter
nSquareEven = list(filter(lambda x:x%2==0, nSquare))
print(nSquareEven,"\n") # Filtered the value from a list and return ,it takes the func that return boolean

# Reduce
from functools import reduce
nSquareEvenSum = reduce(lambda x,y:x+y, nSquareEven)
print(nSquareEvenSum,"\n") # reduce take the value and pass to the func and return single value
