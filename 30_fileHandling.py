import os
os.system('cls')
 
f = open("30_fileHandling.txt","w")
f.write("Hey File has been created")
f.close()

f = open("30_fileHandling.txt","a")
f.write(" Text Appended")
f.close()

f = open("30_fileHandling.txt","r")
text = f.read()
print(text)
f.close()


with open("30_fileHandling_2.txt","w") as f:
    f.write("Hey File2 has been created")

with open("30_fileHandling_2.txt","a") as f:
    f.write(" Text Appended")
    
with open("30_fileHandling_2.txt","r") as f:
    text = f.read()
    print(text)
