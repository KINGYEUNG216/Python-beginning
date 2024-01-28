"""
Factorial Calculator Function

Objective:
Write a function named 'calculate_factorial' to compute the factorial of a number using a for loop.
阶乘是指将一个非负整数 n 与小于或等于 n 的所有正整数相乘的结果。

Function Parameter:
1. number (integer): A non-negative integer for which the factorial is to be calculated.要计算其阶乘的非负整数。

Instructions:
- Use a for loop to calculate the factorial of 'number'.
- Return the factorial result.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. calculate_factorial(5) should return the factorial of 5.
2. calculate_factorial(0) should return 1.
3. calculate_factorial(3) should return the factorial of 3.
4. calculate_factorial(-1) should handle negative input.
"""


def calculate_factorial(number):

 if number < 0:
    print("please enter a non-negative integer ")
    raise ValueError
 
 result = 1
 for i in range(1,number+1):    #range 函数在 Python 中只能用于整数。range 函数的参数和返回值都必须是整数。
    result *= i       #这里的意思是result=result*i相加的结果

 return result
 
    # Your code goes here
    # Implement the factorial calculation using a for loop
    


# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value
