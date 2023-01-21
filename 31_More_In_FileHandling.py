import os
os.system('cls')
     
with open("31_More_In_FileHandling.txt","r") as f:
    i = 0
    while True:
        i = i + 1
        line = f.readline()
        if not line:
            break
        m1 = int(line.split(",")[0])
        m2 = int(line.split(",")[1])
        m3 = int(line.split(",")[2])
        print(f"Marks of student {i} in Maths is: {m1}")
        print(f"Marks of student {i} in English is: {m2}")
        print(f"Marks of student {i} in SST is: {m3}")

        print("\n")
        
with open("31_More_In_FileHandling_2.txt","w") as f:
    lines = ['line1','line2','line3']
    for line in lines:
        f.write(line+"\n")