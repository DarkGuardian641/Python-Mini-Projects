class Solution:

    def isPalindrome(self, x: int):
        temp = x
        reverse = 0

        while (x > 0):
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        if(temp == reverse):
            print("It is a Palindrome")

        else:
            print("It is not a Palindrome")

x = int(input("Enter a number: "))

check = Solution()
check.isPalindrome(x)