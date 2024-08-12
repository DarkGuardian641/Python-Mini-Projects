import os

# Select file path
files = os.listdir("Projects\Clear the clutter\Files")

# Renaming all png files
i = 1
for file in files:
    if file.endswith('.png'):
        print(file)
        os.rename(f"Projects\Clear the clutter\Files\{file}", f"Projects\Clear the clutter\Files\{i}.png")
    i = i + 1
