import os
os.system('cls')
 
def greet(fx):
    def mfx(*arg, **kwarg):
        print("Welcome!")
        fx(*arg, **kwarg)
        print("Thanks for running")
    return mfx


@greet
def hello():
    print("hello world")

hello()
# greet(hello())

@greet
def sum(a,b):
    print(a+b)

sum(1,2)
# greet(sum)(1,2)