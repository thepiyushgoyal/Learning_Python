import random as rand
import os
# os.system('cls')

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)

def fab(index):
    if (index == 0):
        return 0
    elif (index == 1 or index == -1):
        return 1
    elif(index > 1):
        return fab(index-1) + fab(index-2)
    else:
        return fab(index + 2) - fab(index + 1)


# if __name__=="__main__":
#     print(fact(4))
# after doing it comment-out comment the below statement
# print(fact(4))

def randomNamesGenerator(num,words):
    alphaList = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    alphaLowerlist = alphaList.split(",")
    alphaUpperlist = alphaList.swapcase().split(",")
    randNames = list()
    for i in range(0,num):
        randAlphaS = list()
        for j in range(0,words):
            # randAlphanum = rand.choice(0,25)
            randAlpha = alphaLowerlist[rand.randint(0,25)]
            randAlphaS.append(randAlpha)
            # print(randAlphaS)
        randFourAlphaWord = ""
        rfaw = randFourAlphaWord.join(randAlphaS)
        # print(rfaw)
        randName = alphaUpperlist[rand.randint(0,25)]+rfaw
        # print(randName)
        randNames.append(randName)
    return randNames

# namelist = randomNamesGenerator()
# print(namelist)