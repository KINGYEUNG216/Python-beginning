"""
Morse Code Translator Function

Objective:
Write a function named 'morse_translator' that translates a given string into Morse code.

Function Parameter:
text (string): The string to be translated into Morse code.

Instructions:
- Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
- The Morse code for each character should be separated by a space.
- Each word in the string should be separated by a forward slash (/).
- The function should handle both uppercase and lowercase alphabetic characters.
- The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
- Non-alphabetic characters (like numbers or symbols) should not be translated.
- https://en.wikipedia.org/wiki/Morse_code

Example Test Cases:
1. morse_translator("HELLO WORLD") should return the Morse code for the given string.
2. morse_translator("Python") should return the Morse code for the given string.
3. morse_translator("Morse Code") should return the Morse code for the given string.
"""


def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }
 
 #摩斯代码集合
    morse_code_list = []
 #输入的文字间加空格
    words = text.split()
 #循环函数for word是一个任意命名的变量 look through each word in the input text
    for word in words:
        #每个字母对应的摩斯密码数据集
        morse_word = []
        #look through each character in the current word
        for char in word:
            #检查字母（全部变成大写）是否在字典里
            if char.upper() in morse_code_dict:
                #是的话，把每个字母转为摩斯密码
                morse_word.append(morse_code_dict[char.upper()])
        #每个字符的摩尔斯电码之间用空格隔开（join 方法是字符串对象的一个方法，用于将序列中的元素连接成一个字符串）
        morse_code_list.append(" ".join(morse_word))
    #字符串中的每个单词用正斜杠(/)隔开。
    return '/'.join(morse_code_list)



    # Your code goes here
    # Remember to consider both upper and lower case letters, and spaces
    # The function should return the translated Morse code string


# Test cases
print(
    morse_translator("HELLO WORLD")
)  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(
    morse_translator("Morse Code")
)  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
