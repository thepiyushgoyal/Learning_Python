import os
os.system('cls')
 
class animal:
    def __init__(self):
        pass
    def makeSound(self):
        pass

class dog(animal):
    def __init__(self):
        self.name = dog
    def makeSound(self):
        print("bark!")

class cat(animal):
    def __init__(self):
        self.name = cat
    def makeSound(self):
        print("meow!")

c = cat()
d = dog()
c.makeSound()
d.makeSound()