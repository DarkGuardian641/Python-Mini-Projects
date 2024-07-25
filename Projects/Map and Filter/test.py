# Square Function (squares the given number)

def square(num):
    return num * num

# Accept numbers from the user

x = int(input("Enter the length of the list: "))

number = []

for i in range(x):
    ele = int(input("Enter a number: "))
    number.append(ele)

print("The list is:", number)

new_list = []

# for item in number:
#     new_list.append(square(item))

# But we can do the same thing using MAP

new_list = list(map(square,number))
print("The squares are: ",new_list)

# Using Filter

def filter_function(a):
    return a > 9 and a < 100

two_digit = list(filter(filter_function, number))
print("Two digit numbers from our original list (Number's list): ",two_digit)