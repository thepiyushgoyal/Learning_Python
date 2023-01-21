import os
os.system('cls')

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
print("\n")

s3 = {1,2,3,4,5}
s4 = {4,5,6,7,8}
print(s3.intersection(s4))
s3.intersection_update(s4)
print(s3,s4)
print("\n")

s5 = {1,2,3,4,5}
s6 = {4,5,6,7,8}
print(s5.symmetric_difference(s6))
s5.symmetric_difference_update(s6)
print(s5,s6)
print("\n")

s7 = {1,2,3,4,5}
s8 = {4,5,6,7,8}
print(s7.difference(s8))
s7.difference_update(s8)
print(s7,s8)
print("\n")

s9 = {1,2,3,4,5}
s10 = {4,5}
print(s9.isdisjoint(s10))
print(s9.issuperset(s10))
print(s10.issubset(s9))
print("\n",s9)
s9.add(6)
print(s9)
s9.remove(6)# or 
# s9.discard(6)
print(s9)

c = {1,3,5,7,9}
item = c.pop()
print("\n",c)
print(item)
print("\n")

d = {12,34,56,78,90}
# del d
d.clear()
print(d)
