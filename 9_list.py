import os
os.system('cls')

rollno = [401, 402, 403, 404, 405, 406, 407, 408, 409, 410]
print(rollno)

# Positive indexing...
print(rollno[0])
print(rollno[1])
print(rollno[2])
print(rollno[3])
print(rollno[4])
# Negitive indexing...
print(rollno[-5])
print(rollno[-4])
print(rollno[-3])
print(rollno[-2])
print(rollno[-1])

if 405 in rollno:
    print("405 is present.")
else:
    print("405 is absent.")

# Range of Index:
# You can print a range of list items by specifying where you want to start,
#  where do you want to end and if you want to skip elements in between the range.
# Syntax:
# listName[start : end : jumpIndex]

print(rollno[:])
print(rollno[0:])
print(rollno[:11])
print(rollno[5:])
print(rollno[5:11])
print(rollno[-5:])# Negitive...
print(rollno[::2])
print(rollno[1::2])


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)