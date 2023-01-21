import os
os.system('cls')
 

# sets are unordered collection of data items, they store multiple
# values in single variable, just like list but without repeated values
s = {1,2,3,4,2} 
print(s)
new_s = {False, 9.3, 3, "Hello",3}
print(new_s)

# emptyset = {} # it is wrong because it is dict 
# to correct it we will do
emptyset = set()
print(type(emptyset))

for value in new_s:
    print(value)
    