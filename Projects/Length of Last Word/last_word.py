# Find the length of last word in a string

s = input("Enter a sentence: ")
split_string = s.split()
last_word = split_string[-1]
print(len(last_word))