import os
os.system('cls')

# import import_function as fn
# or 
from import_function import fact 
print(fact(5))
# it will first run the statement from import file then run the function of this file

# to avoid this we use 
# if __name =="__main__" # in that file which we are importing 
# the command is in comments please uncomment it to se results