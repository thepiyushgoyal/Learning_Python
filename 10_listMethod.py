import os
os.system('cls')
 
list = [i for i in range(10)]
# print(list)

list = [7,8,5,4,9,2,6,1,3,0]
print(list)

list.append(10)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

print(list.index(8))

print(list.count(8))

# list2 = list
list2 = list.copy()
list2[0] = 11
print(list)

list.insert(0,11)
print(list)

list.reverse()
list_2 = [12,13,14,15]
# list.extend(list_2)
print(list)

mergeList = list + list_2
print(mergeList)