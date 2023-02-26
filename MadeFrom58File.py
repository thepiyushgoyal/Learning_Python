import os
os.system('cls')
 
import shutil
for file in os.listdir():
    if file != '58_shutilModule.py':
        shutil.copy('58_shutilModule.py','MadeFrom58File.py')
    else:
        print("created")