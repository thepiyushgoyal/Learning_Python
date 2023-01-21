import os
os.system('cls')
 

names="Piyush,revanshu,jasbir"
print(names[0:6])
print(names[7:15])
print(names[16:22])

sample = "textInFile"
sampleLen = len(sample)
print(sampleLen)
print(sample[0:])# will print 0 index to last....
print(sample[:])# will print 0 index to last....
print(sample[0:10])# will print 0 index to (10 - 1) index....
print(sample[0:-1])# will print sample[0:len(sample)-1]....