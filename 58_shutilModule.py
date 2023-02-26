import os
os.system('cls')
 
import shutil
for file in os.listdir():
    if file != '58_shutilModule.py':
        shutil.copy('58_shutilModule.py','MadeFrom58File.py')
    else:
        print("created")

# copy2 function is also same - it just copy the meta data of file
# copytree - it is used to copy any directory
# move - it is used to move a file from one to another place by giving src and destination address
# rmtree - used to remove a directory

