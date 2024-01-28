"""
Compound Interest Calculator Function

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.本金
2. r (float): Annual interest rate in decimal.以十进制表示的年利率。
3. n (integer): Number of times interest is compounded per year.每年复利的次数
4. t (integer): Number of years for investment.投资年数

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest. 在这里^是幂运算的意思，一般在python里用**表示；这个公式适用于定期复利，其中利息在每个计息周期内都会与之前的本金和利息相结合。
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""


def compound_interest_calculator(P, r, n, t): 
 #Principal, rate, number of compounding periods, and time must be positive values.数学中大于零的数
 if P <= 0 or r < 0 or n <= 0 or t < 0:
        raise ValueError
 #raise 是一个关键字，用于引发异常。通过 raise 关键字，你可以在代码中显式地触发异常，从而中断正常的程序流程，并且在适当的地方处理这个异常。
 A = P*(1 + r/n)**(n*t)
 return A 





    # Your code goes here
    # Implement the compound interest calculation
    


# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years
