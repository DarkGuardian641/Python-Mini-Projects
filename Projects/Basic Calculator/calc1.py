num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Division by zero is not allowed"

choice = int(input("Select an operation: \n 1 : Add \n 2 : Sub \n 3 : Mul \n 4 : Div\n"))

if choice == 1:
    num3 = add(num1, num2)
elif choice == 2:
    num3 = sub(num1, num2)
elif choice == 3:
    num3 = mul(num1, num2)
elif choice == 4:
    num3 = div(num1, num2)
else:
    num3 = "Invalid input"

print("Result:", num3)
