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
print(fact(4))
