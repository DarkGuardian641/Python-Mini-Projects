a = int(input("Enter a number: "))
def fact(a):

    if ((a==0) or (a==1)):
        return 1
    else:
        return a * fact(a-1)
    
print("Factorial of", a, "is",fact(a))