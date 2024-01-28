"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""

#思路：遍历文本里的每个字符，识别文本里的大写字母是。。。小写字母是。。。然后数集合里大写字母有多少个，小写字母有多少个
def case_counter(text):
    words = text
    uppercase = []
    lowercase = []
    for char in words:
     if char.isupper():
        uppercase.append(char)
     elif char.islower():
        lowercase.append(char)
    count_uppercase = len(uppercase)
    count_lowercase = len(lowercase)
    print(f"Uppercase letters:{count_uppercase},Lowercase letters:{count_lowercase}")
    
    

    # Your code goes here
    # Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
    pass  # Delete this after implementing some code inside this function.


# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0
