from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = 0
        for i in arr:
            if i % 2 != 0:
                n += 1
                if n == 3:
                    return True
            else:
                n = 0
        return False

def input_array() -> List[int]:
    user_input = input("Enter array elements separated by spaces: ")
    elements = user_input.split()
    arr = []
    for element in elements:
        arr.append(int(element))
    return arr

a = Solution()
arr = input_array()
result = a.threeConsecutiveOdds(arr)
print("Three consecutive odds:", result)

