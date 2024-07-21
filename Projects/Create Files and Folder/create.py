import os

# To create a folder named os_module we use:
# os.mkdir("Projects/Create Files and Folder/os_module")

if(not os.path.exists("os_module")):
    os.mkdir("os_module")

# Create 10 files numbered from 1 to 10

for i in range(0,10):
    os.mkdir(f"Projects/Create Files and Folder/os_module/ File {i+1}")
