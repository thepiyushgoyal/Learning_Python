import os
os.system('cls')
 
with open("32_seekg_tellg.txt","w") as f:
    f.write("Hello world")

with open("32_seekg_tellg.txt","r") as f:
    f.seek(6)
    print(f.read(5))

with open("32_seekg_tellg_2.txt","w") as f:
    f.write("Hello world")
    f.truncate(5)

with open("32_seekg_tellg_2.txt","r") as f:
    print(f.read())