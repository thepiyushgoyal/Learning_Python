import os
os.system('cls')

# # PS: Work in DailyPython Folder
# # {
# if (not os.path.exists("28_osModule")):
#     os.mkdir("28_osModule")

# if (not os.path.exists("28_osModule/1 Created")):
#     for i in range(1, 6):
#         os.mkdir(f"28_osModule/{i} Created")

# if (not os.path.exists("28_osModule/1 filed")):
#     for i in range(1, 6):
#         os.rename(f"28_osModule/{i} Created", f"28_osModule/{i} filed")

# folderinDailyPython = os.listdir("28_osModule")
# print(folderinDailyPython)
# #  }
folders = os.listdir("python")
print(folders)

for folder in folders:
    print(os.listdir(f"python/{folder}"))