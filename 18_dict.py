import os
os.system('cls')
 
info = {'name':'Piyush', 'age':19, 'eligible':True}
print(info)
for i in info:
    print(i)
print(info['name'])

print(info.get('name'))

print(info.values())

print(info.keys())
for key in info.keys():
   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 