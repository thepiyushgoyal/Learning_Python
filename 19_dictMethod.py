import os
os.system('cls')

data1 = {1: 90,
         2: 80,
         3: 70,
         4: 60,
         5: 40}

data2 = {6: 91,
         7: 71,
         8: 81,
         9: 61,
         10: 41}

sample = {100: 1,
          200: 2}

print("Data of collection 1: ", data1)
print("Data of collection 2: ", data2)
data1.update(data2) # Combine the data of 2nd into first
print("Updated Data : ", data1)

data2.pop(6) # It will pop he value which we will pass
print("poped Data: ", data2)
data2.popitem() # It will pop the last value
print("poped Data: ", data2)

del sample
# print(sample) # It will give an error as it has been deleted
del data2[7]
print("Data after deleting: ", data2)