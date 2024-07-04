import array as arr

arr = [2,5,23,78,34,25,11,77,12,69,65,45,99,8]

print(arr)
n = int(input("Enter a number: "))

for ele in range(len(arr)):
    if n == arr[ele]:
        print("Index: ",ele)
        break
else:
    print("Element not found")
