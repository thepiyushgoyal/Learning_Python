import os
os.system('cls')
 
def generator():
    for i in range(500):
        yield i

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
