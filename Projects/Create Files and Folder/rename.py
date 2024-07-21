import os

# Renaming Folders:

for i in range(0,10):
    os.rename(f"Projects/Create Files and Folder/os_module/ File {i+1}",
              f"Projects/Create Files and Folder/os_module/ Project {i+1}" )
