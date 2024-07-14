n = int(input("Enter a number: "))
factorial = 1

while (n>0):
    factorial = factorial * n
    n = n - 1

print("Factorial is", factorial)