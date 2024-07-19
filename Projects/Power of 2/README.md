
## Determine if a Number is a Power of Two ([Leetcode - 231](https://leetcode.com/problems/power-of-two/))

Write a function that determines if a given integer is a power of two

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/2df0014b-b46f-4581-bf07-ca04ba87dc66" alt="image">
</p>

<br>

## 🌟 How it works

- The function isPowerOfTwo(n) checks if the number n is a power of two.
- It returns False immediately if n is less than or equal to zero.
- It initializes x to 1 and repeatedly multiplies x by 2 until x is no longer less than n.
- If x equals n after the loop, it returns True; otherwise, it returns False.
- The number n is taken from user input, and the function result is printed.

<br>

## ✅ Test Cases

![image](https://github.com/user-attachments/assets/2ece2b03-cfc1-4092-aca6-f5204beac728)

![image](https://github.com/user-attachments/assets/6612f97d-812d-40a2-9609-ead1d2da1ee6)

![image](https://github.com/user-attachments/assets/d0be745a-1e26-4b04-b90f-37148403cfd7)

<br>

## 📜 Conclusion

The isPowerOfTwo(n) function effectively determines if a given integer is a power of two through a straightforward and iterative approach. By checking the input's validity and multiplying a base value (starting at 1) by 2 until it meets or exceeds the input, the function can accurately identify powers of two. This method ensures that the function can handle both positive and non-positive integers, providing a reliable tool for this specific mathematical check. The user interaction allows for easy testing and validation of various input values, confirming the function's correctness and utility.
<br>

## ⚙️ Prerequisites

Install Python 3 to run the code.

<br>

## 🛠️ How to Run

```python3
  python3 power_of_2.py
```

<br>

## 📺 Output

![image](https://github.com/user-attachments/assets/eae366c4-5147-4e47-ad46-96e5d43efa2a)

<br>

## 🤖 Author
[Atharva Baikar](https://github.com/DarkGuardian641)
