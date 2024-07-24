f = open('Projects\File IO\Myfile.txt','r')

# Read file contents
text = f.read()
print(text)

# Close the file
f.close()