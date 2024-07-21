import os

# Show all existing folders/ Print folders

folders = os.listdir("Projects\Create Files and Folder\os_module")
print(folders)

print("----------")

# Print all files existing in all folders
for folder in folders:
    print(os.listdir(f"Projects\Create Files and Folder\os_module\{folder}"))
