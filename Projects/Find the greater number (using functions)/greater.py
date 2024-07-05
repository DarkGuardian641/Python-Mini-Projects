a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def check(a,b):
    if a>b:
        print(a, "is greater than ",b)
    elif a<b:
        print(b,"is greater than ",a)
    else:
        print("Both numbers are equal")

check(a,b)