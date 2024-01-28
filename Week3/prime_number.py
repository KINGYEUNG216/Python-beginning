"""
Prime Number Checker Function

Objective:
Write a function named 'is_prime' to determine whether a given number is a prime number.

Function Parameter:
number (integer): The number to be checked for primality.

Instructions:
- The function should return 'True' if the 'number' is a prime number and 'False' otherwise.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- Consider edge cases, such as when the input is less than 2, which is not a prime number.
- https://mathspar.com/prime-numberst/#how-to-tell-if-a-number-is-prime

Example Test Cases:
1. is_prime(11) should return 'True', as 11 is a prime number.
2. is_prime(4) should return 'False', as 4 is not a prime number.
3. is_prime(2) should return 'True', as 2 is a prime number.
4. is_prime(1) should return 'False', as 1 is not considered a prime number.
"""

#判断一个数是否为素数的一般步骤如下：
#基本条件： 确保要判断的数是大于1的自然数。素数定义为大于1的自然数，因此小于等于1的数不是素数。
#除法检查： 尝试将该数除以2以及从3开始的每个奇数，直到根号下该数为止。如果在这个过程中发现能整除该数，那么它不是素数。这是因为如果一个数可以被大于1且小于它本身的数整除，那么它就不是素数。
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    #用数字除以2看有没有余数
    elif number % 2 == 0:
        return False
    else:
        # 从3开始，每次以2递增，检查是否能整除
        for i in range(3, int(number**0.5) + 1, 2):
        #2是步长为2的意思，使用步长为2的方式，可以跳过所有的偶数，减少不必要的循环。
        #循环的终止条件为 int(n**0.5) + 1 是因为如果一个数不是素数，它的最小非1因子必然小于或等于其平方根。这是一个常用的优化策略，可以减少循环次数。
        #n**0.5是n开根号的意思
            if number % i == 0:
                return False
        return True
     

    # Your code goes here
    # Implement the logic to determine if the number is prime
    # Return True if the number is prime, False otherwise
    pass  # Delete this after implementing some code inside this function


# Test cases
print(is_prime(11))  # Expected output: True
print(is_prime(4))  # Expected output: False
print(is_prime(2))  # Expected output: True
print(is_prime(1))  # Expected output: False
