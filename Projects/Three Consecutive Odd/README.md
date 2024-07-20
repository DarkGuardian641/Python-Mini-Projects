
## Three Consecutive Odds (Leetcode #1550)

Given an integer array `arr` determine if there are three consecutive odd numbers in the array. Return TRUE if such a sequence exists, otherwise return FALSE.

<br>

<p align="center">
  <img src="https://github.com/DarkGuardian641/Python-Mini-Projects/assets/91188597/c94ff2d7-a2e1-427c-9183-4f8eaec7e1b5" alt="image">
</p>

<br>

## 🌟 How it works

- Prompt the user to input array elements separated by spaces.
- Read the input string and split it into a list of strings.
- Convert the list of strings to a list of integers, arr.
- Initialize a counter n to 0.
- Iterate through each element i in arr:
- If i is odd, increment n.
- If n reaches 3, return True.
- If i is even, reset n to 0.
- If the loop completes without finding three consecutive odd numbers, return False.
- Print the result.

<br>

## ✅ Test Cases

![image](https://github.com/DarkGuardian641/Python-Mini-Projects/assets/91188597/257f3cbb-21e1-418e-aca9-4c75b28604b9)

![image](https://github.com/DarkGuardian641/Python-Mini-Projects/assets/91188597/153939a0-a3bd-4cb0-bb06-b8fefa6e47d4)

<br>

## 📜 Conclusion

- The goal of this problem is to determine whether a given integer array contains any sequence of three consecutive odd numbers. 
- The function should iterate through the array and count consecutive odd numbers, resetting the count when an even number is encountered. 
- If the count reaches three at any point, the function should return `True` otherwise, it should return `False`.

<br>

## ⚙️ Prerequisites

Install Python 3 to run the code.

<br>

## 🛠️ How to Run

```python3
  python3 three_consecutive_odd.py
```

<br>

## 📺 Output

![image](https://github.com/DarkGuardian641/Python-Mini-Projects/assets/91188597/f3947608-46da-4897-9597-60f2a3cade67)

<br>

## 🤖 Author
[Atharva Baikar](https://github.com/DarkGuardian641)
<br>
[Akanksha Kanade](https://github.com/CandyBeans1609)
