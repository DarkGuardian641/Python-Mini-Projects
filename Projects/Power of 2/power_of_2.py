def isPowerOfTwo(n):
    if n <= 0:
        return False
       
    x = 1
    while x < n:
        x = x * 2

    if x == n:
        return True
    else:
        return False
        
n = int(input("Enter a number: "))        
result = isPowerOfTwo(n)
print(result)